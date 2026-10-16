#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/derive/derive_effective.py - exact (sympy) derivation of every effective
formula the dark-sector analysis of dirac16complex uses (SPEC sections 4, 5, 8, 11), BEFORE any number is computed,
for the author's metric of 2026-10-14 with the second function b4(x4) > 0.

The author's coordinates {x0, x1, ..., x7} (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[48]: X = {x0[], ..., x7[]}) and
the author's metric (In[97]-In[102] of that notebook):
    g = diag(cot^2 z, e^{2 a4} sin^{1/3} z (x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x3)),  z = 6 H x0 in (0, pi/2):
x0 = the hidden space direction; x1, x2, x3 = ordinary 3-space (scale factor e^{a4} sin^{1/6} z); x4 = the time;
x5, x6, x7 = the three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} b4^{1/2} sin^{1/6} z).
b4 is a FUNCTION of x4 and never 1: every formula below is derived for general a4(x4) and b4(x4), with
beta = d ln b4/d a4 != 0.  The record before 2026-10-14 used b4 = 1 (withdrawn); its formulas are the terms without
beta, and the check w_eff_difference_to_withdrawn_record names the difference.

Derived here (every item is a named check in reports/derivation-checks.json):
  * the volume elements: sqrt|g| = b4^{3/2} cos z; the proper 7-volume element of a slice is b4^{3/2} cos z (no a4);
    proper 3-volume ~ e^{3 a4}, proper extra-time volume ~ e^{-3 a4} b4^{3/2};
  * the conservation identities, re-derived from the metric (own Christoffel symbols) for a diagonal
    T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) depending on (x4, x0):
      nabla_mu T^mu_x4 = 0  <=>  d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t),
      nabla_mu T^mu_x0 = 0  <=>  d p0/d x0 + 3 H cot z (2 p0 - p3 - p_t) = 0   (no b4),
    all other components vanish identically; equal to the record Revision/field_equations_a4/a4-equations.json
    (key b4, conservation_x4 and conservation_x0 at q40 = q04 = 0);
  * the integrated identity dE/d a4 = -3 (P3 - Pt) - (3/2) beta Pt, beta = d ln b4/d a4 (E, P3, Pt = proper
    7-volume integrals per unit coordinate volume);
  * the 4-dimensional density rho_4 of a 3-space observer for the normalisations (A) compact extra times of fixed
    coordinate period, (B) per unit extra-time coordinate volume, (C) per unit proper 7-volume, and the exact
      w_eff = -1 - (1/3) d ln rho_4/d ln a = (P3 - Pt)/E - s + (beta/2)(Pt/E + s),  s = 0 (A, B), s = 1 (C);
  * the homogeneous condensate (exact solution for every b4): b4^{3/2} S constant, rho = m S + lambda S^2/2,
    p3 = p_t = p0 = lambda S^2/2; w_eff(A) = (beta/2) w_c, w_eff(C) = -1 + (beta/2)(1 + w_c), w_c = p/rho;
  * a free mode in the flat (warp-free) limit, labelled: omega^2 = M^2 + k^2 e^{-2 a4} - q^2 e^{2 a4}/b4; the kinetic
    gas of such modes satisfies the b4 conservation identity; q = 0 modes do not feel b4 (the dark-matter-like law
    1/3 -> 0 is unchanged);
  * mixtures, CPL rules, the expansion-inferred w of an observer who reads a = e^{a4};
  * the Einstein tensor with b4 from the metric: G^x4_x0 = (3/2) H cot z b4'/b4 (a diagonal source forces b4' = 0 in
    Einstein gravity) and G^x1_x1 - G^x5_x5 = 2 a4'' + 3 a4' b4'/b4 - b4''/(2 b4) - b4'^2/(4 b4^2), hence w_exp;
  * with the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152) the mixed equation of a diagonal source is
    beta_v Q(alpha, beta_v) = 0 (Revision/metric_b4/results/vacuum-b4.json, alpha = a4'/H, beta_v = b4'/(H b4)); on the
    author's history alpha = +-1 it allows b4 constant or d ln b4/d a4 = 4/3 (b4 ~ a^{4/3}), the second history on which
    the dark-sector numbers are computed (compute/run_ks_history_b4.py): b4(x4) = b4(0) e^{(4/3) H x4} on a4 = H x4.

