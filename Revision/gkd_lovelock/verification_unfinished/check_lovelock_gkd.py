#!/usr/bin/env python3
r"""Independent sympy verification of the Lovelock tensors of Lovelock's equation (4.38).

WHAT THIS CHECKS
================
The pure-Rust crate ``studies/lovelock_gkd`` computes, with GKD (its refactoring of the
author's generalized Kronecker delta), the three non-zero Lovelock tensors of (4.38),

    A_(k)^{lh} = sqrt(g) g^{jl} P_(k)^h_j,
    P_(k)^h_j  = delta^{h h1 ... h2k}_{j j1 ... j2k} R^{j1 j2}_{h1 h2} ... R^{j(2k-1) j2k}_{h(2k-1) h2k},
    k = 1, 2, 3   (n = 8, m = n/2 = 4, the sum of (4.38) runs to k = m - 1 = 3),

for the author's 8 x 8 test metric

    g = diag( e^{2 a4(x4)} sin(6 H x8)^{1/3}  (x1, x2, x3),
              -1                              (x4),
              -e^{-2 a4(x4)} sin(6 H x8)^{1/3} (x5, x6, x7),
              cot(6 H x8)^2                   (x8) ),

and writes them to ``artifacts/lovelock-gkd/`` (``curvature.json``, ``lovelock-tensors.json``).
This script recomputes everything from the metric with sympy and compares. It shares NO code
with the Rust crate: the geometry is sympy's own differentiation, the generalized delta is the
author's definition evaluated literally with sympy's determinant, and the sums are organised
differently (see "Enumeration" below). It reads only the metric (typed in below from the task
text) and, for the comparison, the two Rust JSON files. It never reads the author's notebook.

CONVENTIONS (stated)
====================
* Coordinates x1 ... x8 are indices 0 ... 7.  H > 0 and a4 is an arbitrary function of x4.
* Christoffel symbols: Gamma^a_{bc} = 1/2 g^{ad} (d_b g_{dc} + d_c g_{db} - d_d g_{bc}).
* Riemann tensor, MTW (Misner-Thorne-Wheeler) sign convention:
      R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc},
  R^{ab}_{cd} = g^{be} R^a_{ecd},  Ricci R_{bd} = R^a_{bad}, so R^h_j = R^{ha}_{ja}, R = R^a_a,
  Einstein G^h_j = R^h_j - 1/2 delta^h_j R.  (A round sphere has R > 0 in this convention.)
* sqrt(g) means sqrt|det g|.  det g = cos^2(6 H x8) exactly (checked), so on the domain
  0 < 6 H x8 < pi/2 (where sin, cos and cot are positive) sqrt|det g| = cos(6 H x8).
* The generalized Kronecker delta is the author's
      kdelta[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]
  i.e. the determinant of the 0/1 matrix M[r][c] = 1 if lower[r] == upper[c] else 0, and
      delta^{h h1 ... h2k}_{j j1 ... j2k} = kdelta[{j, j1, ..., j2k}, {h, h1, ..., h2k}]
  (det M = det M^T, so it does not matter which list labels the rows).
* L_(k) = delta^{h1 ... h2k}_{j1 ... j2k} R^{j1 j2}_{h1 h2} ... is the k-th Lovelock scalar.

Symbols used for exact simplification ("symbol form"): E = e^{a4(x4)}, s = sin(6 H x8)^{1/3},
c = cot(6 H x8), A1 ... A4 = a4', a4'', a4''', a4''''.  They satisfy one relation,
cos^2 + sin^2 = 1, i.e. s^6 (1 + c^2) = 1.  ``canon`` (below) uses it to bring any
expression to the unique form  b0 + b1 s + ... + b5 s^5  with b_r rational functions of
(H, A1..A4, E, c) (1, s, ..., s^5 are linearly independent over those functions because
x^6 - 1/(1 + c^2) is irreducible), so "canon(X - Y) == 0" is an exact proof that X = Y.

ENUMERATION (different from the Rust depth-first search)
========================================================
The Rust code runs, for every (h, j), a depth-first search over ordered tuples of non-zero
R^{ab}_{cd} entries with bit masks.  Here the k-fold products are built breadth-first once,
independently of (h, j): T_1 = the non-zero entries, T_m = T_(m-1) x entries, keeping only
products whose lower indices are pairwise different and whose upper indices are pairwise
different (a repeated index makes two rows - or two columns - of Outer[delta, lower, upper]
equal, so the determinant is 0: "repeated-index lemma").  Then every product is completed by
every j not among its lower indices and every h not among its upper indices, and the weight of
that term is ONE LITERAL CALL of kdelta.  The integer weights are collected per multiset of
entries and multiplied out once, with sympy's sparse polynomial ring QQ[H, A1, A2, c, 1/c].
The repeated-index lemma is not taken on trust: for k = 1 and k = 2 the completely unpruned
literal sums (every ordered product of non-zero entries, every (h, j), every index list sent
to kdelta) are computed as well and must agree exactly; for k = 3 a deterministic random
sample of skipped terms is sent to kdelta and must give 0; for k = 4 random 9-index lists
(8 values) must give 0.  kdelta is memoised by its argument Outer[delta, lower, upper] (a
function of the index lists; more cache hits than keying by the lists themselves).

INDEPENDENT ROUTES AND NORMALISATIONS (derived here)
=====================================================
Expanding the (2k+1) x (2k+1) determinant along the row of h (Laplace) and moving j into the
place of the removed index gives
    P_(k)^h_j = delta^h_j L_(k) - 2k delta^{h1 ... h2k}_{j j2 ... j2k} R^{h j2}_{h1 h2} R^{j3 j4}_{h3 h4} ...
k = 1:  delta^{h1 h2}_{j b} R^{h b}_{h1 h2} = 2 R^h_j and L_(1) = 2 R, so
        P_(1) = 2 R delta - 4 Ric = -4 G.
k = 2:  X^h_j := delta^{h1 h2 h3 h4}_{j b c d} R^{hb}_{h1h2} R^{cd}_{h3h4}; expanding along the
        column of j and using the k = 1 result twice,
        X^h_j = 4 R R^h_j - 8 R^{hb}_{jx} R^x_b - 8 R^h_c R^c_j + 4 R^{hb}_{cd} R^{cd}_{jb},
        L_(2) = X^h_h = 4 (R^2 - 4 R^a_b R^b_a + R^{ab}_{cd} R^{cd}_{ab}) = 4 GB, and
        P_(2) = 4 GB delta - 4 X = -8 H with the classical Gauss-Bonnet (Lanczos) tensor
        H^h_j = 2 (R R^h_j - 2 R^h_a R^a_j - 2 R^{ha}_{jb} R^b_a + R^{habc} R_{jabc})
                - 1/2 delta^h_j (R^2 - 4 R_ab R^ab + R_abcd R^abcd)
        (R^{habc} R_{jabc} = R^{ha}_{bc} R^{bc}_{ja}).  So the constant is -8, as in the task.
k = 3:  L_(3) = 8 (2 T1 + 8 T2 + 24 T3 + 3 T4 + 24 T5 + 16 T6 - 12 T7 + T8) with the eight
        cubic invariants of ``cubic_invariants`` (the classical cubic Lovelock density).
The constants -4, -8 and the eight cubic coefficients are also DERIVED numerically here, from
literal kdelta sums on random algebraic curvature tensors (sums of Kulkarni-Nomizu products of
random integer symmetric matrices, Euclidean signature): P_(1) = alpha G in d = 4,
P_(2) = beta H in d = 5, and L_(3) = sum_i c_i T_i in d = 6 from 9 random tensors (the 9 x 8
system has rank 8, so the c_i are unique).  Further identities: trace sum_h P_(k)^h_h =
(8 - 2k) L_(k), zero covariant divergence, symmetry of g_hh P^h_j (so A^{lh} = A^{hl}).

COMPARISON WITH THE RUST OUTPUT
===============================
Every one of the 3 x 64 mixed P_(k)^h_j and 3 x 64 contravariant A_(k)^{lh} components of
``lovelock-tensors.json`` is rebuilt from its exact monomial list [[num, den, [e_H, e_a4',
e_a4'', e_a4''', e_a4'''', e_E, e_S, e_C]], ...] with E -> exp(a4(x4)), S -> sin(6 H x8)^(1/3),
C -> cot(6 H x8), a4^(n) -> Derivative(a4(x4), (x4, n)), and the difference with this script's
own component is shown to vanish exactly (1) by ``canon`` and (2) by plain sympy (expand /
simplify after cot = cos/sin), and (3) numerically at 5 random rational points with 60 digits.
The same is done for L_(1..3), and for curvature.json: the metric, sqrt|g|, every Christoffel
symbol, every R^{ab}_{cd}, the Ricci and Einstein tensors and the Ricci scalar.  The Rust
Mathematica text of each component is also checked against its own monomial list.  Negative
controls: deliberately tampered Rust components (a coefficient + 1, a wrong power of
sin^(1/3), a wrong power of e^{a4}, an added 10^-30 H^4) must be detected by each of the
three methods separately.

USAGE (from the repository root)
================================
    python scripts/check_lovelock_gkd.py
        reads artifacts/lovelock-gkd/{curvature,lovelock-tensors}.json and writes
        artifacts/lovelock-gkd/python-lovelock-report.json
    python scripts/check_lovelock_gkd.py --artifacts DIR --report OUT.json
Exit status 0 if and only if every check passes.  The report contains no timings, so two runs
give byte-identical files; the run times are printed on the terminal.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import re
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.rings import ring

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACTS = ROOT / "artifacts" / "lovelock-gkd"
REPORT_NAME = "python-lovelock-report.json"
N = 8
NAMES = [f"x{i}" for i in range(1, N + 1)]

# ---------------------------------------------------------------------------------------------
# Symbols: "function form" (what sympy differentiates) and "symbol form" (for exact algebra)
# ---------------------------------------------------------------------------------------------
H = sp.Symbol("H", positive=True)
X = sp.symbols("x1:9", real=True)
x4, x8 = X[3], X[7]
a4 = sp.Function("a4")
TH = 6 * H * x8
THIRD = sp.Rational(1, 3)
DER = [sp.Derivative(a4(x4), (x4, m)) for m in range(1, 5)]  # a4', a4'', a4''', a4''''

E_, s_, c_ = sp.symbols("E s c", positive=True)
A_ = sp.symbols("A1:5")
ci_ = sp.Symbol("ci", positive=True)  # 1/c inside the polynomial ring only
SYMBOL_FORM_SYMBOLS = {H, E_, s_, c_, *A_}
TO_A = {DER[m]: A_[m] for m in range(4)}
FROM_SYMBOLS = {A_[m]: DER[m] for m in range(4)}
FROM_SYMBOLS.update({E_: sp.exp(a4(x4)), s_: sp.sin(TH) ** THIRD, c_: sp.cot(TH)})

# The polynomial ring used for the Lovelock sums (mixed curvature is free of E and s).
RING, _rH, _rA1, _rA2, _rC, rCI = ring([H, A_[0], A_[1], c_, ci_], sp.QQ)
I_C, I_CI = 3, 4  # positions of c and 1/c in the exponent vectors

ZERO6 = (sp.Integer(0),) * 6


def metric_diagonal():
    """The author's metric, typed in from the task text (function form)."""
    warp = sp.sin(TH) ** THIRD
    return ([sp.exp(2 * a4(x4)) * warp] * 3 + [sp.Integer(-1)]
            + [-sp.exp(-2 * a4(x4)) * warp] * 3 + [sp.cot(TH) ** 2])


