#!/usr/bin/env python3
"""um3_background.py - the background of UM-3 (SOLUTION.md, order 0 of the power series FE-35) with the corrected
Lovelock weights w = (1, 1/20, 1/360), Lambda = -7 H^2 (the author's order of 2026-10-25 07:55): which expansion histories
the author's metric admits, what they require, and the author's ad hoc Higgs vacuum on that background.

Inputs: the exact bulk equations FE-29 and fold equations FE-30 of the author's metric (outputs of um3_geometry.py and
um3_fold.py, restated here as polynomials in A = a4'/H, U = b4'/(H b4), A1 = A'/H, U1 = U'/H; the scale factor of the
extra times on the fold is c = e^{-a4} b4, its rate v = c'/c = (U - A) H).  Computed and checked:
  BG0  the restated polynomials equal the stored outputs component by component;
  BG1  the vacua: with constant rates the bulk equations hold exactly on the two lines A = 0 (static ordinary space, any
       b4) and U = A (frozen extra times, any a4); for any a4(x4), b4(x4) the energy constraint
       kappa T^(4)_(4) = A^3 (A - U)^3 H^2 has no second time derivative, so a bulk without any source is at every
       instant on one of the two branches, and on them every component vanishes;
  BG2  off the branches the bulk source starts at the fourth order in the rates (A, U first order, A1, U1 second): the
       bulk is a vacuum to third order for any a4(x4), b4(x4); no stabiliser, no bulk medium, no violation of the null
       energy condition;
  BG3  the primordial era: the author's vacuum (A = 1, U = 0) is not a solution (it would need kappa rho_bulk = -H^2);
       with the volume of the extra times held fixed a vacuum energy on the fold inflates ordinary space exactly as in
       general relativity, the fold fluid adding the pressure along the extra times that the junction requires; with a
       free volume a vacuum energy of the fold inflates the extra times together with ordinary space (U = 2A to second
       order), and no constant-rate solution exists near the static block beyond that order;
  BG4  the fold factor Z(x4) = V_t c^3/V_*: d ln Z/dx4 = 3v, zero with frozen extra times, 3AH with a free volume during
       inflation (Newton's constant, the squares of the gauge and Yukawa couplings and the quartic Higgs coupling, all
       divided by Z, fall like e^{-3N} over N e-folds);
  BG5  the ad hoc Higgs vacuum Phi = (A_c, v)/sqrt 2 (A_c = v_A e^{-2 a40 x4}) is an SU(2) rotation of (0, V)/sqrt 2 with
       V = sqrt(v^2 + A_c^2): with the pure-gauge background W^2_{x4} = theta'/g2 (tan(theta/2) = A_c/v) the isospin
       charge density of the Higgs field vanishes (the Gauss law of FE-17 for homogeneous fields, which the literal ad hoc
       vacuum violates), and the Higgs equation reduces to one radial residual
       R_V = V'' + 3 (b4'/b4) V' + lambda A_c^2 V + c_Phi <Psibar P_L Psi> V;
  BG6  numbers: R_V / (lambda v^3) and the energy density of the ad hoc vacuum for a40/v = 0.1, 1, 10 at x4 = 0, and the
       time after which A_c < 1e-3 v.
Writes outputs/background.json and reports/background_checks.json.
Usage: python universe_model_3/code/um3_background.py

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
import math
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

A, U, A1, U1 = sp.symbols('A U A1 U1', real=True)

# FE-29: kappa T_bulk^a_b / H^2 for the author's metric with the corrected weights w = (1, 1/20, 1/360), Lambda = -7 H^2
# (sigma > 0 side for the flux; the author's order of 2026-10-25 07:55)
T00 = -A*(A - U)*(A**4 - 2*A**3*U + 10*A**2*U**2 + 3*A**2*U1 + 6*A**2 + 12*A*A1*U - 9*A*U**3 - 9*A*U*U1 - 6*A*U
                  - 6*A1*U**2 - 6*U**2) / 5
Tii = -A*(A - U)**2*(A**3 - 4*A**2*U - 5*A*A1 + 3*A*U**2 + 3*A*U1 + 6*A + 2*A1*U + 12*U) / 5
T44 = A**3*(A - U)**3
Trr = -A**2*(A - U)*(A**3 + A**2*U + 5*A*A1 - 2*A*U**2 - 2*A*U1 + 6*A - 3*A1*U - 18*U) / 5
T04 = 3*A**2*U*(A - U)**2                     # times sgn(sigma)
# FE-30: kappa S^a_b / H, the source of the fold
Sii = 2*(9*A**4 - 24*A**3*U - 12*A**2*A1 + 27*A**2*U**2 + 12*A**2*U1 - 24*A**2 + 24*A*A1*U - 6*A*U**3 - 12*A*U*U1
         + 48*A*U - 6*A1*U**2 + 8*A1 - 6*U**4 - 6*U**2*U1 - 48*U**2 - 24*U1 - 48) / 15
S44 = -4*(3*A**4 - 6*A**3*U - 4*A**2 + 3*A*U**3 + 4*A*U + 4*U**2 + 8) / 5
Srr = 2*(9*A**4 - 12*A**3*U + 12*A**2*A1 + 9*A**2*U**2 - 24*A**2 - 12*A*U**3 - 12*A*U*U1 - 6*A1*U**2 - 8*A1
         - 24*U**2 - 16*U1 - 48) / 15
LAMBDA_F = sp.Rational(32, 5)                 # kappa lambda_F / H, the tension of the static block


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def lowest_order(e):
    """The lowest total order of e in the rates (A, U of order 1; A1, U1 of order 2) and the terms of that order."""
    s = sp.Symbol('s_ord')
    es = sp.expand(e.subs({A: s * A, U: s * U, A1: s ** 2 * A1, U1: s ** 2 * U1}, simultaneous=True))
    for k in range(0, 13):
        c = es.coeff(s, k)
        if c != 0:
            return k, sp.factor(c)
    return None, 0


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- BG0: the restated polynomials against the stored outputs of um3_geometry.py and um3_fold.py
    geo = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())['field_equations_lhs_over_H2']
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())['fold_source_kappaS']
    loc = {'A': A, 'U': U, 'Ad': A1, 'Ud': U1, 'H': sp.Symbol('H', positive=True)}
    Hs = loc['H']
    g = {k: sp.sympify(v, locals=loc) for k, v in geo.items()}
    f = {k: sp.sympify(v, locals=loc) for k, v in fold.items()}
    # geometry.json is stored on 0 < z < pi/2 (sigma < 0): the diagonal components are the same on both sides, the flux
    # kappa T^(0)_(4) changes sign
    ok0 = (sp.expand(g['x0,x0'] - T00) == 0 and sp.expand(g['x1,x1'] - Tii) == 0 and sp.expand(g['x4,x4'] - T44) == 0
           and sp.expand(g['x5,x5'] - Trr) == 0 and sp.expand(g['x0,x4'] + T04) == 0
           and sp.expand(f['x1,x1'] / Hs - Sii) == 0 and sp.expand(f['x4,x4'] / Hs - S44) == 0
           and sp.expand(f['x5,x5'] / Hs - Srr) == 0)
    rep.check('BG0_restated_equations', ok0,
              'the polynomials FE-29 (bulk, kappa T/H^2) and FE-30 (fold, kappa S/H) restated in this program equal the outputs '
              'of um3_geometry.py and um3_fold.py component by component (corrected weights w = (1, 1/20, 1/360), Lambda = '
              '-7 H^2)')

    # ---------------- BG1: the vacua
    const = {A1: 0, U1: 0}
    eqs = [sp.expand(5 * e.subs(const)) for e in (T00, Tii, T44, Trr)] + [sp.expand(T04.subs(const))]
    gb = sp.groebner(eqs, A, U, order='lex')
    gb_exprs = [sp.factor(x) for x in gb.exprs]
    sols = sp.solve(eqs, [A, U], dict=True)
    # any a4(x4), b4(x4): the energy constraint T44 = A^3 (A - U)^3 has no second time derivative; it vanishes only for
    # A = 0 or U = A, and on these branches (with A1 = 0, resp. U1 = A1) every component vanishes
    br_static = all(sp.expand(e.subs({A: 0, A1: 0})) == 0 for e in (T00, Tii, T44, Trr, T04))
    br_frozen = all(sp.expand(e.subs({U: A, U1: A1})) == 0 for e in (T00, Tii, T44, Trr, T04))
    no_second = T44.free_symbols <= {A, U} and T04.free_symbols <= {A, U}
    ok1 = (sorted(str(s_) for s_ in sols) == sorted(['{A: 0}', '{U: A}']) and br_static and br_frozen and no_second
           and sp.factor(T44) == A ** 3 * (A - U) ** 3)
    out['BG1'] = {'groebner_basis_constant_rates': [str(x) for x in gb_exprs], 'solutions': [str(s_) for s_ in sols],
                  'kappa_T44_over_H2': str(sp.factor(T44)), 'kappa_T04_over_H2': str(sp.factor(T04)),
                  'static_space_branch_vacuum': br_static, 'frozen_branch_vacuum': br_frozen}
    rep.check('BG1_vacuum_branches', ok1,
              'with constant rates the bulk equations hold exactly on the two lines %s (Groebner basis %s); for any a4(x4), '
              'b4(x4) the energy constraint kappa T^(4)_(4) = %s H^2 (no second time derivative) vanishes only for A = 0 or '
              'U = A, and on these branches every component vanishes: a bulk without any source has at every instant either '
              'static ordinary space (A = 0, any b4) or frozen extra times (U = A, any a4); the static block lies on both, the '
              'expanding fold with frozen extra times on the second, and the author\'s vacuum (A = 1, U = 0) on neither' % (
                  [str(s_) for s_ in sols], [str(x) for x in gb_exprs], sp.factor(T44)))

    # ---------------- BG2: off the branches the bulk is a vacuum to third order in the rates
    orders = {nm: lowest_order(e) for nm, e in (('sigma', T00), ('space', Tii), ('time', T44), ('extra', Trr), ('flux', T04))}
    ok2 = (orders['sigma'][0] == 4 and orders['space'][0] == 4 and orders['extra'][0] == 4 and orders['time'][0] == 6
           and orders['flux'][0] == 5)
    out['BG2'] = {nm: {'order': o, 'leading_terms': str(t)} for nm, (o, t) in orders.items()}
    rep.check('BG2_bulk_vacuum_to_third_order', ok2,
              'counting A, U as first order and A1, U1 as second, the bulk source that a history off the two branches needs '
              'starts at order %s (sigma: %s), %s (ordinary space: %s), %s (extra times: %s), %s (energy: %s) and %s (flux: '
              '%s): the bulk is a vacuum to third order in the rates for any a4(x4), b4(x4); the stabiliser and the bulk media '
              'that the author\'s weights required, and their violation of the null energy condition, are gone' % (
                  orders['sigma'][0], orders['sigma'][1], orders['space'][0], orders['space'][1], orders['extra'][0],
                  orders['extra'][1], orders['time'][0], orders['time'][1], orders['flux'][0], orders['flux'][1]))

    # ---------------- BG3: the primordial era
    av = {A: 1, U: 0, A1: 0, U1: 0}
    need_av = [sp.nsimplify(e.subs(av)) for e in (T00, Tii, T44, Trr, T04)]
    ok3a = need_av == [-sp.Rational(7, 5), -sp.Rational(7, 5), 1, -sp.Rational(7, 5), 0]
    # inflation on the fold with the volume of the extra times held fixed (U = A, A1 = 0): kappa rho_m = (16/5) A^2 H,
    # kappa p_m = -kappa rho_m (a vacuum energy), kappa q required = -(4/5)(8 A^2 + A^4) H
    fro_ds = {U: A, U1: 0, A1: 0}
    rho_m = sp.expand(-S44.subs(fro_ds) - LAMBDA_F)
    p_m = sp.expand(Sii.subs(fro_ds) + LAMBDA_F)
    q_m = sp.expand(Srr.subs(fro_ds) + LAMBDA_F)
    ok3b = (sp.expand(rho_m - sp.Rational(16, 5) * A ** 2) == 0 and sp.expand(p_m + rho_m) == 0
            and sp.expand(q_m + sp.Rational(4, 5) * (8 * A ** 2 + A ** 4)) == 0)
    extra_q = sp.factor(sp.expand(q_m + rho_m))                 # what the fold fluid adds to the q = -rho of the vacuum energy
    # inflation with a free volume: constant rates, a fold source that is a seven-dimensional vacuum energy (isotropic)
    iso = [sp.factor(sp.expand((Sii - S44).subs(const))), sp.factor(sp.expand((Srr - S44).subs(const)))]
    iso_sols = sp.solve(iso, [A, U], dict=True)
    real_iso = sorted({(sp.nsimplify(s_[A]), sp.nsimplify(s_[U])) for s_ in iso_sols if s_[A].is_real and s_[U].is_real},
                      key=lambda t: float(t[0]))
    lead_iso = [lowest_order(e) for e in iso]
    at_2A = [sp.factor(sp.expand(e.subs(U, 2 * A))) for e in iso]
    ok3c = (real_iso == [(-sp.Rational(4, 3), 0), (0, 0), (sp.Rational(4, 3), 0)]
            and sp.expand(lead_iso[0][1] - sp.Rational(16, 5) * (A - U) * (U - 2 * A)) == 0
            and sp.expand(lead_iso[1][1] - sp.Rational(16, 5) * A * (U - 2 * A)) == 0
            and at_2A == [2 * A ** 4, 2 * A ** 4])
    out['BG3'] = {'author_vacuum_needs_kappaT_over_H2_sigma_x1_x4_x5_flux': [str(x) for x in need_av],
                  'inflation_volume_held': {'kappa_rho_m_over_H': str(rho_m), 'kappa_p_m_over_H': str(p_m),
                                            'kappa_q_required_over_H': str(q_m),
                                            'kappa_q_added_by_the_fold_fluid_over_H': str(extra_q)},
                  'inflation_volume_free': {'isotropy_conditions': [str(e) for e in iso],
                                            'real_constant_rate_solutions': [str(t) for t in real_iso],
                                            'second_order': [str(t[1]) for t in lead_iso],
                                            'remainder_at_U_2A': [str(e) for e in at_2A]}}
    rep.check('BG3_primordial_era', ok3a and ok3b and ok3c,
              'the author\'s vacuum (A = 1, U = 0) is not a solution of the corrected equations: it would need the bulk source '
              'kappa T/H^2 = %s (sigma, ordinary space, time, extra times, flux), kappa rho_bulk = -H^2; with the volume of the '
              'extra times held fixed (U = A) a vacuum energy on the fold, kappa rho_m = %s H = -kappa p_m, gives an '
              'exponential expansion with a4\' = A H exactly as in general relativity, and the fold fluid adds the pressure '
              'kappa(q - (-rho_m)) = %s H along the extra times; with a free volume a vacuum energy of the fold (the same in '
              'all seven directions) needs, at constant rates, %s = 0 and %s = 0, whose real solutions are (A, U) = %s: near the '
              'static block only to second order, where both require U = 2A (the extra times inflate together with ordinary '
              'space, a seven-dimensional de Sitter fold), with the remainders %s at U = 2A' % (
                  [str(x) for x in need_av], rho_m, extra_q, iso[0], iso[1], [str(t) for t in real_iso],
                  [str(e) for e in at_2A]))

    # ---------------- BG4: the fold factor
    # Z ~ (e^{-a4} b4)^3: d ln Z/dx4 = 3 H (U - A) = 3 v
    zr = {'frozen_extra_times': sp.Integer(0), 'free_volume_inflation_U_2A': 3 * A, 'author_vacuum_record': -3}
    ok4 = zr['frozen_extra_times'] == 0 and sp.expand(3 * (2 * A - A) - zr['free_volume_inflation_U_2A']) == 0
    Nf = sp.Symbol('N', positive=True)
    out['BG4'] = {'dlnZ_dx4_over_H': {k: str(v) for k, v in zr.items()},
                  'coupling_change_after_N_efolds_free_volume': str(sp.exp(-3 * Nf))}
    rep.check('BG4_fold_factor', ok4,
              'd ln Z/dx4 = 3H(U - A) = 3 v: 0 with frozen extra times (the couplings of the fold stay constant); with a free '
              'volume during an inflation of N e-folds of ordinary space (U = 2A) Z grows like e^{3N} and Newton\'s constant, '
              'the squares of the gauge and Yukawa couplings (g_eff^2 = g^2/Z) and the quartic Higgs coupling fall like '
              'e^{-3N}; record: the author\'s vacuum (A = 1, U = 0) had d ln Z/dx4 = -3H')

    # ---------------- BG5: the ad hoc vacuum as a rotated, displaced Higgs modulus
    x4 = sp.Symbol('x4', real=True)
    v, vA, a40, g2, lam, cn, Hs, u_ = sp.symbols('v v_A a40 g2 lambda c_n H u', positive=True)
    Ac = vA * sp.exp(-2 * a40 * x4)
    b4 = sp.exp(u_ * Hs * x4)                 # b4 = e^{U H x4} with constant U = u (b4'/b4 = u H)
    mu2 = -lam * v**2
    Phi = sp.Matrix([Ac, v]) / sp.sqrt(2)
    tau2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    theta = 2 * sp.atan(Ac / v)
    W = sp.diff(theta, x4) / g2

    def D4(F):
        return sp.diff(F, x4) - sp.I * g2 * W * (tau2 / 2) * F
    DPhi = D4(Phi)
    # isospin charge density J^{2,x4} = i[(D^4 Phi)^dag tau2/2 Phi - Phi^dag tau2/2 D^4 Phi], D^4 = -D_4
    Dup = -DPhi
    J2 = sp.simplify(sp.I * ((Dup.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup)[0]))
    Dup0 = -sp.diff(Phi, x4)
    J2_literal = sp.simplify(sp.I * ((Dup0.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup0)[0]))
    # covariant Higgs equation residual: E = -(D4 D4 Phi + 3 (b4'/b4) D4 Phi) - mu^2 Phi - 2 lam (Phi^dag Phi) Phi - c_n Phi
    PhiPhi = sp.simplify((Phi.H * Phi)[0])
    E = -(D4(DPhi) + 3 * (sp.diff(b4, x4) / b4) * DPhi) - mu2 * Phi - 2 * lam * PhiPhi * Phi - cn * Phi
    E = sp.simplify(E)
    V = sp.sqrt(v**2 + Ac**2)
    RV = sp.diff(V, x4, 2) + 3 * u_ * Hs * sp.diff(V, x4) + lam * Ac**2 * V + cn * V
    Urot = sp.Matrix([[sp.cos(theta / 2), sp.sin(theta / 2)], [-sp.sin(theta / 2), sp.cos(theta / 2)]])
    target = Urot * sp.Matrix([0, -RV]) / sp.sqrt(2)
    diff = sp.simplify(E - target)
    # numerical confirmation at random points (the symbolic simplification may leave nested radicals)
    import random as rnd
    rnd.seed(5)
    maxdev = 0.0
    for _ in range(20):
        vals = {v: rnd.uniform(0.5, 2), vA: rnd.uniform(0.1, 2), a40: rnd.uniform(0.05, 3), g2: rnd.uniform(0.3, 1),
                lam: rnd.uniform(0.05, 0.5), cn: rnd.uniform(-0.2, 0.2), Hs: rnd.uniform(0.1, 2), u_: rnd.uniform(-1, 1),
                x4: rnd.uniform(0, 2)}
        dev = max(abs(complex(sp.N(d.subs(vals)))) for d in diff)
        maxdev = max(maxdev, dev)
        maxdev = max(maxdev, abs(complex(sp.N(J2.subs(vals)))))
    lit = sp.simplify(J2_literal - a40 * v * Ac)
    ok5 = maxdev < 1e-10 and lit == 0
    out['BG5'] = {'W2_x4': str(sp.simplify(W)), 'J2_with_W': str(J2), 'J2_literal_ad_hoc': str(sp.simplify(J2_literal)),
                  'radial_residual': 'R_V = V\'\' + 3(b4\'/b4)V\' + lambda A^2 V + c_Phi<Psibar P_L Psi> V, V = sqrt(v^2 + A^2)',
                  'max_deviation': maxdev}
    rep.check('BG5_ad_hoc_vacuum_gauge_equivalence', ok5,
              'with W^2_x4 = theta\'/g2 = %s the isospin charge density of the Higgs field vanishes (the literal ad hoc vacuum has '
              'J^{2,x4} = a40 v A, which no homogeneous field can balance in the Gauss law); the covariant Higgs equation equals '
              'U(theta)(0, -R_V)/sqrt 2 with the radial residual R_V (max deviation %.1e at 20 random points)' % (
                  sp.simplify(W), maxdev))

    # ---------------- BG6: numbers for the residual and the energy of the ad hoc vacuum (units of v; lambda = 0.129)
    lam_v = 0.12941
    rows = []
    for a40_v in (0.1, 1.0, 10.0):
        for vA_v in (1.0,):
            sub = {v: 1, vA: vA_v, a40: a40_v, lam: lam_v, cn: 0, Hs: 1, u_: 0, g2: 0.6517, x4: 0}
            RV0 = float(sp.N(RV.subs(sub)))
            Vp = float(sp.N(sp.diff(V, x4).subs(sub)))
            rhoH = 0.5 * Vp**2 + lam_v / 4 * (vA_v**2) ** 2
            t3 = math.log(vA_v / 1e-3) / (2 * a40_v)
            rows.append({'a40_over_v': a40_v, 'v_A_over_v': vA_v, 'R_V_over_lambda_v3_at_x4_0': RV0 / lam_v,
                         'rho_H_over_v4_at_x4_0': rhoH, 'time_until_A_below_1e-3_v_in_units_1_over_v': t3})
    out['BG6'] = rows
    ok6 = all(r['R_V_over_lambda_v3_at_x4_0'] > 0 for r in rows)
    rep.check('BG6_numbers', ok6, '; '.join('a40 = %g v: R_V(0) = %.3g lambda v^3, rho_H(0) = %.3g v^4, A_c < 1e-3 v after %.3g/v' % (
        r['a40_over_v'], r['R_V_over_lambda_v3_at_x4_0'], r['rho_H_over_v4_at_x4_0'], r['time_until_A_below_1e-3_v_in_units_1_over_v'])
        for r in rows))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'background.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_background.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'background_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
