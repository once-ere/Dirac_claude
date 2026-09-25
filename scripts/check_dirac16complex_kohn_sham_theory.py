#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent exact checker of the Stage-4 Kohn-Sham theory of dirac16complex in
the static primordial field (sympy + mpmath + standard library; numpy, when
importable, is used only for the double-precision double sums of the exchange
table and for one numerical cross-check of the commutant dimensions; every
claim is decided exactly without it).

Nothing produced by Wolfram is used as truth.  The gamma matrices are rebuilt
from CONTRACT section 1 (exact integers) and merely compared with the committed
fixture; the geometry is recomputed from the metric; the block reduction is
re-derived with exact Gaussian-rational projectors; the Hartree-Fock formula is
re-derived on an explicit Fock space; every symbolic identity is decided by
sympy.  When artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json exists
(written by scripts/verify_dirac16complex_kohn_sham.wls) the check
KS_agreesWithWolfram compares its basis, blocks, matrices and numbers with the
ones derived here, up to the documented conventions; otherwise that check is
recorded as not-run.

Conventions (CONTRACT.md, NUMERICS_CONTRACT.md, STAGE4_SPEC.md incl. section 8)
  * eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), gamma^a = [[0, taubar_a],[tau_a, 0]],
    C = gamma^0 gamma^1 gamma^2 gamma^3, B = -i C gamma^4 (so B C = -i gamma^4),
    chirality gamma^8 = gamma^0 ... gamma^7.
  * Expectation rule: <Psi^dagger M Psi> = u^dagger B M u for a Hilbert-normalised
    one-particle mode; number density u^dagger u, scalar density u^dagger BC u.
  * Static primordial field in the proper hidden coordinate y = ln(sin z)/(6H):
        ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4}(dx1^2+dx2^2+dx3^2) - e^{-2a4}(dx5^2+dx6^2+dx7^2)],
    a4 constant, warp W = e^{Hy}, sqrt|g| = W^6, Z2 mirror W = e^{-H|y|}.
  * Ansatz Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y) gives
        gamma^0 chi' + i kappa(y) k gamma^1 chi - i eps gamma^4 chi = M_eff chi,
    kappa = e^{-Hy-a4}; A0 = gamma^0, A1 = gamma^0 gamma^1, A4 = gamma^0 gamma^4.
  * Block reduction: J = gamma^0 gamma^1 gamma^4 (J^2 = 1), K1 = gamma^2 gamma^3,
    K2 = gamma^5 gamma^6; projector P(j,s2,s3) = (1+jJ)/2 (1-i s2 K1)/2 (1-i s3 K2)/2;
    basis v+ = 8 P (1+gamma^0)/2 e_c (first c with nonzero image), v- = gamma^0 gamma^1 v+,
    |v|^2 = 8; block index 4(1-j)/2 + 2(1-s2)/2 + (1-s3)/2.  In every block
    A0 = sigma3, A1 = -i sigma2, A4 = j sigma1, B = j s2, C = s2 sigma2, BC = j sigma2.
    (The design probes and the Rust crate use s = -j: A0 A1 A4 = -J.)
  * Block ODE chi' = [M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi,
    h_j = j[-i sigma1 d/dy + M_eff sigma2 + kappa k sigma3] + v_v.
  * Exchange (own derivation): E_HF = (lambda/2)[Tr(BC rho)^2 - Tr(BC rho BC rho)];
    uniform gas e_x = -(lambda/32)(n^2 + S^2) exactly (angular average kills p.q);
    v_v = -(lambda/16) n, v_s = -(lambda/16) S.

Uniform gas used for e_x(n, T): the 8-fold degenerate free gas in the d = 4
spatial directions (y, x1, x2, x3) that the good sector moves in, densities per
proper 7-volume (units m^4 for n).  The d = 3 gas (momentum in 3-space only,
units m^3) is tabulated as well because both numerical solvers use it in their
n-only LDA variant; the closed form does not depend on d.

Prints ``check_<name>=true|false``, ``measurement_<name>=...``, ``check_count``,
``failed_check_count``; exits nonzero on failure; writes
artifacts/dirac16complex/kohn-sham/python-theory-report.json and
artifacts/dirac16complex/kohn-sham/exchange-table.json.

Usage: python scripts/check_dirac16complex_kohn_sham_theory.py [--output PATH]
       [--table PATH] [--theory PATH] [--fixture PATH] [--no-table] [--quick]
       [--no-write] [--families geometry,reduction,...]
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import re
import sys
import time
from fractions import Fraction

import mpmath
import sympy as sp

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIRECTORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex", "kohn-sham")
DEFAULT_OUTPUT = os.path.join(ARTIFACT_DIRECTORY, "python-theory-report.json")
DEFAULT_TABLE = os.path.join(ARTIFACT_DIRECTORY, "exchange-table.json")
DEFAULT_THEORY = os.path.join(ARTIFACT_DIRECTORY, "kohn-sham-theory.json")
DEFAULT_FIXTURE = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                               "arbitrary-field", "algebra-fixture.json")
PRODUCER = "scripts/check_dirac16complex_kohn_sham_theory.py"
SOURCE_FILES = ("scripts/check_dirac16complex_kohn_sham_theory.py",)

FAMILIES = ("geometry", "reduction", "boundary", "exchange", "functional", "emt")
FAMILY_CHECKS = {f: "KS_%s" % f for f in FAMILIES}
WOLFRAM_CHECK = "KS_agreesWithWolfram"

ETA = (1, 1, 1, 1, -1, -1, -1, -1)
SPACE_COORDINATES = ("y", "x1", "x2", "x3", "x4", "x5", "x6", "x7")


# ---------------------------------------------------------------------------
# 1. Exact Gaussian-rational linear algebra (16x16 and 2x2 matrices)
# ---------------------------------------------------------------------------

