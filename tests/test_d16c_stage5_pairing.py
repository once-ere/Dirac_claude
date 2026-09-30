"""Unit tests for the independent Stage-5 pairing checker scripts/check_dirac16complex_pairing.py.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_stage5_pairing.py" -v
The fast subset (every test whose name does not contain SLOW) calls the family
functions directly with reduced component/vector sets, shares one PairAlgebra and
one BlockReduction, includes negative controls (a wrong sign map, the identity
instead of gamma^8, the wrong Wick sign, the wrong block route, a tampered Wolfram
export and missing files are all detected) and writes only into tempfile
directories.  The SLOW tests (the command-line entry point in --quick mode, the
G1-jet and Z2 families, a time-like reflection, the primordial-field and
pair-total families) are skipped when D16C_FAST=1; the fast subset takes about
30 s on an idle machine.
"""

import contextlib
import copy
import io
import json
import os
import sys
import tempfile
import unittest
from fractions import Fraction

import sympy as sp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import check_dirac16complex_pairing as P  # noqa: E402

FAST = os.environ.get("D16C_FAST") == "1"
_CACHE = {}


def algebra():
    if "pa" not in _CACHE:
        _CACHE["pa"] = P.PairAlgebra(P.DEFAULT_FIXTURE)
        _CACHE["red"] = P.KS.BlockReduction(_CACHE["pa"].alg)
    return _CACHE["pa"], _CACHE["red"]


def cached(name, function):
    if name not in _CACHE:
        _CACHE[name] = function()
    return _CACHE[name]


def recorder_of(result):
    return result[0] if isinstance(result, tuple) else result


class ExactHelperTests(unittest.TestCase):

    def test_sparse_polynomials(self):
        vt = P.VarTable()
        x, y, z = vt.var("x"), vt.var("y"), vt.var("z")
        p = P.SPoly({(x, x, y): Fraction(3), (y, z): Fraction(-1, 2)})
        self.assertEqual(p.deriv(x).t, {(x, y): Fraction(6)})
        self.assertEqual(p.all_derivatives()[y].t, {(x, x): Fraction(3), (z,): Fraction(-1, 2)})
        # d/dt with x -> z, y -> x (z constant): 3 x^2 y -> 6 x z y + 3 x^3; -(1/2) y z -> -(1/2) x z
        d = p.total_derivative({x: z, y: x})
        self.assertEqual(d.t, {tuple(sorted((x, y, z))): Fraction(6), (x, x, x): Fraction(3),
                               tuple(sorted((x, z))): Fraction(-1, 2)})
        self.assertEqual(p.signed({x: -1}).t, p.t)            # x appears squared
        self.assertEqual(p.signed({y: -1}).t, (-p).t)
        self.assertTrue((p - p).is_zero())
        self.assertEqual(p.mul(P.SPoly({(z,): Fraction(2)})).nterms(), 2)

    def test_exact_inverse_and_cayley(self):
        K = P.STAT_K["U1"]
        U = P.cayley_unitary(K)
        self.assertTrue(P.mat_eq(P.mat_mul(P.mat_dagger(U), U), P.mat_eye(4)))
        inv = P.mat_inverse_cq(U)
        self.assertTrue(P.mat_eq(P.mat_mul(inv, U), P.mat_eye(4)))
        with self.assertRaises(ZeroDivisionError):
            P.mat_inverse_cq(P.mat_zero(3))

    def test_wolfram_parsers(self):
        self.assertEqual(P.parse_wolfram_list("{1, -1, 1/2}"), [1, -1, Fraction(1, 2)])
        self.assertEqual(P.parse_wolfram_floats("{1.5`17., -2.25`17.}"), [1.5, -2.25])
        text = '<|"gamma^2" -> {{6}, {7}}, "gamma^5" -> {{5}, {4}}|>'
        self.assertEqual(P.parse_wolfram_targets(text), {"gamma^2": [[6], [7]], "gamma^5": [[5], [4]]})
        e = P.wolfram_expr("(2*Mz)/(E^a4c*(-H + 2*Mz))", {"E": sp.E, "Mz": sp.Symbol("M"), "a4c": P.KS.A4C, "H": P.KS.H})
        self.assertEqual(sp.simplify(e - 2 * sp.Symbol("M") * sp.exp(-P.KS.A4C) / (2 * sp.Symbol("M") - P.KS.H)), 0)

    def test_report_format(self):
        report = P.build_report({"S5_x": True, "S5_y": False}, {"m": {"a": Fraction(1, 3)}}, {})
        lines, failed = P.report_lines(report)
        self.assertEqual(failed, 1)
        self.assertIn("check_count=2", lines)
        self.assertIn("failed_check_count=1", lines)
        data = P.canonical_json_bytes(report)
        self.assertTrue(data.endswith(b"\n") and b"\r\n" not in data)
        self.assertEqual(json.loads(data.decode())["measurements"]["m"]["a"], "1/3")
        self.assertEqual(set(report), {"schemaVersion", "producer", "checks", "measurements", "sourceSha256", "inputSha256"})


