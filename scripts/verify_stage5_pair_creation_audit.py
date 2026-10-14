#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-10-14, after the Stage-4 audit program
# scripts/verify_stage4_kohn_sham_audit.py (same repository, same licence),
# whose rust-run, same, rust-outputs, snapshot, unchanged and fresh
# subcommands are reproduced here with the same behaviour (rust-run and
# rust-outputs generalised to the Stage-5 subcommand pairs and to --quick
# runs).  Standard library only.
"""Audit steps of the Stage-5 gate (scripts/verify_stage5_pair_creation.{ps1,sh}).

Both gate twins call this one program, so that the PowerShell and the bash
gate apply exactly the same comparisons.  Every subcommand prints
stage5_<name>=<value> lines, ends with one stage5_audit_<subcommand>=OK|FAILED
line and exits 0 (OK) or 1 (FAILED); 2 is a usage error.

Subcommands (paths are relative to the current directory, normally the
repository root):

  rust-run --binary PATH --log-prefix PREFIX [--sequential]
           --job SUB OUTPUT canonical|refined|quick [--job ...]
      Run the Rust binary once per job ("<binary> SUB [--refined|--quick]
      --output OUTPUT"), each job's stdout and stderr in its own log
      PREFIX-<mode>-SUB.log.  By default all jobs run as concurrent processes;
      with --sequential one after another in the order given.  Every job must
      exit 0 with the last stdout line SUCCESS; the first failure stops the
      remaining jobs.  SUB is one of spectrum, scf, excited, thermo, emt, pairs.
  same [--rtol X --atol Y] --pair EXPECTED ACTUAL [--pair ...]
      Every ACTUAL file equals its EXPECTED file byte for byte.  With --rtol
      (and --atol) a .json pair that is not byte-identical may instead be
      equal value by value (same structure, strings and booleans; numbers
      within rtol * max(|a|, |b|) + atol); which rule matched is printed.
  rust-outputs --committed ROOT --run DIR [--run DIR ...] --sub SUB [--sub ...]
      For every SUB: the committed ROOT/<SUB>/ holds exactly the files listed
      in its summary.json ("files", which includes summary.json itself), and
      every run directory DIR/<SUB>/ holds exactly the same files, each
      byte-identical to the committed one.
  report --fresh REPORT [--committed REPORT] [--committed-optional]
         [--require-check NAME ...]
      A JSON report with "checks" (a {name: bool} map) written in this run:
      at least one check, every check true, checkCount / failedCheckCount
      consistent where present, every --require-check present; and, against
      the committed report: the same set of check names and the same
      comparisonsNotRun.  With --committed-optional an absent committed
      report is reported (stage5_report_committed=ABSENT) instead of failing.
      Byte identity with the committed report is printed, not required.
  reference-quick --summary PATH
      A summary written by "ks_reference_pairs.py --quick": quick true,
      complete true, at least one run, no pending run and failedOther empty
      (failed controls are expected and only counted).
  reference-reproduce --committed DIR --output DIR [--max-configs K]
                      [--workers W] [--python EXE] [--log PATH]
      Re-run committed reference pairs runs with scripts/ks_reference_pairs.py
      ("--runs LABELS --output DIR") and compare them byte for byte.  The runs
      are chosen from the committed DIR/reference-pairs-summary.json: per
      field (d16c, then d16c00), the first configuration of the order
      N = 8, lambda = 0, T = 0, |m| = 1 then |m| = 3 whose plusM AND minusM
      records are converged and not failed; at most K configurations
      (default 2), both universes of each.  Every file of each committed run
      directory DIR/<label>/ must exist in OUTPUT/<label>/ with the same
      bytes (and no other file), and each fresh summary record must equal the
      committed one.
  tree-same --committed DIR --fresh DIR
      The two directories hold the same files (recursive, no __pycache__),
      each byte-identical.
  snapshot --into DIR PATH [PATH ...]
      Copy the files, and every file below a directory PATH (without
      __pycache__), as they are when the gate starts, into DIR.
  unchanged --snapshot DIR [--ignore-json-key KEY ...] PATH [PATH ...]
      Every file named or below a named directory is byte-identical to its
      copy in DIR, and no file appeared or disappeared; a .json file may
      instead differ only in the dotted keys given with --ignore-json-key.
  fresh --since EPOCH FILE [FILE ...]
      Every FILE exists and was modified at or after EPOCH (Unix seconds);
      prints stage5_sha256=<hex>  <FILE> for each.
  wolfram-log --log PATH
      The log of a Wolfram step does not contain "Failed to open file"
      (wolframscript prints it, and may still exit 0, when the -file script
      or a file it loads cannot be opened).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt", "pairs")
MODES = ("canonical", "refined", "quick")
MODE_FLAG = {"canonical": [], "refined": ["--refined"], "quick": ["--quick"]}
REFERENCE_SUMMARY = "reference-pairs-summary.json"
REFERENCE_RUNNER = "scripts/ks_reference_pairs.py"
REPRODUCTION_FIELDS = ("d16c", "d16c00")
REPRODUCTION_CONFIGS = ("m1_L3_N8_lam0_T0", "m3_L3_N8_lam0_T0")
REPRODUCTION_UNIVERSES = ("plusM", "minusM")
WOLFRAM_OPEN_FAILURE = "Failed to open file"


class AuditFailure(Exception):
    """A failed requirement; the message is printed as stage5_audit_problem."""


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    try:
        return json.loads(path.read_bytes().decode("utf-8"))
    except (OSError, ValueError) as error:
        raise AuditFailure(f"{path.as_posix()} is not readable UTF-8 JSON: {error}") from error


def emit(name: str, value) -> None:
    print(f"stage5_{name}={value}", flush=True)


def last_line(path: Path) -> str:
    try:
        lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines()]
    except OSError:
        return ""
    lines = [line for line in lines if line]
    return lines[-1] if lines else ""


# ---------------------------------------------------------------------------
# rust-run (as in the Stage-4 audit, with pairs and --quick)


def cmd_rust_run(arguments) -> list[str]:
    binary = Path(arguments.binary)
    if not binary.is_file():
        raise AuditFailure(f"missing binary {binary.as_posix()}")
    executable = os.path.abspath(str(binary))
    jobs = []
    for sub, output, mode in arguments.job:
        if sub not in SUBCOMMANDS or mode not in MODES:
            raise AuditFailure(f"bad job {sub} {output} {mode}")
        command = [executable, sub] + MODE_FLAG[mode] + ["--output", output]
        log = Path(f"{arguments.log_prefix}-{mode}-{sub}.log")
        log.parent.mkdir(parents=True, exist_ok=True)
        jobs.append({"sub": sub, "mode": mode, "output": output, "command": command, "log": log})
    emit("rust_run_mode", "sequential" if arguments.sequential else f"concurrent ({len(jobs)} processes)")
    started = time.monotonic()
    problems: list[str] = []

    def start(job):
        job["handle"] = open(job["log"], "wb")
        job["started"] = time.monotonic()
        job["process"] = subprocess.Popen(job["command"], stdout=job["handle"], stderr=subprocess.STDOUT)

    def finish(job, code):
        job["handle"].close()
        job["seconds"] = time.monotonic() - job["started"]
        job["last"] = last_line(job["log"])
        emit("rust_job", f"{job['mode']} {job['sub']} exit={code} last={job['last']} "
                         f"seconds={job['seconds']:.0f} log={job['log'].as_posix()}")
        if code != 0 or job["last"] != "SUCCESS":
            problems.append(f"{job['mode']} {job['sub']} exited {code} with last line {job['last']!r} "
                            f"(log {job['log'].as_posix()})")

    def stop_others(running):
        for job in running:
            job["process"].terminate()
        for job in running:
            job["process"].wait()
            job["handle"].close()
            emit("rust_job", f"{job['mode']} {job['sub']} STOPPED after the failure above")

    if arguments.sequential:
        for index, job in enumerate(jobs):
            start(job)
            finish(job, job["process"].wait())
            if problems:
                for rest in jobs[index + 1:]:
                    emit("rust_job", f"{rest['mode']} {rest['sub']} NOT STARTED after the failure above")
                break
    else:
        for job in jobs:
            start(job)
        running = list(jobs)
        while running and not problems:
            time.sleep(2.0)
            for job in list(running):
                code = job["process"].poll()
                if code is not None:
                    running.remove(job)
                    finish(job, code)
        if running:
            stop_others(running)
    emit("rust_run_total_seconds", f"{time.monotonic() - started:.0f}")
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
# Rust outputs and trees


def tree_files(directory: Path) -> list[str]:
    return sorted(path.relative_to(directory).as_posix() for path in directory.rglob("*")
                  if path.is_file() and "__pycache__" not in path.parts)


def cmd_rust_outputs(arguments) -> list[str]:
    committed = Path(arguments.committed)
    runs = [Path(run) for run in arguments.run]
    problems = []
    for sub in arguments.sub:
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
            emit(f"rust_outputs_{sub}", f"{len(expected)} files compared in "
                                        f"{', '.join(r.as_posix() for r in runs)} against {committed.as_posix()}/{sub}")
    return problems


def cmd_tree_same(arguments) -> list[str]:
    committed, fresh = Path(arguments.committed), Path(arguments.fresh)
    if not committed.is_dir():
        raise AuditFailure(f"missing committed directory {committed.as_posix()}")
    if not fresh.is_dir():
        raise AuditFailure(f"missing fresh directory {fresh.as_posix()}")
    expected, present = tree_files(committed), tree_files(fresh)
    problems = []
    if not expected:
        problems.append(f"{committed.as_posix()} holds no file")
    if expected != present:
        problems.append(f"{fresh.as_posix()} holds other files than {committed.as_posix()} "
                        f"(extra {sorted(set(present) - set(expected))[:5]}, "
                        f"missing {sorted(set(expected) - set(present))[:5]})")
    different = [name for name in expected if name in present
                 and (committed / name).read_bytes() != (fresh / name).read_bytes()]
    if different:
        problems.append(f"{len(different)} file(s) of {fresh.as_posix()} differ from {committed.as_posix()}, "
                        f"first: {different[0]}")
    emit("tree_same", f"{len(expected) - len(different)}/{len(expected)} files of {committed.as_posix()} "
                      f"byte-identical in {fresh.as_posix()}")
    return problems


# ---------------------------------------------------------------------------
# reports (determinism, Stage-4 identity, pairs checker)


def cmd_report(arguments) -> list[str]:
    fresh_path = Path(arguments.fresh)
    fresh = load_json(fresh_path)
    problems = []
    checks = fresh.get("checks", {}) if isinstance(fresh.get("checks"), dict) else {}
    failed = [name for name, passed in checks.items() if passed is not True]
    if not checks:
        problems.append(f"{fresh_path.as_posix()} has no checks")
    if failed:
        problems.append(f"{fresh_path.as_posix()} failed checks: {', '.join(failed[:10])}")
    if "checkCount" in fresh and fresh.get("checkCount") != len(checks):
        problems.append(f"{fresh_path.as_posix()} checkCount {fresh.get('checkCount')} is not {len(checks)}")
    if "failedCheckCount" in fresh and fresh.get("failedCheckCount") != len(failed):
        problems.append(f"{fresh_path.as_posix()} failedCheckCount {fresh.get('failedCheckCount')} "
                        f"is not {len(failed)}")
    missing = [name for name in arguments.require_check if name not in checks]
    if missing:
        problems.append(f"{fresh_path.as_posix()} lacks the check(s) {', '.join(missing)}")
    emit("report_checks", f"{len(checks) - len(failed)}/{len(checks)} true in {fresh_path.as_posix()}")
    if arguments.committed:
        committed_path = Path(arguments.committed)
        if not committed_path.is_file() and arguments.committed_optional:
            emit("report_committed", f"ABSENT ({committed_path.as_posix()} is not committed; only the fresh "
                                     f"report was audited)")
            return problems
        committed = load_json(committed_path)
        reference_checks = committed.get("checks", {}) if isinstance(committed.get("checks"), dict) else {}
        if set(checks) != set(reference_checks):
            problems.append(f"{fresh_path.as_posix()} has other checks than {committed_path.as_posix()}: only fresh "
                            f"{sorted(set(checks) - set(reference_checks))[:5]}, only committed "
                            f"{sorted(set(reference_checks) - set(checks))[:5]}")
        if fresh.get("comparisonsNotRun") != committed.get("comparisonsNotRun"):
            problems.append(f"comparisonsNotRun {fresh.get('comparisonsNotRun')} differ from the committed "
                            f"{committed.get('comparisonsNotRun')}")
        emit("report_committed", f"{committed_path.as_posix()} ({len(reference_checks)} checks)")
        emit("report_order_equal_to_committed", "yes" if list(checks) == list(reference_checks) else "no")
        emit("report_byte_identical_to_committed",
             "yes" if fresh_path.read_bytes() == committed_path.read_bytes() else "no")
    return problems


# ---------------------------------------------------------------------------
# reference pairs runner


def cmd_reference_quick(arguments) -> list[str]:
    path = Path(arguments.summary)
    summary = load_json(path)
    problems = []
    if summary.get("quick") is not True:
        problems.append(f"{path.as_posix()} is not a --quick summary")
    if summary.get("complete") is not True:
        problems.append(f"{path.as_posix()} is not complete")
    runs = summary.get("runs", [])
    if not runs:
        problems.append(f"{path.as_posix()} has no runs")
    if summary.get("pending"):
        problems.append(f"{path.as_posix()} has pending runs {summary.get('pending')[:5]}")
    if summary.get("failedOther"):
        problems.append(f"{path.as_posix()} has failed runs other than controls: {summary.get('failedOther')[:5]}")
    converged = sum(1 for run in runs if run.get("converged") and not run.get("failed"))
    emit("reference_quick_runs", f"{len(runs)} runs, {converged} converged, failed controls "
                                 f"{len(summary.get('failedControl') or [])}, not attempted "
                                 f"{len(summary.get('notAttempted') or [])}")
    return problems


def select_reproduction(records: dict, max_configs: int) -> list[str]:
    labels = []
    for field in REPRODUCTION_FIELDS:
        for config in REPRODUCTION_CONFIGS:
            pair = [f"{field}_{config}/{universe}" for universe in REPRODUCTION_UNIVERSES]
            if all(label in records and records[label].get("converged") is True
                   and not records[label].get("failed") for label in pair):
                labels += pair
                break
    return labels[:2 * max_configs]


def cmd_reference_reproduce(arguments) -> list[str]:
    committed, output = Path(arguments.committed), Path(arguments.output)
    summary = load_json(committed / REFERENCE_SUMMARY)
    records = {run.get("label"): run for run in summary.get("runs", []) if isinstance(run, dict)}
    labels = select_reproduction(records, arguments.max_configs)
    if not labels:
        raise AuditFailure(f"{(committed / REFERENCE_SUMMARY).as_posix()} has no converged plusM/minusM pair "
                           f"among {', '.join(f + '_' + c for f in REPRODUCTION_FIELDS for c in REPRODUCTION_CONFIGS)}")
    emit("reference_reproduce_runs", ",".join(labels))
    command = [arguments.python, REFERENCE_RUNNER, "--runs", ",".join(labels), "--output", str(output),
               "--workers", str(arguments.workers)]
    log = Path(arguments.log) if arguments.log else output / "reference-reproduce.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    with open(log, "wb") as handle:
        code = subprocess.run(command, stdout=handle, stderr=subprocess.STDOUT, check=False).returncode
    emit("reference_reproduce_runner", f"exit={code} seconds={time.monotonic() - started:.0f} log={log.as_posix()}")
    problems = []
    if code != 0:
        problems.append(f"{REFERENCE_RUNNER} exited {code} (log {log.as_posix()})")
    fresh_summary = output / REFERENCE_SUMMARY
    fresh_records = {}
    if fresh_summary.is_file():
        fresh_records = {run.get("label"): run for run in load_json(fresh_summary).get("runs", [])
                         if isinstance(run, dict)}
    else:
        problems.append(f"missing {fresh_summary.as_posix()}")
    compared = 0
    for label in labels:
        reference_directory, fresh_directory = committed / label, output / label
        expected = tree_files(reference_directory) if reference_directory.is_dir() else []
        if not expected:
            problems.append(f"{reference_directory.as_posix()} holds no committed file")
            continue
        present = tree_files(fresh_directory) if fresh_directory.is_dir() else []
        if present != expected:
            problems.append(f"{fresh_directory.as_posix()} holds other files than {reference_directory.as_posix()} "
                            f"(extra {sorted(set(present) - set(expected))[:5]}, "
                            f"missing {sorted(set(expected) - set(present))[:5]})")
        different = [name for name in expected if name in present and
                     (reference_directory / name).read_bytes() != (fresh_directory / name).read_bytes()]
        if different:
            problems.append(f"{label}: {len(different)} file(s) differ from the committed run, first {different[0]}")
        compared += len(expected)
        if fresh_records.get(label) != records.get(label):
            problems.append(f"{label}: the fresh summary record differs from the committed one")
    emit("reference_reproduce_files", f"{compared} committed files compared in {len(labels)} run directories")
    return problems


# ---------------------------------------------------------------------------
# snapshot / unchanged / fresh (as in the Stage-4 audit)


def drop_key(document, dotted: str) -> None:
    parts = dotted.split(".")
    for part in parts[:-1]:
        if not isinstance(document, dict) or part not in document:
            return
        document = document[part]
    if isinstance(document, dict):
        document.pop(parts[-1], None)


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
        print(f"stage5_sha256={sha256_file(path)}  {path.as_posix()}")
    return problems


def cmd_wolfram_log(arguments) -> list[str]:
    path = Path(arguments.log)
    if not path.is_file():
        raise AuditFailure(f"missing log {path.as_posix()}")
    text = path.read_text(encoding="utf-8", errors="replace")
    hits = [line.strip() for line in text.splitlines() if WOLFRAM_OPEN_FAILURE in line]
    emit("wolfram_log", f"{path.as_posix()}: {len(hits)} line(s) with '{WOLFRAM_OPEN_FAILURE}'")
    return [f"{path.as_posix()} reports '{hits[0]}'"] if hits else []


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    rust_run = commands.add_parser("rust-run")
    rust_run.add_argument("--binary", required=True)
    rust_run.add_argument("--log-prefix", required=True)
    rust_run.add_argument("--sequential", action="store_true")
    rust_run.add_argument("--job", nargs=3, action="append", required=True, metavar=("SUB", "OUTPUT", "MODE"))
    same = commands.add_parser("same")
    same.add_argument("--pair", nargs=2, action="append", required=True, metavar=("EXPECTED", "ACTUAL"))
    same.add_argument("--rtol", type=float, default=None)
    same.add_argument("--atol", type=float, default=0.0)
    outputs = commands.add_parser("rust-outputs")
    outputs.add_argument("--committed", required=True)
    outputs.add_argument("--run", action="append", required=True)
    outputs.add_argument("--sub", action="append", required=True, choices=SUBCOMMANDS)
    report = commands.add_parser("report")
    report.add_argument("--fresh", required=True)
    report.add_argument("--committed")
    report.add_argument("--committed-optional", action="store_true")
    report.add_argument("--require-check", action="append", default=[])
    reference = commands.add_parser("reference-quick")
    reference.add_argument("--summary", required=True)
    reproduce = commands.add_parser("reference-reproduce")
    reproduce.add_argument("--committed", required=True)
    reproduce.add_argument("--output", required=True)
    reproduce.add_argument("--max-configs", type=int, default=2)
    reproduce.add_argument("--workers", type=int, default=4)
    reproduce.add_argument("--python", default=sys.executable)
    reproduce.add_argument("--log")
    tree = commands.add_parser("tree-same")
    tree.add_argument("--committed", required=True)
    tree.add_argument("--fresh", required=True)
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
    wolfram = commands.add_parser("wolfram-log")
    wolfram.add_argument("--log", required=True)
    arguments = parser.parse_args(argv)

    handlers = {
        "rust-run": cmd_rust_run, "same": cmd_same, "rust-outputs": cmd_rust_outputs, "report": cmd_report,
        "reference-quick": cmd_reference_quick, "reference-reproduce": cmd_reference_reproduce,
        "tree-same": cmd_tree_same, "snapshot": cmd_snapshot, "unchanged": cmd_unchanged, "fresh": cmd_fresh,
        "wolfram-log": cmd_wolfram_log,
    }
    try:
        problems = handlers[arguments.command](arguments)
    except AuditFailure as error:
        problems = [str(error)]
    for problem in problems:
        print(f"stage5_audit_problem={problem}")
    print(f"stage5_audit_{arguments.command.replace('-', '_')}={'FAILED' if problems else 'OK'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
