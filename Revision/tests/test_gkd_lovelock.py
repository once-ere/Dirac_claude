#!/usr/bin/env python3
"""Tests for Revision/gkd_lovelock: the Lovelock tensors of (4.38) computed with GKD (Rust,
Revision/gkd_lovelock/code) and their two independent verifications in
Revision/gkd_lovelock/verification/ (the sympy checker check_lovelock_gkd.py and the Wolfram check
verify_lovelock_gkd.wls with the package LovelockGKDCheck.wl).

Run from the repository root:
    python -m unittest Revision/tests/test_gkd_lovelock.py -v
    (or: python -m unittest discover -s Revision/tests -p "test_gkd_lovelock.py" -v)

What is tested
  * fast unit tests of the sympy checker's pieces: the literal generalized delta kdelta
    (= Det[Outer[delta, lower, upper]]), the exact normal form ``canon``, the readers of the Rust
    output, and a negative control (a tampered component is detected);
  * the committed files in Revision/gkd_lovelock/results/ have the pinned sha256 digests below, and
    the Rust report, the GKD self-test, the sympy report and the Wolfram report all say SUCCESS
    with every check PASS (every check has a name, a verdict and a detail);
  * SLOW (skipped when REVISION_FAST=1): the Rust binary is built if needed and
    `lovelock --brute-force-k2` is run twice; both runs must be byte-identical to each other and to
    the committed files; the sympy checker is run twice: both reports byte-identical, all checks
    PASS, equal to the committed python-lovelock-report.json; the checker run on a copy of the Rust
    output with one tampered component must fail;
  * SLOW (skipped when REVISION_FAST=1 or wolframscript is missing, about 70 s): the Wolfram check is
    run once and must reproduce the committed wolfram-gkd-report.json byte for byte;
  * VERY SLOW (only when LOVELOCK_GKD_SELFTEST=1, several minutes): `gkd-selftest
    --exhaustive-max 4` is run twice and must reproduce the committed gkd-selftest.json.
Temporary files go to tempfile directories (under $REVISION_SCRATCH when that is set); the
committed files are never touched.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import sympy as sp

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
GKD_DIR = REVISION / "gkd_lovelock"
VERIFICATION = GKD_DIR / "verification"
sys.path.insert(0, str(VERIFICATION))
import check_lovelock_gkd as C  # noqa: E402

CRATE = GKD_DIR / "code"
ART = GKD_DIR / "results"
EXE = CRATE / "target" / "release" / ("lovelock_gkd.exe" if os.name == "nt" else "lovelock_gkd")
CHECKER = VERIFICATION / "check_lovelock_gkd.py"
WOLFRAM_SCRIPT = VERIFICATION / "verify_lovelock_gkd.wls"
FAST = os.environ.get("REVISION_FAST") == "1"
SELFTEST = os.environ.get("LOVELOCK_GKD_SELFTEST") == "1"
SCRATCH = os.environ.get("REVISION_SCRATCH") or None

# sha256 of the committed files.
PINNED = {
    "curvature.json": "d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e",
    "lovelock-tensors.json": "9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567",
    "lovelock-components.md": "65f95810d3b7b6696227670f03241c20758bcee4e408743803200cae68a1b8e7",
    "lovelock-report.json": "5c919ea827a5e6822a7196bb66ead64fa0a3e70f01f35b2bbfb99a65ae028bb8",
    "gkd-selftest.json": "6cd72bd8d5d8d2f7acb4825ed0a975a26aaad343e323b9c96f6d1fc4f294d1dc",
    "python-lovelock-report.json": "a4d6c0d5e2d063ce01611c06a98a4ba9cff0d61616b480b0b5828e2f3eee4d52",
    "wolfram-gkd-report.json": "71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189",
}
RUST_LOVELOCK_OUTPUTS = ["curvature.json", "lovelock-tensors.json", "lovelock-components.md", "lovelock-report.json"]
PY_CHECK_COUNT = 49
WOLFRAM_CHECK_COUNT = 29


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name):
    return json.loads((ART / name).read_text(encoding="utf-8"))


def build_rust():
    """cargo build --release (a no-op when up to date); returns the binary or None without cargo."""
    cargo = shutil.which("cargo")
    if cargo is None:
        return None
    subprocess.run([cargo, "build", "--release", "--manifest-path", str(CRATE / "Cargo.toml")],
                   check=True, cwd=ROOT, capture_output=True)
    return EXE if EXE.exists() else None


def start(cmd, env=None):
    return subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            env={**os.environ, "PYTHONIOENCODING": "utf-8", **(env or {})})


def finish(proc, timeout=1800):
    out, _ = proc.communicate(timeout=timeout)
    return proc.returncode, out.decode("utf-8", "replace")


def assert_checks_all_pass(test, report, count):
    test.assertEqual(report["verdict"], "SUCCESS")
    test.assertEqual(report["failedCheckCount"], 0)
    test.assertEqual(report["checkCount"], count)
    test.assertEqual(len(report["checks"]), count)
    names = [c["name"] for c in report["checks"]]
    test.assertEqual(len(names), len(set(names)))
    for c in report["checks"]:
        test.assertEqual(set(c), {"name", "verdict", "detail"}, c)
        test.assertEqual(c["verdict"], "PASS", c["name"])
        test.assertTrue(c["detail"])


class TestKdeltaLiteral(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(C.kdelta((1, 2), (1, 2)), 1)
        self.assertEqual(C.kdelta((1, 2), (2, 1)), -1)
        self.assertEqual(C.kdelta((3, 3), (3, 3)), 0)
        self.assertEqual(C.kdelta((0, 1, 2), (1, 2, 0)), 1)
        self.assertEqual(C.kdelta((0, 1, 2), (1, 0, 2)), -1)
        self.assertEqual(C.kdelta((0, 1, 2), (0, 1, 5)), 0)
        with self.assertRaises(ValueError):
            C.kdelta((0, 1), (0,))

    def test_equals_cofactor_determinant(self):
        for m in (1, 2, 3):
            for lower in itertools.product(range(4), repeat=m):
                for upper in itertools.product(range(4), repeat=m):
                    ref = C.cofactor_det([[1 if lo == up else 0 for up in upper] for lo in lower])
                    self.assertEqual(C.kdelta(lower, upper), ref, (lower, upper))

    def test_antisymmetry_and_pigeonhole(self):
        rng = random.Random(3)
        for _ in range(200):
            m = rng.randint(2, 7)
            lower = tuple(rng.sample(range(8), m))
            upper = list(rng.sample(lower, m))
            a, b = rng.sample(range(m), 2)
            swapped = upper[:]
            swapped[a], swapped[b] = swapped[b], swapped[a]
            self.assertEqual(C.kdelta(lower, tuple(upper)), -C.kdelta(lower, tuple(swapped)))
            self.assertIn(C.kdelta(lower, tuple(upper)), (1, -1))
        for _ in range(50):
            lower = tuple(rng.randrange(8) for _ in range(9))
            upper = tuple(rng.randrange(8) for _ in range(9))
            self.assertEqual(C.kdelta(lower, upper), 0)


class TestCanonAndReaders(unittest.TestCase):
    def test_canon_uses_the_trigonometric_relation(self):
        th = C.TH
        self.assertTrue(C.is_zero(sp.sin(th) ** 2 + sp.cos(th) ** 2 - 1))
        self.assertTrue(C.is_zero(sp.sin(th) * sp.cot(th) - sp.cos(th)))
        self.assertTrue(C.is_zero(sp.sin(th) ** 2 * (1 + sp.cot(th) ** 2) - 1))
        self.assertFalse(C.is_zero(sp.sin(th) ** C.THIRD))
        self.assertFalse(C.is_zero(sp.sin(th) ** 2 - sp.cos(th) ** 2))
        self.assertTrue(C.is_zero(sp.exp(2 * C.a4(C.x4)) * sp.exp(-2 * C.a4(C.x4)) - 1))
        self.assertEqual(C.canon(sp.sin(th) ** C.THIRD)[1], 1)

    def test_readers_agree(self):
        entry = load("lovelock-tensors.json")["A3_contravariant_l_h"]["x5,x5"]
        self.assertTrue(C.is_zero(C.from_mathematica(entry["mathematica"]) - C.from_monomials(entry["monomials"])))
        expr = C.from_mathematica("-(4)*Derivative[2][a4][x4]*E^(-2*a4[x4])*Sin[6*H*x8]^(2/3)*Cot[6*H*x8]")
        self.assertEqual(expr, -4 * C.DER[1] * sp.exp(-2 * C.a4(C.x4)) * sp.sin(C.TH) ** sp.Rational(2, 3) * sp.cot(C.TH))
        with self.assertRaises(ValueError):
            C.from_mathematica("Foo[x8]")

    def test_negative_control_is_detected(self):
        comp = C.Comparator(C.Points())
        good = C.from_monomials([[12, 1, [0, 2, 0, 0, 0, -2, 2, 1]], [-60, 1, [2, 0, 0, 0, 0, -2, 2, 1]]])
        same = sp.cos(C.TH) * sp.exp(-2 * C.a4(C.x4)) * sp.sin(C.TH) ** sp.Rational(-1, 3) * (12 * C.DER[0] ** 2 - 60 * C.H ** 2)
        self.assertTrue(comp.compare("same", same, good))
        bad = C.from_monomials([[12, 1, [0, 2, 0, 0, 0, -2, 1, 1]], [-60, 1, [2, 0, 0, 0, 0, -2, 2, 1]]])
        self.assertFalse(comp.compare("bad", same, bad))
        self.assertEqual(comp.detects(same, bad), (True, True, True))
        self.assertEqual(len(comp.failures), 1)


class TestCommittedOutputs(unittest.TestCase):
    def test_pinned_sha256(self):
        for name, digest in PINNED.items():
            self.assertEqual(sha256(ART / name), digest, name)

    def test_lf_line_endings(self):
        for name in ("python-lovelock-report.json", "wolfram-gkd-report.json"):
            data = (ART / name).read_bytes()
            self.assertNotIn(b"\r", data, name)
            self.assertTrue(data.endswith(b"\n"), name)

    def test_rust_reports_say_success(self):
        rust = load("lovelock-report.json")
        self.assertEqual(rust["verdict"], "SUCCESS")
        self.assertEqual(rust["failedCheckCount"], 0)
        self.assertTrue(all(c["passed"] for c in rust["checks"].values()))
        selftest = load("gkd-selftest.json")
        self.assertEqual(selftest["verdict"], "SUCCESS")
        self.assertTrue(all(r["mismatches"] == 0 for r in selftest["results"]))

    def test_python_report(self):
        py = load("python-lovelock-report.json")
        assert_checks_all_pass(self, py, PY_CHECK_COUNT)
        for name in ("curvature.json", "lovelock-tensors.json"):
            self.assertEqual(py["inputsSha256"][name], PINNED[name])
        names = {c["name"] for c in py["checks"]}
        for k in (1, 2, 3):
            self.assertIn(f"rust_k{k}_mixed_components_agree", names)
            self.assertIn(f"rust_k{k}_contravariant_components_agree", names)
        for name in ("k2_equals_minus_8_gauss_bonnet", "normalisation_P2_derived_minus_8",
                     "k1_equals_minus_4_einstein", "normalisation_P1_derived_minus_4",
                     "gkd_literal_equals_cofactor_expansion", "negative_controls_detected"):
            self.assertIn(name, names)

    def test_wolfram_report(self):
        wl = load("wolfram-gkd-report.json")
        assert_checks_all_pass(self, wl, WOLFRAM_CHECK_COUNT)
        self.assertEqual(wl["expectedCheckCount"], WOLFRAM_CHECK_COUNT)
        names = {c["name"] for c in wl["checks"]}
        for p in (1, 2, 3):
            self.assertIn(f"gkd_equals_kdelta_exhaustive_length_{p}", names)
        for p in (4, 5, 6, 7):
            self.assertIn(f"gkd_equals_kdelta_random_length_{p}", names)
        for k in (1, 2):
            self.assertIn(f"k{k}_P_equals_rust_all_64_components", names)
            self.assertIn(f"k{k}_A_equals_rust_all_64_components", names)
        self.assertEqual(wl["authorDefinition"],
                         "kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]")
        for rel in ("Revision/gkd_lovelock/results/curvature.json", "Revision/gkd_lovelock/results/lovelock-tensors.json"):
            self.assertEqual(wl["inputSha256"][rel], PINNED[Path(rel).name])
        for rel, digest in wl["sourceSha256"].items():
            self.assertEqual(sha256(ROOT / rel), digest, rel)


@unittest.skipIf(FAST, "REVISION_FAST=1")
class TestSlowRuns(unittest.TestCase):
    def test_SLOW_rust_binary_and_checker_twice(self):
        exe = build_rust()
        if exe is None:
            self.skipTest("cargo or the release binary is not available")
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            tmp = Path(tmp)
            rust_dirs = [tmp / "rust1", tmp / "rust2"]
            for d in rust_dirs:
                d.mkdir()
            tampered = tmp / "tampered"
            tampered.mkdir()
            shutil.copyfile(ART / "curvature.json", tampered / "curvature.json")
            data = load("lovelock-tensors.json")
            data["P3_mixed_up_h_down_j"]["x1,x1"]["monomials"][0][0] += 1
            (tampered / "lovelock-tensors.json").write_text(json.dumps(data), encoding="utf-8")
            reports = [tmp / "py1.json", tmp / "py2.json", tmp / "py_tampered.json"]
            procs = [start([str(exe), "lovelock", "--output", str(d), "--brute-force-k2"]) for d in rust_dirs]
            procs += [start([sys.executable, str(CHECKER), "--report", str(r)]) for r in reports[:2]]
            procs.append(start([sys.executable, str(CHECKER), "--artifacts", str(tampered), "--report", str(reports[2])]))
            results = [finish(p) for p in procs]
            for code, out in results[:4]:
                self.assertEqual(code, 0, out[-3000:])
            self.assertEqual(results[4][0], 1, results[4][1][-3000:])
            for name in RUST_LOVELOCK_OUTPUTS:
                one, two = (rust_dirs[0] / name).read_bytes(), (rust_dirs[1] / name).read_bytes()
                self.assertEqual(one, two, f"Rust output {name} differs between two runs")
                self.assertEqual(hashlib.sha256(one).hexdigest(), PINNED[name], f"Rust output {name} differs from the committed file")
            one, two = reports[0].read_bytes(), reports[1].read_bytes()
            self.assertEqual(one, two, "checker report differs between two runs")
            self.assertEqual(hashlib.sha256(one).hexdigest(), PINNED["python-lovelock-report.json"])
            assert_checks_all_pass(self, json.loads(one), PY_CHECK_COUNT)
            bad = json.loads(reports[2].read_bytes())
            self.assertEqual(bad["verdict"], "FAILURE")
            self.assertIn("rust_k3_mixed_components_agree", bad["failedChecks"])
            self.assertIn("rust_text_matches_monomials", bad["failedChecks"])
            self.assertNotIn("k3_trace_identity", bad["failedChecks"])  # own results are unaffected

    def test_SLOW_wolfram_check_reproduces_the_report(self):
        ws = shutil.which("wolframscript")
        if ws is None or shutil.which("cargo") is None:
            self.skipTest("wolframscript or cargo is not available")
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            out = Path(tmp) / "wolfram-gkd-report.json"
            proc = start([ws, "-file", str(WOLFRAM_SCRIPT), str(out)],
                         env={"LOVELOCK_GKD_EXPORT_DIR": str(Path(tmp) / "export"), "LOVELOCK_GKD_K3_UNPRUNED": "none"})
            code, text = finish(proc)
            self.assertEqual(code, 0, text[-3000:])
            self.assertEqual(sha256(out), PINNED["wolfram-gkd-report.json"], "Wolfram report differs from the committed file")

    @unittest.skipUnless(SELFTEST, "set LOVELOCK_GKD_SELFTEST=1 to rerun the GKD self-test")
    def test_SLOW_rust_gkd_selftest_twice(self):
        exe = build_rust()
        if exe is None:
            self.skipTest("cargo or the release binary is not available")
        with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
            dirs = [Path(tmp) / "a", Path(tmp) / "b"]
            for d in dirs:
                d.mkdir()
            procs = [start([str(exe), "gkd-selftest", "--exhaustive-max", "4", "--output", str(d)]) for d in dirs]
            for code, out in (finish(p, timeout=3600) for p in procs):
                self.assertEqual(code, 0, out[-3000:])
            one, two = (dirs[0] / "gkd-selftest.json").read_bytes(), (dirs[1] / "gkd-selftest.json").read_bytes()
            self.assertEqual(one, two)
            self.assertEqual(hashlib.sha256(one).hexdigest(), PINNED["gkd-selftest.json"])


if __name__ == "__main__":
    unittest.main()
