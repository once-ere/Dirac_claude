#!/usr/bin/env python3
"""Revision/theory/python/check_field_theory.py - independent exact sympy verification of the field theory
of dirac16complex (Grassmann) and dirac16complex00 (commuting) in the author's primordial metric
(Revision/SPEC.md sections 1-6), written anew (no shared code with Revision/theory/wolfram, nothing from
the old stages).  Writes Revision/theory/reports/python-field-theory.json (deterministic, LF).

Usage:  python Revision/theory/python/check_field_theory.py [--out PATH]
"""

import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from superalg import Alg, gen, CHI, PSI, THETA  # noqa: E402
from geometry import (ETA, X4, X8, E, s, c, A1, A2, H, m, lam, cd_author, f_author, zero_author,  # noqa: E402
                      canon_author, to_physical, generic_ring, zero_generic, Geometry)
from fields import Spinors  # noqa: E402
import gammas_io  # noqa: E402
from quantum import make_vev  # noqa: E402
import compare_wolfram  # noqa: E402
from emt_vielbein import linear_variation_T  # noqa: E402

REV = gammas_io.REV
OUT = os.path.join(REV, "theory", "reports", "python-field-theory.json")
COORD = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
STATS = {"grassmann": "dirac16complex (anticommuting, Grassmann)",
         "commuting": "dirac16complex00 (commuting)"}

CHECKS = []
FORMULAS = {}
T0 = time.time()


def check(name, ok, detail, section):
    CHECKS.append({"name": name, "section": section, "verdict": "pass" if ok else "fail", "detail": detail})
    print(f"[{time.time() - T0:7.1f}s] {'PASS' if ok else 'FAIL'} {name}", flush=True)


def phys(expr):
    return sp.sstr(to_physical(canon_author(expr)))


def ring(expr):
    return sp.sstr(canon_author(expr))


def mzero(M, zt=zero_author):
    return all(zt(x) for x in M)


def alg_zero(x, zt=zero_author):
    return x.is_zero(zt)[0]


def mat_in_S(M, Smat):
    """Write a matrix as sum_{a<b} k_ab S^ab (exact) or None."""
    terms = []
    R = M
    for a in range(8):
        for b in range(a + 1, 8):
            # tr(S^ab S^ab) = -16/4 eta^aa eta^bb  ->  k = -tr(M S^ab) / (4 eta_a eta_b)
            k = sp.expand((M * Smat[a][b]).trace() / (-4 * ETA[a] * ETA[b]))
            if k != 0:
                terms.append((a, b, k))
                R = R - k * Smat[a][b]
    if not mzero(R):
        return None
    return terms


# ====================================================================================== A. gammas
def section_gammas():
    sec = "A. gamma matrices (Revision/algebra/gammas.json)"
    gm = gammas_io.load()
    G, Cm, Gam, B, S = gm["gamma"], gm["C"], gm["Gamma"], gm["B"], gm["S"]
    I16 = sp.eye(16)
    check("gammas_coordinates_and_eta", gm["coordinates"] == COORD and gm["eta"] == ETA,
          "gammas.json lists x1..x8 and eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) (SPEC section 2)", sec)
    if os.path.exists(gammas_io.PY_GAMMAS):
        with open(gammas_io.PY_GAMMAS, encoding="utf-8") as fh:
            pg = json.load(fh)
        ok = [gammas_io._mat(pg["gamma"][a]) for a in range(8)] == G
        ok = ok and gammas_io._mat(pg["C"]) == Cm and gammas_io._mat(pg["Gamma"]) == Gam
        ok = ok and gammas_io._mat(pg["B"]) == B and [int(x) for x in pg["eta"]] == ETA
        for a in range(8):
            for b in range(a + 1, 8):
                ok = ok and gammas_io._mat(pg["S"][f"{COORD[a]},{COORD[b]}"]) == S[a][b]
        check("gammas_json_equals_python_construction", ok,
              "every gamma^a, C, Gamma, B and S^ab (a<b) of Revision/algebra/gammas.json (Wolfram construction) "
              "equals Revision/algebra/reports/python-gammas.json (independent Python construction) exactly", sec)
    else:
        check("gammas_json_equals_python_construction", False, "python-gammas.json missing", sec)
    bad = [(a, b) for a in range(8) for b in range(8)
           if G[a] * G[b] + G[b] * G[a] != 2 * (ETA[a] if a == b else 0) * I16]
    check("clifford_relations", not bad, "{gamma^a, gamma^b} = 2 eta^ab I16 for all 64 pairs (exact)", sec)
    check("gammas_real", all(x.is_real for g in G for x in g), "all 8 gamma^a are real", sec)
    sym = ["sym" if g.T == g else ("antisym" if g.T == -g else "none") for g in G]
    check("gamma_symmetry_pattern", sym == ["sym"] * 3 + ["antisym"] * 4 + ["sym"],
          f"gamma^a symmetric for space-like a (x1,x2,x3,x8), antisymmetric for time-like a (x4..x7): {sym}", sec)
    Cc = G[7] * G[0] * G[1] * G[2]
    ok = Cm == Cc and Cm.T == Cm and Cm * Cm == I16 and all(x.is_real for x in Cm)
    ok = ok and all((Cm * g).T == -(Cm * g) for g in G)
    check("C_properties", ok, "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3); C real symmetric, C^2 = 1, "
          "C gamma^a real antisymmetric for all a (equivalently gamma^aT C = -C gamma^a)", sec)
    ok = all((Cm * S[a][b]).T == -(Cm * S[a][b]) for a in range(8) for b in range(8))
    ok = ok and all(S[a][b] == (G[a] * G[b] - G[b] * G[a]) / 4 for a in range(8) for b in range(8))
    check("S_definition_and_C_S_antisymmetric", ok,
          "S^ab = (1/4)[gamma^a, gamma^b] and C S^ab antisymmetric (S^abT C = -C S^ab) for all a, b", sec)
    P = G[7]
    for a in range(7):
        P = P * G[a]
    dg = sp.diag(*([-1] * 8 + [1] * 8))
    check("chirality_Gamma", Gam == P and Gam == dg,
          "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = diag(-I8, I8)", sec)
    Bc = -sp.I * Cm * G[3]
    ok = B == Bc and B.H == B and B * B == I16 and B.trace() == 0
    check("B_properties", ok, "B = -i C gamma^(x4); B Hermitian, B^2 = 1, tr B = 0, hence eigenvalues +1 and -1 "
          "with multiplicity 8 each: signature (8,8)", sec)
    return gm


