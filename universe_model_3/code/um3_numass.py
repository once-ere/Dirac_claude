#!/usr/bin/env python3
"""um3_numass.py - the lightest neutrino mass and the Dirac phase of the mixing matrix: what UM-3 needs of them, and
what the measurements allow.

The record of UM-3 uses the global fit NuFIT 5.2 (2022; normal ordering, the fit WITHOUT the Super-Kamiokande atmospheric
data: sin^2 theta12 = 0.303, sin^2 theta23 = 0.572, sin^2 theta13 = 0.02203, Delta m^2_21 = 7.41e-5 eV^2, Delta m^2_31 =
2.511e-3 eV^2) with the lightest mass m_1 = 0 and the Dirac phase delta = 0 (NuFIT 5.2 has 197 deg).  This module takes the
newer fit NuFIT 6.0 (I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, I. Martinez-Soler, J. P. Pinheiro and T. Schwetz,
JHEP 12 (2024) 216, arXiv:2410.05380) in both of its data sets:
    IC24 with the Super-Kamiokande atmospheric data (the normal ordering preferred by Delta chi^2 = 6.1): normal ordering
        sin^2 theta12 = 0.308, sin^2 theta23 = 0.470, sin^2 theta13 = 0.02215, delta = 212 deg, Delta m^2_21 = 7.49e-5 eV^2,
        Delta m^2_31 = 2.513e-3 eV^2; inverted ordering sin^2 theta23 = 0.550, sin^2 theta13 = 0.02231, delta = 274 deg,
        Delta m^2_32 = -2.484e-3 eV^2;
    IC19 without the Super-Kamiokande atmospheric data (both orderings fit almost equally well, the inverted one better by
        Delta chi^2 = 0.6): normal ordering sin^2 theta12 = 0.307, sin^2 theta23 = 0.561, sin^2 theta13 = 0.02195,
        delta = 177 deg, Delta m^2_21 = 7.49e-5 eV^2, Delta m^2_31 = 2.534e-3 eV^2 (the data set of the record's fit).
The mixing matrix is U = R23 U13(delta) R12 (rows e, mu, tau; a flavour state is |nu_alpha> = sum_i U*_alpha i |nu_i>), and in
its electron row only theta12 and theta13 appear:
    |U_e1|^2 = cos^2 theta12 cos^2 theta13,  |U_e2|^2 = sin^2 theta12 cos^2 theta13,  |U_e3|^2 = sin^2 theta13.
Checks:
  NM1  the masses m_i(m_lightest) of both orderings and their sums: the smallest sums are sqrt(Dm21) + sqrt(Dm31) (normal)
       and sqrt(|Dm32|) + sqrt(|Dm32| - Dm21) (inverted);
  NM2  the bounds of DESI DR2 (BAO) with the CMB combined with NuFIT 6.0 (W. Elbers et al., arXiv:2503.14744, section IV C;
       LCDM, 95 %): the lightest mass m_l < 0.023 eV (normal ordering; 0.024 eV inverted), sum m_nu < 0.101 eV (normal),
       < 0.133 eV (inverted); the normal ordering is preferred, P(NO) = 0.91 (the inverted ordering is disfavoured, not
       excluded).  The bound sum m_nu < 0.0642 eV of the same data holds for three equal masses with a positive prior on
       the sum and is not a bound on m_1.  At m_1 = 0.023 eV the masses and their sum follow; the effective mass of tritium
       beta decay, m_beta = sqrt(sum |U_ei|^2 m_i^2), stays far below the limit of KATRIN, m_beta < 0.45 eV (90 %, Science
       388 (2025) 180);
  NM3  the Dirac phase drops out of every UM-3 result: |U_ei|^2 does not depend on delta (computed for 0, 177, 212 and
       274 deg), and the three-flavour evolution through the matter of the supernova envelope gives the same P_ee for
       delta = 0 and delta = 212 deg (to the accuracy of the integration), because the matter potential acts only on
       nu_e and the phase can be moved into nu_mu and nu_tau; it enters only the appearance channels: the vacuum
       probability P(nu_mu -> nu_e) = |sum_i U_ei U*_mu i e^{-i m_i^2 L/(2E)}|^2 at L = 295 km, E = 0.6 GeV (the baseline
       and the peak energy of T2K), for delta = 0, 212 and 270 deg, and the Jarlskog invariant J;
  NM4  what the lightest mass changes: the capture rate of the cosmic neutrino background on 100 g of tritium,
       Gamma = Gamma_nr sum_i |U_ei|^2 (1 + s_i) (s_i the mean speed of the mass state i today over the redshifted
       Fermi-Dirac distribution, Gamma_nr the rate of non-relativistic Dirac neutrinos), falls as m_1 grows from 0 to
       0.023 eV; and the sum of the masses, which enters the CMB and BAO calculation of UM-3 through the density of the
       neutrinos today, Omega_nu h^2 = sum m_nu/(93.14 eV), rises from 0.0588 eV to about 0.103 eV;
  NM5  the record (NuFIT 5.2 without the Super-Kamiokande atmospheric data, delta = 0, m_1 = 0) against NuFIT 6.0 (m_1 = 0)
       in the same data set (IC19 without it, delta = 177 deg) and in the preferred one (IC24 with it, delta = 212 deg):
       the solar survival probabilities at the Borexino energies (adiabatic formula of the record), the supernova envelope
       and the CNB rate; the largest relative changes are reported separately for the two comparisons.
Writes outputs/numass.json and reports/numass_checks.json.  Runs in about a second.
Usage: python universe_model_3/code/um3_numass.py

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

import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_flavour as F  # noqa: E402

# NuFIT 6.0 (JHEP 12 (2024) 216), table 1: IC24 with the SK atmospheric data, and IC19 without it
NUFIT6_NO = {'s12': 0.308, 's23': 0.470, 's13': 0.02215, 'delta_deg': 212.0, 'dm21': 7.49e-5, 'dm31': 2.513e-3}
NUFIT6_IO = {'s12': 0.308, 's23': 0.550, 's13': 0.02231, 'delta_deg': 274.0, 'dm21': 7.49e-5, 'dm32': -2.484e-3}
NUFIT6_NO_NOSK = {'s12': 0.307, 's23': 0.561, 's13': 0.02195, 'delta_deg': 177.0, 'dm21': 7.49e-5, 'dm31': 2.534e-3}
# the record: NuFIT 5.2 (2022) without the SK atmospheric data, with delta set to 0 (NuFIT 5.2: 197 deg)
NUFIT52_NO = {'s12': 0.303, 's23': 0.572, 's13': 0.02203, 'delta_deg': 0.0, 'dm21': 7.41e-5, 'dm31': 2.511e-3}
# DESI DR2 BAO + CMB with NuFIT 6.0 (Elbers et al., arXiv:2503.14744, eqs. 22-27), LCDM, 95 %
ML_MAX_NO = 0.023          # eV, lightest mass, normal ordering
ML_MAX_IO = 0.024          # eV, lightest mass, inverted ordering
SUM_MAX_NO = 0.101         # eV
SUM_MAX_IO = 0.133         # eV
P_NO = 0.91                # posterior probability of the normal ordering
SUM_MAX_DEGENERATE = 0.0642  # eV, three equal masses, positive prior on the sum (not a bound on m_1)
MBETA_MAX = 0.45           # eV, KATRIN 2025, 90 %
TCMB = 2.7255
KB, EV = 1.380649e-23, 1.602176634e-19
ZETA3 = 1.2020569031595942
C_SI = 2.99792458e8
SIGMA_BAR_CM2 = 3.834e-45
N_TRITIUM_100G = 100.0 / 3.01604928 * 6.02214076e23


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


def angles(p):
    return tuple(math.asin(math.sqrt(p[k])) for k in ('s12', 's23', 's13'))


def masses_no(m1, p):
    return np.array([m1, math.sqrt(m1 ** 2 + p['dm21']), math.sqrt(m1 ** 2 + p['dm31'])])


def masses_io(m3, p):
    m2 = math.sqrt(m3 ** 2 - p['dm32'])
    return np.array([math.sqrt(m2 ** 2 - p['dm21']), m2, m3])


def mbeta(m, p):
    t12, t23, t13 = angles(p)
    ue2 = np.array([math.cos(t12) ** 2 * math.cos(t13) ** 2, math.sin(t12) ** 2 * math.cos(t13) ** 2, math.sin(t13) ** 2])
    return float(math.sqrt(np.sum(ue2 * m ** 2))), ue2


def envelope(p, delta, E, anti, N=4000):
    """P_ee through the supernova envelope (n_e ~ r^-3), three flavours, normal ordering, with the given parameters (the
    method of the record, um3_flavour.envelope, with its density profile and its path)."""
    t12, t23, t13 = angles(p)
    U = F.pmns(t12, t23, t13, delta)
    m2 = np.diag([0.0, p['dm21'], p['dm31']])
    Uu = U.conj() if anti else U
    sgnV = -1.0 if anti else 1.0
    Hv = Uu @ (m2 / (2 * E * 1e6) / F.HBARC_EV_KM) @ Uu.conj().T

    def Hb(r):
        H = np.broadcast_to(Hv, (len(r), 3, 3)).copy()
        H[:, 0, 0] += sgnV * F.vcc_km(F.ne_env(r))
        return H
    rH = F.r_resonance(p['dm31'], math.cos(2 * t13), E)
    rL = F.r_resonance(p['dm21'], math.cos(2 * t12), E)
    nodes = np.geomspace(0.2 * rH, 5.0 * rL, N + 1)
    psi = F.propagator(Hb, nodes) @ np.array([1, 0, 0], complex)
    pm, ovmin = F.mass_state_probabilities(Hb(np.array([nodes[-1]]))[0], psi, Uu)
    return float(np.sum(pm * np.abs(Uu[0, :]) ** 2)), pm


def solar_adiabatic(p, E, r_prod):
    """The adiabatic solar P_ee of the record (um3_flavour.solar_pee_adiabatic) with the parameters p."""
    t12, t23, t13 = angles(p)
    c13, s13 = math.cos(t13), math.sin(t13)
    k = F.k_vac(p['dm21'], E)
    V = c13 ** 2 * F.vcc_km(F.ne_sun(r_prod))
    c2m = (k * math.cos(2 * t12) - V) / math.hypot(k * math.cos(2 * t12) - V, k * math.sin(2 * t12))
    return c13 ** 4 * (0.5 + 0.5 * math.cos(2 * t12) * c2m) + s13 ** 4


def cnb_rate(m, ue2):
    Tnu0 = (4 / 11) ** (1 / 3) * TCMB
    kT = KB * Tnu0 / EV
    n_flav = 3 * ZETA3 / (2 * math.pi ** 2) * (kT / 1.97327e-5) ** 3
    rate_nr = N_TRITIUM_100G * SIGMA_BAR_CM2 * C_SI * 100 * (n_flav / 2) * 3.15576e7
    pgrid = np.linspace(1e-6, 40.0, 400001) * kT
    wfd = pgrid ** 2 / (np.exp(pgrid / kT) + 1.0)
    speeds = [float(np.trapezoid(wfd * pgrid / np.sqrt(pgrid ** 2 + mm * mm), pgrid) / np.trapezoid(wfd, pgrid)) for mm in m]
    return rate_nr * float(np.sum(ue2 * (1.0 + np.array(speeds)))), speeds, rate_nr


def main():
    t0 = time.time()
    rep = Report()
    out = {'NuFIT_6.0_NO_with_SK_atm': NUFIT6_NO, 'NuFIT_6.0_IO_with_SK_atm': NUFIT6_IO,
           'NuFIT_6.0_NO_without_SK_atm': NUFIT6_NO_NOSK, 'record_NuFIT_5.2_NO_without_SK_atm': NUFIT52_NO,
           'DESI_DR2_with_NuFIT_6.0': {'m_l_max_NO_eV': ML_MAX_NO, 'm_l_max_IO_eV': ML_MAX_IO, 'sum_max_NO_eV': SUM_MAX_NO,
                                       'sum_max_IO_eV': SUM_MAX_IO, 'P_NO': P_NO,
                                       'sum_max_three_equal_masses_eV': SUM_MAX_DEGENERATE}}

    # ---------------- NM1 and NM2
    sum_no_min = float(np.sum(masses_no(0.0, NUFIT6_NO)))
    sum_io_min = float(np.sum(masses_io(0.0, NUFIT6_IO)))
    m_at_max = masses_no(ML_MAX_NO, NUFIT6_NO)
    sum_at_max = float(np.sum(m_at_max))
    mb0, ue2 = mbeta(masses_no(0.0, NUFIT6_NO), NUFIT6_NO)
    mbm, _ = mbeta(m_at_max, NUFIT6_NO)
    # what the degenerate-mass bound would give if it were (wrongly) inserted into the normal-ordering relations
    m1_naive = brentq(lambda m1: float(np.sum(masses_no(m1, NUFIT6_NO))) - SUM_MAX_DEGENERATE, 0.0, 0.05, xtol=1e-12)
    out['NM1'] = {'sum_min_normal_eV': sum_no_min, 'sum_min_inverted_eV': sum_io_min,
                  'masses_normal_m1_0_eV': masses_no(0.0, NUFIT6_NO).tolist(),
                  'masses_inverted_m3_0_eV': masses_io(0.0, NUFIT6_IO).tolist()}
    out['NM2'] = {'m1_max_eV': ML_MAX_NO, 'masses_at_m1_max_eV': m_at_max.tolist(), 'sum_at_m1_max_eV': sum_at_max,
                  'm_beta_range_eV': [mb0, mbm], 'KATRIN_limit_eV': MBETA_MAX,
                  'm1_if_the_degenerate_bound_were_inserted_eV': m1_naive}
    rep.check('NM1_masses', abs(sum_no_min - (math.sqrt(7.49e-5) + math.sqrt(2.513e-3))) < 1e-12
              and abs(sum_io_min - (math.sqrt(2.484e-3) + math.sqrt(2.484e-3 - 7.49e-5))) < 1e-12,
              'NuFIT 6.0: the smallest sum of the masses is %.4f eV in the normal and %.4f eV in the inverted ordering' % (
                  sum_no_min, sum_io_min))
    rep.check('NM2_bounds', sum_no_min < SUM_MAX_NO and sum_io_min < SUM_MAX_IO and abs(sum_at_max - SUM_MAX_NO) < 0.005
              and mbm < 0.03 < MBETA_MAX,
              'DESI DR2 + CMB with NuFIT 6.0 (95 %%): m_l < %.3f eV in the normal ordering (%.3f eV inverted), sum < %.3f eV '
              '(normal), < %.3f eV (inverted); the inverted ordering is disfavoured (P(NO) = %.2f), not excluded: its smallest '
              'sum %.4f eV is allowed; at m_1 = %.0f meV the masses are %s meV, their sum %.4f eV; m_beta = %.2f to %.2f meV, '
              'far below the KATRIN limit %.2f eV (the degenerate bound %.4f eV, wrongly inserted into the normal-ordering '
              'relations, would give %.2f meV)' % (
                  ML_MAX_NO, ML_MAX_IO, SUM_MAX_NO, SUM_MAX_IO, P_NO, sum_io_min, 1e3 * ML_MAX_NO,
                  ['%.2f' % (1e3 * x) for x in m_at_max], sum_at_max, 1e3 * mb0, 1e3 * mbm, MBETA_MAX, SUM_MAX_DEGENERATE,
                  1e3 * m1_naive))

    # ---------------- NM3: the Dirac phase
    t12, t23, t13 = angles(NUFIT6_NO)
    rowsU = {d: (np.abs(F.pmns(t12, t23, t13, math.radians(d))[0, :]) ** 2).tolist() for d in (0.0, 177.0, 212.0, 274.0)}
    dU = max(abs(a - b) for d in rowsU for a, b in zip(rowsU[d], rowsU[0.0]))
    env = {}
    for E in (10.0, 20.0):
        for anti in (False, True):
            p0, _ = envelope(NUFIT6_NO, 0.0, E, anti)
            p1, _ = envelope(NUFIT6_NO, math.radians(212.0), E, anti)
            env['E=%g %s' % (E, 'antineutrino' if anti else 'neutrino')] = {'P_ee_delta_0': p0, 'P_ee_delta_212': p1}
    dP = max(abs(v['P_ee_delta_0'] - v['P_ee_delta_212']) for v in env.values())
    J = {}
    app = {}
    app_bar = {}
    L_km, E_GeV = 295.0, 0.6
    for d in (0.0, 212.0, 270.0):
        U = F.pmns(t12, t23, t13, math.radians(d))
        m2 = np.array([0.0, NUFIT6_NO['dm21'], NUFIT6_NO['dm31']])
        ph = np.exp(-1j * m2 * L_km / (2 * E_GeV * 1e9) / F.HBARC_EV_KM)
        # |nu_mu> = sum_i U*_mu i |nu_i>: amplitude <nu_e| e^{-iHL} |nu_mu> = sum_i U_ei e^{-i phi_i} U*_mu i
        app[d] = float(abs(np.sum(U[0, :] * ph * U[1, :].conj())) ** 2)
        app_bar[d] = float(abs(np.sum(U[0, :].conj() * ph * U[1, :])) ** 2)     # antineutrinos: U -> U*
        J[d] = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))
    out['NM3'] = {'electron_row_abs2': {str(k): v for k, v in rowsU.items()}, 'max_difference_electron_row': dU,
                  'envelope': env, 'max_difference_P_ee': dP,
                  'P_numu_to_nue_T2K_vacuum': {str(k): v for k, v in app.items()},
                  'P_antinumu_to_antinue_T2K_vacuum': {str(k): v for k, v in app_bar.items()},
                  'Jarlskog': {str(k): v for k, v in J.items()}}
    rep.check('NM3_dirac_phase', dU < 1e-15 and dP < 1e-6 and app[212.0] > app[0.0] + 1e-3 and app[270.0] > app[212.0]
              and app_bar[212.0] < app_bar[0.0] and abs(J[212.0]) > 0.01 and abs(J[0.0]) < 1e-17,
              '|U_ei|^2 = %s for delta = 0, 177, 212, 274 deg (largest difference %.0e): the electron row does not contain '
              'delta; the supernova envelope gives the same P_ee for delta = 0 and 212 deg (largest difference %.1e at E = 10, '
              '20 MeV, neutrinos and antineutrinos); the phase appears only in appearance channels: P(nu_mu -> nu_e) in vacuum '
              'at 295 km, 0.6 GeV is %.4f (delta = 0), %.4f (212 deg), %.4f (270 deg); for antineutrinos %.4f, %.4f, %.4f; '
              'J = %.4f at 212 deg' % (['%.5f' % x for x in rowsU[0.0]], dU, dP, app[0.0], app[212.0], app[270.0],
                                        app_bar[0.0], app_bar[212.0], app_bar[270.0], J[212.0]))

    # ---------------- NM4: the lightest mass
    rows4 = []
    for m1 in (0.0, 0.005, 0.010, 0.015, ML_MAX_NO):
        m = masses_no(m1, NUFIT6_NO)
        rate, speeds, rnr = cnb_rate(m, ue2)
        rows4.append({'m1_eV': m1, 'sum_eV': float(np.sum(m)), 'Omega_nu_h2': float(np.sum(m)) / 93.14,
                      'mean_speeds': speeds, 'capture_rate_per_year_100g': rate})
    out['NM4'] = {'rows': rows4, 'rate_nonrelativistic_Dirac': rnr}
    rep.check('NM4_lightest_mass', rows4[0]['capture_rate_per_year_100g'] > rows4[-1]['capture_rate_per_year_100g'] > rnr
              and all(a['capture_rate_per_year_100g'] >= b['capture_rate_per_year_100g'] for a, b in zip(rows4[:-1], rows4[1:])),
              'the CNB capture rate on 100 g of tritium falls from %.2f per year (m_1 = 0) to %.2f (m_1 = %.0f meV) as nu_1 '
              'becomes slow (mean speed %.4f there; %.2f per year if all were at rest); the sum of the masses rises from %.4f '
              'to %.4f eV, and with it the neutrino density of the CMB and BAO calculation, Omega_nu h^2 = sum/(93.14 eV), '
              'from %.2e to %.2e' % (rows4[0]['capture_rate_per_year_100g'], rows4[-1]['capture_rate_per_year_100g'],
                                     1e3 * ML_MAX_NO, rows4[-1]['mean_speeds'][0], rnr, rows4[0]['sum_eV'],
                                     rows4[-1]['sum_eV'], rows4[0]['Omega_nu_h2'], rows4[-1]['Omega_nu_h2']))

    # ---------------- NM5: the record against NuFIT 6.0, like with like and against the preferred data set
    t12r, _, t13r = angles(NUFIT52_NO)
    ue2r = np.array([math.cos(t12r) ** 2 * math.cos(t13r) ** 2, math.sin(t12r) ** 2 * math.cos(t13r) ** 2, math.sin(t13r) ** 2])
    rate_rec, _, _ = cnb_rate(masses_no(0.0, NUFIT52_NO), ue2r)
    comps = {}
    for label, par in (('NuFIT 6.0 without SK-atm', NUFIT6_NO_NOSK), ('NuFIT 6.0 with SK-atm', NUFIT6_NO)):
        sol = []
        for (nm, E, rp) in (('pp', 0.267, 0.10), ('7Be', 0.862, 0.06), ('pep', 1.44, 0.10), ('8B', 8.1, 0.05)):
            r_prod = rp * F.R_SUN_KM
            a = solar_adiabatic(NUFIT52_NO, E, r_prod)
            b = solar_adiabatic(par, E, r_prod)
            sol.append({'line': nm, 'E_MeV': E, 'P_ee_record': a, 'P_ee_new': b, 'relative': (b - a) / a})
        envc = []
        for E in (10.0, 20.0):
            a, _ = envelope(NUFIT52_NO, 0.0, E, False)
            b, _ = envelope(par, math.radians(par['delta_deg']), E, False)
            envc.append({'E_MeV': E, 'P_ee_record': a, 'P_ee_new': b})
        t12n, _, t13n = angles(par)
        ue2n = np.array([math.cos(t12n) ** 2 * math.cos(t13n) ** 2, math.sin(t12n) ** 2 * math.cos(t13n) ** 2,
                         math.sin(t13n) ** 2])
        rate_new, _, _ = cnb_rate(masses_no(0.0, par), ue2n)
        worst = max([abs(x['relative']) for x in sol]
                    + [abs(e['P_ee_new'] - e['P_ee_record']) / max(e['P_ee_record'], 1e-3) for e in envc]
                    + [abs(rate_new / rate_rec - 1)])
        comps[label] = {'solar': sol, 'envelope': envc, 'cnb_rate_record': rate_rec, 'cnb_rate_new': rate_new,
                        'largest_relative_change': worst}
    out['NM5'] = comps
    w1 = comps['NuFIT 6.0 without SK-atm']['largest_relative_change']
    w2 = comps['NuFIT 6.0 with SK-atm']['largest_relative_change']
    rep.check('NM5_record_against_NuFIT6', w1 < 0.03 and w2 < 0.03,
              'solar P_ee (adiabatic; pp, 7Be, pep, 8B): record %s; NuFIT 6.0 without the SK atmospheric data (the record\'s '
              'data set) %s; with it %s; the largest relative change of the solar, supernova-envelope and CNB results is '
              '%.1e like with like and %.1e against the preferred data set' % (
                  ['%.4f' % x['P_ee_record'] for x in comps['NuFIT 6.0 with SK-atm']['solar']],
                  ['%.4f' % x['P_ee_new'] for x in comps['NuFIT 6.0 without SK-atm']['solar']],
                  ['%.4f' % x['P_ee_new'] for x in comps['NuFIT 6.0 with SK-atm']['solar']], w1, w2))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'numass.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_numass.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'numass_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
