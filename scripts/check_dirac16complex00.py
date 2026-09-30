#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent exact checker of the Stage-5 theory of dirac16complex00 (sympy +
mpmath + standard library, with the Stage-1 Python engines).

dirac16complex00 is the CLASSICAL 16-component Pin(4,4) spinor field whose
components are COMMUTING complex scalar fields (the analogue of Dirac's original
4-component wave function); dirac16complex is the second-quantized field with
Grassmann-odd components of Stages 1-4.  Both use the same Lagrangian

    L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
                  - m Psibar Psi - U(Psibar Psi) ]                        (L1)

with the explicit mass term L_m = -m sqrt|g| Psibar Psi (linear in m, quadratic in
the components).  This script re-derives STAGE5_SPEC sections 1-3 for the
commuting field and the side-by-side Grassmann statements, independently of the
Wolfram verifier (wolfram/Dirac16Complex00.wl):

  algebra        gamma^8, C, B, S^{ab} facts; the Pin(4,4) module; invariant forms
  lagrangian     reality of (L1) for commuting components (exact Gaussian-rational
                 jets and the bilinear-symmetry proof), coefficient Hermiticity,
                 the flat Grassmann Lagrangian (Hermitian, Euler-Lagrange), the
                 explicit mass term (commuting spinors, Grassmann elements), the
                 flat dispersion k^2 = m^2
  realRestriction the notebook-type Lagrangian Lg[] = sqrt|g|[Psi^T sigma16 T16^a
                 D_a Psi + H M Psi^T sigma16 Psi]: non-trivial for real commuting
                 Psi (symbolic jets), a pure divergence for real Grassmann Psi
                 (flat and at a curved point), the relation to (L1)
  connection     gamma^mu Omega_mu != 0, divergence identity, spinor curvature,
                 Lichnerowicz constant, the Omega term of the field equation
  EL             Euler-Lagrange equations with SYMBOLIC jets (sparse exact
                 polynomials in the jet coordinates, m, lambda, U(S), U'(S)),
                 commuting (flat, G1, G2) and Grassmann (flat, G1) components
  EMT            symmetry, reality, conservation, trace, current, general smooth U,
                 the full vielbein variation (own closed form, validated by exact
                 linearisation), Gaussian-normal observer splits, homogeneous EoS
  specifics      indefinite charge density, classical energy unbounded below
                 (explicit exact solutions)
  primordial     the Stage-2 primordial field (arbitrary a4): geometry, component
                 field equations, the exact homogeneous state and its EoS, the
                 static field sourced exactly by a commuting homogeneous state
                 (both charts)
  static         the Stage-4 static warped chart: reduced equation, eight 2x2 blocks
                 (own construction, compared with kohn-sham-theory.json), classical
                 modes versus Kohn-Sham orbitals (Krein weights), box modes, one-body
                 mean-field EMT formulas
  citations      the Stage-1..4 Python reports that are cited (hash-validated)
  wolfram        S5_agreesWithWolfram: every exported number/matrix/formula of
                 artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json
                 and the comparable measurements of the Wolfram report, compared
                 with the values derived here (recorded as not-run if absent)

Nothing produced by Wolfram is used as truth: every value is computed here and
only then compared.

Conventions (CONTRACT.md with errata section 11, STAGE2_SPEC.md, STAGE4_SPEC.md
with errata sections 7-9, STAGE5_SPEC.md): zero-based indices, x4 = time,
eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), gamma^a = notebook T16^A[a], C = sigma16 =
gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C, B = -i C gamma^4,
gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8), Omega_mu = (1/2) omega_{mu ab} S^{ab},
omega_{mu ab} = eta_ac omega_mu^c_b, D_mu Psi = d_mu Psi + Omega_mu Psi.  EMT sign:
T_{mu nu} = -(2/sqrt|g|) delta S/delta g^{mu nu}, rho = T_44 in Gaussian normal time,
p_(i) = T^i_i (no sum), T^4_4 = -rho.

Exactness: every decision is an exact zero test in Q, Q(i), the Stage-1/2 exact
rational-function fields (with their relation sin^2 + cos^2 = 1), sparse exact
polynomials over these, exact Grassmann algebras, or sympy exact simplification.
No floating-point number is used for a decision.

Prints check_<name>=true|false, measurement_<name>=..., check_count,
failed_check_count; exits nonzero on failure; writes
artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json
{schemaVersion, producer, checks, measurements, sourceSha256, inputSha256}.

Usage: python scripts/check_dirac16complex00.py [--output PATH] [--theory PATH]
       [--wolfram-report PATH] [--quick] [--families a,b,...] [--no-write]
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import random
import re
import sys
import time
from fractions import Fraction

import mpmath
import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.domains import QQ_I

HERE = os.path.dirname(os.path.abspath(__file__))
REPOSITORY_ROOT = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import d16c_exact as EX  # noqa: E402  (Fraction linear algebra, CONTRACT section 1 gammas)
import d16c_geometry_sympy as G  # noqa: E402  (Stage-1 exact jet geometry engine)
from grassmann_algebra import (Grassmann, GaussianRational, JetGrassmann, JetSpace,  # noqa: E402
                               bilinear, euler_lagrange_all, linear)

PAIR_DIRECTORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "pair-creation")
DEFAULT_OUTPUT = os.path.join(PAIR_DIRECTORY, "python-dirac16complex00-report.json")
DEFAULT_THEORY = os.path.join(PAIR_DIRECTORY, "dirac16complex00-theory.json")
DEFAULT_WOLFRAM_REPORT = os.path.join(PAIR_DIRECTORY, "wolfram-dirac16complex00-report.json")
DEFAULT_FIXTURE = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "arbitrary-field",
                               "algebra-fixture.json")
KS_THEORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "kohn-sham", "kohn-sham-theory.json")
PRODUCER = "scripts/check_dirac16complex00.py"
SOURCE_FILES = ("scripts/check_dirac16complex00.py", "scripts/d16c_exact.py", "scripts/d16c_geometry_sympy.py",
                "scripts/grassmann_algebra.py")
FAMILIES = ("algebra", "lagrangian", "realRestriction", "connection", "EL", "EMT", "specifics", "primordial",
            "static", "citations")
WOLFRAM_CHECK = "S5_agreesWithWolfram"
CONVENTIONS = {
    "indices": "zero-based: x = {x0..x7}, x4 = time, frame indices a = 0..7, spinor indices 0..15",
    "metric": "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)",
    "gammas": "gamma^a = notebook T16^A[a] rebuilt from CONTRACT section 1 (d16c_exact), compared with algebra-fixture.json",
    "adjoint": "C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C, B = -i C gamma^4, gamma^8 = diag(-I8, +I8)",
    "connection": "Omega_mu = (1/2) omega_{mu ab} S^{ab}, omega_{mu ab} = eta_ac omega_mu^c_b, D_mu Psi = d_mu Psi + Omega_mu Psi, "
                  "D_mu Psibar = d_mu Psibar - Psibar Omega_mu",
    "lagrangian": "L = sqrt|g| [(1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - U(Psibar Psi)], "
                  "default U = (lambda/2) S^2, S = Psibar Psi",
    "emt": "T_{mu nu} = -(2/sqrt|g|) delta S/delta g^{mu nu} = -(1/4)[Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi "
           "- (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi] + g_{mu nu} L_s (all indices down); rho = T_44 in "
           "Gaussian normal time (g_44 = -1), p_(i) = T^i_i (no sum), T^4_4 = -rho (Stage-1 convention, kept)",
    "splits": "KE_L = (1/2) K_4, K_4 = (1/2)(Psibar gamma^{x4} D_4 Psi - (D_4 Psibar) gamma^{x4} Psi), PE_L = rho - KE_L; "
              "KE_H = -K_perp (sum over mu != 4), PE_H = m S + U",
    "commutingProxy": "for polynomial identities Psi and Psi^* are independent commuting jet variables (chi = Psi^*); "
                      "reality is decided by the swap symmetry of the real-coefficient polynomial L(chi, psi) and by "
                      "exact Gaussian-rational data with Psi^dagger = conj(Psi)",
}
ETA = (1, 1, 1, 1, -1, -1, -1, -1)
TIME = 4


# ---------------------------------------------------------------------------
# 0. bookkeeping
# ---------------------------------------------------------------------------

class Recorder:
    """Top-level checks S5_<name> (each the conjunction of computed sub-results) and measurements."""

    def __init__(self):
        self.checks = {}
        self.measurements = {}

    def check(self, name, value, detail=None):
        key = "S5_" + name
        if key in self.checks:
            raise KeyError("duplicate check %s" % key)
        self.checks[key] = bool(value)
        if detail is not None:
            self.measurements[name] = detail
        return bool(value)

    def measure(self, name, value):
        self.measurements[name] = value
        return value


def qstr(value):
    """Exact rational (int, Fraction, gmpy2 mpq, sympy Rational) as 'n' or 'n/d'."""
    if isinstance(value, bool):
        raise TypeError("boolean is not a rational")
    if isinstance(value, int):
        return str(value)
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else "%d/%d" % (value.numerator, value.denominator)
    if isinstance(value, sp.Basic):
        if not value.is_Rational:
            return str(value)
        return str(value)
    if type(value).__name__ == "mpq":
        f = Fraction(int(value.numerator), int(value.denominator))
        return qstr(f)
    return str(value)


