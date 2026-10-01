# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the published dirac16complex textbook.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_textbook_publication.py" -v

The book provenance/DIRAC16COMPLEX_TEXTBOOK.md is generated from the chapter files
provenance/textbook/chapters/00-...md to 20-...md by
    python scripts/build_textbook.py
(handoff/specs/TEXTBOOK_SPEC.md, section 2) and built with the builder's DEVELOPER LAYOUT
and chapter numbering from zero:
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md --developer-layout --number-sections-from-zero
into provenance/DIRAC16COMPLEX_TEXTBOOK.{tex,pdf}; the edition dirac16complex-textbook is
registered in provenance/pdf-specifications.json.  Without --number-sections-from-zero LaTeX
would print chapter N as N+1, and every "Section N.M" of the text would point one chapter
too far.

The tests pin the sha256 of the Markdown and of the LaTeX file and require that the
committed Markdown is exactly the assembler's output for the committed chapters (every
assembler check true, and build_textbook.py --verify-output passes), that the committed
.tex is exactly the builder's output for the committed Markdown, that the registered PDF
edition matches the committed PDF and that its LaTeX numbering (the hyperref destinations
section.N and subsection.N.M) is the Markdown numbering, chapter 0 included.  They require
the 21 chapter headings in order and the honesty statements of Section 0.2, of Chapter 16
and of Chapter 17 (quoted from the chapters), and they tie the status numbers of the
abstract and of Chapter 16 to the committed reports.  A lint over the prose of the whole
book (quotations, code and display math excluded) requires every sentence that speaks of
universes being created in pairs, of the theory solving or explaining the matter-antimatter
problem, or of a prediction of the asymmetry, to carry a negation or to mark the statement
as a hypothesis, an open question or a question; the status-word exercises that list such a
statement for classification must be answered HYPOTHESIS or OPEN.

After an intended edit of a chapter: reassemble, rebuild and register with
    python scripts/build_textbook.py
    python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md --developer-layout --number-sections-from-zero --register
and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import functools
import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import build_textbook  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

PROVENANCE = REPOSITORY_ROOT / "provenance"
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_TEXTBOOK.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_TEXTBOOK.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_TEXTBOOK.pdf"
CHAPTERS = PROVENANCE / "textbook" / "chapters"
EDITION = "dirac16complex-textbook"
ARTIFACTS = REPOSITORY_ROOT / "artifacts" / "dirac16complex"
KOHN_SHAM_CHECK_REPORT = ARTIFACTS / "kohn-sham" / "python-check-report.json"
PAIR_CREATION = ARTIFACTS / "pair-creation"
STAGE1_DOCUMENT = PROVENANCE / "DIRAC16COMPLEX_ARBITRARY_FIELD.md"

MARKDOWN_SHA256 = "2b0073d1d4ce453d36112949f0b884f5e8a66ab331943f9584a5a05e0ba13610"
TEX_SHA256 = "6ac598cc6071e00888c8b5b9125fcd6c0c884ac5ebe770d3264474b11e7c98bd"

CHAPTER_HEADINGS = (
    "0. How to read this book",
    "1. Mathematical toolkit from zero",
    "2. Clifford algebras and spinors from zero",
    "3. Split octonions and the notebook's construction of the gamma matrices",
    "4. Curved space from zero",
    "5. Classical field theory, Grassmann numbers, and why the notebook's Lg[] is empty",
    "6. The two fields and their Lagrangians",
    "7. Field equations, energy–momentum tensor and equations of state",
    "8. Canonical quantization in 4+4 dimensions",
    "9. The primordial gravitational field of the notebook",
    "10. Solving differential equations on a computer from zero",
    "11. The five dark-sector experiments",
    "12. Many-body quantum mechanics and density functional theory from zero",
    "13. The Kohn–Sham approximation for dirac16complex in the primordial field",
    "14. The Kohn–Sham approximation for dirac16complex00",
    "15. The pairing theorems",
    "16. Does the big bang create universes in pairs?",
    "17. Matter and antimatter",
    "18. Open problems and how a student could attack them",
    "19. Reproducing everything",
    "20. Glossary and index of verifier checks",
)
SECTION_COUNT = 350

