#!/usr/bin/env python3
"""um4_fold.py - the fold of UM-4: its thin source, the bulk metric of an expanding fold and the equations that the fold
obeys (Einstein gravity in the bulk, Lambda = -21 H^2, um4_gravity.py L4).

The author's form of the metric, d sigma^2 + e^{-2H|sigma|} ghat, solves the bulk equations only when the metric ghat of the
fold is Ricci flat (um4_geometry.py G5).  An expanding fold with matter has a bulk metric of the form
    ds^2 = d sigma^2 + e^{-2H|sigma|} gamma_ab(sigma, x) dx^a dx^b,   gamma_ab(0, x) = ghat_ab(x),
expanded in the number of derivatives along the fold (each derivative counts once, the curvature of the fold twice; the
expansion parameter is the curvature of the fold divided by H^2, A^2 = (a4'/H)^2 for a homogeneous fold).  Computed
(sympy), on the side sigma > 0 (the other side is its mirror image):
  F1  the bulk metric to the first order: gamma_ab = ghat_ab - ((e^{2H|sigma|} - 1)/(5 H^2)) (Rhat_ab - Rhat ghat_ab/12)
      (Rhat_ab, Rhat the Ricci tensor and the scalar curvature of ghat) solves every component of the bulk equations to
      the second order in the derivatives for every a4(x4), b4(x4) (the diagonal components, frame (0)(0), (i)(i), (4)(4),
      (r)(r)), and the mixed component (0)(4) to the third order; no other solution regular at the fold up to the
      homogeneous solutions e^{7H|sigma|} c_ab(x), traceless and conserved (a bulk Weyl tensor; UM-4 takes c_ab = 0, no
      dark radiation, ASSUMED);
  F2  the junction condition (Israel, Z2 mirror symmetry: kappa S^a_b = -2 (K^a_b - K delta^a_b) at 0+, K^a_b the extrinsic
      curvature) with this metric: kappa S^a_b = -12 H delta^a_b + (2/(5H)) Ghat^a_b + (fourth order): with S^a_b =
      -lambda_F delta^a_b + tau^a_b (the tension kappa lambda_F = 12 H and the matter tau of the fold) the fold obeys the
      Einstein equations of seven dimensions, Ghat^a_b = kappa_7 tau^a_b with kappa_7 = (5/2) kappa H and no cosmological
      constant of the fold;
  F3  the exact equations of the fold (Shiromizu, Maeda and Sasaki 2000, in eight dimensions): Gauss's equation with
      Israel's condition gives, for every fold in a bulk of constant curvature -H^2 (the Weyl tensor of the bulk zero; with a
      Weyl tensor its projection E_ab is added), Ghat_ab = kappa_7 tau_ab + kappa^2 pi_ab, pi_ab = -(1/4) tau_ac tau^c_b
      + (1/24) tau tau_ab + (1/8) ghat_ab tau_cd tau^cd - (1/48) ghat_ab tau^2 (verified as an algebraic identity for a
      diagonal tau with independent entries);
  F4  the fold with frozen extra times (e^{-a4} b4 constant): the seven-dimensional equations are the Friedmann equations
      of four-dimensional general relativity, 3 a4'^2 = kappa_7 rho_7 and -(2 a4'' + 3 a4'^2) = kappa_7 P_7, and the
      extra-time component requires the pressure q_7 = -(rho_7 - 3 P_7)/2 along the extra times (the radion condition:
      the matter of the fold must supply it, or the fold fluid adds it, q_hold); with the volume V_* of the extra times
      (four-dimensional densities rho = V_* rho_7): 8 pi G_N = kappa_7/V_*;
  F5  the size of the corrections: kappa^2 pi relative to kappa_7 tau is of the order kappa^2 rho_7^2/(kappa_7 rho_7) =
      (24/5) rho/(lambda_F V_*); in four-dimensional normalisation lambda_F V_* = 30 H^2 M_red^2 (M_red the reduced Planck mass,
      1/(8 pi G_N) = M_red^2), so the scale of the corrections is 4 rho/(25 H^2 M_red^2) = (12/25) A^2 (A = a4'/H) relative to
      the Friedmann equations of general relativity; the correction of the energy equation itself, kappa^2 pi^4_4/(kappa_7
      tau^4_4) with the radion pressure, is A^2/25 for radiation and 11 A^2/400 for dust;
  F6  the Weyl term is required at the second order with frozen extra times: for a perfect fluid with P = w rho and the
      radion condition q = -(1 - 3w) rho/2, the time component of the divergence of pi is a4' rho^2 times
      -3 (w - 1)(w + 1)(3w - 1)/32, zero only for vacuum energy (w = -1), radiation (w = 1/3) and stiff matter (w = 1): for
      dust the projected Weyl tensor E_ab of the bulk cannot vanish at the order rho^2/lambda_F (its value depends on the
      bulk solution: OPEN).
Writes outputs/fold.json and reports/fold_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_fold.py

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

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write                     # noqa: E402
from um4_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

H = sp.Symbol('H', positive=True)
SIG = sp.Symbol('sigma', positive=True)
x1, x2, x3, x4, x5, x6, x7 = sp.symbols('x1:8', real=True)
X = [SIG, x1, x2, x3, x4, x5, x6, x7]
EPS = [1, 1, 1, 1, -1, -1, -1, -1]
a4 = sp.Function('a4')(x4)
lb = sp.Function('lb')(x4)                       # ln b4
eps = sp.Symbol('epsilon')
d = sp.Symbol('delta', positive=True)


def fs(e):
    return sp.expand(sp.powsimp(sp.expand(e), combine='exp'))


def fold_curvature():
    """The Ricci tensor (mixed, frame) and the scalar curvature of the fold metric ghat, with its Einstein tensor."""
    Y = [x1, x2, x3, x4, x5, x6, x7]
    eps7 = [1, 1, 1, -1, -1, -1, -1]
    hh = [sp.exp(a4)] * 3 + [sp.S(1)] + [sp.exp(lb - a4)] * 3
    gg = sp.diag(*[eps7[i] * hh[i] ** 2 for i in range(7)])
    R7 = frame_riemann(gg, Y, hh, simplify=fs)
    G7 = lovelock_tensor(R7, 1, n=7, simplify=fs)
    Rs = sp.simplify(-sp.Rational(2, 5) * sum(G7[i, i] for i in range(7)))
    Ric = [sp.simplify(G7[i, i] + Rs / 2) for i in range(7)]
    return [sp.simplify(G7[i, i]) for i in range(7)], Ric, Rs


def bulk_linear():
    """G^a_b - 21 H^2 delta^a_b for the bulk metric with the exponents -H sigma + (fold) + eps * (alpha, nu, beta), to the
    first order in eps (alpha, nu, beta general functions of sigma and x4)."""
    al = sp.Function('al')(SIG, x4)
    nu = sp.Function('nu')(SIG, x4)
    be = sp.Function('be')(SIG, x4)
    FA = -H * SIG + a4 + eps * al
    FN = -H * SIG + eps * nu
    FB = -H * SIG - a4 + lb + eps * be
    h = [sp.S(1)] + [sp.exp(FA)] * 3 + [sp.exp(FN)] + [sp.exp(FB)] * 3
    g = sp.diag(*[EPS[i] * h[i] ** 2 for i in range(8)])
    Rf = frame_riemann(g, X, h, simplify=fs)
    G = lovelock_tensor(Rf, 1, simplify=fs)
    res = {}
    for (i, j) in [(0, 0), (1, 1), (4, 4), (5, 5), (0, 4)]:
        ex = G[i, j] - (21 * H ** 2 if i == j else 0)
        res[(i, j)] = (sp.expand(ex.subs(eps, 0)), sp.expand(sp.diff(ex, eps).subs(eps, 0)))
    return res, (al, nu, be)


def main():
    rep = Report()
    out = {}
    G7, Ric, Rs = fold_curvature()

    # ---------------- F1: the bulk metric to the first order
    res, (al, nu, be) = bulk_linear()
    f = (sp.exp(2 * H * SIG) - 1) / (10 * H ** 2)
    sol = {al: -f * (Ric[0] - Rs / 12), nu: -f * (Ric[3] - Rs / 12), be: -f * (Ric[4] - Rs / 12)}
    # derivative counting: every x4-derivative of a fold function carries one power of delta (alpha, nu, beta are then of
    # the second order); the terms of e1 with a time derivative of alpha, nu, beta or with a product are of higher order
    def counted(expr):
        e = expr
        for k in (5, 4, 3, 2, 1):
            e = e.subs(sp.Derivative(a4, (x4, k)), d ** k * sp.Symbol('a_%d' % k))
            e = e.subs(sp.Derivative(lb, (x4, k)), d ** k * sp.Symbol('l_%d' % k))
        return sp.expand(e)
    ok1 = True
    orders = {}
    for key, (e0, e1) in res.items():
        tot = e0 + e1.subs({k: v for k, v in sol.items()}).doit()
        tot = counted(tot)
        need = 3 if key == (0, 4) else 2
        low = [sp.simplify(tot.coeff(d, k)) for k in range(need + 1)]
        orders['%d%d' % key] = [str(v) for v in low]
        ok1 &= all(v == 0 for v in low)
    out['F1_bulk_metric_first_order'] = 'gamma_ab = ghat_ab - ((e^{2H|sigma|} - 1)/(5 H^2)) (Rhat_ab - Rhat ghat_ab/12)'
    out['F1_residual_orders'] = orders
    rep.check('F1_bulk_metric_first_order', ok1, 'gamma_ab = ghat_ab - ((e^{2H|sigma|} - 1)/(5H^2))(Rhat_ab - Rhat ghat_ab/12) solves '
              'the components (0)(0), (i)(i), (4)(4), (r)(r) of the bulk equations to the second order and (0)(4) to the third '
              'order in the derivatives along the fold, for every a4(x4), b4(x4)')

    # ---------------- F2: the junction condition
    FA = -H * SIG + a4 + sol[al]
    FN = -H * SIG + sol[nu]
    FB = -H * SIG - a4 + lb + sol[be]
    K = [sp.diff(F_, SIG).subs(SIG, 0) for F_ in (FA, FN, FB)]
    Ktr = 3 * K[0] + K[1] + 3 * K[2]
    kS = [sp.simplify(-2 * (k - Ktr)) for k in K]
    target = [sp.simplify(-12 * H + 2 * G7[i] / (5 * H)) for i in (0, 3, 4)]
    ok2 = all(sp.simplify(kS[n] - target[n]) == 0 for n in range(3))
    out['F2_kappa_S'] = {'space': str(kS[0]), 'time': str(kS[1]), 'extra_times': str(kS[2])}
    out['F2_kappa_7'] = '(5/2) kappa H'
    rep.check('F2_fold_obeys_einstein_7d', ok2, 'kappa S^a_b = -2(K^a_b - K delta^a_b)(0+) = -12 H delta^a_b + (2/(5H)) Ghat^a_b for '
              'the space, time and extra-time components: the fold obeys Ghat^a_b = kappa_7 tau^a_b with kappa_7 = 5 kappa H/2 and '
              'the tension kappa lambda_F = 12 H (no cosmological constant of the fold)')

    # ---------------- F3: the exact equations of the fold (algebraic identity)
    n = 7
    tau = sp.symbols('t0:7', real=True)                          # a diagonal tau^a_b with independent entries
    kap = sp.Symbol('kappa', positive=True)
    T = sp.diag(*tau)
    trT = sum(tau)
    Kmat = -H * sp.eye(n) - kap / 2 * (T - trT / 6 * sp.eye(n))     # Israel with the tension kappa lambda_F = 12 H
    trK = Kmat.trace()
    # Gauss: Rhat^{ab}_{cd} = (-H^2 delta^{ab}_{cd}) + K^a_c K^b_d - K^a_d K^b_c (bulk of constant curvature); its Einstein
    # tensor: Ghat^a_a = -sum over the planes (b, c) not containing a of Rhat^{bc}_{bc}
    sec = {}
    for b in range(n):
        for c in range(b + 1, n):
            sec[(b, c)] = -H ** 2 + Kmat[b, b] * Kmat[c, c]
    Ghat = [sp.expand(-sum(v for (b, c), v in sec.items() if a not in (b, c))) for a in range(n)]
    kap7 = sp.Rational(5, 2) * kap * H
    TT = sum(t_ ** 2 for t_ in tau)
    pi = [-(tau[a] ** 2) / 4 + trT * tau[a] / 24 + TT / 8 - trT ** 2 / 48 for a in range(n)]
    ok3 = all(sp.expand(Ghat[a] - kap7 * tau[a] - kap ** 2 * pi[a]) == 0 for a in range(n))
    out['F3_pi'] = '-(1/4) tau_ac tau^c_b + (1/24) tau tau_ab + (1/8) g tau_cd tau^cd - (1/48) g tau^2'
    rep.check('F3_exact_fold_equations', ok3, 'for a fold in a bulk of constant curvature -H^2 with Israel\'s condition: Ghat_ab = '
              'kappa_7 tau_ab + kappa^2 pi_ab exactly, kappa_7 = 5 kappa H/2, pi_ab = -(1/4) tau_ac tau^c_b + (1/24) tau tau_ab + '
              '(1/8) g tau_cd tau^cd - (1/48) g tau^2 (eight dimensions; a Weyl tensor of the bulk adds -E_ab)')

    # ---------------- F4: frozen extra times
    c0 = sp.Symbol('c0', positive=True)
    frz = {lb: a4 + sp.log(c0)}
    Gf = [sp.simplify(G7[i].subs(frz).doit()) for i in range(7)]
    A1, A2 = sp.diff(a4, x4), sp.diff(a4, x4, 2)
    ok4 = (sp.simplify(Gf[3] + 3 * A1 ** 2) == 0 and sp.simplify(Gf[0] + 2 * A2 + 3 * A1 ** 2) == 0
           and sp.simplify(Gf[4] + 3 * A2 + 6 * A1 ** 2) == 0)
    # the radion condition: kappa_7 q_7 = Gf[4] with kappa_7 rho_7 = -Gf[3], kappa_7 P_7 = Gf[0]
    rho7 = -Gf[3]
    P7 = Gf[0]
    q7 = Gf[4]
    ok4 &= sp.simplify(q7 + (rho7 - 3 * P7) / 2) == 0
    out['F4_frozen'] = {'kappa7_rho7': str(rho7), 'kappa7_P7': str(P7), 'kappa7_q7': str(q7),
                        'radion_condition': 'q_7 = -(rho_7 - 3 P_7)/2', 'newton': '8 pi G_N = kappa_7/V_*'}
    rep.check('F4_friedmann_frozen_extra_times', ok4, 'with e^{-a4} b4 constant: Ghat^(4)_(4) = -3 a4\'^2, Ghat^(i)_(i) = -(2 a4\'\' + 3 a4\'^2), '
              'Ghat^(r)_(r) = -3(a4\'\' + 2 a4\'^2): the Friedmann equations 3 a4\'^2 = kappa_7 rho_7, -(2 a4\'\' + 3 a4\'^2) = kappa_7 P_7 '
              'and the radion condition q_7 = -(rho_7 - 3 P_7)/2')

    # ---------------- F5: the size of the corrections
    Mred, Vs = sp.symbols('M_red V_star', positive=True)
    kappa_from_GN = 2 * Vs / (5 * H * Mred ** 2)                 # 8 pi G_N = 1/M_red^2 = kappa_7/V_* = 5 kappa H/(2 V_*)
    lamF4 = sp.simplify(12 * H / kappa_from_GN * Vs)            # lambda_F V_* (four-dimensional normalisation)
    rho = sp.Symbol('rho', positive=True)                      # four-dimensional density, rho_7 = rho/V_*
    ratio = sp.simplify((kap ** 2 * (rho / Vs) ** 2 / (kap7 * rho / Vs)).subs(kap, kappa_from_GN))   # kappa^2 rho_7^2/(kappa_7 rho_7)
    Afr = sp.Symbol('A', positive=True)
    ratio_A = sp.simplify(ratio.subs(rho, 3 * Mred ** 2 * (Afr * H) ** 2))                         # rho = 3 M_red^2 a4'^2
    ok5 = (sp.simplify(lamF4 - 30 * H ** 2 * Mred ** 2) == 0 and sp.simplify(ratio - sp.Rational(24, 5) * rho / lamF4) == 0
           and sp.simplify(ratio_A - sp.Rational(12, 25) * Afr ** 2) == 0)
    # the actual relative correction of the energy equation: kappa^2 pi^4_4/(kappa_7 tau^4_4) = (-pi^4_4/rho_7^2) (12/25) A^2
    # for a fluid P = w rho with the radion pressure q = -(rho - 3P)/2 (FE-35 and FE-72)
    wv = sp.Symbol('w', real=True)
    r5 = sp.Symbol('rho', positive=True)
    P5_, q5_ = wv * r5, -(r5 - 3 * wv * r5) / 2
    taus5 = [P5_, P5_, P5_, -r5, q5_, q5_, q5_]
    tr5, TT5 = sum(taus5), sum(x_ ** 2 for x_ in taus5)
    pi44 = sp.simplify(-(taus5[3] ** 2) / 4 + tr5 * taus5[3] / 24 + TT5 / 8 - tr5 ** 2 / 48)
    corr = {name_: sp.nsimplify(sp.simplify(-pi44.subs(wv, wv_) / r5 ** 2) * sp.Rational(12, 25))
            for name_, wv_ in (('radiation', sp.Rational(1, 3)), ('dust', 0))}
    ok5 &= corr['radiation'] == sp.Rational(1, 25) and corr['dust'] == sp.Rational(11, 400)
    out['F5_lambdaF_4d'] = str(lamF4)
    out['F5_relative_correction'] = str(ratio)
    out['F5_relative_correction_in_A'] = str(ratio_A)
    out['F5_energy_equation_correction_over_A2'] = {k_: str(v_) for k_, v_ in corr.items()}
    rep.check('F5_size_of_corrections', ok5, 'lambda_F V_* = %s; kappa^2 rho_7^2/(kappa_7 rho_7) = (24/5) rho/(lambda_F V_*) = %s = %s '
              'with rho = 3 M_red^2 a4\'^2 (A = a4\'/H), the scale of the corrections; the correction of the energy equation itself, '
              'kappa^2 pi^4_4/(kappa_7 tau^4_4) with the radion pressure, is %s A^2 for radiation and %s A^2 for dust: the Friedmann '
              'equations of the fold are those of general relativity up to corrections of relative order A^2' % (
                  lamF4, ratio, ratio_A, corr['radiation'], corr['dust']))

    # ---------------- F6: the Weyl term at the second order with frozen extra times
    w = sp.Symbol('w', real=True)
    rr = sp.Symbol('rho', positive=True)
    P = w * rr
    q = -(rr - 3 * P) / 2
    taus = [P, P, P, -rr, q, q, q]                               # tau^a_b: space, time, extra times
    trt = sum(taus)
    TT2 = sum(t_ ** 2 for t_ in taus)
    pis = [-(t_ ** 2) / 4 + trt * t_ / 24 + TT2 / 8 - trt ** 2 / 48 for t_ in taus]
    # divergence along the time of a diagonal tensor on the frozen fold: d_t T^t_t + 3 (a'/a)(T^t_t - T^s_s);
    # with rho' = -3 (a'/a)(1 + w) rho:  (a'/a) [ -6 (1 + w) c_t + 3 (c_t - c_s) ] rho^2 for T = c rho^2
    ct = sp.simplify(pis[3] / rr ** 2)
    cs = sp.simplify(pis[0] / rr ** 2)
    div = sp.factor(sp.simplify(-6 * (1 + w) * ct + 3 * (ct - cs)))
    zeros = sp.solve(div, w)
    ok6 = sp.Rational(1, 3) in zeros and div != 0
    out['F6_divergence_of_pi_over_Hubble_rho2'] = str(div)
    out['F6_zero_for_w'] = [str(z_) for z_ in zeros]
    rep.check('F6_weyl_term_required', ok6, 'frozen extra times, P = w rho, q = -(1 - 3w) rho/2: the time component of the divergence '
              'of pi is (a4\') rho^2 times %s, zero only for w = %s (vacuum energy, radiation, stiff matter): otherwise the projected Weyl tensor '
              'E_ab of the bulk must be non-zero at the order rho^2/lambda_F for dust (its value needs the bulk solution: OPEN)' % (div, zeros))
    return write('fold', 'um4_fold.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
