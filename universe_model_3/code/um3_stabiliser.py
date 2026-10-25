#!/usr/bin/env python3
"""um3_stabiliser.py - the stabiliser of the bulk: the source that a static bulk of the author's metric requires, checked
in every respect that the document STABILISER states.

The author's metric in the proper chart of the hidden direction (sigma the signed proper distance from the fold):
    ds^2 = d sigma^2 + e^{2 fa} (dx1^2 + dx2^2 + dx3^2) - e^{2 fn} dx4^2 - e^{2 fb} (dx5^2 + dx6^2 + dx7^2),
    fa = a4(x4) - H|sigma|,  fb = ln b4(x4) - a4(x4) - H|sigma|,  fn = 0,
and the field equations of the bulk (sigma != 0), Einstein-Lovelock gravity with the author's weights w_(1) = 1,
w_(2) = 1/32, w_(3) = 1/1152, alpha_(p) = w_(p) H^{2-2p}, and Lambda = -10 H^2:
    sum_{p=1}^{3} alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b          (frame components, kappa = 8 pi G_8),
E_(p) the Lovelock tensor of order p.  With A = a4'/H and U = b4'/(b4 H) (constant rates, a4'' = b4'' = 0 except where
stated) the left-hand side is a polynomial in A and U.
Checks:
  ST1  the static bulk (A = U = 0, a4 and b4 constant): the left-hand side is H^2 diag(-5/16, -5/16, -5/16, -5/16, 1/16,
       -5/16, -5/16, -5/16) in the order (sigma, x1, x2, x3, x4, x5, x6, x7), with no energy flux: the static bulk is a
       solution only with the source kappa T = that, a medium at rest with the energy density kappa rho_s = -H^2/16 and the
       isotropic pressure kappa p_s = -5 H^2/16 = 5 kappa rho_s: the stabiliser;
  ST2  the author's vacuum (A = 1, U = 0): the left-hand side vanishes: the primordial bulk needs no stabiliser;
  ST3  without any bulk source, the bulk with constant rates (A, U) solves the equations only at the real points listed
       (the author's vacuum among them); none has 0 <= A < 1/2: a slowly expanding universe needs a bulk source;
  ST4  the stabiliser is conserved by itself on the static bulk: the covariant divergence nabla_M T^M_N of the constant
       tensor diag(p_s, p_s, p_s, p_s, -rho_s, p_s, p_s, p_s) vanishes for every N (its pressure is the same in every
       warped direction and the time is not warped); it exerts no force on anything but through the metric;
  ST5  energy conditions and models: rho_s < 0 and rho_s + p_s = 6 rho_s < 0 (the weak and the null energy condition fail);
       a homogeneous canonical scalar field (rho = K + V, p = K - V, K >= 0) cannot have p = 5 rho with rho < 0, a scalar
       with negative kinetic energy (a ghost, K = 3 rho_s, V = -2 rho_s) can;
  ST6  history: a medium that couples only to gravity obeys nabla_M T^M_4 = 0; for a homogeneous medium with the pressure p
       in every warped direction this is rho' = -3 (b4'/b4) (rho + p), so with p = 5 rho, rho is proportional to b4^-18:
       a stabiliser absent in the author's vacuum stays absent.  The source that the field equations require while the
       universe expands with frozen extra times (U = A) has kappa T^sigma_4 = (3/16) A (1 + A^2) H^2 sgn(sigma): the energy
       current -T^sigma_4 points towards the fold on both sides, so for A > 0 energy flows from the bulk source into the
       fold at the rate kappa [T^sigma_4] = (3/8) A (1 + A^2) H^2 per unit area of the fold: away from the static bulk the
       stabiliser exchanges energy with the fold, and only the total of the bulk source and the fold source is conserved.
       The energy budget: with frozen extra times only ordinary space grows, and the required source releases the energy
       -3 a4' (rho_bulk + p_1) = (9/8) A (1 + A^2) H^3/kappa per unit volume and time (p_1 its pressure along x1,
       kappa (rho_bulk + p_1) = -(3/8)(1 + A^2) H^2); integrated over sigma with the volume weight e^{-6 H |sigma|} this is
       exactly the jump of the flux; its part linear in A, (3/8) A H^2, is the energy 3 a4' rho_d that the pressureless
       part kappa rho_d = H/8 of the fold fluid (the static fold source minus the tension kappa lambda_F = 61 H/8) needs to
       keep its density while the fold grows; and the whole source of the fold (um3_fold.py J5, read from outputs/fold.json)
       takes up exactly the jump: rho_S' + 3 a4' (rho_S + p_S) = [T^sigma_4] for frozen extra times and any a4(x4)
       (rho_S = -S^4_4, p_S = S^1_1; at constant A kappa S = -(19A^2 + 61) H/8, -(10A^2 + 31) H/4, -(2A^4 + 37A^2 + 61) H/8
       along ordinary space, the time and the extra times);
  ST7  why UM-3 needs it: (a) ST3; (b) the alternative, the author's vacuum as the late universe with H = H_0, would make
       every coupling of the fold drift, g^2 proportional to e^{3 H_0 x4}: Delta ln alpha = 3 H_0 Delta t = 0.37 over the
       1.8 Gyr since the natural reactor of Oklo, against the bound |Delta alpha/alpha| below 1e-7; (c) integrated over
       the hidden direction and the extra times the stabiliser carries rho_4 = rho_s V_* /(3H) = -H V_*/(48 kappa) per
       unit volume of ordinary space of the fold (the static block as a whole does not make the fold expand);
  ST8  the energy constraint: the (x4, x4) component of the bulk equations contains no second time derivative (it is free
       of A1 = A'/H and U1 = U'/H for any a4(x4), b4(x4)): kappa T^4_4 = -kappa rho_bulk = (H^2/16) P(A, U) with
       P = 5A^6 - 15A^5 U + 15A^4 U^2 - 9A^4 - 5A^3 U^3 + 18A^3 U + 3A^2 - 9A U^3 - 3A U - 3U^2 + 1; without a bulk source
       P = 0 at every instant, and the smallest value of A^2 + U^2 on P = 0 is 0.2607 (at (A, U) = +-(0.1432, 0.4901)),
       the smallest value of max(|A|, |U|) on P = 0 is 0.4771 (at (A, U) = +-(0.2385, 0.4771)): at no instant can both
       rates of a sourceless bulk be below 0.477 H; with frozen extra times (U = A, any a4(x4)) P = 1 - 3A^2, so
       3 a4'^2 = H^2 + 16 kappa rho_bulk = 16 kappa (rho_bulk - rho_s): the stabiliser is the energy density of the bulk
       at which ordinary space stands still (a bulk source of zero energy density would need a4' = H/sqrt(3));
       the other components at constant A: kappa T = -(H^2/16) (3A^4 + 18A^2 + 5, 9A^2 + 5 [x3], 3A^2 - 1, 3A^4 + 24A^2 + 5
       [x3]) along (sigma; x1, x2, x3; x4; x5, x6, x7): the pressures change at the order A^2 and become anisotropic;
       the (sigma, x4) component is also free of A1 and U1: kappa T^sigma_4 = (3/16) U G(A, U) H^2 sgn(sigma) for any
       a4(x4), b4(x4), with G = 5A^2(A - U)^2 - 6A^2 + 6AU + U^2 + 1: no energy flows along sigma while b4 is constant;
       with frozen extra times the flow is (3/16) A (1 + A^2) H^2 sgn(sigma), zero only at A = 0, where P = 1, so a bulk
       without any source cannot have frozen extra times.
Writes outputs/stabiliser.json and reports/stabiliser_checks.json.  Runs in about 40 seconds.
Usage: python universe_model_3/code/um3_stabiliser.py

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

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_fold as FO  # noqa: E402

H = FO.H
A, U, Ad, Ud = FO.A, FO.U, FO.Ad, FO.Ud
H0_KM_S_MPC = 67.4           # Planck 2018
MPC_KM = 3.0856775814913673e19
GYR_S = 1e9 * 365.25 * 86400
OKLO_GYR = 1.8               # the age of the natural reactor of Oklo
OKLO_BOUND = 1e-7            # |Delta alpha/alpha| (conservative)


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


def bulk_lhs(L, side, vals):
    """The left-hand side of the bulk equations on one side of the fold for the author's metric with the rates vals."""
    sub = FO.author_values(side)
    out = sp.zeros(8, 8)
    for i in range(8):
        for j in range(8):
            out[i, j] = sp.simplify(sp.expand(L[i, j].subs(sub).subs(vals)))
    return out