class AlgebraTests(unittest.TestCase):

    def test_algebra_family(self):
        pa, _ = algebra()
        rec = cached("algebra", lambda: P.check_algebra(pa))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(rec.measurements["oddBilinearMatrixCount"], 456)
        self.assertEqual(rec.measurements["uBudaggerSigns"], [1, 1, 1, 1, 1, -1, -1, -1])

    def test_characters(self):
        pa, _ = algebra()
        self.assertEqual([P.pin_character(pa, pa.gamma[a]) for a in range(8)], [-1] * 4 + [1] * 4)
        u = pa.unit_vector(P.SPACELIKE_VECTORS["spacelikeRational"])
        self.assertEqual(P.pin_character(pa, u), -1)
        self.assertEqual(P.krein_sign(pa, u), 0)        # a general vector mixes +B and -B


class T1Tests(unittest.TestCase):

    def test_generic_polynomial_identities(self):
        pa, _ = algebra()
        rec = cached("T1generic", lambda: P.check_t1generic(pa, quick=True))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(rec.measurements["kineticMonomials"], 23552)
        self.assertEqual(rec.measurements["connectionMonomials"], 21504)

    def test_generic_negative_controls(self):
        pa, _ = algebra()
        gt = P.GenericT1(pa)
        # flip Psi but not Psi^*: the identity must fail
        bad = {v: s for v, s in gt.sign_g8.items() if gt.vt.names[v][0].startswith(("psi", "dpsi", "ddpsi"))
               and not gt.vt.names[v][0].startswith(("psis", "dpsis", "ddpsis"))}
        self.assertFalse((gt.L.signed(bad) + gt.L.signed(gt.sign_ml)).is_zero())
        # the correct map with the SAME lambda fails (erratum E2)
        self.assertFalse((gt.L.signed(gt.sign_g8) + gt.L.signed(gt.sign_m)).is_zero())
        # the correct map with (-m, -lam) holds
        self.assertTrue((gt.L.signed(gt.sign_g8) + gt.L.signed(gt.sign_ml)).is_zero())

    def test_grassmann(self):
        pa, _ = algebra()
        rec = cached("T1grassmann", lambda: P.check_t1grassmann(pa, quick=True))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(rec.measurements["monomials_S2"], 120)
        self.assertEqual(rec.measurements["monomials_Ls"], 1288)
        gr = P.GrassmannT1(pa, max_deriv=1)
        L = gr.Ls(gr.m, gr.lam)
        self.assertNotEqual(L, -gr.Ls(-gr.m, -gr.lam))          # without the map the identity is false
        self.assertTrue(gr.g8(L) == -gr.Ls(-gr.m, -gr.lam))

    def test_krein_fock(self):
        pa, red = algebra()
        rec = cached("T1krein", lambda: P.check_t1krein(pa, red))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(rec.measurements["scalarDensity_particle0_particle1_hole2_hole3"], [1, 1, 1, 1])
        modes = P.krein_rest_modes(red)
        kf = P.KreinFock([m[0] for m in modes], [m[2] for m in modes])
        psi_m = [P.mat_scale(kf.psi[a], pa.chi[a]) for a in range(16)]
        psik_m = [P.mat_scale(kf.psik[a], pa.chi[a]) for a in range(16)]
        car = kf.car_matrix(psik_m, psi_m)
        proj = P.mat_zero(16)
        for v, _, _ in modes:
            for i in range(16):
                for l in range(16):
                    proj[i][l] = proj[i][l] + v[i] * v[l].conj()
        self.assertFalse(P.mat_eq(car, P.mat_mul(pa.B, P.mat_mul(P.mat_mul(pa.g8, proj), pa.g8))))   # not +B


