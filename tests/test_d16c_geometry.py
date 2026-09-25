#!/usr/bin/env python3
"""Fast unittest subset (< 60 s) of the exact Python geometry and Grassmann verifiers.

Run:  python -m unittest discover -s tests -p "test_d16c_geometry.py" -v
The full verifiers are scripts/check_dirac16complex_geometry.py and
scripts/demo_grassmann_lagrangians.py.
"""

from __future__ import annotations

import random
import sys
import unittest
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import d16c_geometry_sympy as G  # noqa: E402
import grassmann_algebra as GA  # noqa: E402
import check_dirac16complex_geometry as CK  # noqa: E402
import demo_grassmann_lagrangians as DM  # noqa: E402


class TestGammaAlgebra(unittest.TestCase):
    def test_notebook_gamma_facts(self):
        dom = G.make_qq_domain()
        gd = G.GammaData(dom)
        rec = CK.Recorder()
        CK.run_algebra(rec, gd, dom)
        self.assertTrue(rec.checks)
        for name, ok in rec.checks.items():
            self.assertTrue(ok, name)
        G.assert_exact(gd.S)


class TestGrassmannAlgebra(unittest.TestCase):
    def test_signs_and_derivatives(self):
        t1, t2, t3 = GA.Grassmann.gen(1), GA.Grassmann.gen(2), GA.Grassmann.gen(3)
        self.assertTrue((t1 * t2 + t2 * t1).is_zero())
        self.assertTrue((t1 * t1).is_zero())
        p = t1 * t2 * t3
        self.assertEqual(p.left_derivative(2), -(t1 * t3))
        self.assertEqual(p.right_derivative(2), -(t1 * t3))
        self.assertEqual(p.left_derivative(1), t2 * t3)
        self.assertEqual(p.right_derivative(3), t1 * t2)

    def test_conjugation_rules(self):
        rec = DM.Recorder()
        DM.demo_conjugation_rules(rec)
        self.assertTrue(rec.checks["GR_conjugationRules"])

    def test_even_derivation_leibniz(self):
        rng = random.Random(7)
        gmap = {0: 4, 1: 5, 2: 6, 3: 7}.get

        def rnd():
            A = GA.Grassmann()
            for _ in range(5):
                A = A + GA.Grassmann.from_monomial(rng.sample(range(4), rng.randint(1, 3)), rng.randint(-3, 3))
            return A

        A, B = rnd(), rnd()
        D = lambda X: X.apply_generator_map_derivation(gmap)  # noqa: E731
        self.assertTrue((D(A * B) - (D(A) * B + A * D(B))).is_zero())
        img = lambda g: GA.Grassmann.gen(gmap(g)) if gmap(g) is not None else None  # noqa: E731
        self.assertTrue((A.apply_even_derivation(img) - D(A)).is_zero())

    def test_batched_el_equals_single(self):
        js = GA.JetSpace(["psi", "psis"], nfield=3, ncoord=2, max_deriv=2)
        rng = random.Random(11)
        parts = {}
        for k in [(), (0,), (1,)]:
            F = GA.Grassmann()
            for _ in range(25):
                s1, s2 = rng.choice(["psi", "psis"]), rng.choice(["psi", "psis"])
                al1 = rng.choice([(), (0,), (1,)])
                al2 = rng.choice([(), (0,), (1,)])
                F = F + GA.Grassmann.from_monomial([js.idx(s1, rng.randrange(3), al1),
                                                    js.idx(s2, rng.randrange(3), al2)], rng.randint(-4, 4))
            parts[k] = F
        L = GA.JetGrassmann(parts)
        for s in ("psi", "psis"):
            batched = GA.euler_lagrange_all(L, js, s)
            for a in range(3):
                self.assertTrue((batched[a] - GA.euler_lagrange(L, js, s, a)).is_zero())


class TestRealGrassmannDemos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dom = G.make_qq_domain()
        cls.gd = G.GammaData(cls.dom)

    def test_mass_kinetic_quartic(self):
        rec = DM.Recorder()
        DM.demo_mass_real(rec, self.gd, self.dom)
        DM.demo_kinetic_real(rec, self.gd, self.dom)
        DM.demo_quartic(rec, self.gd, self.dom)
        DM.demo_current_hermitian(rec, self.gd, self.dom)
        for name in ("GR_massTermVanishesReal", "GR_bilinearOnlyAntisymmetricPartSurvives",
                     "GR_kineticTotalDerivativeReal", "GR_kineticSymmetricMatrixContrast",
                     "GR_quarticTermPolynomial", "GR_scalarBilinearHermitian", "GR_currentHermitian"):
            self.assertTrue(rec.checks[name], name)
        self.assertEqual(rec.meas["GR_massTermVanishesReal_PsiT_C_Psi_nonzeroMonomials"], 0)
        self.assertEqual(rec.meas["GR_quarticTermPolynomial_nonzeroMonomials_k1_to_k17"][16], 0)


