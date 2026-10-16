#!/usr/bin/env python3
"""Tests for Revision/field_equations_a4/ks_source (the field equations for a4 and b4 with the Kohn-Sham source; the
author's metric with b4(x4), b4 a function of x4, never 1).

Run from the repository root:
    python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v

What is tested
  * the numerical helpers of ks_source_a4.py (Hermite and spline interpolation, Simpson, Gauss-Legendre, the Newton
    solve of the two algebraic equations) and the branches of the stated theories, on cases with known exact answers;
  * the committed report: every check has a name, a verdict and a detail, all PASS, the summary counts agree, the
    sha256 digests of the inputs recorded in it are those of the current input files (the report is in sync), and
    the result tables have the expected rows;
  * SLOW (skipped when REVISION_FAST=1): the script is run twice into temporary directories; both runs are
    byte-identical, the CSV tables are byte-identical to the committed ones and the report and the summary agree with
    the committed ones up to the output paths;
  * SLOW negative controls: a copy of the Kohn-Sham results with one profile value of p0 changed (the x0 conservation
    identity is broken at one grid point) and a copy with one integral changed must make the script fail (exit 1, the
    expected checks FAIL). Temporary files go to tempfile directories; the committed files are never touched.
Run time of the whole file: 18 s to 98 s on the development machine, depending on the load (2026-10-08); with
REVISION_FAST=1 about 7 s.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "ks_source_a4.py"
ROOT = HERE.parents[2]
KS_RESULTS = ROOT / "Revision" / "kohn_sham" / "results"
REPORT = HERE / "reports" / "ks-source-a4.json"
SUMMARY = HERE / "reports" / "ks-source-a4-summary.md"
MOMENTS = HERE / "results" / "ks-source-moments.csv"
CASES = HERE / "results" / "ks-source-a4-cases.csv"
FAST = os.environ.get("REVISION_FAST") == "1"


def load_module():
    spec = importlib.util.spec_from_file_location("ks_source_a4", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run(args: list) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT)] + args, capture_output=True, text=True, timeout=600)


def tmpdir() -> str:
    base = os.environ.get("REVISION_SCRATCH")
    return tempfile.mkdtemp(prefix="ks_source_", dir=base if base and os.path.isdir(base) else None)


class Helpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load_module()

    def test_hermite_reproduces_cubic(self):
        f = lambda x: 2 * x ** 3 - x ** 2 + 3 * x - 1
        df = lambda x: 6 * x ** 2 - 2 * x + 3
        xs = [0.0, 0.5, 1.0, 1.5, 2.0]
        for x in (0.1, 0.77, 1.3, 1.99):
            v, dv = self.m.hermite(xs, [f(t) for t in xs], [df(t) for t in xs], x)
            self.assertAlmostEqual(v, f(x), places=12)
            self.assertAlmostEqual(dv, df(x), places=11)

    def test_natural_spline_reproduces_linear(self):
        xs = [0.0, 0.5, 1.0, 1.5, 2.0]
        sp_ = self.m.natural_spline(xs, [3 - 2 * t for t in xs])
        for x in (0.2, 0.9, 1.6):
            self.assertAlmostEqual(sp_(x), 3 - 2 * x, places=13)

    def test_quadratures(self):
        self.assertAlmostEqual(self.m.simpson([t ** 3 for t in [0, 0.5, 1.0]], 0.5), 0.25, places=14)
        xs, ws = self.m.gauss_legendre()
        self.assertAlmostEqual(sum(w * x ** 10 for x, w in zip(xs, ws)), 2 / 11, places=13)
        self.assertAlmostEqual(sum(ws), 2.0, places=13)

    def test_newton_two_equations(self):
        # Q = a^2 + u^2 - 2 (circle), S4 = a - u: the solution with S4 = 0 near (1.1, 0.9) is (1, 1), det J = -4
        th = {"Q": lambda a, u: a * a + u * u - 2, "Qa": lambda a, u: 2 * a, "Qu": lambda a, u: 2 * u,
              "S4": lambda a, u: a - u, "S4a": lambda a, u: 1.0, "S4u": lambda a, u: -1.0}
        a, u, det = self.m.solve_rates(th, 1.1, 0.9, 0.0)
        self.assertAlmostEqual(a, 1.0, places=14)
        self.assertAlmostEqual(u, 1.0, places=14)
        self.assertAlmostEqual(det, -4.0, places=12)
        self.assertIsNone(self.m.solve_rates(th, 1.1, 0.9, 5.0))       # the line a - u = 5 misses the circle

    def test_branches_of_the_theories(self):
        th = self.m.part_a(json.loads((ROOT / "Revision" / "field_equations_a4" / "a4-equations.json").read_text(
            encoding="utf-8")))
        self.assertEqual(th["einstein"]["roots"], [])                    # Q = 3H/2: no history with b4 not constant
        self.assertEqual(len(th["author"]["roots"]), 1)
        self.assertAlmostEqual(th["author"]["roots"][0], 4 / 3, places=14)  # the record's history
        self.assertTrue(th["author"]["root_zero"])
        self.assertEqual(len(th["egb"]["roots"]), 2)
        for r, exact in zip(th["egb"]["roots"], (-6 - 20 ** 0.5, -6 + 20 ** 0.5)):
            self.assertAlmostEqual(r, exact, places=12)
        self.assertEqual(th["lovelock3"]["roots"], [])
        self.assertAlmostEqual(10.0 - th["author"]["S4"](1.0, 4 / 3), -2 / 27, places=14)   # -Lambda - S4, Lambda = -10


class CommittedReport(unittest.TestCase):
    def test_report_all_pass(self):
        rep = json.loads(REPORT.read_text(encoding="utf-8"))
        names = [c["name"] for c in rep["checks"]]
        self.assertEqual(len(names), len(set(names)))
        for c in rep["checks"]:
            self.assertEqual(set(c), {"name", "verdict", "detail"})
            self.assertEqual(c["verdict"], "PASS", c["name"])
            self.assertTrue(c["detail"])
        self.assertEqual(rep["summary"], {"checks": len(names), "pass": len(names), "fail": 0})
        self.assertGreaterEqual(len(names), 22)

    def test_report_in_sync_with_inputs(self):
        rep = json.loads(REPORT.read_text(encoding="utf-8"))
        for path, digest in rep["inputs"].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), digest, path)
        prof = sorted((ROOT / rep["inputProfiles"]["directory"]).glob("*.csv"))
        self.assertEqual(len(prof), rep["inputProfiles"]["files"])
        agg = hashlib.sha256("".join(hashlib.sha256(p.read_bytes()).hexdigest() for p in prof).encode()).hexdigest()
        self.assertEqual(agg, rep["inputProfiles"]["sha256OfSortedDigests"])

    def test_tables(self):
        with MOMENTS.open(encoding="utf-8", newline="") as fh:
            mom = list(csv.DictReader(fh))
        with CASES.open(encoding="utf-8", newline="") as fh:
            cas = list(csv.DictReader(fh))
        self.assertEqual(len(mom), 75)
        self.assertEqual(len(cas), 2 * (1 + 2 * 7))                     # 2 series: author 1 case, EGB 2 branches x 7
        self.assertEqual({c["event"] for c in cas}, {"regular", "fold", "adiabaticity_lost"})
        for b in (MOMENTS, CASES, REPORT, SUMMARY):
            self.assertNotIn(b"\r", b.read_bytes(), b.name)
        # every regular case satisfies the two algebraic equations at a4 = 2, recomputed here from the table, the
        # Kohn-Sham integrals (free gas: E at a4 = 2 is the record's, independent of b4) and the theory functions
        m = load_module()
        th = m.part_a(json.loads((ROOT / "Revision" / "field_equations_a4" / "a4-equations.json").read_text(
            encoding="utf-8")))
        with (KS_RESULTS / "ground" / "emt-integrals.csv").open(encoding="utf-8", newline="") as fh:
            E = {r["id"]: float(r["int_rho"]) for r in csv.DictReader(fh)}
        n = 0
        for c in cas:
            if c["event"] != "regular":
                continue
            a, u = float(c["rate_a20"]), float(c["u_a20"])
            t = th[c["gravity"]]
            sig = float(c["sigma0"]) * E[c["series"] + "_a20"] / E[c["series"] + "_a00"] * float(c["b4_ratio_end"]) ** -1.5
            self.assertLess(abs(t["Q"](a, u)), 1e-9 * (1 + abs(a) + abs(u)) ** 4, c)
            self.assertLess(abs(t["S4"](a, u) + float(c["Lambda"]) + sig), 1e-9 * (1 + abs(float(c["Lambda"]))), c)
            n += 1
        self.assertEqual(n, 8)


@unittest.skipIf(FAST, "REVISION_FAST=1")
class Rerun(unittest.TestCase):
    def test_two_runs_reproduce_committed(self):
        outs = []
        for _ in range(2):
            d = Path(tmpdir())
            try:
                r = run(["--out", str(d)])
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                outs.append({n: (d / n).read_bytes() for n in ("results/ks-source-moments.csv",
                                                                "results/ks-source-a4-cases.csv",
                                                                "reports/ks-source-a4.json",
                                                                "reports/ks-source-a4-summary.md")})
                outs[-1]["dir"] = d.resolve().as_posix()
            finally:
                shutil.rmtree(d, ignore_errors=True)
        a, b = outs
        self.assertEqual(a["results/ks-source-moments.csv"], b["results/ks-source-moments.csv"])
        self.assertEqual(a["results/ks-source-a4-cases.csv"], b["results/ks-source-a4-cases.csv"])
        self.assertEqual(a["results/ks-source-moments.csv"], MOMENTS.read_bytes())
        self.assertEqual(a["results/ks-source-a4-cases.csv"], CASES.read_bytes())
        committed = json.loads(REPORT.read_text(encoding="utf-8"))
        for o in (a, b):
            rep = json.loads(o["reports/ks-source-a4.json"].decode("utf-8"))
            rep["report"], rep["outputs"] = committed["report"], committed["outputs"]
            self.assertEqual(rep, committed)
            md = o["reports/ks-source-a4-summary.md"].decode("utf-8").replace(
                o["dir"] + "/reports/ks-source-a4.json", committed["report"])
            self.assertEqual(md, SUMMARY.read_text(encoding="utf-8"))

    def _tampered(self, edit) -> tuple:
        d = Path(tmpdir())
        ks = d / "ks"
        (ks / "ground").mkdir(parents=True)
        shutil.copytree(KS_RESULTS / "ground" / "profiles", ks / "ground" / "profiles")
        shutil.copy(KS_RESULTS / "ground" / "emt-integrals.csv", ks / "ground" / "emt-integrals.csv")
        shutil.copytree(KS_RESULTS / "adiabatic", ks / "adiabatic")
        shutil.copy(KS_RESULTS / "parameters.json", ks / "parameters.json")
        edit(ks)
        r = run(["--ks-results", str(ks), "--out", str(d / "out")])
        rep = json.loads((d / "out" / "reports" / "ks-source-a4.json").read_text(encoding="utf-8"))
        shutil.rmtree(d, ignore_errors=True)
        return r, {c["name"]: c["verdict"] for c in rep["checks"]}

    def test_negative_control_broken_x0_conservation(self):
        def edit(ks):
            p = ks / "ground" / "profiles" / "N136_lam0_a10.csv"
            lines = p.read_text(encoding="utf-8").split("\n")
            cols = lines[0].split(",")
            j = cols.index("p0")
            row = lines[76].split(",")                       # y = -1.5
            row[j] = repr(float(row[j]) * 1.5)
            lines[76] = ",".join(row)
            p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        r, v = self._tampered(edit)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(v["B2_x0_conservation_on_every_profile"], "FAIL")

    def test_negative_control_wrong_integral(self):
        def edit(ks):
            p = ks / "ground" / "emt-integrals.csv"
            lines = p.read_text(encoding="utf-8").split("\n")
            cols = lines[0].split(",")
            j = cols.index("int_rho")
            for i, ln in enumerate(lines):
                if ln.startswith("N688_lam0_a05,"):
                    row = ln.split(",")
                    row[j] = repr(float(row[j]) * 1.001)
                    lines[i] = ",".join(row)
            p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        r, v = self._tampered(edit)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(v["B1_integrals_reproduced"], "FAIL")


if __name__ == "__main__":
    unittest.main()
