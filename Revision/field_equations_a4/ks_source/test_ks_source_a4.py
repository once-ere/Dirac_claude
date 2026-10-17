#!/usr/bin/env python3
"""Tests for Revision/field_equations_a4/ks_source (the field equations for a4 and b4 with the Kohn-Sham source; the
corrected primordial metric of 2026-10-16, version 2).

Run from the repository root:
    python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v

What is tested
  * the numerical helpers of ks_source_a4.py (Simpson, the 4th-order derivative, the bulk edge of the free k = 0
    spectrum) on cases with known exact answers, and the theory functions built from a4-equations.json (the Einstein
    components in closed form, the record's history source);
  * the committed report: every check has a name, a verdict and a detail, all PASS, the summary counts agree, the
    sha256 digests of the inputs recorded in it are those of the current input files (the report is in sync), and
    the result tables have the expected rows; every integrated case satisfies the constraint at its end point,
    recomputed here from the table and the theory functions;
  * SLOW (skipped when REVISION_FAST=1): the script is run twice into temporary directories; both runs are
    byte-identical, the CSV tables are byte-identical to the committed ones and the report and the summary agree with
    the committed ones up to the output paths;
  * SLOW negative controls: a copy of the Kohn-Sham results with one profile value of p0 of an interacting state changed
    (the x0 conservation identity is broken at one grid point; p0 vanishes identically for lambda = 0) and a copy with
    one integral changed must make the script fail (exit 1, the expected checks FAIL). Temporary files go to tempfile
    directories; the committed files are never touched.
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
A4_JSON = ROOT / "Revision" / "field_equations_a4" / "a4-equations.json"
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

    def test_quadrature_and_derivative(self):
        self.assertAlmostEqual(self.m.simpson([t ** 3 for t in [0, 0.5, 1.0]], 0.5), 0.25, places=14)
        h = 0.02
        xs = [-3.0 + h * i for i in range(151)]
        d = self.m.deriv4([x ** 4 for x in xs], h)
        self.assertLess(max(abs(a - 4 * x ** 3) for a, x in zip(d, xs)), 1e-9)     # exact for quartics up to rounding

    def test_bulk_edge(self):
        # odd l = 0 level of the free k = 0 problem: sqrt(1 + p^2) with tan(p f L) = -p (M = 1)
        for f in (1.0, 0.6, 1.4):
            e = self.m.bulk_edge(f, 3.0)
            p = math.sqrt(e * e - 1.0)
            self.assertLess(abs(math.sin(p * f * 3.0) + p * math.cos(p * f * 3.0)), 1e-12)
            self.assertLess(e, math.sqrt(1.0 + (math.pi / (f * 3.0)) ** 2))
        self.assertAlmostEqual(self.m.bulk_edge(1.0, 3.0), 1.2922928280687830, places=12)   # results/parameters.json bulkEdge

    def test_theory_functions(self):
        th = self.m.part_a(json.loads(A4_JSON.read_text(encoding="utf-8")))
        e = th["einstein"]
        # the Einstein components (a4-equations.json einstein): x4: 3 a'^2 + 6 kk + Lam - (3/2) u^2 (H = 1)
        for (a, u, kk, lam) in ((1.0, 4 / 3, 1.0, -10.0), (0.3, -0.7, 2.5, 0.4)):
            self.assertAlmostEqual(e["F4"](a, u, kk, lam), 3 * a * a + 6 * kk + lam - 1.5 * u * u, places=12)
            self.assertAlmostEqual(e["F1"](a, 0.2, u, -0.1, kk, lam),
                                   -5 * a * a + 0.4 + 6 * kk + lam + 6 * a * u - 2.5 * u * u + 0.2, places=12)
            self.assertAlmostEqual(e["F0"](a, 0.2, u, -0.1, kk, lam),
                                   -3 * a * a + 3 * kk + lam + 1.5 * a * u - 1.5 * u * u + 0.15, places=12)
            J = e["J"]
            self.assertEqual([[J[i][k](a, u, kk) for k in range(2)] for i in range(2)], [[2.0, -2.0], [0.0, -1.5]])
        # the author's weights on the record's history at x4 = 0: kappa rho = -(F4 + Lambda) = 3.57407... (kk = 1)
        a_ = th["author"]
        self.assertAlmostEqual(-(a_["F4"](1.0, 4 / 3, 1.0, -10.0)), 10 - (121 / 432 + 161 / 24 - 9 / 16), places=12)

    def test_report_all_pass(self):
        rep = json.loads(REPORT.read_text(encoding="utf-8"))
        names = [c["name"] for c in rep["checks"]]
        self.assertEqual(len(names), len(set(names)))
        for c in rep["checks"]:
            self.assertEqual(set(c), {"name", "verdict", "detail"})
            self.assertEqual(c["verdict"], "PASS", c["name"])
            self.assertTrue(c["detail"])
        self.assertEqual(rep["summary"], {"checks": len(names), "pass": len(names), "fail": 0})
        self.assertEqual(sorted(names), sorted(
            ["A1_hidden_equals_extra_times_and_no_offdiagonal", "A2_constraint_first_order_second_order_system",
             "A3_constraint_propagation", "A4_x0_conservation_in_y", "A5_free_fold_band_gas_conserves_energy",
             "A6_history_source_reproduced", "B0_source_condition_report_verified", "B1_integrals_reproduced",
             "B2_x0_conservation_on_every_profile", "B3_hidden_direction_mismatch",
             "C1_averaged_hidden_pressure_condition", "C2_energy_relation_along_the_dense_history",
             "C3_record_history_not_sourced_by_the_gas", "C4_source_signs", "D0_free_gas_average_exact",
             "D1_two_step_sizes_agree", "D2_author_weights_from_the_record_history",
             "D3_constraint_kept_along_the_solutions", "D4_outcomes"]))
        self.assertIn("corrected primordial metric of 2026-10-16", rep["metric"])

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
        self.assertEqual(len(cas), 2 * (1 + 3 * 6))                     # 2 free series: the author's 1 case, 3 theories x 6
        for b in (MOMENTS, CASES, REPORT, SUMMARY):
            self.assertNotIn(b"\r", b.read_bytes(), b.name)
        # every case satisfies the constraint at its end point, recomputed from the table and the theory functions
        th = self.m.part_a(json.loads(A4_JSON.read_text(encoding="utf-8")))
        for c in cas:
            a4, b4, ap, u = (float(c[k]) for k in ("a4_end", "b4_end", "a4p_end", "u_end"))
            lam, sig0 = float(c["Lambda"]), float(c["sigma0"])
            kk = math.exp(2 * a4) / b4
            res = th[c["gravity"]]["F4"](ap, u, kk, lam) + sig0 / b4 ** 2
            scale = abs(sig0) + abs(lam) + 1 + abs(th[c["gravity"]]["F4"](ap, u, kk, 0.0))
            self.assertLess(abs(res) / scale, 1e-7, c)
            self.assertEqual(c["outcome"], c["m2_outcome"], c)


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
            rep["report"] = committed["report"]
            self.assertEqual(rep, committed)
            md = o["reports/ks-source-a4-summary.md"].decode("utf-8").replace(
                o["dir"] + "/reports/ks-source-a4.json", committed["report"])
            self.assertEqual(md, SUMMARY.read_text(encoding="utf-8"))

    def _tampered(self, edit) -> tuple:
        d = Path(tmpdir())
        ks = d / "ks"
        (ks / "ground").mkdir(parents=True)
        shutil.copytree(KS_RESULTS / "ground" / "profiles", ks / "ground" / "profiles")
        shutil.copytree(KS_RESULTS / "ground" / "levels", ks / "ground" / "levels")
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
            p = ks / "ground" / "profiles" / "N592_lamp1_a10.csv"
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
                if ln.startswith("N2352_lam0_a05,"):
                    row = ln.split(",")
                    row[j] = repr(float(row[j]) * 1.001)
                    lines[i] = ",".join(row)
            p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
        r, v = self._tampered(edit)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(v["B1_integrals_reproduced"], "FAIL")


if __name__ == "__main__":
    unittest.main()