class CQ:
    """Gaussian rational re + i im with Fraction parts."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, Fraction) else Fraction(re)
        self.im = im if isinstance(im, Fraction) else Fraction(im)

    def __add__(self, other):
        other = cq(other)
        return CQ(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __sub__(self, other):
        other = cq(other)
        return CQ(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        return cq(other) - self

    def __mul__(self, other):
        other = cq(other)
        return CQ(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __neg__(self):
        return CQ(-self.re, -self.im)

    def __truediv__(self, other):
        return self * cq(other).inverse()

    def inverse(self):
        d = self.re * self.re + self.im * self.im
        if d == 0:
            raise ZeroDivisionError("CQ inverse of zero")
        return CQ(self.re / d, -self.im / d)

    def conj(self):
        return CQ(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, other):
        other = cq(other)
        return self.re == other.re and self.im == other.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return "CQ(%s, %s)" % (self.re, self.im)

    def to_sympy(self):
        return sp.Rational(self.re.numerator, self.re.denominator) + sp.I * sp.Rational(
            self.im.numerator, self.im.denominator)

    def to_pair(self):
        return [_frac_str(self.re), _frac_str(self.im)]


def _frac_str(f):
    return str(f.numerator) if f.denominator == 1 else "%d/%d" % (f.numerator, f.denominator)


def cq(value):
    if isinstance(value, CQ):
        return value
    if isinstance(value, complex):
        raise TypeError("floating complex not allowed in exact arithmetic")
    return CQ(Fraction(value), 0)


CQ_ZERO = CQ(0, 0)
CQ_ONE = CQ(1, 0)
CQ_I = CQ(0, 1)


def mat_from_ints(rows):
    return [[CQ(v, 0) for v in row] for row in rows]


def mat_zero(n, m=None):
    m = n if m is None else m
    return [[CQ_ZERO for _ in range(m)] for _ in range(n)]


def mat_eye(n):
    return [[CQ_ONE if i == j else CQ_ZERO for j in range(n)] for i in range(n)]


def mat_mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = []
    for i in range(n):
        row_a = a[i]
        nz = [(j, row_a[j]) for j in range(k) if not row_a[j].is_zero()]
        row = [CQ_ZERO] * m
        for j, aij in nz:
            row_b = b[j]
            for l in range(m):
                blj = row_b[l]
                if not blj.is_zero():
                    row[l] = row[l] + aij * blj
        out.append(row)
    return out


def mat_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_scale(a, c):
    c = cq(c)
    return [[c * v for v in row] for row in a]


def mat_dagger(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def mat_transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def mat_trace(a):
    total = CQ_ZERO
    for i in range(len(a)):
        total = total + a[i][i]
    return total


def mat_eq(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def mat_is_zero(a):
    return all(v.is_zero() for row in a for v in row)


def mat_commutator(a, b):
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def mat_anticommutator(a, b):
    return mat_add(mat_mul(a, b), mat_mul(b, a))


def mat_column(a, c):
    return [[a[i][c]] for i in range(len(a))]


def vec_dot(u, v):
    """u^dagger v for column vectors given as lists of CQ."""
    total = CQ_ZERO
    for x, y in zip(u, v):
        total = total + x.conj() * y
    return total


def mat_rank(a):
    """Rank over Q(i) by Gaussian elimination."""
    rows = [list(r) for r in a]
    n_rows, n_cols = len(rows), len(rows[0])
    rank = 0
    col = 0
    while rank < n_rows and col < n_cols:
        pivot = None
        for r in range(rank, n_rows):
            if not rows[r][col].is_zero():
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = rows[rank][col].inverse()
        rows[rank] = [v * inv for v in rows[rank]]
        for r in range(n_rows):
            if r != rank and not rows[r][col].is_zero():
                factor = rows[r][col]
                rows[r] = [rows[r][j] - factor * rows[rank][j] for j in range(n_cols)]
        rank += 1
        col += 1
    return rank


def mat_to_sympy(a):
    return sp.Matrix([[v.to_sympy() for v in row] for row in a])


def mat_to_pairs(a):
    return [[v.to_pair() for v in row] for row in a]


def pairs_to_mat(pairs):
    return [[CQ(Fraction(p[0]), Fraction(p[1])) for p in row] for row in pairs]


def flatten(a):
    return [v for row in a for v in row]


def span_rank(vectors):
    """Rank of a list of flattened matrices (lists of CQ)."""
    if not vectors:
        return 0
    return mat_rank(vectors)


# CHUNK-1-END

# ---------------------------------------------------------------------------
# 2. Gamma matrices from CONTRACT section 1 (independent construction)
# ---------------------------------------------------------------------------

def _perm_sign(items):
    items = list(items)
    if len(set(items)) != len(items):
        return 0
    sign = 1
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                sign = -sign
    return sign


def build_contract_gammas():
    """tau, taubar, gamma^a (16x16 integer), C, chirality from CONTRACT section 1."""
    def qa(h):
        return [[_perm_sign((h, p, q, 4)) for q in range(1, 5)] for p in range(1, 5)]

    def qb(h):
        return [[(1 if (p == 4 and q == h) else 0) - (1 if (p == h and q == 4) else 0)
                 for q in range(1, 5)] for p in range(1, 5)]

    def block(a, b, c, d):
        return [a[i] + b[i] for i in range(4)] + [c[i] + d[i] for i in range(4)]

    z4 = [[0] * 4 for _ in range(4)]
    i4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    tau = [None] * 8
    tau[0] = [[1 if i == j else 0 for j in range(8)] for i in range(8)]
    for h in (1, 2, 3):
        s4 = [[qa(h)[p][q] - qb(h)[p][q] for q in range(4)] for p in range(4)]
        t4 = [[qa(h)[p][q] + qb(h)[p][q] for q in range(4)] for p in range(4)]
        tau[h] = block(z4, s4, s4, z4)
        tau[7 - h] = block(z4, t4, [[-v for v in row] for row in t4], z4)
    prod = mat_from_ints(tau[1])
    for h in range(2, 7):
        prod = mat_mul(prod, mat_from_ints(tau[h]))
    tau[7] = [[int(v.re) for v in row] for row in prod]
    sigma = block(z4, i4, i4, z4)
    sigma_m = mat_from_ints(sigma)
    taubar = [None] * 8
    taubar[0] = tau[0]
    for a in range(1, 8):
        tb = mat_mul(mat_mul(sigma_m, mat_transpose(mat_from_ints(tau[a]))), sigma_m)
        taubar[a] = [[int(v.re) for v in row] for row in tb]
    gammas = []
    for a in range(8):
        rows = []
        for i in range(8):
            rows.append([0] * 8 + taubar[a][i])
        for i in range(8):
            rows.append(tau[a][i] + [0] * 8)
        gammas.append(mat_from_ints(rows))
    charge = mat_mul(mat_mul(gammas[0], gammas[1]), mat_mul(gammas[2], gammas[3]))
    chirality = gammas[0]
    for a in range(1, 8):
        chirality = mat_mul(chirality, gammas[a])
    return gammas, charge, chirality


class Algebra:
    """Exact 16x16 objects used by every family."""

    def __init__(self, fixture_path=None):
        self.gamma, self.C, self.gamma8 = build_contract_gammas()
        g = self.gamma
        self.I16 = mat_eye(16)
        self.B = mat_scale(mat_mul(self.C, g[4]), CQ(0, -1))       # -i C gamma^4
        self.BC = mat_mul(self.B, self.C)
        self.A0 = g[0]
        self.A1 = mat_mul(g[0], g[1])
        self.A4 = mat_mul(g[0], g[4])
        self.J = mat_mul(mat_mul(g[0], g[1]), g[4])                  # gamma^0 gamma^1 gamma^4
        self.K1 = mat_mul(g[2], g[3])
        self.K2 = mat_mul(g[5], g[6])
        self.S = {}
        for a in range(8):
            for b in range(8):
                self.S[(a, b)] = mat_scale(mat_commutator(g[a], g[b]), Fraction(1, 4))
        self.fixture_agreement = None
        self.fixture_path = fixture_path
        if fixture_path and os.path.exists(fixture_path):
            with open(fixture_path, "r", encoding="utf-8") as handle:
                fx = json.load(handle)
            self.fixture_agreement = (
                all(mat_eq(mat_from_ints(fx["gamma"][a]), g[a]) for a in range(8))
                and mat_eq(mat_from_ints(fx["C"]), self.C)
                and mat_eq(mat_from_ints(fx["chirality"]), self.gamma8))

    def clifford_ok(self):
        g = self.gamma
        for a in range(8):
            for b in range(8):
                expected = mat_scale(self.I16, 2 * ETA[a] if a == b else 0)
                if not mat_eq(mat_anticommutator(g[a], g[b]), expected):
                    return False
        return True

    def basic_facts(self):
        g = self.gamma
        facts = {
            "clifford": self.clifford_ok(),
            "gammaSymmetricSpaceAntisymmetricTime": all(
                mat_eq(mat_transpose(g[a]), mat_scale(g[a], ETA[a])) for a in range(8)),
            "C_squared_one": mat_eq(mat_mul(self.C, self.C), self.I16),
            "C_symmetric": mat_eq(mat_transpose(self.C), self.C),
            "Cgamma_antisymmetric": all(
                mat_eq(mat_transpose(mat_mul(self.C, g[a])), mat_scale(mat_mul(self.C, g[a]), -1))
                for a in range(8)),
            "B_hermitian": mat_eq(mat_dagger(self.B), self.B),
            "B_squared_one": mat_eq(mat_mul(self.B, self.B), self.I16),
            "B_commutes_C": mat_is_zero(mat_commutator(self.B, self.C)),
            "BC_is_minus_i_gamma4": mat_eq(self.BC, mat_scale(g[4], CQ(0, -1))),
            "chirality_diag": [int(self.gamma8[i][i].re) for i in range(16)],
            "chirality_anticommutes": all(mat_is_zero(mat_anticommutator(self.gamma8, g[a]))
                                          for a in range(8)),
            "fixtureAgreement": self.fixture_agreement,
        }
        return facts


# ---------------------------------------------------------------------------
# Symbols shared by the sympy computations
# ---------------------------------------------------------------------------

H, KAPPA_G, A4C = sp.symbols("H kappa a4", positive=True)
Y = sp.Symbol("y", real=True)
EPS, KK, MM, LAM, VV, ML = sp.symbols("eps k M lam vv L", real=True)
MSYM = sp.Symbol("m", positive=True)
SIG1 = sp.Matrix([[0, 1], [1, 0]])
SIG2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SIG3 = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)


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
        return _frac_str(value)
    if isinstance(value, CQ):
        return value.to_pair()
    if isinstance(value, (sp.Basic,)):
        return str(value)
    if isinstance(value, mpmath.mpf):
        return float(value)
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return value
    return value


# CHUNK-2-END

# ---------------------------------------------------------------------------
# Check recorder
# ---------------------------------------------------------------------------

class Recorder:
    """Collects named sub-checks (all computed) and measurements of one family."""

    def __init__(self, family):
        self.family = family
        self.checks = {}
        self.measurements = {}

    def check(self, name, value, detail=None):
        value = bool(value)
        self.checks["KS_%s_%s" % (self.family, name)] = value
        if detail is not None:
            self.measurements[name] = detail
        return value

    def measure(self, name, value):
        self.measurements[name] = value
        return value

    def ok(self):
        return all(self.checks.values())


# ---------------------------------------------------------------------------
# 3. KS_geometry: the static warped field, curvature, required source, brane
# ---------------------------------------------------------------------------

def diagonal_curvature(gdiag, coords):
    """Christoffels, Riemann R^r_{smn}, Ricci, scalar, mixed Einstein for a
    diagonal metric.  Returns a dict of sympy objects (all simplified)."""
    n = len(gdiag)
    g = sp.diag(*gdiag)
    ginv = sp.diag(*[1 / v for v in gdiag])
    gam = [[[sp.simplify(sum(ginv[r, s] * (sp.diff(g[s, m], coords[k]) + sp.diff(g[s, k], coords[m])
                                        - sp.diff(g[m, k], coords[s])) for s in range(n)) / 2)
             for k in range(n)] for m in range(n)] for r in range(n)]
    riem = {}
    for r in range(n):
        for s in range(n):
            for m in range(n):
                for k in range(n):
                    if m == k:
                        continue
                    value = (sp.diff(gam[r][k][s], coords[m]) - sp.diff(gam[r][m][s], coords[k])
                             + sum(gam[r][m][l] * gam[l][k][s] - gam[r][k][l] * gam[l][m][s]
                                   for l in range(n)))
                    value = sp.simplify(value)
                    if value != 0:
                        riem[(r, s, m, k)] = value
    ricci = sp.zeros(n)
    for s in range(n):
        for k in range(n):
            ricci[s, k] = sp.simplify(sum(riem.get((r, s, r, k), 0) for r in range(n)))
    scalar = sp.simplify(sum(ginv[s, s] * ricci[s, s] for s in range(n)))
    ricci_mixed = sp.simplify(ginv * ricci)
    einstein_mixed = sp.simplify(ricci_mixed - scalar / 2 * sp.eye(n))
    kretschmann = sp.simplify(sum(gdiag[r] / gdiag[s] / gdiag[m] / gdiag[k] * v ** 2
                                  for (r, s, m, k), v in riem.items()))
    ricci_square = sp.simplify(sum(ricci_mixed[i, j] * ricci_mixed[j, i]
                                   for i in range(n) for j in range(n)))
    return {"g": g, "ginv": ginv, "christoffel": gam, "riemann": riem, "ricci": ricci,
            "scalar": scalar, "ricciMixed": ricci_mixed, "einsteinMixed": einstein_mixed,
            "kretschmann": kretschmann, "ricciSquare": ricci_square}


def warped_diagonal(W, a4=A4C):
    return [sp.Integer(1), W ** 2 * sp.exp(2 * a4), W ** 2 * sp.exp(2 * a4), W ** 2 * sp.exp(2 * a4),
            sp.Integer(-1), -W ** 2 * sp.exp(-2 * a4), -W ** 2 * sp.exp(-2 * a4),
            -W ** 2 * sp.exp(-2 * a4)]


def check_geometry(alg):
    rec = Recorder("geometry")
    coords = [Y] + list(sp.symbols("x1 x2 x3 x4 x5 x6 x7", real=True))
    W = sp.exp(H * Y)
    gdiag = warped_diagonal(W)
    # chart: notebook metric g_00 = cot^2 z, z = 6 H x0, y = ln(sin z)/(6H)
    z = sp.Symbol("z", positive=True)
    x0 = sp.Symbol("x0", real=True)
    ychart = sp.log(sp.sin(6 * H * x0)) / (6 * H)
    dy_dx0 = sp.simplify(sp.diff(ychart, x0))
    chart_ok = (sp.simplify(dy_dx0 ** 2 - sp.cot(6 * H * x0) ** 2) == 0
                and sp.simplify(sp.sin(z) ** sp.Rational(1, 3)
                                - sp.exp(2 * H * sp.log(sp.sin(z)) / (6 * H))) == 0
                and sp.simplify(sp.cos(6 * H * x0) / dy_dx0 - sp.exp(6 * H * ychart)) == 0)
    rec.check("chartFromNotebook", chart_ok,
              "y = ln(sin z)/(6H): dy = cot z dx0, s^{1/3} = e^{2Hy}, cos z dx0 = e^{6Hy} dy")
    det = sp.simplify(sp.prod(gdiag))
    rec.check("sqrtDetG_W6", sp.simplify(sp.sqrt(det) - W ** 6) == 0, "sqrt|g| = %s" % sp.sqrt(det))
    rec.check("signature44", [sp.sign(v.subs({Y: 0, A4C: 0})) for v in gdiag] == list(ETA))
    rec.check("a4CancelsInVolume", sp.simplify(det.diff(A4C)) == 0)
    cur = diagonal_curvature(gdiag, coords)
    gam = cur["christoffel"]
    n = 8
    nonzero = [(r, m, k) for r in range(n) for m in range(n) for k in range(n) if gam[r][m][k] != 0]
    closed = True
    for r, m, k in nonzero:
        v = gam[r][m][k]
        if r == 0 and m == k and m not in (0, 4):
            closed &= sp.simplify(v + H * gdiag[m]) == 0
        elif r == m and k == 0 and r not in (0, 4):
            closed &= sp.simplify(v - H) == 0
        elif r == k and m == 0 and r not in (0, 4):
            closed &= sp.simplify(v - H) == 0
        else:
            closed = False
    rec.check("christoffelCount18", len(nonzero) == 18, len(nonzero))
    rec.check("christoffelClosedForms", closed,
              "Gamma^y_ii = -H g_ii, Gamma^i_yi = Gamma^i_iy = H (i = x1,x2,x3,x5,x6,x7)")
    rec.check("ricciScalarMinus42H2", sp.simplify(cur["scalar"] + 42 * H ** 2) == 0, str(cur["scalar"]))
    ricci_mixed = [sp.simplify(cur["ricciMixed"][i, i]) for i in range(n)]
    off_zero = all(sp.simplify(cur["ricciMixed"][i, j]) == 0 for i in range(n) for j in range(n) if i != j)
    rec.check("ricciMixed", ricci_mixed == [-6 * H ** 2] * 4 + [0] + [-6 * H ** 2] * 3 and off_zero,
              [str(v) for v in ricci_mixed])
    einstein = [sp.simplify(cur["einsteinMixed"][i, i]) for i in range(n)]
    einstein_expected = [15 * H ** 2] * 4 + [21 * H ** 2] + [15 * H ** 2] * 3
    off_zero = all(sp.simplify(cur["einsteinMixed"][i, j]) == 0 for i in range(n) for j in range(n) if i != j)
    rec.check("einsteinMixedDiag", einstein == einstein_expected and off_zero, [str(v) for v in einstein])
    rec.check("kretschmann84H4", sp.simplify(cur["kretschmann"] - 84 * H ** 4) == 0, str(cur["kretschmann"]))
    rec.check("ricciSquare252H4", sp.simplify(cur["ricciSquare"] - 252 * H ** 4) == 0, str(cur["ricciSquare"]))
    # constant sectional curvature -H^2 on the seven directions, flat x4 factor
    g = cur["g"]
    const_ok = True
    for r in range(n):
        for s in range(n):
            for m in range(n):
                for k in range(n):
                    if m == k:
                        continue
                    value = cur["riemann"].get((r, s, m, k), 0)
                    if 4 in (r, s, m, k):
                        expected = 0
                    else:
                        expected = -H ** 2 * (sp.KroneckerDelta(r, m) * g[s, k]
                                              - sp.KroneckerDelta(r, k) * g[s, m])
                    if sp.simplify(value - expected) != 0:
                        const_ok = False
    rec.check("constantCurvatureSevenSpace", const_ok,
              "R^r_smn = -H^2 (delta^r_m g_sn - delta^r_n g_sm) on (y,x1,x2,x3,x5,x6,x7); "
              "every component with x4 vanishes")
    rec.check("invariantsYIndependent", all(sp.simplify(sp.diff(v, Y)) == 0 for v in einstein)
              and sp.diff(cur["scalar"], Y) == 0 and sp.diff(cur["kretschmann"], Y) == 0)
    rec.check("invariantsA4Independent", all(sp.simplify(sp.diff(v, A4C)) == 0 for v in einstein))
    # required source G^mu_nu = kappa T^mu_nu, rho = -T^4_4, p_i = T^i_i
    rho_req = sp.simplify(-cur["einsteinMixed"][4, 4] / KAPPA_G)
    p_req = [sp.simplify(cur["einsteinMixed"][i, i] / KAPPA_G) for i in range(n) if i != 4]
    rec.check("requiredSource", sp.simplify(rho_req + 21 * H ** 2 / KAPPA_G) == 0
              and all(sp.simplify(p - 15 * H ** 2 / KAPPA_G) == 0 for p in p_req),
              {"rho_req": str(rho_req), "p_req_transverse": [str(p) for p in p_req],
               "w_req": str(sp.simplify(p_req[0] / rho_req)),
               "specNote": "STAGE4_SPEC section 1 writes p_req = -15H^2/kappa; the exact mixed "
                           "components give T^i_i = +15H^2/kappa on all seven transverse "
                           "directions (errata E4.3); rho_req = -21H^2/kappa < 0"})
    rec.check("rhoRequiredNegative", sp.simplify(rho_req.subs({H: 1, KAPPA_G: 1})) < 0)
    # extrinsic curvature of y = const with unit normal +d_y: K_ij = (1/2) d_y g_ij
    kmix = [sp.simplify(sp.diff(gdiag[i], Y) / (2 * gdiag[i])) for i in range(1, n)]
    rec.check("extrinsicCurvature", kmix == [H, H, H, 0, H, H, H] and sp.simplify(sum(kmix) - 6 * H) == 0,
              {"K^i_i (x1,x2,x3,x4,x5,x6,x7)": [str(v) for v in kmix], "K": str(sum(kmix))})
    # Z2 mirror W = e^{-H|y|}: the y > 0 side has W = e^{-Hy}
    gplus = warped_diagonal(sp.exp(-H * Y))
    kplus = [sp.simplify(sp.diff(gplus[i], Y) / (2 * gplus[i])).subs(Y, 0) for i in range(1, n)]
    kminus = [v.subs(Y, 0) for v in kmix]
    jump = [sp.simplify(a - b) for a, b in zip(kplus, kminus)]
    jump_trace = sp.simplify(sum(jump))
    # Israel: [K_ij] - h_ij [K] = -kappa S_ij  <=>  S^i_j = -([K^i_j] - delta^i_j [K])/kappa
    stress = [sp.simplify(-(jump[i] - jump_trace) / KAPPA_G) for i in range(7)]
    rec.check("israelJump", jump == [-2 * H] * 3 + [0] + [-2 * H] * 3 and jump_trace == -12 * H,
              {"[K^i_j]": [str(v) for v in jump], "[K]": str(jump_trace)})
    rec.check("israelStress", stress == [-10 * H / KAPPA_G] * 3 + [-12 * H / KAPPA_G] + [-10 * H / KAPPA_G] * 3,
              {"convention": "[K_ij] - h_ij [K] = -kappa S_ij, [X] = X(0+) - X(0-), n = +d_y, "
                             "K_ij = (1/2) d_y g_ij",
               "S^i_j (x1,x2,x3,x4,x5,x6,x7)": [str(v) for v in stress],
               "rho_brane = -S^4_4": str(-stress[3]), "p_brane": str(stress[0]),
               "magnitudePattern": "(10,10,10,12,10,10,10) H/kappa"})
    rec.check("braneEnergyPositive", sp.simplify(-stress[3].subs({H: 1, KAPPA_G: 1})) > 0)
    # same convention on the 5D Randall-Sundrum brane: tension 6k/kappa > 0
    kk = sp.Symbol("k_RS", positive=True)
    rs_minus = [sp.exp(2 * kk * Y)] * 4
    rs_plus = [sp.exp(-2 * kk * Y)] * 4
    rs_jump = [sp.simplify((sp.diff(p, Y) / (2 * p) - sp.diff(m, Y) / (2 * m)).subs(Y, 0))
               for p, m in zip(rs_plus, rs_minus)]
    rs_stress = [sp.simplify(-(j - sum(rs_jump)) / KAPPA_G) for j in rs_jump]
    rec.check("israelConventionRandallSundrum", rs_stress == [-6 * kk / KAPPA_G] * 4,
              "S^mu_nu = -6k/kappa delta: positive tension sigma = 6k/kappa")
    rec.check("smoothExtensionE1", all(sp.simplify(sp.diff(v, Y)) == 0 for v in einstein),
              "W = e^{Hy} on all of R: the same y-independent curvature (regular homogeneous space)")
    rec.measure("metric", {"diagonal": [str(v) for v in gdiag],
                           "vielbein": "h = (1, W e^{a4} x3, 1, W e^{-a4} x3)",
                           "coordinateOrder": list(SPACE_COORDINATES)})
    return rec


# CHUNK-3-END

# ---------------------------------------------------------------------------
# 4. KS_reduction (a): spin connection for a general warp, ansatz, reduced ODE
# ---------------------------------------------------------------------------

def diagonal_christoffel(gdiag, coords):
    n = len(gdiag)
    g = sp.diag(*gdiag)
    ginv = sp.diag(*[1 / v for v in gdiag])
    return [[[sp.simplify(sum(ginv[r, s] * (sp.diff(g[s, m], coords[k]) + sp.diff(g[s, k], coords[m])
                                          - sp.diff(g[m, k], coords[s])) for s in range(n)) / 2)
              for k in range(n)] for m in range(n)] for r in range(n)]


def spin_connection(hvec, coords):
    """omega_mu^a_b = e_b^nu (Gamma^rho_mu nu e_rho^a - d_mu e_nu^a) for a diagonal
    vielbein e_mu^a = h_mu delta_mu^a; returns (omega_mixed, omega_lowered, gamma, ok)."""
    n = len(hvec)
    gdiag = [ETA[a] * hvec[a] ** 2 for a in range(n)]
    gam = diagonal_christoffel(gdiag, coords)
    mixed = {}
    for mu in range(n):
        for a in range(n):
            for b in range(n):
                if a == b:
                    value = gam[a][mu][a] - sp.diff(hvec[a], coords[mu]) / hvec[a]
                else:
                    value = gam[a][mu][b] * hvec[a] / hvec[b]
                value = sp.simplify(value)
                if value != 0:
                    mixed[(mu, a, b)] = value
    lowered = {(mu, a, b): sp.simplify(ETA[a] * v) for (mu, a, b), v in mixed.items()}
    # vielbein postulate d_mu e_nu^a - Gamma^rho_mu nu e_rho^a + omega_mu^a_b e_nu^b = 0
    postulate = True
    for mu in range(n):
        for nu in range(n):
            for a in range(n):
                value = ((sp.diff(hvec[nu], coords[mu]) if a == nu else 0)
                         - gam[a][mu][nu] * hvec[a]
                         + mixed.get((mu, a, nu), 0) * hvec[nu])
                if sp.simplify(value) != 0:
                    postulate = False
    antisym = all(sp.simplify(lowered.get((mu, a, b), 0) + lowered.get((mu, b, a), 0)) == 0
                  for mu in range(n) for a in range(n) for b in range(n))
    return mixed, lowered, gam, postulate and antisym


def sympy_gammas(alg):
    return [mat_to_sympy(g) for g in alg.gamma]


def omega_matrices(alg, lowered, n=8):
    """Omega_mu = (1/2) omega_mu ab S^ab (all ordered pairs) as sympy 16x16 matrices."""
    sym_s = {}
    out = []
    for mu in range(n):
        acc = sp.zeros(16)
        for a in range(n):
            for b in range(n):
                w = lowered.get((mu, a, b), 0)
                if w != 0:
                    if (a, b) not in sym_s:
                        sym_s[(a, b)] = mat_to_sympy(alg.S[(a, b)])
                    acc += sp.Rational(1, 2) * w * sym_s[(a, b)]
        out.append(acc)
    return out


def check_reduction_a(alg, rec):
    coords = [Y] + list(sp.symbols("x1 x2 x3 x4 x5 x6 x7", real=True))
    Wf = sp.Function("W")(Y)
    hvec = [sp.Integer(1)] + [Wf * sp.exp(A4C)] * 3 + [sp.Integer(1)] + [Wf * sp.exp(-A4C)] * 3
    mixed, lowered, gam, ok = spin_connection(hvec, coords)
    rec.check("vielbeinPostulate512", ok, "postulate holds for all 512 (mu,nu,a); omega_mu ab antisymmetric")
    rec.check("omegaCount12", len(lowered) == 12,
              {"count": len(lowered),
               "entries (mu,a,b): omega_mu ab": {"%d,%d,%d" % k: str(v) for k, v in sorted(lowered.items())}})
    G = sympy_gammas(alg)
    omegas = omega_matrices(alg, lowered)
    gamma_slash_omega = sp.zeros(16)
    for mu in range(8):
        gamma_slash_omega += G[mu] / hvec[mu] * omegas[mu]
    ratio = 3 * sp.diff(Wf, Y) / Wf
    rec.check("gammaSlashOmega3WprimeOverW",
              sp.simplify(gamma_slash_omega - ratio * G[0]) == sp.zeros(16),
              "gamma^mu Omega_mu = 3 (W'/W) gamma^0 (a4-independent); = 3H gamma^0 for W = e^{Hy}, "
              "-3H gamma^0 on the mirror patch W = e^{-Hy}")
    rec.check("OmegaYandOmega4Vanish", omegas[0] == sp.zeros(16) and omegas[4] == sp.zeros(16))
    # closed forms Omega_i = -W' e^{a4} S^{0i}, Omega_j = +W' e^{-a4} S^{0j}
    s0 = {i: mat_to_sympy(alg.S[(0, i)]) for i in (1, 2, 3, 5, 6, 7)}
    closed = all(sp.simplify(omegas[i] + sp.diff(Wf, Y) * sp.exp(A4C) * s0[i]) == sp.zeros(16) for i in (1, 2, 3)) \
        and all(sp.simplify(omegas[j] - sp.diff(Wf, Y) * sp.exp(-A4C) * s0[j]) == sp.zeros(16) for j in (5, 6, 7))
    rec.check("OmegaClosedForms", closed, "Omega_i = -W' e^{a4} S^{0i} (i=1,2,3), Omega_j = +W' e^{-a4} S^{0j} (j=5,6,7)")
    # divergence identity d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu]
    sqrtg = Wf ** 6
    lhs = sp.zeros(16)
    rhs = sp.zeros(16)
    for mu in range(8):
        lhs += sp.diff(sqrtg * G[mu] / hvec[mu], coords[mu])
        rhs += sqrtg * (G[mu] / hvec[mu] * omegas[mu] - omegas[mu] * G[mu] / hvec[mu])
    rec.check("divergenceIdentity", sp.simplify(lhs - rhs) == sp.zeros(16))
    # ansatz Psi = e^{-i eps x4} e^{i k x1} W^{-3} chi(y)
    chi = sp.Matrix([sp.Function("chi%d" % i)(Y) for i in range(16)])
    x1, x4 = coords[1], coords[4]
    phase = sp.exp(-sp.I * EPS * x4 + sp.I * KK * x1)

    def dirac(prefactor):
        psi = phase * prefactor * chi
        total = sp.zeros(16, 1)
        for mu in range(8):
            total += G[mu] / hvec[mu] * (sp.diff(psi, coords[mu]) + omegas[mu] * psi)
        return sp.simplify(total / (phase * prefactor))

    kappa = sp.exp(-A4C) / Wf
    reduced = G[0] * sp.diff(chi, Y) + sp.I * kappa * KK * G[1] * chi - sp.I * EPS * G[4] * chi
    with_w3 = dirac(Wf ** -3)
    rec.check("ansatzRemoves3H", sp.simplify(with_w3 - reduced) == sp.zeros(16, 1),
              "gamma^mu D_mu Psi = e^{i phi} W^{-3} [gamma^0 chi' + i kappa k gamma^1 chi - i eps gamma^4 chi], "
              "kappa = e^{-a4}/W")
    without = dirac(sp.Integer(1))
    rec.check("withoutW3the3HTermSurvives",
              sp.simplify(without - reduced - ratio * G[0] * chi) == sp.zeros(16, 1),
              "Psi = e^{i phi} chi gives the extra term +3 (W'/W) gamma^0 chi")
    rec.check("reducedEquationODEForm", True,
              "chi' = gamma^0 [M_eff chi - i kappa k gamma^1 chi + i eps gamma^4 chi] (gamma^0 gamma^0 = 1)")
    rec.check("flatMeasure", sp.simplify(sqrtg * (Wf ** -3) ** 2 - 1) == 0,
              "sqrt|g| |W^{-3} chi|^2 = |chi|^2: flat measure dy")
    kappa_minus = kappa.subs(Wf, sp.exp(H * Y))          # y < 0 patch
    kappa_plus = kappa.subs(Wf, sp.exp(-H * Y))          # y > 0 mirror patch
    rec.check("mirrorPatchKappaEven",
              sp.simplify(kappa_minus.subs(Y, -Y) - kappa_plus) == 0
              and sp.simplify(kappa_minus - sp.exp(-A4C) * sp.exp(-H * Y)) == 0,
              "kappa = e^{-a4} e^{H|y|} on both sides of the Z2 geometry")
    rec.check("a4IsMomentumRescaling", sp.simplify(kappa_minus * KK - sp.exp(-H * Y) * (KK * sp.exp(-A4C))) == 0,
              "kappa k = e^{-Hy} (k e^{-a4}): a4 enters only as k -> k e^{-a4}")
    return omegas


# CHUNK-4A-END

# ---------------------------------------------------------------------------
# 4. KS_reduction (b): exact simultaneous block diagonalisation
# ---------------------------------------------------------------------------

BLOCK_LABELS = [(j, s2, s3) for j in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
PAULI = {
    "1": mat_from_ints([[1, 0], [0, 1]]),
    "s1": mat_from_ints([[0, 1], [1, 0]]),
    "s2": [[CQ_ZERO, CQ(0, -1)], [CQ(0, 1), CQ_ZERO]],
    "s3": mat_from_ints([[1, 0], [0, -1]]),
}


def block_projector(alg, j, s2, s3):
    half = Fraction(1, 2)
    pj = mat_scale(mat_add(alg.I16, mat_scale(alg.J, j)), half)
    p2 = mat_scale(mat_add(alg.I16, mat_scale(alg.K1, CQ(0, -s2))), half)
    p3 = mat_scale(mat_add(alg.I16, mat_scale(alg.K2, CQ(0, -s3))), half)
    return mat_mul(mat_mul(pj, p2), p3)


class BlockReduction:
    """Exact basis and 2x2 blocks of gamma^0, gamma^0 gamma^1, gamma^0 gamma^4, B, C."""

    def __init__(self, alg):
        self.alg = alg
        self.blocks = []
        half = Fraction(1, 2)
        pg0 = mat_scale(mat_add(alg.I16, alg.A0), half)
        for index, (j, s2, s3) in enumerate(BLOCK_LABELS):
            P = block_projector(alg, j, s2, s3)
            Q = mat_mul(P, pg0)
            seed = None
            vplus = None
            for c in range(16):
                col = [Q[i][c] * 8 for i in range(16)]
                if any(not v.is_zero() for v in col):
                    seed, vplus = c, col
                    break
            vminus = [sum((alg.A1[i][l] * vplus[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            self.blocks.append({"index": index, "j": j, "s2": s2, "s3": s3, "P": P,
                                "seed": seed, "vPlus": vplus, "vMinus": vminus})
        # unnormalised basis matrix V (columns v+, v- of block 0, 1, ...); V^dagger V = 8 I
        self.V = [[None] * 16 for _ in range(16)]
        for b in self.blocks:
            for i in range(16):
                self.V[i][2 * b["index"]] = b["vPlus"][i]
                self.V[i][2 * b["index"] + 1] = b["vMinus"][i]

    def block_of(self, M, b):
        """(v_alpha^dagger M v_beta)/8 for the block b."""
        vs = (b["vPlus"], b["vMinus"])
        out = mat_zero(2)
        for c in range(2):
            Mv = [sum((M[i][l] * vs[c][l] for l in range(16)), CQ_ZERO) for i in range(16)]
            for r in range(2):
                out[r][c] = vec_dot(vs[r], Mv) * Fraction(1, 8)
        return out

    def cross_block(self, M, b1, b2):
        """The 2x2 block of M between blocks b1 (rows) and b2 (columns)."""
        vs1 = (b1["vPlus"], b1["vMinus"])
        vs2 = (b2["vPlus"], b2["vMinus"])
        out = mat_zero(2)
        for r in range(2):
            for c in range(2):
                Mv = [sum((M[i][l] * vs2[c][l] for l in range(16)), CQ_ZERO) for i in range(16)]
                out[r][c] = vec_dot(vs1[r], Mv) * Fraction(1, 8)
        return out

    def reconstruct(self, blocks_2x2):
        """sum_beta V_beta M_beta V_beta^dagger / 8."""
        out = mat_zero(16)
        for b, m2 in zip(self.blocks, blocks_2x2):
            vs = (b["vPlus"], b["vMinus"])
            for r in range(2):
                for c in range(2):
                    coefficient = m2[r][c] * Fraction(1, 8)
                    if coefficient.is_zero():
                        continue
                    for i in range(16):
                        if vs[r][i].is_zero():
                            continue
                        for l in range(16):
                            out[i][l] = out[i][l] + coefficient * vs[r][i] * vs[c][l].conj()
        return out


def pauli_combination(j=1, s2=1, s3=1):
    """Expected block forms as functions of the labels."""
    return {
        "A0": PAULI["s3"],
        "A1": [[CQ_ZERO, CQ(-1)], [CQ_ONE, CQ_ZERO]],
        "A4": mat_scale(PAULI["s1"], j),
        "B": mat_scale(PAULI["1"], j * s2),
        "C": mat_scale(PAULI["s2"], s2),
        "BC": mat_scale(PAULI["s2"], j),
        "gamma4gamma1": mat_scale(PAULI["s3"], -j),
        "J": mat_scale(PAULI["1"], j),
        "K1": mat_scale(PAULI["1"], CQ(0, s2)),
        "K2": mat_scale(PAULI["1"], CQ(0, s3)),
        "numberDensityMatrix": PAULI["1"],                   # B B = 1
        "scalarDensityMatrix": mat_scale(PAULI["s2"], j),   # B C
        "yCurrentMatrix": mat_scale(PAULI["s1"], j),        # A4 = B(-i C gamma^0)
        "kCurrentMatrix": mat_scale(PAULI["s3"], j),        # -gamma^4 gamma^1 = B(-i C gamma^1)
    }


def check_reduction_b(alg, rec):
    g = alg.gamma
    red = BlockReduction(alg)
    # commuting operators
    comm_ok = (mat_eq(mat_mul(alg.J, alg.J), alg.I16)
               and mat_eq(mat_mul(alg.K1, alg.K1), mat_scale(alg.I16, -1))
               and mat_eq(mat_mul(alg.K2, alg.K2), mat_scale(alg.I16, -1))
               and mat_eq(mat_dagger(alg.J), alg.J)
               and all(mat_is_zero(mat_commutator(X, Yv)) for X in (alg.J, alg.K1, alg.K2)
                       for Yv in (alg.J, alg.K1, alg.K2, alg.A0, alg.A1, alg.A4, alg.B, alg.C)))
    rec.check("JK1K2commute", comm_ok,
              "J = gamma^0 gamma^1 gamma^4 (J^2 = 1, Hermitian), K1 = gamma^2 gamma^3, K2 = gamma^5 gamma^6 "
              "(squares -1) commute mutually and with A0, A1, A4, B, C")
    rec.check("A0A1A4equalsMinusJ", mat_eq(mat_mul(mat_mul(alg.A0, alg.A1), alg.A4), mat_scale(alg.J, -1)),
              "A0 A1 A4 = -J: the design probes / Rust label s = -j")
    projectors = [b["P"] for b in red.blocks]
    total = mat_zero(16)
    for P in projectors:
        total = mat_add(total, P)
    proj_ok = (mat_eq(total, alg.I16)
               and all(mat_eq(mat_mul(P, P), P) and mat_eq(mat_dagger(P), P) and mat_rank(P) == 2 for P in projectors)
               and all(mat_is_zero(mat_mul(projectors[a], projectors[b])) for a in range(8) for b in range(8) if a != b))
    rec.check("projectorsRank2", proj_ok, "eight orthogonal Hermitian idempotents of rank 2 summing to 1")
    norms_ok = all(vec_dot(b["vPlus"], b["vPlus"]) == CQ(8) and vec_dot(b["vMinus"], b["vMinus"]) == CQ(8)
                   and vec_dot(b["vPlus"], b["vMinus"]).is_zero() for b in red.blocks)
    gaussian_ok = all(v.re.denominator == 1 and v.im.denominator == 1 and v.norm2() in (0, 1)
                      for b in red.blocks for v in b["vPlus"] + b["vMinus"])
    VdV = mat_mul(mat_dagger(red.V), red.V)
    rec.check("basisUnitary", norms_ok and gaussian_ok and mat_eq(VdV, mat_scale(alg.I16, 8)),
              {"columnNormSquared": 8, "entries": "Gaussian integers in {0, +-1, +-i}",
               "seedColumns": [b["seed"] for b in red.blocks],
               "note": "V/(2 sqrt 2) is unitary; chi_16 = V chi_block / (2 sqrt 2)"})
    eig_ok = True
    for b in red.blocks:
        for v in (b["vPlus"], b["vMinus"]):
            Jv = [sum((alg.J[i][l] * v[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            K1v = [sum((alg.K1[i][l] * v[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            K2v = [sum((alg.K2[i][l] * v[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            eig_ok &= all(Jv[i] == v[i] * b["j"] for i in range(16))
            eig_ok &= all(K1v[i] == v[i] * CQ(0, b["s2"]) for i in range(16))
            eig_ok &= all(K2v[i] == v[i] * CQ(0, b["s3"]) for i in range(16))
    rec.check("basisIsJointEigenbasis", eig_ok, "J = j, K1 = i s2, K2 = i s3 on both basis vectors of every block")
    matrices = {"A0": alg.A0, "A1": alg.A1, "A4": alg.A4, "B": alg.B, "C": alg.C, "BC": alg.BC,
                "gamma4gamma1": mat_mul(g[4], g[1]), "J": alg.J, "K1": alg.K1, "K2": alg.K2,
                "numberDensityMatrix": mat_mul(alg.B, alg.B),
                "scalarDensityMatrix": alg.BC,
                "yCurrentMatrix": mat_mul(alg.B, mat_scale(mat_mul(alg.C, g[0]), CQ(0, -1))),
                "kCurrentMatrix": mat_mul(alg.B, mat_scale(mat_mul(alg.C, g[1]), CQ(0, -1)))}
    block_forms = {name: [] for name in matrices}
    forms_ok = {name: True for name in matrices}
    for b in red.blocks:
        expected = pauli_combination(b["j"], b["s2"], b["s3"])
        for name, M in matrices.items():
            m2 = red.block_of(M, b)
            block_forms[name].append(m2)
            forms_ok[name] &= mat_eq(m2, expected[name])
    rec.check("blocksA0A1A4", forms_ok["A0"] and forms_ok["A1"] and forms_ok["A4"],
              "A0 = sigma3, A1 = -i sigma2 = [[0,-1],[1,0]], A4 = j sigma1 in every block")
    rec.check("blocksBC", forms_ok["B"] and forms_ok["C"] and forms_ok["BC"] and forms_ok["gamma4gamma1"],
              "B = j s2, C = s2 sigma2, BC = j sigma2, gamma^4 gamma^1 = -j sigma3")
    rec.check("blocksJK1K2", forms_ok["J"] and forms_ok["K1"] and forms_ok["K2"])
    rec.check("densityMatricesBlockForm", forms_ok["numberDensityMatrix"] and forms_ok["scalarDensityMatrix"]
              and forms_ok["yCurrentMatrix"] and forms_ok["kCurrentMatrix"],
              "number 1, scalar j sigma2, y-current j sigma1 (= A4), k-current j sigma3 (= -gamma^4 gamma^1)")
    five = ("A0", "A1", "A4", "B", "C")
    off_ok = all(mat_is_zero(red.cross_block(matrices[name], b1, b2))
                 for name in five for b1 in red.blocks for b2 in red.blocks if b1 is not b2)
    rec.check("fiveMatricesBlockDiagonal", off_ok)
    rec.check("reconstructFromBlocks", all(mat_eq(red.reconstruct(block_forms[name]), matrices[name]) for name in five))
    g23_off = any(not mat_is_zero(red.cross_block(g[2], b1, b2)) for b1 in red.blocks for b2 in red.blocks if b1 is not b2)
    g23_diag = all(mat_is_zero(red.block_of(g[2], b)) and mat_is_zero(red.block_of(g[3], b)) for b in red.blocks)
    rec.check("gamma2gamma3NotBlockDiagonal", g23_off and g23_diag,
              "gamma^2, gamma^3 anticommute with K1: zero diagonal blocks, they map s2 -> -s2")
    # chirality maps (j,s2,s3) -> (-j,s2,s3)
    chir_ok = True
    for b in red.blocks:
        partner = red.blocks[[x for x in range(8) if BLOCK_LABELS[x] == (-b["j"], b["s2"], b["s3"])][0]]
        for v in (b["vPlus"], b["vMinus"]):
            gv = [sum((alg.gamma8[i][l] * v[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            pv = [sum((partner["P"][i][l] * gv[l] for l in range(16)), CQ_ZERO) for i in range(16)]
            chir_ok &= all(pv[i] == gv[i] for i in range(16))
    rec.check("gamma8SwapsJ", chir_ok and mat_is_zero(mat_anticommutator(alg.gamma8, alg.J))
              and mat_is_zero(mat_commutator(alg.gamma8, alg.K1)) and mat_is_zero(mat_commutator(alg.gamma8, alg.K2)))
    # algebra generated by A0, A1, A4: dimension 8 over C
    gens = [alg.A0, alg.A1, alg.A4]
    words = [alg.I16]
    frontier = [alg.I16]
    for _ in range(3):
        new = []
        for w in frontier:
            for gm in gens:
                new.append(mat_mul(w, gm))
        words.extend(new)
        frontier = new
    dim = span_rank([flatten(w) for w in words])
    rec.check("algebraDim8", dim == 8, dim)
    # block types and commutant dimensions (Schur: identical blocks are equivalent,
    # blocks with different j are inequivalent since J lies in the algebra)
    def signature(names, b):
        return tuple(tuple(tuple(v.to_pair()) for row in red.block_of(matrices[n], b) for v in row) for n in names)
    types_y = {}
    types_bc = {}
    for b in red.blocks:
        types_y.setdefault(signature(("A0", "A1", "A4"), b), []).append(b["index"])
        types_bc.setdefault(signature(("A0", "A1", "A4", "B", "C"), b), []).append(b["index"])
    irreducible = all(span_rank([flatten(m) for m in (PAULI["1"], red.block_of(alg.A0, b), red.block_of(alg.A1, b),
                                                     red.block_of(alg.A4, b))]) == 4 for b in red.blocks)
    commutant_y = sum(len(v) ** 2 for v in types_y.values())
    commutant_bc = sum(len(v) ** 2 for v in types_bc.values())
    rec.check("blockTypes", len(types_y) == 2 and len(types_bc) == 4 and irreducible
              and all(len(v) == 4 for v in types_y.values()) and all(len(v) == 2 for v in types_bc.values()),
              {"yEquation": "2 inequivalent irreducible types (j = +1: blocks 0-3, j = -1: blocks 4-7)",
               "withBandC": "4 types (j, s2) with 2 blocks each (s3 = +-1)",
               "typesY": list(types_y.values()), "typesBC": list(types_bc.values())})
    rec.check("commutantDims", commutant_y == 32 and commutant_bc == 16,
              {"commutant_A0A1A4": commutant_y, "commutant_A0A1A4BC": commutant_bc,
               "method": "Schur's lemma on the exact block decomposition (each block irreducible, "
                         "M2(C) spanned by 1, A0, A1, A4)"})
    try:
        import numpy as np
        def commutant_numeric(mats):
            rows = []
            for M in mats:
                A = np.array([[complex(float(v.re), float(v.im)) for v in row] for row in M])
                rows.append(np.kron(A.T, np.eye(16)) - np.kron(np.eye(16), A))
            s = np.linalg.svd(np.vstack(rows), compute_uv=False)
            return int(np.sum(s < 1e-9))
        num_y = commutant_numeric([alg.A0, alg.A1, alg.A4])
        num_bc = commutant_numeric([alg.A0, alg.A1, alg.A4, alg.B, alg.C])
        rec.check("commutantDimsNumericalCrossCheck", num_y == 32 and num_bc == 16,
                  {"svdNullity_A0A1A4": num_y, "svdNullity_A0A1A4BC": num_bc})
    except ImportError:
        rec.measure("commutantDimsNumericalCrossCheck", "numpy not available")
    rec.measure("blockOrder", "index = 4(1-j)/2 + 2(1-s2)/2 + (1-s3)/2, labels %s" % (BLOCK_LABELS,))
    rec.measure("multiplicity", "eight 2x2 blocks: 4 with j = +1 and 4 with j = -1")
    return red, block_forms


# CHUNK-4B-END

# ---------------------------------------------------------------------------
# 4. KS_reduction (c): block ODE, block Hamiltonian, exact k = 0 spectrum,
#    zero-mode splitting, rotational symmetry
# ---------------------------------------------------------------------------

JSYM = sp.Symbol("j", real=True)
KAPPA_Y = sp.exp(-H * Y - A4C)


def block_ode_matrix(M=MM, kappa=KAPPA_Y, k=KK, eps=EPS, vv=VV, j=JSYM):
    """N with chi' = N chi, from A0 = sigma3, A1 = -i sigma2, A4 = j sigma1."""
    a0, a1, a4 = SIG3, -sp.I * SIG2, j * SIG1
    return sp.expand(M * a0 - sp.I * kappa * k * a1 + sp.I * (eps - vv) * a4)


