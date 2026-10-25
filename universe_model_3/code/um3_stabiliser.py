#!/usr/bin/env python3
"""um3_stabiliser.py - the stabiliser of the bulk: the source that a static bulk of the author's metric requires with the
author's original Lovelock weights, checked in every respect that the document STABILISER states, and its removal by
the corrected weights.

The author's metric in the proper chart of the hidden direction (sigma the signed proper distance from the fold):
    ds^2 = d sigma^2 + e^{2 fa} (dx1^2 + dx2^2 + dx3^2) - e^{2 fn} dx4^2 - e^{2 fb} (dx5^2 + dx6^2 + dx7^2),
    fa = a4(x4) - H|sigma|,  fb = ln b4(x4) - a4(x4) - H|sigma|,  fn = 0,
and the field equations of the bulk (sigma != 0), Einstein-Lovelock gravity,
    sum_{p=1}^{3} alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b          (frame components, kappa = 8 pi G_8),
alpha_(p) = w_(p) H^{2-2p}, E_(p) the Lovelock tensor of order p.  ST1 to ST8 use the author's original weights
w_(1) = 1, w_(2) = 1/32, w_(3) = 1/1152 and Lambda = -10 H^2: they are the record of the stabiliser as it was found on
2026-10-24.  ST9 uses the corrected weights w_(2) = 1/20, w_(3) = 1/360 and Lambda = -7 H^2 (the author's order of
2026-10-25 07:55: gravitons must travel at the speed of light; these weights are the only ones for which they do, and
then Lambda = -7 H^2 makes the static bulk a vacuum): with them the stabiliser is zero.  With A = a4'/H and U = b4'/(b4 H)
(constant rates, a4'' = b4'' = 0 except where stated) the left-hand side is a polynomial in A and U.
Checks:
  ST1  the static bulk (A = U = 0, a4 and b4 constant): the left-hand side is H^2 diag(-5/16, -5/16, -5/16, -5/16, 1/16,
       -5/16, -5/16, -5/16) in the order (sigma, x1, x2, x3, x4, x5, x6, x7), on both sides of the fold, with no energy
       flux: the static bulk is a solution only with the source kappa T = that, a medium at rest with kappa rho_s = -H^2/16
       and kappa p_s = -5 H^2/16 = 5 kappa rho_s: the stabiliser.  Why: the static block is a space of constant curvature
       -H^2 in the seven directions other than the time (frame curvature R^{ab}_{ab} = -H^2 for each of their 21 pairs)
       times the flat time line, so E_(p) = -(K^p/2) m!/(m - 2p)! with K = -H^2 and m = 6 other curved directions along
       sigma, ordinary space and the extra times, m = 7 along the time; order by order (warped, time)/H^2: Einstein
       (15, 21), Gauss-Bonnet (-45/8, -105/8), cubic (5/16, 35/16), Lambda (-10, -10), sum (-5/16, 1/16).  The source of
       the fold that the static block needs, the jump of the junction potentials (the field equations are linear in the
       second sigma-derivatives, the delta functions of the kink): (x1, x4, x5)/H = Einstein (-10, -12, -10), equal to
       Israel's -([K^a_b] - delta^a_b [K]), Gauss-Bonnet (5/2, 5, 5/2), cubic (-1/8, -3/4, -1/8), total (-61/8, -31/4, -61/8);
  ST2  the author's vacuum (A = 1, U = 0): the left-hand side vanishes, the primordial bulk needs no stabiliser; its fold
       source is kappa S = (-10, -6, -10) H; near it kappa rho_bulk = -(H^2/16) P with P = 12 ((A - 1 - U)^2 + (A - 1)^2)
       to second order; G(1, U) = 2U(3U - 2);
  ST3  without any bulk source: with constant rates the bulk equations hold only at (A, U) = (+-1, 0); for any a4(x4),
       b4(x4) the two constraints of ST8 hold at every instant, P = 0 and U G = 0: U = 0 needs A = +-1
       (P(A, 0) = (A^2 - 1)^2 (5A^2 + 1)), and U != 0 would need a common root of P and G, but their resultant in A,
       6400 U^4 (20U^4 - 15U^2 + 12)^2, has no real root but U = 0: a bulk without any source is at every instant the
       author's vacuum or its time reverse;
  ST4  the stabiliser is conserved by itself on the static bulk: the covariant divergence nabla_M T^M_N of the constant
       tensor diag(p_s, p_s, p_s, p_s, -rho_s, p_s, p_s, p_s) vanishes for every N; for any static medium the sigma
       component is p_sigma' - 6H (p_sigma - p_w) (sigma > 0), free of the energy density: no gravitational pull along
       sigma, because the time is not warped;
  ST5  energy conditions and models, from the values of ST1: rho_s < 0 (the weak energy condition fails), and along the
       null vector n = e(4) + e(1) T_ab n^a n^b = rho_s + p_s = 6 rho_s < 0 (the null energy condition fails); for a
       scalar field with the action -(eps/2)(d phi)^2 - V the variation with respect to the metric gives, for phi(x4),
       rho = K + V and the pressure K - V in every other direction (K = eps phidot^2/2), and for phi(sigma) the pressure
       -rho in every direction but sigma: p = 5 rho with rho < 0 needs phi(x4) with K = 3 rho_s < 0, V = -2 rho_s (a
       ghost, eps = -1); on the static block it has no friction and rolls at a constant speed on a flat potential;
  ST6  history: a medium that couples only to gravity obeys nabla_M T^M_4 = 0; for a homogeneous medium with the pressure p
       in every warped direction this is rho' = -3 (b4'/b4) (rho + p), so with p = 5 rho, rho b4^18 is constant (dsolve):
       a stabiliser absent in the author's vacuum stays absent.  With frozen extra times (U = A, any a4(x4)) the bulk
       source that the equations require is FE-33 (with its A1 = a4''/H^2 terms), with the flux kappa T^sigma_4 =
       (3/16) A (1 + A^2) H^2 sgn(sigma), whose current -T^sigma_4 points towards the fold on both sides and jumps by
       (3/8) A (1 + A^2) H^2; the source of the fold of FE-33, computed here from the junction potentials, with S^4_4 free
       of A1.  Energy budget, a consequence of the Bianchi identity: kappa (rho_bulk + p_1) = -(3/8)(1 + A^2) H^2 at
       constant A, and -3 a4' (rho_bulk + p_1) integrated over sigma with the volume weight e^{-6 H |sigma|} equals the
       jump; at the static block the source of the fold is a tension kappa lambda_F = 61 H/8 plus a pressureless part
       kappa rho_d = H/8 (the fold fluid, FE-65), and 3 a4' rho_d is the part of the jump linear in A; the source of the
       fold takes up exactly the jump, rho_S' + 3 a4' (rho_S + p_S) = [T^sigma_4] for any a4(x4) (the conservation law at
       the fold, an identity);
  ST7  why UM-3 needs it: every term of the fold carries Z = V_t (e^{-a4} b4)^3/V_*, so a coupling has g_eff^2 = g^2/Z and
       d ln g_eff^2/dx4 = 3H (A - U): 3H in the author's vacuum, 0 with frozen extra times; the author's vacuum as the late
       universe (H = H_0) would give Delta ln alpha = 3 H_0 Delta t = 0.37 over the 1.8 Gyr since the natural reactor of
       Oklo, more than a million times the bound |Delta alpha/alpha| < 1.2e-7; integrated over the hidden direction and
       the extra times the stabiliser carries rho_4 = rho_s V_*/(3H) = -H V_*/(48 kappa) per unit volume of ordinary
       space of the fold;
  ST8  the two constraints: the (x4, x4) and the (sigma, x4) components of the bulk equations contain no second time
       derivative (they are free of A1 and U1 for any a4(x4), b4(x4)): kappa T^4_4 = -kappa rho_bulk = (H^2/16) P(A, U),
       P = 5A^6 - 15A^5 U + 15A^4 U^2 - 9A^4 - 5A^3 U^3 + 18A^3 U + 3A^2 - 9A U^3 - 3A U - 3U^2 + 1, and kappa T^sigma_4 =
       (3/16) U G(A, U) H^2 sgn(sigma), G = 5A^2(A - U)^2 - 6A^2 + 6AU + U^2 + 1; with the rate V = U - A of the extra times
       both are symmetric under A <-> V; with frozen extra times (U = A, any a4(x4)) P = 1 - 3A^2, so
       3 a4'^2 = H^2 + 16 kappa rho_bulk = 16 kappa (rho_bulk - rho_s): the stabiliser is the energy density of the bulk
       at which ordinary space stands still; at constant A the pressures change at the order A^2 and differ between
       sigma, ordinary space and the extra times; with frozen extra times the flow is (3/16) A (1 + A^2) H^2 sgn(sigma),
       zero only at A = 0, where P = 1: a bulk without any source cannot have frozen extra times.
  ST9  the corrected weights (1, 1/20, 1/360), Lambda = -7 H^2: the static bulk is a vacuum on both sides of the fold
       ((warped, time)/H^2 = Einstein (15, 21), Gauss-Bonnet (-9, -21), cubic (1, 7), Lambda (-7, -7), sum (0, 0)): the
       stabiliser vanishes; the source of the fold at the static block is a pure tension, kappa S = -(32/5) H in every
       direction along the fold (Einstein (-10, -12, -10), Gauss-Bonnet (4, 8, 4), cubic (-2/5, -12/5, -2/5)); the bulk is
       a vacuum without flux for frozen extra times with any a4(x4) and for static ordinary space with any b4(x4); the two
       constraints become kappa T^4_4 = A^3 (A - U)^3 H^2 and kappa T^sigma_4 = 3 A^2 U (A - U)^2 H^2 sgn(sigma); the author's
       vacuum is no longer a solution (it would need kappa rho_bulk = -H^2); on the frozen branch the fold carries
       kappa rho_m = (16/5) A^2 H and kappa p_m = -(16/15)(3A^2 + 2 A1) H above its tension, conserved by itself.
Writes outputs/stabiliser.json and reports/stabiliser_checks.json.  Runs in about 45 seconds.
Usage: python universe_model_3/code/um3_stabiliser.py

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
     place but a physical object: a thin layer that carries energy and momentum (a brane).
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
sys.path.insert(0, str(HERE))
import um3_fold as FO  # noqa: E402

H = FO.H
A, U, Ad, Ud = FO.A, FO.U, FO.Ad, FO.Ud
H0_KM_S_MPC = 67.4           # Planck 2018
MPC_KM = 3.0856775814913673e19
GYR_S = 1e9 * 365.25 * 86400
OKLO_GYR = 1.8               # the age of the natural reactor of Oklo
OKLO_BOUND = 1.2e-7          # the larger end of -0.9e-7 < Delta alpha/alpha < 1.2e-7 (Damour and Dyson 1996)
# the author's original weights and cosmological constant (ST1 to ST8, the record) and the corrected ones (ST9; the
# author's order of 2026-10-25 07:55: gravitons must travel at the speed of light; um3_weights.py W3, W4)
W_AUTHOR = [None, sp.Integer(1), sp.Rational(1, 32), sp.Rational(1, 1152)]
ALPHA_AUTHOR = [None, sp.Integer(1), W_AUTHOR[2] / H ** 2, W_AUTHOR[3] / H ** 4]
LAMBDA_AUTHOR = -10 * H ** 2
W_CORRECTED = [None, sp.Integer(1), sp.Rational(1, 20), sp.Rational(1, 360)]
ALPHA_CORRECTED = [None, sp.Integer(1), W_CORRECTED[2] / H ** 2, W_CORRECTED[3] / H ** 4]
LAMBDA_CORRECTED = -7 * H ** 2


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


def lhs_with(E, alpha, lam):
    """sum_p alpha_(p) E_(p)^a_b + lam delta^a_b from the Lovelock tensors E of the general warped metric."""
    L = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            L[i, j] = sp.expand(sum(alpha[p] * E[p][i, j] for p in (1, 2, 3)) + (lam if i == j else 0))
    return L


def bulk_lhs(L, side, vals):
    """The left-hand side of the bulk equations on one side of the fold for the author's metric with the rates vals."""
    sub = FO.author_values(side)
    out = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            out[i, j] = sp.simplify(sp.expand(L[i, j].subs(sub).subs(vals)))
    return out


