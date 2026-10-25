#!/usr/bin/env python3
"""um3_geometry.py - exact geometry of the author's UM-3 metric (2026-10-24) and its Einstein-Lovelock equations.

The metric (author, b4 -> b4^2; z = 6 H x0; S = (Sin[z]^2)^(1/6), the positive branch):
    g = diag(Cot[z]^2, e^{2 a4} S, e^{2 a4} S, e^{2 a4} S, -1, -e^{-2 a4} b4^2 S, -e^{-2 a4} b4^2 S, -e^{-2 a4} b4^2 S)
with a4 = a4(x4), b4 = b4(x4) > 0 general functions of the time x4.

Computed exactly (sympy) on the quarter 0 < z < pi/2 and, for the signs, also on pi/2 < z < pi:
  G1  the vielbein, sqrt|g|, the y chart;
  G2  every non-zero frame component R^{ab}_{cd} (they do not depend on x0);
  G3  the Lovelock tensors E_(1), E_(2), E_(3) (frame components) by the combinatorial generalised-delta sum, and
      independently: E_(1) from the coordinate Ricci tensor, the trace identity E_(p)^a_a = -(8-2p)/2 L_(p) with L_(p)
      from its own sum, the contracted Bianchi identity nabla_M E_(p)^M_N = 0, E_(2) from the explicit Gauss-Bonnet
      tensor at random numerical points;
  G4  the field equations sum_p alpha_p E_(p) + Lambda = kappa T with the author's weights w = (1, 1/32, 1/1152),
      alpha_p = w_p H^(2-2p), Lambda = -10 H^2, in the dimensionless variables A = a4'/H, U = b4'/(H b4),
      Ad = a4''/H^2, Ud = U'/H; the author's vacuum (a4 = H x4, b4 constant); the off-diagonal (x0, x4) equation
      and its factorisation; the energy constraint and where positive energy density is possible; the branches
      with a diagonal source; the frozen extra times; the null energy condition;
  G5  the canonical spin connection of dirac16complex with the author's matrices T16^A and gamma^M Omega_M.
Writes outputs/geometry.json and reports/geometry_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_geometry.py
"""
from __future__ import annotations

import itertools
import json
import math
import random
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402
from um3_lovelock import (frame_riemann, lovelock_tensor, lovelock_density, einstein_coordinate,  # noqa: E402
                          christoffel, riemann_coord)


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


X = sp.symbols('x0:8', real=True)
H = sp.Symbol('H', positive=True)
x4 = X[4]
a4 = sp.Function('a4')(x4)
b4 = sp.Function('b4')(x4)
z = 6 * H * X[0]
A, U, Ad, Ud = sp.symbols('A U Ad Ud', real=True)
W = [None, sp.Integer(1), sp.Rational(1, 32), sp.Rational(1, 1152)]
ALPHA = [None, sp.Integer(1), W[2] / H**2, W[3] / H**4]
LAMBDA = -10 * H**2
NAMES = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']


def is_zero(expr, ntest=6, seed=7):
    """Exact zero test: sympy simplification first; if that does not reduce the expression to 0 (trigonometric
    identities in x0 are not always found), evaluate it with 40 significant digits at random points of the quarter
    0 < z < pi/2 for random H, a4, b4 and derivatives; zero if every value is below 1e-25 times its scale."""
    e = sp.simplify(expr)
    if e == 0:
        return True
    e = to_AU(e) if (e.has(a4) or e.has(b4)) else e
    rng = random.Random(seed)
    a4s, b4s = sp.Symbol('a4s'), sp.Symbol('b4s', positive=True)
    e = e.subs({a4: a4s, b4: b4s})
    for _ in range(ntest):
        Hv = sp.Rational(rng.randint(50, 150), 100)
        zv = sp.Rational(rng.randint(5, 150), 100)          # z in (0.05, 1.5) < pi/2
        vals = {H: Hv, X[0]: zv / (6 * Hv), A: sp.Rational(rng.randint(-100, 100), 77), U: sp.Rational(rng.randint(-100, 100), 81),
                Ad: sp.Rational(rng.randint(-100, 100), 83), Ud: sp.Rational(rng.randint(-100, 100), 89),
                a4s: sp.Rational(rng.randint(-100, 100), 97), b4s: sp.Rational(rng.randint(10, 300), 101)}
        for xx in X:
            vals.setdefault(xx, sp.Rational(rng.randint(-100, 100), 103))
        v = sp.N(e.subs(vals), 40)
        if abs(v) > 1e-25:
            return False
    return True


