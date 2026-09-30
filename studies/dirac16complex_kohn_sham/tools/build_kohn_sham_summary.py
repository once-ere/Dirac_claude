#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Collect the Stage-4 Kohn-Sham results into artifacts/dirac16complex/kohn-sham/kohn-sham-summary.json.

Standard library only.  Nothing is computed here: every number is COPIED from
the committed reports and outputs (values are only selected, re-keyed and
counted; CSV cells are parsed from their "%.17e" text), and the SHA-256 of
every file read is recorded, so the summary is tied to exactly the data it
describes.  Pattern: studies/dirac16complex_cosmology/tools/build_numerics_summary.py
(Stage 3, same repository).

Inputs (paths relative to --root, default artifacts/dirac16complex/kohn-sham):

  wolfram-kohn-sham-report.json        scripts/verify_dirac16complex_kohn_sham.wls
  kohn-sham-theory.json                (the same verifier: exact theory data)
  python-theory-report.json            scripts/check_dirac16complex_kohn_sham_theory.py
  exchange-table.json                  (the same checker; hashed only)
  rust/generator-report.json           scripts/generate_dirac16complex_ks_constants.py
  rust/{spectrum,scf,excited,thermo,emt}/summary.json
                                       studies/dirac16complex_kohn_sham (canonical run)
  rust/spectrum/theory-agreement.json  (zero-mode splitting comparison)
  rust/excited/<label>/particle-hole.csv, levels.csv
                                       (first particle-hole pairs of every excited
                                       run; for the runs converged with occupation
                                       smearing: the fractionally occupied levels
                                       and the COUNT of particle-branch states up
                                       to each of them, i.e. where the exact T = 0
                                       aufbau count closes)
  rust/determinism-report.json         studies/dirac16complex_kohn_sham/tools/compare_runs.py
  reference/reference-summary.json     scripts/ks_reference_solver.py
  python-check-report.json             scripts/check_dirac16complex_kohn_sham.py
  notebook-report.json                 Jupyter notebook audit (optional: recorded
                                       as absent when missing)
  mathematica-report.json              Mathematica notebook verifier (optional)

and, from the repository, the algebra fixture
artifacts/dirac16complex/arbitrary-field/algebra-fixture.json and the source
files whose hashes the reports record (studies/dirac16complex_kohn_sham/src/
generated.rs, the Wolfram module and verifier, the reference solver and the
cross-checker).

Refusals (exit 1, nothing written):
  * a required input is missing or is not UTF-8 JSON;
  * a fixture hash recorded by any input differs from the SHA-256 of the
    fixture (inconsistent fixture hashes);
  * a Rust summary comes from a --refined run, or the reference summary from
    a --quick run (not the canonical outputs).
Stale inputs (exit 1, nothing written, unless --allow-incomplete, which
writes the summary with verdict INCOMPLETE and exits 3; never used for the
committed file):
  * the determinism report or the cross-checker report records SHA-256 values
    of the Rust summaries, the reference summary, the theory JSON or the
    solver/checker sources that differ from the files read here (it describes
    another version of its inputs);
  * the reference summary is not complete, or the cross-checker report was
    produced without --repeat / --refined (no rust_repeat_byte_identity /
    rust_refined_convergence check);
  * a source hash recorded by the theory reports or the generator report
    differs from the current file.
A failed check of any producer is reported (verdict FAILURE, exit 1) but the
summary is still written, so that the failure is visible.

The output is deterministic: fixed key order, json.dumps(indent=2) + "\\n",
LF, no absolute paths (inputs are named relative to the root, recorded as
artifacts/dirac16complex/kohn-sham), NaN/Infinity of the sources written as
null.  Re-running the builder on the same inputs reproduces the file byte for
byte.

Usage (from the repository root):
  python studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py
      [--root DIR] [--output PATH] [--allow-incomplete]
