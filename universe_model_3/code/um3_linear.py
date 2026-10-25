#!/usr/bin/env python3
"""um3_linear.py - the linearised Einstein-Lovelock equations of UM-3 for ARBITRARY perturbations of the metric around
its vacua, with the corrected weights w = (1, 1/20, 1/360) and Lambda = -7 H^2 (the author's order of 2026-10-25, 07:55
PDT), the author's original weights (1, 1/32, 1/1152) and Einstein gravity alone for comparison.

Method.  At one point of the bulk (sigma > 0, H = 1) the metric is the background of the author's metric,
    ds^2 = d sigma^2 + e^{2 fa} (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^{2 fb} (dx5^2 + dx6^2 + dx7^2),
plus eps times a perturbation delta g_ab given by its value and its first and second derivatives at the point (its jet).
The Riemann tensor at the point follows exactly from the jets,
    R_abcd = (1/2)(g_ad,bc + g_bc,ad - g_ac,bd - g_bd,ac) + g_ef (Gamma^e_bc Gamma^f_ad - Gamma^e_bd Gamma^f_ac),
with the convention [nabla_c, nabla_d] V^a = R^a_bcd V^b (the unit sphere has R^{01}_{01} = +1), and the Lovelock tensors
    E_(p)^a_b = -2^{-(p+1)} delta^{a c1 ... c2p}_{b d1 ... d2p} R^{d1 d2}_{c1 c2} ... R^{d2p-1 d2p}_{c2p-1 c2p},
so that E_(1) is the Einstein tensor, follow from the generalised Kronecker delta (a sum over sets of p distinct
components R^{U}_{L} whose lower and upper index pairs, together with a and b, are permutations of each other).  All
arithmetic is exact (polynomials with rational coefficients); the terms of first order in eps are the linearised operator.
A perturbation delta g_ab = eps c_ab y^2/2 along one coordinate y (all first derivatives and values zero at the point)
gives exactly the principal symbol of the linearised equations for the covector dy: the coefficients of the second
derivatives of the 36 components delta g_ab along y in the 64 components of the equations.

Checks:
  LN1  the conventions: the unit sphere; on a random metric E_(1) is the Einstein tensor, the trace of E_(2) is -(D - 4)/2
       times the Gauss-Bonnet density and the trace of E_(3) is -(D - 6)/2 times the cubic Lovelock density (D = 8); at the
       static block (a4, b4 constant, the seven directions sigma, x1, x2, x3, x5, x6, x7 a space of constant curvature -H^2,
       the time x4 flat) the entries per unit weight are (15, 21), (-180, -420), (360, 2520) H^2 along the warped directions
       and along the time;
  LN2  the static block, an arbitrary perturbation (all 36 components with random values and first and second
       derivatives): the linearised operator of order p is F_p(3) X3 + F_p(2) X2, where X3 and X2 are the parts of the
       linearised Einstein operator -(1/4) delta^{a c1 c2}_{b d1 d2} delta R^{d1 d2}_{c1 c2} without and with the time among
       the indices a, c1, c2, and (F(3), F(2)) = (1, 1), (-24, -40), (72, 360) H^{2p-2} for p = 1, 2, 3; so the total is
       c_x X3 + c_t X2 with c_x = 1 - 24 w2 + 72 w3 and c_t = 1 - 40 w2 + 360 w3, and dE_(3) = -18 dE_(2) - 360 dE_(1); with
       the corrected weights the whole linearised bulk operator vanishes identically (the bulk has no linear graviton);
       on the line w2 = 18 w3 (c_t = c_x = 1 - 360 w3) it is (1 - 360 w3) times the linearised Einstein operator (bulk
       gravitons at the local speed of light);
  LN3  the family of static blocks of curvature -y H^2, by direct computation of the curvature: per unit weight the
       entries are 15 y, -180 y^2, 360 y^3 (warped directions) and 21 y, -420 y^2, 2520 y^3 (time); with the corrected
       weights and Lambda = -7 H^2 the left-hand side is (y - 1)^2 (y - 7) H^2 and 7 (y - 1)^3 H^2: a degenerate vacuum
       (the Born-Infeld point of Lovelock gravity in eight dimensions: the time entry is that of an eight-dimensional
       space of constant curvature, 7 (y - 1)^3, a triple root);
  LN4  the bulk on the branch of frozen extra times (b4 proportional to e^{a4}; A = a4'/H, A1 = a4''/H^2, sigma > 0):
       principal symbols with the corrected weights.  Along dx4 the matrix of the coefficients of the second time
       derivatives has rank 0 for every A, A1: no component of the metric perturbation has a time-kinetic term
       (Einstein gravity alone and the author's weights: rank 28).  Along dx3 and along d sigma the ranks are 0 at the
       static block and 10 and 16 for A != 0, every entry proportional to A^2: gradient terms without time-kinetic
       terms, so the linearised bulk equations are not hyperbolic and those components respond instantaneously;
  LN5  the bulk on the branch of static ordinary space (A = 0, U = b4'/(H b4), U1 = U'/H): along dx4 rank 0 for every
       U, U1, along dx3 and d sigma ranks 0 at the static block and 19 and 16 for U != 0, every entry proportional to U^2
       (the same structure: gradient terms without time-kinetic terms).
The jet code was written by an independent referee (a Claude agent of this session, 2026-10-25) and is adopted here
after review; it imports nothing from the other UM-3 modules.
Writes outputs/linear.json and reports/linear_checks.json.  Runs in about a minute.
Usage: python universe_model_3/code/um3_linear.py

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

import json
import random
import sys
import time
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

X = sp.symbols('x0:8', real=True)          # x0 = sigma at the point (the proper chart), x1..x7 as the author's
ETA = [1, 1, 1, 1, -1, -1, -1, -1]
W_NEW = (sp.Rational(1, 20), sp.Rational(1, 360))
W_AUTHOR = (sp.Rational(1, 32), sp.Rational(1, 1152))


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


# ------------------------------------------------------------------------------------------ the geometry at a point
def perm_sign(seq_from, seq_to):
    """The sign of the permutation that rearranges seq_from into seq_to (the same distinct elements)."""
    pos = {x: i for i, x in enumerate(seq_from)}
    perm = [pos[x] for x in seq_to]
    seen = [False] * len(perm)
    sgn = 1
    for i in range(len(perm)):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                L += 1
            if L % 2 == 0:
                sgn = -sgn
    return sgn


def jet_name(d, names):
    idx = []
    for v, cnt in d.variable_count:
        idx += [str(X.index(v))] * cnt
    idx.sort()
    return names[d.expr.func] + '_' + ''.join(idx)


class PointGeometry:
    """The metric, its inverse, the Christoffel symbols and the Riemann tensor at the point X = 0, exactly.

    g: 8x8 sympy Matrix in X, containing applied undefined functions (the background metric functions);
    names: {function class: 'fa'}; values: {jet name ('fa_0' = d fa/dx0, 'fa_44', value 'fa_'): expression in the
    ring generators} (missing jets are zero); gens: the sympy Symbols that generate the polynomial ring over QQ;
    eps and order_eps: the perturbation parameter and the order to which everything is truncated."""

    def __init__(self, g, funcs, names, values, gens, eps=None, order_eps=None):
        n = 8
        self.n = n
        self.R, *gs = ring(gens, QQ)
        self.eps_index = [str(s) for s in gens].index(str(eps)) if eps is not None else None
        self.order_eps = order_eps

        def conv(e):
            if e == 0:
                return self.R.zero
            rep = {d: sp.sympify(values.get(jet_name(d, names), 0)) for d in e.atoms(sp.Derivative)}
            e = e.xreplace(rep)
            e = e.xreplace({f: sp.sympify(values.get(names[f.func] + '_', 0)) for f in funcs})
            e = sp.expand(e.xreplace({x: 0 for x in X}))
            return self.R.zero if e == 0 else self.R.from_expr(e)
        self.g = [[conv(g[a, b]) for b in range(n)] for a in range(n)]
        dg_s = [[[sp.diff(g[a, b], X[c]) for b in range(n)] for a in range(n)] for c in range(n)]
        self.dg = [[[conv(dg_s[c][a][b]) for b in range(n)] for a in range(n)] for c in range(n)]
        self.ddg = [[[[conv(sp.diff(dg_s[c][a][b], X[d])) for b in range(n)] for a in range(n)] for d in range(n)]
                    for c in range(n)]
        self._inverse()
        self._riemann()

    def trunc(self, p):
        if self.eps_index is None or self.order_eps is None or p == 0:
            return p
        k = self.eps_index
        return self.R({m: c for m, c in p.items() if m[k] <= self.order_eps})

    def _inverse(self):
        """g^{-1} = eta - eta delta eta + ... to the order of eps kept (the metric is eta at the point up to eps)."""
        n, R = self.n, self.R
        delta = [[self.g[a][b] - (ETA[a] if a == b else 0) for b in range(n)] for a in range(n)]
        if any(delta[a][b] != 0 for a in range(n) for b in range(n)) and self.eps_index is None:
            raise ValueError('the metric at the point is not eta and no eps truncation is given')
        ginv = [[R(ETA[a] if a == b else 0) for b in range(n)] for a in range(n)]
        term = [[R(ETA[a] if a == b else 0) for b in range(n)] for a in range(n)]
        for _ in range(self.order_eps or 0):
            new = [[R.zero for _ in range(n)] for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    s = R.zero
                    for c in range(n):
                        if term[a][c] != 0 and delta[c][b] != 0:
                            s += term[a][c] * delta[c][b]
                    new[a][b] = self.trunc(-s * ETA[b])
            term = new
            for a in range(n):
                for b in range(n):
                    ginv[a][b] = ginv[a][b] + term[a][b]
        self.ginv = ginv

    def _riemann(self):
        n, R = self.n, self.R
        g, dg, ddg, gi = self.g, self.dg, self.ddg, self.ginv
        half = QQ(1, 2)
        G1 = [[[self.trunc((dg[c][d][b] + dg[b][d][c] - dg[d][b][c]) * half) for c in range(n)] for b in range(n)]
              for d in range(n)]               # Gamma_{d b c} = (g_db,c + g_dc,b - g_bc,d)/2
        Gam = [[[R.zero for _ in range(n)] for _ in range(n)] for _ in range(n)]
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    s = R.zero
                    for d in range(n):
                        if gi[a][d] != 0 and G1[d][b][c] != 0:
                            s += gi[a][d] * G1[d][b][c]
                    Gam[a][b][c] = self.trunc(s)
        Rl = {}
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(n):
                    for d in range(c + 1, n):
                        s = (ddg[b][c][a][d] + ddg[a][d][b][c] - ddg[a][c][b][d] - ddg[b][d][a][c]) * half
                        for e in range(n):
                            for f in range(n):
                                if g[e][f] == 0:
                                    continue
                                t = R.zero
                                if Gam[e][b][c] != 0 and Gam[f][a][d] != 0:
                                    t += Gam[e][b][c] * Gam[f][a][d]
                                if Gam[e][b][d] != 0 and Gam[f][a][c] != 0:
                                    t -= Gam[e][b][d] * Gam[f][a][c]
                                if t != 0:
                                    s += g[e][f] * t
                        s = self.trunc(s)
                        if s != 0:
                            Rl[(a, b, c, d)] = s

        def rlow(a, b, c, d):
            sg = 1
            if a > b:
                a, b, sg = b, a, -sg
            if c > d:
                c, d, sg = d, c, -sg
            if a == b or c == d:
                return None
            v = Rl.get((a, b, c, d))
            return None if v is None else (v if sg == 1 else -v)
        Rm = {}
        nz = [[(e, gi[a][e]) for e in range(n) if gi[a][e] != 0] for a in range(n)]
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(n):
                    for d in range(c + 1, n):
                        s = R.zero
                        for e, ge in nz[a]:
                            for f, gf in nz[b]:
                                r = rlow(e, f, c, d)
                                if r is not None:
                                    s += ge * gf * r
                        s = self.trunc(s)
                        if s != 0:
                            Rm[(c, d, a, b)] = s          # key (c, d, a, b) with c < d, a < b: R^{ab}_{cd}
        self.Rmix = Rm


def lovelock(Rmix, p, a, b, trunc=lambda x: x, zero=0):
    """E_(p)^a_b = -2^{p-1} p! times the sum, over sets of p distinct components R^{U_i}_{L_i} (sorted index pairs) whose
    lower indices together with a, and upper indices together with b, are distinct and the same set, of
    sgn(delta^{a L_1 ... L_p}_{b U_1 ... U_p}) prod R^{U_i}_{L_i}.  (The ordered sum over c1..c2p, d1..d2p of the
    definition counts each set p! 4^p times, and -2^{-(p+1)} p! 4^p = -2^{p-1} p!.)"""
    entries = [(k[0], k[1], k[2], k[3], v) for k, v in Rmix.items()]
    acc = [zero]

    def rec(start, lowseq, upseq, used_l, used_u, prod, depth):
        if depth == p:
            if used_l != used_u:
                return
            sg = perm_sign(upseq, lowseq)
            acc[0] = acc[0] + (prod if sg == 1 else -prod)
            return
        for k in range(start, len(entries)):
            c1, c2, d1, d2, v = entries[k]
            if c1 in used_l or c2 in used_l or d1 in used_u or d2 in used_u:
                continue
            rec(k + 1, lowseq + (c1, c2), upseq + (d1, d2), used_l | {c1, c2}, used_u | {d1, d2},
                v if prod is None else trunc(prod * v), depth + 1)
    rec(0, (a,), (b,), frozenset([a]), frozenset([b]), None, 0)
    return trunc(acc[0] * (-(2 ** (p - 1)) * int(sp.factorial(p))))


def mixed(G, a, b, c, d):
    """R^{ab}_{cd} from the stored components."""
    sg = 1
    if a > b:
        a, b, sg = b, a, -sg
    if c > d:
        c, d, sg = d, c, -sg
    if a == b or c == d:
        return G.R.zero
    v = G.Rmix.get((c, d, a, b))
    return G.R.zero if v is None else sg * v


# ------------------------------------------------------------------------------------------ the background metrics
FA_F, FB_F = sp.Function('fa'), sp.Function('fb')
FA, FB = FA_F(X[0], X[4]), FB_F(X[0], X[4])
NAMES = {FA_F: 'fa', FB_F: 'fb'}


def background():
    return sp.diag(1, sp.exp(2 * FA), sp.exp(2 * FA), sp.exp(2 * FA), -1, -sp.exp(2 * FB), -sp.exp(2 * FB),
                   -sp.exp(2 * FB))


def principal_symbol(coord, vals, gens_extra):
    """delta g_ab = eps c_ab y^2/2 along the coordinate y: the linearised E_(p)^a_b at the point, p = 1, 2, 3, as
    expressions linear in the 36 symbols c_ab."""
    eps = sp.Symbol('eps')
    C = {(a, b): sp.Symbol('c%d%d' % (a, b), real=True) for a in range(8) for b in range(a, 8)}
    g = background()
    for (a, b), c in C.items():
        g[a, b] += eps * c * coord ** 2 / 2
        if a != b:
            g[b, a] += eps * c * coord ** 2 / 2
    G = PointGeometry(g, [FA, FB], NAMES, vals, list(gens_extra) + list(C.values()) + [eps], eps=eps, order_eps=1)
    res = {}
    for p in (1, 2, 3):
        for a in range(8):
            for b in range(8):
                val = lovelock(G.Rmix, p, a, b, trunc=G.trunc, zero=G.R.zero)
                res[(p, a, b)] = sp.expand(val.as_expr()).coeff(eps, 1)
    return res, C


def symbol_matrix(res, C, ws):
    keys = list(C.keys())
    M = sp.zeros(64, len(keys))
    for a in range(8):
        for b in range(8):
            e = sp.expand(res[(1, a, b)] + ws[0] * res[(2, a, b)] + ws[1] * res[(3, a, b)])
            for j, k in enumerate(keys):
                M[8 * a + b, j] = sp.factor(sp.diff(e, C[k]))
    return M, keys


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    one = sp.Symbol('one')

    # ---------------- LN1: conventions
    F = sp.Function('F')
    gs = sp.diag(1, sp.exp(2 * F(X[0])), 1, 1, -1, -1, -1, -1)          # unit 2-sphere: F = ln sin x0 at x0 = pi/2
    Gs = PointGeometry(gs, [F(X[0])], {F: 'F'}, {'F_00': -1}, [one])
    sphere = Gs.Rmix.get((0, 1, 0, 1))
    g22 = lovelock(Gs.Rmix, 1, 2, 2)
    g00 = lovelock(Gs.Rmix, 1, 0, 0)
    random.seed(3)
    gr = sp.zeros(8, 8)
    for a in range(8):
        for b in range(a, 8):
            e = ETA[a] if a == b else 0
            for k in range(8):
                e += sp.Rational(random.randint(-3, 3), 7) * X[k]
                for m in range(k, 8):
                    e += sp.Rational(random.randint(-3, 3), 11) * X[k] * X[m]
            gr[a, b] = gr[b, a] = e
    Gr = PointGeometry(gr, [], {}, {}, [one])
    R = Gr.R
    n = 8
    Ric = [[sum((mixed(Gr, a, c, b, c) for c in range(n)), R.zero) for b in range(n)] for a in range(n)]
    Rs = sum((Ric[a][a] for a in range(n)), R.zero)
    einstein = all(lovelock(Gr.Rmix, 1, a, b, zero=R.zero) - (Ric[a][b] - (Rs * QQ(1, 2) if a == b else 0)) == 0
                   for a in range(n) for b in range(n))
    Rm4 = {(a, b, c, d): mixed(Gr, a, b, c, d) for a in range(n) for b in range(n) for c in range(n) for d in range(n)}
    L2 = (Rs * Rs - 4 * sum((Ric[a][b] * Ric[b][a] for a in range(n) for b in range(n)), R.zero)
          + sum((Rm4[(a, b, c, d)] * Rm4[(c, d, a, b)] for a in range(n) for b in range(n) for c in range(n)
                 for d in range(n)), R.zero))
    trE2 = sum((lovelock(Gr.Rmix, 2, a, a, zero=R.zero) for a in range(n)), R.zero)
    # the cubic Lovelock density (all indices in the mixed positions R^{ab}_{cd}; g = eta at the point)
    ric2 = sum((Ric[a][b] * Ric[b][a] for a in range(n) for b in range(n)), R.zero)
    ric3 = sum((Ric[a][b] * Ric[b][c] * Ric[c][a] for a in range(n) for b in range(n) for c in range(n)), R.zero)
    riem2 = L2 - Rs * Rs + 4 * ric2
    t4 = sum((Ric[a][b] * Ric[c][d] * Rm4[(b, d, a, c)] for a in range(n) for b in range(n) for c in range(n)
              for d in range(n) if Ric[a][b] != 0 and Ric[c][d] != 0), R.zero)
    t6 = sum((Ric[b][a] * Rm4[(a, e, c, d)] * Rm4[(c, d, b, e)] for a in range(n) for b in range(n) for c in range(n)
              for d in range(n) for e in range(n) if Ric[b][a] != 0), R.zero)
    t7 = sum((Rm4[(a, b, c, d)] * Rm4[(c, d, e, f)] * Rm4[(e, f, a, b)] for a in range(n) for b in range(n)
              for c in range(n) for d in range(n) for e in range(n) for f in range(n)), R.zero)

    def q(a, c, b, d):                    # R^a_c^b_d = eta^aa eta^bb R_{acbd}, R_{acbd} = eta_aa eta_cc R^{ac}_{bd}
        return ETA[a] * ETA[b] * ETA[a] * ETA[c] * Rm4[(a, c, b, d)]
    t8 = sum((q(a, c, b, d) * q(c, e, d, f) * q(e, a, f, b) for a in range(n) for b in range(n) for c in range(n)
              for d in range(n) for e in range(n) for f in range(n)), R.zero)
    L3 = Rs ** 3 - 12 * Rs * ric2 + 16 * ric3 + 24 * t4 + 3 * Rs * riem2 - 24 * t6 + 4 * t7 - 8 * t8
    trE3 = sum((lovelock(Gr.Rmix, 3, a, a, zero=R.zero) for a in range(n)), R.zero)
    Gb = PointGeometry(background(), [FA, FB], NAMES, {'fa_0': -1, 'fb_0': -1}, [one])
    per = {p: tuple(sp.Integer(sp.sympify(lovelock(Gb.Rmix, p, i, i, zero=Gb.R.zero).as_expr())) for i in (1, 4, 0, 5))
           for p in (1, 2, 3)}
    per_ok = all(tuple(int(v) for v in per[p]) == want for p, want in
                 ((1, (15, 21, 15, 15)), (2, (-180, -420, -180, -180)), (3, (360, 2520, 360, 360))))
    ok1 = (sphere == 1 and g22 == -1 and g00 == 0 and einstein and trE2 + 2 * L2 == 0 and trE3 + L3 == 0 and per_ok)
    out['LN1'] = {'sphere_R0101': str(sphere), 'einstein': einstein, 'trace_E2_plus_2_L2': str(trE2 + 2 * L2),
                  'trace_E3_plus_L3': str(trE3 + L3),
                  'static_block_per_order_11_44_00_55': {str(p): [str(v) for v in per[p]] for p in per}}
    rep.check('LN1_conventions', ok1,
              'unit sphere R^{01}_{01} = %s, G^2_2 = %s, G^0_0 = %s; random metric: E_(1) = Einstein tensor %s, '
              'tr E_(2) = -2 L_GB %s, tr E_(3) = -L_3 %s; static block per unit weight (x1, x4, sigma, x5): %s' % (
                  sphere, g22, g00, einstein, trE2 + 2 * L2 == 0, trE3 + L3 == 0,
                  {p: tuple(str(v) for v in per[p]) for p in per}))

    # ---------------- LN2: the static block, an arbitrary perturbation
    random.seed(11)
    eps = sp.Symbol('eps')
    g = background()
    for a in range(8):
        for b in range(a, 8):
            e = sp.S(0)
            for k in range(8):
                e += sp.Rational(random.randint(-5, 5), 3) * X[k]
                for m in range(k, 8):
                    e += sp.Rational(random.randint(-5, 5), 7) * X[k] * X[m]
            e += sp.Rational(random.randint(-5, 5), 2)
            g[a, b] += eps * e
            if a != b:
                g[b, a] += eps * e
    G = PointGeometry(g, [FA, FB], NAMES, {'fa_0': -1, 'fb_0': -1}, [eps], eps=eps, order_eps=1)
    dE = {}
    for p in (1, 2, 3):
        for a in range(8):
            for b in range(8):
                dE[(p, a, b)] = sp.expand(lovelock(G.Rmix, p, a, b, trunc=G.trunc, zero=G.R.zero).as_expr()).coeff(eps, 1)
    # X2: the part of the linearised Einstein operator with the time (index 4) among a, c1, c2; X3 the rest
    with_time = {k: v for k, v in G.Rmix.items() if 4 in (k[0], k[1])}     # lower pair contains the time
    X2 = {}
    for a in range(8):
        for b in range(8):
            if a == 4:
                X2[(a, b)] = dE[(1, a, b)]
            else:
                X2[(a, b)] = sp.expand(lovelock(with_time, 1, a, b, trunc=G.trunc, zero=G.R.zero).as_expr()).coeff(eps, 1)
    X3 = {k: sp.expand(dE[(1,) + k] - X2[k]) for k in X2}
    Fp = {1: (1, 1), 2: (-24, -40), 3: (72, 360)}
    decomp = all(sp.expand(dE[(p, a, b)] - Fp[p][0] * X3[(a, b)] - Fp[p][1] * X2[(a, b)]) == 0
                 for p in (1, 2, 3) for a in range(8) for b in range(8))
    rel = all(sp.expand(dE[(3, a, b)] + 18 * dE[(2, a, b)] + 360 * dE[(1, a, b)]) == 0 for a in range(8) for b in range(8))
    nz_einstein = sum(1 for a in range(8) for b in range(8) if dE[(1, a, b)] != 0)
    nz_x2 = sum(1 for k in X2 if X2[k] != 0)
    nz_x3 = sum(1 for k in X3 if X3[k] != 0)
    tot_new = [sp.expand(dE[(1, a, b)] + W_NEW[0] * dE[(2, a, b)] + W_NEW[1] * dE[(3, a, b)])
               for a in range(8) for b in range(8)]
    w3l = sp.Rational(1, 720)
    ratio = {sp.nsimplify(sp.expand(dE[(1, a, b)] + 18 * w3l * dE[(2, a, b)] + w3l * dE[(3, a, b)]) / dE[(1, a, b)])
             for a in range(8) for b in range(8) if dE[(1, a, b)] != 0}
    ok2 = (decomp and rel and nz_einstein == 64 and nz_x2 > 0 and nz_x3 > 0 and all(t == 0 for t in tot_new)
           and ratio == {sp.Rational(1, 2)})
    out['LN2'] = {'decomposition_F3_F2': {str(p): list(v) for p, v in Fp.items()}, 'decomposition_holds': decomp,
                  'dE3_plus_18_dE2_plus_360_dE1_zero': rel, 'nonzero_einstein_components': nz_einstein,
                  'nonzero_X2_X3': [nz_x2, nz_x3], 'corrected_weights_max_component': str(max(abs(t) for t in tot_new)),
                  'line_w2_18w3_ratio_to_einstein_at_w3_1_720': [str(r_) for r_ in ratio]}
    rep.check('LN2_static_block_arbitrary_perturbation', ok2,
              'all 36 components of delta g with random values and first and second derivatives: dE_(p) = F_p(3) X3 + '
              'F_p(2) X2 with (F(3), F(2)) = %s (X3, X2 the parts of the linearised Einstein operator without and with the '
              'time among a, c1, c2; %d and %d nonzero components): %s; dE_(3) = -18 dE_(2) - 360 dE_(1): %s; corrected '
              'weights: the whole linearised bulk operator vanishes in all 64 components: %s; on the line w2 = 18 w3 '
              '(w3 = 1/720) it is %s times the linearised Einstein operator' % (
                  Fp, nz_x2, nz_x3, decomp, rel, all(t == 0 for t in tot_new), sorted(ratio)))

    # ---------------- LN3: the family of static blocks of curvature -y H^2, from the curvature
    k_ = sp.Symbol('k')
    y = sp.Symbol('y')
    Gy = PointGeometry(background(), [FA, FB], NAMES, {'fa_0': -k_, 'fb_0': -k_}, [k_])
    Ew = {p: sp.expand(sp.expand(lovelock(Gy.Rmix, p, 1, 1, zero=Gy.R.zero).as_expr()).subs(k_, sp.sqrt(y)))
          for p in (1, 2, 3)}
    Et = {p: sp.expand(sp.expand(lovelock(Gy.Rmix, p, 4, 4, zero=Gy.R.zero).as_expr()).subs(k_, sp.sqrt(y)))
          for p in (1, 2, 3)}
    fam_w = sp.factor(Ew[1] + W_NEW[0] * Ew[2] + W_NEW[1] * Ew[3] - 7)
    fam_t = sp.factor(Et[1] + W_NEW[0] * Et[2] + W_NEW[1] * Et[3] - 7)
    ok3 = (Ew == {1: 15 * y, 2: -180 * y ** 2, 3: 360 * y ** 3} and Et == {1: 21 * y, 2: -420 * y ** 2, 3: 2520 * y ** 3}
           and sp.expand(fam_w - (y - 1) ** 2 * (y - 7)) == 0 and sp.expand(fam_t - 7 * (y - 1) ** 3) == 0)
    out['LN3'] = {'warped_per_order': {str(p): str(v) for p, v in Ew.items()},
                  'time_per_order': {str(p): str(v) for p, v in Et.items()},
                  'corrected_warped_minus_7': str(fam_w), 'corrected_time_minus_7': str(fam_t)}
    rep.check('LN3_degenerate_family', ok3,
              'static blocks of curvature -y H^2 by direct computation: per unit weight %s (warped) and %s (time); with the '
              'corrected weights and Lambda = -7 H^2: %s H^2 and %s H^2 (a double and a triple root at y = 1)' % (
                  Ew, Et, fam_w, fam_t))

    # ---------------- LN4 and LN5: principal symbols on the two vacuum branches
    A, A1 = sp.symbols('A A1', real=True)
    pts = [{A: 0, A1: 0}, {A: sp.Rational(1, 3), A1: sp.Rational(1, 7)}, {A: sp.Rational(1, 10), A1: -sp.Rational(3, 200)}]
    branches = {'frozen': {'fa_0': -1, 'fa_4': A, 'fa_44': A1, 'fb_0': -1},          # U = A: fb independent of x4
                'static_space': {'fa_0': -1, 'fb_0': -1, 'fb_4': A, 'fb_44': A1}}    # A = 0: here A, A1 stand for U, U1
    ranks = {}
    entries = {}
    for br, vals in branches.items():
        for nm, coord in (('x4', X[4]), ('x3', X[3]), ('sigma', X[0])):
            res, C = principal_symbol(coord, vals, [A, A1])
            for wn, ws in (('corrected', W_NEW), ('einstein', (0, 0)), ('author', W_AUTHOR)):
                if wn != 'corrected' and nm != 'x4':
                    continue
                M, keys = symbol_matrix(res, C, ws)
                ranks[(br, nm, wn)] = [M.subs(pt).rank() for pt in pts]
                if wn == 'corrected':
                    ent = {}
                    for i in range(64):
                        for j, kk in enumerate(keys):
                            if M[i, j] != 0:
                                ent['E^%d_%d <- c%d%d' % (i // 8, i % 8, kk[0], kk[1])] = M[i, j]
                    entries[(br, nm)] = ent
    prop_A2 = all(sp.cancel(v / A ** 2).is_polynomial(A, A1) for ent in entries.values() for v in ent.values())
    ok4 = (ranks[('frozen', 'x4', 'corrected')] == [0, 0, 0] and ranks[('frozen', 'x4', 'einstein')] == [28, 28, 28]
           and ranks[('frozen', 'x4', 'author')] == [28, 28, 28] and ranks[('frozen', 'x3', 'corrected')] == [0, 10, 10]
           and ranks[('frozen', 'sigma', 'corrected')] == [0, 16, 16] and prop_A2
           and sp.simplify(entries[('frozen', 'x3')].get('E^5_5 <- c66', 0) + 2 * A ** 2 / 15) == 0
           and sp.simplify(entries[('frozen', 'sigma')].get('E^5_5 <- c66', 0) + A ** 2 * (A ** 2 + A1 + 2) / 10) == 0)
    ok5 = (ranks[('static_space', 'x4', 'corrected')] == [0, 0, 0]
           and ranks[('static_space', 'x3', 'corrected')] == [0, 19, 19]
           and ranks[('static_space', 'sigma', 'corrected')] == [0, 16, 16] and prop_A2)
    out['LN4_LN5'] = {'ranks_at_A_0__1_3__1_10': {'%s %s %s' % k: v for k, v in ranks.items()},
                      'entries_corrected': {'%s %s' % k: {kk: str(vv) for kk, vv in v.items()} for k, v in entries.items()},
                      'every_entry_proportional_to_A2': prop_A2}
    rep.check('LN4_frozen_branch_not_hyperbolic', ok4,
              'frozen extra times, corrected weights: rank of the principal symbol along dx4 %s for A = 0, 1/3, 1/10 (no '
              'component has a time-kinetic term; Einstein gravity alone %s, the author\'s weights %s); along dx3 %s and '
              'along d sigma %s, every entry proportional to A^2 (e.g. E^5_5 <- c66: %s along dx3, %s along d sigma): '
              'gradient terms without time-kinetic terms' % (
                  ranks[('frozen', 'x4', 'corrected')], ranks[('frozen', 'x4', 'einstein')],
                  ranks[('frozen', 'x4', 'author')], ranks[('frozen', 'x3', 'corrected')],
                  ranks[('frozen', 'sigma', 'corrected')], entries[('frozen', 'x3')].get('E^5_5 <- c66'),
                  entries[('frozen', 'sigma')].get('E^5_5 <- c66')))
    rep.check('LN5_static_space_branch_not_hyperbolic', ok5,
              'static ordinary space (A = 0, rate U of b4), corrected weights: ranks along dx4 %s, along dx3 %s, along '
              'd sigma %s for U = 0, 1/3, 1/10 (every entry proportional to U^2)' % (
                  ranks[('static_space', 'x4', 'corrected')], ranks[('static_space', 'x3', 'corrected')],
                  ranks[('static_space', 'sigma', 'corrected')]))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'linear.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_linear.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'linear_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
