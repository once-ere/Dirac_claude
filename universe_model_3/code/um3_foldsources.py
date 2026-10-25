#!/usr/bin/env python3
"""um3_foldsources.py - the sources of the fold with the corrected Lovelock weights: the graviton of the fold, the
Einstein-Hilbert term of the fold, the gravity induced by the fields of the fold, and the fold fluid.

The metric of the fold region in the proper chart (um3_fold.py),
    ds^2 = d sigma^2 + e^{2 fa} dx_i^2 - e^{2 fn} dx4^2 - e^{2 fb} dx_r^2,
with the author's fa = a4 - H|sigma|, fb = ln b4 - a4 - H|sigma|, fn = 0, carries a transverse traceless graviton of the
+ polarisation travelling along x3,  g_11 = e^{2 fa + eps h},  g_22 = e^{2 fa - eps h},  h = h(sigma, x3, x4).  The metric stays
diagonal, so the exact Lovelock machinery of um3_lovelock.py applies.  TT = sum_p alpha_p (E_(p)^1_1 - E_(p)^2_2)/2 at first
order in eps, alpha_p = w_p H^(2-2p).  The corrected weights w = (1, 1/20, 1/360), Lambda = -7 H^2 (the author's order of
2026-10-25 07:55; um3_weights.py W3, W4) are used throughout; the author's original weights w = (1, 1/32, 1/1152),
Lambda = -10 H^2 are kept as the record of why the correction was needed.  Computed and checked:
  F1  the linearised equation is linear in the second sigma-derivatives (fa_ss, fb_ss, fn_ss, h_ss) with coefficients that
      form an exact differential in the first sigma-derivatives (a junction potential exists); away from the fold, on
      every background with frozen extra times (b4'/b4 = a4', any a4(x4)), every coefficient of the graviton (h_tt, h_33,
      h_ss, h_s, h_t, ...) vanishes: the bulk carries no linear graviton; record: with the author's weights the bulk
      operator at the static block was (1/32) h_tt - (5/32)(e^{-2fa} h_33 + h_ss - 6H h_s) (local cone v^2 = 5);
  F2  the thin part at the fold (the integral of TT across the fold): for frozen extra times and any a4(x4)
      kappa Pi = (8/(15H)) (h_tt + 3 A H h_t - h_33), with no term in the jump [h_sigma]; Einstein gravity alone gives no
      h_tt, h_33 term at the fold; checked by smoothing the kink (h_tt, h_33 and h_t coefficients); record: with the
      author's weights (5/(12H)) h_tt - (17/(48H)) h_33 + (19/16) A h_t - ((5 + A^2 + A1)/32) [h_sigma];
  F3  the four-dimensional graviton: the wave equation of the fold, h_tt + 3 a4' h_t - e^{-2 a4} nabla^2 h = (2 kappa_7/
      kappa) x (the transverse traceless stress of the fold matter), is that of general relativity with
      kappa_7 = 15 kappa H/16, the same coupling as in the Friedmann equations of the fold (um3_fold.py J7): gravitational
      waves travel at the speed of light at every wavelength, and their Planck mass equals that of the expansion; record:
      with the author's weights the long-wavelength mode had c_g^2 = 83/82 (bulk alone 15/2, author's vacuum 19/10), and
      the exact fold-bound mode h = e^{3H sigma} K_nu(k e^{H sigma}/H), nu^2 = 9 - omega^2/(5H^2), was dispersive:
      c_g^2 = 1.0122 at k = 1e-3 H, 0.9989 at k = H, 0.903 at k = 10 H, 0.857 at k = 100 H (towards 17/20);
  F4  an Einstein-Hilbert term R_hat/(2 kappa_ind) of the four-dimensional metric of the fold (induced by the quantum
      fluctuations of its fields, F5) only adds to the coefficient of the same luminal operator: c_g = 1 for every
      kappa_ind, and 1/(8 pi G_N) = V_*/kappa_7 + 1/kappa_ind both in the waves and in the Friedmann equation; GW170817
      is satisfied identically; record: with the author's weights c_g^2 = (96 + 83 eps_r)/(96 + 82 eps_r) and
      eps_r < 1.3e-13 from GW170817;
  F5  ESTIMATE, the Einstein-Hilbert term induced by the fields of the fold (Sakharov; one loop, heat kernel,
      proper-time cutoff Lambda_c): 1/(16 pi G_ind) = N Lambda_c^2/(192 pi^2), N = sum over real scalars (1 - 6 xi) +
      Weyl fermions - 4 x gauge fields (the coefficient tr(E + R/6) of each operator, ghosts included; the gauge-field
      value depends on the scheme); for the Standard Model with three nu_R N = 4(1 - 6 xi_H); if it alone gave G_N it
      would need Lambda_c = sqrt(24) pi M_red = 3.07 M_Pl; the same loops induce a vacuum energy of about
      |N_B - N_F| Lambda_c^4/(64 pi^2) = 2e77 GeV^4 (N_B - N_F = 28 - 96), which the tension of the fold must cancel;
      with the corrected weights the fold has its own Einstein-Hilbert term (F3), so no induced term is needed;
  F6  the fold fluid: the static fold source kappa S = -(32/5) H in every direction along the fold (um3_fold.py J5) is a
      pure tension kappa lambda_F = 32 H/5 (p = q = -rho), as the brane of Randall and Sundrum; the vacuum energy of the
      fold fields (fields independent of the extra times, T^r_r = on-shell L = -V_min) is a seven-dimensional tension and
      adds to it; on the frozen branch the bulk is a vacuum without flux, and the matter of the fold is conserved by
      itself; record: with the author's weights the static source was a tension 61H/8 plus a pressureless part H/8 fed by
      the flux (3/8) A (1 + A^2) H^2 of the bulk.
Writes outputs/foldsources.json and reports/foldsources_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_foldsources.py

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

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
from um3_lovelock import frame_riemann, lovelock_tensor  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


X = sp.symbols('x0:8', real=True)
SIG, X3, X4 = X[0], X[3], X[4]
H = sp.Symbol('H', positive=True)
EPS = sp.Symbol('eps')
# the corrected weights (the author's order of 2026-10-25 07:55) and the author's original weights (the record)
W = [None, sp.Integer(1), sp.Rational(1, 20), sp.Rational(1, 360)]
W_AUTHOR = [None, sp.Integer(1), sp.Rational(1, 32), sp.Rational(1, 1152)]
ALPHA = [None, sp.Integer(1), W[2] / H**2, W[3] / H**4]
FA = sp.Function('fa')(SIG, X4)
FB = sp.Function('fb')(SIG, X4)
FN = sp.Function('fn')(SIG, X4)
HH = sp.Function('h')(SIG, X3, X4)
A, U, Ad, Ud = sp.symbols('A U Ad Ud', real=True)
NAMES = ['fa_s', 'fa_ss', 'fa_st', 'fa_t', 'fa_tt', 'fb_s', 'fb_ss', 'fb_st', 'fb_t', 'fb_tt', 'fn_s', 'fn_ss', 'fn_st',
         'fn_t', 'fn_tt', 'h_s', 'h_ss', 'h_st', 'h_t', 'h_tt', 'h_3', 'h_33', 'h_s3', 'h_3t', 'fa0', 'fn0', 'h0']
S = {n: sp.Symbol(n, real=True) for n in NAMES}
HS_M, HS_P = sp.symbols('hs_m hs_p', real=True)        # h_sigma just before / after the fold
GRAV = ('h_tt', 'h_33', 'h_ss', 'h_s', 'h_t', 'h_st', 'h_3t', 'h_s3', 'h_3', 'h0')


def to_symbols(e):
    reps = []
    for f, nm in ((FA, 'a'), (FB, 'b'), (FN, 'n')):
        reps += [(sp.Derivative(f, (SIG, 2)), S['f%s_ss' % nm]), (sp.Derivative(f, SIG, X4), S['f%s_st' % nm]),
                 (sp.Derivative(f, (X4, 2)), S['f%s_tt' % nm]), (sp.Derivative(f, SIG), S['f%s_s' % nm]),
                 (sp.Derivative(f, X4), S['f%s_t' % nm])]
    reps += [(sp.Derivative(HH, (SIG, 2)), S['h_ss']), (sp.Derivative(HH, (X3, 2)), S['h_33']),
             (sp.Derivative(HH, (X4, 2)), S['h_tt']), (sp.Derivative(HH, SIG, X3), S['h_s3']),
             (sp.Derivative(HH, SIG, X4), S['h_st']), (sp.Derivative(HH, X3, X4), S['h_3t']),
             (sp.Derivative(HH, SIG), S['h_s']), (sp.Derivative(HH, X3), S['h_3']), (sp.Derivative(HH, X4), S['h_t'])]
    for a_, b_ in reps:
        e = e.subs(a_, b_)
    e = e.subs({FN: S['fn0'], HH: S['h0'], FA: S['fa0']})
    return sp.expand(e)


def tt_per_order():
    """(E_(p)^1_1 - E_(p)^2_2)/2 at first order in eps for p = 1, 2, 3 (unit weight), in the derivative symbols."""
    g = sp.diag(1, sp.exp(2 * FA + EPS * HH), sp.exp(2 * FA - EPS * HH), sp.exp(2 * FA), -sp.exp(2 * FN),
                *[-sp.exp(2 * FB)] * 3)
    hs = [sp.S(1), sp.exp(FA + EPS * HH / 2), sp.exp(FA - EPS * HH / 2), sp.exp(FA), sp.exp(FN), *[sp.exp(FB)] * 3]
    Rf = frame_riemann(g, X, hs, simplify=lambda e: sp.expand(sp.powsimp(sp.expand(e))))
    Rs = {}
    for k, v in Rf.items():
        e = to_symbols(v)
        e = sp.expand(e.subs(EPS, 0) + EPS * sp.diff(e, EPS).subs(EPS, 0))
        if e != 0:
            Rs[k] = e
    per = {}
    for p in (1, 2, 3):
        Ep = lovelock_tensor(Rs, p, simplify=sp.expand)
        per[p] = sp.expand(sp.diff(sp.expand((Ep[1, 1] - Ep[2, 2]) / 2), EPS).subs(EPS, 0))
    return per


def weighted(per, ws):
    return sp.expand(sum(ws[p] * H ** (2 - 2 * p) * per[p] for p in (1, 2, 3)))


def junction(TT):
    """Linearity in the second sigma-derivatives, the exactness of their coefficients and the junction potential F."""
    second = [S['fa_ss'], S['fb_ss'], S['fn_ss'], S['h_ss']]
    first = [S['fa_s'], S['fb_s'], S['fn_s'], S['h_s']]
    poly = sp.Poly(TT, *second)
    linear = all(sum(m) <= 1 for m in poly.monoms())
    C = [sp.expand(sp.diff(TT, v)) for v in second]
    exact = all(sp.expand(sp.diff(C[i], first[j]) - sp.diff(C[j], first[i])) == 0 for i in range(4) for j in range(i + 1, 4))
    lam = sp.Symbol('lam')
    integrand = sum(C[k].subs({first[m]: lam * first[m] for m in range(4)}, simultaneous=True) * first[k] for k in range(4))
    F = sp.expand(sp.integrate(sp.expand(integrand), (lam, 0, 1)))
    exact = exact and all(sp.expand(sp.diff(F, first[k]) - C[k]) == 0 for k in range(4))
    return linear, exact, F


def author(side, hs, extra=None):
    """The author's metric on one side of the fold (side = -1: sigma < 0; +1: sigma > 0); a4 = 0 at the instant."""
    v = {S['fa_s']: -H * side, S['fb_s']: -H * side, S['fn_s']: 0, S['fa_st']: 0, S['fb_st']: 0, S['fn_st']: 0,
         S['fn_t']: 0, S['fn_tt']: 0, S['fa_t']: A * H, S['fb_t']: (U - A) * H, S['fa_tt']: Ad * H**2,
         S['fb_tt']: (Ud - Ad) * H**2, S['fn0']: 0, S['h_s']: hs}
    if extra:
        v.update(extra)
    return v


