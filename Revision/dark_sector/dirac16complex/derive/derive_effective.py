#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/derive/derive_effective.py - exact (sympy) derivation of every effective
formula the dark-sector analysis of dirac16complex uses (SPEC sections 4, 5, 8, 11), BEFORE any number is computed.

Coordinates as the author names them: x1, x2, x3 = ordinary 3-space (scale factor e^{a4} sin^{1/6} z);
x4 = the time; x5, x6, x7 = the three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor
e^{-a4} sin^{1/6} z, a4 increasing); x8 = the hidden space direction, z = 6 H x8 in (0, pi/2).

Derived here (every item is a named check in reports/derivation-checks.json):
  * the volume elements: sqrt|g| = cos z; the proper 7-volume element of a slice x4 = const is cos z and does not
    depend on a4 (3-space inflation e^{3 a4} compensated by extra-time deflation e^{-3 a4});
  * the conservation identities, re-derived from the metric (own Christoffel symbols) for a diagonal
    T = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) depending on (x4, x8):
      nabla_mu T^mu_x4 = 0  <=>  d rho/d x4 = -3 a4' (p3 - p_t),
      nabla_mu T^mu_x8 = 0  <=>  d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0,
    all other components vanish identically; the hidden-coordinate form p8_y + 6 H p8 = 3 H (p3 + p_t);
  * the integrated identity dE/da4 = -3 (P3 - Pt) (E, P3, Pt = proper 7-volume integrals);
  * the 4-dimensional effective density rho_4 of a 3-space observer for the three normalisations
    (A) compact extra times of fixed coordinate period (closed time-like directions; ASSUMPTION),
    (B) non-compact extra times, per unit extra-time COORDINATE volume,
    (C) per unit PROPER 7-volume (equivalently per unit proper extra-time volume),
    and the exact dilution-inferred w_eff = -1 - (1/3) d ln rho_4 / d ln a, a = e^{a4}:
      w_eff(A) = w_eff(B) = (P3 - Pt)/E,  w_eff(C) = (P3 - Pt)/E - 1;
  * the homogeneous condensate (exact solution): rho = m S + U, p3 = p_t = p8 = S U' - U constant: w_eff(A) = 0,
    w_eff(C) = -1, ratio w = lambda S/(2 m + lambda S) constant; the value of lambda S/m that makes the ratio
    equal to the Unite constant-w value;
  * a free mode in the flat (warp-free) limit, labelled: omega^2 = M^2 + k^2 e^{-2 a4} - q^2 e^{2 a4} from the
    mass shell g^{mu nu} k_mu k_nu = -M^2; per-mode P3 - Pt = (k^2 e^{-2a4} + q^2 e^{2a4})/(3 omega) >= 0;
    the massive mode's w_eff(A) = k^2 a^{-2}/(3 (M^2 + k^2 a^{-2})): 1/3 -> 0 (the dark-matter-like law);
  * mixtures: w_eff = sum X_i / sum E_i - s (s = 0 for A, B; s = 1 for C); radiation-like gas + condensate;
  * the CPL parameters: tangent w0 = w(1), wa = -dw/da at a = 1; the least-squares CPL and constant-w fits over
    a in [a1, 1] (continuous L2 norm in a);
  * the expansion-inferred w_exp = -1 - (2/3) a4''/a4'^2 of a 3-space observer who reads a(t) = e^{a4(x4)} with
    4-dimensional Friedmann equations; Einstein case w_exp = -1 - kappa (p3 - p_t)/(3 a4'^2); linear member -1.

Writes outputs/effective-formulas.json and reports/derivation-checks.json (deterministic, LF).
Exit code 0 iff every check passes.
"""

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
OUT_FORMULAS = OWN / "outputs" / "effective-formulas.json"
OUT_REPORT = OWN / "reports" / "derivation-checks.json"

CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


# ----------------------------------------------------------------------------------------------- metric
x = sp.symbols("x1:9", real=True)            # x[0..7] = x1..x8
x4, x8 = x[3], x[7]
H = sp.symbols("H", positive=True)
a4 = sp.Function("a4")(x4)
z = 6 * H * x8
sz = sp.sin(z)
g = sp.diag(sp.exp(2 * a4) * sz ** sp.Rational(1, 3), sp.exp(2 * a4) * sz ** sp.Rational(1, 3),
            sp.exp(2 * a4) * sz ** sp.Rational(1, 3), -1,
            -sp.exp(-2 * a4) * sz ** sp.Rational(1, 3), -sp.exp(-2 * a4) * sz ** sp.Rational(1, 3),
            -sp.exp(-2 * a4) * sz ** sp.Rational(1, 3), sp.cot(z) ** 2)
ginv = sp.diag(*[1 / g[i, i] for i in range(8)])

# volume elements (0 < z < pi/2: every factor positive)
zs = sp.symbols("z", positive=True)
A4s = sp.symbols("a4", real=True)


def onchart(e):
    return e.subs(a4, A4s).subs(6 * H * x8, zs)


sn, cs = sp.symbols("sn cs", positive=True)      # sin z, cos z on the patch 0 < z < pi/2


def poschart(e):
    return onchart(e).subs({sp.cot(zs): cs / sn}).subs(sp.sin(zs), sn)


sqrt_det_z = sp.simplify(sp.prod([sp.sqrt(poschart(-g[i, i]) if i in (3, 4, 5, 6) else poschart(g[i, i]))
                                  for i in range(8)]))
f3 = onchart(sp.exp(3 * a4) * sz ** sp.Rational(1, 2))          # proper 3-volume element (x1 x2 x3)
ft = onchart(sp.exp(-3 * a4) * sz ** sp.Rational(1, 2))         # proper extra-time volume element (x5 x6 x7)
f8 = sp.cot(zs)                                                 # proper hidden length element
vol7 = sp.simplify(f3 * ft * f8)
check("sqrt_det_g_equals_cos_z", zero(sqrt_det_z - cs),
      f"sqrt|det g| = {sqrt_det_z} (sn = sin z, cs = cos z > 0 on the patch)")
check("proper_7_volume_element_independent_of_a4",
      zero(sp.trigsimp(vol7 - sp.cos(zs))) and sp.diff(vol7, A4s) == 0,
      f"(e^(3a4) sin^(1/2) z)(e^(-3a4) sin^(1/2) z)(cot z) = {sp.trigsimp(vol7)}; d/da4 = 0")
check("proper_3_and_extra_time_volume_scalings",
      zero(sp.diff(sp.log(f3), A4s) - 3) and zero(sp.diff(sp.log(ft), A4s) + 3),
      "d ln(proper 3-volume)/d a4 = +3 (inflating), d ln(proper extra-time volume)/d a4 = -3 (deflating)")

# --------------------------------------------------------------------------------- Christoffel symbols
dims = range(8)
Gam = [[[0] * 8 for _ in dims] for _ in dims]
for l in dims:
    for m_ in dims:
        for n in dims:
            Gam[l][m_][n] = sp.simplify(sum(ginv[l, s] * (sp.diff(g[s, m_], x[n]) + sp.diff(g[s, n], x[m_])
                                                       - sp.diff(g[m_, n], x[s])) for s in dims) / 2)

rho = sp.Function("rho")(x4, x8)
p3 = sp.Function("p3")(x4, x8)
pt = sp.Function("pt")(x4, x8)
p8 = sp.Function("p8")(x4, x8)
T = sp.diag(p3, p3, p3, -rho, pt, pt, pt, p8)                  # T^mu_nu, mixed

div = []
for nu in dims:
    e = sum(sp.diff(T[mu, nu], x[mu]) for mu in dims)
    e += sum(Gam[mu][mu][lam] * T[lam, nu] for mu in dims for lam in dims)
    e -= sum(Gam[lam][mu][nu] * T[mu, lam] for mu in dims for lam in dims)
    div.append(sp.simplify(e))
a4p = sp.diff(a4, x4)
expected_x4 = -sp.diff(rho, x4) - 3 * a4p * (p3 - pt)
expected_x8 = sp.diff(p8, x8) + 3 * H * sp.cot(z) * (2 * p8 - p3 - pt)
others_zero = all(zero(div[i]) for i in (0, 1, 2, 4, 5, 6))
check("conservation_x4_identity", zero(div[3] - expected_x4),
      "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t): d rho/d x4 = -3 a4' (p3 - p_t) on shell")
check("conservation_x8_identity", zero(sp.expand_trig(div[7] - expected_x8)),
      "nabla_mu T^mu_x8 = d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t)")
check("conservation_other_components_vanish", others_zero,
      "nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (homogeneous diagonal T)")

# hidden coordinate y = ln(sin z)/(6 H): dy/dx8 = cot z, so d/dx8 = cot z d/dy
yv = sp.log(sp.sin(z)) / (6 * H)
check("hidden_coordinate_dy_dx8", zero(sp.simplify(sp.diff(yv, x8) - sp.cot(z))), "dy/dx8 = cot z")
P8y, P3v, Ptv, P8v = sp.symbols("p8_y p3 p_t p8", real=True)
# d p8/dx8 = cot z p8_y; the x8 identity times tan z gives p8_y + 6 H p8 - 3 H (p3 + p_t)
yform = sp.simplify(sp.tan(z) * (sp.cot(z) * P8y + 3 * H * sp.cot(z) * (2 * P8v - P3v - Ptv)))
check("conservation_x8_in_y_form", zero(yform - (P8y + 6 * H * P8v - 3 * H * (P3v + Ptv))),
      "tan z * (x8 identity) = p8_y + 6 H p8 - 3 H (p3 + p_t) (the form checked by the Kohn-Sham solver)")

# integrated identity on an explicit family (linear consequence of the pointwise identity)
c8 = sp.sin(z) ** 2
rho_fam = c8 * sp.exp(-a4)
X_fam = c8 * sp.exp(-a4) / 3            # p3 - p_t of the family
fam_ok = zero(sp.diff(rho_fam, x4) + 3 * a4p * X_fam)
lim = sp.pi / (12 * H)
E_fam = sp.integrate(rho_fam * sp.cos(z), (x8, 0, lim))
X_int = sp.integrate(X_fam * sp.cos(z), (x8, 0, lim))
check("integrated_identity_dE_da4", fam_ok and zero(sp.diff(E_fam, x4) + 3 * a4p * X_int),
      f"family rho = sin^2 z e^(-a4), p3 - p_t = rho/3: E = {sp.simplify(E_fam)}, dE/dx4 = -3 a4' (P3 - Pt)")

# ------------------------------------------------------------------- rho_4 and the dilution-inferred w_eff
A = sp.symbols("A", real=True)                  # a4 as the variable of the history
Ef = sp.Function("E")(A)
Xs = sp.symbols("X", real=True)                 # X = P3 - Pt (integrated)
Es = sp.symbols("E", positive=True)
s = sp.symbols("s", real=True)
# rho_4 = E / (proper 3-volume * normaliser of the extra times); proper 3-volume ~ e^{3A};
# extra-time normaliser: A: coordinate period (const), B: coordinate volume (const), C: proper e^{-3A}
norms = {"A_compact_coordinate_period": sp.Integer(1), "B_per_unit_extra_time_coordinate_volume": sp.Integer(1),
         "C_per_unit_proper_7_volume": sp.exp(-3 * A)}
weff = {}
for key, nt in norms.items():
    rho4 = Ef / (sp.exp(3 * A) * nt)
    w = -1 - sp.Rational(1, 3) * sp.diff(sp.log(rho4), A)       # d ln a = d A
    w = sp.simplify(w.subs(sp.Derivative(Ef, A), -3 * Xs).subs(Ef, Es))
    weff[key] = w
check("w_eff_A_equals_X_over_E", zero(weff["A_compact_coordinate_period"] - Xs / Es),
      f"w_eff(A) = {weff['A_compact_coordinate_period']}")
check("w_eff_B_equals_w_eff_A", zero(weff["B_per_unit_extra_time_coordinate_volume"] - Xs / Es),
      "normalising per unit extra-time coordinate volume divides by a constant: same w_eff as A")
check("w_eff_C_equals_X_over_E_minus_1", zero(weff["C_per_unit_proper_7_volume"] - (Xs / Es - 1)),
      f"w_eff(C) = {weff['C_per_unit_proper_7_volume']}")
gen = sp.simplify((-1 - sp.Rational(1, 3) * sp.diff(sp.log(Ef / sp.exp(3 * A * (1 - s))), A))
                  .subs(sp.Derivative(Ef, A), -3 * Xs).subs(Ef, Es))
check("w_eff_general_normaliser", zero(gen - (Xs / Es - s)),
      "rho_4 = E/(e^{3a4} e^{-3 s a4}): w_eff = (P3 - Pt)/E - s; s = 0 (A, B), s = 1 (C)")

# ------------------------------------------------------------------------------------ condensate (exact)
m, lam, S = sp.symbols("m lambda S", real=True)
U = lam * S ** 2 / 2
rho_c = m * S + U
p_c = S * sp.diff(U, S) - U
check("condensate_rho_p", zero(p_c - lam * S ** 2 / 2), "rho = m S + lambda S^2/2, p3 = p_t = p8 = lambda S^2/2")
cond_x4 = zero(expected_x4.subs({rho: rho_c, p3: p_c, pt: p_c}).doit())
cond_x8 = zero(expected_x8.subs({p8: p_c, p3: p_c, pt: p_c}).doit())
check("condensate_satisfies_both_identities", cond_x4 and cond_x8,
      "S constant: d rho/dx4 = 0 = -3 a4' (p - p); x8 identity 3 H cot z (2p - p - p) = 0")
ratio_c = sp.simplify(p_c / rho_c)
check("condensate_ratio_w", zero(ratio_c - lam * S / (2 * m + lam * S)), f"w = p/rho = {ratio_c}")
check("condensate_w_eff", zero(weff["A_compact_coordinate_period"].subs(Xs, 0)) and
      zero(weff["C_per_unit_proper_7_volume"].subs(Xs, 0) + 1),
      "X = P3 - Pt = 0: w_eff(A) = w_eff(B) = 0 (dust-like dilution a^-3), w_eff(C) = -1; constant in time (wa = 0)")
u = sp.symbols("u", real=True)               # u = lambda S/m
w_target = sp.Rational(-764, 1000)
u_sol = sp.solve(sp.Eq(u / (2 + u), w_target), u)
rho_over_mS = 1 + u_sol[0] / 2
check("condensate_ratio_equal_unite_constant_w", len(u_sol) == 1 and rho_over_mS > 0,
      f"u = lambda S/m = {u_sol[0]} = {float(u_sol[0]):.12f} gives w = -0.764; rho/(m S) = 1 + u/2 = "
      f"{float(rho_over_mS):.12f} > 0 (rho > 0 iff m S > 0); the ratio is constant: no time variation")

# ------------------------------------------------------------------ free mode in the flat (warp-free) limit
M, k, q, om = sp.symbols("M k q omega", positive=True)
w_mode = sp.symbols("w4", real=True)           # covariant k_4 = -omega
ginv_flat = sp.diag(sp.exp(-2 * A), -1, -sp.exp(2 * A))         # (one 3-space dir, x4, one extra time)
kv = sp.Matrix([k, -om, q])
shell = sp.solve(sp.Eq((kv.T * ginv_flat * kv)[0], -M ** 2), om)
omega2 = M ** 2 + k ** 2 * sp.exp(-2 * A) - q ** 2 * sp.exp(2 * A)
check("flat_mode_mass_shell", len(shell) == 1 and zero(shell[0] ** 2 - omega2),
      "g^{mu nu} k_mu k_nu = -M^2: omega^2 = M^2 + k^2 e^{-2a4} - q^2 e^{2a4} (k: 3-momentum, q: extra-time momentum)")
omega = sp.sqrt(omega2)
Xmode = sp.simplify(-sp.diff(omega, A) / 3)
check("flat_mode_X_nonnegative", zero(Xmode - (k ** 2 * sp.exp(-2 * A) + q ** 2 * sp.exp(2 * A)) / (3 * omega)),
      "per mode X = P3 - Pt = -(1/3) d omega/d a4 = (k^2 e^{-2a4} + q^2 e^{2a4})/(3 omega) >= 0 for real omega > 0; "
      "kinetic theory: p3 = k_p^2/(3 omega) >= 0, p_t = -q_p^2/(3 omega) <= 0 (time-like extra directions)")
wmass = sp.simplify((Xmode / omega).subs(q, 0))
a = sp.symbols("a", positive=True)
wmass_a = sp.simplify(wmass.subs(A, sp.log(a)))
check("massive_mode_w_eff_law", zero(wmass_a - k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))) and
      sp.limit(wmass_a, a, 0) == sp.Rational(1, 3) and sp.limit(wmass_a, a, sp.oo) == 0,
      "q = 0: w_eff(A) = k^2/(3 (M^2 a^2 + k^2)) -> 1/3 (a -> 0), -> 0 (a -> oo): the dark-matter-like 1/3 -> 0 law")
xk = sp.symbols("x", positive=True)           # x = k^2/M^2 at a = 1
w_ma = k ** 2 / (3 * (M ** 2 * a ** 2 + k ** 2))
w0_m = sp.simplify(w_ma.subs(a, 1).subs(k, sp.sqrt(xk) * M))
wa_m = sp.simplify((-sp.diff(w_ma, a)).subs(a, 1).subs(k, sp.sqrt(xk) * M))
check("massive_mode_cpl_tangent", zero(w0_m - xk / (3 * (1 + xk))) and zero(wa_m - 2 * xk / (3 * (1 + xk) ** 2)),
      f"w0 = {w0_m}, wa = {wa_m} > 0 (freezing sign in the CPL convention)")
check("massless_mode_w_eff", zero((Xmode / omega).subs({q: 0, M: 0}) - sp.Rational(1, 3)),
      "M = 0, q = 0: X/E = 1/3 exactly: w_eff(A) = 1/3 (radiation), w_eff(C) = -2/3")

# --------------------------------------------------------------------------------------------- mixtures
r0 = sp.symbols("r0", positive=True)          # r0 = E_gas/E_condensate at a = 1 (radiation-like gas)
wmix_A = sp.Rational(1, 3) * (r0 / a) / (1 + r0 / a)
w0_mix = sp.simplify(wmix_A.subs(a, 1))
wa_mix = sp.simplify(-sp.diff(wmix_A, a).subs(a, 1))
check("mixture_radiation_condensate_cpl", zero(w0_mix - r0 / (3 * (1 + r0))) and zero(wa_mix - r0 / (3 * (1 + r0) ** 2)),
      f"gas with X = E/3 (E ~ 1/a) + condensate (X = 0, E const): w_eff(A) = (1/3) r/(1 + r), r = r0/a; "
      f"w0 = {w0_mix}, wa = {wa_mix} > 0; w_eff(C) = w_eff(A) - 1 (same wa)")
r0_861 = sp.solve(sp.Eq(r0 / (3 * (1 + r0)) - 1, sp.Rational(-861, 1000)), r0)
check("mixture_C_matching_w0_unite", len(r0_861) == 1,
      f"w_eff(C) = -0.861 at a = 1 needs r0 = {r0_861[0]} = {float(r0_861[0]):.12f}; then "
      f"wa = {float(wa_mix.subs(r0, r0_861[0])):.12f} (> 0), not -0.60")

# --------------------------------------------------------------------------------- CPL fits (exact rules)
w0s, was, a1 = sp.symbols("w0 wa a1", real=True)
wfun = sp.Function("w")
# least squares: minimise int_{a1}^{1} (w(a) - w0 - wa (1 - a))^2 da -> normal equations
J0 = sp.Integral(wfun(a), (a, a1, 1))
J1 = sp.Integral(wfun(a) * (1 - a), (a, a1, 1))
L = 1 - a1
normal = sp.solve([sp.Eq(w0s * L + was * L ** 2 / 2, J0), sp.Eq(w0s * L ** 2 / 2 + was * L ** 3 / 3, J1)], [w0s, was])
w0_fit = sp.simplify(normal[w0s])
wa_fit = sp.simplify(normal[was])
# test on an exact CPL curve: the fit must reproduce it
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
      "a = e^{a4(x4)}, t = x4 (g44 = -1): H_obs = a4', w_exp = -1 - (2/3) a4''/a4'^2")
kap = sp.symbols("kappa", real=True)
d1, d2 = sp.symbols("a4p a4pp", real=True)
# Einstein evolution equation (Revision/field_equations_a4): 2 a4'' = kappa (p3 - p_t)
w_exp_E = -1 - sp.Rational(2, 3) * (kap * (P3v - Ptv) / 2) / d1 ** 2
check("expansion_inferred_w_einstein", zero(w_exp_E - (-1 - kap * (P3v - Ptv) / (3 * d1 ** 2))),
      "Einstein (alpha1 = 1): w_exp = -1 - kappa (p3 - p_t)/(3 a4'^2); the linear member a4 = A H x4 (the only "
      "history the condensate allows, p3 = p_t) gives w_exp = -1 exactly; w_exp < -1 iff kappa (p3 - p_t) > 0 "
      "(valid only for an ADMISSIBLE source; the Kohn-Sham states are not admissible)")

# ------------------------------------------------------------------------------------- phantom statement
check("phantom_condition", zero(weff["C_per_unit_proper_7_volume"] + 1 - Xs / Es),
      "w_eff(C) < -1 iff (P3 - Pt)/E < 0 and w_eff(A) < 0 iff (P3 - Pt)/E < 0: with E > 0 this needs P_t > P3 "
      "(an extra-time pressure exceeding the 3-space pressure), which no real-frequency mode supplies "
      "(flat_mode_X_nonnegative); otherwise E < 0 together with X > 0. This check verifies the identity "
      "w_eff(C) + 1 = X/E, not the origin of a negative E. Negative E is not specific to a negative-norm (Krein) "
      "sector: in the good sector the interacting N = 8, lambda > 0 Kohn-Sham states have E < 0 with X = 0 exactly, "
      "from the interaction energy of the canonical uniform-gas exchange functional (E = 0 at lambda = 0; in the "
      "exact-Fock variant, Revision/kohn_sham/results/exx/exact-fock-variant.csv, the N = 8 states have "
      "|E| <= 2.04e-13); for free modes E < 0 needs a negative Krein charge, outside the positive good-sector "
      "realisation (OPEN)")

formulas = {
    "description": "Exact effective formulas of the dark-sector analysis of dirac16complex (SPEC sections 8, 11), "
                   "derived by Revision/dark_sector/dirac16complex/derive/derive_effective.py (sympy); every entry is "
                   "a named check of reports/derivation-checks.json.",
    "coordinates": "x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 = the three "
                   "exponentially DEFLATING extra times (time-like, scale factor e^{-a4} sin^{1/6} z, a4 increasing); "
                   "x8 = hidden direction, z = 6 H x8 in (0, pi/2), y = ln(sin z)/(6 H).",
    "observerScaleFactor": "a = e^{a4} (3-space scale factor on the brane z = pi/2, normalised a = 1 at the chosen "
                           "'today' a4 = a4_today, i.e. a = e^{a4 - a4_today})",
    "volumes": {"sqrtDetG": "cos z", "proper7VolumeElement": "cos z (independent of a4)",
                "proper3VolumeElement": "e^{3 a4} sin^{1/2} z", "properExtraTimeVolumeElement": "e^{-3 a4} sin^{1/2} z",
                "hiddenLengthElement": "cot z dx8 = dy"},
    "conservation": {"x4": "d rho/d x4 = -3 a4' (p3 - p_t)",
                     "x8": "d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0  <=>  p8_y + 6 H p8 = 3 H (p3 + p_t)",
                     "integrated": "dE/d a4 = -3 (P3 - Pt), E = int rho sqrt|g| d^7x, P3 = int p3 sqrt|g| d^7x, "
                                   "Pt = int p_t sqrt|g| d^7x (fixed occupations / exact solutions)"},
    "rho4": {
        "A_compact_coordinate_period": "ASSUMPTION: the extra times are compact with a fixed coordinate period "
                                       "(closed time-like directions); rho_4 = E/(proper 3-volume) ~ E e^{-3 a4}",
        "B_per_unit_extra_time_coordinate_volume": "non-compact extra times; rho_4 = E/(proper 3-volume x extra-time "
                                                   "coordinate volume) ~ E e^{-3 a4}",
        "C_per_unit_proper_7_volume": "rho_4 = E/(proper 7-volume) x (constant) ~ E (equivalently per unit proper "
                                      "extra-time volume)",
        "general": "rho_4 ~ E e^{-3 (1 - s) a4}: s = 0 (A, B), s = 1 (C)"},
    "wEff": {"definition": "w_eff = -1 - (1/3) d ln rho_4/d ln a",
             "A": "(P3 - Pt)/E", "B": "(P3 - Pt)/E", "C": "(P3 - Pt)/E - 1", "general": "(P3 - Pt)/E - s"},
    "ratios": {"w3": "P3/E", "wt": "Pt/E", "w8": "P8/E (integrated); brane-local p3/rho etc. also reported"},
    "condensate": {"rho": "m S + lambda S^2/2", "p3=p_t=p8": "lambda S^2/2", "w_ratio": "lambda S/(2 m + lambda S)",
                   "w_eff_A": "0", "w_eff_C": "-1", "wa": "0 (every definition)",
                   "ratio_equals_minus_0p764_at_lambdaS_over_m": str(u_sol[0])},
    "flatModeLabelled": {"status": "flat (warp-free) limit, used for the sign structure and the limits only",
                         "omega2": "M^2 + k^2 e^{-2 a4} - q^2 e^{2 a4}",
                         "X": "(k^2 e^{-2 a4} + q^2 e^{2 a4})/(3 omega)",
                         "massive_w_eff_A": "k^2/(3 (M^2 a^2 + k^2))", "massive_w0": str(w0_m), "massive_wa": str(wa_m)},
    "mixtures": {"w_eff": "sum_i X_i/sum_i E_i - s",
                 "radiation_plus_condensate_A": "(1/3) r/(1 + r), r = r0/a", "w0": str(w0_mix), "wa": str(wa_mix),
                 "r0_for_w_eff_C_equal_minus_0p861": str(r0_861[0])},
    "cpl": {"convention": "w(a) = w0 + wa (1 - a); thawing wa < 0, freezing wa > 0 (the formula decides)",
            "tangent": "w0 = w(1), wa = -dw/da at a = 1 = -dw/da4 at a4 = a4_today",
            "leastSquaresW0": str(w0_fit).replace("\n", " "), "leastSquaresWa": str(wa_fit).replace("\n", " "),
            "constantWFit": "w_const = (1/(1 - a1)) int_{a1}^{1} w(a) da"},
    "expansionInferred": {"w_exp": "-1 - (2/3) a4''/a4'^2", "einstein": "-1 - kappa (p3 - p_t)/(3 a4'^2)",
                          "linearMember": "-1"},
    "unite": {"constant_w": "-0.764", "w0": "-0.861", "wa": "-0.60", "deep_past": "-1.461 (w0 + wa; quoted as -1.46)"},
}

fails = [c for c in CHECKS if c["verdict"] != "PASS"]
report = {"producer": "Revision/dark_sector/dirac16complex/derive/derive_effective.py", "engine": f"sympy {sp.__version__}",
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
