#!/usr/bin/env python3
"""Independent exact Python (sympy/gmpy2) verifier of the dirac16complex geometry.

Checks CONTRACT.md sections 1 and 4-7 in the test geometries

* G1: generic non-diagonal test vielbein e = 1 + P(x) at the rational points p1, p2, p3;
* G2: the primordial field of CONTRACT section 9 at a fully symbolic point
      (w = sin(z)^(1/6), c = cos z, E = exp(a4), A1..A3 = a4', a4'', a4''', H);
* G3: diagonal Gaussian-normal x4-only vielbein h_i = 1 + x4^2/(i+2), h_4 = 1
      (homogeneous reduction of the EMT) at three rational times;
* symbolic diagonal metrics (minisuperspace h_mu(x4) and local h_mu(x)) for the
  variational derivation of the EMT.

Every check prints ``check_<name>=true|false``; measurements print
``measurement_<name>=<value>``; the JSON report is written to
artifacts/dirac16complex/arbitrary-field/python-geometry-report.json.
Exit status is nonzero if any check failed.

When the Wolfram geometry report exists (default
artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json, or
``--wolfram-report PATH``; an empty value skips it), the last check
GEO_wolframAgreement compares every measurement both implementations compute
(G1 point data, nonzero counts, the Lichnerowicz constant, the curvature sign,
the G2 values of the symbolic Python results at the exact Wolfram points, and
the EMT sign and trace conventions) and requires equal verdicts for every check
name both reports contain.
"""

from __future__ import annotations

import hashlib
import json
import random
import sys
import time
from pathlib import Path
from typing import Dict, List

import numpy as np
import sympy as sp
from sympy import QQ

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import d16c_geometry_sympy as G  # noqa: E402

REPORT_PATH = ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / "python-geometry-report.json"
SOURCES = ["scripts/d16c_geometry_sympy.py", "scripts/check_dirac16complex_geometry.py"]

G1_SEEDS = {"p1": 1101, "p2": 1202, "p3": 1303}
G2_SEEDS = [2101, 2202, 2303]
G3_SEEDS = {"q1": 3101, "q2": 3202, "q3": 3303}
VAR_SEEDS = [4101, 4202, 4303]

LEGITIMACY_NOTE = (
    "Commuting proxy: the Lagrangian is bilinear in (Psibar-jets, Psi-jets) and every term is written "
    "with the Psibar factor (Psi^* or d_mu Psi^*) to the LEFT of the Psi factor. The Grassmann left "
    "derivative d/dPsi^*_a acts on that leftmost factor without any sign, so term by term it equals the "
    "ordinary derivative of the same polynomial in commuting symbols; the EL expression is linear in the "
    "Psi-jets, hence evaluating it on commuting exact rationals is exact. (For the Psi-equation the "
    "Grassmann result differs from the commuting one only by an overall sign.) The genuine Grassmann "
    "computation is repeated in demo_grassmann_lagrangians.py."
)


class Recorder:
    def __init__(self):
        self.checks: Dict[str, bool] = {}
        self.meas: Dict[str, object] = {}

    def check(self, name: str, ok: bool) -> bool:
        ok = bool(ok)
        if name in self.checks:
            raise KeyError("duplicate check " + name)
        self.checks[name] = ok
        return ok

    def measure(self, name: str, value) -> None:
        if name in self.meas:
            raise KeyError("duplicate measurement " + name)
        self.meas[name] = value


def qstr(x) -> str:
    return str(sp.Rational(int(x.numerator), int(x.denominator)))


# ---------------------------------------------------------------------------
# gamma-algebra sanity checks (CONTRACT section 1)
# ---------------------------------------------------------------------------


def run_algebra(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain) -> None:
    GAM, C, ETA, I16 = gd.GAM, gd.C, gd.ETA, gd.ID16
    cl = all(G.arr_is_zero(GAM[a].dot(GAM[b]) + GAM[b].dot(GAM[a]) - I16 * (2 * ETA[a, b]), dom)
             for a in range(8) for b in range(8))
    rec.check("ALG_cliffordRelations", cl)
    rec.check("ALG_sigma16EqualsGamma0123", G.arr_is_zero(C - gd.SIG16, dom))
    rec.check("ALG_CSymmetricInvolution", G.arr_is_zero(C - C.T, dom) and G.arr_is_zero(C.dot(C) - I16, dom))
    rec.check("ALG_expression1CgammaAntisymmetric",
              all(G.arr_is_zero(C.dot(GAM[a]) + C.dot(GAM[a]).T, dom) for a in range(8)))
    rec.check("ALG_gammaSymmetryPattern",
              all(G.arr_is_zero(GAM[a] - GAM[a].T, dom) if a < 4 else G.arr_is_zero(GAM[a] + GAM[a].T, dom)
                  for a in range(8)))
    rec.check("ALG_CSabAntisymmetric",
              all(G.arr_is_zero(C.dot(gd.S[a, b]) + C.dot(gd.S[a, b]).T, dom) for a in range(8) for b in range(8)))
    chi_expected = np.zeros((16, 16), dtype=object)
    for i in range(16):
        chi_expected[i, i] = dom.conv(-1 if i < 8 else 1)
    rec.check("ALG_chiralityDiag", G.arr_is_zero(gd.CHI - chi_expected, dom))
    sym_ok = True
    anti_ok = True
    for c in range(8):
        for a in range(8):
            for b in range(8):
                ac = C.dot(GAM[c].dot(gd.S[a, b]) + gd.S[a, b].dot(GAM[c]))
                cm = C.dot(GAM[c].dot(gd.S[a, b]) - gd.S[a, b].dot(GAM[c]))
                sym_ok = sym_ok and G.arr_is_zero(ac - ac.T, dom)
                anti_ok = anti_ok and G.arr_is_zero(cm + cm.T, dom)
    rec.check("ALG_CAnticommutatorGammaSSymmetric", sym_ok)
    rec.check("ALG_CCommutatorGammaSAntisymmetric", anti_ok)
    # [S^{ab}, gamma^c] = gamma^a eta^{bc} - gamma^b eta^{ac}
    rec.check("ALG_SabGammaCommutator",
              all(G.arr_is_zero(gd.S[a, b].dot(GAM[c]) - GAM[c].dot(gd.S[a, b]) - GAM[a] * ETA[b, c] + GAM[b] * ETA[a, c],
                                dom) for a in range(8) for b in range(8) for c in range(8)))


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def lichnerowicz(geo: G.Geometry, psi: G.TJet):
    dom = geo.dom
    Dsl = G.dirac_operator(geo, psi)
    Dsl2 = G.dirac_operator(geo, Dsl).value()
    box = G.box_psi(geo, psi)
    diff = G._norm(Dsl2 - box)
    R = geo.Rscalar
    p0 = psi.value()
    ratios = set()
    ok = True
    for i in range(16):
        if dom.is_zero(p0[i]):
            ok = False
            continue
        if dom.is_zero(R):
            ok = False
            continue
        ratios.add(dom.to_str(diff[i] / (R * p0[i])))
    if len(ratios) != 1:
        return False, None
    cval = next(iter(ratios))
    c_dom = dom.conv(sp.Rational(cval))
    ok = ok and G.arr_is_zero(diff - p0 * (R * c_dom), dom)
    return ok, cval


