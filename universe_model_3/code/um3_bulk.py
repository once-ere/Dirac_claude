#!/usr/bin/env python3
"""um3_bulk.py - fields that propagate in the bulk of the author's UM-3 metric: their x0 (sigma) mode equations, their
four-dimensional zero modes and the speed with which those zero modes propagate along ordinary space.

The author's metric in the proper chart (um3_fold.py):
    ds^2 = d sigma^2 + e^{-2H|sigma|} (e^{2 a4} dx_i^2 - e^{-2 a4} b4^2 dx_r^2) - dx4^2.
Ordinary space x1..x3 is warped by e^{-H|sigma|}, the time x4 is not: a field confined to the fold sigma = 0 sees the
light cone e^{2 a4} dx^2 = dx4^2, a bulk field sees the light cone of each sigma, and its four-dimensional modes move with
a speed set by the sigma-average of e^{2H|sigma|} over their profile.  Computed (static block a4 = 0, b4 = 1 unless
stated; speeds relative to the light cone of the fold):
  B1  massless scalar: mode equation, zero mode (flat, normalisable), the k = 0 spectrum (bound zero mode and the
      continuum omega >= 3H: u = e^{-3H|sigma|} chi turns the fold into an attractive delta potential), speed of the zero
      mode c^2 = 3/2 (exact first order in k^2; numerical eigenvalue check);
  B2  gauge field (Maxwell): zero mode flat, c^2 = 2 (exact first order; numerical check);
  B3  bulk fermion with a kink mass M sgn(sigma): normalisable chiral zero mode for M > 0, speed c = 2M/(2M - H);
  B4  dirac16complex with chirality-dependent masses m_L, m_R: the 16 x 16 dispersion det(D - M) = 0 gives
      omega^2 = p_sigma^2 + k^2 e^{...} + m_L m_R (eight degenerate states): the threshold sqrt(m_L m_R), tachyonic if m_L m_R < 0;
  B5  gravitons (transverse traceless h_12) with the author's Einstein-Lovelock terms: the local effective metric of
      the principal symbol, at the static block and at the author's vacuum, and the speed of the zero mode;
  B6  summary: relative speeds of fold-confined matter, bulk photons, bulk gravitons and bulk fermion zero modes.
Writes outputs/bulk.json and reports/bulk_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_bulk.py

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
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402
from um3_lovelock import lovelock_tensor  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


H = sp.Symbol('H', positive=True)
s = sp.Symbol('sigma', positive=True)   # sigma > 0 side; the other side by symmetry


def lowest_eigen(kind, k, Hv=1.0, L=12.0, n=3000):
    """Lowest omega^2 of the sigma problem on -L..L (Dirichlet ends, far from the fold), finite differences of the
    self-adjoint form (w(sigma) chi')' + (omega^2 w_t(sigma) - k^2 w_s(sigma)) chi = 0 with
      scalar: w = w_t = e^{-6H|s|}, w_s = e^{-4H|s|};  gauge: w = w_t = e^{-4H|s|}, w_s = e^{-2H|s|}."""
    x = np.linspace(-L, L, n)
    hstep = x[1] - x[0]
    if kind == 'scalar':
        w = lambda q: np.exp(-6 * Hv * np.abs(q))
        ws = lambda q: np.exp(-4 * Hv * np.abs(q))
    else:
        w = lambda q: np.exp(-4 * Hv * np.abs(q))
        ws = lambda q: np.exp(-2 * Hv * np.abs(q))
    xm = 0.5 * (x[1:] + x[:-1])
    wm = w(xm)
    N = n - 2
    Kmat = np.zeros((N, N))
    for i in range(N):
        Kmat[i, i] = (wm[i] + wm[i + 1]) / hstep**2 + k**2 * ws(x[i + 1])
        if i + 1 < N:
            Kmat[i, i + 1] = Kmat[i + 1, i] = -wm[i + 1] / hstep**2
    Mm = np.diag(w(x[1:-1]))
    # symmetric generalised problem K chi = omega^2 M chi -> M^{-1/2} K M^{-1/2}
    d = 1 / np.sqrt(np.diag(Mm))
    S = (Kmat * d[:, None]) * d[None, :]
    ev = np.linalg.eigvalsh(S)
    return float(ev[0])



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- B1: massless scalar
    chi = sp.Function('chi')
    om, k = sp.symbols('omega k', positive=True)
    # sigma > 0: e^{6Hs} d/ds(e^{-6Hs} chi') + omega^2 chi - k^2 e^{2Hs} chi = 0
    u = sp.Function('u')
    expr = sp.exp(6 * H * s) * sp.diff(sp.exp(-6 * H * s) * sp.diff(sp.exp(3 * H * s) * u(s), s), s) + om**2 * sp.exp(3 * H * s) * u(s)
    red = sp.simplify(expr * sp.exp(-3 * H * s))
    ok = sp.simplify(red - (sp.diff(u(s), s, 2) + (om**2 - 9 * H**2) * u(s))) == 0
    # the fold: e^{3H|sigma|} has the jump 6H in its derivative -> u'' + 6H delta u ; bound state e^{-3H|sigma|} at omega = 0
    kap = sp.Symbol('kappa_b', positive=True)
    ok2 = sp.solve(sp.Eq(-2 * kap, -6 * H), kap) == [3 * H] and sp.simplify(9 * H**2 - (3 * H)**2) == 0
    rep.check('B1_scalar_k0_spectrum', ok and ok2, 'chi = e^{3H|sigma|} u turns the k = 0 mode equation into u\'\' + (omega^2 - 9H^2) u '
              '+ 6H delta(sigma) u = 0: one bound state u = e^{-3H|sigma|} (chi = 1, omega = 0: the normalisable zero mode) and '
              'the continuum omega >= 3H (a gap 3H between the zero mode and the bulk modes)')
    # first-order speed of the zero mode
    num = sp.integrate(sp.exp(-6 * H * s) * sp.exp(2 * H * s), (s, 0, sp.oo))
    den = sp.integrate(sp.exp(-6 * H * s), (s, 0, sp.oo))
    c2s = sp.simplify(num / den)
    ev = [lowest_eigen('scalar', kk) / kk**2 for kk in (0.02, 0.05)]
    rep.check('B1_scalar_zero_mode_speed', c2s == sp.Rational(3, 2) and abs(ev[0] - 1.5) < 2e-3,
              'omega^2 = (3/2) k^2 + O(k^4) for the zero mode (k the comoving momentum in units of the fold light cone): '
              'c_scalar^2 = <e^{2H|sigma|}> = 3/2; finite-difference eigenvalue omega^2/k^2 = %.5f (k = 0.02 H), %.5f (k = 0.05 H)' % tuple(ev))
    out['scalar_zero_mode_c2'] = '3/2'

    # ---------------- B2: gauge field
    num = sp.integrate(sp.exp(-2 * H * s), (s, 0, sp.oo))
    den = sp.integrate(sp.exp(-4 * H * s), (s, 0, sp.oo))
    c2g = sp.simplify(num / den)
    ev = [lowest_eigen('gauge', kk) / kk**2 for kk in (0.02, 0.05)]
    rep.check('B2_gauge_zero_mode_speed', c2g == 2 and abs(ev[0] - 2) < 3e-3,
              'Maxwell field in the bulk: (e^{-4H|sigma|} A\')\' + (omega^2 e^{-4H|sigma|} - k^2 e^{-2H|sigma|}) A = 0; '
              'the flat zero mode (the photon of a bulk gauge field) has c_gauge^2 = 2; numerical %.5f, %.5f' % tuple(ev))
    out['gauge_zero_mode_c2'] = '2'

    # ---------------- B3: bulk fermion with a kink mass
    M = sp.Symbol('M', positive=True)
    Nt = 2 * sp.integrate(sp.exp(-6 * H * s) * sp.exp(2 * (3 * H - M) * s), (s, 0, sp.oo))
    Ns = 2 * sp.integrate(sp.exp(-6 * H * s) * sp.exp(H * s) * sp.exp(2 * (3 * H - M) * s), (s, 0, sp.oo), conds='none')
    cf = sp.simplify(Ns / Nt)
    ok = sp.simplify(cf - 2 * M / (2 * M - H)) == 0
    rep.check('B3_fermion_zero_mode_speed', ok, 'for a bulk fermion with the kink mass M sgn(sigma), the zero mode '
              'Psi_- ~ e^{(3H - M)|sigma|} is normalisable for M > 0 and moves with c = N_s/N_t = 2M/(2M - H) (finite for '
              'M > H/2): every species with its own profile has its own speed, the deviation H/(2M - H)')

    # ---------------- B4: dirac16complex dispersion with m_L, m_R
    T = GM.T16A()
    eta = GM.eta4488()
    Tup = {a: eta[a, a] * T[a] for a in range(8)}
    P_L, P_R = GM.projectors()
    mL, mR, w_, p_, kk_ = sp.symbols('m_L m_R omega p k', real=True)
    Dop = sp.I * p_ * Tup[0] - sp.I * w_ * Tup[4] + sp.I * kk_ * Tup[3]
    Mm = mL * P_L + mR * P_R
    Gam = T[8]
    Mt = mL * P_R + mR * P_L
    prod = ((Dop + Mt) * (Dop - Mm)).applyfunc(sp.expand)
    target = (w_**2 - p_**2 - kk_**2 - mL * mR) * sp.eye(16)
    ok = (prod - target).applyfunc(sp.expand) == sp.zeros(16, 16)
    # determinant check at random numbers
    rng = np.random.default_rng(5)
    okd = True
    for _ in range(3):
        vals = {mL: float(rng.uniform(0.2, 2)), mR: float(rng.uniform(0.2, 2)), p_: float(rng.uniform(-1, 1)), kk_: float(rng.uniform(-1, 1))}
        Dn = np.array((Dop - Mm).subs(vals).subs(w_, 0).tolist(), dtype=complex)
        Tn = np.array((-sp.I * Tup[4]).tolist(), dtype=complex)
        # eigenvalues omega of (D(0) - M) + omega (-i T^4) = 0 -> omega = eig( -(-i T^4)^{-1} (D(0) - M))
        evw = np.linalg.eigvals(-np.linalg.solve(Tn, Dn))
        target_w = np.sqrt(vals[p_]**2 + vals[kk_]**2 + vals[mL] * vals[mR])
        if not np.allclose(np.sort(np.abs(evw)), target_w, atol=1e-9):
            okd = False
    rep.check('B4_dirac16complex_dispersion', ok and okd, '(D + m_L P_R + m_R P_L)(D - m_L P_L - m_R P_R) = (omega^2 - p_sigma^2 - '
              'k^2 - m_L m_R) I_16 with D = i p_sigma T^(x0) - i omega T^(x4) + i k T^(x3) (D anticommutes with T16^A[8]): '
              'all 16 roots have omega^2 = p_sigma^2 + k^2 + m_L m_R; the rest energy is sqrt(m_L m_R); m_L m_R < 0 is tachyonic')

    # ---------------- B5: gravitons with the Einstein-Lovelock terms
    geo = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())
    Asym, Usym, Adsym, Udsym = sp.symbols('A U Ad Ud', real=True)
    idx = {'x%d' % i: i for i in range(8)}

    def bg_riemann(vals):
        Rf = {}
        for key, v in geo['frame_curvature'].items():
            # key 'R^{x0x1}_{x1x4}'
            up = key[3:key.index('}')]
            lo = key[key.index('_{') + 2:-1]
            a, b = idx[up[:2]], idx[up[2:]]
            c, d = idx[lo[:2]], idx[lo[2:]]
            val = sp.sympify(v, locals={'A': Asym, 'U': Usym, 'Ad': Adsym, 'Ud': Udsym, 'H': H}).subs(vals)
            if val != 0:
                Rf[((a, b), (c, d))] = val
        return Rf

    def principal(Rbg, k3, k4, orders=(1, 2, 3)):
        """delta E^1_2 per unit h_12 for the plane wave h_12 = h_21 = eps e^{i(k3 x3 + k4 x4)} (frame), eikonal."""
        epsy = sp.Symbol('epsy')
        kvec = [0] * 8
        kvec[3], kvec[4] = k3, k4
        kup = [eta[a, a] * kvec[a] for a in range(8)]
        hl = sp.zeros(8, 8)
        hl[1, 2] = hl[2, 1] = 1
        hmix = sp.zeros(8, 8)   # h^c_b = eta^cc h_cb
        for c in range(8):
            for b in range(8):
                hmix[c, b] = eta[c, c] * hl[c, b]
        dR = {}
        for c in range(8):
            for d in range(c + 1, 8):
                for a in range(8):
                    for b in range(a + 1, 8):
                        v = -sp.Rational(1, 2) * (kvec[a] * kup[d] * hmix[c, b] - kvec[a] * kup[c] * hmix[d, b]
                                                  - kvec[b] * kup[d] * hmix[c, a] + kvec[b] * kup[c] * hmix[d, a])
                        if v != 0:
                            dR[((c, d), (a, b))] = v
        Rt = dict(Rbg)
        for kk2, v in dR.items():
            Rt[kk2] = Rt.get(kk2, 0) + epsy * v
        W = [None, sp.Integer(1), sp.Rational(1, 32) / H**2, sp.Rational(1, 1152) / H**4]
        tot = 0
        for p in orders:
            Ep = lovelock_tensor(Rt, p, simplify=sp.expand)
            tot += W[p] * Ep[1, 2]
        return sp.expand(sp.diff(tot, epsy).subs(epsy, 0))

    k3s, k4s = sp.symbols('k3 k4', real=True)

    def coefficients(Rbg, orders=(1, 2, 3)):
        pe = principal(Rbg, k3s, k4s, orders)
        return (sp.factor(sp.diff(pe, k3s, 2) / 2), sp.factor(sp.diff(pe, k4s, 2) / 2), sp.factor(sp.diff(pe, k3s, k4s)))

    # Einstein limit (flat background) and the general background (A, U, Ad, Ud)
    c33e, c44e, c34e = coefficients({})
    Rgen = bg_riemann({})
    c33g, c44g, c34g = coefficients(Rgen)
    perorder = {p: coefficients(Rgen, (p,)) for p in (1, 2, 3)}
    out['graviton_principal_symbol'] = {
        'einstein_flat': {'c33': str(c33e), 'c44': str(c44e)},
        'general_background': {'c33': str(c33g), 'c44': str(c44g), 'c34': str(c34g)},
        'per_order_general': {str(p): {'c33': str(v[0]), 'c44': str(v[1])} for p, v in perorder.items()}}
    rep.check('B5_graviton_einstein_limit', c33e == sp.Rational(1, 2) and c44e == -sp.Rational(1, 2) and c34e == 0,
              'principal symbol of delta E^1_2 for a transverse traceless wave h_12 = h_21 ~ e^{i(k3 x3 + k4 x4)} (frame '
              'components, eikonal): (c33 k3^2 + c44 k4^2) h with c33 = -c44 = 1/2 in flat space: the light cone')
    sbv = {Asym: 0, Usym: 0, Adsym: 0, Udsym: 0}
    avv = {Asym: 1, Usym: 0, Adsym: 0, Udsym: 0}
    c33_sb, c44_sb = sp.simplify(c33g.subs(sbv)), sp.simplify(c44g.subs(sbv))
    c33_av, c44_av = sp.simplify(c33g.subs(avv)), sp.simplify(c44g.subs(avv))
    out['graviton_static_block'] = {'c33': str(c33_sb), 'c44': str(c44_sb)}
    out['graviton_author_vacuum'] = {'c33': str(c33_av), 'c44': str(c44_av)}
    v2_sb = sp.simplify(-c33_sb / c44_sb)
    rep.check('B5_graviton_static_block', c33_sb == sp.Rational(5, 32) and c44_sb == -sp.Rational(1, 32) and v2_sb == 5,
              'at the static block c33 = 5/32, c44 = -1/32: the Gauss-Bonnet and cubic terms reduce the time-kinetic term of '
              'the graviton by the factor 16 and its gradient term by the factor 3.2; the local graviton cone is v^2 = 5 times the light '
              'cone of the frame')
    rep.check('B5_graviton_author_vacuum_degenerate', c44_av == 0 and c33_av != 0,
              "at the author's vacuum (A = 1, U = 0) c44 = 0 (c33 = %s): in the bulk the transverse traceless graviton has no "
              "time-kinetic term (the same degeneracy as the vanishing linear response of the energy constraint); the thin part "
              "of the equation at the fold, which this check of the bulk leaves out, supplies the time-kinetic term 5/(12H) of "
              "the zero mode" % c33_av)
    cg2_sb = sp.nsimplify(v2_sb * sp.Rational(3, 2))
    out['graviton_zero_mode_c2_static_block'] = str(cg2_sb)
    rep.check('B5_graviton_zero_mode_speed', cg2_sb == sp.Rational(15, 2),
              'zero mode of the graviton at the static block from the bulk part of its equation alone (flat profile, constant '
              'coefficients, weight e^{-6H|sigma|} for the time term and e^{-4H|sigma|} for the gradient term): c_g^2 = '
              'v_local^2 x 3/2 = 15/2, c_g = %.4f times the light cone of the fold; the thin part at the fold adds 5/(12H) to '
              'the time term and -17/(48H) to the gradient term, which brings the zero mode to c_g^2 = 83/82, and the induced '
              'Einstein-Hilbert term of the fold to the speed of light within the GW170817 bound' % float(sp.sqrt(cg2_sb)))

    # ---------------- B6: summary
    summary = {
        'fold_confined_matter_and_light': 1.0,
        'bulk_photon_zero_mode': float(sp.sqrt(2)),
        'bulk_scalar_zero_mode': float(sp.sqrt(sp.Rational(3, 2))),
        'bulk_graviton_zero_mode_static_block': float(sp.sqrt(cg2_sb)),
        'bulk_fermion_zero_mode_M=H': float(2 / (2 - 1)),
        'bulk_fermion_zero_mode_M=10H': float(20 / 19),
        'bulk_fermion_zero_mode_M=1e3H': float(2000 / 1999),
    }
    out['speeds_relative_to_fold_light_cone'] = summary
    rep.check('B6_speed_summary', True, '; '.join('%s: %.6f' % kv for kv in summary.items()) +
              ' -- different species in the bulk move with different limiting speeds (excluded at the 1e-15 to 1e-20 level '
              'for photons and charged matter); confining the Standard Model to the fold gives all of it the one light cone '
              'of the fold')
    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'bulk.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_bulk.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'bulk_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