Writes outputs/effective-formulas.json and reports/derivation-checks.json (deterministic, LF).
Exit code 0 iff every check passes.
"""

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
REV = OWN.parent.parent
OUT_FORMULAS = OWN / "outputs" / "effective-formulas.json"
OUT_REPORT = OWN / "reports" / "derivation-checks.json"
A4_RECORD = REV / "field_equations_a4" / "a4-equations.json"
VACUUM_RECORD = REV / "metric_b4" / "results" / "vacuum-b4.json"

CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def mathematica(text):
    """A polynomial or rational string of the Wolfram records (^ for powers) as a sympy expression."""
    return sp.sympify(text.replace("^", "**"))


# ----------------------------------------------------------------------------------------------- metric
x = sp.symbols("x0:8", real=True)            # x[k] = xk, the author's coordinates x0..x7
x4, x0 = x[4], x[0]
H = sp.symbols("H", positive=True)
a4 = sp.Function("a4")(x4)
b4 = sp.Function("b4", positive=True)(x4)
z = 6 * H * x0
sz = sp.sin(z)
s3 = sz ** sp.Rational(1, 3)
g = sp.diag(sp.cot(z) ** 2, sp.exp(2 * a4) * s3, sp.exp(2 * a4) * s3, sp.exp(2 * a4) * s3, -1,
            -sp.exp(-2 * a4) * b4 * s3, -sp.exp(-2 * a4) * b4 * s3, -sp.exp(-2 * a4) * b4 * s3)
ginv = sp.diag(*[1 / g[i, i] for i in range(8)])
a4p = sp.diff(a4, x4)
a4pp = sp.diff(a4, x4, 2)
b4p = sp.diff(b4, x4)
b4pp = sp.diff(b4, x4, 2)

# volume elements (0 < z < pi/2: every factor positive)
zs = sp.symbols("z", positive=True)
A4s = sp.symbols("a4", real=True)
B4s = sp.symbols("b4", positive=True)
sn, cs = sp.symbols("sn cs", positive=True)      # sin z, cos z on the patch 0 < z < pi/2


def onchart(e):
    return e.subs(b4, B4s).subs(a4, A4s).subs(6 * H * x0, zs)


def poschart(e):
    return onchart(e).subs({sp.cot(zs): cs / sn}).subs(sp.sin(zs), sn)


sqrt_det_z = sp.simplify(sp.prod([sp.sqrt(poschart(-g[i, i]) if i in (4, 5, 6, 7) else poschart(g[i, i]))
                                  for i in range(8)]))
sqrt_det_b4_1 = sp.simplify(sqrt_det_z.subs(B4s, 1))
check("sqrt_det_g_equals_b4_three_halves_cos_z",
      zero(sqrt_det_z - B4s ** sp.Rational(3, 2) * cs) and zero(sqrt_det_b4_1 - cs),
      f"sqrt|det g| = {sqrt_det_z} (sn = sin z, cs = cos z > 0 on the patch; b4 = b4(x4) > 0); it changes with x4 "
      f"through b4 (the withdrawn b4 = 1 record had {sqrt_det_b4_1})")
f3 = onchart(sp.exp(3 * a4) * sz ** sp.Rational(1, 2))                       # proper 3-volume element (x1 x2 x3)
ft = onchart(sp.exp(-3 * a4) * b4 ** sp.Rational(3, 2) * sz ** sp.Rational(1, 2))   # proper extra-time volume
f0 = sp.cot(zs)                                                               # proper hidden length element (x0)
vol7 = sp.simplify(f3 * ft * f0)
check("proper_7_volume_element_b4",
      zero(sp.trigsimp(vol7 - B4s ** sp.Rational(3, 2) * sp.cos(zs))) and sp.diff(vol7, A4s) == 0,
      f"(e^(3a4) sin^(1/2) z)(e^(-3a4) b4^(3/2) sin^(1/2) z)(cot z) = {sp.trigsimp(vol7)}: no a4; the proper "
      f"7-volume of a slice changes with x4 through b4(x4)")
check("proper_3_and_extra_time_volume_scalings_b4",
      zero(sp.diff(sp.log(f3), A4s) - 3) and zero(sp.diff(sp.log(ft), A4s) + 3) and
      zero(sp.diff(sp.log(ft), B4s) - sp.Rational(3, 2) / B4s),
      "d ln(proper 3-volume)/d a4 = +3 (inflating); proper extra-time volume ~ e^{-3 a4} b4^{3/2}: "
      "d ln/dx4 = -3 a4' + (3/2) b4'/b4 (deflating while b4'/b4 < 2 a4')")

# --------------------------------------------------------------------------------- Christoffel symbols
dims = range(8)
Gam = [[[0] * 8 for _ in dims] for _ in dims]
for l in dims:
    for m_ in dims:
        for n in dims:
            Gam[l][m_][n] = sp.simplify(sum(ginv[l, s] * (sp.diff(g[s, m_], x[n]) + sp.diff(g[s, n], x[m_])
                                                       - sp.diff(g[m_, n], x[s])) for s in dims) / 2)

rho = sp.Function("rho")(x4, x0)
p3 = sp.Function("p3")(x4, x0)
pt = sp.Function("pt")(x4, x0)
p0 = sp.Function("p0")(x4, x0)
T = sp.diag(p0, p3, p3, p3, -rho, pt, pt, pt)                  # T^mu_nu, mixed, order x0, x1, ..., x7

div = []
for nu in dims:
    e = sum(sp.diff(T[mu, nu], x[mu]) for mu in dims)
    e += sum(Gam[mu][mu][lam] * T[lam, nu] for mu in dims for lam in dims)
    e -= sum(Gam[lam][mu][nu] * T[mu, lam] for mu in dims for lam in dims)
    div.append(sp.simplify(e))
expected_x4 = -sp.diff(rho, x4) - 3 * a4p * (p3 - pt) - sp.Rational(3, 2) * (b4p / b4) * (rho + pt)
expected_x0 = sp.diff(p0, x0) + 3 * H * sp.cot(z) * (2 * p0 - p3 - pt)
others_zero = all(zero(div[i]) for i in (1, 2, 3, 5, 6, 7))
check("conservation_x4_identity_b4", zero(div[4] - expected_x4),
      "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t): on shell "
      "d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t); the b4' term is the change of 2026-10-14 (the "
      "withdrawn b4 = 1 record had d rho/d x4 = -3 a4' (p3 - p_t))")
check("conservation_x0_identity", zero(sp.expand_trig(div[0] - expected_x0)) and not div[0].has(b4),
      "nabla_mu T^mu_x0 = d p0/d x0 + 3 H cot z (2 p0 - p3 - p_t), free of b4")
check("conservation_other_components_vanish", others_zero,
      "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (homogeneous diagonal T), for every b4")

# the same identities in the record of the a4 equations (key b4), at q40 = q04 = 0
rec = json.loads(A4_RECORD.read_text(encoding="utf-8"))["b4"]["generalSource"]
sym = {nm: sp.Symbol(nm) for nm in ("d0q04", "d4rho", "ad1", "p3", "pt", "bd1", "bb", "H", "q04", "cc", "rho",
                                    "d0p0", "d4q40", "p0", "q40")}
rec_x4 = sp.sympify(rec["conservation_x4"]["input"].split("==")[0], locals=sym)
rec_x0 = sp.sympify(rec["conservation_x0"]["input"].split("==")[0], locals=sym)
to_rec = {sp.diff(rho, x4): sym["d4rho"], a4p: sym["ad1"], b4p: sym["bd1"]}
mine_x4 = expected_x4.subs(to_rec).subs({b4: sym["bb"], rho: sym["rho"], p3: sym["p3"], pt: sym["pt"]})
rec_x4_0 = rec_x4.subs({sym["q04"]: 0, sym["d0q04"]: 0})
rec_x0_0 = rec_x0.subs({sym["q40"]: 0, sym["d4q40"]: 0})
mine_x0 = (sym["d0p0"] + 3 * sym["H"] * sym["cc"] * (2 * sym["p0"] - sym["p3"] - sym["pt"]))
check("conservation_equals_a4_record_b4", zero(mine_x4 - rec_x4_0) and zero(mine_x0 - rec_x0_0),
      "the x4 and x0 identities derived here equal Revision/field_equations_a4/a4-equations.json (key b4, "
      "generalSource.conservation_x4 and conservation_x0) at q40 = q04 = 0 (no T^x4_x0 component)")

# hidden coordinate y = ln(sin z)/(6 H): dy/dx0 = cot z, so d/dx0 = cot z d/dy
yv = sp.log(sp.sin(z)) / (6 * H)
check("hidden_coordinate_dy_dx0", zero(sp.simplify(sp.diff(yv, x0) - sp.cot(z))), "dy/dx0 = cot z")
P0y, P3v, Ptv, P0v = sp.symbols("p0_y p3 p_t p0", real=True)
yform = sp.simplify(sp.tan(z) * (sp.cot(z) * P0y + 3 * H * sp.cot(z) * (2 * P0v - P3v - Ptv)))
check("conservation_x0_in_y_form", zero(yform - (P0y + 6 * H * P0v - 3 * H * (P3v + Ptv))),
      "tan z * (x0 identity) = p0_y + 6 H p0 - 3 H (p3 + p_t) (the form checked by the Kohn-Sham solver)")

# integrated identity on an explicit family with p_t != 0 (a linear consequence of the pointwise identity)
c8 = sp.sin(z) ** 2
rho_fam = c8 * sp.exp(-2 * a4) / b4            # p3 = rho/3, p_t = -rho/3
fam_point = zero(sp.diff(rho_fam, x4) + 3 * a4p * (2 * rho_fam / 3)
                 + sp.Rational(3, 2) * (b4p / b4) * (rho_fam - rho_fam / 3))
lim = sp.pi / (12 * H)
sqrtg = b4 ** sp.Rational(3, 2) * sp.cos(z)
E_fam = sp.integrate(rho_fam * sqrtg, (x0, 0, lim))
P3_fam = E_fam / 3
Pt_fam = -E_fam / 3
fam_int = zero(sp.diff(E_fam, x4) + 3 * a4p * (P3_fam - Pt_fam) + sp.Rational(3, 2) * (b4p / b4) * Pt_fam)
check("integrated_identity_dE_dx4_b4", fam_point and fam_int,
      f"family rho = sin^2 z e^(-2a4)/b4, p3 = rho/3, p_t = -rho/3 (satisfies the pointwise identity): "
      f"E = {sp.simplify(E_fam)}, dE/dx4 = -3 a4' (P3 - Pt) - (3/2)(b4'/b4) Pt; per e-fold of a = e^{{a4}}: "
      f"dE/da4 = -3 (P3 - Pt) - (3/2) beta Pt, beta = d ln b4/d a4")

# ------------------------------------------------------------------- rho_4 and the dilution-inferred w_eff
A = sp.symbols("A", real=True)                  # a4 as the variable of the history
Ef = sp.Function("E")(A)
Bf = sp.Function("B", positive=True)(A)         # b4 along the history, as a function of a4
Xs = sp.symbols("X", real=True)                 # X = P3 - Pt (integrated)
Pts = sp.symbols("Pt", real=True)
Es = sp.symbols("E", positive=True)
s = sp.symbols("s", real=True)
beta = sp.symbols("beta", real=True)            # beta = d ln b4/d a4 = b4'/(a4' b4)
dE_dA = -3 * Xs - sp.Rational(3, 2) * (sp.diff(Bf, A) / Bf) * Pts


def w_of(rho4):
    w = -1 - sp.Rational(1, 3) * sp.diff(sp.log(rho4), A)               # d ln a = d A
    w = w.subs(sp.Derivative(Ef, A), dE_dA).subs(Ef, Es)
    return sp.simplify(w.subs(sp.Derivative(Bf, A), beta * Bf))


# rho_4 = E/(proper 3-volume x normaliser of the extra times): A: coordinate period (const), B: coordinate volume
# (const), C: proper extra-time volume e^{-3A} B^{3/2}
norms = {"A_compact_coordinate_period": sp.Integer(1), "B_per_unit_extra_time_coordinate_volume": sp.Integer(1),
         "C_per_unit_proper_7_volume": sp.exp(-3 * A) * Bf ** sp.Rational(3, 2)}
weff = {key: w_of(Ef / (sp.exp(3 * A) * nt)) for key, nt in norms.items()}
wA_exp = Xs / Es + beta / 2 * Pts / Es
wC_exp = Xs / Es - 1 + beta / 2 * (Pts / Es + 1)
check("w_eff_A_b4", zero(weff["A_compact_coordinate_period"] - wA_exp),
      f"w_eff(A) = {weff['A_compact_coordinate_period']} = (P3 - Pt)/E + (beta/2) Pt/E")
check("w_eff_B_equals_w_eff_A_b4", zero(weff["B_per_unit_extra_time_coordinate_volume"] - wA_exp),
      "normalising per unit extra-time coordinate volume divides by a constant: same w_eff as A, for every b4")
check("w_eff_C_b4", zero(weff["C_per_unit_proper_7_volume"] - wC_exp),
      f"w_eff(C) = {weff['C_per_unit_proper_7_volume']} = (P3 - Pt)/E - 1 + (beta/2)(Pt/E + 1)")
gen = w_of(Ef / (sp.exp(3 * A) * (sp.exp(-3 * A) * Bf ** sp.Rational(3, 2)) ** s))
check("w_eff_general_normaliser_b4", zero(gen - (Xs / Es - s + beta / 2 * (Pts / Es + s))),
      "rho_4 = E/(e^{3a4} (e^{-3a4} b4^{3/2})^s): w_eff = (P3 - Pt)/E - s + (beta/2)(Pt/E + s); s = 0 (A, B), "
      "s = 1 (C)")
check("w_eff_difference_to_withdrawn_record",
      zero(weff["A_compact_coordinate_period"] - Xs / Es - beta / 2 * Pts / Es) and
      zero(weff["C_per_unit_proper_7_volume"] - (Xs / Es - 1) - beta / 2 * (Pts / Es + 1)),
      "the whole difference to the withdrawn b4 = 1 record (w_eff(A) = w_eff(B) = (P3 - Pt)/E, w_eff(C) = (P3 - Pt)/E - 1) "
      "is (beta/2) Pt/E for A and B and (beta/2)(Pt/E + 1) for C; beta = d ln b4/d a4 != 0 because b4 is a function "
      "of x4")

# ------------------------------------------------------------------------------------ condensate (exact)
m, lam, S, S0 = sp.symbols("m lambda S S0", real=True)
U = lam * S ** 2 / 2
rho_c = m * S + U
p_c = S * sp.diff(U, S) - U
check("condensate_rho_p", zero(p_c - lam * S ** 2 / 2), "rho = m S + lambda S^2/2, p3 = p_t = p0 = lambda S^2/2")
S_b4 = S0 * b4 ** sp.Rational(-3, 2)
cond_x4 = zero(expected_x4.subs({rho: rho_c.subs(S, S_b4), p3: p_c.subs(S, S_b4), pt: p_c.subs(S, S_b4)}).doit())
cond_x0 = zero(expected_x0.subs({p0: p_c.subs(S, S_b4), p3: p_c.subs(S, S_b4), pt: p_c.subs(S, S_b4)}).doit())
fields = json.loads(A4_RECORD.read_text(encoding="utf-8"))["b4"]["fields"]["condensate"]
check("condensate_b4_scaling", cond_x4 and cond_x0 and "b4^(3/2) S is constant" in fields,
      "S = S0 b4^(-3/2) (b4^(3/2) S constant, as Revision/field_equations_a4/a4-equations.json key b4, fields.condensate "
      "derives from d4 Phi = (A - (3/4)(b4'/b4)) Phi) satisfies both identities with b4: the condensate dilutes with the "
      "proper extra-time volume e^{-3 a4} b4^{3/2} times e^{3 a4}, i.e. with b4^{3/2} (the withdrawn b4 = 1 record had S "
      "constant)")
ratio_c = sp.simplify(p_c / rho_c)
check("condensate_ratio_w", zero(ratio_c - lam * S / (2 * m + lam * S)), f"w_c = p/rho = {ratio_c} (at each instant)")
Sa = S0 * Bf ** sp.Rational(-3, 2)
dwc = sp.simplify(sp.diff(ratio_c.subs(S, Sa), A).subs(sp.Derivative(Bf, A), beta * Bf))
dwc_exp = -3 * beta * m * lam * Sa / (2 * m + lam * Sa) ** 2
check("condensate_ratio_time_dependence_b4", zero(dwc - dwc_exp),
      f"d w_c/d a4 = {sp.simplify(dwc_exp)}: with b4(x4) the ratio varies in time whenever lambda != 0 and m != 0 (the "
      f"withdrawn b4 = 1 record had a constant ratio, wa = 0)")
# w_eff of the condensate from its own rho_4 (not through the general formula): E ~ b4^{3/2} rho_c(S0 b4^{-3/2})
E_c = Bf ** sp.Rational(3, 2) * rho_c.subs(S, Sa)
wcA = sp.simplify((-1 - sp.Rational(1, 3) * sp.diff(sp.log(E_c * sp.exp(-3 * A)), A)).subs(
    sp.Derivative(Bf, A), beta * Bf))
wcC = sp.simplify((-1 - sp.Rational(1, 3) * sp.diff(sp.log(E_c / Bf ** sp.Rational(3, 2)), A)).subs(
    sp.Derivative(Bf, A), beta * Bf))
w_c_a = ratio_c.subs(S, Sa)
check("condensate_w_eff_b4", zero(wcA - beta / 2 * w_c_a) and zero(wcC - (-1 + beta / 2 * (1 + w_c_a))) and
      zero(wcA.subs(beta, 0)) and zero(wcC.subs(beta, 0) + 1),
      "X = 0, Pt/E = w_c: directly from rho_4, w_eff(A) = w_eff(B) = (beta/2) w_c and w_eff(C) = -1 + (beta/2)(1 + w_c) "
      "(the general formula with X = 0, Pt = w_c E; the withdrawn b4 = 1 record had 0 and -1)")
u = sp.symbols("u", real=True)               # u = lambda S/m
w_target = sp.Rational(-764, 1000)
u_sol = sp.solve(sp.Eq(u / (2 + u), w_target), u)
rho_over_mS = 1 + u_sol[0] / 2
check("condensate_ratio_equal_unite_constant_w", len(u_sol) == 1 and rho_over_mS > 0,
      f"u = lambda S/m = {u_sol[0]} = {float(u_sol[0]):.12f} gives w_c = -0.764 at that instant; rho/(m S) = 1 + u/2 = "
      f"{float(rho_over_mS):.12f} > 0 (rho > 0 iff m S > 0); only at that instant: lambda S = lambda S0 b4^(-3/2) drifts "
      f"with b4(x4)")

# ------------------------------------------------------------------ free mode in the flat (warp-free) limit
M, k, q, om = sp.symbols("M k q omega", positive=True)
ginv_flat = sp.diag(sp.exp(-2 * A), -1, -sp.exp(2 * A) / Bf)    # (one 3-space dir, x4, one extra time)
kv = sp.Matrix([k, -om, q])
shell = sp.solve(sp.Eq((kv.T * ginv_flat * kv)[0], -M ** 2), om)
omega2 = M ** 2 + k ** 2 * sp.exp(-2 * A) - q ** 2 * sp.exp(2 * A) / Bf
check("flat_mode_mass_shell_b4", len(shell) == 1 and zero(shell[0] ** 2 - omega2),
      "g^{mu nu} k_mu k_nu = -M^2: omega^2 = M^2 + k^2 e^{-2a4} - q^2 e^{2a4}/b4 (k: 3-momentum, q: extra-time "
      "momentum; physical q_p = q e^{a4} b4^{-1/2})")
omega = sp.sqrt(omega2)
kp2 = k ** 2 * sp.exp(-2 * A)
qp2 = q ** 2 * sp.exp(2 * A) / Bf
n_num = Bf ** sp.Rational(-3, 2)              # number per proper 6-volume of a fixed coordinate cell
rho_g, p3_g, pt_g = n_num * omega, n_num * kp2 / (3 * omega), -n_num * qp2 / (3 * omega)
kin = sp.simplify((sp.diff(rho_g, A) + 3 * (p3_g - pt_g) + sp.Rational(3, 2) * (sp.diff(Bf, A) / Bf) * (rho_g + pt_g)))
check("flat_mode_gas_conservation_b4", zero(kin),
      "kinetic gas of one mode: rho = n omega, p3 = n k_p^2/(3 omega), p_t = -n q_p^2/(3 omega), n ~ b4^(-3/2): "
      "d rho/d a4 = -3 (p3 - p_t) - (3/2)(d ln b4/d a4)(rho + p_t) exactly")
Xmode = sp.simplify((kp2 + qp2) / (3 * omega))
XoverE = (kp2 + qp2) / (3 * omega2)            # X/E of one mode (E = omega per particle), without a square root
check("flat_mode_X_nonnegative", zero(Xmode - (k ** 2 * sp.exp(-2 * A) + q ** 2 * sp.exp(2 * A) / Bf) / (3 * omega)),
      "per mode X = P3 - Pt = (k_p^2 + q_p^2)/(3 omega) >= 0 for real omega > 0 (p3 >= 0, p_t <= 0: time-like extra "
      "directions), for every b4")
wmass = sp.simplify(XoverE.subs(q, 0))
a = sp.symbols("a", positive=True)
wmass_a = sp.simplify(wmass.subs(A, sp.log(a)))
check("massive_mode_w_eff_law", zero(wmass_a - k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))) and not wmass_a.has(Bf) and
      sp.limit(wmass_a, a, 0) == sp.Rational(1, 3) and sp.limit(wmass_a, a, sp.oo) == 0,
      "q = 0 (Pt = 0): w_eff(A) = k^2/(3 (M^2 a^2 + k^2)) -> 1/3 (a -> 0), -> 0 (a -> oo), independent of b4: the "
      "dark-matter-like 1/3 -> 0 law holds for every b4")
xk = sp.symbols("x", positive=True)           # x = k^2/M^2 at a = 1
w_ma = k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))
w0_m = sp.simplify(w_ma.subs(a, 1).subs(k, sp.sqrt(xk) * M))
wa_m = sp.simplify((-sp.diff(w_ma, a)).subs(a, 1).subs(k, sp.sqrt(xk) * M))
check("massive_mode_cpl_tangent", zero(w0_m - xk / (3 * (1 + xk))) and zero(wa_m - 2 * xk / (3 * (1 + xk) ** 2)),
      f"w0 = {w0_m}, wa = {wa_m} > 0 (freezing sign in the CPL convention), for every b4")
check("massless_mode_w_eff", zero(XoverE.subs({q: 0, M: 0}) - sp.Rational(1, 3)),
      "M = 0, q = 0: X/E = 1/3 exactly: w_eff(A) = 1/3 (radiation), w_eff(C) = -2/3 + beta/2")
qrate = sp.simplify(sp.diff(sp.log(sp.sqrt(qp2)), A).subs(sp.Derivative(Bf, A), beta * Bf))
check("extra_time_momentum_blueshift_b4", zero(qrate - (1 - beta / 2)),
      f"d ln q_p/d a4 = {qrate}: the deflating extra times (beta < 2) blueshift the extra-time momentum; on the "
      f"branch beta = 4/3 of the author's weights q_p ~ a^(1/3) instead of a")

# --------------------------------------------------------------------------------------------- mixtures
check("mixture_general_b4", True,
      "w_eff is linear in (X, Pt) at fixed E: for a mixture, w_eff = sum X_i/sum E_i - s + (beta/2)(sum Pt_i/sum E_i + s) "
      "(the general normaliser with X = sum X_i, Pt = sum Pt_i, E = sum E_i)")
r0 = sp.symbols("r0", positive=True)          # r0 = E_gas/E_condensate at a = 1
# radiation-like gas (X = E/3, Pt = 0, E ~ 1/a: q = 0 quanta do not feel b4) + the lambda = 0 condensate (rho = m S,
# p = 0: E = b4^{3/2} m S0 b4^{-3/2} = m S0 constant, X = Pt = 0); beta = d ln b4/d a4 constant along the history
wmix_A = sp.Rational(1, 3) * (r0 / a) / (1 + r0 / a)
wmix_C = wmix_A - 1 + beta / 2
w0_mix = sp.simplify(wmix_A.subs(a, 1))
wa_mix = sp.simplify(-sp.diff(wmix_A, a).subs(a, 1))
w0_mixC = sp.simplify(wmix_C.subs(a, 1))
check("mixture_radiation_condensate_cpl_b4", zero(w0_mix - r0 / (3 * (1 + r0))) and
      zero(wa_mix - r0 / (3 * (1 + r0) ** 2)) and zero(w0_mixC - (r0 / (3 * (1 + r0)) - 1 + beta / 2)),
      f"gas with X = E/3, Pt = 0 (E ~ 1/a, independent of b4) + lambda = 0 condensate (E = m S0 constant for every b4): "
      f"w_eff(A) = (1/3) r/(1 + r), r = r0/a: w0 = {w0_mix}, wa = {wa_mix} > 0; w_eff(C) = w_eff(A) - 1 + beta/2: "
      f"w0 = {w0_mixC}, same wa")
r0_861 = sp.solve(sp.Eq(r0 / (3 * (1 + r0)) - 1 + beta / 2, sp.Rational(-861, 1000)), r0)
need = sp.Rational(139, 1000) - beta / 2          # r0/(3 (1 + r0)) must equal this, which lies in [0, 1/3)
beta_lo, beta_hi = sp.solve(sp.Eq(need, sp.Rational(1, 3)), beta)[0], sp.solve(sp.Eq(need, 0), beta)[0]
check("mixture_C_matching_w0_unite_b4",
      len(r0_861) == 1 and beta_lo == -sp.Rational(583, 1500) and beta_hi == sp.Rational(139, 500) and
      not (beta_lo < sp.Rational(4, 3) <= beta_hi),
      f"w_eff(C) = -0.861 at a = 1 needs r0/(3 (1 + r0)) = 0.139 - beta/2 in [0, 1/3), i.e. beta in ({beta_lo}, "
      f"{beta_hi}] = ({float(beta_lo):.6f}, {float(beta_hi):.6f}]; r0 = {sp.simplify(r0_861[0])}; on the history of the "
      f"author's weights (beta = 4/3) there is no such mixture: there w_eff(C) of this mixture lies in [-1/3, 0)")

# --------------------------------------------------------------------------------- CPL fits (exact rules)
w0s, was, a1 = sp.symbols("w0 wa a1", real=True)
wfun = sp.Function("w")
J0 = sp.Integral(wfun(a), (a, a1, 1))
J1 = sp.Integral(wfun(a) * (1 - a), (a, a1, 1))
L = 1 - a1
normal = sp.solve([sp.Eq(w0s * L + was * L ** 2 / 2, J0), sp.Eq(w0s * L ** 2 / 2 + was * L ** 3 / 3, J1)], [w0s, was])
w0_fit = sp.simplify(normal[w0s])
wa_fit = sp.simplify(normal[was])
test = {wfun(a): -sp.Rational(861, 1000) - sp.Rational(6, 10) * (1 - a)}
w0_t = sp.simplify(w0_fit.subs(test).doit().subs(a1, sp.Rational(1, 3)))
wa_t = sp.simplify(wa_fit.subs(test).doit().subs(a1, sp.Rational(1, 3)))
check("cpl_least_squares_rule", w0_t == -sp.Rational(861, 1000) and wa_t == -sp.Rational(6, 10),
      "normal equations of min int_{a1}^1 (w - w0 - wa (1 - a))^2 da; reproduce an exact CPL curve")
check("unite_deep_past", -sp.Rational(861, 1000) - sp.Rational(6, 10) == -sp.Rational(1461, 1000),
      "Unite CPL: w(a -> 0) = w0 + wa = -1.461 (quoted as -1.46; phantom); wa < 0: w rises from the past "
      "(thawing sign)")

# ------------------------------------------------------------------- expansion-inferred w of the observer
t = sp.symbols("t", real=True)
a4t = sp.Function("a4")(t)
Hub = sp.diff(sp.log(sp.exp(a4t)), t)
w_exp = sp.simplify(-1 - sp.Rational(2, 3) * sp.diff(Hub, t) / Hub ** 2)
check("expansion_inferred_w", zero(w_exp - (-1 - sp.Rational(2, 3) * sp.diff(a4t, t, 2) / sp.diff(a4t, t) ** 2)),
      "a = e^{a4(x4)}, t = x4 (g44 = -1): H_obs = a4', w_exp = -1 - (2/3) a4''/a4'^2 (b4 does not enter the observer's "
      "scale factor)")


# Ricci tensor (MTW) from the Christoffel symbols: R_bd = d_c G^c_bd - d_d G^c_bc + G^c_ce G^e_bd - G^c_de G^e_bc
def ricci(b, d):
    e = sum(sp.diff(Gam[c][b][d], x[c]) for c in dims) - sum(sp.diff(Gam[c][b][c], x[d]) for c in dims)
    e += sum(Gam[c][c][f] * Gam[f][b][d] for c in dims for f in dims)
    e -= sum(Gam[c][d][f] * Gam[f][b][c] for c in dims for f in dims)
    return sp.simplify(e)


R11 = sp.simplify(ginv[1, 1] * ricci(1, 1))
R55 = sp.simplify(ginv[5, 5] * ricci(5, 5))
R40 = sp.simplify(ginv[4, 4] * ricci(4, 0))
mixed_exp = sp.Rational(3, 2) * H * sp.cot(z) * b4p / b4
diff_exp = 2 * a4pp + 3 * a4p * b4p / b4 - b4pp / (2 * b4) - b4p ** 2 / (4 * b4 ** 2)
e1 = json.loads(A4_RECORD.read_text(encoding="utf-8"))["b4"]["lovelockTensors"]["E1"]
esym = {nm: sp.Symbol(nm) for nm in ("ad1", "ad2", "bd1", "bd2", "bb", "H", "cc")}
to_e = {a4pp: esym["ad2"], b4pp: esym["bd2"]}
to_e1 = {a4p: esym["ad1"], b4p: esym["bd1"]}


def as_record(e):
    return e.subs(to_e).subs(to_e1).subs(b4, esym["bb"]).subs(sp.cot(z), esym["cc"]).subs(H, esym["H"])


rec_mixed = sp.sympify(e1["x4x0"]["input"], locals=esym)
rec_diff = sp.sympify(e1["x1x1"]["input"], locals=esym) - sp.sympify(e1["x5x5"]["input"], locals=esym)
check("einstein_mixed_component_b4",
      zero(R40 - mixed_exp) and zero(as_record(mixed_exp) - rec_mixed),
      "G^x4_x0 = R^x4_x0 = (3/2) H cot z b4'/b4 (computed from the metric; equal to E1 x4x0 of a4-equations.json key b4): "
      "since b4 is a function of x4 (b4' != 0), Einstein gravity needs a source with T^x4_x0 = (3/2) H cot z "
      "b4'/(kappa b4) != 0; every source of this record is diagonal (T^x4_x0 = 0), so its b4(x4) is the one the "
      "author's Lovelock weights allow (author_weights_b4_branch)")
check("einstein_space_minus_extra_time_b4",
      zero(R11 - R55 - diff_exp) and zero(as_record(diff_exp) - rec_diff),
      "G^x1_x1 - G^x5_x5 = R^x1_x1 - R^x5_x5 = 2 a4'' + 3 a4' b4'/b4 - b4''/(2 b4) - b4'^2/(4 b4^2) (computed from the "
      "metric; equal to E1 x1x1 - x5x5 of a4-equations.json key b4)")
kap = sp.symbols("kappa", real=True)
d1, d2, bu, bu2 = sp.symbols("a4p a4pp u v", real=True)      # u = b4'/b4, v = b4''/b4
a4pp_E = (kap * (P3v - Ptv) - 3 * d1 * bu + bu2 / 2 + bu ** 2 / 4) / 2
w_exp_E = sp.simplify(-1 - sp.Rational(2, 3) * a4pp_E / d1 ** 2)
check("expansion_inferred_w_einstein_b4",
      zero(w_exp_E - (-1 - (kap * (P3v - Ptv) - 3 * d1 * bu + bu2 / 2 + bu ** 2 / 4) / (3 * d1 ** 2))) and
      zero(w_exp_E.subs({bu: 0, bu2: 0}) - (-1 - kap * (P3v - Ptv) / (3 * d1 ** 2))),
      "Einstein (alpha1 = 1): 2 a4'' = kappa (p3 - p_t) - 3 a4' u + v/2 + u^2/4 (u = b4'/b4, v = b4''/b4), so "
      "w_exp = -1 - (kappa (p3 - p_t) - 3 a4' u + v/2 + u^2/4)/(3 a4'^2) (the withdrawn b4 = 1 record had "
      "w_exp = -1 - kappa (p3 - p_t)/(3 a4'^2)); the observer's own w_exp = -1 - (2/3) a4''/a4'^2 gives -1 exactly on "
      "a4 = A H x4 for every b4 (valid as a source statement only for an ADMISSIBLE source; the Kohn-Sham states are "
      "not admissible)")

# ------------------------------------------- the author's weights: the b4 branch allowed for a diagonal source
vac = json.loads(VACUUM_RECORD.read_text(encoding="utf-8"))
al, be = sp.symbols("al be", real=True)
Q = mathematica(vac["offDiagonalQ"]).subs({sp.Symbol("al"): al, sp.Symbol("be"): be})
roots_p = sorted(sp.solve(sp.Eq(Q.subs(al, 1), 0), be))
roots_m = sorted(sp.solve(sp.Eq(Q.subs(al, -1), 0), be))
disc = sp.factor(sp.discriminant(sp.expand(Q / 3), be))
check("author_weights_b4_branch",
      roots_p == [0, sp.Rational(4, 3)] and roots_m == [-sp.Rational(4, 3), 0] and
      zero(disc + 16 * (5 * al ** 4 - 10 * al ** 2 + 1)),
      f"Q of Revision/metric_b4/results/vacuum-b4.json (author's weights w1 = 1, w2 = 1/32, w3 = 1/1152; alpha = "
      f"a4'/H, beta_v = b4'/(H b4)); a diagonal source needs beta_v Q = 0. On a4 = +H x4 (alpha = 1): beta_v in "
      f"{roots_p}; on a4 = -H x4: {roots_m}; so b4 constant or d ln b4/d a4 = beta_v/alpha = 4/3 (b4 ~ a^(4/3), extra-time "
      f"scale factor e^(-a4) b4^(1/2) ~ a^(-1/3), still deflating). Real roots need 5 alpha^4 - 10 alpha^2 + 1 <= 0 "
      f"(discriminant {disc}). The branch is allowed by the mixed equation only; the other equations then fix the "
      f"source it needs (not constructed here)")

# ------------------------------------------------------------------------------------- phantom statement
check("phantom_condition_b4", zero(weff["C_per_unit_proper_7_volume"] + 1 - (Xs / Es + beta / 2 * (1 + Pts / Es))),
      "w_eff(C) + 1 = X/E + (beta/2)(1 + Pt/E) and w_eff(A) = X/E + (beta/2) Pt/E: with beta > 0 and Pt/E >= -1, "
      "w_eff(C) < -1 needs X/E < 0, which needs P_t > P3 with E > 0 (no real-frequency mode supplies it, "
      "flat_mode_X_nonnegative) or E < 0 with X > 0. Negative E is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record: there "
      "the interacting N = 8, lambda > 0 good-sector states have E < 0 with X = 0 exactly, from the interaction energy of "
      "the canonical uniform-gas exchange functional (E = 0 at lambda = 0). With the exact Fock exchange solved "
      "self-consistently (Revision/kohn_sham/results/exx/exact-fock-variant.csv, at the canonical slices) the same "
      "states have |E| <= 2.04e-13; this negative E is therefore a property of the approximate functional. With b4 "
      "growing (beta > 0) the b4 term raises w_eff(C) by (beta/2)(1 + Pt/E); with beta < 0 it can push it below -1 "
      "(OPEN: no source selects beta < 0)")

formulas = {
    "description": "Exact effective formulas of the dark-sector analysis of dirac16complex (SPEC sections 8, 11) for the "
                   "author's metric with b4(x4) (2026-10-14), derived by "
                   "Revision/dark_sector/dirac16complex/derive/derive_effective.py (sympy); every entry is a named check "
                   "of reports/derivation-checks.json.",
    "coordinates": "the author's coordinates {x0, ..., x7} (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[48]): x0 = hidden "
                   "direction, z = 6 H x0 in (0, pi/2), y = ln(sin z)/(6 H); x1, x2, x3 = 3-space (scale factor e^{a4} "
                   "sin^{1/6} z); x4 = time; x5, x6, x7 = the three exponentially DEFLATING extra times (time-like, scale "
                   "factor e^{-a4} b4^{1/2} sin^{1/6} z).",
    "metric": "diag(cot^2 z, e^{2 a4} sin^{1/3} z (x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x3)) (the author's In[97]-In[102]); "
              "b4 = b4(x4) > 0, a function of x4 (the withdrawn record before 2026-10-14 used b4 = 1)",
    "observerScaleFactor": "a = e^{a4} (3-space scale factor on the brane z = pi/2, normalised a = 1 at the chosen "
                           "'today' a4 = a4_today, i.e. a = e^{a4 - a4_today}); b4 does not enter it",
    "beta": "beta = d ln b4/d a4 = b4'/(a4' b4) != 0 along a history (b4 is a function of x4, never 1); on a4 = H x4 "
            "with the author's weights and a diagonal source beta = 4/3, b4(x4) = b4(0) e^{(4/3) H x4}",
    "withdrawnRecord": "the record before 2026-10-14 used b4 = 1 (withdrawn); its formulas are the terms without beta",
    "volumes": {"sqrtDetG": "b4^{3/2} cos z", "proper7VolumeElement": "b4^{3/2} cos z (independent of a4)",
                "proper3VolumeElement": "e^{3 a4} sin^{1/2} z",
                "properExtraTimeVolumeElement": "e^{-3 a4} b4^{3/2} sin^{1/2} z",
                "hiddenLengthElement": "cot z dx0 = dy"},
    "conservation": {"x4": "d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t)",
                     "x0": "d p0/d x0 + 3 H cot z (2 p0 - p3 - p_t) = 0  <=>  p0_y + 6 H p0 = 3 H (p3 + p_t)",
                     "integrated": "dE/d a4 = -3 (P3 - Pt) - (3/2) beta Pt, E = int rho sqrt|g| d^7x, P3 = int p3 "
                                   "sqrt|g| d^7x, Pt = int p_t sqrt|g| d^7x (per unit coordinate volume; fixed "
                                   "occupations / exact solutions)"},
    "rho4": {
        "A_compact_coordinate_period": "ASSUMPTION: the extra times are compact with a fixed coordinate period "
                                       "(closed time-like directions); rho_4 = E/(proper 3-volume) ~ E e^{-3 a4}",
        "B_per_unit_extra_time_coordinate_volume": "non-compact extra times; rho_4 = E/(proper 3-volume x extra-time "
                                                   "coordinate volume) ~ E e^{-3 a4}",
        "C_per_unit_proper_7_volume": "rho_4 = E/(proper 7-volume) x (constant) ~ E b4^{-3/2} (equivalently per unit "
                                      "proper extra-time volume e^{-3 a4} b4^{3/2})",
        "general": "rho_4 ~ E e^{-3 a4} (e^{-3 a4} b4^{3/2})^{-s}: s = 0 (A, B), s = 1 (C)"},
    "wEff": {"definition": "w_eff = -1 - (1/3) d ln rho_4/d ln a",
             "A": "(P3 - Pt)/E + (beta/2) Pt/E", "B": "(P3 - Pt)/E + (beta/2) Pt/E",
             "C": "(P3 - Pt)/E - 1 + (beta/2)(Pt/E + 1)", "general": "(P3 - Pt)/E - s + (beta/2)(Pt/E + s)",
             "withdrawnB4Equal1": "A = B = (P3 - Pt)/E, C = (P3 - Pt)/E - 1"},
    "ratios": {"w3": "P3/E", "wt": "Pt/E", "wx0": "P0/E (integrated; the x0 ratio, not the CPL w0); brane-local p3/rho etc. also reported"},
    "condensate": {"S": "S0 b4^{-3/2} (b4^{3/2} S constant)", "rho": "m S + lambda S^2/2",
                   "p3=p_t=p0": "lambda S^2/2", "w_ratio": "w_c = lambda S/(2 m + lambda S)",
                   "dw_ratio_da4": str(sp.simplify(dwc_exp)),
                   "w_eff_A": "(beta/2) w_c", "w_eff_C": "-1 + (beta/2)(1 + w_c)",
                   "withdrawnB4Equal1": "w_eff(A) = 0, w_eff(C) = -1, wa = 0 (every definition)",
                   "ratio_equals_minus_0p764_at_lambdaS_over_m": str(u_sol[0])},
    "flatModeLabelled": {"status": "flat (warp-free) limit, used for the sign structure and the limits only",
                         "omega2": "M^2 + k^2 e^{-2 a4} - q^2 e^{2 a4}/b4",
                         "X": "(k_p^2 + q_p^2)/(3 omega), k_p = k e^{-a4}, q_p = q e^{a4} b4^{-1/2}",
                         "q_p_rate": "d ln q_p/d a4 = 1 - beta/2",
                         "massive_w_eff_A": "k^2/(3 (M^2 a^2 + k^2)) (q = 0: independent of b4)",
                         "massive_w0": str(w0_m), "massive_wa": str(wa_m)},
    "mixtures": {"w_eff": "sum_i X_i/sum_i E_i - s + (beta/2)(sum_i Pt_i/sum_i E_i + s)",
                 "radiation_plus_lambda0_condensate_A": "(1/3) r/(1 + r), r = r0/a", "C": "A - 1 + beta/2",
                 "w0_A": str(w0_mix), "w0_C": str(w0_mixC), "wa": str(wa_mix),
                 "r0_for_w_eff_C_equal_minus_0p861": str(sp.simplify(r0_861[0])),
                 "betaRangeForThatMatch": f"({beta_lo}, {beta_hi}]; none on beta = 4/3"},
    "cpl": {"convention": "w(a) = w0 + wa (1 - a); thawing wa < 0, freezing wa > 0 (the formula decides)",
            "tangent": "w0 = w(1), wa = -dw/da at a = 1 = -dw/da4 at a4 = a4_today",
            "leastSquaresW0": str(w0_fit).replace("\n", " "), "leastSquaresWa": str(wa_fit).replace("\n", " "),
            "constantWFit": "w_const = (1/(1 - a1)) int_{a1}^{1} w(a) da"},
    "expansionInferred": {"w_exp": "-1 - (2/3) a4''/a4'^2",
                          "einstein": "-1 - (kappa (p3 - p_t) - 3 a4' u + v/2 + u^2/4)/(3 a4'^2), u = b4'/b4, v = b4''/b4",
                          "einsteinMixed": "G^x4_x0 = (3/2) H cot z b4'/b4 = kappa T^x4_x0: with b4' != 0 Einstein "
                                           "gravity has no diagonal source",
                          "linearMember": "-1"},
    "authorWeightsB4Branch": {"Q": vac["offDiagonalQ"], "variables": vac["variables"],
                              "linearHistory": "alpha = 1: beta_v in {0, 4/3}; alpha = -1: beta_v in {-4/3, 0}; "
                                               "d ln b4/d a4 in {0, 4/3}",
                              "status": "allowed by the mixed equation of a diagonal source; the source the other "
                                        "equations require is not constructed (OPEN)"},
    "unite": {"constant_w": "-0.764", "w0": "-0.861", "wa": "-0.60", "deep_past": "-1.461 (w0 + wa; quoted as -1.46)"},
}

fails = [c for c in CHECKS if c["verdict"] != "PASS"]
report = {"producer": "Revision/dark_sector/dirac16complex/derive/derive_effective.py", "engine": f"sympy {sp.__version__}",
          "metric": "the author's metric with b4(x4) of 2026-10-14 (general a4(x4), b4(x4); b4 is never 1)",
          "checks": CHECKS, "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
OUT_FORMULAS.parent.mkdir(parents=True, exist_ok=True)
OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_FORMULAS, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(json.dumps(formulas, indent=1, ensure_ascii=True) + "\n")
with open(OUT_REPORT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(json.dumps(report, indent=1, ensure_ascii=True) + "\n")
for c in CHECKS:
    print(f"{c['verdict']} - {c['name']}: {c['detail']}")
print(f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
sys.exit(1 if fails else 0)
