"""Independent exact verifier of the dirac16complex algebra (standard library only).

Recomputes every algebraic and flat-space quantization claim of CONTRACT.md
sections 1, 2, 5 and 8 with exact rational / Gaussian-rational arithmetic
(``fractions.Fraction``; no floating point anywhere), compares the result
with the exact fixture written by ``build_dirac16complex_fixture.py`` and,
when present, with the Wolfram algebra report.

Prints one ``check_<name>=true|false`` line per check, one
``measurement_<name>=<value>`` line per measurement, then ``check_count=N``
and ``failed_check_count=K``; exits nonzero if any check failed.  Writes
``artifacts/dirac16complex/arbitrary-field/python-algebra-report.json``.
"""

import argparse
import json
import os
import sys
from fractions import Fraction

try:
    from scripts import d16c_exact as X
    from scripts import build_dirac16complex_fixture as builder
except ModuleNotFoundError:  # executed as "python scripts/check_...py"
    import d16c_exact as X
    import build_dirac16complex_fixture as builder

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIRECTORY = os.path.join(REPOSITORY_ROOT, "artifacts", "dirac16complex",
                                  "arbitrary-field")
DEFAULT_FIXTURE = os.path.join(ARTIFACT_DIRECTORY, "algebra-fixture.json")
DEFAULT_OUTPUT = os.path.join(ARTIFACT_DIRECTORY, "python-algebra-report.json")
DEFAULT_WOLFRAM_REPORT = os.path.join(ARTIFACT_DIRECTORY, "wolfram-algebra-report.json")
DIRAC_MAIN_TRIALITY = os.path.join(REPOSITORY_ROOT, "dirac-main", "artifacts", "exact",
                                   "triality44.json")
DIRAC_MAIN_SPLIT_OCTONION = os.path.join(REPOSITORY_ROOT, "dirac-main", "artifacts",
                                         "exact", "split-octonion.json")
PRODUCER = "scripts/check_dirac16complex_algebra.py"
SOURCE_FILES = (
    "scripts/d16c_exact.py",
    "scripts/build_dirac16complex_fixture.py",
    "scripts/check_dirac16complex_algebra.py",
)

ALGEBRA_CHECKS = (
    "ALG_clifford",
    "ALG_gammaTransposeSymmetry",
    "ALG_chargeMatrix",
    "ALG_expression1",
    "ALG_spinTransposeProperties",
    "ALG_chirality",
    "ALG_faithful",
    "ALG_pinIrreducibleComplex",
    "ALG_spinDecomposition",
    "ALG_cliffordPictureIntertwiner",
    "ALG_octonionPictureIntertwiner",
    "ALG_chargeFormB",
    "ALG_invariantForms",
    "ALG_gamma8Map",
    "ALG_pinLiftCharacter",
    "QNT_flatModeHamiltonian",
    "QNT_kreinSignature",
    "QNT_unitaryAndKreinSubgroups",
    "QNT_currentHermiticity",
)
FIXTURE_CHECK = "ALG_fixtureAgreement"
WOLFRAM_CHECK = "ALG_wolframAgreement"

# Exact rational sample momenta k_j (j = 0,1,2,3,5,6,7; j = 4 is the time
# direction and is excluded) and masses m for QNT_flatModeHamiltonian.
GOOD_SECTOR_SAMPLES = (
    ("1", {}),
    ("3/2", {0: "1/2", 1: "-1/3", 2: "2"}),
    ("0", {0: "1", 1: "1", 2: "1", 3: "1"}),
    ("-2/3", {0: "-2/7", 1: "5/3", 3: "1/4"}),
    ("7/5", {3: "-3"}),
)
EXTRA_TIME_SAMPLES = (
    ("1", {5: "1"}),
    ("1", {0: "1/2", 6: "-2/3"}),
    ("1/2", {0: "1/7", 1: "2/7", 2: "3/7", 3: "4/7", 5: "5/7", 6: "6/7", 7: "1"}),
    ("1", {7: "2"}),
    ("0", {1: "3", 5: "3"}),
)

# Fixed rational vectors u = u_a gamma^a (nonzero norm) for ALG_pinLiftCharacter.
PIN_VECTOR_SAMPLES = (
    ("1", "1/2", "0", "-1/3", "0", "0", "0", "0"),
    ("0", "0", "1/2", "0", "1", "0", "-1/3", "0"),
    ("1", "2", "-1", "1/2", "1/3", "-2", "1", "1/4"),
    ("-3/5", "0", "0", "0", "0", "4/5", "0", "0"),
)


def _frac(text):
    return Fraction(text)


def _json_value(value):
    if isinstance(value, Fraction):
        return X.rational_to_json(value)
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _json_value(item) for key, item in value.items()}
    return value


class Context:
    """Exact objects shared by the checks (constructed independently of the
    fixture file)."""

    def __init__(self):
        self.eta = X.eta()
        self.I16 = X.identity(16)
        self.I8 = X.identity(8)
        self.tau = X.notebook_tau()
        self.taubar = X.notebook_taubar(self.tau)
        self.g = X.notebook_gammas()
        self.C = X.charge_matrix(self.g)
        self.g8 = X.chirality(self.g)
        self.S = X.spin_generators(self.g)
        self.B = X.charge_form_b(self.g)
        self.tensor = X.tensor_gammas()
        self.octonion = X.octonion_gammas()
        self.minus = list(range(8))       # chirality -1 (notebook Psi16upper)
        self.plus = list(range(8, 16))    # chirality +1 (notebook Psi16lower)
        self.p_minus = X.scale(Fraction(1, 2), X.sub(self.I16, self.g8))
        self.p_plus = X.scale(Fraction(1, 2), X.add(self.I16, self.g8))
        self._monomials = None
        self.k_clifford = None
        self.k_octonion = None

    @property
    def monomials(self):
        if self._monomials is None:
            self._monomials = X.monomials(self.g)
        return self._monomials

    def block_diagonal(self, matrix):
        return (X.is_zero(X.sub_block(matrix, self.minus, self.plus))
                and X.is_zero(X.sub_block(matrix, self.plus, self.minus)))

    def block_off_diagonal(self, matrix):
        return (X.is_zero(X.sub_block(matrix, self.minus, self.minus))
                and X.is_zero(X.sub_block(matrix, self.plus, self.plus)))


# ---------------------------------------------------------------------------
# ALG checks
# ---------------------------------------------------------------------------

def check_clifford(ctx):
    ok = all(X.equal(X.anticommutator(ctx.g[a], ctx.g[b]),
                     X.scale(2 * ctx.eta[a][b], ctx.I16))
             for a in range(8) for b in range(8))
    integer = all(value.denominator == 1 for m in ctx.g for row in m for value in row)
    shape_ok = all(X.shape(m) == (16, 16) for m in ctx.g) and len(ctx.g) == 8
    return ok and integer and shape_ok, {
        "ALG_gammaCount": len(ctx.g),
        "ALG_gammaIntegerEntries": integer,
        "ALG_cliffordPairsVerified": 64,
    }


