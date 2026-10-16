#!/usr/bin/env python3
"""Revision field equations for a4[x4] and b4[x4]: independent sympy derivation and cross-check.

Revision/SPEC.md section 5, for the author's metric with b4(x4) and GENERAL functions a4 and b4 > 0 (since
2026-10-15: the user's orders "b4 is a function of x4; b4 is NEVER 1" and "move everything to b4(x4)"; until then
this checker treated the restriction b4 = 1, the withdrawn earlier metric).  Revision code only; nothing is imported
from the old stages and nothing from the Wolfram side is used as an input except the two files that are being
CHECKED and the fixture:

  Revision/gkd_lovelock/results/lovelock-tensors.json   (the GKD branch's exact monomial lists)
  Revision/field_equations_a4/a4-equations.json         (written by the Wolfram verifier)
  Revision/algebra/gammas.json                          (the author's T16, order x0..x7: REQUIRED; read
                                                         strictly; a missing or malformed file stops the
                                                         run at once with a line "ERROR  ..." and exit code 1)

Everything else is computed here from the metric of SPEC section 1, by a different implementation:
  * the metric is written in the symbols Ee = e^{a4}, Sh = sin^{1/6} z, Cc = cot z (z = 6 H x0), Bq = b4^{1/2} in the
    author's coordinates x0..x7 (index k = xk) with exact derivation rules (d/dx4: a4^(n) -> a4^(n+1), Ee -> a4' Ee,
    Bq -> u Bq/2, u -> v -> w -> w5 with u = b4'/b4, v = u'; d/dx0: Sh -> H Cc Sh, Cc -> -6 H (1 + Cc^2)), so no
    trigonometric simplification is needed;
  * Christoffel symbols, Riemann R^{ab}_{cd} (MTW), Ricci and Einstein tensors;
  * GKD as the sign of a permutation (not as a determinant);
  * the Lovelock tensors P_(1), P_(2), P_(3) as polynomials (sympy Poly) in H, a4', a4'', u, v, cot z;
  * the field equations, their structure, the Bianchi identity, conservation, the exponential histories
    (Groebner bases for the vacuum and condensate questions);
  * the spinor lemmas in the author's T16 from Revision/algebra/gammas.json (the PRIMARY representation,
    SPEC section 2: its off-diagonal coefficients are the ones compared with a4-equations.json) and, ONLY
    for comparison, in a real tensor-product representation built here (own_rep, different from the
    Wolfram comparison representation), with an exact equivalence check (intertwiner space of dimension
    1, K^T K = c I16) and the representation independence of the off-diagonal coefficients.

Outputs (deterministic, LF):
  Revision/field_equations_a4/reports/python-a4-report.json   every check with name, verdict, detail
  Revision/field_equations_a4/reports/a4-equations-summary.md  the key equations, from this file's own results

Usage (from anywhere): python Revision/field_equations_a4/python/check_field_equations_a4.py
Exit code 0 iff every check passes (a check that cannot run is "pending", never "pass"); exit code 1 with a
line "ERROR  ..." (and no output written) if Revision/algebra/gammas.json is missing or malformed.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import sys
import time
from fractions import Fraction
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
# the author's T16: Revision/algebra/gammas.json, read strictly (before any computation)
# ----------------------------------------------------------------------------------------------
# The fixture's documented encoding (its "encoding" field): every matrix is a list of rows; an exact rational is
# a JSON integer when it is an integer and otherwise a JSON string "p/q" in lowest terms with q > 0 (so a string
# has q > 1); a complex matrix is {"re": ..., "im": ...};
# indices 0..7 of gamma, eta and S stand for x0..x7.  Anything else (a float, a boolean, another string, a wrong
# shape, a missing key, a file that is not a JSON object, a missing file) is an ERROR: one line, exit code 1.
class FixtureError(Exception):
    pass


def _fixture_rat(x, where: str) -> Fraction:
    if isinstance(x, bool) or not isinstance(x, (int, str)):
        raise FixtureError(f"{where} = {x!r} is not an exact rational in the fixture encoding "
                           "(a JSON integer, or a string \"p/q\" in lowest terms with q > 1)")
    if isinstance(x, int):
        return Fraction(x)
    m = re.fullmatch(r"(-?[0-9]+)/([0-9]+)", x)
    f = Fraction(int(m.group(1)), int(m.group(2))) if m and int(m.group(2)) != 0 else None
    # lowest terms, q > 1: the value written back in the same encoding is the same string
    if f is None or f.denominator == 1 or f"{f.numerator}/{f.denominator}" != x:
        raise FixtureError(f"{where} = {x!r} is not an exact rational in the fixture encoding "
                           "(a JSON integer, or a string \"p/q\" in lowest terms with q > 1)")
    return f


def _fixture_vector(v, n: int, where: str) -> list:
    if not (isinstance(v, list) and len(v) == n):
        raise FixtureError(f"{where} is not a list of {n} entries")
    return [_fixture_rat(x, f"{where}[{i}]") for i, x in enumerate(v)]


def _fixture_matrix(m, where: str) -> sp.Matrix:
    if not (isinstance(m, list) and len(m) == 16 and all(isinstance(r, list) and len(r) == 16 for r in m)):
        raise FixtureError(f"{where} is not a list of 16 rows of 16 entries")
    return sp.Matrix([[sp.Rational(_fixture_rat(x, f"{where}[{i}][{j}]")) for j, x in enumerate(r)] for i, r in enumerate(m)])


def _fixture_matrix_list(v, n: int, where: str) -> list:
    if not (isinstance(v, list) and len(v) == n):
        raise FixtureError(f"{where} is not a list of {n} matrices")
    return [_fixture_matrix(m, f"{where}[{a}]") for a, m in enumerate(v)]


def load_fixture(path: Path) -> dict:
    if not path.is_file():
        raise FixtureError("input file not found")
    raw = path.read_bytes()
    try:
        fx = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FixtureError(f"not valid JSON: {exc}") from None
    if not isinstance(fx, dict):
        raise FixtureError("not a JSON object")
    missing = [k for k in ("coordinates", "notebookFrameIndex", "eta", "gamma", "C", "Gamma", "B", "S") if k not in fx]
    if missing:
        raise FixtureError(f"missing keys {', '.join(missing)}")
    if not (isinstance(fx["coordinates"], list) and len(fx["coordinates"]) == 8 and all(isinstance(c, str) for c in fx["coordinates"])):
        raise FixtureError("coordinates is not a list of 8 strings")
    nfi = fx["notebookFrameIndex"]
    if not (isinstance(nfi, list) and len(nfi) == 8 and all(isinstance(i, int) and not isinstance(i, bool) for i in nfi)):
        raise FixtureError("notebookFrameIndex is not a list of 8 integers")
    if not (isinstance(fx["B"], dict) and set(fx["B"]) == {"re", "im"}):
        raise FixtureError("B is not an object {\"re\": ..., \"im\": ...}")
    if not (isinstance(fx["S"], list) and len(fx["S"]) == 8):
        raise FixtureError("S is not a list of 8 lists of matrices")
    return {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "coordinates": fx["coordinates"], "notebookFrameIndex": nfi,
        "eta": _fixture_vector(fx["eta"], 8, "eta"),
        "gamma": _fixture_matrix_list(fx["gamma"], 8, "gamma"),
        "C": _fixture_matrix(fx["C"], "C"),
        "Gamma": _fixture_matrix(fx["Gamma"], "Gamma"),
        "B": _fixture_matrix(fx["B"]["re"], "B.re") + sp.I * _fixture_matrix(fx["B"]["im"], "B.im"),
        "S": [_fixture_matrix_list(fx["S"][a], 8, f"S[{a}]") for a in range(8)],
    }


try:
    FIXTURE = load_fixture(GAMMAS_JSON)
except FixtureError as exc:
    print(f"ERROR  {GAMMAS_JSON}: {exc}", flush=True)
    sys.exit(1)

# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# symbols and exact derivations (general a4 and b4)
# ----------------------------------------------------------------------------------------------
H, ad1, ad2, ad3, ad4 = sp.symbols("H ad1 ad2 ad3 ad4")
Ee, Sh, Cc, Bq = sp.symbols("Ee Sh Cc Bq", positive=True)  # e^{a4}, sin^{1/6} z, cot z, b4^{1/2}
uu, vv, ww, w5 = sp.symbols("uu vv ww w5")  # u = b4'/b4, v = u', w = v', w5 = w'
alpha1, alpha2, alpha3, Lam, kappa, AA, be = sp.symbols("alpha1 alpha2 alpha3 Lam kappa AA be")
# p0 = the pressure along the hidden direction x0; q40 = T^x4_x0, q04 = T^x0_x4
rho, p3, pt, p0, q40, q04 = sp.symbols("rho p3 pt p0 q40 q04")
SRC = [rho, p3, pt, p0, q40, q04]
D4SRC = {s: sp.Symbol("d4" + s.name) for s in SRC}
D0SRC = {s: sp.Symbol("d0" + s.name) for s in SRC}

RULE4 = {ad1: ad2, ad2: ad3, ad3: ad4, Ee: ad1 * Ee, Bq: uu * Bq / 2, uu: vv, vv: ww, ww: w5, **D4SRC}
RULE0 = {Sh: H * Cc * Sh, Cc: -6 * H * (1 + Cc**2), **D0SRC}


def deriv(e, mu: int):
    """Partial derivative with respect to coordinate index mu (0..7 = the author's x0..x7)."""
    rule = RULE4 if mu == 4 else RULE0 if mu == 0 else None
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
COORDS = [f"x{i}" for i in range(8)]  # the author's x0..x7
gdiag = [Cc**2] + [Ee**2 * Sh**2] * 3 + [sp.Integer(-1)] + [-(Bq**2) * Ee**-2 * Sh**2] * 3
ginv = [sp.cancel(1 / x) for x in gdiag]
vielb = [Cc] + [Ee * Sh] * 3 + [sp.Integer(1)] + [Bq * Sh / Ee] * 3  # e^a_mu = sqrt|g_mumu|
eta = [1, 1, 1, 1, -1, -1, -1, -1]

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
      all(not v.has(Sh) and not v.has(Ee) and not v.has(Bq) for v in RUU.values()),
      f"every R^ab_cd is free of sin^(1/6) z, e^(a4) and b4^(1/2) (computed with the symbol calculus of this file, general a4 and b4): b4 enters only through u = b4'/b4 and v = u'; {len(RUU)} nonzero of 4096 ordered index lists")
