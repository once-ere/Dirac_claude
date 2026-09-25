# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the Stage-1 provenance document (dirac16complex in an arbitrary gravitational field).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_arbitrary_field_publication.py" -v

The document provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md is built with
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md
into provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{tex,pdf}; the edition
dirac16complex-arbitrary-field is registered in provenance/pdf-specifications.json.

The tests pin the sha256 of the Markdown and of the LaTeX file, require that the
committed .tex is exactly the builder's output for the committed .md, that the
registered PDF edition matches the committed PDF, that the title, subtitle, the 14
sections of the outline and the required phrases are present, and that every check
name, number, matrix and hash the document quotes agrees with the five Stage-1
reports and stage1-summary.json in artifacts/dirac16complex/arbitrary-field/
(rewritten by steps 01 to 07 of scripts/verify_stage1_arbitrary_field.{ps1,sh}
before these tests run).

After an intended edit of the document: rebuild and register it with
    python scripts/build_provenance_pdf.py --register provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md
and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

PROVENANCE = REPOSITORY_ROOT / "provenance"
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_ARBITRARY_FIELD.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_ARBITRARY_FIELD.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_ARBITRARY_FIELD.pdf"
EDITION = "dirac16complex-arbitrary-field"
ARTIFACTS = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "arbitrary-field"
REPORT_FILES = {
    "wolfram-algebra": "wolfram-algebra-report.json",
    "wolfram-geometry": "wolfram-geometry-report.json",
    "python-algebra": "python-algebra-report.json",
    "python-geometry": "python-geometry-report.json",
    "grassmann-demo": "grassmann-demo-report.json",
}
SUMMARY = ARTIFACTS / "stage1-summary.json"
FIXTURE = ARTIFACTS / "algebra-fixture.json"

MARKDOWN_SHA256 = "1b86c6101f76f1a15e1371423a42b870cce19b1a347218e51ea47e0024179a82"
TEX_SHA256 = "4151f7f5b329f454cca2c677136b0aaf2d21d3d256318a6e348e763c63aa61a6"

TITLE = ("dirac16complex: a complex Grassmann spinor of Pin(4,4) in an arbitrary "
         "gravitational field")
SUBTITLE = ("Lagrangian, covariant field equations, energy-momentum tensor, canonical "
            "quantization and equations of state")
REQUIRED_PHRASES = (
    "dirac16complex",
    "Grassmann",
    "Pin(4,4)",
    "Spin(4,4)",
    "vielbein postulate",
    "canonical spin connection",
    "energy-momentum tensor",
    "equation of state",
    "Krein",
    "total covariant derivative of the vielbein",
    "Christoffel",
    "Euler-Lagrange",
    "Lichnerowicz",
    "Dirac sea",
    "Fock space",
    "ultrahyperbolic",
    "thawing",
    "(+,-,-,-)",
)
REQUIRED_SECTIONS = (
    "Abstract",
    "1. Scope, claims and non-claims",
    "2. Counting and notation dictionary",
    "3. The Clifford module in the split-octonion and Clifford pictures",
    "4. Definition of dirac16complex",
    "5. Canonical spin connection and covariant derivative",
    "6. Why the notebook Lagrangian Lg[] is empty for a Grassmann field",
    "7. The dirac16complex Lagrangian",
    "8. Euler-Lagrange equations in an arbitrary gravitational field",
    "9. Energy-momentum tensor operator, energies, pressure and equation of state",
    "10. Canonical quantization in 4+4 dimensions",
    "11. Verification records",
    "12. Reproduction",
    "13. Limitations",
)
# Expression [2] of the task: the notebook's Lg[] (cell 1064), verbatim.
EXPRESSION_2 = (
    r"Lg[]:=Sqrt[detgg] *( Transpose[\[CapitalPsi]16].\[Sigma]16.Sum[FullSimplify[((T16^\[Alpha])"
    r"[\[Alpha]1-1]/.sg),constraintVars].(D[ \[CapitalPsi]16,X[[\[Alpha]1]]]+(Q1/2)*Sum[\[Omega]mat"
    r"[[\[Alpha]1,a,b]]*SAB[[a,b]].\[CapitalPsi]16,{a,1,8},{b,1,8}]),{\[Alpha]1,1,Length[X]}]+(H*M)"
    r"*Transpose[\[CapitalPsi]16].\[Sigma]16.\[CapitalPsi]16)//Simplify[#,constraintVars]&")
