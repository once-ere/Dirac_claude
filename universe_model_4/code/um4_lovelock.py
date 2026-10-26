#!/usr/bin/env python3
"""um4_lovelock.py - exact curvature and Lovelock tensors of a diagonal metric (a library of UM-4, the same as that of UM-3).

The Lovelock tensor of order p (the metric variation of the Lovelock density of order p) is

    E_(p)^a_b = -(1/2^(p+1)) delta^{a a1 b1 ... ap bp}_{b c1 d1 ... cp dp} R^{c1 d1}_{a1 b1} ... R^{cp dp}_{ap bp},

with the generalised Kronecker delta (the determinant of the matrix of Kronecker deltas).  For a diagonal metric the
frame components R^{cd}_{ab} are few, so the sum is evaluated exactly by enumerating the non-zero curvature factors:
every factor carries an unordered lower pair {a_j < b_j} and an unordered upper pair {c_j < d_j} (the four orderings of
each factor give the same contribution, a factor 4 each), the k factors are taken as an unordered set (a factor k!),
and the delta is +-1 when the upper index string is a permutation of the lower one.

Functions:
    frame_riemann(g, X, h)  -> {((c,d),(a,b)): expr}  with c<d, a<b, all non-zero frame components
    lovelock_tensor(Rf, p, n=8)          -> n x n sympy Matrix of the frame components E_(p)^a_b; the mixed
                                            coordinate components are E^M_N = (h_N/h_M) E^a_b (a = M, b = N)
    einstein_from_christoffel(...)       -> independent route for p = 1 (coordinate Ricci tensor)
"""
from __future__ import annotations

import itertools
import math

import sympy as sp


def christoffel(g, X):
    n = len(X)
    gi = sp.diag(*[1 / g[i, i] for i in range(n)])
    G = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for i in range(n):
            for j in range(n):
                val = gi[l, l] * (sp.diff(g[l, i], X[j]) + sp.diff(g[l, j], X[i]) - sp.diff(g[i, j], X[l])) / 2
                G[l][i][j] = sp.simplify(val)
    return G


def riemann_coord(g, X, G=None):
    """R^l_{i j k} = d_j G^l_{k i} - d_k G^l_{j i} + G^l_{j m} G^m_{k i} - G^l_{k m} G^m_{j i}
    (convention R^l_{ijk} V^i = [nabla_j, nabla_k] V^l)."""
    n = len(X)
    if G is None:
        G = christoffel(g, X)
    R = {}
    for l in range(n):
        for i in range(n):
            for j in range(n):
                for k in range(j + 1, n):
                    v = sp.diff(G[l][k][i], X[j]) - sp.diff(G[l][j][i], X[k])
                    for m in range(n):
                        v += G[l][j][m] * G[m][k][i] - G[l][k][m] * G[m][j][i]
                    v = sp.simplify(v)
                    if v != 0:
                        R[(l, i, j, k)] = v
                        R[(l, i, k, j)] = -v
    return R


def frame_riemann(g, X, h, simplify=sp.simplify):
    """Frame components R^{ab}_{cd} of a diagonal metric g = diag(eps_a h_a^2), orthonormal frame e^a = h_a dx^a.

    h: the list of the positive scale factors h_a (given explicitly, so that no absolute value is needed).
    Coordinate R^{MN}_{PQ} = R^M_{N P Q} / g_NN (diagonal metric) converts as R^{ab}_{cd} = R^{ab}_{cd}(coord) h_a h_b/(h_c h_d).
    Returned: dict {((a,b),(c,d)): value} with a<b, c<d and value != 0.
    """
    n = len(X)
    R = riemann_coord(g, X)
    out = {}
    for (l, i, j, k), v in R.items():
        if j >= k or l == i:
            continue
        up = v / g[i, i]
        a, b, sign = (l, i, 1) if l < i else (i, l, -1)
        val = simplify(sign * up * h[a] * h[b] / (h[j] * h[k]))
        if val == 0:
            continue
        key = ((a, b), (j, k))
        if key in out:
            if simplify(out[key] - val) != 0:
                raise RuntimeError(f"inconsistent component {key}: {out[key]} vs {val}")
        else:
            out[key] = val
    return out


