"""Unit tests of the Stage-4 integration tools (standard library only).

  * studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py: on a
    small synthetic input tree (written into a temporary directory by this
    test, never committed) the summary copies the numbers, is byte-identical
    on repetition and independent of the root location, records the SHA-256
    of every input, and refuses missing inputs, inconsistent fixture hashes,
    a --refined Rust summary and stale reports (a preview with
    --allow-incomplete is marked INCOMPLETE); a failed producer check gives
    verdict FAILURE; the fallback parameters of an excited record are taken
    from the record itself, and the aufbau count of a smeared run is counted.
  * scripts/verify_stage4_kohn_sham_audit.py: the same / rust-run /
    rust-outputs / snapshot / unchanged / fresh / determinism /
    reference-quick / checker-report subcommands, each with a negative
    control (rust-run with stand-in subcommand scripts run by this Python:
    concurrent and sequential, a failing job stops the others).
  * scripts/verify_stage4_kohn_sham.{ps1,sh}: both twins list the same steps
    in the same order with the same expected wall times (their --dry-run /
    -DryRun output), launch the same Rust jobs (concurrent by default,
    --sequential-rust / -SequentialRust, --refined-thermo / -RefinedThermo),
    select steps with --steps / -Steps, end with the same final lines and are
    LF-only.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_gate.py" -v
Nothing here runs the gate itself, a solver or a notebook.
"""

import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDER_PATH = os.path.join(REPO, "studies", "dirac16complex_kohn_sham", "tools", "build_kohn_sham_summary.py")
AUDIT_PATH = os.path.join(REPO, "scripts", "verify_stage4_kohn_sham_audit.py")
GATE_PS1 = os.path.join(REPO, "scripts", "verify_stage4_kohn_sham.ps1")
GATE_SH = os.path.join(REPO, "scripts", "verify_stage4_kohn_sham.sh")
FIXTURE = "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"
SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_module("build_kohn_sham_summary", BUILDER_PATH)
audit = load_module("verify_stage4_kohn_sham_audit", AUDIT_PATH)


