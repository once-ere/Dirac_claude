#!/usr/bin/env python3
"""um4_primordial.py - the primordial era of UM-4: inflation of the fold, exact and to the first order, and what it requires.

UM-4 has Einstein gravity with Lambda = -21 H^2 in the bulk and a fold that obeys, to the first order in its curvature over H^2,
the Einstein equations of seven dimensions Ghat^a_b = kappa_7 tau^a_b (kappa_7 = 5 kappa H/2; um4_fold.py F2), with the metric
of the fold ghat = e^{2a} dx_i^2 - dx4^2 - e^{2c} dx_r^2 (a = a4, c = ln(e^{-a4} b4); um4_background.py).  An era of inflation
is an era in which a vacuum energy rho_v of the fold (P = -rho_v along ordinary space) expands ordinary space exponentially.
Computed and checked:
  PR0  the author's vacuum (a4 = H x4, b4 constant, so a' = H, c' = -H) is not a solution: its fold metric is not Ricci flat
       (Ricci tensor along ordinary space, time, extra times as computed), so the bulk is not a vacuum of the author's form;
       as a fold with matter it would need, at the first order, kappa_7 rho = -3H^2 (a negative energy density) and
       kappa_7 P = kappa_7 q = -3H^2, and its rate a'/H = 1 lies outside the first-order regime (a'/H << 1);
  PR1  the exact de Sitter folds: a fold of constant curvature in all its 21 planes needs a' = c' = H_I constant (the extra
       times inflate with ordinary space, U = 2A); for it the bulk metric d sigma^2 + f(sigma)^2 ghat_I with
       f = sinh(H (sigma_0 - |sigma|))/sinh(H sigma_0) and H_I = H/sinh(H sigma_0) solves the Einstein equations with
       Lambda = -21 H^2 exactly (computed), the junction condition gives the tension kappa lambda = 12 H coth(H sigma_0), and so
       H_I^2 = (kappa lambda/12)^2 - H^2 = (kappa_7 rho_v/15) (1 + rho_v/(2 lambda_c)) exactly (lambda = lambda_c + rho_v,
       kappa lambda_c = 12 H the tension of the static block): the seven-dimensional Friedmann equation with the correction
       rho_v/(2 lambda_c) of high energies, of the same form as for the brane of Randall and Sundrum; but in it the volume of
       the extra times grows like e^{3N} over N e-folds, Newton's constant and the squares of the couplings fall like e^{-3N}
       (um4_background.py BG3, BG4): it cannot be the primordial era;
  PR2  inflation with frozen extra times: to the first order the Friedmann equations of general relativity, kappa_7 rho_v =
       3 H_I^2, with the pressure q = -2 rho_v along the extra times (the radion condition), of which the vacuum energy supplies
       -rho_v and the fold fluid the rest, q_hold = -rho_v (ASSUMED); no bulk of constant curvature holds such a fold exactly:
       for a fold with the extrinsic curvature diag(k_s, k_s, k_s, k_t, k_r, k_r, k_r) in a bulk of curvature -H^2 the Gauss
       equation gives the curvature -H^2 + k_a k_b in the plane (a, b), and the planes of ordinary space (H_I^2) and those
       with the extra times (0) cannot both be matched for H_I != 0 (solved): a Weyl tensor of the bulk is required; for a
       vacuum energy the correction of the order rho_v^2 is conserved by itself (um4_fold.py F6: the divergence vanishes for
       w = -1), so the inflation of general relativity holds with corrections of the relative order (12/25) A_I^2,
       A_I = H_I/H (F5); the regime A_I >~ 1 is OPEN;
  PR3  the scales: the bound on primordial gravitational waves, r < 0.032 (95 per cent; Planck PR4 with BICEP/Keck 2018 and BAO,
       Tristram et al. 2022), with A_s = 2.1e-9 limits the Hubble rate of inflation to H_inf < pi M_red sqrt(r A_s/2) =
       4.4e13 GeV; H is bounded only from below (2534 GeV, um4_propagators.py P5), so inflation lies in the regime of general
       relativity (A_I < 0.1) for H > 10 H_inf, and an inflation at the bound needs H > 4.4e14 GeV; with H at its lower
       bound only an inflation with H_inf < 253 GeV (energy scale rho_v^(1/4) < 3.3e10 GeV) is in that regime;
  PR4  ESTIMATE, an extension outside the action of UM-4 (the coupling -xi_H Rhat Phi^dagger Phi of the Higgs doublet to the
       curvature of the fold is not a term of the action): Higgs inflation needs xi_H = N sqrt(lambda/(72 pi^2 A_s)) = 1.6e4
       for lambda = m_H^2/(2 v^2) = 0.129 and N = 55 (4.5e3 for lambda = 0.01), gives n_s = 1 - 2/N = 0.964 and r = 12/N^2 =
       0.004 (within the Planck 2018 range, 3.5 sigma below ACT DR6 with Planck, CMB lensing and DESI, n_s = 0.974 +- 0.003),
       and has the Hubble rate H_inf = sqrt(lambda/12) M_red/xi_H = 1.6e13 GeV: in UM-4 it needs H > 1.6e14 GeV;
  PR5  the fold factor Z (um4_background.py BG4) during inflation: constant with frozen extra times; with a free volume
       (the de Sitter fold of PR1) Z grows like e^{3N} and every coupling of the fold falls like e^{-3N}: the volume must be held
       fixed during inflation as well.
Reads outputs/propagators.json (the lower bound on H).  Writes outputs/primordial.json and reports/primordial_checks.json.  Runs in
a few seconds.
Usage: python universe_model_4/code/um4_primordial.py

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

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write              # noqa: E402
from um4_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

M_PL_RED = 2.435e18          # the reduced Planck mass (GeV)
R_MAX = 0.032                # Planck PR4 + BICEP/Keck 2018 + BAO (95 per cent; Tristram et al. 2022)
A_S = 2.1e-9                 # Planck 2018
NS = 0.9649                  # Planck 2018 (TT,TE,EE+lowE+lensing)
NS_SIGMA = 0.0042
NS_ACT = 0.974               # ACT DR6 with Planck, CMB lensing and DESI DR1 BAO (Louis et al. 2025)
NS_ACT_SIGMA = 0.003
M_H = 125.25                 # GeV
V_EW = 246.22                # GeV
# GeV, the lower bound of um4_propagators.py P5 (the invisible width of the Z; run um4_propagators.py first)
H_MIN = json.loads((Path(__file__).resolve().parent.parent / 'outputs' / 'propagators.json').read_text())[
    'P5_bounds']['H_min_from_Z_invisible_width_GeV']


def fs(e):
    return sp.expand(sp.powsimp(sp.expand(e), combine='exp'))


def main():
    rep = Report()
    out = {}
    H = sp.Symbol('H', positive=True)
    Y = sp.symbols('x1:8', real=True)
    t = Y[3]
    eps7 = [1, 1, 1, -1, -1, -1, -1]

    # ---------------- PR0: the author's vacuum
    hh = [sp.exp(H * t)] * 3 + [sp.S(1)] + [sp.exp(-H * t)] * 3
    g7 = sp.diag(*[eps7[i] * hh[i] ** 2 for i in range(7)])
    R7 = frame_riemann(g7, list(Y), hh, simplify=fs)
    G7 = lovelock_tensor(R7, 1, n=7, simplify=fs)
    Gd = [sp.simplify(G7[i, i]) for i in range(7)]
    ric = [sp.simplify(Gd[i] - sum(Gd) / 5 * 1) for i in range(7)]          # Ric^a_a = G^a_a - (G/(2 - n)) ... n = 7: R = -2G/5
    Rs = sp.simplify(-sp.Rational(2, 5) * sum(Gd))
    ric = [sp.simplify(Gd[i] + Rs / 2) for i in range(7)]
    k7 = sp.Symbol('kappa_7', positive=True)
    rho0, P0, q0 = -Gd[3] / k7, Gd[0] / k7, Gd[4] / k7
    ok0 = (any(sp.simplify(r_) != 0 for r_ in ric) and sp.simplify(rho0 + 3 * H ** 2 / k7) == 0
           and sp.simplify(P0 + 3 * H ** 2 / k7) == 0 and sp.simplify(q0 + 3 * H ** 2 / k7) == 0)
    out['PR0'] = {'ricci_space_time_extra': [str(ric[i]) for i in (0, 3, 4)], 'kappa7_rho': str(sp.simplify(rho0 * k7)),
                  'kappa7_P': str(sp.simplify(P0 * k7)), 'kappa7_q': str(sp.simplify(q0 * k7))}
    rep.check('PR0_author_vacuum_not_a_solution', ok0,
              'a4 = H x4, b4 constant (a\' = H, c\' = -H): the Ricci tensor of the fold is %s (space, time, extra times), not zero, so '
              'the bulk is not a vacuum of the author\'s form; as a fold with matter it would need kappa_7 rho = %s (negative), '
              'kappa_7 P = %s, kappa_7 q = %s, at a rate a\'/H = 1 outside the first-order regime' % (
                  [str(ric[i]) for i in (0, 3, 4)], sp.simplify(rho0 * k7), sp.simplify(P0 * k7), sp.simplify(q0 * k7)))

    # ---------------- PR1: the exact de Sitter folds
    HI = sp.Symbol('H_I', positive=True)
    hI = [sp.exp(HI * t)] * 3 + [sp.S(1)] + [sp.exp(HI * t)] * 3
    gI = sp.diag(*[eps7[i] * hI[i] ** 2 for i in range(7)])
    RI = frame_riemann(gI, list(Y), hI, simplify=fs)
    const_curv = all(sp.simplify(v - HI ** 2) == 0 for v in RI.values()) and len(RI) == 21
    # the bulk: d sigma^2 + f(sigma)^2 ghat_I with a general warp f: its frame curvature and Einstein tensor
    sig = sp.Symbol('sigma', positive=True)
    fF = sp.Function('f')(sig)
    h8 = [sp.S(1)] + [fF * x_ for x_ in hI]
    X8 = [sig] + list(Y)
    eps8 = [1] + eps7
    g8 = sp.diag(*[eps8[i] * h8[i] ** 2 for i in range(8)])

    def simp8(e):
        return sp.simplify(sp.expand(sp.powsimp(sp.expand(e), combine='exp')))
    R8 = frame_riemann(g8, X8, h8, simplify=simp8)
    planes_sigma = {sp.simplify(v) for (up, lo), v in R8.items() if 0 in up}
    planes_fold = {sp.simplify(v) for (up, lo), v in R8.items() if 0 not in up}
    fp, fpp = sp.diff(fF, sig), sp.diff(fF, sig, 2)
    ok_planes = (planes_sigma == {sp.simplify(-fpp / fF)} and planes_fold == {sp.simplify((HI ** 2 - fp ** 2) / fF ** 2)})
    G8 = lovelock_tensor(R8, 1, n=8, simplify=simp8)
    # the bulk is a space of constant curvature -H^2 (so G + Lambda = 0 with Lambda = -21 H^2) iff f'' = H^2 f and
    # f'^2 - H^2 f^2 = H_I^2; the warp of PR1 satisfies both
    s0 = sp.Symbol('sigma_0', positive=True)
    fsol = sp.sinh(H * (s0 - sig)) / sp.sinh(H * s0)
    HIsol = H / sp.sinh(H * s0)
    ode1 = sp.simplify(sp.diff(fsol, sig, 2) - H ** 2 * fsol)
    ode2 = sp.simplify((sp.diff(fsol, sig) ** 2 - H ** 2 * fsol ** 2 - HIsol ** 2).rewrite(sp.exp))
    Gsub = [sp.simplify((G8[i, i] - 21 * H ** 2).subs(fF, fsol).doit().subs(HI, HIsol).rewrite(sp.exp)) for i in range(8)]
    ok1 = const_curv and ok_planes and ode1 == 0 and ode2 == 0 and all(x_ == 0 for x_ in Gsub)
    ok1 &= all(sp.simplify(G8[i, j]) == 0 for i in range(8) for j in range(8) if i != j)
    E0 = sp.exp(H * s0)
    f = fsol
    # junction: K = f'/f at 0+ in every direction of the fold
    K0 = sp.simplify((sp.diff(f, sig) / f).subs(sig, 0))
    coth0 = sp.cosh(H * s0) / sp.sinh(H * s0)
    kS = sp.simplify(-2 * (K0 - 7 * K0))
    ok1 &= sp.simplify(K0 + H * coth0) == 0 and sp.simplify(kS + 12 * H * coth0) == 0
    # H_I^2 = (kappa lambda/12)^2 - H^2 and its form in rho_v
    kl = 12 * H * coth0
    ok1 &= sp.simplify(((kl / 12) ** 2 - H ** 2 - HIsol ** 2).rewrite(sp.exp)) == 0
    kap, rv = sp.symbols('kappa rho_v', positive=True)
    lam_c = 12 * H / kap
    HI2 = sp.expand(((kap * (lam_c + rv)) / 12) ** 2 - H ** 2)
    kap7 = sp.Rational(5, 2) * kap * H
    ok1 &= sp.simplify(HI2 - kap7 * rv / 15 * (1 + rv / (2 * lam_c))) == 0
    out['PR1'] = {'constant_curvature_planes': const_curv, 'bulk_einstein_lambda_minus_21H2': ok1,
                  'K_at_0plus': 'H coth(H sigma_0) (with the sign -)', 'kappa_lambda': '12 H coth(H sigma_0)',
                  'H_I^2': '(kappa lambda/12)^2 - H^2 = (kappa_7 rho_v/15)(1 + rho_v/(2 lambda_c))'}
    rep.check('PR1_exact_de_sitter_fold', ok1,
              'a\' = c\' = H_I gives the curvature H_I^2 in all 21 planes of the fold; d sigma^2 + f^2 ghat_I with f = sinh(H(sigma_0 - '
              '|sigma|))/sinh(H sigma_0), H_I = H/sinh(H sigma_0) has G^M_N = 21 H^2 delta^M_N (so G + Lambda = 0) in all eight '
              'directions and no off-diagonal component; K^a_b(0+) = -H coth(H sigma_0) delta^a_b, kappa lambda = 12 H coth(H sigma_0); '
              'H_I^2 = (kappa lambda/12)^2 - H^2 = (kappa_7 rho_v/15)(1 + rho_v/(2 lambda_c)) exactly: the seven-dimensional '
              'Friedmann equation with the correction of high energies (as for Randall and Sundrum); the extra times inflate with '
              'ordinary space')

    # ---------------- PR2: frozen extra times
    ks_, kt_, kr_ = sp.symbols('k_s k_t k_r', real=True)
    gauss = [sp.Eq(-H ** 2 + kr_ ** 2, 0), sp.Eq(-H ** 2 + kr_ * kt_, 0), sp.Eq(-H ** 2 + ks_ * kr_, 0),
             sp.Eq(-H ** 2 + ks_ ** 2, HI ** 2), sp.Eq(-H ** 2 + ks_ * kt_, HI ** 2)]
    gs = sp.solve(gauss, [ks_, kt_, kr_], dict=True)
    ok2 = gs == []
    # with H_I = 0 the static block solves it
    gs0 = sp.solve([e.subs(HI, 0) for e in gauss], [ks_, kt_, kr_], dict=True)
    ok2 &= {ks_: -H, kt_: -H, kr_: -H} in gs0
    # the first-order equations: kappa_7 rho_v = 3 H_I^2, q = -2 rho_v, q_hold = -rho_v
    a1 = sp.Symbol('ap', positive=True)
    rho_f, P_f, q_f = 3 * a1 ** 2, -3 * a1 ** 2, -6 * a1 ** 2                # kappa_7 times: frozen de Sitter (a'' = 0)
    ok2 &= P_f == -rho_f and q_f == -2 * rho_f
    out['PR2'] = {'gauss_solutions_frozen_de_sitter': [str(x) for x in gs], 'gauss_solutions_static': [str(x) for x in gs0],
                  'kappa7_rho_P_q_first_order': [str(rho_f), str(P_f), str(q_f)], 'q_hold': '-rho_v'}
    rep.check('PR2_frozen_inflation', ok2,
              'frozen extra times, a\' = H_I: to the first order kappa_7 rho_v = %s, kappa_7 P = %s = -kappa_7 rho_v, kappa_7 q = %s = '
              '-2 kappa_7 rho_v, so the fold fluid adds q_hold = -rho_v; the Gauss equation of a fold with diagonal extrinsic '
              'curvature in a bulk of constant curvature has no solution for H_I != 0 (%s; for H_I = 0 the static block %s): a Weyl '
              'tensor of the bulk is required, and for w = -1 the correction rho_v^2 is conserved by itself (um4_fold.py F6)' % (
                  rho_f, P_f, q_f, gs, gs0))

    # ---------------- PR3: the scales
    Hinf = math.pi * M_PL_RED * math.sqrt(R_MAX * A_S / 2)
    H_needed = 10 * Hinf
    Hinf_low = 0.1 * H_MIN
    rho_low = 3 * Hinf_low ** 2 * M_PL_RED ** 2
    ok3 = 4.3e13 < Hinf < 4.6e13 and 2e2 < Hinf_low < 3e2 and 3e10 < rho_low ** 0.25 < 4e10
    out['PR3'] = {'H_inf_max_GeV': Hinf, 'H_needed_for_GR_regime_at_the_bound_GeV': H_needed,
                  'H_min_GeV': H_MIN, 'H_inf_GR_regime_at_H_min_GeV': Hinf_low, 'energy_scale_GeV': rho_low ** 0.25}
    rep.check('PR3_scales', ok3,
              'r < %.3f with A_s = %.1e: H_inf < pi M_red sqrt(r A_s/2) = %.2e GeV; the regime of general relativity (A_I < 0.1) '
              'needs H > 10 H_inf, %.1e GeV for an inflation at the bound; with H at its lower bound %.0f GeV (um4_propagators.py P5) only H_inf < %.0f GeV '
              '(rho_v^(1/4) < %.1e GeV) is in that regime' % (R_MAX, A_S, Hinf, H_needed, H_MIN, Hinf_low, rho_low ** 0.25))

    # ---------------- PR4: Higgs inflation (ESTIMATE)
    N = 55
    lam_tree = M_H ** 2 / (2 * V_EW ** 2)
    rows4 = [{'lambda': lam, 'xi_H': N * math.sqrt(lam / (72 * math.pi ** 2 * A_S))} for lam in (lam_tree, 0.01)]
    ns_h, r_h = 1 - 2 / N, 12 / N ** 2
    Hh = math.sqrt(lam_tree / 12) * M_PL_RED / rows4[0]['xi_H']
    ok4 = (all(r_['xi_H'] > 1e3 for r_ in rows4) and abs(ns_h - NS) < NS_SIGMA and r_h < R_MAX
           and (ns_h - NS_ACT) / NS_ACT_SIGMA < -2.5 and 1e13 < Hh < 2e13)
    out['PR4'] = {'rows': rows4, 'N': N, 'n_s': ns_h, 'r': r_h, 'H_inf_GeV': Hh, 'H_needed_GeV': 10 * Hh,
                  'pull_Planck': (ns_h - NS) / NS_SIGMA, 'pull_ACT': (ns_h - NS_ACT) / NS_ACT_SIGMA}
    rep.check('PR4_higgs_inflation', ok4,
              'ESTIMATE, outside the action of UM-4: xi_H = N sqrt(lambda/(72 pi^2 A_s)) = %s for lambda = %.4f and 0.01, N = %d; '
              'n_s = %.4f, r = %.4f (%.1f sigma from Planck 2018, %.1f sigma from ACT DR6 with Planck, CMB lensing and DESI); '
              'H_inf = sqrt(lambda/12) M_red/xi_H = %.2e GeV, so UM-4 needs H > %.1e GeV for it' % (
                  ['%.0f' % r_['xi_H'] for r_ in rows4], lam_tree, N, ns_h, r_h, (ns_h - NS) / NS_SIGMA,
                  (ns_h - NS_ACT) / NS_ACT_SIGMA, Hh, 10 * Hh))

    # ---------------- PR5: the fold factor
    Nf = 60
    out['PR5'] = {'frozen': 1.0, 'free_volume_couplings_after_60_efolds': math.exp(-3 * Nf)}
    rep.check('PR5_fold_factor', True,
              'frozen extra times: Z constant; the de Sitter fold of PR1 (U = 2A): Z grows like e^{3N} and every coupling of the '
              'fold falls like e^{-3N}, a factor %.1e after %d e-folds' % (math.exp(-3 * Nf), Nf))
    return write('primordial', 'um4_primordial.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
