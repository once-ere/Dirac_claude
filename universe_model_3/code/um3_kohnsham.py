#!/usr/bin/env python3
"""um3_kohnsham.py - the self-consistent Kohn-Sham solution for dirac16complex bound to the fold (the equations FE-36 to
FE-43 of UM-3, written out below).

The orbitals of a homogeneous gas of the particles chi (the bound states of dirac16complex, at rest along ordinary space,
independent of the extra times) on the static block, Psi = e^{3H|sigma|} chi(sigma) e^{-i omega x4}, obey FE-41 reduced to
the hidden direction (units m_Psi = 1):
    chi' = gamma^(0) [ i omega gamma^(4) + 1 + M(sigma) ] chi            (sigma != 0),
    M(sigma) = lambda_Psi (n_s - N) = G e^{6H|sigma|} ( rho_hat(sigma) 1 - N_hat(sigma) ),
    rho_hat = (1/4) sum_k chibar_k chi_k,   N_hat = (1/4) sum_k chi_k chibar_k,   chibar = chi^dagger sigma16,
    chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-)                 (the fold, FE-39),
with the four positive-energy orbitals of the bound level (Krein charge -1 each, energy E = -omega Q = omega) occupied, and
the dimensionless self-coupling G = lambda_Psi n_chi / V* (n_chi the number density of chi on the fold).  gamma^(a) are
the author's matrices T^(a) of 4+4.nb; the spin connection is removed exactly by e^{3H|sigma|} (FE-36); gravity enters
through the warp factor e^{6H|sigma|} of the proper density.  The Higgs portal closes a second loop: mu_L is proportional
to v_loc^2 = v^2 - c_Phi <Psibar P_L Psi>(0)/lambda (FE-49): mu_L = mu_L0 (1 - kappa_H rho_hat_L(0)/rho_hat_L0(0)), with
kappa_H = c_Phi n_chi rho_hat_L0(0)/(lambda v^2 V*).  Its sign is fixed: the Higgs portal alone binds the fold (mu_L0 =
c_Phi v^2/(2 V*) < 0, so c_Phi < 0) and the occupied orbitals have rho_hat_L0(0) > 0, so kappa_H < 0: the gas raises v_loc^2
and deepens the binding.

Symmetry reduction.  The author's T_0..T_3 are symmetric and T_4..T_7 antisymmetric, so the rotations of ordinary space
(Sigma^{ij}) and of the extra times (Sigma^{rs}) form a compact group SU(2) x SU(2) of orthogonal matrices; gamma^(0),
gamma^(4), P_L, P_R, sigma16 and the Krein operator commute with it, and 16 = (2,2) x 4.  The four occupied orbitals form
one (2,2) multiplet, the mean field is invariant, and the problem reduces exactly to the 4-dimensional weight space W
(Sigma^{12} = Sigma^{56} = i/2): xi = Q_W^dagger chi, with N_hat restricted to W = (1/4) xi xi^dagger sigma16_W.  The
reduced solution is lifted back to the full multiplet (rotations by pi) and checked in sixteen dimensions.

Method: shooting (classical RK4 on |sigma| <= L, the step written as a matrix for all grid points at once, the solutions
re-orthonormalised every eight steps; for the level search only the values at the fold are needed and the eight step
matrices between two re-orthonormalisations are multiplied first), the bound level as the zero of the Krein-signed
matching residual within 0.05 of the previous level (a frequency beyond the local threshold at the far end, or a field so
large that the integration overflows, counts as no level; omega > 0), densities from the orbital, Anderson mixing of the
mean field (beta = 0.5 with depth 6, or beta = 0.2 with depth 10 where that fails: above the free threshold the saturated
tail is long and the linearised map has large negative eigenvalues; the extrapolated field is held to the bound of the
computed one), convergence when the relative change of the field is below 1e-8 and the level moves by less than 1e-10, or
the best iterate below 1e-7 once the residual has stopped falling (the floor set by the precision of the level),
continuation in G with intermediate couplings inserted where a step fails.  The computation is split into six parts (K1,
the regimes I, II and III, the Higgs loop K6 and the weakly bound point K9); every invocation of a part stops after at most
400 s (the standing rule: no individual calculation longer than 423 s) and keeps a checkpoint after every completed step
(the mean field as an exact binary copy, the level, the coupling, the mixing that worked last), from which the next
invocation continues with the same arithmetic; the assembly reads the six parts and makes the checks.
Checks:
  K1  without the self-interaction the shooting with the full 16 x 16 matrices reproduces FE-40 with eight degenerate states,
      four orbitals of each Krein sign; the reduced 4-dimensional problem has the same level with two degenerate states (one of each sign);
  K2  regime I (q_b > 3H): the self-consistent shift at small G equals first-order perturbation theory,
      delta omega = G int e^{6H|sigma|} (rho_hat^2 - tr N_hat^2) d sigma (= 2 E_int, E_int the interaction energy per
      particle); the occupied and the empty multiplets split;
  K3  every converged solution, lifted to sixteen dimensions, satisfies the Kohn-Sham equation, the fold matching and
      self-consistency (residuals), for G up to 1 in the three regimes q_b > 3H, 3H/2 < q_b < 3H, q_b < 3H/2;
  K4  the dilute limit: delta omega ~ G for q_b > 3H/2 and delta omega ~ G^{q_b/(3H - q_b)} for q_b < 3H/2;
  K5  in regimes II and III the proper scalar density saturates far from the fold where the local decay rate of the
      density reaches 6H (repulsive self-interaction); for G < 0 (G = -1e-4, -1e-2, from the free state) the iteration finds
      a bound state in regime I and no level in regimes II and III, where the proper density of the free state grows (the
      attraction would close the local gap there);
  K6  the Higgs-portal loop converges jointly with the orbitals, with the sign of kappa_H that the attractive Higgs portal
      implies (rho_hat_L0(0) > 0 for the occupied orbitals, so kappa_H < 0; the test value is kappa_H = -0.3): the gas raises
      v_loc^2, mu_L becomes more negative, and the level falls below its value without the feedback;
  K7  the equation of state of the chi gas: energy per particle e = omega - E_int, pressure P = n E_int, also the
      pressure along the extra times q = P (on-shell Lagrangian); P/e -> 0 in the dilute limit (cold dark matter);
  K8  regimes I and II: the repulsive mean field raises the level through the free continuum threshold omega = m_Psi = 1
      at a finite G without unbinding it: far from the fold the proper density saturates (density decay rate 6H; in regime I
      once the decay rate of the orbital falls below 3H), the far mean field keeps the local mass above omega, and the state
      stays bound up to G = 1 (in the computed cases a repulsive self-interaction does not dissolve the particles chi into
      the bulk);
  K9  a weakly bound point compatible with the direct-detection bound on the Higgs portal (q_b = 0.03 m_Psi, so
      q_b/omega_b = 0.03) and with a nearly luminal chi (H = 0.002 m_Psi, c_b^2 = q_b/(q_b - H) = 1.07): the shooting
      reproduces FE-40, and the self-consistent shift approaches first-order perturbation theory as G -> 0.
Writes outputs/kohnsham_parts/*.json (the parts, not kept in the repository), outputs/kohnsham.json and
reports/kohnsham_checks.json.
Usage (repository root; repeat a part until it reports that it is complete, exit code 0; 3 means run it again):
    python universe_model_3/code/um3_kohnsham.py part K1     (and part I, part II, part III, part K6, part K9)
    python universe_model_3/code/um3_kohnsham.py assemble
    python universe_model_3/code/um3_kohnsham.py             (the status of the parts)

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
import signal
import sys
import time
from pathlib import Path

import numpy as np
import scipy.linalg as sla
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402


def numeric_mats():
    T = GM.T16A()
    eta = GM.eta4488()
    Tn = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
    Tup = {a: float(eta[a, a]) * Tn[a] for a in range(8)}
    PL, PR = GM.projectors()
    return (Tn, Tup, np.array(PL.tolist(), dtype=float), np.array(PR.tolist(), dtype=float),
            np.array(GM.sigma16().tolist(), dtype=float))


TN, TUP, PLN, PRN, SIG = numeric_mats()
G0, G4 = TUP[0], TUP[4]
I16 = np.eye(16)
BKR = 1j * SIG @ G4          # the Krein operator (FE-43)


def sig(a, b):
    return 0.25 * (TUP[a] @ TUP[b] - TUP[b] @ TUP[a])


GENS = [sig(i, j) for i, j in ((1, 2), (1, 3), (2, 3), (5, 6), (5, 7), (6, 7))]
_X = GENS[0] + 2 * GENS[3]
_ev, _V = np.linalg.eig(_X)
QW, _ = np.linalg.qr(_V[:, np.abs(_ev - 1.5j) < 1e-8])      # the weight space W: Sigma^{12} = Sigma^{56} = i/2
ROT1 = sla.expm(np.pi * GENS[1])     # rotation by pi in the (1,3) plane: Sigma^{12} -> -Sigma^{12}
ROT2 = sla.expm(np.pi * GENS[4])     # rotation by pi in the (5,7) plane: Sigma^{56} -> -Sigma^{56}


def restrict(A):
    return QW.conj().T @ A @ QW


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def trap(f, h):
    return h * (0.5 * f[0] + f[1:-1].sum(axis=0) + 0.5 * f[-1])


class Shooter:
    """Shooting for chi' = g0 (i w g4 + 1 + M(sigma)) chi in dimension d (16, or 4 for W) with the fold matching."""
    WMAX = 0.05      # the widest bracket (in units of m_Psi) searched around the expected level

    def __init__(self, H, muL, muR, L, h, d, qr_every=8):
        self.H, self.muL0, self.muL, self.muR = H, muL, muL, muR
        self.d = d
        if d == 16:
            self.g0, self.g4, self.pl, self.pr, self.sg, self.kr = G0, G4, PLN, PRN, SIG, BKR
        else:
            self.g0, self.g4, self.pl, self.pr, self.sg, self.kr = (restrict(X) for X in (G0, G4, PLN, PRN, SIG, BKR))
        self.n = int(round(L / h))
        self.h = L / self.n
        self.s = np.linspace(0.0, L, self.n + 1)
        self.qr_every = qr_every
        z = np.zeros((self.n + 1, d, d), complex)
        self.M = {-1: z.copy(), 1: z.copy()}
        self._prep()

    def _prep(self):
        self.Tf = sla.expm(self.g0 @ (self.muL * self.pl + self.muR * self.pr))
        self.GM = {sd: np.einsum('ab,jbc->jac', self.g0, self.M[sd]) for sd in (-1, 1)}
        self.GMm = {sd: 0.5 * (self.GM[sd][1:] + self.GM[sd][:-1]) for sd in (-1, 1)}
        self.C04 = self.g0 @ self.g4

    def set_field(self, Ml, Mr, muL=None):
        self.M = {-1: Ml, 1: Mr}
        if muL is not None:
            self.muL = muL
        self._prep()

    def _start(self, w, side):
        """The decaying solutions at the far end |sigma| = L (orthonormal columns) and the base matrix of the equation."""
        base = 1j * w * self.C04 + self.g0
        try:
            ev, V = np.linalg.eig(base + self.GM[side][self.n])
        except np.linalg.LinAlgError as exc:
            raise RuntimeError('no eigenvectors at the far end (%s)' % exc)
        sel = ev.real > 0 if side < 0 else ev.real < 0
        if sel.sum() != self.d // 2:
            raise RuntimeError('no decaying subspace of half dimension at the far end (local continuum)')
        Y, _ = np.linalg.qr(V[:, sel])
        return Y, base

    def _steps(self, base, side):
        """The classical fourth-order Runge-Kutta step of the linear equation Y' = K(sigma) Y as a matrix: Y_{j-1} = P[j-1] Y_j
        for the step from the grid point j to j - 1 (all n steps at once).  With k1 = K1 Y, k2 = K2 (Y + dd/2 k1),
        k3 = K2 (Y + dd/2 k2), k4 = K3 (Y + dd k3) (K1, K2, K3 at s_j, s_{j-1/2}, s_{j-1}) the step is
        P = 1 + dd/6 (K1 + 2 A2 + 2 A3 + A4), A2 = K2 (1 + dd/2 K1), A3 = K2 (1 + dd/2 A2), A4 = K3 (1 + dd A3)."""
        dd = self.h if side < 0 else -self.h
        GMs = self.GM[side]
        K1 = base + GMs[1:]
        K2 = base + self.GMm[side]
        K3 = base + GMs[:-1]
        one = np.eye(self.d)
        A2 = K2 @ (one + 0.5 * dd * K1)
        A3 = K2 @ (one + 0.5 * dd * A2)
        A4 = K3 @ (one + dd * A3)
        return one + dd / 6.0 * (K1 + 2.0 * A2 + 2.0 * A3 + A4)

    def integrate(self, w, side):
        """Inward integration from |sigma| = L to the fold, re-orthonormalised at every qr_every-th grid point; the solutions
        at every grid point (Ys) and the triangular factors of the re-orthonormalisations (Rk).  A field so large that the
        integration overflows has no bound level (RuntimeError)."""
        n, d = self.n, self.d
        Y, base = self._start(w, side)
        Ys = np.empty((n + 1, d, d // 2), complex)
        Rk = {}
        try:
            with np.errstate(over='raise', invalid='raise'):
                P = self._steps(base, side)
                Ys[n] = Y
                for j in range(n, 0, -1):
                    Y = P[j - 1] @ Y
                    if (j - 1) % self.qr_every == 0:
                        Y, R = np.linalg.qr(Y)
                        Rk[j - 1] = R
                    Ys[j - 1] = Y
        except (FloatingPointError, np.linalg.LinAlgError) as exc:
            raise RuntimeError('the integration overflows (%s)' % exc)
        if not np.isfinite(Ys).all():
            raise RuntimeError('the integration overflows')
        return Ys, Rk

    def integrate_end(self, w, side):
        """The same integration, returning only the solutions at the fold: the steps between two re-orthonormalisations are
        multiplied together first (in a tree of pairwise products), the same arithmetic in a different order."""
        n, q = self.n, self.qr_every
        Y, base = self._start(w, side)
        try:
            with np.errstate(over='raise', invalid='raise'):
                P = self._steps(base, side)
                r = n % q
                for j in range(n, n - r, -1):
                    Y = P[j - 1] @ Y
                if r:
                    Y, _ = np.linalg.qr(Y)
                nb = (n - r) // q
                B = P[:n - r].reshape(nb, q, self.d, self.d)
                while B.shape[1] > 1:
                    if B.shape[1] % 2:
                        B = np.concatenate([B[:, :-2], (B[:, -2] @ B[:, -1])[:, None]], axis=1)
                        continue
                    B = B[:, 0::2] @ B[:, 1::2]
                B = B[:, 0]
                for m in range(nb - 1, -1, -1):
                    Y, _ = np.linalg.qr(B[m] @ Y)
        except (FloatingPointError, np.linalg.LinAlgError) as exc:
            raise RuntimeError('the integration overflows (%s)' % exc)
        if not np.isfinite(Y).all():
            raise RuntimeError('the integration overflows')
        return Y

    def match(self, w, full=True):
        if not full:
            return np.hstack([self.integrate_end(w, 1), -self.Tf @ self.integrate_end(w, -1)]), None
        Yl, Rl = self.integrate(w, -1)
        Yr, Rr = self.integrate(w, 1)
        return np.hstack([Yr[0], -self.Tf @ Yl[0]]), (Yl, Rl, Yr, Rr)

    def sv(self, w):
        return np.linalg.svd(self.match(w, full=False)[0], compute_uv=False)[::-1]

    def reconstruct(self, Ys, Rk, c0):
        out = np.empty((self.n + 1, self.d), complex)
        c = c0.copy()
        for j in range(self.n + 1):
            out[j] = Ys[j] @ c
            if j in Rk:
                c = np.linalg.solve(Rk[j], c)
        return out

    def null_orbitals(self, w, k):
        A, (Yl, Rl, Yr, Rr) = self.match(w)
        U, s, Vh = np.linalg.svd(A)
        order = np.argsort(s)
        null = Vh.conj().T[:, order[:k]]
        half = self.d // 2
        return ([(self.reconstruct(Yl, Rl, null[half:, kk]), self.reconstruct(Yr, Rr, null[:half, kk])) for kk in range(k)],
                np.sort(s))

    def gram(self, orbs, op):
        n = len(orbs)
        Gm = np.zeros((n, n), complex)
        for a in range(n):
            for b in range(n):
                fl = np.einsum('ji,ik,jk->j', orbs[a][0].conj(), op, orbs[b][0])
                fr = np.einsum('ji,ik,jk->j', orbs[a][1].conj(), op, orbs[b][1])
                Gm[a, b] = trap(fl, self.h) + trap(fr, self.h)
        return 0.5 * (Gm + Gm.conj().T)

    def krein_split(self, w, k):
        """The k orbitals of the null space at w combined into Krein-orthonormal ones: (negative, positive, eigenvalues, s)."""
        orbs, s = self.null_orbitals(w, k)
        Gk = self.gram(orbs, self.kr)
        ev, R = np.linalg.eigh(Gk)
        neg, pos = [], []
        for kk in range(len(ev)):
            c = R[:, kk] / math.sqrt(abs(ev[kk]))
            o = (sum(c[a] * orbs[a][0] for a in range(len(orbs))), sum(c[a] * orbs[a][1] for a in range(len(orbs))))
            (neg if ev[kk] < 0 else pos).append(o)
        return neg, pos, ev, s

    def fneg(self, w):
        """The squared residual of the best matching vector with negative Krein norm: zero exactly at the occupied
        (Krein-negative) level.  The Krein norm of a bound state is estimated from its values at the fold,
        v^dagger B v + w^dagger B w (exact for the free profiles, (that)/(2q)), within the two-dimensional near-null space."""
        Yr0, Yl0 = self.integrate_end(w, 1), self.integrate_end(w, -1)
        A = np.hstack([Yr0, -self.Tf @ Yl0])
        U, s, Vh = np.linalg.svd(A)
        V = Vh.conj().T
        order = np.argsort(s)
        V2 = V[:, order[:2]]
        h2 = self.d // 2
        P = np.zeros((self.d, self.d), complex)
        P[:h2, :h2] = Yr0.conj().T @ self.kr @ Yr0
        P[h2:, h2:] = Yl0.conj().T @ self.kr @ Yl0
        S2 = np.diag(np.sort(s)[:2] ** 2).astype(complex)        # exact in the basis of the singular vectors
        P2 = V2.conj().T @ P @ V2
        P2 = 0.5 * (P2 + P2.conj().T)
        mu, X = np.linalg.eig(np.linalg.solve(P2, S2))
        best = np.inf
        for kk in range(2):
            x = X[:, kk]
            pn = float((x.conj() @ P2 @ x).real)
            if pn < 0:
                best = min(best, float((x.conj() @ S2 @ x).real) / abs(pn))
        return best

    def level(self, w_guess, width, thresh=1e-7):
        """The occupied (Krein-negative) level near w_guess: the zero of sqrt(fneg) (bracket widened until the smallest
        singular value vanishes there), confirmed by the Krein charge of the orbital."""
        def g(dx):
            # an omega beyond the local threshold at the far end (no decaying solutions there), or a field so large that
            # the integration overflows, is not a bound level; nor is omega <= 0 (the occupied orbitals have Krein charge -1
            # and positive energy E = -omega Q = omega)
            if w_guess + dx <= 0.0:
                return 1e3
            try:
                f = self.fneg(w_guess + dx)
            except (RuntimeError, np.linalg.LinAlgError):
                return 1e3
            return math.sqrt(max(f, 0.0)) if math.isfinite(f) else 1e3
        width = min(width, self.WMAX)
        for _ in range(8):
            # minimise in the offset dx from w_guess: scipy's bounded method has the tolerance sqrt(eps)|x| + xatol/3,
            # which in the offset is far below the 1e-8 it would be in omega itself
            w = w_guess + float(minimize_scalar(g, bounds=(-width, width), method='bounded',
                                                options={'xatol': 1e-16, 'maxiter': 2000}).x)
            try:
                s = self.sv(w)
                found = math.isfinite(self.fneg(w)) and s[0] < thresh
            except (RuntimeError, np.linalg.LinAlgError):
                found = False
            if found:
                break
            if width >= self.WMAX:
                raise RuntimeError('no Krein-negative level within %.2f of %.12f' % (self.WMAX, w_guess))
            width = min(10 * width, self.WMAX)
        else:
            raise RuntimeError('no Krein-negative level near %.12f' % w_guess)
        k = max(1, int(np.sum(s < thresh)))
        try:
            neg, pos, ev, s2 = self.krein_split(w, k)
        except np.linalg.LinAlgError as exc:
            raise RuntimeError('no Krein-negative level near %.12f (%s)' % (w_guess, exc))
        if len(neg) != 1:
            raise RuntimeError('no Krein-negative level near %.12f (Krein eigenvalues %s)' % (w_guess, ev))
        return w, neg[0], ev, s2


def densities_W(sh, xi):
    """rho_hat, N_hat restricted to W and the left-handed scalar density, from the W-orbital xi = (left, right)."""
    out = {}
    for side, idx in ((-1, 0), (1, 1)):
        x = xi[idx]
        rho = np.einsum('ji,ik,jk->j', x.conj(), sh.sg, x).real
        Nh = 0.25 * np.einsum('ji,jk,kl->jil', x, x.conj(), sh.sg)
        rhoL = np.einsum('ji,ik,jk->j', x.conj(), sh.sg @ sh.pl, x).real
        out[side] = (rho, Nh, rhoL)
    return out


def field_W(sh, dens, G, cap):
    F = {}
    capped = False
    for side in (-1, 1):
        rho, Nh, _ = dens[side]
        wgt = G * np.exp(6 * sh.H * sh.s)
        M = wgt[:, None, None] * (rho[:, None, None] * np.eye(sh.d)[None] - Nh)
        nrm = np.linalg.norm(M, axis=(1, 2))
        scale = np.minimum(1.0, cap / np.maximum(nrm, 1e-300))
        F[side] = M * scale[:, None, None]
        capped = capped or bool((scale < 1).any())
    return F, capped


def lift(xi):
    """The four orbitals of the (2,2) multiplet in sixteen dimensions: Q_W xi and its rotations by pi."""
    out = []
    for R in (I16, ROT1, ROT2, ROT1 @ ROT2):
        out.append((xi[0] @ QW.T @ R.T, xi[1] @ QW.T @ R.T))
    return out


def full_residuals(sh, w, occ16, G):
    """Residuals of the sixteen-dimensional problem for the lifted orbitals: the mean field rebuilt in sixteen
    dimensions, the Kohn-Sham equation (central differences), the fold matching, the Krein charges and orthogonality."""
    Tf16 = sla.expm(G0 @ (sh.muL * PLN + sh.muR * PRN))
    res_ode, res_match = 0.0, 0.0
    M16 = {}
    for side, idx in ((-1, 0), (1, 1)):
        chis = np.array([o[idx] for o in occ16])
        rho = np.einsum('kji,il,kjl->j', chis.conj(), SIG, chis).real / 4
        Nh = np.einsum('kji,kjl,lm->jim', chis, chis.conj(), SIG) / 4
        M16[side] = G * np.exp(6 * sh.H * sh.s)[:, None, None] * (rho[:, None, None] * I16[None] - Nh)
    for o in occ16:
        for side, idx in ((-1, 0), (1, 1)):
            chi = o[idx]
            dsig = -sh.h if side < 0 else sh.h
            dchi = (chi[2:] - chi[:-2]) / (2 * dsig)
            K = np.einsum('ab,jbc->jac', G0, 1j * w * G4[None] + I16[None] + M16[side][1:-1])
            rhs = np.einsum('jab,jb->ja', K, chi[1:-1])
            res_ode = max(res_ode, float(np.abs(dchi - rhs).max() / np.abs(rhs).max()))
        res_match = max(res_match, float(np.linalg.norm(o[1][0] - Tf16 @ o[0][0]) / np.linalg.norm(o[1][0])))
    charges = [float(sum(trap(np.einsum('ji,ik,jk->j', o[i].conj(), BKR, o[i]).real, sh.h) for i in (0, 1))) for o in occ16]
    off = 0.0
    for a in range(4):
        for b in range(a + 1, 4):
            v = sum(trap(np.einsum('ji,ik,jk->j', occ16[a][i].conj(), BKR, occ16[b][i]), sh.h) for i in (0, 1))
            off = max(off, abs(v))
    return res_ode, res_match, charges, float(off)


ANDERSON_DEPTH = 6


def solve(sh, G, w_start, kappaH=0.0, rhoL0=None, beta=0.5, depth=None, tol=1e-8, maxit=150, cap=20.0, width=0.02, trace=None):
    """Iterate the reduced Kohn-Sham problem to self-consistency at coupling G with Anderson mixing of the mean field
    (and of mu_L for the Higgs loop).  Plain linear mixing would need a very small weight: far from the fold a small change of
    the mean field changes the decay rate of the orbital, and with it the far density, by a large factor of the opposite
    sign, so the linearised Kohn-Sham map has large negative eigenvalues (the argument of SOLUTION.md; they are not
    computed).  sh keeps its field (continuation in G)."""
    def pack(Ml, Mr, mu):
        return np.concatenate([Ml.ravel(), Mr.ravel(), [mu]])

    def unpack(x):
        n = (x.size - 1) // 2
        return x[:n].reshape(sh.M[-1].shape), x[n:2 * n].reshape(sh.M[1].shape), float(x[-1].real)
    depth = ANDERSON_DEPTH if depth is None else depth
    x = pack(sh.M[-1], sh.M[1], sh.muL)
    Xh, Rh = [], []
    w = w_start
    retries = 0
    hist = []
    best = (np.inf, -1, None)       # the smallest residual so far, its iteration and its input field
    for it in range(maxit):
        Ml, Mr, mu = unpack(x)
        sh.set_field(Ml, Mr, mu)
        try:
            w_new, xi, kev, s = sh.level(w, width)
        except (RuntimeError, np.linalg.LinAlgError) as exc:
            # the extrapolated field has no Krein-negative level near w: go back to the last iterate that had one and take
            # a short plain step from it, with the Anderson history cleared
            if Xh and retries < 4:
                retries += 1
                x = Xh[-1] + 0.25 * beta * Rh[-1]
                Xh, Rh = Xh[-1:], Rh[-1:]
                width = max(width, 1e-3)
                continue
            return {'converged': False, 'reason': str(exc), 'G': G, 'iterations': it}
        dens = densities_W(sh, xi)
        F, capped = field_W(sh, dens, G, cap)
        mu_t = sh.muL
        if kappaH != 0.0:
            rhoL_fold = 0.5 * (dens[-1][2][0] + dens[1][2][0])
            mu_t = sh.muL0 * (1.0 - kappaH * rhoL_fold / rhoL0)
        f = pack(F[-1], F[1], mu_t)
        r = f - x
        rn = float(np.abs(r).max() / max(1e-300, np.abs(f[:-1]).max()))
        hist.append((float(w_new), rn))
        if trace is not None:
            trace.append((it, float(w_new), rn))
        if rn < best[0]:
            best = (rn, it, x.copy())
        Xh.append(x.copy())
        Rh.append(r.copy())
        if len(Xh) > depth + 1:
            Xh.pop(0)
            Rh.pop(0)
        if len(Xh) >= 2:
            dX = np.array([Xh[i + 1] - Xh[i] for i in range(len(Xh) - 1)]).T
            dR = np.array([Rh[i + 1] - Rh[i] for i in range(len(Rh) - 1)]).T
            gam = np.linalg.lstsq(dR, r, rcond=None)[0]
            x = x + beta * r - (dX + beta * dR) @ gam
        else:
            x = x + beta * r
        # the extrapolated mean field is held to the same bound as the output of the Kohn-Sham map (norm <= cap at every
        # point; a converged solution lies well inside it, K3)
        Ml, Mr, mu = unpack(x)
        x = pack(*(M * np.minimum(1.0, cap / np.maximum(np.linalg.norm(M, axis=(1, 2)), 1e-300))[:, None, None]
                   for M in (Ml, Mr)), mu)
        dw = w_new - w
        w = w_new
        width = max(10 * abs(dw), 1e-9)
        if it > 2 and rn < tol and abs(dw) < 1e-10:
            break
        # above the free threshold (regime I, omega > m_Psi) the residual reaches a floor of a few 1e-8, set by the
        # precision of the level: once it is below 1e-7 and has not fallen for 15 iterations, the best iterate is taken
        if best[0] < 1e-7 and it - best[1] >= 15:
            x = best[2]
            break
    else:
        if not best[0] < 1e-7:
            return {'converged': False, 'reason': 'no convergence in %d iterations (smallest residual %.1e)' % (maxit, best[0]),
                    'G': G, 'omega': w, 'history': hist[-5:]}
        x = best[2]
    Ml, Mr, mu = unpack(x)
    sh.set_field(Ml, Mr, mu)
    try:
        w, xi, kev, s = sh.level(w, max(width, 1e-9))
    except (RuntimeError, np.linalg.LinAlgError) as exc:
        return {'converged': False, 'reason': str(exc), 'G': G}
    dens = densities_W(sh, xi)
    F, capped = field_W(sh, dens, G, cap)
    selfcons = max(np.abs(F[-1] - sh.M[-1]).max(), np.abs(F[1] - sh.M[1]).max()) / max(1e-300, np.abs(F[1]).max())
    occ16 = lift(xi)
    res_ode, res_match, charges, off = full_residuals(sh, w, occ16, G)
    eint = 0.0
    for side in (-1, 1):
        rho, Nh, _ = dens[side]
        trN2 = 4.0 * np.einsum('jab,jba->j', Nh, Nh).real          # tr over sixteen dimensions = 4 x tr over W
        eint += 0.5 * G * trap(np.exp(6 * sh.H * sh.s) * (rho ** 2 - trN2), sh.h)
    rho_r = dens[1][0]
    jfar = int(0.85 * sh.n)
    k5 = max(5, int(1.0 / sh.h))
    rate = float(-(np.log(abs(rho_r[jfar + k5])) - np.log(abs(rho_r[jfar - k5]))) / (2 * k5 * sh.h))
    return {'converged': True, 'G': G, 'omega': float(w), 'iterations': it + 1, 'krein_eig': [float(x) for x in kev],
            'singular_values': [float(x) for x in s], 'E_int_per_particle': float(eint),
            'energy_per_particle': float(w - eint), 'pressure_over_energy': float(eint / (w - eint)),
            'residual_KS_ode_16': res_ode, 'residual_fold_matching_16': res_match, 'residual_selfconsistency': float(selfcons),
            'krein_charges_16': charges, 'krein_offdiagonal_16': off, 'capped': capped, 'muL': float(sh.muL),
            'density_decay_rate_far': rate,
            'proper_density_far': float(G * math.exp(6 * sh.H * sh.s[jfar]) * rho_r[jfar]),
            'mean_field_norm_max': float(max(np.linalg.norm(sh.M[sd], axis=(1, 2)).max() for sd in (-1, 1))),
            'rhoL_fold': float(0.5 * (dens[-1][2][0] + dens[1][2][0]))}


def first_order_shift(sh16, w):
    """delta omega / G from first-order perturbation theory with the four Krein-negative orbitals of the level of eight degenerate states."""
    neg, pos, ev, s = sh16.krein_split(w, 8)
    tot = 0.0
    for side, idx in ((-1, 0), (1, 1)):
        chis = np.array([o[idx] for o in neg])
        rho = np.einsum('kji,il,kjl->j', chis.conj(), SIG, chis).real / 4
        Nh = np.einsum('kji,kjl,lm->jim', chis, chis.conj(), SIG) / 4
        trN2 = np.einsum('jab,jba->j', Nh, Nh).real
        tot += trap(np.exp(6 * sh16.H * sh16.s) * (rho ** 2 - trN2), sh16.h)
    return tot, len(neg)


TARGETS = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]
REGIMES = {'I': (0.05, 60.0, 0.03), 'II': (0.15, 60.0, 0.02), 'III': (0.3, 20.0, 0.02)}
# (H, the box L, the step h).  Far from the fold the saturated orbital decays as e^{-3H|sigma|}: at the end of the box it is
# e^{-9} (I), e^{-27} (II) and e^{-18} (III) of its value at the fold.  A longer box in regime III only lengthens the
# saturated tail, which makes the iteration stiff (the linearised map grows with the length of the tail).
MU_L, MU_R = -0.6, 0.0


def regime_sequence(name):
    """The couplings of the continuation: in regimes II and III from a G so small that the proper density does not reach
    saturation inside the grid, up by factors of 3 to 1e-6, then by factors of sqrt(10) to 0.1 and in steps of 0.1 (0.15
    first) to 1; in regime I the targets to 0.1 and steps of 0.05 to 1 (through the crossing of omega = 1).  Every target
    G = 1e-6, 1e-5, ..., 1 is in the sequence."""
    Hv, L, h = REGIMES[name]
    qb = -MU_L / 2
    grow = 6 * Hv - 2 * qb
    if grow > 0:
        seq, g = [], 0.05 / (0.3 * math.exp(grow * L))
        while g < 1e-6:
            seq.append(g)
            g *= 3.0
        mid = [x for t in TARGETS[:5] for x in (t, t * math.sqrt(10.0))] + [TARGETS[5]]   # 1e-6, 3.2e-6, ..., 0.1
        return seq + mid + [0.15] + [round(0.1 * k, 1) for k in range(2, 11)]
    return TARGETS[:6] + [round(0.15 + 0.05 * k, 2) for k in range(18)]          # 0.15, 0.2, ..., 1.0


MIXINGS = ((0.5, 6), (0.2, 10))   # (beta, depth) of the Anderson mixing: the default, and the gentler, deeper one that
                                  # converges above the free threshold of regime I, where the saturated tail is long


def step_to(sh, G, Gprev, w, attempts=12):
    """Continue the converged state held by sh at Gprev (level w) to G; where a step fails, the state is restored and an
    intermediate coupling (the geometric midpoint) is solved first.  Returns the result at G and the inserted results."""
    saved = (sh.M[-1].copy(), sh.M[1].copy(), sh.muL)
    lo, wlo, hi = Gprev, w, G
    inserted = []
    r = None
    for _ in range(attempts):
        order = getattr(sh, 'mix_order', list(MIXINGS))
        for mix in order:
            try:
                r = solve(sh, hi, wlo, beta=mix[0], depth=mix[1])
            except (RuntimeError, np.linalg.LinAlgError, FloatingPointError) as exc:
                r = {'converged': False, 'reason': repr(exc), 'G': hi}
            if r.get('converged'):
                r['mixing'] = list(mix)
                sh.mix_order = [mix] + [m for m in order if m != mix]      # the mixing that worked is tried first next
                break
            sh.set_field(*saved)
        if r.get('converged'):
            if hi == G:
                return r, inserted
            inserted.append(r)
            lo, wlo, hi = hi, r['omega'], G
            saved = (sh.M[-1].copy(), sh.M[1].copy(), sh.muL)
            continue
        sh.set_field(*saved)
        hi = math.sqrt(lo * hi) if lo > 0 else hi / 3
    return r, inserted


PARTS_DIR = UM3 / 'outputs' / 'kohnsham_parts'
PART_NAMES = ('K1', 'I', 'II', 'III', 'K6', 'K9')
HARD_LIMIT = 400      # seconds: no individual calculation may run longer than 423 s (the standing rule); a part that
                      # reaches this limit stops, keeps its last checkpoint and is continued by the next invocation
SOFT_BUDGET = 240     # no new step of a part is started after this many seconds
SNAPSHOT_G = (0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0)   # couplings whose self-consistent mean field is kept for um3_krein.py


class TimeUp(Exception):
    """The hard time limit of one invocation was reached."""


def _alarm(signum, frame):
    raise TimeUp()


def _save_json(path, data):
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(data, indent=1, sort_keys=True, default=str) + '\n')
    tmp.replace(path)