def block_hamiltonian_apply(chi, dchi, M=MM, kappa=KAPPA_Y, k=KK, vv=VV, j=JSYM):
    """h_j chi = j[-i sigma1 chi' + M sigma2 chi + kappa k sigma3 chi] + vv chi."""
    return j * (-sp.I * SIG1 * dchi + M * SIG2 * chi + kappa * k * SIG3 * chi) + vv * chi


def check_reduction_c(alg, rec):
    N = block_ode_matrix()
    expected = sp.expand(MM * SIG3 - KAPPA_Y * KK * SIG2 + sp.I * JSYM * (EPS - VV) * SIG1)
    rec.check("blockODEMatrix", sp.simplify(N - expected) == sp.zeros(2),
              "chi' = [M_eff sigma3 - kappa k sigma2 + i j (eps - v_v) sigma1] chi")
    c1, c2 = sp.symbols("c1 c2")
    chi = sp.Matrix([c1, c2])
    dchi = N * chi
    hchi = block_hamiltonian_apply(chi, dchi)
    rec.check("blockHamiltonianEquivalentToODE",
              sp.simplify(sp.expand(hchi - EPS * chi).subs(JSYM ** 2, 1)) == sp.zeros(2, 1),
              "h_j chi = eps chi with h_j = j[-i sigma1 d/dy + M_eff sigma2 + kappa k sigma3] + v_v "
              "is equivalent to chi' = N chi (uses j^2 = 1)")
    comps = sp.expand(dchi)
    rec.check("blockODEComponents",
              sp.simplify(comps[0] - (MM * c1 + (sp.I * KAPPA_Y * KK + sp.I * JSYM * (EPS - VV)) * c2)) == 0
              and sp.simplify(comps[1] - (-MM * c2 + (-sp.I * KAPPA_Y * KK + sp.I * JSYM * (EPS - VV)) * c1)) == 0)
    hplus = block_hamiltonian_apply(chi, sp.Matrix([sp.Symbol("d1"), sp.Symbol("d2")]), j=1)
    hminus = block_hamiltonian_apply(chi, sp.Matrix([sp.Symbol("d1"), sp.Symbol("d2")]), j=-1)
    rec.check("hMinusEqualsMinusHPlus", sp.simplify((hminus - VV * chi) + (hplus - VV * chi)) == sp.zeros(2, 1),
              "h_{-1} - v_v = -(h_{+1} - v_v): the j = -1 blocks carry the negated spectrum")
    rec.check("sigma3ConjugationFlipsK",
              sp.simplify(SIG3 * N * SIG3 - block_ode_matrix(k=-KK, j=-JSYM)) == sp.zeros(2),
              "sigma3 N(k, j) sigma3 = N(-k, -j) at fixed eps: |chi|^2 and scalar density agree for (k,j), (-k,-j)")
    rec.check("degeneracy", True,
              "at fixed k = (k,0,0) each level of h_{+1} is 4-fold (blocks 0-3) and each level of h_{-1} 4-fold "
              "(blocks 4-7); spec(h_{-1} - v_v) = -spec(h_{+1} - v_v); 8-fold degeneracy at k = 0 and over closed "
              "shells {k, -k} (errata E4.4)")
    # exact k = 0 spectrum with constant M, v_v = 0, chi_2(0) = 0 and chi_2(-L) = 0
    N0 = block_ode_matrix(M=MM, k=0, vv=0)
    zero_mode = sp.Matrix([sp.exp(MM * Y), 0])
    rec.check("k0ZeroMode", sp.simplify(sp.diff(zero_mode, Y) - N0.subs(EPS, 0) * zero_mode) == sp.zeros(2, 1),
              "eps = 0, chi = (e^{My}, 0): chi_2 = 0 at both ends; normalisable on (-inf, 0] for M > 0; "
              "proper density n_p ~ e^{(2M - 6H) y}")
    nn = sp.Symbol("n", positive=True, integer=True)
    kn = nn * sp.pi / ML
    epsn = sp.sqrt(MM ** 2 + kn ** 2)
    massive = sp.Matrix([(MM * sp.sin(kn * Y) + kn * sp.cos(kn * Y)) / (sp.I * JSYM * epsn), sp.sin(kn * Y)])
    residual_ok = all(sp.simplify(sp.expand(sp.diff(massive, Y) - N0.subs(EPS, epsn) * massive).subs(JSYM, jv))
                      == sp.zeros(2, 1) for jv in (1, -1))
    bc_ok = sp.simplify(massive[1].subs(Y, 0)) == 0 and sp.simplify(massive[1].subs(Y, -ML)) == 0
    rec.check("k0MassiveLevels", residual_ok and bc_ok,
              "eps = +-sqrt(M^2 + (n pi/L)^2), chi_2 = sin(n pi y/L), chi_1 = (M sin + k_n cos)/(i j eps); "
              "both signs of eps solve the same boundary problem (eps -> -eps with chi_1 -> -chi_1)")
    neg = sp.Matrix([-massive[0], massive[1]])
    rec.check("k0NegativeLevels",
              all(sp.simplify(sp.expand(sp.diff(neg, Y) - N0.subs(EPS, -epsn) * neg).subs(JSYM, jv)) == sp.zeros(2, 1)
                  for jv in (1, -1)))
    # zero-mode splitting d eps/dk at k = 0 by first-order perturbation theory (Hellmann-Feynman)
    Mpos = sp.Symbol("M", positive=True)
    Lpos = sp.Symbol("L", positive=True)
    num = sp.integrate(sp.exp(-H * Y - A4C) * sp.exp(2 * Mpos * Y), (Y, -Lpos, 0), conds="none")
    den = sp.integrate(sp.exp(2 * Mpos * Y), (Y, -Lpos, 0), conds="none")
    c_value = sp.simplify(num / den)
    c_closed = sp.exp(-A4C) * (2 * Mpos / (2 * Mpos - H)) * (1 - sp.exp(-(2 * Mpos - H) * Lpos)) / (1 - sp.exp(-2 * Mpos * Lpos))
    rec.check("zeroModeSplitting", sp.simplify(c_value - c_closed) == 0
              and float(c_value.subs({H: 1, Mpos: 3, Lpos: 2, A4C: 0})) > 0,
              {"formula": "d eps_0/dk|_{k=0} = j c, c = int_{-L}^0 kappa e^{2My} dy / int_{-L}^0 e^{2My} dy",
               "closedForm": str(c_closed), "sympy": str(c_value),
               "note": "dh/dk = j kappa sigma3 and sigma3 = +1 on the zero mode; c > 0 (positive integrand); "
                       "+ck for j = +1 (Rust label s = -1), -ck for j = -1; at H = 2M the closed form is "
                       "the limit c = e^{-a4} 2M L/(1 - e^{-2ML})"})
    rec.measure("zeroModeSplittingSympy", c_value)
    # rotational symmetry: R = c + s gamma^1 gamma^2 rotates gamma^1 into the (1,2) plane and commutes
    # with gamma^0, gamma^4, B, C
    G = sympy_gammas(alg)
    cth, sth = sp.symbols("c_half s_half", real=True)
    X = G[1] * G[2]
    R = cth * sp.eye(16) + sth * X
    Rinv = cth * sp.eye(16) - sth * X
    conj1 = sp.expand(R * G[1] * Rinv)
    rot = sp.expand((cth ** 2 - sth ** 2) * G[1] + 2 * cth * sth * G[2])
    rot_minus = sp.expand((cth ** 2 - sth ** 2) * G[1] - 2 * cth * sth * G[2])
    sign = "+" if sp.simplify(conj1 - rot) == sp.zeros(16) else ("-" if sp.simplify(conj1 - rot_minus) == sp.zeros(16) else "none")
    RB = mat_to_sympy(alg.B)
    RC = mat_to_sympy(alg.C)
    commutes = all(sp.expand(R * M - M * R) == sp.zeros(16) for M in (G[0], G[4], RB, RC))
    unit = sp.simplify(sp.expand(R * Rinv) - (cth ** 2 + sth ** 2) * sp.eye(16)) == sp.zeros(16)
    rec.check("rotationalSymmetry", sign != "none" and commutes and unit,
              {"R": "cos(theta/2) + sin(theta/2) gamma^1 gamma^2 ((gamma^1 gamma^2)^2 = -1)",
               "R gamma^1 R^-1": "cos(theta) gamma^1 %s sin(theta) gamma^2" % sign,
               "commutesWith": "gamma^0, gamma^4, B, C (hence with A0, A4, the parity projectors and the theta = 0 bag)",
               "consequence": "the spectrum depends on |k| only; the chiral-bag condition theta != 0 rotates with k"})
    return N


