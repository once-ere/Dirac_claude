#!/usr/bin/env python3
"""um3_neutrino.py - the flavour evolution of the three Dirac neutrinos of UM-3 (FIELD_EQUATIONS.md, FE-48 to FE-53).

The neutrinos live on the fold with the flavour structure of the Standard Model (three Dirac neutrinos, U_PMNS); the
action of UM-3 adds two things: the flavour-blind potential V_Psi of the current portal (FE-49) and the local value
v_loc of the Higgs field, which the Higgs portal and the ad hoc vacuum can change (all masses scale with v_loc/v, the
Fermi constant with (v/v_loc)^2).  Computed and checked:
  N1  (FE-48, FE-49) a potential proportional to the unit matrix leaves the flavour evolution unchanged (exact, with a
      random Hamiltonian); rescaling v -> v_loc in the Yukawa mass matrices leaves |U_PMNS| and the Jarlskog invariant
      unchanged and scales every mass by v_loc/v; the resonance density scales as (v_loc/v)^4; the shift of v_loc by
      the local dark matter, Delta v^2/v^2 = g_hchi rho_chi/(lambda v^3 omega_b), is of order 1e-50;
  N2  (FE-50) the mixing angle in matter from the exact diagonalisation of the two-flavour Hamiltonian equals the
      formula; theta_m = 45 degrees at the resonance density; the Landau-Zener probability equals the jump probability
      from an exact integration of the Schroedinger equation through a linear density profile;
  N3  (FE-51) the fast flavour instability: for axially symmetric electron-lepton-number distributions without an
      angular crossing every eigenfrequency of the linearised equations (azimuthal modes m = 0 and 1) is real (the
      matrix is similar to a symmetric one); with a crossing an exponentially growing mode exists; the growth rate is
      converged in the number of angular nodes;
  N4  (FE-52) the equipartition map conserves the electron lepton number and the numbers of neutrinos and
      antineutrinos exactly, keeps every occupation number in [0, 1], and equilibrates the less abundant of nu_e and
      anti-nu_e with the heavy-lepton flavours whenever the Pauli bound is inactive;
  N5  (FE-53, FE-58, FE-62) the CNB today: T_nu = (4/11)^(1/3) T_gamma, n_nu = 3 zeta(3)/(2 pi^2) T_nu^3 per flavour,
      N_eff = 3 for instantaneous decoupling, the density parameter of massive neutrinos, Delta N_eff of three
      right-handed neutrinos that decouple above the electroweak scale.
Writes outputs/neutrino.json and reports/neutrino_checks.json.
Usage: python universe_model_3/code/um3_neutrino.py

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

import numpy as np
import scipy.linalg as sla
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

# constants (PDG 2024 values; natural units hbar = c = 1)
HBARC_GEV_CM = 1.973269804e-14       # GeV cm
KB_GEV_PER_K = 8.617333262e-14       # GeV / K
GF = 1.1663788e-5                    # GeV^-2
V_EW = (math.sqrt(2.0) * GF) ** -0.5  # 246.22 GeV
MH = 125.25                          # GeV
LAMBDA_H = MH ** 2 / (2.0 * V_EW ** 2)
T_GAMMA0_K = 2.7255                  # K
ZETA3 = 1.2020569031595942
RHO_C_OVER_H2_GEV_CM3 = 1.05375e-5   # GeV / cm^3


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def random_hermitian(rng, n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2


def evolve(H, rho0, t):
    U = sla.expm(-1j * H * t)
    return U @ rho0 @ U.conj().T


def pmns_from_yukawas(Ye, Ynu, v):
    """(v/sqrt 2) Y = U_L diag(m) U_R^dagger (singular value decomposition, masses ascending); U_PMNS = U_eL^dagger U_nuL."""
    def left(Y):
        U, m, Vh = np.linalg.svd(v / math.sqrt(2.0) * Y)
        order = np.argsort(m)
        return U[:, order], m[order]
    UeL, me = left(Ye)
    UnL, mn = left(Ynu)
    return UeL.conj().T @ UnL, me, mn


def jarlskog(U):
    return float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))


def two_flavour_h(Delta, th, V):
    """Two-flavour Hamiltonian (traceless part) in the flavour basis (e, x): vacuum term Delta = dm^2/(2E), the
    charged-current potential V in the electron flavour."""
    c, s = math.cos(2 * th), math.sin(2 * th)
    return np.array([[(-Delta * c + V) / 2, Delta * s / 2], [Delta * s / 2, (Delta * c - V) / 2]])


def jump_probability(Delta, th, Vp, L):
    """Exact integration of i d psi/dr = H(r) psi through the linear profile V = V_res + Vp r, r in [-L, L], starting in
    the upper eigenstate of matter; returns the probability of ending in the lower one (the jump)."""
    Vres = Delta * math.cos(2 * th)

    def rhs(r, y):
        p = y[:2] + 1j * y[2:]
        dp = -1j * two_flavour_h(Delta, th, Vres + Vp * r) @ p
        return np.concatenate([dp.real, dp.imag])
    _, U0 = np.linalg.eigh(two_flavour_h(Delta, th, Vres - Vp * L))
    psi0 = U0[:, 1].astype(complex)
    sol = solve_ivp(rhs, (-L, L), np.concatenate([psi0.real, psi0.imag]), rtol=1e-10, atol=1e-12, method='DOP853')
    p = sol.y[:2, -1] + 1j * sol.y[2:, -1]
    _, U1 = np.linalg.eigh(two_flavour_h(Delta, th, Vres + Vp * L))
    return 1.0 - abs(np.vdot(U1[:, 1], p)) ** 2


def ffi_growth(G, mu, w, Ks, m):
    """Largest imaginary part of the eigenfrequencies of the linearised fast-flavour equations (FE-51) for an axially
    symmetric ELN distribution G(mu), wave vector K along the axis, azimuthal mode m (0 or 1):
        Omega Q_i = K mu_i Q_i - sum_j w_j G_j k_m(i, j) Q_j,
        k_0 = 2 pi (1 - mu_i mu_j),  k_1 = -pi sqrt(1 - mu_i^2) sqrt(1 - mu_j^2)."""
    s = np.sqrt(1 - mu ** 2)
    best, arg = 0.0, None
    for K in Ks:
        if m == 0:
            A = K * np.diag(mu) - 2 * np.pi * (w * G)[None, :] * (1 - np.outer(mu, mu))
        else:
            A = K * np.diag(mu) + np.pi * (w * G)[None, :] * np.outer(s, s)
        g = float(np.linalg.eigvals(A).imag.max())
        if g > best:
            best, arg = g, float(K)
    return best, arg


def equipartition(Fe, Fb, Fx):
    """FE-52: the flavour equipartition with conservation of the electron lepton number and of the numbers of neutrinos
    and antineutrinos, the four heavy-lepton species equal, and the Pauli bound."""
    delta = np.maximum(2.0 / 3.0 * (np.minimum(Fe, Fb) - Fx), np.maximum(Fe, Fb) - 1.0)
    return Fe - delta, Fb - delta, Fx + delta / 2.0, delta



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {'constants': {'G_F': GF, 'v': V_EW, 'lambda': LAMBDA_H, 'T_gamma0_K': T_GAMMA0_K}}
    rng = np.random.default_rng(20261024)

    # ---------------- N1: flavour blindness of V_Psi; invariance of the mixing under v_loc
    H = random_hermitian(rng, 3)
    rho0 = random_hermitian(rng, 3)
    rho0 = rho0 @ rho0  # a positive matrix
    dev = max(np.abs(evolve(H + Vs * np.eye(3), rho0, t) - evolve(H, rho0, t)).max()
              for Vs in (0.3, -2.0, 17.0) for t in (0.5, 3.0, 40.0))
    Ye = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    Ynu = 1e-12 * (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
    U1, me1, mn1 = pmns_from_yukawas(Ye, Ynu, V_EW)
    vloc = 1.37 * V_EW
    U2, me2, mn2 = pmns_from_yukawas(Ye, Ynu, vloc)
    dU = float(np.abs(np.abs(U1) - np.abs(U2)).max())
    dJ = abs(jarlskog(U1) - jarlskog(U2))
    ratio = np.concatenate([me2 / me1, mn2 / mn1])
    dm2, E, th = 2.5e-21, 1e-2, 0.15        # GeV^2, GeV (10 MeV), rad
    nres = lambda dm2_, GF_: dm2_ * math.cos(2 * th) / (2 * math.sqrt(2.0) * GF_ * E)
    scale = nres(dm2 * (vloc / V_EW) ** 2, GF * (V_EW / vloc) ** 2) / nres(dm2, GF)
    rho_chi = 0.3 * HBARC_GEV_CM ** 3        # 0.3 GeV/cm^3 in GeV^4
    shift = rho_chi / (LAMBDA_H * V_EW ** 3 * 100.0)   # per unit g_hchi, omega_b = 100 GeV
    out['N1'] = {'max_deviation_with_V_Psi': float(dev), 'max_delta_abs_U': dU, 'delta_Jarlskog': dJ,
                 'mass_ratios': ratio.tolist(), 'resonance_density_scale': scale, 'expected_scale': (vloc / V_EW) ** 4,
                 'dv2_over_v2_per_g_hchi': shift}
    rep.check('N1_flavour_blindness_and_v_loc',
              dev < 1e-10 and dU < 1e-12 and dJ < 1e-12 and np.allclose(ratio, vloc / V_EW, rtol=1e-12)
              and abs(scale / (vloc / V_EW) ** 4 - 1) < 1e-12 and 1e-51 < shift < 1e-49,
              'V_Psi * 1 changes rho(t) by at most %.1e (exact: it commutes); v -> 1.37 v leaves |U_PMNS| (max change %.1e) and '
              'the Jarlskog invariant (change %.1e) unchanged and scales all six masses by %.6f; resonance density scales by %.6f '
              '= (v_loc/v)^4; Delta v^2/v^2 = %.2e g_hchi for 0.3 GeV/cm^3 and omega_b = 100 GeV' % (
                  dev, dU, dJ, float(ratio.mean()), scale, shift))

    # ---------------- N2: matter-enhanced conversion
    Delta = dm2 / (2 * E)
    err_angle = 0.0
    for V in np.linspace(0.0, 3.0 * Delta, 13):
        e, U = np.linalg.eigh(two_flavour_h(Delta, th, V))
        # the heavier eigenstate (column 1) is (sin theta_m, cos theta_m) in (e, x) up to sign
        thm_num = math.atan2(abs(U[0, 1]), abs(U[1, 1]))
        thm_formula = 0.5 * math.atan2(math.sin(2 * th), math.cos(2 * th) - V / Delta)
        err_angle = max(err_angle, abs(thm_num - thm_formula))
    Vres = Delta * math.cos(2 * th)
    e, U = np.linalg.eigh(two_flavour_h(Delta, th, Vres))
    thm_res = math.degrees(math.atan2(abs(U[0, 1]), abs(U[1, 1])))
    lz = []
    for (D_, th_, Vp_) in [(1.0, 0.15, 0.05), (1.0, 0.1, 0.02), (2.0, 0.3, 0.5)]:
        gam = D_ ** 2 * math.sin(2 * th_) ** 2 / abs(Vp_)
        # FE-50 form: gamma = dm^2 sin^2 2theta / (2E cos 2theta) * |d ln n_e/dr|^-1 at the resonance
        gam_fe50 = D_ * math.sin(2 * th_) ** 2 / math.cos(2 * th_) * (D_ * math.cos(2 * th_)) / abs(Vp_)
        P = math.exp(-math.pi / 2 * gam_fe50)
        Pnum = jump_probability(D_, th_, Vp_, 400 * D_ * math.sin(2 * th_) / Vp_)
        lz.append({'Delta': D_, 'theta': th_, 'dV/dr': Vp_, 'gamma': gam, 'P_LZ': P, 'P_numeric': Pnum})
    out['N2'] = {'max_error_matter_angle_rad': err_angle, 'theta_m_at_resonance_deg': thm_res, 'landau_zener': lz}
    rep.check('N2_msw_and_landau_zener',
              err_angle < 1e-12 and abs(thm_res - 45.0) < 1e-9 and all(abs(x['P_numeric'] / x['P_LZ'] - 1) < 1e-4 for x in lz),
              'tan 2theta_m formula vs exact diagonalisation: max error %.1e rad; theta_m = %.9f deg at n_e,res; Landau-Zener '
              'vs exact integration through a linear profile: %s' % (
                  err_angle, thm_res, ', '.join('%.6f/%.6f' % (x['P_LZ'], x['P_numeric']) for x in lz)))

    # ---------------- N3: the crossing criterion of the fast instability
    Ks = np.linspace(-3, 3, 241)
    dists = {'no crossing, forward nu_e excess': lambda mu: 1.0 + 0.6 * mu,
             'no crossing, peaked': lambda mu: 0.3 * np.exp(2 * mu),
             'no crossing, anti-nu_e excess': lambda mu: -(0.5 + 0.4 * mu ** 2),
             'crossing, linear': lambda mu: mu - 0.3,
             'crossing, forward peak': lambda mu: 2.0 * np.exp(3 * (mu - 1)) - 0.15,
             'crossing, nu_e vs anti-nu_e': lambda mu: 0.6 * np.exp(2 * (mu - 1)) - 0.5 * np.exp(1.2 * (mu - 1))}
    res = []
    for nn in (80, 160):
        mu, w = np.polynomial.legendre.leggauss(nn)
        for name, f in dists.items():
            G = f(mu)
            g0, k0 = ffi_growth(G, mu, w, Ks, 0)
            g1, k1 = ffi_growth(G, mu, w, Ks, 1)
            res.append({'nodes': nn, 'distribution': name, 'crossing': bool(G.max() > 0 > G.min()),
                        'growth_m0': g0, 'K_m0': k0, 'growth_m1': g1, 'K_m1': k1})
    ok_no = all(max(r['growth_m0'], r['growth_m1']) < 1e-10 for r in res if not r['crossing'])
    ok_yes = all(max(r['growth_m0'], r['growth_m1']) > 1e-2 for r in res if r['crossing'])
    conv = []
    for name in dists:
        a = [r for r in res if r['distribution'] == name and r['nodes'] == 80][0]
        b = [r for r in res if r['distribution'] == name and r['nodes'] == 160][0]
        if a['crossing']:
            conv.append(abs(max(a['growth_m0'], a['growth_m1']) / max(b['growth_m0'], b['growth_m1']) - 1))
    out['N3'] = res
    rep.check('N3_fast_instability_crossing', ok_no and ok_yes and max(conv) < 1e-2,
              'without an angular crossing all eigenfrequencies are real (max imaginary part %.1e); with a crossing the growth '
              'rates are %s (units of the ELN scale); change from 80 to 160 angular nodes at most %.1e' % (
                  max(max(r['growth_m0'], r['growth_m1']) for r in res if not r['crossing']),
                  ', '.join('%.3f' % max(r['growth_m0'], r['growth_m1']) for r in res if r['crossing'] and r['nodes'] == 160),
                  max(conv)))

    # ---------------- N4: the equipartition map FE-52
    F = rng.uniform(0, 1, size=(3, 200000))
    Fe, Fb, Fx = F
    Fe2, Fb2, Fx2, d = equipartition(Fe, Fb, Fx)
    eln = np.abs((Fe2 - Fb2) - (Fe - Fb)).max()
    nnu = np.abs((Fe2 + 2 * Fx2) - (Fe + 2 * Fx)).max()
    nnb = np.abs((Fb2 + 2 * Fx2) - (Fb + 2 * Fx)).max()
    inside = bool(((Fe2 >= -1e-15) & (Fe2 <= 1 + 1e-15) & (Fb2 >= -1e-15) & (Fb2 <= 1 + 1e-15)
                   & (Fx2 >= -1e-15) & (Fx2 <= 1 + 1e-15)).all())
    free = 2.0 / 3.0 * (np.minimum(Fe, Fb) - Fx) >= np.maximum(Fe, Fb) - 1.0
    less = np.where(Fe <= Fb, Fe2, Fb2)
    equi = float(np.abs(less[free] - Fx2[free]).max())
    out['N4'] = {'samples': int(F.shape[1]), 'max_change_ELN': float(eln), 'max_change_number_nu': float(nnu),
                 'max_change_number_nubar': float(nnb), 'all_in_unit_interval': inside,
                 'fraction_pauli_bound_active': float(1 - free.mean()), 'max_equipartition_error': equi}
    rep.check('N4_equipartition_conservation', max(eln, nnu, nnb) < 1e-14 and inside and equi < 1e-14,
              '%d random (F_e, Fbar_e, F_x) in [0,1]^3: ELN, number of nu and of anti-nu conserved to %.1e; every occupation in '
              '[0, 1]; the less abundant of nu_e, anti-nu_e equals the heavy flavours (error %.1e) where the Pauli bound is '
              'inactive (it is active in %.1f%% of the samples)' % (F.shape[1], max(eln, nnu, nnb), equi, 100 * (1 - free.mean())))

    # ---------------- N5: the CNB
    Tnu0 = (4.0 / 11.0) ** (1.0 / 3.0) * T_GAMMA0_K
    T_cm = Tnu0 * KB_GEV_PER_K / HBARC_GEV_CM          # 1/cm
    n_nu = 3 * ZETA3 / (2 * math.pi ** 2) * T_cm ** 3  # per flavour, nu + anti-nu
    Neff_inst = 8 / 7 * (11 / 4) ** (4 / 3) * (3 * 7 / 8 * (4 / 11) ** (4 / 3))
    denom_inst = RHO_C_OVER_H2_GEV_CM3 * 1e9 / n_nu     # eV: Omega_nu h^2 = sum m / denom
    dNeff_ew = 3 * (10.75 / 106.75) ** (4 / 3)
    out['N5'] = {'T_nu0_K': Tnu0, 'n_nu0_per_cm3_per_flavour': n_nu, 'N_eff_instantaneous': Neff_inst,
                 'Omega_nu_h2_denominator_instantaneous_eV': denom_inst, 'Omega_nu_h2_denominator_used_eV': 93.14,
                 'Delta_N_eff_nuR_decoupled_above_EW': dNeff_ew}
    rep.check('N5_cnb', abs(Tnu0 - 1.9454) < 1e-3 and abs(n_nu - 112.0) < 0.5 and abs(Neff_inst - 3) < 1e-12
              and 0.005 < denom_inst / 93.14 - 1 < 0.015 and abs(dNeff_ew - 0.141) < 0.002,
              'T_nu0 = %.4f K; n_nu0 = %.2f /cm^3 per flavour; N_eff = %.3f for instantaneous decoupling; Omega_nu h^2 = sum m/(%.2f eV) '
              'for instantaneous decoupling, 1.0%% above the 93.14 eV that includes the non-thermal heating of the neutrinos; '
              'Delta N_eff = %.3f for three nu_R decoupling above the electroweak scale' % (Tnu0, n_nu, Neff_inst, denom_inst, dNeff_ew))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'neutrino.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_neutrino.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'neutrino_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