def _state_paths(tag):
    return PARTS_DIR / ('%s.state.json' % tag), PARTS_DIR / ('%s.state.npz' % tag)


def _save_state(tag, sh, st):
    """Checkpoint of a continuation: the mean field held by the shooter (exact binary copy) and the bookkeeping."""
    js, nz = _state_paths(tag)
    tmp = nz.with_name(nz.name + '.tmp')
    with open(tmp, 'wb') as f:
        np.savez(f, Ml=sh.M[-1], Mr=sh.M[1])
    tmp.replace(nz)
    st['muL'] = float(sh.muL)
    st['mix_order'] = [list(m) for m in sh.mix_order] if hasattr(sh, 'mix_order') else None
    _save_json(js, st)


def _load_state(tag, sh):
    js, nz = _state_paths(tag)
    if not js.exists():
        return None
    st = json.loads(js.read_text())
    with np.load(nz) as z:
        sh.set_field(z['Ml'].copy(), z['Mr'].copy(), st['muL'])
    if st.get('mix_order') is not None:
        sh.mix_order = [tuple(m) for m in st['mix_order']]
    return st


def _drop_state(tag):
    for q in _state_paths(tag):
        if q.exists():
            q.unlink()


def regime_part(name, t0):
    """The continuation in G of one regime, then the two attractive couplings from the free state; checkpointed after
    every step.  Returns True when the regime is complete (its part file written)."""
    final = PARTS_DIR / ('regime_%s.json' % name)
    if final.exists():
        return True
    Hv, L, h = REGIMES[name]
    qb = -MU_L / 2
    wb = math.sqrt(1 - qb * qb)
    keys = ('converged', 'omega', 'iterations', 'residual_KS_ode_16', 'residual_selfconsistency', 'density_decay_rate_far',
            'capped', 'reason')
    tag = 'regime_' + name
    sh = Shooter(Hv, MU_L, MU_R, L, h, 4)
    st = _load_state(tag, sh)
    if st is None:
        if 6 * Hv - 4 * qb < 0:
            pt, _ = first_order_shift(Shooter(Hv, MU_L, MU_R, L, h, 16), wb)
        else:
            pt = float('inf')
        st = {'pt': pt, 'w': wb, 'Gprev': 0.0, 'next': 0, 'stopped': False, 'rows': [], 'path': [], 'log': [],
              'neg_rows': [], 'seconds': time.time() - t0}
        _save_state(tag, sh, st)
    seq = regime_sequence(name)
    pt = st['pt']
    while st['next'] < len(seq) and not st['stopped']:
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = seq[st['next']]
        r, inserted = step_to(sh, G, st['Gprev'], st['w'])
        for x in inserted + [r]:
            x['first_order_prediction'] = (wb + pt * x['G']) if math.isfinite(pt) else None
            st['path'].append({k: x.get(k) for k in ('G', 'converged', 'omega', 'iterations', 'reason')})
            print('progress: regime %s G = %.3g converged %s omega = %s, %s iterations (%.0f s)' % (
                name, x['G'], x.get('converged'), x.get('omega'), x.get('iterations'), time.time() - t0), flush=True)
            x['target'] = x['G'] in TARGETS
            if x is r and x.get('converged') and x['G'] in SNAPSHOT_G:
                # the self-consistent mean field of this coupling, kept for the analysis of the Krein norm (um3_krein.py)
                with open(PARTS_DIR / ('snapshot_%s_G%g.npz' % (name, x['G'])), 'wb') as f:
                    np.savez(f, Ml=sh.M[-1], Mr=sh.M[1], muL=sh.muL, omega=x['omega'], G=x['G'], H=Hv, L=L, h=h)
            st['rows'].append(x)
            if x['target'] or not x.get('converged') or name == 'I':
                st['log'].append('  regime %s G=%.3g: %s' % (name, x['G'], {k: x.get(k) for k in keys}))
        if r.get('converged'):
            st['w'], st['Gprev'] = r['omega'], G
        else:
            st['stopped'] = True
        st['next'] += 1
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    while len(st['neg_rows']) < 2:
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = (-1e-4, -1e-2)[len(st['neg_rows'])]
        sh2 = Shooter(Hv, MU_L, MU_R, L, h, 4)
        try:
            r = solve(sh2, G, wb)
        except TimeUp:
            raise
        except Exception as exc:
            r = {'converged': False, 'reason': str(exc), 'G': G}
        st['neg_rows'].append(r)
        st['log'].append('  regime %s G=%g: %s' % (name, G, {k: r.get(k) for k in ('converged', 'omega', 'reason', 'capped')}))
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    _save_json(final, {'H': Hv, 'L': L, 'h': h, 'first_order_dw_over_G': pt, 'positive_G': st['rows'],
                       'negative_G': st['neg_rows'], 'continuation_path': st['path'], 'log': st['log'],
                       'seconds': st['seconds'], 'definition_of_the_fold': fold_definition()})
    _drop_state(tag)
    return True