# The sentence of the Stage-1 document (its Section 1.3, item 6) that Section 0.2 and
# Chapter 16 quote.
STAGE1_SENTENCE = ("a structural property of the equations, not a claim that universes of "
                   "masses $\\pm M$ are created in pairs")

# Quoted from Section 0.2.
SECTION_0_2_STATEMENTS = (
    "Two parts of the request are not established by this project, and a textbook that wrote "
    "them as established would teach something false.",
    "it teaches exactly what the repository proves and computes, together with every "
    "assumption, and it never writes \"proved\" for a statement that is not proved.",
    "The first of the two parts is \"the big bang creates universes in pairs\". The notebook "
    "states it as a hypothesis",
    "Cell 6 says: \"HYPOTHESIS: If, employing the Einstein eqs (or Einstein-Lovelock eqs), "
    "superluminal inflation/deflation exists, then at time x4 = 0 ... a pair of universes "
    "with MASSES ± M is created\".",
    "Cell 17 records the task: \"TODO: prove Universe(s) of masses ±M are created in pairs!\"",
    "Their consequences are strong but limited.",
    "For the quantized field the cancellation is not one between two separate universes.",
    "There the image $\\gamma^8\\Psi$ is not a second universe",
    "Whether any quantum description of two independent universes gives a cancellation is "
    "open (row L37).",
    "And no creation process, no rate and no probability amplitude is derived, and no "
    "dynamical big bang is computed.",
    STAGE1_SENTENCE,
    "Chapter 16 states exactly what is proved, what is merely consistent and what is not "
    "derived; the missing step is an open problem.",
    "The theory as built fails the first two conditions exactly and does not address the "
    "third.",
    "Sakharov's first condition fails",
    "So Sakharov's second condition fails as well",
    "No departure from equilibrium is computed, and the theory contains no baryons of the "
    "Standard Model of particle physics",
    "It therefore does not solve the matter–antimatter problem.",
    "If a second classical field is in the configuration $\\gamma^8\\Psi$ of the first (an "
    "assumption, not derived), the two carry zero total charge; for two independently "
    "quantized universes there is no such cancellation (Chapter 17).",
    "lists what would be needed to turn such an idea into an explanation, and labels every "
    "scenario as a hypothesis.",
)

# Quoted from Chapter 16, by section.
CHAPTER_16_STATEMENTS = {
    "16.1": (
        "**OPEN (not derived).** No creation process, no creation rate, no probability "
        "amplitude, no wave function of the universe and no dynamical big bang is derived "
        "anywhere in the project.",
        "**HYPOTHESIS.** \"The big bang creates universes in pairs\" therefore remains what "
        "the notebook calls it, a hypothesis.",
        STAGE1_SENTENCE,
        "These separate conservation laws forbid the appearance of a cancelling pair out of "
        "the empty state unless each member has zero charge",
        "Only an interaction between the members, which the theory does not contain, could "
        "leave the totals as the only conserved quantities (OPEN).",
        "at the quantum level the cancellation is OPEN.",
        "It is much weaker than \"the process happens\".",
    ),
    "16.2": (
        "The project documents have responded to the TODO of cell 17 twice, in the same "
        "careful way, without claiming to have carried it out.",
        "**Status.** The hypothesis of cells 6, 7 and 17 is a HYPOTHESIS",
    ),
    "16.11": (
        "There is no equation whose solution describes a transition from a state without "
        "universes to a state with a pair.",
        "**No dynamical big bang.**",
        "**No selection of pairs.** T1 to T3 hold for every solution.",
        "**No solution of the matter–antimatter problem.** The pairing theorems do not "
        "create charge.",
        "That it explains the observed excess of matter is not established.",
    ),
}