def check_gamma_transpose_symmetry(ctx):
    kinds = []
    ok = True
    for a in range(8):
        symmetric = X.is_symmetric(ctx.g[a])
        antisymmetric = X.is_antisymmetric(ctx.g[a])
        kinds.append("symmetric" if symmetric else ("antisymmetric" if antisymmetric
                                                   else "neither"))
        ok = ok and (symmetric if a < 4 else antisymmetric)
    return ok, {"ALG_gammaTransposeKinds": kinds}


def check_charge_matrix(ctx):
    product = X.matmul_many(ctx.g[0], ctx.g[1], ctx.g[2], ctx.g[3])
    signature = X.symmetric_signature(ctx.C)
    ok = (X.equal(ctx.C, product)
          and X.equal(ctx.C, X.expected_charge_matrix())
          and X.is_symmetric(ctx.C)
          and X.equal(X.matmul(ctx.C, ctx.C), ctx.I16)
          and signature == (8, 8, 0))
    return ok, {"ALG_chargeMatrixSignature": list(signature)}


def check_expression1(ctx):
    results = []
    for a in range(8):
        c_g = X.matmul(ctx.C, ctx.g[a])
        results.append(X.equal(X.transpose(c_g), X.neg(c_g)))
    return all(results), {"ALG_expression1PerFrameIndex": results}


def check_spin_transpose_properties(ctx):
    count = 0
    ok = True
    for (a, b), s in ctx.S.items():
        c_s = X.matmul(ctx.C, s)
        ok = ok and X.is_antisymmetric(c_s)
        count += 1
        for c in range(8):
            anti = X.matmul(ctx.C, X.anticommutator(ctx.g[c], s))
            comm = X.matmul(ctx.C, X.commutator(ctx.g[c], s))
            ok = ok and X.is_symmetric(anti) and X.is_antisymmetric(comm)
            count += 2
    return ok, {"ALG_spinTransposeIdentitiesVerified": count}


def check_chirality(ctx):
    ok = (X.equal(ctx.g8, X.matmul_many(*ctx.g))
          and X.equal(ctx.g8, X.expected_chirality())
          and X.equal(X.matmul(ctx.g8, ctx.g8), ctx.I16)
          and all(X.is_zero(X.anticommutator(ctx.g8, ga)) for ga in ctx.g)
          and all(X.is_zero(X.commutator(ctx.g8, s)) for s in ctx.S.values())
          and X.is_zero(X.commutator(ctx.g8, ctx.C)))
    diagonal = [int(ctx.g8[i][i]) for i in range(16)]
    return ok, {
        "ALG_chiralityDiagonal": diagonal,
        "chirality": X.matrix_to_json(ctx.g8),
    }


def check_faithful(ctx):
    monomials = ctx.monomials
    all_rank = X.rank([X.flatten(m) for _, m in monomials])
    even = [m for subset, m in monomials if len(subset) % 2 == 0]
    odd = [m for subset, m in monomials if len(subset) % 2 == 1]
    even_rank = X.rank([X.flatten(m) for m in even])
    odd_rank = X.rank([X.flatten(m) for m in odd])
    ok = len(monomials) == 256 and all_rank == 256 and len(even) == 128 and even_rank == 128
    return ok, {
        "ALG_monomialCount": len(monomials),
        "ALG_fullAlgebraRank": all_rank,
        "ALG_evenAlgebraRank": even_rank,
        "ALG_oddAlgebraRank": odd_rank,
    }


def check_pin_irreducible_complex(ctx):
    dimension = X.commutant_dimension(ctx.g)
    return dimension == 1, {
        "ALG_pinCommutantDimensionQ": dimension,
        "ALG_pinCommutantArgument": (
            "the commutant equations gamma^a X = X gamma^a have rational coefficients, "
            "so the complex solution space is the complexification of the rational one "
            "(rank is invariant under field extension): dim_C = dim_Q = %d; with "
            "Cl(4,4) (x) C = Mat16(C) this makes C^16 an irreducible complex Pin(4,4) "
            "module" % dimension),
    }


def check_spin_decomposition(ctx):
    spin = list(ctx.S.values())
    dimension = X.commutant_dimension(spin)
    projectors_commute = all(X.is_zero(X.commutator(p, s))
                             for p in (ctx.p_minus, ctx.p_plus) for s in spin)
    block_diagonal = all(ctx.block_diagonal(s) for s in spin)
    minus_action = [X.sub_block(s, ctx.minus, ctx.minus) for s in spin]
    plus_action = [X.sub_block(s, ctx.plus, ctx.plus) for s in spin]
    minus_commutant = X.commutant_dimension(minus_action)
    plus_commutant = X.commutant_dimension(plus_action)
    cross = X.intertwiner_dimension(minus_action, plus_action)
    cross_reverse = X.intertwiner_dimension(plus_action, minus_action)
    even = [m for subset, m in ctx.monomials if len(subset) % 2 == 0]
    minus_even_rank = X.rank([X.flatten(X.sub_block(m, ctx.minus, ctx.minus)) for m in even])
    plus_even_rank = X.rank([X.flatten(X.sub_block(m, ctx.plus, ctx.plus)) for m in even])
    ok = (dimension == 2 and projectors_commute and block_diagonal
          and minus_commutant == 1 and plus_commutant == 1
          and cross == 0 and cross_reverse == 0
          and minus_even_rank == 64 and plus_even_rank == 64)
    return ok, {
        "ALG_spinCommutantDimensionQ": dimension,
        "ALG_spinMinusBlockCommutantDimension": minus_commutant,
        "ALG_spinPlusBlockCommutantDimension": plus_commutant,
        "ALG_spinCrossIntertwinerDimension": cross,
        "ALG_spinCrossIntertwinerDimensionReverse": cross_reverse,
        "ALG_evenAlgebraRankMinusBlock": minus_even_rank,
        "ALG_evenAlgebraRankPlusBlock": plus_even_rank,
    }


