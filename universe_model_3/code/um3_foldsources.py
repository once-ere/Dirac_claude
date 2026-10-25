#!/usr/bin/env python3
"""um3_foldsources.py - the sources of the fold: the Einstein-Hilbert term of the fold and the fold fluid.

The metric of the fold region in the proper chart (um3_fold.py),
    ds^2 = d sigma^2 + e^{2 fa} dx_i^2 - e^{2 fn} dx4^2 - e^{2 fb} dx_r^2,
with the author's fa = a4 - H|sigma|, fb = ln b4 - a4 - H|sigma|, fn = 0, carries a transverse traceless graviton of the
+ polarisation travelling along x3,  g_11 = e^{2 fa + eps h},  g_22 = e^{2 fa - eps h},  h = h(sigma, x3, x4).  The metric stays
diagonal, so the exact Lovelock machinery of um3_lovelock.py applies.  Computed and checked (author's weights
w = (1, 1/32, 1/1152), alpha_p = w_p H^(2-2p), Lambda = -10 H^2; TT = (E^1_1 - E^2_2)/2 at first order in eps):
  F1  the linearised equation is linear in the second sigma-derivatives (fa_ss, fb_ss, fn_ss, h_ss) and their
      coefficients form an exact differential in the first sigma-derivatives (a junction potential exists); away from
      the fold it reproduces the bulk principal symbol of um3_bulk.py (B5): (1/32) h_tt - (5/32) h_33 at the static block
      (frame), no time-kinetic term at the author's vacuum;
  F2  the thin part at the kinked fold (the integral of TT across the fold): with frozen extra times (any a4' = A H, the
      static block included) kappa Pi = (5/(12H)) h_tt - (17/(48H)) h_33 + (19/16) A h_t - ((5 + A^2 + Ad)/32) [h_sigma], at the
      author's vacuum (5/(12H)) h_tt - (13/(24H)) h_33 - (1/4)[h_sigma]: the Gauss-Bonnet and cubic terms of the author's
      action give the fold its own graviton kinetic term (Einstein gravity alone gives none); checked by smoothing the kink;
  F3  the four-dimensional graviton (the zero mode, flat in sigma; the thin part included): K_tt = 1/(96H) + 5/(12H) =
      41/(96H), K_33 = -5/(64H) - 17/(48H) = -83/(192H), c_g^2 = 83/82 for frozen extra times (the bulk alone: 15/2, B5);
      at the author's vacuum the fold restores the time-kinetic term, c_g^2 = 19/10;
  F4  with the induced Einstein-Hilbert term of the fold (IN-9) of strength kappa_4: c_g^2 = (96 + 83 eps_r)/(96 + 82 eps_r),
      eps_r = kappa_4 V*/(kappa H); GW170817 ((c_g - c)/c < 7e-16) requires eps_r < 1.34e-13; the Planck mass of the
      gravitational waves and that of the Friedmann equation differ by the factor 1 + eps_r/48;
  F5  the Einstein-Hilbert term induced by the fields of the fold (Sakharov; one loop, heat kernel, proper-time cutoff
      Lambda): 1/(16 pi G_ind) = N Lambda^2/(192 pi^2), N = sum over real scalars (1 - 6 xi) + Weyl fermions - 4 x gauge
      fields (from tr(E + R/6) of each operator, ghosts included); the Standard Model with three nu_R has N = 4(1 - 6 xi_H):
      the 48 Weyl fermions and the 12 gauge fields cancel exactly; the measured Planck mass needs Lambda = sqrt(24) pi M_red
      = 3.75e19 GeV at xi_H = 0, and xi_H < 1/6;
  F6  the fold fluid: the static fold source kappa S = diag(-61/8, -31/4, -61/8) H (um3_fold J5) is a tension
      lambda_F = 61 H V*/(8 kappa) plus a pressureless static energy density rho_d = H V*/(8 kappa) (1/62 of it); the
      vacuum energy of the fold fields (the potential at its minimum; fields independent of the extra times, so that
      T^r_r is the on-shell Lagrangian) is a seven-dimensional tension; the pressureless part is not separately conserved
      when the fold expands, and the energy it needs, 3 a4' rho_d, is exactly the part of the jump of the bulk energy flux
      at the fold that is linear in a4' (frozen extra times): it belongs to the bulk medium.
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
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


X = sp.symbols('x0:8', real=True)
SIG, X3, X4 = X[0], X[3], X[4]
H = sp.Symbol('H', positive=True)
EPS = sp.Symbol('eps')
W = [None, sp.Integer(1), sp.Rational(1, 32), sp.Rational(1, 1152)]
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


def tt_operator():
    """TT = sum_p alpha_p (E_(p)^1_1 - E_(p)^2_2)/2 at first order in eps, in the derivative symbols."""
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
    TT = 0
    per = {}
    for p in (1, 2, 3):
        Ep = lovelock_tensor(Rs, p, simplify=sp.expand)
        tt1 = sp.expand(sp.diff(sp.expand((Ep[1, 1] - Ep[2, 2]) / 2), EPS).subs(EPS, 0))
        per[p] = tt1
        TT += ALPHA[p] * tt1
    return sp.expand(TT), per


def author(side, hs, extra=None):
    """The author's metric on one side of the fold (side = -1: sigma < 0; +1: sigma > 0); a4 = 0 at the instant."""
    v = {S['fa_s']: -H * side, S['fb_s']: -H * side, S['fn_s']: 0, S['fa_st']: 0, S['fb_st']: 0, S['fn_st']: 0,
         S['fn_t']: 0, S['fn_tt']: 0, S['fa_t']: A * H, S['fb_t']: (U - A) * H, S['fa_tt']: Ad * H**2,
         S['fb_tt']: (Ud - Ad) * H**2, S['fn0']: 0, S['h_s']: hs}
    if extra:
        v.update(extra)
    return v



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- F1: the linearised TT equation
    TT, per = tt_operator()
    second = [S['fa_ss'], S['fb_ss'], S['fn_ss'], S['h_ss']]
    first = [S['fa_s'], S['fb_s'], S['fn_s'], S['h_s']]
    poly = sp.Poly(TT, *second)
    linear = all(sum(m) <= 1 for m in poly.monoms())
    C = [sp.expand(sp.diff(TT, v)) for v in second]
    smooth = sp.expand(TT - sum(c * v for c, v in zip(C, second)))
    exact = all(sp.expand(sp.diff(C[i], first[j]) - sp.diff(C[j], first[i])) == 0 for i in range(4) for j in range(i + 1, 4))
    lam = sp.Symbol('lam')
    integrand = sum(C[k].subs({first[m]: lam * first[m] for m in range(4)}, simultaneous=True) * first[k] for k in range(4))
    F = sp.expand(sp.integrate(sp.expand(integrand), (lam, 0, 1)))
    exact = exact and all(sp.expand(sp.diff(F, first[k]) - C[k]) == 0 for k in range(4))
    # the bulk operator on a flat profile (h_s = h_ss = h_st = 0), sigma > 0, a4 = 0 at the instant (fa0 = -H sigma)
    bulk = sp.expand(smooth.subs(author(+1, 0, {S['h_ss']: 0, S['h_st']: 0})))
    ctt_b = sp.expand(sp.diff(bulk, S['h_tt']))
    c33_b = sp.expand(sp.diff(bulk, S['h_33']))
    ct_b = sp.expand(sp.diff(bulk, S['h_t']))
    sb = {A: 0, U: 0, Ad: 0, Ud: 0}
    av = {A: 1, U: 0, Ad: 0, Ud: 0}
    # frame normalisation at the point (fa0 = 0) for the comparison with um3_bulk.py B5
    ok_b5 = (sp.simplify(ctt_b.subs(sb).subs(S['fa0'], 0) - sp.Rational(1, 32)) == 0
             and sp.simplify(c33_b.subs(sb).subs(S['fa0'], 0) + sp.Rational(5, 32)) == 0
             and sp.simplify(ctt_b.subs(av)) == 0 and sp.simplify(c33_b.subs(av)) != 0)
    out['tt_bulk_coefficients'] = {'h_tt': str(sp.factor(ctt_b)), 'h_33': str(sp.factor(c33_b)), 'h_t': str(sp.factor(ct_b))}
    rep.check('F1_linearised_tt_equation', linear and exact and ok_b5,
              'TT = sum_p alpha_p (E^1_1 - E^2_2)/2 (first order in the + polarisation h along x3) is linear in fa_ss, fb_ss, '
              'fn_ss, h_ss with coefficients that are an exact differential in the first sigma-derivatives (a junction '
              'potential exists); away from the fold, at the static block, it is (1/32) h_tt - (5/32) e^{-2fa} h_33 (the bulk '
              'principal symbol of um3_bulk.py B5: c44 = -1/32, c33 = 5/32, local cone v^2 = 5), and at the author\'s vacuum '
              'its h_tt coefficient vanishes (no time-kinetic term)')

    # ---------------- F2: the thin part at the fold
    Jf = sp.expand(F.subs(author(+1, HS_P)) - F.subs(author(-1, HS_M)))
    Jf0 = sp.expand(Jf.subs(S['fa0'], 0))
    jcoef = {k: sp.factor(sp.expand(sp.diff(Jf0, S[k]))) for k in ('h_tt', 'h_33', 'h_t')}
    jcoef['jump'] = sp.factor(sp.expand(sp.diff(Jf0, HS_P)))
    jcoef_m = sp.factor(sp.expand(sp.diff(Jf0, HS_M)))
    rest = sp.expand(Jf0 - sum(sp.diff(Jf0, S[k]) * S[k] for k in ('h_tt', 'h_33', 'h_t')) - sp.diff(Jf0, HS_P) * HS_P
                     - jcoef_m * HS_M)
    fro = {U: A, Ud: Ad}
    thin_frozen = {k: sp.simplify(v.subs(fro)) for k, v in jcoef.items()}
    thin_av = {k: sp.simplify(v.subs(av)) for k, v in jcoef.items()}
    ok_jump = sp.simplify(jcoef_m + jcoef['jump']) == 0 and rest == 0
    ok_frozen = (thin_frozen['h_tt'] == sp.Rational(5, 12) / H and thin_frozen['h_33'] == -sp.Rational(17, 48) / H
                 and sp.simplify(thin_frozen['h_t'] - sp.Rational(19, 16) * A) == 0
                 and sp.simplify(thin_frozen['jump'] + (5 + A**2 + Ad) / 32) == 0)
    ok_av = thin_av['h_tt'] == sp.Rational(5, 12) / H and thin_av['h_33'] == -sp.Rational(13, 24) / H
    einstein_thin = {k: sp.expand(sp.diff(F.subs(author(+1, HS_P)) - F.subs(author(-1, HS_M)), S[k]))
                     for k in ('h_tt', 'h_33')}
    # Einstein gravity alone (p = 1): no thin kinetic term
    TT1 = sp.expand(per[1])
    C1 = [sp.expand(sp.diff(TT1, v)) for v in second]
    integ1 = sum(C1[k].subs({first[m]: lam * first[m] for m in range(4)}, simultaneous=True) * first[k] for k in range(4))
    F1p = sp.expand(sp.integrate(sp.expand(integ1), (lam, 0, 1)))
    J1p = sp.expand(F1p.subs(author(+1, HS_P)) - F1p.subs(author(-1, HS_M)))
    ok_einstein = sp.diff(J1p, S['h_tt']) == 0 and sp.diff(J1p, S['h_33']) == 0
    # numerical check by smoothing the kink: fa_s = fb_s = -H tanh(sigma/w)
    mp.mp.dps = 30
    TTn = sp.expand(TT)
    worst = 0.0
    okn = True
    for (Av, Uv) in ((0.0, 0.0), (1.0, 0.0), (0.3, 0.3)):
        base = {H: 1, S['fn_s']: 0, S['fn_ss']: 0, S['fa_st']: 0, S['fb_st']: 0, S['fn_st']: 0, S['fn_t']: 0,
                S['fn_tt']: 0, S['fn0']: 0, S['fa_t']: Av, S['fb_t']: Uv - Av, S['fa_tt']: 0, S['fb_tt']: 0,
                S['h_s']: 0, S['h_ss']: 0, S['h_st']: 0}
        for coef in ('h_tt', 'h_33'):
            e = TTn.subs(base).subs({S[c]: (1 if c == coef else 0) for c in ('h_tt', 'h_33', 'h_t')})
            f = sp.lambdify((S['fa_s'], S['fb_s'], S['fa_ss'], S['fb_ss'], S['fa0']), e, 'mpmath')
            exact_v = float(jcoef[coef].subs({H: 1, A: Av, U: Uv, Ad: 0, Ud: 0}))
            res = []
            for wv in (1e-4, 1e-5):
                gfun = lambda s_: f(-mp.tanh(s_ / wv), -mp.tanh(s_ / wv), -(1 / wv) * mp.sech(s_ / wv)**2,
                                    -(1 / wv) * mp.sech(s_ / wv)**2, -wv * mp.log(mp.cosh(s_ / wv)))
                res.append(float(mp.quad(gfun, [-40 * wv, -wv, 0, wv, 40 * wv])))
            d1, d2 = abs(res[0] - exact_v), abs(res[1] - exact_v)
            worst = max(worst, d2)
            okn = okn and d2 < 1e-3 and d2 < 0.2 * d1 + 1e-12
    out['thin_part'] = {'general': {k: str(v) for k, v in jcoef.items()},
                        'frozen_extra_times': {k: str(v) for k, v in thin_frozen.items()},
                        'author_vacuum': {k: str(v) for k, v in thin_av.items()}}
    rep.check('F2_thin_part_at_the_fold', linear and ok_jump and ok_frozen and ok_av and ok_einstein and okn,
              'the integral of TT across the fold: with frozen extra times (b4\'/b4 = a4\' = A H, any A, the static block '
              'A = 0 included) kappa Pi = (5/(12H)) h_tt - (17/(48H)) h_33 + (19/16) A h_t - ((5 + A^2 + Ad)/32)[h_sigma]; at the author\'s '
              'vacuum (5/(12H)) h_tt - (13/(24H)) h_33 - (1/4)[h_sigma]; Einstein gravity alone has no h_tt, h_33 term at the '
              'fold, so the graviton kinetic term of the fold comes from the Gauss-Bonnet and cubic terms; smoothing the kink '
              '(fa_s = fb_s = -H tanh(sigma/w)) and integrating the full equation reproduces it (deviation %.1e at w = 1e-5, '
              'falling linearly with w)' % worst)

    # ---------------- F3: the four-dimensional graviton (zero mode)
    # sqrt|g| = e^{3 fa + fn + 3 fb} = e^{-6H|sigma|} (a4 = 0, b4 = 1); fa0 = -H|sigma|
    sg = sp.Symbol('s', positive=True)
    weight = sp.exp(-6 * H * sg)
    Ktt_b = 2 * sp.integrate(weight * ctt_b.subs(S['fa0'], -H * sg), (sg, 0, sp.oo))
    K33_b = 2 * sp.integrate(weight * c33_b.subs(S['fa0'], -H * sg), (sg, 0, sp.oo))
    Ktt = {nm: sp.simplify(Ktt_b.subs(v) + jcoef['h_tt'].subs(v)) for nm, v in (('frozen', fro), ('av', av))}
    K33 = {nm: sp.simplify(K33_b.subs(v) + jcoef['h_33'].subs(v)) for nm, v in (('frozen', fro), ('av', av))}
    cg2 = {nm: sp.simplify(-K33[nm] / Ktt[nm]) for nm in Ktt}
    cg2_bulk = sp.simplify(-K33_b.subs(sb) / Ktt_b.subs(sb))
    thin_v2 = sp.simplify(-thin_frozen['h_33'] / thin_frozen['h_tt'])
    out['zero_mode'] = {'K_tt_frozen': str(Ktt['frozen']), 'K_33_frozen': str(K33['frozen']), 'c_g^2_frozen': str(cg2['frozen']),
                        'K_tt_author_vacuum': str(Ktt['av']), 'K_33_author_vacuum': str(K33['av']),
                        'c_g^2_author_vacuum': str(cg2['av']), 'c_g^2_bulk_alone_static_block': str(cg2_bulk),
                        'thin_part_cone_v^2': str(thin_v2), 'thin_share_of_time_kinetic_term':
                        str(sp.simplify(thin_frozen['h_tt'] / Ktt['frozen']))}
    ok3 = (sp.simplify(Ktt['frozen'] - sp.Rational(41, 96) / H) == 0 and sp.simplify(K33['frozen'] + sp.Rational(83, 192) / H) == 0
           and cg2['frozen'] == sp.Rational(83, 82) and cg2_bulk == sp.Rational(15, 2) and thin_v2 == sp.Rational(17, 20)
           and cg2['av'] == sp.Rational(19, 10) and sp.simplify(Ktt['av'] - sp.Rational(5, 12) / H) == 0)
    rep.check('F3_four_dimensional_graviton', ok3,
              'the zero mode (flat in sigma, weight sqrt|g| = e^{-6H|sigma|}) with the thin part: K_tt = 1/(96H) + 5/(12H) = '
              '41/(96H), K_33 = -5/(64H) - 17/(48H) = -83/(192H) for frozen extra times (any A): c_g^2 = 83/82, c_g = %.6f c '
              '(the bulk alone gives 15/2, um3_bulk.py B5; the thin part alone 17/20; the fold carries 40/41 of the '
              'time-kinetic term); at the author\'s vacuum the bulk has no time-kinetic term but the fold has, K_tt = 5/(12H): '
              'c_g^2 = 19/10' % math.sqrt(83 / 82))

    # ---------------- F4: with the induced Einstein-Hilbert term of the fold
    er = sp.Symbol('eps_r', positive=True)
    # (V*/kappa) [K_tt h_tt + K_33 h_33] + (1/kappa_4)(1/2)(h_tt - h_33),  eps_r = kappa_4 V*/(kappa H)
    num = sp.Rational(1, 2) + er * H * (-K33['frozen'])
    den = sp.Rational(1, 2) + er * H * Ktt['frozen']
    cg2_ind = sp.simplify(num / den)
    ok4a = sp.simplify(cg2_ind - (96 + 83 * er) / (96 + 82 * er)) == 0
    bound_v = 7e-16                                          # GW170817: -3e-15 < (c_g - c)/c < 7e-16
    # c_g/c - 1 = delta  <=>  c_g^2 - 1 = x = 2 delta + delta^2 = eps_r/(96 + 82 eps_r)  <=>  eps_r = 96 x/(1 - 82 x)
    xg = 2 * bound_v + bound_v**2
    eps_max = 96 * xg / (1 - 82 * xg)
    ok4a = ok4a and sp.simplify(((96 + 83 * er) / (96 + 82 * er) - 1).subs(er, sp.Float(eps_max, 30)) - xg) < 1e-28
    MT_over_MF = sp.simplify((1 + 2 * er * H * Ktt['frozen']) / (1 + sp.Rational(5, 6) * er))
    out['induced_gravity_gw_speed'] = {'c_g^2': str(cg2_ind), 'GW170817_upper_(c_g-c)/c': bound_v, 'eps_r_max': eps_max,
                                       'M_T^2/M_F^2': str(MT_over_MF)}
    rep.check('F4_gravitational_wave_speed', ok4a and 1.3e-13 < eps_max < 1.4e-13
              and sp.simplify(MT_over_MF - (1 + sp.Rational(41, 48) * er) / (1 + sp.Rational(5, 6) * er)) == 0,
              'with the induced Einstein-Hilbert term of the fold (IN-9; its kinetic term (1/kappa_4)(h_tt - h_33)/2 has the '
              'light cone) the four-dimensional graviton has c_g^2 = (96 + 83 eps_r)/(96 + 82 eps_r), eps_r = kappa_4 V*/(kappa H): '
              'GW170817, (c_g - c)/c < 7e-16, requires eps_r < %.3e; the Planck mass of the gravitational waves, '
              '(1 + 41 eps_r/48)/kappa_4, differs from that of the Friedmann equation, (1 + 5 eps_r/6)/kappa_4, by the factor '
              '1 + eps_r/48 to first order' % eps_max)

    # ---------------- F5: the Einstein-Hilbert term induced by the fold fields (Sakharov)
    xi, R_ = sp.symbols('xi R')
    # tr(E + R/6) for Laplace-type operators D = -(nabla^2 + E):  scalar E = -xi R; Dirac D^2 = -nabla^2 + R/4 (4x4);
    # Maxwell in Feynman gauge E^mu_nu = -R^mu_nu (trace -R) with two scalar ghosts (minus sign)
    a1_scalar = (-xi * R_ + R_ / 6)
    a1_dirac = 4 * (-R_ / 4 + R_ / 6)
    a1_vector = (-R_ + 4 * R_ / 6) - 2 * (R_ / 6)
    # effective weights relative to a minimal real scalar (fermion loops with the opposite sign; Weyl = half a Dirac)
    w_scalar = sp.simplify(a1_scalar / (R_ / 6))
    w_weyl = sp.simplify(-a1_dirac / 2 / (R_ / 6))
    w_vector = sp.simplify(a1_vector / (R_ / 6))
    n_s, n_w, n_v = 4, 48, 12            # Higgs doublet (4 real), 3 x 16 Weyl fermions (with nu_R), 8 + 3 + 1 gauge fields
    N = sp.expand(n_s * w_scalar + n_w * w_weyl + n_v * w_vector)
    N_no_nuR = sp.expand(n_s * w_scalar + 45 * w_weyl + n_v * w_vector)
    M_red = 2.435e18                     # reduced Planck mass (GeV), (8 pi G_N)^(-1/2)
    # 1/(16 pi G) = N Lambda^2/(192 pi^2)  ->  M_red^2 = 1/(8 pi G) = N Lambda^2/(96 pi^2)
    Lam = math.sqrt(96 * math.pi**2 / float(N.subs(xi, 0))) * M_red
    out['sakharov'] = {'weight_scalar': str(w_scalar), 'weight_weyl': str(w_weyl), 'weight_vector': str(w_vector),
                       'N_SM_with_nuR': str(N), 'N_SM_without_nuR': str(N_no_nuR), 'Lambda_GeV_xi0': Lam,
                       'Lambda_over_M_Pl': Lam / 1.22089e19}
    ok5 = (w_scalar == 1 - 6 * xi and w_weyl == 1 and w_vector == -4 and N == 4 - 24 * xi
           and abs(Lam - math.sqrt(24) * math.pi * M_red) < 1e10)
    rep.check('F5_induced_gravity_of_the_fold_fields', ok5,
              'the one-loop effective action of the fold fields with a proper-time cutoff Lambda contains the Einstein-Hilbert '
              'term 1/(16 pi G_ind) = N Lambda^2/(192 pi^2), N = sum (1 - 6 xi) over real scalars + (number of Weyl fermions) - 4 x '
              '(number of gauge fields) (from tr(E + R/6); Weyl %s, gauge field with ghosts %s); for the Standard Model with three '
              'nu_R N = %s: the 48 Weyl fermions cancel the 12 gauge fields exactly (without nu_R N = %s); the measured Planck mass '
              'needs Lambda = sqrt(24) pi M_red = %.3e GeV = %.2f M_Pl at xi_H = 0, and xi_H < 1/6 for the right sign' % (
                  w_weyl, w_vector, N, N_no_nuR, Lam, Lam / 1.22089e19))

    # ---------------- F6: the fold fluid
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    stat = {k: sp.sympify(v, locals={'H': H}) for k, v in fold['fold_source_static_block'].items()}
    # kappa S^a_b (mixed, frame) = diag(p, -rho, q): static block
    kp, krho, kq = stat['x1,x1'], -stat['x4,x4'], stat['x5,x5']        # S^1_1 = p, S^4_4 = -rho, S^5_5 = q
    lambda_F = -kp                                                      # the tension: p = q = -lambda_F
    rho_d = sp.simplify(krho - lambda_F)
    ok6a = sp.simplify(kp - kq) == 0 and lambda_F == sp.Rational(61, 8) * H and rho_d == H / 8
    # vacuum energy of fold fields independent of the extra times: T_MN = -2 dL/dg^MN + g_MN L; along the extra times the
    # fields have no derivatives, so T^r_r = L; at the minimum L = -V_min, and the four-dimensional part is -V_min delta:
    Vmin = sp.Symbol('V_min', positive=True)
    Tvac = {'p': -Vmin, 'rho': Vmin, 'q': -Vmin}
    ok6b = Tvac['p'] == -Tvac['rho'] and Tvac['q'] == -Tvac['rho']
    # conservation with frozen extra times: D_a S^a_4 = -(rho' + 3 a4'(rho + p)); the static part loses 3 A H (rho_d)
    fro_src = {k: sp.sympify(v, locals={'H': H, 'A': A, 'Ad': Ad}) for k, v in fold['fold_source_frozen'].items()}
    flux_jump = sp.Rational(3, 8) * A * (1 + A**2) * H**2                # [kappa T^sigma_4] with frozen extra times (J6, J7)
    static_loss = 3 * A * H * (krho + kp)                               # 3 a4' kappa (rho_s + p_s)
    ok6c = sp.simplify(static_loss - sp.expand(flux_jump).coeff(A, 1) * A) == 0 and sp.simplify(static_loss - 3 * A * H**2 / 8) == 0
    # and the whole frozen source is balanced by the whole flux (um3_fold J6), the A^3 part by the A^3 part (J7)
    rho_f = -fro_src['x4,x4']
    p_f = fro_src['x1,x1']
    a4 = sp.Function('a4')(X4)
    sub_t = {A: sp.diff(a4, X4) / H, Ad: sp.diff(a4, X4, 2) / H**2}
    lhs = sp.diff(rho_f.subs(sub_t), X4) + 3 * sp.diff(a4, X4) * (rho_f + p_f).subs(sub_t)
    ok6d = sp.simplify(lhs - flux_jump.subs(sub_t)) == 0
    out['fold_fluid'] = {'kappa_lambda_F': str(lambda_F), 'kappa_rho_d': str(rho_d), 'fraction_rho_d': str(rho_d / krho),
                         'bulk_flux_jump_frozen': str(flux_jump), 'static_part_energy_need': str(static_loss)}
    rep.check('F6_fold_fluid', ok6a and ok6b and ok6c and ok6d,
              'the static fold source kappa S = diag(p, -rho, q) = (-61/8, -31/4, -61/8) H is a tension kappa lambda_F = 61H/8 '
              '(p = q = -lambda_F) plus a pressureless static density kappa rho_d = H/8 (1/62 of the energy; p = q = 0); the '
              'vacuum energy of fields of the fold that do not depend on the extra times is a seven-dimensional tension '
              '(T^r_r = on-shell L = -V_min, T^mu_nu = -V_min delta); when the fold expands with frozen extra times the static '
              'part needs the energy 3 a4\' rho_d per time, and the jump of the bulk energy flux at the fold, kappa [T^sigma_4] = '
              '(3/8) A (1 + A^2) H^2, supplies exactly that with its linear part (and the rest of the source with the rest: '
              'rho\' + 3 a4\'(rho + p) = [T^sigma_4] for the whole frozen source)')

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