def _check_angle(arg):
    if sp.expand(arg - TH) != 0:
        raise ValueError(f"unexpected trigonometric argument {arg}")


def to_symbol_form(expr):
    """Function form -> symbol form (E, s, c, A1..A4).  Exact, no simplification."""
    expr = sp.sympify(expr).xreplace(TO_A)

    def fexp(arg):
        q = sp.cancel(arg / a4(x4))
        if not q.is_Rational:
            raise ValueError(f"unexpected exponential exp({arg})")
        return E_ ** q

    def fsin(arg):
        _check_angle(arg)
        return s_ ** 3

    def fcos(arg):
        _check_angle(arg)
        return c_ * s_ ** 3

    def fcot(arg):
        _check_angle(arg)
        return c_

    def ftan(arg):
        _check_angle(arg)
        return 1 / c_

    def fcsc(arg):
        _check_angle(arg)
        return s_ ** -3

    def fsec(arg):
        _check_angle(arg)
        return 1 / (c_ * s_ ** 3)

    expr = expr.replace(sp.exp, fexp)
    for f, rule in ((sp.sin, fsin), (sp.cos, fcos), (sp.cot, fcot), (sp.tan, ftan),
                    (sp.csc, fcsc), (sp.sec, fsec)):
        expr = expr.replace(f, rule)
    extra = expr.free_symbols - SYMBOL_FORM_SYMBOLS
    if extra or expr.has(sp.Function("a4")) or expr.has(sp.Derivative):
        raise ValueError(f"could not bring to symbol form: {expr} (left: {extra})")
    return expr


def to_function_form(expr):
    """Symbol form -> function form (inverse of to_symbol_form)."""
    return sp.sympify(expr).xreplace(FROM_SYMBOLS)