def check_clifford_picture_intertwiner(ctx):
    tensor = ctx.tensor
    tensor_clifford = all(X.equal(X.anticommutator(tensor[a], tensor[b]),
                                  X.scale(2 * ctx.eta[a][b], ctx.I16))
                          for a in range(8) for b in range(8))
    dimension = X.intertwiner_dimension(tensor, ctx.g)
    _, k = X.primitive_intertwiner(tensor, ctx.g)
    ctx.k_clifford = k
    measurements = {"ALG_cliffordIntertwinerDimension": dimension}
    if k is None:
        return False, measurements
    k_rank = X.rank(k)
    intertwines = all(X.equal(X.matmul(tensor[a], k), X.matmul(k, ctx.g[a])) for a in range(8))
    k_inverse = X.inverse(k)
    c_dm = X.matmul_many(tensor[0], tensor[1], tensor[2], tensor[3])
    charge_ok = X.equal(X.matmul_many(k, ctx.C, k_inverse), c_dm)
    volume = X.tensor_volume_form()
    image = X.matmul_many(k, ctx.g8, k_inverse)
    if X.equal(image, volume):
        sign = 1
    elif X.equal(image, X.neg(volume)):
        sign = -1
    else:
        sign = 0
    measurements.update({
        "ALG_cliffordIntertwinerRank": k_rank,
        "ALG_cliffordTensorGammasClifford": tensor_clifford,
        "ALG_cliffordKChargeKinvEqualsCdm": charge_ok,
        "ALG_cliffordKChiralityKinvSignVsGGGG": sign,
        "ALG_cliffordKIsSignedPermutation": X.is_signed_permutation(k),
        "K_clifford": X.matrix_to_json(k),
    })
    ok = tensor_clifford and dimension == 1 and k_rank == 16 and intertwines and charge_ok
    return ok, measurements


def _zorn_sanity():
    samples = [
        [_frac(v) for v in ("1/2", "-1", "2/3", "0", "3", "-1/5", "1", "2")],
        [_frac(v) for v in ("-2", "1/3", "0", "1", "-1/2", "4", "-3/7", "1/9")],
        [_frac(v) for v in ("0", "5/4", "-1", "1/2", "2", "0", "1/3", "-1")],
    ]
    unit = X.octonion_basis(0)
    ok = True
    for x in samples:
        ok = ok and X.octonion_product(unit, x) == x and X.octonion_product(x, unit) == x
        ok = ok and X.octonion_product(x, X.octonion_conjugate(x)) == [
            X.octonion_norm(x) * value for value in unit]
        for y in samples:
            xy = X.octonion_product(x, y)
            ok = ok and X.octonion_norm(xy) == X.octonion_norm(x) * X.octonion_norm(y)
            ok = ok and X.octonion_conjugate(xy) == X.octonion_product(
                X.octonion_conjugate(y), X.octonion_conjugate(x))
            # left and right alternative laws
            ok = ok and X.octonion_product(X.octonion_product(x, x), y) == \
                X.octonion_product(x, X.octonion_product(x, y))
            ok = ok and X.octonion_product(X.octonion_product(y, x), x) == \
                X.octonion_product(y, X.octonion_product(x, x))
    x, y, z = samples
    associative = (X.octonion_product(X.octonion_product(x, y), z)
                   == X.octonion_product(x, X.octonion_product(y, z)))
    return ok, associative


def check_octonion_picture_intertwiner(ctx):
    zorn_ok, associative_sample = _zorn_sanity()
    gam = ctx.octonion
    clifford = all(X.equal(X.anticommutator(gam[a], gam[b]),
                           X.scale(2 * ctx.eta[a][b], ctx.I16))
                   for a in range(8) for b in range(8))
    # K_octonion: intertwiner from the octonion picture to the notebook picture,
    # gamma^a K = K Gamma^a (the direction also used by the Wolfram verifier)
    dimension = X.intertwiner_dimension(ctx.g, gam)
    _, k = X.primitive_intertwiner(ctx.g, gam)
    ctx.k_octonion = k
    measurements = {
        "ALG_zornModelIdentitiesOnSamples": zorn_ok,
        "ALG_zornSampleAssociative": associative_sample,
        "ALG_octonionGammasClifford": clifford,
        "ALG_octonionIntertwinerDimension": dimension,
    }
    if k is None:
        return False, measurements
    k_rank = X.rank(k)
    intertwines = all(X.equal(X.matmul(ctx.g[a], k), X.matmul(k, gam[a])) for a in range(8))
    reverse_dimension = X.intertwiner_dimension(gam, ctx.g)
    gram = X.matmul(X.transpose(k), k)
    gram_factor = gram[0][0] if X.equal(gram, X.scale(gram[0][0], ctx.I16)) else None
    upper = X.sub_block(k, ctx.minus, ctx.minus)
    lower = X.sub_block(k, ctx.plus, ctx.plus)
    k_block_diagonal = ctx.block_diagonal(k)
    left = X.octonion_left_matrices()
    tau_equals_left = [X.equal(ctx.tau[a], left[a]) for a in range(8)]
    tau_intertwiner_dimension = X.intertwiner_dimension(left, ctx.tau)
    _, p = X.primitive_intertwiner(left, ctx.tau)
    tau_signed_permutation = (tau_intertwiner_dimension == 1 and p is not None
                              and X.is_signed_permutation(p))
    measurements.update({
        "ALG_octonionIntertwinerRank": k_rank,
        "ALG_octonionIntertwinerDirection": "gamma^a K = K Gamma^a",
        "ALG_octonionReverseIntertwinerDimension": reverse_dimension,
        "ALG_octonionKIsSignedPermutation": X.is_signed_permutation(k),
        "ALG_octonionKBlockDiagonal": k_block_diagonal,
        "ALG_octonionKEqualBlocks": X.equal(upper, lower),
        "ALG_octonionKGramFactor": (X.rational_to_json(gram_factor)
                                    if gram_factor is not None else "not-scalar"),
        "ALG_tauEqualsLeftMultiplicationPerIndex": tau_equals_left,
        "ALG_tauLeftMultiplicationIntertwinerDimension": tau_intertwiner_dimension,
        "ALG_tauEqualsLeftMultiplicationUpToSignedPermutation": tau_signed_permutation,
        "K_octonion": X.matrix_to_json(k),
    })
    dirac_main = "not-run"
    if os.path.exists(DIRAC_MAIN_TRIALITY):
        with open(DIRAC_MAIN_TRIALITY, "rb") as handle:
            document = json.loads(handle.read().decode("utf-8"))
        generators = [X.fraction_matrix(m) for m in document["octonionCliffordGenerators"]]
        dirac_main = all(X.equal(generators[a], gam[a]) for a in range(8))
    measurements["ALG_octonionGammasEqualDiracMainTriality44Json"] = dirac_main
    # K_clifford K_octonion intertwines Gamma -> gammaHat (gammaHat K_c K_o = K_c gamma K_o
    # = K_c K_o Gamma); compare with dirac-main's independently published
    # canonicalCliffordIntertwiner (gammaHat K = K Gamma)
    canonical = "not-run"
    if os.path.exists(DIRAC_MAIN_TRIALITY) and ctx.k_clifford is not None:
        published = X.fraction_matrix(document["canonicalCliffordIntertwiner"])
        composite = X.matmul(ctx.k_clifford, k)
        composite = X.fraction_matrix(
            X.reshape(X.primitive_integer_vector(X.flatten(composite)), 16, 16))
        canonical = X.equal(composite, published)
    measurements["ALG_KcliffordKoctonionEqualsDiracMainCanonicalIntertwiner"] = canonical
    dirac_main_tensor = "not-run"
    if os.path.exists(DIRAC_MAIN_SPLIT_OCTONION):
        with open(DIRAC_MAIN_SPLIT_OCTONION, "rb") as handle:
            document = json.loads(handle.read().decode("utf-8"))
        tensor = document["multiplicationTensor"]
        dirac_main_tensor = all(
            X.octonion_product(X.octonion_basis(i), X.octonion_basis(j))
            == [Fraction(v) for v in tensor[i][j]] for i in range(8) for j in range(8))
    measurements["ALG_zornProductEqualsDiracMainSplitOctonionJson"] = dirac_main_tensor
    ok = (zorn_ok and clifford and dimension == 1 and reverse_dimension == 1
          and k_rank == 16 and intertwines)
    return ok, measurements