def el_psibar_check(geo: G.Geometry, psi: G.TJet, m) -> (bool, Dict[str, object]):
    """LAG_eulerLagrangePsibar: EL(Psi^*) == sqrt|g| (C (gamma^mu D_mu Psi - m Psi))."""
    dom = geo.dom
    EL = G.euler_lagrange_psibar(geo, psi, m, lam=0)
    Dsl = G.dirac_operator(geo, psi).value()
    sg = geo.sqrtg.value()[()]
    target = G._norm(geo.gd.C.dot(Dsl - psi.value() * m) * sg)
    ok = G.arr_is_zero(EL - target, dom)
    # the spin-connection contribution to the EL expression
    om_part = G._norm(geo.gd.C.dot(geo.slash_omega().dot(psi.value())) * sg)
    nb_nonzero = G.count_nonzero(om_part, dom)
    return ok and nb_nonzero > 0, {"spinConnectionTermNonzeroComponents": nb_nonzero,
                                   "ELnonzeroComponents": G.count_nonzero(EL, dom)}


def el_psi_check(geo: G.Geometry, chi: G.TJet, m) -> bool:
    """EL(Psi) (commuting) == - sqrt|g| ((D_mu Psibar) gamma^mu + m Psibar)."""
    dom = geo.dom
    EL = G.euler_lagrange_psi(geo, chi, m, lam=0)
    pb = G.psibar_from_chi(geo, chi)
    Dpb = G.covariant_derivative_psibar(geo, pb, pb.grad()).value()
    val = np.einsum("mi,mij->j", Dpb, geo.gam.value()) + pb.value() * m
    sg = geo.sqrtg.value()[()]
    return G.arr_is_zero(EL + G._norm(val * sg), dom)


def emt_onshell_block(geo: G.Geometry, rng: random.Random, m, lam, order: int, conservation: bool):
    """On-shell (to order-1 if conservation) random fields; returns dict of results."""
    dom = geo.dom
    psi = G.random_spinor_jet(rng, dom, order)
    chi = G.random_spinor_jet(rng, dom, order)
    psi, chi = G.solve_onshell(geo, psi, chi, m, lam, max_order=order)
    E, Eb, _ = G.field_equations(geo, psi, chi, m, lam)
    solved = G.jet_is_zero(E, dom) and G.jet_is_zero(Eb, dom)
    parts = G.emt_from_fields(geo, psi, chi, m, lam)
    T = parts["T"]
    S = parts["S"].value()[()]
    T0 = T.value()
    trace = np.einsum("mn,mn->", geo.ginv.value(), T0)
    U = S * S * lam * dom.frac(1, 2)
    Up = S * lam
    target = -m * S + 7 * S * Up - 8 * U
    out = {
        "solved": solved,
        "symmetric": G.arr_is_zero(T0 - T0.T, dom),
        "trace_ok": dom.is_zero(trace - target),
        "trace": trace, "S": S,
        "Ls_onshell_ok": dom.is_zero(parts["Ls"].value()[()] - (S * Up - U)),
    }
    if conservation:
        div = G.emt_divergence(geo, T)
        out["conserved"] = G.arr_is_zero(div, dom)
        out["div_nonzero"] = G.count_nonzero(div, dom)
        out["dT_nonzero"] = G.count_nonzero(T.grad().value(), dom)
        out["T_nonzero"] = G.count_nonzero(T0, dom)
    return out


def emt_offshell_divergence_nonzero(geo: G.Geometry, rng: random.Random, m, lam) -> int:
    """Negative control: for random OFF-shell fields nabla^mu T_mu nu must not vanish."""
    dom = geo.dom
    psi = G.random_spinor_jet(rng, dom, 2)
    chi = G.random_spinor_jet(rng, dom, 2)
    T = G.emt_from_fields(geo, psi, chi, m, lam)["T"]
    return G.count_nonzero(G.emt_divergence(geo, T), dom)


def emt_offshell_trace(geo: G.Geometry, rng: random.Random, m, lam) -> bool:
    """Off-shell identity T^mu_mu = 7 K - 8 (m S + U), K = kinetic term."""
    dom = geo.dom
    psi = G.random_spinor_jet(rng, dom, 1)
    chi = G.random_spinor_jet(rng, dom, 1)
    parts = G.emt_from_fields(geo, psi, chi, m, lam)
    T0 = parts["T"].value()
    trace = np.einsum("mn,mn->", geo.ginv.value(), T0)
    S = parts["S"].value()[()]
    K = parts["kin"].value()[()]
    U = S * S * lam * dom.frac(1, 2)
    return dom.is_zero(trace - (7 * K - 8 * (m * S + U)))


def geometry_block(rec_c: Dict[str, bool], rec_m: Dict[str, object], geo: G.Geometry, tag: str, full_jets: bool = True):
    """Geometric identities of CONTRACT section 4 (per point)."""
    dom = geo.dom
    mo = None if full_jets else 0
    vp1 = G.jet_is_zero(geo.vielbein_postulate("christoffel"), dom, mo)
    vp2 = G.jet_is_zero(geo.vielbein_postulate("anholonomy"), dom, mo)
    agree = G.jet_is_zero(geo.omega_low - geo.omega_low_anh, dom, mo)
    rec_c["vp"] = vp1 and vp2 and agree
    rec_m["GEO_vielbeinPostulate_christoffelRoute_" + tag] = vp1
    rec_m["GEO_vielbeinPostulate_anholonomyRoute_" + tag] = vp2
    rec_m["GEO_omegaTwoRoutesAgree_" + tag] = agree
    rec_c["anti"] = G.jet_is_zero(geo.omega_antisym_defect(), dom, mo)
    rec_m["GEO_nonzeroOmegaLowComponents_" + tag] = G.count_nonzero(geo.omega_low.value(), dom)
    rec_m["GEO_nonzeroOmegaMixedSymmetricPart_" + tag] = G.count_nonzero(
        geo.omega_mixed.value() + np.einsum("mab->mba", geo.omega_mixed.value()), dom)
    DG = geo.gamma_covariant_derivative()
    rec_c["dgam"] = G.jet_is_zero(DG, dom, mo)
    DGn = geo.gamma_covariant_derivative(notebook=True).value()
    nz = G.count_nonzero(DGn, dom)
    pairs = sum(1 for mu in range(8) for nu in range(8) if not G.arr_is_zero(DGn[mu, nu], dom))
    rec_c["nbfail"] = nz > 0
    rec_m["GEO_notebookContraction_nonzeroEntries_DmuGammaNu_" + tag] = nz
    rec_m["GEO_notebookContraction_nonzeroPairs_DmuGammaNu_" + tag] = pairs
    rec_c["div"] = G.jet_is_zero(geo.divergence_identity_defect(), dom, mo)
    sg_gam = G.jmul(geo.sqrtg.truncate(1), geo.gam.truncate(1)).grad().value()
    rec_m["GEO_divergenceIdentity_lhsNonzeroEntries_" + tag] = G.count_nonzero(np.einsum("mmij->ij", sg_gam), dom)
    gam0 = geo.gam.value()
    for lab, Om in (("canonical", geo.Omega.value()), ("notebook", geo.Omega_nb.value())):
        acomm = np.einsum("mij,mjk->ik", gam0, Om) + np.einsum("mij,mjk->ik", Om, gam0)
        rec_m["GEO_anticommutatorGammaMuOmegaMu_%s_nonzeroEntries_%s" % (lab, tag)] = G.count_nonzero(acomm, dom)
        if lab == "canonical":
            rec_c["acommzero"] = G.arr_is_zero(acomm, dom)
    rec_m["GEO_divergenceIdentity_notebookContraction_nonzeroEntries_" + tag] = G.count_nonzero(
        geo.divergence_identity_defect(notebook=True).value(), dom)
    rec_c["sqrtg"] = G.jet_is_zero(geo.detg - G.jmul(geo.sqrtg, geo.sqrtg), dom, mo)
    half = dom.frac(1, 2)
    Fexp = np.einsum("abmn,abij->mnij", geo.Rframe_low, geo.gd.S) * half
    plus = G.arr_is_zero(geo.Fspin - Fexp, dom)
    minus = G.arr_is_zero(geo.Fspin + Fexp, dom)
    fnz = G.count_nonzero(geo.Fspin, dom)
    frame = G.arr_is_zero(geo.Romega_mixed - geo.Rframe_mixed, dom)
    ric = geo.Ric
    ricsym = G.arr_is_zero(ric - ric.T, dom)
    rec_m["GEO_curvature_spinCurvaturePlusHalfRiemannS_" + tag] = plus
    rec_m["GEO_curvature_spinCurvatureMinusHalfRiemannS_" + tag] = minus
    rec_m["GEO_curvature_spinCurvatureNonzeroEntries_" + tag] = fnz
    rec_m["GEO_curvature_frameCurvatureEqualsRiemann_" + tag] = frame
    rec_m["GEO_curvature_ricciSymmetric_" + tag] = ricsym
    rec_c["curv"] = plus and not minus and fnz > 0 and frame and ricsym