check("riemann_pair_antisymmetry",
      all(sp.cancel(RUU.get((b, a, c, d), 0) + v) == 0 and sp.cancel(RUU.get((a, b, d, c), 0) + v) == 0 for (a, b, c, d), v in RUU.items()),
      "R^{ab}_{cd} = -R^{ba}_{cd} = -R^{ab}_{dc}")

# Ricci and Einstein (mixed)
ricci_mixed = [[norm(sum(RUU.get((a, h, a, j), 0) for a in range(N8))) for j in range(N8)] for h in range(N8)]
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
GENS = (H, ad1, ad2, uu, vv, Cc, Tc)


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
      f"the {len(pairs)} components R^ab_cd (a<b, c<d) are Laurent polynomials in cot z with polynomial coefficients in H, a4', a4'', u, v")


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
      "P_(1)^h_j (GKD permutation sign) = -4 G^h_j (Ricci route), all 64 components (general a4 and b4)")
for k in (1, 2, 3):
    check(f"P{k}_trace_identity", sp.expand(sum(P[k][i][i] for i in range(N8)) - (8 - 2 * k) * Lsc[k]) == 0,
          f"sum_h P_({k})^h_h = (8 - {2 * k}) L_({k}); L_({k}) = {sp.expand(Lsc[k])}")
    off_ok = all(P[k][h][j] == 0 for h in range(N8) for j in range(N8) if h != j and (h, j) not in ((4, 0), (0, 4)))
    pair_ok = all(sp.expand(P[k][h][j].subs(uu, 0)) == 0 for h, j in ((4, 0), (0, 4)))
    grp_ok = P[k][1][1] == P[k][2][2] == P[k][3][3] and P[k][5][5] == P[k][6][6] == P[k][7][7]
    check(f"P{k}_structure", off_ok and pair_ok and grp_ok and not any(P[k][i][i].has(Cc) for i in range(N8)),
          f"P_({k}): the only nonzero off-diagonal components are x4-x0 and x0-x4, each proportional to u = b4'/b4; the diagonal is free of x0, x1 = x2 = x3, x5 = x6 = x7")

# compare with the GKD branch's monomial lists (13 exponents: H, a4', a4'', a4''', a4'''', E = e^{a4}, S = sin^{1/3} z,
# C = cot z, Q = b4^(1/2), b4', b4'', b4''', b4''''), in the ring of this file: b4^(n)/b4 written through u, v, w, w5
B4D = [uu * Bq**2, (vv + uu**2) * Bq**2, (ww + 3 * uu * vv + uu**3) * Bq**2,
       (w5 + 4 * uu * ww + 3 * vv**2 + 6 * uu**2 * vv + uu**4) * Bq**2]
Smon = sp.Symbol("Smon")
MONO_VARS = (H, ad1, ad2, ad3, ad4, Ee, Smon, Cc, Bq) + tuple(B4D)
if LOVELOCK_JSON.exists():
    lj = json.loads(LOVELOCK_JSON.read_text(encoding="utf-8"))

    def from_monomials(mons):
        e = sp.Integer(0)
        for num, den, ex in mons:
            if len(ex) != 13:
                raise SystemExit("ERROR  a monomial of lovelock-tensors.json does not have 13 exponents (format since 2026-10-14)")
            t = sp.Rational(num, den)
            for v, n in zip(MONO_VARS, ex):
                t *= v**n
            e += t
        return sp.expand(e)

    for k in (1, 2, 3):
        key = f"P{k}_mixed_up_h_down_j"
        ok = True
        no_extra = True
        for h in range(N8):
            for j in range(N8):
                e = from_monomials(lj[key][f"{COORDS[h]},{COORDS[j]}"]["monomials"])
                if e.has(Smon) or e.has(Ee) or e.has(ad3) or e.has(ad4) or e.has(Bq) or e.has(ww) or e.has(w5):
                    no_extra = False
                if sp.expand(e - P[k][h][j]) != 0:
                    ok = False
        check(f"P{k}_equals_gkd_branch_monomials", ok and no_extra,
              f"all 64 components of P_({k}) computed here equal Revision/gkd_lovelock/results/lovelock-tensors.json ({key}) for general b4 (b4^(n) written as b4 times polynomials in u = b4'/b4 and its derivatives); no warp, e^(a4), b4^(1/2) or higher derivatives remain")
        Lstr = lj[f"L{k}"]
        Lstr = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"ad\1", Lstr)
        Lstr = re.sub(r"Derivative\[(\d)\]\[b4\]\[x4\]", r"bder\1", Lstr)
        Lstr = Lstr.replace("b4[x4]", "bq2").replace("^", "**")
        bloc = {"ad1": ad1, "ad2": ad2, "ad3": ad3, "ad4": ad4, "H": H, "bq2": Bq**2,
                "bder1": B4D[0], "bder2": B4D[1], "bder3": B4D[2], "bder4": B4D[3]}
        Ls = sp.sympify(Lstr, locals=bloc)
        check(f"L{k}_equals_gkd_branch", sp.expand(sp.cancel(Ls) - Lsc[k]) == 0, f"L_({k}) = {sp.expand(Lsc[k])}")
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
          f"nabla_mu E_({k})^mu_nu = 0 for nu = x0..x7 (Christoffel symbols of this file; general a4 and b4)")

