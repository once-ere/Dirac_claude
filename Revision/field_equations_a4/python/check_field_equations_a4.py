#!/usr/bin/env python3
"""Revision field equations for a4[x4]: independent sympy derivation and cross-check.

Revision/SPEC.md section 5.  Revision code only; nothing is imported from the old stages and nothing
from the Wolfram side is used as an input except the two files that are being CHECKED:

  Revision/gkd_lovelock/results/lovelock-tensors.json   (the GKD branch's exact monomial lists)
  Revision/field_equations_a4/a4-equations.json         (written by the Wolfram verifier)

Everything else is computed here from the metric of SPEC section 1, by a different implementation:
  * the metric is written in the symbols Ee = e^{a4}, Sh = sin^{1/6} z, Cc = cot z (z = 6 H x8) with
    exact derivation rules (d/dx4: a4^(n) -> a4^(n+1), Ee -> a4' Ee; d/dx8: Sh -> H Cc Sh,
    Cc -> -6 H (1 + Cc^2)), so no trigonometric simplification is needed;
  * Christoffel symbols, Riemann R^{ab}_{cd} (MTW), Ricci and Einstein tensors;
  * GKD as the sign of a permutation (not as a determinant);
  * the Lovelock tensors P_(1), P_(2), P_(3) as polynomials (sympy Poly);
  * the field equations, their reduction, the Bianchi identity, conservation, the linear member;
  * the spinor lemmas in two Clifford representations: a real representation built here
    (different from the Wolfram one) and, when Revision/algebra/gammas.json exists, the author's T16.

Outputs (deterministic, LF):
  Revision/field_equations_a4/reports/python-a4-report.json   every check with name, verdict, detail
  Revision/field_equations_a4/reports/a4-equations-summary.md  the key equations, from this file's own results

Usage (from anywhere): python Revision/field_equations_a4/python/check_field_equations_a4.py
Exit code 0 iff every check passes (a check that cannot run is "pending", never "pass").
"""

from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

import mpmath
import sympy as sp

HERE = Path(__file__).resolve().parent
FIELD = HERE.parent
REV = FIELD.parent
LOVELOCK_JSON = REV / "gkd_lovelock" / "results" / "lovelock-tensors.json"
A4_JSON = FIELD / "a4-equations.json"
GAMMAS_JSON = REV / "algebra" / "gammas.json"
REPORT = FIELD / "reports" / "python-a4-report.json"
SUMMARY = FIELD / "reports" / "a4-equations-summary.md"

CHECKS: list[dict] = []


def check(name: str, ok, detail: str, pending: bool = False) -> None:
    verdict = "pending" if pending else ("PASS" if ok is True else "FAIL")
    CHECKS.append({"name": name, "verdict": verdict, "detail": detail})


# ----------------------------------------------------------------------------------------------
# symbols and exact derivations
# ----------------------------------------------------------------------------------------------
H, ad1, ad2, ad3, ad4 = sp.symbols("H ad1 ad2 ad3 ad4")
Ee, Sh, Cc = sp.symbols("Ee Sh Cc", positive=True)  # e^{a4}, sin^{1/6} z, cot z
alpha1, alpha2, alpha3, Lam, kappa, AA = sp.symbols("alpha1 alpha2 alpha3 Lam kappa AA")
rho, p3, pt, p8, q48, q84 = sp.symbols("rho p3 pt p8 q48 q84")
SRC = [rho, p3, pt, p8, q48, q84]
D4SRC = {s: sp.Symbol("d4" + s.name) for s in SRC}
D8SRC = {s: sp.Symbol("d8" + s.name) for s in SRC}

RULE4 = {ad1: ad2, ad2: ad3, ad3: ad4, Ee: ad1 * Ee, **D4SRC}
RULE8 = {Sh: H * Cc * Sh, Cc: -6 * H * (1 + Cc**2), **D8SRC}


def deriv(e, mu: int):
    """Partial derivative with respect to coordinate index mu (0..7 = x1..x8)."""
    rule = RULE4 if mu == 3 else RULE8 if mu == 7 else None
    if rule is None:
        return sp.Integer(0)
    return sp.Add(*[sp.diff(e, s) * v for s, v in rule.items() if e.has(s)])


def norm(e):
    """Canonical rational form; Sh is eliminated where possible with Sh^12 (1 + Cc^2) = 1."""
    e = sp.cancel(sp.expand(e))
    if e.has(Sh):
        n, d = sp.fraction(e)
        e2 = sp.cancel(sp.expand(n).subs(Sh**12, 1 / (1 + Cc**2)) / sp.expand(d).subs(Sh**12, 1 / (1 + Cc**2)))
        e = e2
    return e


N8 = 8
COORDS = [f"x{i}" for i in range(1, 9)]
gdiag = [Ee**2 * Sh**2] * 3 + [sp.Integer(-1)] + [-(Ee**-2) * Sh**2] * 3 + [Cc**2]
ginv = [sp.cancel(1 / x) for x in gdiag]
vielb = [Ee * Sh] * 3 + [sp.Integer(1)] + [Sh / Ee] * 3 + [Cc]  # e^a_mu = sqrt|g_mumu|
eta = [1, 1, 1, -1, -1, -1, -1, 1]

t_start = time.time()