def metric(quarter=1):
    """The author's metric written for one quarter of the cell: quarter 1 is 0 < z < pi/2 (sin z > 0, cot z > 0),
    quarter 2 is pi/2 < z < pi (sin z > 0, cot z < 0).  The positive scale factors h_a are returned with it."""
    s = sp.sin(z)
    S = s**sp.Rational(1, 3)
    g = sp.diag(sp.cot(z)**2, *[sp.exp(2 * a4) * S] * 3, -1, *[-sp.exp(-2 * a4) * b4**2 * S] * 3)
    h0 = sp.cot(z) if quarter == 1 else -sp.cot(z)
    h = [h0] + [sp.exp(a4) * s**sp.Rational(1, 6)] * 3 + [sp.S(1)] + [sp.exp(-a4) * b4 * s**sp.Rational(1, 6)] * 3
    return g, h


def to_AU(expr):
    """Replace the derivatives of a4, b4 by the dimensionless variables A, U, Ad, Ud (b4 itself cancels)."""
    e = expr.subs(sp.Derivative(b4, (x4, 2)), b4 * (Ud * H**2 + U**2 * H**2))
    e = e.subs(sp.Derivative(a4, (x4, 2)), Ad * H**2)
    e = e.subs(sp.Derivative(b4, x4), U * H * b4)
    e = e.subs(sp.Derivative(a4, x4), A * H)
    return sp.simplify(e)


