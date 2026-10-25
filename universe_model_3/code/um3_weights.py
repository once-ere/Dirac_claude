#!/usr/bin/env python3
"""um3_weights.py - the Lovelock weights for which gravitons travel at the speed of light, and what they imply.

The author's metric in the proper chart of the hidden direction (sigma the signed proper distance from the fold):
    ds^2 = d sigma^2 + e^{2 fa} (dx1^2 + dx2^2 + dx3^2) - e^{2 fn} dx4^2 - e^{2 fb} (dx5^2 + dx6^2 + dx7^2),
    fa = a4(x4) - H|sigma|,  fb = ln b4(x4) - a4(x4) - H|sigma|,  fn = 0,
and Einstein-Lovelock gravity in eight dimensions, sum_{p=1}^{3} alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b, with
alpha_(p) = w_(p) H^{2-2p}, w_(1) = 1 and the weights w2 = w_(2), w3 = w_(3) and Lambda = lam H^2 left free (in eight
dimensions the Lovelock term of order 4 is a total derivative and adds nothing).  A = a4'/H, U = b4'/(H b4) (the rate of the
extra times is U - A), A1 = A'/H.  The author's weights were w2 = 1/32, w3 = 1/1152, Lambda = -10 H^2.

Checks:
  W1  the bulk graviton: the linearised equation of a transverse traceless wave of the + polarisation in ordinary space
      (g_11 = e^{2 fa + eps h}, g_22 = e^{2 fa - eps h}, h = h(sigma, x3, x4); TT = (E^1_1 - E^2_2)/2 at first order in eps)
      on the static block (A = U = 0) is, away from the fold,
          (c_t/2) h_tt - (c_x/2) (e^{2H|sigma|} h_33 + h_ss - 6 H sgn(sigma) h_s),
          c_t = 1 - 40 w2 + 360 w3,   c_x = 1 - 24 w2 + 72 w3,
      and the + polarisation in the extra times (g_55, g_66) has the same coefficients: bulk gravitons move with the local
      speed sqrt(c_x/c_t) times that of light; with the author's weights c_t = 1/16, c_x = 5/16: sqrt 5;
  W2  the graviton of the fold: the integral of TT across the fold (the jump of its junction potential) at the static
      block is (16 (w2 - 6 w3) h_tt - 12 (w2 - 2 w3) h_33)/H - (c_x/2) [h_s]; the long-wavelength mode (flat in sigma,
      weight sqrt|g| = e^{-6H|sigma|}) has K_tt = c_t/(6H) + 16 (w2 - 6 w3)/H and K_33 = c_x/(4H) + 12 (w2 - 2 w3)/H, and
      K_tt - K_33 = -c_t/(12 H) for every w2, w3: it travels at the speed of light only if c_t = 0; with the author's
      weights c_g^2 = K_33/K_tt = 83/82;
  W3  the unique weights: no bulk graviton faster than light and a graviton of the fold at the speed of light require
      c_t = c_x = 0, whose only solution is w2 = 1/20, w3 = 1/360 (c_t = 0 with c_x != 0 would give bulk gravitons of
      infinite speed);
  W4  with w2 = 1/20, w3 = 1/360 the static block needs sum alpha_p E_(p) + Lambda = (7 + lam) H^2 delta^a_b, the same in
      every direction: Lambda = -7 H^2 makes it a vacuum; order by order (warped directions, time)/H^2: Einstein (15, 21),
      Gauss-Bonnet (-9, -21), cubic (1, 7), Lambda (-7, -7); on the family of spaces of constant curvature -y H^2 times the
      time line the left-hand side is (y - 1)^2 (y - 7) H^2 (warped) and 7 (y - 1)^3 H^2 (time): the static block (y = 1) is a
      degenerate vacuum;
  W5  the bulk equations of the author's metric with the corrected weights and Lambda = -7 H^2, any a4(x4), b4(x4):
      kappa T^(4)_(4) = A^3 (A - U)^3 H^2 and kappa T^(0)_(4) = 3 A^2 U (A - U)^2 H^2 sgn(sigma) (no second time derivative);
      every one of the 64 components on both sides of the fold vanishes for frozen extra times (U = A, U1 = A1, any a4(x4))
      and for static ordinary space (A = 0, any b4(x4)); with constant rates these are the only vacua; the author's vacuum
      (A = 1, U = 0) would need the bulk energy density kappa rho_bulk = -H^2;
  W6  the fold with the corrected weights, frozen extra times, any a4(x4): kappa S^(i)_(i) = -(16/15)(6 + 3A^2 + 2A1) H,
      kappa S^(4)_(4) = -(16/5)(2 + A^2) H, kappa S^(r)_(r) = -(4/5)(8 + 8A^2 + A^4 + 4A1 + A^2 A1) H: at the static block a pure
      tension, kappa lambda_F = 32 H/5 (as the brane of Randall and Sundrum), and above it rho_m = 3 a4'^2/kappa_7 and
      p_m = -(2 a4'' + 3 a4'^2)/kappa_7 with kappa_7 = 15 kappa H/16: the two Friedmann equations of four-dimensional general
      relativity; the matter of the fold is conserved by itself (no flow from the bulk); the extra-time component
      requires the pressure q_m = -(4/5)(8A^2 + A^4 + 4A1 + A^2 A1) H/kappa along the extra times;
  W7  the graviton of the fold with the corrected weights on every frozen background: the bulk operator of W1 vanishes
      identically (h_tt, h_33, h_ss, h_s, h_t: no linear propagation in the bulk), the thin part is
      (8/(15H)) (h_tt + 3 A H h_t - h_33) with no [h_s] term: the graviton of four-dimensional general relativity,
      (1/(2 kappa_7)) (h_tt + 3 a4' h_t - e^{-2 a4} nabla^2 h), with the same kappa_7 as W6: gravitational waves on the fold
      travel at the speed of light at every wavelength;
  W8  the record of the author's weights (1/32, 1/1152, Lambda = -10 H^2): the author's vacuum is a vacuum solution; there
      the bulk graviton has no time-kinetic term (c_t = 0 at the author's vacuum) but a spatial one; the static block needs
      the source H^2 diag(-5/16, -5/16, -5/16, -5/16, 1/16, -5/16, -5/16, -5/16) (the stabiliser), and the frozen expanding
      bulk needs a source as well.
Writes outputs/weights.json and reports/weights_checks.json.  Runs in about a minute.
Usage: python universe_model_3/code/um3_weights.py

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
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_fold as FO            # noqa: E402
import um3_foldsources as FS     # noqa: E402
from um3_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

w2, w3, lam = sp.symbols('w2 w3 lam', real=True)
H = FO.H
A, U, Ad, Ud = FO.A, FO.U, FO.Ad, FO.Ud
W_NEW = (sp.Rational(1, 20), sp.Rational(1, 360), -7)
W_AUTHOR = (sp.Rational(1, 32), sp.Rational(1, 1152), -10)


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


def tt_per_order(pol):
    """The linearised + polarisation in the frame pair pol = (1, 2) (ordinary space) or (5, 6) (extra times), travelling
    along x3: the unweighted first-order parts of (E_(p)^i_i - E_(p)^j_j)/2, p = 1, 2, 3, in the derivative symbols of
    um3_foldsources.py."""
    X, SIG, X4 = FS.X, FS.SIG, FS.X4
    FA, FB, FN, HH, EPS = FS.FA, FS.FB, FS.FN, FS.HH, FS.EPS
    diag = [sp.S(1), sp.exp(2 * FA), sp.exp(2 * FA), sp.exp(2 * FA), -sp.exp(2 * FN), -sp.exp(2 * FB), -sp.exp(2 * FB),
            -sp.exp(2 * FB)]
    hs = [sp.S(1), sp.exp(FA), sp.exp(FA), sp.exp(FA), sp.exp(FN), sp.exp(FB), sp.exp(FB), sp.exp(FB)]
    i, j = pol
    diag[i] = diag[i] * sp.exp(EPS * HH)
    diag[j] = diag[j] * sp.exp(-EPS * HH)
    hs[i] = hs[i] * sp.exp(EPS * HH / 2)
    hs[j] = hs[j] * sp.exp(-EPS * HH / 2)
    g = sp.diag(*diag)
    Rf = frame_riemann(g, X, hs, simplify=lambda e: sp.expand(sp.powsimp(sp.expand(e))))
    Rs = {}
    for k, v in Rf.items():
        e = FS.to_symbols(v)
        e = sp.expand(e.subs(EPS, 0) + EPS * sp.diff(e, EPS).subs(EPS, 0))
        if e != 0:
            Rs[k] = e
    per = {}
    for p in (1, 2, 3):
        Ep = lovelock_tensor(Rs, p, simplify=sp.expand)
        per[p] = sp.expand(sp.diff(sp.expand((Ep[i, i] - Ep[j, j]) / 2), EPS).subs(EPS, 0))
    return per


def split(per):
    """For each order: the part without second sigma-derivatives (bulk), and the junction potential F with
    dF/d(first derivative) = the coefficient of the second derivative (for the thin part)."""
    S = FS.S
    second = [S['fa_ss'], S['fb_ss'], S['fn_ss'], S['h_ss']]
    first = [S['fa_s'], S['fb_s'], S['fn_s'], S['h_s']]
    lam_ = sp.Symbol('lam_')
    out = {}
    for p, e in per.items():
        C = [sp.expand(sp.diff(e, v)) for v in second]
        smooth = sp.expand(e - sum(c * v for c, v in zip(C, second)))
        integrand = sum(C[k].subs({first[m]: lam_ * first[m] for m in range(4)}, simultaneous=True) * first[k]
                        for k in range(4))
        F = sp.expand(sp.integrate(sp.expand(integrand), (lam_, 0, 1)))
        out[p] = (smooth, F, C[3])
    return out


def weighted(p, ws):
    return {1: sp.S(1), 2: ws[0] / H ** 2, 3: ws[1] / H ** 4}[p]


def bulk_coeffs(parts, vals, ws):
    S = FS.S
    tot = {nm: sp.S(0) for nm in ('h_tt', 'h_33', 'h_ss', 'h_s', 'h_t')}
    for p in (1, 2, 3):
        smooth, F, Css = parts[p]
        sub = FS.author(+1, S['h_s'], {S['h_st']: 0})
        b = sp.expand(smooth.subs(sub).subs(vals).subs(S['fa0'], 0))
        css = sp.expand(Css.subs(sub).subs(vals).subs(S['fa0'], 0))
        for nm in ('h_tt', 'h_33', 'h_s', 'h_t'):
            tot[nm] += weighted(p, ws) * sp.diff(b, S[nm])
        tot['h_ss'] += weighted(p, ws) * css
    return {k: sp.factor(sp.simplify(v)) for k, v in tot.items()}


def thin_coeffs(parts, vals, ws):
    S = FS.S
    tot = sp.S(0)
    for p in (1, 2, 3):
        smooth, F, Css = parts[p]
        tot += weighted(p, ws) * sp.expand(F.subs(FS.author(+1, FS.HS_P)).subs(vals) - F.subs(FS.author(-1, FS.HS_M)).subs(vals))
    tot = sp.expand(tot.subs(S['fa0'], 0))
    out = {nm: sp.factor(sp.simplify(sp.diff(tot, S[nm]))) for nm in ('h_tt', 'h_33', 'h_t')}
    out['hs_p'] = sp.factor(sp.simplify(sp.diff(tot, FS.HS_P)))
    out['hs_m'] = sp.factor(sp.simplify(sp.diff(tot, FS.HS_M)))
    return out


def lhs_matrix(E, ws, lamv, vals, side):
    """sum_p alpha_p E_(p)^a_b + Lambda delta^a_b over H^2 for the author's metric on one side of the fold (polynomials in
    the rates; expand is enough, the exponentials of the metric drop out of the frame components)."""
    M = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            e = E[1][i, j] + ws[0] / H ** 2 * E[2][i, j] + ws[1] / H ** 4 * E[3][i, j] + (lamv * H ** 2 if i == j else 0)
            M[i, j] = sp.expand(sp.expand(e.subs(FO.author_values(side)).subs(vals)) / H ** 2)
    return M


def main():
    t0 = time.time()
    rep = Report()
    out = {'weights_author': [str(x) for x in W_AUTHOR], 'weights_corrected': [str(x) for x in W_NEW]}
    sym = (w2, w3)
    st = {A: 0, U: 0, Ad: 0, Ud: 0}
    fro = {U: A, Ud: Ad}
    av = {A: 1, U: 0, Ad: 0, Ud: 0}

    # ---------------- W1: the bulk graviton at the static block, general weights, both polarisations
    parts12 = split(tt_per_order((1, 2)))
    parts56 = split(tt_per_order((5, 6)))
    b12 = bulk_coeffs(parts12, st, sym)
    b56 = bulk_coeffs(parts56, st, sym)
    c_t = 1 - 40 * w2 + 360 * w3
    c_x = 1 - 24 * w2 + 72 * w3
    ok1 = (sp.simplify(b12['h_tt'] - c_t / 2) == 0 and sp.simplify(b12['h_33'] + c_x / 2) == 0
           and sp.simplify(b12['h_ss'] + c_x / 2) == 0 and sp.simplify(b12['h_s'] - 3 * H * c_x) == 0 and b12['h_t'] == 0
           and all(sp.simplify(b56[k] - b12[k]) == 0 for k in b12))
    ct_a, cx_a = c_t.subs({w2: W_AUTHOR[0], w3: W_AUTHOR[1]}), c_x.subs({w2: W_AUTHOR[0], w3: W_AUTHOR[1]})
    out['W1'] = {'bulk_static_pol_12': {k: str(v) for k, v in b12.items()}, 'bulk_static_pol_56': {k: str(v) for k, v in b56.items()},
                 'c_t': str(c_t), 'c_x': str(c_x), 'author_c_t': str(ct_a), 'author_c_x': str(cx_a),
                 'author_local_speed_squared': str(cx_a / ct_a)}
    rep.check('W1_bulk_graviton', ok1 and ct_a == sp.Rational(1, 16) and cx_a == sp.Rational(5, 16),
              'static block, away from the fold: TT = (c_t/2) h_tt - (c_x/2)(e^{2H|sigma|} h_33 + h_ss - 6H sgn(sigma) h_s) with '
              'c_t = %s, c_x = %s, the same for the + polarisation in the extra times: the local speed of bulk gravitons is '
              'sqrt(c_x/c_t); with the author\'s weights c_t = %s, c_x = %s: v^2 = %s' % (c_t, c_x, ct_a, cx_a, cx_a / ct_a))

    # ---------------- W2: the graviton of the fold at long wavelengths, general weights
    t12 = thin_coeffs(parts12, st, sym)
    th_t = 16 * (w2 - 6 * w3) / H
    th_x = 12 * (w2 - 2 * w3) / H
    ok2a = (sp.simplify(t12['h_tt'] - th_t) == 0 and sp.simplify(t12['h_33'] + th_x) == 0 and t12['h_t'] == 0
            and sp.simplify(t12['hs_p'] + c_x / 2) == 0 and sp.simplify(t12['hs_m'] - c_x / 2) == 0)
    sg = sp.Symbol('s', positive=True)
    # the flat profile: bulk coefficients at depth s carry the frame factors (h_33 with e^{2Hs}) and the weight e^{-6Hs}
    Ktt = sp.simplify(2 * sp.integrate(sp.exp(-6 * H * sg) * c_t / 2, (sg, 0, sp.oo)) + th_t)
    K33 = sp.simplify(2 * sp.integrate(sp.exp(-6 * H * sg) * sp.exp(2 * H * sg) * c_x / 2, (sg, 0, sp.oo)) + th_x)
    diffK = sp.simplify(Ktt - K33 + c_t / (12 * H))
    cg2_a = sp.simplify((K33 / Ktt).subs({w2: W_AUTHOR[0], w3: W_AUTHOR[1]}))
    out['W2'] = {'thin_static': {k: str(v) for k, v in t12.items()}, 'K_tt': str(Ktt), 'K_33': str(K33),
                 'K_tt_minus_K_33': str(sp.factor(Ktt - K33)), 'author_c_g_squared': str(cg2_a)}
    rep.check('W2_graviton_of_the_fold', ok2a and diffK == 0 and cg2_a == sp.Rational(83, 82),
              'thin part at the static block: %s h_tt - %s h_33 - (c_x/2)[h_s]; the long-wavelength mode has K_tt = %s, '
              'K_33 = %s, K_tt - K_33 = %s for all weights: the graviton of the fold travels at the speed of light only if '
              'c_t = 0; with the author\'s weights c_g^2 = %s' % (th_t, th_x, Ktt, K33, sp.factor(Ktt - K33), cg2_a))

    # ---------------- W3: the unique weights
    sol = sp.solve([sp.Eq(c_t, 0), sp.Eq(c_x, 0)], [w2, w3], dict=True)
    ok3 = sol == [{w2: W_NEW[0], w3: W_NEW[1]}]
    out['W3'] = {'solutions': [{str(k): str(v) for k, v in s_.items()} for s_ in sol]}
    rep.check('W3_unique_weights', ok3,
              'c_t = c_x = 0 has the single solution %s: no bulk graviton faster than light and a luminal graviton of the fold '
              'fix the weights uniquely (c_t = 0 alone, with c_x != 0, would make bulk gravitons infinitely fast)' % sol)

    # ---------------- W4: the static block with the corrected weights
    Rs, E, L = FO.general_lhs()
    stat_gen = lhs_matrix(E, (w2, w3), lam, st, 1)
    stat_new = lhs_matrix(E, W_NEW[:2], lam, st, 1)
    iso = all(sp.simplify(stat_new[i, i] - (7 + lam)) == 0 for i in range(8)) and all(
        stat_new[i, j] == 0 for i in range(8) for j in range(8) if i != j)
    per_order = {}
    for p in (1, 2, 3):
        vv = [sp.nsimplify(weighted(p, W_NEW[:2]) * E[p][k, k].subs(FO.author_values(1)).subs(st) / H ** 2) for k in (1, 4)]
        per_order[p] = vv
    y = sp.Symbol('y', positive=True)

    def family(m):
        return sum(-weighted(p, W_NEW[:2]) * (-y * H ** 2) ** p / 2 * sp.factorial(m) / sp.factorial(m - 2 * p)
                   for p in (1, 2, 3)) / H ** 2
    fam_w = sp.factor(family(6) - 7)
    fam_t = sp.factor(family(7) - 7)
    ok4 = (iso and per_order == {1: [15, 21], 2: [-9, -21], 3: [1, 7]}
           and sp.expand(fam_w - (y - 1) ** 2 * (y - 7)) == 0 and sp.expand(fam_t - 7 * (y - 1) ** 3) == 0)
    out['W4'] = {'static_general_weights_warped_time': [str(sp.factor(stat_gen[1, 1])), str(sp.factor(stat_gen[4, 4]))],
                 'static_corrected': str(sp.factor(stat_new[1, 1])), 'per_order_warped_time': {str(p): [str(x) for x in v]
                                                                                              for p, v in per_order.items()},
                 'family_warped_minus_7': str(fam_w), 'family_time_minus_7': str(fam_t)}
    rep.check('W4_static_block_is_a_vacuum', ok4,
              'general weights: the static block needs %s (warped) and %s (time); with w2 = 1/20, w3 = 1/360 every component '
              'is (7 + lam) H^2: Lambda = -7 H^2 makes the static bulk a vacuum (no stabiliser); order by order (warped, time): '
              'Einstein %s, Gauss-Bonnet %s, cubic %s; along the spaces of constant curvature -y H^2 the left-hand side minus '
              '7 H^2 is %s (warped) and %s (time): a degenerate vacuum at y = 1' % (
                  sp.factor(stat_gen[1, 1]), sp.factor(stat_gen[4, 4]), per_order[1], per_order[2], per_order[3], fam_w, fam_t))

    # ---------------- W5: the bulk equations with the corrected weights, any a4, b4
    full = lhs_matrix(E, W_NEW[:2], W_NEW[2], {}, 1)
    T44 = sp.factor(full[4, 4])
    T04 = sp.factor(full[0, 4])
    no_second = T44.free_symbols <= {A, U} and T04.free_symbols <= {A, U}
    Mfro = {s_: lhs_matrix(E, W_NEW[:2], W_NEW[2], fro, s_) for s_ in (-1, 1)}
    Mss = {s_: lhs_matrix(E, W_NEW[:2], W_NEW[2], {A: 0, Ad: 0}, s_) for s_ in (-1, 1)}
    zero_frozen = all(Mfro[s_][i, j] == 0 for s_ in (-1, 1) for i in range(8) for j in range(8))
    zero_static_space = all(Mss[s_][i, j] == 0 for s_ in (-1, 1) for i in range(8) for j in range(8))
    gen_c = lhs_matrix(E, W_NEW[:2], W_NEW[2], {Ad: 0, Ud: 0}, 1)
    comps = list({sp.factor(gen_c[i, j]) for i in range(8) for j in range(8) if gen_c[i, j] != 0})
    sols = sp.solve(comps, [A, U], dict=True)
    av_rho = sp.simplify(-T44.subs({A: 1, U: 0}))
    ok5 = (no_second and sp.expand(T44 - A ** 3 * (A - U) ** 3) == 0 and sp.expand(T04 - 3 * A ** 2 * U * (A - U) ** 2) == 0
           and zero_frozen and zero_static_space and sorted(map(str, sols)) == sorted(['{A: 0}', '{U: A}']) and av_rho == -1)
    out['W5'] = {'kappa_T44_over_H2': str(T44), 'kappa_T04_over_H2_sigma_positive': str(T04), 'frozen_vacuum': zero_frozen,
                 'static_space_vacuum': zero_static_space, 'constant_rate_vacua': [str(s_) for s_ in sols],
                 'author_vacuum_kappa_rho_bulk_over_H2': str(av_rho)}
    rep.check('W5_bulk_vacua', ok5,
              'with w = (1, 1/20, 1/360) and Lambda = -7 H^2, any a4(x4), b4(x4): kappa T^(4)_(4) = %s H^2, kappa T^(0)_(4) = %s '
              'H^2 sgn(sigma) (no second time derivative); all 64 components vanish on both sides of the fold for frozen '
              'extra times (U = A, any a4(x4)): %s, and for static ordinary space (A = 0, any b4(x4)): %s; with constant rates '
              'the vacua are %s; the author\'s vacuum would need kappa rho_bulk = %s H^2' % (
                  T44, T04, zero_frozen, zero_static_space, sols, av_rho))

    # ---------------- W6: the fold with the corrected weights: a tension and the Friedmann equations
    import um3_stabiliser as ST
    Lnew = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            Lnew[i, j] = sp.expand(E[1][i, j] + W_NEW[0] / H ** 2 * E[2][i, j] + W_NEW[1] / H ** 4 * E[3][i, j]
                                   + (W_NEW[2] * H ** 2 if i == j else 0))
    Fj, exact = ST.junction_potentials(Lnew)
    kS = ST.fold_source(Fj, fro)
    want = {(1, 1): -sp.Rational(16, 15) * (6 + 3 * A ** 2 + 2 * Ad), (4, 4): -sp.Rational(16, 5) * (2 + A ** 2),
            (5, 5): -sp.Rational(4, 5) * (8 + 8 * A ** 2 + A ** 4 + 4 * Ad + A ** 2 * Ad)}
    ok6a = exact and all(sp.simplify(kS[k] / H - want[k]) == 0 for k in want)
    lamF = -kS[(4, 4)].subs({A: 0, Ad: 0})
    k7 = sp.Symbol('kappa_7', positive=True)
    kap = sp.Symbol('kappa', positive=True)
    rho_m = sp.simplify((-kS[(4, 4)] - lamF) / kap)
    p_m = sp.simplify((kS[(1, 1)] + lamF) / kap)
    k4v = sp.Rational(15, 16) * kap * H
    friedmann1 = sp.simplify(rho_m - 3 * (A * H) ** 2 / k4v) == 0
    friedmann2 = sp.simplify(p_m + (2 * Ad * H ** 2 + 3 * (A * H) ** 2) / k4v) == 0
    q_m = sp.factor(sp.simplify((kS[(5, 5)] + lamF) / H))
    # conservation of the fold matter by itself: rho' + 3 a4' (rho + p) = 0 for any a4(x4)
    x4 = sp.Symbol('x4')
    a4 = sp.Function('a4')(x4)
    sub_t = {A: sp.diff(a4, x4) / H, Ad: sp.diff(a4, x4, 2) / H ** 2}
    cons = sp.simplify(sp.diff(rho_m.subs(sub_t), x4) + 3 * sp.diff(a4, x4) * (rho_m + p_m).subs(sub_t))
    ok6 = (ok6a and lamF == sp.Rational(32, 5) * H and all(sp.simplify(kS[k].subs({A: 0, Ad: 0}) + lamF) == 0 for k in kS)
           and friedmann1 and friedmann2 and cons == 0)
    out['W6'] = {'fold_source_frozen_over_H': {'%d' % k[0]: str(sp.factor(v / H)) for k, v in kS.items()},
                 'kappa_lambda_F': str(lamF), 'kappa_7': '15 kappa H/16', 'q_m_kappa_over_H': str(q_m), 'conservation': str(cons)}
    rep.check('W6_fold_is_an_einstein_brane', ok6,
              'frozen extra times, any a4(x4): kappa S = %s H (ordinary space, time, extra times); at the static block a pure '
              'tension kappa lambda_F = %s; above it rho_m = 3 a4\'^2/kappa_7 and p_m = -(2 a4\'\' + 3 a4\'^2)/kappa_7 with '
              'kappa_7 = 15 kappa H/16 (the two Friedmann equations of four-dimensional general relativity), the matter of the '
              'fold conserved by itself; the extra-time component requires kappa q_m = %s H' % (
                  [str(sp.factor(kS[(i, i)] / H)) for i in (1, 4, 5)], lamF, q_m))

    # ---------------- W7: the graviton of the fold with the corrected weights, every frozen background
    b_new = bulk_coeffs(parts12, fro, W_NEW[:2])
    t_new = thin_coeffs(parts12, fro, W_NEW[:2])
    b_new56 = bulk_coeffs(parts56, fro, W_NEW[:2])
    ok7 = (all(v == 0 for v in b_new.values()) and sp.simplify(t_new['h_tt'] - sp.Rational(8, 15) / H) == 0
           and sp.simplify(t_new['h_33'] + sp.Rational(8, 15) / H) == 0 and sp.simplify(t_new['h_t'] - sp.Rational(8, 5) * A) == 0
           and t_new['hs_p'] == 0 and t_new['hs_m'] == 0 and sp.simplify(1 / (2 * k4v) * kap - sp.Rational(8, 15) / H) == 0)
    out['W7'] = {'bulk_frozen_pol_12': {k: str(v) for k, v in b_new.items()}, 'bulk_frozen_pol_56': {k: str(v) for k, v in b_new56.items()},
                 'thin_frozen': {k: str(v) for k, v in t_new.items()}}
    rep.check('W7_graviton_at_the_speed_of_light', ok7,
              'w = (1, 1/20, 1/360), frozen extra times, any a4(x4): the bulk TT operator of the + polarisation in ordinary '
              'space vanishes identically (%s), in the extra times it is %s; the thin part is (8/(15H))(h_tt + 3 A H h_t - h_33) '
              'with no [h_s] term = (kappa/(2 kappa_7))(h_tt + 3 a4\' h_t - e^{-2a4} nabla^2 h): the graviton of general '
              'relativity on the fold, with the kappa_7 of W6; it travels at the speed of light at every wavelength' % (
                  {k: str(v) for k, v in b_new.items()}, {k: str(v) for k, v in b_new56.items()}))

    # ---------------- W8: the record of the author's weights
    stat_a = lhs_matrix(E, W_AUTHOR[:2], W_AUTHOR[2], st, 1)
    av_a = lhs_matrix(E, W_AUTHOR[:2], W_AUTHOR[2], av, 1)
    fro_a = lhs_matrix(E, W_AUTHOR[:2], W_AUTHOR[2], {U: A, Ud: 0, Ad: 0}, 1)
    b_av = bulk_coeffs(parts12, av, W_AUTHOR[:2])
    stab = [sp.nsimplify(stat_a[i, i]) for i in range(8)]
    ok8 = (all(av_a[i, j] == 0 for i in range(8) for j in range(8)) and b_av['h_tt'] == 0 and b_av['h_33'] != 0
           and stab == [sp.Rational(-5, 16)] * 4 + [sp.Rational(1, 16)] + [sp.Rational(-5, 16)] * 3
           and sp.simplify(-fro_a[4, 4] - (3 * A ** 2 - 1) / 16) == 0)
    out['W8'] = {'author_vacuum_is_vacuum': True, 'bulk_graviton_at_author_vacuum': {k: str(v) for k, v in b_av.items()},
                 'static_block_needs': [str(x) for x in stab], 'frozen_needs_kappa_rho_over_H2': str(sp.factor(-fro_a[4, 4]))}
    rep.check('W8_record_of_the_author_weights', ok8,
              'w = (1, 1/32, 1/1152), Lambda = -10 H^2: the author\'s vacuum solves the bulk equations; there the bulk graviton '
              'has no time-kinetic term (%s); the static block needs the source H^2 diag%s (the stabiliser), the frozen '
              'expanding bulk kappa rho_bulk = %s H^2' % (
                  {k: str(v) for k, v in b_av.items()}, tuple(str(x) for x in stab), sp.factor(-fro_a[4, 4])))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'weights.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_weights.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'weights_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
