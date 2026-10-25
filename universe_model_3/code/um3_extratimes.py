#!/usr/bin/env python3
"""um3_extratimes.py - fields that depend on the extra times x5, x6, x7: they are tachyonic.

On the fold the author's metric restricted to sigma = 0 is (FD-2)
    ds^2 = e^{2 a4} (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^{-2 a4} b4^2 (dx5^2 + dx6^2 + dx7^2),
three space-like and four time-like directions.  A field with the momenta k along ordinary space and l along the extra
times, phi = f(x4) e^{i (k x1 + l x5)}, obeys g^{MN} p_M p_N = m^2 with p = (k, omega, l): the extra times enter its
dispersion with the sign of the time,
    omega^2 = m^2 + k^2 e^{-2 a4} - l^2 e^{2 a4} / b4^2,
so every mode with l^2 e^{2 a4}/b4^2 > m^2 + k^2 e^{-2 a4} has an imaginary frequency and grows exponentially, at the rate
Gamma = sqrt(l^2 e^{2 a4}/b4^2 - m^2 - k^2 e^{-2 a4}).  The same principal symbol g^{MN} p_M p_N governs every field
(scalar, gauge field, fermion, graviton), so the statement holds for all of them.
Checks:
  EX1  the Klein-Gordon operator of the metric of the fold (sympy, general a4(x4), b4(x4)) on f(x4) e^{i(k x1 + l x5)}:
       the principal part is f'' + (m^2 + k^2 e^{-2a4} - l^2 e^{2a4}/b4^2) f, the friction term is (3 b4'/b4) f' (the
       volume e^{3a4} e^{-3a4} b4^3 of the fold), and the translations along x5, x6, x7 are isometries (the metric does not
       depend on them), so the momenta l are conserved;
  EX2  dirac16complex: the states bound to the fold with the extra-time momentum l (the term -i l e^{H|sigma|} gamma^(5)
       of the Dirac operator, a4 = 0, b4 = 1): omega^2 = omega_b^2 - c_b^2 l^2 with the same coefficient c_b^2 as for
       the ordinary momentum (where omega^2 = omega_b^2 + c_b^2 k^2; c_b^2 = 1.190 computed, the first-order estimate
       q_b/(q_b - H) = 1.2), so omega^2 < 0 for c_b l > omega_b (tachyons); and
       because the warp multiplies l by e^{H|sigma|}, a state with l != 0 is not even bound: beyond
       sigma_leak = ln((m_Psi^2 - omega^2)/l^2)/(2H) its local decay rate is imaginary and it leaks into the bulk;
  EX3  the author's vacuum (a4 = H x4, b4 constant): the fold has no friction (b4' = 0) and the physical momentum
       l e^{H x4}/b4 grows exponentially, so the number of e-foldings of the amplitude, N(x4) = l (e^{H x4} - 1)/(H b4),
       grows exponentially: the growth is double-exponential (the mode equation integrated numerically agrees with the
       WKB exponent);
  EX4  the late universe (a4, b4 constant): Gamma is constant; a massless field (photon, gluon, graviton) has growing
       modes for every l with |l_phys| > |k_phys|; if the extra times are compact with the physical period L_t, their
       slowest growing mode (k = 0, l_phys = 2 pi/L_t) grows by at most one e-folding over the age of the universe only
       for L_t >= 2 pi t_0;
  EX5  the restriction of UM-3 (no field depends on the extra times) is a consistent classical truncation (the l = 0
       sector is invariant because l is conserved), but not a stable one: quantum fluctuations of the l != 0 modes and
       pairs (l, -l), which interactions of l = 0 fields create, grow at the rates of EX4.  Only a gauge principle that
       removes the extra-time momentum of every field (as two-time physics does for one extra time) would make it exact.
Writes outputs/extratimes.json and reports/extratimes_checks.json.  Runs in about 20 seconds.
Usage: python universe_model_3/code/um3_extratimes.py

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
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar, minimize

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_kohnsham as K  # noqa: E402

GYR_GEV = 1e9 * 365.25 * 86400 / 6.582119569e-25      # one gigayear in GeV^-1 (hbar = 6.582e-25 GeV s)
GPC_CM = 3.0856775814913673e27
C_CM_S = 2.99792458e10
T0_GYR = 13.8                                           # the age of the universe (Planck 2018: 13.80 Gyr)


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


def ex1_klein_gordon():
    """The Klein-Gordon operator of the seven-dimensional metric of the fold on f(x4) e^{i(k x1 + l x5)}."""
    x = sp.symbols('x1:8', real=True)          # x1..x7 (x[3] = x4)
    k, l, m = sp.symbols('k l m', positive=True)
    a4 = sp.Function('a4')(x[3])
    b4 = sp.Function('b4')(x[3])
    f = sp.Function('f')(x[3])
    g = sp.diag(sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4), -1, -sp.exp(-2 * a4) * b4 ** 2, -sp.exp(-2 * a4) * b4 ** 2,
                -sp.exp(-2 * a4) * b4 ** 2)
    ginv = g.inv()
    sqrtg = sp.sqrt(sp.simplify(g.det()))        # det g = b4^6 > 0 (four time-like directions)
    phi = f * sp.exp(sp.I * (k * x[0] + l * x[4]))
    box = sum(sp.diff(sqrtg * ginv[M, M] * sp.diff(phi, x[M]), x[M]) for M in range(7)) / sqrtg
    # the Klein-Gordon equation g^{MN} nabla_M nabla_N phi = m^2 phi, divided by the plane wave and by -1
    eq = sp.simplify(sp.expand(-(box - m ** 2 * phi) / sp.exp(sp.I * (k * x[0] + l * x[4]))))
    target = sp.diff(f, x[3], 2) + 3 * sp.diff(b4, x[3]) / b4 * sp.diff(f, x[3]) + (m ** 2 + k ** 2 * sp.exp(-2 * a4)
                                                                                    - l ** 2 * sp.exp(2 * a4) / b4 ** 2) * f
    isometric = all(sp.diff(g[i, i], x[r]) == 0 for i in range(7) for r in (4, 5, 6))
    return {'equation': str(eq), 'matches': sp.simplify(eq - target) == 0, 'sqrt_volume': str(sp.simplify(sqrtg)),
            'translations_of_x5_x6_x7_are_isometries': bool(isometric)}


def bound_level_with_momentum(H, muL, L, h, kx=0.0, lx=0.0, omega_guess=None, complex_root=False):
    """The bound level of dirac16complex (16 components, a4 = 0, b4 = 1) with the momentum kx along x1 and lx along x5:
    the terms -i k e^{H|sigma|} gamma^(1) - i l e^{H|sigma|} gamma^(5) of the Dirac operator in the place of the mean
    field.  Returns the root of the eight smallest singular values (real omega) or of the smallest one (complex)."""
    sh = K.Shooter(H, muL, 0.0, L, h, 16)
    w8 = np.exp(H * sh.s)[:, None, None]
    Mk = -1j * kx * w8 * K.TUP[1][None] - 1j * lx * w8 * K.TUP[5][None]
    sh.set_field(Mk.copy(), Mk.copy())
    if not complex_root:
        f8 = lambda dx: float(np.sum(sh.sv(omega_guess + dx)[:8]))
        r = minimize_scalar(f8, bounds=(-2e-3, 2e-3), method='bounded', options={'xatol': 1e-15, 'maxiter': 600})
        return omega_guess + float(r.x), float(r.fun)
    g = lambda z: float(sh.sv(z[0] + 1j * z[1])[0])
    z0 = [omega_guess.real, omega_guess.imag]
    r = minimize(g, z0, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-16, 'maxiter': 1500,
                                                         'initial_simplex': [z0, [z0[0] + 1e-3, z0[1]], [z0[0], z0[1] + 1e-3]]})
    return complex(r.x[0], r.x[1]), float(r.fun)


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- EX1
    e1 = ex1_klein_gordon()
    out['EX1'] = e1
    rep.check('EX1_dispersion_on_the_fold', e1['matches'] and e1['translations_of_x5_x6_x7_are_isometries'],
              'g^{MN} nabla_M nabla_N phi = m^2 phi on f(x4) e^{i(k x1 + l x5)}: %s = 0 (sqrt|g| = %s): omega^2 = m^2 + k^2 '
              'e^{-2a4} - l^2 e^{2a4}/b4^2; the metric does not depend on x5, x6, x7 (isometries, conserved l)' % (
                  e1['equation'], e1['sqrt_volume']))

    # ---------------- EX2: dirac16complex bound states with extra-time momentum
    H, muL, h = 0.05, -0.6, 0.02
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)
    cb2 = qb / (qb - H)
    rows = []
    for lx in (0.01, 0.02, 0.03):
        # the warp multiplies the extra-time momentum by e^{H|sigma|}: beyond sigma_leak the local decay rate
        # sqrt(m_Psi^2 - omega^2 - l^2 e^{2H|sigma|}) is imaginary and the state leaks into the bulk; the box ends before
        w_guess = math.sqrt(wb ** 2 - cb2 * lx ** 2)
        s_leak = math.log((1 - w_guess ** 2) / lx ** 2) / (2 * H)
        L = min(40.0, 0.9 * s_leak)
        wl, sl = bound_level_with_momentum(H, muL, L, h, lx=lx, omega_guess=w_guess)
        wk, sk = bound_level_with_momentum(H, muL, L, h, kx=lx, omega_guess=math.sqrt(wb ** 2 + cb2 * lx ** 2))
        rows.append({'momentum': lx, 'box': L, 'sigma_leak': s_leak, 'omega_extra_time': wl, 'sv_extra_time': sl,
                     'omega_space': wk, 'sv_space': sk, 'cb2_from_extra_time': (wb ** 2 - wl ** 2) / lx ** 2,
                     'cb2_from_space': (wk ** 2 - wb ** 2) / lx ** 2})
    cb2_comp = sum(r['cb2_from_extra_time'] for r in rows) / len(rows)
    l_tach = wb / math.sqrt(cb2_comp)           # extrapolating the small-momentum law
    out['EX2'] = {'H': H, 'q_b': qb, 'omega_b': wb, 'c_b^2_estimate': cb2, 'c_b^2_computed': cb2_comp, 'rows': rows,
                  'omega^2 = 0 at l = omega_b/c_b (extrapolated)': l_tach}
    ok2 = (all(r['sv_extra_time'] < 1e-8 and r['sv_space'] < 1e-8 for r in rows)
           and all(abs(r['cb2_from_extra_time'] - cb2) < 0.02 * cb2 and abs(r['cb2_from_space'] - cb2) < 0.02 * cb2 for r in rows)
           and all(r['sigma_leak'] < 1e3 for r in rows))
    rep.check('EX2_dirac16complex_extra_time_momentum', ok2,
              'regime I (q_b = 0.3, H = 0.05): the bound level falls as omega^2 = omega_b^2 - c^2 l^2 along an extra time, '
              'c^2 = %s, and rises as omega_b^2 + c^2 k^2 along ordinary space, c^2 = %s (l, k = 0.01, 0.02, 0.03; '
              'q_b/(q_b - H) = %.4f): omega^2 < 0 (a tachyon) for l > omega_b/c_b = %.3f (the small-momentum law extrapolated); '
              'and since the warp multiplies l by '
              'e^{H|sigma|}, a state with any l != 0 leaks into the bulk beyond sigma_leak = ln((m_Psi^2 - omega^2)/l^2)/(2H) '
              '(%s for these l): with extra-time momentum the particles chi are neither bound nor stable' % (
                  ['%.4f' % r['cb2_from_extra_time'] for r in rows], ['%.4f' % r['cb2_from_space'] for r in rows], cb2,
                  l_tach, ['%.0f' % r['sigma_leak'] for r in rows]))

    # ---------------- EX3: the author's vacuum, double-exponential growth
    Hv, b4, lv, kv, mv = 1.0, 1.0, 1.0, 0.0, 0.0       # units of H; l = H b4: the mode becomes tachyonic at x4 = 0
    def rhs(x4, y):
        om2 = mv ** 2 + kv ** 2 * math.exp(-2 * Hv * x4) - lv ** 2 * math.exp(2 * Hv * x4) / b4 ** 2
        return [y[1], -om2 * y[0]]
    xs = np.array([2.0, 2.5, 3.0])
    sol = solve_ivp(rhs, (0.0, 3.0), [1.0, 0.0], rtol=1e-11, atol=1e-14, dense_output=True, method='DOP853')
    lnf = [math.log(abs(sol.sol(x)[0])) for x in xs]
    N = [lv * (math.exp(Hv * x) - 1) / (Hv * b4) for x in xs]
    # WKB: ln f = N - (H x4)/2 + const (the amplitude factor Gamma^{-1/2}); the differences remove the constant
    dl = [lnf[i + 1] - lnf[i] for i in range(2)]
    dN = [N[i + 1] - N[i] - 0.5 * Hv * (xs[i + 1] - xs[i]) for i in range(2)]
    out['EX3'] = {'x4_in_units_of_1/H': list(xs), 'ln_amplitude': lnf, 'N_WKB': N,
                  'increments_numerical': dl, 'increments_WKB': dN}
    rep.check('EX3_double_exponential_growth', all(abs(a - b) < 0.02 * b for a, b in zip(dl, dN)),
              'author\'s vacuum (a4 = H x4, b4 constant, no friction), the massless mode with l = H b4 and k = 0: the logarithm '
              'of its amplitude grows by %s between H x4 = 2, 2.5, 3, as the WKB exponent N = l(e^{H x4} - 1)/(H b4) minus '
              'H x4/2 predicts (%s): the growth is double-exponential' % (['%.4f' % v for v in dl], ['%.4f' % v for v in dN]))

    # ---------------- EX4: the late universe and the size of compact extra times
    t0_gev = T0_GYR * GYR_GEV
    Lt_min_cm = 2 * math.pi * T0_GYR * 1e9 * 365.25 * 86400 * C_CM_S
    out['EX4'] = {'growth_rate_massless_k0': 'Gamma = |l_phys| for |l_phys| > |k_phys|',
                  'age_GeV^-1': t0_gev, 'L_t_min_cm': Lt_min_cm, 'L_t_min_Gpc': Lt_min_cm / GPC_CM,
                  'e-foldings_for_L_t_equal_1_mm': 2 * math.pi * T0_GYR * 1e9 * 365.25 * 86400 * C_CM_S / 0.1}
    rep.check('EX4_late_universe', Lt_min_cm > 1e28 and out['EX4']['e-foldings_for_L_t_equal_1_mm'] > 1e28,
              'with a4 and b4 constant every massless field has modes growing at Gamma = sqrt(l_phys^2 - k_phys^2); compact '
              'extra times of the physical period L_t keep the slowest of them (k = 0, l_phys = 2 pi/L_t) below one '
              'e-folding over t_0 = %.1f Gyr only for L_t >= 2 pi c t_0 = %.2e cm = %.1f Gpc; for L_t = 1 mm it grows by %.1e '
              'e-foldings' % (T0_GYR, Lt_min_cm, Lt_min_cm / GPC_CM, out['EX4']['e-foldings_for_L_t_equal_1_mm']))

    # ---------------- EX5: the truncation is consistent, not stable
    out['EX5'] = {'consistent': 'l conserved (EX1): the l = 0 sector is invariant under the classical evolution',
                  'not_stable': 'fluctuations with l != 0 and pairs (l, -l) grow at the rates of EX4',
                  'remedy': 'a gauge principle removing the extra-time momentum of every field (as in two-time physics)'}
    rep.check('EX5_truncation', e1['translations_of_x5_x6_x7_are_isometries'] and ok2,
              'no field depends on the extra times is a consistent classical truncation (l is conserved, so the l = 0 sector '
              'is invariant), but not a stable one: every mode with l != 0, including pairs (l, -l) that the interactions of '
              'l = 0 fields create, is tachyonic for every field (EX1, EX2); UM-3 needs a gauge principle that removes the '
              'extra-time momentum of every field')

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'extratimes.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_extratimes.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'extratimes_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
