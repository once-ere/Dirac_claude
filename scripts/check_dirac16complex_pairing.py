#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent exact checker of the Stage-5 {+M, -M} pairing theorems T1, T2, T3 and of
the statistics (Wick) sign, for BOTH fields of STAGE5_SPEC:

  dirac16complex    anticommuting (Grassmann-odd) components, second quantised
  dirac16complex00  commuting (c-number) components, classical

(sympy + mpmath + the standard library; numpy only as the object-array container of
the Stage-1 jet engine).  Nothing produced by Wolfram is used as truth: the gamma
matrices are rebuilt from CONTRACT section 1 (scripts/check_dirac16complex_kohn_sham_theory.py,
Algebra) and only compared with the committed fixture; the curved geometries are
recomputed from vielbein jets (scripts/d16c_geometry_sympy.py); the Grassmann algebra is
scripts/grassmann_algebra.py; the Stage-4 block basis is rebuilt with exact
Gaussian-rational projectors (BlockReduction of the Stage-4 checker).  Only the final
family S5_pairingAgreesWithWolfram reads artifacts/dirac16complex/pair-creation/
pairing-theory.json and wolfram-pairing-report.json, and compares them with the
results derived here.

What is re-derived (families; every check is computed, none is asserted):
  algebra      gamma^8, C, B facts, the 456 odd bilinear matrices, Pin characters,
               the Krein sign u B u^dagger of the basis reflections.
  T1generic    L_{m,lam}[g8 Psi] = -L_{-m,-lam}[Psi], the field equation and its
               conjugate, the Euler-Lagrange expressions derived from L, the current and
               all 36 EMT components as POLYNOMIAL identities in independent generic
               symbols (inverse vielbein e_a^mu, a general spin-algebra connection
               Omega_mu = W_{mu,bc} gamma^b gamma^c, sqrt|g|, g_{mu nu}, e_{mu a}, the field
               jets and their derivatives): every gravitational field, off shell,
               commuting components (dirac16complex00).
  T1grassmann  the same identities with Grassmann-odd components (dirac16complex):
               288 (Lagrangian) / 1440 (Euler-Lagrange) odd generators, exact rational
               geometric coefficients.
  T1jets       exact jets of the general non-diagonal Stage-1 vielbein G1: L, EMT (64),
               field equations, current, on-shell images, conservation of both EMTs,
               the pair sums, and the vielbein sign flip e -> -e.
  T1primordial the Stage-2 primordial field (notebook chart, arbitrary a4(t)).
  T1krein      an exact Krein-Fock model (4 rest modes, the filled sea): the canonical
               anticommutator -B of the image field, H -> -H, Q -> -Q as operators, the
               image field's own generators -H[Psi_-; -m] = +H, -Q[Psi_-] = +Q (the same
               quantum system, not a second universe), and the independently quantised
               -m theory.
  T2frame      Pin(4,4) reflections u (8 basis vectors, general rational unit vectors),
               twisted and untwisted frame lifts, exact G1 jets.
  T2z2         the Z2 static primordial field: Psi'(y) = gamma^0 Psi(-y) maps m(y) to
               -m(-y) with the same lambda, EMT pull-back, P_B = i gamma^0 gamma^8.
  T3block      block form of gamma^8, gamma^1, gamma^0 on the Stage-4 basis, block ODE and
               Hamiltonian maps, parity and bag boundary conditions, densities, potentials.
  T3ks         the Kohn-Sham functional and operator (both statistics, sg symbolic),
               exact k = 0 solutions of the +M, the transformed -M and the untransformed
               -M (control) problems, the zero-mode splitting.
  T3emt        the 16-component orbital EMT kernels in the static field, the gamma^8
               identity (64 components), standard rule (+T) and image rule (-T), and the
               Stage-4 block formulas.
  stat         the Wick sign: exact fermionic Fock space, exact bosonic thermal series,
               exact classical Gaussian moments, fixed-amplitude phases, the expectation
               rule, filled shell, uniform gas e_x = sg (lam/32)(n^2 + S^2), LDA potentials.
  totals       field-level and KS-level pair totals on explicit exact configurations.

Conventions (CONTRACT.md with errata section 11, STAGE4_SPEC.md sections 8-9,
STAGE5_SPEC.md): eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), gamma^a = [[0, taubar_a],[tau_a, 0]],
C = gamma^0 gamma^1 gamma^2 gamma^3, Psibar = Psi^dagger C, B = -i C gamma^4,
gamma^8 = gamma^0 ... gamma^7 = diag(-I8, +I8), Omega_mu = (1/8) omega_{mu ab}[gamma^a, gamma^b],
L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi
              - (lam/2)(Psibar Psi)^2 ],
T_{mu nu} = -(1/4)[Psibar gamma_mu D_nu Psi + (mu <-> nu) - (D_mu Psibar) gamma_nu Psi - (mu <-> nu)]
            + g_{mu nu} L/sqrt|g|,
j^mu = Psibar gamma^mu Psi; expectation rule <Psi^dagger X Psi> = u^dagger B X u;
statistics sign sg = -1 (dirac16complex), +1 (dirac16complex00).

Prints ``check_<name>=true|false``, ``measurement_<name>=...``, ``check_count``,
``failed_check_count``; exits nonzero on failure; writes
artifacts/dirac16complex/pair-creation/python-pairing-report.json
{schemaVersion, producer, checks, measurements, sourceSha256, inputSha256}.

Usage: python scripts/check_dirac16complex_pairing.py [--output PATH] [--theory PATH]
       [--wolfram-report PATH] [--fixture PATH] [--families a,b,...] [--quick] [--no-write]
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import random
import sys
import time
from fractions import Fraction

import mpmath
import numpy as np
import sympy as sp

SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIRECTORY not in sys.path:
    sys.path.insert(0, SCRIPT_DIRECTORY)

import check_dirac16complex_kohn_sham_theory as KS  # noqa: E402  (Stage-4 exact Python machinery, read only)
import d16c_geometry_sympy as G  # noqa: E402  (Stage-1 exact jet engine, read only)
import grassmann_algebra as GA  # noqa: E402  (Stage-1 Grassmann algebra, read only)

REPOSITORY_ROOT = os.path.dirname(SCRIPT_DIRECTORY)
PAIR_DIRECTORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "pair-creation")
DEFAULT_OUTPUT = os.path.join(PAIR_DIRECTORY, "python-pairing-report.json")
DEFAULT_THEORY = os.path.join(PAIR_DIRECTORY, "pairing-theory.json")
DEFAULT_WOLFRAM_REPORT = os.path.join(PAIR_DIRECTORY, "wolfram-pairing-report.json")
DEFAULT_FIXTURE = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "arbitrary-field",
                               "algebra-fixture.json")
STAGE4_THEORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "kohn-sham", "kohn-sham-theory.json")
PRODUCER = "scripts/check_dirac16complex_pairing.py"
SOURCE_FILES = ("scripts/check_dirac16complex_pairing.py",
                "scripts/check_dirac16complex_kohn_sham_theory.py",
                "scripts/d16c_geometry_sympy.py",
                "scripts/grassmann_algebra.py")
WOLFRAM_SOURCES = ("wolfram/Dirac16ComplexPairing.wl", "scripts/verify_dirac16complex_pairing.wls")

FAMILIES = ("algebra", "T1generic", "T1grassmann", "T1jets", "T1primordial", "T1krein", "T2frame",
            "T2z2", "T3block", "T3ks", "T3emt", "stat", "totals")
WOLFRAM_CHECK = "S5_pairingAgreesWithWolfram"

ETA = (1, 1, 1, 1, -1, -1, -1, -1)
COORDINATE_NAMES = ("y", "x1", "x2", "x3", "x4", "x5", "x6", "x7")
PAIRS = [(b, c) for b in range(8) for c in range(b + 1, 8)]          # the 28 index pairs b < c

CQ = KS.CQ
CQ_ZERO, CQ_ONE, CQ_I = KS.CQ_ZERO, KS.CQ_ONE, KS.CQ_I
mat_mul, mat_add, mat_sub, mat_scale = KS.mat_mul, KS.mat_add, KS.mat_sub, KS.mat_scale
mat_dagger, mat_transpose, mat_trace = KS.mat_dagger, KS.mat_transpose, KS.mat_trace
mat_eq, mat_is_zero, mat_eye, mat_zero = KS.mat_eq, KS.mat_is_zero, KS.mat_eye, KS.mat_zero
mat_commutator, mat_anticommutator = KS.mat_commutator, KS.mat_anticommutator
mat_to_sympy, vec_dot, mat_rank = KS.mat_to_sympy, KS.vec_dot, KS.mat_rank


# ---------------------------------------------------------------------------
# 0. Small exact helpers
# ---------------------------------------------------------------------------

def frac_str(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else "%d/%d" % (value.numerator, value.denominator)


def mat_neg(a):
    return [[-v for v in row] for row in a]


def mat_mul_many(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = mat_mul(out, m)
    return out


def mat_inverse_cq(a):
    """Exact Gauss-Jordan inverse over Q(i)."""
    n = len(a)
    rows = [list(a[i]) + [CQ_ONE if i == j else CQ_ZERO for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if not rows[r][col].is_zero()), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        inv = rows[col][col].inverse()
        rows[col] = [v * inv for v in rows[col]]
        for r in range(n):
            if r != col and not rows[r][col].is_zero():
                factor = rows[r][col]
                rows[r] = [rows[r][j] - factor * rows[col][j] for j in range(2 * n)]
    return [row[n:] for row in rows]


def real_matrix(a):
    """Fraction matrix of a real CQ matrix (raises if an entry is not real)."""
    out = []
    for row in a:
        if any(v.im != 0 for v in row):
            raise ValueError("matrix is not real")
        out.append([v.re for v in row])
    return out


def mat_apply(a, v):
    return [sum((a[i][l] * v[l] for l in range(len(v))), CQ_ZERO) for i in range(len(a))]


def vec_is_eigen(a, v, value):
    av = mat_apply(a, v)
    return all(av[i] == v[i] * value for i in range(len(v)))


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def relative(path):
    try:
        return os.path.relpath(path, REPOSITORY_ROOT).replace(os.sep, "/")
    except ValueError:
        return path.replace(os.sep, "/")


def jsonable(value):
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, Fraction):
        return frac_str(value)
    if isinstance(value, CQ):
        return value.to_pair()
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, str)) or value is None:
        return value
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return value
    if isinstance(value, mpmath.mpf):
        return float(value)
    if isinstance(value, sp.Basic):
        return str(value)
    return str(value)


class Recorder:
    """Named computed sub-checks and measurements of one family (prefix S5_<family>_)."""

    def __init__(self, family):
        self.family = family
        self.checks = {}
        self.measurements = {}

    def check(self, name, value, detail=None):
        value = bool(value)
        self.checks["S5_%s_%s" % (self.family, name)] = value
        if detail is not None:
            self.measurements[name] = detail
        return value

    def measure(self, name, value):
        self.measurements[name] = value
        return value

    def ok(self):
        return bool(self.checks) and all(self.checks.values())


# ---------------------------------------------------------------------------
# 1. Sparse commutative polynomials with exact rational coefficients
#    (generic-symbol identities: every variable is an independent symbol)
# ---------------------------------------------------------------------------

class VarTable:
    """Integer indices for named polynomial variables."""

    def __init__(self):
        self.names = []
        self.index = {}

    def var(self, name):
        if name not in self.index:
            self.index[name] = len(self.names)
            self.names.append(name)
        return self.index[name]

    def __len__(self):
        return len(self.names)


class SPoly:
    """sum_mono c_mono prod(vars); monomials are sorted tuples of variable indices
    (a repeated index is a power); coefficients are Fractions."""

    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {} if terms is None else terms

    def add_term(self, mono, c):
        if c == 0:
            return
        v = self.t.get(mono, 0) + c
        if v == 0:
            self.t.pop(mono, None)
        else:
            self.t[mono] = v

    def iadd(self, other, factor=1):
        for mono, c in other.t.items():
            self.add_term(mono, c * factor)
        return self

    def copy(self):
        return SPoly(dict(self.t))

    def __add__(self, other):
        return self.copy().iadd(other)

    def __sub__(self, other):
        return self.copy().iadd(other, -1)

    def __neg__(self):
        return SPoly({m: -c for m, c in self.t.items()})

    def scale(self, factor):
        factor = Fraction(factor)
        if factor == 0:
            return SPoly()
        return SPoly({m: c * factor for m, c in self.t.items()})

    def times_var(self, v):
        return SPoly({tuple(sorted(m + (v,))): c for m, c in self.t.items()})

    def mul(self, other):
        out = SPoly()
        for m1, c1 in self.t.items():
            for m2, c2 in other.t.items():
                out.add_term(tuple(sorted(m1 + m2)), c1 * c2)
        return out

    def is_zero(self):
        return not self.t

    def nterms(self):
        return len(self.t)

    def variables(self):
        s = set()
        for m in self.t:
            s.update(m)
        return s

    def signed(self, signs):
        """Substitute v -> signs[v] * v (signs: dict var -> +-1; missing = +1)."""
        out = {}
        for m, c in self.t.items():
            s = 1
            for v in m:
                s *= signs.get(v, 1)
            out[m] = c if s > 0 else -c
        return SPoly(out)

    def deriv(self, v):
        out = SPoly()
        for m, c in self.t.items():
            k = m.count(v)
            if k:
                lst = list(m)
                lst.remove(v)
                out.add_term(tuple(lst), c * k)
        return out

    def all_derivatives(self):
        """{v: dP/dv} for every variable v of P, in one pass."""
        out = {}
        for m, c in self.t.items():
            for pos, v in enumerate(m):
                if pos > 0 and m[pos - 1] == v:
                    continue
                k = m.count(v)
                lst = list(m)
                lst.remove(v)
                d = out.get(v)
                if d is None:
                    d = SPoly()
                    out[v] = d
                d.add_term(tuple(lst), c * k)
        return out

    def total_derivative(self, dmap):
        """Even derivation with v -> dmap[v] (variables missing from dmap are constants)."""
        out = SPoly()
        for m, c in self.t.items():
            for pos, v in enumerate(m):
                w = dmap.get(v)
                if w is None:
                    continue
                if pos > 0 and m[pos - 1] == v:
                    continue          # count each distinct variable once, with its multiplicity
                k = m.count(v)
                lst = list(m)
                lst.remove(v)
                lst.append(w)
                out.add_term(tuple(sorted(lst)), c * k)
        return out


def add_bilinear(poly, M, left, right, extra=(), coeff=1):
    """poly += coeff * sum_{ij} M_ij left_i right_j prod(extra) (M a real Fraction matrix)."""
    coeff = Fraction(coeff)
    for i, row in enumerate(M):
        li = left[i]
        for j, mij in enumerate(row):
            if mij != 0:
                poly.add_term(tuple(sorted((li, right[j]) + tuple(extra))), coeff * mij)
    return poly


# CHUNK-1-END

# ---------------------------------------------------------------------------
# 2. The exact 16x16 algebra (rebuilt from CONTRACT section 1) and family "algebra"
# ---------------------------------------------------------------------------

class PairAlgebra:
    """gamma^a, C, B, gamma^8 and the products used below, exact (CQ and real Fraction forms)."""

    def __init__(self, fixture_path=DEFAULT_FIXTURE):
        alg = KS.Algebra(fixture_path)
        self.alg = alg
        g = alg.gamma
        self.gamma = g
        self.C = alg.C
        self.B = alg.B
        self.BC = alg.BC
        self.g8 = alg.gamma8
        self.I16 = alg.I16
        self.fixture_agreement = alg.fixture_agreement
        self.diagonal_g8 = all(self.g8[i][l].is_zero() for i in range(16) for l in range(16) if i != l)
        self.chi = [int(self.g8[i][i].re) for i in range(16)]
        self.biv = {bc: mat_mul(g[bc[0]], g[bc[1]]) for bc in PAIRS}
        self.S = {bc: mat_scale(self.biv[bc], Fraction(1, 2)) for bc in PAIRS}      # S^{bc} = gamma^b gamma^c / 2
        self.Cg = [mat_mul(self.C, g[a]) for a in range(8)]
        self.g_bc = {(a, bc): mat_mul(g[a], self.biv[bc]) for a in range(8) for bc in PAIRS}
        self.bc_g = {(bc, a): mat_mul(self.biv[bc], g[a]) for a in range(8) for bc in PAIRS}
        # real Fraction forms (every one of these matrices is real)
        self.R = {"C": real_matrix(self.C), "g8": real_matrix(self.g8)}
        self.Rg = [real_matrix(m) for m in g]
        self.RCg = [real_matrix(m) for m in self.Cg]
        self.Rg_bc = {k: real_matrix(m) for k, m in self.g_bc.items()}
        self.RC_g_bc = {k: real_matrix(mat_mul(self.C, m)) for k, m in self.g_bc.items()}
        self.RC_bc_g = {k: real_matrix(mat_mul(self.C, m)) for k, m in self.bc_g.items()}
        self.RC_anti = {}
        for a in range(8):
            for bc in PAIRS:
                m = mat_add(mat_mul(self.C, self.g_bc[(a, bc)]), mat_mul(self.C, self.bc_g[(bc, a)]))
                self.RC_anti[(a, bc)] = real_matrix(m)            # C {gamma^a, gamma^b gamma^c}

    def unit_vector(self, v):
        """u = v_a gamma^a (CQ matrix) for a rational coefficient vector v."""
        out = mat_zero(16)
        for a in range(8):
            if v[a] != 0:
                out = mat_add(out, mat_scale(self.gamma[a], Fraction(v[a])))
        return out


def eta_norm(v):
    return sum((Fraction(ETA[a]) * Fraction(v[a]) * Fraction(v[a]) for a in range(8)), Fraction(0))


def pin_character(pa, u):
    """chi(u) with u^dagger C = chi C u^{-1} (0 if neither sign holds)."""
    uinv = mat_inverse_cq(u)
    lhs = mat_mul(mat_dagger(u), pa.C)
    rhs = mat_mul(pa.C, uinv)
    if mat_eq(lhs, rhs):
        return 1
    if mat_eq(lhs, mat_neg(rhs)):
        return -1
    return 0


def krein_sign(pa, u):
    """+1 if u B u^dagger = B, -1 if = -B, 0 otherwise."""
    x = mat_mul_many(u, pa.B, mat_dagger(u))
    if mat_eq(x, pa.B):
        return 1
    if mat_eq(x, mat_neg(pa.B)):
        return -1
    return 0


def vector_action(pa, u):
    """Lambda with u gamma^a u^{-1} = sum_c Lambda[a][c] gamma^c (untwisted adjoint), exact."""
    uinv = mat_inverse_cq(u)
    lam = []
    for a in range(8):
        x = mat_mul_many(u, pa.gamma[a], uinv)
        row = []
        for c in range(8):
            t = mat_trace(mat_mul(x, pa.gamma[c]))            # Tr(gamma^a' gamma^c) = 16 eta_cc delta
            if t.im != 0:
                raise ValueError("complex vector action")
            row.append(t.re * Fraction(1, 16 * ETA[c]))
        recon = mat_zero(16)
        for c in range(8):
            recon = mat_add(recon, mat_scale(pa.gamma[c], row[c]))
        if not mat_eq(recon, x):
            raise ValueError("u gamma^a u^-1 is not a vector")
        lam.append(row)
    return lam


# General rational unit vectors for the reflection checks (chosen here; different from the Wolfram ones)
SPACELIKE_VECTORS = {"spacelikeInteger": (1, 1, 1, 1, 1, 1, 1, 0),
                     "spacelikeRational": (Fraction(3, 5), Fraction(4, 5), Fraction(1, 2), Fraction(1, 2),
                                           Fraction(1, 2), Fraction(1, 2), 0, 0)}
TIMELIKE_VECTORS = {"timelikeInteger": (1, 1, 1, 0, 1, 1, 1, 1),
                    "timelikeRational": (Fraction(1, 2), 0, Fraction(1, 2), 0, Fraction(3, 5), Fraction(4, 5),
                                         Fraction(1, 2), Fraction(1, 2))}


def check_algebra(pa):
    rec = Recorder("algebra")
    g = pa.gamma
    rec.check("fixtureMatches", pa.fixture_agreement is True,
              "gamma^a, C, chirality rebuilt from CONTRACT section 1 equal the committed fixture")
    rec.check("clifford", pa.alg.clifford_ok(), "{gamma^a, gamma^b} = 2 eta^{ab}")
    g8 = pa.g8
    g8_ok = (mat_eq(mat_dagger(g8), g8) and mat_eq(mat_mul(g8, g8), pa.I16)
             and all(mat_is_zero(mat_anticommutator(g8, g[a])) for a in range(8))
             and mat_is_zero(mat_commutator(g8, pa.C))
             and all(mat_is_zero(mat_commutator(g8, pa.S[bc])) for bc in PAIRS)
             and pa.diagonal_g8 and pa.chi == [-1] * 8 + [1] * 8
             and mat_eq(g8, mat_mul_many(*g)))
    rec.check("gamma8Properties", g8_ok,
              "gamma^8 = gamma^0...gamma^7 = diag(-I8, +I8): Hermitian, square 1, anticommutes with every gamma^a, "
              "commutes with C and with all 28 S^{bc} (hence with Omega_mu for every connection)")
    C = pa.C
    c_ok = (all(v.im == 0 for row in C for v in row) and mat_eq(mat_transpose(C), C) and mat_eq(mat_mul(C, C), pa.I16)
            and all(all(v.im == 0 for row in pa.Cg[a] for v in row)
                    and mat_eq(mat_transpose(pa.Cg[a]), mat_neg(pa.Cg[a])) for a in range(8)))
    rec.check("CProperties", c_ok, "C real symmetric, C^2 = 1; C gamma^a real antisymmetric (anti-Hermitian), a = 0..7")
    B = pa.B
    trace_b = mat_trace(B)
    b_ok = (mat_eq(mat_dagger(B), B) and mat_eq(mat_mul(B, B), pa.I16) and mat_is_zero(mat_commutator(B, C))
            and mat_eq(pa.BC, mat_scale(g[4], CQ(0, -1))) and trace_b.is_zero()
            and mat_eq(mat_mul_many(g8, B, g8), mat_neg(B))
            and mat_eq(B, mat_scale(mat_mul_many(g[0], g[1], g[2], g[3], g[4]), CQ(0, -1))))
    rec.check("BProperties", b_ok, "B = -i C gamma^4 = -i gamma^0..gamma^4: Hermitian, B^2 = 1, Tr B = 0 (spectrum "
                                   "(+1)^8 (-1)^8), [B, C] = 0, BC = -i gamma^4, gamma^8 B gamma^8 = -B")
    factors = [mat_mul(g[0], g[1]), mat_mul(g[2], g[3]), mat_mul(g[4], g[5]), mat_mul(g[6], g[7])]
    comp_ok = (mat_eq(mat_mul_many(*factors), g8)
               and all(mat_eq(mat_mul(f, f), mat_neg(pa.I16)) for f in factors)
               and all(mat_is_zero(mat_commutator(f1, f2)) for f1 in factors for f2 in factors)
               and all(mat_eq(mat_mul_many(g8, g[a], g8), mat_neg(g[a])) for a in range(8)))
    rec.check("gamma8InIdentityComponent", comp_ok,
              "gamma^8 = (g0 g1)(g2 g3)(g4 g5)(g6 g7), four commuting bivectors with X^2 = -1, so gamma^8 = "
              "exp((pi/2)(X1 + X2 + X3 + X4)) lies in Spin_0(4,4); its vector action is -1 (in SO_0(4,4))")
    rec.check("gammaDaggerC", all(mat_eq(mat_mul(mat_dagger(g[a]), C), mat_neg(pa.Cg[a])) for a in range(8)),
              "gamma^a dagger C = -C gamma^a for a = 0..7")
    odd = [pa.Cg[a] for a in range(8)]
    odd += [mat_mul(pa.Cg[a], pa.S[bc]) for a in range(8) for bc in PAIRS]
    odd += [mat_mul_many(C, pa.S[bc], g[a]) for a in range(8) for bc in PAIRS]
    parity_ok = all(mat_eq(mat_mul_many(g8, X, g8), mat_neg(X)) for X in odd) and mat_eq(mat_mul_many(g8, C, g8), C)
    rec.check("bilinearParities", parity_ok and len(odd) == 456,
              {"count": len(odd), "statement": "gamma^8 X gamma^8 = -X for X in {C gamma^a, C gamma^a S^{bc}, "
                                               "C S^{bc} gamma^a} (8 + 224 + 224 = 456) and gamma^8 C gamma^8 = +C"})
    rec.measure("oddBilinearMatrixCount", len(odd))
    lower = range(8)
    upper = range(8, 16)
    block_ok = (all(C[i][l].is_zero() for i in lower for l in upper) and all(C[i][l].is_zero() for i in upper for l in lower)
                and all(pa.S[bc][i][l].is_zero() for bc in PAIRS for i in lower for l in upper)
                and all(pa.S[bc][i][l].is_zero() for bc in PAIRS for i in upper for l in lower)
                and all(g[a][i][l].is_zero() for a in range(8) for i in lower for l in lower)
                and all(g[a][i][l].is_zero() for a in range(8) for i in upper for l in upper))
    rec.check("chiralBlockStructure", block_ok,
              "C and every S^{bc} are block diagonal in (Psi_0..Psi_7 | Psi_8..Psi_15), every gamma^a is block "
              "off-diagonal: gamma^8 Psi = (-Psi_upper, +Psi_lower)")
    chars = []
    norms = []
    for a in range(8):
        v = [1 if b == a else 0 for b in range(8)]
        chars.append(pin_character(pa, g[a]))
        norms.append(int(eta_norm(v)))
    general = {}
    for name, v in list(SPACELIKE_VECTORS.items()) + list(TIMELIKE_VECTORS.items()):
        u = pa.unit_vector(v)
        n = eta_norm(v)
        general[name] = {"vector": [frac_str(x) for x in v], "norm": frac_str(n),
                         "uSquaredIsNorm": mat_eq(mat_mul(u, u), mat_scale(pa.I16, n)),
                         "character": pin_character(pa, u), "kreinSign": krein_sign(pa, u)}
    char_ok = (chars == [-n for n in norms] and all(gv["uSquaredIsNorm"] and gv["character"] == -int(Fraction(gv["norm"]))
                                                    for gv in general.values()))
    rec.check("characterIsMinusNorm", char_ok,
              {"basisCharacters": chars, "basisNorms": norms, "general": general,
               "statement": "u^dagger C = chi(u) C u^{-1} with chi(u) = -n(u) for every real unit vector"})
    signs = [krein_sign(pa, g[a]) for a in range(8)]
    rec.check("kreinUnderBasicReflections", signs == [1, 1, 1, 1, 1, -1, -1, -1],
              {"uBudaggerSigns_gamma0to7": signs,
               "derivation": "B = -i gamma^0 gamma^1 gamma^2 gamma^3 gamma^4: gamma^a (a <= 4) commutes with the "
                             "5-fold product, gamma^5..gamma^7 anticommute; with gamma^a dagger = eta_aa gamma^a this gives "
                             "+B, +B, +B, +B, +B, -B, -B, -B (not the Pin character: B is tied to the x4 foliation)"})
    rec.measure("uBudaggerSigns", signs)
    return rec


