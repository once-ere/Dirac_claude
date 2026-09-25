"""Unit tests for the independent primordial-field checker (sympy + stdlib).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_primordial.py" -v
The tests call the check functions directly (one shared Context), include
negative controls so that no check can pass vacuously, and write only into
tempfile directories.  ReportTests.test_default_invocation_compares_with_the_
wolfram_components reads the committed Wolfram component file
artifacts/dirac16complex/primordial-field/primordial-components.json (the Stage-2
gate writes it first with scripts/verify_dirac16complex_primordial.wls).
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from fractions import Fraction

try:
    from scripts import check_dirac16complex_primordial as P
except ModuleNotFoundError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                    "scripts"))
    import check_dirac16complex_primordial as P

import sympy as sp

_CTX = None


def context():
    global _CTX
    if _CTX is None:
        _CTX = P.Context()
    return _CTX


class ExactScalarTests(unittest.TestCase):

    def test_zero_test_uses_the_trig_relation_and_detects_nonzero(self):
        self.assertTrue(P.is_zero(P.CZ ** 2 + P.W ** 12 - 1))
        self.assertTrue(P.is_zero((P.CZ ** 2 - 1) / P.W ** 6 + P.W ** 6))
        self.assertFalse(P.is_zero(P.CZ - 1))
        self.assertFalse(P.is_zero(P.CZ ** 2 + P.W ** 12))
        self.assertFalse(P.is_zero(P.EA * P.A1 - P.A1))

    def test_canonical_substitutions(self):
        z = P.ZARG
        self.assertTrue(P.equal(P.canon_x(sp.sin(z) ** sp.Rational(1, 3)), P.W ** 2))
        self.assertTrue(P.equal(P.canon_x(sp.cot(z) ** 2), P.CZ ** 2 / P.W ** 12))
        derivative = sp.diff(sp.exp(2 * P.FX4), P.X4, 2)
        self.assertTrue(P.equal(P.canon_x(derivative),
                                P.EA ** 2 * (4 * P.H ** 2 * P.A1 ** 2 + 2 * P.H ** 2 * P.A2)))
        self.assertTrue(P.equal(P.canon_r(sp.exp(-P.H * P.ZETA - P.A4R)), 1 / (P.W * P.EA)))

    def test_derivations_match_sympy_differentiation(self):
        z = P.ZARG
        expression = sp.cos(z) ** 3 * sp.sin(z) ** sp.Rational(-5, 6) * sp.exp(-P.FX4)
        self.assertTrue(P.equal(P.d0(P.canon_x(expression)),
                                P.canon_x(sp.diff(expression, P.X0))))
        expression = sp.exp(3 * P.FX4) * sp.diff(P.FX4, P.X4)
        self.assertTrue(P.equal(P.d4(P.canon_x(expression)),
                                P.canon_x(sp.diff(expression, P.X4))))


class SampleRingTests(unittest.TestCase):

    def test_radical_and_transcendental_arithmetic(self):
        s0 = Fraction(3, 5)
        r = P.QRE({(1, 0, 0): Fraction(1)}, s0)
        e = P.QRE({(0, 1, 0): Fraction(1)}, s0)
        i = P.QRE({(0, 0, 1): Fraction(1)}, s0)
        power = P.QRE.const(1, s0)
        for _ in range(6):
            power = power * r
        self.assertTrue((power - s0).is_zero())
        self.assertTrue((i * i + 1).is_zero())
        self.assertTrue((r * r.inverse() - 1).is_zero())
        self.assertTrue((e * e.inverse() - 1).is_zero())
        self.assertFalse((r * r - s0).is_zero())
        self.assertTrue(((r + i * e).conj() - (r - i * e)).is_zero())
        with self.assertRaises(ValueError):
            (r + e).inverse()

    def test_evaluator_matches_direct_arithmetic(self):
        env, s0 = P.sample_environment(P.SAMPLE_POINTS[0])
        value = P.to_qre(P.W ** 7 * P.CZ / P.EA - 3 * P.H * sp.I, env, s0)
        expected = (P.QRE({(1, -1, 0): s0 * Fraction(4, 5)}, s0)
                    - P.QRE({(0, 0, 1): Fraction(3)}, s0))
        self.assertTrue((value - expected).is_zero())


class AlgebraTests(unittest.TestCase):

    def test_setup_and_fixture(self):
        ok, measurements = P.check_algebra_setup(context())
        self.assertTrue(ok, measurements)
        self.assertEqual(measurements["P_algebraSetup"]["chiralityDiagonal"],
                         [-1] * 8 + [1] * 8)

    def test_blade_algebra(self):
        for a in range(8):
            for b in range(8):
                anti = P.cl_anti(P.gamma_blade(a), P.gamma_blade(b))
                expected = {0: 2 * P.ETA[a]} if a == b else {}
                self.assertTrue(P.cl_equal(anti, expected))
        charge = P.cl(P.CHARGE_MASK, 1)
        self.assertTrue(P.cl_equal(P.cl_mul(charge, charge), {0: 1}))

    def test_fixture_mismatch_is_detected(self):
        ctx = context()
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "fixture.json")
            gammas = [[row[:] for row in g] for g in ctx.gamma]
            gammas[3][0] = [-v for v in gammas[3][0]]
            with open(path, "w", encoding="utf-8") as handle:
                json.dump({"gamma": gammas, "C": ctx.charge}, handle)
            ok, measurements = P.check_algebra_setup(ctx, path)
        self.assertFalse(ok)
        self.assertFalse(measurements["P_algebraSetup"]["fixtureAgreement"])


class GeometryTests(unittest.TestCase):

    def test_metric_and_zeta(self):
        ok, measurements = P.check_metric(context())
        self.assertTrue(ok, measurements)
        self.assertEqual(measurements["P_metric"]["signature"], [4, 4])
        self.assertEqual(measurements["P_metric"]["sqrtAbsDetG"], "cos(z)")
        ok, measurements = P.check_zeta(context())
        self.assertTrue(ok, measurements)

    def test_christoffel_and_spin_connection(self):
        ok, measurements = P.check_christoffel(context())
        self.assertTrue(ok)
        self.assertEqual(measurements["P_christoffel"]["nonzeroOrderedCount"], 37)
        self.assertEqual(measurements["P_christoffel"]["nonzeroIndependentCount"], 25)
        ok, measurements = P.check_spinconn(context())
        self.assertTrue(ok)
        self.assertEqual(measurements["P_spinconn"]["nonzeroCount"], 24)
        self.assertEqual(measurements["P_spinconn"]["vielbeinPostulateZeroComponents"], 512)

    def test_wrong_closed_form_is_rejected(self):
        closed = P.closed_christoffel()
        ctx = context()
        self.assertTrue(P.equal(ctx.Gamma[0][1][1], P.canon_r(closed[(0, 1, 1)])))
        self.assertFalse(P.equal(ctx.Gamma[0][1][1], P.canon_r(-closed[(0, 1, 1)])))
        self.assertFalse(P.equal(ctx.Gamma[4][5][5], P.canon_r(closed[(4, 1, 1)])))

    def test_omega_and_gamma_constancy(self):
        ok, measurements = P.check_omega(context())
        self.assertTrue(ok)
        self.assertEqual(measurements["P_Omega"]["gammaMuOmegaMu"], "3*H*g0")
        ok, measurements = P.check_gamma_const(context())
        self.assertTrue(ok)
        self.assertEqual(measurements["P_gammaConst"]["correctContractionZeroPairs"], 64)
        self.assertEqual(measurements["P_gammaConst"]["notebookContractionNonzeroPairs"], 15)

    def test_gamma_constancy_detects_a_perturbed_connection(self):
        ctx = context()
        perturbed = P.cl_add(ctx.Omega[1], P.cl_scale(P.cl_mul(P.gamma_blade(1), P.gamma_blade(4)),
                                                       P.H))
        base = P.cl_add(P.cl_d_gamma_derivative(ctx, 1, 4),
                        *[P.cl_scale(ctx.gamma_up[lam], ctx.Gamma[4][1][lam]) for lam in range(8)
                          if ctx.Gamma[4][1][lam] != 0])
        self.assertTrue(P.cl_is_zero(P.cl_add(base, P.cl_comm(ctx.Omega[1], ctx.gamma_up[4]))))
        self.assertFalse(P.cl_is_zero(P.cl_add(base, P.cl_comm(perturbed, ctx.gamma_up[4]))))

    def test_einstein_and_notebook_cell_584(self):
        ok, measurements, _ = P.check_einstein(context())
        self.assertTrue(ok, measurements)
        nb = measurements["P_einstein"]["notebookCell584"]
        self.assertTrue(nb["covariantAgrees"])
        self.assertTrue(nb["ricciScalarCell583Agrees"])

    def test_source_x0_independent_state_supplies_linear_a4_exactly(self):
        ok, measurements = P.check_source(context())
        self.assertTrue(ok, measurements)
        source = measurements["P_source"]
        self.assertTrue(source["einsteinTransverseDifferenceIs2H2a4pp"])
        self.assertTrue(source["realKRho_times_sinz_x0Independent"])
        self.assertTrue(source["x0Independent"]["offDiagonalAre15ThreeGammaBilinears"])
        self.assertEqual(len(source["x0Independent"]["offDiagonal"]), 21)
        for label, rho, p in (("A", "-36", "0"), ("B", "-24", "12")):
            example = source["x0IndependentExamples"][label]
            self.assertTrue(example["allGminusKappaT64Zero"])
            self.assertTrue(example["negativeControlSlopePlus1Fails"])
            self.assertEqual((example["rho"], example["pTransverse"]), (rho, p))

    def test_source_rejects_a_wrong_example(self):
        original = P.SOURCE_EXAMPLES
        try:
            wrong = dict(original[1])
            wrong["m"] = wrong["m"] + 1          # m S != -36 H^2/kappa
            wrong["Meff"] = wrong["Meff"] + 1
            P.SOURCE_EXAMPLES = (original[0], wrong)
            ok, measurements = P.check_source(context())
        finally:
            P.SOURCE_EXAMPLES = original
        self.assertFalse(ok)
        self.assertFalse(measurements["P_source"]["x0IndependentExamples"]["B"]["conditions"])

    def test_a4_linear_numbers(self):
        ok, measurements = P.check_a4linear(context())
        self.assertTrue(ok)
        row = measurements["P_a4linear"]["table"][0]
        self.assertEqual(row["R"], "-36*H**2")
        self.assertEqual(row["rho_req"], "-24*H**2/kappa")
        self.assertEqual(row["w_req"], "-1/2")


class FieldEquationTests(unittest.TestCase):

    def test_euler_lagrange_components(self):
        ok, measurements, tables = P.check_el(context())
        self.assertTrue(ok, measurements)
        self.assertEqual(len(tables["table"]), 16)
        self.assertTrue(all(len(row) == 9 for row in tables["table"]))

    def test_blocks_agree_with_notebook(self):
        ok, measurements = P.check_blocks(context())
        self.assertTrue(ok)
        self.assertEqual(measurements["P_blocks"]["blocks"],
                         [[0, 5, 8, 13], [1, 4, 9, 12], [2, 7, 10, 15], [3, 6, 11, 14]])

    def test_notebook_cell1137_equals_correct_equations_plus_q_terms(self):
        result = P.compare_notebook_cell1137(context())
        self.assertEqual(result["equationsParsed"], 16)
        self.assertTrue(result["linearPartAgreesWithCorrectEquations"])
        self.assertEqual(result["residualIsPlusMinus_q_yZj"],
                         [1, -1, -1, 1, 1, -1, -1, 1] + [0] * 8)

    def test_emt_modes_quantization(self):
        ok, measurements = P.check_emt(context())
        self.assertTrue(ok)
        zeta = measurements["P_EMT"]["zetaWave"]
        self.assertTrue(zeta["rhoFrozenInX4"])
        self.assertTrue(all(zeta["conservationPerNu"]))
        self.assertEqual(measurements["P_EMT"]["anticommutatorNonzeroCount"], 21)
        ok, measurements = P.check_modes(context())
        self.assertTrue(ok)
        ok, measurements = P.check_quant(context())
        self.assertTrue(ok)

    def test_p0_is_not_frozen_for_nonzero_k(self):
        data = P.emt_zeta_wave(context())
        charge = P.cl(P.CHARGE_MASK, sp.Integer(1))
        q_p0 = P.cl_scale(P.cl_mul(charge, P.gamma_blade(0)), -sp.I * P.KZ * data["f2"])
        rate = P.cl_add(P.cl_mul(data["Adag"], q_p0), P.cl_mul(q_p0, data["A"]))
        self.assertFalse(P.cl_is_zero(rate))
        self.assertTrue(P.cl_is_zero({k: v.subs(P.KZ, 0) for k, v in rate.items()}))


class WolframComparisonTests(unittest.TestCase):

    def _write_components(self, directory, table, perturb=False):
        equations = []
        for a, row in enumerate(table):
            terms = []
            for coefficient, mu, b in row:
                text = sp.mathematica_code(coefficient)
                if perturb and a == 3 and mu == 5:
                    text = "2*(" + text + ")"
                terms.append({"coefficient": text, "derivative": mu, "component": b})
            terms.append({"coefficient": "-(m + lam*S)", "derivative": None, "component": a})
            equations.append({"component": a, "terms": terms})
        path = os.path.join(directory, "primordial-components.json")
        with open(path, "w", encoding="utf-8") as handle:
            json.dump({"equations": equations}, handle)
        return path

    def test_synthetic_components_agree_and_perturbation_is_caught(self):
        ctx = context()
        _, _, tables = P.check_el(ctx, sample=False)
        with tempfile.TemporaryDirectory() as directory:
            path = self._write_components(directory, tables["table"])
            ok, measurements = P.check_wolfram_agreement(ctx, path, tables["table"])
            self.assertTrue(ok, measurements)
            path = self._write_components(directory, tables["table"], perturb=True)
            ok, measurements = P.check_wolfram_agreement(ctx, path, tables["table"])
            self.assertFalse(ok)
            self.assertTrue(measurements["wolframMismatches"])

    @staticmethod
    def _python_text(expression):
        a4 = sp.Symbol("a4")
        e = sp.sympify(expression).subs(sp.Derivative(P.A4R, P.TS), sp.Symbol("a4p"))
        e = e.subs(P.A4R, a4).subs(P.MASS, sp.Symbol("m"))
        return sp.sstr(e)

    def _nested_record(self, coefficient, mu, b):
        wl = sp.mathematica_code(sp.sympify(coefficient).subs(P.MASS, sp.Symbol("mm"))
                                 .subs(P.SSYM, sp.Symbol("SS")))
        return {"component": b, "derivative": "none" if mu in (None, "mass") else mu,
                "coefficient": {"tex": "unused", "py": self._python_text(coefficient), "wl": wl}}

    def test_nested_wolfram_layout_with_both_printers_and_evolution(self):
        ctx = context()
        _, _, tables = P.check_el(ctx, sample=False)
        mass = -(P.MASS + P.LAM * P.SSYM)

        def document(perturb):
            equations = []
            for n in range(16):
                terms = [self._nested_record(c, mu, b) for c, mu, b in tables["table"][n]]
                terms.append(self._nested_record(mass, None, n))
                evolution = [self._nested_record(c, mu, b) for c, mu, b in tables["evolution"][n]]
                if perturb and n == 7:
                    evolution[0]["coefficient"]["py"] = "2*(" + evolution[0]["coefficient"]["py"] + ")"
                equations.append({"n": n, "terms": terms, "evolution": {"terms": evolution}})
            return {"eulerLagrange": {"equations": equations}}

        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "primordial-components.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(document(False), handle)
            ok, measurements = P.check_wolfram_agreement(ctx, path, tables["table"],
                                                         tables["evolution"])
            self.assertTrue(ok, measurements)
            self.assertEqual(measurements["wolframPrintersCompared"], ["py", "wl"])
            self.assertEqual(measurements["wolframFormsCompared"], ["terms", "evolution"])
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(document(True), handle)
            ok, measurements = P.check_wolfram_agreement(ctx, path, tables["table"],
                                                         tables["evolution"])
            self.assertFalse(ok)
            self.assertTrue(all("evolution py row 7" in m for m in measurements["wolframMismatches"]))


class ReportTests(unittest.TestCase):

    def test_main_writes_deterministic_lf_report(self):
        with tempfile.TemporaryDirectory() as directory:
            output = os.path.join(directory, "report.json")
            missing = os.path.join(directory, "absent-components.json")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = P.main(["--output", output, "--wolfram-components", missing,
                               "--allow-missing-wolfram"])
            self.assertEqual(code, 0, buffer.getvalue()[-2000:])
            with open(output, "rb") as handle:
                first = handle.read()
            with contextlib.redirect_stdout(io.StringIO()):
                P.main(["--output", output, "--wolfram-components", missing,
                        "--allow-missing-wolfram"])
            with open(output, "rb") as handle:
                second = handle.read()
        self.assertEqual(first, second)
        self.assertNotIn(b"\r\n", first)
        self.assertTrue(first.endswith(b"\n"))
        report = json.loads(first.decode("utf-8"))
        self.assertEqual(report["schemaVersion"], 1)
        self.assertEqual(list(report["checks"]), list(P.CHECK_NAMES))
        self.assertTrue(all(report["checks"].values()))
        self.assertEqual(report["measurements"]["wolframAgreement"], "not-run")
        self.assertIn("scripts/check_dirac16complex_primordial.py", report["sourceSha256"])
        lines = buffer.getvalue().splitlines()
        self.assertIn("check_count=%d" % len(P.CHECK_NAMES), lines)
        self.assertIn("failed_check_count=0", lines)

    def test_missing_wolfram_components_fail_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            output = os.path.join(directory, "report.json")
            missing = os.path.join(directory, "absent-components.json")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = P.main(["--output", output, "--wolfram-components", missing])
            with open(output, "rb") as handle:
                report = json.loads(handle.read().decode("utf-8"))
        self.assertEqual(code, 1, buffer.getvalue()[-2000:])
        self.assertEqual(list(report["checks"]), list(P.CHECK_NAMES) + [P.WOLFRAM_CHECK])
        self.assertFalse(report["checks"][P.WOLFRAM_CHECK])
        self.assertTrue(all(report["checks"][name] for name in P.CHECK_NAMES))
        self.assertEqual(report["measurements"]["wolframAgreement"], "missing")
        lines = buffer.getvalue().splitlines()
        self.assertIn("failed_check_count=1", lines)
        self.assertTrue(any(line.startswith("error=missing Wolfram component file")
                            for line in lines))

    def test_default_invocation_compares_with_the_wolfram_components(self):
        # The default --wolfram-components path is the file the Wolfram verifier
        # writes; the gate runs that verifier first, so the default invocation must
        # find it, run P_EL_agreesWithWolfram and record wolframAgreement=compared.
        self.assertTrue(os.path.isfile(P.DEFAULT_WOLFRAM_COMPONENTS),
                        "run wolframscript -file scripts/verify_dirac16complex_primordial.wls "
                        "first: %s is missing" % P.DEFAULT_WOLFRAM_COMPONENTS)
        with tempfile.TemporaryDirectory() as directory:
            output = os.path.join(directory, "report.json")
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = P.main(["--output", output])
            with open(output, "rb") as handle:
                report = json.loads(handle.read().decode("utf-8"))
        self.assertEqual(code, 0, buffer.getvalue()[-2000:])
        self.assertEqual(list(report["checks"]), list(P.CHECK_NAMES) + [P.WOLFRAM_CHECK])
        self.assertTrue(all(report["checks"].values()))
        measurements = report["measurements"]
        self.assertEqual(measurements["wolframAgreement"], "compared")
        self.assertEqual(measurements["P_EL_wolfram"]["wolframMismatchCount"], 0)
        self.assertEqual(measurements["P_EL_wolfram"]["wolframPrintersCompared"], ["py", "wl"])
        self.assertEqual(measurements["P_EL_wolfram"]["wolframFormsCompared"],
                         ["terms", "evolution"])
        self.assertTrue(all(count > 0 for count in
                            measurements["P_EL_wolfram"]["wolframCoefficientsCompared"].values()))
        self.assertIn("artifacts/dirac16complex/primordial-field/primordial-components.json",
                      report["inputSha256"])
        lines = buffer.getvalue().splitlines()
        self.assertIn("measurement_wolframAgreement=compared", lines)
        self.assertIn("check_%s=true" % P.WOLFRAM_CHECK, lines)


if __name__ == "__main__":
    unittest.main()