# ----------------------------------------------------------------------------------------------
# field equations (general b4)
# ----------------------------------------------------------------------------------------------
al = {1: alpha1, 2: alpha2, 3: alpha3}
LHS = [[sp.expand(sum(al[k] * E[k][h][j] for k in (1, 2, 3)) + (Lam if h == j else 0)) for j in range(N8)] for h in range(N8)]
e11, e44, e55, e00 = (sp.expand(LHS[i][i] - Lam) for i in (1, 4, 5, 0))  # x1, x4, x5, x0
e40, e04 = LHS[4][0], LHS[0][4]
Q = sp.expand(sp.cancel(e40 / (Cc * uu)))
check("other_components_vanish",
      all(LHS[h][j] == 0 for h in range(N8) for j in range(N8) if h != j and (h, j) not in ((4, 0), (0, 4))) and
      LHS[1][1] == LHS[2][2] == LHS[3][3] and LHS[5][5] == LHS[6][6] == LHS[7][7],
      "every off-diagonal left-hand side except x4-x0 and x0-x4 is 0; x1 = x2 = x3 and x5 = x6 = x7")
check("offdiagonal_factorises",
      not Q.has(Cc) and sp.expand(e04 + uu * Q / Cc) == 0 and not any(LHS[i][i].has(Cc) for i in range(N8)),
      f"sum_k alpha_k E^x4_x0 = cot z u Q, sum_k alpha_k E^x0_x4 = -tan z u Q, Q = {Q}; the diagonal is free of x0")
J = sp.Matrix([[sp.diff(e11 - e55, ad2), sp.diff(e11 - e55, vv)], [sp.diff(e00, ad2), sp.diff(e00, vv)]]).applyfunc(sp.expand)
lin_ok = all(not x.has(ad2) and not x.has(vv) for x in J) and \
    sp.expand(e11 - e55 - J[0, 0] * ad2 - J[0, 1] * vv - (e11 - e55).subs({ad2: 0, vv: 0})) == 0 and \
    sp.expand(e00 - J[1, 0] * ad2 - J[1, 1] * vv - e00.subs({ad2: 0, vv: 0})) == 0
detJ = sp.factor(J.det())
ein = {alpha1: 1, alpha2: 0, alpha3: 0}
check("second_order_system", lin_ok and detJ != 0 and J.subs(ein) == sp.Matrix([[2, sp.Rational(-1, 2)], [0, sp.Rational(-3, 2)]]),
      f"the x1 - x5 and x0 components are linear in (a4'', v), v = (b4'/b4)', with Jacobian J, det J = {detJ} (not identically zero; Einstein J = [[2, -1/2], [0, -3/2]])")
Iid = sp.expand(e11 + e55 - 2 * e00)
check("algebraic_identity", sp.expand(Iid.subs({uu: 0, vv: 0})) == 0 and sp.expand(Iid.subs(ein) - (sp.Rational(3, 4) * uu**2 + vv / 2)) == 0,
      "sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x0_x0) = I, zero for u = v = 0; Einstein I = (3/4) u^2 + v/2: kappa (p3 + p_t - 2 p0) = I")
check("constraint_first_order", not e44.has(ad2) and not e44.has(vv) and not e44.has(Cc),
      "the x4 component contains a4' and u but no a4'', no v and no x0")
check("bianchi_x4",
      sp.expand(deriv(e44, 4) - 3 * ad1 * (e11 - e55) - sp.Rational(3, 2) * uu * (e55 - e44) - 6 * H * uu * Q) == 0,
      "d/dx4 sum_k alpha_k E^x4_x4 = 3 a4' (E^x1_x1 - E^x5_x5) + (3/2) u (E^x5_x5 - E^x4_x4) + 6 H u Q identically")

# conservation of a general source T(x4, x0)
Tg = [[sp.Integer(0)] * N8 for _ in range(N8)]
for i in (1, 2, 3):
    Tg[i][i] = p3
for i in (5, 6, 7):
    Tg[i][i] = pt
Tg[4][4] = -rho
Tg[0][0] = p0
Tg[4][0] = q40
Tg[0][4] = q04
divT = divergence(Tg)
d4r, d0p0, d0q04, d4q40 = D4SRC[rho], D0SRC[p0], D0SRC[q04], D4SRC[q40]
exp_x4 = -d4r - 3 * ad1 * (p3 - pt) - sp.Rational(3, 2) * uu * (rho + pt) + d0q04 - 6 * H * q04 / Cc
exp_x0 = d0p0 + 3 * H * Cc * (2 * p0 - p3 - pt) + d4q40 + sp.Rational(3, 2) * uu * q40
check("conservation_components",
      all(divT[i] == 0 for i in (1, 2, 3, 5, 6, 7)) and sp.cancel(divT[4] - exp_x4) == 0 and sp.cancel(divT[0] - exp_x0) == 0,
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - p_t) - (3/2) u (rho + p_t) + d0 q04 - 6 H tan z q04; "
      "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (2 p0 - p3 - p_t) + d4 q40 + (3/2) u q40")

check("einstein_components",
      sp.expand(e44.subs(ein) - (3 * ad1**2 + 21 * H**2 - sp.Rational(3, 2) * ad1 * uu - sp.Rational(3, 4) * uu**2)) == 0 and
      sp.expand(e11.subs(ein) - (ad2 - 3 * ad1**2 + 15 * H**2 + 3 * ad1 * uu - sp.Rational(3, 2) * uu**2 - sp.Rational(3, 2) * vv)) == 0 and
      sp.expand(e55.subs(ein) - (-ad2 - 3 * ad1**2 + 15 * H**2 - sp.Rational(3, 4) * uu**2 - vv)) == 0 and
      sp.expand(e00.subs(ein) - (-3 * ad1**2 + 15 * H**2 + sp.Rational(3, 2) * ad1 * uu - sp.Rational(3, 2) * uu**2 - sp.Rational(3, 2) * vv)) == 0 and
      sp.expand(Q.subs(ein) - sp.Rational(3, 2) * H) == 0,
      "Einstein: G^x4_x4 = 3 a4'^2 + 21 H^2 - (3/2) a4' u - (3/4) u^2, G^x1_x1 = a4'' - 3 a4'^2 + 15 H^2 + 3 a4' u - (3/2) u^2 - (3/2) v, "
      "G^x5_x5 = -a4'' - 3 a4'^2 + 15 H^2 - (3/4) u^2 - v, G^x0_x0 = -3 a4'^2 + 15 H^2 + (3/2) a4' u - (3/2) u^2 - (3/2) v, Q = 3 H/2")
