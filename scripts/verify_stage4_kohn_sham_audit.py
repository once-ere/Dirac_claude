#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-30, after the Stage-3 audit program
# scripts/verify_stage3_dark_sector_audit.py (same repository, same licence),
# whose solver, snapshot, unchanged, fresh, prepare-notebook and notebook
# subcommands are reproduced here unchanged in behaviour.
"""Audit steps of the Stage-4 gate (scripts/verify_stage4_kohn_sham.{ps1,sh}).

Both gate twins call this one program, so that the PowerShell and the bash
gate apply exactly the same comparisons.  Standard library only.  Every
subcommand prints stage4_<name>=<value> lines, ends with one
stage4_audit_<subcommand>=OK|FAILED line and exits 0 (OK) or 1 (FAILED);
2 is a usage error.

Subcommands (paths are relative to the current directory, normally the
repository root):

  solver --pin SHA [--vendor DIR]
      vendor/rustSolveIt is a git checkout at exactly SHA, its tracked files
      are unmodified and the two path dependencies
      sundials_rs/crates/{sundials_core,cvode_rs} exist.
  same [--rtol X --atol Y] --pair EXPECTED ACTUAL [--pair ...]
      Every ACTUAL file equals its EXPECTED file byte for byte.  With --rtol
      (and --atol) a .json pair that is not byte-identical may instead be
      equal value by value: same structure, same strings and booleans, and
      numbers within rtol * max(|a|, |b|) + atol; which rule matched is
      printed per pair.
  rust-outputs --committed ROOT --run DIR [--run DIR ...]
      For spectrum, scf, excited, thermo, emt: the committed ROOT/<sub>/ holds
      exactly the files listed in its summary.json ("files", which includes
      summary.json itself; recursive listing), and every run directory
      DIR/<sub>/ holds exactly the same files, each byte-identical to the
      committed one.
  determinism --committed REPORT --fresh REPORT [--full-refined]
      The fresh report of studies/dirac16complex_kohn_sham/tools/compare_runs.py
      has only true checks, the same check names as the committed
      rust/determinism-report.json and the same number of repeat-compared
      files; with --full-refined (the refined tree includes thermo) it must
      also be byte-identical to the committed report, otherwise the refined
      run counts are printed next to the committed ones.
  reference-quick --summary PATH
      A reference-solver summary written by "ks_reference_solver.py --quick":
      quick true, complete true, selfTests present, every run converged and
      none failed.
  checker-report --committed REPORT --fresh REPORT
      The fresh report of scripts/check_dirac16complex_kohn_sham.py (run in
      this gate with --repeat and --refined on the gate's trees) has
      checkCount = number of checks, failedCheckCount 0, only true checks,
      the checks rust_repeat_byte_identity and rust_refined_convergence, the
      same set of check names and the same comparisonsNotRun as the committed
      python-check-report.json.  Byte identity is printed, not required (the
      report records absolute paths in some measurement strings).
  prepare-notebook --source NB --dest NB [--dest NB ...]
      Copy NB with every code cell's outputs removed and execution_count
      null, so that an executed copy can only carry outputs of this run.
  notebook --committed-report JSON --fresh-report JSON [--ignore-key KEY ...]
           [--committed-notebook NB --fresh-notebook NB]
      The notebook report written in this run has verdict SUCCESS and equals
      the committed notebook-report.json in every field except the paths of
      the audited notebook files ("notebook" and executions[].notebook) and
      the dotted keys given with --ignore-key.  With the two notebook options
      it also prints whether the executed copy is byte-identical to the
      committed notebook (information only).
  snapshot --into DIR PATH [PATH ...]
      Copy the files, and every file below a directory PATH (without
      __pycache__), as they are when the gate starts, into DIR.
  unchanged --snapshot DIR [--ignore-json-key KEY ...] PATH [PATH ...]
      Every file named or below a named directory is byte-identical to its
      copy in DIR, and no file appeared or disappeared; a .json file may
      instead differ only in the dotted keys given with --ignore-json-key.
  fresh --since EPOCH FILE [FILE ...]
      Every FILE exists and was modified at or after EPOCH (Unix seconds);
      prints stage4_sha256=<hex>  <FILE> for each.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")
CHECKER_REQUIRED = ("rust_repeat_byte_identity", "rust_refined_convergence")


class AuditFailure(Exception):
    """A failed requirement; the message is printed as stage4_audit_problem."""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    try:
        return json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, ValueError) as error:
        raise AuditFailure(f"{path.as_posix()} is not readable UTF-8 JSON: {error}") from error


def emit(name: str, value) -> None:
    print(f"stage4_{name}={value}")


# ---------------------------------------------------------------------------
# solver (as in the Stage-3 audit)


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
    emit("solver_remote", git_output(["remote", "get-url", "origin"], vendor).strip())
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
# same (byte identity, optionally value by value for JSON)


def values_equal(a, b, path: str, bad: list, rtol: float, atol: float) -> None:
    if isinstance(a, dict) and isinstance(b, dict) and list(a) == list(b):
        for key in a:
            values_equal(a[key], b[key], f"{path}/{key}", bad, rtol, atol)
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for index, (x, y) in enumerate(zip(a, b)):
            values_equal(x, y, f"{path}/{index}", bad, rtol, atol)
    elif isinstance(a, bool) or isinstance(b, bool) or a is None or b is None or isinstance(a, str):
        if a != b:
            bad.append(path)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if math.isnan(a) or math.isnan(b):
            if not (math.isnan(a) and math.isnan(b)):
                bad.append(path)
        elif not abs(a - b) <= rtol * max(abs(a), abs(b)) + atol:
            bad.append(path)
    else:
        bad.append(path)


def cmd_same(arguments) -> list[str]:
    problems = []
    for expected_name, actual_name in arguments.pair:
        expected, actual = Path(expected_name), Path(actual_name)
        if not expected.is_file() or not actual.is_file():
            problems.append(f"missing {expected.as_posix()} or {actual.as_posix()}")
            continue
        if expected.read_bytes() == actual.read_bytes():
            emit("same", f"{actual.as_posix()} byte-identical to {expected.as_posix()} "
                         f"(sha256 {sha256_file(actual)})")
            continue
        if arguments.rtol is None or actual.suffix != ".json":
            problems.append(f"{actual.as_posix()} differs from {expected.as_posix()}")
            continue
        bad: list = []
        values_equal(load_json(expected), load_json(actual), "", bad, arguments.rtol, arguments.atol)
        if bad:
            problems.append(f"{actual.as_posix()} differs from {expected.as_posix()} beyond relative "
                            f"{arguments.rtol:g} / absolute {arguments.atol:g} ({len(bad)} value(s), first {bad[0]})")
        else:
            emit("same", f"{actual.as_posix()} equal to {expected.as_posix()} value by value (relative "
                         f"{arguments.rtol:g}, absolute {arguments.atol:g}), not byte-identical")
    return problems


# ---------------------------------------------------------------------------
# Rust outputs


def tree_files(directory: Path) -> list[str]:
    return sorted(path.relative_to(directory).as_posix() for path in directory.rglob("*") if path.is_file())


def cmd_rust_outputs(arguments) -> list[str]:
    committed = Path(arguments.committed)
    runs = [Path(run) for run in arguments.run]
    problems = []
    total = 0
    for sub in SUBCOMMANDS:
        summary = load_json(committed / sub / "summary.json")
        expected = list(summary.get("files", []))
        if "summary.json" not in expected or len(set(expected)) != len(expected):
            problems.append(f"{committed.as_posix()}/{sub}/summary.json has a malformed files list")
            continue
        present = tree_files(committed / sub)
        if present != sorted(expected):
            problems.append(f"{committed.as_posix()}/{sub}/ holds other files than its summary lists "
                            f"(extra {sorted(set(present) - set(expected))[:5]}, "
                            f"missing {sorted(set(expected) - set(present))[:5]})")
        different = []
        for run in runs:
            directory = run / sub
            if not directory.is_dir():
                problems.append(f"missing run directory {directory.as_posix()}")
                continue
            fresh = tree_files(directory)
            if fresh != sorted(expected):
                problems.append(f"{directory.as_posix()} holds other files than the committed summary lists "
                                f"(extra {sorted(set(fresh) - set(expected))[:5]}, "
                                f"missing {sorted(set(expected) - set(fresh))[:5]})")
            for name in expected:
                reference, candidate = committed / sub / name, directory / name
                if reference.is_file() and candidate.is_file() and reference.read_bytes() != candidate.read_bytes():
                    different.append(candidate.as_posix())
        if different:
            problems.append(f"{sub}: {len(different)} file(s) differ from {committed.as_posix()}/{sub}/, "
                            f"first: {different[0]}")
        else:
            emit(f"rust_outputs_{sub}", f"{len(expected)} files byte-identical in "
                                        f"{', '.join(r.as_posix() for r in runs)} and {committed.as_posix()}/{sub}")
        total += len(expected)
    emit("rust_outputs_compared_files", f"{total} per run, {len(runs)} run(s)")
    return problems


def cmd_determinism(arguments) -> list[str]:
    committed_path, fresh_path = Path(arguments.committed), Path(arguments.fresh)
    committed, fresh = load_json(committed_path), load_json(fresh_path)
    problems = []
    checks = fresh.get("checks", {})
    failed = [name for name, passed in checks.items() if passed is not True]
    if not checks or failed:
        problems.append(f"{fresh_path.as_posix()} failed checks: {failed or 'no checks'}")
    if list(checks) != list(committed.get("checks", {})):
        problems.append(f"{fresh_path.as_posix()} has other checks than {committed_path.as_posix()}")
    fresh_m, committed_m = fresh.get("measurements", {}), committed.get("measurements", {})
    if fresh_m.get("repeatFilesCompared") != committed_m.get("repeatFilesCompared"):
        problems.append(f"repeat files compared {fresh_m.get('repeatFilesCompared')} against the committed "
                        f"{committed_m.get('repeatFilesCompared')}")
    identical = fresh_path.read_bytes() == committed_path.read_bytes()
    emit("determinism_checks", f"{len(checks) - len(failed)}/{len(checks)} true")
    emit("determinism_repeat_files", fresh_m.get("repeatFilesCompared"))
    for key in ("refinedRunsCompared", "refinedLevelsCompared", "refinedMaxRelativeEnergy",
                "refinedMaxRelativeFreeEnergy", "refinedMaxAbsEps"):
        emit(f"determinism_{key}", f"{fresh_m.get(key)} (committed {committed_m.get(key)})")
    emit("determinism_byte_identical_to_committed", "yes" if identical else "no")
    if arguments.full_refined and not identical:
        problems.append(f"{fresh_path.as_posix()} is not byte-identical to {committed_path.as_posix()} although the "
                        f"refined tree is complete (--full-refined)")
    return problems


def cmd_reference_quick(arguments) -> list[str]:
    path = Path(arguments.summary)
    summary = load_json(path)
    problems = []
    if summary.get("quick") is not True:
        problems.append(f"{path.as_posix()} is not a --quick summary")
    if summary.get("complete") is not True:
        problems.append(f"{path.as_posix()} is not complete")
    tests = summary.get("selfTests")
    if not isinstance(tests, dict) or not tests:
        problems.append(f"{path.as_posix()} has no selfTests (the --quick self-tests did not run)")
    else:
        emit("reference_quick_self_tests", ",".join(sorted(tests)))
        emit("reference_quick_analytic_max_error", tests.get("analyticMaxError"))
    runs = summary.get("runs", [])
    bad = [run.get("label") for run in runs if not run.get("converged") or run.get("failed")]
    if not runs or bad:
        problems.append(f"{path.as_posix()}: runs {len(runs)}, not converged or failed: {bad}")
    emit("reference_quick_runs", f"{len(runs)} runs, all converged: {'yes' if runs and not bad else 'no'}")
    return problems


def cmd_checker_report(arguments) -> list[str]:
    committed_path, fresh_path = Path(arguments.committed), Path(arguments.fresh)
    committed, fresh = load_json(committed_path), load_json(fresh_path)
    problems = []
    checks = fresh.get("checks", {})
    failed = [name for name, passed in checks.items() if passed is not True]
    if not checks:
        problems.append(f"{fresh_path.as_posix()} has no checks")
    if failed:
        problems.append(f"{fresh_path.as_posix()} failed checks: {', '.join(failed)}")
    if fresh.get("checkCount") != len(checks) or fresh.get("failedCheckCount") != len(failed) or failed:
        problems.append(f"{fresh_path.as_posix()} checkCount/failedCheckCount are "
                        f"{fresh.get('checkCount')}/{fresh.get('failedCheckCount')}, expected {len(checks)}/0")
    missing = [name for name in CHECKER_REQUIRED if name not in checks]
    if missing:
        problems.append(f"{fresh_path.as_posix()} lacks {', '.join(missing)} (run the checker with --repeat and --refined)")
    reference_checks = committed.get("checks", {})
    if set(checks) != set(reference_checks):
        problems.append(f"{fresh_path.as_posix()} has other checks than {committed_path.as_posix()}: only fresh "
                        f"{sorted(set(checks) - set(reference_checks))[:5]}, only committed "
                        f"{sorted(set(reference_checks) - set(checks))[:5]}")
    if fresh.get("comparisonsNotRun") != committed.get("comparisonsNotRun"):
        problems.append(f"comparisonsNotRun {fresh.get('comparisonsNotRun')} differ from the committed "
                        f"{committed.get('comparisonsNotRun')}")
    emit("checker_report", f"{len(checks) - len(failed)}/{len(checks)} checks true (committed "
                           f"{committed.get('checkCount')}/{committed.get('checkCount')} with "
                           f"{committed.get('failedCheckCount')} failed)")
    emit("checker_report_order_equal_to_committed", "yes" if list(checks) == list(reference_checks) else "no")
    emit("checker_report_byte_identical_to_committed",
         "yes" if fresh_path.read_bytes() == committed_path.read_bytes() else "no")
    return problems


# ---------------------------------------------------------------------------
# notebooks (as in the Stage-3 audit, plus --ignore-key)


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


def drop_key(document, dotted: str) -> None:
    parts = dotted.split(".")
    for part in parts[:-1]:
        if not isinstance(document, dict) or part not in document:
            return
        document = document[part]
    if isinstance(document, dict):
        document.pop(parts[-1], None)


def without_notebook_paths(report: dict, ignored) -> dict:
    report = json.loads(json.dumps(report))
    report.pop("notebook", None)
    for execution in report.get("executions", []):
        if isinstance(execution, dict):
            execution.pop("notebook", None)
    for key in ignored:
        drop_key(report, key)
    return report


def cmd_notebook(arguments) -> list[str]:
    fresh_path, committed_path = Path(arguments.fresh_report), Path(arguments.committed_report)
    fresh, reference = load_json(fresh_path), load_json(committed_path)
    problems = []
    if fresh.get("verdict") != "SUCCESS":
        problems.append(f"{fresh_path.as_posix()} verdict is {fresh.get('verdict')!r}")
    left = without_notebook_paths(fresh, arguments.ignore_key)
    right = without_notebook_paths(reference, arguments.ignore_key)
    if left != right:
        keys = sorted(key for key in set(left) | set(right) if left.get(key) != right.get(key))
        problems.append(f"{fresh_path.as_posix()} differs from {committed_path.as_posix()} in {keys}")
    else:
        gauntlet = fresh.get("gauntlet", {}) if isinstance(fresh.get("gauntlet"), dict) else {}
        emit("notebook_report",
             f"equal to the committed report except the notebook paths: "
             f"{len(fresh.get('executions', []))} executions, gauntlet "
             f"{gauntlet.get('passed')}/{gauntlet.get('count')}, "
             f"{len(fresh.get('figures', []))} figures with the committed sha256")
    if arguments.committed_notebook and arguments.fresh_notebook:
        same = Path(arguments.committed_notebook).read_bytes() == Path(arguments.fresh_notebook).read_bytes()
        emit("notebook_executed_copy_byte_identical_to_committed", "yes" if same else "no")
    return problems


# ---------------------------------------------------------------------------
# snapshot / unchanged / fresh (as in the Stage-3 audit)


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
        print(f"stage4_sha256={sha256_file(path)}  {path.as_posix()}")
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    solver = commands.add_parser("solver")
    solver.add_argument("--pin", required=True)
    solver.add_argument("--vendor", default="vendor/rustSolveIt")
    same = commands.add_parser("same")
    same.add_argument("--pair", nargs=2, action="append", required=True, metavar=("EXPECTED", "ACTUAL"))
    same.add_argument("--rtol", type=float, default=None)
    same.add_argument("--atol", type=float, default=0.0)
    outputs = commands.add_parser("rust-outputs")
    outputs.add_argument("--committed", required=True)
    outputs.add_argument("--run", action="append", required=True)
    determinism = commands.add_parser("determinism")
    determinism.add_argument("--committed", required=True)
    determinism.add_argument("--fresh", required=True)
    determinism.add_argument("--full-refined", action="store_true")
    reference = commands.add_parser("reference-quick")
    reference.add_argument("--summary", required=True)
    checker = commands.add_parser("checker-report")
    checker.add_argument("--committed", required=True)
    checker.add_argument("--fresh", required=True)
    prepare = commands.add_parser("prepare-notebook")
    prepare.add_argument("--source", required=True)
    prepare.add_argument("--dest", action="append", required=True)
    notebook = commands.add_parser("notebook")
    notebook.add_argument("--committed-report", required=True)
    notebook.add_argument("--fresh-report", required=True)
    notebook.add_argument("--ignore-key", action="append", default=[])
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
        "solver": cmd_solver, "same": cmd_same, "rust-outputs": cmd_rust_outputs,
        "determinism": cmd_determinism, "reference-quick": cmd_reference_quick,
        "checker-report": cmd_checker_report, "prepare-notebook": cmd_prepare_notebook,
        "notebook": cmd_notebook, "snapshot": cmd_snapshot, "unchanged": cmd_unchanged, "fresh": cmd_fresh,
    }
    try:
        problems = handlers[arguments.command](arguments)
    except AuditFailure as error:
        problems = [str(error)]
    for problem in problems:
        print(f"stage4_audit_problem={problem}")
    print(f"stage4_audit_{arguments.command.replace('-', '_')}={'FAILED' if problems else 'OK'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
