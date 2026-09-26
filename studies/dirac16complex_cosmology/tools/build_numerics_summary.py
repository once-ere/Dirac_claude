"""Collect the Stage-3 numerics results into artifacts/dirac16complex/numerics/numerics-summary.json.

Standard library only.  Nothing is computed here: every number is copied
from the committed outputs of the Rust study and of the Python checkers,

  <root>/expN/summary.json               (Rust self-checks, solver totals, measurements)
  <root>/expN/python-check-report.json   (scripts/check_dirac16complex_expN.py)
  <root>/exp3/fits.json                  (scripts/analyze_dirac16complex_exp3.py)

and the SHA-256 of each source file is recorded, so the summary is tied to
exactly the data it describes.  The script refuses (exit 1) when an input is
missing, when the fixture hash differs between inputs, or when a checker
report was produced without --repeat / --refined; it reports (but does not
hide) any failed check.

Order of the pipeline (from the repository root):

  cargo build --release   (in studies/dirac16complex_cosmology)
  studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology all
  python scripts/analyze_dirac16complex_exp3.py
  python scripts/check_dirac16complex_expN.py --repeat DIR_N --refined DIR_N'   (N = 1..5)
  python studies/dirac16complex_cosmology/tools/build_numerics_summary.py

Usage: python studies/dirac16complex_cosmology/tools/build_numerics_summary.py [--output ROOT]
Writes <ROOT>/numerics-summary.json (fixed key order, 2-space indent, LF).
"""

import argparse
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DEFAULT_ROOT = os.path.join(REPO, "artifacts", "dirac16complex", "numerics")
PRODUCER = "studies/dirac16complex_cosmology/tools/build_numerics_summary.py"
EXPERIMENTS = [
    ("exp1", "Primordial (pair-creation) field: frozen dirac16complex"),
    ("exp2", "Self-consistent 8D Einstein - dirac16complex homogeneous cosmology"),
    ("exp3", "4D-effective late universe: dirac16complex condensate as dark energy"),
    ("exp4", "dirac16complex quanta as dark matter: Fermi gas EoS and pair creation"),
    ("exp5", "Extra-time sector: the ultrahyperbolic instability"),
]
OPTIONAL_CHECKS = ["repeatByteIdentity", "refinedConvergence"]


class SummaryError(Exception):
    pass


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def load(root, relative):
    path = os.path.join(root, relative)
    if not os.path.exists(path):
        raise SummaryError("missing input %s" % path)
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)
    return document, {"path": relative.replace(os.sep, "/"), "sha256": sha256_file(path)}


def pick(mapping, keys):
    return {key: mapping[key] for key in keys if key in mapping}


# --------------------------------------------------------------- blocks --

def rust_block(summary):
    checks = summary["checks"]
    failed = [name for name, passed in checks.items() if not passed]
    return {
        "verdict": summary["verdict"],
        "checkCount": len(checks),
        "passedCount": len(checks) - len(failed),
        "failedCount": len(failed),
        "failed": failed,
        "checks": checks,
    }


def python_block(report):
    checks = report["checks"]
    failed = [name for name, passed in checks.items() if not passed]
    missing = [name for name in OPTIONAL_CHECKS if name not in checks]
    if missing:
        raise SummaryError("%s was not run with --repeat/--refined (missing %s)"
                           % (report["checker"], ", ".join(missing)))
    return {
        "checker": report["checker"],
        "verdict": report["verdict"],
        "checkCount": report["checkCount"],
        "passedCount": report["checkCount"] - report["failedCheckCount"],
        "failedCount": report["failedCheckCount"],
        "failed": failed,
        "repeatByteIdentity": checks["repeatByteIdentity"],
        "refinedConvergence": checks["refinedConvergence"],
        "checks": checks,
    }


def solver_block(summary):
    return {
        "method": summary["solver"],
        "refined": summary["refined"],
        "tolerances": summary["tolerances"],
        "steps": summary["solverTotals"]["steps"],
        "rhsEvaluations": summary["solverTotals"]["rhsEvaluations"],
        "outputFiles": len(summary["files"]),
    }


# ------------------------------------------------------ key results -----