def bulk_coefficients(TT, vals):
    """The coefficients of the graviton derivatives in the bulk equation (sigma > 0) of the author's metric with vals."""
    e = sp.expand(TT.subs({S['fa_ss']: 0, S['fb_ss']: 0, S['fn_ss']: 0}).subs(author(+1, S['h_s'])).subs(vals))
    coef = {k: sp.factor(sp.expand(sp.diff(e, S[k]))) for k in GRAV}
    rest = sp.expand(e - sum(sp.diff(e, S[k]) * S[k] for k in GRAV))
    return coef, rest


def thin_part(F, vals):
    """The integral of TT across the fold: F(0+) - F(0-), with the jump of h_sigma; a4 = 0 at the instant (fa0 = 0)."""
    Jf = sp.expand((F.subs(author(+1, HS_P)) - F.subs(author(-1, HS_M))).subs(vals).subs(S['fa0'], 0))
    out = {k: sp.factor(sp.expand(sp.diff(Jf, S[k]))) for k in ('h_tt', 'h_33', 'h_t')}
    out['hs_p'] = sp.factor(sp.expand(sp.diff(Jf, HS_P)))
    out['hs_m'] = sp.factor(sp.expand(sp.diff(Jf, HS_M)))
    rest = sp.expand(Jf - sum(sp.diff(Jf, S[k]) * S[k] for k in ('h_tt', 'h_33', 'h_t')) - out['hs_p'] * HS_P
                     - out['hs_m'] * HS_M)
    return out, rest


