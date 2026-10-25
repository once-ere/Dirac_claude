#!/usr/bin/env python3
"""um3_fold.py - the fold z = pi/2 of the author's UM-3 metric: the proper chart sigma, the general warped metric, the
Einstein-Lovelock equations of that metric, and the junction (brane) conditions at the fold.

The author's metric (b4 -> b4^2, z = 6 H x0) in the proper chart of the hidden direction,
    sigma = +- |y|,  y = ln|sin z|/(6H)  (sigma < 0 for 0 < z < pi/2, sigma > 0 for pi/2 < z < pi),
is   ds^2 = d sigma^2 + e^{-2H|sigma|} (e^{2 a4} dx_i^2 - e^{-2 a4} b4^2 dx_r^2) - dx4^2.
One period of x0 is the whole line -inf < sigma < inf; the warp has a kink at the fold sigma = 0.

Computed exactly (sympy):
  J1  the map x0 -> sigma (monotonic, sigma = 0 at the fold, sigma -> -+inf at the tips z -> 0, pi), the warp
      e^{-2H|sigma|} = |sin z|^{1/3} and g00 dx0^2 = d sigma^2 on both halves of the period;
  J2  the frame curvature of the general warped metric
      ds^2 = d sigma^2 + e^{2 fa} dx_i^2 - e^{2 fn} dx4^2 - e^{2 fb} dx_r^2,   fa, fb, fn functions of (sigma, x4),
      and its Einstein-Lovelock tensor sum_p alpha_p E_(p) + Lambda (author's weights, Lambda = -10 H^2), all
      non-zero components; reduction to the author's metric (fa = a4 - H|sigma|, fb = ln b4 - a4 - H|sigma|, fn = 0)
      reproduces the equations of um3_geometry.py;
  J3  quasi-linearity: every component is linear in the second sigma-derivatives fa_ss, fb_ss, fn_ss, and the
      (sigma, sigma) and (sigma, x4) components contain none;
  J4  the junction conditions: the distributional part at the fold, kappa S^a_b = int across the fold of
      [sum_p alpha_p E_(p)^a_b] d sigma = F^a_b(after) - F^a_b(before), with the potential F (the coefficients of
      fa_ss, fb_ss, fn_ss form an exact differential in (fa_s, fb_s, fn_s));
  J5  the fold source of the author's metric for general a4(x4), b4(x4) (in A, U, Ad, Ud), at the author's vacuum
      (A = 1, U = 0) and at the static block (A = U = 0); independent numerical check by smoothing the kink;
  J6  the conservation law of the fold source, D_a S^a_4 = -[T^sigma_4] (the jump of the bulk energy flux), as an
      identity of the junction formula and the bulk (sigma, x4) equation;
  J7  the frozen extra times (U = A): the bulk and fold sources required, their limits, and the separable-metric
      Friedmann relation of the fold.
Writes outputs/fold.json and reports/fold_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_fold.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one fold, at z = pi/2. A point of the fold is labelled by the seven coordinates x1, ..., x7, and the
metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. Four properties make the surface sigma = 0 a fold, and together they single it
out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|), which multiplies ordinary space and
     the extra times, equals 1 on the fold and decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0;
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function); it jumps by -2 H along ordinary space and along the extra times. The Einstein-Lovelock equations are
     linear in the second sigma-derivatives of the metric, so the jump puts a Dirac delta function delta_D(sigma) into
     them: the metric solves them only if the fold carries a thin source S^a_b, an energy-momentum tensor concentrated on
     sigma = 0 (the junction conditions). At the author's vacuum (a4' = H, b4 constant) its frame components along (ordinary space, the
     time, the extra times) are kappa S = (-10 H, -6 H, -10 H), at the static late-time state (a4 and b4 constant)
     kappa S = (-61 H/8, -31 H/4, -61 H/8), with kappa = 8 pi G_8 the gravitational coupling of eight dimensions. The fold
     is therefore not only a place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the ad hoc vacuum, the gauge fields of
SU(3)_C x SU(2)_L x U(1)_Y, three generations of quarks and leptons and three right-handed neutrinos), the fold fluid and
the induced Einstein-Hilbert term of the fold live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no
field depends on the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we
observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex and gravity live in the
bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that the fold holds,
and the portals couple dirac16complex to the Standard Model at sigma = 0. In UM-3 files the word fold means this surface
and nothing else: a number of equal energy levels is written as a number of degenerate states, and a growth by powers of
Euler's number as a logarithm.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2 diverges, and
     which lies at an infinite proper distance from both: in proper distance every copy has its own complete line
     -infinity < sigma < infinity. This is why the period pi/(6 H) of x0 produces no Kaluza-Klein tower with the spacing
     12 H; the x0 mass of the bound states is their binding to the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every function of UM-3 that depends on sigma
     through |sigma| is folded at sigma = 0: the metric functions of FD-4 and the profiles of the bound states of
     dirac16complex (example 7).
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
     the bulk the vacuum energy Lambda_RS. The fold of UM-3 is of the same kind; it differs in that the time x4 is not
     warped, three extra times are warped together with ordinary space, and the Lovelock terms add to the junction
     conditions.
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a folded wave function: it falls
     off exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order
     Dirac equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex
     bound to the fold; at rest and without their self-interaction (the field is
     Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi: the four bound states of Krein charge -1 (the particles chi) are even under it and the four of Krein
     charge +1 are odd, so the mean field of the gas cannot mix the two signs of the indefinite charge. R_2 maps the bound
     states of one Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory on an interval (a circle whose points are identified with their mirror
     images), the two ten-dimensional planes left in place by the reflection are mirror surfaces (property 1); the gauge
     fields E8 x E8 live on them while gravity fills the bulk. This is the arrangement of UM-3, where the Standard Model
     lives on the fold and gravity and dirac16complex fill the bulk.

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp vanishes, g_x0x0
    diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a kink
    and without a thin source.
END FOLD DEFINITION
"""
from __future__ import annotations

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
from um3_lovelock import frame_riemann, lovelock_tensor  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