def canon(expr):
    """Unique normal form (b0, ..., b5): expr = sum_r b_r s^r with s^6 = 1/(1 + c^2)."""
    expr = sp.sympify(expr)
    if expr == 0:
        return ZERO6
    expr = sp.expand(to_symbol_form(expr))
    parts = [[] for _ in range(6)]
    for term in sp.Add.make_args(expr):
        coeff, k = term.as_coeff_exponent(s_)
        if not k.is_Integer or coeff.has(s_):
            raise ValueError(f"term not a monomial in s: {term}")
        k = int(k)
        r = k % 6
        parts[r].append(coeff * (1 + c_ ** 2) ** (-((k - r) // 6)))
    return tuple(sp.cancel(sp.Add(*p)) for p in parts)


def is_zero(expr):
    return all(b == 0 for b in canon(expr))


def sympy_zero(diff):
    """Plain sympy: rewrite cot = cos/sin, tan = sin/cos, expand, and simplify if needed."""
    e = sp.sympify(diff)
    if e == 0:
        return True
    e = e.replace(sp.cot, lambda a: sp.cos(a) / sp.sin(a)).replace(sp.tan, lambda a: sp.sin(a) / sp.cos(a))
    e = sp.expand(e)
    if e == 0:
        return True
    return sp.simplify(sp.trigsimp(e)) == 0


# ---------------------------------------------------------------------------------------------
# Ring helpers (Laurent polynomials in c via the extra generator ci = 1/c)
# ---------------------------------------------------------------------------------------------
def ring_normalise(p):
    """Cancel c * ci = 1 in every monomial, so equal Laurent polynomials are equal elements."""
    acc = {}
    for monom, coeff in p.terms():
        e = list(monom)
        m = min(e[I_C], e[I_CI])
        e[I_C] -= m
        e[I_CI] -= m
        key = tuple(e)
        acc[key] = acc.get(key, 0) + coeff
    return RING.from_dict({k: v for k, v in acc.items() if v != 0}) if acc else RING.zero


def ring_from_symbol_form(expr):
    num, den = sp.fraction(sp.cancel(sp.sympify(expr)))
    powers = sp.Poly(den, c_).as_dict() if den.has(c_) else {(0,): den}
    if len(powers) != 1:
        raise ValueError(f"denominator {den} is not a monomial in c")
    ((m,), const), = powers.items()
    if const.free_symbols:
        raise ValueError(f"denominator {den} is not a monomial in c")
    return ring_normalise(RING.from_expr(num) * rCI ** m * (1 / sp.Rational(const)))


def ring_to_symbol_form(p):
    return sp.sympify(p.as_expr()).xreplace({ci_: 1 / c_})


def ring_equal(p, q):
    return ring_normalise(p - q) == RING.zero


# ---------------------------------------------------------------------------------------------
# The generalized Kronecker delta, literally as the author defined it
# ---------------------------------------------------------------------------------------------
_DET_CACHE: dict = {}
KDELTA_STATS = {"calls": 0, "sympyDeterminants": 0}


def kdelta(lower, upper):
    """kdelta[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]].

    Outer[delta, lower, upper] is the matrix whose entry (r, c) is 1 if lower[r] == upper[c]
    and 0 otherwise; its determinant is taken with sympy (Matrix.det).  No permutation sign is
    used anywhere.  The determinant is memoised by the matrix (row-major tuple of booleans).
    """
    m = len(lower)
    if m != len(upper):
        raise ValueError("kdelta needs two index lists of the same length")
    KDELTA_STATS["calls"] += 1
    outer = tuple(lo == up for lo in lower for up in upper)
    value = _DET_CACHE.get(outer)
    if value is None:
        matrix = sp.Matrix([[1 if outer[r * m + c] else 0 for c in range(m)] for r in range(m)])
        value = int(matrix.det())
        _DET_CACHE[outer] = value
        KDELTA_STATS["sympyDeterminants"] += 1
    return value


def cofactor_det(rows):
    """Reference determinant by cofactor (Laplace) expansion along the first row, pure Python."""
    m = len(rows)
    if m == 0:
        return 1
    if m == 1:
        return rows[0][0]
    total = 0
    for c in range(m):
        if rows[0][c]:
            minor = [row[:c] + row[c + 1:] for row in rows[1:]]
            total += (-1) ** c * rows[0][c] * cofactor_det(minor)
    return total


def gkd_selftest(rec):
    rng = random.Random(4242)
    ref_cache = {}

    def ref(lower, upper):
        key = tuple(lo == up for lo in lower for up in upper)
        if key not in ref_cache:
            ref_cache[key] = cofactor_det([[1 if lo == up else 0 for up in upper] for lo in lower])
        return ref_cache[key]

    exhaustive = 0
    mismatches = 0
    for m in (1, 2, 3):
        for lower in itertools.product(range(N), repeat=m):
            for upper in itertools.product(range(N), repeat=m):
                exhaustive += 1
                if kdelta(lower, upper) != ref(lower, upper):
                    mismatches += 1
    sampled = 0
    for m in (4, 5, 6, 7, 8):
        for _ in range(1500):
            if rng.random() < 0.5:  # a permutation-related pair, so that non-zero values occur
                lower = tuple(rng.sample(range(N), m))
                upper = tuple(rng.sample(lower, m))
            else:
                lower = tuple(rng.randrange(N) for _ in range(m))
                upper = tuple(rng.randrange(N) for _ in range(m))
            sampled += 1
            if kdelta(lower, upper) != ref(lower, upper):
                mismatches += 1
    rec.add("gkd_literal_equals_cofactor_expansion", mismatches == 0,
            f"kdelta (sympy Det of Outer[delta, lower, upper]) equals an independent cofactor-expansion "
            f"determinant for all {exhaustive} pairs of index lists of length 1, 2, 3 over 8 values and "
            f"{sampled} random pairs of length 4..8; mismatches: {mismatches}")
    examples = {
        "kdelta[{1,2},{1,2}]": kdelta((1, 2), (1, 2)),
        "kdelta[{1,2},{2,1}]": kdelta((1, 2), (2, 1)),
        "kdelta[{1,1},{1,1}]": kdelta((1, 1), (1, 1)),
        "kdelta[{1,2,3},{2,3,1}]": kdelta((1, 2, 3), (2, 3, 1)),
        "kdelta[{1,2,3},{1,2,4}]": kdelta((1, 2, 3), (1, 2, 4)),
    }
    ok = list(examples.values()) == [1, -1, 0, 1, 0]
    rec.add("gkd_examples", ok, "; ".join(f"{k} = {v}" for k, v in examples.items()))
    nine = 0
    bad = 0
    for _ in range(300):
        lower = tuple(rng.randrange(N) for _ in range(9))
        upper = tuple(rng.randrange(N) for _ in range(9))
        nine += 1
        if kdelta(lower, upper) != 0:
            bad += 1
    rec.add("gkd_nine_indices_in_eight_dimensions_vanish", bad == 0,
            f"kdelta of {nine} random pairs of 9-index lists over 8 values is 0 (two equal rows: "
            f"pigeonhole), so P_(4) = 0 and (4.38) stops at k = m - 1 = 3; non-zero: {bad}")


# ---------------------------------------------------------------------------------------------
# Lovelock sums (generic: entry values may be ints or ring elements)
# ---------------------------------------------------------------------------------------------
def lovelock_sums(entries, k, n, zero, one):
    """Breadth-first enumeration (see the module docstring).

    entries: list of ((a, b), (c, d), value) for the non-zero R^{ab}_{cd}.
    Returns (P, L, counters) with P[h][j] = P_(k)^h_j and L = L_(k).
    """
    level = [(lo, up, (i,)) for i, (lo, up, _) in enumerate(entries)]
    for _ in range(k - 1):
        nxt = []
        for lower, upper, ids in level:
            for i, (lo, up, _) in enumerate(entries):
                if lo[0] in lower or lo[1] in lower or up[0] in upper or up[1] in upper:
                    continue  # repeated index: kdelta = 0 (lemma; checked literally elsewhere)
                nxt.append((lower + lo, upper + up, ids + (i,)))
        level = nxt
    weights_p: dict = {}
    weights_l: dict = {}
    calls = nonzero = 0
    for lower, upper, ids in level:
        key = tuple(sorted(ids))
        v = kdelta(lower, upper)
        calls += 1
        if v:
            nonzero += 1
            weights_l[key] = weights_l.get(key, 0) + v
        js = [j for j in range(n) if j not in lower]
        hs = [h for h in range(n) if h not in upper]
        for j in js:
            jl = (j,) + lower
            for h in hs:
                v = kdelta(jl, (h,) + upper)
                calls += 1
                if v:
                    nonzero += 1
                    bucket = weights_p.setdefault((h, j), {})
                    bucket[key] = bucket.get(key, 0) + v
    products: dict = {}

    def product(key):
        p = products.get(key)
        if p is None:
            p = one
            for i in key:
                p = p * entries[i][2]
            products[key] = p
        return p

    P = [[zero for _ in range(n)] for _ in range(n)]
    for (h, j), bucket in weights_p.items():
        acc = zero
        for key, w in bucket.items():
            if w:
                acc = acc + w * product(key)
        P[h][j] = acc
    L = zero
    for key, w in weights_l.items():
        if w:
            L = L + w * product(key)
    counters = {"k": k, "products": len(level), "kdeltaCalls": calls, "kdeltaNonzero": nonzero,
                "distinctMultisets": len(products)}
    return P, L, counters


def lovelock_sums_unpruned(entries, k, n, zero, one):
    """Literal sum: every ordered k-tuple of non-zero entries and every (h, j), no pruning."""
    P = [[zero for _ in range(n)] for _ in range(n)]
    L = zero
    calls = 0
    for ids in itertools.product(range(len(entries)), repeat=k):
        lower = tuple(x for i in ids for x in entries[i][0])
        upper = tuple(x for i in ids for x in entries[i][1])
        prod = None
        v = kdelta(lower, upper)
        calls += 1
        if v:
            prod = one
            for i in ids:
                prod = prod * entries[i][2]
            L = L + v * prod
        for j in range(n):
            jl = (j,) + lower
            for h in range(n):
                v = kdelta(jl, (h,) + upper)
                calls += 1
                if v:
                    if prod is None:
                        prod = one
                        for i in ids:
                            prod = prod * entries[i][2]
                    P[h][j] = P[h][j] + v * prod
    return P, L, calls


# ---------------------------------------------------------------------------------------------
# Classical curvature expressions (generic over a dict of non-zero R^{ab}_{cd})
# ---------------------------------------------------------------------------------------------
def ricci(rm, n, zero):
    ric = [[zero for _ in range(n)] for _ in range(n)]
    for (h, a, j, b), v in rm.items():
        if a == b:
            ric[h][j] = ric[h][j] + v
    return ric


def trace(m, n, zero):
    t = zero
    for i in range(n):
        t = t + m[i][i]
    return t


def riemann_square(rm, zero):
    t = zero
    for (a, b, c, d), v in rm.items():
        w = rm.get((c, d, a, b))
        if w is not None:
            t = t + v * w
    return t


def ricci_square(ric, n, zero):
    t = zero
    for a in range(n):
        for b in range(n):
            t = t + ric[a][b] * ric[b][a]
    return t


def twice_gauss_bonnet_tensor(rm, ric, rs, n, zero):
    """2 H^h_j = 4 (R R^h_j - 2 R^h_a R^a_j - 2 R^{ha}_{jb} R^b_a + R^{ha}_{bc} R^{bc}_{ja}) - delta GB."""
    gb = rs * rs - 4 * ricci_square(ric, n, zero) + riemann_square(rm, zero)
    out = [[zero for _ in range(n)] for _ in range(n)]
    for h in range(n):
        for j in range(n):
            t1 = rs * ric[h][j]
            t2 = zero
            for a in range(n):
                t2 = t2 + ric[h][a] * ric[a][j]
            out[h][j] = 4 * t1 - 8 * t2
    for (h, a, j, b), v in rm.items():  # - 2 R^{ha}_{jb} R^b_a
        out[h][j] = out[h][j] - 8 * v * ric[b][a]
    for (h, a, b, c), v in rm.items():  # + R^{ha}_{bc} R^{bc}_{ja}
        for j in range(n):
            w = rm.get((b, c, j, a))
            if w is not None:
                out[h][j] = out[h][j] + 4 * v * w
    for h in range(n):
        out[h][h] = out[h][h] - gb
    return out, gb


def cubic_invariants(rm, ric, rs, n, zero):
    """T1..T8 of the classical cubic Lovelock density, every contraction in mixed form."""
    t = [zero] * 8
    for (a, b, c, d), v in rm.items():
        for (c2, d2, e, f), w in rm.items():
            if (c2, d2) == (c, d):
                u = rm.get((e, f, a, b))
                if u is not None:
                    t[0] = t[0] + v * w * u                       # R^{ab}_{cd} R^{cd}_{ef} R^{ef}_{ab}
        for e in range(n):
            for f in range(n):
                w = rm.get((c, e, b, f))
                if w is None:
                    continue
                u = rm.get((d, f, a, e))
                if u is not None:
                    t[1] = t[1] + v * w * u                       # R^{ab}_{cd} R^{ce}_{bf} R^{df}_{ae}
        for e in range(n):
            w = rm.get((c, d, b, e))
            if w is not None:
                t[2] = t[2] + v * w * ric[e][a]                   # R^{ab}_{cd} R^{cd}_{be} R^e_a
        t[4] = t[4] + v * ric[c][a] * ric[d][b]                   # R^{ab}_{cd} R^c_a R^d_b
    t[3] = rs * riemann_square(rm, zero)                          # R R^{ab}_{cd} R^{cd}_{ab}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                t[5] = t[5] + ric[a][b] * ric[b][c] * ric[c][a]   # R^a_b R^b_c R^c_a
    t[6] = rs * ricci_square(ric, n, zero)                        # R R^a_b R^b_a
    t[7] = rs * rs * rs                                           # R^3
    return t


CUBIC_COEFFICIENTS = [2, 8, 24, 3, 24, 16, -12, 1]


# ---------------------------------------------------------------------------------------------
# Random algebraic curvature tensors (normalisation derivations)
# ---------------------------------------------------------------------------------------------
def random_curvature(d, rng, terms=3):
    """Sum of Kulkarni-Nomizu products h (.) k of random integer symmetric matrices."""
    R = np.zeros((d, d, d, d), dtype=np.int64)
    for _ in range(terms):
        h = np.zeros((d, d), dtype=np.int64)
        k = np.zeros((d, d), dtype=np.int64)
        for i in range(d):
            for j in range(i, d):
                h[i, j] = h[j, i] = rng.randint(-3, 3)
                k[i, j] = k[j, i] = rng.randint(-3, 3)
        R += (np.einsum("ac,bd->abcd", h, k) + np.einsum("bd,ac->abcd", h, k)
              - np.einsum("ad,bc->abcd", h, k) - np.einsum("bc,ad->abcd", h, k))
    return R


def curvature_symmetries_hold(R):
    return bool((R == -R.transpose(1, 0, 2, 3)).all() and (R == R.transpose(2, 3, 0, 1)).all()
                and (R + R.transpose(0, 2, 3, 1) + R.transpose(0, 3, 1, 2) == 0).all())


def as_sparse(R):
    d = R.shape[0]
    rm = {}
    for idx in itertools.product(range(d), repeat=4):
        v = int(R[idx])
        if v:
            rm[idx] = v
    return rm


def derive_normalisations(rec):
    rng = random.Random(1985)
    # k = 1, d = 4: unpruned literal P_(1) versus G.
    ratios1 = set()
    ok1 = True
    for _ in range(3):
        R = random_curvature(4, rng)
        ok1 &= curvature_symmetries_hold(R)
        rm = as_sparse(R)
        entries = [((a, b), (c, d), v) for (a, b, c, d), v in sorted(rm.items())]
        P, L, _ = lovelock_sums_unpruned(entries, 1, 4, 0, 1)
        ric = ricci(rm, 4, 0)
        rs = trace(ric, 4, 0)
        G2 = [[2 * ric[h][j] - (rs if h == j else 0) for j in range(4)] for h in range(4)]  # 2 G
        for h in range(4):
            for j in range(4):
                if G2[h][j]:
                    ratios1.add(sp.Rational(2 * P[h][j], G2[h][j]))
                elif P[h][j]:
                    ok1 = False
        ok1 &= (L == 2 * rs)
    ok1 &= ratios1 == {sp.Integer(-4)}
    rec.add("normalisation_P1_derived_minus_4", ok1,
            f"3 random algebraic curvature tensors in d = 4, unpruned literal kdelta sums: P_(1)^h_j / G^h_j "
            f"takes the single value {sorted(ratios1)} on all non-zero components, and L_(1) = 2 R")
    # k = 2, d = 5: P_(2) versus the Gauss-Bonnet tensor.
    ratios2 = set()
    ok2 = True
    for _ in range(3):
        R = random_curvature(5, rng)
        ok2 &= curvature_symmetries_hold(R)
        rm = as_sparse(R)
        entries = [((a, b), (c, d), v) for (a, b, c, d), v in sorted(rm.items())]
        P, L, _ = lovelock_sums(entries, 2, 5, 0, 1)
        ric = ricci(rm, 5, 0)
        rs = trace(ric, 5, 0)
        H2, gb = twice_gauss_bonnet_tensor(rm, ric, rs, 5, 0)
        for h in range(5):
            for j in range(5):
                if H2[h][j]:
                    ratios2.add(sp.Rational(2 * P[h][j], H2[h][j]))
                elif P[h][j]:
                    ok2 = False
        ok2 &= (L == 4 * gb)
    ok2 &= ratios2 == {sp.Integer(-8)}
    rec.add("normalisation_P2_derived_minus_8", ok2,
            f"3 random algebraic curvature tensors in d = 5, literal kdelta sums: P_(2)^h_j / H^h_j (Gauss-Bonnet "
            f"tensor) takes the single value {sorted(ratios2)} on all non-zero components, and L_(2) = 4 GB")
    # k = 3, d = 6: solve L_(3) = sum_i c_i T_i from 9 random tensors.
    perms = list(itertools.permutations(range(6)))
    K = np.array([[kdelta(lo, up) for up in perms] for lo in perms], dtype=np.int64)
    pa = np.array(perms, dtype=np.int64)
    rows, rhs = [], []
    ok3 = True
    for _ in range(9):
        R = random_curvature(6, rng)
        ok3 &= curvature_symmetries_hold(R)
        prod = (R[pa[:, None, 0], pa[:, None, 1], pa[None, :, 0], pa[None, :, 1]]
                * R[pa[:, None, 2], pa[:, None, 3], pa[None, :, 2], pa[None, :, 3]]
                * R[pa[:, None, 4], pa[:, None, 5], pa[None, :, 4], pa[None, :, 5]])
        rhs.append(int((K * prod).sum()))
        rm = as_sparse(R)
        ric = ricci(rm, 6, 0)
        rs = trace(ric, 6, 0)
        rows.append([int(x) for x in cubic_invariants(rm, ric, rs, 6, 0)])
    M = sp.Matrix(rows)
    v = sp.Matrix(rhs)
    rank = M.rank()
    coeffs = None
    if rank == 8:
        coeffs = list((M.T * M).LUsolve(M.T * v))
        ok3 &= (M * sp.Matrix(coeffs) - v).is_zero_matrix
    ok3 &= rank == 8 and coeffs == [8 * c for c in CUBIC_COEFFICIENTS]
    rec.add("normalisation_L3_cubic_derived", bool(ok3),
            f"9 random algebraic curvature tensors in d = 6, literal sums over all 720 x 720 pairs of index "
            f"permutations with kdelta: the 9 x 8 matrix of cubic invariants has rank {rank} and the unique "
            f"solution of L_(3) = sum c_i T_i is c = {coeffs} = 8 x {CUBIC_COEFFICIENTS}")


# ---------------------------------------------------------------------------------------------
# Geometry with sympy
# ---------------------------------------------------------------------------------------------
def geometry(rec):
    diag = metric_diagonal()
    g = sp.diag(*diag)
    gi = g.inv()
    ok = all(is_zero((g * gi)[a, b] - (1 if a == b else 0)) for a in range(N) for b in range(N))
    rec.add("metric_inverse", ok, "g g^{-1} = 1 exactly (sympy Matrix.inv)")
    det = g.det()
    sqrt_g = sp.cos(TH)
    pts = Points()
    literal_root = sp.sqrt(sp.Abs(det))
    numeric_ok = all(abs(pts.evaluate(literal_root, p) - pts.evaluate(sqrt_g, p)) < sp.Float("1e-50", 60)
                     and pts.evaluate(sqrt_g, p) > 0 for p in pts.points)
    rec.add("sqrt_abs_det_g", is_zero(det - sqrt_g ** 2) and numeric_ok,
            "det g = cos^2(6 H x8) exactly, so sqrt|det g| = cos(6 H x8) on 0 < 6 H x8 < pi/2; sympy's "
            "sqrt(Abs(det g)) equals cos(6 H x8) > 0 at the 5 random points (60 digits)")
    gamma = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                v = sp.Integer(0)
                for d in range(N):
                    if gi[a, d] != 0:
                        v += gi[a, d] * (sp.diff(g[d, c], X[b]) + sp.diff(g[d, b], X[c]) - sp.diff(g[b, c], X[d]))
                gamma[a][b][c] = v / 2
    gamma_canon = {}
    for a in range(N):
        for b in range(N):
            for c in range(N):
                cf = canon(gamma[a][b][c])
                if any(x != 0 for x in cf):
                    gamma_canon[a, b, c] = cf
    sym_ok = all(gamma_canon.get((a, b, c)) == gamma_canon.get((a, c, b))
                 for a in range(N) for b in range(N) for c in range(N))
    rec.add("christoffel_symmetric", sym_ok, "Gamma^a_{bc} = Gamma^a_{cb}")
    riem = {}
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    v = sp.diff(gamma[a][b][d], X[c]) - sp.diff(gamma[a][b][c], X[d])
                    for e in range(N):
                        v += gamma[a][c][e] * gamma[e][b][d] - gamma[a][d][e] * gamma[e][b][c]
                    riem[a, b, c, d] = v
    bianchi_ok = all(is_zero(riem[a, b, c, d] + riem[a, c, d, b] + riem[a, d, b, c])
                     for a in range(N) for b in range(N) for c in range(N) for d in range(N))
    rec.add("riemann_first_bianchi", bianchi_ok, "R^a_{bcd} + R^a_{cdb} + R^a_{dbc} = 0 exactly for all 4096 index lists")
    rud = {}
    free_ok = True
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    v = sp.Integer(0)
                    for e in range(N):
                        if gi[b, e] != 0:
                            v += gi[b, e] * riem[a, e, c, d]
                    cf = canon(v)
                    if any(x != 0 for x in cf[1:]) or cf[0].has(E_):
                        free_ok = False
                    if cf[0] != 0:
                        rud[a, b, c, d] = cf[0]
    rec.add("mixed_riemann_free_of_warp_and_exponential", free_ok,
            "every R^{ab}_{cd} is free of sin(6 H x8)^(1/3) and of e^{a4}: a rational function of H, a4', a4'', cot(6 H x8)")
    anti_ok = all(sp.cancel(v + rud.get((b, a, c, d), 0)) == 0 and sp.cancel(v + rud.get((a, b, d, c), 0)) == 0
                  for (a, b, c, d), v in rud.items())
    gsym = [to_symbol_form(x) for x in diag]
    pair_ok = all(is_zero(gsym[a] * gsym[b] * v - gsym[c] * gsym[d] * rud.get((c, d, a, b), 0))
                  for (a, b, c, d), v in rud.items())
    rec.add("riemann_antisymmetry_and_pair_symmetry", anti_ok and pair_ok,
            f"R^ab_cd = -R^ba_cd = -R^ab_dc and R_abcd = R_cdab exactly; {len(rud)} non-zero R^ab_cd")
    return {"diag": diag, "g": g, "gi": gi, "sqrt_g": sqrt_g, "gamma": gamma, "gamma_canon": gamma_canon,
            "rud": rud, "gsym": gsym}


# ---------------------------------------------------------------------------------------------
# Reading the Rust output
# ---------------------------------------------------------------------------------------------
def index_pair(key):
    a, b = key.split(",")
    return NAMES.index(a), NAMES.index(b)


def from_monomials(monomials):
    """Rebuild a component from [[num, den, [eH, ea1, ea2, ea3, ea4, eE, eS, eC]], ...] (function form)."""
    total = sp.Integer(0)
    for num, den, e in monomials:
        if len(e) != 8:
            raise ValueError(f"bad exponent vector {e}")
        term = sp.Rational(num, den) * H ** e[0]
        for m in range(4):
            term *= DER[m] ** e[1 + m]
        term *= sp.exp(a4(x4)) ** e[5] * (sp.sin(TH) ** THIRD) ** e[6] * sp.cot(TH) ** e[7]
        total += term
    return total


_MMA_LOCALS = {"H": H, "x8": x8, "E": sp.E, "a4x4": a4(x4), "sin": sp.sin, "cot": sp.cot,
               **{f"Da4n{m + 1}": DER[m] for m in range(4)}}


def from_mathematica(text):
    """Parse the Rust Mathematica text (InputForm subset) into a function-form sympy expression."""
    t = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"Da4n\1", text)
    t = t.replace("a4[x4]", "a4x4").replace("Sin[6*H*x8]", "sin(6*H*x8)").replace("Cot[6*H*x8]", "cot(6*H*x8)")
    if "[" in t or "]" in t:
        raise ValueError(f"unparsed Mathematica text: {text}")
    t = t.replace("^", "**")
    expr = sp.parse_expr(t, local_dict=dict(_MMA_LOCALS))
    if expr.free_symbols - {H, x4, x8}:
        raise ValueError(f"unknown symbols in {text}: {expr.free_symbols}")
    return expr


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Points:
    """5 random rational points with 0 < 6 H x8 < pi/2; values of a4 and of its derivatives."""

    def __init__(self, seed=20261001, count=5):
        rng = random.Random(seed)
        self.points = []
        for _ in range(count):
            h = sp.Rational(rng.randint(10, 60), 100)
            theta = sp.Rational(rng.randint(10, 150), 100)  # 0.10 ... 1.50 < pi/2
            x = theta / (6 * h)
            vals = [sp.Rational(rng.randint(-99, 99), 100) for _ in range(5)]
            self.points.append((h, x, vals))

    def evaluate(self, expr, point):
        h, x, vals = point
        e = sp.sympify(expr).xreplace({DER[m]: vals[m + 1] for m in range(4)})
        e = e.xreplace({a4(x4): vals[0]}).xreplace({H: h, x8: x})
        return sp.N(e, 60)

    def describe(self):
        return [{"H": str(h), "x8": str(x), "6Hx8": str(6 * h * x), "a4": str(v[0]), "a4'": str(v[1]),
                 "a4''": str(v[2]), "a4'''": str(v[3]), "a4''''": str(v[4])} for h, x, v in self.points]


class Comparator:
    """Exact (canon), plain-sympy and numeric comparison of two function-form expressions."""

    def __init__(self, points):
        self.points = points
        self.count = 0
        self.nonzero = 0
        self.failures = []
        self.numeric_evaluations = 0
        self.max_numeric = sp.Integer(0)

    def compare(self, label, mine, theirs):
        self.count += 1
        diff = sp.sympify(mine) - sp.sympify(theirs)
        exact = is_zero(diff)
        plain = sympy_zero(diff)
        numeric = True
        if sp.sympify(mine) != 0 or sp.sympify(theirs) != 0:
            self.nonzero += 1
            for pt in self.points.points:
                a = self.points.evaluate(mine, pt)
                b = self.points.evaluate(theirs, pt)
                self.numeric_evaluations += 1
                if not (a.is_number and b.is_number and a.is_real and b.is_real):
                    numeric = False  # something was left unevaluated: never count that as agreement
                    continue
                dev = abs(a - b) / max(1, abs(a))
                if dev > self.max_numeric:
                    self.max_numeric = dev
                if dev > sp.Float("1e-45", 60):
                    numeric = False
        if not (exact and plain and numeric):
            self.failures.append(f"{label}: canon={exact} sympy={plain} numeric={numeric}")
        return exact and plain and numeric

    def detects(self, mine, wrong):
        """Negative control: does each method separately see that `wrong` differs from `mine`?"""
        diff = sp.sympify(mine) - sp.sympify(wrong)
        numeric = any(abs(self.points.evaluate(mine, pt) - self.points.evaluate(wrong, pt))
                      > sp.Float("1e-45", 60) * max(1, abs(self.points.evaluate(mine, pt)))
                      for pt in self.points.points)
        return (not is_zero(diff), not sympy_zero(diff), numeric)

    def summary(self):
        return (f"{self.count} comparisons ({self.nonzero} with a non-zero side): the difference vanishes exactly "
                f"by canon and by sympy expand/simplify, and at the 5 random points "
                f"({self.numeric_evaluations} evaluations, max relative deviation "
                f"{sp.Float(self.max_numeric, 3) if self.max_numeric else 0} at 60 digits); failures: "
                f"{self.failures[:5] if self.failures else 'none'}")


# ---------------------------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------------------------
class Recorder:
    def __init__(self):
        self.checks = {}

    def add(self, name, passed, detail):
        if name in self.checks:
            raise ValueError(f"duplicate check {name}")
        self.checks[name] = {"passed": bool(passed), "detail": detail}
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)


def run(artifacts: Path, timings: dict):
    rec = Recorder()
    t0 = time.perf_counter()

    def lap(name):
        timings[name] = time.perf_counter() - t0

    print("1. GKD (literal kdelta) self-test", flush=True)
    gkd_selftest(rec)
    lap("gkd_selftest")

    print("2. Normalisations derived on random algebraic curvature tensors", flush=True)
    derive_normalisations(rec)
    lap("normalisations")

    print("3. Geometry of the metric (sympy)", flush=True)
    geo = geometry(rec)
    rud = geo["rud"]
    lap("geometry")

    print("4. Lovelock sums with literal kdelta", flush=True)
    entries = [((a, b), (c, d), ring_from_symbol_form(v)) for (a, b, c, d), v in sorted(rud.items())]
    rm_ring = {(a, b, c, d): v for ((a, b), (c, d), v) in entries}
    P, L, counters = {}, {}, []
    for k in (1, 2, 3):
        Pk, Lk, cnt = lovelock_sums(entries, k, N, RING.zero, RING.one)
        P[k] = [[ring_normalise(x) for x in row] for row in Pk]
        L[k] = ring_normalise(Lk)
        counters.append(cnt)
        lap(f"lovelock_k{k}")
    for k in (1, 2):
        Pu, Lu, calls = lovelock_sums_unpruned(entries, k, N, RING.zero, RING.one)
        same = all(ring_equal(Pu[h][j], P[k][h][j]) for h in range(N) for j in range(N)) and ring_equal(Lu, L[k])
        rec.add(f"k{k}_unpruned_literal_sum_agrees", same,
                f"the completely unpruned literal sum ({len(entries)}^{k} ordered products of non-zero R^ab_cd x 64 (h, j) "
                f"+ the scalar: {calls} kdelta calls) equals the pruned sum exactly, for all 64 components and L_({k})")
        lap(f"unpruned_k{k}")
    rng = random.Random(77)
    sampled = skipped = 0
    nonzero_skipped = 0
    for _ in range(20000):
        ids = [rng.randrange(len(entries)) for _ in range(3)]
        h, j = rng.randrange(N), rng.randrange(N)
        lower = (j,) + tuple(x for i in ids for x in entries[i][0])
        upper = (h,) + tuple(x for i in ids for x in entries[i][1])
        sampled += 1
        if len(set(lower)) < 7 or len(set(upper)) < 7:
            skipped += 1
            if kdelta(lower, upper) != 0:
                nonzero_skipped += 1
    rec.add("k3_pruned_terms_vanish_literally", nonzero_skipped == 0 and skipped > 0,
            f"{sampled} random (3 non-zero R^ab_cd entries, h, j) terms of the unpruned k = 3 sum: {skipped} have a "
            f"repeated index (skipped by the enumeration) and kdelta gives 0 for every one of them (non-zero: {nonzero_skipped})")
    nonzero4 = 0
    for _ in range(300):
        ids = [rng.randrange(len(entries)) for _ in range(4)]
        h, j = rng.randrange(N), rng.randrange(N)
        lower = (j,) + tuple(x for i in ids for x in entries[i][0])
        upper = (h,) + tuple(x for i in ids for x in entries[i][1])
        if kdelta(lower, upper) != 0:
            nonzero4 += 1
    rec.add("k4_terms_vanish_literally", nonzero4 == 0,
            f"300 random (4 non-zero R^ab_cd entries, h, j) terms of P_(4): kdelta of the 9-index lists is 0 for every "
            f"one (non-zero: {nonzero4}); with 9 indices in 8 dimensions every term has a repeated index, so P_(4) = 0")
    lap("k3_k4_sampled")

    print("5. Independent routes and identities", flush=True)
    zero = RING.zero
    ric = ricci(rm_ring, N, zero)
    rs = trace(ric, N, zero)
    ok = all(ring_equal(P[1][h][j], -4 * ric[h][j] + (2 * rs if h == j else zero)) for h in range(N) for j in range(N))
    rec.add("k1_equals_minus_4_einstein", ok, "P_(1)^h_j = -4 G^h_j exactly (G = Ric - R/2 from the sympy Ricci tensor)")
    rec.add("L1_equals_2R", ring_equal(L[1], 2 * rs), "L_(1) = 2 R exactly")
    H2, gb = twice_gauss_bonnet_tensor(rm_ring, ric, rs, N, zero)
    ok = all(ring_equal(P[2][h][j], -4 * H2[h][j]) for h in range(N) for j in range(N))
    rec.add("k2_equals_minus_8_gauss_bonnet", ok,
            "P_(2)^h_j = -8 H^h_j exactly, H = classical Gauss-Bonnet (Lanczos) tensor; derivation in the module docstring")
    rec.add("L2_equals_4_gauss_bonnet", ring_equal(L[2], 4 * gb), "L_(2) = 4 (R^2 - 4 Ric.Ric + Riem.Riem) exactly")
    # The Gauss-Bonnet formula is written with R^{habc} R_{jabc}, R_ab R^ab, R_abcd R^abcd; the code uses the
    # mixed forms.  Check the index placement with the metric explicitly (symbol form, diagonal g).
    gsym = geo["gsym"]
    r_low = {key: gsym[key[0]] * gsym[key[1]] * v for key, v in rud.items()}        # R_abcd
    r_up = {key: v / (gsym[key[2]] * gsym[key[3]]) for key, v in rud.items()}       # R^abcd
    ric_sym = [[ring_to_symbol_form(ric[h][j]) for j in range(N)] for h in range(N)]
    place_ok = True
    for h in range(N):
        for j in range(N):
            explicit = sum((v * r_low.get((j, a, b, c), 0) for (hh, a, b, c), v in r_up.items() if hh == h), sp.Integer(0))
            mixed = sum((v * rud.get((b, c, j, a), 0) for (hh, a, b, c), v in rud.items() if hh == h), sp.Integer(0))
            place_ok &= is_zero(explicit - mixed)
    ric_low_up = sum((gsym[a] * ric_sym[a][b] * ric_sym[a][b] / gsym[b] for a in range(N) for b in range(N)), sp.Integer(0))
    ric_mixed = sum((ric_sym[a][b] * ric_sym[b][a] for a in range(N) for b in range(N)), sp.Integer(0))
    place_ok &= is_zero(ric_low_up - ric_mixed)
    riem_low_up = sum((v * r_up[key] for key, v in r_low.items()), sp.Integer(0))
    place_ok &= is_zero(riem_low_up - ring_to_symbol_form(riemann_square(rm_ring, zero)))
    rec.add("gauss_bonnet_index_placement", place_ok,
            "with g explicitly: R^{habc} R_{jabc} = R^{ha}_{bc} R^{bc}_{ja} (all 64 h, j), R_ab R^ab = R^a_b R^b_a and "
            "R_abcd R^abcd = R^ab_cd R^cd_ab exactly")
    T = cubic_invariants(rm_ring, ric, rs, N, zero)
    l3c = zero
    for coef, t in zip(CUBIC_COEFFICIENTS, T):
        l3c = l3c + coef * t
    rec.add("L3_equals_8_cubic_lovelock_density", ring_equal(L[3], 8 * l3c),
            "L_(3) = 8 (2 T1 + 8 T2 + 24 T3 + 3 T4 + 24 T5 + 16 T6 - 12 T7 + T8) exactly (coefficients derived in check normalisation_L3_cubic_derived)")
    for k in (1, 2, 3):
        tr = zero
        for h in range(N):
            tr = tr + P[k][h][h]
        rec.add(f"k{k}_trace_identity", ring_equal(tr, (N - 2 * k) * L[k]), f"sum_h P_({k})^h_h = (8 - {2 * k}) L_({k}) exactly")
    P_sym = {k: [[ring_to_symbol_form(P[k][h][j]) for j in range(N)] for h in range(N)] for k in (1, 2, 3)}
    P_fun = {k: [[to_function_form(P_sym[k][h][j]) for j in range(N)] for h in range(N)] for k in (1, 2, 3)}
    gamma = geo["gamma"]
    for k in (1, 2, 3):
        div_ok = True
        for j in range(N):
            v = sp.Integer(0)
            for h in range(N):
                v += sp.diff(P_fun[k][h][j], X[h])
                for e in range(N):
                    v += gamma[h][h][e] * P_fun[k][e][j] - gamma[e][h][j] * P_fun[k][h][e]
            div_ok &= is_zero(v)
        rec.add(f"k{k}_divergence_free", div_ok, f"nabla_h P_({k})^h_j = 0 exactly for j = x1..x8 (sympy diff + Christoffels)")
        sym_ok = all(is_zero(gsym[h] * P_sym[k][h][j] - gsym[j] * P_sym[k][j][h]) for h in range(N) for j in range(N))
        rec.add(f"k{k}_symmetric", sym_ok, f"g_hh P_({k})^h_j = g_jj P_({k})^j_h exactly, so A_({k})^lh = A_({k})^hl")
        free = all(not P_sym[k][h][j].has(s_) and not P_sym[k][h][j].has(E_) for h in range(N) for j in range(N))
        rec.add(f"k{k}_free_of_warp", free, f"every P_({k})^h_j is free of sin(6 H x8)^(1/3) and of e^(a4)")
    lap("routes")

    print("6. Comparison with the Rust output", flush=True)
    tensors_path = artifacts / "lovelock-tensors.json"
    curvature_path = artifacts / "curvature.json"
    tensors = json.loads(tensors_path.read_text(encoding="utf-8"))
    curv = json.loads(curvature_path.read_text(encoding="utf-8"))
    points = Points()
    sqrt_g = geo["sqrt_g"]
    gi = geo["gi"]
    A_fun = {}
    for k in (1, 2, 3):
        A_fun[k] = [[sp.Integer(0) for _ in range(N)] for _ in range(N)]
        for up_l in range(N):  # A_(k)^{lh} = sqrt|g| g^{jl} P_(k)^h_j
            for h in range(N):
                v = sp.Integer(0)
                for j in range(N):
                    if gi[j, up_l] != 0:
                        v += sqrt_g * gi[j, up_l] * P_fun[k][h][j]
                A_fun[k][up_l][h] = v
    text_ok = True
    text_count = 0
    for k in (1, 2, 3):
        for kind, mine_of, key in (("mixed", lambda a, b: P_fun[k][a][b], f"P{k}_mixed_up_h_down_j"),
                                   ("contravariant", lambda a, b: A_fun[k][a][b], f"A{k}_contravariant_l_h")):
            block = tensors[key]
            comp = Comparator(points)
            seen = set()
            for name, entry in block.items():
                a, b = index_pair(name)
                seen.add((a, b))
                theirs = from_monomials(entry["monomials"])
                comp.compare(f"{key}[{name}]", mine_of(a, b), theirs)
                text_count += 1
                text_ok &= is_zero(from_mathematica(entry["mathematica"]) - theirs)
            complete = seen == {(a, b) for a in range(N) for b in range(N)}
            what = "P_({k})^h_j" if kind == "mixed" else "A_({k})^lh"
            rec.add(f"rust_k{k}_{kind}_components_agree", complete and not comp.failures,
                    f"{what.format(k=k)}: all 64 components of {key} present; " + comp.summary())
        comp = Comparator(points)
        comp.compare(f"L{k}", to_function_form(ring_to_symbol_form(L[k])), from_mathematica(tensors[f"L{k}"]))
        rec.add(f"rust_L{k}_agrees", not comp.failures, f"L_({k}): " + comp.summary())

    def tampered(key, name, change):
        monomials = [[num, den, list(e)] for num, den, e in tensors[key][name]["monomials"]]
        change(monomials)
        return from_monomials(monomials)

    def bump(ms):
        ms[0][0] += 1

    def warp(ms):
        ms[0][2][6] -= 1

    def flip_e(ms):
        ms[0][2][5] = -ms[0][2][5]

    controls = [
        ("P3^x8_x8 with its first coefficient + 1", P_fun[3][7][7], tampered("P3_mixed_up_h_down_j", "x8,x8", bump)),
        ("A2^x1x1 with S^2 -> S^1 in its first monomial", A_fun[2][0][0], tampered("A2_contravariant_l_h", "x1,x1", warp)),
        ("A1^x5x5 with E^2 -> E^-2 in its first monomial", A_fun[1][4][4], tampered("A1_contravariant_l_h", "x5,x5", flip_e)),
        ("P2^x4_x4 + 10^-30 H^4", P_fun[2][3][3],
         from_monomials(tensors["P2_mixed_up_h_down_j"]["x4,x4"]["monomials"]) + sp.Rational(1, 10 ** 30) * H ** 4),
    ]
    neg = Comparator(points)
    found = [(label, neg.detects(mine, wrong)) for label, mine, wrong in controls]
    rec.add("negative_controls_detected", all(all(f) for _, f in found),
            "each of canon, plain sympy and the 60-digit numerics separately detects every tampered Rust component: "
            + "; ".join(f"{label}: {f}" for label, f in found))
    lap("compare_tensors")
    # curvature.json
    comp = Comparator(points)
    md = curv["metricDiagonal"]
    for i in range(N):
        comp.compare(f"metricDiagonal[{i}]", geo["diag"][i], from_mathematica(md[i]))
    comp.compare("sqrtAbsDetG", sqrt_g, from_mathematica(curv["sqrtAbsDetG"]))
    rec.add("rust_metric_and_sqrt_g_agree", len(md) == N and not comp.failures,
            "metricDiagonal (8 entries) and sqrtAbsDetG: " + comp.summary())
    comp = Comparator(points)
    rust_gamma = {}
    for item in curv["christoffelNonzero_b_le_c"]:
        rust_gamma[NAMES.index(item["a"]), NAMES.index(item["b"]), NAMES.index(item["c"])] = item["value"]
    mine_keys = {(a, b, c) for (a, b, c) in geo["gamma_canon"] if b <= c}
    same_set = mine_keys == set(rust_gamma)
    for key in sorted(mine_keys & set(rust_gamma)):
        a, b, c = key
        comp.compare(f"Gamma{key}", geo["gamma"][a][b][c], from_mathematica(rust_gamma[key]))
    rec.add("rust_christoffels_agree", same_set and not comp.failures,
            f"the {len(mine_keys)} non-zero Gamma^a_bc (b <= c) of sympy are exactly the {len(rust_gamma)} listed; " + comp.summary())
    comp = Comparator(points)
    rust_r = {}
    for item in curv["riemannMixedNonzero"]:
        up, down = item["up"], item["down"]
        rust_r[NAMES.index(up[0]), NAMES.index(up[1]), NAMES.index(down[0]), NAMES.index(down[1])] = item["value"]
    same_set = set(rud) == set(rust_r)
    for key in sorted(set(rud) & set(rust_r)):
        comp.compare(f"R{key}", to_function_form(rud[key]), from_mathematica(rust_r[key]))
    rec.add("rust_riemann_agrees", same_set and not comp.failures,
            f"the {len(rud)} non-zero R^ab_cd of sympy are exactly the {len(rust_r)} listed; " + comp.summary())
    comp = Comparator(points)
    ric_fun = [[to_function_form(ring_to_symbol_form(ric[h][j])) for j in range(N)] for h in range(N)]
    rs_fun = to_function_form(ring_to_symbol_form(rs))
    for name, entry in curv["ricciMixed"].items():
        h, j = index_pair(name)
        theirs = from_monomials(entry["monomials"])
        comp.compare(f"Ricci[{name}]", ric_fun[h][j], theirs)
        text_count += 1
        text_ok &= is_zero(from_mathematica(entry["mathematica"]) - theirs)
    for name, entry in curv["einsteinMixed"].items():
        h, j = index_pair(name)
        theirs = from_monomials(entry["monomials"])
        comp.compare(f"Einstein[{name}]", ric_fun[h][j] - (rs_fun / 2 if h == j else 0), theirs)
        text_count += 1
        text_ok &= is_zero(from_mathematica(entry["mathematica"]) - theirs)
    comp.compare("ricciScalar", rs_fun, from_mathematica(curv["ricciScalar"]))
    rec.add("rust_ricci_einstein_scalar_agree",
            len(curv["ricciMixed"]) == 64 and len(curv["einsteinMixed"]) == 64 and not comp.failures,
            "ricciMixed (64), einsteinMixed (64) from their monomials and ricciScalar: " + comp.summary())
    rec.add("rust_text_matches_monomials", text_ok,
            f"in all {text_count} components with monomial lists (lovelock-tensors.json and curvature.json), the "
            f"Mathematica text and the monomial list are the same expression exactly")
    lap("compare_curvature")

    results = {}
    for k in (1, 2, 3):
        results[f"P{k}_mixed_nonzero"] = {f"{NAMES[h]},{NAMES[j]}": sp.sstr(P_sym[k][h][j])
                                          for h in range(N) for j in range(N) if P_sym[k][h][j] != 0}
        results[f"L{k}"] = sp.sstr(ring_to_symbol_form(L[k]))
    results["sqrtAbsDetG"] = sp.sstr(sqrt_g)
    inputs = {name: sha256(artifacts / name) for name in ("curvature.json", "lovelock-tensors.json")}
    return rec, counters, results, inputs, points


def build_report(rec, counters, results, inputs, points):
    failed = [k for k, v in rec.checks.items() if not v["passed"]]
    return {
        "program": "scripts/check_lovelock_gkd.py",
        "purpose": "independent sympy verification of the Lovelock tensors P_(k)^h_j, A_(k)^lh (k = 1, 2, 3) and the "
                   "curvature computed by studies/lovelock_gkd (Rust, GKD); shares no code with the Rust crate",
        "conventions": {
            "riemann": "MTW: R^a_bcd = d_c Gamma^a_bd - d_d Gamma^a_bc + Gamma^a_ce Gamma^e_bd - Gamma^a_de Gamma^e_bc; "
                       "R^ab_cd = g^be R^a_ecd; R^h_j = R^ha_ja; G = Ric - R/2",
            "kdelta": "Det[Outer[delta, lower, upper]] with sympy Matrix.det, memoised by the 0/1 matrix",
            "lovelock": "P_(k)^h_j = kdelta[{j,j1..j2k},{h,h1..h2k}] R^{j1j2}_{h1h2}...; L_(k) = kdelta[{j1..},{h1..}] R...R; "
                        "A_(k)^lh = sqrt|g| g^jl P_(k)^h_j",
            "sqrtAbsDetG": "cos(6 H x8) (det g = cos^2(6 H x8); domain 0 < 6 H x8 < pi/2)",
            "symbols": "A1 = a4'(x4), A2 = a4''(x4), c = cot(6 H x8)",
        },
        "inputsSha256": inputs,
        "randomPoints": points.describe(),
        "counters": {"lovelockSums": counters, "kdeltaCallsTotal": KDELTA_STATS["calls"],
                     "distinctOuterMatricesDeterminedBySympy": KDELTA_STATS["sympyDeterminants"]},
        "independentResults": results,
        "checks": rec.checks,
        "checkCount": len(rec.checks),
        "failedCheckCount": len(failed),
        "failedChecks": failed,
        "verdict": "SUCCESS" if not failed else "FAILURE",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--artifacts", default=str(DEFAULT_ARTIFACTS), help="directory with the Rust JSON outputs")
    parser.add_argument("--report", default=None, help=f"output report (default: <artifacts>/{REPORT_NAME})")
    args = parser.parse_args(argv)
    artifacts = Path(args.artifacts)
    report_path = Path(args.report) if args.report else artifacts / REPORT_NAME
    timings: dict = {}
    start = time.perf_counter()
    rec, counters, results, inputs, points = run(artifacts, timings)
    report = build_report(rec, counters, results, inputs, points)
    text = json.dumps(report, indent=2, ensure_ascii=True) + "\n"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("run times (s, cumulative): " + ", ".join(f"{k} {v:.1f}" for k, v in timings.items()))
    print(f"total {time.perf_counter() - start:.1f} s; {report['checkCount']} checks, "
          f"{report['failedCheckCount']} failed; verdict {report['verdict']}; report {report_path}")
    return 0 if report["verdict"] == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