def divergence_diag(g, X, Tdiag):
    """nabla_M T^M_N for a diagonal metric g and a diagonal mixed tensor T^M_M = Tdiag[M] (functions of X)."""
    n = len(X)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                              for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    div = []
    for N in range(n):
        e = sp.diff(Tdiag[N], X[N])
        e += sum(Gam[M][M][P] * (Tdiag[P] if P == N else 0) for M in range(n) for P in range(n))
        e -= sum(Gam[P][M][N] * (Tdiag[M] if M == P else 0) for M in range(n) for P in range(n))
        div.append(sp.simplify(e))
    return div


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    Rs, E, L = FO.general_lhs()
    t_lhs = time.time() - t0

    # ---------------- ST1: the static bulk
    st = {}
    for side in (-1, 1):
        M = bulk_lhs(L, side, {A: 0, U: 0, Ad: 0, Ud: 0})
        st[side] = M
    diag = [sp.nsimplify(st[1][i, i] / H ** 2) for i in range(8)]
    offd = [st[s][i, j] for s in (-1, 1) for i in range(8) for j in range(8) if i != j]
    target = [sp.Rational(-5, 16)] * 4 + [sp.Rational(1, 16)] + [sp.Rational(-5, 16)] * 3
    same_sides = all(sp.simplify(st[1][i, i] - st[-1][i, i]) == 0 for i in range(8))
    kappa_rho = -diag[4] * H ** 2          # T^4_4 = -rho
    kappa_p = diag[0] * H ** 2
    out['ST1'] = {'lhs_over_H2_static': [str(x) for x in diag], 'kappa_rho_s': str(kappa_rho), 'kappa_p_s': str(kappa_p),
                  'off_diagonal_zero': all(x == 0 for x in offd), 'same_on_both_sides': same_sides}
    rep.check('ST1_static_bulk_requires_the_stabiliser', diag == target and all(x == 0 for x in offd) and same_sides
              and sp.simplify(kappa_p - 5 * kappa_rho) == 0,
              'a4, b4 constant: sum_p alpha_p E_(p) + Lambda = H^2 diag%s (sigma, x1, x2, x3, x4, x5, x6, x7) on both sides of '
              'the fold, no flux: the static bulk requires kappa rho_s = %s, kappa p_s = %s = 5 kappa rho_s' % (
                  tuple(str(x) for x in diag), kappa_rho, kappa_p))

    # ---------------- ST2: the author's vacuum
    av = bulk_lhs(L, 1, {A: 1, U: 0, Ad: 0, Ud: 0})
    av2 = bulk_lhs(L, -1, {A: 1, U: 0, Ad: 0, Ud: 0})
    zero_av = all(av[i, j] == 0 and av2[i, j] == 0 for i in range(8) for j in range(8))
    out['ST2'] = {'author_vacuum_lhs_zero': zero_av}
    rep.check('ST2_absent_in_the_author_vacuum', zero_av,
              'a4 = H x4, b4 constant (A = 1, U = 0): every component of sum_p alpha_p E_(p) + Lambda vanishes on both sides of '
              'the fold: the primordial bulk is a vacuum solution and needs no stabiliser')

    # ---------------- ST3: vacuum solutions with constant rates
    gen = bulk_lhs(L, 1, {Ad: 0, Ud: 0})
    comps = sorted({sp.factor(sp.expand(gen[i, j] / H ** 2)) for i in range(8) for j in range(8) if gen[i, j] != 0},
                   key=lambda e: len(str(e)))
    sols = sp.solve(list(comps), [A, U], dict=True)
    real = []
    for s_ in sols:
        a_, u_ = complex(s_[A]), complex(s_[U])
        if abs(a_.imag) < 1e-12 and abs(u_.imag) < 1e-12:
            real.append((round(a_.real, 12), round(u_.real, 12)))
    real = sorted(set(real))
    out['ST3'] = {'components_over_H2': [str(c) for c in comps], 'real_vacuum_points_A_U': real}
    rep.check('ST3_no_slowly_expanding_vacuum', (1.0, 0.0) in real and not any(0 <= a_ < 0.5 for a_, u_ in real),
              'with constant rates the bulk without a source solves the equations only at (A, U) = %s: the author\'s vacuum '
              '(1, 0) is one of them, and none has 0 <= A < 1/2' % real)

    # ---------------- ST4: the stabiliser is conserved by itself on the static bulk
    X = sp.symbols('x0:8', real=True)
    sig = X[0]
    a0, lb0 = sp.symbols('a0 lb0', real=True)
    gS = sp.diag(1, *[sp.exp(2 * (a0 - H * sig))] * 3, -1, *[-sp.exp(2 * (lb0 - a0 - H * sig))] * 3)   # sigma > 0
    rho_s, p_s = sp.symbols('rho_s p_s', real=True)
    Tst = [p_s] * 4 + [-rho_s] + [p_s] * 3
    div = divergence_diag(gS, X, Tst)
    out['ST4'] = {'divergence': [str(x) for x in div]}
    rep.check('ST4_conserved_by_itself', all(x == 0 for x in div),
              'nabla_M T^M_N of the constant tensor diag(p_s, p_s, p_s, p_s, -rho_s, p_s, p_s, p_s) on the static bulk: %s for '
              'N = sigma, x1, ..., x7' % [str(x) for x in div])

    # ---------------- ST5: energy conditions and scalar models
    krho = -sp.Rational(1, 16)
    kp = -sp.Rational(5, 16)
    K, V = sp.symbols('K V', real=True)
    sol_can = sp.solve([sp.Eq(K - V, 5 * (K + V))], [V], dict=True)[0]
    rho_can = sp.simplify((K + V).subs(sol_can))
    ghost = {'K': 3 * krho, 'V': -2 * krho}
    out['ST5'] = {'kappa_rho_over_H2': str(krho), 'kappa_rho_plus_p_over_H2': str(krho + kp), 'scalar_with_p_5rho': {
        'V': str(sol_can[V]), 'rho': str(rho_can)}, 'ghost_model_over_H2_per_kappa': {k: str(v) for k, v in ghost.items()}}
    rep.check('ST5_energy_conditions', krho < 0 and krho + kp < 0 and rho_can == K / 3
              and sp.simplify(ghost['K'] - ghost['V'] - 5 * (ghost['K'] + ghost['V'])) == 0 and ghost['K'] + ghost['V'] == krho,
              'kappa rho_s = %s H^2 < 0 and kappa(rho_s + p_s) = %s H^2 < 0: the weak and the null energy conditions fail; a '
              'homogeneous scalar with p = 5 rho has V = %s and rho = %s, positive for a canonical field (K >= 0), so only a '
              'scalar with negative kinetic energy K = 3 rho_s, V = -2 rho_s (a ghost) reproduces the stabiliser' % (
                  krho, krho + kp, sol_can[V], rho_can))

    # ---------------- ST6: the history
    x4 = X[4]
    a4f = sp.Function('a4')(x4)
    b4f = sp.Function('b4')(x4)
    rhof = sp.Function('rho')(x4)
    pf = sp.Function('p')(x4)
    gG = sp.diag(1, *[sp.exp(2 * (a4f - H * sig))] * 3, -1, *[-sp.exp(2 * (sp.log(b4f) - a4f - H * sig))] * 3)
    divG = divergence_diag(gG, X, [pf] * 4 + [-rhof] + [pf] * 3)
    cons = sp.simplify(divG[4])
    target6 = -sp.diff(rhof, x4) - 3 * sp.diff(b4f, x4) / b4f * (rhof + pf)
    # with p = 5 rho: rho b4^18 is constant
    rr = sp.Function('r')(x4)
    ode = sp.Eq(sp.diff(rr, x4), -18 * sp.diff(b4f, x4) / b4f * rr)
    solved = sp.dsolve(ode, rr)
    froz = bulk_lhs(L, 1, {U: A, Ud: Ad})
    froz_m = bulk_lhs(L, -1, {U: A, Ud: Ad})
    flux_p = sp.factor(froz[0, 4] / H ** 2)
    flux_m = sp.factor(froz_m[0, 4] / H ** 2)
    jump = sp.factor(flux_p - flux_m)
    # the energy budget (frozen extra times, constant rate): the energy released in the bulk by the growth of ordinary
    # space, integrated over sigma with the volume weight, is the jump of the flux; its linear part feeds the fold fluid
    frc = bulk_lhs(L, 1, {U: A, Ud: 0, Ad: 0})
    k_rho = -frc[4, 4]                                   # kappa rho_bulk
    k_p1 = frc[1, 1]                                     # kappa p along x1
    k_sum = sp.factor(k_rho + k_p1)
    released = -3 * A * H * (k_rho + k_p1)               # kappa x energy per unit volume and time
    integrated = sp.simplify(2 * sp.integrate(sp.exp(-6 * H * sig) * released, (sig, 0, sp.oo)))
    kappa_lambdaF = sp.Rational(61, 8) * H
    kappa_rhod = sp.Rational(31, 4) * H - kappa_lambdaF     # -kappa S^4_4 - kappa lambda_F at the static block
    need_fold = 3 * A * H * kappa_rhod
    jump_lin = sp.expand(jump * H ** 2).coeff(A, 1) * A
    fold_json = json.loads((UM3 / 'outputs' / 'fold.json').read_text())['fold_source_kappaS']
    loc = {'A': A, 'U': U, 'Ad': Ad, 'Ud': Ud, 'H': H}
    kS = {k: sp.sympify(v, locals=loc).subs({U: A, Ud: Ad}) for k, v in fold_json.items()}
    kS_const = {k: sp.factor(v.subs(Ad, 0)) for k, v in kS.items()}
    rho_S_dot = -sp.diff(kS['x4,x4'], A) * Ad * H                 # d/dx4 of -kappa S^4_4(A) with A' = Ad H
    fold_balance = sp.simplify(rho_S_dot + 3 * A * H * (kS['x1,x1'] - kS['x4,x4']) - jump * H ** 2) == 0
    budget_ok = (sp.simplify(k_sum + sp.Rational(3, 8) * (1 + A ** 2) * H ** 2) == 0 and fold_balance
                 and sp.simplify(integrated - jump * H ** 2) == 0 and kappa_rhod == H / 8
                 and sp.simplify(need_fold - jump_lin) == 0)
    out['ST6'] = {'conservation_x4_component': str(cons), 'p_equal_5rho_solution': str(solved),
                  'frozen_flux_kappaT_sigma_x4_over_H2_sigma_positive': str(flux_p),
                  'frozen_flux_sigma_negative': str(flux_m), 'jump_at_the_fold_over_H2': str(jump),
                  'kappa_rho_plus_p1_frozen': str(k_sum), 'released_energy_integrated_over_sigma': str(integrated),
                  'kappa_lambda_F': str(kappa_lambdaF), 'kappa_rho_d': str(kappa_rhod),
                  'energy_needed_by_rho_d': str(need_fold), 'part_of_jump_linear_in_A': str(jump_lin),
                  'fold_source_frozen_constant_A': {k: str(v) for k, v in kS_const.items()},
                  'fold_takes_up_the_jump_any_a4': fold_balance}
    rep.check('ST6_history', sp.simplify(cons - target6) == 0
              and sp.simplify(flux_p - sp.Rational(3, 16) * A * (1 + A ** 2)) == 0 and sp.simplify(flux_p + flux_m) == 0
              and budget_ok,
              'nabla_M T^M_4 = %s for a homogeneous medium (p in every warped direction): rho\' = -3 (b4\'/b4)(rho + p), and '
              'with p = 5 rho %s: a stabiliser absent in the author\'s vacuum stays absent; with frozen extra times the '
              'required bulk source carries the flux kappa T^sigma_4 = %s H^2 (sigma > 0), %s H^2 (sigma < 0), which jumps by '
              '%s H^2 at the fold: the energy current -T^sigma_4 points towards the fold on both sides, so away from the static '
              'bulk the bulk source feeds the fold; energy budget: kappa (rho_bulk + p_1) = %s, the energy released by the '
              'growth of ordinary space, -3 a4\' (rho_bulk + p_1), integrated over sigma with the weight e^{-6 H |sigma|}, is '
              '%s = the jump; its linear part %s is the energy 3 a4\' rho_d that the pressureless part kappa rho_d = %s of the '
              'fold fluid (the static source minus the tension kappa lambda_F = %s) needs; the whole source of the fold '
              '(kappa S = %s at constant A) takes up exactly the jump, rho_S\' + 3 a4\' (rho_S + p_S) = [T^sigma_4], for frozen '
              'extra times and any a4(x4): %s' % (
                  cons, solved, flux_p, flux_m, jump, k_sum, integrated, jump_lin, kappa_rhod, kappa_lambdaF,
                  {k: str(v) for k, v in kS_const.items()}, fold_balance))

    # ---------------- ST7: the importance
    H0 = H0_KM_S_MPC / MPC_KM                     # 1/s
    dlnalpha = 3 * H0 * OKLO_GYR * GYR_S
    Vs, kap = sp.symbols('V_s kappa', positive=True)
    rho4 = sp.simplify(krho * H ** 2 / kap * Vs * sp.integrate(sp.exp(-6 * H * sig), (sig, 0, sp.oo)) * 2)
    out['ST7'] = {'vacuum_points': real, 'H0_per_s': H0, 'delta_ln_alpha_Oklo_if_author_vacuum_late': dlnalpha,
                  'Oklo_bound': OKLO_BOUND, 'rho_4_of_the_stabiliser': str(rho4)}
    rep.check('ST7_importance', dlnalpha > 1e5 * OKLO_BOUND and sp.simplify(rho4 + H * Vs / (48 * kap)) == 0,
              'without the stabiliser a slowly expanding bulk is impossible (ST3); taking instead the author\'s vacuum as the '
              'late universe (H = H_0) would make the couplings of the fold drift as g^2 ~ e^{3 H_0 x4}: Delta ln alpha = '
              '3 H_0 Delta t = %.2f over the %.1f Gyr since Oklo, against |Delta alpha/alpha| < %.0e; integrated over the '
              'hidden direction and the extra times the stabiliser carries rho_4 = rho_s V_*/(3H) = %s per unit volume of '
              'ordinary space of the fold' % (dlnalpha, OKLO_GYR, OKLO_BOUND, rho4))

    # ---------------- ST8: the energy constraint
    full = bulk_lhs(L, 1, {})
    P = sp.expand(16 * full[4, 4] / H ** 2)          # kappa T^4_4 = (H^2/16) P, kappa rho_bulk = -(H^2/16) P
    Ptarget = (5 * A ** 6 - 15 * A ** 5 * U + 15 * A ** 4 * U ** 2 - 9 * A ** 4 - 5 * A ** 3 * U ** 3 + 18 * A ** 3 * U + 3 * A ** 2
               - 9 * A * U ** 3 - 3 * A * U - 3 * U ** 2 + 1)
    no_second = P.free_symbols <= {A, U}
    Pfun = sp.lambdify((A, U), P, 'math')
    nth = 200000
    def circle_min(r):
        return min(Pfun(r * math.cos(2 * math.pi * k / nth), r * math.sin(2 * math.pi * k / nth)) for k in range(nth))
    lo, hi = 0.3, 0.8
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if circle_min(mid) > 0:
            lo = mid
        else:
            hi = mid
    kbest = min(range(nth), key=lambda k: Pfun(hi * math.cos(2 * math.pi * k / nth), hi * math.sin(2 * math.pi * k / nth)))
    a_min, u_min = hi * math.cos(2 * math.pi * kbest / nth), hi * math.sin(2 * math.pi * kbest / nth)
    # the smallest b for which the square |A| <= b, |U| <= b meets P = 0: the first b on a grid at which the boundary
    # of the square reaches P <= 0, refined by bisection between that grid point and the one before
    nsq = 20000
    def square_min(b):
        pts = [(-b + 2 * b * k / nsq) for k in range(nsq + 1)]
        return min(min(Pfun(t, b), Pfun(t, -b), Pfun(b, t), Pfun(-b, t)) for t in pts)
    b_grid = [0.005 * k for k in range(1, 121)]
    b_hi = next(b for b in b_grid if square_min(b) <= 0)
    b_lo = b_hi - 0.005
    for _ in range(30):
        mid = 0.5 * (b_lo + b_hi)
        if square_min(mid) > 0:
            b_lo = mid
        else:
            b_hi = mid
    tbest = min((Pfun(t, s * b_hi) if side == 0 else Pfun(s * b_hi, t), t, side, s)
                for t in [(-b_hi + 2 * b_hi * k / nsq) for k in range(nsq + 1)] for side in (0, 1) for s in (1, -1))
    sq_point = [tbest[1], tbest[3] * b_hi] if tbest[2] == 0 else [tbest[3] * b_hi, tbest[1]]
    # a direct check from inside: on a grid of the plane, P > 0 wherever A^2 + U^2 < 0.999 r_min^2 or
    # max(|A|, |U|) < 0.999 b_min
    inside_ok = True
    ngr = 400
    for i in range(ngr + 1):
        for j in range(ngr + 1):
            a_, u_ = -0.6 + 1.2 * i / ngr, -0.6 + 1.2 * j / ngr
            if (a_ * a_ + u_ * u_ < 0.999 * hi * hi or max(abs(a_), abs(u_)) < 0.999 * b_hi) and Pfun(a_, u_) <= 0:
                inside_ok = False
    Pfrozen = sp.expand(P.subs(U, A))
    froz_any = bulk_lhs(L, 1, {U: A, Ud: Ad})
    friedmann = sp.simplify(-froz_any[4, 4] - (3 * A ** 2 - 1) * H ** 2 / 16) == 0      # kappa rho_bulk, any a4(x4)
    comps8 = [sp.factor(-16 * frc[i, i] / H ** 2) for i in range(8)]
    flux_gen = sp.factor(full[0, 4] / H ** 2)
    Gf = 5 * A ** 2 * (A - U) ** 2 - 6 * A ** 2 + 6 * A * U + U ** 2 + 1
    flux_ok = flux_gen.free_symbols <= {A, U} and sp.simplify(flux_gen - sp.Rational(3, 16) * U * Gf) == 0
    flux_frozen = sp.factor(flux_gen.subs(U, A))
    # a bulk without any source cannot have frozen extra times: the flow (3/16) A (1 + A^2) H^2 vanishes only at A = 0,
    # where P = 1
    no_frozen_vacuum = (sp.simplify(flux_frozen - sp.Rational(3, 16) * A * (1 + A ** 2)) == 0
                        and sp.solve(sp.Eq(flux_frozen, 0), A) == [0] and P.subs({A: 0, U: 0}) == 1)
    out['ST8'] = {'P_of_A_U': str(P), 'free_of_A1_U1': no_second, 'r_min': hi, 'r_min_squared': hi * hi,
                  'closest_sourceless_point_A_U': [a_min, u_min],
                  'smallest_max_abs_A_abs_U_on_P_zero': b_hi, 'square_contact_point_A_U': sq_point,
                  'grid_check_from_inside': inside_ok, 'P_frozen': str(Pfrozen),
                  'frozen_kappa_rho_bulk_any_a4': '(3A^2 - 1) H^2/16' if friedmann else 'FAILED',
                  'frozen_components_times_minus16_over_H2': [str(c) for c in comps8],
                  'flux_any_a4_b4_over_H2_sigma_positive': str(flux_gen), 'flux_free_of_A1_U1': flux_ok,
                  'flux_frozen_over_H2_sigma_positive': str(flux_frozen),
                  'sourceless_bulk_cannot_have_frozen_extra_times': no_frozen_vacuum}
    rep.check('ST8_energy_constraint', no_second and sp.expand(P - Ptarget) == 0 and abs(hi - 0.51063) < 1e-4
              and abs(b_hi - 0.47705) < 1e-4 and inside_ok
              and sp.expand(Pfrozen - (1 - 3 * A ** 2)) == 0 and friedmann and flux_ok and no_frozen_vacuum,
              'the (x4, x4) component of the bulk equations is free of A1 and U1 (a constraint): kappa T^4_4 = (H^2/16) P(A, U), '
              'P = %s; without a source P = 0 at every instant, and min(A^2 + U^2) on P = 0 is %.4f (sqrt %.4f, at (A, U) = '
              '(%.4f, %.4f) and its mirror), and min(max(|A|, |U|)) on P = 0 is %.4f (at (A, U) = (%.4f, %.4f) and its '
              'mirror; a grid of the plane confirms P > 0 inside both bounds): at no instant can both rates of a sourceless '
              'bulk be below %.3f H; with frozen extra times P = %s for any a4(x4): 3 a4\'^2 = H^2 + 16 kappa rho_bulk = '
              '16 kappa (rho_bulk - rho_s), the stabiliser is the bulk energy density at which ordinary space stands still '
              '(a bulk source of zero energy density would need a4\' = H/sqrt 3); at constant A the components '
              '-16 kappa T/H^2 along (sigma, x1, x2, x3, x4, x5, x6, x7) are %s; the (sigma, x4) component is free of A1 and '
              'U1 as well: kappa T^sigma_4 = %s H^2 = (3/16) U G(A, U) H^2 for sigma > 0; with frozen extra times it is %s H^2, '
              'zero only at A = 0, where P = 1: a bulk without any source cannot have frozen extra times' % (
                  P, hi * hi, hi, a_min, u_min, b_hi, sq_point[0], sq_point[1], b_hi, Pfrozen, [str(c) for c in comps8],
                  flux_gen, flux_frozen))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['lovelock_time_s'] = round(t_lhs, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'stabiliser.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_stabiliser.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'stabiliser_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