# CHUNK-4C-END

# ---------------------------------------------------------------------------
# 5. KS_boundary: y-current, parity conditions, bag family, symmetries
# ---------------------------------------------------------------------------

def check_boundary(alg, red):
    rec = Recorder("boundary")
    g = alg.gamma
    G = sympy_gammas(alg)
    # y-current J^y = -i Psibar gamma^y Psi = -i Psi^dagger C gamma^0 Psi -> u^dagger B(-i C gamma^0) u
    current16 = mat_mul(alg.B, mat_scale(mat_mul(alg.C, g[0]), CQ(0, -1)))
    rec.check("currentMatrix", mat_eq(current16, alg.A4) and mat_eq(mat_dagger(alg.A4), alg.A4)
              and all(v.im == 0 for row in alg.A4 for v in row)
              and mat_eq(alg.A4, mat_scale(mat_mul(g[4], g[0]), -1)),
              "B(-i C gamma^0) = gamma^0 gamma^4 = A4 = -gamma^4 gamma^0: real symmetric (B absorbed, "
              "STAGE4_SPEC section 4 corrected by errata E4.5)")
    A0s, A1s, A4s = mat_to_sympy(alg.A0), mat_to_sympy(alg.A1), mat_to_sympy(alg.A4)
    N16 = MM * A0s - sp.I * KAPPA_Y * KK * A1s + sp.I * (EPS - VV) * A4s
    N16dag = N16.H
    rec.check("currentConservedAlongY", sp.expand(N16dag * A4s + A4s * N16) == sp.zeros(16),
              "N^dagger A4 + A4 N = 0 for real M_eff, kappa, k, eps, v_v: d/dy (chi^dagger A4 chi) = 0")
    rec.check("hilbertNormNotConservedAlongY",
              sp.expand(N16dag + N16 - (2 * MM * A0s - 2 * sp.I * KAPPA_Y * KK * A1s)) == sp.zeros(16)
              and sp.expand(N16dag + N16) != sp.zeros(16),
              "N^dagger + N = 2 M_eff A0 - 2 i kappa k A1 != 0: chi^dagger chi is not conserved in y")
    N2 = block_ode_matrix()
    rec.check("currentBlockForm", sp.expand(N2.H * SIG1 + SIG1 * N2) == sp.zeros(2)
              and all(mat_eq(red.block_of(alg.A4, b), mat_scale(PAULI["s1"], b["j"])) for b in red.blocks),
              "A4 = j sigma1: J^y_mode = j (chi_1^* chi_2 + chi_2^* chi_1) e^{-6Hy}/l^3")
    # parity conditions Psi(-y) = +- gamma^0 Psi(y): (1 -+ gamma^0) chi(0) = 0
    even = sp.Rational(1, 2) * (I2 - SIG3)
    odd = sp.Rational(1, 2) * (I2 + SIG3)
    rec.check("parityProjectorsBlockForm", even == sp.Matrix([[0, 0], [0, 1]]) and odd == sp.Matrix([[1, 0], [0, 0]])
              and all(mat_eq(red.block_of(alg.A0, b), PAULI["s3"]) for b in red.blocks),
              {"even (+gamma^0)": "chi_2(0) = 0", "odd (-gamma^0)": "chi_1(0) = 0",
               "projector": "P chi(0) = 0 with P = (1 -+ sigma3)/2"})
    c1, c2 = sp.symbols("c1 c2")
    cur = lambda chi: sp.expand((chi.H * SIG1 * chi)[0])
    rec.check("parityKillsCurrent", cur(sp.Matrix([c1, 0])) == 0 and cur(sp.Matrix([0, c2])) == 0,
              "chi^dagger sigma1 chi = 2 Re(chi_1^* chi_2) vanishes when either component vanishes")
    # chiral-bag family at the tip
    th = sp.Symbol("theta", real=True)
    Q = sp.cos(th) * SIG3 + sp.sin(th) * SIG2
    qv = sp.Matrix([sp.cos(th / 2), sp.I * sp.sin(th / 2)])
    a = sp.Symbol("a")
    bag_ok = (sp.simplify(Q * Q - I2) == sp.zeros(2) and sp.simplify(Q.H - Q) == sp.zeros(2)
              and sp.simplify(Q * SIG1 + SIG1 * Q) == sp.zeros(2)
              and sp.simplify(Q * qv - qv) == sp.zeros(2, 1)
              and sp.simplify(cur(a * qv).subs(sp.conjugate(a), sp.Symbol("abar"))) == 0)
    rec.check("bagFamily", bag_ok,
              {"family": "(1 - Q(theta)) chi(-L) = 0, Q = cos(theta) sigma3 + sin(theta) sigma2, Q^2 = 1, {Q, sigma1} = 0",
               "eigenvector": "chi(-L) ~ (cos(theta/2), i sin(theta/2))", "current": "chi^dagger sigma1 chi = 0"})
    rec.check("bagThetaZeroIsEvenParity", Q.subs(th, 0) == SIG3,
              "theta = 0: chi_2(-L) = 0, the even-parity condition at the tip (admits the k = 0 zero mode e^{My})")
    Q16 = sp.cos(th) * G[0] + sp.I * sp.sin(th) * G[0] * G[1]
    q16_ok = (sp.simplify(Q16 * Q16 - sp.eye(16)) == sp.zeros(16) and sp.simplify(Q16.H - Q16) == sp.zeros(16)
              and sp.simplify(Q16 * A4s + A4s * Q16) == sp.zeros(16))
    q16_blocks = all(sp.simplify(mat_to_sympy(red.block_of(alg.A0, b)) * sp.cos(th)
                                 + sp.I * sp.sin(th) * mat_to_sympy(red.block_of(alg.A1, b)) - Q) == sp.zeros(2)
                     for b in red.blocks)
    rec.check("bagIn16", q16_ok and q16_blocks,
              "Q(theta) = cos(theta) gamma^0 + i sin(theta) gamma^0 gamma^1 (chiral-bag family), Hermitian, "
              "squares to 1, anticommutes with A4; block form Q")
    # general lemma: Q chi = chi with {Q, A4} = 0 kills the current (also for the parity projectors)
    x = sp.Matrix(sp.symbols("x0:16"))
    xbar = sp.Matrix(sp.symbols("xb0:16"))
    def form(Mx):
        return sp.expand((xbar.T * Mx * x)[0])
    # chi^+ A4 chi = chi^+ A4 Q chi = -chi^+ Q A4 chi = -(Q chi)^+ A4 chi = -chi^+ A4 chi: the algebraic content is
    # the identity chi^+ (A4 Q + Q A4) chi = 0; also checked on the eigenvector family chi = (1 + Q) w
    cs, sn = sp.symbols("c_theta s_theta", real=True)
    Qcs = cs * G[0] + sp.I * sn * G[0] * G[1]
    lemma = sp.expand(form(A4s * Qcs) + form(Qcs * A4s)) == 0
    w = sp.Matrix(sp.symbols("w0:16"))
    wbar = sp.Matrix(sp.symbols("wb0:16"))
    v = (sp.eye(16) + Qcs) * w
    vbar = (sp.eye(16) + Qcs.T) * wbar          # row vector v^dagger = w^dagger (1 + Q), Q Hermitian
    on_eigenvectors = sp.expand(sp.expand((vbar.T * A4s * v)[0]).subs(sn ** 2, 1 - cs ** 2)) == 0
    lemma = lemma and on_eigenvectors
    rec.check("currentKilledByAnticommutingProjector", lemma,
              "for Q chi = chi and Q Hermitian with {Q, A4} = 0: chi^dagger A4 chi = chi^dagger A4 Q chi "
              "= -chi^dagger Q A4 chi = -chi^dagger A4 chi = 0")
    # self-adjointness: boundary term of <phi|h chi> - <h phi|chi>
    f1, f2, h1, h2 = [sp.Function(n)(Y) for n in ("f1", "f2", "h1", "h2")]
    phi = sp.Matrix([f1, f2])
    chi = sp.Matrix([h1, h2])
    hphi = block_hamiltonian_apply(phi, sp.diff(phi, Y))
    hchi = block_hamiltonian_apply(chi, sp.diff(chi, Y))
    integrand = sp.expand((phi.H * hchi)[0] - (hphi.H * chi)[0])
    total_derivative = sp.expand(-sp.I * JSYM * sp.diff((phi.H * SIG1 * chi)[0], Y))
    rec.check("selfAdjointBoundaryTerm", sp.simplify(integrand - total_derivative) == 0,
              "phi^dagger (h chi) - (h phi)^dagger chi = -i j d/dy (phi^dagger sigma1 chi): the boundary term "
              "vanishes on any pair of current-killing conditions, so h is self-adjoint, eps real, eigenfunctions "
              "orthogonal in the flat y-measure")
    # tip asymptotics: when -kappa k sigma2 dominates, chi' = -kappa k sigma2 chi
    ssym = sp.Symbol("s", real=True)
    kpos = sp.Symbol("k", positive=True)
    vs = sp.Matrix([1, sp.I * ssym])            # sigma2 v = s v for s = +-1
    amp = sp.exp(ssym * kpos * sp.exp(-H * Y - A4C) / H)
    sol = amp * vs
    ode_ok = all(sp.simplify((sp.diff(sol, Y) + sp.exp(-H * Y - A4C) * kpos * SIG2 * sol).subs(ssym, sv)) == sp.zeros(2, 1)
                 for sv in (1, -1))
    decays = sp.limit(amp.subs({ssym: -1, H: 1, A4C: 0, kpos: 1}), Y, -sp.oo) == 0
    grows = sp.limit(amp.subs({ssym: 1, H: 1, A4C: 0, kpos: 1}), Y, -sp.oo) == sp.oo
    rec.check("tipAsymptotics", ode_ok and decays and grows
              and sp.simplify(Q.subs(th, -sp.pi / 2) + SIG2) == sp.zeros(2)
              and sp.simplify(SIG2 * sp.Matrix([1, -sp.I]) + sp.Matrix([1, -sp.I])) == sp.zeros(2, 1),
              "chi = exp(s k e^{-Hy-a4}/H) (1, i s): decays toward the tip iff s = -sgn(k); "
              "theta = -pi/2 (k > 0) selects sigma2 = -1, chi(-L) ~ (1, -i); theta = +pi/2 for k < 0")
    # P_A: chi(y) -> gamma^0 chi(-y) maps mass M(y) to -M(-y); P_B: i gamma^0 gamma^8 keeps M(-y)
    Mf = sp.Function("Mf")(Y)
    kf = sp.Function("kf")(Y)
    Nf = Mf * A0s - sp.I * kf * KK * A1s + sp.I * (EPS - VV) * A4s
    PA = G[0]
    PB = sp.I * G[0] * mat_to_sympy(alg.gamma8)
    # for chi~(y) = P chi(-y): chi~' = -P N(-y) P^-1 chi~ ; compare with N built from transformed functions
    imageA = sp.expand(-PA * Nf * PA)
    targetA = sp.expand(-Mf * A0s - sp.I * kf * KK * A1s + sp.I * (EPS - VV) * A4s)
    rec.check("parityA_symmetryIffMassOdd", sp.expand(imageA - targetA) == sp.zeros(16),
              "-gamma^0 N(M, kappa) gamma^0 = N(-M, kappa): with kappa even, P_A maps solutions with M(y) to "
              "solutions with -M(-y); a symmetry iff M_eff is odd (the +-M mirror pair, CONTRACT errata E2)")
    imageB = sp.expand(-PB * Nf * PB)
    rec.check("parityB_symmetryForEvenMass", sp.expand(imageB - Nf) == sp.zeros(16)
              and sp.expand(PB * PB - sp.eye(16)) == sp.zeros(16) and sp.expand(PB.H - PB) == sp.zeros(16),
              "P_B = i gamma^0 gamma^8 (Hermitian, squares to 1): -P_B N(M, kappa) P_B = N(M, kappa), the symmetry "
              "for an even mass function")
    PB16 = mat_scale(mat_mul(alg.gamma[0], alg.gamma8), CQ(0, 1))
    pairs_ok = True
    pair_forms = []
    for b in red.blocks:
        partner = red.blocks[[x for x in range(8) if BLOCK_LABELS[x] == (-b["j"], b["s2"], b["s3"])][0]]
        cross = red.cross_block(PB16, b, partner)
        diag = red.block_of(PB16, b)
        pairs_ok &= mat_is_zero(diag) and (mat_eq(cross, PAULI["s1"]) or mat_eq(cross, mat_scale(PAULI["s1"], -1)))
        pair_forms.append("%d->%d: %ssigma1" % (b["index"], partner["index"], "+" if mat_eq(cross, PAULI["s1"]) else "-"))
    rec.check("parityB_couplesJBlocks", pairs_ok and mat_is_zero(mat_anticommutator(PB16, alg.J))
              and mat_is_zero(mat_anticommutator(PB16, alg.A4)),
              {"anticommutesWithJ": True, "anticommutesWithA4": True, "blockPairs": pair_forms,
               "consequence": "(1 -+ P_B) chi(0) = 0 couples block (j,s2,s3) with (-j,s2,s3): a 4x4 problem; "
                              "the KS problem uses the block-diagonal P_A conditions (errata E4.6)"})
    par_ok = (sp.expand(form(A4s * PA) + form(PA * A4s)) == 0
              and mat_is_zero(mat_anticommutator(alg.A0, alg.A4)))
    rec.check("parityOperatorsKillCurrent", par_ok, "gamma^0 and P_B anticommute with A4")
    dens = {"n": mat_mul(alg.B, alg.B), "s": alg.BC, "t": mat_scale(mat_mul(g[4], g[1]), -1), "c": alg.A4}
    table = {}
    for name, M in dens.items():
        pa = mat_mul(mat_mul(alg.gamma[0], M), alg.gamma[0])
        pb = mat_mul(mat_mul(PB16, M), PB16)
        table[name] = {"P_A": "even" if mat_eq(pa, M) else ("odd" if mat_eq(pa, mat_scale(M, -1)) else "mixed"),
                       "P_B": "even" if mat_eq(pb, M) else ("odd" if mat_eq(pb, mat_scale(M, -1)) else "mixed")}
    rec.check("densityParities", table == {"n": {"P_A": "even", "P_B": "even"}, "s": {"P_A": "odd", "P_B": "even"},
                                           "t": {"P_A": "even", "P_B": "even"}, "c": {"P_A": "odd", "P_B": "odd"}},
              table)
    rec.measure("used", "the KS problem uses the block-level conditions chi_2(0) = 0 / chi_1(0) = 0 (both parities "
                        "as boundary conditions, not as symmetries) and the bag family at y = -L")
    return rec


# CHUNK-5-END

# ---------------------------------------------------------------------------
# 6. KS_exchange (a): Hartree-Fock formula on an explicit Fock space, filled
#    shell, the exchange kernel, angular average, block form, closed form
# ---------------------------------------------------------------------------

class FockSpace:
    """M fermionic modes on 2^M states (Jordan-Wigner), exact CQ matrices."""

    def __init__(self, modes):
        self.modes = modes
        dim = 2 ** modes
        self.dim = dim
        self.b = []
        for n in range(modes):
            mat = mat_zero(dim)
            for state in range(dim):
                if (state >> n) & 1:
                    sign = (-1) ** sum((state >> m) & 1 for m in range(n))
                    mat[state ^ (1 << n)][state] = CQ(sign)
            self.b.append(mat)
        self.bdag = [mat_dagger(m) for m in self.b]

    def car_ok(self):
        for n in range(self.modes):
            for m in range(self.modes):
                expected = mat_eye(self.dim) if n == m else mat_zero(self.dim)
                if not mat_eq(mat_anticommutator(self.b[n], self.bdag[m]), expected):
                    return False
                if not mat_is_zero(mat_anticommutator(self.b[n], self.b[m])):
                    return False
        return True

    def slater(self, occupied):
        state = 0
        for n in occupied:
            state |= 1 << n
        vec = [CQ_ZERO] * self.dim
        vec[state] = CQ_ONE
        return vec

    def expectation(self, op, vec):
        opv = [sum((op[i][l] * vec[l] for l in range(self.dim)), CQ_ZERO) for i in range(self.dim)]
        return vec_dot(vec, opv)


def hartree_fock_wick(alg, red):
    """Verify E_HF on a 4-mode Fock space built from B = +1 block basis vectors.
    Psi_a = sum_n u_{n,a} b_n with u_n = v_n / sqrt 8 orthonormal B-eigenvectors (B u = u),
    S = Psi^dagger C Psi = sum_{nm} c_{nm} b_n^dagger b_m, c = u^dagger C u.
    Normal ordering: :b_n^+ b_m b_p^+ b_q: = -b_n^+ b_p^+ b_m b_q.
    Claim: <Phi|:S^2:|Phi> = Tr(BC rho)^2 - Tr(BC rho BC rho), rho = sum_occ u u^dagger."""
    plus_blocks = [b for b in red.blocks if b["j"] * b["s2"] == 1]        # B = +1 blocks: 0, 1, 6, 7
    modes = [plus_blocks[0]["vPlus"], plus_blocks[0]["vMinus"], plus_blocks[1]["vPlus"], plus_blocks[2]["vMinus"]]
    # orthonormality and B u = u (unnormalised: v^dagger v = 8)
    ortho = all((vec_dot(modes[a], modes[b]) == (CQ(8) if a == b else CQ_ZERO)) for a in range(4) for b in range(4))
    b_plus = all(all(sum((alg.B[i][l] * v[l] for l in range(16)), CQ_ZERO) == v[i] for i in range(16)) for v in modes)
    fock = FockSpace(4)
    car = fock.car_ok()
    eighth = Fraction(1, 8)
    def bilinear(X):
        return [[vec_dot(modes[n], [sum((X[i][l] * modes[m][l] for l in range(16)), CQ_ZERO) for i in range(16)]) * eighth
                 for m in range(4)] for n in range(4)]
    c = bilinear(alg.C)
    dim = fock.dim
    normal_s2 = mat_zero(dim)
    for n in range(4):
        for m in range(4):
            for p in range(4):
                for q in range(4):
                    coefficient = c[n][m] * c[p][q]
                    if coefficient.is_zero():
                        continue
                    term = mat_mul(mat_mul(fock.bdag[n], fock.bdag[p]), mat_mul(fock.b[m], fock.b[q]))
                    normal_s2 = mat_add(normal_s2, mat_scale(term, -coefficient))
    s_op = mat_zero(dim)
    for n in range(4):
        for m in range(4):
            if not c[n][m].is_zero():
                s_op = mat_add(s_op, mat_scale(mat_mul(fock.bdag[n], fock.b[m]), c[n][m]))
    results = []
    all_ok = ortho and b_plus and car
    for occupied in ((0,), (1,), (0, 1), (0, 2), (1, 3), (0, 1, 2), (0, 1, 3), (0, 1, 2, 3)):
        vec = fock.slater(occupied)
        rho = mat_zero(16)
        for n in occupied:
            for i in range(16):
                for l in range(16):
                    rho[i][l] = rho[i][l] + modes[n][i] * modes[n][l].conj() * eighth
        bcr = mat_mul(alg.BC, rho)
        hartree = mat_trace(bcr) * mat_trace(bcr)
        exchange = mat_trace(mat_mul(bcr, bcr))
        direct = fock.expectation(normal_s2, vec)
        s_mean = fock.expectation(s_op, vec)
        ok = (direct == hartree - exchange) and (s_mean == mat_trace(bcr))
        all_ok &= ok
        results.append({"occupied": list(occupied), "<:S^2:>": direct.to_pair(), "Tr(BC rho)^2": hartree.to_pair(),
                        "Tr(BC rho BC rho)": exchange.to_pair(), "ok": ok})
    return all_ok, {"modes": "v+, v- of block 0, v+ of block 1, v- of block 6 (B = +1, orthonormal after /sqrt 8)",
                    "carVerified": car, "orthonormal": ortho, "BeigenvaluePlusOne": b_plus, "cases": results}


