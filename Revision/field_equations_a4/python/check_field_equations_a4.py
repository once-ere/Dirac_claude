#!/usr/bin/env python3
"""Revision field equations for a4[x4] and b4[x4]: independent sympy derivation and cross-check.

Revision/SPEC.md section 5, for the CORRECTED primordial metric of 2026-10-16 (version 2; SPEC section 1,
Revision/metric_warped/), general functions a4(x4) and b4(x4) > 0 and every real z = 6 H x0 (the user's order
"go ahead with the recomputation using the corrected metric", HANDOFF.md 0.10, phase W2; the metric of 2026-10-14 and
its off-diagonal pair E^x4_x0 are withdrawn).  Revision code only; nothing is imported from the old stages and nothing
from the Wolfram side is used as an input except the files that are being CHECKED and the fixture:

  Revision/gkd_lovelock/results/lovelock-tensors.json   (the GKD branch's exact monomial lists, 14 exponents)
  Revision/field_equations_a4/a4-equations.json         (written by the Wolfram verifier)
  Revision/metric_warped/results/warped-metric.json     (the independent sympy record of the corrected metric)
  Revision/algebra/gammas.json                          (the author's T16, order x0..x7: REQUIRED; read
                                                         strictly; a missing or malformed file stops the
                                                         run at once with a line "ERROR  ..." and exit code 1)

Everything else is computed here from the metric of SPEC section 1, by a different implementation:
  * the metric is written in the symbols Ee = e^{a4}, Bq = b4^{1/2}, Cc = cot z (signed), Ww = (sin^2 z)^{1/12} > 0
    (z = 6 H x0) in the author's coordinates x0..x7 (index k = xk) with exact derivation rules (d/dx4: a4^(n) ->
    a4^(n+1), Ee -> a4' Ee, Bq -> u Bq/2, u -> v -> w -> w5 with u = b4'/b4, v = u'; d/dx0: Ww -> H Cc Ww,
    Cc -> -6 H (1 + Cc^2)) and the relation Ww^12 (1 + Cc^2) = 1, valid for every real z, so no trigonometric
    simplification is needed:
        g = diag(Bq^2 Cc^2/Ee^2, Ee^2, Ee^2, Ee^2, -1, -Bq^2 Ww^2/Ee^2 (x3));
  * Christoffel symbols, Riemann R^{ab}_{cd} (MTW), Ricci and Einstein tensors;
  * GKD as the sign of a permutation (not as a determinant);
  * the Lovelock tensors P_(1), P_(2), P_(3) as polynomials (sympy Poly) in H, a4', a4'', u, v and k = e^{2a4}/b4;
  * the field equations, their structure, the Bianchi identity, conservation, the exponential histories
    (linear algebra and Groebner bases for the vacuum and condensate questions);
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
MW_JSON = REV / "metric_warped" / "results" / "warped-metric.json"
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
# symbols and exact derivations (the corrected metric, general a4 and b4, every real z)
# ----------------------------------------------------------------------------------------------
H, ad1, ad2, ad3, ad4 = sp.symbols("H ad1 ad2 ad3 ad4")
Ee, Bq, Ww = sp.symbols("Ee Bq Ww", positive=True)  # e^{a4}, b4^{1/2}, (sin^2 z)^{1/12}
Cc = sp.Symbol("Cc", real=True)  # cot z, signed
uu, vv, ww, w5 = sp.symbols("uu vv ww w5")  # u = b4'/b4, v = u', w = v', w5 = w'
kk = sp.Symbol("kk", positive=True)  # k = e^{2 a4}/b4 = Ee^2/Bq^2
alpha1, alpha2, alpha3, Lam, kappa, AA, be = sp.symbols("alpha1 alpha2 alpha3 Lam kappa AA be")
# p0 = the pressure along the hidden direction x0; q40 = T^x4_x0, q04 = T^x0_x4
rho, p3, pt, p0, q40, q04 = sp.symbols("rho p3 pt p0 q40 q04")
SRC = [rho, p3, pt, p0, q40, q04]
D4SRC = {s: sp.Symbol("d4" + s.name) for s in SRC}
D0SRC = {s: sp.Symbol("d0" + s.name) for s in SRC}

RULE4 = {ad1: ad2, ad2: ad3, ad3: ad4, Ee: ad1 * Ee, Bq: uu * Bq / 2, uu: vv, vv: ww, ww: w5, **D4SRC}
RULE0 = {Ww: H * Cc * Ww, Cc: -6 * H * (1 + Cc**2), **D0SRC}


def deriv(e, mu: int):
    """Partial derivative with respect to coordinate index mu (0..7 = the author's x0..x7)."""
    rule = RULE4 if mu == 4 else RULE0 if mu == 0 else None
    if rule is None:
        return sp.Integer(0)
    return sp.Add(*[sp.diff(e, s) * v for s, v in rule.items() if e.has(s)])


def _reduce_w(p):
    """Reduce the powers of Ww >= 12 with Ww^12 = 1/(1 + Cc^2) (exact for every real z)."""
    p = sp.expand(p)
    if not p.has(Ww):
        return p
    out = sp.Integer(0)
    for term in sp.Add.make_args(p):
        c, n = term.as_coeff_exponent(Ww)
        n = int(n)
        q, r = divmod(n, 12)
        out += c * Ww**r * (1 + Cc**2) ** (-q)
    return sp.expand(out)


def norm(e):
    """Canonical rational form: powers of Ww reduced modulo 12 in numerator and denominator, then cancelled."""
    e = sp.cancel(sp.expand(e))
    if e.has(Ww):
        n, d = sp.fraction(e)
        e = sp.cancel(_reduce_w(n) / _reduce_w(d))
    return e


N8 = 8
COORDS = [f"x{i}" for i in range(8)]  # the author's x0..x7
gdiag = [Bq**2 * Cc**2 / Ee**2] + [Ee**2] * 3 + [sp.Integer(-1)] + [-(Bq**2) * Ww**2 / Ee**2] * 3
ginv = [sp.cancel(1 / x) for x in gdiag]
vielb = [Bq * Cc / Ee] + [Ee] * 3 + [sp.Integer(1)] + [Bq * Ww / Ee] * 3  # e^a_mu, (e^a_mu)^2 = |g_mumu|; e^x0 signed
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

check("mixed_riemann_free_of_x0",
      all(not v.has(Ww) and not v.has(Cc) for v in RUU.values()) and len(RUU) == 112,
      f"every R^ab_cd is free of x0 (no Ww = (sin^2 z)^(1/12), no cot z; symbol calculus of this file, general a4 and b4, every real z); {len(RUU)} nonzero of 4096 ordered index lists")
check("mixed_riemann_only_sectional",
      all({c, d} == {a, b} for (a, b, c, d) in RUU),
      f"every nonzero R^ab_cd has {{c, d}} = {{a, b}} ({len(RUU) // 4} planes); no mixed component")
check("riemann_pair_antisymmetry",
      all(sp.cancel(RUU.get((b, a, c, d), 0) + v) == 0 and sp.cancel(RUU.get((a, b, d, c), 0) + v) == 0 for (a, b, c, d), v in RUU.items()),
      "R^{ab}_{cd} = -R^{ba}_{cd} = -R^{ab}_{dc}")

# Ricci and Einstein (mixed)
ricci_mixed = [[norm(sum(RUU.get((a, h, a, j), 0) for a in range(N8))) for j in range(N8)] for h in range(N8)]
Rscal = norm(sum(ricci_mixed[i][i] for i in range(N8)))
G = [[norm(ricci_mixed[h][j] - (sp.Rational(1, 2) * Rscal if h == j else 0)) for j in range(N8)] for h in range(N8)]


# ----------------------------------------------------------------------------------------------
# the variables of the field equations and the polynomial ring
# ----------------------------------------------------------------------------------------------
GENS = (H, ad1, ad2, uu, vv, kk)


def to_uvk(v):
    """A function of a4', a4'', e^{a4}, b4 (through Bq, u, v), free of x0, written in u, v and k = Ee^2/Bq^2."""
    e = sp.cancel(sp.sympify(v).subs(Ee, sp.sqrt(kk) * Bq))
    if e.has(Bq) or e.has(Ee) or e.has(Ww) or e.has(Cc):
        raise ValueError(f"not a function of H, a4', a4'', u, v, k only: {v}")
    return e


def ring_poly(v):
    e = to_uvk(v)
    n, d = sp.fraction(sp.cancel(e))
    if d.free_symbols:
        raise ValueError(f"not a polynomial in {GENS}: {e}")
    return sp.Poly(sp.expand(n / d), *GENS)


pairs = [(a, b, c, d, ring_poly(v)) for (a, b, c, d), v in sorted(RUU.items()) if a < b and c < d]
check("riemann_entries_polynomial",
      all(sp.expand(p.as_expr() - to_uvk(RUU[(a, b, c, d)])) == 0 for a, b, c, d, p in pairs) and len(pairs) == 28,
      f"the {len(pairs)} components R^ab_cd (a<b, c<d) are polynomials in H, a4', a4'', u = b4'/b4, v = u', k = e^(2a4)/b4")
cflat = sp.Symbol("cflat")
flat = {ad1: 0, ad2: 0, uu: 2 / (sp.Symbol("x4") - cflat), vv: -2 / (sp.Symbol("x4") - cflat)**2,
        kk: 1 / (H**2 * (sp.Symbol("x4") - cflat)**2)}
check("flat_member", all(sp.simplify(p.as_expr().subs(flat)) == 0 for *_, p in pairs),
      "a4 = 0, b4 = H^2 (x4 - c)^2 (u = 2/(x4 - c), v = -2/(x4 - c)^2, k = 1/(H^2 (x4 - c)^2)): every R^ab_cd vanishes (the flat member)")


# ----------------------------------------------------------------------------------------------
# GKD as a permutation sign and the Lovelock tensors
# ----------------------------------------------------------------------------------------------
def gkd(up, low) -> int:
    if len(set(up)) != len(up) or set(up) != set(low):
        return 0
    perm = [up.index(x) for x in low]
    inv = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
    return -1 if inv % 2 else 1


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
    return [[sp.expand(P[h][j].as_expr()) for j in range(N8)] for h in range(N8)], sp.expand(L.as_expr())


t0 = time.time()
P = {}
Lsc = {}
for k in (1, 2, 3):
    P[k], Lsc[k] = lovelock(k)
t_lovelock = time.time() - t0

Guvk = [[sp.expand(to_uvk(G[h][j])) for j in range(N8)] for h in range(N8)]
check("P1_equals_minus_4_Einstein",
      all(sp.expand(P[1][h][j] + 4 * Guvk[h][j]) == 0 for h in range(N8) for j in range(N8)),
      "P_(1)^h_j (GKD permutation sign) = -4 G^h_j (Ricci route), all 64 components (general a4 and b4)")
for k in (1, 2, 3):
    check(f"P{k}_trace_identity", sp.expand(sum(P[k][i][i] for i in range(N8)) - (8 - 2 * k) * Lsc[k]) == 0,
          f"sum_h P_({k})^h_h = (8 - {2 * k}) L_({k}); L_({k}) = {sp.expand(Lsc[k])}")
    off_ok = all(P[k][h][j] == 0 for h in range(N8) for j in range(N8) if h != j)
    grp_ok = P[k][1][1] == P[k][2][2] == P[k][3][3] and P[k][0][0] == P[k][5][5] == P[k][6][6] == P[k][7][7]
    check(f"P{k}_structure", off_ok and grp_ok,
          f"P_({k}) is diagonal (all 56 off-diagonal components vanish) with x1 = x2 = x3 and x0 = x5 = x6 = x7, a polynomial in H, a4', a4'', u, v, k")

# compare with the GKD branch's monomial lists (14 exponents: H, a4', a4'', a4''', a4'''', E = e^{a4}, W = (sin^2 z)^(1/12),
# C = cot z, Q = b4^(1/2), b4', b4'', b4''', b4'''', G = sign(cot z)), in the ring of this file: b4^(n)/b4 written through
# u, v, w, w5
B4D = [uu * Bq**2, (vv + uu**2) * Bq**2, (ww + 3 * uu * vv + uu**3) * Bq**2,
       (w5 + 4 * uu * ww + 3 * vv**2 + 6 * uu**2 * vv + uu**4) * Bq**2]
Gsg = sp.Symbol("Gsg")
MONO_VARS = (H, ad1, ad2, ad3, ad4, Ee, Ww, Cc, Bq) + tuple(B4D) + (Gsg,)
lj = None
if LOVELOCK_JSON.exists():
    lj = json.loads(LOVELOCK_JSON.read_text(encoding="utf-8"))

    def from_monomials(mons):
        e = sp.Integer(0)
        for num, den, ex in mons:
            if len(ex) != 14:
                raise SystemExit("ERROR  a monomial of lovelock-tensors.json does not have 14 exponents (format since 2026-10-16)")
            t = sp.Rational(num, den)
            for v, n in zip(MONO_VARS, ex):
                t *= v**n
            e += t
        return sp.expand(e)

    a4x = sp.Symbol("a4x")
    for k in (1, 2, 3):
        key = f"P{k}_mixed_up_h_down_j"
        ok = True
        no_extra = True
        for h in range(N8):
            for j in range(N8):
                e = from_monomials(lj[key][f"{COORDS[h]},{COORDS[j]}"]["monomials"])
                if e.has(Ww) or e.has(Cc) or e.has(Gsg) or e.has(ad3) or e.has(ad4) or e.has(ww) or e.has(w5):
                    no_extra = False
                if sp.expand(to_uvk(e) - P[k][h][j]) != 0:
                    ok = False
        check(f"P{k}_equals_gkd_branch_monomials", ok and no_extra,
              f"all 64 components of P_({k}) computed here equal Revision/gkd_lovelock/results/lovelock-tensors.json ({key}) for general a4, b4 (b4^(n) written as b4 times polynomials in u = b4'/b4 and its derivatives); no x0 dependence or higher derivatives remain")
        Lstr = lj[f"L{k}"]
        Lstr = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"ad\1", Lstr)
        Lstr = re.sub(r"Derivative\[(\d)\]\[b4\]\[x4\]", r"bder\1", Lstr)
        Lstr = Lstr.replace("b4[x4]", "bq2").replace("a4[x4]", "a4x").replace("^", "**")
        bloc = {"ad1": ad1, "ad2": ad2, "ad3": ad3, "ad4": ad4, "H": H, "bq2": Bq**2, "a4x": a4x, "E": sp.E,
                "bder1": B4D[0], "bder2": B4D[1], "bder3": B4D[2], "bder4": B4D[3]}
        Ls = sp.sympify(Lstr, locals=bloc).subs(a4x, sp.log(Ee))
        check(f"L{k}_equals_gkd_branch", sp.expand(to_uvk(Ls) - Lsc[k]) == 0, f"L_({k}) = {sp.expand(Lsc[k])}")
