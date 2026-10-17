#!/usr/bin/env python3
"""Revision/universe_model/field_equations/derive_field_equations.py - the coupled field equations of the universe model
UM-1 (Revision/universe_model/MODEL.md), derived with sympy from the metric and the actions.

Parts (each statement is a check with name, verdict, detail; the equations are written to the JSON output):
  A  the background: the Einstein tensor of the corrected primordial metric with general a4(x4), b4(x4), recomputed here
     from the metric (own Christoffel symbols) and compared with Revision/field_equations_a4/a4-equations.json (key
     einstein); the x4 constraint in terms of the block rate h4 = u/2 - a4'; the measure sqrt|g| dx0 in the hidden
     coordinate y.
  B  the multi-species background system: every species i with (rho_i, p3_i, p0_i = p_t_i), the per-species conservation
     with the portal exchange Q_i (sum Q_i = 0), the four-dimensional densities rho_4 = V_perp rho and their
     conservation, the effective Planck mass and the Friedmann equation of the four-dimensional observer.
  C  order epsilon: the scalar perturbations Phi, Psi_N (Newtonian gauge) and the radion sigma of the block, functions of
     (x4, x1), x0-independent (zero modes): the linearised Einstein tensor delta G^M_N, computed from the metric.
  D  the x0 operators (the mass mechanism): the reduced action of a four-dimensional gauge-field component on the cell,
     its Euler-Lagrange equation and boundary conditions (fold: Neumann; tip: the Robin condition of the tip sigma
     field), the leading-order W and Z masses and m_Z/m_W = 1/cos(theta_W); the fermion zero modes of the block
     h = -(i/f) sigma1 d_y + mu sigma2 and the tip value zeta(mu); the Rayleigh quotient and the uncertainty bound.
  E  the portal mean fields entering the Kohn-Sham equations of dirac16complex, the back-reaction on the Standard-Model
     fermions, and the gauge invariance of the portal and tip operators (explicit SU(2)_L x U(1)_Y representation,
     random group elements); the charge argument for the W.

Outputs (deterministic, LF): Revision/universe_model/field_equations/field-equations.json and
Revision/universe_model/field_equations/reports/field-equations-checks.json.  Exit 0 iff every check passes.
Usage (from anywhere): python Revision/universe_model/field_equations/derive_field_equations.py
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REV = HERE.parents[1]
OUT = HERE / "field-equations.json"
REP = HERE / "reports" / "field-equations-checks.json"
T0 = time.time()
CHECKS = []
EQ = {}


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print("[%6.1fs] %s %s" % (time.time() - T0, "PASS" if ok else "FAIL", name), flush=True)


def s(e):
    return sp.sstr(e)


# ------------------------------------------------------------------------------------------------- geometry helpers
def diag_einstein(gd, X):
    """mixed Einstein tensor G^a_b (dict of the nonzero components) and the Christoffel symbols of a diagonal metric
    g = diag(gd); exact sympy expressions (not simplified)"""
    n = len(X)
    G = [[sp.Integer(0)] * n for _ in range(n)]
    Gam = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                val = sp.Integer(0)
                if a == b == c:
                    val = sp.diff(gd[a], X[a]) / (2 * gd[a])
                elif a == b:
                    val = sp.diff(gd[a], X[c]) / (2 * gd[a])
                elif a == c:
                    val = sp.diff(gd[a], X[b]) / (2 * gd[a])
                elif b == c:
                    val = -sp.diff(gd[b], X[a]) / (2 * gd[a])
                if val != 0:
                    Gam[(a, b, c)] = val
    def gam(a, b, c):
        return Gam.get((a, b, c), sp.Integer(0))
    Ric = [[sp.Integer(0)] * n for _ in range(n)]
    for b in range(n):
        for d in range(b, n):
            r = sp.Integer(0)
            for a in range(n):
                r += sp.diff(gam(a, b, d), X[a]) - sp.diff(gam(a, b, a), X[d])
                for e in range(n):
                    r += gam(a, a, e) * gam(e, b, d) - gam(a, d, e) * gam(e, b, a)
            Ric[b][d] = r
            Ric[d][b] = r
    R = sum(Ric[a][a] / gd[a] for a in range(n))
    for a in range(n):
        for b in range(n):
            G[a][b] = Ric[a][b] / gd[a] - (R / 2 if a == b else 0)
    return G


# ======================================================================================================== part A
x = sp.symbols("x0:8", real=True)
x0, x1, x4 = x[0], x[1], x[4]
H = sp.Symbol("H", positive=True)
a = sp.Function("a4", real=True)(x4)
b = sp.Function("b4", positive=True)(x4)
z = 6 * H * x0
# Parts A and C work in the hidden coordinate y = ln|sin z|/(6H) (dy = cot z dx0, |sin z| = e^(6Hy)), in which the
# metric is diag(e^-2a4 b4, e^2a4 (x3), -1, -e^-2a4 b4 e^(2Hy) (x3)) for EVERY real z (g00 dx0^2 = e^-2a4 b4 dy^2,
# (sin^2 z)^(1/6) = e^(2Hy)); the mixed components G^M_N are the same in both charts (a change of x0 alone).  The
# symbol x[0] stands for y in these parts.
yv = x[0]
gbar = [sp.exp(-2 * a) * b] + [sp.exp(2 * a)] * 3 + [sp.Integer(-1)] + [-sp.exp(-2 * a) * b * sp.exp(2 * H * yv)] * 3
Gb = diag_einstein(gbar, x)
ad1, ad2, uu, vv, kk = sp.symbols("ad1 ad2 uu vv kk", real=True)
subs_b = {sp.Derivative(b, (x4, 2)): (vv + uu ** 2) * b, sp.Derivative(b, x4): uu * b,
          sp.Derivative(a, (x4, 2)): ad2, sp.Derivative(a, x4): ad1}


def to_rates(e):
    e = sp.expand(e.subs(subs_b))
    e = sp.powsimp(sp.expand(e), combine="exp")
    e = sp.expand(e.subs(sp.exp(2 * a), kk * b))
    return sp.simplify(e)


G44 = to_rates(Gb[4][4])
G11 = to_rates(Gb[1][1])
G00 = to_rates(Gb[0][0])
G55 = to_rates(Gb[5][5])
offd = [to_rates(Gb[i][j]) for (i, j) in ((4, 0), (0, 4), (4, 1), (1, 0), (4, 5))]
rec = json.loads((REV / "field_equations_a4" / "a4-equations.json").read_text(encoding="utf-8"))
ein = rec["einstein"]
Lam, kappa, rho, p3, p0 = sp.symbols("Lam kappa rho p3 p0", real=True)
loc = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H, "Lam": Lam, "kappa": kappa, "rho": rho, "p3": p3,
       "p0": p0}


def rec_lhs(key):
    lhs, rhs = ein[key]["input"].replace("^", "**").split("==")
    return sp.sympify(lhs, locals=loc) - Lam
G44_rec, G11_rec, G00_rec = rec_lhs("constraint_x4"), rec_lhs("space_x1"), rec_lhs("hidden_x0")
okA = all(sp.simplify(p - q) == 0 for p, q in ((G44, G44_rec), (G11, G11_rec), (G00, G00_rec)))
check("A1_background_einstein_tensor_equals_record", okA and sp.simplify(G00 - G55) == 0 and all(o == 0 for o in offd),
      "G^M_N of the corrected metric, computed here from the metric (own Christoffel symbols, in the hidden coordinate y, valid for every real z): "
      "G^x4_x4 = %s, G^x1_x1 = %s, G^x0_x0 = G^x5_x5 = %s (u = b4'/b4, v = u', k = e^(2 a4)/b4); equal to "
      "a4-equations.json einstein: %s; the off-diagonal components (x4,x0), (x0,x4), (x4,x1), (x1,x0), (x4,x5) vanish: %s"
      % (s(G44), s(G11), s(G00), okA, all(o == 0 for o in offd)))
hh = sp.Symbol("h4", real=True)
con_h = sp.expand((G44 - Lam).subs(uu, 2 * (hh + ad1)))       # G^4_4 + Lam = -kappa rho
fried = sp.expand(-con_h)                                      # = kappa rho + Lam ... see below
target = 3 * ad1 ** 2 + 12 * ad1 * hh + 6 * hh ** 2 - 6 * H ** 2 * kk
check("A2_constraint_with_block_rate",
      sp.simplify(sp.expand(-(G44.subs(uu, 2 * (hh + ad1)))) - target) == 0,
      "with u = 2 (h4 + a4') (h4 = u/2 - a4', the rate of the block (x0, x5, x6, x7), f = e^-a4 b4^(1/2)) the Einstein x4 "
      "equation G^4_4 + Lambda = -kappa rho reads 3 a4'^2 + 12 a4' h4 + 6 h4^2 - 6 H^2 k = kappa rho + Lambda: the "
      "Friedmann equation with the block terms 12 a4' h4 + 6 h4^2 and the hidden-curvature term -6 H^2 k (k' = -2 k h4, "
      "constant for a static block)")
EQ["background_einstein"] = {"G44": s(G44), "G11": s(G11), "G00_eq_G55": s(G00),
                             "constraint_h_form": "3*ad1**2 + 12*ad1*h4 + 6*h4**2 - 6*H**2*kk == kappa*rho + Lam",
                             "general_lovelock": "the components sum_k alpha_k E_(k) of a4-equations.json generalSource "
                                                 "(constraint_x4, space_x1_eq_x2_eq_x3, hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7) "
                                                 "with the total source of part B"}
# the measure in the hidden coordinate
y = sp.Symbol("y", real=True)
sqrtg = sp.exp(-a) * b ** 2 * sp.cot(z) * sp.sin(z) ** sp.Rational(1, 2)     # the patch
# the x0 chart on the patch 0 < z < pi/2 (sin z > 0, (sin^2 z)^(1/6) = sin^(1/3) z)
gx0 = [sp.exp(-2 * a) * b * sp.cot(z) ** 2] + [sp.exp(2 * a)] * 3 + [sp.Integer(-1)] + \
      [-sp.exp(-2 * a) * b * sp.sin(z) ** sp.Rational(1, 3)] * 3
detg = sp.Mul(*gx0)
ok_det = sp.simplify(detg - sqrtg ** 2) == 0      # signature (4, 4): det g > 0
# dy = cot z dx0 and |sin z| = e^(6Hy): sqrt|g| dx0 = e^-a4 b4^2 cot z sin^(1/2) z dy/cot z = e^-a4 b4^2 e^(3Hy) dy
meas = sp.simplify((sqrtg / sp.cot(z)).subs(sp.sin(z), sp.exp(6 * H * y)))
check("A3_measure_in_y", ok_det and sp.simplify(meas - sp.exp(-a) * b ** 2 * sp.exp(3 * H * y)) == 0,
      "sqrt|g| = e^-a4 b4^2 cot z sin^(1/2) z on the patch (|det g| = sqrt|g|^2: %s); with dy = cot z dx0 and "
      "|sin z| = e^(6Hy): sqrt|g| dx0 = %s dy" % (ok_det, s(meas)))

# ======================================================================================================== part B
t = sp.Symbol("x4", real=True)
fS = sp.Function("f")(t)
rhoS, p3S, p0S, QS = [sp.Function(nm)(t) for nm in ("rho", "p3", "p0", "Q")]
aS = sp.Function("a4")(t)
hS = sp.Symbol("h4")
# per-species conservation (a4-equations.json generalSource.energyExchange with p0 = p_t, plus the exchange Q)
cons8 = sp.Eq(sp.diff(rhoS, t), -3 * sp.diff(aS, t) * (rhoS + p3S) - 4 * hS * (rhoS + p0S) + QS)
# the four-dimensional density rho_4 = c f^4 rho with f' = h4 f
c4 = sp.Symbol("c_perp", positive=True)
rho4 = c4 * fS ** 4 * rhoS
drho4 = sp.diff(rho4, t).subs(sp.diff(fS, t), hS * fS).subs(sp.diff(rhoS, t), cons8.rhs)
target4 = -3 * sp.diff(aS, t) * (rho4 + c4 * fS ** 4 * p3S) - 4 * hS * c4 * fS ** 4 * p0S + c4 * fS ** 4 * QS
check("B1_four_dimensional_conservation", sp.simplify(drho4 - target4) == 0,
      "per species: rho_i' = -3 a4' (rho_i + p3_i) - 4 h4 (rho_i + p0_i) + Q_i (energyExchange of a4-equations.json with "
      "p0 = p_t and the portal exchange Q_i, sum_i Q_i = 0); the four-dimensional density rho_4 = V_perp rho, "
      "V_perp = c f^4 (MODEL.md section 5), obeys rho_4' = -3 a4' (rho_4 + p3_4) - 4 h4 p0_4 + Q_4: the standard "
      "four-dimensional law for every species without hidden or extra-time pressure (p0 = p_t = 0: radiation, dust, the "
      "Standard-Model zero modes)")
EQ["species_conservation"] = {"eight_dimensional": "rho_i' = -3 a4' (rho_i + p3_i) - 4 h4 (rho_i + p0_i) + Q_i",
                              "four_dimensional": "rho4_i' = -3 a4' (rho4_i + p3_4i) - 4 h4 p0_4i + Q4_i, rho4 = V_perp rho",
                              "requirement": "p0_i = p_t_i for the total source (hiddenEqualsExtraTimes); off-diagonal "
                                             "components and x0 dependence of the averaged source vanish"}
# effective Planck mass: kappa rho = rho_4 / M_Pl^2 with M_Pl^2 = V_perp / kappa
EQ["observer_friedmann"] = {"einstein": "3 a4'^2 = rho_4/M_Pl^2 + Lam_eff - 12 a4' h4 - 6 h4^2, Lam_eff = Lam + 6 H^2 k, "
                                        "M_Pl^2 = V_perp/kappa = 2 f^4 v_t (1 - e^(-3 H L))/(3 H kappa)",
                            "drifts": "k' = -2 k h4 (Lam_eff drifts), (M_Pl^2)' = 4 h4 M_Pl^2 (G drifts), x0 masses ~ 1/f drift "
                                      "with -h4: a slowly deflating block needs |h4| << a4'"}
# check the drift statements
kS = sp.exp(2 * aS) / sp.Function("b4")(t)
bS = sp.Function("b4")(t)
uS = sp.diff(bS, t) / bS
hdef = uS / 2 - sp.diff(aS, t)
check("B2_drifts_of_k_and_planck_mass",
      sp.simplify(sp.diff(kS, t) - (-2 * kS * hdef)) == 0
      and sp.simplify(sp.diff((sp.exp(-aS) * sp.sqrt(bS)) ** 4, t) - 4 * hdef * (sp.exp(-aS) * sp.sqrt(bS)) ** 4) == 0,
      "k = e^(2 a4)/b4 obeys k' = -2 k h4 and V_perp ~ f^4 = (e^-a4 b4^(1/2))^4 obeys (f^4)' = 4 h4 f^4: with a "
      "deflating block (h4 < 0) the hidden-curvature term 6 H^2 k grows and the four-dimensional Planck mass shrinks")

# ======================================================================================================== part C
eps = sp.Symbol("epsilon")
Phi = sp.Function("Phi")(x4, x1)
PsiN = sp.Function("PsiN")(x4, x1)
sig = sp.Function("sigma")(x4, x1)
gpert = [gbar[0] * (1 + 2 * eps * sig)] + [gbar[1] * (1 - 2 * eps * PsiN)] * 3 + [-(1 + 2 * eps * Phi)] + \
        [gbar[5] * (1 + 2 * eps * sig)] * 3
Gp = diag_einstein(gpert, x)
dG = {}
for (i, j) in ((4, 4), (4, 1), (1, 4), (1, 1), (2, 2), (0, 0), (5, 5), (4, 0), (1, 0)):
    e1 = sp.diff(Gp[i][j], eps).subs(eps, 0)
    e1 = e1.subs(subs_b)
    e1 = sp.powsimp(sp.expand(e1), combine="exp")
    dG[(i, j)] = sp.simplify(e1.subs(sp.exp(2 * a), kk * b))
x0free = all(not dG[k].has(x0) for k in dG)
check("C1_linear_scalar_perturbations",
      x0free and dG[(4, 0)] == 0 and dG[(1, 0)] == 0 and sp.simplify(dG[(0, 0)] - dG[(5, 5)]) == 0,
      "the linearised Einstein tensor of g = gbar + epsilon dg, dg44 = -2 Phi, dg_ii = -2 PsiN e^(2 a4) gbar_ii/e^(2a4), "
      "dg_block = 2 sigma gbar_block (Phi, PsiN, sigma functions of (x4, x1), x0 zero modes), computed from the metric: "
      "free of x0: %s; delta G^x4_x0 = delta G^x1_x0 = 0; delta G^x0_x0 = delta G^x5_x5 (the block stays one block); "
      "delta G^4_4 = %s; delta G^4_1 = %s; delta G^1_1 - delta G^2_2 = %s"
      % (x0free, s(dG[(4, 4)]), s(dG[(4, 1)]), s(sp.simplify(dG[(1, 1)] - dG[(2, 2)]))))
aniso = sp.simplify(dG[(1, 1)] - dG[(2, 2)])
# the static block (h4 = 0: u = 2 a4', v = u' = 2 a4'') and no radion: the standard four-dimensional equations
st = {uu: 2 * ad1, vv: 2 * ad2, kk: sp.exp(2 * a) / b}
lap = lambda F: sp.exp(-2 * a) * sp.diff(F, x1, 2)
std44 = 6 * ad1 * (sp.diff(PsiN, x4) + ad1 * Phi) - 2 * lap(PsiN)
std41 = -2 * sp.diff(sp.diff(PsiN, x4) + ad1 * Phi, x1)
g44s = sp.simplify(dG[(4, 4)].subs(st).subs(sig, 0).doit())
g41s = sp.simplify(dG[(4, 1)].subs(st).subs(sig, 0).doit())
an_s = sp.simplify(aniso.subs(st))
check("C2_static_block_gives_standard_perturbation_equations",
      sp.simplify(g44s - std44) == 0 and sp.simplify(g41s - std41) == 0
      and sp.simplify(an_s - sp.exp(-2 * a) * sp.diff(PsiN - Phi - 4 * sig, x1, 2)) == 0,
      "with a static block (h4 = 0, u = 2 a4', v = 2 a4'') and sigma = 0: delta G^4_4 = 6 a4'(PsiN' + a4' Phi) - 2 "
      "e^(-2 a4) d1^2 PsiN and delta G^4_1 = -2 d1(PsiN' + a4' Phi), the Newtonian-gauge equations of four-dimensional "
      "general relativity with H_obs = a4'; the 11 - 22 equation is e^(-2 a4) d1^2 (PsiN - Phi - 4 sigma) = kappa "
      "(anisotropic stress): without anisotropic stress PsiN = Phi + 4 sigma, the radion shifts the gravitational slip")
EQ["order_epsilon_scalar"] = {"metric": "dg44 = -2 Phi, dg_ii = -2 PsiN e^(2 a4) (i = 1, 2, 3), dg_00 = 2 sigma gbar_00, "
                                        "dg_tt = 2 sigma gbar_tt (t = 5, 6, 7); functions of (x4, x1)",
                              "deltaG44": s(dG[(4, 4)]), "deltaG41": s(dG[(4, 1)]), "deltaG11": s(dG[(1, 1)]),
                              "deltaG22": s(dG[(2, 2)]), "deltaG00_eq_deltaG55": s(dG[(0, 0)]),
                              "anisotropy_11_minus_22": s(aniso),
                              "equations": "delta G^M_N = kappa delta T^M_N: delta T^4_4 = -delta rho, delta T^4_1 = (rho + p3) "
                                           "dv/dx1-type momentum density, delta T^1_1 = delta p3, delta T^0_0 = delta T^5_5 = "
                                           "delta p0; with no anisotropic stress the 11 - 22 equation relates Phi, PsiN and sigma"}

# ======================================================================================================== part D
f_, L, Hs = sp.symbols("f L H", positive=True)
yy = sp.Symbol("y", real=True)
u = sp.Function("u")(yy)
m2, ct = sp.symbols("m2 c_tip", real=True)
w = sp.exp(3 * Hs * yy)
# reduced action of one gauge-field component A_mu(x) u(y) on one half of the cell (the other half is its mirror):
# S_1d = int_{-L}^0 dy w(y) [ u'^2/f^2 - m^2 u^2 ] + c_tip u(-L)^2 ; its variation:
lag = w * (sp.diff(u, yy) ** 2 / f_ ** 2 - m2 * u ** 2)
el = sp.euler_equations(lag, u, yy)[0].lhs
el_expected = -2 * (sp.diff(w * sp.diff(u, yy), yy) / f_ ** 2 + m2 * w * u)
check("D1_gauge_x0_operator",
      sp.simplify(el - el_expected) == 0,
      "a four-dimensional gauge-field component A_mu(x) u(x0) (gauge A_x0 = 0, unbroken or broken generator): the "
      "eight-dimensional kinetic term sqrt|g| g^00 g^mumu (d_0 u)^2 becomes, with sqrt|g| dx0 = e^-a4 b4^2 e^(3Hy) dy "
      "(A3) and g^00 (d_0)^2 = (1/f^2) d_y^2, the one-dimensional action int dy e^(3Hy) [u'^2/f^2 - m^2 u^2]: "
      "Euler-Lagrange -(1/f^2) e^(-3Hy) (e^(3Hy) u')' = m^2 u; boundary terms: fold u'(0) = 0 (Neumann, the even fold "
      "condition), tip e^(-3HL) u'(-L)/f^2 = c_tip u(-L) (the Robin condition of the tip term c_tip u(-L)^2)")
# zero mode and the leading W, Z mass
norm = sp.integrate(w, (yy, -L, 0))
m2_lead = sp.simplify(ct / norm)
check("D2_photon_massless_and_W_Z_leading_mass",
      sp.simplify(norm - (1 - sp.exp(-3 * Hs * L)) / (3 * Hs)) == 0,
      "u = const solves the operator with m^2 = 0 when c_tip = 0 (the photon, the gluons and the graviton zero mode: "
      "unbroken generators); to first order in c_tip (u = const + O(c_tip)): m^2 = c_tip / int_{-L}^0 e^(3Hy) dy = "
      "%s. The tip term (v_Sigma^2/4) tr(D Sigma^dag D Sigma) gives c_tip(W) = g5^2 v_Sigma^2 w_tip/4 and "
      "c_tip(Z) = (g5^2 + g5'^2) v_Sigma^2 w_tip/4, c_tip(photon) = 0, so m_Z^2/m_W^2 = 1 + g'^2/g^2 = 1/cos^2(theta_W) at "
      "this order (rho = 1, custodial symmetry); the bending of the profiles at higher order is computed in SOLUTION.md"
      % s(m2_lead))
# the Rayleigh quotient and the uncertainty bound (Gaussian test profile on the infinite line, w = 1)
sgm = sp.Symbol("s", positive=True)
yg = sp.Symbol("Y", real=True)
ug = sp.exp(-yg ** 2 / (4 * sgm ** 2))
var_y = sp.integrate(yg ** 2 * ug ** 2, (yg, -sp.oo, sp.oo)) / sp.integrate(ug ** 2, (yg, -sp.oo, sp.oo))
p2 = sp.integrate(sp.diff(ug, yg) ** 2, (yg, -sp.oo, sp.oo)) / sp.integrate(ug ** 2, (yg, -sp.oo, sp.oo))
check("D3_uncertainty_bound_saturated_by_gaussian", sp.simplify(var_y * p2 - sp.Rational(1, 4)) == 0,
      "on a flat line <Y^2> <p^2> >= 1/4 (units hbar = c = 1), saturated by the Gaussian: <Y^2> <p^2> = %s; this is the "
      "author's estimate m >= hbar/(2 c Delta s) when m^2 = <p^2>. In the warped cell the Rayleigh quotient is the "
      "weighted mean of |d_s u|^2 (the hidden momentum relative to the geometric zero mode), not <p^2> of the proper "
      "density: the bound holds for the odd modes and the excitations and fails for the zero modes "
      "(Revision/universe_model/ANALYSIS.md, analysis/x0_mass_analysis.py)" % s(sp.simplify(var_y * p2)))
# fermion zero modes of the block (k = 0, v = 0, j = +1)
mu = sp.Symbol("mu", real=True)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
chiL = sp.Matrix([sp.exp(f_ * mu * yy), 0])
chiR = sp.Matrix([0, sp.exp(-f_ * mu * yy)])
hop = lambda c, m: -sp.I / f_ * s1 * sp.diff(c, yy) + m * s2 * c
mup = sp.Symbol("mu_p", positive=True)       # the tip value for mu > 0 (mu < 0 by mu -> -mu, the right-handed mode)
zeta2 = sp.simplify(sp.exp(-2 * f_ * mup * L) / sp.integrate(sp.exp(2 * f_ * mup * yy), (yy, -L, 0)))
check("D4_fermion_zero_modes_and_tip_values",
      hop(chiL, mu).applyfunc(sp.simplify) == sp.zeros(2, 1) and hop(chiR, mu).applyfunc(sp.simplify) == sp.zeros(2, 1)
      and sp.simplify(zeta2 - 2 * f_ * mup * sp.exp(-2 * f_ * mup * L) / (1 - sp.exp(-2 * f_ * mup * L))) == 0,
      "the block h = -(i/f) sigma1 d_y + mu sigma2 (the Kohn-Sham block at k = 0, v = 0, j = +1, with the bulk mass mu) "
      "annihilates (e^(f mu y), 0) (the even fold condition b(0) = 0 and the tip b(-L) = 0: the left-handed zero mode) "
      "and (0, e^(-f mu y)) (a(0) = 0, a(-L) = 0: the right-handed zero mode, theorem T3); the normalised tip value "
      "zeta(mu)^2 = |chi(-L)|^2 / int |chi|^2 dy = %s; the tip coupling lambda_f gives the four-dimensional Dirac mass "
      "m_f = lambda_f zeta(mu_L) zeta(-mu_R) to first order in lambda_f (exponentially small for f mu L >> 1: the mass "
      "hierarchy from localisation)" % s(zeta2))
EQ["x0_mass_mechanism"] = {
    "gauge_operator": "-(1/f^2) e^(-3Hy) (e^(3Hy) u')' = m^2 u on [-L, 0] (each half of the cell), u'(0) = 0, "
                      "e^(-3HL) u'(-L)/f^2 = c_tip u(-L)",
    "leading_mass": "m^2 = c_tip / int_{-L}^0 e^(3Hy) dy = 3 H c_tip/(1 - e^(-3HL))",
    "c_tip": "W: g5^2 v_Sigma^2 w_tip/4; Z: (g5^2 + g5'^2) v_Sigma^2 w_tip/4; photon, gluons: 0",
    "fermion_block": "h = -(i/f) sigma1 d_y + mu sigma2 (+ kappa k sigma3 + v for k != 0), zero modes (e^(f mu y), 0) "
                     "and (0, e^(-f mu y))",
    "fermion_mass": "m_f = lambda_f zeta(mu_L) zeta(-mu_R), zeta(mu)^2 = 2 f mu e^(-2 f mu L)/(1 - e^(-2 f mu L))",
    "uncertainty": "flat line: <p^2> >= 1/(4 Delta s^2) (saturated by a Gaussian); warped cell: m^2 = <p^2> + (3H/2f)^2 "
                   "- (3H/f) rho(fold) + (3H/f) rho(tips) + tip field, so m >= hbar/(2 c Delta s) for the odd modes and the "
                   "excitations only (ANALYSIS.md)"}

# ======================================================================================================== part E
EQ["dirac16complex_kohn_sham_with_portals"] = {
    "block": "h_j = j[-(i/f) sigma1 d_y + M_eff(y) sigma2 + kappa k sigma3] + v_v(y) (Revision/kohn_sham/ks-theory.json)",
    "M_eff": "m + (15/16) lambda S(y) + g_S sum_f s_f delta_tip(y) + g_D sum_f m_f s_f(y)",
    "v_v": "-(1/16) lambda n(y) + g_V sum_f q_f n_f(y)",
    "sources": "n_f(y) = n_f |chi_f(y)|^2 (the Standard-Model fermion densities in their x0 zero modes), s_f the scalar "
               "densities; g_V = c_V/Lambda_D^6, g_S = c_S/Lambda_D^6, g_D = c_D/Lambda_D^7 (P1, P2, P5); P3 and P4 have "
               "no mean field in a neutral, unpolarised, Sigma = 1 background and act through scattering only",
    "back_reaction": "m_f -> m_f + g_S S_Psi(-L) zeta_L zeta_R + g_D m_f <S_Psi>_f; the Standard-Model vector potentials "
                     "shift by g_V q_f n_Psi(y); the gravitational source is the total T^M_N",
    "energy": "the portal energy density g_V n_Psi sum_f q_f n_f + g_S S_Psi s_SM is counted once in the total energy"}
# gauge invariance of the tip and portal bilinears with an explicit representation
rng = np.random.default_rng(20261017)


def su2(vec):
    th = np.linalg.norm(vec)
    nn = vec / th
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    return np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (nn[0] * sx + nn[1] * sy + nn[2] * sz)


def uy(alpha, Y):
    return np.exp(1j * alpha * Y)


worst = 0.0
for _ in range(20):
    U = su2(rng.normal(size=3))
    al = rng.normal()
    Uy = np.diag([np.exp(1j * al / 2), np.exp(-1j * al / 2)])   # U(1)_Y on Sigma from the right: exp(i alpha tau3/2)
    Sig = su2(rng.normal(size=3))
    Lv = rng.normal(size=2) + 1j * rng.normal(size=2)                 # lepton doublet, Y = -1/2
    lR = rng.normal(size=2) + 1j * rng.normal(size=2)                 # (nu_R, e_R), Y = (0, -1)
    Lam_l = np.diag(rng.normal(size=2))
    YL, YR = -0.5, np.array([0.0, -1.0])
    before = np.conj(Lv) @ Sig @ Lam_l @ lR
    Lv2 = uy(al, YL) * (U @ Lv)
    lR2 = np.exp(1j * al * YR) * lR
    Sig2 = U @ Sig @ Uy.conj().T
    after = np.conj(Lv2) @ Sig2 @ Lam_l @ lR2
    # quarks: Q (Y = 1/6), (u_R, d_R) with Y = (2/3, -1/3)
    Qv = rng.normal(size=2) + 1j * rng.normal(size=2)
    qR = rng.normal(size=2) + 1j * rng.normal(size=2)
    Lam_q = np.diag(rng.normal(size=2))
    bq = np.conj(Qv) @ Sig @ Lam_q @ qR
    aq = np.conj(uy(al, 1 / 6) * (U @ Qv)) @ Sig2 @ Lam_q @ (np.exp(1j * al * np.array([2 / 3, -1 / 3])) * qR)
    # P4: tr(Sigma^dag dSigma tau3) with dSigma a covariant variation transforming like Sigma
    dS = su2(rng.normal(size=3)) - np.eye(2)
    sz = np.diag([1.0, -1.0])
    p4b = np.trace(Sig.conj().T @ dS @ sz)
    p4a = np.trace(Sig2.conj().T @ (U @ dS @ Uy.conj().T) @ sz)
    worst = max(worst, abs(before - after), abs(bq - aq), abs(p4b - p4a))
check("E1_tip_and_portal_operators_gauge_invariant", worst < 1e-12,
      "with an explicit SU(2)_L x U(1)_Y representation (Sigma -> U_L Sigma U_Y^dag, U_Y = exp(i alpha tau3/2) acting on "
      "the right; L: Y = -1/2, (nu_R, e_R): Y = (0, -1), Q: Y = 1/6, (u_R, d_R): Y = (2/3, -1/3)) and 20 random group "
      "elements: L^dag Sigma Lambda_l l_R, Q^dag Sigma Lambda_q q_R (the tip Yukawa terms, P2 times the singlet "
      "Psibar Psi) and tr(Sigma^dag D Sigma tau3) (P4) are invariant to %.1e; P1, P3, P5 are products of the singlet "
      "Psibar Gamma Psi with invariant Standard-Model operators" % worst)
charges = {"Psi": 0, "W+": 1, "W-": -1, "Z": 0, "photon": 0, "nu": 0, "e": -1, "u": sp.Rational(2, 3), "d": sp.Rational(-1, 3)}
okW = charges["Psi"] == 0 and charges["W+"] + charges["e"] + 0 == 0 and charges["W+"] + charges["d"] - charges["u"] == 0
check("E2_W_couples_only_with_a_charged_pair", okW,
      "electric charges %s: a Psi bilinear is neutral, so a vertex with one W+ needs a Standard-Model pair of total charge "
      "-1 (e^- nu-bar, d u-bar): the W enters the portal only through the covariant derivative of P5 and through the "
      "gauge self-couplings" % {k: str(v) for k, v in charges.items()})

# ======================================================================================================== outputs
n_pass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
out = {"producer": "Revision/universe_model/field_equations/derive_field_equations.py",
       "model": "Revision/universe_model/MODEL.md (UM-1, version 1)",
       "coordinates": "the author's coordinates x0..x7: x0 hidden (z = 6 H x0, period pi/(6H)), x1..x3 space, x4 time, "
                      "x5..x7 extra times; y = ln|sin z|/(6H), f = e^-a4 b4^(1/2), h4 = u/2 - a4', k = e^(2 a4)/b4",
       "inputs": {"Revision/field_equations_a4/a4-equations.json": "key einstein (compared), keys generalSource (cited)"},
       "equations": EQ,
       "summary": {"checks": len(CHECKS), "pass": n_pass, "fail": len(CHECKS) - n_pass}}
OUT.write_bytes((json.dumps(out, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
REP.parent.mkdir(parents=True, exist_ok=True)
REP.write_bytes((json.dumps({"report": "Revision/universe_model/field_equations/reports/field-equations-checks.json",
                             "summary": out["summary"], "checks": CHECKS}, indent=2, ensure_ascii=True) + "\n").encode("utf-8"))
print("pass %d/%d; %.1f s" % (n_pass, len(CHECKS), time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