# ---------------------------------------------------------------------------
# G1
# ---------------------------------------------------------------------------


def run_g1(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain, labels=("p1", "p2", "p3"), full: bool = True):
    emat = G.g1_vielbein_sympy()
    agg: Dict[str, List[bool]] = {}
    cvals = []

    def add(key, ok):
        agg.setdefault(key, []).append(bool(ok))

    for lab in labels:
        pt = G.G1_POINTS[lab]
        rng = random.Random(G1_SEEDS[lab])
        ej = G.vielbein_jet_from_sympy(emat, pt, 2, dom)
        G.assert_exact(ej.value())
        e0 = ej.value()
        dete = G.mat_det(e0, dom)
        g0 = e0.dot(gd.ETA).dot(e0.T)
        sig = G.symmetric_signature_rational(g0)
        rec.measure("GEO_detVielbein_G1_" + lab, qstr(dete))
        rec.measure("GEO_metricSignature_G1_" + lab, "(%d,%d,%d)" % sig)
        geo = G.Geometry(ej, gd, dom, "G1_" + lab)
        g44 = geo.ginv.value()[4, 4]
        rec.measure("GEO_inverseMetric44_G1_" + lab, qstr(g44))
        add("sig", (dete != 0) and sig == (4, 4, 0) and g44 != 0)
        cc: Dict[str, bool] = {}
        mm: Dict[str, object] = {}
        geometry_block(cc, mm, geo, "G1_" + lab, full_jets=full)
        for k, v in mm.items():
            rec.measure(k, v)
        for k, v in cc.items():
            add(k, v)
        rec.measure("GEO_ricciScalar_G1_" + lab, qstr(geo.Rscalar))
        # Lichnerowicz
        psi2 = G.random_spinor_jet(rng, dom, 2)
        okL, cval = lichnerowicz(geo, psi2)
        add("lich", okL)
        cvals.append(cval)
        rec.measure("GEO_lichnerowicz_c_G1_" + lab, str(cval))
        # Euler-Lagrange (commuting proxy, lam = 0)
        m = dom.conv(G.rand_rational(rng))
        rec.measure("LAG_mass_G1_" + lab, qstr(m))
        psiL = G.random_spinor_jet(rng, dom, 2)
        okE, info = el_psibar_check(geo, psiL, m)
        add("elpb", okE)
        rec.measure("LAG_eulerLagrangePsibar_spinConnectionTermNonzeroComponents_G1_" + lab,
                    info["spinConnectionTermNonzeroComponents"])
        chiL = G.random_spinor_jet(rng, dom, 2)
        add("elpsi", el_psi_check(geo, chiL, m))
        # EMT (on-shell to first order, lam != 0)
        lam = dom.conv(G.rand_rational(rng))
        rec.measure("EMT_lambda_G1_" + lab, qstr(lam))
        res = emt_onshell_block(geo, rng, m, lam, order=2, conservation=full)
        add("onshell", res["solved"])
        add("emtsym", res["symmetric"])
        add("trace", res["trace_ok"])
        add("lsonshell", res["Ls_onshell_ok"])
        rec.measure("EMT_trace_G1_" + lab, qstr(res["trace"]))
        rec.measure("EMT_S_G1_" + lab, qstr(res["S"]))
        if full:
            add("conserved", res["conserved"])
            rec.measure("EMT_nonzeroEntries_T_dT_G1_" + lab, [res["T_nonzero"], res["dT_nonzero"]])
            nz_off = emt_offshell_divergence_nonzero(geo, rng, m, lam)
            rec.measure("EMT_offShellDivergenceNonzeroComponents_G1_" + lab, nz_off)
            add("offshellcontrol", nz_off > 0)
        add("traceoff", emt_offshell_trace(geo, rng, m, lam))
        G.assert_exact(geo.Omega.value())
        G.assert_exact(geo.Riem)

    rec.check("GEO_frameNondegenerate_G1", all(agg["sig"]))
    rec.check("GEO_vielbeinPostulate_G1", all(agg["vp"]))
    rec.check("GEO_omegaAntisymmetry_G1", all(agg["anti"]))
    rec.check("GEO_gammaCovariantConstancy_G1", all(agg["dgam"]))
    rec.check("GEO_notebookContractionFails_G1", all(agg["nbfail"]))
    rec.check("GEO_divergenceIdentity_G1", all(agg["div"]))
    rec.check("GEO_sqrtgSquaredEqualsDetg_G1", all(agg["sqrtg"]))
    rec.check("GEO_curvature_G1", all(agg["curv"]))
    rec.check("GEO_lichnerowicz_G1", all(agg["lich"]) and len(set(cvals)) == 1 and cvals[0] is not None)
    rec.measure("GEO_lichnerowicz_c_G1", str(cvals[0]))
    rec.check("LAG_eulerLagrangePsibar_G1", all(agg["elpb"]))
    rec.check("LAG_eulerLagrangePsi_G1", all(agg["elpsi"]))
    rec.check("EMT_onshellJetSolve_G1", all(agg["onshell"]))
    rec.check("EMT_symmetric_G1", all(agg["emtsym"]))
    rec.check("EMT_trace_G1", all(agg["trace"]))
    rec.check("EMT_traceOffShellIdentity_G1", all(agg["traceoff"]))
    rec.check("EMT_onshellLagrangianSUprimeMinusU_G1", all(agg["lsonshell"]))
    if full:
        rec.check("EMT_conservation_G1", all(agg["conserved"]) and all(agg["offshellcontrol"]))
    return cvals[0]


# ---------------------------------------------------------------------------
# G2 (primordial field, symbolic point)
# ---------------------------------------------------------------------------