# Quoted from Chapter 17, by section.
CHAPTER_17_STATEMENTS = {
    "17.1": (
        "**The honest answer.** The theory as built does not solve the matter–antimatter "
        "problem, and within the theory the central step of such a solution is impossible.",
        "so no process of the theory can create a net charge inside one universe; for the "
        "quantized field this holds at a formal level, because no regularization of the "
        "quantum theory is constructed and no anomaly is computed (Section 17.9).",
        "Nothing in the repository computes a departure from thermal equilibrium.",
        "no cancellation between two independently quantised universes follows",
        "Under three hypotheses that nothing in the repository derives",
        "The picture predicts no number; in particular it does not predict the observed "
        "baryon-to-photon ratio $\\eta\\approx6\\times10^{-10}$.",
    ),
    "17.14": (
        "**The hypotheses.** The following three statements are **hypotheses**. None of them "
        "is derived anywhere in the repository.",
        "- **H1 (HYPOTHESIS, not derived).**",
        "- **H2 (HYPOTHESIS, not derived).**",
        "- **H3 (HYPOTHESIS, not derivable within the theory).**",
        "The observed $\\eta\\approx6\\times10^{-10}$ is **not predicted**",
    ),
    "17.15": (
        "**The answer.** The dirac16complex theory as built does **not** solve the "
        "matter–antimatter problem.",
        "and it predicts no value of $\\eta$.",
        "The statement \"this theory solves the matter–antimatter mysteries\" is therefore "
        "not established; it cannot be proved within the theory as built, because its "
        "central part, the creation of a net charge inside one universe, is excluded by "
        "Theorem M1.",
    ),
    "17.16": (
        "none of them is present in the theory, none is claimed to be natural, and none has "
        "been shown to be sufficient.",
    ),
    "17.18": (
        "- L. Boyle, K. Finn and N. Turok, \"CPT-Symmetric Universe\", Phys. Rev. Lett. 121, "
        "251301 (2018).",
    ),
}

# The abstract states both answers.
ABSTRACT_STATEMENTS = (
    "and no creation process, rate or amplitude is derived, so the statement remains the "
    "notebook's hypothesis.",
    "Does the theory explain the excess of matter over antimatter? It does not:",
    "compared with an independent reference solver in 63 checks, of which 62 pass",
)

# The exact Stage-5 reports and the counts that Section 16.1 quotes for them.
PAIR_CREATION_REPORTS = {
    "wolfram-pairing-report.json": 141,
    "python-pairing-report.json": 172,
    "wolfram-dirac16complex00-report.json": 46,
    "python-dirac16complex00-report.json": 49,
}

# Text that the lint never sees: code spans first (they may contain quotes), then
# quotations (the request, the notebook's cells and other quoted words are reported, not
# asserted).
CODE_SPAN = re.compile(r"`[^`\n]*`")
QUOTATION = re.compile(r"\"[^\"\n]*\"|“[^”\n]*”")
BLOCK_BOUNDARY = re.compile(r"\n[ \t]*\n|\n(?=[ \t]*(?:[-*]|\d+\.|\|)[ \t])")
SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z(*])")
NEGATION = re.compile(r"\b(?:not|no|cannot|neither|nor|none|never|nothing|without|fails?|"
                      r"failed|excluded|impossible)\b|n't\b", re.I)
HEDGE = re.compile(r"hypothes|\bOPEN\b|\bwhether\b|\bif\b|\?", re.I)
REQUEST = re.compile(r"\bask(?:s|ed)?\b|\brequest", re.I)
CREATION_VERB = re.compile(r"\bcreat(?:e|es|ed|ing)\b", re.I)
UNIVERSES_IN_PAIRS = re.compile(r"universe.*\b(?:in pairs|together)\b|\bpairs? of universes\b",
                                re.I)
SOLVE_VERB = re.compile(r"\b(?:solv(?:e|es|ed|ing)|resolv(?:e|es|ed|ing)|explain(?:s|ed|ing)?|"
                        r"accounts? for|solution (?:of|to))\b", re.I)
MATTER_ANTIMATTER_PROBLEM = re.compile(
    r"anti[ \-–]?matter[ \-–]*(?:problem|myster|asymmetr|puzzle)|excess of matter|"
    r"matter over antimatter|asymmetry between matter|baryon(?:ic)? asymmetr|"
    r"baryon-to-photon", re.I)
PREDICTION = re.compile(r"\bpredict", re.I)
PREDICTION_TOPIC = re.compile(r"baryon|asymmetr|antimatter|\bvalue of\b", re.I)
PROOF_VERB = re.compile(r"\bprov(?:e|es|ed|en|ing)\b|\bproof\b|\bestablish(?:es|ed)?\b|"
                        r"\bdemonstrat(?:e|es|ed)\b|\bshow(?:s|n|ed)?\b", re.I)