def check_charge_form_b(ctx):
    b = ctx.B
    identity = X.cidentity(16)
    hermitian = X.cis_hermitian(b)
    square = X.cequal(X.cmatmul(b, b), identity)
    rank_minus_one = X.crank(X.csub(b, identity))
    rank_plus_one = X.crank(X.cadd(b, identity))
    eigen_plus = 16 - rank_minus_one
    eigen_minus = 16 - rank_plus_one
    signature = X.hermitian_signature(b)
    c = X.cmatrix(ctx.C)
    commutes = X.cis_zero(X.ccommutator(c, b))
    minus_i_g4 = (X.zeros(16), X.neg(ctx.g[4]))
    bc_ok = X.cequal(X.cmatmul(b, c), minus_i_g4)
    ok = (hermitian and square and eigen_plus == 8 and eigen_minus == 8
          and signature == (8, 8, 0) and commutes and bc_ok)
    return ok, {
        "ALG_chargeFormBEigenvalueMultiplicities": {"plus1": eigen_plus, "minus1": eigen_minus},
        "ALG_chargeFormBHermitianSignature": list(signature),
    }


def check_invariant_forms(ctx):
    spin = list(ctx.S.values())
    left = [X.transpose(s) for s in spin]
    right = [X.neg(s) for s in spin]
    basis = X.intertwiner_basis(left, right)       # S^T M + M S = 0
    c_minus = X.matmul(ctx.C, ctx.p_minus)
    c_plus = X.matmul(ctx.C, ctx.p_plus)

    def invariant(m):
        return all(X.is_zero(X.add(X.matmul(X.transpose(s), m), X.matmul(m, s))) for s in spin)

    spanned = (invariant(c_minus) and invariant(c_plus)
               and X.rank([X.flatten(c_minus), X.flatten(c_plus)]) == 2
               and X.rank([X.flatten(m) for m in basis]
                          + [X.flatten(c_minus), X.flatten(c_plus)]) == len(basis))
    forms = basis + [c_minus, c_plus]
    even = all(ctx.block_diagonal(m) for m in forms)
    odd_with_g4 = all(ctx.block_off_diagonal(X.matmul(m, ctx.g[4])) for m in forms)
    ok = len(basis) == 2 and spanned and even and odd_with_g4
    return ok, {
        "ALG_invariantFormDimensionQ": len(basis),
        "ALG_invariantFormsSpannedByCPminusCPplus": spanned,
        "ALG_invariantFormsBlockDiagonal": even,
        "ALG_invariantFormsTimesGamma4BlockOffDiagonal": odd_with_g4,
        "ALG_invariantFormsCPminusCPplusSymmetric": (X.is_symmetric(c_minus)
                                                    and X.is_symmetric(c_plus)),
    }


def check_gamma8_map(ctx):
    g8t = X.transpose(ctx.g8)
    adjoint_ok = X.equal(X.matmul(g8t, ctx.C), X.matmul(ctx.C, ctx.g8))
    mass_invariant = X.equal(X.matmul_many(g8t, ctx.C, ctx.g8), ctx.C)
    kinetic_flip = all(
        X.equal(X.matmul_many(g8t, ctx.C, ga, ctx.g8), X.neg(X.matmul(ctx.C, ga)))
        for ga in ctx.g)
    connection_commutes = all(X.is_zero(X.commutator(ctx.g8, s)) for s in ctx.S.values())
    connection_term_flip = all(
        X.equal(X.matmul_many(g8t, ctx.C, ga, s, ctx.g8),
                X.neg(X.matmul_many(ctx.C, ga, s)))
        for ga in ctx.g for s in ctx.S.values())
    ok = adjoint_ok and mass_invariant and kinetic_flip and connection_commutes \
        and connection_term_flip
    return ok, {
        "ALG_gamma8MapKineticSign": -1 if kinetic_flip else 0,
        "ALG_gamma8MapMassSign": 1 if mass_invariant else 0,
        "ALG_gamma8MapPotentialSign": 1 if mass_invariant else 0,
        "ALG_gamma8MapLagrangianStatement": (
            "Psi -> gamma8 Psi: K -> -K, S = Psibar Psi -> S, hence "
            "L_{m,U}[gamma8 Psi] = -L_{-m,-U}[Psi]; the contract form L_m -> -L_{-m} "
            "holds exactly when U = 0"),
    }


def _vector_matrix(ctx, u):
    matrix = X.zeros(16)
    for a in range(8):
        if u[a]:
            matrix = X.add(matrix, X.scale(u[a], ctx.g[a]))
    return matrix


def _vector_components(ctx, matrix):
    """Components v_c of v = v_c gamma^c, via tr(v gamma^c) = 16 eta^cc v_c."""
    return [X.trace(X.matmul(matrix, ctx.g[c])) / (16 * ctx.eta[c][c]) for c in range(8)]