def _perm_sign(src, dst):
    """Sign of the permutation taking the sequence src to the sequence dst (both of distinct elements)."""
    pos = {v: i for i, v in enumerate(src)}
    perm = [pos[v] for v in dst]
    sign = 1
    seen = [False] * len(perm)
    for i in range(len(perm)):
        if seen[i]:
            continue
        j, cyc = i, 0
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            cyc += 1
        if cyc % 2 == 0:
            sign = -sign
    return sign


def lovelock_tensor(Rf, p, n=8, simplify=sp.simplify):
    """E_(p)^a_b for all a, b from the frame components Rf = {((c,d),(a,b)): R^{cd}_{ab}} (c<d, a<b).

    E_(p)^a_b = -(1/2^(p+1)) sum delta^{a A}_{b C} prod R^{C_j}_{A_j}
              = -(1/2^(p+1)) * 4^p * p! * sum over unordered sets of p lower pairs (and their upper pairs).
    """
    by_lower = {}
    for (up, lo), v in Rf.items():
        by_lower.setdefault(lo, []).append((up, v))
    pairs = sorted(by_lower)
    E = sp.zeros(n, n)
    pref = sp.Rational(-(4 ** p) * math.factorial(p), 2 ** (p + 1))
    for a in range(n):
        for combo in itertools.combinations(pairs, p):
            idx = [a]
            for lo in combo:
                idx += list(lo)
            if len(set(idx)) != len(idx):
                continue
            lower_seq = idx
            lowset = set(idx)
            for choice in itertools.product(*[by_lower[lo] for lo in combo]):
                upper = []
                for up, _ in choice:
                    upper += list(up)
                if len(set(upper)) != len(upper):
                    continue
                rest = lowset - set(upper)
                if len(rest) != 1:
                    continue
                b = rest.pop()
                upper_seq = [b] + upper
                s = _perm_sign(lower_seq, upper_seq)
                term = sp.S(s)
                for _, v in choice:
                    term *= v
                E[a, b] += pref * term
    return E.applyfunc(simplify)


def lovelock_density(Rf, p, n=8, simplify=sp.simplify):
    """L_(p) = (1/2^p) delta^{A}_{C} prod R^{C_j}_{A_j} = (4^p p!/2^p) sum over unordered sets of p lower pairs."""
    by_lower = {}
    for (up, lo), v in Rf.items():
        by_lower.setdefault(lo, []).append((up, v))
    pairs = sorted(by_lower)
    pref = sp.Rational((4 ** p) * math.factorial(p), 2 ** p)
    tot = sp.S(0)
    for combo in itertools.combinations(pairs, p):
        idx = []
        for lo in combo:
            idx += list(lo)
        if len(set(idx)) != len(idx):
            continue
        for choice in itertools.product(*[by_lower[lo] for lo in combo]):
            upper = []
            for up, _ in choice:
                upper += list(up)
            if set(upper) != set(idx):
                continue
            s = _perm_sign(idx, upper)
            term = sp.S(s)
            for _, v in choice:
                term *= v
            tot += pref * term
    return simplify(tot)


def einstein_coordinate(g, X):
    """Mixed Einstein tensor G^M_N = R^M_N - delta R/2 from the coordinate Ricci tensor (independent route)."""
    n = len(X)
    R = riemann_coord(g, X)
    Ric = sp.zeros(n, n)
    for (l, i, j, k), v in R.items():
        if l == j:
            Ric[i, k] += v
    Ric = Ric.applyfunc(sp.simplify)
    mixed = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            mixed[a, b] = sp.simplify(Ric[a, b] / g[a, a])
    Rs = sp.simplify(sum(mixed[a, a] for a in range(n)))
    G = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            G[a, b] = sp.simplify(mixed[a, b] - (Rs / 2 if a == b else 0))
    return G, Rs
