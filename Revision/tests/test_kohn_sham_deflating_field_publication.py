#!/usr/bin/env python3
"""Publication test for Revision/docs/KOHN_SHAM_DEFLATING_FIELD.{md,tex,pdf}.

The document records the Kohn-Sham model of dirac16complex in the author's primordial field with the
exponentially deflating extra times x5, x6, x7, in the corrected metric of 2026-10-16 (version 2,
Revision/SPEC.md section 1: g = diag(e^(-2 a4) b4 cot^2 z, e^(2 a4) (x3), -1, -e^(-2 a4) b4 (sin^2 z)^(1/6) (x3)),
z = 6 H x0 real) (Revision/SPEC.md sections 7 and 10, deliverable 4): the block reduction, the instantaneous ground
and first excited states along the PRESCRIBED history a4 = A H x4, b4 = b4(0) e^((4/3) A H x4), the Mermin
thermodynamics, the adiabaticity and the Fermi-level crossings, the energy-momentum tensor profiles, the
rescaling partners, the source conditions (the recorded states are NOT admissible sources of the a4 and b4
equations), the pointer to T3 and what is not done.  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_kohn_sham_deflating_field_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md (same options as the
    build command above), both files are UTF-8 with LF line endings, and their sha256 are pinned;
  * the PDF is registered in the Revision registry Revision/pdf-specifications.json (edition
    kohn-sham-deflating-field: path, page count and sha256 of the committed PDF) and NOT in the registry
    of the earlier stages; the PDF is structurally sound;
  * title, subtitle and section headings; the last section is "What is proved, computed, assumed and
    not established"; the key statements are present, the statements of the withdrawn metrics and
    overclaims are absent;
  * every check name the document cites exists in a Revision report with the verdict PASS, and every
    check of the Kohn-Sham reports and of the source-conditions report is listed;
  * the report-count table and every "(X of Y PASS)" statement equal the counts of the reports;
  * every table of results is re-generated here from the Kohn-Sham results files and must occur
    verbatim; every further number quoted in the text is found in its report, results file or README;
  * OPTIONAL (only when REVISION_PDF_REBUILD=1; needs pdflatex, about 20 s): the PDF is rebuilt in
    verify mode and must match the registry.

After an intended edit of the document: rebuild in verify mode until warning-free, register it
(--register), and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

DOCS = REVISION / "docs"
MARKDOWN = DOCS / "KOHN_SHAM_DEFLATING_FIELD.md"
TEX = DOCS / "KOHN_SHAM_DEFLATING_FIELD.tex"
PDF = DOCS / "KOHN_SHAM_DEFLATING_FIELD.pdf"
EDITION = "kohn-sham-deflating-field"
REGISTRY = REVISION / "pdf-specifications.json"
OLD_REGISTRY = ROOT / "provenance" / "pdf-specifications.json"
REBUILD = os.environ.get("REVISION_PDF_REBUILD") == "1"

MARKDOWN_SHA256 = "e39c47efa044aaf41e2a1d45f22db38e5c95770a51738f3515acd7f0a955764d"
TEX_SHA256 = "e52ff4bdca350807716852565d9132980fd2d862fbdb980811e59e0334f223e8"

KS = REVISION / "kohn_sham"
RESULTS = KS / "results"
REPORTS = KS / "reports"
KS_THEORY = KS / "ks-theory.json"
THEORY_WOLFRAM = REPORTS / "ks-theory-wolfram.json"
THEORY_PYTHON = REPORTS / "ks-theory-python.json"
RUST_SOLVER = REPORTS / "ks-rust-solver.json"
DETERMINISM = REPORTS / "ks-rust-determinism.json"
MERMIN_ROOTS = REPORTS / "ks-rust-mermin-roots.json"
REFERENCE = REPORTS / "ks-reference.json"
CROSSCHECK = REPORTS / "ks-crosscheck.json"
SOURCE_CONDITIONS = REVISION / "field_equations_a4" / "reports" / "ks-source-conditions.json"
SOURCE_A4 = REVISION / "field_equations_a4" / "ks_source" / "reports" / "ks-source-a4.json"
TIP = KS / "tip_convergence"

# The reports of the count table (section 13.1), in the order of the table.
COUNTED_REPORTS = (
    "Revision/kohn_sham/reports/ks-theory-wolfram.json",
    "Revision/kohn_sham/reports/ks-theory-python.json",
    "Revision/kohn_sham/reports/ks-rust-solver.json",
    "Revision/kohn_sham/reports/ks-rust-determinism.json",
    "Revision/kohn_sham/reports/ks-rust-mermin-roots.json",
    "Revision/kohn_sham/reports/ks-reference.json",
    "Revision/kohn_sham/reports/ks-crosscheck.json",
    "Revision/field_equations_a4/reports/ks-source-conditions.json",
    "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "Revision/field_equations_a4/reports/python-a4-report.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
    "Revision/pairing/kohn_sham/reports/python-t3.json",
    "Revision/kohn_sham/tip_convergence/tip-convergence.json",
)
# Reports whose every check the document lists.
COMPLETELY_LISTED = (
    THEORY_WOLFRAM, THEORY_PYTHON, RUST_SOLVER, DETERMINISM, MERMIN_ROOTS, REFERENCE, CROSSCHECK,
    SOURCE_CONDITIONS, SOURCE_A4,
)
# Every report whose check names the document may cite.
CITABLE_REPORT_GLOBS = (
    "kohn_sham/reports/*.json",
    "field_equations_a4/reports/*.json",
    "field_equations_a4/ks_source/reports/*.json",
    "pairing/kohn_sham/reports/*.json",
    "kohn_sham/tip_convergence/*.json",
)
# "(X of Y PASS)" statements of the text: report path -> the phrase that names it.
PASS_STATEMENTS = (
    ("Revision/kohn_sham/reports/ks-theory-wolfram.json", "`Revision/kohn_sham/reports/ks-theory-wolfram.json` ({p} of {t} PASS)"),
    ("Revision/kohn_sham/reports/ks-theory-python.json", "`Revision/kohn_sham/reports/ks-theory-python.json` ({p} of {t} PASS)"),
    ("Revision/field_equations_a4/reports/ks-source-conditions.json", "`Revision/field_equations_a4/reports/ks-source-conditions.json` ({p} of {t} PASS)"),
    ("Revision/field_equations_a4/ks_source/reports/ks-source-a4.json", "`Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` ({p} of {t} PASS)"),
    ("Revision/pairing/kohn_sham/reports/wolfram-t3.json", "`Revision/pairing/kohn_sham/reports/wolfram-t3.json` ({p} of {t} PASS)"),
    ("Revision/pairing/kohn_sham/reports/python-t3.json", "`Revision/pairing/kohn_sham/reports/python-t3.json` ({p} of {t} PASS)"),
    ("Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json", "`Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` ({p} of {t} PASS)"),
    ("Revision/pairing/kohn_sham/reports/python-t3-completion.json", "`Revision/pairing/kohn_sham/reports/python-t3-completion.json` ({p} of {t} PASS)"),
    ("Revision/dark_sector/dirac16complex/reports/ks-history-run.json", "`Revision/dark_sector/dirac16complex/reports/ks-history-run.json`: {p} of {t} PASS"),
    ("Revision/kohn_sham/reports/ks-crosscheck.json", "{p} of {t} checks PASS over"),
    ("Revision/kohn_sham/reports/ks-crosscheck.json", "within the stated uncertainty ({p} of {t} checks, "),
    ("Revision/kohn_sham/reports/ks-rust-determinism.json", "The Rust determinism report ({p} of {t} PASS)"),
    ("Revision/kohn_sham/tip_convergence/tip-convergence.json", "`Revision/kohn_sham/tip_convergence/tip-convergence.json`, {p} of {t} checks PASS"),
)

TITLE = "Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times"
SUBTITLE_START = "The block reduction, the instantaneous ground and first excited states along the prescribed history"
SECTIONS = (
    "## Abstract",
    "## 1. The task and the answer",
    "## 2. Setting: the author's field, the good sector and the hidden coordinate",
    "### 2.1 The corrected metric in the Kohn-Sham record",
    "## 3. The exact block reduction",
    "## 4. The functional: Hartree, exact uniform-gas exchange, Mermin",
    "## 5. Boundary conditions, filling convention, numerics and parameters",
    "## 6. Instantaneous ground and first excited states along the prescribed history",
    "## 7. Adiabaticity and Fermi-level crossings",
    "## 8. Mermin thermodynamics",
    "## 9. Energy-momentum tensor profiles",
    "## 10. The rescaling partners",
    "## 11. The recorded states are not admissible sources of the $a_4$ and $b_4$ equations",
    "## 12. The Kohn-Sham-level pairing T3",
    "## 13. Verification records",
    "## 14. Reproduction",
    "## 15. What is proved, computed, assumed and not established",
)
KEY_STATEMENTS = (
    "in the corrected metric of 2026-10-16 (version 2): $g = \\mathrm{diag}\\big(e^{-2a_4}b_4\\cot^2 z,\\ e^{2a_4}\\,(\\times3),\\ -1,\\ "
    "-e^{-2a_4}b_4(\\sin^2 z)^{1/6}\\,(\\times3)\\big)$, $z = 6Hx_0$ real",
    "the three extra times, which DEFLATE exponentially, with the scale factor $e^{-a_4}b_4^{1/2}(\\sin^2 z)^{1/12}$ and $a_4$ "
    "increasing (they are never treated as static)",
    "the hidden direction has the scale factor $e^{-a_4}b_4^{1/2}|\\cot z|$ and shrinks together with them",
    "\\Psi = e^{ik\\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\\chi(y,x_4)",
    "The factor $e^{-(3/2)Hy}$ removes the term $\\tfrac32(H/f)\\gamma^0$ and the factor $e^{a_4/2}b_4^{-1}$ the term "
    "$(b_4'/b_4 - \\tfrac12a_4')\\gamma^4$; without either the term survives.",
    "h_j = j\\big[-\\tfrac{i}{f}\\sigma_1\\,\\tfrac{d}{dy} + M_{\\mathrm{eff}}(y)\\sigma_2 + \\kappa k\\sigma_3\\big] + v_v(y) ,",
    "\\kappa(x_4) = e^{-a_4(x_4)},\\qquad f(x_4) = e^{-a_4}b_4^{1/2} ,",
    "M_{\\mathrm{eff}}(y) = m + \\tfrac{15}{16}\\lambda S(y) ,\\qquad v_v(y) = -\\tfrac{\\lambda}{16}n(y) ,",
    "e_x = -\\tfrac{\\lambda}{32}\\big(n^2 + S^2\\big)",
    "$\\mathrm{Vol}_7(a_{4,0}) = \\ell^3v_t\\,e^{(2\\beta - 1)a_{4,0}} = \\ell^3v_te^{(5/3)a_{4,0}}$",
    "the effective coupling falls like $e^{-(5/3)a_{4,0}}$",
    "**Fold (both fold conditions filled, ASSUMED).**",
    "That both are filled is ASSUMED (the record's convention); there is no mirror copy.",
    "The construction of the withdrawn metric, a Z2 orbifold at the patch end whose mirror copy carried $-m$, does not "
    "exist in the corrected metric.",
    "**Tip (chosen).**",
    "With $\\kappa$ independent of $y$ nothing suppresses an orbital toward the tip",
    "**Filling (CONVENTION, justification OPEN).**",
    "The even $j = +1$ fold band is $\\varepsilon = \\kappa k$ EXACTLY for every $k$, with the orbital $(e^{fMy}, 0)$",
    "The free states of the matrix are exact fold-band gases",
    "so the free states have $p_0 = p_t = 0$ (the table shows rounding values) and $\\int p_3 = E_{KS}/3$",
    "dE/da_4 = -3P_3 + P_t + \\tfrac13P_0",
    "PRESCRIBED, not solved for",
    "because the hidden direction shrinks, $Q_{\\max}$ is not zero even for $N = 8$ at $\\lambda = 0$",
    "the instantaneous ground state is not the adiabatically reached state",
    "labelled in its report as NOT a proof of T3",
    "T3 does not establish a creation process, a rate or an amplitude.",
    "1. The time-dependent (non-adiabatic) Kohn-Sham problem (TDDFT) is OPEN",
    "2. Correlation: the functional is Hartree plus exchange only",
    "3. Back-reaction: the Kohn-Sham states are a test field on a prescribed background",
    "1. Both fold conditions filled at the fold $z = \\pi/2$, where the two halves of a cell meet (ASSUMED); the metric is "
    "degenerate there and no junction condition is derived.",
    "Discrepancy recorded, not hidden",
    "the Kohn-Sham gas of this record is a test field on the prescribed background $a_4 = AHx_4$, "
    "$b_4 = b_4(0)e^{(4/3)AHx_4}$ without back-reaction",
    "These are statements of that approximation, not of the field equations.",
)
# Statements of the withdrawn metrics (2026-10-14 and version 1 of 2026-10-16) that must not be left.
STALE = (
    "W^{-3}", "b_4^{-3/4}", "$b_4$ does not enter $h_j$", "\\sin^{1/6}z", "\\sin^{1/3}", "e^{6Hy}", "e^{-H|y|}",
    "Z2 brane", "Z2 image", "brane zero mode", "brane parit", "mirror warp", "**Brane (ASSUMED).**", "kappa(-L)",
    "e^{(6H - 2m)|y|}", "N = 136", "N = 688", "N = 696", "N136", "N688", "e^{2a_{4,0}}$", "162731",
    "the $a_4'$ pieces of the three inflating directions",
)
FORBIDDEN = (
    r"\b(?:TDDFT|time-dependent (?:Kohn-Sham )?problem) (?:is|was|has been) (?:solved|computed|proved|proven)",
    r"\bback-reaction (?:is|was|has been) (?:included|computed|solved|derived)",
    r"\bthe Z2 (?:brane|mirror|orbifold) (?:is|has been|was) (?:derived|proved|proven)",
    r"\bthe Kohn-Sham (?:gas|source|states?) (?:drives?|selects?|starts?) (?:the )?(?:exponential )?deflation",
    r"\b(?:the|both) fold conditions? (?:is|are|has been|have been|was|were) (?:derived|proved|proven)",
)
FILE_SUFFIXES = (".json", ".py", ".wls", ".wl", ".md", ".tex", ".pdf", ".rs", ".csv", ".toml")
SLICES = ("a00", "a05", "a10", "a15", "a20")
NS = (8, 592, 2352)
N_MID = 592


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def code_spans(text: str) -> list[str]:
    """Inline code spans outside fenced code blocks."""
    spans = []
    in_code = False
    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            spans.extend(re.findall(r"`([^`]+)`", line))
    return spans


def cited_check_names(text: str) -> list[str]:
    names = []
    for span in code_spans(text):
        if span.endswith(FILE_SUFFIXES) or "/" in span:
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*", span):
            names.append(span)
    return names


def report_checks() -> dict[str, list[str]]:
    """Check name -> list of verdicts (upper case) over every citable Revision report."""
    verdicts: dict[str, list[str]] = {}
    for pattern in CITABLE_REPORT_GLOBS:
        for path in sorted(REVISION.glob(pattern)):
            data = load_json(path)
            if not isinstance(data, dict):
                continue
            for check in data.get("checks", []):
                verdicts.setdefault(check["name"], []).append(str(check["verdict"]).upper())
    return verdicts


def count_report(path: Path) -> tuple[int, int, int]:
    checks = load_json(path)["checks"]
    passed = sum(1 for check in checks if str(check["verdict"]).upper() == "PASS")
    failed = sum(1 for check in checks if str(check["verdict"]).upper() == "FAIL")
    return len(checks), passed, failed


def check_detail(path: Path, name: str) -> str:
    for check in load_json(path)["checks"]:
        if check["name"] == name:
            return check["detail"]
    raise KeyError(f"{name} not in {path}")


def csv_rows(relative: str) -> list[dict]:
    with open(RESULTS / relative, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_by_id(relative: str) -> dict:
    return {row["id"]: row for row in csv_rows(relative)}


def g7(value) -> str:
    return format(float(value), ".7g")


def g4(value) -> str:
    return format(float(value), ".4g")


def g3(value) -> str:
    return format(float(value), ".3g")


class MarkdownAndTex(unittest.TestCase):
    def test_tex_is_builder_output(self):
        expected = builder.convert(
            markdown_text(),
            strip_heading_numbers=True,
            developer_layout=True,
            image_root=ROOT,
        )
        self.assertEqual(TEX.read_text(encoding="utf-8"), expected)

    def test_utf8_lf_and_pinned_sha256(self):
        for path in (MARKDOWN, TEX):
            data = path.read_bytes()
            data.decode("utf-8")
            self.assertNotIn(b"\r", data, path.name)
            self.assertNotIn(b"\t", data, path.name)
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)
        self.assertEqual(sha256_file(TEX), TEX_SHA256)


class RegisteredPdf(unittest.TestCase):
    def test_registered_in_the_revision_registry(self):
        registry = check_provenance_pdf.load_specifications(REGISTRY)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        pdf_bytes = PDF.read_bytes()
        self.assertEqual(entry["path"], "Revision/docs/KOHN_SHAM_DEFLATING_FIELD.pdf")
        self.assertEqual(entry["sha256"], hashlib.sha256(pdf_bytes).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(pdf_bytes)))

    def test_not_in_the_registry_of_the_earlier_stages(self):
        if OLD_REGISTRY.exists():
            self.assertNotIn(EDITION, json.loads(OLD_REGISTRY.read_text(encoding="utf-8")))

    def test_pdf_structure(self):
        pdf_bytes = PDF.read_bytes()
        self.assertTrue(pdf_bytes.startswith(b"%PDF-"))
        self.assertTrue(pdf_bytes.rstrip().endswith(b"%%EOF"))
        self.assertEqual(check_dissertation_pdf.parse_media_boxes(pdf_bytes), [(0.0, 0.0, 612.0, 792.0)])

    @unittest.skipUnless(REBUILD, "set REVISION_PDF_REBUILD=1 to rebuild the PDF in verify mode")
    def test_rebuild_in_verify_mode(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_provenance_pdf.py"),
             str(MARKDOWN.relative_to(ROOT)), "--developer-layout",
             "--specifications", str(REGISTRY.relative_to(ROOT))],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=1800)
        output = completed.stdout.decode("utf-8", "replace")
        self.assertEqual(completed.returncode, 0, output[-3000:])
        self.assertIn("check_logWarningFree=true", output)
        self.assertIn("provenance_pdf=OK", output)


class Content(unittest.TestCase):
    def setUp(self):
        self.text = markdown_text()

    def test_title_subtitle_sections(self):
        lines = self.text.split("\n")
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertTrue(lines[2].startswith("## " + SUBTITLE_START))
        positions = []
        for heading in SECTIONS:
            self.assertIn("\n" + heading + "\n", self.text, heading)
            positions.append(self.text.index("\n" + heading + "\n"))
        self.assertEqual(positions, sorted(positions))
        level2 = [line for line in lines if line.startswith("## ")]
        self.assertEqual(level2[-1], "## 15. What is proved, computed, assumed and not established")
        tex = TEX.read_text(encoding="utf-8")
        self.assertIn("\\section{What is proved, computed, assumed and not established}", tex)

    def test_key_statements(self):
        for statement in KEY_STATEMENTS:
            self.assertIn(statement, self.text, statement)

    def test_no_statement_of_the_withdrawn_metrics(self):
        for marker in STALE:
            self.assertNotIn(marker, self.text, marker)

    def test_author_request_quoted_from_the_readme(self):
        # the quotation of the README is wrapped over lines that start with "> "
        readme = re.sub(r"\n>[ ]?", " ", (REVISION / "README.md").read_text(encoding="utf-8"))
        for piece in ("plan and employ a DFT-motivated approximation similar to the one that you already created",
                      "with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT ground "
                      "and first-excited-state computation"):
            self.assertIn(piece, readme)
            self.assertIn(piece, self.text)

    def test_no_overclaims(self):
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)
        for word in ("ASSUMED", "PRESCRIBED", "OPEN", "CONVENTION"):
            self.assertIn(word, self.text, word)

    def test_negative_controls(self):
        """The content checks are not vacuous: tampered statements are detected."""
        tampered = (
            "The time-dependent problem is solved by the solver.",
            "Back-reaction is included through the a4 equations.",
            "The Z2 orbifold is derived from the field equations.",
            "The Kohn-Sham gas drives the exponential deflation.",
            "Both fold conditions are derived from the field equations.",
        )
        self.assertEqual(len(tampered), len(FORBIDDEN))
        for pattern, sentence in zip(FORBIDDEN, tampered):
            self.assertIsNotNone(re.search(pattern, sentence, re.IGNORECASE), pattern)
        self.assertNotIn("ground_scf_converge", report_checks())
        total, passed, failed = count_report(CROSSCHECK)
        wrong_row = f"| `Revision/kohn_sham/reports/ks-crosscheck.json` | {total + 1} | {passed} | {failed} |"
        self.assertNotIn(wrong_row, self.text)
        ground = csv_by_id("ground/summary.csv")
        wrong = f"| 0 | 0 | {g7(float(ground[f'N{N_MID}_lam0_a00']['E_KS']) * (1 + 1e-6))} |"
        self.assertNotIn(wrong, self.text)
        # a stale statement of the withdrawn metric inserted into a copy is detected
        copy = self.text + "\nthe ansatz with $W^{-3}$\n"
        self.assertTrue(any(marker in copy for marker in STALE))

    def test_no_material_of_the_earlier_stages(self):
        for marker in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            self.assertNotIn(marker, self.text, marker)

    def test_cited_checks_exist_and_pass(self):
        verdicts = report_checks()
        cited = cited_check_names(self.text)
        self.assertGreater(len(cited), 250)
        for name in cited:
            self.assertIn(name, verdicts, name)
            self.assertTrue(all(v == "PASS" for v in verdicts[name]), name)

    def test_every_check_of_the_listed_reports_is_cited(self):
        cited = set(cited_check_names(self.text))
        for path in COMPLETELY_LISTED:
            for check in load_json(path)["checks"]:
                self.assertIn(check["name"], cited, f"{check['name']} of {path.name}")

    def test_report_count_table(self):
        for relative in COUNTED_REPORTS:
            total, passed, failed = count_report(ROOT / relative)
            row = f"| `{relative}` | {total} | {passed} | {failed} |"
            self.assertIn(row, self.text, row)
            self.assertEqual(failed, 0, relative)
            self.assertEqual(passed, total, relative)

    def test_pass_statements(self):
        for relative, phrase in PASS_STATEMENTS:
            total, passed, failed = count_report(ROOT / relative)
            self.assertEqual((passed, failed), (total, 0), relative)
            self.assertIn(phrase.format(p=passed, t=total), self.text, relative)


class Tables(unittest.TestCase):
    """Every table of results, re-generated from the results files, occurs verbatim."""

    def setUp(self):
        self.text = markdown_text()

    def assert_rows(self, rows):
        for row in rows:
            self.assertIn("\n" + row + "\n", self.text, row)

    def test_couplings(self):
        params = load_json(RESULTS / "parameters.json")
        self.assertEqual([v["N"] for v in params["couplingCalibration"]["values"]], [float(n) for n in NS])
        self.assert_rows(f"| {int(v['N'])} | {g7(v['strengthPerLambda'])} | {v['lambda1']} | {v['lambda2']} |"
                         for v in params["couplingCalibration"]["values"])

    def test_ground_and_excited_mid(self):
        ground, excited = csv_by_id("ground/summary.csv"), csv_by_id("excited/summary.csv")
        rows = []
        for tag in ("lam0", "lamp1", "lamm1", "lamp2", "lamm2"):
            for s in ("a00", "a10", "a20"):
                g, e = ground[f"N{N_MID}_{tag}_{s}"], excited[f"N{N_MID}_{tag}_{s}"]
                rows.append(f"| {g7(g['lambda'])} | {g7(g['a4'])} | {g7(g['E_KS'])} | {g7(g['KS_gap'])} | "
                            f"{g7(e['delta_SCF'])} |")
        self.assertEqual(len(rows), 15)
        self.assert_rows(rows)

    def test_gap_redshift(self):
        ground = csv_by_id("ground/summary.csv")
        self.assert_rows(f"| {n} | " + " | ".join(g7(ground[f'N{n}_lam0_{s}']['KS_gap']) for s in SLICES) + " |"
                         for n in NS)
        for n in NS:
            gaps = [float(ground[f"N{n}_lam0_{s}"]["KS_gap"]) for s in SLICES]
            self.assertEqual(gaps, sorted(gaps, reverse=True), n)
        # N = 8: the gap is the fold-band step kappa dk = 0.25 e^(-a4,0)
        for s, a in zip(SLICES, (0.0, 0.5, 1.0, 1.5, 2.0)):
            self.assertAlmostEqual(float(ground[f"N8_lam0_{s}"]["KS_gap"]), 0.25 * math.exp(-a), places=10)

    def test_adiabaticity(self):
        adia = csv_by_id("adiabatic/adiabaticity.csv")
        self.assert_rows(
            f"| {n} | {g7(a['a4'])} | {g7(a['Q_max'])} | {g7(a['Q_max_delta_eps'])} | {g7(a['dE_da4_emt'])} | "
            f"{g7(a['dE_da4_finite_difference'])} |"
            for n in (N_MID, 2352) for a in (adia[f"N{n}_lam0_{s}"] for s in SLICES))

    def test_crossing_demo(self):
        rows = csv_rows("adiabatic/crossing-demo.csv")
        self.assertEqual(len(rows), 5)
        self.assertEqual({r["N"] for r in rows}, {"2360"})
        self.assert_rows(
            f"| {g7(r['a4'])} | {r['occupied_set_equal_to_a4_0']} | {r['open_shell']} | {g7(r['E_aufbau'])} | "
            f"{g7(r['E_adiabatically_continued'])} | {g7(r['difference'])} |" for r in rows)

    def test_thermodynamics(self):
        thermo = csv_by_id("thermo/thermodynamics.csv")
        self.assert_rows(
            f"| {g7(r['a4'])} | {g7(r['T'])} | {g7(r['mu'])} | {g7(r['E'])} | {g7(r['entropy'])} | "
            f"{g7(r['Omega_direct'])} | {g3(r['sea_holes_over_N'])} |"
            for r in (thermo[f"N{N_MID}_lam0_{s}_{t}"] for s in ("a00", "a20") for t in ("T10", "T20", "T50")))

    def test_emt_integrals(self):
        emt = csv_by_id("ground/emt-integrals.csv")
        self.assert_rows(
            f"| {n} | {g7(r['a4'])} | {g7(r['int_rho'])} | {g7(r['int_p3'])} | {g7(r['int_p_t'])} | {g7(r['int_p0'])} |"
            for n in (N_MID, 2352) for r in (emt[f"N{n}_lam0_{s}"] for s in SLICES))
        # the free states are fold-band gases: int p3 = E_KS/3, int p0 and int p_t vanish to rounding
        for n in NS:
            for s in SLICES:
                r = emt[f"N{n}_lam0_{s}"]
                scale = max(abs(float(r["int_rho"])), 1e-300)
                self.assertLess(abs(float(r["int_p3"]) - float(r["int_rho"]) / 3) / scale, 1e-9, r["id"])
                self.assertLess(abs(float(r["int_p0"])) / scale, 1e-9, r["id"])
                self.assertLess(abs(float(r["int_p_t"])) / scale, 1e-9, r["id"])

    def test_rescaling(self):
        resc = csv_by_id("rescaling/rescaling.csv")
        self.assert_rows(
            f"| {g7(r['a4'])} | {g7(r['partner_dk'])} | {g7(r['partner_v_t'])} | {g7(r['partner_H'])} | "
            f"{g7(r['partner_L'])} | {g4(r['max_abs_delta_eps'])} | {g4(r['rel_delta_E'])} | {g7(r['partner_E_KS'])} |"
            for r in (resc[f"N{N_MID}_lamp1_{s}"] for s in SLICES[1:]))
        for s in SLICES[1:]:
            r = resc[f"N{N_MID}_lamp1_{s}"]
            a = float(r["a4"])
            self.assertAlmostEqual(float(r["partner_dk"]), 0.25 * math.exp(-a), places=12)
            self.assertAlmostEqual(float(r["partner_v_t"]), math.exp(-a), places=12)
            self.assertAlmostEqual(float(r["partner_H"]), math.exp(a / 3), places=12)
            self.assertAlmostEqual(float(r["partner_L"]), 3.0 * math.exp(-a / 3), places=12)
            self.assertEqual((r["same_label_set"], r["same_occupations"]), ("true", "true"))


class QuotedNumbers(unittest.TestCase):
    """Every further number of the text, found in its report, results file or README."""

    def setUp(self):
        self.text = markdown_text()

    def pair(self, source_text: str, in_source: str, in_document: str | None = None):
        self.assertIn(in_source, source_text, in_source)
        self.assertIn(in_source if in_document is None else in_document, self.text, in_document or in_source)

    def test_tip_convergence_numbers(self, text=None):
        """The numbers of the tip-cutoff study quoted in sections 5, 15.2-15.4 and the abstract, re-derived from
        Revision/kohn_sham/tip_convergence/ (tip-convergence.json and its two CSV files)."""
        text = self.text if text is None else text
        record = load_json(TIP / "tip-convergence.json")
        with (TIP / "tip-convergence-extrapolation.csv").open(encoding="utf-8", newline="") as handle:
            extra = {(r["protocol"], r["id"], r["quantity"]): r for r in csv.DictReader(handle)}
        with (TIP / "tip-convergence-table.csv").open(encoding="utf-8", newline="") as handle:
            table = {(r["id"], float(r["L"])): r for r in csv.DictReader(handle)
                     if r["protocol"] == "fixed" and r["status"] == "ok"
                     and int(r["G"]) == round(300 * float(r["L"]))}
        grid = record["Lvalues"]
        steps = {round(b - a, 12) for a, b in zip(grid, grid[1:])}
        self.assertEqual(len(steps), 1)
        checks = record["checks"]
        self.assertTrue(all(c["verdict"] == "PASS" for c in checks))
        self.assertEqual((record["summary"]["passed"], record["summary"]["total"]), (len(checks), len(checks)))
        comparisons = record["reference"]["comparisons"]
        self.assertTrue(comparisons and all(c["pass"] for c in comparisons))
        reference_l = sorted({c["L"] for c in comparisons} | {j["L"] for j in record["reference"]["jobs"]})
        self.assertEqual(len(reference_l), 2)
        expected = [f"$L = {grid[0]:g}$ to ${grid[-1]:g}$ in steps of ${steps.pop():g}$",
                    f"`Revision/kohn_sham/tip_convergence/tip-convergence.json`, {len(checks)} of {len(checks)} checks PASS",
                    f"the reference solver agrees at $L = {reference_l[0]:g}$ and ${reference_l[1]:g}$",
                    f"the reference at $L = {reference_l[0]:g}$ and ${reference_l[1]:g}$)",
                    f"The dependence on the tip cutoff $L$ from {grid[0]:g} to {grid[-1]:g} of"]
        # the free fold-band states do not depend on L (every free state except N = 2352 at a4,0 = 0)
        free = sorted({s for (s, length) in table if "lam0" in s and "_T" not in s and s != "N2352_lam0_a00"})
        self.assertEqual(len(free), 9)
        for s in free:
            for q in ("E_KS", "HOMO", "LUMO", "KS_gap"):
                values = [float(table[(s, length)][q]) for length in grid if (s, length) in table]
                self.assertEqual(len(values), len(grid), (s, q))
                self.assertLessEqual(max(values) - min(values), 1e-15 * max(max(abs(v) for v in values), 1.0), (s, q))
        # the fold values: rho(0; L) = rho(0; inf)/(1 - e^(-2 f m L)), f = e^(-a4,0/3), checked on the free N = 592 states
        for a4, pct in ((0.0, "0.25%"), (1.0, "1.38%"), (2.0, "4.81%")):
            f = math.exp(-a4 / 3)
            self.assertEqual(f"{100 * (1 / (1 - math.exp(-6 * f)) - 1):.2f}%", pct)
            sid = f"N592_lam0_a{int(10 * a4):02d}"
            ratio = float(table[(sid, 3.0)]["rho_brane"]) / float(table[(sid, 6.0)]["rho_brane"])
            exact = (1 - math.exp(-12 * f)) / (1 - math.exp(-6 * f))
            self.assertLess(abs(ratio / exact - 1), 1e-12, sid)
        expected.append("high by 0.25%, 1.38% and 4.81% at $a_{4,0} = 0, 1, 2$")
        # the bulk edge and N = 2352 at a4,0 = 0
        edge = record["k0Spectrum"]["bulkEdge_odd_l0_of_L"]
        expected.append(f"the bulk edge {edge[f'{3.0:.15e}']:.4f} that defines $N = 2352$ is an $L = 3$ value "
                        f"({edge[f'{6.0:.15e}']:.4f} at $L = 6$)")
        s = "N2352_lam0_a00"
        closed = min(length for (t, length), r in table.items() if t == s and float(r["KS_gap"]) == 0.0)
        expected.append(f"changes its occupied set from $L = {closed:g}$ on (its gap "
                        f"{float(table[(s, 3.0)]['KS_gap']):.5f} closes; $E_{{KS}} = {float(table[(s, 3.0)]['E_KS']):.3f}$ "
                        f"at $L = 3$ and ${float(table[(s, 6.0)]['E_KS']):.3f}$ at $L = 6$, not converged)")
        self.assertTrue(extra[("fixed", s, "E_KS")]["verdict"].startswith("NOT CONVERGED"))
        # the N = 8 interaction energies at L = 3 and at large L
        ratios = []
        for a4, digits in (("a00", 4), ("a10", 4), ("a20", 3)):
            plus, minus = extra[("fixed", f"N8_lamp1_{a4}", "E_KS")], extra[("fixed", f"N8_lamm1_{a4}", "E_KS")]
            self.assertEqual(float(plus["value_L3"]), -float(minus["value_L3"]))
            self.assertEqual(float(plus["extrapolated_Linf"]), -float(minus["extrapolated_Linf"]))
            self.assertTrue(plus["verdict"].startswith("converg"))
            v3, vinf = abs(float(plus["value_L3"])), abs(float(plus["extrapolated_Linf"]))

            def sci(v, d):
                mantissa, exponent = f"{v:.{d}e}".split("e")
                return rf"\mp {mantissa}\times10^{{{int(exponent)}}}"
            expected.append(f"${sci(v3, digits)}$ against ${sci(vinf, digits)}$")
            ratios.append(f"{v3 / vinf:.3f}")
        expected += [f"{ratios[0]}, {ratios[1]} and {ratios[2]} of the large-$L$ values",
                     f"the recorded $N = 8$ interaction energy is {ratios[0]}, {ratios[1]} and {ratios[2]} of its large-$L$ "
                     "value at $a_{4,0} = 0, 1, 2$"]
        # the interaction shifts at a4,0 = 2
        shifts = []
        for n in (592, 2352):
            for tag in ("lamp1", "lamm1"):
                e, e0 = extra[("fixed", f"N{n}_{tag}_a20", "E_KS")], extra[("fixed", f"N{n}_lam0_a20", "E_KS")]
                shifts.append((float(e["extrapolated_Linf"]) - float(e0["extrapolated_Linf"]))
                              / (float(e["value_L3"]) - float(e0["value_L3"])))
        expected.append(f"are {min(shifts):.1f} to {max(shifts):.1f} times larger at large $L$ than at $L = 3$")
        # the interacting states: converged, failing
        interacting = [r for (p, sid, q), r in extra.items() if p == "fixed" and q == "E_KS" and "lam0" not in sid]
        converged = [r for r in interacting if r["verdict"].startswith("converg")]
        failing = sorted((r["id"], float(r["first_failed_L"])) for r in interacting if r["first_failed_L"])
        self.assertEqual(failing, [("N2352_lamm1_a00", 4.5), ("N2352_lamp1_a00", 3.5)])
        self.assertEqual({r["id"] for r in interacting} - {r["id"] for r in converged}, {s for s, _ in failing})
        expected += [f"{len(converged)} of the {len(interacting)} interacting states studied converge",
                     "from $L = 3.5$ for $+\\lambda_1$ and from $L = 4.5$ for $-\\lambda_1$"]
        # the Mermin state whose limit is not established
        self.assertTrue(extra[("fixed", "N592_lam0_a20_T50", "E_KS")]["verdict"].startswith("NOT CONVERGED"))
        expected.append("nor for the Mermin state N592_lam0_a20_T50")
        # the recorded states
        states = record["analysis"]["fixed"]
        ground = [v for v in states.values() if not v["T"]]
        thermal = sorted((v["N"], v["lambda_tag"], v["a4"], v["T"]) for v in states.values() if v["T"])
        self.assertEqual({v["N"] for v in ground}, {8, 592, 2352})
        self.assertEqual(thermal, [(592, "lam0", 2.0, 0.05), (592, "lamp1", 1.0, 0.02)])
        expected.append(f"of {len(states)} recorded states, the {len(ground)} ground states with "
                        "$N \\in \\{8, 592, 2352\\}$")
        # the calibration rule as a function of L
        lam = record["couplings"]["recalibrated_lambda1_of_L"]
        at = lambda n, length: lam[str(n)][f"{length:.15e}"]  # noqa: E731
        self.assertEqual([at(n, 3.0) for n in (8, 592, 2352)], [157.7, 2.131, 0.5363])
        self.assertTrue(all(at(n, 6.0) < at(n, 3.0) / 100 for n in (8, 592, 2352)))
        mantissa, exponent = f"{at(2352, 6.0):.2e}".split("e")
        expected.append(f"$157.7$, $2.131$ and $0.5363$ at $L = 3$, ${at(8, 6.0):g}$, ${at(592, 6.0):g}$ and "
                        f"${mantissa}\\times10^{{{int(exponent)}}}$ at $L = 6$")
        for statement in expected:
            self.assertIn(statement, text, statement)

    def test_tip_convergence_numbers_detect_a_changed_value(self):
        # negative controls: one quoted number of the study changed in a copy of the text must be detected
        for old, new in (("1.2923", "1.2924"), ("4.81%", "4.80%"), ("2245.486", "2245.487"),
                         ("0.215 of the large", "0.216 of the large"), ("17 of the 19", "18 of the 19"),
                         ("from $L = 4.5$ for", "from $L = 5$ for"), ("$1.249$", "$1.25$"),
                         ("of 29 recorded states", "of 28 recorded states")):
            with self.subTest(old=old):
                self.assertIn(old, self.text)
                with self.assertRaises(AssertionError):
                    self.test_tip_convergence_numbers(self.text.replace(old, new))

    def test_theory_record(self):
        theory = load_json(KS_THEORY)
        potentials = theory["exchange"]["kohnShamPotentials"]
        self.assertEqual(potentials["Meff_coefficient_of_lambda_S"], "15/16")
        self.assertEqual(potentials["vv_coefficient_of_lambda_n"], "-1/16")
        self.assertEqual(theory["exchange"]["uniformGas"]["coefficient_n2"], "-1/32")
        self.assertEqual(theory["exchange"]["uniformGas"]["coefficient_S2"], "-1/32")
        self.assertEqual(theory["exchange"]["uniformGas"]["filledShellRatio"],
                         "E_x/E_H = -1/8 for one filled level at rest (n = S)")
        self.assertIn("$E_x/E_H = -1/8$", self.text)
        self.assertIn("PRESCRIBED BACKGROUND", theory["adiabaticity"]["history"])
        self.assertIn("filling both theta = 0 and theta = pi is ASSUMED", theory["boundaryConditions"]["fold"]["status"])
        self.assertIn("OPEN", theory["adiabaticity"]["caveat"])
        detail = check_detail(THEORY_WOLFRAM, "brane_band_slope")
        self.assertIn("c = E^(-a4,0) exactly", detail)
        self.assertIn("its slope is $c = e^{-a_{4,0}}$ for every $M$, $L$ and $f$", self.text)
        self.assertIn("0.606530659713 (a4,0 = 1/2", detail)
        self.pair(check_detail(RUST_SOLVER, "theory_input_coefficients"), "M_eff = m + 0.9375 lambda S",
                  "$M_{\\mathrm{eff}} = m + 0.9375\\lambda S$")
        self.pair(check_detail(RUST_SOLVER, "theory_input_coefficients"), "v_v = -0.0625 lambda n",
                  "$v_v = -0.0625\\lambda n$")
        self.assertIn("eps = kappa k exactly", check_detail(RUST_SOLVER, "free_rescaling_relation_and_band_monotone"))
        forms = check_detail(RUST_SOLVER, "theory_input_metric_forms")
        for piece in ("f = e^(-a4) b4^(1/2)", "kappa = e^(-a4) constant in y", "P = e^(-3Hy)/Vol_7",
                      "Vol_7 = ell^3 v_t e^((2 beta - 1) a4,0)", "p0' + 3H (p0 - p_t) = 0",
                      "dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0", "entries not matching: none"):
            self.assertIn(piece, forms, piece)

    def test_parameters(self):
        params = load_json(RESULTS / "parameters.json")
        physics, numerics = params["physics"], params["numerics"]
        self.assertEqual((physics["H"], physics["m"], physics["L_tipCutoff"], physics["dk"], physics["v_t"]),
                         (1.0, 1.0, 3.0, 0.25, 1.0))
        self.assertIn("$H = m = 1$, $L = 3$, $\\Delta k = 0.25$, $v_t = 1$", self.text)
        self.assertIn(f"$\\mathrm{{Vol}}_7(0) = {physics['Vol7AtA4Zero']!r}$", self.text)
        self.assertAlmostEqual(physics["historyBeta"], 4 / 3, places=14)
        self.assertEqual(physics["Vol7Rule"], "Vol_7(a4,0) = ell^3 v_t e^{(2 beta - 1) a4,0}")
        self.assertEqual(physics["hiddenScaleRule"], "f(a4,0) = e^{(beta/2 - 1) a4,0} (b4(0) = 1)")
        self.assertEqual(physics["kappaRule"], "kappa(a4,0) = e^{-a4,0}, constant in y")
        self.assertIn("$\\mathrm{Vol}_7(a_{4,0}) = \\mathrm{Vol}_7(0)\\,e^{(5/3)a_{4,0}}$", self.text)
        self.assertIn("$\\beta = 4/3$", self.text)
        self.assertEqual(physics["slicesA4"], [0.0, 0.5, 1.0, 1.5, 2.0])
        self.assertEqual(physics["temperatures"], [0.01, 0.02, 0.05])
        self.assertEqual((physics["tipTheta"], physics["historyA"]), (0.0, 1.0))
        self.assertIn("$a_{4,0} \\in \\{0, 0.5, 1, 1.5, 2\\}$", self.text)
        self.assertIn("$T \\in \\{0.01, 0.02, 0.05\\}$", self.text)
        self.assertEqual((numerics["rk4Steps"], numerics["rootTolerance"], numerics["scfTolerance"]),
                         (900, 1e-13, 1e-11))
        self.assertIn("RK4 on 900 steps, Pruefer counting and a root tolerance of 1e-13, Anderson-mixed SCF to 1e-11",
                      self.text)
        self.assertEqual(params["particleNumbers"]["values"], [float(n) for n in NS])
        self.assertIn("$N = 8, 592, 2352$", self.text)
        self.assertIn(f"the bulk edge {params['particleNumbers']['bulkEdge']!r}", self.text)
        self.assertIn("N = sum g f over both fold conditions", params["conventions"]["particleNumber"])
        self.assertIn("the solver uses sum g f = N", params["conventions"]["particleNumber"])

    def test_matrix_sizes(self):
        crosscheck = load_json(CROSSCHECK)
        comparisons = crosscheck["comparisons"]
        self.assertEqual(comparisons, 217571)
        self.assertEqual(crosscheck["matrix"], {"ground": 75, "thermal": 135, "exact_fock_variant": 60,
                                                "rescaling_partners": 60, "particle_hole_lists": 75,
                                                "crossing_demo_slices": 5})
        self.assertIn(f"{comparisons} comparisons", self.text)
        self.assertIn("75 ground states, 135 thermal states, 60 exact-Fock-variant states, 60 rescaling partners, "
                      "75 particle-hole lists and the 5 slices of the crossing demonstration", self.text)
        rule = crosscheck["tolerance_rule"]
        self.assertIn("3 (U_ref + U_Rust) + 1e-12 scale", rule)
        self.assertIn("(16/15) |canonical - refined|", rule)
        self.assertEqual(len(csv_rows("ground/summary.csv")), 75)
        self.assertEqual(len(csv_rows("thermo/thermodynamics.csv")), 135)
        self.assertEqual(len(csv_rows("exx/exact-fock-variant.csv")), 60)
        self.assertEqual(len(csv_rows("rescaling/rescaling.csv")), 60)
        self.assertTrue(all(r["open_shell"] == "false" for r in csv_rows("ground/summary.csv")))

    def test_adiabatic_numbers(self):
        rows = csv_rows("adiabatic/adiabaticity.csv")
        top = max(rows, key=lambda r: float(r["Q_max"]))
        self.assertEqual((top["id"], top["Q_max_pair"]), ("N2352_lamm1_a00", "26:+1:even:0 -> 26:+1:even:1"))
        self.assertIn(f"is {g7(top['Q_max'])} (state N2352_lamm1_a00, pair `26:+1:even:0 -> 26:+1:even:1`", self.text)
        self.assertIn(f"$Q_{{\\max}} \\leq {g7(top['Q_max'])}$", self.text)
        self.assertLess(float(top["Q_max"]), 0.2)
        self.assertIn("the largest values approach 0.2 for $N = 2352$ at $a_{4,0} = 0$", self.text)
        # N = 8: nonzero already at lambda = 0 (the hidden direction shrinks along the history)
        free8 = csv_by_id("adiabatic/adiabaticity.csv")["N8_lam0_a00"]
        self.assertGreater(float(free8["Q_max"]), 0.0)
        self.assertIn(f"(state N8_lam0_a00: {g7(free8['Q_max'])})", self.text)
        n8 = max((r for r in rows if r["N"] == "8"), key=lambda r: float(r["Q_max"]))
        self.assertEqual((n8["id"], n8["Q_max_pair"]), ("N8_lamp2_a00", "0:-1:even:0 -> 0:-1:even:1"))
        self.assertIn(f"$Q_{{\\max}} \\leq {g7(n8['Q_max'])}$ (state N8_lamp2_a00, pair "
                      "`0:-1:even:0 -> 0:-1:even:1`)", self.text)
        self.pair(check_detail(RUST_SOLVER, "adiabatic_hellmann_feynman"), "worst value 6.444e-11", "(worst 6.444e-11")
        self.assertIn("(1 - beta/2) T_j", check_detail(RUST_SOLVER, "adiabatic_hellmann_feynman"))
        history = load_json(RESULTS / "adiabatic" / "history.json")
        self.assertEqual(len(history["series"]), 15)
        self.assertTrue(all(series["fermiLevelCrossings"] == [] for series in history["series"]))
        self.assertTrue(all(r["occupied_set_changed"] == "false" for r in csv_rows("adiabatic/fermi-level-crossings.csv")))
        self.assertIn("every one of the 15 series", self.text)
        self.assertIn("N = 2360 (the smallest closed shell of the a4,0 = 0 aufbau that occupies a level off the even "
                      "j = +1 fold band)", check_detail(RUST_SOLVER, "adiabatic_crossing_flag_demonstration"))
        self.assertIn("$\\lambda = 0$ and $N = 2360$ (the smallest closed shell of the $a_{4,0} = 0$ aufbau that "
                      "occupies a level off the even $j = +1$ fold band", self.text)
        # the free fold-band gases: dE/da4 = -E_KS in both forms
        ground = csv_by_id("ground/summary.csv")
        for n in NS:
            for s in SLICES:
                r = csv_by_id("adiabatic/adiabaticity.csv")[f"N{n}_lam0_{s}"]
                e = float(ground[f"N{n}_lam0_{s}"]["E_KS"])
                for key in ("dE_da4_emt", "dE_da4_finite_difference"):
                    self.assertLess(abs(float(r[key]) + e), 1e-6 * max(abs(e), 1.0), (r["id"], key))

    def test_excited_and_thermo_numbers(self):
        self.pair(check_detail(RUST_SOLVER, "excited_delta_scf_free_equals_gap"), "15 cases; worst value 3.086e-13",
                  "worst difference 3.086e-13 over 15 cases")
        detail = check_detail(RUST_SOLVER, "thermo_sea_hole_diagnostic_computed")
        self.pair(detail, "27 of 135 states (largest 594.496 N)", "27 of 135 states")
        self.assertIn("the largest is 594.496 N", self.text)
        thermo = csv_rows("thermo/thermodynamics.csv")
        outside = [r for r in thermo if r["particle_only_convention_within_1pc"] == "false"]
        self.assertEqual(len(outside), 27)
        self.assertTrue(all(float(r["a4"]) >= 0.5 for r in outside))
        self.assertGreater(sum(1 for r in outside if r["N"] == "8"), len(outside) / 2)
        self.assertIn("most of them at $N = 8$ and all at $a_{4,0} \\geq 0.5$", self.text)
        self.assertIn(f"N{N_MID}_lam0_a20_T50", [r["id"] for r in outside])
        self.assertIn(f"(state N{N_MID}_lam0_a20_T50)", self.text)
        self.pair(check_detail(MERMIN_ROOTS, "root_precision_self_check"), "1.5e-38")

    def test_rescaling_and_t3_numbers(self):
        self.pair(check_detail(RUST_SOLVER, "rescaling_identity_between_slices"), "worst value 1.643e-13",
                  "The worst level difference is 1.643e-13")
        self.pair(check_detail(RUST_SOLVER, "rescaling_identity_energy_profiles"), "worst value 8.193e-13",
                  "the profiles 8.193e-13")
        detail = check_detail(RUST_SOLVER, "t3_block_map_solver_selftest")
        self.assertIn("NOT a proof of T3", detail)
        self.pair(detail, "(worst 3.62e-13, tolerance 1e-9)", "(worst 3.62e-13, tolerance 1e-9;")

    def test_determinism_and_refinement_numbers(self):
        self.pair(check_detail(DETERMINISM, "repeat_byte_identical"), "244 files", "all 244 result files")
        for name, value in (("refined_ground_energies", "1.728e-11"), ("refined_eigenvalues", "5.688e-10"),
                            ("refined_eigenvalues", "50420"), ("refined_profiles", "1.950e-10"),
                            ("refined_adiabatic_derivatives", "4.513e-08"),
                            ("refined_thermodynamics", "1.874e-10"), ("refined_heat_capacity", "3.853e-09")):
            self.pair(check_detail(DETERMINISM, name), value)
        description = load_json(KS / "checker" / "rust-refinement.json")["description"]
        self.assertIn("canonical: RK4 G = 900, root tolerance 1e-13, SCF tolerance 1e-11", description)
        self.assertIn("refined: G = 1800, root tolerance 1e-14, SCF tolerance 1e-14", description)
        model = (KS / "solver" / "src" / "model.rs").read_text(encoding="utf-8")
        self.assertIn("Numerics { g: 1800, root_tol: 1e-14, scf_tol: 1e-14, scf_max_iter: 1000,", model)
        self.assertIn("(900 to 1800 RK4 steps, root tolerance 1e-14, SCF tolerance 1e-14 with at most 1000 iterations)",
                      self.text)
        self.assertEqual(count_report(RUST_SOLVER)[0], 45)

    def test_reference_numbers(self):
        self.assertIn("(second order: 4", check_detail(REFERENCE, "free_convergence_order_two"))
        self.assertIn("G = 300, 600", check_detail(REFERENCE, "free_k0_analytic_spectra"))
        self.assertIn("G = 2400", check_detail(REFERENCE, "richardson_uncertainty_validated"))
        self.assertIn("three grids (300, 600, 1200)", self.text)
        self.assertIn("differences E_cont - E_aufbau: 0.0: 0, 0.5: 4.676353789",
                      check_detail(REFERENCE, "crossing_demo_reference"))

    def test_source_condition_numbers(self):
        detail = check_detail(SOURCE_CONDITIONS, "ks_profiles_depend_on_x0")
        self.pair(detail, ">= 0.456213", "\\geq 0.456213")
        self.assertIn("(70 with a nonzero energy-momentum tensor)", detail)
        self.assertIn("Every one of the 70 nonzero ground-state profiles depends on $x_0$", self.text)
        detail = check_detail(SOURCE_CONDITIONS, "ks_hidden_pressure_condition")
        self.assertIn("for exactly the 10 nonzero states with lambda = 0", detail)
        self.assertIn("fails (> 1e-06) for every one of the 60 states with lambda != 0 (smallest: 0.080929", detail)
        self.assertIn("for exactly the 10 nonzero states with $\\lambda = 0$", self.text)
        self.assertIn("fails for every one of the 60 states with $\\lambda \\neq 0$ "
                      "($\\max_y|p_0 - p_t|/\\max|T| \\geq 0.080929$", self.text)
        self.assertIn("C3 holds for every recorded state", check_detail(SOURCE_CONDITIONS, "ks_offdiagonal_condition"))
        detail = check_detail(SOURCE_CONDITIONS, "ks_history_is_a_prescribed_background")
        self.pair(detail, "kappa rho = 3.57407", "$\\kappa\\rho = 3.57407$ at $a_{4,0} = 0$")
        self.pair(detail, "kappa rho = -7.63383", "$-7.63383$ at $a_{4,0} = 2$")
        self.assertIn("5 states have an identically vanishing", check_detail(SOURCE_CONDITIONS, "ks_zero_source_states_listed"))
        self.assertIn("Five states have an identically vanishing tensor", self.text)
        conclusion = load_json(SOURCE_CONDITIONS)["conclusion"]
        self.assertIn("No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the corrected metric",
                      conclusion)
        a4 = load_json(SOURCE_A4)
        self.assertEqual(a4["summary"], {"checks": 19, "pass": 19, "fail": 0})
        for name, in_source, in_document in (
                ("B2_x0_conservation_on_every_profile", "1.21233e-05", "1.21233e-05"),
                ("B3_hidden_direction_mismatch", "mu1_rho in [0.147738, 0.738255]", "between 0.147738 and 0.738255"),
                ("C1_averaged_hidden_pressure_condition", ">= 0.00613418", "$\\geq 0.00613418$"),
                ("C3_record_history_not_sourced_by_the_gas", "rho_bar = 0.216249 at a4 = 0, 0.00104404 at a4 = 2",
                 "$\\bar\\rho = 0.216249$ and $0.00104404$"),
                ("C3_record_history_not_sourced_by_the_gas", "from 16.5276 to -7311.81", "from 16.5276 to $-7311.81$"),
                ("D2_author_weights_from_the_record_history",
                 "x4 = 0.428813 (a4 = 0.361572, b4 = 0.862627, a4'/H = 0.978369, u/H = -2.60176)",
                 "$x_4 = 0.428813$ ($a_4 = 0.361572$, $b_4 = 0.862627$, $a_4'/H = 0.978369$, $u/H = -2.60176$"),
                ("D4_outcomes", "a4_turns 24, regular 6, runaway 4, singular_second_order_system 4",
                 "$a_4$ turning 24 times, regular 6 times, runaway 4 times and singular 4 times"),
                ("D4_outcomes", "38 cases", "over 38 cases")):
            self.pair(check_detail(SOURCE_A4, name), in_source, in_document)
        conclusions = " ".join(a4["conclusions"])
        self.assertIn("No recorded Kohn-Sham state is an admissible source of the corrected metric", conclusions)
        self.assertIn("the history is a prescribed background without back-reaction", conclusions)

    def test_run_times_from_the_readmes(self):
        sources = (
            (KS / "theory" / "WOLFRAMSCRIPT_PROVENANCE.md", ("about 40 to 85 seconds", "about 75 to 165 seconds"),
             ("about 40 to 85 s", "about 75 to 165 s")),
            (KS / "solver" / "README.md",
             ("part 1/2 134.6 s, part 2/2 130.5 s, assembly 5.4 s", "Repeat in three parts: 76.7 s, 70.4 s, 85.7 s",
              "in four parts: 176.5 s, 186.1 s, 183.0 s, 163.8 s"),
             ("the Rust canonical matrix in two parts of 134.6 s and 130.5 s with an assembly of 5.4 s",
              "the repeat in three parts of 76.7 s, 70.4 s and 85.7 s",
              "the refined-tolerance run in four parts of 176.5 s, 186.1 s, 183.0 s and 163.8 s")),
            (KS / "reference" / "README.md",
             ("193.0, 175.4, 214.0, 179.8, 100.7 and 191.2 s", "136.8, 143.7, 133.7, 133.7, 134.2 and\n  139.8 s"),
             ("stage 1 193.0, 175.4, 214.0, 179.8, 100.7 and 191.2 s",
              "stage 2 136.8, 143.7, 133.7, 133.7, 134.2 and 139.8 s")),
            (KS / "checker" / "README.md", ("in 108.8 s", "87.6 s in total"),
             ("the refinement measurement 108.8 s", "the cross-checker itself 87.6 s")),
            (KS / "tip_convergence" / "README.md", ("966 s in all, 7 of 7 checks PASS",),
             ("the tip-cutoff study 966 s in ten parts",)),
            (REVISION / "field_equations_a4" / "ks_source" / "README.md",
             ("The script takes about 4.4 s and the tests about 20 s",),
             ("the Kohn-Sham source analysis about 4.4 s and its unit tests about 20 s",)),
            (REVISION / "field_equations_a4" / "README.md", ("Wolfram\n57 of 57 (20 s), sympy 69 of 69 (8 s)",),
             ("the $a_4$ verifiers 20 s (Wolfram) and 8 s (sympy)",)),
            (REVISION / "pairing" / "kohn_sham" / "wolfram" / "WOLFRAMSCRIPT_PROVENANCE.md",
             ("`verify_t3.wls` `9/9 checks passed` (5.8 s of wall time),\n  `check_t3.py` 12 of 12 (1.3 s)",),
             ("the T3 verifiers 5.8 s and 1.3 s",)),
        )
        for path, in_source, in_document in sources:
            text = path.read_text(encoding="utf-8")
            for value in in_source:
                self.assertIn(value, text, f"{value} in {path.name}")
            for value in in_document:
                self.assertIn(value, self.text, value)
        # section 13.4: the re-run of the canonical matrix in parts (the times of the solver README)
        self.assertIn("(`revision_ks_solver all --cache <scratch> --part i/3 --inner-threads 2`, then `--out "
                      "<scratch>/results --report <scratch>/report.json`; 76.7 s, 70.4 s, 85.7 s and 5.7 s)", self.text)
        self.assertIn("assembly 5.7 s", (KS / "solver" / "README.md").read_text(encoding="utf-8"))
        self.assertIn("(45 of 45 checks PASS)", self.text)
        self.assertEqual(count_report(RUST_SOLVER)[0], 45)


if __name__ == "__main__":
    unittest.main()