def exchange_kernel_table(alg):
    """T_ab = Tr(X_a Gamma X_b Gamma) with Gamma = -i gamma^4, X_0 = Gamma (mass), X_j = i Gamma gamma^j
    X_j = -i Gamma gamma^j (momentum p_j, j = 0..3), so that h_p = m X_0 + sum_j p_j X_j."""
    g = alg.gamma
    Gam = alg.BC                                        # -i gamma^4
    X = [Gam] + [mat_scale(mat_mul(Gam, g[j]), CQ(0, -1)) for j in range(4)]   # -gamma^4 gamma^j = -i Gamma gamma^j
    table = [[mat_trace(mat_mul(mat_mul(X[a], Gam), mat_mul(X[b], Gam))) for b in range(5)] for a in range(5)]
    h_form = all(mat_eq(mat_scale(mat_mul(g[4], g[j]), -1), X[j + 1]) for j in range(4)) \
        and mat_eq(mat_scale(g[4], CQ(0, -1)), X[0])
    return table, h_form, X


def check_exchange_a(alg, red, rec):
    g = alg.gamma
    ok, detail = hartree_fock_wick(alg, red)
    rec.check("wickTheoremHF", ok, detail)
    rec.check("hartreeFockFormula", ok,
              "E_HF = (lambda/2)[Tr(BC rho)^2 - Tr(BC rho BC rho)] per unit volume, rho = sum_n f_n u_n u_n^dagger, "
              "with the expectation rule <Psi^dagger X Psi> = Tr(B X rho) (two-point function G = rho B)")
    # filled shell: 8 positive-energy states at one momentum p (exact Pythagorean point m = 3, k = 4, E = 5)
    m0, k0, e0 = 3, 4, 5
    h = mat_add(mat_scale(g[4], CQ(0, -m0)), mat_scale(mat_mul(g[4], g[1]), -k0))
    P = mat_scale(mat_add(mat_scale(alg.I16, e0), h), Fraction(1, 2 * e0))
    proj_ok = mat_eq(mat_mul(P, P), P) and mat_rank(P) == 8 and mat_eq(mat_mul(h, P), mat_scale(P, e0))
    S1 = mat_trace(mat_mul(alg.BC, P))
    ex1 = mat_trace(mat_mul(mat_mul(alg.BC, P), mat_mul(alg.BC, P)))
    rec.check("filledShellProjector", proj_ok and mat_eq(mat_dagger(h), h),
              "P_+(k) = (1 + h_k/E)/2, h_k = -i m gamma^4 - k gamma^4 gamma^1 Hermitian, rank 8, h P = E P")
    rec.check("filledShellScalarDensity", S1 == CQ(Fraction(8 * m0, e0)), {"Tr(BC P_+)": S1.to_pair(), "8m/E": "24/5"})
    rec.check("filledShellOneEighth", ex1 == S1 * S1 * Fraction(1, 8) and ex1 == CQ(Fraction(8 * m0 * m0, e0 * e0)),
              {"Tr(BC P_+ BC P_+)": ex1.to_pair(), "ratio": _frac_str(ex1.re / (S1.re * S1.re)),
               "statement": "E_x = -(lambda/2) S^2/8 = -E_H/8 for one filled shell (8 states at one k)"})
    table, h_form, X = exchange_kernel_table(alg)
    # expected: T_00 = 16, T_0j = T_j0 = 0, T_jl = -16 delta_jl
    tab_ok = (table[0][0] == CQ(16) and all(table[0][j].is_zero() and table[j][0].is_zero() for j in range(1, 5))
              and all(table[a][b] == (CQ(-16) if a == b else CQ_ZERO) for a in range(1, 5) for b in range(1, 5)))
    rec.check("kernelTraceTable", tab_ok and h_form,
              {"Gamma": "-i gamma^4 = BC, Gamma^2 = 1", "h_p": "m Gamma - sum_j p_j (i Gamma gamma^j) = -i m gamma^4 - gamma^4 gamma^j p_j",
               "Tr(X_a Gamma X_b Gamma)": [[v.to_pair() for v in row] for row in table]})
    # kernel: 4 E_p E_q Tr(P_a(p) Gamma P_b(q) Gamma) = Tr((E_p + a h_p) Gamma (E_q + b h_q) Gamma)
    #       = 16 E_p E_q + a b Tr(h_p Gamma h_q Gamma) = 16 [E_p E_q + a b (m^2 - p.q)]
    m, Ep, Eq = sp.symbols("m E_p E_q", positive=True)
    pv = sp.symbols("p0:4", real=True)
    qv = sp.symbols("q0:4", real=True)
    T = [[table[a][b].to_sympy() for b in range(5)] for a in range(5)]
    hp = [m] + list(pv)
    hq = [m] + list(qv)
    tr_hh = sp.expand(sum(hp[a] * hq[b] * T[a][b] for a in range(5) for b in range(5)))
    tr_gamma_h = sp.expand(sum(hp[a] * mat_trace(X[a]).to_sympy() for a in range(5)))
    tr_gamma_gamma = mat_trace(mat_mul(alg.BC, alg.BC)).to_sympy()
    kernels = {}
    kernel_ok = True
    for a in (1, -1):
        for b in (1, -1):
            value = sp.expand((tr_gamma_gamma * Ep * Eq + a * Eq * tr_gamma_h + b * Ep * tr_gamma_h
                               + a * b * tr_hh) / (4 * Ep * Eq))
            expected = 4 * (1 + a * b * (m ** 2 - sum(pv[j] * qv[j] for j in range(4))) / (Ep * Eq))
            kernel_ok &= sp.simplify(value - expected) == 0
            kernels["K_%s%s" % ("+" if a == 1 else "-", "+" if b == 1 else "-")] = str(expected)
    rec.check("kernelClosedForm", kernel_ok and tr_gamma_h == 0 and tr_gamma_gamma == 16,
              {"kernel": "Tr(P_a(p) BC P_b(q) BC) = 4[1 + a b (m^2 - p.q)/(E_p E_q)]",
               "forms": kernels, "Tr(Gamma h)": str(tr_gamma_h), "Tr(Gamma Gamma)": str(tr_gamma_gamma),
               "note": "the spin-summed |ubar_p u_q|^2 of the spec with ubar u -> u^dagger BC u"})
    # angular average of p.q vanishes: S^3 (d = 4) and S^2 (d = 3)
    th = sp.Symbol("theta", positive=True)
    ang4 = sp.integrate(sp.sin(th) ** 2 * sp.cos(th), (th, 0, sp.pi))
    ang3 = sp.integrate(sp.sin(th) * sp.cos(th), (th, 0, sp.pi))
    norm4 = sp.integrate(sp.sin(th) ** 2, (th, 0, sp.pi))
    rec.check("angularAverageOfPdotQVanishes", ang4 == 0 and ang3 == 0 and norm4 == sp.pi / 2,
              {"int sin^2 cos (S^3)": str(ang4), "int sin cos (S^2)": str(ang3), "int sin^2": str(norm4)})
    # block form of the Fock term with rho_beta = (n + s sigma2 + t sigma3 + c sigma1)/2 and BC = j sigma2
    nb, sb, tb, cb = sp.symbols("n_b s_b t_b c_b", real=True)
    rho_b = (nb * I2 + sb * SIG2 + tb * SIG3 + cb * SIG1) / 2
    fock_b = sp.expand((JSYM * SIG2 * rho_b * JSYM * SIG2 * rho_b).trace().subs(JSYM ** 2, 1))
    rec.check("blockFormOfFockTerm", sp.simplify(fock_b - (nb ** 2 + sb ** 2 - tb ** 2 - cb ** 2) / 2) == 0,
              "Tr(BC rho BC rho) = sum_beta (n_b^2 + s_b^2 - t_b^2 - c_b^2)/2, so E_x = -(lambda/4) sum_beta (...) "
              "(errata E4.7); for the uniform gas with n_b = n/8, s_b = S/8, t_b = c_b = 0 this is (n^2 + S^2)/16")
    # closed form from the kernel: with I0+- = int f_+-, I1+- = int f_+- m/E (8 states included, isotropic)
    i0p, i0m, i1p, i1m = sp.symbols("I0p I0m I1p I1m", real=True)
    # Tr(BC rho BC rho) = (1/64)[ (f+f+ + f-f-) K++_avg - 2 f+f- K+-_avg ] with K_avg = 4(1 +- m^2/EE'),
    # the 1/8 per Tr normalisation: n = 8 (I0+ - I0-), S = 8 (I1+ + I1-) with I's per 8 states
    trace_gas = sp.Rational(1, 64) * 4 * ((i0p ** 2 + i1p ** 2) + (i0m ** 2 + i1m ** 2) - 2 * (i0p * i0m - i1p * i1m))
    n_gas = i0p - i0m
    s_gas = i1p + i1m
    rec.check("uniformGasClosedForm", sp.simplify(trace_gas - (n_gas ** 2 + s_gas ** 2) / 16) == 0,
              {"e_x": "-(lambda/2) Tr(BC rho BC rho) = -(lambda/32)(n^2 + S^2) for every T and every d",
               "n": "8 int (f_+ - f_-)", "S": "8 int (m/E)(f_+ + f_-)",
               "decomposition": "e_x^(v) = -(lambda/32) n^2 (number part), e_x^(s) = -(lambda/32) S^2 (scalar part)"})
    # antiparticle convention: Tr(BC P_-) = -8m/E and Tr(P_-) = 8 at the exact point
    Pm = mat_scale(mat_sub(mat_scale(alg.I16, e0), h), Fraction(1, 2 * e0))
    rec.check("antiparticleConvention", mat_trace(mat_mul(alg.BC, Pm)) == CQ(Fraction(-8 * m0, e0))
              and mat_trace(Pm) == CQ(8) and mat_trace(mat_mul(alg.BC, P)) == CQ(Fraction(8 * m0, e0)),
              "rho = int [f_+ P_+ - f_- P_-] (normal ordering: holes of the sea): antiparticles carry negative "
              "number density (Tr P_- = 8 with weight -f_-) and positive scalar density (Tr BC P_- = -8m/E)")
    return table


# CHUNK-6A-END

# ---------------------------------------------------------------------------
# 6. KS_exchange (b): uniform-gas thermodynamics, T = 0 closed forms, double
#    quadrature of the exchange energy (mpmath), LDA potentials
# ---------------------------------------------------------------------------

_GL_CACHE = {}


def gauss_legendre_nodes(n):
    """Nodes and weights on [-1, 1] as mpmath mpf (computed once at 30 digits)."""
    if n in _GL_CACHE:
        return _GL_CACHE[n]
    with mpmath.workdps(30):
        xs, ws = [], []
        for i in range(n):
            z = mpmath.cos(mpmath.pi * (i + mpmath.mpf(3) / 4) / (n + mpmath.mpf(1) / 2))
            for _ in range(100):
                p1, p2 = mpmath.mpf(1), mpmath.mpf(0)
                for j in range(n):
                    p3 = p2
                    p2 = p1
                    p1 = ((2 * j + 1) * z * p2 - j * p3) / (j + 1)
                pp = n * (z * p1 - p2) / (z * z - 1)
                dz = p1 / pp
                z = z - dz
                if abs(dz) < mpmath.mpf(10) ** -28:
                    break
            xs.append(z)
            ws.append(2 / ((1 - z * z) * pp * pp))
    _GL_CACHE[n] = (xs, ws)
    return xs, ws


def angular_rule(d, n):
    """Normalised angular average over the angle between p and q in d spatial
    dimensions: d = 4 weight sin^2 (Gauss-Chebyshev of the second kind),
    d = 3 weight sin (Gauss-Legendre); nodes are cos(theta)."""
    if d == 4:
        xs = [mpmath.cos(mpmath.pi * k / (n + 1)) for k in range(1, n + 1)]
        ws = [mpmath.pi / (n + 1) * mpmath.sin(mpmath.pi * k / (n + 1)) ** 2 for k in range(1, n + 1)]
        total = mpmath.pi / 2
    elif d == 3:
        xs, ws = gauss_legendre_nodes(n)
        total = mpmath.mpf(2)
    else:
        raise ValueError("d must be 3 or 4")
    return [x for x in xs], [w / total for w in ws]


def measure_prefactor(d):
    """8 int d^dp/(2 pi)^d = prefactor * int p^{d-1} dp: 1/pi^2 (d = 4), 4/pi^2 (d = 3)."""
    return {4: 1 / mpmath.pi ** 2, 3: 4 / mpmath.pi ** 2}[d]


def fermi(x):
    if x > 0:
        e = mpmath.exp(-x)
        return e / (1 + e)
    return 1 / (1 + mpmath.exp(x))


def gas_panels(m, mu, T, ctx_float):
    """Break points of the radial integration adapted to the Fermi edge."""
    if T <= 0:
        kf = math.sqrt(mu * mu - m * m) if mu > m else 0.0
        return [0.0, kf], True
    emax = max(abs(mu), 0.0) + 40.0 * T
    pmax = math.sqrt(max(emax * emax - m * m, 0.0)) + 1.0
    edges = {0.0, pmax}
    if mu > m:
        pmu = math.sqrt(mu * mu - m * m)
        delta = T * mu / pmu if pmu > 0 else T
        for c in (-12.0, -3.0, 3.0, 12.0):
            e = pmu + c * delta
            if 0.0 < e < pmax:
                edges.add(e)
    else:
        for c in (0.5, 2.0, 8.0):
            e = c * T
            if 0.0 < e < pmax:
                edges.add(e)
    return sorted(edges), False


class GasRule:
    """Radial quadrature nodes (mpf) with occupations for one (m, mu, T, d)."""

    def __init__(self, m, mu, T, d, nodes_per_panel):
        self.m, self.mu, self.T, self.d = mpmath.mpf(m), mpmath.mpf(mu), mpmath.mpf(T), d
        edges, step = gas_panels(float(m), float(mu), float(T), True)
        xs, ws = gauss_legendre_nodes(nodes_per_panel)
        self.p, self.w, self.E, self.fp, self.fm = [], [], [], [], []
        pref = measure_prefactor(d)
        for a, b in zip(edges[:-1], edges[1:]):
            a, b = mpmath.mpf(a), mpmath.mpf(b)
            if b - a <= 0:
                continue
            for x, wgt in zip(xs, ws):
                p = (b - a) / 2 * x + (b + a) / 2
                dp = (b - a) / 2 * wgt
                E = mpmath.sqrt(self.m ** 2 + p * p)
                if step:
                    fp, fm = mpmath.mpf(1), mpmath.mpf(0)
                else:
                    fp = fermi((E - self.mu) / self.T)
                    fm = fermi((E + self.mu) / self.T)
                self.p.append(p)
                self.w.append(pref * p ** (d - 1) * dp)
                self.E.append(E)
                self.fp.append(fp)
                self.fm.append(fm)

    def moments(self):
        """n, S, e_kin, entropy density, dn/dmu, dS/dmu (8 states included)."""
        n = S = ek = ent = dn = dS = mpmath.mpf(0)
        for p, w, E, fp, fm in zip(self.p, self.w, self.E, self.fp, self.fm):
            n += w * (fp - fm)
            S += w * self.m / E * (fp + fm)
            ek += w * E * (fp + fm)
            if self.T > 0:
                for f in (fp, fm):
                    if 0 < f < 1:
                        ent -= w * (f * mpmath.log(f) + (1 - f) * mpmath.log(1 - f))
                dfp = fp * (1 - fp) / self.T
                dfm = fm * (1 - fm) / self.T
                dn += w * (dfp + dfm)
                dS += w * self.m / E * (dfp - dfm)
        return {"n": n, "S": S, "eKin": ek, "entropy": ent, "dn_dmu": dn, "dS_dmu": dS}

    def exchange_trace(self, angular_nodes=4):
        """Tr(BC rho BC rho) by the double radial quadrature with the raw kernel
        K_ab = 4[1 + ab (m^2 - p q cos theta)/(E E')] and an explicit angular rule."""
        xs, ws = angular_rule(self.d, angular_nodes)
        m2 = self.m ** 2
        total = mpmath.mpf(0)
        N = len(self.p)
        for i in range(N):
            wi, Ei, pi_, ai, bi = self.w[i], self.E[i], self.p[i], self.fp[i], self.fm[i]
            if ai == 0 and bi == 0:
                continue
            for j in range(N):
                aj, bj = self.fp[j], self.fm[j]
                if aj == 0 and bj == 0:
                    continue
                pq = pi_ * self.p[j]
                inv = 1 / (Ei * self.E[j])
                acc = mpmath.mpf(0)
                for x, wx in zip(xs, ws):
                    ratio = (m2 - pq * x) * inv
                    kpp = 4 * (1 + ratio)
                    kpm = 4 * (1 - ratio)
                    acc += wx * ((ai * aj + bi * bj) * kpp - 2 * ai * bj * kpm)
                total += wi * self.w[j] * acc
        # the radial weights carry the 8 internal states (n = sum w (f+ - f-)); the kernel already
        # traces over them, so the measure of the double integral is w/8 per momentum
        return total / 64


def gas_mu_of_n(n, T, m, d, nodes_per_panel=32):
    """Chemical potential with density n > 0 (T = 0: closed form; T > 0: bisection)."""
    n = mpmath.mpf(n)
    if T <= 0:
        kf = (4 * mpmath.pi ** 2 * n) ** mpmath.mpf("0.25") if d == 4 else (3 * mpmath.pi ** 2 * n / 4) ** (mpmath.mpf(1) / 3)
        return mpmath.sqrt(m * m + kf * kf)
    lo, hi = mpmath.mpf(0), mpmath.mpf(m) + mpmath.mpf(T)
    while GasRule(m, hi, T, d, nodes_per_panel).moments()["n"] < n:
        hi *= 2
    # n(mu) is smooth and strictly increasing (dn/dmu > 0): safeguarded Newton inside the bracket
    mu = (lo + hi) / 2
    tolerance = mpmath.mpf(10) ** (-(mpmath.mp.dps - 2))
    for _ in range(60):
        mom = GasRule(m, mu, T, d, nodes_per_panel).moments()
        residual = mom["n"] - n
        if residual < 0:
            lo = mu
        else:
            hi = mu
        if abs(residual) <= tolerance * n or hi - lo <= tolerance * max(hi, 1):
            break
        step = residual / mom["dn_dmu"] if mom["dn_dmu"] > 0 else mpmath.mpf(0)
        candidate = mu - step
        if step == 0 or not (lo < candidate < hi):
            candidate = (lo + hi) / 2
        mu = candidate
    return mu


def t0_closed_forms():
    """Sympy derivation of the T = 0 uniform-gas densities in d = 4 and d = 3."""
    p, kf, m = sp.symbols("p k_F m", positive=True)
    ef = sp.sqrt(m ** 2 + kf ** 2)
    out = {}
    for d, pref in ((4, 1 / sp.pi ** 2), (3, 4 / sp.pi ** 2)):
        n = sp.simplify(sp.integrate(pref * p ** (d - 1), (p, 0, kf)))
        S = sp.simplify(sp.integrate(pref * p ** (d - 1) * m / sp.sqrt(m ** 2 + p ** 2), (p, 0, kf)))
        ek = sp.simplify(sp.integrate(pref * p ** (d - 1) * sp.sqrt(m ** 2 + p ** 2), (p, 0, kf)))
        dSdn = sp.simplify(sp.diff(S, kf) / sp.diff(n, kf))
        out[d] = {"n": n, "S": S, "eKin": ek, "dSdn": dSdn, "E_F": ef}
    return out