# Names of the notebook that the WolframScript form of the new Lagrangian must use.
NEW_LAGRANGIAN_NAMES = (
    r"ConjugateTranspose[\[CapitalPsi]16].\[Sigma]16",
    r"(T16^\[Alpha])[\[Alpha]1 - 1]",
    r"\[Omega]low",
    r"\[Eta]4488[[a, c]] \[Omega]mat[[\[Alpha]1, c, b]]",
    r"SAB[[a, b]]",
    r"Sqrt[Abs[detgg]]",
    r"D[\[CapitalPsi]16, X[[\[Alpha]1]]]",
    "m = -H*M;",
)
CHECK_NAME = re.compile(r"\b(?:ALG|GEO|LAG|EMT|QNT|GR|NEG)_[A-Za-z0-9_]+")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def fenced_blocks(text: str) -> list[list[str]]:
    blocks, current, inside = [], [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            if inside:
                blocks.append(current)
                current = []
            inside = not inside
            continue
        if inside:
            current.append(line)
    assert not inside
    return blocks


def section(text: str, heading: str) -> str:
    start = text.index("\n" + heading + "\n")
    rest = text[start + len(heading) + 2:]
    match = re.search(r"\n#{2,3} ", rest)
    return rest[:match.start()] if match else rest


def matrix_rows(block: list[str]) -> list[list[int]]:
    rows = []
    for line in block:
        if line.startswith("["):
            rows.append([int(value) for value in line.strip("[] ").split()])
    return rows


class PinTests(unittest.TestCase):

    def test_markdown_sha256_pin(self):
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)

    def test_tex_sha256_pin(self):
        self.assertEqual(sha256_file(TEX), TEX_SHA256)

    def test_markdown_is_lf_only_utf8(self):
        content = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", content)
        content.decode("utf-8")
        self.assertTrue(content.endswith(b"\n"))

    def test_tex_is_the_builder_output_of_the_markdown(self):
        latex = builder.convert(markdown_text(), strip_heading_numbers=True)
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())

    def test_registered_edition_matches_the_committed_pdf(self):
        registry = check_provenance_pdf.load_specifications(
            check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf")
        content = PDF.read_bytes()
        self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(content)))
        self.assertTrue(content.startswith(b"%PDF-"))
        self.assertTrue(content.rstrip().endswith(b"%%EOF"))


