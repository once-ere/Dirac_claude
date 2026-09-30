#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Stage-5 run comparisons of dirac16complex_kohn_sham (standard library only).

Mode 1, determinism and tolerance convergence of the `pairs` tree:

    python tools/compare_pairs_runs.py --canonical ROOT [--repeat ROOT2]
                                       [--refined ROOT3] [--report PATH]

  ROOT is the output root of `pairs` (the tree is ROOT/pairs/).
  * repeat: every file listed in ROOT/pairs/summary.json (`files`, including
    summary.json) must exist in ROOT2/pairs/ with the same SHA-256 (byte
    identity of a second run of the same binary with the same flags);
  * refined (a `pairs --refined` run): for every configuration, the
    universes plusM and minusM (the check `refined_convergence`; both must be
    converged KS states in both trees) and, measured only, the control where
    it converged in both trees: E and F (relative 1e-7, or absolute 1e-9 |m|
    where they vanish), mu, the KS gap and Delta-SCF (absolute 1e-7 |m|) and
    the eps column of levels.csv by level key (absolute 1e-7 |m|, the
    Stage-4 compare_runs.py tolerances); the pairing deviations of both runs
    are reported side by side, and the verdict of the refined run must be
    SUCCESS (it re-checks every pairing identity at the refined tolerances).

Mode 2, byte identity of the Stage-4 subcommands (the Stage-5 changes must
not change a single Stage-4 byte):

    python tools/compare_pairs_runs.py --stage4-committed DIR --stage4-run DIR
                                       [--full SUB ...] [--quick SUB ...]
                                       [--report PATH]

  DIR (committed) is artifacts/dirac16complex/kohn-sham/rust (read only);
  the run directory holds `<sub>/` trees written by the current binary.
  * --full SUB (a canonical run of SUB): every file of the committed
    SUB/summary.json list, summary.json included, byte-identical;
  * --quick SUB (a `SUB --quick` run, a subset of the canonical matrix):
    every file of every run directory of the quick tree byte-identical with
    the committed file of the same path; every run record of the quick
    summary.json equal (as JSON) to the committed record with the same label;
    every check of the quick summary with a committed counterpart equal;
    every row of every top-level CSV of the quick tree present, byte for
    byte, in the committed CSV of the same name.

`--binary PATH` records the SHA-256 of the executable that produced the
trees (measurement binarySha256).