def check_pin_lift_character(ctx):
    vectors = [[Fraction(1 if i == a else 0) for i in range(8)] for a in range(8)]
    vectors += [[_frac(v) for v in sample] for sample in PIN_VECTOR_SAMPLES]
    ok = True
    s_u = []
    mass_factor = []
    kinetic_untwisted = []
    kinetic_twisted = []
    norms = []
    lorentz_ok = True
    for u in vectors:
        norm = sum((ctx.eta[a][a] * u[a] * u[a] for a in range(8)), Fraction(0))
        norms.append(norm)
        if norm == 0:
            ok = False
            continue
        um = _vector_matrix(ctx, u)
        umt = X.transpose(um)
        u_inverse = X.scale(1 / norm, um)
        ok = ok and X.equal(X.matmul(um, um), X.scale(norm, ctx.I16))
        # u^T C = s_u C u
        if X.equal(X.matmul(umt, ctx.C), X.neg(X.matmul(ctx.C, um))):
            s_u.append(-1)
        elif X.equal(X.matmul(umt, ctx.C), X.matmul(ctx.C, um)):
            s_u.append(1)
        else:
            s_u.append(0)
            ok = False
        # mass term: u^T C u = f_m C
        mass = X.matmul_many(umt, ctx.C, um)
        f_m = next(mass[i][j] / ctx.C[i][j] for i in range(16) for j in range(16)
                   if ctx.C[i][j] != 0)
        ok = ok and X.equal(mass, X.scale(f_m, ctx.C)) and f_m == -norm
        mass_factor.append(f_m)
        # kinetic term: u^T (C gamma^b) u = f_k C Lambda(gamma^b)
        f_untwisted = set()
        f_twisted = set()
        lam = []
        for b in range(8):
            conjugated = X.matmul_many(um, ctx.g[b], u_inverse)       # u gamma^b u^-1
            components = _vector_components(ctx, conjugated)
            lam.append(components)
            lorentz_ok = lorentz_ok and X.equal(_vector_matrix(ctx, components), conjugated)
            twisted = X.neg(conjugated)                                # alpha(u) gamma^b u^-1
            lhs = X.matmul_many(umt, ctx.C, ctx.g[b], um)
            for factor, image, bucket in ((-norm, conjugated, f_untwisted),
                                          (norm, twisted, f_twisted)):
                if X.equal(lhs, X.scale(factor, X.matmul(ctx.C, image))):
                    bucket.add(factor)
                else:
                    bucket.add(None)
        # Lambda (rows b: gamma^b -> Lambda_b^c gamma^c) preserves eta
        lam_matrix = [[lam[b][c] for c in range(8)] for b in range(8)]
        lorentz_ok = lorentz_ok and X.equal(
            X.matmul_many(lam_matrix, ctx.eta, X.transpose(lam_matrix)), ctx.eta)
        ok = ok and f_untwisted == {-norm} and f_twisted == {norm}
        kinetic_untwisted.append(-norm if f_untwisted == {-norm} else None)
        kinetic_twisted.append(norm if f_twisted == {norm} else None)
    # products of two vectors: g^T C g = n(u1) n(u2) C
    pairs = [(0, 4), (1, 5), (0, 1), (4, 5), (8, 9), (10, 11)]
    product_factors = []
    for i, j in pairs:
        u1, u2 = vectors[i], vectors[j]
        m = X.matmul(_vector_matrix(ctx, u1), _vector_matrix(ctx, u2))
        expected = norms[i] * norms[j]
        product_factors.append(expected)
        ok = ok and X.equal(X.matmul_many(X.transpose(m), ctx.C, m), X.scale(expected, ctx.C))
    flip = X.matmul(ctx.g[0], ctx.g[4])
    spinor_norm_flip = X.equal(X.matmul_many(X.transpose(flip), ctx.C, flip), X.neg(ctx.C))
    ok = ok and lorentz_ok and spinor_norm_flip and all(value == -1 for value in s_u)
    return ok, {
        "ALG_pinLiftVectorNorms": _json_value(norms),
        "ALG_pinLiftTransposeSign_s_u": s_u,
        "ALG_pinLiftMassFactor": _json_value(mass_factor),
        "ALG_pinLiftKineticFactorUntwisted": _json_value(kinetic_untwisted),
        "ALG_pinLiftKineticFactorTwisted": _json_value(kinetic_twisted),
        "ALG_pinLiftUntwistedAdjointInO44": lorentz_ok,
        "ALG_pinLiftProductPairs": [list(p) for p in pairs],
        "ALG_pinLiftProductBilinearFactor": _json_value(product_factors),
        "ALG_pinLiftGamma0Gamma4FlipsPsibarPsi": spinor_norm_flip,
        "ALG_pinLiftQuarticPotentialFactor": _json_value([f * f for f in mass_factor]),
        "ALG_pinLiftInteractingNote": (
            "for a unit spacelike u (character -1) S -> -S while U(S) = (lambda/2) S^2 is "
            "invariant, so L_{m,lambda} -> -L_{m,-lambda} and the field equation "
            "gamma^mu D_mu Psi = (m + lambda S) Psi maps to the lambda -> -lambda equation; "
            "L -> +-L and Pin(4,4)-covariance of the field equations are exact for U = 0"),
        "ALG_pinLiftCharacterStatement": (
            "Psi -> u Psi with u^2 = n(u): u^T C = -C u, Psibar Psi -> -n(u) Psibar Psi; "
            "untwisted lift (v -> u v u^-1): kinetic term -> -n(u) x kinetic (same as mass, "
            "so the free Lagrangian goes to -n(u) L); twisted lift (v -> alpha(u) v u^-1): "
            "kinetic -> +n(u), opposite to mass; for g = u1 u2 Psibar Psi -> n(u1) n(u2) "
            "Psibar Psi (spinor norm), gamma0 gamma4 flips it; U(S) = (lambda/2) S^2 is "
            "invariant under every sign flip of S"),
    }


# ---------------------------------------------------------------------------
# QNT checks
# ---------------------------------------------------------------------------

def _momentum_vector(entries):
    k = [Fraction(0)] * 8
    for j, value in entries.items():
        if j == 4:
            raise ValueError("k_4 is not a spatial momentum")
        k[j] = _frac(value)
    return k


def flat_mode_hamiltonian(ctx, mass, k):
    """h_k = -i m gamma^4 - gamma^4 sum_{j != 4} gamma^j k_j as (real, imag)."""
    slash = X.zeros(16)
    for j in range(8):
        if j != 4 and k[j]:
            slash = X.add(slash, X.scale(k[j], ctx.g[j]))
    real = X.neg(X.matmul(ctx.g[4], slash))
    imag = X.scale(-mass, ctx.g[4])
    return (real, imag)