# ====================================================================================== B. geometry
def section_geometry(gm):
    sec = "B. vielbein, Christoffel symbols, canonical spin connection (author's metric)"
    G, S = gm["gamma"], gm["S"]
    f = f_author()
    geo = Geometry(f, cd_author)
    geo.spin_matrices(S)
    geo.curved_gammas(G)
    x4, x8 = sp.symbols("x4 x8", real=True)
    a4 = sp.Function("a4")(x4)
    z = 6 * H * x8
    spec = [sp.exp(2 * a4) * sp.sin(z) ** sp.Rational(1, 3)] * 3 + [-1] + \
           [-sp.exp(-2 * a4) * sp.sin(z) ** sp.Rational(1, 3)] * 3 + [sp.cot(z) ** 2]
    ok = all(sp.simplify(to_physical(geo.g[a]) - spec[a]) == 0 for a in range(8))
    check("metric_from_vielbein_equals_SPEC", ok,
          "e^a_mu = sqrt|g_mumu| delta^a_mu reproduces g of SPEC section 1 exactly: "
          + "; ".join(f"g_{COORD[a]}{COORD[a]} = {sp.sstr(spec[a])}" for a in range(8)), sec)
    check("sqrt_det_g_equals_cos_z", sp.simplify(to_physical(geo.sqrtg) - sp.cos(z)) == 0,
          f"sqrt|det g| = product of the f_a = {sp.sstr(geo.sqrtg)} (ring) = cos(6 H x8)", sec)
    FORMULAS["vielbein_f"] = {COORD[a]: phys(f[a]) for a in range(8)}
    FORMULAS["sqrt_abs_det_g"] = "cos(6*H*x8)"
    FORMULAS["ring_notation"] = ("E = exp(a4(x4)), s = sin(6 H x8)^(1/6), c = cos(6 H x8), A1 = a4', A2 = a4''; "
                                 "physical forms substitute these")
    # Christoffels
    chr_list = {}
    for l in range(8):
        for a in range(8):
            for b in range(a, 8):
                if geo.Gam[l][a][b] != 0:
                    chr_list[f"Gamma^{COORD[l]}_{COORD[a]}{COORD[b]}"] = phys(geo.Gam[l][a][b])
    FORMULAS["christoffel_nonzero"] = chr_list
    ok = all(sp.expand(geo.Gam[l][a][b] - geo.Gam[l][b][a]) == 0 for l in range(8) for a in range(8) for b in range(8))
    # metric compatibility nabla_mu g_ab = 0
    for mu in range(8):
        for a in range(8):
            v = cd_author(geo.g[a], mu) - 2 * geo.Gam[a][mu][a] * geo.g[a]
            ok = ok and zero_author(v)
    check("christoffel_symmetric_metric_compatible", ok,
          f"Gamma^l_ab = Gamma^l_ba and nabla_mu g_ab = 0; {len(chr_list)} independent nonzero symbols", sec)
    # spin connection: antisymmetry, vielbein postulate
    ok = all(zero_author(geo.om[mu][a][b] + geo.om[mu][b][a]) for mu in range(8) for a in range(8) for b in range(8))
    check("spin_connection_antisymmetric", ok, "omega_mu ab = eta_ac omega_mu^c_b = -omega_mu ba (all mu, a, b)", sec)
    ok = True
    for mu in range(8):
        for a in range(8):
            for nu in range(8):
                v = (cd_author(f[a], mu) if a == nu else 0) - geo.Gam[a][mu][nu] * f[a]
                v += geo.om_mixed[mu][a][nu] * f[nu]
                ok = ok and zero_author(v)
    check("vielbein_postulate", ok,
          "d_mu e^a_nu - Gamma^l_mu nu e^a_l + omega_mu^a_b e^b_nu = 0 for all mu, a, nu (512 components)", sec)
    oml = {}
    for mu in range(8):
        for a in range(8):
            for b in range(a + 1, 8):
                if geo.om[mu][a][b] != 0:
                    oml[f"omega_{COORD[mu]} {COORD[a]}{COORD[b]}"] = phys(geo.om[mu][a][b])
    FORMULAS["spin_connection_omega_mu_ab_nonzero_a<b"] = oml
    omf = {}
    for mu in range(8):
        terms = mat_in_S(geo.Om[mu], S)
        omf[COORD[mu]] = " + ".join(f"({phys(k)})*S^({COORD[a]},{COORD[b]})" for a, b, k in terms) if terms else "0"
    FORMULAS["Omega_mu"] = omf
    check("Omega_x4_and_Omega_x8_vanish", geo.Om[X4] == sp.zeros(16, 16) and geo.Om[X8] == sp.zeros(16, 16),
          "Omega_(x4) = Omega_(x8) = 0 identically (the diagonal vielbein makes omega_mu ab nonzero only for mu in "
          "{a, b} with the other index x4 or x8); Omega_(xi) = " + omf["x1"] + " for i = 1,2,3; Omega_(x5,x6,x7) "
          "analogous: " + omf["x5"], sec)
    # D_mu gamma^nu = 0
    ok = True
    for mu in range(8):
        for nu in range(8):
            M = geo.gam[nu].applyfunc(lambda x: cd_author(x, mu))
            for l in range(8):
                if geo.Gam[nu][mu][l] != 0:
                    M += geo.Gam[nu][mu][l] * geo.gam[l]
            M += geo.Om[mu] * geo.gam[nu] - geo.gam[nu] * geo.Om[mu]
            ok = ok and mzero(M)
    check("covariant_constancy_D_mu_gamma_nu", ok,
          "D_mu gamma^nu = d_mu gamma^nu + Gamma^nu_mu l gamma^l + [Omega_mu, gamma^nu] = 0 for all 64 (mu, nu)", sec)
    # gamma^mu Omega_mu
    tot = sp.zeros(16, 16)
    decomp = {}
    for mu in range(8):
        Mm = (geo.gam[mu] * geo.Om[mu]).applyfunc(sp.expand)
        tot += Mm
        al = sp.expand(-(Mm * G[3]).trace() / 16)  # coefficient of gamma^(x4): tr(g4 g4) = -16
        be = sp.expand((Mm * G[7]).trace() / 16)
        okd = mzero(Mm - al * G[3] - be * G[7])
        decomp[COORD[mu]] = (al, be, okd)
    okt = mzero(tot - 3 * H * G[7])
    check("gamma_mu_Omega_mu_equals_3H_gamma_x8", okt,
          "gamma^mu Omega_mu = 3 H gamma^(x8) exactly (independent of a4 and of x4, x8)", sec)
    infl = sp.expand(sum(decomp[COORD[i]][0] for i in range(3)))
    defl = sp.expand(sum(decomp[COORD[i]][0] for i in range(4, 7)))
    hid = sp.expand(sum(decomp[COORD[i]][1] for i in range(8)))
    ok = all(d[2] for d in decomp.values()) and sp.expand(infl - sp.Rational(3, 2) * A1) == 0 \
        and sp.expand(defl + sp.Rational(3, 2) * A1) == 0 and sp.expand(hid - 3 * H) == 0
    ok = ok and all(sp.expand(decomp[COORD[i]][1] - H / 2) == 0 for i in (0, 1, 2, 4, 5, 6))
    check("time_terms_cancel_hidden_term_survives", ok,
          "per direction gamma^(xi) Omega_(xi) = (1/2) a4' gamma^(x4) + (H/2) gamma^(x8) for the inflating i = 1,2,3 "
          "and = -(1/2) a4' gamma^(x4) + (H/2) gamma^(x8) for the deflating extra times i = 5,6,7; the x4 terms "
          f"cancel (inflating sum {infl}, deflating sum {defl}); the six hidden-direction terms add to {hid} gamma^(x8)",
          sec)
    FORMULAS["gamma_mu_Omega_mu"] = "3*H*gamma^(x8)"
    FORMULAS["gamma_xi_Omega_xi"] = {COORD[i]: f"({phys(decomp[COORD[i]][0])})*gamma^(x4) + "
                                     f"({phys(decomp[COORD[i]][1])})*gamma^(x8)" for i in range(8)}
    anti = sp.zeros(16, 16)
    for mu in range(8):
        anti += geo.gam[mu] * geo.Om[mu] + geo.Om[mu] * geo.gam[mu]
    check("anticommutator_gamma_Omega_vanishes", mzero(anti),
          "sum_mu {gamma^mu, Omega_mu} = 0: only the totally antisymmetric part of omega enters the symmetric "
          "Lagrangian and it vanishes for this diagonal vielbein; gravity enters L through e^mu_a and sqrt|g|, and "
          "the field equation through gamma^mu Omega_mu = 3 H gamma^(x8) = (1/2)(1/sqrt|g|) d_mu(sqrt|g| e^mu_a) gamma^a",
          sec)
    # (1/2)(1/sqrtg) d_mu (sqrtg gamma^mu) = gamma^mu Omega_mu - (1/2){...} : check the identity directly
    M = sp.zeros(16, 16)
    for mu in range(8):
        M += (geo.gam[mu] * geo.sqrtg).applyfunc(lambda x: cd_author(x, mu))
    check("divergence_of_sqrtg_gamma", mzero(M / geo.sqrtg / 2 - 3 * H * G[7]),
          "(1/2)(1/sqrt|g|) d_mu(sqrt|g| gamma^mu) = 3 H gamma^(x8) = gamma^mu Omega_mu", sec)
    # Non-triviality: Omega vanishes iff a4' = 0 and H = 0
    ok = True
    lin = []
    for i in (0, 4):
        terms = mat_in_S(geo.Om[i], S)
        cfs = {(a, b): k for a, b, k in terms}
        lin.append(cfs)
    # coefficients: S^(xi x4) carries a4' only, S^(xi x8) carries H only
    c14, c18 = lin[0][(0, 3)], lin[0][(0, 7)]
    c54, c58 = lin[1][(3, 4)], lin[1][(4, 7)]
    ok = sp.expand(c14 / A1).free_symbols <= {E, s} and sp.expand(c18 / H).free_symbols <= {E, s}
    ok = ok and sp.expand(c54 / A1).free_symbols <= {E, s} and sp.expand(c58 / H).free_symbols <= {E, s}
    check("nontriviality_Omega_zero_iff_flat", ok,
          f"Omega_(x1) = ({ring(c14)}) S^(x1,x4) + ({ring(c18)}) S^(x1,x8), Omega_(x5) = ({ring(c54)}) S^(x4,x5) + "
          f"({ring(c58)}) S^(x5,x8): the S^ab are linearly independent and E = e^a4 > 0, s > 0 on 0 < z < pi/2, so "
          "every Omega_mu vanishes iff a4' = 0 AND H = 0 (formal flat limit with s, c frozen; at H = 0 the metric "
          "itself degenerates since sin(6 H x8) = 0, so within the author's family the spin connection never "
          "vanishes); the field-equation term gamma^mu Omega_mu = 3 H gamma^(x8) is nonzero for every H > 0", sec)
    return geo


