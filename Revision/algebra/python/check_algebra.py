#!/usr/bin/env python3
"""Revision algebra: independent exact Python construction and verification of the author's T16.

Revision/SPEC.md section 2.  This file is Revision code; it imports nothing from the old stages.
It re-constructs the author's real 16 x 16 gamma matrices T16 from the author's own formulas
(input cells of Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb,
read only, never modified):

  In[45]   eta4488 = diag(I4, -I4)                         (notebook frame order 0..7)
  In[46]   sigma   = {{0, I4}, {I4, 0}}
  In[294]  Qa[h,p,q] = Signature[{h,p,q,4}]
           Qb[h,p,q] = ID4[[p,4]] ID4[[q,h]] - ID4[[p,h]] ID4[[q,4]]
           SelfDualAntiSymmetric = Qa - Qb,  AntiSelfDualAntiSymmetric = Qa + Qb
  In[300]  s4by4[h] = Table[SelfDualAntiSymmetric[h,p,q], {p,4}, {q,4}],      h = 1..3
  In[301]  t4by4[h] = Table[AntiSelfDualAntiSymmetric[h,p,q], {p,4}, {q,4}],  h = 1..3
  In[338]  tau[0] = ID8; tau[7-h] = {{0, t4by4[h]}, {-t4by4[h], 0}};
           tau[h] = {{0, s4by4[h]}, {s4by4[h], 0}};  tau[7] = tau[1].tau[2]...tau[6]
  In[351]  taubar[0] = ID8; taubar[A] = sigma.Transpose[tau[A]].sigma  (A = 1..7)
  In[371]  T16A[A1] = {{0, taubar[A1]}, {tau[A1], 0}}  (A1 = 0..7)
  In[370]  sigma16 = T16A[0].T16A[1].T16A[2].T16A[3]
  In[372]  T16A[8] = T16A[0].T16A[1]...T16A[7]

and maps the notebook frame order (0 = hidden, 1-3 = 3-space, 4 = time, 5-7 = extra times) to the
author's coordinates x1..x8 (SPEC section 1-2): gamma^(x8) = T16[0], gamma^(x1..x3) = T16[1..3],
gamma^(x4) = T16[4], gamma^(x5..x7) = T16[5..7]; eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in x1..x8.

All arithmetic is exact: Python integers and fractions.Fraction (own Gaussian elimination), with
sympy (Matrix, DomainMatrix over QQ) as an independent second engine for the ranks, B and the
characteristic polynomials.

Outputs (deterministic, LF):
  Revision/algebra/reports/python-algebra.json  every check with name, verdict, detail
  Revision/algebra/reports/python-gammas.json   this construction's matrices (x1..x8 order)
The comparison with Revision/algebra/gammas.json (the Wolfram fixture) is done entry by entry
when that file exists; otherwise the check is recorded with verdict "pending".

Usage: python Revision/algebra/python/check_algebra.py
"""

from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ALGEBRA = HERE.parent
REPORTS = ALGEBRA / "reports"
FIXTURE = ALGEBRA / "gammas.json"
REPORT = REPORTS / "python-algebra.json"
OUR_GAMMAS = REPORTS / "python-gammas.json"

COORDS = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
# author's coordinate index (0..7 for x1..x8) -> notebook T16 index
COORD_TO_T16 = [1, 2, 3, 4, 5, 6, 7, 0]
ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # x1..x8, SPEC section 2


# --------------------------------------------------------------------------- exact matrix helpers
def zeros(n, m=None):
    m = n if m is None else m
    return [[0] * m for _ in range(n)]