def key_exp1(summary, report):
    runs = summary["runs"]
    eigenmodes = []
    for run in runs:
        if run["profile"] == "A1" and run["initialSpinor"] == "pos_Bp" and run["lambda"] == 0.0:
            initial = run["initial"]
            eigenmodes.append({
                "run": run["id"], "hiddenMomentumK": run["hiddenMomentumK"], "energyE": run["energyE"],
                "rho": initial["rho"], "p0": initial["p"][0], "pMean": initial["pMean"], "w": initial["w"],
                "KE_L": initial["KE_L"], "PE_L": initial["PE_L"], "w_L": initial["w_L"], "S": initial["S"],
            })
    return {
        "runCount": len(runs),
        "grid": summary["grid"],
        "einsteinRequirement": [pick(b, ["profile", "amplitude", "a4Final", "rhoReqMin", "rhoReqMax",
                                         "wReqMin", "wReqMax"]) for b in summary["backgrounds"]],
        "lambdaSelfConsistentMass": summary["parameters"]["lambdaSelfConsistentMass"],
        "freeEigenmodes": eigenmodes,
        "limits": summary["limits"],
        "rustMeasurements": summary["measurements"],
        "pythonMeasurements": report["measurements"],
        "notes": summary["notes"],
    }


def key_exp2(summary, report):
    runs = []
    for run in summary["runs"]:
        exact, grid, measured = run["exact"], run["grid"], run["measurements"]
        runs.append({
            "run": run["id"], "x0": run["x0"], "S0": run["S0"], "lambda": run["lambda"], "mEff0": run["mEff0"],
            "rho0": run["rho0"],
            "exact": pick(exact, ["theta0", "alpha", "beta", "singularityTime", "kasnerExponents",
                                  "kasnerSumSquares", "extraTimeTurnTime", "mEffZeroVolume", "rhoZeroVolume"]),
            "grid": grid,
            "measured": pick(measured, ["maxConstraintRelative", "maxScalarDensityDrift", "maxAnisotropyVolumeDrift",
                                        "maxExactVolumeError", "maxExactSpinorError", "maxSpinorShapeError",
                                        "maxSpinorPhaseError", "spinorPhaseRoundingBound",
                                        "minThetaOver3HaPositiveEnergy", "minWeffPositiveEnergy",
                                        "negativeKineticRows", "phantomRows", "phantomVolumeMin", "phantomVolumeMax",
                                        "negativeEnergyRows", "negativeEnergyVolumeMax", "minRho",
                                        "finalAnisotropy", "finalHubbleTimesT", "finalW", "finalWeff",
                                        "extraTimeTurnTimeMeasured", "kasnerExtrapolated",
                                        "kasnerSumSquaresExtrapolated"]),
        })
    return {
        "runs": runs,
        "thetaOver3HaMinAllRows": report["measurements"]["thetaOver3HaMinAllRows"],
        "limits": summary["limits"],
        "rustMeasurements": summary["measurements"],
        "pythonMeasurements": report["measurements"],
        "notes": summary["notes"],
    }


def key_exp3(summary, report, fits):
    models = []
    fit_models = {block["x0"]: block for block in fits["models"]}
    runs_by_x0 = {}
    for run in summary["runs"]:
        runs_by_x0.setdefault(run["x0"], []).append(run)
    for model in summary["models"]:
        x0 = model["x0"]
        block = dict(model)
        fit = fit_models[x0]
        block["tangentMinusUnite"] = fit["tangentMinusUnite"]
        block["wFitRequested"] = fit["wFitRequested"]
        block["muFitRequested"] = fit["muFitRequested"]
        restricted_w = fit["wFitRestricted"]
        block["wFitRestricted"] = pick(restricted_w, ["range", "w0", "wa", "rmsResidual", "status", "reason"])
        restricted_mu = fit["muFitRestricted"]
        block["muFitRestricted"] = {
            "range": restricted_mu.get("range"),
            "points": restricted_mu.get("points"),
            "cplOffsetProfiled": pick(restricted_mu.get("cplOffsetProfiled", {}), ["w0", "wa", "rmsResidualMag"]),
            "wConstantOffsetProfiled": pick(restricted_mu.get("wConstantOffsetProfiled", {}),
                                            ["w", "rmsResidualMag"]),
        }
        block["muVsUniteCPL"] = fit.get("muVsUniteCPL")
        block["runs"] = [{
            "run": run["id"], "mu": run["mu"], "massOverH0": run["massOverH0"],
            "backwardEnd": pick(run["backward"], ["nEnd", "aEnd", "zEnd", "reachedContractMinimum",
                                                  "stopConsistentWithBounce"]),
            "decelerationSignChanges": run["measured"]["decelerationSignChanges"],
        } for run in runs_by_x0.get(x0, [])]
        models.append(block)
    gamma = fits["gammaVariant"]
    return {
        "parameters": summary["parameters"],
        "models": models,
        "unite": fits["unite"],
        "gammaVariant": {
            "definition": gamma["definition"],
            "x0": gamma["x0"], "n": gamma["n"], "gamma": gamma["gamma"],
            "tangentCPLofPressureRatio": gamma["tangentCPLofPressureRatio"],
            "tangentCPLofEffectiveW": gamma["tangentCPLofEffectiveW"],
            "effectiveWFitRequested": gamma["effectiveWFitRequested"],
            "objections": gamma["objections"],
        },
        "scan": {key: value for key, value in fits["scan"].items()
                 if key not in ("columns", "muScanColumns")},
        "muIndependence": summary["muIndependence"],
        "limits": summary["limits"],
        "rustMeasurements": summary["measurements"],
        "pythonMeasurements": report["measurements"],
        "contractDeviations": summary["contractDeviations"],
        "notes": summary["notes"],
    }