def run_g2(rec: Recorder, full: bool = True):
    dom = G.make_g2_domain()
    gd = G.GammaData(dom)
    ej = G.g2_vielbein_jet(2, dom)
    geo = G.Geometry(ej, gd, dom, "G2", sqrtg_sign=1)
    rec.measure("G2_domain", dom.name)
    rec.measure("G2_substitution",
                "z=6Hx0, t=Hx4; exact symbolic differentiation in (z,t), then a4'''->A3, a4''->A2, a4'->A1, "
                "a4->log(E) (E=exp(A0)), sin z->w^6, cos z->c with w=sin(z)^(1/6)>0, c>0; relation "
                "w^12+c^2-1=0 applied only by ideal reduction inside zero tests (counted)")
    cc: Dict[str, bool] = {}
    mm: Dict[str, object] = {}
    geometry_block(cc, mm, geo, "G2", full_jets=full)
    for k, v in mm.items():
        rec.measure(k, v)
    rec.check("GEO_vielbeinPostulate_G2", cc["vp"])
    rec.check("GEO_omegaAntisymmetry_G2", cc["anti"])
    rec.check("GEO_gammaCovariantConstancy_G2", cc["dgam"])
    rec.check("GEO_notebookContractionFails_G2", cc["nbfail"])
    rec.check("GEO_divergenceIdentity_G2", cc["div"])
    rec.check("GEO_sqrtgSquaredEqualsDetg_G2", cc["sqrtg"])
    rec.check("GEO_curvature_G2", cc["curv"])
    rec.check("GEO_anticommutatorGammaOmegaVanishesDiagonal_G2", cc["acommzero"])
    # primordial-field facts of CONTRACT section 9
    H, A1, A2, cz = G.G2_H, G.G2_A1, G.G2_A2, G.G2_C
    sg = geo.sqrtg.value()[()]
    inv_sqrtg = dom.is_zero(sg - dom.conv(cz))
    inv_sqrtg4 = dom.is_zero(geo.sqrtg.coeff((4,))[()])
    rec.measure("GEO_sqrtg_G2", dom.to_str(sg))
    rec.measure("GEO_primordialInvariants_sqrtgEqualsCosz_G2", inv_sqrtg)
    rec.measure("GEO_primordialInvariants_d4sqrtgZero_G2", inv_sqrtg4)
    inv_om24 = G.count_nonzero(geo.omega_low.value(), dom) == 24
    rec.measure("GEO_primordialInvariants_omegaLowNonzeroCount24_G2", inv_om24)
    R = geo.Rscalar
    rec.measure("GEO_ricciScalar_G2", dom.to_str(R))
    inv_R = dom.is_zero(R - dom.conv(6 * H ** 2 * (A1 ** 2 - 7)))
    rec.measure("GEO_primordialInvariants_ricciScalar_G2", inv_R)
    Gexp = [-3 * H ** 2 * (A1 ** 2 - 5)] + [H ** 2 * (15 - 3 * A1 ** 2 + A2)] * 3 + [3 * H ** 2 * (7 + A1 ** 2)] + \
           [H ** 2 * (15 - 3 * A1 ** 2 - A2)] * 3
    Gm = geo.Gmixed
    okG = all(dom.is_zero(Gm[i, i] - dom.conv(Gexp[i])) for i in range(8))
    offd = all(dom.is_zero(Gm[i, j]) for i in range(8) for j in range(8) if i != j)
    rec.measure("GEO_primordialInvariants_einsteinTensorMixed_G2", okG and offd)
    rec.check("GEO_primordialInvariants_G2", inv_sqrtg and inv_sqrtg4 and inv_om24 and inv_R and okG and offd)
    rec.measure("GEO_einsteinTensorMixedDiagonal_G2", [dom.to_str(Gm[i, i]) for i in range(8)])
    # diagonal slash formula
    sl = geo.slash_omega()
    e0 = geo.e.value()
    form = np.zeros((16, 16), dtype=object)
    half = dom.frac(1, 2)
    for b in range(8):
        s = dom.zero
        for cix in range(8):
            if cix != b:
                s = s + geo.e.coeff((b,))[cix, cix] / e0[cix, cix]
        form = form + gd.GAM[b] * (half * s / e0[b, b])
    ok_form = G.arr_is_zero(sl - form, dom)
    ok_3h = G.arr_is_zero(sl - gd.GAM[0] * dom.conv(3 * H), dom)
    rec.check("GEO_diagonalSlashFormula_G2", ok_form and ok_3h)
    sln = geo.slash_omega(notebook=True)
    rec.measure("GEO_slashOmega_canonical_G2", "gamma^mu Omega_mu = (%s) gamma^0" % dom.to_str(np.einsum("ij,ji->", sl, gd.GAM[0]) / 16))
    rec.measure("GEO_slashOmega_notebook_coefficients_G2",
                {"gamma0": dom.to_str(np.einsum("ij,ji->", sln, gd.GAM[0]) / 16),
                 "gamma4": dom.to_str(-np.einsum("ij,ji->", sln, gd.GAM[4]) / 16),
                 "residualNonzero": G.count_nonzero(
                     sln - gd.GAM[0] * (np.einsum("ij,ji->", sln, gd.GAM[0]) / 16)
                     - gd.GAM[4] * (-np.einsum("ij,ji->", sln, gd.GAM[4]) / 16), dom)})
    # fields at the symbolic point, 3 seeds
    lich_ok, el_ok, elpsi_ok, tr_ok, sym_ok, solv_ok, cons_ok, troff_ok, ls_ok = ([] for _ in range(9))
    cvals = []
    for k, seed in enumerate(G2_SEEDS):
        rng = random.Random(seed)
        psi2 = G.random_spinor_jet(rng, dom, 2)
        okL, cval = lichnerowicz(geo, psi2)
        lich_ok.append(okL)
        cvals.append(cval)
        m = dom.conv(G.rand_rational(rng))
        psiL = G.random_spinor_jet(rng, dom, 2)
        okE, info = el_psibar_check(geo, psiL, m)
        el_ok.append(okE)
        rec.measure("LAG_eulerLagrangePsibar_spinConnectionTermNonzeroComponents_G2_s%d" % k,
                    info["spinConnectionTermNonzeroComponents"])
        chiL = G.random_spinor_jet(rng, dom, 2)
        elpsi_ok.append(el_psi_check(geo, chiL, m))
        lam = dom.conv(G.rand_rational(rng))
        res = emt_onshell_block(geo, rng, m, lam, order=2 if full else 1, conservation=full)
        solv_ok.append(res["solved"])
        tr_ok.append(res["trace_ok"])
        sym_ok.append(res["symmetric"])
        ls_ok.append(res["Ls_onshell_ok"])
        if full:
            cons_ok.append(res["conserved"])
            rec.measure("EMT_nonzeroEntries_T_dT_G2_s%d" % k, [res["T_nonzero"], res["dT_nonzero"]])
            if k == 0:
                nz_off = emt_offshell_divergence_nonzero(geo, rng, m, lam)
                rec.measure("EMT_offShellDivergenceNonzeroComponents_G2_s0", nz_off)
                cons_ok.append(nz_off > 0)
        troff_ok.append(emt_offshell_trace(geo, rng, m, lam))
    rec.check("GEO_lichnerowicz_G2", all(lich_ok) and len(set(cvals)) == 1 and cvals[0] is not None)
    rec.measure("GEO_lichnerowicz_c_G2", str(cvals[0]))
    rec.check("LAG_eulerLagrangePsibar_G2", all(el_ok))
    rec.check("LAG_eulerLagrangePsi_G2", all(elpsi_ok))
    rec.check("EMT_onshellJetSolve_G2", all(solv_ok))
    rec.check("EMT_symmetric_G2", all(sym_ok))
    rec.check("EMT_trace_G2", all(tr_ok))
    rec.check("EMT_traceOffShellIdentity_G2", all(troff_ok))
    rec.check("EMT_onshellLagrangianSUprimeMinusU_G2", all(ls_ok))
    if full:
        rec.check("EMT_conservation_G2", all(cons_ok))
    rec.measure("G2_relationUsesInZeroTests", dom.relation_uses)
    return cvals[0]


