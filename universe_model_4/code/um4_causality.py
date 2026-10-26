#!/usr/bin/env python3
"""um4_causality.py - does anything that crosses the bulk of UM-4 outrun light on the fold?  Signals between two points of
the fold through the bulk, on the static block (exactly) and on an expanding fold (to the first order in its rates).

A signal that leaves the fold, travels through the bulk at the local speed of light and returns to the fold arrives earlier
than light on the fold only if the light cone of some slice of the bulk is wider than that of the fold.  Computed:
  C1  the static block: in the conformal coordinate zeta = sgn(sigma) (e^{H|sigma|} - 1)/H the metric is
      (1 + H|zeta|)^{-2} (d zeta^2 + dx_i^2 - dx4^2 - dx_r^2), conformal to flat space of signature (4, 4), so the null geodesics
      are the straight null lines of flat space: at fixed extra times a signal between two points of the fold at the distance L
      along x3 needs the time sqrt(L^2 + (path along zeta)^2) >= L, equality only along the fold (checked for the null geodesic
      equations and for a sample of bulk paths; at fixed extra times this is the triangle inequality of the flat section): no
      signal that stays at fixed extra times crosses the static bulk faster than light on the fold (UM-3: the bulk light cone
      e^{H|sigma|} times wider); a null line that also moves by Y along an extra time needs only Delta x4 = sqrt(L^2 - Y^2),
      zero for Y = L, so in the full spacetime of signature (4, 4) no such bound holds: the statement is one about the fields
      that do not depend on the extra times (those that UM-4 keeps; a field with a momentum along them is one of the modes of
      um4_extratimes.py EX1);
  C2  an expanding fold with frozen extra times, with the bulk metric to the first order (um4_fold.py F1): with
      Rhat^(4)_(4) - Rhat^(1)_(1) = 2 a4'' computed from the metric of the fold, the coordinate speed of light along x3 at the
      depth sigma, relative to that on the fold, is 1 - a4'' (e^{2H|sigma|} - 1)/(5 H^2) to the first order: wider than on the
      fold wherever a4'' < 0; with the deceleration parameter q (a4'' = -(1 + q) H_4^2, H_4 = a4') that is wherever the Hubble
      rate falls (q > -1, today included: q_0 = -0.55), and narrower only if it grows (q < -1); the excess at small depth is
      (2/5)(1 + q) H_4^2 |sigma|/H;
  C3  the largest advance of a signal through the bulk where a4'' < 0 (the path that minimises the travel time between two
      points of the fold at the distance L, small depth): sigma(x) = (|a4''|/(5H)) x (L - x), the advance Delta t =
      a4''^2 L^3/(150 H^2), relative to L: (1 + q)^2 (H_4 L)^2 A^2/150 with A = H_4/H (checked by minimising the travel time
      numerically; where a4'' > 0 the minimum is the path along the fold, no advance); over the Hubble distance today (the
      small-distance formula extrapolated to L = 1/H_4^(0), q_0 = -0.55, H_4^(0) = 1.44e-42 GeV: an order of magnitude) this is
      4.4e-94 for H = 2534 GeV (the lower bound of um4_propagators.py P5; 4.5e-94 for H = 2.5 TeV) and below 3e-63 for
      H >= 1e-3 eV: a signal through the bulk is ahead of light on the fold, but by an unobservable amount, and on the static
      fold not at all;
  C4  closed time-like curves: the four time-like directions of the metric of UM-4 (the time and the three extra times) allow
      the circle (x4, x5) = (x4c + R cos t, x5c + R sin t) at fixed sigma, x1, x2, x3, x6, x7, whose squared tangent is
      -e^{-2H|sigma|} R^2 (sin^2 t + e^{-2 a4} b4^2 cos^2 t) < 0 for every t and any functions a4(x4), b4(x4) (sympy, and sampled):
      a closed time-like curve through every point, along which x4 rises and falls, so x4 is not a time function of the
      eight-dimensional spacetime; on a section of fixed extra times x4 is the only time-like direction, and there it is a time
      function (the fields of UM-4 do not depend on the extra times).
Reads outputs/propagators.json (the bound on H).  Writes outputs/causality.json and reports/causality_checks.json; exit code 0
iff every check passes.
Usage: python universe_model_4/code/um4_causality.py

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
functions, sinh, cosh, tanh = sinh/cosh and coth = cosh/sinh the hyperbolic functions, |y| the absolute value, max and
min the larger and the smaller of their arguments; det, tr and ^T are the determinant, the trace and the transpose of a
square matrix, and 1_4, 1_8 and 1_16 the identity matrices of 4, 8 and 16 rows; f(0+) and f(0-) are the limits of
f(sigma) as sigma approaches 0 from above and from below.

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
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the cosmological constant Lambda_RS (the vacuum energy Lambda_RS/kappa_5), and the bulk is otherwise empty.
     The fold of UM-4 is of the same kind, with every direction of the fold warped by the same factor as in the model of
     Randall and Sundrum: its static block is a space of constant curvature -H^2 in all eight directions, a vacuum of
     Einstein gravity with Lambda = -21 H^2, with a fold of pure tension (FD-12), and the graviton is bound to the fold as
     there. It differs in that the fold has seven dimensions, three of them extra times, in that the space is not cut at
     the brane (Randall and Sundrum identify the two sides of their brane, one physical side; the fold of UM-4 has two
     distinct sides, example 7), and in that the gauge fields live in the bulk as well.
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
     resonance of the energy omega_0 at rest and the width Gamma = (2/e) (q_b^2/m_Psi) e^(-2 F_t(upsilon_b) m_Psi/H) (to the
     leading order in H/q_b), with the tunnelling exponent F_t(upsilon) = ln((1 + sqrt(1 - upsilon^2))/upsilon)
     - sqrt(1 - upsilon^2) and upsilon_b = omega_b/m_Psi (the tunnelling through the region between the fold and sigma_t,
     where the profile decays at the local rate sqrt(m_Psi^2 - omega_r^2 e^(2 H |sigma|)), which falls to 0 at sigma_t). The
     profile is not a function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (for states at rest R_1 is the reflection across the fold combined with the reflection of ordinary space, R_2 the
     reflection across the fold combined with the reflection of the extra times). T_a (a = 0, ..., 7) are the author's real
     16 x 16 Dirac matrices T16^A[a] of 4+4.nb, built there from six real 4 x 4 matrices (rows separated by ";"):
        (FD-13) s_1 = [0 0 0 1; 0 0 1 0; 0 -1 0 0; -1 0 0 0],   s_2 = [0 0 -1 0; 0 0 0 1; 1 0 0 0; 0 -1 0 0],
                s_3 = [0 1 0 0; -1 0 0 0; 0 0 0 1; 0 0 -1 0],   t_1 = [0 0 0 -1; 0 0 1 0; 0 -1 0 0; 1 0 0 0],
                t_2 = [0 0 -1 0; 0 0 0 -1; 1 0 0 0; 0 1 0 0],   t_3 = [0 1 0 0; -1 0 0 0; 0 0 0 -1; 0 0 1 0],
                Xi_0 = 1_8,  Xi_1 = [[0, s_1], [s_1, 0]],  Xi_2 = [[0, s_2], [s_2, 0]],  Xi_3 = [[0, s_3], [s_3, 0]],
                Xi_4 = [[0, t_3], [-t_3, 0]],  Xi_5 = [[0, t_2], [-t_2, 0]],  Xi_6 = [[0, t_1], [-t_1, 0]],
                Xi_7 = Xi_1 Xi_2 Xi_3 Xi_4 Xi_5 Xi_6 = [[-1_4, 0], [0, 1_4]],
                Xibar_0 = 1_8,  Xibar_a = sigma_8 Xi_a^T sigma_8 (a = 1, ..., 7),  sigma_8 = [[0, 1_4], [1_4, 0]],
                T_a = [[0, Xibar_a], [Xi_a, 0]]  (a = 0, ..., 7)
     ([[A, B], [C, D]] the matrix made of the four blocks A, B, C, D, 0 a block of zeros; s_1, s_2, s_3 and t_1, t_2, t_3
     are s4by4[1..3] and t4by4[1..3], Xi_a and Xibar_a are tau[a] and taubar[a], sigma_8 is sigma88 of the notebook).
     They obey {T_a, T_b} = T_a T_b + T_b T_a = 2 eta_ab 1_16 with eta = diag(1, 1, 1, 1, -1, -1, -1, -1);
     gamma^(a) = eta^aa T_a (no sum) are the Dirac matrices of the frame, gamma^(0) along sigma; the chirality matrix is
     Gamma_8 = T_0 T_1 ... T_7 = [[-1_8, 0], [0, 1_8]], the chiral projectors are P_L = (1_16 - Gamma_8)/2 and
     P_R = (1_16 + Gamma_8)/2, and sigma_16 = T_0 T_1 T_2 T_3 = [[-sigma_8, 0], [0, sigma_8]] defines the Dirac adjoint
     Psibar = Psi^dagger sigma_16 (Psi^dagger the complex conjugate transpose).
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

import json
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write             # noqa: E402
from um4_lovelock import einstein_coordinate     # noqa: E402

H = sp.Symbol('H', positive=True)
SIG = sp.Symbol('sigma', positive=True)
zeta = sp.Symbol('zeta', positive=True)


def main():
    rep = Report()
    out = {}

    # ---------------- C1: the static block is conformally flat
    sig_of_zeta = sp.log(1 + H * zeta) / H
    W2 = sp.exp(-2 * H * sig_of_zeta)
    dsig_dzeta = sp.diff(sig_of_zeta, zeta)
    conf = sp.simplify(W2 - 1 / (1 + H * zeta) ** 2) == 0 and sp.simplify(dsig_dzeta ** 2 - 1 / (1 + H * zeta) ** 2) == 0
    # null geodesics of a conformally flat metric are the null straight lines: check the geodesic equation of
    # ds^2 = Omega^2 (dzeta^2 + dx3^2 - dx4^2) for the line zeta = v t, x3 = u t, x4 = t (u^2 + v^2 = 1), affinely
    # reparametrised: for a null curve the conformal factor changes only the affine parameter.
    t = sp.Symbol('t', positive=True)
    u_, v_ = sp.Rational(3, 5), sp.Rational(4, 5)
    Om2 = 1 / (1 + H * zeta) ** 2
    coords = [zeta, sp.Symbol('x3'), sp.Symbol('x4')]
    g = sp.diag(Om2, Om2, -Om2)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
                                for d in range(3)) / 2) for c in range(3)] for b in range(3)] for a in range(3)]
    lam = sp.Function('lam')(t)
    curve = [v_ * lam, u_ * lam, lam]
    # with the affine parameter s: d lam/ds = 1/Omega^2 (lam(s)); geodesic: x'' + Gamma x' x' = 0 in s
    # check: for x^a = c^a lam, the geodesic equation reduces to lam'' + (d ln Omega^2/d lam) lam'^2 = 0 (null case)
    sub = {zeta: v_ * lam}
    res = []
    for a in range(3):
        acc = sp.diff(curve[a], t, 2) + sum(Gam[a][b][c].subs(sub) * sp.diff(curve[b], t) * sp.diff(curve[c], t)
                                            for b in range(3) for c in range(3))
        res.append(sp.simplify(acc))
    # every component must be proportional to its c^a with the same factor (a reparametrisation of a straight line)
    fac = [sp.simplify(res[a] / [v_, u_, 1][a]) for a in range(3)]
    straight = sp.simplify(fac[0] - fac[2]) == 0 and sp.simplify(fac[1] - fac[2]) == 0
    # sample of bulk paths between two points of the fold at the distance L: flat-space travel time >= L
    rng = np.random.default_rng(1)
    L = 1.0
    worst = np.inf
    for _ in range(200):
        amp = rng.uniform(0, 0.5)
        xs = np.linspace(0, L, 401)
        zs = amp * np.sin(np.pi * xs / L) * rng.uniform(0.2, 1.0)
        tt = np.sum(np.sqrt(np.diff(xs) ** 2 + np.diff(zs) ** 2))
        worst = min(worst, tt - L)
    # the restriction to fixed extra times is essential: in the full conformally flat space of signature (4, 4) a null straight
    # line from a point of the fold may move along an extra time; the null condition of its displacement
    # (d zeta, d x3, d x4, d x5) = (0, L, D, Y) is L^2 = D^2 + Y^2, so it reaches x3 = L with D = sqrt(L^2 - Y^2) < L, and
    # with Y = L at D = 0: no bound Delta x4 >= L holds for signals that move along the extra times
    Dx4, Yx5 = sp.symbols('D Y', real=True)
    Ls = sp.Symbol('L', positive=True)
    gflat = sp.diag(1, 1, -1, -1)                        # (zeta, x3, x4, x5) at zeta = 0, conformal factor 1
    disp = sp.Matrix([0, Ls, Dx4, Yx5])
    null_cond = sp.expand((disp.T * gflat * disp)[0])
    roots = sp.solve(sp.Eq(null_cond, 0), Dx4)
    fwd = [r0 for r0 in roots if sp.simplify(r0.subs(Yx5, 0) - Ls) == 0]  # the future-directed root (D = L without Y)
    D_of_Y = sp.simplify(fwd[0]) if fwd else None
    extra_time_shortcut = D_of_Y is not None and sp.simplify(D_of_Y.subs(Yx5, Ls)) == 0
    ok1 = conf and straight and worst >= 0 and extra_time_shortcut
    out['C1_static'] = {'conformal_coordinate': 'zeta = (e^{H|sigma|} - 1)/H', 'metric': '(1 + H|zeta|)^-2 (dzeta^2 + dx^2 - dx4^2 - dx_r^2)',
                        'smallest_delay_of_sampled_bulk_paths_at_fixed_extra_times': float(worst),
                        'null_line_with_extra_time_displacement_Y': 'Delta x4 = %s' % D_of_Y}
    rep.check('C1_static_no_shortcut', ok1, 'the static block is conformally flat in zeta = (e^{H|sigma|} - 1)/H; the null geodesics are the '
              'null straight lines (geodesic equation checked); at fixed extra times a bulk path between two points of the fold takes '
              'the time sqrt(L^2 + ...) >= L (smallest delay of 200 sampled paths %.2e L, the triangle inequality of the flat section): '
              'nothing that stays at fixed extra times crosses the static bulk faster than light on the fold; a null line that also '
              'moves by Y along an extra time has Delta x4 = %s, down to 0 for Y = L: in the full spacetime of signature (4, 4) no such '
              'bound holds, and the bound is the statement for fields that do not depend on the extra times' % (worst, D_of_Y))

    # ---------------- C2: the light cone at the depth sigma of an expanding fold
    A2 = sp.Symbol('a4pp', real=True)          # a4''
    A1 = sp.Symbol('a4p', positive=True)       # a4'
    f = (sp.exp(2 * H * SIG) - 1) / (10 * H ** 2)
    # frozen extra times (b4 = c0 e^{a4}): the Ricci tensor of the metric of the fold FD-2, computed from its Christoffel
    # symbols; Rhat^(4)_(4) - Rhat^(1)_(1) enters the speed of light at the depth sigma through the bulk metric FE-34
    Y7 = sp.symbols('y1:8', real=True)
    a4f = sp.Function('a4')(Y7[3])
    c0 = sp.Symbol('c_0', positive=True)
    gfold = sp.diag(sp.exp(2 * a4f), sp.exp(2 * a4f), sp.exp(2 * a4f), -1, -c0 ** 2, -c0 ** 2, -c0 ** 2)
    Gf_, Rf_ = einstein_coordinate(gfold, list(Y7))
    Ric_mixed = [sp.simplify(Gf_[i_, i_] + Rf_ / 2) for i_ in range(7)]
    Rdiff_x = sp.simplify(Ric_mixed[3] - Ric_mixed[0])
    Rdiff = sp.simplify(Rdiff_x.subs(sp.Derivative(a4f, (Y7[3], 2)), A2).subs(sp.Derivative(a4f, Y7[3]), A1))
    ok_rd = sp.simplify(Rdiff - 2 * A2) == 0
    nu_minus_alpha = -f * Rdiff
    ratio2 = 1 + 2 * nu_minus_alpha               # (dx3/dx4)^2 at sigma over that on the fold, first order
    ratio = sp.series(sp.sqrt(ratio2), A2, 0, 2).removeO()
    target = 1 - A2 * (sp.exp(2 * H * SIG) - 1) / (5 * H ** 2)
    ok2 = sp.simplify(ratio - target) == 0 and ok_rd
    qq = sp.Symbol('q', real=True)
    small = sp.series(target.subs(A2, -(1 + qq) * A1 ** 2), SIG, 0, 2).removeO()
    ok2 &= sp.simplify(small - (1 + sp.Rational(2, 5) * (1 + qq) * A1 ** 2 * SIG / H)) == 0
    out['C2_light_cone_ratio'] = str(target)
    out['C2_small_depth'] = str(small)
    out['C2_Rhat44_minus_Rhat11'] = str(Rdiff)
    rep.check('C2_expanding_fold_light_cone', ok2, 'first order (F1 metric, frozen extra times): with Rhat^(4)_(4) - Rhat^(1)_(1) = %s computed '
              'from the metric of the fold, the coordinate speed of light along x3 at the depth sigma over that on the fold is %s; at '
              'small depth %s with a4\'\' = -(1 + q) H_4^2 (H_4 = a4\', q the deceleration parameter): the light cone of the bulk is wider '
              'than that of the fold wherever a4\'\' < 0, i.e. wherever the Hubble rate falls (q > -1, which includes today, q_0 = -0.55), '
              'and narrower only if it grows (q < -1)' % (Rdiff, target, small))

    # ---------------- C3: the largest advance
    Lsym, x = sp.symbols('L x', positive=True)
    beta = sp.Symbol('beta', positive=True)       # beta = 2 |a4''|/(5H): the speed excess per unit depth
    sig_x = beta / 2 * x * (Lsym - x)
    dT = sp.integrate(sp.diff(sig_x, x) ** 2 / 2 - beta * sig_x, (x, 0, Lsym))
    adv = sp.simplify(-dT)
    ok3 = sp.simplify(adv - beta ** 2 * Lsym ** 3 / 24) == 0
    a4pp = sp.Symbol('a4pp_abs', positive=True)
    adv_a = sp.simplify(adv.subs(beta, 2 * a4pp / (5 * H)))
    ok3 &= sp.simplify(adv_a - a4pp ** 2 * Lsym ** 3 / (150 * H ** 2)) == 0
    # numerical minimisation of the travel time T[sigma] = int dx (sqrt(1 + sigma'^2) / (1 + beta sigma)) for small beta
    bnum, Ln = 1e-3, 1.0
    N = 60
    xs = np.linspace(0, Ln, N + 1)
    def T(z):
        zz = np.concatenate([[0.0], z, [0.0]])
        dz = np.diff(zz)
        dx = np.diff(xs)
        mid = 0.5 * (zz[1:] + zz[:-1])
        return np.sum(np.sqrt(dx ** 2 + dz ** 2) / (1 + bnum * mid)) - Ln
    z0 = np.zeros(N - 1)
    r_ = minimize(T, z0, method='BFGS', options={'gtol': 1e-16, 'maxiter': 5000})
    adv_num = -r_.fun
    adv_pred = bnum ** 2 * Ln ** 3 / 24
    ok3 &= abs(adv_num / adv_pred - 1) < 0.02
    # where the bulk cone is narrower (a4'' > 0, beta < 0) no path beats the fold: the minimum of the travel time is the path
    # along the fold itself (advance 0)
    bneg = -1e-3
    def Tneg(z):
        zz = np.concatenate([[0.0], z, [0.0]])
        dz = np.diff(zz)
        dx = np.diff(xs)
        mid = 0.5 * (np.abs(zz[1:]) + np.abs(zz[:-1]))
        return np.sum(np.sqrt(dx ** 2 + dz ** 2) / (1 + bneg * mid)) - Ln
    r_neg = minimize(Tneg, 0.01 * np.sin(np.pi * xs[1:-1]), method='BFGS', options={'gtol': 1e-16, 'maxiter': 5000})
    ok3 &= r_neg.fun > -1e-12 and np.max(np.abs(r_neg.x)) < 1e-4
    # today, over the Hubble distance (the small-distance formula extrapolated to L = 1/H_4: an order of magnitude)
    H40 = 1.44e-42                     # GeV
    q0 = -0.55
    Hmin = 1e-12                       # GeV (1e-3 eV)
    Hbound = json.loads((HERE.parent / 'outputs' / 'propagators.json').read_text())['P5_bounds']['H_min_from_Z_invisible_width_GeV']
    rel_today = (1 + q0) ** 2 * (H40 / Hmin) ** 2 / 150
    rel_today_tev = (1 + q0) ** 2 * (H40 / 2.5e3) ** 2 / 150          # H = 2.5 TeV
    rel_today_bound = (1 + q0) ** 2 * (H40 / Hbound) ** 2 / 150       # H at the bound of um4_propagators.py P5
    ok3 &= rel_today < 1e-56 and 3e-94 < rel_today_tev < 6e-94 and 3e-94 < rel_today_bound < 6e-94
    out['C3_advance'] = {'formula': 'Delta t = a4\'\'^2 L^3/(150 H^2)', 'relative_over_Hubble_distance': '(1 + q)^2 (H_4/H)^2/150',
                         'numeric_beta_1e-3': {'advance': adv_num, 'prediction': adv_pred},
                         'today_for_H_1e-3_eV': rel_today, 'today_for_H_2.5_TeV': rel_today_tev,
                         'today_for_H_at_the_bound': rel_today_bound, 'H_bound_GeV': Hbound,
                         'narrower_cone_a4pp_positive': {'advance': -float(r_neg.fun), 'largest_depth': float(np.max(np.abs(r_neg.x)))}}
    rep.check('C3_largest_advance', ok3, 'where a4\'\' < 0 the optimal bulk path sigma = (|a4\'\'|/(5H)) x (L - x) gains Delta t = '
              'a4\'\'^2 L^3/(150 H^2) over light along the fold (numerical minimisation: %.4f of the formula); where a4\'\' > 0 the '
              'minimisation returns the path along the fold (advance %.1e); over the Hubble distance today (the formula extrapolated '
              'to L = 1/H_4, an order of magnitude) Delta t/L = %.1e for H = %.0f GeV, the bound of um4_propagators.py P5 (%.1e for '
              'H = 2.5 TeV, below %.0e for H >= 1e-3 eV): the bulk is ahead of light on the fold, but by an unobservable amount' % (
                  adv_num / adv_pred, -float(r_neg.fun), rel_today_bound, Hbound, rel_today_tev, rel_today))

    # ---------------- C4: closed time-like curves; x4 is a time function only on the sections of fixed extra times
    t_, R_ = sp.symbols('t R', positive=True)
    s0 = sp.Symbol('sigma_0', real=True)
    x4c, x5c = sp.symbols('x_4c x_5c', real=True)
    a4f, b4f = sp.Function('a4'), sp.Function('b4')
    x4t = x4c + R_ * sp.cos(t_)
    x5t = x5c + R_ * sp.sin(t_)
    w2 = sp.exp(-2 * H * sp.Abs(s0))
    # the metric of UM-4 in the proper chart (FE-27) along the circle in the plane of x4 and x5 at fixed sigma, x1..x3, x6, x7
    tang = w2 * (-sp.diff(x4t, t_) ** 2 - sp.exp(-2 * a4f(x4t)) * b4f(x4t) ** 2 * sp.diff(x5t, t_) ** 2)
    form = -w2 * R_ ** 2 * (sp.sin(t_) ** 2 + sp.exp(-2 * a4f(x4t)) * b4f(x4t) ** 2 * sp.cos(t_) ** 2)
    ok4 = sp.simplify(tang - form) == 0
    # numerically negative for sample functions a4, b4 and depths: the curve is time-like everywhere and closed
    tt = np.linspace(0, 2 * np.pi, 721)
    worst = -np.inf
    for sig0, a4n, b4n in ((0.0, lambda x: 0.3 * np.sin(x), lambda x: 1 + 0.2 * np.cos(x)), (2.0, lambda x: 0.1 * x, lambda x: 2.0 + 0 * x)):
        x4n = 0.5 + 1.0 * np.cos(tt)
        val = -np.exp(-2 * abs(sig0)) * (np.sin(tt) ** 2 + np.exp(-2 * a4n(x4n)) * b4n(x4n) ** 2 * np.cos(tt) ** 2)
        worst = max(worst, float(val.max()))
    ok4 &= worst < 0
    # along the circle x4 rises and falls (dx4/dt = -R sin t): x4 is not a time function of the eight-dimensional spacetime;
    # on a section of fixed x5, x6, x7 the metric d sigma^2 + e^{-2H|sigma|}(e^{2 a4} dx_i^2 - dx4^2) has x4 as its only time-like
    # direction, so a causal vector V != 0 there has V^4 != 0: x4 is a time function of the section
    V = sp.symbols('V_s V_1 V_2 V_3 V_4', real=True)
    a4s = sp.Symbol('a_4', real=True)
    gsec = sp.diag(1, sp.exp(2 * a4s) * w2, sp.exp(2 * a4s) * w2, sp.exp(2 * a4s) * w2, -w2)
    quad_ = sp.expand((sp.Matrix(V).T * gsec * sp.Matrix(V))[0])
    diag_only = sp.simplify(quad_ - sum(quad_.coeff(v_, 2) * v_ ** 2 for v_ in V)) == 0
    ok4 &= diag_only and all(quad_.coeff(v_, 2).is_positive for v_ in V[:4]) and quad_.coeff(V[4], 2).is_negative
    ok4 &= sp.diff(x4t, t_) == -R_ * sp.sin(t_)
    out['C4_closed_timelike_curves'] = {'curve': '(x4, x5) = (x4c + R cos t, x5c + R sin t) at fixed sigma, x1, x2, x3, x6, x7',
                                        'squared_tangent': str(form), 'largest_value_sampled': worst,
                                        'section_of_fixed_extra_times': 'x4 the only time-like direction: a time function'}
    rep.check('C4_closed_timelike_curves', ok4, 'the circle (x4, x5) = (x4c + R cos t, x5c + R sin t) at any depth has the squared tangent '
              '-e^{-2H|sigma|} R^2 (sin^2 t + e^{-2 a4} b4^2 cos^2 t) < 0 for every t and every a4(x4), b4(x4) (largest sampled value '
              '%.2e): a closed time-like curve through every point (four time-like directions), along which x4 rises and falls; on a '
              'section of fixed extra times x4 is the only time-like direction, so x4 is a time function there and only there' % worst)
    return write('causality', 'um4_causality.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