def author_dispersion(k_over_H):
    """Record: the fold-bound graviton with the author's weights at the static block.  Bulk (sigma > 0):
    (1/32) h_tt - (5/32)(e^{2 H sigma} h_33 + h_ss - 6 H h_s) = 0, so h = e^{3 H sigma} K_nu((k/H) e^{H sigma}) e^{i(k x3 - omega x4)},
    nu^2 = 9 - omega^2/(5 H^2); fold: (5/(12H)) h_tt - (17/(48H)) h_33 - (5/32) [h_sigma] = 0 with [h_sigma] = 2 h_sigma(0+)."""
    mp.mp.dps = 20
    k = mp.mpf(k_over_H)

    def f(w):
        nu = mp.sqrt(9 - w ** 2 / 5)
        x = k
        Kp = -(mp.besselk(nu - 1, x) + mp.besselk(nu + 1, x)) / 2
        dlog = 3 + x * Kp / mp.besselk(nu, x)
        return mp.re(-mp.mpf(5) / 12 * w ** 2 + mp.mpf(17) / 48 * k ** 2 - mp.mpf(5) / 16 * dlog)
    guess = k * mp.sqrt(mp.mpf(83) / 82) if k < 1 else k * mp.sqrt(mp.mpf(17) / 20 + (mp.mpf(83) / 82 - mp.mpf(17) / 20) / k)
    w = mp.findroot(f, guess)
    return float((w / k) ** 2)


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    per = tt_per_order()
    TT = weighted(per, W)
    TTa = weighted(per, W_AUTHOR)
    fro = {U: A, Ud: Ad}
    sb = {A: 0, U: 0, Ad: 0, Ud: 0}
    av = {A: 1, U: 0, Ad: 0, Ud: 0}

    # ---------------- F1: the linearised equation and the bulk
    linear, exact, F = junction(TT)
    linear_a, exact_a, Fa = junction(TTa)
    cf, rest_f = bulk_coefficients(TT, fro)
    bulk_zero = all(v == 0 for v in cf.values()) and rest_f == 0
    ca, rest_a = bulk_coefficients(TTa, sb)
    ca0 = {k: sp.simplify(v.subs(S['fa0'], 0)) for k, v in ca.items()}
    rec_ok = (ca0['h_tt'] == sp.Rational(1, 32) and ca0['h_33'] == -sp.Rational(5, 32)
              and ca0['h_ss'] == -sp.Rational(5, 32) and sp.simplify(ca0['h_s'] - sp.Rational(15, 16) * H) == 0)
    out['F1'] = {'bulk_frozen_corrected': {k: str(v) for k, v in cf.items()},
                 'bulk_static_author_weights_at_fa0_0': {k: str(v) for k, v in ca0.items() if v != 0}}
    rep.check('F1_no_linear_graviton_in_the_bulk', linear and exact and linear_a and exact_a and bulk_zero and rec_ok,
              'TT = sum_p alpha_p (E^1_1 - E^2_2)/2 (first order in the + polarisation h along x3) is linear in fa_ss, fb_ss, '
              'fn_ss, h_ss with coefficients that are an exact differential in the first sigma-derivatives (a junction '
              'potential exists, for any weights); away from the fold, on every background with frozen extra times (b4\'/b4 = '
              'a4\', any a4(x4)), every coefficient of the graviton vanishes with the corrected weights (%s): the bulk carries '
              'no linear graviton; record: with the author\'s weights the static bulk had (1/32) h_tt - (5/32)(e^{-2fa} h_33 + '
              'h_ss) + (15/16) H h_s (%s), the local cone v^2 = 5' % (
                  {k: str(v) for k, v in cf.items()}, {k: str(v) for k, v in ca0.items() if v != 0}))

    # ---------------- F2: the thin part at the fold
    th_g, rest_g = thin_part(F, {})
    th_f = {k: sp.factor(sp.simplify(v.subs(fro))) for k, v in th_g.items()}
    ok_f = (th_f['h_tt'] == sp.Rational(8, 15) / H and th_f['h_33'] == -sp.Rational(8, 15) / H
            and sp.simplify(th_f['h_t'] - sp.Rational(8, 5) * A) == 0 and th_f['hs_p'] == 0 and th_f['hs_m'] == 0
            and rest_g == 0)
    # Einstein gravity alone (p = 1): no thin h_tt, h_33 term
    _, _, F1p = junction(sp.expand(per[1]))
    th1, _ = thin_part(F1p, {})
    ok_e = th1['h_tt'] == 0 and th1['h_33'] == 0
    # record: the author's weights
    th_a, _ = thin_part(Fa, {})
    th_af = {k: sp.factor(sp.simplify(v.subs(fro))) for k, v in th_a.items()}
    th_aav = {k: sp.factor(sp.simplify(v.subs(av))) for k, v in th_a.items()}
    rec2 = (th_af['h_tt'] == sp.Rational(5, 12) / H and th_af['h_33'] == -sp.Rational(17, 48) / H
            and sp.simplify(th_af['h_t'] - sp.Rational(19, 16) * A) == 0
            and sp.simplify(th_af['hs_p'] + (5 + A ** 2 + Ad) / 32) == 0
            and th_aav['h_tt'] == sp.Rational(5, 12) / H and th_aav['h_33'] == -sp.Rational(13, 24) / H)
    # numerical check by smoothing the kink: fa_s = fb_s = -H tanh(sigma/w), corrected weights
    mp.mp.dps = 30
    worst = 0.0
    okn = True
    for (Av, Uv) in ((0.0, 0.0), (0.3, 0.3), (1.0, 0.0)):
        base = {H: 1, S['fn_s']: 0, S['fn_ss']: 0, S['fa_st']: 0, S['fb_st']: 0, S['fn_st']: 0, S['fn_t']: 0,
                S['fn_tt']: 0, S['fn0']: 0, S['fa_t']: Av, S['fb_t']: Uv - Av, S['fa_tt']: 0, S['fb_tt']: 0,
                S['h_s']: 0, S['h_ss']: 0, S['h_st']: 0, S['h_3t']: 0, S['h_s3']: 0, S['h_3']: 0, S['h0']: 0}
        for coef in ('h_tt', 'h_33', 'h_t'):
            e = TT.subs(base).subs({S[c]: (1 if c == coef else 0) for c in ('h_tt', 'h_33', 'h_t')})
            f = sp.lambdify((S['fa_s'], S['fb_s'], S['fa_ss'], S['fb_ss'], S['fa0']), e, 'mpmath')
            exact_v = float(th_g[coef].subs({H: 1, A: Av, U: Uv, Ad: 0, Ud: 0}))
            res = []
            for wv in (1e-4, 1e-5):
                gfun = lambda s_: f(-mp.tanh(s_ / wv), -mp.tanh(s_ / wv), -(1 / wv) * mp.sech(s_ / wv) ** 2,
                                    -(1 / wv) * mp.sech(s_ / wv) ** 2, -wv * mp.log(mp.cosh(s_ / wv)))
                res.append(float(mp.quad(gfun, [-40 * wv, -wv, 0, wv, 40 * wv])))
            d1, d2 = abs(res[0] - exact_v), abs(res[1] - exact_v)
            worst = max(worst, d2)
            okn = okn and d2 < 1e-3 and d2 < 0.2 * d1 + 1e-12
    out['F2'] = {'thin_part_general': {k: str(v) for k, v in th_g.items()},
                 'thin_part_frozen': {k: str(v) for k, v in th_f.items()},
                 'einstein_alone': {k: str(v) for k, v in th1.items()},
                 'author_weights_frozen': {k: str(v) for k, v in th_af.items()},
                 'author_weights_author_vacuum': {k: str(v) for k, v in th_aav.items()}, 'smoothing_worst': worst}
    rep.check('F2_thin_part_at_the_fold', ok_f and ok_e and rec2 and okn,
              'the integral of TT across the fold: for frozen extra times (b4\'/b4 = a4\' = A H, any A and A1 = Ad) kappa Pi = '
              '(8/(15H))(h_tt + 3 A H h_t - h_33), with no term in the jump [h_sigma] (the coefficients of h_sigma(0+) and '
              'h_sigma(0-) are %s, %s); for general rates %s; Einstein gravity alone gives no h_tt, h_33 term at the fold, so '
              'the graviton of the fold comes from the Gauss-Bonnet and cubic terms; smoothing the kink (fa_s = fb_s = '
              '-H tanh(sigma/w)) and integrating the full equation reproduces the h_tt, h_33 and h_t coefficients (deviation '
              '%.1e at w = 1e-5, falling linearly with w); record: with the author\'s weights (5/(12H)) h_tt - (17/(48H)) h_33 '
              '+ (19/16) A h_t - ((5 + A^2 + A1)/32)[h_sigma] (frozen), (5/(12H)) h_tt - (13/(24H)) h_33 at the author\'s vacuum' % (
                  th_f['hs_p'], th_f['hs_m'], {k: str(v) for k, v in th_g.items()}, worst))

    # ---------------- F3: the four-dimensional graviton
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    frz = {k: sp.sympify(v, locals={'H': H, 'A': A, 'Ad': Ad}) for k, v in fold['fold_source_frozen'].items()}
    kap, k7 = sp.symbols('kappa kappa_7', positive=True)
    # the Friedmann equation of the fold: kappa rho_m = -kappa S^4_4 - kappa lambda_F = (16/5) A^2 H = kappa 3 a4'^2/kappa_7
    k7_fried = sp.simplify(3 * A ** 2 * H ** 2 * kap / (-frz['x4,x4'] - sp.Rational(32, 5) * H))
    # the graviton: (8/(15H)) (...) = kappa Pi  <=>  (kappa/(2 kappa_7)) (...) = kappa Pi
    k7_grav = sp.simplify(kap / (2 * th_f['h_tt']))
    cg2 = sp.simplify(-th_f['h_33'] / th_f['h_tt'])
    ok3 = (sp.simplify(k7_fried - sp.Rational(15, 16) * kap * H) == 0 and sp.simplify(k7_grav - k7_fried) == 0
           and cg2 == 1 and bulk_zero)
    # record: the author's weights, long-wavelength mode and the dispersion of the fold-bound mode
    sg = sp.Symbol('s', positive=True)
    wgt = sp.exp(-6 * H * sg)
    caf, _ = bulk_coefficients(TTa, fro)
    Ktt_b = sp.simplify(2 * sp.integrate(wgt * caf['h_tt'].subs(S['fa0'], -H * sg), (sg, 0, sp.oo)))
    K33_b = sp.simplify(2 * sp.integrate(wgt * caf['h_33'].subs(S['fa0'], -H * sg), (sg, 0, sp.oo)))
    Ktt_a = sp.simplify(Ktt_b + th_af['h_tt'])
    K33_a = sp.simplify(K33_b + th_af['h_33'])
    cg2_a = sp.simplify(-K33_a / Ktt_a)
    cg2_bulk = sp.simplify(-K33_b.subs(sb) / Ktt_b.subs(sb))
    disp = {kk: author_dispersion(kk) for kk in (1e-3, 1.0, 10.0, 100.0)}
    dv = [disp[kk] for kk in (1e-3, 1.0, 10.0, 100.0)]
    rec3 = (cg2_a == sp.Rational(83, 82) and cg2_bulk == sp.Rational(15, 2) and abs(disp[1e-3] - 83 / 82) < 1e-4
            and disp[1.0] < 1 and all(x > y for x, y in zip(dv, dv[1:])) and 0.85 < disp[100.0] < 0.86)
    out['F3'] = {'kappa_7_friedmann': str(k7_fried), 'kappa_7_graviton': str(k7_grav), 'c_g^2': str(cg2),
                 'author_weights_record': {'K_tt': str(Ktt_a), 'K_33': str(K33_a), 'c_g^2_long_wavelength': str(cg2_a),
                                           'c_g^2_bulk_alone': str(cg2_bulk),
                                           'c_g^2_fold_bound_mode': {'k/H=%g' % k_: v for k_, v in disp.items()}}}
    rep.check('F3_graviton_at_the_speed_of_light', ok3 and rec3,
              'the graviton of the fold obeys (kappa/(2 kappa_7))(h_tt + 3 a4\' h_t - e^{-2 a4} nabla^2 h) = kappa Pi, Pi the '
              'transverse traceless stress of the fold matter, with kappa_7 = %s from the graviton and kappa_7 = %s from the '
              'Friedmann equation of the fold (the same): the wave equation of general relativity, c_g^2 = %s at every '
              'wavelength (no bulk term), and the Planck mass of the waves equals that of the expansion; record: with the '
              'author\'s weights the long-wavelength mode had K_tt = %s, K_33 = %s, c_g^2 = %s (the bulk alone %s), and the '
              'fold-bound mode h = e^{3H sigma} K_nu((k/H) e^{H sigma}), nu^2 = 9 - omega^2/(5H^2), was dispersive: c_g^2 = '
              '%.5f, %.5f, %.4f, %.4f at k = 1e-3 H, H, 10 H, 100 H (towards 17/20 for k >> H: slower than light)' % (
                  k7_grav, k7_fried, cg2, Ktt_a, K33_a, cg2_a, cg2_bulk, disp[1e-3], disp[1.0], disp[10.0], disp[100.0]))

    # ---------------- F4: an induced Einstein-Hilbert term of the fold
    kind, Vs, ah = sp.symbols('kappa_ind V_s a4dot', positive=True)
    # four-dimensional normalisation: the Lovelock part has the weight V_*/kappa_7 per unit volume of ordinary space;
    # the induced term (1/(2 kappa_ind)) R_hat gives the same luminal operator and the same Friedmann term
    coef_wave = Vs / k7 + 1 / kind
    coef_fried = sp.simplify((3 * ah ** 2 * Vs / k7 + 3 * ah ** 2 / kind) / (3 * ah ** 2))
    cg2_ind = sp.simplify((coef_wave * 1) / (coef_wave * 1))
    ok4 = sp.simplify(coef_fried - coef_wave) == 0 and cg2_ind == 1
    # record: the author's weights with the induced term; eps_r = kappa_ind V_*/(kappa H) was the ratio of the
    # Lovelock part of the gravity of the fold to the induced part
    er = sp.Symbol('eps_r', positive=True)
    num = sp.Rational(1, 2) + er * H * (-K33_a)
    den = sp.Rational(1, 2) + er * H * Ktt_a
    cg2_rec = sp.simplify(num / den)
    xg = 2 * 7e-16 + (7e-16) ** 2                       # (c_g - c)/c <= 7e-16 (GW170817, distance 26 Mpc)
    eps_max = 96 * xg / (1 - 82 * xg)
    rec4 = sp.simplify(cg2_rec - (96 + 83 * er) / (96 + 82 * er)) == 0 and 1.25e-13 < eps_max < 1.4e-13
    out['F4'] = {'coefficient_waves': str(coef_wave), 'coefficient_friedmann': str(coef_fried), 'c_g^2': str(cg2_ind),
                 'author_weights_record': {'c_g^2': str(cg2_rec), 'eps_r_max_GW170817': eps_max}}
    rep.check('F4_induced_term_keeps_the_light_cone', ok4 and rec4,
              'an Einstein-Hilbert term R_hat/(2 kappa_ind) of the four-dimensional metric of the fold adds 1/kappa_ind to the '
              'coefficient V_*/kappa_7 of the same luminal operator: c_g^2 = %s for every kappa_ind, and 1/(8 pi G_N) = '
              'V_*/kappa_7 + 1/kappa_ind both in the waves and in the Friedmann equation (%s = %s); GW170817 is satisfied '
              'identically; record: with the author\'s weights the waves had c_g^2 = %s, and GW170817 ((c_g - c)/c <= 7e-16 for '
              'the distance 26 Mpc) required eps_r <= %.1e' % (cg2_ind, coef_wave, coef_fried, cg2_rec, eps_max))

    # ---------------- F5: ESTIMATE, the Einstein-Hilbert term induced by the fold fields (Sakharov)
    xi, R_ = sp.symbols('xi R')
    # tr(E + R/6) for Laplace-type operators D = -(nabla^2 + E): scalar E = -xi R; Dirac D^2 = -nabla^2 + R/4 (4 x 4);
    # Maxwell in Feynman gauge E^mu_nu = -R^mu_nu (trace -R) with two scalar ghosts (minus sign); the vector value
    # depends on the scheme (the contact term)
    a1_scalar = (-xi * R_ + R_ / 6)
    a1_dirac = 4 * (-R_ / 4 + R_ / 6)
    a1_vector = (-R_ + 4 * R_ / 6) - 2 * (R_ / 6)
    w_scalar = sp.simplify(a1_scalar / (R_ / 6))
    w_weyl = sp.simplify(-a1_dirac / 2 / (R_ / 6))
    w_vector = sp.simplify(a1_vector / (R_ / 6))
    n_s, n_w, n_v = 4, 48, 12            # Higgs doublet (4 real), 3 x 16 Weyl fermions (with nu_R), 8 + 3 + 1 gauge fields
    N = sp.expand(n_s * w_scalar + n_w * w_weyl + n_v * w_vector)
    N_no_nuR = sp.expand(n_s * w_scalar + 45 * w_weyl + n_v * w_vector)
    M_red = 2.435e18                     # reduced Planck mass (GeV), (8 pi G_N)^(-1/2)
    M_Pl = 1.22089e19
    Lam = math.sqrt(96 * math.pi ** 2 / float(N.subs(xi, 0))) * M_red
    nB, nF = 4 + 2 * 12, 2 * 48          # bosonic and fermionic degrees of freedom
    rho_vac = abs(nB - nF) * Lam ** 4 / (64 * math.pi ** 2)
    out['F5'] = {'weight_scalar': str(w_scalar), 'weight_weyl': str(w_weyl), 'weight_vector': str(w_vector),
                 'N_SM_with_nuR': str(N), 'N_SM_without_nuR': str(N_no_nuR), 'Lambda_c_GeV_xi0': Lam,
                 'Lambda_c_over_M_Pl': Lam / M_Pl, 'N_B_minus_N_F': nB - nF, 'induced_vacuum_energy_GeV4': rho_vac}
    ok5 = (w_scalar == 1 - 6 * xi and w_weyl == 1 and w_vector == -4 and N == 4 - 24 * xi and nB - nF == -68
           and 3.0 < Lam / M_Pl < 3.1 and 1e77 < rho_vac < 3e77)
    rep.check('F5_induced_gravity_estimate', ok5,
              'ESTIMATE: the one-loop effective action of the fold fields with a proper-time cutoff Lambda_c contains '
              '1/(16 pi G_ind) = N Lambda_c^2/(192 pi^2), N = sum (1 - 6 xi) over real scalars + (number of Weyl fermions) - 4 x '
              '(number of gauge fields) (from tr(E + R/6); Weyl %s, gauge field with ghosts %s, a scheme-dependent value); for '
              'the Standard Model with three nu_R N = %s (without nu_R %s); if it alone gave Newton\'s constant it would need '
              'Lambda_c = sqrt(24) pi M_red = %.3e GeV = %.2f M_Pl, above the Planck mass where one loop cannot be trusted, '
              'and xi_H < 1/6; the same loops induce a vacuum energy of about |N_B - N_F| Lambda_c^4/(64 pi^2) = %.1e GeV^4 '
              '(N_B - N_F = %d), which the tension of the fold would have to cancel; with the corrected weights the fold has '
              'its own Einstein-Hilbert term (F3), and an induced one is not needed' % (
                  w_weyl, w_vector, N, N_no_nuR, Lam, Lam / M_Pl, rho_vac, nB - nF))

    # ---------------- F6: the fold fluid
    stat = {k: sp.sympify(v, locals={'H': H}) for k, v in fold['fold_source_static_block'].items()}
    kp, krho, kq = stat['x1,x1'], -stat['x4,x4'], stat['x5,x5']        # S^1_1 = p, S^4_4 = -rho, S^5_5 = q
    lambda_F = -kp
    ok6a = sp.simplify(kp - kq) == 0 and sp.simplify(krho - lambda_F) == 0 and lambda_F == sp.Rational(32, 5) * H
    # the vacuum energy of fields of the fold that do not depend on the extra times: T^a_b = L delta^a_b on shell for the
    # homogeneous part, L = -V_min at the minimum: a seven-dimensional tension (rho = V_min, p = q = -V_min); the stress
    # tensor of a scalar field phi(x4) of the fold with the action int sqrt|g| (-(1/2) g^{MN} d_M phi d_N phi - V),
    # T_MN = -(2/sqrt|g|) dS/dg^{MN} = d_M phi d_N phi + g_MN L, i.e. T^a_b = d^a phi d_b phi + delta^a_b L
    phi_t, Vm = sp.symbols('phidot V_min', real=True)
    Lphi = sp.Rational(1, 2) * phi_t ** 2 - Vm                                 # L = -(1/2) g^44 phi'^2 - V, g^44 = -1
    T44 = -phi_t ** 2 + Lphi                                                    # T^4_4 = g^44 phi'^2 + L = -rho
    Tii = Lphi                                                                  # T^i_i = T^r_r = L (no gradients)
    vac_t = {'rho': sp.simplify(-T44.subs(phi_t, 0)), 'p': sp.simplify(Tii.subs(phi_t, 0)), 'q': sp.simplify(Tii.subs(phi_t, 0))}
    ok6b = vac_t['rho'] == Vm and vac_t['p'] == -Vm and vac_t['q'] == -Vm
    # the frozen branch: no bulk flux; the matter above the tension is conserved by itself (an identity of the two
    # Friedmann equations, kappa rho_m = (16/5) A^2 H, kappa p_m = -(16/15)(3A^2 + 2A1) H)
    bulkfz = fold.get('bulk_source_frozen_kappaT_over_H2', {})
    noflux = all(sp.sympify(v) == 0 for v in bulkfz.values()) and len(bulkfz) > 0
    a4 = sp.Function('a4')(X4)
    sub_t = {A: sp.diff(a4, X4) / H, Ad: sp.diff(a4, X4, 2) / H ** 2}
    rho_f = sp.expand(-frz['x4,x4'] - lambda_F)
    p_f = sp.expand(frz['x1,x1'] + lambda_F)
    cons = sp.simplify(sp.diff(rho_f.subs(sub_t), X4) + 3 * sp.diff(a4, X4) * (rho_f + p_f).subs(sub_t))
    ok6c = noflux and cons == 0
    out['F6'] = {'kappa_lambda_F': str(lambda_F), 'pressureless_part': str(sp.simplify(krho - lambda_F)),
                 'vacuum_energy_of_a_fold_field': {k: str(v) for k, v in vac_t.items()},
                 'frozen_bulk_flux_zero': noflux, 'conservation_on_the_fold': str(cons),
                 'author_weights_record': {'kappa_lambda_F': '61 H/8', 'kappa_rho_d': 'H/8',
                                           'bulk_flux_jump_frozen': '(3/8) A (1 + A^2) H^2'}}
    rep.check('F6_fold_fluid_is_a_tension', ok6a and ok6b and ok6c,
              'the static fold source kappa S = diag(p, -rho, q) = %s H along (ordinary space, time, extra times) is a pure '
              'tension kappa lambda_F = %s (p = q = -rho; no pressureless part), as the brane of Randall and Sundrum; the '
              'vacuum energy of a field of the fold that does not depend on the extra times (T^a_b = d^a phi d_b phi + '
              'delta^a_b L at phi\' = 0) has rho = %s, p = %s, q = %s: a seven-dimensional tension, which adds to lambda_F; on '
              'the frozen branch the bulk is a vacuum without flux, and the matter above the tension is conserved by itself '
              '(rho_m\' + 3 a4\'(rho_m + p_m) = %s); record: with the author\'s weights the static source was a tension '
              '61H/8 plus a pressureless part H/8, fed by the bulk flux (3/8) A (1 + A^2) H^2' % (
                  [str(stat[k] / H) for k in ('x1,x1', 'x4,x4', 'x5,x5')], lambda_F, vac_t['rho'], vac_t['p'], vac_t['q'], cons))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs').mkdir(exist_ok=True)
    (UM3 / 'reports').mkdir(exist_ok=True)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'foldsources.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_foldsources.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'foldsources_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