def key_exp4(summary, report):
    thermal = {key: value for key, value in summary["thermal"].items() if key != "modeSolverStats"}
    pair = {key: value for key, value in summary["pair"].items() if key != "masses"}
    masses = [pick(block, ["m", "a2End", "tEnd", "nA3", "nA3Instantaneous", "nA3AtKink",
                           "nA3KinkTailBeyondKMax", "nA3TailCorrected", "rhoA3End", "rhoA3EndTailCorrected",
                           "wFrozenSpectrumAtA1", "wEnd", "wFrozenSpectrumAtA1TailCorrected",
                           "wEndTailCorrected", "wFrozenSpectrumAtA1Instantaneous", "wEndInstantaneous",
                           "maxBeta2", "maxBeta2Adiabatic", "kPeakK3Beta2", "tailNodes", "tailMaxRelDev"])
              for block in summary["pair"]["masses"]]
    selection = summary["methodSelection"]
    return {
        "parameters": summary["parameters"],
        "counting": summary["counting"],
        "methodSelection": {
            "selected": selection["selected"],
            "rule": selection["rule"],
            "trials": [pick(t, ["node", "k", "method", "steps", "rhsEvals", "maxErrorVsReference"])
                       for t in selection["trials"]],
        },
        "thermal": thermal,
        "pair": pair,
        "pairMasses": masses,
        "limits": summary["limits"],
        "pythonMeasurements": report["measurements"],
        "findings": summary["findings"],
    }


def key_exp5(summary, report):
    runs = []
    for run in summary["runs"]:
        runs.append({
            "run": run["id"], "q": run["q"], "cSign": run["cSign"], "tStar": run["tStar"], "tEnd": run["tEnd"],
            "energy0": run["energy0"], "kreinNorm0": run["kreinNorm0"],
            "finalNormHilbert": run["finalNormHilbert"], "kreinDrift": run["kreinDrift"],
            "wkb": run["wkb"], "rateEarly": run["rateEarly"], "rateLate": run["rateLate"],
        })
    return {
        "parameters": summary["parameters"],
        "runs": runs,
        "limits": summary["limits"],
        "rustMeasurements": summary["measurements"],
        "pythonMeasurements": report["measurements"],
        "notes": summary["notes"],
    }


KEY = {"exp1": key_exp1, "exp2": key_exp2, "exp4": key_exp4, "exp5": key_exp5}


# ----------------------------------------------------------------- main --