nec0 = sp.expand(e00 - e44)
check("einstein_null_energy_x0",
      sp.expand(nec0.subs(ein) - (-6 * H**2 - 3 * ad1**2 - sp.Rational(3, 4) * (uu - 2 * ad1)**2 - sp.Rational(3, 2) * vv)) == 0,
      "Einstein: kappa (rho + p0) = -6 H^2 - 3 a4'^2 - (3/4)(u - 2 a4')^2 - (3/2) v < 0 wherever v >= 0")
check("einstein_no_vacuum",
      sp.expand(Q.subs(ein) - sp.Rational(3, 2) * H) == 0 and sp.expand((e44 - e00).subs(ein).subs({uu: 0, vv: 0}) - 6 * (ad1**2 + H**2)) == 0,
      "T = 0: the x4-x0 equation (3/2) H cot z u = 0 forces u = 0, and then the x4 and x0 equations give 6 (a4'^2 + H^2) = 0, impossible for H > 0")

# exponential histories a4 = A H x4 + a0, b4 = b4(0) e^{beta A H x4}
hist = {ad1: AA * H, ad2: 0, uu: be * AA * H, vv: 0}
h11, h44, h55, h00 = (sp.expand(x.subs(hist)) for x in (e11, e44, e55, e00))
hQ = sp.factor(Q.subs(hist))
check("exponential_history_required_source",
      not any(x.has(Cc) for x in (h11, h44, h55, h00, hQ)) and sp.expand(hQ.subs(ein) - sp.Rational(3, 2) * H) == 0,
      f"on a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) the required rho, p3, p_t, p0 are constants and kappa q40 = cot z beta A H Q, Q = {hQ} (Einstein Q = 3 H/2)")
authW = {alpha1: 1 / H**2, alpha2: sp.Rational(1, 32) / H**4, alpha3: sp.Rational(1, 1152) / H**6, Lam: -10}
hQauth = sp.factor(hQ.subs(authW))
check("author_weights_branch", sp.simplify(hQauth.subs(AA, 1) - 3 * be * (3 * be - 4) / (64 * H)) == 0,
      f"the author's weights (alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lam = -10): Q = {hQauth}; at A = 1, Q = 3 beta (3 beta - 4)/(64 H): q40 = 0 exactly for beta = 0 and beta = 4/3")
hs = [sp.simplify(x) for x in (-(h44 + Lam), h11 + Lam, h55 + Lam, h00 + Lam)]
hsv = [sp.nsimplify(sp.simplify(x.subs(authW).subs({AA: 1, be: sp.Rational(4, 3)}))) for x in hs]
check("author_weights_history_source", hsv == [sp.Rational(-2, 27), sp.Rational(-2, 9), sp.Rational(-22, 27), sp.Rational(-14, 27)],
      f"a4 = H x4, b4 = b4(0) e^((4/3) H x4), the author's weights: kappa (rho, p3, p_t, p0) = {hsv}, q40 = 0 (not a vacuum)")


def numer(e):
    return sp.expand(sp.fraction(sp.cancel(sp.together(e)))[0])


tg = sp.Symbol("tg")
vac_auth = [numer(x.subs(authW)) for x in (h44 + Lam, h11 + Lam, h55 + Lam, h00 + Lam, be * hQ)]
gb = sp.groebner(vac_auth, be, AA, order="lex")
sols = sp.solve(list(gb), [be, AA], dict=True)
real_sols = sorted((s[be], s[AA]) for s in sols if all(v.is_real for v in s.values()))
check("author_weights_no_vacuum_with_b4_not_constant", real_sols == [(0, -1), (0, 1)],
      f"the author's weights: the exponential histories that are vacuum solutions are exactly (beta, A) = {real_sols} (Groebner basis in beta, A with H as a parameter): b4 constant (the withdrawn metric), none with b4 not constant")
egb = {alpha1: 1, alpha3: 0}
qe = sp.expand(hQ.subs(egb))
a2sol = sp.solve(qe, alpha2)  # Q = 0 is linear in alpha2
br1 = {be: 4, alpha2: 1 / (40 * H**2 * (1 - AA**2))}
br2 = {be: 2 * (1 + AA**2) / AA**2, alpha2: -AA**2 / (4 * H**2 * (AA**2 - 1)**2)}
eq_vac = [x.subs(egb) for x in (h11 - h44, h55 - h44, h00 - h44, hQ)]
br_ok = all(sp.simplify(x.subs(br)) == 0 for br in (br1, br2) for x in eq_vac)
# completeness: with alpha2 from Q = 0 the three differences have a common factor; outside the two branches no common zero
rest = [numer(x.subs(egb).subs(alpha2, a2sol[0])) for x in (h11 - h44, h55 - h44, h00 - h44)] if len(a2sol) == 1 else []
g_common = sp.gcd(sp.gcd(rest[0], rest[1]), rest[2]) if rest else sp.Integer(0)
facs = [f for f, _ in sp.factor_list(g_common)[1]]
branch_polys = {sp.expand(be - 4), sp.expand(AA**2 * be - 2 - 2 * AA**2)}
fac_ok = branch_polys <= {sp.expand(f) for f in facs} | {sp.expand(-f) for f in facs}
quot = [sp.quo(r, g_common, AA, be) for r in rest] if rest else []
gq = sp.groebner(quot + [tg * AA * be * H - 1], tg, AA, be, H, order="lex") if quot else None
check("egb_exponential_vacuum_branches", br_ok and fac_ok and gq is not None and list(gq) == [1],
      "Einstein-Gauss-Bonnet (alpha1 = 1, alpha3 = 0): beta = 4, alpha2 = 1/(40 H^2 (1 - A^2)) and beta = 2 (1 + A^2)/A^2, alpha2 = -A^2/(4 H^2 (A^2 - 1)^2) "
      "satisfy every vacuum equation; with alpha2 from Q = 0 the remaining differences share the factors (beta - 4) and (A^2 beta - 2 - 2 A^2) "
      "and have no other common zero with A beta H != 0 (Groebner basis [1]): these are all vacuum exponential histories with b4 not constant")

# ----------------------------------------------------------------------------------------------
# comparison with a4-equations.json (the Wolfram output)
# ----------------------------------------------------------------------------------------------
bb, bd1 = sp.symbols("bb bd1")
LOC = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam,
       "kappa": kappa, "AA": AA, "be": be, "rho": rho, "p3": p3, "pt": pt, "p0": p0, "q40": q40, "q04": q04, "cc": Cc,
       "uu": uu, "vv": vv, "bb": bb, "bd1": bd1,
       **{v.name: v for v in D4SRC.values()}, **{v.name: v for v in D0SRC.values()}}


def parse(s: str):
    s = s.replace("Sqrt[", "sqrt(").replace("]", ")").replace("{", "[").replace("}", "]").replace("^", "**")
    e = sp.sympify(s, locals=LOC)
    return e.subs(bd1, uu * bb) if not isinstance(e, list) else e


def parse_eq(s: str):
    l, r = s.split(" == ")
    return sp.expand(parse(l) - parse(r))