def _flat_mode_structure(ctx):
    """Structural (all real k, m) proof of the three QNT_flatModeHamiltonian
    statements.  h_k = m M_m + sum_j k_j M_j with M_m = -i gamma^4 and
    M_j = -gamma^4 gamma^j (j != 4)."""
    coefficients = [("m", (X.zeros(16), X.neg(ctx.g[4])))]
    for j in (0, 1, 2, 3, 5, 6, 7):
        coefficients.append((j, (X.neg(X.matmul(ctx.g[4], ctx.g[j])), X.zeros(16))))
    identity = X.cidentity(16)
    # pairwise anticommutators {M_x, M_y} = 2 delta_xy eps_x I, eps_m = 1, eps_j = eta^jj
    clifford = True
    for index, (label_x, m_x) in enumerate(coefficients):
        for label_y, m_y in coefficients[index:]:
            anti = X.cadd(X.cmatmul(m_x, m_y), X.cmatmul(m_y, m_x))
            if label_x == label_y:
                eps = 1 if label_x == "m" else ctx.eta[label_x][label_x]
                clifford = clifford and X.cequal(anti, X.cscale(2 * eps, 0, identity))
            else:
                clifford = clifford and X.cis_zero(anti)
    hermitian = {str(label): X.cis_hermitian(m) for label, m in coefficients}
    anti_hermitian = {str(label): X.cequal(X.cdagger(m), X.cscale(-1, 0, m))
                      for label, m in coefficients}
    commutes = {str(label): X.cis_zero(X.ccommutator(m, ctx.B)) for label, m in coefficients}
    extra = [m for label, m in coefficients if label in (5, 6, 7)]
    # the anti-Hermitian parts / B-commutators of M_5, M_6, M_7 are linearly independent,
    # so they cancel iff k5 = k6 = k7 = 0
    independent_parts = X.rank([X.flatten(X.realify(m)) for m in extra]) == 3
    independent_commutators = X.rank([X.flatten(X.realify(X.ccommutator(m, ctx.B)))
                                      for m in extra]) == 3
    good_labels = ("m", "0", "1", "2", "3")
    ok = (clifford
          and all(hermitian[label] and commutes[label] for label in good_labels)
          and all(anti_hermitian[label] and not commutes[label] for label in ("5", "6", "7"))
          and independent_parts and independent_commutators)
    return ok, {
        "QNT_flatModeCoefficientCliffordAlgebra": clifford,
        "QNT_flatModeCoefficientHermitian": hermitian,
        "QNT_flatModeCoefficientCommutesWithB": commutes,
        "QNT_flatModeExtraTimePartsIndependent": independent_parts and independent_commutators,
    }


def check_flat_mode_hamiltonian(ctx):
    structure_ok, structure = _flat_mode_structure(ctx)
    rows = []
    ok = structure_ok
    for good, samples in ((True, GOOD_SECTOR_SAMPLES), (False, EXTRA_TIME_SAMPLES)):
        for mass_text, entries in samples:
            mass = _frac(mass_text)
            k = _momentum_vector(entries)
            h = flat_mode_hamiltonian(ctx, mass, k)
            hermitian = X.cis_hermitian(h)
            energy_squared = (mass * mass + sum(k[j] * k[j] for j in range(4))
                              - sum(k[j] * k[j] for j in range(5, 8)))
            square_ok = X.cequal(X.cmatmul(h, h), X.cscale(energy_squared, 0, X.cidentity(16)))
            commutes = X.cis_zero(X.ccommutator(h, ctx.B))
            sector = all(k[j] == 0 for j in range(5, 8))
            ok = ok and sector == good and hermitian == good and commutes == good and square_ok
            rows.append({
                "m": X.rational_to_json(mass),
                "k": [X.rational_to_json(k[j]) for j in range(8)],
                "extraTimeFree": sector,
                "hermitian": hermitian,
                "commutesWithB": commutes,
                "energySquared": X.rational_to_json(energy_squared),
                "squareIsEnergySquaredTimesIdentity": square_ok,
            })
    negative = [row for row in rows if Fraction(str(row["energySquared"])) < 0]
    measurements = dict(structure)
    measurements.update({
        "QNT_flatModeSamples": rows,
        "QNT_flatModeSampleCount": len(rows),
        "QNT_flatModeNegativeEnergySquaredSamples": len(negative),
        "QNT_flatModeMomentumConvention": (
            "k_j with j in {0,1,2,3,5,6,7} (k_4 excluded); E^2 = m^2 + k0^2+k1^2+k2^2+k3^2 "
            "- k5^2 - k6^2 - k7^2"),
    })
    return ok, measurements


def check_krein_signature(ctx):
    a = (X.zeros(16), X.neg(ctx.g[4]))            # -i gamma^4
    identity = X.cidentity(16)
    involution = X.cequal(X.cmatmul(a, a), identity)
    plus_dimension = 16 - X.crank(X.csub(a, identity))
    minus_dimension = 16 - X.crank(X.cadd(a, identity))
    half = Fraction(1, 2)
    p_plus = X.cscale(half, 0, X.cadd(identity, a))
    p_minus = X.cscale(half, 0, X.csub(identity, a))
    projector_ok = (X.cequal(X.cmatmul(p_plus, p_plus), p_plus)
                    and X.cequal(X.cmatmul(a, p_plus), p_plus)
                    and X.crank(p_plus) == plus_dimension)
    plus_signature = X.hermitian_signature(X.cmatmul_many(X.cdagger(p_plus), ctx.B, p_plus))
    minus_signature = X.hermitian_signature(X.cmatmul_many(X.cdagger(p_minus), ctx.B, p_minus))
    # independent cross-check: C commutes with -i gamma^4 and equals B on E_+
    c = X.cmatrix(ctx.C)
    c_plus = X.cscale(half, 0, X.cadd(identity, c))
    c_minus = X.cscale(half, 0, X.csub(identity, c))
    cross_check = (X.cis_zero(X.ccommutator(c, a))
                   and (X.crank(X.cmatmul(p_plus, c_plus)), X.crank(X.cmatmul(p_plus, c_minus)))
                   == plus_signature[:2])
    ok = (involution and plus_dimension == 8 and minus_dimension == 8 and projector_ok
          and plus_signature == (4, 4, 8) and minus_signature == (4, 4, 8) and cross_check)
    return ok, {
        "QNT_kreinPositiveEnergyEigenspaceDimension": plus_dimension,
        "QNT_kreinNegativeEnergyEigenspaceDimension": minus_dimension,
        "QNT_kreinBSignatureOnPlusEigenspace": list(plus_signature[:2]),
        "QNT_kreinBSignatureOnMinusEigenspace": list(minus_signature[:2]),
        "QNT_kreinProjectorCrossCheck": cross_check,
    }


