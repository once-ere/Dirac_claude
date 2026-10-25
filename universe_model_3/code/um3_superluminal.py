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
  SL1  the small-momentum coefficient c_b^2 computed exactly (16-component shooting at k = 0.01) against the estimate
       q_b/(q_b - H), at three points (regime I, a stronger warp, the weakly bound point K9);
  SL2  the whole dispersion of the bound level up to k = 30 m_Psi (regime I): omega/k decreases towards 1 from above (the
       momentum term k^2 (e^{2H|sigma|} - 1), about 2 H k^2 |sigma| near the fold, confines the state to the fold like a
       linear potential, so omega - k grows only like k^{1/3}); the group velocity d omega/dk exceeds the speed of light for
       ultrarelativistic chi (k above a few m_Psi), by at most a few parts in a thousand, and tends to 1 at large k: the
       front velocity of the particles chi is the speed of light;
  SL3  the particles chi of the cosmological history are slow: the group velocity at the momentum of a halo particle
       (k = 10^-3 omega_b) and at a thermal momentum of the freeze-out (k = sqrt(3 omega_b T), T = omega_b/25) is far below 1;
  SL4  causality: x4 is a time function of the whole metric (every causal curve has dx4 != 0), so there are no closed causal
       curves; but the bulk is a shortcut between points of the fold: the optical metric d sigma^2 + e^{-2H|sigma|} dx^2 is
       the hyperbolic plane of radius 1/H and the fold one of its horocycles, so the earliest arrival of a bulk signal over
       the coordinate distance Dx on the fold is T(Dx) = (2/H) arcsinh(H Dx/2) < Dx (numerically: the shortest null path
       found by minimisation over paths agrees);
  SL5  ESTIMATE: Lorentz violation passed to the Standard Model through loops of chi with the portal couplings of the relic
       abundance, delta c ~ (g omega_b^2/(16 pi^2))^2 (c_b^2 - 1), against the bounds on the maximal speed of electrons;
       the binding this requires, H/q_b.
Writes outputs/superluminal.json and reports/superluminal_checks.json.  Runs in about 3 minutes.
Usage: python universe_model_3/code/um3_superluminal.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one fold, at z = pi/2. A point of the fold is labelled by the seven coordinates x1, ..., x7, and the
metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. Four properties make the surface sigma = 0 a fold, and together they single it
out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|), which multiplies ordinary space and
     the extra times, equals 1 on the fold and decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0;
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function); it jumps by -2 H along ordinary space and along the extra times. The Einstein-Lovelock equations are
     linear in the second sigma-derivatives of the metric, so the jump puts a Dirac delta function delta_D(sigma) into
     them: the metric solves them only if the fold carries a thin source S^a_b, an energy-momentum tensor concentrated on
     sigma = 0 (the junction conditions). At the author's vacuum (a4' = H, b4 constant) its frame components along (ordinary space, the
     time, the extra times) are kappa S = (-10 H, -6 H, -10 H), at the static late-time state (a4 and b4 constant)
     kappa S = (-61 H/8, -31 H/4, -61 H/8), with kappa = 8 pi G_8 the gravitational coupling of eight dimensions. The fold
     is therefore not only a place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the ad hoc vacuum, the gauge fields of