# ---------------------------------------------------------------------------
# G3: homogeneous reduction of the EMT
# ---------------------------------------------------------------------------


def run_g3(rec: Recorder, gd: G.GammaData, dom: G.ExactDomain):
    emat = G.g3_vielbein_sympy()
    ok_all = []
    ok_slash = []
    ok_offd = []
    ok_t4i = []
    for lab, pt in G.G3_POINTS.items():
        rng = random.Random(G3_SEEDS[lab])
        ej = G.vielbein_jet_from_sympy(emat, pt, 2, dom)
        geo = G.Geometry(ej, gd, dom, "G3_" + lab, curvature=False)
        # slash formula for a diagonal vielbein
        e0 = geo.e.value()
        half = dom.frac(1, 2)
        form = np.zeros((16, 16), dtype=object)
        for b in range(8):
            s = dom.zero
            for cix in range(8):
                if cix != b:
                    s = s + geo.e.coeff((b,))[cix, cix] / e0[cix, cix]
            form = form + gd.GAM[b] * (half * s / e0[b, b])
        ok_slash.append(G.arr_is_zero(geo.slash_omega() - form, dom))
        m = dom.conv(G.rand_rational(rng))
        lam = dom.conv(G.rand_rational(rng))
        psi = G.random_spinor_jet(rng, dom, 1, dirs=[G.TIME_INDEX])
        chi = G.random_spinor_jet(rng, dom, 1, dirs=[G.TIME_INDEX])
        psi, chi = G.solve_onshell(geo, psi, chi, m, lam, max_order=1)
        E, Eb, _ = G.field_equations(geo, psi, chi, m, lam)
        solved = G.arr_is_zero(E.value(), dom) and G.arr_is_zero(Eb.value(), dom)
        parts = G.emt_from_fields(geo, psi, chi, m, lam)
        T = parts["T"].value()
        S = parts["S"].value()[()]
        U = S * S * lam * half
        Up = S * lam
        g0 = geo.g.value()
        rho = T[4, 4]  # N = 1, u = d_4
        ok_rho = dom.is_zero(rho - (m * S + U))
        ok_p = all(dom.is_zero(T[i, i] - g0[i, i] * (S * Up - U)) for i in range(8) if i != 4)
        ginv0 = geo.ginv.value()
        pvals = [ginv0[i, i] * T[i, i] for i in range(8) if i != 4]
        ok_iso = all(dom.is_zero(pv - pvals[0]) for pv in pvals)
        # KE / PE split
        pb = parts["pb"].value()
        Dpsi = parts["Dpsi"].value()
        Dpb = parts["Dpb"].value()
        g4 = geo.gam.value()[4]
        KE = (pb.dot(g4).dot(Dpsi[4]) - Dpb[4].dot(g4).dot(psi.value())) * dom.frac(1, 4)
        PE = rho - KE
        ok_ke = dom.is_zero(KE - S * (m + Up) * half)
        ok_pe = dom.is_zero(PE - (m * S + 2 * U - S * Up) * half)
        ok_rp = dom.is_zero((KE + PE) - rho) and dom.is_zero((KE - PE) - pvals[0])
        # off-diagonal components
        h = [e0[i, i] for i in range(8)]
        hd = [geo.e.coeff((4,))[i, i] for i in range(8)]
        eps = [1, 1, 1, 1, -1, -1, -1, -1]
        GAM = gd.GAM
        okij = True
        for i in range(8):
            for j in range(8):
                if i == j or i == 4 or j == 4:
                    continue
                Hi, Hj = hd[i] / h[i], hd[j] / h[j]
                bil = pb.dot(GAM[i]).dot(GAM[j]).dot(GAM[4]).dot(psi.value())
                exp = bil * (Hi - Hj) * h[i] * h[j] * (eps[i] * eps[j]) * dom.frac(1, 4)
                okij = okij and dom.is_zero(T[i, j] - exp)
        ok4i = True
        dpsi4 = psi.coeff((4,))
        dpb4 = chi.coeff((4,)).dot(gd.C)
        for i in range(8):
            if i == 4:
                continue
            exp = (pb.dot(GAM[i]).dot(dpsi4) - dpb4.dot(GAM[i]).dot(psi.value())) * h[i] * eps[i] * dom.frac(-1, 4)
            ok4i = ok4i and dom.is_zero(T[4, i] - exp) and dom.is_zero(T[i, 4] - exp)
        ok_offd.append(okij and ok4i)
        ok_all.append(solved and ok_rho and ok_p and ok_iso and ok_ke and ok_pe and ok_rp)
        # on shell the time-space components vanish identically for homogeneous states
        n4i = sum(0 if dom.is_zero(T[4, i]) else 1 for i in range(8) if i != 4)
        nij = sum(0 if dom.is_zero(T[i, j]) else 1 for i in range(8) for j in range(8)
                  if i != j and i != 4 and j != 4)
        ok_t4i.append(n4i == 0)
        rec.measure("EMT_homogeneous_offDiagonalNonzeroCounts_G3_" + lab, {"T_4i": n4i, "T_ij": nij})
        rec.measure("EMT_homogeneous_G3_" + lab, {
            "x4": str(pt[4]), "m": qstr(m), "lambda": qstr(lam), "S": qstr(S), "rho": qstr(rho),
            "p": qstr(pvals[0]), "KE": qstr(KE), "PE": qstr(PE),
            "w": qstr(pvals[0] / rho) if rho != 0 else "undefined"})
    rec.measure("EMT_homogeneousReduction_diagonalPart_G3", all(ok_all))
    rec.measure("EMT_homogeneousReduction_offDiagonalForms_G3", all(ok_offd))
    rec.check("EMT_homogeneousReduction", all(ok_all) and all(ok_offd))
    rec.check("GEO_diagonalSlashFormula_G3", all(ok_slash))
    rec.check("EMT_homogeneousTimeSpaceVanishesOnShell_G3", all(ok_t4i))
    rec.measure("EMT_homogeneousReduction_offDiagonalFormulas_G3",
                "T_ij = +(1/4) eps_i eps_j h_i h_j (H_i - H_j) Psibar gamma^(i) gamma^(j) gamma^(4) Psi (i!=j, both !=4); "
                "T_4i = -(1/4) eps_i h_i (Psibar gamma^(i) d_4 Psi - d_4 Psibar gamma^(i) Psi); H_i = h_i'/h_i, "
                "gamma^(a) flat, eps = eta diagonal")


# ---------------------------------------------------------------------------
# EMT from the variation of the reduced action (symbolic diagonal metrics)
# ---------------------------------------------------------------------------


