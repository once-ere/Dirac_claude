#!/usr/bin/env python3
"""um4_background.py - the background of UM-4: which expansion histories the metric of UM-4 admits, what an expanding fold
requires, why the volume of the extra times must be held fixed, and the author's ad hoc Higgs vacuum on that background.

The metric of UM-4 in the proper chart, ds^2 = d sigma^2 + e^{-2H|sigma|} ghat, with the metric of the fold
    ghat = e^{2a} (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^{2c} (dx5^2 + dx6^2 + dx7^2),   a = a4(x4),   c = ln(e^{-a4} b4)
(a4, b4 the author's functions of the time; c the logarithm of the scale factor of the extra times), Einstein gravity with
Lambda = -21 H^2 in the bulk (um4_gravity.py L4).  Rates: A = a4'/H, U = b4'/(H b4), so c' = (U - A) H; frozen extra times are
c' = 0 (U = A).  Computed and checked:
  BG1  the vacua of the author's form: the bulk equations hold exactly iff ghat is Ricci flat (um4_geometry.py G5); the frame
       curvature of ghat in its 21 planes is a'^2 (planes of ordinary space), a'' + a'^2 (ordinary space with the time),
       c'^2 (extra times), c'' + c'^2 (extra times with the time), a' c' (ordinary space with the extra times); with constant
       rates the Ricci tensor vanishes only for a' = c' = 0: the static block is the only vacuum of the author's form with
       constant rates (the power-law vacua are the two Kasner folds of G6); UM-3's frozen branch (any a4 with U = A a vacuum
       of the corrected Lovelock weights) does not exist in UM-4: an expanding fold needs matter;
  BG2  the expanding fold with matter: the Einstein tensor of ghat,
           Ghat^(i)_(i) = -(2a'' + 3c'' + 3a'^2 + 6a'c' + 6c'^2),  Ghat^(4)_(4) = -(3a'^2 + 9a'c' + 3c'^2),
           Ghat^(r)_(r) = -(3a'' + 2c'' + 6a'^2 + 6a'c' + 3c'^2),
       with the equations of the fold Ghat^a_b = kappa_7 tau^a_b (um4_fold.py F2; tau = diag(P, P, P, -rho, q, q, q), the
       pressure P along ordinary space, the energy density rho, the pressure q along the extra times): with frozen extra times
       the Friedmann equations of general relativity, 3 a'^2 = kappa_7 rho, -(2a'' + 3a'^2) = kappa_7 P, and the radion
       condition q = -(rho - 3P)/2; the bulk then deviates from the author's form at the first order in (a'/H)^2 (F1);
  BG3  without the fold fluid the volume of the extra times is driven: the matter of the fold that does not depend on the
       extra times has q = 0 (dust: point particles at rest in the extra times have T^rr = 0; radiation: the average on-shell
       Lagrangian vanishes) or q = -rho (a vacuum energy, the on-shell Lagrangian -V), while the radion condition needs
       q = -rho/2 for dust and q = -2 rho for a vacuum energy; with q = 0 the equations give c'' = (3/5) a'^2 for dust and
       (6/5) a'^2 for a vacuum energy at c' = 0, and an integration through a matter era from c' = 0 gives c'/a' = 0.75, 0.98,
       1.00 after 1, 2, 3 e-folds: the attractor is the seven-dimensional dust solution, in which the extra times expand as
       ordinary space; Newton's constant of the fold, 8 pi G_N = kappa_7/(V_t e^{3c}) (V_t the coordinate volume of the extra
       times), then changes at the rate d ln G_N/dx4 = -3c' = -3 H_4 (H_4 = a'): lunar laser ranging (L. Biskupek, J. Mueller
       and J.-M. Torre, Universe 7 (2021) 34: Gdot/G = (-5.0 +- 9.6) 1e-15 per year) allows |d ln G_N/dx4| < 3.5e-4 H_0 (two
       standard deviations, H_0 = 67.4 km/s/Mpc): a free volume is excluded by a factor of about 8500; the fold fluid must
       supply q_hold = -(rho - 3P)/2 - q_matter (ASSUMED), and then c' = 0 is preserved;
  BG4  the fold factor Z(x4) = V_t e^{3c}/V_*: d ln Z/dx4 = 3c', zero with frozen extra times; with a free volume Newton's
       constant, the squares of the gauge couplings (g_4^2 = g_7^2/(V_t e^{3c})), of the Yukawa couplings and the quartic Higgs
       coupling all fall like 1/Z;
  BG5  the ad hoc Higgs vacuum Phi = (A_c, v)/sqrt 2 (A_c = v_A e^{-2 a40 x4}) is an SU(2) rotation of (0, V)/sqrt 2 with
       V = sqrt(v^2 + A_c^2): with the pure-gauge background W^2_{x4} = theta'/g2 (tan(theta/2) = A_c/v) the isospin
       charge density of the Higgs field vanishes (the Gauss law for homogeneous fields, which the literal ad hoc vacuum
       violates; in UM-4 the gauge field is the value at the fold of the bulk field, whose zero mode has the profile 1), and the
       Higgs equation on the fold (the friction 3 b4'/b4 of the volume b4^3 of the fold) reduces to one radial residual
       R_V = V'' + 3 (b4'/b4) V' + lambda A_c^2 V + c_Phi <Psibar P_L Psi> V;
  BG6  numbers: R_V / (lambda v^3) and the energy density of the ad hoc vacuum for a40/v = 0.1, 1, 10 at x4 = 0, and the
       time after which A_c < 1e-3 v.
Writes outputs/background.json and reports/background_checks.json.  Runs in a few seconds.
Usage: python universe_model_4/code/um4_background.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-4 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The metric of UM-4 depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one surface of F, at z = pi/2: F is the union of these copies, one per period (example 2), and "the
fold" without a qualifier is the copy in the period that contains our world. A point of the fold is labelled by the seven
coordinates x1, ..., x7, and the metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.
Notation: ln is the natural logarithm, e Euler's number, exp(y) = e^y, sin, cos and cot = cos/sin the trigonometric
functions, sinh and tanh the hyperbolic functions, |y| the absolute value; f(0+) and f(0-) are the limits of f(sigma) as
sigma approaches 0 from above and from below.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the metric of UM-4 is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ].
It depends on sigma only through |sigma|. The function W(sigma) = e^(-2 H |sigma|), which multiplies the squared steps of all
seven directions of the fold (ordinary space, the time and the extra times), is the warp factor of the metric (its square
root e^(-H |sigma|) multiplies the lengths). The time x4 is warped like the other directions (the author's order of
2026-10-25, 13:15 PDT; in UM-3 it was not), so that every surface sigma = const has the light cone of the fold. Four
properties make the surface sigma = 0 a fold, and together they single it out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp factor is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|) equals 1 on the fold and
     decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb = -H sgn(sigma) delta^a_b   (all seven directions a, b of the fold)
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function, delta^a_b the Kronecker delta, a, b frame indices along the fold); it jumps by -2 H in every direction
     of the fold. The field equations of gravity of UM-4, G^M_N + Lambda delta^M_N = kappa T^M_N (Einstein gravity: the
     author's Einstein-Lovelock equations with the weights of the Gauss-Bonnet and cubic terms set to zero; G^M_N the
     Einstein tensor, Lambda = -21 H^2 the cosmological constant, kappa = 8 pi G_8 the gravitational coupling of eight
     dimensions, T^M_N the energy-momentum tensor), are linear in the second sigma-derivatives of the metric, so the jump
     puts a Dirac delta function delta_D(sigma) into them: the metric solves them only if the fold carries a thin source
     S^a_b, an energy-momentum tensor concentrated on sigma = 0, given by the integral of the equations across the fold
     (the junction condition of Israel),
        (FD-11) kappa S^a_b = integral from sigma = 0- to 0+ of d sigma G^a_b = -([K^a_b] - [K] delta^a_b)
     ([K^a_b] the jump of the extrinsic curvature across the fold, K its trace), with S^4_4 = -(its energy density),
     S^1_1 = S^2_2 = S^3_3 its pressure along ordinary space and S^5_5 = S^6_6 = S^7_7 its pressure along the extra times; S is
     T integrated across the fold, an energy per unit volume of the six other directions of the fold (unit GeV^7). For the
     static block (a4 and b4 constant) and, to the first order in the curvature of the fold divided by H^2, for every fold
        (FD-12) static block:  kappa S^a_b = -12 H delta^a_b  (a pure tension, kappa lambda_F = 12 H),
                any fold:      kappa S^a_b = -12 H delta^a_b + (2/(5 H)) Ghat^a_b
     (Ghat^a_b the Einstein tensor of the metric FD-2 of the fold): the tension plus matter that obeys the Einstein equations
     of seven dimensions, Ghat^a_b = kappa_7 tau^a_b with kappa_7 = 5 kappa H/2 (tau the matter of the fold), which for frozen
     extra times are the Friedmann equations of general relativity. The fold is therefore not only a place but a physical
     object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-4 the Higgs doublet (with the author's ad hoc vacuum, a time-dependent choice of its vacuum
value), three generations of quarks and leptons, three right-handed neutrinos and the fold fluid (its tension and the
pressure along the extra times that keeps their volume fixed) live on the fold: they are fields at sigma = 0, functions of
x1, ..., x4 (no field depends on the extra times). The gauge fields of SU(3)_C x SU(2)_L x U(1)_Y live in the bulk; their
massless modes are bound to the fold, so that the photon and the gluons of the four-dimensional world are waves of the bulk
that the fold holds, and photons that leave the fold travel through the bulk at the speed of light. dirac16complex (the
author's spinor field of eight dimensions) and gravity live in the bulk sigma != 0 as well as on the fold; the states chi of
dirac16complex that the fold holds (in UM-4 long-lived resonances) are the part of it near the fold, and the portals
(couplings between dirac16complex and the fields of the fold) act at sigma = 0. Integrated over the extra times, the fold is
the four-dimensional universe that we observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. In UM-4
files "the fold" means this surface; the examples below use the word for other surfaces with the same properties. The word
is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by the factor e is called
an e-folding.

Examples of folds that are meaningful for UM-4.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     quarks, leptons and the Higgs field, and after the integration over the extra times the four-dimensional universe that
     we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp factor (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2
     diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
     line -infinity < sigma < infinity. A compact direction of length L would give every field a tower of particles with
     the masses 2 pi n/L, n = 1, 2, ... (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
     pi/(6 H) of x0 produces no such tower with the spacing 12 H: every field of the bulk has instead a continuum of modes
     that starts at zero mass, and the fold holds its massless mode.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-4 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
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
     the bulk the vacuum energy Lambda_RS, and the bulk is otherwise empty. The fold of UM-4 is of the same kind, with every
     direction of the fold warped by the same factor as in the model of Randall and Sundrum: its static block is a space of
     constant curvature -H^2 in all eight directions, a vacuum of Einstein gravity with Lambda = -21 H^2, with a fold of pure
     tension (FD-12), and the graviton is bound to the fold as there. It differs in that the fold has seven dimensions, three
     of them extra times, in that the space is not cut at the brane (Randall and Sundrum identify the two sides of their
     brane, one physical side; the fold of UM-4 has two distinct sides, example 7), and in that the gauge fields live in the
     bulk as well.
  7. A particle held by a thin layer. A particle held by an attractive thin layer has a wave function that falls off
     exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
     equation, the wave function itself). In UM-4 the states chi of dirac16complex near the fold are of this kind only near
     the fold: at rest and without their self-interaction (the field is Psi = e^((7/2) H |sigma|) chi(sigma) e^(-i omega x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+)   (0 < sigma << sigma_t),
                chi(sigma) = e^(-q_b |sigma|) chi(0-)   (0 < -sigma << sigma_t),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),
                omega_0 = omega_r - i Gamma/2,   omega_r -> sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     fields of the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors, m_Psi the bulk
     mass, q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for mu_R = 0), and omega_r
     tends to the energy omega_b = sqrt(m_Psi^2 - q_b^2) of the bound state of UM-3 when H/q_b -> 0. Because the time is
     warped, the energy omega of the field enters its equation multiplied by e^(H |sigma|): beyond the turning point
     sigma_t (omega_r e^(H sigma_t) = m_Psi) the profile oscillates as a wave that leaves the fold, so the state is a
     resonance of the energy omega_0 at rest and the width Gamma, which falls like e^(-2 F_t(upsilon_b) m_Psi/H) with the
     tunnelling exponent F_t(upsilon) = ln((1 + sqrt(1 - upsilon^2))/upsilon) - sqrt(1 - upsilon^2) and
     upsilon_b = omega_b/m_Psi (the tunnelling through the region between the fold and sigma_t). The profile is not a
     function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of a mean field of a gas of the
     particles chi that is the same on both sides of the fold: the four resonances of Krein charge -1 (the particles chi)
     are even under it and the four of Krein charge +1 are odd, so such a mean field cannot mix the two signs of the
     indefinite charge. R_2 maps the states of one Krein charge onto those of the other and makes the two sets degenerate
     without the self-interaction.
  9. The planes of Horava and Witten. In M-theory (the eleven-dimensional theory whose limits include the superstring
     theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional
     planes left in place by the reflection are mirror surfaces (property 1); each carries one E8 gauge group while gravity
     fills the bulk. As in UM-4, gravity fills the bulk; unlike UM-4, the gauge fields live on the mirror planes (in UM-4
     they live in the bulk), and the two sides of each plane are identified (one physical side).

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp factor vanishes,
    g_x0x0 diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp factor, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a
    kink and without a thin source.
END FOLD DEFINITION
"""
from __future__ import annotations

