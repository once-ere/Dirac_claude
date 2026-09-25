#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Independent exact checker of the Stage-4 Kohn-Sham theory of dirac16complex in
the static primordial field (sympy + mpmath + standard library; numpy is used
only to tabulate the exchange table quickly and is not needed for any check).

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