# Christoffel symbols of a diagonal metric
Gam = [[[sp.Integer(0)] * N8 for _ in range(N8)] for _ in range(N8)]
for a in range(N8):
    for b in range(N8):
        for c in range(N8):
            val = 0
            if a == c:
                val += deriv(gdiag[a], b)
            if a == b:
                val += deriv(gdiag[a], c)
            if b == c:
                val -= deriv(gdiag[b], a)
            Gam[a][b][c] = norm(sp.Rational(1, 2) * ginv[a] * val)

# Riemann (MTW) R^a_{bcd}, then R^{ab}_{cd} = g^{bb} R^a_{bcd}
RUU = {}
for a, b, c, d in itertools.product(range(N8), repeat=4):
    r = deriv(Gam[a][b][d], c) - deriv(Gam[a][b][c], d)
    r += sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(N8))
    r = norm(ginv[b] * r)
    if r != 0:
        RUU[(a, b, c, d)] = r

check("mixed_riemann_free_of_warp_and_a4",
      all(not v.has(Sh) and not v.has(Ee) for v in RUU.values()),
      f"every R^ab_cd is free of sin^(1/6) z and e^(a4) (computed with the symbol calculus of this file); {len(RUU)} nonzero of 4096 ordered index lists")
check("riemann_pair_antisymmetry",
      all(RUU.get((b, a, c, d), 0) == -v and RUU.get((a, b, d, c), 0) == -v for (a, b, c, d), v in RUU.items()),
      "R^{ab}_{cd} = -R^{ba}_{cd} = -R^{ab}_{dc}")

# Ricci and Einstein (mixed)
ricci_mixed = [[norm(sum(RUU.get((a, h, a, j), 0) for a in range(N8))) for j in range(N8)] for h in range(N8)]
# R^h_j = R^{ah}_{aj}: R^a_{b a d} with b raised -> R^{a h}_{a j}
Rscal = norm(sum(ricci_mixed[i][i] for i in range(N8)))
G = [[norm(ricci_mixed[h][j] - (sp.Rational(1, 2) * Rscal if h == j else 0)) for j in range(N8)] for h in range(N8)]


# ----------------------------------------------------------------------------------------------
# GKD as a permutation sign and the Lovelock tensors
# ----------------------------------------------------------------------------------------------
def gkd(up, low) -> int:
    if len(set(up)) != len(up) or set(up) != set(low):
        return 0
    perm = [up.index(x) for x in low]
    inv = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
    return -1 if inv % 2 else 1


Tc = sp.Symbol("Tc", positive=True)  # stands for tan z = 1/cot z in the Laurent polynomials
GENS = (H, ad1, ad2, Cc, Tc)


def laurent(v):
    n, d = sp.fraction(sp.cancel(v))
    dp = sp.Poly(d, Cc)
    if len(dp.terms()) != 1:
        raise ValueError(f"not a Laurent polynomial in cot z: {v}")
    (deg,), c = dp.terms()[0]
    return sp.Poly(sp.expand(n * Tc**deg / c), *GENS)


def unlaurent(e):
    return sp.cancel(sp.expand(e).subs(Tc, 1 / Cc))


pairs = [(a, b, c, d, laurent(v)) for (a, b, c, d), v in sorted(RUU.items()) if a < b and c < d]
check("riemann_entries_laurent",
      all(sp.cancel(unlaurent(p.as_expr()) - RUU[(a, b, c, d)]) == 0 for a, b, c, d, p in pairs),
      f"the {len(pairs)} components R^ab_cd (a<b, c<d) are Laurent polynomials in cot z with polynomial coefficients in H, a4', a4''")


def lovelock(k: int):
    zero = sp.Poly(0, *GENS)
    P = [[zero for _ in range(N8)] for _ in range(N8)]
    L = zero
    for tup in itertools.product(pairs, repeat=k):
        low = [x for t in tup for x in t[0:2]]  # R upper indices -> GKD lower list
        up = [x for t in tup for x in t[2:4]]   # R lower indices -> GKD upper list
        if len(set(low)) != len(low) or len(set(up)) != len(up):
            continue
        val = sp.Poly(4**k, *GENS)
        for t in tup:
            val = val * t[4]
        if set(up) == set(low):
            L = L + val * gkd(up, low)
        for h in range(N8):
            if h in up:
                continue
            for j in range(N8):
                if j in low:
                    continue
                s = gkd([h] + up, [j] + low)
                if s:
                    P[h][j] = P[h][j] + val * s
    return [[unlaurent(P[h][j].as_expr()) for j in range(N8)] for h in range(N8)], unlaurent(L.as_expr())


t0 = time.time()
P = {}
Lsc = {}
for k in (1, 2, 3):
    P[k], Lsc[k] = lovelock(k)
t_lovelock = time.time() - t0

check("P1_equals_minus_4_Einstein",
      all(sp.expand(P[1][h][j] + 4 * G[h][j]) == 0 for h in range(N8) for j in range(N8)),
      "P_(1)^h_j (GKD permutation sign) = -4 G^h_j (Ricci route), all 64 components")
for k in (1, 2, 3):
    check(f"P{k}_trace_identity", sp.expand(sum(P[k][i][i] for i in range(N8)) - (8 - 2 * k) * Lsc[k]) == 0,
          f"sum_h P_({k})^h_h = (8 - {2 * k}) L_({k}); L_({k}) = {sp.expand(Lsc[k])}")
    diag_ok = all(P[k][h][j] == 0 for h in range(N8) for j in range(N8) if h != j)
    grp_ok = P[k][0][0] == P[k][1][1] == P[k][2][2] and P[k][4][4] == P[k][5][5] == P[k][6][6]
    check(f"P{k}_structure", diag_ok and grp_ok and not any(P[k][i][i].has(Cc) for i in range(N8)),
          f"P_({k}) diagonal (x4-x8 components 0), free of x8, x1 = x2 = x3, x5 = x6 = x7")