SU(3)_C x SU(2)_L x U(1)_Y, three generations of quarks and leptons and three right-handed neutrinos), the fold fluid and
the induced Einstein-Hilbert term of the fold live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no
field depends on the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we
observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex and gravity live in the
bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that the fold holds,
and the portals couple dirac16complex to the Standard Model at sigma = 0. In UM-3 files the word fold means this surface
and nothing else: a number of equal energy levels is written as a number of degenerate states, and a growth by powers of
Euler's number as a logarithm.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2 diverges, and
     which lies at an infinite proper distance from both: in proper distance every copy has its own complete line
     -infinity < sigma < infinity. This is why the period pi/(6 H) of x0 produces no Kaluza-Klein tower with the spacing
     12 H; the x0 mass of the bound states is their binding to the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every function of UM-3 that depends on sigma
     through |sigma| is folded at sigma = 0: the metric functions of FD-4 and the profiles of the bound states of
     dirac16complex (example 7).
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
     the bulk the vacuum energy Lambda_RS. The fold of UM-3 is of the same kind; it differs in that the time x4 is not
     warped, three extra times are warped together with ordinary space, and the Lovelock terms add to the junction
     conditions.
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a folded wave function: it falls
     off exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order
     Dirac equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex
     bound to the fold; at rest and without their self-interaction (the field is
     Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi: the four bound states of Krein charge -1 (the particles chi) are even under it and the four of Krein
     charge +1 are odd, so the mean field of the gas cannot mix the two signs of the indefinite charge. R_2 maps the bound
     states of one Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory on an interval (a circle whose points are identified with their mirror
     images), the two ten-dimensional planes left in place by the reflection are mirror surfaces (property 1); the gauge
     fields E8 x E8 live on them while gravity fills the bulk. This is the arrangement of UM-3, where the Standard Model
     lives on the fold and gravity and dirac16complex fill the bulk.

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp vanishes, g_x0x0
    diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a kink
    and without a thin source.
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
BOUND_EC_FAST = 1.2e-17      # electrons faster than light: inverse Compton, E_max/m = 2e8 (Crab), 1/(2 (E/m)^2)
BOUND_EC_SLOW = 6e-20        # electrons slower than light: synchrotron, gamma_max = 3e9 (Crab), 1/(2 gamma^2)


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


def moving_level(H, muL, k, guess, width, L=None, h=None):
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
    xs = np.linspace(guess - width, guess + width, 41)
    vals = [f(x) for x in xs]
    best = None
    for i in range(1, 40):
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
              'chi have a limiting speed above that of light on the fold, slightly below the estimate' % (
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
    vg = [{'k': 0.5 * (a['k'] + b['k']), 'v_group': (b['omega'] - a['omega']) / (b['k'] - a['k'])} for a, b in zip(disp[:-1], disp[1:])]
    vmax = max(vg, key=lambda r: r['v_group'])
    above = [r['k'] for r in vg if r['v_group'] > 1]
    out['SL2'] = {'dispersion': disp, 'group_velocity': vg, 'v_max': vmax, 'window_v_above_1': [min(above), max(above)] if above else None,
                  'omega_over_k_at_30': disp[-1]['omega'] / disp[-1]['k']}
    ratios = [d['omega'] / d['k'] for d in disp[1:]]
    excess = [(d['k'], d['omega'] - d['k']) for d in disp if d['k'] >= 10]
    expo = math.log(excess[-1][1] / excess[0][1]) / math.log(excess[-1][0] / excess[0][0])
    out['SL2']['omega_minus_k_exponent_k10_to_k30'] = expo
    ok2 = (all(d['sv'] < 1e-6 for d in disp) and all(r2 < r1 for r1, r2 in zip(ratios[5:], ratios[6:]))
           and 1 < disp[-1]['omega'] / disp[-1]['k'] < 1.02 and 1 < vmax['v_group'] < 1.01 and 1 <= vg[-1]['v_group'] < vmax['v_group']
           and 0.15 < expo < 0.4)
    rep.check('SL2_dispersion', ok2,
              'regime I, k = 0 ... 30 m_Psi: omega/k falls towards 1 from above (%.4f at k = 10, %.4f at k = 30); omega - k grows '
              'like k^%.2f between k = 10 and 30 (k^{1/3} for a linear confining potential 2 H k^2 |sigma|); the group '
              'velocity d omega/dk is above 1 from k = %.2f m_Psi on, with the maximum %.4f at k = %.1f, and returns towards 1 '
              '(%.4f at k = 25): ultrarelativistic chi move faster than light on the fold by at most %.1e, and the front '
              'velocity (k -> infinity) is the speed of light' % (
                  disp[13]['omega'] / disp[13]['k'], disp[-1]['omega'] / disp[-1]['k'], expo,
                  (min(above) if above else float('nan')), vmax['v_group'], vmax['k'], vg[-1]['v_group'], vmax['v_group'] - 1))

    # ---------------- SL3: the particles of the cosmological history are slow
    cb2 = sl1[0]['c_b^2_computed']
    k_halo = 1e-3 * wb
    k_fo = math.sqrt(3 * wb * wb / 25)
    v_halo = cb2 * k_halo / math.sqrt(wb * wb + cb2 * k_halo ** 2)
    # at the freeze-out momentum, the group velocity from the computed dispersion (interpolated)
    kk = np.array([d['k'] for d in disp])
    ww = np.array([d['omega'] for d in disp])
    v_fo = float(np.interp(k_fo, [r['k'] for r in vg], [r['v_group'] for r in vg]))
    out['SL3'] = {'k_halo': k_halo, 'v_halo': v_halo, 'k_freeze_out': k_fo, 'v_freeze_out': v_fo}
    rep.check('SL3_cosmological_chi_are_slow', v_halo < 2e-3 and v_fo < 0.6 and (not above or min(above) > k_fo),
              'regime I: a halo particle (k = 1e-3 omega_b) moves at %.2e, a thermal one at the freeze-out (k = sqrt(3 omega_b T), '
              'T = omega_b/25, k = %.3f) at %.3f: the group velocity exceeds 1 only for relativistic chi (k above %.2f m_Psi), '
              'which exist only before the freeze-out' % (v_halo, k_fo, v_fo, min(above) if above else float('nan')))

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
    # x4 is a time function: on every causal direction of the metric, dx4^2 >= d sigma^2 + e^{-2H|sigma|} dx^2 > 0 unless
    # the direction lies entirely along the extra times, which are time-like as well (dx4 and dx_r together)
    out['SL4'] = {'shortest_bulk_signal': res4}
    rep.check('SL4_causality_and_bulk_shortcut', all(r['T_path'] >= r['T_exact'] * (1 - 1e-6) and r['T_path'] < r['T_exact'] * 1.02
                                                     and r['T_exact'] < r['dx'] for r in res4),
              'the optical metric of the bulk, d sigma^2 + e^{-2H|sigma|} dx^2, is the hyperbolic plane of radius 1/H and the fold '
              'a horocycle: the earliest bulk signal over Dx arrives after T = (2/H) arcsinh(H Dx/2) < Dx (H Dx = 0.5, 2, 10, 100: '
              'T = %s, the shortest path found by minimisation %s, along the fold %s); x4 is a time function of the metric, so '
              'there are no closed causal curves, but the bulk is a shortcut between points of the fold' % (
                  ['%.4f' % r['T_exact'] for r in res4], ['%.4f' % r['T_path'] for r in res4], ['%.1f' % r['dx'] for r in res4]))

    # ---------------- SL5: ESTIMATE, Lorentz violation in the Standard Model through loops of chi
    sv_gev = SIGMAV_PAIR / GEV2_TO_CM3S
    rows5 = []
    for wbg in (1500.0, 3000.0, 10000.0):           # the lepton portals can give the relic density above about 1.5 TeV
        nf = 9
        g2w2 = 2 * math.pi * sv_gev / nf             # g_f^2 omega_b^2 for nine chiral lepton states
        gw2 = math.sqrt(g2w2) * wbg                   # g_f omega_b^2 (dimensionless)
        factor = (gw2 / (16 * math.pi ** 2)) ** 2
        rows5.append({'omega_b_GeV': wbg, 'g_omega_b^2': gw2, 'loop_factor': factor,
                      'max_cb2_minus_1_fast': BOUND_EC_FAST / factor, 'max_cb2_minus_1_slow': BOUND_EC_SLOW / factor,
                      'max_H_over_qb_fast': BOUND_EC_FAST / factor})
    out['SL5'] = {'sigma_v_pair_GeV^-2': sv_gev, 'rows': rows5, 'bounds': {'electron_faster': BOUND_EC_FAST, 'electron_slower': BOUND_EC_SLOW}}
    rep.check('SL5_loop_estimate', all(r['max_H_over_qb_fast'] < 1e-8 for r in rows5),
              'ESTIMATE: with lepton portals at the strength of the relic density (sigma v = %.1e GeV^-2 for one chi with one '
              'antichi, nine chiral lepton states) a loop of chi changes the maximal speed of the electron by about '
              '(g omega_b^2/(16 pi^2))^2 (c_b^2 - 1) = %s (c_b^2 - 1) for omega_b = 1.5, 3, 10 TeV; the bounds |c_e - 1| < '
              '1.2e-17 (faster, inverse Compton) and 6e-20 (slower, synchrotron) then require c_b^2 - 1 = H/(q_b - H) below %s: '
              'the binding must be tight, q_b/H above %s' % (
                  sv_gev, ['%.1e' % r['loop_factor'] for r in rows5], ['%.0e' % r['max_H_over_qb_fast'] for r in rows5],
                  ['%.0e' % (1 / r['max_H_over_qb_fast']) for r in rows5]))

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