def check_unitary_and_krein_subgroups(ctx):
    b_imag = ctx.B[1]            # B = i * b_imag with b_imag real
    anti_hermitian = []
    commuting = []
    krein = []
    for (a, b), s in ctx.S.items():
        if X.is_antisymmetric(s):
            anti_hermitian.append((a, b))
        if X.is_zero(X.commutator(s, b_imag)):
            commuting.append((a, b))
        # S real so S^dagger = S^T;  S^T B + B S = i (S^T b + b S)
        if X.is_zero(X.add(X.matmul(X.transpose(s), b_imag), X.matmul(b_imag, s))):
            krein.append((a, b))
    compact_commuting = [pair for pair in commuting if pair in anti_hermitian]
    expected_unitary = [pair for pair in X.spin_pairs()
                        if set(pair) <= {0, 1, 2, 3} or set(pair) <= {5, 6, 7}]
    expected_krein = [pair for pair in X.spin_pairs() if 4 not in pair]
    krein_failing = [pair for pair in X.spin_pairs() if pair not in krein]
    ok = (compact_commuting == expected_unitary and len(compact_commuting) == 9
          and krein == expected_krein and len(krein) == 21
          and krein_failing == [pair for pair in X.spin_pairs() if 4 in pair])
    return ok, {
        "QNT_unitaryGenerators": [list(p) for p in compact_commuting],
        "QNT_unitaryGeneratorCount": len(compact_commuting),
        "QNT_antiHermitianGeneratorCount": len(anti_hermitian),
        "QNT_generatorsCommutingWithB": [list(p) for p in commuting],
        "QNT_generatorsCommutingWithBCount": len(commuting),
        "QNT_literalClaimExactlyNineCommuteWithB": len(commuting) == 9,
        "QNT_kreinGeneratorCount": len(krein),
        "QNT_kreinFailingGenerators": [list(p) for p in krein_failing],
        "QNT_unitaryCheckMeaning": (
            "unitary (w.r.t. Psi^dagger Psi) generators commuting with B = anti-Hermitian "
            "S^ab with [S^ab,B]=0: exactly the 9 with a,b in {0,1,2,3} or {5,6,7} "
            "(Spin(4)xSpin(3)); the 4 boosts S^{a4} (a<4) also commute with B but are "
            "Hermitian (not unitary), so 13 S^ab commute with B in total; Krein condition "
            "S^T B + B S = 0 holds exactly for the 21 with a,b != 4 (spin(4,3))"),
    }


def check_current_hermiticity(ctx):
    hermitian = []
    for mu in range(8):
        current = (X.zeros(16), X.neg(X.matmul(ctx.C, ctx.g[mu])))    # -i C gamma^mu
        hermitian.append(X.cis_hermitian(current))
    j4 = (X.zeros(16), X.neg(X.matmul(ctx.C, ctx.g[4])))
    equals_b = X.cequal(j4, ctx.B)
    return all(hermitian) and equals_b, {
        "QNT_currentMatrixHermitianPerIndex": hermitian,
        "QNT_currentTimeComponentEqualsB": equals_b,
    }


# ---------------------------------------------------------------------------
# Fixture and Wolfram agreement
# ---------------------------------------------------------------------------

def _parse_matrix_list(value):
    return [X.matrix_from_json(item) for item in value]


def check_fixture_agreement(ctx, fixture_path):
    measurements = {}
    if not os.path.exists(fixture_path):
        measurements["ALG_fixturePresent"] = False
        return False, measurements
    with open(fixture_path, "rb") as handle:
        data = handle.read()
    measurements["ALG_fixturePresent"] = True
    lf_only = b"\r" not in data and data.endswith(b"\n")
    try:
        document = json.loads(data.decode("utf-8"))
    except ValueError:
        measurements["ALG_fixtureParses"] = False
        return False, measurements
    # the checker's own objects (constructed independently of the fixture file)
    expected = {
        "eta": ctx.eta,
        "sigma8": X.sigma8(),
        "tau": ctx.tau,
        "taubar": ctx.taubar,
        "gamma": ctx.g,
        "C": ctx.C,
        "chirality": ctx.g8,
        "gammaClifford": ctx.tensor,
        "gammaOctonion": ctx.octonion,
        "K_clifford": ctx.k_clifford,
        "K_octonion": ctx.k_octonion,
    }
    field_results = {}
    try:
        field_results["schemaVersion"] = document.get("schemaVersion") == 1
        field_results["indexing"] = document.get("indexing") == "zero-based"
        for key in ("eta", "sigma8", "C", "chirality", "K_clifford", "K_octonion"):
            field_results[key] = (expected[key] is not None
                                  and X.equal(X.matrix_from_json(document[key]), expected[key]))
        for key in ("tau", "taubar", "gamma", "gammaClifford", "gammaOctonion"):
            parsed = _parse_matrix_list(document[key])
            field_results[key] = (len(parsed) == len(expected[key])
                                  and all(X.equal(p, e) for p, e in zip(parsed, expected[key])))
        entries = document["S"]
        field_results["S"] = (
            [(entry["a"], entry["b"]) for entry in entries] == list(ctx.S.keys())
            and all(X.equal(X.matrix_from_json(entry["matrix"]), ctx.S[(entry["a"], entry["b"])])
                    for entry in entries))
        field_results["B"] = X.cequal((X.matrix_from_json(document["B"]["real"]),
                                       X.matrix_from_json(document["B"]["imag"])), ctx.B)
    except (KeyError, TypeError, ValueError):
        field_results["structure"] = False
    # JSON round trip of the in-memory construction
    objects = builder.construct_objects()
    regenerated = builder.fixture_bytes(objects)
    round_trip = json.loads(regenerated.decode("utf-8"))
    round_trip_ok = (
        all(X.equal(X.matrix_from_json(round_trip[key]), objects[key])
            for key in ("eta", "C", "chirality", "K_clifford", "K_octonion"))
        and all(X.equal(X.matrix_from_json(entry["matrix"]), objects["S"][(entry["a"], entry["b"])])
                for entry in round_trip["S"])
        and all(X.equal(p, e) for p, e in zip(_parse_matrix_list(round_trip["gamma"]),
                                              objects["gamma"])))
    byte_identical = regenerated == data
    measurements.update({
        "ALG_fixtureFieldAgreement": field_results,
        "ALG_fixtureLfOnlyWithTrailingNewline": lf_only,
        "ALG_fixtureInMemoryJsonRoundTrip": round_trip_ok,
        "ALG_fixtureByteIdenticalToRegeneration": byte_identical,
        "ALG_fixtureSha256": X.sha256_bytes(data),
    })
    ok = all(field_results.values()) and lf_only and round_trip_ok and byte_identical
    return ok, measurements


_WOLFRAM_KEYS = {
    "K_clifford": ("K_clifford", "KClifford", "K_Clifford", "kClifford"),
    "K_octonion": ("K_octonion", "KOctonion", "K_Octonion", "kOctonion"),
    "chirality": ("chirality", "Chirality", "gamma8", "chiralityMatrix",
                  "chiralityDiagonal", "ALG_chiralityDiagonal"),
}


def _parse_wolfram_matrix(key, value):
    """A 16x16 matrix, or (chirality only) its diagonal as a flat list."""
    if isinstance(value, list) and value and all(not isinstance(v, list) for v in value):
        if key != "chirality":
            raise ValueError("flat list only allowed for the chirality diagonal")
        return X.diagonal([X.rational_from_json(v) for v in value])
    return X.matrix_from_json(value)


def _lookup(document, names):
    for container in (document.get("measurements", {}), document):
        if isinstance(container, dict):
            for name in names:
                if name in container:
                    return name, container[name]
    return None, None