def check_exchange_b(rec, quick=False):
    forms = t0_closed_forms()
    m, kf = sp.symbols("m k_F", positive=True)
    ef = sp.sqrt(m ** 2 + kf ** 2)
    f4 = forms[4]
    ok4 = (sp.simplify(f4["n"] - kf ** 4 / (4 * sp.pi ** 2)) == 0
           and sp.simplify(f4["S"] - m / (3 * sp.pi ** 2) * ((kf ** 2 - 2 * m ** 2) * ef + 2 * m ** 3)) == 0
           and sp.simplify(f4["eKin"] - ((3 * kf ** 2 - 2 * m ** 2) * ef ** 3 + 2 * m ** 5) / (15 * sp.pi ** 2)) == 0
           and sp.simplify(f4["dSdn"] - m / ef) == 0)
    rec.check("T0_closedForms_d4", ok4,
              {"n": str(f4["n"]), "S": str(f4["S"]), "eKin": str(f4["eKin"]), "dS/dn": str(f4["dSdn"]),
               "e_x(n,0)": "-(lambda/32)[n^2 + S(k_F(n))^2], k_F = (4 pi^2 n)^{1/4}",
               "v_x_total": "d e_x/dn|_{T=0} = -(lambda/16)[n + S m/E_F]"})
    f3 = forms[3]
    s3_expected = 2 * m / sp.pi ** 2 * (kf * ef - m ** 2 * sp.log((kf + ef) / m))
    s3_diff = (f3["S"] - s3_expected).rewrite(sp.log)
    s3_ok = sp.simplify(s3_diff) == 0 or all(abs(sp.N(s3_diff.subs({m: 1, kf: v}), 40)) < sp.Float(10) ** -35
                                              for v in (sp.Rational(1, 3), 2, 7))
    ok3 = (sp.simplify(f3["n"] - 4 * kf ** 3 / (3 * sp.pi ** 2)) == 0 and s3_ok
           and sp.simplify(f3["dSdn"] - m / ef) == 0)
    rec.check("T0_closedForms_d3", ok3, {"n": str(f3["n"]), "S": str(f3["S"]), "eKin": str(f3["eKin"]),
                                        "dS/dn": str(f3["dSdn"])})
    # rest-gas limit k_F -> 0: S -> n, e_x -> -(lambda/16) n^2 = -e_H/8
    ratio = sp.limit(f4["S"] / f4["n"], kf, 0)
    rec.check("restGasLimit", ratio == 1, "k_F -> 0: S = n, e_x = -(lambda/16) n^2 = -e_H/8 (filled-shell value)")
    # LDA potentials
    n_, S_, lam_ = sp.symbols("n S lambda", real=True)
    ex = -lam_ / 32 * (n_ ** 2 + S_ ** 2)
    Su = sp.Function("S_u")(n_)
    ex_n_only = ex.subs(S_, Su)
    rec.check("ldaPotentials", sp.diff(ex, n_) == -lam_ * n_ / 16 and sp.diff(ex, S_) == -lam_ * S_ / 16
              and sp.simplify(sp.diff(ex_n_only, n_) + lam_ / 16 * (n_ + Su * sp.diff(Su, n_))) == 0,
              {"v_v": "de_x/dn|_S = -(lambda/16) n (potential type, enters as eps -> eps - v_v)",
               "v_s": "de_x/dS|_n = -(lambda/16) S (mass type, enters M_eff = m + lambda S + v_s)",
               "v_x_nOnly": "de_x(n,T)/dn|_T = -(lambda/16)[n + S_u dS_u/dn] (STAGE4_SPEC recommendation KS-V)",
               "used": "KS-VS: M_eff = m + lambda S_p + v_s = m + (15/16) lambda S_p, v_v = -(lambda/16) n_p, the exact "
                       "functional derivative of the LDA functional; KS-V uses the exact Hartree shift and v_x only"})
    rec.check("couplingDimension", (8 - 2 * sp.Rational(7, 2)) == 1 and (8 - 4 * sp.Rational(7, 2)) == -6,
              "[Psi] = 7/2 in 8D, [m] = 1, [lambda] = mass^-6: the contact interaction beyond Hartree-Fock is not "
              "renormalisable; no correlation term; lambda-hat = lambda m^6")
    # double quadrature with mpmath at several (n, T), d = 4 and d = 3
    points = [(4, "0.01", "0"), (4, "1", "0"), (4, "20", "0"), (4, "0.1", "0.1"), (4, "1", "0.3"), (4, "0.5", "1"),
              (4, "0.001", "0.5"), (3, "1", "0"), (3, "0.3", "0.2"), (3, "2", "1")]
    if quick:
        points = [(4, "1", "0"), (4, "1", "0.3"), (3, "0.3", "0.2")]
    spot = []
    all_ok = True
    with mpmath.workdps(20):
        for d, ns, Ts in points:
            n, T = mpmath.mpf(ns), mpmath.mpf(Ts)
            mu = gas_mu_of_n(n, T, 1, d)
            coarse = GasRule(1, mu, T, d, 16)
            fine = GasRule(1, mu, T, d, 32)
            mc, mf = coarse.moments(), fine.moments()
            trc, trf = coarse.exchange_trace(4), fine.exchange_trace(6)
            closed = (mf["n"] ** 2 + mf["S"] ** 2) / 16
            err = abs(trf - trc) + abs(mf["n"] - mc["n"]) * abs(mf["n"]) / 4 + abs(mf["S"] - mc["S"]) * abs(mf["S"]) / 4
            dev = abs(trf - closed)
            tol = max(10 * err, mpmath.mpf(10) ** -12 * closed)
            ok = dev <= tol and abs(mf["n"] - n) <= mpmath.mpf(10) ** -10 * n
            all_ok &= ok
            spot.append({"d": d, "n": float(n), "T": float(T), "mu": float(mu), "S": float(mf["S"]),
                         "Tr_quadrature": mpmath.nstr(trf, 17), "closedForm": mpmath.nstr(closed, 17),
                         "absDeviation": mpmath.nstr(dev, 3), "errorEstimate": mpmath.nstr(err, 3),
                         "e_x_over_lambda": mpmath.nstr(-trf / 2, 17), "ok": ok})
    rec.check("doubleQuadratureMpmath", all_ok,
              {"method": "composite Gauss-Legendre in |p|, |q| (panels around the Fermi edge; 16 vs 32 nodes per "
                         "panel as the error estimate), raw kernel 4[1 + ab (m^2 - pq cos theta)/(EE')] with a 4- resp. "
                         "6-node exact angular rule (sin^2 theta for d = 4, sin theta for d = 3), mpmath 20 digits",
               "points": spot})
    return spot


# CHUNK-6B-END

# ---------------------------------------------------------------------------
# 7. KS_functional: Mermin-Kohn-Sham functional on a discrete model (exact
#    Wirtinger derivatives), stationarity, occupations, energies, identities
# ---------------------------------------------------------------------------

def check_functional():
    rec = Recorder("functional")
    A, NORB = 2, 2                                   # grid points, orbitals (j = +1 and j = -1)
    w = sp.symbols("w0:%d" % A, positive=True)       # flat-measure weights
    ys = sp.symbols("y0:%d" % A, real=True)
    ell, lam, T, mu, mm = sp.symbols("ell lambda T mu m", positive=True)
    f = sp.symbols("f0:%d" % NORB, positive=True)
    jn = (1, -1)
    x = {(n, a, c): sp.Symbol("x_%d_%d_%d" % (n, a, c)) for n in range(NORB) for a in range(A) for c in range(2)}
    xb = {(n, a, c): sp.Symbol("xb_%d_%d_%d" % (n, a, c)) for n in range(NORB) for a in range(A) for c in range(2)}
    def chi(n, a):
        return sp.Matrix([x[(n, a, 0)], x[(n, a, 1)]])
    def chib(n, a):
        return sp.Matrix([[xb[(n, a, 0)], xb[(n, a, 1)]]])      # row vector chi^dagger
    # Hermitian kinetic matrices K_n (4x4 = 2 points x 2 components), K_n = W H0_n so that
    # <chi|h_0|chi>_w = chi^dagger K_n chi
    K = []
    for n in range(NORB):
        entries = {}
        for r in range(4):
            for c in range(4):
                if r < c:
                    entries[(r, c)] = sp.Symbol("kr_%d_%d_%d" % (n, r, c), real=True) + sp.I * sp.Symbol("ki_%d_%d_%d" % (n, r, c), real=True)
                elif r == c:
                    entries[(r, c)] = sp.Symbol("kr_%d_%d_%d" % (n, r, c), real=True)
                else:
                    entries[(r, c)] = sp.conjugate(entries[(c, r)])
        K.append(sp.Matrix(4, 4, lambda r, c: entries[(r, c)]))
    def vec(n):
        return sp.Matrix([x[(n, 0, 0)], x[(n, 0, 1)], x[(n, 1, 0)], x[(n, 1, 1)]])
    def vecb(n):
        return sp.Matrix([[xb[(n, 0, 0)], xb[(n, 0, 1)], xb[(n, 1, 0)], xb[(n, 1, 1)]]])
    kinetic = sum(f[n] * (vecb(n) * K[n] * vec(n))[0] for n in range(NORB))
    def n_p(a):
        return sp.exp(-6 * H * ys[a]) * sum(f[n] * (chib(n, a) * chi(n, a))[0] for n in range(NORB)) / ell ** 3
    def S_p(a):
        return sp.exp(-6 * H * ys[a]) * sum(f[n] * jn[n] * (chib(n, a) * SIG2 * chi(n, a))[0] for n in range(NORB)) / ell ** 3
    dV = [w[a] * sp.exp(6 * H * ys[a]) * ell ** 3 for a in range(A)]
    E_H = sum(dV[a] * lam / 2 * S_p(a) ** 2 for a in range(A))
    E_x = sum(dV[a] * (-lam / 32) * (n_p(a) ** 2 + S_p(a) ** 2) for a in range(A))
    S_ent = -sum(f[n] * sp.log(f[n]) + (1 - f[n]) * sp.log(1 - f[n]) for n in range(NORB))
    F = kinetic - T * S_ent + E_H + E_x
    v_v = [-lam / 16 * n_p(a) for a in range(A)]
    v_s = [-lam / 16 * S_p(a) for a in range(A)]
    # stationarity in chi^dagger: dF/dxb = f_n [ (K_n chi_n)_(a,c) + w_a ((lam S_p + v_s) j_n sigma2 chi_n + v_v chi_n)_(a,c) ]
    stationary = True
    for n in range(NORB):
        kchi = K[n] * vec(n)
        for a in range(A):
            local = (lam * S_p(a) + v_s[a]) * jn[n] * SIG2 * chi(n, a) + v_v[a] * chi(n, a)
            for c in range(2):
                lhs = sp.diff(F, xb[(n, a, c)])
                rhs = f[n] * (kchi[2 * a + c] + w[a] * local[c])
                if sp.expand(lhs - rhs) != 0:
                    stationary = False
    rec.check("stationarityGivesKSEquation", stationary,
              "dF/dchi_n^dagger(a) = f_n w_a [h_0 chi_n + (lambda S_p + v_s)(j sigma2) chi_n + v_v chi_n](a) = f_n eps_n w_a chi_n(a): "
              "the KS equation with M_eff = m + lambda S_p + v_s, v_s = -(lambda/16) S_p, v_v = -(lambda/16) n_p; the "
              "e^{-6Hy} of the densities cancels the e^{6Hy} of dV_7 (local, flat y-measure)")
    # occupations: dF/df_n = <chi_n|h_KS|chi_n> + T ln(f/(1-f)) - mu  (mu from the constraint sum f = N)
    occ_ok = True
    hks = []
    for n in range(NORB):
        expectation = (vecb(n) * K[n] * vec(n))[0] + sum(
            w[a] * (chib(n, a) * ((lam * S_p(a) + v_s[a]) * jn[n] * SIG2 + v_v[a] * I2) * chi(n, a))[0] for a in range(A))
        hks.append(expectation)
        lhs = sp.diff(F - mu * sum(f), f[n])
        rhs = expectation + T * sp.log(f[n] / (1 - f[n])) - mu
        occ_ok &= sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0
    eps_n, Tn, mun = sp.symbols("epsilon T_n mu_n", positive=True)
    fn = sp.Symbol("f_n", real=True)
    solved = sp.solve(sp.Eq(eps_n + Tn * sp.log(fn / (1 - fn)) - mun, 0), fn)
    fd_ok = len(solved) == 1 and sp.simplify(solved[0] - 1 / (sp.exp((eps_n - mun) / Tn) + 1)) == 0
    rec.check("fermiDiracOccupations", occ_ok and fd_ok,
              "dF/df_n = eps_n + T ln(f_n/(1 - f_n)) - mu = 0 gives f_n = 1/(exp((eps_n - mu)/T) + 1)")
    # double counting: sum f <h_KS> = sum f <h_0> + 2 E_H + 2 E_x  =>  E = sum f eps - E_H - E_x
    rec.check("totalEnergyDoubleCounting",
              sp.expand(sum(f[n] * hks[n] for n in range(NORB)) - kinetic - 2 * E_H - 2 * E_x) == 0,
              "E = sum f <h_0> + E_H + E_x = sum f eps - E_H - E_x (eps_n = <h_KS>_n on normalised orbitals); F = E - T S_ent")
    # Hellmann-Feynman (explicit derivatives; the implicit ones vanish at stationarity)
    hf_lambda = sp.simplify(sp.diff(F, lam) - (E_H + E_x) / lam) == 0
    hf_T = sp.simplify(sp.diff(F, T) + S_ent) == 0
    # mass: dh_0/dm = j sigma2 => sum_n f_n sum_a w_a chi^dagger j sigma2 chi = int S_p dV_7
    hf_m = sp.expand(sum(f[n] * sum(w[a] * jn[n] * (chib(n, a) * SIG2 * chi(n, a))[0] for a in range(A)) for n in range(NORB))
                     - sum(dV[a] * S_p(a) for a in range(A))) == 0
    rec.check("hellmannFeynmanLambda", hf_lambda, "dF/dlambda = (E_H + E_x)/lambda at the self-consistent densities")
    rec.check("hellmannFeynmanTemperature", hf_T, "dF/dT = -S_ent (Mermin)")
    rec.check("hellmannFeynmanMass", hf_m, "dF/dm = int S_p dV_7 = sum_n f_n int chi_n^dagger (j sigma2) chi_n dy")
    dh_dk = sp.diff(JSYM * (MM * SIG2 + KAPPA_Y * KK * SIG3), KK)
    rec.check("hellmannFeynmanMomentum", dh_dk == JSYM * KAPPA_Y * SIG3,
              "d eps_n/dk = j int kappa(y) chi_n^dagger sigma3 chi_n dy = l^3 int e^{6Hy} kappa t_n dy at fixed potentials")
    # Mermin structure: with Fermi-Dirac occupations the total T-derivative of F is -S_ent
    eps_syms = sp.symbols("e0:%d" % NORB, real=True)
    Tpos = sp.Symbol("T", positive=True)
    fd = [1 / (sp.exp((eps_syms[n] - mu) / Tpos) + 1) for n in range(NORB)]
    F_model = sum(fd[n] * eps_syms[n] for n in range(NORB)) - Tpos * (
        -sum(fd[n] * sp.log(fd[n]) + (1 - fd[n]) * sp.log(1 - fd[n]) for n in range(NORB))) - mu * sum(fd)
    S_model = -sum(fd[n] * sp.log(fd[n]) + (1 - fd[n]) * sp.log(1 - fd[n]) for n in range(NORB))
    rec.check("merminStructure", sp.simplify(sp.diff(F_model, Tpos) + S_model) == 0,
              "grand potential Omega = sum f eps - T S_ent - mu N at Fermi-Dirac occupations: dOmega/dT = -S_ent; "
              "C_V = dE/dT")
    # variant V: n-only LDA e_x(n, T) = -(lambda/32)(n^2 + S_u(n,T)^2)
    Su = sp.Function("S_u")
    E_xV = sum(dV[a] * (-lam / 32) * (n_p(a) ** 2 + Su(n_p(a)) ** 2) for a in range(A))
    variant_ok = True
    nsym = sp.Symbol("n_sym", positive=True)
    vx_of_n = -lam / 16 * (nsym + Su(nsym) * sp.diff(Su(nsym), nsym))
    for n in range(NORB):
        for a in range(A):
            vx = vx_of_n.subs(nsym, n_p(a))
            for c in range(2):
                lhs = sp.diff(E_xV, xb[(n, a, c)])
                rhs = f[n] * w[a] * vx * chi(n, a)[c]
                if sp.simplify(sp.expand(lhs - rhs).doit()) != 0:
                    variant_ok = False
    rec.check("variantV", variant_ok,
              "with E_x = int dV_7 e_x(n_p, T) the stationarity gives M_eff = m + lambda S_p (no scalar exchange) and "
              "v_x = -(lambda/16)[n_p + S_u dS_u/dn] (STAGE4_SPEC recommendation KS-V)")
    rec.measure("definition", "F[{chi_n},{f_n}] = sum f_n <chi_n|h_0|chi_n> - T S_ent[f] + E_H[S_p] + E_x[n_p, S_p], "
                              "h_0 = j[-i sigma1 d/dy + m sigma2 + kappa k sigma3], dV_7 = e^{6Hy} l^3 dy, constraints "
                              "int chi_n^dagger chi_n dy = 1 (eps_n), sum f_n = N (mu)")
    rec.measure("numericalUse", "finite differences of the self-consistent F in lambda, m, T and of eps_n in k must "
                                "reproduce (E_H + E_x)/lambda, int S_p dV_7, -S_ent and j int kappa t_n; with N conservation, "
                                "current conservation and the double-counting identity these are the stationarity checks")
    return rec


# CHUNK-7-END

# ---------------------------------------------------------------------------
# 8. KS_emt: the Stage-2 energy-momentum tensor reduced to a KS block orbital
# ---------------------------------------------------------------------------

def sesquilinear_coefficients(Q, j):
    """Decompose a 2x2 matrix Q = alpha 1 + beta (j sigma2) + gamma (j sigma3) + delta (j sigma1)
    so that chi^dagger Q chi = alpha n + beta s + gamma t + delta c (per e^{-6Hy}/l^3)."""
    alpha = sp.simplify(Q.trace() / 2)
    beta = sp.simplify((SIG2 * Q).trace() / 2 * j)
    gamma = sp.simplify((SIG3 * Q).trace() / 2 * j)
    delta = sp.simplify((SIG1 * Q).trace() / 2 * j)
    residual = sp.simplify(Q - alpha * I2 - beta * j * SIG2 - gamma * j * SIG3 - delta * j * SIG1)
    return {"n": alpha, "s": beta, "t": gamma, "c": delta}, residual == sp.zeros(2)