if A4_JSON.exists():
    aj = json.loads(A4_JSON.read_text(encoding="utf-8"))
    ok = True
    for k in (1, 2, 3):
        comp = aj["lovelockTensors"][f"E{k}"]
        for key, (h, j) in {"x0x0": (0, 0), "x1x1": (1, 1), "x4x4": (4, 4), "x5x5": (5, 5), "x4x0": (4, 0), "x0x4": (0, 4)}.items():
            if sp.cancel(parse(comp[key]["input"]) - E[k][h][j]) != 0:
                ok = False
    check("json_lovelock_components", ok, "E_(1..3) components x0x0, x1x1, x4x4, x5x5, x4x0, x0x4 in a4-equations.json (in u = b4'/b4, v = u') equal this file's")
    gs = aj["generalSource"]
    mine = {
        "constraint_x4": e44 + Lam + kappa * rho, "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
        "extraTime_x5_eq_x6_eq_x7": e55 + Lam - kappa * pt, "hidden_x0": e00 + Lam - kappa * p0,
        "offDiagonal_x4x0": e40 - kappa * q40, "offDiagonal_x0x4": e04 - kappa * q04,
        "identity_x1_plus_x5_minus_2x0": Iid - kappa * (p3 + pt - 2 * p0),
    }
    ok = all(sp.cancel(parse_eq(gs[k]["input"]) - v) == 0 for k, v in mine.items())
    ok = ok and sp.expand(parse(gs["offDiagonalFactor_Q"]["input"]) - Q) == 0
    Jw = sp.Matrix(parse(gs["secondOrderJacobian"]["input"]))
    ok = ok and (Jw - J).applyfunc(sp.cancel) == sp.zeros(2, 2) and sp.cancel(parse(gs["secondOrderJacobianDet"]["input"]) - detJ) == 0
    check("json_general_source_equations", ok,
          "constraint, x1, x5, x0, the off-diagonal pair with its factor Q, the identity x1 + x5 - 2 x0 and the Jacobian with its determinant in a4-equations.json equal this file's")
    src = gs["sourceRequiredByGivenHistory"]
    ok = (sp.cancel(parse(src["rho"]["input"]) + (e44 + Lam) / kappa) == 0 and sp.cancel(parse(src["p3"]["input"]) - (e11 + Lam) / kappa) == 0
          and sp.cancel(parse(src["pt"]["input"]) - (e55 + Lam) / kappa) == 0 and sp.cancel(parse(src["p0"]["input"]) - (e00 + Lam) / kappa) == 0
          and sp.cancel(parse(src["q40"]["input"]) - e40 / kappa) == 0 and sp.cancel(parse(src["q04"]["input"]) - e04 / kappa) == 0)
    nc = gs["nullCombinations"]
    ok = ok and sp.expand(parse(nc["kappa(rho+p0)"]["input"]) - nec0) == 0 and sp.expand(parse(nc["kappa(rho+p3)"]["input"]) - (e11 - e44)) == 0 \
        and sp.expand(parse(nc["kappa(rho+pt)"]["input"]) - (e55 - e44)) == 0
    check("json_required_source_and_null_combinations", ok, "sourceRequiredByGivenHistory (with q40, q04) and nullCombinations equal this file's")
    cx4 = parse_eq(gs["conservation_x4"]["input"])
    cx0 = parse_eq(gs["conservation_x0"]["input"])
    check("json_conservation", sp.cancel(cx4 - exp_x4) == 0 and sp.cancel(cx0 - exp_x0) == 0,
          "conservation_x4 and conservation_x0 in a4-equations.json equal this file's covariant divergence")
    ei = aj["einstein"]
    ok = (sp.expand(parse_eq(ei["constraint_x4"]["input"]) - (e44.subs(ein) + Lam + kappa * rho)) == 0
          and sp.expand(parse_eq(ei["space_x1"]["input"]) - (e11.subs(ein) + Lam - kappa * p3)) == 0
          and sp.expand(parse_eq(ei["extraTime_x5"]["input"]) - (e55.subs(ein) + Lam - kappa * pt)) == 0
          and sp.expand(parse_eq(ei["hidden_x0"]["input"]) - (e00.subs(ein) + Lam - kappa * p0)) == 0
          and sp.expand(parse_eq(ei["offDiagonal_x4x0"]["input"]) - (e40.subs(ein) - kappa * q40)) == 0
          and sp.expand(parse_eq(ei["nullEnergy"]["input"]) - (kappa * (rho + p0) - nec0.subs(ein))) == 0)
    check("json_einstein", ok, "the Einstein special case in a4-equations.json (all components, the off-diagonal pair, the null energy) equals this file's")
    eh = aj["exponentialHistory"]["requiredSource"]
    ok = (sp.simplify(parse(eh["rho"]["input"]) + (h44 + Lam) / kappa) == 0 and sp.simplify(parse(eh["p3"]["input"]) - (h11 + Lam) / kappa) == 0
          and sp.simplify(parse(eh["pt"]["input"]) - (h55 + Lam) / kappa) == 0 and sp.simplify(parse(eh["p0"]["input"]) - (h00 + Lam) / kappa) == 0
          and sp.simplify(parse(eh["Q"]["input"]) - hQ) == 0 and sp.simplify(parse(eh["q40"]["input"]) - Cc * be * AA * H * hQ / kappa) == 0
          and sp.simplify(parse(aj["exponentialHistory"]["authorWeights"]["Q"]["input"]) - hQauth) == 0)
    check("json_exponential_history", ok, "rho, p3, p_t, p0, q40 and Q of the exponential history (and Q for the author's weights) in a4-equations.json equal this file's")
else:
    aj = None
    check("json_comparison", False, "a4-equations.json missing (run the Wolfram verifier first)", pending=True)

# ----------------------------------------------------------------------------------------------
# spinor lemmas: the author's T16 (primary) and, for comparison only, a representation built here
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
    # COMPARISON representation only (not used for any result): space-like e1..e4 (square +1), time-like
    # f1..f4 (square -1); a tensor-product construction different from the Wolfram comparison representation
    e1, e2 = kron(s1, I2, I2, I2), kron(s3, I2, I2, I2)
    f1, f2 = kron(ep, s1, I2, I2), kron(ep, s3, I2, I2)
    e3, e4 = kron(ep, ep, s1, I2), kron(ep, ep, s3, I2)
    f3, f4 = kron(ep, ep, ep, s1), kron(ep, ep, ep, s3)
    return [e4, e1, e2, e3, f1, f2, f3, f4]  # x0, x1, ..., x7 (the same generator per coordinate as before 2026-10-14)


def author_rep():
    # the PRIMARY representation: the author's T16 of Revision/algebra/gammas.json (read strictly at start-up),
    # gamma^(xk) = T16[k], k = 0..7 (SPEC section 2)
    return FIXTURE["gamma"]