# compare with the GKD branch's monomial lists
MONO_VARS = (H, ad1, ad2, ad3, ad4, Ee, sp.Symbol("Smon"), Cc)
if LOVELOCK_JSON.exists():
    lj = json.loads(LOVELOCK_JSON.read_text(encoding="utf-8"))

    def from_monomials(mons):
        e = sp.Integer(0)
        for num, den, ex in mons:
            t = sp.Rational(num, den)
            for v, n in zip(MONO_VARS, ex):
                t *= v**n
            e += t
        return e

    for k in (1, 2, 3):
        key = f"P{k}_mixed_up_h_down_j"
        ok = True
        no_extra = True
        for h in range(N8):
            for j in range(N8):
                e = from_monomials(lj[key][f"{COORDS[h]},{COORDS[j]}"]["monomials"])
                if e.has(MONO_VARS[6]) or e.has(Ee) or e.has(ad3) or e.has(ad4):
                    no_extra = False
                if sp.expand(e - P[k][h][j]) != 0:
                    ok = False
        check(f"P{k}_equals_gkd_branch_monomials", ok and no_extra,
              f"all 64 components of P_({k}) computed here equal Revision/gkd_lovelock/results/lovelock-tensors.json ({key}); no warp, e^(a4) or higher derivatives in the lists")
        Ls = sp.sympify(lj[f"L{k}"].replace("Derivative[1][a4][x4]", "ad1").replace("^", "**"))
        check(f"L{k}_equals_gkd_branch", sp.expand(Ls - Lsc[k]) == 0, f"L_({k}) = {sp.expand(Lsc[k])}")
else:
    check("gkd_branch_monomials", False, "Revision/gkd_lovelock/results/lovelock-tensors.json missing", pending=True)

E = {k: [[sp.expand(-P[k][h][j] / 2 ** (k + 1)) for j in range(N8)] for h in range(N8)] for k in (1, 2, 3)}


def divergence(T):
    """nabla_mu T^mu_nu for a mixed tensor T (list of lists of expressions in the symbol calculus)."""
    out = []
    for n in range(N8):
        s = sum(deriv(T[m][n], m) for m in range(N8))
        s += sum(Gam[m][m][l] * T[l][n] for m in range(N8) for l in range(N8))
        s -= sum(Gam[l][m][n] * T[m][l] for m in range(N8) for l in range(N8))
        out.append(norm(s))
    return out


for k in (1, 2, 3):
    check(f"E{k}_divergence_free", all(x == 0 for x in divergence(E[k])),
          f"nabla_mu E_({k})^mu_nu = 0 for nu = x1..x8 (Christoffel symbols of this file)")

# ----------------------------------------------------------------------------------------------
# field equations
# ----------------------------------------------------------------------------------------------
al = {1: alpha1, 2: alpha2, 3: alpha3}
LHS = [[sp.expand(sum(al[k] * E[k][h][j] for k in (1, 2, 3)) + (Lam if h == j else 0)) for j in range(N8)] for h in range(N8)]
e11, e44, e55, e88 = (sp.expand(LHS[i][i] - Lam) for i in (0, 3, 4, 7))
Fevo = sp.expand(sp.cancel((e11 - e55) / ad2))
check("evolution_factorises", not Fevo.has(ad2) and sp.expand(Fevo * ad2 - (e11 - e55)) == 0,
      f"sum_k alpha_k (E^x1_x1 - E^x5_x5) = a4'' F(a4'), F = {Fevo}")
coeffs = sp.Poly(Fevo, ad1, H).coeffs()
sol = sp.solve(coeffs, [alpha1, alpha2, alpha3], dict=True)
check("evolution_F_not_identically_zero", sol == [{alpha1: 0, alpha2: 0, alpha3: 0}],
      "F vanishes identically in (a4', H) only for alpha1 = alpha2 = alpha3 = 0")
check("algebraic_identity", sp.expand(e11 + e55 - 2 * e88) == 0,
      "sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x8_x8) = 0 identically: the equations force p3 + p_t = 2 p8")
check("constraint_and_x8_first_order", not e44.has(ad2) and not e88.has(ad2),
      "the x4 and x8 components contain a4' but not a4''")
check("bianchi_x4", sp.expand(deriv(e44, 3) - 3 * ad1 * (e11 - e55)) == 0,
      "d/dx4 sum_k alpha_k E^x4_x4 = 3 a4' sum_k alpha_k (E^x1_x1 - E^x5_x5)")
check("other_components_vanish",
      all(LHS[h][j] == 0 for h in range(N8) for j in range(N8) if h != j) and
      LHS[0][0] == LHS[1][1] == LHS[2][2] and LHS[4][4] == LHS[5][5] == LHS[6][6],
      "every off-diagonal left-hand side (including x4-x8) is 0; x1 = x2 = x3 and x5 = x6 = x7")

# conservation of a general source T(x4, x8)
Tg = [[sp.Integer(0)] * N8 for _ in range(N8)]
for i in (0, 1, 2):
    Tg[i][i] = p3
