"""Exact standard-library linear algebra for the dirac16complex project.

Everything here uses ``fractions.Fraction`` (or Python integers); no floating
point number is ever created.  Conventions follow CONTRACT.md:

* all indices are zero-based;
* ``eta = diag(1, 1, 1, 1, -1, -1, -1, -1)``;
* the primary gamma matrices are the notebook ``T16^A[a]`` in the
  split-octonion block basis, ``gamma^a = [[0, taubar[a]], [tau[a], 0]]``;
* ``C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3``;
* ``gamma^8 = gamma^0 ... gamma^7``;
* ``S^{ab} = (1/4)[gamma^a, gamma^b]``.

Real matrices are lists of lists of ``Fraction``.  A Gaussian-rational
complex matrix is a pair ``(real, imag)`` of real Fraction matrices.
"""

from fractions import Fraction
from itertools import combinations
import hashlib
import json
import math

DIMENSION = 8
SPINOR_DIMENSION = 16
ETA_DIAGONAL = (1, 1, 1, 1, -1, -1, -1, -1)


# ---------------------------------------------------------------------------
# Real (rational) dense matrices
# ---------------------------------------------------------------------------

def fraction_matrix(rows):
    """Convert a nested list of ints/Fractions into a Fraction matrix."""
    return [[Fraction(value) for value in row] for row in rows]


def zeros(rows, columns=None):
    columns = rows if columns is None else columns
    return [[Fraction(0)] * columns for _ in range(rows)]


def identity(size):
    return [[Fraction(1 if i == j else 0) for j in range(size)] for i in range(size)]


def diagonal(values):
    size = len(values)
    return [[Fraction(values[i]) if i == j else Fraction(0) for j in range(size)]
            for i in range(size)]


def shape(matrix):
    return (len(matrix), len(matrix[0]) if matrix else 0)


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def add(left, right):
    return [[a + b for a, b in zip(row_l, row_r)] for row_l, row_r in zip(left, right)]


def sub(left, right):
    return [[a - b for a, b in zip(row_l, row_r)] for row_l, row_r in zip(left, right)]


def neg(matrix):
    return [[-value for value in row] for row in matrix]


def scale(factor, matrix):
    factor = Fraction(factor)
    return [[factor * value for value in row] for row in matrix]


def matmul(left, right):
    """Dense product that skips zero entries (the matrices here are sparse)."""
    rows = len(left)
    inner = len(right)
    columns = len(right[0]) if right else 0
    right_sparse = [[(j, value) for j, value in enumerate(right[k]) if value != 0]
                    for k in range(inner)]
    result = []
    for i in range(rows):
        out = [Fraction(0)] * columns
        for k, a_ik in enumerate(left[i]):
            if a_ik == 0:
                continue
            for j, b_kj in right_sparse[k]:
                out[j] += a_ik * b_kj
        result.append(out)
    return result


