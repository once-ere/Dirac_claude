#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/derive/derive_effective.py - exact (sympy) derivation of every effective
formula the dark-sector analysis of dirac16complex uses (SPEC sections 4, 5, 8, 11), BEFORE any number is computed,
for the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1).

The author's coordinates {x0, x1, ..., x7} and the corrected metric
    g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),  z = 6 H x0 real:
x0 = the hidden space direction; x1, x2, x3 = ordinary 3-space (scale factor e^{a4}); x4 = the time; x5, x6, x7 = the
three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); the hidden
direction carries the same factor e^{-a4} b4^{1/2}.  b4 is a FUNCTION of x4: every formula below is derived for general
a4(x4) and b4(x4), with beta = d ln b4/d a4.  The record's history is a4 = H x4, b4 = e^{(4/3) H x4} (beta = 4/3;
Revision/kohn_sham/ks-theory.json adiabaticity.historyBeta), a PRESCRIBED background: with the author's weights it needs
the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam of
Revision/field_equations_a4/a4-equations.json, which the Kohn-Sham gas does not supply.

Every real z: the x0 dependence enters only through C = cot z (signed) and W = (sin^2 z)^{1/12} > 0, with the exact
derivative rules dC/dx0 = -6 H (1 + C^2) and dW/dx0 = H C W (valid wherever sin z != 0); no branch of sin z is chosen.

Derived here (every item is a named check in reports/derivation-checks.json):
  * the volume elements: sqrt|g| = e^{-a4} b4^2 |C| W^3; proper 3-volume e^{3 a4}; proper extra-time volume
    e^{-3 a4} b4^{3/2} W^3; proper hidden length e^{-a4} b4^{1/2} |C| dx0 = f |dy| (y = ln|sin z|/(6H), f = e^{-a4} b4^{1/2});
    the proper 7-volume of a cell Vol_7 ~ e^{-a4} b4^2;
  * the conservation identities from the metric (own Christoffel symbols) for a diagonal T = diag(p0, p3 (x3), -rho,
    p_t (x3)) depending on (x4, x0): nabla_mu T^mu_x4 = 0 <=> d4 rho = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t),
    h4 = u/2 - a4', u = b4'/b4; nabla_mu T^mu_x0 = 0 <=> d0 p0 + 3 H cot z (p0 - p_t) = 0 <=> p0_y + 3 H (p0 - p_t) = 0;
    equal to the record (a4-equations.json generalSource.conservation_x4, conservation_x0 at q40 = q04 = 0, energyExchange);
  * the integrated identity dE/dx4 = -3 a4' P3 - h4 (P0 + 3 Pt), i.e. dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt)
    (beta = 4/3: -3 P3 + Pt + P0/3, ks-theory.json emt.energyChange), on two explicit families;
  * the 4-dimensional density rho_4 of a 3-space observer for the normalisations (A) compact extra times and hidden
    direction of fixed coordinate period, (B) per unit coordinate volume of the extra times and the hidden direction,
    (C) per unit proper 7-volume, and the exact w_eff = -1 - (1/3) d ln rho_4/d ln a;
  * the homogeneous condensate (a4-equations.json fields.dirac16complex00.homogeneousCondensate): S ~ e^{a4} b4^{-2},
    rho = m S + lambda S^2/2, p3 = p_t = p0 = lambda S^2/2, its w_eff;
  * a free mode in the flat (warp-free) limit, labelled: omega^2 = M^2 + k^2 e^{-2 a4} + l^2 e^{2 a4}/b4 - q^2 e^{2 a4}/b4
    (l: hidden momentum, q: extra-time momentum); its kinetic gas satisfies the conservation identity; the
    dark-matter-like law 1/3 -> 0 of a massive 3-space quantum; the fold band eps = e^{-a4} |k| of the Kohn-Sham record
    is a massless 3-space quantum (w_eff(A) = 1/3);
  * mixtures, CPL rules, the expansion-inferred w of an observer who reads a = e^{a4};
  * the Einstein tensor from the metric: no mixed component (G^x4_x0 = 0 for every a4, b4), G^x1_x1 - G^x5_x5 equal to
    the record, and w_exp with an Einstein source;
  * the record's history and the source it needs (a prescribed background).