Prints one line per producer, the totals, the output path and the verdict
(SUCCESS / FAILURE / INCOMPLETE) as the last line.
"""

import argparse
import csv
import hashlib
import json
import math
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CANONICAL_ROOT = "artifacts/dirac16complex/kohn-sham"
DEFAULT_ROOT = os.path.join(REPO, *CANONICAL_ROOT.split("/"))
FIXTURE = "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"
PRODUCER = "studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py"
SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")
# Occupation floor of the particle-hole lists of T = 0 runs in both solvers
# (runs.rs PH_OCCUPATION_FLOOR; the reference solver's T = 0 rule): used here
# only to SELECT the fractionally occupied levels of a smeared run for copying.
OCCUPATION_FLOOR = 1e-12
PARTICLE_HOLE_ROWS = 3
LABEL = re.compile(r"^m(?P<m>\d+)_L(?P<L>\d+)_N(?P<N>\d+)_(?P<lam>lam[a-z0-9]+?)_T(?P<T>[0-9p]+)"
                   r"(?:_(?P<suffix>.+))?$")
CROSS_CHECK_REQUIRED = ("rust_repeat_byte_identity", "rust_refined_convergence")


class SummaryError(Exception):
    """A refusal: nothing is written."""


class Inputs:
    """Reads the inputs, remembers their SHA-256 and the problems found."""

    def __init__(self, root, allow_incomplete):
        self.root = root
        self.allow_incomplete = allow_incomplete
        self.sources = []
        self.stale = []
        self.consistency = {}

    def path(self, relative):
        return os.path.join(self.root, *relative.split("/"))

    def exists(self, relative):
        return os.path.isfile(self.path(relative))

    def raw(self, relative, repository=False):
        path = os.path.join(REPO, *relative.split("/")) if repository else self.path(relative)
        if not os.path.isfile(path):
            raise SummaryError("missing input %s" % (relative if repository else CANONICAL_ROOT + "/" + relative))
        with open(path, "rb") as handle:
            data = handle.read()
        name = relative if repository else CANONICAL_ROOT + "/" + relative
        self.sources.append({"path": name, "sha256": hashlib.sha256(data).hexdigest()})
        return data

    def json(self, relative, repository=False):
        data = self.raw(relative, repository)
        try:
            return json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as error:
            raise SummaryError("%s is not UTF-8 JSON: %s" % (relative, error))

    def csv_rows(self, relative):
        text = self.raw(relative).decode("utf-8")
        rows = list(csv.reader(text.splitlines()))
        if not rows:
            raise SummaryError("%s is empty" % relative)
        return rows[0], rows[1:]

    def sha(self, relative, repository=False):
        """SHA-256 of a file already read (or read now)."""
        name = relative if repository else CANONICAL_ROOT + "/" + relative
        for entry in self.sources:
            if entry["path"] == name:
                return entry["sha256"]
        self.raw(relative, repository)
        return self.sources[-1]["sha256"]

    def require(self, name, passed, detail, stale=True):
        """Record a consistency check; a failure is a refusal (stale=False) or
        a stale input (refusal unless --allow-incomplete)."""
        self.consistency[name] = {"passed": bool(passed), "detail": detail}
        if passed:
            return
        if not stale:
            raise SummaryError("%s: %s" % (name, detail))
        self.stale.append("%s: %s" % (name, detail))


def clean(value):
    """NaN and infinities of the sources -> null; everything else unchanged."""
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, list):
        return [clean(item) for item in value]
    return value


def pick(mapping, keys):
    return {key: mapping.get(key) for key in keys}


def number(text):
    """A CSV cell ("%.17e", or nan) as a JSON value."""
    value = float(text)
    return value if math.isfinite(value) else None


def parse_label(label):
    match = LABEL.match(label)
    if not match:
        return {"m": None, "L": None, "N": None, "lambdaName": None, "T": None, "suffix": None}
    return {"m": float(match.group("m")), "L": float(match.group("L")), "N": float(match.group("N")),
            "lambdaName": match.group("lam"), "T": float(match.group("T").replace("p", ".")),
            "suffix": match.group("suffix")}


def check_block(checks):
    """Counts of a {name: bool} check dictionary."""
    if not isinstance(checks, dict) or not checks:
        raise SummaryError("a report has no non-empty checks object")
    failed = [name for name, passed in checks.items() if passed is not True]
    return {"checkCount": len(checks), "passedCount": len(checks) - len(failed),
            "failedCount": len(failed), "failed": failed}


# ------------------------------------------------------------ producers --

def fixture_consistency(inp, name, recorded, fixture_sha):
    inp.require("fixture_" + name, recorded == fixture_sha,
                "%s records fixture sha256 %s, the fixture is %s" % (name, recorded, fixture_sha), stale=False)


def source_consistency(inp, name, recorded, relative):
    """A repository source hash recorded by a report equals the current file."""
    current = inp.sha(relative, repository=True)
    inp.require("source_%s_%s" % (name, os.path.basename(relative)), recorded == current,
                "%s records sha256 %s for %s, the file is %s" % (name, recorded, relative, current))


def theory_producers(inp, fixture_sha):
    wolfram = inp.json("wolfram-kohn-sham-report.json")
    fixture_consistency(inp, "wolfram_report", wolfram["sourceSha256"].get(FIXTURE), fixture_sha)
    for relative, recorded in wolfram["sourceSha256"].items():
        if relative != FIXTURE:
            source_consistency(inp, "wolfram_report", recorded, relative)
    theory = inp.json("kohn-sham-theory.json")
    fixture_consistency(inp, "theory_json", theory["sourceSha256"].get(FIXTURE), fixture_sha)
    inp.require("theory_json_same_verifier_run", theory["sourceSha256"] == wolfram["sourceSha256"],
                "kohn-sham-theory.json and wolfram-kohn-sham-report.json record the same source hashes")
    sympy = inp.json("python-theory-report.json")
    fixture_consistency(inp, "python_theory_report", sympy["inputSha256"].get(FIXTURE), fixture_sha)
    theory_key = CANONICAL_ROOT + "/kohn-sham-theory.json"
    recorded_theory = sympy["inputSha256"].get(theory_key)
    inp.require("python_theory_report_theory_json", recorded_theory == inp.sha("kohn-sham-theory.json"),
                "python-theory-report.json compared kohn-sham-theory.json %s (file %s)"
                % (recorded_theory, inp.sha("kohn-sham-theory.json")))
    for relative, recorded in sympy["sourceSha256"].items():
        source_consistency(inp, "python_theory_report", recorded, relative)
    table_sha = inp.sha("exchange-table.json")
    generator = inp.json("rust/generator-report.json")
    fixture_consistency(inp, "generator_report", generator["sourceSha256"].get(FIXTURE), fixture_sha)
    for relative, recorded in generator["sourceSha256"].items():
        if relative != FIXTURE:
            source_consistency(inp, "generator_report", recorded, relative)
    blocks = {
        "wolfram": dict(check_block(wolfram["checks"]), producer=wolfram["producer"],
                        report=CANONICAL_ROOT + "/wolfram-kohn-sham-report.json"),
        "sympy": dict(check_block(sympy["checks"]), producer=sympy["producer"],
                      report=CANONICAL_ROOT + "/python-theory-report.json",
                      wolframAgreement=sympy["measurements"].get("wolframAgreement"),
                      exchangeTable=pick(sympy["measurements"].get("exchangeTable") or {},
                                         ["rows", "maxRelativeDeviationFromClosedForm", "quick"])),
        "constantsGenerator": dict(check_block(generator["checks"]), producer=generator["producer"],
                                   report=CANONICAL_ROOT + "/rust/generator-report.json"),
    }
    return blocks, theory, table_sha


def rust_producers(inp, fixture_sha, table_sha):
    summaries = {}
    blocks = {}
    for sub in SUBCOMMANDS:
        summary = inp.json("rust/%s/summary.json" % sub)
        if summary.get("experiment") != sub:
            raise SummaryError("rust/%s/summary.json is labelled %r" % (sub, summary.get("experiment")))
        fixture_consistency(inp, "rust_" + sub, summary["fixture"]["sha256"], fixture_sha)
        if summary.get("refined") is not False:
            raise SummaryError("rust/%s/summary.json comes from a --refined run, not the canonical one" % sub)
        block = check_block(summary["checks"])
        block.update({"verdict": summary["verdict"], "outputFiles": len(summary["files"]),
                      "solverSteps": summary["solverTotals"]["steps"],
                      "rhsEvaluations": summary["solverTotals"]["rhsEvaluations"],
                      "tolerances": summary["tolerances"]})
        if sub != "spectrum":
            block["runs"] = len(summary.get("runs", []))
        blocks[sub] = block
        summaries[sub] = summary
    exchange = summaries["spectrum"].get("exchangeTable") or {}
    inp.require("spectrum_exchange_table", exchange.get("sha256") == table_sha,
                "rust/spectrum/summary.json cross-checked exchange-table.json %s (file %s)"
                % (exchange.get("sha256"), table_sha))
    first = summaries["spectrum"]
    header = {"study": first["study"], "engine": first["engine"], "solver": first["solver"],
              "tolerances": first["tolerances"]}
    return blocks, summaries, header


def determinism_producer(inp):
    report = inp.json("rust/determinism-report.json")
    for sub in SUBCOMMANDS:
        recorded = report["sourceSha256"].get(sub + "/summary.json")
        current = inp.sha("rust/%s/summary.json" % sub)
        inp.require("determinism_report_%s" % sub, recorded == current,
                    "determinism-report.json compared rust/%s/summary.json %s (file %s)" % (sub, recorded, current))
    for name in ("repeat_byte_identity", "refined_convergence"):
        inp.require("determinism_report_has_" + name, name in report["checks"],
                    "determinism-report.json has the check %s" % name)
    block = check_block(report["checks"])
    block.update({"producer": report["producer"], "report": CANONICAL_ROOT + "/rust/determinism-report.json",
                  "checks": report["checks"]})
    block.update(pick(report["measurements"], [
        "repeatFilesCompared", "repeatDifferingFiles", "refinedRunsCompared", "refinedLevelsCompared",
        "refinedMaxRelativeEnergy", "refinedMaxRelativeFreeEnergy", "refinedMaxAbsMu", "refinedMaxAbsEps",
        "refinedEnergyTolerance", "refinedEpsTolerance"]))
    return block


def reference_producer(inp, fixture_sha):
    summary = inp.json("reference/reference-summary.json")
    fixture_consistency(inp, "reference_summary", summary.get("fixtureSha256"), fixture_sha)
    if summary.get("quick") is not False:
        raise SummaryError("reference/reference-summary.json comes from a --quick run")
    inp.require("reference_complete", summary.get("complete") is True,
                "reference-summary.json complete flag is %r" % summary.get("complete"))
    tests = summary.get("selfTests")
    has_tests = isinstance(tests, dict) and bool(tests)
    inp.require("reference_self_tests_present", has_tests,
                "reference-summary.json carries its selfTests block (absent after a --skip-self-tests run)")
    runs = summary.get("runs", [])
    block = {
        "producer": summary["producer"], "report": CANONICAL_ROOT + "/reference/reference-summary.json",
        "solverVersion": summary.get("solverVersion"), "method": summary.get("method"),
        "complete": summary.get("complete"), "runCount": len(runs),
        "notConverged": [run["label"] for run in runs if not run.get("converged")],
        "failed": [run["label"] for run in runs if run.get("failed")],
        "smeared": [run["label"] for run in runs if run.get("exactZeroTemperatureOccupations") is False],
        "selfTestsPresent": has_tests,
        "selfTestAnalyticMaxError": tests.get("analyticMaxError") if has_tests else None,
        "skippedRuns": summary.get("skippedRuns", []),
        "closedShells": pick(summary.get("closedShells") or {}, ["N_8", "N_mid", "N_big", "N_mid3"]),
        "couplings": [pick(entry, ["m", "L", "N", "strengthPerUnitLambdaHat", "lambdaHat1", "lambdaHat2"])
                      for entry in summary.get("couplings", [])],
    }
    return block


def cross_check_producer(inp):
    report = inp.json("python-check-report.json")
    checks = report["checks"]
    block = check_block(checks)
    if report.get("checkCount") != len(checks) or report.get("failedCheckCount") != block["failedCount"]:
        raise SummaryError("python-check-report.json: checkCount/failedCheckCount do not match its checks")
    sources = report.get("sourceSha256", {})
    expected = {"referenceSummary": inp.sha("reference/reference-summary.json"),
                "theoryJson": inp.sha("kohn-sham-theory.json"),
                "referenceSolver": inp.sha("scripts/ks_reference_solver.py", repository=True),
                "checker": inp.sha("scripts/check_dirac16complex_kohn_sham.py", repository=True)}
    for sub in SUBCOMMANDS:
        expected["rust_" + sub] = inp.sha("rust/%s/summary.json" % sub)
    for key, current in expected.items():
        inp.require("cross_check_source_" + key, sources.get(key) == current,
                    "python-check-report.json records %s = %s (current %s)" % (key, sources.get(key), current))
    for name in CROSS_CHECK_REQUIRED:
        inp.require("cross_check_has_" + name, name in checks,
                    "python-check-report.json has %s (run the checker with --repeat and --refined)" % name)
    inp.require("cross_check_reference_fixture", checks.get("reference_fixture_hash") is True,
                "the cross-checker found the reference summary's fixture hash equal to the fixture", stale=False)
    block.update({"producer": report["producer"], "report": CANONICAL_ROOT + "/python-check-report.json",
                  "schemaVersion": report.get("schemaVersion"),
                  "comparisonsNotRun": report.get("comparisonsNotRun", []),
                  "repeatByteIdentity": checks.get("rust_repeat_byte_identity"),
                  "refinedConvergence": checks.get("rust_refined_convergence"),
                  "rustReproductions": report.get("measurements", {}).get("rustReproductions")})
    return block, report


def recorded_sources_current(inp, name, recorded, fixture_sha):
    """Every repository path (a key with a '/') recorded in a report's sourceSha256
    equals the current file: kohn-sham artifacts are resolved against the root,
    everything else against the repository; the fixture must match exactly."""
    for key in sorted(recorded):
        value = recorded[key]
        if "/" not in key:
            continue                      # named entries (builder, runner, ...) are not paths
        if key == FIXTURE:
            fixture_consistency(inp, name + "_source", value, fixture_sha)
            continue
        if key.startswith(CANONICAL_ROOT + "/"):
            relative, repository = key[len(CANONICAL_ROOT) + 1:], False
        else:
            relative, repository = key, True
        path = os.path.join(REPO, *relative.split("/")) if repository else inp.path(relative)
        current = inp.sha(relative, repository) if os.path.isfile(path) else None
        inp.require("%s_source_%s" % (name, key), current == value,
                    "%s records sha256 %s for %s, the file is %s" % (name, value, key, current or "missing"))


def optional_producer(inp, relative, fixture_sha):
    """Notebook / Mathematica report: counted when present."""
    if not inp.exists(relative):
        return {"status": "absent", "report": CANONICAL_ROOT + "/" + relative}
    report = inp.json(relative)
    name = os.path.splitext(relative)[0].replace("-", "_")
    block = {"status": "present", "report": CANONICAL_ROOT + "/" + relative,
             "producer": report.get("producer") or report.get("generatedBy"),
             "verdict": report.get("verdict")}
    if isinstance(report.get("checks"), dict) and report["checks"]:
        block.update(check_block(report["checks"]))
        for key, count in (("checkCount", block["checkCount"]), ("failedCheckCount", block["failedCount"])):
            if key in report and report[key] != count:
                raise SummaryError("%s: %s = %r does not match its checks (%d)" % (relative, key, report[key], count))
    if isinstance(report.get("sourceSha256"), dict):
        recorded_sources_current(inp, name, report["sourceSha256"], fixture_sha)
    gauntlet = report.get("gauntlet")
    if isinstance(gauntlet, dict):
        block["gauntlet"] = pick(gauntlet, ["count", "passed", "failed", "skipped"])
        if "checkCount" not in block and isinstance(gauntlet.get("count"), int):
            # a skipped gauntlet item is neither passed nor failed; the verdict decides
            failed = gauntlet.get("failed") if isinstance(gauntlet.get("failed"), int) else 0
            passed = gauntlet.get("passed") if isinstance(gauntlet.get("passed"), int) else gauntlet["count"] - failed
            block.update({"checkCount": gauntlet["count"], "passedCount": passed,
                          "failedCount": failed, "failed": []})
    if isinstance(report.get("figures"), list):
        block["figures"] = len(report["figures"])
    if "fixtureSha256" in report:
        fixture_consistency(inp, os.path.splitext(relative)[0].replace("-", "_"), report["fixtureSha256"],
                            fixture_sha)
    if "checkCount" not in block:
        raise SummaryError("%s has neither a checks object nor a gauntlet count" % relative)
    return block


# -------------------------------------------------------------- physics --

def dig(mapping, *keys):
    for key in keys:
        if not isinstance(mapping, dict):
            return None
        mapping = mapping.get(key)
    return mapping


def geometry_block(theory):
    geometry = theory.get("geometry", {})
    mirror = dig(geometry, "extensions", "E2_Z2mirror") or {}
    return {
        "source": CANONICAL_ROOT + "/kohn-sham-theory.json (exact strings, H and kappa symbolic)",
        "metric": dig(geometry, "metric", "tex"),
        "properVolumeElement": dig(geometry, "metric", "properVolumeElement"),
        "ricciScalar": dig(geometry, "curvature", "ricciScalar"),
        "einsteinMixedValues": dig(geometry, "curvature", "einsteinMixedValues"),
        "requiredSource": pick(geometry.get("requiredSource") or {}, ["convention", "rho", "rhoValue", "p", "pValue", "w"]),
        "extrinsicCurvature": dig(geometry, "extrinsicCurvature", "value"),
        "brane": pick(mirror, ["warp", "israelConvention", "braneStress", "braneStressValues", "braneEnergyDensity",
                               "branePressure"]),
    }


def run_identity(record):
    """(m, L, N, lambdaName, T, suffix, lambdaHat) of a run record: the
    parameters when the record has them, else the label."""
    parsed = parse_label(record["label"])
    params = record.get("parameters") or {}
    return {"label": record["label"], "m": params.get("m", parsed["m"]), "L": params.get("L", parsed["L"]),
            "N": params.get("N", record.get("N", parsed["N"])),
            "lambdaName": record.get("lambdaName") or parsed["lambdaName"],
            "T": params.get("T", parsed["T"]), "suffix": parsed["suffix"],
            "lambdaHat": params.get("lambdaHat", record.get("lambdaHat"))}


EMT_KEYS = ["rhoAvg", "pYAvg", "p3Avg", "pTAvg", "wY", "w3", "wT", "braneFraction_within_1_over_H",
            "tipFraction_within_1_over_H_of_cutoff", "rhoRequired_kappa1", "kappaNeeded", "sPAvg", "nPAvg",
            "sPMin", "sPMax", "energyFromRho", "conservationResidualMax_normalised"]
E41_KEYS = ["lambdaSAvgOverM", "lambdaSOverMRequired", "kappaFromMassCondition", "kappaFromCouplingCondition",
            "met", "lambdaHatNeededFirstOrder"]


def emt_subset(record):
    emt = record.get("emt") or {}
    block = pick(emt, EMT_KEYS)
    block["E41"] = pick(emt.get("E41_sourcingConditions") or {}, E41_KEYS)
    return block


def scf_table(summary):
    rows = []
    for record in summary["runs"]:
        row = run_identity(record)
        params = record.get("parameters") or {}
        row.update(pick(params, ["a4_0", "gridPoints", "deltaKOverM", "occupationSmearing",
                                 "zeroTemperatureFallbackStage"]))
        row.update(pick(record, ["converged", "exactZeroTemperatureOccupations", "iterations", "energy", "mu",
                                 "epsHomo", "epsLumo", "ksGap", "hartreeEnergy", "exchangeEnergy", "nTotal",
                                 "maxLambdaSOverM", "maxVxOverM", "states"]))
        row["emt"] = emt_subset(record)
        rows.append(row)
    return rows


def l_convergence(rows):
    groups = {}
    for row in rows:
        if row["suffix"] is None and row["T"] == 0.0:
            groups.setdefault((row["m"], row["N"], row["lambdaName"]), []).append(row)
    out = []
    for key in sorted(groups, key=lambda k: (k[0], k[1], k[2])):
        entries = sorted(groups[key], key=lambda r: r["L"])
        if len({entry["L"] for entry in entries}) < 2:
            continue
        out.append({"m": key[0], "N": key[1], "lambdaName": key[2],
                    "byL": [pick(entry, ["L", "label", "lambdaHat", "energy", "ksGap", "mu", "epsLumo",
                                         "maxLambdaSOverM"]) for entry in entries]})
    return out


def particle_hole_rows(inp, label):
    header, rows = inp.csv_rows("rust/excited/%s/particle-hole.csv" % label)
    return [{name: number(cell) for name, cell in zip(header, row)} for row in rows[:PARTICLE_HOLE_ROWS]]


def fractional_levels(inp, label, particles):
    """Particle-branch levels with OCCUPATION_FLOOR < f < 1 - OCCUPATION_FLOOR (copied rows), each
    with the COUNT of particle-branch states (multiplicities) at or below it in eps (CSV order breaks
    ties), and the level (if any) at which that count equals the particle number N: there the exact
    T = 0 aufbau count closes."""
    header, rows = inp.csv_rows("rust/excited/%s/levels.csv" % label)
    index = {name: position for position, name in enumerate(header)}
    ordered = sorted((row for row in rows if float(row[index["branch"]]) > 0),
                     key=lambda row: float(row[index["eps"]]))
    levels, closes, count = [], None, 0.0
    for row in ordered:
        count += float(row[index["multiplicity"]])
        copied = {name: number(row[index[name]]) for name in
                  ("n2", "k", "multiplicity", "parity", "s", "index", "eps", "f")}
        if closes is None and particles is not None and count == particles:
            closes = dict(copied, statesAtOrBelow=count)
        f = float(row[index["f"]])
        if OCCUPATION_FLOOR < f < 1.0 - OCCUPATION_FLOOR:
            levels.append(dict(copied, statesAtOrBelow=count))
    return levels, closes


def excited_blocks(inp, summary, scf_rows):
    scf_by_label = {row["label"]: row for row in scf_rows}
    table, refinements, smeared = [], [], []
    for record in summary["runs"]:
        row = run_identity(record)
        params = record.get("parameters") or {}
        scf = scf_by_label.get(record["label"], {})
        row["gridPoints"] = params.get("gridPoints", scf.get("gridPoints"))
        row.update(pick(record, ["E0", "mu", "epsHomo", "epsLumo", "ksGap", "deltaScf", "E1", "lowestParticleHole",
                                 "maxLambdaSOverM", "groundIterations", "excitedIterations"]))
        if "exactZeroTemperatureOccupations" in record:
            # the excited record carries the parameters of its own converged ground state
            row["exactZeroTemperatureOccupations"] = record["exactZeroTemperatureOccupations"]
            row["occupationSmearing"] = params.get("occupationSmearing")
            row["zeroTemperatureFallbackStage"] = params.get("zeroTemperatureFallbackStage")
            row["occupationSource"] = "excited record"
        else:
            row["exactZeroTemperatureOccupations"] = scf.get("exactZeroTemperatureOccupations")
            row["occupationSmearing"] = scf.get("occupationSmearing")
            row["zeroTemperatureFallbackStage"] = scf.get("zeroTemperatureFallbackStage")
            row["occupationSource"] = "scf run of the same label" if scf else "not recorded"
        row["particleHoleFirst"] = particle_hole_rows(inp, record["label"])
        (refinements if row["suffix"] else table).append(row)
        if row["exactZeroTemperatureOccupations"] is False:
            levels, closes = fractional_levels(inp, record["label"], row["N"])
            smeared.append({"label": record["label"], "gridPoints": row["gridPoints"],
                            "occupationSmearing": row["occupationSmearing"],
                            "zeroTemperatureFallbackStage": row["zeroTemperatureFallbackStage"],
                            "N": row["N"], "ksGap": row["ksGap"], "deltaScf": row["deltaScf"],
                            "aufbauCountClosesAt": closes,
                            "fractionallyOccupiedLevels": levels,
                            "particleHoleFirst": row["particleHoleFirst"]})
    global_checks = {name: passed for name, passed in summary["checks"].items() if not re.match(r"^m\d", name)}
    return table, refinements, smeared, global_checks


def thermo_block(summary):
    runs = []
    for record in summary["runs"]:
        row = run_identity(record)
        row.update(pick(record, ["converged", "iterations", "energy", "freeEnergy", "entropy", "mu",
                                 "grandPotential", "heatCapacity", "heatCapacityFiniteDifference",
                                 "heatCapacityFixedSpectrum", "heatCapacityFixedSpectrumFromEntropy",
                                 "maxLambdaSOverM", "maxVxOverM", "states"]))
        runs.append(row)
    return {"temperaturesOverM": summary.get("temperaturesOverM"), "seriesRule": summary.get("seriesRule"),
            "heatCapacity": summary.get("heatCapacity"), "series": summary.get("series"),
            "skippedRuns": summary.get("skippedRuns"), "runs": runs}


def emt_block(summary):
    runs = []
    for record in summary["runs"]:
        row = run_identity(record)
        row.update(pick(record, ["energy", "converged"]))
        row.update(emt_subset(record))
        runs.append(row)
    return {"requiredSource": summary.get("requiredSource"), "E41": summary.get("E41"),
            "sourcingThreeConditions": summary.get("sourcingThreeConditions"),
            "positiveRhoExpectation": summary.get("positiveRhoExpectation"), "runs": runs}


# ------------------------------------------------------ rust vs reference --

VALUE_KEYS = ["rust", "reference", "referenceLambdaCorrected", "truncationCorrection", "deviation", "tolerance"]


def comparison_values(detail):
    out = {}
    for key in ("E0", "mu", "ksGap", "deltaSCF", "lowestParticleHole"):
        if isinstance(detail.get(key), dict):
            out[key] = pick(detail[key], VALUE_KEYS)
    if isinstance(detail.get("eigenvalues"), dict):
        out["eigenvalues"] = pick(detail["eigenvalues"], ["compared", "unmatched", "maxAbsDeviation",
                                                          "maxDeviationOverTolerance", "branchMismatches",
                                                          "occupationMismatches"])
    if isinstance(detail.get("lambdaHat"), dict):
        out["lambdaHat"] = pick(detail["lambdaHat"], ["rust", "reference", "relativeDifference"])
    if isinstance(detail.get("occupationSmearing"), dict):
        out["occupationSmearing"] = detail["occupationSmearing"]
    emt = detail.get("emt")
    if isinstance(emt, dict):
        # the deviation only (relative for the averages, absolute for the fractions)
        out["emtDeviation"] = {key: value.get("relative", value.get("absolute"))
                               for key, value in emt.items() if isinstance(value, dict) and key != "E41"}
        if isinstance(emt.get("E41"), dict):
            out["emtDeviation"]["E41agree"] = emt["E41"].get("agree")
    thermo = detail.get("thermo")
    if isinstance(thermo, dict):
        out["thermo"] = {key: pick(value, ["deviation", "tolerance", "truncationCorrection"])
                         for key, value in thermo.items() if isinstance(value, dict) and key != "truncation"}
    return out


def rust_versus_reference(report):
    checks, measurements = report["checks"], report.get("measurements", {})
    families = {}
    for name, passed in checks.items():
        if name.startswith("canonical_"):
            family = name[len("canonical_"):]
            families[family] = {"passed": passed, "worstRatio": measurements.get("canonicalWorstRatio_" + family),
                                "detail": measurements.get(name + "_detail")}
    runs, reproductions, not_run = [], [], []
    for name, entry in report.get("comparisons", {}).items():
        status = entry.get("status")
        detail = entry.get("detail")
        if name.startswith("canonical_"):
            sub, _, label = name[len("canonical_"):].partition("_")
            if status == "ran" and isinstance(detail, dict):
                runs.append(dict({"subcommand": sub, "label": label, "referenceLabel": detail.get("referenceLabel")},
                                 **comparison_values(detail)))
            else:
                not_run.append({"comparison": name, "status": status, "detail": detail})
        elif name.startswith("reproduce_"):
            reproductions.append({"comparison": name, "status": status, "passed": checks.get(name),
                                  "values": comparison_values(detail) if isinstance(detail, dict) else detail})
        elif status != "ran":
            not_run.append({"comparison": name, "status": status, "detail": detail})
    return {
        "source": CANONICAL_ROOT + "/python-check-report.json",
        "tolerances": report.get("tolerances"),
        "families": families,
        "runs": runs,
        "reproductions": reproductions,
        "stationarity": {name: checks.get(name) for name in checks if name.startswith("stationarity_")},
        "stationarityRelative": pick(measurements, ["stationarity_dF_dlambda_relative", "stationarity_dF_dm_relative"]),
        "notRun": not_run,
        "canonicalWithoutReferenceRun": measurements.get("canonicalWithoutReferenceRun"),
        "rustFreeN8GapByL": measurements.get("rustFreeN8GapByL"),
        "referenceFirstLevelByL": measurements.get("referenceFirstLevelByL"),
        "referenceCouplings": measurements.get("referenceCouplings"),
    }


# ----------------------------------------------------------------- main --

def build(root, allow_incomplete=False):
    inp = Inputs(root, allow_incomplete)
    fixture_sha = inp.sha(FIXTURE, repository=True)
    theory_blocks, theory, table_sha = theory_producers(inp, fixture_sha)
    rust_blocks, summaries, header = rust_producers(inp, fixture_sha, table_sha)
    agreement = inp.json("rust/spectrum/theory-agreement.json")
    inp.require("theory_agreement_theory_json", agreement.get("sha256") == inp.sha("kohn-sham-theory.json"),
                "rust/spectrum/theory-agreement.json compared kohn-sham-theory.json %s (file %s)"
                % (agreement.get("sha256"), inp.sha("kohn-sham-theory.json")))
    determinism = determinism_producer(inp)
    reference = reference_producer(inp, fixture_sha)
    cross, report = cross_check_producer(inp)
    notebook = optional_producer(inp, "notebook-report.json", fixture_sha)
    mathematica = optional_producer(inp, "mathematica-report.json", fixture_sha)

    scf_rows = scf_table(summaries["scf"])
    excited, refinements, smeared, excited_checks = excited_blocks(inp, summaries["excited"], scf_rows)
    spectrum = summaries["spectrum"]
    physics = {
        "units": "H = 1; energies, eps, mu, gaps and temperatures in units of m unless stated (m/H = 1 or 3); "
                 "lambda_hat = lambda m^6",
        "geometry": geometry_block(theory),
        "spectrum": {
            "closedShells": pick(spectrum["reference"], ["nMid", "nLarge", "nMidM3"]),
            "closedShells_m1_L3_N_epsHomo": spectrum["reference"].get("closedShells_m1_L3_N_epsHomo"),
            "closedShells_m3_L3_N_epsHomo": spectrum["reference"].get("closedShells_m3_L3_N_epsHomo"),
            "zeroModeSplitting": dig(agreement, "checks", "theory_zero_mode_splitting"),
            "exchangeTable": pick(spectrum.get("exchangeTable") or {}, ["status"]),
        },
        "couplings": {
            "rule": spectrum["reference"].get("couplingRule"),
            "perConfiguration": [pick(entry, ["m", "L", "N", "strengthPerUnitLambdaHat", "lambdaHat1", "lambdaHat2",
                                              "sRef_maxProperScalarDensity_free",
                                              "nRef_maxProperNumberDensity_free"])
                                 for entry in spectrum["reference"].get("couplings", [])],
            "hot": [pick(series, ["N", "lambdaHat1", "lambdaHatHot", "temperaturesRun_lambdaHat1",
                                  "temperaturesRun_lambdaHatHot"]) for series in summaries["thermo"].get("series", [])],
        },
        "groundAndExcited": excited,
        "excitedRefinements": refinements,
        "excitedGlobalChecks": excited_checks,
        "smearedGroundStates": {
            "note": "T = 0 ground states converged only with Fermi-Dirac occupation smearing at the physical "
                    "T = 0 (F = E) after a level crossing at the Fermi level (scf.rs fallback): their KS gap, "
                    "Delta-SCF and particle-hole list refer to the smeared ensemble; the particle-hole pairs of "
                    "T = 0 runs count a state as a hole when f exceeds the occupation floor and as a particle when "
                    "1 - f exceeds it (runs.rs PH_OCCUPATION_FLOOR, the reference solver's T = 0 rule), so the "
                    "Fermi-Dirac tails are excluded; fractionallyOccupiedLevels lists the particle-branch levels "
                    "of the excited run's levels.csv strictly between the floor and 1 - floor, each with "
                    "statesAtOrBelow = the number of particle-branch states (multiplicities counted, eps "
                    "order) up to and including it; aufbauCountClosesAt is the level at which that count "
                    "equals N (the exact T = 0 aufbau count closes there, so the smeared ensemble is not an "
                    "open shell of the aufbau), null if no level closes it",
            "runs": smeared,
        },
        "scfRuns": scf_rows,
        "scfGlobalChecks": {name: passed for name, passed in summaries["scf"]["checks"].items()
                            if not re.match(r"^m\d", name)},
        "lConvergence": l_convergence(scf_rows),
        "thermodynamics": thermo_block(summaries["thermo"]),
        "emt": emt_block(summaries["emt"]),
    }
    producers = {"wolfram": theory_blocks["wolfram"], "sympy": theory_blocks["sympy"],
                 "constantsGenerator": theory_blocks["constantsGenerator"], "rust": rust_blocks,
                 "determinism": determinism, "reference": reference, "crossChecker": cross,
                 "notebook": notebook, "mathematica": mathematica}
    counted = [("wolfram", theory_blocks["wolfram"]), ("sympy", theory_blocks["sympy"]),
               ("constantsGenerator", theory_blocks["constantsGenerator"])]
    counted += [("rust_" + sub, rust_blocks[sub]) for sub in SUBCOMMANDS]
    counted += [("determinism", determinism), ("crossChecker", cross)]
    counted += [(name, block) for name, block in (("notebook", notebook), ("mathematica", mathematica))
                if block["status"] == "present"]
    totals = {"checks": sum(block["checkCount"] for _, block in counted),
              "failed": sum(block["failedCount"] for _, block in counted),
              "byProducer": {name: {"checks": block["checkCount"], "failed": block["failedCount"]}
                             for name, block in counted},
              "notCounted": [name for name, block in (("notebook", notebook), ("mathematica", mathematica))
                             if block["status"] != "present"] + ["reference (its self-tests and runs are "
                                                                 "judged by the cross-checker)"]}
    verdicts_ok = all(rust_blocks[sub]["verdict"] == "SUCCESS" for sub in SUBCOMMANDS)
    verdicts_ok &= all(block.get("verdict") in (None, "SUCCESS") for block in (notebook, mathematica)
                       if block["status"] == "present")
    verdicts_ok &= not reference["notConverged"] and not reference["failed"]
    if inp.stale and not allow_incomplete:
        raise SummaryError("stale or incomplete inputs (use --allow-incomplete for a preview):\n  "
                           + "\n  ".join(inp.stale))
    if totals["failed"] or not verdicts_ok:
        verdict = "FAILURE"
    elif inp.stale:
        verdict = "INCOMPLETE"
    else:
        verdict = "SUCCESS"
    document = {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "root": CANONICAL_ROOT,
        "study": header["study"],
        "engine": header["engine"],
        "solver": header["solver"],
        "fixture": {"path": FIXTURE, "sha256": fixture_sha},
        "provenance": ("Every number below is copied from the listed input files (the Wolfram and sympy theory "
                       "reports, the constants generator report, the Rust summaries of the canonical run and "
                       "selected rows of its CSV files, the determinism report, the reference-solver summary, the "
                       "cross-checker report, and the notebook and Mathematica reports when present); nothing is "
                       "recomputed here. NaN or infinite source values are written as null."),
        "verdict": verdict,
        "incompleteInputs": inp.stale,
        "totals": totals,
        "producers": producers,
        "consistency": inp.consistency,
        "physics": physics,
        "rustVersusReference": rust_versus_reference(report),
        "inputs": sorted(inp.sources, key=lambda entry: entry["path"]),
    }
    return clean(document)


def render(document):
    text = json.dumps(document, indent=2, allow_nan=False) + "\n"
    for needle in (REPO, REPO.replace("\\", "/"), REPO.replace("/", "\\")):
        if needle and needle in text:
            raise SummaryError("the summary would contain the absolute repository path %s" % needle)
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=DEFAULT_ROOT, help="the kohn-sham artifact directory to read")
    parser.add_argument("--output", default=None, help="default <root>/kohn-sham-summary.json")
    parser.add_argument("--allow-incomplete", action="store_true",
                        help="write a preview (verdict INCOMPLETE, exit 3) when inputs are stale or incomplete")
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.root)
    output = os.path.abspath(arguments.output or os.path.join(root, "kohn-sham-summary.json"))
    try:
        document = build(root, arguments.allow_incomplete)
        text = render(document)
    except (SummaryError, KeyError, TypeError, ValueError) as error:
        print("ERROR: %s: %s" % (type(error).__name__, error))
        print("REFUSED")
        return 1
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    for name, block in document["totals"]["byProducer"].items():
        print("%s: %d checks, %d failed" % (name, block["checks"], block["failed"]))
    for problem in document["incompleteInputs"]:
        print("incomplete: %s" % problem)
    totals = document["totals"]
    print("totals: %d checks, %d failed; inputs %d files" % (totals["checks"], totals["failed"],
                                                               len(document["inputs"])))
    print("wrote %s" % output)
    print(document["verdict"])
    return {"SUCCESS": 0, "FAILURE": 1, "INCOMPLETE": 3}[document["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