def run_emt_variation(rec: Recorder, local: bool):
    hs = sp.symbols("h0:8", positive=True)
    if local:
        dhs = {(mu, nu): sp.Symbol("dh%d_%d" % (mu, nu)) for mu in range(8) for nu in range(8)}
    else:
        dhs = {(mu, 4): sp.Symbol("hd%d" % mu) for mu in range(8)}
    gens = list(hs) + [dhs[k] for k in sorted(dhs)]
    K = QQ.frac_field(*gens)
    dom = G.ExactDomain(K, "QQ(h, dh)")
    gd = G.GammaData(dom)
    hv = [dom.conv(s) for s in hs]
    dhv = {k: dom.conv(v) for k, v in dhs.items()}
    ej = G.generic_diagonal_jet(hv, dhv, dom)
    geo = G.Geometry(ej, gd, dom, "diag", sqrtg_sign=1, curvature=False)
    tag = "diagonalLocal" if local else "minisuperspace"
    ok_nov, ok_T, ok_extra = [], [], []
    for seed in VAR_SEEDS:
        rng = random.Random(seed + (7 if local else 0))
        m = dom.conv(G.rand_rational(rng))
        lam = dom.conv(G.rand_rational(rng))
        dirs = None if local else [G.TIME_INDEX]
        psi = G.random_spinor_jet(rng, dom, 1, dirs=dirs)
        chi = G.random_spinor_jet(rng, dom, 1, dirs=dirs)
        parts = G.emt_from_fields(geo, psi, chi, m, lam)
        L = geo.sqrtg.value()[()] * parts["Ls"].value()[()]
        sg = geo.sqrtg.value()[()]
        # the reduced Lagrangian must not depend on the metric velocities
        nov = all(L.diff(dhv[k]) == 0 for k in dhv)
        ok_nov.append(nov)
        T = parts["T"].value()
        ginv0 = geo.ginv.value()
        okT = True
        for mu in range(8):
            Tmix_var = hv[mu] * L.diff(hv[mu]) / sg        # T^mu_mu from -(2/sqrt g) dS/dg^{mu mu}
            Tmix_cov = ginv0[mu, mu] * T[mu, mu]
            okT = okT and dom.is_zero(Tmix_var - Tmix_cov)
        ok_T.append(okT)
        # rho and p from lapse / scale-factor derivatives
        S = parts["S"].value()[()]
        U = S * S * lam * dom.frac(1, 2)
        rho_var = -hv[4] * L.diff(hv[4]) / sg                # rho = T_44 u^4 u^4 with u = d_4 / N
        rho_cov = T[4, 4] / (hv[4] * hv[4])
        extra = dom.is_zero(rho_var - rho_cov)
        if not local:
            # homogeneous: rho = m S + U and p_i = L_s off-shell
            extra = extra and dom.is_zero(rho_var - (m * S + U))
            Ls = parts["Ls"].value()[()]
            extra = extra and all(dom.is_zero(hv[i] * L.diff(hv[i]) / sg - Ls) for i in range(8) if i != 4)
        ok_extra.append(extra)
        if seed == VAR_SEEDS[0]:
            rec.measure("EMT_variation_%s_rho_seed%d" % (tag, seed), dom.to_str(rho_var))
            rec.measure("EMT_variation_%s_T11mixed_seed%d" % (tag, seed), dom.to_str(hv[1] * L.diff(hv[1]) / sg))
    rec.measure("EMT_variation_%s_noMetricVelocityDependence" % tag, all(ok_nov))
    rec.measure("EMT_variation_%s_diagonalTmixedAgree" % tag, all(ok_T))
    rec.measure("EMT_variation_%s_rhoAndPressure" % tag, all(ok_extra))
    rec.measure("EMT_variation_%s_setup" % tag,
                ("diagonal vielbein diag(h_0..h_7) with symbolic h_mu and symbolic d_nu h_mu (all nu)" if local else
                 "minisuperspace: diagonal vielbein diag(h_0..h_7)(x4), lapse N = h_4, symbolic h_mu and h_mu'; "
                 "homogeneous fields Psi(x4)") + "; exact random rational field jets, off-shell")
    return all(ok_nov) and all(ok_T) and all(ok_extra)


# ---------------------------------------------------------------------------
# Cross-implementation agreement with the Wolfram geometry report
# ---------------------------------------------------------------------------

WOLFRAM_REPORT_PATH = ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / "wolfram-geometry-report.json"
WOLFRAM_CHECK = "GEO_wolframAgreement"


def _mathematica_to_sympy(text: str):
    """Exact value of a Wolfram InputForm string such as "(3*Sqrt[455])/64" or "-2672/147"."""
    expr = str(text).strip().replace("Sqrt[", "sqrt(").replace("Log[", "log(").replace("]", ")")
    expr = expr.replace("^", "**")
    return sp.sympify(expr, rational=True)


def _python_expr_to_sympy(text: str, values: Dict[str, object]):
    """Exact value of a Python-report sympy string at the given symbol values (E is exp(a4),
    not Euler's number)."""
    names = ("w", "c", "E", "A1", "A2", "A3", "H")
    local = {name: sp.Symbol(name) for name in names}
    expr = sp.sympify(str(text), locals=local, rational=True)
    return expr.subs({local[name]: value for name, value in values.items()})


def _exact_equal(left, right) -> bool:
    difference = sp.nsimplify(sp.radsimp(sp.expand(sp.sympify(left) - sp.sympify(right))))
    return difference == 0


def _int_triple(text: str) -> List[int]:
    return [int(v) for v in str(text).replace("{", " ").replace("}", " ").replace("(", " ")
            .replace(")", " ").replace(",", " ").split()]


def _parse_g2_point(text: str) -> Dict[str, object]:
    """Wolfram G2.pX.point -> exact values of sin z, cos z, H, a4', a4'', a4'''."""
    fields = {}
    for part in str(text).split(", "):
        key, _, value = part.partition(" = ")
        fields[key.strip()] = value.strip()
    return {"sinz": _mathematica_to_sympy(fields["sin z"]), "c": _mathematica_to_sympy(fields["cos z"]),
            "w": _mathematica_to_sympy(fields["w"]), "H": _mathematica_to_sympy(fields["H"]),
            "A1": _mathematica_to_sympy(fields["a4'(t)"]), "A2": _mathematica_to_sympy(fields["a4''(t)"]),
            "A3": _mathematica_to_sympy(fields["a4'''(t)"])}


def _parse_notebook_slash(text: str):
    """"gamma^mu OmegaNotebook_mu = (x) gamma^0 + (y) gamma^4, residual zero: true" -> (x, y, residualZero)."""
    import re
    match = re.search(r"=\s*\((.*?)\)\s*gamma\^0\s*\+\s*\((.*?)\)\s*gamma\^4,\s*residual zero:\s*(\w+)", str(text))
    if not match:
        raise ValueError("unparsed notebook slash: " + str(text))
    return _mathematica_to_sympy(match.group(1)), _mathematica_to_sympy(match.group(2)), match.group(3) == "true"


def _normalized(text: str) -> str:
    return (str(text).replace(" ", "").replace("(S)", "").replace("lambda", "lam"))


