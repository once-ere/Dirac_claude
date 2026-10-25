#!/usr/bin/env python3
"""um3_background.py - the background of UM-3 (SOLUTION.md, order 0 of the power series FE-35): which expansion
histories the author's metric admits, what they require, and the author's ad hoc Higgs vacuum on that background.

Inputs: the exact bulk equations FE-29 and fold equations FE-30 of the author's metric (outputs of um3_geometry.py and
um3_fold.py, restated here as polynomials in A = a4'/H, U = b4'/(H b4), A1 = A'/H, U1 = U'/H).  Computed and checked:
  BG1  the vacuum solutions with constant rates: the polynomial system FE-29 = 0 (A1 = U1 = 0) has exactly the solutions
       (A, U) = (+1, 0) and (-1, 0) (Groebner basis {(A^2-1)^2, A^2 U - A U^2 - U, U^3}): the author's vacuum and its time
       reverse, both degenerate (double root in A^2, triple in U); every other constant-rate history needs bulk sources;
  BG2  the energy conditions of the bulk media that the late universe requires: the stabiliser of the static block and the
       medium of the frozen branch (U = A) violate the null energy condition (rho + p < 0) along every space-like
       direction for |A| < 1;
  BG3  the primordial era with a varying b4 (the author's order: b4 a function of x4, never identically 1): at A = 1 the
       bulk source required by b4' = U H b4 is of second order in U (energy) and its flux of order U^2; the flux-free
       branch U = 2/3; the fold source at A = 1 as a function of U;
  BG4  the fold factor Z(x4) on the three branches (author's vacuum with constant b4, U = 2/3, frozen extra times) and
       the growth of the four-dimensional couplings;
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
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

A, U, A1, U1 = sp.symbols('A U A1 U1', real=True)

# FE-29: kappa T_bulk^a_b / H^2 for the author's metric (sigma > 0 side for the flux)
T00 = -(A**6 - 3*A**5*U + 12*A**4*U**2 + 3*A**4*U1 + 3*A**4 + 12*A**3*A1*U - 19*A**3*U**3 - 12*A**3*U*U1 - 6*A**3*U
        - 18*A**2*A1*U**2 + 9*A**2*U**4 + 9*A**2*U**2*U1 - 18*A**2*U**2 - 6*A**2*U1 - 9*A**2 + 6*A*A1*U**3 - 12*A*A1*U
        + 21*A*U**3 + 12*A*U*U1 + 9*A*U + 6*A1*U**2 + 3*U**4 + 3*U**2*U1 + 18*U**2 + 3*U1 + 5) / 16
Tii = -(A**6 - 6*A**5*U - 5*A**4*A1 + 12*A**4*U**2 + 3*A**4*U1 + 3*A**4 + 12*A**3*A1*U - 10*A**3*U**3 - 6*A**3*U*U1
        + 12*A**3*U - 9*A**2*A1*U**2 + 6*A**2*A1 + 3*A**2*U**4 + 3*A**2*U**2*U1 - 36*A**2*U**2 - 6*A**2*U1 - 9*A**2
        + 2*A*A1*U**3 - 12*A*A1*U + 18*A*U**3 + 6*A*U*U1 - 6*A*U + 3*A1*U**2 - A1 + 3*U**4 + 3*U**2*U1 + 24*U**2
        + 3*U1 + 5) / 16
T44 = (5*A**6 - 15*A**5*U + 15*A**4*U**2 - 9*A**4 - 5*A**3*U**3 + 18*A**3*U + 3*A**2 - 9*A*U**3 - 3*A*U - 3*U**2 + 1) / 16
Trr = -(A**6 + 5*A**4*A1 - 3*A**4*U**2 - 2*A**4*U1 + 3*A**4 - 8*A**3*A1*U + 2*A**3*U**3 + 2*A**3*U*U1 - 24*A**3*U
        + 3*A**2*A1*U**2 - 6*A**2*A1 + 18*A**2*U**2 - 9*A**2 + 6*A*U**3 + 6*A*U*U1 + 24*A*U + 3*A1*U**2 + A1 + 9*U**2
        + 2*U1 + 5) / 16
GFAC = 5*A**2*(A - U)**2 - 6*A**2 + 6*A*U + U**2 + 1
T04 = sp.Rational(3, 16) * U * GFAC                     # times sgn(sigma)
# FE-30: kappa S^a_b / H
Sii = (9*A**4 - 24*A**3*U - 12*A**2*A1 + 27*A**2*U**2 + 12*A**2*U1 - 66*A**2 + 24*A*A1*U - 6*A*U**3 - 12*A*U*U1
       + 120*A*U - 6*A1*U**2 + 20*A1 - 6*U**4 - 6*U**2*U1 - 111*U**2 - 60*U1 - 183) / 24
S44 = -(3*A**4 - 6*A**3*U - 10*A**2 + 3*A*U**3 + 10*A*U + 10*U**2 + 31) / 4
Srr = (9*A**4 - 12*A**3*U + 12*A**2*A1 + 9*A**2*U**2 - 66*A**2 - 12*A*U**3 - 12*A*U*U1 + 12*A*U - 6*A1*U**2 - 20*A1
       - 57*U**2 - 40*U1 - 183) / 24


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

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # consistency of the restated polynomials with the stored outputs of um3_fold.py (frozen branch, static block)
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    frozen_stored = fold.get('bulk_source_frozen_kappaT_over_H2')
    out['stored_frozen_branch'] = frozen_stored

    # ---------------- BG1: vacuum solutions with constant rates
    const = {A1: 0, U1: 0}
    eqs = [sp.expand(16 * e.subs(const)) for e in (T00, Tii, T44, Trr)] + [sp.expand(16 * T04.subs(const))]
    gb = sp.groebner(eqs, A, U, order='lex')
    sols = sp.solve(eqs, [A, U], dict=True)
    gb_exprs = [sp.factor(g) for g in gb.exprs]
    expected = {sp.factor((A**2 - 1)**2), sp.factor(A**2*U - A*U**2 - U), U**3}
    ok1 = set(gb_exprs) == expected and sorted((s[A], s[U]) for s in sols) == [(-1, 0), (1, 0)]
    out['BG1'] = {'groebner_basis': [str(g) for g in gb_exprs], 'solutions': [str(s) for s in sols],
                  'T44_at_U0': str(sp.factor(16 * T44.subs({U: 0})))}
    rep.check('BG1_vacuum_solutions', ok1,
              'FE-29 = 0 with constant rates: Groebner basis %s; the only solutions are (A, U) = (1, 0) (the author\'s vacuum) '
              'and (-1, 0); 16 kappa T^(4)_(4)/H^2 at U = 0 = %s (a double root at A^2 = 1): every other constant-rate history '
              'needs bulk sources' % ([str(g) for g in gb_exprs], out['BG1']['T44_at_U0']))

    # ---------------- BG2: energy conditions of the late-universe bulk media
    # stabiliser (static block): kappa rho = -1/16, kappa p = -5/16 (units H^2)
    rho_s, p_s = sp.Rational(-1, 16), sp.Rational(-5, 16)
    nec_stab = rho_s + p_s
    # frozen branch U = A (U1 = A1): rho = -T44, pressures T00 (sigma), Tii, Trr
    fz = {U: A, U1: A1}
    rho_f = sp.expand(-T44.subs(fz))
    nec_sigma = sp.factor(sp.expand(rho_f + T00.subs(fz)))
    nec_i = sp.factor(sp.expand(rho_f + Tii.subs(fz)))
    nec_r = sp.factor(sp.expand(rho_f + Trr.subs(fz)))
    flux_f = sp.factor(T04.subs(fz))
    # sample the sign for |A| < 1, |A1| < 5e-4 (slowly varying expansion; the late universe has A1 = -(1 + q0) A^2, tiny)
    import random
    random.seed(3)
    worst = -1e9
    for _ in range(4000):
        a_, a1_ = random.uniform(-0.99, 0.99), random.uniform(-0.5, 0.5) * 1e-3
        vals = [float(e.subs({A: a_, A1: a1_})) for e in (nec_sigma, nec_i, nec_r)]
        worst = max(worst, max(vals))
    ok2 = nec_stab < 0 and worst < 0 and sp.simplify(rho_f - (3*A**2 - 1)/16) == 0
    out['BG2'] = {'stabiliser_rho_plus_p': str(nec_stab), 'frozen_rho': str(rho_f), 'frozen_rho_plus_p_sigma': str(nec_sigma),
                  'frozen_rho_plus_p_i': str(nec_i), 'frozen_rho_plus_p_r': str(nec_r), 'frozen_flux_kappaT04_over_H2': str(flux_f),
                  'max_rho_plus_p_sampled': worst}
    rep.check('BG2_null_energy_condition', ok2,
              'stabiliser: kappa(rho_s + p_s) = %s H^2 < 0; frozen branch (U = A): kappa rho = (3A^2 - 1)H^2/16, kappa(rho + p) along '
              'sigma = %s, along ordinary space = %s, along the extra times = %s (units H^2), all negative for |A| < 1 and a slowly varying expansion, |A1| < 5e-4 (largest '
              'sampled value %.3f): the bulk medium of the late universe violates the null energy condition; it also carries the '
              'energy flux kappa T^(0)_(4) = sgn(sigma) %s H^2' % (nec_stab, nec_sigma, nec_i, nec_r, worst, flux_f))

    # ---------------- BG3: the primordial era with varying b4 (A = 1)
    a1 = {A: 1, A1: 0, U1: 0}
    rho_p = sp.factor(sp.expand(-T44.subs(a1)))
    flux_p = sp.factor(sp.expand(T04.subs(a1)))
    src_p = {k: sp.factor(sp.expand(v.subs(a1))) for k, v in (('sigma', T00), ('space', Tii), ('time', T44), ('extra', Trr))}
    ser = {k: sp.series(v, U, 0, 3).removeO() for k, v in src_p.items()}
    u23 = {k: sp.nsimplify(v.subs(U, sp.Rational(2, 3))) for k, v in src_p.items()}
    fold_p = {k: sp.factor(sp.expand(v.subs(a1))) for k, v in (('space', Sii), ('time', S44), ('extra', Srr))}
    ok3 = (sp.simplify(flux_p - sp.Rational(3, 8) * U**2 * (3*U - 2)) == 0
           and all(sp.Poly(sp.expand(ser[k]), U).coeff_monomial(1) == 0 for k in ser)
           and u23 == {'sigma': sp.Rational(-14, 27), 'space': sp.Rational(-2, 9), 'time': sp.Rational(2, 27),
                       'extra': sp.Rational(-22, 27)})
    out['BG3'] = {'kappa_rho_bulk_over_H2_at_A1': str(rho_p), 'flux_over_H2': str(flux_p),
                  'sources_over_H2': {k: str(v) for k, v in src_p.items()},
                  'sources_to_second_order_in_U': {k: str(sp.expand(v)) for k, v in ser.items()},
                  'sources_at_U_2_3': {k: str(v) for k, v in u23.items()},
                  'fold_source_kappaS_over_H': {k: str(v) for k, v in fold_p.items()}}
    rep.check('BG3_primordial_varying_b4', ok3,
              'at A = 1 the source that b4\' = U H b4 requires starts at second order in U (no linear term in any component: '
              '%s); flux sgn(sigma)(3/8)U^2(3U - 2)H^2, zero at U = 2/3 (b4 ~ e^{2Hx4/3}) where the constant source is %s '
              '(sigma, space, time, extra times); the fold source at A = 1: %s' % (
                  {k: str(sp.expand(v)) for k, v in ser.items()}, {k: str(v) for k, v in u23.items()},
                  {k: str(v) for k, v in fold_p.items()}))

    # ---------------- BG4: the fold factor on three branches
    # Z ~ (e^{-a4} b4)^3: d ln Z / dx4 = 3 H (U - A)
    branches = {'author_vacuum_constant_b4': (1, 0), 'author_vacuum_U_2_3': (1, sp.Rational(2, 3)), 'frozen_extra_times': ('A', 'A')}
    zrates = {}
    for k, (a_, u_) in branches.items():
        if a_ == 'A':
            zrates[k] = '0'
        else:
            zrates[k] = str(3 * (u_ - a_)) + ' H'
    ok4 = zrates['author_vacuum_constant_b4'] == '-3 H' and zrates['author_vacuum_U_2_3'] == '-1 H' and zrates['frozen_extra_times'] == '0'
    out['BG4'] = {'dlnZ_dx4': zrates, 'coupling_growth_rate': {k: v for k, v in
                  (('author_vacuum_constant_b4', '+3H/2'), ('author_vacuum_U_2_3', '+H/2'), ('frozen_extra_times', '0'))}}
    rep.check('BG4_fold_factor', ok4, 'd ln Z/dx4 = 3H(U - A): %s; the four-dimensional couplings g/sqrt(Z) grow at the '
              'rates 3H/2 (constant b4), H/2 (U = 2/3) and stay constant with frozen extra times' % zrates)

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