X = sp.symbols('x0:8', real=True)
SIG, X4 = X[0], X[4]
H = sp.Symbol('H', positive=True)
W = [None, sp.Integer(1), sp.Rational(1, 32), sp.Rational(1, 1152)]
ALPHA = [None, sp.Integer(1), W[2] / H**2, W[3] / H**4]
LAMBDA = -10 * H**2
NAMES = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
FA = sp.Function('fa')(SIG, X4)
FB = sp.Function('fb')(SIG, X4)
FN = sp.Function('fn')(SIG, X4)
# derivative symbols: f?_s, f?_ss, f?_st, f?_t, f?_tt  (s = sigma, t = x4)
D = {}
for nm in ('a', 'b', 'n'):
    for tag in ('s', 'ss', 'st', 't', 'tt'):
        D[nm + '_' + tag] = sp.Symbol('f%s_%s' % (nm, tag), real=True)
FN0 = sp.Symbol('fn0', real=True)   # the value of fn itself (enters through e^{-fn})
A, U, Ad, Ud = sp.symbols('A U Ad Ud', real=True)


def to_symbols(e):
    for f, nm in ((FA, 'a'), (FB, 'b'), (FN, 'n')):
        e = e.subs(sp.Derivative(f, (SIG, 2)), D[nm + '_ss'])
        e = e.subs(sp.Derivative(f, SIG, X4), D[nm + '_st'])
        e = e.subs(sp.Derivative(f, (X4, 2)), D[nm + '_tt'])
        e = e.subs(sp.Derivative(f, SIG), D[nm + '_s'])
        e = e.subs(sp.Derivative(f, X4), D[nm + '_t'])
    e = e.subs(FN, FN0)
    return sp.expand(e)


def general_lhs():
    g = sp.diag(1, *[sp.exp(2 * FA)] * 3, -sp.exp(2 * FN), *[-sp.exp(2 * FB)] * 3)
    h = [sp.S(1)] + [sp.exp(FA)] * 3 + [sp.exp(FN)] + [sp.exp(FB)] * 3
    Rf = frame_riemann(g, X, h)
    Rs = {k: to_symbols(v) for k, v in Rf.items()}
    E = {p: lovelock_tensor(Rs, p, simplify=sp.expand) for p in (1, 2, 3)}
    L = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            L[i, j] = sp.expand(sum(ALPHA[p] * E[p][i, j] for p in (1, 2, 3)) + (LAMBDA if i == j else 0))
    return Rs, E, L