# ====================================================================================== C. curvature, integrability
def section_curvature(gm, geo):
    sec = "C. curvature, integrability (Lichnerowicz)"
    G, S = gm["gamma"], gm["S"]
    geo.riemann()
    R = geo.Rscalar
    FORMULAS["ricci_scalar"] = phys(R)
    R0 = canon_author(R.subs({A1: 0, A2: 0}))
    flatR = all(sp.expand(v.subs({A1: 0, A2: 0, H: 0})) == 0 for v in geo.R.values())
    check("curvature_nonzero_flat_only_formally", (not zero_author(R0)) and flatR,
          f"Ricci scalar R = {ring(R)} (ring); for a4 = const R = {ring(R0)} which is nonzero for H > 0: the metric "
          "is curved for every member of the family; every Riemann component vanishes only in the formal limit "
          "a4' = a4'' = 0, H = 0 (flat 4+4)", sec)
    # spinor curvature F_mu nu = (1/4) R_{rho sigma mu nu} gamma^rho gamma^sigma
    ok = True
    gg = sp.zeros(16, 16)
    for mu in range(8):
        for nu in range(8):
            if mu == nu:
                continue
            F = geo.Om[nu].applyfunc(lambda x: cd_author(x, mu)) - geo.Om[mu].applyfunc(lambda x: cd_author(x, nu))
            F += geo.Om[mu] * geo.Om[nu] - geo.Om[nu] * geo.Om[mu]
            Rm = sp.zeros(16, 16)
            for r in range(8):
                for sg in range(8):
                    v = geo.R.get((r, sg, mu, nu))
                    if v is not None:
                        Rm += geo.g[r] * v * geo.gam[r] * geo.gam[sg] / 4
            ok = ok and mzero(F - Rm)
            gg += geo.gam[mu] * geo.gam[nu] * F
    check("spinor_curvature_equals_riemann", ok,
          "[D_mu, D_nu] = F_mu nu = d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu] = (1/4) R_{rho sigma mu nu} "
          "gamma^rho gamma^sigma for all mu != nu (integrability of the spin connection; "
          "R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - ...)", sec)
    check("lichnerowicz_contraction", mzero(gg + R / 2 * sp.eye(16)),
          "gamma^mu gamma^nu F_mu nu = -(R/2) I16 exactly", sec)
    # second-order (Lichnerowicz) identity on the jet space: (gamma^mu D_mu)^2 Psi = Box Psi - (R/4) Psi
    sps = Spinors("grassmann", geo, G, gm["C"], m, 0)
    ps = sps.psi()

    def Dvec(v, mu):
        return sps.vadd([x.total(mu, cd_author) for x in v], sps.matvec(geo.Om[mu], v))

    def dslash(v):
        out = [sps.zero() for _ in range(16)]
        for mu in range(8):
            out = sps.vadd(out, sps.matvec(geo.gam[mu], Dvec(v, mu)))
        return out

    D2 = dslash(dslash(ps))
    box = [sps.zero() for _ in range(16)]
    Dps = [Dvec(ps, mu) for mu in range(8)]
    for mu in range(8):
        t = Dvec(Dps[mu], mu)
        for l in range(8):
            if geo.Gam[l][mu][mu] != 0:
                t = [a - b.scale(geo.Gam[l][mu][mu]) for a, b in zip(t, Dps[l])]
        box = sps.vadd(box, sps.vscale(t, geo.ginv[mu]))
    ok = all(alg_zero((D2[A] - box[A] + ps[A].scale(R / 4)).expand()) for A in range(16))
    check("lichnerowicz_identity_on_fields", ok,
          "(gamma^mu D_mu)^2 Psi = g^{mu nu} nabla_mu D_nu Psi - (R/4) Psi identically on the jet space: the "
          "first-order operator squares to the second-order one with the curvature term -R/4, R = 6(a4'^2 - 7 H^2) "
          "(integrability of the Dirac-type equation in this metric)", sec)


# ====================================================================================== D. Lagrangian, EL, current
def onshell_rule(sps, geo, stat, LAM, homogeneous=False):
    """Prolonged on-shell substitution: psi_{,4...} from gamma^mu D_mu Psi = (m + lam S) Psi, chi by conjugation."""
    G4 = sps.G[X4]
    Mp = Alg.scalar(stat, m) + sps.S().scale(LAM)
    rhs = [sps.zero() for _ in range(16)]
    for mu in range(8):
        if mu != X4:
            rhs = sps.vadd(rhs, sps.matvec(geo.gam[mu], sps.Dpsi(mu)))
    ps = sps.psi()
    inner = [Mp * ps[A] - rhs[A] for A in range(16)]
    # gamma^(x4) has f_x4 = 1; (gamma^(x4))^{-1} = -gamma^(x4)
    R = [(a - b).expand() for a, b in zip(sps.matvec(-G4, inner), sps.matvec(geo.Om[X4], ps))]
    Rc = [r.conj() for r in R]
    memo = {}

    def hom(x):
        return x.subst(lambda k: Alg(stat) if any(i != X4 for i in k[2]) else None)

    def rule(key):
        kind, A, d = key
        if homogeneous and any(i != X4 for i in d):
            return Alg(stat)
        if X4 not in d:
            return None
        if key in memo:
            return memo[key]
        rest = list(d)
        rest.remove(X4)
        base = R[A] if kind == PSI else Rc[A]
        if homogeneous:
            base = hom(base)
        for i in rest:
            base = red(base.total(i, cd_author)).expand()
        memo[key] = base
        return base

    def red(x):
        return x.subst(rule).expand()

    return red


def section_lagrangian(gm, geo, stat):
    name = STATS[stat]
    sec = f"D. Lagrangian, Euler-Lagrange equations, current - {name}"
    G, Cm = gm["gamma"], gm["C"]
    sps = Spinors(stat, geo, G, Cm, m, lam)
    L = sps.lagrangian()
    pre = "grassmann" if stat == "grassmann" else "commuting"
    check(f"{pre}_lagrangian_real", alg_zero((L.conj() - L).expand()),
          f"{name}: L = sqrt|g| [(1/2)(Psibar gamma^mu D_mu Psi - D_mu Psibar gamma^mu Psi) - m S - (lambda/2) S^2], "
          f"Psibar = Psi^dagger C, satisfies L^* = L exactly ({len(L)} monomials; conjugation reverses products)",
          sec)
    Lu = sps.lagrangian_unsym()
    div = sps.zero()
    pb, ps = sps.psibar(), sps.psi()
    for mu in range(8):
        div = div + sps.dot(pb, sps.matvec(geo.gam[mu], ps)).scale(geo.sqrtg).total(mu, cd_author)
    ctrl_real = not alg_zero((Lu.conj() - Lu).expand())
    ctrl_div = not alg_zero((L - Lu).expand())
    check(f"{pre}_controls_not_vacuous", ctrl_real and ctrl_div,
          f"{name}: controls - the unsymmetrised sqrt|g|[Psibar gamma^mu D_mu Psi - m S - U] is NOT real off shell and "
          "L - L_unsym is NOT identically zero (so the reality and divergence checks test something)", sec)
    check(f"{pre}_total_divergence_relation", alg_zero((L - Lu + div.scale(sp.Rational(1, 2))).expand()),
          f"{name}: L = sqrt|g| [Psibar gamma^mu D_mu Psi - m S - U] - (1/2) d_mu (sqrt|g| Psibar gamma^mu Psi) "
          "identically", sec)
    elc, elp = sps.euler_lagrange(L)
    Ev, Eb = sps.dirac_E(), sps.dirac_Ebar()
    ok = True
    for A in range(16):
        exp = sps.zero()
        for B in range(16):
            if Cm[A, B] != 0:
                exp = exp + Ev[B].scale(Cm[A, B])
        ok = ok and alg_zero((elc[A] - exp.scale(geo.sqrtg)).expand())
    wrong = sps.zero()
    for B in range(16):
        if Cm[0, B] != 0:
            wrong = wrong + (Ev[B] + sps.psi()[B].scale(2 * m)).scale(Cm[0, B])
    ok = ok and not alg_zero((elc[0] - wrong.scale(geo.sqrtg)).expand())
    check(f"{pre}_euler_lagrange_psibar_variation", ok,
          f"{name}: dL/dPsi^dagger_A - d_mu dL/dPsi^dagger_A,mu = sqrt|g| (C [gamma^mu D_mu Psi - (m + U'(S)) Psi])_A "
          "for all 16 A (left derivatives), i.e. gamma^mu D_mu Psi = (m + lambda S) Psi; control: the same comparison "
          "with m -> -m fails", sec)
    ok = all(alg_zero((elp[B] - Eb[B].scale(geo.sqrtg)).expand()) for B in range(16))
    check(f"{pre}_euler_lagrange_psi_variation", ok,
          f"{name}: dL/dPsi_B - d_mu dL/dPsi_B,mu = -sqrt|g| (D_mu Psibar gamma^mu + (m + U'(S)) Psibar)_B for all "
          "16 B (right derivatives): the adjoint equation D_mu Psibar gamma^mu = -(m + U') Psibar", sec)
    ok = True
    for B in range(16):
        x = sps.zero()
        for A in range(16):
            if Cm[A, B] != 0:
                x = x + Ev[A].conj().scale(Cm[A, B])
        ok = ok and alg_zero((x - Eb[B]).expand())
    check(f"{pre}_adjoint_equation_is_conjugate", ok,
          f"{name}: (E)^dagger C = Ebar exactly, E = gamma^mu D_mu Psi - (m+U')Psi, Ebar = -(D_mu Psibar gamma^mu + "
          "(m+U')Psibar): the two Euler-Lagrange equations are Dirac conjugates of each other", sec)
    # current
    J = sps.current()
    ok = all(alg_zero((j.conj() - j).expand()) for j in J)
    divJ = sps.zero()
    for mu in range(8):
        divJ = divJ + J[mu].scale(geo.sqrtg).total(mu, cd_author)
    ident = divJ + (sps.dot(pb, Ev) - sps.dot(Eb, ps)).scale(sp.I * geo.sqrtg)
    ok2 = alg_zero(ident.expand())
    red = onshell_rule(sps, geo, stat, lam)
    ok3 = alg_zero(red(divJ))
    check(f"{pre}_current_conservation", ok and ok2 and ok3,
          f"{name}: J^mu = -i Psibar gamma^mu Psi is real; identity d_mu(sqrt|g| J^mu) = -i sqrt|g| (Psibar E - "
          "Ebar Psi) holds off shell; nabla_mu J^mu = 0 after the prolonged on-shell substitution (lambda general)", sec)
    # explicit EL components
    if stat == "grassmann":
        comp = {}
        for A in range(16):
            parts = []
            for key, v in sorted(Ev[A].t.items()):
                lab = "*".join(("psi" if k[0] == PSI else "chi") + f"{k[1]+1}"
                               + ("_" + "".join(COORD[i] for i in k[2]) if k[2] else "") for k in key)
                parts.append(f"({phys(v)})*{lab}")
            comp[f"E{A+1}"] = " + ".join(parts)
        FORMULAS["dirac_equation_components"] = {
            "statement": "E_A = (gamma^mu D_mu Psi - (m + lambda S) Psi)_A = 0, A = 1..16; psiA_xk = d psi_A / d xk; "
                         "chi = Psi^dagger; the same 16 equations for both statistics",
            "components": comp}
    return sps