class TestPrimordialG2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dom = G.make_g2_domain()
        cls.gd = G.GammaData(cls.dom)
        cls.geo = G.Geometry(G.g2_vielbein_jet(2, cls.dom), cls.gd, cls.dom, "G2", sqrtg_sign=1)

    def test_connection_identities(self):
        geo, dom = self.geo, self.dom
        self.assertTrue(G.jet_is_zero(geo.vielbein_postulate("christoffel"), dom))
        self.assertTrue(G.jet_is_zero(geo.vielbein_postulate("anholonomy"), dom))
        self.assertTrue(G.jet_is_zero(geo.omega_antisym_defect(), dom))
        self.assertEqual(G.count_nonzero(geo.omega_low.value(), dom), 24)
        self.assertTrue(G.jet_is_zero(geo.gamma_covariant_derivative(max_order=0), dom))
        self.assertFalse(G.jet_is_zero(geo.gamma_covariant_derivative(notebook=True, max_order=0), dom))
        self.assertTrue(G.jet_is_zero(geo.divergence_identity_defect(max_order=0), dom))

    def test_primordial_facts(self):
        geo, dom, gd = self.geo, self.dom, self.gd
        H, A1, A2 = G.G2_H, G.G2_A1, G.G2_A2
        self.assertTrue(dom.is_zero(geo.sqrtg.value()[()] - dom.conv(G.G2_C)))
        self.assertTrue(G.arr_is_zero(geo.slash_omega() - gd.GAM[0] * dom.conv(3 * H), dom))
        self.assertTrue(dom.is_zero(geo.Rscalar - dom.conv(6 * H ** 2 * (A1 ** 2 - 7))))
        self.assertTrue(dom.is_zero(geo.Gmixed[4, 4] - dom.conv(3 * H ** 2 * (7 + A1 ** 2))))
        self.assertTrue(dom.is_zero(geo.Gmixed[1, 1] - dom.conv(H ** 2 * (15 - 3 * A1 ** 2 + A2))))

    def test_lichnerowicz(self):
        ok, c = CK.lichnerowicz(self.geo, G.random_spinor_jet(random.Random(2101), self.dom, 2))
        self.assertTrue(ok)
        self.assertEqual(c, "-1/4")

    def test_notebook_lg_trivial_and_complex_nontrivial(self):
        dom = self.dom
        cc, mm = {}, {}
        DM.demo_notebook_lg(cc, mm, self.geo, "G2", dom.conv(sp.Rational(-2, 3)))
        self.assertTrue(cc["trivial"])
        self.assertTrue(cc["pureDivergence"])
        DM.demo_complex(cc, mm, self.geo, "G2", dom.conv(sp.Rational(1, 2)), dom.conv(sp.Rational(3, 5)))
        for k in ("complex", "quartic", "psiEq", "herm", "unsymNotHerm"):
            self.assertTrue(cc[k], k)