def divergence_diag(g, X, Tdiag):
    """nabla_M T^M_N for a diagonal metric g and a diagonal mixed tensor T^M_M = Tdiag[M] (functions of X)."""
    n = len(X)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                              for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    div = []
    for N in range(n):
        e = sp.diff(Tdiag[N], X[N])
        e += sum(Gam[M][M][P] * (Tdiag[P] if P == N else 0) for M in range(n) for P in range(n))
        e -= sum(Gam[P][M][N] * (Tdiag[M] if M == P else 0) for M in range(n) for P in range(n))
        div.append(sp.simplify(e))
    return div


def junction_potentials(Lmat):
    """The junction potential of the diagonal fold-direction components (x1, x4, x5) of Lmat: F with
    dF/d(f?_s) = the coefficient of the second sigma-derivative f?_ss (? = a, b, n).  The field equations are linear in the
    second sigma-derivatives, which are delta functions at the fold, so the integral of a component across the fold is
    F(after) - F(before): it depends only on the first sigma-derivatives on the two sides.  Returns ({(i, i): F}, exact)."""
    first = [FO.D['a_s'], FO.D['b_s'], FO.D['n_s']]
    second = [FO.D['a_ss'], FO.D['b_ss'], FO.D['n_ss']]
    lam = sp.Symbol('lam')
    out = {}
    exact = True
    for i in (1, 4, 5):
        e = Lmat[i, i].subs({FO.D['a_st']: 0, FO.D['b_st']: 0, FO.D['n_st']: 0})
        C = [sp.diff(e, v) for v in second]
        integrand = sum(C[k].subs({first[m]: lam * first[m] for m in range(3)}, simultaneous=True) * first[k]
                        for k in range(3))
        F = sp.expand(sp.integrate(sp.expand(integrand), (lam, 0, 1)))
        exact = exact and all(sp.expand(sp.diff(F, first[k]) - C[k]) == 0 for k in range(3))
        out[(i, i)] = F
    return out, exact


