#!/usr/bin/env python3
"""um4_gravity.py - the gravity of UM-4: which Lovelock weights and which cosmological constant let gravitons propagate at
the speed of light in the bulk (the author's order of 2026-10-25, 13:15 PDT: "both photons and gravitons actually
propagate at c in the bulk").

The Einstein-Lovelock equations of eight dimensions, sum_{p=1}^{3} alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b with
alpha_(p) = w_(p) H^{2-2p} (w_(1) = 1, w2 = w_(2), w3 = w_(3)) and Lambda = lam H^2, on the UM-4 metric (um4_geometry.py),
whose static block is a space of constant curvature -H^2 in all eight directions.  A transverse traceless gravitational wave
of the + polarisation in ordinary space multiplies g_11 and g_22 by e^{eps h} and e^{-eps h}, h = h(sigma, x3, x4); its
equation is the part of first order in eps of (E^1_1 - E^2_2)/2.  Checks:
  L1  the vacua: on the family of static blocks of curvature -y H^2 (warp e^{-2 sqrt(y) H |sigma|} in all seven directions),
      computed from their curvature, sum alpha_p E_(p) + Lambda = P(y) H^2 delta^a_b with the vacuum polynomial
      P(y) = 21 y - 420 w2 y^2 + 2520 w3 y^3 + lam; the static block (y = 1) is a vacuum iff P(1) = 0.  Einstein gravity
      (w2 = w3 = 0): lam = -21, the single root y = 1, P'(1) = 21.  The author's original weights (1/32, 1/1152): lam =
      -161/16, roots y = 1 and (5 -+ sqrt(33/5))/2, P'(1) = 21/16 > 0 (the root 1.215 has P' < 0).  The Born-Infeld weights
      of UM-3 (1/20, 1/360) with lam = -7: P = 7 (y - 1)^3, a triple root (degenerate: no linear graviton);
  L2  the graviton around the static block of UM-4 for any weights: away from the fold its equation is
          (P'(1)/42) [ e^{2H|sigma|} (h_tt - h_33) - h_ss + 7 H sgn(sigma) h_s ] = 0
      (h_tt = d^2h/dx4^2, h_33 = d^2h/dx3^2, h_ss = d^2h/d sigma^2, h_s = dh/d sigma; no other derivative), and the +
      polarisation along the extra times has the same equation: around the static block every non-degenerate choice of the
      weights gives bulk gravitons on the light cone (the speed of light of the fold at every sigma), with the strength
      P'(1)/21 relative to Einstein gravity; the degenerate weights (P'(1) = 0) give none, P'(1) < 0 a ghost;
  L3  the gravitons on backgrounds that are not of constant curvature: the static warped metrics
      d sigma^2 + e^{-2 p H sigma} dx_i^2 - e^{-2 q H sigma} dx4^2 - e^{-2 r H sigma} dx_r^2 (sigma > 0, constant p, q, r;
      p = q = r = 1 is the static block of UM-4, p = r = 1, q = 0 that of UM-3): the coefficients of the second derivatives
      along the time, ordinary space and sigma (in the frame) are c_t, c_x and c_s; Einstein gravity gives c_t = c_x = c_s = 1
      on every such background, while with the Gauss-Bonnet and cubic terms c_x - c_t = -4 (p - q)(18 r^2 w3 - w2)(p + q + 3 r)
      (zero when the time is warped like ordinary space, p = q, for any weights) and c_s - c_t is another polynomial in p, q, r
      linear in w2 and w3; both vanish for all p, q, r only for w2 = w3 = 0: only Einstein gravity lets gravitons travel at the
      speed of light on every background; for UM-3's static block the
      coefficients are those of UM-3, c_t = 1 - 40 w2 + 360 w3 and c_x = 1 - 24 w2 + 72 w3 (with the author's weights
      c_x/c_t = 5);
  L4  the gravity of UM-4: w2 = w3 = 0 (Einstein gravity) and Lambda = -21 H^2: the static block is the unique vacuum,
      bulk gravitons propagate at the speed of light on every background, and the fold is a pure tension kappa lambda_F = 12 H
      (um4_geometry.py G7); with the author's original weights the static block would also be a vacuum (Lambda = -161 H^2/16,
      gravitons at the speed of light around it with 1/16 of the Einstein strength), but on every background that is not of
      constant curvature their gravitons would leave the light cone (L3), so UM-4 does not use them.
Writes outputs/gravity.json and reports/gravity_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_gravity.py

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

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write                     # noqa: E402
from um4_lovelock import frame_riemann, lovelock_tensor  # noqa: E402

H = sp.Symbol('H', positive=True)
SIG = sp.Symbol('sigma', positive=True)          # the side sigma > 0 (the other side is its mirror image)
x1, x2, x3, x4, x5, x6, x7 = sp.symbols('x1:8', real=True)
X = [SIG, x1, x2, x3, x4, x5, x6, x7]
w2, w3, lam, y = sp.symbols('w2 w3 lam y')
pp, qq, rr = sp.symbols('p q r', positive=True)
eps = sp.Symbol('epsilon')
hf = sp.Function('h')(SIG, x3, x4)
EPSG = [1, 1, 1, 1, -1, -1, -1, -1]
W_AUTHOR = (sp.Rational(1, 32), sp.Rational(1, 1152))
W_BI = (sp.Rational(1, 20), sp.Rational(1, 360))


def lovelock_lhs(Rf, ws, lamv, n=8):
    E = {p: lovelock_tensor(Rf, p, n) for p in (1, 2, 3)}
    return sp.Matrix(n, n, lambda i, j: E[1][i, j] + ws[0] / H ** 2 * E[2][i, j] + ws[1] / H ** 4 * E[3][i, j]
                     + (lamv * H ** 2 if i == j else 0))


def fast_simp(e):
    return sp.expand(sp.powsimp(sp.expand(e), combine='exp'))


def per_order_tt(fa, fn, fb, pol):
    """The first-order parts of (E_(p)^i_i - E_(p)^j_j)/2 (p = 1, 2, 3) for the + polarisation pol = (1, 2) or (5, 6) on the
    static diagonal background with the exponents fa (ordinary space), fn (time), fb (extra times)."""
    expo = [sp.S(0), fa, fa, fa, fn, fb, fb, fb]
    i, j = pol
    hs = [sp.S(1)] + [sp.exp(expo[k]) for k in range(1, 8)]
    hs[i] = hs[i] * sp.exp(eps * hf / 2)
    hs[j] = hs[j] * sp.exp(-eps * hf / 2)
    g = sp.diag(*[EPSG[k] * hs[k] ** 2 for k in range(8)])
    Rf = frame_riemann(g, X, hs, simplify=fast_simp)
    out = {}
    for p in (1, 2, 3):
        E = lovelock_tensor(Rf, p, simplify=lambda e: e)
        lin = sp.diff((E[i, i] - E[j, j]) / 2, eps).subs(eps, 0)
        out[p] = sp.expand(sp.simplify(lin.doit()))
    return out


DER = {'h_tt': sp.Derivative(hf, x4, 2), 'h_33': sp.Derivative(hf, x3, 2), 'h_ss': sp.Derivative(hf, SIG, 2),
       'h_s': sp.Derivative(hf, SIG), 'h_t': sp.Derivative(hf, x4), 'h_3': sp.Derivative(hf, x3),
       'h_st': sp.Derivative(hf, SIG, x4), 'h_s3': sp.Derivative(hf, SIG, x3), 'h_3t': sp.Derivative(hf, x3, x4), 'h': hf}


def coefficients(expr):
    """The coefficients of the derivatives of h in a linear expression, and the remainder (checked to vanish)."""
    syms = {k: sp.Symbol('D_' + k) for k in DER}
    e = expr
    for k in ['h_tt', 'h_33', 'h_ss', 'h_st', 'h_s3', 'h_3t', 'h_s', 'h_t', 'h_3']:
        e = e.subs(DER[k], syms[k])
    e = e.subs(hf, syms['h'])
    e = sp.expand(e)
    co = {k: sp.simplify(sp.diff(e, syms[k])) for k in syms}
    rest = sp.simplify(e - sum(co[k] * syms[k] for k in syms))
    return co, rest


def main():
    rep = Report()
    out = {}

    # ---------------- L1: the vacua
    fam = -sp.sqrt(y) * H * SIG
    hs = [sp.S(1)] + [sp.exp(fam)] * 7
    g = sp.diag(*[EPSG[k] * hs[k] ** 2 for k in range(8)])
    Rf = frame_riemann(g, X, hs)
    E = {p: lovelock_tensor(Rf, p) for p in (1, 2, 3)}
    Pv = sp.expand((E[1][1, 1] + w2 / H ** 2 * E[2][1, 1] + w3 / H ** 4 * E[3][1, 1]) / H ** 2 + lam)
    same = all(sp.simplify(E[p][k, k] - E[p][1, 1]) == 0 for p in (1, 2, 3) for k in range(8))
    P_expect = 21 * y - 420 * w2 * y ** 2 + 2520 * w3 * y ** 3 + lam
    ok1 = same and sp.expand(Pv - P_expect) == 0
    cases = {}
    for name, ws in (('einstein', (0, 0)), ('author_original', W_AUTHOR), ('born_infeld_um3', W_BI)):
        lam1 = sp.solve(P_expect.subs({w2: ws[0], w3: ws[1], y: 1}), lam)[0]
        Py = sp.expand(P_expect.subs({w2: ws[0], w3: ws[1], lam: lam1}))
        roots = sp.solve(Py, y)
        d1 = sp.diff(Py, y)
        cases[name] = {'lam': lam1, 'P': sp.factor(Py), 'roots': roots, 'dP_at_roots': [sp.nsimplify(d1.subs(y, r_)) for r_ in roots]}
    ok1 &= cases['einstein']['lam'] == -21 and cases['einstein']['roots'] == [1] and cases['einstein']['dP_at_roots'] == [21]
    ca = cases['author_original']
    ok1 &= ca['lam'] == sp.Rational(-161, 16) and sp.simplify(sp.diff(ca['P'], y).subs(y, 1) - sp.Rational(21, 16)) == 0
    ok1 &= len(ca['roots']) == 3 and any(sp.simplify(r_ - (5 - sp.sqrt(sp.Rational(33, 5))) / 2) == 0 for r_ in ca['roots'])
    ok1 &= sp.expand(cases['born_infeld_um3']['P'] - 7 * (y - 1) ** 3) == 0 and cases['born_infeld_um3']['lam'] == -7
    out['L1_vacuum_polynomial'] = str(P_expect)
    out['L1_cases'] = {k: {kk: (str(vv) if not isinstance(vv, list) else [str(x_) for x_ in vv]) for kk, vv in v.items()}
                       for k, v in cases.items()}
    out['L1_author_roots_numeric'] = [float(r_) for r_ in ca['roots']]
    out['L1_author_dP_numeric'] = [float(sp.diff(ca['P'], y).subs(y, r_)) for r_ in ca['roots']]
    rep.check('L1_vacua', ok1, 'P(y) = %s from the curvature of the static blocks of curvature -y H^2; Einstein: lam = -21, single root '
              'y = 1, P\'(1) = 21; the author\'s weights: lam = %s, P = %s, roots %s with P\' = %s; Born-Infeld (UM-3): P = %s' % (
                  P_expect, ca['lam'], ca['P'], [round(float(r_), 4) for r_ in ca['roots']],
                  [round(v, 4) for v in out['L1_author_dP_numeric']], cases['born_infeld_um3']['P']))

    # ---------------- L2: the graviton around the static block of UM-4, any weights
    st = -H * SIG
    ok2 = True
    res2 = {}
    for pol in ((1, 2), (5, 6)):
        parts = per_order_tt(st, st, st, pol)
        tot = sp.expand(parts[1] + w2 / H ** 2 * parts[2] + w3 / H ** 4 * parts[3])
        co, rest = coefficients(tot)
        c = sp.simplify(sp.diff(P_expect, y).subs(y, 1) / 42)        # P'(1)/42
        e2 = sp.exp(2 * H * SIG)
        expect = {'h_tt': c * e2, 'h_33': -c * e2, 'h_ss': -c, 'h_s': 7 * H * c}
        okp = rest == 0 and all(sp.simplify(co[k] - expect.get(k, 0)) == 0 for k in co)
        ok2 &= okp
        res2['%d%d' % pol] = {k: str(v) for k, v in co.items() if v != 0}
    out['L2_graviton_static_block'] = res2
    rep.check('L2_graviton_static_block_any_weights', ok2, 'the + polarisations in ordinary space and along the extra times, any w2, '
              'w3: (P\'(1)/42)[e^{2H sigma}(h_tt - h_33) - h_ss + 7H h_s] (sigma > 0), P\'(1) = 21 - 840 w2 + 7560 w3, no other '
              'term: around the static block every non-degenerate weight gives gravitons on the light cone of the fold at every '
              'sigma, with the strength P\'(1)/21')

    # ---------------- L3: backgrounds that are not of constant curvature
    fa, fn, fb = -pp * H * SIG, -qq * H * SIG, -rr * H * SIG
    parts = per_order_tt(fa, fn, fb, (1, 2))
    coefs = {}
    for p in (1, 2, 3):
        co, rest = coefficients(parts[p])
        if rest != 0:
            raise SystemExit('remainder in L3 at order %d: %s' % (p, rest))
        coefs[p] = co
    # frame coefficients: c_t multiplies e^{2 q H sigma} h_tt, c_x multiplies e^{2 p H sigma} h_33, c_s multiplies h_ss
    ct = {p: sp.simplify(2 * coefs[p]['h_tt'] * sp.exp(-2 * qq * H * SIG) / H ** (2 * p - 2)) for p in (1, 2, 3)}
    cx = {p: sp.simplify(-2 * coefs[p]['h_33'] * sp.exp(-2 * pp * H * SIG) / H ** (2 * p - 2)) for p in (1, 2, 3)}
    cs = {p: sp.simplify(-2 * coefs[p]['h_ss'] / H ** (2 * p - 2)) for p in (1, 2, 3)}
    ok3 = ct[1] == 1 and cx[1] == 1 and cs[1] == 1
    CT = sp.expand(ct[1] + w2 * ct[2] + w3 * ct[3])
    CX = sp.expand(cx[1] + w2 * cx[2] + w3 * cx[3])
    CS = sp.expand(cs[1] + w2 * cs[2] + w3 * cs[3])
    dev = sp.expand(CX - CT)
    # the deviation vanishes for all p, q, r only if w2 = w3 = 0
    poly = sp.Poly(dev, pp, qq, rr)
    lin_eqs = [sp.expand(c_) for c_ in poly.coeffs()]
    sol = sp.solve(lin_eqs, [w2, w3], dict=True)
    ok3 &= sol == [{w2: 0, w3: 0}]
    um3 = {pp: 1, qq: 0, rr: 1}
    ok3 &= sp.expand(CT.subs(um3) - (1 - 40 * w2 + 360 * w3)) == 0 and sp.expand(CX.subs(um3) - (1 - 24 * w2 + 72 * w3)) == 0
    um4 = {pp: 1, qq: 1, rr: 1}
    ok3 &= all(sp.expand(C_.subs(um4) - (1 - 40 * w2 + 360 * w3)) == 0 for C_ in (CT, CX, CS))
    ratio_author_um3 = sp.nsimplify((CX / CT).subs(um3).subs({w2: W_AUTHOR[0], w3: W_AUTHOR[1]}))
    ok3 &= ratio_author_um3 == 5
    out['L3_coefficients_per_order'] = {'c_t': {str(p): str(sp.factor(ct[p])) for p in ct},
                                        'c_x': {str(p): str(sp.factor(cx[p])) for p in cx},
                                        'c_s': {str(p): str(sp.factor(cs[p])) for p in cs}}
    out['L3_deviation_cx_minus_ct'] = str(sp.factor(dev))
    out['L3_deviation_cs_minus_ct'] = str(sp.factor(sp.expand(CS - CT)))
    out['L3_author_weights_UM3_block_cx_over_ct'] = str(ratio_author_um3)
    rep.check('L3_light_cone_on_every_background', ok3, 'static warps (p, q, r): Einstein c_t = c_x = c_s = 1 for all p, q, r; with '
              'the higher terms c_x - c_t = %s and c_s - c_t = %s, which vanish for all p, q, r only for w2 = w3 = 0; at p = q = r = 1 all three '
              'equal P\'(1)/21 = 1 - 40 w2 + 360 w3; at UM-3\'s block (1, 0, 1) c_t = 1 - 40 w2 + 360 w3, c_x = 1 - 24 w2 + 72 w3, '
              'with the author\'s weights c_x/c_t = %s' % (sp.factor(dev), sp.factor(sp.expand(CS - CT)), ratio_author_um3))

    # ---------------- L4: the gravity of UM-4
    ok4 = (cases['einstein']['lam'] == -21 and cases['einstein']['dP_at_roots'] == [21] and sol == [{w2: 0, w3: 0}])
    out['L4_um4_gravity'] = {'w2': '0', 'w3': '0', 'Lambda': '-21 H^2', 'kappa_lambda_F': '12 H',
                             'reason': 'the only Lovelock weights with gravitons on the light cone on every background'}
    rep.check('L4_gravity_of_UM4', ok4, 'UM-4 uses Einstein gravity (w2 = w3 = 0) with Lambda = -21 H^2: the static block is the unique '
              'vacuum (P\'(1) = 21 > 0), gravitons propagate on the light cone on every background (L3), the fold is a pure '
              'tension kappa lambda_F = 12 H; the author\'s original weights would need Lambda = -161 H^2/16 and keep gravitons on '
              'the light cone only around the static block')
    return write('gravity', 'um4_gravity.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