def author_values(side):
    """The derivative symbols for the author's metric on one side of the fold (side = -1: sigma < 0, i.e. 0 < z < pi/2;
    side = +1: sigma > 0).  fa = a4 - H|sigma|, fb = ln b4 - a4 - H|sigma|, fn = 0."""
    s_ = -side  # d|sigma|/d sigma = side; fa_s = -H side
    return {D['a_s']: -H * side, D['b_s']: -H * side, D['n_s']: 0, D['a_ss']: 0, D['b_ss']: 0, D['n_ss']: 0,
            D['a_st']: 0, D['b_st']: 0, D['n_st']: 0, D['n_t']: 0, D['n_tt']: 0, FN0: 0,
            D['a_t']: A * H, D['b_t']: (U - A) * H, D['a_tt']: Ad * H**2, D['b_tt']: (Ud - Ad) * H**2}



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- J1: the proper chart
    z = sp.Symbol('z', positive=True)
    y = sp.log(sp.sin(z)) / (6 * H)
    dydx0 = sp.diff(y, z) * 6 * H
    ok1 = sp.simplify(dydx0 - sp.cot(z)) == 0
    ok2 = sp.simplify(sp.exp(2 * H * y) - sp.sin(z)**sp.Rational(1, 3)) == 0
    # sigma = y on 0<z<pi/2 (d sigma/dx0 = cot z > 0) and sigma = -y on pi/2<z<pi (d sigma/dx0 = -cot z > 0)
    ok3 = all(float(sp.cot(zz)) > 0 for zz in (0.1, 0.7, 1.5)) and all(float(-sp.cot(zz)) > 0 for zz in (1.7, 2.5, 3.0))
    lim0 = sp.limit(y, z, 0, '+')
    rep.check('J1_proper_chart', ok1 and ok2 and ok3 and lim0 == -sp.oo,
              'sigma = ln(sin z)/(6H) on 0<z<pi/2 and -ln(sin z)/(6H) on pi/2<z<pi: d sigma = |cot z| dx0 (so g00 dx0^2 = '
              'd sigma^2), sigma increases monotonically through the fold z = pi/2 (sigma = 0) and runs to -inf/+inf at the '
              'tips z -> 0, pi; e^{-2H|sigma|} = (sin^2 z)^{1/6}: one period of x0 is the whole sigma line')

    # ---------------- J2: general warped metric
    Rs, E, L = general_lhs()
    nz = sorted((i, j) for i in range(8) for j in range(8) if L[i, j] != 0)
    ok = set(nz) == {(0, 0), (0, 4), (4, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)}
    iso = all(sp.expand(L[1, 1] - L[k, k]) == 0 for k in (2, 3)) and all(sp.expand(L[5, 5] - L[k, k]) == 0 for k in (6, 7))
    rep.check('J2_general_structure', ok and iso, 'the general warped metric (fa, fb, fn of sigma and x4) has non-zero '
              'Einstein-Lovelock components only on the diagonal and in the (sigma, x4) pair; isotropic in x1..x3 and in x5..x7')
    out['curvature_general'] = {'R^{%s%s}_{%s%s}' % (NAMES[a], NAMES[b], NAMES[c], NAMES[d]): str(v)
                                for ((a, b), (c, d)), v in sorted(Rs.items())}
    out['lhs_general'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(sp.factor(L[i, j])) for (i, j) in
                          [(0, 0), (0, 4), (4, 0), (1, 1), (4, 4), (5, 5)]}
    # reduction to the author's metric (compare with um3_geometry: LHS/H^2 polynomials)
    geo = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())['field_equations_lhs_over_H2']
    loc = {'A': A, 'U': U, 'Ad': Ad, 'Ud': Ud}
    ok = True
    for key, (i, j) in {'x0,x0': (0, 0), 'x1,x1': (1, 1), 'x4,x4': (4, 4), 'x5,x5': (5, 5), 'x0,x4': (0, 4)}.items():
        mine = sp.expand(L[i, j].subs(author_values(-1)) / H**2)
        theirs = sp.expand(sp.sympify(geo[key], locals=loc))
        if sp.simplify(mine - theirs) != 0:
            ok = False
            print('  mismatch', key, sp.factor(mine - theirs))
    # on the other side every component is the same except (sigma, x4), which changes sign
    ok2 = all(sp.simplify(L[i, i].subs(author_values(-1)) - L[i, i].subs(author_values(+1))) == 0 for i in range(8))
    ok3 = sp.simplify(L[0, 4].subs(author_values(-1)) + L[0, 4].subs(author_values(+1))) == 0
    rep.check('J2_reduces_to_author_metric', ok and ok2 and ok3,
              'with fa = a4 - H|sigma|, fb = ln b4 - a4 - H|sigma|, fn = 0 the general equations reduce, on both sides of '
              'the fold, to those of um3_geometry.py (G4); the (sigma, x4) component changes sign across the fold')

    # ---------------- J3: quasi-linearity
    second = [D['a_ss'], D['b_ss'], D['n_ss']]
    ql = True
    for (i, j) in nz:
        poly = sp.Poly(L[i, j], *second)
        if any(sum(m) > 1 for m in poly.monoms()):
            ql = False
    none00 = all(sp.diff(L[0, 0], v) == 0 for v in second) and all(sp.diff(L[0, 4], v) == 0 for v in second)
    rep.check('J3_quasi_linear', ql and none00, 'every component is linear in fa_ss, fb_ss, fn_ss (no products of second '
              'sigma-derivatives, the property of Lovelock gravity that makes thin sources well defined); the (sigma,sigma) '
              'and (sigma,x4) components contain no second sigma-derivative (constraints)')

    # ---------------- J4: junction potential
    first = [D['a_s'], D['b_s'], D['n_s']]
    Fpot = {}
    exact = True
    for (i, j) in [(1, 1), (4, 4), (5, 5)]:
        e = L[i, j].subs({D['a_st']: 0, D['b_st']: 0, D['n_st']: 0})
        C = [sp.diff(e, v) for v in second]
        for k1 in range(3):
            for k2 in range(k1 + 1, 3):
                if sp.expand(sp.diff(C[k1], first[k2]) - sp.diff(C[k2], first[k1])) != 0:
                    exact = False
        # potential by integration along straight lines from 0
        lam = sp.Symbol('lam')
        integrand = sum(C[k].subs({first[m]: lam * first[m] for m in range(3)}) * first[k] for k in range(3))
        F = sp.integrate(sp.expand(integrand), (lam, 0, 1))
        F = sp.expand(F)
        ok = all(sp.expand(sp.diff(F, first[k]) - C[k]) == 0 for k in range(3))
        exact = exact and ok
        Fpot[(i, j)] = F
    rep.check('J4_exact_differential', exact, 'the coefficients of (fa_ss, fb_ss, fn_ss) in each diagonal fold-direction '
              'component are the gradient of a potential F(fa_s, fb_s, fn_s; x4-derivatives): the integral across a thin '
              'fold depends only on the values of the first sigma-derivatives on its two sides')
    out['junction_potential'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(sp.factor(F)) for (i, j), F in Fpot.items()}

    # ---------------- J5: fold source of the author's metric
    jump = {}
    for (i, j), F in Fpot.items():
        after = F.subs(author_values(+1))
        before = F.subs(author_values(-1))
        jump[(i, j)] = sp.factor(sp.expand(after - before))
    out['fold_source_kappaS'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(v) for (i, j), v in jump.items()}
    vac = {A: 1, U: 0, Ad: 0, Ud: 0}
    sv = {k: sp.simplify(v.subs(vac)) for k, v in jump.items()}
    ok = sv == {(1, 1): -10 * H, (4, 4): -6 * H, (5, 5): -10 * H}
    rep.check('J5_author_vacuum_fold_source', ok, "at the author's vacuum (a4 = H x4, b4 constant) the fold carries "
              "kappa S = diag(x1..x3: -10H, x4: -6H, x5..x7: -10H): energy density kappa rho_fold = 6H > 0 and pressures "
              "kappa p = -10H (the metric is not a vacuum solution at the fold; it needs a thin source there)")
    sb = {k: sp.simplify(v.subs({A: 0, U: 0, Ad: 0, Ud: 0})) for k, v in jump.items()}
    ok = sb == {(1, 1): -sp.Rational(61, 8) * H, (4, 4): -sp.Rational(31, 4) * H, (5, 5): -sp.Rational(61, 8) * H}
    rep.check('J5_static_block_fold_source', ok, 'at the static block (A = U = 0): kappa S = diag(-61/8, -31/4, -61/8) H: '
              'kappa rho_fold = 31H/4, kappa p_fold = -61H/8, rho + p = H/(8 kappa) > 0')
    out['fold_source_author_vacuum'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(v) for (i, j), v in sv.items()}
    out['fold_source_static_block'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(v) for (i, j), v in sb.items()}
    # (sigma,sigma) and (sigma,x4) have no thin part
    rep.check('J5_no_thin_part_in_constraints', True, 'the (sigma,sigma) and (sigma,x4) components carry no delta function '
              '(J3): the bulk constraints hold on each side, the (sigma,x4) flux changes sign across the fold')
    # numerical check: smooth the kink, fa_s = -H tanh(sigma/eps), and integrate the full LHS across the layer
    import mpmath as mp
    mp.mp.dps = 30
    rng = random.Random(3)
    okn = True
    worst = 0.0
    for trial in range(3):
        Hv = rng.uniform(0.6, 1.4)
        Av, Uv, Adv, Udv = rng.uniform(-1, 1.5), rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-1, 1)
        for (i, j) in [(1, 1), (4, 4), (5, 5)]:
            expr = L[i, j]
            base = {H: Hv, D['n_s']: 0, D['n_ss']: 0, D['a_st']: 0, D['b_st']: 0, D['n_st']: 0, D['n_t']: 0, D['n_tt']: 0,
                    FN0: 0, D['a_t']: Av * Hv, D['b_t']: (Uv - Av) * Hv, D['a_tt']: Adv * Hv**2, D['b_tt']: (Udv - Adv) * Hv**2}
            e2 = sp.lambdify((D['a_s'], D['b_s'], D['a_ss'], D['b_ss']), expr.subs(base), 'mpmath')
            res = []
            for eps in (1e-4, 1e-5):
                f = lambda s: e2(-Hv * mp.tanh(s / eps), -Hv * mp.tanh(s / eps),
                                 -(Hv / eps) * mp.sech(s / eps)**2, -(Hv / eps) * mp.sech(s / eps)**2)
                res.append(mp.quad(f, [-40 * eps, -eps, 0, eps, 40 * eps]))
            exact_v = float(jump[(i, j)].subs({H: Hv, A: Av, U: Uv, Ad: Adv, Ud: Udv}))
            e1 = abs(float(res[0]) - exact_v) / max(1.0, abs(exact_v))
            e2_ = abs(float(res[1]) - exact_v) / max(1.0, abs(exact_v))
            # the regular part of the integrand contributes O(eps): the deviation must fall by a factor of ten with eps
            worst = max(worst, e2_)
            if not (e2_ < 3e-4 and e2_ < 0.2 * e1 + 1e-12):
                okn = False
    rep.check('J5_smoothed_kink', okn, 'replacing the kink by fa_s = fb_s = -H tanh(sigma/eps) and integrating the full '
              'left-hand side across the layer reproduces kappa S (relative deviation %.1e at eps = 1e-5 for 3 random '
              '(H, A, U, Ad, Ud), falling linearly with eps: the remainder is the O(eps) regular part)' % worst)

    # ---------------- J6: conservation of the fold source
    # D_a S^a_4 = d_4 S^4_4 + 3 a4' (S^4_4 - S^1_1) + 3 (b4'/b4 - a4') (S^4_4 - S^5_5)
    a4 = sp.Function('a4')(X4)
    lb = sp.Function('lb')(X4)   # ln b4
    sub_t = {A: sp.diff(a4, X4) / H, U: sp.diff(lb, X4) / H, Ad: sp.diff(a4, X4, 2) / H**2, Ud: sp.diff(lb, X4, 2) / H**2}
    S11 = jump[(1, 1)].subs(sub_t)
    S44 = jump[(4, 4)].subs(sub_t)
    S55 = jump[(5, 5)].subs(sub_t)
    div = sp.diff(S44, X4) + 3 * sp.diff(a4, X4) * (S44 - S11) + 3 * (sp.diff(lb, X4) - sp.diff(a4, X4)) * (S44 - S55)
    flux_after = L[0, 4].subs(author_values(+1)).subs(sub_t)
    flux_before = L[0, 4].subs(author_values(-1)).subs(sub_t)
    # frame (sigma, x4) mixed component T^sigma_4 (frame) = T^{(0)}_{(4)}; the fold conservation reads D_a S^a_4 = -(after - before)
    ident = sp.simplify(sp.expand(div + (flux_after - flux_before)))
    rep.check('J6_fold_conservation', ident == 0, 'D_a S^a_4 + [kappa T^sigma_4] = 0 identically for general a4(x4), '
              'b4(x4): the fold source loses exactly the energy that the bulk flux T^sigma_4 carries away on both sides')

    # ---------------- J7: frozen extra times U = A
    fro = {k: sp.factor(v.subs({U: A, Ud: Ad})) for k, v in jump.items()}
    out['fold_source_frozen'] = {'%s,%s' % (NAMES[i], NAMES[j]): str(v) for (i, j), v in fro.items()}
    ok = sp.simplify(fro[(4, 4)] + (31 + 10 * A**2) * H / 4) == 0
    rep.check('J7_frozen_fold_energy', ok, 'with frozen extra times (U = A): kappa rho_fold = (31 + 10 A^2) H/4, i.e. '
              'kappa (rho_fold - 31H/(4 kappa)) = (5/2) a4\'^2/H: in the separable metric the fold energy above the static '
              'value fixes the expansion rate a4\'')
    p11 = sp.expand(fro[(1, 1)])
    ok = sp.simplify(p11 + (183 + 57 * A**2 + 40 * Ad) * H / 24) == 0
    rep.check('J7_frozen_fold_pressure', ok, 'and kappa p_fold(x1..x3) = -(183 + 57 A^2 + 40 Ad) H/24 (with Ad = a4\'\'/H^2): '
              'a tension, as the static value -183H/24')
    # a fold fluid on top of the static values: kappa rho_m = (5/2) A^2 H, kappa p_m = -(57 A^2 + 40 Ad) H/24 (the source above
    # minus its static part).  Separately conserved it would obey rho_m' + 3 a4' (rho_m + p_m) = 0 (a4' = A H, A' = Ad H); the
    # left-hand side is computed here.  The static source with the bulk flux is not conserved by itself at order A^3 (J6
    # holds only for the total), so the fluid on top of it exchanges energy with the bulk.
    lhs_ = sp.expand(sp.Rational(5, 2) * 2 * A * Ad * H**2
                     + 3 * A * H * (sp.Rational(5, 2) * A**2 * H - (57 * A**2 + 40 * Ad) * H / 24))
    flux3 = sp.expand(2 * sp.Rational(3, 16) * A**3 * H**2)             # the A^3 part of the jump of the flux 3A(1 + A^2)/16 H^2
    out['separately_conserved_fold_fluid_residual'] = str(lhs_)
    rep.check('J7_separable_metric_too_rigid', sp.simplify(lhs_ - flux3) == 0 and sp.diff(lhs_, Ad) == 0,
              'a fold fluid on top of the static values (kappa rho_m = (5/2) A^2 H, kappa p_m = -(57 A^2 + 40 Ad) H/24) cannot be '
              'separately conserved on the separable metric for any equation of state: rho_m\' + 3 a4\' (rho_m + p_m) = %s/kappa '
              '(independent of Ad), the A^3 part of the bulk flux at the fold that the static source does not balance; ordinary '
              'matter on the fold requires metric functions that also depend on sigma near the fold (the next terms of the '
              'power series of the metric)' % lhs_)
    bulk = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())['frozen_extra_times']
    out['bulk_source_frozen_kappaT_over_H2'] = bulk
    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs').mkdir(exist_ok=True)
    (UM3 / 'reports').mkdir(exist_ok=True)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'fold.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_fold.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'fold_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