def compare_with_wolfram(py_checks: Dict[str, bool], py_meas: Dict[str, object], wolfram_doc: Dict[str, object]):
    """Compare every measurement both geometry verifiers compute.  Returns (ok, rows, verdicts).

    G1 is compared point by point (same three rational points, exact values).  G2 is compared by
    evaluating the Python (fully symbolic) results at the three exact Wolfram points.  The random
    field data and the parameters m, lambda differ between the implementations, so field-dependent
    values (EMT traces, rho, p, ...) are compared only through the formulas both verify."""
    wm = wolfram_doc.get("measurements", {}) if isinstance(wolfram_doc.get("measurements"), dict) else {}
    wc = wolfram_doc.get("checks", {}) if isinstance(wolfram_doc.get("checks"), dict) else {}
    rows = []

    def add(label, wolfram_value, python_value, agree):
        rows.append({"measurement": label, "wolfram": str(wolfram_value), "python": str(python_value),
                     "agree": bool(agree)})

    def guarded(label, function):
        try:
            function()
        except (KeyError, TypeError, ValueError, AttributeError, sp.SympifyError) as error:
            rows.append({"measurement": label, "agree": False, "error": "%s: %s" % (type(error).__name__, error)})

    # --- G1: same points, exact rational values -----------------------------------------------------
    for lab in ("p1", "p2", "p3"):
        wp, tag = "G1.%s." % lab, "G1_" + lab

        def g1_point(lab=lab, wp=wp, tag=tag):
            wcoords = [sp.Rational(v) for v in _int_free_split(wm[wp + "coordinates"])]
            pcoords = [sp.Rational(v) for v in py_meas["G1_points"][lab]]
            add(tag + " coordinates", wcoords, pcoords, wcoords == pcoords)
            det_w, det_p = sp.Rational(wm[wp + "detFrame"]), sp.Rational(py_meas["GEO_detVielbein_" + tag])
            add(tag + " det e", det_w, det_p, det_w == det_p)
            sq_w = sp.Rational(wm[wp + "sqrtAbsG"])
            add(tag + " sqrt|g| = |det e|", sq_w, abs(det_p), sq_w == abs(det_p))
            add(tag + " metric inertia", wm[wp + "metricInertia"], py_meas["GEO_metricSignature_" + tag],
                _int_triple(wm[wp + "metricInertia"]) == _int_triple(py_meas["GEO_metricSignature_" + tag]))
            g44_w, g44_p = sp.Rational(wm[wp + "inverseMetric44"]), sp.Rational(py_meas["GEO_inverseMetric44_" + tag])
            add(tag + " g^44", g44_w, g44_p, g44_w == g44_p)
            r_w, r_p = sp.Rational(wm[wp + "scalarCurvature"]), sp.Rational(py_meas["GEO_ricciScalar_" + tag])
            add(tag + " R", r_w, r_p, r_w == r_p)
        guarded(tag + " point data", g1_point)

    # --- counts, Lichnerowicz constant and curvature convention (G1 points and G2 points) ------------
    point_tags = [("G1.%s." % lab, "G1_" + lab) for lab in ("p1", "p2", "p3")] + \
                 [("G2.%s." % lab, "G2") for lab in ("p1", "p2", "p3")]
    for wp, tag in point_tags:
        label = wp.rstrip(".")

        def counts(wp=wp, tag=tag, label=label):
            for wkey, pkey in (("nonzeroOmegaLower", "GEO_nonzeroOmegaLowComponents_"),
                               ("nonzeroOmegaMixedSymmetricPart", "GEO_nonzeroOmegaMixedSymmetricPart_"),
                               ("notebookDGammaNonzeroEntries", "GEO_notebookContraction_nonzeroEntries_DmuGammaNu_")):
                add("%s %s" % (label, wkey), wm[wp + wkey], py_meas[pkey + tag], int(wm[wp + wkey]) == int(py_meas[pkey + tag]))
            c_w, c_p = sp.Rational(wm[wp + "lichnerowiczC"]), sp.Rational(py_meas["GEO_lichnerowicz_c_" + tag])
            add(label + " Lichnerowicz c", c_w, c_p, c_w == c_p)
            add(label + " Lichnerowicz c = +1/4 fails", wm[wp + "lichnerowiczPlusQuarterHolds"], "c unique",
                wm[wp + "lichnerowiczPlusQuarterHolds"] in (False, "false"))
            for wkey, pkey in (("curvatureCandidate.plusHalfLowered", "GEO_curvature_spinCurvaturePlusHalfRiemannS_"),
                               ("curvatureCandidate.minusHalfLowered", "GEO_curvature_spinCurvatureMinusHalfRiemannS_")):
                wv = wm[wp + wkey] in (True, "true")
                add("%s %s" % (label, wkey), wv, py_meas[pkey + tag], wv == bool(py_meas[pkey + tag]))
        guarded(label + " counts", counts)

    # --- G2: Python symbolic results evaluated at the exact Wolfram points --------------------------
    for lab in ("p1", "p2", "p3"):
        wp = "G2.%s." % lab

        def g2_point(lab=lab, wp=wp):
            pt = _parse_g2_point(wm[wp + "point"])
            add("G2.%s sin^2 z + cos^2 z = 1 and sin z = w^6" % lab, (pt["sinz"], pt["c"]), "identity",
                _exact_equal(pt["sinz"] ** 2 + pt["c"] ** 2, 1) and _exact_equal(pt["w"] ** 6, pt["sinz"]))
            values = {"c": pt["c"], "w": pt["w"], "H": pt["H"], "A1": pt["A1"], "A2": pt["A2"], "A3": pt["A3"]}
            sq_w = _mathematica_to_sympy(wm[wp + "sqrtAbsG"])
            sq_p = _python_expr_to_sympy(py_meas["GEO_sqrtg_G2"], values)
            add("G2.%s sqrt|g|" % lab, sq_w, sq_p, _exact_equal(sq_w, sq_p))
            add("G2.%s det e = sqrt|g|" % lab, wm[wp + "detFrame"], sq_p, _exact_equal(_mathematica_to_sympy(wm[wp + "detFrame"]), sq_p))
            r_w = _mathematica_to_sympy(wm[wp + "scalarCurvature"])
            r_p = _python_expr_to_sympy(py_meas["GEO_ricciScalar_G2"], values)
            add("G2.%s R" % lab, r_w, r_p, _exact_equal(r_w, r_p))
            x_w, y_w, residual_zero = _parse_notebook_slash(wm[wp + "notebookSlash"])
            coefficients = py_meas["GEO_slashOmega_notebook_coefficients_G2"]
            x_p = _python_expr_to_sympy(coefficients["gamma0"], values)
            y_p = _python_expr_to_sympy(coefficients["gamma4"], values)
            add("G2.%s notebook gamma^mu Omega_mu, gamma^0 coefficient" % lab, x_w, x_p, _exact_equal(x_w, x_p))
            add("G2.%s notebook gamma^mu Omega_mu, gamma^4 coefficient" % lab, y_w, y_p, _exact_equal(y_w, y_p))
            add("G2.%s notebook gamma^mu Omega_mu residual" % lab, residual_zero, coefficients["residualNonzero"],
                residual_zero and int(coefficients["residualNonzero"]) == 0)
        guarded("G2.%s point data" % lab, g2_point)

    # --- conventions both implementations verify ------------------------------------------------------
    def conventions():
        import re
        match = re.search(r"c = (-?\d+/\d+)", str(wm["convention.lichnerowicz"]))
        c_conv = sp.Rational(match.group(1)) if match else None
        c_py = {sp.Rational(py_meas["GEO_lichnerowicz_c_G1"]), sp.Rational(py_meas["GEO_lichnerowicz_c_G2"])}
        add("Lichnerowicz constant (convention statements)", c_conv, sorted(c_py), c_py == {c_conv})
        formula = "T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu}"
        add("EMT sign convention", formula in str(wm["emt.signConvention"]), formula in str(py_meas["EMT_signConvention"]),
            formula in str(wm["emt.signConvention"]) and formula in str(py_meas["EMT_signConvention"]))
        tokens = ("T^mu_mu=-mS+7SU'-8U", "=-mS+3lamS^2")
        w_trace, p_trace = _normalized(wm["emt.trace"]), _normalized(py_meas["EMT_traceStatement"])
        add("EMT on-shell trace formula", w_trace, p_trace,
            all(token.replace("T^mu_mu=", "") in w_trace for token in tokens)
            and all(token.replace("T^mu_mu=", "") in p_trace for token in tokens))
    guarded("conventions", conventions)

    shared = sorted(set(wc) & set(py_checks))
    verdicts = {name: {"wolfram": wc[name] is True, "python": bool(py_checks[name])} for name in shared}
    disagreeing = sorted(name for name, pair in verdicts.items() if pair["wolfram"] != pair["python"])
    ok = bool(rows) and all(row["agree"] for row in rows) and bool(shared) and not disagreeing
    return ok, rows, {"shared": shared, "disagreeing": disagreeing}


