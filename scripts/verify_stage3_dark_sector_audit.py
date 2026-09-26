#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-25.
"""Audit steps of the Stage-3 gate (scripts/verify_stage3_dark_sector.{ps1,sh}).

Both gate twins call this one program, so that the PowerShell and the bash
gate apply exactly the same comparisons.  Standard library only.  Every
subcommand prints stage3_<name>=<value> lines, ends with one
stage3_audit_<subcommand>=OK|FAILED line and exits 0 (OK) or 1 (FAILED);
2 is a usage error.

Subcommands (paths are relative to the current directory, normally the
repository root):

  solver --pin SHA [--vendor DIR]
      vendor/rustSolveIt is a git checkout at exactly SHA, its tracked files
      are unmodified (git status --porcelain is empty) and the two path
      dependencies sundials_rs/crates/{sundials_core,cvode_rs} exist.
  outputs --committed ROOT --run DIR [--run DIR ...]
      For exp1..exp5: every run directory DIR/expN holds exactly the files
      listed in ROOT/expN/summary.json ("files", which includes summary.json
      itself), and every one of them is byte-identical to ROOT/expN/<file>
      (hence also to the same file of every other run).
  analysis --committed ROOT --fresh DIR
      The EXP-3 analysis files fits.json, fits_scan.csv, fits_mu_scan.csv of
      DIR/exp3 equal ROOT/exp3: byte for byte, or else value by value
      (relative 1e-6, absolute 1e-8; Nelder-Mead "iterations" not compared),
      the rule of the Jupyter notebook's compare_files_numerically (numpy
      builds differ in the last digits of these numpy-written files).
      fits.json must have verdict SUCCESS and only true validation checks.
  reports --committed ROOT --fresh DIR
      For exp1..exp5: DIR/expN/python-check-report.json (written by the
      checker in this run) has schemaVersion 1, verdict SUCCESS, only true
      checks, failedCheckCount 0, the checks repeatByteIdentity and
      refinedConvergence, exactly the check names (in the same order) and
      the fixture hash of the committed ROOT/expN/python-check-report.json,
      and that fixture hash equals the sha256 of the algebra fixture.
      Whether the report is also byte-identical to the committed one is
      printed (it is on the platform that produced the committed files; the
      measurements are float64 results of numpy linear algebra, whose last
      digits depend on the numpy/BLAS build).
  numerics-summary --committed ROOT --fresh DIR
      DIR/numerics-summary.json (built from the fresh outputs in this run)
      has verdict SUCCESS and the same totals (check counts, failures,
      solver steps, RHS evaluations) as ROOT/numerics-summary.json; byte
      identity is printed.
  prepare-notebook --source NB --dest NB [--dest NB ...]
      Copy NB with every code cell's outputs removed and execution_count
      null, so that an executed copy can only carry outputs of this run.
  notebook --committed-report JSON --fresh-report JSON
           [--committed-notebook NB --fresh-notebook NB]
      The notebook report written in this run by notebooks/check_notebook.py
      has verdict SUCCESS and equals the committed notebook-report.json in
      every field except the paths of the audited notebook files (cell
      counts, rule results, the 71 gauntlet results with their printed
      details, and the sha256 of the 17 figures).  With the two notebook
      options it also prints whether the executed copy is byte-identical to
      the committed notebook (the simulator path it prints is platform
      specific, so this is information, not a requirement).
  snapshot --into DIR PATH [PATH ...]
      Copy the files, and every file below a directory PATH (without
      __pycache__), as they are when the gate starts, into DIR, keeping
      their relative paths.
  unchanged --snapshot DIR [--ignore-json-key KEY ...] PATH [PATH ...]
      Every file named or below a named directory is byte-identical to its
      copy in DIR, and no file appeared or disappeared; a .json file may
      instead differ only in the dotted keys given with --ignore-json-key.
  fresh --since EPOCH FILE [FILE ...]
      Every FILE exists and was modified at or after EPOCH (Unix seconds);
      prints stage3_sha256=<hex>  <FILE> for each.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path

EXPERIMENTS = ("exp1", "exp2", "exp3", "exp4", "exp5")
ANALYSIS_FILES = ("fits.json", "fits_scan.csv", "fits_mu_scan.csv")
REQUIRED_OPTIONAL_CHECKS = ("repeatByteIdentity", "refinedConvergence")
FIXTURE = Path("artifacts/dirac16complex/arbitrary-field/algebra-fixture.json")
NUMERIC_RTOL = 1e-6
NUMERIC_ATOL = 1e-8


class AuditFailure(Exception):
    """A failed requirement; the message is printed as stage3_audit_problem."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_json(path: Path):
    try:
        return json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, ValueError) as error:
        raise AuditFailure(f"{path.as_posix()} is not readable UTF-8 JSON: {error}") from error


