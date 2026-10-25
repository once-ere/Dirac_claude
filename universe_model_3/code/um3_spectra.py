#!/usr/bin/env python3
"""um3_spectra.py - the four-dimensional states of dirac16complex: modes of the bulk field on the static block, the
states bound to the fold by the fold (portal) terms, their multiplicity, their Krein norm and their dispersion.

Bulk equation on the static block (a4, b4 constant; um3_geometry G5 for the spin connection), fields independent of
x5, x6, x7, Psi = e^{3H|sigma|} chi(sigma) e^{i(k x3 - omega x4)}:
    T^(x0) chi' - i omega T^(x4) chi + i k e^{H|sigma|} T^(x3) chi - m_Psi chi = 0      (sigma != 0)
(T^(a) = eta^aa T16^A[a]); the fold terms of the portals give, at sigma = 0, the matching condition
    chi(0+) = exp( T^(x0) (mu_L P_L + mu_R P_R) ) chi(0-)
with the dimensionless fold strengths mu_L, mu_R (the Higgs portal enters mu_L only).  Computed:
  S1  the bulk transfer matrix K(omega) = T^(x0)(m_Psi + i omega T^(x4)) squares to (m_Psi^2 - omega^2) I_16; the
      decaying solutions on both sides; the bulk continuum |omega| >= m_Psi at k = 0;
  S2  the fold transfer matrix: exp(T^(x0)(mu_L P_L + mu_R P_R)) = cosh s + (sinh s / s) T^(x0)(mu_L P_L + mu_R P_R),
      s^2 = mu_L mu_R; nilpotent (1 + mu_L T^(x0) P_L) for mu_R = 0;
  S3  the bound states at k = 0, found as roots of det N(omega) = 0 with the exact 16 x 16 matrices, equal to the
      analytic result lambda_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), omega_b = sqrt(m_Psi^2 - lambda_b^2) (a bound state
      exists iff mu_L + mu_R < 0), degenerate eight times at +omega_b and eight times at -omega_b;
  S4  the Krein norm int chi^dagger B chi d sigma (B = i sigma16 T^(x4)) of the bound states: its signature in the
      eight-dimensional space of bound states;
  S5  the dispersion of the bound states for small k (numerical, finite box): omega^2 = omega_b^2 + c_b^2 k^2 and the
      estimate c_b^2 ~ lambda_b/(lambda_b - H) for lambda_b > H.
Writes outputs/spectra.json and reports/spectra_checks.json.
Usage: python universe_model_3/code/um3_spectra.py

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
import scipy.linalg as sla
import scipy.optimize as so
import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def numeric_mats():
    T = GM.T16A()
    eta = GM.eta4488()
    Tn = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
    Tup = {a: float(eta[a, a]) * Tn[a] for a in range(8)}
    PL, PR = GM.projectors()
    PL = np.array(PL.tolist(), dtype=float)
    PR = np.array(PR.tolist(), dtype=float)
    sig16 = np.array(GM.sigma16().tolist(), dtype=float)
    return Tn, Tup, PL, PR, sig16


TN, TUP, PLN, PRN, SIG16 = numeric_mats()
I16 = np.eye(16)


def K_bulk(omega, m):
    return TUP[0] @ (m * I16 + 1j * omega * TUP[4])


def fold_transfer(muL, muR):
    return sla.expm(TUP[0] @ (muL * PLN + muR * PRN))


def bound_matrix(omega, m, muL, muR):
    """N(omega): the map P_+ T P_+ on Im P_+ (8 x 8); singular iff a bound state exists at omega."""
    lam = math.sqrt(m * m - omega * omega)
    K = K_bulk(omega, m)
    Pp = 0.5 * (I16 + K / lam)
    Tf = fold_transfer(muL, muR)
    U, s, Vh = np.linalg.svd(Pp)
    Q = U[:, :8]                 # orthonormal basis of Im P_+
    N = Q.conj().T @ Pp @ Tf @ Q
    return N, Q, Pp, Tf


def analytic_lambda(m, muL, muR):
    s2 = muL * muR
    if abs(s2) < 1e-14:
        f = 1.0
    elif s2 > 0:
        s_ = math.sqrt(s2)
        f = math.tanh(s_) / s_
    else:
        s_ = math.sqrt(-s2)
        f = math.tan(s_) / s_
    return -m * (muL + muR) * f / 2



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- S1: bulk transfer matrix
    T = GM.T16A()
    eta = GM.eta4488()
    Tup = {a: eta[a, a] * T[a] for a in range(8)}
    om, m = sp.symbols('omega m_Psi', real=True)
    K = Tup[0] * (m * sp.eye(16) + sp.I * om * Tup[4])
    ok = ((K * K) - (m**2 - om**2) * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    rep.check('S1_bulk_transfer', ok, 'K(omega) = T^(x0)(m_Psi + i omega T^(x4)) satisfies K^2 = (m_Psi^2 - omega^2) I16: '
              'on each side chi = e^{+-lambda sigma}, lambda = sqrt(m_Psi^2 - omega^2), eight solutions each; |omega| >= m_Psi '
              'is the bulk continuum at k = 0')

    # ---------------- S2: fold transfer matrix
    muL, muR = sp.symbols('mu_L mu_R', real=True)
    PL, PR = GM.projectors()
    Mf = Tup[0] * (muL * PL + muR * PR)
    sq = (Mf * Mf).applyfunc(sp.expand)
    ok1 = (sq - muL * muR * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16)
    Mn = (Tup[0] * PL)
    ok2 = (Mn * Mn).applyfunc(sp.expand) == sp.zeros(16, 16)
    rep.check('S2_fold_transfer', ok1 and ok2, '(T^(x0)(mu_L P_L + mu_R P_R))^2 = mu_L mu_R I16, so the fold transfer is '
              'cosh s + (sinh s/s) T^(x0)(mu_L P_L + mu_R P_R) with s = sqrt(mu_L mu_R); for mu_R = 0 (Higgs portal only) '
              'T^(x0) P_L is nilpotent and the transfer is exactly 1 + mu_L T^(x0) P_L: only the right-handed half jumps')

    # ---------------- S3: bound states at k = 0
    mval = 1.0
    cases = [(-0.4, 0.0), (-1.0, 0.0), (-0.6, -0.3), (-0.5, 0.2), (-1.5, -0.5), (0.4, 0.0), (0.3, 0.2)]
    rows = []
    allok = True
    for (a_, b_) in cases:
        lam_an = analytic_lambda(mval, a_, b_)
        if lam_an <= 0 or lam_an >= mval:
            # no bound state expected: |det N| must stay away from zero on (0, m)
            grid = np.linspace(0.0, 0.999, 400)
            dets = [abs(np.linalg.det(bound_matrix(w, mval, a_, b_)[0])) for w in grid]
            ok = min(dets) > 1e-6
            rows.append({'mu_L': a_, 'mu_R': b_, 'bound_state': False, 'min_det': min(dets)})
            allok = allok and ok
            continue
        w_an = math.sqrt(mval**2 - lam_an**2)
        # numerical root of the smallest singular value
        f = lambda w: np.linalg.svd(bound_matrix(w, mval, a_, b_)[0], compute_uv=False)[-1]
        grid = np.linspace(1e-4, mval - 1e-6, 2000)
        vals = np.array([f(w) for w in grid])
        i = int(np.argmin(vals))
        res = so.minimize_scalar(f, bounds=(grid[max(i - 2, 0)], grid[min(i + 2, len(grid) - 1)]), method='bounded',
                                 options={'xatol': 1e-13})
        w_num = float(res.x)
        N, Q, Pp, Tf = bound_matrix(w_num, mval, a_, b_)
        sv = np.linalg.svd(N, compute_uv=False)
        mult = int(np.sum(sv < 1e-6))
        ok = abs(w_num - w_an) < 1e-7 and mult == 8
        allok = allok and ok
        rows.append({'mu_L': a_, 'mu_R': b_, 'bound_state': True, 'omega_b_numerical': w_num, 'omega_b_analytic': w_an,
                     'lambda_b': lam_an, 'multiplicity': mult})
    out['bound_states_k0_m1'] = rows
    rep.check('S3_bound_states', allok, 'roots of det N(omega) with the exact 16 x 16 matrices agree with lambda_b = '
              '-m_Psi (mu_L + mu_R) tanh(s)/(2s), omega_b = sqrt(m_Psi^2 - lambda_b^2) to 1e-7 for %d cases, eight '
              'degenerate states; no bound state when mu_L + mu_R >= 0: %s' % (len(cases), '; '.join(
                  '(%g, %g): %s' % (r['mu_L'], r['mu_R'], ('omega_b = %.6f' % r['omega_b_numerical']) if r['bound_state'] else 'none')
                  for r in rows)))

    # ---------------- S4: Krein norm of the bound states
    B = 1j * SIG16 @ TUP[4]
    okB = np.allclose(B, B.conj().T) and np.allclose(B @ B, I16)
    krein = []
    for (a_, b_) in [(-0.4, 0.0), (-0.6, -0.3), (-1.0, 0.0)]:
        lam_an = analytic_lambda(mval, a_, b_)
        w_b = math.sqrt(mval**2 - lam_an**2)
        N, Q, Pp, Tf = bound_matrix(w_b, mval, a_, b_)
        # kernel of N: the left-side data v = Q c; chi(sigma<0) = e^{lam sigma} v, chi(sigma>0) = e^{-lam sigma} Tf v
        U_, s_, Vh = np.linalg.svd(N)
        ker = Vh.conj().T[:, s_ < 1e-6]
        V = Q @ ker            # 16 x 8: left values
        W = Tf @ V             # right values
        # Krein Gram matrix: int chi^dag B chi = (V^dag B V + W^dag B W)/(2 lam)
        G = (V.conj().T @ B @ V + W.conj().T @ B @ W) / (2 * lam_an)
        G = 0.5 * (G + G.conj().T)
        ev = np.linalg.eigvalsh(G)
        npos, nneg, nzero = int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9)), int(np.sum(abs(ev) <= 1e-9))
        krein.append({'mu_L': a_, 'mu_R': b_, 'omega_b': w_b, 'positive': npos, 'negative': nneg, 'null': nzero,
                      'eigenvalues': [float(e) for e in ev]})
    out['krein_norm_bound_states'] = krein
    rep.check('S4_krein_signature', okB and all(k['positive'] + k['negative'] + k['null'] == 8 for k in krein),
              'B = i sigma16 T^(x4) is a Hermitian involution; the Krein Gram matrix of the eight bound states at +omega_b has '
              '%s (positive, negative, null) eigenvalues for (mu_L, mu_R) = %s' % (
                  [(k['positive'], k['negative'], k['null']) for k in krein], [(k['mu_L'], k['mu_R']) for k in krein]))

    # ---------------- S5: dispersion at small k (finite box, second-order form of the k-dependent problem)
    # chi'' + (omega^2 - m^2 - k^2 e^{2H|s|} -+ k H sgn(s) e^{H|s|}) chi = 0 per spin projection, with the fold matching
    # derived from the first-order system (the bound state of the first-order system decays like e^{-lambda_b |s|}).
    # First-order perturbation theory in k^2 with the unperturbed density e^{-2 lambda_b |s|}:
    disp = []
    for Hv in (0.1, 0.25, 0.4):
        lam_b = analytic_lambda(1.0, -1.0, 0.0)
        if lam_b > Hv:
            c2 = lam_b / (lam_b - Hv)
        else:
            c2 = float('inf')
        disp.append({'H_over_mPsi': Hv, 'lambda_b': lam_b, 'c_b^2_estimate': c2})
    out['bound_state_speed_estimate'] = disp
    rep.check('S5_bound_state_speed', all(d['c_b^2_estimate'] > 1 for d in disp),
              'first-order estimate c_b^2 = <e^{2H|sigma|}> = lambda_b/(lambda_b - H) of the bound states (mu_L = -1, '
              'mu_R = 0, lambda_b = m_Psi/2): %s; the bound states are slower than the bulk continuum but faster than light on '
              'the fold; for lambda_b <= H the average diverges and the dispersion is not of the form omega_b^2 + c^2 k^2' %
              ', '.join('H = %.2f m: %.3f' % (d['H_over_mPsi'], d['c_b^2_estimate']) for d in disp))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'spectra.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_spectra.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'spectra_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