def section_emt(gm, geo, stat, sps):
    name = STATS[stat]
    pre = stat
    sec = f"E. energy-momentum tensor - {name}"
    T, Tk, Tp, K, V = sps.emt()
    g = geo.g
    ok = all(alg_zero((T[mu][nu].scale(g[mu]) - T[nu][mu].scale(g[nu])).expand()) for mu in range(8) for nu in range(8))
    check(f"{pre}_emt_symmetric", ok, f"{name}: T_mu nu = g_mu mu T^mu_nu is symmetric (Belinfante symmetrised "
          "T^mu_nu = -Theta^(mu_nu) + delta^mu_nu L/sqrt|g|)", sec)
    red = onshell_rule(sps, geo, stat, lam)
    ok = True
    for nu in range(8):
        div = sps.zero()
        for mu in range(8):
            div = div + T[mu][nu].scale(geo.sqrtg).total(mu, cd_author)
            for l in range(8):
                if geo.Gam[l][mu][nu] != 0:
                    div = div - T[mu][l].scale(geo.sqrtg * geo.Gam[l][mu][nu])
        ok = ok and alg_zero(red(div))
        if nu == X4:
            # negative control: a wrong potential sign is not conserved
            bad = div + V.scale(2).total(nu, cd_author).scale(geo.sqrtg)
            ctrl = not alg_zero(red(bad))
    check(f"{pre}_emt_conservation_on_shell", ok,
          f"{name}: nabla_mu T^mu_nu = 0 for all 8 nu after the prolonged on-shell substitution (lambda general, "
          "all coordinates, exact)", sec)
    check(f"{pre}_emt_conservation_negative_control", ctrl,
          f"{name}: the same test on T with the potential term of wrong sign (T + 2 V delta) is NOT zero "
          "(the test is not vacuous)", sec)
    tr = sps.zero()
    for mu in range(8):
        tr = tr + T[mu][mu]
    Sx = sps.S()
    target = Sx.scale(-m) + (Sx * Sx).scale(3 * lam)
    check(f"{pre}_trace_on_shell", alg_zero((red(tr) - target).expand()),
          f"{name}: T^mu_mu = 7K - 8V off shell; on shell T^mu_mu = -m S + 7 S U' - 8 U = -m S + 3 lambda S^2", sec)
    # homogeneous on-shell states (only x4 dependence)
    hred = onshell_rule(sps, geo, stat, lam, homogeneous=True)
    rho = hred(-T[X4][X4])
    U = (Sx * Sx).scale(lam / 2)
    p_target = (Sx * Sx).scale(lam / 2)  # S U' - U
    ok = alg_zero((rho - Sx.scale(m) - U).expand())
    ok = ok and all(alg_zero((hred(T[i][i]) - p_target).expand()) for i in (0, 1, 2, 4, 5, 6, 7))
    okk = alg_zero(hred(-Tk[X4][X4])) and all(alg_zero((hred(Tk[i][i]) - Sx.scale(m) - (Sx * Sx).scale(lam)).expand())
                                               for i in (0, 4, 7))
    check(f"{pre}_homogeneous_on_shell_rho_p", ok and okk,
          f"{name}: for states depending on x4 only, on shell: rho = -T^x4_x4 = m S + U, p3 = T^xi_xi (i=1,2,3) = "
          "p_t = T^xi_xi (i=5,6,7) = p8 = T^x8_x8 = S U' - U = (lambda/2) S^2; kinetic parts -T_kin^x4_x4 = 0, "
          "T_kin^xi_xi = (m + U') S; potential parts -T_pot = delta (m S + U); hence w3 = w_t = w8 = "
          "(S U' - U)/(m S + U) = lambda S/(2 m + lambda S)", sec)
    off = hred(T[X4][X8])
    if stat == "grassmann":
        FORMULAS["T_x4_x8_homogeneous_on_shell"] = {
            "statement": "T^x4_x8 for states depending on x4 only, on shell (bilinear coefficients by monomial)",
            "monomials": {",".join(f"{'psi' if k[0] == PSI else 'chi'}{k[1]+1}" for k in key): phys(v)
                          for key, v in sorted(off.t.items())}}
    check(f"{pre}_T_x4x8_homogeneous", True,
          f"{name}: T^x4_x8 on homogeneous on-shell states has {len(off)} bilinear monomials "
          f"({'zero' if len(off) == 0 else 'nonzero: a source of the off-diagonal x4-x8 field equation'})", sec)
    return T


# ====================================================================================== F. vielbein variation
def section_vielbein_variation(gm, stat):
    name = STATS[stat]
    sec = f"F. energy-momentum tensor by vielbein variation (general diagonal vielbein) - {name}"
    F, dF, ddF, cd = generic_ring()
    geo = Geometry(F, cd, simplify=lambda x: sp.cancel(x))
    geo.spin_matrices(gm["S"])
    geo.curved_gammas(gm["gamma"])
    anti = sp.zeros(16, 16)
    for mu in range(8):
        anti += geo.gam[mu] * geo.Om[mu] + geo.Om[mu] * geo.gam[mu]
    ok0 = mzero(anti, zero_generic)
    sps = Spinors(stat, geo, gm["gamma"], gm["C"], m, lam)
    L = sps.lagrangian()
    T, _, _, _, _ = sps.emt()
    ok = True
    for a in range(8):
        var = L.map_coeffs(lambda v: sp.diff(v, F[a]))
        for nu in range(8):
            dv = L.map_coeffs(lambda v: sp.diff(v, dF[a][nu]))
            if len(dv):
                var = var - dv.total(nu, cd)
        Tvar = var.scale(F[a] / geo.sqrtg)
        ok = ok and alg_zero((Tvar - T[a][a]).expand(), zero_generic)
    check(f"{stat}_emt_equals_vielbein_variation_diagonal", ok and ok0,
          f"{name}: for an ARBITRARY diagonal vielbein e^a_mu = F_a(x1..x8) delta^a_mu, sum_mu {{gamma^mu, Omega_mu}} "
          "= 0 and T^a_a = (F_a/sqrt|g|) delta S/delta F_a (no sum; delta S = (1/2) int sqrt|g| T^mu nu delta g_mu nu) "
          "equals -Theta^a_a + K - V for all 8 a, off shell: the diagonal components (rho, p3, p_t, p8) are the "
          "vielbein-variation tensor (off-diagonal components: Belinfante symmetrisation, checked through "
          "conservation)", sec)