def emit(name: str, value) -> None:
    print(f"stage3_{name}={value}")


# ---------------------------------------------------------------------------
# solver


def git_output(arguments, directory: Path) -> str:
    try:
        completed = subprocess.run(["git", "-C", str(directory), *arguments],
                                   capture_output=True, text=True, encoding="utf-8",
                                   errors="replace", check=False)
    except OSError as error:
        raise AuditFailure(f"git could not be started: {error}") from error
    if completed.returncode != 0:
        raise AuditFailure(f"git {' '.join(arguments)} failed in {directory.as_posix()} "
                           f"(exit {completed.returncode}): {completed.stderr.strip()}")
    return completed.stdout


def cmd_solver(arguments) -> list[str]:
    vendor = Path(arguments.vendor)
    problems = []
    if not (vendor / ".git").exists():
        raise AuditFailure(f"{vendor.as_posix()} is not a git checkout (run scripts/setup_solver)")
    head = git_output(["rev-parse", "HEAD"], vendor).strip()
    emit("solver_commit", head)
    if head != arguments.pin:
        problems.append(f"{vendor.as_posix()} is at {head}, expected the pinned {arguments.pin}")
    remote = git_output(["remote", "get-url", "origin"], vendor).strip()
    emit("solver_remote", remote)
    status = git_output(["status", "--porcelain", "--untracked-files=no"], vendor)
    modified = [line for line in status.splitlines() if line.strip()]
    emit("solver_modified_tracked_files", len(modified))
    if modified:
        problems.append(f"{vendor.as_posix()} has {len(modified)} modified tracked file(s), "
                        f"first: {modified[0].strip()}")
    for crate in ("sundials_core", "cvode_rs"):
        manifest = vendor / "sundials_rs" / "crates" / crate / "Cargo.toml"
        if not manifest.is_file():
            problems.append(f"missing {manifest.as_posix()}")
    return problems


# ---------------------------------------------------------------------------
# Rust outputs


def cmd_outputs(arguments) -> list[str]:
    committed = Path(arguments.committed)
    runs = [Path(run) for run in arguments.run]
    problems = []
    total = 0
    for experiment in EXPERIMENTS:
        summary = load_json(committed / experiment / "summary.json")
        expected = list(summary.get("files", []))
        if "summary.json" not in expected or len(set(expected)) != len(expected):
            problems.append(f"{committed.as_posix()}/{experiment}/summary.json has a malformed files list")
            continue
        reference = {}
        for name in expected:
            path = committed / experiment / name
            if not path.is_file():
                problems.append(f"committed file missing: {path.as_posix()}")
                continue
            reference[name] = path.read_bytes()
        different = []
        for run in runs:
            directory = run / experiment
            if not directory.is_dir():
                problems.append(f"missing run directory {directory.as_posix()}")
                continue
            present = sorted(entry.name for entry in directory.iterdir())
            if present != sorted(expected):
                extra = sorted(set(present) - set(expected))
                missing = sorted(set(expected) - set(present))
                problems.append(f"{directory.as_posix()} holds other files than the committed "
                                f"summary lists (extra {extra}, missing {missing})")
            for name, data in reference.items():
                path = directory / name
                if path.is_file() and path.read_bytes() != data:
                    different.append(path.as_posix())
        if different:
            problems.append(f"{experiment}: {len(different)} file(s) differ from "
                            f"{committed.as_posix()}/{experiment}/, first: {different[0]}")
        else:
            emit(f"outputs_{experiment}",
                 f"{len(expected)} files byte-identical in {', '.join(r.as_posix() for r in runs)} "
                 f"and {committed.as_posix()}/{experiment}")
        total += len(expected)
    emit("outputs_compared_files", f"{total} per run, {len(runs)} runs")
    return problems


# ---------------------------------------------------------------------------
# EXP-3 analysis files


def numbers_equal(a, b, path: str, bad: list) -> None:
    if isinstance(a, dict) and isinstance(b, dict) and list(a) == list(b):
        for key in a:
            numbers_equal(a[key], b[key], f"{path}/{key}", bad)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for index, (x, y) in enumerate(zip(a, b)):
            numbers_equal(x, y, f"{path}/{index}", bad)
    elif isinstance(a, bool) or isinstance(b, bool) or a is None or b is None or isinstance(a, str):
        if a != b:
            bad.append(path)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if path.endswith("/iterations"):
            return
        if math.isnan(a) or math.isnan(b):
            if not (math.isnan(a) and math.isnan(b)):
                bad.append(path)
        elif not abs(a - b) <= NUMERIC_RTOL * max(abs(a), abs(b)) + NUMERIC_ATOL:
            bad.append(path)
    else:
        bad.append(path)