def k9_part(t0):
    """K9: the Kohn-Sham states at mu_L = -0.06 (q_b = 0.03), H = 0.002 (regime I, q_b = 15H), L = 500, h = 0.25;
    checkpointed after every coupling."""
    final = PARTS_DIR / 'K9.json'
    if final.exists():
        return True
    muL, muR, Hv, L, h = -0.06, 0.0, 0.002, 500.0, 0.25
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)
    tag = 'K9'
    sh = Shooter(Hv, muL, muR, L, h, 4)
    st = _load_state(tag, sh)
    if st is None:
        ts = time.time()
        sh16 = Shooter(Hv, muL, muR, L, h, 16)
        f8 = lambda dx: float(np.sum(sh16.sv(wb + dx)[:8]))
        w16 = wb + float(minimize_scalar(f8, bounds=(-1e-4, 1e-4), method='bounded',
                                         options={'xatol': 1e-16, 'maxiter': 2000}).x)
        pt, nneg = first_order_shift(sh16, wb)
        st = {'w16': w16, 'pt': pt, 'nneg': nneg, 'rows': [], 'w': wb, 'seconds': time.time() - ts}
        _save_state(tag, sh, st)
    couplings = (1e-4, 1e-3, 1e-2)
    while len(st['rows']) < len(couplings):
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = couplings[len(st['rows'])]
        r = solve(sh, G, st['w'])
        r['ratio_to_first_order'] = (r['omega'] - wb) / (st['pt'] * G) if r.get('converged') else None
        st['rows'].append(r)
        if r.get('converged'):
            st['w'] = r['omega']
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    _save_json(final, {'muL': muL, 'H': Hv, 'q_b': qb, 'omega_b_FE40': wb, 'omega_16': st['w16'],
                       'first_order_dw_over_G': st['pt'], 'krein_negative_orbitals': st['nneg'],
                       'c_b_squared': qb / (qb - Hv), 'q_b_over_omega_b': qb / wb, 'rows': st['rows'],
                       'seconds': st['seconds'], 'definition_of_the_fold': fold_definition()})
    _drop_state(tag)
    return True