def sha_repo(relative):
    with open(os.path.join(REPO, *relative.split("/")), "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def sha_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def write_json(path, document):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(document, indent=2) + "\n")


def write_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


LEVELS_HEADER = ("n2,k,multiplicity,parity,s,index,eps,branch,eps_free,f,weight,scalar_charge,pressure_charge,"
                 "matching_residual,winding_residual,sign_changes,theta_residual\n")


def level_row(n2, k, mult, eps, f, branch=1.0):
    values = [n2, k, mult, 1.0, 1.0, 0.0, eps, branch, eps, f, f, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    return ",".join("%.17e" % v for v in values) + "\n"


def make_root(root):
    """A minimal, internally consistent synthetic input tree (test data)."""
    fixture = sha_repo(FIXTURE)
    wolfram_sources = {"wolfram/Dirac16ComplexKohnSham.wl": sha_repo("wolfram/Dirac16ComplexKohnSham.wl"),
                       "scripts/verify_dirac16complex_kohn_sham.wls":
                           sha_repo("scripts/verify_dirac16complex_kohn_sham.wls"),
                       FIXTURE: fixture}
    write_json(os.path.join(root, "wolfram-kohn-sham-report.json"),
               {"schemaVersion": 1, "producer": "wolfram", "checks": {"a": True, "b": True}, "measurements": {},
                "sourceSha256": wolfram_sources})
    theory = {"schemaVersion": 1, "producer": "wolfram", "sourceSha256": wolfram_sources,
              "geometry": {"curvature": {"ricciScalar": "R = -42 H^2",
                                         "einsteinMixedValues": ["15", "15", "15", "15", "21", "15", "15", "15"]},
                           "requiredSource": {"rhoValue": "-21", "pValue": "15", "w": "w_req = -5/7"},
                           "extensions": {"E2_Z2mirror": {"braneEnergyDensity": "rho_brane = +12 H/kappa"}}}}
    write_json(os.path.join(root, "kohn-sham-theory.json"), theory)
    theory_sha = sha_file(os.path.join(root, "kohn-sham-theory.json"))
    write_json(os.path.join(root, "python-theory-report.json"),
               {"schemaVersion": 1, "producer": "sympy", "checks": {"c": True},
                "measurements": {"wolframAgreement": "compared", "exchangeTable": {"rows": 3}},
                "sourceSha256": {"scripts/check_dirac16complex_kohn_sham_theory.py":
                                 sha_repo("scripts/check_dirac16complex_kohn_sham_theory.py")},
                "inputSha256": {FIXTURE: fixture, "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json": theory_sha}})
    write_json(os.path.join(root, "exchange-table.json"), {"rows": []})
    table_sha = sha_file(os.path.join(root, "exchange-table.json"))
    write_json(os.path.join(root, "rust", "generator-report.json"),
               {"schemaVersion": 1, "producer": "generator", "checks": {"g": True},
                "sourceSha256": {FIXTURE: fixture, "studies/dirac16complex_kohn_sham/src/generated.rs":
                                 sha_repo("studies/dirac16complex_kohn_sham/src/generated.rs")}})
    common = {"schemaVersion": 1, "study": "dirac16complex-kohn-sham", "fixture": {"path": FIXTURE, "sha256": fixture},
              "engine": "engine", "solver": "solver", "refined": False,
              "tolerances": {"rtol": 1e-12, "atol": 1e-14, "maxStep": 0.05},
              "reference": {"nMid": 112.0, "nLarge": 1016.0, "nMidM3": 112.0, "couplingRule": "rule",
                            "couplings": [{"m": 1.0, "L": 3.0, "N": 8.0, "strengthPerUnitLambdaHat": 10.0,
                                           "lambdaHat1": 0.01, "lambdaHat2": 0.1}]},
              "solverTotals": {"steps": 10, "rhsEvaluations": 20}, "verdict": "SUCCESS"}
    scf_run = {"label": "m1_L3_N8_lam0_T0", "lambdaName": "lam0",
               "parameters": {"m": 1.0, "L": 3.0, "N": 8.0, "T": 0.0, "lambdaHat": 0.0, "occupationSmearing": 0.0,
                              "zeroTemperatureFallbackStage": 0},
               "converged": True, "exactZeroTemperatureOccupations": True, "energy": 0.0, "mu": 0.0, "ksGap": 0.43,
               "emt": {"rhoAvg": 0.0, "braneFraction_within_1_over_H": 0.87,
                       "E41_sourcingConditions": {"met": False}}}
    scf_l2 = copy.deepcopy(scf_run)
    scf_l2.update({"label": "m1_L2_N8_lam0_T0", "ksGap": 0.42})
    scf_l2["parameters"]["L"] = 2.0
    smeared = copy.deepcopy(scf_run)
    smeared.update({"label": "m1_L3_N1016_lamm2_T0", "lambdaName": "lamm2", "exactZeroTemperatureOccupations": False})
    smeared["parameters"].update({"N": 1016.0, "lambdaHat": -0.0015, "occupationSmearing": 0.001,
                                  "zeroTemperatureFallbackStage": 1})
    excited_runs = [{"label": "m1_L3_N8_lam0_T0", "N": 8.0, "lambdaHat": 0.0, "E0": 0.0, "mu": 0.0,
                     "epsHomo": 0.0, "epsLumo": 0.4307336786379114, "ksGap": 0.4307336786379114,
                     "deltaScf": 0.4307336786379114, "E1": 0.4307336786379114,
                     "lowestParticleHole": 0.4307336786379114, "maxLambdaSOverM": 0.0},
                    {"label": "m1_L3_N1016_lamm2_T0", "N": 1016.0, "lambdaHat": -0.0015, "E0": 1126.8,
                     "mu": 1.39, "epsHomo": 1.389, "epsLumo": 1.43, "ksGap": 0.041, "deltaScf": 0.0436,
                     "E1": 1126.84, "lowestParticleHole": 6.6e-12, "maxLambdaSOverM": 1.37},
                    # a refinement record that carries the parameters of its own ground state
                    {"label": "m1_L3_N1016_lamm2_T0_g601", "N": 1016.0, "lambdaHat": -0.0015,
                     "parameters": {"m": 1.0, "L": 3.0, "N": 1016.0, "T": 0.0, "lambdaHat": -0.0015,
                                    "gridPoints": 601, "occupationSmearing": 0.001,
                                    "zeroTemperatureFallbackStage": 1},
                     "exactZeroTemperatureOccupations": False, "E0": 1126.8, "mu": 1.39, "epsHomo": 1.389,
                     "epsLumo": 1.43, "ksGap": 0.041, "deltaScf": 0.04362, "E1": 1126.84,
                     "lowestParticleHole": 1.7e-12, "maxLambdaSOverM": 1.37}]
    summaries = {
        "spectrum": dict(common, experiment="spectrum", checks={"s1": True},
                         files=["reduction.json", "summary.json"],
                         exchangeTable={"status": "present", "sha256": table_sha}),
        "scf": dict(common, experiment="scf", checks={"m1_L3_N8_lam0_T0_converged": True, "grid_refinement_energy": True},
                    files=["summary.json"], runs=[scf_run, scf_l2, smeared]),
        "excited": dict(common, experiment="excited", checks={"m1_L3_N8_lam0_T0_gap_positive": True},
                        files=["summary.json"], runs=excited_runs),
        "thermo": dict(common, experiment="thermo", checks={"t1": True}, files=["summary.json"], runs=[],
                       series=[{"N": 8.0, "lambdaHat1": 0.01, "lambdaHatHot": 2.4e-5}], skippedRuns=[]),
        "emt": dict(common, experiment="emt", checks={"e1": True}, files=["summary.json"], runs=[scf_run],
                    requiredSource="rho_req = -21 H^2/kappa", positiveRhoExpectation={"holds": [], "fails": []}),
    }
    for sub, summary in summaries.items():
        write_json(os.path.join(root, "rust", sub, "summary.json"), summary)
    write_json(os.path.join(root, "rust", "spectrum", "theory-agreement.json"),
               {"path": "x", "status": "compared", "sha256": theory_sha,
                "checks": {"theory_zero_mode_splitting": {"passed": True, "detail": "c = 1.9"}}})
    for label in ("m1_L3_N8_lam0_T0", "m1_L3_N1016_lamm2_T0", "m1_L3_N1016_lamm2_T0_g601"):
        write_text(os.path.join(root, "rust", "excited", label, "particle-hole.csv"),
                   "excitation,eps_hole,eps_particle,k_hole,k_particle\n"
                   "6.58073595616315288e-12,1.38946077952050628e+00,1.38946077952708702e+00,0.0e+00,0.0e+00\n"
                   "3.69079856789222838e-03,1.38576998095261406e+00,1.38946077952050628e+00,9.35e-01,0.0e+00\n")
        write_text(os.path.join(root, "rust", "excited", label, "levels.csv"),
                   LEVELS_HEADER + level_row(14.0, 0.935, 192.0, 1.3857, 0.978) + level_row(0.0, 0.0, 4.0, 1.3894, 0.5266)
                   + level_row(30.0, 1.4, 192.0, 1.8, 1e-185) + level_row(1.0, 0.25, 824.0, 0.9, 1.0)
                   + level_row(1.0, 0.25, 824.0, -0.9, 1.0, branch=-1.0))
    write_json(os.path.join(root, "rust", "determinism-report.json"),
               {"schemaVersion": 1, "producer": "compare_runs",
                "checks": {"repeat_byte_identity": True, "refined_convergence": True},
                "measurements": {"repeatFilesCompared": 5, "refinedMaxAbsEps": 2.8e-8},
                "sourceSha256": {sub + "/summary.json": sha_file(os.path.join(root, "rust", sub, "summary.json"))
                                 for sub in SUBCOMMANDS}})
    write_json(os.path.join(root, "reference", "reference-summary.json"),
               {"schemaVersion": 1, "producer": "reference", "fixtureSha256": fixture, "quick": False, "complete": True,
                "selfTests": {"analyticMaxError": 3.6e-8}, "runs": [{"label": "m1_L3_N8_lam0_T0", "converged": True}],
                "couplings": [], "closedShells": {"N_mid": 112.0}})
    checks = {"reference_fixture_hash": True, "canonical_E0": True, "rust_repeat_byte_identity": True,
              "rust_refined_convergence": True}
    sources = {"referenceSummary": sha_file(os.path.join(root, "reference", "reference-summary.json")),
               "theoryJson": theory_sha, "referenceSolver": sha_repo("scripts/ks_reference_solver.py"),
               "checker": sha_repo("scripts/check_dirac16complex_kohn_sham.py")}
    for sub in SUBCOMMANDS:
        sources["rust_" + sub] = sha_file(os.path.join(root, "rust", sub, "summary.json"))
    write_json(os.path.join(root, "python-check-report.json"),
               {"schemaVersion": 2, "producer": "checker", "checks": checks, "checkCount": len(checks),
                "failedCheckCount": 0, "measurements": {"canonicalWorstRatio_E0": 0.03, "canonical_E0_detail": "E0"},
                "comparisons": {"canonical_scf_m1_L3_N8_lam0_T0": {
                    "status": "ran", "detail": {"referenceLabel": "m1_L3_N8_lam0_T0",
                                                "E0": {"rust": 0.0, "reference": 1e-9, "deviation": 1e-9,
                                                       "tolerance": 8e-6}}},
                    "stationarity": {"status": "not run", "detail": "--no-stationarity"}},
                "sourceSha256": sources, "comparisonsNotRun": ["stationarity"]})
    return root


def run_builder(root, output, *extra):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = builder.main(["--root", root, "--output", output, *extra])
    return code, buffer.getvalue()


def run_audit(*arguments):
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = audit.main(list(arguments))
    return code, buffer.getvalue()


class SummaryBuilderTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.mkdtemp(prefix="d16c_ks_summary_")
        self.root = make_root(os.path.join(self.temp, "root"))
        self.output = os.path.join(self.temp, "out", "kohn-sham-summary.json")

    def tearDown(self):
        shutil.rmtree(self.temp, ignore_errors=True)

    def build(self, *extra, output=None):
        return run_builder(self.root, output or self.output, *extra)

    def test_success_copies_numbers_and_is_deterministic(self):
        code, text = self.build()
        self.assertEqual(code, 0, text)
        self.assertTrue(text.rstrip().endswith("SUCCESS"))
        with open(self.output, "rb") as handle:
            first = handle.read()
        self.assertNotIn(b"\r", first)
        document = json.loads(first)
        self.assertEqual(document["verdict"], "SUCCESS")
        rows = {row["label"]: row for row in document["physics"]["groundAndExcited"]}
        self.assertEqual(rows["m1_L3_N8_lam0_T0"]["ksGap"], 0.4307336786379114)      # copied, not recomputed
        self.assertEqual(rows["m1_L3_N1016_lamm2_T0"]["occupationSmearing"], 0.001)
        self.assertEqual(rows["m1_L3_N1016_lamm2_T0"]["occupationSource"], "scf run of the same label")
        self.assertEqual(rows["m1_L3_N8_lam0_T0"]["particleHoleFirst"][0]["excitation"], 6.580735956163153e-12)
        self.assertEqual(rows["m1_L3_N1016_lamm2_T0"]["zeroTemperatureFallbackStage"], 1)
        refinement = document["physics"]["excitedRefinements"][0]
        self.assertEqual(refinement["label"], "m1_L3_N1016_lamm2_T0_g601")
        self.assertEqual(refinement["occupationSource"], "excited record")
        self.assertEqual((refinement["gridPoints"], refinement["zeroTemperatureFallbackStage"]), (601, 1))
        smeared = document["physics"]["smearedGroundStates"]["runs"]
        self.assertEqual([run["label"] for run in smeared], ["m1_L3_N1016_lamm2_T0", "m1_L3_N1016_lamm2_T0_g601"])
        # the floor selects the two fractional levels, not the Fermi-Dirac tail (1e-185) nor f = 1
        self.assertEqual([level["f"] for level in smeared[0]["fractionallyOccupiedLevels"]], [0.978, 0.5266])
        # counted, not computed: 824 fully occupied particle states + the 192-fold band = N = 1016
        # (the Dirac-sea row of the same |eps| is not counted); the k = 0 level lies above
        self.assertEqual([level["statesAtOrBelow"] for level in smeared[0]["fractionallyOccupiedLevels"]],
                         [1016.0, 1020.0])
        self.assertEqual((smeared[0]["aufbauCountClosesAt"]["eps"], smeared[0]["aufbauCountClosesAt"]["multiplicity"]),
                         (1.3857, 192.0))
        self.assertEqual(smeared[1]["zeroTemperatureFallbackStage"], 1)
        self.assertEqual(document["physics"]["lConvergence"][0]["N"], 8.0)
        self.assertEqual([entry["L"] for entry in document["physics"]["lConvergence"][0]["byL"]], [2.0, 3.0])
        self.assertEqual(document["totals"]["byProducer"]["wolfram"], {"checks": 2, "failed": 0})
        self.assertEqual(document["producers"]["notebook"]["status"], "absent")
        self.assertEqual(document["rustVersusReference"]["runs"][0]["E0"]["deviation"], 1e-9)
        read = {entry["path"] for entry in document["inputs"]}
        self.assertIn("artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lam0_T0/particle-hole.csv", read)
        self.assertIn("artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0/levels.csv", read)
        self.assertIn(FIXTURE, read)
        # byte identity on repetition and for another root location
        other_root = os.path.join(self.temp, "elsewhere", "kohn-sham")
        shutil.copytree(self.root, other_root)
        second = os.path.join(self.temp, "out2.json")
        self.assertEqual(run_builder(other_root, second)[0], 0)
        with open(second, "rb") as handle:
            self.assertEqual(handle.read(), first)
        self.assertNotIn(self.temp.replace("\\", "/").encode(), first)
        self.assertNotIn(self.temp.encode(), first)

    def test_missing_input_is_refused_and_nothing_written(self):
        os.remove(os.path.join(self.root, "rust", "determinism-report.json"))
        code, text = self.build()
        self.assertEqual(code, 1)
        self.assertIn("missing input", text)
        self.assertFalse(os.path.exists(self.output))

    def test_inconsistent_fixture_hash_is_refused_even_with_allow_incomplete(self):
        path = os.path.join(self.root, "rust", "thermo", "summary.json")
        with open(path, encoding="utf-8") as handle:
            summary = json.load(handle)
        summary["fixture"]["sha256"] = "0" * 64
        write_json(path, summary)
        code, text = self.build("--allow-incomplete")
        self.assertEqual(code, 1)
        self.assertIn("fixture_rust_thermo", text)
        self.assertFalse(os.path.exists(self.output))

    def test_refined_summary_is_refused(self):
        path = os.path.join(self.root, "rust", "scf", "summary.json")
        with open(path, encoding="utf-8") as handle:
            summary = json.load(handle)
        summary["refined"] = True
        write_json(path, summary)
        code, text = self.build()
        self.assertEqual(code, 1)
        self.assertIn("--refined", text)

    def test_stale_report_is_refused_or_marked_incomplete(self):
        path = os.path.join(self.root, "rust", "emt", "summary.json")
        with open(path, encoding="utf-8") as handle:
            summary = json.load(handle)
        summary["solverTotals"]["steps"] = 11          # the determinism and checker reports are now stale
        write_json(path, summary)
        code, text = self.build()
        self.assertEqual(code, 1)
        self.assertIn("determinism_report_emt", text)
        self.assertFalse(os.path.exists(self.output))
        code, text = self.build("--allow-incomplete")
        self.assertEqual(code, 3, text)
        with open(self.output, encoding="utf-8") as handle:
            document = json.load(handle)
        self.assertEqual(document["verdict"], "INCOMPLETE")
        self.assertTrue(any("cross_check_source_rust_emt" in item for item in document["incompleteInputs"]))

    def test_missing_self_tests_and_repeat_checks_are_incomplete(self):
        path = os.path.join(self.root, "reference", "reference-summary.json")
        with open(path, encoding="utf-8") as handle:
            summary = json.load(handle)
        del summary["selfTests"]
        write_json(path, summary)
        code, text = self.build()
        self.assertEqual(code, 1)
        self.assertIn("reference_self_tests_present", text)

    def test_failed_producer_check_gives_failure_but_is_written(self):
        path = os.path.join(self.root, "wolfram-kohn-sham-report.json")
        with open(path, encoding="utf-8") as handle:
            report = json.load(handle)
        report["checks"]["b"] = False
        write_json(path, report)
        # the theory JSON and the checker record the same sources: still consistent
        code, text = self.build()
        self.assertEqual(code, 1)
        with open(self.output, encoding="utf-8") as handle:
            document = json.load(handle)
        self.assertEqual(document["verdict"], "FAILURE")
        self.assertEqual(document["producers"]["wolfram"]["failed"], ["b"])

    def test_optional_notebook_report_is_counted(self):
        write_json(os.path.join(self.root, "notebook-report.json"),
                   {"producer": "nb", "verdict": "SUCCESS", "gauntlet": {"count": 7, "passed": 7, "failed": 0},
                    "figures": [1, 2]})
        code, text = self.build()
        self.assertEqual(code, 0, text)
        with open(self.output, encoding="utf-8") as handle:
            document = json.load(handle)
        self.assertEqual(document["producers"]["notebook"]["checkCount"], 7)
        self.assertEqual(document["totals"]["byProducer"]["notebook"], {"checks": 7, "failed": 0})

    def test_nan_sources_become_null(self):
        self.assertIsNone(builder.clean(float("nan")))
        self.assertEqual(builder.clean({"a": [1.0, float("inf")]}), {"a": [1.0, None]})
        self.assertEqual(builder.parse_label("m1_L3_N112_lamp1rescaled_T0_dk0p15")["lambdaName"], "lamp1rescaled")
        self.assertEqual(builder.parse_label("m1_L3_N8_lamh_T0p3")["T"], 0.3)
        self.assertEqual(builder.parse_label("m1_L3_N1016_lamm2_T0_g601")["suffix"], "g601")


class AuditTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.mkdtemp(prefix="d16c_ks_audit_")
        self.cwd = os.getcwd()
        os.chdir(self.temp)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp, ignore_errors=True)

    def test_same_bytes_values_and_negative_controls(self):
        write_json("a/x.json", {"v": 1.0, "s": "t"})
        write_json("b/x.json", {"v": 1.0, "s": "t"})
        self.assertEqual(run_audit("same", "--pair", "a/x.json", "b/x.json")[0], 0)
        write_json("b/x.json", {"v": 1.0 + 1e-12, "s": "t"})
        self.assertEqual(run_audit("same", "--pair", "a/x.json", "b/x.json")[0], 1)
        code, text = run_audit("same", "--rtol", "1e-9", "--atol", "1e-12", "--pair", "a/x.json", "b/x.json")
        self.assertEqual(code, 0, text)
        self.assertIn("value by value", text)
        write_json("b/x.json", {"v": 1.0 + 1e-6, "s": "t"})
        self.assertEqual(run_audit("same", "--rtol", "1e-9", "--pair", "a/x.json", "b/x.json")[0], 1)
        write_json("b/x.json", {"v": 1.0, "s": "u"})
        self.assertEqual(run_audit("same", "--rtol", "1e-9", "--pair", "a/x.json", "b/x.json")[0], 1)
        write_text("a/y.rs", "x\n")
        write_text("b/y.rs", "y\n")
        self.assertEqual(run_audit("same", "--rtol", "1e-9", "--pair", "a/y.rs", "b/y.rs")[0], 1)

    def make_tree(self, root):
        for sub in SUBCOMMANDS:
            write_text(os.path.join(root, sub, "run1", "levels.csv"), "eps\n1.0\n")
            write_json(os.path.join(root, sub, "summary.json"), {"files": ["run1/levels.csv", "summary.json"]})

    def test_rust_outputs(self):
        self.make_tree("committed")
        self.make_tree("run")
        code, text = run_audit("rust-outputs", "--committed", "committed", "--run", "run")
        self.assertEqual(code, 0, text)
        write_text("run/scf/run1/levels.csv", "eps\n1.0000001\n")
        code, text = run_audit("rust-outputs", "--committed", "committed", "--run", "run")
        self.assertEqual(code, 1)
        self.assertIn("scf: 1 file(s) differ", text)
        self.make_tree("run")
        write_text("run/emt/stray.csv", "x\n")
        self.assertEqual(run_audit("rust-outputs", "--committed", "committed", "--run", "run")[0], 1)
        os.remove("run/emt/stray.csv")
        write_text("committed/thermo/unlisted.csv", "x\n")
        self.assertEqual(run_audit("rust-outputs", "--committed", "committed", "--run", "run")[0], 1)

    FAKE_SUBCOMMAND = (
        "import os, sys, time\n"
        "args = sys.argv[1:]\n"
        "out = args[args.index('--output') + 1]\n"
        "name = os.path.basename(sys.argv[0])\n"
        "os.makedirs(os.path.join(out, name), exist_ok=True)\n"
        "time.sleep(float(os.environ.get('FAKE_SLEEP_' + name, '0.2')))\n"
        "with open(os.path.join(out, name, 'mode.txt'), 'w') as handle:\n"
        "    handle.write('refined' if '--refined' in args else 'canonical')\n"
        "code = int(os.environ.get('FAKE_EXIT_' + name, '0'))\n"
        "print('SUCCESS' if code == 0 else 'FAILURE')\n"
        "sys.exit(code)\n")

    def test_rust_run_concurrent_sequential_and_failures(self):
        # the "binary" is this Python; the subcommand names are small scripts in the
        # working directory, so "<python> scf [--refined] --output DIR" runs the scf stand-in
        for sub in SUBCOMMANDS:
            write_text(sub, self.FAKE_SUBCOMMAND)
        jobs = []
        for sub in SUBCOMMANDS:
            jobs += ["--job", sub, "run-a", "canonical"]
        jobs += ["--job", "scf", "refined", "refined"]
        code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/r", *jobs)
        self.assertEqual(code, 0, text)
        self.assertIn("concurrent (6 processes)", text)
        self.assertEqual(text.count("exit=0 last=SUCCESS"), 6)
        with open(os.path.join("refined", "scf", "mode.txt"), encoding="utf-8") as handle:
            self.assertEqual(handle.read(), "refined")
        with open(os.path.join("run-a", "thermo", "mode.txt"), encoding="utf-8") as handle:
            self.assertEqual(handle.read(), "canonical")
        self.assertTrue(os.path.isfile(os.path.join("logs", "r-refined-scf.log")))
        code, text = run_audit("rust-run", "--sequential", "--binary", sys.executable, "--log-prefix", "logs/s", *jobs)
        self.assertEqual(code, 0, text)
        self.assertIn("stage4_rust_run_mode=sequential", text)
        # a failing job: its exit code and last line are reported, the others are stopped
        os.environ["FAKE_EXIT_scf"] = "1"
        os.environ["FAKE_SLEEP_thermo"] = "60"
        try:
            started = time.monotonic()
            code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/f",
                                   "--job", "scf", "run-a", "canonical", "--job", "thermo", "run-a", "canonical")
            self.assertLess(time.monotonic() - started, 50.0)
            self.assertEqual(code, 1)
            self.assertIn("canonical scf exited 1 with last line 'FAILURE'", text)
            self.assertIn("canonical thermo STOPPED", text)
            code, text = run_audit("rust-run", "--sequential", "--binary", sys.executable, "--log-prefix", "logs/g",
                                   "--job", "scf", "run-a", "canonical", "--job", "emt", "run-a", "canonical")
            self.assertEqual(code, 1)
            self.assertIn("canonical emt NOT STARTED", text)
        finally:
            del os.environ["FAKE_EXIT_scf"]
            del os.environ["FAKE_SLEEP_thermo"]
        # a job whose last line is not SUCCESS fails even with exit code 0
        write_text("emt", "print('SUCCESS')\nprint('trailing output')\n")
        code, text = run_audit("rust-run", "--binary", sys.executable, "--log-prefix", "logs/h",
                               "--job", "emt", "run-a", "canonical")
        self.assertEqual(code, 1, text)
        self.assertEqual(run_audit("rust-run", "--binary", "missing.exe", "--log-prefix", "logs/m",
                                   "--job", "emt", "run-a", "canonical")[0], 1)

    def test_snapshot_unchanged_fresh(self):
        write_text("tree/a.txt", "a\n")
        write_json("tree/b.json", {"engine": {"binary": "x"}, "v": 1})
        self.assertEqual(run_audit("snapshot", "--into", "snap", "tree")[0], 0)
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "tree")[0], 0)
        write_json("tree/b.json", {"engine": {"binary": "y"}, "v": 1})
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "tree")[0], 1)
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "--ignore-json-key", "engine.binary", "tree")[0], 0)
        write_text("tree/c.txt", "new\n")
        self.assertEqual(run_audit("unchanged", "--snapshot", "snap", "--ignore-json-key", "engine.binary", "tree")[0], 1)
        since = int(time.time()) - 5
        self.assertEqual(run_audit("fresh", "--since", str(since), "tree/c.txt")[0], 0)
        self.assertEqual(run_audit("fresh", "--since", str(since + 3600), "tree/c.txt")[0], 1)
        self.assertEqual(run_audit("fresh", "--since", str(since), "tree/missing.txt")[0], 1)

    def test_determinism(self):
        report = {"checks": {"canonical_summaries_present": True, "repeat_byte_identity": True,
                             "refined_convergence": True},
                  "measurements": {"repeatFilesCompared": 327, "refinedRunsCompared": 65}}
        write_json("committed.json", report)
        partial = copy.deepcopy(report)
        partial["measurements"]["refinedRunsCompared"] = 43
        write_json("fresh.json", partial)
        self.assertEqual(run_audit("determinism", "--committed", "committed.json", "--fresh", "fresh.json")[0], 0)
        self.assertEqual(run_audit("determinism", "--committed", "committed.json", "--fresh", "fresh.json",
                                   "--full-refined")[0], 1)
        partial["checks"]["refined_convergence"] = False
        write_json("fresh.json", partial)
        self.assertEqual(run_audit("determinism", "--committed", "committed.json", "--fresh", "fresh.json")[0], 1)

    def test_reference_quick(self):
        summary = {"quick": True, "complete": True, "selfTests": {"analyticMaxError": 2e-7},
                   "runs": [{"label": "a", "converged": True}]}
        write_json("ref/reference-summary.json", summary)
        self.assertEqual(run_audit("reference-quick", "--summary", "ref/reference-summary.json")[0], 0)
        del summary["selfTests"]
        write_json("ref/reference-summary.json", summary)
        self.assertEqual(run_audit("reference-quick", "--summary", "ref/reference-summary.json")[0], 1)

    def test_checker_report(self):
        checks = {"a": True, "rust_repeat_byte_identity": True, "rust_refined_convergence": True}
        committed = {"checks": checks, "checkCount": 3, "failedCheckCount": 0, "comparisonsNotRun": []}
        write_json("committed.json", committed)
        write_json("fresh.json", committed)
        self.assertEqual(run_audit("checker-report", "--committed", "committed.json", "--fresh", "fresh.json")[0], 0)
        fresh = copy.deepcopy(committed)
        del fresh["checks"]["rust_refined_convergence"]
        fresh["checkCount"] = 2
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("checker-report", "--committed", "committed.json", "--fresh", "fresh.json")[0], 1)
        fresh = copy.deepcopy(committed)
        fresh["checks"]["a"] = False
        fresh["failedCheckCount"] = 1
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("checker-report", "--committed", "committed.json", "--fresh", "fresh.json")[0], 1)

    def test_prepare_notebook_and_notebook_report(self):
        notebook = {"cells": [{"cell_type": "code", "outputs": [1], "execution_count": 3, "source": ""}],
                    "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
        write_json("nb.ipynb", notebook)
        self.assertEqual(run_audit("prepare-notebook", "--source", "nb.ipynb", "--dest", "out/nb.ipynb")[0], 0)
        with open("out/nb.ipynb", encoding="utf-8") as handle:
            cleared = json.load(handle)
        self.assertEqual(cleared["cells"][0]["outputs"], [])
        self.assertIsNone(cleared["cells"][0]["execution_count"])
        report = {"notebook": "notebooks/x.ipynb", "executions": [{"notebook": "a"}], "verdict": "SUCCESS",
                  "gauntlet": {"count": 2, "passed": 2}}
        write_json("committed.json", report)
        fresh = dict(report, notebook="build/stage4/notebook/x.ipynb")
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("notebook", "--committed-report", "committed.json", "--fresh-report",
                                   "fresh.json")[0], 0)
        fresh["gauntlet"] = {"count": 2, "passed": 1}
        write_json("fresh.json", fresh)
        self.assertEqual(run_audit("notebook", "--committed-report", "committed.json", "--fresh-report",
                                   "fresh.json")[0], 1)