class T2Tests(unittest.TestCase):

    def test_frame_reflection_gamma0(self):
        pa, _ = algebra()
        rec, table = P.check_t2frame(pa, vectors=[("gamma^0", (1, 0, 0, 0, 0, 0, 0, 0))])
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(table[0]["twisted_u"]["result"], "L_{m,lambda}[e R_u, u Psi] = +L_{-m,lambda}[e, Psi]")
        self.assertEqual(table[0]["untwisted_u"]["result"], "L_{m,lambda}[-e R_u, u Psi] = -L_{m,-lambda}[e, Psi]")
        self.assertEqual(P.lagrangian_map_string("e R_u", "u Psi", -1, 1), "L_{m,lambda}[e R_u, u Psi] = -L_{-m,-lambda}[e, Psi]")


class T3Tests(unittest.TestCase):

    def test_block_maps(self):
        pa, red = algebra()
        rec, own = cached("T3block", lambda: P.check_t3block(pa, red))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(rec.measurements["gamma8PhasesByTargetBlock"], [1, 1, -1, -1, 1, 1, -1, -1])
        self.assertEqual(own["densitySigns"]["sigma2"], [1, -1, 1, 1])
        # negative control: sigma1 is not the gamma^8 route (it flips k, keeps j)
        N = P.KS.block_ode_matrix
        self.assertNotEqual(sp.simplify(P.SIG1 * N() * P.SIG1 - N(M=-P.MM, j=-P.JS)), sp.zeros(2))

    def test_ks_family(self):
        pa, _ = algebra()
        rec, own = cached("T3ks", lambda: P.check_t3ks(pa))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertAlmostEqual(own["cValues"]["cPlus"], 1.9051482536448665, places=12)
        self.assertAlmostEqual(own["cValues"]["cControl"], 13.421975197576822, places=11)

    def test_orbital_emt_quick(self):
        pa, red = algebra()
        rec, found = P.check_t3emt(pa, red, quick=True)
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(found["rho = T_44"]["n"], "eps - vv")


class StatisticsTests(unittest.TestCase):

    def test_stat_family(self):
        pa, red = algebra()
        rec, own = cached("stat", lambda: P.check_stat(pa, red))
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(own["filledShellRatio"], Fraction(1, 8))
        self.assertEqual(own["restShellCovarianceEigenvalues"], [-1] * 4 + [0] * 8 + [1] * 4)

    def test_wrong_wick_signs_are_detected(self):
        fw = P.FermionWick()
        U = P.cayley_unitary(P.STAT_K["U2"])
        f = P.FERMION_OCCUPATIONS[2]
        rho = P.rho_matrix(U, f)
        got = fw.expectation(P.STAT_A, P.STAT_B, U, f, normal=True)
        plus, _ = P.wick_prediction(P.STAT_A, P.STAT_B, rho, +1)
        minus, _ = P.wick_prediction(P.STAT_A, P.STAT_B, rho, -1)
        self.assertEqual(got, minus)
        self.assertNotEqual(got, plus)