BIG_BANG = re.compile(r"\bbig bang\b", re.I)
STATUS_EXERCISE = re.compile(r"^(?:\*\*)?Exercise (\d+\.\d+)\.(?:\*\*)? .*\bstatus words?\b")
EXERCISE_ITEM = re.compile(r"\(([a-z])\) ")
# Affirmative forms that no sentence of the book may contain outside quotations.
FORBIDDEN_PHRASES = (
    "this theory solves", "the theory solves", "theory explains the matter",
    "theory explains the observed", "theory resolves", "solves the matter",
    "explains the matter–antimatter", "proves that the big bang", "proved that the big bang",
    "shows that the big bang", "we prove that universes", "it is proved that universes",
    "the big bang is proved", "is proved to create", "the theory predicts",
    "predicts the observed", "is explained by the pair",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


@functools.lru_cache(maxsize=None)
def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


@functools.lru_cache(maxsize=None)
def assembly() -> build_textbook.Assembly:
    return build_textbook.assemble(CHAPTERS, image_root=REPOSITORY_ROOT,
                                   display_root=REPOSITORY_ROOT)


def sections(text: str) -> dict[str, str]:
    """Map '16.1' (a ### heading) or '16' (a ## heading) to its text up to the next heading."""
    result = {}
    pattern = re.compile(r"^(#{2,3}) (\d+(?:\.\d+)?)\.? ", re.M)
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(2)] = text[match.start():end]
    return result


def fenced_blocks(text: str) -> list[list[str]]:
    blocks, current, inside = [], [], False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            if inside:
                blocks.append(current)
                current = []
            inside = not inside
            continue
        if inside:
            current.append(line)
    return blocks


def prose_blocks(text: str) -> list[str]:
    """Paragraphs, list items, table rows and headings outside fenced code and display
    math, each joined into one line."""
    kept, in_code, in_math = [], False, False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            kept.append("")
        elif in_code:
            kept.append("")
        elif stripped == "$$":
            in_math = not in_math
            kept.append("")
        elif in_math:
            kept.append("")
        elif stripped.startswith("#"):
            kept.extend(["", line, ""])
        else:
            kept.append(line)
    blocks = (" ".join(block.split()) for block in BLOCK_BOUNDARY.split("\n".join(kept)))
    return [block for block in blocks if block]


def without_quotations(block: str) -> str:
    block = CODE_SPAN.sub(" ", block)
    if block.count("\"") % 2 == 0:
        block = QUOTATION.sub(" ", block)
    return block


def claim_sentences(block: str) -> list[str]:
    return [sentence for sentence in SENTENCE_BOUNDARY.split(without_quotations(block))
            if sentence.strip()]


def is_pair_creation_sentence(sentence: str) -> bool:
    return bool(CREATION_VERB.search(sentence) and UNIVERSES_IN_PAIRS.search(sentence))


def is_matter_antimatter_solution_sentence(sentence: str) -> bool:
    return bool(SOLVE_VERB.search(sentence) and MATTER_ANTIMATTER_PROBLEM.search(sentence))


def is_prediction_sentence(sentence: str) -> bool:
    return bool(PREDICTION.search(sentence) and PREDICTION_TOPIC.search(sentence))


def is_big_bang_proof_sentence(sentence: str) -> bool:
    return bool(BIG_BANG.search(sentence) and PROOF_VERB.search(sentence))


def affirmative_forbidden_phrases(text: str) -> tuple[int, list[tuple[str, str]]]:
    """(number of occurrences, [(phrase, sentence)] of the occurrences not preceded by a
    negation of the same sentence) of FORBIDDEN_PHRASES in the prose of text."""
    found, offending = 0, []
    for block in prose_blocks(text):
        for sentence in claim_sentences(block):
            lowered = sentence.lower()
            for phrase in FORBIDDEN_PHRASES:
                position = lowered.find(phrase)
                if position < 0:
                    continue
                found += 1
                if NEGATION.search(sentence[:position]) is None:
                    offending.append((phrase, sentence))
    return found, offending