for i in (4, 5, 6):
    Tg[i][i] = pt
Tg[3][3] = -rho
Tg[7][7] = p8
Tg[3][7] = q48
Tg[7][3] = q84
divT = divergence(Tg)
d4r, d8p8, d8q84, d4q48 = D4SRC[rho], D8SRC[p8], D8SRC[q84], D4SRC[q48]
exp_x4 = -d4r - 3 * ad1 * (p3 - pt) + d8q84 - 6 * H * q84 / Cc
exp_x8 = d8p8 + 3 * H * Cc * (2 * p8 - p3 - pt) + d4q48
check("conservation_components",
      all(divT[i] == 0 for i in (0, 1, 2, 4, 5, 6)) and sp.cancel(divT[3] - exp_x4) == 0 and sp.cancel(divT[7] - exp_x8) == 0,
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - p_t) + d8 q84 - 6 H tan z q84; nabla_mu T^mu_x8 = d8 p8 + 3 H cot z (2 p8 - p3 - p_t) + d4 q48")

ein = {alpha1: 1, alpha2: 0, alpha3: 0}
check("einstein_components",
      sp.expand(e44.subs(ein) - (3 * ad1**2 + 21 * H**2)) == 0 and sp.expand(e11.subs(ein) - (ad2 - 3 * ad1**2 + 15 * H**2)) == 0 and
      sp.expand(e55.subs(ein) - (-ad2 - 3 * ad1**2 + 15 * H**2)) == 0 and sp.expand(e88.subs(ein) - (-3 * ad1**2 + 15 * H**2)) == 0,
      "G^x4_x4 = 3 a4'^2 + 21 H^2, G^x1_x1 = a4'' - 3 a4'^2 + 15 H^2, G^x5_x5 = -a4'' - 3 a4'^2 + 15 H^2, G^x8_x8 = -3 a4'^2 + 15 H^2")
nec8 = sp.expand(e88 - e44)
check("einstein_null_energy_x8", sp.expand(nec8.subs(ein) + 6 * ad1**2 + 6 * H**2) == 0,
      "Einstein: kappa (rho + p8) = -6 (a4'^2 + H^2) < 0 for every a4, Lambda")
check("einstein_no_vacuum",
      sp.expand((e44 - e88).subs(ein) - 6 * (ad1**2 + H**2)) == 0 and sp.expand((e44 + e88).subs(ein) - 36 * H**2) == 0,
      "T = 0: the x4 and x8 equations give (x4 - x8) 6 (a4'^2 + H^2) = 0, impossible for real a4' and H > 0 (and 36 H^2 + 2 Lambda = 0)")

lin = {ad1: AA * H, ad2: 0}
rho_lin = sp.expand(-(e44 + Lam).subs(lin) / kappa)
p_lin = sp.expand((e88 + Lam).subs(lin) / kappa)
check("linear_member_equal_pressures",
      sp.expand((e11 - e88).subs(lin)) == 0 and sp.expand((e55 - e88).subs(lin)) == 0,
      "a4 = A H x4 + a0: p3 = p_t = p8 = p constant, rho constant (any alpha_k)")
Vfac = sp.expand(sp.cancel((e44 - e88).subs(lin) / (6 * (AA**2 + 1) * H**2)))
check("linear_member_vacuum_factor", Vfac.is_polynomial(AA) and sp.expand(6 * (AA**2 + 1) * H**2 * Vfac - (e44 - e88).subs(lin)) == 0,
      f"sum_k alpha_k (E^x4_x4 - E^x8_x8) at a4' = A H = 6 (A^2 + 1) H^2 V, V = {Vfac}")
Vegb = sp.expand(Vfac.subs({alpha1: 1, alpha3: 0}))
check("einstein_gauss_bonnet_vacuum_linear", sp.expand(Vegb - (1 - 8 * alpha2 * H**2 * (AA**2 + 5))) == 0,
      "alpha1 = 1, alpha3 = 0: V = 1 - 8 alpha2 H^2 (A^2 + 5); vacuum A^2 = (1 - 40 alpha2 H^2)/(8 alpha2 H^2)")

msym, lamsym, Ssym, sigT = sp.symbols("m lam S sigmaT")
condC = sp.expand(e44.subs(ein).subs(lin) + Lam + kappa * sigT * (msym * Ssym + lamsym * Ssym**2 / 2))
condX = sp.expand(e88.subs(ein).subs(lin) + Lam - kappa * sigT * (lamsym * Ssym**2 / 2))
check("condensate_einstein_quadratic_U",
      sp.expand(condC + condX - (36 * H**2 + 2 * Lam + kappa * sigT * msym * Ssym)) == 0 and
      sp.expand(condC - condX - (6 * (AA**2 + 1) * H**2 + kappa * sigT * Ssym * (msym + lamsym * Ssym))) == 0,
      "Einstein, linear a4, U = (lambda/2) S^2: kappa sigmaT m S = -(36 H^2 + 2 Lambda), 6 (A^2 + 1) H^2 = -kappa sigmaT S (m + lambda S)")

# ----------------------------------------------------------------------------------------------
# comparison with a4-equations.json (the Wolfram output)
# ----------------------------------------------------------------------------------------------
LOC = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam,
       "kappa": kappa, "AA": AA, "rho": rho, "p3": p3, "pt": pt, "p8": p8, "q48": q48, "q84": q84, "cc": Cc,
       **{v.name: v for v in D4SRC.values()}, **{v.name: v for v in D8SRC.values()}}


