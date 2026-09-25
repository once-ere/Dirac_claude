"""Independent exact checker of dirac16complex in the primordial field (Stage 2).

sympy + standard library only.  Nothing produced by Wolfram is used as truth:
the gamma matrices are rebuilt from CONTRACT section 1 (and merely compared with
the committed exact fixture), the geometry is recomputed from the metric, and
the Wolfram component file (when present) is only compared against.

Field (CONTRACT section 9, notebook MatrixMetric44), zero-based x0..x7,
z = 6 H x0 in (0, pi/2), t = H x4, a4 = a4(t) arbitrary:
    g = diag(cot^2 z, s^(1/3) e^(2 a4) (x3), -1, -s^(1/3) e^(-2 a4) (x3)),
    s = sin z, diagonal vielbein h = (cot z, s^(1/6) e^a4 (x3), 1, s^(1/6) e^-a4 (x3)).

Exactness strategy
  * Scalars (metric, Christoffels, spin connection, curvature) are sympy
    expressions; every identity is reduced to the canonical variables
    w = sin(z)^(1/6) > 0, Cz = cos(z) > 0, Ea = e^(a4) > 0, A1..A4 = a4', ..., a4''''
    and decided exactly (numerator reduced modulo Cz^2 + w^12 - 1).
  * 16x16 identities are proved symbolically in the Clifford algebra Cl(4,4)
    (basis blades gamma^A, A a subset of {0..7}); the notebook matrices are
    verified to be a faithful representation of the blade algebra (all 65536
    blade products and all 255 traces), so a blade identity is a matrix identity.
  * In addition every matrix identity is re-checked with the actual 16x16
    matrices at two exact sample points (sin z = 3/5 and 5/13, s^(1/6) kept as
    an exact radical r with r^6 = sin z, e^(a4) kept as a transcendental E for a
    rational a4), in the exact ring Q(i)(r)[E, 1/E] (field ``QRE`` below).

Prints ``check_<name>=true|false``, ``measurement_<name>=<value>``,
``check_count`` and ``failed_check_count``; exits nonzero on failure and writes
``artifacts/dirac16complex/primordial-field/python-primordial-report.json``.

The default invocation also runs ``P_EL_agreesWithWolfram`` against
``artifacts/dirac16complex/primordial-field/primordial-components.json`` (written
by ``wolframscript -file scripts/verify_dirac16complex_primordial.wls``) and
records ``measurement_wolframAgreement=compared``; if that file is missing the
check is false (``wolframAgreement=missing``) and the exit code is nonzero.
``--allow-missing-wolfram`` restores the standalone mode (the comparison is
skipped and ``wolframAgreement=not-run``).
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from fractions import Fraction

import sympy as sp

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIRECTORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                                  "primordial-field")
DEFAULT_OUTPUT = os.path.join(ARTIFACT_DIRECTORY, "python-primordial-report.json")
DEFAULT_WOLFRAM_COMPONENTS = os.path.join(ARTIFACT_DIRECTORY, "primordial-components.json")
DEFAULT_FIXTURE = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                               "arbitrary-field", "algebra-fixture.json")
PRODUCER = "scripts/check_dirac16complex_primordial.py"
SOURCE_FILES = ("scripts/check_dirac16complex_primordial.py",)

CHECK_NAMES = (
    "P_algebraSetup",
    "P_metric",
    "P_zeta",
    "P_christoffel",
    "P_spinconn",
    "P_Omega",
    "P_gammaConst",
    "P_EL",
    "P_blocks",
    "P_EMT",
    "P_modes",
    "P_einstein",
    "P_source",
    "P_quant",
    "P_a4linear",
)
WOLFRAM_CHECK = "P_EL_agreesWithWolfram"

NOTEBOOK_BLOCKS = ((0, 5, 8, 13), (1, 4, 9, 12), (2, 7, 10, 15), (3, 6, 11, 14))

# Notebook cell 584 stored output (EinsteinG of MatrixMetric44), verbatim from the
# notebook Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
# (Out[536]); cell 583 stored output RS (Out[535]).
NOTEBOOK_CELL584_EINSTEIN_G = (
    "{{-3*H^2*Cot[6*H*x0]^2*(-5 + Derivative[1][a4][H*x4]^2), 0, 0, 0, 0, 0, 0, 0}, "
    "{0, (-E^(2*a4[H*x4]))*H^2*Sin[6*H*x0]^(1/3)*(-15 + 3*Derivative[1][a4][H*x4]^2 - "
    "Derivative[2][a4][H*x4]), 0, 0, 0, 0, 0, 0}, {0, 0, (-E^(2*a4[H*x4]))*H^2*"
    "Sin[6*H*x0]^(1/3)*(-15 + 3*Derivative[1][a4][H*x4]^2 - Derivative[2][a4][H*x4]), "
    "0, 0, 0, 0, 0}, {0, 0, 0, (-E^(2*a4[H*x4]))*H^2*Sin[6*H*x0]^(1/3)*(-15 + "
    "3*Derivative[1][a4][H*x4]^2 - Derivative[2][a4][H*x4]), 0, 0, 0, 0}, {0, 0, 0, 0, "
    "-3*H^2*(7 + Derivative[1][a4][H*x4]^2), 0, 0, 0}, {0, 0, 0, 0, 0, (H^2*"
    "Sin[6*H*x0]^(1/3)*(-15 + 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]))/"
    "E^(2*a4[H*x4]), 0, 0}, {0, 0, 0, 0, 0, 0, (H^2*Sin[6*H*x0]^(1/3)*(-15 + "
    "3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]))/E^(2*a4[H*x4]), 0}, "
    "{0, 0, 0, 0, 0, 0, 0, (H^2*Sin[6*H*x0]^(1/3)*(-15 + 3*Derivative[1][a4][H*x4]^2 + "
    "Derivative[2][a4][H*x4]))/E^(2*a4[H*x4])}}"
)
NOTEBOOK_CELL583_RICCI_SCALAR = "6*H^2*(-7 + Derivative[1][a4][H*x4]^2)"

# Notebook cell 1137 stored output (coupledyZeqs, Out[1116]) and the cell-1111
# relabelling yZ[j] = Z[NOTEBOOK_YZ_TO_Z[j]], Z[k][z, t] = f16[k] = Psi_k.
NOTEBOOK_CELL1137_BLOCK_EQUATIONS = (
    '{{Derivative[0, 1][yZ[0]][z, t] == -3*yZ[1][z, t] - M*yZ[3][z, t] + (Q1*Sinh[a4[t]]*'
    'yZ[0][z, t]*Derivative[1][a4][t])/E^a4[t] - 6*Tan[z]*Derivative[1, 0][yZ[1]][z, t], '
    'Derivative[0, 1][yZ[1]][z, t] == -3*yZ[0][z, t] - M*yZ[2][z, t] - (Q1*Sinh[a4[t]]*yZ'
    '[1][z, t]*Derivative[1][a4][t])/E^a4[t] - 6*Tan[z]*Derivative[1, 0][yZ[0]][z, t], De'
    'rivative[0, 1][yZ[2]][z, t] == M*yZ[1][z, t] + 3*yZ[3][z, t] - (Q1*Sinh[a4[t]]*yZ[2]'
    '[z, t]*Derivative[1][a4][t])/E^a4[t] + 6*Tan[z]*Derivative[1, 0][yZ[3]][z, t], Deriv'
    'ative[0, 1][yZ[3]][z, t] == M*yZ[0][z, t] + 3*yZ[2][z, t] + (Q1*Sinh[a4[t]]*yZ[3][z,'
    ' t]*Derivative[1][a4][t])/E^a4[t] + 6*Tan[z]*Derivative[1, 0][yZ[2]][z, t]}, {Deriva'
    'tive[0, 1][yZ[4]][z, t] == 3*yZ[5][z, t] + M*yZ[7][z, t] + (Q1*Sinh[a4[t]]*yZ[4][z, '
    't]*Derivative[1][a4][t])/E^a4[t] + 6*Tan[z]*Derivative[1, 0][yZ[5]][z, t], Derivativ'
    'e[0, 1][yZ[5]][z, t] == 3*yZ[4][z, t] + M*yZ[6][z, t] - (Q1*Sinh[a4[t]]*yZ[5][z, t]*'
    'Derivative[1][a4][t])/E^a4[t] + 6*Tan[z]*Derivative[1, 0][yZ[4]][z, t], Derivative[0'
    ', 1][yZ[6]][z, t] == (-M)*yZ[5][z, t] - 3*yZ[7][z, t] - (Q1*Sinh[a4[t]]*yZ[6][z, t]*'
    'Derivative[1][a4][t])/E^a4[t] - 6*Tan[z]*Derivative[1, 0][yZ[7]][z, t], Derivative[0'
    ', 1][yZ[7]][z, t] == (-M)*yZ[4][z, t] - 3*yZ[6][z, t] + (Q1*Sinh[a4[t]]*yZ[7][z, t]*'
    'Derivative[1][a4][t])/E^a4[t] - 6*Tan[z]*Derivative[1, 0][yZ[6]][z, t]}, {Derivative'
    '[0, 1][yZ[8]][z, t] == 3*yZ[9][z, t] + M*yZ[11][z, t] + 6*Tan[z]*Derivative[1, 0][yZ'
    '[9]][z, t], Derivative[0, 1][yZ[9]][z, t] == 3*yZ[8][z, t] + M*yZ[10][z, t] + 6*Tan['
    'z]*Derivative[1, 0][yZ[8]][z, t], Derivative[0, 1][yZ[10]][z, t] == (-M)*yZ[9][z, t]'
    ' - 3*(yZ[11][z, t] + 2*Tan[z]*Derivative[1, 0][yZ[11]][z, t]), Derivative[0, 1][yZ[1'
    '1]][z, t] == (-M)*yZ[8][z, t] - 3*(yZ[10][z, t] + 2*Tan[z]*Derivative[1, 0][yZ[10]]['
    'z, t])}, {Derivative[0, 1][yZ[12]][z, t] == -3*yZ[13][z, t] - M*yZ[15][z, t] - 6*Tan'
    '[z]*Derivative[1, 0][yZ[13]][z, t], Derivative[0, 1][yZ[13]][z, t] == -3*yZ[12][z, t'
    '] - M*yZ[14][z, t] - 6*Tan[z]*Derivative[1, 0][yZ[12]][z, t], Derivative[0, 1][yZ[14'
    ']][z, t] == M*yZ[13][z, t] + 3*yZ[15][z, t] + 6*Tan[z]*Derivative[1, 0][yZ[15]][z, t'
    '], Derivative[0, 1][yZ[15]][z, t] == M*yZ[12][z, t] + 3*yZ[14][z, t] + 6*Tan[z]*Deri'
    'vative[1, 0][yZ[14]][z, t]}}'
)
NOTEBOOK_YZ_TO_Z = (0, 5, 8, 13, 1, 4, 9, 12, 2, 7, 10, 15, 3, 6, 11, 14)

# Exact sample points for the 16x16 matrix checks: sin z, cos z rational
# (Pythagorean), a4 and its t-derivatives rational, physical parameters rational.
SAMPLE_POINTS = (
    {"label": "P1", "sinz": "3/5", "cosz": "4/5", "a4": "1/3", "A1": "1/2", "A2": "-2/3",
     "A3": "3/4", "A4": "-1/5", "H": "1", "M": "5/7", "K": "3/2", "k": "2/3", "q": "-1/4",
     "kappa": "1"},
    {"label": "P2", "sinz": "5/13", "cosz": "12/13", "a4": "-2/7", "A1": "-3/5",
     "A2": "4/3", "A3": "-1/6", "A4": "2/9", "H": "3/4", "M": "-1/3", "K": "2/5",
     "k": "-5/4", "q": "7/3", "kappa": "3/2"},
)

ETA = (1, 1, 1, 1, -1, -1, -1, -1)
SPACE = (1, 2, 3)          # transverse positive-norm directions (3-space)
EXTRA_TIMES = (5, 6, 7)    # transverse negative-norm directions
TRANSVERSE6 = SPACE + EXTRA_TIMES


# ---------------------------------------------------------------------------
# 1. Gamma matrices (CONTRACT section 1), rebuilt from scratch
# ---------------------------------------------------------------------------

def _levi_civita(sequence):
    values = list(sequence)
    if len(set(values)) != len(values):
        return 0
    sign = 1
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                sign = -sign
    return sign


def _zeros(rows, cols):
    return [[0] * cols for _ in range(rows)]


def _eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def _matmul(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    out = _zeros(rows, cols)
    for i in range(rows):
        row = a[i]
        for k in range(inner):
            v = row[k]
            if v:
                bk = b[k]
                for j in range(cols):
                    if bk[j]:
                        out[i][j] += v * bk[j]
    return out


def _transpose(a):
    return [list(r) for r in zip(*a)]


def _neg(a):
    return [[-v for v in row] for row in a]


def _blocks(tl, tr, bl, br):
    n = len(tl)
    top = [tl[i] + tr[i] for i in range(n)]
    bottom = [bl[i] + br[i] for i in range(n)]
    return top + bottom


def notebook_tau():
    """tau[0..7] (8x8 integer) exactly as the notebook / CONTRACT section 1."""
    def qa(h, p, q):
        return _levi_civita((h, p, q, 4))

    def qb(h, p, q):
        return (1 if (p == 4 and q == h) else 0) - (1 if (p == h and q == 4) else 0)

    s4 = {h: [[qa(h, p, q) - qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]
          for h in (1, 2, 3)}
    t4 = {h: [[qa(h, p, q) + qb(h, p, q) for q in range(1, 5)] for p in range(1, 5)]
          for h in (1, 2, 3)}
    z4 = _zeros(4, 4)
    tau = {0: _eye(8)}
    for h in (1, 2, 3):
        tau[7 - h] = _blocks(z4, t4[h], _neg(t4[h]), z4)
    for h in (1, 2, 3):
        tau[h] = _blocks(z4, s4[h], s4[h], z4)
    product = _eye(8)
    for a in range(1, 7):
        product = _matmul(product, tau[a])
    tau[7] = product
    return [tau[a] for a in range(8)]


def notebook_gammas():
    """Returns (gamma[0..7], C, tau, taubar, sigma8) as dense integer matrices."""
    tau = notebook_tau()
    z4 = _zeros(4, 4)
    sigma = _blocks(z4, _eye(4), _eye(4), z4)
    taubar = [_eye(8)] + [_matmul(_matmul(sigma, _transpose(tau[a])), sigma)
                          for a in range(1, 8)]
    z8 = _zeros(8, 8)
    gamma = [_blocks(z8, taubar[a], tau[a], z8) for a in range(8)]
    charge = _blocks(_neg(sigma), z8, z8, sigma)
    return gamma, charge, tau, taubar, sigma


def signed_permutation(matrix):
    """(perm, signs) if every row has exactly one entry +-1, else None."""
    perm, signs = [], []
    for row in matrix:
        nonzero = [(j, v) for j, v in enumerate(row) if v]
        if len(nonzero) != 1 or nonzero[0][1] not in (1, -1):
            return None
        perm.append(nonzero[0][0])
        signs.append(nonzero[0][1])
    return tuple(perm), tuple(signs)


def sp_mul(p, q):
    pp, ps = p
    qp, qs = q
    return (tuple(qp[pp[i]] for i in range(len(pp))),
            tuple(ps[i] * qs[pp[i]] for i in range(len(pp))))


def sp_dense(p):
    perm, signs = p
    n = len(perm)
    out = _zeros(n, n)
    for i in range(n):
        out[i][perm[i]] = signs[i]
    return out


# ---------------------------------------------------------------------------
# 2. Clifford algebra Cl(4,4) in the blade basis
# ---------------------------------------------------------------------------

def _popcount(x):
    return bin(x).count("1")


_SIGN_CACHE = {}


def blade_sign(a, b):
    """gamma^A gamma^B = blade_sign(A,B) gamma^(A xor B) (ascending-order blades)."""
    key = (a, b)
    cached = _SIGN_CACHE.get(key)
    if cached is not None:
        return cached
    swaps = 0
    x = a >> 1
    while x:
        swaps += _popcount(x & b)
        x >>= 1
    sign = -1 if swaps & 1 else 1
    common = a & b
    for c in range(8):
        if (common >> c) & 1:
            sign *= ETA[c]
    _SIGN_CACHE[key] = sign
    return sign


def blade_label(mask):
    if mask == 0:
        return "1"
    return "*".join("g%d" % c for c in range(8) if (mask >> c) & 1)


def blade_dagger_sign(mask):
    """(gamma^A)^dagger = blade_dagger_sign(A) gamma^A for the notebook matrices
    (gamma^a real, symmetric for a<4, antisymmetric for a>=4)."""
    k = _popcount(mask)
    sign = -1 if (k * (k - 1) // 2) % 2 else 1
    for c in range(4, 8):
        if (mask >> c) & 1:
            sign = -sign
    return sign


def cl(mask, coefficient=1):
    return {mask: coefficient}


def cl_add(*elements):
    out = {}
    for element in elements:
        for mask, c in element.items():
            out[mask] = out[mask] + c if mask in out else c
    return out


def cl_scale(element, factor):
    return {mask: factor * c for mask, c in element.items()}


def cl_sub(x, y):
    return cl_add(x, cl_scale(y, -1))


def cl_mul(x, y):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            term = ca * cb
            if blade_sign(a, b) < 0:
                term = -term
            key = a ^ b
            out[key] = out[key] + term if key in out else term
    return out


def cl_mul_all(*elements):
    out = {0: sp.Integer(1)}
    for element in elements:
        out = cl_mul(out, element)
    return out


def cl_comm(x, y):
    return cl_sub(cl_mul(x, y), cl_mul(y, x))


def cl_anti(x, y):
    return cl_add(cl_mul(x, y), cl_mul(y, x))


def cl_dagger(element, conj):
    return {mask: blade_dagger_sign(mask) * conj(c) for mask, c in element.items()}


def gamma_blade(a, coefficient=1):
    return {1 << a: coefficient}


CHARGE_MASK = 0b00001111   # C = gamma^0 gamma^1 gamma^2 gamma^3
CHIRALITY_MASK = 0b11111111  # gamma^8 = gamma^0 ... gamma^7


# ---------------------------------------------------------------------------
# 3. Symbolic scalars: canonical variables and exact zero test
# ---------------------------------------------------------------------------

H = sp.Symbol("H", positive=True)
XS = sp.symbols("x0:8", real=True)
X0, X4 = XS[0], XS[4]
FX4 = sp.Function("F")(X4)          # F(x4) := a4(H x4)
ZARG = 6 * H * X0
W, CZ, EA = sp.symbols("w Cz Ea", positive=True)
A1, A2, A3, A4 = sp.symbols("A1 A2 A3 A4", real=True)
ADER = {1: A1, 2: A2, 3: A3, 4: A4}
MASS, LAM, KZ, KMOM, QMOM, KAPPA = sp.symbols("m lam K k q kappa", real=True)
SSYM = sp.Symbol("S", real=True)    # the scalar bilinear Psibar Psi in U'(S) = lam S
CANON_RELATION = CZ ** 2 + W ** 12 - 1

# readable symbols used for the closed forms
ZS = sp.Symbol("z", positive=True)
TS = sp.Symbol("t", real=True)
A4R = sp.Function("a4")(TS)
ZETA = sp.Symbol("zeta", real=True)


def canon_x(expression):
    """x-form (x0, x4, F(x4)) -> canonical variables."""
    e = sp.sympify(expression)
    e = e.subs({sp.cot(ZARG): sp.cos(ZARG) / sp.sin(ZARG),
                sp.tan(ZARG): sp.sin(ZARG) / sp.cos(ZARG),
                sp.csc(ZARG): 1 / sp.sin(ZARG), sp.sec(ZARG): 1 / sp.cos(ZARG)})
    for n in (4, 3, 2, 1):
        e = e.subs(sp.Derivative(FX4, (X4, n)), H ** n * ADER[n])
    e = e.subs(FX4, sp.log(EA))
    e = e.subs({sp.sin(ZARG): W ** 6, sp.cos(ZARG): CZ})
    return sp.expand_power_exp(e)


def canon_r(expression):
    """readable form (z, t, a4(t), zeta) -> canonical variables."""
    e = sp.sympify(expression)
    e = e.subs({sp.tan(ZS): sp.sin(ZS) / sp.cos(ZS), sp.cot(ZS): sp.cos(ZS) / sp.sin(ZS),
                sp.csc(ZS): 1 / sp.sin(ZS), sp.sec(ZS): 1 / sp.cos(ZS)})
    for n in (4, 3, 2, 1):
        e = e.subs(sp.Derivative(A4R, (TS, n)), ADER[n])
    e = e.subs(A4R, sp.log(EA))
    e = e.subs(ZETA, sp.log(W) / H)
    e = e.subs({sp.sin(ZS): W ** 6, sp.cos(ZS): CZ})
    return sp.expand_power_exp(e)


def to_readable(expression):
    e = sp.sympify(expression)
    e = e.subs({A4: sp.Derivative(A4R, (TS, 4)), A3: sp.Derivative(A4R, (TS, 3)),
                A2: sp.Derivative(A4R, (TS, 2)), A1: sp.Derivative(A4R, TS)})
    e = e.subs({EA: sp.exp(A4R), CZ: sp.cos(ZS), W: sp.sin(ZS) ** sp.Rational(1, 6)})
    return e


def is_zero(expression):
    """Exact zero test for an expression in canonical variables."""
    e = sp.sympify(expression)
    if e == 0:
        return True
    numerator, _ = sp.fraction(sp.together(e))
    numerator = sp.expand(numerator)
    if numerator == 0:
        return True
    if numerator.has(CZ):
        numerator = sp.expand(sp.rem(numerator, CANON_RELATION, CZ))
    return numerator == 0


def equal(a, b):
    return is_zero(sp.sympify(a) - sp.sympify(b))


def reduced(expression):
    """Canonical-variable expression with the numerator reduced mod Cz^2+w^12-1."""
    numerator, denominator = sp.fraction(sp.together(sp.sympify(expression)))
    numerator = sp.expand(numerator)
    if numerator.has(CZ):
        numerator = sp.expand(sp.rem(numerator, CANON_RELATION, CZ))
    return sp.factor(numerator) / sp.factor(denominator)


def d0(expression):
    """d/dx0 on canonical variables (x0 enters through w and Cz only)."""
    e = sp.sympify(expression)
    return 6 * H * (sp.diff(e, W) * CZ / (6 * W ** 5) - sp.diff(e, CZ) * W ** 6)


def d4(expression):
    """d/dx4 on canonical variables (x4 enters through Ea and A1..A3)."""
    e = sp.sympify(expression)
    return H * (sp.diff(e, EA) * EA * A1 + sp.diff(e, A1) * A2 + sp.diff(e, A2) * A3
                + sp.diff(e, A3) * A4)


def conj_canon(expression):
    """Complex conjugation: every canonical symbol and parameter is real."""
    return sp.sympify(expression).subs(sp.I, -sp.I)


def cl_is_zero(element):
    return all(is_zero(c) for c in element.values())


def cl_equal(x, y):
    return cl_is_zero(cl_sub(x, y))


def cl_clean(element):
    return {mask: c for mask, c in element.items() if not is_zero(c)}


def cl_text(element, readable=True):
    parts = []
    for mask in sorted(element):
        c = reduced(element[mask])
        if c == 0:
            continue
        c = to_readable(c) if readable else c
        parts.append("(%s)*%s" % (sp.sstr(c), blade_label(mask)))
    return " + ".join(parts) if parts else "0"


def expr_text(expression):
    return sp.sstr(expression)


def cl_d0(element):
    return {mask: d0(c) for mask, c in element.items()}


def cl_d4(element):
    return {mask: d4(c) for mask, c in element.items()}


# ---------------------------------------------------------------------------
# 4. Exact sample-point ring Q(i)(r)[E, 1/E], r^6 = sin z, E = e^(a4)
# ---------------------------------------------------------------------------

class QRE:
    """Exact element sum c_{k,n,j} r^k E^n i^j with k in 0..5, n in Z, j in {0,1}.

    r = sin(z)^(1/6) with r^6 = s0 rational and x^6 - s0 irreducible over Q
    (Eisenstein for the sample values), E = exp(a4) with a4 rational nonzero,
    transcendental over the algebraic numbers (Lindemann-Weierstrass), i^2 = -1.
    Hence the monomials are linearly independent over Q and the zero test (all
    coefficients zero) is exact in both directions."""

    __slots__ = ("terms", "s0")

    def __init__(self, terms, s0):
        self.terms = {key: value for key, value in terms.items() if value != 0}
        self.s0 = s0

    @classmethod
    def const(cls, value, s0):
        return cls({(0, 0, 0): Fraction(value)}, s0)

    def _coerce(self, other):
        if isinstance(other, QRE):
            return other
        return QRE.const(other, self.s0)

    def __add__(self, other):
        other = self._coerce(other)
        terms = dict(self.terms)
        for key, value in other.terms.items():
            terms[key] = terms.get(key, 0) + value
        return QRE(terms, self.s0)

    __radd__ = __add__

    def __neg__(self):
        return QRE({key: -value for key, value in self.terms.items()}, self.s0)

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        terms = {}
        for (k1, n1, j1), v1 in self.terms.items():
            for (k2, n2, j2), v2 in other.terms.items():
                value = v1 * v2
                k, n, j = k1 + k2, n1 + n2, j1 + j2
                if k >= 6:
                    k -= 6
                    value *= self.s0
                if j >= 2:
                    j -= 2
                    value = -value
                key = (k, n, j)
                terms[key] = terms.get(key, 0) + value
        return QRE(terms, self.s0)

    __rmul__ = __mul__

    def is_zero(self):
        return not self.terms

    def inverse(self):
        if len(self.terms) != 1:
            raise ValueError("only monomials are inverted in the sample ring")
        (k, n, j), value = next(iter(self.terms.items()))
        coefficient = Fraction(1) / value
        if k:
            k = 6 - k
            coefficient /= self.s0
        if j:
            coefficient = -coefficient
        return QRE({(k, -n, j): coefficient}, self.s0)

    def conj(self):
        return QRE({(k, n, j): (-v if j else v) for (k, n, j), v in self.terms.items()},
                   self.s0)

    def __eq__(self, other):
        return (self - other).is_zero()

    def __hash__(self):  # pragma: no cover - not used as a key
        return hash(tuple(sorted(self.terms.items())))


def sample_environment(point):
    s0 = Fraction(point["sinz"])
    c0 = Fraction(point["cosz"])
    if s0 * s0 + c0 * c0 != 1 or not (0 < s0 < 1 and 0 < c0 < 1):
        raise ValueError("sample point is not on the unit circle in (0, pi/2)")
    env = {
        W: QRE({(1, 0, 0): Fraction(1)}, s0),
        CZ: QRE.const(c0, s0),
        EA: QRE({(0, 1, 0): Fraction(1)}, s0),
    }
    for name, symbol in (("A1", A1), ("A2", A2), ("A3", A3), ("A4", A4), ("H", H),
                         ("M", MASS), ("K", KZ), ("k", KMOM), ("q", QMOM),
                         ("kappa", KAPPA)):
        env[symbol] = QRE.const(Fraction(point[name]), s0)
    env[LAM] = QRE.const(0, s0)
    return env, s0


def to_qre(expression, env, s0):
    e = sp.sympify(expression)
    if e.is_Rational:
        return QRE.const(Fraction(int(e.p), int(e.q)), s0)
    if e == sp.I:
        return QRE({(0, 0, 1): Fraction(1)}, s0)
    if e.is_Symbol:
        return env[e]
    if e.is_Add:
        total = QRE.const(0, s0)
        for arg in e.args:
            total = total + to_qre(arg, env, s0)
        return total
    if e.is_Mul:
        total = QRE.const(1, s0)
        for arg in e.args:
            total = total * to_qre(arg, env, s0)
        return total
    if e.is_Pow and e.exp.is_Integer:
        base = to_qre(e.base, env, s0)
        n = int(e.exp)
        if n < 0:
            base = base.inverse()
            n = -n
        result = QRE.const(1, s0)
        for _ in range(n):
            result = result * base
        return result
    raise ValueError("cannot evaluate %r in the sample ring" % (e,))


# sparse 16x16 matrices over QRE: {(i, j): QRE}

def qm_from_int(dense, s0):
    return {(i, j): QRE.const(v, s0) for i, row in enumerate(dense)
            for j, v in enumerate(row) if v}


def qm_add(*matrices):
    out = {}
    for matrix in matrices:
        for key, value in matrix.items():
            out[key] = out[key] + value if key in out else value
    return {key: value for key, value in out.items() if not value.is_zero()}


def qm_scale(matrix, factor):
    return {key: value * factor for key, value in matrix.items()
            if not (value * factor).is_zero()}


def qm_sub(a, b):
    return qm_add(a, {key: -value for key, value in b.items()})


def qm_mul(a, b):
    rows = {}
    for (k, j), value in b.items():
        rows.setdefault(k, []).append((j, value))
    out = {}
    for (i, k), value in a.items():
        for j, bv in rows.get(k, ()):
            product = value * bv
            out[(i, j)] = out[(i, j)] + product if (i, j) in out else product
    return {key: value for key, value in out.items() if not value.is_zero()}


def qm_dagger(matrix):
    return {(j, i): value.conj() for (i, j), value in matrix.items()}


def qm_is_zero(matrix):
    return all(value.is_zero() for value in matrix.values())


def qm_identity(s0, factor=1):
    return {(i, i): QRE.const(factor, s0) for i in range(16)}


# ---------------------------------------------------------------------------
# 5. Context: algebra and symbolic geometry of the primordial field
# ---------------------------------------------------------------------------

class Context:
    def __init__(self):
        start = time.time()
        (self.gamma, self.charge, self.tau, self.taubar,
         self.sigma8) = notebook_gammas()
        self.gamma_sp = [signed_permutation(g) for g in self.gamma]
        self.charge_sp = signed_permutation(self.charge)
        self._build_blade_matrices()
        self._build_geometry()
        self.timing_context = time.time() - start

    # -- algebra -----------------------------------------------------------
    def _build_blade_matrices(self):
        identity = (tuple(range(16)), (1,) * 16)
        self.blade_sp = {}
        for mask in range(256):
            p = identity
            for c in range(8):
                if (mask >> c) & 1:
                    p = sp_mul(p, self.gamma_sp[c])
            self.blade_sp[mask] = p

    def blade_dense(self, mask):
        return sp_dense(self.blade_sp[mask])

    # -- geometry ------------------------------------------------------------
    def _build_geometry(self):
        sn, cs = sp.sin(ZARG), sp.cos(ZARG)
        sixth = sp.Rational(1, 6)
        self.h_x = ([cs / sn] + [sn ** sixth * sp.exp(FX4)] * 3 + [sp.Integer(1)]
                    + [sn ** sixth * sp.exp(-FX4)] * 3)
        # contract metric, written independently of the vielbein
        third = sp.Rational(1, 3)
        self.g_contract = ([sp.cot(ZARG) ** 2] + [sn ** third * sp.exp(2 * FX4)] * 3
                           + [sp.Integer(-1)] + [-sn ** third * sp.exp(-2 * FX4)] * 3)
        self.e_x = [[self.h_x[m] if m == a else sp.Integer(0) for a in range(8)]
                    for m in range(8)]
        eta = [[ETA[a] if a == b else 0 for b in range(8)] for a in range(8)]
        self.g_x = [[sum(self.e_x[m][a] * eta[a][b] * self.e_x[n][b]
                         for a in range(8) for b in range(8)) for n in range(8)]
                    for m in range(8)]
        self.ginv_x = [[(1 / self.g_x[m][m]) if m == n else sp.Integer(0)
                        for n in range(8)] for m in range(8)]
        self.einv_x = [[(1 / self.h_x[m]) if m == a else sp.Integer(0) for m in range(8)]
                       for a in range(8)]  # einv[a][mu] = e_a^mu
        g, gi = self.g_x, self.ginv_x
        gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for r in range(8):
            for m in range(8):
                for n in range(8):
                    total = sp.Integer(0)
                    for s in range(8):
                        if gi[r][s] == 0:
                            continue
                        total += sp.Rational(1, 2) * gi[r][s] * (
                            sp.diff(g[n][s], XS[m]) + sp.diff(g[m][s], XS[n])
                            - sp.diff(g[m][n], XS[s]))
                    gam[r][m][n] = total
        self.Gamma_x = gam
        self.Gamma = [[[canon_x(gam[r][m][n]) for n in range(8)] for m in range(8)]
                      for r in range(8)]
        e, ei = self.e_x, self.einv_x
        om = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for m in range(8):
            for a in range(8):
                for b in range(8):
                    total = sp.Integer(0)
                    for n in range(8):
                        if ei[b][n] == 0:
                            continue
                        inner = sum(gam[r][m][n] * e[r][a] for r in range(8))
                        total += ei[b][n] * (inner - sp.diff(e[n][a], XS[m]))
                    om[m][a][b] = total
        self.omega_mixed_x = om
        self.omega_mixed = [[[canon_x(om[m][a][b]) for b in range(8)] for a in range(8)]
                            for m in range(8)]
        self.omega = [[[ETA[a] * self.omega_mixed[m][a][b] for b in range(8)]
                       for a in range(8)] for m in range(8)]  # omega_{mu ab}
        self.h = [canon_x(v) for v in self.h_x]
        self.g = [canon_x(self.g_x[m][m]) for m in range(8)]
        self.ginv = [canon_x(self.ginv_x[m][m]) for m in range(8)]
        self.einv = [canon_x(1 / self.h_x[m]) for m in range(8)]
        # d_mu e_a^nu (diagonal): de_inv[mu][nu] = d_mu (1/h_nu)
        self.d_einv = [[canon_x(sp.diff(1 / self.h_x[n], XS[m])) for n in range(8)]
                       for m in range(8)]
        # Clifford objects
        self.gamma_up = [gamma_blade(n, self.einv[n]) for n in range(8)]   # gamma^mu
        self.gamma_down = [gamma_blade(n, ETA[n] * self.h[n]) for n in range(8)]
        self.Omega = [self._omega_blades(self.omega[m]) for m in range(8)]
        self.Omega_notebook = [self._omega_blades(self.omega_mixed[m]) for m in range(8)]

    @staticmethod
    def _omega_blades(omega_ab):
        """(1/2) sum_{a,b} w_ab S^{ab}, S^{ab} = (1/2) gamma^a gamma^b (a != b)."""
        out = {}
        for a in range(8):
            for b in range(8):
                if a == b or omega_ab[a][b] == 0:
                    continue
                c = sp.Rational(1, 4) * omega_ab[a][b] * blade_sign(1 << a, 1 << b)
                key = (1 << a) | (1 << b)
                out[key] = out[key] + c if key in out else c
        return out


# ---------------------------------------------------------------------------
# 6. Closed forms (hand-derived; each is verified against the general formulas)
# ---------------------------------------------------------------------------

S16 = sp.sin(ZS) ** sp.Rational(1, 6)
S13 = sp.sin(ZS) ** sp.Rational(1, 3)
A4P = sp.Derivative(A4R, TS)
A4PP = sp.Derivative(A4R, (TS, 2))


def eps_sign(i):
    return 1 if i in SPACE else -1


def closed_christoffel():
    """dict (rho, mu, nu) -> readable closed form (all nonzero ordered entries)."""
    out = {(0, 0, 0): -6 * H / (sp.sin(ZS) * sp.cos(ZS))}
    for i in TRANSVERSE6:
        out[(i, 0, i)] = H * sp.cot(ZS)
        out[(i, i, 0)] = H * sp.cot(ZS)
        out[(i, 4, i)] = eps_sign(i) * H * A4P
        out[(i, i, 4)] = eps_sign(i) * H * A4P
        out[(0, i, i)] = -eps_sign(i) * H * sp.tan(ZS) * S13 * sp.exp(2 * eps_sign(i) * A4R)
        out[(4, i, i)] = H * A4P * S13 * sp.exp(2 * eps_sign(i) * A4R)
    return out


def closed_omega():
    """dict (mu, a, b) -> readable closed form of omega_{mu ab} (24 entries)."""
    out = {}
    for i in TRANSVERSE6:
        ei = eps_sign(i)
        v0 = ei * H * S16 * sp.exp(ei * A4R)
        v4 = H * A4P * S16 * sp.exp(ei * A4R)
        out[(i, i, 0)] = v0
        out[(i, 0, i)] = -v0
        out[(i, i, 4)] = v4
        out[(i, 4, i)] = -v4
    return out


def closed_coefficients():
    """c_mu in gamma^mu d_mu = sum_mu c_mu gamma^(a=mu) d_mu (x0 form)."""
    return ([sp.tan(ZS)] + [S16 ** -1 * sp.exp(-A4R)] * 3 + [sp.Integer(1)]
            + [S16 ** -1 * sp.exp(A4R)] * 3)


def closed_coefficients_zeta():
    """Same operator with d_0 = cot z d_zeta: c_zeta = 1, s^(-1/6) = e^(-H zeta)."""
    return ([sp.Integer(1)] + [sp.exp(-H * ZETA - A4R)] * 3 + [sp.Integer(1)]
            + [sp.exp(-H * ZETA + A4R)] * 3)


def closed_einstein_mixed():
    return ([-3 * H ** 2 * (A4P ** 2 - 5)] + [H ** 2 * (15 - 3 * A4P ** 2 + A4PP)] * 3
            + [3 * H ** 2 * (7 + A4P ** 2)] + [H ** 2 * (15 - 3 * A4P ** 2 - A4PP)] * 3)


def closed_ricci_scalar():
    return 6 * H ** 2 * (A4P ** 2 - 7)


def closed_anticommutators():
    """dict (mu, nu), mu <= nu -> Clifford element of {g_mu,W_nu}+{g_nu,W_mu}."""
    out = {}
    for i in TRANSVERSE6:
        ei = eps_sign(i)
        w0 = ei * H * S16 * sp.exp(ei * A4R)
        w4 = H * A4P * S16 * sp.exp(ei * A4R)
        mask = (1 << 0) | (1 << i) | (1 << 4)
        # gamma^0 gamma^i gamma^4 = sign * blade(0,i,4)
        s_0i4 = blade_sign(1 << 0, 1 << i) * blade_sign((1 << 0) | (1 << i), 1 << 4)
        out[(0, i)] = {mask: canon_r(sp.cot(ZS) * w4) * s_0i4}
        out[tuple(sorted((4, i)))] = {mask: canon_r(w0) * s_0i4}
    for i in SPACE:
        for j in EXTRA_TIMES:
            mask = (1 << i) | (1 << j) | (1 << 4)
            s_ij4 = blade_sign(1 << i, 1 << j) * blade_sign((1 << i) | (1 << j), 1 << 4)
            out[(i, j)] = {mask: canon_r(2 * H * A4P * S13) * s_ij4}
    return out


# ---------------------------------------------------------------------------
# 7. Checks
# ---------------------------------------------------------------------------

def _load_fixture_gammas(path):
    if not path or not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)

    def as_int(value):
        return int(Fraction(value)) if Fraction(value).denominator == 1 else None

    try:
        gammas = [[[as_int(v) for v in row] for row in matrix] for matrix in document["gamma"]]
        charge = [[as_int(v) for v in row] for row in document["C"]]
    except (KeyError, TypeError, ValueError):
        return "malformed"
    return gammas, charge


def check_algebra_setup(ctx, fixture_path=DEFAULT_FIXTURE):
    m = {}
    gamma = ctx.gamma
    identity = _eye(16)
    clifford = True
    for a in range(8):
        for b in range(8):
            anti = [[x + y for x, y in zip(r1, r2)]
                    for r1, r2 in zip(_matmul(gamma[a], gamma[b]), _matmul(gamma[b], gamma[a]))]
            expected = [[2 * ETA[a] * v if a == b else 0 for v in row] for row in identity]
            clifford = clifford and anti == expected
    m["cliffordRelations"] = clifford
    m["gammaSignedPermutations"] = all(p is not None for p in ctx.gamma_sp)
    product = _eye(16)
    for a in range(4):
        product = _matmul(product, gamma[a])
    m["chargeIsGamma0123"] = product == ctx.charge
    chirality = ctx.blade_dense(CHIRALITY_MASK)
    m["chiralityDiagonal"] = [chirality[i][i] for i in range(16)]
    chirality_ok = chirality == [[(-1 if i < 8 else 1) if i == j else 0 for j in range(16)]
                                 for i in range(16)]
    # faithful blade representation: M_A M_B = sign(A,B) M_(A^B), Tr M_A = 0 (A != 0)
    rep_ok = True
    for a in range(256):
        pa = ctx.blade_sp[a]
        for b in range(256):
            prod = sp_mul(pa, ctx.blade_sp[b])
            target = ctx.blade_sp[a ^ b]
            s = blade_sign(a, b)
            if prod[0] != target[0] or any(x != s * y for x, y in zip(prod[1], target[1])):
                rep_ok = False
                break
        if not rep_ok:
            break
    traces_ok = all(sum(sg for i, (pi, sg) in enumerate(zip(*ctx.blade_sp[a])) if pi == i) == 0
                    for a in range(1, 256))
    m["bladeProductsVerified"] = 65536 if rep_ok else "failed"
    m["bladeTracesZero"] = traces_ok
    dagger_ok = all(
        _transpose(ctx.blade_dense(a)) == [[blade_dagger_sign(a) * v for v in row]
                                           for row in ctx.blade_dense(a)]
        for a in range(256))
    m["bladeDaggerSigns"] = dagger_ok
    fixture = _load_fixture_gammas(fixture_path)
    if fixture is None:
        m["fixtureAgreement"] = "not-run"
        fixture_ok = True
    elif fixture == "malformed":
        m["fixtureAgreement"] = False
        fixture_ok = False
    else:
        fixture_ok = fixture[0] == ctx.gamma and fixture[1] == ctx.charge
        m["fixtureAgreement"] = fixture_ok
    ok = (clifford and m["gammaSignedPermutations"] and m["chargeIsGamma0123"]
          and chirality_ok and rep_ok and traces_ok and dagger_ok and fixture_ok)
    return ok, {"P_algebraSetup": m}


def check_metric(ctx):
    m = {}
    ok_components = all(equal(canon_x(ctx.g_x[a][b]),
                              canon_x(ctx.g_contract[a]) if a == b else 0)
                        for a in range(8) for b in range(8))
    m["eEtaET_equals_contractMetric"] = ok_components
    signs = []
    for a in range(8):
        value = sp.factor(ctx.g[a])       # unreduced: products of positive symbols
        if value.is_positive:
            signs.append(1)
        elif value.is_negative:
            signs.append(-1)
        else:
            signs.append(0)
    m["diagonalSigns"] = signs
    signature = (signs.count(1), signs.count(-1))
    m["signature"] = list(signature)
    det = sp.Integer(1)
    for a in range(8):
        det *= ctx.g[a]
    det_ok = equal(det, CZ ** 2)
    m["detG"] = "cos(z)**2" if det_ok else sp.sstr(to_readable(reduced(det)))
    m["detGSign"] = "positive (even number, 4, of negative eigenvalues)"
    m["sqrtAbsDetG"] = "cos(z)" if det_ok else "mismatch"
    m["sqrtAbsDetG_x4Independent"] = is_zero(d4(CZ))
    inverse_ok = all(equal(ctx.g[a] * ctx.ginv[a], 1) for a in range(8))
    m["inverseMetric"] = inverse_ok
    m["specStatementNote"] = ("STAGE2_SPEC P_metric writes 'det g = -cos^2 z (...)'; the "
                              "measured determinant is +cos^2 z (signature (4,4) has an "
                              "even number of negative entries); sqrt|g| = cos z holds.")
    ok = ok_components and signature == (4, 4) and det_ok and inverse_ok
    return ok, {"P_metric": m}


def check_zeta(ctx):
    m = {}
    zeta_x = sp.log(sp.sin(ZARG)) / (6 * H)
    dzeta = sp.diff(zeta_x, X0)
    ok_dzeta = equal(canon_x(dzeta), CZ / W ** 6)           # d zeta/dx0 = cot z
    ok_gzz = equal(canon_x(dzeta ** 2), ctx.g[0])            # dzeta^2 = g_00 dx0^2
    warp = sp.exp(2 * H * zeta_x)
    ok_warp = equal(canon_x(warp), W ** 2)                  # e^{2 H zeta} = s^(1/3)
    ok_space = all(equal(canon_x(warp * sp.exp(2 * FX4)), ctx.g[i]) for i in SPACE)
    ok_time = all(equal(canon_x(-warp * sp.exp(-2 * FX4)), ctx.g[i]) for i in EXTRA_TIMES)
    lim0 = sp.limit(sp.log(sp.sin(ZS)) / (6 * H), ZS, 0, "+")
    lim1 = sp.log(sp.sin(sp.pi / 2)) / (6 * H)
    ok_range = lim0 == -sp.oo and sp.simplify(lim1) == 0
    ok_monotone = bool((CZ / W ** 6).is_positive)  # d zeta/dx0 = cot z > 0 on (0, pi/2)
    sqrtg_zeta = canon_x(sp.cos(ZARG)) / (CZ / W ** 6)       # sqrt|g| dx0 = sqrt|g_zeta| dzeta
    ok_sqrtg = equal(sqrtg_zeta, W ** 6)
    m["zeta"] = "zeta = log(sin(z))/(6*H)"
    m["dzeta_dx0"] = "cot(z)" if ok_dzeta else "mismatch"
    m["warpedMetric"] = ("ds^2 = dzeta^2 - dx4^2 + exp(2*H*zeta)*(exp(2*a4)*(dx1^2+dx2^2+dx3^2)"
                         " - exp(-2*a4)*(dx5^2+dx6^2+dx7^2))")
    m["zetaRange"] = "(-oo, 0)" if ok_range else "mismatch"
    m["sqrtAbsDetG_zetaCoordinates"] = "exp(6*H*zeta) = sin(z)" if ok_sqrtg else "mismatch"
    ok = (ok_dzeta and ok_gzz and ok_warp and ok_space and ok_time and ok_range and ok_sqrtg
          and ok_monotone)
    m["componentsVerified"] = {"g_zetazeta": ok_gzz, "warpFactor": ok_warp,
                               "space": ok_space, "extraTimes": ok_time,
                               "monotone": ok_monotone}
    return ok, {"P_zeta": m}


def _chr_label(r, mu, nu):
    return "Gamma^%d_{%d%d}" % (r, mu, nu)


def check_christoffel(ctx):
    m = {}
    closed = closed_christoffel()
    nonzero = [(r, mu, nu) for r in range(8) for mu in range(8) for nu in range(8)
               if not is_zero(ctx.Gamma[r][mu][nu])]
    matches = all(equal(ctx.Gamma[r][mu][nu], canon_r(closed.get((r, mu, nu), 0)))
                  for r in range(8) for mu in range(8) for nu in range(8))
    symmetric = all(equal(ctx.Gamma[r][mu][nu], ctx.Gamma[r][nu][mu])
                    for r in range(8) for mu in range(8) for nu in range(mu + 1, 8))
    # d0, d4 derivations agree with sympy's own differentiation (used later)
    derivations = all(equal(d0(ctx.Gamma[r][mu][nu]),
                            canon_x(sp.diff(ctx.Gamma_x[r][mu][nu], X0)))
                      and equal(d4(ctx.Gamma[r][mu][nu]),
                                canon_x(sp.diff(ctx.Gamma_x[r][mu][nu], X4)))
                      for (r, mu, nu) in nonzero)
    independent = [(r, mu, nu) for (r, mu, nu) in nonzero if mu <= nu]
    m["nonzeroOrderedCount"] = len(nonzero)
    m["nonzeroIndependentCount"] = len(independent)
    m["closedFormsMatch"] = matches
    m["lowerIndexSymmetry"] = symmetric
    m["derivationsConsistent"] = derivations
    m["list"] = ["%s = %s" % (_chr_label(r, mu, nu), expr_text(closed[(r, mu, nu)]))
                 for (r, mu, nu) in independent]
    ok = matches and symmetric and derivations and len(nonzero) == 37 and len(independent) == 25
    return ok, {"P_christoffel": m}


def check_spinconn(ctx):
    m = {}
    closed = closed_omega()
    nonzero = [(mu, a, b) for mu in range(8) for a in range(8) for b in range(8)
               if not is_zero(ctx.omega[mu][a][b])]
    matches = all(equal(ctx.omega[mu][a][b], canon_r(closed.get((mu, a, b), 0)))
                  for mu in range(8) for a in range(8) for b in range(8))
    antisym = all(is_zero(ctx.omega[mu][a][b] + ctx.omega[mu][b][a])
                  for mu in range(8) for a in range(8) for b in range(8))
    vp_zero = 0
    for mu in range(8):
        for nu in range(8):
            for a in range(8):
                value = (sp.diff(ctx.e_x[nu][a], XS[mu])
                         - sum(ctx.Gamma_x[r][mu][nu] * ctx.e_x[r][a] for r in range(8))
                         + sum(ctx.omega_mixed_x[mu][a][b] * ctx.e_x[nu][b] for b in range(8)))
                if is_zero(canon_x(value)):
                    vp_zero += 1
    # the mixed omega_mu^a_b is symmetric for a mixed space/time pair
    mixed_symmetric = all(
        is_zero(ctx.omega_mixed[mu][a][b] - ctx.omega_mixed[mu][b][a])
        for mu in range(8) for a in range(4) for b in range(4, 8))
    m["nonzeroCount"] = len(nonzero)
    m["closedFormsMatch"] = matches
    m["antisymmetric512"] = antisym
    m["vielbeinPostulateZeroComponents"] = vp_zero
    m["mixedOmegaSymmetricForSpaceTimePairs"] = mixed_symmetric
    m["list"] = ["omega_{%d,%d%d} = %s" % (mu, a, b, expr_text(closed[(mu, a, b)]))
                 for (mu, a, b) in sorted(closed)]
    ok = matches and antisym and vp_zero == 512 and len(nonzero) == 24 and mixed_symmetric
    return ok, {"P_spinconn": m}


def _omega_block_form(ctx):
    """Omega_i = (w_ii0/2) diag(taubar_i, tau_i) + (w_ii4/2) diag(taubar_i tau_4, tau_i taubar_4)."""
    blocks = {}
    for i in TRANSVERSE6:
        upper0 = ctx.taubar[i]
        lower0 = ctx.tau[i]
        upper4 = _matmul(ctx.taubar[i], ctx.tau[4])
        lower4 = _matmul(ctx.tau[i], ctx.taubar[4])
        blocks[i] = (upper0, lower0, upper4, lower4)
    return blocks


def check_omega(ctx, sample=True):
    m = {}
    ok = True
    closed_w = closed_omega()
    closed_elements = {}
    for mu in range(8):
        if mu in TRANSVERSE6:
            c0 = canon_r(closed_w[(mu, mu, 0)])
            c4 = canon_r(closed_w[(mu, mu, 4)])
            element = cl_add(
                cl_scale(cl_mul(gamma_blade(mu), gamma_blade(0)), c0 / 2),
                cl_scale(cl_mul(gamma_blade(mu), gamma_blade(4)), c4 / 2))
        else:
            element = {}
        closed_elements[mu] = element
    closed_ok = all(cl_equal(ctx.Omega[mu], closed_elements[mu]) for mu in range(8))
    ok = ok and closed_ok
    m["closedFormsMatch"] = closed_ok
    m["Omega0_and_Omega4_zero"] = cl_is_zero(ctx.Omega[0]) and cl_is_zero(ctx.Omega[4])
    m["closedForm"] = ("Omega_0 = Omega_4 = 0; Omega_i = (1/2) omega_{i,i0} gamma^i gamma^0 + "
                       "(1/2) omega_{i,i4} gamma^i gamma^4 (i = 1,2,3,5,6,7)")
    slash = cl_add(*[cl_mul(ctx.gamma_up[mu], ctx.Omega[mu]) for mu in range(8)])
    slash_ok = cl_equal(slash, gamma_blade(0, 3 * H))
    ok = ok and slash_ok
    m["gammaMuOmegaMu"] = "3*H*g0" if slash_ok else cl_text(slash)
    back = cl_add(*[cl_mul(ctx.Omega[mu], ctx.gamma_up[mu]) for mu in range(8)])
    m["OmegaMuGammaMu"] = cl_text(back)
    m["commutator_gammaMu_OmegaMu"] = cl_text(cl_sub(slash, back))
    slash_nb = cl_add(*[cl_mul(ctx.gamma_up[mu], ctx.Omega_notebook[mu]) for mu in range(8)])
    m["gammaMuOmegaMu_notebookContraction"] = cl_text(slash_nb)
    nb_expected = cl_add(gamma_blade(0, sp.Rational(3, 2) * H),
                         gamma_blade(4, sp.Rational(3, 2) * H * A1))
    m["notebookContractionSlashIs_3/2H(g0 + a4' g4)"] = cl_equal(slash_nb, nb_expected)
    blocks = _omega_block_form(ctx)
    m["blockForm"] = {
        "description": ("Omega_i = (omega_{i,i0}/2) blockdiag(taubar[i], tau[i]) + "
                        "(omega_{i,i4}/2) blockdiag(taubar[i].tau[4], tau[i].taubar[4]); "
                        "upper block = chirality -1 (Psi_0..Psi_7), lower = +1 (Psi_8..Psi_15)"),
        "blocks": {str(i): {"upper_g0": blocks[i][0], "lower_g0": blocks[i][1],
                            "upper_g4": blocks[i][2], "lower_g4": blocks[i][3]}
                   for i in TRANSVERSE6},
    }
    if sample:
        sample_ok, sample_m = _omega_sample_checks(ctx)
        m["samplePoints"] = sample_m
        ok = ok and sample_ok
    return ok, {"P_Omega": m}


class SampleMatrices:
    """Actual 16x16 matrices (from the notebook gammas) at one exact sample point."""

    def __init__(self, ctx, point):
        self.ctx = ctx
        self.point = point
        self.env, self.s0 = sample_environment(point)
        s0 = self.s0
        self.val = lambda e: to_qre(e, self.env, s0)
        self.g = [qm_from_int(ctx.gamma[a], s0) for a in range(8)]
        self.C = qm_from_int(ctx.charge, s0)
        self.I = qm_identity(s0)
        self.S = {}
        for a in range(8):
            for b in range(8):
                self.S[(a, b)] = qm_scale(qm_sub(qm_mul(self.g[a], self.g[b]),
                                                 qm_mul(self.g[b], self.g[a])), Fraction(1, 4))
        self.Omega = [self._omega(ctx.omega[mu]) for mu in range(8)]
        self.OmegaNB = [self._omega(ctx.omega_mixed[mu]) for mu in range(8)]
        self.gup = [qm_scale(self.g[n], self.val(ctx.einv[n])) for n in range(8)]
        self.gdown = [qm_scale(self.g[n], self.val(ETA[n] * ctx.h[n])) for n in range(8)]

    def _omega(self, omega_ab):
        terms = []
        for a in range(8):
            for b in range(8):
                if omega_ab[a][b] == 0:
                    continue
                value = self.val(omega_ab[a][b])
                if value.is_zero():
                    continue
                terms.append(qm_scale(self.S[(a, b)], value * Fraction(1, 2)))
        return qm_add(*terms) if terms else {}

    def D_gamma(self, omega):
        out = {}
        ctx = self.ctx
        for mu in range(8):
            for nu in range(8):
                total = qm_scale(self.g[nu], self.val(ctx.d_einv[mu][nu]))
                for lam in range(8):
                    gm = ctx.Gamma[nu][mu][lam]
                    if gm != 0:
                        total = qm_add(total, qm_scale(self.gup[lam], self.val(gm)))
                total = qm_add(total, qm_sub(qm_mul(omega[mu], self.gup[nu]),
                                             qm_mul(self.gup[nu], omega[mu])))
                out[(mu, nu)] = total
        return out


def _sample_matrices(ctx):
    cached = getattr(ctx, "_sample_cache", None)
    if cached is None:
        cached = [SampleMatrices(ctx, point) for point in SAMPLE_POINTS]
        ctx._sample_cache = cached
    return cached


def _omega_sample_checks(ctx):
    results = {}
    ok = True
    blocks = _omega_block_form(ctx)
    for sm in _sample_matrices(ctx):
        s0 = sm.s0
        slash = qm_add(*[qm_mul(sm.gup[mu], sm.Omega[mu]) for mu in range(8)])
        slash_ok = qm_is_zero(qm_sub(slash, qm_scale(sm.g[0], sm.val(3 * H))))
        block_ok = qm_is_zero(sm.Omega[0]) and qm_is_zero(sm.Omega[4])
        for i in TRANSVERSE6:
            up0, lo0, up4, lo4 = blocks[i]
            z8 = _zeros(8, 8)
            m0 = qm_from_int(_blocks(up0, z8, z8, lo0), s0)
            m4 = qm_from_int(_blocks(up4, z8, z8, lo4), s0)
            c0 = sm.val(canon_r(closed_omega()[(i, i, 0)])) * Fraction(1, 2)
            c4 = sm.val(canon_r(closed_omega()[(i, i, 4)])) * Fraction(1, 2)
            candidate = qm_add(qm_scale(m0, c0), qm_scale(m4, c4))
            block_ok = block_ok and qm_is_zero(qm_sub(candidate, sm.Omega[i]))
        results[sm.point["label"]] = {"gammaMuOmegaMu_eq_3Hgamma0": slash_ok,
                                      "blockFormMatches": block_ok}
        ok = ok and slash_ok and block_ok
    return ok, results


def check_gamma_const(ctx, sample=True):
    m = {}
    zero_pairs = 0
    violations = []
    for mu in range(8):
        for nu in range(8):
            base = cl_add(cl_d_gamma_derivative(ctx, mu, nu),
                          *[cl_scale(ctx.gamma_up[lam], ctx.Gamma[nu][mu][lam])
                            for lam in range(8) if ctx.Gamma[nu][mu][lam] != 0])
            correct = cl_add(base, cl_comm(ctx.Omega[mu], ctx.gamma_up[nu]))
            if cl_is_zero(correct):
                zero_pairs += 1
            notebook = cl_clean(cl_add(base, cl_comm(ctx.Omega_notebook[mu], ctx.gamma_up[nu])))
            if notebook:
                violations.append("D_%d gamma^%d = %s" % (mu, nu, cl_text(notebook)))
    m["correctContractionZeroPairs"] = zero_pairs
    m["notebookContractionNonzeroPairs"] = len(violations)
    m["notebookContractionViolations"] = violations
    ok = zero_pairs == 64 and len(violations) > 0
    if sample:
        sample_m = {}
        for sm in _sample_matrices(ctx):
            dg = sm.D_gamma(sm.Omega)
            dnb = sm.D_gamma(sm.OmegaNB)
            zero_ok = all(qm_is_zero(v) for v in dg.values())
            nb_nonzero = sum(1 for v in dnb.values() if not qm_is_zero(v))
            sample_m[sm.point["label"]] = {"correctAllZero": zero_ok,
                                           "notebookNonzeroPairs": nb_nonzero}
            ok = ok and zero_ok and nb_nonzero == len(violations)
        m["samplePoints"] = sample_m
    return ok, {"P_gammaConst": m}


def cl_d_gamma_derivative(ctx, mu, nu):
    return gamma_blade(nu, ctx.d_einv[mu][nu])


# -- Euler-Lagrange components ------------------------------------------------

def component_table(ctx, coefficients):
    """rows a: list of (coefficient, derivative mu or None, component b) for
    gamma^mu D_mu Psi - (m + lam S) Psi = 0 (derivative None: 3H term)."""
    rows = []
    for a in range(16):
        terms = []
        for mu in range(8):
            perm, signs = ctx.gamma_sp[mu]
            terms.append((signs[a] * coefficients[mu], mu, perm[a]))
        perm0, signs0 = ctx.gamma_sp[0]
        terms.append((signs0[a] * 3 * H, None, perm0[a]))
        rows.append(terms)
    return rows


def evolution_table(ctx, coefficients):
    """d_4 Psi_a = sum_(mu != 4) c_mu (g4 g_mu)_ab d_mu Psi_b + 3H (g4 g0)_ab Psi_b
    - (m + lam S) (g4)_ab Psi_b."""
    rows = []
    g4 = ctx.gamma_sp[4]
    for a in range(16):
        terms = []
        for mu in range(8):
            if mu == 4:
                continue
            perm, signs = sp_mul(g4, ctx.gamma_sp[mu])
            terms.append((signs[a] * coefficients[mu], mu, perm[a]))
        perm, signs = sp_mul(g4, ctx.gamma_sp[0])
        terms.append((signs[a] * 3 * H, None, perm[a]))
        perm, signs = g4
        terms.append((-signs[a] * (MASS + LAM * SSYM), "mass", perm[a]))
        rows.append(terms)
    return rows


def _row_text(terms, derivative_names, lhs, rhs_mass=True):
    parts = []
    for coefficient, mu, b in terms:
        if mu is None:
            parts.append("(%s)*Psi_%d" % (expr_text(coefficient), b))
        elif mu == "mass":
            parts.append("(%s)*Psi_%d" % (expr_text(coefficient), b))
        else:
            parts.append("(%s)*%s(Psi_%d)" % (expr_text(coefficient), derivative_names[mu], b))
    text = " + ".join(parts)
    if rhs_mass:
        return "%s = (m + lam*S)*Psi_%d" % (text, lhs)
    return "%s = %s" % (lhs, text)


def check_el(ctx, sample=True):
    m = {}
    ok = True
    coefficients = closed_coefficients()
    # (i) symbolic: the covariant operator gamma^mu (d_mu + Omega_mu)
    op_ok = all(cl_equal(ctx.gamma_up[mu], gamma_blade(mu, canon_r(coefficients[mu])))
                for mu in range(8))
    slash = cl_add(*[cl_mul(ctx.gamma_up[mu], ctx.Omega[mu]) for mu in range(8)])
    slash_ok = cl_equal(slash, gamma_blade(0, 3 * H))
    ok = ok and op_ok and slash_ok
    m["derivativeCoefficientsMatch"] = op_ok
    m["nonDerivativeTermIs3Hgamma0"] = slash_ok
    m["coefficients_x0Form"] = [expr_text(c) for c in coefficients]
    # zeta form: tan z d_0 = d_zeta, s^(-1/6) = e^(-H zeta)
    zeta_coefficients = closed_coefficients_zeta()
    dz_dx0 = CZ / W ** 6
    zeta_ok = equal(canon_r(coefficients[0]) * dz_dx0, 1) and all(
        equal(canon_r(zeta_coefficients[mu]), canon_r(coefficients[mu])) for mu in range(1, 8))
    ok = ok and zeta_ok
    m["zetaFormConsistent"] = zeta_ok
    m["coefficients_zetaForm"] = [expr_text(c) for c in zeta_coefficients]
    names_x0 = ["d%d" % mu for mu in range(8)]
    names_zeta = ["dzeta"] + ["d%d" % mu for mu in range(1, 8)]
    table = component_table(ctx, coefficients)
    table_zeta = component_table(ctx, zeta_coefficients)
    m["equations_x0Form"] = [_row_text(table[a], names_x0, a) for a in range(16)]
    m["equations_zetaForm"] = [_row_text(table_zeta[a], names_zeta, a) for a in range(16)]
    evolution = evolution_table(ctx, coefficients)
    m["evolutionForm_x0"] = [_row_text(evolution[a], names_x0, "d4(Psi_%d)" % a, False)
                             for a in range(16)]
    m["legend"] = ("z = 6*H*x0, t = H*x4, a4 = a4(t), S = Psibar Psi = Psi^dagger C Psi, "
                   "U(S) = (lam/2) S^2, U'(S) = lam*S; dmu = d/dx_mu, dzeta = d/dzeta")
    # each row: exactly 8 derivative terms (one per coordinate), one 3H term, one mass term
    structure_ok = all(len(row) == 9 and sorted(t[1] for t in row if t[1] is not None)
                       == list(range(8)) for row in table)
    ok = ok and structure_ok
    m["eachRowHasAllEightDerivatives"] = structure_ok
    # (ii) the component table (read off the gamma matrices) equals the covariant
    # operator built from actual 16x16 matrices at the exact sample points
    if sample:
        sample_m = {}
        for sm in _sample_matrices(ctx):
            derivative_ok = True
            for mu in range(8):
                table_matrix = {}
                for a in range(16):
                    for coefficient, nu, b in table[a]:
                        if nu == mu:
                            table_matrix[(a, b)] = sm.val(canon_r(coefficient))
                derivative_ok = derivative_ok and qm_is_zero(qm_sub(table_matrix, sm.gup[mu]))
            table_n = {}
            for a in range(16):
                for coefficient, nu, b in table[a]:
                    if nu is None:
                        table_n[(a, b)] = sm.val(coefficient)
            slash_matrix = qm_add(*[qm_mul(sm.gup[mu], sm.Omega[mu]) for mu in range(8)])
            nd_ok = qm_is_zero(qm_sub(table_n, slash_matrix))
            # evolution form equals -gamma^4 (m - slash - sum_(mu!=4) gamma^mu d_mu)
            ev_ok = True
            g4 = sm.g[4]
            for mu in range(8):
                if mu == 4:
                    continue
                ev = {}
                for a in range(16):
                    for coefficient, nu, b in evolution[a]:
                        if nu == mu:
                            ev[(a, b)] = sm.val(canon_r(coefficient))
                ev_ok = ev_ok and qm_is_zero(qm_sub(ev, qm_mul(g4, sm.gup[mu])))
            sample_m[sm.point["label"]] = {"derivativeMatrices": derivative_ok,
                                           "nonDerivativeMatrix": nd_ok,
                                           "evolutionForm": ev_ok}
            ok = ok and derivative_ok and nd_ok and ev_ok
        m["samplePoints"] = sample_m
    return ok, {"P_EL": m}, {"table": table, "evolution": evolution}


def check_blocks(ctx):
    m = {}
    # fields of (x0, x4) only: the linear operator involves gamma^0, gamma^4 (and
    # gamma^4 gamma^0 in the evolution form); mass term is diagonal
    adjacency = {a: set() for a in range(16)}
    for mask in (1 << 0, 1 << 4, (1 << 0) | (1 << 4)):
        perm, _ = ctx.blade_sp[mask]
        for a in range(16):
            adjacency[a].add(perm[a])
            adjacency[perm[a]].add(a)
    seen, blocks = set(), []
    for start in range(16):
        if start in seen:
            continue
        stack, component = [start], set()
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            stack.extend(adjacency[node] - component)
        seen |= component
        blocks.append(tuple(sorted(component)))
    blocks = sorted(blocks)
    notebook = sorted(tuple(sorted(b)) for b in NOTEBOOK_BLOCKS)
    m["blocks"] = [list(b) for b in blocks]
    m["notebookBlocks"] = [list(b) for b in notebook]
    m["agreesWithNotebook"] = blocks == notebook
    m["chiralityContent"] = [[sum(1 for c in b if c < 8), sum(1 for c in b if c >= 8)]
                             for b in blocks]
    m["note"] = ("for lam != 0 the blocks are coupled only through the scalar S = Psibar Psi "
                 "(a bilinear in all 16 components); the linear operator is block diagonal")
    m["notebookCell1137"] = compare_notebook_cell1137(ctx)
    ok = blocks == notebook and all(len(b) == 4 for b in blocks)
    return ok, {"P_blocks": m}


def compare_notebook_cell1137(ctx):
    """Measurement (not a check): the notebook's stored cell-1137 block equations
    against the correct (z, t) evolution form for Psi(x0, x4), lam = 0:
        d_t Psi = 6 tan z g4 g0 d_z Psi + 3 g4 g0 Psi - (m/H) g4 Psi."""
    from sympy.parsing.mathematica import parse_mathematica
    text = NOTEBOOK_CELL1137_BLOCK_EQUATIONS
    text = re.sub(r"Derivative\[1, 0\]\[yZ\[(\d+)\]\]\[z, t\]", r"nbDz\g<1>", text)
    text = re.sub(r"Derivative\[0, 1\]\[yZ\[(\d+)\]\]\[z, t\]", r"nbDt\g<1>", text)
    text = re.sub(r"yZ\[(\d+)\]\[z, t\]", r"nbY\g<1>", text)
    text = text.replace("Derivative[1][a4][t]", "nbA1").replace("a4[t]", "nbA0")
    equations = [e.strip() for e in text.strip("{}").replace("}, {", ", ").split(",")]
    q1, mnb, zz, a0, a1 = sp.symbols("Q1 M z nbA0 nbA1")
    ys = [sp.Symbol("nbY%d" % j) for j in range(16)]
    dz = [sp.Symbol("nbDz%d" % j) for j in range(16)]
    z_to_y = {k: j for j, k in enumerate(NOTEBOOK_YZ_TO_Z)}
    g4g0 = sp_mul(ctx.gamma_sp[4], ctx.gamma_sp[0])
    g4 = ctx.gamma_sp[4]
    residuals, linear_ok, parsed_count, q_signs = [], True, 0, []
    for equation in equations:
        lhs, rhs = equation.split("==")
        j = int(lhs.strip()[len("nbDt"):])
        rhs_nb = parse_mathematica(rhs.strip())
        a = NOTEBOOK_YZ_TO_Z[j]
        ours = (6 * sp.tan(zz) * g4g0[1][a] * dz[z_to_y[g4g0[0][a]]]
                + 3 * g4g0[1][a] * ys[z_to_y[g4g0[0][a]]]
                + mnb * g4[1][a] * ys[z_to_y[g4[0][a]]])        # -(m/H) = M_notebook
        residual = sp.simplify(sp.expand(rhs_nb - ours))
        parsed_count += 1
        linear_ok = linear_ok and sp.simplify(residual.subs(q1, 0)) == 0
        q_value = q1 * sp.sinh(a0) * a1 * sp.exp(-a0)
        coefficient = sp.simplify(residual / (q_value * ys[j])) if residual != 0 else 0
        if coefficient not in (0, 1, -1):
            linear_ok = False
        q_signs.append(int(coefficient))
        readable = residual.subs({a0: A4R, a1: A4P}).subs(
            {ys[k]: sp.Symbol("yZ%d" % k) for k in range(16)})
        residuals.append("d_t yZ%d: notebook - correct = %s" % (j, sp.sstr(readable)))
    return {
        "equationsParsed": parsed_count,
        "identification": ("M_notebook = -m/H (CONTRACT: m = -H M), t = H x4, z = 6 H x0, "
                           "yZ[j] = Psi_%s[j]" % (list(NOTEBOOK_YZ_TO_Z),)),
        "linearPartAgreesWithCorrectEquations": linear_ok,
        "residualIsPlusMinus_q_yZj": q_signs,
        "residuals": residuals,
        "note": ("every notebook term except the Q1 terms equals the correct evolution form "
                 "for Psi(x0, x4), lam = 0; the correct equations contain no a4 at all (a4 "
                 "cancels from gamma^mu Omega_mu = 3 H gamma^0); the residual is exactly "
                 "+-q yZ_j with q = Q1 sinh(a4) a4' e^-a4 in blocks 1-2 (yZ0..yZ7) and 0 in "
                 "blocks 3-4; Q1 is the notebook's spin-connection switch, so these terms come "
                 "from its (Q1/2) omega SAB term (detailed attribution: P_notebookCompare)"),
    }


# -- energy-momentum tensor ---------------------------------------------------

def _zeta_wave_operators():
    """A = -gamma^4 (M - i K gamma^0) (u' = A u) and A^dagger (Clifford elements)."""
    a_elem = cl_mul(gamma_blade(4, -1), cl_add({0: MASS}, gamma_blade(0, -sp.I * KZ)))
    a_dag = cl_dagger(a_elem, conj_canon)
    return a_elem, a_dag


def emt_zeta_wave(ctx):
    """Q-matrices of T_mu nu = |f|^2 u^dagger Q_mu nu u for the zeta plane wave
    Psi = e^{(-3H + iK) zeta} u(x4), lam = 0 (U = 0), on shell."""
    a_elem, a_dag = _zeta_wave_operators()
    charge = cl(CHARGE_MASK, sp.Integer(1))
    f2 = W ** -6                              # |e^{(-3H+iK) zeta}|^2 = 1/sin z
    kappa0 = (-3 * H + sp.I * KZ) * CZ / W ** 6     # d_0 f / f   (d zeta/dx0 = cot z)
    kappa0_bar = (-3 * H - sp.I * KZ) * CZ / W ** 6
    right, left = [], []
    for mu in range(8):
        if mu == 0:
            r = cl_add({0: kappa0}, ctx.Omega[0])
            l_ = cl_sub(cl_scale(charge, kappa0_bar), cl_mul(charge, ctx.Omega[0]))
        elif mu == 4:
            r = cl_add(a_elem, ctx.Omega[4])
            l_ = cl_sub(cl_mul(a_dag, charge), cl_mul(charge, ctx.Omega[4]))
        else:
            r = dict(ctx.Omega[mu])
            l_ = cl_scale(cl_mul(charge, ctx.Omega[mu]), -1)
        right.append(r)
        left.append(l_)

    def kinetic(mu, nu):  # Psibar g_mu D_nu Psi - (D_nu Psibar) g_mu Psi  (per |f|^2)
        return cl_sub(cl_mul_all(charge, ctx.gamma_down[mu], right[nu]),
                      cl_mul(left[nu], ctx.gamma_down[mu]))

    lag = cl_scale(cl_add(*[cl_sub(cl_mul_all(charge, ctx.gamma_up[mu], right[mu]),
                                   cl_mul(left[mu], ctx.gamma_up[mu])) for mu in range(8)]),
                   sp.Rational(1, 2))
    lag = cl_sub(lag, cl_scale(charge, MASS))       # L_s (lam = 0, m = M)
    q = [[None] * 8 for _ in range(8)]
    for mu in range(8):
        for nu in range(8):
            element = cl_scale(cl_add(kinetic(mu, nu), kinetic(nu, mu)), -sp.Rational(1, 4))
            if mu == nu:
                element = cl_add(element, cl_scale(lag, ctx.g[mu]))
            q[mu][nu] = cl_scale(element, f2)
    k4 = cl_scale(cl_sub(cl_mul_all(charge, ctx.gamma_up[4], right[4]),
                         cl_mul(left[4], ctx.gamma_up[4])), sp.Rational(1, 2) * f2)
    ke_h = cl_scale(cl_add(*[cl_sub(cl_mul_all(charge, ctx.gamma_up[j], right[j]),
                                    cl_mul(left[j], ctx.gamma_up[j]))
                             for j in range(8) if j != 4]), -sp.Rational(1, 2) * f2)
    return {"Q": q, "L": cl_scale(lag, f2), "K4": k4, "KE_H": ke_h, "A": a_elem,
            "Adag": a_dag, "f2": f2, "right": right, "left": left}


def check_emt(ctx, sample=True):
    m = {}
    ok = True
    # (a) anticommutator list {gamma_mu, Omega_nu} + {gamma_nu, Omega_mu}, mu <= nu
    closed = closed_anticommutators()
    nonzero, listing, ac_ok = [], [], True
    for mu in range(8):
        for nu in range(mu, 8):
            element = cl_add(cl_anti(ctx.gamma_down[mu], ctx.Omega[nu]),
                             cl_anti(ctx.gamma_down[nu], ctx.Omega[mu]))
            expected = closed.get((mu, nu), {})
            ac_ok = ac_ok and cl_equal(element, expected)
            if not cl_is_zero(element):
                nonzero.append((mu, nu))
                listing.append("(%d,%d): %s" % (mu, nu, cl_text(element)))
    m["anticommutatorNonzeroCount"] = len(nonzero)
    m["anticommutatorsMatchClosedForms"] = ac_ok
    m["anticommutators"] = listing
    diagonal_transverse_zero = all((i, i) not in nonzero for i in TRANSVERSE6)
    m["transverseDiagonalAnticommutatorsVanish"] = diagonal_transverse_zero
    m["T_general"] = ("T_mu nu = -(1/4)[Psibar g_mu d_nu Psi + Psibar g_nu d_mu Psi - d_mu Psibar "
                      "g_nu Psi - d_nu Psibar g_mu Psi] - (1/4) Psibar({g_mu,W_nu}+{g_nu,W_mu}) Psi "
                      "+ g_mu nu L_s, g_mu = eta_mu h_mu gamma^mu (flat)")
    m["transversePressureIdentity"] = (
        "for every Psi(x0,x4): T^i_i = L_s (i = 1,2,3,5,6,7), on shell = S U'(S) - U(S)")
    ok = ok and ac_ok and len(nonzero) == 21 and diagonal_transverse_zero
    # (b) zeta plane wave, lam = 0
    data = emt_zeta_wave(ctx)
    q, f2 = data["Q"], data["f2"]
    charge = cl(CHARGE_MASK, sp.Integer(1))
    c_g0 = cl_mul(charge, gamma_blade(0))
    q_rho = cl_scale(cl_add(cl_scale(charge, MASS), cl_scale(c_g0, -sp.I * KZ)), f2)
    q_p0 = cl_scale(c_g0, -sp.I * KZ * f2)
    lag_zero = cl_is_zero(data["L"])
    rho_ok = cl_equal(q[4][4], q_rho)
    p_transverse_ok = all(cl_is_zero(cl_scale(q[i][i], ctx.ginv[i])) for i in TRANSVERSE6)
    p0_ok = cl_equal(cl_scale(q[0][0], ctx.ginv[0]), q_p0)
    ke_l = cl_scale(data["K4"], sp.Rational(1, 2))
    ke_l_ok = cl_equal(ke_l, cl_scale(q_rho, sp.Rational(1, 2)))
    ke_h_ok = cl_equal(data["KE_H"], q_p0)
    pe_h = cl_scale(charge, MASS * f2)
    pe_h_ok = cl_equal(cl_sub(q[4][4], data["KE_H"]), pe_h)
    hermitian_ok = all(cl_equal(cl_dagger(q[mu][nu], conj_canon), q[mu][nu])
                       for mu in range(8) for nu in range(8))
    trace = cl_add(*[cl_scale(q[mu][mu], ctx.ginv[mu]) for mu in range(8)])
    trace_ok = cl_equal(trace, cl_scale(charge, -MASS * f2))
    free_of_a4 = all(is_zero(sp.diff(c, EA)) and is_zero(sp.diff(c, A1)) and is_zero(sp.diff(c, A2))
                     for element in (q[4][4], cl_scale(q[0][0], ctx.ginv[0]), data["K4"],
                                     data["KE_H"])
                     for c in element.values())
    a_elem, a_dag = data["A"], data["Adag"]

    def evolve(element):  # d/dx4 of u^dagger Q u  (plus explicit x4 dependence)
        return cl_add(cl_mul(a_dag, element), cl_mul(element, a_elem), cl_d4(element))

    rho_frozen = cl_is_zero(evolve(q_rho))
    p0_rate = cl_clean(evolve(q_p0))
    p0_rate_expected = cl_scale(cl_mul_all(charge, gamma_blade(4), gamma_blade(0)),
                                -2 * sp.I * KZ * MASS * f2)
    p0_rate_ok = cl_equal(evolve(q_p0), p0_rate_expected)
    # the rate is the commutator i[h, Q] with the Hermitian h = i A: it vanishes on
    # h-eigenstates, and i[h, i[h, R]] = -(2E)^2 R, E^2 = M^2 + K^2 (oscillation at 2E)
    h_elem = cl_scale(a_elem, sp.I)
    rate = evolve(q_p0)
    rate_is_commutator = cl_equal(rate, cl_scale(cl_comm(h_elem, q_p0), sp.I))
    second = cl_scale(cl_comm(h_elem, cl_scale(cl_comm(h_elem, rate), sp.I)), sp.I)
    rate_frequency_2e = cl_equal(second, cl_scale(rate, -4 * (MASS ** 2 + KZ ** 2)))
    # conservation nabla_mu T^mu_nu = 0 for all nu (all 64 components of T^mu_nu)
    mixed = [[cl_scale(q[mu][nu], ctx.ginv[mu]) for nu in range(8)] for mu in range(8)]
    conservation = []
    for nu in range(8):
        terms = [cl_d0(mixed[0][nu]), evolve(mixed[4][nu])]
        for mu in range(8):
            for lam in range(8):
                gm = ctx.Gamma[mu][mu][lam]
                if gm != 0:
                    terms.append(cl_scale(mixed[lam][nu], gm))
                gl = ctx.Gamma[lam][mu][nu]
                if gl != 0:
                    terms.append(cl_scale(mixed[mu][lam], -gl))
        conservation.append(cl_is_zero(cl_add(*terms)))
    off_diagonal = []
    for mu in range(8):
        for nu in range(mu + 1, 8):
            element = cl_clean(q[mu][nu])
            if element:
                rate = cl_clean(evolve(element))
                off_diagonal.append({"component": "T_%d%d" % (mu, nu),
                                     "Q": cl_text(element),
                                     "conservedInX4": not rate})
    m["zetaWave"] = {
        "ansatz": "Psi = exp((-3H + iK) zeta) u(x4), zeta = log(sin z)/(6H), lam = 0 (M_eff = m)",
        "bilinears": "S = u^dagger C u / sin z,  J0 = -i u^dagger C g0 u / sin z",
        "rho": "T_44 = m S + K J0",
        "p_transverse_1_2_3_5_6_7": "T^i_i = L_s = 0 (on shell, lam = 0) for i = 1,2,3,5,6,7",
        "p_0": "T^0_0 = K J0 + L_s = K J0",
        "KE_L": "(1/2) K_4 = (1/2)(m S + K J0) = rho/2",
        "PE_L": "rho - KE_L = (1/2)(m S + K J0)",
        "KE_H": "K J0",
        "PE_H": "m S",
        "w": "pbar/rho = (K J0/7)/(m S + K J0); K = 0: rho = m S, p = 0, w = 0 (dust)",
        "trace": "T^mu_mu = -m S",
        "onShellLagrangianZero": lag_zero,
        "rhoMatches": rho_ok, "transversePressuresZero": p_transverse_ok,
        "p0Matches": p0_ok, "KE_LMatches": ke_l_ok, "KE_HMatches": ke_h_ok,
        "PE_HMatches": pe_h_ok, "hermitian": hermitian_ok, "traceMatches": trace_ok,
        "a4Independent": free_of_a4,
        "rhoFrozenInX4": rho_frozen,
        "p0RateOfChange": cl_text(p0_rate),
        "p0RateMatches_-2iKm_u^dag_C_g4_g0_u": p0_rate_ok,
        "p0FrozenInX4": ("only for K = 0 or on stationary (h-eigen) states; for K != 0 "
                         "superpositions p_0 oscillates at frequency 2E (measured rate "
                         "d/dx4 (u^dag Q_p0 u) = -2iKm u^dag C g4 g0 u / sin z)"),
        "p0RateIsCommutator_i[h,Q]": rate_is_commutator,
        "p0RateOscillatesAt2E": rate_frequency_2e,
        "conservationPerNu": conservation,
        "offDiagonal": off_diagonal,
        "specDeviations": [
            "STAGE2_SPEC P_EMT 'frozen in x4': rho = T_44 and the six transverse pressures "
            "are frozen for every state; p_0 = T^0_0 = K J0 is frozen only for K = 0 or on "
            "h-eigenstates (rate = i[h, Q_p0] != 0 for K m != 0)",
            "the pressure is isotropic only in the six transverse directions 1,2,3,5,6,7; "
            "the hidden-space direction carries p_0 = K J0 (anisotropic for K J0 != 0)",
            "CONTRACT 7 'T_ii = g_ii (S U' - U)' holds for i = 1,2,3,5,6,7 for every "
            "Psi(x0, x4) but not for i = 0 when K J0 != 0",
            "for lam != 0 the zeta plane wave is not an exact solution (M_eff = m + lam S "
            "with S = u^dag C u / sin z depends on zeta); the exact statements are for "
            "lam = 0 (or S = 0)",
            "the zeta wave generally has nonzero off-diagonal T_0i, T_4i, T_ij (listed); "
            "consistency with the diagonal metric requires states on which these "
            "bilinears vanish",
        ],
    }
    zeta_ok = (lag_zero and rho_ok and p_transverse_ok and p0_ok and ke_l_ok and ke_h_ok
               and pe_h_ok and hermitian_ok and trace_ok and free_of_a4 and rho_frozen
               and p0_rate_ok and rate_is_commutator and rate_frequency_2e
               and all(conservation))
    ok = ok and zeta_ok
    if sample:
        sample_ok, sample_m = _emt_sample_checks(ctx)
        m["samplePoints"] = sample_m
        ok = ok and sample_ok
    return ok, {"P_EMT": m}


def _emt_sample_checks(ctx):
    """Rebuild T_44, T^0_0, T^i_i for the zeta wave from actual matrices."""
    results = {}
    ok = True
    for sm in _sample_matrices(ctx):
        v = sm.val
        s0 = sm.s0
        mass = v(MASS)
        kz = v(KZ)
        i_unit = QRE({(0, 0, 1): Fraction(1)}, s0)
        g0, g4, C = sm.g[0], sm.g[4], sm.C
        a_mat = qm_scale(qm_mul(g4, qm_sub(qm_scale(sm.I, mass),
                                           qm_scale(g0, i_unit * kz))), -1)
        a_dag = qm_dagger(a_mat)
        kappa0 = v((-3 * H + sp.I * KZ) * CZ / W ** 6)
        kappa0_bar = kappa0.conj()
        right, left = [], []
        for mu in range(8):
            om = sm.Omega[mu]
            if mu == 0:
                r = qm_add(qm_scale(sm.I, kappa0), om)
                l_ = qm_sub(qm_scale(C, kappa0_bar), qm_mul(C, om))
            elif mu == 4:
                r = qm_add(a_mat, om)
                l_ = qm_sub(qm_mul(a_dag, C), qm_mul(C, om))
            else:
                r = om
                l_ = qm_scale(qm_mul(C, om), -1)
            right.append(r)
            left.append(l_)

        def kin(mu, nu):
            return qm_sub(qm_mul(qm_mul(C, sm.gdown[mu]), right[nu]),
                          qm_mul(left[nu], sm.gdown[mu]))

        lag = qm_add(*[qm_sub(qm_mul(qm_mul(C, sm.gup[mu]), right[mu]),
                              qm_mul(left[mu], sm.gup[mu])) for mu in range(8)])
        lag = qm_sub(qm_scale(lag, Fraction(1, 2)), qm_scale(C, mass))
        f2 = v(W ** -6)

        def t_mixed(mu):
            element = qm_scale(qm_add(kin(mu, mu), kin(mu, mu)), Fraction(-1, 4))
            element = qm_add(element, qm_scale(lag, v(ctx.g[mu])))
            return qm_scale(element, f2 * v(ctx.ginv[mu]))

        c_g0 = qm_mul(C, g0)
        rho_expected = qm_scale(qm_sub(qm_scale(C, mass), qm_scale(c_g0, i_unit * kz)), f2)
        rho = qm_scale(t_mixed(4), -1)                     # T_44 = -T^4_4
        rho_ok = qm_is_zero(qm_sub(rho, rho_expected))
        p0_matrix = t_mixed(0)
        p0_ok = qm_is_zero(qm_sub(p0_matrix, qm_scale(c_g0, -(i_unit * kz) * f2)))
        pt_ok = all(qm_is_zero(t_mixed(i)) for i in TRANSVERSE6)
        frozen = qm_is_zero(qm_add(qm_mul(a_dag, rho_expected), qm_mul(rho_expected, a_mat)))
        # exact example values for two explicit spinors (definitions, not closed forms)
        k4 = qm_scale(qm_sub(qm_mul(qm_mul(C, sm.gup[4]), right[4]),
                             qm_mul(left[4], sm.gup[4])), f2 * Fraction(1, 2))
        ke_h = qm_scale(qm_add(*[qm_sub(qm_mul(qm_mul(C, sm.gup[j]), right[j]),
                                        qm_mul(left[j], sm.gup[j])) for j in range(8) if j != 4]),
                        f2 * Fraction(-1, 2))
        s_matrix = qm_scale(C, f2)
        p0_rate = qm_add(qm_mul(a_dag, p0_matrix), qm_mul(p0_matrix, a_mat))
        examples = {}
        for name, vector in (("u_a = e0 + e4", {0: 1, 4: 1}),
                             ("u_b = e0 + i e1 + e4 + i e12", {0: 1, 1: 1j, 4: 1, 12: 1j})):
            u = {}
            for index, value in vector.items():
                if isinstance(value, complex):
                    u[index] = QRE({(0, 0, 1): Fraction(int(value.imag))}, s0)
                else:
                    u[index] = QRE.const(value, s0)

            def form(matrix):
                total = QRE.const(0, s0)
                for (i, j), entry in matrix.items():
                    if i in u and j in u:
                        total = total + u[i].conj() * entry * u[j]
                return total

            rho_v = form(rho)
            p0_v = form(p0_matrix)
            ke_l_v = form(k4) * Fraction(1, 2)
            ke_h_v = form(ke_h)
            s_v = form(s_matrix)
            values = {"S": s_v, "rho": rho_v, "p_0": p0_v,
                      "p_1..3,5..7": form(t_mixed(1)), "KE_L": ke_l_v, "PE_L": rho_v - ke_l_v,
                      "KE_H": ke_h_v, "PE_H": rho_v - ke_h_v, "d4_p0": form(p0_rate)}
            text = {key: qre_text(value) for key, value in values.items()}
            if len(rho_v.terms) <= 1 and (0, 0, 0) in rho_v.terms and len(p0_v.terms) <= 1:
                rho_q = rho_v.terms.get((0, 0, 0), Fraction(0))
                p0_q = p0_v.terms.get((0, 0, 0), Fraction(0))
                text["w"] = str(p0_q / 7 / rho_q) if rho_q else "undefined (rho = 0)"
            examples[name] = text
        results[sm.point["label"]] = {"rho": rho_ok, "p0": p0_ok, "pTransverse": pt_ok,
                                      "rhoFrozen": frozen, "examples_lam0": examples}
        ok = ok and rho_ok and p0_ok and pt_ok and frozen
    return ok, results


def qre_text(value):
    """Readable exact text of a sample-ring element (r = sin(z)^(1/6), E = e^a4)."""
    if value.is_zero():
        return "0"
    parts = []
    for (k, n, j), c in sorted(value.terms.items()):
        factors = [str(c)]
        if k:
            factors.append("r^%d" % k)
        if n:
            factors.append("E^%d" % n)
        if j:
            factors.append("i")
        parts.append("*".join(factors))
    return " + ".join(parts)


# -- modes --------------------------------------------------------------------

def check_modes(ctx, sample=True):
    m = {}
    ok = True
    # exact reduction: gamma^0_curved d_0 f/f + gamma^mu Omega_mu = i K gamma^0
    kappa0 = (-3 * H + sp.I * KZ) * CZ / W ** 6
    reduction = cl_add(cl_scale(ctx.gamma_up[0], kappa0),
                       *[cl_mul(ctx.gamma_up[mu], ctx.Omega[mu]) for mu in range(8)])
    reduction_ok = cl_equal(reduction, gamma_blade(0, sp.I * KZ))
    m["reduction"] = ("Psi = exp((-3H + iK) zeta) u(x4): gamma^mu D_mu Psi = M_eff Psi <=> "
                      "gamma^4 du/dx4 = (M_eff - i K gamma^0) u (exact for lam = 0 or S = 0; "
                      "for lam != 0, M_eff = m + lam S with S = u^dag C u / sin z depends on zeta)")
    m["reductionExact"] = reduction_ok
    a_elem, a_dag = _zeta_wave_operators()
    a_sq = cl_mul(a_elem, a_elem)
    a_sq_ok = cl_equal(a_sq, {0: -(MASS ** 2 + KZ ** 2)})
    m["A_squared"] = "-(M^2 + K^2) 1" if a_sq_ok else cl_text(a_sq)
    h_elem = cl_scale(a_elem, sp.I)
    h_herm = cl_equal(cl_dagger(h_elem, conj_canon), h_elem)
    h_sq_ok = cl_equal(cl_mul(h_elem, h_elem), {0: MASS ** 2 + KZ ** 2})
    h_trace_zero = is_zero(h_elem.get(0, 0))
    m["h"] = "h = i A = -i M g4 - K g4 g0 (Hermitian), h^2 = (M^2 + K^2) 1, tr h = 0"
    m["dispersion"] = "E^2 = M_eff^2 + K^2, eigenvalues +E (x8), -E (x8)"
    m["hHermitian"] = h_herm
    m["hSquared"] = h_sq_ok
    m["hTraceless"] = h_trace_zero
    ok = ok and reduction_ok and a_sq_ok and h_herm and h_sq_ok and h_trace_zero
    # k != 0, q != 0: exact reduced equation and its coefficients
    k_coefficient = canon_r(closed_coefficients()[1])        # s^(-1/6) e^{-a4}
    q_coefficient = canon_r(closed_coefficients()[5])        # s^(-1/6) e^{+a4}
    zeta_forms_ok = (equal(k_coefficient, canon_r(sp.exp(-H * ZETA - A4R)))
                     and equal(q_coefficient, canon_r(sp.exp(-H * ZETA + A4R))))
    # coefficient c(zeta, t) = e^{-H zeta} e^{-a4(t)}: d_zeta ln c = -H, d_t ln c = -a4'
    c_readable = sp.exp(-H * ZETA - A4R)
    dz = sp.simplify(sp.diff(c_readable, ZETA) / c_readable)
    dt = sp.simplify(sp.diff(c_readable, TS) / c_readable)
    nonseparable = sp.simplify(dz + H) == 0 and sp.simplify(dt + A4P) == 0
    m["kCoefficientLogDerivatives"] = {"d_zeta": expr_text(dz), "d_t": expr_text(dt)}
    m["kModes"] = ("Psi = exp(-3H zeta) exp(i k x1 + i q x5) phi(zeta, x4): gamma^0 d_zeta phi + "
                   "gamma^4 d_4 phi + i (k e^{-H zeta - a4(t)} gamma^1 + q e^{-H zeta + a4(t)} "
                   "gamma^5) phi = M phi; the coefficients are products of a nonconstant "
                   "function of zeta and a nonconstant function of t, so the k != 0 and q != 0 "
                   "modes do not separate into zeta- and t-dependent factors (the document "
                   "writes k_1 for k and k_5 for q)")
    m["kCoefficientZetaForm"] = zeta_forms_ok
    m["kCoefficientNotConstantInEitherVariable"] = nonseparable
    # local (frozen-coefficient) dispersion with kt = k e^{-H zeta - a4}, qt = q e^{-H zeta + a4}
    kt, qt = sp.symbols("kt qt", real=True)
    x_elem = cl_add(gamma_blade(0, KZ), gamma_blade(1, kt), gamma_blade(5, qt))
    a_loc = cl_mul(gamma_blade(4, -1), cl_sub({0: MASS}, cl_scale(x_elem, sp.I)))
    a_loc_sq_ok = cl_equal(cl_mul(a_loc, a_loc),
                           {0: -(MASS ** 2 + KZ ** 2 + kt ** 2 - qt ** 2)})
    h_loc = cl_scale(a_loc, sp.I)
    # h_loc - h_loc^dagger = -2 qt gamma^4 gamma^5; the anti-Hermitian part is half of it
    h_minus_adjoint = cl_clean(cl_sub(h_loc, cl_dagger(h_loc, conj_canon)))
    anti_hermitian_part = cl_clean(cl_scale(h_minus_adjoint, sp.Rational(1, 2)))
    expected_part = cl_scale(cl_mul(gamma_blade(4), gamma_blade(5)), -2 * qt)
    hloc_ok = (cl_equal(cl_sub(h_loc, cl_dagger(h_loc, conj_canon)), expected_part)
               and cl_equal(anti_hermitian_part,
                            cl_scale(cl_mul(gamma_blade(4), gamma_blade(5)), -qt)))
    m["localDispersion"] = ("E^2 = M^2 + K^2 + (k e^{-H zeta - a4})^2 - (q e^{-H zeta + a4})^2 "
                            "(WKB / frozen coefficients, local)")
    m["localDispersionExactForFrozenCoefficients"] = a_loc_sq_ok
    m["hLocal_minus_hLocalDagger"] = cl_text(h_minus_adjoint) if h_minus_adjoint else "0"
    m["hLocalAntiHermitianPart"] = cl_text(anti_hermitian_part) if anti_hermitian_part else "0"
    m["hLocalHermitianIffQZero"] = hloc_ok
    m["instabilityOnset"] = ("E^2 < 0 iff (q e^{-H zeta + a4})^2 > M^2 + K^2 + (k e^{-H zeta - a4})^2;"
                             " k = 0: a4(t) > H zeta + (1/2) log((M^2 + K^2)/q^2); a4 = t: "
                             "t* = H zeta + log(sqrt(M^2 + K^2)/|q|)")
    # onset check for a4 = t, k = 0 at the exact values M = 3, K = 4, q = 1/2 (E^2 = 0 at t*)
    tstar = H * ZETA + sp.log(sp.sqrt(sp.Integer(3) ** 2 + 4 ** 2) / sp.Rational(1, 2))
    e2 = (sp.Integer(3) ** 2 + 4 ** 2 - (sp.Rational(1, 2) * sp.exp(-H * ZETA + tstar)) ** 2)
    onset_ok = sp.simplify(e2) == 0
    m["instabilityOnsetVerified_M3_K4_q1/2"] = onset_ok
    ok = ok and zeta_forms_ok and nonseparable and a_loc_sq_ok and hloc_ok and onset_ok
    if sample:
        sample_m = {}
        for sm in _sample_matrices(ctx):
            v = sm.val
            i_unit = QRE({(0, 0, 1): Fraction(1)}, sm.s0)
            mass, kz = v(MASS), v(KZ)
            a_mat = qm_scale(qm_mul(sm.g[4], qm_sub(qm_scale(sm.I, mass),
                                                    qm_scale(sm.g[0], i_unit * kz))), -1)
            sq_ok = qm_is_zero(qm_add(qm_mul(a_mat, a_mat),
                                      qm_scale(sm.I, mass * mass + kz * kz)))
            h_mat = qm_scale(a_mat, i_unit)
            herm_ok = qm_is_zero(qm_sub(qm_dagger(h_mat), h_mat))
            kt_v = v(KMOM) * v(canon_r(closed_coefficients()[1]))
            qt_v = v(QMOM) * v(canon_r(closed_coefficients()[5]))
            x_mat = qm_add(qm_scale(sm.g[0], kz), qm_scale(sm.g[1], kt_v),
                           qm_scale(sm.g[5], qt_v))
            a_l = qm_scale(qm_mul(sm.g[4], qm_sub(qm_scale(sm.I, mass),
                                                  qm_scale(x_mat, i_unit))), -1)
            e2_v = mass * mass + kz * kz + kt_v * kt_v - qt_v * qt_v
            loc_ok = qm_is_zero(qm_add(qm_mul(a_l, a_l), qm_scale(sm.I, e2_v)))
            sample_m[sm.point["label"]] = {"A_squared": sq_ok, "hHermitian": herm_ok,
                                           "localDispersion": loc_ok}
            ok = ok and sq_ok and herm_ok and loc_ok
        m["samplePoints"] = sample_m
    return ok, {"P_modes": m}


# -- Einstein tensor ------------------------------------------------------------

def ricci_from_christoffel(gamma_x):
    ric = [[sp.Integer(0)] * 8 for _ in range(8)]
    for mu in range(8):
        for nu in range(8):
            total = sp.Integer(0)
            for r in range(8):
                total += sp.diff(gamma_x[r][mu][nu], XS[r]) - sp.diff(gamma_x[r][mu][r], XS[nu])
                for lam in range(8):
                    total += (gamma_x[r][r][lam] * gamma_x[lam][mu][nu]
                              - gamma_x[r][nu][lam] * gamma_x[lam][mu][r])
            ric[mu][nu] = total
    return ric


def christoffel_x(g_diag):
    gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for r in range(8):
        for mu in range(8):
            for nu in range(8):
                total = sp.Integer(0)
                if nu == r:
                    total += sp.diff(g_diag[r], XS[mu])
                if mu == r:
                    total += sp.diff(g_diag[r], XS[nu])
                if mu == nu:
                    total -= sp.diff(g_diag[mu], XS[r])
                gam[r][mu][nu] = total / (2 * g_diag[r])
    return gam


def parse_notebook_einstein():
    from sympy.parsing.mathematica import parse_mathematica
    text = (NOTEBOOK_CELL584_EINSTEIN_G
            .replace("Derivative[1][a4][H*x4]", "nbA1")
            .replace("Derivative[2][a4][H*x4]", "nbA2")
            .replace("a4[H*x4]", "nbA0"))
    parsed = parse_mathematica(text)
    rtext = NOTEBOOK_CELL583_RICCI_SCALAR.replace("Derivative[1][a4][H*x4]", "nbA1")
    rparsed = parse_mathematica(rtext)
    names = {"H": H, "x0": X0, "nbA0": sp.log(EA), "nbA1": A1, "nbA2": A2}

    def convert(e):
        e = e.subs({sp.Symbol(k): v for k, v in names.items()})
        return canon_x(e)

    return [[convert(parsed[i][j]) for j in range(8)] for i in range(8)], convert(rparsed)


def check_einstein(ctx):
    m = {}
    ric_x = ricci_from_christoffel(ctx.Gamma_x)
    ric = [[canon_x(ric_x[mu][nu]) for nu in range(8)] for mu in range(8)]
    ricci_scalar = sum(ctx.ginv[mu] * ric[mu][mu] for mu in range(8))
    r_ok = equal(ricci_scalar, canon_r(closed_ricci_scalar()))
    off_ok = all(is_zero(ric[mu][nu]) for mu in range(8) for nu in range(8) if mu != nu)
    g_mixed = [ctx.ginv[mu] * ric[mu][mu] - ricci_scalar / 2 for mu in range(8)]
    closed = closed_einstein_mixed()
    g_ok = all(equal(g_mixed[mu], canon_r(closed[mu])) for mu in range(8))
    m["ricciScalar"] = expr_text(closed_ricci_scalar()) if r_ok else "mismatch"
    m["einsteinMixedDiagonal"] = [expr_text(c) for c in closed]
    m["offDiagonalZero"] = off_ok
    m["ricciScalarMatches"] = r_ok
    m["einsteinMatches"] = g_ok
    # Bianchi identity nabla_mu G^mu_nu = 0
    bianchi = []
    for nu in range(8):
        total = d0(g_mixed[nu]) if nu == 0 else sp.Integer(0)
        if nu == 4:
            total += d4(g_mixed[4])
        for mu in range(8):
            total += ctx.Gamma[mu][mu][nu] * g_mixed[nu]
            total -= ctx.Gamma[mu][mu][nu] * g_mixed[mu]
        bianchi.append(is_zero(total))
    m["contractedBianchi"] = bianchi
    # notebook cell 584 (covariant G_mu nu) and cell 583 (R)
    nb_g, nb_r = parse_notebook_einstein()
    nb_cov_ok = all(equal(nb_g[mu][nu], ctx.g[mu] * g_mixed[mu] if mu == nu else 0)
                    for mu in range(8) for nu in range(8))
    nb_mixed = [ctx.ginv[mu] * nb_g[mu][mu] for mu in range(8)]
    nb_mixed_ok = all(equal(nb_mixed[mu], canon_r(closed[mu])) for mu in range(8))
    nb_r_ok = equal(nb_r, ricci_scalar)
    m["notebookCell584"] = {
        "interpretation": "covariant G_mu nu; mixed G^mu_nu = g^{mu mu} G_mu mu",
        "covariantAgrees": nb_cov_ok,
        "mixedAgreesWithClosedForms": nb_mixed_ok,
        "mixedFromNotebook": [sp.sstr(to_readable(reduced(v))) for v in nb_mixed],
        "ricciScalarCell583Agrees": nb_r_ok,
    }
    # required source (G^mu_nu = kappa T^mu_nu, T^4_4 = -rho, T^i_i = p_i)
    rho_req = -closed[4] / KAPPA
    p_req = [closed[mu] / KAPPA for mu in range(8) if mu != 4]
    m["rhoRequired"] = expr_text(rho_req)
    m["pressuresRequired_0_1_2_3_5_6_7"] = [expr_text(p) for p in p_req]
    rho_negative = sp.simplify(-rho_req * KAPPA / (3 * H ** 2) - (7 + A4P ** 2)) == 0
    m["rhoRequiredNegative"] = ("rho_req = -3H^2(7 + a4'^2)/kappa <= -21 H^2/kappa < 0"
                                if rho_negative else "mismatch")
    nec0 = sp.factor(sp.simplify(rho_req + p_req[0]))
    sec = sp.factor(sp.simplify(5 * rho_req + sum(p_req)))
    nec_space = [sp.factor(sp.simplify(rho_req + p_req[j])) for j in range(1, 4)]
    nec_time = [sp.factor(sp.simplify(rho_req + p_req[j])) for j in range(4, 7)]
    m["energyConditions_observer_d4"] = {
        "WEC_rho": "violated (rho_req < 0)",
        "NEC_rho_plus_p0": expr_text(nec0) + "  (< 0: violated)",
        "rho_plus_p_1_2_3": [expr_text(v) for v in nec_space],
        "rho_plus_p_5_6_7": [expr_text(v) for v in nec_time],
        "SEC_8D_(5rho + sum p)": expr_text(sec) + "  (<= 0, = 0 only if a4' = 0; SEC also "
                                                  "fails through the NEC)",
        "DEC": "violated (rho_req < 0)",
    }
    nec_ok = sp.simplify(nec0 + 6 * H ** 2 * (1 + A4P ** 2) / KAPPA) == 0
    sec_ok = sp.simplify(sec + 36 * H ** 2 * A4P ** 2 / KAPPA) == 0
    rho_req_c = canon_r(rho_req)
    x0_independent_req = is_zero(d0(rho_req_c))
    m["rhoRequired_x0Independent"] = x0_independent_req
    m["sourceByDirac16complex"] = "see P_source (T^mu_nu of explicit dirac16complex states)"
    ok = (r_ok and off_ok and g_ok and all(bianchi) and nb_cov_ok and nb_mixed_ok and nb_r_ok
          and rho_negative and nec_ok and sec_ok and x0_independent_req)
    return ok, {"P_einstein": m}, {"ricci": ric, "Gmixed": g_mixed}


# -- can a dirac16complex state supply the source? ------------------------------

MEFF = sp.Symbol("Meff", real=True)

# the 15 off-diagonal bilinears of the x0-independent state: name -> (mask of the
# three-gamma product, ordered factors)
SOURCE_BILINEARS = tuple(
    [("V%d" % a, (0, a, 4)) for a in TRANSVERSE6]
    + [("W%d%d" % (i, j), (i, 4, j)) for i in SPACE for j in EXTRA_TIMES])

# exact examples (H = 1): Psi = exp(i omega x4) u0, u0 = sqrt(S / v^dag C v) v
SOURCE_EXAMPLES = (
    {"label": "A", "m": sp.Integer(5), "lam": sp.Integer(0), "kappa": sp.Integer(1),
     "c": sp.sqrt(5), "S": sp.Rational(-36, 5), "Meff": sp.Integer(5), "omega": sp.Integer(4),
     "v": (3, -sp.I, 0, 0, 3, sp.I, 0, 0, 1, -3 * sp.I, 0, 0, 1, 3 * sp.I, 0, 0)},
    {"label": "B", "m": sp.Integer(-15), "lam": sp.Rational(25, 6), "kappa": sp.Integer(1),
     "c": sp.Integer(1), "S": sp.Rational(12, 5), "Meff": sp.Integer(-5), "omega": sp.Integer(4),
     "v": (1, 3 * sp.I, 0, 0, 1, -3 * sp.I, 0, 0, -3, -sp.I, 0, 0, -3, sp.I, 0, 0)},
)


def _mask(indices):
    out = 0
    for c in indices:
        out |= 1 << c
    return out


def emt_x0_independent(ctx):
    """Clifford elements Q_mu nu with T_mu nu = u^dagger Q_mu nu u for the
    x0-independent state Psi = u(x4) (K = -3iH in s^(-1/2 + iK/(6H)) u), on shell:
    du/dx4 = A u, A = -gamma^4 (Meff - 3H gamma^0).  S = u^dag C u is x0- and
    x4-independent, so Meff = m + lam S is a constant; U = (lam/2) S^2 is written
    as the bilinear ((Meff - m)/2) S."""
    charge = cl(CHARGE_MASK, sp.Integer(1))
    a_elem = cl_mul(gamma_blade(4, -1), cl_add({0: MEFF}, gamma_blade(0, -3 * H)))
    a_dag = cl_dagger(a_elem, conj_canon)
    right, left = [], []
    for mu in range(8):
        if mu == 4:
            right.append(cl_add(a_elem, ctx.Omega[4]))
            left.append(cl_sub(cl_mul(a_dag, charge), cl_mul(charge, ctx.Omega[4])))
        else:
            right.append(dict(ctx.Omega[mu]))
            left.append(cl_scale(cl_mul(charge, ctx.Omega[mu]), -1))

    def kinetic(mu, nu):
        return cl_sub(cl_mul_all(charge, ctx.gamma_down[mu], right[nu]),
                      cl_mul(left[nu], ctx.gamma_down[mu]))

    kin_half = cl_scale(cl_add(*[cl_sub(cl_mul_all(charge, ctx.gamma_up[mu], right[mu]),
                                        cl_mul(left[mu], ctx.gamma_up[mu])) for mu in range(8)]),
                        sp.Rational(1, 2))
    potential = cl_scale(charge, (MEFF - MASS) / 2)
    lag = cl_sub(cl_sub(kin_half, cl_scale(charge, MASS)), potential)
    q = [[None] * 8 for _ in range(8)]
    for mu in range(8):
        for nu in range(8):
            element = cl_scale(cl_add(kinetic(mu, nu), kinetic(nu, mu)), -sp.Rational(1, 4))
            if mu == nu:
                element = cl_add(element, cl_scale(lag, ctx.g[mu]))
            q[mu][nu] = element
    dirac = cl_sub(cl_add(*[cl_mul(ctx.gamma_up[mu], right[mu]) for mu in range(8)]), {0: MEFF})
    s_rate = cl_add(cl_mul(a_dag, charge), cl_mul(charge, a_elem))
    return {"Q": q, "A": a_elem, "Adag": a_dag, "kinHalf": kin_half, "L": lag,
            "dirac": dirac, "S_rate": s_rate}


def _dense_value(ctx, element, u, values):
    """u^dagger (sum_mask c_mask gamma^mask) u with the parameters substituted."""
    total = sp.Integer(0)
    ubar = [sp.conjugate(x) for x in u]
    for mask, c in element.items():
        coefficient = sp.sympify(c).subs(values)
        if coefficient == 0:
            continue
        perm, signs = ctx.blade_sp[mask]
        form = sum(ubar[i] * signs[i] * u[perm[i]] for i in range(16))
        total += coefficient * sp.expand(form)
    return total


def _dense_matrix(ctx, mask):
    return sp.Matrix(ctx.blade_dense(mask))


def check_source(ctx):
    """Whether a dirac16complex state (c-number reading of the bilinears) can satisfy
    G^mu_nu = kappa T^mu_nu in this field."""
    m = {}
    closed = [canon_r(c) for c in closed_einstein_mixed()]
    # (1) every Psi(x0, x4): A_ii = 0 and d_i Psi = 0 give T^i_i = L_s for the six
    # transverse directions, while G^i_i - G^j_j = 2 H^2 a4''
    a_diag_zero = all(cl_is_zero(cl_add(cl_anti(ctx.gamma_down[i], ctx.Omega[i]),
                                        cl_anti(ctx.gamma_down[i], ctx.Omega[i])))
                      for i in TRANSVERSE6)
    g_difference = all(equal(closed[i] - closed[j], 2 * H ** 2 * A2)
                       for i in SPACE for j in EXTRA_TIMES)
    m["everyX0X4State"] = ("T^i_i = T^j_j = L_s for every Psi(x0,x4) (A_ii = 0, d_i Psi = 0) "
                           "while G^i_i - G^j_j = 2 H^2 a4'': a4'' != 0 excludes every such "
                           "state")
    m["transverseDiagonalAnticommutatorsVanish"] = a_diag_zero
    m["einsteinTransverseDifferenceIs2H2a4pp"] = g_difference
    # (2) the zeta plane wave with real K (lam = 0): every coefficient of Q_44 is
    # (x0-independent)/sin z, the required rho is x0-independent and nonzero
    q44 = emt_zeta_wave(ctx)["Q"][4][4]
    cond_scaling = bool(q44) and all(is_zero(d0(c * W ** 6)) and not is_zero(c)
                                     for c in cl_clean(q44).values())
    rho_req = canon_r(-closed_einstein_mixed()[4] / KAPPA)
    rho_req_ok = is_zero(d0(rho_req)) and not is_zero(rho_req)
    m["realKPlaneWave"] = ("Psi = exp((-3H + iK) zeta) u(x4), K real, lam = 0: rho = u^dag Q_44 u "
                           "with Q_44 ~ 1/sin z, rho_req x0-independent and <= -21 H^2/kappa, so "
                           "rho = rho_req on an open z-range forces rho = 0 != rho_req")
    m["realKRho_times_sinz_x0Independent"] = cond_scaling
    # (3) the x0-independent state Psi = u(x4)
    data = emt_x0_independent(ctx)
    q = data["Q"]
    charge = cl(CHARGE_MASK, sp.Integer(1))
    dirac_ok = cl_is_zero(data["dirac"])
    s_conserved = cl_is_zero(data["S_rate"])
    kin_ok = cl_equal(data["kinHalf"], cl_scale(charge, MEFF))
    t44_ok = cl_equal(cl_scale(q[4][4], ctx.ginv[4]), cl_scale(charge, -(MASS + MEFF) / 2))
    tt_ok = all(cl_equal(cl_scale(q[mu][mu], ctx.ginv[mu]), cl_scale(charge, (MEFF - MASS) / 2))
                for mu in range(8) if mu != 4)
    off_ok, off_list = True, []
    for mu in range(8):
        for nu in range(mu + 1, 8):
            element = cl_clean(cl_mul(charge, q[mu][nu]))   # C Q: gamma products
            if (mu, nu) == (0, 4) or {mu, nu} <= set(SPACE) or {mu, nu} <= set(EXTRA_TIMES):
                expected = None
            elif mu in (0, 4) or nu == 4:
                expected = _mask((0, nu if mu in (0, 4) else mu, 4))
            else:
                expected = _mask((mu, nu, 4))
            if expected is None:
                off_ok = off_ok and not element
            else:
                off_ok = off_ok and list(element) == [expected]
                if list(element) == [expected]:
                    off_list.append("T_%d%d = (%s) Psibar %s Psi" % (
                        mu, nu, sp.sstr(to_readable(reduced(element[expected]))),
                        blade_label(expected)))
    m["x0Independent"] = {
        "ansatz": "Psi = u(x4), du/dx4 = -gamma^4 (Meff - 3H gamma^0) u, S = u^dag C u constant",
        "diracExact": dirac_ok, "S_conserved": s_conserved, "kineticHalfIsMeffS": kin_ok,
        "T44_is_minus_(mS+U)": t44_ok, "Tmumu_is_SUprime_minus_U": tt_ok,
        "offDiagonalAre15ThreeGammaBilinears": off_ok, "offDiagonal": off_list,
    }
    # conditions with the 15 bilinears zero: G^4_4 = kappa T^4_4, G^0_0 = kappa T^0_0
    t44 = -(MASS + MEFF) / 2 * SSYM
    tt = (MEFF - MASS) / 2 * SSYM
    solution = sp.solve([closed[4] - KAPPA * t44, closed[0] - KAPPA * tt], [MASS, MEFF], dict=True)
    cond_ok = (len(solution) == 1
               and equal(solution[0][MASS], -36 * H ** 2 / (KAPPA * SSYM))
               and equal(solution[0][MEFF], -6 * H ** 2 * (1 + A1 ** 2) / (KAPPA * SSYM))
               and equal((solution[0][MEFF] - solution[0][MASS]) * SSYM,
                         2 * H ** 2 * (15 - 3 * A1 ** 2) / KAPPA))
    if cond_ok:
        rest = [closed[mu] - KAPPA * (t44 if mu == 4 else tt) for mu in range(8)]
        rest = [sp.sympify(r).subs(solution[0]) for r in rest]
        cond_ok = (all(is_zero(r.subs(A2, 0)) for r in rest)
                   and not all(is_zero(r) for r in rest))
    m["x0IndependentConditions"] = ("a4'' = 0, m S = -36 H^2/kappa, lam S^2 = Meff S - m S = "
                                    "2 H^2 (15 - 3 a4'^2)/kappa, Meff = -6 H^2 (1 + a4'^2)/(kappa S), "
                                    "15 bilinears zero")
    m["x0IndependentConditionsVerified"] = cond_ok
    # explicit exact examples (H = 1)
    examples, examples_ok = {}, True
    g_mat = [sp.Matrix(ctx.gamma[a]) for a in range(8)]
    c_mat = sp.Matrix(ctx.charge)
    eye = sp.eye(16)

    def s_ab(a, b):
        return (g_mat[a] * g_mat[b] - g_mat[b] * g_mat[a]) / 4

    j_gen = [s_ab(2, 3) - s_ab(6, 7), s_ab(3, 1) - s_ab(7, 5), s_ab(1, 2) - s_ab(5, 6)]
    for ex in SOURCE_EXAMPLES:
        w = ex["omega"]
        a_mat = -g_mat[4] * (ex["Meff"] * eye - 3 * g_mat[0])
        basis = sp.Matrix.vstack(*j_gen, a_mat - sp.I * w * eye).nullspace()
        q_mat = sp.Matrix.hstack(*basis) if basis else sp.zeros(16, 0)
        forms = {}
        for name, factors in SOURCE_BILINEARS:
            x = c_mat * g_mat[factors[0]] * g_mat[factors[1]] * g_mat[factors[2]]
            forms[name] = sp.simplify(q_mat.H * x * q_mat)
        nonzero = sorted(name for name, f in forms.items() if f != sp.zeros(*f.shape))
        construction = (w ** 2 == ex["Meff"] ** 2 - 9 and len(basis) == 2
                        and nonzero == ["W15", "W26", "W37"]
                        and forms["W15"] == forms["W26"] == forms["W37"])
        v = sp.Matrix(ex["v"])
        in_span = sp.Matrix.hstack(q_mat, v).rank() == 2
        eigen = sp.simplify(a_mat * v - sp.I * w * v) == sp.zeros(16, 1)
        bilinears_zero = all(sp.simplify((v.H * c_mat * g_mat[f[0]] * g_mat[f[1]] * g_mat[f[2]]
                                          * v)[0]) == 0 for _, f in SOURCE_BILINEARS)
        s_v = sp.simplify((v.H * c_mat * v)[0])
        u0 = [sp.sqrt(ex["S"] / s_v) * x for x in ex["v"]]
        s_u0 = sp.simplify(sum(sp.conjugate(u0[i]) * (c_mat * sp.Matrix(u0))[i]
                               for i in range(16)))
        consistent = (s_u0 == ex["S"] and ex["m"] + ex["lam"] * s_u0 == ex["Meff"]
                      and ex["m"] * ex["S"] == -36 / ex["kappa"]
                      and sp.simplify(ex["lam"] * ex["S"] ** 2
                                      - 2 * (15 - 3 * ex["c"] ** 2) / ex["kappa"]) == 0)
        values = {H: 1, MASS: ex["m"], MEFF: ex["Meff"], A1: ex["c"], A2: 0, KAPPA: ex["kappa"]}
        residual_zero, residual_bad = True, False
        for mu in range(8):
            for nu in range(8):
                t_value = _dense_value(ctx, cl_scale(q[mu][nu], ctx.ginv[mu]), u0, values)
                g_value = closed[mu] if mu == nu else sp.Integer(0)
                r = sp.sympify(g_value).subs(values) - ex["kappa"] * t_value
                residual_zero = residual_zero and is_zero(sp.expand(r))
                if mu == nu:   # negative control: slope c + 1
                    bad = {**values, A1: ex["c"] + 1}
                    rb = (sp.sympify(g_value).subs(bad) - ex["kappa"]
                          * _dense_value(ctx, cl_scale(q[mu][nu], ctx.ginv[mu]), u0, bad))
                    residual_bad = residual_bad or not is_zero(sp.expand(rb))
        rho = ex["m"] * s_u0 + ex["lam"] / 2 * s_u0 ** 2
        ok_ex = (construction and in_span and eigen and bilinears_zero and consistent
                 and residual_zero and residual_bad
                 and rho == -3 * (7 + ex["c"] ** 2) / ex["kappa"])
        examples_ok = examples_ok and ok_ex
        examples[ex["label"]] = {
            "H": "1", "kappa": str(ex["kappa"]), "m": str(ex["m"]), "lam": str(ex["lam"]),
            "a4": sp.sstr(ex["c"] * TS), "Meff": str(ex["Meff"]), "omega": str(w),
            "S": str(s_u0), "v": [sp.sstr(x) for x in ex["v"]],
            "u0NormFactorSquared": str(sp.simplify(ex["S"] / s_v)),
            "rho": str(rho), "pTransverse": str(ex["lam"] / 2 * s_u0 ** 2),
            "construction_dim2_onlyW15W26W37": construction, "vInIntersection": in_span,
            "eigenvector": eigen, "bilinearsZero": bilinears_zero, "conditions": consistent,
            "allGminusKappaT64Zero": residual_zero, "negativeControlSlopePlus1Fails": residual_bad,
        }
    m["x0IndependentExamples"] = examples
    ok = (a_diag_zero and g_difference and cond_scaling and rho_req_ok and dirac_ok
          and s_conserved and kin_ok and t44_ok and tt_ok and off_ok and cond_ok and examples_ok)
    return ok, {"P_source": m}


# -- canonical quantization -----------------------------------------------------

def check_quant(ctx):
    m = {}
    s0 = Fraction(1)
    C = qm_from_int(ctx.charge, s0)
    g4 = qm_from_int(ctx.gamma[4], s0)
    i_unit = QRE({(0, 0, 1): Fraction(1)}, s0)
    B = qm_scale(qm_mul(C, g4), -i_unit)
    I16 = qm_identity(s0)
    herm = qm_is_zero(qm_sub(qm_dagger(B), B))
    square = qm_is_zero(qm_sub(qm_mul(B, B), I16))
    trace = sum((B.get((i, i), QRE.const(0, s0)) for i in range(16)), QRE.const(0, s0))
    traceless = trace.is_zero()
    commutes = qm_is_zero(qm_sub(qm_mul(C, B), qm_mul(B, C)))
    bc = qm_is_zero(qm_sub(qm_mul(B, C), qm_scale(g4, -i_unit)))
    inverse = qm_is_zero(qm_sub(qm_mul(qm_mul(C, g4), B), qm_scale(I16, i_unit)))
    # i gamma^4 C / (g^44 sqrt|g|) with g^44 = -1, curved gamma^4 = flat gamma^4 (h_4 = 1)
    g44_ok = equal(ctx.ginv[4], -1) and equal(ctx.einv[4], 1)
    alt = qm_is_zero(qm_sub(qm_scale(qm_mul(g4, C), -i_unit), B))
    heisenberg = qm_is_zero(qm_sub(qm_scale(qm_mul(B, C), -i_unit), qm_scale(g4, -1)))
    m["B"] = "B = -i C gamma^4"
    m["BHermitian"] = herm
    m["BSquaredIdentity"] = square
    m["BTraceZero_eigenvalues_plus1x8_minus1x8"] = traceless
    m["C_B_commute"] = commutes
    m["B_C_eq_-i_gamma4"] = bc
    m["i_inverse_Cgamma4_eq_B"] = inverse
    m["alternativeForm_i_gamma4_C_over_g44"] = alt and g44_ok
    m["heisenbergReproducesEL"] = heisenberg
    # momentum: time-derivative part (1/2) sqrt|g| (Psibar g^4 d4 Psi - d4 Psibar g^4 Psi)
    # = sqrt|g| Psibar g^4 d4 Psi - (1/2) d4(...) + (1/2) Psibar d4(sqrt|g| gamma^4) Psi
    sqrtg = CZ
    d4_sqrtg_gamma4 = d4(sqrtg * ctx.einv[4])
    momentum_ok = is_zero(d4_sqrtg_gamma4)
    m["momentum"] = "Pi = sqrt|g| Psi^dagger C gamma^4 = cos(z) Psi^dagger C gamma^4"
    m["d4_sqrtg_gamma4_zero"] = momentum_ok
    m["anticommutator"] = ("{Psi_a(x), Psi_b^dagger(y)} = B_ab delta^7(x - y) / cos(z) at equal x4 "
                           "(sqrt|g| = cos z)")
    # Hamiltonian density
    anti_sum = cl_add(*[cl_anti(ctx.gamma_up[j], ctx.Omega[j]) for j in range(8) if j != 4])
    anti_zero = cl_is_zero(anti_sum)
    m["sum_j{gamma^j,Omega_j}_zero"] = anti_zero
    m["hamiltonianDensity"] = (
        "H = cos(z) [ -(1/2) sum_(j != 4) c_j (Psibar g_j d_j Psi - d_j Psibar g_j Psi) + m S + U(S) ]"
        " + total derivative, c = (tan z, s^(-1/6) e^{-a4} x3, -, s^(-1/6) e^{a4} x3); = sqrt|g| T_44")
    # divergence identity d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu]
    lhs = cl_add(*[cl_d0(cl_scale(ctx.gamma_up[0], sqrtg)), cl_d4(cl_scale(ctx.gamma_up[4], sqrtg))])
    rhs = cl_scale(cl_add(*[cl_comm(ctx.gamma_up[mu], ctx.Omega[mu]) for mu in range(8)]), sqrtg)
    divergence_ok = cl_equal(lhs, rhs)
    m["divergenceIdentity"] = divergence_ok
    # good sector Hermiticity: -iM g4, g4 g0, g4 gj (j = 1..3) Hermitian; g4 gj (j = 5..7) not
    herm_parts = {}
    for label, element in (("-iM_g4", gamma_blade(4, -sp.I * MASS)),
                           ("g4_g0", cl_mul(gamma_blade(4), gamma_blade(0)))):
        herm_parts[label] = cl_equal(cl_dagger(element, conj_canon), element)
    for j in TRANSVERSE6:
        element = cl_mul(gamma_blade(4), gamma_blade(j))
        herm_parts["g4_g%d" % j] = ("Hermitian" if cl_equal(cl_dagger(element, conj_canon), element)
                                    else "anti-Hermitian" if cl_equal(
                                        cl_dagger(element, conj_canon), cl_scale(element, -1))
                                    else "neither")
    parts_ok = (herm_parts["-iM_g4"] and herm_parts["g4_g0"]
                and all(herm_parts["g4_g%d" % j] == "Hermitian" for j in SPACE)
                and all(herm_parts["g4_g%d" % j] == "anti-Hermitian" for j in EXTRA_TIMES))
    m["goodSectorMatrixParts"] = herm_parts
    # i (d_zeta + 3H) is symmetric w.r.t. exp(6 H zeta) d zeta (sqrt|g| in zeta coordinates)
    f1, f2_, g1, g2 = [sp.Function(n)(ZETA) for n in ("f1", "f2", "g1", "g2")]
    f, g = f1 + sp.I * f2_, g1 + sp.I * g2
    fbar = f1 - sp.I * f2_

    def op(u):
        return sp.I * (sp.diff(u, ZETA) + 3 * H * u)

    op_f_bar = sp.expand(sp.I * (-1) * (sp.diff(fbar, ZETA) + 3 * H * fbar))  # conj(op f)
    lhs_s = sp.exp(6 * H * ZETA) * (fbar * op(g) - op_f_bar * g)
    rhs_s = sp.diff(sp.I * sp.exp(6 * H * ZETA) * fbar * g, ZETA)
    symmetric_ok = sp.simplify(sp.expand(lhs_s - rhs_s)) == 0
    m["zetaOperatorSymmetric_measure_exp6Hzeta"] = symmetric_ok
    m["goodSector"] = ("h = -i M g4 + i g4 g0 (d_zeta + 3H) + sum_j i c_j g4 g_j d_j is Hermitian "
                       "w.r.t. int sqrt|g| Psi^dag Psi iff there is no dependence on x5, x6, x7 "
                       "(q = 0)")
    # gamma^8 map: gamma^8 anticommutes with gamma^mu, commutes with Omega_mu and C
    g8 = cl(CHIRALITY_MASK, sp.Integer(1))
    anti_ok = all(cl_is_zero(cl_anti(g8, ctx.gamma_up[mu])) for mu in range(8))
    comm_ok = all(cl_is_zero(cl_comm(g8, ctx.Omega[mu])) for mu in range(8))
    charge = cl(CHARGE_MASK, sp.Integer(1))
    s_invariant = cl_equal(cl_mul_all(cl_dagger(g8, conj_canon), charge, g8), charge)
    kinetic_flip = all(cl_equal(cl_mul_all(cl_dagger(g8, conj_canon), charge, ctx.gamma_up[mu], g8),
                                cl_scale(cl_mul(charge, ctx.gamma_up[mu]), -1)) for mu in range(8))
    m["gamma8Map"] = ("Psi -> gamma^8 Psi maps solutions for (m, lam) to solutions for (-m, -lam) "
                      "in this field; S invariant; L_(m,lam)[g8 Psi] = -L_(-m,-lam)[Psi]")
    m["gamma8Checks"] = {"anticommutesWithGammaMu": anti_ok, "commutesWithOmegaMu": comm_ok,
                         "SInvariant": s_invariant, "kineticBilinearFlips": kinetic_flip}
    ok = (herm and square and traceless and commutes and bc and inverse and alt and g44_ok
          and heisenberg and momentum_ok and anti_zero and divergence_ok and parts_ok
          and symmetric_ok and anti_ok and comm_ok and s_invariant and kinetic_flip)
    return ok, {"P_quant": m}


# -- a4 linear ------------------------------------------------------------------

def check_a4linear(ctx):
    m = {}
    cc = sp.Symbol("c", real=True)
    sn, cs = sp.sin(ZARG), sp.cos(ZARG)
    third = sp.Rational(1, 3)
    lin = cc * H * X4                                     # a4(t) = c t, t = H x4
    g_diag = ([cs ** 2 / sn ** 2] + [sn ** third * sp.exp(2 * lin)] * 3 + [sp.Integer(-1)]
              + [-sn ** third * sp.exp(-2 * lin)] * 3)
    gam = christoffel_x(g_diag)
    ric = ricci_from_christoffel(gam)
    ginv = [1 / v for v in g_diag]
    r_lin = canon_x(sum(ginv[mu] * ric[mu][mu] for mu in range(8)))
    g_lin = [canon_x(ginv[mu] * ric[mu][mu]) - r_lin / 2 for mu in range(8)]
    expected_r = 6 * H ** 2 * (cc ** 2 - 7)
    expected_g = ([-3 * H ** 2 * (cc ** 2 - 5)] + [H ** 2 * (15 - 3 * cc ** 2)] * 3
                  + [3 * H ** 2 * (7 + cc ** 2)] + [H ** 2 * (15 - 3 * cc ** 2)] * 3)
    r_ok = equal(r_lin, expected_r)
    g_ok = all(equal(g_lin[mu], expected_g[mu]) for mu in range(8))
    general_ok = all(equal(canon_r(closed_einstein_mixed()[mu]).subs({A1: cc, A2: 0}),
                           expected_g[mu]) for mu in range(8))
    rows = []
    mm = sp.Symbol("M", real=True)
    for label, value in (("a4 = t", sp.Integer(1)),
                         ("a4' = 2(M-1)/3 (cell 150)", 2 * (mm - 1) / 3),
                         ("a4' = 2(M+1)/3 (cell 150)", 2 * (mm + 1) / 3)):
        subs = {cc: value}
        rho = sp.factor(-expected_g[4].subs(subs) / KAPPA)
        pressures = [sp.factor(expected_g[mu].subs(subs) / KAPPA) for mu in range(8) if mu != 4]
        w_eos = sp.factor(sp.simplify(pressures[0] / rho))
        rows.append({"case": label,
                     "R": sp.sstr(sp.factor(expected_r.subs(subs))),
                     "G_mixed_diagonal": [sp.sstr(sp.factor(v.subs(subs))) for v in expected_g],
                     "rho_req": sp.sstr(rho),
                     "p_req_0_1_2_3_5_6_7": [sp.sstr(p) for p in pressures],
                     "isotropic": all(sp.simplify(p - pressures[0]) == 0 for p in pressures),
                     "w_req": sp.sstr(w_eos)})
    m["generalLinear"] = {"a4": "c t", "R": "6*H**2*(c**2 - 7)",
                          "G_mixed_diagonal": [sp.sstr(v) for v in expected_g],
                          "w_req": "(c**2 - 5)/(c**2 + 7) (isotropic pressure for every c)"}
    m["table"] = rows
    first = rows[0]
    numbers_ok = (first["R"] == sp.sstr(-36 * H ** 2)
                  and first["rho_req"] == sp.sstr(sp.factor(-24 * H ** 2 / KAPPA))
                  and first["p_req_0_1_2_3_5_6_7"] == [sp.sstr(sp.factor(12 * H ** 2 / KAPPA))] * 7
                  and first["w_req"] == "-1/2")
    m["recomputedFromMetric"] = r_ok and g_ok
    m["agreesWithGeneralClosedForms"] = general_ok
    m["a4EqualsT_numbers"] = numbers_ok
    ok = r_ok and g_ok and general_ok and numbers_ok and all(r["isotropic"] for r in rows)
    return ok, {"P_a4linear": m}


# -- Wolfram component comparison ------------------------------------------------

_NONE_DERIVATIVE = (None, "none", "None", "Null", "null", "mass")


def _parse_wolfram_expression(text):
    """Wolfram InputForm coefficient -> canonical variables (z, t, a4[t] or x0, x4)."""
    from sympy.parsing.mathematica import parse_mathematica
    replaced = str(text)
    for n in (4, 3, 2, 1):
        replaced = replaced.replace("Derivative[%d][a4][t]" % n, "wfA%d" % n)
        replaced = replaced.replace("Derivative[%d][a4][H*x4]" % n, "wfA%d" % n)
    replaced = replaced.replace("a4[t]", "wfA0").replace("a4[H*x4]", "wfA0")
    replaced = replaced.replace("\\[Lambda]", "lam").replace("\u03bb", "lam")
    replaced = re.sub(r"\bS\b", "wfS", replaced)   # a bare S would parse as sympy.S
    parsed = parse_mathematica(replaced)
    names = {"wfA0": sp.log(EA), "wfA1": A1, "wfA2": A2, "wfA3": A3, "wfA4": A4,
             "H": H, "z": ZS, "m": MASS, "mm": MASS, "lam": LAM, "K": KZ, "KK": KZ,
             "x0": X0, "zeta": ZETA, "wfS": SSYM, "SS": SSYM}
    parsed = parsed.subs({sp.Symbol(k): v for k, v in names.items()})
    return canon_x(canon_r(parsed))


def _parse_python_expression(text):
    """Wolfram's sympy-syntax printer (z, H, a4, a4p, a4pp, m, lam, S) -> canonical."""
    names = {"z": ZS, "H": H, "a4": sp.log(EA), "a4p": A1, "a4pp": A2, "a4ppp": A3,
             "a4pppp": A4, "m": MASS, "lam": LAM, "S": SSYM, "K": KZ, "I": sp.I,
             "sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "exp": sp.exp}
    parsed = sp.sympify(str(text), locals=names)
    return canon_x(canon_r(parsed))


def _find_equations(document):
    """The list of 16 equation records: top-level 'equations', or nested under
    'eulerLagrange' (optionally inside 'components')."""
    queue = [document]
    preferred = None
    while queue:
        node = queue.pop(0)
        if isinstance(node, dict):
            value = node.get("equations")
            if (isinstance(value, list) and len(value) == 16
                    and all(isinstance(e, dict) and "terms" in e for e in value)):
                if preferred is None:
                    preferred = value
            for key in ("eulerLagrange", "components"):
                if key in node:
                    queue.insert(0, node[key])
    return preferred


def _term_texts(term):
    coefficient = term.get("coefficient")
    if isinstance(coefficient, dict):
        return {key: coefficient[key] for key in ("wl", "py") if isinstance(coefficient.get(key), str)}
    return {"wl": coefficient}


def _collect(terms, value_of, printer):
    collected = {}
    for term in terms:
        derivative = term.get("derivative")
        mu = None if derivative in _NONE_DERIVATIVE else int(derivative)
        key = (mu, int(term["component"]))
        texts = _term_texts(term)
        if printer not in texts:
            raise ValueError("printer %s missing" % printer)
        parse = _parse_wolfram_expression if printer == "wl" else _parse_python_expression
        value = value_of(parse(texts[printer]))
        collected[key] = collected[key] + value if key in collected else value
    return collected


def _ours(rows, value_of, diagonal=None):
    collected = {}
    for coefficient, mu, b in rows:
        key = (None if mu in _NONE_DERIVATIVE else mu, b)
        value = value_of(canon_r(coefficient))
        collected[key] = collected[key] + value if key in collected else value
    if diagonal is not None:
        key = (None, diagonal[0])
        collected[key] = collected.get(key, diagonal[1] * 0) + diagonal[1]
    return collected


def check_wolfram_agreement(ctx, path, table, evolution=None):
    """Compare every coefficient of the 16 component equations (and, when present,
    of the evolution form) with the Wolfram component file, at the two exact sample
    points (with lam = 1/2, S = 7/3 so that the U'(S) term is compared too).

    Layout: 16 equation records, either at the top level ('equations') or under
    'eulerLagrange' / 'components' -> 'eulerLagrange'; each record has 'terms' =
    [{component: k, derivative: 0..7 | 'none' | null, coefficient: string or
    {wl: Wolfram InputForm, py: sympy syntax, ...}}] for
    gamma^mu D_mu Psi - (m + lam S) Psi = 0, and optionally 'evolution' -> 'terms'
    for d_4 Psi_n = ...  Every available printer (wl, py) is compared.  A file in
    another layout makes the check false (reported as 'unparsed-layout')."""
    with open(path, "r", encoding="utf-8") as handle:
        document = json.load(handle)
    measurements = {"wolframComponentsFile": os.path.basename(path)}
    equations = _find_equations(document)
    if equations is None:
        measurements["wolframAgreement"] = "unparsed-layout"
        measurements["wolframTopLevelKeys"] = (sorted(document)[:40]
                                               if isinstance(document, dict) else [])
        return False, measurements
    order = []
    for position, equation in enumerate(equations):
        n = equation.get("n", equation.get("component", position))
        order.append(int(n))
    if sorted(order) != list(range(16)):
        measurements["wolframAgreement"] = "unparsed-layout"
        measurements["wolframEquationIndices"] = order
        return False, measurements
    printers = sorted({p for equation in equations for term in equation["terms"]
                       for p in _term_texts(term)})
    mismatches, compared = [], {}
    forms = ["terms"] + (["evolution"] if evolution is not None
                         and all(isinstance(e.get("evolution"), dict) for e in equations)
                         else [])
    for sm in _sample_matrices(ctx):
        env = dict(sm.env)
        env[LAM] = QRE.const(Fraction(1, 2), sm.s0)       # compare the U'(S) = lam S term too
        env[SSYM] = QRE.const(Fraction(7, 3), sm.s0)

        def value_of(expression, env=env, s0=sm.s0):
            return to_qre(expression, env, s0)

        for form in forms:
            for printer in printers:
                count = 0
                for equation, n in zip(equations, order):
                    terms = equation["terms"] if form == "terms" else equation["evolution"]["terms"]
                    try:
                        theirs = _collect(terms, value_of, printer)
                    except (KeyError, TypeError, ValueError, sp.SympifyError) as error:
                        mismatches.append("%s %s %s row %d: %s" % (sm.point["label"], form,
                                                                  printer, n, error))
                        continue
                    if form == "terms":
                        ours = _ours(table[n], value_of,
                                     (n, -value_of(MASS + LAM * SSYM)))
                    else:
                        ours = _ours(evolution[n], value_of)
                    zero = QRE.const(0, sm.s0)
                    for key in sorted(set(ours) | set(theirs), key=str):
                        count += 1
                        if not (ours.get(key, zero) - theirs.get(key, zero)).is_zero():
                            mismatches.append("%s %s %s row %d key %s" % (
                                sm.point["label"], form, printer, n, key))
                label = "%s/%s" % (form, printer)
                compared[label] = compared.get(label, 0) + count
    measurements["wolframAgreement"] = "compared"
    measurements["wolframPrintersCompared"] = printers
    measurements["wolframFormsCompared"] = forms
    measurements["wolframCoefficientsCompared"] = compared
    measurements["wolframMismatchCount"] = len(mismatches)
    measurements["wolframMismatches"] = mismatches[:50]
    ok = not mismatches and bool(compared) and all(v > 0 for v in compared.values())
    return ok, measurements


# ---------------------------------------------------------------------------
# 8. Driver and report
# ---------------------------------------------------------------------------

def _sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _relative(path):
    absolute = os.path.abspath(path)
    try:
        relative = os.path.relpath(absolute, REPOSITORY_ROOT)
    except ValueError:
        return absolute.replace("\\", "/")
    if relative.startswith(".."):
        return absolute.replace("\\", "/")
    return relative.replace("\\", "/")


def _jsonable(value):
    if isinstance(value, bool) or value is None or isinstance(value, (int, str)):
        return value
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    return str(value)


def run_checks(ctx=None, fixture_path=DEFAULT_FIXTURE,
               wolfram_path=DEFAULT_WOLFRAM_COMPONENTS, sample=True,
               require_wolfram=False):
    """Run the fifteen checks and, when the Wolfram component file exists, the
    comparison P_EL_agreesWithWolfram.  With require_wolfram=True (the command-line
    default) a missing component file is a failed P_EL_agreesWithWolfram
    (wolframAgreement = 'missing'), so that the gate cannot pass without the
    comparison; with require_wolfram=False it is skipped (wolframAgreement =
    'not-run').  The top-level measurement 'wolframAgreement' is recorded in every
    case ('compared', 'unparsed-layout', 'missing' or 'not-run')."""
    ctx = Context() if ctx is None else ctx
    checks, measurements, timings = {}, {}, {}

    def record(name, function, *args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        timings[name] = round(time.time() - start, 3)
        checks[name] = bool(result[0])
        measurements.update(result[1])
        return result

    record("P_algebraSetup", check_algebra_setup, ctx, fixture_path)
    record("P_metric", check_metric, ctx)
    record("P_zeta", check_zeta, ctx)
    record("P_christoffel", check_christoffel, ctx)
    record("P_spinconn", check_spinconn, ctx)
    record("P_Omega", check_omega, ctx, sample)
    record("P_gammaConst", check_gamma_const, ctx, sample)
    el = record("P_EL", check_el, ctx, sample)
    record("P_blocks", check_blocks, ctx)
    record("P_EMT", check_emt, ctx, sample)
    record("P_modes", check_modes, ctx, sample)
    record("P_einstein", check_einstein, ctx)
    record("P_source", check_source, ctx)
    record("P_quant", check_quant, ctx)
    record("P_a4linear", check_a4linear, ctx)
    inputs = {}
    if fixture_path and os.path.exists(fixture_path):
        inputs[_relative(fixture_path)] = _sha256_file(fixture_path)
    if wolfram_path and os.path.exists(wolfram_path):
        start = time.time()
        agree, wm = check_wolfram_agreement(ctx, wolfram_path, el[2]["table"],
                                            el[2]["evolution"])
        timings[WOLFRAM_CHECK] = round(time.time() - start, 3)
        checks[WOLFRAM_CHECK] = bool(agree)
        measurements["P_EL_wolfram"] = wm
        measurements["wolframAgreement"] = wm.get("wolframAgreement", "unparsed-layout")
        inputs[_relative(wolfram_path)] = _sha256_file(wolfram_path)
    elif require_wolfram:
        checks[WOLFRAM_CHECK] = False
        measurements["wolframAgreement"] = "missing"
        measurements["wolframComponentsExpectedAt"] = (_relative(wolfram_path)
                                                        if wolfram_path else None)
    else:
        measurements["wolframAgreement"] = "not-run"
    measurements["samplePointDefinitions"] = [dict(p) for p in SAMPLE_POINTS]
    return checks, measurements, timings, inputs


def build_report(checks, measurements, inputs):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    sources = {rel: _sha256_file(os.path.join(script_directory, os.path.basename(rel)))
               for rel in SOURCE_FILES}
    return {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "checks": checks,
        "measurements": _jsonable(measurements),
        "sourceSha256": sources,
        "inputSha256": inputs,
    }


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
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--wolfram-components", default=DEFAULT_WOLFRAM_COMPONENTS,
                        help="component file written by scripts/verify_dirac16complex_"
                             "primordial.wls (default: %(default)s); it must exist "
                             "unless --allow-missing-wolfram is given")
    parser.add_argument("--allow-missing-wolfram", action="store_true",
                        help="skip P_EL_agreesWithWolfram (wolframAgreement=not-run) "
                             "when the component file is absent, instead of failing")
    parser.add_argument("--no-write", action="store_true")
    arguments = parser.parse_args(argv)
    checks, measurements, timings, inputs = run_checks(
        fixture_path=arguments.fixture, wolfram_path=arguments.wolfram_components,
        require_wolfram=not arguments.allow_missing_wolfram)
    if measurements.get("wolframAgreement") == "missing":
        print("error=missing Wolfram component file %s (run wolframscript -file "
              "scripts/verify_dirac16complex_primordial.wls first, or pass "
              "--allow-missing-wolfram)" % _relative(arguments.wolfram_components))
    report = build_report(checks, measurements, inputs)
    lines, failed = report_lines(report)
    for line in lines:
        print(line)
    for name, seconds in timings.items():
        print("timing_%s=%s" % (name, seconds))
    expected = list(CHECK_NAMES) + ([WOLFRAM_CHECK] if WOLFRAM_CHECK in checks else [])
    if list(report["checks"]) != expected:
        print("error=unexpected check set %s" % ",".join(report["checks"]))
        return 2
    if not arguments.no_write:
        os.makedirs(os.path.dirname(os.path.abspath(arguments.output)), exist_ok=True)
        with open(arguments.output, "wb") as handle:
            handle.write(canonical_json_bytes(report))
        print("report=%s" % _relative(arguments.output))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