@functools.lru_cache(maxsize=None)
def lint() -> dict[str, object]:
    return lint_text(markdown_text())


def lint_text(text: str) -> dict[str, object]:
    """Inspect every sentence of text; return the inspected counts, the offending
    sentences of each kind and the items of status-word exercises that state a pair
    creation for classification (exercise number, item letter)."""
    counts = {"pairs": 0, "solves": 0, "predicts": 0, "bigBangProof": 0}
    offending: dict[str, list[str]] = {name: [] for name in counts}
    classified: list[tuple[str, str]] = []
    for block in prose_blocks(text):
        exercise = STATUS_EXERCISE.match(block)
        if exercise:
            items = EXERCISE_ITEM.split(without_quotations(block))
            for letter, item in zip(items[1::2], items[2::2]):
                if is_pair_creation_sentence(item) and not (NEGATION.search(item)
                                                            or HEDGE.search(item)):
                    classified.append((exercise.group(1), letter))
            continue
        for sentence in claim_sentences(block):
            if is_pair_creation_sentence(sentence):
                counts["pairs"] += 1
                if not (NEGATION.search(sentence) or HEDGE.search(sentence)):
                    offending["pairs"].append(sentence)
            if is_matter_antimatter_solution_sentence(sentence):
                counts["solves"] += 1
                if not (NEGATION.search(sentence) or "?" in sentence
                        or REQUEST.search(sentence)):
                    offending["solves"].append(sentence)
            if is_prediction_sentence(sentence):
                counts["predicts"] += 1
                if not (NEGATION.search(sentence) or HEDGE.search(sentence)):
                    offending["predicts"].append(sentence)
            if is_big_bang_proof_sentence(sentence):
                counts["bigBangProof"] += 1
                if not (NEGATION.search(sentence) or HEDGE.search(sentence)):
                    offending["bigBangProof"].append(sentence)
    return {"counts": counts, "offending": offending, "classified": classified}


class TextbookTestCase(unittest.TestCase):
    """assertIn with a short failure message for the long book text."""

    def assertIn(self, member, container, msg=None):
        if isinstance(container, str) and len(container) > 400:
            if member not in container:
                self.fail(msg or "%r not found in the text" % (member,))
        else:
            super().assertIn(member, container, msg)


class AssemblyTests(TextbookTestCase):

    def test_markdown_sha256_pin(self):
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)

    def test_markdown_is_lf_only_utf8_with_one_final_newline(self):
        content = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", content)
        self.assertFalse(content.startswith(b"\xef\xbb\xbf"))
        content.decode("utf-8")
        self.assertTrue(content.endswith(b"\n"))
        self.assertFalse(content.endswith(b"\n\n"))

    def test_every_assembler_check_passes(self):
        result = assembly()
        self.assertEqual([(p.check, p.location, p.message) for p in result.problems], [])
        self.assertEqual(sorted(result.checks),
                         sorted(build_textbook.COMMON_CHECKS + build_textbook.STRICT_CHECKS))
        self.assertTrue(all(result.checks.values()), result.checks)
        self.assertEqual(result.missing, [])
        self.assertEqual([chapter.number for chapter in result.chapters], list(range(21)))
        self.assertEqual(sum(len(chapter.sections) for chapter in result.chapters),
                         SECTION_COUNT)

    def test_every_cross_reference_resolves(self):
        statuses = [reference.status for reference in assembly().references]
        self.assertGreater(statuses.count("resolved"), 3000)
        self.assertEqual(statuses.count("unresolved"), 0)
        self.assertEqual(statuses.count("pending"), 0)

    def test_markdown_is_the_assembler_output(self):
        self.assertEqual(MARKDOWN.read_bytes(), assembly().text.encode("utf-8"))

    def test_verify_output_command_passes(self):
        completed = subprocess.run(
            [sys.executable, str(REPOSITORY_ROOT / "scripts" / "build_textbook.py"),
             "--verify-output"],
            cwd=REPOSITORY_ROOT, capture_output=True, check=False, timeout=600)
        output = completed.stdout.decode("utf-8", "replace").replace("\r\n", "\n")
        self.assertEqual(completed.returncode, 0, output[-2000:])
        self.assertIn("check_outputUpToDate=true\n", output)
        self.assertIn("failed_check_count=0\n", output)
        self.assertIn("assembly_sha256=%s\n" % MARKDOWN_SHA256, output)
        self.assertTrue(output.rstrip("\n").endswith("textbook_assembly=OK"), output[-300:])