# CHUNK-2-END

# ---------------------------------------------------------------------------
# 3. Family "T1generic": T1 as polynomial identities in independent generic symbols
#    (commuting components = dirac16complex00; every gravitational field, off shell)
# ---------------------------------------------------------------------------

class GenericT1:
    """Generic-symbol Lagrangian, field equations, EL expressions, current and EMT.

    Variables (all independent): psi_a, psis_a (= Psi^*_a), their first and second jets,
    E[a][mu] = e_a^mu, W[mu][bc] (Omega_mu = sum_{b<c} W_{mu,bc} gamma^b gamma^c: a general
    element of the spin algebra, i.e. an arbitrary connection), G = sqrt|g|, the lowered
    frame F[mu][a] (gamma_mu = F_{mu a} gamma^a), g[mu][nu] = g_{mu nu}, m and lam; for
    the Euler-Lagrange expressions also the first derivatives dE, dW, dG of the
    geometric coefficients.  No relation between E, F, g, W, G is used, so every
    identity below holds for every vielbein and connection (a stronger statement)."""

    def __init__(self, pa):
        self.pa = pa
        vt = VarTable()
        self.vt = vt
        self.psi = [vt.var(("psi", a)) for a in range(16)]
        self.psis = [vt.var(("psis", a)) for a in range(16)]
        self.dpsi = [[vt.var(("dpsi", mu, a)) for a in range(16)] for mu in range(8)]
        self.dpsis = [[vt.var(("dpsis", mu, a)) for a in range(16)] for mu in range(8)]
        self.ddpsi = {}
        self.ddpsis = {}
        for mu in range(8):
            for nu in range(mu, 8):
                self.ddpsi[(mu, nu)] = [vt.var(("ddpsi", mu, nu, a)) for a in range(16)]
                self.ddpsis[(mu, nu)] = [vt.var(("ddpsis", mu, nu, a)) for a in range(16)]
        self.E = [[vt.var(("E", a, mu)) for mu in range(8)] for a in range(8)]
        self.W = [{bc: vt.var(("W", mu) + bc) for bc in PAIRS} for mu in range(8)]
        self.G = vt.var(("G",))
        self.dE = [[[vt.var(("dE", a, mu, nu)) for nu in range(8)] for mu in range(8)] for a in range(8)]
        self.dW = [{bc: [vt.var(("dW", mu) + bc + (nu,)) for nu in range(8)] for bc in PAIRS} for mu in range(8)]
        self.dG = [vt.var(("dG", nu)) for nu in range(8)]
        self.m = vt.var(("m",))
        self.lam = vt.var(("lam",))
        self.F = [[vt.var(("F", mu, a)) for a in range(8)] for mu in range(8)]
        self.g = {}
        for mu in range(8):
            for nu in range(mu, 8):
                self.g[(mu, nu)] = self.g[(nu, mu)] = vt.var(("g", mu, nu))
        chi = pa.chi
        self.sign_g8 = {}
        for a in range(16):
            for lst in ([self.psi, self.psis] + self.dpsi + self.dpsis + list(self.ddpsi.values())
                        + list(self.ddpsis.values())):
                self.sign_g8[lst[a]] = chi[a]
        self.sign_ml = {self.m: -1, self.lam: -1}
        self.sign_m = {self.m: -1}
        self.sign_both = dict(self.sign_g8)
        self.sign_both.update(self.sign_ml)
        # total derivatives d_nu on every jet and geometric variable
        self.dmap = []
        for nu in range(8):
            d = {}
            for a in range(16):
                d[self.psi[a]] = self.dpsi[nu][a]
                d[self.psis[a]] = self.dpsis[nu][a]
                for mu in range(8):
                    key = (min(mu, nu), max(mu, nu))
                    d[self.dpsi[mu][a]] = self.ddpsi[key][a]
                    d[self.dpsis[mu][a]] = self.ddpsis[key][a]
            for a in range(8):
                for mu in range(8):
                    d[self.E[a][mu]] = self.dE[a][mu][nu]
            for mu in range(8):
                for bc in PAIRS:
                    d[self.W[mu][bc]] = self.dW[mu][bc][nu]
            d[self.G] = self.dG[nu]
            self.dmap.append(d)
        self._build()

    def _build(self):
        pa = self.pa
        RC = pa.R["C"]
        self.S = add_bilinear(SPoly(), RC, self.psis, self.psi)
        kin_d = SPoly()
        for mu in range(8):
            for a in range(8):
                add_bilinear(kin_d, pa.RCg[a], self.psis, self.dpsi[mu], (self.E[a][mu],), Fraction(1, 2))
                add_bilinear(kin_d, pa.RCg[a], self.dpsis[mu], self.psi, (self.E[a][mu],), Fraction(-1, 2))
        kin_c = SPoly()
        for mu in range(8):
            for a in range(8):
                for bc in PAIRS:
                    add_bilinear(kin_c, pa.RC_anti[(a, bc)], self.psis, self.psi,
                                 (self.E[a][mu], self.W[mu][bc]), Fraction(1, 2))
        self.kin_d, self.kin_c = kin_d, kin_c
        self.kin = kin_d + kin_c
        self.S2 = self.S.mul(self.S)
        self.Ls = self.kin - self.S.times_var(self.m) - self.S2.times_var(self.lam).scale(Fraction(1, 2))
        self.L = self.Ls.times_var(self.G)

    def field_equation(self):
        """E_i = (gamma^mu D_mu Psi)_i - (m + lam S) Psi_i (16 polynomials)."""
        pa = self.pa
        out = [SPoly() for _ in range(16)]
        for mu in range(8):
            for a in range(8):
                ea = self.E[a][mu]
                Ga = pa.Rg[a]
                for i in range(16):
                    for j in range(16):
                        if Ga[i][j] != 0:
                            out[i].add_term(tuple(sorted((ea, self.dpsi[mu][j]))), Ga[i][j])
                for bc in PAIRS:
                    M = pa.Rg_bc[(a, bc)]
                    w = self.W[mu][bc]
                    for i in range(16):
                        for j in range(16):
                            if M[i][j] != 0:
                                out[i].add_term(tuple(sorted((ea, w, self.psi[j]))), M[i][j])
        for i in range(16):
            out[i].add_term(tuple(sorted((self.m, self.psi[i]))), -1)
            out[i].iadd(self.S.times_var(self.psi[i]).times_var(self.lam), -1)
        return out

    def conjugate_field_equation(self):
        """Ebar_j = ((D_mu Psibar) gamma^mu)_j + (m + lam S) Psibar_j (16 polynomials)."""
        pa = self.pa
        RC = pa.R["C"]
        out = [SPoly() for _ in range(16)]
        for mu in range(8):
            for a in range(8):
                ea = self.E[a][mu]
                M = pa.RCg[a]
                for i in range(16):
                    for j in range(16):
                        if M[i][j] != 0:
                            out[j].add_term(tuple(sorted((ea, self.dpsis[mu][i]))), M[i][j])
                for bc in PAIRS:
                    Mb = pa.RC_bc_g[(bc, a)]
                    w = self.W[mu][bc]
                    for i in range(16):
                        for j in range(16):
                            if Mb[i][j] != 0:
                                out[j].add_term(tuple(sorted((ea, w, self.psis[i]))), -Mb[i][j])
        for j in range(16):
            pb = SPoly()
            for i in range(16):
                if RC[i][j] != 0:
                    pb.add_term((self.psis[i],), RC[i][j])
            out[j].iadd(pb.times_var(self.m))
            out[j].iadd(pb.mul(self.S).times_var(self.lam))
        return out

    def euler_lagrange_psis(self):
        """EL_a = dL/dpsis_a - sum_nu d_nu (dL/d(d_nu psis_a)), L = G L_s, with the total derivative
        acting on the field jets AND on the geometric coefficients."""
        dL = self.L.all_derivatives()
        empty = SPoly()
        out = []
        for a in range(16):
            e = dL.get(self.psis[a], empty).copy()
            for nu in range(8):
                e.iadd(dL.get(self.dpsis[nu][a], empty).total_derivative(self.dmap[nu]), -1)
            out.append(e)
        return out

    def current(self):
        out = []
        for mu in range(8):
            j = SPoly()
            for a in range(8):
                add_bilinear(j, self.pa.RCg[a], self.psis, self.psi, (self.E[a][mu],))
            out.append(j)
        return out

    def emt_kinetic(self, mu, nu):
        """K_{mu nu} = -(1/4)[A_mn + A_nm - Bar_mn - Bar_nm], A_mn = Psibar gamma_m D_n Psi,
        Bar_mn = (D_m Psibar) gamma_n Psi (gamma_m = F_{m a} gamma^a, Omega = W gamma gamma)."""
        pa = self.pa

        def A(m1, n1):
            p = SPoly()
            for a in range(8):
                f = self.F[m1][a]
                add_bilinear(p, pa.RCg[a], self.psis, self.dpsi[n1], (f,))
                for bc in PAIRS:
                    add_bilinear(p, pa.RC_g_bc[(a, bc)], self.psis, self.psi, (f, self.W[n1][bc]))
            return p

        def Bar(m1, n1):
            p = SPoly()
            for a in range(8):
                f = self.F[n1][a]
                add_bilinear(p, pa.RCg[a], self.dpsis[m1], self.psi, (f,))
                for bc in PAIRS:
                    add_bilinear(p, pa.RC_bc_g[(bc, a)], self.psis, self.psi, (f, self.W[m1][bc]), -1)
            return p

        k = A(mu, nu) + A(nu, mu) - Bar(mu, nu) - Bar(nu, mu)
        return k.scale(Fraction(-1, 4))


def check_t1generic(pa, quick=False):
    rec = Recorder("T1generic")
    gt = GenericT1(pa)
    s8, sml, sboth, sm = gt.sign_g8, gt.sign_ml, gt.sign_both, gt.sign_m
    rec.measure("variables", len(gt.vt))
    rec.measure("kineticMonomials", gt.kin.nterms())
    rec.measure("connectionMonomials", gt.kin_c.nterms())
    rec.measure("lagrangianMonomials", gt.L.nterms())
    w_vars = {gt.W[mu][bc] for mu in range(8) for bc in PAIRS}
    rec.check("nontrivial", gt.kin_d.nterms() > 0 and gt.kin_c.nterms() > 0 and gt.S.nterms() == 16
              and gt.S2.nterms() == 136 and bool(gt.L.variables() & w_vars),
              {"kineticMonomials": gt.kin.nterms(), "connectionMonomials": gt.kin_c.nterms(),
               "S": gt.S.nterms(), "S^2": gt.S2.nterms(),
               "note": "the connection enters L through Psibar {gamma^mu, Omega_mu} Psi / 2 (non-trivial coupling to "
                       "the spin connection and, through e_a^mu and sqrt|g|, to gravity)"})
    rec.check("scalarInvariantKineticOdd", gt.S.signed(s8).t == gt.S.t and (gt.kin.signed(s8) + gt.kin).is_zero()
              and gt.S2.signed(s8).t == gt.S2.t,
              "S[gamma^8 Psi] = S[Psi], K[gamma^8 Psi] = -K[Psi], U even")
    lhs = gt.L.signed(s8)
    rhs = gt.L.signed(sml)
    rec.check("lagrangian", (lhs + rhs).is_zero(), "L_{m,lam}[gamma^8 Psi] = -L_{-m,-lam}[Psi] (polynomial identity)")
    naive = lhs + gt.L.signed(sm)
    target = gt.S2.times_var(gt.lam).times_var(gt.G).scale(-1)
    rec.check("naiveFixedLambdaFails", (naive - target).is_zero() and not naive.is_zero(),
              "L_{m,lam}[gamma^8 Psi] + L_{-m,lam}[Psi] = -lam sqrt|g| S^2 != 0 (CONTRACT erratum E2)")
    E = gt.field_equation()
    fe_ok = all((E[i].signed(sboth) + E[i].scale(pa.chi[i])).is_zero() for i in range(16))
    rec.check("fieldEquation", fe_ok and all(not e.is_zero() for e in E),
              "E_{-m,-lam}[gamma^8 Psi] = -gamma^8 E_{m,lam}[Psi] (16 components, with the cubic term)")
    Eb = gt.conjugate_field_equation()
    feb_ok = all((Eb[j].signed(sboth) + Eb[j].scale(pa.chi[j])).is_zero() for j in range(16))
    rec.check("conjugateFieldEquation", feb_ok and all(not e.is_zero() for e in Eb),
              "Ebar_{-m,-lam}[gamma^8 Psi] = -Ebar_{m,lam}[Psi] gamma^8")
    EL = gt.euler_lagrange_psis()
    el_ok = all((EL[a].signed(s8).scale(pa.chi[a]) + EL[a].signed(sml)).is_zero() for a in range(16))
    geo_deriv = set(gt.dG) | {gt.dE[a][mu][nu] for a in range(8) for mu in range(8) for nu in range(8)}
    el_vars = set().union(*[e.variables() for e in EL])
    rec.check("eulerLagrangeFromLagrangian", el_ok and bool(el_vars & w_vars) and bool(el_vars & geo_deriv),
              {"statement": "gamma^8 EL^{(m,lam)}[gamma^8 Psi] = -EL^{(-m,-lam)}[Psi] for the Euler-Lagrange expressions "
                            "dL/dPsi^* - d_mu dL/d(d_mu Psi^*) derived from L (total derivative acting on the geometric "
                            "coefficients too); hence Psi solves EL_{m,lam} iff gamma^8 Psi solves EL_{-m,-lam}",
               "monomials": sum(e.nterms() for e in EL)})
    cur = gt.current()
    rec.check("current", all((j.signed(s8) + j).is_zero() and not j.is_zero() for j in cur),
              "j^mu[gamma^8 Psi] = -j^mu[Psi] (every mu)")
    Ls_ok = (gt.Ls.signed(sboth) + gt.Ls).is_zero()
    pairs = [(mu, nu) for mu in range(8) for nu in range(mu, 8)]
    if quick:
        pairs = [(0, 0), (1, 4), (4, 4), (3, 7)]
    emt_ok = Ls_ok
    for (mu, nu) in pairs:
        K = gt.emt_kinetic(mu, nu)
        emt_ok &= (K.signed(s8) + K).is_zero() and not K.is_zero()
    # one component assembled in full, T = K + g L_s, to show the decomposition explicitly
    Tfull = gt.emt_kinetic(4, 4) + gt.Ls.times_var(gt.g[(4, 4)])
    full_ok = (Tfull.signed(sboth) + Tfull).is_zero()
    rec.check("emtAll36", emt_ok and full_ok,
              {"components": len(pairs), "statement": "T_{mu nu}[gamma^8 Psi; -m, -lam] = -T_{mu nu}[Psi; m, lam]",
               "method": "T = K_{mu nu} + g_{mu nu} L_s with g_{mu nu} an independent symbol: the identity holds iff it holds "
                         "for K_{mu nu} (each component) and for L_s; T_44 also assembled in full"})
    rec.check("connectionCommutesWithGamma8",
              all(mat_is_zero(mat_commutator(pa.g8, pa.biv[bc])) for bc in PAIRS),
              "[gamma^8, gamma^b gamma^c] = 0 for all 28 pairs: [gamma^8, Omega_mu] = 0 for every connection")
    return rec


# CHUNK-3-END

# ---------------------------------------------------------------------------
# 4. Family "T1grassmann": the same identities for Grassmann-odd components
#    (dirac16complex), exact rational geometric coefficients
# ---------------------------------------------------------------------------

def rand_q(rng, span=9, den=9):
    while True:
        p = rng.randint(-span, span)
        if p != 0:
            return Fraction(p, rng.randint(1, den))


def fmat_zero(n=16):
    return [[Fraction(0)] * n for _ in range(n)]


def fmat_mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = []
    for i in range(n):
        row = [Fraction(0)] * m
        for l in range(k):
            ail = a[i][l]
            if ail != 0:
                bl = b[l]
                for j in range(m):
                    if bl[j] != 0:
                        row[j] += ail * bl[j]
        out.append(row)
    return out


