# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the Stage-2 provenance document (dirac16complex in the primordial field).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_primordial_publication.py" -v

The document provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md is built with
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md
into provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.{tex,pdf}; the edition
dirac16complex-primordial-field is registered in provenance/pdf-specifications.json.

The tests pin the sha256 of the Markdown and of the LaTeX file, require that the
committed .tex is exactly the builder's output for the committed .md, that the
registered PDF edition matches the committed PDF, that the required phrases,
title, subtitle and sections are present, and that the numbers and TeX strings
the document quotes agree with the Stage-2 reports and the Wolfram component file
(artifacts/dirac16complex/primordial-field/*.json, rewritten by steps 01 and 02 of
scripts/verify_stage2_primordial_field.{ps1,sh} before these tests run).

After an intended edit of the document: rebuild and register it with
    python scripts/build_provenance_pdf.py --register provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md
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
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_PRIMORDIAL_FIELD.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_PRIMORDIAL_FIELD.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf"
EDITION = "dirac16complex-primordial-field"
ARTIFACTS = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "primordial-field"
COMPONENTS = ARTIFACTS / "primordial-components.json"
WOLFRAM_REPORT = ARTIFACTS / "wolfram-primordial-report.json"
PYTHON_REPORT = ARTIFACTS / "python-primordial-report.json"

MARKDOWN_SHA256 = "287886ab6eb8892993773b10978c912fe537a0e003daaa36064d1d226ea45b9e"
TEX_SHA256 = "4b7a0906f2a7e86a7ed29bf466f662d49d3bd6d7cd8991735e02199662b306d0"

TITLE = "dirac16complex in the primordial pair-creation gravitational field"
SUBTITLE = ("Explicit components of the connection, field equations, energy-momentum "
            "tensor, quantization and equations of state")
REQUIRED_PHRASES = (
    "primordial",
    "pair-creation",
    "vielbein postulate",
    "canonical spin connection",
    "energy-momentum tensor",
    "equation of state",
    "cell 1058",
    "Krein",
)
REQUIRED_SECTIONS = (
    "Abstract",
    "1. Scope and non-claims",
    "2. Notation and conventions",
    "3. Why this field is a reasonable primordial field",
    "4. The metric and the vielbein",
    "5. Christoffel symbols",
    "6. Canonical spin connection and the vielbein postulate",
    "7. The spinor connection",
    "8. Contraction with the gammas and covariant constancy",
    "9. The Lagrangian in this field",
    "10. The sixteen component Euler-Lagrange equations",
    "11. Comparison with the notebook's cell-1137 equations",
    "12. The energy-momentum tensor",
    "13. Homogeneous sector and equations of state",
    "14. Modes",
    "15. Einstein tensor and the required source",
    "16. The gamma-8 map: a structural plus-minus M pairing",
    "17. Canonical quantization in this field",
    "18. Verification records",
    "19. Reproduction",
    "20. Limitations",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def tagged_displays(text: str) -> dict[str, str]:
    """Map each \\tag{...} of an aligned display to its math, line breaks removed.

    The lines of an aligned block start with '&' and continuation lines with
    '\\quad '; both, and the '\\\\' line ends, are removed so that the result can
    be compared with the concatenated JSON lines.
    """
    displays = {}
    pattern = re.compile(
        r"\$\$\n\\begin\{aligned\}\n((?:(?!\\end\{aligned\}).)*?)\n"
        r"\\end\{aligned\}\\tag\{([^}]*)\}\n\$\$", re.S)
    for match in pattern.finditer(text):
        lines = match.group(1).split("\n")
        pieces = []
        for line in lines:
            assert line.startswith("&"), line
            line = line[1:]
            if line.endswith(" \\\\"):
                line = line[:-3]
            if line.startswith("\\quad "):
                line = line[len("\\quad "):]
            pieces.append(line)
        displays[match.group(2)] = pieces
    return displays


def joined(lines: list[str]) -> str:
    out = lines[0]
    for line in lines[1:]:
        if line.startswith("\\quad "):
            line = line[len("\\quad "):]
        out += line
    return out


class PinTests(unittest.TestCase):

    def test_markdown_sha256_pin(self):
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)

    def test_tex_sha256_pin(self):
        self.assertEqual(sha256_file(TEX), TEX_SHA256)

    def test_markdown_is_lf_only_utf8(self):
        content = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", content)
        content.decode("utf-8")

    def test_tex_is_the_builder_output_of_the_markdown(self):
        latex = builder.convert(markdown_text(), strip_heading_numbers=True)
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())

    def test_registered_edition_matches_the_committed_pdf(self):
        registry = check_provenance_pdf.load_specifications(
            check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf")
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
            "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md", "")))

    def test_every_fenced_code_line_fits(self):
        inside = False
        for line in markdown_text().split("\n"):
            if line.startswith("```"):
                inside = not inside
                continue
            if inside:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
        self.assertFalse(inside)


class AgreementWithArtifactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.components = load_json(COMPONENTS)
        cls.wolfram = load_json(WOLFRAM_REPORT)
        cls.python = load_json(PYTHON_REPORT)
        cls.displays = tagged_displays(cls.text)

    def test_check_counts_quoted_match_the_reports(self):
        wolfram_checks = self.wolfram["checks"]
        python_checks = self.python["checks"]
        self.assertTrue(all(value is True for value in wolfram_checks.values()))
        self.assertTrue(all(value is True for value in python_checks.values()))
        self.assertIn("WolframScript (%d of %d checks true)" % (len(wolfram_checks),
                                                              len(wolfram_checks)), self.text)
        self.assertIn("Python/sympy (%d of %d checks true" % (len(python_checks),
                                                             len(python_checks)), self.text)
        self.assertIn("All %d checks are true:" % len(wolfram_checks), self.text)
        self.assertIn("All %d checks are true:" % len(python_checks), self.text)
        for name in python_checks:
            self.assertIn(name, self.text)
        for name in wolfram_checks:
            group = name.split("_")[1]
            self.assertIn(name[len("P_" + group + "_"):], self.text)

    def test_wolfram_agreement_quoted_matches_the_python_report(self):
        measurements = self.python["measurements"]
        self.assertEqual(measurements["wolframAgreement"], "compared")
        agreement = measurements["P_EL_wolfram"]
        self.assertEqual(agreement["wolframMismatchCount"], 0)
        self.assertEqual(agreement["wolframCoefficientsCompared"],
                         {"terms/py": 320, "terms/wl": 320,
                          "evolution/py": 288, "evolution/wl": 288})
        self.assertIn("That is 320 coefficients for the equations", self.text)
        self.assertIn("and 288 for the evolution form", self.text)

    def test_geometry_counts_quoted_match_the_components(self):
        self.assertEqual(self.components["christoffel"]["nonzeroCount"], 37)
        self.assertEqual(self.components["christoffel"]["nonzeroCountMuLeNu"], 25)
        self.assertEqual(self.components["spinConnection"]["nonzeroCount"], 24)
        self.assertEqual(len(self.components["EMT"]["anticommutators"]), 21)
        self.assertEqual(self.wolfram["measurements"]["notebookContraction_DmuGammaNu_nonzeroPairs"], 15)
        self.assertEqual(self.wolfram["measurements"]["notebookContraction_DmuGammaNu_nonzeroEntries"], 288)
        for phrase in ("exactly 37 of the 512 symbols", "Exactly 24 components",
                       "Exactly 21 of the 36 matrices", "violates $D_\\mu\\gamma^\\nu=0$ in 15 of the 64 pairs",
                       "with 288 nonzero matrix entries"):
            self.assertIn(phrase, self.text)

    def test_christoffel_spin_connection_and_connection_terms_are_the_component_tex(self):
        for entry in self.components["christoffel"]["entries"]:
            self.assertIn("| $%s$ | $%s$ |" % (entry["label"], entry["tex"]), self.text)
        for entry in self.components["spinConnection"]["lowered"]:
            self.assertIn("| $%s$ | $%s$ |" % (entry["label"], entry["tex"]), self.text)
        for record in self.components["EMT"]["anticommutators"]:
            product = record["clifford"][0]
            self.assertIn("| $(%d,%d)$ | $%s$ | $%s$ |" % (
                record["mu"], record["nu"], product["tex"], product["coefficient"]["tex"]),
                self.text)

    def test_sixteen_component_equations_are_the_component_tex(self):
        equations = self.components["eulerLagrange"]["equations"]
        self.assertEqual([equation["n"] for equation in equations], list(range(16)))
        for equation in equations:
            n = equation["n"]
            with self.subTest(row=n):
                self.assertEqual("".join(self.displays["E%d" % n]), joined(equation["texLines"]))
                self.assertEqual("".join(self.displays["V%d" % n]),
                                 joined(equation["evolution"]["texLines"]))
                self.assertEqual(len(equation["terms"]), 10)
        row0 = equations[0]
        self.assertEqual("".join(self.displays["E0: x form"]), joined(row0["texLinesX0"]))
        self.assertEqual("".join(self.displays["E0: zeta form"]), joined(row0["texLinesZeta"]))
        self.assertEqual("".join(self.displays["E0: z, t form"]), joined(row0["texLinesZT"]))

    def test_block_and_notebook_equations_are_the_component_tex(self):
        for block in self.components["blocksX0X4"]["blocks"]:
            tag = "block " + ",".join(str(k) for k in block["components"])
            expected = [joined(eq["texLines"]) for eq in block["equationsZT"]]
            self.assertEqual(self.displays[tag], expected)
        stored = {eq["yZ"]: eq for eq in self.components["notebookComparison"]["equations"]}
        for number in range(4):
            expected = [joined(stored[y]["notebookStoredTeX"]) for y in range(4 * number, 4 * number + 4)]
            self.assertEqual(self.displays["stored, block %d" % (number + 1)], expected)

    def test_q_term_signs_quoted_match_the_wolfram_report(self):
        signs = self.wolfram["measurements"]["qTermSignsByYZ"]
        pairs = [(int(y), int(sign)) for y, sign in re.findall(r"\{(-?\d+), (-?\d+)\}", signs)]
        self.assertEqual(len(pairs), 16)
        for y, sign in pairs:
            psi = self.components["notebookComparison"]["crossReference"]
            psi_index = [row["Psi"] for row in psi if row["yZ"] == y][0]
            cell = {1: "$+q\\,yZ_{%d}$" % y, -1: "$-q\\,yZ_{%d}$" % y, 0: "none"}[sign]
            self.assertIn("| $yZ_{%d}$ | $\\Psi_{%d}$ |" % (y, psi_index), self.text)
            row = [line for line in self.text.split("\n")
                   if line.startswith("| $yZ_{%d}$ |" % y)][0]
            self.assertTrue(row.endswith("| %s |" % cell), row)

    def test_einstein_and_source_quoted_match_the_components(self):
        einstein = self.components["einstein"]
        for entry in einstein["GmixedDiagonal"]:
            self.assertIn(entry["texContract"], self.text)
        self.assertIn("R&=6H^2(a_4'^2-7)", self.text)
        self.assertIn("\\rho_{\\mathrm{req}}=-3H^2(7+a_4'^2)/\\kappa", self.text)
        self.assertEqual(self.wolfram["measurements"]["condensateWronskian_1_invS_invS2"],
                         "-2*Cot[z]^3*Csc[z]^3")
        self.assertIn("=-2\\cot^3z\\,\\csc^3z\\ne0", self.text)
        values = self.components["a4linear"]["values"]
        self.assertEqual(values["rhoReq"], "-24H^2/\\kappa")
        self.assertIn("\\rho_{\\mathrm{req}}=-24H^2/\\kappa", self.text)

    def test_exact_examples_quoted_match_the_python_report(self):
        examples = self.python["measurements"]["P_EMT"]["samplePoints"]["P1"]["examples_lam0"]
        example = examples["u_b = e0 + i e1 + e4 + i e12"]
        self.assertEqual((example["S"], example["rho"], example["p_0"]), ("-10/3", "-155/21", "-5"))
        self.assertIn("$S=-10/3$, $\\rho=-155/21$ and $p_{(0)}=-5$", self.text)
        for label in ("P1", "P2"):
            for key, name in (("u_a = e0 + e4", "u_a"), ("u_b = e0 + i e1 + e4 + i e12", "u_b")):
                data = self.python["measurements"]["P_EMT"]["samplePoints"][label]["examples_lam0"][key]
                row = "\\text{%s},\\ %s & %s & %s & %s & %s & %s & %s & %s & %s" % (
                    label, name, data["S"], data["rho"], data["p_0"], data["KE_L"],
                    data["KE_H"], data["PE_H"], data["d4_p0"], data["w"])
                self.assertIn(row, self.text)

    def test_recorded_hashes_match_the_reports(self):
        sources = self.wolfram["sourceSha256"]
        inputs = self.python["inputSha256"]
        checker = self.python["sourceSha256"]
        expected = {
            "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb":
                sources["Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"],
            "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json":
                sources["artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"],
            "wolfram/Dirac16ComplexPrimordial.wl": sources["wolfram/Dirac16ComplexPrimordial.wl"],
            "scripts/verify_dirac16complex_primordial.wls":
                sources["scripts/verify_dirac16complex_primordial.wls"],
            "scripts/check_dirac16complex_primordial.py":
                checker["scripts/check_dirac16complex_primordial.py"],
            "artifacts/dirac16complex/primordial-field/primordial-components.json":
                inputs["artifacts/dirac16complex/primordial-field/primordial-components.json"],
        }
        for path, digest in expected.items():
            with self.subTest(path=path):
                self.assertIn(path + "\n  " + digest + "\n", self.text)
        self.assertEqual(
            inputs["artifacts/dirac16complex/primordial-field/primordial-components.json"],
            sha256_file(COMPONENTS))


if __name__ == "__main__":
    unittest.main()