Usage: python Revision/dark_sector/dirac16complex/derive/derive_effective.py
Writes outputs/effective-formulas.json and reports/derivation-checks.json (deterministic, LF).
Exit code 0 iff every check passes.
"""

import json
import os
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
REV = Path(os.environ["REVISION_DIR"]) if os.environ.get("REVISION_DIR") else OWN.parent.parent
OUT_FORMULAS = OWN / "outputs" / "effective-formulas.json"
OUT_REPORT = OWN / "reports" / "derivation-checks.json"
A4_RECORD = REV / "field_equations_a4" / "a4-equations.json"
KS_THEORY = REV / "kohn_sham" / "ks-theory.json"

CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


rec_all = json.loads(A4_RECORD.read_text(encoding="utf-8"))
if "corrected primordial metric of 2026-10-16" not in rec_all["title"]:
    print("ERROR  a4-equations.json is not the record of the corrected metric")
    sys.exit(1)
kst = json.loads(KS_THEORY.read_text(encoding="utf-8"))

# ----------------------------------------------------------------------------------------------- metric
x = sp.symbols("x0:8", real=True)            # x[k] = xk, the author's coordinates x0..x7
x4, x0 = x[4], x[0]
H = sp.symbols("H", positive=True)
a4 = sp.Function("a4")(x4)
b4 = sp.Function("b4", positive=True)(x4)
C = sp.symbols("C", real=True)               # cot z, signed (every real z)
W = sp.symbols("W", positive=True)           # (sin^2 z)^(1/12) > 0
dC = -6 * H * (1 + C ** 2)                   # dC/dx0
dW = H * C * W                               # dW/dx0
g = sp.diag(sp.exp(-2 * a4) * b4 * C ** 2, sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4), -1,
            -sp.exp(-2 * a4) * b4 * W ** 2, -sp.exp(-2 * a4) * b4 * W ** 2, -sp.exp(-2 * a4) * b4 * W ** 2)
ginv = sp.diag(*[1 / g[i, i] for i in range(8)])
a4p = sp.diff(a4, x4)
a4pp = sp.diff(a4, x4, 2)
b4p = sp.diff(b4, x4)
b4pp = sp.diff(b4, x4, 2)
dims = range(8)


def D(e, mu):
    """partial derivative along x_mu: the x0 dependence through C, W (and explicit x0), the x4 dependence through
    a4, b4 and the source functions; nothing depends on x1..x3, x5..x7"""
    if mu == 0:
        return sp.diff(e, x0) + sp.diff(e, C) * dC + sp.diff(e, W) * dW
    if mu == 4:
        return sp.diff(e, x4)
    return sp.Integer(0)


# the derivative rules are exact: check them against the trigonometric forms on both signs of sin z
z = 6 * H * x0
Cz = sp.cot(z)
Wz_pos = sp.sin(z) ** sp.Rational(1, 6)                # (sin^2)^(1/12) where sin z > 0
Wz_neg = (-sp.sin(z)) ** sp.Rational(1, 6)             # where sin z < 0
rule_C = zero(sp.diff(Cz, x0) - dC.subs(C, Cz))
rule_W = all(zero(sp.simplify(sp.diff(Wz, x0) - (H * Cz * Wz))) for Wz in (Wz_pos, Wz_neg))
check("x0_derivative_rules_every_real_z", rule_C and rule_W,
      "C = cot z and W = (sin^2 z)^(1/12) satisfy dC/dx0 = -6 H (1 + C^2) and dW/dx0 = H C W on both signs of sin z "
      "(W = (+-sin z)^(1/6)); every x0 derivative below uses only these rules, so every statement holds for every real z "
      "with sin z != 0 (no branch of sin z chosen)")

A4s = sp.symbols("a4", real=True)
B4s = sp.symbols("b4", positive=True)


def onchart(e):
    return e.subs(b4, B4s).subs(a4, A4s)


sqrt_det = sp.sqrt(sp.prod([onchart(-g[i, i] if i >= 4 else g[i, i]) for i in range(8)]))
sqrt_det = sp.simplify(sp.powsimp(sp.powdenest(sqrt_det, force=False)))
Cabs = sp.Abs(C)
check("sqrt_det_g", zero(sp.simplify(sqrt_det ** 2 - (sp.exp(-A4s) * B4s ** 2 * C * W ** 3) ** 2)),
      f"|det g| = (e^(-a4) b4^2 |C| W^3)^2: sqrt|g| = e^(-a4) b4^2 |cot z| |sin z|^(1/2) (C = cot z, W^3 = |sin z|^(1/2)); "
      f"it changes with x4 through e^(-a4) b4^2")
f3 = sp.exp(3 * A4s)                                      # proper 3-volume element (x1 x2 x3)
ft = sp.exp(-3 * A4s) * B4s ** sp.Rational(3, 2) * W ** 3   # proper extra-time volume element
fh = sp.exp(-A4s) * B4s ** sp.Rational(1, 2) * Cabs        # proper hidden length element (x0)
vol7 = sp.simplify(f3 * ft * fh)
check("proper_volume_elements",
      zero(sp.simplify(vol7 ** 2 - (sp.exp(-A4s) * B4s ** 2 * C * W ** 3) ** 2)) and zero(sp.diff(sp.log(f3), A4s) - 3)
      and zero(sp.diff(sp.log(ft), A4s) + 3) and zero(sp.diff(sp.log(ft), B4s) - sp.Rational(3, 2) / B4s)
      and zero(sp.diff(sp.log(fh), A4s) + 1) and zero(sp.diff(sp.log(fh), B4s) - sp.Rational(1, 2) / B4s),
      "proper 3-volume e^(3 a4) (inflating); proper extra-time volume e^(-3 a4) b4^(3/2) W^3; proper hidden length "
      "e^(-a4) b4^(1/2) |cot z| dx0 = f |dy|, f = e^(-a4) b4^(1/2) (y = ln|sin z|/(6H), dy = cot z dx0); their product is "
      "sqrt|g|: the proper 7-volume of a cell is Vol_7 ~ e^(-a4) b4^2 = e^((2 beta - 1) a4) on b4 ~ e^(beta a4)")
yv_pos = sp.log(sp.sin(z)) / (6 * H)
yv_neg = sp.log(-sp.sin(z)) / (6 * H)
check("hidden_coordinate_dy_dx0", zero(sp.simplify(sp.diff(yv_pos, x0) - Cz)) and zero(sp.simplify(sp.diff(yv_neg, x0) - Cz)),
      "y = ln|sin z|/(6H): dy/dx0 = cot z on both signs of sin z, so d/dx0 = cot z d/dy and |sin z| = e^(6Hy)")

# --------------------------------------------------------------------------------- Christoffel symbols
Gam = [[[0] * 8 for _ in dims] for _ in dims]
for l in dims:
    for m_ in dims:
        for n in dims:
            Gam[l][m_][n] = sp.simplify(sum(ginv[l, s] * (D(g[s, m_], n) + D(g[s, n], m_) - D(g[m_, n], s))
                                            for s in dims) / 2)

rho = sp.Function("rho")(x4, x0)
p3 = sp.Function("p3")(x4, x0)
pt = sp.Function("pt")(x4, x0)
p0 = sp.Function("p0")(x4, x0)
T = sp.diag(p0, p3, p3, p3, -rho, pt, pt, pt)                  # T^mu_nu, mixed, order x0, x1, ..., x7

div = []
for nu in dims:
    e = sum(D(T[mu, nu], mu) for mu in dims)
    e += sum(Gam[mu][mu][lam] * T[lam, nu] for mu in dims for lam in dims)
    e -= sum(Gam[lam][mu][nu] * T[mu, lam] for mu in dims for lam in dims)
    div.append(sp.simplify(e))
u_ = b4p / b4
h4 = u_ / 2 - a4p
expected_x4 = -sp.diff(rho, x4) - 3 * a4p * (rho + p3) - h4 * (rho + p0) - 3 * h4 * (rho + pt)
expected_x0 = sp.diff(p0, x0) + 3 * H * C * (p0 - pt)
others_zero = all(zero(div[i]) for i in (1, 2, 3, 5, 6, 7))
check("conservation_x4_identity", zero(div[4] - expected_x4),
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t), h4 = u/2 - a4', u = b4'/b4 (the "
      "expansion rate of the hidden direction and of each extra time): on shell d4 rho = -3 a4' (rho + p3) - h4 (rho + p0) "
      "- 3 h4 (rho + p_t), for every a4(x4), b4(x4) and every real z")
check("conservation_x0_identity", zero(div[0] - expected_x0) and not div[0].has(b4),
      "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t), free of a4 and b4")
check("conservation_other_components_vanish", others_zero,
      "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (T depends on x4 and x0 only)")
P0y, P3v, Ptv, P0v = sp.symbols("p0_y p3 p_t p0", real=True)
yform = sp.expand((C * P0y + 3 * H * C * (P0v - Ptv)) / C)
check("conservation_x0_in_y_form", zero(yform - (P0y + 3 * H * (P0v - Ptv))) and
      kst["emt"]["conservationY"].startswith("p0' + 3H (p0 - p_t) = 0"),
      "with d0 = cot z d_y: (x0 identity)/cot z = p0_y + 3 H (p0 - p_t), the identity of ks-theory.json emt.conservationY "
      "that the Kohn-Sham solvers check on every state")

# the same identities in the record of the a4 equations (generalSource), without an off-diagonal source
gs = rec_all["generalSource"]
sym = {nm: sp.Symbol(nm) for nm in ("d0q04", "d4rho", "ad1", "p3", "pt", "uu", "H", "q04", "cc", "rho", "d0p0", "d4q40",
                                    "p0", "q40", "tt", "kk")}
rec_x4 = sp.sympify(gs["conservation_x4"]["input"].split("==")[0].replace("^", "**"), locals=sym)
rec_x0 = sp.sympify(gs["conservation_x0"]["input"].split("==")[0].replace("^", "**"), locals=sym)
rec_ex = sp.sympify(gs["energyExchange"]["input"].split("==")[0].replace("^", "**"), locals=sym)
to_rec = {sp.diff(rho, x4): sym["d4rho"], b4p: sym["uu"] * b4, a4p: sym["ad1"]}
mine_x4 = sp.simplify(expected_x4.subs(to_rec).subs({rho: sym["rho"], p3: sym["p3"], pt: sym["pt"], p0: sym["p0"]}))
mine_x0 = sym["d0p0"] + 3 * sym["H"] * sym["cc"] * (sym["p0"] - sym["pt"])
rec_x4_0 = rec_x4.subs({sym["q04"]: 0, sym["d0q04"]: 0})
rec_x0_0 = rec_x0.subs({sym["q40"]: 0, sym["d4q40"]: 0, sym["q04"]: 0})
ex_mine = mine_x4.subs(sym["pt"], sym["p0"])
check("conservation_equals_a4_record", zero(mine_x4 - rec_x4_0) and zero(mine_x0 - rec_x0_0) and zero(ex_mine - rec_ex),
      "the x4 and x0 identities derived here equal Revision/field_equations_a4/a4-equations.json generalSource."
      "conservation_x4 and conservation_x0 at q40 = q04 = 0 (no T^x4_x0), and with p_t = p0 the record's energyExchange "
      "-d4 rho - 3 a4' (p3 + rho) - 4 h4 (p0 + rho) = 0")

# integrated identity: E = int sqrt|g| rho dx0 (per unit coordinate volume of x1..x3, x5..x7)
# family 1: the x0-averaged free fold-band gas (Kohn-Sham record: every occupied orbital (e^{f M y}, 0), eps = e^{-a4}|k|)
R = sp.Function("R")(x0)
rho_f1 = R * b4 ** -2
sub_f1 = {rho: rho_f1, p3: rho_f1 / 3, p0: 0, pt: 0}
f1_point = zero(expected_x4.subs(sub_f1).doit()) and zero(expected_x0.subs(sub_f1).doit())
I_R = sp.Symbol("I_R")                 # int R |cot z| W^3 dx0 over the cell (a constant)
E_f1 = sp.exp(-a4) * b4 ** 2 * b4 ** -2 * I_R
dE_rule = lambda E_, P3_, Pt_, P0_: -3 * a4p * P3_ - h4 * (P0_ + 3 * Pt_)   # noqa: E731
f1_int = zero(sp.diff(E_f1, x4) - dE_rule(E_f1, E_f1 / 3, 0, 0))
# family 2: a homogeneous perfect fluid p3 = p_t = p0 = w rho (x0-independent)
wv = sp.symbols("w", real=True)
Vt = sp.exp(-a4) * b4 ** 2
rho_f2 = Vt ** (-(1 + wv))
sub_f2 = {rho: rho_f2, p3: wv * rho_f2, pt: wv * rho_f2, p0: wv * rho_f2}
f2_point = zero(sp.simplify(expected_x4.subs(sub_f2).doit())) and zero(expected_x0.subs(sub_f2).doit())
I1 = sp.Symbol("I_1")                  # int |cot z| W^3 dx0 (a constant)
E_f2 = Vt * rho_f2 * I1
f2_int = zero(sp.simplify(sp.diff(E_f2, x4) - dE_rule(E_f2, wv * E_f2, wv * E_f2, wv * E_f2)))
beta = sp.symbols("beta", real=True)
check("integrated_identity_dE_dx4", f1_point and f1_int and f2_point and f2_int,
      "for sources that satisfy both pointwise identities, E = int sqrt|g| rho dx0 obeys dE/dx4 = -3 a4' P3 - h4 (P0 + 3 Pt) "
      "(P = int sqrt|g| p dx0), i.e. dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt), beta = d ln b4/d a4; checked on the x0-averaged "
      "free fold-band gas rho = R(x0) b4^(-2), p3 = rho/3, p0 = p_t = 0 (E ~ e^(-a4) for every b4) and on the homogeneous "
      "fluid p = w rho, rho ~ (e^(-a4) b4^2)^(-(1 + w)) (E ~ (e^(-a4) b4^2)^(-w)); at beta = 4/3: dE/da4 = -3 P3 + Pt + P0/3")
hist_rule = sp.expand(-3 * P3v - (sp.Rational(4, 3) / 2 - 1) * (P0v + 3 * Ptv))
check("integrated_identity_equals_ks_theory", zero(hist_rule - (-3 * P3v + Ptv + P0v / 3)) and
      kst["emt"]["energyChange"].replace(" ", "").find("-3P3+P_t+P0/3") >= 0,
      "at beta = 4/3 the rule is dE/da4 = -3 P3 + Pt + P0/3, the identity of ks-theory.json emt.energyChange that the "
      "Kohn-Sham record satisfies along its history (fixed occupations)")

# ------------------------------------------------------------------- rho_4 and the dilution-inferred w_eff
A = sp.symbols("A", real=True)                  # a4 as the variable of the history
Ef = sp.Function("E")(A)
Bf = sp.Function("B", positive=True)(A)         # b4 along the history, as a function of a4
Es = sp.symbols("E", positive=True)
P3s, Pts, P0s = sp.symbols("P3 Pt P0", real=True)
s = sp.symbols("s", real=True)
dE_dA = -3 * P3s - (sp.diff(Bf, A) / (2 * Bf) - 1) * (P0s + 3 * Pts)


def w_of(rho4):
    w = -1 - sp.Rational(1, 3) * sp.diff(sp.log(rho4), A)               # d ln a = d A
    w = w.subs(sp.Derivative(Ef, A), dE_dA).subs(Ef, Es)
    return sp.simplify(w.subs(sp.Derivative(Bf, A), beta * Bf))


# rho_4 = E/(proper 3-volume x normaliser of the extra times and the hidden direction): A: coordinate period (const),
# B: coordinate volume (const), C: their proper volume e^{-4A} B^2 (so that E/(e^{3A} e^{-4A} B^2) = E/Vol_7)
norms = {"A_compact_coordinate_period": sp.Integer(1), "B_per_unit_coordinate_volume": sp.Integer(1),
         "C_per_unit_proper_7_volume": sp.exp(-4 * A) * Bf ** 2}
weff = {key: w_of(Ef / (sp.exp(3 * A) * nt)) for key, nt in norms.items()}
wA_exp = P3s / Es + (beta / 2 - 1) * (P0s + 3 * Pts) / (3 * Es)
wC_exp = wA_exp - (4 - 2 * beta) / 3
check("w_eff_A", zero(weff["A_compact_coordinate_period"] - wA_exp),
      f"w_eff(A) = {weff['A_compact_coordinate_period']} = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) (= P3/E - (P0 + 3 Pt)/(9E) "
      f"at beta = 4/3)")
check("w_eff_B_equals_w_eff_A", zero(weff["B_per_unit_coordinate_volume"] - wA_exp),
      "normalising per unit coordinate volume of the extra times and the hidden direction divides by a constant: the same "
      "w_eff as A, for every b4")
check("w_eff_C", zero(weff["C_per_unit_proper_7_volume"] - wC_exp),
      f"w_eff(C) = {weff['C_per_unit_proper_7_volume']} = w_eff(A) - (4 - 2 beta)/3 (= w_eff(A) - 4/9 at beta = 4/3): "
      f"rho_4 ~ E/Vol_7, Vol_7 ~ e^(-a4) b4^2")
gen = w_of(Ef / (sp.exp(3 * A) * (sp.exp(-4 * A) * Bf ** 2) ** s))
check("w_eff_general_normaliser", zero(gen - (wA_exp - s * (4 - 2 * beta) / 3)),
      "rho_4 = E/(e^(3a4) (e^(-4a4) b4^2)^s): w_eff = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3; s = 0 (A, B), "
      "s = 1 (C)")

# ------------------------------------------------------------------------------------ condensate (exact)
m, lam, S, S0 = sp.symbols("m lambda S S0", real=True)
U = lam * S ** 2 / 2
rho_c = m * S + U
p_c = S * sp.diff(U, S) - U
check("condensate_rho_p", zero(p_c - lam * S ** 2 / 2), "rho = m S + lambda S^2/2, p3 = p_t = p0 = S U' - U = lambda S^2/2")
cond_rec = rec_all["fields"]["dirac16complex00"]["homogeneousCondensate"]
S_law = S0 * sp.exp(a4) * b4 ** -2
sub_c = {rho: rho_c.subs(S, S_law), p3: p_c.subs(S, S_law), pt: p_c.subs(S, S_law), p0: p_c.subs(S, S_law)}
cond_x4 = zero(sp.simplify(expected_x4.subs(sub_c).doit()))
cond_x0 = zero(expected_x0.subs(sub_c).doit())
check("condensate_scaling", cond_x4 and cond_x0 and "S = e^{a4} b4^{-2} S0 (exact)" in cond_rec,
      "S = S0 e^(a4) b4^(-2) (a4-equations.json fields.dirac16complex00.homogeneousCondensate) satisfies both identities: the "
      "condensate dilutes with the proper 7-volume e^(-a4) b4^2 (S Vol_7 constant)")
ratio_c = sp.simplify(p_c / rho_c)
check("condensate_ratio_w", zero(ratio_c - lam * S / (2 * m + lam * S)), f"w_c = p/rho = {ratio_c} (at each instant)")
Sa = S0 * sp.exp(A) * Bf ** -2
dwc = sp.simplify(sp.diff(ratio_c.subs(S, Sa), A).subs(sp.Derivative(Bf, A), beta * Bf))
dwc_exp = (1 - 2 * beta) * 2 * m * lam * Sa / (2 * m + lam * Sa) ** 2
check("condensate_ratio_time_dependence", zero(dwc - dwc_exp),
      f"d w_c/d a4 = {sp.simplify(dwc_exp)}: lambda S falls like e^((1 - 2 beta) a4) (e^(-(5/3) a4) at beta = 4/3), so the "
      f"ratio varies in time whenever lambda != 0 and m != 0")
E_c = sp.exp(-A) * Bf ** 2 * rho_c.subs(S, Sa)             # E = Vol_7 rho (per coordinate cell)
wcA = sp.simplify((-1 - sp.Rational(1, 3) * sp.diff(sp.log(E_c * sp.exp(-3 * A)), A)).subs(sp.Derivative(Bf, A), beta * Bf))
wcC = sp.simplify((-1 - sp.Rational(1, 3) * sp.diff(sp.log(E_c / (sp.exp(-A) * Bf ** 2)), A)).subs(
    sp.Derivative(Bf, A), beta * Bf))
w_c_a = ratio_c.subs(S, Sa)
gen_c = wA_exp.subs({P3s: w_c_a * Es, Pts: w_c_a * Es, P0s: w_c_a * Es})
check("condensate_w_eff", zero(wcA - (2 * beta - 1) / 3 * w_c_a) and zero(wcC - (wcA - (4 - 2 * beta) / 3)) and
      zero(gen_c - (2 * beta - 1) / 3 * w_c_a),
      "directly from rho_4: w_eff(A) = w_eff(B) = ((2 beta - 1)/3) w_c (5/9 w_c at beta = 4/3) and w_eff(C) = w_eff(A) - "
      "(4 - 2 beta)/3; the general formula with P3 = Pt = P0 = w_c E gives the same")
uu = sp.symbols("u", real=True)               # u = lambda S/m
w_target = sp.Rational(-764, 1000)
u_sol = sp.solve(sp.Eq(uu / (2 + uu), w_target), uu)
rho_over_mS = 1 + u_sol[0] / 2
check("condensate_ratio_equal_unite_constant_w", len(u_sol) == 1 and rho_over_mS > 0,
      f"u = lambda S/m = {u_sol[0]} = {float(u_sol[0]):.12f} gives w_c = -0.764 at that instant; rho/(m S) = 1 + u/2 = "
      f"{float(rho_over_mS):.12f} > 0; w_eff(A) = (5/9) w_c at beta = 4/3, and only at that instant (lambda S drifts)")

# ------------------------------------------------------------------ free mode in the flat (warp-free) limit
M, k, l_, q, om = sp.symbols("M k l q omega", positive=True)
ginv_flat = sp.diag(sp.exp(-2 * A), -1, sp.exp(2 * A) / Bf, -sp.exp(2 * A) / Bf)   # (one 3-space dir, x4, x0, one extra time)
kv = sp.Matrix([k, -om, l_, q])
shell = sp.solve(sp.Eq((kv.T * ginv_flat * kv)[0], -M ** 2), om)
omega2 = M ** 2 + k ** 2 * sp.exp(-2 * A) + l_ ** 2 * sp.exp(2 * A) / Bf - q ** 2 * sp.exp(2 * A) / Bf
check("flat_mode_mass_shell", len(shell) == 1 and zero(shell[0] ** 2 - omega2),
      "g^{mu nu} k_mu k_nu = -M^2 with the warp factors set to 1: omega^2 = M^2 + k^2 e^(-2a4) + l^2 e^(2a4)/b4 - "
      "q^2 e^(2a4)/b4 (k: 3-momentum, l: hidden momentum, q: extra-time momentum; physical l_p = l e^(a4) b4^(-1/2), "
      "q_p = q e^(a4) b4^(-1/2))")
omega = sp.sqrt(omega2)
kp2 = k ** 2 * sp.exp(-2 * A)
lp2 = l_ ** 2 * sp.exp(2 * A) / Bf
qp2 = q ** 2 * sp.exp(2 * A) / Bf
n_num = sp.exp(A) * Bf ** -2                 # number per proper 7-volume of a fixed coordinate cell
rho_g, p3_g, p0_g, pt_g = n_num * omega, n_num * kp2 / (3 * omega), n_num * lp2 / omega, -n_num * qp2 / (3 * omega)
bet_ = sp.diff(Bf, A) / Bf
kin = sp.simplify(sp.diff(rho_g, A) + 3 * (rho_g + p3_g) + (bet_ / 2 - 1) * (rho_g + p0_g) + 3 * (bet_ / 2 - 1) * (rho_g + pt_g))
check("flat_mode_gas_conservation", zero(kin),
      "kinetic gas of one mode: rho = n omega, p3 = n k_p^2/(3 omega), p0 = n l_p^2/omega, p_t = -n q_p^2/(3 omega), "
      "n ~ e^(a4) b4^(-2): d rho/d a4 = -3 (rho + p3) - (beta/2 - 1)(rho + p0) - 3 (beta/2 - 1)(rho + p_t) exactly (the "
      "x4 identity per unit a4)")
wmode = sp.simplify(-sp.Rational(1, 3) * sp.diff(sp.log(omega.subs({l_: 0, q: 0})), A))
a = sp.symbols("a", positive=True)
wmass_a = sp.simplify(wmode.subs(A, sp.log(a)))
check("massive_mode_w_eff_law", zero(wmass_a - k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))) and not wmass_a.has(Bf) and
      sp.limit(wmass_a, a, 0) == sp.Rational(1, 3) and sp.limit(wmass_a, a, sp.oo) == 0,
      "l = q = 0 (a 3-space quantum, E ~ omega per particle): w_eff(A) = -(1/3) d ln omega/d a4 = k^2/(3 (M^2 a^2 + k^2)) "
      "-> 1/3 (a -> 0), -> 0 (a -> oo), independent of b4: the dark-matter-like 1/3 -> 0 law")
xk = sp.symbols("x", positive=True)           # x = k^2/M^2 at a = 1
w_ma = k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))
w0_m = sp.simplify(w_ma.subs(a, 1).subs(k, sp.sqrt(xk) * M))
wa_m = sp.simplify((-sp.diff(w_ma, a)).subs(a, 1).subs(k, sp.sqrt(xk) * M))
check("massive_mode_cpl_tangent", zero(w0_m - xk / (3 * (1 + xk))) and zero(wa_m - 2 * xk / (3 * (1 + xk) ** 2)),
      f"w0 = {w0_m}, wa = {wa_m} > 0 (freezing sign in the CPL convention), for every b4")
eps_fold = sp.exp(-A) * k
check("fold_band_quantum_w_eff", zero(-sp.Rational(1, 3) * sp.diff(sp.log(eps_fold), A) - sp.Rational(1, 3)) and
      kst["checksNumeric"]["braneBandSlopeFormula"].find("e^{-a4,0}") >= 0,
      "the occupied fold band of the Kohn-Sham record, eps = e^(-a4) |k| exactly (ks-theory.json, slope c = e^(-a4,0)), is a "
      "massless 3-space quantum: w_eff(A) = -(1/3) d ln eps/d a4 = 1/3 (radiation-like) for every b4; w_eff(C) = 1/3 - "
      "(4 - 2 beta)/3 = -1/9 at beta = 4/3")
qrate = sp.simplify(sp.diff(sp.log(sp.sqrt(qp2)), A).subs(sp.Derivative(Bf, A), beta * Bf))
check("extra_time_momentum_blueshift", zero(qrate - (1 - beta / 2)),
      f"d ln q_p/d a4 = d ln l_p/d a4 = {qrate}: the deflating extra times and hidden direction (beta < 2) blueshift their "
      f"momenta; at beta = 4/3, q_p ~ a^(1/3)")

# --------------------------------------------------------------------------------------------- mixtures
r0 = sp.symbols("r0", positive=True)          # r0 = E_gas/E_condensate at a = 1
# fold-band gas (P3 = E/3, Pt = P0 = 0, E ~ 1/a for every b4) + the lambda = 0 condensate (rho = m S, p = 0: E = m S0 Vol_7
# S0^-1 ... = m S0 constant; P = 0)
wmix_A = sp.Rational(1, 3) * (r0 / a) / (1 + r0 / a)
wmix_C = wmix_A - (4 - 2 * beta) / 3
w0_mix = sp.simplify(wmix_A.subs(a, 1))
wa_mix = sp.simplify(-sp.diff(wmix_A, a).subs(a, 1))
w0_mixC = sp.simplify(wmix_C.subs(a, 1))
Ec_l0 = sp.simplify(E_c.subs(lam, 0))
check("mixture_fold_band_gas_condensate_cpl", zero(w0_mix - r0 / (3 * (1 + r0))) and zero(wa_mix - r0 / (3 * (1 + r0) ** 2))
      and zero(w0_mixC - (r0 / (3 * (1 + r0)) - (4 - 2 * beta) / 3)) and not Ec_l0.has(A) and not Ec_l0.has(Bf),
      f"fold-band gas (P3 = E/3, Pt = P0 = 0, E ~ 1/a for every b4) + the lambda = 0 condensate (E = {Ec_l0}, constant for "
      f"every b4): w_eff(A) = (1/3) r/(1 + r), r = r0/a: w0 = {w0_mix}, wa = {wa_mix} > 0; w_eff(C) = w_eff(A) - (4 - 2 beta)/3: "
      f"w0 = {w0_mixC}, same wa")
need = sp.Rational(-861, 1000) + (4 - 2 * beta) / 3          # r0/(3 (1 + r0)) must equal this, in [0, 1/3)
beta_lo = sp.solve(sp.Eq(need, sp.Rational(1, 3)), beta)[0]
beta_hi = sp.solve(sp.Eq(need, 0), beta)[0]
mix_ok = (sp.Rational(4, 3) <= min(beta_lo, beta_hi)) or (sp.Rational(4, 3) > max(beta_lo, beta_hi))
check("mixture_C_matching_w0_unite", mix_ok,
      f"w_eff(C) = -0.861 at a = 1 needs r0/(3 (1 + r0)) = -0.861 + (4 - 2 beta)/3 in [0, 1/3), i.e. beta in "
      f"({min(beta_lo, beta_hi)}, {max(beta_lo, beta_hi)}] = ({float(min(beta_lo, beta_hi)):.6f}, "
      f"{float(max(beta_lo, beta_hi)):.6f}]; on the record's history (beta = 4/3) there is no such mixture: there w_eff(C) of "
      f"this mixture lies in [-4/9, -1/9)")

# --------------------------------------------------------------------------------- CPL fits (exact rules)
w0s, was, a1 = sp.symbols("w0 wa a1", real=True)
wfun = sp.Function("w")
J0 = sp.Integral(wfun(a), (a, a1, 1))
J1 = sp.Integral(wfun(a) * (1 - a), (a, a1, 1))
Lr = 1 - a1
normal = sp.solve([sp.Eq(w0s * Lr + was * Lr ** 2 / 2, J0), sp.Eq(w0s * Lr ** 2 / 2 + was * Lr ** 3 / 3, J1)], [w0s, was])
w0_fit = sp.simplify(normal[w0s])
wa_fit = sp.simplify(normal[was])
test = {wfun(a): -sp.Rational(861, 1000) - sp.Rational(6, 10) * (1 - a)}
w0_t = sp.simplify(w0_fit.subs(test).doit().subs(a1, sp.Rational(1, 3)))
wa_t = sp.simplify(wa_fit.subs(test).doit().subs(a1, sp.Rational(1, 3)))
check("cpl_least_squares_rule", w0_t == -sp.Rational(861, 1000) and wa_t == -sp.Rational(6, 10),
      "normal equations of min int_{a1}^1 (w - w0 - wa (1 - a))^2 da; reproduce an exact CPL curve")
check("unite_deep_past", -sp.Rational(861, 1000) - sp.Rational(6, 10) == -sp.Rational(1461, 1000),
      "Unite CPL: w(a -> 0) = w0 + wa = -1.461 (quoted as -1.46; phantom); wa < 0: w rises from the past (thawing sign)")

# ------------------------------------------------------------------- expansion-inferred w of the observer
t = sp.symbols("t", real=True)
a4t = sp.Function("a4")(t)
Hub = sp.diff(sp.log(sp.exp(a4t)), t)
w_exp = sp.simplify(-1 - sp.Rational(2, 3) * sp.diff(Hub, t) / Hub ** 2)
check("expansion_inferred_w", zero(w_exp - (-1 - sp.Rational(2, 3) * sp.diff(a4t, t, 2) / sp.diff(a4t, t) ** 2)),
      "a = e^(a4(x4)), t = x4 (g44 = -1, no warp of 3-space): H_obs = a4', w_exp = -1 - (2/3) a4''/a4'^2 (b4 does not enter "
      "the observer's scale factor)")


# Ricci tensor (MTW) from the Christoffel symbols: R_bd = d_c G^c_bd - d_d G^c_bc + G^c_ce G^e_bd - G^c_de G^e_bc
def ricci(b, d_):
    e = sum(D(Gam[c][b][d_], c) for c in dims) - sum(D(Gam[c][b][c], d_) for c in dims)
    e += sum(Gam[c][c][f] * Gam[f][b][d_] for c in dims for f in dims)
    e -= sum(Gam[c][d_][f] * Gam[f][b][c] for c in dims for f in dims)
    return sp.simplify(e)


Ric = {(i, i): sp.simplify(ginv[i, i] * ricci(i, i)) for i in dims}
R40 = sp.simplify(ginv[4, 4] * ricci(4, 0))
Rs = sp.simplify(sum(Ric[(i, i)] for i in dims))
G = {i: sp.simplify(Ric[(i, i)] - Rs / 2) for i in dims}
ad1, ad2, vv, kk = sp.symbols("ad1 ad2 vv kk", real=True)
to_vars = {a4pp: ad2, b4pp: (vv + sym["uu"] ** 2) * b4}


def as_vars(e):
    e = e.subs(to_vars).subs({b4p: sym["uu"] * b4, a4p: ad1})
    e = e.subs(b4, sp.exp(2 * a4) / kk).subs(a4, sp.Symbol("A4"))
    return sp.simplify(e)


e1 = rec_all["lovelockTensors"]
check("einstein_no_mixed_component", zero(R40) and all(not (G[i].has(x0) or G[i].has(C) or G[i].has(W)) for i in dims) and zero(G[0] - G[5]),
      "R^x4_x0 = 0 identically for every a4(x4), b4(x4) and every real z (no mixed component: Einstein gravity admits a "
      "diagonal source for every b4); every G^mu_mu is free of x0 and of C, W, and G^x0_x0 = G^x5_x5 (a source needs "
      "p0 = p_t), as in a4-equations.json generalSource")
G_rec = {}
for key in ("x0x0", "x1x1", "x4x4", "x5x5"):
    if key in e1.get("E1", {}):
        G_rec[key] = sp.sympify(e1["E1"][key]["input"].replace("^", "**"),
                                locals={"ad1": ad1, "ad2": ad2, "uu": sym["uu"], "vv": vv, "kk": kk, "H": H})
diff_mine = as_vars(G[1] - G[5])
diff_rec = (G_rec["x1x1"] - G_rec["x5x5"]) if ("x1x1" in G_rec and "x5x5" in G_rec) else None
check("einstein_space_minus_extra_time", diff_rec is not None and zero(sp.simplify(diff_mine - diff_rec)),
      f"G^x1_x1 - G^x5_x5 = {sp.factor(diff_mine)} (computed from the metric; equal to E1 x1x1 - x5x5 of "
      f"a4-equations.json lovelockTensors)")
kap = sp.symbols("kappa", real=True)
# Einstein: x1 component minus x5 component: G^1_1 - G^5_5 = kappa (p3 - p_t); solve for a4''
sol_ad2 = sp.solve(sp.Eq(diff_mine, kap * (P3v - Ptv)), ad2)
w_exp_E = sp.simplify(-1 - sp.Rational(2, 3) * sol_ad2[0] / ad1 ** 2) if len(sol_ad2) == 1 else None
check("expansion_inferred_w_einstein", w_exp_E is not None,
      f"Einstein (alpha1 = 1): G^x1_x1 - G^x5_x5 = kappa (p3 - p_t) gives a4'' and w_exp = {w_exp_E} (valid as a source "
      f"statement only for an ADMISSIBLE source: x0-independent, p0 = p_t; the Kohn-Sham states are not admissible)")

# ------------------------------------------- the record's history and the source it needs
aw = rec_all["exponentialHistory"]["authorWeights"]
hist_src = aw["historySource_kappaT_minus_Lam"]
check("record_history_needs_a_source", "be = 4/3" in aw["recordHistory"] and all(k_ in hist_src for k_ in ("minus_rho", "p3", "p0", "pt"))
      and kst["adiabaticity"]["historyBeta"] == "4/3",
      "the record's history a4 = H x4, b4 = e^((4/3) H x4) (ks-theory.json adiabaticity.historyBeta = 4/3; a4-equations.json "
      "exponentialHistory.authorWeights.recordHistory) needs, with the author's weights, the x0-independent source "
      "historySource_kappaT_minus_Lam (minus_rho, p3, p0 = pt; a function of kk = e^((2/3) H x4)); the Kohn-Sham gas does not "
      "supply it (Revision/field_equations_a4/reports/ks-source-conditions.json): the history is a PRESCRIBED background")

# ------------------------------------------------------------------------------------- phantom statement
check("phantom_condition", zero(weff["C_per_unit_proper_7_volume"] + 1 -
                                 (P3s / Es + (beta / 2 - 1) * (P0s + 3 * Pts) / (3 * Es) + 1 - (4 - 2 * beta) / 3)),
      "w_eff(C) + 1 = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) + (2 beta - 1)/3: at beta = 4/3, w_eff(C) < -1 needs P3/E - "
      "(P0 + 3 Pt)/(9E) < -5/9; w_eff(A) < -1 needs P3/E - (P0 + 3 Pt)/(9E) < -1. A real-frequency kinetic gas has P3 >= 0, "
      "Pt <= 0 and P0 >= 0 (flat_mode_gas_conservation: p3 = n k_p^2/(3 omega), p_t = -n q_p^2/(3 omega), p0 = n l_p^2/omega), "
      "so with E > 0 it needs a large hidden kinetic pressure P0 > 9 E (P3/E + 5/9) (for C) or E < 0")

formulas = {
    "description": "Exact effective formulas of the dark-sector analysis of dirac16complex (SPEC sections 8, 11) for the "
                   "corrected primordial metric of 2026-10-16 (version 2), derived by "
                   "Revision/dark_sector/dirac16complex/derive/derive_effective.py (sympy); every entry is a named check "
                   "of reports/derivation-checks.json.",
    "coordinates": "the author's coordinates {x0, ..., x7}: x0 = hidden direction, z = 6 H x0 real, y = ln|sin z|/(6 H); "
                   "x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three exponentially DEFLATING "
                   "extra times (time-like, scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); the hidden direction carries "
                   "e^{-a4} b4^{1/2} too",
    "metric": "diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)) (Revision/SPEC.md section 1, "
              "version 2); b4 = b4(x4) > 0",
    "observerScaleFactor": "a = e^{a4} (3-space scale factor, no warp), normalised a = 1 at the chosen 'today' a4 = "
                           "a4_today, i.e. a = e^{a4 - a4_today}; b4 does not enter it",
    "beta": "beta = d ln b4/d a4 = b4'/(a4' b4); the record's history a4 = H x4, b4 = e^{(4/3) H x4} has beta = 4/3 (a "
            "prescribed background: it needs the source exponentialHistory.authorWeights.historySource_kappaT_minus_Lam)",
    "volumes": {"sqrtDetG": "e^{-a4} b4^2 |cot z| |sin z|^{1/2}", "proper3VolumeElement": "e^{3 a4}",
                "properExtraTimeVolumeElement": "e^{-3 a4} b4^{3/2} |sin z|^{1/2}",
                "hiddenLengthElement": "e^{-a4} b4^{1/2} |cot z| dx0 = f |dy|, f = e^{-a4} b4^{1/2}",
                "cellVolume": "Vol_7 ~ e^{-a4} b4^2 = e^{(2 beta - 1) a4}"},
    "conservation": {"x4": "d4 rho = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t), h4 = b4'/(2 b4) - a4'",
                     "x0": "d0 p0 + 3 H cot z (p0 - p_t) = 0  <=>  p0_y + 3 H (p0 - p_t) = 0",
                     "integrated": "dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt) (beta = 4/3: -3 P3 + Pt + P0/3), E = int rho "
                                   "sqrt|g| d^7x, P = int p sqrt|g| d^7x per unit coordinate volume (fixed occupations / "
                                   "exact solutions)"},
    "rho4": {
        "A_compact_coordinate_period": "ASSUMPTION: the extra times and the hidden direction are compact with a fixed "
                                       "coordinate period; rho_4 = E/(proper 3-volume) ~ E e^{-3 a4}",
        "B_per_unit_coordinate_volume": "per unit coordinate volume of the extra times and the hidden direction; rho_4 ~ "
                                        "E e^{-3 a4}",
        "C_per_unit_proper_7_volume": "rho_4 = E/Vol_7 x (constant) ~ E e^{a4} b4^{-2}",
        "general": "rho_4 ~ E e^{-3 a4} (e^{-4 a4} b4^2)^{-s}: s = 0 (A, B), s = 1 (C)"},
    "wEff": {"definition": "w_eff = -1 - (1/3) d ln rho_4/d ln a",
             "A": "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E)", "B": "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E)",
             "C": "A - (4 - 2 beta)/3", "general": "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3",
             "atBeta4over3": {"A": "P3/E - (P0 + 3 Pt)/(9E)", "C": "A - 4/9"}},
    "ratios": {"w3": "P3/E", "wt": "Pt/E", "wx0": "P0/E (integrated; the x0 ratio, not the CPL w0)"},
    "condensate": {"S": "S0 e^{a4} b4^{-2} (S Vol_7 constant)", "rho": "m S + lambda S^2/2",
                   "p3=p_t=p0": "lambda S^2/2", "w_ratio": "w_c = lambda S/(2 m + lambda S)",
                   "dw_ratio_da4": str(sp.simplify(dwc_exp)),
                   "w_eff_A": "((2 beta - 1)/3) w_c", "w_eff_C": "A - (4 - 2 beta)/3",
                   "ratio_equals_minus_0p764_at_lambdaS_over_m": str(u_sol[0])},
    "flatModeLabelled": {"status": "flat (warp-free) limit, used for the sign structure and the limits only",
                         "omega2": "M^2 + k^2 e^{-2 a4} + l^2 e^{2 a4}/b4 - q^2 e^{2 a4}/b4",
                         "q_p_rate": "d ln q_p/d a4 = d ln l_p/d a4 = 1 - beta/2",
                         "massive_w_eff_A": "k^2/(3 (M^2 a^2 + k^2)) (l = q = 0: independent of b4)",
                         "massive_w0": str(w0_m), "massive_wa": str(wa_m),
                         "foldBand": "eps = e^{-a4} |k| exactly (ks-theory.json): w_eff(A) = 1/3, w_eff(C) = 1/3 - (4 - 2 beta)/3"},
    "mixtures": {"w_eff": "linear in (P3, Pt, P0) at fixed E: sum over the components",
                 "foldBandGas_plus_lambda0_condensate_A": "(1/3) r/(1 + r), r = r0/a", "C": "A - (4 - 2 beta)/3",
                 "w0_A": str(w0_mix), "w0_C": str(w0_mixC), "wa": str(wa_mix),
                 "betaRangeForW0CEqualMinus0p861": f"({min(beta_lo, beta_hi)}, {max(beta_lo, beta_hi)}]; none at beta = 4/3"},
    "cpl": {"convention": "w(a) = w0 + wa (1 - a); thawing wa < 0, freezing wa > 0 (the formula decides)",
            "tangent": "w0 = w(1), wa = -dw/da at a = 1 = -dw/da4 at a4 = a4_today",
            "leastSquaresW0": str(w0_fit).replace("\n", " "), "leastSquaresWa": str(wa_fit).replace("\n", " "),
            "constantWFit": "w_const = (1/(1 - a1)) int_{a1}^{1} w(a) da"},
    "expansionInferred": {"w_exp": "-1 - (2/3) a4''/a4'^2",
                          "einstein": str(w_exp_E),
                          "einsteinMixed": "G^x4_x0 = 0 identically (the corrected metric has no mixed component)",
                          "linearMember": "-1"},
    "recordHistory": {"history": "a4 = H x4, b4 = e^{(4/3) H x4}", "source": hist_src,
                      "status": "a prescribed background; the Kohn-Sham gas is not its source"},
    "unite": {"constant_w": "-0.764", "w0": "-0.861", "wa": "-0.60", "deep_past": "-1.461 (w0 + wa; quoted as -1.46)"},
}

fails = [c for c in CHECKS if c["verdict"] != "PASS"]
report = {"producer": "Revision/dark_sector/dirac16complex/derive/derive_effective.py", "engine": f"sympy {sp.__version__}",
          "metric": "the corrected primordial metric of 2026-10-16 (version 2; general a4(x4), b4(x4); every real z)",
          "checks": CHECKS, "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
OUT_FORMULAS.parent.mkdir(parents=True, exist_ok=True)
OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_FORMULAS, "w", encoding="utf-8", newline="\n") as fh_:
    fh_.write(json.dumps(formulas, indent=1, ensure_ascii=True) + "\n")
with open(OUT_REPORT, "w", encoding="utf-8", newline="\n") as fh_:
    fh_.write(json.dumps(report, indent=1, ensure_ascii=True) + "\n")
for c in CHECKS:
    print(f"{c['verdict']} - {c['name']}: {c['detail']}")
print(f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
sys.exit(1 if fails else 0)