class TexAndPdfTests(TextbookTestCase):

    def test_tex_sha256_pin(self):
        self.assertEqual(sha256_file(TEX), TEX_SHA256)

    def test_tex_is_the_builder_output_with_developer_layout_and_sections_from_zero(self):
        latex = builder.convert(markdown_text(), strip_heading_numbers=True,
                                developer_layout=True, image_root=REPOSITORY_ROOT,
                                sections_from_zero=True)
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())

    def test_tex_numbers_the_first_chapter_zero(self):
        latex = TEX.read_text(encoding="utf-8")
        self.assertEqual(latex.count("\\setcounter{section}{-1}"), 1)
        self.assertIn("\\tableofcontents\n\\newpage\n\\setcounter{section}{-1}\n", latex)
        first = latex.index("\n\\section{")
        self.assertLess(latex.index("\\setcounter{section}{-1}"), first)
        self.assertTrue(latex.startswith("\n\\section{How to read this book}", first))
        self.assertEqual(latex.count("\n\\section{"), len(CHAPTER_HEADINGS))
        self.assertEqual(latex.count("\n\\subsection{"), SECTION_COUNT)
        self.assertNotIn("\\subsubsection{", latex)

    def test_registered_edition_matches_the_committed_pdf(self):
        registry = check_provenance_pdf.load_specifications(
            check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_TEXTBOOK.pdf")
        content = PDF.read_bytes()
        self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(content)))
        self.assertTrue(content.startswith(b"%PDF-"))
        self.assertTrue(content.rstrip().endswith(b"%%EOF"))

    def test_pdf_numbering_is_the_markdown_numbering(self):
        # hyperref names the destination of a section after its LaTeX number: section.N for
        # chapter N and subsection.N.M for section N.M.  Chapter 0 must be section.0, and the
        # set of numbers must be exactly the set of headings of the Markdown.
        content = PDF.read_bytes()
        chapters = {int(n) for n in re.findall(rb"\(section\.(-?\d+)\)", content)}
        subsections = {(int(a), int(b))
                       for a, b in re.findall(rb"\(subsection\.(-?\d+)\.(\d+)\)", content)}
        expected_sections = set()
        for line in markdown_text().split("\n"):
            match = re.match(r"^### (\d+)\.(\d+) ", line)
            if match:
                expected_sections.add((int(match.group(1)), int(match.group(2))))
        self.assertEqual(chapters, set(range(len(CHAPTER_HEADINGS))))
        self.assertEqual(len(expected_sections), SECTION_COUNT)
        self.assertEqual(subsections, expected_sections)
        self.assertIn((13, 2), subsections)
        self.assertIn("Section 13.2", markdown_text())

    def test_figures_exist_and_are_png(self):
        figures = builder.figure_paths(markdown_text())
        self.assertGreater(len(figures), 0)
        for figure in figures:
            with self.subTest(figure=figure):
                self.assertTrue(figure.startswith("artifacts/"), figure)
                self.assertTrue((REPOSITORY_ROOT / figure).read_bytes().startswith(
                    builder.PNG_SIGNATURE))