def parse(s: str):
    return sp.sympify(s.replace("^", "**"), locals=LOC)


def parse_eq(s: str):
    l, r = s.split(" == ")
    return sp.expand(parse(l) - parse(r))


if A4_JSON.exists():
    aj = json.loads(A4_JSON.read_text(encoding="utf-8"))
    ok = True
    for k in (1, 2, 3):
        comp = aj["lovelockTensors"][f"E{k}"]
        for key, (h, j) in {"x1x1": (0, 0), "x4x4": (3, 3), "x5x5": (4, 4), "x8x8": (7, 7), "x4x8": (3, 7), "x8x4": (7, 3)}.items():
            if sp.expand(parse(comp[key]["input"]) - E[k][h][j]) != 0:
                ok = False
    check("json_lovelock_components", ok, "E_(1..3) components x1x1, x4x4, x5x5, x8x8, x4x8, x8x4 in a4-equations.json equal this file's")
    gs = aj["generalSource"]
    mine = {
        "constraint_x4": e44 + Lam + kappa * rho, "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
        "extraTime_x5_eq_x6_eq_x7": e55 + Lam - kappa * pt, "hidden_x8": e88 + Lam - kappa * p8,
        "evolution_x1_minus_x5": ad2 * Fevo - kappa * (p3 - pt), "algebraic_condition": p3 + pt - 2 * p8,
    }
    ok = all(sp.expand(parse_eq(gs[k]["input"]) - v) == 0 for k, v in mine.items())
    ok = ok and sp.expand(parse(gs["evolution_F"]["input"]) - Fevo) == 0
    check("json_general_source_equations", ok, "constraint, x1, x5, x8, evolution (with F) and algebraic condition in a4-equations.json equal this file's")
    src = gs["sourceRequiredByGivenA4"]
    ok = (sp.expand(parse(src["rho"]["input"]) + (e44 + Lam) / kappa) == 0 and sp.expand(parse(src["p3"]["input"]) - (e11 + Lam) / kappa) == 0
          and sp.expand(parse(src["pt"]["input"]) - (e55 + Lam) / kappa) == 0 and sp.expand(parse(src["p8"]["input"]) - (e88 + Lam) / kappa) == 0)
    nc = gs["nullCombinations"]
    ok = ok and sp.expand(parse(nc["kappa(rho+p8)"]["input"]) - nec8) == 0 and sp.expand(parse(nc["kappa(rho+p3)"]["input"]) - (e11 - e44)) == 0 \
        and sp.expand(parse(nc["kappa(rho+pt)"]["input"]) - (e55 - e44)) == 0
    check("json_required_source_and_null_combinations", ok, "sourceRequiredByGivenA4 and nullCombinations equal this file's")
    cx4 = parse_eq(gs["conservation_x4"]["input"])
    cx8 = parse_eq(gs["conservation_x8"]["input"])
    check("json_conservation", sp.cancel(cx4 - exp_x4) == 0 and sp.cancel(cx8 - exp_x8) == 0,
          "conservation_x4 and conservation_x8 in a4-equations.json equal this file's covariant divergence")
    ei = aj["einstein"]
    ok = (sp.expand(parse_eq(ei["constraint_x4"]["input"]) - (e44.subs(ein) + Lam + kappa * rho)) == 0
          and sp.expand(parse_eq(ei["evolution"]["input"]) - (2 * ad2 - kappa * (p3 - pt))) == 0
          and sp.expand(parse_eq(ei["hidden_x8"]["input"]) - (e88.subs(ein) + Lam - kappa * p8)) == 0
          and sp.expand(parse_eq(ei["x4_plus_x8"]["input"]) - (36 * H**2 + 2 * Lam - kappa * (p8 - rho))) == 0)
    check("json_einstein", ok, "the Einstein special case in a4-equations.json equals this file's")
    lm = aj["linearMember"]
    ok = (sp.expand(parse(lm["rho"]["input"]) - rho_lin) == 0 and sp.expand(parse(lm["p"]["input"]) - p_lin) == 0
          and sp.expand(parse(lm["vacuumFactor"]["input"]) - Vfac) == 0
          and sp.expand(parse(lm["rhoPlusPEinstein"]["input"]) - (rho_lin + p_lin).subs(ein)) == 0)
    check("json_linear_member", ok, "rho, p, the vacuum factor V and rho + p (Einstein) of the linear member equal this file's")
else:
    aj = None
    check("json_comparison", False, "a4-equations.json missing (run the Wolfram verifier first)", pending=True)