def check_emt(alg, red):
    rec = Recorder("emt")
    g = alg.gamma
    W = sp.exp(H * Y)
    hvec = [sp.Integer(1)] + [W * sp.exp(A4C)] * 3 + [sp.Integer(1)] + [W * sp.exp(-A4C)] * 3
    gdiag = [ETA[a] * hvec[a] ** 2 for a in range(8)]
    # static connection (closed forms verified in KS_reduction_OmegaClosedForms): Omega_i = -W' e^{a4} S^{0i},
    # Omega_j = +W' e^{-a4} S^{0j}; as (coefficient, exact matrix) pairs
    Wp = sp.diff(W, Y)
    omega_terms = {}
    for i in (1, 2, 3):
        omega_terms[i] = (-Wp * sp.exp(A4C), alg.S[(0, i)])
    for jx in (5, 6, 7):
        omega_terms[jx] = (Wp * sp.exp(-A4C), alg.S[(0, jx)])
    # {gamma_mu, Omega_nu} + {gamma_nu, Omega_mu} nonzero pairs (16x16, exact structure)
    nonzero_pairs = []
    Gs = sympy_gammas(alg)
    for mu in range(8):
        for nu in range(mu, 8):
            acc = sp.zeros(16)
            for (m1, n1) in ((mu, nu), (nu, mu)):
                if n1 in omega_terms:
                    coefficient, Smat = omega_terms[n1]
                    Om = coefficient * mat_to_sympy(Smat)
                    gl = gdiag[m1] / hvec[m1] * Gs[m1]
                    acc += gl * Om + Om * gl
            if sp.expand(acc) != sp.zeros(16):
                nonzero_pairs.append((SPACE_COORDINATES[mu], SPACE_COORDINATES[nu]))
    rec.check("staticAnticommutators", nonzero_pairs == [("x1", "x4"), ("x2", "x4"), ("x3", "x4"), ("x4", "x5"), ("x4", "x6"), ("x4", "x7")],
              {"nonzeroPairs": nonzero_pairs, "note": "six of the Stage-2 21 pairs survive for a4 constant: "
                                                       "A_{i4} = H e^{Hy+a4} gamma^0 gamma^i gamma^4, A_{4j} = H e^{Hy-a4} gamma^0 gamma^4 gamma^j"})
    # per-block reduction: chi' = N chi on shell, densities n, s, t, c
    c1, c2, cb1, cb2 = sp.symbols("c1 c2 cb1 cb2")
    chi = sp.Matrix([c1, c2])
    chib = sp.Matrix([[cb1, cb2]])
    results = {}
    forms_ok = True
    for b in red.blocks:
        j = b["j"]
        N = block_ode_matrix(j=j)                       # on-shell chi' = N chi with the block's own j
        Nd = N.H                                        # N^dagger (all parameters real)
        def blk(M):
            return mat_to_sympy(red.block_of(M, b))
        BCg = [blk(mat_mul(alg.BC, g[a])) for a in range(8)]
        BC2 = blk(alg.BC)
        def d_op(nu):
            """block operator of D_nu on the ansatz (acting on chi): returns (matrix on chi, matrix on chi')"""
            on_chi = sp.zeros(2)
            on_dchi = sp.zeros(2)
            if nu == 0:
                on_dchi = I2
                on_chi = -3 * H * I2
            elif nu == 1:
                on_chi = sp.I * KK * I2
            elif nu == 4:
                on_chi = -sp.I * EPS * I2
            return on_chi, on_dchi
        def bilinear(mu, nu):
            """chi^dagger [BC gamma_mu D_nu] chi with the connection term, per e^{-6Hy}/l^3."""
            lower = gdiag[mu] / hvec[mu]                  # gamma_mu = g_mu mu gamma^mu = (g_mu mu / h_mu) gamma^a
            on_chi, on_dchi = d_op(nu)
            value = (chib * (lower * BCg[mu]) * (on_chi * chi + on_dchi * N * chi))[0]
            if nu in omega_terms:
                coefficient, Smat = omega_terms[nu]
                value += coefficient * lower * (chib * blk(mat_mul(mat_mul(alg.BC, g[mu]), Smat)) * chi)[0]
            return value
        def bilinear_bar(mu, nu):
            """(D_mu Psi)^dagger C gamma_nu Psi -> (d_mu chi)^dagger [BC gamma_nu] chi - chi^dagger [BC Omega_mu gamma_nu] chi."""
            lower = gdiag[nu] / hvec[nu]
            on_chi, on_dchi = d_op(mu)
            row = chib * on_chi.H + chib * Nd * on_dchi          # (d_mu chi)^dagger
            value = (row * (lower * BCg[nu]) * chi)[0]
            if mu in omega_terms:
                coefficient, Smat = omega_terms[mu]
                value -= coefficient * lower * (chib * blk(mat_mul(mat_mul(alg.BC, Smat), g[nu])) * chi)[0]
            return value
        # on-shell one-body Lagrangian density: (1/2)(Psibar gamma^mu D_mu Psi - D_mu Psibar gamma^mu Psi) - m Psibar Psi
        Ls = sp.Rational(1, 2) * sum((bilinear(mu, mu) - bilinear_bar(mu, mu)) / gdiag[mu] for mu in range(8)) \
            - MSYM * (chib * BC2 * chi)[0]
        Ls = sp.expand(Ls)
        def T_lower(mu, nu):
            value = -sp.Rational(1, 4) * (bilinear(mu, nu) + bilinear(nu, mu) - bilinear_bar(mu, nu) - bilinear_bar(nu, mu))
            if mu == nu:
                value += gdiag[mu] * Ls
            return sp.expand(value)
        def coefficients(expr):
            Q = sp.zeros(2)
            for r, rb in enumerate((cb1, cb2)):
                for cidx, cc in enumerate((c1, c2)):
                    Q[r, cidx] = sp.expand(expr).coeff(rb).coeff(cc)
            coeffs, exact = sesquilinear_coefficients(Q, j)
            return coeffs, exact
        rho, ok_rho = coefficients(T_lower(4, 4))
        py, ok_py = coefficients(T_lower(0, 0))
        p1, ok_p1 = coefficients(T_lower(1, 1) / gdiag[1])
        p2, ok_p2 = coefficients(T_lower(2, 2) / gdiag[2])
        p3, ok_p3 = coefficients(T_lower(3, 3) / gdiag[3])
        pt = [coefficients(T_lower(jx, jx) / gdiag[jx]) for jx in (5, 6, 7)]
        ls_c, ok_ls = coefficients(Ls)
        ty4, ok_ty4 = coefficients(T_lower(0, 4))
        ty1, ok_ty1 = coefficients(T_lower(0, 1))
        t41, ok_t41 = coefficients(-T_lower(4, 1))        # T^4_1 = g^{44} T_41 = -T_41
        t14, ok_t14 = coefficients(-T_lower(1, 4))
        others = {}
        for mu in range(8):
            for nu in range(mu + 1, 8):
                if (mu, nu) in ((0, 1), (0, 4), (1, 4)):
                    continue
                cf, okc = coefficients(T_lower(mu, nu))
                others[(SPACE_COORDINATES[mu], SPACE_COORDINATES[nu])] = all(v == 0 for v in cf.values()) and okc
        trace_c = {key: sp.simplify(sum(coefficients(T_lower(mu, mu) / gdiag[mu])[0][key] for mu in range(8)))
                   for key in ("n", "s", "t", "c")}
        results[b["index"]] = {"rho": rho, "p_y": py, "p_1": p1, "p_2": p2, "p_3": p3, "p_t": pt, "Ls": ls_c,
                               "T_y4": ty4, "T_y1": ty1, "T^4_1": t41, "T^4_1 (from T_14)": t14,
                               "others": others, "trace": trace_c}
        forms_ok &= all([ok_rho, ok_py, ok_p1, ok_p2, ok_p3, ok_ls, ok_ty4, ok_ty1, ok_t41, ok_t14] + [p[1] for p in pt])
    rec.check("bilinearExtractionExact", forms_ok, "every component is a sesquilinear form in (chi, chi^dagger) "
              "spanned by the four densities n, s, t, c (no residual)")
    first = results[0]
    def normalised_t41(k):
        t = results[k]["T^4_1"]
        jk = red.blocks[k]["j"]
        return {"n": t["n"], "c_js": sp.simplify(t["s"] * jk), "t": t["t"], "c": t["c"]}
    same = all(results[k][key] == first[key] for k in results for key in ("rho", "p_y", "p_1", "p_2", "p_3", "Ls", "T_y1", "trace"))
    same_t41 = all(normalised_t41(k) == normalised_t41(0) for k in results)
    ty4_by_j = {jv: str(results[k]["T_y4"]["c"]) for k in results for jv in (red.blocks[k]["j"],)}
    rec.check("blockIndependentForms", same and same_t41,
              {"note": "the reduced components have the same (n, s, t, c) coefficients in all 8 blocks; T^4_1 has the "
                       "same coefficients of n, t and of (j s) = e^{-6Hy} chi^dagger sigma2 chi / l^3",
               "T_y4 coefficient of c by j": ty4_by_j})
    exp_rho = {"n": EPS - VV, "s": -(MM - MSYM), "t": 0, "c": 0}
    exp_py = {"n": EPS, "s": -MSYM, "t": -KAPPA_Y * KK, "c": 0}
    exp_p1 = {"n": VV, "s": MM - MSYM, "t": KAPPA_Y * KK, "c": 0}
    exp_p23 = {"n": VV, "s": MM - MSYM, "t": 0, "c": 0}
    def eq(a, b):
        return all(sp.simplify(a[k] - b[k]) == 0 for k in ("n", "s", "t", "c"))
    rec.check("rho", eq(first["rho"], exp_rho), {k: str(v) for k, v in first["rho"].items()})
    rec.check("py", eq(first["p_y"], exp_py), {k: str(v) for k, v in first["p_y"].items()})
    rec.check("p1", eq(first["p_1"], exp_p1), {k: str(v) for k, v in first["p_1"].items()})
    rec.check("p2p3", eq(first["p_2"], exp_p23) and eq(first["p_3"], exp_p23), {k: str(v) for k, v in first["p_2"].items()})
    rec.check("pt", all(eq(p[0], exp_p23) for p in first["p_t"]), {k: str(v) for k, v in first["p_t"][0][0].items()})
    rec.check("onShellLagrangian", eq(first["Ls"], exp_p23), {k: str(v) for k, v in first["Ls"].items()})
    rec.check("Ty4ProportionalToCurrent", all(first["T_y4"][k] == 0 for k in ("n", "s", "t")),
              {"coefficientOfCurrent": str(first["T_y4"]["c"]), "note": "vanishes for eigenstates (c = 0)"})
    rec.check("Ty1ProportionalToCurrent", all(first["T_y1"][k] == 0 for k in ("n", "s", "t")),
              {"coefficientOfCurrent": str(first["T_y1"]["c"])})
    t41 = first["T^4_1"]
    t41n = normalised_t41(0)
    rec.check("T41form", sp.simplify(t41n["n"] - KK / 2) == 0 and t41n["c"] == 0
              and sp.simplify(t41n["c_js"] - H * sp.exp(A4C + H * Y) / 4) == 0
              and sp.simplify(t41n["t"] - sp.exp(A4C + H * Y) * EPS / 2) == 0,
              {"T^4_1": "c_n n + c_t t + c_js (j s), (j s) = e^{-6Hy} chi^dagger sigma2 chi / l^3",
               "c_n": str(t41n["n"]), "c_t": str(t41n["t"]), "c_js": str(t41n["c_js"]), "c_s": "0", "c_c": str(t41n["c"]),
               "origin of c_js": "the connection term A_{14} = H e^{Hy+a4} gamma^0 gamma^1 gamma^4"})
    rec.check("symmetric", eq(first["T^4_1"], first["T^4_1 (from T_14)"]))
    # T^4_1 under (k, j) -> (-k, -j), chi -> sigma3 chi: n even, t and (j s) odd, k odd => T^4_1 odd: cancels over {k, -k}
    # the (n,s,t,c) coefficients refer to s = j chi^dagger sigma2 chi and t = j chi^dagger sigma3 chi; under the map
    # j s -> -(j s) and j t -> ... : chi -> sigma3 chi gives chi^dagger sigma2 chi -> -chi^dagger sigma2 chi and
    # chi^dagger sigma3 chi -> +chi^dagger sigma3 chi, with j -> -j: s -> +s, t -> -t.
    # block 4 has j = -1: T^4_1 of (block 4, -k) on the mapped densities (n, s invariant, t -> -t) must be -T^4_1 of (block 0, k)
    t41_partner = results[4]["T^4_1"]
    t41_mapped = {"n": t41_partner["n"].subs(KK, -KK), "s": t41_partner["s"].subs(KK, -KK),
                  "t": -t41_partner["t"].subs(KK, -KK), "c": -t41_partner["c"].subs(KK, -KK)}
    cancels = all(sp.simplify(t41_mapped[k] + t41[k]) == 0 for k in ("n", "s", "t", "c"))
    rec.check("T41cancelsOverShell", cancels, "T^4_1 is odd under (k,j,chi) -> (-k,-j,sigma3 chi) at the same eps "
                                             "(n, s invariant, t and (j s) flip): it cancels over every closed shell "
                                             "{k,-k} x 8 blocks")
    rec.check("offBlockComponentsVanishPerOrbital", all(first["others"].values()),
              {"vanishing": sorted("%s%s" % k for k in first["others"])})
    tr = first["trace"]
    rec.check("trace", sp.simplify(tr["n"] - 7 * VV) == 0 and sp.simplify(tr["s"] - (7 * (MM - MSYM) - MSYM)) == 0
              and tr["t"] == 0 and tr["c"] == 0, {k: str(v) for k, v in tr.items()})
    # rest state (H -> 0 homogeneous limit of the formulas): eps = M = m, s = n, k = 0, v_v = 0: dust
    sub = {EPS: MSYM, MM: MSYM, KK: 0, VV: 0}
    dust = (sp.simplify(first["rho"]["n"].subs(sub)) == MSYM and sp.simplify(first["rho"]["s"].subs(sub)) == 0
            and sp.simplify(first["p_y"]["n"].subs(sub) + first["p_y"]["s"].subs(sub)) == 0
            and sp.simplify(first["p_1"]["n"].subs(sub) + first["p_1"]["s"].subs(sub)) == 0)
    rec.check("restStateDust", dust, "eps = M_eff = m, s = n, k = 0, v_v = 0: rho = m n, p_y = p_(i) = 0 (dust)")
    # interaction part and KS-state sums
    rec.measure("interactionPart", "<U> = e_H + e_x = (lambda/2) S_p^2 - (lambda/32)(n_p^2 + S_p^2) enters rho with + and "
                                   "every p_(i) with - (all seven transverse directions); L_s = sum f L_s^(1) - <U>")
    rec.measure("ksState", {"rho": "sum_n f_n [eps_n n_n - (M_eff - m) s_n - v_v n_n] + e_H + e_x",
                            "p_y": "sum_n f_n [eps_n n_n - m s_n - kappa k_n t_n] - e_H - e_x",
                            "p_3": "sum_n f_n [(1/3) kappa k_n t_n + (M_eff - m) s_n + v_v n_n] - e_H - e_x (shell average)",
                            "p_t": "sum_n f_n [(M_eff - m) s_n + v_v n_n] - e_H - e_x"})
    # Z2 parity of the KS quantities from the density parities (P_A: n even, s odd, t even, c odd; M_eff - m odd)
    parity = {"n": 1, "s": -1, "t": 1, "c": -1, "Meff-m": -1, "vv": 1, "kappa": 1, "eps": 1, "m": -1}
    rho_terms = [parity["eps"] * parity["n"], parity["Meff-m"] * parity["s"], parity["vv"] * parity["n"]]
    py_terms = [parity["eps"] * parity["n"], parity["m"] * parity["s"], parity["kappa"] * parity["t"]]
    p1_terms = [parity["kappa"] * parity["t"], parity["Meff-m"] * parity["s"], parity["vv"] * parity["n"]]
    rec.check("densityParityTable", all(v == 1 for v in rho_terms + py_terms + p1_terms),
              {"P_A": "n even, s odd, t even, c odd; with the mirror mass -m (M_eff - m odd) rho, p_y, p_(i) are even",
               "P_B": "n, s, t even, c odd",
               "sectors": "even-parity orbitals carry n(0) = |chi_1(0)|^2 and s(0) = t(0) = 0 on the brane; odd-parity "
                          "orbitals n(0) = |chi_2(0)|^2, s(0) = t(0) = 0"})
    Lp = sp.Symbol("L", positive=True)
    vol = sp.integrate(sp.exp(6 * H * Y), (Y, -Lp, 0))
    rec.check("properVolumeAverage", sp.simplify(vol - (1 - sp.exp(-6 * H * Lp)) / (6 * H)) == 0,
              "<X> = int_{-L}^0 X e^{6Hy} dy / int_{-L}^0 e^{6Hy} dy, int e^{6Hy} dy = (1 - e^{-6HL})/(6H); brane-localised "
              "fraction int_{-delta}^0 n_p e^{6Hy} dy / int_{-L}^0 n_p e^{6Hy} dy")
    # comparison with the required source and the E4.1 conditions for the static field
    Ssym = sp.Symbol("S", positive=True)
    m_real = sp.Symbol("m_r", real=True)
    m_needed = sp.solve(sp.Eq(m_real * Ssym, -36 * H ** 2 / KAPPA_G), m_real)[0]
    lam_needed = sp.solve(sp.Eq(LAM * Ssym ** 2, 30 * H ** 2 / KAPPA_G), LAM)[0]
    rec.check("requiredSourceComparison", sp.simplify(m_needed * Ssym + 36 * H ** 2 / KAPPA_G) == 0
              and bool(sp.simplify(lam_needed.subs({H: 1, KAPPA_G: 1, Ssym: 2})) > 0)
              and bool(sp.simplify(m_needed.subs({H: 1, KAPPA_G: 1, Ssym: 2})) < 0),
              {"field": "rho_req = -21 H^2/kappa < 0, p_req = +15 H^2/kappa (w = -5/7)",
               "ksState": "rho = sum f (eps - v_v) n - (lambda/2) S_p^2 - v_s S_p + e_x >= 0 for positive-energy occupations "
                          "at weak coupling: the mismatch is at least |rho_req| + rho_KS",
               "E4.1 static conditions": "m S = -36 H^2/kappa and lambda S^2 = 30 H^2/kappa: lambda > 0 and m S < 0",
               "m for given S": str(m_needed), "lambda for given S": str(lam_needed),
               "signOfS": "the uniform gas has S = 8 int (m/E)(f_+ + f_-) > 0 for m > 0, so the sourcing solutions need "
                          "m < 0 (the gamma^8 image m -> -m, lambda -> -lambda of a positive-mass state has S -> -S, "
                          "CONTRACT errata E2); the numerics must report the sign of S_p and the ratios to the source"})
    own = {"T41": {"n": t41n["n"], "s": sp.Integer(0), "t": t41n["t"], "c_js": t41n["c_js"]},
           "Ty4": first["T_y4"]["c"], "Ty1": first["T_y1"]["c"]}
    return rec, own


# CHUNK-8-END

# ---------------------------------------------------------------------------
# 9. The exchange table e_x(n, T) (units m = 1) for the LDA of both solvers
# ---------------------------------------------------------------------------

TABLE_DENSITY_DECADES = (-4, 3)          # n from 1e-4 to 1e3 (units m^d), 4 points per decade
TABLE_TEMPERATURES = ("0", "0.05", "0.1", "0.2", "0.3", "0.5", "0.7", "1", "1.5", "2")
QUICK_TEMPERATURES = ("0", "0.3", "1")


def _float_rule_arrays(rule):
    return ([float(v) for v in rule.p], [float(v) for v in rule.w], [float(v) for v in rule.E],
            [float(v) for v in rule.fp], [float(v) for v in rule.fm])


def exchange_trace_float(rule, d, angular_nodes=4):
    """Tr(BC rho BC rho) by the same double quadrature in double precision
    (numpy when available, otherwise pure Python); returns a float."""
    p, w, E, fp, fm = _float_rule_arrays(rule)
    xs, ws = angular_rule(d, angular_nodes)
    xs = [float(v) for v in xs]
    ws = [float(v) for v in ws]
    m2 = float(rule.m) ** 2
    try:
        import numpy as np
        P = np.array(p)
        Wt = np.array(w) / 8.0
        Ea = np.array(E)
        A = np.array(fp) * Wt
        Bv = np.array(fm) * Wt
        inv = 1.0 / np.outer(Ea, Ea)
        pq = np.outer(P, P)
        total = 0.0
        for x, wx in zip(xs, ws):
            ratio = (m2 - pq * x) * inv
            kpp = 4.0 * (1.0 + ratio)
            kpm = 4.0 * (1.0 - ratio)
            total += wx * (np.outer(A, A).ravel().dot(kpp.ravel()) + np.outer(Bv, Bv).ravel().dot(kpp.ravel())
                           - 2.0 * np.outer(A, Bv).ravel().dot(kpm.ravel()))
        return float(total)
    except ImportError:
        total = 0.0
        n = len(p)
        for i in range(n):
            ai, bi = fp[i] * w[i] / 8.0, fm[i] * w[i] / 8.0
            for j in range(n):
                aj, bj = fp[j] * w[j] / 8.0, fm[j] * w[j] / 8.0
                inv = 1.0 / (E[i] * E[j])
                pq = p[i] * p[j]
                for x, wx in zip(xs, ws):
                    ratio = (m2 - pq * x) * inv
                    total += wx * ((ai * aj + bi * bj) * 4.0 * (1.0 + ratio) - 2.0 * ai * bj * 4.0 * (1.0 - ratio))
        return total


def table_row(n, T, d):
    """One table entry (floats) with quadrature error estimates."""
    with mpmath.workdps(20):
        nm, Tm = mpmath.mpf(n), mpmath.mpf(T)
        mu = gas_mu_of_n(nm, Tm, 1, d)
        coarse = GasRule(1, mu, Tm, d, 16)
        fine = GasRule(1, mu, Tm, d, 32)
        mc, mf = coarse.moments(), fine.moments()
        trc = exchange_trace_float(coarse, d, 4)
        trf = exchange_trace_float(fine, d, 6)
        closed = (mf["n"] ** 2 + mf["S"] ** 2) / 16
        S = mf["S"]
        if Tm > 0:
            dSdn = mf["dS_dmu"] / mf["dn_dmu"]
        else:
            kf = mpmath.sqrt(mu * mu - 1)
            dSdn = 1 / mpmath.sqrt(1 + kf * kf)
        row = {
            "n": float(nm), "T": float(Tm), "mu": float(mu), "S": float(S), "dSdn": float(dSdn),
            "exOverLambda_closedForm": float(-closed / 2),
            "exOverLambda_quadrature": float(-trf / 2),
            "quadratureErrorEstimate": float(abs(trf - trc) / 2),
            "momentsErrorEstimate": {"n": float(abs(mf["n"] - mc["n"])), "S": float(abs(mf["S"] - mc["S"]))},
            "relativeDeviationFromClosedForm": float(abs(trf - closed) / closed) if closed != 0 else 0.0,
            "vxOverLambda_nOnly": float(-(nm + S * dSdn) / 16),
            "vvOverLambda": float(-nm / 16),
            "vsOverLambda": float(-S / 16),
            "eKin": float(mf["eKin"]),
            "entropyDensity": float(mf["entropy"]),
        }
    return row


