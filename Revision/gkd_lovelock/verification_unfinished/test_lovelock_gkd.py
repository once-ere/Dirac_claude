#!/usr/bin/env python3
"""Tests for the Lovelock tensors of (4.38) computed with GKD (studies/lovelock_gkd, Rust) and for
the independent sympy checker scripts/check_lovelock_gkd.py.

Run from the repository root:
    python -m unittest discover -s tests -p "test_lovelock_gkd.py" -v

What is tested
  * fast unit tests of the checker's pieces: the literal generalized delta kdelta
    (= Det[Outer[delta, lower, upper]]), the exact normal form ``canon``, the readers of the Rust
    output, and negative controls (a tampered component is detected);
  * the committed outputs in artifacts/lovelock-gkd/ have the pinned sha256 digests below and
    their reports say SUCCESS with every check passed;
  * SLOW (skipped when D16C_FAST=1, about 30-60 s): the Rust binary is built if needed
    (cargo build --release) and `lovelock --brute-force-k2` is run twice into temporary
    directories: both runs must be byte-identical to each other and to the committed files;
    the checker is run twice (in parallel) into temporary reports: both must be byte-identical,
    pass every check and equal the committed python-lovelock-report.json; and the checker, run
    on a copy of the Rust output with one tampered component, must fail;
  * VERY SLOW (only when LOVELOCK_GKD_SELFTEST=1, about 6 minutes): `gkd-selftest
    --exhaustive-max 4` is run twice and must reproduce the committed gkd-selftest.json.
Everything is written into tempfile directories; the committed files are never touched.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_lovelock_gkd as C  # noqa: E402

CRATE = ROOT / "studies" / "lovelock_gkd"
ART = ROOT / "artifacts" / "lovelock-gkd"
EXE = CRATE / "target" / "release" / ("lovelock_gkd.exe" if os.name == "nt" else "lovelock_gkd")
CHECKER = ROOT / "scripts" / "check_lovelock_gkd.py"
FAST = os.environ.get("D16C_FAST") == "1"
SELFTEST = os.environ.get("LOVELOCK_GKD_SELFTEST") == "1"

# sha256 of the committed outputs (files are stored byte-for-byte: .gitattributes "* -text").
PINNED = {
    "curvature.json": "d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e",
    "lovelock-tensors.json": "9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567",
    "lovelock-components.md": "65f95810d3b7b6696227670f03241c20758bcee4e408743803200cae68a1b8e7",
    "lovelock-report.json": "5c919ea827a5e6822a7196bb66ead64fa0a3e70f01f35b2bbfb99a65ae028bb8",
    "gkd-selftest.json": "6cd72bd8d5d8d2f7acb4825ed0a975a26aaad343e323b9c96f6d1fc4f294d1dc",
    "python-lovelock-report.json": "166bab5f2575b55076eb1b36deab5ed802344874b6707f0d91751ad826aa6053",
}
RUST_LOVELOCK_OUTPUTS = ["curvature.json", "lovelock-tensors.json", "lovelock-components.md", "lovelock-report.json"]
CHECK_COUNT = 49


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build_rust():
    """cargo build --release (a no-op when up to date); returns the binary or None without cargo."""
    cargo = shutil.which("cargo")
    if cargo is None:
        return None
    subprocess.run([cargo, "build", "--release", "--manifest-path", str(CRATE / "Cargo.toml")],
                   check=True, cwd=ROOT, capture_output=True)
    return EXE if EXE.exists() else None


def start(cmd):
    return subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            env={**os.environ, "PYTHONIOENCODING": "utf-8"})


def finish(proc, timeout=1800):
    out, _ = proc.communicate(timeout=timeout)
    return proc.returncode, out.decode("utf-8", "replace")


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
        import itertools
        for m in (1, 2, 3):
            for lower in itertools.product(range(4), repeat=m):
                for upper in itertools.product(range(4), repeat=m):
                    ref = C.cofactor_det([[1 if lo == up else 0 for up in upper] for lo in lower])
                    self.assertEqual(C.kdelta(lower, upper), ref, (lower, upper))

    def test_antisymmetry_and_pigeonhole(self):
        import random
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
        tensors = json.loads((ART / "lovelock-tensors.json").read_text(encoding="utf-8"))
        entry = tensors["A3_contravariant_l_h"]["x5,x5"]
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

    def test_reports_say_success(self):
        rust = json.loads((ART / "lovelock-report.json").read_text(encoding="utf-8"))
        self.assertEqual(rust["verdict"], "SUCCESS")
        self.assertEqual(rust["failedCheckCount"], 0)
        self.assertTrue(all(c["passed"] for c in rust["checks"].values()))
        selftest = json.loads((ART / "gkd-selftest.json").read_text(encoding="utf-8"))
        self.assertEqual(selftest["verdict"], "SUCCESS")
        self.assertTrue(all(r["mismatches"] == 0 for r in selftest["results"]))
        py = json.loads((ART / "python-lovelock-report.json").read_text(encoding="utf-8"))
        self.assertEqual(py["verdict"], "SUCCESS")
        self.assertEqual(py["failedCheckCount"], 0)
        self.assertEqual(py["checkCount"], CHECK_COUNT)
        self.assertTrue(all(c["passed"] for c in py["checks"].values()))
        for name in ("curvature.json", "lovelock-tensors.json"):
            self.assertEqual(py["inputsSha256"][name], PINNED[name])


@unittest.skipIf(FAST, "D16C_FAST=1")
class TestSlowRuns(unittest.TestCase):
    def test_SLOW_rust_binary_and_checker_twice(self):
        exe = build_rust()
        if exe is None:
            self.skipTest("cargo or the release binary is not available")
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            rust_dirs = [tmp / "rust1", tmp / "rust2"]
            for d in rust_dirs:
                d.mkdir()
            tampered = tmp / "tampered"
            tampered.mkdir()
            shutil.copyfile(ART / "curvature.json", tampered / "curvature.json")
            data = json.loads((ART / "lovelock-tensors.json").read_text(encoding="utf-8"))
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
            report = json.loads(one)
            self.assertEqual(report["verdict"], "SUCCESS")
            self.assertEqual(report["checkCount"], CHECK_COUNT)
            self.assertTrue(all(c["passed"] for c in report["checks"].values()))
            bad = json.loads(reports[2].read_bytes())
            self.assertEqual(bad["verdict"], "FAILURE")
            self.assertIn("rust_k3_mixed_components_agree", bad["failedChecks"])
            self.assertIn("rust_text_matches_monomials", bad["failedChecks"])
            self.assertNotIn("k3_equals", " ".join(bad["failedChecks"]))  # own results are unaffected

    @unittest.skipUnless(SELFTEST, "set LOVELOCK_GKD_SELFTEST=1 to rerun the 6-minute GKD self-test")
    def test_SLOW_rust_gkd_selftest_twice(self):
        exe = build_rust()
        if exe is None:
            self.skipTest("cargo or the release binary is not available")
        with tempfile.TemporaryDirectory() as tmp:
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