def ident(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = zeros(n, m)
    for i in range(n):
        ai = a[i]
        oi = out[i]
        for t in range(k):
            x = ai[t]
            if x:
                bt = b[t]
                for j in range(m):
                    if bt[j]:
                        oi[j] += x * bt[j]
    return out


def mulall(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = mul(out, m)
    return out


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scal(c, a):
    return [[c * x for x in r] for r in a]


def tr(a):
    return [list(r) for r in zip(*a)]


def neg(a):
    return scal(-1, a)


def is_zero(a):
    return all(x == 0 for r in a for x in r)


def eq(a, b):
    return is_zero(sub(a, b))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def block(blocks):
    """ArrayFlatten of a 2 x 2 block list; 0 entries stand for zero blocks."""
    rs = [None, None]
    cs = [None, None]
    for i in range(2):
        for j in range(2):
            b = blocks[i][j]
            if b != 0:
                rs[i] = len(b)
                cs[j] = len(b[0])
    out = zeros(rs[0] + rs[1], cs[0] + cs[1])
    for i in range(2):
        for j in range(2):
            b = blocks[i][j]
            if b == 0:
                continue
            for r in range(rs[i]):
                for c in range(cs[j]):
                    out[r + (rs[0] if i else 0)][c + (cs[0] if j else 0)] = b[r][c]
    return out


def sub_block(a, r0, c0, n):
    return [row[c0:c0 + n] for row in a[r0:r0 + n]]


def diag(*vals):
    n = len(vals)
    return [[vals[i] if i == j else 0 for j in range(n)] for i in range(n)]


def anticomm(a, b):
    return add(mul(a, b), mul(b, a))


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


def signature(lst):
    """Mathematica Signature: sign of the permutation, 0 for a repeated entry."""
    if len(set(lst)) != len(lst):
        return 0
    inv = sum(1 for i in range(len(lst)) for j in range(i + 1, len(lst)) if lst[i] > lst[j])
    return -1 if inv % 2 else 1


# --------------------------------------------------------------------------- the author's construction
def kd(i, j):
    return 1 if i == j else 0


def Qa(h, p, q):
    return signature([h, p, q, 4])


def Qb(h, p, q):
    return kd(p, 4) * kd(q, h) - kd(p, h) * kd(q, 4)


def s4by4(h):
    return [[Qa(h, p, q) - Qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]


def t4by4(h):
    return [[Qa(h, p, q) + Qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]


def construct():
    I4, I8 = ident(4), ident(8)
    eta4488 = block([[I4, 0], [0, neg(I4)]])
    sigma = block([[zeros(4), I4], [I4, zeros(4)]])
    tau = {0: I8}
    for h in (1, 2, 3):
        tau[7 - h] = block([[zeros(4), t4by4(h)], [neg(t4by4(h)), zeros(4)]])
    for h in (1, 2, 3):
        tau[h] = block([[zeros(4), s4by4(h)], [s4by4(h), zeros(4)]])
    tau[7] = mulall(tau[1], tau[2], tau[3], tau[4], tau[5], tau[6])
    taubar = {0: I8}
    for A in range(1, 8):
        taubar[A] = mulall(sigma, tr(tau[A]), sigma)
    T16 = {A: block([[zeros(8), taubar[A]], [tau[A], zeros(8)]]) for A in range(8)}
    sigma16 = mulall(T16[0], T16[1], T16[2], T16[3])
    T16_8 = mulall(*[T16[A] for A in range(8)])
    return dict(eta4488=eta4488, sigma=sigma, tau=tau, taubar=taubar, T16=T16,
                sigma16=sigma16, T16_8=T16_8)


# --------------------------------------------------------------------------- exact linear algebra
def rank_fraction(rows, ncols):
    """Rank of a matrix given as a list of sparse dict rows {col: int}, exact (Fraction pivots)."""
    pivots = {}  # col -> normalized row (dict)
    rank = 0
    for row in rows:
        r = {c: Fraction(v) for c, v in row.items() if v}
        while r:
            c = min(r)
            if c in pivots:
                f = r[c]
                prow = pivots[c]
                for cc, vv in prow.items():
                    nv = r.get(cc, 0) - f * vv
                    if nv:
                        r[cc] = nv
                    else:
                        r.pop(cc, None)
            else:
                f = r[c]
                pivots[c] = {cc: vv / f for cc, vv in r.items()}
                rank += 1
                break
    return rank


def rank_sympy(rows, ncols):
    dense = [[row.get(c, 0) for c in range(ncols)] for row in rows]
    dm = DomainMatrix([[sympy.QQ(x) for x in r] for r in dense], (len(dense), ncols), sympy.QQ)
    return dm.rank()


def commutant_rows(mats_left, mats_right, n_left, n_right):
    """Rows of the linear system L X - X R = 0 for every pair (L, R); X is n_left x n_right."""
    rows = []
    for L, R in zip(mats_left, mats_right):
        for i in range(n_left):
            for j in range(n_right):
                row = {}
                for k in range(n_left):
                    if L[i][k]:
                        idx = k * n_right + j
                        row[idx] = row.get(idx, 0) + L[i][k]
                for k in range(n_right):
                    if R[k][j]:
                        idx = i * n_right + k
                        row[idx] = row.get(idx, 0) - R[k][j]
                row = {c: v for c, v in row.items() if v}
                if row:
                    rows.append(row)
    return rows


def solution_dim(mats_left, mats_right, n_left, n_right):
    rows = commutant_rows(mats_left, mats_right, n_left, n_right)
    n = n_left * n_right
    r1 = rank_fraction(rows, n)
    r2 = rank_sympy(rows, n)
    return n - r1, n - r2


def vec_rows(mats):
    return [{i * 16 + j: m[i][j] for i in range(16) for j in range(16) if m[i][j]} for m in mats]


# --------------------------------------------------------------------------- report helpers
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "pass" if ok else "fail", "detail": detail})
    return ok


def as_int(m):
    return [[int(x) for x in r] for r in m]


# --------------------------------------------------------------------------- comparison with the fixture
# The fixture's documented encoding (its "encoding" field): a matrix is a list of rows; an exact
# rational is a JSON integer, or a string "p/q" in lowest terms with q > 0; a complex matrix is
# {"re": ..., "im": ...}; indices 0..7 of gamma, eta and S stand for x1..x8.  Parsing is strict:
# anything else (floats, other keys) makes the comparison fail.
def _rat(x):
    if isinstance(x, bool) or isinstance(x, float):
        raise ValueError(f"non-exact entry {x!r}")
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str) and "/" in x:
        p, q = x.split("/")
        f = Fraction(int(p), int(q))
        if f.denominator == 1 or f"{f.numerator}/{f.denominator}" != x:
            raise ValueError(f"rational string not in lowest terms {x!r}")
        return f
    raise ValueError(f"unrecognized entry {x!r}")


def _real(obj, n=16):
    if not (isinstance(obj, list) and len(obj) == n and all(isinstance(r, list) and len(r) == n for r in obj)):
        raise ValueError("not a list of rows of the right size")
    return [[_rat(x) for x in r] for r in obj]


def _diffs(fm, om):
    return sum(1 for i in range(len(om)) for j in range(len(om)) if fm[i][j] != Fraction(om[i][j]))


def compare_fixture(ours):
    name = "fixture_comparison_gammas_json"
    if not FIXTURE.exists():
        CHECKS.append({"name": name, "verdict": "pending",
                       "detail": "PENDING: Revision/algebra/gammas.json does not exist at the time of this run; "
                                 "this construction's matrices are in Revision/algebra/reports/python-gammas.json "
                                 "for a later entry-by-entry comparison"})
        return "pending"
    fx = json.loads(FIXTURE.read_text(encoding="utf-8"))
    res = []

    def item(key, fn):
        try:
            ok, d = fn(fx[key])
        except Exception as exc:  # noqa: BLE001  (strict parsing: any deviation is a failure)
            ok, d = False, f"cannot read: {exc}"
        res.append((key, ok, d))

    item("coordinates", lambda v: (v == COORDS, f"{v}"))
    item("eta", lambda v: (v == ETA, f"{v}"))

    def cmp_gamma(v):
        if len(v) != 8:
            return False, f"{len(v)} matrices"
        d = [_diffs(_real(v[a]), ours["gamma"][a]) for a in range(8)]
        return sum(d) == 0, f"8 matrices x 256 entries, differing entries per x1..x8: {d}"

    item("gamma", cmp_gamma)
    item("C", lambda v: ((lambda d: (d == 0, f"256 entries, {d} differ"))(_diffs(_real(v), ours["C"]))))
    item("Gamma", lambda v: ((lambda d: (d == 0, f"256 entries, {d} differ"))(_diffs(_real(v), ours["Gamma"]))))

    def cmp_B(v):
        if set(v) != {"re", "im"}:
            raise ValueError(f"keys {sorted(v)}")
        d = _diffs(_real(v["re"]), zeros(16)) + _diffs(_real(v["im"]), ours["B_imag"])
        return d == 0, f"re and im parts, 512 entries, {d} differ"

    item("B", cmp_B)

    def cmp_S(v):
        if len(v) != 8 or any(len(r) != 8 for r in v):
            return False, "not an 8 x 8 array of matrices"
        d = sum(_diffs(_real(v[a][b]), ours["S"][(a, b)]) for a in range(8) for b in range(8))
        return d == 0, f"64 matrices S^ab (a, b = x1..x8) x 256 entries, {d} differ"

    item("S", cmp_S)
    allok = all(ok for _, ok, _ in res)
    detail = "entry-by-entry comparison with Revision/algebra/gammas.json (the Wolfram fixture): " + "; ".join(
        f"{k}: {'equal' if ok else 'DIFFERENT'} ({d})" for k, ok, d in res)
    check(name, allok, detail)
    return "pass" if allok else "fail"


# --------------------------------------------------------------------------- main
def main():
    t0 = time.perf_counter()
    nb = construct()
    T16, tau, taubar, sigma = nb["T16"], nb["tau"], nb["taubar"], nb["sigma"]
    I8, I16 = ident(8), ident(16)

    # ---- the author's 4 x 4 blocks equal the notebook's displayed output Out[304]
    out304_s = {
        1: [[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]],
        2: [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
        3: [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
    }
    out304_t = {
        1: [[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0]],
        2: [[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]],
        3: [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
    }
    ok = all(eq(s4by4(h), out304_s[h]) and eq(t4by4(h), out304_t[h]) for h in (1, 2, 3))
    check("notebook_blocks_s4_t4", ok,
          "s4by4[h], t4by4[h] (h = 1..3) rebuilt from Qa = Signature[{h,p,q,4}] and Qb (In[294], In[300], "
          "In[301]) equal the six matrices displayed in the notebook's Out[304]")
    ok = all(eq(tr(s4by4(h)), neg(s4by4(h))) and eq(tr(t4by4(h)), neg(t4by4(h))) for h in (1, 2, 3))
    ok = ok and all(eq(mul(s4by4(h), s4by4(h)), neg(ident(4))) and eq(mul(t4by4(h), t4by4(h)), neg(ident(4)))
                    for h in (1, 2, 3))
    ok = ok and all(is_zero(comm(s4by4(h), t4by4(k))) for h in (1, 2, 3) for k in (1, 2, 3))
    check("blocks_antisymmetric_square_minus_one_commute", ok,
          "every s4by4[h] and t4by4[h] is antisymmetric with square -I4, and every s4by4[h] commutes with every "
          "t4by4[k] (self-dual and anti-self-dual parts)")

    # ---- tau matrices: the notebook's own assertions
    eta4488 = nb["eta4488"]
    ok = eq(sigma, mulall(tau[1], tau[2], tau[3]))
    check("notebook_sigma_eq_tau1tau2tau3", ok, "sigma == tau[1].tau[2].tau[3] (notebook assertion)")
    bad = [(A, B) for A in range(1, 8) for B in range(1, 8)
           if not eq(anticomm(tau[A], tau[B]), scal(-2 * eta4488[A][B], I8))]
    check("notebook_tau_clifford", not bad,
          "tau[A].tau[B] + tau[B].tau[A] == -2 eta4488[[A+1,B+1]] ID8 for A, B = 1..7 (49 pairs)"
          + ("" if not bad else f"; failures {bad}"))
    ok = eq(tau[7], diag(-1, -1, -1, -1, 1, 1, 1, 1)) and eq(mulall(*[tau[A] for A in range(1, 8)]), I8)
    check("tau7_and_product", ok, "tau[7] = diag(-I4, I4) and tau[1]...tau[7] = ID8")
    ok = all(eq(mul(sigma, taubar[A]), tr(mul(sigma, tau[A]))) for A in range(8))
    ok = ok and all(eq(taubar[A], neg(tau[A])) for A in range(1, 8))
    check("taubar_relations", ok,
          "sigma.taubar[A] == Transpose[sigma.tau[A]] for A = 0..7 (notebook assertion) and taubar[A] = -tau[A] "
          "for A = 1..7")
    bad = [(A, B) for A in range(8) for B in range(8)
           if not eq(add(mul(tau[A], taubar[B]), mul(tau[B], taubar[A])), scal(2 * eta4488[A][B], I8))]
    check("notebook_tau_taubar_clifford", not bad,
          "tau[A].taubar[B] + tau[B].taubar[A] == 2 eta4488[[A+1,B+1]] ID8 for A, B = 0..7 (64 pairs)")

    # ---- map to the author's coordinates
    gamma = [T16[COORD_TO_T16[a]] for a in range(8)]
    check("coordinate_map", True,
          "gamma^(x1..x3) = T16[1..3], gamma^(x4) = T16[4], gamma^(x5..x7) = T16[5..7], gamma^(x8) = T16[0] "
          "(SPEC section 2); eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in x1..x8 is eta4488 with its index 0 moved last: "
          + str([eta4488[COORD_TO_T16[a]][COORD_TO_T16[a]] for a in range(8)] == ETA))
    CHECKS[-1]["verdict"] = "pass" if [eta4488[COORD_TO_T16[a]][COORD_TO_T16[a]] for a in range(8)] == ETA else "fail"

    # ---- Clifford relation (own integer arithmetic and sympy)
    bad = [(COORDS[a], COORDS[b]) for a in range(8) for b in range(8)
           if not eq(anticomm(gamma[a], gamma[b]), scal(2 * (ETA[a] if a == b else 0), I16))]
    check("clifford_relation", not bad,
          "{gamma^a, gamma^b} = 2 eta^ab I16 for all 64 ordered pairs a, b in x1..x8, eta = diag(+,+,+,-,-,-,-,+)"
          + ("" if not bad else f"; failures {bad}"))
    sg = [sympy.Matrix(g) for g in gamma]
    bad_s = [(a, b) for a in range(8) for b in range(a, 8)
             if sg[a] * sg[b] + sg[b] * sg[a] != 2 * (ETA[a] if a == b else 0) * sympy.eye(16)]
    check("clifford_relation_sympy", not bad_s,
          "the same 36 unordered relations re-evaluated with sympy.Matrix (second engine)")
    entries = sorted({x for g in gamma for r in g for x in r})
    ok = entries == [-1, 0, 1] and all(sum(1 for x in r if x) == 1 for g in gamma for r in g)
    check("reality_signed_permutations", ok,
          f"every gamma^a is real with integer entries {entries}; each is a signed permutation matrix "
          "(one nonzero entry per row)")
    sym = [COORDS[a] for a in range(8) if eq(tr(gamma[a]), gamma[a])]
    asym = [COORDS[a] for a in range(8) if eq(tr(gamma[a]), neg(gamma[a]))]
    ok = sym == ["x1", "x2", "x3", "x8"] and asym == ["x4", "x5", "x6", "x7"]
    check("symmetry_pattern", ok,
          f"symmetric: {sym} (the space-like directions); antisymmetric: {asym} (the time-like directions); "
          "hence gamma^a T = eta_aa gamma^a")

    # ---- C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
    C = mulall(gamma[7], gamma[0], gamma[1], gamma[2])
    ok = eq(C, nb["sigma16"]) and eq(C, block([[neg(sigma), zeros(8)], [zeros(8), sigma]]))
    check("C_equals_notebook_sigma16", ok,
          "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) equals the notebook's sigma16 = T16A[0..3] product "
          "(In[370]) and equals diag(-sigma, sigma) (notebook assertion)")
    ok = eq(tr(C), C) and eq(mul(C, C), I16)
    check("C_real_symmetric_involution", ok, "C is real (integer entries), C^T = C and C^2 = I16")
    bad = [COORDS[a] for a in range(8) if not eq(tr(mul(C, gamma[a])), neg(mul(C, gamma[a])))]
    check("C_gamma_antisymmetric", not bad,
          "C gamma^a is real antisymmetric for every a in x1..x8" + ("" if not bad else f"; failures {bad}"))
    ok2 =all(eq(mulall(C, gamma[a], C), neg(tr(gamma[a]))) for a in range(8))
    check("C_conjugation", ok2,
          "C gamma^a C^-1 = -(gamma^a)^T for all a (equivalent to C gamma^a antisymmetric with C symmetric); "
          "this makes Psibar Psi = Psi^dagger C Psi Pin(4,4)-invariant")

    # ---- chirality Gamma
    Gamma = mulall(*[T16[A] for A in range(8)])
    Gamma_coords = mulall(gamma[7], *[gamma[a] for a in range(7)])
    ok = eq(Gamma, Gamma_coords) and eq(Gamma, nb["T16_8"]) and eq(Gamma, block([[neg(I8), zeros(8)], [zeros(8), I8]]))
    check("chirality_diag", ok,
          "Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) (the notebook's product order T16A[0]...T16A[7], In[372]) "
          "= diag(-I8, I8)")
    ok = eq(mul(Gamma, Gamma), I16) and all(is_zero(anticomm(Gamma, gamma[a])) for a in range(8))
    check("chirality_anticommutes", ok, "Gamma^2 = I16 and Gamma anticommutes with every gamma^a")
    ok = eq(Gamma, mulall(C, gamma[3], gamma[4], gamma[5], gamma[6]))
    check("chirality_eq_C_times_time_gammas", ok,
          "Gamma = C gamma^(x4) gamma^(x5) gamma^(x6) gamma^(x7) (notebook assertion T16A[8] == sigma16.T16A[4..7])")
    ok = (eq(mul(C, Gamma), mul(Gamma, C)) and eq(tr(Gamma), Gamma) and eq(mulall(tr(Gamma), C, Gamma), C)
          and all(eq(mulall(tr(Gamma), C, gamma[a], Gamma), neg(mul(C, gamma[a]))) for a in range(8)))
    check("chirality_C_relation", ok,
          "C Gamma = Gamma C (C is a product of four gammas), Gamma^T = Gamma, Gamma^T C Gamma = C and "
          "Gamma^T C gamma^a Gamma = -C gamma^a for every a: under Psi -> Gamma Psi the bilinear Psibar Psi is "
          "unchanged and every Psibar gamma^a E Psi with E an even product of gammas changes sign (input for the pairing theorem T1)")

    # ---- B = -i C gamma^(x4)
    Cg4 = mul(C, gamma[3])
    B_imag = neg(Cg4)  # B = i * B_imag  (B = -i C gamma^(x4))
    # Hermitian: B^dagger = conj(B)^T = -i * B_imag^T ; equals B iff B_imag^T = -B_imag
    herm = eq(tr(B_imag), neg(B_imag))
    # B^2 = (i)^2 B_imag^2 = -B_imag^2
    sq = eq(neg(mul(B_imag, B_imag)), I16)
    trB = trace(B_imag)
    Bs = sympy.I * sympy.Matrix(B_imag)
    herm_s = Bs.H == Bs
    sq_s = Bs * Bs == sympy.eye(16)
    lam = sympy.Symbol("lam")
    cp = sympy.factor(Bs.charpoly(lam).as_expr())
    sig_ok = sympy.expand(cp - (lam - 1) ** 8 * (lam + 1) ** 8) == 0
    check("B_hermitian_involution_signature", herm and sq and trB == 0 and herm_s and sq_s and sig_ok,
          f"B = -i C gamma^(x4) is purely imaginary, Hermitian ({herm}, sympy {herm_s}), B^2 = I16 ({sq}, sympy "
          f"{sq_s}), tr B = {trB}; hence the eigenvalues are +1 and -1 with multiplicities 8 and 8: signature (8,8); "
          f"sympy characteristic polynomial = {cp}")
    # B gamma^a B^-1 with B = i Bi and B^-1 = B:  B g B = -Bi g Bi.  (B gamma^a)^dagger = gamma^a^T B (gamma real).
    commute = [COORDS[a] for a in range(8) if eq(neg(mulall(B_imag, gamma[a], B_imag)), gamma[a])]
    anticommute = [COORDS[a] for a in range(8) if eq(neg(mulall(B_imag, gamma[a], B_imag)), neg(gamma[a]))]
    hermitian = [COORDS[a] for a in range(8) if eq(neg(mulall(B_imag, gamma[a], B_imag)), tr(gamma[a]))]
    antihermitian = [COORDS[a] for a in range(8) if eq(neg(mulall(B_imag, gamma[a], B_imag)), neg(tr(gamma[a])))]
    ok = (commute == ["x1", "x2", "x3", "x4", "x8"] and anticommute == ["x5", "x6", "x7"]
          and hermitian == ["x1", "x2", "x3", "x5", "x6", "x7", "x8"] and antihermitian == ["x4"])
    check("B_gamma_relations", ok,
          f"B commutes with gamma^a for a in {commute} and anticommutes for a in {anticommute}; equivalently "
          f"B gamma^a is Hermitian for a in {hermitian} and anti-Hermitian for a in {antihermitian} "
          "(B gamma^(x4) = -i C is anti-Hermitian). Measured facts recorded for the quantisation work (SPEC "
          "section 6); no interpretation is attached here")

    # ---- S^ab = (1/4)[gamma^a, gamma^b]  (exact: entries in {0, +-1/2})
    S = {}
    for a in range(8):
        for b in range(8):
            S[(a, b)] = [[Fraction(x, 4) for x in r] for r in comm(gamma[a], gamma[b])]
    ok = all(eq(S[(a, b)], neg(S[(b, a)])) for a in range(8) for b in range(8))
    ok = ok and all(eq(S[(a, b)], scal(Fraction(1, 2), mul(gamma[a], gamma[b]))) for a in range(8)
                    for b in range(8) if a != b)
    vals = sorted({x for k in S for r in S[k] for x in r})
    check("S_definition", ok,
          f"S^ab = (1/4)[gamma^a, gamma^b] is antisymmetric in a, b and equals (1/2) gamma^a gamma^b for a != b; "
          f"28 independent real matrices, entries in {[str(v) for v in vals]}")

    def etaab(a, b):
        return ETA[a] if a == b else 0

    bad = 0
    for (a, b, c, d) in itertools.product(range(8), repeat=4):
        if a >= b or c >= d:
            continue
        lhs = comm(S[(a, b)], S[(c, d)])
        rhs = zeros(16)
        for coef, key in ((etaab(b, c), (a, d)), (-etaab(a, c), (b, d)),
                          (-etaab(b, d), (a, c)), (etaab(a, d), (b, c))):
            if coef:
                rhs = add(rhs, scal(coef, S[key]))
        if not eq(lhs, rhs):
            bad += 1
    check("S_lorentz_algebra", bad == 0,
          "[S^ab, S^cd] = eta^bc S^ad - eta^ac S^bd - eta^bd S^ac + eta^ad S^bc for all 28 x 28 pairs: "
          f"the Lie algebra so(4,4); failures {bad}")
    bad = 0
    for a, b, c in itertools.product(range(8), repeat=3):
        lhs = comm(S[(a, b)], gamma[c])
        rhs = sub(scal(etaab(b, c), gamma[a]), scal(etaab(a, c), gamma[b]))
        if not eq(lhs, rhs):
            bad += 1
    check("S_vector_action", bad == 0,
          f"[S^ab, gamma^c] = gamma^a eta^bc - gamma^b eta^ac for all 512 triples (gamma^c is a vector); failures {bad}")
    ok = all(eq(add(mul(tr(S[k]), C), mul(C, S[k])), zeros(16)) for k in S)
    ok = ok and all(is_zero(comm(Gamma, S[k])) for k in S)
    check("S_preserves_C_and_commutes_with_Gamma", ok,
          "(S^ab)^T C + C S^ab = 0 for all a, b (Psibar Psi is Spin(4,4)-invariant) and [Gamma, S^ab] = 0 "
          "(the chiral halves are Spin(4,4)-invariant)")
    ok = all(is_zero(sub_block(S[k], 0, 8, 8)) and is_zero(sub_block(S[k], 8, 0, 8)) for k in S)
    check("S_block_diagonal", ok, "every S^ab is block diagonal diag(S_-^ab, S_+^ab) in the chiral basis")

    # ---- Pin(4,4): Burnside spanning + commutant
    t1 = time.perf_counter()
    prods = []
    for k in range(9):
        for subset in itertools.combinations(range(8), k):
            m = I16
            for a in subset:
                m = mul(m, gamma[a])
            prods.append((subset, m))
    rows = vec_rows([m for _, m in prods])
    r_all = rank_fraction(rows, 256)
    r_all_s = rank_sympy(rows, 256)
    check("clifford_products_span_M16", r_all == 256 and r_all_s == 256,
          f"the 256 ordered products gamma^(a1)...gamma^(ak) (a1 < ... < ak) are linearly independent: rank "
          f"{r_all} (Fraction elimination), {r_all_s} (sympy DomainMatrix over QQ); so the algebra generated by "
          "the gamma^a is all of M16(R) (Cl(4,4) = M16(R)), and by Burnside the 16-dimensional representation is "
          "irreducible over R and over C")
    d1, d2 = solution_dim(gamma, gamma, 16, 16)
    check("pin_commutant_dimension_1", d1 == 1 and d2 == 1,
          f"dimension of {{X in M16 : X gamma^a = gamma^a X for all a}} = {d1} (Fraction), {d2} (sympy): only "
          "multiples of I16 (rational system, so the same dimension over R and C). Pin(4,4) is generated by the "
          "unit vectors gamma(v), eta(v,v) = +-1, whose span contains every gamma^a; hence the 16-dimensional "
          "representation of Pin(4,4) is irreducible (Schur)")

    # ---- Spin(4,4): even products, commutant, inequivalence
    even = [m for s, m in prods if len(s) % 2 == 0]
    r_even = rank_fraction(vec_rows(even), 256)
    r_even_s = rank_sympy(vec_rows(even), 256)
    even_bd = all(is_zero(sub_block(m, 0, 8, 8)) and is_zero(sub_block(m, 8, 0, 8)) for m in even)
    check("even_products_span_M8_plus_M8", r_even == 128 and r_even_s == 128 and even_bd,
          f"the 128 even products are block diagonal ({even_bd}) and linearly independent: rank {r_even} "
          f"(Fraction), {r_even_s} (sympy) = 64 + 64; the even subalgebra (the linear span of Spin(4,4) and the "
          "associative algebra generated by the S^ab) is all of M8(R) + M8(R) acting on the two chiral halves. "
          "Hence each half is irreducible and the two halves are inequivalent (if equivalent, the image would "
          "have dimension 64)")
    Slist = [S[(a, b)] for a in range(8) for b in range(a + 1, 8)]
    S2 = [[[2 * x for x in r] for r in m] for m in Slist]  # integer multiples, same commutant
    S2 = [[[int(x) for x in r] for r in m] for m in S2]
    d1, d2 = solution_dim(S2, S2, 16, 16)
    Pm = [sub_block(m, 0, 0, 8) for m in S2]
    Pp = [sub_block(m, 8, 8, 8) for m in S2]
    dm1, dm2 = solution_dim(Pm, Pm, 8, 8)
    dp1, dp2 = solution_dim(Pp, Pp, 8, 8)
    di1, di2 = solution_dim(Pm, Pp, 8, 8)   # X: (+) -> (-),  S_- X = X S_+
    dj1, dj2 = solution_dim(Pp, Pm, 8, 8)   # X: (-) -> (+)
    # the projectors span the commutant
    Pminus = diag(*([1] * 8 + [0] * 8))
    Pplus = diag(*([0] * 8 + [1] * 8))
    proj_ok = all(is_zero(comm(Pminus, m)) and is_zero(comm(Pplus, m)) for m in S2)
    proj_ok = proj_ok and eq(scal(Fraction(1, 2), sub(I16, Gamma)), Pminus) and eq(scal(Fraction(1, 2), add(I16, Gamma)), Pplus)
    check("spin_commutant_dimension_2", d1 == 2 and d2 == 2 and proj_ok,
          f"dimension of {{X in M16 : [X, S^ab] = 0 for all 28 S^ab}} = {d1} (Fraction), {d2} (sympy); it is "
          "spanned by the chiral projectors (1 - Gamma)/2 = diag(I8, 0) and (1 + Gamma)/2 = diag(0, I8), which "
          f"commute with every S^ab ({proj_ok})")
    check("spin_halves_irreducible", dm1 == dm2 == 1 and dp1 == dp2 == 1,
          f"commutant of the S^ab restricted to the Gamma = -1 half: dimension {dm1} (sympy {dm2}); to the "
          f"Gamma = +1 half: {dp1} (sympy {dp2}); each 8-dimensional half is an irreducible representation of "
          "Spin(4,4) (connected group: invariance under Spin(4,4) = invariance under its Lie algebra spanned by "
          "the S^ab)")
    check("spin_halves_inequivalent", di1 == di2 == 0 and dj1 == dj2 == 0,
          f"intertwiners S_-^ab X = X S_+^ab: dimension {di1} (sympy {di2}); S_+^ab X = X S_-^ab: dimension {dj1} "
          f"(sympy {dj2}); the two 8-dimensional irreducible representations of Spin(4,4) are inequivalent")
    ok = all(eq(mul(gamma[a], Pminus), mul(Pplus, gamma[a])) for a in range(8))
    check("reflections_exchange_halves", ok,
          "gamma^a P_- = P_+ gamma^a for every a: each reflection (an element of Pin(4,4) of determinant -1 in "
          "O(4,4)) maps one chiral half onto the other; so the irreducible 16 of Pin(4,4) restricts to Spin(4,4) "
          "as the direct sum 8_- + 8_+ of two inequivalent irreducible 8-dimensional representations")
    t_lin = time.perf_counter() - t1

    # ---- outputs
    ours = {"gamma": gamma, "C": C, "Gamma": Gamma, "B_imag": B_imag, "S": S}
    REPORTS.mkdir(parents=True, exist_ok=True)

    def frac_str(x):
        x = Fraction(x)
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

    gammas_out = {
        "description": "Revision: the author's T16 rebuilt by Revision/algebra/python/check_algebra.py, mapped to "
                       "the author's coordinates x1..x8 (SPEC section 2). Real matrices as integer arrays; B as "
                       "{re, im}; S^ab as exact rational strings.",
        "coordinates": COORDS,
        "eta": ETA,
        "map_coordinate_to_T16_index": {COORDS[a]: COORD_TO_T16[a] for a in range(8)},
        "gamma": [as_int(g) for g in gamma],
        "C": as_int(C),
        "Gamma": as_int(Gamma),
        "B": {"re": as_int(zeros(16)), "im": as_int(B_imag)},
        "S": {f"{COORDS[a]},{COORDS[b]}": [[frac_str(x) for x in r] for r in S[(a, b)]]
              for a in range(8) for b in range(a + 1, 8)},
    }
    OUR_GAMMAS.write_bytes((json.dumps(gammas_out, indent=1) + "\n").encode("utf-8"))

    status = compare_fixture(ours)

    n_fail = sum(1 for c in CHECKS if c["verdict"] == "fail")
    report = {
        "report": "Revision/algebra/reports/python-algebra.json",
        "producer": "Revision/algebra/python/check_algebra.py (exact: int, fractions.Fraction, sympy)",
        "spec": "Revision/SPEC.md section 2",
        "construction": "author's formulas: Qa, Qb, s4by4, t4by4, tau, taubar = sigma tau^T sigma, "
                        "T16 = {{0, taubar}, {tau, 0}}; coordinate map gamma^(x8) = T16[0], gamma^(x1..x7) = T16[1..7]",
        "fixture_comparison": status,
        "summary": {"checks": len(CHECKS),
                    "pass": sum(1 for c in CHECKS if c["verdict"] == "pass"),
                    "fail": n_fail,
                    "pending": sum(1 for c in CHECKS if c["verdict"] == "pending")},
        "checks": CHECKS,
    }
    REPORT.write_bytes((json.dumps(report, indent=2) + "\n").encode("utf-8"))
    total = time.perf_counter() - t0
    print(f"{len(CHECKS)} checks: {report['summary']}; fixture comparison: {status}; "
          f"linear algebra {t_lin:.1f} s, total {total:.1f} s", file=sys.stderr)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