else:
    check("gkd_branch_monomials", False, "Revision/gkd_lovelock/results/lovelock-tensors.json missing", pending=True)

E = {k: [[sp.expand(-P[k][h][j] / 2 ** (k + 1)) for j in range(N8)] for h in range(N8)] for k in (1, 2, 3)}
FROM_UVK = {uu: uu, vv: vv, kk: Ee**2 / Bq**2}  # u, v are already ring symbols with derivation rules


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
    Ek_sym = [[E[k][h][j].subs(kk, Ee**2 / Bq**2) for j in range(N8)] for h in range(N8)]
    check(f"E{k}_divergence_free", all(x == 0 for x in divergence(Ek_sym)),
          f"nabla_mu E_({k})^mu_nu = 0 for nu = x0..x7 (Christoffel symbols of this file; general a4 and b4, every real z)")

# ----------------------------------------------------------------------------------------------
# field equations
# ----------------------------------------------------------------------------------------------
al = {1: alpha1, 2: alpha2, 3: alpha3}
LHS = [[sp.expand(sum(al[k] * E[k][h][j] for k in (1, 2, 3)) + (Lam if h == j else 0)) for j in range(N8)] for h in range(N8)]
e11, e44, e00 = (sp.expand(LHS[i][i] - Lam) for i in (1, 4, 0))  # x1, x4, x0
check("independent_components",
      all(LHS[h][j] == 0 for h in range(N8) for j in range(N8) if h != j) and
      LHS[1][1] == LHS[2][2] == LHS[3][3] and LHS[0][0] == LHS[5][5] == LHS[6][6] == LHS[7][7],
      "every off-diagonal left-hand side is 0; x1 = x2 = x3 and x0 = x5 = x6 = x7: the field equations need T^mu_nu = 0 for mu != nu and p0 = p_t")