def fmat_add(a, b, factor=1):
    return [[x + factor * y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def fmat_scale(a, factor):
    return [[factor * x for x in row] for row in a]


class GrassmannT1:
    """L, field equations, EMT, current and EL of dirac16complex with Grassmann-odd jets
    theta_{psi,a;alpha}, theta_{psis,a;alpha} (psis = Psi^*), constant exact rational geometric
    coefficients e_a^mu, Omega_mu = W_{mu,bc} gamma^b gamma^c, gamma_mu = F_{mu a} gamma^a, g_{mu nu},
    sqrt|g| (the identities are linear in these coefficients)."""

    def __init__(self, pa, seed=5020260930, max_deriv=2):
        self.pa = pa
        base = random.Random(seed)

        class _Generic:
            """Coefficients from a wide range, so that no accidental cancellation occurs (the monomial
            counts are then those of generic coefficients)."""

            def randint(self, lo, hi):
                return base.randint(lo * 1000 - 7, hi * 1000 + 7) if lo < 0 else base.randint(lo, hi * 997)

        rng = _Generic()
        js = GA.JetSpace(["psi", "psis"], nfield=16, ncoord=8, max_deriv=max_deriv)
        self.js = js
        self.psi0 = js.gens("psi")
        self.psis0 = js.gens("psis")
        self.dpsi = [js.gens("psi", (mu,)) for mu in range(8)]
        self.dpsis = [js.gens("psis", (mu,)) for mu in range(8)]
        chi = pa.chi
        self.gen_sign = [chi[js.label(i)[1]] for i in range(js.ngen)]
        self.E = [[rand_q(rng) for _ in range(8)] for _ in range(8)]              # E[a][mu]
        self.W = [{bc: rand_q(rng) for bc in PAIRS} for _ in range(8)]
        self.F = [[rand_q(rng) for _ in range(8)] for _ in range(8)]              # F[mu][a]
        self.gmet = {}
        for mu in range(8):
            for nu in range(mu, 8):
                self.gmet[(mu, nu)] = self.gmet[(nu, mu)] = rand_q(rng)
        self.sqrtg = rand_q(rng)
        self.m = rand_q(rng)
        self.lam = rand_q(rng)
        biv = {bc: real_matrix(pa.biv[bc]) for bc in PAIRS}
        self.gup = []
        self.Om = []
        self.glow = []
        for mu in range(8):
            gu = fmat_zero()
            gl = fmat_zero()
            for a in range(8):
                gu = fmat_add(gu, pa.Rg[a], self.E[a][mu])
                gl = fmat_add(gl, pa.Rg[a], self.F[mu][a])
            om = fmat_zero()
            for bc in PAIRS:
                om = fmat_add(om, biv[bc], self.W[mu][bc])
            self.gup.append(gu)
            self.glow.append(gl)
            self.Om.append(om)
        RC = pa.R["C"]
        self.RC = RC
        self.S = GA.bilinear(RC, self.psis0, self.psi0)
        kin = GA.Grassmann()
        half = Fraction(1, 2)
        for mu in range(8):
            Cg = fmat_mul(RC, self.gup[mu])
            anti = fmat_add(fmat_mul(Cg, self.Om[mu]), fmat_mul(fmat_mul(RC, self.Om[mu]), self.gup[mu]))
            kin = kin + GA.bilinear(Cg, self.psis0, self.dpsi[mu]).scale(half) \
                - GA.bilinear(Cg, self.dpsis[mu], self.psi0).scale(half) + GA.bilinear(anti, self.psis0, self.psi0).scale(half)
        self.kin = kin
        self.S2 = self.S * self.S

    def g8(self, F):
        """The automorphism theta_{s,a;alpha} -> chi_a theta_{s,a;alpha} (Psi -> gamma^8 Psi, Psi^* -> gamma^8 Psi^*)."""
        out = {}
        for m, c in F.terms.items():
            s = 1
            for gidx in m:
                s *= self.gen_sign[gidx]
            out[m] = c if s > 0 else -c
        return GA.Grassmann(out)

    def Ls(self, m, lam):
        return self.kin - self.S.scale(m) - self.S2.scale(Fraction(lam) / 2)

    def dirac(self, m, lam):
        out = []
        slash_om = fmat_zero()
        for mu in range(8):
            slash_om = fmat_add(slash_om, fmat_mul(self.gup[mu], self.Om[mu]))
        for i in range(16):
            e = GA.Grassmann()
            for mu in range(8):
                e = e + GA.linear(self.gup[mu][i], self.dpsi[mu])
            e = e + GA.linear(slash_om[i], self.psi0)
            psi_i = GA.Grassmann.gen(self.psi0[i])
            e = e - psi_i.scale(m) - (self.S * psi_i).scale(lam)
            out.append(e)
        return out

    def dirac_bar(self, m, lam):
        out = []
        RC = self.RC
        cols = [fmat_mul(RC, self.gup[mu]) for mu in range(8)]
        conn = [fmat_mul(fmat_mul(RC, self.Om[mu]), self.gup[mu]) for mu in range(8)]
        for j in range(16):
            e = GA.Grassmann()
            for mu in range(8):
                e = e + GA.linear([cols[mu][i][j] for i in range(16)], self.dpsis[mu])
                e = e - GA.linear([conn[mu][i][j] for i in range(16)], self.psis0)
            pb = GA.linear([RC[i][j] for i in range(16)], self.psis0)
            e = e + pb.scale(m) + (self.S * pb).scale(lam)
            out.append(e)
        return out

    def current(self):
        return [GA.bilinear(fmat_mul(self.RC, self.gup[mu]), self.psis0, self.psi0) for mu in range(8)]

    def emt(self, mu, nu, m, lam):
        RC = self.RC

        def A(m1, n1):
            Cg = fmat_mul(RC, self.glow[m1])
            return GA.bilinear(Cg, self.psis0, self.dpsi[n1]) + GA.bilinear(fmat_mul(Cg, self.Om[n1]), self.psis0, self.psi0)

        def Bar(m1, n1):
            Cg = fmat_mul(RC, self.glow[n1])
            return GA.bilinear(Cg, self.dpsis[m1], self.psi0) \
                - GA.bilinear(fmat_mul(fmat_mul(RC, self.Om[m1]), self.glow[n1]), self.psis0, self.psi0)

        k = (A(mu, nu) + A(nu, mu) - Bar(mu, nu) - Bar(nu, mu)).scale(Fraction(-1, 4))
        return k + self.Ls(m, lam).scale(self.gmet[(mu, nu)])

    def euler_lagrange(self, m, lam):
        L = self.Ls(m, lam).scale(self.sqrtg)
        return GA.euler_lagrange_all(GA.JetGrassmann({(): L}), self.js, "psis")


def check_t1grassmann(pa, quick=False):
    rec = Recorder("T1grassmann")
    gr = GrassmannT1(pa, max_deriv=1 if quick else 2)
    m, lam = gr.m, gr.lam
    rec.measure("generators", gr.js.ngen)
    rec.measure("couplings", {"m": frac_str(m), "lam": frac_str(lam), "sqrtg": frac_str(gr.sqrtg)})
    L = gr.Ls(m, lam)
    rec.measure("monomials_Ls", L.nterms())
    rec.measure("monomials_S2", gr.S2.nterms())
    odd_ok = all(len(mono) % 2 == 1 for i in range(16) for mono in GA.Grassmann.gen(gr.psi0[i]).terms)
    rec.check("nontrivial", gr.S2.nterms() == 120 and gr.kin.nterms() > 0 and L.is_even() and odd_ok
              and all(len(mono) == 4 for mono in gr.S2.terms),
              {"S^2": gr.S2.nterms(), "note": "the quartic self-interaction S^2 is a nonzero degree-4 element (120 "
                                              "monomials; squares of odd generators vanish, unlike the commuting 136)"})
    rec.check("scalarEvenKineticOdd", gr.g8(gr.S) == gr.S and gr.g8(gr.kin) == -gr.kin and gr.g8(gr.S2) == gr.S2,
              "S -> S, K -> -K, S^2 -> S^2 under theta -> chi theta")
    rec.check("lagrangian", gr.g8(L) == -gr.Ls(-m, -lam) and gr.g8(gr.Ls(m, 0)) == -gr.Ls(-m, 0),
              "L_{m,lam}[gamma^8 Psi] = -L_{-m,-lam}[Psi] in the Grassmann algebra (all m, lam: K odd, S and S^2 even)")
    naive = gr.g8(L) + gr.Ls(-m, lam)
    rec.check("naiveFixedLambdaFails", naive == -gr.S2.scale(lam) and not naive.is_zero(),
              "L_{m,lam}[gamma^8 Psi] + L_{-m,lam}[Psi] = -lam S^2 != 0")
    D = gr.dirac(m, lam)
    Dm = gr.dirac(-m, -lam)
    rec.check("diracOperator", all(gr.g8(Dm[i]) == -D[i].scale(pa.chi[i]) for i in range(16))
              and all(3 in D[i].degrees() and D[i].is_odd() for i in range(16)),
              "E_{-m,-lam}[gamma^8 Psi] = -gamma^8 E_{m,lam}[Psi] with the cubic term lam S Psi (odd, degree 3)")
    Db = gr.dirac_bar(m, lam)
    Dbm = gr.dirac_bar(-m, -lam)
    rec.check("conjugateDiracOperator", all(gr.g8(Dbm[j]) == -Db[j].scale(pa.chi[j]) for j in range(16)),
              "Ebar_{-m,-lam}[gamma^8 Psi] = -Ebar_{m,lam}[Psi] gamma^8")
    pairs = [(mu, nu) for mu in range(8) for nu in range(mu, 8)]
    if quick:
        pairs = [(0, 0), (1, 4), (4, 4), (2, 6)]
    emt_ok = all(gr.g8(gr.emt(mu, nu, -m, -lam)) == -gr.emt(mu, nu, m, lam) for (mu, nu) in pairs)
    rec.check("emt", emt_ok, {"components": len(pairs),
                              "statement": "T_{mu nu}[gamma^8 Psi; -m, -lam] = -T_{mu nu}[Psi; m, lam] (Grassmann-even elements)"})
    rec.check("current", all(gr.g8(j) == -j and not j.is_zero() for j in gr.current()), "j^mu -> -j^mu")
    if not quick:
        el_p = gr.euler_lagrange(m, lam)
        el_m = gr.euler_lagrange(-m, -lam)
        rec.check("eulerLagrangeFromLagrangian",
                  all(gr.g8(el_p[a]).scale(pa.chi[a]) == -el_m[a] for a in range(16))
                  and all(not e.is_zero() and e.is_odd() for e in el_p),
                  {"statement": "left-derivative Euler-Lagrange expressions of sqrt|g| L_{m,lam} (constant coefficients): "
                                "gamma^8 EL^{(m,lam)}[gamma^8 Psi] = -EL^{(-m,-lam)}[Psi]",
                   "generators": gr.js.ngen, "monomials": sum(e.nterms() for e in el_p)})
    return rec


# CHUNK-4-END

# ---------------------------------------------------------------------------
# 5. Families "T1jets" (exact jets of the general Stage-1 vielbein G1) and
#    "T1primordial" (the Stage-2 primordial field, arbitrary a4(t))
# ---------------------------------------------------------------------------

def jet_map_spinor(J, M):
    """(M Psi) for a spinor jet (last axis 16) and a constant exact 16x16 object matrix M."""
    return J.map(lambda v: np.einsum("ij,...j->...i", M, v))


def jet_scale_last(J, chi_arr):
    return J.map(lambda v: v * chi_arr)


def dom_matrix(dom, cq_matrix):
    """Exact domain object array of a real CQ matrix."""
    rm = real_matrix(cq_matrix)
    out = np.empty((len(rm), len(rm[0])), dtype=object)
    for i, row in enumerate(rm):
        for j, v in enumerate(row):
            out[i, j] = dom.conv(sp.Rational(v.numerator, v.denominator))
    return out


def jets_all_zero(J, dom):
    return G.jet_is_zero(J, dom)


def spinor_quantities(geo, psi, chi, m, lam):
    """L_s, kinetic, S, T_{mu nu}, E, Ebar, j^mu for the commuting jets psi (Psi) and chi (Psi^*)."""
    E, Eb, parts = G.field_equations(geo, psi, chi, m, lam)
    T = G.emt_covariant(geo, parts["pb"], parts["Dpb"], psi, parts["Dpsi"], parts["Ls"])
    j = G.jein("mj,j->m", G.jein("i,mij->mj", parts["pb"], geo.gam), psi)
    return {"Ls": parts["Ls"], "kin": parts["kin"], "S": parts["S"], "T": T, "E": E, "Eb": Eb, "j": j}


def geometry_from(ej, gd, dom, name, curvature=False, sqrtg_sign=None):
    return G.Geometry(ej, gd, dom, name, sqrtg_sign=sqrtg_sign, curvature=curvature)


T1JET_SEEDS = {"p1": 61, "p2": 62, "p3": 63}
# distinct couplings (m != +-lam), so that an exchange of the roles of m and lam could not go unnoticed
T1JET_COUPLINGS = {"p1": (sp.Rational(3, 7), sp.Rational(-5, 4)), "p2": (sp.Rational(-2, 9), sp.Rational(7, 3)),
                   "p3": (sp.Rational(5, 2), sp.Rational(1, 6))}


def check_t1jets(pa, quick=False):
    rec = Recorder("T1jets")
    dom = G.make_qq_domain()
    gd = G.GammaData(dom)
    chi_arr = np.array([dom.conv(c) for c in pa.chi], dtype=object)
    emat = G.g1_vielbein_sympy()
    labels = ["p1"] if quick else ["p1", "p2", "p3"]
    agg = {}

    def add(key, ok):
        agg.setdefault(key, []).append(bool(ok))

    for lab in labels:
        full = (lab == "p1") and not quick
        order = 2 if full else 1
        rng = random.Random(T1JET_SEEDS[lab])
        ej = G.vielbein_jet_from_sympy(emat, G.G1_POINTS[lab], order, dom)
        geo = geometry_from(ej, gd, dom, "G1_" + lab)
        m = dom.conv(T1JET_COUPLINGS[lab][0])
        lam = dom.conv(T1JET_COUPLINGS[lab][1])
        rec.measure("couplings_" + lab, {"m": dom.to_str(m), "lam": dom.to_str(lam)})
        psi = G.random_spinor_jet(rng, dom, order)
        chi = G.random_spinor_jet(rng, dom, order)
        psi8, chi8 = jet_scale_last(psi, chi_arr), jet_scale_last(chi, chi_arr)
        q = spinor_quantities(geo, psi, chi, m, lam)
        qi = spinor_quantities(geo, psi8, chi8, -m, -lam)       # the image with (-m, -lam)
        q8 = spinor_quantities(geo, psi8, chi8, m, lam)         # the image with (m, lam)
        qn = spinor_quantities(geo, psi, chi, -m, lam)          # (-m, same lam)
        qml = spinor_quantities(geo, psi, chi, -m, -lam)
        add("lagrangian", jets_all_zero(q8["Ls"] + qml["Ls"], dom))
        add("scalarEvenKineticOdd", jets_all_zero(q8["S"] - q["S"], dom) and jets_all_zero(q8["kin"] + q["kin"], dom)
            and not jets_all_zero(q["kin"], dom))
        naive = q8["Ls"] + qn["Ls"]
        S0 = q["S"].value()[()]
        add("naiveFixedLambdaFails", dom.is_zero(naive.value()[()] + lam * S0 * S0) and not dom.is_zero(naive.value()[()]))
        add("emt", jets_all_zero(qi["T"] + q["T"], dom) and G.count_nonzero(q["T"].value(), dom) > 0)
        add("current", jets_all_zero(qi["j"] + q["j"], dom))
        add("fieldEquations", jets_all_zero(qi["E"] + jet_scale_last(q["E"], chi_arr), dom)
            and jets_all_zero(qi["Eb"] + jet_scale_last(q["Eb"], chi_arr), dom))
        add("connectionCommutes", all(G.arr_is_zero(np.einsum("ij,jk->ik", gd.CHI, geo.Omega.value()[mu])
                                                     - np.einsum("ij,jk->ik", geo.Omega.value()[mu], gd.CHI), dom)
                                      for mu in range(8)) and not G.arr_is_zero(geo.slash_omega(), dom))
        rec.measure("S_value_" + lab, dom.to_str(S0))
        # on-shell images
        ps, cs = G.solve_onshell(geo, psi, chi, m, lam, max_order=order)
        Es, Ebs, _ = G.field_equations(geo, ps, cs, m, lam)
        ps8, cs8 = jet_scale_last(ps, chi_arr), jet_scale_last(cs, chi_arr)
        Ei, Ebi, _ = G.field_equations(geo, ps8, cs8, -m, -lam)
        Ewrong, _, _ = G.field_equations(geo, ps8, cs8, m, lam)
        Ewrong2, _, _ = G.field_equations(geo, ps8, cs8, -m, lam)
        add("onShellImage", jets_all_zero(Es, dom) and jets_all_zero(Ebs, dom) and jets_all_zero(Ei, dom)
            and jets_all_zero(Ebi, dom) and not G.arr_is_zero(Ewrong.value(), dom)
            and not G.arr_is_zero(Ewrong2.value(), dom))
        qs = spinor_quantities(geo, ps, cs, m, lam)
        qs8 = spinor_quantities(geo, ps8, cs8, -m, -lam)
        pair_ok = (jets_all_zero(qs["T"] + qs8["T"], dom) and jets_all_zero(qs["j"] + qs8["j"], dom)
                   and jets_all_zero(qs["Ls"] + qs8["Ls"], dom) and jets_all_zero(qs8["S"] - qs["S"], dom)
                   and not G.arr_is_zero(qs["T"].value(), dom))
        add("pairEMTAndCurrentVanish", pair_ok)
        if full:
            div1 = G.emt_divergence(geo, qs["T"])
            div2 = G.emt_divergence(geo, qs8["T"])
            off = G.emt_divergence(geo, q["T"])
            add("conservationBoth", G.arr_is_zero(div1, dom) and G.arr_is_zero(div2, dom)
                and G.count_nonzero(off, dom) > 0 and G.count_nonzero(qs["T"].grad().value(), dom) > 0)
        # vielbein sign flip e -> -e (order-1 jets suffice for the point identities)
        ej1 = ej.truncate(1)
        geo1 = geo if order == 1 else geometry_from(ej1, gd, dom, "G1_" + lab + "_o1")
        geon = geometry_from(ej1.map(lambda v: -v), gd, dom, "G1_" + lab + "_minus")
        same_geo = (G.jet_is_zero(geon.g - geo1.g, dom) and G.jet_is_zero(geon.sqrtg - geo1.sqrtg, dom)
                    and G.jet_is_zero(geon.Omega - geo1.Omega, dom) and G.jet_is_zero(geon.gam + geo1.gam, dom))
        add("vielbeinSignFlipGeometry", same_geo)
        p1j, c1j = psi.truncate(1), chi.truncate(1)
        a = spinor_quantities(geon, p1j, c1j, m, lam)
        b = spinor_quantities(geo1, p1j, c1j, -m, -lam)
        b0 = spinor_quantities(geo1, p1j, c1j, m, lam)
        a8 = spinor_quantities(geon, jet_scale_last(p1j, chi_arr), jet_scale_last(c1j, chi_arr), m, lam)
        add("vielbeinSignFlipIsT1", jets_all_zero(a["Ls"] + b["Ls"], dom) and jets_all_zero(a["T"] + b["T"], dom))
        add("gamma8WithFrameSignIsSymmetry", jets_all_zero(a8["Ls"] - b0["Ls"], dom) and jets_all_zero(a8["T"] - b0["T"], dom)
            and jets_all_zero(a8["E"] - jet_scale_last(b0["E"], chi_arr), dom)
            and not jets_all_zero(a8["E"] + jet_scale_last(b0["E"], chi_arr), dom))
    texts = {
        "lagrangian": "L_s[gamma^8 Psi; m, lam] = -L_s[Psi; -m, -lam] (jets of order 1-2 at the G1 points)",
        "scalarEvenKineticOdd": "S even, kinetic term odd under Psi -> gamma^8 Psi",
        "naiveFixedLambdaFails": "L_s[gamma^8 Psi; m, lam] + L_s[Psi; -m, lam] = -lam S^2 != 0",
        "emt": "T_{mu nu}[gamma^8 Psi; -m, -lam] = -T_{mu nu}[Psi; m, lam], all 64 components (jets)",
        "current": "j^mu[gamma^8 Psi] = -j^mu[Psi]",
        "fieldEquations": "E_{-m,-lam}[gamma^8 Psi] = -gamma^8 E_{m,lam}[Psi] and the conjugate equation",
        "connectionCommutes": "[gamma^8, Omega_mu] = 0 for the G1 connection; gamma^mu Omega_mu != 0 (curved field)",
        "onShellImage": "an on-shell Psi (m, lam) has an on-shell image for (-m, -lam); the image is not a solution for "
                        "(m, lam) or (-m, lam)",
        "pairEMTAndCurrentVanish": "on shell: T[Psi] + T[gamma^8 Psi] = 0, j + j' = 0, L + L' = 0, S' = S",
        "conservationBoth": "nabla^mu T_{mu nu} = 0 for both members of the pair (order-2 jets at p1); nonzero off shell",
        "vielbeinSignFlipGeometry": "e -> -e leaves g, sqrt|g| and Omega unchanged and reverses gamma^mu",
        "vielbeinSignFlipIsT1": "L_s[-e, Psi; m, lam] = -L_s[e, Psi; -m, -lam] and T likewise",
        "gamma8WithFrameSignIsSymmetry": "(gamma^8, e -> -e) is an exact symmetry: L, T invariant, E[-e, gamma^8 Psi] = "
                                         "+gamma^8 E[e, Psi] (gamma'^mu = -gamma^mu and gamma^mu gamma^8 = -gamma^8 gamma^mu)",
    }
    for key, values in agg.items():
        rec.check(key, all(values) and len(values) > 0, {"points": labels, "results": values, "statement": texts[key]})
    return rec


def check_t1primordial(pa, quick=False):
    rec = Recorder("T1primordial")
    dom = G.make_g2_domain()
    gd = G.GammaData(dom)
    chi_arr = np.array([dom.conv(c) for c in pa.chi], dtype=object)
    ej = G.g2_vielbein_jet(1, dom)
    geo = geometry_from(ej, gd, dom, "G2", sqrtg_sign=1)
    so = geo.slash_omega()
    gamma0 = gd.GAM[0]
    three_h = dom.conv(3 * G.G2_H)
    om_vals = [dom.to_str(x) for x in geo.Omega.value().flat if not dom.is_zero(x)]
    rec.check("nontrivialCoupling", G.arr_is_zero(so - gamma0 * three_h, dom) and any("A1" in s or "E" in s for s in om_vals),
              {"slashOmega": "gamma^mu Omega_mu = 3H gamma^0 (a4 cancels)", "OmegaNonzeroEntries": len(om_vals),
               "note": "the individual Omega_mu depend on a4(t) (E = e^{a4}, A1 = a4'), gamma^mu Omega_mu does not"})
    rng = random.Random(71)
    m = dom.conv(sp.Rational(-4, 11))
    lam = dom.conv(sp.Rational(9, 5))
    rec.measure("couplings", {"m": "-4/11", "lam": "9/5"})
    psi = G.random_spinor_jet(rng, dom, 1)
    chi = G.random_spinor_jet(rng, dom, 1)
    q = spinor_quantities(geo, psi, chi, m, lam)
    qi = spinor_quantities(geo, jet_scale_last(psi, chi_arr), jet_scale_last(chi, chi_arr), -m, -lam)
    q8 = spinor_quantities(geo, jet_scale_last(psi, chi_arr), jet_scale_last(chi, chi_arr), m, lam)
    qml = spinor_quantities(geo, psi, chi, -m, -lam)
    rec.check("scalarAndKinetic", G.arr_is_zero(q8["S"].value() - q["S"].value(), dom)
              and G.arr_is_zero(q8["kin"].value() + q["kin"].value(), dom))
    rec.check("lagrangian", G.arr_is_zero(q8["Ls"].value() + qml["Ls"].value(), dom),
              "L[gamma^8 Psi; m, lam] = -L[Psi; -m, -lam] in the notebook chart, generic fields of all 8 coordinates")
    rec.check("diracOperator", G.arr_is_zero(qi["E"].value() + q["E"].value() * chi_arr, dom)
              and G.arr_is_zero(qi["Eb"].value() + q["Eb"].value() * chi_arr, dom))
    rec.check("emt64", G.arr_is_zero(qi["T"].value() + q["T"].value(), dom) and G.count_nonzero(q["T"].value(), dom) > 0,
              {"nonzeroComponents": G.count_nonzero(q["T"].value(), dom)})
    rec.check("current", G.arr_is_zero(qi["j"].value() + q["j"].value(), dom))
    rec.measure("domain", dom.name)
    rec.measure("relationUses", dom.relation_uses)
    return rec


# CHUNK-5-END

# ---------------------------------------------------------------------------
# 6. Family "T1krein": exact Krein-Fock model of the quantum field dirac16complex
# ---------------------------------------------------------------------------

def krein_rest_modes(red):
    """Four joint eigenvectors of h = -i gamma^4 (m = 1) and B in the rest sector, exact:
    u = (v+ +- i v-)/4 in the Stage-4 blocks 0 (j = s2 = 1, B = +1) and 2 (j = 1, s2 = -1, B = -1)."""
    def w(b, s):
        return [(vp + CQ(0, s) * vm) * Fraction(1, 4) for vp, vm in zip(b["vPlus"], b["vMinus"])]
    b0, b2 = red.blocks[0], red.blocks[2]
    return [(w(b0, 1), 1, 1), (w(b2, 1), 1, -1), (w(b0, -1), -1, 1), (w(b2, -1), -1, -1)]


class KreinFock:
    """Field Psi_a = sum_n u_{n,a} c_n and Krein adjoint Psi^K_a = sum_n beta_n conj(u_{n,a}) c_n^dagger on the
    positive-CAR Fock space of the modes (Jordan-Wigner, exact)."""

    def __init__(self, vectors, betas):
        self.u = vectors
        self.beta = betas
        self.n = len(vectors)
        self.fock = KS.FockSpace(self.n)
        self.dim = self.fock.dim
        c, cd = self.fock.b, self.fock.bdag
        self.psi = []
        self.psik = []
        for a in range(16):
            p = mat_zero(self.dim)
            pk = mat_zero(self.dim)
            for n in range(self.n):
                if not self.u[n][a].is_zero():
                    p = mat_add(p, mat_scale(c[n], self.u[n][a]))
                    pk = mat_add(pk, mat_scale(cd[n], self.u[n][a].conj() * self.beta[n]))
            self.psi.append(p)
            self.psik.append(pk)

    def bilinear(self, M):
        """sum_ab Psi^K_a M_ab Psi_b = sum_nm beta_n (u_n^dagger M u_m) c_n^dagger c_m."""
        c, cd = self.fock.b, self.fock.bdag
        out = mat_zero(self.dim)
        for n in range(self.n):
            for k in range(self.n):
                coefficient = vec_dot(self.u[n], mat_apply(M, self.u[k])) * self.beta[n]
                if not coefficient.is_zero():
                    out = mat_add(out, mat_scale(mat_mul(cd[n], c[k]), coefficient))
        return out

    def bilinear_from_fields(self, M, left=None, right=None):
        left = self.psik if left is None else left
        right = self.psi if right is None else right
        out = mat_zero(self.dim)
        for a in range(16):
            for b in range(16):
                if not M[a][b].is_zero():
                    out = mat_add(out, mat_scale(mat_mul(left[a], right[b]), M[a][b]))
        return out

    def car_matrix(self, left, right):
        """X_ab with {right_a, left_b} = X_ab 1 (None if not proportional to 1)."""
        ident = mat_eye(self.dim)
        X = []
        for a in range(16):
            row = []
            for b in range(16):
                ac = mat_anticommutator(right[a], left[b])
                value = ac[0][0]
                if not mat_eq(ac, mat_scale(ident, value)):
                    return None
                row.append(value)
            X.append(row)
        return X

    def state(self, create=(), annihilate=(), base=None):
        vec = base if base is not None else [CQ_ONE] + [CQ_ZERO] * (self.dim - 1)
        for n in annihilate:
            vec = mat_apply(self.fock.b[n], vec)
        for n in create:
            vec = mat_apply(self.fock.bdag[n], vec)
        return vec

    @staticmethod
    def expect(op, vec):
        return vec_dot(vec, mat_apply(op, vec))


def check_t1krein(pa, red):
    rec = Recorder("T1krein")
    g = pa.gamma
    hp = mat_scale(g[4], CQ(0, -1))            # h(m = 1) = -i gamma^4 = BC
    hm = mat_scale(g[4], CQ(0, 1))             # h(m = -1)
    rec.check("restHamiltonians", mat_eq(mat_dagger(hp), hp) and mat_eq(mat_mul(hp, hp), pa.I16)
              and mat_is_zero(mat_commutator(hp, pa.B)) and mat_eq(mat_mul_many(pa.g8, hp, pa.g8), hm)
              and mat_eq(hp, pa.BC),
              "h(m) = -i m gamma^4 (k = 0, CONTRACT section 8): Hermitian, h^2 = m^2, [h, B] = 0, "
              "gamma^8 h(m) gamma^8 = h(-m)")
    modes = krein_rest_modes(red)
    vecs = [x[0] for x in modes]
    eps = [x[1] for x in modes]
    betas = [x[2] for x in modes]
    modes_ok = all(vec_is_eigen(hp, v, CQ(e)) and vec_is_eigen(pa.B, v, CQ(bt)) for v, e, bt in modes) and \
        all(vec_dot(vecs[a], vecs[b]) == (CQ_ONE if a == b else CQ_ZERO) for a in range(4) for b in range(4))
    rec.check("modes", modes_ok, {"(eps, beta)": list(zip(eps, betas)),
                                   "vectors": "(v+ +- i v-)/4 of Stage-4 blocks 0 and 2 (exact, orthonormal)"})
    kf = KreinFock(vecs, betas)
    P = mat_zero(16)
    for v in vecs:
        for i in range(16):
            for l in range(16):
                P[i][l] = P[i][l] + v[i] * v[l].conj()
    BP = mat_mul(pa.B, P)
    car = kf.car_matrix(kf.psik, kf.psi)
    zero_car = all(mat_is_zero(mat_anticommutator(kf.psi[a], kf.psi[b])) for a in range(16) for b in range(16))
    rec.check("fieldCAR", car is not None and mat_eq(car, BP) and zero_car,
              "{Psi_a, Psi^K_b} = (B P)_ab (P the projector on the four modes), {Psi_a, Psi_b} = 0: the Krein CAR "
              "{c_n, c_n^K} = beta_n realised on a positive Fock space")
    rec.check("bilinearFromFields", mat_eq(kf.bilinear(pa.C), kf.bilinear_from_fields(pa.C)),
              "sum Psi^K_a C_ab Psi_b equals the mode form sum beta_n u_n^dagger C u_m c_n^dagger c_m")
    sea = kf.state(create=(2, 3))
    excitations = {"particle0": kf.state(create=(0,), base=sea), "particle1": kf.state(create=(1,), base=sea),
                   "hole2": kf.state(annihilate=(2,), base=sea), "hole3": kf.state(annihilate=(3,), base=sea)}
    rec.check("statesNormalised", all(vec_dot(s, s) == CQ_ONE for s in list(excitations.values()) + [sea]))
    ops = {"C": pa.C, "B": pa.B, "Bh": mat_mul(pa.B, hp), "Cgamma4": mat_mul(pa.C, g[4]), "BC": pa.BC}
    rule_ok = True
    table = {}
    for name, M in ops.items():
        O = kf.bilinear(M)
        s0 = kf.expect(O, sea)
        for label, st in excitations.items():
            n = int(label[-1])
            value = kf.expect(O, st) - s0
            predicted = vec_dot(vecs[n], mat_apply(mat_mul(pa.B, M), vecs[n]))
            if label.startswith("hole"):
                predicted = -predicted
            rule_ok &= value == predicted
            table.setdefault(name, {})[label] = value.to_pair()
    rec.check("expectationRule", rule_ok, {"rule": "particle in mode u: <:Psi^K M Psi:> = u^dagger B M u; hole: "
                                                   "-u^dagger B M u (normal ordering = subtraction of the sea value)",
                                           "values": table})
    H = kf.bilinear(mat_mul(pa.B, hp))
    energies = [kf.expect(H, st) - kf.expect(H, sea) for st in excitations.values()]
    rec.check("positiveExcitations", all(e == CQ_ONE for e in energies),
              {"energies": [e.to_pair() for e in energies], "note": "every excitation has energy |eps| = m > 0"})
    Sop = kf.bilinear(pa.C)
    scal = [kf.expect(Sop, st) - kf.expect(Sop, sea) for st in excitations.values()]
    rec.measure("scalarDensity_particle0_particle1_hole2_hole3", [int(s.re) for s in scal])
    # the image field Psi_- = gamma^8 Psi on the same Fock space
    chi = pa.chi
    psi_m = [mat_scale(kf.psi[a], chi[a]) for a in range(16)]
    psik_m = [mat_scale(kf.psik[a], chi[a]) for a in range(16)]
    car_m = kf.car_matrix(psik_m, psi_m)
    P_minus = mat_mul_many(pa.g8, P, pa.g8)
    rec.check("imageAnticommutatorMinusB", car_m is not None and mat_eq(car_m, mat_neg(mat_mul(pa.B, P_minus))),
              "{Psi_-, Psi_-^K} = gamma^8 B P gamma^8 = -B P_- (P_- = gamma^8 P gamma^8): the image carries the Krein "
              "metric -B, i.e. it is canonically a field of -L_{-m,-lam}")
    H_plus = kf.bilinear_from_fields(mat_mul(pa.B, hp))
    H_minus = kf.bilinear_from_fields(mat_mul(pa.B, hm), left=psik_m, right=psi_m)
    Q_plus = kf.bilinear_from_fields(pa.B)
    Q_minus = kf.bilinear_from_fields(pa.B, left=psik_m, right=psi_m)
    S_plus = kf.bilinear_from_fields(pa.C)
    S_minus = kf.bilinear_from_fields(pa.C, left=psik_m, right=psi_m)
    no_h = mat_sub(H_minus, mat_scale(mat_eye(kf.dim), kf.expect(H_minus, sea)))
    no_hp = mat_sub(H_plus, mat_scale(mat_eye(kf.dim), kf.expect(H_plus, sea)))

    def spin_apply(M, ops):
        """(M Psi)_a = sum_b M_ab Psi_b for a 16 x 16 spinor matrix M and a list of 16 Fock operators."""
        out = []
        for a in range(16):
            acc = mat_zero(kf.dim)
            for b in range(16):
                if not M[a][b].is_zero():
                    acc = mat_add(acc, mat_scale(ops[b], M[a][b]))
            out.append(acc)
        return out
    # the image field's own generators: with its anticommutator -B, [Psi_-, H[Psi_-; -m]] = -h(-m) Psi_- and
    # [Psi_-, Q[Psi_-]] = -Psi_-, while the state evolves by i d_4 Psi_- = [Psi_-, H_+] = h(-m) Psi_- (and
    # [Psi, H_+] = h(m) Psi, [Psi, Q_+] = +Psi): its x4-generator is -H[Psi_-; -m] = +H_+, its U(1) generator
    # -Q[Psi_-] = +Q_+
    h_psi = spin_apply(hp, kf.psi)
    hm_psi_m = spin_apply(hm, psi_m)
    gen_ok = any(not mat_is_zero(x) for x in psi_m)
    for a in range(16):
        gen_ok = (gen_ok and mat_eq(mat_commutator(kf.psi[a], H_plus), h_psi[a])
                  and mat_eq(mat_commutator(kf.psi[a], Q_plus), kf.psi[a])
                  and mat_eq(mat_commutator(psi_m[a], H_plus), hm_psi_m[a])
                  and mat_eq(mat_commutator(psi_m[a], H_minus), mat_neg(hm_psi_m[a]))
                  and mat_eq(mat_commutator(psi_m[a], Q_minus), mat_neg(psi_m[a])))
    rec.check("imageOperatorIdentities", mat_eq(H_minus, mat_neg(H_plus)) and mat_eq(Q_minus, mat_neg(Q_plus))
              and mat_eq(S_minus, S_plus) and mat_eq(no_h, mat_neg(no_hp)) and not mat_is_zero(H_plus) and gen_ok,
              "H[Psi_-; -m] = Psi_-^K B h(-m) Psi_- = -H[Psi; m], Q_- = -Q, S_- = S as Fock operators; normal ordering "
              "commutes with the map (:H_-: = -:H_+:); the image field's own generators: [Psi_-, H[Psi_-; -m]] = "
              "-h(-m) Psi_-, [Psi_-, Q[Psi_-]] = -Psi_- while i d_4 Psi_- = [Psi_-, H_+] = h(-m) Psi_-, so its "
              "x4-generator is -H[Psi_-; -m] = +H_+ and its U(1) generator -Q[Psi_-] = +Q_+ (the same quantum system "
              "as Psi in other variables)")
    img = {}
    img_ok = True
    for label, st in excitations.items():
        e_p = kf.expect(H_plus, st) - kf.expect(H_plus, sea)
        e_m = kf.expect(H_minus, st) - kf.expect(H_minus, sea)
        q_p = kf.expect(Q_plus, st) - kf.expect(Q_plus, sea)
        q_m = kf.expect(Q_minus, st) - kf.expect(Q_minus, sea)
        s_p = kf.expect(S_plus, st) - kf.expect(S_plus, sea)
        s_m = kf.expect(S_minus, st) - kf.expect(S_minus, sea)
        img_ok &= e_m == -e_p and q_m == -q_p and s_m == s_p and e_m == CQ(-1)
        if label.startswith("particle"):
            n = int(label[-1])
            um = mat_apply(pa.g8, vecs[n])
            img_ok &= e_m == vec_dot(um, mat_apply(mat_mul_many(mat_neg(pa.B), pa.B, hm), um))
        img[label] = {"E": [e_p.to_pair(), e_m.to_pair()], "Q": [q_p.to_pair(), q_m.to_pair()],
                      "S": [s_p.to_pair(), s_m.to_pair()]}
    rec.check("imageExpectationValues", img_ok,
              {"(+ universe, image)": img, "statement": "the L_{-m,-lam} formulas H[Psi_-; -m] and Q[Psi_-] give "
                                                        "every quantum of the image the energy -|eps| and the opposite "
                                                        "charge; particle values u_-^dagger (-B) M u_-, u_- = gamma^8 u. "
                                                        "These are minus the image field's own x4-generator and charge "
                                                        "(imageOperatorIdentities), not the energy and charge of a "
                                                        "second universe"})
    # independent quantisation of the -m theory with its own +B structure
    wvec = [mat_apply(pa.g8, v) for v in vecs]
    wbeta = [-bt for bt in betas]
    wm_ok = all(vec_is_eigen(hm, w, CQ(e)) and vec_is_eigen(pa.B, w, CQ(bt)) for w, e, bt in zip(wvec, eps, wbeta))
    rec.check("minusMModes", wm_ok, "w_n = gamma^8 u_n: h(-m) w_n = eps_n w_n (same eps), B w_n = -beta_n w_n")
    kw = KreinFock(wvec, wbeta)
    Pw = mat_zero(16)
    for v in wvec:
        for i in range(16):
            for l in range(16):
                Pw[i][l] = Pw[i][l] + v[i] * v[l].conj()
    carw = kw.car_matrix(kw.psik, kw.psi)
    rec.check("independentCARPlusB", carw is not None and mat_eq(carw, mat_mul(pa.B, Pw)),
              "the independently quantised -m field has {Psi', Psi'^K} = +B P_w (its own positive J = B structure)")
    seaw = kw.state(create=(2, 3))
    exw = {"particle0": kw.state(create=(0,), base=seaw), "particle1": kw.state(create=(1,), base=seaw),
           "hole2": kw.state(annihilate=(2,), base=seaw), "hole3": kw.state(annihilate=(3,), base=seaw)}
    Hw, Qw, Sw = kw.bilinear(mat_mul(pa.B, hm)), kw.bilinear(pa.B), kw.bilinear(pa.C)
    Qp, Sp = kf.bilinear(pa.B), kf.bilinear(pa.C)
    ind_ok = True
    ind = {}
    for label in excitations:
        e1 = kf.expect(H, excitations[label]) - kf.expect(H, sea)
        q1 = kf.expect(Qp, excitations[label]) - kf.expect(Qp, sea)
        s1 = kf.expect(Sp, excitations[label]) - kf.expect(Sp, sea)
        e2 = kw.expect(Hw, exw[label]) - kw.expect(Hw, seaw)
        q2 = kw.expect(Qw, exw[label]) - kw.expect(Qw, seaw)
        s2 = kw.expect(Sw, exw[label]) - kw.expect(Sw, seaw)
        ind_ok &= e2 == e1 and q2 == q1 and s2 == -s1
        ind[label] = {"+m (E,Q,S)": [e1.to_pair(), q1.to_pair(), s1.to_pair()],
                      "-m independent (E,Q,S)": [e2.to_pair(), q2.to_pair(), s2.to_pair()]}
    rec.check("independentExpectationValues", ind_ok,
              {"values": ind, "statement": "an independently (positively) quantised -m universe: (E, Q, S) -> (E, Q, -S); "
                                           "its energy-momentum does NOT cancel that of the +m universe"})
    return rec


# CHUNK-6-END

# ---------------------------------------------------------------------------
# 7. Family "T2frame": Pin(4,4) reflections with twisted / untwisted frame lifts
# ---------------------------------------------------------------------------

def reflection_rows(v, n):
    """R_u(gamma^a) = gamma^a - 2 eta(e_a, v)/n(u) v = sum_c R[a][c] gamma^c."""
    return [[Fraction(1 if a == c else 0) - 2 * Fraction(ETA[a]) * Fraction(v[a]) * Fraction(v[c]) / n
             for c in range(8)] for a in range(8)]


def sign_of_multiple(x, y, dom):
    """+1 if x == y, -1 if x == -y (x, y jets or arrays), 0 otherwise."""
    if isinstance(x, G.TJet):
        if G.jet_is_zero(x - y, dom):
            return 1
        if G.jet_is_zero(x + y, dom):
            return -1
        return 0
    if G.arr_is_zero(x - y, dom):
        return 1
    if G.arr_is_zero(x + y, dom):
        return -1
    return 0


def lagrangian_map_string(frame, field, sK, sS):
    """Result of the transformation in the notation of STAGE5_SPEC: L_{m,lam}[frame, field] = sK L_{m',lam'}."""
    mp = "m" if sS * sK == 1 else "-m"
    lp = "lambda" if sK == 1 else "-lambda"
    if sK == 1 and mp == "m" and lp == "lambda":
        rhs = "L_{m,lambda}[e, Psi]"
    else:
        rhs = "%sL_{%s,%s}[e, Psi]" % ("+" if sK == 1 else "-", mp, lp)
    return "L_{m,lambda}[%s, %s] = %s" % (frame, field, rhs)


def check_t2frame(pa, quick=False, vectors=None):
    """``vectors`` (optional list of (name, coefficient tuple)) overrides the default set (tests)."""
    rec = Recorder("T2frame")
    override = vectors
    dom = G.make_qq_domain()
    gd = G.GammaData(dom)
    ej = G.vielbein_jet_from_sympy(G.g1_vielbein_sympy(), G.G1_POINTS["p1"], 1, dom)
    geo = geometry_from(ej, gd, dom, "G1_p1")
    rng = random.Random(81)
    m = dom.conv(sp.Rational(5, 3))
    lam = dom.conv(sp.Rational(-2, 7))
    psi = G.random_spinor_jet(rng, dom, 1)
    chi = G.random_spinor_jet(rng, dom, 1)
    base = {}

    def reference(mm, ll):
        key = (str(mm), str(ll))
        if key not in base:
            base[key] = spinor_quantities(geo, psi, chi, mm, ll)
        return base[key]

    q0 = reference(m, lam)
    vectors = [("gamma^%d" % a, tuple(1 if b == a else 0 for b in range(8))) for a in range(8)]
    vectors += list(SPACELIKE_VECTORS.items()) + list(TIMELIKE_VECTORS.items())
    if quick:
        vectors = [vectors[0], vectors[4], ("spacelikeRational", SPACELIKE_VECTORS["spacelikeRational"]),
                   ("timelikeRational", TIMELIKE_VECTORS["timelikeRational"])]
    if override is not None:
        vectors = list(override)
    chi8 = dom_matrix(dom, pa.g8)
    agg = {}
    table = []

    def add(key, ok):
        agg.setdefault(key, []).append(bool(ok))

    for name, v in vectors:
        U = pa.unit_vector(v)
        n = eta_norm(v)
        add("unitVectors", mat_eq(mat_mul(U, U), mat_scale(pa.I16, n)) and n in (1, -1))
        ch = pin_character(pa, U)
        add("characterIsMinusNorm", ch == -int(n))
        Lam = vector_action(pa, U)
        Rr = reflection_rows(v, n)
        add("untwistedAdjointIsMinusReflection", all(Lam[a][c] == -Rr[a][c] for a in range(8) for c in range(8)))
        Ud = dom_matrix(dom, U)
        Uinv = Ud * dom.conv(sp.Rational(1) / sp.Rational(n.numerator, n.denominator))
        row = {"u": name, "vector": [frac_str(x) for x in v], "norm": frac_str(n), "character": ch,
               "uBudaggerSign": krein_sign(pa, U)}
        for lift in ("twisted", "untwisted"):
            sgn = -1 if lift == "twisted" else 1
            Mt = np.empty((8, 8), dtype=object)
            for a in range(8):
                for c in range(8):
                    Mt[c, a] = dom.conv(sp.Rational(sgn) * sp.Rational(Lam[a][c].numerator, Lam[a][c].denominator))
            Minv = G.mat_inv(Mt, dom)
            ejp = ej.map(lambda arr: arr.dot(Minv))
            geop = geometry_from(ejp, gd, dom, "G1_p1_%s_%s" % (name, lift))
            om0, om1 = geo.Omega.value(), geop.Omega.value()
            g0, g1 = geo.gam.value(), geop.gam.value()
            geo_ok = (G.jet_is_zero(geop.g - geo.g, dom) and G.jet_is_zero(geop.sqrtg - geo.sqrtg, dom)
                      and all(G.arr_is_zero(om1[mu] - Ud.dot(om0[mu]).dot(Uinv), dom) for mu in range(8))
                      and all(G.arr_is_zero(g1[mu] - Ud.dot(g0[mu]).dot(Uinv) * dom.conv(sgn), dom) for mu in range(8)))
            add("frameReflectionsGeometry", geo_ok)
            for tag, Mfield in (("u", Ud), ("gamma8u", chi8.dot(Ud))):
                if tag == "gamma8u" and lift == "twisted":
                    continue
                ps, cs = jet_map_spinor(psi, Mfield), jet_map_spinor(chi, Mfield)
                q1 = spinor_quantities(geop, ps, cs, m, lam)
                sK = sign_of_multiple(q1["kin"], q0["kin"], dom)
                sS = sign_of_multiple(q1["S"], q0["S"], dom)
                sj = sign_of_multiple(q1["j"], q0["j"], dom)
                if tag == "u":
                    predicted_K = -ch if lift == "twisted" else ch
                    predicted_S = ch
                else:
                    predicted_K = ch
                    predicted_S = ch
                    predicted_K = -predicted_K       # gamma^8 reverses the kinetic term, keeps S
                ok_signs = sK == predicted_K and sS == predicted_S and sj == sK and sK != 0 and sS != 0
                mm = m * (sS * sK)
                ll = lam * sK
                ref = reference(mm, ll)
                ok_L = G.jet_is_zero(q1["Ls"] - ref["Ls"].scale(sK), dom)
                ok_T = G.jet_is_zero(q1["T"] - ref["T"].scale(sK), dom)
                add("scalarAndCurrentSigns", ok_signs)
                frame = "e R_u" if lift == "twisted" else "-e R_u"
                field = "u Psi" if tag == "u" else "gamma^8 u Psi"
                text = lagrangian_map_string(frame, field, sK, sS)
                row["%s_%s" % (lift, tag)] = {"sK": sK, "sS": sS, "sj": sj, "L": ok_L, "T": ok_T, "result": text}
                space = n == 1
                if tag == "u" and lift == "twisted":
                    add("twistedSpacelikeMapsToMinusMSameLambda" if space else "twistedTimelike", ok_L and ok_T and ok_signs)
                elif tag == "u":
                    add("untwistedSpacelikeContractE3" if space else "untwistedTimelikeSymmetry", ok_L and ok_T and ok_signs)
                else:
                    add("gamma8TimesUntwistedSpacelike" if space else "gamma8TimesUntwistedTimelike",
                        ok_L and ok_T and ok_signs)
            if lift == "twisted" and n == 1 and name in ("gamma^0", "spacelikeRational"):
                # on-shell: Psi solves (-m, lam) in the frame e  =>  u Psi solves (m, lam) in the frame e R_u
                psn, csn = G.solve_onshell(geo, psi, chi, -m, lam, max_order=1)
                E1, Eb1, _ = G.field_equations(geop, jet_map_spinor(psn, Ud), jet_map_spinor(csn, Ud), m, lam)
                E2, _, _ = G.field_equations(geop, jet_map_spinor(psn, Ud), jet_map_spinor(csn, Ud), -m, lam)
                add("onShellImage", G.arr_is_zero(E1.value(), dom) and G.arr_is_zero(Eb1.value(), dom)
                    and not G.arr_is_zero(E2.value(), dom))
        table.append(row)
    texts = {
        "unitVectors": "u = v_a gamma^a with u^2 = n(u) = +-1",
        "characterIsMinusNorm": "chi(u) = -n(u)",
        "untwistedAdjointIsMinusReflection": "u gamma^a u^{-1} = -R_u(gamma^a) (R_u the hyperplane reflection)",
        "frameReflectionsGeometry": "e -> e R_u (twisted) / e -> -e R_u (untwisted): g, sqrt|g| unchanged, "
                                    "Omega -> u Omega u^{-1}, gamma^mu -> -+ u gamma^mu u^{-1}",
        "scalarAndCurrentSigns": "kinetic term -> sK K, S -> sS S, j -> sK j with sK = -chi (twisted) / chi (untwisted), "
                                 "sS = chi; gamma^8 u flips sK",
        "twistedSpacelikeMapsToMinusMSameLambda": "space-like u (chi = -1), twisted: L_{m,lam}[e R_u, u Psi] = "
                                                  "L_{-m,lam}[e, Psi], T -> +T (same metric), S -> -S, j -> +j",
        "twistedTimelike": "time-like u (chi = +1), twisted: L -> -L_{-m,-lam}, T -> -T",
        "untwistedSpacelikeContractE3": "space-like u, untwisted: L -> -L_{m,-lam} (CONTRACT E3)",
        "untwistedTimelikeSymmetry": "time-like u, untwisted: exact symmetry",
        "gamma8TimesUntwistedSpacelike": "gamma^8 u, untwisted, space-like: L -> +L_{-m,lam}",
        "gamma8TimesUntwistedTimelike": "gamma^8 u, untwisted, time-like: L -> -L_{-m,-lam}",
        "onShellImage": "Psi on shell for (-m, lam) in the frame e => u Psi on shell for (m, lam) in the frame e R_u "
                        "(not for (-m, lam))",
    }
    for key, values in agg.items():
        rec.check(key, all(values) and len(values) > 0, {"results": len(values), "statement": texts[key]})
    rec.measure("table", table)
    rec.measure("couplings", {"m": "5/3", "lam": "-2/7"})
    return rec, table


# CHUNK-7-END

# ---------------------------------------------------------------------------
# 8. Family "T2z2": the Z2-extended static primordial field (proper chart y)
#    W = e^{Hy} (y < 0, notebook patch), W = e^{-Hy} (y > 0, mirror side)
# ---------------------------------------------------------------------------

YPOS = sp.Symbol("y", positive=True)       # the mirror-side point y > 0; its partner is -y < 0


def z2_patch(pa, side):
    """Vielbein diag(1, W e^{a4} (x3), 1, W e^{-a4} (x3)) and Omega_mu (own spin connection), side = -1 (W = e^{Hy})
    or +1 (W = e^{-Hy}), evaluated at the point y (side +1) or -y (side -1)."""
    Yp = sp.Symbol("Yp", real=True)
    xs = sp.symbols("x1:8", real=True)
    W = sp.exp(-side * KS.H * Yp)
    h = [sp.Integer(1)] + [W * sp.exp(KS.A4C)] * 3 + [sp.Integer(1)] + [W * sp.exp(-KS.A4C)] * 3
    _, lowered, _, ok = KS.spin_connection(h, [Yp] + list(xs))
    Om = KS.omega_matrices(pa.alg, lowered)
    point = YPOS if side == 1 else -YPOS
    hv = [sp.simplify(x.subs(Yp, point)) for x in h]
    Omv = [sp.simplify(M.subs(Yp, point)) for M in Om]
    return {"h": hv, "Omega": Omv, "postulateOk": ok, "W": sp.simplify(W.subs(Yp, point))}


def z2_linear_dirac(G16, patch):
    """D Psi = sum_l M_l data_l with data labels 'v' (value) and 'd0'..'d7' (partial derivatives)."""
    out = {"v": sp.zeros(16)}
    for mu in range(8):
        gu = G16[mu] / patch["h"][mu]
        out["d%d" % mu] = gu
        out["v"] = out["v"] + gu * patch["Omega"][mu]
    return out


def form_add(target, key, M):
    target[key] = target[key] + M if key in target else M


def z2_kinetic_form(C16, G16, patch):
    """K_s = (1/2) sum_mu [Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi] as {(left, right): matrix}."""
    f = {}
    half = sp.Rational(1, 2)
    for mu in range(8):
        gu = G16[mu] / patch["h"][mu]
        Om = patch["Omega"][mu]
        form_add(f, ("v", "d%d" % mu), half * C16 * gu)
        form_add(f, ("v", "v"), half * C16 * gu * Om)
        form_add(f, ("d%d" % mu, "v"), -half * C16 * gu)
        form_add(f, ("v", "v"), half * C16 * Om * gu)
    return f


def z2_emt_kinetic_form(C16, G16, patch, mu, nu):
    f = {}
    quarter = sp.Rational(-1, 4)

    def glow(a):
        return ETA[a] * patch["h"][a] * G16[a]

    for (m1, n1) in ((mu, nu), (nu, mu)):
        form_add(f, ("v", "d%d" % n1), quarter * C16 * glow(m1))
        form_add(f, ("v", "v"), quarter * C16 * glow(m1) * patch["Omega"][n1])
        form_add(f, ("d%d" % m1, "v"), -quarter * C16 * glow(n1))
        form_add(f, ("v", "v"), quarter * C16 * patch["Omega"][m1] * glow(n1))
    return f


def label_sign(label):
    return -1 if label == "d0" else 1


def pull_form(form, P):
    """Form of the image Psi'(y) = P Psi(-y) expressed in the data of Psi at -y: s_l s_r P^dagger M P."""
    Pd = P.H
    return {(l, r): label_sign(l) * label_sign(r) * (Pd * M * P) for (l, r), M in form.items()}


def pull_linear(lin, P):
    return {l: label_sign(l) * M * P for l, M in lin.items()}


def dicts_equal(a, b, scale=1):
    keys = set(a) | set(b)
    for k in keys:
        x = a.get(k, sp.zeros(16))
        y = b.get(k, sp.zeros(16))
        d = sp.expand(x - scale * y)
        if any(sp.simplify(v) != 0 for v in d if v != 0):
            return False
    return True


def check_t2z2(pa, quick=False):
    rec = Recorder("T2z2")
    G16 = [mat_to_sympy(g) for g in pa.gamma]
    C16 = mat_to_sympy(pa.C)
    g0 = G16[0]
    plus = z2_patch(pa, 1)
    minus = z2_patch(pa, -1)
    geo_ok = (plus["postulateOk"] and minus["postulateOk"]
              and all(sp.simplify(a - b) == 0 for a, b in zip(plus["h"], minus["h"]))
              and all(sp.simplify(sp.expand(A - g0 * B * g0)) == sp.zeros(16) for A, B in zip(plus["Omega"], minus["Omega"])))
    slash_p = sp.zeros(16)
    slash_m = sp.zeros(16)
    for mu in range(8):
        slash_p += G16[mu] / plus["h"][mu] * plus["Omega"][mu]
        slash_m += G16[mu] / minus["h"][mu] * minus["Omega"][mu]
    slash_ok = (sp.simplify(slash_p + 3 * KS.H * g0) == sp.zeros(16) and sp.simplify(slash_m - 3 * KS.H * g0) == sp.zeros(16))
    rec.check("geometry", geo_ok and slash_ok,
              {"statement": "h_mu(y) = h_mu(-y) (W = e^{-H|y|} even): y -> -y is an isometry; Omega^+_mu(y) = "
                            "gamma^0 Omega^-_mu(-y) gamma^0 (the frame reflection of e_0); gamma^mu Omega_mu = -3H gamma^0 "
                            "(y > 0) and +3H gamma^0 (y < 0); vielbein postulate on both patches",
               "W(y>0)": str(plus["W"]), "W(-y)": str(minus["W"])})
    Dp = z2_linear_dirac(G16, plus)
    Dm = z2_linear_dirac(G16, minus)
    PA = g0
    dirac_ok = dicts_equal(pull_linear(Dp, PA), {l: -g0 * M for l, M in Dm.items()})
    rec.check("diracOperator", dirac_ok,
              "gamma^mu D_mu Psi'(y) = -gamma^0 (gamma^mu D_mu Psi)(-y) for Psi'(y) = gamma^0 Psi(-y) (all 9 data "
              "components, both patches)")
    Sform = {("v", "v"): C16}
    S_ok = dicts_equal(pull_form(Sform, PA), Sform, scale=-1)
    rec.check("scalarOdd", S_ok, "S[Psi'](y) = -S[Psi](-y) (gamma^0 C gamma^0 = -C)")
    Kp = z2_kinetic_form(C16, G16, plus)
    Km = z2_kinetic_form(C16, G16, minus)
    rec.check("kineticEven", dicts_equal(pull_form(Kp, PA), Km), "K[Psi'](y) = K[Psi](-y)")
    # explicit data symbols for the Lagrangian and the field equation (with the quartic and cubic terms)
    F = {l: sp.Matrix(sp.symbols("F_%s_0:16" % l)) for l in ["v"] + ["d%d" % mu for mu in range(8)]}
    Fb = {l: sp.Matrix(sp.symbols("Fb_%s_0:16" % l)) for l in ["v"] + ["d%d" % mu for mu in range(8)]}
    m_s, lam_s, mp = sp.symbols("m lam m_y", real=True)

    def evaluate(form, left, right):
        total = 0
        for (l, r), M in form.items():
            total += (left[l].T * M * right[r])[0]
        return sp.expand(total)

    def image_data(data, P):
        return {l: label_sign(l) * P * v for l, v in data.items()}

    Fi, Fbi = image_data(F, PA), image_data(Fb, PA)        # Psi'(y) data in terms of Psi(-y) data (P real)
    S_img = evaluate(Sform, Fbi, Fi)
    S_orig = evaluate(Sform, Fb, F)
    L_img = evaluate(Kp, Fbi, Fi) + m_s * S_img - lam_s / 2 * S_img ** 2          # L_{-m,lam}[Psi'](y)
    L_orig = evaluate(Km, Fb, F) - m_s * S_orig - lam_s / 2 * S_orig ** 2          # L_{m,lam}[Psi](-y)
    sqrtg_even = sp.simplify(plus["W"] ** 6 - minus["W"] ** 6) == 0
    rec.check("lagrangianEven", sp.simplify(sp.expand(L_img - L_orig)) == 0 and sqrtg_even,
              "L_{-m,lam}[Psi'](y) = L_{m,lam}[Psi](-y) with the quartic term; sqrt|g| = W^6 is even")

    def dirac_value(lin, data):
        out = sp.zeros(16, 1)
        for l, M in lin.items():
            out += M * data[l]
        return out

    E_img = dirac_value(Dp, Fi) - (-m_s + lam_s * S_img) * Fi["v"]
    E_orig = dirac_value(Dm, F) - (m_s + lam_s * S_orig) * F["v"]
    rec.check("fieldEquationMapsToMinusMSameLambda", sp.simplify(sp.expand(E_img + g0 * E_orig)) == sp.zeros(16, 1),
              "E_{-m,lam}[Psi'](y) = -gamma^0 E_{m,lam}[Psi](-y) (with the cubic term): Psi solves (m, lam) on y < 0 iff "
              "Psi' solves (-m, lam) on y > 0 (the SAME lambda)")
    E_same = dirac_value(Dp, Fi) - (m_s + lam_s * S_img) * Fi["v"]
    rec.check("sameMassFails", sp.simplify(sp.expand(E_same + g0 * E_orig - (-2 * m_s) * g0 * F["v"])) == sp.zeros(16, 1),
              "with the same mass: E_{m,lam}[Psi'](y) + gamma^0 E_{m,lam}[Psi](-y) = -2m gamma^0 Psi(-y) != 0")
    E_fun = dirac_value(Dp, Fi) - (mp + lam_s * S_img) * Fi["v"]
    E_fun_orig = dirac_value(Dm, F) - (-mp + lam_s * S_orig) * F["v"]
    mf_ok = sp.simplify(sp.expand(E_fun + g0 * E_fun_orig)) == sp.zeros(16, 1)
    rec.check("massFunctionMap", mf_ok,
              "for a mass function m(y): E_{m(y)}[Psi'](y) = -gamma^0 E_{-m(y)}[Psi](-y): the image solves the equation "
              "with the mass function y -> -m(-y)")
    ma, mb = sp.symbols("m_a m_b", real=True)
    diff = (dirac_value(Dm, F) - ma * F["v"]) - (dirac_value(Dm, F) - mb * F["v"])
    rec.check("symmetricIffOddMass", mf_ok and sp.expand(diff - (mb - ma) * F["v"]) == sp.zeros(16, 1),
              "a Z2-symmetric configuration Psi(y) = gamma^0 Psi(-y) solves the equations on both sides with ONE mass "
              "function m iff (m(y) + m(-y)) Psi(-y) = 0, i.e. iff m is odd where Psi != 0: the -M mirror universe")
    pairs = [(mu, nu) for mu in range(8) for nu in range(8)]
    if quick:
        pairs = [(0, 0), (0, 4), (1, 1), (4, 4), (1, 4), (5, 6)]
    svec = [-1] + [1] * 7
    emt_ok = True
    for (mu, nu) in pairs:
        emt_ok &= dicts_equal(pull_form(z2_emt_kinetic_form(C16, G16, plus, mu, nu), PA),
                              z2_emt_kinetic_form(C16, G16, minus, mu, nu), scale=svec[mu] * svec[nu])
    rec.check("emtPullback", emt_ok and S_ok,
              {"components": len(pairs),
               "statement": "T'_{mu nu}(y) = s_mu s_nu T_{mu nu}(-y), s = (-1, 1, ..., 1) (order y, x1..x7) for Psi' with "
                            "(-m, lam): kinetic parts pulled back, L_s even, S odd, g_{mu nu} even: the EMT of the mirror "
                            "universe is the pull-back (same energy density and pressures)"})
    cur_ok = all(dicts_equal(pull_form({("v", "v"): C16 * G16[mu] / plus["h"][mu]}, PA),
                             {("v", "v"): C16 * G16[mu] / minus["h"][mu]}, scale=svec[mu]) for mu in range(8))
    rec.check("currentPullback", cur_ok, "j'^mu(y) = s_mu j^mu(-y): the charge density j^4 is even")
    # P_B = i gamma^0 gamma^8
    G8 = mat_to_sympy(pa.g8)
    PB = sp.I * g0 * G8
    pb_basic = sp.expand(PB * PB - sp.eye(16)) == sp.zeros(16) and sp.expand(PB.H - PB) == sp.zeros(16)
    pb_dirac = dicts_equal(pull_linear(Dp, PB), {l: PB * M for l, M in Dm.items()})
    pb_S = dicts_equal(pull_form(Sform, PB), Sform, scale=-1)
    pb_K = dicts_equal(pull_form(Kp, PB), Km, scale=-1)
    rec.check("PBfieldLevelFlipsLambda", pb_basic and pb_dirac and pb_S and pb_K,
              "P_B: Psi'(y) = i gamma^0 gamma^8 Psi(-y): D Psi' = P_B (D Psi)(-y), S -> -S, K -> -K, hence "
              "E_{m,-lam}[Psi'](y) = P_B E_{m,lam}[Psi](-y) and L_{m,-lam}[Psi'](y) = -L_{m,lam}[Psi](-y)")
    Bs, BCs = mat_to_sympy(pa.B), mat_to_sympy(pa.BC)
    dens = {"n": Bs * Bs, "s": BCs, "t": -G16[4] * G16[1], "c": g0 * G16[4]}
    table = {}
    for name, M in dens.items():
        pa_img = sp.expand(g0 * M * g0)
        pb_img = sp.expand(PB * M * PB)
        table[name] = {"P_A": "even" if pa_img == M else ("odd" if pa_img == -M else "mixed"),
                       "P_B": "even" if pb_img == M else ("odd" if pb_img == -M else "mixed")}
    rec.check("ruleParities", table == {"n": {"P_A": "even", "P_B": "even"}, "s": {"P_A": "odd", "P_B": "even"},
                                        "t": {"P_A": "even", "P_B": "even"}, "c": {"P_A": "odd", "P_B": "odd"}},
              {"table": table, "note": "expectation-rule matrices n = B B, s = BC, t = -gamma^4 gamma^1, c = gamma^0 gamma^4: "
                                       "the rule matrix BC is P_B-even while C is P_B-odd"})
    rec.check("PBRuleMatrixEvenCOdd", sp.expand(PB * BCs * PB - BCs) == sp.zeros(16) and sp.expand(PB * C16 * PB + C16) == sp.zeros(16),
              "P_B BC P_B = BC, P_B C P_B = -C: P_B is a same-lambda symmetry only at the mean-field level with the "
              "expectation rule, not at the field level")
    return rec


# CHUNK-8-END

# ---------------------------------------------------------------------------
# 9. Family "T3block": block form of the maps on the exact Stage-4 basis
# ---------------------------------------------------------------------------

SIG1, SIG2, SIG3, I2 = KS.SIG1, KS.SIG2, KS.SIG3, KS.I2
JS, MM, KK, EPS, VV = KS.JSYM, KS.MM, KS.KK, KS.EPS, KS.VV
KAPPA = KS.KAPPA_Y
SG = sp.Symbol("sg", real=True)            # statistics sign: -1 dirac16complex, +1 dirac16complex00
LAMS, NS, SS, MSY = sp.symbols("lam n S m", real=True)
THETA = sp.Symbol("theta", real=True)


def phase_times(M2, P2):
    """c with M2 = c P2 (2x2 CQ matrices; P2 a Pauli matrix), or None."""
    for r in range(2):
        for c in range(2):
            if not P2[r][c].is_zero():
                coefficient = M2[r][c] / P2[r][c]
                return coefficient if mat_eq(M2, mat_scale(P2, coefficient)) else None
    return None


def block_index(label):
    return KS.BLOCK_LABELS.index(label)


def bag_Q(theta):
    return sp.cos(theta) * SIG3 + sp.sin(theta) * SIG2


def check_t3block(pa, red):
    rec = Recorder("T3block")
    P = KS.PAULI
    blocks = red.blocks
    phases8 = [None] * 8
    ok8 = True
    for s in blocks:
        t_label = (-s["j"], s["s2"], s["s3"])
        t = blocks[block_index(t_label)]
        for other in blocks:
            M2 = red.cross_block(pa.g8, other, s)
            if other is t:
                c = phase_times(M2, P["s2"])
                ok8 &= c is not None and c.norm2() == 1
                phases8[t["index"]] = c
            else:
                ok8 &= mat_is_zero(M2)
    rec.check("gamma8IsSigma2BetweenPartnerBlocks", ok8,
              {"phasesByTargetBlock": [c.to_pair() if c is not None else None for c in phases8],
               "statement": "V^dagger gamma^8 V maps block (j, s2, s3) onto (-j, s2, s3) as c sigma2 (|c| = 1)"})
    rec.measure("gamma8PhasesByTargetBlock", [int(c.re) if c is not None and c.im == 0 else str(c) for c in phases8])
    phases1 = []
    ok1 = True
    for s in blocks:
        for other in blocks:
            M2 = red.cross_block(pa.gamma[1], other, s)
            if other is s:
                c = phase_times(M2, P["s1"])
                ok1 &= c is not None and c.norm2() == 1
                phases1.append(c)
            else:
                ok1 &= mat_is_zero(M2)
    rec.check("gamma1IsSigma1InEveryBlock", ok1, {"phases": [c.to_pair() if c else None for c in phases1]})
    rec.measure("gamma1Phases", [int(c.re) if c is not None and c.im == 0 else str(c) for c in phases1])
    ok0 = all(mat_eq(red.block_of(pa.gamma[0], b), P["s3"]) for b in blocks) and \
        all(mat_is_zero(red.cross_block(pa.gamma[0], b1, b2)) for b1 in blocks for b2 in blocks if b1 is not b2)
    rec.check("gamma0IsSigma3", ok0, "gamma^0 = sigma3 in every block (block diagonal)")
    targets = {}
    for a in (2, 3, 5, 6, 7):
        lst = []
        for s in blocks:
            lst.append([o["index"] for o in blocks if not mat_is_zero(red.cross_block(pa.gamma[a], o, s))])
        targets["gamma^%d" % a] = lst
    rec.measure("otherGammasTargetBlocks", targets)
    # block ODE and Hamiltonian maps (sympy)
    N = KS.block_ode_matrix
    ode_ok = {
        "sigma2": sp.simplify(SIG2 * N() * SIG2 - N(M=-MM, j=-JS)) == sp.zeros(2),
        "sigma1": sp.simplify(SIG1 * N() * SIG1 - N(M=-MM, k=-KK)) == sp.zeros(2),
        "sigma3": sp.simplify(-SIG3 * N() * SIG3 - N(M=-MM)) == sp.zeros(2),
        "antiunitary": sp.simplify(N().conjugate() - N(k=-KK, j=-JS)) == sp.zeros(2),
        "sigma2K": sp.simplify(SIG2 * N().conjugate() * SIG2 - N(M=-MM, k=-KK)) == sp.zeros(2),
    }
    rec.check("blockODEMaps", all(ode_ok.values()),
              {"results": ode_ok, "N_j(M, k)": "M sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1",
               "sigma2": "sigma2 N_j(M, k) sigma2 = N_{-j}(-M, k)", "sigma1": "sigma1 N_j(M, k) sigma1 = N_j(-M, -k)",
               "sigma3": "-sigma3 N_j(M, k) sigma3 = N_j(-M, k) (with y -> -y)",
               "antiunitary": "K N_j(M, k) K = N_{-j}(M, -k)", "sigma2K": "sigma2 K: (j, M, k) -> (j, -M, -k)"})
    A0s, A1s, A4s = mat_to_sympy(pa.gamma[0]), mat_to_sympy(mat_mul(pa.gamma[0], pa.gamma[1])), \
        mat_to_sympy(mat_mul(pa.gamma[0], pa.gamma[4]))

    def N16(M, k):
        return M * A0s - sp.I * KAPPA * k * A1s + sp.I * (EPS - VV) * A4s

    G8s, G1s = mat_to_sympy(pa.g8), mat_to_sympy(pa.gamma[1])
    rec.check("sixteenComponentODEMaps", sp.expand(G8s * N16(MM, KK) * G8s - N16(-MM, KK)) == sp.zeros(16)
              and sp.expand(G1s * N16(MM, KK) * G1s - N16(-MM, -KK)) == sp.zeros(16),
              "gamma^8 N(M, k) gamma^8 = N(-M, k), gamma^1 N(M, k) gamma^1 = N(-M, -k), "
              "N = M gamma^0 - i kappa k gamma^0 gamma^1 + i (eps - v_v) gamma^0 gamma^4")
    c1, c2, d1, d2 = sp.symbols("c1 c2 d1 d2")
    chi = sp.Matrix([c1, c2])
    dchi = sp.Matrix([d1, d2])
    hap = KS.block_hamiltonian_apply
    h_ok = (sp.expand(SIG2 * hap(chi, dchi) - hap(SIG2 * chi, SIG2 * dchi, M=-MM, j=-JS)) == sp.zeros(2, 1)
            and sp.expand(SIG1 * hap(chi, dchi) - hap(SIG1 * chi, SIG1 * dchi, M=-MM, k=-KK)) == sp.zeros(2, 1))
    rec.check("hamiltonianMaps", h_ok, "sigma2 h_j(M, k) = h_{-j}(-M, k) sigma2 and sigma1 h_j(M, k) = h_j(-M, -k) sigma1 as "
                                       "differential operators, v_v unchanged (h_j = j[-i sigma1 d_y + M sigma2 + kappa k "
                                       "sigma3] + v_v)")
    Pe = (I2 - SIG3) / 2
    Po = (I2 + SIG3) / 2
    rec.check("parityMap", SIG2 * Pe * SIG2 == Po and SIG1 * Pe * SIG1 == Po and SIG3 * Pe * SIG3 == Pe,
              "even parity chi_2(0) = 0 <-> odd parity chi_1(0) = 0 under sigma2 and sigma1 (p -> -p); unchanged "
              "under sigma3")
    Q = bag_Q(THETA)
    bag_ok = (sp.simplify(SIG2 * Q * SIG2 - bag_Q(sp.pi - THETA)) == sp.zeros(2)
              and sp.simplify(SIG1 * Q * SIG1 - bag_Q(THETA + sp.pi)) == sp.zeros(2)
              and sp.simplify(SIG3 * Q * SIG3 - bag_Q(-THETA)) == sp.zeros(2)
              and bag_Q(0) == SIG3 and sp.simplify(bag_Q(sp.pi) + SIG3) == sp.zeros(2)
              and sp.simplify(bag_Q(sp.pi - (-sp.pi / 2)) - bag_Q(-sp.pi / 2)) == sp.zeros(2)
              and sp.simplify(bag_Q(-sp.pi / 2 + sp.pi) - bag_Q(sp.pi / 2)) == sp.zeros(2))
    rec.check("bagAngleMap", bag_ok,
              {"sigma2": "sigma2 Q(theta) sigma2 = Q(pi - theta)", "sigma1": "sigma1 Q(theta) sigma1 = Q(theta + pi)",
               "sigma3": "sigma3 Q(theta) sigma3 = Q(-theta)",
               "stage4Default": "theta = 0 (chi_2(-L) = 0) -> theta = pi (chi_1(-L) = 0) under sigma2 and sigma1",
               "asymptoticBag": "theta(k) = -sgn(k) pi/2 is mapped onto itself (sigma2: same k; sigma1: k -> -k)"})
    a, b = sp.symbols("a b")
    rust = sp.expand(SIG2 * sp.Matrix([a, sp.I * b]) - sp.Matrix([b, sp.I * a])) == sp.zeros(2, 1)
    rec.check("sigma2IsRustSwap", rust, "chi = (a, i b): sigma2 (a, i b) = (b, i a), the component swap a <-> b")
    x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2", real=True)
    ch = sp.Matrix([x1 + sp.I * y1, x2 + sp.I * y2])

    def dens(v, j):
        return [sp.expand((v.H * v)[0]), sp.expand(j * (v.H * SIG2 * v)[0]), sp.expand(j * (v.H * SIG3 * v)[0]),
                sp.expand(j * (v.H * SIG1 * v)[0])]

    base = dens(ch, JS)
    maps = {"sigma2": dens(SIG2 * ch, -JS), "sigma1": dens(SIG1 * ch, JS), "sigma3": dens(SIG3 * ch, JS)}
    signs = {}
    for name, vals in maps.items():
        sg = []
        for x, y in zip(vals, base):
            sg.append(1 if sp.expand(x - y) == 0 else (-1 if sp.expand(x + y) == 0 else 0))
        signs[name] = sg
    rec.check("densityAndCurrentMaps", signs == {"sigma2": [1, -1, 1, 1], "sigma1": [1, -1, -1, 1], "sigma3": [1, -1, 1, -1]},
              {"signs (n, s, t, c)": signs, "densities": "n = chi^dagger chi, s = j chi^dagger sigma2 chi, t = j chi^dagger "
                                                        "sigma3 chi, c = j chi^dagger sigma1 chi",
               "imageRule": "with the Krein metric -B of the gamma^8 image every one-body density flips in addition: "
                            "sigma2 route (n, s, t, c) -> (-n, s, -t, -c)"})
    rec.measure("densitySigns", signs)
    # 16-component version on the Stage-4 basis: u -> gamma^8 u, standard rule and image rule
    rule = {"n": pa.I16, "s": pa.BC, "t": mat_neg(mat_mul(pa.gamma[4], pa.gamma[1])), "c": mat_mul(pa.gamma[0], pa.gamma[4])}
    rng = random.Random(91)
    ok16 = True
    for bidx in (0, 3, 5):
        blk = blocks[bidx]
        xs = [CQ(rng.randint(-5, 5), rng.randint(-5, 5)) for _ in range(2)]
        u = [blk["vPlus"][i] * xs[0] + blk["vMinus"][i] * xs[1] for i in range(16)]
        u8 = mat_apply(pa.g8, u)
        for name, R in rule.items():
            v0 = vec_dot(u, mat_apply(R, u))
            v1 = vec_dot(u8, mat_apply(R, u8))
            expected = {"n": 1, "s": -1, "t": 1, "c": 1}[name]
            ok16 &= v1 == v0 * expected
            # image rule: the rule matrix B M -> (-B) M
            vimg = vec_dot(u8, mat_apply(mat_neg(R), u8))
            ok16 &= vimg == v0 * (-expected)
    rec.check("densityMaps16", ok16, "on 16-component orbitals of the Stage-4 blocks: u -> gamma^8 u gives (n, s, t, c) -> "
                                     "(n, -s, t, c) with the standard rule and (-n, s, -t, -c) with the image rule")
    # potentials (sg symbolic, sg^2 = 1)
    vs = SG * LAMS * SS / 16
    vv = SG * LAMS * NS / 16
    meff = MSY + LAMS * SS + vs
    energy = LAMS / 2 * SS ** 2 + SG * LAMS / 32 * (NS ** 2 + SS ** 2)
    std = {MSY: -MSY, SS: -SS}
    img = {MSY: -MSY, LAMS: -LAMS, NS: -NS}
    wrong = {MSY: -MSY, LAMS: -LAMS, SS: -SS}
    pot_std = (sp.expand(meff.subs(std, simultaneous=True) + meff) == 0 and sp.expand(vv.subs(std, simultaneous=True) - vv) == 0
               and sp.expand(vs.subs(std, simultaneous=True) + vs) == 0 and sp.expand(energy.subs(std, simultaneous=True) - energy) == 0)
    fail_lam = sp.expand(meff.subs(wrong, simultaneous=True) + meff)
    rec.check("potentialsStandardRule", pot_std and sp.simplify(fail_lam - 2 * LAMS * SS * (1 + SG / 16)) == 0,
              {"map": "(m, lam, n, S) -> (-m, lam, n, -S): M_eff -> -M_eff, v_s -> -v_s, v_v -> v_v, e_H + e_x invariant",
               "withMinusLambda": "M_eff(-m, -lam, n, -S) + M_eff = 2 lam S (1 + sg/16) != 0: fails for lam S != 0"})
    pot_img = (sp.expand(meff.subs(img, simultaneous=True) + meff) == 0 and sp.expand(vv.subs(img, simultaneous=True) - vv) == 0
               and sp.expand(energy.subs(img, simultaneous=True) + energy) == 0)
    rec.check("potentialsImageRule", pot_img,
              "(m, lam, n, S) -> (-m, -lam, -n, S): M_eff -> -M_eff, v_v -> v_v, e_H + e_x -> -(e_H + e_x)")
    coeffs = {int(s): sp.nsimplify(sp.expand(meff.subs(SG, s) - MSY).coeff(LAMS * SS)) for s in (-1, 1)}
    rec.check("statisticsCoefficients", coeffs == {-1: sp.Rational(15, 16), 1: sp.Rational(17, 16)},
              {"M_eff": "m + (1 + sg/16) lam S_p", "dirac16complex": "m + (15/16) lam S_p",
               "dirac16complex00": "m + (17/16) lam S_p"})
    return rec, {"phases8": phases8, "phases1": phases1, "targets": targets, "densitySigns": signs}


# CHUNK-9-END

# ---------------------------------------------------------------------------
# 10. Family "T3ks": the Kohn-Sham functional and operator, exact k = 0 solutions
# ---------------------------------------------------------------------------

class KSModel:
    """Two orbitals chi_i (block labels j_i, occupations f_i) with independent symbols for chi, chi^* and chi';
    energy density per unit y (w = e^{6Hy} l^3 the proper-volume weight):
      e = sum_i f_i chi_i^dagger h0_{j_i}(m) chi_i + w [ (lam/2) S_p^2 + sg (lam/32)(n_p^2 + S_p^2) ],
      n_p = sum f chi^dagger chi / w, S_p = sum f j chi^dagger sigma2 chi / w,
      h0_j(m) = j[-i sigma1 d_y + m sigma2 + kappa k sigma3]."""

    def __init__(self):
        self.f = sp.symbols("f1 f2", positive=True)
        self.j = sp.symbols("j1 j2", real=True)
        self.w = sp.Symbol("w", positive=True)
        self.x = [sp.Matrix(sp.symbols("x%d_1:3" % i)) for i in (1, 2)]
        self.xb = [sp.Matrix(sp.symbols("xb%d_1:3" % i)) for i in (1, 2)]
        self.dx = [sp.Matrix(sp.symbols("dx%d_1:3" % i)) for i in (1, 2)]

    @staticmethod
    def h0(x, dx, j, m, k):
        return j * (-sp.I * SIG1 * dx + m * SIG2 * x + KAPPA * k * SIG3 * x)

    def densities(self, x, xb, j):
        n = sum(self.f[i] * (xb[i].T * x[i])[0] for i in range(2)) / self.w
        S = sum(self.f[i] * j[i] * (xb[i].T * SIG2 * x[i])[0] for i in range(2)) / self.w
        return n, S

    def energy(self, x, xb, dx, j, m, lam, k, sign_one_body=1):
        n, S = self.densities(x, xb, j)
        n, S = n * sign_one_body, S * sign_one_body
        kin = sum(self.f[i] * (xb[i].T * self.h0(x[i], dx[i], j[i], m, k))[0] for i in range(2)) * sign_one_body
        return sp.expand(kin + self.w * (lam / 2 * S ** 2 + SG * lam / 32 * (n ** 2 + S ** 2)))

    @staticmethod
    def hks(x, dx, j, m, lam, n, S, k):
        meff = m + lam * S + SG * lam / 16 * S
        vv = SG * lam / 16 * n
        return j * (-sp.I * SIG1 * dx + meff * SIG2 * x + KAPPA * k * SIG3 * x) + vv * x

    def reduce_j(self, expr):
        return sp.expand(sp.expand(expr).subs({self.j[0] ** 2: 1, self.j[1] ** 2: 1, SG ** 2: 1}))


def exact_zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def check_t3ks(pa, quick=False):
    rec = Recorder("T3ks")
    km = KSModel()
    x, xb, dx, j = km.x, km.xb, km.dx, list(km.j)
    m, lam, k = MSY, LAMS, KK
    e = km.energy(x, xb, dx, j, m, lam, k)
    n, S = km.densities(x, xb, j)
    stat_ok = True
    for i in range(2):
        grad = sp.Matrix([sp.diff(e, xb[i][r]) for r in range(2)])
        target = km.f[i] * km.hks(x[i], dx[i], j[i], m, lam, n, S, k)
        stat_ok &= all(km.reduce_j(grad[r] - target[r]) == 0 for r in range(2))
    rec.check("stationarityBothStatistics", stat_ok,
              "d e / d chi_i^* = f_i h_KS chi_i with h_KS = j[-i sigma1 d_y + M_eff sigma2 + kappa k sigma3] + v_v, "
              "M_eff = m + lam S_p + v_s, v_s = sg (lam/16) S_p, v_v = sg (lam/16) n_p (sg symbolic: both statistics)")
    # sigma2 route: chi -> sigma2 chi, chi^* -> conj(sigma2) chi^* = -sigma2 chi^*, j -> -j, m -> -m, the SAME lambda
    x2 = [SIG2 * v for v in x]
    xb2 = [-SIG2 * v for v in xb]
    dx2 = [SIG2 * v for v in dx]
    j2 = [-v for v in j]
    e2 = km.energy(x2, xb2, dx2, j2, -m, lam, k)
    rec.check("sigma2FunctionalInvariant", km.reduce_j(e2 - e) == 0,
              "E[sigma2 chi; j -> -j, -m, lam] = E[chi; j, m, lam] for sg = +-1 (entropy terms depend on f only)")
    n2, S2 = km.densities(x2, xb2, j2)
    rec.check("sigma2Densities", km.reduce_j(n2 - n) == 0 and km.reduce_j(S2 + S) == 0, "n_p -> n_p, S_p -> -S_p")
    eq_ok = True
    fail_ok = True
    for i in range(2):
        lhs = SIG2 * km.hks(x[i], dx[i], j[i], m, lam, n, S, k)
        rhs = km.hks(x2[i], dx2[i], j2[i], -m, lam, n, -S, k)
        eq_ok &= all(km.reduce_j(lhs[r] - rhs[r]) == 0 for r in range(2))
        wrong = km.hks(x2[i], dx2[i], j2[i], -m, -lam, n, -S, k)
        fail_ok &= any(km.reduce_j(lhs[r] - wrong[r]) != 0 for r in range(2))
    rec.check("sigma2KSOperatorEquivariant", eq_ok and fail_ok,
              {"statement": "sigma2 h_KS,j[m, lam; n, S] = h_KS,-j[-m, lam; n, -S] sigma2: the SCF map is equivariant",
               "negativeControl": "the ordinary KS problem with -lam (and the mapped densities) does NOT map"})
    x1 = [SIG1 * v for v in x]
    xb1 = [SIG1 * v for v in xb]
    dx1 = [SIG1 * v for v in dx]
    e1 = km.energy(x1, xb1, dx1, j, -m, lam, -k)
    rec.check("sigma1FunctionalInvariant", km.reduce_j(e1 - e) == 0,
              "sigma1 route (gamma^1: same j, k -> -k): E[sigma1 chi; -m, -k] = E[chi; m, k] (closed shells {k, -k})")
    eimg = km.energy(x2, xb2, dx2, j2, -m, -lam, k, sign_one_body=-1)
    img_eq = True
    nI, SI = -n2, -S2
    for i in range(2):
        lhs = SIG2 * km.hks(x[i], dx[i], j[i], m, lam, n, S, k)
        rhs = km.hks(x2[i], dx2[i], j2[i], -m, -lam, nI, SI, k)
        img_eq &= all(km.reduce_j(lhs[r] - rhs[r]) == 0 for r in range(2))
    rec.check("imageRuleEnergyOdd", km.reduce_j(eimg + e) == 0 and img_eq and km.reduce_j(nI + n) == 0
              and km.reduce_j(SI - S) == 0,
              "Krein image (metric -B, -lam): n -> -n, S -> S, E -> -E (the (-m, -lam) formulas evaluated on the "
              "image, T1krein), and the image orbitals sigma2 chi solve the KS equations of (-m, -lam) with the image "
              "densities")
    epsl, mu, T, ff = sp.symbols("epsilon mu T f", real=True)
    fd = 1 / (sp.exp((epsl - mu) / T) + 1)
    fd_img = 1 / (sp.exp((-epsl + mu) / (-T)) + 1)
    Eb, Sent = sp.symbols("E S_ent", real=True)
    dF_plus = epsl - mu + T * sp.log(ff / (1 - ff))
    dF_img = -epsl + mu + (-T) * sp.log(ff / (1 - ff))
    rec.check("occupationsAndTemperature", sp.simplify(fd - fd_img) == 0 and sp.expand(dF_img + dF_plus) == 0
              and sp.expand((-Eb - (-T) * Sent) + (Eb - T * Sent)) == 0,
              "f_FD(eps; mu, T) = f_FD(-eps; -mu, -T); the Mermin stationarity eps - mu + T ln(f/(1-f)) = 0 maps onto itself "
              "for (-eps, -mu, -T): the image is a stationary state of F_- at temperature -T, F_-(-T) = -F_+(T)")
    # ---- exact k = 0 solutions (constant M > 0, v_v = 0) ----
    Y_, H_, A4_ = KS.Y, KS.H, KS.A4C
    Mp = sp.Symbol("M", positive=True)
    Lp = sp.Symbol("L", positive=True)

    def N0(M, jv, eps):
        return KS.block_ode_matrix(M=M, k=0, eps=eps, vv=0, j=jv)

    def solves(vec, M, jv, eps):
        return sp.simplify(sp.diff(vec, Y_) - N0(M, jv, eps) * vec) == sp.zeros(2, 1)

    zp = sp.Matrix([sp.exp(Mp * Y_), 0])
    zp_ok = all(solves(zp, Mp, jv, 0) for jv in (1, -1)) and zp[1] == 0
    rec.check("zeroModePlusM", zp_ok, "+M, even parity chi_2(0) = 0, bag theta = 0 (chi_2(-L) = 0): chi = (e^{My}, 0), eps = 0")
    zi = SIG2 * zp
    zi_ok = all(solves(zi, -Mp, -jv, 0) for jv in (1, -1)) and zi[0] == 0
    rec.check("zeroModeImage", zi_ok, "image sigma2 chi = (0, i e^{My}) solves the -M block (-j) with chi_1 = 0 at y = 0 and y = -L "
                                      "(odd parity, theta = pi)")
    zc = sp.Matrix([sp.exp(-Mp * Y_), 0])
    ratio_c = sp.simplify((zc[0] ** 2).subs(Y_, 0) / (zc[0] ** 2).subs(Y_, -Lp))
    ratio_p = sp.simplify((zp[0] ** 2).subs(Y_, 0) / (zp[0] ** 2).subs(Y_, -Lp))
    rec.check("zeroModeUntransformedControl", all(solves(zc, -Mp, jv, 0) for jv in (1, -1)) and zc[1] == 0
              and sp.simplify(ratio_c - sp.exp(-2 * Mp * Lp)) == 0 and sp.simplify(ratio_p - sp.exp(2 * Mp * Lp)) == 0,
              {"statement": "-M with the untransformed BCs (even parity, theta = 0): chi = (e^{-My}, 0), eps = 0, localised "
                            "at the tip", "braneToTipDensityRatio": {"control": str(ratio_c), "+M": str(ratio_p)}})
    kap = sp.exp(-H_ * Y_ - A4_)

    def splitting(vec):
        dens = sp.simplify(vec[0] * sp.conjugate(vec[0]) + vec[1] * sp.conjugate(vec[1]))
        sig3 = sp.simplify(vec[0] * sp.conjugate(vec[0]) - vec[1] * sp.conjugate(vec[1]))
        return sp.simplify(sp.integrate(kap * sig3, (Y_, -Lp, 0), conds="none") / sp.integrate(dens, (Y_, -Lp, 0), conds="none"))

    c_plus = splitting(zp)                     # <sigma3 kappa> with dh_j/dk = j kappa sigma3
    c_image = -splitting(zi)                   # block -j: dh/dk = -j kappa sigma3
    c_ctrl = splitting(zc)
    c_closed = sp.exp(-A4_) * (2 * Mp / (2 * Mp - H_)) * (1 - sp.exp(-(2 * Mp - H_) * Lp)) / (1 - sp.exp(-2 * Mp * Lp))
    c_ctrl_closed = sp.exp(-A4_) * (2 * Mp / (2 * Mp + H_)) * (sp.exp((2 * Mp + H_) * Lp) - 1) / (sp.exp(2 * Mp * Lp) - 1)
    rec.check("zeroModeSplittingMapsExactly", sp.simplify(c_plus - c_closed) == 0 and sp.simplify(c_image - c_plus) == 0,
              {"c(M)": str(c_closed), "note": "d eps/dk|_0 = j c(M) for +M (block j) and for the image (block -j, sigma3 = -1)"})
    rec.check("controlSplittingClosedForm", sp.simplify(c_ctrl - c_ctrl_closed) == 0, {"c_ctrl": str(c_ctrl_closed)})
    Yv = sp.Symbol("Yv", positive=True)
    tpos = sp.Symbol("t", positive=True)
    diff_target = sp.Rational(2, 3) * (Yv - 1) ** 2 / (Yv + 1)
    at_h = sp.simplify((c_ctrl_closed - c_closed).subs(Mp, H_).subs(A4_, 0)
                       - diff_target.subs(Yv, sp.exp(H_ * Lp)))
    positive = sp.simplify(diff_target.subs(Yv, 1 + tpos)).is_positive
    num = {"cPlus": float(c_closed.subs({Mp: 1, H_: 1, Lp: 3, A4_: 0})),
           "cControl": float(c_ctrl_closed.subs({Mp: 1, H_: 1, Lp: 3, A4_: 0}))}
    rec.check("controlDiffersFromPairedProblem", at_h == 0 and positive is True,
              {"atMEqualsH": "c_ctrl - c(M) = (2/3)(Y - 1)^2/(Y + 1) > 0, Y = e^{HL} > 1 (a4 = 0)",
               "values_M1_H1_L3_a0 (float, labelled)": num})
    rec.measure("cValues_M1_H1_L3_a0_float", num)
    q = sp.Symbol("q", positive=True)
    nn = sp.Symbol("n", positive=True, integer=True)
    qn = nn * sp.pi / Lp
    ep = sp.sqrt(Mp ** 2 + qn ** 2)
    massive = sp.Matrix([(Mp * sp.sin(qn * Y_) + qn * sp.cos(qn * Y_)) / (sp.I * JS * ep), sp.sin(qn * Y_)])
    mimg = SIG2 * massive
    ctrl = sp.Matrix([(-Mp * sp.sin(qn * Y_) + qn * sp.cos(qn * Y_)) / (sp.I * JS * ep), sp.sin(qn * Y_)])
    mass_ok = True
    for jv in (1, -1):
        mass_ok &= solves(massive.subs(JS, jv), Mp, jv, ep) and solves(mimg.subs(JS, jv), -Mp, -jv, ep)
        mass_ok &= solves(ctrl.subs(JS, jv), -Mp, jv, ep)
    mass_ok &= (sp.simplify(massive[1].subs(Y_, 0)) == 0 and sp.simplify(massive[1].subs(Y_, -Lp)) == 0
                and sp.simplify(mimg[0].subs(Y_, 0)) == 0 and sp.simplify(mimg[0].subs(Y_, -Lp)) == 0)
    rec.check("massiveLevelsMap", mass_ok,
              "eps = +-sqrt(M^2 + (n pi/L)^2): the +M even/theta = 0 orbital maps onto a -M odd/theta = pi orbital at the same "
              "eps (these levels coincide also for the untransformed control)")
    epm = sp.sqrt(Mp ** 2 + q ** 2)
    mixed_p = sp.Matrix([sp.sin(q * Y_), (q * sp.cos(q * Y_) - Mp * sp.sin(q * Y_)) / (sp.I * JS * epm)])
    mixed_c = sp.Matrix([sp.sin(q * Y_), (q * sp.cos(q * Y_) + Mp * sp.sin(q * Y_)) / (sp.I * JS * epm)])
    mix_ok = True
    for jv in (1, -1):
        mix_ok &= solves(mixed_p.subs(JS, jv), Mp, jv, epm) and solves(mixed_c.subs(JS, jv), -Mp, jv, epm)
        mimg2 = SIG2 * mixed_p.subs(JS, jv)
        mix_ok &= solves(mimg2, -Mp, -jv, epm)
    cond_p = sp.simplify(mixed_p[1].subs(Y_, -Lp) * sp.I * JS * epm)
    cond_c = sp.simplify(mixed_c[1].subs(Y_, -Lp) * sp.I * JS * epm)
    img_cond = sp.simplify((SIG2 * mixed_p)[0].subs(Y_, -Lp) * sp.I * JS * epm / (-sp.I))
    mix_ok &= (sp.simplify(cond_p - (q * sp.cos(q * Lp) + Mp * sp.sin(q * Lp))) == 0
               and sp.simplify(cond_c - (q * sp.cos(q * Lp) - Mp * sp.sin(q * Lp))) == 0
               and sp.simplify(img_cond - cond_p) == 0 and mixed_p[0].subs(Y_, 0) == 0)
    rec.check("mixedSectorSolutions", mix_ok,
              {"+M": "odd parity chi_1(0) = 0, theta = 0: eps = +-sqrt(M^2 + q^2), q cos(qL) + M sin(qL) = 0",
               "control": "-M, same BCs: q cos(qL) - M sin(qL) = 0",
               "transformed": "-M, even parity with theta = pi (the image): the same condition as +M"})
    # disjointness: both conditions imply q cos(qL) = 0 and M sin(qL) = 0, impossible for M > 0
    s_, c_ = sp.symbols("s c", real=True)
    sol = sp.solve([q * c_ + Mp * s_, q * c_ - Mp * s_, s_ ** 2 + c_ ** 2 - 1], [s_, c_], dict=True)
    rec.check("controlMixedSectorLevelsDisjoint", sol == [],
              "q cos qL + M sin qL = 0 and q cos qL - M sin qL = 0 have no common solution (sin^2 + cos^2 = 1, M, q > 0)")
    kb = sp.Symbol("kappa_b", positive=True)
    eb = sp.sqrt(Mp ** 2 - kb ** 2)
    bound_c = sp.Matrix([sp.sinh(kb * Y_), (kb * sp.cosh(kb * Y_) + Mp * sp.sinh(kb * Y_)) / (sp.I * JS * eb)])
    bound_p = sp.Matrix([sp.sinh(kb * Y_), (kb * sp.cosh(kb * Y_) - Mp * sp.sinh(kb * Y_)) / (sp.I * JS * eb)])
    b_ok = all(solves(bound_c.subs(JS, jv), -Mp, jv, eb) and solves(bound_p.subs(JS, jv), Mp, jv, eb) for jv in (1, -1))
    cond_bc = sp.simplify(bound_c[1].subs(Y_, -Lp) * sp.I * JS * eb)
    cond_bp = sp.simplify(bound_p[1].subs(Y_, -Lp) * sp.I * JS * eb)
    b_ok &= sp.simplify(cond_bc - (kb * sp.cosh(kb * Lp) - Mp * sp.sinh(kb * Lp))) == 0
    b_ok &= sp.simplify(cond_bp - (kb * sp.cosh(kb * Lp) + Mp * sp.sinh(kb * Lp))) == 0     # > 0: no +M bound state
    f_half = sp.tanh(sp.Rational(3, 2)) - sp.Rational(1, 2)
    f_one = sp.tanh(3) - 1
    sign_ok = bool(sp.simplify(sp.exp(3) - 3) > 0) and bool(f_one < 0) and bool(f_half > 0)
    root = mpmath.findroot(lambda z: mpmath.tanh(3 * z) - z, 0.9)
    rec.check("controlSubGapBoundState", b_ok and sign_ok and 0.5 < float(root) < 1,
              {"statement": "control (-M, odd parity, theta = 0): chi = (sinh(ky), ...), |eps| = sqrt(M^2 - k^2) < M with "
                            "tanh(kL) = k/M: a root k in (0, M) iff ML > 1; +M: k cosh kL + M sinh kL > 0, no bound state",
               "M1_L3": "tanh(3/2) > 1/2 (e^3 > 3) and tanh(3) < 1: root in (1/2, 1)",
               "root_float_labelled": float(root)})
    return rec, {"cPlus": c_closed, "cControl": c_ctrl_closed, "cValues": num}


# CHUNK-10-END

# ---------------------------------------------------------------------------
# 11. Family "T3emt": 16-component orbital EMT kernels in the static field (y < 0)
#     Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y), chi' = N chi on shell
# ---------------------------------------------------------------------------

def sparse16(cq_matrix):
    return sp.SparseMatrix(16, 16, {(i, l): v.to_sympy() for i, row in enumerate(cq_matrix)
                                    for l, v in enumerate(row) if not v.is_zero()})


def sympy_block(M, blk):
    """(v_r^dagger M v_c)/8 on the block's basis (M a sympy 16x16 matrix)."""
    vs = [sp.Matrix([v.to_sympy() for v in blk["vPlus"]]), sp.Matrix([v.to_sympy() for v in blk["vMinus"]])]
    return sp.Matrix(2, 2, lambda r, c: sp.expand((vs[r].H * M * vs[c])[0] / 8))


class OrbitalEMT:
    """X_{mu nu}(m, M_eff): chi^dagger X chi = W^6 x (classical bilinear T_{mu nu}) with Psibar = Psi^dagger C;
    with the expectation rule the orbital value is chi^dagger B X chi."""

    def __init__(self, pa):
        self.pa = pa
        Yp = KS.Y
        W = sp.exp(KS.H * Yp)
        self.h = [sp.Integer(1)] + [W * sp.exp(KS.A4C)] * 3 + [sp.Integer(1)] + [W * sp.exp(-KS.A4C)] * 3
        _, lowered, _, ok = KS.spin_connection(self.h, [Yp] + list(sp.symbols("x1:8", real=True)))
        self.connection_ok = ok
        self.Om = [sp.SparseMatrix(M) for M in KS.omega_matrices(pa.alg, lowered)]
        self.G = [sparse16(g) for g in pa.gamma]
        self.C = sparse16(pa.C)
        self.B = sparse16(pa.B)
        self.G8 = sparse16(pa.g8)
        self.cache = {}

    def kernels(self, m, M):
        key = (str(m), str(M))
        if key in self.cache:
            return self.cache[key]
        G, C, Om, h = self.G, self.C, self.Om, self.h
        I16 = sp.SparseMatrix(sp.eye(16))
        N = M * G[0] - sp.I * KAPPA * KK * (G[0] * G[1]) + sp.I * (EPS - VV) * (G[0] * G[4])
        Nd = N.H                                                    # N^dagger (all parameters real)
        dpart = {0: N - 3 * KS.H * I16, 1: sp.I * KK * I16, 4: -sp.I * EPS * I16}
        dpart_bar = {0: Nd - 3 * KS.H * I16, 1: -sp.I * KK * I16, 4: sp.I * EPS * I16}
        zero = sp.SparseMatrix(16, 16, {})
        Dop = [dpart.get(nu, zero) + Om[nu] for nu in range(8)]
        Dbar = [dpart_bar.get(mu, zero) * C - C * Om[mu] for mu in range(8)]          # (D_mu Psibar) = chi^dagger Dbar_mu
        glow = [ETA[a] * h[a] * G[a] for a in range(8)]
        gup = [G[a] / h[a] for a in range(8)]
        XL = zero
        for mu in range(8):
            XL = XL + sp.Rational(1, 2) * (C * gup[mu] * Dop[mu] - Dbar[mu] * gup[mu])
        XL = XL - m * C
        X = {}
        for mu in range(8):
            for nu in range(mu, 8):
                A = C * glow[mu] * Dop[nu] + C * glow[nu] * Dop[mu] - Dbar[mu] * glow[nu] - Dbar[nu] * glow[mu]
                val = -sp.Rational(1, 4) * A
                if mu == nu:
                    val = val + ETA[mu] * h[mu] ** 2 * XL
                X[(mu, nu)] = X[(nu, mu)] = val.applyfunc(sp.expand)
        self.cache[key] = (X, XL.applyfunc(sp.expand))
        return self.cache[key]


def sparse_is_zero(M):
    return all(sp.simplify(v) == 0 for v in M.values())


def check_t3emt(pa, red, quick=False):
    rec = Recorder("T3emt")
    oe = OrbitalEMT(pa)
    X, _ = oe.kernels(MSY, MM)
    Xm, _ = oe.kernels(-MSY, -MM)
    G8, B = oe.G8, oe.B
    comps = [(mu, nu) for mu in range(8) for nu in range(8)]
    if quick:
        comps = [(0, 0), (1, 1), (4, 4), (1, 4), (0, 4), (5, 5)]
    op_ok = oe.connection_ok
    std_ok = True
    img_ok = True
    for c in comps:
        lhs = (G8 * Xm[c] * G8).applyfunc(sp.expand)
        op_ok &= sparse_is_zero(lhs + X[c])
        std_ok &= sparse_is_zero((G8 * B * Xm[c] * G8 - B * X[c]).applyfunc(sp.expand))
        img_ok &= sparse_is_zero((G8 * (-B) * Xm[c] * G8 + B * X[c]).applyfunc(sp.expand))
    rec.check("gamma8OperatorIdentity64", op_ok, {"components": len(comps),
                                                  "statement": "gamma^8 X_{mu nu}(-m, -M_eff) gamma^8 = -X_{mu nu}(m, M_eff)"})
    rec.check("standardRulePlusT", std_ok,
              "(gamma^8 chi)^dagger B X(-m, -M_eff) (gamma^8 chi) = chi^dagger B X(m, M_eff) chi: T -> +T (gamma^8 B gamma^8 = -B)")
    rec.check("imageRuleMinusT", img_ok, "with the Krein metric -B of the image: T -> -T (the (-m, -lam) formula; "
                                         "relative to the image's own canonical structure its source is +T, T1krein)")
    # Stage-4 cross-check on the blocks (expectation rule: chi^dagger B X chi)
    expected = {
        (4, 4): {"n": EPS - VV, "s": -(MM - MSY), "t": 0, "c": 0},
        (0, 0): {"n": EPS, "s": -MSY, "t": -KAPPA * KK, "c": 0},
        (1, 1): {"n": VV, "s": MM - MSY, "t": KAPPA * KK, "c": 0},
        (2, 2): {"n": VV, "s": MM - MSY, "t": 0, "c": 0},
        (3, 3): {"n": VV, "s": MM - MSY, "t": 0, "c": 0},
        (5, 5): {"n": VV, "s": MM - MSY, "t": 0, "c": 0},
    }
    names = {(4, 4): "rho = T_44", (0, 0): "p_y = T_00", (1, 1): "p_1 = T^1_1", (2, 2): "p_2 = T^2_2", (3, 3): "p_3 = T^3_3",
             (5, 5): "p_t = T^5_5"}
    found = {}
    cross_ok = True
    for bidx in (0, 4):
        blk = red.blocks[bidx]
        jv = blk["j"]
        for c, exp in expected.items():
            Q = sympy_block(sp.Matrix(B * X[c]), blk)
            if c in ((1, 1), (2, 2), (3, 3), (5, 5)):
                Q = Q / (ETA[c[0]] * oe.h[c[0]] ** 2)
            coeffs, exact = KS.sesquilinear_coefficients(Q, jv)
            ok = exact and all(sp.simplify(coeffs[k] - exp[k]) == 0 for k in ("n", "s", "t", "c"))
            cross_ok &= ok
            if bidx == 0:
                found[names[c]] = {k: str(sp.simplify(v)) for k, v in coeffs.items()}
    rec.check("stage4CrossCheck", cross_ok,
              {"orbitalEMT": found, "blocks": [0, 4],
               "statement": "reduced to the Stage-4 blocks the kernels give rho = (eps - v_v) n - (M_eff - m) s, "
                            "p_y = eps n - m s - kappa k t, p_1 = v_v n + (M_eff - m) s + kappa k t, "
                            "p_2 = p_3 = p_t = v_v n + (M_eff - m) s (per e^{-6Hy}/l^3; STAGE4 emt family)"})
    # block-level invariance of the orbital formulas (standard rule: (n, s, t, c) -> (n, -s, t, c), m, M -> -m, -M)
    n_, s_, t_, c_ = sp.symbols("n_o s_o t_o c_o", real=True)
    forms = {k: v["n"] * n_ + v["s"] * s_ + v["t"] * t_ + v["c"] * c_ for k, v in expected.items()}
    std_map = {MSY: -MSY, MM: -MM, s_: -s_}
    img_map = {MSY: -MSY, MM: -MM, n_: -n_, t_: -t_, c_: -c_}
    blk_ok = all(sp.expand(f.subs(std_map, simultaneous=True) - f) == 0 for f in forms.values()) and \
        all(sp.expand(f.subs(img_map, simultaneous=True) + f) == 0 for f in forms.values())
    eHx = sp.Symbol("eHx", real=True)
    rho_ks = forms[(4, 4)] + eHx
    rec.check("orbitalFormulasMap", blk_ok and sp.expand(rho_ks.subs(std_map, simultaneous=True) - rho_ks) == 0,
              "the per-orbital rho, p_y, p_(i) are invariant under the standard-rule map and change sign under the image "
              "rule; the interaction part e_H + e_x is invariant (standard) / odd (image, -lam), so the KS-state EMT maps "
              "the same way")
    rec.check("connectionClosedForms",
              all(sp.simplify(sp.Matrix(oe.Om[i]) + sp.diff(sp.exp(KS.H * KS.Y), KS.Y) * sp.exp(KS.A4C)
                              * mat_to_sympy(mat_scale(pa.biv[(0, i)], Fraction(1, 2)))) == sp.zeros(16) for i in (1, 2, 3))
              and all(sp.simplify(sp.Matrix(oe.Om[i]) - sp.diff(sp.exp(KS.H * KS.Y), KS.Y) * sp.exp(-KS.A4C)
                                  * mat_to_sympy(mat_scale(pa.biv[(0, i)], Fraction(1, 2)))) == sp.zeros(16) for i in (5, 6, 7))
              and all(sp.Matrix(oe.Om[i]) == sp.zeros(16) for i in (0, 4)),
              "own spin connection: Omega_i = -W' e^{a4} S^{0i} (i = 1..3), Omega_j = +W' e^{-a4} S^{0j} (j = 5..7), "
              "Omega_y = Omega_4 = 0 (the Stage-4 closed forms)")
    return rec, found


# CHUNK-11-END

# ---------------------------------------------------------------------------
# 12. Family "stat": the statistics (Wick) sign, exactly
# ---------------------------------------------------------------------------

def cayley_unitary(K):
    """U = (1 - K)(1 + K)^{-1} for an anti-Hermitian Gaussian-rational K (exactly unitary)."""
    n = len(K)
    ident = mat_eye(n)
    return mat_mul(mat_sub(ident, K), mat_inverse_cq(mat_add(ident, K)))


STAT_K = {
    "U1": [[CQ(0, 1), CQ(1), CQ(0), CQ(2, 1)], [CQ(-1), CQ(0, -2), CQ(0, 1), CQ(0)],
           [CQ(0), CQ(0, 1), CQ(0, 1), CQ(1, -1)], [CQ(-2, 1), CQ(0), CQ(-1, -1), CQ(0, 3)]],
    "U2": [[CQ(0, 2), CQ(1, 2), CQ(-1), CQ(0)], [CQ(-1, 2), CQ(0), CQ(0, 1), CQ(3)],
           [CQ(1), CQ(0, 1), CQ(0, -1), CQ(1, 1)], [CQ(0), CQ(-3), CQ(-1, 1), CQ(0, 1)]],
}
STAT_A = [[CQ(2), CQ(1, 1), CQ(0, -1), CQ(3)], [CQ(1, -1), CQ(-1), CQ(2, 1), CQ(0)],
          [CQ(0, 1), CQ(2, -1), CQ(3), CQ(-1, 1)], [CQ(3), CQ(0), CQ(-1, -1), CQ(-2)]]
STAT_B = [[CQ(-1), CQ(0, 2), CQ(1), CQ(1, 1)], [CQ(0, -2), CQ(4), CQ(0), CQ(2, -3)],
          [CQ(1), CQ(0), CQ(1), CQ(0, 1)], [CQ(1, -1), CQ(2, 3), CQ(0, -1), CQ(-3)]]
FERMION_OCCUPATIONS = [(1, 0, 1, 0), (1, 1, 0, 0), (Fraction(1, 3), Fraction(2, 5), Fraction(1, 7), Fraction(3, 4)),
                       (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))]


def is_hermitian(M):
    return mat_eq(mat_dagger(M), M)


def rho_matrix(U, f):
    """rho = U diag(f) U^dagger (rho_ba = <psi_a^dagger psi_b>)."""
    n = len(U)
    D = [[CQ(f[i]) if i == j else CQ_ZERO for j in range(n)] for i in range(n)]
    return mat_mul_many(U, D, mat_dagger(U))


def wick_prediction(A, Bm, rho, sign):
    tA = mat_trace(mat_mul(A, rho))
    tB = mat_trace(mat_mul(Bm, rho))
    ex = mat_trace(mat_mul_many(A, rho, Bm, rho))
    return tA * tB + ex * sign, mat_trace(mat_mul_many(A, Bm, rho))


class FermionWick:
    """Exact Fock space of 4 fermion modes; diagonal parts of the quartic words (state independent)."""

    def __init__(self):
        self.fs = KS.FockSpace(4)
        c, cd = self.fs.b, self.fs.bdag
        self.normal = {}
        self.product = {}
        rng4 = range(4)
        for n in rng4:
            for p in rng4:
                left = mat_mul(cd[n], cd[p])
                for q in rng4:
                    for mm in rng4:
                        X = mat_mul(left, mat_mul(c[q], c[mm]))          # c_n^+ c_p^+ c_q c_m
                        self.normal[(n, mm, p, q)] = [X[s][s] for s in range(16)]
        for n in rng4:
            for mm in rng4:
                left = mat_mul(cd[n], c[mm])
                for p in rng4:
                    for q in rng4:
                        X = mat_mul(left, mat_mul(cd[p], c[q]))          # c_n^+ c_m c_p^+ c_q
                        self.product[(n, mm, p, q)] = [X[s][s] for s in range(16)]

    @staticmethod
    def weights(f):
        """Diagonal of D = prod_n [(1 - f_n) c_n c_n^+ + f_n c_n^+ c_n] in the occupation basis."""
        out = []
        for s in range(16):
            w = Fraction(1)
            for n in range(4):
                w *= Fraction(f[n]) if (s >> n) & 1 else 1 - Fraction(f[n])
            out.append(CQ(w))
        return out

    def expectation(self, A, Bm, U, f, normal=True):
        At = mat_mul_many(mat_dagger(U), A, U)
        Bt = mat_mul_many(mat_dagger(U), Bm, U)
        w = self.weights(f)
        table = self.normal if normal else self.product
        total = CQ_ZERO
        for (n, mm, p, q), diag in table.items():
            coefficient = At[n][mm] * Bt[p][q]
            if coefficient.is_zero():
                continue
            value = sum((w[s] * diag[s] for s in range(16) if not diag[s].is_zero()), CQ_ZERO)
            total = total + coefficient * value
        return total


def boson_diagonal(word, ks):
    """<k| word |k> for a word [(mode, dagger), ...] (applied right to left) on number states with symbolic k."""
    shift = [0] * len(ks)
    coefficient = sp.Integer(1)
    for mode, dagger in reversed(word):
        if dagger:
            coefficient *= sp.sqrt(ks[mode] + shift[mode] + 1)
            shift[mode] += 1
        else:
            coefficient *= sp.sqrt(ks[mode] + shift[mode])
            shift[mode] -= 1
    if any(shift):
        return sp.Integer(0)
    return sp.expand(coefficient)


def moment_substitute(poly, ks, moments):
    """E[poly(k)] for independent modes with E[k_n^e] = moments[n][e]."""
    poly = sp.Poly(sp.expand(poly), *ks)
    total = 0
    for exps, coefficient in poly.terms():
        term = coefficient
        for n, e in enumerate(exps):
            term *= moments[n][e]
        total += term
    return sp.expand(total)


def sym_matrix(M):
    return sp.Matrix([[v.to_sympy() for v in row] for row in M])


# CHUNK-12A-END

def moving_shell_modes(red, m=7, p=24, E=25):
    """Joint eigenvectors of h_p = -i m gamma^4 - p gamma^4 gamma^1 (E = 25) and B, exact: in the Stage-4 blocks
    h_p = j (m sigma2 + p sigma3); (E + p, i m) and (p - E, i m) with E(E + p) = 35^2 give rational norms."""
    out = []
    for bidx, beta in ((0, 1), (2, -1)):
        blk = red.blocks[bidx]
        for eps, coeff, norm in ((E, (E + p, m), 140), (-E, (p - E, m), 20)):
            u = [(blk["vPlus"][i] * coeff[0] + blk["vMinus"][i] * CQ(0, coeff[1])) * Fraction(1, norm) for i in range(16)]
            out.append((u, eps, beta))
    return out


def check_stat(pa, red, quick=False):
    rec = Recorder("stat")
    A, Bm = STAT_A, STAT_B
    Us = {"identity": mat_eye(4)}
    anti_ok = True
    for name, K in STAT_K.items():
        anti_ok &= mat_eq(mat_dagger(K), mat_neg(K))
        Us[name] = cayley_unitary(K)
    unit_ok = all(mat_eq(mat_mul(mat_dagger(U), U), mat_eye(4)) for U in Us.values())
    rec.check("testUnitaries", anti_ok and unit_ok and is_hermitian(A) and is_hermitian(Bm),
              "three exact unitaries (identity and two Cayley transforms of anti-Hermitian Gaussian-integer matrices) and "
              "Hermitian A, B with Gaussian-integer entries")
    fw = FermionWick()
    qf_ok = True
    wick_ok = True
    control = False
    cases = []
    for uname, U in Us.items():
        for f in FERMION_OCCUPATIONS:
            w = fw.weights(f)
            qf_ok &= sum(w, CQ_ZERO) == CQ_ONE
            rho = rho_matrix(U, f)
            onebody = CQ_ZERO
            At = mat_mul_many(mat_dagger(U), A, U)
            for n in range(4):
                onebody = onebody + At[n][n] * CQ(f[n])
            qf_ok &= onebody == mat_trace(mat_mul(A, rho))
            pred, abr = wick_prediction(A, Bm, rho, -1)
            got_n = fw.expectation(A, Bm, U, f, normal=True)
            got_f = fw.expectation(A, Bm, U, f, normal=False)
            wick_ok &= got_n == pred and got_f == pred + abr
            wrong, _ = wick_prediction(A, Bm, rho, +1)
            control |= got_n != wrong
            cases.append({"basis": uname, "f": [frac_str(x) for x in f], "<:(psi^+ A psi)(psi^+ B psi):>": got_n.to_pair()})
    rec.check("fermionQuasiFreeStates", qf_ok, "D = prod_n [(1 - f_n) c c^+ + f_n c^+ c]: Tr D = 1, <psi^+ A psi> = Tr(A rho), "
                                              "rho = U diag(f) U^+ (pure Slater determinants and mixed states)")
    rec.check("fermionWickMinus", wick_ok and control,
              {"statement": "<:(psi^+ A psi)(psi^+ B psi):> = Tr(A rho) Tr(B rho) - Tr(A rho B rho); the full product adds "
                            "Tr(A B rho) (12 states: 3 bases x 4 occupation sets)", "cases": cases})
    # bosons: exact thermal series (3 modes, symbolic occupations)
    fs = sp.symbols("f0:3", positive=True)
    ks = sp.symbols("k0:3", integer=True, nonnegative=True)
    qv = sp.Symbol("q", positive=True)
    kk = sp.Symbol("kk", integer=True, nonnegative=True)
    geo_moments = []
    for e in range(3):
        s = sp.summation(kk ** e * qv ** kk, (kk, 0, sp.oo))
        if isinstance(s, sp.Piecewise):
            s = s.args[0][0]
        geo_moments.append(sp.simplify((1 - qv) * s))
    moments_b = [[sp.factor(sp.simplify(geo_moments[e].subs(qv, fs[n] / (1 + fs[n])))) for e in range(3)] for n in range(3)]
    mom_ok = all(sp.simplify(moments_b[n][1] - fs[n]) == 0 and sp.simplify(moments_b[n][2] - fs[n] - 2 * fs[n] ** 2) == 0
                 for n in range(3))
    rec.check("singleModeMoments", mom_ok,
              "geometric (thermal) number distribution (1 - q) q^k, q = f/(1 + f): <k> = f, <k^2> = f + 2 f^2 (exact series)")
    K3 = [[CQ(0, 1), CQ(2, -1), CQ(1)], [CQ(-2, -1), CQ(0, 2), CQ(0, 1)], [CQ(-1), CQ(0, 1), CQ(0, -1)]]
    U3 = cayley_unitary(K3)
    A3 = [row[:3] for row in A[:3]]
    B3 = [row[:3] for row in Bm[:3]]
    U3s, A3s, B3s = sym_matrix(U3), sym_matrix(A3), sym_matrix(B3)
    rho3 = U3s * sp.diag(*fs) * U3s.H
    At3 = sp.expand(U3s.H * A3s * U3s)
    Bt3 = sp.expand(U3s.H * B3s * U3s)
    tA, tB = sp.expand((A3s * rho3).trace()), sp.expand((B3s * rho3).trace())
    ex3 = sp.expand((A3s * rho3 * B3s * rho3).trace())
    abr3 = sp.expand((A3s * B3s * rho3).trace())
    tot_n = 0
    tot_f = 0
    for n, mm, p, q in itertools.product(range(3), repeat=4):
        coefficient = At3[n, mm] * Bt3[p, q]
        dn = boson_diagonal([(n, 1), (p, 1), (mm, 0), (q, 0)], ks)
        df = boson_diagonal([(n, 1), (mm, 0), (p, 1), (q, 0)], ks)
        if dn != 0:
            tot_n += coefficient * moment_substitute(dn, ks, moments_b)
        if df != 0:
            tot_f += coefficient * moment_substitute(df, ks, moments_b)
    boson_ok = (sp.simplify(sp.expand(tot_n - (tA * tB + ex3))) == 0 and sp.simplify(sp.expand(tot_f - (tA * tB + ex3 + abr3))) == 0
                and sp.simplify(ex3) != 0)
    rec.check("bosonThermalWickPlus", boson_ok,
              "bosonic thermal quasi-free states (symbolic occupations f0, f1, f2, a rational unitary basis change): "
              "<:(psi^+ A psi)(psi^+ B psi):> = Tr(A rho) Tr(B rho) + Tr(A rho B rho); full product + Tr(A B rho)")
    # classical circular Gaussian ensemble of commuting modes: exact moment integrals
    r, th = sp.symbols("r theta", positive=True)

    def gauss_moment(f, alpha, beta):
        radial = sp.integrate(2 / f * r ** (alpha + beta + 1) * sp.exp(-r ** 2 / f), (r, 0, sp.oo))
        angular = sp.integrate(sp.exp(sp.I * (beta - alpha) * th), (th, 0, 2 * sp.pi)) / (2 * sp.pi)
        return sp.simplify(radial * angular)

    def fixed_moment(f, alpha, beta):
        angular = sp.integrate(sp.exp(sp.I * (beta - alpha) * th), (th, 0, 2 * sp.pi)) / (2 * sp.pi)
        return sp.simplify(sp.sqrt(f) ** (alpha + beta) * angular)

    g_cache = {}

    def product_moment(word, kind):
        """<c-bar_n c_m c-bar_p c_q> for word (n, m, p, q) with independent modes."""
        n, mm, p, q = word
        total = sp.Integer(1)
        for mode in range(3):
            alpha = (n == mode) + (p == mode)
            beta = (mm == mode) + (q == mode)
            key = (kind, mode, alpha, beta)
            if key not in g_cache:
                g_cache[key] = (gauss_moment if kind == "gauss" else fixed_moment)(fs[mode], alpha, beta)
            total *= g_cache[key]
        return total

    single_ok = all(sp.simplify(gauss_moment(fs[0], a_, a_) - sp.factorial(a_) * fs[0] ** a_) == 0 for a_ in range(3)) and \
        gauss_moment(fs[0], 1, 2) == 0
    tot_g = 0
    tot_fx = 0
    for word in itertools.product(range(3), repeat=4):
        n, mm, p, q = word
        coefficient = At3[n, mm] * Bt3[p, q]
        tot_g += coefficient * product_moment(word, "gauss")
        tot_fx += coefficient * product_moment(word, "fixed")
    gauss_ok = sp.simplify(sp.expand(tot_g - (tA * tB + ex3))) == 0
    rec.check("classicalGaussianWickPlus", gauss_ok and single_ok,
              "circular Gaussian ensemble, density (1/(pi f)) e^{-|c|^2/f} per mode: <c-bar^a c^b> = delta_ab a! f^a (exact "
              "integrals); <(psi^* A psi)(psi^* B psi)> = Tr(A rho) Tr(B rho) + Tr(A rho B rho), no Tr(A B rho) term")
    dev = sum(fs[n] ** 2 * At3[n, n] * Bt3[n, n] for n in range(3))
    rec.check("fixedAmplitudePhasesDeviate", sp.simplify(sp.expand(tot_fx - (tA * tB + ex3 - dev))) == 0
              and sp.simplify(dev) != 0,
              "random phases with FIXED amplitudes |c_n|^2 = f_n: the Gaussian result minus sum_n f_n^2 (U^+AU)_nn (U^+BU)_nn")
    # the expectation rule: two-point function rho B, both statistics
    rng = random.Random(121)
    rho16 = mat_zero(16)
    for _ in range(3):
        v = [CQ(rng.randint(-2, 2), rng.randint(-2, 2)) for _ in range(16)]
        wgt = Fraction(rng.randint(1, 5), rng.randint(1, 5))
        for i in range(16):
            for l in range(16):
                rho16[i][l] = rho16[i][l] + v[i] * v[l].conj() * wgt
    K16 = mat_mul(rho16, pa.B)
    t1 = mat_trace(mat_mul(pa.C, K16))
    t2 = mat_trace(mat_mul_many(pa.C, K16, pa.C, K16))
    rec.check("expectationRuleTraces", t1 == mat_trace(mat_mul(pa.BC, rho16))
              and t2 == mat_trace(mat_mul_many(pa.BC, rho16, pa.BC, rho16)) and not t2.is_zero(),
              "with the two-point function G = rho B of the rule: Tr(C G) = Tr(BC rho), Tr(C G C G) = Tr(BC rho BC rho); "
              "hence E_HF = (lam/2)[Tr(BC rho)^2 + sg Tr(BC rho BC rho)], sg = -1 (anticommuting), +1 (commuting)")
    modes = moving_shell_modes(red)
    hmov = mat_add(mat_scale(pa.gamma[4], CQ(0, -7)), mat_scale(mat_mul(pa.gamma[4], pa.gamma[1]), -24))
    mv_ok = all(vec_is_eigen(hmov, u, CQ(e)) and vec_is_eigen(pa.B, u, CQ(bt)) for u, e, bt in modes) and \
        all(vec_dot(modes[a][0], modes[b][0]) == (CQ_ONE if a == b else CQ_ZERO) for a in range(4) for b in range(4))
    kf = KreinFock([x[0] for x in modes], [x[2] for x in modes])
    Kc = [[vec_dot(modes[n][0], mat_apply(pa.C, modes[k][0])) * modes[n][2] for k in range(4)] for n in range(4)]
    c, cd = kf.fock.b, kf.fock.bdag
    normal_S2 = mat_zero(kf.dim)
    for n, k, p, q in itertools.product(range(4), repeat=4):
        coefficient = Kc[n][k] * Kc[p][q]
        if not coefficient.is_zero():
            normal_S2 = mat_add(normal_S2, mat_scale(mat_mul_many(cd[n], cd[p], c[q], c[k]), coefficient))
    Sop = kf.bilinear(pa.C)
    hf_ok = mv_ok and any(not Kc[n][k].is_zero() for n in range(4) for k in range(4) if n != k)
    hf_cases = []
    for occ in ((0,), (1,), (0, 1), (0, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 2, 3)):
        st = kf.state(create=occ)
        rho = mat_zero(16)
        for n in occ:
            u = modes[n][0]
            for i in range(16):
                for l in range(16):
                    rho[i][l] = rho[i][l] + u[i] * u[l].conj()
        bcr = mat_mul(pa.BC, rho)
        hart = mat_trace(bcr) * mat_trace(bcr)
        exch = mat_trace(mat_mul(bcr, bcr))
        got = KreinFock.expect(normal_S2, st)
        hf_ok &= got == hart - exch and KreinFock.expect(Sop, st) == mat_trace(bcr)
        hf_cases.append({"occupied": list(occ), "<:S^2:>": got.to_pair(), "Tr(BC rho)^2": hart.to_pair(),
                         "Tr(BC rho BC rho)": exch.to_pair()})
    rec.check("expectationRuleKreinFock", hf_ok,
              {"statement": "anticommuting Krein-Fock field on 4 moving-shell modes (m = 7, p = 24, E = 25) with BOTH Krein "
                            "signs: <:S^2:> = Tr(BC rho)^2 - Tr(BC rho BC rho), <S> = Tr(BC rho)", "cases": hf_cases})
    # filled shell at an exact point of the good sector: m = 2, p = (0, 1, 2, 4), E = 5
    mf, pf, Ef = 2, (0, 1, 2, 4), 5
    h = mat_scale(pa.gamma[4], CQ(0, -mf))
    for jdir in range(4):
        if pf[jdir]:
            h = mat_sub(h, mat_scale(mat_mul(pa.gamma[4], pa.gamma[jdir]), pf[jdir]))
    Pp = mat_scale(mat_add(mat_scale(pa.I16, Ef), h), Fraction(1, 2 * Ef))
    Pm = mat_scale(mat_sub(mat_scale(pa.I16, Ef), h), Fraction(1, 2 * Ef))
    proj_ok = mat_eq(mat_mul(Pp, Pp), Pp) and mat_rank(Pp) == 8 and mat_eq(mat_mul(h, Pp), mat_scale(Pp, Ef)) \
        and is_hermitian(h)
    S1 = mat_trace(mat_mul(pa.BC, Pp))
    ex1 = mat_trace(mat_mul_many(pa.BC, Pp, pa.BC, Pp))
    ratio = ex1.re / (S1.re * S1.re)
    rec.check("filledShellExchangeRatio", proj_ok and S1 == CQ(Fraction(8 * mf, Ef)) and ratio == Fraction(1, 8),
              {"Tr(BC P+)": S1.to_pair(), "Tr(BC P+ BC P+)": ex1.to_pair(), "ratio": frac_str(ratio),
               "statement": "E_x = sg (lam/2) Tr(BC P BC P) = sg E_H / 8: -E_H/8 (dirac16complex), +E_H/8 (dirac16complex00)"})
    rec.measure("filledShellRatio", frac_str(ratio))
    cov = check_stat_gas(pa, rec, Pp, Pm)
    return rec, {"filledShellRatio": ratio, "restShellCovarianceEigenvalues": cov}


def good_sector_h(pa, m, p):
    h = mat_scale(pa.gamma[4], CQ(0, -m))
    for jdir in range(4):
        if p[jdir]:
            h = mat_sub(h, mat_scale(mat_mul(pa.gamma[4], pa.gamma[jdir]), p[jdir]))
    return h


def check_stat_gas(pa, rec, Pp, Pm):
    """Uniform gas: exact finite gas, the continuum kernel, LDA potentials, T = 0 derivative, covariance positivity."""
    m = 2
    shells = {2: [(0, 0, 0, 0)], 3: [(1, 2, 0, 0), (0, 0, 2, 1)], 4: [(2, 2, 2, 0)], 5: [(0, 1, 2, 4), (4, 2, 1, 0)]}
    fplus = {2: Fraction(1), 3: Fraction(3, 4), 4: Fraction(1, 3), 5: Fraction(1, 10)}
    fminus = {2: Fraction(1, 7), 3: Fraction(1, 11), 4: Fraction(0), 5: Fraction(1, 13)}
    rho = mat_zero(16)
    npts = 0
    gas_ok = True
    for E, plist in shells.items():
        for p in plist:
            for sgn in ((1,) if not any(p) else (1, -1)):
                pv = tuple(sgn * x for x in p)
                h = good_sector_h(pa, m, pv)
                gas_ok &= mat_eq(mat_mul(h, h), mat_scale(pa.I16, E * E))
                P1 = mat_scale(mat_add(mat_scale(pa.I16, E), h), Fraction(1, 2 * E))
                P2 = mat_scale(mat_sub(mat_scale(pa.I16, E), h), Fraction(1, 2 * E))
                rho = mat_add(rho, mat_sub(mat_scale(P1, fplus[E]), mat_scale(P2, fminus[E])))
                npts += 1
    n_gas = mat_trace(rho)
    S_gas = mat_trace(mat_mul(pa.BC, rho))
    x_gas = mat_trace(mat_mul_many(pa.BC, rho, pa.BC, rho))
    closed = (n_gas * n_gas + S_gas * S_gas) * Fraction(1, 16)
    n_expected = sum((8 * (fplus[E] - fminus[E]) * len(pl) * (1 if E == 2 else 2) for E, pl in shells.items()), Fraction(0))
    S_expected = sum((8 * Fraction(m, E) * (fplus[E] + fminus[E]) * len(pl) * (1 if E == 2 else 2) for E, pl in shells.items()),
                     Fraction(0))
    lam = sp.Symbol("lam")
    ex_by_sg = {s: sp.nsimplify(s * lam / 2 * sp.Rational(x_gas.re.numerator, x_gas.re.denominator)) for s in (-1, 1)}
    closed_by_sg = {s: s * lam / 32 * sp.Rational((n_gas * n_gas + S_gas * S_gas).re.numerator,
                                                  (n_gas * n_gas + S_gas * S_gas).re.denominator) for s in (-1, 1)}
    rec.check("uniformGasExactFinite", gas_ok and x_gas == closed and n_gas == CQ(n_expected) and S_gas == CQ(S_expected)
              and all(sp.simplify(ex_by_sg[s] - closed_by_sg[s]) == 0 for s in (-1, 1)),
              {"gas": "m = 2, %d momenta closed under p -> -p on the shells E = 2, 3, 4, 5 (exact), arbitrary isotropic "
                      "occupations f_+(E), f_-(E); rho = sum [f_+ P_+(p) - f_- P_-(p)] (holes of the sea)" % npts,
               "n": n_gas.to_pair(), "S": S_gas.to_pair(), "Tr(BC rho BC rho)": x_gas.to_pair(),
               "statement": "Tr(BC rho BC rho) = (n^2 + S^2)/16 exactly: e_x = sg (lam/32)(n^2 + S^2) for both statistics"})
    # continuum: the kernel Tr(P_a(p) BC P_b(q) BC) = 4 [1 + a b (m^2 - p.q)/(E_p E_q)]
    Gam = sym_matrix(pa.BC)
    Xs = [Gam] + [sym_matrix(mat_neg(mat_mul(pa.gamma[4], pa.gamma[jdir]))) for jdir in range(4)]
    msym, Ep, Eq = sp.symbols("m E_p E_q", positive=True)
    pvec = sp.symbols("p0:4", real=True)
    qvec = sp.symbols("q0:4", real=True)
    hps = msym * Xs[0] + sum((pvec[i] * Xs[i + 1] for i in range(4)), sp.zeros(16))
    hqs = msym * Xs[0] + sum((qvec[i] * Xs[i + 1] for i in range(4)), sp.zeros(16))
    I16s = sp.eye(16)
    kern_ok = sp.expand(hps * hps - (msym ** 2 + sum(x ** 2 for x in pvec)) * I16s) == sp.zeros(16)
    for a_ in (1, -1):
        for b_ in (1, -1):
            Pa = (I16s + a_ * hps / Ep) / 2
            Pb = (I16s + b_ * hqs / Eq) / 2
            val = sp.expand((Pa * Gam * Pb * Gam).trace())
            target = 4 * (1 + a_ * b_ * (msym ** 2 - sum(pvec[i] * qvec[i] for i in range(4))) / (Ep * Eq))
            kern_ok &= sp.simplify(val - target) == 0
    i0p, i0m, i1p, i1m, J = sp.symbols("I0p I0m I1p I1m J", real=True)
    # sum_ab s_a s_b f_a f_b K_ab with s_+ = +1, s_- = -1 (holes) and s_a a = +1: the three parts of the kernel give
    # 4 (int (f_+ - f_-))^2 + 4 (int (f_+ + f_-) m/E)^2 - 4 |int (f_+ + f_-) p/E|^2 = 4 (I0^2 + I1^2 - J^2)
    trace_gas = 4 * ((i0p - i0m) ** 2 + (i1p + i1m) ** 2) - 4 * J ** 2
    n_c = 8 * (i0p - i0m)
    S_c = 8 * (i1p + i1m)
    rec.check("uniformGasExchange", kern_ok and sp.simplify(trace_gas.subs(J, 0) - (n_c ** 2 + S_c ** 2) / 16) == 0,
              {"kernel": "Tr(P_a(p) BC P_b(q) BC) = 4[1 + a b (m^2 - p.q)/(E_p E_q)] (exact trace table)",
               "gas": "rho = int [f_+ P_+ - f_- P_-]: Tr(BC rho BC rho) = 4[(I0+ - I0-)^2 + (I1+ + I1-)^2] - 4 |J|^2 with "
                      "I0 = int f, I1 = int f m/E, J = int (f_+ + f_-) p/E... = 0 for any occupation even under p -> -p",
               "n": "8 (I0+ - I0-)", "S": "8 (I1+ + I1-)",
               "result": "e_x = sg (lam/2) Tr(BC rho BC rho) = sg (lam/32)(n^2 + S^2) for every T: -(lam/32)(n^2 + S^2) "
                         "(dirac16complex), +(lam/32)(n^2 + S^2) (dirac16complex00)"})
    nS, SS_, lamS, mS = sp.symbols("n S lam m", real=True)
    ok_lda = True
    lda = {}
    for s in (-1, 1):
        ex = s * lamS / 32 * (nS ** 2 + SS_ ** 2)
        eh = lamS / 2 * SS_ ** 2
        vv = sp.diff(ex, nS)
        vs = sp.diff(ex, SS_)
        meff = mS + sp.diff(eh + ex, SS_)
        ok_lda &= sp.simplify(vv - s * lamS * nS / 16) == 0 and sp.simplify(vs - s * lamS * SS_ / 16) == 0
        ok_lda &= sp.simplify(meff - (mS + (1 + sp.Rational(s, 16)) * lamS * SS_)) == 0
        lda[s] = {"v_v": str(vv), "v_s": str(vs), "M_eff": str(sp.factor(meff - mS) + mS)}
    rec.check("ldaPotentials", ok_lda, {"dirac16complex (sg=-1)": lda[-1], "dirac16complex00 (sg=+1)": lda[1],
                                        "note": "M_eff = m + (15/16) lam S_p resp. m + (17/16) lam S_p; v_x = v_v"})
    pF, pp = sp.symbols("p_F p", positive=True)
    t0_ok = True
    for d in (3, 4):
        cd = sp.Symbol("c_d", positive=True)
        n_t0 = 8 * cd * sp.integrate(pp ** (d - 1), (pp, 0, pF))
        S_t0 = 8 * cd * sp.Integral(msym / sp.sqrt(msym ** 2 + pp ** 2) * pp ** (d - 1), (pp, 0, pF))
        for s in (-1, 1):
            ex = s * lamS / 32 * (n_t0 ** 2 + S_t0 ** 2)
            dex_dn = sp.diff(ex, pF) / sp.diff(n_t0, pF)
            target = s * lamS / 16 * (n_t0 + S_t0 * msym / sp.sqrt(msym ** 2 + pF ** 2))
            t0_ok &= sp.simplify((dex_dn - target).doit()) == 0
    rest = sp.limit((sp.Integer(1) * lamS / 32 * (nS ** 2 + SS_ ** 2) / (lamS / 2 * SS_ ** 2)).subs(SS_, nS), nS, 1)
    rec.check("T0TotalDerivative", t0_ok and rest == sp.Rational(1, 8),
              {"statement": "at T = 0 along the gas: de_x/dn = sg (lam/16)[n + S m/E_F] (d = 3 and 4)",
               "restGasLimit": "S -> n (m/E -> 1): e_x/e_H -> sg/8"})
    # covariance of the rule on a filled rest shell: K = P_+ B (m = 1, p = 0)
    P0 = mat_scale(mat_add(pa.I16, pa.BC), Fraction(1, 2))
    Kc = mat_mul(P0, pa.B)
    lam_ = sp.Symbol("x")
    cp = sp.factor(sym_matrix(Kc).charpoly(lam_).as_expr())
    eig = sp.roots(sp.Poly(cp, lam_))
    eig_list = sorted(sum([[int(k)] * v for k, v in eig.items()], []))
    zero_charge = (mat_trace(mat_mul(pa.B, P0)).is_zero() and mat_trace(mat_mul(pa.C, P0)).is_zero()
                   and mat_trace(mat_mul(pa.B, Pp)).is_zero() and mat_trace(mat_mul(pa.C, Pp)).is_zero())
    rec.check("expectationRuleCovarianceIndefinite",
              eig_list == [-1] * 4 + [0] * 8 + [1] * 4 and is_hermitian(Kc) and zero_charge,
              {"eigenvalues of K = P_+ B (filled rest shell)": eig_list,
               "consequence": "K is indefinite: the dirac16complex00 KS model with the expectation rule is a formal "
                              "(Krein-signed) Gaussian functional, not a probability ensemble of classical fields; with the "
                              "positive covariance K = rho a filled shell has Tr(B P_+) = Tr(C P_+) = 0 (zero charge, zero "
                              "scalar density) at rest and at the moving point m = 2, p = (0,1,2,4)"})
    rec.measure("restShellCovarianceEigenvalues", eig_list)
    return eig_list


# CHUNK-12B-END

# ---------------------------------------------------------------------------
# 13. Family "totals": pair totals, field level and Kohn-Sham level
# ---------------------------------------------------------------------------

def check_totals(pa, quick=False):
    rec = Recorder("totals")
    # (a) chiral pair (T1) in the primordial field of the notebook (arbitrary a4(t), symbolic point)
    dom = G.make_g2_domain()
    gd = G.GammaData(dom)
    chi_arr = np.array([dom.conv(c) for c in pa.chi], dtype=object)
    geo = geometry_from(G.g2_vielbein_jet(1, dom), gd, dom, "G2", sqrtg_sign=1)
    rng = random.Random(131)
    m = dom.conv(sp.Rational(7, 5))
    lam = dom.conv(sp.Rational(-3, 8))
    psi = G.random_spinor_jet(rng, dom, 1)
    chi = G.random_spinor_jet(rng, dom, 1)
    qa = spinor_quantities(geo, psi, chi, m, lam)
    qb = spinor_quantities(geo, jet_scale_last(psi, chi_arr), jet_scale_last(chi, chi_arr), -m, -lam)
    S0 = qa["S"].value()
    rec.check("fieldLevelChiralPair",
              G.arr_is_zero(qa["T"].value() + qb["T"].value(), dom) and G.arr_is_zero(qa["j"].value() + qb["j"].value(), dom)
              and G.arr_is_zero(qa["Ls"].value() + qb["Ls"].value(), dom) and G.arr_is_zero(qb["S"].value() - S0, dom)
              and not G.arr_is_zero(S0, dom) and G.count_nonzero(qa["T"].value(), dom) == 64,
              {"field": "Stage-2 primordial field (notebook chart, arbitrary a4(t), generic point)",
               "pair": "{(m, lam, Psi), (-m, -lam, gamma^8 Psi)}", "totals": "T = 0 (64 components), j = 0, L = 0, S = 2 S",
               "meaning": "the chiral {+M, -M} pair carries no energy-momentum, no charge and no action, at every x4"})
    # (b) mirror pair (T2) in the G1 field: {(m, lam, e, Psi), (-m, lam, e R_u, u Psi)} with u = gamma^1 (space-like)
    domq = G.make_qq_domain()
    gdq = G.GammaData(domq)
    ej = G.vielbein_jet_from_sympy(G.g1_vielbein_sympy(), G.G1_POINTS["p2"], 1, domq)
    geo1 = geometry_from(ej, gdq, domq, "G1_p2")
    U = pa.gamma[1]
    Lam = vector_action(pa, U)
    Mt = np.empty((8, 8), dtype=object)
    for a in range(8):
        for c in range(8):
            Mt[c, a] = domq.conv(sp.Rational(-Lam[a][c].numerator, Lam[a][c].denominator))
    geo2 = geometry_from(ej.map(lambda arr: arr.dot(G.mat_inv(Mt, domq))), gdq, domq, "G1_p2_reflected")
    Ud = dom_matrix(domq, U)
    rng = random.Random(132)
    m1 = domq.conv(sp.Rational(-5, 6))
    l1 = domq.conv(sp.Rational(4, 3))
    p1 = G.random_spinor_jet(rng, domq, 1)
    c1 = G.random_spinor_jet(rng, domq, 1)
    qa = spinor_quantities(geo1, p1, c1, m1, l1)
    qb = spinor_quantities(geo2, jet_map_spinor(p1, Ud), jet_map_spinor(c1, Ud), -m1, l1)
    rec.check("fieldLevelMirrorPair",
              G.arr_is_zero(qb["T"].value() - qa["T"].value(), domq) and G.arr_is_zero(qb["j"].value() - qa["j"].value(), domq)
              and G.arr_is_zero(qb["Ls"].value() - qa["Ls"].value(), domq) and G.arr_is_zero(qb["S"].value() + qa["S"].value(), domq)
              and not G.arr_is_zero(qa["T"].value(), domq),
              {"pair": "{(m, lam, e, Psi), (-m, lam, e R_u, u Psi)}, u = gamma^1 (space-like, chi = -1), G1 field at p2",
               "totals": "T = 2T, j = 2j, L = 2L, S = 0: the mirror pair doubles the energy-momentum"})
    # (c) Kohn-Sham level on exact k = 0 orbitals (constant M_eff = M, bare mass m, v_v = 0)
    Y_ = KS.Y
    Mp = sp.Symbol("M", positive=True)
    mb = sp.Symbol("m_bare", real=True)
    Lp = sp.Symbol("L", positive=True)
    qn = sp.Symbol("n", positive=True, integer=True) * sp.pi / Lp
    ep = sp.sqrt(Mp ** 2 + qn ** 2)
    orb = sp.Matrix([(Mp * sp.sin(qn * Y_) + qn * sp.cos(qn * Y_)) / (sp.I * ep), sp.sin(qn * Y_)])     # block j = +1
    img = SIG2 * orb                                                                                      # block j = -1, -M

    def dens(v, j):
        vh = v.H
        return {"n": sp.simplify((vh * v)[0]), "s": sp.simplify(j * (vh * SIG2 * v)[0]),
                "t": sp.simplify(j * (vh * SIG3 * v)[0]), "c": sp.simplify(j * (vh * SIG1 * v)[0])}

    d_plus = dens(orb, 1)
    d_img = dens(img, -1)

    def emt(d, M, mbare, eps):
        return {"rho": eps * d["n"] - (M - mbare) * d["s"], "p_y": eps * d["n"] - mbare * d["s"],
                "p_i": (M - mbare) * d["s"]}

    T_plus = emt(d_plus, Mp, mb, ep)
    T_std = emt(d_img, -Mp, -mb, ep)                                    # standard rule, the ordinary -M universe
    T_imgrule = {k: -v for k, v in emt(d_img, -Mp, -mb, ep).items()}   # Krein image: every one-body value flips
    zero = lambda e: sp.simplify(e) == 0  # noqa: E731
    solves = sp.simplify(sp.diff(img, Y_) - KS.block_ode_matrix(M=-Mp, k=0, eps=ep, vv=0, j=-1) * img) == sp.zeros(2, 1)
    bcs = zero(img[0].subs(Y_, 0)) and zero(img[0].subs(Y_, -Lp))
    mirror_ok = (solves and bcs and zero(d_plus["c"]) and zero(d_img["n"] - d_plus["n"]) and zero(d_img["s"] + d_plus["s"])
                 and all(zero(T_std[k] - T_plus[k]) for k in T_plus) and not zero(d_plus["s"]))
    rec.check("ksMirrorPair", mirror_ok,
              {"orbital": "+M: chi = ((M sin qy + q cos qy)/(i eps), sin qy), q = n pi/L, block j = +1 (even parity, "
                          "theta = 0); -M: sigma2 chi in block j = -1 (odd parity, theta = pi), the same eps",
               "totals": "n_pair = 2n, S_pair = 0, rho, p_y, p_(i) doubled (standard rule); E_pair = 2E (same spectrum)"})
    # image rule: every one-body value is minus the standard-rule value of the mapped orbital
    n_image, s_image = -d_img["n"], -d_img["s"]
    n_pair = sp.simplify(d_plus["n"] + n_image)
    s_pair = sp.simplify(d_plus["s"] + s_image)
    rec.check("ksKreinImagePair",
              all(zero(T_imgrule[k] + T_plus[k]) for k in T_plus) and zero(n_pair)
              and zero(s_pair - 2 * d_plus["s"]) and not zero(d_plus["s"]),
              {"totals": "Krein image (metric -B, -lam): n_pair = 0 (charge 0), rho_pair = p_pair = 0 pointwise, "
                         "S_pair = 2 S_+", "note": "the image values are the negatives of the standard-rule values of the "
                                                   "mapped orbital: the totals are the identity X + (-X) = 0 for one "
                                                   "state in two sets of variables (T1krein), not a cancellation "
                                                   "between two universes"})
    return rec


# CHUNK-13-END

# ---------------------------------------------------------------------------
# 14. S5_pairingAgreesWithWolfram: compare the Wolfram exports with the results derived here
# ---------------------------------------------------------------------------

def parse_wolfram_list(text):
    """'{1, -1, 1}' -> [1, -1, 1] (integers or rationals)."""
    inner = text.strip().strip("{}")
    return [Fraction(x.strip()) for x in inner.split(",") if x.strip()]


def parse_wolfram_floats(text):
    import re
    return [float(x) for x in re.findall(r"(-?\d+\.\d+)`", text)]


def parse_wolfram_targets(text):
    """'<|"gamma^2" -> {{6}, {7}, ...}, ...|>' -> {"gamma^2": [[6], [7], ...], ...}."""
    import re
    out = {}
    for name, body in re.findall(r'"(gamma\^\d)"\s*->\s*\{((?:\{[^{}]*\},?\s*)+)\}', text):
        out[name] = [[int(v) for v in grp.split(",") if v.strip()] for grp in re.findall(r"\{([^{}]*)\}", body)]
    return out


def wolfram_expr(text, symbols):
    return sp.sympify(text.replace("^", "**"), locals=symbols)


def sign_word(s, letter):
    return ("%s" % letter) if s == 1 else ("-%s" % letter)


def check_wolfram_agreement(own, theory_path, report_path):
    rec = Recorder("wolfram")
    missing = [p for p in (theory_path, report_path) if not (p and os.path.exists(p))]
    if missing:
        rec.check("filesPresent", False, {"missing": [relative(p) for p in missing]})
        return rec
    with open(theory_path, "r", encoding="utf-8") as handle:
        th = json.load(handle)
    with open(report_path, "r", encoding="utf-8") as handle:
        wr = json.load(handle)
    checks = wr.get("checks", {})
    rec.check("reportAllTrue", bool(checks) and all(v is True for v in checks.values()),
              {"wolframCheckCount": len(checks), "wolframFailed": sorted(k for k, v in checks.items() if v is not True)})
    current = {}
    for rel in list(WOLFRAM_SOURCES) + ["wolfram/Dirac16ComplexGeometry.wl",
                                        "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
                                        "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json"]:
        path = os.path.join(REPOSITORY_ROOT, rel)
        current[rel] = sha256_file(path) if os.path.exists(path) else None
    rs = wr.get("sourceSha256", {})
    ts = th.get("sourceSha256", {})
    rec.check("sourcesCurrent", all(rs.get(k) == v and ts.get(k) == v for k, v in current.items()),
              {"comparedFiles": sorted(current), "note": "the Wolfram report and pairing-theory.json were produced from the "
                                                         "current Wolfram sources and inputs"})
    referenced = set()

    def collect(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "checks" and isinstance(value, dict):
                    referenced.update(value.keys())
                else:
                    collect(value)
        elif isinstance(node, list):
            for value in node:
                collect(value)

    collect(th)
    rec.check("theoryChecksTrue", bool(referenced) and all(checks.get(k) is True for k in referenced),
              {"referencedChecks": len(referenced)})
    wm = wr.get("measurements", {})
    rec.check("algebraMeasurements", wm.get("algebra_oddBilinearMatrixCount") == own["oddCount"]
              and wm.get("algebra_uBudagger_sign_for_u_gamma0to7") == own["uB"],
              {"wolfram": [wm.get("algebra_oddBilinearMatrixCount"), wm.get("algebra_uBudagger_sign_for_u_gamma0to7")],
               "python": [own["oddCount"], own["uB"]]})
    rec.check("monomialCounts", wm.get("T1generic_kineticMonomials") == own["kinetic"]
              and wm.get("T1generic_connectionMonomials") == own["connection"]
              and wm.get("T1grassmann_monomials_Ls") == own["grassmannLs"] and wm.get("T1grassmann_monomials_S2") == own["grassmannS2"],
              {"wolfram": [wm.get("T1generic_kineticMonomials"), wm.get("T1generic_connectionMonomials"),
                           wm.get("T1grassmann_monomials_Ls"), wm.get("T1grassmann_monomials_S2")],
               "python": [own["kinetic"], own["connection"], own["grassmannLs"], own["grassmannS2"]],
               "note": "generic-coefficient supports; an independent count of the same polynomials"})
    kd = wm.get("T1krein_scalarDensity_particle1_particle2_hole3_hole4", "")
    rec.check("kreinScalarDensities", [int(x) for x in parse_wolfram_list(kd)] == own["kreinScalar"],
              {"wolfram": kd, "python": own["kreinScalar"]})
    bm = th["T3"]["blockMaps"]
    ph8 = [tuple(p) for p in bm["gamma8"]["phasesByTargetBlock"]]
    ph1 = [tuple(p) for p in bm["gamma1"]["phases"]]
    mine8 = [tuple(c.to_pair()) for c in own["phases8"]]
    mine1 = [tuple(c.to_pair()) for c in own["phases1"]]
    targets = parse_wolfram_targets(bm["otherGammas"])
    rec.check("blockMaps", ph8 == mine8 and ph1 == mine1 and targets == own["targets"] and own["basisIdentical"],
              {"gamma8Phases": [ph8 == mine8, mine8], "gamma1Phases": ph1 == mine1, "otherGammas": targets == own["targets"],
               "basisIdenticalToStage4Export": own["basisIdentical"]})
    ds = {k: [int(x) for x in parse_wolfram_list(wm.get("T3block_densitySigns_%s" % k, "{}"))] for k in ("sigma2", "sigma1", "sigma3")}
    names = ("n", "s", "t", "c")
    texts_ok = True
    for k, signs in own["densitySigns"].items():
        mapped = "(n, s, t, c) -> (%s)" % ", ".join(sign_word(s, nm) for s, nm in zip(signs, names))
        texts_ok &= bm["densitiesAndCurrents"][k].startswith(mapped)
    rec.check("densitySigns", ds == own["densitySigns"] and texts_ok, {"wolfram": ds, "python": own["densitySigns"]})
    Mp, Lp = sp.Symbol("M", positive=True), sp.Symbol("L", positive=True)
    syms = {"E": sp.E, "LL": Lp, "Mz": Mp, "a4c": KS.A4C, "H": KS.H}
    ctl = th["T3"]["untransformedBCControl"]
    cw = wolfram_expr(ctl["closedForms"]["cPaired"], syms)
    cc = wolfram_expr(ctl["closedForms"]["cControl"], syms)
    floats = parse_wolfram_floats(ctl["valuesM1H1L3a0_floatLabelled"])
    fl_ok = len(floats) == 2 and abs(floats[0] - own["cValues"]["cPlus"]) < 1e-12 * abs(floats[0]) \
        and abs(floats[1] - own["cValues"]["cControl"]) < 1e-12 * abs(floats[1])
    rec.check("zeroModeSplitting", sp.simplify(cw - own["cPlus"]) == 0 and sp.simplify(cc - own["cControl"]) == 0 and fl_ok,
              {"wolframFloats": floats, "pythonFloats": own["cValues"]})
    rec.check("statisticsNumbers", wm.get("stat_filledShellRatio") == frac_str(own["filledShellRatio"])
              and [int(x) for x in parse_wolfram_list(wm.get("stat_restShellCovarianceEigenvalues", "{}"))] == own["covariance"],
              {"filledShellRatio": [wm.get("stat_filledShellRatio"), frac_str(own["filledShellRatio"])],
               "covarianceEigenvalues": own["covariance"]})
    table_ok = True
    rows = []
    for row in th["T2"]["table"]:
        v = [Fraction(x) for x in row["vector"]]
        pa = own["pa"]
        u = pa.unit_vector(v)
        n = eta_norm(v)
        ch = pin_character(pa, u)
        kb = krein_sign(pa, u)
        sK_t, sS_t = -ch, ch
        sK_u, sS_u = ch, ch
        twisted = lagrangian_map_string("e R_u", "u Psi", sK_t, sS_t) + "; T -> %sT; S -> %sS; j -> %sj" % (
            "+" if sK_t == 1 else "-", "+" if sS_t == 1 else "-", "+" if sK_t == 1 else "-")
        untw = lagrangian_map_string("-e R_u", "u Psi", sK_u, sS_u)
        g8u = lagrangian_map_string("-e R_u", "gamma^8 u Psi", -ch, ch)
        ok = (Fraction(row["norm"]) == n and int(row["character"]) == ch and int(row["uBudaggerSign"]) == kb
              and row["twistedFrameResult"] == twisted and row["untwistedFrameResult"].startswith(untw)
              and row["gamma8TimesUntwisted"] == g8u)
        mine = own["t2table"].get(row["u"])
        if mine is not None:
            ok &= (mine["twisted_u"]["sK"], mine["twisted_u"]["sS"]) == (sK_t, sS_t) and \
                (mine["untwisted_u"]["sK"], mine["untwisted_u"]["sS"]) == (sK_u, sS_u)
        table_ok &= ok
        rows.append({"u": row["u"], "agrees": ok})
    rec.check("T2table", table_ok, {"rows": rows, "note": "norm, character and Krein sign recomputed from the Wolfram vectors; "
                                                          "result strings generated from the signs derived here (the sign "
                                                          "pattern of the basis vectors is the one computed with G1 jets)"})
    frag = [
        (th["T1"]["statement"], "L_{m,lambda}[gamma^8 Psi] = -L_{-m,-lambda}[Psi]"),
        (th["T1"]["statement"], "T_{mu nu}[gamma^8 Psi; -m, -lambda] = -T_{mu nu}[Psi; m, lambda]"),
        (th["T1"]["statement"], "j^mu[Psi_-] = -j^mu[Psi]"),
        (th["T1"]["kreinMetric"], "gamma^8 B gamma^8 = -B"),
        (bm["odeMaps"]["sigma2"], "sigma2 N_j(M, k) sigma2 = N_{-j}(-M, k)"),
        (bm["odeMaps"]["sigma1"], "sigma1 N_j(M, k) sigma1 = N_j(-M, -k)"),
        (bm["boundaryConditions"]["bag"], "sigma2 Q(theta) sigma2 = Q(pi - theta)"),
        (bm["boundaryConditions"]["bag"], "sigma1 Q(theta) sigma1 = Q(theta + pi)"),
        (bm["boundaryConditions"]["bag"], "sigma3 Q(theta) sigma3 = Q(-theta)"),
        (bm["potentials"]["definitions"], "m + (15/16) lambda S_p resp. m + (17/16) lambda S_p"),
        (bm["orbitalEMT"], "rho = eps n - (M_eff - m) s - v_v n, p_y = eps n - m s - kappa k t, p_1 = kappa k t + "
                           "(M_eff - m) s + v_v n, p_2 = p_3 = p_t = (M_eff - m) s + v_v n"),
        (th["statistics"]["hartreeFock"]["formula"], "sg = -1 (dirac16complex), sg = +1 (dirac16complex00)"),
        (th["statistics"]["hartreeFock"]["uniformGas"], "-(lambda/32)(n^2 + S^2) (dirac16complex), +(lambda/32)(n^2 + S^2) "
                                                        "(dirac16complex00)"),
        (th["statistics"]["wick"]["anticommuting"], "Tr(A rho) Tr(B rho) - Tr(A rho B rho)"),
        (th["statistics"]["wick"]["commutingClassical"], "Tr(A rho) Tr(B rho) + Tr(A rho B rho)"),
        (th["T3"]["theoremStandardRule"], "P(-m, pi - theta) with the SAME lambda"),
        (th["T3"]["whatMustTransform"]["lambda"], "unchanged for the ordinary -M universe"),
        (th["T3"]["numericsPrescription"]["minusMTransformed"], "lambda unchanged"),
        (th["T3"]["numericsPrescription"]["minusMTransformed"], "tip bag theta = pi"),
        (ctl["exact"], "q cos(qL) + M sin(qL) = 0 for +M and by q cos(qL) - M sin(qL) = 0 for the control"),
        (ctl["exact"], "tanh(kappa L) = kappa/M whenever M L > 1"),
        (th["pairTotals"]["fieldLevel"]["chiralPairT1"], "T = 0, j = 0, L = 0, S = 2S"),
        (th["pairTotals"]["fieldLevel"]["mirrorPairT2"], "T = 2T, j = 2j, L = 2L, S = 0"),
        (th["pairTotals"]["ksLevel"]["mirrorPair"], "E_pair = 2 E_+"),
        (th["pairTotals"]["ksLevel"]["kreinImagePair"], "E_pair = 0, charge 0, T_pair = 0 pointwise, S_pair = 2 S_+"),
        (th["T2"]["statement"], "(the SAME lambda)"),
    ]
    missing_frag = [f for text, f in frag if f not in text]
    rec.check("statementsAgree", not missing_frag and own["ownStatementsVerified"],
              {"fragments": len(frag), "missing": missing_frag,
               "note": "each fragment states a result that the corresponding family of this checker computed (all of "
                       "them passed); the fragment must occur in the Wolfram statement"})
    np_ = th.get("notProved", [])
    rec.check("honestyStatements", any("no dynamical creation rate" in s for s in np_)
              and "Interpretation, not derived" in th.get("notebookHypothesis", ""),
              "pairing-theory.json keeps the non-claims: no creation rate/amplitude is derived; pair creation itself is "
              "interpretation")
    return rec


# CHUNK-14-END

# ---------------------------------------------------------------------------
# 15. Driver, report, command line
# ---------------------------------------------------------------------------

def basis_identical_to_stage4(red, path=STAGE4_THEORY):
    """The Stage-4 basis rebuilt here equals the one exported in kohn-sham-theory.json (read only)."""
    if not os.path.exists(path):
        return False
    with open(path, "r", encoding="utf-8") as handle:
        blocks = json.load(handle)["reduction"]["blockDiagonalisation"]["blocks"]
    for mine, theirs in zip(red.blocks, blocks):
        if [v.to_pair() for v in mine["vPlus"]] != theirs["vPlus"] or [v.to_pair() for v in mine["vMinus"]] != theirs["vMinus"]:
            return False
    return len(blocks) == 8


def run_checks(fixture_path=DEFAULT_FIXTURE, theory_path=DEFAULT_THEORY, report_path=DEFAULT_WOLFRAM_REPORT,
               families=None, quick=False, wolfram=True):
    families = list(FAMILIES) if families is None else list(families)
    checks = {}
    measurements = {"quick": quick, "families": families}
    timings = {}
    exceptions = {}
    inputs = {}
    pa = PairAlgebra(fixture_path)
    red = KS.BlockReduction(pa.alg)
    for path in (fixture_path, STAGE4_THEORY):
        if path and os.path.exists(path):
            inputs[relative(path)] = sha256_file(path)
    results = {}

    def family(name, function):
        start = time.time()
        try:
            out = function()
        except Exception as error:      # noqa: BLE001 - a failing family is a failed check, never a crash
            exceptions[name] = "%s: %s" % (type(error).__name__, error)
            checks["S5_%s" % name] = False
            timings[name] = round(time.time() - start, 3)
            return None
        timings[name] = round(time.time() - start, 3)
        rec = out[0] if isinstance(out, tuple) else out
        checks.update(rec.checks)
        checks["S5_%s" % name] = rec.ok()
        measurements["S5_%s" % name] = rec.measurements
        results[name] = out
        return out

    runners = {
        "algebra": lambda: check_algebra(pa),
        "T1generic": lambda: check_t1generic(pa, quick=quick),
        "T1grassmann": lambda: check_t1grassmann(pa, quick=quick),
        "T1jets": lambda: check_t1jets(pa, quick=quick),
        "T1primordial": lambda: check_t1primordial(pa, quick=quick),
        "T1krein": lambda: check_t1krein(pa, red),
        "T2frame": lambda: check_t2frame(pa, quick=quick),
        "T2z2": lambda: check_t2z2(pa, quick=quick),
        "T3block": lambda: check_t3block(pa, red),
        "T3ks": lambda: check_t3ks(pa, quick=quick),
        "T3emt": lambda: check_t3emt(pa, red, quick=quick),
        "stat": lambda: check_stat(pa, red, quick=quick),
        "totals": lambda: check_totals(pa, quick=quick),
    }
    for name in FAMILIES:
        if name in families:
            family(name, runners[name])
    needed = ("algebra", "T1generic", "T1grassmann", "T1krein", "T2frame", "T3block", "T3ks", "T3emt", "stat", "totals")
    if wolfram and all(n in results for n in needed):
        start = time.time()
        try:
            t2rows = {row["u"]: row for row in results["T2frame"][1]}
            m_alg = results["algebra"].measurements
            m_gen = results["T1generic"].measurements
            m_gr = results["T1grassmann"].measurements
            own = {
                "pa": pa, "oddCount": m_alg["oddBilinearMatrixCount"], "uB": m_alg["uBudaggerSigns"],
                "kinetic": m_gen["kineticMonomials"], "connection": m_gen["connectionMonomials"],
                "grassmannLs": m_gr["monomials_Ls"], "grassmannS2": m_gr["monomials_S2"],
                "kreinScalar": results["T1krein"].measurements["scalarDensity_particle0_particle1_hole2_hole3"],
                "phases8": results["T3block"][1]["phases8"], "phases1": results["T3block"][1]["phases1"],
                "targets": results["T3block"][1]["targets"], "densitySigns": results["T3block"][1]["densitySigns"],
                "basisIdentical": basis_identical_to_stage4(red),
                "cPlus": results["T3ks"][1]["cPlus"], "cControl": results["T3ks"][1]["cControl"],
                "cValues": results["T3ks"][1]["cValues"],
                "filledShellRatio": results["stat"][1]["filledShellRatio"],
                "covariance": results["stat"][1]["restShellCovarianceEigenvalues"],
                "t2table": t2rows,
                "ownStatementsVerified": all(checks.get("S5_%s" % n) for n in needed),
            }
            rec = check_wolfram_agreement(own, theory_path, report_path)
            checks.update(rec.checks)
            checks[WOLFRAM_CHECK] = rec.ok()
            measurements[WOLFRAM_CHECK] = rec.measurements
            for path in (theory_path, report_path):
                if path and os.path.exists(path):
                    inputs[relative(path)] = sha256_file(path)
        except Exception as error:      # noqa: BLE001
            exceptions["wolfram"] = "%s: %s" % (type(error).__name__, error)
            checks[WOLFRAM_CHECK] = False
        timings["wolfram"] = round(time.time() - start, 3)
    else:
        measurements["wolframAgreement"] = "not-run (requires the families %s and wolfram=True)" % ", ".join(needed)
    checks["S5_internal_noException"] = not exceptions
    if exceptions:
        measurements["exceptions"] = exceptions
    return checks, measurements, inputs, timings


def build_report(checks, measurements, inputs):
    sources = {rel: sha256_file(os.path.join(REPOSITORY_ROOT, rel)) for rel in SOURCE_FILES}
    return {"schemaVersion": 1, "producer": PRODUCER, "checks": checks, "measurements": jsonable(measurements),
            "sourceSha256": sources, "inputSha256": inputs}


def canonical_json_bytes(document):
    text = json.dumps(document, indent=2, ensure_ascii=True) + "\n"
    return text.replace("\r\n", "\n").encode("utf-8")


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, str)):
        return str(value)
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def report_lines(report):
    lines = ["check_%s=%s" % (k, "true" if v else "false") for k, v in report["checks"].items()]
    for key, value in report["measurements"].items():
        lines.append("measurement_%s=%s" % (key, format_value(value)))
    failed = sum(1 for v in report["checks"].values() if not v)
    lines.append("check_count=%d" % len(report["checks"]))
    lines.append("failed_check_count=%d" % failed)
    return lines, failed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--theory", default=DEFAULT_THEORY, help="Wolfram pairing-theory.json (compared, never trusted)")
    parser.add_argument("--wolfram-report", default=DEFAULT_WOLFRAM_REPORT)
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--families", default=",".join(FAMILIES), help="comma-separated subset of %s" % ",".join(FAMILIES))
    parser.add_argument("--quick", action="store_true", help="reduced component/vector/point sets (tests)")
    parser.add_argument("--no-wolfram", action="store_true", help="skip the agreement check")
    parser.add_argument("--no-write", action="store_true")
    arguments = parser.parse_args(argv)
    families = [f.strip() for f in arguments.families.split(",") if f.strip()]
    unknown = [f for f in families if f not in FAMILIES]
    if unknown:
        print("error=unknown families %s" % ",".join(unknown))
        return 2
    checks, measurements, inputs, timings = run_checks(
        fixture_path=arguments.fixture, theory_path=arguments.theory, report_path=arguments.wolfram_report,
        families=families, quick=arguments.quick, wolfram=not arguments.no_wolfram)
    report = build_report(checks, measurements, inputs)
    lines, failed = report_lines(report)
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
