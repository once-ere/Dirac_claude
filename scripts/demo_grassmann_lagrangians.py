#!/usr/bin/env python3
"""Exact Grassmann-algebra demonstrations for dirac16complex (CONTRACT section 3 and 5).

Why the notebook Lagrangian Lg[] cannot be used for a fermion, and why the new
Lagrangian is non-trivial:

GR_massTermVanishesReal        Psi^T C Psi = 0 for real Grassmann Psi16 (C symmetric),
                               Psi^T C gamma^a Psi != 0 (C gamma^a antisymmetric).
GR_kineticTotalDerivativeReal  Psi^T A d_mu Psi = (1/2) d_mu (Psi^T A Psi) for antisymmetric A
                               (identity in the jet algebra; d_mu an even derivation).
GR_notebookLgELTrivial         Lg[] with real Grassmann Psi16 in curved space (G1 at p1 and the
                               symbolic primordial field G2): every Euler-Lagrange component is
                               identically zero for the canonical Omega; with the notebook
                               contraction it is nonzero but derivative-free (algebraic).
GR_complexLagrangianNonTrivial complex Grassmann Psi, Psibar = Psi^dagger C: the EL expression
                               w.r.t. Psi^*_a equals sqrt|g| (C (gamma^mu D_mu Psi - m Psi))_a.
GR_lagrangianHermitian         L^* = L with (theta1 theta2)^* = theta2^* theta1^*.
GR_quarticTermPolynomial       (Psibar Psi)^k != 0 for k = 1..16, = 0 for k = 17.

Writes artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
import time
from pathlib import Path
from typing import Dict, List

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import d16c_geometry_sympy as G  # noqa: E402
from grassmann_algebra import (Grassmann, GaussianRational, JetGrassmann, JetSpace, bilinear,  # noqa: E402
                               euler_lagrange, euler_lagrange_all, linear)

REPORT_PATH = ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / "grassmann-demo-report.json"
SOURCES = ["scripts/grassmann_algebra.py", "scripts/demo_grassmann_lagrangians.py", "scripts/d16c_geometry_sympy.py"]
SEED = 5101


class Recorder:
    def __init__(self):
        self.checks: Dict[str, bool] = {}
        self.meas: Dict[str, object] = {}

    def check(self, name, ok):
        if name in self.checks:
            raise KeyError(name)
        self.checks[name] = bool(ok)

    def measure(self, name, value):
        if name in self.meas:
            raise KeyError(name)
        self.meas[name] = value


def mat(a) -> List[List[object]]:
    a = np.asarray(a, dtype=object)
    return [[a[i, j] for j in range(a.shape[1])] for i in range(a.shape[0])]


# ---------------------------------------------------------------------------
# real Psi16: mass term and kinetic term
# ---------------------------------------------------------------------------


def demo_mass_real(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain):
    th = list(range(16))
    mass = bilinear(mat(gd.C), th, th)
    counts = []
    coeffs = set()
    for a in range(8):
        e = bilinear(mat(gd.C.dot(gd.GAM[a])), th, th)
        counts.append(e.nterms())
        coeffs.update(str(c) for c in e.terms.values())
    rec.check("GR_massTermVanishesReal", mass.nterms() == 0 and all(c > 0 for c in counts))
    rec.measure("GR_massTermVanishesReal_PsiT_C_Psi_nonzeroMonomials", mass.nterms())
    rec.measure("GR_massTermVanishesReal_PsiT_Cgamma_a_Psi_nonzeroMonomials", counts)
    rec.measure("GR_massTermVanishesReal_PsiT_Cgamma_a_Psi_coefficientValues", sorted(coeffs))
    # Psi^T M Psi = Psi^T M_antisym Psi for a random integer matrix
    rng = random.Random(SEED)
    M = np.array([[dom.conv(rng.randint(-5, 5)) for _ in range(16)] for _ in range(16)], dtype=object)
    MA = (M - M.T) * dom.frac(1, 2)
    rec.check("GR_bilinearOnlyAntisymmetricPartSurvives",
              bilinear(mat(M), th, th) == bilinear(mat(MA), th, th)
              and bilinear(mat((M + M.T) * dom.frac(1, 2)), th, th).nterms() == 0)


def demo_kinetic_real(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain):
    js = JetSpace(["psi"], max_deriv=2)
    th = js.gens("psi")
    rng = random.Random(SEED + 1)
    R = np.array([[dom.conv(rng.randint(-4, 4)) for _ in range(16)] for _ in range(16)], dtype=object)
    Aanti = R - R.T
    mats = [("Cgamma%d" % a, gd.C.dot(gd.GAM[a])) for a in range(8)] + [("randomAntisymmetric", Aanti)]
    ok = True
    ok_el = True
    for name, A in mats:
        biA = bilinear(mat(A), th, th)
        for mu in range(8):
            lhs = bilinear(mat(A), th, js.gens("psi", (mu,)))
            rhs = js.total_derivative(biA, mu).scale(dom.frac(1, 2))
            ok = ok and (lhs == rhs) and lhs.nterms() > 0
            # constant-coefficient Lagrangian lhs has identically vanishing EL expression
            L = JetGrassmann({(): lhs})
            if any(e.nterms() != 0 for e in euler_lagrange_all(L, js, "psi")):
                ok_el = False
    rec.check("GR_kineticTotalDerivativeReal", ok and ok_el)
    rec.measure("GR_kineticTotalDerivativeReal_matricesTested", [n for n, _ in mats])
    # contrast: symmetric matrix (C itself): Psi^T C d Psi != 0, d(Psi^T C Psi) = 0, EL = 2 C d_mu Psi != 0
    biC = bilinear(mat(gd.C), th, th)
    lhsC = bilinear(mat(gd.C), th, js.gens("psi", (0,)))
    ELC = euler_lagrange(JetGrassmann({(): lhsC}), js, "psi", 0)
    expect = linear(list(gd.C[0, :] * 2), js.gens("psi", (0,)))
    rec.check("GR_kineticSymmetricMatrixContrast",
              lhsC.nterms() > 0 and js.total_derivative(biC, 0).nterms() == 0 and ELC == expect)
    rec.measure("GR_kineticSymmetricMatrixContrast_statement",
                "A = C (symmetric): Psi^T C d_0 Psi has %d monomials, d_0(Psi^T C Psi) = 0, EL_0 = 2 (C d_0 Psi)_0"
                % lhsC.nterms())


# ---------------------------------------------------------------------------
# curved-space Lagrangians
# ---------------------------------------------------------------------------


def jet_bilinear(Mjet: G.TJet, left, right) -> JetGrassmann:
    """sum M(x)_ab theta_left_a theta_right_b with order-1 Taylor data of M."""
    parts = {}
    for k in [()] + [(l,) for l in range(8)]:
        parts[k] = bilinear(mat(Mjet.coeff(k)), left, right)
    return JetGrassmann(parts)


def jet_scale_element(sjet: G.TJet, F: Grassmann) -> JetGrassmann:
    """s(x) F for a scalar jet s and a constant-coefficient element F."""
    parts = {}
    for k in [()] + [(l,) for l in range(8)]:
        parts[k] = F.scale(sjet.coeff(k)[()])
    return JetGrassmann(parts)


def jsum(items: List[JetGrassmann]) -> JetGrassmann:
    out = items[0]
    for it in items[1:]:
        out = out + it
    return out


def coefficient_jets(geo: G.Geometry, notebook: bool):
    """sqrt|g| C gamma^mu, sqrt|g| C gamma^mu Omega_mu, sqrt|g| C Omega_mu gamma^mu, sqrt|g| C (order-1 jets)."""
    C = geo.gd.C
    Om = geo.Omega_nb if notebook else geo.Omega
    sg = geo.sqrtg.truncate(1)
    gam = geo.gam.truncate(1)
    Om = Om.truncate(1)
    A = G.jmul(sg, G.jein("ij,mjk->mik", C, gam))                                   # (8,16,16)
    B = G.jmul(sg, G.jein("ij,mjk->ik", C, G.jein("mij,mjk->mik", gam, Om)))       # C gamma^mu Omega_mu
    Bp = G.jmul(sg, G.jein("ij,mjk->ik", C, G.jein("mij,mjk->mik", Om, gam)))      # C Omega_mu gamma^mu
    M = G.jmul(sg, TJetC(C))
    return A, B, Bp, M


def TJetC(C):
    return G.TJet.const(C)


def slice_mu(A: G.TJet, mu: int) -> G.TJet:
    return A.map(lambda v: v[mu])


def notebook_lagrangian_real(geo: G.Geometry, js: JetSpace, HM, notebook: bool) -> JetGrassmann:
    """sqrt|g| [Psi^T C gamma^mu (d_mu Psi + Omega_mu Psi) + H M Psi^T C Psi] (Q1 = 1), real Grassmann Psi16."""
    A, B, _, M = coefficient_jets(geo, notebook)
    th = js.gens("psi")
    terms = [jet_bilinear(slice_mu(A, mu), th, js.gens("psi", (mu,))) for mu in range(8)]
    terms.append(jet_bilinear(B, th, th))
    terms.append(jet_bilinear(M, th, th).scale(HM))
    return jsum(terms)


def demo_notebook_lg(rec_c: Dict[str, bool], rec_m: Dict[str, object], geo: G.Geometry, tag: str, HM):
    dom = geo.dom
    js = JetSpace(["psi"], max_deriv=2)
    th = js.gens("psi")
    results = {}
    for nb in (False, True):
        L = notebook_lagrangian_real(geo, js, HM, nb)
        E = euler_lagrange_all(L, js, "psi")
        nz = [e for e in E if not e.is_zero(dom.is_zero)]
        deriv_free = all(js.deriv_order(g) == 0 for e in E for g in e.generators())
        results[nb] = (E, len(nz), sum(e.nterms() for e in E), deriv_free, L)
    E0, nz0, nt0, _, L0 = results[False]
    E1, nz1, nt1, df1, L1 = results[True]
    # predicted algebraic EL with the notebook contraction: sqrt|g| C [gamma^mu, Omega^nb_mu - Omega_mu] Psi
    diffOm = geo.Omega_nb.value() - geo.Omega.value()
    gam0 = geo.gam.value()
    Npred = geo.gd.C.dot(np.einsum("mij,mjk->ik", gam0, diffOm) - np.einsum("mij,mjk->ik", diffOm, gam0)) \
        * geo.sqrtg.value()[()]
    pred_ok = all((E1[a] - linear(list(Npred[a, :]), th)).is_zero(dom.is_zero) for a in range(16))
    # pure divergence: Lg[] (canonical) = d_mu V^mu with V^mu = (1/2) sqrt|g| Psi^T C gamma^mu Psi
    A, _, _, _ = coefficient_jets(geo, False)
    V = [jet_bilinear(slice_mu(A, mu), th, th).scale(dom.frac(1, 2)) for mu in range(8)]
    divV = Grassmann()
    for mu in range(8):
        divV = divV + V[mu].total_derivative_at_point(js, mu)
    pure_div = (L0.value() - divV).is_zero(dom.is_zero)
    rec_c["trivial"] = nz0 == 0 and nz1 > 0 and df1 and pred_ok
    rec_c["pureDivergence"] = pure_div
    rec_m["GR_notebookLgEL_canonicalOmega_nonzeroComponents_" + tag] = nz0
    rec_m["GR_notebookLgEL_notebookContraction_nonzeroComponents_" + tag] = nz1
    rec_m["GR_notebookLgEL_notebookContraction_totalTerms_" + tag] = nt1
    rec_m["GR_notebookLgEL_notebookContraction_derivativeFree_" + tag] = df1
    rec_m["GR_notebookLgEL_notebookContraction_matchesSqrtgC[gamma,OmegaNB-Omega]Psi_" + tag] = pred_ok
    rec_m["GR_notebookLg_lagrangianTerms_canonical_" + tag] = L0.value().nterms()


def new_lagrangian(geo: G.Geometry, js: JetSpace, m, lam) -> Dict[str, object]:
    """sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - (lam/2)(Psibar Psi)^2 ],
    Psibar_a = sum_b Psi^*_b C_ba, D_mu Psibar = d_mu Psibar - Psibar Omega_mu, complex Grassmann Psi."""
    dom = geo.dom
    half = dom.frac(1, 2)
    A, B, Bp, M = coefficient_jets(geo, False)
    ps = js.gens("psi")
    pss = js.gens("psis")
    K1 = jsum([jet_bilinear(slice_mu(A, mu), pss, js.gens("psi", (mu,))) for mu in range(8)])
    K2 = jet_bilinear(B, pss, ps)
    K3 = jsum([jet_bilinear(slice_mu(A, mu), js.gens("psis", (mu,)), ps) for mu in range(8)])
    K4 = jet_bilinear(Bp, pss, ps)
    S = bilinear(mat(geo.gd.C), pss, ps)
    S2 = S * S
    L = (K1 + K2 - K3 + K4).scale(half) - jet_bilinear(M, pss, ps).scale(m) - \
        jet_scale_element(geo.sqrtg.truncate(1), S2).scale(lam * half)
    return {"L": L, "S": S, "A": A, "B": B, "Bp": Bp, "M": M, "K12": K1 + K2}


def demo_complex(rec_c: Dict[str, bool], rec_m: Dict[str, object], geo: G.Geometry, tag: str, m, lam):
    dom = geo.dom
    js = JetSpace(["psi", "psis"], max_deriv=2)
    ps = js.gens("psi")
    pss = js.gens("psis")
    C = geo.gd.C
    sg = geo.sqrtg.value()[()]
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    slash = np.einsum("mij,mjk->ik", gam0, Om0)                  # gamma^mu Omega_mu
    slashR = np.einsum("mij,mjk->ik", Om0, gam0)                 # Omega_mu gamma^mu
    ok_all = True
    ok_q = True
    ok_psi = True
    herm = True
    info = {}
    for lam_case in (0, 1):
        lam_v = lam if lam_case else dom.zero
        parts = new_lagrangian(geo, js, m, lam_v)
        L = parts["L"]
        S = parts["S"]
        E_all = euler_lagrange_all(L, js, "psis")
        Ep_all = euler_lagrange_all(L, js, "psi")
        if lam_case:
            # cross-check the batched EL against the one-component implementation
            ok_q = ok_q and (E_all[3] - euler_lagrange(L, js, "psis", 3)).is_zero(dom.is_zero)
        for a in range(16):
            E = E_all[a]
            # target: sqrt|g| ( C (gamma^mu D_mu Psi - (m + lam S) Psi) )_a
            tgt = Grassmann()
            for mu in range(8):
                tgt = tgt + linear(list(C.dot(gam0[mu])[a, :] * sg), js.gens("psi", (mu,)))
            tgt = tgt + linear(list(C.dot(slash)[a, :] * sg), ps) - linear(list(C[a, :] * (sg * m)), ps)
            if lam_case:
                tgt = tgt - (S * linear(list(C[a, :]), ps)).scale(sg * lam_v)
            good = (E - tgt).is_zero(dom.is_zero)
            if lam_case:
                ok_q = ok_q and good
            else:
                ok_all = ok_all and good
                if a == 0:
                    info["derivTerms"] = sum(1 for mono in E.terms if any(js.deriv_order(g) == 1 for g in mono))
                    om_part = linear(list(C.dot(slash)[a, :] * sg), ps)
                    info["omegaTerms"] = om_part.nterms()
            # Psi equation: sqrt|g| ((D_mu Psibar) gamma^mu + (m + lam S) Psibar)_a
            Ep = Ep_all[a]
            tgp = Grassmann()
            for mu in range(8):
                tgp = tgp + linear(list(C.dot(gam0[mu])[:, a] * sg), js.gens("psis", (mu,)))
            tgp = tgp - linear(list(C.dot(slashR)[:, a] * sg), pss) + linear(list(C[:, a] * (sg * m)), pss)
            if lam_case:
                tgp = tgp + (S * linear(list(C[:, a]), pss)).scale(sg * lam_v)
            ok_psi = ok_psi and (Ep - tgp).is_zero(dom.is_zero)
        # Hermiticity of all jet parts of L
        cmap = js.conj_map({"psi": "psis", "psis": "psi"})
        for k, v in L.parts.items():
            herm = herm and (v.conjugate(cmap) - v).is_zero(dom.is_zero)
        herm = herm and (S.conjugate(cmap) - S).is_zero(dom.is_zero)
        if lam_case:
            # negative control: the unsymmetrised kinetic term Psibar gamma^mu D_mu Psi alone is NOT Hermitian
            K12 = parts["K12"].value()
            info["unsymNotHermitian"] = not (K12.conjugate(cmap) - K12).is_zero(dom.is_zero)
    om_nonzero = G.count_nonzero(slash, dom)
    rec_c["complex"] = ok_all and info["derivTerms"] > 0 and info["omegaTerms"] > 0 and om_nonzero > 0
    rec_c["quartic"] = ok_q
    rec_c["psiEq"] = ok_psi
    rec_c["herm"] = herm
    rec_c["unsymNotHerm"] = info["unsymNotHermitian"]
    rec_m["GR_complexLagrangianNonTrivial_EL0_derivativeJetTerms_" + tag] = info["derivTerms"]
    rec_m["GR_complexLagrangianNonTrivial_EL0_spinConnectionTerms_" + tag] = info["omegaTerms"]
    rec_m["GR_complexLagrangianNonTrivial_gammaMuOmegaMu_nonzeroEntries_" + tag] = om_nonzero


def demo_current_hermitian(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain):
    js = JetSpace(["psi", "psis"], max_deriv=0)
    ps = js.gens("psi")
    pss = js.gens("psis")
    cmap = js.conj_map({"psi": "psis", "psis": "psi"})
    minus_i = GaussianRational(dom.zero, dom.conv(-1))
    ok = True
    anti = True
    for a in range(8):
        Mg = gd.C.dot(gd.GAM[a])
        Jr = bilinear(mat(Mg), pss, ps)                       # Psibar gamma^a Psi (real coefficients)
        anti = anti and (Jr.conjugate(cmap) + Jr).nterms() == 0 and Jr.nterms() > 0
        Jc = Grassmann({mm: GaussianRational(dom.zero, dom.zero) + c * minus_i for mm, c in Jr.terms.items()})
        ok = ok and (Jc.conjugate(cmap) - Jc).is_zero(lambda c: c == 0)
    # B = -i C gamma^4 form: Psi^dagger B Psi = J^4 (flat) is Hermitian
    rec.check("GR_currentHermitian", ok and anti)
    rec.measure("GR_currentHermitian_statement",
                "Psibar gamma^a Psi is anti-Hermitian ((Psi^dag A Psi)^* = Psi^dag A^dag Psi, A = C gamma^a real "
                "antisymmetric); J^a = -i Psibar gamma^a Psi is Hermitian (Gaussian-rational coefficients)")


def demo_emt_hermitian(rec_c, geo: G.Geometry, m, lam):
    """T_{mu nu} of CONTRACT section 7 as Grassmann elements at the point: T^* = T."""
    dom = geo.dom
    js = JetSpace(["psi", "psis"], max_deriv=1)
    ps = js.gens("psi")
    pss = js.gens("psis")
    C = geo.gd.C
    gl = geo.gam_low.value()
    gu = geo.gam.value()
    Om = geo.Omega.value()
    g0 = geo.g.value()
    half = dom.frac(1, 2)
    quarter = dom.frac(1, 4)
    # Psibar X D_n Psi = psis^T C X (d_n psi + Omega_n psi); (D_n Psibar) X Psi = (d_n psis^T C - psis^T C Omega_n) X psi
    def pb_X_Dpsi(X, n):
        return bilinear(mat(C.dot(X)), pss, js.gens("psi", (n,))) + bilinear(mat(C.dot(X).dot(Om[n])), pss, ps)

    def Dpb_X_psi(X, n):
        return bilinear(mat(C.dot(X)), js.gens("psis", (n,)), ps) - bilinear(mat(C.dot(Om[n]).dot(X)), pss, ps)

    kin = Grassmann()
    for mu in range(8):
        kin = kin + pb_X_Dpsi(gu[mu], mu) - Dpb_X_psi(gu[mu], mu)
    S = bilinear(mat(C), pss, ps)
    Ls = kin.scale(half) - S.scale(m) - (S * S).scale(lam * half)
    cmap = js.conj_map({"psi": "psis", "psis": "psi"})
    herm = (Ls.conjugate(cmap) - Ls).is_zero(dom.is_zero)
    for mu in range(8):
        for nu in range(mu, 8):
            T = (pb_X_Dpsi(gl[mu], nu) + pb_X_Dpsi(gl[nu], mu) - Dpb_X_psi(gl[nu], mu) - Dpb_X_psi(gl[mu], nu)
                 ).scale(-quarter) + Ls.scale(g0[mu, nu])
            herm = herm and (T.conjugate(cmap) - T).is_zero(dom.is_zero)
    rec_c["emtHerm"] = herm


def demo_quartic(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain):
    js = JetSpace(["psi", "psis"], max_deriv=0)
    ps = js.gens("psi")
    pss = js.gens("psis")
    S = bilinear(mat(gd.C), pss, ps)
    counts = []
    coeff_ok = True
    P = Grassmann.scalar(dom.one)
    for k in range(1, 18):
        P = P * S
        counts.append(P.nterms())
        if k <= 16:
            coeff_ok = coeff_ok and P.nterms() == math.comb(16, k) and \
                all(abs(int(c)) == math.factorial(k) for c in P.terms.values())
    explicit_small = all(counts[k - 1] > 0 for k in (1, 2, 3))
    degree_arg = 2 * 17 > 32
    ok = explicit_small and coeff_ok and all(counts[k - 1] > 0 for k in range(1, 17)) and counts[16] == 0 and degree_arg
    rec.check("GR_quarticTermPolynomial", ok)
    rec.measure("GR_quarticTermPolynomial_nonzeroMonomials_k1_to_k17", counts)
    rec.measure("GR_quarticTermPolynomial_degreeArgument",
                "S = Psibar Psi has Grassmann degree 2; S^17 has degree 34 > 32 generators (16 Psi + 16 Psi^*) => 0; "
                "explicit powers computed for all k = 1..17; |coefficients| = k!, #monomials = binom(16,k)")
    cmap = js.conj_map({"psi": "psis", "psis": "psi"})
    rec.check("GR_scalarBilinearHermitian", (S.conjugate(cmap) - S).nterms() == 0 and S.nterms() == 16)


def demo_conjugation_rules(rec: Recorder):
    """Basic rules: (t1 t2)^* = t2^* t1^*, involution, (AB)^* = B^* A^*."""
    # generators 0,1 = theta1, theta2 ; 2,3 = theta1^*, theta2^*
    cm = {0: 2, 1: 3, 2: 0, 3: 1}.__getitem__
    t1, t2 = Grassmann.gen(0), Grassmann.gen(1)
    lhs = (t1 * t2).conjugate(cm)
    rhs = Grassmann.gen(3) * Grassmann.gen(2)
    rng = random.Random(SEED + 7)
    A = Grassmann()
    B = Grassmann()
    for _ in range(6):
        A = A + Grassmann.from_monomial(rng.sample(range(4), rng.randint(0, 3)), rng.randint(-3, 3))
        B = B + Grassmann.from_monomial(rng.sample(range(4), rng.randint(0, 3)), rng.randint(-3, 3))
    prod_rule = ((A * B).conjugate(cm) - B.conjugate(cm) * A.conjugate(cm)).nterms() == 0
    invol = (A.conjugate(cm).conjugate(cm) - A).nterms() == 0
    anti = (t1 * t2 + t2 * t1).nterms() == 0 and (t1 * t1).nterms() == 0
    rec.check("GR_conjugationRules", lhs == rhs and prod_rule and invol and anti)


def sha256_of(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def main() -> int:
    t0 = time.time()
    rec = Recorder()

    def stamp(label):
        print("[%7.1f s] %s" % (time.time() - t0, label), file=sys.stderr, flush=True)

    dom = G.make_qq_domain()
    gd = G.GammaData(dom)
    demo_conjugation_rules(rec)
    demo_mass_real(rec, gd, dom)
    demo_kinetic_real(rec, gd, dom)
    stamp("flat demos done")
    demo_quartic(rec, gd, dom)
    demo_current_hermitian(rec, gd, dom)
    stamp("quartic/current done")
    # curved geometries: G1 at p1 (rational) and G2 (symbolic primordial field)
    rng = random.Random(SEED + 11)
    geo1 = G.Geometry(G.vielbein_jet_from_sympy(G.g1_vielbein_sympy(), G.G1_POINTS["p1"], 2, dom), gd, dom,
                      "G1_p1", curvature=False)
    dom2 = G.make_g2_domain()
    gd2 = G.GammaData(dom2)
    geo2 = G.Geometry(G.g2_vielbein_jet(2, dom2), gd2, dom2, "G2", sqrtg_sign=1, curvature=False)
    stamp("geometries built")
    per = {}
    for geo, tag in ((geo1, "G1_p1"), (geo2, "G2")):
        d = geo.dom
        HM = d.conv(G.rand_rational(rng))
        m = d.conv(G.rand_rational(rng))
        lam = d.conv(G.rand_rational(rng))
        cc: Dict[str, bool] = {}
        mm: Dict[str, object] = {}
        demo_notebook_lg(cc, mm, geo, tag, HM)
        stamp("notebook Lg " + tag)
        demo_complex(cc, mm, geo, tag, m, lam)
        stamp("complex L " + tag)
        demo_emt_hermitian(cc, geo, m, lam)
        stamp("EMT hermitian " + tag)
        per[tag] = cc
        for k, v in mm.items():
            rec.measure(k, v)
        rec.measure("GR_parameters_" + tag, {"HM": d.to_str(HM), "m": d.to_str(m), "lambda": d.to_str(lam)})
    rec.check("GR_notebookLgELTrivial", per["G1_p1"]["trivial"] and per["G2"]["trivial"])
    rec.check("GR_notebookLgPureDivergence", per["G1_p1"]["pureDivergence"] and per["G2"]["pureDivergence"])
    rec.check("GR_complexLagrangianNonTrivial", per["G1_p1"]["complex"] and per["G2"]["complex"])
    rec.check("GR_complexQuarticEL", per["G1_p1"]["quartic"] and per["G2"]["quartic"])
    rec.check("GR_complexPsiEquation", per["G1_p1"]["psiEq"] and per["G2"]["psiEq"])
    rec.check("GR_lagrangianHermitian", per["G1_p1"]["herm"] and per["G2"]["herm"])
    rec.check("GR_emtHermitian", per["G1_p1"]["emtHerm"] and per["G2"]["emtHerm"])
    rec.check("GR_unsymmetrizedKineticNotHermitian", per["G1_p1"]["unsymNotHerm"] and per["G2"]["unsymNotHerm"])
    rec.measure("GR_geometries",
                "G1 at p1 (generic non-diagonal vielbein, exact rationals) and G2 (primordial field, symbolic point "
                "w=sin(z)^(1/6), c=cos z, E=exp(a4), A1, A2, H); coefficient functions carried as exact order-1 "
                "Taylor data, total derivative d_mu = explicit coefficient derivative + even derivation on field jets")
    rec.measure("GR_generatorCounts",
                {"realPsi16JetSpace": JetSpace(["psi"], max_deriv=2).ngen,
                 "complexPsiJetSpace": JetSpace(["psi", "psis"], max_deriv=2).ngen})
    rec.measure("G2_relationUsesInZeroTests", dom2.relation_uses)

    report = {
        "schemaVersion": 1,
        "producer": "scripts/demo_grassmann_lagrangians.py (python %s, sympy %s, numpy %s)" % (
            sys.version.split()[0], sp.__version__, np.__version__),
        "checks": rec.checks,
        "measurements": rec.meas,
        "sourceSha256": {rel: sha256_of(rel) for rel in SOURCES},
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_bytes((json.dumps(report, indent=2, sort_keys=False, ensure_ascii=True) + "\n").encode("utf-8"))
    for k, v in rec.checks.items():
        print("check_%s=%s" % (k, "true" if v else "false"))
    for k, v in rec.meas.items():
        if isinstance(v, (dict, list)):
            v = json.dumps(v, sort_keys=False, ensure_ascii=True)
        print("measurement_%s=%s" % (k, v))
    failed = [k for k, v in rec.checks.items() if not v]
    print("check_count=%d" % len(rec.checks))
    print("failed_check_count=%d" % len(failed))
    stamp("done")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