def intertwiners(src, dst):
    """Basis of {K : K src[a] = dst[a] K for all a}, exact (DomainMatrix nullspace over QQ).

    Row-major vec(K), unknown K[p, q] at index 16 p + q:  (K A)[i, j] = sum_k K[i, k] A[k, j],
    (B K)[i, j] = sum_k B[i, k] K[k, j]."""
    from sympy.polys.domains import QQ
    from sympy.polys.matrices import DomainMatrix
    n = 16
    rows = {}  # sparse: {row: {column: value}}
    r = 0
    for A, B in zip(src, dst):
        for i in range(n):
            for j in range(n):
                row = {}
                for k in range(n):
                    if A[k, j] != 0:
                        row[i * n + k] = row.get(i * n + k, 0) + sp.Rational(A[k, j])
                    if B[i, k] != 0:
                        row[k * n + j] = row.get(k * n + j, 0) - sp.Rational(B[i, k])
                row = {c: QQ(int(v.p), int(v.q)) for c, v in row.items() if v != 0}
                if row:
                    rows[r] = row
                r += 1
    ns = DomainMatrix(rows, (r, n * n), QQ).nullspace().to_Matrix()
    return [sp.Matrix(n, n, list(ns.row(b))) for b in range(ns.rows)]


Z16 = sp.zeros(16, 16)
MM = sp.Symbol("MM", real=True)


def spinor_checks(label: str, gF, prefix: str = ""):
    """The spinor lemmas in the representation gF (general a4 and b4); prefix labels every detail."""

    def lcheck(name, ok, detail):
        check(name, ok, prefix + detail)

    I16 = sp.eye(16)
    cl = all(gF[a] * gF[b] + gF[b] * gF[a] == 2 * eta[a] * (1 if a == b else 0) * I16 for a in range(8) for b in range(8))
    lcheck(f"{label}_clifford", cl, "{gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,1,-1,-1,-1,-1)")
    C = gF[0] * gF[1] * gF[2] * gF[3]
    cprops = C == C.T and C * C == I16 and all((C * g).T == -(C * g) for g in gF) and all(x.is_real for x in C)
    lcheck(f"{label}_C_properties", cprops, "C = gamma^x0 gamma^x1 gamma^x2 gamma^x3 real symmetric, C^2 = 1, C gamma^a antisymmetric")
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
    lcheck(f"{label}_Omega_x0_x4_zero", Om[4] == Z16 and Om[0] == Z16, "Omega_x0 = Omega_x4 = 0")
    lcheck(f"{label}_anticommutator_no_sum",
           all((gC[m] * Om[m] + Om[m] * gC[m]).applyfunc(norm) == Z16 for m in range(8)),
           "{gamma^mu, Omega_mu} = 0 for each mu (no sum)")
    Gd = sum((gC[m] * Om[m] for m in range(8)), Z16).applyfunc(norm)
    lcheck(f"{label}_gravity_term", (Gd - 3 * H * gF[0] - sp.Rational(3, 4) * uu * gF[4]).applyfunc(sp.expand) == Z16,
           "gamma^mu Omega_mu = 3 H gamma^x0 + (3/4)(b4'/b4) gamma^x4")
    A = (-gC[4] * (MM * I16 - Gd)).applyfunc(sp.expand)
    A0 = (A + sp.Rational(3, 4) * uu * I16).applyfunc(sp.expand)  # the b4-free part: Phi = b4^(-3/4) chi, d4 chi = A0 chi
    lcheck(f"{label}_condensate_S_b4_three_halves_constant",
           (C * A + A.T * C + sp.Rational(3, 2) * uu * C).applyfunc(sp.expand) == Z16 and not any(x.has(uu) for x in A0),
           "C A + A^T C = -(3/2)(b4'/b4) C: b4^(3/2) S is constant along x4; A = A0 - (3/4)(b4'/b4) with A0 free of b4")
    adj = (A.T * C * gC[4] - C * sum((Om[m] * gC[m] for m in range(8)), Z16) + MM * C).applyfunc(norm)
    lcheck(f"{label}_condensate_adjoint", adj == Z16, "(D_mu Phibar) gamma^mu = -M Phibar for the condensate")

    def dphi(nu):
        return (A if nu == 4 else Z16) + Om[nu]

    def dphibar(nu):
        return (A.T * C if nu == 4 else Z16) - C * Om[nu]

    Nm = [[((C * gC[m] * dphi(n) - dphibar(n) * gC[m]) / 2) for n in range(8)] for m in range(8)]
    Ns = [[((Nm[m][n] + (gdiag[n] / gdiag[m]) * Nm[n][m]) / 2).applyfunc(norm) for n in range(8)] for m in range(8)]
    diag_ok = Ns[4][0] == Z16 and Ns[0][4] == Z16 and all(Ns[m][m] == Z16 for m in (0, 1, 2, 3, 5, 6, 7)) and \
        (Ns[4][4] - MM * C).applyfunc(sp.expand) == Z16
    lcheck(f"{label}_condensate_kinetic_diagonal", diag_ok, "K^x4_x4 = M S, K^mu_mu = 0 otherwise, K^x4_x0 = K^x0_x4 = 0 (general b4)")
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
            idx = next((i, j) for i in range(16) for j in range(16) if B[i, j] != 0)
            X = norm(Nmn[idx] / B[idx])
            if X != 0 and (Nmn - X * B).applyfunc(norm) == Z16:
                triples_found.add(t)
                coeffs_found[(m, n)] = (t, X)
                found = True
                break
        ok = ok and found
    exp_trip = {tuple(sorted((i, 4, 0))) for i in (1, 2, 3, 5, 6, 7)} | {tuple(sorted((i, j, 4))) for i in (1, 2, 3) for j in (5, 6, 7)}
    lcheck(f"{label}_condensate_offdiagonal_three_gamma", ok and triples_found == exp_trip,
           f"every nonzero off-diagonal kinetic component ({len(expected)} ordered pairs) is a multiple of one of the 15 bilinears Phibar gamma^a gamma^b gamma^c Phi, {{a,b,c}} = {{i,x4,x0}} or {{i,j,x4}}")
    # exact witness at (M, H) = (5, 1): chi = e^{-4 i x4} Phi0 with A0 Phi0 = -4 i Phi0; Phi = b4^(-3/4) chi
    Av = A0.subs({MM: 5, H: 1})
    w = 4

    def sector(e):
        stack = sp.Matrix.vstack(Av + sp.I * w * I16, gF[1] * gF[5] - e * I16, gF[2] * gF[6] - e * I16, gF[3] * gF[7] - e * I16)
        return stack.nullspace()

    n1, n2 = sector(-1), sector(1)
    wit_ok = len(n1) == 1 and len(n2) == 1
    if wit_ok:
        v1, v2 = n1[0], n2[0]
        s = sp.expand((v1.H * C * v2)[0])
        ph = v1 + sp.conjugate(s) * v2
        ph = ph.applyfunc(sp.expand)
        Sval = sp.expand((ph.H * C * ph)[0])
        # d4 (b4^(-3/4) e^{-4 i x4} Phi0) = (-(3/4) u - 4 i) Phi equals A Phi = (A0 - (3/4) u) Phi
        lhs = (-sp.Rational(3, 4) * uu - sp.I * w) * ph
        rhs = (A.subs({MM: 5, H: 1}) * ph)
        wit_ok = (Av * ph + sp.I * w * ph).applyfunc(sp.expand) == sp.zeros(16, 1) and (lhs - rhs).applyfunc(sp.expand) == sp.zeros(16, 1) \
            and Sval != 0 and sp.im(Sval) == 0
        for t in exp_trip:
            B = C * gF[t[0]] * gF[t[1]] * gF[t[2]]
            wit_ok = wit_ok and sp.expand((ph.H * B * ph)[0]) == 0
    lcheck(f"{label}_condensate_witness", wit_ok,
           "exact witness at (M, H) = (5, 1): Phi = b4^(-3/4) e^{-4 i x4} Phi0, Phi0 = v1 + conj(v1^dagger C v2) v2 from the sectors gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1, +1 of A0; it solves d4 Phi = A Phi for every b4; all 15 three-gamma bilinears vanish, b4^(3/2) S != 0 real")
    return coeffs_found


