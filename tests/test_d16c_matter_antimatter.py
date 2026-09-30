"""Unit tests for the independent matter-antimatter checker (sympy + stdlib + grassmann_algebra).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_matter_antimatter.py" -v
The fast subset (every test except the one tagged SLOW in its name) runs in well under a
minute: it calls the check functions directly on a shared Algebra and one shared curved
geometry, includes negative controls (a U(1)-breaking term, the notebook spin-connection
contraction, a wrong Pin element, a wrong statistics sign) and writes only into tempfile
directories.  The SLOW test runs the command-line entry point and is skipped when the
environment variable D16C_FAST=1 is set.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
import check_dirac16complex_matter_antimatter as MA  # noqa: E402
from grassmann_algebra import Grassmann, JetSpace  # noqa: E402

_ALG = None
_GEO = None


def algebra():
    global _ALG
    if _ALG is None:
        _ALG = MA.Algebra(MA.DEFAULT_FIXTURE)
    return _ALG


def curved():
    global _GEO
    if _GEO is None:
        _GEO = MA.geometry_generic(algebra())
    return _GEO


class ExactToolsTests(unittest.TestCase):

    def test_permutation_signature(self):
        self.assertEqual(MA.permutation_signature((1, 2, 3, 4)), 1)
        self.assertEqual(MA.permutation_signature((2, 1, 3, 4)), -1)
        self.assertEqual(MA.permutation_signature((1, 1, 3, 4)), 0)

    def test_commuting_polynomials(self):
        x, y = MA.CPoly.gen(0), MA.CPoly.gen(1)
        self.assertTrue(MA.elements_equal(x * y, y * x))
        self.assertEqual((x * x).left_derivative(0), x.scale(2))
        self.assertEqual(((x + y) ** 2).nterms(), 3)
        g0, g1 = Grassmann.gen(0), Grassmann.gen(1)
        self.assertTrue(MA.elements_equal(g0 * g1, -(g1 * g0)))
        self.assertEqual((g0 * g0).nterms(), 0)

    def test_nullspace_and_primitive(self):
        rows = [{0: 1, 1: -1}, {1: 2, 2: -2}]
        basis = MA.exact_nullspace(rows, 3)
        self.assertEqual(len(basis), 1)
        self.assertEqual(MA.primitive_integer(basis[0]), [1, 1, 1])
        self.assertEqual(MA.primitive_integer([Fraction(-1, 2), Fraction(1, 3)]), [3, -2])
        self.assertTrue(MA.proportional([2, 4], [1, 2]))
        self.assertFalse(MA.proportional([2, 5], [1, 2]))

    def test_statistics_sign_of_symmetric_bilinear(self):
        js = JetSpace(["psi", "psis"], max_deriv=0)
        C = algebra().C.tolist()
        for alg, zero in ((Grassmann, True), (MA.CPoly, False)):
            P = MA.gen_list(alg, js.gens("psi"))
            self.assertEqual(MA.form(alg, C, P, P).nterms() == 0, zero)


class AlgebraTests(unittest.TestCase):

    def test_fixture_and_clifford(self):
        alg = algebra()
        self.assertTrue(all(alg.fixture_agreement().values()))
        for a in range(8):
            for b in range(8):
                ac = alg.gam[a] @ alg.gam[b] + alg.gam[b] @ alg.gam[a]
                self.assertTrue(np.array_equal(ac, 2 * MA.ETA[a] * (a == b) * alg.I16))
        self.assertTrue(np.array_equal(alg.g8, np.diag([-1] * 8 + [1] * 8)))
        self.assertTrue(MA.is_symmetric_int(alg.C) and np.array_equal(alg.C @ alg.C, alg.I16))

    def test_divergence_identity_all_first_jets_and_negative_control(self):
        eye = [[int(i == j) for j in range(8)] for i in range(8)]
        good = MA.divergence_identity_all_directions(algebra(), eye)
        self.assertTrue(good["divergenceIdentity"] and good["gammaCovariantlyConstant"] and good["omegaAntisymmetric"])
        bad = MA.divergence_identity_all_directions(algebra(), eye, notebook_contraction=True)
        self.assertFalse(bad["gammaCovariantlyConstant"])

    def test_curved_geometry_consistency(self):
        chk = curved().matrix_checks()
        self.assertTrue(chk["inverseMetric"] and chk["omegaAntisymmetric"] and chk["gammaCovariantlyConstant"]
                        and chk["divergenceIdentity"])
        self.assertGreater(chk["gammaMuOmegaMuNonzeroEntries"], 0)


class M1Tests(unittest.TestCase):

    def test_m1_curved_both_statistics(self):
        rec = MA.check_M1(algebra(), quick=True, geos=[curved()])
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertIn("MA_M1_noetherIdentity_grassmann_G_A_generic_nondiagonal", rec.checks)
        self.assertIn("MA_M1_noetherIdentity_commuting_G_A_generic_nondiagonal", rec.checks)

    def test_u1_breaking_term_is_detected(self):
        """Negative control: a charge-2 term Psi^T C Psi (commuting) is not U(1) invariant."""
        alg = algebra()
        flat = MA.FlatGeometry(alg)
        js = JetSpace(["psi", "psis"], max_deriv=1)
        A = MA.CPoly
        comps = MA.field_components(A, js)
        eye = [[Fraction(int(i == j)) for j in range(16)] for i in range(16)]
        tc = MA.transform_components(A, comps, eye, phase=MA.PHASE)
        L0, _, _ = MA.lagrangian_value(A, flat, comps, MA.MASS, MA.LAMBDA)
        L1, _, _ = MA.lagrangian_value(A, flat, tc, MA.MASS, MA.LAMBDA)
        self.assertTrue(MA.elements_equal(L0, L1))
        brk = MA.form(A, alg.C.tolist(), comps["P"], comps["P"])
        brk1 = MA.form(A, alg.C.tolist(), tc["P"], tc["P"])
        self.assertFalse(MA.elements_equal(L0 + brk, L1 + brk1))


    def test_wrong_statistics_sign_is_detected(self):
        """Negative control: the commuting Psi equation carries the sign -1; +1 must be rejected."""
        flat = MA.FlatGeometry(algebra())
        js = JetSpace(["psi", "psis"], max_deriv=2)
        A = MA.CPoly
        comps = MA.field_components(A, js)
        Ljet, _, _ = MA.lagrangian(A, flat, comps, MA.MASS, MA.LAMBDA, 0, keys=MA.JET_KEYS)
        Epsi = MA.euler_lagrange_fast(A, Ljet, js, "psi")
        _, good = MA.el_targets(A, flat, comps, MA.MASS, MA.LAMBDA, 0, -1)
        _, bad = MA.el_targets(A, flat, comps, MA.MASS, MA.LAMBDA, 0, +1)
        self.assertTrue(all(MA.elements_equal(e, t) for e, t in zip(Epsi, good)))
        self.assertFalse(any(MA.elements_equal(e, t) for e, t in zip(Epsi, bad)))


class M2Tests(unittest.TestCase):

    def test_charge_conjugation_and_internal_maps(self):
        rec, flat, _, table = MA.check_M2(algebra(), geo_curved=curved())
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(table["C0: Psi -> Psi^* | commuting"]["map"], "L_{m,lam} -> +L_{m,lam}")
        self.assertEqual(table["C0: Psi -> Psi^* | commuting"]["chargeSign_q4"], -1)
        self.assertEqual(table["C8: Psi -> gamma8 Psi^* | grassmann"]["map"], "L_{m,lam} -> +L_{-m,lam}")
        self.assertEqual(table["C8: Psi -> gamma8 Psi^* | grassmann"]["chargeSign_q4"], -1)

    def test_matrix_criterion_matches_jets_and_rejects_wrong_element(self):
        alg = algebra()
        flat = MA.FlatGeometry(alg)
        Lam = MA.lam_matrix(MA.diag_signs([1, 2, 3]))
        R = MA.pin_product(alg, [1, 2, 3], with_g8=True)
        for stat in MA.STATISTICS:
            jc = MA.jet_characters(alg, flat, stat, R, Lam, True)
            mc = MA.matrix_characters(alg, R, Lam, True, stat)
            self.assertEqual((jc["sigmaK"], jc["sigmaS"], jc["q"]), (mc["sigmaK"], mc["sigmaS"], mc["q"]))
            self.assertTrue(jc["lagrangianMapVerified"])
        # wrong Pin element for the coordinate map: gamma^0 with the identity map
        self.assertIsNone(MA.matrix_characters(alg, alg.gam[0], MA.lam_matrix([1] * 8), False, "grassmann"))
        jc = MA.jet_characters(alg, flat, "grassmann", alg.gam[0], None, False)
        self.assertEqual(jc["sigmaK"], 0)

    def test_character_table_and_sakharov_second_condition(self):
        rows = MA.enumerate_discrete_group(algebra())
        complete, summary = MA.summarize_discrete_group(rows)
        self.assertTrue(complete)
        self.assertEqual(len(rows), 1024)
        for stat in MA.STATISTICS:
            self.assertEqual(set(summary[stat]["classCounts"].values()), {256})
        self.assertTrue(summary["commuting"]["C_exact"])
        self.assertFalse(summary["grassmann"]["C_exact"])
        self.assertTrue(summary["grassmann"]["C_exactWhen_m_equals_0"])
        self.assertTrue(summary["grassmann"]["CP_exact_improperSpatialReflection"])


class M3Tests(unittest.TestCase):

    def test_invariant_forms_and_survival(self):
        rec, inv = MA.check_M3(algebra(), geo=curved())
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        self.assertEqual(len(inv), 2)
        surv = rec.measurements["derivativeTypeSurvivalCurved"]
        self.assertTrue(surv["grassmann | sqrt|g| Psi^T C gamma^mu D_mu Psi"]["eulerLagrangeIdenticallyZero"])
        self.assertFalse(surv["grassmann | sqrt|g| Psi^T C gamma8 gamma^mu D_mu Psi"]["eulerLagrangeIdenticallyZero"])
        self.assertFalse(surv["commuting | sqrt|g| Psi^T C gamma^mu D_mu Psi"]["eulerLagrangeIdenticallyZero"])

    def test_quartic_examples(self):
        rec = MA.Recorder("M3")
        MA.check_M3_quartic(algebra(), rec, quick=True)
        self.assertTrue(rec.ok())


class M4Tests(unittest.TestCase):

    def test_gamma8_pair_curved_and_krein_modes(self):
        rec = MA.check_M4(algebra(), geo=curved())
        self.assertTrue(rec.ok(), {k: v for k, v in rec.checks.items() if not v})
        sample = rec.measurements["kreinModeFacts"]["samples"][0]
        self.assertEqual(sample["kreinSignatureOnPositiveEnergySpace"], [4, 4])
        self.assertEqual(sample["perQuantum(E, Q, S)"]["imageWithMetricMinusB"][:2], ["-4", "-1"])

    def test_stage5_pairing_absent_is_open(self):
        with tempfile.TemporaryDirectory() as tmp:
            info, inputs = MA.stage5_pairing(os.path.join(tmp, "none.json"), os.path.join(tmp, "none2.json"))
        self.assertTrue(info["status"].startswith("OPEN"))
        self.assertEqual(inputs, {})


class WolframComparatorTests(unittest.TestCase):
    """The comparator logic on a synthetic file in the Wolfram layout (not the real Wolfram output)."""

    def synthetic(self, rows):
        out = []
        for r in rows:
            mono = r["axes"] if not r["gamma8"] else [a for a in range(8) if a not in r["axes"]]
            entry = out[-1] if out and out[-1]["R"] == r["axes"] and out[-1]["monomial"] == mono else None
            if entry is None:
                entry = {"R": r["axes"], "monomial": mono, "maps": {}}
                out.append(entry)
            for stat in MA.STATISTICS:
                mc = r[stat]
                entry["maps"]["%s/%s" % ("antilinear" if r["antilinear"] else "linear", stat)] = {
                    "kappa": mc["sigmaK"], "sigma": mc["sigmaS"], "currentSigns": mc["q"]}
        return {"M2_classificationRows": out, "M2_symmetrySummary": MA.wolfram_summary_from_rows(rows)}

    def test_comparator_accepts_consistent_and_rejects_corrupted(self):
        alg = algebra()
        rows = MA.enumerate_discrete_group(alg)
        theory = self.synthetic(rows)
        own = {"rows": rows, "ccAllOneDimensional": True}
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "theory.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(theory, handle)
            ok, rec = MA.check_wolfram_agreement(alg, path, own)
            self.assertTrue(ok, rec.measurements)
            self.assertIn("M2_classificationRows", rec.measurements["comparedItems"])
            theory["M2_classificationRows"][7]["maps"]["antilinear/grassmann"]["kappa"] *= -1
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(theory, handle)
            ok, rec = MA.check_wolfram_agreement(alg, path, own)
            self.assertFalse(ok)
            with open(path, "w", encoding="utf-8") as handle:
                json.dump({"unrelated": 1}, handle)
            ok, rec = MA.check_wolfram_agreement(alg, path, own)
            self.assertFalse(ok)                     # nothing comparable is not agreement


class ReportTests(unittest.TestCase):

    def test_report_schema_honesty_and_determinism(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = os.path.join(tmp, "no-theory.json")
            checks, meas, inputs, _ = MA.run_checks(theory_path=missing, families=["M4"], quick=True)
            self.assertTrue(all(checks.values()), {k: v for k, v in checks.items() if not v})
            self.assertEqual(meas["wolframAgreement"], "not-run")
            self.assertNotIn(MA.WOLFRAM_CHECK, checks)
            self.assertTrue(meas["honestAnswer"].startswith("NOT PROVED"))
            for h in ("H1", "H2", "H3"):
                self.assertIn("HYPOTHESIS", meas["M5_conditionalScenario"]["hypotheses"][h])
            report = MA.build_report(checks, meas, inputs)
            self.assertEqual(set(report), {"schemaVersion", "producer", "checks", "measurements", "sourceSha256",
                                           "inputSha256"})
            b1 = MA.canonical_json_bytes(report)
            b2 = MA.canonical_json_bytes(MA.build_report(checks, meas, inputs))
            self.assertEqual(b1, b2)
            self.assertNotIn(b"\r\n", b1)
            lines, failed = MA.report_lines(report)
            self.assertEqual(failed, 0)
            self.assertTrue(lines[-1].startswith("failed_check_count="))

    @unittest.skipIf(os.environ.get("D16C_FAST") == "1", "slow command-line run")
    def test_SLOW_command_line_full_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "report.json")
            proc = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "check_dirac16complex_matter_antimatter.py"),
                                   "--output", out], capture_output=True, text=True, cwd=REPO)
            self.assertEqual(proc.returncode, 0, proc.stdout[-2000:] + proc.stderr[-2000:])
            self.assertIn("failed_check_count=0", proc.stdout)
            with open(out, "r", encoding="utf-8") as handle:
                report = json.load(handle)
            self.assertEqual(report["schemaVersion"], 1)
            self.assertTrue(all(report["checks"].values()))


if __name__ == "__main__":
    unittest.main()
