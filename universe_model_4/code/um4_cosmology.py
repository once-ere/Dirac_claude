#!/usr/bin/env python3
"""um4_cosmology.py - the CMB, the CNB and the BAO of UM-4 (SOLUTION.md; the cosmological perturbations and the expanding
universe of FIELD_EQUATIONS.md, FE-53 to FE-59 and FE-62).

In UM-4 the fold obeys, to the first order in its curvature over H^2, the Einstein equations of seven dimensions with
kappa_7 = 5 kappa H/2 (um4_fold.py F2), and with the volume of the extra times held fixed (the fold fluid supplies the pressure
along the extra times, um4_background.py BG3: a free volume is excluded by lunar laser ranging) these are the Friedmann
equations of general relativity with 8 pi G_N = kappa_7/V_* (F4); the corrections are of the relative order (12/25) A^2 with
A = a4'/H (F5), below 1e-50 after nucleosynthesis for H >= 2.5 TeV (um4_propagators.py P5), and are dropped together with the
terms eps_c^2 (eps_c ~ 1e-5, the size of the Bardeen potentials of FE-54).  The cosmological perturbations are those of
general relativity on the fold: the bulk graviton and the bulk photon have the zero modes of the fold and a continuum of
massive modes whose effects are suppressed by powers of k/H (um4_propagators.py P2, P3), negligible at cosmological wave
numbers.  The CMB and the BAO are then FE-54 to FE-57 for the content of UM-4:
  * the dark matter: the particles chi of dirac16complex (the long-lived resonances at the fold, um4_spectra.py U6),
    pressureless (P/e -> 0 in the dilute limit, um4_kohnsham.py K7), with a drag on the baryons that the direct-detection
    bounds make negligible (FE-55);
  * the dark energy: the vacuum energy rho_Lambda of the fold, w = -1 exactly (FE-59; um4_foldsources.py FS4);
  * the baryons and photons of the Standard Model;
  * three Dirac neutrinos of the normal ordering with the lightest mass zero (m_2 = sqrt(Delta m^2_21) = 8.61 meV,
    m_3 = sqrt(Delta m^2_31) = 50.1 meV), whose right-handed states are not populated (N_eff = 3.044), or are populated by
    the current portal and decouple above the electroweak scale (Delta N_eff = 3 (10.75/106.75)^{4/3} = 0.141, FE-62).
The Boltzmann hierarchy (FE-55) and the line-of-sight integrals (FE-57) are solved by CAMB (Lewis, Challinor and Lasenby
2000) with these inputs; the background FE-58/FE-59 and the BAO ruler FE-56 are computed a second time here, independently.
The primordial spectrum and the optical depth are inputs (ASSUMED, FE-57): the Planck 2018 values (TT,TE,EE+lowE+lensing).
Checks:
  C1  the background: H(z) of FE-59 (general relativity, to the first order in (H_4/H)^2, with frozen extra times) with
      photons, the three neutrino states (exact Fermi-Dirac integrals), baryons, chi and rho_Lambda, computed here, equals
      CAMB's to 1e-5 from z = 0 to 1e4; age of the fold universe;
  C2  the BAO ruler FE-56: the sound horizon at the drag epoch and D_M, D_H, D_V at the DESI redshifts, integrated here,
      equal CAMB's to 1e-4;
  C3  the CMB to order eps_c: the derived quantities z*, r*, 100 theta*, z_drag, r_drag, k_D, z_eq, sigma_8 and the age of
      UM-4 with the Planck 2018 parameters lie within 1 sigma of the Planck 2018 values;
  C4  the CMB spectra against the Planck 2018 high-l data (plik-lite TT, TE, EE: 613 bins for 30 <= l <= 2508, and two
      low-l TT bins): the implementation here reproduces the reference log-likelihoods of the plik-lite code on its test
      spectrum; chi^2 of UM-4 and of UM-4 with thermal nu_R at the same theta*;
  C5  the BAO against DESI DR2 (13 measurements with their correlations): chi^2 of UM-4 with the Planck parameters, and with
      Omega_m and h r_d fitted to DESI alone; UM-4 has w = -1 and cannot follow the w0 > -1, wa < 0 that DESI DR2 + CMB prefer
      at 3.1 sigma;
  C6  the CNB: T_nu = (4/11)^{1/3} T_gamma, 112 per cm^3 per flavour (FE-53), the three mass states and the redshifts at
      which they become non-relativistic, Omega_nu h^2 (FE-58); for Dirac neutrinos only one helicity of each state is
      populated, so the capture rate on tritium is half that of Majorana neutrinos (about 4 per year per 100 g).
The Planck data are downloaded once into universe_model_4/external/ (git clone of github.com/heatherprince/planck-lite-py,
which carries the plik-lite files of the Planck Legacy Archive); they are not redistributed.
Writes outputs/cosmology.json, outputs/cmb_spectra.csv, outputs/cmb_spectra.png and reports/cosmology_checks.json.
Usage: python universe_model_4/code/um4_cosmology.py

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
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.io import FortranFile
from scipy.optimize import minimize
import scipy.linalg as sla

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
EXT = UM4 / 'external' / 'planck-lite-py'

# constants (SI, CODATA 2018 as in CAMB)
C_SI, G_SI, SIGMA_B, KB, EV = 2.99792458e8, 6.67430e-11, 5.670374419e-8, 1.380649e-23, 1.602176634e-19
MPC = 3.085677581491367e22
C_KMS = C_SI / 1e3
TCMB = 2.7255
ZETA3, ZETA5 = 1.2020569031595942, 1.0369277551433699
# Planck 2018 (TT,TE,EE+lowE+lensing): the inputs and the derived values with their errors (Planck 2018 VI, Table 2)
P18 = {'ombh2': 0.02237, 'omch2': 0.1200, 'tau': 0.0544, 'lnAs': 3.044, 'ns': 0.9649, 'H0': 67.36}
P18_DERIVED = {'age': (13.797, 0.023), 'zstar': (1089.92, 0.25), 'rstar': (144.43, 0.26), 'thetastar': (1.04110, 0.00031),
               'zdrag': (1059.94, 0.30), 'rdrag': (147.09, 0.26), 'kd': (0.14087, 0.00030), 'zeq': (3402.0, 26.0),
               'sigma8': (0.8111, 0.0060)}
# DESI DR2 (DESI Collaboration 2025, arXiv:2503.14738, Table IV): z_eff, D_V/r_d or (D_M/r_d, D_H/r_d, r_MH)
DESI_DR2 = [('BGS', 0.295, ('V', 7.942, 0.075)),
            ('LRG1', 0.510, ('MH', 13.588, 0.167, 21.863, 0.425, -0.459)),
            ('LRG2', 0.706, ('MH', 17.351, 0.177, 19.455, 0.330, -0.404)),
            ('LRG3+ELG1', 0.934, ('MH', 21.576, 0.152, 17.641, 0.193, -0.416)),
            ('ELG2', 1.321, ('MH', 27.601, 0.318, 14.176, 0.221, -0.434)),
            ('QSO', 1.484, ('MH', 30.512, 0.760, 12.817, 0.516, -0.500)),
            ('Lya', 2.330, ('MH', 38.988, 0.531, 8.632, 0.101, -0.431))]
# the neutrino masses of UM-4 (normal ordering, lightest state massless; Delta m^2 of FIELD_EQUATIONS)
DM21, DM31 = 7.41e-5, 2.511e-3
M_NU = (0.0, math.sqrt(DM21), math.sqrt(DM31))
NEFF_SM = 3.044
DNEFF_NUR = 3 * (10.75 / 106.75) ** (4 / 3)
# tritium capture of the CNB (Long, Lunardini and Sabancilar 2014): the averaged cross-section and the target
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


# ---------------------------------------------------------------- the background, computed here
_I0 = 7 * math.pi ** 4 / 120


def _I_exact(y):
    return quad(lambda q: q * q * math.sqrt(q * q + y * y) * math.exp(-q) / (1.0 + math.exp(-q)), 0, 120.0, limit=400,
                epsabs=0, epsrel=1e-12)[0]


_YT = np.geomspace(1e-4, 3e4, 900)
_IT = CubicSpline(np.log(_YT), np.log([_I_exact(y) for y in _YT]))


def fd_energy_integral(y):
    """I(y) = int_0^inf q^2 sqrt(q^2 + y^2)/(e^q + 1) dq (I(0) = 7 pi^4/120); non-relativistic expansion above y = 3e4."""
    y = np.asarray(y, float)
    out = np.empty_like(y)
    small, big = y <= _YT[0], y >= _YT[-1]
    mid = ~small & ~big
    out[small] = _I0
    out[mid] = np.exp(_IT(np.log(y[mid])))
    out[big] = 1.5 * ZETA3 * y[big] + 22.5 * ZETA5 / (2 * y[big])
    return out


class Background:
    """H(z) of FE-59 for a flat fold: photons, three neutrino states of masses m_i with the temperature
    T_i = (N_eff/3)^{1/4} (4/11)^{1/3} T_gamma (the convention of CAMB for N_eff), baryons, chi (pressureless) and the
    vacuum energy rho_Lambda (the remainder to the critical density)."""

    def __init__(self, h, ombh2, omch2, masses=M_NU, neff=NEFF_SM, Tcmb=TCMB):
        self.h = h
        H0 = h * 1e5 / MPC
        rho_c = 3 * H0 ** 2 / (8 * math.pi * G_SI)
        self.Og = 4 * SIGMA_B * Tcmb ** 4 / C_SI ** 3 / rho_c
        self.Ob, self.Oc = ombh2 / h ** 2, omch2 / h ** 2
        self.Tnu = (neff / 3) ** 0.25 * (4 / 11) ** (1 / 3) * Tcmb
        self.kTnu_eV = KB * self.Tnu / EV
        self.masses = masses
        self.Onu_rel = 7 / 8 * (self.Tnu / Tcmb) ** 4 * self.Og       # per state, relativistic limit
        self.OL = 1 - self.Og - self.Ob - self.Oc - self.Onu(0.0)

    def Onu(self, z):
        z = np.asarray(z, float)
        a = 1 / (1 + z)
        tot = 0.0
        for m in self.masses:
            tot = tot + self.Onu_rel * a ** -4 * fd_energy_integral(m * a / self.kTnu_eV) / _I0
        return tot

    def E2(self, z):
        z = np.asarray(z, float)
        return self.Og * (1 + z) ** 4 + self.Onu(z) + (self.Ob + self.Oc) * (1 + z) ** 3 + self.OL

    def H(self, z):
        return 100 * self.h * np.sqrt(self.E2(z))                    # km/s/Mpc

    def DM(self, z, n=4000):
        zz = np.linspace(0, z, n + 1)
        return float(np.trapezoid(C_KMS / self.H(zz), zz)) if n else 0.0

    def DM_simpson(self, z, n=4000):
        zz = np.linspace(0, z, 2 * n + 1)
        f = C_KMS / self.H(zz)
        dz = zz[1] - zz[0]
        return float(dz / 3 * (f[0] + f[-1] + 4 * f[1:-1:2].sum() + 2 * f[2:-1:2].sum()))

    def rs(self, zd, n=20000):
        """FE-56: r_s = int_0^{tau_d} c_s d tau_c, c_s = 1/sqrt(3(1 + R)), R = 3 rho_b/(4 rho_gamma), as an integral over ln a."""
        la = np.linspace(math.log(1e-9), math.log(1 / (1 + zd)), 2 * n + 1)
        a = np.exp(la)
        z = 1 / a - 1
        R = 3 * self.Ob / (4 * self.Og) * a
        f = C_KMS / np.sqrt(3 * (1 + R)) / (a * self.H(z))
        d = la[1] - la[0]
        return float(d / 3 * (f[0] + f[-1] + 4 * f[1:-1:2].sum() + 2 * f[2:-1:2].sum()))

    def age_Gyr(self, n=20000):
        la = np.linspace(math.log(1e-10), 0.0, 2 * n + 1)
        a = np.exp(la)
        f = 1 / self.H(1 / a - 1)
        d = la[1] - la[0]
        s = d / 3 * (f[0] + f[-1] + 4 * f[1:-1:2].sum() + 2 * f[2:-1:2].sum())
        return float(s * MPC / 1e3 / (3.15576e7 * 1e9))


# ---------------------------------------------------------------- CAMB
def camb_params(neff=NEFF_SM, masses=M_NU, thetastar=None, planck_neutrinos=False, lmax=2508, par=None):
    """CAMB parameters: the Planck 2018 inputs (or those of par: ombh2, omch2, lnAs, ns, tau) and the neutrinos of UM-4 (one
    massless and two massive Dirac states, each with the CAMB degeneracy N_eff/3), or Planck's convention (one massive state
    of 0.06 eV); with thetastar the Hubble constant is solved for that acoustic angle with the final neutrino set-up."""
    import camb
    q = dict(P18)
    q.update(par or {})
    p = camb.CAMBparams()
    p.set_cosmology(H0=q['H0'], ombh2=q['ombh2'], omch2=q['omch2'], mnu=0.06, nnu=neff, num_massive_neutrinos=1,
                    tau=q['tau'], TCMB=TCMB)
    p.InitPower.set_params(As=math.exp(q['lnAs']) * 1e-10, ns=q['ns'])
    p.set_for_lmax(lmax, lens_potential_accuracy=1)
    p.WantTransfer = True
    p.set_matter_power(redshifts=[0.0], kmax=10.0)
    if not planck_neutrinos:
        deg = neff / 3
        mm = [m for m in masses if m > 0]
        p.num_nu_massless = deg * (3 - len(mm))
        p.num_nu_massive = len(mm)
        p.nu_mass_eigenstates = len(mm)
        p.nu_mass_degeneracies = [deg] * len(mm)
        p.nu_mass_numbers = [1] * len(mm)
        p.nu_mass_fractions = [m / sum(mm) for m in mm]
        p.omnuh2 = sum(mm) / 94.06410581217612 * deg ** 0.75
        p.share_delta_neff = False
    if thetastar is not None:
        p.set_H0_for_theta(thetastar, cosmomc_approx=False)
    return p


def camb_run(p):
    import camb
    r = camb.get_results(p)
    d = r.get_derived_params()
    d['sigma8'] = float(r.get_sigma8_0())
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK')['total']   # D_l: TT, EE, BB, TE
    return r, d, cl


# ---------------------------------------------------------------- Planck 2018 plik-lite (high l) and two low-l TT bins
def fetch_planck():
    data = EXT / 'data'
    if not (data / 'planck2018_plik_lite' / 'cl_cmb_plik_v22.dat').exists():
        EXT.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/heatherprince/planck-lite-py.git', str(EXT)],
                       check=True, capture_output=True, timeout=300)
    return data


class PlikLite:
    """The plik-lite likelihood (Planck 2018 likelihood paper, arXiv:1907.12875): binned, foreground-marginalised C_l with
    their covariance; Planck calibration y_P = 1; optionally two Gaussian low-l TT bins (Prince and Dunkley 2019)."""

    def __init__(self, data_dir, spectra='TTTEEE', low_ell=False):
        d = Path(data_dir) / 'planck2018_plik_lite'
        self.nb = {'TT': 215, 'TE': 199, 'EE': 199}
        bval, X, sig = np.genfromtxt(d / 'cl_cmb_plik_v22.dat', unpack=True)
        self.blmin = np.loadtxt(d / 'blmin.dat').astype(int)
        self.blmax = np.loadtxt(d / 'blmax.dat').astype(int)
        self.w = np.loadtxt(d / 'bweight.dat')
        n = sum(self.nb.values())
        f = FortranFile(d / 'c_matrix_plik_v22.dat', 'r')
        cov = f.read_reals(dtype=float).reshape((n, n))
        cov = np.tril(cov) + np.tril(cov, -1).T                 # the file holds the lower triangle
        self.spectra = spectra
        sel = np.arange(self.nb['TT']) if spectra == 'TT' else np.arange(n)
        self.X = X[sel]
        self.bval = bval[sel]
        self.sig = sig[sel]
        fisher = sla.cho_solve(sla.cho_factor(cov[np.ix_(sel, sel)]), np.eye(len(sel)))
        self.low = None
        if low_ell:
            dl = Path(data_dir) / 'planck2018_low_ell'
            bl, Xl, sl = np.genfromtxt(dl / 'CTT_bin_low_ell_2018.dat', unpack=True)
            self.low = (np.loadtxt(dl / 'blmin_low_ell.dat').astype(int), np.loadtxt(dl / 'blmax_low_ell.dat').astype(int),
                        np.loadtxt(dl / 'bweight_low_ell.dat'), int(np.loadtxt(dl / 'plmin_low_ell.dat')))
            self.X = np.concatenate([Xl, self.X])
            self.bval = np.concatenate([bl, self.bval])
            self.sig = np.concatenate([sl, self.sig])
            F = np.zeros((len(self.X), len(self.X)))
            F[:len(Xl), :len(Xl)] = np.diag(1 / sl ** 2)
            F[len(Xl):, len(Xl):] = fisher
            fisher = F
        self.fisher = fisher

    def binned(self, Dl, ellmin, nbins):
        """The first nbins bins of the plik binning (the same widths and weights for TT, TE and EE; l = 30 + index)."""
        ls = np.arange(len(Dl)) + ellmin
        Cl = Dl / (ls * (ls + 1) / (2 * np.pi))
        out = np.empty(nbins)
        for i in range(nbins):
            lo, hi = self.blmin[i] + 30, self.blmax[i] + 30
            out[i] = np.sum(Cl[lo - ellmin:hi + 1 - ellmin] * self.w[self.blmin[i]:self.blmax[i] + 1])
        return out

    def binned_low(self, Dl, ellmin):
        blmin, blmax, w, plmin = self.low
        ls = np.arange(len(Dl)) + ellmin
        Cl = Dl / (ls * (ls + 1) / (2 * np.pi))
        return np.array([np.sum(Cl[blmin[i] + plmin - ellmin:blmax[i] + plmin + 1 - ellmin] * w[blmin[i]:blmax[i] + 1])
                         for i in range(len(blmin))])

    def chi2(self, Dtt, Dte, Dee, ellmin=2):
        parts = [self.binned(Dtt, ellmin, self.nb['TT'])]
        if self.spectra == 'TTTEEE':
            parts += [self.binned(Dte, ellmin, self.nb['TE']), self.binned(Dee, ellmin, self.nb['EE'])]
        model = np.concatenate(parts)
        if self.low is not None:
            model = np.concatenate([self.binned_low(Dtt, ellmin), model])
        r = model - self.X
        return float(r @ self.fisher @ r)


# ---------------------------------------------------------------- DESI DR2
def desi_chi2(model):
    """model(z) -> (D_M/r_d, D_H/r_d, D_V/r_d); chi^2 with the correlation of D_M and D_H of each tracer."""
    chi2, rows = 0.0, []
    for name, z, m in DESI_DR2:
        DMr, DHr, DVr = model(z)
        if m[0] == 'V':
            c = ((DVr - m[1]) / m[2]) ** 2
            rows.append({'tracer': name, 'z': z, 'DV_rd': [m[1], m[2], DVr]})
        else:
            _, dm, sdm, dh, sdh, rho = m
            C = np.array([[sdm ** 2, rho * sdm * sdh], [rho * sdm * sdh, sdh ** 2]])
            r = np.array([DMr - dm, DHr - dh])
            c = float(r @ np.linalg.solve(C, r))
            rows.append({'tracer': name, 'z': z, 'DM_rd': [dm, sdm, DMr], 'DH_rd': [dh, sdh, DHr]})
        rows[-1]['chi2'] = float(c)
        chi2 += c
    return chi2, rows


REFIT_PARAMS = ('ombh2', 'omch2', 'thetastar', 'lnAs', 'ns')
REFIT_STEPS = {'ombh2': 1e-4, 'omch2': 1e-3, 'thetastar': 2e-6, 'lnAs': 1e-2, 'ns': 4e-3}


def model_vector(lik, cl):
    return lik.binned_low(cl[:, 0][2:2509], 2), lik.binned(cl[2:2509, 0], 2, 215), lik.binned(cl[2:2509, 3], 2, 199), \
        lik.binned(cl[2:2509, 1], 2, 199)


def lik_vector(lik, cl):
    lo, tt, te, ee = model_vector(lik, cl)
    return np.concatenate([lo, tt, te, ee])


def cls_at(x, neff):
    par = {k: v for k, v in zip(REFIT_PARAMS, x) if k != 'thetastar'}
    p = camb_params(neff=neff, thetastar=x[2], par=par)
    import camb
    r = camb.get_results(p)
    return r.get_cmb_power_spectra(p, CMB_unit='muK')['total'], float(p.H0)


def planck_refit(lik, x0, neffs):
    """Gauss-Newton fit of (omega_b, omega_chi, theta*, ln 10^10 A_s, n_s) to the plik-lite TT/TE/EE spectra and the two
    low-l TT bins (tau fixed at the Planck value), with the CAMB Jacobian at the Planck point, for each N_eff."""
    x0 = np.array(x0, float)
    J = np.empty((len(lik.X), len(x0)))
    for j, k in enumerate(REFIT_PARAMS):
        e = np.zeros(len(x0))
        e[j] = REFIT_STEPS[k]
        Xp = lik_vector(lik, cls_at(x0 + e, neffs[0])[0])
        Xm = lik_vector(lik, cls_at(x0 - e, neffs[0])[0])
        J[:, j] = (Xp - Xm) / (2 * REFIT_STEPS[k])
    A = J.T @ lik.fisher @ J
    out = {}
    for neff in neffs:
        x = x0.copy()
        hist = []
        for it in range(3):
            cl, H0 = cls_at(x, neff)
            r = lik_vector(lik, cl) - lik.X
            chi = float(r @ lik.fisher @ r)
            hist.append({'x': x.tolist(), 'H0': H0, 'chi2': chi})
            if it == 2:
                break
            x = x - np.linalg.solve(A, J.T @ lik.fisher @ r)
        best = min(hist, key=lambda d: d['chi2'])
        out['%.3f' % neff] = {'best': best, 'history': hist,
                              'errors_from_fisher': dict(zip(REFIT_PARAMS, np.sqrt(np.diag(np.linalg.inv(A))).tolist()))}
    return out



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {'inputs': {'planck2018': P18, 'neutrino_masses_eV': list(M_NU), 'N_eff': NEFF_SM, 'Delta_N_eff_nuR': DNEFF_NUR,
                      'T_cmb_K': TCMB}}
    h = P18['H0'] / 100

    # ---------------- CAMB: UM-4, UM-4 with thermal nu_R at the same theta*, and Planck's own neutrino convention
    rU, dU, clU = camb_run(camb_params())
    rP, dP, clP = camb_run(camb_params(planck_neutrinos=True))
    rR, dR, clR = camb_run(camb_params(neff=NEFF_SM + DNEFF_NUR, thetastar=dU['thetastar'] / 100))
    out['camb_derived'] = {'UM4': dU, 'UM4_with_thermal_nuR_same_theta': dR, 'Planck_convention_one_massive_nu': dP}
    print('  CAMB: UM-4 %s' % {k: round(v, 5) for k, v in dU.items()}, flush=True)

    # ---------------- C1: background
    bg = Background(h, P18['ombh2'], P18['omch2'])
    zs = np.concatenate([np.linspace(0, 3, 31), np.geomspace(3.5, 1e4, 40)])
    Hc = np.array([rU.hubble_parameter(z) for z in zs])
    Hm = bg.H(zs)
    dev = float(np.max(np.abs(Hm / Hc - 1)))
    age_here = bg.age_Gyr()
    out['C1'] = {'max_rel_dev_H_vs_CAMB': dev, 'z_range': [0, 1e4], 'Omega': {'gamma': bg.Og, 'b': bg.Ob, 'chi': bg.Oc,
                 'nu_today': float(bg.Onu(0.0)), 'Lambda': bg.OL}, 'age_Gyr_here': age_here, 'age_Gyr_CAMB': dU['age']}
    rep.check('C1_background_power_series', dev < 1e-5 and abs(age_here / dU['age'] - 1) < 1e-4,
              'H(z) of FE-59 computed here (Omega_gamma = %.4e, Omega_nu today = %.4e, Omega_b = %.4f, Omega_chi = %.4f, '
              'Omega_Lambda = %.4f) equals CAMB to %.1e for 0 <= z <= 1e4; age %.4f Gyr (CAMB %.4f); with Einstein gravity in '
              'the bulk and the volume of the extra times held fixed the Friedmann equations of the fold are those of general '
              'relativity up to corrections of the relative order (12/25)(H_4/H)^2 (um4_fold.py F5), below 1e-50 after '
              'nucleosynthesis for H >= 2.5 TeV, so the fold expands as in general relativity' % (
                  bg.Og, float(bg.Onu(0.0)), bg.Ob, bg.Oc, bg.OL, dev, age_here, dU['age']))

    # ---------------- C2: BAO ruler
    rs_here = bg.rs(dU['zdrag'])
    dist = []
    for name, z, m in DESI_DR2:
        DMh = bg.DM_simpson(z)
        DMc = float(rU.comoving_radial_distance(z))
        DHh, DHc = C_KMS / float(bg.H(z)), C_KMS / float(rU.hubble_parameter(z))
        dist.append({'z': z, 'DM_here': DMh, 'DM_CAMB': DMc, 'DH_here': DHh, 'DH_CAMB': DHc})
    ddev = max(max(abs(d['DM_here'] / d['DM_CAMB'] - 1), abs(d['DH_here'] / d['DH_CAMB'] - 1)) for d in dist)
    out['C2'] = {'rs_drag_here': rs_here, 'rs_drag_CAMB': dU['rdrag'], 'distances': dist, 'max_rel_dev_distances': ddev}
    rep.check('C2_BAO_ruler', abs(rs_here / dU['rdrag'] - 1) < 1e-4 and ddev < 1e-4,
              'FE-56 integrated here: r_s(z_drag = %.2f) = %.3f Mpc (CAMB %.3f); D_M and D_H at the seven DESI redshifts '
              'agree with CAMB to %.1e' % (dU['zdrag'], rs_here, dU['rdrag'], ddev))

    # ---------------- C3: CMB derived quantities vs Planck 2018
    cmp_ = {}
    for k, (v, s) in P18_DERIVED.items():
        cmp_[k] = {'UM4': dU[k], 'Planck2018': v, 'sigma': s, 'pull': (dU[k] - v) / s}
    out['C3'] = cmp_
    rep.check('C3_CMB_derived_vs_Planck', all(abs(c['pull']) < 1 for c in cmp_.values()),
              'UM-4 with the Planck 2018 parameters: %s (pulls in units of the Planck errors, all below 1)' % (
                  ', '.join('%s %.5g (Planck %.5g +- %.2g, %+.2f)' % (k, c['UM4'], c['Planck2018'], c['sigma'], c['pull'])
                            for k, c in cmp_.items())))

    # ---------------- C4: Planck 2018 high-l spectra
    c4 = {}
    try:
        data = fetch_planck()
        ref = np.genfromtxt(data / 'Dl_planck2015fit.dat', unpack=True)
        lref = int(ref[0][0])
        tt_hi = PlikLite(data, 'TT', False)
        all_lo = PlikLite(data, 'TTTEEE', True)
        val = {'TT_high_l': -0.5 * tt_hi.chi2(ref[1], ref[2], ref[3], lref), 'TTTEEE_with_low_l_bins': -0.5 * all_lo.chi2(
            ref[1], ref[2], ref[3], lref)}
        expected = {'TT_high_l': -101.58123068722583, 'TTTEEE_with_low_l_bins': -293.95586501795134}
        hi = PlikLite(data, 'TTTEEE', False)
        res = {}
        for name, cl in (('UM4', clU), ('UM4_with_thermal_nuR_same_theta', clR), ('Planck_convention', clP)):
            Dtt, Dee, Dte = cl[2:2509, 0], cl[2:2509, 1], cl[2:2509, 3]
            res[name] = {'chi2_TTTEEE_high_l': hi.chi2(Dtt, Dte, Dee, 2), 'chi2_TT_high_l': tt_hi.chi2(Dtt, Dte, Dee, 2),
                         'chi2_TTTEEE_with_low_l_bins': all_lo.chi2(Dtt, Dte, Dee, 2)}
        nbin = len(hi.X)
        fit = planck_refit(all_lo, [P18['ombh2'], P18['omch2'], dU['thetastar'] / 100, P18['lnAs'], P18['ns']],
                           [NEFF_SM, NEFF_SM + DNEFF_NUR])
        c4 = {'validation_loglike': val, 'expected_loglike': expected, 'results': res, 'n_bins_high_l': nbin,
              'refit_TTTEEE_with_low_l_bins': fit,
              'data': 'Planck 2018 plik-lite v22 (Planck Legacy Archive) via github.com/heatherprince/planck-lite-py'}
        fU, fR = fit['%.3f' % NEFF_SM]['best'], fit['%.3f' % (NEFF_SM + DNEFF_NUR)]['best']
        dchi_fit = fR['chi2'] - fU['chi2']
        okv = all(abs(val[k] - expected[k]) < 1e-6 for k in expected)
        chiU = res['UM4']['chi2_TTTEEE_high_l']
        dchi = res['UM4_with_thermal_nuR_same_theta']['chi2_TTTEEE_high_l'] - chiU
        ok4 = okv and abs(chiU - nbin) < 3 * math.sqrt(2 * nbin)
        detail = ('the implementation reproduces the plik-lite reference log-likelihoods %s (expected %s); UM-4: chi^2 = %.1f for '
                  '%d high-l TT/TE/EE bins (expected %d +- %.0f), TT alone %.1f for 215 bins; UM-4 with three thermal nu_R '
                  '(N_eff = %.3f) at the same theta* and the same other parameters: Delta chi^2 = %+.1f (the damping tail); '
                  'with omega_b, omega_chi, theta*, A_s and n_s refitted (tau fixed) to the high-l spectra and the two low-l TT '
                  'bins: chi^2 = %.1f (N_eff = %.3f, H0 = %.2f) and %.1f (N_eff = %.3f, H0 = %.2f), Delta chi^2 = %+.1f' % (
                      {k: round(v, 6) for k, v in val.items()}, expected, chiU, nbin, nbin, math.sqrt(2 * nbin),
                      res['UM4']['chi2_TT_high_l'], NEFF_SM + DNEFF_NUR, dchi, fU['chi2'], NEFF_SM, fU['H0'], fR['chi2'],
                      NEFF_SM + DNEFF_NUR, fR['H0'], dchi_fit))
    except Exception as exc:                                     # no network and no cached data
        ok4 = False
        detail = 'the Planck 2018 plik-lite data are not available (%s)' % exc
    out['C4'] = c4
    rep.check('C4_CMB_spectra_vs_Planck_high_l', ok4, detail)

    # ---------------- C5: DESI DR2
    def model_from(bgx, rd):
        def m(z):
            DM = bgx.DM_simpson(z)
            DH = C_KMS / float(bgx.H(z))
            return DM / rd, DH / rd, (z * DM * DM * DH) ** (1 / 3) / rd
        return m
    chiP, rowsP = desi_chi2(model_from(bg, dU['rdrag']))
    # DESI alone: Omega_m and h r_d (the radiation and neutrinos of UM-4 kept, the baryon fraction of Planck)
    fb = P18['ombh2'] / (P18['ombh2'] + P18['omch2'])

    def chi_fit(x):
        Om, hrd = x
        if not (0.05 < Om < 0.8 and 50 < hrd < 150):
            return 1e9
        b = Background(h, Om * h * h * fb, Om * h * h * (1 - fb) - 0.0)
        b.Oc = Om - b.Ob - float(b.Onu(0.0))
        b.OL = 1 - b.Og - b.Ob - b.Oc - float(b.Onu(0.0))
        return desi_chi2(model_from(b, hrd / h))[0]
    fit = minimize(chi_fit, x0=[0.30, 100.0], method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-8, 'maxiter': 4000})
    Om_fit, hrd_fit = fit.x
    Om_P = bg.Ob + bg.Oc + float(bg.Onu(0.0))
    dchi_P = chiP - fit.fun
    # significance of Delta chi^2 for 2 parameters
    p2 = math.exp(-dchi_P / 2)
    from scipy.stats import norm, chi2 as chi2dist
    sig_P = float(norm.isf(p2 / 2)) if p2 > 0 else float('inf')
    out['C5'] = {'chi2_UM4_planck_parameters': chiP, 'rows': rowsP, 'n_data': 13,
                 'fit_DESI_alone': {'Omega_m': Om_fit, 'h_rd_Mpc': hrd_fit, 'chi2_min': float(fit.fun),
                                    'p_value': float(chi2dist.sf(fit.fun, 11))},
                 'UM4_planck': {'Omega_m': Om_P, 'h_rd_Mpc': h * dU['rdrag']},
                 'Delta_chi2_planck_fixed_vs_DESI_best': dchi_P, 'equivalent_gaussian_sigma_2dof_planck_fixed': sig_P}
    rep.check('C5_BAO_vs_DESI_DR2', fit.success and chi2dist.sf(fit.fun, 11) > 0.01,
              'UM-4 with the Planck parameters (Omega_m = %.4f, h r_d = %.2f Mpc): chi^2 = %.1f for the 13 DESI DR2 '
              'measurements; fitted to DESI alone: Omega_m = %.4f, h r_d = %.2f Mpc, chi^2 = %.1f for 11 degrees of freedom '
              '(p = %.2f; DESI DR2 finds the same for the cosmological-constant model); the Planck point lies Delta chi^2 = %.1f '
              'above the DESI optimum when its own errors are neglected (with the CMB errors DESI DR2 quotes a 2.3 sigma '
              'tension between BAO and CMB): UM-4 has the w = -1 of a vacuum energy (FE-59) exactly, inherits this '
              'tension, and cannot produce the w0 > -1, wa < 0 that DESI DR2 + CMB prefer at 3.1 sigma' % (
                  Om_P, h * dU['rdrag'], chiP, Om_fit, hrd_fit, fit.fun, chi2dist.sf(fit.fun, 11), dchi_P))

    # ---------------- C6: the CNB
    Tnu0 = (4 / 11) ** (1 / 3) * TCMB
    kT = KB * Tnu0 / EV
    n_flav = 3 * ZETA3 / (2 * math.pi ** 2) * (kT / 1.97327e-5) ** 3          # cm^-3, FE-53
    states = []
    for i, m in enumerate(M_NU):
        z_nr = m / (3.15 * kT) - 1 if m > 0 else None
        states.append({'state': i + 1, 'mass_eV': m, 'z_nonrelativistic': z_nr, 'relativistic_today': m < 3.15 * kT})
    Onuh2 = sum(M_NU) / 93.14
    Onuh2_massive = (float(bg.Onu(0.0)) - bg.Onu_rel) * h * h                    # the two massive states
    s12, s13 = 0.303, 0.02203                       # sin^2 theta12, sin^2 theta13 of NuFIT 5.2 (as in um4_flavour.py)
    U = np.array([(1 - s12) * (1 - s13), s12 * (1 - s13), s13])                  # |U_e1|^2, |U_e2|^2, |U_e3|^2
    rate_nr = N_TRITIUM_100G * SIGMA_BAR_CM2 * C_SI * 100 * (n_flav / 2) * 3.15576e7      # per year, all states NR, Dirac
    # the mean speed of each mass state today over the redshifted relativistic Fermi-Dirac distribution of the momenta,
    # s_i = <p/E>; the left-handed helicity of a state of speed s is captured (1 + s) times as often as at rest (the helicity
    # factor 1 - 2 h s of the capture cross-section, h = -1/2)
    pgrid = np.linspace(1e-6, 40.0, 400001) * kT
    wfd = pgrid ** 2 / (np.exp(pgrid / kT) + 1.0)
    speeds = [float(np.trapezoid(wfd * pgrid / np.sqrt(pgrid ** 2 + m * m), pgrid) / np.trapezoid(wfd, pgrid)) for m in M_NU]
    for st, sp in zip(states, speeds):
        st['mean_speed_today'] = sp
    rate_um4 = rate_nr * float(np.sum(U * (1.0 + np.array(speeds))))      # nu_1 massless (speed 1), nu_2 and nu_3 slow
    out['C6'] = {'T_nu0_K': Tnu0, 'kT_nu0_eV': kT, 'n_per_flavour_cm3': n_flav, 'n_total_cm3': 3 * n_flav,
                 'n_per_helicity_state_cm3': n_flav / 2, 'states': states, 'Omega_nu_h2_FE58': Onuh2,
                 'Omega_nu_h2_massive_states_here': Onuh2_massive, 'Omega_nu_h2_CAMB': float(rU.Params.omnuh2),
                 'capture_rate_per_year_100g_Dirac_nonrelativistic': rate_nr,
                 'capture_rate_per_year_100g_Majorana_nonrelativistic': 2 * rate_nr,
                 'capture_rate_per_year_100g_UM4_massless_nu1': rate_um4, '|U_ei|^2': U.tolist()}
    rep.check('C6_cosmic_neutrino_background', abs(Tnu0 - 1.9454) < 1e-3 and abs(n_flav - 112.0) < 0.5
              and abs(Onuh2_massive / Onuh2 - 1) < 0.01 and abs(rate_nr - 4.0) < 0.3 and abs(speeds[0] - 1) < 1e-9
              and 0 < speeds[2] < speeds[1] < 0.1,
              'T_nu = (4/11)^{1/3} T_gamma = %.4f K (%.3e eV); %.1f neutrinos and antineutrinos per cm^3 per flavour (%.0f in all, '
              'FE-53); m = 0, %.2f meV, %.1f meV: nu_2 and nu_3 became non-relativistic at z = %.1f and %.0f, nu_1 is '
              'relativistic; Omega_nu h^2 = %.3e (FE-58: Sum m/93.14 eV = %.3e, CAMB %.3e); the right-handed states are not '
              'populated, so the CNB of UM-4 has one helicity per state and the capture rate on tritium is %.1f per year per '
              '100 g for non-relativistic Dirac neutrinos (Long, Lunardini and Sabancilar: about 4; Majorana about 8), %.2f '
              'with the massless nu_1 and the mean speeds %.4f and %.4f of nu_2 and nu_3 today' % (
                  Tnu0, kT, n_flav, 3 * n_flav, 1e3 * M_NU[1], 1e3 * M_NU[2], states[1]['z_nonrelativistic'],
                  states[2]['z_nonrelativistic'], Onuh2_massive, Onuh2, float(rU.Params.omnuh2), rate_nr, rate_um4,
                  speeds[1], speeds[2]))

    # ---------------- spectra and plot
    ls = np.arange(2, 2509)
    table = np.column_stack([ls, clU[2:2509, 0], clU[2:2509, 3], clU[2:2509, 1], clR[2:2509, 0], clR[2:2509, 3], clR[2:2509, 1]])
    np.savetxt(UM4 / 'outputs' / 'cmb_spectra.csv', table, delimiter=',', fmt=['%d'] + ['%.6e'] * 6,
               header='l,DTT_UM4,DTE_UM4,DEE_UM4,DTT_UM4_nuR,DTE_UM4_nuR,DEE_UM4_nuR (D_l = l(l+1)C_l/2pi in muK^2, lensed)')
    try:
        plot_spectra(ls, clU, clR, c4)
    except Exception as exc:
        print('  plot skipped: %s' % exc)

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM4 / 'outputs' / 'cosmology.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=float) + '\n')
    report = {'script': 'universe_model_4/code/um4_cosmology.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM4 / 'reports' / 'cosmology_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


def plot_spectra(ls, clU, clR, c4):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    data = None
    if c4:
        d = EXT / 'data' / 'planck2018_plik_lite'
        bval, X, sig = np.genfromtxt(d / 'cl_cmb_plik_v22.dat', unpack=True)
        data = (bval, X, sig)
    fig, ax = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
    names = [('TT', 0, 0, 215), ('TE', 3, 215, 414), ('EE', 1, 414, 613)]
    for k, (nm, col, a, b) in enumerate(names):
        ax[k].plot(ls, clU[2:2509, col], color='#1f4e79', lw=1.2, label='UM-4 (N_eff = 3.044)')
        ax[k].plot(ls, clR[2:2509, col], color='#c55a11', lw=0.9, ls='--', label='UM-4 with thermal nu_R (N_eff = 3.185)')
        if data is not None:
            bl = data[0][a:b]
            f = bl * (bl + 1) / (2 * np.pi)
            ax[k].errorbar(bl, data[1][a:b] * f, yerr=data[2][a:b] * f, fmt='.', ms=2, color='0.35', elinewidth=0.6,
                           label='Planck 2018 plik-lite')
        ax[k].set_ylabel(r'$D_\ell^{\mathrm{%s}}$ [$\mu$K$^2$]' % nm)
        ax[k].grid(alpha=0.3)
    ax[0].legend(fontsize=8)
    ax[2].set_xlabel(r'multipole $\ell$')
    fig.suptitle('CMB spectra of UM-4 (Planck 2018 parameters)')
    fig.tight_layout()
    fig.savefig(UM4 / 'outputs' / 'cmb_spectra.png', dpi=130)
    plt.close(fig)


if __name__ == '__main__':
    sys.exit(main())