KAPPA_H = -0.3      # the test value of the Higgs loop; negative, the sign that the attractive Higgs portal implies (K6)


def higgs_loop(kappaH=KAPPA_H, G=0.1):
    """K6: the Kohn-Sham states with the Higgs-portal loop closed (regime I, kappa_H = -0.3, G = 0.1), from the free state."""
    wb = math.sqrt(1 - (MU_L / 2) ** 2)
    sh = Shooter(0.05, MU_L, MU_R, 60.0, 0.03, 4)
    negW0, _, _, _ = sh.krein_split(wb, 2)
    d0 = densities_W(sh, negW0[0])
    rhoL0 = 0.5 * (d0[-1][2][0] + d0[1][2][0])
    return solve(sh, G, wb, kappaH=kappaH, rhoL0=rhoL0), float(rhoL0)


def k6_part(t0):
    final = PARTS_DIR / 'K6.json'
    if final.exists():
        return True
    rH, rhoL0 = higgs_loop()
    _save_json(final, {'solution': rH, 'rhoL0': rhoL0, 'seconds': time.time() - t0,
                       'definition_of_the_fold': fold_definition()})
    return True


def k1_part(t0):
    """K1: the free level, with the full 16 x 16 matrices and reduced to W."""
    final = PARTS_DIR / 'K1.json'
    if final.exists():
        return True
    muL, muR = MU_L, MU_R
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)
    sh16 = Shooter(0.05, muL, muR, 60.0, 0.03, 16)
    f8 = lambda dx: float(np.sum(sh16.sv(wb + dx)[:8]))
    w16 = wb + float(minimize_scalar(f8, bounds=(-1e-3, 1e-3), method='bounded', options={'xatol': 1e-16, 'maxiter': 2000}).x)
    neg, pos, ev16, s16 = sh16.krein_split(w16, 8)
    shW = Shooter(0.05, muL, muR, 60.0, 0.03, 4)
    f2 = lambda dx: float(np.sum(shW.sv(wb + dx)[:2]))
    wW = wb + float(minimize_scalar(f2, bounds=(-1e-3, 1e-3), method='bounded', options={'xatol': 1e-16, 'maxiter': 2000}).x)
    negW, posW, evW, sW = shW.krein_split(wW, 2)
    _save_json(final, {'omega_FE40': wb, 'omega_16': w16, 'omega_W': wW, 'sv16': [float(x) for x in s16[:9]],
                       'svW': [float(x) for x in sW], 'krein16': [len(neg), len(pos)], 'kreinW': [len(negW), len(posW)],
                       'seconds': time.time() - t0, 'definition_of_the_fold': fold_definition()})
    return True