class WolframAgreementTests(unittest.TestCase):

    def own(self):
        pa, red = algebra()
        rec_alg = cached("algebra", lambda: P.check_algebra(pa))
        rec_gen = cached("T1generic", lambda: P.check_t1generic(pa, quick=True))
        rec_gr = cached("T1grassmann", lambda: P.check_t1grassmann(pa, quick=True))
        rec_kr = cached("T1krein", lambda: P.check_t1krein(pa, red))
        _, blk = cached("T3block", lambda: P.check_t3block(pa, red))
        _, ks = cached("T3ks", lambda: P.check_t3ks(pa))
        _, st = cached("stat", lambda: P.check_stat(pa, red))
        return {"pa": pa, "oddCount": rec_alg.measurements["oddBilinearMatrixCount"], "uB": rec_alg.measurements["uBudaggerSigns"],
                "kinetic": rec_gen.measurements["kineticMonomials"], "connection": rec_gen.measurements["connectionMonomials"],
                "grassmannLs": rec_gr.measurements["monomials_Ls"], "grassmannS2": rec_gr.measurements["monomials_S2"],
                "kreinScalar": rec_kr.measurements["scalarDensity_particle0_particle1_hole2_hole3"],
                "phases8": blk["phases8"], "phases1": blk["phases1"], "targets": blk["targets"],
                "densitySigns": blk["densitySigns"], "basisIdentical": P.basis_identical_to_stage4(red),
                "cPlus": ks["cPlus"], "cControl": ks["cControl"], "cValues": ks["cValues"],
                "filledShellRatio": st["filledShellRatio"], "covariance": st["restShellCovarianceEigenvalues"],
                "t2table": {}, "ownStatementsVerified": True}

    def test_agreement_with_committed_exports(self):
        if not (os.path.exists(P.DEFAULT_THEORY) and os.path.exists(P.DEFAULT_WOLFRAM_REPORT)):
            self.skipTest("Wolfram exports not present")
        rec = P.check_wolfram_agreement(self.own(), P.DEFAULT_THEORY, P.DEFAULT_WOLFRAM_REPORT)
        self.assertTrue(rec.ok(), rec.checks)

    def test_tampered_export_is_detected(self):
        if not os.path.exists(P.DEFAULT_THEORY):
            self.skipTest("Wolfram exports not present")
        with open(P.DEFAULT_THEORY, "r", encoding="utf-8") as handle:
            theory = json.load(handle)
        bad = copy.deepcopy(theory)
        bad["T3"]["blockMaps"]["gamma8"]["phasesByTargetBlock"][0] = ["-1", "0"]
        bad["T2"]["table"][0]["character"] = "1"
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "pairing-theory.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(bad, handle)
            rec = P.check_wolfram_agreement(self.own(), path, P.DEFAULT_WOLFRAM_REPORT)
            self.assertFalse(rec.checks["S5_wolfram_blockMaps"])
            self.assertFalse(rec.checks["S5_wolfram_T2table"])
            self.assertFalse(rec.ok())
            rec2 = P.check_wolfram_agreement(self.own(), os.path.join(tmp, "missing.json"), P.DEFAULT_WOLFRAM_REPORT)
            self.assertEqual(rec2.checks, {"S5_wolfram_filesPresent": False})

    def test_committed_report_is_current(self):
        if not os.path.exists(P.DEFAULT_OUTPUT):
            self.skipTest("python-pairing-report.json not present")
        with open(P.DEFAULT_OUTPUT, "r", encoding="utf-8") as handle:
            report = json.load(handle)
        self.assertEqual(report["producer"], P.PRODUCER)
        self.assertTrue(all(report["checks"].values()))
        self.assertTrue(report["checks"][P.WOLFRAM_CHECK])
        self.assertFalse(report["measurements"]["quick"])
        self.assertGreaterEqual(len(report["checks"]), 170)
        for rel, digest in report["sourceSha256"].items():
            self.assertEqual(P.sha256_file(os.path.join(REPO, rel)), digest, rel)


@unittest.skipIf(FAST, "D16C_FAST=1")
class SlowTests(unittest.TestCase):

    def test_SLOW_jets_quick(self):
        pa, _ = algebra()
        rec = P.check_t1jets(pa, quick=True)
        self.assertTrue(rec.ok(), rec.checks)
        self.assertNotIn("S5_T1jets_conservationBoth", rec.checks)    # order-2 jets only in the full run

    def test_SLOW_z2_and_timelike_reflection(self):
        pa, _ = algebra()
        self.assertTrue(P.check_t2z2(pa, quick=True).ok())
        rec, table = P.check_t2frame(pa, vectors=[("timelikeRational", P.TIMELIKE_VECTORS["timelikeRational"])])
        self.assertTrue(rec.ok(), rec.checks)
        self.assertEqual(table[0]["twisted_u"]["result"], "L_{m,lambda}[e R_u, u Psi] = -L_{-m,-lambda}[e, Psi]")

    def test_SLOW_primordial_and_totals(self):
        pa, _ = algebra()
        self.assertTrue(P.check_t1primordial(pa).ok())
        self.assertTrue(P.check_totals(pa).ok())

    def test_SLOW_command_line_quick(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "report.json")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = P.main(["--quick", "--output", out])
            text = buf.getvalue()
            self.assertEqual(code, 0, text[-2000:])
            self.assertIn("failed_check_count=0", text)
            with open(out, "r", encoding="utf-8") as handle:
                report = json.load(handle)
            self.assertTrue(report["checks"][P.WOLFRAM_CHECK])
            self.assertTrue(report["measurements"]["quick"])


if __name__ == "__main__":
    unittest.main()
