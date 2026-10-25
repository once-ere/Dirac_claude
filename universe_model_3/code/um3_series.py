#!/usr/bin/env python3
"""um3_series.py - the corrections to the author's separable metric around the static block (the power series FE-35)
and what the junction conditions require of the cosmology of the fold, with the corrected Lovelock weights
w = (1, 1/20, 1/360) and Lambda = -7 H^2 (the author's order of 2026-10-25 07:55; SOLUTION.md, FE-59).

The general warped metric FE-34, ds^2 = d sigma^2 + e^{2 fa} dx_i^2 - e^{2 fn} dx4^2 - e^{2 fb} dx_r^2, is expanded around
the static block fa = fb = -H|sigma|, fn = 0 (a4 = 0, b4 = 1 normalised):
    fa = -H|sigma| + eps alpha(sigma),  fb = -H|sigma| + eps beta(sigma),  fn = eps nu(sigma)    (static).
Inputs: the exact left-hand side of FE-1, the junction potential of FE-4 for the general metric, and the fold source of
the author's metric for any a4(x4), b4(x4) (outputs/fold.json of um3_fold.py).  Rates: A = a4'/H, U = b4'/(H b4),
Ad = A'/H, Ud = U'/H; the scale factor of the extra times on the fold is c = e^{-a4} b4, its rate v = c'/c = (U - A) H.
Computed and checked:
  SR1  the static block is a vacuum (no source at order 0, no stabiliser), and the linearised static bulk operator
       vanishes identically on both sides of the fold: around the static block the bulk equations have no linear part
       (a degenerate vacuum);
  SR2  the second-order static operator; its sigma component fixes alpha'/beta' to one of two values, and then the
       components along ordinary space and the extra times force every non-trivial static deformation to grow like
       e^{3H|sigma|} away from the fold: there is no bounded static correction;
  SR3  the junction conditions: the fold source does not respond linearly to jumps of the sigma-derivatives (the
       coefficients of the second derivatives vanish with the linear operator); the second-order response;
  SR4  the fold is a seven-dimensional Einstein brane: the fold source of the author's metric for any a4(x4), b4(x4),
       plus its tension kappa lambda_F = 32 H/5, equals to second order in the rates (16/(15 H)) G^a_b, G^a_b the Einstein
       tensor of the seven-dimensional metric of the fold, so kappa_7 = 15 kappa H/16; the remainders start at fourth
       order; for frozen extra times the Friedmann equations hold exactly; the radion equation
       v' + 3 v (a4' + v) = (kappa_7/5)(rho - 3p + 2q) (q the pressure along the extra times);
  SR5  without a stabilisation the radion equation drives the volume of the extra times once matter and vacuum energy
       dominate: integrated from the radiation era to today, Newton's constant and the fine-structure constant change
       today at a rate excluded by lunar laser ranging (G'/G = (-5.0 +- 9.6) 1e-15 per year), by optical clocks
       (alpha'/alpha = (1.8 +- 2.5) 1e-19 per year), by the Oklo reactor (|Delta alpha/alpha| < 1.2e-7 over 1.8 Gyr) and
       by nucleosynthesis (G then over G today = 1.01 +0.20 -0.16);
  SR6  with the volume held fixed (the fold fluid supplies the missing pressure along the extra times, IN-10) the
       four-dimensional equations are those of general relativity with 8 pi G_N = kappa_7/V_*; the pressure the fold
       fluid must add today, -Delta_r = -0.793 rho_c.
Writes outputs/series.json and reports/series_checks.json.  Runs in about a minute.
Usage: python universe_model_3/code/um3_series.py

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
import sympy as sp
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
from um3_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

H = sp.Symbol('H', positive=True)
eps = sp.Symbol('eps')
NAMES = ['fa_s', 'fa_ss', 'fa_st', 'fa_t', 'fa_tt', 'fb_s', 'fb_ss', 'fb_st', 'fb_t', 'fb_tt', 'fn_s', 'fn_ss', 'fn_st',
         'fn_t', 'fn_tt', 'fn0']
SY = {n: sp.Symbol(n, real=True) for n in NAMES}
a1, a2, b1, b2, n1, n2, n0 = sp.symbols('a1 a2 b1 b2 n1 n2 n0', real=True)
A, U, Ad, Ud = sp.symbols('A U Ad Ud', real=True)

# today's composition of the fold universe (fractions of the critical density; Planck 2018 with three massless
# neutrino states counted as radiation) and the extra-time pressure of each component in units of its energy density:
# radiation q = 0, the bound states chi of dirac16complex q = 0, the baryons (particles made of fields of the fold) q = -rho,
# the vacuum energy p = q = -rho
SPECIES = {'radiation': (9.1e-5, 1.0 / 3.0, 0.0), 'chi': (0.265, 0.0, 0.0), 'baryons': (0.049, 0.0, -1.0),
           'vacuum_energy': (0.685, -1.0, -1.0)}
H0_PER_YEAR = 67.4 * 1.0e3 / 3.0856775814913673e22 * 3.15576e7      # H_0 = 67.4 km/s/Mpc in 1/year
GDOT_BOUND = 9.6e-15        # |G'/G| per year, one sigma: (-5.0 +- 9.6) 1e-15 (lunar laser ranging, Biskupek et al. 2021)
ALPHADOT_BOUND = 2.5e-19    # |alpha'/alpha| per year, one sigma: (1.8 +- 2.5) 1e-19 (optical clocks, Filzinger et al. 2023)
OKLO_BOUND = 1.2e-7         # |Delta alpha/alpha| since the Oklo reactor 1.8 Gyr ago (z = 0.14; Damour and Dyson 1996)
GBBN_RANGE = (0.85, 1.21)   # G at nucleosynthesis over G today, 1.01 +0.20 -0.16 (68 per cent; Copi, Davis and Krauss 2004)
Z_OKLO = 0.14


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def static_sub(side):
    """Static perturbation of the static block on one side (side = +1: sigma > 0, fa_s = -H + eps a1)."""
    s = {SY['fa_s']: -H * side + eps * a1, SY['fa_ss']: eps * a2, SY['fb_s']: -H * side + eps * b1, SY['fb_ss']: eps * b2,
         SY['fn_s']: eps * n1, SY['fn_ss']: eps * n2, SY['fn0']: eps * n0}
    for k in ('fa_st', 'fa_t', 'fa_tt', 'fb_st', 'fb_t', 'fb_tt', 'fn_st', 'fn_t', 'fn_tt'):
        s[SY[k]] = 0
    return s


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def einstein_7(t):
    """The Einstein tensor G^a_b (frame) of the seven-dimensional metric of the fold,
    diag(e^{2a}, e^{2a}, e^{2a}, -1, -c^2, -c^2, -c^2) in (x1, x2, x3, x4, x5, x6, x7), with a(x4), c(x4)."""
    X7 = sp.symbols('y1:8', real=True)
    tt = X7[3]
    af = sp.Function('a')(tt)
    cf = sp.Function('c')(tt)
    g = sp.diag(sp.exp(2 * af), sp.exp(2 * af), sp.exp(2 * af), -1, -cf ** 2, -cf ** 2, -cf ** 2)
    hs = [sp.exp(af)] * 3 + [sp.S(1)] + [cf] * 3
    Rf = frame_riemann(g, X7, hs, simplify=lambda e: sp.simplify(e))
    G = lovelock_tensor(Rf, 1, n=7, simplify=sp.simplify)
    # a' = A H, a'' = Ad H^2, c'/c = V H, c''/c = ((V1) + V^2) H^2 with V = U - A, V1 = Ud - Ad
    V, V1 = U - A, Ud - Ad
    rep = {}
    out = {}
    for i in range(7):
        e = G[i, i]
        e = e.subs(sp.Derivative(cf, (tt, 2)), cf * (V1 + V ** 2) * H ** 2).subs(sp.Derivative(cf, tt), cf * V * H)
        e = e.subs(sp.Derivative(af, (tt, 2)), Ad * H ** 2).subs(sp.Derivative(af, tt), A * H)
        out[i] = sp.expand(sp.simplify(e))
    off = all(sp.simplify(G[i, j]) == 0 for i in range(7) for j in range(7) if i != j)
    return out, off


def truncate(e, order):
    """Keep the terms of e up to the given order in the rates (A, U of order 1; Ad, Ud of order 2)."""
    s = sp.Symbol('s_ord')
    es = sp.expand(e.subs({A: s * A, U: s * U, Ad: s ** 2 * Ad, Ud: s ** 2 * Ud}, simultaneous=True))
    return sp.expand(sum(es.coeff(s, k) for k in range(order + 1)))


def radion_history(stabilised=False):
    """The fold universe with the volume of the extra times free: the seven-dimensional Einstein equations of the fold
    (SR4) with the four components of SPECIES, integrated in N = ln(e^{a4}) from N = ln(1e-9) (radiation era, v = 0) to
    N = 0 (today, a4 = 0).  Units: H_0 = 1 (today's expansion rate if the volume did not change), kappa_7 rho_crit = 3.
    Each component has rho = 3 Omega e^{-3(1+w)N} c^{-3(1+u)} (c the scale factor of the extra times, c = 1 at N0)."""
    names = list(SPECIES)
    Om = np.array([SPECIES[k][0] for k in names])
    w = np.array([SPECIES[k][1] for k in names])
    u = np.array([SPECIES[k][2] for k in names])

    def dens(N, lnc):
        return 3.0 * Om * np.exp(-3.0 * (1 + w) * N - 3.0 * (1 + u) * lnc)

    def rates(N, y):
        lnc, v = y
        rho = dens(N, lnc)
        X = rho.sum() / 3.0                                   # kappa rho/3 = a'^2 + 3 a' v + v^2
        ap = (-3.0 * v + math.sqrt(max(5.0 * v * v + 4.0 * X, 0.0))) / 2.0
        src = (rho * (1 - 3 * w + 2 * u)).sum() / 5.0        # (kappa/5)(rho - 3p + 2q)
        dv = 0.0 if stabilised else src - 3.0 * v * (ap + v)
        return [v / ap, dv / ap]

    N0 = math.log(1e-9)
    N_bbn = math.log(2.35e-10)          # T = 1 MeV (T_0 = 2.35e-4 eV)
    N_oklo = -math.log(1 + Z_OKLO)
    N0 = min(N0, N_bbn - 1.0)
    sol = solve_ivp(rates, (N0, 0.0), [0.0, 0.0], method='LSODA', rtol=1e-10, atol=1e-14,
                    t_eval=[N_bbn, N_oklo, 0.0])
    lnc_bbn, lnc_oklo, lnc_end = (float(x) for x in sol.y[0])
    v_end = float(sol.y[1, -1])
    rho_end = dens(0.0, lnc_end)
    X = rho_end.sum() / 3.0
    ap_end = (-3.0 * v_end + math.sqrt(5.0 * v_end ** 2 + 4.0 * X)) / 2.0
    return {'ln_c_today_minus_initial': float(lnc_end), 'v_today_over_H0': float(v_end), 'a4prime_today_over_H0': float(ap_end),
            'ln_c_today_minus_oklo': float(lnc_end - lnc_oklo), 'ln_c_today_minus_bbn': float(lnc_end - lnc_bbn),
            'Gdot_over_G_per_year': float(-3.0 * v_end * H0_PER_YEAR),
            'alphadot_over_alpha_per_year': float(-3.0 * v_end * H0_PER_YEAR),
            'Delta_ln_alpha_since_oklo': float(-3.0 * (lnc_end - lnc_oklo)),
            'Delta_ln_G_since_bbn': float(-3.0 * (lnc_end - lnc_bbn))}


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    loc = dict(SY, H=H)
    L = {k: sp.sympify(v, locals=loc) for k, v in fold['lhs_general'].items()}
    F = {k: sp.sympify(v, locals=loc) for k, v in fold['junction_potential'].items()}
    comps = [('sigma', 'x0,x0'), ('space', 'x1,x1'), ('time', 'x4,x4'), ('extra', 'x5,x5')]

    # ---------------- SR1: order 0 and the linearised static operator
    lin, zero, ser2 = {}, {}, {}
    for side in (+1, -1):
        sub = static_sub(side)
        for nm, k in comps:
            e = L[k].subs(sub)
            se = sp.series(e, eps, 0, 3).removeO()
            zero[(side, nm)] = sp.simplify(se.coeff(eps, 0))
            lin[(side, nm)] = sp.expand(sp.simplify(se.coeff(eps, 1)))
            ser2[(side, nm)] = sp.factor(sp.expand(se.coeff(eps, 2)))
    ok0 = all(zero[k] == 0 for k in zero)
    okl = all(lin[k] == 0 for k in lin)
    out['SR1'] = {'order_0': {nm: str(zero[(1, nm)]) for nm, _ in comps}, 'order_1': {nm: str(lin[(1, nm)]) for nm, _ in comps}}
    rep.check('SR1_degenerate_static_block', ok0 and okl,
              'with w = (1, 1/20, 1/360) and Lambda = -7 H^2 the static block is a vacuum (order 0: %s, no stabiliser) and the '
              'linearised static bulk operator vanishes identically on both sides of the fold (order 1 in eps for the '
              'deformations fa = -H|sigma| + eps alpha, fb = -H|sigma| + eps beta, fn = eps nu: %s): around the static block the bulk '
              'equations have no linear part, a degenerate vacuum' % (out['SR1']['order_0'], out['SR1']['order_1']))

    # ---------------- SR2: the second-order static operator and its solutions
    q2 = {nm: ser2[(1, nm)] for nm, _ in comps}
    mirror = {a1: -a1, b1: -b1, n1: -n1}
    okm = all(sp.simplify(ser2[(-1, nm)] - q2[nm].subs(mirror, simultaneous=True)) == 0 for nm, _ in comps)
    exp_sigma = -sp.Rational(24, 5) * (a1 ** 2 + 3 * a1 * b1 + b1 ** 2)
    ok_sig = sp.simplify(q2['sigma'] - exp_sigma) == 0 and q2['time'] == 0
    # the ansatz alpha' = l1 f(sigma), beta' = l2 f(sigma): sigma component fixes l1/l2, the others fix f'/f
    l1, l2, ff, fp = sp.symbols('l1 l2 f fp', real=True)
    ans = {a1: l1 * ff, a2: l1 * fp, b1: l2 * ff, b2: l2 * fp}
    ratios = sp.solve(sp.Eq(q2['sigma'].subs(ans).subs(l2, 1) / ff ** 2, 0), l1)
    growth = []
    for r in ratios:
        rates_ = set()
        for nm in ('space', 'extra'):
            e = sp.factor(q2[nm].subs(ans).subs({l1: r, l2: 1}))
            sol = sp.solve(sp.Eq(e, 0), fp)
            rates_ |= {sp.simplify(x / ff) for x in sol}
        growth.append({'l1_over_l2': str(sp.nsimplify(r)), 'fprime_over_f': [str(x) for x in rates_]})
    ok2 = okm and ok_sig and len(ratios) == 2 and all(g['fprime_over_f'] == ['3*H'] for g in growth)
    out['SR2'] = {'second_order': {nm: str(v) for nm, v in q2.items()}, 'static_solutions': growth}
    rep.check('SR2_second_order_static', ok2,
              'the static bulk equations start at second order in the deformation (alpha\' = a1, alpha\'\' = a2, beta\' = b1, '
              'beta\'\' = b2, nu\' = n1): sigma %s, ordinary space %s, time %s, extra times %s (sigma > 0; the mirror image for '
              'sigma < 0); the sigma component fixes alpha\'/beta\' = %s, and then ordinary space and the extra times require '
              'f\'/f = %s: every non-trivial static deformation grows like e^{3H|sigma|} away from the fold; there is no bounded '
              'static correction' % (q2['sigma'], q2['space'], q2['time'], q2['extra'], [g['l1_over_l2'] for g in growth],
                                       sorted({x for g in growth for x in g['fprime_over_f']})))

    # ---------------- SR3: the junction conditions for static deformations
    ja, jb, jn = sp.symbols('ja jb jn')   # the jumps [alpha'], [beta'], [nu'] (mirror-odd: value at 0+ = jump/2)
    jump1, jump2 = {}, {}
    for nm, k in comps[1:]:
        Fp = F[k].subs(static_sub(+1)).subs({a1: ja / 2, b1: jb / 2, n1: jn / 2, n0: 0})
        Fm = F[k].subs(static_sub(-1)).subs({a1: -ja / 2, b1: -jb / 2, n1: -jn / 2, n0: 0})
        se = sp.series(sp.expand(Fp - Fm), eps, 0, 3).removeO()
        jump1[nm] = sp.simplify(se.coeff(eps, 1))
        jump2[nm] = sp.factor(sp.expand(se.coeff(eps, 2)))
    ok3 = all(v == 0 for v in jump1.values())
    out['SR3'] = {'kappa_deltaS_first_order': {nm: str(v) for nm, v in jump1.items()},
                  'kappa_deltaS_second_order': {nm: str(v) for nm, v in jump2.items()}}
    rep.check('SR3_junction_of_static_deformations', ok3,
              'the fold source does not respond linearly to jumps [alpha\'], [beta\'], [nu\'] of the sigma-derivatives at the fold '
              '(first order: %s), as the coefficients of the second derivatives in the linear bulk operator vanish (SR1); at '
              'second order kappa delta S (space, time, extra) = %s (ja, jb, jn the jumps)' % (
                  {nm: str(v) for nm, v in jump1.items()}, {nm: str(v) for nm, v in jump2.items()}))

    # ---------------- SR4: the fold as a seven-dimensional Einstein brane
    G7, off = einstein_7(None)
    kS = {k: sp.sympify(v, locals={'H': H, 'A': A, 'U': U, 'Ad': Ad, 'Ud': Ud}) for k, v in fold['fold_source_kappaS'].items()}
    lamF = sp.Rational(32, 5) * H                       # the tension of the static block (kappa lambda_F)
    pairs = {'space': ('x1,x1', 0), 'time': ('x4,x4', 3), 'extra': ('x5,x5', 4)}
    res2, res4 = {}, {}
    for nm, (k, i) in pairs.items():
        diff = sp.expand(kS[k] + lamF - sp.Rational(16, 15) / H * G7[i])
        res2[nm] = truncate(diff, 2)
        res4[nm] = sp.factor(diff)
    ok4a = off and all(v == 0 for v in res2.values())
    # the radion equation from the seven-dimensional Einstein equations: rho = -G^4_4/k7, p = G^1_1/k7, q = G^5_5/k7
    v_, vd_ = (U - A) * H, (Ud - Ad) * H ** 2
    comb = sp.expand((-G7[3] - 3 * G7[0] + 2 * G7[4]) / 5 - (vd_ + 3 * v_ * (A * H + v_)))
    ok4b = sp.simplify(comb) == 0
    # the four-dimensional Friedmann equations for frozen extra times hold exactly (no higher order)
    fro = {U: A, Ud: Ad}
    exact_fr = {nm: sp.factor(sp.expand(res4[nm].subs(fro))) for nm in res4}
    ok4c = exact_fr['space'] == 0 and exact_fr['time'] == 0 and exact_fr['extra'] != 0
    out['SR4'] = {'einstein_tensor_7': {str(i): str(v) for i, v in G7.items()},
                  'fold_source_minus_einstein_second_order': {nm: str(v) for nm, v in res2.items()},
                  'fold_source_minus_einstein_all_orders': {nm: str(v) for nm, v in res4.items()},
                  'frozen_remainder': {nm: str(v) for nm, v in exact_fr.items()},
                  'radion_equation': "v' + 3 v (a4' + v) = (kappa_7/5)(rho - 3p + 2q)"}
    rep.check('SR4_seven_dimensional_einstein_brane', ok4a and ok4b and ok4c,
              'the fold source of the author\'s metric for any a4(x4), b4(x4) plus the tension kappa lambda_F = 32H/5 equals, to '
              'second order in the rates (A, U of first order, A1 = Ad, U1 = Ud of second), (16/(15H)) G^a_b with G^a_b the '
              'Einstein tensor of the seven-dimensional metric of the fold, diag(e^{2a4}, e^{2a4}, e^{2a4}, -1, -c^2, -c^2, -c^2), '
              'c = e^{-a4} b4: the fold obeys Einstein gravity in seven dimensions with kappa_7 = 15 kappa H/16; the remainders '
              'start at fourth order (space %s; time %s; extra times %s); for frozen extra times the components along ordinary '
              'space and the time hold exactly (the Friedmann equations), the extra-time component keeps %s; the Einstein '
              'equations give the radion equation v\' + 3v(a4\' + v) = (kappa_7/5)(rho - 3p + 2q) for the rate v = c\'/c of the '
              'extra times' % (res4['space'], res4['time'], res4['extra'], exact_fr['extra']))

    # ---------------- SR5: the volume of the extra times without a stabilisation
    free = radion_history(stabilised=False)
    held = radion_history(stabilised=True)
    out['SR5'] = {'species': {k: {'Omega': v[0], 'w': v[1], 'q_over_rho': v[2]} for k, v in SPECIES.items()},
                  'free_volume': free, 'held_volume': held,
                  'bounds': {'Gdot_over_G_per_year_1sigma': GDOT_BOUND, 'alphadot_over_alpha_per_year_1sigma': ALPHADOT_BOUND,
                             'oklo_Delta_alpha': OKLO_BOUND}, 'H0_per_year': H0_PER_YEAR}
    fac_G = abs(free['Gdot_over_G_per_year']) / GDOT_BOUND
    fac_a = abs(free['alphadot_over_alpha_per_year']) / ALPHADOT_BOUND
    fac_o = abs(free['Delta_ln_alpha_since_oklo']) / OKLO_BOUND
    g_bbn = math.exp(-free['Delta_ln_G_since_bbn'])          # G at nucleosynthesis over G today
    ok5 = (held['ln_c_today_minus_initial'] == 0.0 and free['v_today_over_H0'] > 0.1 and fac_G > 100 and fac_a > 1e7
           and fac_o > 1e5 and not (GBBN_RANGE[0] < g_bbn < GBBN_RANGE[1]))
    out['SR5']['free_volume']['G_bbn_over_G_today'] = g_bbn
    rep.check('SR5_free_volume_excluded', ok5,
              'without a stabilisation the radion equation drives the volume of the extra times: integrated from the radiation '
              'era (where radiation, rho = 3p, q = 0, does not drive it) to today with chi (q = 0), baryons (q = -rho) and '
              'vacuum energy (q = -rho), the scale factor c of the extra times grows by ln c = %.3f, and today v = c\'/c = %.3f H_0 '
              '= %.2f a4\' (H_0 = 67.4 km/s/Mpc the expansion rate the same densities give with the volume held fixed); Newton\'s '
              'constant 8 pi G_N = kappa_7/(V_t c^3) and the fine-structure constant (alpha ~ 1/Z ~ c^-3) then change by -3v = '
              '%.2e per year, %.0f times the bound of lunar laser ranging (%.1e) and %.1e times that of optical clocks (%.1e); '
              'alpha changed by %.3f since the Oklo reactor (%.1e times its bound %.1e), and G at nucleosynthesis was %.1f times '
              'today\'s (allowed 1.01 +0.20 -0.16): the volume of the extra times must be held fixed' % (
                  free['ln_c_today_minus_initial'], free['v_today_over_H0'],
                  free['v_today_over_H0'] / free['a4prime_today_over_H0'], free['Gdot_over_G_per_year'], fac_G, GDOT_BOUND,
                  fac_a, ALPHADOT_BOUND, free['Delta_ln_alpha_since_oklo'], fac_o, OKLO_BOUND, g_bbn))

    # ---------------- SR6: the volume held fixed by the fold fluid
    kq_req = sp.sympify(fold['extra_time_pressure_required']['kappa_q_m'], locals={'H': H, 'A': A, 'Ad': Ad})
    rho, p_, q_ = sp.symbols('rho p q', real=True)
    k7 = sp.Symbol('kappa_7', positive=True)
    # with frozen extra times: kappa_7 rho = 3 A^2 H^2, kappa_7 p = -(3 A^2 + 2 Ad) H^2; kappa = 16 kappa_7/(15 H)
    lead = sp.expand(truncate(kq_req, 2) * 15 * H / 16)                       # kappa_7 q_required to second order
    target = -sp.Rational(1, 2) * (3 * A ** 2 * H ** 2 + 3 * (3 * A ** 2 + 2 * Ad) * H ** 2)   # -(kappa_7/2)(rho - 3p)
    ok6a = sp.simplify(lead - target) == 0
    Delta = sum(om * (wq + (1 - 3 * w) / 2) for om, w, wq in SPECIES.values())
    out['SR6'] = {'kappa_q_required': str(kq_req), 'kappa7_q_required_second_order': str(lead),
                  'Delta_r_over_rho_c_today': Delta, 'fold_fluid_extra_pressure_today_over_rho_c': -Delta}
    ok6 = ok6a and 0.79 < Delta < 0.80
    rep.check('SR6_volume_held_by_the_fold_fluid', ok6,
              'with the extra times frozen the fold source holds exactly the Friedmann equations of general relativity (SR4), '
              'with 8 pi G_N = kappa_7/V_* = 15 kappa H/(16 V_*); the extra-time component requires the pressure kappa q = %s '
              '(to second order q = -(rho - 3p)/2): radiation supplies it, the other components do not; the mismatch '
              'Delta_r = sum (q + (rho - 3p)/2) = %.3f rho_c today, so the fold fluid has to carry the pressure -%.3f rho_c along '
              'the extra times on top of its tension (IN-10) to hold the volume fixed' % (kq_req, Delta, Delta))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'series.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_series.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'series_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
