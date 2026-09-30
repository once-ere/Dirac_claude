# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the matter-antimatter provenance document of dirac16complex.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_matter_antimatter_publication.py" -v

The document provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md is built with
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md
into provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.{tex,pdf}; the edition
dirac16complex-matter-antimatter is registered in provenance/pdf-specifications.json.

The tests pin the sha256 of the Markdown and of the LaTeX file, require that the
committed .tex is exactly the builder's output for the committed .md, that the
registered PDF edition matches the committed PDF, that the title, subtitle, sections
and required phrases are present, that the honest answer comes first and that no
sentence claims what is not proved, and that every check count, check name, number,
table entry and hash the document quotes agrees with the exact reports:

    artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
    artifacts/dirac16complex/matter-antimatter/python-matter-antimatter-report.json
    artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json
    artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
    artifacts/dirac16complex/pair-creation/pairing-theory.json

The table of named discrete maps (Section 5.5) is recomputed here from the
transformation rule of Theorem M2 and compared with the Wolfram and Python summaries.

After an intended edit of the document: rebuild and register it with
    python scripts/build_provenance_pdf.py --register provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md
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

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

PROVENANCE = REPOSITORY_ROOT / "provenance"
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_MATTER_ANTIMATTER.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_MATTER_ANTIMATTER.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf"
EDITION = "dirac16complex-matter-antimatter"
ARTIFACTS = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "matter-antimatter"
WOLFRAM_REPORT = ARTIFACTS / "wolfram-matter-antimatter-report.json"
PYTHON_REPORT = ARTIFACTS / "python-matter-antimatter-report.json"
THEORY = ARTIFACTS / "matter-antimatter-theory.json"
PAIRING = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "pair-creation"
PAIRING_REPORT = PAIRING / "wolfram-pairing-report.json"
PAIRING_THEORY = PAIRING / "pairing-theory.json"
STAGE1 = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "arbitrary-field"

MARKDOWN_SHA256 = "5f6cf7eb4a08565ad9ff78ff0499970dfba2670513704c20bf36419d301ef71f"
TEX_SHA256 = "ffacebf1a4d6720970b607c8f945e162d218502427c8bb51bf809e1e001ea0e3"

# The Python report records the hash of the Wolfram theory file it compared with.  The
# committed report was written against an earlier, otherwise identical Wolfram run
# (Section 11.3 of the document); a regenerated report records the current hash.
STALE_THEORY_SHA256 = "a3a85c9adc1b19733a3a4f09e8702eed2b6966e6156b644012011fcfe57a0d31"

TITLE = "Matter and antimatter in the dirac16complex theory: what can be proved"
SUBTITLE = ("Exact charge conservation, discrete symmetries, the allowed charge-violating "
            "terms, the chirality pair of universes and the Sakharov conditions, with "
            "independent machine checks")
REQUIRED_SECTIONS = (
    "1. Summary: the honest answer first",
    "2. The matter-antimatter problem from zero",
    "3. The theory, its two fields and the conventions",
    "4. Theorem M1: exact U(1) symmetry and charge conservation",
    "5. Theorem M2: charge conjugation, reflections and time reversal",
    "6. Theorem M3: the charge-violating terms allowed by the symmetry",
    "7. Theorem M4: the chirality pair of universes",
    "8. M5: the conditional scenario, stated as a hypothesis",
    "9. M6: the Sakharov scorecard",
    "10. What would have to be added to the theory",
    "11. Verification records",
    "12. Reproduction",
    "13. Non-claims",
    "14. References",
)
REQUIRED_PHRASES = (
    "cannot be proved",
    "Sakharov's first condition fails",
    "Sakharov's second condition fails",
    "baryon-to-photon ratio",
    "Planck 2018",
    "Boyle, Finn and Turok",
    "JETP Lett. 5, 24 (1967)",
    "Astron. Astrophys. 641, A6 (2020)",
    "Phys. Rev. Lett. 121, 251301 (2018)",
    "**not predicted**",
    "**hypotheses**",
    "H1 (hypothesis, not derived)",
    "H2 (hypothesis, not derived)",
    "H3 (hypothesis, not derivable within the theory)",
    "Majorana-type",
    "Krein metric $-B$",
    "PAIR_T1krein",
    "recorded floating-point data",
)
REFERENCE_COUNT = 13


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def prose_lines(text: str) -> list[str]:
    """The lines outside fenced code blocks."""
    lines, inside = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            inside = not inside
            continue
        if not inside:
            lines.append(line)
    return lines