def read_csv_columns(path: Path):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        raise AuditFailure(f"{path.as_posix()} is empty")
    return rows[0], [[float(value) for value in row] for row in rows[1:]]


def csv_equal(fresh: Path, committed: Path) -> list:
    header_a, rows_a = read_csv_columns(fresh)
    header_b, rows_b = read_csv_columns(committed)
    if header_a != header_b or len(rows_a) != len(rows_b):
        return ["header or row count"]
    bad = []
    for index, (row_a, row_b) in enumerate(zip(rows_a, rows_b)):
        if len(row_a) != len(row_b):
            bad.append(f"row {index}")
            continue
        for column, x, y in zip(header_a, row_a, row_b):
            if math.isnan(x) or math.isnan(y):
                if not (math.isnan(x) and math.isnan(y)):
                    bad.append(f"row {index} {column}")
            elif not abs(x - y) <= NUMERIC_RTOL * max(abs(x), abs(y)) + NUMERIC_ATOL:
                bad.append(f"row {index} {column}")
    return bad


def cmd_analysis(arguments) -> list[str]:
    committed = Path(arguments.committed) / "exp3"
    fresh = Path(arguments.fresh) / "exp3"
    problems = []
    fits = load_json(fresh / "fits.json")
    checks = fits.get("validation", {}).get("checks", {})
    if fits.get("verdict") != "SUCCESS" or not checks or not all(value is True for value in checks.values()):
        problems.append(f"{(fresh / 'fits.json').as_posix()} is not a successful analysis "
                        f"(verdict {fits.get('verdict')!r})")
    else:
        emit("analysis_validation_checks", f"{len(checks)}/{len(checks)} true")
    for name in ANALYSIS_FILES:
        fresh_path, committed_path = fresh / name, committed / name
        if not fresh_path.is_file() or not committed_path.is_file():
            problems.append(f"missing {fresh_path.as_posix()} or {committed_path.as_posix()}")
            continue
        if fresh_path.read_bytes() == committed_path.read_bytes():
            emit(f"analysis_{name}", "byte-identical to the committed file")
            continue
        if name.endswith(".json"):
            bad = []
            numbers_equal(load_json(fresh_path), load_json(committed_path), "", bad)
        else:
            bad = csv_equal(fresh_path, committed_path)
        if bad:
            problems.append(f"{fresh_path.as_posix()} differs from {committed_path.as_posix()} "
                            f"beyond relative {NUMERIC_RTOL:g} / absolute {NUMERIC_ATOL:g} "
                            f"({len(bad)} value(s), first {bad[0]})")
        else:
            emit(f"analysis_{name}",
                 f"equal to the committed file value by value (relative {NUMERIC_RTOL:g}, "
                 f"absolute {NUMERIC_ATOL:g}), not byte-identical")
    return problems


# ---------------------------------------------------------------------------
# checker reports


def cmd_reports(arguments) -> list[str]:
    committed = Path(arguments.committed)
    fresh = Path(arguments.fresh)
    fixture_hash = sha256_file(FIXTURE)
    problems = []
    total = 0
    for experiment in EXPERIMENTS:
        fresh_path = fresh / experiment / "python-check-report.json"
        committed_path = committed / experiment / "python-check-report.json"
        report = load_json(fresh_path)
        reference = load_json(committed_path)
        checks = report.get("checks")
        label = fresh_path.as_posix()
        if report.get("schemaVersion") != 1:
            problems.append(f"{label} schemaVersion is not 1")
            continue
        if not isinstance(checks, dict) or not checks:
            problems.append(f"{label} has no non-empty checks object")
            continue
        failed = [name for name, value in checks.items() if value is not True]
        if failed:
            problems.append(f"{label} failed checks: {','.join(failed)}")
        if report.get("verdict") != "SUCCESS" or report.get("failedCheckCount") != 0 \
                or report.get("checkCount") != len(checks):
            problems.append(f"{label} verdict/counts are not SUCCESS/0/{len(checks)}")
        missing = [name for name in REQUIRED_OPTIONAL_CHECKS if name not in checks]
        if missing:
            problems.append(f"{label} lacks {','.join(missing)} (run the checker with --repeat and --refined)")
        if list(checks) != list(reference.get("checks", {})):
            problems.append(f"{label} has other checks than the committed {committed_path.as_posix()} "
                            f"({len(checks)} against {len(reference.get('checks', {}))})")
        if report.get("fixtureSha256") != fixture_hash or reference.get("fixtureSha256") != fixture_hash:
            problems.append(f"{label} or the committed report records another fixture hash than "
                            f"sha256({FIXTURE.as_posix()}) = {fixture_hash}")
        identical = fresh_path.read_bytes() == committed_path.read_bytes()
        detail = ""
        if not identical:
            fresh_m, ref_m = report.get("measurements", {}), reference.get("measurements", {})
            changed = [key for key in ref_m if fresh_m.get(key) != ref_m.get(key)]
            detail = f" (measurements differing in the last digits: {','.join(changed) or 'none'})"
        emit(f"report_{experiment}",
             f"{len(checks) - len(failed)}/{len(checks)} checks true, including "
             f"{' and '.join(REQUIRED_OPTIONAL_CHECKS)}; byte-identical to the committed report: "
             f"{'yes' if identical else 'no'}{detail}")
        total += len(checks)
    emit("report_total_checks", total)
    return problems


