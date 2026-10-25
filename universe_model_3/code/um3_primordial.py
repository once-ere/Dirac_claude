#!/usr/bin/env python3
"""um3_primordial.py - the primordial era of UM-3 with the corrected Lovelock weights w = (1, 1/20, 1/360),
Lambda = -7 H^2 (the author's order of 2026-10-25 07:55), and the record of the author's vacuum.

With the corrected weights the bulk is a vacuum for frozen extra times and any a4(x4), and the fold obeys the Friedmann
equations of general relativity exactly (um3_fold.py J7, um3_series.py SR4): the primordial era is whatever the fields of
the fold make of it.  The author's vacuum a4 = H x4, b4 = b0, the primordial era of the earlier version, is no longer a
solution.  A field of the fold has the action (four-dimensional normalisation)
    S = int d^4x sqrt(-h) Z [ -(1/2) h^{mu nu} d_mu phi d_nu phi - (1/2) m^2 phi^2 ],
    h_{mu nu} = diag(e^{2 a4}, e^{2 a4}, e^{2 a4}, -1),  sqrt(-h) = e^{3 a4},  Z = V_t (e^{-a4} b4)^3 / V_*,
(V_t the coordinate volume of the extra times, V_* their physical volume in the late universe) and its Fourier mode
phi_k(x4) obeys (sqrt(-h) Z phi_k')' / (sqrt(-h) Z) + (k^2 e^{-2 a4} + m^2) phi_k = 0.
Checks:
  PR0  the author's vacuum (A = a4'/H = 1, U = b4'/(H b4) = 0) is not a solution of the corrected bulk equations: it
       would need the bulk source kappa T/H^2 = (-7/5, -7/5, 1, -7/5, 0) (sigma, ordinary space, time, extra times, flux),
       kappa rho_bulk = -H^2 (outputs of um3_geometry.py);
  PR1  record: in the author's vacuum sqrt(-h) Z = V_t b0^3/V_* is constant: the fields of the fold feel no Hubble
       friction (sympy);
  PR2  record: the massless mode equation phi'' + k^2 e^{-2 H x4} phi = 0 is Bessel's equation of order 0 in k tau,
       tau = e^{-H x4}/H; with the canonical normalisation phi_k = sqrt(pi/(4H)) H_0^(1)(k tau), and at late times
       |phi_k|^2 = (pi/(4H)) [1 + (4/pi^2) L^2], L = ln(k tau/2) + gamma_E: the spectral index of k^3 |phi_k|^2 is
       n_S - 1 = 3 + (8/pi^2) L/(1 + 4 L^2/pi^2), not a power law, at least 3 - 2/pi = 2.363 (Planck: n_s - 1 = -0.035);
  PR3  record: the gauge couplings of the fold, g^2/Z, grow like e^{3 H x4} in the author's vacuum;
  PR4  with the corrected weights and the volume of the extra times held fixed (Z constant; the fold fluid supplies the
       pressure along the extra times, IN-10) an era of nearly exponential expansion of the fold is the inflation of
       general relativity, driven by a field of the fold; the bound on primordial gravitational waves, r < 0.032 (95 per
       cent; Planck PR4 with BICEP/Keck 2018 and BAO, Tristram et al. 2022), with A_s = 2.1e-9 limits its Hubble rate to
       H_inf < pi M_Pl,red sqrt(r A_s/2) = 4.4e13 GeV; during it the fold fluid must add the pressure
       -rho_v (1 + A^2/4) along the extra times (A = H_inf/H): with H at most 4.6e-13 GeV (the bound of um3_superluminal.py
       SL5 if the loops make electrons faster) and H_inf at its bound, A is at least 1e26, so the pressure is at least
       about 2e51 rho_v and 1e103 times the tension of the fold fluid (the ratio to the tension is about A^4/8 and grows
       without limit as H gets smaller), and after inflation A = H_4/H > 1 above T ~ 0.6 TeV; what supplies it is OPEN;
  PR5  ESTIMATE, an extension outside the action of UM-3 (the non-minimal coupling -xi_H R_fold Phi^dagger Phi of the
       Higgs doublet to the curvature of the fold is not a term of IN-11): Higgs inflation is possible now that the fold
       has its own Einstein-Hilbert term (the induced gravity, which required xi_H < 1/6, is not needed):
       xi_H = N sqrt(lambda/(72 pi^2 A_s)) = 1.6e4 for lambda = m_H^2/(2 v^2)
       = 0.129 and N = 55 (4.5e3 for the value lambda = 0.01 that the running gives near the inflationary scale), with
       n_s = 1 - 2/N = 0.964 and r = 12/N^2 = 0.004: within the Planck 2018 range (n_s = 0.9649 +- 0.0042) and below the
       tensor bound, 3.5 sigma below the combination of ACT DR6 with Planck, CMB lensing and DESI (n_s = 0.974 +- 0.003);
  PR6  with a free volume an inflation of the fold is seven-dimensional: a vacuum energy of the fold expands the extra
       times together with ordinary space (U = 2A, um3_background.py BG3), Newton's constant 8 pi G_N = kappa_7/(V_t c^3),
       the squares of the gauge and Yukawa couplings and the quartic Higgs coupling (all divided by the fold factor Z) fall
       like e^{-3N} over N e-folds, and the four-dimensional predictions of PR4 and PR5 do not apply: the volume must be
       held fixed during inflation as well.
Reads outputs/geometry.json, outputs/background.json and outputs/superluminal.json (run um3_superluminal.py first).
Writes outputs/primordial.json and reports/primordial_checks.json.  Runs in a few seconds.
Usage: python universe_model_3/code/um3_primordial.py

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
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import hankel1

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

M_PL_RED = 2.435e18          # the reduced Planck mass (GeV)
R_MAX = 0.032                # Planck PR4 + BICEP/Keck 2018 + BAO (95 %; Tristram et al. 2022)
A_S = 2.1e-9                 # Planck 2018
NS = 0.9649                  # Planck 2018 (TT,TE,EE+lowE+lensing)
NS_SIGMA = 0.0042
NS_ACT = 0.974                # ACT DR6 with Planck, CMB lensing and DESI DR1 BAO (Louis et al. 2025)
NS_ACT_SIGMA = 0.003
M_H = 125.25                 # GeV
V_EW = 246.22                # GeV
EULER_GAMMA = 0.5772156649015329


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


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- PR0: the author's vacuum is not a solution of the corrected equations
    geo = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())
    need = geo['author_vacuum_needs_kappaT_over_H2']
    need_v = {k: sp.nsimplify(v) for k, v in need.items()} if isinstance(need, dict) else [sp.nsimplify(v) for v in need]
    vals0 = list(need_v.values()) if isinstance(need_v, dict) else need_v
    ok0 = any(v != 0 for v in vals0) and sorted(str(v) for v in vals0) == sorted(['-7/5', '-7/5', '1', '-7/5', '0'])
    out['PR0'] = {'author_vacuum_needs_kappaT_over_H2': {k: str(v) for k, v in need_v.items()} if isinstance(need_v, dict)
                  else [str(v) for v in vals0]}
    rep.check('PR0_author_vacuum_not_a_solution', ok0,
              'with w = (1, 1/20, 1/360) and Lambda = -7 H^2 the author\'s vacuum (a4 = H x4, b4 constant) would need the bulk '
              'source kappa T/H^2 = %s: it is no longer a solution, and the primordial era of UM-3 is that of the fields of the '
              'fold on the frozen branch, where the fold obeys the Friedmann equations of general relativity' % (
                  out['PR0']['author_vacuum_needs_kappaT_over_H2']))

    # ---------------- PR1
    x4, H, b0, Vt, Vs = sp.symbols('x4 H b0 V_t V_s', positive=True)
    a4 = H * x4
    b4 = b0
    sqrth = sp.exp(3 * a4)
    Z = Vt * (sp.exp(-a4) * b4) ** 3 / Vs
    prod = sp.simplify(sqrth * Z)
    out['PR1'] = {'sqrt(-h) Z': str(prod)}
    rep.check('PR1_no_friction', sp.diff(prod, x4) == 0,
              'record: author\'s vacuum a4 = H x4, b4 = b0: sqrt(-h) Z = %s, constant: the mode equation of a field of the '
              'fold has no friction term' % prod)

    # ---------------- PR2: the spectrum
    Hn = 1.0
    x4_end = 12.0                    # late time, H x4 = 12: k tau = k e^{-12}
    ks = np.array([1e3, 2e3, 4e3, 8e3, 1.6e4]) * math.exp(-0.0)
    rows = []
    for k in ks:
        # start at k tau_start = 400 (deep inside the horizon), the WKB vacuum phi = sqrt(pi/(4H)) H_0^(1)(k tau)
        tau0 = 400.0 / k
        x0 = -math.log(Hn * tau0) / Hn
        z0 = k * tau0
        ph0 = math.sqrt(math.pi / (4 * Hn)) * hankel1(0, z0)
        # d phi/dx4 = d phi/d tau * d tau/dx4 = -k H_0^(1)'(k tau) * (H tau) * norm = k H_1^(1)(k tau) H tau norm
        dph0 = math.sqrt(math.pi / (4 * Hn)) * k * hankel1(1, z0) * Hn * tau0

        def rhs(x, y):
            om2 = k * k * math.exp(-2 * Hn * x)
            return [y[2], y[3], -om2 * y[0], -om2 * y[1]]
        sol = solve_ivp(rhs, (x0, x4_end), [ph0.real, ph0.imag, dph0.real, dph0.imag], rtol=1e-10, atol=1e-13,
                        method='DOP853')
        phi = complex(sol.y[0, -1], sol.y[1, -1])
        tau = math.exp(-Hn * x4_end) / Hn
        exact = math.sqrt(math.pi / (4 * Hn)) * hankel1(0, k * tau)
        late = (math.pi / (4 * Hn)) * (1 + 4 / math.pi ** 2 * (math.log(k * tau / 2) + EULER_GAMMA) ** 2)
        rows.append({'k': float(k), 'k_tau_end': k * tau, 'abs2_numerical': abs(phi) ** 2, 'abs2_hankel': abs(exact) ** 2,
                     'abs2_late_formula': late, 'P': k ** 3 * abs(phi) ** 2 / (2 * math.pi ** 2)})
    lnk = np.log([r['k'] for r in rows])
    lnP = np.log([r['P'] for r in rows])
    n_minus_1 = float(np.polyfit(lnk, lnP, 1)[0])
    # the local index of the late-time formula: P ~ k^3 [1 + (4/pi^2) L^2], L = ln(k tau/2) + gamma_E
    Ls = sp.Symbol('L', real=True)
    nloc = 3 + sp.diff(sp.log(1 + 4 * Ls ** 2 / sp.pi ** 2), Ls)
    nloc_ok = sp.simplify(nloc - (3 + (8 / sp.pi ** 2) * Ls / (1 + 4 * Ls ** 2 / sp.pi ** 2))) == 0
    crit = sp.solve(sp.diff(nloc, Ls), Ls)
    nmin = min(float(nloc.subs(Ls, c)) for c in crit)
    out['PR2'] = {'rows': rows, 'n_minus_1_fit': n_minus_1, 'n_minus_1_local': str(nloc), 'n_minus_1_min': nmin,
                  'Planck_ns_minus_1': NS - 1}
    rep.check('PR2_spectrum', all(abs(r['abs2_numerical'] - r['abs2_hankel']) < 1e-6 * r['abs2_hankel'] for r in rows)
              and all(abs(r['abs2_late_formula'] - r['abs2_hankel']) < 0.02 * r['abs2_hankel'] for r in rows)
              and 2.36 < n_minus_1 < 3.0 and nloc_ok and abs(nmin - (3 - 2 / math.pi)) < 1e-9,
              'record: the mode equation integrated from the early-time vacuum agrees with sqrt(pi/(4H)) H_0^(1)(k tau) '
              '(relative difference below 1e-6) and at k tau = %.1e ... %.1e with the late-time formula; the local index of '
              'k^3 |phi_k|^2/(2 pi^2) is n_S - 1 = %s with L = ln(k tau/2) + gamma_E, not a power law: it tends to 3 at late '
              'times and is never below 3 - 2/pi = %.3f (a fit over these k gives %.3f), against n_s - 1 = %.4f observed' % (
                  rows[0]['k_tau_end'], rows[-1]['k_tau_end'], nloc, nmin, n_minus_1, NS - 1))

    # ---------------- PR3: the gauge couplings
    g = sp.symbols('g', positive=True)
    geff2 = sp.simplify(g ** 2 / Z * Vt * b0 ** 3 / Vs)     # normalised to g^2 at x4 = 0
    rate = sp.simplify(sp.diff(sp.log(geff2), x4))
    out['PR3'] = {'g_eff^2 / g^2 (normalised at x4 = 0)': str(sp.simplify(geff2 / g ** 2)), 'd ln g_eff^2/d x4': str(rate)}
    rep.check('PR3_couplings_grow', sp.simplify(rate - 3 * H) == 0,
              'record: the gauge action carries Z/g^2: g_eff^2 = g^2/Z grows like %s (d ln g_eff^2/dx4 = %s): the couplings of the '
              'fold grow like e^{3 H x4/2} in the author\'s vacuum' % (sp.simplify(geff2 / g ** 2), rate))

    # ---------------- PR4: inflation of the fold with the volume of the extra times held fixed
    bg = json.loads((UM3 / 'outputs' / 'background.json').read_text())['BG3']['inflation_volume_held']
    Asym = sp.Symbol('A', real=True)
    rho_v = sp.sympify(bg['kappa_rho_m_over_H'], locals={'A': Asym})
    p_v = sp.sympify(bg['kappa_p_m_over_H'], locals={'A': Asym})
    q_add = sp.sympify(bg['kappa_q_added_by_the_fold_fluid_over_H'], locals={'A': Asym})
    ok4a = sp.simplify(p_v + rho_v) == 0 and sp.simplify(q_add + rho_v * (1 + Asym ** 2 / 4)) == 0
    Hinf = math.pi * M_PL_RED * math.sqrt(R_MAX * A_S / 2)
    sl5 = json.loads((UM3 / 'outputs' / 'superluminal.json').read_text())['SL5']['rows']
    H_max = [r_['max_H_GeV_if_faster_qb_0.03_omega_b'] for r_ in sl5 if r_['omega_b_GeV'] == 1500.0][0]
    A_inf = Hinf / H_max
    T_A1 = math.sqrt(H_max * 1.22e19 / (1.66 * math.sqrt(106.75)))        # H_4 = 1.66 sqrt(g*) T^2/M_Pl = H
    out['PR4'] = {'H_inf_max_GeV': Hinf, 'r_max': R_MAX, 'A_s': A_S, 'kappa_rho_v_over_H': str(rho_v),
                  'kappa_q_added_by_the_fold_fluid_over_H': str(q_add), 'H_max_GeV_electron_bound': H_max,
                  'A_inf_at_the_bounds': A_inf, 'q_hold_over_rho_v_at_the_bounds': A_inf ** 2 / 4,
                  'q_hold_over_tension_at_the_bounds': A_inf ** 4 / 8, 'T_GeV_where_A_is_1_after_inflation': T_A1}
    rep.check('PR4_inflation_of_the_fold', ok4a and 4.3e13 < Hinf < 4.6e13 and A_inf > 1e25 and 100 < T_A1 < 1000,
              'with the volume of the extra times held fixed a vacuum energy of the fold (kappa rho_v = %s H = -kappa p) '
              'expands ordinary space exponentially as in general relativity (a4\' = A H), the fold fluid adding the pressure '
              'kappa delta q = %s H = -kappa rho_v (1 + A^2/4) along the extra times; the observed spectrum (n_s - 1 = %.4f) '
              'is that of such an era, whose Hubble rate the bound r < %.3f (A_s = %.1e) limits to H_inf < pi M_Pl,red '
              'sqrt(r A_s/2) = %.2e GeV; with H at most %.2e GeV (SL5, electrons made faster) A = H_inf/H is at least %.1e, '
              'so the pressure that the fold fluid adds is at least about %.0e rho_v and %.0e times its own tension (about '
              'A^4/8 times, growing without limit as H gets smaller; rho_v = 3 H_inf^2 M_Pl,red^2, lambda_F = 6 H^2 '
              'M_Pl,red^2); after inflation A = H_4/H exceeds 1 above T = %.0f GeV; what '
              'supplies this pressure is OPEN' % (rho_v, q_add, NS - 1, R_MAX, A_S, Hinf, H_max, A_inf, A_inf ** 2 / 4,
                                                  A_inf ** 4 / 8, T_A1))

    # ---------------- PR5: ESTIMATE, Higgs inflation
    N = 55
    lam_tree = M_H ** 2 / (2 * V_EW ** 2)
    rows5 = []
    for lam in (lam_tree, 0.01):
        xi = N * math.sqrt(lam / (72 * math.pi ** 2 * A_S))
        rows5.append({'lambda': lam, 'xi_H': xi})
    ns_h = 1 - 2 / N
    r_h = 12 / N ** 2
    out['PR5'] = {'rows': rows5, 'N': N, 'n_s': ns_h, 'r': r_h,
                  'Planck': {'n_s': NS, 'sigma': NS_SIGMA}, 'ACT_P_LB': {'n_s': NS_ACT, 'sigma': NS_ACT_SIGMA},
                  'pull_Planck': (ns_h - NS) / NS_SIGMA, 'pull_ACT': (ns_h - NS_ACT) / NS_ACT_SIGMA}
    ok5 = (all(r_['xi_H'] > 1e3 for r_ in rows5) and abs(ns_h - NS) < NS_SIGMA and r_h < R_MAX
           and (ns_h - NS_ACT) / NS_ACT_SIGMA < -2.5)
    rep.check('PR5_higgs_inflation', ok5,
              'ESTIMATE, an extension outside the action of UM-3 (the coupling -xi_H R_fold Phi^dagger Phi is not in '
              'IN-11): with its own Einstein-Hilbert term the fold no longer needs the induced gravity that required '
              'xi_H < 1/6, so the Higgs field can be the inflaton: xi_H = N sqrt(lambda/(72 pi^2 A_s)) = %s for lambda = %.4f '
              '(m_H^2/(2 v^2)) and 0.01 (the running value near the inflationary scale), N = %d; then n_s = 1 - 2/N = %.4f and '
              'r = 12/N^2 = %.4f: %.1f sigma from Planck 2018 (%.4f +- %.4f), below the tensor bound, %.1f sigma from ACT DR6 '
              'with Planck, CMB lensing and DESI (%.3f +- %.3f); the unitarity of Higgs inflation above M_Pl/xi_H is debated' % (
                  ['%.0f' % r_['xi_H'] for r_ in rows5], lam_tree, N, ns_h, r_h, (ns_h - NS) / NS_SIGMA, NS, NS_SIGMA,
                  (ns_h - NS_ACT) / NS_ACT_SIGMA, NS_ACT, NS_ACT_SIGMA))

    # ---------------- PR6: a free volume makes the inflation seven-dimensional
    bgf = json.loads((UM3 / 'outputs' / 'background.json').read_text())['BG3']['inflation_volume_free']
    sec = [sp.sympify(e, locals={'A': Asym, 'U': sp.Symbol('U', real=True)}) for e in bgf['second_order']]
    Usym = sp.Symbol('U', real=True)
    u_sol = sp.solve(sec[1].subs(Asym, 1), Usym)
    ok6 = u_sol == [2] and sp.simplify(sec[0].subs({Asym: 1, Usym: 2})) == 0
    Nf = 60
    out['PR6'] = {'U_over_A_free_volume': [str(u) for u in u_sol], 'coupling_factor_after_60_efolds': math.exp(-3 * Nf),
                  'G_N_factor_after_60_efolds': math.exp(-3 * Nf)}
    rep.check('PR6_free_volume_inflation', ok6,
              'with a free volume a vacuum energy of the fold makes the source of the fold the same in all seven directions '
              'only for U = %s A (to second order; um3_background.py BG3): the extra times inflate together with ordinary '
              'space, so 8 pi G_N = kappa_7/(V_t c^3), the squares of the gauge and Yukawa couplings and the quartic Higgs '
              'coupling (all divided by the fold factor Z) fall like e^{-3N} (a factor %.1e after %d e-folds) and the four-dimensional predictions of PR4 and PR5 do not apply: UM-3 needs the volume of the extra '
              'times held fixed during inflation as well' % (u_sol, math.exp(-3 * Nf), Nf))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'primordial.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_primordial.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'primordial_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
