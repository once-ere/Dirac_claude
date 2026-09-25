"""Unit tests for the independent Stage-4 Kohn-Sham theory checker (sympy + mpmath + stdlib).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_theory.py" -v
The fast subset (everything except the two tests tagged SLOW in their names)
runs in well under a minute; it calls the check functions directly on a shared
Algebra/BlockReduction, includes negative controls (a wrong gamma matrix, a
wrong kernel, a wrong closed form and a wrong parity are detected) and writes
only into tempfile directories.  The SLOW tests run the command-line entry point
in --quick mode and are skipped when the environment variable D16C_FAST=1 is set.
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from fractions import Fraction

import mpmath
import sympy as sp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import check_dirac16complex_kohn_sham_theory as T  # noqa: E402

_ALG = None
_RED = None
_REDUCTION_RUN = None
_EMT_RUN = None


def algebra():
    global _ALG
    if _ALG is None:
        _ALG = T.Algebra(T.DEFAULT_FIXTURE)
    return _ALG


def reduction():
    global _RED
    if _RED is None:
        _RED = T.BlockReduction(algebra())
    return _RED


def reduction_run():
    """(recorder, BlockReduction, block forms) of the full reduction family, computed once."""
    global _REDUCTION_RUN
    if _REDUCTION_RUN is None:
        rec = T.Recorder("reduction")
        T.check_reduction_a(algebra(), rec)
        red, forms = T.check_reduction_b(algebra(), rec)
        T.check_reduction_c(algebra(), rec)
        _REDUCTION_RUN = (rec, red, forms)
    return _REDUCTION_RUN


def emt_run():
    global _EMT_RUN
    if _EMT_RUN is None:
        _EMT_RUN = T.check_emt(algebra(), reduction())
    return _EMT_RUN


class ExactArithmeticTests(unittest.TestCase):

    def test_gaussian_rationals(self):
        a = T.CQ(Fraction(1, 2), Fraction(-3, 4))
        b = T.CQ(2, 5)
        self.assertEqual(a * b, T.CQ(Fraction(1, 2) * 2 + Fraction(3, 4) * 5, Fraction(5, 2) - Fraction(3, 2)))
        self.assertEqual(a * a.inverse(), T.CQ_ONE)
        self.assertEqual(a.conj(), T.CQ(Fraction(1, 2), Fraction(3, 4)))
        self.assertEqual(T.CQ(0, 1) * T.CQ(0, 1), T.CQ(-1))
        with self.assertRaises(ZeroDivisionError):
            T.CQ_ZERO.inverse()

    def test_matrix_rank_and_products(self):
        eye = T.mat_eye(4)
        self.assertEqual(T.mat_rank(eye), 4)
        self.assertEqual(T.mat_rank(T.mat_zero(4)), 0)
        m = T.mat_from_ints([[1, 2], [2, 4]])
        self.assertEqual(T.mat_rank(m), 1)
        self.assertTrue(T.mat_eq(T.mat_mul(m, T.mat_eye(2)), m))


class AlgebraTests(unittest.TestCase):

    def test_contract_construction_matches_fixture_and_clifford(self):
        facts = algebra().basic_facts()
        self.assertTrue(facts["fixtureAgreement"])
        self.assertTrue(all(facts[k] for k in ("clifford", "C_squared_one", "Cgamma_antisymmetric", "B_hermitian",
                                                "B_squared_one", "B_commutes_C", "BC_is_minus_i_gamma4")))
        self.assertEqual(facts["chirality_diag"], [-1] * 8 + [1] * 8)

    def test_fixture_mismatch_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "fixture.json")
            with open(T.DEFAULT_FIXTURE, "r", encoding="utf-8") as handle:
                fx = json.load(handle)
            fx["gamma"][3][0] = [-v for v in fx["gamma"][3][0]]
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(fx, handle)
            self.assertFalse(T.Algebra(path).fixture_agreement)


class GeometryTests(unittest.TestCase):

    def test_geometry_family(self):
        rec = T.check_geometry(algebra())
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(rec.measurements["requiredSource"]["rho_req"], "-21*H**2/kappa")
        self.assertEqual(rec.measurements["israelStress"]["S^i_j (x1,x2,x3,x4,x5,x6,x7)"][3], "-12*H/kappa")

    def test_curvature_of_a_wrong_warp_differs(self):
        coords = [T.Y] + list(sp.symbols("x1 x2 x3 x4 x5 x6 x7", real=True))
        cur = T.diagonal_curvature(T.warped_diagonal(sp.exp(2 * T.H * T.Y)), coords)
        self.assertNotEqual(sp.simplify(cur["scalar"] + 42 * T.H ** 2), 0)


class ReductionTests(unittest.TestCase):

    def test_block_reduction_family(self):
        rec, red, forms = reduction_run()
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(rec.measurements["algebraDim8"], 8)
        self.assertEqual(rec.measurements["commutantDims"]["commutant_A0A1A4"], 32)
        self.assertEqual(rec.measurements["basisUnitary"]["seedColumns"], [4, 0, 0, 4, 0, 4, 4, 0])

    def test_block_forms_are_the_pauli_combinations(self):
        red = reduction()
        for b in red.blocks:
            expected = T.pauli_combination(b["j"], b["s2"], b["s3"])
            self.assertTrue(T.mat_eq(red.block_of(algebra().A4, b), expected["A4"]))
            self.assertTrue(T.mat_eq(red.block_of(algebra().BC, b), expected["BC"]))
            self.assertTrue(T.mat_eq(red.block_of(algebra().B, b), expected["B"]))

    def test_negative_control_wrong_generator_breaks_block_form(self):
        red = reduction()
        wrong = T.mat_mul(algebra().gamma[2], algebra().gamma[0])
        self.assertFalse(all(T.mat_is_zero(red.cross_block(wrong, b1, b2))
                             for b1 in red.blocks for b2 in red.blocks if b1 is not b2))

    def test_block_ode_and_hamiltonian(self):
        N = T.block_ode_matrix(j=1)
        self.assertEqual(sp.simplify(N - (T.MM * T.SIG3 - T.KAPPA_Y * T.KK * T.SIG2 + sp.I * (T.EPS - T.VV) * T.SIG1)),
                         sp.zeros(2))
        c1, c2 = sp.symbols("c1 c2")
        chi = sp.Matrix([c1, c2])
        h = T.block_hamiltonian_apply(chi, N * chi, j=1)
        self.assertEqual(sp.simplify(h - T.EPS * chi), sp.zeros(2, 1))
        wrong = T.block_hamiltonian_apply(chi, N * chi, j=-1)
        self.assertNotEqual(sp.simplify(wrong - T.EPS * chi), sp.zeros(2, 1))


class BoundaryTests(unittest.TestCase):

    def test_boundary_family(self):
        rec = T.check_boundary(algebra(), reduction())
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(rec.measurements["densityParities"]["s"], {"P_A": "odd", "P_B": "even"})

    def test_negative_control_wrong_current_matrix(self):
        alg = algebra()
        wrong = T.mat_mul(alg.gamma[0], alg.gamma[1])       # A1 instead of A4
        N16 = T.mat_to_sympy(alg.A0) * T.MM + sp.I * T.EPS * T.mat_to_sympy(alg.A4)
        W = T.mat_to_sympy(wrong)
        self.assertNotEqual(sp.expand(N16.H * W + W * N16), sp.zeros(16))


class ExchangeTests(unittest.TestCase):

    def test_exchange_algebra_family(self):
        rec = T.Recorder("exchange")
        T.check_exchange_a(algebra(), reduction(), rec)
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(rec.measurements["filledShellOneEighth"]["ratio"], "1/8")

    def test_wick_theorem_detects_a_wrong_sign(self):
        ok, detail = T.hartree_fock_wick(algebra(), reduction())
        self.assertTrue(ok)
        two = [c for c in detail["cases"] if c["occupied"] == [0, 1]][0]
        self.assertEqual(two["<:S^2:>"], ["-2", "0"])
        self.assertNotEqual(two["<:S^2:>"], two["Tr(BC rho BC rho)"])   # the exchange term enters with a minus sign

    def test_kernel_table_and_wrong_kernel(self):
        table, h_form, _ = T.exchange_kernel_table(algebra())
        self.assertTrue(h_form)
        self.assertEqual(table[0][0], T.CQ(16))
        self.assertEqual(table[1][1], T.CQ(-16))
        self.assertNotEqual(table[1][1], T.CQ(16))

    def test_t0_closed_forms_and_gas_quadrature(self):
        forms = T.t0_closed_forms()
        kf = sp.Symbol("k_F", positive=True)
        self.assertEqual(sp.simplify(forms[4]["n"] - kf ** 4 / (4 * sp.pi ** 2)), 0)
        with mpmath.workdps(20):
            mu = T.gas_mu_of_n(mpmath.mpf(1), mpmath.mpf(0), 1, 4)
            rule = T.GasRule(1, mu, 0, 4, 24)
            mom = rule.moments()
            self.assertLess(abs(mom["n"] - 1), mpmath.mpf(10) ** -15)
            kf_value = (4 * mpmath.pi ** 2) ** mpmath.mpf("0.25")
            s_closed = ((kf_value ** 2 - 2) * mpmath.sqrt(1 + kf_value ** 2) + 2) / (3 * mpmath.pi ** 2)
            self.assertLess(abs(mom["S"] - s_closed), mpmath.mpf(10) ** -15)
            tr = rule.exchange_trace(4)
            closed = (mom["n"] ** 2 + mom["S"] ** 2) / 16
            self.assertLess(abs(tr - closed), mpmath.mpf(10) ** -15)
            self.assertGreater(abs(tr - (mom["n"] ** 2 + mom["S"] ** 2) / 8), mpmath.mpf(10) ** -3)   # wrong closed form

    def test_finite_temperature_point_and_float_double_sum(self):
        with mpmath.workdps(20):
            mu = T.gas_mu_of_n(mpmath.mpf("0.3"), mpmath.mpf("0.2"), 1, 3)
            rule = T.GasRule(1, mu, mpmath.mpf("0.2"), 3, 16)
            mom = rule.moments()
            self.assertLess(abs(mom["n"] - mpmath.mpf("0.3")), mpmath.mpf(10) ** -9)
            closed = float((mom["n"] ** 2 + mom["S"] ** 2) / 16)
            tr_float = T.exchange_trace_float(rule, 3, 4)
            self.assertLess(abs(tr_float - closed), 1e-12 * closed)
        row = T.table_row("0.5", "0.3", 4)
        self.assertLess(row["relativeDeviationFromClosedForm"], 1e-12)
        self.assertAlmostEqual(row["vvOverLambda"], -0.5 / 16)


class FunctionalAndEmtTests(unittest.TestCase):

    def test_functional_family(self):
        rec = T.check_functional()
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})

    def test_emt_family_and_negative_control(self):
        rec, own = emt_run()
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(rec.measurements["rho"], {"n": "eps - vv", "s": "-M + m", "t": "0", "c": "0"})
        self.assertEqual(sp.simplify(own["Ty1"] - T.KK), 0)
        coeffs, exact = T.sesquilinear_coefficients(T.SIG2 + 3 * T.I2, 1)
        self.assertTrue(exact)
        self.assertEqual((coeffs["n"], coeffs["s"]), (3, 1))
        coeffs_minus, _ = T.sesquilinear_coefficients(T.SIG2 + 3 * T.I2, -1)
        self.assertEqual(coeffs_minus["s"], -1)


class WolframComparisonTests(unittest.TestCase):

    def test_inputform_translation(self):
        LL, a4c, Hs, Ms = sp.symbols("LL a4c H M", positive=True)
        expr = T._inputform_to_sympy("(-2*(-1 + E^(LL*(H - 2*M)))*M)/(E^a4c*(-1 + E^(-2*LL*M))*(H - 2*M))",
                                     {"LL": LL, "a4c": a4c, "H": Hs, "M": Ms, "E": sp.E})
        self.assertEqual(sp.simplify(expr.subs({LL: 2, a4c: 0, Hs: 1, Ms: 3}) - (6 * (1 - sp.exp(-10)) / (5 * (1 - sp.exp(-12))))), 0)

    def test_agreement_with_committed_theory_file_when_present(self):
        if not os.path.exists(T.DEFAULT_THEORY):
            self.skipTest("kohn-sham-theory.json not present")
        rec, red, forms = reduction_run()
        emt_rec, own = emt_run()
        own = dict(own, cValue=rec.measurements["zeroModeSplittingSympy"])
        wrec = T.check_wolfram_agreement(algebra(), red, forms, T.DEFAULT_THEORY, own)
        self.assertTrue(wrec.ok(), {k: v for k, v in wrec.checks.items() if not v})

    def test_wrong_basis_in_theory_file_is_detected(self):
        if not os.path.exists(T.DEFAULT_THEORY):
            self.skipTest("kohn-sham-theory.json not present")
        with open(T.DEFAULT_THEORY, "r", encoding="utf-8") as handle:
            th = json.load(handle)
        th["reduction"]["blockDiagonalisation"]["blocks"][0]["A4"] = [[["0", "0"], ["-1", "0"]], [["-1", "0"], ["0", "0"]]]
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "theory.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(th, handle)
            rec, red, forms = reduction_run()
            emt_rec, own = emt_run()
            own = dict(own, cValue=rec.measurements["zeroModeSplittingSympy"])
            wrec = T.check_wolfram_agreement(algebra(), red, forms, path, own)
        self.assertFalse(wrec.checks["KS_wolfram_blockMatricesIdentical"])


class ReportTests(unittest.TestCase):

    def test_SLOW_main_quick_mode_writes_deterministic_lf_report_and_table(self):
        if os.environ.get("D16C_FAST") == "1":
            self.skipTest("D16C_FAST=1")
        with tempfile.TemporaryDirectory() as directory:
            output = os.path.join(directory, "report.json")
            table = os.path.join(directory, "table.json")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = T.main(["--output", output, "--table", table, "--quick"])
            self.assertEqual(code, 0, buffer.getvalue()[-3000:])
            with open(output, "rb") as handle:
                first = handle.read()
            with open(table, "rb") as handle:
                table_bytes = handle.read()
            with contextlib.redirect_stdout(io.StringIO()):
                T.main(["--output", output, "--table", table, "--quick"])
            with open(output, "rb") as handle:
                second = handle.read()
            with open(table, "rb") as handle:
                table_second = handle.read()
        self.assertEqual(first, second)
        self.assertEqual(table_bytes, table_second)
        self.assertNotIn(b"\r\n", first)
        self.assertTrue(first.endswith(b"\n"))
        report = json.loads(first.decode("utf-8"))
        self.assertEqual(report["schemaVersion"], 1)
        self.assertTrue(all(report["checks"][T.FAMILY_CHECKS[f]] for f in T.FAMILIES))
        self.assertIn("scripts/check_dirac16complex_kohn_sham_theory.py", report["sourceSha256"])
        lines = buffer.getvalue().splitlines()
        self.assertIn("failed_check_count=0", lines)
        self.assertTrue(any(line.startswith("check_count=") for line in lines))
        doc = json.loads(table_bytes.decode("utf-8"))
        self.assertEqual(doc["primary"], "d4")
        self.assertLess(doc["maxRelativeDeviationFromClosedForm"], 1e-9)

    def test_SLOW_missing_theory_file_records_not_run(self):
        if os.environ.get("D16C_FAST") == "1":
            self.skipTest("D16C_FAST=1")
        with tempfile.TemporaryDirectory() as directory:
            output = os.path.join(directory, "report.json")
            missing = os.path.join(directory, "absent-theory.json")
            with contextlib.redirect_stdout(io.StringIO()):
                code = T.main(["--output", output, "--theory", missing, "--no-table", "--families", "geometry,boundary"])
            with open(output, "rb") as handle:
                report = json.loads(handle.read().decode("utf-8"))
        self.assertEqual(code, 0)
        self.assertEqual(report["measurements"]["wolframAgreement"], "not-run")
        self.assertNotIn(T.WOLFRAM_CHECK, report["checks"])


if __name__ == "__main__":
    unittest.main()