def to_fraction(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if type(value).__name__ == "mpq":
        return Fraction(int(value.numerator), int(value.denominator))
    if isinstance(value, sp.Basic) and value.is_Rational:
        return Fraction(int(value.p), int(value.q))
    if isinstance(value, str):
        return Fraction(value)
    raise TypeError("not a rational: %r" % (value,))


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def relative(path):
    return os.path.relpath(os.path.abspath(path), REPOSITORY_ROOT).replace(os.sep, "/")


def all_true(mapping):
    """True iff every leaf of a nested dict/list of booleans is True (non-boolean leaves ignored)."""
    if isinstance(mapping, bool):
        return mapping
    if isinstance(mapping, dict):
        return all(all_true(v) for v in mapping.values() if isinstance(v, (bool, dict, list)))
    if isinstance(mapping, list):
        return all(all_true(v) for v in mapping if isinstance(v, (bool, dict, list)))
    return True


# ---------------------------------------------------------------------------
# 1. deterministic exact random data (the Stage-1 64-bit LCG, as documented in
#    dirac16complex00-theory.json "randomFieldData"; used to reproduce exported
#    numbers, never as truth) and a local seeded generator for own checks
# ---------------------------------------------------------------------------

def lcg_rationals(seed, count):
    """state' = (6364136223846793005 state + 1442695040888963407) mod 2^64 (state_0 = seed);
    value_k = (floor(state_k/2^33) mod 19 - 9) / (floor(state_k/2^13) mod 9 + 1), k = 1..count."""
    state = seed
    out = []
    for _ in range(count):
        state = (6364136223846793005 * state + 1442695040888963407) % (1 << 64)
        out.append(Fraction(((state >> 33) % 19) - 9, ((state >> 13) % 9) + 1))
    return out


def lcg_symmetric(seed):
    values = lcg_rationals(seed, 36 * 16)
    arr = [[None] * 8 for _ in range(8)]
    k = 0
    for i in range(8):
        for j in range(i, 8):
            block = values[16 * k:16 * k + 16]
            arr[i][j] = block
            arr[j][i] = block
            k += 1
    return arr


def lcg_field_data(seed):
    """(Psi, d Psi, dd Psi, Psi^dagger, d Psi^dagger, dd Psi^dagger) of the Stage-1 fdata[seed]
    (derivatives, not Taylor coefficients; d Psi[mu][a])."""
    d1 = lcg_rationals(seed + 1, 128)
    d4 = lcg_rationals(seed + 4, 128)
    return (lcg_rationals(seed, 16), [d1[16 * mu:16 * mu + 16] for mu in range(8)], lcg_symmetric(seed + 2),
            lcg_rationals(seed + 3, 16), [d4[16 * mu:16 * mu + 16] for mu in range(8)], lcg_symmetric(seed + 5))


def jet_from_derivatives(value, first, second, dom, order=2):
    """TJet with Taylor coefficients from derivative data (d_mu d_nu f / alpha!)."""
    c = {(): np.array([dom.conv(sp.Rational(v.numerator, v.denominator)) if isinstance(v, Fraction) else v
                       for v in value], dtype=object)}
    if order >= 1:
        for mu in range(8):
            c[(mu,)] = np.array([dom.conv(sp.Rational(v.numerator, v.denominator)) if isinstance(v, Fraction) else v
                                 for v in first[mu]], dtype=object)
    if order >= 2:
        for mu in range(8):
            for nu in range(mu, 8):
                row = []
                for v in second[mu][nu]:
                    w = dom.conv(sp.Rational(v.numerator, v.denominator)) if isinstance(v, Fraction) else v
                    row.append(w * dom.frac(1, 2) if mu == nu else w)
                c[(mu, nu)] = np.array(row, dtype=object)
    return G.TJet(order, c)


# ---------------------------------------------------------------------------
# 2. sparse exact commutative polynomials in jet coordinates (symbolic field jets)
# ---------------------------------------------------------------------------

def _zero_scalar(value):
    try:
        return value == 0
    except Exception:  # noqa: BLE001
        return False


class Poly:
    """Sparse polynomial {sorted tuple of variable ids: exact coefficient}.  Coefficients may be
    Python ints, Fractions, gmpy2 mpq, Gaussian rationals or elements of the Stage-1/2 exact fields.
    Derivations (partial derivatives, total derivatives in jet space, chain rules for U(S)) are
    implemented by ``derivation`` (Leibniz rule with a user-given image of every variable)."""

    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {} if terms is None else terms

    @staticmethod
    def const(value):
        return Poly({(): value}) if not _zero_scalar(value) else Poly()

    @staticmethod
    def var(index, coeff=1):
        return Poly({(index,): coeff})

    def copy(self):
        return Poly(dict(self.t))

    def _acc(self, mono, coeff):
        old = self.t.get(mono)
        if old is None:
            if not _zero_scalar(coeff):
                self.t[mono] = coeff
        else:
            new = old + coeff
            if _zero_scalar(new):
                del self.t[mono]
            else:
                self.t[mono] = new

    def __add__(self, other):
        if isinstance(other, np.ndarray):
            return NotImplemented
        if not isinstance(other, Poly):
            if _zero_scalar(other):
                return self
            other = Poly({(): other})
        out = Poly(dict(self.t))
        for mono, coeff in other.t.items():
            out._acc(mono, coeff)
        return out

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        if isinstance(other, np.ndarray):
            return NotImplemented
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def partials(self):
        """{var: d self / d var} for every variable (one pass, plain partial derivatives)."""
        out = {}
        for mono, coeff in self.t.items():
            previous = None
            for position, var in enumerate(mono):
                if var == previous:
                    continue
                previous = var
                d = out.get(var)
                if d is None:
                    d = Poly()
                    out[var] = d
                d._acc(mono[:position] + mono[position + 1:], coeff * mono.count(var))
        return out

    def __mul__(self, other):
        if isinstance(other, np.ndarray):
            return NotImplemented
        if isinstance(other, Poly):
            out = Poly()
            for m1, c1 in self.t.items():
                for m2, c2 in other.t.items():
                    mono = tuple(sorted(m1 + m2)) if (m1 and m2) else (m1 or m2)
                    out._acc(mono, c1 * c2)
            return out
        if _zero_scalar(other):
            return Poly()
        out = {}
        for m, c in self.t.items():
            v = c * other
            if not _zero_scalar(v):
                out[m] = v
        return Poly(out)

    __rmul__ = __mul__

    def derivation(self, image):
        """Leibniz rule: D(prod of variables) = sum over factors; image(var) -> Poly or None."""
        out = Poly()
        cache = {}
        for mono, coeff in self.t.items():
            previous = None
            for position, var in enumerate(mono):
                if var == previous:
                    continue
                previous = var
                if var not in cache:
                    cache[var] = image(var)
                img = cache[var]
                if img is None or not img.t:
                    continue
                multiplicity = mono.count(var)
                rest = mono[:position] + mono[position + 1:]
                base = coeff * multiplicity
                for m2, c2 in img.t.items():
                    out._acc(tuple(sorted(rest + m2)) if (rest and m2) else (rest or m2), base * c2)
        return out

    def drop_vars(self, variables):
        variables = set(variables)
        return Poly({m: c for m, c in self.t.items() if not variables.intersection(m)})

    def evaluate(self, values):
        """Substitute exact values for every variable (dict id -> scalar)."""
        total = 0
        for mono, coeff in self.t.items():
            term = coeff
            for var in mono:
                term = term * values[var]
            total = total + term
        return total

    def coefficient_of(self, var):
        """Part linear in ``var`` divided by it (terms containing var exactly once)."""
        out = Poly()
        for mono, coeff in self.t.items():
            if mono.count(var) == 1:
                i = mono.index(var)
                out._acc(mono[:i] + mono[i + 1:], coeff)
        return out

    def is_zero(self, dom=None):
        if dom is None:
            return all(_zero_scalar(c) for c in self.t.values())
        return all(dom.is_zero(c) for c in self.t.values())

    def nterms(self):
        return len(self.t)

    def variables(self):
        s = set()
        for m in self.t:
            s.update(m)
        return s


def poly_array(values):
    arr = np.empty(len(values), dtype=object)
    for i, v in enumerate(values):
        arr[i] = v
    return arr


def poly_zero_array(shape):
    arr = np.empty(shape, dtype=object)
    for idx in np.ndindex(*shape):
        arr[idx] = Poly()
    return arr


def as_poly(value):
    return value if isinstance(value, Poly) else Poly.const(value)


class JetVars:
    """Registry of jet coordinates u_{s,a;alpha} (species s, component a, sorted derivative
    multi-index alpha, |alpha| <= 2; the VALUE of the derivative, not a Taylor coefficient) and of
    the scalar symbols m, lam, HM (bookkeeping mass of the notebook), U0 = U(S), U1 = U'(S),
    U2 = U''(S) at the point."""

    EXTRA = ("m", "lam", "HM", "U0", "U1", "U2")

    def __init__(self, species=("chi", "psi")):
        self.ids = {}
        self.labels = []
        for name in self.EXTRA:
            self._add((name,))
        self.species = tuple(species)
        for s in self.species:
            for alpha in G.multi_indices(2):
                for a in range(16):
                    self._add((s, a, alpha))

    def _add(self, key):
        self.ids[key] = len(self.labels)
        self.labels.append(key)

    def id(self, *key):
        if len(key) == 1:
            return self.ids[key]
        s, a, alpha = key
        return self.ids[(s, a, tuple(sorted(alpha)))]

    def v(self, *key):
        return Poly.var(self.id(*key))

    def vector(self, s, alpha=()):
        return poly_array([self.v(s, a, alpha) for a in range(16)])

    def gradient(self, s):
        """(8, 16) array of d_mu u_{s,a}."""
        arr = np.empty((8, 16), dtype=object)
        for mu in range(8):
            for a in range(16):
                arr[mu, a] = self.v(s, a, (mu,))
        return arr

    def shift_image(self, mu):
        """image(var) of the total derivative D_mu on the field-jet coordinates (None for scalars)."""
        def image(var):
            key = self.labels[var]
            if len(key) == 1:
                return None
            s, a, alpha = key
            if len(alpha) >= 2:
                raise ValueError("jet space too small for D_%d of %r" % (mu, key))
            return self.v(s, a, alpha + (mu,))
        return image


class Dual:
    """a + b eps with eps^2 = 0 over exact rationals (first-order exact linearisation)."""

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    @staticmethod
    def _c(x):
        return x if isinstance(x, Dual) else Dual(x, 0)

    def __add__(self, o):
        o = self._c(o)
        return Dual(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = self._c(o)
        return Dual(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return self._c(o) - self

    def __neg__(self):
        return Dual(-self.a, -self.b)

    def __mul__(self, o):
        o = self._c(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = self._c(o)
        if o.a == 0:
            raise ZeroDivisionError("dual division by a non-invertible element")
        return Dual(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))

    def __rtruediv__(self, o):
        return self._c(o) / self

    def __eq__(self, o):
        o = self._c(o)
        return self.a == o.a and self.b == o.b

    def __hash__(self):  # pragma: no cover
        return hash((self.a, self.b))


# ---------------------------------------------------------------------------
# 3. the algebra (rebuilt from CONTRACT section 1; the fixture is only compared)
# ---------------------------------------------------------------------------

def cq_matrix(real):
    """Real Fraction matrix as a Gaussian-rational (re, im) pair."""
    return (EX.fraction_matrix(real), EX.zeros(len(real), len(real[0])))


def c_i_times(matrix):
    real, imag = matrix
    return (EX.neg(imag), real)


def cvec_dot(u, M, v):
    """u^dagger M v for Gaussian-rational vectors u, v (lists of (re, im)) and M = (re, im)."""
    re_m, im_m = M
    total_re = Fraction(0)
    total_im = Fraction(0)
    for i in range(len(u)):
        ur, ui = u[i]
        if ur == 0 and ui == 0:
            continue
        acc_re = Fraction(0)
        acc_im = Fraction(0)
        for j in range(len(v)):
            mr, mi = re_m[i][j], im_m[i][j]
            if mr == 0 and mi == 0:
                continue
            vr, vi = v[j]
            acc_re += mr * vr - mi * vi
            acc_im += mr * vi + mi * vr
        # conj(u_i) (acc) with conj(u_i) = ur - i ui
        total_re += ur * acc_re + ui * acc_im
        total_im += ur * acc_im - ui * acc_re
    return (total_re, total_im)


def cmat_vec(M, v):
    re_m, im_m = M
    out = []
    for i in range(len(re_m)):
        acc_re = Fraction(0)
        acc_im = Fraction(0)
        for j in range(len(v)):
            mr, mi = re_m[i][j], im_m[i][j]
            if mr == 0 and mi == 0:
                continue
            vr, vi = v[j]
            acc_re += mr * vr - mi * vi
            acc_im += mr * vi + mi * vr
        out.append((acc_re, acc_im))
    return out


def complex_nullspace(M):
    """Exact basis of {v in Q(i)^n : M v = 0} via the realification [[A, -B], [B, A]]; returns
    complex vectors (lists of (re, im)).  The real solution space is closed under v -> i v, so the
    complex dimension is half the real one; a Q(i)-basis is extracted greedily."""
    real, imag = M
    n = len(real[0])
    rows = EX.realify(M)
    basis_real = EX.nullspace(rows, 2 * n)
    chosen = []
    for vec in basis_real:
        cand = [(vec[k], vec[n + k]) for k in range(n)]
        trial = chosen + [cand]
        mat = ([[c[k][0] for c in trial] for k in range(n)], [[c[k][1] for c in trial] for k in range(n)])
        if EX.crank(mat) == len(trial):
            chosen = trial
    return chosen


class Algebra:
    """gamma^a, C, gamma^8, S^{ab}, B as exact Fraction matrices (d16c_exact), plus the same
    objects as sympy Integer matrices."""

    def __init__(self, fixture_path=DEFAULT_FIXTURE):
        self.fixture_path = fixture_path
        self.gam = EX.notebook_gammas()
        self.C = EX.charge_matrix(self.gam)
        self.g8 = EX.chirality(self.gam)
        self.S = EX.spin_generators(self.gam)
        self.B = EX.charge_form_b(self.gam)
        self.I16 = EX.identity(16)
        self.eta = EX.eta()
        self.Pm = EX.scale(Fraction(1, 2), EX.sub(self.I16, self.g8))
        self.Pp = EX.scale(Fraction(1, 2), EX.add(self.I16, self.g8))
        gam_s, _, _, _, _ = G.notebook_gamma_sympy()
        self.gam_sym = gam_s
        self.C_sym = gam_s[0] * gam_s[1] * gam_s[2] * gam_s[3]
        self.B_sym = -sp.I * self.C_sym * gam_s[4]
        chi = sp.eye(16)
        for g in gam_s:
            chi = chi * g
        self.g8_sym = chi
        self.S_sym = {(a, b): (gam_s[a] * gam_s[b] - gam_s[b] * gam_s[a]) / 4 for a in range(8) for b in range(8)}

    def fixture_agreement(self):
        with open(self.fixture_path, "r", encoding="utf-8") as handle:
            fx = json.load(handle)
        out = {}
        out["gamma"] = all(EX.equal(EX.matrix_from_json(fx["gamma"][a]), self.gam[a]) for a in range(8))
        out["C"] = EX.equal(EX.matrix_from_json(fx["C"]), self.C)
        out["chirality"] = EX.equal(EX.matrix_from_json(fx["chirality"]), self.g8)
        out["B"] = (EX.equal(EX.matrix_from_json(fx["B"]["real"]), self.B[0])
                    and EX.equal(EX.matrix_from_json(fx["B"]["imag"]), self.B[1]))
        s_ok = True
        count = 0
        for entry in fx["S"]:
            a, b = entry["a"], entry["b"]
            s_ok = s_ok and EX.equal(EX.matrix_from_json(entry["matrix"]), self.S[(a, b)])
            count += 1
        out["S"] = s_ok and count == 28
        out["SCount"] = count
        return out


def check_algebra(alg, rec):
    gam, C, g8, B, I16 = alg.gam, alg.C, alg.g8, alg.B, alg.I16
    mm = EX.matmul
    fx = alg.fixture_agreement()
    rec.check("fixture_matchesContractConstruction", all(v for k, v in fx.items() if k != "SCount"), fx)
    facts = {}
    facts["clifford"] = all(EX.equal(EX.anticommutator(gam[a], gam[b]), EX.scale(2 * (ETA[a] if a == b else 0), I16))
                            for a in range(8) for b in range(8))
    facts["gammaSymmetryPattern"] = all((EX.is_symmetric(gam[a]) if a < 4 else EX.is_antisymmetric(gam[a]))
                                        for a in range(8))
    facts["gamma8Hermitian"] = EX.is_symmetric(g8)          # real matrix: Hermitian <=> symmetric
    facts["gamma8SquaredIsOne"] = EX.equal(mm(g8, g8), I16)
    facts["gamma8AnticommutesWithEveryGamma"] = all(EX.is_zero(EX.anticommutator(g8, gam[a])) for a in range(8))
    facts["gamma8CommutesWithC"] = EX.is_zero(EX.commutator(g8, C))
    facts["gamma8CommutesWithEveryBivector"] = all(EX.is_zero(EX.commutator(g8, mm(gam[a], gam[b])))
                                                   for a in range(8) for b in range(8))
    facts["gamma8CommutesWithEverySab"] = all(EX.is_zero(EX.commutator(g8, s)) for s in alg.S.values())
    facts["gamma8IsDiagMinusI8PlusI8"] = EX.equal(g8, EX.expected_chirality())
    facts["CRealSymmetric"] = EX.is_symmetric(C)
    facts["CSquaredIsOne"] = EX.equal(mm(C, C), I16)
    facts["CEqualsBlockDiagMinusSigmaSigma"] = EX.equal(C, EX.expected_charge_matrix())
    facts["CgammaRealAntisymmetric"] = all(EX.is_antisymmetric(mm(C, gam[a])) for a in range(8))
    facts["CSabRealAntisymmetric"] = all(EX.is_antisymmetric(mm(C, s)) for s in alg.S.values())
    facts["BHermitian"] = EX.cis_hermitian(B)
    facts["BSquaredIsOne"] = EX.cequal(EX.cmatmul(B, B), EX.cidentity(16))
    facts["BSignature"] = list(EX.hermitian_signature(B))
    facts["BEigenvaluesPlusMinusOneEight"] = facts["BSignature"] == [8, 8, 0] and facts["BSquaredIsOne"]
    facts["BCommutesWithC"] = EX.cis_zero(EX.ccommutator(B, cq_matrix(C)))
    facts["BCEqualsMinusIGamma4"] = EX.cequal(EX.cmatmul(B, cq_matrix(C)), EX.cscale(0, -1, cq_matrix(gam[4])))
    g8c = cq_matrix(g8)
    facts["gamma8Bgamma8EqualsMinusB"] = EX.cequal(EX.cmatmul_many(g8c, B, g8c), (EX.neg(B[0]), EX.neg(B[1])))
    facts["gamma8CgammaGamma8EqualsMinusCgamma"] = all(EX.equal(EX.matmul_many(g8, C, gam[a], g8),
                                                                EX.neg(mm(C, gam[a]))) for a in range(8))
    facts["Cgamma4EqualsIB"] = EX.cequal(cq_matrix(mm(C, gam[4])), c_i_times(B))
    facts["CSignature"] = list(EX.symmetric_signature(C))
    ok = all(v for k, v in facts.items() if isinstance(v, bool)) and facts["CSignature"] == [8, 8, 0]
    rec.check("algebra_leadFacts", ok, facts)

    pin = {}
    pin["commutantOfGammas"] = EX.commutant_dimension(gam)
    pin["commutantOfSpinGenerators"] = EX.commutant_dimension(list(alg.S.values()))
    s_list = list(alg.S.values())
    forms = EX.intertwiner_basis([EX.transpose(s) for s in s_list], [EX.neg(s) for s in s_list])
    pin["invariantBilinearForms"] = len(forms)
    cpm = mm(C, alg.Pm)
    cpp = mm(C, alg.Pp)
    span_rank = EX.rank([EX.flatten(f) for f in forms] + [EX.flatten(cpm), EX.flatten(cpp)])
    pin["formsSpannedByCPminusCPplus"] = span_rank == 2 and len(forms) == 2
    pin["SabRealAndCPreserving"] = all(EX.is_zero(EX.add(mm(EX.transpose(s), C), mm(C, s))) for s in s_list)
    ok = (pin["commutantOfGammas"] == 1 and pin["commutantOfSpinGenerators"] == 2 and pin["formsSpannedByCPminusCPplus"]
          and pin["SabRealAndCPreserving"])
    pin["statement"] = ("C^16 is an irreducible complex Pin(4,4) (Clifford) module (commutant 1), splitting under "
                        "Spin(4,4) into the two chiral halves (commutant 2); every S^{ab} is real with "
                        "S^T C + C S = 0, so Psi^dagger C Psi is Spin_0(4,4)-invariant (R^dagger = R^T, "
                        "R^T C R = C); the invariant forms X (S^T X + X S = 0) are spanned by C P_- and C P_+. "
                        "The 16 commuting components of dirac16complex00 carry the same representation as the "
                        "16 Grassmann components of dirac16complex.")
    rec.check("algebra_pinModuleAndSpinInvariance", ok, pin)

    anti = {"anticommutator": True, "CanticommutatorSymmetric": True, "CcommutatorAntisymmetric": True,
            "commutatorVector": True}
    for (a, b), s in alg.S.items():
        for c in range(8):
            ac = EX.anticommutator(gam[c], s)
            expected = EX.matmul_many(gam[c], gam[a], gam[b]) if c not in (a, b) else EX.zeros(16)
            anti["anticommutator"] = anti["anticommutator"] and EX.equal(ac, expected)
            anti["CanticommutatorSymmetric"] = anti["CanticommutatorSymmetric"] and EX.is_symmetric(mm(C, ac))
            cm = EX.commutator(gam[c], s)
            anti["CcommutatorAntisymmetric"] = anti["CcommutatorAntisymmetric"] and EX.is_antisymmetric(mm(C, cm))
            vec = EX.sub(EX.scale(ETA[b] if b == c else 0, gam[a]), EX.scale(ETA[a] if a == c else 0, gam[b]))
            anti["commutatorVector"] = anti["commutatorVector"] and EX.equal(EX.commutator(s, gam[c]), vec)
    rec.check("algebra_anticommutatorTotallyAntisymmetric", all(anti.values()), anti)


# ---------------------------------------------------------------------------
# 4. exact test geometries (Stage-1 engine d16c_geometry_sympy, built lazily)
# ---------------------------------------------------------------------------

G4_SEED_BASE = 64000


def g4_integers(seed, count):
    """(numerator of the LCG rational) mod 3 - 1, entries in {-1, 0, 1} (theory JSON G4 definition)."""
    return [(v.numerator % 3) - 1 for v in lcg_rationals(seed, count)]


def g4_frame_data(k=1):
    """E0 = U L (U, L unitriangular), E1[l][mu][a], E2[l][k][mu][a] of the G4 frame jet (definition
    copied from dirac16complex00-theory.json testGeometries.G4; rebuilt here, not read)."""
    u_vals = g4_integers(G4_SEED_BASE + 10 * k, 64)
    l_vals = g4_integers(G4_SEED_BASE + 1 + 10 * k, 64)
    U = [[Fraction(1 if i == j else (u_vals[8 * i + j] if j > i else 0)) for j in range(8)] for i in range(8)]
    L = [[Fraction(1 if i == j else (l_vals[8 * i + j] if j < i else 0)) for j in range(8)] for i in range(8)]
    E0 = EX.matmul(U, L)
    e1_vals = g4_integers(G4_SEED_BASE + 2 + 10 * k, 512)
    E1 = [[[Fraction(e1_vals[64 * l + 8 * mu + a]) for a in range(8)] for mu in range(8)] for l in range(8)]
    e2_vals = g4_integers(G4_SEED_BASE + 3 + 10 * k, 36 * 64)
    E2 = [[None] * 8 for _ in range(8)]
    c = 0
    for l in range(8):
        for kk in range(l, 8):
            block = e2_vals[64 * c:64 * c + 64]
            mat = [[Fraction(block[8 * mu + a]) for a in range(8)] for mu in range(8)]
            E2[l][kk] = mat
            E2[kk][l] = mat
            c += 1
    return E0, E1, E2


def g4_vielbein_jet(dom, k=1):
    E0, E1, E2 = g4_frame_data(k)

    def arr(m):
        out = np.empty((8, 8), dtype=object)
        for i in range(8):
            for j in range(8):
                out[i, j] = dom.conv(sp.Rational(m[i][j].numerator, m[i][j].denominator))
        return out

    c = {(): arr(E0)}
    for l in range(8):
        c[(l,)] = arr(E1[l])
    for l in range(8):
        for kk in range(l, 8):
            m = E2[l][kk]
            if l == kk:
                m = [[v / 2 for v in row] for row in m]
            c[(l, kk)] = arr(m)
    return G.TJet(2, c)


def static_z_domain():
    K = QQ.frac_field(G.G2_W, G.G2_C, G.G2_E)
    return G.ExactDomain(K, "QQ(w,c,E) mod (w^12+c^2-1)", relations=[G.G2_W ** 12 + G.G2_C ** 2 - 1])


def static_z_vielbein_jet(order, dom, H=1):
    """Stage-2 notebook chart with a4 = a4_0 CONSTANT (the static member), E = e^{a4_0}, H fixed:
    h = (cot z, s^{1/6} E (x3), 1, s^{1/6}/E (x3)), z = 6 H x0, s = sin z = w^6, cos z = c."""
    z = sp.Symbol("z")
    s = sp.sin(z)
    E = G.G2_E
    h = [sp.cos(z) / s] + [s ** sp.Rational(1, 6) * E] * 3 + [sp.Integer(1)] + [s ** sp.Rational(1, 6) / E] * 3
    c = {}
    for alpha in G.multi_indices(order):
        arr = np.empty((8, 8), dtype=object)
        for i in range(8):
            for j in range(8):
                arr[i, j] = dom.zero
        n0 = alpha.count(0)
        if n0 == len(alpha):
            fact = G.alpha_factorial(alpha)
            for i in range(8):
                f = sp.diff(h[i], z, n0) if n0 else h[i]
                f = f * (6 * sp.Integer(H)) ** n0 / fact
                f = f.subs({sp.sin(z): G.G2_W ** 6, sp.cos(z): G.G2_C})
                f = sp.powsimp(sp.expand_power_base(f, force=False))
                if f.free_symbols - {G.G2_W, G.G2_C, G.G2_E}:
                    raise AssertionError("unexpected symbols in the static z-chart jet: %s" % f)
                arr[i, i] = dom.conv(f)
        c[alpha] = arr
    return G.TJet(order, c)


def flat_vielbein_jet(dom, order=1):
    c = {}
    for alpha in G.multi_indices(order):
        arr = np.empty((8, 8), dtype=object)
        for i in range(8):
            for j in range(8):
                arr[i, j] = dom.one if (i == j and not alpha) else dom.zero
        c[alpha] = arr
    return G.TJet(order, c)


class Geometries:
    """Cache of exact geometries at their evaluation points (vielbein jets of order 2 unless noted)."""

    def __init__(self):
        self.qq = G.make_qq_domain()
        self.gd_qq = G.GammaData(self.qq)
        self._cache = {}
        self.timings = {}

    def _get(self, key, builder):
        if key not in self._cache:
            start = time.time()
            self._cache[key] = builder()
            self.timings[key] = round(time.time() - start, 3)
        return self._cache[key]

    def g1(self, label):
        def build():
            e = G.vielbein_jet_from_sympy(G.g1_vielbein_sympy(), G.G1_POINTS[label], 2, self.qq)
            return G.Geometry(e, self.gd_qq, self.qq, "G1" + label)
        return self._get("G1" + label, build)

    def g2(self):
        def build():
            dom = G.make_g2_domain()
            gd = G.GammaData(dom)
            return G.Geometry(G.g2_vielbein_jet(2, dom), gd, dom, "G2", sqrtg_sign=1)
        return self._get("G2", build)

    def g3(self, label):
        def build():
            e = G.vielbein_jet_from_sympy(G.g3_vielbein_sympy(), G.G3_POINTS[label], 2, self.qq)
            return G.Geometry(e, self.gd_qq, self.qq, "G3" + label, sqrtg_sign=1)
        return self._get("G3" + label, build)

    def g4(self, k=1):
        def build():
            return G.Geometry(g4_vielbein_jet(self.qq, k), self.gd_qq, self.qq, "G4p%d" % k)
        return self._get("G4p%d" % k, build)

    def flat(self):
        def build():
            return G.Geometry(flat_vielbein_jet(self.qq, 1), self.gd_qq, self.qq, "flat", sqrtg_sign=1,
                              curvature=False)
        return self._get("flat", build)

    def static_z(self):
        def build():
            dom = static_z_domain()
            gd = G.GammaData(dom)
            return G.Geometry(static_z_vielbein_jet(2, dom), gd, dom, "staticZ", sqrtg_sign=1)
        return self._get("staticZ", build)


def val(jet_or_array):
    """Scalar value of a 0-d jet/array."""
    if isinstance(jet_or_array, G.TJet):
        return jet_or_array.value()[()]
    return np.asarray(jet_or_array, dtype=object)[()]


def exact_summary(dom, x, limit=160):
    """Exact string if short, else {decimal (20 digits, display only), sha256 of the exact string}."""
    text = exact_str(dom, x)
    if len(text) <= limit:
        return text
    out = {"exactSha256": hashlib.sha256(text.encode("ascii")).hexdigest(), "exactLength": len(text)}
    try:
        f = to_fraction(x)
        with mpmath.workdps(30):
            out["decimal"] = mpmath.nstr(mpmath.mpf(f.numerator) / f.denominator, 20)
    except Exception:  # noqa: BLE001
        pass
    return out


def exact_str(dom, x):
    if isinstance(x, Poly):
        return "poly(%d terms)" % x.nterms()
    try:
        return dom.to_str(x)
    except Exception:  # noqa: BLE001
        return str(x)


# ---------------------------------------------------------------------------
# 5. (L1) with symbolic field jets and its Euler-Lagrange expressions
# ---------------------------------------------------------------------------

def obj0(x):
    a = np.empty((), dtype=object)
    a[()] = x
    return a


def const_jet(arr):
    return G.TJet.const(np.asarray(arr, dtype=object) if not isinstance(arr, np.ndarray) else arr)


def lag_parts(geo, pb, dpb, psi, dpsi):
    """Stage-1 formula pieces (d16c_geometry_sympy.lagrangian_scalar with m = lambda = 0):
    Dpsi, Dpb, kin = (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi), S = Psibar Psi."""
    return G.lagrangian_scalar(geo, pb, dpb, psi, dpsi, 0, 0)


def polys_equal(a, b, dom):
    a = np.asarray(a, dtype=object).ravel()
    b = np.asarray(b, dtype=object).ravel()
    if a.shape != b.shape:
        return False
    return all(as_poly(x - y).is_zero(dom) for x, y in zip(a, b))


class SymbolicLagrangian:
    """(L1) at one point with SYMBOLIC jets: L(x; u) = L0(u) + x^l L_l(u) + O(x^2), where u are the jet
    coordinates chi_a = Psi^*_a, psi_a, d_mu chi_a, d_mu psi_a (commuting symbols, Psi and Psi^*
    independent) and m, lambda, U(S), U'(S) are symbols.  potential: 'quartic' (U = lam S^2/2),
    'general' (U(S) = U0 with dU0 = U1 dS, dU1 = U2 dS) or 'none'."""

    def __init__(self, geo, potential="quartic", V=None):
        self.geo = geo
        self.dom = geo.dom
        self.potential = potential
        self.V = V if V is not None else JetVars()
        V = self.V
        g1 = geo.truncated(1)
        self.g1 = g1
        C = geo.gd.C
        self.chi = V.vector("chi")
        self.psi = V.vector("psi")
        self.dchi = V.gradient("chi")
        self.dpsi = V.gradient("psi")
        self.pb = np.einsum("i,ij->j", self.chi, C)
        self.dpb = np.einsum("mi,ij->mj", self.dchi, C)
        parts = lag_parts(g1, const_jet(self.pb), const_jet(self.dpb), const_jet(self.psi), const_jet(self.dpsi))
        self.S0 = as_poly(val(parts["S"]))
        m = V.v("m")
        half = self.dom.frac(1, 2)
        if potential == "quartic":
            U = V.v("lam") * self.S0 * self.S0 * half
            self.Uprime = V.v("lam") * self.S0
        elif potential == "general":
            U = V.v("U0")
            self.Uprime = V.v("U1")
        else:
            U = Poly()
            self.Uprime = Poly()
        self.kin = parts["kin"]
        Ls = parts["kin"] - const_jet(obj0(m * self.S0 + U))
        self.L = G.jmul(g1.sqrtg, Ls)
        self.L0 = as_poly(val(self.L))
        self.Ll = [as_poly(self.L.coeff((l,))[()]) for l in range(8)]
        self._p0 = None
        self._pl = None

    # -- derivatives with the chain rule for U(S) ---------------------------------
    def _chain(self, plain, var):
        """d/d var including dU0 = U1 dS, dU1 = U2 dS (plain = dict of plain partials of F)."""
        V = self.V
        out = plain.get(var, Poly())
        if self.potential == "general":
            dS = self.S0.partials().get(var)
            if dS is not None and dS.t:
                if V.id("U0") in plain:
                    out = out + plain[V.id("U0")] * V.v("U1") * dS
                if V.id("U1") in plain:
                    out = out + plain[V.id("U1")] * V.v("U2") * dS
        return out

    def partial(self, F, var, plain=None):
        return self._chain(plain if plain is not None else F.partials(), var)

    def total_derivative(self, F, mu):
        V = self.V
        shift = V.shift_image(mu)
        DS = self.S0.derivation(shift)
        U0, U1 = V.id("U0"), V.id("U1")

        def image(var):
            if var == U0:
                return V.v("U1") * DS
            if var == U1:
                return V.v("U2") * DS
            return shift(var)
        return F.derivation(image)

    def plain_partials(self):
        if self._p0 is None:
            self._p0 = self.L0.partials()
            self._pl = [p.partials() for p in self.Ll]
        return self._p0, self._pl

    def euler_lagrange(self, species):
        """E_a = dL/du_a - sum_mu D_mu (dL/du_{mu a}) at the point (jet identity)."""
        V = self.V
        p0, pl = self.plain_partials()
        E = []
        for a in range(16):
            e = self._chain(p0, V.id(species, a, ()))
            for mu in range(8):
                q = V.id(species, a, (mu,))
                e = e - self._chain(pl[mu], q) - self.total_derivative(self._chain(p0, q), mu)
            E.append(e)
        return poly_array(E)

    # -- closed forms ---------------------------------------------------------------
    def targets(self):
        """sqrt|g| C (gamma^mu D_mu psi - (m + U') psi) and -sqrt|g| ((D_mu pb) gamma^mu + (m + U') pb)."""
        g = self.geo
        C = g.gd.C
        sg0 = val(g.sqrtg)
        gam0 = g.gam.value()
        Om0 = g.Omega.value()
        Mf = self.V.v("m") + self.Uprime
        Dpsi0 = self.dpsi + np.einsum("mij,j->mi", Om0, self.psi)
        slash = np.einsum("mij,mj->i", gam0, Dpsi0)
        t_chi = np.einsum("ij,j->i", C, slash - self.psi * Mf) * sg0
        Dpb0 = self.dpb - np.einsum("j,mjk->mk", self.pb, Om0)
        t_psi = -(np.einsum("mj,mjk->k", Dpb0, gam0) + self.pb * Mf) * sg0
        return t_chi, t_psi

    def momenta_closed_forms(self):
        """P_a = dL/dchi_a, Q^mu_a = dL/d(d_mu chi_a) (value and explicit first derivatives) and the psi
        counterparts, from the formulas derived by hand in the module notes."""
        g = self.geo
        C = g.gd.C
        dom = self.dom
        half = dom.frac(1, 2)
        sg0 = val(g.sqrtg)
        gam0 = g.gam.value()
        Om0 = g.Omega.value()
        Mf = self.V.v("m") + self.Uprime
        Dpsi0 = self.dpsi + np.einsum("mij,j->mi", Om0, self.psi)
        CgD = np.einsum("ij,mjk,mk->i", C, gam0, Dpsi0)
        COg = np.einsum("ij,mjk,mkl,l->i", C, Om0, gam0, self.psi)
        P_chi = (CgD * half + COg * half - np.einsum("ij,j->i", C, self.psi) * Mf) * sg0
        Mj = G.jmul(g.sqrtg, G.jein("ij,mjk->mik", C, g.gam))            # sqrt|g| C gamma^mu as an x-jet
        Q_chi = [np.einsum("mab,b->ma", Mj.coeff(k), self.psi) * (-half) for k in [()] + [(l,) for l in range(8)]]
        pgO = np.einsum("j,mjk,mkl->l", self.pb, gam0, Om0)
        pOg = np.einsum("j,mjk,mkl->l", self.pb, Om0, gam0)
        dpg = np.einsum("mj,mjk->k", self.dpb, gam0)
        P_psi = (pgO * half - dpg * half + pOg * half - self.pb * Mf) * sg0
        Nj = G.jmul(g.sqrtg, g.gam)                                         # sqrt|g| gamma^mu as an x-jet
        Q_psi = [np.einsum("a,mab->mb", self.pb, Nj.coeff(k)) * half for k in [()] + [(l,) for l in range(8)]]
        return P_chi, Q_chi, P_psi, Q_psi

    def check_momenta(self):
        V = self.V
        dom = self.dom
        p0, pl = self.plain_partials()
        P_chi, Q_chi, P_psi, Q_psi = self.momenta_closed_forms()
        ok = True
        for species, P, Q in (("chi", P_chi, Q_chi), ("psi", P_psi, Q_psi)):
            for a in range(16):
                ok = ok and (self._chain(p0, V.id(species, a, ())) - P[a]).is_zero(dom)
                for mu in range(8):
                    q = V.id(species, a, (mu,))
                    ok = ok and (self._chain(p0, q) - Q[0][mu, a]).is_zero(dom)
                    for l in range(8):
                        ok = ok and (self._chain(pl[l], q) - Q[l + 1][mu, a]).is_zero(dom)
                if not ok:
                    return False
        return ok


def el_symbolic_point(geo, potential="quartic"):
    """Euler-Lagrange equations of (L1) at one point with symbolic jets: jet identity and closed-form
    momenta; returns (ok, detail)."""
    sl = SymbolicLagrangian(geo, potential)
    dom = sl.dom
    E_chi = sl.euler_lagrange("chi")
    E_psi = sl.euler_lagrange("psi")
    t_chi, t_psi = sl.targets()
    V = sl.V
    d = {}
    d["psiDagger"] = polys_equal(E_chi, t_chi, dom)
    d["psi"] = polys_equal(E_psi, t_psi, dom)
    d["momentaClosedForms"] = sl.check_momenta()
    m_part = [e.coefficient_of(V.id("m")) for e in E_chi]
    Cpsi = np.einsum("ij,j->i", geo.gd.C, sl.psi) * (-val(geo.sqrtg))
    d["massTermInEquation"] = polys_equal(poly_array(m_part), Cpsi, dom) and any(not as_poly(x).is_zero(dom) for x in Cpsi)
    slashOm = np.einsum("mij,mjk->ik", geo.gam.value(), geo.Omega.value())
    om_term = np.einsum("ij,jk,k->i", geo.gd.C, slashOm, sl.psi)
    d["omegaTermNonzeroComponents"] = sum(1 for x in om_term if not as_poly(x).is_zero(dom))
    d["LTerms"] = sl.L0.nterms()
    return d["psiDagger"] and d["psi"] and d["momentaClosedForms"] and d["massTermInEquation"], d, sl


def poly_rename(p, mapping):
    out = Poly()
    for mono, coeff in p.t.items():
        out._acc(tuple(sorted(mapping.get(v, v) for v in mono)), coeff)
    return out


def species_map(V, source, target):
    return {V.id(source, a, alpha): V.id(target, a, alpha) for alpha in G.multi_indices(2) for a in range(16)}


def el_generic(L0, Ll, V, species):
    """Jet-identity Euler-Lagrange expressions (no special symbols) for one species."""
    p0 = L0.partials()
    pl = [p.partials() for p in Ll]
    E = []
    for a in range(16):
        e = p0.get(V.id(species, a, ()), Poly())
        for mu in range(8):
            q = V.id(species, a, (mu,))
            e = e - pl[mu].get(q, Poly()) - p0.get(q, Poly()).derivation(V.shift_image(mu))
        E.append(e)
    return poly_array(E)


# ---------------------------------------------------------------------------
# 6. Grassmann algebras (grassmann_algebra.py) for the side-by-side statements
# ---------------------------------------------------------------------------

def grassmann_right_el(L, js, species):
    """Right Euler-Lagrange expressions d_R L/d theta_a - d_mu (d_R L / d theta_{a;mu}) at the point."""
    res = []
    for a in range(js.nfield):
        E = L.value().right_derivative(js.idx(species, a))
        for mu in range(js.ncoord):
            g = js.idx(species, a, (mu,))
            Pi = L.map(lambda v, g=g: v.right_derivative(g))
            E = E - Pi.total_derivative_at_point(js, mu)
        res.append(E)
    return res


def gvec(js, species, alpha=()):
    return [Grassmann.gen(js.idx(species, a, alpha)) for a in range(js.nfield)]


def gmatvec(M, vec):
    """sum_j M[i][j] vec[j] for a coefficient matrix and a list of Grassmann elements."""
    out = []
    for i in range(len(M)):
        acc = Grassmann()
        for j in range(len(vec)):
            c = M[i][j]
            if c != 0:
                acc = acc + vec[j].scale(c)
        out.append(acc)
    return out


def gvecmat(vec, M):
    out = []
    for j in range(len(M[0])):
        acc = Grassmann()
        for i in range(len(vec)):
            c = M[i][j]
            if c != 0:
                acc = acc + vec[i].scale(c)
        out.append(acc)
    return out


def grassmann_L1_parts(geo, m, lam, js):
    """(L1) with complex Grassmann components as a JetGrassmann (coefficients with their order-1
    x-dependence at the point): generators psi_a, psis_a = Psi^*_a and first derivatives."""
    g1 = geo.truncated(1)
    C = geo.gd.C
    half = geo.dom.frac(1, 2)
    A = G.jmul(g1.sqrtg, G.jein("ij,mjk->mik", C, g1.gam))                           # sqrt|g| C gamma^mu
    anti = G.jein("mij,mjk->ik", g1.gam, g1.Omega) + G.jein("mij,mjk->ik", g1.Omega, g1.gam)
    K0 = G.jmul(g1.sqrtg, G.jein("ij,jk->ik", C, anti)).scale(half)                  # (1/2) sqrt|g| C {gamma, Omega}
    psi, psis = js.gens("psi"), js.gens("psis")
    S = bilinear(C, psis, psi)
    S2 = S * S
    parts = {}
    keys = [()] + [(l,) for l in range(8)]
    for key in keys:
        Ak = A.coeff(key)
        L = Grassmann()
        for mu in range(8):
            L = L + bilinear(Ak[mu], psis, js.gens("psi", (mu,))).scale(half)
            L = L - bilinear(Ak[mu], js.gens("psis", (mu,)), psi).scale(half)
        L = L + bilinear(K0.coeff(key), psis, psi)
        sgk = g1.sqrtg.coeff(key)[()]
        L = L - S.scale(m * sgk) - S2.scale(lam * half * sgk)
        parts[key] = L
    return JetGrassmann(parts), S


def grassmann_L1_targets(geo, m, lam, js, S):
    C = geo.gd.C
    sg0 = val(geo.sqrtg)
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    psi = gvec(js, "psi")
    psis = gvec(js, "psis")
    left = []
    Dpsi = [[gvec(js, "psi", (mu,))[c] + gmatvec(Om0[mu], psi)[c] for c in range(16)] for mu in range(8)]
    slash = [sum((gmatvec(gam0[mu], Dpsi[mu])[b] for mu in range(8)), Grassmann()) for b in range(16)]
    inner = [slash[b] - psi[b].scale(m) - (S * psi[b]).scale(lam) for b in range(16)]
    left = [x.scale(sg0) for x in gmatvec(C, inner)]
    pb = gvecmat(psis, C)
    dpb = [gvecmat(gvec(js, "psis", (mu,)), C) for mu in range(8)]
    Dpb = [[dpb[mu][b] - gvecmat(pb, Om0[mu])[b] for b in range(16)] for mu in range(8)]
    dg = [sum((gvecmat(Dpb[mu], gam0[mu])[b] for mu in range(8)), Grassmann()) for b in range(16)]
    right = [(dg[b] + pb[b].scale(m) + (S * pb[b]).scale(lam)).scale(-sg0) for b in range(16)]
    return left, right


def grassmann_flat_checks(gd, m, lam):
    """Flat (L1) with Grassmann components: L^* = L, the unsymmetrized kinetic term alone is not
    Hermitian, left EL w.r.t. Psi^* and right EL w.r.t. Psi."""
    js = JetSpace(["psi", "psis"], 16, 8, max_deriv=2)
    C = gd.C
    half = QQ(1, 2)
    psi, psis = js.gens("psi"), js.gens("psis")
    kin = Grassmann()
    kin_u = Grassmann()
    for mu in range(8):
        Cg = C.dot(gd.GAM[mu])
        kin = kin + bilinear(Cg, psis, js.gens("psi", (mu,))).scale(half) - bilinear(Cg, js.gens("psis", (mu,)), psi).scale(half)
        kin_u = kin_u + bilinear(Cg, psis, js.gens("psi", (mu,)))
    S = bilinear(C, psis, psi)
    L = kin - S.scale(m) - (S * S).scale(lam * half)
    conj = js.conj_map({"psi": "psis", "psis": "psi"})
    d = {}
    d["hermitian"] = (L.conjugate(conj) - L).is_zero()
    d["unsymmetrizedKineticNotHermitian"] = not (kin_u.conjugate(conj) - kin_u).is_zero()
    d["SHermitian"] = (S.conjugate(conj) - S).is_zero()
    Lj = JetGrassmann({(): L})
    E_left = euler_lagrange_all(Lj, js, "psis")
    E_right = grassmann_right_el(Lj, js, "psi")
    flat = G.Geometry(flat_vielbein_jet(G.make_qq_domain(), 1), gd, G.make_qq_domain(), "flat", sqrtg_sign=1,
                      curvature=False)
    t_left, t_right = grassmann_L1_targets(flat, m, lam, js, S)
    d["leftEL"] = all((E_left[a] - t_left[a]).is_zero() for a in range(16))
    d["rightEL"] = all((E_right[a] - t_right[a]).is_zero() for a in range(16))
    mass_el = [x.scale(-m) for x in gmatvec(C, gvec(js, "psi"))]
    d["massTermInEquation"] = all(not x.is_zero() for x in mass_el)
    d["LMonomials"] = L.nterms()
    return all(v for v in d.values() if isinstance(v, bool)), d


def grassmann_mass_term(gd, max_power=17):
    js = JetSpace(["psi", "psis"], 16, 8, max_deriv=0)
    S = bilinear(gd.C, js.gens("psis"), js.gens("psi"))
    conj = js.conj_map({"psi": "psis", "psis": "psi"})
    d = {"SMonomials": S.nterms(), "SHermitian": (S.conjugate(conj) - S).is_zero(), "SEven": S.is_even()}
    power = Grassmann.scalar(1)
    counts = []
    for k in range(1, max_power + 1):
        power = power * S
        counts.append(power.nterms())
    d["powerMonomialCounts"] = counts
    d["binomialCounts"] = counts[:16] == [math.comb(16, k) for k in range(1, min(16, max_power) + 1)][:len(counts[:16])]
    if max_power >= 17:
        d["S17Zero"] = counts[16] == 0
        d["S16Nonzero"] = counts[15] == 1
    d["S2Monomials"] = counts[1] if len(counts) > 1 else None
    d["S3Monomials"] = counts[2] if len(counts) > 2 else None
    ok = d["SMonomials"] == 16 and d["SHermitian"] and d["binomialCounts"] and d.get("S17Zero", True)
    return ok, d


def commuting_mass_term(alg):
    """Psibar Psi = Psi^dagger C Psi on explicit commuting spinors (Gaussian rationals)."""
    def e(k, re=1, im=0):
        v = [(Fraction(0), Fraction(0))] * 16
        v = list(v)
        v[k] = (Fraction(re), Fraction(im))
        return v

    def plus(u, v):
        return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(u, v)]
    Cc = cq_matrix(alg.C)
    cases = {"e0+e4": plus(e(0), e(4)), "e8+e12": plus(e(8), e(12)), "e0+ie4": plus(e(0), e(4, 0, 1))}
    out = {}
    for name, v in cases.items():
        s = cvec_dot(v, Cc, v)
        out[name] = {"S": qstr(s[0]), "imaginaryPart": qstr(s[1])}
    lam = sp.Symbol("x")
    cp = sp.factor(sp.Matrix(alg.C).charpoly(lam).as_expr())
    out["charPolyC"] = str(cp)
    out["signatureC"] = list(EX.symmetric_signature(alg.C))
    ok = (out["e0+e4"]["S"] == "-2" and out["e8+e12"]["S"] == "2" and out["e0+ie4"]["S"] == "0"
          and all(out[k]["imaginaryPart"] == "0" for k in cases) and out["signatureC"] == [8, 8, 0]
          and sp.expand(cp - (lam - 1) ** 8 * (lam + 1) ** 8) == 0)
    return ok, out


def flat_dispersion(alg):
    """(i gamma.k - m)(i gamma.k + m) = -(eta^{ab} k_a k_b + m^2) I; solution-space dimensions."""
    ks = sp.symbols("k0:8", real=True)
    msym = sp.Symbol("m", real=True)
    gk = sp.zeros(16, 16)
    for a in range(8):
        gk += ks[a] * alg.gam_sym[a]
    lhs = (sp.I * gk - msym * sp.eye(16)) * (sp.I * gk + msym * sp.eye(16))
    kk = sum(ETA[a] * ks[a] ** 2 for a in range(8))
    ident = sp.expand(lhs + (kk + msym ** 2) * sp.eye(16)) == sp.zeros(16, 16)

    def nullity(kvec, mval):
        re = EX.scale(-mval, EX.identity(16))
        im = EX.zeros(16)
        for a in range(8):
            im = EX.add(im, EX.scale(kvec[a], alg.gam[a]))
        return 16 - EX.crank((re, im))
    on = nullity([1, 1, 2, 3, 4, 0, 0, 0], 1)
    off = nullity([1, 1, 2, 3, 3, 0, 0, 0], 1)
    d = {"productIdentity": ident, "dimensionOnShell_m1_k11234": on, "dimensionOffShell_k4_3": off,
         "dispersion": "k4^2 + k5^2 + k6^2 + k7^2 - k0^2 - k1^2 - k2^2 - k3^2 = m^2 (Psi = u e^{i k.x})"}
    return ident and on == 8 and off == 0, d


def swap_symmetric(p, V, dom):
    """p(chi, psi) == p(psi, chi) (the polynomial reality criterion for real coefficients)."""
    mapping = species_map(V, "chi", "psi")
    mapping.update(species_map(V, "psi", "chi"))
    return (p - poly_rename(p, mapping)).is_zero(dom)


def complex_jet(rng, dom, order):
    X = G.random_spinor_jet(rng, dom, order)
    Y = G.random_spinor_jet(rng, dom, order)
    c = {}
    for k in X.c:
        c[k] = np.array([QQ_I(X.c[k][i], Y.c[k][i]) for i in range(16)], dtype=object)
    return G.TJet(order, c)


def conj_jet(J):
    return J.map(lambda a: np.array([QQ_I(z.x, -z.y) for z in np.asarray(a, dtype=object).ravel()],
                                    dtype=object).reshape(np.asarray(a).shape))


def re_part(z):
    return z.x if hasattr(z, "x") else z


def im_part(z):
    return z.y if hasattr(z, "y") else 0


def imag_zero(arr):
    return all(im_part(z) == 0 for z in np.asarray(arr, dtype=object).ravel())


def reality_point(geo, rng, full_complex=True):
    """Reality of (L1) for commuting components at one point: (i) swap symmetry of the symbolic
    polynomial L(chi, psi) (value and the 8 explicit first-derivative jets), (ii) Im L = 0 for
    Gaussian-rational jets Psi = X + i Y with Psi^dagger = conj(Psi) (value and first-derivative
    jets of L along the configuration), (iii) coefficient-level Hermiticity K0 = K0^T, L^mu = (K^mu)^T,
    K^mu = (1/2) sqrt|g| C gamma^mu, (iv) the unsymmetrized kinetic term alone is not real."""
    dom = geo.dom
    d = {}
    sl = SymbolicLagrangian(geo, "quartic")
    V = sl.V
    d["swapSymmetricValue"] = swap_symmetric(sl.L0, V, dom)
    d["swapSymmetricJets"] = all(swap_symmetric(p, V, dom) for p in sl.Ll)
    sn = SymbolicLagrangian(geo, "none", V=V)
    L0 = sn.L0
    C = geo.gd.C
    sg0 = val(geo.sqrtg)
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    half = dom.frac(1, 2)

    def coeff(i1, i2):
        return L0.t.get(tuple(sorted((i1, i2))), dom.zero)
    K0 = [[coeff(V.id("chi", a, ()), V.id("psi", b, ())) for b in range(16)] for a in range(16)]
    Kmu = [[[coeff(V.id("chi", a, ()), V.id("psi", b, (mu,))) for b in range(16)] for a in range(16)] for mu in range(8)]
    Lmu = [[[coeff(V.id("chi", a, (mu,)), V.id("psi", b, ())) for b in range(16)] for a in range(16)] for mu in range(8)]
    anti = np.einsum("mij,mjk->ik", gam0, Om0) + np.einsum("mij,mjk->ik", Om0, gam0)
    K0_expected = np.einsum("ij,jk->ik", C, anti) * (half * sg0)
    Kmu_expected = np.einsum("ij,mjk->mik", C, gam0) * (half * sg0)
    d["K0Hermitian"] = all(dom.is_zero(K0[a][b] - K0[b][a]) for a in range(16) for b in range(16))
    d["K0ClosedForm"] = all(dom.is_zero(K0[a][b] - K0_expected[a, b]) for a in range(16) for b in range(16))
    d["KmuClosedForm"] = all(dom.is_zero(Kmu[mu][a][b] - Kmu_expected[mu, a, b])
                             for mu in range(8) for a in range(16) for b in range(16))
    d["LmuEqualsKmuDagger"] = all(dom.is_zero(Lmu[mu][a][b] - Kmu[mu][b][a])
                                  for mu in range(8) for a in range(16) for b in range(16))
    d["KmuAntisymmetric"] = all(dom.is_zero(Kmu[mu][a][b] + Kmu[mu][b][a])
                                for mu in range(8) for a in range(16) for b in range(16))
    # unsymmetrized kinetic term chi^T C gamma^mu D_mu psi is not swap symmetric (not real)
    Dpsi0 = sl.dpsi + np.einsum("mij,j->mi", Om0, sl.psi)
    unsym = as_poly(np.einsum("j,mjk,mk->", sl.pb, gam0, Dpsi0))
    d["unsymmetrizedKineticNotReal"] = not swap_symmetric(unsym, V, dom)
    if full_complex and dom.K == QQ:
        psi = complex_jet(rng, dom, 2)
        pb = G.jein("...i,ij->...j", conj_jet(psi), C)
        parts = G.lagrangian_scalar(geo, pb, pb.grad(), psi, psi.grad(), dom.frac(3, 7), dom.frac(5, 11))
        L = G.jmul(geo.sqrtg, parts["Ls"])
        d["complexDataImLZeroValueAndJets"] = all(imag_zero(L.coeff(k)) for k in [()] + [(l,) for l in range(8)])
        d["complexDataLNonzero"] = any(re_part(z) != 0 for z in np.asarray(L.value(), dtype=object).ravel())
        t1 = G.jein("...mj,...mj->...", G.jein("...i,mij->...mj", pb, geo.gam), parts["Dpsi"])
        d["complexDataUnsymmetrizedImNonzero"] = not imag_zero(t1.value())
    return all(v for v in d.values() if isinstance(v, bool)), d


def grassmann_curved_L1(geo, m, lam):
    """(L1) with complex Grassmann components at a curved point (coefficients carry their x-jets):
    L^* = L for every part; left EL w.r.t. Psi^* and right EL w.r.t. Psi equal the covariant
    field equations (the same form as for commuting components)."""
    js = JetSpace(["psi", "psis"], 16, 8, max_deriv=2)
    Lj, S = grassmann_L1_parts(geo, m, lam, js)
    conj = js.conj_map({"psi": "psis", "psis": "psi"})
    d = {"hermitianAllParts": all((v.conjugate(conj) - v).is_zero() for v in Lj.parts.values())}
    E_left = euler_lagrange_all(Lj, js, "psis")
    E_right = grassmann_right_el(Lj, js, "psi")
    t_left, t_right = grassmann_L1_targets(geo, m, lam, js, S)
    d["leftEL"] = all((E_left[a] - t_left[a]).is_zero() for a in range(16))
    d["rightEL"] = all((E_right[a] - t_right[a]).is_zero() for a in range(16))
    d["valueMonomials"] = Lj.value().nterms()
    return all(v for v in d.values() if isinstance(v, bool)), d


def grassmann_real_lg(geo, HM, notebook=False):
    """Notebook-type Lg = sqrt|g|[r^T C gamma^mu D_mu r + HM r^T C r] for a REAL Grassmann 16-vector r
    at a curved point: EL expressions (left derivatives) and the mass term."""
    js = JetSpace(["r"], 16, 8, max_deriv=2)
    g1 = geo.truncated(1)
    C = geo.gd.C
    Om = g1.Omega_nb if notebook else g1.Omega
    A = G.jmul(g1.sqrtg, G.jein("ij,mjk->mik", C, g1.gam))
    N = G.jmul(g1.sqrtg, G.jein("ij,jl->il", C, G.jein("mjk,mkl->jl", g1.gam, Om)))
    r = js.gens("r")
    mass = bilinear(C, r, r)
    parts = {}
    for key in [()] + [(l,) for l in range(8)]:
        L = Grassmann()
        Ak = A.coeff(key)
        for mu in range(8):
            L = L + bilinear(Ak[mu], r, js.gens("r", (mu,)))
        L = L + bilinear(N.coeff(key), r, r) + mass.scale(HM * g1.sqrtg.coeff(key)[()])
        parts[key] = L
    Lj = JetGrassmann(parts)
    E = euler_lagrange_all(Lj, js, "r")
    first_derivative_generators = {js.idx("r", a, (mu,)) for a in range(16) for mu in range(8)}
    d = {"massTermZero": mass.is_zero(), "ELzero": all(e.is_zero() for e in E),
         "ELderivativeFree": all(not (e.generators() & first_derivative_generators) for e in E),
         "LgMonomials": Lj.value().nterms(), "LgNonzero": Lj.value().nterms() > 0}
    return d


def grassmann_real_flat(gd):
    """Flat real Grassmann Psi: Psi^T C Psi = 0, Psi^T C gamma^a d_mu Psi = (1/2) d_mu(Psi^T C gamma^a Psi)."""
    js = JetSpace(["r"], 16, 8, max_deriv=2)
    r = js.gens("r")
    d = {"massTermZero": bilinear(gd.C, r, r).is_zero()}
    counts = []
    ok_div = True
    L = Grassmann()
    for a in range(8):
        Cg = gd.C.dot(gd.GAM[a])
        q = bilinear(Cg, r, r)
        counts.append(q.nterms())
        for mu in range(8):
            lhs = bilinear(Cg, r, js.gens("r", (mu,)))
            ok_div = ok_div and (lhs - js.total_derivative(q, mu).scale(QQ(1, 2))).is_zero()
        L = L + bilinear(Cg, r, js.gens("r", (a,)))
    L = L + bilinear(gd.C, r, r).scale(QQ(2, 3))
    E = euler_lagrange_all(JetGrassmann({(): L}), js, "r")
    d["vectorBilinearMonomials"] = counts
    d["kineticIsHalfTotalDerivative"] = ok_div
    d["flatLgELzero"] = all(e.is_zero() for e in E)
    d["flatLgNonzero"] = L.nterms() > 0
    ok = d["massTermZero"] and ok_div and d["flatLgELzero"] and d["flatLgNonzero"] and all(c > 0 for c in counts)
    return ok, d


def grassmann_complex_decomposition(gd):
    """Grassmann Psi = rho + i iota (rho, iota real): Psibar Psi = 2 i rho^T C iota (pure cross term)."""
    rho = list(range(16))
    iota = list(range(16, 32))
    one = GaussianRational(QQ(1), QQ(0))
    i_unit = GaussianRational(QQ(0), QQ(1))
    psi = [Grassmann({(rho[a],): one, (iota[a],): i_unit}) for a in range(16)]
    psis = [p.conjugate(lambda g: g) for p in psi]
    S = Grassmann()
    for a in range(16):
        for b in range(16):
            c = gd.C[a, b]
            if c != 0:
                S = S + (psis[a] * psi[b]).scale(GaussianRational(c, QQ(0)))
    target = bilinear(gd.C, rho, iota).scale(GaussianRational(QQ(0), QQ(2)))
    d = {"crossTermOnly": (S - target).is_zero(),
         "diagonalTermsVanish": bilinear(gd.C, rho, rho).is_zero() and bilinear(gd.C, iota, iota).is_zero()}
    return d["crossTermOnly"] and d["diagonalTermsVanish"], d


def notebook_lg_symbolic(geo, V, species, mass_coefficient, notebook=False):
    """Lg[X] = sqrt|g| [X^T C gamma^mu D_mu X + mass_coefficient X^T C X] (commuting, symbolic X jets)."""
    g1 = geo.truncated(1)
    C = geo.gd.C
    Xv = V.vector(species)
    dX = V.gradient(species)
    Om = g1.Omega_nb if notebook else g1.Omega
    D = const_jet(dX) + G.jein("mij,...j->...mi", Om, const_jet(Xv))
    row = np.einsum("i,ij->j", Xv, C)
    kin = G.jein("...mj,...mj->...", G.jein("...i,mij->...mj", const_jet(row), g1.gam), D)
    mass = const_jet(obj0(as_poly(np.dot(row, Xv)) * mass_coefficient))
    L = G.jmul(g1.sqrtg, kin + mass)
    return L, as_poly(np.dot(row, Xv))


def real_restriction_point(geo, notebook):
    """EL of the notebook-type Lagrangian for real commuting X (canonical or notebook contraction)."""
    dom = geo.dom
    V = JetVars(species=("X",))
    HM = V.v("HM")
    L, SX = notebook_lg_symbolic(geo, V, "X", HM, notebook=notebook)
    L0 = as_poly(val(L))
    Ll = [as_poly(L.coeff((l,))[()]) for l in range(8)]
    E = el_generic(L0, Ll, V, "X")
    C = geo.gd.C
    sg0 = val(geo.sqrtg)
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    Xv = V.vector("X")
    DX = V.gradient("X") + np.einsum("mij,j->mi", Om0, Xv)
    canonical = np.einsum("ij,j->i", C, np.einsum("mij,mj->i", gam0, DX) + Xv * HM) * (2 * sg0)
    delta = geo.Omega_nb.value() - Om0
    anti = np.einsum("mij,mjk->ik", gam0, delta) + np.einsum("mij,mjk->ik", delta, gam0)
    extra_matrix = np.einsum("ij,jk->ik", C, anti) * sg0
    extra = np.einsum("ij,j->i", extra_matrix, Xv)
    target = canonical + extra if notebook else canonical
    d = {"EL": polys_equal(E, target, dom)}
    mass_part = poly_array([e.coefficient_of(V.id("HM")) for e in E])
    d["massPartIs2sqrtgCX"] = polys_equal(mass_part, np.einsum("ij,j->i", C, Xv) * (2 * sg0), dom)
    d4 = np.empty((16, 16), dtype=object)
    for a in range(16):
        for b in range(16):
            d4[a, b] = E[a].t.get((V.id("X", b, (TIME,)),), dom.zero)
    det = G.mat_det(d4, dom)
    d["kineticNotDivergence"] = not dom.is_zero(det) and all(
        dom.is_zero(d4[a, b] - 2 * sg0 * np.dot(C[a], gam0[TIME][:, b])) for a in range(16) for b in range(16))
    d["notebookExtraTermNonzero"] = not all(dom.is_zero(x) for x in extra_matrix.ravel())
    d["Lnonzero"] = L0.nterms() > 0
    ok = d["EL"] and d["massPartIs2sqrtgCX"] and d["kineticNotDivergence"] and d["Lnonzero"]
    return ok, d


def relation_to_L1(geo):
    """(L1) at Psi = X + i Y equals sqrt|g|[K_R[X] + K_R[Y] - m(S_X + S_Y) - U(S_X + S_Y)] (U = lam S^2/2);
    Y = 0 is a consistent truncation and the X equation is 2 sqrt|g| C (gamma D X - (m + lam S_X) X)."""
    dom = geo.dom
    V = JetVars(species=("chi", "psi", "X", "Y"))
    sn = SymbolicLagrangian(geo, "none", V=V)
    m = V.v("m")
    lam = V.v("lam")
    half = dom.frac(1, 2)
    to_xx = species_map(V, "chi", "X")
    to_xx.update(species_map(V, "psi", "X"))
    to_yy = species_map(V, "chi", "Y")
    to_yy.update(species_map(V, "psi", "Y"))
    to_xy = species_map(V, "chi", "X")
    to_xy.update(species_map(V, "psi", "Y"))
    to_yx = species_map(V, "chi", "Y")
    to_yx.update(species_map(V, "psi", "X"))
    LgX, SX = notebook_lg_symbolic(geo, V, "X", -m)
    LgY, SY = notebook_lg_symbolic(geo, V, "Y", -m)
    keys = [()] + [(l,) for l in range(8)]
    d = {"decomposition": True, "imaginaryPartZero": True}
    for k in keys:
        lb = as_poly(sn.L.coeff(k)[()])
        re = poly_rename(lb, to_xx) + poly_rename(lb, to_yy)
        im = poly_rename(lb, to_xy) - poly_rename(lb, to_yx)
        d["decomposition"] = d["decomposition"] and (re - as_poly(LgX.coeff(k)[()]) - as_poly(LgY.coeff(k)[()])).is_zero(dom)
        d["imaginaryPartZero"] = d["imaginaryPartZero"] and im.is_zero(dom)
    Ssum = SX + SY
    U = const_jet(obj0(Ssum * Ssum * lam * half))
    Lreal = LgX + LgY - G.jmul(geo.truncated(1).sqrtg, U)
    L0 = as_poly(val(Lreal))
    Ll = [as_poly(Lreal.coeff((l,))[()]) for l in range(8)]
    Yvars = [V.id("Y", a, alpha) for alpha in G.multi_indices(2) for a in range(16)]
    EY = el_generic(L0, Ll, V, "Y")
    d["consistentTruncation"] = all(e.drop_vars(Yvars).is_zero(dom) for e in EY)
    EXq = el_generic(L0, Ll, V, "X")
    C = geo.gd.C
    sg0 = val(geo.sqrtg)
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    Xv = V.vector("X")
    DX = V.gradient("X") + np.einsum("mij,j->mi", Om0, Xv)
    target = np.einsum("ij,j->i", C, np.einsum("mij,mj->i", gam0, DX) - Xv * (m + lam * SX)) * (2 * sg0)
    d["realEquation"] = polys_equal(poly_array([e.drop_vars(Yvars) for e in EXq]), target, dom)
    return all(d.values()), d


# ---------------------------------------------------------------------------
# 7. coupling to the spin connection and to gravity
# ---------------------------------------------------------------------------

def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def connection_point(geo, rng, is_g2=False):
    dom = geo.dom
    d = {}
    gam0 = geo.gam.value()
    Om0 = geo.Omega.value()
    slash = np.einsum("mij,mjk->ik", gam0, Om0)
    d["gammaOmegaNonzeroEntries"] = G.count_nonzero(slash, dom)
    if is_g2:
        d["gammaOmegaEquals3Hgamma0"] = G.arr_is_zero(slash - geo.gd.GAM[0] * (3 * dom.conv(G.G2_H)), dom)
    d["divergenceIdentity"] = G.jet_is_zero(geo.divergence_identity_defect(max_order=0), dom)
    d["gammaCovariantlyConstant"] = G.jet_is_zero(geo.gamma_covariant_derivative(max_order=0), dom)
    half = dom.frac(1, 2)
    F_expected = np.einsum("abmn,abij->mnij", geo.Rframe_low, geo.gd.S) * half
    d["spinCurvatureIsHalfRiemannS"] = G.arr_is_zero(geo.Fspin - F_expected, dom)
    d["spinCurvatureNonzero"] = not G.arr_is_zero(geo.Fspin, dom)
    # Lichnerowicz: (gamma D)^2 psi - Box psi = c R psi
    psi = G.random_spinor_jet(rng, dom, 2)
    Dirac = G.dirac_operator(geo, psi)
    DD = G.dirac_operator(geo, Dirac).value()
    box = G.box_psi(geo, psi)
    delta = DD - box
    R = geo.Rscalar
    cs = set()
    ok_l = True
    for a in range(16):
        rp = R * psi.value()[a]
        if dom.is_zero(rp):
            ok_l = ok_l and dom.is_zero(delta[a])
        else:
            cs.add(dom.to_str(delta[a] / rp))
    d["lichnerowiczC"] = sorted(cs)
    d["lichnerowicz"] = ok_l and sorted(cs) == ["-1/4"]
    d["scalarCurvature"] = exact_summary(dom, R)
    # on shell (U = 0, second order): (gamma D)^2 psi = m^2 psi and Box psi - (R/4) psi = m^2 psi
    m = dom.frac(3, 7)
    chi = G.random_spinor_jet(rng, dom, 2)
    psi_on, _ = G.solve_onshell(geo, G.random_spinor_jet(rng, dom, 2), chi, m, 0, max_order=2)
    E1 = G.dirac_operator(geo, psi_on)
    d["onShellFirstOrder"] = G.jet_is_zero(E1 - G.jmul(G.TJet.const(m), psi_on.truncate(E1.order)), dom, max_order=1)
    DD_on = G.dirac_operator(geo, E1).value()
    d["onShellSecondOrder"] = G.arr_is_zero(DD_on - psi_on.value() * (m * m), dom)
    box_on = G.box_psi(geo, psi_on)
    d["onShellLichnerowiczMassShell"] = G.arr_is_zero(box_on - psi_on.value() * (R * dom.frac(1, 4)) - psi_on.value() * (m * m), dom)
    # only the totally antisymmetric part omega_[cab] enters the symmetrized kinetic term
    om_frame = np.einsum("cm,mab->cab", geo.einv.value(), geo.omega_low.value())
    alt = np.empty((8, 8, 8), dtype=object)
    perms = list(itertools.permutations(range(3)))
    for c in range(8):
        for a in range(8):
            for b in range(8):
                idx = (c, a, b)
                total = dom.zero
                for p in perms:
                    total = total + om_frame[idx[p[0]], idx[p[1]], idx[p[2]]] * perm_sign(p)
                alt[c, a, b] = total * dom.frac(1, 6)
    GAM = geo.gd.GAM
    rhs = np.zeros((16, 16), dtype=object)
    for c in range(8):
        for a in range(8):
            for b in range(8):
                if len({c, a, b}) == 3 and not dom.is_zero(alt[c, a, b]):
                    rhs = rhs + GAM[c].dot(GAM[a]).dot(GAM[b]) * (alt[c, a, b] * half)
    anti = np.einsum("mij,mjk->ik", gam0, Om0) + np.einsum("mij,mjk->ik", Om0, gam0)
    d["onlyTotallyAntisymmetricOmega"] = G.arr_is_zero(anti - rhs, dom)
    d["anticommutatorTermNonzero"] = not G.arr_is_zero(anti, dom)
    d["totallyAntisymmetricOmegaNonzero"] = not G.arr_is_zero(alt, dom)
    # the Omega term of the field equation
    om_term = slash.dot(psi.value())
    d["omegaTermNonzeroComponents"] = G.count_nonzero(om_term, dom)
    return d


def run_connection(geos, rec, quick):
    rng = random.Random(60000)
    labels = ["p1"] if quick else ["p1", "p2", "p3"]
    res = {}
    for lab in labels:
        res["G1" + lab] = connection_point(geos.g1(lab), rng)
    res["G2"] = connection_point(geos.g2(), rng, is_g2=True)
    ok = True
    for key, d in res.items():
        base = (d["divergenceIdentity"] and d["gammaCovariantlyConstant"] and d["spinCurvatureIsHalfRiemannS"]
                and d["spinCurvatureNonzero"] and d["lichnerowicz"] and d["onShellFirstOrder"] and d["onShellSecondOrder"]
                and d["onShellLichnerowiczMassShell"] and d["onlyTotallyAntisymmetricOmega"] and d["gammaOmegaNonzeroEntries"] > 0)
        if key == "G2":
            base = base and d["gammaOmegaEquals3Hgamma0"] and not d["anticommutatorTermNonzero"]
        else:
            base = base and d["anticommutatorTermNonzero"] and d["totallyAntisymmetricOmegaNonzero"]
        ok = ok and base
    rec.check("connection_nonTrivialCoupling", ok, res)
    rec.check("connection_OmegaTermInFieldEquation", all(d["omegaTermNonzeroComponents"] == 16 for d in res.values()),
              {k: d["omegaTermNonzeroComponents"] for k, d in res.items()})
    return res


# ---------------------------------------------------------------------------
# 8. family runners: lagrangian, realRestriction, EL
# ---------------------------------------------------------------------------

def run_lagrangian(alg, geos, rec, quick):
    rng = random.Random(51000)
    real = {"flat": reality_point(geos.flat(), rng)[1], "G1p1": reality_point(geos.g1("p1"), rng)[1],
            "G2": reality_point(geos.g2(), rng)[1]}
    if not quick:
        for lab in ("p2", "p3"):
            real["G1" + lab] = reality_point(geos.g1(lab), rng)[1]
    ok_real = all(all(v for k, v in d.items() if isinstance(v, bool)) for d in real.values())
    rec.check("lagrangian_realCommuting", ok_real, real)
    herm_keys = ("K0Hermitian", "K0ClosedForm", "KmuClosedForm", "LmuEqualsKmuDagger", "KmuAntisymmetric")
    rec.check("lagrangian_coefficientHermiticity", all(all(d[k] for k in herm_keys) for d in real.values()),
              {"statement": "Ls = chi^T K0 psi + chi^T K^mu d_mu psi + d_mu chi^T L^mu psi - m S - U with "
                            "K0 = (1/2) sqrt|g| C {gamma^mu, Omega_mu} real symmetric (Hermitian), K^mu = "
                            "(1/2) sqrt|g| C gamma^mu real antisymmetric and L^mu = (K^mu)^T = (K^mu)^dagger "
                            "(coefficients read off the symbolic polynomial L); because complex conjugation "
                            "reverses products (trivially for commuting numbers, by (theta1 theta2)^* = "
                            "theta2^* theta1^* for Grassmann numbers) this makes L real/Hermitian for both "
                            "statistics.",
               "points": sorted(real)})
    ok_g, dg = grassmann_flat_checks(geos.gd_qq, QQ(3, 7), QQ(5, 11))
    rec.check("lagrangian_grassmannFlatHermitianAndEL", ok_g, dg)
    ok_c, dc = commuting_mass_term(alg)
    rec.check("massTerm_commutingExplicitSpinors", ok_c, dc)
    ok_m, dm = grassmann_mass_term(geos.gd_qq, 4 if quick else 17)
    rec.check("massTerm_grassmannNonzero", ok_m, dm)
    ok_d, dd = flat_dispersion(alg)
    rec.check("massTerm_dispersionFlat", ok_d, dd)


def run_real_restriction(geos, rec, quick):
    res = {}
    points = [("flat", geos.flat()), ("G1p1", geos.g1("p1")), ("G2", geos.g2())]
    if not quick:
        points += [("G1p2", geos.g1("p2")), ("G1p3", geos.g1("p3"))]
    ok = True
    for name, geo in points:
        r = {"canonical": real_restriction_point(geo, False)[1]}
        if name != "flat":
            r["notebookContraction"] = real_restriction_point(geo, True)[1]
        res[name] = r
        for key, d in r.items():
            ok = ok and d["EL"] and d["massPartIs2sqrtgCX"] and d["kineticNotDivergence"] and d["Lnonzero"]
        if name.startswith("G1"):
            ok = ok and r["notebookContraction"]["notebookExtraTermNonzero"]
        if name == "G2":
            ok = ok and not r["notebookContraction"]["notebookExtraTermNonzero"]
    rec.check("realRestriction_commutingNonTrivial", ok, res)
    ok_f, df = grassmann_real_flat(geos.gd_qq)
    rec.check("realRestriction_grassmannFlatTrivial", ok_f, df)
    g1 = geos.g1("p1")
    dcan = grassmann_real_lg(g1, QQ(2, 3))
    dnb = grassmann_real_lg(g1, QQ(2, 3), notebook=True)
    rec.check("realRestriction_grassmannCurvedTrivial",
              dcan["massTermZero"] and dcan["ELzero"] and dcan["LgNonzero"] and dnb["ELderivativeFree"],
              {"point": "G1p1", "HM": "2/3", "canonical": dcan, "notebookContraction": dnb})
    ok_x, dx = grassmann_complex_decomposition(geos.gd_qq)
    rec.check("realRestriction_grassmannComplexDecomposition", ok_x, dx)
    rel = {"flat": relation_to_L1(geos.flat())[1], "G1p1": relation_to_L1(g1)[1]}
    if not quick:
        rel["G2"] = relation_to_L1(geos.g2())[1]
    rec.check("realRestriction_relationToL1", all(all(d.values()) for d in rel.values()), rel)


def run_el(geos, rec, quick):
    res = {}
    ok_flat_q, d = el_symbolic_point(geos.flat(), "quartic")[:2]
    ok_flat_u, du = el_symbolic_point(geos.flat(), "general")[:2]
    rec.check("EL_commutingFlat", ok_flat_q and ok_flat_u, {"quartic": d, "generalU": du})
    points = [("G1p1", geos.g1("p1")), ("G2", geos.g2())]
    if not quick:
        points += [("G1p2", geos.g1("p2")), ("G1p3", geos.g1("p3"))]
    ok = True
    for name, geo in points:
        okp, dp = el_symbolic_point(geo, "quartic")[:2]
        res[name] = dp
        ok = ok and okp and dp["omegaTermNonzeroComponents"] == 16
    rec.check("EL_commutingCurved", ok, res)
    gen = {}
    ok_g = True
    for name, geo in points[:2]:
        okp, dp = el_symbolic_point(geo, "general")[:2]
        gen[name] = dp
        ok_g = ok_g and okp
    rec.check("EL_commutingGeneralSmoothU", ok_g, gen)
    ok_gc, dgc = grassmann_curved_L1(geos.g1("p1"), QQ(3, 7), QQ(5, 11))
    rec.check("EL_grassmannCurved", ok_gc, {"point": "G1p1", "m": "3/7", "lambda": "5/11", **dgc})
    ok_gf = grassmann_flat_checks(geos.gd_qq, QQ(3, 7), QQ(5, 11))[0]
    rec.check("EL_identicalFormBothStatistics", ok and ok_gc and ok_flat_q and ok_gf,
              {"statement": "commuting components (symbolic jets, flat, G1 and G2) and Grassmann components (exact "
                            "Grassmann algebra, flat and G1 p1 with left derivatives for Psi^* and right derivatives "
                            "for Psi) give the same field equations gamma^mu D_mu Psi = (m + U'(S)) Psi, "
                            "(D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar."})


# ---------------------------------------------------------------------------
# 9. energy-momentum tensor, current, observer splits (commuting components)
# ---------------------------------------------------------------------------

def emt_general(geo, psi, chi, m, U_of_S):
    """T_{mu nu} of CONTRACT section 7 with a general potential: U_of_S(S jet) -> U jet.
    Returns the Stage-1 pieces plus T (all indices down)."""
    pb = G.psibar_from_chi(geo, chi)
    parts = lag_parts(geo, pb, pb.grad(), psi, psi.grad())
    S = parts["S"]
    Ls = parts["kin"] - S.scale(m) - U_of_S(S)
    T = G.emt_covariant(geo, pb, parts["Dpb"], psi, parts["Dpsi"], Ls)
    parts.update({"pb": pb, "Ls": Ls, "T": T})
    return parts


def quartic_U(lam, dom):
    half = dom.frac(1, 2)
    return lambda S: G.jmul(S, S).scale(lam * half)


def general_U(V):
    """U(S(x)) = U0 + U1 (S(x) - S0) + (U2/2)(S(x) - S0)^2 truncated (the jets used are of order <= 1)."""
    def U(S):
        dS = S - G.TJet.const(S.value())
        return G.TJet.const(obj0(V.v("U0"))) + dS.map(lambda v: np.asarray(v, dtype=object) * V.v("U1"))
    return U


def general_Uprime(V):
    def Up(S):
        dS = S - G.TJet.const(S.value())
        return G.TJet.const(obj0(V.v("U1"))) + dS.map(lambda v: np.asarray(v, dtype=object) * V.v("U2"))
    return Up


def field_equations_general(geo, psi, chi, m, Uprime_of_S):
    pb = G.psibar_from_chi(geo, chi)
    parts = lag_parts(geo, pb, pb.grad(), psi, psi.grad())
    mU = Uprime_of_S(parts["S"]) + G.TJet.const(m)
    E = G.jein("mij,mj->i", geo.gam, parts["Dpsi"]) - G.jmul(mU, psi)
    Ebar = G.jein("mi,mij->j", parts["Dpb"], geo.gam) + G.jmul(mU, pb)
    return E, Ebar


def solve_onshell_general(geo, psi, chi, m, Uprime_of_S, max_order=2):
    """Own on-shell jet solver for a general U'(S): replaces the d_4-containing Taylor coefficients so
    that the field equations (and their first derivatives for max_order = 2) hold at the point."""
    dom = geo.dom
    C = geo.gd.C
    psi = G.TJet(psi.order, {k: v.copy() for k, v in psi.c.items()})
    chi = G.TJet(chi.order, {k: v.copy() for k, v in chi.c.items()})
    G4 = geo.gam.value()[TIME]
    G4i = G.mat_inv(G4, dom)
    half = dom.frac(1, 2)

    def correct(key, r, rb, factor):
        psi.c[key] = np.asarray(psi.c[key] - G4i.dot(r) * factor, dtype=object)
        chi.c[key] = np.asarray(chi.c[key] - (rb.dot(G4i)).dot(C) * factor, dtype=object)

    E, Eb = field_equations_general(geo, psi, chi, m, Uprime_of_S)
    correct((TIME,), E.value(), Eb.value(), dom.one)
    if max_order >= 2:
        E, Eb = field_equations_general(geo, psi, chi, m, Uprime_of_S)
        for nu in range(8):
            if nu != TIME:
                correct(tuple(sorted((nu, TIME))), E.coeff((nu,)), Eb.coeff((nu,)), dom.one)
        E, Eb = field_equations_general(geo, psi, chi, m, Uprime_of_S)
        correct((TIME, TIME), E.coeff((TIME,)), Eb.coeff((TIME,)), half)
    E, Eb = field_equations_general(geo, psi, chi, m, Uprime_of_S)
    order = 1 if max_order >= 2 else 0
    ok = all(G.arr_is_zero(np.vectorize(lambda x: 0 if as_poly(x).is_zero(dom) else 1, otypes=[object])(J.coeff(k)), dom)
             for J in (E, Eb) for k in [()] + ([(l,) for l in range(8)] if order else []))
    return psi, chi, ok


def current_divergence(geo, pb, psi):
    """sum_mu d_mu (sqrt|g| Psibar gamma^mu Psi) at the point."""
    j = G.jein("mj,j->m", G.jein("i,mij->mj", pb, geo.gam), psi)
    sj = G.jmul(geo.sqrtg.truncate(j.order), j)
    total = 0
    for mu in range(8):
        total = total + sj.d(mu).value()[mu]
    return total


def trace_value(geo, T):
    return np.einsum("mn,mn->", geo.ginv.value(), T.value())


def emt_point(geo, rng, m, lam, complex_data=True):
    dom = geo.dom
    d = {}
    # off shell
    psi = G.random_spinor_jet(rng, dom, 2)
    chi = G.random_spinor_jet(rng, dom, 2)
    off = emt_general(geo, psi, chi, m, quartic_U(lam, dom))
    T0 = off["T"].value()
    d["symmetricOffShell"] = G.arr_is_zero(T0 - T0.T, dom)
    swapped = emt_general(geo, chi, psi, m, quartic_U(lam, dom))
    d["swapSymmetricOffShell"] = G.jet_is_zero(off["T"] - swapped["T"], dom, max_order=1)
    d["divergenceNonzeroOffShell"] = not G.arr_is_zero(G.emt_divergence(geo, off["T"]), dom)
    d["currentDivergenceNonzeroOffShell"] = not dom.is_zero(current_divergence(geo, off["pb"], psi))
    # on shell (Stage-1 solver, second order)
    psi_on, chi_on = G.solve_onshell(geo, G.random_spinor_jet(rng, dom, 2), G.random_spinor_jet(rng, dom, 2), m, lam, max_order=2)
    E, Eb, _ = G.field_equations(geo, psi_on, chi_on, m, lam)
    d["onShellJetsSolved"] = G.jet_is_zero(E, dom, max_order=1) and G.jet_is_zero(Eb, dom, max_order=1)
    on = emt_general(geo, psi_on, chi_on, m, quartic_U(lam, dom))
    d["conservationOnShell"] = G.arr_is_zero(G.emt_divergence(geo, on["T"]), dom)
    S0 = val(on["S"])
    tr = trace_value(geo, on["T"])
    d["traceOnShell"] = dom.is_zero(tr - (-m * S0 + 7 * S0 * lam * S0 - 8 * lam * S0 * S0 * dom.frac(1, 2))) and not dom.is_zero(S0)
    d["traceOnShellValue"] = exact_summary(dom, tr)
    d["onShellLagrangianIsSUprimeMinusU"] = dom.is_zero(val(on["Ls"]) - (lam * S0 * S0 - lam * S0 * S0 * dom.frac(1, 2)))
    d["currentConservedOnShell"] = dom.is_zero(current_divergence(geo, on["pb"], psi_on))
    if complex_data and dom.K == QQ:
        cpsi = complex_jet(rng, dom, 2)
        cpb = G.jein("...i,ij->...j", conj_jet(cpsi), geo.gd.C)
        parts = lag_parts(geo, cpb, cpb.grad(), cpsi, cpsi.grad())
        Ls = parts["kin"] - parts["S"].scale(m) - G.jmul(parts["S"], parts["S"]).scale(lam * dom.frac(1, 2))
        Tc = G.emt_covariant(geo, cpb, parts["Dpb"], cpsi, parts["Dpsi"], Ls).value()
        d["realForConjugateData"] = imag_zero(Tc) and any(re_part(z) != 0 for z in Tc.ravel())
        jv = np.einsum("i,mij,j->m", cpb.value(), geo.gam.value(), cpsi.value())
        d["currentjImaginary"] = all(re_part(z) == 0 for z in jv) and any(im_part(z) != 0 for z in jv)
    # observer split in Gaussian normal time
    g0 = geo.g.value()
    gauss = dom.is_zero(g0[TIME, TIME] + 1) and all(dom.is_zero(g0[TIME, i]) for i in range(8) if i != TIME)
    d["gaussianNormal"] = gauss
    if gauss:
        gam4 = geo.gam.value()[TIME]
        pb0 = off["pb"].value()
        K4 = (pb0.dot(gam4).dot(off["Dpsi"].value()[TIME]) - off["Dpb"].value()[TIME].dot(gam4).dot(psi.value())) * dom.frac(1, 2)
        K = val(off["kin"])
        S_off = val(off["S"])
        rho = T0[TIME, TIME]
        KEH = -(K - K4)
        PEH = m * S_off + lam * S_off * S_off * dom.frac(1, 2)
        d["rhoEqualsKEHplusPEH_offShell"] = dom.is_zero(rho - KEH - PEH)
        d["rhoEqualsK4minusLs_offShell"] = dom.is_zero(rho - (K4 - val(off["Ls"])))
    return d


def emt_general_U_point(geo, rng, m):
    """Conservation, trace -m S + 7 S U' - 8 U and current conservation for a GENERAL smooth U:
    U(S0), U'(S0), U''(S0) are independent symbols (exact polynomials)."""
    dom = geo.dom
    V = JetVars(species=())
    psi0 = G.random_spinor_jet(rng, dom, 2)
    chi0 = G.random_spinor_jet(rng, dom, 2)
    psi, chi, ok = solve_onshell_general(geo, psi0, chi0, m, general_Uprime(V))
    d = {"onShellSolved": ok}
    parts = emt_general(geo, psi, chi, m, general_U(V))
    div = G.emt_divergence(geo, parts["T"])
    d["conservation"] = all(as_poly(x).is_zero(dom) for x in np.asarray(div, dtype=object).ravel())
    S0 = as_poly(val(parts["S"]))
    tr = as_poly(trace_value(geo, parts["T"]))
    d["trace"] = (tr - (-(S0 * m) + S0 * V.v("U1") * 7 - V.v("U0") * 8)).is_zero(dom)
    d["currentConserved"] = as_poly(current_divergence(geo, parts["pb"], psi)).is_zero(dom)
    # the solver reproduces the Stage-1 solver for U = (lam/2) S^2 (U1 = lam S0, U2 = lam, U0 = lam S0^2/2)
    lam = dom.frac(5, 11)
    s0 = np.dot(G.psibar_from_chi(geo, chi0).value(), psi0.value())
    values = {V.id("U0"): lam * s0 * s0 * dom.frac(1, 2), V.id("U1"): lam * s0, V.id("U2"): lam}
    psi_q, chi_q = G.solve_onshell(geo, psi0, chi0, m, lam, max_order=2)
    agree = True
    for mine, ref in ((psi, psi_q), (chi, chi_q)):
        for k in ref.c:
            for x, y in zip(np.asarray(mine.c[k], dtype=object).ravel(), np.asarray(ref.c[k], dtype=object).ravel()):
                agree = agree and dom.is_zero(as_poly(x).evaluate(values) - y)
    d["solverMatchesStage1ForQuartic"] = agree
    return d


def homogeneous_g3(geo, m, lam, psi_value, chi_value, general=False):
    """Homogeneous Psi(x4) on the Bianchi-I frame G3, on shell: rho, p_(i), KE/PE splits, T_ij, T_4i."""
    dom = geo.dom
    V = JetVars(species=())

    def jet(vals):
        c = {(): np.array([dom.conv(sp.Rational(v.numerator, v.denominator)) for v in vals], dtype=object)}
        for alpha in G.multi_indices(2)[1:]:
            c[alpha] = np.array([dom.zero] * 16, dtype=object)
        return G.TJet(2, c)
    psi0, chi0 = jet(psi_value), jet(chi_value)
    if general:
        psi, chi, ok = solve_onshell_general(geo, psi0, chi0, m, general_Uprime(V))
        U_of_S = general_U(V)
    else:
        psi, chi = G.solve_onshell(geo, psi0, chi0, m, lam, max_order=2)
        E, Eb, _ = G.field_equations(geo, psi, chi, m, lam)
        ok = G.jet_is_zero(E, dom, max_order=1) and G.jet_is_zero(Eb, dom, max_order=1)
        U_of_S = quartic_U(lam, dom)
    homog = all(all(as_poly(x).is_zero(dom) for x in np.asarray(J.c[k], dtype=object).ravel())
                for J in (psi, chi) for k in J.c if k and any(i != TIME for i in k))
    parts = emt_general(geo, psi, chi, m, U_of_S)
    T0 = parts["T"].value()
    ginv = geo.ginv.value()
    S0 = as_poly(val(parts["S"]))
    if general:
        U0, U1 = V.v("U0"), V.v("U1")
    else:
        U0, U1 = as_poly(lam * val(parts["S"]) * val(parts["S"]) * dom.frac(1, 2)), as_poly(lam * val(parts["S"]))
    trans = [i for i in range(8) if i != TIME]
    rho = as_poly(T0[TIME, TIME])
    pis = [as_poly(ginv[i, i] * T0[i, i]) for i in trans]
    gam4 = geo.gam.value()[TIME]
    pb0 = parts["pb"].value()
    K4 = as_poly((pb0.dot(gam4).dot(parts["Dpsi"].value()[TIME]) - parts["Dpb"].value()[TIME].dot(gam4).dot(psi.value())) * dom.frac(1, 2))
    KEL = K4 * dom.frac(1, 2)
    PEL = rho - KEL
    K = as_poly(val(parts["kin"]))
    KEH = -(K - K4)
    PEH = S0 * m + U0
    hv = [geo.e.value()[i, i] for i in range(8)]
    hdv = [geo.e.coeff((TIME,))[i, i] for i in range(8)]
    Hh = [hdv[i] / hv[i] for i in range(8)]
    gl = geo.gam_low.value()
    psv = psi.value()
    Tij_ok = True
    Tij_nonzero = False
    for i in trans:
        for j in trans:
            if i == j:
                continue
            formula = as_poly(pb0.dot(gl[i]).dot(gl[j]).dot(gam4).dot(psv)) * ((Hh[i] - Hh[j]) * dom.frac(1, 4))
            Tij_ok = Tij_ok and (as_poly(T0[i, j]) - formula).is_zero(dom)
            Tij_nonzero = Tij_nonzero or not as_poly(T0[i, j]).is_zero(dom)
    z = lambda p: as_poly(p).is_zero(dom)  # noqa: E731
    out = {"solved": ok and homog, "rho": z(rho - (S0 * m + U0)), "pressuresIsotropic": all(z(p - (S0 * U1 - U0)) for p in pis),
           "KE_L": z(KEL - (S0 * (U1 + m)) * dom.frac(1, 2)), "PE_L": z(PEL - (S0 * m + U0 * 2 - S0 * U1) * dom.frac(1, 2)),
           "KE_H": z(KEH), "PE_H": z(rho - PEH), "rhoPlusP": z(rho + pis[0] - KEL * 2), "pMinus": z(pis[0] - (KEL - PEL)),
           "Tij": Tij_ok, "T4iZeroOnShell": all(z(T0[TIME, i]) for i in trans), "TijNonzero": Tij_nonzero}
    if not general:
        r, p = to_fraction(T0[TIME, TIME]), to_fraction(ginv[0, 0] * T0[0, 0])
        out.update({"rhoExact": qstr(r), "pExact": qstr(p), "KE_LExact": qstr(to_fraction(KEL.t.get((), 0))),
                    "PE_LExact": qstr(to_fraction(PEL.t.get((), 0))), "wExact": qstr(p / r), "SExact": qstr(to_fraction(S0.t.get((), 0)))})
    return out


G3_PARAMETERS = {"q1": (Fraction(3, 7), Fraction(5, 11)), "q2": (Fraction(-2, 5), Fraction(7, 13)),
                 "q3": (Fraction(5, 9), Fraction(-3, 8))}


# ---------------------------------------------------------------------------
# 10. the full vielbein variation (own closed form; exact linearisation checks)
#
# Lean form of (L1): with Bil^{cab} = Psibar {gamma^c, S^{ab}} Psi (totally antisymmetric),
# F^a_rho = (1/2)(Psibar gamma^a d_rho Psi - d_rho Psibar gamma^a Psi) (flat gammas),
# K_{cab} = e_c^rho e_a^sigma (d_rho e_{sigma b} - d_sigma e_{rho b}) (object of anholonomy) and
# omega_[cab] = (1/2) K_[cab]:
#     L = |det e| [ e_a^rho F^a_rho + (1/8) K_{cab} Bil^{cab} - m S - U(S) ].
# L is affine in d e, so dL/d(d_nu e_mu^d) = P^nu_{mu d} = (1/4) sqrt|g| e_c^nu e_a^mu Bil^{ca}_d, and
#     dL/de_mu^d = sqrt|g| [ e_d^mu Ls - e_a^mu F^a_rho e_d^rho - (1/4) e_c^mu K_{dab} Bil^{cab} ].
# E[mu, d] = dL/de_mu^d - d_nu P^nu_{mu d}; X^{mu nu} = E[mu, d] e^{d nu}; the claim is
# (X + X^T)/2 = sqrt|g| T^{mu nu} (T from the Stage-1 formula) off shell, (X - X^T)/2 = 0 on shell.
# ---------------------------------------------------------------------------

def _mat_inverse_generic(M):
    n = len(M)
    A = [list(M[i]) + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            x = A[r][col]
            re = x.a if isinstance(x, Dual) else x
            if re != 0:
                piv = r
                break
        if piv is None:
            raise ZeroDivisionError("singular")
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r != col:
                f = A[r][col]
                if not (f == 0):
                    A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [row[n:] for row in A]


def _det_generic(M):
    n = len(M)
    A = [list(r) for r in M]
    det = 1
    for col in range(n):
        piv = None
        for r in range(col, n):
            x = A[r][col]
            re = x.a if isinstance(x, Dual) else x
            if re != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        pv = A[col][col]
        det = det * pv
        for r in range(col + 1, n):
            f = A[r][col]
            if not (f == 0):
                q = f / pv
                A[r] = [x - q * y for x, y in zip(A[r], A[col])]
    return det


class LeanLagrangian:
    """(L1) at a point as an explicit function of (e, d e) for fixed field data (value level)."""

    def __init__(self, geo, psi, chi, m, lam):
        dom = geo.dom
        self.dom = dom
        gd = geo.gd
        self.m, self.lam = m, lam
        pb = G.psibar_from_chi(geo, chi)
        self.pb, self.psi = pb, psi
        pb0, psi0 = pb.value(), psi.value()
        dpsi0, dpb0 = psi.grad().value(), pb.grad().value()
        half = dom.frac(1, 2)
        self.F = [[(pb0.dot(gd.GAM[a]).dot(dpsi0[rho]) - dpb0[rho].dot(gd.GAM[a]).dot(psi0)) * half for rho in range(8)]
                  for a in range(8)]
        self.Mcab = np.empty((8, 8, 8, 16, 16), dtype=object)
        for c in range(8):
            for a in range(8):
                for b in range(8):
                    self.Mcab[c, a, b] = gd.GAM[c].dot(gd.S[a, b]) + gd.S[a, b].dot(gd.GAM[c])
        self.Bil = np.einsum("i,cabij,j->cab", pb0, self.Mcab, psi0)
        self.S0 = pb0.dot(psi0)
        self.sign = geo.sqrtg_sign
        self.e0 = [[geo.e.value()[i, j] for j in range(8)] for i in range(8)]
        de = geo.e.grad().value()                   # [nu, mu, a] = d_nu e_mu^a
        self.de0 = [[[de[n, mu, a] for a in range(8)] for mu in range(8)] for n in range(8)]

    def K_tensor(self, einv, de):
        Dq = [[[(de[r][s][b] - de[s][r][b]) * ETA[b] for b in range(8)] for s in range(8)] for r in range(8)]
        K = [[[0] * 8 for _ in range(8)] for _ in range(8)]
        for b in range(8):
            tmp = [[sum((einv[c][r] * Dq[r][s][b] for r in range(8) if not (Dq[r][s][b] == 0)), 0) for s in range(8)]
                   for c in range(8)]
            for c in range(8):
                for a in range(8):
                    K[c][a][b] = sum((tmp[c][s] * einv[a][s] for s in range(8)), 0)
        return K

    def value(self, e=None, de=None):
        e = self.e0 if e is None else e
        de = self.de0 if de is None else de
        einv = _mat_inverse_generic(e)
        sg = _det_generic(e) * self.sign
        K = self.K_tensor(einv, de)
        Ls = sum((einv[a][r] * self.F[a][r] for a in range(8) for r in range(8)), 0)
        Ls = Ls + sum((K[c][a][b] * self.Bil[c, a, b] for c in range(8) for a in range(8) for b in range(8)
                       if not (self.Bil[c, a, b] == 0)), 0) * self.dom.frac(1, 8)
        Ls = Ls - self.m * self.S0 - self.lam * self.S0 * self.S0 * self.dom.frac(1, 2)
        return sg * Ls, sg, Ls, einv, K

    def closed_form_dLde(self):
        L, sg, Ls, einv, K = self.value()
        q = self.dom.frac(1, 4)
        out = [[None] * 8 for _ in range(8)]
        for mu in range(8):
            for d in range(8):
                t1 = einv[d][mu] * Ls
                t2 = sum((einv[a][mu] * self.F[a][r] * einv[d][r] for a in range(8) for r in range(8)), 0)
                t3 = sum((einv[c][mu] * K[d][a][b] * self.Bil[c, a, b] for c in range(8) for a in range(8) for b in range(8)
                          if not (self.Bil[c, a, b] == 0)), 0)
                out[mu][d] = sg * (t1 - t2 - t3 * q)
        return out

    def closed_form_P(self):
        L, sg, Ls, einv, K = self.value()
        q = self.dom.frac(1, 4)
        return [[[sg * q * sum((einv[c][n] * einv[a][mu] * self.Bil[c, a, d] * ETA[d] for c in range(8) for a in range(8)), 0)
                  for d in range(8)] for mu in range(8)] for n in range(8)]


def vielbein_variation_point(geo, psi, chi, m, lam, psi_on, chi_on, all_directions=True):
    dom = geo.dom
    d = {}
    lean = LeanLagrangian(geo, psi, chi, m, lam)
    parts = emt_general(geo, psi, chi, m, quartic_U(lam, dom))
    stage1_L = val(G.jmul(geo.sqrtg, parts["Ls"]))
    Lval = lean.value()[0]
    d["leanLagrangianEqualsStage1"] = dom.is_zero(Lval - stage1_L)
    dLde = lean.closed_form_dLde()
    lin_ok = True
    directions = [(mu, a) for mu in range(8) for a in range(8)]
    for mu, a in directions:
        e_d = [[Dual(lean.e0[i][j], 1 if (i == mu and j == a) else 0) for j in range(8)] for i in range(8)]
        Ld = lean.value(e=e_d)[0]
        lin_ok = lin_ok and dom.is_zero(Ld.b - dLde[mu][a])
    d["dLdeMatchesLinearisation64"] = lin_ok
    P = lean.closed_form_P()
    aff_ok = True
    dirs = [(n, mu, a) for n in range(8) for mu in range(8) for a in range(8)]
    if not all_directions:
        dirs = dirs[:64]
    for n, mu, a in dirs:
        de = [[[lean.de0[x][y][z] + (1 if (x == n and y == mu and z == a) else 0) for z in range(8)] for y in range(8)]
              for x in range(8)]
        aff_ok = aff_ok and dom.is_zero(lean.value(de=de)[0] - Lval - P[n][mu][a])
    d["PMatchesAffineDifferences"] = aff_ok
    d["affineDirectionsChecked"] = len(dirs)
    # d_nu P^nu_{mu d} from x-jets of sqrt|g|, e_a^mu and Bil
    pb = lean.pb
    Bil = G.jein("cabj,j->cab", G.jein("i,cabij->cabj", pb, lean.Mcab), psi)
    etaM = np.array([[dom.conv(ETA[i] if i == j else 0) for j in range(8)] for i in range(8)], dtype=object)
    BilLow = Bil.map(lambda v: np.einsum("cab,bd->cad", v, etaM))
    A = G.jein("cn,cad->nad", geo.einv.truncate(1), BilLow)
    Pj = G.jmul(geo.sqrtg.truncate(1), G.jein("am,nad->nmd", geo.einv.truncate(1), A)).scale(dom.frac(1, 4))
    d["PjetValueMatchesClosedForm"] = all(dom.is_zero(Pj.value()[n, mu, a] - P[n][mu][a]) for n in range(8) for mu in range(8) for a in range(8))
    divP = [[sum((Pj.d(n).value()[n, mu, a] for n in range(8)), 0) for a in range(8)] for mu in range(8)]
    E = [[dLde[mu][a] - divP[mu][a] for a in range(8)] for mu in range(8)]
    einv0 = geo.einv.value()
    X = np.array([[sum((E[mu][a] * ETA[a] * einv0[a, nu] for a in range(8)), 0) for nu in range(8)] for mu in range(8)], dtype=object)
    ginv = geo.ginv.value()
    sg0 = val(geo.sqrtg)
    Tup = ginv.dot(parts["T"].value()).dot(ginv) * sg0
    d["symmetricPartEqualsSqrtgTupper_offShell"] = G.arr_is_zero((X + X.T) * dom.frac(1, 2) - Tup, dom)
    d["antisymmetricPartNonzero_offShell"] = not G.arr_is_zero(X - X.T, dom)
    # on shell
    lean_on = LeanLagrangian(geo, psi_on, chi_on, m, lam)
    dLde_on = lean_on.closed_form_dLde()
    Bil_on = G.jein("cabj,j->cab", G.jein("i,cabij->cabj", lean_on.pb, lean_on.Mcab), psi_on)
    A_on = G.jein("cn,cad->nad", geo.einv.truncate(1), Bil_on.map(lambda v: np.einsum("cab,bd->cad", v, etaM)))
    Pj_on = G.jmul(geo.sqrtg.truncate(1), G.jein("am,nad->nmd", geo.einv.truncate(1), A_on)).scale(dom.frac(1, 4))
    E_on = [[dLde_on[mu][a] - sum((Pj_on.d(n).value()[n, mu, a] for n in range(8)), 0) for a in range(8)] for mu in range(8)]
    X_on = np.array([[sum((E_on[mu][a] * ETA[a] * einv0[a, nu] for a in range(8)), 0) for nu in range(8)] for mu in range(8)], dtype=object)
    parts_on = emt_general(geo, psi_on, chi_on, m, quartic_U(lam, dom))
    Tup_on = ginv.dot(parts_on["T"].value()).dot(ginv) * sg0
    d["symmetricPartEqualsSqrtgTupper_onShell"] = G.arr_is_zero((X_on + X_on.T) * dom.frac(1, 2) - Tup_on, dom)
    d["antisymmetricPartZero_onShell"] = G.arr_is_zero(X_on - X_on.T, dom)
    d["offShellS"] = exact_summary(dom, lean.S0)
    return d, parts["T"].value()


def run_emt(geos, rec, quick):
    rng = random.Random(62000)
    res = {}
    points = [("G1p1", geos.g1("p1")), ("G2", geos.g2())]
    if not quick:
        points[1:1] = [("G1p2", geos.g1("p2")), ("G1p3", geos.g1("p3"))]
    params = [(Fraction(3, 7), Fraction(5, 11)), (Fraction(-2, 5), Fraction(7, 13)), (Fraction(5, 9), Fraction(-3, 8))]
    for i, (name, geo) in enumerate(points):
        dom = geo.dom
        m, lam = params[i % 3]
        res[name] = emt_point(geo, rng, dom.conv(sp.Rational(m.numerator, m.denominator)),
                              dom.conv(sp.Rational(lam.numerator, lam.denominator)))
    rec.check("EMT_symmetricAndReal", all(d["symmetricOffShell"] and d["swapSymmetricOffShell"] and d.get("realForConjugateData", True)
                                          for d in res.values()), {k: {kk: d[kk] for kk in ("symmetricOffShell", "swapSymmetricOffShell", "realForConjugateData") if kk in d} for k, d in res.items()})
    rec.check("EMT_conservationOnShell", all(d["onShellJetsSolved"] and d["conservationOnShell"] and d["divergenceNonzeroOffShell"]
                                             for d in res.values()), res)
    rec.check("EMT_traceOnShell", all(d["traceOnShell"] and d["onShellLagrangianIsSUprimeMinusU"] for d in res.values()),
              {k: d["traceOnShellValue"] for k, d in res.items()})
    rec.check("current_conservationAndReality", all(d["currentConservedOnShell"] and d["currentDivergenceNonzeroOffShell"]
                                                    and d.get("currentjImaginary", True) for d in res.values()),
              {k: {kk: d[kk] for kk in ("currentConservedOnShell", "currentDivergenceNonzeroOffShell", "currentjImaginary") if kk in d}
               for k, d in res.items()})
    rec.check("EMT_observerSplitGaussianNormal", any(d["gaussianNormal"] for d in res.values()) and all(
        d["rhoEqualsKEHplusPEH_offShell"] and d["rhoEqualsK4minusLs_offShell"] for d in res.values() if d["gaussianNormal"]),
        {k: {kk: d[kk] for kk in ("gaussianNormal", "rhoEqualsKEHplusPEH_offShell", "rhoEqualsK4minusLs_offShell") if kk in d}
         for k, d in res.items()})
    gen = {}
    for name, geo in (points[:1] + points[-1:]):
        gen[name] = emt_general_U_point(geo, random.Random(62030), geo.dom.frac(3, 7))
    rec.check("EMT_generalSmoothU", all(all(d.values()) for d in gen.values()), gen)
    homog = {}
    for k, lab in enumerate(("q1", "q2", "q3"), start=1):
        geo = geos.g3(lab)
        q = geo.dom
        m, lam = G3_PARAMETERS[lab]
        base = lcg_field_data(63000 + 100 * k)
        mq = q.conv(sp.Rational(m.numerator, m.denominator))
        lq = q.conv(sp.Rational(lam.numerator, lam.denominator))
        homog["G3" + lab] = {"quartic": homogeneous_g3(geo, mq, lq, base[0], base[3]),
                             "generalU": homogeneous_g3(geo, mq, None, base[0], base[3], general=True),
                             "x4": qstr(to_fraction(G.G3_POINTS[lab][4])), "m": qstr(m), "lambda": qstr(lam),
                             "dataSeed": 63000 + 100 * k}
    rec.check("EMT_homogeneousEquationsOfState", all(all_true(h["quartic"]) and all_true(h["generalU"]) for h in homog.values()), homog)
    # full vielbein variation: G1 p1 (LCG data of the export), G4 (integer frame), G3 q1
    var = {}
    vpoints = [("G1p1", geos.g1("p1"), 61000 + 100), ("G4p1", geos.g4(1), 61000 + 200), ("G3q1", geos.g3("q1"), 61000 + 300)]
    exported_T = None
    for name, geo, seed in vpoints:
        dom = geo.dom
        m, lam = dom.frac(3, 7), dom.frac(5, 11)
        off = lcg_field_data(seed)
        psi = jet_from_derivatives(off[0], off[1], off[2], dom)
        chi = jet_from_derivatives(off[3], off[4], off[5], dom)
        on = lcg_field_data(seed + 50)
        psi_on, chi_on = G.solve_onshell(geo, jet_from_derivatives(on[0], on[1], on[2], dom),
                                         jet_from_derivatives(on[3], on[4], on[5], dom), m, lam, max_order=1)
        dd, Tlow = vielbein_variation_point(geo, psi, chi, m, lam, psi_on, chi_on, all_directions=not quick)
        dd["seeds"] = [seed, seed + 50]
        var[name] = dd
        if name == "G1p1":
            exported_T = [[qstr(to_fraction(Tlow[i, j])) for j in range(8)] for i in range(8)]
    ok = all(all(v for k, v in dd.items() if isinstance(v, bool)) for dd in var.values())
    rec.check("EMT_vielbeinVariation", ok, var)
    return {"G1p1_offShellTlower": exported_T, "G1p1_offShellS": var["G1p1"]["offShellS"],
            "homogeneousG3": homog, "emtPoints": res}


# ---------------------------------------------------------------------------
# 11. dirac16complex00 specifics: indefinite charge, classical energy unbounded below
#     (flat space; a direct EMT implementation, independent of the jet engine)
# ---------------------------------------------------------------------------

def cscale_vec(c, v):
    cr, ci = c
    return [(cr * a - ci * b, cr * b + ci * a) for a, b in v]


def cnorm2(v):
    return sum((a * a + b * b for a, b in v), Fraction(0))


def mat_of(real):
    return cq_matrix(real)


def flat_plane_wave_parts(alg, u, kcov):
    """Bilinear pieces of a flat plane wave Psi = u e^{i k_mu x^mu} (kcov = (k_0..k_7), k_4 = -omega):
    returns (Tkin_{mu nu} = -(1/4)[...] + eta_{mu nu} Kin, Kin, S) as Gaussian rationals (re, im)."""
    Cc = mat_of(alg.C)
    gam_c = [mat_of(g) for g in alg.gam]
    Cg = [EX.cmatmul(Cc, g) for g in gam_c]
    # Psibar gamma^a d_nu Psi = i k_nu u^dagger C gamma^a u; (d_nu Psibar) gamma^a Psi = -i k_nu u^dagger C gamma^a u
    V = [cvec_dot(u, Cg[a], u) for a in range(8)]                 # u^dagger C gamma^a u
    S = cvec_dot(u, Cc, u)

    def times_i(z, k):
        return (-z[1] * k, z[0] * k)
    kin = (Fraction(0), Fraction(0))
    for a in range(8):
        # (1/2)(i k_a V^a - (-i k_a) V^a) = i k_a V^a with gamma^a upper and d_a
        t = times_i(V[a], kcov[a])
        kin = (kin[0] + t[0], kin[1] + t[1])
    T = [[None] * 8 for _ in range(8)]
    for mu in range(8):
        for nu in range(8):
            # gamma_mu = eta_mu mu gamma^mu; A_{mu nu} = i k_nu eta_mu V^mu, B_{mu nu} = -i k_mu eta_nu V^nu
            A1 = times_i(V[mu], kcov[nu] * ETA[mu])
            A2 = times_i(V[nu], kcov[mu] * ETA[nu])
            B1 = times_i(V[nu], -kcov[mu] * ETA[nu])
            B2 = times_i(V[mu], -kcov[nu] * ETA[mu])
            re = -(A1[0] + A2[0] - B1[0] - B2[0]) / 4
            im = -(A1[1] + A2[1] - B1[1] - B2[1]) / 4
            if mu == nu:
                re += ETA[mu] * kin[0]
                im += ETA[mu] * kin[1]
            T[mu][nu] = (re, im)
    return T, kin, S


def plane_wave_T(alg, u, kcov, m, U, scale=Fraction(1)):
    """Full T_{mu nu} = scale*(Tkin - eta m S_u) - eta U(scale S_u) for Psi = sqrt(scale) u e^{ik.x}."""
    Tk, kin, S = flat_plane_wave_parts(alg, u, kcov)
    Sfull = S[0] * scale
    T = [[None] * 8 for _ in range(8)]
    for mu in range(8):
        for nu in range(8):
            re = Tk[mu][nu][0] * scale
            im = Tk[mu][nu][1] * scale
            if mu == nu:
                re += ETA[mu] * (-m * Sfull - U(Sfull))
            T[mu][nu] = (re, im)
    return T, Sfull, S[1] * scale


def dirac_residual(alg, u, kcov, M):
    """(i gamma^mu k_mu - M) u with gamma^mu k_mu = sum_a gamma^a k_a (flat)."""
    gk = EX.zeros(16)
    for a in range(8):
        gk = EX.add(gk, EX.scale(kcov[a] * 1, alg.gam[a]))
    op = (EX.scale(-M, EX.identity(16)), gk)
    return cmat_vec(op, u)


def single_particle_h(alg, M, kspace):
    """h_k = -i M gamma^4 - gamma^4 gamma^j k_j (j = 0..3, 5..7), i d_4 Psi = h Psi."""
    g4 = alg.gam[4]
    real = EX.zeros(16)
    for j in range(8):
        if j != TIME and kspace[j] != 0:
            real = EX.sub(real, EX.scale(kspace[j], EX.matmul(g4, alg.gam[j])))
    imag = EX.scale(-M, g4)
    return (real, imag)


def stack(*mats):
    return ([row for m in mats for row in m[0]], [row for m in mats for row in m[1]])


def cminus_scalar(M, s):
    return (EX.sub(M[0], EX.scale(s, EX.identity(16))), M[1])


def check_charge_indefinite(alg):
    d = {}
    B = alg.B
    plus = complex_nullspace(cminus_scalar(B, 1))
    minus = complex_nullspace(cminus_scalar(B, -1))
    d["dimBplus"] = len(plus)
    d["dimBminus"] = len(minus)
    up, um = plus[0], minus[0]
    jp, jm = cvec_dot(up, B, up), cvec_dot(um, B, um)
    d["J4Plus"] = qstr(jp[0])
    d["normPlus"] = qstr(cnorm2(up))
    d["J4Minus"] = qstr(jm[0])
    d["normMinus"] = qstr(cnorm2(um))
    d["J4PlusEqualsNorm"] = jp == (cnorm2(up), 0)
    d["J4MinusEqualsMinusNorm"] = jm == (-cnorm2(um), 0)
    d["PsiPlus"] = [[qstr(a), qstr(b)] for a, b in up]
    d["PsiMinus"] = [[qstr(a), qstr(b)] for a, b in um]
    # j^4 = Psibar gamma^4 Psi = i Psi^dagger B Psi (C gamma^4 = i B)
    Cg4 = mat_of(EX.matmul(alg.C, alg.gam[4]))
    j4 = cvec_dot(up, Cg4, up)
    d["j4IsIJ4"] = j4 == (Fraction(0), jp[0])
    # every Spin(4,4)-invariant Hermitian form H = al C P_- + be C P_+ (al, be real): the charge density
    # matrix Herm(c H gamma^4) is traceless with square |k|^2, k = (conj(c) be - c al)/2
    al, be, cr, ci = sp.symbols("alpha beta c_r c_i", real=True)
    Cs = alg.C_sym
    Pm = (sp.eye(16) - alg.g8_sym) / 2
    Pp = (sp.eye(16) + alg.g8_sym) / 2
    H = al * Cs * Pm + be * Cs * Pp
    c = cr + sp.I * ci
    X = c * H * alg.gam_sym[4]
    Hm = (X + X.H) / 2
    k2 = sp.expand(((cr - sp.I * ci) * be - c * al) * ((cr + sp.I * ci) * be - (cr - sp.I * ci) * al) / 4)
    d["candidateChargeDensityTraceless"] = sp.simplify(Hm.trace()) == 0
    d["candidateChargeDensitySquareIsK2"] = sp.expand(Hm * Hm - k2 * sp.eye(16)) == sp.zeros(16, 16)
    d["hermitianFormsAreInvariantSpace"] = all(sp.expand(S.T * H + H * S) == sp.zeros(16, 16)
                                               for (a, b), S in alg.S_sym.items() if a < b)
    ok = (d["dimBplus"] == 8 and d["dimBminus"] == 8 and d["J4PlusEqualsNorm"] and d["J4MinusEqualsMinusNorm"]
          and d["j4IsIJ4"] and d["candidateChargeDensityTraceless"] and d["candidateChargeDensitySquareIsK2"]
          and d["hermitianFormsAreInvariantSpace"])
    d["statement"] = ("C gamma^4 = i B, so j^4 = Psibar gamma^4 Psi = i Psi^dagger B Psi and the real conserved charge "
                      "density is J^4 = -i j^4 = Psi^dagger B Psi (Gaussian normal gauge). B is Hermitian with eigenvalues "
                      "+1 and -1 eight times each, so J^4 = +|Psi|^2 or -|Psi|^2 on the B-eigenvectors: INDEFINITE. Every "
                      "Spin(4,4)-invariant Hermitian form gives a candidate density Herm(c H gamma^4) with eigenvalues "
                      "+-|k| (eight each): no positive-definite conserved charge density exists; the probability "
                      "interpretation of Dirac's wave function fails for the classical field dirac16complex00 in (4,4).")
    return ok, d


def check_energy_unbounded(alg):
    d = {}
    m = Fraction(1)
    kspace = [Fraction(v) for v in (1, 1, 2, 3, 0, 0, 0, 0)]
    h = single_particle_h(alg, m, kspace)
    d["hCommutesWithB"] = EX.cis_zero(EX.ccommutator(h, alg.B))
    waves = []
    ok_waves = True
    gordon = True
    for omega in (Fraction(4), Fraction(-4)):
        eig = complex_nullspace(cminus_scalar(h, omega))
        P = ([[v[k][0] for v in eig] for k in range(16)], [[v[k][1] for v in eig] for k in range(16)])
        Pd = EX.cdagger(P)
        lhs = EX.cmatmul(EX.cmatmul(Pd, mat_of(alg.C)), P)
        rhs = EX.cmatmul(EX.cmatmul(Pd, alg.B), P)
        gordon = gordon and EX.cequal(lhs, EX.cscale(m / omega, 0, rhs))
        for s in (1, -1):
            joint = complex_nullspace(stack(cminus_scalar(h, omega), cminus_scalar(alg.B, s)))
            u = joint[0]
            kcov = list(kspace)
            kcov[TIME] = -omega
            res = dirac_residual(alg, u, kcov, m)
            T, S, Sim = plane_wave_T(alg, u, kcov, m, lambda x: Fraction(0))
            J4 = cvec_dot(u, alg.B, u)
            rho = T[TIME][TIME]
            u2 = cscale_vec((Fraction(2), Fraction(1)), u)
            T2, _, _ = plane_wave_T(alg, u2, kcov, m, lambda x: Fraction(0))
            w = {"omega": qstr(omega), "kreinSign": s, "dimEigenspace": len(eig), "dimJoint": len(joint),
                 "solves": all(a == 0 and b == 0 for a, b in res), "rho": qstr(rho[0]), "rhoImaginary": qstr(rho[1]),
                 "J4": qstr(J4[0]), "norm": qstr(cnorm2(u)), "rhoIsOmegaJ4": rho == (omega * J4[0], 0),
                 "rhoScalesAbsC2": T2[TIME][TIME] == (5 * rho[0], 5 * rho[1]),
                 "u": [[qstr(a), qstr(b)] for a, b in u]}
            expected_sign = 1 if (omega > 0) == (s > 0) else -1
            w["signAsExpected"] = (rho[0] > 0) if expected_sign > 0 else (rho[0] < 0)
            ok_waves = ok_waves and w["solves"] and w["rhoIsOmegaJ4"] and w["rhoScalesAbsC2"] and w["signAsExpected"] \
                and len(eig) == 8 and len(joint) == 4 and rho[1] == 0
            waves.append(w)
    d["freePlaneWaves"] = waves
    d["gordonIdentity"] = gordon
    # homogeneous rest states, lambda = -1: rho = m S + (lambda/2) S^2 -> -infinity
    lam = Fraction(-1)
    rest = complex_nullspace(stack(cminus_scalar((EX.zeros(16), EX.neg(alg.gam[4])), 1), cminus_scalar(alg.B, 1)))
    v = rest[0]
    Sv = cvec_dot(v, mat_of(alg.C), v)[0]
    homog = []
    ok_h = True
    for S in (Fraction(1), Fraction(10), Fraction(100)):
        t = S / Sv
        Meff = m + lam * S
        omega = Meff                               # -i gamma^4 v = v  =>  omega = M_eff
        kcov = [Fraction(0)] * 8
        kcov[TIME] = -omega
        res = dirac_residual(alg, v, kcov, Meff)
        T, Sfull, _ = plane_wave_T(alg, v, kcov, m, lambda x: lam * x * x / 2, scale=t)
        rho = T[TIME][TIME]
        e = {"S": qstr(S), "lambda": qstr(lam), "solves": all(a == 0 and b == 0 for a, b in res) and Sfull == S,
             "rho": qstr(rho[0]), "rhoFormula": rho == (m * S + lam * S * S / 2, 0)}
        ok_h = ok_h and e["solves"] and e["rhoFormula"]
        homog.append(e)
    d["homogeneousNegativeLambda"] = homog
    # lambda = +1: self-consistent plane waves, omega = 1, M_eff = M, |k|^2 = 1 - M^2, S = M - 1
    lam = Fraction(1)
    fam = []
    ok_f = True
    previous = None
    for Mv, kv in ((Fraction(3, 5), Fraction(4, 5)), (Fraction(5, 13), Fraction(12, 13)), (Fraction(7, 25), Fraction(24, 25)),
                   (Fraction(9, 41), Fraction(40, 41)), (Fraction(11, 61), Fraction(60, 61))):
        ks = [Fraction(0)] * 8
        ks[1] = kv
        hk = single_particle_h(alg, Mv, ks)
        joint = complex_nullspace(stack(cminus_scalar(hk, 1), cminus_scalar(alg.B, -1)))
        u = joint[0]
        S = Mv - 1
        Su = cvec_dot(u, mat_of(alg.C), u)[0]
        t = S / Su
        kcov = list(ks)
        kcov[TIME] = Fraction(-1)
        res = dirac_residual(alg, u, kcov, m + lam * S)
        T, Sfull, _ = plane_wave_T(alg, u, kcov, m, lambda x: lam * x * x / 2, scale=t)
        rho = T[TIME][TIME][0]
        formula = m * S + lam * S * S / 2 + kv * kv * S / Mv
        e = {"M": qstr(Mv), "k": qstr(kv), "S": qstr(S), "amplitudeSquaredPositive": t > 0,
             "solves": all(a == 0 and b == 0 for a, b in res) and Sfull == S and m + lam * S == Mv,
             "rho": qstr(rho), "rhoFormula": rho == formula and T[TIME][TIME][1] == 0}
        ok_f = ok_f and e["solves"] and e["rhoFormula"] and t > 0 and (previous is None or rho < previous)
        previous = rho
        fam.append(e)
    d["selfConsistentPlaneWavesPositiveLambda"] = fam
    M = sp.Symbol("M", positive=True)
    rho_M = (M - 1) + (M - 1) ** 2 / 2 + (1 - M ** 2) * (M - 1) / M
    d["limitMto0"] = str(sp.limit(rho_M, M, 0, "+"))
    deriv = sp.factor(sp.diff(rho_M, M))
    d["drhodM"] = str(deriv)
    d["drhodMPositiveOn01"] = bool(sp.solveset(sp.numer(sp.together(deriv)) <= 0, M, sp.Interval.open(0, 1)) == sp.EmptySet) \
        if sp.denom(sp.together(deriv)).is_positive is not False else False
    lam_s, m_s, S_s = sp.symbols("lambda m S", real=True)
    rho_h = m_s * S_s + lam_s * S_s ** 2 / 2
    crit = sp.solve(sp.diff(rho_h, S_s), S_s)
    d["homogeneousPositiveLambdaMinimum"] = str(sp.simplify(rho_h.subs(S_s, crit[0]))) if len(crit) == 1 else None
    d["homogeneousPositiveLambdaNote"] = ("for lambda > 0 the homogeneous (k = 0) states alone are bounded below by "
                                          "-m^2/(2 lambda); unboundedness for lambda > 0 needs k != 0 (the self-consistent "
                                          "plane-wave family)")
    ok = (d["hCommutesWithB"] and ok_waves and gordon and ok_h and ok_f and d["limitMto0"] == "-oo")
    return ok, d


# ---------------------------------------------------------------------------
# 12. the Stage-2 primordial field (notebook chart z = 6 H x0, t = H x4, arbitrary a4)
# ---------------------------------------------------------------------------

STATIC_SOURCE = {"m": Fraction(-30), "lambda": Fraction(125, 6), "S": Fraction(6, 5), "H": 1}


def primordial_geometry(geos):
    geo = geos.g2()
    dom = geo.dom
    w, c, E, A1, A2, A3, H = G.G2_GENS
    d = {}
    d["sqrtgIsCosZ"] = dom.is_zero(val(geo.sqrtg) - dom.conv(c))
    slash = np.einsum("mij,mjk->ik", geo.gam.value(), geo.Omega.value())
    d["gammaOmegaIs3Hgamma0"] = G.arr_is_zero(slash - geo.gd.GAM[0] * dom.conv(3 * H), dom)
    d["ricciScalar"] = dom.is_zero(geo.Rscalar - dom.conv(6 * H ** 2 * (A1 ** 2 - 7)))
    closed = [-3 * H ** 2 * (A1 ** 2 - 5)] + [H ** 2 * (15 - 3 * A1 ** 2 + A2)] * 3 + [3 * H ** 2 * (7 + A1 ** 2)] + \
             [H ** 2 * (15 - 3 * A1 ** 2 - A2)] * 3
    d["einsteinClosedForms"] = all(dom.is_zero(geo.Gmixed[i, j] - (dom.conv(closed[i]) if i == j else dom.zero))
                                   for i in range(8) for j in range(8))
    d["einsteinMixed"] = [str(sp.factor(e)) for e in closed]
    sz = geos.static_z()
    dz = sz.dom
    d["staticMemberEinstein"] = [dz.to_str(sz.Gmixed[i, i]) for i in range(8)]
    d["staticMemberEinsteinIs15_21"] = all(dz.is_zero(sz.Gmixed[i, j] - (dz.conv(21 if i == TIME else 15) if i == j else 0))
                                           for i in range(8) for j in range(8))
    d["staticMemberRicciScalar"] = dz.to_str(sz.Rscalar)
    d["requiredSourceStatic"] = {"rho_req": "-21 H^2/kappa", "p_req": "+15 H^2/kappa (all seven transverse directions)",
                                 "w_req": "-5/7"}
    ok = all(v for v in d.values() if isinstance(v, bool)) and d["staticMemberRicciScalar"] == "-42"
    return ok, d


def primordial_el_components(geos):
    """The Euler-Lagrange expression w.r.t. Psi^* at the symbolic G2 point equals sqrt|g| C times
    tan z gamma^0 d_0 Psi + s^{-1/6} e^{-a4} gamma^i d_i Psi + gamma^4 d_4 Psi + s^{-1/6} e^{a4} gamma^j d_j Psi
    + 3 H gamma^0 Psi - (m + lambda S) Psi (i = 1,2,3; j = 5,6,7)."""
    geo = geos.g2()
    dom = geo.dom
    w, c, E, A1, A2, A3, H = G.G2_GENS
    sl = SymbolicLagrangian(geo, "quartic")
    E_chi = sl.euler_lagrange("chi")
    GAM = geo.gd.GAM
    coef = [dom.conv(w ** 6 / c)] + [dom.conv(1 / (w * E))] * 3 + [dom.one] + [dom.conv(E / w)] * 3
    comp = poly_zero_array((16,))
    for mu in range(8):
        comp = comp + GAM[mu].dot(sl.dpsi[mu]) * coef[mu]
    comp = comp + GAM[0].dot(sl.psi) * dom.conv(3 * H) - sl.psi * (sl.V.v("m") + sl.Uprime)
    target = geo.gd.C.dot(comp) * dom.conv(c)
    d = {"componentForm": polys_equal(E_chi, target, dom),
         "curvedGammas": G.arr_is_zero(geo.gam.value() - np.array([GAM[mu] * coef[mu] for mu in range(8)], dtype=object), dom)}
    return d["componentForm"] and d["curvedGammas"], d


def homogeneous_state(geo, m, lam, psi_value, chi_value, general=False):
    """x4-only state (all other derivatives zero), solved on shell to second order; rho = -T^4_4,
    p_(i) = T^i_i, KE/PE splits; also d_4 S = 0 and d_4 Psi = -gamma^4 (M_eff - gamma^mu Omega_mu) Psi."""
    dom = geo.dom
    V = JetVars(species=())

    def jet(vals):
        c = {(): np.array([dom.conv(v) if not isinstance(v, Fraction) else dom.conv(sp.Rational(v.numerator, v.denominator))
                           for v in vals], dtype=object)}
        for alpha in G.multi_indices(2)[1:]:
            c[alpha] = np.array([dom.zero] * 16, dtype=object)
        return G.TJet(2, c)
    psi0, chi0 = jet(psi_value), jet(chi_value)
    if general:
        psi, chi, ok = solve_onshell_general(geo, psi0, chi0, m, general_Uprime(V))
        U_of_S = general_U(V)
    else:
        psi, chi = G.solve_onshell(geo, psi0, chi0, m, lam, max_order=2)
        E, Eb, _ = G.field_equations(geo, psi, chi, m, lam)
        ok = G.jet_is_zero(E, dom, max_order=1) and G.jet_is_zero(Eb, dom, max_order=1)
        U_of_S = quartic_U(lam, dom)
    parts = emt_general(geo, psi, chi, m, U_of_S)
    T0 = parts["T"].value()
    ginv = geo.ginv.value()
    S0 = as_poly(val(parts["S"]))
    if general:
        U0, U1 = V.v("U0"), V.v("U1")
    else:
        s0 = val(parts["S"])
        U0, U1 = as_poly(lam * s0 * s0 * dom.frac(1, 2)), as_poly(lam * s0)
    z = lambda p: as_poly(p).is_zero(dom)  # noqa: E731
    slash = np.einsum("mij,mjk->ik", geo.gam.value(), geo.Omega.value())
    Mf = U1 + m
    expected_d4 = -(geo.gd.GAM[TIME].dot(psi.value() * Mf - slash.dot(psi.value())))
    trans = [i for i in range(8) if i != TIME]
    rho = as_poly(-(ginv[TIME, TIME] * T0[TIME, TIME]))
    pis = [as_poly(ginv[i, i] * T0[i, i]) for i in trans]
    gam4 = geo.gam.value()[TIME]
    pb0 = parts["pb"].value()
    K4 = as_poly((pb0.dot(gam4).dot(parts["Dpsi"].value()[TIME]) - parts["Dpb"].value()[TIME].dot(gam4).dot(psi.value())) * dom.frac(1, 2))
    KEL = K4 * dom.frac(1, 2)
    K = as_poly(val(parts["kin"]))
    out = {"solvesAtSecondOrder": ok,
           "homogeneous": all(z(x) for J in (psi, chi) for k in J.c if k and any(i != TIME for i in k) for x in np.asarray(J.c[k], dtype=object).ravel()),
           "d4PsiIsMinusGamma4MeffMinusSlashOmega": all(z(a - b) for a, b in zip(psi.c[(TIME,)], expected_d4)),
           "d4SZero": all(z(x) for x in np.asarray(parts["S"].coeff((TIME,)), dtype=object).ravel()),
           "rho": z(rho - (S0 * m + U0)), "pressures": all(z(p - (S0 * U1 - U0)) for p in pis),
           "KE_L": z(KEL - S0 * Mf * dom.frac(1, 2)), "PE_L": z(rho - KEL - (S0 * m + U0 * 2 - S0 * U1) * dom.frac(1, 2)),
           "KE_H": z(-(K - K4)), "rhoEqualsKEHplusPEH": z(rho - (-(K - K4)) - (S0 * m + U0))}
    return out


def check_matrix_identity_S_conserved(alg):
    """N = -gamma^4 (M - 3 H gamma^0): N^dagger C + C N = 0 for real M, H, so S = Psi^dagger C Psi is exactly
    constant along d_4 Psi = N Psi (then M_eff = m + U'(S) is constant and the linear ODE is solved exactly)."""
    M, H = sp.symbols("M H", real=True)
    g0, g4 = alg.gam_sym[0], alg.gam_sym[4]
    N = -g4 * (M * sp.eye(16) - 3 * H * g0)
    return sp.expand(N.H * alg.C_sym + alg.C_sym * N) == sp.zeros(16, 16)


def static_source_vector(theory):
    v = theory["primordial"]["staticSourceExample"]["v"] if theory else None
    return [(Fraction(a), Fraction(b)) for a, b in v] if v else None


def static_source_z(geos, alg, v):
    """Static member (a4 constant, H = kappa = 1) in the notebook z chart, commuting homogeneous state
    Psi = e^{i omega x4} sqrt(t) v: exact field equation and T^mu_nu = G^mu_nu in all 64 components."""
    geo = geos.static_z()
    dom = geo.dom
    P = STATIC_SOURCE
    m, lam, S = P["m"], P["lambda"], P["S"]
    Meff = m + lam * S
    d = {"Meff": qstr(Meff)}
    # the x4-frequency: N v = i omega v, N = -gamma^4 (M_eff - 3 gamma^0)
    N = EX.scale(-1, EX.matmul(alg.gam[4], EX.sub(EX.scale(Meff, EX.identity(16)), EX.scale(3, alg.gam[0]))))
    Nv = cmat_vec((N, EX.zeros(16)), v)
    omega = None
    for cand in (Fraction(4), Fraction(-4)):
        if all(a == -cand * vi and b == cand * vr for (a, b), (vr, vi) in zip(Nv, v)):
            omega = cand
    d["omega"] = qstr(omega) if omega is not None else None
    d["omegaSquaredIsMeff2Minus9"] = omega is not None and omega * omega == Meff * Meff - 9
    vCv = cvec_dot(v, cq_matrix(alg.C), v)
    d["vDaggerCv"] = qstr(vCv[0])
    t = S / vCv[0]
    d["amplitudeSquared"] = qstr(t)
    if omega is None:
        return False, d

    def conv(x):
        return dom.conv(sp.Rational(x.numerator, x.denominator))

    def jet(values, d4, d44):
        c = {(): np.array([conv(x) for x in values], dtype=object)}
        for alpha in G.multi_indices(2)[1:]:
            c[alpha] = np.array([dom.zero] * 16, dtype=object)
        c[(TIME,)] = np.array([conv(x) for x in d4], dtype=object)
        c[(TIME, TIME)] = np.array([conv(x / 2) for x in d44], dtype=object)
        return G.TJet(2, c)
    vr = [a for a, b in v]
    vi = [b for a, b in v]
    X = jet(vr, [-omega * x for x in vi], [-omega * omega * x for x in vr])      # Re(e^{i omega x4} v)
    Y = jet(vi, [omega * x for x in vr], [-omega * omega * x for x in vi])       # Im(e^{i omega x4} v)
    mq, Mq = conv(m), conv(Meff)
    okE = True
    for Z in (X, Y):
        E, Eb, _ = G.field_equations(geo, Z, Z, Mq, 0)
        okE = okE and G.jet_is_zero(E, dom, max_order=1) and G.jet_is_zero(Eb, dom, max_order=1)
    d["fieldEquationExact"] = okE
    zero_U = lambda Sj: Sj.scale(0)  # noqa: E731
    TXX = emt_general(geo, X, X, mq, zero_U)
    TYY = emt_general(geo, Y, Y, mq, zero_U)
    TXY = emt_general(geo, Y, X, mq, zero_U)      # chi = X (Psi^* slot), psi = Y
    TYX = emt_general(geo, X, Y, mq, zero_U)
    tq = conv(t)
    Sfull = (val(TXX["S"]) + val(TYY["S"])) * tq
    d["S"] = dom.to_str(Sfull)
    Uval = conv(lam) * Sfull * Sfull * dom.frac(1, 2)
    g0 = geo.g.value()
    T = (TXX["T"].value() + TYY["T"].value()) * tq - g0 * Uval
    Tim = (TXY["T"].value() - TYX["T"].value()) * tq
    d["imaginaryPartZero"] = G.arr_is_zero(Tim, dom)
    Tmixed = geo.ginv.value().dot(T)
    d["einsteinEqualsKappaT64"] = G.arr_is_zero(Tmixed - geo.Gmixed, dom)
    rho = -Tmixed[TIME, TIME]
    p = Tmixed[0, 0]
    gam4 = geo.gam.value()[TIME]
    K4 = dom.zero
    for Z, parts in ((X, TXX), (Y, TYY)):
        K4 = K4 + (parts["pb"].value().dot(gam4).dot(parts["Dpsi"].value()[TIME])
                   - parts["Dpb"].value()[TIME].dot(gam4).dot(Z.value())) * dom.frac(1, 2)
    KEL = K4 * tq * dom.frac(1, 2)
    d.update({"rho": dom.to_str(rho), "p": dom.to_str(p), "w": dom.to_str(p / rho), "KE_L": dom.to_str(KEL),
              "PE_L": dom.to_str(rho - KEL),
              "pressuresIsotropic": all(dom.is_zero(Tmixed[i, i] - p) for i in range(8) if i != TIME)})
    ok = (okE and d["einsteinEqualsKappaT64"] and d["imaginaryPartZero"] and d["S"] == qstr(S) and d["rho"] == "-21"
          and d["p"] == "15" and d["pressuresIsotropic"] and d["omegaSquaredIsMeff2Minus9"])
    return ok, d


def run_primordial(alg, geos, rec, quick, theory):
    ok, d = primordial_geometry(geos)
    rec.check("primordial_geometryMatchesStage2", ok, d)
    ok, d = primordial_el_components(geos)
    rec.check("primordial_ELcommuting", ok, d)
    geo = geos.g2()
    dom = geo.dom
    rng = random.Random(64500)
    vals_psi = [G.rand_rational(rng) for _ in range(16)]
    vals_chi = [G.rand_rational(rng) for _ in range(16)]
    m, lam = dom.frac(3, 7), dom.frac(5, 11)
    hq = homogeneous_state(geo, m, lam, vals_psi, vals_chi)
    hu = homogeneous_state(geo, m, None, vals_psi, vals_chi, general=True)
    ident = check_matrix_identity_S_conserved(alg)
    rec.check("primordial_homogeneousState", all_true(hq) and all_true(hu) and ident,
              {"quartic": hq, "generalU": hu, "NdaggerCplusCNZero": ident,
               "statement": "x0-independent commuting state Psi = u(x4) in the Stage-2 primordial field with arbitrary "
                            "a4(t): d_4 u = -gamma^4 (M_eff - 3 H gamma^0) u, and N^dagger C + C N = 0 makes "
                            "S = u^dagger C u exactly constant, so this is an exact classical solution for every U; "
                            "rho = -T^4_4 = m S + U, p_(i) = T^i_i = S U' - U (seven directions), KE_L = S (m + U')/2, "
                            "PE_L = (m S + 2U - S U')/2, KE_H = 0, PE_H = rho."})
    v = static_source_vector(theory) or [(Fraction(a), Fraction(b)) for a, b in
                                        ((1, 0), (0, 3), (0, 0), (0, 0), (1, 0), (0, -3), (0, 0), (0, 0),
                                         (-3, 0), (0, -1), (0, 0), (0, 0), (-3, 0), (0, 1), (0, 0), (0, 0))]
    ok, d = static_source_z(geos, alg, v)
    d["vector"] = [[qstr(a), qstr(b)] for a, b in v]
    d["parameters"] = {k: qstr(Fraction(x)) for k, x in STATIC_SOURCE.items()}
    rec.check("primordial_staticFieldSourcedExactly", ok, d)
    return d


# ---------------------------------------------------------------------------
# 13. the Stage-4 static warped chart (sympy, closed form; independent of the jet engine)
#     ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4}(dx1^2+dx2^2+dx3^2) - e^{-2a4}(dx5^2+dx6^2+dx7^2)]
# ---------------------------------------------------------------------------

def szero(expr):
    """Exact zero test of a sympy expression (expand, combine exponentials, simplify)."""
    e = sp.expand(expr)
    if e == 0:
        return True
    e = sp.expand(sp.powsimp(e, combine="exp"))
    if e == 0:
        return True
    return sp.simplify(e) == 0


def smat_zero(M):
    return all(szero(x) for x in M)


class StaticWarped:
    def __init__(self, alg):
        self.alg = alg
        self.y = sp.Symbol("y", real=True)
        self.x = [self.y] + list(sp.symbols("x1:8", real=True))
        self.H = sp.Symbol("H", positive=True)
        self.a4 = sp.Symbol("a4c", real=True)
        y, H, a4 = self.y, self.H, self.a4
        W = sp.exp(H * y)
        E = sp.exp(a4)
        self.W = W
        self.kappa = sp.exp(-H * y - a4)
        h = [sp.Integer(1), W * E, W * E, W * E, sp.Integer(1), W / E, W / E, W / E]
        self.h = h
        g = [ETA[i] * h[i] ** 2 for i in range(8)]
        self.g = g
        X = self.x
        Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for r in range(8):
            for mu in range(8):
                for nu in range(8):
                    val_ = 0
                    if r == nu:
                        val_ += sp.diff(g[r], X[mu])
                    if r == mu:
                        val_ += sp.diff(g[r], X[nu])
                    if mu == nu:
                        val_ -= sp.diff(g[mu], X[r])
                    Gam[r][mu][nu] = sp.simplify(val_ / (2 * g[r]))
        self.Gam = Gam
        om = [[[sp.simplify((Gam[a][mu][b] * h[a] - (sp.diff(h[a], X[mu]) if a == b else 0)) / h[b])
                for b in range(8)] for a in range(8)] for mu in range(8)]
        self.omega_mixed = om
        self.omega_low = [[[ETA[a] * om[mu][a][b] for b in range(8)] for a in range(8)] for mu in range(8)]
        S = alg.S_sym
        self.Omega = []
        for mu in range(8):
            M = sp.zeros(16, 16)
            for a in range(8):
                for b in range(8):
                    if self.omega_low[mu][a][b] != 0:
                        M += self.omega_low[mu][a][b] * S[(a, b)] / 2
            self.Omega.append(M.applyfunc(sp.simplify))
        gam = alg.gam_sym
        self.gam_up = [gam[mu] / h[mu] for mu in range(8)]
        self.gam_low = [g[mu] * self.gam_up[mu] for mu in range(8)]
        self.sqrtg = sp.simplify(sp.prod(h))
        # Ricci tensor, scalar, mixed Einstein tensor
        Ric = sp.zeros(8, 8)
        for s_ in range(8):
            for n in range(8):
                val_ = 0
                for r in range(8):
                    val_ += sp.diff(Gam[r][s_][n], X[r]) - sp.diff(Gam[r][s_][r], X[n])
                    for l in range(8):
                        val_ += Gam[r][r][l] * Gam[l][s_][n] - Gam[r][n][l] * Gam[l][s_][r]
                Ric[s_, n] = sp.simplify(val_)
        self.Ric = Ric
        self.R = sp.simplify(sum(Ric[i, i] / g[i] for i in range(8)))
        self.Gmixed = sp.Matrix(8, 8, lambda i, j: sp.simplify(Ric[i, j] / g[i] - (self.R / 2 if i == j else 0)))

    def reduced_T(self, chi, chibar, a, abar, R, m):
        """Psi = P(x) chi(y), Psi^dagger = conj(P) chibar (row), d_mu log P = a[mu] (abar = conjugate):
        T_{mu nu}/|P|^2, kin/|P|^2, S/|P|^2 of the (L1) bilinears with Psibar -> Psi^dagger R C
        (R = 1: classical commuting field; R = B: Stage-4 Kohn-Sham expectation rule); U = 0 part."""
        C = self.alg.C_sym
        X = self.x
        Dpsi = [a[mu] * chi + chi.diff(X[mu]) + self.Omega[mu] * chi for mu in range(8)]
        pb = chibar * R * C
        dpb = [(abar[mu] * chibar + chibar.diff(X[mu])) * R * C for mu in range(8)]
        Dpb = [dpb[mu] - pb * self.Omega[mu] for mu in range(8)]
        A = [[(pb * self.gam_low[mu] * Dpsi[nu])[0, 0] for nu in range(8)] for mu in range(8)]
        B = [[(Dpb[mu] * self.gam_low[nu] * chi)[0, 0] for nu in range(8)] for mu in range(8)]
        kin = sum(((pb * self.gam_up[mu] * Dpsi[mu])[0, 0] - (Dpb[mu] * self.gam_up[mu] * chi)[0, 0]) for mu in range(8)) / 2
        S = (pb * chi)[0, 0]
        T = sp.Matrix(8, 8, lambda i, j: -(A[i][j] + A[j][i] - B[i][j] - B[j][i]) / 4 + (self.g[i] * (kin - m * S) if i == j else 0))
        return {"T": T, "kin": kin, "S": S, "pb": pb, "Dpsi": Dpsi, "Dpb": Dpb}


def block_basis(alg):
    """Own construction of the Stage-4 block basis: J = gamma^0 gamma^1 gamma^4, K1 = gamma^2 gamma^3,
    K2 = gamma^5 gamma^6, P(j,s2,s3) = (1+jJ)/2 (1-i s2 K1)/2 (1-i s3 K2)/2, v+ = 8 P (1+gamma^0)/2 e_c for the
    first standard vector with nonzero image, v- = gamma^0 gamma^1 v+; block index 4(1-j)/2 + 2(1-s2)/2 + (1-s3)/2."""
    g = alg.gam_sym
    I16 = sp.eye(16)
    J = g[0] * g[1] * g[4]
    K1 = g[2] * g[3]
    K2 = g[5] * g[6]
    labels = []
    cols = []
    seeds = []
    for j in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                P = (I16 + j * J) / 2 * (I16 - sp.I * s2 * K1) / 2 * (I16 - sp.I * s3 * K2) / 2
                Q = 8 * P * (I16 + g[0]) / 2
                c = next(cc for cc in range(16) if any(Q[r, cc] != 0 for r in range(16)))
                vp = Q[:, c]
                vm = g[0] * g[1] * vp
                labels.append((j, s2, s3))
                seeds.append(c)
                cols += [vp, vm]
    V = sp.Matrix.hstack(*cols)
    return V, labels, seeds


def sigma(k):
    return {0: sp.eye(2), 1: sp.Matrix([[0, 1], [1, 0]]), 2: sp.Matrix([[0, -sp.I], [sp.I, 0]]), 3: sp.Matrix([[1, 0], [0, -1]])}[k]


def block_forms(alg, V, labels):
    g = alg.gam_sym
    mats = {"A0": g[0], "A1": g[0] * g[1], "A4": g[0] * g[4], "B": alg.B_sym, "C": alg.C_sym, "BC": alg.B_sym * alg.C_sym,
            "gamma4gamma1": g[4] * g[1]}
    out = []
    for i, (j, s2, s3) in enumerate(labels):
        Vb = V[:, 2 * i:2 * i + 2]
        forms = {k: sp.simplify(Vb.H * M * Vb / 8) for k, M in mats.items()}
        expected = {"A0": sigma(3), "A1": -sp.I * sigma(2), "A4": j * sigma(1), "B": j * s2 * sigma(0), "C": s2 * sigma(2),
                    "BC": j * sigma(2), "gamma4gamma1": -j * sigma(3)}
        out.append({"forms": forms, "matches": {k: forms[k] == expected[k] for k in expected},
                    "BtimesBlockIsKreinSign": sp.simplify(alg.B_sym * Vb - j * s2 * Vb) == sp.zeros(16, 2)})
    return out


def parse_gq_matrix(rows):
    return sp.Matrix([[sp.Rational(r[0]) + sp.I * sp.Rational(r[1]) for r in row] for row in rows])


def static_reduced_equation(sw, alg):
    y, H = sw.y, sw.H
    k, eps = sp.symbols("k epsilon", real=True)
    Meff = sp.Function("Meff")(y)
    chi = sp.Matrix([sp.Function("chi%d" % n)(y) for n in range(16)])
    a = [-3 * H, sp.I * k, 0, 0, -sp.I * eps, 0, 0, 0]
    X = sw.x
    dirac = sp.zeros(16, 1)
    for mu in range(8):
        dirac += sw.gam_up[mu] * (a[mu] * chi + chi.diff(X[mu]) + sw.Omega[mu] * chi)
    dirac -= Meff * chi
    g = alg.gam_sym
    target = g[0] * chi.diff(y) + sp.I * sw.kappa * k * g[1] * chi - sp.I * eps * g[4] * chi - Meff * chi
    ok_red = smat_zero(dirac - target)
    no_w3 = sp.zeros(16, 1)
    for mu in range(8):
        no_w3 += sw.gam_up[mu] * ((a[mu] + (3 * H if mu == 0 else 0)) * chi + chi.diff(X[mu]) + sw.Omega[mu] * chi)
    survives = not smat_zero(no_w3 - Meff * chi - target)
    return ok_red, {"reducedEquation": ok_red, "withoutW3the3HTermSurvives": survives,
                    "form": "gamma^0 chi' + i kappa(y) k gamma^1 chi - i eps gamma^4 chi = M_eff chi, kappa = e^{-Hy-a4}"}


def static_block_ode(sw, alg, V, labels):
    y = sw.y
    k, eps = sp.symbols("k epsilon", real=True)
    Meff = sp.Function("Meff")(y)
    vv = sp.Function("vv")(y)
    g = alg.gam_sym
    # chi' = gamma^0 [M_eff chi - i kappa k gamma^1 chi + i (eps - v_v) gamma^4 chi]
    Nfull = g[0] * (Meff * sp.eye(16) - sp.I * sw.kappa * k * g[1] + sp.I * (eps - vv) * g[4])
    red = (V.H * Nfull * V / 8).applyfunc(sp.simplify)
    ok = True
    for i, (j, s2, s3) in enumerate(labels):
        for jj in range(8):
            blk = red[2 * i:2 * i + 2, 2 * jj:2 * jj + 2]
            if jj == i:
                expected = Meff * sigma(3) - sw.kappa * k * sigma(2) + sp.I * j * (eps - vv) * sigma(1)
                ok = ok and smat_zero(blk - expected)
            else:
                ok = ok and smat_zero(blk)
    return ok


def block_mode(V, i, c1, c2, cb1, cb2):
    v1, v2 = V[:, 2 * i], V[:, 2 * i + 1]
    chi = v1 * c1 + v2 * c2
    chibar = (v1.H * cb1 + v2.H * cb2)
    return chi, chibar


def static_classical_vs_ks(sw, alg, V, labels, blocks):
    y, H = sw.y, sw.H
    k, eps, m = sp.symbols("k epsilon m", real=True)
    c1, c2, cb1, cb2 = [sp.Function(n)(y) for n in ("c1", "c2", "cb1", "cb2")]
    a = [-3 * H, sp.I * k, 0, 0, -sp.I * eps, 0, 0, 0]
    ab = [-3 * H, -sp.I * k, 0, 0, sp.I * eps, 0, 0, 0]
    out = []
    for i in blocks:
        j, s2, s3 = labels[i]
        chi, chibar = block_mode(V, i, c1, c2, cb1, cb2)
        cl = sw.reduced_T(chi, chibar, a, ab, sp.eye(16), m)
        ks = sw.reduced_T(chi, chibar, a, ab, alg.B_sym, m)
        rel = all(szero(cl["T"][p, q] - j * s2 * ks["T"][p, q]) for p in range(8) for q in range(p, 8))
        nonzero = not all(szero(ks["T"][p, q]) for p in range(8) for q in range(p, 8))
        gam4 = sw.gam_up[TIME]

        def K4(parts):
            return ((parts["pb"] * gam4 * parts["Dpsi"][TIME])[0, 0] - (parts["Dpb"][TIME] * gam4 * chi)[0, 0]) / 2
        n8 = 8 * (cb1 * c1 + cb2 * c2)
        out.append({"block": i, "j": j, "s2": s2, "s3": s3, "kreinSign": j * s2,
                    "classicalEqualsKreinSignTimesKS36": rel, "KSnonzero": nonzero,
                    "K4_KS_equals_eps_n": szero(K4(ks) - eps * n8),
                    "K4_classical_equals_kreinSign_eps_n": szero(K4(cl) - j * s2 * eps * n8)})
    return out


def static_box_modes(sw, alg, V, labels):
    y = sw.y
    out = []
    first_plus = next(i for i, (j, s2, s3) in enumerate(labels) if j * s2 == 1)
    first_minus = next(i for i, (j, s2, s3) in enumerate(labels) if j * s2 == -1)
    M, eps = 3, 5
    for i in (first_plus, first_minus):
        j, s2, s3 = labels[i]
        c2 = sp.sin(4 * y)
        c1 = sp.simplify((sp.diff(c2, y) + M * c2) / (sp.I * j * eps))          # from chi_2' = -M chi_2 + i j eps chi_1
        N = M * sigma(3) + sp.I * j * eps * sigma(1)
        ode = smat_zero(sp.Matrix([sp.diff(c1, y), sp.diff(c2, y)]) - N * sp.Matrix([c1, c2]))
        chi, _ = block_mode(V, i, c1, c2, 0, 0)
        chibar = chi.H
        g = alg.gam_sym
        full_ode = smat_zero(g[0] * chi.diff(y) - sp.I * eps * g[4] * chi - M * chi)
        a = [-3 * sw.H, 0, 0, 0, -sp.I * eps, 0, 0, 0]
        ab = [-3 * sw.H, 0, 0, 0, sp.I * eps, 0, 0, 0]
        parts = sw.reduced_T(chi, chibar, a, ab, sp.eye(16), M)
        rho_raw = sp.expand(parts["T"][TIME, TIME])
        s4, c4 = sp.symbols("s4 c4")
        quad = sp.Poly(sp.expand(rho_raw.subs({sp.sin(4 * y): s4, sp.cos(4 * y): c4})), s4, c4)
        coeffs = {mon: cf for mon, cf in zip(quad.monoms(), quad.coeffs())}
        homogeneous = all(sum(mon) == 2 for mon in coeffs)
        a_ss, a_cc, a_sc = coeffs.get((2, 0), 0), coeffs.get((0, 2), 0), coeffs.get((1, 1), 0)
        A0, B8, C8 = sp.nsimplify((a_ss + a_cc) / 2), sp.nsimplify((a_cc - a_ss) / 2), sp.nsimplify(a_sc / 2)
        rho = A0 + B8 * sp.cos(8 * y) + C8 * sp.sin(8 * y)
        n16 = sp.expand((chibar * chi)[0, 0])
        out.append({"block": i, "kreinSign": j * s2, "odeAndBoundary": ode and full_ode and c2.subs(y, 0) == 0 and
                    sp.simplify(c2.subs(y, -sp.pi / 4)) == 0,
                    "rhoTimesW6": str(sp.factor(rho)), "rhoTimesW6Coefficients": [str(A0), str(B8), str(C8)],
                    "canonicalFormExact": homogeneous and szero(rho_raw - rho) and all(v.is_Rational for v in (A0, B8, C8)),
                    "rhoEqualsKreinSignTimesEpsN": szero(rho_raw - j * s2 * eps * n16),
                    "sign": j * s2, "_rho": rho})
    return out


def static_ks_energy_split(sw, alg):
    y = sw.y
    k, eps, m = sp.symbols("k epsilon m", real=True)
    chi = sp.Matrix([sp.Function("ch%d" % n)(y) for n in range(16)])
    chibar = sp.Matrix([[sp.Function("cb%d" % n)(y) for n in range(16)]])
    a = [-3 * sw.H, sp.I * k, 0, 0, -sp.I * eps, 0, 0, 0]
    ab = [-3 * sw.H, -sp.I * k, 0, 0, sp.I * eps, 0, 0, 0]
    parts = sw.reduced_T(chi, chibar, a, ab, alg.B_sym, m)
    Kperp = sum(((parts["pb"] * sw.gam_up[mu] * parts["Dpsi"][mu])[0, 0] - (parts["Dpb"][mu] * sw.gam_up[mu] * chi)[0, 0])
                for mu in range(8) if mu != TIME) / 2
    return szero(parts["T"][TIME, TIME] - (-Kperp + m * parts["S"]))


def static_mean_field_emt(sw, alg, V, labels, blocks):
    """One-body EMT of a Kohn-Sham block orbital (Stage-4 rule, bare mass m in the Lagrangian) that
    solves chi' = [M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi: the Stage-4 formulas."""
    y = sw.y
    k, eps, m = sp.symbols("k epsilon m", real=True)
    Meff = sp.Function("Meff")(y)
    vv = sp.Function("vv")(y)
    c1, c2, cb1, cb2 = [sp.Function(n)(y) for n in ("c1", "c2", "cb1", "cb2")]
    a = [-3 * sw.H, sp.I * k, 0, 0, -sp.I * eps, 0, 0, 0]
    ab = [-3 * sw.H, -sp.I * k, 0, 0, sp.I * eps, 0, 0, 0]
    g = alg.gam_sym
    out = []
    for i in blocks:
        j, s2, s3 = labels[i]
        N = Meff * sigma(3) - sw.kappa * k * sigma(2) + sp.I * j * (eps - vv) * sigma(1)
        Nb = Meff * sigma(3) + sw.kappa * k * sigma(2) - sp.I * j * (eps - vv) * sigma(1)
        dc = N * sp.Matrix([c1, c2])
        dcb = Nb * sp.Matrix([cb1, cb2])
        subs = {sp.Derivative(c1, y): dc[0], sp.Derivative(c2, y): dc[1],
                sp.Derivative(cb1, y): dcb[0], sp.Derivative(cb2, y): dcb[1]}
        chi, chibar = block_mode(V, i, c1, c2, cb1, cb2)
        parts = sw.reduced_T(chi, chibar, a, ab, alg.B_sym, m)
        Tm = parts["T"]
        n = (chibar * chi)[0, 0]
        s = (chibar * alg.B_sym * alg.C_sym * chi)[0, 0]
        t = (chibar * (-g[4] * g[1]) * chi)[0, 0]
        kap = sw.kappa
        formulas = {"rho": (Tm[TIME, TIME], eps * n - (Meff - m) * s - vv * n),
                    "p_y": (Tm[0, 0] / sw.g[0], eps * n - m * s - kap * k * t),
                    "p_1": (Tm[1, 1] / sw.g[1], kap * k * t + (Meff - m) * s + vv * n)}
        for idx in (2, 3, 5, 6, 7):
            formulas["p_%d" % idx] = (Tm[idx, idx] / sw.g[idx], (Meff - m) * s + vv * n)
        formulas["Ls"] = (parts["kin"] - m * parts["S"], (Meff - m) * s + vv * n)
        res = {name: szero(sp.expand(lhs.subs(subs)) - rhs) for name, (lhs, rhs) in formulas.items()}
        res.update({"block": i, "j": j})
        out.append(res)
    return out


def static_source_y(sw, alg, v, omega):
    """The same exact source in the proper y chart: Psi = e^{i omega x4} sqrt(t) v (t = S/v^dagger C v)."""
    P = STATIC_SOURCE
    m, lam, S = [sp.Rational(P[k].numerator, P[k].denominator) for k in ("m", "lambda", "S")]
    vs = sp.Matrix([sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator) for a, b in v])
    vCv = (vs.H * alg.C_sym * vs)[0, 0]
    t = S / vCv
    om = sp.Rational(omega.numerator, omega.denominator)
    a = [0, 0, 0, 0, sp.I * om, 0, 0, 0]
    ab = [0, 0, 0, 0, -sp.I * om, 0, 0, 0]
    parts = sw.reduced_T(vs, vs.H, a, ab, sp.eye(16), m)
    T = parts["T"] * t - sp.diag(*sw.g) * (lam * S ** 2 / 2)
    Tmixed = sp.Matrix(8, 8, lambda i, j: T[i, j] / sw.g[i])
    Gm = sw.Gmixed.subs(sw.H, 1)
    Meff = m + lam * S
    eq = sp.zeros(16, 1)
    for mu in range(8):
        eq += sw.gam_up[mu] * (a[mu] * vs + sw.Omega[mu] * vs)
    eq = eq.subs(sw.H, 1) - Meff * vs
    return {"fieldEquation": smat_zero(eq), "einsteinEqualsKappaT64": smat_zero((Tmixed - Gm).subs(sw.H, 1)),
            "rho": str(sp.simplify(-Tmixed[TIME, TIME].subs(sw.H, 1))), "p": str(sp.simplify(Tmixed[0, 0].subs(sw.H, 1))),
            "S": str(sp.simplify(parts["S"] * t))}


def run_static(alg, rec, quick, theory, omega_source, v_source):
    sw = StaticWarped(alg)
    d = {"R": str(sw.R), "Gmixed": [str(sw.Gmixed[i, i]) for i in range(8)], "sqrtg": str(sw.sqrtg)}
    slash = sum((sw.gam_up[mu] * sw.Omega[mu] for mu in range(8)), sp.zeros(16, 16))
    d["gammaOmegaIs3Hgamma0"] = smat_zero(slash - 3 * sw.H * alg.gam_sym[0])
    d["geometry"] = (sw.R == -42 * sw.H ** 2 and all(szero(sw.Gmixed[i, j] - ((21 if i == TIME else 15) * sw.H ** 2 if i == j else 0))
                                                     for i in range(8) for j in range(8)) and szero(sw.sqrtg - sw.W ** 6))
    ok_red, dred = static_reduced_equation(sw, alg)
    d.update(dred)
    rec.check("static_geometryAndReducedEquation", d["geometry"] and d["gammaOmegaIs3Hgamma0"] and ok_red and dred["withoutW3the3HTermSurvives"], d)
    V, labels, seeds = block_basis(alg)
    forms = block_forms(alg, V, labels)
    b = {"labels": [list(l) for l in labels], "seedColumns": seeds,
         "unitary": sp.simplify(V.H * V / 8) == sp.eye(16),
         "formsMatchStage4Table": all(all(f["matches"].values()) for f in forms),
         "BonBlockIsKreinSign": all(f["BtimesBlockIsKreinSign"] for f in forms),
         "kreinSigns": [j * s2 for j, s2, s3 in labels]}
    b["blockODE"] = static_block_ode(sw, alg, V, labels)
    ksj = None
    if os.path.exists(KS_THEORY):
        with open(KS_THEORY, "r", encoding="utf-8") as handle:
            ksj = json.load(handle)
        bd = ksj["reduction"]["blockDiagonalisation"]
        b["basisEqualsKohnShamTheoryJson"] = parse_gq_matrix(bd["basisMatrixUnnormalised"]) == V
        ok_json = len(bd["blocks"]) == 8
        for i, blk in enumerate(bd["blocks"]):
            j, s2, s3 = labels[i]
            ok_json = ok_json and (int(blk["j"]), int(blk["s2"]), int(blk["s3"])) == (j, s2, s3) and int(blk["seedColumn"]) == seeds[i]
            ok_json = ok_json and sp.Rational(blk["Beigenvalue"]) == j * s2
            for key in ("A0", "A1", "A4", "B", "C", "BC"):
                ok_json = ok_json and parse_gq_matrix(blk[key]) == forms[i]["forms"][key]
        b["blocksEqualKohnShamTheoryJson"] = ok_json
    else:
        b["basisEqualsKohnShamTheoryJson"] = False
        b["blocksEqualKohnShamTheoryJson"] = False
    rec.check("static_blocksFromStage4Theory", all(v for v in b.values() if isinstance(v, bool)) and sorted(b["kreinSigns"]) == [-1] * 4 + [1] * 4, b)
    blocks = [0, 2] if quick else list(range(8))
    per = static_classical_vs_ks(sw, alg, V, labels, blocks)
    rec.check("static_classicalModeIsKreinWeightedKS", all(p["classicalEqualsKreinSignTimesKS36"] and p["KSnonzero"] and p["K4_KS_equals_eps_n"]
                                                          and p["K4_classical_equals_kreinSign_eps_n"] for p in per), {"blocks": per})
    box = static_box_modes(sw, alg, V, labels)
    rec.check("static_classicalEnergyKreinSigned", all(bm["odeAndBoundary"] and bm["rhoEqualsKreinSignTimesEpsN"] and bm["canonicalFormExact"] for bm in box)
              and sorted(bm["sign"] for bm in box) == [-1, 1], {"boxModes": [{k: v for k, v in bm.items() if not k.startswith("_")} for bm in box]})
    rec.check("static_KSorbitalEnergySplit", static_ks_energy_split(sw, alg),
              {"statement": "Kohn-Sham rule Psi^dagger -> u^dagger B: rho = T_44 = -K_perp + m s off shell (16 arbitrary component functions)"})
    mf = static_mean_field_emt(sw, alg, V, labels, [0, 4] if quick else list(range(8)))
    rec.check("static_meanFieldOneBodyEMT", all(all(v for k, v in r.items() if isinstance(v, bool)) for r in mf), {"blocks": mf})
    src = static_source_y(sw, alg, v_source, omega_source) if omega_source is not None else {"notRun": True}
    rec.check("static_sourceProperChart", src.get("fieldEquation", False) and src.get("einsteinEqualsKappaT64", False)
              and src.get("rho") == "-21" and src.get("p") == "15" and src.get("S") == "6/5", src)
    return {"box": box, "labels": labels, "per": per, "V": V}


# ---------------------------------------------------------------------------
# 14. citations of the Stage-1..4 Python reports (cited checks true, source hashes current)
# ---------------------------------------------------------------------------

CITED_REPORTS = {
    "artifacts/dirac16complex/arbitrary-field/python-geometry-report.json": [
        "LAG_eulerLagrangePsibar_G1", "LAG_eulerLagrangePsibar_G2", "LAG_eulerLagrangePsi_G1", "LAG_eulerLagrangePsi_G2",
        "EMT_conservation_G1", "EMT_conservation_G2", "EMT_trace_G1", "EMT_trace_G2", "EMT_variation",
        "GEO_lichnerowicz_G1", "GEO_lichnerowicz_G2", "EMT_homogeneousReduction"],
    "artifacts/dirac16complex/arbitrary-field/grassmann-demo-report.json": [
        "GR_notebookLgELTrivial", "GR_notebookLgPureDivergence", "GR_complexLagrangianNonTrivial", "GR_complexQuarticEL",
        "GR_complexPsiEquation", "GR_lagrangianHermitian", "GR_emtHermitian", "GR_quarticTermPolynomial",
        "GR_unsymmetrizedKineticNotHermitian", "GR_massTermVanishesReal"],
    "artifacts/dirac16complex/arbitrary-field/python-algebra-report.json": [
        "QNT_kreinSignature", "QNT_flatModeHamiltonian", "ALG_gamma8Map", "ALG_pinLiftCharacter", "ALG_invariantForms"],
    "artifacts/dirac16complex/primordial-field/python-primordial-report.json": ["P_EL", "P_EMT", "P_einstein", "P_source", "P_quant"],
    "artifacts/dirac16complex/kohn-sham/python-theory-report.json": [
        "KS_reduction_blocksBC", "KS_reduction_blockODEMatrix", "KS_reduction_ansatzRemoves3H", "KS_geometry_einsteinMixedDiag"],
}


def run_citations(rec):
    out = {}
    ok = True
    for rel, names in CITED_REPORTS.items():
        path = os.path.join(REPOSITORY_ROOT, rel)
        entry = {"exists": os.path.exists(path)}
        if entry["exists"]:
            with open(path, "r", encoding="utf-8") as handle:
                doc = json.load(handle)
            checks = doc.get("checks", {})
            entry["citedChecks"] = {n: checks.get(n) is True for n in names}
            hashes = {}
            for src, digest in sorted(doc.get("sourceSha256", {}).items()):
                p = os.path.join(REPOSITORY_ROOT, src)
                hashes[src] = os.path.exists(p) and sha256_file(p) == digest
            entry["sourceHashesCurrent"] = hashes
            entry["producer"] = doc.get("producer")
            entry["ok"] = all(entry["citedChecks"].values()) and all(hashes.values()) and bool(hashes)
        else:
            entry["ok"] = False
        ok = ok and entry["ok"]
        out[rel] = entry
    out["statement"] = ("Grassmann-side statements not recomputed here at every curved point (curved EL at the Stage-1 "
                        "points G1/G2, local spin invariance, the canonical momentum, Krein signatures, the Stage-2 and "
                        "Stage-4 reductions) are cited from the committed Python reports; each cited check is true and "
                        "every source file recorded in the report still has the recorded SHA-256. The positivity of the "
                        "normal-ordered Grassmann Hamiltonian (Stage 1 section 10.7) is a derivation, not a machine check.")
    rec.check("citation_pythonStage1to4ReportsMatchSources", ok, out)


# ---------------------------------------------------------------------------
# 15. S5_agreesWithWolfram: compare every exported number/matrix/formula with the values derived here
# ---------------------------------------------------------------------------

def parse_plain_formula(text, symbols):
    from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application, parse_expr,
                                            standard_transformations)
    t = text.replace("U'(S)", "U1").replace("U(S)", "U0").replace("U'", "U1").replace("lambda", "lam")
    t = re.sub(r"(?<![A-Za-z_])U(?![A-Za-z_0-9'(])", "U0", t)
    t = re.sub(r"k_(\d)", r"k\1", t)
    return parse_expr(t, local_dict=symbols, transformations=standard_transformations + (implicit_multiplication_application, convert_xor))


def parse_mathematica_trig(text, y):
    t = text.replace("Cos[", "cos(").replace("Sin[", "sin(").replace("]", ")")
    return sp.sympify(t, locals={"y": y, "cos": sp.cos, "sin": sp.sin})


def gq_list(rows):
    return [(Fraction(a), Fraction(b)) for a, b in rows]


def gq_matrix_fraction(rows):
    return ([[Fraction(e[0]) for e in row] for row in rows], [[Fraction(e[1]) for e in row] for row in rows])


G2_WOLFRAM_POINTS = ({"w": Fraction(1, 2), "H": Fraction(2, 3), "A1": Fraction(3, 7)},
                     {"w": Fraction(2, 3), "H": Fraction(1, 5), "A1": Fraction(-4, 9)},
                     {"w": Fraction(3, 4), "H": Fraction(5, 7), "A1": Fraction(6, 5)})   # Stage-1 G2 test points (a4' = A1)


def compare_with_wolfram(alg, own, theory_path, report_path):
    res = {}
    not_comparable = {}

    def add(name, value):
        res[name] = bool(value)

    th = None
    if theory_path and os.path.exists(theory_path):
        with open(theory_path, "r", encoding="utf-8") as handle:
            th = json.load(handle)
    wr = None
    if report_path and os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as handle:
            wr = json.load(handle)
    if th is not None:
        cs = th["commutingFieldSpecifics"]
        add("theory.B", EX.cequal(gq_matrix_fraction(cs["B"]), alg.B))
        add("theory.C", EX.equal([[Fraction(v) for v in row] for row in cs["C"]], alg.C))
        add("theory.gamma8", EX.equal([[Fraction(v) for v in row] for row in cs["gamma8"]], alg.g8))
        add("theory.Cgamma4EqualsIB", cs["Cgamma4EqualsIB"] is True and own["leadFacts"]["Cgamma4EqualsIB"])
        ci = cs["chargeIndefinite"]
        for key in ("Plus", "Minus"):
            v = gq_list(ci["Psi" + key])
            j4 = cvec_dot(v, alg.B, v)
            add("theory.chargeIndefinite.%s" % key, j4[1] == 0 and qstr(j4[0]) == qstr(Fraction(ci["J4" + key]))
                and qstr(cnorm2(v)) == qstr(Fraction(ci["norm" + key])))
        eu = cs["energyUnboundedBelow"]
        m1 = Fraction(1)
        kspace = [Fraction(v) for v in (1, 1, 2, 3, 0, 0, 0, 0)]
        for idx, w in enumerate(eu["freePlaneWaves"]):
            u = gq_list(w["u"])
            omega = Fraction(w["omega"])
            kcov = list(kspace)
            kcov[TIME] = -omega
            solves = all(a == 0 and b == 0 for a, b in dirac_residual(alg, u, kcov, m1))
            T, _, _ = plane_wave_T(alg, u, kcov, m1, lambda x: Fraction(0))
            j4 = cvec_dot(u, alg.B, u)
            Bu = cmat_vec(alg.B, u)
            krein = w["kreinSign"]
            eig = all(a == krein * c and b == krein * d_ for (a, b), (c, d_) in zip(Bu, u))
            add("theory.freePlaneWave%d" % idx, solves and eig and T[TIME][TIME] == (Fraction(w["rho"]), 0) and
                j4 == (Fraction(w["J4"]), 0) and cnorm2(u) == Fraction(w["norm"]) and w["solves"] is True and w["dim"] == 4
                and all(x["dimJoint"] == 4 for x in own["energy"]["freePlaneWaves"]))
        add("theory.gordonIdentity", eu["gordonIdentity"] is True and own["energy"]["gordonIdentity"])
        mine_h = {e["S"]: e for e in own["energy"]["homogeneousNegativeLambda"]}
        for e in eu["homogeneousNegativeLambda"]:
            s = qstr(Fraction(e["S"]))
            add("theory.homogeneousNegativeLambda.S%s" % s, s in mine_h and mine_h[s]["rho"] == qstr(Fraction(e["rho"]))
                and qstr(Fraction(e["lambda"])) == mine_h[s]["lambda"])
        mine_f = {e["M"]: e for e in own["energy"]["selfConsistentPlaneWavesPositiveLambda"]}
        for e in eu["selfConsistentPlaneWavesPositiveLambda"]:
            M = qstr(Fraction(e["M"]))
            add("theory.selfConsistentPlaneWave.M%s" % M, M in mine_f and all(mine_f[M][k] == qstr(Fraction(e[k])) for k in ("k", "S", "rho")))
        pr = th["primordial"]["staticSourceExample"]
        mine_s = own["staticSource"]
        add("theory.staticSource.parameters", all(qstr(Fraction(pr[k])) == v for k, v in
                                                  (("m", "-30"), ("lambda", "125/6"), ("S", mine_s["S"]), ("Meff", mine_s["Meff"]),
                                                   ("omega", mine_s["omega"]), ("vDaggerCv", mine_s["vDaggerCv"]))))
        add("theory.staticSource.values", all(qstr(Fraction(pr[k])) == mine_s[k] for k in ("rho", "p", "w", "KE_L", "PE_L")))
        add("theory.staticSource.einstein", "diag(15,15,15,15,21,15,15,15)" in pr["einstein"] and mine_s["einsteinEqualsKappaT64"])
        st = th["static"]
        labels = own["staticLabels"]
        add("theory.blockKreinSigns", [(b["block"], b["j"], b["s2"], b["kreinSign"]) for b in st["blockKreinSigns"]] ==
            [(i, j, s2, j * s2) for i, (j, s2, s3) in enumerate(labels)])
        y = sp.Symbol("y", real=True)
        mine_box = {bm["block"]: bm for bm in own["box"]}
        for bm in st["boxModes"]:
            mb = mine_box.get(bm["block"])
            theirs = parse_mathematica_trig(bm["rhoTimesW6"], y)
            add("theory.boxMode.block%d" % bm["block"], mb is not None and szero(theirs - mb["_rho"].subs(sp.Symbol("y", real=True), y))
                and bm["kreinSign"] == mb["kreinSign"])
        g4 = th["testGeometries"]["G4"]
        E0 = g4_frame_data(1)[0]
        add("theory.G4.E0", [[int(v) for v in row] for row in E0] == g4["E0"])
        add("theory.G4.nonzeroOffDiagonal", sum(1 for i in range(8) for j in range(8) if i != j and E0[i][j] != 0) == g4["nonzeroOffDiagonalOfE0"])
        add("theory.G4.gUpper44", own["G4"]["gUpper44"] == qstr(Fraction(g4["gUpper44"])))
        add("theory.G4.scalarCurvature", own["G4"]["scalarCurvature"] == qstr(Fraction(g4["scalarCurvature"])))
        vv = th["exactValues"]["vielbeinVariationG1p1"]
        if own.get("G1p1_offShellTlower") is not None:
            add("theory.vielbeinVariationG1p1.T", own["G1p1_offShellTlower"] == [[qstr(Fraction(v)) for v in row] for row in vv["offShellTlowerExact"]])
            add("theory.vielbeinVariationG1p1.S", own["G1p1_offShellS"] == qstr(Fraction(vv["offShellS"])) and vv["seeds"] == [61100, 61150])
        else:
            not_comparable["theory.vielbeinVariationG1p1"] = "EMT family not run"
        hg = th["exactValues"]["homogeneousG3"]
        if own.get("homogeneousG3"):
            for k, lab in enumerate(("q1", "q2", "q3"), start=1):
                mine = own["homogeneousG3"]["G3" + lab]["quartic"]
                theirs = hg["G3t%d" % k]
                add("theory.homogeneousG3.t%d" % k, all(mine[key] == qstr(Fraction(theirs[key])) for key in
                                                        ("rhoExact", "pExact", "KE_LExact", "PE_LExact", "wExact", "SExact"))
                    and own["homogeneousG3"]["G3" + lab]["x4"] == qstr(Fraction(theirs["x4"])))
        else:
            not_comparable["theory.homogeneousG3"] = "EMT family not run"
        # formulas
        m_, S_, lam_, U0, U1 = sp.symbols("m S lam U0 U1")
        syms = {"m": m_, "S": S_, "lam": lam_, "U0": U0, "U1": U1}
        trace_text = th["emt"]["trace"].split("=", 1)[1].replace("on shell", "")
        add("formula.trace", sp.simplify(parse_plain_formula(trace_text, syms) - (-m_ * S_ + 7 * S_ * U1 - 8 * U0)) == 0)
        hom = th["energySplits"]["homogeneous"]
        pieces = {"rho": (r"rho = ([^,]+),", m_ * S_ + U0), "p": (r"p_\(i\) = (.+?) \(all", S_ * U1 - U0),
                  "KE_L": (r"KE_L = (.+?), PE_L", S_ * (m_ + U1) / 2), "PE_L": (r"PE_L = (.+?), KE_H", (m_ * S_ + 2 * U0 - S_ * U1) / 2),
                  "w": (r"w = (.+?) = \(KE_L", (S_ * U1 - U0) / (m_ * S_ + U0))}
        for key, (pattern, mine) in pieces.items():
            mt = re.search(pattern, hom)
            add("formula.homogeneous.%s" % key, mt is not None and sp.simplify(parse_plain_formula(mt.group(1), syms) - mine) == 0)
        mt = re.search(r"w = (lambda S/\(2m \+ lambda S\))", th["energySplits"]["freeAndDefault"])
        add("formula.defaultW", mt is not None and sp.simplify(parse_plain_formula(mt.group(1), syms) - (lam_ * S_ ** 2 / 2) / (m_ * S_ + lam_ * S_ ** 2 / 2)) == 0)
        ks = sp.symbols("k0:8")
        ksyms = dict(syms, **{"k%d" % i: ks[i] for i in range(8)})
        mt = re.search(r"flat: (.+?) = m\^2", th["lagrangian"]["dispersion"])
        add("formula.dispersion", mt is not None and sp.simplify(parse_plain_formula(mt.group(1), ksyms) - (-sum(ETA[a] * ks[a] ** 2 for a in range(8)))) == 0
            and own["dispersion"]["productIdentity"])
        mt = re.findall(r"Psibar Psi = (-?\d+), \+?(-?\d+), (-?\d+) on e_0\+e_4, e_8\+e_12, e_0\+i e_4", th["lagrangian"]["massTerm"])
        mm = own["massTerm"]
        add("formula.massTermValues", bool(mt) and [str(int(x)) for x in mt[0]] == [mm["e0+e4"]["S"], mm["e8+e12"]["S"], mm["e0+ie4"]["S"]])
        add("formula.blockODE", "chi' = [M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi" in th["fieldEquations"]["staticReduced"]
            and own["blockODE"])
        add("formula.realRestrictionCommuting", "2 sqrt|g| C (gamma^mu D_mu Psi + H M Psi)" in th["realRestriction"]["commuting"]
            and own["realRestrictionOK"])
        add("formula.emtDefinition", th["emt"]["tex"].startswith("T_{\\mu\\nu}=-\\tfrac14") and own["emtVariationOK"])
        statements = {
            "statement.fieldEquationsEL": (th["fieldEquations"]["EL"], ["sqrt|g| C (gamma^mu D_mu Psi - (m + U'(S)) Psi)",
                                           "-sqrt|g| ((D_mu Psibar) gamma^mu + (m + U'(S)) Psibar)"], own["checks"].get("S5_EL_commutingCurved")),
            "statement.primordialComponents": (th["fieldEquations"]["primordialComponents"],
                                               ["tan z gamma^0 d_0 Psi", "3 H gamma^0 Psi = (m + U'(S)) Psi"],
                                               own["checks"].get("S5_primordial_ELcommuting")),
            "statement.current": (th["emt"]["current"], ["J^4 = Psi^dagger B Psi"], own["checks"].get("S5_charge_indefinite")),
            "statement.conservation": (th["emt"]["conservation"], ["nabla^mu T_{mu nu} = 0 on shell"],
                                       own["checks"].get("S5_EMT_conservationOnShell") and own["checks"].get("S5_EMT_generalSmoothU")),
            "statement.observerIdentity": (th["energySplits"]["identity"], ["rho = T_44 = KE_H + PE_H = K_4 - L_s"],
                                           own["checks"].get("S5_EMT_observerSplitGaussianNormal")),
            "statement.relationToL1": (th["realRestriction"]["relationToL1"], ["L1 = sqrt|g| [K_R[X] + K_R[Y] - m (S_X + S_Y) - U(S_X + S_Y)]",
                                       "Psibar Psi = 2 i rho^T C iota"], own["checks"].get("S5_realRestriction_relationToL1")
                                       and own["checks"].get("S5_realRestriction_grassmannComplexDecomposition")),
            "statement.grassmannRealRestriction": (th["realRestriction"]["grassmann"], ["Psi^T C Psi = 0 identically"],
                                                   own["checks"].get("S5_realRestriction_grassmannCurvedTrivial")),
            "statement.classicalVersusKohnSham": (th["static"]["classicalVersusKohnSham"], ["(j s2) T_{mu nu}^{KS one-body}"],
                                                  own["checks"].get("S5_static_classicalModeIsKreinWeightedKS")),
            "statement.meanFieldEMT": (th["static"]["meanFieldEMT"], ["rho^(1) = eps n - (M_eff - m) s - v_v n",
                                       "p_y^(1) = eps n - m s - kappa k t", "p_(1)^(1) = kappa k t + (M_eff - m) s + v_v n",
                                       "p_(2,3)^(1) = p_(5,6,7)^(1) = (M_eff - m) s + v_v n"], own["checks"].get("S5_static_meanFieldOneBodyEMT")),
            "statement.stage2Homogeneous": (th["primordial"]["stage2Homogeneous"]["statement"],
                                            ["rho = -T^4_4 = m S + U, p_(i) = T^i_i = S U' - U"], own["checks"].get("S5_primordial_homogeneousState")),
            "statement.reality": (th["lagrangian"]["reality"], ["K^mu = (1/2) sqrt|g| C gamma^mu"],
                                  own["checks"].get("S5_lagrangian_coefficientHermiticity")),
            "statement.vielbeinVariation": (th["emt"]["vielbeinVariation"], ["sqrt|g| T^{mu nu} off shell"],
                                            own["checks"].get("S5_EMT_vielbeinVariation")),
        }
        for key, (text, substrings, own_ok) in statements.items():
            add(key, all(sub in text for sub in substrings) and bool(own_ok))
        add("definitions.randomFieldDataReproduced", res.get("theory.vielbeinVariationG1p1.T", False)
            and all(res.get("theory.homogeneousG3.t%d" % k, False) for k in (1, 2, 3)))
        not_comparable["theory.conventions/fields/difference/operatorVersion/energyStatement"] =             "prose without numbers (read against the binding conventions; no exact comparison possible)"
    else:
        not_comparable["theory"] = "dirac16complex00-theory.json absent"
    if wr is not None:
        meas = wr.get("measurements", {})
        conn = meas.get("connection", {})
        for lab, mine in own.get("connection", {}).items():
            if lab in conn:
                w = conn[lab]
                dec = mine["scalarCurvature"]["decimal"] if isinstance(mine["scalarCurvature"], dict) else None
                add("report.connection.%s" % lab, w["gammaOmegaNonzeroEntries"] == mine["gammaOmegaNonzeroEntries"]
                    and [w["lichnerowiczC"]] == mine["lichnerowiczC"] and (dec is None or w["scalarCurvatureDecimal"][:14] == dec[:14]))
        for k, pt in enumerate(G2_WOLFRAM_POINTS, start=1):
            lab = "G2p%d" % k
            if lab in conn:
                R = 6 * pt["H"] ** 2 * (pt["A1"] ** 2 - 7)
                with mpmath.workdps(30):
                    dec = mpmath.nstr(mpmath.mpf(R.numerator) / R.denominator, 17)
                add("report.connection.%s.scalarCurvature" % lab, conn[lab]["scalarCurvatureDecimal"][:12] == dec[:12]
                    and conn[lab]["gammaOmegaNonzeroEntries"] == 16)
        if "G4p1" in conn:
            add("report.connection.G4p1.scalarCurvature", conn["G4p1"]["scalarCurvatureDecimal"].rstrip(".") == own["G4"]["scalarCurvature"])
        elc = meas.get("EL.commutingCurved", {})
        for lab, mine in own.get("el", {}).items():
            key = lab if lab in elc else ("G2p1" if lab == "G2" else None)
            if key in elc:
                add("report.EL.LTerms.%s" % lab, elc[key]["LTerms"] == mine["LTerms"])
        gc = meas.get("realRestriction.grassmannCurved", {})
        if gc and own.get("grassmannCurved"):
            add("report.grassmannCurved.LgMonomials", gc["LgMonomials"] == own["grassmannCurved"]["LgMonomials"] and gc["HM"] == "2/3")
        mg = meas.get("massTerm.grassmann", {})
        if mg:
            counts = own["grassmannMass"]["powerMonomialCounts"]
            add("report.massTerm.grassmann", [mg["SMonomials"], mg["S2Monomials"], mg["S3Monomials"]] == counts[:3])
        props = meas.get("EMT.properties", {})
        params = [(Fraction(3, 7), Fraction(5, 11)), (Fraction(-2, 5), Fraction(7, 13)), (Fraction(5, 9), Fraction(-3, 8))]
        order = ["G1p1", "G1p2", "G1p3", "G2p1", "G2p2", "G2p3"]
        for k, lab in enumerate(order, start=1):
            if lab in props and "traceOnShellValue" in props[lab]:
                m, lam = params[(k - 1) % 3]
                data = lcg_field_data(62000 + 100 * k + 10)
                S0 = sum((data[3][a] * alg.C[a][b] * data[0][b] for a in range(16) for b in range(16)), Fraction(0))
                add("report.EMT.traceOnShellValue.%s" % lab, qstr(-m * S0 + 3 * lam * S0 * S0) == qstr(Fraction(props[lab]["traceOnShellValue"])))
        fx = meas.get("fixture.entriesCompared", {})
        if fx:
            add("report.fixture", all(fx.get(k) is True for k in ("gamma", "C", "chirality", "B", "S")) and fx.get("SCount") == 28
                and own["fixture"]["SCount"] == 28)
        sb = meas.get("static.blocksAndModes", {})
        mine_blocks = {p["block"]: p for p in own.get("staticPer", [])}
        for b in sb.get("blocks", []):
            if b["block"] in mine_blocks:
                p = mine_blocks[b["block"]]
                add("report.static.block%d" % b["block"], b["kreinSign"] == p["kreinSign"] and b["classicalEqualsKreinSignTimesKS64"] is True
                    and p["classicalEqualsKreinSignTimesKS36"] and b["K4_KS_equals_eps_n"] is True and p["K4_KS_equals_eps_n"])
        wchecks = wr.get("checks", {})
        res["report.allWolframChecksTrue"] = bool(wchecks) and all(v is True for v in wchecks.values())
        mapping = {}
        for name in wchecks:
            mine = "S5_" + name[len("C00_"):] if name.startswith("C00_") else None
            mapping[name] = mine if mine in own["checks"] else None
        agree = {n: (own["checks"][m] == wchecks[n]) for n, m in mapping.items() if m is not None}
        res["report.verdictsAgreeWherePaired"] = all(agree.values()) and len(agree) >= 30
        not_comparable["report.unpairedWolframChecks"] = sorted(n for n, m in mapping.items() if m is None)
        res_pairs = len(agree)
    else:
        not_comparable["report"] = "wolfram-dirac16complex00-report.json absent"
        res_pairs = 0
    return res, not_comparable, res_pairs


# ---------------------------------------------------------------------------
# 16. runner, report, command line
# ---------------------------------------------------------------------------

def source_frequency(alg, v):
    Meff = STATIC_SOURCE["m"] + STATIC_SOURCE["lambda"] * STATIC_SOURCE["S"]
    N = EX.scale(-1, EX.matmul(alg.gam[4], EX.sub(EX.scale(Meff, EX.identity(16)), EX.scale(3, alg.gam[0]))))
    Nv = cmat_vec((N, EX.zeros(16)), v)
    for cand in (Fraction(4), Fraction(-4)):
        if all(a == -cand * vi and b == cand * vr for (a, b), (vr, vi) in zip(Nv, v)):
            return cand
    return None


def check_g4_generic(geos, rec):
    E0 = g4_frame_data(1)[0]
    eta = EX.eta()
    gm = EX.matmul_many(E0, eta, EX.transpose(E0))
    geo = geos.g4(1)
    dom = geo.dom
    d = {"detE0": qstr(EX.determinant(E0)), "detG": qstr(EX.determinant(gm)),
         "inverseMetricInteger": all(v.denominator == 1 for row in EX.inverse(gm) for v in row),
         "nonzeroOffDiagonalOfE0": sum(1 for i in range(8) for j in range(8) if i != j and E0[i][j] != 0),
         "signature": list(EX.symmetric_signature(gm)), "gUpper44": exact_str(dom, geo.ginv.value()[TIME, TIME]),
         "scalarCurvature": exact_str(dom, geo.Rscalar)}
    ok = (d["detE0"] == "1" and d["detG"] == "1" and d["inverseMetricInteger"] and d["nonzeroOffDiagonalOfE0"] > 20
          and d["signature"] == [4, 4, 0] and d["gUpper44"] != "0" and d["scalarCurvature"] != "0")
    rec.check("geometry_G4Generic", ok, d)
    return d


def jsonable(value):
    if isinstance(value, bool) or value is None or isinstance(value, (int, str)):
        return value
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, Fraction) or type(value).__name__ == "mpq":
        return qstr(value)
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items() if not str(k).startswith("_")}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, np.ndarray):
        return [jsonable(v) for v in value.tolist()]
    return str(value)