def section(text: str, heading: str) -> str:
    start = text.index("\n" + heading + "\n")
    level = heading.split(" ")[0]
    rest = text[start + len(heading) + 2:]
    ends = [m.start() for m in re.finditer(r"^#{2,%d} " % len(level), rest, re.M)]
    return rest[:ends[0]] if ends else rest


def table_rows(text: str, header: str) -> list[list[str]]:
    lines = text.split("\n")
    start = lines.index(header)
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def sentences(text: str) -> list[str]:
    flat = " ".join(line for line in prose_lines(text) if not line.startswith("|"))
    return [s for s in re.split(r"(?<=[.!?])\s+", flat) if s]


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
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf")
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

    def test_required_sections_in_order(self):
        headings = [line[3:] for line in markdown_text().split("\n") if line.startswith("## ")]
        self.assertEqual(headings[0], SUBTITLE)
        self.assertEqual(headings[1:], list(REQUIRED_SECTIONS))

    def test_required_phrases(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_the_first_paragraph_is_the_honest_answer(self):
        lines = markdown_text().split("\n")
        start = lines.index("## 1. Summary: the honest answer first")
        first = next(line for line in lines[start + 1:] if line.strip())
        self.assertTrue(first.startswith("**The honest answer.** The request was to prove that "
                                         "this theory solves the current matter-antimatter "
                                         "mysteries; that statement is not proved in this "
                                         "document, and it cannot be proved"), first[:200])
        for phrase in ("exactly invariant under the phase transformation",
                       "for every potential $U(S)$", "conserved in every gravitational field",
                       "no process described by the theory can create a net charge inside one "
                       "universe", "Sakharov's first condition fails",
                       "Sakharov's second condition fails as well",
                       "No departure-from-equilibrium computation exists"):
            self.assertIn(phrase, first)
        # nothing precedes the honest answer except the title block
        self.assertEqual([line for line in lines[:start] if line.strip()],
                         ["# " + TITLE, "## " + SUBTITLE])

    def test_no_sentence_claims_the_solution_or_a_prediction(self):
        negations = ("not", "cannot", "neither", "none", "no ")
        for sentence in sentences(markdown_text()):
            lowered = sentence.lower()
            if "solve" in lowered and "matter-antimatter" in lowered:
                with self.subTest(sentence=sentence[:120]):
                    self.assertTrue(any(word in lowered for word in negations), sentence)
            if "predict" in lowered:
                with self.subTest(sentence=sentence[:120]):
                    self.assertTrue(any(word in lowered for word in negations), sentence)
        text = markdown_text()
        for forbidden in ("we prove that the theory solves", "this proves that the theory solves",
                          "the theory predicts", "predicts the observed", "is explained by the pair"):
            self.assertNotIn(forbidden, text.lower())

    def test_hypotheses_are_labelled_wherever_they_are_introduced(self):
        text = markdown_text()
        block = section(text, "### 8.1 The hypotheses")
        for label in ("H1", "H2", "H3"):
            line = [l for l in block.split("\n") if l.startswith("- **" + label)][0]
            self.assertIn("hypothesis, not deriv", line)
        self.assertIn("The implication is proved. H1, H2 and H3 are assumptions, none of them "
                      "is derived", text)

    def test_no_placeholders_or_todo_and_no_other_provenance_documents(self):
        text = markdown_text()
        self.assertIsNone(re.search(r"@@[A-Z0-9_]+@@", text))
        self.assertNotIn("TODO", text)
        self.assertNotIn("FIXME", text)
        self.assertIsNone(re.search(r"provenance/[A-Za-z0-9_]+\.md", text.replace(
            "provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md", "")))

    def test_no_double_hyphen_in_prose(self):
        for line in prose_lines(markdown_text()):
            if line.startswith("|---"):
                continue
            self.assertNotIn("--", line, line[:120])

    def test_every_fenced_code_line_fits(self):
        inside = False
        for line in markdown_text().split("\n"):
            if line.startswith("```"):
                inside = not inside
                continue
            if inside:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
        self.assertFalse(inside)

    def test_tables_have_at_most_four_columns(self):
        for line in markdown_text().split("\n"):
            if line.startswith("|"):
                self.assertLessEqual(line.strip().strip("|").count("|") + 1, 4, line)

    def test_references_are_numbered_and_all_cited(self):
        text = markdown_text()
        references = section(text, "## 14. References")
        numbers = [int(n) for n in re.findall(r"^- \[(\d+)\] ", references, re.M)]
        self.assertEqual(numbers, list(range(1, REFERENCE_COUNT + 1)))
        body = text[:text.index("## 14. References")]
        cited = {int(n) for n in re.findall(r"\[(\d+)\]", body)}
        self.assertEqual(cited, set(numbers))


def flatten(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from flatten(item)
    elif isinstance(value, list):
        for item in value:
            yield from flatten(item)
    else:
        yield value


class AgreementWithArtifactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.wolfram = load_json(WOLFRAM_REPORT)
        cls.python = load_json(PYTHON_REPORT)
        cls.theory = load_json(THEORY)
        cls.pairing = load_json(PAIRING_REPORT)
        cls.pairing_theory = load_json(PAIRING_THEORY)
        cls.wm = cls.wolfram["measurements"]
        cls.pm = cls.python["measurements"]

    def test_check_counts_quoted_match_the_reports(self):
        for report, count in ((self.wolfram, 44), (self.python, 75), (self.pairing, 141)):
            self.assertEqual(report["schemaVersion"], 1)
            self.assertEqual(len(report["checks"]), count)
            self.assertTrue(all(value is True for value in report["checks"].values()))
            self.assertIn("  %d of %d checks true\n" % (count, count), self.text)
        self.assertIn("The Wolfram report, all 44 checks:", self.text)
        self.assertIn("The Python report, all 75 checks:", self.text)
        self.assertIn("all of its 141 checks are true", self.text)
        self.assertIn("Wolfram Language 15.0.1", self.wolfram["producer"])
        self.assertIn("Wolfram Language 15.0.1", self.text)

    def test_every_check_name_is_quoted(self):
        code = "\n".join(line for line in self.text.split("\n"))
        for report in (self.wolfram, self.python):
            for name in report["checks"]:
                with self.subTest(name=name):
                    self.assertRegex(code, r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])")

    def test_stage5_krein_checks_quoted_are_the_reports(self):
        quoted = set(re.findall(r"PAIR_T1krein_[A-Za-z]+", self.text))
        in_report = {name for name in self.pairing["checks"] if name.startswith("PAIR_T1krein_")}
        self.assertEqual(quoted, in_report)
        self.assertEqual(len(in_report), 12)
        self.assertTrue(all(self.pairing["checks"][name] for name in in_report))
        stage5 = self.pm["M4"]["stage5Pairing"]
        self.assertTrue(stage5["T1kreinPresent"] and stage5["T1kreinReportChecksAllTrue"])
        self.assertEqual(set(stage5["T1kreinReportChecks"]), in_report)
        self.assertEqual(self.wm["M4_kreinLevelStatus"],
                         "taken from the Stage-5 pairing report (all of its checks true)")
        self.assertIn("T1krein", self.pairing_theory)
        self.assertIn("energy -|eps| and charge -1 per quantum",
                      self.pairing_theory["T1krein"]["imageField"])
        self.assertIn("(E, Q, S) -> (E, Q, -S)",
                      self.pairing_theory["T1krein"]["independentQuantisation"])

    def test_stage1_checks_and_hashes_cited(self):
        cited = self.wm["M1_stage1ChecksCited"]["reports"]
        for label, entry in cited.items():
            path = "artifacts/dirac16complex/arbitrary-field/" + entry["file"]
            self.assertIn(path + "\n  " + entry["sha256"] + "\n", self.text)
            self.assertEqual(sha256_file(STAGE1 / entry["file"]), entry["sha256"])
            for name, value in entry["checks"].items():
                self.assertTrue(value)
                self.assertIn(name, self.text)

    def test_m1_numbers_quoted_match_the_reports(self):
        counts = self.wm["M1_grassmannPowersOfS_monomialCounts_k1to17"]
        self.assertIn(", ".join(str(c) for c in counts[:-2]) + ", %d and %d monomials" % tuple(counts[-2:]),
                      self.text)
        grass = self.wm["M1_u1GrassmannG1"]
        self.assertEqual({row["monomials"] for row in grass}, {1848})
        self.assertTrue(all(row["charges"] == [0] for row in grass))
        self.assertIn("1848 monomials at each point", self.text)
        noether = self.wm["M1_noetherIdentityGrassmannG1"]
        self.assertEqual({row["lhsMonomials"] for row in noether}, {1088})
        self.assertIn("1088 monomials on the left-hand side", self.text)
        onshell = self.wm["M1_onShellConservationG1"]
        pairs = ", ".join("$(%s,%s)$" % (row["m"], row["lambda"]) for row in onshell[:2])
        self.assertIn("$(m,\\lambda)=" + pairs.replace("$(", "(", 1) + " and $(%s,%s)$"
                      % (onshell[2]["m"], onshell[2]["lambda"]), self.text)
        ks = self.wm["M1_ksFixedNetNumber"]
        self.assertEqual((ks["referenceRunFiles"], ks["referenceLevelsChecked"], ks["rustRunFiles"]),
                         (56, 168, 33))
        self.assertIn("56 reference-solver run files with 168 levels and 33 Rust run files", self.text)
        self.assertIn("%.4e (reference solver) and %.3e (Rust)" % (
            ks["maxAbsDeviationReference"], ks["maxAbsDeviationRust"]), self.text)
        m1 = self.pm["M1"]["perStatisticsAndGeometry"]
        quoted = (m1["grassmann_G_A_generic_nondiagonal"]["lagrangianMonomials"],
                  m1["commuting_G_A_generic_nondiagonal"]["lagrangianMonomials"],
                  m1["grassmann_G_B_diagonal_x0_x4"]["lagrangianMonomials"],
                  m1["commuting_G_B_diagonal_x0_x4"]["lagrangianMonomials"])
        self.assertIn("%d (anticommuting) and %d (commuting) monomials in G_A and %d and %d in G_B"
                      % quoted, self.text)
        self.assertIn("the Noether divergence has %d monomials in G_A and %d in G_B" % (
            m1["grassmann_G_A_generic_nondiagonal"]["noetherDivergenceMonomials"],
            m1["grassmann_G_B_diagonal_x0_x4"]["noetherDivergenceMonomials"]), self.text)
        jets = self.pm["M1"]["divergenceIdentityAllFirstJets"]
        self.assertEqual(jets["proofs"]["E0_identity"]["directions"], 512)
        self.assertEqual(jets["proofs"]["E0_identity"]["directionsWithNonzeroOmega"], 448)
        self.assertFalse(jets["negativeControlNotebookContraction"]["divergenceIdentity"])
        self.assertIn("all 512 basis directions are verified exactly (448 of them have", self.text)
        conventions = self.pm["conventions"]
        self.assertEqual(conventions["exactPhase"], "e^{i alpha} = (3 + 4 i)/5")
        self.assertEqual(conventions["parameters"], {"m": "3/2", "lambda": "5/7", "mu3": "2/3"})
        self.assertIn("$e^{i\\alpha}=(3+4i)/5$; $m=3/2$, $\\lambda=5/7$", self.text)
        self.assertIn("$\\mu_3=2/3$", self.text)

    def test_m2_counts_quoted_match_the_reports(self):
        frames = self.wm["M2_frameLevelG1"]
        per_point = [sum(1 for row in frames if row["point"] == p) for p in (1, 2, 3)]
        self.assertEqual((len(frames), per_point), (31, [21, 5, 5]))
        self.assertTrue(all(row["commutingAgrees"] and row["grassmannAgrees"] for row in frames))
        self.assertIn("31 frame reflections (21 at p1, 5 each at p2 and p3)", self.text)
        flat = self.wm["M2_lagrangianLevelFlat"]
        self.assertEqual(flat["mapsPerStatistics"], 1024)
        self.assertEqual((flat["mismatchesCommuting"], flat["mismatchesGrassmann"]), ([], []))
        self.assertEqual(self.wm["M2_classificationSummary"]["rows"], 512)
        table = self.pm["M2"]["discreteGroupCharacterTable"]
        for statistics in ("grassmann", "commuting"):
            self.assertEqual(sorted(table[statistics]["classCounts"].values()), [256] * 4)
            self.assertEqual(table[statistics]["exactSymmetries"], 256)
            self.assertEqual(table[statistics]["exactChargeFlippingWithoutX4Reversal"], 64)
        canonical = self.pm["M2"]["canonicalStructureOfExactGrassmannSymmetries"]["counts"]
        self.assertEqual((canonical["unitary_preservesX4"], canonical["antiunitary_reversesX4"],
                          canonical["other"]), (128, 128, []))
        self.assertEqual(self.wm["M2_canonicalStructure"]["exactGrassmannSymmetriesChecked"], 256)
        self.assertEqual(self.wm["M2_canonicalStructure"]["signs M B^T M^dagger / B"],
                         {"M=I": -1, "M=gamma8": 1})
        self.assertEqual(self.pm["M2"]["characterHomomorphism"]["randomCompositesTested"], 400)
        for phrase in ("4 classes of 256, 256 exact symmetries, 64 exact charge-reversing",
                       "128 unitary and $x_4$-preserving, 128 antiunitary and $x_4$-reversing",
                       "checked on 400 random composites", "all 512 pairs $(M,R)$",
                       "for all 1024 maps per statistics"):
            self.assertIn(phrase, self.text)
        vectors = [key.split(" n(u)=")[0].replace("u=[", "").replace("]", "")
                   for key in self.pm["M2"]["genericUnitVectorReflections"] if "| linear | grassmann" in key]
        self.assertEqual(len(vectors), 3)
        for vector in vectors:
            self.assertIn("$u=(%s)$" % vector.replace(" ", ""), self.text)
        agreement = self.pm["MA_agreesWithWolfram"]
        self.assertEqual((agreement["classificationRows"]["compared"],
                          agreement["classificationRows"]["disagreements"]), (2048, []))
        self.assertEqual((agreement["symmetrySummary"]["itemsCompared"],
                          agreement["symmetrySummary"]["diffs"]), (22, []))
        self.assertEqual(agreement["chargeReversingSymmetries"]["counts"],
                         {"grassmann": [64, 64], "commuting": [64, 64]})
        self.assertIn("the classification rows (2048 compared, no disagreement)", self.text)
        self.assertIn("(22 items compared, no difference)", self.text)
        intertwiners = self.wm["M2_conjugationIntertwiners"]
        self.assertEqual((intertwiners["dimensionEtaPlus"], intertwiners["dimensionEtaMinus"],
                          intertwiners["basisEtaPlus"], intertwiners["basisEtaMinus"]),
                         (1, 1, "I16", "gamma^8"))
        transpose = self.wm["M2_transposeIntertwiners"]
        self.assertEqual((transpose["dimensionZetaPlus"], transpose["dimensionZetaMinus"]), (1, 1))
        self.assertTrue(transpose["basisZetaMinus"].startswith("C "))
        self.assertTrue(transpose["basisZetaPlus"].startswith("gamma^8 C "))
        self.assertEqual(self.wm["M2_statisticsSign"]["grassmann"], -1)
        self.assertEqual(self.wm["M2_statisticsSign"]["commuting"], 1)

    def test_named_map_table_follows_the_rule_and_the_summaries(self):
        """Section 5.5, recomputed from Theorem M2 (Lemma B signs, statistics sign s)."""
        everything = set(range(8))
        definitions = {
            "$C_0$": (set(), "R", "anti"),
            "$C_8$": (set(), "c", "anti"),
            "chirality": (set(), "c", "lin"),
            "$P_b$, $b\\le3$": ({0}, "R", "lin"),
            "$P'_b$, $b\\le3$": ({0}, "c", "lin"),
            "$C_0P_b$": ({0}, "R", "anti"),
            "$C_8P_b$": ({0}, "c", "anti"),
            "$P_{123}$": ({1, 2, 3}, "R", "lin"),
            "$C_8P_{123}$": ({1, 2, 3}, "c", "anti"),
            "$P_{0123}$": ({0, 1, 2, 3}, "R", "lin"),
            "$C_0P_{0123}$": ({0, 1, 2, 3}, "R", "anti"),
            "$T$": ({4}, "c", "lin"),
            "$T$, antilinear": ({4}, "c", "anti"),
            "total inversion": (everything, "R", "lin"),
            "CPT": (everything, "R", "anti"),
            "$CP_{123}T$": ({1, 2, 3, 4}, "R", "anti"),
        }
        forms = {(1, 1): "exact", (1, -1): "$\\mathcal L_{-m,\\lambda}$",
                 (-1, -1): "$-\\mathcal L_{m,-\\lambda}$", (-1, 1): "$-\\mathcal L_{-m,-\\lambda}$"}

        def signs(reflected, monomial, kind, s):
            epsilon = (-1) ** len(reflected) * (1 if monomial == "R" else -1)
            sigma_r = (-1) ** len(reflected & {0, 1, 2, 3})
            if kind == "lin":
                kappa, sigma = sigma_r * epsilon, sigma_r
                current = kappa
            else:
                kappa, sigma = s * sigma_r * epsilon, s * sigma_r
                current = -kappa
            return kappa, sigma, current

        rows = table_rows(self.text, "| Map | Definition | Commuting | Anticommuting |")
        self.assertEqual([row[0] for row in rows], list(definitions))
        exact = {}
        for name, definition, commuting, anticommuting in rows:
            reflected, monomial, kind = definitions[name]
            for s, cell in ((1, commuting), (-1, anticommuting)):
                kappa, sigma, current = signs(reflected, monomial, kind, s)
                with self.subTest(map=name, s=s):
                    self.assertTrue(cell.startswith(forms[(kappa, sigma)]), cell)
                    if "$Q\\to" in cell:
                        self.assertNotIn(4, reflected)
                        self.assertTrue(cell.endswith("$Q\\to-Q$" if current == -1 else "$Q\\to Q$"))
                exact[(name, s)] = (kappa, sigma) == (1, 1)
        for statistics, s in (("commuting", 1), ("grassmann", -1)):
            summary = self.wm["M2_symmetrySummary"][statistics]
            self.assertEqual(summary, self.pm["MA_agreesWithWolfram"]["symmetrySummary"]["python"][statistics])
            expected = {
                "C (R empty, antilinear) exact": exact[("$C_0$", s)] or exact[("$C_8$", s)],
                "P (one space-like reflection, linear) exact":
                    exact[("$P_b$, $b\\le3$", s)] or exact[("$P'_b$, $b\\le3$", s)],
                "CP (one space-like reflection, antilinear) exact":
                    exact[("$C_0P_b$", s)] or exact[("$C_8P_b$", s)],
                "P3 (x1,x2,x3, linear) exact": exact[("$P_{123}$", s)],
                "CP3 (x1,x2,x3, antilinear) exact": exact[("$C_8P_{123}$", s)],
                "T (x4, linear) exact": exact[("$T$", s)],
                "T (x4, antilinear) exact": exact[("$T$, antilinear", s)],
                "CPT (all x, antilinear) exact": exact[("CPT", s)],
                "CP3T (x1..x4, antilinear) exact": exact[("$CP_{123}T$", s)],
            }
            for key, value in expected.items():
                with self.subTest(statistics=statistics, key=key):
                    self.assertEqual(summary[key], value)
        self.assertTrue(self.pm["M2"]["discreteGroupCharacterTable"]["commuting"]["C_exact"])
        self.assertFalse(self.pm["M2"]["discreteGroupCharacterTable"]["grassmann"]["C_exact"])
        self.assertTrue(self.pm["M2"]["discreteGroupCharacterTable"]["grassmann"]["CP_exact_improperSpatialReflection"])

    def test_m3_numbers_quoted_match_the_reports(self):
        forms = self.wm["M3_spinInvariantMassForms"]
        self.assertEqual((forms["dimension"], forms["symmetricSubspaceDimension"],
                          forms["antisymmetricSubspaceDimension"]), (2, 2, 0))
        characters = {tuple(c["character"]): c["dimension"] for c in self.wm["M3_pinCharacterForms"]["characters"]}
        self.assertEqual(characters, {(1, 1): 0, (-1, 1): 1, (1, -1): 1, (-1, -1): 0})
        self.assertIn("dimensions 0, 1, 1, 0 for the trivial, $-n$, $+n$ and determinant characters",
                      self.text)
        survival = self.wm["M3_survival"]
        self.assertEqual(survival["grassmannControlAntisymmetricNonzeroMonomials"], 8)
        ranks = survival["commutingMassTypeRanks"]
        self.assertEqual((ranks["C P_-"], ranks["C P_+"], ranks["C"], ranks["C gamma^8"]), (8, 8, 16, 16))
        self.assertIn("ranks 8, 8, 16 and 16 for $CP_-$, $CP_+$, $C$ and $C\\gamma^8$", self.text)
        self.assertIn("a control with an antisymmetric matrix has 8 nonzero monomials", self.text)
        quartic = self.wm["M3_extraGrassmannQuartic"]
        self.assertEqual((quartic["Q4Monomials"], quartic["Q4Charges"]), (40, [4]))
        examples = self.pm["M3"]["quarticChargeViolatingExamplesGrassmann"]["examples"]
        q2 = examples["grassmann | Q2 = sum_{a<b} eta_aa eta_bb (Psi^T C g^a g^b Psi)(Psi^dagger C g^a g^b Psi)"]
        self.assertEqual((q2["monomials"], q2["u1Charge"]), (160, 2))
        self.assertTrue(examples["grassmann | relation to the chiral form"]["proportional"])
        self.assertIn("= 8 sum", examples["grassmann | relation to the chiral form"]["relation"])
        self.assertIn("(40 monomials, charge 4)", self.text)
        self.assertIn("(160 monomials, charge 2)", self.text)
        self.assertIn("$Q_4$ equals exactly 8 times the chiral form", self.text)
        mass = self.pm["M3"]["massTypeSurvivalAndCharge"]
        self.assertEqual((mass["grassmann | Psi^T C Psi"]["monomials"], mass["commuting | Psi^T C Psi"]["monomials"],
                          mass["grassmann | Psi^dagger C Psi"]["monomials"]), (0, 8, 16))
        curved = self.pm["M3"]["derivativeTypeSurvivalCurved"]
        self.assertEqual(curved["grassmann | sqrt|g| Psi^T C gamma8 gamma^mu D_mu Psi"]["nonzeroELComponents"], 16)
        self.assertTrue(curved["grassmann | sqrt|g| Psi^T C gamma^mu D_mu Psi"]["totalDivergence"])
        self.assertTrue(curved["commuting | sqrt|g| Psi^T C gamma8 gamma^mu D_mu Psi"]["totalDivergence"])
        self.assertEqual(self.pm["M3"]["fullSpinCharacter"],
                         {"strictlyInvariantUnderFullSpin44": 0, "covariantWithSpinorNormCharacter": 2})

    def test_m4_numbers_and_krein_table_match_the_reports(self):
        self.assertEqual(self.wm["M4_pairEMTGrassmannG1point1"],
                         {"pairEMTVanishesAll64": True, "EMTNonzeroComponents": 64, "symmetric": True})
        self.assertIn("all 64 components of $T^{\\mathrm{pair}}_{\\mu\\nu}$ vanish at p1", self.text)
        per = self.pm["M4"]["gamma8ChargeFlipCurved"]["perStatistics"]
        self.assertEqual({per[s]["emtNonzeroComponents"] for s in per}, {36})
        rows = table_rows(self.text, "| $m$, $k$ | $+m$ universe | Image field, $-B$ | Independent, $+B$ |")
        samples = self.pm["M4"]["kreinModeFacts"]["samples"]
        self.assertEqual(len(rows), len(samples))
        for row, sample in zip(rows, samples):
            quantum = sample["perQuantum(E, Q, S)"]
            expected = ["$%s$, $(%s)$" % (sample["m"], ",".join(sample["k"]))] + [
                "$(%s)$" % ",".join(quantum[key]) for key in
                ("plusUniverse", "imageWithMetricMinusB", "independentMinusMWithMetricPlusB")]
            self.assertEqual(row, expected)
            self.assertEqual(sample["kreinSignatureOnPositiveEnergySpace"], [4, 4])
        self.assertTrue(all(self.wm["M4_kreinOneParticle"]["checks"].values()))

    def test_m5_and_m6_statements_match_the_reports(self):
        m5 = self.wm["M5_implication"]
        self.assertEqual(m5["symbolicCheck"], {"Q_+ + Q_- simplifies to": "0",
                                               "dQ_-/dx4 given dQ_+/dx4 = 0": "0"})
        self.assertIn("ASSUMPTION", m5["hypotheses"]["H1"])
        self.assertIn("ASSUMPTION", m5["hypotheses"]["H2"])
        self.assertIn("ASSUMPTION", m5["hypotheses"]["H3"])
        self.assertIn("NOT predicted", m5["notPredicted"])
        self.assertIn("NOT PROVED", self.pm["honestAnswer"])
        self.assertIn("NOT proved", self.theory["honestyRule"])
        scorecard = self.pm["M6_sakharovScorecard"]
        rows = table_rows(self.text, "| Sakharov condition [1] | Status in the theory as built | "
                                     "What would have to be added |")
        self.assertEqual(len(rows), len(scorecard), 3)
        for row, entry in zip(rows, scorecard):
            status = entry["statusInTheoryAsBuilt"]
            if status.startswith("FAILS"):
                self.assertTrue(row[1].startswith("Fails"), row[1])
            else:
                self.assertTrue(status.startswith("NOT ADDRESSED"))
                self.assertTrue(row[1].startswith("Not addressed"), row[1])
            for name in entry["computedBy"]:
                if name.startswith("MA_M1_noetherIdentity_"):
                    continue  # quoted through the pattern MA_M1_noetherIdentity_<X>_<G>
                self.assertIn(name, self.text)
        self.assertIn("MA_M1_noetherIdentity_<X>_<G>", self.text)

    def test_recorded_hashes_match_the_reports_and_the_files(self):
        wolfram_sources = self.wolfram["sourceSha256"]
        python_sources = self.python["sourceSha256"]
        python_inputs = self.python["inputSha256"]
        expected = {
            "wolfram/Dirac16ComplexMatterAntimatter.wl": wolfram_sources["wolfram/Dirac16ComplexMatterAntimatter.wl"],
            "scripts/verify_dirac16complex_matter_antimatter.wls":
                wolfram_sources["scripts/verify_dirac16complex_matter_antimatter.wls"],
            "wolfram/Dirac16ComplexGeometry.wl": wolfram_sources["wolfram/Dirac16ComplexGeometry.wl"],
            "scripts/check_dirac16complex_matter_antimatter.py":
                python_sources["scripts/check_dirac16complex_matter_antimatter.py"],
            "scripts/grassmann_algebra.py": python_sources["scripts/grassmann_algebra.py"],
            "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json":
                wolfram_sources["artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"],
            "artifacts/dirac16complex/pair-creation/pairing-theory.json":
                wolfram_sources["artifacts/dirac16complex/pair-creation/pairing-theory.json"],
            "artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json":
                wolfram_sources["artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json"],
            "artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json": sha256_file(THEORY),
            "artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json":
                sha256_file(WOLFRAM_REPORT),
        }
        for path, digest in expected.items():
            with self.subTest(path=path):
                self.assertIn(path + "\n  " + digest + "\n", self.text)
                self.assertEqual(sha256_file(REPOSITORY_ROOT / path), digest)
        for path in ("artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
                     "artifacts/dirac16complex/pair-creation/pairing-theory.json",
                     "artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json"):
            self.assertEqual(python_inputs[path], wolfram_sources[path])
        self.assertEqual(self.theory["sourceSha256"], wolfram_sources)
        compared = python_inputs["artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json"]
        self.assertIn(compared, (STALE_THEORY_SHA256, sha256_file(THEORY)))
        self.assertIn("matter-antimatter-theory.json compared by the committed Python report\n  "
                      + STALE_THEORY_SHA256 + "\n", self.text)
        self.assertIn("matter-antimatter-theory.json, current file\n  " + sha256_file(THEORY) + "\n",
                      self.text)


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