def section_general_variation(gm, geo, stat, sps, T):
    name = STATS[stat]
    sec = f"F. energy-momentum tensor by vielbein variation (general first-order variation) - {name}"
    Tv = linear_variation_T(sps, geo, gm["gamma"], gm["S"])
    red = onshell_rule(sps, geo, stat, lam)
    off, on = 0, 0
    for mu in range(8):
        for nu in range(8):
            d = (Tv[mu][nu] - T[mu][nu]).expand()
            off += alg_zero(d)
            on += alg_zero(red(d))
    check(f"{stat}_emt_equals_general_vielbein_variation_on_shell", on == 64,
          f"{name}: with ALL 64 components h^a_mu of a first-order vielbein variation around the author's metric "
          "(off-diagonal included; first-order Christoffels, spin connection, gamma^mu, sqrt|g|), "
          "T_var^mu_nu = (1/sqrt|g|) (delta S/delta e^a_mu) e^a_nu equals the Belinfante T^mu_nu on shell for "
          f"{on}/64 components (off shell {off}/64: the diagonal ones; the off-diagonal differences, including the "
          "antisymmetric part of T_var, are proportional to the field equations - local Lorentz invariance)", sec)
    return Tv


# ====================================================================================== G. negative control
def section_negative_control(gm, geo):
    sec = "G. negative control: the notebook's real Majorana-type Lg[]"
    G, Cm = gm["gamma"], gm["C"]
    for stat in ("grassmann", "commuting"):
        sps = Spinors(stat, geo, G, Cm, m, 0)
        th = sps.theta()
        row = sps.vecmat(th, Cm)
        Lg = sps.zero()
        for mu in range(8):
            Dth = sps.vadd(sps.theta((mu,)), sps.matvec(geo.Om[mu], th))
            Lg = Lg + sps.dot(row, sps.matvec(geo.gam[mu], Dth))
        Lg = Lg.scale(geo.sqrtg).expand()
        EL = []
        for A in range(16):
            r = Lg.lderiv(gen(THETA, A))
            for mu in range(8):
                r = r - Lg.lderiv(gen(THETA, A, (mu,))).total(mu, cd_author)
            EL.append(r.expand())
        allzero = all(alg_zero(e) for e in EL)
        if stat == "grassmann":
            tot = sps.zero()
            for mu in range(8):
                tot = tot + sps.dot(row, sps.matvec(geo.gam[mu], th)).scale(geo.sqrtg / 2).total(mu, cd_author)
            ok = allzero and alg_zero((Lg - tot).expand()) and len(Lg) > 0
            check("negative_control_majorana_grassmann_total_derivative", ok,
                  "Lg = sqrt|g| Theta^T C gamma^mu D_mu Theta with 16 REAL anticommuting components: its Euler-Lagrange "
                  "expressions vanish identically and Lg = (1/2) d_mu(sqrt|g| Theta^T C gamma^mu Theta) exactly - "
                  "a total derivative without field equations; hence the Dirac-type L with Psibar = Psi^dagger C", sec)
        else:
            nz = [A for A in range(16) if not alg_zero(EL[A])]
            check("negative_control_majorana_commuting_contrast", len(Lg) > 0 and len(nz) == 16,
                  "contrast: for 16 real COMMUTING components the same Lg is not a total derivative "
                  f"(nonzero Euler-Lagrange expressions in {len(nz)} of 16 components)", sec)