class ContentTests(unittest.TestCase):

    def test_title_and_subtitle(self):
        lines = markdown_text().split("\n")
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertEqual(lines[2], "## " + SUBTITLE)
        self.assertEqual(sum(1 for line in lines if line.startswith("# ")), 1)

    def test_required_phrases(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_required_sections_in_order(self):
        headings = [line[3:] for line in markdown_text().split("\n") if line.startswith("## ")]
        self.assertEqual(headings[0], SUBTITLE)
        self.assertEqual(headings[1:], list(REQUIRED_SECTIONS))

    def test_no_placeholders_or_todo_and_no_other_provenance_documents(self):
        text = markdown_text()
        self.assertIsNone(re.search(r"@@[A-Z0-9_]+@@", text))
        self.assertNotIn("TODO", text)
        self.assertNotIn("FIXME", text)
        self.assertIsNone(re.search(r"provenance/[A-Za-z0-9_]+\.md", text.replace(
            "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md", "")))

    def test_every_fenced_code_line_fits(self):
        for block in fenced_blocks(markdown_text()):
            for line in block:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
                self.assertNotIn("\t", line)

    def test_expression_2_is_quoted_verbatim(self):
        joined = ["".join(block) for block in fenced_blocks(markdown_text())]
        self.assertIn(EXPRESSION_2, joined)

    def test_new_lagrangian_uses_the_notebook_names(self):
        text = markdown_text()
        block = [b for b in fenced_blocks(text) if any("Ldirac16complex[] :=" in line for line in b)]
        self.assertEqual(len(block), 1)
        code = "\n".join(block[0])
        for name in NEW_LAGRANGIAN_NAMES:
            with self.subTest(name=name):
                self.assertIn(name, code)

    def test_thawing_freezing_signs_are_formula_consistent(self):
        text = markdown_text()
        self.assertIn("$dw/da=-w_a$", text)
        self.assertIn("thawing has $w_a<0$ and freezing has $w_a>0$", text)

    def test_lichnerowicz_constant_and_curvature_sign_are_stated(self):
        text = markdown_text()
        self.assertIn(r"c=-\tfrac14", text)
        self.assertIn(r"=+\tfrac12R_{ab\mu\nu}S^{ab}", text)


class AgreementWithArtifactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.reports = {label: load_json(ARTIFACTS / name) for label, name in REPORT_FILES.items()}
        cls.summary = load_json(SUMMARY)
        cls.blocks = fenced_blocks(cls.text)

    def measurements(self, label: str) -> dict:
        return self.reports[label]["measurements"]

    def test_all_checks_true_and_every_check_is_listed(self):
        for label, report in self.reports.items():
            with self.subTest(report=label):
                self.assertEqual(report["schemaVersion"], 1)
                self.assertTrue(report["checks"])
                self.assertTrue(all(value is True for value in report["checks"].values()))
                listing = [block for block in self.blocks if block and block[0].startswith(label + ":")]
                self.assertEqual(len(listing), 1, label)
                names = " ".join(listing[0])[len(label) + 1:].split()
                self.assertEqual(names, list(report["checks"].keys()))

    def test_every_cited_name_exists_in_a_report(self):
        checks = set()
        measurements = set()
        for report in self.reports.values():
            checks.update(report["checks"])
            measurements.update(report["measurements"])
        for name in sorted(set(CHECK_NAME.findall(self.text))):
            with self.subTest(name=name):
                self.assertTrue(name in checks or any(key.startswith(name) for key in measurements),
                                name)

    def test_counts_quoted_match_the_summary(self):
        counts = self.summary["counts"]
        total = counts["total"]
        self.assertEqual(total["passed"], total["checks"])
        self.assertEqual(total["failed"], 0)
        self.assertIn("pass %d of %d checks in five reports" % (total["passed"], total["checks"]),
                      self.text)
        for label, name in REPORT_FILES.items():
            n = counts[label]["checks"]
            self.assertEqual(counts[label]["passed"], n)
            self.assertEqual(n, len(self.reports[label]["checks"]))
            self.assertRegex(self.text, r"\n%s +scripts/\S+ +%d of %d\n" % (re.escape(name), n, n))
        self.assertEqual(self.summary["disagreements"], [])
        self.assertEqual(self.summary["failedChecks"], [])
        self.assertIn("%d agreed key measurements" % len(self.summary["agreedMeasurements"]),
                      self.text)

    def test_cross_implementation_agreement_quoted(self):
        pa = self.measurements("python-algebra")
        pg = self.measurements("python-geometry")
        wa = self.measurements("wolfram-algebra")
        self.assertEqual(pa["wolframSharedMeasurementCount"], pa["wolframSharedMeasurementsAgreeing"])
        self.assertEqual(pg["GEO_wolframSharedMeasurementCount"],
                         pg["GEO_wolframSharedMeasurementsAgreeing"])
        self.assertEqual(pa["wolframCheckVerdictDisagreements"], [])
        self.assertEqual(pg["GEO_wolframCheckVerdictDisagreements"], [])
        self.assertIn("cross-comparison of %d algebra and %d geometry measurements" % (
            pa["wolframSharedMeasurementCount"], pg["GEO_wolframSharedMeasurementCount"]), self.text)
        self.assertIn("%d shared check names" % len(pa["wolframCheckNamesShared"]), self.text)
        self.assertIn("%d shared check names" % len(pg["GEO_wolframCheckNamesShared"]), self.text)
        fixture = wa["fixtureAgreement.summary"]
        self.assertTrue(fixture["agree"])
        self.assertEqual(fixture["disagreeByName"], 0)
        self.assertIn("%d of %d matrices agree by name" % (fixture["matricesFound"],
                                                          fixture["agreeByName"]), self.text)

    def test_expression_1_block_is_the_verified_literal_input(self):
        wa = self.measurements("wolfram-algebra")
        self.assertEqual(wa["ALG_expression1.list"], [True] * 8)
        self.assertIn([wa["ALG_expression1.literalInput"]], self.blocks)
        self.assertIn("from the %d verbatim notebook definition cells"
                      % wa["ALG_expression1.notebookCellsEvaluated"], self.text)

    def test_intertwiner_matrices_are_the_report_matrices(self):
        wa = self.measurements("wolfram-algebra")
        pa = self.measurements("python-algebra")
        k_block = [b for b in self.blocks if b and b[0] == "K_clifford ="]
        q_block = [b for b in self.blocks if b and b[0] == "Q ="]
        self.assertEqual(len(k_block), 1)
        self.assertEqual(len(q_block), 1)
        self.assertEqual(matrix_rows(k_block[0]), wa["K_clifford"])
        self.assertEqual(matrix_rows(k_block[0]), pa["K_clifford"])
        q = matrix_rows(q_block[0])
        self.assertEqual(q, wa["ALG_octonionPictureIntertwiner.notebookBasisChange"]["Q"])
        k_octonion = wa["K_octonion"]
        for i in range(8):
            for j in range(8):
                self.assertEqual(k_octonion[i][j], q[i][j])
                self.assertEqual(k_octonion[i + 8][j + 8], q[i][j])
                self.assertEqual(k_octonion[i][j + 8], 0)
                self.assertEqual(k_octonion[i + 8][j], 0)
        self.assertEqual(pa["K_octonion"], k_octonion)
        self.assertEqual(pa["ALG_cliffordIntertwinerDimension"], 1)
        self.assertEqual(pa["ALG_cliffordIntertwinerRank"], 16)
        self.assertEqual(pa["ALG_octonionIntertwinerDimension"], 1)
        self.assertEqual(pa["ALG_octonionIntertwinerRank"], 16)
        self.assertTrue(pa["ALG_cliffordKChargeKinvEqualsCdm"])
        self.assertEqual(wa["ALG_cliffordPictureIntertwiner.imageOfNotebookMinusAndPlusBlocks"],
                         [[1, 2, 4, 7, 8, 11, 13, 14], [0, 3, 5, 6, 9, 10, 12, 15]])
        self.assertIn("{1, 2, 4, 7, 8, 11, 13, 14}", self.text)
        self.assertIn("{0, 3, 5, 6, 9, 10, 12, 15}", self.text)

    def test_representation_theory_numbers(self):
        wa = self.measurements("wolfram-algebra")
        pa = self.measurements("python-algebra")
        self.assertEqual((wa["ALG_faithful.fullRank"], wa["ALG_faithful.evenRank"]), (256, 128))
        self.assertEqual(pa["ALG_pinCommutantDimensionQ"], 1)
        self.assertEqual(wa["ALG_pinIrreducibleComplex.commutantDimension"], 1)
        self.assertEqual(wa["ALG_spinDecomposition.spinCommutantDimension"], 2)
        self.assertEqual(wa["ALG_spinDecomposition.blockCommutantDimensions"], [1, 1])
        self.assertEqual(wa["ALG_spinDecomposition.blockEvenAlgebraRanks"], [64, 64])
        self.assertEqual(wa["ALG_spinDecomposition.crossIntertwinerDimensions"], [0, 0])
        self.assertEqual(pa["ALG_chargeMatrixSignature"], [8, 8, 0])
        self.assertEqual(pa["ALG_chargeFormBEigenvalueMultiplicities"], {"plus1": 8, "minus1": 8})
        self.assertEqual(wa["ALG_invariantForms.invariantBilinearFormDimension"], 2)
        for phrase in ("the block commutants have dimensions (1, 1)",
                       "the even-algebra ranks on the blocks are (64, 64)",
                       "the cross-intertwiner dimensions are (0, 0)",
                       "linearly independent (rank 256), and the 128 even ones have rank 128",
                       "The commutant of the 28 spin generators $S^{ab}$ has dimension 2",
                       "form a 2-dimensional space spanned by $CP_-$ and $CP_+$"):
            self.assertIn(phrase, self.text)

    def test_subgroup_counts(self):
        wa = self.measurements("wolfram-algebra")
        pa = self.measurements("python-algebra")
        self.assertEqual(wa["QNT_unitaryAndKreinSubgroups.countCommutingWithB"], 13)
        self.assertEqual(pa["QNT_unitaryGeneratorCount"], 9)
        self.assertEqual(pa["QNT_kreinGeneratorCount"], 21)
        self.assertEqual(pa["QNT_antiHermitianGeneratorCount"], 12)
        self.assertEqual(len(pa["QNT_kreinFailingGenerators"]), 7)
        self.assertFalse(pa["QNT_literalClaimExactlyNineCommuteWithB"])
        for phrase in ("Exactly 13 of the 28 generators", "Exactly 9 generators",
                       "Exactly 21 generators", "fails for all 7 generators",
                       "Exactly 12 generators"):
            self.assertIn(phrase, self.text)

    def test_quantization_numbers(self):
        wa = self.measurements("wolfram-algebra")
        pa = self.measurements("python-algebra")
        rest = wa["QNT_kreinSignature.restPositiveFrequency"]
        self.assertEqual((rest["dimension"], rest["signature"]), (8, [4, 4]))
        self.assertEqual(pa["QNT_kreinBSignatureOnPlusEigenspace"], [4, 4])
        samples = pa["QNT_flatModeSamples"]
        negative = [s["energySquared"] for s in samples if str(s["energySquared"]).startswith("-")]
        self.assertEqual(len(samples), pa["QNT_flatModeSampleCount"])
        self.assertEqual(len(negative), pa["QNT_flatModeNegativeEnergySquaredSamples"])
        self.assertIn("plus %d exact samples (Python); %d of the samples" % (
            len(samples), len(negative)), self.text)
        self.assertIn("$E^2=%s$ and $E^2=%s$" % tuple(negative), self.text)
        self.assertEqual(wa["QNT_flatModeHamiltonian.hSquared"],
                         "(m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 - k7^2) I16")
        self.assertTrue(wa["QNT_currentHermiticity.J4MatrixEqualsB"])

    def test_geometry_numbers(self):
        wg = self.measurements("wolfram-geometry")
        pg = self.measurements("python-geometry")
        points = ("p1", "p2", "p3")
        for geometry in ("G1", "G2"):
            for point in points:
                self.assertEqual(wg["%s.%s.lichnerowiczC" % (geometry, point)], "-1/4")
                self.assertEqual(wg["%s.%s.curvatureCandidate.plusHalfLowered" % (geometry, point)],
                                 "true")
        self.assertEqual(pg["GEO_lichnerowicz_c_G2"], "-1/4")
        self.assertEqual([wg["G2.%s.scalarCurvature" % p] for p in points],
                         ["-2672/147", "-1102/675", "-834/49"])
        self.assertIn("$-2672/147$, $-1102/675$ and $-834/49$", self.text)
        self.assertEqual({wg["G1.%s.nonzeroOmegaLower" % p] for p in points}, {448})
        self.assertEqual(wg["G2.p1.nonzeroOmegaLower"], 24)
        self.assertEqual(pg["GEO_notebookContraction_nonzeroPairs_DmuGammaNu_G2"], 15)
        self.assertEqual(pg["GEO_notebookContraction_nonzeroEntries_DmuGammaNu_G2"], 288)
        self.assertEqual([wg["G2.%s.notebookDGammaMaxAbs" % p] for p in points], ["2/3", "1/5", "9/5"])
        self.assertIn("is 448 at each G1 point and 24 in G2", self.text)
        self.assertIn("in 15 pairs with 288 nonzero entries in G2", self.text)
        self.assertIn("$2/3$, $1/5$ and $9/5$ at the three G2 points", self.text)
        self.assertEqual(pg["GEO_ricciScalar_G2"], "6*H**2*(A1**2 - 7)")
        self.assertEqual(pg["GEO_slashOmega_canonical_G2"], "gamma^mu Omega_mu = (3*H) gamma^0")
        self.assertEqual(wg["emt.trace"], "on-shell T^mu_mu = -m S + 7 S U'(S) - 8 U(S) = -m S + 3 lambda S^2")
        self.assertIn(r"T^\mu{}_\mu=-mS+7SU'(S)-8U(S)=-mS+3\lambda S^2", self.text)
        self.assertEqual({pg["EMT_homogeneous_offDiagonalNonzeroCounts_G3_%s" % q]["T_ij"]
                          for q in ("q1", "q2", "q3")}, {42})

    def test_grassmann_numbers(self):
        gr = self.measurements("grassmann-demo")
        powers = gr["GR_quarticTermPolynomial_nonzeroMonomials_k1_to_k17"]
        self.assertEqual(powers[-1], 0)
        self.assertIn(", ".join(str(p) for p in powers[:-2]) + " and %d" % powers[-2], self.text)
        self.assertEqual(gr["GR_massTermVanishesReal_PsiT_C_Psi_nonzeroMonomials"], 0)
        self.assertEqual(gr["GR_notebookLgEL_canonicalOmega_nonzeroComponents_G1_p1"], 0)
        self.assertEqual(gr["GR_notebookLgEL_canonicalOmega_nonzeroComponents_G2"], 0)
        self.assertEqual(gr["GR_notebookLgEL_notebookContraction_nonzeroComponents_G1_p1"], 16)
        self.assertEqual(gr["GR_generatorCounts"], {"realPsi16JetSpace": 720, "complexPsiJetSpace": 1440})

    def test_homogeneous_sample_quoted_matches_the_python_report(self):
        sample = self.measurements("python-geometry")["EMT_homogeneous_G3_q1"]
        quoted = ("at $x_4=%s$ with $m=%s$, $\\lambda=%s$ and $S=%s$ the Python report gives "
                  "$\\rho=%s$, $\\mathrm{KE}_L=%s$, $\\mathrm{PE}_L=%s$ and $w=%s$") % (
            sample["x4"], sample["m"], sample["lambda"], sample["S"], sample["rho"],
            sample["KE"], sample["PE"], sample["w"])
        self.assertIn(quoted, self.text)

    def test_recorded_hashes_match_the_files_and_the_reports(self):
        block = section(self.text, "### 11.7 Files and hashes")
        lines = [b for b in fenced_blocks(block)][0]
        self.assertEqual(len(lines) % 2, 0)
        pairs = {lines[i]: lines[i + 1].strip() for i in range(0, len(lines), 2)}
        recorded = {}
        for report in self.reports.values():
            recorded.update(report["sourceSha256"])
            recorded.update(report.get("inputSha256", {}))
        for name in list(REPORT_FILES.values()) + ["stage1-summary.json", "algebra-fixture.json"]:
            path = "artifacts/dirac16complex/arbitrary-field/" + name
            with self.subTest(path=path):
                self.assertEqual(pairs[path], sha256_file(ARTIFACTS / name))
        for label, entry in self.summary["reports"].items():
            self.assertEqual(pairs[entry["path"]], entry["sha256"])
        for path, digest in pairs.items():
            if path.startswith("artifacts/dirac16complex/arbitrary-field/") and path not in recorded:
                continue
            with self.subTest(path=path):
                self.assertEqual(digest, recorded[path])
                if not path.startswith("dirac-main/") or (REPOSITORY_ROOT / path).exists():
                    self.assertEqual(digest, sha256_file(REPOSITORY_ROOT / path))


if __name__ == "__main__":
    unittest.main()