def run_checks(families=FAMILIES, quick=False, theory_path=DEFAULT_THEORY, report_path=DEFAULT_WOLFRAM_REPORT,
               fixture_path=DEFAULT_FIXTURE, log=None):
    rec = Recorder()
    exceptions = {}
    timings = {}
    own = {}
    alg = Algebra(fixture_path)
    geos = Geometries()
    theory = None
    if theory_path and os.path.exists(theory_path):
        with open(theory_path, "r", encoding="utf-8") as handle:
            theory = json.load(handle)

    def guarded(name, fn):
        start = time.time()
        try:
            fn()
        except Exception as error:  # noqa: BLE001
            import traceback
            exceptions[name] = "%s: %s | %s" % (type(error).__name__, error, traceback.format_exc().splitlines()[-3:])
        timings[name] = round(time.time() - start, 3)
        if log:
            log("family %s done in %.1f s" % (name, timings[name]))

    if "algebra" in families:
        guarded("algebra", lambda: check_algebra(alg, rec))
    if "lagrangian" in families:
        guarded("lagrangian", lambda: run_lagrangian(alg, geos, rec, quick))
    if "realRestriction" in families:
        def rr():
            run_real_restriction(geos, rec, quick)
            m = rec.measurements
            rel = m["realRestriction_relationToL1"]
            rec.check("realRestriction_commutingFlatDecomposition", rel["flat"]["decomposition"] and rel["flat"]["imaginaryPartZero"],
                      {"statement": "commuting Psi = X + i Y: Psibar Psi = X^T C X + Y^T C Y and the symmetrized kinetic term "
                                    "= X^T C gamma^mu d_mu X + Y^T C gamma^mu d_mu Y exactly (flat; symbolic jets)",
                       "flat": rel["flat"]})
            cn = m["realRestriction_commutingNonTrivial"]
            rec.check("realRestriction_commutingNotebookContraction",
                      all(v["notebookContraction"]["EL"] for k, v in cn.items() if "notebookContraction" in v),
                      {k: v["notebookContraction"] for k, v in cn.items() if "notebookContraction" in v})
            own["realRestrictionOK"] = rec.checks["S5_realRestriction_commutingNonTrivial"]
            own["grassmannCurved"] = m["realRestriction_grassmannCurvedTrivial"]["canonical"]
        guarded("realRestriction", rr)
    if "connection" in families:
        guarded("connection", lambda: own.__setitem__("connection", run_connection(geos, rec, quick)))
    if "EL" in families:
        def el():
            run_el(geos, rec, quick)
            own["el"] = rec.measurements["EL_commutingCurved"]
        guarded("EL", el)
    if "EMT" in families:
        def emt():
            own.update(run_emt(geos, rec, quick))
            own["G4"] = check_g4_generic(geos, rec)
            own["emtVariationOK"] = rec.checks["S5_EMT_vielbeinVariation"]
        guarded("EMT", emt)
    if "specifics" in families:
        def spec():
            ok, d = check_charge_indefinite(alg)
            rec.check("charge_indefinite", ok, d)
            ok, d = check_energy_unbounded(alg)
            rec.check("energy_unboundedBelow", ok, d)
            own["energy"] = d
        guarded("specifics", spec)
    v_source = static_source_vector(theory) or [(Fraction(a), Fraction(b)) for a, b in
                                               ((1, 0), (0, 3), (0, 0), (0, 0), (1, 0), (0, -3), (0, 0), (0, 0),
                                                (-3, 0), (0, -1), (0, 0), (0, 0), (-3, 0), (0, 1), (0, 0), (0, 0))]
    if "primordial" in families:
        guarded("primordial", lambda: own.__setitem__("staticSource", run_primordial(alg, geos, rec, quick, theory)))
    if "static" in families:
        def static():
            out = run_static(alg, rec, quick, theory, source_frequency(alg, v_source), v_source)
            own["box"] = out["box"]
            own["staticLabels"] = out["labels"]
            own["staticPer"] = out["per"]
            own["blockODE"] = rec.measurements["static_blocksFromStage4Theory"]["blockODE"]
        guarded("static", static)
    if "citations" in families:
        guarded("citations", lambda: run_citations(rec))
    inputs = {}
    if fixture_path and os.path.exists(fixture_path):
        inputs[relative(fixture_path)] = sha256_file(fixture_path)
    if os.path.exists(KS_THEORY):
        inputs[relative(KS_THEORY)] = sha256_file(KS_THEORY)
    have_wolfram = (theory_path and os.path.exists(theory_path)) or (report_path and os.path.exists(report_path))
    if have_wolfram and set(families) == set(FAMILIES) and not exceptions:
        start = time.time()
        try:
            m = rec.measurements
            own["leadFacts"] = m["algebra_leadFacts"]
            own["dispersion"] = m["massTerm_dispersionFlat"]
            own["massTerm"] = m["massTerm_commutingExplicitSpinors"]
            own["grassmannMass"] = m["massTerm_grassmannNonzero"]
            own["fixture"] = m["fixture_matchesContractConstruction"]
            own["checks"] = dict(rec.checks, S5_internal_noException=True)
            res, nc, pairs = compare_with_wolfram(alg, own, theory_path, report_path)
            rec.checks[WOLFRAM_CHECK] = bool(res) and all(res.values())
            rec.measurements["agreesWithWolfram"] = {"items": res, "itemCount": len(res),
                                                    "failedItems": sorted(k for k, v in res.items() if not v),
                                                    "notComparable": nc, "pairedVerdicts": pairs}
            rec.measurements["wolframAgreement"] = "compared"
            for p in (theory_path, report_path):
                if p and os.path.exists(p):
                    inputs[relative(p)] = sha256_file(p)
        except Exception as error:  # noqa: BLE001
            import traceback
            exceptions["wolfram"] = "%s: %s | %s" % (type(error).__name__, error, traceback.format_exc().splitlines()[-3:])
            rec.checks[WOLFRAM_CHECK] = False
            rec.measurements["wolframAgreement"] = "error"
        timings["wolfram"] = round(time.time() - start, 3)
    elif have_wolfram:
        rec.measurements["wolframAgreement"] = "not-run (requires all families and no exception)"
    else:
        rec.measurements["wolframAgreement"] = "not-run"
        rec.measurements["wolframTheoryExpectedAt"] = relative(theory_path) if theory_path else None
    rec.checks["S5_internal_noException"] = not exceptions
    if exceptions:
        rec.measurements["exceptions"] = exceptions
    rec.measurements["families"] = list(families)
    rec.measurements["quick"] = bool(quick)
    rec.measurements["timingsNote"] = "timings are printed, not stored (deterministic report)"
    rec.measurements["conventions"] = CONVENTIONS
    return rec.checks, rec.measurements, inputs, timings