orep = own_rep()
coeffs_own = spinor_checks("ownrep", orep, prefix="comparison representation (own_rep, built here; not used for any result): ")
arep = author_rep()
fixture_C = arep[0] * arep[1] * arep[2] * arep[3]
fixture_Gamma = arep[0] * arep[1] * arep[2] * arep[3] * arep[4] * arep[5] * arep[6] * arep[7]
fixture_S_ok = all(FIXTURE["S"][a][b] == (arep[a] * arep[b] - arep[b] * arep[a]) / 4 for a in range(8) for b in range(8))
check("authorT16_fixture_read",
      FIXTURE["coordinates"] == COORDS and FIXTURE["notebookFrameIndex"] == [0, 1, 2, 3, 4, 5, 6, 7]
      and FIXTURE["eta"] == eta and FIXTURE["C"] == fixture_C and len(arep) == 8
      and fixture_S_ok and FIXTURE["Gamma"] == fixture_Gamma and FIXTURE["B"] == -sp.I * fixture_C * arep[4],
      f"Revision/algebra/gammas.json (sha256 {FIXTURE['sha256']}) read with strict parsing (every entry a JSON integer or a "
      "string \"p/q\" in lowest terms; a missing or malformed file stops the run with an ERROR line and exit code 1): "
      "coordinates x0..x7 (the author's), notebook frame index [0, 1, 2, 3, 4, 5, 6, 7] (gamma^(xk) = T16[k]), "
      "eta = diag(1,1,1,1,-1,-1,-1,-1), the fixture's C equals gamma^x0 gamma^x1 gamma^x2 gamma^x3 (the notebook's sigma16), "
      "its S, Gamma and B equal (1/4)[gamma^a, gamma^b], gamma^x0 gamma^x1 ... gamma^x7 and -i C gamma^x4; "
      "the author's T16 is the primary representation (its coefficients are compared with a4-equations.json)")
coeffs_author = spinor_checks("authorT16", arep)

kb = intertwiners(orep, arep)  # K gamma_own^a = gamma_T16^a K
Kmat = kb[0] if len(kb) == 1 else Z16
kc = (Kmat.T * Kmat)[0, 0]
C_own = orep[0] * orep[1] * orep[2] * orep[3]
equiv_ok = (len(kb) == 1 and kc > 0 and Kmat.T * Kmat == kc * sp.eye(16)
            and all(Kmat * orep[a] == arep[a] * Kmat for a in range(8)) and Kmat * C_own == fixture_C * Kmat)
check("representations_equivalent_authorT16_ownrep", equiv_ok,
      f"exact (sympy DomainMatrix nullspace over QQ): the intertwiners K with K gamma_own^a = gamma_T16^a K for a = x0..x7 "
      f"(gamma_own the comparison representation) form a space of dimension {len(kb)}, and K^T K = {kc} I16 "
      f"(K is sqrt({kc}) times an orthogonal matrix) with K C_own = C_T16 K: the comparison representation is equivalent "
      "to the author's T16, so every trace of a product of gammas is the same in both")

