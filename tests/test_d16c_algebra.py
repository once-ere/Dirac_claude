"""Unit tests for the exact dirac16complex algebra (standard library only).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_algebra.py" -v
Tests call the functions directly and write only into tempfile directories.
"""

import contextlib
import io
import json
import math
import os
import random
import sys
import tempfile
import unittest
from fractions import Fraction

try:
    from scripts import d16c_exact as X
    from scripts import build_dirac16complex_fixture as builder
    from scripts import check_dirac16complex_algebra as checker
except ModuleNotFoundError:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                    "scripts"))
    import d16c_exact as X
    import build_dirac16complex_fixture as builder
    import check_dirac16complex_algebra as checker

REPOSITORY_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CL44_SEED = os.path.join(REPOSITORY_ROOT, "dirac-main", "artifacts", "exact", "cl44-seed.json")


def random_rational(generator, bound=9):
    numerator = generator.randint(-bound, bound)
    denominator = generator.randint(1, bound)
    return Fraction(numerator, denominator)


class ExactLinearAlgebraTests(unittest.TestCase):

    def test_rank_nullspace_and_rref(self):
        matrix = [[1, 2, 3], [2, 4, 6], [1, 0, 1]]
        self.assertEqual(X.rank(matrix), 2)
        basis = X.nullspace(matrix, 3)
        self.assertEqual(len(basis), 1)
        product = X.matmul(X.fraction_matrix(matrix), [[v] for v in basis[0]])
        self.assertTrue(X.is_zero(product))
        self.assertEqual(X.rank([{0: 1, 5: 2}, {5: 4, 0: 2}, {3: Fraction(1, 3)}]), 2)

    def test_inverse_and_determinant(self):
        matrix = X.fraction_matrix([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
        self.assertEqual(X.determinant(matrix), Fraction(18))
        self.assertTrue(X.equal(X.matmul(matrix, X.inverse(matrix)), X.identity(3)))
        with self.assertRaises(ValueError):
            X.inverse([[1, 2], [2, 4]])

    def test_symmetric_signature(self):
        self.assertEqual(X.symmetric_signature(X.diagonal([1, -2, 0])), (1, 1, 1))
        self.assertEqual(X.symmetric_signature([[0, 1], [1, 0]]), (1, 1, 0))
        self.assertEqual(X.symmetric_signature([[0, 1, 1], [1, 0, 1], [1, 1, 0]]), (1, 2, 0))
        self.assertEqual(X.symmetric_signature(X.zeros(3)), (0, 0, 3))
        with self.assertRaises(ValueError):
            X.symmetric_signature([[0, 1], [0, 0]])

    def test_complex_rank_and_hermitian_signature(self):
        sigma_y = X.cmatrix(X.zeros(2), [[0, -1], [1, 0]])
        self.assertTrue(X.cis_hermitian(sigma_y))
        self.assertEqual(X.hermitian_signature(sigma_y), (1, 1, 0))
        rank_one = X.cmatrix([[1, 0], [0, -1]], [[0, 1], [1, 0]])   # [[1, i], [i, -1]]
        self.assertEqual(X.crank(rank_one), 1)
        self.assertEqual(X.crank(X.cidentity(3)), 3)

    def test_primitive_integer_vector(self):
        self.assertEqual(X.primitive_integer_vector([0, Fraction(-2, 3), Fraction(4, 3)]),
                         [0, 1, -2])
        self.assertEqual(X.primitive_integer_vector([Fraction(3), Fraction(6)]), [1, 2])

    def test_mathematica_signature(self):
        self.assertEqual(X.mathematica_signature((1, 2, 3, 4)), 1)
        self.assertEqual(X.mathematica_signature((2, 1, 3, 4)), -1)
        self.assertEqual(X.mathematica_signature((3, 1, 2, 4)), 1)
        self.assertEqual(X.mathematica_signature((1, 1, 3, 4)), 0)

    def test_rational_json_round_trip(self):
        values = [Fraction(0), Fraction(-3), Fraction(1, 2), Fraction(-7, 9)]
        encoded = [X.rational_to_json(v) for v in values]
        self.assertEqual(encoded, [0, -3, "1/2", "-7/9"])
        self.assertEqual([X.rational_from_json(v) for v in json.loads(json.dumps(encoded))],
                         values)
        with self.assertRaises(ValueError):
            X.rational_from_json(True)

    def test_kron_and_blocks(self):
        product = X.kron([[1, 2], [3, 4]], [[0, 1], [1, 0]])
        self.assertEqual(X.shape(product), (4, 4))
        # (A (x) B)[i*2+k][j*2+l] = A[i][j] B[k][l]
        self.assertEqual(product[1], [1, 0, 2, 0])
        self.assertEqual(product[2], [0, 3, 0, 4])
        block = X.block_matrix([[0, X.identity(2)], [X.identity(2), 0]])
        self.assertEqual(X.shape(block), (4, 4))
        self.assertEqual((block[0][0], block[0][2], block[3][1]), (0, 1, 1))
        sigma = X.sigma8()
        self.assertTrue(X.equal(X.matmul(sigma, sigma), X.identity(8)))
        self.assertTrue(X.equal(X.sub_block(sigma, range(4), range(4, 8)), X.identity(4)))


class ConstructionTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.g = X.notebook_gammas()
        cls.eta = X.eta()
        cls.C = X.charge_matrix(cls.g)
        cls.I16 = X.identity(16)

    def test_notebook_gammas_clifford_and_transpose(self):
        for a in range(8):
            self.assertEqual(X.shape(self.g[a]), (16, 16))
            for b in range(8):
                self.assertTrue(X.equal(X.anticommutator(self.g[a], self.g[b]),
                                        X.scale(2 * self.eta[a][b], self.I16)))
            if a < 4:
                self.assertTrue(X.is_symmetric(self.g[a]))
            else:
                self.assertTrue(X.is_antisymmetric(self.g[a]))

    def test_charge_matrix_and_chirality(self):
        self.assertTrue(X.equal(self.C, X.expected_charge_matrix()))
        self.assertTrue(X.equal(X.chirality(self.g), X.expected_chirality()))
        self.assertEqual(X.symmetric_signature(self.C), (8, 8, 0))
        for a in range(8):
            c_g = X.matmul(self.C, self.g[a])
            self.assertTrue(X.is_antisymmetric(c_g))

    def test_tau_structure(self):
        tau = X.notebook_tau()
        taubar = X.notebook_taubar(tau)
        for a in range(8):
            for b in range(8):
                # (tau[a] taubar[b] + tau[b] taubar[a]) / 2 = eta_ab I8
                symmetric = X.scale(Fraction(1, 2),
                                    X.add(X.matmul(tau[a], taubar[b]),
                                          X.matmul(tau[b], taubar[a])))
                self.assertTrue(X.equal(symmetric, X.scale(self.eta[a][b], X.identity(8))))
            self.assertTrue(X.is_signed_permutation(tau[a]))

    @unittest.skipUnless(os.path.exists(CL44_SEED), "dirac-main cl44 seed not present")
    def test_tensor_gammas_equal_dirac_main_seed(self):
        with open(CL44_SEED, "rb") as handle:
            seed = json.loads(handle.read().decode("utf-8"))
        tensor = X.tensor_gammas()
        for a in range(8):
            self.assertTrue(X.equal(X.fraction_matrix(seed["generators"][a]), tensor[a]))

    def test_zorn_octonion_identities_random(self):
        generator = random.Random(20260925)
        unit = X.octonion_basis(0)
        for _ in range(6):
            x = [random_rational(generator) for _ in range(8)]
            y = [random_rational(generator) for _ in range(8)]
            xy = X.octonion_product(x, y)
            self.assertEqual(X.octonion_norm(xy), X.octonion_norm(x) * X.octonion_norm(y))
            self.assertEqual(X.octonion_product(x, X.octonion_conjugate(x)),
                             [X.octonion_norm(x) * v for v in unit])
            self.assertEqual(X.octonion_product(X.octonion_product(x, x), y),
                             X.octonion_product(x, X.octonion_product(x, y)))
            self.assertEqual(X.octonion_product(X.octonion_product(x, y), x),
                             X.octonion_product(x, X.octonion_product(y, x)))
            self.assertEqual(X.from_zorn(X.to_zorn(x)), x)

    def test_octonion_gammas_clifford(self):
        gam = X.octonion_gammas()
        for a in range(8):
            for b in range(8):
                self.assertTrue(X.equal(X.anticommutator(gam[a], gam[b]),
                                        X.scale(2 * self.eta[a][b], self.I16)))

    def test_clifford_intertwiner_normalisation(self):
        tensor = X.tensor_gammas()
        dimension, k = X.primitive_intertwiner(tensor, self.g)
        self.assertEqual(dimension, 1)
        self.assertEqual(X.rank(k), 16)
        flat = [int(v) for v in X.flatten(k)]
        self.assertGreater(next(v for v in flat if v), 0)
        divisor = 0
        for value in flat:
            divisor = math.gcd(divisor, abs(value))
        self.assertEqual(divisor, 1)
        c_dm = X.matmul_many(tensor[0], tensor[1], tensor[2], tensor[3])
        self.assertTrue(X.equal(X.matmul_many(k, self.C, X.inverse(k)), c_dm))

    def test_flat_mode_hamiltonian_random_momenta(self):
        ctx = checker.Context()
        generator = random.Random(4488)
        for trial in range(4):
            mass = random_rational(generator)
            k = [random_rational(generator) for _ in range(8)]
            k[4] = Fraction(0)
            if trial % 2 == 0:
                k[5] = k[6] = k[7] = Fraction(0)
            h = checker.flat_mode_hamiltonian(ctx, mass, k)
            energy_squared = (mass ** 2 + sum(k[j] ** 2 for j in range(4))
                              - sum(k[j] ** 2 for j in range(5, 8)))
            self.assertTrue(X.cequal(X.cmatmul(h, h),
                                     X.cscale(energy_squared, 0, X.cidentity(16))))
            good = all(k[j] == 0 for j in range(5, 8))
            self.assertEqual(X.cis_hermitian(h), good)
            self.assertEqual(X.cis_zero(X.ccommutator(h, ctx.B)), good)


class VerifierTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.precomputed = checker.compute_algebra()

    def fresh(self):
        checks, measurements, ctx = self.precomputed
        return dict(checks), dict(measurements), ctx

    def test_all_algebra_checks_pass(self):
        checks, measurements, _ = self.fresh()
        self.assertEqual(list(checks), list(checker.ALGEBRA_CHECKS))
        failed = [name for name, value in checks.items() if not value]
        self.assertEqual(failed, [])
        self.assertEqual(measurements["ALG_fullAlgebraRank"], 256)
        self.assertEqual(measurements["ALG_cliffordKChiralityKinvSignVsGGGG"], 1)

    def test_commuting_with_b_measurements(self):
        _, measurements, _ = self.fresh()
        self.assertEqual(measurements["QNT_unitaryGeneratorCount"], 9)
        self.assertEqual(measurements["QNT_generatorsCommutingWithBCount"], 13)
        self.assertFalse(measurements["QNT_literalClaimExactlyNineCommuteWithB"])
        self.assertEqual(measurements["QNT_kreinGeneratorCount"], 21)

    def test_fixture_deterministic_lf(self):
        with tempfile.TemporaryDirectory() as directory:
            first = os.path.join(directory, "a", "algebra-fixture.json")
            second = os.path.join(directory, "b", "algebra-fixture.json")
            data_first = builder.write_fixture(first)
            data_second = builder.write_fixture(second)
            with open(first, "rb") as handle:
                self.assertEqual(handle.read(), data_first)
            self.assertEqual(data_first, data_second)
            self.assertNotIn(b"\r", data_first)
            self.assertTrue(data_first.endswith(b"}\n"))
            document = json.loads(data_first.decode("utf-8"))
            self.assertEqual(document["indexing"], "zero-based")
            self.assertEqual(len(document["gamma"]), 8)
            self.assertEqual(len(document["S"]), 28)

    def test_verify_with_temporary_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = os.path.join(directory, "algebra-fixture.json")
            builder.write_fixture(fixture)
            report = checker.verify(fixture, os.path.join(directory, "absent.json"),
                                    precomputed=self.fresh())
            self.assertTrue(report["checks"]["ALG_fixtureAgreement"])
            self.assertNotIn("ALG_wolframAgreement", report["checks"])
            self.assertEqual(report["measurements"]["wolframAgreement"], "not-run")
            self.assertEqual(len(report["checks"]), 20)
            self.assertTrue(all(report["checks"].values()))
            self.assertEqual(sorted(report["sourceSha256"]), sorted(checker.SOURCE_FILES))

    def test_tampered_fixture_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = os.path.join(directory, "algebra-fixture.json")
            builder.write_fixture(fixture)
            with open(fixture, "rb") as handle:
                document = json.loads(handle.read().decode("utf-8"))
            document["gamma"][3][0][0] = 1
            with open(fixture, "wb") as handle:
                handle.write(X.canonical_json_bytes(document))
            report = checker.verify(fixture, None, precomputed=self.fresh())
            self.assertFalse(report["checks"]["ALG_fixtureAgreement"])
            self.assertFalse(
                report["measurements"]["ALG_fixtureFieldAgreement"]["gamma"])

    def test_wolfram_agreement_comparison_logic(self):
        # Exercises the comparison code with a synthetic report; it does not
        # claim that Wolfram was run.
        _, measurements, _ = self.fresh()
        with tempfile.TemporaryDirectory() as directory:
            fixture = os.path.join(directory, "algebra-fixture.json")
            builder.write_fixture(fixture)
            synthetic = os.path.join(directory, "wolfram-algebra-report.json")
            payload = {"schemaVersion": 1, "checks": {"ALG_clifford": True},
                       "measurements": {"K_clifford": measurements["K_clifford"],
                                        "K_octonion": measurements["K_octonion"],
                                        "chirality": measurements["chirality"]}}
            with open(synthetic, "wb") as handle:
                handle.write(X.canonical_json_bytes(payload))
            report = checker.verify(fixture, synthetic, precomputed=self.fresh())
            self.assertTrue(report["checks"]["ALG_wolframAgreement"])
            payload["measurements"]["K_octonion"] = [[-v for v in row]
                                                    for row in measurements["K_octonion"]]
            with open(synthetic, "wb") as handle:
                handle.write(X.canonical_json_bytes(payload))
            report = checker.verify(fixture, synthetic, precomputed=self.fresh())
            self.assertFalse(report["checks"]["ALG_wolframAgreement"])
            # opposite intertwiner direction for K_octonion and a flat chirality diagonal
            k_octonion = X.matrix_from_json(measurements["K_octonion"])
            inverse = X.reshape(X.primitive_integer_vector(X.flatten(X.inverse(k_octonion))),
                                16, 16)
            payload["measurements"]["K_octonion"] = inverse
            payload["measurements"]["chirality"] = measurements["ALG_chiralityDiagonal"]
            with open(synthetic, "wb") as handle:
                handle.write(X.canonical_json_bytes(payload))
            report = checker.verify(fixture, synthetic, precomputed=self.fresh())
            self.assertTrue(report["checks"]["ALG_wolframAgreement"])
            self.assertEqual(report["measurements"]["wolframKOctonionDirection"],
                             "Gamma^a K = K gamma^a")

    def test_main_prints_protocol_and_writes_report(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = os.path.join(directory, "algebra-fixture.json")
            output = os.path.join(directory, "report.json")
            builder.write_fixture(fixture)
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = checker.main(["--fixture", fixture, "--output", output,
                                     "--wolfram-report", os.path.join(directory, "none.json")])
            lines = stream.getvalue().splitlines()
            self.assertEqual(code, 0)
            self.assertIn("check_count=20", lines)
            self.assertIn("failed_check_count=0", lines)
            self.assertIn("check_QNT_unitaryAndKreinSubgroups=true", lines)
            with open(output, "rb") as handle:
                data = handle.read()
            self.assertNotIn(b"\r", data)
            report = json.loads(data.decode("utf-8"))
            self.assertEqual(report["schemaVersion"], 1)
            self.assertEqual(report["producer"], checker.PRODUCER)

    def test_report_is_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = os.path.join(directory, "algebra-fixture.json")
            builder.write_fixture(fixture)
            first = X.canonical_json_bytes(checker.verify(fixture, None,
                                                          precomputed=self.fresh()))
            second = X.canonical_json_bytes(checker.verify(fixture, None,
                                                           precomputed=self.fresh()))
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