J = sp.Matrix([[sp.diff(e11, ad2), sp.diff(e11, vv)], [sp.diff(e00, ad2), sp.diff(e00, vv)]]).applyfunc(sp.expand)
lin_ok = all(not x.has(ad2) and not x.has(vv) for x in J) and \
    sp.expand(e11 - J[0, 0] * ad2 - J[0, 1] * vv - e11.subs({ad2: 0, vv: 0})) == 0 and \
    sp.expand(e00 - J[1, 0] * ad2 - J[1, 1] * vv - e00.subs({ad2: 0, vv: 0})) == 0
detJ = sp.factor(J.det())
ein = {alpha1: 1, alpha2: 0, alpha3: 0}
check("second_order_system", lin_ok and detJ != 0 and J.subs(ein) == sp.Matrix([[2, -2], [0, sp.Rational(-3, 2)]]),
      f"the x1 and x0 components are linear in (a4'', v), v = (b4'/b4)', with Jacobian J, det J = {detJ} (not identically zero; Einstein J = [[2, -2], [0, -3/2]])")
check("constraint_first_order", not e44.has(ad2) and not e44.has(vv),
      "the x4 component contains a4', u and k but no a4'' and no v")
hh = uu / 2 - ad1


def d4uvk(e):
    return sp.expand(sp.diff(e, ad1) * ad2 + sp.diff(e, ad2) * ad3 + sp.diff(e, uu) * vv + sp.diff(e, vv) * ww
                     + sp.diff(e, kk) * kk * (2 * ad1 - uu))


check("bianchi_x4",
      sp.expand(d4uvk(e44) - 3 * ad1 * (e11 - e44) - 4 * hh * (e00 - e44)) == 0,
      "d/dx4 sum_k alpha_k E^x4_x4 = 3 a4' (E^x1_x1 - E^x4_x4) + 4 h4 (E^x0_x0 - E^x4_x4) identically, h4 = u/2 - a4', k' = k (2 a4' - u)")

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
Tn = 1 / Cc  # tan z
exp_x4 = -d4r - 3 * ad1 * (rho + p3) - 3 * hh * (rho + pt) - hh * (rho + p0) + d0q04 - 3 * H * (Cc + 2 * Tn) * q04
exp_x0 = d0p0 + 3 * H * Cc * (p0 - pt) + d4q40 + sp.Rational(3, 2) * uu * q40 - hh * Cc**2 * q04 * Bq**2 / Ee**2
check("conservation_components",
      all(divT[i] == 0 for i in (1, 2, 3, 5, 6, 7)) and norm(divT[4] - exp_x4) == 0 and norm(divT[0] - exp_x0) == 0,
      "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0) + d0 q04 - 3 H (cot z + 2 tan z) q04; "
      "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t) + d4 q40 + (3/2) u q40 - h4 cot^2 z q04/k")

# the independent sympy record of the corrected metric
mw = json.loads(MW_JSON.read_text(encoding="utf-8")) if MW_JSON.exists() else None
if mw is not None:
    EA, bbs, bd1s, bd2s = sp.symbols("EA bb bd1 bd2")
    mwloc = {"EA": EA, "H": H, "ad1": ad1, "ad2": ad2, "bb": bbs, "bd1": bd1s, "bd2": bd2s}
    mwE = {k: sp.expand(sp.cancel(sp.sympify(v, locals=mwloc).subs({EA: sp.sqrt(kk * bbs), bd1s: uu * bbs, bd2s: (vv + uu**2) * bbs})))
           for k, v in mw["einstein_diagonal"].items()}
    check("einstein_equals_metric_warped_record",
          set(mwE) == {"x0", "x1", "x4", "x5"} and all(sp.expand(mwE[c] - E[1][i][i]) == 0 for c, i in (("x0", 0), ("x1", 1), ("x4", 4), ("x5", 5))),
          "G = E_(1) computed here equals Revision/metric_warped/results/warped-metric.json (einstein_diagonal: x0, x1, x4, x5)")
else:
    check("einstein_equals_metric_warped_record", False, "Revision/metric_warped/results/warped-metric.json missing", pending=True)