def run_part(name):
    """Run (or continue) one part within the time limit: True when the part is complete."""
    PARTS_DIR.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(HARD_LIMIT)
    try:
        if name == 'K1':
            return k1_part(t0)
        if name in REGIMES:
            return regime_part(name, t0)
        if name == 'K6':
            return k6_part(t0)
        if name == 'K9':
            return k9_part(t0)
        raise SystemExit('unknown part %s (parts: %s)' % (name, ', '.join(PART_NAMES)))
    except TimeUp:
        print('part %s reached the time limit of %d s; its last checkpoint is kept, run it again' % (name, HARD_LIMIT),
              flush=True)
        return False
    finally:
        signal.alarm(0)


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def assemble():
    t0 = time.time()
    missing = [n for n in PART_NAMES if not (PARTS_DIR / (('regime_%s.json' % n) if n in REGIMES else (n + '.json'))).exists()]
    if missing:
        print('parts not yet complete: %s (run: python universe_model_3/code/um3_kohnsham.py part NAME)' % ', '.join(missing))
        return 2
    part = {n: json.loads((PARTS_DIR / (('regime_%s.json' % n) if n in REGIMES else (n + '.json'))).read_text())
            for n in PART_NAMES}
    rep = Report()
    out = {'units': 'm_Psi = 1', 'muL': -0.6, 'muR': 0.0}
    muL, muR = -0.6, 0.0
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)

    sym = {'T0..T3 symmetric': all(np.allclose(TN[a], TN[a].T) for a in range(4)),
           'T4..T7 antisymmetric': all(np.allclose(TN[a], -TN[a].T) for a in range(4, 8)),
           'commutant contains g0, g4, P_L, sigma16, Krein': all(np.allclose(X @ g, g @ X) for X in (G0, G4, PLN, SIG, BKR) for g in GENS),
           'dim W': int(QW.shape[1])}
    out['symmetry'] = sym

    # ---------------- K1: the free level, full and reduced
    k1 = part['K1']
    w16, wW, s16, sW = k1['omega_16'], k1['omega_W'], k1['sv16'], k1['svW']
    nneg, npos = k1['krein16']
    nnegW, nposW = k1['kreinW']
    out['K1'] = {k: v for k, v in k1.items() if k not in ('seconds', 'definition_of_the_fold')}
    rep.check('K1_free_level', abs(w16 - wb) < 1e-10 and abs(wW - wb) < 1e-10 and s16[7] < 1e-6 < s16[8] and sW[1] < 1e-6 < sW[2]
              and nneg == 4 and npos == 4 and nnegW == 1 and nposW == 1
              and all(v for k, v in sym.items() if k != 'dim W') and sym['dim W'] == 4,
              'omega = %.10f (16 dimensions), %.10f (reduced to W), FE-40: %.10f; eight degenerate states (two in W) with Krein signature '
              '(%d, %d) [(%d, %d) in W]; T_0..T_3 symmetric, T_4..T_7 antisymmetric, the compact rotations SU(2) x SU(2) commute '
              'with gamma^(0), gamma^(4), P_L, sigma16 and the Krein operator, 16 = (2,2) x 4' % (
                  w16, wW, wb, nneg, npos, nnegW, nposW))

    # ---------------- the three regimes (continuation in G), the Higgs loop (K6) and the weakly bound point (K9), each
    # computed as a separate part (checkpointed, every invocation under the time limit)
    out['regimes'] = {k: {'H': v[0], 'q_b': qb, '3H': 3 * v[0], '3H/2': 1.5 * v[0]} for k, v in REGIMES.items()}
    results = {name: {k: v for k, v in part[name].items() if k not in ('seconds', 'definition_of_the_fold')}
               for name in REGIMES}
    k9 = {k: v for k, v in part['K9'].items() if k not in ('seconds', 'definition_of_the_fold')}
    rH, rhoL0 = part['K6']['solution'], part['K6']['rhoL0']
    compute_seconds = sum(part[n]['seconds'] for n in PART_NAMES)
    for name in REGIMES:
        for line in results[name].pop('log'):
            print(line, flush=True)
    out['results'] = results

    # ---------------- K2
    rI = results['I']
    small = [r for r in rI['positive_G'] if r.get('converged') and r['G'] in TARGETS[:4]]
    ratios = [(r['omega'] - wb) / (rI['first_order_dw_over_G'] * r['G']) for r in small]
    splitW = [r['singular_values'][1] for r in rI['positive_G'] if r.get('converged') and r['G'] >= 1e-2]
    rep.check('K2_first_order_limit', len(small) == 4 and all(abs(x - 1) < 2e-3 for x in ratios) and all(x > 1e-6 for x in splitW),
              'regime I: (omega - omega_b)/(first-order shift) = %s for G <= 1e-3 (first-order coefficient %.6f); at the occupied '
              'level the other Krein state of W is split off (second singular value %s for G >= 1e-2)' % (
                  ['%.5f' % x for x in ratios], rI['first_order_dw_over_G'], ['%.2e' % x for x in splitW]))

    # ---------------- K3
    allr = [r for nm in results for r in results[nm]['positive_G']]
    conv = [r for r in allr if r.get('converged')]
    worst = max(max(r['residual_KS_ode_16'], r['residual_fold_matching_16']) for r in conv) if conv else 1.0
    worst_sc = max(r['residual_selfconsistency'] for r in conv) if conv else 1.0
    charges_ok = all(all(abs(q + 1) < 1e-6 for q in r['krein_charges_16']) and r['krein_offdiagonal_16'] < 1e-6 for r in conv)
    tg = all(any(r.get('converged') and r['G'] == g for r in results[nm]['positive_G']) for nm in ('I', 'II', 'III')
             for g in TARGETS)
    rep.check('K3_residuals_16', tg and worst < 1e-3 and worst_sc < 1e-6 and charges_ok and not any(r['capped'] for r in conv),
              '%d converged solutions (the three regimes for G = 1e-6 ... 1 and the continuation between); lifted to '
              'sixteen dimensions the four orbitals have Krein charge -1 each and are Krein-orthogonal; largest relative residual '
              'of the 16-dimensional Kohn-Sham equation (with the mean field rebuilt from the lifted orbitals) and fold matching '
              '%.1e (central differences on the grid), of self-consistency (the reduced problem) %.1e; no cap active' % (
                  len(conv), worst, worst_sc))

    # ---------------- K8: regimes I and II through omega = m_Psi without unbinding
    k8, ok8 = {}, True
    for name in ('I', 'II'):
        Hv = REGIMES[name][0]
        rows_ = sorted([r for r in results[name]['positive_G'] if r.get('converged')], key=lambda r: r['G'])
        cross = None
        for a, b in zip(rows_[:-1], rows_[1:]):
            if a['omega'] < 1.0 <= b['omega']:
                cross = a['G'] + (1.0 - a['omega']) * (b['G'] - a['G']) / (b['omega'] - a['omega'])
                break
        above = [r for r in rows_ if r['omega'] > 1.0]
        sat = [abs(r['density_decay_rate_far'] - 6 * Hv) / (6 * Hv) for r in above]
        reached = any(r['G'] == 1.0 for r in rows_)
        k8[name] = {'G_omega_equals_mPsi': cross, 'omega_at_G1': rows_[-1]['omega'] if reached else None,
                    'decay_rate_far_above_threshold': [r['density_decay_rate_far'] for r in above], '6H': 6 * Hv,
                    'largest_relative_deviation_from_6H': max(sat) if sat else None,
                    'omega_where_free_decay_rate_is_3H': math.sqrt(1 - (3 * Hv) ** 2) if 3 * Hv < 1 else None}
        ok8 = ok8 and cross is not None and reached and bool(above) and max(sat) < 0.02
    out['K8'] = k8
    rep.check('K8_through_the_free_threshold', ok8,
              'the repulsive mean field raises the level through the free continuum threshold omega = m_Psi = 1 at G = %.3f '
              '(regime I) and G = %.3f (regime II), and the state stays bound up to G = 1 (omega = %.6f and %.6f there): far '
              'from the fold the proper density saturates (the density decays at 6H to within %.1e and %.1e above the '
              'threshold), so the far mean field keeps the local mass above omega: in the computed cases a repulsive '
              'self-interaction does not dissolve the particles chi into the bulk (the saturation needs the warp, H > 0)' % (
                  k8['I']['G_omega_equals_mPsi'] or float('nan'), k8['II']['G_omega_equals_mPsi'] or float('nan'),
                  k8['I']['omega_at_G1'] or float('nan'), k8['II']['omega_at_G1'] or float('nan'),
                  k8['I']['largest_relative_deviation_from_6H'] or float('nan'),
                  k8['II']['largest_relative_deviation_from_6H'] or float('nan')))

    # ---------------- K4
    expo = {}
    for name in results:
        rr = [r for r in results[name]['positive_G'] if r.get('converged') and r['G'] in TARGETS[:3]]     # 1e-6, 1e-5, 1e-4
        x = np.log([r['G'] for r in rr])
        y = np.log([r['omega'] - wb for r in rr])
        slope = float(np.polyfit(x, y, 1)[0])
        Hv = results[name]['H']
        pred = 1.0 if qb > 1.5 * Hv else qb / (3 * Hv - qb)
        expo[name] = {'fitted': slope, 'predicted': pred}
    out['K4'] = expo
    rep.check('K4_dilute_exponents', all(abs(v['fitted'] - v['predicted']) < 0.05 for v in expo.values()),
              'delta omega ~ G^p for G <= 1e-4: %s (predicted 1 for q_b > 3H/2, q_b/(3H - q_b) for q_b < 3H/2)' % (
                  {k: 'fit %.3f, predicted %.3f' % (v['fitted'], v['predicted']) for k, v in expo.items()}))

    # ---------------- K5
    sat = {}
    for name in ('II', 'III'):
        Hv = results[name]['H']
        r = [x for x in results[name]['positive_G'] if x.get('converged') and x['G'] == 1e-2][0]
        sat[name] = {'density_decay_rate_far': r['density_decay_rate_far'], '6H': 6 * Hv,
                     'proper_density_far': r['proper_density_far']}
    negI = [r.get('converged', False) for r in results['I']['negative_G']]
    negII = [r.get('converged', False) for r in results['II']['negative_G']]
    negIII = [r.get('converged', False) for r in results['III']['negative_G']]
    out['K5'] = {'saturation': sat, 'negative_G_regime_I_converged': negI, 'negative_G_regime_II_converged': negII,
                 'negative_G_regime_III_converged': negIII}
    rep.check('K5_saturation_and_runaway', all(abs(v['density_decay_rate_far'] - v['6H']) / v['6H'] < 0.05 for v in sat.values())
              and all(negI) and not any(negII) and not any(negIII),
              'far from the fold the scalar density decays at %s (6H: the proper density e^{6H|sigma|} n_s saturates); '
              'attractive self-interaction G = -1e-4, -1e-2 from the free state: regime I converges %s; in regimes II and III, '
              'where the proper density of the free state grows away from the fold, the level search finds no Krein-negative '
              'level (%s; %s)' % ({k: '%.4f vs %.3f' % (v['density_decay_rate_far'], v['6H']) for k, v in sat.items()}, negI,
                                  [r.get('reason', '') for r in results['II']['negative_G']],
                                  [r.get('reason', '') for r in results['III']['negative_G']]))

    # ---------------- K6
    rI01 = [r for r in results['I']['positive_G'] if r['G'] == 0.1][0]
    # Hellmann-Feynman: rho_hat_L0(0) = d omega_b/d mu_L; on the grid (h = 0.03 in regime I) the trapezoidal Krein
    # normalisation of a profile ~ e^{-q_b |sigma|} overestimates the norm by (2 q_b h)^2/12, and the density by as much less
    hf = -muL / (4 * wb)
    hf_rel = abs(rhoL0 - hf) / hf
    hf_trap = (2 * qb * REGIMES['I'][2]) ** 2 / 12
    out['K6'] = {'kappa_H': KAPPA_H, 'solution': rH, 'without_feedback_omega': rI01.get('omega'), 'rhoL0_fold': float(rhoL0),
                 'sign_of_kappa_H': 'negative: c_Phi < 0 (mu_L0 < 0) and rho_hat_L0(0) > 0',
                 'linear_estimate_muL': muL / (1 + KAPPA_H),      # rho_hat_L(0) proportional to q_b, q_b to mu_L
                 'hellmann_feynman_domega_dmuL': -muL / (4 * wb),  # d omega_b / d mu_L = -m^2 mu_L/(4 omega_b) (FE-40)
                 'relative_difference': hf_rel, 'trapezoid_normalisation_error': hf_trap}
    rep.check('K6_higgs_portal_loop', bool(rH.get('converged')) and rH.get('residual_selfconsistency', 1) < 1e-6
              and rH.get('residual_KS_ode_16', 1) < 1e-3 and rhoL0 > 0 and hf_rel < 1e-4 and abs(hf_rel - hf_trap) < 0.05 * hf_trap
              and KAPPA_H < 0
              and rH.get('muL', muL) < muL - 1e-3 and rH.get('omega', 2.0) < rI01.get('omega', 0.0),
              'the occupied orbitals have rho_hat_L0(0) = %.8f > 0, equal to d omega_b/d mu_L = -mu_L/(4 omega_b) = %.8f '
              '(Hellmann-Feynman) up to the relative difference %.2e, the error %.2e of the trapezoidal normalisation on the '
              'grid; the Higgs portal alone binds the fold (c_Phi < 0), so '
              'kappa_H < 0; with kappa_H = %.2f and G = 0.1 the joint loop converges in %s iterations: the gas raises v_loc^2, '
              'mu_L = %.6f (from %.2f; %.4f if rho_hat_L(0) were proportional to q_b), and the level falls to omega = %.8f '
              '(%.8f without the feedback)' % (
                  rhoL0, hf, hf_rel, hf_trap, KAPPA_H, rH.get('iterations'), rH.get('muL', float('nan')), muL, muL / (1 + KAPPA_H),
                  rH.get('omega', float('nan')), rI01.get('omega', float('nan'))))

    # ---------------- K7
    eos = {name: [(r['G'], r['pressure_over_energy']) for r in results[name]['positive_G'] if r.get('converged')
                  and r['target']] for name in results}
    out['K7'] = eos
    dil = [v[0][1] for v in eos.values()]                                          # G = 1e-6
    rep.check('K7_equation_of_state', all(v[0][0] == 1e-6 for v in eos.values()) and all(abs(x) < 1e-3 for x in dil)
              and all(p > 0 for v in eos.values() for _, p in v),
              'P/e (= q/e) at G = 1e-6: %s; at G = 1: %s; positive (repulsive) and vanishing in the dilute limit: the chi gas is '
              'cold dark matter' % (['%.2e' % x for x in dil], ['%.3f' % v[-1][1] for v in eos.values()]))

    # ---------------- K9: a weakly bound point
    out['K9'] = k9
    rr = k9['rows']
    ok9 = (abs(k9['omega_16'] - k9['omega_b_FE40']) < 1e-10 and k9['krein_negative_orbitals'] == 4
           and all(r.get('converged') for r in rr) and abs(rr[0]['ratio_to_first_order'] - 1) < 2e-3
           and abs(1 - rr[0]['ratio_to_first_order']) < abs(1 - rr[1]['ratio_to_first_order']) < abs(1 - rr[2]['ratio_to_first_order'])
           and max(r['residual_KS_ode_16'] for r in rr) < 1e-3 and max(r['residual_selfconsistency'] for r in rr) < 1e-6
           and all(0 < r['pressure_over_energy'] < 1e-3 for r in rr))
    rep.check('K9_weak_binding', ok9,
              'q_b = 0.03 m_Psi (q_b/omega_b = %.3f, the direct-detection bound on the Higgs portal), H = 0.002 m_Psi (c_b^2 = %.3f): '
              'omega = %.10f from the 16-dimensional shooting (FE-40: %.10f), first-order coefficient %.6f; self-consistent shift / '
              'first order = %s for G = 1e-4, 1e-3, 1e-2 (approaching 1 as G -> 0), P/e = %s: a dilute, weakly bound gas of chi is '
              'pressureless; its self-interaction shifts the orbital energy by %.2e m_Psi per unit G and the energy per particle '
              'by %.2e m_Psi (half of it: the orbital energy counts the interaction twice)' % (
                  k9['q_b_over_omega_b'], k9['c_b_squared'], k9['omega_16'], k9['omega_b_FE40'], k9['first_order_dw_over_G'],
                  ['%.5f' % r['ratio_to_first_order'] for r in rr], ['%.1e' % r['pressure_over_energy'] for r in rr],
                  k9['first_order_dw_over_G'], (rr[0]['energy_per_particle'] - k9['omega_b_FE40']) / rr[0]['G']))

    out['runtime_s'] = round(compute_seconds + time.time() - t0, 1)     # the parts and the assembly
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'kohnsham.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_kohnsham.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'kohnsham_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed (the parts computed in %.1f s, the assembly in %.1f s)' % (
        report['passed'], report['total'], compute_seconds, time.time() - t0))
    return 0 if report['all_passed'] else 1


def main(argv):
    if len(argv) == 2 and argv[0] == 'part':
        return 0 if run_part(argv[1]) else 3
    if argv == ['assemble']:
        return assemble()
    print(__doc__.split('BEGIN FOLD DEFINITION')[0])
    for n in PART_NAMES:
        f = PARTS_DIR / (('regime_%s.json' % n) if n in REGIMES else (n + '.json'))
        tag = ('regime_' + n) if n in REGIMES else n
        print('part %-4s %s' % (n, 'complete' if f.exists() else ('checkpointed' if _state_paths(tag)[0].exists()
                                                                    else 'not started')))
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