def fold_source(F, vals):
    """kappa S^a_a = F(sigma = 0+) - F(sigma = 0-) for the author's metric with the rates vals."""
    return {k: sp.factor(sp.expand(F_.subs(FO.author_values(+1)).subs(vals) - F_.subs(FO.author_values(-1)).subs(vals)))
            for k, F_ in F.items()}


def scalar_stress(eps, dphi):
    """T^M_M of a scalar field with the action S = int d^8X sqrt|g| (-(eps/2) g^{MN} d_M phi d_N phi - V), obtained by
    varying the action with respect to the inverse metric of a diagonal metric, T_MN = -(2/sqrt|g|) dS/dg^{MN}, and raising
    one index.  dphi[M] = d_M phi.  Returns (the list of T^M_M in terms of the inverse-metric symbols, those symbols, V)."""
    gam = sp.symbols('gam0:8', nonzero=True)
    Vp = sp.Symbol('V', real=True)
    sqrtg = sp.Mul(*[1 / sp.sqrt(sp.Abs(gm)) for gm in gam])
    Lag = -sp.Rational(1, 2) * eps * sum(gam[M] * dphi[M] ** 2 for M in range(8)) - Vp
    T = []
    for M in range(8):
        TMM = -2 / sqrtg * sp.diff(sqrtg * Lag, gam[M])
        T.append(sp.simplify(gam[M] * TMM))
    return T, gam, Vp


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    Rs, E, L_corrected = FO.general_lhs()
    assert FO.W == W_CORRECTED and FO.LAMBDA == LAMBDA_CORRECTED
    L = lhs_with(E, ALPHA_AUTHOR, LAMBDA_AUTHOR)            # ST1 to ST8: the author's weights (the record)
    t_lhs = time.time() - t0
    stat = {A: 0, U: 0, Ad: 0, Ud: 0}
    vac = {A: 1, U: 0, Ad: 0, Ud: 0}
    Fall, exact_all = junction_potentials(L)

    # ---------------- ST1: the static bulk, order by order, and the source of the fold that it needs
    st = {side: bulk_lhs(L, side, stat) for side in (-1, 1)}
    diag = [sp.nsimplify(st[1][i, i] / H ** 2) for i in range(8)]
    offd = [st[s][i, j] for s in (-1, 1) for i in range(8) for j in range(8) if i != j]
    target = [sp.Rational(-5, 16)] * 4 + [sp.Rational(1, 16)] + [sp.Rational(-5, 16)] * 3
    same_sides = all(sp.simplify(st[1][i, i] - st[-1][i, i]) == 0 for i in range(8))
    kappa_rho_s = -diag[4] * H ** 2          # T^4_4 = -rho
    kappa_p_s = diag[0] * H ** 2
    # the curvature of the static block: constant curvature -H^2 in the seven directions other than the time, none with it
    m7 = [0, 1, 2, 3, 5, 6, 7]
    Rst = {k: sp.simplify(v.subs(FO.author_values(1)).subs(stat)) for k, v in Rs.items()}
    Rst = {k: v for k, v in Rst.items() if v != 0}
    pairs7 = [(a, b) for a in m7 for b in m7 if a < b]
    const_curv = (set(Rst) == {(pq, pq) for pq in pairs7}
                  and all(sp.simplify(Rst[(pq, pq)] + H ** 2) == 0 for pq in pairs7))

    def cc(p, m):
        # E_(p) along a direction of a space of constant curvature K = -H^2 with m other curved directions
        return -sp.Rational(1, 2) * (-H ** 2) ** p * sp.factorial(m) / sp.factorial(m - 2 * p)
    per_order = {}
    orders_ok = True
    for p in (1, 2, 3):
        vals_p = [sp.simplify(ALPHA_AUTHOR[p] * E[p][i, i].subs(FO.author_values(1)).subs(stat)) for i in range(8)]
        orders_ok = (orders_ok and all(sp.simplify(vals_p[i] - ALPHA_AUTHOR[p] * cc(p, 6)) == 0 for i in m7)
                     and sp.simplify(vals_p[4] - ALPHA_AUTHOR[p] * cc(p, 7)) == 0)
        per_order[p] = [sp.nsimplify(vals_p[1] / H ** 2), sp.nsimplify(vals_p[4] / H ** 2)]
    lam_row = [sp.nsimplify(LAMBDA_AUTHOR / H ** 2)] * 2
    sum_ok = all(sp.simplify(sum(per_order[p][k] for p in (1, 2, 3)) + lam_row[k] - [target[1], target[4]][k]) == 0
                 for k in range(2))
    # the source of the fold, order by order (junction potentials), and the Einstein part against Israel's formula
    thin = {}
    exact_p = True
    for p in (1, 2, 3):
        Fp, ex = junction_potentials(ALPHA_AUTHOR[p] * E[p])
        exact_p = exact_p and ex
        thin[p] = {k: v for k, v in fold_source(Fp, {}).items()}
    thin_static = {p: [sp.nsimplify(thin[p][(i, i)].subs(stat) / H) for i in (1, 4, 5)] for p in (1, 2, 3)}
    total_static = fold_source(Fall, stat)
    want_thin = {1: [-10, -12, -10], 2: [sp.Rational(5, 2), 5, sp.Rational(5, 2)],
                 3: [-sp.Rational(1, 8), -sp.Rational(3, 4), -sp.Rational(1, 8)]}
    thin_ok = all(thin_static[p] == want_thin[p] for p in (1, 2, 3))
    total_ok = (total_static == {(1, 1): -sp.Rational(61, 8) * H, (4, 4): -sp.Rational(31, 4) * H,
                                 (5, 5): -sp.Rational(61, 8) * H})
    # Israel: kappa S^a_b = -([K^a_b] - delta^a_b [K]), K^a_b = (1/2) g^{ac} d_sigma g_cb = diag(fa_s x3, fn_s, fb_s x3)
    Kd = [FO.D['a_s']] * 3 + [FO.D['n_s']] + [FO.D['b_s']] * 3
    jK = [sp.expand(k_.subs(FO.author_values(+1)) - k_.subs(FO.author_values(-1))) for k_ in Kd]
    israel = {(i, i): sp.expand(-(jK[i - 1] - sum(jK))) for i in (1, 4, 5)}
    israel_ok = all(sp.simplify(thin[1][k] - israel[k]) == 0 for k in israel)
    out['ST1'] = {'lhs_over_H2_static': [str(x) for x in diag], 'kappa_rho_s': str(kappa_rho_s), 'kappa_p_s': str(kappa_p_s),
                  'off_diagonal_zero': all(x == 0 for x in offd), 'same_on_both_sides': same_sides,
                  'frame_curvature_static_block': {'%s%s,%s%s' % (k[0] + k[1]): str(v) for k, v in Rst.items()},
                  'per_order_over_H2_warped_and_time': {'Einstein': [str(x) for x in per_order[1]],
                                                        'Gauss-Bonnet': [str(x) for x in per_order[2]],
                                                        'cubic': [str(x) for x in per_order[3]],
                                                        'Lambda': [str(x) for x in lam_row]},
                  'fold_source_per_order_over_H_x1_x4_x5': {'Einstein': [str(x) for x in thin_static[1]],
                                                            'Gauss-Bonnet': [str(x) for x in thin_static[2]],
                                                            'cubic': [str(x) for x in thin_static[3]]},
                  'fold_source_static_block_over_H': [str(total_static[(i, i)] / H) for i in (1, 4, 5)],
                  'israel_einstein_part': {'%d' % k[0]: str(v) for k, v in israel.items()}}
    rep.check('ST1_static_bulk_requires_the_stabiliser',
              diag == target and all(x == 0 for x in offd) and same_sides and sp.simplify(kappa_p_s - 5 * kappa_rho_s) == 0
              and const_curv and orders_ok and sum_ok and exact_all and exact_p and thin_ok and total_ok and israel_ok,
              'a4, b4 constant: sum_p alpha_p E_(p) + Lambda = H^2 diag%s (sigma, x1, x2, x3, x4, x5, x6, x7) on both sides of '
              'the fold, no flux: the static bulk requires kappa rho_s = %s, kappa p_s = %s = 5 kappa rho_s; the static block '
              'has the frame curvature R^{ab}_{ab} = -H^2 for each of the 21 pairs of the seven directions other than the time '
              'and none with the time (a space of constant curvature -H^2 times the time line), so alpha_p E_(p) = '
              '-alpha_p (K^p/2) m!/(m - 2p)! with K = -H^2, m = 6 along sigma, ordinary space and the extra times and m = 7 '
              'along the time: (warped, time)/H^2 = Einstein %s, Gauss-Bonnet %s, cubic %s, Lambda %s, sum (-5/16, 1/16); the '
              'source of the fold (the jump of the junction potentials) at the static block, (x1, x4, x5)/H: Einstein %s '
              '(= Israel\'s -([K^a_b] - delta^a_b [K])), Gauss-Bonnet %s, cubic %s, total %s' % (
                  tuple(str(x) for x in diag), kappa_rho_s, kappa_p_s, per_order[1], per_order[2], per_order[3], lam_row,
                  thin_static[1], thin_static[2], thin_static[3], [str(total_static[(i, i)] / H) for i in (1, 4, 5)]))

    # ---------------- ST2: the author's vacuum
    av = bulk_lhs(L, 1, vac)
    av2 = bulk_lhs(L, -1, vac)
    zero_av = all(av[i, j] == 0 and av2[i, j] == 0 for i in range(8) for j in range(8))
    S_av = fold_source(Fall, vac)
    S_av_ok = S_av == {(1, 1): -10 * H, (4, 4): -6 * H, (5, 5): -10 * H}
    full = bulk_lhs(L, 1, {})
    P = sp.expand(16 * full[4, 4] / H ** 2)          # kappa T^4_4 = (H^2/16) P, kappa rho_bulk = -(H^2/16) P
    Gf = 5 * A ** 2 * (A - U) ** 2 - 6 * A ** 2 + 6 * A * U + U ** 2 + 1
    tt, dd, uu = sp.symbols('t d u', real=True)
    P2 = sp.expand(sp.series(P.subs({A: 1 + tt * dd, U: tt * uu}), tt, 0, 3).removeO()).coeff(tt, 2)
    near_ok = (P.subs({A: 1, U: 0}) == 0 and sp.expand(P.subs({A: 1 + tt * dd, U: tt * uu})).coeff(tt, 1) == 0
               and sp.expand(P2 - 12 * ((dd - uu) ** 2 + dd ** 2)) == 0)
    G1_ok = sp.expand(Gf.subs(A, 1) - 2 * U * (3 * U - 2)) == 0
    out['ST2'] = {'author_vacuum_lhs_zero': zero_av, 'fold_source_author_vacuum_over_H': [str(S_av[(i, i)] / H) for i in (1, 4, 5)],
                  'second_order_of_P_at_the_vacuum': str(sp.factor(P2)), 'G_at_A_1': str(sp.factor(Gf.subs(A, 1)))}
    rep.check('ST2_absent_in_the_author_vacuum', zero_av and S_av_ok and near_ok and G1_ok,
              'a4 = H x4, b4 constant (A = 1, U = 0): every component of sum_p alpha_p E_(p) + Lambda vanishes on both sides of '
              'the fold: the primordial bulk is a vacuum solution and needs no stabiliser; its fold source is kappa S = '
              '(x1, x4, x5) %s; near the vacuum kappa rho_bulk = -(H^2/16) P with P = %s ((A - 1 - U)^2 + (A - 1)^2) + third '
              'order, G(1, U) = %s' % ([str(S_av[(i, i)] / H) + ' H' for i in (1, 4, 5)], 12, sp.factor(Gf.subs(A, 1))))

    # ---------------- ST3: the bulk without any source
    gen = bulk_lhs(L, 1, {Ad: 0, Ud: 0})
    comps = sorted({sp.factor(sp.expand(gen[i, j] / H ** 2)) for i in range(8) for j in range(8) if gen[i, j] != 0},
                   key=lambda e: len(str(e)))
    sols = sp.solve(list(comps), [A, U], dict=True)
    real = []
    for s_ in sols:
        a_, u_ = complex(s_[A]), complex(s_[U])
        if abs(a_.imag) < 1e-12 and abs(u_.imag) < 1e-12:
            real.append((round(a_.real, 12), round(u_.real, 12)))
    real = sorted(set(real))
    flux_gen = sp.factor(full[0, 4] / H ** 2)
    res = sp.factor(sp.resultant(P, Gf, A))
    real_U = sorted(set(sp.real_roots(sp.Poly(sp.expand(res), U))))
    P_U0 = sp.factor(P.subs(U, 0))
    any_rate_ok = (real_U == [0] and sp.expand(P_U0 - (A - 1) ** 2 * (A + 1) ** 2 * (5 * A ** 2 + 1)) == 0
                   and sp.simplify(flux_gen - sp.Rational(3, 16) * U * Gf) == 0)
    out['ST3'] = {'components_over_H2_constant_rates': [str(c) for c in comps], 'real_vacuum_points_A_U': real,
                  'resultant_of_P_and_G_in_A': str(res), 'its_real_roots_U': [str(r) for r in real_U],
                  'P_at_U_0': str(P_U0)}
    rep.check('ST3_no_other_vacuum', real == [(-1.0, 0.0), (1.0, 0.0)] and any_rate_ok,
              'without any bulk source: with constant rates the bulk equations hold only at (A, U) = %s; for any a4(x4), '
              'b4(x4) the two constraints (ST8) must hold at every instant, P(A, U) = 0 and U G(A, U) = 0: for U = 0, '
              'P = %s vanishes only at A = +-1; for U != 0, G = 0 and P = 0 would need a common root of the resultant %s, '
              'whose only real root is U = 0: a bulk without any source is at every instant the author\'s vacuum (A = 1, U = 0) '
              'or its time reverse (A = -1, U = 0)' % (real, P_U0, res))

    # ---------------- ST4: the stabiliser is conserved by itself on the static bulk; no pull along sigma
    X = sp.symbols('x0:8', real=True)
    sig = X[0]
    a0, lb0 = sp.symbols('a0 lb0', real=True)
    gS = sp.diag(1, *[sp.exp(2 * (a0 - H * sig))] * 3, -1, *[-sp.exp(2 * (lb0 - a0 - H * sig))] * 3)   # sigma > 0
    rho_s, p_s = sp.symbols('rho_s p_s', real=True)
    Tst = [p_s] * 4 + [-rho_s] + [p_s] * 3
    div = divergence_diag(gS, X, Tst)
    psig, pw, rhow = (sp.Function(n_)(sig) for n_ in ('p_sigma', 'p_w', 'rho_w'))
    div_med = divergence_diag(gS, X, [psig] + [pw] * 3 + [-rhow] + [pw] * 3)
    hydro = sp.simplify(div_med[0] - (sp.diff(psig, sig) - 6 * H * (psig - pw)))
    out['ST4'] = {'divergence': [str(x) for x in div], 'sigma_component_for_a_static_medium': str(sp.simplify(div_med[0]))}
    rep.check('ST4_conserved_by_itself', all(x == 0 for x in div) and hydro == 0 and not div_med[0].has(rhow),
              'nabla_M T^M_N of the constant tensor diag(p_s, p_s, p_s, p_s, -rho_s, p_s, p_s, p_s) on the static bulk: %s for '
              'N = sigma, x1, ..., x7; for any static medium with the pressure p_sigma along sigma and p_w along the warped '
              'directions the sigma component is %s = 0: the energy density does not enter (the time is not warped, so there '
              'is no gravitational pull along sigma), and p_sigma = p_w needs a constant pressure' % (
                  [str(x) for x in div], sp.simplify(div_med[0])))

    # ---------------- ST5: energy conditions and scalar models
    krho = sp.nsimplify(kappa_rho_s / H ** 2)
    kp = sp.nsimplify(kappa_p_s / H ** 2)
    eta = [1, 1, 1, 1, -1, -1, -1, -1]
    Tmix = [kp] * 4 + [-krho] + [kp] * 3                                     # kappa T^a_a / H^2
    def Tnn(n):
        return sum(eta[a] * Tmix[a] * n[a] ** 2 for a in range(8))          # T_ab n^a n^b, T_aa = eta_aa T^a_a
    n41 = [0, 1, 0, 0, 1, 0, 0, 0]
    n40 = [1, 0, 0, 0, 1, 0, 0, 0]
    n15 = [0, 1, 0, 0, 0, 1, 0, 0]
    nulls_ok = all(sum(eta[a] * n[a] ** 2 for a in range(8)) == 0 for n in (n41, n40, n15))
    nec = {'n = e(4) + e(1)': Tnn(n41), 'n = e(4) + e(0)': Tnn(n40), 'n = e(1) + e(5)': Tnn(n15)}
    phid = sp.Symbol('phidot', real=True)
    res5 = {}
    model_ok = True
    for epsv, name in ((1, 'ordinary'), (-1, 'ghost')):
        Th, gam, Vp = scalar_stress(epsv, [0, 0, 0, 0, phid, 0, 0, 0])          # phi(x4)
        Th = [sp.simplify(t_.subs({gam[0]: 1, gam[4]: -1})) for t_ in Th]
        rho_h = sp.simplify(-Th[4])
        p_h = sp.simplify(Th[1])
        model_ok = model_ok and all(sp.simplify(Th[i] - p_h) == 0 for i in (0, 1, 2, 3, 5, 6, 7))
        Ks = sp.Rational(1, 2) * epsv * phid ** 2
        model_ok = model_ok and sp.simplify(rho_h - (Ks + Vp)) == 0 and sp.simplify(p_h - (Ks - Vp)) == 0
        Ts, gam, Vp = scalar_stress(epsv, [phid, 0, 0, 0, 0, 0, 0, 0])          # phi(sigma)
        Ts = [sp.simplify(t_.subs({gam[0]: 1, gam[4]: -1})) for t_ in Ts]
        rho_st = sp.simplify(-Ts[4])
        model_ok = model_ok and all(sp.simplify(Ts[i] + rho_st) == 0 for i in (1, 2, 3, 5, 6, 7))
        res5[name] = {'phi(x4): rho': str(rho_h), 'phi(x4): p': str(p_h), 'phi(sigma): rho': str(rho_st),
                      'phi(sigma): p_sigma': str(Ts[0]), 'phi(sigma): p_other': str(Ts[1])}
    Kq, Vq = sp.symbols('K V', real=True)
    sol_h = sp.solve([sp.Eq(Kq - Vq, 5 * (Kq + Vq))], [Vq], dict=True)[0]
    rho_h5 = sp.simplify((Kq + Vq).subs(sol_h))
    ghost = {'K': 3 * krho, 'V': -2 * krho}
    ghost_ok = (rho_h5 == Kq / 3 and sp.simplify(ghost['K'] - ghost['V'] - 5 * (ghost['K'] + ghost['V'])) == 0
                and ghost['K'] + ghost['V'] == krho and ghost['K'] < 0)
    # the field equation of phi(x4) on the static block: sqrt|g| does not depend on x4 (no friction), so constant rho and p
    # mean a constant speed phidot on a flat stretch of the potential
    sqrt_static = sp.sqrt(sp.Abs(gS.det()))
    no_friction = sp.diff(sqrt_static, X[4]) == 0
    out['ST5'] = {'kappa_rho_over_H2': str(krho), 'kappa_rho_plus_p_over_H2': str(krho + kp),
                  'null_energy_condition_over_H2': {k: str(v) for k, v in nec.items()},
                  'scalar_fields': res5, 'homogeneous_scalar_with_p_5rho': {'V': str(sol_h[Vq]), 'rho': str(rho_h5)},
                  'ghost_model_over_H2_per_kappa': {k: str(v) for k, v in ghost.items()}, 'no_friction': no_friction}
    rep.check('ST5_energy_conditions', krho < 0 and nulls_ok and nec['n = e(4) + e(1)'] == krho + kp < 0
              and nec['n = e(4) + e(0)'] < 0 and nec['n = e(1) + e(5)'] == 0 and model_ok and ghost_ok and no_friction,
              'from ST1: kappa rho_s = %s H^2 < 0 (the weak energy condition fails) and, for the null vector n = e(4) + e(1) '
              '(the time and an ordinary direction), kappa T_ab n^a n^b = kappa (rho_s + p_s) = %s H^2 < 0 (the null energy '
              'condition fails; also along n = e(4) + e(0); along n = e(1) + e(5) it is 0); a scalar field with the action '
              '-(eps/2)(d phi)^2 - V: varying with respect to the metric gives, for phi(x4), rho = eps phidot^2/2 + V and the '
              'pressure eps phidot^2/2 - V in every other direction, and for phi(sigma) the pressure -rho in every direction but '
              'sigma (never 5 rho unless rho = 0); with p = 5 rho, V = %s and rho = %s, so rho_s < 0 needs a negative kinetic '
              'energy: only the ghost (eps = -1, K = 3 rho_s, V = -2 rho_s) reproduces the stabiliser among the scalar fields; '
              'on the static block there is no friction, so it rolls at a constant speed on a flat stretch of its potential' % (
                  krho, krho + kp, sol_h[Vq], rho_h5))

    # ---------------- ST6: the history and the energy of the fold
    x4 = X[4]
    a4f = sp.Function('a4')(x4)
    b4f = sp.Function('b4')(x4)
    rhof = sp.Function('rho')(x4)
    pf = sp.Function('p')(x4)
    gG = sp.diag(1, *[sp.exp(2 * (a4f - H * sig))] * 3, -1, *[-sp.exp(2 * (sp.log(b4f) - a4f - H * sig))] * 3)
    divG = divergence_diag(gG, X, [pf] * 4 + [-rhof] + [pf] * 3)
    cons = sp.simplify(divG[4])
    target6 = -sp.diff(rhof, x4) - 3 * sp.diff(b4f, x4) / b4f * (rhof + pf)
    rr = sp.Function('r')(x4)
    ode = sp.Eq(sp.diff(rr, x4), -18 * sp.diff(b4f, x4) / b4f * rr)
    solved = sp.dsolve(ode, rr)
    dsolve_ok = sp.simplify(sp.diff(solved.rhs * b4f ** 18, x4)) == 0 and solved.rhs != 0
    # frozen extra times (U = A, U1 = A1), any a4(x4): the bulk source of FE-33 (A1 = Ad = a4''/H^2)
    froz = bulk_lhs(L, 1, {U: A, Ud: Ad})
    froz_m = bulk_lhs(L, -1, {U: A, Ud: Ad})
    fe33_bulk = {'rho': (3 * A ** 2 - 1) / 16,
                 'T00': -(3 * A ** 4 + 3 * A ** 2 * Ad + 18 * A ** 2 + 3 * Ad + 5) / 16,
                 'Tii': -(9 * A ** 2 + 2 * Ad + 5) / 16,
                 'Trr': -(3 * A ** 4 + 3 * A ** 2 * Ad + 24 * A ** 2 + 3 * Ad + 5) / 16,
                 'T04': 3 * A * (1 + A ** 2) / 16}
    fe33_bulk_ok = (sp.simplify(-froz[4, 4] / H ** 2 - fe33_bulk['rho']) == 0
                    and sp.simplify(froz[0, 0] / H ** 2 - fe33_bulk['T00']) == 0
                    and all(sp.simplify(froz[i, i] / H ** 2 - fe33_bulk['Tii']) == 0 for i in (1, 2, 3))
                    and all(sp.simplify(froz[i, i] / H ** 2 - fe33_bulk['Trr']) == 0 for i in (5, 6, 7))
                    and sp.simplify(froz[0, 4] / H ** 2 - fe33_bulk['T04']) == 0
                    and sp.simplify(froz_m[0, 4] / H ** 2 + fe33_bulk['T04']) == 0)
    flux_p = sp.factor(froz[0, 4] / H ** 2)
    flux_m = sp.factor(froz_m[0, 4] / H ** 2)
    jump = sp.factor(flux_p - flux_m)
    kS = fold_source(Fall, {U: A, Ud: Ad})                       # frozen extra times, any a4(x4)
    fe33_fold = {(1, 1): -(57 * A ** 2 + 40 * Ad + 183) / 24, (4, 4): -(10 * A ** 2 + 31) / 4,
                 (5, 5): -(2 * A ** 4 + 2 * A ** 2 * Ad + 37 * A ** 2 + 20 * Ad + 61) / 8}
    fe33_fold_ok = all(sp.simplify(kS[k] / H - fe33_fold[k]) == 0 for k in fe33_fold) and sp.diff(kS[(4, 4)], Ad) == 0
    # the energy budget at constant A (identity of the Bianchi identity of the bulk)
    frc = bulk_lhs(L, 1, {U: A, Ud: 0, Ad: 0})
    k_rho = -frc[4, 4]
    k_p1 = frc[1, 1]
    k_sum = sp.factor(k_rho + k_p1)
    released = -3 * A * H * (k_rho + k_p1)
    integrated = sp.simplify(2 * sp.integrate(sp.exp(-6 * H * sig) * released, (sig, 0, sp.oo)))
    # the fold fluid at the static block, from the computed source of the fold: a tension plus a pressureless part
    S0 = {k: v.subs(stat) for k, v in kS.items()}
    kappa_lambdaF = -S0[(1, 1)]                                  # p = -lambda_F along ordinary space
    kappa_rhod = -S0[(4, 4)] - kappa_lambdaF                     # rho_ff = -S^4_4 = lambda_F + rho_d
    fluid_ok = (kappa_lambdaF == sp.Rational(61, 8) * H and S0[(5, 5)] == -kappa_lambdaF and kappa_rhod == H / 8)
    need_fold = 3 * A * H * kappa_rhod
    jump_lin = sp.expand(jump * H ** 2).coeff(A, 1) * A
    rho_S_dot = -sp.diff(kS[(4, 4)], A) * Ad * H                 # d/dx4 of -kappa S^4_4(A), with A' = Ad H
    fold_balance = sp.simplify(rho_S_dot + 3 * A * H * (kS[(1, 1)] - kS[(4, 4)]) - jump * H ** 2) == 0
    budget_ok = (sp.simplify(k_sum + sp.Rational(3, 8) * (1 + A ** 2) * H ** 2) == 0 and fold_balance
                 and sp.simplify(integrated - jump * H ** 2) == 0 and sp.simplify(need_fold - jump_lin) == 0)
    out['ST6'] = {'conservation_x4_component': str(cons), 'p_equal_5rho_solution': str(solved),
                  'frozen_bulk_source_over_H2': {k: str(sp.factor(v)) for k, v in fe33_bulk.items()},
                  'frozen_flux_kappaT_sigma_x4_over_H2_sigma_positive': str(flux_p),
                  'frozen_flux_sigma_negative': str(flux_m), 'jump_at_the_fold_over_H2': str(jump),
                  'kappa_rho_plus_p1_frozen': str(k_sum), 'released_energy_integrated_over_sigma': str(integrated),
                  'kappa_lambda_F': str(kappa_lambdaF), 'kappa_rho_d': str(kappa_rhod),
                  'energy_needed_by_rho_d': str(need_fold), 'part_of_jump_linear_in_A': str(jump_lin),
                  'fold_source_frozen_over_H': {'%d' % k[0]: str(sp.factor(v / H)) for k, v in kS.items()},
                  'fold_takes_up_the_jump_any_a4': fold_balance}
    rep.check('ST6_history', sp.simplify(cons - target6) == 0 and dsolve_ok and fe33_bulk_ok and fe33_fold_ok
              and sp.simplify(flux_p + flux_m) == 0 and budget_ok and fluid_ok,
              'nabla_M T^M_4 = %s for a homogeneous medium (p in every warped direction): rho\' = -3 (b4\'/b4)(rho + p), and '
              'with p = 5 rho %s, i.e. rho b4^18 constant: a stabiliser absent in the author\'s vacuum stays absent; with '
              'frozen extra times (U = A, any a4(x4), A1 = a4\'\'/H^2) the required bulk source is FE-33 (verified with its '
              'A1 terms) and carries the flux kappa T^sigma_4 = %s H^2 (sigma > 0), %s H^2 (sigma < 0), which jumps by %s H^2 at '
              'the fold: the energy current -T^sigma_4 points towards the fold on both sides; the source of the fold (the '
              'jump of the junction potentials) is %s H (x1, x4, x5), with S^4_4 free of A1; energy budget (a consequence of '
              'the Bianchi identity): kappa (rho_bulk + p_1) = %s at constant A, and -3 a4\' (rho_bulk + p_1) integrated over '
              'sigma with the weight e^{-6 H |sigma|} is %s = the jump; at the static block the source of the fold is a '
              'tension kappa lambda_F = %s plus a pressureless part kappa rho_d = %s, which needs 3 a4\' rho_d = %s, the part '
              'of the jump linear in A; the source of the fold takes up exactly the jump, rho_S\' + 3 a4\' (rho_S + p_S) = '
              '[T^sigma_4] for any a4(x4) (the conservation law at the fold, an identity): %s' % (
                  cons, solved, flux_p, flux_m, jump, [str(sp.factor(kS[(i, i)] / H)) for i in (1, 4, 5)], k_sum,
                  integrated, kappa_lambdaF, kappa_rhod, jump_lin, fold_balance))

    # ---------------- ST7: the importance
    # every term of the fold carries Z = V_t (e^{-a4} b4)^3 / V_*; a gauge field -Z F^2/(4 g^2) has g_eff^2 = g^2/Z
    Zf = (sp.exp(-a4f) * b4f) ** 3
    dlng2 = sp.simplify(-sp.diff(sp.log(Zf), x4))
    dlng2_rates = sp.simplify(dlng2.subs({sp.Derivative(a4f, x4): A * H, sp.Derivative(b4f, x4): U * H * b4f}))
    drift_ok = (sp.simplify(dlng2_rates - 3 * H * (A - U)) == 0 and dlng2_rates.subs({A: 1, U: 0}) == 3 * H
                and dlng2_rates.subs(U, A) == 0)
    H0 = H0_KM_S_MPC / MPC_KM                     # 1/s
    dlnalpha = 3 * H0 * OKLO_GYR * GYR_S
    Vs, kap = sp.symbols('V_s kappa', positive=True)
    rho4 = sp.simplify(krho * H ** 2 / kap * Vs * sp.integrate(sp.exp(-6 * H * sig), (sig, 0, sp.oo)) * 2)
    out['ST7'] = {'d_ln_g2_dx4': str(dlng2_rates), 'H0_per_s': H0, 'delta_ln_alpha_Oklo_if_author_vacuum_late': dlnalpha,
                  'Oklo_bound': OKLO_BOUND, 'ratio_to_the_bound': dlnalpha / OKLO_BOUND,
                  'rho_4_of_the_stabiliser': str(rho4)}
    rep.check('ST7_importance', drift_ok and dlnalpha > 1e6 * OKLO_BOUND and sp.simplify(rho4 + H * Vs / (48 * kap)) == 0,
              'every term of the fold carries Z = V_t (e^{-a4} b4)^3/V_*, so a coupling has g_eff^2 = g^2/Z and '
              'd ln g_eff^2/dx4 = %s: 3H in the author\'s vacuum, 0 with frozen extra times; taking the author\'s vacuum as the '
              'late universe (H = H_0 = %.3e /s) would give Delta ln alpha = 3 H_0 Delta t = %.3f over the %.1f Gyr since Oklo, '
              '%.1e times the bound |Delta alpha/alpha| < %.1e; integrated over the hidden direction and the extra times the '
              'stabiliser carries rho_4 = rho_s V_*/(3H) = %s per unit volume of ordinary space of the fold' % (
                  dlng2_rates, H0, dlnalpha, OKLO_GYR, dlnalpha / OKLO_BOUND, OKLO_BOUND, rho4))

    # ---------------- ST8: the two constraints of the bulk equations
    Ptarget = (5 * A ** 6 - 15 * A ** 5 * U + 15 * A ** 4 * U ** 2 - 9 * A ** 4 - 5 * A ** 3 * U ** 3 + 18 * A ** 3 * U + 3 * A ** 2
               - 9 * A * U ** 3 - 3 * A * U - 3 * U ** 2 + 1)
    no_second = P.free_symbols <= {A, U}
    flux_ok = flux_gen.free_symbols <= {A, U} and sp.simplify(flux_gen - sp.Rational(3, 16) * U * Gf) == 0
    Vr = sp.Symbol('V', real=True)                               # the rate of the extra times, V = U - A
    PV = sp.expand(P.subs(U, A + Vr))
    GV = sp.expand(Gf.subs(U, A + Vr))
    sym_ok = (sp.expand(PV - PV.subs({A: Vr, Vr: A}, simultaneous=True)) == 0
              and sp.expand(GV - GV.subs({A: Vr, Vr: A}, simultaneous=True)) == 0)
    Pfrozen = sp.expand(P.subs(U, A))
    froz_any = bulk_lhs(L, 1, {U: A, Ud: Ad})
    friedmann = sp.simplify(-froz_any[4, 4] - (3 * A ** 2 - 1) * H ** 2 / 16) == 0      # kappa rho_bulk, any a4(x4)
    comps8 = [sp.factor(-16 * frc[i, i] / H ** 2) for i in range(8)]
    aniso = len({comps8[0], comps8[1], comps8[5]}) == 3
    flux_frozen = sp.factor(flux_gen.subs(U, A))
    no_frozen_vacuum = (sp.simplify(flux_frozen - sp.Rational(3, 16) * A * (1 + A ** 2)) == 0
                        and sp.solve(sp.Eq(flux_frozen, 0), A) == [0] and P.subs({A: 0, U: 0}) == 1)
    out['ST8'] = {'P_of_A_U': str(P), 'free_of_A1_U1': no_second, 'P_of_A_and_V': str(PV), 'G_of_A_and_V': str(GV),
                  'P_frozen': str(Pfrozen), 'frozen_kappa_rho_bulk_any_a4': '(3A^2 - 1) H^2/16' if friedmann else 'FAILED',
                  'frozen_components_times_minus16_over_H2_constant_A': [str(c) for c in comps8],
                  'flux_any_a4_b4_over_H2_sigma_positive': str(flux_gen), 'flux_free_of_A1_U1': flux_ok,
                  'flux_frozen_over_H2_sigma_positive': str(flux_frozen),
                  'sourceless_bulk_cannot_have_frozen_extra_times': no_frozen_vacuum}
    rep.check('ST8_the_two_constraints', no_second and sp.expand(P - Ptarget) == 0 and flux_ok and sym_ok
              and sp.expand(Pfrozen - (1 - 3 * A ** 2)) == 0 and friedmann and aniso and no_frozen_vacuum,
              'the (x4, x4) and (sigma, x4) components of the bulk equations contain no second time derivative for any '
              'a4(x4), b4(x4) (they are free of A1 and U1): kappa T^4_4 = (H^2/16) P(A, U), P = %s, and kappa T^sigma_4 = %s H^2 '
              '= (3/16) U G(A, U) H^2 for sigma > 0; with the rate V = U - A of the extra times P = %s and G = %s, both '
              'symmetric under A <-> V; with frozen extra times P = %s for any a4(x4): 3 a4\'^2 = H^2 + 16 kappa rho_bulk = '
              '16 kappa (rho_bulk - rho_s): the stabiliser is the bulk energy density at which ordinary space stands still; at '
              'constant A the components -16 kappa T/H^2 along (sigma, x1, x2, x3, x4, x5, x6, x7) are %s (the pressures change '
              'at the order A^2 and differ between sigma, ordinary space and the extra times); with frozen extra times the '
              'flow is %s H^2, zero only at A = 0, where P = 1: a bulk without any source cannot have frozen extra times' % (
                  P, flux_gen, PV, GV, Pfrozen, [str(c) for c in comps8], flux_frozen))

    # ---------------- ST9: the corrected weights remove the stabiliser
    Lc = L_corrected
    stc = {side: bulk_lhs(Lc, side, stat) for side in (-1, 1)}
    zero_static = all(stc[s_][i, j] == 0 for s_ in (-1, 1) for i in range(8) for j in range(8))
    per_c = {}
    for p in (1, 2, 3):
        vals_p = [sp.simplify(ALPHA_CORRECTED[p] * E[p][i, i].subs(FO.author_values(1)).subs(stat)) for i in range(8)]
        per_c[p] = [sp.nsimplify(vals_p[1] / H ** 2), sp.nsimplify(vals_p[4] / H ** 2)]
    lam_c = [sp.nsimplify(LAMBDA_CORRECTED / H ** 2)] * 2
    per_c_ok = (per_c == {1: [15, 21], 2: [-9, -21], 3: [1, 7]} and lam_c == [-7, -7]
                and all(sum(per_c[p][k] for p in (1, 2, 3)) + lam_c[k] == 0 for k in range(2)))
    Fc, exact_c = junction_potentials(Lc)
    thin_c = {}
    for p in (1, 2, 3):
        Fp, ex = junction_potentials(ALPHA_CORRECTED[p] * E[p])
        exact_c = exact_c and ex
        thin_c[p] = [sp.nsimplify(fold_source(Fp, stat)[(i, i)] / H) for i in (1, 4, 5)]
    tot_c = fold_source(Fc, stat)
    tension_ok = (tot_c == {(1, 1): -sp.Rational(32, 5) * H, (4, 4): -sp.Rational(32, 5) * H,
                            (5, 5): -sp.Rational(32, 5) * H}
                  and thin_c == {1: [-10, -12, -10], 2: [4, 8, 4],
                                 3: [-sp.Rational(2, 5), -sp.Rational(12, 5), -sp.Rational(2, 5)]})
    # frozen extra times (U = A, any a4(x4)) and static ordinary space (A = 0, any b4(x4)): vacua, no flux
    frz = {side: bulk_lhs(Lc, side, {U: A, Ud: Ad}) for side in (-1, 1)}
    sts = {side: bulk_lhs(Lc, side, {A: 0, Ad: 0}) for side in (-1, 1)}
    vac_ok = all(frz[s_][i, j] == 0 and sts[s_][i, j] == 0 for s_ in (-1, 1) for i in range(8) for j in range(8))
    # the two constraints with the corrected weights, and the author's vacuum
    genc = bulk_lhs(Lc, 1, {})
    P_c = sp.factor(genc[4, 4] / H ** 2)
    flux_c = sp.factor(genc[0, 4] / H ** 2)
    avc = bulk_lhs(Lc, 1, vac)
    av_rho = sp.nsimplify(-avc[4, 4] / H ** 2)
    cons_ok = (sp.expand(P_c - A ** 3 * (A - U) ** 3) == 0 and sp.expand(flux_c - 3 * A ** 2 * U * (A - U) ** 2) == 0
               and av_rho == -1 and P_c.free_symbols <= {A, U})
    # the fold of the frozen branch: the matter on it is conserved by itself (no flux into it)
    kSc = fold_source(Fc, {U: A, Ud: Ad})
    rho_c = sp.expand(-kSc[(4, 4)] - sp.Rational(32, 5) * H)
    p_c = sp.expand(kSc[(1, 1)] + sp.Rational(32, 5) * H)
    fric = sp.simplify(-sp.diff(kSc[(4, 4)], A) * Ad * H + 3 * A * H * (rho_c + p_c))
    friedmann_ok = (sp.simplify(rho_c - sp.Rational(16, 5) * A ** 2 * H) == 0
                    and sp.simplify(p_c + sp.Rational(16, 15) * (3 * A ** 2 + 2 * Ad) * H) == 0 and fric == 0)
    out['ST9'] = {'weights': [str(w) for w in W_CORRECTED[1:]], 'Lambda_over_H2': str(LAMBDA_CORRECTED / H ** 2),
                  'static_bulk_lhs_zero': zero_static,
                  'per_order_over_H2_warped_and_time': {'Einstein': [str(x) for x in per_c[1]],
                                                        'Gauss-Bonnet': [str(x) for x in per_c[2]],
                                                        'cubic': [str(x) for x in per_c[3]],
                                                        'Lambda': [str(x) for x in lam_c]},
                  'fold_source_per_order_over_H_x1_x4_x5': {'Einstein': [str(x) for x in thin_c[1]],
                                                            'Gauss-Bonnet': [str(x) for x in thin_c[2]],
                                                            'cubic': [str(x) for x in thin_c[3]]},
                  'fold_source_static_block_over_H': [str(tot_c[(i, i)] / H) for i in (1, 4, 5)],
                  'frozen_and_static_space_vacua': vac_ok, 'kappa_T44_over_H2': str(P_c),
                  'kappa_T04_over_H2_sigma_positive': str(flux_c), 'author_vacuum_needs_kappa_rho_bulk_over_H2': str(av_rho),
                  'frozen_fold_kappa_rho_m': str(rho_c), 'frozen_fold_kappa_p_m': str(p_c)}
    rep.check('ST9_corrected_weights_remove_the_stabiliser',
              zero_static and per_c_ok and exact_c and tension_ok and vac_ok and cons_ok and friedmann_ok,
              'with the corrected weights w = (1, 1/20, 1/360) and Lambda = -7 H^2 the static bulk is a vacuum on both sides of '
              'the fold: (warped, time)/H^2 = Einstein %s, Gauss-Bonnet %s, cubic %s, Lambda %s, sum (0, 0), so the stabiliser '
              'of ST1 is zero; the source of the fold at the static block is (x1, x4, x5)/H = Einstein %s, Gauss-Bonnet %s, '
              'cubic %s, total %s: a pure tension kappa lambda_F = 32H/5, no pressureless part; the bulk is a vacuum for frozen '
              'extra times with any a4(x4) and for static ordinary space with any b4(x4), without any flux; the two constraints '
              'become kappa T^4_4 = %s H^2 and kappa T^sigma_4 = %s H^2 (sigma > 0); the author\'s vacuum (A = 1, U = 0) is no '
              'longer a solution (it would need kappa rho_bulk = %s H^2); on the frozen branch the fold carries kappa rho_m = %s '
              'and kappa p_m = %s above its tension, conserved by itself (rho_m\' + 3 a4\'(rho_m + p_m) = %s)' % (
                  per_c[1], per_c[2], per_c[3], lam_c, thin_c[1], thin_c[2], thin_c[3],
                  [str(tot_c[(i, i)] / H) for i in (1, 4, 5)], P_c, flux_c, av_rho, rho_c, p_c, fric))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['lovelock_time_s'] = round(t_lhs, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'stabiliser.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_stabiliser.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'stabiliser_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