def _int_free_split(text: str) -> List[str]:
    """"{1/7, -2/9, ...}" -> ["1/7", "-2/9", ...]."""
    return [part.strip() for part in str(text).strip().strip("{}").split(",") if part.strip()]


def run_wolfram_agreement(rec: Recorder, report_path) -> None:
    if not report_path or not Path(report_path).exists():
        rec.measure("GEO_wolframAgreement", "not-run")
        return
    data = Path(report_path).read_bytes()
    rec.measure("GEO_wolframReportSha256", hashlib.sha256(data).hexdigest())
    try:
        document = json.loads(data.decode("utf-8"))
    except ValueError:
        rec.measure("GEO_wolframReportParses", False)
        rec.check(WOLFRAM_CHECK, False)
        return
    ok, rows, verdicts = compare_with_wolfram(dict(rec.checks), rec.meas, document)
    rec.measure("GEO_wolframSharedMeasurementCount", len(rows))
    rec.measure("GEO_wolframSharedMeasurementsAgreeing", sum(1 for row in rows if row["agree"]))
    rec.measure("GEO_wolframSharedMeasurementDisagreements", [row for row in rows if not row["agree"]])
    rec.measure("GEO_wolframSharedMeasurements", rows)
    rec.measure("GEO_wolframCheckNamesShared", verdicts["shared"])
    rec.measure("GEO_wolframCheckVerdictDisagreements", verdicts["disagreeing"])
    rec.check(WOLFRAM_CHECK, ok)


def sha256_of(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def main(argv=None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--wolfram-report", default=str(WOLFRAM_REPORT_PATH),
                        help="Wolfram geometry report to compare with (GEO_wolframAgreement); "
                             "an empty value skips the comparison")
    arguments = parser.parse_args(argv)
    t0 = time.time()
    rec = Recorder()
    dom = G.make_qq_domain()
    gd = G.GammaData(dom)
    def stamp(label):
        print("[%7.1f s] %s" % (time.time() - t0, label), file=sys.stderr, flush=True)

    run_algebra(rec, gd, dom)
    stamp("algebra done")
    c1 = run_g1(rec, gd, dom)
    stamp("G1 done")
    c2 = run_g2(rec)
    stamp("G2 done")
    rec.check("GEO_lichnerowiczConstantSameG1G2", c1 == c2 and c1 is not None)
    run_g3(rec, gd, dom)
    stamp("G3 done")
    v1 = run_emt_variation(rec, local=False)
    stamp("EMT variation (minisuperspace) done")
    v2 = run_emt_variation(rec, local=True)
    stamp("EMT variation (diagonal local) done")
    rec.check("EMT_variation", v1 and v2)
    rec.measure("GEO_lichnerowicz_statement",
                "(gamma^mu D_mu)^2 Psi = g^{mu nu} nabla_mu D_nu Psi + c R Psi with c = %s; "
                "R = g^{sn} R^r_{s r n}, R^r_{s m n} = d_m Gamma^r_{ns} - d_n Gamma^r_{ms} + "
                "Gamma^r_{ml} Gamma^l_{ns} - Gamma^r_{nl} Gamma^l_{ms}" % c1)
    rec.measure("GEO_spinCurvature_statement",
                "F_{mu nu} = d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu] = (1/2) R_{ab mu nu} S^{ab}, "
                "R_{ab mu nu} = eta_ac e_r^c R^r_{s mu nu} e_b^s")
    rec.measure("EMT_signConvention",
                "T_{mu nu} = -(2/sqrt|g|) dS/dg^{mu nu} reproduces CONTRACT section 7 exactly: "
                "T^mu_mu(no sum) = (h_mu/sqrt|g|) dL/dh_mu for diagonal e = diag(h); rho = T_44/N^2 = "
                "-(N/sqrt|g|) dL/dN; p_i = T^i_i = (h_i/sqrt|g|) dL/dh_i; homogeneous: rho = m S + U, p = L_s "
                "(= S U' - U on shell)")
    rec.measure("EMT_traceStatement", "T^mu_mu = 7 K - 8 (m S + U) off shell; on shell T^mu_mu = -m S + 7 S U' - 8 U "
                                      "(= -m S + 3 lam S^2 for U = lam S^2/2)")
    rec.measure("LAG_commutingProxyJustification", LEGITIMACY_NOTE)
    rec.measure("seeds", {"G1": G1_SEEDS, "G2": G2_SEEDS, "G3": G3_SEEDS, "variation": VAR_SEEDS})
    rec.measure("G1_points", {k: [str(v) for v in pt] for k, pt in G.G1_POINTS.items()})
    rec.measure("G3_points_x4", {k: str(pt[4]) for k, pt in G.G3_POINTS.items()})
    # last: compares the finished Python results with the Wolfram geometry report
    run_wolfram_agreement(rec, arguments.wolfram_report)
    stamp("Wolfram agreement done")

    report = {
        "schemaVersion": 1,
        "producer": "scripts/check_dirac16complex_geometry.py (python %s, sympy %s, numpy %s)" % (
            sys.version.split()[0], sp.__version__, np.__version__),
        "checks": rec.checks,
        "measurements": rec.meas,
        "sourceSha256": {rel: sha256_of(rel) for rel in SOURCES},
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(report, indent=2, sort_keys=False, ensure_ascii=True) + "\n"
    REPORT_PATH.write_bytes(data.encode("utf-8"))
    for k, v in rec.checks.items():
        print("check_%s=%s" % (k, "true" if v else "false"))
    for k, v in rec.meas.items():
        if isinstance(v, (dict, list)):
            v = json.dumps(v, sort_keys=False, ensure_ascii=True)
        print("measurement_%s=%s" % (k, v))
    failed = [k for k, v in rec.checks.items() if not v]
    print("check_count=%d" % len(rec.checks))
    print("failed_check_count=%d" % len(failed))
    print("runtime_seconds=%.1f" % (time.time() - t0), file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
