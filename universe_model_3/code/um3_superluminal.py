#!/usr/bin/env python3
"""um3_superluminal.py - how fast do the particles chi move, and what does a speed above that of light on the fold mean?

The author's metric warps ordinary space but not the time (FD-4):
    ds^2 = d sigma^2 + e^{-2H|sigma|} [e^{2a4} dx_i^2 - e^{-2a4} b4^2 dx_r^2] - dx4^2,
so at the depth |sigma| light moves along ordinary space with the coordinate speed e^{H|sigma|} e^{-a4}: the bulk is faster
than the fold.  A state of dirac16complex bound to the fold samples the bulk over its width 1/q_b; moving with the momentum
k along x1 (the term -i k e^{H|sigma|} gamma^(1) of the Dirac operator, a4 = 0) its frequency omega(k) obeys
omega^2 = omega_b^2 + c_b^2 k^2 for small k, with c_b^2 close to the average of the warp e^{2H|sigma|} over its density,
q_b/(q_b - H).
Checks:
  SL1  the small-momentum coefficient c_b^2 = d omega^2/d k^2 at k = 0 (the speed coefficient of slow chi; c_b is not a speed
       that chi ever reach) computed exactly (16-component shooting at k = 0.01) against the estimate q_b/(q_b - H), at
       three points (regime I, a stronger warp, the weakly bound point K9);
  SL2  the whole dispersion of the bound level up to k = 30 m_Psi (regime I, H = 0.05, q_b = 0.3): omega/k decreases towards
       1 from above, while omega - k keeps growing (like k^0.26; the momentum term k^2 (e^{2H|sigma|} - 1), about
       2 H k^2 |sigma| near the fold, confines the state like a linear potential, k^{1/3}); the group velocity d omega/dk
       by central differences (dk = 0.25) at k = 5.5, 6.5, 13, 25: below 1 at 5.5, above 1 from about k = 6 m_Psi on,
       largest near k = 13 (1.0046), falling slowly towards 1 (1.0038 at k = 25); with the stronger warp H = 0.1 at the
       same binding (H/q_b = 1/3) at k = 7, 9, 11 (about 1.009): the excess over the speed of light grows with H/q_b;
  SL3  the particles chi of the cosmological history are slow: the group velocity at the momentum of a halo particle
       (k = 10^-3 omega_b) and at a thermal momentum of the freeze-out (k = sqrt(3 omega_b T), T = omega_b/25) is far below 1;
  SL4  causality: the metric restricted to the plane of the time x4 and an extra time is negative definite, so with four
       time-like directions the eight-dimensional metric has closed time-like curves through every point (the circle
       (x4, x5) = (R cos s, R sin s); with compact extra times the circle of x5 alone); x4 is a time function only on the
       section at fixed extra times.  There the bulk is a shortcut between points of the fold: the optical metric
       d sigma^2 + e^{-2H|sigma|} dx^2 is the hyperbolic plane of radius 1/H and the fold one of its horocycles, so the
       earliest arrival of a bulk signal over the coordinate distance Dx on the fold is T(Dx) = (2/H) arcsinh(H Dx/2) < Dx
       (numerically: the shortest null path found by minimisation over paths agrees); over one light year on the fold a
       bulk signal needs 7e-14 s for H = 1e-9 GeV;
  SL5  ESTIMATE: Lorentz violation passed to the Standard Model through loops of chi with the portal couplings of the relic
       abundance, delta c ~ (g omega_b^2/(16 pi^2))^2 (c_b^2 - 1), with a sign that is not computed, against the bounds on
       the maximal speed of electrons (faster than light: c_e - 1 < 5e-21, Stecker 2014; slower: 1 - c_e < 5.6e-20):
       the binding this requires, q_b/H above 1e14 to 4e15, and with q_b about 0.03 omega_b the bound H < 5e-13 GeV.
Writes outputs/superluminal.json and reports/superluminal_checks.json.  Runs in about 5 minutes.
Usage: python universe_model_3/code/um3_superluminal.py

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
from scipy.optimize import minimize, minimize_scalar

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_kohnsham as K  # noqa: E402

GEV2_TO_CM3S = 0.3893793721e-27 * 2.99792458e10        # 1 GeV^-2 times c in cm^3/s
SIGMAV_PAIR = 9e-26                                      # (sigma v) of one chi with one antichi for the relic density (cm^3/s)
BOUND_EC_FAST = 5e-21        # electrons faster than light: no vacuum Cherenkov radiation of the 5.1 PeV electrons of the
                             # 2010 Crab flare (F. W. Stecker, Astroparticle Physics (2014), doi:10.1016/j.astropartphys.2014.02.007,
                             # arXiv:1306.6095), 1/(2 (E/m)^2)
BOUND_EC_SLOW = 5.6e-20      # electrons slower than light: synchrotron electrons of gamma = 3e9 in the Crab nebula exist only
                             # if |c_e - 1| < 1/(2 gamma^2) (Jacobson, Liberati, Mattingly, Nature 424 (2003) 1019)


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


def moving_level(H, muL, k, guess, width, L=None, h=None, npt=41):
    """The bound level of dirac16complex with the momentum k along x1 (16 components, a4 = 0): the root of the smallest
    singular value within guess +- width (every local minimum of a grid refined; the root closest to the guess with a
    singular value below 1e-7).  The box and the step follow the local decay rate k e^{H sigma} at its end."""
    if L is None:
        L = 40.0 if k <= 0.3 else min(40.0, math.log(max(1.0, 60.0 / k)) / H + 2.0)
        L = max(L, 6.0)
    if h is None:
        rate = max(1.0, k * math.exp(H * L))
        h = min(0.02, 0.35 / rate)
    sh = K.Shooter(H, muL, 0.0, L, h, 16)
    Mk = (-1j * k * np.exp(H * sh.s))[:, None, None] * K.TUP[1][None]
    sh.set_field(Mk.copy(), Mk.copy())

    def f(w):
        try:
            return float(sh.sv(w)[0])
        except RuntimeError:
            return np.inf
    xs = np.linspace(guess - width, guess + width, npt)
    vals = [f(x) for x in xs]
    best = None
    for i in range(1, npt - 1):
        if vals[i] <= vals[i - 1] and vals[i] <= vals[i + 1]:
            r = minimize_scalar(f, bounds=(xs[i - 1], xs[i + 1]), method='bounded', options={'xatol': 1e-15, 'maxiter': 600})
            if r.fun < 1e-7 and (best is None or abs(r.x - guess) < abs(best[0] - guess)):
                best = (float(r.x), float(r.fun))
    if best is None:
        return None, min(vals), L, h
    return best[0], best[1], L, h


def main():
    t0 = time.time()
    rep = Report()
    out = {'units': 'm_Psi = 1'}

    # ---------------- SL1: the small-momentum coefficient
    pts = [('regime I', 0.05, -0.6), ('stronger warp', 0.1, -0.6), ('weakly bound point K9', 0.002, -0.06)]
    sl1 = []
    for nm, H, muL in pts:
        qb = -muL / 2
        wb = math.sqrt(1 - qb * qb)
        est = qb / (qb - H)
        k = 0.01 if qb > 0.1 else 0.001
        L = 40.0 if qb > 0.1 else 500.0
        hh = 0.02 if qb > 0.1 else 0.25
        w, s, _, _ = moving_level(H, muL, k, math.sqrt(wb * wb + est * k * k), 2e-4 * max(k / 0.01, 0.05), L=L, h=hh)
        sl1.append({'point': nm, 'H': H, 'q_b': qb, 'omega_b': wb, 'k': k, 'omega': w, 'sv': s,
                    'c_b^2_computed': (w * w - wb * wb) / (k * k), 'c_b^2_estimate': est})
    out['SL1'] = sl1
    rep.check('SL1_small_momentum', all(r['sv'] < 1e-7 for r in sl1)
              and all(1 < r['c_b^2_computed'] < r['c_b^2_estimate'] * 1.001 for r in sl1)
              and all(0.8 < (r['c_b^2_computed'] - 1) / (r['c_b^2_estimate'] - 1) < 1.0 for r in sl1),
              'omega^2 = omega_b^2 + c_b^2 k^2 at small k: %s (computed, against the estimate q_b/(q_b - H)): the particles '
              'chi at low momentum move with the speed coefficient c_b above that of light on the fold, slightly below the estimate' % (
                  '; '.join('%s: %.5f (%.5f)' % (r['point'], r['c_b^2_computed'], r['c_b^2_estimate']) for r in sl1)))

    # ---------------- SL2: the whole dispersion, regime I
    H, muL = 0.05, -0.6
    qb = 0.3
    wb = math.sqrt(1 - qb * qb)
    ks = [0.0, 0.1, 0.2, 0.35, 0.5, 0.7, 1.0, 1.4, 2.0, 2.8, 4.0, 5.5, 7.5, 10.0, 14.0, 20.0, 30.0]
    disp = []
    for i, k in enumerate(ks):
        if i == 0:
            guess, width = wb, 1e-3
        elif i == 1:
            guess, width = math.sqrt(wb * wb + 1.19 * k * k), 2e-3
        else:
            k1, w1 = disp[-1]['k'], disp[-1]['omega']
            k2, w2 = disp[-2]['k'], disp[-2]['omega']
            guess = w1 + (w1 - w2) / (k1 - k2) * (k - k1)
            width = max(3e-3, 0.08 * (k - k1))
        w, s_, L, hh = moving_level(H, muL, k, guess, width)
        if w is None:
            w, s_, L, hh = moving_level(H, muL, k, guess, 3 * width)
        disp.append({'k': k, 'omega': w if w is not None else float('nan'), 'sv': s_, 'box': L, 'step': hh})
        if w is None:
            break
    secant = [{'k': 0.5 * (a['k'] + b['k']), 'v_secant': (b['omega'] - a['omega']) / (b['k'] - a['k'])}
              for a, b in zip(disp[:-1], disp[1:])]
    kgrid = [d['k'] for d in disp]
    wgrid = [d['omega'] for d in disp]

    def level_near(Hh, k, guess, width, npt):
        w, s_, L_, h_ = moving_level(Hh, muL, k, guess, width, npt=npt)
        if w is None:
            w, s_, L_, h_ = moving_level(Hh, muL, k, guess, 8 * width, npt=41)
        return w, s_

    def group_velocity(Hh, k, w_guess, v_guess, width, dk=0.25):
        """d omega/dk by the central difference (omega(k + dk) - omega(k - dk))/(2 dk); its error is of the order of
        dk^2 times the third derivative of omega(k), below 1e-5 here because the dispersion is nearly straight."""
        wm, sm = level_near(Hh, k - dk, w_guess - v_guess * dk, width, 21)
        wp, sp_ = level_near(Hh, k + dk, wm + 2 * dk * v_guess, 0.004, 11)
        return {'k': k, 'v_group': (wp - wm) / (2 * dk), 'omega_minus': wm, 'omega_plus': wp, 'sv': max(sm, sp_)}
    vg = []
    for k in (5.5, 6.5, 13.0, 25.0):
        wg = float(np.interp(k, kgrid, wgrid))
        vgu = float(np.interp(k, [r['k'] for r in secant], [r['v_secant'] for r in secant]))
        vg.append(group_velocity(H, k, wg, vgu, 0.01))
    # a stronger warp: H = 0.1 with the same binding q_b = 0.3 (H/q_b = 1/3 instead of 1/6)
    vg2 = []
    for k, wg in ((7.0, 7.3577), (9.0, 9.3729), (11.0, 11.3895)):
        vg2.append(group_velocity(0.1, k, wg, 1.009, 0.05))
    vmax = max(vg, key=lambda r: r['v_group'])
    vmax2 = max(vg2, key=lambda r: r['v_group'])
    out['SL2'] = {'dispersion': disp, 'secant_slopes': secant, 'group_velocity_H_0.05': vg, 'group_velocity_H_0.1': vg2,
                  'v_max_H_0.05': vmax, 'v_max_H_0.1': vmax2, 'omega_over_k_at_30': disp[-1]['omega'] / disp[-1]['k']}
    ratios = [d['omega'] / d['k'] for d in disp[1:]]
    excess = [(d['k'], d['omega'] - d['k']) for d in disp if d['k'] >= 10]
    expo = math.log(excess[-1][1] / excess[0][1]) / math.log(excess[-1][0] / excess[0][0])
    out['SL2']['omega_minus_k_exponent_k10_to_k30'] = expo
    v_by_k = {r['k']: r['v_group'] for r in vg}
    ok2 = (all(d['sv'] < 1e-6 for d in disp) and all(r['sv'] < 1e-6 for r in vg + vg2)
           and all(r2 < r1 for r1, r2 in zip(ratios[5:], ratios[6:]))
           and 1 < disp[-1]['omega'] / disp[-1]['k'] < 1.02 and v_by_k[5.5] < 1 < v_by_k[6.5] < v_by_k[13.0]
           and v_by_k[25.0] < v_by_k[13.0] and 1.004 < v_by_k[13.0] < 1.005 and vmax2['v_group'] > v_by_k[13.0]
           and 0.15 < expo < 0.4)
    rep.check('SL2_dispersion', ok2,
              'regime I (H = 0.05, q_b = 0.3), k = 0 ... 30 m_Psi: omega/k falls towards 1 from above (%.4f at k = 10, %.4f '
              'at k = 30), while omega - k keeps growing, like k^%.2f between k = 10 and 30 (k^{1/3} for a linear confining '
              'potential 2 H k^2 |sigma|); the group velocity d omega/dk (central differences) is %.5f at k = 5.5, %.5f at '
              '6.5, %.5f at 13 and %.5f at 25: above 1 from about k = 6 m_Psi on, largest near k = 13, falling slowly towards '
              '1; with the stronger warp H = 0.1 (H/q_b = 1/3) it is %s at k = 7, 9, 11: the excess grows with H/q_b' % (
                  disp[13]['omega'] / disp[13]['k'], disp[-1]['omega'] / disp[-1]['k'], expo, v_by_k[5.5], v_by_k[6.5],
                  v_by_k[13.0], v_by_k[25.0], ['%.5f' % r['v_group'] for r in vg2]))

    # ---------------- SL3: the particles of the cosmological history are slow
    cb2 = sl1[0]['c_b^2_computed']
    k_halo = 1e-3 * wb
    k_fo = math.sqrt(3 * wb * wb / 25)
    v_halo = cb2 * k_halo / math.sqrt(wb * wb + cb2 * k_halo ** 2)
    # at the freeze-out momentum, the group velocity from the computed dispersion (interpolated)
    kk = np.array([d['k'] for d in disp])
    ww = np.array([d['omega'] for d in disp])
    v_fo = float(np.interp(k_fo, [r['k'] for r in secant], [r['v_secant'] for r in secant]))
    out['SL3'] = {'k_halo': k_halo, 'v_halo': v_halo, 'k_freeze_out': k_fo, 'v_freeze_out': v_fo}
    rep.check('SL3_cosmological_chi_are_slow', v_halo < 2e-3 and v_fo < 0.6 and k_fo < 5.5,
              'regime I: a halo particle (k = 1e-3 omega_b) moves at %.2e, a thermal one at the freeze-out (k = sqrt(3 omega_b T), '
              'T = omega_b/25, k = %.3f) at %.3f: the group velocity exceeds 1 only for ultrarelativistic chi (k above about '
              '6 m_Psi, SL2), which exist only long before the freeze-out' % (v_halo, k_fo, v_fo))

    # ---------------- SL4: causality and the shortcut through the bulk
    Hs = 1.0
    res4 = []
    for dx in (0.5, 2.0, 10.0, 100.0):
        exact = 2 / Hs * math.asinh(Hs * dx / 2)
        # the shortest null path found numerically: a path sigma(x) (n points) from (0, 0) to (0, dx), time = optical length
        n = 40
        xs = np.linspace(0, dx, n + 1)

        def length(p):
            sg = np.concatenate([[0.0], np.abs(p), [0.0]])
            dsg = np.diff(sg)
            dxx = np.diff(xs)
            sm = 0.5 * (sg[1:] + sg[:-1])
            return float(np.sum(np.sqrt(dsg ** 2 + np.exp(-2 * Hs * sm) * dxx ** 2)))
        p0 = (2 / Hs) * np.log1p(Hs * dx / 2) * np.sin(np.pi * xs[1:-1] / dx)
        r = minimize(length, p0, method='L-BFGS-B', options={'maxiter': 20000, 'maxfun': 200000})
        res4.append({'dx': dx, 'T_exact': exact, 'T_path': r.fun, 'T_fold': dx})
    # closed time-like curves: the metric restricted to the plane of the time x4 and an extra time x5 is
    # -dx4^2 - w dx5^2 with w = e^{-2H|sigma|} e^{-2 a4} b4^2 > 0, negative definite, so every curve in that plane, the
    # circle (x4, x5) = (R cos s, R sin s) included, is time-like: the eight-dimensional metric has closed time-like curves
    # through every point, and with compact extra times the circle of x5 alone is one.  On the section at fixed extra
    # times (sigma, x1, x2, x3, x4; signature (4, 1)) x4 is a time function: there g^{x4 x4} = -1 and every causal curve
    # has dx4 != 0.
    ss = np.linspace(0.0, 2 * np.pi, 721)
    ctc = []
    for w_ in (1e-6, 0.3, 1.0, 7.0):
        ds2_over_R2 = -(np.sin(ss) ** 2 + w_ * np.cos(ss) ** 2)
        ctc.append({'w': w_, 'max_ds2_over_R2': float(ds2_over_R2.max())})
    ctc_ok = all(c['max_ds2_over_R2'] < 0 for c in ctc)
    # the size of the shortcut: one light year along the fold, H = 1e-9 GeV and 4e-13 GeV
    GEV_INV_M = 1.973269804e-16          # 1 GeV^-1 in metres
    GEV_INV_S = 6.582119569e-25          # 1 GeV^-1 in seconds
    LY_M = 9.4607304725808e15
    dx_ly = LY_M / GEV_INV_M
    short = []
    for Hg in (1e-9, 4e-13):
        T = 2 / Hg * math.asinh(Hg * dx_ly / 2)
        short.append({'H_GeV': Hg, 'T_one_light_year_s': T * GEV_INV_S, 'T_along_the_fold_s': dx_ly * GEV_INV_S})
    out['SL4'] = {'shortest_bulk_signal': res4, 'closed_timelike_curves_x4_x5': ctc, 'one_light_year': short}
    rep.check('SL4_causality_and_bulk_shortcut', ctc_ok and all(r['T_path'] >= r['T_exact'] * (1 - 1e-6)
                                                                and r['T_path'] < r['T_exact'] * 1.02
                                                                and r['T_exact'] < r['dx'] for r in res4),
              'the metric restricted to the plane of x4 and an extra time is negative definite (largest ds^2/R^2 along the '
              'circle (x4, x5) = (R cos s, R sin s) is %s for w = e^{-2H|sigma| - 2a4} b4^2 = %s): with four time-like '
              'directions the eight-dimensional metric has closed time-like curves through every point; x4 is a time '
              'function only on the section at fixed extra times; there, the optical metric of the bulk, d sigma^2 + '
              'e^{-2H|sigma|} dx^2, is the hyperbolic plane of radius 1/H and the fold a horocycle: the earliest bulk signal '
              'over Dx arrives after T = (2/H) arcsinh(H Dx/2) < Dx (H Dx = 0.5, 2, 10, 100: T = %s, the shortest path found '
              'by minimisation %s, along the fold %s); over one light year (%.2e s along the fold) a bulk signal needs '
              '%.1e s for H = 1e-9 GeV and %.1e s for H = 4e-13 GeV' % (
                  ['%.1e' % c['max_ds2_over_R2'] for c in ctc], [c['w'] for c in ctc],
                  ['%.4f' % r['T_exact'] for r in res4], ['%.4f' % r['T_path'] for r in res4],
                  ['%.1f' % r['dx'] for r in res4], short[0]['T_along_the_fold_s'], short[0]['T_one_light_year_s'],
                  short[1]['T_one_light_year_s']))

    # ---------------- SL5: ESTIMATE, Lorentz violation in the Standard Model through loops of chi
    sv_gev = SIGMAV_PAIR / GEV2_TO_CM3S
    rows5 = []
    for wbg in (1500.0, 3000.0, 10000.0):           # the lepton portals can give the relic density above about 1.5 TeV
        nf = 9
        g2w2 = 2 * math.pi * sv_gev / nf             # g_f^2 omega_b^2 for nine chiral lepton states
        gw2 = math.sqrt(g2w2) * wbg                   # g_f omega_b^2 (dimensionless)
        factor = (gw2 / (16 * math.pi ** 2)) ** 2
        rows5.append({'omega_b_GeV': wbg, 'g_omega_b^2': gw2, 'loop_factor': factor,
                      'max_cb2_minus_1_if_faster': BOUND_EC_FAST / factor, 'max_cb2_minus_1_if_slower': BOUND_EC_SLOW / factor,
                      'min_qb_over_H_if_faster': factor / BOUND_EC_FAST, 'min_qb_over_H_if_slower': factor / BOUND_EC_SLOW,
                      'max_H_GeV_if_faster_qb_0.03_omega_b': 0.03 * wbg * BOUND_EC_FAST / factor})
    out['SL5'] = {'sigma_v_pair_GeV^-2': sv_gev, 'rows': rows5,
                  'bounds': {'electron_faster': BOUND_EC_FAST, 'electron_slower': BOUND_EC_SLOW}}
    rep.check('SL5_loop_estimate', all(r['min_qb_over_H_if_faster'] > 1e13 for r in rows5),
              'ESTIMATE: with lepton portals at the strength of the relic density (sigma v = %.1e GeV^-2 for one chi with one '
              'antichi, nine chiral lepton states) a loop of chi changes the maximal speed of the electron by about '
              '(g omega_b^2/(16 pi^2))^2 (c_b^2 - 1) = %s (c_b^2 - 1) for omega_b = 1.5, 3, 10 TeV, with a sign that is not '
              'computed; the bounds c_e - 1 < 5e-21 (faster: no vacuum Cherenkov radiation of the 5 PeV electrons of the 2010 '
              'Crab flare) and 1 - c_e < 5.6e-20 (slower: synchrotron electrons with gamma = 3e9) require q_b/H above %s '
              '(faster) or %s (slower); with q_b about 0.03 omega_b this means H below %s GeV' % (
                  sv_gev, ['%.1e' % r['loop_factor'] for r in rows5], ['%.1e' % r['min_qb_over_H_if_faster'] for r in rows5],
                  ['%.1e' % r['min_qb_over_H_if_slower'] for r in rows5],
                  ['%.0e' % r['max_H_GeV_if_faster_qb_0.03_omega_b'] for r in rows5]))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'superluminal.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_superluminal.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'superluminal_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