class TestGenericG1Point(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dom = G.make_qq_domain()
        cls.gd = G.GammaData(cls.dom)
        ej = G.vielbein_jet_from_sympy(G.g1_vielbein_sympy(), G.G1_POINTS["p1"], 2, cls.dom)
        cls.ej = ej
        cls.geo = G.Geometry(ej, cls.gd, cls.dom, "G1_p1", curvature=False)

    def test_signature_and_identities(self):
        geo, dom = self.geo, self.dom
        e0 = self.ej.value()
        self.assertNotEqual(G.mat_det(e0, dom), 0)
        self.assertEqual(G.symmetric_signature_rational(e0.dot(self.gd.ETA).dot(e0.T)), (4, 4, 0))
        self.assertTrue(G.jet_is_zero(geo.vielbein_postulate("anholonomy"), dom, 0))
        self.assertTrue(G.jet_is_zero(geo.omega_low - geo.omega_low_anh, dom, 0))
        self.assertTrue(G.jet_is_zero(geo.omega_antisym_defect(), dom, 0))
        self.assertTrue(G.jet_is_zero(geo.gamma_covariant_derivative(max_order=0), dom))
        self.assertFalse(G.jet_is_zero(geo.gamma_covariant_derivative(notebook=True, max_order=0), dom))
        self.assertTrue(G.jet_is_zero(geo.divergence_identity_defect(max_order=0), dom))

    def test_euler_lagrange_commuting_proxy(self):
        rng = random.Random(1101)
        m = self.dom.conv(G.rand_rational(rng))
        ok, info = CK.el_psibar_check(self.geo, G.random_spinor_jet(rng, self.dom, 2), m)
        self.assertTrue(ok)
        self.assertGreater(info["spinConnectionTermNonzeroComponents"], 0)
        self.assertTrue(CK.el_psi_check(self.geo, G.random_spinor_jet(rng, self.dom, 2), m))

    def test_emt_trace_onshell(self):
        rng = random.Random(1202)
        m = self.dom.conv(G.rand_rational(rng))
        lam = self.dom.conv(G.rand_rational(rng))
        res = CK.emt_onshell_block(self.geo, rng, m, lam, order=1, conservation=False)
        self.assertTrue(res["solved"])
        self.assertTrue(res["symmetric"])
        self.assertTrue(res["trace_ok"])
        self.assertTrue(res["Ls_onshell_ok"])
        self.assertTrue(CK.emt_offshell_trace(self.geo, rng, m, lam))


class TestEMTReductions(unittest.TestCase):
    def test_minisuperspace_variation_and_homogeneous_reduction(self):
        rec = CK.Recorder()
        self.assertTrue(CK.run_emt_variation(rec, local=False))
        for name in ("EMT_variation_minisuperspace_noMetricVelocityDependence",
                     "EMT_variation_minisuperspace_diagonalTmixedAgree", "EMT_variation_minisuperspace_rhoAndPressure"):
            self.assertIs(rec.meas[name], True, name)
        dom = G.make_qq_domain()
        CK.run_g3(rec, G.GammaData(dom), dom)
        for name in ("EMT_homogeneousReduction", "GEO_diagonalSlashFormula_G3"):
            self.assertTrue(rec.checks[name], name)
        self.assertIs(rec.meas["EMT_homogeneousReduction_offDiagonalForms_G3"], True)


class TestWolframAgreementLogic(unittest.TestCase):
    """Exercises GEO_wolframAgreement on synthetic reports; it does not claim that Wolfram was run."""

    @staticmethod
    def synthetic():
        coords = {"p1": ["1/7", "-2/9", "1/5", "3/11", "-1/13", "2/17", "-3/19", "1/23"],
                  "p2": ["-1/3", "1/4", "2/7", "-1/5", "1/6", "-2/11", "1/9", "3/13"],
                  "p3": ["2/9", "1/8", "-1/7", "1/10", "-3/14", "1/12", "2/15", "-1/16"]}
        wm = {"convention.lichnerowicz": "(gamma^mu D_mu)^2 Psi = ... + c R Psi with c = -1/4, R = ...",
              "emt.signConvention": "CONTRACT section 7 sign confirmed: T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu} ...",
              "emt.trace": "on-shell T^mu_mu = -m S + 7 S U'(S) - 8 U(S) = -m S + 3 lambda S^2"}
        pm = {"G1_points": coords, "GEO_lichnerowicz_c_G1": "-1/4", "GEO_lichnerowicz_c_G2": "-1/4",
              "EMT_signConvention": "T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu} reproduces CONTRACT section 7",
              "EMT_traceStatement": "T^mu_mu = 7 K - 8 (m S + U) off shell; on shell T^mu_mu = -m S + 7 S U' - 8 U "
                                    "(= -m S + 3 lam S^2 for U = lam S^2/2)",
              "GEO_sqrtg_G2": "c", "GEO_ricciScalar_G2": "6*H**2*(A1**2 - 7)",
              "GEO_slashOmega_notebook_coefficients_G2": {"gamma0": "3*H/2", "gamma4": "3*A1*H/2", "residualNonzero": 0}}
        for k, lab in enumerate(("p1", "p2", "p3")):
            w, tag = "G1.%s." % lab, "G1_" + lab
            wm.update({w + "coordinates": "{" + ", ".join(coords[lab]) + "}", w + "detFrame": "%d/7" % (k + 8),
                       w + "sqrtAbsG": "%d/7" % (k + 8), w + "metricInertia": "{4, 4, 0}",
                       w + "inverseMetric44": "-%d/5" % (k + 6), w + "scalarCurvature": "%d/3" % (k - 7)})
            pm.update({"GEO_detVielbein_" + tag: "%d/7" % (k + 8), "GEO_metricSignature_" + tag: "(4,4,0)",
                       "GEO_inverseMetric44_" + tag: "-%d/5" % (k + 6), "GEO_ricciScalar_" + tag: "%d/3" % (k - 7)})
        for family, tag_of in (("G1", lambda lab: "G1_" + lab), ("G2", lambda lab: "G2")):
            counts = (448, 256, 4096) if family == "G1" else (24, 12, 288)
            for lab in ("p1", "p2", "p3"):
                w, tag = "%s.%s." % (family, lab), tag_of(lab)
                wm.update({w + "nonzeroOmegaLower": counts[0], w + "nonzeroOmegaMixedSymmetricPart": counts[1],
                           w + "notebookDGammaNonzeroEntries": counts[2], w + "lichnerowiczC": "-1/4",
                           w + "lichnerowiczPlusQuarterHolds": "false",
                           w + "curvatureCandidate.plusHalfLowered": "true",
                           w + "curvatureCandidate.minusHalfLowered": "false"})
                pm.update({"GEO_nonzeroOmegaLowComponents_" + tag: counts[0],
                           "GEO_nonzeroOmegaMixedSymmetricPart_" + tag: counts[1],
                           "GEO_notebookContraction_nonzeroEntries_DmuGammaNu_" + tag: counts[2],
                           "GEO_lichnerowicz_c_" + tag: "-1/4",
                           "GEO_curvature_spinCurvaturePlusHalfRiemannS_" + tag: True,
                           "GEO_curvature_spinCurvatureMinusHalfRiemannS_" + tag: False})
        # G2 point p1 of the Wolfram verifier: H = 2/3, a4' = 3/7 -> R = -2672/147, notebook (1, 3/7)
        for lab in ("p1", "p2", "p3"):
            w = "G2.%s." % lab
            wm.update({w + "point": "w = 1/2, sin z = 1/64, cos z = (3*Sqrt[455])/64, H = 2/3, a4(t) = Log[2], "
                                    "a4'(t) = 3/7, a4''(t) = -5/11, a4'''(t) = 2/13",
                       w + "sqrtAbsG": "(3*Sqrt[455])/64", w + "detFrame": "(3*Sqrt[455])/64",
                       w + "scalarCurvature": "-2672/147",
                       w + "notebookSlash": "gamma^mu OmegaNotebook_mu = (1) gamma^0 + (3/7) gamma^4, residual zero: true"})
        checks = {"GEO_lichnerowicz_G1": True, "GEO_curvature_G2": True}
        return {"schemaVersion": 1, "checks": dict(checks), "measurements": wm}, dict(checks), pm

    def test_agreement_and_tampering(self):
        wolfram, checks, pm = self.synthetic()
        ok, rows, verdicts = CK.compare_with_wolfram(checks, pm, wolfram)
        self.assertTrue(ok, [row for row in rows if not row["agree"]])
        self.assertEqual(verdicts["shared"], ["GEO_curvature_G2", "GEO_lichnerowicz_G1"])
        tampered = (("G1.p2.scalarCurvature", "-5/3", False), ("G2.p3.scalarCurvature", "-2672/149", False),
                    ("G2.p1.lichnerowiczC", "1/4", False), ("G1.p3.nonzeroOmegaLower", 447, False),
                    ("G2.p2.notebookSlash",
                     "gamma^mu OmegaNotebook_mu = (1) gamma^0 + (-3/7) gamma^4, residual zero: true", False))
        for key, value, _ in tampered:
            wolfram, checks, pm = self.synthetic()
            wolfram["measurements"][key] = value
            self.assertFalse(CK.compare_with_wolfram(checks, pm, wolfram)[0], key)
        wolfram, checks, pm = self.synthetic()
        del wolfram["measurements"]["G1.p1.inverseMetric44"]
        self.assertFalse(CK.compare_with_wolfram(checks, pm, wolfram)[0])
        wolfram, checks, pm = self.synthetic()
        wolfram["checks"]["GEO_lichnerowicz_G1"] = False
        ok, _, verdicts = CK.compare_with_wolfram(checks, pm, wolfram)
        self.assertFalse(ok)
        self.assertEqual(verdicts["disagreeing"], ["GEO_lichnerowicz_G1"])


if __name__ == "__main__":
    unittest.main()