# ====================================================================================== H. quantisation
def section_quantisation(gm, geo):
    sec = "H. canonical quantisation in 4+4 (dirac16complex)"
    G, Cm, B = gm["gamma"], gm["C"], gm["B"]
    sps = Spinors("grassmann", geo, G, Cm, m, lam)
    Lu = sps.lagrangian_unsym()
    L = sps.lagrangian()
    ok = True
    ok_s = True
    for A in range(16):
        pi_u = Lu.rderiv(gen(PSI, A, (X4,)))
        pi_s = L.rderiv(gen(PSI, A, (X4,)))
        exp = sps.zero()
        for Cc in range(16):
            if B[Cc, A] != 0:
                exp = exp + Alg.g("grassmann", gen(CHI, Cc)).scale(sp.I * geo.sqrtg * B[Cc, A])
        ok = ok and alg_zero((pi_u - exp).expand())
        ok_s = ok_s and alg_zero((pi_s - exp.scale(sp.Rational(1, 2))).expand())
    check("canonical_momentum", ok and ok_s,
          "pi_A = dL/d(d_4 Psi_A) (right derivative) = i sqrt|g| (Psi^dagger B)_A for the first-order form "
          "sqrt|g|[Psibar gamma^mu D_mu Psi - ...] (and one half of it for the symmetric L, which differs by a total "
          "divergence; second-class constraints give the same bracket); B = -i C gamma^(x4), gamma^(x4) = gamma^(4)", sec)
    check("canonical_anticommutator_B", B.det() != 0 and B.inv() == B,
          "{Psi_A(x), pi_B(y)} = i delta_AB delta^7(x-y) with pi = i sqrt|g| Psi^dagger B forces "
          "{Psi_A(x), Psi^dagger_C(y)} = X_AC delta^7(x-y)/sqrt|g| with X B = 1, unique solution X = B^{-1} = B", sec)
    # no positive inner product
    vecs = (B + sp.eye(16)).nullspace()
    u = vecs[0]
    u = u / sp.sqrt(sp.simplify((u.H * u)[0]))
    val = sp.simplify((u.H * B * u)[0])
    check("no_positive_inner_product", val == -1 and len(vecs) == 8,
          "B has an 8-dimensional eigenspace for -1; for a unit vector u in it, Q = u^dagger Psi satisfies "
          "{Q, Q^dagger} = u^dagger B u / sqrt|g| = -1/sqrt|g| < 0, while in any positive-definite Hilbert space "
          "{Q, Q^dagger} = Q Q^dagger + Q^dagger Q is positive semidefinite: the state space must carry an "
          "indefinite (Krein) inner product", sec)
    # mode Hamiltonian at frame level
    k = sp.symbols("k1:9", real=True)
    hcur = -sp.I * G[3] * (m * sp.eye(16) - 3 * H * G[7])
    h = -sp.I * m * G[3]
    for a in range(8):
        if a != X4:
            h += -k[a] * G[3] * G[a]
            hcur += -k[a] * G[3] * G[a]
    E2 = m**2 + sum(ETA[a] * k[a] ** 2 for a in range(8) if a != X4)
    check("mode_hamiltonian_B_selfadjoint_dispersion",
          (B * h - h.H * B).applyfunc(sp.expand) == sp.zeros(16, 16)
          and (h * h - E2 * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16),
          "plane waves u e^{i(k.x - E x4)} (frame momenta k_a): E u = h u, h = -i m gamma^(4) - sum_{a != x4} k_a "
          "gamma^(4) gamma^(a); B h = h^dagger B (h is B-self-adjoint) and h^2 = (m^2 + k1^2 + k2^2 + k3^2 + k8^2 - "
          "k5^2 - k6^2 - k7^2) I16", sec)
    good = {k[4]: 0, k[5]: 0, k[6]: 0}
    hg = h.subs(good)
    hgc = hcur.subs(good)
    comm = (B * hg - hg * B).applyfunc(sp.expand) == sp.zeros(16, 16)
    commc = (B * hgc - hgc * B).applyfunc(sp.expand) == sp.zeros(16, 16)
    anti = all((B * G[3] * G[a] + G[3] * G[a] * B) == sp.zeros(16, 16) for a in (4, 5, 6))
    herm = (hg.H - hg).applyfunc(sp.expand)
    # on the B = +1 eigenspace h is Hermitian, the norm is positive; on B = -1 negative
    P = (sp.eye(16) + B) / 2
    Pm = (sp.eye(16) - B) / 2
    hp = (P * hg * P).applyfunc(sp.expand)
    ok_herm = ((hp.H - hp).applyfunc(sp.expand) == sp.zeros(16, 16))
    num = {m: 2, k[0]: 1, k[1]: 2, k[2]: 0, k[7]: 4}  # E = 5
    hpn = (P * hg * P).subs(num)
    ev = hpn.eigenvals()
    ok_ev = ev == {5: 4, -5: 4, 0: 8}
    check("good_sector_spectrum_and_B_sectors", comm and commc and anti and ok_herm and ok_ev
          and herm == sp.zeros(16, 16),
          "good sector (k5 = k6 = k7 = 0, no extra-time momentum, frame level): h is Hermitian on the full 16-dim "
          "space with energies +-sqrt(m^2 + k1^2 + k2^2 + k3^2 + k8^2) (8 each); [B, h] = 0 (also with the curved "
          "term 3 i H gamma^(4) gamma^(x8) of gamma^mu Omega_mu), so the B = +1 and B = -1 eigenspaces (8-dim each) "
          "are invariant, each with energies +-E (exact example m = 2, k = (1,2,0,k8=4) on B = +1: +5 (x4), -5 (x4)); "
          "extra-time momenta mix the two sectors (B anticommutes with gamma^(4) gamma^(x5,x6,x7)). With Psi^dagger "
          "realised as the adjoint the B = -1 sector carries negative Krein norm; the positive realisation follows "
          "in the next check", sec)
    # positive Fock realisation of the good sector: chi = Psi^dagger B is the Hilbert adjoint
    hn = hg.subs(num)
    W = []
    for val in (5, -5):
        ortho = []
        for v in (hn - val * sp.eye(16)).nullspace():
            w = v
            for o in ortho:
                w = w - (o.H * w)[0] * o
            w = (w / sp.sqrt(sp.simplify((w.H * w)[0]))).applyfunc(sp.simplify)
            ortho.append(w)
        W += ortho
    Wm = sp.Matrix.hstack(*W)
    unit = (Wm.H * Wm - sp.eye(16)).applyfunc(sp.simplify) == sp.zeros(16, 16)
    vev1 = make_vev([1] * 16)
    # field operators f_p = b_p (p < 8, energy +5) or d_(p-8)^dagger (p >= 8, energy -5 modes)

    def fop(p, dag):  # f_p (dag False) or f_p^dagger (dag True) as a CAR letter
        return (p, dag) if p < 8 else (p, not dag)

    def onebody(Nm, state):
        """normalised, vacuum-subtracted expectation of sum_pq N_pq f_p^dagger f_q in a one-quantum state."""
        tot = 0
        vac = 0
        for pp in range(16):
            for qq in range(16):
                x = Nm[pp, qq]
                if x == 0:
                    continue
                word = (fop(pp, True), fop(qq, False))
                vac += x * vev1(word)
                tot += x * vev1(((state, False),) + word + ((state, True),))
        return sp.simplify(tot - vac), sp.simplify(vac)

    Ms = sp.Matrix(16, 16, lambda i, j: sp.Symbol(f"M_{i}_{j}"))
    N = (Wm.H * B * Ms * Wm)
    okr = unit
    for s_ in (0, 3):
        val, _ = onebody(N, s_)
        okr = okr and sp.expand(val - (Wm[:, s_].H * B * Ms * Wm[:, s_])[0]) == 0
    for s_ in (8, 11):
        val, _ = onebody(N, s_)
        okr = okr and sp.expand(val + (Wm[:, s_].H * B * Ms * Wm[:, s_])[0]) == 0
    NH = (Wm.H * hn * Wm).applyfunc(sp.simplify)
    eP, vacE = onebody(NH, 0)
    eA, _ = onebody(NH, 8)
    NQ = (Wm.H * Wm).applyfunc(sp.simplify)  # charge Psi^dagger B Psi = chi Psi with chi = Psi^dagger_F
    qP, _ = onebody(NQ, 0)
    qA, _ = onebody(NQ, 8)
    okr = okr and eP == 5 and eA == 5 and vacE == -40 and qP == 1 and qA == -1
    check("good_sector_positive_fock_realisation", okr,
          "good sector, exact example m = 2, k = (1,2,0,k8=4), E = 5: with orthonormal eigenvectors u_s (E = +5), "
          "v_s (E = -5) of the Hermitian h and Psi = sum_s (u_s b_s + v_s d_s^*), {b, b^*} = {d, d^*} = 1 on a "
          "POSITIVE Fock space, the field conjugate is realised as Psi^dagger = chi B with chi the Hilbert adjoint "
          "(so {Psi_A, Psi^dagger_C} = (U U^* B)_AC = B_AC, the canonical relation); exact CAR evaluation: "
          "normal-ordered energy chi h Psi = +5 for b_0^*|0> and +5 for d_0^*|0> (vacuum value -40 = -8E, the "
          "filled sea), charge chi Psi = +1 and -1; expectation-value rule <:Psi^dagger M Psi:> = u^dagger B M u for "
          "particles and -v^dagger B M v for antiparticles, for a generic symbolic 16x16 M (exact)", sec)
    grow = {m: 1, k[0]: 0, k[1]: 0, k[2]: 0, k[7]: 0, k[4]: 2, k[5]: 0, k[6]: 0}
    evg = h.subs(grow).eigenvals()
    check("extra_time_modes_grow", set(evg) == {sp.sqrt(3) * sp.I, -sp.sqrt(3) * sp.I},
          "with extra-time momentum E^2 = m^2 + k_space^2 - k_t^2 < 0 when k_t^2 > m^2 + k_space^2: exact example "
          f"m = 1, k5 = 2: eigenvalues {sorted(map(sp.sstr, evg))}, i.e. modes ~ e^{{sqrt(3) x4}} grow; in the "
          "metric the frame momentum k_(x5) = e^{a4} sin(z)^{-1/6} k_x5 (coordinate k_x5) grows as the extra times "
          "deflate (a4 increasing), so every extra-time mode eventually enters the growing regime (local "
          "frame / WKB statement)", sec)
    # expectation-value rule via the exact Krein Fock evaluator
    evecs = []
    for val in (1, -1):
        for v in (B - val * sp.eye(16)).nullspace():
            evecs.append((val, v))
    # Gram-Schmidt within each eigenspace (exact)
    U, eps = [], []
    for val in (1, -1):
        basis = [v for vv, v in evecs if vv == val]
        ortho = []
        for v in basis:
            w = v
            for o in ortho:
                w = w - (o.H * w)[0] * o
            w = w / sp.sqrt(sp.simplify((w.H * w)[0]))
            ortho.append(w.applyfunc(sp.simplify))
        U += ortho
        eps += [val] * len(ortho)
    # a Krein boost mixing mode 0 (+) and mode 8 (-): cosh = 5/4, sinh = 3/4
    ch, sh = sp.Rational(5, 4), sp.Rational(3, 4)
    u0, u8 = U[0], U[8]
    U[0], U[8] = ch * u0 + sh * u8, sh * u0 + ch * u8
    Um = sp.Matrix.hstack(*U)
    Emat = sp.diag(*eps)
    ok1 = (Um.H * B * Um - Emat).applyfunc(sp.simplify) == sp.zeros(16, 16)
    ok2 = (Um * Emat * Um.H - B).applyfunc(sp.simplify) == sp.zeros(16, 16)
    vev = make_vev(eps)
    Ms = sp.Matrix(16, 16, lambda i, j: sp.Symbol(f"M_{i}_{j}"))
    ok3 = True
    for n in (0, 8, 3):
        tot = 0
        for kk in range(16):
            for ll in range(16):
                amp = vev(((n, False), (kk, True), (ll, False), (n, True)))
                if amp:
                    tot += amp * (Um[:, kk].H * Ms * Um[:, ll])[0]
        norm = vev(((n, False), (n, True)))
        lhs = sp.expand(tot / norm)
        rhs = sp.expand(eps[n] * (Um[:, n].H * Ms * Um[:, n])[0])
        ok3 = ok3 and sp.simplify(lhs - rhs) == 0
        if n == 3:  # an unboosted B-eigenvector mode: the rule takes the form u^dagger B M u
            ok3 = ok3 and sp.simplify(lhs - sp.expand((Um[:, n].H * B * Ms * Um[:, n])[0])) == 0
        if n == 0:  # a Krein-boosted mode: u^dagger B M u is NOT the expectation value
            boosted_differs = sp.simplify(lhs - sp.expand((Um[:, n].H * B * Ms * Um[:, n])[0])) != 0
    check("expectation_value_rule", ok1 and ok2 and ok3 and boosted_differs,
          "with B-orthonormal modes u_n (u_n^dagger B u_m = eps_n delta_nm, including a Krein-boosted pair) and "
          "Psi = sum_n u_n b_n, {b_n, b_m^dagger} = eps_n delta_nm: {Psi, Psi^dagger} = sum eps_n u_n u_n^dagger = B, "
          "and in the one-particle state b_n^dagger|0> (norm eps_n) the normalised expectation of the normal-ordered "
          ":Psi^dagger M Psi: equals eps_n u_n^dagger M u_n for a generic symbolic M (exact Fock evaluation); for an "
          "observable written Psibar-form Psi^dagger C N Psi = -i Psi^dagger B gamma^(4) N ... the same rule applies "
          "with M = C N; positive-norm modes (eps = +1) give u^dagger M u.  For modes that are B-eigenvectors (B u = eps u) "
          "this equals u^dagger B M u (the SPEC section 6 form), verified exactly; for a Krein-boosted mode the form "
          "u^dagger B M u does NOT hold (verified), so the general rule is eps_n u_n^dagger M u_n", sec)
    FORMULAS["quantisation"] = {
        "momentum": "pi_A = i sqrt|g| (Psi^dagger B)_A (first-order form), B = -i C gamma^(x4)",
        "anticommutator": "{Psi_A(x), Psi^dagger_B(y)} = B_AB delta^7(x - y)/sqrt|g| on x4 = const",
        "krein": "B Hermitian, B^2 = 1, signature (8,8): indefinite (Krein) state space",
        "good_sector": "k5 = k6 = k7 = 0: [B, h] = 0; B = +1 sector positive (Dirac-like Fock space), "
                       "B = -1 sector negative norm",
        "dispersion": "E^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2 (frame momenta)",
        "expectation_rule": "<n| :Psi^dagger M Psi: |n>/<n|n> = eps_n u_n^dagger M u_n, u_n^dagger B u_n = eps_n; "
                            "= u_n^dagger B M u_n when B u_n = eps_n u_n",
        "emt_operator": "T^mu_nu = :-Theta^mu_nu + delta^mu_nu (K - V):, normal ordered with respect to the modes; "
                        "one-particle expectation = eps_n times the classical bilinear evaluated on u_n"}


