#!/usr/bin/env python3
"""Publication test for Revision/docs/KOHN_SHAM_DEFLATING_FIELD.{md,tex,pdf}.

The document records the Kohn-Sham model of dirac16complex in the author's primordial field with the
exponentially deflating extra times x5, x6, x7 (Revision/SPEC.md sections 7 and 10, deliverable 4): the
block reduction, the instantaneous ground and first excited states along the PRESCRIBED history
a4 = A H x4, the Mermin thermodynamics, the adiabaticity and the Fermi-level crossings, the
energy-momentum tensor profiles, the rescaling partners, the source conditions (the recorded states are
NOT admissible sources of the a4 equations), the pointer to T3 and what is not done.  It is built and
registered with

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
    not established"; the key statements are present and overclaims are absent;
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

MARKDOWN_SHA256 = "ed25278e22dc3ae2b3df420f93a470141ebec9ea65d19f172751142c4a1b9088"
TEX_SHA256 = "fa48c464634b59ca75dc7113e15a72bbd39f4b2c9bbefab170fe232e7718da52"

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
)
# Reports whose every check the document lists.
COMPLETELY_LISTED = (
    THEORY_WOLFRAM, THEORY_PYTHON, RUST_SOLVER, DETERMINISM, MERMIN_ROOTS, REFERENCE, CROSSCHECK,
    SOURCE_CONDITIONS,
)
# Every report whose check names the document may cite.
CITABLE_REPORT_GLOBS = (
    "kohn_sham/reports/*.json",
    "field_equations_a4/reports/*.json",
    "field_equations_a4/ks_source/reports/*.json",
    "pairing/kohn_sham/reports/*.json",
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
    ("Revision/kohn_sham/reports/ks-crosscheck.json", "31 of 31 checks PASS over"),
)

TITLE = "Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times"
SUBTITLE_START = "The block reduction, the instantaneous ground and first excited states along the prescribed history"
SECTIONS = (
    "## Abstract",
    "## 1. The task and the answer",
    "## 2. Setting: the author's field, the good sector and the hidden coordinate",
    "## 3. The exact block reduction",
    "## 4. The functional: Hartree, exact uniform-gas exchange, Mermin",
    "## 5. Boundary conditions, filling convention, numerics and parameters",
    "## 6. Instantaneous ground and first excited states along the prescribed history",
    "## 7. Adiabaticity and Fermi-level crossings",
    "## 8. Mermin thermodynamics",
    "## 9. Energy-momentum tensor profiles",
    "## 10. The rescaling partners",
    "## 11. The recorded states are not admissible sources of the $a_4$ equations",
    "## 12. The Kohn-Sham-level pairing T3",
    "## 13. Verification records",
    "## 14. Reproduction",
    "## 15. What is proved, computed, assumed and not established",
)
KEY_STATEMENTS = (
    "the three extra times, which DEFLATE exponentially, with the scale factor $e^{-a_4}\\sin^{1/6}z$",
    "they are never treated as static",
    "the $a_4'$ pieces of the three inflating directions, $+\\frac32a_4'\\gamma^4$, and of the three deflating directions, $-\\frac32a_4'\\gamma^4$, cancel",
    "The factor $W^{-3}$ removes the term $3H\\gamma^8$",
    "M_{\\mathrm{eff}}(y) = m + \\tfrac{15}{16}\\lambda S(y) ,\\qquad v_v(y) = -\\tfrac{\\lambda}{16}n(y) ,",
    "e_x = -\\tfrac{\\lambda}{32}\\big(n^2 + S^2\\big)",
    "**Brane (ASSUMED).**",
    "**Tip (chosen).**",
    "**Filling (CONVENTION, justification OPEN).**",
    "PRESCRIBED, not solved for",
    "the deflation of the extra times is exactly what keeps it so",
    "the recorded states are not sources of the field equations for $a_4$; the history $a_4 = AHx_4$ is PRESCRIBED",
    "has no solution, and nothing about $a_4$ is derived from it",
    "These are statements of that approximation, not of the field equations.",
    "the Kohn-Sham gas of this record is a test field on the prescribed background $a_4 = AHx_4$ without back-reaction",
    "labelled in its report as NOT a proof of T3",
    "T3 does not establish a creation process, a rate or an amplitude.",
    "1. The time-dependent (non-adiabatic) Kohn-Sham problem (TDDFT) is OPEN",
    "2. Correlation: the functional is Hartree plus exchange only",
    "3. Back-reaction: the Kohn-Sham states are a test field on a prescribed background",
    "Discrepancy recorded, not hidden",
    "the instantaneous ground state is not the adiabatically reached state",
)
FORBIDDEN = (
    r"\b(?:TDDFT|time-dependent (?:Kohn-Sham )?problem) (?:is|was|has been) (?:solved|computed|proved|proven)",
    r"\bback-reaction (?:is|was|has been) (?:included|computed|solved|derived)",
    r"\bthe Z2 (?:brane|mirror) (?:is|has been|was) (?:derived|proved|proven)",
    r"\bthe Kohn-Sham (?:gas|source|states?) (?:drives?|selects?|starts?) (?:the )?(?:exponential )?deflation",
)
FILE_SUFFIXES = (".json", ".py", ".wls", ".wl", ".md", ".tex", ".pdf", ".rs", ".csv", ".toml")
SLICES = ("a00", "a05", "a10", "a15", "a20")


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
            "The Z2 brane is derived from the field equations.",
            "The Kohn-Sham gas drives the exponential deflation.",
        )
        self.assertEqual(len(tampered), len(FORBIDDEN))
        for pattern, sentence in zip(FORBIDDEN, tampered):
            self.assertIsNotNone(re.search(pattern, sentence, re.IGNORECASE), pattern)
        self.assertNotIn("ground_scf_converge", report_checks())
        total, passed, failed = count_report(CROSSCHECK)
        wrong_row = f"| `Revision/kohn_sham/reports/ks-crosscheck.json` | {total + 1} | {passed} | {failed} |"
        self.assertNotIn(wrong_row, self.text)
        ground = csv_by_id("ground/summary.csv")
        wrong = f"| 0 | 0 | {g7(float(ground['N136_lam0_a00']['E_KS']) * (1 + 1e-6))} |"
        self.assertNotIn(wrong, self.text)

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
        self.assertEqual([v["N"] for v in params["couplingCalibration"]["values"]], [8.0, 136.0, 688.0])
        self.assert_rows(f"| {int(v['N'])} | {g7(v['strengthPerLambda'])} | {v['lambda1']} | {v['lambda2']} |"
                         for v in params["couplingCalibration"]["values"])

    def test_ground_and_excited_136(self):
        ground, excited = csv_by_id("ground/summary.csv"), csv_by_id("excited/summary.csv")
        rows = []
        for tag in ("lam0", "lamp1", "lamm1", "lamp2", "lamm2"):
            for s in ("a00", "a10", "a20"):
                g, e = ground[f"N136_{tag}_{s}"], excited[f"N136_{tag}_{s}"]
                rows.append(f"| {g7(g['lambda'])} | {g7(g['a4'])} | {g7(g['E_KS'])} | {g7(g['KS_gap'])} | "
                            f"{g7(e['delta_SCF'])} |")
        self.assertEqual(len(rows), 15)
        self.assert_rows(rows)

    def test_gap_redshift(self):
        ground = csv_by_id("ground/summary.csv")
        self.assert_rows(f"| {n} | " + " | ".join(g7(ground[f'N{n}_lam0_{s}']['KS_gap']) for s in SLICES) + " |"
                         for n in (8, 136, 688))
        for n in (8, 136, 688):
            gaps = [float(ground[f"N{n}_lam0_{s}"]["KS_gap"]) for s in SLICES]
            self.assertEqual(gaps, sorted(gaps, reverse=True), n)

    def test_adiabaticity(self):
        adia = csv_by_id("adiabatic/adiabaticity.csv")
        self.assert_rows(
            f"| {n} | {g7(a['a4'])} | {g7(a['Q_max'])} | {g7(a['Q_max_delta_eps'])} | {g7(a['dE_da4_emt'])} | "
            f"{g7(a['dE_da4_finite_difference'])} |"
            for n in (136, 688) for a in (adia[f"N{n}_lam0_{s}"] for s in SLICES))

    def test_crossing_demo(self):
        rows = csv_rows("adiabatic/crossing-demo.csv")
        self.assertEqual(len(rows), 5)
        self.assertEqual({r["N"] for r in rows}, {"696"})
        self.assert_rows(
            f"| {g7(r['a4'])} | {r['occupied_set_equal_to_a4_0']} | {r['open_shell']} | {g7(r['E_aufbau'])} | "
            f"{g7(r['E_adiabatically_continued'])} | {g7(r['difference'])} |" for r in rows)

    def test_thermodynamics(self):
        thermo = csv_by_id("thermo/thermodynamics.csv")
        self.assert_rows(
            f"| {g7(r['a4'])} | {g7(r['T'])} | {g7(r['mu'])} | {g7(r['E'])} | {g7(r['entropy'])} | "
            f"{g7(r['Omega_direct'])} | {g3(r['sea_holes_over_N'])} |"
            for r in (thermo[f"N136_lam0_{s}_{t}"] for s in ("a00", "a20") for t in ("T10", "T20", "T50")))

    def test_emt_integrals(self):
        emt = csv_by_id("ground/emt-integrals.csv")
        self.assert_rows(
            f"| {n} | {g7(r['a4'])} | {g7(r['int_rho'])} | {g7(r['int_p3'])} | {g7(r['int_p_t'])} | {g7(r['int_p8'])} |"
            for n in (136, 688) for r in (emt[f"N{n}_lam0_{s}"] for s in SLICES))

    def test_rescaling(self):
        resc = csv_by_id("rescaling/rescaling.csv")
        self.assert_rows(
            f"| {g7(r['a4'])} | {g7(r['partner_dk'])} | {g7(r['partner_v_t'])} | {g4(r['max_abs_delta_eps'])} | "
            f"{g4(r['rel_delta_E'])} | {g7(r['partner_E_KS'])} |"
            for r in (resc[f"N136_lamp1_{s}"] for s in SLICES[1:]))
        for s in SLICES[1:]:
            r = resc[f"N136_lamp1_{s}"]
            a = float(r["a4"])
            self.assertAlmostEqual(float(r["partner_dk"]), 0.25 * 2.718281828459045 ** (-a), places=12)
            self.assertEqual((r["same_label_set"], r["same_occupations"]), ("true", "true"))


class QuotedNumbers(unittest.TestCase):
    """Every further number of the text, found in its report, results file or README."""

    def setUp(self):
        self.text = markdown_text()

    def pair(self, source_text: str, in_source: str, in_document: str | None = None):
        self.assertIn(in_source, source_text, in_source)
        self.assertIn(in_source if in_document is None else in_document, self.text, in_document or in_source)

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
        self.assertEqual(theory["boundaryConditions"]["brane"]["status"], "ASSUMED")
        self.assertIn("OPEN", theory["adiabaticity"]["caveat"])
        self.pair(check_detail(THEORY_WOLFRAM, "brane_band_slope"), "1.905148253644866")
        self.pair(check_detail(RUST_SOLVER, "theory_input_coefficients"), "M_eff = m + 0.9375 lambda S",
                  "$M_{\\mathrm{eff}} = m + 0.9375\\lambda S$")
        self.pair(check_detail(RUST_SOLVER, "theory_input_coefficients"), "v_v = -0.0625 lambda n",
                  "$v_v = -0.0625\\lambda n$")

    def test_parameters(self):
        params = load_json(RESULTS / "parameters.json")
        physics, numerics = params["physics"], params["numerics"]
        self.assertEqual((physics["H"], physics["m"], physics["L_tipCutoff"], physics["dk"], physics["v_t"]),
                         (1.0, 1.0, 3.0, 0.25, 1.0))
        self.assertIn("$H = m = 1$, $L = 3$, $\\Delta k = 0.25$, $v_t = 1$", self.text)
        self.assertIn(f"$\\mathrm{{Vol}}_7 = {physics['Vol7']!r}$", self.text)
        self.assertEqual(physics["slicesA4"], [0.0, 0.5, 1.0, 1.5, 2.0])
        self.assertEqual(physics["temperatures"], [0.01, 0.02, 0.05])
        self.assertEqual((physics["tipTheta"], physics["historyA"]), (0.0, 1.0))
        self.assertIn("$a_{4,0} \\in \\{0, 0.5, 1, 1.5, 2\\}$", self.text)
        self.assertIn("$T \\in \\{0.01, 0.02, 0.05\\}$", self.text)
        self.assertEqual((numerics["rk4Steps"], numerics["rootTolerance"], numerics["scfTolerance"]),
                         (900, 1e-13, 1e-11))
        self.assertIn("RK4 on 900 steps, Pruefer counting and a root tolerance of 1e-13, Anderson-mixed SCF to 1e-11",
                      self.text)
        self.assertEqual(params["particleNumbers"]["values"], [8.0, 136.0, 688.0])
        self.assertIn(f"bulk edge {params['particleNumbers']['bulkEdge']!r}", self.text)
        self.assertIn("sum w_Z2 g f = N", params["conventions"]["particleNumber"])

    def test_matrix_sizes(self):
        crosscheck = load_json(CROSSCHECK)
        self.assertEqual(crosscheck["comparisons"], 162691)
        self.assertEqual(crosscheck["matrix"], {"ground": 75, "thermal": 135, "exact_fock_variant": 60,
                                                "rescaling_partners": 60, "particle_hole_lists": 75,
                                                "crossing_demo_slices": 5})
        self.assertIn("162691 comparisons", self.text)
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
        self.assertEqual(top["id"], "N688_lamm2_a00")
        self.assertEqual(top["Q_max_pair"], "11:+1:even:0 -> 11:+1:even:1")
        self.assertIn(f"is {g7(top['Q_max'])} (state N688_lamm2_a00, pair `11:+1:even:0 -> 11:+1:even:1`", self.text)
        self.assertIn(f"$Q_{{\\max}} \\leq {g7(top['Q_max'])}$", self.text)
        self.assertTrue(all(float(r["Q_max"]) == 0.0 for r in rows if r["N"] == "8"))
        self.pair(check_detail(RUST_SOLVER, "adiabatic_hellmann_feynman"), "worst value 2.609e-9", "(worst 2.609e-9")
        history = load_json(RESULTS / "adiabatic" / "history.json")
        self.assertEqual(len(history["series"]), 15)
        self.assertTrue(all(series["fermiLevelCrossings"] == [] for series in history["series"]))
        self.assertTrue(all(r["occupied_set_changed"] == "false" for r in csv_rows("adiabatic/fermi-level-crossings.csv")))
        self.assertIn("every one of the 15 series", self.text)
        self.assertIn("$N = 696$", self.text)

    def test_excited_and_thermo_numbers(self):
        self.pair(check_detail(RUST_SOLVER, "excited_delta_scf_free_equals_gap"), "15 cases; worst value 2.011e-11",
                  "worst difference 2.011e-11 over 15 cases")
        detail = check_detail(RUST_SOLVER, "thermo_sea_hole_diagnostic_computed")
        self.pair(detail, "15 of 135 states (largest 30.976 N)", "15 of 135 states")
        self.assertIn("the largest is 30.976 N", self.text)
        thermo = csv_rows("thermo/thermodynamics.csv")
        outside = [r for r in thermo if r["particle_only_convention_within_1pc"] == "false"]
        self.assertEqual(len(outside), 15)
        self.assertTrue(all(float(r["a4"]) >= 1.0 for r in outside))
        self.assertIn("all at $a_{4,0} \\geq 1$", self.text)
        self.assertIn("N136_lam0_a20_T50", [r["id"] for r in outside])
        self.pair(check_detail(MERMIN_ROOTS, "root_precision_self_check"), "7.5e-35")

    def test_rescaling_and_t3_numbers(self):
        self.pair(check_detail(RUST_SOLVER, "rescaling_identity_between_slices"), "worst value 1.478e-13",
                  "The worst level difference is 1.478e-13")
        self.pair(check_detail(RUST_SOLVER, "rescaling_identity_energy_profiles"), "worst value 3.318e-13",
                  "the profiles 3.318e-13")
        detail = check_detail(RUST_SOLVER, "t3_block_map_solver_selftest")
        self.assertIn("NOT a proof of T3", detail)
        self.pair(detail, "(worst 9.95e-14, tolerance 1e-9)", "(worst 9.95e-14, tolerance 1e-9;")

    def test_determinism_and_refinement_numbers(self):
        self.pair(check_detail(DETERMINISM, "repeat_byte_identical"), "244 files", "all 244 result files")
        for name, value in (("refined_ground_energies", "1.901e-12"), ("refined_eigenvalues", "2.135e-09"),
                            ("refined_eigenvalues", "23724"), ("refined_profiles", "2.800e-09"),
                            ("refined_adiabatic_derivatives", "9.024e-10"),
                            ("refined_thermodynamics", "2.489e-10"), ("refined_heat_capacity", "5.689e-09")):
            self.pair(check_detail(DETERMINISM, name), value)
        description = load_json(KS / "checker" / "rust-refinement.json")["description"]
        self.assertIn("canonical: RK4 G = 900, root tolerance 1e-13, SCF tolerance 1e-11", description)
        self.assertIn("refined: G = 1800, 1e-14, 1e-12", description)
        self.assertIn("(900 to 1800 RK4 steps, root tolerance 1e-14, SCF tolerance 1e-12)", self.text)
        self.assertEqual(count_report(RUST_SOLVER)[0], 42)
        self.assertIn("42 of 42 checks PASS in 128 s", self.text)

    def test_reference_numbers(self):
        self.assertIn("(second order: 4", check_detail(REFERENCE, "free_convergence_order_two"))
        self.assertIn("G = 300, 600", check_detail(REFERENCE, "free_k0_analytic_spectra"))
        self.assertIn("G = 2400", check_detail(REFERENCE, "richardson_uncertainty_validated"))
        self.assertIn("three grids (300, 600, 1200)", self.text)

    def test_source_condition_numbers(self):
        detail = check_detail(SOURCE_CONDITIONS, "ks_profiles_depend_on_x8")
        self.pair(detail, ">= 0.0497329", "\\geq 0.0497329")
        self.assertIn("70 with a nonzero", detail)
        self.assertIn("Every one of the 70 nonzero ground-state profiles", self.text)
        detail = check_detail(SOURCE_CONDITIONS, "ks_profiles_violate_algebraic_condition")
        self.pair(detail, "between 2.09192", "between 2.09192 and 3.99006")
        self.assertIn("and 3.99006", detail)
        detail = check_detail(SOURCE_CONDITIONS, "ks_integrals_violate_algebraic_condition")
        for value in ("0.414328", "N136_lam0_a00: 0.339767", "N136_lam0_a10: 0.25969", "N136_lam0_a20: 0.239714"):
            self.pair(detail, value, value.split(": ")[-1])
        self.assertIn("5 states have an identically vanishing", check_detail(SOURCE_CONDITIONS,
                                                                            "ks_zero_source_states_listed"))
        self.assertIn("Five states have an identically vanishing tensor", self.text)
        conclusions = " ".join(load_json(SOURCE_A4)["conclusions"])
        for value in ("0.583068", "1.95362", "1.1321", "0.847549", "0.149623", "0.0724197", "0.102772"):
            self.pair(conclusions, value)
        self.assertIn("has no solution; nothing about a4 is DERIVED from it", conclusions)

    def test_run_times_from_the_readmes(self):
        sources = (
            (KS / "theory" / "WOLFRAMSCRIPT_PROVENANCE.md", ("about 40 to 85 seconds", "about 75 to 165 seconds"),
             ("about 40 to 85 s", "about 75 to 165 s")),
            (KS / "solver" / "README.md", ("78.1 s in total", "repeat of the canonical matrix 178.4 s", "618.6 s"),
             ("78.1 s on an idle machine", "the repeat 178.4 s", "the refined run 618.6 s")),
            (KS / "reference" / "README.md", ("578.3 s",), ("the reference 578.3 s",)),
            (KS / "checker" / "README.md", ("85.2 s and 61.3 s [31.6 s, 31.3 s]", "721.2 s and 777.1 s in total [588.9 s"),
             ("31.6 s idle and 85.2 s shared", "588.9 s idle and 721.2 s shared")),
            (REVISION / "field_equations_a4" / "ks_source" / "README.md", ("3 s on an idle development machine, up\nto about 20 s",),
             ("3 s to about 20 s",)),
            (REVISION / "field_equations_a4" / "README.md", ("43-70 s (Wolfram) and 7-28 s",),
             ("43 to 70 s (Wolfram) and 7 to 28 s (sympy)",)),
            (DOCS / "PAIR_CREATION_PROOFS.md", ("the T3 verifiers 10 of 10 (about 3 s) and 13 of 13 (about 1 s)",),
             ("the T3 verifiers about 3 s and 1 s",)),
        )
        for path, in_source, in_document in sources:
            text = path.read_text(encoding="utf-8")
            for value in in_source:
                self.assertIn(value, text, f"{value} in {path.name}")
            for value in in_document:
                self.assertIn(value, self.text, value)


if __name__ == "__main__":
    unittest.main()