check("einstein_components",
      sp.expand(e44.subs(ein) - (6 * H**2 * kk + 3 * ad1**2 - sp.Rational(3, 2) * uu**2)) == 0 and
      sp.expand(e11.subs(ein) - (2 * ad2 - 5 * ad1**2 + 6 * H**2 * kk + 6 * ad1 * uu - sp.Rational(5, 2) * uu**2 - 2 * vv)) == 0 and
      sp.expand(e00.subs(ein) - (3 * H**2 * kk - 3 * ad1**2 + sp.Rational(3, 2) * ad1 * uu - sp.Rational(3, 2) * uu**2 - sp.Rational(3, 2) * vv)) == 0,
      "Einstein: G^x4_x4 = 6 H^2 k + 3 a4'^2 - (3/2) u^2, G^x1_x1 = 2 a4'' - 5 a4'^2 + 6 H^2 k + 6 a4' u - (5/2) u^2 - 2 v, "
      "G^x0_x0 = G^x5_x5 = 3 H^2 k - 3 a4'^2 + (3/2) a4' u - (3/2) u^2 - (3/2) v")
nec0 = sp.expand(e00 - e44)
nec3 = sp.expand(e11 - e44)
check("einstein_null_combinations",
      sp.expand(nec0.subs(ein) + sp.Rational(3, 2) * (2 * H**2 * kk + 4 * ad1**2 - ad1 * uu + vv)) == 0 and
      sp.expand(nec3.subs(ein) - (2 * ad2 - 8 * ad1**2 + 6 * ad1 * uu - uu**2 - 2 * vv)) == 0,
      "Einstein: kappa (rho + p0) = -(3/2)(2 H^2 k + 4 a4'^2 - a4' u + v), kappa (rho + p3) = 2 a4'' - 8 a4'^2 + 6 a4' u - u^2 - 2 v")
check("einstein_flat_vacuum",
      all(sp.simplify(x.subs(ein).subs(flat)) == 0 for x in (e44, e11, e00)),
      "Einstein: a4 = 0, b4 = H^2 (x4 - c)^2 solves the vacuum equations with Lambda = 0")
# exponential histories a4 = A H x4 + a0, b4 = b4(0) e^{beta A H x4}: u = beta A H, v = 0, k = k0 e^{(2 - beta) A H x4}
hist = {ad1: AA * H, ad2: 0, uu: be * AA * H, vv: 0}
h11, h44, h00 = (sp.expand(x.subs(hist)) for x in (e11, e44, e00))
ein_d1 = sp.factor(sp.expand((h44 - h11).subs(ein)))
ein_d2 = sp.expand((h44 - h00).subs(ein))
kk_sol = sp.solve(ein_d2, kk)
check("einstein_no_exponential_vacuum",
      sp.expand(ein_d1 - AA**2 * H**2 * (be - 2) * (be - 4)) == 0 and len(kk_sol) == 1 and sp.expand(kk_sol[0] - AA**2 * (be - 4) / 2) == 0,
      "Einstein, exponential histories: the vacuum equations give (x4 - x1) A^2 H^2 (beta - 2)(beta - 4) = 0 and (x4 - x0) k = A^2 (beta - 4)/2: "
      "beta = 4 gives k = 0, beta = 2 gives k = -A^2, A = 0 gives k = 0: no solution with k > 0 for any Lambda")
check("exponential_history_required_source",
      all(sp.Poly(x, kk).degree() <= 2 for x in (h11, h44, h00)) and sp.expand(sp.Poly(h44.subs(ein), kk).coeff_monomial(kk) - 6 * H**2) == 0,
      "on a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) the required rho, p3, p0 = p_t are polynomials of degree <= 2 in k = k0 e^((2 - beta) A H x4): constant only for beta = 2 or A = 0")
authW = {alpha1: 1 / H**2, alpha2: sp.Rational(1, 32) / H**4, alpha3: sp.Rational(1, 1152) / H**6, Lam: -10}
rec = {AA: 1, be: sp.Rational(4, 3)}
auth_hist = [sp.expand(x.subs(authW).subs(rec)) for x in (h44, h11, h00)]
ein_hist = [sp.expand(x.subs(ein).subs(rec)) for x in (h44, h11, h00)]
if mw is not None:
    x4s = sp.Symbol("x4")

    def mw_hist(s):
        e = sp.sympify(s, locals={"H": H, "x4": x4s})
        return sp.expand(sp.simplify(e.subs(sp.exp(2 * H * x4s / 3), kk).subs(sp.exp(4 * H * x4s / 3), kk**2)))

    ha = mw["history_source"]["author_weights_A1_beta43"]
    he = mw["history_source"]["einstein_A1_beta43"]
    ok = [mw_hist(ha["-rho"]), mw_hist(ha["p3"]), mw_hist(ha["p0"])] == auth_hist and mw_hist(ha["p_t"]) == auth_hist[2] and \
        [mw_hist(he["-rho"]), mw_hist(he["p3"]), mw_hist(he["p0"])] == ein_hist
    check("author_weights_history_source", ok,
          f"the record's history a4 = H x4, b4 = e^((4/3) H x4) (k = e^((2/3) H x4)) with the author's weights: kappa T - Lam = "
          f"(-rho: {auth_hist[0]}, p3: {auth_hist[1]}, p0 = p_t: {auth_hist[2]}); Einstein {ein_hist}: equal to Revision/metric_warped/results/warped-metric.json (history_source)")
else:
    check("author_weights_history_source", False, "warped-metric.json missing", pending=True)


def numer(e):
    return sp.expand(sp.fraction(sp.cancel(sp.together(e)))[0])


def no_real_solution(polys, gens):
    """True if the polynomial system has no real solution: some element of a lex Groebner basis is a nonzero constant,
    or a univariate element (in the last generator) has no real root."""
    gb = sp.groebner(polys, *gens, order="lex")
    if list(gb) == [1]:
        return True
    for g in gb:
        if g.free_symbols <= {gens[-1]} and g.free_symbols:
            if sp.Poly(g, gens[-1]).count_roots() == 0:
                return True
    return False


vac_auth = [numer(x.subs(authW)) for x in (h44 + Lam, h11 + Lam, h00 + Lam)]
co_auth = [c for x in vac_auth for c in sp.Poly(x, kk).all_coeffs()]
Hn = sp.Integer(1)  # H scales out of the author's-weights system (alpha_k H^(2k) fixed): set H = 1
vac_b2 = [numer(x.subs({be: 2, H: 1})) for x in vac_auth]
vac_a0 = [numer(x.subs({AA: 0, H: 1})) for x in vac_auth]
sols_b2 = sp.solve(vac_b2, [AA, kk], dict=True)
real_b2 = [s for s in sols_b2 if all(v.is_real for v in s.values()) and s.get(kk, -1) > 0] if sols_b2 else []
sols_a0 = sp.solve(vac_a0, [kk], dict=True)
real_a0 = [s for s in sols_a0 if s[kk].is_real and s[kk] > 0]
check("author_weights_no_exponential_vacuum",
      no_real_solution([numer(c.subs(H, 1)) for c in co_auth if c != 0], [be, AA]) and not real_b2 and not real_a0,
      "the author's weights: no exponential history is a vacuum solution (where k varies every coefficient of k^0, k^1, k^2 must vanish: no real solution; "
      "for constant k > 0, beta = 2 or A = 0: no real solution)")
