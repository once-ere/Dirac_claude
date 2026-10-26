#!/usr/bin/env python3
"""um4_foldsources.py - the sources of the fold of UM-4: its tension, the gravitational waves of the fold, the gravity that
the fields of the fold induce, the fold fluid and the tuning of the tension.

The metric of UM-4 in the proper chart, ds^2 = d sigma^2 + e^{-2H|sigma|} ghat (+ the corrections of um4_fold.py F1 for a curved
fold), Einstein gravity with Lambda = -21 H^2 in the bulk, and the thin source S^a_b of the fold (the junction condition of
Israel, kappa S^a_b = -([K^a_b] - [K] delta^a_b)).  Computed and checked:
  FS1  the tension: for an n-dimensional fold in a bulk of n + 1 dimensions with the warp e^{-2H|sigma|} in every direction of the
       fold, K^a_b = -H sgn(sigma) delta^a_b and kappa S^a_b = -2(n - 1) H delta^a_b: a pure tension kappa lambda_F = 2(n - 1) H,
       12 H for the seven-dimensional fold of UM-4 and 6 H for the four-dimensional brane of Randall and Sundrum (whose
       lambda_RS = 6 k_RS/kappa_5 it reproduces); with the bulk energy Lambda = -n(n - 1) H^2/2 (-21 H^2 for n = 7, -6 k_RS^2 for
       n = 4) this is the critical tension, for which the fold has no cosmological constant of its own (um4_fold.py F2);
  FS2  the gravitational waves of the fold: with frozen extra times a transverse traceless wave of the + polarisation in
       ordinary space, g_11 = e^{2a + eps h}, g_22 = e^{2a - eps h}, h = h(x3, x4), has the linearised Einstein tensor
       (Ghat^1_1 - Ghat^2_2)/2 = (1/2) [h'' + 3 a' h' - e^{-2a} d^2h/dx3^2] eps (computed): the wave equation of general relativity
       on the expanding fold, so with Ghat = kappa_7 tau the waves obey h'' + 3a'h' - e^{-2a} nabla^2 h = 2 kappa_7 Pi (Pi =
       (tau^1_1 - tau^2_2)/2 the anisotropic stress of the matter of the fold), travel at the speed of light at every
       wavelength and couple with the same kappa_7 as the Friedmann equations: the gravitational waves and the expansion of the
       fold have the same Planck mass, and the speed of GW170817 (equal to that of light to 1e-15) holds identically;
  FS3  ESTIMATE, the gravity induced by the fields of the fold (Sakharov; one loop, heat kernel, proper-time cutoff
       Lambda_c): 1/(16 pi G_ind) = N_ind Lambda_c^2/(192 pi^2), N_ind = sum over real scalars (1 - 6 xi) + Weyl fermions - 4 x
       gauge fields of the fold; in UM-4 the gauge fields live in the bulk, so the fields of the fold are the Higgs doublet
       (four real scalars) and 48 Weyl fermions (three generations with three right-handed neutrinos): N_ind = 52 - 24 xi_H;
       it adds to the Planck mass of the fold, 1/(8 pi G_N) = V_*/kappa_7 + 1/kappa_ind, with kappa_ind = 8 pi G_ind; for a cutoff
       Lambda_c of the order of H it is negligible (for H = 2.5 TeV a part 1e-30 of M_red^2); the same loops give the fold a
       vacuum energy of about |N_B - N_F| Lambda_c^4/(64 pi^2) (N_B = 4, N_F = 96 real degrees of freedom), a seven-dimensional
       tension that adds to lambda_F;
  FS4  the tuning of the tension and the dark energy: a tension lambda_F + delta_lambda (delta_lambda the vacuum energy of the fold
       fields and of the fold fluid beyond the critical tension) gives the fold a cosmological constant, Ghat^a_b = kappa_7 (tau^a_b
       - delta_lambda delta^a_b) to the first order (the junction condition with the bulk metric of um4_fold.py F1), so the vacuum
       energy of the four-dimensional world is rho_Lambda = V_* delta_lambda; the observed rho_Lambda = 2.5e-47 GeV^4 then needs
       delta_lambda/lambda_F = rho_Lambda/(30 H^2 M_red^2) (lambda_F V_* = 30 H^2 M_red^2, um4_fold.py F5), 2.3e-92 for H = 2.5 TeV:
       the cosmological constant problem of the brane of Randall and Sundrum, unsolved in UM-4 (OPEN); a vacuum energy with
       frozen extra times needs the pressure q = -2 rho_Lambda along the extra times (the radion condition), of which the tension
       supplies -rho_Lambda and the fold fluid the rest (ASSUMED);
  FS5  the fold fluid (ASSUMED): the static fold source is a pure tension (p = q = -rho); the matter of the fold that does not
       depend on the extra times has q = 0 (radiation, dust) or q = -rho (vacuum energy), and the radion condition q = -(rho -
       3P)/2 of the frozen extra times (um4_fold.py F4) requires the fold fluid to add q_hold = -(rho - 3P)/2 - q_matter: zero for
       radiation, -rho/2 for dust, -rho for a vacuum energy; its energy density is not fixed by the junction condition (it is a
       pressure along the extra times only), and what supplies it is OPEN.
Writes outputs/foldsources.json and reports/foldsources_checks.json.  Runs in a few seconds.
Usage: python universe_model_4/code/um4_foldsources.py

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
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write              # noqa: E402
from um4_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

M_PL_RED = 2.435e18          # GeV
RHO_LAMBDA = 2.5e-47         # GeV^4 (Planck 2018: Omega_Lambda = 0.685, h = 0.674)
H_MIN = 2.5e3                # GeV (um4_propagators.py P5)


def fs(e):
    return sp.expand(sp.powsimp(sp.expand(e), combine='exp'))


def main():
    rep = Report()
    out = {}
    H = sp.Symbol('H', positive=True)

    # ---------------- FS1: the tension for an n-dimensional fold
    rows1 = {}
    ok1 = True
    for n in (4, 7):
        K = -H                                            # K^a_b at 0+, every direction
        kS = -2 * (K - n * K)                             # kappa S^a_b = -2 (K^a_b - K delta^a_b)
        Lam = -sp.Rational(n * (n - 1), 2) * H ** 2
        rows1[n] = {'kappa_lambda_F': str(sp.simplify(-kS)), 'Lambda': str(Lam)}
        ok1 &= sp.simplify(-kS - 2 * (n - 1) * H) == 0
    # the bulk energy of a space of constant curvature -H^2 in n + 1 dimensions: G^M_N = n(n - 1) H^2/2 delta^M_N
    ok1 &= rows1[7]['kappa_lambda_F'] == '12*H' and rows1[4]['kappa_lambda_F'] == '6*H' and rows1[7]['Lambda'] == '-21*H**2'
    out['FS1'] = rows1
    rep.check('FS1_tension', ok1, 'kappa lambda_F = 2(n - 1) H with Lambda = -n(n - 1) H^2/2: n = 7 (UM-4) %s, %s; n = 4 (Randall and '
              'Sundrum) %s, %s, their lambda_RS = 6 k_RS/kappa_5 and Lambda_RS = -6 k_RS^2' % (
                  rows1[7]['kappa_lambda_F'], rows1[7]['Lambda'], rows1[4]['kappa_lambda_F'], rows1[4]['Lambda']))

    # ---------------- FS2: the gravitational waves of the fold
    Y = sp.symbols('x1:8', real=True)
    t, x3 = Y[3], Y[2]
    a = sp.Function('a')(t)
    hf = sp.Function('h')(x3, t)
    eps = sp.Symbol('epsilon')
    eps7 = [1, 1, 1, -1, -1, -1, -1]
    hh = [sp.exp(a + eps * hf / 2), sp.exp(a - eps * hf / 2), sp.exp(a), sp.S(1), sp.S(1), sp.S(1), sp.S(1)]
    g7 = sp.diag(*[eps7[i] * hh[i] ** 2 for i in range(7)])
    R7 = frame_riemann(g7, list(Y), hh, simplify=fs)
    G7 = lovelock_tensor(R7, 1, n=7, simplify=fs)
    TT = sp.expand(sp.diff((G7[0, 0] - G7[1, 1]) / 2, eps).subs(eps, 0))
    target = sp.Rational(1, 2) * (sp.diff(hf, t, 2) + 3 * sp.diff(a, t) * sp.diff(hf, t) - sp.exp(-2 * a) * sp.diff(hf, x3, 2))
    ok2 = sp.simplify(TT - target) == 0
    out['FS2'] = {'linearised_TT': str(sp.simplify(TT)), 'wave_operator': "h'' + 3 a' h' - e^{-2a} h_33"}
    rep.check('FS2_gravitational_waves_of_the_fold', ok2,
              '(Ghat^1_1 - Ghat^2_2)/2 at the first order in eps = %s: the wave equation of general relativity on the expanding fold '
              '(speed of light at every wavelength), with the coupling kappa_7 of the Friedmann equations: GW170817 holds '
              'identically' % sp.simplify(TT))

    # ---------------- FS3: induced gravity (ESTIMATE)
    xi = sp.Symbol('xi_H', real=True)
    N_ind = 4 * (1 - 6 * xi) + 48
    Lc = H_MIN
    inv16piG = float(N_ind.subs(xi, 0)) * Lc ** 2 / (192 * math.pi ** 2)
    frac = 2 * inv16piG / M_PL_RED ** 2               # 1/(8 pi G_ind) relative to M_red^2
    NB, NF = 4, 96
    rho_vac = abs(NB - NF) * Lc ** 4 / (64 * math.pi ** 2)
    ok3 = sp.expand(N_ind - (52 - 24 * xi)) == 0 and frac < 1e-29
    out['FS3'] = {'N_ind': str(sp.expand(N_ind)), 'one_over_8piG_ind_over_Mred2_at_cutoff_H_min': frac,
                  'vacuum_energy_of_the_fold_fields_GeV4_at_cutoff_H_min': rho_vac}
    rep.check('FS3_induced_gravity', ok3,
              'ESTIMATE: N_ind = %s for the fields of the fold of UM-4 (the Higgs doublet and 48 Weyl fermions; the gauge fields are '
              'in the bulk); with the cutoff Lambda_c = %.1e GeV, 1/(8 pi G_ind) = %.1e M_red^2 (negligible); the same loops give a '
              'vacuum energy of about %.1e GeV^4, a tension of the fold' % (sp.expand(N_ind), Lc, frac, rho_vac))

    # ---------------- FS4: the tuning of the tension
    tune = RHO_LAMBDA / (30 * H_MIN ** 2 * M_PL_RED ** 2)
    # the first-order fold equation with a detuned tension: kappa S = -(12 H + kappa dl) delta + (2/(5H)) Ghat + kappa tau
    # (the bulk metric of um4_fold.py F1 fixes the relation between S and Ghat), so Ghat = kappa_7 (tau - dl delta)
    kap, dl = sp.symbols('kappa delta_lambda', positive=True)
    Gh = sp.Symbol('Ghat')
    tau = sp.Symbol('tau')
    lhs = -12 * H + 2 * Gh / (5 * H)                    # kappa S from the bulk (F2)
    rhs = -kap * (12 * H / kap + dl) + kap * tau        # the source: tension lambda_F + delta_lambda and matter tau
    Gsol = sp.solve(sp.Eq(lhs, rhs), Gh)[0]
    kap7 = sp.Rational(5, 2) * kap * H
    ok4 = sp.simplify(Gsol - kap7 * (tau - dl)) == 0 and 1e-93 < tune < 1e-91
    out['FS4'] = {'fold_equation_with_detuned_tension': str(sp.simplify(Gsol)), 'delta_lambda_over_lambda_F_for_rho_Lambda': tune,
                  'H_GeV': H_MIN}
    rep.check('FS4_tension_tuning', ok4,
              'with the tension lambda_F + delta_lambda: Ghat = %s = kappa_7 (tau - delta_lambda): the fold has the cosmological constant '
              'kappa_7 delta_lambda and the four-dimensional vacuum energy rho_Lambda = V_* delta_lambda; the observed value needs '
              'delta_lambda/lambda_F = %.1e at H = %.1e GeV (OPEN, as for Randall and Sundrum)' % (sp.simplify(Gsol), tune, H_MIN))

    # ---------------- FS5: the fold fluid
    rho, P = sp.symbols('rho P', real=True)
    need = -(rho - 3 * P) / 2
    cases = {'radiation': (rho / 3, 0), 'dust': (0, 0), 'vacuum energy': (-rho, -rho)}
    hold = {k_: sp.simplify(need.subs(P, v[0]) - v[1]) for k_, v in cases.items()}
    ok5 = hold['radiation'] == 0 and sp.simplify(hold['dust'] + rho / 2) == 0 and sp.simplify(hold['vacuum energy'] + rho) == 0
    out['FS5'] = {k_: str(v) for k_, v in hold.items()}
    rep.check('FS5_fold_fluid', ok5, 'q_hold = -(rho - 3P)/2 - q_matter: radiation %s, dust %s, vacuum energy %s (ASSUMED; its source is '
              'OPEN)' % (hold['radiation'], hold['dust'], hold['vacuum energy']))
    return write('foldsources', 'um4_foldsources.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