# compare the off-diagonal coefficients of the author's T16 (primary) with a4-equations.json
# (numerically, 40 digits, at three points of (a4, cot z, H, a4', b4, u))
if aj is not None:
    offj = aj["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    a4v = sp.Symbol("a4v")
    loc2 = dict(LOC)
    loc2["a4v"] = a4v
    pts = [(sp.Rational(3, 7), sp.Rational(5, 3), sp.Rational(2, 5), sp.Rational(-4, 9), sp.Rational(7, 3), sp.Rational(1, 5)),
           (sp.Rational(-1, 3), sp.Rational(1, 2), sp.Rational(7, 4), sp.Rational(5, 2), sp.Rational(1, 4), sp.Rational(-3, 2)),
           (sp.Rational(2, 1), sp.Rational(9, 5), sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(5, 2), sp.Rational(2, 3))]
    mpmath.mp.dps = 40
    ok = len(offj) == len(coeffs_author)
    for entry in offj:
        comp = entry["component"].split(" ")[0]  # K^x1_x4; the coordinate xk has index k
        mu = int(comp[3])
        nu = int(comp.split("_")[1][1])
        if (mu, nu) not in coeffs_author or len(entry["terms"]) != 1:
            ok = False
            continue
        t, X = coeffs_author[(mu, nu)]
        names = entry["terms"][0]["bilinear"].replace("Phibar ", "").replace(" Phi", "").split(" ")
        tj = tuple(int(nm[-1]) for nm in names)
        if tj != t:
            ok = False
            continue
        s = entry["terms"][0]["coefficient"]["input"].replace("Sqrt[", "sqrt(").replace("]", ")").replace("^", "**")
        Xj = sp.sympify(s, locals=loc2)
        for av, cv, hv, a1v, bv, uv in pts:
            vj = sp.N(Xj.subs({a4v: av, Cc: cv, H: hv, ad1: a1v, bb: bv, uu: uv}), 40)
            vm = sp.N(X.subs({Ee: sp.exp(av), Sh: (1 + cv**2) ** sp.Rational(-1, 12), Cc: cv, H: hv, ad1: a1v, Bq: sp.sqrt(bv), uu: uv}), 40)
            if abs(vj - vm) > sp.Float("1e-30") * (1 + abs(vm)):
                ok = False
    check("json_offdiagonal_coefficients", ok,
          "every off-diagonal kinetic coefficient of a4-equations.json equals this file's (the author's T16, the primary representation, general b4; same triple, value at three exact points to 40 digits)")
same = set(coeffs_author) == set(coeffs_own) and all(
    coeffs_author[k][0] == coeffs_own[k][0] and sp.simplify(coeffs_author[k][1] - coeffs_own[k][1]) == 0 for k in coeffs_own)
check("offdiagonal_coefficients_representation_independent", same,
      "the author's T16 (primary) and the comparison representation built here give the same triples and the same coefficients (general b4)")

# the condensate as a source with b4 not constant (q40 = q04 = 0, p3 = p_t = p0)
cond_auth = [numer(x.subs(authW)) for x in (be * hQ, h11 - h55, h11 - h00)]
gca = sp.groebner(cond_auth + [tg * be * H - 1], tg, be, AA, H, order="lex")
# a real solution would make every element of the basis vanish; the element in AA alone has no real root
gca_uni = [g for g in gca if g.free_symbols == {AA}]
auth_no_real = list(gca) == [1] or any(sp.Poly(g, AA).count_roots() == 0 for g in gca_uni)
cond_egb = [numer(x.subs(egb).subs(alpha2, a2sol[0])) for x in (h11 - h55, h11 - h00)] if len(a2sol) == 1 else []
gce = sp.gcd(cond_egb[0], cond_egb[1]) if cond_egb else sp.Integer(0)
fce = {sp.expand(f) for f, _ in sp.factor_list(gce)[1]} | {sp.expand(-f) for f, _ in sp.factor_list(gce)[1]}
qce = [sp.quo(r, gce, AA, be) for r in cond_egb] if cond_egb else []
gqe = sp.groebner(qce + [tg * AA * be * H - 1], tg, AA, be, H, order="lex") if qce else None
check("condensate_source_with_b4_not_constant",
      sp.expand(Q.subs(ein) - sp.Rational(3, 2) * H) == 0 and auth_no_real and branch_polys <= fce and gqe is not None and list(gqe) == [1],
      "a source with q40 = q04 = 0 and p3 = p_t = p0 (the homogeneous condensate) and b4 not constant: Einstein impossible (Q = 3 H/2 forces b4' = 0); "
      "the author's weights: no exponential history with beta != 0 (the Groebner basis of the conditions with beta H != 0 contains a polynomial in A without real roots); Einstein-Gauss-Bonnet: only the two branches beta = 4 and beta = 2 (1 + A^2)/A^2 (alpha2 from Q = 0)")

t_total = time.time() - t_start

# ----------------------------------------------------------------------------------------------
# outputs
# ----------------------------------------------------------------------------------------------
npass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
nfail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
npend = sum(1 for c in CHECKS if c["verdict"] == "pending")
report = {
    "producer": "Revision/field_equations_a4/python/check_field_equations_a4.py (sympy, exact)",
    "spec": "Revision/SPEC.md section 5 (the metric with b4(x4), general a4 and b4)",
    "inputsChecked": ["Revision/gkd_lovelock/results/lovelock-tensors.json", "Revision/field_equations_a4/a4-equations.json",
                      "Revision/algebra/gammas.json (author's T16: the primary representation, required)"],
    "checkCount": len(CHECKS), "passCount": npass, "failCount": nfail, "pendingCount": npend,
    "verdict": "PASS" if nfail == 0 and npend == 0 else ("FAIL" if nfail else "PENDING"),
    "checks": CHECKS,
}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_bytes((json.dumps(report, indent=2) + "\n").encode("utf-8"))


def lx(e) -> str:
    s = sp.latex(e, symbol_names={ad1: "a_4'", ad2: "a_4''", alpha1: r"\alpha_1", alpha2: r"\alpha_2", alpha3: r"\alpha_3",
                                   Lam: r"\Lambda", AA: "A", be: r"\beta", uu: "u", vv: "v", p3: "p_3", pt: "p_t", p0: "p_0"})
    return s.replace("a_4'^{2}", "(a_4')^{2}").replace("a_4'^{4}", "(a_4')^{4}").replace("a_4'^{6}", "(a_4')^{6}")


lines = [
    "# Field equations for a4[x4] and b4[x4] (summary generated by check_field_equations_a4.py)",
    "",
    "Computed by Revision code from the metric of `Revision/SPEC.md` section 1 with b4(x4), for general a4 and b4",
    "(b4 is never set to 1); every line below is an output of",
    "`Revision/field_equations_a4/python/check_field_equations_a4.py` (sympy), cross-checked against the Wolfram",
    "output `Revision/field_equations_a4/a4-equations.json`. Report: `reports/python-a4-report.json`.",
    "",
    "Field equations: $\\sum_{k=1}^{3}\\alpha_k E_{(k)}{}^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu = \\kappa T^\\mu{}_\\nu$,",
    "$E_{(k)} = -P_{(k)}/2^{k+1}$, $T = \\mathrm{diag}(p_0,p_3,p_3,p_3,-\\rho,p_t,p_t,p_t)$ (order x0..x7) $+ q_{40}, q_{04}$;",
    "$u = b_4'/b_4$, $v = u'$.",
    "",
    "## Independent components (general Lovelock, general b4)",
    "",
    f"* constraint (x4): $ {lx(e44)} + \\Lambda = -\\kappa\\rho$",
    f"* 3-space (x1 = x2 = x3): $ {lx(e11)} + \\Lambda = \\kappa p_3$",
    f"* extra times (x5 = x6 = x7): $ {lx(e55)} + \\Lambda = \\kappa p_t$",
    f"* hidden (x0): $ {lx(e00)} + \\Lambda = \\kappa p_0$",
    f"* off-diagonal: $\\kappa q_{{40}} = \\cot z\\, u\\, Q$, $\\kappa q_{{04}} = -\\tan z\\, u\\, Q$, $Q = {lx(Q)}$; all other off-diagonal components $0 = \\kappa T^\\mu{{}}_\\nu$",
    "* the x1 - x5 and x0 components are linear in $(a_4'', v)$ and determine them where their Jacobian is nonsingular; the x4 component is the constraint",
    f"* identity: $\\kappa(p_3 + p_t - 2p_0) = {lx(Iid)}$",
    "",
    "## Einstein gravity ($\\alpha_1 = 1$, $\\alpha_2 = \\alpha_3 = 0$)",
    "",
    f"* $ {lx(e44.subs(ein))} + \\Lambda = -\\kappa\\rho$, $ {lx(e00.subs(ein))} + \\Lambda = \\kappa p_0$, $Q = 3H/2$: a source with $q_{{40}} = 0$ forces $b_4' = 0$",
    f"* $\\kappa(\\rho + p_0) = {lx(nec0.subs(ein))}$; no vacuum solution for $H > 0$ and any $\\Lambda$",
    "",
    "## Exponential histories $a_4 = A H x_4 + a_0$, $b_4 = b_4(0) e^{\\beta A H x_4}$",
    "",
    f"* $\\kappa q_{{40}} = \\cot z\\,\\beta A H\\, Q$, $Q = {lx(hQ)}$",
    f"* the author's weights: $Q = {lx(hQauth)}$; at $A = 1$: $q_{{40}} = 0$ exactly for $\\beta = 0$ and $\\beta = 4/3$; at $\\beta = 4/3$: $\\kappa(\\rho, p_3, p_t, p_0) = (-2/27, -2/9, -22/27, -14/27)$ (not a vacuum)",
    "* vacuum: the author's weights only for $\\beta = 0$, $A = \\pm 1$; Einstein-Gauss-Bonnet only for $\\beta = 4$ or $\\beta = 2(1 + A^2)/A^2$ with a tuned $\\alpha_2$",
    "",
    r"## Field sources (convention $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu \mathcal{L})$, $\sigma_T = +1$ per SPEC section 4)",
    "",
    r"* lemmas: $\gamma^\mu\Omega_\mu = 3H\gamma^{x0} + \tfrac34 u\,\gamma^{x4}$; $\{\gamma^\mu,\Omega_\mu\}=0$ for each $\mu$ (no sum)",
    r"* dirac16complex00, homogeneous condensate $\Phi(x_4) = b_4^{-3/4}\chi$: $b_4^{3/2}S$ constant, $\rho = \sigma_T(mS+U)$, $p_3=p_t=p_0=\sigma_T(SU'-U)$, $q_{40} = 0$;",
    r"  the off-diagonal equations need the 15 bilinears $\bar\Phi\gamma^a\gamma^b\gamma^c\Phi$ to vanish (exact witnesses exist);",
    r"  with $b_4$ not constant such a source is impossible in Einstein gravity, sources no exponential history for the author's weights, and only the two tuned branches in Einstein-Gauss-Bonnet",
    r"* dirac16complex: the same with normal-ordered expectation values (the operator form of the on-shell trace identity is ASSUMED for the field on a whole slice)",
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