Prints `check_<name>=true|false`, `measurement_<name>=...`, `check_count`,
`failed_check_count`; writes the JSON report {schemaVersion, producer,
checks, measurements, sourceSha256}; exits 1 when any check fails.
"""

import argparse
import csv
import hashlib
import json
import os
import sys

PRODUCER = "studies/dirac16complex_kohn_sham/tools/compare_pairs_runs.py"
ENERGY_TOLERANCE = 1.0e-7
ENERGY_FLOOR = 1.0e-9
EPS_TOLERANCE = 1.0e-7
UNIVERSES = ["plusM", "minusM", "minusM_control"]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def eps_column(path):
    with open(path, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    header = rows[0]
    index = header.index("eps")
    keys = [header.index(name) for name in ("n2", "parity", "s", "index")]
    return {tuple(row[k] for k in keys): float(row[index]) for row in rows[1:]}


def as_float(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    return None


def energy_close(a, b, mass):
    if a is None and b is None:
        return True, 0.0
    if a is None or b is None:
        return False, float("inf")
    diff = abs(a - b)
    scale = max(abs(a), abs(b))
    ok = diff <= ENERGY_TOLERANCE * scale or diff <= ENERGY_FLOOR * mass
    return ok, diff / scale if scale > 0 else diff


def compare_pairs(args, checks, measurements, sources):
    base = os.path.join(args.canonical, "pairs")
    summary_path = os.path.join(base, "summary.json")
    if not os.path.exists(summary_path):
        checks["canonical_summary_present"] = False
        return
    summary = load_json(summary_path)
    sources["pairs/summary.json"] = sha256_file(summary_path)
    checks["canonical_summary_present"] = True
    checks["canonical_verdict_success"] = summary.get("verdict") == "SUCCESS"
    measurements["canonicalChecks"] = len(summary.get("checks", {}))
    measurements["canonicalFailedChecks"] = sorted(
        name for name, passed in summary.get("checks", {}).items() if not passed)
    files = list(summary.get("files", []))
    measurements["canonicalFiles"] = len(files)
    if args.repeat:
        compared = 0
        differing = []
        for name in files:
            a = os.path.join(base, name)
            b = os.path.join(args.repeat, "pairs", name)
            if not (os.path.exists(a) and os.path.exists(b)):
                differing.append(name + " (missing)")
                continue
            compared += 1
            if sha256_file(a) != sha256_file(b):
                differing.append(name)
        checks["repeat_byte_identity"] = compared == len(files) and compared > 0 and not differing
        measurements["repeatFilesCompared"] = compared
        measurements["repeatDifferingFiles"] = differing[:20]
    if args.refined:
        refined_summary_path = os.path.join(args.refined, "pairs", "summary.json")
        if not os.path.exists(refined_summary_path):
            checks["refined_summary_present"] = False
            return
        refined_summary = load_json(refined_summary_path)
        checks["refined_summary_present"] = True
        checks["refined_verdict_success"] = refined_summary.get("verdict") == "SUCCESS"
        measurements["refinedFailedChecks"] = sorted(
            name for name, passed in refined_summary.get("checks", {}).items() if not passed)
        measurements["refinedTolerances"] = refined_summary.get("tolerances")
        labels = [c["label"] for c in summary.get("configurations", [])]
        refined_labels = {c["label"] for c in refined_summary.get("configurations", [])}
        groups = {"paired": ["plusM", "minusM"], "control": ["minusM_control"]}
        worst = {g: {"energy": 0.0, "free": 0.0, "mu": 0.0, "gap": 0.0, "deltaScf": 0.0, "eps": 0.0}
                 for g in groups}
        failures = {g: [] for g in groups}
        compared = {g: 0 for g in groups}
        skipped = {g: [] for g in groups}
        levels_compared = {g: 0 for g in groups}
        pairing_side_by_side = []
        missing = []
        for label in labels:
            if label not in refined_labels:
                missing.append(label)
                continue
            p1 = load_json(os.path.join(base, label, "pairing.json"))
            p2 = load_json(os.path.join(args.refined, "pairs", label, "pairing.json"))
            mass = p1["configuration"]["absMass"]
            dev1 = p1.get("pairingDeviation_plusM_vs_minusM") or {}
            dev2 = p2.get("pairingDeviation_plusM_vs_minusM") or {}
            pairing_side_by_side.append({
                "label": label,
                "canonicalMaxAbsDeltaEps": dev1.get("maxAbsDeltaEps"),
                "refinedMaxAbsDeltaEps": dev2.get("maxAbsDeltaEps"),
                "canonicalAbsDeltaE": (dev1.get("scalars_absDifference_absValueA") or {}).get("E", [None])[0],
                "refinedAbsDeltaE": (dev2.get("scalars_absDifference_absValueA") or {}).get("E", [None])[0],
            })
            for group, universes in groups.items():
                for universe in universes:
                    tag = "%s/%s" % (label, universe)
                    r1_path = os.path.join(base, label, universe, "run.json")
                    r2_path = os.path.join(args.refined, "pairs", label, universe, "run.json")
                    if not (os.path.exists(r1_path) and os.path.exists(r2_path)):
                        failures[group].append(tag + " (run.json missing)")
                        continue
                    r1 = load_json(r1_path)
                    r2 = load_json(r2_path)
                    if "error" in r1 or "error" in r2 or not r1.get("converged") or not r2.get("converged"):
                        # a state that is not a converged KS state in both trees is not compared
                        skipped[group].append(tag)
                        if group == "paired":
                            failures[group].append(tag + " (not converged or not solved)")
                        continue
                    compared[group] += 1
                    w = worst[group]
                    for key, name in (("energy", "energy"), ("freeEnergy", "free")):
                        ok, rel = energy_close(as_float(r1.get(key)), as_float(r2.get(key)), mass)
                        w[name] = max(w[name], rel)
                        if not ok:
                            failures[group].append("%s %s %r vs %r" % (tag, key, r1.get(key), r2.get(key)))
                    for key, name in (("mu", "mu"), ("ksGap", "gap")):
                        a, b = as_float(r1.get(key)), as_float(r2.get(key))
                        if a is None and b is None:
                            continue
                        d = abs(a - b) if a is not None and b is not None else float("inf")
                        w[name] = max(w[name], d)
                        if d > EPS_TOLERANCE * mass:
                            failures[group].append("%s %s %r vs %r" % (tag, key, a, b))
                    e1 = as_float((r1.get("firstExcitedState") or {}).get("deltaScf"))
                    e2 = as_float((r2.get("firstExcitedState") or {}).get("deltaScf"))
                    if e1 is not None or e2 is not None:
                        d = abs(e1 - e2) if e1 is not None and e2 is not None else float("inf")
                        w["deltaScf"] = max(w["deltaScf"], d)
                        if d > EPS_TOLERANCE * mass:
                            failures[group].append("%s deltaScf %r vs %r" % (tag, e1, e2))
                    l1 = os.path.join(base, label, universe, "levels.csv")
                    l2 = os.path.join(args.refined, "pairs", label, universe, "levels.csv")
                    if os.path.exists(l1) and os.path.exists(l2):
                        t1, t2 = eps_column(l1), eps_column(l2)
                        common = set(t1) & set(t2)
                        levels_compared[group] += len(common)
                        if common:
                            d = max(abs(t1[k] - t2[k]) for k in common)
                            w["eps"] = max(w["eps"], d)
                            if d > EPS_TOLERANCE * mass:
                                failures[group].append("%s eps %r" % (tag, d))
        checks["refined_configurations_present"] = not missing
        measurements["refinedMissingConfigurations"] = missing[:20]
        # the check covers the paired universes; the control (not the image of
        # the +M universe, outside the window premise at lambda != 0) is measured
        checks["refined_convergence"] = compared["paired"] > 0 and not failures["paired"]
        for group, prefix in (("paired", "refined"), ("control", "refinedControl")):
            measurements[prefix + "RunsCompared"] = compared[group]
            measurements[prefix + "RunsNotCompared_notConvergedInBoth"] = len(skipped[group])
            measurements[prefix + "LevelsCompared"] = levels_compared[group]
            measurements[prefix + "MaxRelativeEnergy"] = worst[group]["energy"]
            measurements[prefix + "MaxRelativeFreeEnergy"] = worst[group]["free"]
            measurements[prefix + "MaxAbsMu"] = worst[group]["mu"]
            measurements[prefix + "MaxAbsGap"] = worst[group]["gap"]
            measurements[prefix + "MaxAbsDeltaScf"] = worst[group]["deltaScf"]
            measurements[prefix + "MaxAbsEps"] = worst[group]["eps"]
            measurements[prefix + "Failures"] = failures[group][:40]
        measurements["refinedEnergyTolerance"] = ENERGY_TOLERANCE
        measurements["refinedEnergyFloorPerAbsM"] = ENERGY_FLOOR
        measurements["refinedEpsTolerancePerAbsM"] = EPS_TOLERANCE
        measurements["pairingDeviationsCanonicalVsRefined"] = pairing_side_by_side


def list_files(root):
    out = []
    for directory, _, names in os.walk(root):
        for name in names:
            out.append(os.path.relpath(os.path.join(directory, name), root).replace(os.sep, "/"))
    return sorted(out)


def compare_stage4(args, checks, measurements, sources):
    committed = args.stage4_committed
    run = args.stage4_run
    for sub in args.full:
        path = os.path.join(committed, sub, "summary.json")
        summary = load_json(path)
        sources["kohn-sham/rust/%s/summary.json" % sub] = sha256_file(path)
        names = list(summary.get("files", []))
        if "summary.json" not in names:
            names.append("summary.json")
        differing = []
        for name in names:
            a = os.path.join(committed, sub, name)
            b = os.path.join(run, sub, name)
            if not os.path.exists(b) or sha256_file(a) != sha256_file(b):
                differing.append(name)
        extra = sorted(set(list_files(os.path.join(run, sub))) - set(names))
        checks["stage4_%s_full_byte_identity" % sub] = bool(names) and not differing and not extra
        measurements["stage4_%s_filesCompared" % sub] = len(names)
        measurements["stage4_%s_differing" % sub] = differing[:20]
        measurements["stage4_%s_unexpectedFiles" % sub] = extra[:20]
    for sub in args.quick:
        run_root = os.path.join(run, sub)
        path = os.path.join(committed, sub, "summary.json")
        sources["kohn-sham/rust/%s/summary.json" % sub] = sha256_file(path)
        committed_summary = load_json(path)
        quick_summary = load_json(os.path.join(run_root, "summary.json"))
        files = list_files(run_root)
        run_files = [f for f in files if "/" in f]
        top_csv = [f for f in files if "/" not in f and f.endswith(".csv")]
        differing = []
        for name in run_files:
            a = os.path.join(committed, sub, name)
            b = os.path.join(run_root, name)
            if not os.path.exists(a) or sha256_file(a) != sha256_file(b):
                differing.append(name)
        checks["stage4_%s_quick_run_files_byte_identical" % sub] = bool(run_files) and not differing
        measurements["stage4_%s_quickRunFilesCompared" % sub] = len(run_files)
        measurements["stage4_%s_quickRunDirectories" % sub] = sorted({f.split("/")[0] for f in run_files})
        measurements["stage4_%s_quickDiffering" % sub] = differing[:20]
        committed_runs = {r.get("label"): r for r in committed_summary.get("runs", [])}
        quick_runs = quick_summary.get("runs", [])
        record_mismatch = [r.get("label") for r in quick_runs
                           if committed_runs.get(r.get("label")) != r]
        checks["stage4_%s_quick_run_records_equal" % sub] = bool(quick_runs) and not record_mismatch
        measurements["stage4_%s_quickRunRecords" % sub] = len(quick_runs)
        measurements["stage4_%s_quickRecordMismatch" % sub] = record_mismatch[:20]
        committed_checks = committed_summary.get("checks", {})
        quick_checks = quick_summary.get("checks", {})
        shared = [name for name in quick_checks if name in committed_checks]
        check_mismatch = [name for name in shared if quick_checks[name] != committed_checks[name]]
        failed_quick = [name for name, passed in quick_checks.items() if not passed]
        checks["stage4_%s_quick_checks_agree" % sub] = (bool(shared) and not check_mismatch
                                                         and not failed_quick)
        measurements["stage4_%s_quickChecks" % sub] = len(quick_checks)
        measurements["stage4_%s_quickChecksShared" % sub] = len(shared)
        measurements["stage4_%s_quickChecksOnlyInQuick" % sub] = sorted(
            name for name in quick_checks if name not in committed_checks)[:20]
        measurements["stage4_%s_quickCheckMismatch" % sub] = check_mismatch[:20]
        measurements["stage4_%s_quickVerdict" % sub] = quick_summary.get("verdict")
        missing_rows = []
        rows_compared = 0
        for name in top_csv:
            with open(os.path.join(committed, sub, name), "r", encoding="utf-8", newline="") as handle:
                committed_lines = set(handle.read().split("\n"))
            with open(os.path.join(run_root, name), "r", encoding="utf-8", newline="") as handle:
                lines = [line for line in handle.read().split("\n") if line]
            for line in lines:
                rows_compared += 1
                if line not in committed_lines:
                    missing_rows.append("%s: %s" % (name, line[:80]))
        checks["stage4_%s_quick_csv_rows_contained" % sub] = not missing_rows
        measurements["stage4_%s_quickCsvRowsCompared" % sub] = rows_compared
        measurements["stage4_%s_quickCsvRowsMissing" % sub] = missing_rows[:20]


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--canonical", default=None)
    parser.add_argument("--repeat", default=None)
    parser.add_argument("--refined", default=None)
    parser.add_argument("--stage4-committed", dest="stage4_committed", default=None)
    parser.add_argument("--stage4-run", dest="stage4_run", default=None)
    parser.add_argument("--full", nargs="*", default=[])
    parser.add_argument("--quick", nargs="*", default=[])
    parser.add_argument("--report", default=None)
    parser.add_argument("--binary", default=None,
                        help="the executable that produced the trees (its SHA-256 is recorded)")
    args = parser.parse_args()
    checks = {}
    measurements = {}
    sources = {}
    if args.canonical:
        compare_pairs(args, checks, measurements, sources)
    if args.stage4_committed and args.stage4_run:
        compare_stage4(args, checks, measurements, sources)
    if not checks:
        parser.error("nothing to compare")
    if args.binary:
        measurements["binarySha256"] = sha256_file(args.binary)
    for name, passed in checks.items():
        print("check_%s=%s" % (name, "true" if passed else "false"))
    for name, value in measurements.items():
        if not isinstance(value, list) or len(value) <= 6:
            print("measurement_%s=%s" % (name, json.dumps(value)))
    failed = [name for name, passed in checks.items() if not passed]
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % len(failed))
    if args.report:
        sources[PRODUCER] = sha256_file(os.path.abspath(__file__))
        report = {"schemaVersion": 1, "producer": PRODUCER,
                  "checks": dict(sorted(checks.items())),
                  "measurements": dict(sorted(measurements.items())),
                  "sourceSha256": dict(sorted(sources.items()))}
        os.makedirs(os.path.dirname(os.path.abspath(args.report)), exist_ok=True)
        with open(args.report, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(report, indent=2) + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
