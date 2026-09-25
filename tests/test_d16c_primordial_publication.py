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
import zlib
from pathlib import Path

import sympy as sp

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

MARKDOWN_SHA256 = "550d9052e90e1ecedf05eaa2f64685a46d46938a319a0f0d1eb8cd03f620c645"
TEX_SHA256 = "c1cd3773ef2f15c43002449745171afeb48e14e8d35a3c5d0d100c4906ab607e"

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
        sets = self.components["notebookComparison"].get("crossReference")
        blocks = ((0, 5, 8, 13), (1, 4, 9, 12), (2, 7, 10, 15), (3, 6, 11, 14))
        self.assertEqual([row["Psi"] for row in sorted(sets, key=lambda r: r["yZ"])],
                         [k for block in blocks for k in block])
        for number, block in enumerate(blocks):
            expected = [joined(stored[y]["notebookStoredTeX"]) for y in range(4 * number, 4 * number + 4)]
            tag = "stored, block " + ",".join(str(k) for k in block)
            self.assertEqual(self.displays[tag], expected)
        # blocks are named by their component sets, never numbered from 1 (CONTRACT section 0)
        self.assertIsNone(re.search(r"\| [1-4]: \$", self.text))

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

    def test_omega_array_is_generated_from_the_component_file(self):
        symbols = {name: sp.Symbol(name) for name in ("H", "z", "a4", "a4p")}
        begin = self.text.index("\\begin{array}{c|cccccc}")
        end = self.text.index("\\end{array}", begin)
        lines = self.text[begin:end].split("\n")[2:]
        rows = [line.rstrip().removesuffix(" \\\\").split(" & ") for line in lines if " & " in line]
        self.assertEqual(len(rows), 16)
        matrices = {m["mu"]: m for m in self.components["Omega"]["matrices"]}
        for column, mu in enumerate((1, 2, 3, 5, 6, 7), start=1):
            sign = 1 if mu < 4 else -1
            alpha = symbols["H"] * sp.sin(symbols["z"]) ** sp.Rational(1, 6) * sp.exp(sign * symbols["a4"])
            for n in range(16):
                entries = [e for e in matrices[mu]["entries"] if e["row"] == n]
                terms = []
                for entry in entries:
                    ratio = sp.simplify(sp.sympify(entry["py"], locals=symbols) / (alpha / 2))
                    if ratio in (1, -1):
                        terms.insert(0, ("-" if ratio == -1 else "+") + "\\Psi_{%d}" % entry["col"])
                    else:
                        self.assertIn(sp.simplify(ratio / symbols["a4p"]), (1, -1))
                        terms.append(("-" if sp.simplify(ratio / symbols["a4p"]) == -1 else "+")
                                     + "a_4'\\Psi_{%d}" % entry["col"])
                cell = "".join(terms).removeprefix("+")
                with self.subTest(n=n, mu=mu):
                    self.assertEqual(rows[n][0], str(n))
                    self.assertEqual(rows[n][column], cell)

    def test_notebook_contraction_table_matches_both_reports(self):
        violations = self.python["measurements"]["P_gammaConst"]["notebookContractionViolations"]
        expected = []
        for i in (1, 2, 3):
            expected.append("D_%d gamma^%d = (H*Derivative(a4(t), t))*g4" % (i, i))
            expected.append("D_%d gamma^4 = (H*exp(a4(t))*sin(z)**(1/6)*Derivative(a4(t), t))*g%d" % (i, i))
        for j in (5, 6, 7):
            expected.append("D_%d gamma^0 = (H*exp(-a4(t))*sin(z)**(7/6)/cos(z))*g%d" % (j, j))
            expected.append("D_%d gamma^4 = (2*H*exp(-a4(t))*sin(z)**(1/6)*Derivative(a4(t), t))*g%d"
                            % (j, j))
            expected.append("D_%d gamma^%d = (H)*g0 + (-2*H*Derivative(a4(t), t))*g4" % (j, j))
        self.assertEqual(sorted(violations), sorted(expected))
        self.assertTrue(self.wolfram["checks"]["P_gammaConst_notebookContractionClosedForms"])
        for row in ("| $(i,i)$, $i=1,2,3$ | $H\\,a_4'\\,\\gamma^4$ |",
                    "| $(i,4)$, $i=1,2,3$ | $H\\,s^{1/6}e^{a_4}a_4'\\,\\gamma^i$ |",
                    "| $(j,0)$, $j=5,6,7$ | $H\\,s^{7/6}e^{-a_4}\\sec z\\,\\gamma^j$ |",
                    "| $(j,4)$, $j=5,6,7$ | $2H\\,s^{1/6}e^{-a_4}a_4'\\,\\gamma^j$ |",
                    "| $(j,j)$, $j=5,6,7$ | $H\\gamma^0-2H\\,a_4'\\,\\gamma^4$ |"):
            self.assertIn(row, self.text)

    def test_energy_condition_table_is_the_component_tex(self):
        conditions = self.components["einstein"]["energyConditions"]
        for key, lhs in (("WEC_rho", "\\rho"), ("NEC_e4_plus_e0", "\\rho+p_{(0)}"),
                         ("NEC_e4_plus_ei_(i=1,2,3)", "\\rho+p_{(i)}"),
                         ("NEC_ej_plus_e0_(j=5,6,7)", "p_{(0)}-p_{(j)}"),
                         ("NEC_ej_plus_ei", "p_{(i)}-p_{(j)}"),
                         ("SEC_timelikeConvergence_R44", "R_{44}")):
            self.assertIn("| $%s=%s$ |" % (lhs, conditions[key]["expr"]), self.text)

    def test_source_analysis_quoted_matches_both_reports(self):
        source = self.components["source"]["x0Independent"]
        groups = {}
        for entry in source["offDiagonal"]:
            mu, nu = entry["mu"], entry["nu"]
            if mu == 0:
                key, index, name = ("(0,i)" if nu < 4 else "(0,j)"), nu, ("i" if nu < 4 else "j")
            elif nu == 4:
                key, index, name = "(i,4)", mu, "i"
            elif mu == 4:
                key, index, name = "(4,j)", nu, "j"
            else:
                key, index, name = "(i,j)", None, None
            tex = entry["tex"]
            if index is not None:
                tex = tex.replace("\\gamma^{%d}" % index, "\\gamma^{%s}" % name)
            else:
                tex = tex.replace("\\gamma^{%d}" % mu, "\\gamma^{i}").replace("\\gamma^{%d}" % nu,
                                                                             "\\gamma^{j}")
            row = "| $%s$ | $\\bar\\Psi%s\\Psi$ | $%s$ |" % (key, tex, entry["coefficient"]["tex"])
            groups.setdefault(key, set()).add(row)
        self.assertEqual(sorted(groups), ["(0,i)", "(0,j)", "(4,j)", "(i,4)", "(i,j)"])
        self.assertEqual(sum(1 for _ in source["offDiagonal"]), 21)
        for key, rows in groups.items():
            self.assertEqual(len(rows), 1, key)
            self.assertIn(rows.pop(), self.text)
        wolfram = {e["label"]: e for e in source["examples"]}
        python = self.python["measurements"]["P_source"]["x0IndependentExamples"]
        for label in ("A", "B"):
            w, p = wolfram[label], python[label]
            self.assertEqual((str(w["S"]), str(w["rho"]), str(w["pTransverse"])),
                             (p["S"], p["rho"], p["pTransverse"]))
            self.assertEqual(w["u0NormFactorSquared"], p["u0NormFactorSquared"])
            vector = [x.strip().replace("*I", "i").replace("I", "i")
                      for x in w["v"].strip("{}").split(",")]
            self.assertEqual(vector, [x.replace("*I", "i").replace("I", "i") for x in p["v"]])
            self.assertIn("u_0=\\sqrt{%s}\\,(%s)." % (w["u0NormFactorSquared"], ",".join(vector)),
                          self.text)
            self.assertIn("$S=%s$" % w["S"], self.text)
            self.assertIn("Here $\\rho=%s$ and $p=%s$" % (w["rho"], w["pTransverse"]), self.text)
            self.assertTrue(p["allGminusKappaT64Zero"] and p["negativeControlSlopePlus1Fails"])
        for name in ("x0IndependentExactExamples", "x0IndependentConstruction",
                     "realKPlaneWaveCannotSource", "transversePressuresEqualForEveryX0X4State"):
            self.assertTrue(self.wolfram["checks"]["P_source_" + name])
        self.assertTrue(self.python["checks"]["P_source"])

    def test_cell_labels_and_session_evidence_quoted_match_the_wolfram_report(self):
        measurements = self.wolfram["measurements"]
        bullet = [line for line in self.text.split("\n") if line.startswith('- "Cell $N$"')][0]
        self.assertIn("(%d cells)" % measurements["notebookNonOutputCellCount"], bullet)
        for item in measurements["notebookCitedCellLabels"].split("; "):
            number, rest = item.split(": ", 1)
            label, outs = rest.split(" -> ")
            self.assertIn("%s %s" % (number, label), bullet)
            ranges = [(int(a), int(b)) for a, b in re.findall(r"Out\[(\d+)\] to Out\[(\d+)\]", bullet)]
            for out in re.findall(r"Out\[(\d+)\]", outs):
                self.assertTrue("Out[%s]" % out in bullet or any(a <= int(out) <= b for a, b in ranges), out)
        evidence = measurements["notebookSessionEvidence"]
        self.assertIn("Fri 30 Jan 2026", evidence)
        self.assertIn("cell 1058 last CellChangeTimes: 2025-12-04", evidence)
        self.assertIn("15.0 for Microsoft Windows (64-bit) (July 2, 2026)", evidence)
        self.assertIn("verifier kernel: 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)", evidence)
        for phrase in ("2026-01-30", "2025-12-04", "15.0.1 of July 2, 2026", "from In[1024] for cell 1058 to In[1113]"):
            self.assertIn(phrase, self.text)

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


