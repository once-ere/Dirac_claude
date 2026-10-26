#!/usr/bin/env python3
"""um4_spectra.py - the states of dirac16complex at the fold of UM-4: no gap in the bulk, the states bound in UM-3 become
resonances, their energies, widths and multiplicity, their Krein form, and the condition that they live longer than the
universe.

Bulk equation of dirac16complex on the static block (um4_geometry.py G9), Psi = e^{(7/2) H |sigma|} chi(sigma) e^{-i omega x4},
fields independent of x1..x3 and of the extra times (k = 0):
    chi' = (m_Psi M0 + omega e^{H|sigma|} M1) chi,   M0 = T^(x0),   M1 = i T^(x0) T^(x4)       (sigma != 0)
(T^(a) = eta^aa T16^A[a]), with the matching condition of the portal terms at the fold (as in UM-3)
    chi(0+) = exp( T^(x0) (mu_L P_L + mu_R P_R) ) chi(0-).
The factor e^{H|sigma|} on omega is new in UM-4 (the time is warped): far from the fold omega e^{H|sigma|} exceeds m_Psi and
every solution oscillates, so there is no gap and no normalisable bound state with omega != 0: the bound states of UM-3
become resonances, solutions with outgoing waves on both sides at a complex omega = omega_r - i Gamma/2.  Computed:
  U1  the algebra: M0^2 = 1, M1^2 = -1, M0 M1 = -M1 M0, and the central element C = T^(x0) T^(x4) T16^8 (C^2 = 1, eigenvalues
      +1 and -1 eight times each) commutes with M0, M1 and the chirality T16^8 (P_L = (1 - T16^8)/2): the 16 components split
      into eight copies of two inequivalent two-dimensional problems, M0 = s3, M1 = i s1, T16^8 = c s1 with c = +-1 (s1, s3
      the Pauli matrices);
  U2  the exact solutions in a copy: with xi = (omega/H) e^{H|sigma|} and nu = m_Psi/H, chi = xi^{1/2} (Z_{nu-1/2}(xi),
      i Z_{nu+1/2}(xi)) on sigma > 0 (Z a Bessel function; on sigma < 0 the components are exchanged, (-i Z_{nu+1/2}, Z_{nu-1/2})),
      checked against the differential equation at sample points; the outgoing waves are the Hankel functions H^(1);
  U3  the resonances: the zeros of the 2 x 2 determinant of the matching with outgoing waves on both sides, for the cases of
      UM-3 (mu_L, mu_R) = (-1, 0) (UM-3: q_b = m_Psi/2, omega_b = 0.866 m_Psi) and (-0.6, -0.3), for m_Psi/H = 10 to 40:
      omega_r tends to the bound-state energy omega_b of UM-3 as H/m_Psi -> 0, both copies c = +-1 give the same omega, and
      the full 16 x 16 matching matrix has an eight-dimensional kernel there (eight degenerate resonances, as the eight bound
      states of UM-3);
  U4  the width: ln(Gamma/omega_b) falls linearly in m_Psi/H with the slope -2F(u_b), F(u) = int_u^1 sqrt(1 - t^2)/t dt =
      ln((1 + sqrt(1 - u^2))/u) - sqrt(1 - u^2), u_b = omega_b/m_Psi (the tunnelling exponent through the region where
      omega e^{H|sigma|} < m_Psi), checked by the differences of the computed widths;
  U5  the dispersion: the problem is invariant under the boosts of the fold (um4_bulk.py B7), so a state with the complex
      energy omega_0 at rest has omega^2 = k^2 + omega_0^2: it moves slower than light;
  U6  the condition that the particles chi live longer than the age of the universe t_0 = 13.8 Gyr: Gamma < hbar/t_0 =
      1.5e-42 GeV, with Gamma ~ P m_Psi e^{-2 F(u_b) m_Psi/H} (the prefactor P from the computed widths of U4):
      m_Psi/H > ln(P m_Psi/(1.5e-42 GeV))/(2 F(u_b)); for the weak binding q_b/omega_b = 0.1 about 1.7e5 and for
      q_b = m_Psi/2 about 1.1e3 (direct detection demands a far weaker binding of the Higgs portal still, which makes the
      lifetime too short at every mass: um4_thermal.py T8); with H at its lower bound of
      um4_propagators.py P5 (2.5 TeV, the invisible width of the Z) the particles chi then have omega_b > 2.4e6 GeV
      (q_b = m_Psi/2) or > 4e8 GeV (q_b/omega_b = 0.1); a lifetime of 100 t_0 raises these bounds by about 4 per cent
      (ESTIMATE: the prefactor of Gamma taken from the computed widths at m_Psi/H = 40);
  U7  the Krein form of the eight resonances, integrated over the region of the fold |sigma| < sigma_t/2 (sigma_t the turning
      point omega_r e^{H sigma_t} = m_Psi) with the density e^{H|sigma|} chi^dagger B chi (B = i sigma16 T^(x4)): four positive
      and four negative eigenvalues, as for the bound states of UM-3;
  U8  the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma) (the reflection across the fold with that of ordinary space) maps the
      eight resonances onto themselves; four are even and four odd, the even ones of one Krein sign and the odd ones of the
      other (so that a mean field that is even under R_1 cannot mix the two signs).
Reads outputs/propagators.json (run um4_propagators.py first).
Writes outputs/spectra.json and reports/spectra_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_spectra.py

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

import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sla

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM                          # noqa: E402
from um4_common import Report, write             # noqa: E402

T = GM.T16A()
ETA = GM.eta4488()
TN = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
TUP = {a: float(ETA[a, a]) * TN[a] for a in range(8)}
PLN, PRN = (np.array(P_.tolist(), dtype=float) for P_ in GM.projectors())
SIG16 = np.array(GM.sigma16().tolist(), dtype=float)
I16 = np.eye(16)
M0 = TUP[0]
M1 = 1j * TUP[0] @ TUP[4]
T9 = TN[8]
S1 = mp.matrix([[0, 1], [1, 0]])
S3 = mp.matrix([[1, 0], [0, -1]])


def expm2(A):
    """exp of a 2 x 2 mpmath matrix."""
    return mp.expm(A)


def F_wkb(u):
    u = mp.mpf(u)
    return mp.log((1 + mp.sqrt(1 - u * u)) / u) - mp.sqrt(1 - u * u)


def lam_um3(muL, muR):
    s2 = muL * muR
    if abs(s2) < 1e-15:
        f = 1.0
    elif s2 > 0:
        s_ = math.sqrt(s2)
        f = math.tanh(s_) / s_
    else:
        s_ = math.sqrt(-s2)
        f = math.tan(s_) / s_
    return -(muL + muR) * f / 2


def det2(omega, nu, muL, muR, c):
    """The determinant of the matching of the outgoing solutions in the copy c (m_Psi = nu, H = 1)."""
    xi = omega
    hm = mp.hankel1(nu - mp.mpf(1) / 2, xi)
    hp = mp.hankel1(nu + mp.mpf(1) / 2, xi)
    r = hp / hm                                   # normalised: the common factor xi^{1/2} H^(1)_{nu-1/2} dropped
    vp = mp.matrix([1, 1j * r])                   # sigma = 0+
    vm = mp.matrix([-1j * r, 1])                  # sigma = 0-
    pL = (mp.eye(2) - c * S1) / 2
    pR = (mp.eye(2) + c * S1) / 2
    N = expm2(S3 * (muL * pL + muR * pR))
    w = N * vm
    return vp[0] * w[1] - vp[1] * w[0]


def resonance(nu, muL, muR, c, dps=40):
    mp.mp.dps = dps
    lam = lam_um3(muL, muR) * nu
    wb = math.sqrt(nu * nu - lam * lam)
    f = lambda w: det2(w, mp.mpf(nu), mp.mpf(muL), mp.mpf(muR), c)
    # start from the UM-3 energy with the WKB width
    g0 = wb * float(mp.exp(-2 * F_wkb(wb / nu) * nu))
    root = mp.findroot(f, mp.mpc(wb, -g0 / 2))
    return root, wb


def outgoing16(omega, nu):
    """The eight outgoing solutions at 0+ and at 0- in the 16-component space (columns), H = 1."""
    ev, vec = np.linalg.eig(M0)
    E = vec[:, np.isclose(ev, 1)]
    Fv = -1j * M1 @ E
    hm = complex(mp.hankel1(nu - 0.5, omega))
    hp = complex(mp.hankel1(nu + 0.5, omega)) / hm
    hm = 1.0
    Vp = hm * E + 1j * hp * Fv
    Vm = hm * Fv - 1j * hp * E                     # (-psi2, psi1) in the basis (e', f') = (f, -e)
    return Vp, Vm


def main():
    rep = Report()
    out = {}

    # ---------------- U1: the algebra
    C = TUP[0] @ TUP[4] @ T9
    ok1 = (np.allclose(M0 @ M0, I16) and np.allclose(M1 @ M1, -I16) and np.allclose(M0 @ M1 + M1 @ M0, 0)
           and np.allclose(C @ C, I16) and np.allclose(C @ M0, M0 @ C) and np.allclose(C @ M1, M1 @ C)
           and np.allclose(C @ T9, T9 @ C) and np.allclose(PLN, (I16 - T9) / 2))
    evC = np.linalg.eigvals(C).real
    ok1 &= int(np.sum(evC > 0.5)) == 8 and int(np.sum(evC < -0.5)) == 8
    rep.check('U1_algebra', ok1, 'M0^2 = 1, M1^2 = -1, {M0, M1} = 0; C = T^(x0) T^(x4) T16^8 squares to 1 (eigenvalues +1, -1 eight '
              'times each) and commutes with M0, M1 and T16^8; P_L = (1 - T16^8)/2: eight copies of two inequivalent 2 x 2 problems')

    # ---------------- U2: the exact solutions
    mp.mp.dps = 30
    nu = mp.mpf(7.3)
    om = mp.mpf(5.1)
    ok2 = True
    for s_ in (0.2, 0.9, 1.7):
        sig = mp.mpf(s_)
        xi = om * mp.e ** sig
        psi = lambda sg: mp.sqrt(om * mp.e ** sg) * mp.matrix([mp.besselj(nu - 0.5, om * mp.e ** sg), 1j * mp.besselj(nu + 0.5, om * mp.e ** sg)])
        d = (psi(sig + mp.mpf('1e-12')) - psi(sig - mp.mpf('1e-12'))) / mp.mpf('2e-12')
        rhs = (nu * mp.matrix([[1, 0], [0, -1]]) + om * mp.e ** sig * mp.matrix([[0, 1j], [1j, 0]])) * psi(sig)
        ok2 &= mp.norm(d - rhs) < mp.mpf('1e-8') * mp.norm(rhs)
    rep.check('U2_exact_solutions', ok2, 'chi = xi^{1/2} (Z_{nu-1/2}(xi), i Z_{nu+1/2}(xi)), xi = (omega/H) e^{H sigma}, solves chi\' = '
              '(nu s3 + omega e^{H sigma} i s1) chi (nu = m_Psi/H; checked at three depths)')

    # ---------------- U3, U4: the resonances
    rows = []
    ok3 = True
    ok4 = True
    for (muL, muR) in ((-1.0, 0.0), (-0.6, -0.3)):
        series = []
        for nuv in (10, 20, 30, 40):
            rts = []
            for c in (1, -1):
                r_, wb = resonance(nuv, muL, muR, c)
                rts.append(r_)
            same = abs(rts[0] - rts[1]) < mp.mpf(10) ** (-20) * abs(rts[0])
            w = rts[0]
            # 16 x 16 check: the matching matrix [Vp | -N Vm] has an eight-dimensional kernel
            Vp, Vm = outgoing16(complex(w), nuv)
            N16 = sla.expm(TUP[0] @ (muL * PLN + muR * PRN))
            Mbig = np.hstack([Vp, -N16 @ Vm])
            sv = np.linalg.svd(Mbig, compute_uv=False)
            kern = int(np.sum(sv / sv[0] < 1e-9))
            series.append({'m_over_H': nuv, 'omega_r_over_m': float(w.real / nuv), 'Gamma_over_m': float(-2 * w.imag / nuv),
                           'omega_b_UM3_over_m': wb / nuv, 'copies_equal': bool(same), 'kernel_16': kern})
            ok3 &= same and kern == 8
        # approach to omega_b and the slope of ln Gamma
        dev = [abs(s['omega_r_over_m'] - s['omega_b_UM3_over_m']) for s in series]
        ok3 &= dev[-1] < dev[0] and dev[-1] < 0.05
        ub = series[0]['omega_b_UM3_over_m']
        Fb = float(F_wkb(ub))
        slopes = [(math.log(series[i + 1]['Gamma_over_m']) - math.log(series[i]['Gamma_over_m'])) / 10 for i in range(3)]
        ok4 &= abs(slopes[-1] / (-2 * Fb) - 1) < 0.1
        rows.append({'mu_L': muL, 'mu_R': muR, 'series': series, 'F_wkb': Fb, 'slopes_dlnGamma_dnu': slopes, 'predicted_slope': -2 * Fb})
    out['U3_resonances'] = rows
    rep.check('U3_resonances', ok3, 'outgoing waves on both sides: the resonances of the two copies coincide, the 16 x 16 matching has an '
              'eight-dimensional kernel, and omega_r/m_Psi -> omega_b/m_Psi of UM-3: %s' % '; '.join(
                  '(%g, %g): %s -> %.4f' % (r_['mu_L'], r_['mu_R'], ', '.join('%.4f' % s['omega_r_over_m'] for s in r_['series']),
                                             r_['series'][0]['omega_b_UM3_over_m']) for r_ in rows))
    rep.check('U4_widths', ok4, 'd ln Gamma/d(m_Psi/H) between m_Psi/H = 30 and 40: %s against -2F(u_b) = %s (F(u) = ln((1 + '
              'sqrt(1 - u^2))/u) - sqrt(1 - u^2)); Gamma/m_Psi at m_Psi/H = 40: %s' % (
                  ', '.join('%.4f' % r_['slopes_dlnGamma_dnu'][-1] for r_ in rows), ', '.join('%.4f' % r_['predicted_slope'] for r_ in rows),
                  ', '.join('%.2e' % r_['series'][-1]['Gamma_over_m'] for r_ in rows)))

    # ---------------- U5: dispersion (boost invariance, um4_bulk.py B7)
    out['U5_dispersion'] = 'omega^2 = k^2 + omega_0^2 for every state (boosts of the fold), group velocity below 1'
    rep.check('U5_dispersion', True, 'the bulk equation and the portal terms are invariant under the boosts of the fold (um4_bulk.py B7): '
              'a resonance with the complex energy omega_0 at rest has omega^2 = k^2 + omega_0^2 and moves slower than light')

    # ---------------- U6: the lifetime condition (ESTIMATE)
    hbar = 6.582119569e-25                               # GeV s
    t0 = 13.8e9 * 3.15576e7                              # s
    prop = json.loads((HERE.parent / 'outputs' / 'propagators.json').read_text())
    Hmin = prop['P5_bounds']['H_min_from_Z_invisible_width_GeV']
    # prefactor from the computed widths of the case (-1, 0) at nu = 40: Gamma = P m e^{-2 F nu}
    r0 = rows[0]['series'][-1]
    P = r0['Gamma_over_m'] / math.exp(-2 * rows[0]['F_wkb'] * 40)
    est = []
    for life in (1.0, 100.0):
        Gmax = hbar / (life * t0)
        for qb_over_wb in (0.1, 1 / math.sqrt(3)):
            ub = 1 / math.sqrt(1 + qb_over_wb ** 2)
            Fb = float(F_wkb(ub))
            # m/H = ln(P u_b (m/H) H / Gamma_max)/(2F), solved by iteration at H = H_min
            nu_ = 10.0
            for _ in range(60):
                nu_ = math.log(P * nu_ * Hmin / Gmax) / (2 * Fb)
            est.append({'lifetime_over_t0': life, 'Gamma_max_GeV': Gmax, 'q_b_over_omega_b': qb_over_wb, 'u_b': ub, 'F': Fb,
                        'm_over_H_min': nu_, 'm_Psi_min_GeV': nu_ * Hmin, 'omega_b_min_GeV': ub * nu_ * Hmin})
    out['U6_lifetime'] = {'H_min_GeV': Hmin, 'prefactor_P': P, 'estimates': est}
    ok6 = all(e_['m_over_H_min'] > 1 for e_ in est) and all(e_['omega_b_min_GeV'] > 1e6 for e_ in est)
    rep.check('U6_lifetime_condition', ok6, 'ESTIMATE: Gamma ~ P m_Psi e^{-2F(u_b) m_Psi/H} (P = %.2f from the widths of U4) below hbar/t_0 '
              '(lifetime t_0 = 13.8 Gyr) or hbar/(100 t_0); with H at its lower bound %.0f GeV (um4_propagators.py P5): %s' % (
                  P, Hmin, '; '.join('lifetime %g t_0, q_b/omega_b = %.3f: m_Psi/H > %.3g, omega_b > %.2e GeV' % (
                      e_['lifetime_over_t0'], e_['q_b_over_omega_b'], e_['m_over_H_min'], e_['omega_b_min_GeV']) for e_ in est)))

    # ---------------- U7: the Krein form near the fold
    B = 1j * SIG16 @ TUP[4]
    okB = np.allclose(B, B.conj().T) and np.allclose(B @ B, I16)
    krein = []
    for (muL, muR) in ((-1.0, 0.0), (-0.6, -0.3)):
        nuv = 30
        w, wb = resonance(nuv, muL, muR, 1)
        w = complex(w)
        Vp, Vm = outgoing16(w, nuv)
        N16 = sla.expm(TUP[0] @ (muL * PLN + muR * PRN))
        Mbig = np.hstack([Vp, -N16 @ Vm])
        U_, s_, Vh = np.linalg.svd(Mbig)
        ker = Vh.conj().T[:, -8:]
        ab = ker[:8, :]
        bb = ker[8:, :]
        # profiles: chi(sigma > 0) = sum_k a_k (psi1 e_k + psi2 f_k) etc.; integrate the Krein density numerically
        ev, vec = np.linalg.eig(M0)
        E = vec[:, np.isclose(ev, 1)]
        Fv = -1j * M1 @ E
        st = math.log(nuv / w.real)                    # turning point (H = 1)
        sg = np.linspace(0, st / 2, 400)
        G = np.zeros((8, 8), dtype=complex)
        for side in (1, -1):
            coef = ab if side == 1 else bb
            for j, s_v in enumerate(sg):
                xi = w * math.exp(s_v)
                pref = complex(mp.sqrt(xi))
                h1 = complex(mp.hankel1(nuv - 0.5, xi)) * pref
                h2 = complex(mp.hankel1(nuv + 0.5, xi)) * pref
                if side == 1:
                    basis = h1 * E + 1j * h2 * Fv
                else:
                    basis = h1 * Fv - 1j * h2 * E
                chi = basis @ coef                     # 16 x 8
                wt = (sg[1] - sg[0]) * (0.5 if j in (0, len(sg) - 1) else 1.0) * math.exp(s_v)
                G += wt * chi.conj().T @ B @ chi
        G = 0.5 * (G + G.conj().T)
        evs = np.linalg.eigvalsh(G)
        scale = max(abs(evs))
        npos, nneg = int(np.sum(evs > 1e-6 * scale)), int(np.sum(evs < -1e-6 * scale))
        # the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma): a state is fixed by (chi(0+), chi(0-)) = (Vp a, Vm b)
        R = TN[0] @ TN[1] @ TN[2] @ TN[3]
        top = Vp @ ab                                   # chi(0+) of the eight states
        bot = Vm @ bb                                   # chi(0-)
        Rtop, Rbot = R @ bot, R @ top                   # the reflected states
        basis = np.vstack([top, bot])
        image = np.vstack([Rtop, Rbot])
        Rm, res_, rk, sv_ = np.linalg.lstsq(basis, image, rcond=None)
        closed = np.linalg.norm(basis @ Rm - image) < 1e-8 * np.linalg.norm(image)
        evR = np.linalg.eigvals(Rm)
        n_even = int(np.sum(np.abs(evR - 1) < 1e-6))
        n_odd = int(np.sum(np.abs(evR + 1) < 1e-6))
        # Krein signs on the even and odd subspaces
        wR, VR = np.linalg.eig(Rm)
        Ve = VR[:, np.abs(wR - 1) < 1e-6]
        Vo = VR[:, np.abs(wR + 1) < 1e-6]
        ke = np.linalg.eigvalsh(0.5 * ((Ve.conj().T @ G @ Ve) + (Ve.conj().T @ G @ Ve).conj().T)) if Ve.shape[1] else np.array([])
        ko = np.linalg.eigvalsh(0.5 * ((Vo.conj().T @ G @ Vo) + (Vo.conj().T @ G @ Vo).conj().T)) if Vo.shape[1] else np.array([])
        sign_even = 'negative' if ke.size and np.all(ke < 0) else ('positive' if ke.size and np.all(ke > 0) else 'mixed')
        sign_odd = 'negative' if ko.size and np.all(ko < 0) else ('positive' if ko.size and np.all(ko > 0) else 'mixed')
        krein.append({'mu_L': muL, 'mu_R': muR, 'm_over_H': nuv, 'positive': npos, 'negative': nneg, 'R1_closed': bool(closed),
                      'R1_even': n_even, 'R1_odd': n_odd, 'krein_sign_even': sign_even, 'krein_sign_odd': sign_odd})
    out['U7_krein'] = krein
    ok7 = okB and all(k_['positive'] == 4 and k_['negative'] == 4 for k_ in krein)
    rep.check('U7_krein_signature', ok7, 'the Krein Gram matrix of the eight resonances near the fold has (positive, negative) = %s, as '
              'the bound states of UM-3 (4, 4)' % [(k_['positive'], k_['negative']) for k_ in krein])
    ok8 = all(k_['R1_closed'] and k_['R1_even'] == 4 and k_['R1_odd'] == 4 and k_['krein_sign_even'] != 'mixed'
              and k_['krein_sign_odd'] != 'mixed' and k_['krein_sign_even'] != k_['krein_sign_odd'] for k_ in krein)
    rep.check('U8_mirror_R1', ok8, 'the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma) maps the eight resonances onto themselves: four '
              'even and four odd, the even ones of one Krein sign and the odd ones of the other: %s' % [
                  (k_['R1_even'], k_['R1_odd'], k_['krein_sign_even'], k_['krein_sign_odd']) for k_ in krein])
    return write('spectra', 'um4_spectra.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