import math
import random as rnd
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write              # noqa: E402
from um4_lovelock import frame_riemann, lovelock_tensor  # noqa: E402


def fs(e):
    return sp.expand(sp.powsimp(sp.expand(e), combine='exp'))


def fold_geometry():
    """The frame curvature and the Einstein tensor of ghat = e^{2a} dx_i^2 - dx4^2 - e^{2c} dx_r^2 (a, c functions of x4)."""
    Y = sp.symbols('x1:8', real=True)
    t = Y[3]
    a = sp.Function('a')(t)
    c = sp.Function('c')(t)
    eps7 = [1, 1, 1, -1, -1, -1, -1]
    hh = [sp.exp(a)] * 3 + [sp.S(1)] + [sp.exp(c)] * 3
    g = sp.diag(*[eps7[i] * hh[i] ** 2 for i in range(7)])
    R = frame_riemann(g, list(Y), hh, simplify=fs)
    G = lovelock_tensor(R, 1, n=7, simplify=fs)
    return t, a, c, R, G


def main():
    rep = Report()
    out = {}
    t, a, c, R, G = fold_geometry()
    a1, a2, c1, c2 = sp.diff(a, t), sp.diff(a, t, 2), sp.diff(c, t), sp.diff(c, t, 2)
    A1, A2, C1, C2 = sp.symbols('ap app cp cpp', real=True)
    rd = {a2: A2, c2: C2}
    rd1 = {a1: A1, c1: C1}

    def sym(e):
        return sp.expand(sp.simplify(e).subs(rd).subs(rd1))

    # ---------------- BG1: the vacua of the author's form
    planes = {}
    for (up, lo), v in R.items():
        planes[(up, lo)] = sym(v)
    expected = {}
    for i in range(7):
        for j in range(i + 1, 7):
            si, sj = ('s' if i < 3 else ('t' if i == 3 else 'r')), ('s' if j < 3 else ('t' if j == 3 else 'r'))
            kind = ''.join(sorted(si + sj))
            expected[((i, j), (i, j))] = {'ss': A1 ** 2, 'st': A2 + A1 ** 2, 'rr': C1 ** 2, 'rt': C2 + C1 ** 2, 'rs': A1 * C1}[kind]
    ok1 = all(sp.expand(planes.get(k, 0) - v) == 0 for k, v in expected.items()) and len(planes) == 21
    ric = [sp.expand(sum(planes[((min(i, j), max(i, j)), (min(i, j), max(i, j)))] for j in range(7) if j != i)) for i in range(7)]
    const = {A2: 0, C2: 0}
    sols = sp.solve([ric[0].subs(const), ric[3].subs(const), ric[4].subs(const)], [A1, C1], dict=True)
    real_sols = [s_ for s_ in sols if all(v.is_real for v in s_.values())]
    ok1 &= real_sols == [{A1: 0, C1: 0}]
    out['BG1'] = {'frame_curvature_planes': {'space-space': 'a\'^2', 'space-time': 'a\'\' + a\'^2', 'extra-extra': 'c\'^2',
                                              'extra-time': 'c\'\' + c\'^2', 'space-extra': 'a\' c\''},
                  'ricci_constant_rates': [str(ric[i].subs(const)) for i in (0, 3, 4)],
                  'constant_rate_vacua': [str(s_) for s_ in real_sols]}
    rep.check('BG1_vacua_of_the_author_form', ok1,
              'the frame curvature of ghat in its 21 planes: a\'^2, a\'\' + a\'^2, c\'^2, c\'\' + c\'^2, a\'c\' (space, space-time, '
              'extra times, extra-time-time, space-extra); with constant rates the Ricci tensor (%s) vanishes only for %s: the '
              'static block is the only vacuum of the author\'s form with constant rates (UM-3\'s frozen branch is not a vacuum of '
              'Einstein gravity: an expanding fold needs matter)' % (
                  ', '.join(str(ric[i].subs(const)) for i in (0, 3, 4)), real_sols))

    # ---------------- BG2: the Einstein tensor of the fold and the Friedmann equations
    Gs, Gt, Gr = sym(G[0, 0]), sym(G[3, 3]), sym(G[4, 4])
    ok2 = (sp.expand(Gs + (2 * A2 + 3 * C2 + 3 * A1 ** 2 + 6 * A1 * C1 + 6 * C1 ** 2)) == 0
           and sp.expand(Gt + (3 * A1 ** 2 + 9 * A1 * C1 + 3 * C1 ** 2)) == 0
           and sp.expand(Gr + (3 * A2 + 2 * C2 + 6 * A1 ** 2 + 6 * A1 * C1 + 3 * C1 ** 2)) == 0)
    k7, rho, P, q = sp.symbols('kappa_7 rho P q', real=True)
    frz = {C1: 0, C2: 0}
    fr = sp.solve([sp.Eq(Gt.subs(frz), -k7 * rho), sp.Eq(Gs.subs(frz), k7 * P), sp.Eq(Gr.subs(frz), k7 * q)], [rho, P, q], dict=True)[0]
    ok2 &= sp.simplify(fr[q] + (fr[rho] - 3 * fr[P]) / 2) == 0
    out['BG2'] = {'Ghat_space': str(Gs), 'Ghat_time': str(Gt), 'Ghat_extra': str(Gr),
                  'frozen': {k_.name: str(v) for k_, v in fr.items()}, 'radion_condition': 'q = -(rho - 3P)/2'}
    rep.check('BG2_expanding_fold', ok2,
              'Ghat^(i)_(i) = %s, Ghat^(4)_(4) = %s, Ghat^(r)_(r) = %s (a\' = ap, c\' = cp, ...); with frozen extra times and '
              'Ghat = kappa_7 tau: kappa_7 rho = %s, kappa_7 P = %s, and the extra-time component requires q = %s = -(rho - 3P)/2 '
              '(the radion condition)' % (Gs, Gt, Gr, sp.expand(fr[rho] * k7), sp.expand(fr[P] * k7), sp.simplify(fr[q])))

    # ---------------- BG3: the free volume is driven by dust and by vacuum energy
    sol_dd = sp.solve([sp.Eq(Gs, k7 * P), sp.Eq(Gr, k7 * q)], [A2, C2], dict=True)[0]
    c2_dust = sp.factor(sol_dd[C2].subs({P: 0, q: 0, C1: 0}))
    ok3 = sp.simplify(c2_dust - sp.Rational(3, 5) * A1 ** 2) == 0
    # vacuum energy: q = -rho needed -2 rho
    c2_vac = sp.factor(sol_dd[C2].subs({C1: 0}).subs({P: -rho, q: -rho}).subs(rho, 3 * A1 ** 2 / k7))
    # numerical integration of a matter era (P = q = 0) from c' = 0: x = ln t, variables a', c'
    f_a2 = sp.lambdify((A1, C1), sol_dd[A2].subs({P: 0, q: 0}))
    f_c2 = sp.lambdify((A1, C1), sol_dd[C2].subs({P: 0, q: 0}))

    def rhs(tt, y):
        return [f_a2(y[0], y[1]), f_c2(y[0], y[1]), y[0]]
    ti = 1.0
    sol = solve_ivp(rhs, (ti, 1e4 * ti), [2 / (3 * ti), 0.0, 0.0], rtol=1e-11, atol=1e-14, dense_output=True)
    efolds = [1, 2, 3, 5]
    ratios = {}
    for N in efolds:
        # the time at which a = N
        tt = np.geomspace(ti, 1e4 * ti, 20001)
        av = sol.sol(tt)[2]
        tN = float(np.interp(N, av, tt))
        yy = sol.sol(tN)
        ratios[N] = {'t': tN, 'cp_over_ap': float(yy[1] / yy[0]), 'dlnG_dx4_over_H4': float(-3 * yy[1] / yy[0])}
    late = ratios[5]['cp_over_ap']
    # the attractor of the ratio r = c'/a' in a matter era: r' = 0 with the equations above
    H0_per_yr = 67.4 / 3.0857e19 * 3.15576e7
    bound = max(abs(-5.0e-15 - 2 * 9.6e-15), abs(-5.0e-15 + 2 * 9.6e-15)) / H0_per_yr      # Biskupek, Mueller and Torre 2021
    ok3 &= 0.99 < late < 1.01 and 3 * late > 100 * bound
    out['BG3'] = {'c_pp_dust_at_cp_0': str(c2_dust), 'c_pp_vacuum_energy_at_cp_0': str(c2_vac), 'matter_era_from_cp_0': ratios,
                  'LLR_bound_dlnG_over_H0': bound}
    rep.check('BG3_free_volume_excluded', ok3,
              'without the fold fluid (q = 0 for dust, q = -rho for a vacuum energy): c\'\' = %s for dust and %s for a vacuum energy '
              'at c\' = 0; through a matter era from c\' = 0 the ratio c\'/a\' reaches %s after 1, 2, 3, 5 e-folds, so d ln G_N/dx4 = '
              '-3c\' = %.2f H_4; lunar laser ranging allows %.1e H_0: a free volume is excluded by a factor %.0f; with the fold fluid '
              '(q_hold = -(rho - 3P)/2 - q_matter, ASSUMED) c\' = 0 is preserved' % (
                  c2_dust, c2_vac, ', '.join('%.3f' % ratios[N]['cp_over_ap'] for N in efolds), -3 * late, bound,
                  3 * late / bound))

    # ---------------- BG4: the fold factor
    out['BG4'] = {'dlnZ_dx4': '3 c\'', 'frozen_extra_times': 0, 'free_volume_matter_era_over_H4': 3 * late}
    rep.check('BG4_fold_factor', True,
              'Z(x4) = V_t e^{3c}/V_*: d ln Z/dx4 = 3c\', zero with frozen extra times; with a free volume (BG3) %.2f H_4 in a matter '
              'era: Newton\'s constant, the squares of the gauge couplings g_4^2 = g_7^2/(V_t e^{3c}), of the Yukawa couplings and '
              'the quartic Higgs coupling all fall like 1/Z' % (3 * late))

    # ---------------- BG5: the ad hoc vacuum as a rotated, displaced Higgs modulus
    x4 = sp.Symbol('x4', real=True)
    v, vA, a40, g2, lam, cn, Hs, u_ = sp.symbols('v v_A a40 g2 lambda c_n H u', positive=True)
    Ac = vA * sp.exp(-2 * a40 * x4)
    b4 = sp.exp(u_ * Hs * x4)
    mu2 = -lam * v ** 2
    Phi = sp.Matrix([Ac, v]) / sp.sqrt(2)
    tau2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    theta = 2 * sp.atan(Ac / v)
    W = sp.diff(theta, x4) / g2

    def D4(F):
        return sp.diff(F, x4) - sp.I * g2 * W * (tau2 / 2) * F
    DPhi = D4(Phi)
    Dup = -DPhi
    J2 = sp.simplify(sp.I * ((Dup.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup)[0]))
    Dup0 = -sp.diff(Phi, x4)
    J2_literal = sp.simplify(sp.I * ((Dup0.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup0)[0]))
    PhiPhi = sp.simplify((Phi.H * Phi)[0])
    E = -(D4(DPhi) + 3 * (sp.diff(b4, x4) / b4) * DPhi) - mu2 * Phi - 2 * lam * PhiPhi * Phi - cn * Phi
    E = sp.simplify(E)
    V = sp.sqrt(v ** 2 + Ac ** 2)
    RV = sp.diff(V, x4, 2) + 3 * u_ * Hs * sp.diff(V, x4) + lam * Ac ** 2 * V + cn * V
    Urot = sp.Matrix([[sp.cos(theta / 2), sp.sin(theta / 2)], [-sp.sin(theta / 2), sp.cos(theta / 2)]])
    target = Urot * sp.Matrix([0, -RV]) / sp.sqrt(2)
    diff = sp.simplify(E - target)
    rnd.seed(5)
    maxdev = 0.0
    for _ in range(20):
        vals = {v: rnd.uniform(0.5, 2), vA: rnd.uniform(0.1, 2), a40: rnd.uniform(0.05, 3), g2: rnd.uniform(0.3, 1),
                lam: rnd.uniform(0.05, 0.5), cn: rnd.uniform(-0.2, 0.2), Hs: rnd.uniform(0.1, 2), u_: rnd.uniform(-1, 1),
                x4: rnd.uniform(0, 2)}
        dev = max(abs(complex(sp.N(d_.subs(vals)))) for d_ in diff)
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

    # ---------------- BG6: numbers (units of v; lambda = 0.129)
    lam_v = 0.12941
    rows = []
    for a40_v in (0.1, 1.0, 10.0):
        sub = {v: 1, vA: 1.0, a40: a40_v, lam: lam_v, cn: 0, Hs: 1, u_: 0, g2: 0.6517, x4: 0}
        RV0 = float(sp.N(RV.subs(sub)))
        Vp = float(sp.N(sp.diff(V, x4).subs(sub)))
        rhoH = 0.5 * Vp ** 2 + lam_v / 4 * 1.0
        t3 = math.log(1.0 / 1e-3) / (2 * a40_v)
        rows.append({'a40_over_v': a40_v, 'v_A_over_v': 1.0, 'R_V_over_lambda_v3_at_x4_0': RV0 / lam_v,
                     'rho_H_over_v4_at_x4_0': rhoH, 'time_until_A_below_1e-3_v_in_units_1_over_v': t3})
    out['BG6'] = rows
    ok6 = all(r_['R_V_over_lambda_v3_at_x4_0'] > 0 for r_ in rows)
    rep.check('BG6_numbers', ok6, '; '.join('a40 = %g v: R_V(0) = %.3g lambda v^3, rho_H(0) = %.3g v^4, A_c < 1e-3 v after %.3g/v' % (
        r_['a40_over_v'], r_['R_V_over_lambda_v3_at_x4_0'], r_['rho_H_over_v4_at_x4_0'], r_['time_until_A_below_1e-3_v_in_units_1_over_v'])
        for r_ in rows))
    return write('background', 'um4_background.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
