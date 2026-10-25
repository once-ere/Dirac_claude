#!/usr/bin/env python3
"""um3_krein.py - is the indefinite Krein norm of the dirac16complex charge stable?

The charge of dirac16complex is Q_Psi = int Psi^dagger B Psi with the Krein operator B = i sigma16 gamma^(4), a Hermitian
involution with eight eigenvalues +1 and eight -1 (the author's real matrices T_a of 4+4.nb, gamma^(a) = eta_aa T_a).  The
canonical anticommutator of the field is {Psi, Psi^dagger} = -B (the overall sign chosen so that the occupied bound states
of Krein charge -1, the particles chi, have positive norm); a mode u_n with int u_n^dagger B u_n = kappa_n (kappa_n = -1 or
+1) then has {a_n, a_n^dagger} = -kappa_n, the Hamiltonian is H = sum_n (-kappa_n omega_n) a_n^dagger a_n, and every quantum
raises H by its frequency, [H, a_n^dagger] = omega_n a_n^dagger.  In the positive-energy quantisation (a_n|0> = 0 for
omega_n > 0, a_n^dagger|0> = 0 for omega_n < 0) every particle and every hole carries positive energy and the norm -kappa_n
of its mode: the particles and the holes of the modes of Krein charge +1 are ghosts (norm -1), those of the modes of
Krein charge -1 are physical (norm +1).  The physical states are therefore the particles chi (charge -1 at +omega_b) and
the holes in the states of charge -1 at -omega_b (the conjugates of the states of charge +1 at +omega_b); the holes in the
conjugates of the chi states (charge +1 at -omega_b) are ghost antiparticles.  A fermion cannot trade its norm for its
energy ({a, a^dagger} = -1 has no positive-definite representation), so the ghosts cannot be removed by a choice of the
vacuum.

Checks (the bound states at rest on the static block, units m_Psi = 1, mu_L = -0.6, mu_R = 0, as in um3_kohnsham.py):
  KR1  the charge form: B Hermitian, B^2 = 1, signature (8, 8); the anticommutator {a_n, a_m^dagger} = -kappa_n delta_nm
       of the modes derived from {Psi, Psi^dagger} = -B; in the explicit Fock representation of one fermionic mode (a
       two-dimensional Krein space) the one-quantum state has the norm -kappa for either choice of vacuum and
       [H, a^dagger] = omega a^dagger; complex conjugation maps the bound level at +omega_b onto the one at -omega_b and
       reverses every Krein charge (the author's matrices are real);
  KR2  the symmetries of the problem at rest: the matrices that commute with gamma^(0), gamma^(4) and Gamma_8 and keep
       sigma16 (U^dagger sigma16 U = sigma16) form a Lie algebra of real dimension 32: 16 compact generators that keep the
       two Krein sectors and 16 Hermitian generators (boosts) that anticommute with B and mix them, among them the nine
       Lorentz boosts Sigma^{ir} between ordinary space and the extra times; with gamma^(1), gamma^(2), gamma^(3) added
       (moving particles) only u(1) + su(2) of the extra times remains, compact and sector-keeping;
  KR3  the mirror of the fold: under R_1 chi(sigma) -> T_0 T_1 T_2 T_3 chi(-sigma) the four bound states of Krein charge -1
       are even and the four of charge +1 odd; R_2 chi(sigma) -> T_0 T_5 T_6 T_7 chi(-sigma) maps each sector onto the other;
       the self-consistent occupied orbital and its mean field are R_1-even;
  KR4  flat directions: the boosts of KR2 map the self-consistent gas (regime I, G_KS = 0.1) onto self-consistent gases
       (the residuals of the sixteen-dimensional Kohn-Sham equation and of the fold matching unchanged, Krein charges -1,
       Krein-orthogonal) whose orbitals contain Krein-positive admixtures: exact flat directions; the linear response of
       the bound level (the time-dependent Kohn-Sham equations restricted to the occupied and the empty multiplet) has 32
       frequencies of the order 1e-4, far below the splitting of the two multiplets, among them one imaginary pair: exact
       zero modes would give 0, so its truncation error is as large as its frequencies and it does not decide the stability
       of the dilute gas;
  KR5  the Krein-positive partner of the occupied level in the self-consistent mean fields of the regimes I, II and III at
       G_KS = 0.01, 0.1, 0.2, 0.3, 0.5, 0.7 and 1: a real level above the occupied one in the dilute gas, moving away from
       it as G_KS grows (they cannot mix: opposite R_1 parity); at larger G_KS a complex pair omega +- i Gamma, in regime I
       where the partner reaches the continuum at the end of the computational box (the size of the box was not varied),
       in regimes II and III in the discrete spectrum: an indication that dense gases are unstable, not converged;
  KR6  selection rules at the fold: of the 256 products Gamma_I of the author's matrices, the chirality-blind fold
       operators (products of gamma^(1)..gamma^(4)) never connect a physical state with a ghost at rest, the chiral ones
       (the same products times Gamma_8) always do (scattering conversion or the creation of a physical particle with a
       ghost antiparticle); for moving particles the scalar, density and vector-current operators still do not, the
       magnetic dipole does in proportion to the momentum;
  KR7  the consequence: in the positive-energy quantisation the vacuum cannot decay (every quantum of the free field has
       positive energy), but the left-handed Higgs portal of the author's specification (c_R = 0) creates a physical
       particle with a ghost antiparticle at rest with an amplitude 0.89 times its elastic one: the ghosts are produced
       wherever the chiral portals act, and UM-3 with chiral fold couplings is not unitary; chirality-blind couplings are
       necessary, not shown to be sufficient; the classical stability of the gas is not decided (KR4, KR5).
The mean fields of KR3 to KR5 are the snapshots that um3_kohnsham.py keeps in outputs/kohnsham_parts (run its parts first).
Writes outputs/krein.json and reports/krein_checks.json.  Runs in about 4.5 minutes (under the 423 s limit).
Usage: python universe_model_3/code/um3_krein.py

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

import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import scipy.linalg as sla
from scipy.optimize import minimize, minimize_scalar

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_kohnsham as K  # noqa: E402

T = K.TUP
I16 = np.eye(16)
SIG = K.SIG
BKR = K.BKR
G8 = K.TN[8]
S1 = T[0] @ T[1] @ T[2] @ T[3]
S2 = T[0] @ T[5] @ T[6] @ T[7]
WB = math.sqrt(1 - 0.09)
PARTS = UM3 / 'outputs' / 'kohnsham_parts'


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


def commutant(ops):
    M = np.vstack([np.kron(O, I16) - np.kron(I16, O.T) for O in ops])
    u, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-9):].conj()
    return [null[k].reshape(16, 16) for k in range(null.shape[0])]


def real_null(rows_of, basis, tol=1e-9):
    """The real combinations of basis that satisfy the real-linear condition rows_of(X) = 0."""
    A = np.array([np.concatenate([rows_of(X).real.ravel(), rows_of(X).imag.ravel()]) for X in basis]).T
    u, s, vh = np.linalg.svd(A)
    null = vh[np.sum(s > tol):]
    return [sum(c * X for c, X in zip(v, basis)) for v in null]


def symmetry_algebra(extra=()):
    C = commutant([T[0], T[4], G8] + list(extra))
    basis = [ph * X for X in C for ph in (1.0, 1j)]
    return real_null(lambda X: X.conj().T @ SIG + SIG @ X, basis)


def fold_value(a, b, Op):
    """a^dagger sigma16 Op b at the fold: the mean of the two sides."""
    return 0.5 * (a[0][0].conj() @ SIG @ Op @ b[0][0] + a[1][0].conj() @ SIG @ Op @ b[1][0])


def krein_charge(o, h):
    return float(sum(K.trap(np.einsum('ji,ik,jk->j', o[i].conj(), BKR, o[i]), h) for i in (0, 1)).real)


def conj(o):
    return (o[0].conj(), o[1].conj())


def reflect(o, S):
    """(R chi)(sigma) = S chi(-sigma): the sigma < 0 profile of R chi is S times the sigma > 0 profile of chi."""
    return ((S @ o[1].T).T, (S @ o[0].T).T)


def flat(o):
    return np.concatenate([o[0].ravel(), o[1].ravel()])


def load_snapshot(name, G):
    f = PARTS / ('snapshot_%s_G%g.npz' % (name, G))
    if not f.exists():
        return None
    z = np.load(f)
    sh = K.Shooter(float(z['H']), -0.6, 0.0, float(z['L']), float(z['h']), 4)
    sh.set_field(z['Ml'].copy(), z['Mr'].copy(), float(z['muL']))
    return sh, float(z['omega'])


def empty_level(sh, w, G):
    """The Krein-positive level of the reduced problem above the occupied one: the minimum of the smallest singular value
    in (w + 0.01 G, w + 0.15 G), where the splitting lies (it is about 0.05 G in regime I)."""
    f = lambda x: sh.sv(x)[0]
    lo, hi = w + 0.01 * G, w + 0.15 * G
    ws = np.linspace(lo, hi, 29)
    vals = []
    for x in ws:
        try:
            vals.append(f(x))
        except RuntimeError:
            vals.append(np.inf)
    i = int(np.argmin(vals))
    a, b = ws[max(i - 1, 0)], ws[min(i + 1, len(ws) - 1)]
    r = minimize_scalar(f, bounds=(a, b), method='bounded', options={'xatol': 1e-15, 'maxiter': 500})
    return float(r.x), float(r.fun)


def rpa_bound_level(sh, w, G):
    """The linearised time-dependent Kohn-Sham equations of the four occupied orbitals chi_o, restricted to admixtures of
    the four empty Krein-positive orbitals phi_p of the bound level: i dc/dt = A c + B c*, frequencies of
    [[A, B], [-B*, -A*]] (A Hermitian, B symmetric; chibar = chi^dagger sigma16; w = e^{6H|sigma|})."""
    negW, posW, ev, s = sh.krein_split(w, 1)
    xi = negW[0]
    wp, smin = empty_level(sh, w, G)
    orbs, s2 = sh.null_orbitals(wp, 1)
    kp = sh.gram(orbs, sh.kr)[0, 0].real
    phi = (orbs[0][0] / math.sqrt(abs(kp)), orbs[0][1] / math.sqrt(abs(kp)))
    occ, emp = K.lift(xi), K.lift(phi)
    wgt = np.exp(6 * sh.H * sh.s)
    bil = lambda a, b, side: np.einsum('ji,ik,jk->j', a[side].conj(), SIG, b[side])
    n = 4
    A = np.zeros((n * n, n * n), complex)
    Bm = np.zeros((n * n, n * n), complex)
    D = wp - w
    for q, o, p, o2 in itertools.product(range(n), repeat=4):
        tA = tB = 0.0
        for side in (0, 1):
            tA = tA + K.trap(wgt * (bil(occ[o2], emp[p], side) * bil(emp[q], occ[o], side)
                                    - bil(emp[q], emp[p], side) * bil(occ[o2], occ[o], side)), sh.h)
            tB = tB + K.trap(wgt * (bil(emp[p], occ[o2], side) * bil(emp[q], occ[o], side)
                                    - bil(emp[q], occ[o2], side) * bil(emp[p], occ[o], side)), sh.h)
        A[q * n + o, p * n + o2] = (D if (q == p and o == o2) else 0.0) - G / 4 * tA
        Bm[q * n + o, p * n + o2] = -G / 4 * tB
    nu = np.linalg.eigvals(np.block([[A, Bm], [-Bm.conj(), -A.conj()]]))
    charges = [krein_charge(o, sh.h) for o in emp]
    n_imag = int(np.sum(np.abs(nu.imag) > 1e-3 * np.abs(nu).max()))
    real_part = [float(x) for x in sorted(np.abs(nu[np.abs(nu.imag) <= 1e-3 * np.abs(nu).max()].real))]
    return {'omega_occupied': w, 'omega_empty': wp, 'splitting': D, 'smin_empty': smin, 'empty_krein_charges': charges,
            'A_hermitian': float(np.abs(A - A.conj().T).max()), 'B_symmetric': float(np.abs(Bm - Bm.T).max()),
            'max_abs_frequency': float(np.abs(nu).max()), 'max_abs_imaginary': float(np.abs(nu.imag).max()),
            'n_imaginary': n_imag, 'largest_real_frequency': max(real_part) if real_part else 0.0,
            'max_A_minus_splitting': float(np.abs(A - D * np.eye(n * n)).max()), 'max_B': float(np.abs(Bm).max())}


def moving_states(k, H=0.05, L=40.0, h=0.02):
    """The free bound states moving along x_1 with the momentum k (the term -i k e^{H|sigma|} gamma^(1) of the Dirac
    operator at a_4 = 0): the level, its Krein-negative and Krein-positive states."""
    sh = K.Shooter(H, -0.6, 0.0, L, h, 16)
    Mk = (-1j * k * np.exp(H * sh.s))[:, None, None] * T[1][None]
    sh.set_field(Mk.copy(), Mk.copy())
    w0 = math.sqrt(WB ** 2 + 0.3 / (0.3 - H) * k * k)
    f8 = lambda dx: float(np.sum(sh.sv(w0 + dx)[:8]))
    w = w0 + float(minimize_scalar(f8, bounds=(-5e-3, 5e-3), method='bounded', options={'xatol': 1e-15, 'maxiter': 500}).x)
    nk = int(np.sum(sh.sv(w) < 1e-6))
    neg, pos, ev, s = sh.krein_split(w, nk)
    return w, neg, pos, nk


SNAPSHOT_G = (0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0)


def partner_level(sh, w):
    """The Krein-positive partner of the occupied level w of the reduced problem.  First the local continuum of the far
    bulk: the smallest frequency above w at which the equation at the end of the box has a non-decaying solution.  Below
    it, a real root of the matching (local minima of the smallest singular value on a grid that is fine near w, refined;
    a singular value below 1e-7 and a positive Krein charge) is a bound partner.  Without one, the complex root above w
    (Nelder-Mead from the best points of a grid in the complex plane; a singular value below 1e-10 and an imaginary part
    above 1e-6) is a normalisable mode that grows as e^{Gamma x4}, Gamma its imaginary part; with neither, the partner
    has dissolved into the continuum of the far bulk."""
    def f(x):
        try:
            return float(sh.sv(x)[0])
        except (RuntimeError, np.linalg.LinAlgError):
            return 1e3
    far = None
    for x in np.linspace(w, w + 0.8, 321):
        ev = np.linalg.eigvals(1j * x * sh.C04 + sh.g0 + sh.GM[1][sh.n])
        if np.abs(ev.real).min() < 1e-9:
            far = float(x)
            break
    top = far if far is not None else w + 0.8
    ws = w + np.geomspace(1e-5, max(top - w - 1e-6, 2e-5), 120)
    vals = [f(x) for x in ws]
    roots = []
    for i in range(len(ws)):
        left = vals[i - 1] if i > 0 else np.inf
        right = vals[i + 1] if i + 1 < len(ws) else np.inf
        if vals[i] <= left and vals[i] <= right and vals[i] < 1e2:
            a = ws[i - 1] if i > 0 else w + 1e-6
            b = ws[i + 1] if i + 1 < len(ws) else top - 1e-7
            r = minimize_scalar(f, bounds=(a, b), method='bounded', options={'xatol': 1e-15, 'maxiter': 600})
            if r.fun < 1e-7 and r.x < top:
                try:
                    orbs, s2 = sh.null_orbitals(float(r.x), 1)
                except (RuntimeError, np.linalg.LinAlgError):
                    continue
                kq = float(sh.gram(orbs, sh.kr)[0, 0].real)
                if kq > 0:
                    roots.append({'omega': float(r.x), 'sv': float(r.fun), 'krein': kq})
    if roots:
        r0 = min(roots, key=lambda r: r['omega'])
        return {'kind': 'real', 'omega_occupied': w, 'omega_partner': r0['omega'], 'sv': r0['sv'], 'krein': r0['krein'],
                'far_continuum_from': far, 'growth_rate': 0.0}

    def g(z):
        try:
            return float(sh.sv(z[0] + 1j * z[1])[0])
        except (RuntimeError, np.linalg.LinAlgError):
            return 1e3
    pts = [(re, im) for re in np.linspace(w + 1e-3, w + 0.6, 61) for im in (2e-4, 1e-3, 4e-3, 1.6e-2, 5e-2)]
    if far is not None:
        # just above the continuum of the far bulk, where an embedded partner turns into a slowly growing mode
        pts += [(re, im) for re in np.arange(far - 0.01, far + 0.12, 0.002) for im in (1e-5, 3e-5, 1e-4, 3e-4, 1e-3)]
    grid = sorted((g([re, im]), re, im) for re, im in pts)
    best = None
    for v0, re, im in grid[:4]:
        z0 = [re, im]
        r = minimize(g, z0, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-18, 'maxiter': 800,
                                                            'initial_simplex': [z0, [re + 1e-3, im], [re, im * 2.0]]})
        if r.fun < 1e-10 and r.x[1] > 1e-6 and r.x[0] > w + 1e-4 and (best is None or r.x[0] < best[0]):
            best = (float(r.x[0]), float(r.x[1]), float(r.fun))
    if best is None:
        return {'kind': 'dissolved', 'omega_occupied': w, 'far_continuum_from': far, 'growth_rate': 0.0}
    return {'kind': 'complex', 'omega_occupied': w, 'omega_partner': best[0], 'growth_rate': best[1], 'sv': best[2],
            'far_continuum_from': far}


def _partner_job(args):
    name, G = args
    snp = load_snapshot(name, G)
    return ('%s G=%g' % (name, G)), (partner_level(*snp) if snp is not None else None)


def main():
    t0 = time.time()
    rep = Report()
    out = {'units': 'm_Psi = 1', 'muL': -0.6, 'muR': 0.0}

    # ---------------- KR1: the charge form and the Fock representation of one mode
    evB = np.linalg.eigvalsh(BKR)
    herm, invol = np.allclose(BKR, BKR.conj().T), np.allclose(BKR @ BKR, I16)
    fock = {}
    for kappa in (-1, 1):
        # basis |0>, |1>; a |1> = |0>; the Krein metric eta = diag(1, -kappa); the Krein adjoint a^K = eta^{-1} a^dagger eta
        a = np.array([[0.0, 1.0], [0.0, 0.0]])
        eta = np.diag([1.0, -kappa])
        aK = np.linalg.inv(eta) @ a.T @ eta
        anti = a @ aK + aK @ a
        omega = 0.7
        Hm = -kappa * omega * aK @ a
        comm = Hm @ aK - aK @ Hm
        # the other vacuum: |1> annihilated by a^K, the hole a|1> = |0> ... its norm relative to the vacuum norm
        norm_particle = (eta[1, 1] / eta[0, 0])
        norm_hole = (eta[0, 0] / eta[1, 1])
        fock[kappa] = {'anticommutator': float(anti[0, 0]), 'anticommutator_is_multiple_of_1': bool(np.allclose(anti, anti[0, 0] * np.eye(2))),
                       'norm_one_quantum': float(norm_particle), 'norm_hole_relative': float(norm_hole),
                       'H_raises_by_omega': bool(np.allclose(comm, omega * aK))}
    # the derivation from the field: in a basis of modes u_n of the 16 components with u_n^dagger B u_m = kappa_n delta_nm
    # (the eigenvectors of B), Psi = sum_n a_n u_n gives a_n = kappa_n u_n^dagger B Psi, and the canonical anticommutator
    # {Psi, Psi^dagger} = -B gives {a_n, a_m^dagger} = kappa_n kappa_m u_n^dagger B (-B) B u_m = -kappa_n delta_nm
    evB2, Ub = np.linalg.eigh(BKR)
    kap_n = np.sign(evB2)
    gram_B = Ub.conj().T @ BKR @ Ub
    acomm = np.diag(kap_n) @ Ub.conj().T @ BKR @ (-BKR) @ BKR @ Ub @ np.diag(kap_n)
    derived_ok = bool(np.allclose(gram_B, np.diag(kap_n)) and np.allclose(acomm, -np.diag(kap_n)))
    sh16 = K.Shooter(0.05, -0.6, 0.0, 40.0, 0.02, 16)
    neg, pos, ev, s = sh16.krein_split(WB, 8)
    conj_charges = sorted(round(krein_charge(conj(o), sh16.h), 9) for o in neg + pos)
    out['KR1'] = {'B_eigenvalues': [float(x) for x in evB], 'fock': {str(k): v for k, v in fock.items()},
                  'anticommutator_derived_from_the_field': derived_ok, 'krein_charges_of_conjugates': conj_charges}
    rep.check('KR1_charge_form', herm and invol and int(np.sum(evB > 0)) == 8 and int(np.sum(evB < 0)) == 8 and derived_ok
              and all(fock[k]['anticommutator'] == -k and fock[k]['anticommutator_is_multiple_of_1'] and fock[k]['norm_one_quantum'] == -k
                      and fock[k]['norm_hole_relative'] == -k and fock[k]['H_raises_by_omega'] for k in (-1, 1))
              and len(neg) == 4 and len(pos) == 4
              and all(round(krein_charge(conj(o), sh16.h), 6) == 1.0 for o in neg)
              and all(round(krein_charge(conj(o), sh16.h), 6) == -1.0 for o in pos),
              'B = i sigma16 gamma^(4) is a Hermitian involution with eight eigenvalues +1 and eight -1; expanding the field in '
              'modes with u_n^dagger B u_m = kappa_n delta_nm, the canonical anticommutator {Psi, Psi^dagger} = -B gives '
              '{a_n, a_m^dagger} = -kappa_n delta_nm (derived for the 16 modes of B); the Fock space of one mode of Krein '
              'charge kappa with the indefinite metric diag(1, -kappa) represents it: the one-quantum state has the norm '
              '-kappa for either vacuum (particle or hole), and [H, a^K] = omega a^K: the particles and the holes of the Krein-positive modes are '
              'ghosts (norm -1), those of the Krein-negative modes physical (norm +1), all at positive energy; the conjugates '
              'of the four Krein-negative (positive) bound states at '
              '+omega_b are Krein-positive (negative) states at -omega_b')

    # ---------------- KR2: the symmetries at rest and their breaking by motion
    alg = symmetry_algebra()
    keep = real_null(lambda X: X @ BKR - BKR @ X, alg)
    mix = real_null(lambda X: X @ BKR + BKR @ X, alg)
    compact_keep = sum(np.allclose(X, -X.conj().T) for X in keep)
    herm_mix = sum(np.allclose(X, X.conj().T) for X in mix)
    boosts_ir = [K.sig(i, r) for i in (1, 2, 3) for r in (5, 6, 7)]

    def in_span(X, L):
        Bm = np.array([np.concatenate([Y.real.ravel(), Y.imag.ravel()]) for Y in L]).T
        x = np.concatenate([X.real.ravel(), X.imag.ravel()])
        c = np.linalg.lstsq(Bm, x, rcond=None)[0]
        return float(np.linalg.norm(Bm @ c - x))
    ir_in = max(in_span(X, mix) for X in boosts_ir)
    alg_moving = symmetry_algebra([T[1], T[2], T[3]])
    moving_keep = all(np.allclose(X @ BKR, BKR @ X) for X in alg_moving)
    moving_compact = all(np.allclose(X, -X.conj().T) for X in alg_moving)
    out['KR2'] = {'dimension_at_rest': len(alg), 'sector_keeping': len(keep), 'compact_among_them': int(compact_keep),
                  'sector_mixing': len(mix), 'hermitian_boosts_among_them': int(herm_mix),
                  'space_extra_time_boosts_in_the_mixing_part_residual': ir_in, 'dimension_moving': len(alg_moving)}
    rep.check('KR2_symmetry_at_rest', len(alg) == 32 and len(keep) == 16 and compact_keep == 16 and len(mix) == 16
              and herm_mix == 16 and ir_in < 1e-9 and len(alg_moving) == 4 and moving_keep and moving_compact,
              'at rest the sigma16-preserving matrices that commute with gamma^(0), gamma^(4), Gamma_8 form a Lie algebra of '
              'real dimension %d: %d compact generators keep the Krein sectors, %d Hermitian generators anticommute with B and '
              'mix them (the nine space-extra-time boosts Sigma^{ir} among them, residual %.1e); with gamma^(1), gamma^(2), '
              'gamma^(3) added (moving particles) %d generators remain, compact and sector-keeping (u(1) + su(2) of the extra '
              'times)' % (len(alg), len(keep), len(mix), ir_in, len(alg_moving)))

    # ---------------- KR3: the reflections across the fold
    Sneg = np.array([flat(o) for o in neg]).T
    Spos = np.array([flat(o) for o in pos]).T
    r1_neg = max(np.linalg.norm(flat(reflect(o, S1)) - flat(o)) / np.linalg.norm(flat(o)) for o in neg)
    r1_pos = max(np.linalg.norm(flat(reflect(o, S1)) + flat(o)) / np.linalg.norm(flat(o)) for o in pos)

    def resid_in(v, Sb):
        c = np.linalg.lstsq(Sb, v, rcond=None)[0]
        return float(np.linalg.norm(Sb @ c - v) / np.linalg.norm(v))
    r2_np = max(resid_in(flat(reflect(o, S2)), Spos) for o in neg)
    r2_pn = max(resid_in(flat(reflect(o, S2)), Sneg) for o in pos)
    sigma_props = {'S1 keeps sigma16': bool(np.allclose(S1.T @ SIG @ S1, SIG)), 'S2 reverses sigma16': bool(np.allclose(S2.T @ SIG @ S2, -SIG)),
                   'S1 commutes with B': bool(np.allclose(S1 @ BKR, BKR @ S1)), 'S2 anticommutes with B': bool(np.allclose(S2 @ BKR, -BKR @ S2))}
    snap = load_snapshot('I', 0.1)
    sc = {}
    if snap is not None:
        shI, wI = snap
        negW, posW, evW, sW = shI.krein_split(wI, 1)
        QW = K.QW
        S1W = QW.conj().T @ S1 @ QW
        o = negW[0]
        v, u = flat(reflect(o, S1W)), flat(o)
        c = np.vdot(u, v) / np.vdot(u, u)
        sc = {'omega': wI, 'parity': [float(c.real), float(c.imag)], 'residual': float(np.linalg.norm(v - c * u) / np.linalg.norm(v)),
              'mean_field_even': float(max(np.abs(shI.M[-1][j] - S1W @ shI.M[1][j] @ S1W.conj().T).max() for j in range(0, shI.n + 1, 25))
                                       / np.abs(shI.M[1]).max())}
    out['KR3'] = {'R1_even_residual_negative': r1_neg, 'R1_odd_residual_positive': r1_pos, 'R2_maps_negative_to_positive': r2_np,
                  'R2_maps_positive_to_negative': r2_pn, 'matrices': sigma_props, 'self_consistent': sc}
    rep.check('KR3_mirror_of_the_fold', r1_neg < 1e-12 and r1_pos < 1e-12 and r2_np < 1e-12 and r2_pn < 1e-12 and all(sigma_props.values())
              and sc and abs(sc['parity'][0] - 1) < 1e-8 and sc['residual'] < 1e-8 and sc['mean_field_even'] < 1e-8,
              'R_1 (T_0T_1T_2T_3, keeps sigma16 and B): the four Krein-negative bound states even (residual %.1e), the four '
              'Krein-positive odd (%.1e); R_2 (T_0T_5T_6T_7, reverses sigma16 and B): each sector mapped onto the other '
              '(%.1e, %.1e); the self-consistent occupied orbital of regime I at G_KS = 0.1 is R_1-even (parity %.8f, residual '
              '%.1e) and so is its mean field (relative deviation %.1e)' % (
                  r1_neg, r1_pos, r2_np, r2_pn, sc.get('parity', [float('nan')])[0], sc.get('residual', float('nan')),
                  sc.get('mean_field_even', float('nan'))))

    # ---------------- KR4: flat directions and the linear response of the bound level
    kr4 = {}
    ok4 = False
    if snap is not None:
        shI, wI = snap
        negW, posW, evW, sW = shI.krein_split(wI, 1)
        occ = K.lift(negW[0])
        base = K.full_residuals(shI, wI, occ, 0.1)
        fam = []
        for kx in (0, 7, 13):
            X = mix[kx] / np.linalg.norm(mix[kx], 2)
            for th in (0.3, 1.0):
                U = sla.expm(th * X)
                occU = [(o_[0] @ U.T, o_[1] @ U.T) for o_ in occ]
                rr = K.full_residuals(shI, wI, occU, 0.1)
                # the positive-definite norm int |chi|^2 of the boosted orbitals relative to the original ones: it grows while
                # the Krein charges stay -1 (the Krein-positive admixture)
                grow = float(sum(np.linalg.norm(o_[i]) ** 2 for o_ in occU for i in (0, 1))
                             / sum(np.linalg.norm(o_[i]) ** 2 for o_ in occ for i in (0, 1)))
                fam.append({'generator': kx, 'theta': th, 'res_ode': rr[0], 'res_match': rr[1], 'charges': rr[2], 'offdiag': rr[3],
                            'norm_U': float(np.linalg.norm(U, 2)), 'positive_norm_growth': grow})
        rpa = rpa_bound_level(shI, wI, 0.1)
        kr4 = {'base_residuals': [base[0], base[1]], 'family': fam, 'linear_response': rpa}
        ok4 = (all(abs(f['res_ode'] - base[0]) < 0.05 * base[0] and (f['theta'] < 0.5 or f['positive_norm_growth'] > 1.5) and f['res_match'] < 1e-12 and all(abs(q + 1) < 1e-9 for q in f['charges'])
                   and f['offdiag'] < 1e-9 for f in fam)
               and all(abs(q - 1) < 1e-6 for q in rpa['empty_krein_charges']) and rpa['smin_empty'] < 1e-7
               and rpa['max_abs_frequency'] < 0.05 * rpa['splitting'] and rpa['A_hermitian'] < 1e-15 and rpa['B_symmetric'] < 1e-15
               and rpa['n_imaginary'] >= 1)
    out['KR4'] = kr4
    rep.check('KR4_flat_directions', ok4,
              'regime I, G_KS = 0.1: three boosts e^{theta X} (theta = 0.3, 1; |U| = e^theta) map the self-consistent gas onto '
              'self-consistent gases (residual of the 16-dimensional Kohn-Sham equation %.2e as without the boost, fold matching '
              '%.0e, Krein charges -1, Krein-orthogonal) whose orbitals carry Krein-positive admixtures (their positive-definite norm grows '
              'up to %.2f times while the charges stay -1): the boosts are exact flat directions of the self-consistent gas; the '
              'linear response truncated to the bound level (16 admixtures of the four empty Krein-positive orbitals, splitting '
              '%.3e) has frequencies of the order 1e-4 (largest |nu| %.2e), %d of them imaginary (|Im nu| up to %.2e, the '
              'largest real one %.2e): exact zero modes would give 0, so the truncation error is as large as these frequencies, '
              'and the truncated response does not decide whether the dilute gas is stable' % (
                  kr4.get('base_residuals', [float('nan')])[0], max([f['res_match'] for f in kr4.get('family', [])] or [float('nan')]),
                  max([f['positive_norm_growth'] for f in kr4.get('family', [])] or [float('nan')]),
                  kr4.get('linear_response', {}).get('splitting', float('nan')),
                  kr4.get('linear_response', {}).get('max_abs_frequency', float('nan')),
                  kr4.get('linear_response', {}).get('n_imaginary', -1),
                  kr4.get('linear_response', {}).get('max_abs_imaginary', float('nan')),
                  kr4.get('linear_response', {}).get('largest_real_frequency', float('nan'))))

    # ---------------- KR5: the Krein-positive partner level in the self-consistent mean fields (two processes)
    from multiprocessing import Pool
    jobs = [(n, g) for n in ('I', 'II', 'III') for g in SNAPSHOT_G]
    with Pool(2) as pool:
        kr5 = dict(pool.map(_partner_job, jobs))
    out['KR5'] = kr5
    dilute_real = all(kr5['%s G=%g' % (n, g)] and kr5['%s G=%g' % (n, g)]['kind'] == 'real' for n in ('I', 'II', 'III')
                      for g in (0.01, 0.1))
    classified = all(v is not None and v['kind'] in ('real', 'complex', 'dissolved') for v in kr5.values())
    onset = {}
    for n in ('I', 'II', 'III'):
        kinds = [(g, kr5['%s G=%g' % (n, g)]['kind']) for g in SNAPSHOT_G]
        first_c = next((g for g, k in kinds if k == 'complex'), None)
        last_real = max((g for g, k in kinds if k == 'real' and (first_c is None or g < first_c)), default=None)
        diss = [g for g, k in kinds if k == 'dissolved']
        onset[n] = {'last_bound_partner': last_real, 'first_growing_mode': first_c, 'dissolved_at': diss,
                    'growth_rates': {('%g' % g): kr5['%s G=%g' % (n, g)]['growth_rate'] for g, k in kinds if k == 'complex'}}
    out['KR5_onset'] = onset
    gaps = {}
    where = {}
    for n in ('I', 'II', 'III'):
        gaps[n] = [kr5['%s G=%g' % (n, g)]['omega_partner'] - kr5['%s G=%g' % (n, g)]['omega_occupied'] for g in SNAPSHOT_G]
        for g in SNAPSHOT_G:
            v = kr5['%s G=%g' % (n, g)]
            if v['kind'] == 'complex':
                far_ = v.get('far_continuum_from')
                where['%s G=%g' % (n, g)] = ('in the continuum of the end of the box' if far_ is not None and v['omega_partner'] > far_
                                             else 'in the discrete spectrum')
    gaps_grow = all(all(b > a for a, b in zip(gaps[n][:-1], gaps[n][1:])) for n in gaps)
    out['KR5_gap_partner_minus_occupied'] = gaps
    out['KR5_where_the_complex_partners_lie'] = where

    def describe(n):
        o = onset[n]
        parts = ['bound partner up to G_KS = %s' % o['last_bound_partner']]
        if o['dissolved_at']:
            parts.append('dissolved into the continuum of the far bulk at G_KS = %s' % ', '.join('%g' % g for g in o['dissolved_at']))
        if o['first_growing_mode'] is not None:
            parts.append('a complex partner from G_KS = %g (Gamma = %s m_Psi; %s)' % (
                o['first_growing_mode'], ', '.join('%.1e at %s' % (v, g) for g, v in o['growth_rates'].items()),
                ', '.join(sorted(set(where['%s G=%s' % (n, g)] for g in o['growth_rates'])))))
        parts.append('the gap partner - occupied %s' % ', '.join('%.4f' % x for x in gaps[n]))
        return 'regime %s: %s' % (n, ', '.join(parts))
    rep.check('KR5_partner_level', classified and dilute_real and gaps_grow,
              'the Krein-positive partner of the occupied level in the self-consistent mean field (G_KS = 0.01, 0.1, 0.2, '
              '0.3, 0.5, 0.7, 1): %s; the partner moves away from the occupied level as G_KS grows (it cannot mix with it: '
              'they have opposite R_1 parity in an R_1-even mean field), and it turns complex where it reaches the continuum '
              'at the end of the computational box (regime I; this depends on the size of the box, which was not varied) or '
              'meets another level (regimes II and III); dilute gas (G_KS = 0.01, 0.1) with a bound, real partner in all three '
              'regimes: %s' % ('; '.join(describe(n) for n in ('I', 'II', 'III')), dilute_real))

    # ---------------- KR6: selection rules at the fold
    negm = [conj(o) for o in pos]    # negative-frequency modes of Krein charge -1: their holes are physical antiparticles
    posm = [conj(o) for o in neg]    # negative-frequency modes of Krein charge +1: their holes are ghost antiparticles

    def amps(Op):
        m = lambda A, B: max(abs(fold_value(b, a, Op)) for a in A for b in B)
        return {'physical_to_physical': m(neg, neg), 'physical_to_ghost': m(neg, pos), 'pair_physical': m(neg, negm),
                'pair_physical_with_ghost_antiparticle': m(neg, posm), 'pair_ghost_with_physical_antiparticle': m(pos, negm)}
    classes = {'fold_chirality_blind': [], 'fold_chiral': [], 'other': []}
    for r in range(9):
        for I in itertools.combinations(range(8), r):
            Op = I16.copy()
            for a in I:
                Op = Op @ T[a]
            v = amps(Op)
            mixes = v['physical_to_ghost'] > 1e-9 or v['pair_physical_with_ghost_antiparticle'] > 1e-9 or v['pair_ghost_with_physical_antiparticle'] > 1e-9
            if set(I) <= {1, 2, 3, 4}:
                classes['fold_chirality_blind'].append(mixes)
            elif set(I) >= {0, 5, 6, 7}:          # the products Gamma_J Gamma_8, J within {1, 2, 3, 4}
                classes['fold_chiral'].append(mixes)
            else:
                classes['other'].append(mixes)
    portal_ops = {'P_L (Higgs portal)': K.PLN, 'P_R': K.PRN, '1': I16, 'gamma^(4)': T[4], 'gamma^(4) P_L': T[4] @ K.PLN,
                  'gamma^(1)': T[1], 'gamma^(1) P_L': T[1] @ K.PLN, 'Sigma^{12}': K.sig(1, 2), 'Sigma^{12} P_L': K.sig(1, 2) @ K.PLN,
                  'Sigma^{14}': K.sig(1, 4), 'Sigma^{14} P_L': K.sig(1, 4) @ K.PLN, 'Gamma_8': G8}
    table = {nm: amps(Op) for nm, Op in portal_ops.items()}
    mov = {}
    for k in (0.05, 0.15):
        w, nk_, pk_, nk = moving_states(k)
        mm = lambda Op: (max(abs(fold_value(b, a, Op)) for a in nk_ for b in pk_), max(abs(fold_value(b, a, Op)) for a in nk_ for b in nk_))
        mov[str(k)] = {'omega': w, 'states': nk, 'krein': [len(nk_), len(pk_)],
                       'physical_to_ghost': {nm: mm(Op)[0] for nm, Op in (('1', I16), ('gamma^(4)', T[4]), ('gamma^(1)', T[1]),
                                                                        ('gamma^(2)', T[2]), ('Sigma^{12}', K.sig(1, 2)),
                                                                        ('Sigma^{24}', K.sig(2, 4)), ('gamma^(4) Gamma_8', T[4] @ G8))}}
    out['KR6'] = {'counts': {k: [len(v), int(sum(v))] for k, v in classes.items()}, 'portal_table': table, 'moving': mov}
    hl = table['P_L (Higgs portal)']
    ok6 = (len(classes['fold_chirality_blind']) == 16 and not any(classes['fold_chirality_blind'])
           and len(classes['fold_chiral']) == 16 and all(classes['fold_chiral'])
           and all(max(mov[str(k)]['physical_to_ghost'][n] for n in ('1', 'gamma^(4)', 'gamma^(1)', 'gamma^(2)')) < 1e-9 for k in (0.05, 0.15))
           and mov['0.15']['physical_to_ghost']['Sigma^{12}'] > 2 * mov['0.05']['physical_to_ghost']['Sigma^{12}'] > 0
           and hl['physical_to_ghost'] < 1e-12 and hl['pair_physical'] < 1e-12 and hl['pair_physical_with_ghost_antiparticle'] > 0.1)
    rep.check('KR6_selection_rules', ok6,
              'at the fold, at rest: none of the 16 chirality-blind fold operators (products of gamma^(1)..gamma^(4)) connects a '
              'physical state with a ghost, each of the 16 chiral ones (times Gamma_8) does; the Higgs portal P_L: elastic %.3f, '
              'conversion %.0e, physical pair %.0e (p-wave), physical particle with ghost antiparticle %.3f (s-wave); moving '
              'along x_1 (k = 0.05, 0.15): the scalar, density and vector currents still do not mix (below 1e-9), the magnetic '
              'dipole Sigma^{12} does, %.1e and %.1e, in proportion to k' % (
                  hl['physical_to_physical'], hl['physical_to_ghost'], hl['pair_physical'], hl['pair_physical_with_ghost_antiparticle'],
                  mov['0.05']['physical_to_ghost']['Sigma^{12}'], mov['0.15']['physical_to_ghost']['Sigma^{12}']))

    # ---------------- KR7: the consequence
    ratio = hl['pair_physical_with_ghost_antiparticle'] / hl['physical_to_physical']
    out['KR7'] = {'higgs_portal_ghost_pair_over_elastic': ratio,
                  'vacuum': 'stable in the positive-energy quantisation: every quantum raises H by its frequency (KR1)',
                  'unitarity': 'violated by the chiral parts of the portals (KR6); the Higgs portal is purely left-handed'}
    rep.check('KR7_consequence', ratio > 0.5 and fock[1]['H_raises_by_omega'] and fock[-1]['H_raises_by_omega'] and dilute_real,
              'in the positive-energy quantisation every quantum of the free field carries positive energy, so the vacuum is '
              'the state of lowest energy and cannot decay; the left-handed Higgs portal creates a physical particle chi with a '
              'ghost antiparticle at rest with %.2f times its elastic amplitude: ghosts are produced wherever the chiral portals '
              'act (without the self-interaction their bound level is degenerate with that of the particles), so with chiral '
              'fold couplings UM-3 is not unitary; chirality-blind couplings are necessary for a unitary UM-3 (at rest they '
              'never connect the two sectors), but not shown to be sufficient (the magnetic dipole connects them for moving '
              'particles, KR6); the classical stability of the gas is not decided: the exact boosts are flat directions, the '
              'truncated response of the dilute gas has frequencies of the order of its truncation error (KR4), and the '
              'complex partners of the dense gases are not converged in the size of the box (KR5)' % ratio)

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'krein.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_krein.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'krein_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