def check_wolfram_agreement(ctx, report_path):
    with open(report_path, "rb") as handle:
        data = handle.read()
    measurements = {"wolframReportSha256": X.sha256_bytes(data)}
    try:
        document = json.loads(data.decode("utf-8"))
    except ValueError:
        measurements["wolframReportParses"] = False
        return False, measurements
    expected = {"K_clifford": ctx.k_clifford, "K_octonion": ctx.k_octonion,
                "chirality": ctx.g8}
    results = {}
    found = {}
    directions = {}
    for key, names in _WOLFRAM_KEYS.items():
        name, value = _lookup(document, names)
        found[key] = name
        if value is None or expected[key] is None:
            results[key] = False
            continue
        try:
            matrix = _parse_wolfram_matrix(key, value)
        except (TypeError, ValueError, ZeroDivisionError):
            results[key] = False
            continue
        results[key] = X.shape(matrix) == (16, 16) and X.equal(matrix, expected[key])
        if key == "K_octonion":
            # CONTRACT.md does not fix the direction explicitly: accept the primitive
            # inverse (Gamma^a K = K gamma^a) as well and record which one was found
            inverse = X.fraction_matrix(X.reshape(
                X.primitive_integer_vector(X.flatten(X.inverse(expected[key]))), 16, 16))
            if results[key]:
                directions[key] = "gamma^a K = K Gamma^a"
            elif X.shape(matrix) == (16, 16) and X.equal(matrix, inverse):
                directions[key] = "Gamma^a K = K gamma^a"
                results[key] = True
            else:
                directions[key] = "no-match"
    wolfram_checks = document.get("checks", {}) if isinstance(document.get("checks"), dict) else {}
    measurements.update({
        "wolframMatrixAgreement": results,
        "wolframMatrixKeysFound": found,
        "wolframKOctonionDirection": directions.get("K_octonion", "not-found"),
        "wolframCheckNamesShared": sorted(set(wolfram_checks) & set(ALGEBRA_CHECKS)),
        "wolframChecksFalse": sorted(name for name, value in wolfram_checks.items()
                                     if value is not True),
    })
    return all(results.values()), measurements


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

CHECK_FUNCTIONS = (
    ("ALG_clifford", check_clifford),
    ("ALG_gammaTransposeSymmetry", check_gamma_transpose_symmetry),
    ("ALG_chargeMatrix", check_charge_matrix),
    ("ALG_expression1", check_expression1),
    ("ALG_spinTransposeProperties", check_spin_transpose_properties),
    ("ALG_chirality", check_chirality),
    ("ALG_faithful", check_faithful),
    ("ALG_pinIrreducibleComplex", check_pin_irreducible_complex),
    ("ALG_spinDecomposition", check_spin_decomposition),
    ("ALG_cliffordPictureIntertwiner", check_clifford_picture_intertwiner),
    ("ALG_octonionPictureIntertwiner", check_octonion_picture_intertwiner),
    ("ALG_chargeFormB", check_charge_form_b),
    ("ALG_invariantForms", check_invariant_forms),
    ("ALG_gamma8Map", check_gamma8_map),
    ("ALG_pinLiftCharacter", check_pin_lift_character),
    ("QNT_flatModeHamiltonian", check_flat_mode_hamiltonian),
    ("QNT_kreinSignature", check_krein_signature),
    ("QNT_unitaryAndKreinSubgroups", check_unitary_and_krein_subgroups),
    ("QNT_currentHermiticity", check_current_hermiticity),
)


def compute_algebra(ctx=None):
    """Run the 19 algebra/quantization checks; returns (checks, measurements, ctx)."""
    ctx = Context() if ctx is None else ctx
    checks = {}
    measurements = {}
    for name, function in CHECK_FUNCTIONS:
        result, values = function(ctx)
        checks[name] = bool(result)
        measurements.update(values)
    return checks, measurements, ctx


def _relative(path):
    absolute = os.path.abspath(path)
    try:
        relative = os.path.relpath(absolute, REPOSITORY_ROOT)
    except ValueError:
        return absolute.replace("\\", "/")
    if relative.startswith(".."):
        return absolute.replace("\\", "/")
    return relative.replace("\\", "/")


def verify(fixture_path=DEFAULT_FIXTURE, wolfram_report_path=DEFAULT_WOLFRAM_REPORT,
           precomputed=None):
    """Full verification; returns the report document (not yet written)."""
    if precomputed is None:
        checks, measurements, ctx = compute_algebra()
    else:
        checks, measurements, ctx = precomputed
        checks = dict(checks)
        measurements = dict(measurements)
    fixture_ok, fixture_measurements = check_fixture_agreement(ctx, fixture_path)
    checks[FIXTURE_CHECK] = bool(fixture_ok)
    measurements.update(fixture_measurements)
    inputs = {}
    if os.path.exists(fixture_path):
        inputs[_relative(fixture_path)] = X.sha256_file(fixture_path)
    if wolfram_report_path and os.path.exists(wolfram_report_path):
        wolfram_ok, wolfram_measurements = check_wolfram_agreement(ctx, wolfram_report_path)
        checks[WOLFRAM_CHECK] = bool(wolfram_ok)
        measurements.update(wolfram_measurements)
        inputs[_relative(wolfram_report_path)] = X.sha256_file(wolfram_report_path)
    else:
        measurements["wolframAgreement"] = "not-run"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    sources = {}
    for relative in SOURCE_FILES:
        sources[relative] = X.sha256_file(os.path.join(script_directory,
                                                       os.path.basename(relative)))
    return {
        "schemaVersion": 1,
        "producer": PRODUCER,
        "checks": checks,
        "measurements": _json_value(measurements),
        "sourceSha256": sources,
        "inputSha256": inputs,
    }


def expected_check_names(report):
    names = list(ALGEBRA_CHECKS) + [FIXTURE_CHECK]
    if WOLFRAM_CHECK in report["checks"]:
        names.append(WOLFRAM_CHECK)
    return names


def format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, str)):
        return str(value)
    return json.dumps(value, separators=(",", ":"), ensure_ascii=True)


def report_lines(report):
    lines = []
    for name, value in report["checks"].items():
        lines.append("check_%s=%s" % (name, "true" if value else "false"))
    for name, value in report["measurements"].items():
        lines.append("measurement_%s=%s" % (name, format_value(value)))
    failed = sum(1 for value in report["checks"].values() if not value)
    lines.append("check_count=%d" % len(report["checks"]))
    lines.append("failed_check_count=%d" % failed)
    return lines, failed


def write_report(report, path):
    data = X.canonical_json_bytes(report)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--fixture", default=DEFAULT_FIXTURE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--wolfram-report", default=DEFAULT_WOLFRAM_REPORT)
    arguments = parser.parse_args(argv)
    report = verify(arguments.fixture, arguments.wolfram_report)
    lines, failed = report_lines(report)
    for line in lines:
        print(line)
    names = expected_check_names(report)
    if list(report["checks"]) != names:
        print("error=unexpected check set %s" % ",".join(report["checks"]))
        return 2
    write_report(report, arguments.output)
    print("report=%s" % _relative(arguments.output))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