def build_exchange_table(quick=False):
    """The table for d = 4 (primary, proper 7-volume densities in m^4) and d = 3 (m^3)."""
    lo, hi = TABLE_DENSITY_DECADES
    per_decade = 4
    if quick:
        exponents = [lo + 2 * i for i in range((hi - lo) // 2 + 1)]
        densities = [mpmath.mpf(10) ** e for e in exponents]
        temps = QUICK_TEMPERATURES
    else:
        densities = [mpmath.mpf(10) ** (mpmath.mpf(i) / per_decade) for i in range(lo * per_decade, hi * per_decade + 1)]
        temps = TABLE_TEMPERATURES
    tables = {}
    worst = 0.0
    for d in (4, 3):
        rows = []
        for T in temps:
            for n in densities:
                row = table_row(n, T, d)
                rows.append(row)
                worst = max(worst, row["relativeDeviationFromClosedForm"])
        tables["d%d" % d] = {
            "dimension": d,
            "units": "m = 1: n in m^%d, e_x/lambda in m^%d, T in m, mu in m" % (d, 2 * d),
            "description": ("8-fold degenerate free relativistic gas with momentum in the %d spatial directions "
                            "(%s); densities per unit %d-volume; normal ordered (f_+ particles, f_- antiparticles)"
                            % (d, "y, x1, x2, x3 (proper 7-volume densities of the KS problem)" if d == 4
                               else "x1, x2, x3 only; the y-frozen gas used by the numerical solvers' lda-n variant", d)),
            "densityGrid": [row["n"] for row in rows[:len(densities)]],
            "temperatureGrid": [float(mpmath.mpf(t)) for t in temps],
            "rowOrder": "for T in temperatureGrid: for n in densityGrid",
            "columns": ["n", "T", "mu", "S", "dSdn", "exOverLambda_closedForm", "exOverLambda_quadrature",
                        "quadratureErrorEstimate", "momentsErrorEstimate", "relativeDeviationFromClosedForm",
                        "vxOverLambda_nOnly", "vvOverLambda", "vsOverLambda", "eKin", "entropyDensity"],
            "rows": rows,
        }
    document = {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "description": "Uniform-gas exchange energy density e_x(n, T) of the dirac16complex contact interaction "
                       "U = (lambda/2) S^2 (Hartree-Fock, normal ordered), tabulated for the LDA of the Stage-4 solvers.",
        "closedForm": "e_x(n, T) = -(lambda/32) [n^2 + S_u(n, T)^2] exactly (the angular average kills p.q); "
                      "e_H = (lambda/2) S^2; v_v = de_x/dn|_S = -(lambda/16) n; v_s = de_x/dS|_n = -(lambda/16) S; "
                      "n-only LDA potential v_x = de_x/dn|_T = -(lambda/16)[n + S_u dS_u/dn]",
        "howToUse": "e_x = lambda * exOverLambda_closedForm (both solvers implement the closed form; the table is the "
                    "independent cross-check and supplies S_u(n, T), dS_u/dn for the n-only variant KS-V). The proper "
                    "7-volume density n_p of the KS problem has units m^4: use table d4. Table d3 (units m^3) matches "
                    "the gas relation coded in scripts/ks_reference_solver.py and the Rust crate (momentum in 3-space only) "
                    "and is dimensionally inconsistent with n_p unless a y-extent is factored out; it is kept for comparison.",
        "interpolation": "S_u and dS_u/dn are smooth in (log10 n, T): interpolate them bilinearly (or with cubic "
                         "splines) on the grid (log10 n, T) at fixed T rows, then evaluate the closed form; do not "
                         "differentiate the interpolant of S_u to get dS_u/dn (tabulated directly). Beyond the grid "
                         "use the T = 0 closed forms (n <-> k_F) or recompute; at T > 0 and n -> 0 the thermal S_u "
                         "tends to the pair value S_u(0, T) > 0.",
        "quadrature": "mu from n by bisection (T > 0) or k_F (T = 0); moments and Tr(BC rho BC rho) by composite "
                      "Gauss-Legendre in |p| (panels at the Fermi edge; 16 vs 32 nodes per panel give the error "
                      "estimate) with the raw kernel 4[1 + ab(m^2 - pq cos theta)/(EE')] and an exact 4/6-node angular "
                      "rule; mpmath 20 digits for the moments, double precision for the double sum",
        "primary": "d4",
        "maxRelativeDeviationFromClosedForm": worst,
        "tables": tables,
        "sourceSha256": {},
    }
    return document


# CHUNK-9-END

# ---------------------------------------------------------------------------
# 10. KS_agreesWithWolfram: compare with kohn-sham-theory.json (conventions:
#     same J, K1, K2, projectors, seed rule and block order; exact rationals)
# ---------------------------------------------------------------------------

def _inputform_to_sympy(text, symbols):
    """Translate the small Wolfram InputForm subset used in the theory file."""
    s = text.strip()
    s = s.replace("E^(", "exp(")
    s = re.sub(r"E\^([A-Za-z_][A-Za-z0-9_]*)", r"exp(\1)", s)
    s = s.replace("vv[y]", "vv").replace("Meff[y]", "Meff").replace("^", "**")
    return sp.sympify(s, locals=symbols)


def check_wolfram_agreement(alg, red, block_forms, theory_path, own):
    """own: dict with the exact quantities derived here (c formula, T41 coefficients, ...)."""
    rec = Recorder("wolfram")
    with open(theory_path, "r", encoding="utf-8") as handle:
        th = json.load(handle)
    geo = th.get("geometry", {})
    cur = geo.get("curvature", {})
    ein = [str(v) for v in cur.get("einsteinMixedValues", [])]
    rec.check("einsteinValues", ein == ["15", "15", "15", "15", "21", "15", "15", "15"], ein)
    req = geo.get("requiredSource", {})
    rec.check("requiredSource", req.get("rhoValue") == "-21" and req.get("pValue") == "15", req.get("w"))
    ext = geo.get("extrinsicCurvature", {}).get("values", [])
    rec.check("extrinsicCurvature", [str(v) for v in ext] == ["1", "1", "1", "0", "1", "1", "1"], ext)
    brane = geo.get("extensions", {}).get("E2_Z2mirror", {})
    rec.check("braneStress", [str(v) for v in brane.get("braneStressValues", [])] == ["-10", "-10", "-10", "-12", "-10", "-10", "-10"]
              and "[K_ij] - h_ij [K] = -kappa S_ij" in brane.get("israelConvention", ""),
              "same sign convention and the same S^i_j = -(10,10,10,12,10,10,10) H/kappa")
    rec.check("christoffelCount", geo.get("christoffel", {}).get("nonzeroCount") == 18)
    bd = th.get("reduction", {}).get("blockDiagonalisation", {})
    blocks = bd.get("blocks", [])
    rec.check("blockCount", len(blocks) == 8 and str(bd.get("columnNormSquared")) == "8")
    same_labels = all(int(b["j"]) == BLOCK_LABELS[i][0] and int(b["s2"]) == BLOCK_LABELS[i][1]
                      and int(b["s3"]) == BLOCK_LABELS[i][2] and b["index"] == i for i, b in enumerate(blocks))
    rec.check("blockOrder", same_labels, "index = 4(1-j)/2 + 2(1-s2)/2 + (1-s3)/2")
    basis_identical = True
    subspace_identical = True
    seeds_identical = True
    matrices_identical = {name: True for name in ("A0", "A1", "A4", "B", "C", "BC", "gamma4gamma1",
                                                  "numberDensityMatrix", "scalarDensityMatrix", "yCurrentMatrix",
                                                  "kCurrentMatrix")}
    for i, wb in enumerate(blocks):
        mine = red.blocks[i]
        vplus = [CQ(Fraction(p[0]), Fraction(p[1])) for p in wb["vPlus"]]
        vminus = [CQ(Fraction(p[0]), Fraction(p[1])) for p in wb["vMinus"]]
        basis_identical &= (vplus == mine["vPlus"]) and (vminus == mine["vMinus"])
        seeds_identical &= wb.get("seedColumn") == mine["seed"]
        # same 2-dimensional subspace: P_mine v_wolfram = v_wolfram for both vectors
        for v in (vplus, vminus):
            pv = [sum((mine["P"][r][l] * v[l] for l in range(16)), CQ_ZERO) for r in range(16)]
            subspace_identical &= all(pv[r] == v[r] for r in range(16))
        for name in matrices_identical:
            theirs = pairs_to_mat(wb[name])
            matrices_identical[name] &= mat_eq(theirs, block_forms[name][i])
    rec.check("basisVectorsIdentical", basis_identical, "v+, v- of every block identical (same seed rule)")
    rec.check("seedColumnsIdentical", seeds_identical)
    rec.check("blockSubspacesIdentical", subspace_identical)
    rec.check("blockMatricesIdentical", all(matrices_identical.values()), matrices_identical)
    vmat = bd.get("basisMatrixUnnormalised")
    if vmat:
        theirs = pairs_to_mat(vmat)
        rec.check("basisMatrixIdentical", mat_eq(theirs, red.V))
    types = bd.get("types", {})
    rec.check("typesAndDims", types.get("algebraDim") == 8 and types.get("commutantDim") == 32
              and types.get("commutantDimWithBC") == 16)
    formulas = bd.get("blockFormulas", {})
    rec.check("blockFormulas", formulas.get("A0") == "sigma3" and formulas.get("A4") == "j sigma1"
              and formulas.get("BC") == "j sigma2" and formulas.get("B") == "j s2 (scalar)"
              and formulas.get("C") == "s2 sigma2" and formulas.get("gamma4gamma1") == "-j sigma3", formulas)
    # zero-mode splitting coefficient
    zm = th.get("reduction", {}).get("blockODE", {}).get("zeroMode", {})
    try:
        LL, a4c, Hs, Ms = sp.symbols("LL a4c H M", positive=True)
        theirs_c = _inputform_to_sympy(zm.get("cValue", ""), {"LL": LL, "a4c": a4c, "H": Hs, "M": Ms, "E": sp.E})
        mine_c = own["cValue"].subs({sp.Symbol("L", positive=True): LL, A4C: a4c, H: Hs, sp.Symbol("M", positive=True): Ms})
        rec.check("zeroModeSplitting", sp.simplify(theirs_c - mine_c) == 0, str(theirs_c))
    except Exception as error:      # noqa: BLE001 - reported, never hidden
        rec.check("zeroModeSplitting", False, "unparsed: %s" % error)
    # boundary projectors
    proj = th.get("boundary", {}).get("parityConditions", {}).get("projectors", {})
    even = pairs_to_mat(proj.get("even", [[["1", "0"], ["0", "0"]], [["0", "0"], ["1", "0"]]]))
    odd = pairs_to_mat(proj.get("odd", [[["1", "0"], ["0", "0"]], [["0", "0"], ["1", "0"]]]))
    rec.check("parityProjectors", mat_eq(even, mat_from_ints([[0, 0], [0, 1]])) and mat_eq(odd, mat_from_ints([[1, 0], [0, 0]])))
    # exchange
    ex = th.get("exchange", {})
    rec.check("filledShellRatio", str(ex.get("filledShell", {}).get("ratio")) == "1/8")
    closed = ex.get("uniformGas", {}).get("closedForm", "")
    rec.check("exchangeClosedForm", "lambda/32" in closed and "n^2 + S^2" in closed, closed[:120])
    kern = ex.get("kernel", {})
    rec.check("kernelForms", "4 [ 1 + (m^2 - p.q)/(E_p E_q) ]" in kern.get("plusPlus", "")
              and "4 [ 1 - (m^2 - p.q)/(E_p E_q) ]" in kern.get("plusMinus", ""), kern.get("plusPlus"))
    # EMT off-diagonal coefficients
    emt = th.get("emt", {}).get("oneBody", {}).get("offDiagonal", {})
    try:
        syms = {"kk": KK, "eps": EPS, "vv": VV, "a4c": A4C, "H": H, "y": Y, "E": sp.E}
        m41 = re.search(r"\{[^{}]*\}", emt.get("T_41", ""))
        theirs_41 = [_inputform_to_sympy(v, syms) for v in m41.group(0).strip("{}").split(",")]
        mine_41 = [own["T41"][k] for k in ("n", "s", "t", "c_js")]
        ok41 = all(sp.simplify(a - b) == 0 for a, b in zip(theirs_41, mine_41))
        m_y4 = re.search(r"coefficient (.+?)\): vanishes", emt.get("T_y4", ""))
        theirs_y4 = _inputform_to_sympy(m_y4.group(1), syms)
        ok_y4 = sp.simplify(theirs_y4 - own["Ty4"]) == 0
        m_y1 = re.search(r"coefficient (.+?)\): vanishes", emt.get("T_y1", ""))
        theirs_y1 = _inputform_to_sympy(m_y1.group(1), syms)
        ok_y1 = sp.simplify(theirs_y1 - own["Ty1"]) == 0
        rec.check("emtOffDiagonalCoefficients", ok41 and ok_y4 and ok_y1,
                  {"T41_theirs": [str(v) for v in theirs_41], "T41_mine": [str(v) for v in mine_41],
                   "Ty4_theirs": str(theirs_y4), "Ty4_mine": str(own["Ty4"]),
                   "Ty1_theirs": str(theirs_y1), "Ty1_mine": str(own["Ty1"])})
    except Exception as error:      # noqa: BLE001
        rec.check("emtOffDiagonalCoefficients", False, "unparsed: %s" % error)
    rec.measure("conventions", {"J": "gamma^0 gamma^1 gamma^4 on both sides (Rust/probe label s = -j)",
                                "basisRule": "v+ = 8 P (1 + gamma^0)/2 e_c, first c with nonzero image; v- = gamma^0 gamma^1 v+",
                                "theoryFile": relative(theory_path)})
    return rec


# CHUNK-10-END

# ---------------------------------------------------------------------------
# 11. Driver, report, command line
# ---------------------------------------------------------------------------

def run_checks(fixture_path=DEFAULT_FIXTURE, theory_path=DEFAULT_THEORY, families=None, quick=False,
               build_table=True):
    families = list(FAMILIES) if families is None else list(families)
    checks = {}
    measurements = {}
    timings = {}
    inputs = {}
    exceptions = {}
    alg = Algebra(fixture_path)
    facts = alg.basic_facts()
    checks["KS_fixture_contractConstructionMatchesFixture"] = bool(facts["fixtureAgreement"])
    checks["KS_fixture_cliffordAndC"] = bool(facts["clifford"] and facts["C_squared_one"] and facts["Cgamma_antisymmetric"])
    checks["KS_fixture_Bproperties"] = bool(facts["B_hermitian"] and facts["B_squared_one"] and facts["B_commutes_C"]
                                            and facts["BC_is_minus_i_gamma4"])
    measurements["fixture"] = facts
    if fixture_path and os.path.exists(fixture_path):
        inputs[relative(fixture_path)] = sha256_file(fixture_path)
    red = None
    block_forms = None
    own = {}

    def family(name, function):
        start = time.time()
        try:
            result = function()
        except Exception as error:      # noqa: BLE001 - a failing family is a failed check, never a crash
            exceptions[name] = "%s: %s" % (type(error).__name__, error)
            checks[FAMILY_CHECKS.get(name, "KS_%s" % name)] = False
            timings[name] = round(time.time() - start, 3)
            return None
        timings[name] = round(time.time() - start, 3)
        return result

    if "geometry" in families:
        rec = family("geometry", lambda: check_geometry(alg))
        if rec is not None:
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["geometry"]] = rec.ok()
            measurements["KS_geometry"] = rec.measurements
    if any(f in families for f in ("reduction", "boundary", "emt")) or os.path.exists(theory_path or ""):
        red = BlockReduction(alg)
    if "reduction" in families:
        rec = Recorder("reduction")

        def reduction():
            check_reduction_a(alg, rec)
            red_local, forms = check_reduction_b(alg, rec)
            check_reduction_c(alg, rec)
            return red_local, forms
        result = family("reduction", reduction)
        if result is not None:
            red, block_forms = result
            own["cValue"] = rec.measurements.get("zeroModeSplittingSympy")
            rec.measurements.pop("zeroModeSplittingSympy", None)
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["reduction"]] = rec.ok()
            measurements["KS_reduction"] = rec.measurements
    if "boundary" in families:
        rec = family("boundary", lambda: check_boundary(alg, red))
        if rec is not None:
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["boundary"]] = rec.ok()
            measurements["KS_boundary"] = rec.measurements
    if "exchange" in families:
        rec = Recorder("exchange")

        def exchange():
            check_exchange_a(alg, red if red is not None else BlockReduction(alg), rec)
            check_exchange_b(rec, quick=quick)
            return rec
        result = family("exchange", exchange)
        if result is not None:
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["exchange"]] = rec.ok()
            measurements["KS_exchange"] = rec.measurements
    if "functional" in families:
        rec = family("functional", check_functional)
        if rec is not None:
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["functional"]] = rec.ok()
            measurements["KS_functional"] = rec.measurements
    if "emt" in families:
        result = family("emt", lambda: check_emt(alg, red))
        if result is not None:
            rec, own_emt = result
            own.update(own_emt)
            checks.update(rec.checks)
            checks[FAMILY_CHECKS["emt"]] = rec.ok()
            measurements["KS_emt"] = rec.measurements
    table = None
    if build_table:
        start = time.time()
        try:
            table = build_exchange_table(quick=quick)
            worst = table["maxRelativeDeviationFromClosedForm"]
            checks["KS_exchange_tableConsistentWithClosedForm"] = bool(worst < 1e-9)
            measurements["exchangeTable"] = {"maxRelativeDeviationFromClosedForm": worst,
                                             "rows": sum(len(t["rows"]) for t in table["tables"].values()),
                                             "quick": quick}
            if "exchange" in families and FAMILY_CHECKS["exchange"] in checks:
                checks[FAMILY_CHECKS["exchange"]] = checks[FAMILY_CHECKS["exchange"]] and checks["KS_exchange_tableConsistentWithClosedForm"]
        except Exception as error:      # noqa: BLE001
            exceptions["exchangeTable"] = "%s: %s" % (type(error).__name__, error)
            checks["KS_exchange_tableConsistentWithClosedForm"] = False
        timings["exchangeTable"] = round(time.time() - start, 3)
    if theory_path and os.path.exists(theory_path) and red is not None and block_forms is not None \
            and all(k in own for k in ("cValue", "T41", "Ty4", "Ty1")):
        start = time.time()
        try:
            rec = check_wolfram_agreement(alg, red, block_forms, theory_path, own)
            checks.update(rec.checks)
            checks[WOLFRAM_CHECK] = rec.ok()
            measurements["KS_agreesWithWolfram"] = rec.measurements
            measurements["wolframAgreement"] = "compared"
            inputs[relative(theory_path)] = sha256_file(theory_path)
        except Exception as error:      # noqa: BLE001
            exceptions["wolfram"] = "%s: %s" % (type(error).__name__, error)
            checks[WOLFRAM_CHECK] = False
            measurements["wolframAgreement"] = "error"
        timings["wolfram"] = round(time.time() - start, 3)
    else:
        measurements["wolframAgreement"] = "not-run"
        measurements["wolframTheoryExpectedAt"] = relative(theory_path) if theory_path else None
    checks["KS_internal_noException"] = not exceptions
    if exceptions:
        measurements["exceptions"] = exceptions
    measurements["families"] = families
    return checks, measurements, inputs, table, timings


def build_report(checks, measurements, inputs):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    sources = {rel: sha256_file(os.path.join(script_directory, os.path.basename(rel))) for rel in SOURCE_FILES}
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
    parser.add_argument("--table", default=DEFAULT_TABLE, help="exchange-table.json path")
    parser.add_argument("--theory", default=DEFAULT_THEORY, help="Wolfram kohn-sham-theory.json (compared when present)")
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--families", default=",".join(FAMILIES), help="comma-separated subset of %s" % ",".join(FAMILIES))
    parser.add_argument("--no-table", action="store_true", help="do not build the exchange table")
    parser.add_argument("--quick", action="store_true", help="fewer quadrature points (tests)")
    parser.add_argument("--no-write", action="store_true")
    arguments = parser.parse_args(argv)
    families = [f.strip() for f in arguments.families.split(",") if f.strip()]
    unknown = [f for f in families if f not in FAMILIES]
    if unknown:
        print("error=unknown families %s" % ",".join(unknown))
        return 2
    checks, measurements, inputs, table, timings = run_checks(
        fixture_path=arguments.fixture, theory_path=arguments.theory, families=families, quick=arguments.quick,
        build_table=not arguments.no_table)
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
        if table is not None:
            table["sourceSha256"] = report["sourceSha256"]
            with open(arguments.table, "wb") as handle:
                handle.write(canonical_json_bytes(table))
            print("table=%s" % relative(arguments.table))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