def build_report(checks, measurements, inputs):
    sources = {rel: sha256_file(os.path.join(REPOSITORY_ROOT, rel)) for rel in SOURCE_FILES}
    return {"schemaVersion": 1, "producer": PRODUCER, "checks": checks, "measurements": jsonable(measurements),
            "sourceSha256": sources, "inputSha256": dict(sorted(inputs.items()))}


def canonical_json_bytes(document):
    text = json.dumps(document, indent=2, ensure_ascii=True) + "\n"
    return text.replace("\r\n", "\n").encode("utf-8")


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, str)):
        return str(value)
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def report_lines(report, compact=True):
    lines = ["check_%s=%s" % (k, "true" if v else "false") for k, v in report["checks"].items()]
    for key, value in report["measurements"].items():
        text = format_value(value)
        if compact and len(text) > 400:
            text = text[:400] + "...(truncated; full value in the JSON report)"
        lines.append("measurement_%s=%s" % (key, text))
    failed = sum(1 for v in report["checks"].values() if not v)
    lines.append("check_count=%d" % len(report["checks"]))
    lines.append("failed_check_count=%d" % failed)
    return lines, failed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--theory", default=DEFAULT_THEORY, help="Wolfram dirac16complex00-theory.json (compared when present)")
    parser.add_argument("--wolfram-report", default=DEFAULT_WOLFRAM_REPORT, help="Wolfram report (compared when present)")
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--families", default=",".join(FAMILIES), help="comma-separated subset of %s" % ",".join(FAMILIES))
    parser.add_argument("--quick", action="store_true", help="fewer points/blocks/directions (tests)")
    parser.add_argument("--no-write", action="store_true")
    parser.add_argument("--full-measurements", action="store_true", help="print measurements untruncated")
    arguments = parser.parse_args(argv)
    families = [f.strip() for f in arguments.families.split(",") if f.strip()]
    unknown = [f for f in families if f not in FAMILIES]
    if unknown:
        print("error=unknown families %s" % ",".join(unknown))
        return 2
    started = time.time()

    def log(message):
        print("progress=%s (%.0f s)" % (message, time.time() - started), flush=True)
    checks, measurements, inputs, timings = run_checks(families=families, quick=arguments.quick, theory_path=arguments.theory,
                                                       report_path=arguments.wolfram_report, fixture_path=arguments.fixture, log=log)
    report = build_report(checks, measurements, inputs)
    lines, failed = report_lines(report, compact=not arguments.full_measurements)
    for line in lines:
        print(line)
    for name, seconds in timings.items():
        print("timing_%s=%s" % (name, seconds))
    if not arguments.no_write:
        os.makedirs(os.path.dirname(os.path.abspath(arguments.output)), exist_ok=True)
        with open(arguments.output, "wb") as handle:
            handle.write(canonical_json_bytes(report))
        print("report=%s" % relative(arguments.output))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
