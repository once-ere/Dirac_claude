#!/usr/bin/env python3
"""Publication test for Revision/docs/DARK_SECTOR_HYPOTHESES.{md,tex,pdf}.

The document is deliverable 5 of Revision/SPEC.md section 10: the two hypotheses of SPEC section 8
(Hypothesis for dirac16complex, Hypothesis00 for dirac16complex00), the lead's analysis of SPEC
section 11 checked point by point, the observer assumption for rho_4 with the definitions (A), (B),
(C), the method, the results for each field, the comparison with the Supernovae Unite values, the
verdicts and what remains open.  Since 2026-10-15 every result is for the author's metric with the
second function b4(x4) (a function of x4, never 1), on the history a4 = H x4,
b4 = b4(0) e^((4/3) H x4) of the author's weights; the b4 = 1 record is withdrawn.  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_dark_sector_hypotheses_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md (same options as the
    build command above), both files are UTF-8 with LF line endings, and their sha256 are pinned;
  * the PDF is registered in the Revision registry Revision/pdf-specifications.json (edition
    dark-sector-hypotheses: path, page count and sha256 of the committed PDF) and NOT in the
    registry of the earlier stages; the PDF is structurally sound;
  * title, subtitle and section headings; the last section is "What is proved, computed, assumed
    and not established";
  * the key statements are present (tuned models are NOT predictions, the ghost-like sector is not
    an established physical state, the observer normalisation is an ASSUMPTION, neither hypothesis
    is established), and overclaims are absent (with negative controls);
  * every check name the document cites exists in a Revision report with the verdict PASS, and
    every check of the six dark-sector reports is listed (complete verification records);
  * the report-count table equals the counts recomputed from the reports;
  * every number quoted in the document is read from its JSON report: either it occurs verbatim
    in the detail of the named check, or it is the stated rounding of the named JSON value;
  * OPTIONAL (only when REVISION_PDF_REBUILD=1; needs pdflatex, about 10 s): the PDF is rebuilt in
    verify mode and must match the registry.

After an intended edit of the document: rebuild in verify mode until warning-free, register it
(--register), and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import csv
import fnmatch
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

DOCS = REVISION / "docs"
MARKDOWN = DOCS / "DARK_SECTOR_HYPOTHESES.md"
TEX = DOCS / "DARK_SECTOR_HYPOTHESES.tex"
PDF = DOCS / "DARK_SECTOR_HYPOTHESES.pdf"
EDITION = "dark-sector-hypotheses"
REGISTRY = REVISION / "pdf-specifications.json"
OLD_REGISTRY = ROOT / "provenance" / "pdf-specifications.json"
REBUILD = os.environ.get("REVISION_PDF_REBUILD") == "1"

MARKDOWN_SHA256 = "85f18d1acb1a4372a419f9f7302f32250fc003679706a385b4f55cd591f44710"
TEX_SHA256 = "3267c0f3ae437d22d2504b9c8a7687077d21d2449f7200ceccbcc88bed10ccca"

DARK = REVISION / "dark_sector"
D16 = DARK / "dirac16complex"
D00 = DARK / "dirac16complex00"
DERIVATION = D16 / "reports" / "derivation-checks.json"
KS_HISTORY = D16 / "reports" / "ks-history-run.json"
EOS_CHECKS = D16 / "reports" / "eos-checks.json"
INDEPENDENT = D16 / "reports" / "independent-checks.json"
EOS_SUMMARY = D16 / "outputs" / "eos-summary.json"
FREE_GAS = D16 / "outputs" / "independent-free-gas.json"
DERIVE_EOS = D00 / "reports" / "python-derive-eos.json"
INDEPENDENT_NUMERICS = D00 / "reports" / "python-independent-numerics.json"
EOS_THEORY = D00 / "eos-theory.json"
NUMERICS = D00 / "results" / "independent-numerics.json"
WOLFRAM = DARK / "reports" / "wolfram-dark-sector-b4.json"
KS_SOURCE = REVISION / "field_equations_a4" / "reports" / "ks-source-conditions.json"
A4_EQUATIONS = REVISION / "field_equations_a4" / "a4-equations.json"
EXACT_FOCK = REVISION / "kohn_sham" / "results" / "exx" / "exact-fock-variant.csv"

# The seven dark-sector reports, every check of which the document lists (section 11.2).
DARK_REPORTS = (DERIVATION, KS_HISTORY, EOS_CHECKS, INDEPENDENT, DERIVE_EOS, INDEPENDENT_NUMERICS, WOLFRAM)
# The reports of the count table (section 11.1), in the order of the table.
COUNTED_REPORTS = (
    "Revision/dark_sector/dirac16complex/reports/derivation-checks.json",
    "Revision/dark_sector/dirac16complex/reports/ks-history-run.json",
    "Revision/dark_sector/dirac16complex/reports/eos-checks.json",
    "Revision/dark_sector/dirac16complex/reports/independent-checks.json",
    "Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json",
    "Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json",
    "Revision/dark_sector/reports/wolfram-dark-sector-b4.json",
    "Revision/field_equations_a4/reports/ks-source-conditions.json",
)
# Every report whose check names the document may cite.
CITABLE_REPORT_GLOBS = (
    "dark_sector/dirac16complex/reports/*.json",
    "dark_sector/dirac16complex00/reports/*.json",
    "dark_sector/reports/*.json",
    "field_equations_a4/reports/ks-source-conditions.json",
)

TITLE = ("Dark-sector hypotheses for dirac16complex and dirac16complex00: the equation of state seen "
         "from 3-space")
SUBTITLE_START = ("Hypothesis and Hypothesis00 investigated in the author's primordial gravitational field "
                  "with exponentially deflating extra times")
SECTIONS = (
    "## Abstract",
    "## 1. The hypotheses and the short answer",
    "## 2. Setting and conventions",
    "## 3. The observer assumption: $\\rho_4$ and the definitions (A), (B), (C)",
    "## 4. Method",
    "## 5. Results for dirac16complex",
    "## 6. Results for dirac16complex00",
    "## 7. Comparison with the Unite values",
    "## 8. The lead's analysis (SPEC section 11), checked point by point",
    "## 9. Verdicts",
    "## 10. What remains open",
    "## 11. Verification records",
    "## 12. Reproduction",
    "## 13. What is proved, computed, assumed and not established",
)
LAST_SECTION = "## 13. What is proved, computed, assumed and not established"
KEY_STATEMENTS = (
    "A model with as many tuned parameters as matched numbers reproduces them by construction and is "
    "NOT a prediction.",
    "A ghost (negative-energy) component is a ghost-like sector, not an established physical state",
    "This record establishes neither Hypothesis nor Hypothesis00",
    "Nothing in this record establishes that either field is dark energy or dark matter.",
    "The rho_4 normalisation is an ASSUMPTION about the observer, not a consequence of the field "
    "equations, and this record does not choose one.",
    r"$w_{\rm eff} = X/E - s + (\beta/2)(P_t/E + s)$ with $X = P_3 - P_t$",
    "every verdict moves by exactly $-1/3$ between (A, B) and (C)",
    "$x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE exponentially",
    "$b_4$ is a function of $x_4$, and every result below is computed with it",
    "The history is therefore a PRESCRIBED BACKGROUND for test fields.",
    "both CHOSEN on the withdrawn record to solve tangent $= (-0.861, -0.60)$",
    "On the withdrawn record the M4 tangent and the M5 fit equal the Unite pair by construction.",
    "so $w_0 = -0.861$ needs $G \\geq 1583/1000$",
    "the $b_4$-free identity of the withdrawn record fails on the interacting series",
    "NOT FOUND in the computed states",
    "Positive-energy extra-time momentum does NOT supply it",
    "In this convention thawing means $w_a < 0$",
    "$w_{\\rm exp} = -1$ exactly",
    "so it is not the supernova constant-$w$ fit -0.764, which weights the data",
    "No supernova likelihood, distance fit or covariance is computed anywhere in this record.",
    "This value of $\\lambda S/m$ is CHOSEN to give -0.764: one parameter tuned to one number.",
    "2. Any Unite value as an output of the field equations: no positive-energy content reaches them on the history",
    "Negative $E$ is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record",
    "This negative $E$ is therefore a property of the approximate functional; good-sector states with "
    "$E < 0$ are not established beyond it.",
    "\\kappa\\,(\\rho,\\ p_3,\\ p_t,\\ p_0) = \\Big(-\\frac{2}{27},\\ -\\frac{2}{9},\\ -\\frac{22}{27},\\ -\\frac{14}{27}\\Big)",
    "no condensate is it",
    "in the positive realisation of the good sector (with the ASSUMED brane condition",
    "crosses $-1$ on $[1/3, 1]$?",
)
FORBIDDEN = (
    r"\b(?:hypothesis(?:00)?|hypotheses)\s+(?:is|are|has been|have been|was|were)\s+"
    r"(?:confirmed|proved|proven|established|verified|supported)\b",
    r"\bdirac16complex(?:00)?\s+(?:is|provides|explains|accounts for|produces)\s+(?:the\s+)?"
    r"(?:observed\s+)?dark\s+(?:energy|matter)\b",
    r"\bpredict(?:s|ed|ion of)?\s+(?:the\s+)?Unite\b",
    r"\bghost(?:-like)?\s+(?:sector|component|modes?)\s+(?:is|are)\s+(?:a\s+)?"
    r"(?:physical|established|real)\b",
    r"\b(?:proves?|proved|proven)\s+(?:that\s+)?(?:a\s+)?(?:time-varying\s+)?dark[- ](?:energy|matter)\b",
    # w >= -1 for M3 and M4 holds only before the turning point a_* of their extra-time mode
    r"\b(?:M3|M4)\b[^.]*\bnever\s+crosses\s+\$?-1",
    r"\bthawing\b[^.;]*\$w\s*\\geq\s*-1\$\s+at\s+every\s+\$a\$",
    # negative E is not specific to the Krein sector (the N = 8, lambda > 0 good-sector states have E < 0)
    r"otherwise\s+\$E\s*<\s*0\$,\s+the\s+negative-norm",
    # the Einstein linear-member ratio is phantom only for kappa * rho > 0
    r"\$w\s*<\s*-1\$\s+for\s+\$\\rho\s*>\s*0\$",
    # negative E of the N = 8 states is a property of the canonical uniform-gas functional (exact Fock: |E| <= 2.04e-13)
    r"not\s+specific\s+to\s+a\s+negative-norm\s+\(Krein\)\s+sector\s*:",
    # kappa > 0 and rho > 0 on the linear member need Lambda < -(21 + 3 A^2) H^2; it is no bare example
    r"e\.g\.\s+for\s+\$\\kappa\s*>\s*0\$\s+and\s+\$\\rho\s*>\s*0\$",
)
FILE_SUFFIXES = (".json", ".py", ".wls", ".wl", ".md", ".tex", ".pdf", ".rs", ".csv", ".toml")


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
        if span.endswith(FILE_SUFFIXES):
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.*]*", span):
            names.append(span)
    return names


def report_checks() -> dict[str, list[str]]:
    """Check name -> list of verdicts (upper case) over every citable Revision report."""
    verdicts: dict[str, list[str]] = {}
    for pattern in CITABLE_REPORT_GLOBS:
        for path in sorted(REVISION.glob(pattern)):
            for check in load_json(path).get("checks", []):
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


def fixed(value: float, digits: int) -> str:
    return f"{value:.{digits}f}"


def series(name: str) -> dict:
    for entry in load_json(EOS_SUMMARY)["series"]:
        if entry["series"] == name:
            return entry
    raise KeyError(name)


# Numbers quoted verbatim from the detail of a named check: (report, check, substrings).  Each
# substring must occur in the check's detail AND in the document.
DETAIL_NUMBERS = (
    (DERIVATION, "condensate_ratio_equal_unite_constant_w", ("-382/441", "-0.866213151927", "0.566893424036")),
    (DERIVATION, "mixture_C_matching_w0_unite_b4", ("(-0.388667, 0.278000]",)),
    (DERIVATION, "unite_deep_past", ("-1.461",)),
    (KS_HISTORY, "all_runs_succeeded", ("615 runs (15 series x 41 slices)",)),
    (KS_HISTORY, "a4_0_states_equal_committed_record", ("0.000e+00",)),
    (KS_HISTORY, "y_conservation_every_state", ("1.951e-08",)),
    (KS_HISTORY, "particle_number_every_state", ("2.442e-15",)),
    (EOS_CHECKS, "conservation_with_b4_term", ("6.351e-06", "6.7e-06")),
    (EOS_CHECKS, "conservation_without_b4_term_fails", ("1.630e+00",)),
    (EOS_CHECKS, "conservation_integrated_simpson", ("3.585e-07",)),
    (EOS_CHECKS, "derivative_two_ways", ("6.394e-07", "3.532e-05")),
    (EOS_CHECKS, "gas_radiation_like_band", ("[0.292903, 0.326429]",)),
    (EOS_CHECKS, "gas_C_near_zero_on_b4_history", ("[-0.040430, -0.006905]",)),
    (EOS_CHECKS, "n8_interacting_zero_modes_dilute_with_b4",
     ("[0.018402, 0.019031]", "0.018316", "[0.931316, 0.999997]", "[0.620877, 0.666665]")),
    (EOS_CHECKS, "condensate_drifts_with_b4", ("-2.695392", "-0.509333", "-0.842667", "-1.796928")),
    (EOS_CHECKS, "mixture_C_cannot_reach_unite_w0_with_lambda0_condensate", ("-0.333015",)),
    (EOS_CHECKS, "mixture_scan_three_definitions_b4",
     ("0.5891697548245", "0.6119842735815", "0.2910614215438", "-2.639515126434")),
    (EOS_CHECKS, "gas_cpl_thawing_sign_small",
     ("[-0.017766, -0.009043]", "[-0.026521, -0.019590]", "[-0.040430, -0.006905]")),
    (INDEPENDENT, "exact_k0_spectra", ("1.421e-14", "1.292292828069")),
    (INDEPENDENT, "brane_band_slope", ("1.9051482536",)),
    (INDEPENDENT, "collocation_converged", ("6.01e-15",)),
    (INDEPENDENT, "energy_vs_rust_solver", ("82 states", "1.897e-12")),
    (INDEPENDENT, "w_eff_vs_primary", ("1.492e-12",)),
    (INDEPENDENT, "cpl_tangent_vs_primary", ("4.027e-07",)),
    (INDEPENDENT, "bulk_band_dark_matter_law", ("0.239626", "2.268e-03", "0.765177", "0.778801")),
    (INDEPENDENT, "brane_band_radiation_law", ("[0.291594, 0.333275]",)),
    (DERIVE_EOS, "condensate_ratio_equals_unite_constant_w", ("-382/441",)),
    (DERIVE_EOS, "condensate_phantom_interval", ("(-2, -1)",)),
    (DERIVE_EOS, "unite_line_fit_proxy", ("-1.011", "-1.061")),
    (DERIVE_EOS, "unite_crossing_point", ("461/600", "139/461")),
    (DERIVE_EOS, "condensate_ratio_drift_at_unite_value", ("-84231/31250", "-2.695392")),
    (DERIVE_EOS, "branch_required_source", ("-2/27", "-2/9", "-22/27", "-14/27")),
    (DERIVE_EOS, "M2_tangent_exact_b4", ("417/1000", "-583/3000", "81037/500000")),
    (DERIVE_EOS, "M3_tangent_exact_b4", ("417/1417", "-287/1000", "-196963/4500000")),
    (DERIVE_EOS, "M4_withdrawn_tuning_on_b4_history", ("264037/403037", "57963/264037", "-0.33280216468")),
    (DERIVE_EOS, "positive_models_bounded_by_minus_one_third",
     ("-0.194333333333", "-0.332598868774", "-0.33280216468")),
    (DERIVE_EOS, "unite_w0_requires_dominant_ghost", ("1583/1000", "1583/2583")),
    (INDEPENDENT_NUMERICS, "B_solve_M3_s", ("0.29429162", "0.2942837")),
    (INDEPENDENT_NUMERICS, "B_positive_models_bounded", ("-0.31820563",)),
    (INDEPENDENT_NUMERICS, "B_growth_rate", ("6.2639848", "0.30893327", "0.31165344")),
    (INDEPENDENT_NUMERICS, "B_condensate_dilutes_with_b4", ("1.2610746e-13", "0.91990032")),
    (INDEPENDENT_NUMERICS, "B_dilution_equals_formula_M2", ("4.0240551e-05",)),
    (WOLFRAM, "D7_branch_required_source", ("-2/27", "-2/9", "-22/27", "-14/27")),
)


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
        self.assertEqual(entry["path"], "Revision/docs/DARK_SECTOR_HYPOTHESES.pdf")
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
        self.assertEqual(level2[-1], LAST_SECTION)
        tex = TEX.read_text(encoding="utf-8")
        self.assertIn("\\section{What is proved, computed, assumed and not established}", tex)
        for sub in ("### 13.1 Proved", "### 13.2 Computed", "### 13.3 Assumed", "### 13.4 Not established"):
            self.assertIn("\n" + sub, self.text, sub)

    def test_key_statements(self):
        for statement in KEY_STATEMENTS:
            self.assertIn(statement, self.text, statement)

    def test_hypotheses_quoted_from_the_readme(self):
        readme = (REVISION / "README.md").read_text(encoding="utf-8")
        self.assertIn("> Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying "
                      "dark energy\n> equation of state", readme)
        self.assertIn("“Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying "
                      "dark energy equation of state and/or a possible physical mechanism for a time-varying "
                      "dark matter equation of state, both of which you will investigate.”", self.text)
        self.assertIn("> Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.",
                      readme)
        self.assertIn("“Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.”",
                      self.text)

    def test_tuned_models_are_labelled(self):
        """Every model or mixture tuned to a Unite number is marked CHOSEN and by construction."""
        for row in (
            "| M2 | positive-energy good-sector gas, $q = 0$ | $k^2/(k^2+m^2) = 417/1000$ at $a = 1$, CHOSEN on the "
            "withdrawn record for $w_0 = -0.861$ |",
            "| M3 | positive-energy extra-time mode, $k = 0$ | $s = q_p^2/m^2 = 417/1417$, CHOSEN on the withdrawn "
            "record for $w_0 = -0.861$ |",
            "| M4 | condensate + positive extra-time mode | $s = 264037/403037$ and $\\Omega_q = 57963/264037$, "
            "both CHOSEN on the withdrawn record to solve tangent $= (-0.861, -0.60)$ |",
            "| M5 | M4-type + GHOST: massless modes of negative classical energy | $G = 3/10$ of the total at "
            "$a = 1$ (a stated choice); $s$ and $\\Omega_q$ CHOSEN on the withdrawn record so that its fit over "
            "$[1/2, 1]$ was $(-0.861, -0.60)$ |",
        ):
            self.assertIn(row, self.text, row)
        self.assertGreaterEqual(self.text.count("by construction"), 6)
        self.assertGreaterEqual(self.text.count("CHOSEN"), 10)
        self.assertGreaterEqual(self.text.count("ghost-like sector"), 4)

    def test_no_overclaims(self):
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)
        self.assertNotRegex(self.text, r"(?<!never )\bproved that\b")

    def test_negative_controls(self):
        """The content checks are not vacuous: tampered statements are detected."""
        tampered = (
            "Hypothesis00 is confirmed by the model M4.",
            "dirac16complex00 provides the dark energy of the Unite data.",
            "The model M4 predicts the Unite values.",
            "The ghost sector is physical.",
            "This proves that a time-varying dark energy exists.",
            "M4, tuned to the Unite tangent, never crosses $-1$.",
            r"as freezing (M2) or thawing (M3, M4) evolution with $w \geq -1$ at every $a$",
            "otherwise $E < 0$, the negative-norm (Krein) sector",
            r"the linear member, a constant ratio $w < -1$ for $\rho > 0$",
            "Negative $E$ is not specific to a negative-norm (Krein) sector: in the good sector",
            r"phantom exactly when $\kappa\rho > 0$, e.g. for $\kappa > 0$ and $\rho > 0$",
        )
        self.assertEqual(len(tampered), len(FORBIDDEN))
        for pattern, sentence in zip(FORBIDDEN, tampered):
            self.assertIsNotNone(re.search(pattern, sentence, re.IGNORECASE), pattern)
        self.assertNotIn("M4_tangent_equals_unit", report_checks())
        total, passed, failed = count_report(DERIVATION)
        wrong_row = (f"| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | "
                     f"{total + 1} | {passed} | {failed} |")
        self.assertNotIn(wrong_row, self.text)
        self.assertNotIn("0.436704", self.text)  # a tampered gas fraction would not be quoted

    def test_no_material_of_the_earlier_stages(self):
        for marker in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            self.assertNotIn(marker, self.text, marker)

    def test_private_pdf_only_its_numbers(self):
        self.assertNotIn("Gmail", self.text)
        self.assertIn("The author's private PDF (not part of the repository; only these numbers are used)",
                      self.text)

    def test_cited_checks_exist_and_pass(self):
        verdicts = report_checks()
        cited = cited_check_names(self.text)
        self.assertGreater(len(cited), 150)
        for name in cited:
            if "*" in name:
                matches = fnmatch.filter(verdicts, name)
                self.assertTrue(matches, name)
                for match in matches:
                    self.assertTrue(all(v == "PASS" for v in verdicts[match]), match)
                continue
            self.assertIn(name, verdicts, name)
            self.assertTrue(all(v == "PASS" for v in verdicts[name]), name)

    def test_every_dark_sector_check_is_listed(self):
        cited = set(cited_check_names(self.text))
        for path in DARK_REPORTS:
            names = [check["name"] for check in load_json(path)["checks"]]
            for name in names:
                self.assertIn(name, cited, f"{name} of {path.name}")
        headers = (
            ("**dirac16complex, derive_effective.py**", DERIVATION),
            ("**dirac16complex, run_ks_history.py**", KS_HISTORY),
            ("**dirac16complex, compute_eos.py**", EOS_CHECKS),
            ("**dirac16complex, independent_free_gas.py**", INDEPENDENT),
            ("**dirac16complex00, derive_eos.py (A)**", DERIVE_EOS),
            ("**dirac16complex00, independent_numerics.py (B)**", INDEPENDENT_NUMERICS),
            ("**dark sector, verify_dark_sector_b4.wls (Wolfram)**", WOLFRAM),
        )
        for header, path in headers:
            self.assertIn(f"{header} ({len(load_json(path)['checks'])} checks):", self.text, header)

    def test_report_count_table(self):
        for relative in COUNTED_REPORTS:
            total, passed, failed = count_report(ROOT / relative)
            row = f"| `{relative}` | {total} | {passed} | {failed} |"
            self.assertIn(row, self.text, row)
            self.assertEqual(failed, 0, relative)
            self.assertEqual(passed, total, relative)
        self.assertEqual(load_json(DERIVATION)["summary"], {"total": 39, "pass": 39, "fail": 0})
        self.assertEqual(load_json(DERIVE_EOS)["summary"], "49/49 checks pass")
        self.assertEqual(load_json(INDEPENDENT_NUMERICS)["summary"], "32/32 checks pass")
        self.assertEqual((load_json(WOLFRAM)["checkCount"], load_json(WOLFRAM)["failedCount"]), (8, 0))
        self.assertIn("39 of 39, 7 of 7, 15 of 15, 10 of 10, 49 of 49, 32 of 32 and 8 of 8 checks passed", self.text)


class QuotedNumbers(unittest.TestCase):
    """Every number of the document is read from its JSON report."""

    def setUp(self):
        self.text = markdown_text()

    def assertQuoted(self, value: str):
        self.assertIn(value, self.text, value)

    def test_check_detail_numbers(self):
        for path, name, substrings in DETAIL_NUMBERS:
            detail = check_detail(path, name)
            for substring in substrings:
                self.assertIn(substring, detail, f"{substring} not in {name}")
                self.assertQuoted(substring)

    def test_unite_values(self):
        unite = load_json(EOS_SUMMARY)["unite_comparison"]["unite"]
        self.assertEqual((unite["w_const"], unite["w0"], unite["wa"]), (-0.764, -0.861, -0.6))
        theory = load_json(EOS_THEORY)["models"]["unite"]
        self.assertEqual(Fraction(theory["constant_w"]), Fraction(-764, 1000))
        self.assertEqual(Fraction(theory["w0"]) + Fraction(theory["wa"]), Fraction(-1461, 1000))
        self.assertEqual(theory["crossing_of_minus_1"]["a"], "461/600")
        self.assertEqual(fixed(float(Fraction(461, 600)), 4), "0.7683")
        self.assertQuoted("$a = 461/600 = 0.7683$ ($z = 139/461$")
        self.assertQuoted("$(w_0, w_a) = (-0.861, -0.60)$")
        self.assertQuoted("the Supernovae Unite constant-$w$ fit $w = -0.764$")

    def test_kohn_sham_gas_series(self):
        s = series("N688_lam0")
        lo, hi = s["w_eff_A_B_range"]
        self.assertQuoted(f"$w_{{\\rm eff}}(A) = w_{{\\rm eff}}(B)$ goes from {fixed(lo, 4)} to {fixed(hi, 4)}")
        self.assertQuoted(f"({fixed(lo, 4)} to {fixed(hi, 4)} for $N = 688$, $\\lambda = 0$)")
        lo, hi = s["w_eff_C_range"]
        self.assertQuoted(f"$w_{{\\rm eff}}(C)$ from {fixed(lo, 4)} to {fixed(hi, 4)}")
        lo, hi = s["ratio_wx0_range"]  # the hidden-direction ratio P0/E (named w8 before 2026-10-14)
        self.assertQuoted(f"$w_{{x_0}} = P_0/E$ goes from {fixed(lo, 4)} to {fixed(hi, 4)}")
        start, end = s["dlnE_da4_at_0_and_2"]
        self.assertQuoted(f"goes from {fixed(start, 4)} at $a_4 = 0$ to {fixed(end, 4)} at $a_4 = 2$")
        self.assertEqual(s["ratio_wt_range"], [0.0, 0.0])
        worst = max(abs(x) for entry in load_json(EOS_SUMMARY)["series"]
                    if entry.get("N") in (136, 688) and "ratio_wt_range" in entry
                    for x in entry["ratio_wt_range"])
        self.assertLessEqual(worst, 0.002)
        self.assertQuoted("$|P_t/E| \\leq 0.002$ over the $N = 136, 688$ series")

    def test_cpl_tangent_and_fit_table(self):
        s = series("N688_lam0")
        tangents = {t["a4_today"]: t for t in s["cplTangent"]}
        self.assertEqual(sorted(tangents), [0.5, 1.0, 1.5, 2.0])
        w0 = " | ".join(fixed(tangents[a]["w_eff_C"]["w0"], 4) for a in (0.5, 1.0, 1.5, 2.0))
        wa = " | ".join(fixed(tangents[a]["w_eff_C"]["wa"], 5) for a in (0.5, 1.0, 1.5, 2.0))
        self.assertQuoted(f"| $w_0$ under (C) | {w0} |")
        self.assertQuoted(f"| $w_a$ (every definition) | {wa} |")
        for a in (0.5, 1.0, 1.5, 2.0):
            t = tangents[a]
            self.assertAlmostEqual(t["w_eff_C"]["wa"], t["w_eff_A_B"]["wa"], places=12)
            self.assertAlmostEqual(t["w_eff_A_B"]["w0"] - t["w_eff_C"]["w0"], 1.0 / 3.0, places=10)  # 1 - beta/2
        fits = {(f["a4_today"], round(f["a_range"][0], 4)): f for f in s["cplFits"]}
        half, third = fits[(2.0, 0.5)], fits[(2.0, 0.3333)]
        self.assertQuoted(f"over $a \\in [1/2, 1]$, $w_a = {fixed(half['w_eff_C']['wa'], 5)}$ and constant proxy "
                          f"${fixed(half['w_eff_C']['w_const'], 4)}$ under (C)")
        self.assertQuoted(f"over $[1/3, 1]$, $w_a = {fixed(third['w_eff_C']['wa'], 5)}$ and "
                          f"${fixed(third['w_eff_C']['w_const'], 4)}$")
        scan = load_json(EOS_SUMMARY)["mixture_scan"]["C"]["closest"]
        self.assertEqual(scan["distance"], 0.2910614215438)
        self.assertQuoted(f"$({scan['w0']}, {scan['wa']})$ under (C) (distance {scan['distance']}")
        self.assertEqual(load_json(EOS_SUMMARY)["beta"], 4.0 / 3.0)

    def test_condensate_ratio(self):
        u = Fraction(-382, 441)
        self.assertEqual(u / (2 + u), Fraction(-764, 1000))
        cond = load_json(EOS_SUMMARY)["condensate"]
        self.assertAlmostEqual(cond["u_for_ratio_minus_0p764_today"], float(u), places=12)
        self.assertEqual(f"{float(1 + u / 2):.12f}", "0.566893424036")
        # on the history lambda S/m = u ~ e^(-2 a4): wa = -dw/da4 = 4 u/(2 + u)^2, exactly -84231/31250
        self.assertEqual(4 * u / (2 + u) ** 2, Fraction(-84231, 31250))
        self.assertAlmostEqual(cond["ratio_wa_at_that_u"], float(Fraction(-84231, 31250)), places=12)
        self.assertQuoted("$-84231/31250 = -2.695392$")

    def test_dirac16complex00_models(self):
        models = load_json(EOS_THEORY)["models"]

        def row(name, label, wa_digits):
            t, f = models[name]["N2"]["CPL_tangent"], models[name]["N2"]["fit_a_1/2_to_1"]
            wa = fixed(float(t["wa"]), wa_digits)
            if float(t["wa"]) > 0:
                wa = "+" + wa
            return (f"| {label} | {fixed(float(t['w0']), 4)} | {wa} | {fixed(float(f['w0']), 4)} | "
                    f"{fixed(float(f['wa']), 4)} | {fixed(float(f['constant_w']), 4)} | no |")

        m2 = models["M2_positive_good_sector_gas"]
        self.assertEqual(m2["N2_tangent_exact"], {"w0": "-583/3000", "wa": "81037/500000"})
        self.assertEqual(m2["N2"]["CPL_tangent"]["wa"], "0.162074")
        self.assertQuoted(row("M2_positive_good_sector_gas", "M2", 6))
        m3 = models["M3_positive_extra_time_mode"]
        self.assertEqual((m3["N2_tangent_exact"]["w0"], m3["N2_tangent_exact"]["wa"]), ("-287/1000", "-196963/4500000"))
        self.assertQuoted(row("M3_positive_extra_time_mode", "M3", 6))
        self.assertEqual(m3["turning_point_a_star"]["exact"], "(1417/417)^(3/2)")
        self.assertQuoted(f"$a_* = (1417/417)^{{3/2}} = {fixed((1417 / 417) ** 1.5, 4)}$")
        m4 = models["M4_condensate_plus_extra_time_mode"]
        self.assertEqual((m4["parameters"]["s"], m4["parameters"]["Omega_q"]), ("264037/403037", "57963/264037"))
        self.assertQuoted(row("M4_condensate_plus_extra_time_mode", "M4", 6))
        self.assertEqual(m4["min_w_N2_on_(0,1]"], "-0.33280216468")
        self.assertQuoted(f"at $a_* = {fixed(float(m4['turning_point_a_star']), 4)}$ and then grows")
        m5 = models["M5_with_ghost_component"]
        self.assertQuoted(row("M5_with_ghost_component", "M5", 4))
        p = m5["parameters"]
        self.assertEqual(p["G"], "3/10")
        self.assertQuoted(f"$s = {fixed(float(p['s']), 4)}$, $\\Omega_q = {fixed(float(p['Omega_q']), 4)}$, "
                          f"condensate fraction $\\Omega_c = {fixed(float(p['Omega_c']), 4)}$")
        self.assertQuoted(f"its turning point is at $a_* = {fixed(float(m5['turning_point_a_star']), 4)}$")
        self.assertQuoted("$G = 3/10$ of the total at $a = 1$")
        for name in ("M5_with_ghost_component",):
            self.assertEqual(models[name]["N2"]["crossings_of_minus_1_in_[1/3,1]"], [], name)
        for name in ("M2_positive_good_sector_gas", "M3_positive_extra_time_mode",
                     "M4_condensate_plus_extra_time_mode"):
            self.assertEqual(models[name]["N2"]["crossings_of_minus_1_in_[1/3,1]"], [], name)
        m2n1 = models["M2_positive_good_sector_gas"]["N1"]["CPL_tangent"]
        self.assertQuoted(f"tangent $({m2n1['w0']}, {m2n1['wa']})$")

    def test_modes_and_growth(self):
        theory = load_json(EOS_THEORY)["modes"]
        cases = theory["cases"]
        triples = ", ".join(f"({c['m']}, {c['k']}, {c['q']})" for c in cases)
        self.assertEqual(triples, "(3, 4, 0), (5, 0, 3), (4, 4, 4)")
        self.assertQuoted("$(m, k, q) = (3, 4, 0)$, $(5, 0, 3)$ and $(4, 4, 4)$, with $\\omega = \\pm5$, $\\pm4$ "
                          "and $\\pm4$")
        self.assertEqual([c["omega"] for c in cases], ["5", "4", "4"])
        for case in cases:
            for sign in ("omega_pos", "omega_neg"):
                self.assertEqual(case[sign], {"dimension": 8, "krein_signature": [4, 4]})
        growing = theory["growing"]
        self.assertEqual((growing["m"], growing["k"], growing["q"], growing["omega"]), (3, 0, 5, "4 i"))
        self.assertQuoted("$(m, k, q) = (3, 0, 5)$, $\\omega = 4i$")
        numerics = load_json(NUMERICS)
        self.assertEqual(numerics["krein_signed_energy"], {"omega": 1.25, "rho_Q_minus": -1.25, "rho_Q_plus": 1.25})
        self.assertQuoted("at $\\omega = 1.25$ the vectors with $Q = +1$ and $Q = -1$ have $\\rho = +1.25$ and "
                          "$-1.25$")
        growth = numerics["growth"]
        self.assertQuoted(f"$10^{{{growth['log10_amplitude_growth_5.5_to_7.4']:.2f}}}$")
        self.assertQuoted(f"($\\rho/Q$ = {growth['rho_over_Q_at_7.4']!r} at $a = 7.4$")
        self.assertEqual(numerics["settings"]["eps_AH_over_m"], 0.001)
        self.assertQuoted("$H/m = 10^{-3}$")
        self.assertEqual(numerics["models"]["M5_with_ghost_component"]["crossings_N2"], 0)

    def test_implementation_b_invariants(self):
        drift, onshell, residual, deviation = [], [], [], []
        for check in load_json(INDEPENDENT_NUMERICS)["checks"]:
            detail = check["detail"]
            if check["name"].startswith("B_run_"):
                drift.append(float(re.search(r"Krein charge per coordinate volume b4\^\(3/2\) Q: drift ([0-9.e+-]+)",
                                             detail).group(1)))
                onshell.append(float(re.search(r"max \|L0\| \(on shell\) ([0-9.e+-]+)", detail).group(1)))
                residual.append(float(re.search(r"relative residual ([0-9.e+-]+)", detail).group(1)))
            if check["name"].startswith("B_vs_A_M"):
                match = re.search(r"max deviation ([0-9.e+-]+)", detail)
                if match:
                    deviation.append(float(match.group(1)))
        self.assertEqual(len(drift), 6)
        self.assertEqual(f"{max(drift):.7e}", "1.2612134e-13")
        self.assertEqual(f"{max(onshell):.7e}", "1.3322676e-15")
        self.assertEqual(f"{max(residual):.7e}", "4.7810141e-08")
        self.assertEqual(max(deviation), 2.2666232e-05)
        for value in ("drift at most 1.2612134e-13", "at most 1.3322676e-15", "at most 4.7810141e-08",
                      "to within 2.2666232e-05"):
            self.assertQuoted(value)

    def test_branch_required_source(self):
        """The source the author's equations need on a4 = H x4, b4 ~ e^((4/3) H x4) (sections 2.4, 6.1, 9.2, 13.1):
        computed in sympy from the record of the a4 equations and in Wolfram from the author's Lovelock tensors;
        exact arithmetic: it satisfies both conservation identities with b4 (beta = 4/3, constant source)."""
        src = load_json(EOS_THEORY)["condensate"]["branchRequiredSource"]
        rho, p3, pt, p0 = (Fraction(src[k]) for k in ("kappa_rho", "kappa_p3", "kappa_pt", "kappa_p0"))
        self.assertEqual((rho, p3, pt, p0), (Fraction(-2, 27), Fraction(-2, 9), Fraction(-22, 27), Fraction(-14, 27)))
        self.assertEqual(src["kappa_q40"], "0")
        self.assertEqual(-3 * (p3 - pt) - Fraction(3, 2) * Fraction(4, 3) * (rho + pt), 0)   # d rho/dx4 = 0
        self.assertEqual(p3 + pt, 2 * p0)                                                  # the x0 identity
        self.assertIn("{-2/27, -2/9, -22/27, -14/27}", check_detail(WOLFRAM, "D7_branch_required_source"))
        self.assertIn("{0, 4/3}", check_detail(WOLFRAM, "D6_author_weights_branch"))
        self.assertQuoted("which vanishes for a constant $b_4$ and for $\\beta_v = 4/3$")

    def test_exact_fock_variant_of_the_n8_states(self):
        """The negative E of the N = 8, lambda > 0 states is a property of the uniform-gas functional (section 4.7)."""
        with open(EXACT_FOCK, encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row["N"] == "8"]
        self.assertEqual(len(rows), 20)
        largest = max(abs(float(row["E_exact_fock_scf"])) for row in rows)
        self.assertLessEqual(largest, 2.04e-13)
        self.assertEqual(f"{largest:.2e}", "2.04e-13")
        for row in rows:
            if float(row["lambda"]) > 0:
                canonical = float(row["E_uniform_gas"])
                first_order = float(row["E_uniform_gas_plus_deltaE_x"])
                self.assertLess(canonical, 0)
                self.assertLess(first_order, 0)
                self.assertLess(abs(first_order), abs(canonical))
        self.assertQuoted("the same $N = 8$ states have $\\lvert E\\rvert \\leq 2.04 \\times 10^{-13}$")
        self.assertQuoted("still leaves $E < 0$, of smaller magnitude")
        self.assertIn(self.exact_fock_slices_statement(rows), self.text)

    def exact_fock_slices_statement(self, rows):
        """The slices of the exact-Fock N = 8 rows and the equality of E across them, as section 4.7 states them."""
        slices = sorted({float(row["a4"]) for row in rows})
        self.assertEqual(slices, [0.0, 0.5, 1.0, 1.5, 2.0])
        tags = sorted({row["lambda_tag"] for row in rows})
        self.assertEqual(tags, ["lamm1", "lamm2", "lamp1", "lamp2"])
        for tag in tags:
            energies = [row["E_exact_fock_scf"] for row in rows if row["lambda_tag"] == tag]
            self.assertEqual(len(energies), len(slices), tag)
            self.assertEqual(len(set(energies)), 1, f"{tag}: E_exact_fock_scf differs between the slices")
        listed = ", ".join(f"{a:g}" for a in slices)
        return f"(computed at the canonical slices $a_4 = {listed}$, with the same $E$ at each)"

    def test_exact_fock_slices_detect_a_change(self):
        # negative controls: a changed slice list in the text, and a changed E at one slice in the data, are detected
        with open(EXACT_FOCK, encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row["N"] == "8"]
        statement = self.exact_fock_slices_statement(rows)
        self.assertNotIn(statement, self.text.replace("$a_4 = 0, 0.5, 1, 1.5, 2$", "$a_4 = 0, 1, 2$"))
        changed = [dict(row) for row in rows]
        changed[1]["E_exact_fock_scf"] = "-8.125852314700990e-14"
        with self.assertRaises(AssertionError):
            self.exact_fock_slices_statement(changed)
        dropped = [row for row in rows if float(row["a4"]) != 1.5]
        with self.assertRaises(AssertionError):
            self.exact_fock_slices_statement(dropped)

    def test_ks_source_conditions(self):
        data = load_json(KS_SOURCE)
        self.assertEqual(data["summary"], {"checks": 6, "pass": 6, "fail": 0})  # 6 since 2026-10-14 (ks_verdict_holds_for_every_b4)
        self.assertIn("No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source", data["conclusion"])
        self.assertQuoted("No recorded Kohn-Sham state is an admissible source of the author's metric")

    def test_abstract_numbers(self):
        abstract = self.text.split("## Abstract", 1)[1].split("## 1.", 1)[0]
        for value in ("615 instantaneous states", "0.2929 to 0.3183", "0.239626 to 2.268e-03",
                      "-0.040430 and -0.006905", "$\\lambda S/m = -382/441$", "(-0.861, -0.60)", "$w = -0.764$",
                      "1583/1000", "(-2/27, -2/9, -22/27, -14/27)", "closest distance 0.291"):
            self.assertIn(value, abstract, value)
        self.assertEqual(len(load_json(KS_HISTORY)["slices"]) * 15, 615)


if __name__ == "__main__":
    unittest.main()