def build(root):
    fixture = None
    blocks = []
    totals = {"rustChecks": 0, "rustFailed": 0, "pythonChecks": 0, "pythonFailed": 0,
              "analysisChecks": 0, "analysisFailed": 0, "solverSteps": 0, "rhsEvaluations": 0}
    engine = study = None
    for name, title in EXPERIMENTS:
        summary, summary_source = load(root, os.path.join(name, "summary.json"))
        report, report_source = load(root, os.path.join(name, "python-check-report.json"))
        if summary["experiment"] != name or report["experiment"] != name:
            raise SummaryError("%s: experiment label mismatch" % name)
        if fixture is None:
            fixture = summary["fixture"]
            engine, study = summary["engine"], summary["study"]
        for label, value in (("summary.json", summary["fixture"]["sha256"]),
                             ("python-check-report.json", report["fixtureSha256"])):
            if value != fixture["sha256"]:
                raise SummaryError("%s/%s: fixture hash %s differs from %s" % (name, label, value, fixture["sha256"]))
        if summary["refined"]:
            raise SummaryError("%s/summary.json comes from a --refined run, not the canonical one" % name)
        sources = [summary_source, report_source]
        block = {
            "experiment": name,
            "title": title,
            "rust": rust_block(summary),
            "python": python_block(report),
        }
        if name == "exp3":
            fits, fits_source = load(root, os.path.join(name, "fits.json"))
            sources.append(fits_source)
            validation = fits["validation"]["checks"]
            analysis_failed = [key for key, passed in validation.items() if not passed]
            block["analysis"] = {
                "producer": fits["producer"],
                "verdict": fits["verdict"],
                "checkCount": len(validation),
                "passedCount": len(validation) - len(analysis_failed),
                "failedCount": len(analysis_failed),
                "failed": analysis_failed,
                "checks": validation,
            }
            totals["analysisChecks"] += len(validation)
            totals["analysisFailed"] += len(analysis_failed)
            key = key_exp3(summary, report, fits)
        else:
            key = KEY[name](summary, report)
        block["solver"] = solver_block(summary)
        block["keyResults"] = key
        block["sources"] = sources
        totals["rustChecks"] += block["rust"]["checkCount"]
        totals["rustFailed"] += block["rust"]["failedCount"]
        totals["pythonChecks"] += block["python"]["checkCount"]
        totals["pythonFailed"] += block["python"]["failedCount"]
        totals["solverSteps"] += block["solver"]["steps"]
        totals["rhsEvaluations"] += block["solver"]["rhsEvaluations"]
        blocks.append(block)
    all_passed = all(b["rust"]["verdict"] == "SUCCESS" and b["python"]["verdict"] == "SUCCESS"
                     and b.get("analysis", {"verdict": "SUCCESS"})["verdict"] == "SUCCESS" for b in blocks)
    all_passed &= totals["rustFailed"] == 0 and totals["pythonFailed"] == 0 and totals["analysisFailed"] == 0
    document = {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "study": study,
        "engine": engine,
        "fixture": fixture,
        "provenance": ("Every number below is copied from the listed source files (summary.json of the Rust "
                       "study, python-check-report.json of the independent checkers, fits.json of the EXP-3 "
                       "analysis); nothing is recomputed here. The checker reports include the repeat-run "
                       "byte-identity check (--repeat) and the refined-tolerance convergence check (--refined)."),
        "totals": totals,
        "verdict": "SUCCESS" if all_passed else "FAILURE",
        "experiments": blocks,
    }
    return document


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    arguments = parser.parse_args(argv)
    root = os.path.abspath(arguments.output)
    try:
        document = build(root)
    except (SummaryError, KeyError, ValueError) as error:
        print("ERROR: %s" % error)
        print("FAILURE")
        return 1
    path = os.path.join(root, "numerics-summary.json")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(document, indent=2, allow_nan=False) + "\n")
    for block in document["experiments"]:
        line = "%s: rust %d/%d, python %d/%d (repeat=%s, refined=%s)" % (
            block["experiment"], block["rust"]["passedCount"], block["rust"]["checkCount"],
            block["python"]["passedCount"], block["python"]["checkCount"],
            block["python"]["repeatByteIdentity"], block["python"]["refinedConvergence"])
        if "analysis" in block:
            line += ", analysis %d/%d" % (block["analysis"]["passedCount"], block["analysis"]["checkCount"])
        line += ", steps=%d, rhs=%d" % (block["solver"]["steps"], block["solver"]["rhsEvaluations"])
        print(line)
    totals = document["totals"]
    print("totals: rust %d checks (%d failed), python %d checks (%d failed), analysis %d checks (%d failed)"
          % (totals["rustChecks"], totals["rustFailed"], totals["pythonChecks"], totals["pythonFailed"],
             totals["analysisChecks"], totals["analysisFailed"]))
    print("wrote %s" % path)
    print(document["verdict"])
    return 0 if document["verdict"] == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