def pdf_font_charsets(content: bytes) -> dict[str, set[str]]:
    """FontName -> set of glyph names in its /CharSet (object streams inflated)."""
    chunks = [content]
    for match in re.finditer(rb"stream\r?\n", content):
        start = match.end()
        end = content.find(b"endstream", start)
        try:
            chunks.append(zlib.decompress(content[start:end]))
        except zlib.error:
            pass
    text = b"\n".join(chunks)
    fonts = {}
    pattern = re.compile(rb"/FontName\s*/([A-Z]{6}\+[A-Za-z0-9-]+)(?:(?!/FontName).){0,600}?/CharSet\s*\(([^)]*)\)",
                         re.S)
    for match in pattern.finditer(text):
        fonts[match.group(1).decode()] = set(match.group(2).decode().strip("/").split("/"))
    return fonts


class PdfGlyphTests(unittest.TestCase):
    """pdflatex does not warn about these glyph substitutions, so the PDF itself is checked:
    no \\mathbb 1 (msbm slot 49 is 'notforces'), no '--' en-dash ligature and no curly
    left quote for a backtick in the typewriter font."""

    def test_no_notforces_endash_or_quoteleft_substitutions(self):
        fonts = pdf_font_charsets(PDF.read_bytes())
        mono = [name for name in fonts if "LMMono" in name]
        self.assertTrue(mono, sorted(fonts))
        for name in mono:
            self.assertNotIn("endash", fonts[name], name)
            self.assertNotIn("quoteleft", fonts[name], name)
        for name in fonts:
            if "MSBM" in name:
                self.assertNotIn("notforces", fonts[name], name)


if __name__ == "__main__":
    unittest.main()