class ContentTests(TextbookTestCase):

    def test_title_block(self):
        lines = markdown_text().split("\n")
        self.assertEqual(lines[0], "# " + build_textbook.TITLE)
        self.assertEqual(lines[2], "## " + build_textbook.SUBTITLE)
        self.assertEqual(lines[4], "## Abstract")
        self.assertEqual(lines[6], build_textbook.ABSTRACT)
        self.assertEqual(sum(1 for line in lines if line.startswith("# ")), 1)

    def test_the_21_chapter_headings_in_order(self):
        headings = [line[3:] for line in markdown_text().split("\n") if line.startswith("## ")]
        self.assertEqual(headings[:2], [build_textbook.SUBTITLE, "Abstract"])
        self.assertEqual(headings[2:], list(CHAPTER_HEADINGS))

    def test_chapter_files_carry_the_headings(self):
        files = sorted(path for path in CHAPTERS.glob("*.md"))
        self.assertEqual(len(files), len(CHAPTER_HEADINGS))
        for number, (path, heading) in enumerate(zip(files, CHAPTER_HEADINGS)):
            with self.subTest(chapter=path.name):
                self.assertTrue(path.name.startswith("%02d-" % number))
                first = path.read_text(encoding="utf-8").split("\n", 1)[0]
                self.assertEqual(first, "## " + heading)

    def test_section_numbers_are_consecutive(self):
        current, expected, count = None, 1, 0
        for line in markdown_text().split("\n"):
            major = re.match(r"^## (\d+)\. ", line)
            minor = re.match(r"^### (\d+)\.(\d+) ", line)
            if major:
                current, expected = int(major.group(1)), 1
            elif minor:
                self.assertEqual((int(minor.group(1)), int(minor.group(2))),
                                 (current, expected), line)
                expected += 1
                count += 1
        self.assertEqual(count, SECTION_COUNT)

    def test_every_fenced_code_line_fits_and_has_no_tab(self):
        for block in fenced_blocks(markdown_text()):
            for line in block:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
                self.assertNotIn("\t", line)

    def test_no_placeholders_and_todo_only_in_the_notebook_quotation(self):
        text = markdown_text()
        self.assertIsNone(re.search(r"@@[A-Z0-9_]+@@", text))
        self.assertNotIn("FIXME", text)
        rest = text.replace("TODO: prove Universe(s) of masses ±M are created in pairs!", "")
        rest = rest.replace("the TODO of cell 17", "")
        self.assertNotIn("TODO", rest)


class HonestyStatementTests(TextbookTestCase):

    @classmethod
    def setUpClass(cls):
        cls.section = sections(markdown_text())

    def test_section_0_2_states_what_is_not_established(self):
        body = self.section["0.2"]
        self.assertTrue(body.startswith("### 0.2 The request and what can honestly be delivered"))
        for statement in SECTION_0_2_STATEMENTS:
            with self.subTest(statement=statement[:60]):
                self.assertIn(statement, body)

    def test_chapter_16_states_what_is_proved_and_what_is_not_derived(self):
        for number, statements in CHAPTER_16_STATEMENTS.items():
            for statement in statements:
                with self.subTest(section=number, statement=statement[:60]):
                    self.assertIn(statement, self.section[number])

    def test_chapter_17_states_that_the_theory_does_not_solve_the_problem(self):
        for number, statements in CHAPTER_17_STATEMENTS.items():
            for statement in statements:
                with self.subTest(section=number, statement=statement[:60]):
                    self.assertIn(statement, self.section[number])

    def test_chapter_17_gives_the_honest_answer_first(self):
        paragraphs = [p for p in self.section["17.1"].split("\n\n")[1:] if p.strip()]
        self.assertTrue(paragraphs[1].startswith(CHAPTER_17_STATEMENTS["17.1"][0]),
                        paragraphs[1][:200])

    def test_stage1_sentence_is_quoted_verbatim(self):
        self.assertIn(STAGE1_SENTENCE, STAGE1_DOCUMENT.read_text(encoding="utf-8"))
        self.assertIn(STAGE1_SENTENCE, self.section["0.2"])
        self.assertIn(STAGE1_SENTENCE, self.section["16.1"])

    def test_abstract_states_both_answers(self):
        for statement in ABSTRACT_STATEMENTS:
            with self.subTest(statement=statement[:60]):
                self.assertIn(statement, build_textbook.ABSTRACT)

    def test_stage4_cross_check_status_agrees_with_the_report(self):
        report = load_json(KOHN_SHAM_CHECK_REPORT)
        self.assertEqual((report["checkCount"], report["failedCheckCount"]), (63, 1))
        self.assertEqual(report["failed"], ["canonical_eigenvalues"])
        self.assertEqual(sum(1 for value in report["checks"].values() if value is False), 1)
        self.assertIn("its final cross-check against the independent reference solver has 63 "
                      "checks of which 1 failed (`artifacts/dirac16complex/kohn-sham/"
                      "python-check-report.json`, the check `canonical_eigenvalues`)",
                      self.section["16.1"])

    def test_stage5_report_counts_agree_with_the_reports(self):
        block = self.section["16.1"]
        for name, count in PAIR_CREATION_REPORTS.items():
            with self.subTest(report=name):
                checks = load_json(PAIR_CREATION / name)["checks"]
                self.assertEqual(len(checks), count)
                self.assertTrue(all(value is True for value in checks.values()))
                self.assertRegex(block, r"%s +%d of %d checks true" % (re.escape(name), count,
                                                                      count))