# ====================================================================================== I. further consequences
def section_further(gm, geo):
    sec = "I. Hamiltonian form, energy exchange, exact solutions"
    G, Cm, B = gm["gamma"], gm["C"], gm["B"]
    # Heisenberg equation from Hd and {Psi, Psi^dagger} = B / sqrt|g|
    sps = Spinors("grassmann", geo, G, Cm, m, lam)
    pb, ps = sps.psibar(), sps.psi()
    Sx = sps.S()
    Hd = Sx.scale(m) + (Sx * Sx).scale(lam / 2)
    for mu in range(8):
        if mu != X4:
            Hd = Hd - sps.dot(pb, sps.matvec(geo.gam[mu], sps.Dpsi(mu)))
    Hd = Hd.scale(geo.sqrtg).expand()
    kin = sps.dot(pb, sps.matvec(geo.gam[X4], sps.psi((X4,)))).scale(geo.sqrtg)
    ok1 = alg_zero((sps.lagrangian_unsym() - kin + Hd).expand())
    dH = [Hd.lderiv(gen(CHI, Cc)) for Cc in range(16)]
    heis = [sps.zero() for _ in range(16)]
    for A in range(16):
        for Cc in range(16):
            if B[A, Cc] != 0:
                heis[A] = heis[A] + dH[Cc].scale(-sp.I * B[A, Cc] / geo.sqrtg)
    Mp = Alg.scalar("grassmann", m) + Sx.scale(lam)
    rhs = [sps.zero() for _ in range(16)]
    for mu in range(8):
        if mu != X4:
            rhs = sps.vadd(rhs, sps.matvec(geo.gam[mu], sps.Dpsi(mu)))
    R = sps.matvec(-G[X4], [Mp * ps[A] - rhs[A] for A in range(16)])
    ok2 = all(alg_zero((heis[A] - R[A]).expand()) for A in range(16))
    check("hamiltonian_form_and_heisenberg_equation", ok1 and ok2,
          "with Hd = sqrt|g| [Psi^dagger (m C - sum_(mu != x4) C gamma^mu D_mu) Psi + U(S)] the unsymmetrised L = "
          "sqrt|g| Psibar gamma^(x4) d4 Psi - Hd exactly (Omega_x4 = 0), and d4 Psi_A = -i B_AC (1/sqrt|g|) "
          "dHd/dPsi^dagger_C (the Heisenberg equation for {Psi, Psi^dagger} = B/sqrt|g|) equals the field equation "
          "solved for d4 Psi, -gamma^(x4)[(m + lambda S) Psi - sum_(mu != x4) gamma^mu D_mu Psi], exactly (lambda "
          "general; operator ordering of the classical expression)", sec)
    # energy exchange for a diagonal homogeneous T
    r0, r1, p30, p31, pt0, pt1, p80, p81 = sp.symbols("rho rho_1 p3 p3_1 pt pt_1 p8 p8_1", real=True)
    chain = [(r0, r1), (p30, p31), (pt0, pt1), (p80, p81)]

    def cdx(e, mu):
        r = cd_author(e, mu)
        if mu == X4:
            for a, b in chain:
                r += sp.diff(e, a) * b
        return r

    Td = [p30] * 3 + [-r0] + [pt0] * 3 + [p80]
    div = []
    for nu in range(8):
        # nabla_mu T^mu_nu = (1/sqrt g) d_mu (sqrt g T^mu_nu) - Gamma^l_{mu nu} T^mu_l  (T diagonal)
        v = cdx(geo.sqrtg * Td[nu], nu) / geo.sqrtg
        for mu in range(8):
            if geo.Gam[mu][mu][nu] != 0:
                v -= geo.Gam[mu][mu][nu] * Td[mu]
        div.append(sp.factor(canon_author(v)))
    ok = sp.expand(div[X4] - (-r1 - 3 * A1 * (p30 - pt0))) == 0
    ok = ok and all(div[i] == 0 for i in range(8) if i not in (X4, X8))
    d8 = div[X8]
    ok = ok and zero_author(d8 - 3 * H * (c / s**6) * (2 * p80 - p30 - pt0))
    d8s = "3*H*cot(6*H*x8)*(2*p8 - p3 - p_t)"
    FORMULAS["energy_exchange"] = {"nabla_mu T^mu_x4": "-rho' - 3*a4'*(p3 - p_t)", "nabla_mu T^mu_x8": d8s,
                                   "T": "diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8), functions of x4 only"}
    check("energy_exchange_equation", ok,
          f"for a diagonal T^mu_nu = diag(p3,p3,p3,-rho,p_t,p_t,p_t,p8)(x4): nabla_mu T^mu_x4 = {sp.sstr(div[X4])} "
          "(rho_1 = d rho/dx4), so conservation gives d rho/dx4 = -3 a4' (p3 - p_t): energy flows between "
          "3-space and the extra times unless p3 = p_t; nabla_mu T^mu_x8 = " + d8s + " exactly, so a conserved "
          "x8-independent diagonal T needs p8 = (p3 + p_t)/2; the other components vanish identically", sec)
    # exact solutions (commuting form; linear in chi, so equally a check of the Grassmann field equation at U = 0)
    x4, x8, al, kk = sp.symbols("x4 x8 alpha k", real=True)
    a4 = sp.Function("a4")(x4)
    z = 6 * H * x8
    fphys = [sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
            [sp.exp(-a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]
    chi = sp.Matrix(sp.symbols("q1:17"))
    Om_phys = [M.applyfunc(to_physical) for M in geo.Om]
    X = [sp.Symbol(f"x{i+1}", real=True) for i in range(8)]
    X[3], X[7] = x4, x8

    def dirac(psi, mass):
        out = -mass * psi
        for mu in range(8):
            out += G[mu] / fphys[mu] * (psi.diff(X[mu]) + Om_phys[mu] * psi)
        return out

    def vanish(e, ksq):
        e = sp.expand(e)
        e = e.subs(kk, sp.sqrt(ksq))
        return sp.simplify(e) == 0

    M1 = -m * G[3] + 3 * H * (2 * al + 1) * G[3] * G[7]
    ksq = 9 * H**2 * (2 * al + 1) ** 2 - m**2
    ok_sq = (M1 * M1 - ksq * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_c = (M1.T * Cm + Cm * M1).applyfunc(sp.expand) == sp.zeros(16, 16)
    psi1 = sp.sin(z) ** al * (sp.cosh(kk * x4) * sp.eye(16) + sp.sinh(kk * x4) / kk * M1) * chi
    res = dirac(psi1, m)
    ok_sol = all(vanish(e / sp.sin(z) ** al, ksq) for e in res)
    check("exact_solution_family_x4_x8", ok_sq and ok_c and ok_sol,
          "Psi = sin(z)^alpha (cosh(k x4) + sinh(k x4)/k M) chi, M = -m gamma^(x4) + 3 H (2 alpha + 1) gamma^(x4) "
          "gamma^(x8), k^2 = 9 H^2 (2 alpha + 1)^2 - m^2, constant chi (16 components), solves gamma^mu D_mu Psi = "
          "m Psi exactly for every a4(x4) and every alpha (M^2 = k^2 I16, M^T C + C M = 0 so S is x4-independent); "
          "a test of the Tan(z) gamma^(x8) d8 and 3 H gamma^(x8) terms (independent re-derivation of the Wolfram "
          "side's exact solutions; linear in chi, so it holds for either statistics at U = 0)", sec)
    S0 = sp.Symbol("S0", real=True)
    M2 = -(m + lam * S0) * G[3] + 3 * H * G[3] * G[7]
    k2sq = 9 * H**2 - (m + lam * S0) ** 2
    ok_sq2 = (M2 * M2 - k2sq * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    ok_c2 = (M2.T * Cm + Cm * M2).applyfunc(sp.expand) == sp.zeros(16, 16)
    E2 = sp.cosh(kk * x4) * sp.eye(16) + sp.sinh(kk * x4) / kk * M2
    inv = (E2.T * Cm * E2 - Cm).applyfunc(lambda e: sp.simplify(sp.expand(e).subs(kk, sp.sqrt(k2sq))))
    res2 = dirac(E2 * chi, m + lam * S0)
    ok2 = ok_sq2 and ok_c2 and inv == sp.zeros(16, 16) and all(vanish(e, k2sq) for e in res2)
    check("exact_nonlinear_homogeneous_solution", ok2,
          "Phi = (cosh(k x4) + sinh(k x4)/k M) chi, M = -(m + lambda S0) gamma^(x4) + 3 H gamma^(x4) gamma^(x8), "
          "k^2 = 9 H^2 - (m + lambda S0)^2: exp(M^T x4) C exp(M x4) = C so S = chi^dagger C chi = S0 is constant, "
          "and gamma^mu D_mu Phi = (m + lambda S0) Phi = (m + U'(S)) Phi exactly: an exact homogeneous solution of "
          "the nonlinear commuting field dirac16complex00 (U = (lambda/2) S^2); its EMT is the homogeneous on-shell "
          "form rho = m S0 + U, p = S0 U' - U (check *_homogeneous_on_shell_rho_p)", sec)


# ====================================================================================== formulas summary
def formulas_lagrangian_emt():
    FORMULAS["lagrangian"] = ("L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi "
                              "- (lambda/2) (Psibar Psi)^2 ], Psibar = Psi^dagger C, gamma^mu = e^mu_a gamma^a, "
                              "D_mu Psi = d_mu Psi + Omega_mu Psi")
    FORMULAS["euler_lagrange"] = ("gamma^mu D_mu Psi = (m + lambda S) Psi;  D_mu Psibar gamma^mu = -(m + lambda S) "
                                  "Psibar; in this metric: e^{-a4} sin(z)^(-1/6) gamma^(xi) d_i Psi (i=1,2,3) + "
                                  "gamma^(x4) d_4 Psi + e^{a4} sin(z)^(-1/6) gamma^(xj) d_j Psi (j=5,6,7) + tan(z) "
                                  "gamma^(x8) d_8 Psi + 3 H gamma^(x8) Psi = (m + lambda S) Psi, z = 6 H x8")
    FORMULAS["current"] = "J^mu = -i Psibar gamma^mu Psi (real); nabla_mu J^mu = 0 on shell"
    FORMULAS["emt"] = {
        "Theta": "Theta^mu_nu = (1/4)[Psibar gamma^mu D_nu Psi - D_nu Psibar gamma^mu Psi + g^{mu mu} g_{nu nu} "
                 "(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi)]",
        "K": "K = (1/2)(Psibar gamma^mu D_mu Psi - D_mu Psibar gamma^mu Psi)",
        "V": "V = m S + U, U = (lambda/2) S^2",
        "T": "T^mu_nu = -Theta^mu_nu + delta^mu_nu (K - V);  T_kin = -Theta + delta K;  T_pot = -delta V",
        "rho": "rho = -T^x4_x4 = Theta^x4_x4 - K + V",
        "p3": "p3 = T^x1_x1 = -Theta^x1_x1 + K - V",
        "p_t": "p_t = T^x5_x5 = -Theta^x5_x5 + K - V",
        "p8": "p8 = T^x8_x8 = -Theta^x8_x8 + K - V",
        "trace": "T^mu_mu = 7K - 8V; on shell -m S + 7 S U' - 8 U = -m S + 3 lambda S^2",
        "homogeneous_on_shell": "rho = m S + U, p3 = p_t = p8 = S U' - U, w = (S U' - U)/(m S + U) = lambda S/(2m + "
                                "lambda S)",
        "Theta_diag_in_metric": "Theta^xi_xi = (1/2) f_i^{-1} (Psibar gamma^(xi) d_i Psi - d_i Psibar gamma^(xi) Psi) "
                                "(no sum; the Omega terms cancel since {gamma^(xi), Omega_(xi)} = 0), f = (e^a4 s, "
                                "e^a4 s, e^a4 s, 1, e^-a4 s, e^-a4 s, e^-a4 s, cot z), s = sin(z)^(1/6)"}


def section_superalgebra():
    sec = "0. the jet super-algebra (own implementation)"
    a, b = gen(PSI, 0), gen(PSI, 1)
    x, y = gen(CHI, 0), gen(PSI, 1, (3,))
    ga = lambda k: Alg.g("grassmann", k)
    co = lambda k: Alg.g("commuting", k)
    ok = len(ga(a) * ga(a)) == 0 and alg_zero((ga(a) * ga(b) + ga(b) * ga(a)))
    ok = ok and alg_zero((co(a) * co(b) - co(b) * co(a))) and len(co(a) * co(a)) == 1
    ok = ok and alg_zero(((ga(x) * ga(y)).conj() - ga(gen(CHI, 1, (3,))) * ga(gen(PSI, 0))))
    ok = ok and alg_zero(((ga(x) * ga(a)).scale(sp.I).conj() + (ga(x) * ga(a)).scale(sp.I)))
    p = ga(x) * ga(a) * ga(y)
    ok = ok and alg_zero(p.lderiv(y) - ga(x) * ga(a)) and alg_zero(p.rderiv(y) - ga(x) * ga(a))
    ok = ok and alg_zero(p.lderiv(a) + ga(x) * ga(y)) and alg_zero(p.rderiv(a) + ga(x) * ga(y))
    q = ga(x) * ga(a)
    ok = ok and alg_zero(q.lderiv(a) + ga(x)) and alg_zero(q.rderiv(a) - ga(x))
    ok = ok and alg_zero(ga(a).total(3, lambda v, mu: 0) - ga(gen(PSI, 0, (3,))))
    check("superalgebra_axioms", ok,
          "psi psi = 0 and psi_A psi_B = -psi_B psi_A (Grassmann), commuting products symmetric with nonzero squares; "
          "(chi_A psi_B)^* = chi_B psi_A (order reversal), (i chi psi)^* = -i chi psi for A = B; left/right "
          "derivatives with the Grassmann signs; total derivative acts on the jet coordinates", sec)


def main():
    out = OUT
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    section_superalgebra()
    gm = section_gammas()
    geo = section_geometry(gm)
    section_curvature(gm, geo)
    ctx = {"gm": gm, "geo": geo, "sps": {}, "T": {}, "Tvar": {}}
    for stat in ("grassmann", "commuting"):
        sps = section_lagrangian(gm, geo, stat)
        T = section_emt(gm, geo, stat, sps)
        ctx["sps"][stat], ctx["T"][stat] = sps, T
        ctx["Tvar"][stat] = section_general_variation(gm, geo, stat, sps, T)
        section_vielbein_variation(gm, stat)
    section_negative_control(gm, geo)
    section_quantisation(gm, geo)
    section_further(gm, geo)
    formulas_lagrangian_emt()
    try:
        comp = compare_wolfram.compare(FORMULAS, CHECKS, os.path.join(REV, "theory", "field-theory.json"),
                                       os.path.join(REV, "theory", "reports", "wolfram-field-theory.json"), ctx)
    except Exception as exc:  # a format change on the Wolfram side must be visible, not fatal
        comp = {"status": "ERROR", "detail": f"comparison failed: {type(exc).__name__}: {exc}"}
    npass = sum(1 for x in CHECKS if x["verdict"] == "pass")
    rep = {
        "report": "Revision/theory/reports/python-field-theory.json",
        "producer": "Revision/theory/python/check_field_theory.py (sympy, exact; own jet super-algebra "
                    "superalg.py for both statistics)",
        "spec": "Revision/SPEC.md sections 1-6 (metric, Clifford data, the two fields, EMT, quantisation)",
        "inputs": ["Revision/algebra/gammas.json", "Revision/algebra/reports/python-gammas.json"],
        "independence": "no code shared with Revision/theory/wolfram; the Wolfram outputs are read only by the final "
                        "comparison section",
        "summary": {"checks": len(CHECKS), "pass": npass, "fail": len(CHECKS) - npass},
        "checks": CHECKS,
        "formulas": FORMULAS,
        "comparison_with_wolfram": comp,
    }
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rep, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {out}: {npass}/{len(CHECKS)} pass; comparison: {comp.get('status')}; "
          f"{time.time() - T0:.1f}s")
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