def matmul_many(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = matmul(result, matrix)
    return result


def commutator(left, right):
    return sub(matmul(left, right), matmul(right, left))


def anticommutator(left, right):
    return add(matmul(left, right), matmul(right, left))


def equal(left, right):
    if shape(left) != shape(right):
        return False
    return all(a == b for row_l, row_r in zip(left, right) for a, b in zip(row_l, row_r))


def is_zero(matrix):
    return all(value == 0 for row in matrix for value in row)


def is_symmetric(matrix):
    return equal(matrix, transpose(matrix))


def is_antisymmetric(matrix):
    return equal(matrix, neg(transpose(matrix)))


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def kron(left, right):
    rows_r, cols_r = shape(right)
    rows_l, cols_l = shape(left)
    result = zeros(rows_l * rows_r, cols_l * cols_r)
    for i in range(rows_l):
        for j in range(cols_l):
            a_ij = Fraction(left[i][j])
            if a_ij == 0:
                continue
            for k in range(rows_r):
                for l in range(cols_r):
                    result[i * rows_r + k][j * cols_r + l] = a_ij * right[k][l]
    return result


def kron_list(matrices):
    result = fraction_matrix(matrices[0])
    for matrix in matrices[1:]:
        result = kron(result, matrix)
    return result


def block_matrix(blocks):
    """Assemble a block matrix.  ``0`` entries stand for zero blocks whose
    size is inferred from the other blocks in the same block row/column."""
    block_rows = len(blocks)
    block_cols = len(blocks[0])
    heights = [None] * block_rows
    widths = [None] * block_cols
    for r in range(block_rows):
        for c in range(block_cols):
            block = blocks[r][c]
            if isinstance(block, list):
                heights[r], widths[c] = shape(block)
    if None in heights or None in widths:
        raise ValueError("cannot infer block sizes")
    result = []
    for r in range(block_rows):
        for i in range(heights[r]):
            row = []
            for c in range(block_cols):
                block = blocks[r][c]
                if isinstance(block, list):
                    row.extend(Fraction(value) for value in block[i])
                else:
                    if block != 0:
                        raise ValueError("scalar blocks other than 0 are not allowed")
                    row.extend([Fraction(0)] * widths[c])
            result.append(row)
    return result


def sub_block(matrix, row_indices, column_indices):
    return [[matrix[i][j] for j in column_indices] for i in row_indices]


def flatten(matrix):
    return [value for row in matrix for value in row]


def reshape(vector, rows, columns):
    return [list(vector[i * columns:(i + 1) * columns]) for i in range(rows)]


def inverse(matrix):
    """Exact Gauss-Jordan inverse; raises ValueError when singular."""
    size = len(matrix)
    augmented = [[Fraction(value) for value in row] + [Fraction(1 if i == j else 0)
                                                        for j in range(size)]
                 for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((r for r in range(column, size) if augmented[r][column] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for r in range(size):
            if r != column and augmented[r][column] != 0:
                factor = augmented[r][column]
                augmented[r] = [a - factor * b for a, b in zip(augmented[r], augmented[column])]
    return [row[size:] for row in augmented]


def determinant(matrix):
    """Exact determinant by fraction Gaussian elimination."""
    size = len(matrix)
    work = [[Fraction(value) for value in row] for row in matrix]
    det = Fraction(1)
    for column in range(size):
        pivot = next((r for r in range(column, size) if work[r][column] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            det = -det
        pivot_value = work[column][column]
        det *= pivot_value
        for r in range(column + 1, size):
            if work[r][column] != 0:
                factor = work[r][column] / pivot_value
                work[r] = [a - factor * b for a, b in zip(work[r], work[column])]
    return det


# ---------------------------------------------------------------------------
# Sparse exact elimination: rank, reduced row echelon form, nullspace
# ---------------------------------------------------------------------------

def _sparse_row(row):
    if isinstance(row, dict):
        return {column: Fraction(value) for column, value in row.items() if value != 0}
    return {column: Fraction(value) for column, value in enumerate(row) if value != 0}


def reduced_row_echelon(rows):
    """Return ``{pivot_column: row_dict}`` of the exact reduced row echelon
    form over Q.  Every pivot row has a 1 in its pivot column and no entry in
    any other pivot column.  ``rows`` may be dense lists or sparse dicts."""
    pivots = {}
    for raw in rows:
        row = _sparse_row(raw)
        for column in [c for c in row if c in pivots]:
            factor = row.get(column)
            if not factor:
                continue
            for c, value in pivots[column].items():
                new_value = row.get(c, Fraction(0)) - factor * value
                if new_value:
                    row[c] = new_value
                else:
                    row.pop(c, None)
        if not row:
            continue
        pivot_column = min(row)
        pivot_value = row[pivot_column]
        row = {c: value / pivot_value for c, value in row.items()}
        for other_column, other in pivots.items():
            factor = other.get(pivot_column)
            if factor:
                for c, value in row.items():
                    new_value = other.get(c, Fraction(0)) - factor * value
                    if new_value:
                        other[c] = new_value
                    else:
                        other.pop(c, None)
        pivots[pivot_column] = row
    return pivots


def rank(rows):
    """Exact rank over Q of a list of rows (dense lists or sparse dicts)."""
    return len(reduced_row_echelon(rows))


def nullspace(rows, column_count):
    """Exact basis of ``{v : rows . v = 0}`` over Q (one vector per free column,
    free columns in increasing order)."""
    pivots = reduced_row_echelon(rows)
    free_columns = [c for c in range(column_count) if c not in pivots]
    basis = []
    for free in free_columns:
        vector = [Fraction(0)] * column_count
        vector[free] = Fraction(1)
        for pivot_column, row in pivots.items():
            value = row.get(free)
            if value:
                vector[pivot_column] = -value
        basis.append(vector)
    return basis


def primitive_integer_vector(vector):
    """Scale a nonzero rational vector to a primitive integer vector whose first
    nonzero entry is positive (the dirac-main / Wolfram normalisation)."""
    values = [Fraction(v) for v in vector]
    nonzero = [v for v in values if v != 0]
    if not nonzero:
        raise ValueError("zero vector")
    lcm = 1
    for v in nonzero:
        lcm = lcm * v.denominator // math.gcd(lcm, v.denominator)
    integers = [int(v * lcm) for v in values]
    divisor = 0
    for value in integers:
        divisor = math.gcd(divisor, abs(value))
    integers = [value // divisor for value in integers]
    first = next(value for value in integers if value != 0)
    if first < 0:
        integers = [-value for value in integers]
    return integers


def symmetric_signature(matrix):
    """Signature ``(positive, negative, zero)`` of a real symmetric rational
    matrix by exact congruence diagonalisation (Sylvester's law of inertia)."""
    size = len(matrix)
    work = [[Fraction(value) for value in row] for row in matrix]
    if not is_symmetric(work):
        raise ValueError("matrix is not symmetric")
    positive = negative = 0
    active = list(range(size))
    while active:
        pivot = next((i for i in active if work[i][i] != 0), None)
        if pivot is None:
            pair = next(((i, j) for i in active for j in active
                         if i < j and work[i][j] != 0), None)
            if pair is None:
                break
            i, j = pair
            # congruence x_i -> x_i + x_j makes the (i, i) entry 2 a_ij != 0
            for k in active:
                work[i][k] += work[j][k]
            for k in active:
                work[k][i] += work[k][j]
            pivot = i
        pivot_value = work[pivot][pivot]
        if pivot_value > 0:
            positive += 1
        else:
            negative += 1
        rest = [k for k in active if k != pivot]
        for k in rest:
            factor = work[k][pivot] / pivot_value
            if factor:
                pivot_row = work[pivot]
                row_k = work[k]
                for l in rest:
                    row_k[l] -= factor * pivot_row[l]
        active = rest
    return (positive, negative, size - positive - negative)


def is_signed_permutation(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        return False
    column_hits = [0] * size
    for row in matrix:
        nonzero = [(j, v) for j, v in enumerate(row) if v != 0]
        if len(nonzero) != 1 or abs(nonzero[0][1]) != 1:
            return False
        column_hits[nonzero[0][0]] += 1
    return all(hits == 1 for hits in column_hits)


# ---------------------------------------------------------------------------
# Gaussian-rational complex matrices, stored as (real, imag) pairs
# ---------------------------------------------------------------------------

def cmatrix(real, imag=None):
    real = fraction_matrix(real)
    imag = zeros(*shape(real)) if imag is None else fraction_matrix(imag)
    return (real, imag)


def cidentity(size):
    return (identity(size), zeros(size))


def cadd(left, right):
    return (add(left[0], right[0]), add(left[1], right[1]))


def csub(left, right):
    return (sub(left[0], right[0]), sub(left[1], right[1]))


def cscale(re_factor, im_factor, matrix):
    """Multiply by the Gaussian rational ``re_factor + i im_factor``."""
    re_factor = Fraction(re_factor)
    im_factor = Fraction(im_factor)
    real, imag = matrix
    return (sub(scale(re_factor, real), scale(im_factor, imag)),
            add(scale(re_factor, imag), scale(im_factor, real)))


def cmatmul(left, right):
    a, b = left
    c, d = right
    return (sub(matmul(a, c), matmul(b, d)), add(matmul(a, d), matmul(b, c)))


def cmatmul_many(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = cmatmul(result, matrix)
    return result


def ccommutator(left, right):
    return csub(cmatmul(left, right), cmatmul(right, left))


def cdagger(matrix):
    return (transpose(matrix[0]), neg(transpose(matrix[1])))


def cequal(left, right):
    return equal(left[0], right[0]) and equal(left[1], right[1])


def cis_zero(matrix):
    return is_zero(matrix[0]) and is_zero(matrix[1])


def cis_hermitian(matrix):
    return cequal(matrix, cdagger(matrix))


def realify(matrix):
    """Real 2n x 2m matrix [[A, -B], [B, A]] of the complex matrix A + i B."""
    real, imag = matrix
    return block_matrix([[real, neg(imag)], [imag, real]])


def crank(matrix):
    """Exact rank over Q(i): half the rational rank of the realified matrix."""
    real_rank = rank(realify(matrix))
    if real_rank % 2:
        raise ArithmeticError("realified rank must be even")
    return real_rank // 2


def hermitian_signature(matrix):
    """Signature (positive, negative, zero) of a Gaussian-rational Hermitian
    matrix: the realification is real symmetric with doubled signature."""
    if not cis_hermitian(matrix):
        raise ValueError("matrix is not Hermitian")
    positive, negative, zero = symmetric_signature(realify(matrix))
    if positive % 2 or negative % 2 or zero % 2:
        raise ArithmeticError("realified signature must be even")
    return (positive // 2, negative // 2, zero // 2)


# ---------------------------------------------------------------------------
# Linear equations for intertwiners and commutants
# ---------------------------------------------------------------------------

def intertwiner_equations(left_list, right_list):
    """Sparse rows of ``left[a] X - X right[a] = 0`` for an n x m unknown X,
    variables ordered row-major (index i*m + j)."""
    rows = []
    for left, right in zip(left_list, right_list):
        n = len(left)
        m = len(right)
        left_sparse = [[(k, v) for k, v in enumerate(left[i]) if v != 0] for i in range(n)]
        right_columns = [[(k, right[k][j]) for k in range(m) if right[k][j] != 0]
                         for j in range(m)]
        for i in range(n):
            for j in range(m):
                row = {}
                for k, value in left_sparse[i]:
                    index = k * m + j
                    row[index] = row.get(index, Fraction(0)) + Fraction(value)
                for k, value in right_columns[j]:
                    index = i * m + k
                    row[index] = row.get(index, Fraction(0)) - Fraction(value)
                row = {c: v for c, v in row.items() if v != 0}
                if row:
                    rows.append(row)
    return rows


def intertwiner_basis(left_list, right_list):
    """Exact basis (as matrices) of ``{X : left[a] X = X right[a] for all a}``."""
    n = len(left_list[0])
    m = len(right_list[0])
    basis = nullspace(intertwiner_equations(left_list, right_list), n * m)
    return [reshape(vector, n, m) for vector in basis]


def intertwiner_dimension(left_list, right_list):
    n = len(left_list[0])
    m = len(right_list[0])
    return n * m - rank(intertwiner_equations(left_list, right_list))


def commutant_dimension(representation):
    return intertwiner_dimension(representation, representation)


def primitive_intertwiner(left_list, right_list):
    """The primitive integer generator of a one-dimensional intertwiner space
    (first nonzero entry in row-major order positive), with the dimension."""
    basis = intertwiner_basis(left_list, right_list)
    if len(basis) != 1:
        return len(basis), None
    n = len(left_list[0])
    m = len(right_list[0])
    return 1, fraction_matrix(reshape(primitive_integer_vector(flatten(basis[0])), n, m))


# ---------------------------------------------------------------------------
# Notebook (split-octonion block basis) gamma matrices
# ---------------------------------------------------------------------------

def eta():
    return diagonal(ETA_DIAGONAL)


def mathematica_signature(sequence):
    """Mathematica's Signature[list]: 0 on repeats, else the permutation sign."""
    items = list(sequence)
    if len(set(items)) != len(items):
        return 0
    inversions = sum(1 for i in range(len(items)) for j in range(i + 1, len(items))
                     if items[i] > items[j])
    return -1 if inversions % 2 else 1


def _qa(h, p, q):
    return mathematica_signature((h, p, q, 4))


def _qb(h, p, q):
    delta = lambda i, j: 1 if i == j else 0
    return delta(p, 4) * delta(q, h) - delta(p, h) * delta(q, 4)


def notebook_s4(h):
    """Self-dual 4x4 block s4[h] (notebook, 1-based h = 1, 2, 3)."""
    return fraction_matrix([[_qa(h, p, q) - _qb(h, p, q) for q in range(1, 5)]
                            for p in range(1, 5)])


def notebook_t4(h):
    """Anti-self-dual 4x4 block t4[h] (notebook, 1-based h = 1, 2, 3)."""
    return fraction_matrix([[_qa(h, p, q) + _qb(h, p, q) for q in range(1, 5)]
                            for p in range(1, 5)])


def sigma8():
    """sigma = [[0, I4], [I4, 0]]."""
    return block_matrix([[0, identity(4)], [identity(4), 0]])


def notebook_tau():
    """tau[0..7] (8x8): tau[0] = I8, tau[h] = [[0, s4],[s4, 0]],
    tau[7-h] = [[0, t4], [-t4, 0]] (h = 1, 2, 3), tau[7] = tau[1]...tau[6]."""
    tau = [None] * 8
    tau[0] = identity(8)
    for h in range(1, 4):
        s4 = notebook_s4(h)
        t4 = notebook_t4(h)
        tau[h] = block_matrix([[0, s4], [s4, 0]])
        tau[7 - h] = block_matrix([[0, t4], [neg(t4), 0]])
    tau[7] = matmul_many(*tau[1:7])
    return tau


def notebook_taubar(tau=None):
    """taubar[0] = I8, taubar[A] = sigma tau[A]^T sigma for A >= 1."""
    tau = notebook_tau() if tau is None else tau
    sigma = sigma8()
    taubar = [identity(8)]
    for a in range(1, 8):
        taubar.append(matmul_many(sigma, transpose(tau[a]), sigma))
    return taubar


def notebook_gammas():
    """gamma^a = T16^A[a] = [[0, taubar[a]], [tau[a], 0]], a = 0..7."""
    tau = notebook_tau()
    taubar = notebook_taubar(tau)
    return [block_matrix([[0, taubar[a]], [tau[a], 0]]) for a in range(8)]


def charge_matrix(gammas):
    """C = gamma^0 gamma^1 gamma^2 gamma^3."""
    return matmul_many(gammas[0], gammas[1], gammas[2], gammas[3])


def chirality(gammas):
    """gamma^8 = gamma^0 gamma^1 ... gamma^7."""
    return matmul_many(*gammas)


def spin_generator(gammas, a, b):
    """S^{ab} = (1/4)[gamma^a, gamma^b]."""
    return scale(Fraction(1, 4), commutator(gammas[a], gammas[b]))


def spin_pairs():
    return list(combinations(range(8), 2))


def spin_generators(gammas):
    """Dictionary {(a, b): S^{ab}} for a < b in lexicographic order."""
    return {(a, b): spin_generator(gammas, a, b) for a, b in spin_pairs()}


def expected_charge_matrix():
    """blockdiag(-sigma, sigma)."""
    sigma = sigma8()
    return block_matrix([[neg(sigma), 0], [0, sigma]])


def expected_chirality():
    """diag(-I8, +I8)."""
    return diagonal([-1] * 8 + [1] * 8)


def charge_form_b(gammas):
    """B = -i C gamma^4 as a Gaussian-rational (real, imag) pair."""
    c_g4 = matmul(charge_matrix(gammas), gammas[4])
    return (zeros(16), neg(c_g4))


def monomials(gammas):
    """All 256 ordered monomials gamma^{a1}...gamma^{ak} (a1 < ... < ak) in
    Mathematica Subsets order (by length, then lexicographic)."""
    size = len(gammas[0])
    result = []
    for length in range(len(gammas) + 1):
        for subset in combinations(range(len(gammas)), length):
            matrix = identity(size)
            for index in subset:
                matrix = matmul(matrix, gammas[index])
            result.append((subset, matrix))
    return result


# ---------------------------------------------------------------------------
# dirac-main tensor-product (Clifford) picture
# ---------------------------------------------------------------------------

POSITIVE_BLOCK = [[0, 1], [1, 0]]    # P
NEGATIVE_BLOCK = [[0, 1], [-1, 0]]   # N
GRADING_BLOCK = [[1, 0], [0, -1]]    # G
IDENTITY_BLOCK = [[1, 0], [0, 1]]


def tensor_generator(slot, block):
    """G^{(x)(slot-1)} (x) block (x) I^{(x)(4-slot)} for slot = 1..4."""
    factors = [GRADING_BLOCK] * (slot - 1) + [block] + [IDENTITY_BLOCK] * (4 - slot)
    return kron_list(factors)


def tensor_gammas():
    """dirac-main gammas ordered (gp1..gp4, gm1..gm4) = frame 0..7."""
    return ([tensor_generator(slot, POSITIVE_BLOCK) for slot in range(1, 5)]
            + [tensor_generator(slot, NEGATIVE_BLOCK) for slot in range(1, 5)])


def tensor_volume_form():
    """G (x) G (x) G (x) G."""
    return kron_list([GRADING_BLOCK] * 4)


# ---------------------------------------------------------------------------
# Zorn vector-matrix split octonions
# ---------------------------------------------------------------------------

def _dot(u, v):
    return sum((a * b for a, b in zip(u, v)), Fraction(0))


def _cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def to_zorn(x):
    """Coordinates x0..x7 -> Zorn data (a, u, v, b)."""
    x = [Fraction(value) for value in x]
    a = x[0] + x[4]
    b = x[0] - x[4]
    u = tuple(x[i] + x[i + 4] for i in range(1, 4))
    v = tuple(-x[i] + x[i + 4] for i in range(1, 4))
    return (a, u, v, b)


def from_zorn(zorn):
    a, u, v, b = zorn
    half = Fraction(1, 2)
    return ([(a + b) * half] + [(u[i] - v[i]) * half for i in range(3)]
            + [(a - b) * half] + [(u[i] + v[i]) * half for i in range(3)])


def zorn_product(left, right):
    """(a,u,v,b)(c,r,w,d) = (ac + u.w, a r + d u - v x w, c v + b w + u x r, v.r + b d)."""
    a, u, v, b = left
    c, r, w, d = right
    vw = _cross(v, w)
    ur = _cross(u, r)
    return (a * c + _dot(u, w),
            tuple(a * r[i] + d * u[i] - vw[i] for i in range(3)),
            tuple(c * v[i] + b * w[i] + ur[i] for i in range(3)),
            _dot(v, r) + b * d)


def octonion_product(x, y):
    return from_zorn(zorn_product(to_zorn(x), to_zorn(y)))


def octonion_conjugate(x):
    return [Fraction(x[0])] + [-Fraction(value) for value in x[1:]]


def octonion_norm(x):
    return sum((Fraction(ETA_DIAGONAL[i]) * Fraction(x[i]) ** 2 for i in range(8)), Fraction(0))


def octonion_basis(index):
    return [Fraction(1 if i == index else 0) for i in range(8)]


def octonion_left_matrix(x):
    """Matrix of L_x(y) = x y: column j is x e_j."""
    columns = [octonion_product(x, octonion_basis(j)) for j in range(8)]
    return transpose(columns)


def octonion_left_matrices():
    return [octonion_left_matrix(octonion_basis(a)) for a in range(8)]


def octonion_gammas():
    """Gamma(e_a) = [[0, L_{conj(e_a)}], [L_{e_a}, 0]]."""
    result = []
    for a in range(8):
        e_a = octonion_basis(a)
        result.append(block_matrix([[0, octonion_left_matrix(octonion_conjugate(e_a))],
                                    [octonion_left_matrix(e_a), 0]]))
    return result


# ---------------------------------------------------------------------------
# Exact JSON serialisation helpers
# ---------------------------------------------------------------------------

def rational_to_json(value):
    """Integers as JSON integers, other rationals as strings "p/q"."""
    value = Fraction(value)
    if value.denominator == 1:
        return int(value.numerator)
    return "%d/%d" % (value.numerator, value.denominator)


def rational_from_json(value):
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("unsupported rational encoding: %r" % (value,))


def matrix_to_json(matrix):
    return [[rational_to_json(value) for value in row] for row in matrix]


def matrix_from_json(rows):
    return [[rational_from_json(value) for value in row] for row in rows]


def canonical_json_bytes(document):
    """Deterministic UTF-8, LF, trailing newline."""
    text = json.dumps(document, indent=2, sort_keys=False, ensure_ascii=True) + "\n"
    return text.encode("utf-8")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as handle:
        return sha256_bytes(handle.read())