class OverclaimLintTests(TextbookTestCase):
    """No sentence of the book claims that the theory solves the matter-antimatter problem
    or that the big bang is proved to create universes in pairs."""

    def test_the_lint_inspects_the_relevant_sentences(self):
        counts = lint()["counts"]
        self.assertGreaterEqual(counts["pairs"], 10, counts)
        self.assertGreaterEqual(counts["solves"], 5, counts)
        self.assertGreaterEqual(counts["predicts"], 5, counts)

    def test_no_sentence_asserts_that_universes_are_created_in_pairs(self):
        self.assertEqual(lint()["offending"]["pairs"], [])

    def test_no_sentence_asserts_a_proof_about_the_big_bang(self):
        self.assertEqual(lint()["offending"]["bigBangProof"], [])

    def test_no_sentence_asserts_that_the_theory_solves_the_matter_antimatter_problem(self):
        self.assertEqual(lint()["offending"]["solves"], [])

    def test_no_sentence_asserts_a_prediction_of_the_asymmetry(self):
        self.assertEqual(lint()["offending"]["predicts"], [])

    def test_no_affirmative_forbidden_phrase_outside_quotations(self):
        # A phrase of FORBIDDEN_PHRASES may occur only after a negation of the same sentence,
        # as in "**Not claimed**: ...; that this theory explains the matter-antimatter
        # asymmetry" or "nothing computed here predicts the observed amount of dark matter".
        found, offending = affirmative_forbidden_phrases(markdown_text())
        self.assertEqual(offending, [])
        self.assertLess(found, 10)

    def test_the_lint_flags_planted_overclaims_and_passes_their_negations(self):
        planted = (
            "This theory solves the matter–antimatter problem.",
            "The big bang creates universes in pairs.",
            "Universes of masses $\\pm M$ are created in pairs at $x_4=0$.",
            "Theorem T1 proves that the big bang produces a pair of universes.",
            "The pair of universes explains the observed baryon asymmetry.",
            "The theory predicts the observed baryon-to-photon ratio.",
        )
        controls = (
            "This theory does not solve the matter–antimatter problem.",
            "Nothing in the repository shows that universes are created in pairs.",
            "Whether the big bang creates universes in pairs is an open question.",
            "The notebook states the hypothesis that universes are created in pairs.",
            "The scenario does not predict the observed baryon asymmetry.",
            "The author asks that this theory solve the matter–antimatter mysteries.",
            "The request reads \"this theory solves matter anti-matter mysteries\".",
            "Does the big bang create universes in pairs?",
        )
        text = "## 0. Planted\n\n" + "\n\n".join(planted + controls) + "\n"
        result = lint_text(text)
        flagged = [sentence for sentences in result["offending"].values()
                   for sentence in sentences]
        _, phrases = affirmative_forbidden_phrases(text)
        flagged += [sentence for _, sentence in phrases]
        self.assertEqual(sorted(set(flagged)), sorted(planted))
        self.assertEqual(sorted(set(sentence for _, sentence in phrases)),
                         sorted([planted[0], planted[3], planted[5]]))

    def test_status_word_exercises_classify_pair_creation_as_hypothesis_or_open(self):
        classified = lint()["classified"]
        self.assertGreaterEqual(len(classified), 1)
        answers = {}
        for block in prose_blocks(markdown_text()):
            match = re.match(r"^(?:\*\*)?Answer (\d+\.\d+)\.(?:\*\*)? ", block)
            if match:
                answers[match.group(1)] = block
        for number, letter in classified:
            with self.subTest(exercise=number, item=letter):
                self.assertRegex(answers[number], r"\(%s\) (?:HYPOTHESIS|OPEN)\b" % letter)


if __name__ == "__main__":
    unittest.main()