egb = {alpha1: 1, alpha3: 0}
vac_egb = [sp.expand(x.subs(egb)) for x in (h44 + Lam, h11 + Lam, h00 + Lam)]
co_egb = [c for x in vac_egb for c in sp.Poly(x, kk).all_coeffs()]
# beta = 2 (constant k): linear in (alpha2, Lam)
lin = [x.subs(be, 2) for x in vac_egb]
# the x4 and x1 equations have the same coefficients of (alpha2, Lambda) at beta = 2; the x4 and x0 equations determine them
sol_l = sp.solve([lin[0], lin[2]], [alpha2, Lam], dict=True)
br_ok = len(sol_l) == 1 and sp.simplify(sol_l[0][alpha2] + 1 / (4 * H**2 * (AA**2 - kk))) == 0 and sp.simplify(lin[1].subs(sol_l[0])) == 0
coef_mat = sp.Matrix([[sp.diff(x, alpha2), sp.diff(x, Lam)] for x in (lin[0], lin[2])])
sing = sp.factor(coef_mat.det())
check("egb_exponential_vacuum_branches",
      br_ok and sing != 0 and sp.simplify(sing.subs(kk, AA**2)) == 0,
      f"Einstein-Gauss-Bonnet (alpha1 = 1, alpha3 = 0): for constant k (beta = 2) the x4 and x0 equations determine alpha2 = -1/(4 H^2 (A^2 - k)) and Lambda "
      f"(coefficient determinant {sing}, zero only at k = A^2), and the x1 equation then holds identically: a vacuum exponential history for these tuned couplings")
# where k varies, each coefficient of k^0, k^1, k^2 must vanish: no solution with H != 0 (alpha2 and Lambda free)
tq = sp.Symbol("tq")
co_vary = [numer(c) for c in co_egb if c != 0]
gb_vary = sp.groebner(co_vary + [tq * H - 1], tq, Lam, alpha2, be, AA, H, order="lex")
check("egb_no_vacuum_where_k_varies", list(gb_vary) == [1],
      "Einstein-Gauss-Bonnet: where k varies every coefficient of k^0, k^1, k^2 in the three vacuum equations must vanish: no solution with H != 0 (Groebner basis [1], alpha2 and Lambda free)")

# ----------------------------------------------------------------------------------------------
# comparison with a4-equations.json (the Wolfram output)
# ----------------------------------------------------------------------------------------------
bb, bd1 = sp.symbols("bb bd1")
hhs = sp.Symbol("hh")
LOC = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam,
       "kappa": kappa, "AA": AA, "be": be, "rho": rho, "p3": p3, "pt": pt, "p0": p0, "q40": q40, "q04": q04, "cc": Cc, "tt": 1 / Cc,
       "uu": uu, "vv": vv, "kk": kk, "bb": bb, "bd1": bd1,
       **{v.name: v for v in D4SRC.values()}, **{v.name: v for v in D0SRC.values()}}


def parse(s: str):
    s = s.replace("Sqrt[", "sqrt(").replace("]", ")").replace("{", "[").replace("}", "]").replace("^", "**")
    e = sp.sympify(s, locals=LOC)
    return e.subs(bd1, uu * bb) if not isinstance(e, list) else e


def parse_eq(s: str):
    l, r = s.split(" == ")
    return sp.expand(parse(l) - parse(r))