def gauss_bonnet_tensor_numeric(Rf_num, n=8):
    """E_(2)^a_b from the explicit Gauss-Bonnet tensor (frame, eta = diag):  H_ab = 2(R R_ab - 2 R_ac R^c_b
    - 2 R_acbd R^cd + R_a^cde R_bcde) - (1/2) eta_ab L_GB, with E_(2)^a_b = H^a_b (the variation of sqrt|g| L_GB)."""
    import numpy as np
    eta = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(float)
    R = np.zeros((n, n, n, n))  # R^{ab}_{cd}
    for ((a, b), (c, d)), v in Rf_num.items():
        for (p, q, s1) in ((a, b, 1), (b, a, -1)):
            for (r, t, s2) in ((c, d, 1), (d, c, -1)):
                R[p, q, r, t] = s1 * s2 * v
    # all-lower R_{abcd} = eta_aa eta_bb R^{ab}_{cd}
    Rl = np.einsum('ae,bf,efcd->abcd', eta, eta, R)
    Ric = np.einsum('abcb->ac', np.einsum('ae,ebcd->abcd', eta, R))  # R_{ac} = R^b_{a b c}... use R^{ab}_{cb}
    # careful construction: R_ac = R^b_{abc}; R^b_{abc} = eta_aa R^{ba}_{bc} with sign: R^{ab}_{cd} is antisymmetric
    Ric = np.zeros((n, n))
    for a_ in range(n):
        for c_ in range(n):
            Ric[a_, c_] = sum(R[b_, a_, b_, c_] for b_ in range(n)) * eta[a_, a_]  # R_{ac} = eta_aa R^{ba}_{bc}
    Rs = sum(Ric[a_, a_] * eta[a_, a_] for a_ in range(n))
    Ricu = eta @ Ric  # R^a_c
    Ricuu = eta @ Ric @ eta
    LGB = Rs**2 - 4 * np.einsum('ab,ab->', Ric, Ricuu) + np.einsum('abcd,abcd->', Rl, np.einsum('ae,bf,cg,dh,efgh->abcd', eta, eta, eta, eta, Rl))
    Hab = np.zeros((n, n))
    Rluu = np.einsum('abcd,ce,df->abef', Rl, eta, eta)
    for a_ in range(n):
        for b_ in range(n):
            t1 = Rs * Ric[a_, b_]
            t2 = sum(Ric[a_, c_] * Ricu[c_, b_] for c_ in range(n))
            t3 = sum(Rl[a_, c_, b_, d_] * Ricuu[c_, d_] for c_ in range(n) for d_ in range(n))
            t4 = np.einsum('cde,cde->', np.einsum('cde->cde', np.einsum('cf,dg,eh,fgh->cde', eta, eta, eta, Rl[a_])), Rl[b_])
            Hab[a_, b_] = 2 * (t1 - 2 * t2 - 2 * t3 + t4) - 0.5 * eta[a_, b_] * LGB
    return eta @ Hab, LGB  # mixed H^a_b


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- G1: metric, vielbein, sqrt|g|
    g, h = metric(1)
    sqrtg = sp.simplify(sp.prod(h))
    ok = sp.simplify(sqrtg - b4**3 * sp.cos(z)) == 0
    rep.check('G1_sqrt_det', ok, 'sqrt|g| = b4^3 cos z on 0 < z < pi/2 (b4^3 |cos z| on the whole cell); a4 cancels')
    eps = [1, 1, 1, 1, -1, -1, -1, -1]
    ok = all(is_zero(h[i]**2 - eps[i] * g[i, i]) for i in range(8))
    rep.check('G1_vielbein', ok, 'g = diag(eps_a h_a^2), h = (|cot z|, e^{a4} S^{1/2} (x3), 1, e^{-a4} b4 S^{1/2} (x3))')
    # y chart: y = ln|sin z|/(6H), dy = cot z dx0, S = e^{2 H y}
    yv = sp.Symbol('y', real=True)
    ok = sp.simplify(sp.diff(sp.log(sp.sin(z)) / (6 * H), X[0]) - sp.cot(z)) == 0
    rep.check('G1_y_chart', ok, 'y = ln|sin z|/(6H): dy = cot z dx0, so g00 dx0^2 = dy^2 and S = e^{2Hy}: '
              'ds^2 = dy^2 + e^{2Hy}(e^{2a4} dx_i^2 - e^{-2a4} b4^2 dx_t^2) - dx4^2, sqrt|g| = b4^3 e^{6Hy}')

    # ---------------- G2: frame curvature
    Rf = frame_riemann(g, X, h)
    Rau = {k: to_AU(v) for k, v in Rf.items()}
    free_x0 = all(not v.has(X[0]) for v in Rau.values())
    rep.check('G2_curvature_free_of_x0', free_x0, '%d non-zero frame components R^{ab}_{cd} (a<b, c<d), none depends on x0' % len(Rf))
    sec = {}
    mixed = {}
    for ((a, b), (c, d)), v in Rau.items():
        if (a, b) == (c, d):
            sec[(a, b)] = v
        else:
            mixed[((a, b), (c, d))] = v
    expect_sec = {
        'R^{0i}_{0i}': (sec[(0, 1)], -H**2), 'R^{0t}_{0t}': (sec[(0, 5)], -H**2),
        'R^{ij}_{ij}': (sec[(1, 2)], H**2 * (A**2 - 1)), 'R^{i4}_{i4}': (sec[(1, 4)], H**2 * (A**2 + Ad)),
        'R^{it}_{it}': (sec[(1, 5)], H**2 * (-1 - A**2 + A * U)),
        'R^{4t}_{4t}': (sec[(4, 5)], H**2 * ((U - A)**2 + Ud - Ad)),
        'R^{tt}_{tt}': (sec[(5, 6)], H**2 * ((U - A)**2 - 1)),
    }
    ok = all(sp.simplify(v - e) == 0 for v, e in expect_sec.values()) and (0, 4) not in sec
    rep.check('G2_sectional_curvatures', ok, '; '.join('%s = %s' % (k, sp.factor(e)) for k, (v, e) in expect_sec.items()) + '; R^{04}_{04} = 0')
    ok = sp.simplify(mixed[((0, 1), (1, 4))] - H**2 * A) == 0 and sp.simplify(mixed[((0, 5), (4, 5))] - H**2 * (A - U)) == 0
    allmixed = all(((a, b), (c, d)) in mixed for (a, b, c, d) in [(0, 1, 1, 4), (0, 2, 2, 4), (0, 3, 3, 4), (0, 5, 4, 5), (0, 6, 4, 6), (0, 7, 4, 7)])
    rep.check('G2_mixed_components', ok and allmixed and len(mixed) == 12,
              'the only other components: R^{0i}_{4i} = R^{4i}_{0i} sign = H^2 A (i = x1, x2, x3) and R^{0t}_{4t} = H^2 (A - U) '
              '(t = x5, x6, x7), with the frame of x0 oriented along cot z (12 components counting both pair orders)')
    out['frame_curvature'] = {('R^{%s}_{%s}' % (''.join(NAMES[i] for i in k[0]), ''.join(NAMES[i] for i in k[1]))): str(sp.factor(v))
                              for k, v in Rau.items()}

    # ---------------- G3: Lovelock tensors
    E = {p: lovelock_tensor(Rf, p) for p in (1, 2, 3)}
    Eau = {p: E[p].applyfunc(to_AU) for p in (1, 2, 3)}
    nz = {p: sorted({(a, b) for a in range(8) for b in range(8) if Eau[p][a, b] != 0}) for p in (1, 2, 3)}
    diag_ok = all(set(nz[p]) == {(a, a) for a in range(8)} | {(0, 4), (4, 0)} for p in (1, 2, 3))
    rep.check('G3_structure', diag_ok, 'every E_(p) has only the diagonal components and the (x0, x4) pair')
    sym_ok = all(sp.simplify(Eau[p][1, 1] - Eau[p][i, i]) == 0 for p in (1, 2, 3) for i in (2, 3)) and \
        all(sp.simplify(Eau[p][5, 5] - Eau[p][t, t]) == 0 for p in (1, 2, 3) for t in (6, 7))
    rep.check('G3_isotropy', sym_ok, 'E^{x1}_{x1} = E^{x2}_{x2} = E^{x3}_{x3} and E^{x5}_{x5} = E^{x6}_{x6} = E^{x7}_{x7} for every p')
    ok = all(not Eau[p][a, b].has(X[0]) for p in (1, 2, 3) for a in range(8) for b in range(8))
    rep.check('G3_free_of_x0', ok, 'no frame component of E_(1), E_(2), E_(3) depends on x0')
    # independent route p = 1
    Gc, Rs = einstein_coordinate(g, X)
    ok = True
    for a in range(8):
        for b in range(8):
            frame_from_coord = sp.simplify(Gc[a, b] * h[a] / h[b])
            if not is_zero(to_AU(frame_from_coord) - Eau[1][a, b]):
                ok = False
    rep.check('G3_einstein_two_routes', ok, 'E_(1) from the generalised delta equals R^M_N - delta R/2 from the coordinate Ricci tensor (converted to the frame)')
    # trace identity
    ok = True
    for p in (1, 2, 3):
        L = to_AU(lovelock_density(Rf, p))
        tr = sp.simplify(sum(Eau[p][a, a] for a in range(8)))
        if sp.simplify(tr + sp.Rational(8 - 2 * p, 2) * L) != 0:
            ok = False
        out.setdefault('lovelock_density', {})[str(p)] = str(sp.factor(L))
    rep.check('G3_trace_identity', ok, 'E_(p)^a_a = -(8 - 2p)/2 L_(p) for p = 1, 2, 3 with L_(p) from its own sum')
    # Bianchi identity in coordinates: nabla_M E^M_N = d_M E^M_N + G^M_{ML} E^L_N - G^L_{MN} E^M_L
    Gm = christoffel(g, X)
    ok = True
    for p in (1, 2, 3):
        Ec = sp.zeros(8, 8)
        for a in range(8):
            for b in range(8):
                Ec[a, b] = E[p][a, b] * h[b] / h[a]   # coordinate mixed components
        for N in range(8):
            div = 0
            for M in range(8):
                div += sp.diff(Ec[M, N], X[M])
                for Lx in range(8):
                    div += Gm[M][M][Lx] * Ec[Lx, N] - Gm[Lx][M][N] * Ec[M, Lx]
            if not is_zero(div):
                ok = False
                print('   Bianchi fails p=%d N=%d' % (p, N))
    rep.check('G3_bianchi_identity', ok, 'nabla_M E_(p)^M_N = 0 identically (all N, p = 1, 2, 3) for general a4(x4), b4(x4)')
    # explicit Gauss-Bonnet tensor at random points
    import numpy as np
    rng = random.Random(20261024)
    ok = True
    for trial in range(4):
        vals = {H: rng.uniform(0.5, 1.5)}
        subsA = {A: rng.uniform(-1, 1), U: rng.uniform(-1, 1), Ad: rng.uniform(-1, 1), Ud: rng.uniform(-1, 1)}
        Rnum = {k: float(v.subs(subsA).subs(vals)) for k, v in Rau.items()}
        Hm, LGB = gauss_bonnet_tensor_numeric(Rnum)
        E2n = np.array(Eau[2].subs(subsA).subs(vals).evalf(), dtype=float)
        if not np.allclose(Hm, E2n, atol=1e-9 * max(1, abs(E2n).max())):
            ok = False
            print('   GB mismatch', np.abs(Hm - E2n).max())
    rep.check('G3_gauss_bonnet_explicit', ok, 'E_(2) equals the explicit Gauss-Bonnet tensor 2(R R_ab - 2R_ac R^c_b - 2R_acbd R^cd + R_a^cde R_bcde) - eta_ab L_GB/2 at 4 random points')
    out['lovelock_tensors'] = {'E%d' % p: {'%s,%s' % (NAMES[a], NAMES[b]): str(sp.factor(Eau[p][a, b] / H**(2 * p)))
                                           for (a, b) in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4), (4, 0)]} for p in (1, 2, 3)}

    # quarter 2: the same frame components with the orientation of the x0 frame reversed
    g2, h2 = metric(2)
    Rf2 = frame_riemann(g2, X, h2)
    ok = True
    for k, v in Rf2.items():
        v1 = Rf.get(k)
        odd = (k[0].count(0) + k[1].count(0)) % 2 == 1
        if v1 is None or sp.simplify(to_AU(v) - (-1 if odd else 1) * to_AU(v1)) != 0:
            ok = False
    E2q = {p: lovelock_tensor(Rf2, p).applyfunc(to_AU) for p in (1, 2, 3)}
    ok2 = all(sp.simplify(E2q[p][a, b] - (-1 if (a == 0) != (b == 0) else 1) * Eau[p][a, b]) == 0 for p in (1, 2, 3) for a in range(8) for b in range(8))
    rep.check('G3_second_quarter', ok and ok2, 'on pi/2 < z < pi (cot z < 0, h0 = -cot z) every component is the same except that those with one x0 frame index change sign (the fold reflection)')

    # ---------------- G4: field equations
    LHS = sp.zeros(8, 8)
    for a in range(8):
        for b in range(8):
            LHS[a, b] = sp.factor(sp.expand(sum(ALPHA[p] * Eau[p][a, b] for p in (1, 2, 3)) / H**2 + (LAMBDA / H**2 if a == b else 0)))
    out['field_equations_lhs_over_H2'] = {'%s,%s' % (NAMES[a], NAMES[b]): str(LHS[a, b]) for (a, b) in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4), (4, 0)]}
    vac = {A: 1, U: 0, Ad: 0, Ud: 0}
    ok = all(sp.simplify(LHS[a, b].subs(vac)) == 0 for a in range(8) for b in range(8))
    rep.check('G4_author_vacuum', ok, "a4 = H x4, b4 constant (A = 1, U = 0) solves the vacuum equations with w = (1, 1/32, 1/1152), Lambda = -10 H^2 (the author's eternal inflation/deflation, Dirac_Einstein-Lovelock_4+4_Nash.nb In[134])")
    Gpoly = 5 * A**4 - 10 * A**3 * U + 5 * A**2 * U**2 - 6 * A**2 + 6 * A * U + U**2 + 1
    ok = sp.simplify(LHS[0, 4] - (-sp.Rational(3, 16) * U * Gpoly)) == 0 and sp.simplify(LHS[4, 0] + LHS[0, 4]) == 0
    rep.check('G4_offdiagonal_factor', ok, 'the (x0, x4) equation: -(3/16) U G(A, U) H^2 = kappa T^{x0}_{x4} with G = 5A^2(A - U)^2 - 6A^2 + 6AU + U^2 + 1')
    # energy constraint near the vacuum
    dlt = sp.Symbol('delta', real=True)
    P44 = sp.expand(LHS[4, 4])
    quad = sp.expand(sp.series(P44.subs(A, 1 + dlt).subs(U, sp.Symbol('eps') * U).subs(dlt, sp.Symbol('eps') * dlt), sp.Symbol('eps'), 0, 3).removeO().subs(sp.Symbol('eps'), 1))
    ok = sp.simplify(quad - sp.Rational(3, 4) * ((dlt - U)**2 + dlt**2)) == 0
    rep.check('G4_vacuum_degenerate', ok, 'near the vacuum the energy constraint is kappa rho = -H^2 P44, P44 = (3/4)[(delta - U)^2 + delta^2] + O(3), delta = A - 1: '
              'the linear terms vanish (the effective Newton constant is zero at the vacuum) and kappa rho <= 0 to second order')
    ok = sp.simplify(P44.subs(U, 0) - (A**2 - 1)**2 * (5 * A**2 + 1) / 16) == 0
    rep.check('G4_constant_b4', ok, 'with b4 constant: P44 = (A^2 - 1)^2 (5A^2 + 1)/16 >= 0, so kappa rho <= 0 for every expansion rate')
    # branches with a diagonal source: G(A, U) = 0
    Ubr = sp.solve(sp.Eq(Gpoly, 0), U)
    disc = sp.factor(sp.discriminant(Gpoly, U))
    ok = sp.simplify(disc + 4 * (5 * A**4 - 10 * A**2 + 1)) == 0 and set(sp.simplify(u.subs(A, 1)) for u in Ubr) == {0, sp.Rational(2, 3)}
    amin = sp.sqrt(1 - 2 / sp.sqrt(5))
    amax = sp.sqrt(1 + 2 / sp.sqrt(5))
    rep.check('G4_diagonal_source_branches', ok, 'G(A, U) = 0 has real roots U only for 5A^4 - 10A^2 + 1 <= 0, i.e. %.4f <= |A| <= %.4f; at A = 1 the roots are U = 0 and U = 2/3'
              % (float(amin), float(amax)))
    src = {k: sp.simplify(LHS[k].subs({A: 1, U: sp.Rational(2, 3), Ad: 0, Ud: 0})) for k in [(0, 0), (1, 1), (4, 4), (5, 5)]}
    ok = src == {(0, 0): -sp.Rational(14, 27), (1, 1): -sp.Rational(2, 9), (4, 4): sp.Rational(2, 27), (5, 5): -sp.Rational(22, 27)}
    rep.check('G4_branch_A1_U23', ok, 'a4 = H x4, b4 = b4(0) e^{2 H x4/3}: kappa T = (x0, x1, x4, x5) = (-14/27, -2/9, 2/27, -22/27) H^2 (constant): '
              'kappa rho = -2/27 H^2 < 0 and kappa (rho + p_1) = -8/27 H^2 < 0')
    # frozen extra times: U = A (e^{-a4} b4 constant)
    fro = {k: sp.factor(LHS[k].subs({U: A, Ud: Ad})) for k in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4)]}
    ok = sp.simplify(fro[(4, 4)] + (3 * A**2 - 1) / 16) == 0 and sp.simplify(fro[(0, 4)] + 3 * A * (A**2 + 1) / 16) == 0
    nec = sp.factor(fro[(1, 1)] - fro[(4, 4)])
    ok2 = sp.simplify(nec + (6 * A**2 + 2 * Ad + 6) / 16) == 0
    rep.check('G4_frozen_extra_times', ok and ok2, 'with e^{-a4} b4 constant (U = A): kappa rho = (3A^2 - 1) H^2/16, kappa T^{x0}_{x4} = -(3/16) A (1 + A^2) H^2 and '
              'kappa(rho + p_1) = -(6 + 6A^2 + 2Ad) H^2/16 < 0 (the null energy condition is violated unless a4'' < -3(1 + A^2) H^2)')
    out['frozen_extra_times'] = {'%s,%s' % (NAMES[k[0]], NAMES[k[1]]): str(v) for k, v in fro.items()}
    # where can rho > 0: numerical map
    import numpy as np
    f44 = sp.lambdify((A, U), P44, 'numpy')
    Uthr = []
    for Av in [0.0, 0.1, 0.3, 0.5, 1 / math.sqrt(3), 1.0, 1.5, 2.0]:
        us = np.linspace(0, 6, 60001)
        vals = f44(Av, us)
        pos = us[vals < 0]
        Uthr.append((Av, float(pos[0]) if len(pos) else None))
    out['positive_energy_threshold_U_ge_0'] = Uthr
    rep.check('G4_positive_energy_needs_fast_b4', all(t is not None and t > 0.45 for _, t in Uthr),
              'for U >= 0, kappa rho > 0 needs U above %s at A = %s: b4 must change at a rate of order H' % ([round(t, 3) for _, t in Uthr], [round(a_, 3) for a_, _ in Uthr]))
    ok = sp.simplify(P44.subs(A, 0) + (3 * U**2 - 1) / 16) == 0
    rep.check('G4_static_space', ok, 'static 3-space (A = 0): kappa rho = (3U^2 - 1) H^2/16, positive only for |b4\'/b4| > H/sqrt 3')

    # ---------------- G5: the canonical spin connection
    T = GM.T16A()
    eta = GM.eta4488()
    # vielbein e^a_M = h_a delta^a_M; spin connection omega_{M ab} from de^a + omega^a_b e^b = 0 for a diagonal frame:
    # omega_{M ab} = e_a^N (d_M e_bN - Gamma^P_{MN} e_bP)  (lowered frame index b: e_bN = eta_bb h_b delta_bN)
    om = {}
    for M in range(8):
        for a in range(8):
            for b in range(8):
                val = 0
                N = a
                eb_N = lambda Nn: eta[b, b] * h[b] if Nn == b else 0
                term = sp.diff(eb_N(N), X[M]) - sum(Gm[P][M][N] * eb_N(P) for P in range(8))
                val = term / h[a]
                val = sp.simplify(val)
                if val != 0:
                    om[(M, a, b)] = val
    ok = all(sp.simplify(om.get((M, a, b), 0) + om.get((M, b, a), 0)) == 0 for M in range(8) for a in range(8) for b in range(8))
    rep.check('G5_spin_connection_antisymmetric', ok, 'omega_{M ab} = -omega_{M ba} (metric compatibility)')
    S = GM.SAB()
    Omega = {}
    for M in range(8):
        Om = sp.zeros(16, 16)
        for a in range(8):
            for b in range(8):
                if (M, a, b) in om:
                    Om += sp.Rational(1, 2) * om[(M, a, b)] * eta[a, a] * eta[b, b] * S[(a, b)]
        Omega[M] = Om.applyfunc(sp.simplify)
    # gamma^M = e_a^M T^a with T^a = eta^aa T_a
    gOm = sp.zeros(16, 16)
    for M in range(8):
        gOm += (eta[M, M] * T[M] / h[M]) * Omega[M]
    gOm = gOm.applyfunc(lambda e: sp.simplify(to_AU(e)))
    target = 3 * H * T[0] + sp.Rational(3, 2) * U * H * eta[4, 4] * T[4]
    ok = (gOm - target).applyfunc(sp.simplify) == sp.zeros(16, 16)
    rep.check('G5_gamma_Omega', ok, 'gamma^M Omega_M = 3H T^(x0) + (3/2)(b4\'/b4) T^(x4) on 0 < z < pi/2 (T^a = eta^aa T_a; on the second half the first term is -3H T^(x0) '
              'with the frame of x0 along cot z): the gravitational coupling of dirac16complex through the canonical spin connection is never identically zero (H > 0)')
    # covariant constancy of the gammas: D_M gamma^N = d_M gamma^N + Gamma^N_{MP} gamma^P + [Omega_M, gamma^N] = 0
    ok = True
    for M in range(8):
        for N in range(8):
            gN = eta[N, N] * T[N] / h[N]
            expr = sp.diff(gN, X[M]) + sum((Gm[N][M][P] * (eta[P, P] * T[P] / h[P]) for P in range(8)), sp.zeros(16, 16)) + Omega[M] * gN - gN * Omega[M]
            if not all(is_zero(e_) for e_ in expr if e_ != 0):
                ok = False
                break
        if not ok:
            break
    rep.check('G5_vielbein_postulate', ok, 'D_M gamma^N = 0 (the gamma matrices are covariantly constant with the canonical spin connection)')
    out['spin_connection_gamma_Omega'] = '3 H T^(x0) + (3/2) (b4\'/b4) T^(x4) (first half of the cell)'

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs').mkdir(exist_ok=True)
    (UM3 / 'reports').mkdir(exist_ok=True)
    (UM3 / 'outputs' / 'geometry.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_geometry.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'geometry_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