def cmd_numerics_summary(arguments) -> list[str]:
    fresh_path = Path(arguments.fresh) / "numerics-summary.json"
    committed_path = Path(arguments.committed) / "numerics-summary.json"
    fresh, reference = load_json(fresh_path), load_json(committed_path)
    problems = []
    if fresh.get("verdict") != "SUCCESS":
        problems.append(f"{fresh_path.as_posix()} verdict is {fresh.get('verdict')!r}")
    if fresh.get("totals") != reference.get("totals"):
        problems.append(f"{fresh_path.as_posix()} totals {fresh.get('totals')} differ from the "
                        f"committed {reference.get('totals')}")
    else:
        emit("numerics_summary_totals", json.dumps(fresh.get("totals"), sort_keys=True))
    emit("numerics_summary_byte_identical",
         "yes" if fresh_path.read_bytes() == committed_path.read_bytes() else "no")
    return problems


# ---------------------------------------------------------------------------
# notebooks


def cmd_prepare_notebook(arguments) -> list[str]:
    source = Path(arguments.source)
    notebook = load_json(source)
    cleared = 0
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
            cleared += 1
    if not cleared:
        raise AuditFailure(f"{source.as_posix()} has no code cells")
    text = json.dumps(notebook, indent=1, ensure_ascii=False) + "\n"
    for name in arguments.dest:
        destination = Path(name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8", newline="\n")
        emit("notebook_prepared", f"{destination.as_posix()} ({cleared} code cells cleared)")
    return []


def without_notebook_paths(report: dict) -> dict:
    report = json.loads(json.dumps(report))
    report.pop("notebook", None)
    for execution in report.get("executions", []):
        if isinstance(execution, dict):
            execution.pop("notebook", None)
    return report


def cmd_notebook(arguments) -> list[str]:
    fresh_path, committed_path = Path(arguments.fresh_report), Path(arguments.committed_report)
    fresh, reference = load_json(fresh_path), load_json(committed_path)
    problems = []
    if fresh.get("verdict") != "SUCCESS":
        problems.append(f"{fresh_path.as_posix()} verdict is {fresh.get('verdict')!r}")
    left, right = without_notebook_paths(fresh), without_notebook_paths(reference)
    if left != right:
        keys = sorted(key for key in set(left) | set(right) if left.get(key) != right.get(key))
        problems.append(f"{fresh_path.as_posix()} differs from {committed_path.as_posix()} in {keys}")
    else:
        gauntlet = fresh.get("gauntlet", {})
        emit("notebook_report",
             f"equal to the committed report except the notebook paths: "
             f"{len(fresh.get('executions', []))} executions, gauntlet "
             f"{gauntlet.get('passed')}/{gauntlet.get('count')}, "
             f"{len(fresh.get('figures', []))} figures with the committed sha256")
    if arguments.committed_notebook and arguments.fresh_notebook:
        same = Path(arguments.committed_notebook).read_bytes() == Path(arguments.fresh_notebook).read_bytes()
        emit("notebook_executed_copy_byte_identical_to_committed", "yes" if same else "no")
    return problems


def expand(names, base: Path | None = None) -> list[str]:
    """Files named, and every file below a named directory (no __pycache__),
    as relative POSIX paths; the directories are looked up below base."""
    files = []
    for name in names:
        root = (base / name) if base is not None else Path(name)
        if root.is_dir():
            for path in sorted(root.rglob("*")):
                if path.is_file() and "__pycache__" not in path.parts:
                    relative = path.relative_to(base) if base is not None else path
                    files.append(relative.as_posix())
        else:
            files.append(Path(name).as_posix())
    return files


def cmd_snapshot(arguments) -> list[str]:
    target = Path(arguments.into)
    files = expand(arguments.files)
    for name in files:
        source = Path(name)
        if not source.is_file():
            raise AuditFailure(f"cannot snapshot missing file {source.as_posix()}")
        destination = target / source
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    emit("snapshot", f"{len(files)} files copied into {target.as_posix()}")
    return []


def drop_key(document, dotted: str) -> None:
    parts = dotted.split(".")
    for part in parts[:-1]:
        if not isinstance(document, dict) or part not in document:
            return
        document = document[part]
    if isinstance(document, dict):
        document.pop(parts[-1], None)


def cmd_unchanged(arguments) -> list[str]:
    snapshot = Path(arguments.snapshot)
    problems = []
    identical = 0
    files = sorted(set(expand(arguments.files)) | set(expand(arguments.files, base=snapshot)))
    for name in files:
        current, before = Path(name), snapshot / name
        if not before.is_file():
            problems.append(f"{current.as_posix()} appeared during this run (not in the snapshot)")
            continue
        if not current.is_file():
            problems.append(f"{current.as_posix()} was deleted during this run")
            continue
        if current.read_bytes() == before.read_bytes():
            identical += 1
            continue
        if name.endswith(".json") and arguments.ignore_json_key:
            left, right = load_json(current), load_json(before)
            for key in arguments.ignore_json_key:
                drop_key(left, key)
                drop_key(right, key)
            if left == right:
                emit("unchanged_modulo_keys", f"{current.as_posix()} (ignored: {','.join(arguments.ignore_json_key)})")
                identical += 1
                continue
        problems.append(f"{current.as_posix()} was changed by this run (it differs from the version "
                        f"on disk when the gate started)")
    emit("unchanged_files", f"{identical}/{len(files)} byte-identical to the snapshot taken at the gate start")
    return problems


def cmd_fresh(arguments) -> list[str]:
    problems = []
    for name in arguments.files:
        path = Path(name)
        if not path.is_file():
            problems.append(f"missing {path.as_posix()}")
            continue
        if int(path.stat().st_mtime) < arguments.since:
            problems.append(f"{path.as_posix()} was not rewritten by this run")
            continue
        print(f"stage3_sha256={sha256_file(path)}  {path.as_posix()}")
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    solver = commands.add_parser("solver")
    solver.add_argument("--pin", required=True)
    solver.add_argument("--vendor", default="vendor/rustSolveIt")
    outputs = commands.add_parser("outputs")
    outputs.add_argument("--committed", required=True)
    outputs.add_argument("--run", action="append", required=True)
    for name in ("analysis", "reports", "numerics-summary"):
        sub = commands.add_parser(name)
        sub.add_argument("--committed", required=True)
        sub.add_argument("--fresh", required=True)
    prepare = commands.add_parser("prepare-notebook")
    prepare.add_argument("--source", required=True)
    prepare.add_argument("--dest", action="append", required=True)
    notebook = commands.add_parser("notebook")
    notebook.add_argument("--committed-report", required=True)
    notebook.add_argument("--fresh-report", required=True)
    notebook.add_argument("--committed-notebook")
    notebook.add_argument("--fresh-notebook")
    snapshot = commands.add_parser("snapshot")
    snapshot.add_argument("--into", required=True)
    snapshot.add_argument("files", nargs="+")
    unchanged = commands.add_parser("unchanged")
    unchanged.add_argument("--snapshot", required=True)
    unchanged.add_argument("--ignore-json-key", action="append", default=[])
    unchanged.add_argument("files", nargs="+")
    fresh = commands.add_parser("fresh")
    fresh.add_argument("--since", type=int, required=True)
    fresh.add_argument("files", nargs="+")
    arguments = parser.parse_args(argv)

    handlers = {
        "solver": cmd_solver, "outputs": cmd_outputs, "analysis": cmd_analysis,
        "reports": cmd_reports, "numerics-summary": cmd_numerics_summary,
        "prepare-notebook": cmd_prepare_notebook, "notebook": cmd_notebook,
        "snapshot": cmd_snapshot, "unchanged": cmd_unchanged, "fresh": cmd_fresh,
    }
    try:
        problems = handlers[arguments.command](arguments)
    except AuditFailure as error:
        problems = [str(error)]
    for problem in problems:
        print(f"stage3_audit_problem={problem}")
    print(f"stage3_audit_{arguments.command.replace('-', '_')}={'FAILED' if problems else 'OK'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