def find_executable(*names):
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


class GateTwinTests(unittest.TestCase):

    def test_both_twins_are_lf_only_and_end_alike(self):
        for path in (GATE_PS1, GATE_SH, AUDIT_PATH, BUILDER_PATH):
            with open(path, "rb") as handle:
                data = handle.read()
            self.assertNotIn(b"\r", data, path)
            self.assertTrue(data.endswith(b"\n"), path)
        for path in (GATE_PS1, GATE_SH):
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            for needle in ("stage4_kohn_sham_verification=OK", "stage4_kohn_sham_verification=FAILED",
                           "stage4_kohn_sham_verification=PARTIAL", "stage4_kohn_sham_verification=DRY-RUN",
                           "scripts/verify_stage4_kohn_sham_audit.py", "run_logged"):
                self.assertIn(needle, text, "%s lacks %s" % (path, needle))

    @staticmethod
    def steps_of(output):
        names = []
        for line in output.splitlines():
            for prefix in ("stage4_dry_run_step=", "stage4_skipped_step=", "stage4_step_not_selected="):
                if line.startswith(prefix):
                    names.append(line[len(prefix):].split(" ")[0])
        return names

    @staticmethod
    def expected_of(output):
        """(step, expected wall time) of every dry-run line."""
        pairs = []
        for line in output.splitlines():
            if line.startswith("stage4_dry_run_step="):
                name, _, rest = line[len("stage4_dry_run_step="):].partition(" expected=[")
                pairs.append((name, rest[:-1] if rest.endswith("]") else rest))
        return pairs

    def run_twin(self, command):
        completed = subprocess.run(command, cwd=REPO, capture_output=True, text=True, encoding="utf-8",
                                   errors="replace", timeout=300)
        return completed.returncode, completed.stdout + completed.stderr

    def test_dry_runs_list_the_same_steps(self):
        bash = find_executable("bash")
        pwsh = find_executable("pwsh")
        if not bash or not pwsh:
            self.skipTest("bash and pwsh are both needed to compare the twins")
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun"])
        if "stage4_failed_step=tools" in out_sh + out_ps:
            self.skipTest("a required tool is missing on this machine")
        self.assertEqual(code_sh, 0, out_sh[-2000:])
        self.assertEqual(code_ps, 0, out_ps[-2000:])
        steps_sh, steps_ps = self.steps_of(out_sh), self.steps_of(out_ps)
        self.assertEqual(steps_sh, steps_ps)
        self.assertEqual(len(steps_sh), 37)
        self.assertEqual([name[7:9] for name in steps_sh], ["%02d" % n for n in range(37)])
        self.assertIn("stage4-14-rust-runs", steps_sh)
        # the same expected wall time for every step, and no unfilled placeholder
        self.assertEqual(self.expected_of(out_sh), self.expected_of(out_ps))
        self.assertNotIn("@@", out_sh + out_ps)
        self.assertTrue(out_sh.rstrip().endswith("stage4_kohn_sham_verification=DRY-RUN"))
        self.assertTrue(out_ps.rstrip().endswith("stage4_kohn_sham_verification=DRY-RUN"))
        # step 14 launches all Rust processes concurrently unless asked otherwise
        for output in (out_sh, out_ps):
            command = [line for line in output.splitlines() if "rust-run --binary" in line][0]
            self.assertEqual(command.count("--job"), 9)
            self.assertNotIn("--sequential", command)
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run", "--sequential-rust", "--refined-thermo",
                                         "--steps", "14"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun", "-SequentialRust",
                                         "-RefinedThermo", "-Steps", "14"])
        for output in (out_sh, out_ps):
            command = [line for line in output.splitlines() if "rust-run --binary" in line][0]
            self.assertEqual(command.count("--job"), 10)
            self.assertIn("--sequential", command)
        self.assertEqual(self.expected_of(out_sh), self.expected_of(out_ps))
        # step selection: only 05 and 13 are listed as steps to run
        code_sh, out_sh = self.run_twin([bash, GATE_SH, "--dry-run", "--steps", "05,stage4-13-print-config"])
        code_ps, out_ps = self.run_twin([pwsh, "-NoProfile", "-File", GATE_PS1, "-DryRun", "-Steps",
                                         "05,stage4-13-print-config"])
        for output in (out_sh, out_ps):
            selected = [line.split("=")[1].split(" ")[0] for line in output.splitlines()
                        if line.startswith("stage4_dry_run_step=")]
            self.assertEqual(selected, ["stage4-05-theory-same", "stage4-13-print-config"])

