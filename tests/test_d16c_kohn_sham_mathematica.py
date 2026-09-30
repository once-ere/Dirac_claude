"""Tests of the Stage-4 Mathematica cross-check (notebooks/Dirac16ComplexKohnSham.nb).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_mathematica.py" -v

What is tested (standard library only; wolframscript is used only by the rebuild test,
which is skipped when it is not on PATH):
  * artifacts/dirac16complex/kohn-sham/mathematica-report.json is the report of a
    passing run: the repository checker schema {schemaVersion, producer, checks,
    measurements, sourceSha256}, every check true, checkCount equal to the verifier's
    expected count, verdict SUCCESS, deterministic formatting (LF, trailing newline,
    no absolute paths);
  * the report is current: every input it records (packages, Rust outputs,
    generated.rs, fixture) still has the recorded SHA-256, the fixture hash is the
    fixture's, and the notebook has the verifier's expected number of Input cells and
    is byte-identical to a fresh build of the builder;
  * the figures listed in the report are exactly the PNG files under
    figures/mathematica/, valid PNGs without the "Creation Time" text chunk;
  * the reported agreement numbers are re-read against the committed Rust files in
    Python (level counts, lambda_hat_2, E_0, eps_HOMO, KS gap, closed-shell tables)
    and are inside the tolerances the notebook states.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
KS = REPO / "artifacts" / "dirac16complex" / "kohn-sham"
REPORT = KS / "mathematica-report.json"
FIGURES = KS / "figures" / "mathematica"
NOTEBOOK = REPO / "notebooks" / "Dirac16ComplexKohnSham.nb"
BUILDER = REPO / "scripts" / "build_dirac16complex_ks_mathematica_notebook.wls"
VERIFIER = REPO / "scripts" / "verify_dirac16complex_ks_mathematica_notebook.wls"
FIXTURE = REPO / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"
RUST = KS / "rust"
SCF_RUN = RUST / "scf" / "m1_L3_N8_lamp2_T0" / "run.json"
FREE_FILES = ["free-spectrum-m%d-L%d.csv" % (m, l) for m in (1, 3) for l in (2, 3, 4)]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def verifier_expected(name):
    match = re.search(name + r"\s*=\s*(\d+)", VERIFIER.read_text(encoding="utf-8"))
    return int(match.group(1))


def csv_rows(path):
    lines = Path(path).read_text(encoding="utf-8").strip().split("\n")
    header = lines[0].split(",")
    return [dict(zip(header, (float(v) for v in line.split(",")))) for line in lines[1:]]


class ReportSchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = REPORT.read_text(encoding="utf-8")
        cls.report = json.loads(cls.text)

    def test_checker_schema(self):
        for key in ("schemaVersion", "producer", "checks", "measurements", "sourceSha256"):
            self.assertIn(key, self.report)
        self.assertEqual(self.report["schemaVersion"], 1)
        self.assertIn("notebooks/Dirac16ComplexKohnSham.nb", self.report["producer"])
        self.assertTrue(all(isinstance(v, bool) for v in self.report["checks"].values()))
        self.assertTrue(all(isinstance(v, (int, float)) and not isinstance(v, bool)
                            for v in self.report["measurements"].values()))

    def test_all_checks_pass(self):
        checks = self.report["checks"]
        failed = [name for name, value in checks.items() if value is not True]
        self.assertEqual(failed, [])
        self.assertEqual(self.report["failedChecks"], [])
        self.assertEqual(self.report["verdict"], "SUCCESS")
        self.assertEqual(self.report["checkCount"], len(checks))

    def test_check_count_is_the_verifier_expectation(self):
        self.assertEqual(self.report["checkCount"], verifier_expected("expectedCheckCount"))

    def test_deterministic_format(self):
        self.assertTrue(self.text.endswith("\n"))
        self.assertNotIn("\r", self.text)
        self.assertNotIn("\\/", self.text)
        self.assertIsNone(re.search(r"[A-Za-z]:[\\/]|/Users/|/home/", self.text))
        for forbidden in ("elapsed", "Timing", "seconds"):
            self.assertNotIn(forbidden, self.text)

    def test_engine_block(self):
        engine = self.report["engine"]
        self.assertEqual(engine["command"], "print-config")
        self.assertEqual(engine["exitCode"], 0)
        self.assertEqual(engine["lastLine"], "SUCCESS")
        self.assertTrue(engine["binary"].startswith("studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham"))
        self.assertTrue(all(engine["checks"].values()))


class ReportIsCurrent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = load_json(REPORT)

    def test_recorded_inputs_are_unchanged(self):
        sources = self.report["sourceSha256"]
        self.assertGreaterEqual(len(sources), 15)
        for relative, digest in sources.items():
            path = REPO / relative
            self.assertTrue(path.is_file(), relative)
            self.assertEqual(sha256(path), digest, "input changed since the notebook was evaluated: " + relative)
        for required in ("wolfram/Dirac16ComplexKohnSham.wl", "wolfram/Dirac16ComplexGeometry.wl",
                         "artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/run.json",
                         "artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/profiles.csv",
                         "artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/levels.csv",
                         "studies/dirac16complex_kohn_sham/src/generated.rs"):
            self.assertIn(required, sources)
        for name in FREE_FILES:
            self.assertIn("artifacts/dirac16complex/kohn-sham/rust/spectrum/" + name, sources)

    def test_fixture_hash(self):
        self.assertEqual(self.report["fixtureSha256"], sha256(FIXTURE))

    def test_notebook_input_cell_count(self):
        text = NOTEBOOK.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r',\s*"Input"\]', text)), verifier_expected("expectedInputCount"))
        self.assertNotIn("\r", text)
        self.assertIsNone(re.search(r"[ \t]\n", text))

    @unittest.skipIf(shutil.which("wolframscript") is None, "wolframscript not on PATH")
    def test_notebook_is_a_fresh_build(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fresh.nb"
            result = subprocess.run(["wolframscript", "-file", str(BUILDER), str(target)],
                                    cwd=REPO, capture_output=True, text=True, timeout=600)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(target.read_bytes(), NOTEBOOK.read_bytes())


class Figures(unittest.TestCase):
    def test_listed_figures_are_the_directory(self):
        report = load_json(REPORT)
        listed = set(report["figures"])
        on_disk = {"artifacts/dirac16complex/kohn-sham/figures/mathematica/" + p.name for p in FIGURES.glob("*.png")}
        self.assertEqual(listed, on_disk)
        self.assertEqual(len(listed), 6)

    def test_png_without_creation_time(self):
        for path in FIGURES.glob("*.png"):
            data = path.read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n", path.name)
            position = 8
            while position < len(data):
                length = int.from_bytes(data[position:position + 4], "big")
                kind = data[position + 4:position + 8]
                if kind == b"tEXt":
                    self.assertFalse(data[position + 8:position + 8 + length].startswith(b"Creation Time"), path.name)
                position += 12 + length
            self.assertEqual(position, len(data), path.name)


class AgreementAgainstRustFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = load_json(REPORT)
        cls.m = cls.report["measurements"]
        cls.run = load_json(SCF_RUN)
        cls.spectrum = load_json(RUST / "spectrum" / "summary.json")

    def test_level_counts(self):
        total = sum(len(csv_rows(RUST / "spectrum" / name)) for name in FREE_FILES)
        self.assertEqual(self.m["freeSpectraLevelCount"], total)
        self.assertEqual(self.m["scfSpectrumLevelCount"], self.run["states"])
        self.assertEqual(self.m["scfSpectrumShells"], self.run["shellsUsed"])
        k0 = sum(1 for name in FREE_FILES for row in csv_rows(RUST / "spectrum" / name) if row["n2"] == 0)
        self.assertEqual(self.m["boxExactLevelCount"], k0)

    def test_parameter_set(self):
        coupling = [c for c in self.spectrum["reference"]["couplings"] if c["N"] == 8 and c["m"] == 1 and c["L"] == 3][0]
        self.assertEqual(self.m["scfLambdaHat"], coupling["lambdaHat2"])
        parameters = self.run["parameters"]
        self.assertEqual((parameters["N"], parameters["T"], parameters["L"], parameters["m"], parameters["H"]), (8, 0, 3, 1, 1))

    def test_scf_numbers_against_run_json(self):
        self.assertLessEqual(abs(self.m["scfEnergy"] - self.run["energy"]), 1e-9)
        self.assertLessEqual(abs(self.m["scfEpsHomo"] - self.run["epsHomo"]), 1e-9)
        self.assertLessEqual(abs(self.m["scfKsGap"] - self.run["ksGap"]), 1e-8)
        for name, tolerance in (("scfEnergyDeviation", 1e-9), ("scfEpsHomoDeviation", 1e-9), ("scfKsSumDeviation", 1e-9),
                                ("scfHartreeDeviation", 1e-9), ("scfExchangeDeviation", 1e-9), ("scfNcMaxDeviationOverD", 1e-9),
                                ("scfScMaxDeviationOverD", 1e-9), ("scfHomoProfileMaxDeviation", 1e-8),
                                ("scfSpectrumMaxAbsDeviation", 1e-8), ("scfKsGapDeviation", 1e-8), ("scfEpsFreeMaxAbsDeviation", 1e-8),
                                ("freeSpectraMaxAbsDeviation", 1e-8), ("boxExactVsRustMaxAbsDeviation", 1e-8),
                                ("boxNDSolveVsExactMaxAbsDeviation", 1e-10), ("closedShellsMaxAbsDeviation", 1e-8),
                                ("freeSpectraMaxScalarChargeDeviation", 1e-8), ("freeSpectraMaxMatchingResidual", 1e-8),
                                ("zeroModeSlopeMaxDeviation", 1e-6)):
            self.assertLessEqual(self.m[name], tolerance, name)
        self.assertLessEqual(self.m["scfMeffMaxAbsDeviation"], self.m["scfMeffTolerance"])
        self.assertLessEqual(self.m["scfVxMaxAbsDeviation"], self.m["scfVxTolerance"])
        self.assertLess(self.m["scfFinalResidual"], 1e-12)

    def test_closed_shell_tables(self):
        self.assertEqual(self.m["closedShellEntries_m1_L3"], len(self.spectrum["reference"]["closedShells_m1_L3_N_epsHomo"]))
        self.assertEqual(self.m["closedShellEntries_m3_L3"], len(self.spectrum["reference"]["closedShells_m3_L3_N_epsHomo"]))
        numbers = self.report["shooting"]["closedShellNumbers"]
        self.assertEqual((numbers["nMid"], numbers["nLarge"], numbers["nMidM3"]),
                         tuple(int(self.spectrum["reference"][k]) for k in ("nMid", "nLarge", "nMidM3")))

    def test_zero_mode_splitting_closed_form(self):
        # c = 2/(1 + e^{-3}) at m = H = 1, L = 3, a4 = 0 (exact package closed form)
        self.assertAlmostEqual(self.m["zeroModeSplittingC_m1_H1_L3"], 2.0 / (1.0 + 2.718281828459045 ** -3), places=13)

    def test_theory_package_count(self):
        wolfram = load_json(KS / "wolfram-kohn-sham-report.json")
        self.assertEqual(self.m["theoryPackageCheckCount"], len(wolfram["checks"]))


if __name__ == "__main__":
    unittest.main()