aj = None
if A4_JSON.exists():
    aj = json.loads(A4_JSON.read_text(encoding="utf-8"))
    ok = True
    for k in (1, 2, 3):
        comp = aj["lovelockTensors"][f"E{k}"]
        for key, (h, j) in {"x0x0": (0, 0), "x1x1": (1, 1), "x4x4": (4, 4), "x5x5": (5, 5)}.items():
            if sp.expand(parse(comp[key]["input"]) - E[k][h][j]) != 0:
                ok = False
    check("json_lovelock_components", ok, "E_(1..3) components x0x0, x1x1, x4x4, x5x5 in a4-equations.json (in u = b4'/b4, v = u', k = e^(2a4)/b4) equal this file's")
    gs = aj["generalSource"]
    mine = {
        "constraint_x4": e44 + Lam + kappa * rho, "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
        "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7": e00 + Lam - kappa * p0,
    }
    ok = all(sp.expand(parse_eq(gs[k]["input"]) - v) == 0 for k, v in mine.items())
    Jw = sp.Matrix(parse(gs["secondOrderJacobian"]["input"]))
    ok = ok and (Jw - J).applyfunc(sp.expand) == sp.zeros(2, 2) and sp.cancel(parse(gs["secondOrderJacobianDet"]["input"]) - detJ) == 0
    check("json_general_source_equations", ok,
          "constraint, x1 and x0 (= x5) components and the Jacobian with its determinant in a4-equations.json equal this file's")
    src = gs["sourceRequiredByGivenHistory"]
    ok = (sp.cancel(parse(src["rho"]["input"]) + (e44 + Lam) / kappa) == 0 and sp.cancel(parse(src["p3"]["input"]) - (e11 + Lam) / kappa) == 0
          and sp.cancel(parse(src["pt"]["input"]) - (e00 + Lam) / kappa) == 0 and sp.cancel(parse(src["p0"]["input"]) - (e00 + Lam) / kappa) == 0)
    nc = gs["nullCombinations"]
    ok = ok and sp.expand(parse(nc["kappa(rho+p0)"]["input"]) - nec0) == 0 and sp.expand(parse(nc["kappa(rho+p3)"]["input"]) - nec3) == 0
    check("json_required_source_and_null_combinations", ok, "sourceRequiredByGivenHistory (p0 = p_t) and nullCombinations equal this file's")
    cx4 = parse_eq(gs["conservation_x4"]["input"])
    cx0 = parse_eq(gs["conservation_x0"]["input"]).subs(kk, Ee**2 / Bq**2)
    ex_ok = sp.expand(parse_eq(gs["energyExchange"]["input"]) - (-d4r - 3 * ad1 * (rho + p3) - 4 * hh * (rho + p0))) == 0
    check("json_conservation", sp.cancel(cx4 - exp_x4) == 0 and sp.cancel(cx0 - exp_x0) == 0 and ex_ok,
          "conservation_x4, conservation_x0 and energyExchange (p0 = p_t, no off-diagonal source) in a4-equations.json equal this file's covariant divergence")
    ei = aj["einstein"]
    jE = sp.Matrix(parse(ei["secondOrderJacobian"]["input"]))
    ok = (sp.expand(parse_eq(ei["constraint_x4"]["input"]) - (e44.subs(ein) + Lam + kappa * rho)) == 0
          and sp.expand(parse_eq(ei["space_x1"]["input"]) - (e11.subs(ein) + Lam - kappa * p3)) == 0
          and sp.expand(parse_eq(ei["hidden_x0"]["input"]) - (e00.subs(ein) + Lam - kappa * p0)) == 0
          and sp.expand(parse_eq(ei["nullEnergy_x0"]["input"]) - (kappa * (rho + p0) - nec0.subs(ein))) == 0
          and sp.expand(parse_eq(ei["nullEnergy_x1"]["input"]) - (kappa * (rho + p3) - nec3.subs(ein))) == 0
          and (jE - sp.Matrix([[2, -2 / bb], [0, -sp.Rational(3, 2) / bb]])).applyfunc(sp.cancel) == sp.zeros(2, 2))
    check("json_einstein", ok, "the Einstein special case in a4-equations.json (components, null combinations, Jacobian in (a4'', b4'')) equals this file's")
    eh = aj["exponentialHistory"]["requiredSource"]
    ok = (sp.simplify(parse(eh["rho"]["input"]) + (h44 + Lam) / kappa) == 0 and sp.simplify(parse(eh["p3"]["input"]) - (h11 + Lam) / kappa) == 0
          and sp.simplify(parse(eh["p0"]["input"]) - (h00 + Lam) / kappa) == 0 and sp.simplify(parse(eh["pt"]["input"]) - (h00 + Lam) / kappa) == 0)
    aw = aj["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
    ok = ok and [sp.expand(parse(aw[k]["input"])) for k in ("minus_rho", "p3", "p0")] == auth_hist and sp.expand(parse(aw["pt"]["input"])) == auth_hist[2]
    check("json_exponential_history", ok, "rho, p3, p0 = p_t of the exponential history and the author's-weights history source in a4-equations.json equal this file's")
else:
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
    return [e4, e1, e2, e3, f1, f2, f3, f4]  # x0, x1, ..., x7


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
CG = sp.Rational(3, 2) * H * Ee / Bq   # gamma^mu Omega_mu = CG gamma^x0 + VG gamma^x4
VG = uu - ad1 / 2
EXP_TRIPLES = {(0, i, 4) for i in (1, 2, 3)} | {(0, i, t) for i in (1, 2, 3) for t in (5, 6, 7)} | \
    {(i, 4, t) for i in (1, 2, 3) for t in (5, 6, 7)} | {(0, 4, t) for t in (5, 6, 7)}


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
    om0 = (Om[0] - sp.Rational(1, 2) * (Bq * Cc / Ee) * hh * gF[0] * gF[4]).applyfunc(norm)
    lcheck(f"{label}_Omega_x4_zero_Omega_x0", Om[4] == Z16 and om0 == Z16,
           "Omega_x4 = 0 and Omega_x0 = (1/2) cot z e^{-a4} b4^{1/2} h4 gamma^x0 gamma^x4 (h4 = u/2 - a4')")
    lcheck(f"{label}_anticommutator_no_sum",
           all((gC[m] * Om[m] + Om[m] * gC[m]).applyfunc(norm) == Z16 for m in range(8)),
           "{gamma^mu, Omega_mu} = 0 for each mu (no sum)")
    Gd = sum((gC[m] * Om[m] for m in range(8)), Z16).applyfunc(norm)
    lcheck(f"{label}_gravity_term", (Gd - CG * gF[0] - VG * gF[4]).applyfunc(norm) == Z16,
           "gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^x0 + (b4'/b4 - a4'/2) gamma^x4")
    A = (-gC[4] * (MM * I16 - Gd)).applyfunc(norm)
    Bm = (-MM * gF[4] + CG * gF[4] * gF[0]).applyfunc(norm)
    lcheck(f"{label}_condensate_equation",
           (A - Bm + VG * I16).applyfunc(norm) == Z16 and (Bm * Bm - (CG**2 - MM**2) * I16).applyfunc(norm) == Z16
           and not any(x.has(Cc) or x.has(Ww) for x in A),
           "d4 Phi = A Phi with A = B - (u - a4'/2) I16, B = -M gamma^x4 + (3/2) H e^{a4} b4^{-1/2} gamma^x4 gamma^x0, B^2 = (c^2 - M^2) I16, free of x0")
    lcheck(f"{label}_condensate_S_law",
           (C * A + A.T * C + 2 * VG * C).applyfunc(norm) == Z16,
           "C A + A^T C = -2 (u - a4'/2) C: S = e^{a4} b4^{-2} S0")
    adj = (A.T * C * gC[4] - C * sum((Om[m] * gC[m] for m in range(8)), Z16) + MM * C).applyfunc(norm)
    lcheck(f"{label}_condensate_adjoint", adj == Z16, "(D_mu Phibar) gamma^mu = -M Phibar for the condensate")

    def dphi(nu):
        return (A if nu == 4 else Z16) + Om[nu]

    def dphibar(nu):
        return (A.T * C if nu == 4 else Z16) - C * Om[nu]

    Nm = [[((C * gC[m] * dphi(n) - dphibar(n) * gC[m]) / 2) for n in range(8)] for m in range(8)]
    Ns = [[((Nm[m][n] + (gdiag[n] / gdiag[m]) * Nm[n][m]) / 2).applyfunc(norm) for n in range(8)] for m in range(8)]
    diag_ok = Ns[4][0] == Z16 and Ns[0][4] == Z16 and all(Ns[m][m] == Z16 for m in (0, 1, 2, 3, 5, 6, 7)) and \
        (Ns[4][4] - MM * C).applyfunc(norm) == Z16
    lcheck(f"{label}_condensate_kinetic_diagonal", diag_ok, "K^x4_x4 = M S, K^mu_mu = 0 otherwise, K^x4_x0 = K^x0_x4 = 0")
    # decompose every nonzero off-diagonal component in the basis C gamma^a gamma^b gamma^c (trace projection)
    basis = {t: C * gF[t[0]] * gF[t[1]] * gF[t[2]] for t in itertools.combinations(range(8), 3)}
    binv = {t: B.inv() for t, B in basis.items()}
    coeffs = {}
    ok = True
    for m in range(8):
        for n in range(8):
            if m == n or Ns[m][n] == Z16:
                continue
            dec = {}
            for t, Bi in binv.items():
                X = norm((Bi * Ns[m][n]).trace() / 16)
                if X != 0:
                    dec[t] = X
            rec_ = sum((X * basis[t] for t, X in dec.items()), Z16)
            ok = ok and (rec_ - Ns[m][n]).applyfunc(norm) == Z16
            coeffs[(m, n)] = dec
    found = set().union(*[set(d) for d in coeffs.values()]) if coeffs else set()
    lcheck(f"{label}_condensate_offdiagonal_three_gamma", ok and found == EXP_TRIPLES,
           f"every nonzero off-diagonal kinetic component ({len(coeffs)} ordered pairs) is a combination of the 24 bilinears "
           "Phibar gamma^a gamma^b gamma^c Phi, {a,b,c} = {x0,i,x4}, {x0,i,t}, {i,x4,t}, {x0,x4,t} (i = x1..x3, t = x5..x7)")
    # exact witness on a history with constant k = k0 = 4 (b4 = e^{2 a4}/4, u = 2 a4') at (M, H) = (5, 1): c = 3, w = 4
    cval = sp.Rational(3, 2) * 2  # (3/2) H sqrt(k0)
    w = 4
    Bv = (-5 * gF[4] + cval * gF[4] * gF[0])

    def sector(e):
        stack = sp.Matrix.vstack(Bv + sp.I * w * I16, gF[1] * gF[5] - e * I16, gF[2] * gF[6] - e * I16, gF[3] * gF[7] - e * I16)
        return stack.nullspace()

    n1, n2 = sector(-1), sector(1)
    wit_ok = len(n1) == 1 and len(n2) == 1
    if wit_ok:
        v1, v2 = n1[0], n2[0]
        s = sp.expand((v1.H * C * v2)[0])
        ph = (v1 + sp.conjugate(s) * v2).applyfunc(sp.expand)
        Sval = sp.expand((ph.H * C * ph)[0])
        # Phi = e^{a4/2} b4^{-1} e^{-4 i x4} Phi0 on the history u = 2 a4', k = 4: d4 Phi = (a4'/2 - u - 4 i) Phi must equal A Phi
        hist_k = {uu: 2 * ad1, Ee: 2 * Bq, MM: 5, H: 1}
        lhs = ((ad1 / 2 - 2 * ad1) - sp.I * w) * ph
        rhs = A.subs(hist_k).applyfunc(norm) * ph
        wit_ok = (Bv * ph + sp.I * w * ph).applyfunc(sp.expand) == sp.zeros(16, 1) and (lhs - rhs).applyfunc(sp.expand) == sp.zeros(16, 1) \
            and Sval != 0 and sp.im(Sval) == 0
        for t in EXP_TRIPLES:
            wit_ok = wit_ok and sp.expand((ph.H * basis[t] * ph)[0]) == 0
    lcheck(f"{label}_condensate_witness", wit_ok,
           "exact witness on the histories with constant k = e^{2a4}/b4 = 4 (b4 = e^{2 a4}/4, any a4) at (M, H) = (5, 1): Phi = e^{a4/2} b4^{-1} e^{-4 i x4} Phi0, "
           "Phi0 = v1 + conj(v1^dagger C v2) v2 from the sectors gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1, +1 of B; it solves d4 Phi = A Phi; all 24 three-gamma bilinears vanish, e^{-a4} b4^2 S != 0 real")
    return coeffs


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
# (numerically, 40 digits, at three points of (a4, z, H, a4', b4, u))
if aj is not None:
    offj = aj["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    a4v, svs, cvs, wws = sp.symbols("a4v sv cv ww")
    loc2 = dict(LOC)
    loc2.update({"a4v": a4v, "sv": svs, "cv": cvs, "ww": wws})
    pts = [(sp.Rational(3, 7), sp.Rational(11, 10), sp.Rational(2, 5), sp.Rational(-4, 9), sp.Rational(7, 3), sp.Rational(1, 5)),
           (sp.Rational(-1, 3), sp.Rational(27, 10), sp.Rational(7, 4), sp.Rational(5, 2), sp.Rational(1, 4), sp.Rational(-3, 2)),
           (sp.Rational(2, 1), sp.Rational(-22, 10), sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(5, 2), sp.Rational(2, 3))]
    mpmath.mp.dps = 40
    ok = len(offj) == len(coeffs_author)
    for entry in offj:
        comp = entry["component"].split(" ")[0]  # K^x1_x4; the coordinate xk has index k
        mu = int(comp[3])
        nu = int(comp.split("_")[1][1])
        if (mu, nu) not in coeffs_author or len(entry["terms"]) != len(coeffs_author[(mu, nu)]):
            ok = False
            continue
        for term in entry["terms"]:
            names = term["bilinear"].replace("Phibar ", "").replace(" Phi", "").split(" ")
            tj = tuple(int(nm[-1]) for nm in names)
            if tj not in coeffs_author[(mu, nu)]:
                ok = False
                continue
            X = coeffs_author[(mu, nu)][tj]
            s = term["coefficient"]["input"].replace("Sqrt[", "sqrt(").replace("]", ")").replace("^", "**")
            Xj = sp.sympify(s, locals=loc2)
            for av, zv, hv, a1v, bv, uv in pts:
                vj = sp.N(Xj.subs({a4v: av, svs: sp.sin(zv), cvs: sp.cos(zv), wws: (sp.sin(zv) ** 2) ** sp.Rational(1, 12),
                                   H: hv, ad1: a1v, bb: bv, uu: uv}), 40)
                vm = sp.N(X.subs({Ee: sp.exp(av), Ww: (sp.sin(zv) ** 2) ** sp.Rational(1, 12), Cc: sp.cot(zv), H: hv, ad1: a1v,
                                  Bq: sp.sqrt(bv), uu: uv}), 40)
                if abs(vj - vm) > sp.Float("1e-30") * (1 + abs(vm)):
                    ok = False
    check("json_offdiagonal_coefficients", ok,
          "every off-diagonal kinetic coefficient of a4-equations.json equals this file's (the author's T16, the primary representation; same triples, value at three exact points (z = 1.1, 2.7, -2.2) to 40 digits)")
same = set(coeffs_author) == set(coeffs_own) and all(
    set(coeffs_author[k]) == set(coeffs_own[k]) and all(norm(coeffs_author[k][t] - coeffs_own[k][t]) == 0 for t in coeffs_own[k]) for k in coeffs_own)
check("offdiagonal_coefficients_representation_independent", same,
      "the author's T16 (primary) and the comparison representation built here give the same triples and the same coefficients")

# the condensate as a source (p3 = p_t = p0): sum_k alpha_k (E^x1_x1 - E^x0_x0) = 0 on the exponential histories
cond_e = numer((h11 - h00).subs(ein))
cond_a = numer((h11 - h00).subs(authW))
ce_coeffs = [c for c in sp.Poly(cond_e, kk).all_coeffs()]
ca_coeffs = [c for c in sp.Poly(cond_a, kk).all_coeffs()]
sol_a_b2 = [r for r in sp.solve(cond_a.subs({be: 2, H: 1}), kk) if sp.simplify(r + AA**2) != 0]  # the root k = -A^2 is not positive
sol_a_a0 = sp.solve(cond_a.subs({AA: 0, H: 1}), kk)
check("condensate_source_equal_pressures",
      sp.expand(sp.Poly(cond_e, kk).coeff_monomial(kk) - 3 * H**2) == 0 and sp.solve(cond_e.subs(be, 2), kk) == [-AA**2]
      and no_real_solution([numer(c.subs(H, 1)) for c in ca_coeffs if c != 0], [be, AA])
      and len(sol_a_b2) == 1 and sp.simplify(sol_a_b2[0] - (16 + 2 * AA**2) / (2 + AA**2)) == 0 and sol_a_a0 == [8],
      "p3 = p_t = p0 needs sum_k alpha_k (E^x1_x1 - E^x0_x0) = 0; exponential histories: Einstein (the k-coefficient is 3 H^2; at beta = 2, k = -A^2): no solution with k > 0; "
      "the author's weights: none where k varies, and for constant k exactly k0 = (16 + 2 A^2)/(2 + A^2) (beta = 2) and k0 = 8 (A = 0)")

t_total = time.time() - t_start

# ----------------------------------------------------------------------------------------------
# outputs
# ----------------------------------------------------------------------------------------------
npass = sum(1 for c in CHECKS if c["verdict"] == "PASS")
nfail = sum(1 for c in CHECKS if c["verdict"] == "FAIL")
npend = sum(1 for c in CHECKS if c["verdict"] == "pending")
report = {
    "producer": "Revision/field_equations_a4/python/check_field_equations_a4.py (sympy, exact)",
    "spec": "Revision/SPEC.md section 5 (the corrected metric of 2026-10-16, version 2; general a4 and b4, every real z)",
    "inputsChecked": ["Revision/gkd_lovelock/results/lovelock-tensors.json", "Revision/field_equations_a4/a4-equations.json",
                      "Revision/metric_warped/results/warped-metric.json",
                      "Revision/algebra/gammas.json (author's T16: the primary representation, required)"],
    "checkCount": len(CHECKS), "passCount": npass, "failCount": nfail, "pendingCount": npend,
    "verdict": "PASS" if nfail == 0 and npend == 0 else ("FAIL" if nfail else "PENDING"),
    "checks": CHECKS,
}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_bytes((json.dumps(report, indent=2) + "\n").encode("utf-8"))


def lx(e) -> str:
    s = sp.latex(e, symbol_names={ad1: "a_4'", ad2: "a_4''", alpha1: r"\alpha_1", alpha2: r"\alpha_2", alpha3: r"\alpha_3",
                                   Lam: r"\Lambda", AA: "A", be: r"\beta", uu: "u", vv: "v", kk: "k", p3: "p_3", pt: "p_t", p0: "p_0"})
    return s.replace("a_4'^{2}", "(a_4')^{2}").replace("a_4'^{4}", "(a_4')^{4}").replace("a_4'^{6}", "(a_4')^{6}")


lines = [
    "# Field equations for a4[x4] and b4[x4] (summary generated by check_field_equations_a4.py)",
    "",
    "Computed by Revision code from the corrected metric of `Revision/SPEC.md` section 1 (version 2, 2026-10-16), for",
    "general a4 and b4 and every real z = 6 H x0; every line below is an output of",
    "`Revision/field_equations_a4/python/check_field_equations_a4.py` (sympy), cross-checked against the Wolfram",
    "output `Revision/field_equations_a4/a4-equations.json`. Report: `reports/python-a4-report.json`.",
    "",
    "Field equations: $\\sum_{k=1}^{3}\\alpha_k E_{(k)}{}^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu = \\kappa T^\\mu{}_\\nu$,",
    "$E_{(k)} = -P_{(k)}/2^{k+1}$, $T = \\mathrm{diag}(p_0,p_3,p_3,p_3,-\\rho,p_t,p_t,p_t)$ (order x0..x7);",
    "$u = b_4'/b_4$, $v = u'$, $k = e^{2a_4}/b_4$.",
    "",
    "## Independent components (general Lovelock)",
    "",
    f"* constraint (x4): $ {lx(e44)} + \\Lambda = -\\kappa\\rho$",
    f"* 3-space (x1 = x2 = x3): $ {lx(e11)} + \\Lambda = \\kappa p_3$",
    f"* hidden direction and extra times (x0 = x5 = x6 = x7): $ {lx(e00)} + \\Lambda = \\kappa p_0 = \\kappa p_t$",
    "* every off-diagonal component: $0 = \\kappa T^\\mu{}_\\nu$; the hidden and extra-time pressures are equal, $p_0 = p_t$",
    "* the x1 and x0 components are linear in $(a_4'', v)$ and determine them where their Jacobian is nonsingular; the x4 component is the constraint",
    f"* energy exchange: $\\partial_4\\rho + 3a_4'(\\rho + p_3) + 4h_4(\\rho + p_0) = 0$, $h_4 = u/2 - a_4'$",
    "",
    "## Einstein gravity ($\\alpha_1 = 1$, $\\alpha_2 = \\alpha_3 = 0$)",
    "",
    f"* $ {lx(e44.subs(ein))} + \\Lambda = -\\kappa\\rho$, $ {lx(e11.subs(ein))} + \\Lambda = \\kappa p_3$, $ {lx(e00.subs(ein))} + \\Lambda = \\kappa p_0$",
    f"* $\\kappa(\\rho + p_0) = {lx(nec0.subs(ein))}$; the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ is a vacuum; no exponential history is a vacuum",
    "",
    "## Exponential histories $a_4 = A H x_4 + a_0$, $b_4 = b_4(0) e^{\\beta A H x_4}$ ($k = k_0 e^{(2 - \\beta) A H x_4}$)",
    "",
    f"* the author's weights, the record's history ($A = 1$, $\\beta = 4/3$, $k = e^{{2Hx_4/3}}$): $\\kappa T - \\Lambda$: $-\\kappa\\rho - \\Lambda = {lx(auth_hist[0])}$, "
    f"$\\kappa p_3 - \\Lambda = {lx(auth_hist[1])}$, $\\kappa p_0 - \\Lambda = \\kappa p_t - \\Lambda = {lx(auth_hist[2])}$ (a prescribed background, not a vacuum)",
    "* vacuum: none for Einstein and for the author's weights; Einstein-Gauss-Bonnet only for constant $k = k_0$ ($\\beta = 2$) with $\\alpha_2 = -1/(4H^2(A^2 - k_0))$",
    "",
    r"## Field sources (convention $T^\mu{}_\nu = \sigma_T(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu \mathcal{L})$, $\sigma_T = +1$ per SPEC section 4)",
    "",
    r"* lemmas: $\gamma^\mu\Omega_\mu = \tfrac32 H e^{a_4} b_4^{-1/2}\gamma^{x0} + (u - a_4'/2)\gamma^{x4}$; $\{\gamma^\mu,\Omega_\mu\}=0$ for each $\mu$ (no sum)",
    r"* dirac16complex00, homogeneous condensate $\Phi(x_4) = e^{a_4/2} b_4^{-1}\chi$: $S = e^{a_4} b_4^{-2} S_0$, $\rho = \sigma_T(mS+U)$, $p_3=p_t=p_0=\sigma_T(SU'-U)$;",
    r"  the off-diagonal equations need the 24 bilinears $\bar\Phi\gamma^a\gamma^b\gamma^c\Phi$ to vanish (exact witnesses for constant $k$);",
    r"  equal pressures on the exponential histories: none in Einstein gravity; the author's weights only for constant $k$",
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
