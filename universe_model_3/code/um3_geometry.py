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
  G4  the field equations sum_p alpha_p E_(p) + Lambda = kappa T with the corrected weights w = (1, 1/20, 1/360),
      alpha_p = w_p H^(2-2p), Lambda = -7 H^2 (the unique values for which the graviton of the fold travels at the
      speed of light and the static bulk has no linear graviton, um3_weights.py; the author's original values were w = (1, 1/32, 1/1152), Lambda = -10 H^2), in the dimensionless
      variables A = a4'/H, U = b4'/(H b4), Ad = a4''/H^2, Ud = U'/H: the static block, every history with frozen extra
      times and every history with static ordinary space are vacua; the two constraints; the author's vacuum (a4 = H x4,
      b4 constant) is not a vacuum any more; the vacua with constant rates;
  G5  the canonical spin connection of dirac16complex with the author's matrices T16^A and gamma^M Omega_M.
Writes outputs/geometry.json and reports/geometry_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_geometry.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one surface of F, at z = pi/2: F is the union of these copies, one per period (example 2), and "the
fold" without a qualifier is the copy in the period that contains our world. A point of the fold is labelled by the seven
coordinates x1, ..., x7, and the metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.
Notation: ln is the natural logarithm, e Euler's number, exp(y) = e^y, sin, cos and cot = cos/sin the trigonometric
functions, tanh the hyperbolic tangent, |y| the absolute value; f(0+) and f(0-) are the limits of f(sigma) as sigma
approaches 0 from above and from below.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. The function W(sigma) = e^(-2 H |sigma|), which multiplies the squared steps of
ordinary space and of the extra times, is the warp factor of the metric (its square root e^(-H |sigma|) multiplies the
lengths); the time x4 is not warped. Four properties make the surface sigma = 0 a fold, and together they single it out
within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp factor is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|) equals 1 on the fold and
     decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function, a, b frame indices along the fold); it jumps by -2 H along ordinary space and along the extra times.
     The Einstein-Lovelock equations of UM-3, sum_p alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b (E_(p) the
     Lovelock tensor of order p = 1, 2, 3, alpha_(p) = w_(p) H^(2-2p) its coupling with the weights w = (1, 1/20, 1/360),
     Lambda = -7 H^2 the cosmological constant, kappa = 8 pi G_8 the gravitational coupling of eight dimensions, T^a_b the
     energy-momentum tensor, delta^a_b the Kronecker delta), are linear in the second sigma-derivatives of the metric, so
     the jump puts a Dirac delta function delta_D(sigma) into them: the metric solves them only if the fold carries a thin
     source S^a_b, an energy-momentum tensor concentrated on sigma = 0, given by the integral of the equations across the
     fold (the junction conditions),
        (FD-11) kappa S^a_b = integral from sigma = 0- to 0+ of d sigma sum_p alpha_(p) E_(p)^a_b,
     with S^4_4 = -(its energy density), S^1_1 = S^2_2 = S^3_3 its pressure along ordinary space and S^5_5 = S^6_6 = S^7_7
     its pressure along the extra times; S is T integrated across the fold, an energy per unit volume of the six other
     directions of the fold (unit GeV^7). On the static block (a4 and b4 constant) and on an expanding fold whose extra
     times are frozen (b4 proportional to e^(a4), A = a4'/H, A1 = a4''/H^2)
        (FD-12) static block:      kappa S^a_b = -(32/5) H delta^a_b  (a pure tension),
                frozen extra times: kappa S^1_1 = -(16/15)(6 + 3 A^2 + 2 A1) H,  kappa S^4_4 = -(16/5)(2 + A^2) H,
                                    kappa S^5_5 = -(4/5)(8 + 8 A^2 + A^4 + 4 A1 + A^2 A1) H:
     the tension plus matter that obeys the Friedmann equations of general relativity. The fold is therefore not only a
     place but a physical object: a thin layer that carries energy and momentum (a brane). (FD-11 and FD-12 were added
     to this definition on 2026-10-25, after FD-1 to FD-10, with the corrected Lovelock weights; they stand here because
     they belong to property 3.)
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the author's ad hoc vacuum, a time-dependent
choice of its vacuum value; the gauge fields of SU(3)_C x SU(2)_L x U(1)_Y; three generations of quarks and leptons and
three right-handed neutrinos) and the fold fluid (its tension and the pressure along the extra times that keeps their
volume fixed) live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no field depends on the extra
times). Integrated over the extra times, the fold is the four-dimensional universe that we observe, with the metric
diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex (the author's spinor field of eight dimensions) and
gravity live in the bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that
the fold holds, and the portals (couplings between dirac16complex and Standard-Model fields) act at sigma = 0. In UM-3
files "the fold" means this surface; the examples below use the word for other surfaces with the same properties. The
word is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by the factor e is
called an e-folding.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp factor (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2
     diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
     line -infinity < sigma < infinity. A compact direction of length L would give every field a tower of particles with
     the masses 2 pi n/L, n = 1, 2, ... (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
     pi/(6 H) of x0 produces no such tower with the spacing 12 H, and the x0 mass of the bound states is their binding to
     the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every metric function of FD-4 depends on sigma
     through |sigma| and is folded at sigma = 0 in this sense.
  5. A fold map. In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map u -> u^2 of a line onto
     a half-line: it folds the line at u = 0, two points +u and -u land on the same point, and the derivative of the map
     vanishes on the fold. Near the fold the map from the author's coordinate x0 to the distance |sigma| from the fold is
     of this kind (FD-6), and g_x0x0 = cot(z)^2, the square of the derivative d sigma/d x0, vanishes there.
  6. The brane of Randall and Sundrum. The five-dimensional metric
        (FD-8)  dy_RS^2 + e^(-2 k_RS |y_RS|) (dx1^2 + dx2^2 + dx3^2 - dx4^2),
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2/kappa_5
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the vacuum energy Lambda_RS, and the bulk is otherwise empty. The fold of UM-3 is of the same kind: its static
     block is a vacuum of the bulk with a fold of pure tension (FD-12). It differs in that the time x4 is not warped,
     three extra times are warped together with ordinary space, the Lovelock terms add to the junction conditions, and
     the space is not cut at the brane: Randall and Sundrum identify the two sides of their brane (one physical side),
     while the fold of UM-3 has two distinct sides (example 7).
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a wave function that falls off
     exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
     equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex bound
     to the fold; at rest and without their self-interaction (the field is Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0). The profile is not a function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi (the average field that the particles of the gas create and feel): the four bound states of Krein
     charge -1 (the particles chi) are even under it and the four of Krein charge +1 are odd, so the mean field of the gas
     cannot mix the two signs of the indefinite charge. R_2 maps the bound states of one Krein charge onto those of the
     other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory (the eleven-dimensional theory whose limits include the superstring
     theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional
     planes left in place by the reflection are mirror surfaces (property 1); each carries one E8 gauge group while gravity
     fills the bulk. As in UM-3, the gauge fields live on the mirror surface and gravity in the bulk; unlike UM-3, the two
     sides of each plane are identified (one physical side).

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp factor vanishes,
    g_x0x0 diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp factor, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a
    kink and without a thin source.
END FOLD DEFINITION
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
# the corrected weights (the author's order of 2026-10-25 07:55; the author's original values: 1/32, 1/1152, -10 H^2)
W = [None, sp.Integer(1), sp.Rational(1, 20), sp.Rational(1, 360)]
ALPHA = [None, sp.Integer(1), W[2] / H**2, W[3] / H**4]
LAMBDA = -7 * H**2
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



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

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
    zero = lambda vals: all(sp.expand(LHS[a, b].subs(vals)) == 0 for a in range(8) for b in range(8))
    rep.check('G4_static_block_vacuum', zero({A: 0, U: 0, Ad: 0, Ud: 0}),
              'with the corrected weights w = (1, 1/20, 1/360) and Lambda = -7 H^2 (um3_weights.py) the static block (a4, b4 '
              'constant) solves the vacuum equations: the late-time bulk needs no source')
    rep.check('G4_frozen_extra_times_vacuum', zero({U: A, Ud: Ad}),
              'with e^{-a4} b4 constant (U = A, U1 = A1) every component vanishes for any a4(x4): an expanding universe with '
              'frozen extra times is a vacuum of the bulk equations')
    rep.check('G4_static_space_vacuum', zero({A: 0, Ad: 0}),
              'with a4 constant (A = A1 = 0) every component vanishes for any b4(x4)')
    P44 = sp.factor(sp.expand(LHS[4, 4]))
    T04 = sp.factor(sp.expand(LHS[0, 4]))
    ok = (sp.expand(P44 - A**3 * (A - U)**3) == 0 and sp.expand(T04 + 3 * A**2 * U * (A - U)**2) == 0
          and sp.simplify(LHS[4, 0] + LHS[0, 4]) == 0 and P44.free_symbols <= {A, U} and T04.free_symbols <= {A, U})
    rep.check('G4_constraints', ok, 'the (x4, x4) component, kappa T^{x4}_{x4} = %s H^2, and the (x0, x4) component, '
              'kappa T^{x0}_{x4} = %s H^2 on 0 < z < pi/2 (the opposite sign on the other half of the period), contain no '
              'second time derivative' % (P44, T04))
    vac = {A: 1, U: 0, Ad: 0, Ud: 0}
    av = {k: sp.simplify(LHS[k].subs(vac)) for k in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4)]}
    rep.check('G4_author_vacuum_not_a_solution', av[(4, 4)] == 1,
              "a4 = H x4, b4 constant (A = 1, U = 0; the author's vacuum, a solution with the author's original weights "
              "w = (1, 1/32, 1/1152) and Lambda = -10 H^2) is not a vacuum with the corrected weights: it would need kappa T = %s H^2 "
              "(x0, x1, x4, x5, flux)" % [str(av[k]) for k in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4)]])
    gen = [sp.factor(sp.expand(LHS[a, b].subs({Ad: 0, Ud: 0}))) for a in range(8) for b in range(8)]
    sols = sp.solve([g for g in gen if g != 0], [A, U], dict=True)
    rep.check('G4_constant_rate_vacua', sorted(map(str, sols)) == sorted(['{A: 0}', '{U: A}']),
              'with constant rates the vacuum solutions are %s: static ordinary space with any constant rate of b4, or frozen '
              'extra times with any constant expansion rate' % sols)
    fro = {k: sp.factor(LHS[k].subs({U: A, Ud: Ad})) for k in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4)]}
    out['frozen_extra_times'] = {'%s,%s' % (NAMES[k[0]], NAMES[k[1]]): str(v) for k, v in fro.items()}
    out['author_vacuum_needs_kappaT_over_H2'] = {'%s,%s' % (NAMES[k[0]], NAMES[k[1]]): str(v) for k, v in av.items()}

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
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'geometry.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_geometry.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'geometry_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