# ----------------------------------------------------------------------------------------------
# spinor lemmas in two representations
# ----------------------------------------------------------------------------------------------
s1 = sp.Matrix([[0, 1], [1, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
ep = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def own_rep():
    # space-like e1..e4 (square +1), time-like f1..f4 (square -1); a construction different from the Wolfram one
    e1, e2 = kron(s1, I2, I2, I2), kron(s3, I2, I2, I2)
    f1, f2 = kron(ep, s1, I2, I2), kron(ep, s3, I2, I2)
    e3, e4 = kron(ep, ep, s1, I2), kron(ep, ep, s3, I2)
    f3, f4 = kron(ep, ep, ep, s1), kron(ep, ep, ep, s3)
    return [e1, e2, e3, f1, f2, f3, f4, e4]  # x1, x2, x3, x4, x5, x6, x7, x8


def author_rep():
    if not GAMMAS_JSON.exists():
        return None
    gj = json.loads(GAMMAS_JSON.read_text(encoding="utf-8"))
    return [sp.Matrix([[sp.Rational(x) for x in row] for row in m]) for m in gj["gamma"]]


Z16 = sp.zeros(16, 16)
MM = sp.Symbol("MM", real=True)


def spinor_checks(label: str, gF):
    I16 = sp.eye(16)
    cl = all(gF[a] * gF[b] + gF[b] * gF[a] == 2 * eta[a] * (1 if a == b else 0) * I16 for a in range(8) for b in range(8))
    check(f"{label}_clifford", cl, "{gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,-1,-1,-1,-1,1)")
    C = gF[7] * gF[0] * gF[1] * gF[2]
    cprops = C == C.T and C * C == I16 and all((C * g).T == -(C * g) for g in gF) and all(x.is_real for x in C)
    check(f"{label}_C_properties", cprops, "C = gamma^x8 gamma^x1 gamma^x2 gamma^x3 real symmetric, C^2 = 1, C gamma^a antisymmetric")
    Sab = [[(gF[a] * gF[b] - gF[b] * gF[a]) / 4 for b in range(8)] for a in range(8)]
    # omega_mu^a_b = e^a_a (delta_ab d_mu e_b^b + Gamma^a_{mu b} e_b^b)  (diagonal vielbein; e_b^b = 1/e^b_b)
    Om = []
    for mu in range(8):
        M = sp.zeros(16, 16)
        for a in range(8):
            for b in range(8):
                einvb = 1 / vielb[b]
                w = vielb[a] * ((deriv(einvb, mu) if a == b else 0) + Gam[a][mu][b] * einvb)
                w = norm(eta[a] * w)  # omega_mu ab
                if w != 0:
                    M += sp.Rational(1, 2) * w * Sab[a][b]
        Om.append(M.applyfunc(norm))
    gC = [(gF[m] / vielb[m]).applyfunc(norm) for m in range(8)]
    check(f"{label}_Omega_x4_x8_zero", Om[3] == Z16 and Om[7] == Z16, "Omega_x4 = Omega_x8 = 0")
    check(f"{label}_anticommutator_no_sum",
          all((gC[m] * Om[m] + Om[m] * gC[m]).applyfunc(norm) == Z16 for m in range(8)),
          "{gamma^mu, Omega_mu} = 0 for each mu (no sum)")
    Gd = sum((gC[m] * Om[m] for m in range(8)), Z16).applyfunc(norm)
    check(f"{label}_gravity_term", Gd == 3 * H * gF[7], "gamma^mu Omega_mu = 3 H gamma^x8")
    A = (-gC[3] * (MM * I16 - Gd)).applyfunc(sp.expand)
    check(f"{label}_condensate_S_constant", (C * A + A.T * C).applyfunc(sp.expand) == Z16, "C A + A^T C = 0: S constant along x4")
    adj = (A.T * C * gC[3] - C * sum((Om[m] * gC[m] for m in range(8)), Z16) + MM * C).applyfunc(norm)
    check(f"{label}_condensate_adjoint", adj == Z16, "(D_mu Phibar) gamma^mu = -M Phibar for the condensate")

    def dphi(nu):
        return (A if nu == 3 else Z16) + Om[nu]

    def dphibar(nu):
        return (A.T * C if nu == 3 else Z16) - C * Om[nu]

    Nm = [[((C * gC[m] * dphi(n) - dphibar(n) * gC[m]) / 2) for n in range(8)] for m in range(8)]
    Ns = [[((Nm[m][n] + (gdiag[n] / gdiag[m]) * Nm[n][m]) / 2).applyfunc(norm) for n in range(8)] for m in range(8)]
    diag_ok = Ns[3][7] == Z16 and Ns[7][3] == Z16 and all(Ns[m][m] == Z16 for m in (0, 1, 2, 4, 5, 6, 7)) and \
        (Ns[3][3] - MM * C).applyfunc(sp.expand) == Z16
    check(f"{label}_condensate_kinetic_diagonal", diag_ok, "K^x4_x4 = M S, K^mu_mu = 0 otherwise, K^x4_x8 = K^x8_x4 = 0")
    # off-diagonal: each nonzero N^mu_nu is X C gamma^a gamma^b gamma^c with the expected triple
    expected = {}
    for m in range(8):
        for n in range(8):
            if m == n or Ns[m][n] == Z16:
                continue
            expected[(m, n)] = Ns[m][n]
    triples_found = set()
    coeffs_found = {}
    ok = True
    for (m, n), Nmn in expected.items():
        found = False
        for t in itertools.combinations(range(8), 3):
            B = C * gF[t[0]] * gF[t[1]] * gF[t[2]]
            # coefficient from one nonzero entry, then verify the whole matrix
            idx = next((i, j) for i in range(16) for j in range(16) if B[i, j] != 0)
            X = norm(Nmn[idx] / B[idx])
            if X != 0 and (Nmn - X * B).applyfunc(norm) == Z16:
                triples_found.add(t)
                coeffs_found[(m, n)] = (t, X)
                found = True
                break
        ok = ok and found
    exp_trip = {tuple(sorted((i, 3, 7))) for i in (0, 1, 2, 4, 5, 6)} | {tuple(sorted((i, j, 3))) for i in (0, 1, 2) for j in (4, 5, 6)}
    check(f"{label}_condensate_offdiagonal_three_gamma", ok and triples_found == exp_trip,
          f"every nonzero off-diagonal kinetic component ({len(expected)} ordered pairs) is a multiple of one of the 15 bilinears Phibar gamma^a gamma^b gamma^c Phi, {{a,b,c}} = {{i,x4,x8}} or {{i,j,x4}}")
    # exact witness at (M, H) = (5, 1)
    Av = A.subs({MM: 5, H: 1})
    w = 4

    def sector(e):
        stack = sp.Matrix.vstack(Av + sp.I * w * I16, gF[0] * gF[4] - e * I16, gF[1] * gF[5] - e * I16, gF[2] * gF[6] - e * I16)
        return stack.nullspace()

    n1, n2 = sector(-1), sector(1)
    wit_ok = len(n1) == 1 and len(n2) == 1
    if wit_ok:
        v1, v2 = n1[0], n2[0]
        s = sp.expand((v1.H * C * v2)[0])
        ph = v1 + sp.conjugate(s) * v2
        ph = ph.applyfunc(sp.expand)
        Sval = sp.expand((ph.H * C * ph)[0])
        wit_ok = (Av * ph + sp.I * w * ph).applyfunc(sp.expand) == sp.zeros(16, 1) and Sval != 0 and sp.im(Sval) == 0
        for t in exp_trip:
            B = C * gF[t[0]] * gF[t[1]] * gF[t[2]]
            wit_ok = wit_ok and sp.expand((ph.H * B * ph)[0]) == 0
    check(f"{label}_condensate_witness", wit_ok,
          "exact witness at (M, H) = (5, 1): Phi = e^{-4 i x4} Phi0, Phi0 = v1 + conj(v1^dagger C v2) v2 from the sectors gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1, +1; all 15 three-gamma bilinears vanish, S != 0 real")
    return coeffs_found


coeffs_own = spinor_checks("ownrep", own_rep())
arep = author_rep()
if arep is not None:
    coeffs_author = spinor_checks("authorT16", arep)
else:
    coeffs_author = None
    check("authorT16_spinor_checks", False, "Revision/algebra/gammas.json not present", pending=True)

# compare the off-diagonal coefficients with a4-equations.json (numerically, 40 digits, at three points)
if aj is not None:
    offj = aj["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    a4v = sp.Symbol("a4v")
    loc2 = dict(LOC)
    loc2["a4v"] = a4v
    pts = [(sp.Rational(3, 7), sp.Rational(5, 3), sp.Rational(2, 5), sp.Rational(-4, 9)),
           (sp.Rational(-1, 3), sp.Rational(1, 2), sp.Rational(7, 4), sp.Rational(5, 2)),
           (sp.Rational(2, 1), sp.Rational(9, 5), sp.Rational(1, 6), sp.Rational(1, 3))]
    mpmath.mp.dps = 40
    ok = len(offj) == len(coeffs_own)
    for entry in offj:
        comp = entry["component"].split(" ")[0]  # K^x1_x4
        mu = int(comp[3]) - 1
        nu = int(comp.split("_")[1][1]) - 1
        if (mu, nu) not in coeffs_own or len(entry["terms"]) != 1:
            ok = False
            continue
        t, X = coeffs_own[(mu, nu)]
        names = entry["terms"][0]["bilinear"].replace("Phibar ", "").replace(" Phi", "").split(" ")
        tj = tuple(int(nm[-1]) - 1 for nm in names)
        if tj != t:
            ok = False
            continue
        Xj = sp.sympify(entry["terms"][0]["coefficient"]["input"].replace("^", "**"), locals=loc2)
        for av, cv, hv, a1v in pts:
            vj = sp.N(Xj.subs({a4v: av, Cc: cv, H: hv, ad1: a1v}), 40)
            vm = sp.N(X.subs({Ee: sp.exp(av), Sh: (1 + cv**2) ** sp.Rational(-1, 12), Cc: cv, H: hv, ad1: a1v}), 40)
            if abs(vj - vm) > sp.Float("1e-30") * (1 + abs(vm)):
                ok = False
    check("json_offdiagonal_coefficients", ok,
          "every off-diagonal kinetic coefficient of a4-equations.json equals this file's (own representation; same triple, value at three exact points to 40 digits)")
    if coeffs_author is not None:
        same = set(coeffs_author) == set(coeffs_own) and all(
            coeffs_author[k][0] == coeffs_own[k][0] and sp.simplify(coeffs_author[k][1] - coeffs_own[k][1]) == 0 for k in coeffs_own)
        check("offdiagonal_coefficients_representation_independent", same,
              "the author's T16 and the representation built here give the same triples and the same coefficients")

t_total = time.time() - t_start

# ----------------------------------------------------------------------------------------------
# outputs
# ----------------------------------------------------------------------------------------------
npass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
nfail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
npend = sum(1 for c in CHECKS if c["verdict"] == "pending")
report = {
    "producer": "Revision/field_equations_a4/python/check_field_equations_a4.py (sympy, exact)",
    "spec": "Revision/SPEC.md section 5",
    "inputsChecked": ["Revision/gkd_lovelock/results/lovelock-tensors.json", "Revision/field_equations_a4/a4-equations.json",
                      "Revision/algebra/gammas.json (author's T16, when present)"],
    "checkCount": len(CHECKS), "passCount": npass, "failCount": nfail, "pendingCount": npend,
    "verdict": "PASS" if nfail == 0 and npend == 0 else ("FAIL" if nfail else "PENDING"),
    "checks": CHECKS,
}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_bytes((json.dumps(report, indent=2) + "\n").encode("utf-8"))


def lx(e) -> str:
    s = sp.latex(e, symbol_names={ad1: "a_4'", ad2: "a_4''", alpha1: r"\alpha_1", alpha2: r"\alpha_2", alpha3: r"\alpha_3",
                                   Lam: r"\Lambda", AA: "A", p3: "p_3", pt: "p_t", p8: "p_8"})
    return s.replace("a_4'^{2}", "(a_4')^{2}").replace("a_4'^{4}", "(a_4')^{4}").replace("a_4'^{6}", "(a_4')^{6}")


lines = [
    "# Field equations for a4[x4] (summary generated by check_field_equations_a4.py)",
    "",
    "Computed by Revision code from the metric of `Revision/SPEC.md` section 1; every line below is an output of",
    "`Revision/field_equations_a4/python/check_field_equations_a4.py` (sympy), cross-checked against the Wolfram",
    "output `Revision/field_equations_a4/a4-equations.json`. Report: `reports/python-a4-report.json`.",
    "",
    "Field equations: $\\sum_{k=1}^{3}\\alpha_k E_{(k)}{}^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu = \\kappa T^\\mu{}_\\nu$,",
    "$E_{(k)} = -P_{(k)}/2^{k+1}$, $T = \\mathrm{diag}(p_3,p_3,p_3,-\\rho,p_t,p_t,p_t,p_8)$.",
    "",
    "## Independent components (general Lovelock)",
    "",
    f"* constraint (x4): $ {lx(e44)} + \\Lambda = -\\kappa\\rho$",
    f"* 3-space (x1 = x2 = x3): $ {lx(e11)} + \\Lambda = \\kappa p_3$",
    f"* extra times (x5 = x6 = x7): $ {lx(e55)} + \\Lambda = \\kappa p_t$",
    f"* hidden (x8): $ {lx(e88)} + \\Lambda = \\kappa p_8$",
    "* off-diagonal (x4-x8 and all others): $0 = \\kappa T^\\mu{}_\\nu$",
    f"* evolution (x1 - x5): $a_4''\\,F(a_4') = \\kappa (p_3 - p_t)$, $F = {lx(Fevo)}$",
    "* algebraic: $p_3 + p_t = 2 p_8$; x8-dependence: every component of $T^\\mu{}_\\nu$ independent of x8",
    "",
    "## Einstein gravity ($\\alpha_1 = 1$, $\\alpha_2 = \\alpha_3 = 0$)",
    "",
    f"* $ {lx(e44.subs(ein))} + \\Lambda = -\\kappa\\rho$, $2 a_4'' = \\kappa(p_3 - p_t)$, $ {lx(e88.subs(ein))} + \\Lambda = \\kappa p_8$",
    f"* $\\kappa(\\rho + p_8) = {lx(nec8.subs(ein))} < 0$; no vacuum solution for $H > 0$ and any $\\Lambda$",
    "",
    "## The linear member $a_4 = A H x_4 + a_0$",
    "",
    f"* $\\rho = {lx(rho_lin)}$",
    f"* $p_3 = p_t = p_8 = p = {lx(p_lin)}$",
    f"* vacuum needs $V = {lx(Vfac)} = 0$",
    "",
    r"## Field sources (convention $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu \mathcal{L})$, $\sigma_T = +1$ per SPEC section 4)",
    "",
    r"* lemmas: $\gamma^\mu\Omega_\mu = 3H\gamma^{x8}$; $\{\gamma^\mu,\Omega_\mu\}=0$ for each $\mu$ (no sum)",
    r"* dirac16complex00, homogeneous condensate $\Phi(x_4)$: $S$ constant, $\rho = \sigma_T(mS+U)$, $p_3=p_t=p_8=\sigma_T(SU'-U)$;",
    r"  the off-diagonal equations need the 15 bilinears $\bar\Phi\gamma^a\gamma^b\gamma^c\Phi$, $\{a,b,c\}=\{i,x4,x8\},\{i,j,x4\}$, to vanish (exact witnesses exist);",
    r"  then $p_3 = p_t$ forces $a_4'' F(a_4') = 0$, hence $a_4 = A H x_4 + a_0$",
    r"* Einstein with $U = \lambda S^2/2$: $\kappa\sigma_T m S = -(36H^2 + 2\Lambda)$, $6(A^2+1)H^2 = -\kappa\sigma_T S(m+\lambda S)$",
    r"* dirac16complex: the same with normal-ordered expectation values; a Kohn-Sham gas with $\langle k_1\rangle \ne \langle k_5\rangle$ drives $a_4''$",
    "",
    "## Run",
    "",
    f"* checks: {len(CHECKS)} ({npass} pass, {nfail} fail, {npend} pending)",
    "",
]
SUMMARY.write_bytes(("\n".join(lines)).encode("utf-8"))
print(f"checks: {len(CHECKS)}, pass {npass}, fail {nfail}, pending {npend}; Lovelock {t_lovelock:.1f} s, total {t_total:.1f} s")
for c in CHECKS:
    if c["verdict"] != "PASS":
        print(c["verdict"], c["name"], c["detail"])
sys.exit(0 if nfail == 0 and npend == 0 else 1)
