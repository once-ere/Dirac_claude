#!/usr/bin/env python3
"""Publication test for Revision/docs/DARK_SECTOR_HYPOTHESES.{md,tex,pdf}.

The document is deliverable 5 of Revision/SPEC.md section 10: the two hypotheses of SPEC section 8
(Hypothesis for dirac16complex, Hypothesis00 for dirac16complex00), the lead's analysis of SPEC
section 11 checked point by point, the observer assumption for rho_4 with the definitions (A), (B),
(C), the method, the results for each field, the comparison with the Supernovae Unite values, the
verdicts and what remains open.  Since phase W7 (2026-10-17) every result is for the CORRECTED
metric of 2026-10-16 (version 2, SPEC section 1): g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1,
-e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real, b4 a function of x4 (never 1), the fold
cos z = 0 at y = 0 joining the two halves of a cell (no Z2 orbifold); the history a4 = H x4,
b4 = b4(0) e^((4/3) H x4) is a PRESCRIBED background.  The metric of 2026-10-14 (with b4(x4) and the
sin^{1/3} z factors) is withdrawn; its Wolfram record wolfram-dark-sector-b4.json may be named only as
that record, and no number or check of it may be cited.  It is built and registered with

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
    an established physical state, the observer normalisation is an ASSUMPTION, the history is a
    PRESCRIBED background, neither hypothesis is established), overclaims and statements of the
    withdrawn metric are absent (with negative controls), the author's coordinates x0..x7 are used
    and the extra times are never called static or frozen;
  * every check name the document cites exists in a Revision report of the corrected metric with the
    verdict PASS (the withdrawn Wolfram twin is not citable), and every check of the seven
    dark-sector reports (the Wolfram verification of the corrected metric included) is listed
    (complete verification records);
  * the report-count table equals the counts recomputed from the reports;
  * every number quoted in the document is read from its JSON report: either it occurs verbatim
    in the detail of the named check, or it is the stated rounding of the named JSON value, or it
    follows from them by exact arithmetic recomputed here;
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

MARKDOWN_SHA256 = "134711d3827b4872d4af7fa67f096065aec1089f95f4498f1596fd654c5ef428"
TEX_SHA256 = "dc0c830e11a4cf53b435f3a7171e69f8852cac9e7d76d131f3706e269be97e0a"

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
# The Wolfram verification of the corrected metric (7 checks) and the record of the withdrawn metric of 2026-10-14.
WOLFRAM = DARK / "reports" / "wolfram-dark-sector.json"
WOLFRAM_B4 = DARK / "reports" / "wolfram-dark-sector-b4.json"
AUTHOR_INPUTS = DARK / "reports" / "author-notebook-inputs.json"
KS_SOURCE = REVISION / "field_equations_a4" / "reports" / "ks-source-conditions.json"
A4_EQUATIONS = REVISION / "field_equations_a4" / "a4-equations.json"
KS_THEORY = REVISION / "kohn_sham" / "ks-theory.json"
KS_CROSSCHECK = REVISION / "kohn_sham" / "reports" / "ks-crosscheck.json"
EXACT_FOCK = REVISION / "kohn_sham" / "results" / "exx" / "exact-fock-variant.csv"

# The seven dark-sector reports of the corrected metric, every check of which the document lists (section 11.2).
DARK_REPORTS = (DERIVATION, KS_HISTORY, EOS_CHECKS, INDEPENDENT, DERIVE_EOS, INDEPENDENT_NUMERICS, WOLFRAM)
# The reports of the count table (section 11.1), in the order of the table.
COUNTED_REPORTS = (
    "Revision/dark_sector/dirac16complex/reports/derivation-checks.json",
    "Revision/dark_sector/dirac16complex/reports/ks-history-run.json",
    "Revision/dark_sector/dirac16complex/reports/eos-checks.json",
    "Revision/dark_sector/dirac16complex/reports/independent-checks.json",
    "Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json",
    "Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json",
    "Revision/dark_sector/reports/wolfram-dark-sector.json",
    "Revision/field_equations_a4/reports/ks-source-conditions.json",
)
# Every report whose check names the document may cite (the corrected metric only).
CITABLE_REPORT_GLOBS = (
    "dark_sector/dirac16complex/reports/*.json",
    "dark_sector/dirac16complex00/reports/*.json",
    "dark_sector/reports/*.json",
    "field_equations_a4/reports/ks-source-conditions.json",
)
# The record of the withdrawn metric of 2026-10-14: named as that record only, never cited for a check.
WITHDRAWN_REPORTS = ("dark_sector/reports/wolfram-dark-sector-b4.json",)

TITLE = ("Dark-sector hypotheses for dirac16complex and dirac16complex00: the equation of state seen "
         "from 3-space")
SUBTITLE_START = ("Hypothesis and Hypothesis00 investigated in the author's primordial gravitational field "
                  "with exponentially deflating extra times, in the corrected metric of 2026-10-16 (version 2) "
                  "with the two functions $a_4(x_4)$ and $b_4(x_4)$")
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
    r"$w_{\rm eff} = P_3/E + (\beta/2 - 1)(P_0 + 3P_t)/(3E) - s\,(4 - 2\beta)/3$ with $\beta = d\ln b_4/da_4$",
    "every verdict moves by exactly $-4/9$ between (A, B) and (C)",
    "$x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE exponentially",
    "$b_4$ is a function of $x_4$, and every result below is computed with it",
    "The history is therefore a PRESCRIBED BACKGROUND for test fields.",
    "the field equations of the corrected metric do not select it",
    "it grows with $x_4$, it satisfies the conservation identity of section 3.1 exactly",
    "the corrected metric has no $Z_2$ orbifold and no mirror copy carrying $-m$",
    "the fold $\\cos z = 0$ at $y = 0$ joins the two halves of a cell, and $y = -L$ is the tip",
    "the hidden direction has the scale factor $e^{-a_4}b_4^{1/2}\\lvert\\cot z\\rvert$: it shrinks with the "
    "extra times",
    "both CHOSEN on the withdrawn record to solve tangent $= (-0.861, -0.60)$",
    "On the withdrawn record the M4 tangent and the M5 fit equal the Unite pair by construction.",
    "so $w_0 = -0.861$ needs $G \\geq 3749/3000$",
    "(the negative control: the form without the terms of the hidden direction and the extra times fails)",
    "NOT FOUND in the computed states",
    "2. dirac16complex, dark matter: not found.",
    "does not show the dust-like law",
    "Positive-energy extra-time momentum does NOT supply it",
    "In this convention thawing means $w_a < 0$",
    "$w_{\\rm exp} = -1$ exactly",
    "so it is not the supernova constant-$w$ fit -0.764, which weights the data",
    "No supernova likelihood, distance fit or covariance is computed anywhere in this record.",
    "This value of $\\lambda S/m$ is CHOSEN to give -0.764: one parameter tuned to one number.",
    "Under (C) this CHOSEN condensate lies near the Unite $w_0$, with a slope steeper than the Unite "
    "$w_a = -0.60$: a tuned value, not a prediction.",
    "2. Any Unite value as an output of the field equations: no positive-energy mode gas reaches them on the "
    "history, a condensate matches a single Unite number only with a CHOSEN $\\lambda S/m$ and never the pair",
    "Negative $E$ is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record",
    "This negative $E$ is therefore a property of the approximate functional; good-sector states with "
    "$E < 0$ are not established beyond it.",
    "no condensate is it",
    "in the positive realisation of the good sector (with the ASSUMED filling of both fold conditions",
    "crosses $-1$ on $[1/3, 1]$?",
    "it is kept so that the withdrawn record stays reproducible",
    "no number or check of this document comes from it",
    "No script was re-run for this document",
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
    # w >= -4/9 for M3 and M4 holds only before the turning point a_* of their extra-time mode
    r"\b(?:M3|M4)\b[^.]*\bnever\s+crosses\s+\$?-1",
    r"\bthawing\b[^.;]*\$w\s*\\geq\s*-1\$\s+at\s+every\s+\$a\$",
    # negative E is not specific to the Krein sector (the N = 8, lambda > 0 good-sector states have E < 0)
    r"otherwise\s+\$E\s*<\s*0\$,\s+the\s+negative-norm",
    # the Einstein linear-member ratio is phantom only for kappa * rho > 0
    r"\$w\s*<\s*-1\$\s+for\s+\$\\rho\s*>\s*0\$",
    # negative E of the N = 8 states is a property of the canonical uniform-gas functional (exact Fock: |E| <= 4.98e-12)
    r"not\s+specific\s+to\s+a\s+negative-norm\s+\(Krein\)\s+sector\s*:",
    # kappa > 0 and rho > 0 on the linear member need Lambda < -(21 + 3 A^2) H^2; it is no bare example
    r"e\.g\.\s+for\s+\$\\kappa\s*>\s*0\$\s+and\s+\$\\rho\s*>\s*0\$",
    # the corrected metric (2026-10-16): the history needs a source that GROWS with x4 (the withdrawn record had a
    # constant one)
    r"\bconstant\s+source\b",
    # the fold joins the two halves of a cell: no Z2 orbifold, no mirror copy carrying -m
    r"(?<!no )\bmirror\s+copy\s+carrying\b",
    r"\bZ_?2\$?\s+(?:brane|orbifold)\s+(?:at|of)\b",
    # the bulk band is blue-shifted by the shrinking hidden direction: no dust-like law
    r"\bbulk\s+band\s+(?:shows|has|follows|gives)\s+the\s+(?:dark-matter-like|dust-like)\b",
    # the shift between (A, B) and (C) is -(4 - 2 beta)/3 = -4/9 on the history (the withdrawn record had -1/3)
    r"\bmoves\s+by\s+exactly\s+\$-1/3\$",
    # z = 6 H x0 takes every real value in the corrected metric
    r"z\s*=\s*6Hx_0\s*\\in\s*\(0,\s*\\pi/2\)",
    # the extra times deflate exponentially; never static or frozen
    r"\bextra\s+times?\b[^.]*\b(?:static|frozen)\b",
    # no overclaim about pair creation
    r"\buniverses\s+are\s+created\s+in\s+pairs\b",
)
# Numbers and statements of the withdrawn metric of 2026-10-14 that must not occur in the document any more.
WITHDRAWN_MARKERS = (
    "1583/1000", "1583/2583", "-84231/31250", "-2.695392", "-2/27", "-22/27", "-14/27", "0.239626", "2.268e-03",
    "-0.040541", "-0.006532", "0.2910614215438", "-0.333015", "-0.33280216468", "-0.194333333333", "6.351e-06",
    "1.630e+00", "2.04 \\times 10^{-13}", "2.12 \\times 10^{-13}", "0.9307", "0.6581", "brane band",
    "brane zero mode", "Z2 brane", "b_4^{3/2}\\cos z", "N = 688", "N = 136", "\\sin^{1/3}", "\\sin^{1/6}z",
    "$X = P_3 - P_t$", "X/E", "\\frac34(b_4'/b_4)", "-1 + \\beta/2",
)
FILE_SUFFIXES = (".json", ".py", ".wls", ".wl", ".md", ".tex", ".pdf", ".rs", ".csv", ".toml", ".nb", ".sh")


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


def citable_report_paths() -> list[Path]:
    withdrawn = {(REVISION / relative).resolve() for relative in WITHDRAWN_REPORTS}
    paths = []
    for pattern in CITABLE_REPORT_GLOBS:
        for path in sorted(REVISION.glob(pattern)):
            if path.resolve() not in withdrawn:
                paths.append(path)
    return paths


def report_checks() -> dict[str, list[str]]:
    """Check name -> list of verdicts (upper case) over every citable Revision report."""
    verdicts: dict[str, list[str]] = {}
    for path in citable_report_paths():
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


def polynomial(text: str):
    """An exact polynomial in kk from a record string such as '-9*kk**2/16 + 161*kk/24 + 121/432' (or with ^)."""
    expression = re.sub(r"(\d+)", r"F(\1)", text.replace("^", "**"))
    if not re.fullmatch(r"[F()\d\s+\-*/k]*", expression):
        raise ValueError(text)
    return lambda kk: eval(expression, {"__builtins__": {}}, {"F": Fraction, "kk": kk})  # noqa: S307


def quadratic_coefficients(function) -> tuple[Fraction, Fraction, Fraction]:
    """(c2, c1, c0) of a polynomial of degree <= 2, verified at a fourth point."""
    c0 = function(Fraction(0))
    c1 = (function(Fraction(1)) - function(Fraction(-1))) / 2
    c2 = (function(Fraction(1)) + function(Fraction(-1))) / 2 - c0
    if function(Fraction(3)) != 9 * c2 + 3 * c1 + c0:
        raise AssertionError("degree above 2")
    return c2, c1, c0


def render_quadratic(coefficients: tuple[Fraction, Fraction, Fraction]) -> str:
    """The LaTeX form of the document: -\\tfrac{9}{16}\\xi^2 + \\tfrac{161}{24}\\xi + \\tfrac{121}{432}."""
    parts = []
    for power, c in zip((2, 1, 0), coefficients):
        if c == 0:
            continue
        magnitude = abs(c)
        number = (f"\\tfrac{{{magnitude.numerator}}}{{{magnitude.denominator}}}" if magnitude.denominator != 1
                  else str(magnitude.numerator))
        term = number + ("\\xi^2" if power == 2 else "\\xi" if power == 1 else "")
        if not parts:
            parts.append(("-" if c < 0 else "") + term)
        else:
            parts.append(("- " if c < 0 else "+ ") + term)
    return " ".join(parts)


# Numbers quoted verbatim from the detail of a named check: (report, check, substrings).  Each
# substring must occur in the check's detail AND in the document.
DETAIL_NUMBERS = (
    (DERIVATION, "condensate_ratio_equal_unite_constant_w", ("-382/441", "-0.866213151927", "0.566893424036")),
    (DERIVATION, "mixture_C_matching_w0_unite", ("(417/2000, 1417/2000]", "(0.208500, 0.708500]", "[-4/9, -1/9)")),
    (DERIVATION, "unite_deep_past", ("-1.461",)),
    (KS_HISTORY, "all_runs_succeeded", ("615 runs (15 series x 41 slices)",)),
    (KS_HISTORY, "committed_slices_equal_committed_record", ("300 integrals", "0.000e+00")),
    (KS_HISTORY, "lambda0_series_exact_fold_band", ("123 states", "2.333e-15")),
    (KS_HISTORY, "cell_volume_follows_b4", ("4.441e-16",)),
    (KS_HISTORY, "lambda_eff_form_agrees", ("48 states", "8.159e-13")),
    (KS_HISTORY, "occupied_labels_fixed_along_history", ("15 of 15",)),
    (KS_HISTORY, "y_conservation_every_state", ("5.751e-10",)),
    (KS_HISTORY, "particle_number_every_state", ("2.554e-15",)),
    (EOS_CHECKS, "conservation_identity", ("(h = 0.05)", "2.103e-06")),
    (EOS_CHECKS, "conservation_integrated_simpson", ("2.208e-07",)),
    (EOS_CHECKS, "derivative_two_ways", ("1.410e-06",)),
    (EOS_CHECKS, "free_gas_exact_fold_band", ("7.8e-16", "3.1e-15")),
    (EOS_CHECKS, "interacting_gas_ranges",
     ("[0.330585, 0.336132]", "[-0.113860, -0.108312]", "[-3.240e-02, 3.024e-02]", "[-1.192e-01, 1.114e-01]")),
    (EOS_CHECKS, "n8_interacting_states", ("[0.948351, 0.998955]", "[0.232167, 0.408203]")),
    (EOS_CHECKS, "condensate_drifts", ("-2.246160", "-0.424444", "-0.868889", "-1.247867")),
    (EOS_CHECKS, "mixture_C_cannot_reach_unite_w0_with_lambda0_condensate", ("-0.444111",)),
    (EOS_CHECKS, "mixture_scan_three_definitions",
     ("0.5443135585304", "0.5861919480853", "0.1604394909208", "-0.7055555555556", "-0.6397222222222",
      "-1.779879740253", "-0.8286111111111", "-3.136", "-2.159381216106", "-4.447785313931", "-3.006388888889")),
    (EOS_CHECKS, "gas_cpl_far_from_unite", ("[-0.003892, 0.003904]", "[-0.002392, 0.002261]", "[-0.113860, -0.108312]")),
    (INDEPENDENT, "exact_k0_spectra", ("n = 96", "4.086e-14", "1.292292828069")),
    (INDEPENDENT, "fold_band_dispersion", ("4.58e-14", "5.55e-15")),
    (INDEPENDENT, "collocation_converged", ("1.05e-14",)),
    (INDEPENDENT, "energy_vs_rust_solver", ("82 states", "3.568e-13")),
    (INDEPENDENT, "w_eff_vs_primary", ("1.220e-13",)),
    (INDEPENDENT, "free_gas_w_eff_one_third", ("1.23e-13",)),
    (INDEPENDENT, "cpl_tangent_vs_primary", ("2.737e-11",)),
    (INDEPENDENT, "bulk_band_w_eff", ("0.318721", "-0.081074", "2.7183", "0.2636")),
    (INDEPENDENT, "fold_band_radiation_law", ("2.87e-12",)),
    (DERIVE_EOS, "condensate_ratio_equals_unite_constant_w", ("-382/441",)),
    (DERIVE_EOS, "condensate_phantom_interval", ("(-2, -1)",)),
    (DERIVE_EOS, "unite_line_fit_proxy", ("-1.011", "-1.061")),
    (DERIVE_EOS, "unite_crossing_point", ("461/600", "139/461")),
    (DERIVE_EOS, "condensate_ratio_drift_at_unite_value", ("-28077/12500", "-2.24616", "-1.24786666667")),
    (DERIVE_EOS, "M2_tangent_exact", ("417/1000", "-2749/9000", "81037/500000")),
    (DERIVE_EOS, "M3_tangent_exact", ("417/1417", "-3583/9000", "-196963/4500000")),
    (DERIVE_EOS, "M4_former_tuning_on_the_history", ("264037/403037", "57963/264037", "-0.443913275792")),
    (DERIVE_EOS, "positive_models_bounded_by_minus_four_ninths",
     ("-0.305444444444", "-0.443709979885", "-0.443913275792")),
    (DERIVE_EOS, "unite_w0_requires_dominant_ghost", ("3749/3000", "3749/6749")),
    (DERIVE_EOS, "M5_former_composition_on_the_history", ("-0.443790594178", "-0.32308292878")),
    (INDEPENDENT_NUMERICS, "B_solve_M3_s", ("0.29428947", "0.2942837")),
    (INDEPENDENT_NUMERICS, "B_positive_models_bounded", ("-0.42931652",)),
    (INDEPENDENT_NUMERICS, "B_growth_rate", ("6.2639848", "0.30909994", "0.3118201")),
    (INDEPENDENT_NUMERICS, "B_condensate_dilutes", ("9.8449027e-14", "0.87800024")),
    (INDEPENDENT_NUMERICS, "B_dilution_equals_formula_M2", ("2.7779535e-05",)),
    (INDEPENDENT_NUMERICS, "B_ghost_negative_energy", ("-0.11509411",)),
    (INDEPENDENT_NUMERICS, "B_vs_A_M5_crossing", ("67 points",)),
    (INDEPENDENT_NUMERICS, "B_superposition_average", ("0.27738092",)),
    (KS_SOURCE, "ks_history_is_a_prescribed_background", ("3.57407", "-7.63383")),
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

    def test_corrected_metric_and_author_coordinates(self):
        """The corrected metric (version 2) in the author's coordinates x0..x7; the extra times deflate."""
        for statement in (
            "e^{-2a_4(x_4)}\\,b_4(x_4)\\cot^2 z\\,dx_0^2 + e^{2a_4(x_4)}\\big(dx_1^2+dx_2^2+dx_3^2\\big) - dx_4^2",
            "- e^{-2a_4(x_4)}\\,b_4(x_4)\\,(\\sin^2 z)^{1/6}\\,\\big(dx_5^2+dx_6^2+dx_7^2\\big)",
            "$\\sqrt{|g|} = e^{-a_4}b_4^2\\lvert\\cot z\\rvert\\,\\lvert\\sin z\\rvert^{1/2}$",
            "$x_0, x_1, \\dots, x_7$",
            "`X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}`",
            "with $z = 6Hx_0$ real (every real value)",
            "$\\gamma^\\mu\\Omega_\\mu = \\frac32He^{a_4}b_4^{-1/2}\\gamma^{(x_0)} + (b_4'/b_4 - \\frac12a_4')\\gamma^{(x_4)}$",
        ):
            self.assertIn(statement, self.text, statement)
        # the records state the same metric, volume element and fold
        self.assertIn("e^(-a4) b4^2 |cot z| |sin z|^(1/2)", check_detail(DERIVATION, "sqrt_det_g"))
        for path in (DERIVATION, KS_HISTORY, WOLFRAM):
            self.assertIn("the corrected primordial metric of 2026-10-16 (version 2", load_json(path)["metric"])
        fold = load_json(KS_THEORY)["boundaryConditions"]["fold"]["statement"]
        self.assertIn("the fold cos z = 0 joins the two halves of a cell", fold)
        self.assertIn("the same chi(y) on both halves", fold)
        authors = load_json(AUTHOR_INPUTS)
        self.assertEqual((authors["cellCount"], authors["inputCellCount"]), (147, 113))
        self.assertIn("147 cells, 113 input cells", self.text)
        # never the labelling x1..x8 or x8, never static or frozen extra times
        self.assertIsNone(re.search(r"x_\{?8\b|\bx8\b|x_1,\s*\\dots,\s*x_8", self.text))
        self.assertIsNone(re.search(r"(?i)\b(?:static|frozen)\b", self.text))
        self.assertGreaterEqual(len(re.findall(r"deflat", self.text)), 8)

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
        # the closest point to the Unite pair is a pure condensate with a CHOSEN ratio
        self.assertIn("the pure condensate with $w_c = -0.47$ today, gas fraction 0, CHOSEN", self.text)

    def test_no_overclaims(self):
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)
        self.assertNotRegex(self.text, r"(?<!never )\bproved that\b")

    def test_no_statement_of_the_withdrawn_metric(self):
        """No number or statement of the withdrawn metric of 2026-10-14 is quoted, and no check of its record is
        cited; the twin is named only as the record of the withdrawn metric."""
        for marker in WITHDRAWN_MARKERS:
            self.assertNotIn(marker, self.text, marker)
        cited = set(cited_check_names(self.text))
        current = set(report_checks())
        withdrawn_only = {check["name"] for check in load_json(WOLFRAM_B4)["checks"]} - current
        self.assertTrue(withdrawn_only)
        self.assertFalse(cited & withdrawn_only, sorted(cited & withdrawn_only))
        self.assertEqual((load_json(WOLFRAM_B4)["checkCount"], load_json(WOLFRAM_B4)["failedCount"]), (8, 0))
        self.assertIn("Its twin `verify_dark_sector_b4.wls` (`Revision/dark_sector/reports/wolfram-dark-sector-b4.json`, "
                      "8 checks) is the Wolfram record of the withdrawn metric of 2026-10-14", self.text)
        # the twin is mentioned nowhere else
        self.assertEqual(self.text.count("wolfram-dark-sector-b4.json"), 1)
        # a b4 check name (withdrawn record) would be rejected by the citation test
        self.assertNotIn("D7_branch_required_source", report_checks())

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
            "On this history the author's equations then require the constant source of section 2.4.",
            "The brane has a mirror copy carrying $-m$.",
            r"with the ASSUMED $Z_2$ brane at $z = \pi/2$",
            "The massive bulk band shows the dark-matter-like law.",
            "On the history every verdict moves by exactly $-1/3$ between (A, B) and (C).",
            r"with $z = 6Hx_0 \in (0,\pi/2)$",
            "In this computation the extra times are static.",
            "Universes are created in pairs.",
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
        # the markers of the withdrawn metric are detected in a stale sentence
        stale = "w_eff(C) between -0.040541 and -0.006532 on the brane band of N = 688"
        self.assertTrue(any(marker in stale for marker in WITHDRAWN_MARKERS))

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
        for name in (check["name"] for check in load_json(KS_SOURCE)["checks"]):
            self.assertIn(name, cited, f"{name} of {KS_SOURCE.name}")
        headers = (
            ("**dirac16complex, derive_effective.py**", DERIVATION),
            ("**dirac16complex, run_ks_history.py**", KS_HISTORY),
            ("**dirac16complex, compute_eos.py**", EOS_CHECKS),
            ("**dirac16complex, independent_free_gas.py**", INDEPENDENT),
            ("**dirac16complex00, derive_eos.py (A)**", DERIVE_EOS),
            ("**dirac16complex00, independent_numerics.py (B)**", INDEPENDENT_NUMERICS),
            ("**dark sector, verify_dark_sector.wls (Wolfram)**", WOLFRAM),
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
        self.assertEqual(load_json(DERIVATION)["summary"], {"total": 37, "pass": 37, "fail": 0})
        self.assertEqual(load_json(KS_HISTORY)["summary"], {"total": 8, "pass": 8, "fail": 0})
        self.assertEqual(load_json(EOS_CHECKS)["summary"], {"total": 13, "pass": 13, "fail": 0})
        self.assertEqual(load_json(INDEPENDENT)["summary"], {"total": 10, "pass": 10, "fail": 0})
        self.assertEqual(load_json(DERIVE_EOS)["summary"], "48/48 checks pass")
        self.assertEqual(load_json(INDEPENDENT_NUMERICS)["summary"], "32/32 checks pass")
        self.assertEqual((load_json(WOLFRAM)["checkCount"], load_json(WOLFRAM)["failedCount"]), (7, 0))
        self.assertEqual(load_json(WOLFRAM)["producer"], "Revision/dark_sector/wolfram/verify_dark_sector.wls")
        self.assertIn("37 of 37, 8 of 8, 13 of 13, 10 of 10, 48 of 48, 32 of 32 and 7 of 7 checks passed", self.text)
        for line in ("37/37 checks pass", "13/13 checks pass", "10/10 checks pass", "derive_eos: 48/48 checks pass",
                     "independent_numerics: 32/32 checks pass", "7/7 checks passed"):
            self.assertIn(line, self.text, line)


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

    def test_observer_shift_and_weights(self):
        """The shift -(4 - 2 beta)/3 and the weight beta/2 - 1 of the hidden and extra-time pressures at beta = 4/3."""
        beta = Fraction(4, 3)
        self.assertEqual(load_json(EOS_SUMMARY)["beta"], 4.0 / 3.0)
        self.assertEqual(load_json(KS_THEORY)["adiabaticity"]["historyBeta"], "4/3")
        self.assertEqual((4 - 2 * beta) / 3, Fraction(4, 9))
        self.assertEqual(beta / 2 - 1, Fraction(-1, 3))
        self.assertEqual((2 * beta - 1) / 3, Fraction(5, 9))
        self.assertEqual(2 * beta - 1, Fraction(5, 3))     # Vol_7 ~ e^((5/3) a4), S ~ e^(-(5/3) a4)
        self.assertEqual(1 - beta / 2, Fraction(1, 3))     # q_p, l_p ~ a^(1/3)
        self.assertEqual(Fraction(1, 3) - Fraction(4, 9), Fraction(-1, 9))   # the fold band under (C)
        formulas = load_json(D16 / "outputs" / "effective-formulas.json")["wEff"]
        self.assertEqual(formulas["general"], "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3")
        self.assertEqual(formulas["atBeta4over3"], {"A": "P3/E - (P0 + 3 Pt)/(9E)", "C": "A - 4/9"})
        self.assertIn("w_eff(A) - 4/9", check_detail(DERIVATION, "w_eff_C"))
        self.assertIn("w_eff(N1) - 4/9 on the history beta = 4/3", check_detail(DERIVE_EOS, "observer_N2_weff_identity"))
        self.assertQuoted("$w_{\\rm eff}(C) = w_{\\rm eff}(A) - 4/9$: every verdict moves by exactly $-4/9$")
        self.assertQuoted("a value $w_{\\rm eff}(C) < -1$ needs $P_3/E - (P_0 + 3P_t)/(9E) < -5/9$")
        self.assertIn("P3/E - (P0 + 3 Pt)/(9E) < -5/9", check_detail(DERIVATION, "phantom_condition"))
        self.assertIn("P0 > 9 E (P3/E + 5/9)", check_detail(DERIVATION, "phantom_condition"))
        self.assertQuoted("$P_0 > 9E(P_3/E + 5/9)$")

    def test_kohn_sham_history_setup(self):
        self.assertIn("every occupied orbital is the fold-band orbital (e^(f M y), 0) with eps = e^(-a4) |k|",
                      check_detail(KS_HISTORY, "lambda0_series_exact_fold_band"))
        self.assertQuoted("every occupied orbital is the fold-band orbital $(e^{fMy}, 0)$ with "
                          "$\\varepsilon = e^{-a_4}\\lvert k\\rvert$")
        report = load_json(KS_HISTORY)
        slices = report["slices"]
        self.assertEqual((len(slices), slices[0], slices[-1]), (41, 0.0, 2.0))
        self.assertEqual(len(slices) * 15, 615)
        self.assertQuoted("at the 41 slices $a_4 = 0, 0.05, \\dots, 2$ for $N = 8, 592, 2352$")
        self.assertIn("H = m = 1, L = 3, theta = 0", report["solver"])
        self.assertQuoted("with $H = m = 1$, $L = 3$, tip $\\theta = 0$, $T = 0$")
        self.assertIn("Vol_7(a4) = ell^3 v_t e^((5/3) a4)", report["coupling"])
        self.assertIn("f = e^(-a4/3)", report["coupling"])
        self.assertQuoted("$\\mathrm{Vol}_7(a_4) = \\ell^3v_te^{(5/3)a_4}$")
        self.assertQuoted("$\\lambda_{\\rm eff} = \\hat\\lambda\\,e^{-(5/3)a_4}$")
        lam = {entry["series"]: entry["lambda"] for entry in load_json(EOS_SUMMARY)["series"]}
        l1 = ", ".join(f"{lam[f'N{n}_lamp1']:g}" for n in (8, 592, 2352))
        l2 = ", ".join(f"{lam[f'N{n}_lamp2']:g}" for n in (8, 592, 2352))
        self.assertEqual((l1, l2), ("157.7, 2.131, 0.5363", "473.1, 6.393, 1.609"))
        for n in (8, 592, 2352):
            self.assertEqual(lam[f"N{n}_lamm1"], -lam[f"N{n}_lamp1"])
            self.assertEqual(lam[f"N{n}_lamm2"], -lam[f"N{n}_lamp2"])
            self.assertEqual(lam[f"N{n}_lam0"], 0.0)
        self.assertQuoted(f"$\\lambda_1 = {l1}$ and $\\lambda_2 = {l2}$ for $N = 8, 592, 2352$")

    def test_kohn_sham_gas_series(self):
        summary = load_json(EOS_SUMMARY)
        self.assertEqual(summary["zeroSeries"], ["N8_lam0"])
        self.assertIn("E = P3 = Pt = P0 = 0 at every slice", series("N8_lam0")["status"])
        entries = [entry for entry in summary["series"] if "w_eff_A_B_range" in entry]
        self.assertEqual(len(entries), 14)
        lowest = min(entries, key=lambda entry: entry["w_eff_C_range"][0])
        self.assertEqual(lowest["N"], 8)
        self.assertQuoted("the smallest $w_{\\rm eff}(C)$ of the 14 series with $E \\neq 0$ is "
                          f"{fixed(lowest['w_eff_C_range'][0], 6)} ($N = 8$)")
        # the free gas: an exact fold-band gas
        for name in ("N592_lam0", "N2352_lam0"):
            s = series(name)
            for values, exact in ((s["w_eff_A_B_range"], 1 / 3), (s["w_eff_C_range"], -1 / 9),
                                  (s["ratio_w3_range"], 1 / 3)):
                for value in values:
                    self.assertAlmostEqual(value, exact, places=12)
            self.assertEqual(s["ratio_wt_range"], [0.0, 0.0])
            self.assertLess(max(abs(x) for x in s["ratio_wx0_range"]), 1e-15)
            for tangent in s["cplTangent"]:
                self.assertAlmostEqual(tangent["w_eff_C"]["w0"], -1 / 9, places=12)
                self.assertLess(abs(tangent["w_eff_C"]["wa"]), 1e-12)
        self.assertQuoted("$w_{\\rm eff}(A) = w_{\\rm eff}(B) = 1/3$ exactly (radiation-like, with no time variation")
        self.assertQuoted("$w_{\\rm eff}(C) = 1/3 - 4/9 = -1/9$ and $w_a = 0$")
        # the interacting gas (N = 592, 2352): the rounding of the JSON ranges equals the check detail
        inter = [entry for entry in entries if entry["N"] in (592, 2352) and entry["lambda"] != 0.0]
        self.assertEqual(len(inter), 8)
        self.assertTrue(all(entry["sign_of_E"] == "positive" for entry in inter))
        a_lo = fixed(min(e["w_eff_A_B_range"][0] for e in inter), 6)
        a_hi = fixed(max(e["w_eff_A_B_range"][1] for e in inter), 6)
        c_lo = fixed(min(e["w_eff_C_range"][0] for e in inter), 6)
        c_hi = fixed(max(e["w_eff_C_range"][1] for e in inter), 6)
        w_lo = fixed(min(e["ratio_w3_range"][0] for e in inter), 6)
        w_hi = fixed(max(e["ratio_w3_range"][1] for e in inter), 6)
        detail = check_detail(EOS_CHECKS, "interacting_gas_ranges")
        self.assertIn(f"w_eff(A) in [{a_lo}, {a_hi}]", detail)
        self.assertIn(f"w_eff(C) = w_eff(A) - 4/9 in [{c_lo}, {c_hi}]", detail)
        self.assertQuoted(f"| interacting Kohn-Sham gas, $N = 592, 2352$ (section 5.2) | {a_lo} to {a_hi} | "
                          f"{c_lo} to {c_hi} | {w_lo} to {w_hi} |")
        self.assertQuoted(f"The ratio $w_3 = P_3/E$ lies in [{w_lo}, {w_hi}]")
        # N = 8 with lambda != 0
        n8 = [entry for entry in entries if entry["N"] == 8]
        self.assertEqual(len(n8), 4)
        for entry in n8:
            self.assertEqual(entry["ratio_w3_range"], entry["ratio_wt_range"])           # P3 = Pt
            self.assertEqual(entry["sign_of_E"], "negative" if entry["lambda"] > 0 else "positive")
        self.assertEqual((fixed(min(e["w_eff_A_B_range"][0] for e in n8), 6),
                          fixed(max(e["w_eff_A_B_range"][1] for e in n8), 6)), ("0.232167", "0.408203"))
        x_lo = fixed(min(e["ratio_wx0_range"][0] for e in n8), 6)
        x_hi = fixed(max(e["ratio_wx0_range"][1] for e in n8), 6)
        self.assertQuoted(f"the hidden-direction ratio $P_0/E$ lies in [{x_lo}, {x_hi}]")
        self.assertQuoted(f"$P_0/E$ in [{x_lo}, {x_hi}] for $N = 8$")
        n_lo = fixed(min(e["w_eff_C_range"][0] for e in n8), 6)
        n_hi = fixed(max(e["w_eff_C_range"][1] for e in n8), 6)
        self.assertQuoted(f"$w_{{\\rm eff}}(C) = w_{{\\rm eff}}(A) - 4/9$ lies in [{n_lo}, {n_hi}]")
        self.assertQuoted(f"$w_{{\\rm eff}}(C)$ between {n_lo} and {n_hi}")
        self.assertQuoted(f"have $w_{{\\rm eff}}(C) \\geq {n_lo}$")
        self.assertIn("E has the sign of -lambda at every slice: True", check_detail(EOS_CHECKS, "n8_interacting_states"))
        self.assertQuoted("$E$ has the sign of $-\\lambda$ at every slice")

    def test_cpl_tangent_and_fit_table(self):
        s = series("N2352_lamp1")
        tangents = {t["a4_today"]: t for t in s["cplTangent"]}
        self.assertEqual(sorted(tangents), [0.5, 1.0, 1.5, 2.0])
        w0 = " | ".join(fixed(tangents[a]["w_eff_C"]["w0"], 4) for a in (0.5, 1.0, 1.5, 2.0))
        wa = " | ".join(fixed(tangents[a]["w_eff_C"]["wa"], 6) for a in (0.5, 1.0, 1.5, 2.0))
        self.assertQuoted("CPL tangents of the interacting series $N = 2352$, $\\hat\\lambda = +\\lambda_1$:")
        self.assertQuoted(f"| $w_0$ under (C) | {w0} |")
        self.assertQuoted(f"| $w_a$ (every definition) | {wa} |")
        for a in (0.5, 1.0, 1.5, 2.0):
            t = tangents[a]
            self.assertAlmostEqual(t["w_eff_C"]["wa"], t["w_eff_A_B"]["wa"], places=12)
            self.assertAlmostEqual(t["w_eff_A_B"]["w0"] - t["w_eff_C"]["w0"], 4.0 / 9.0, places=10)  # (4 - 2 beta)/3
        self.assertQuoted("($w_0$ under (A), (B) is $w_0(C) + 4/9$.)")
        fits = {(f["a4_today"], round(f["a_range"][0], 4)): f for f in s["cplFits"]}
        half, third = fits[(2.0, 0.5)], fits[(2.0, 0.3333)]
        self.assertQuoted(f"over $a \\in [1/2, 1]$, $w_a = {fixed(half['w_eff_C']['wa'], 6)}$ and constant proxy "
                          f"${fixed(half['w_eff_C']['w_const'], 4)}$ under (C)")
        self.assertQuoted(f"over $[1/3, 1]$, $w_a = {fixed(third['w_eff_C']['wa'], 6)}$ and "
                          f"${fixed(third['w_eff_C']['w_const'], 4)}$")
        # the gas has |wa| <= the largest magnitude of the recorded tangent and fit ranges
        detail = check_detail(EOS_CHECKS, "gas_cpl_far_from_unite")
        bounds = re.search(r"tangent wa in \[([-0-9.]+), ([-0-9.]+)\], least-squares fit wa in \[([-0-9.]+), "
                           r"([-0-9.]+)\]", detail).groups()
        largest = max(bounds, key=lambda b: abs(float(b))).lstrip("-")
        self.assertEqual(largest, "0.003904")
        self.assertQuoted(f"$\\lvert w_a\\rvert \\leq {largest}$")
        # the mixture scans
        scans = load_json(EOS_SUMMARY)["mixture_scan"]
        closest = scans["C"]["closest"]
        self.assertEqual(closest["distance"], 0.1604394909208)
        self.assertEqual((closest["gas_fraction"], closest["w_c_today"]), (0.0, -0.47))
        self.assertEqual(closest["distance"], min(s["closest"]["distance"] for s in scans.values()))
        self.assertQuoted(f"$({closest['w0']}, {closest['wa']})$ under (C) (distance {closest['distance']}")
        ratio, ab = scans["ratio"]["closest"], scans["A_B"]["closest"]
        self.assertQuoted(f"$({ratio['w0']}, {ratio['wa']})$ in the ratio definition (distance {ratio['distance']})")
        self.assertQuoted(f"$({ab['w0']}, {ab['wa']})$ under (A), (B) (distance {ab['distance']})")
        # the pure condensate under (C): w_eff(C) = (5/9) w_c - 4/9 at w_c = -0.47
        self.assertEqual(f"{float(Fraction(5, 9) * Fraction(-47, 100) - Fraction(4, 9)):.13f}", "-0.7055555555556")
        self.assertQuoted("(closest distance 0.1604394909208, under (C))")
        # every scanned mixture with w0 within 0.1 of the Unite w0 has wa in [min, max], both recorded; all steeper
        near_c = (scans["C"]["min_wa_with_w0_within_0p1_of_unite"], scans["C"]["max_wa_with_w0_within_0p1_of_unite"])
        self.assertEqual(near_c, (-1.779879740253, -0.8286111111111))
        self.assertLess(max(s["max_wa_with_w0_within_0p1_of_unite"] for s in scans.values()), -0.6)
        self.assertQuoted(f"$w_a$ between {near_c[0]} and {near_c[1]} under (C)")
        self.assertQuoted("steeper than the Unite $-0.60$ in every definition")
        self.assertEqual(load_json(EOS_SUMMARY)["mixture_C_lambda0_condensate_min_w_eff_C"], -0.4441111111111)

    def test_condensate_ratio(self):
        u = Fraction(-382, 441)
        self.assertEqual(u / (2 + u), Fraction(-764, 1000))
        cond = load_json(EOS_SUMMARY)["condensate"]
        self.assertAlmostEqual(cond["u_for_ratio_minus_0p764_today"], float(u), places=12)
        self.assertEqual(f"{float(1 + u / 2):.12f}", "0.566893424036")
        # on the history lambda S/m = u ~ e^(-(5/3) a4): wa = -dw/da4 = (10/3) u/(2 + u)^2, exactly -28077/12500
        ratio_wa = Fraction(10, 3) * u / (2 + u) ** 2
        self.assertEqual(ratio_wa, Fraction(-28077, 12500))
        self.assertAlmostEqual(cond["ratio_wa_at_that_u"], float(ratio_wa), places=12)
        self.assertQuoted("$-28077/12500 = -2.24616$")
        # w_eff(A) = (5/9) w_c and w_eff(C) = (5/9) w_c - 4/9, both with (5/9) of the ratio's wa
        self.assertEqual(fixed(cond["w_eff_A_B_today_at_that_u"], 6), "-0.424444")
        self.assertEqual(fixed(cond["w_eff_C_today_at_that_u"], 6), "-0.868889")
        self.assertEqual(f"{float(Fraction(5, 9) * Fraction(-764, 1000) - Fraction(4, 9)):.6f}", "-0.868889")
        self.assertEqual(Fraction(5, 9) * ratio_wa, Fraction(-9359, 7500))
        self.assertEqual(f"{float(Fraction(5, 9) * ratio_wa):.6f}", fixed(cond["wa_A_B_C_at_that_u"], 6))
        self.assertEqual(fixed(cond["wa_A_B_C_at_that_u"], 6), "-1.247867")
        # M1 under (C): the tangent slope is (5/9)(10/3) u/(2 + u)^2 = (50/27) u/(2 + u)^2
        self.assertEqual(Fraction(5, 9) * Fraction(10, 3), Fraction(50, 27))
        m1 = load_json(EOS_THEORY)["models"]["M1_condensate"]
        self.assertEqual(m1["N2"]["w"], "-4/9 + (5/9) u/(2 + u)")
        self.assertEqual(m1["ratio"]["CPL"]["wa"], "(10/3) u/(2 + u)^2")
        self.assertQuoted("| M1 | $-4/9 + 5w/9$ | $(50/27)\\,u/(2+u)^2$ |")
        # the observer reads (5/9)(1 + w) - 1 = (5/9) w - 4/9, below -1 exactly where w is
        for w in (Fraction(-3, 2), Fraction(-1), Fraction(-764, 1000), Fraction(1, 3)):
            self.assertEqual(Fraction(5, 9) * (1 + w) - 1, Fraction(5, 9) * w - Fraction(4, 9))
        # with u ~ a^(-5/3) the ratio enters the phantom window (u = -1) at a^(5/3) = -u and its energy vanishes
        # (u = -2) at a^(5/3) = -u/2; there w_eff(C) < -1 (section 5.5; eos-theory.json, key ghost)
        self.assertEqual((-u, -u / 2), (Fraction(382, 441), Fraction(191, 441)))
        enter, vanish = f"{float(-u) ** 0.6:.12f}", f"{float(-u / 2) ** 0.6:.12f}"
        self.assertEqual((enter, vanish), ("0.917434069855", "0.605280756393"))
        self.assertQuoted(f"$a = (382/441)^{{3/5}} = {enter}$ back to $a = (191/441)^{{3/5}} = {vanish}$")
        ghost = load_json(EOS_THEORY)["ghost"]
        self.assertIn(f"from a = (382/441)^(3/5) = {enter} back to a = (191/441)^(3/5) = {vanish}", ghost)
        self.assertQuoted(f"a drifting $\\lambda < 0$ condensate crosses at $a = {enter}$")

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
        self.assertEqual(m2["N2_tangent_exact"], {"w0": "-2749/9000", "wa": "81037/500000"})
        r = Fraction(417, 1000)
        self.assertEqual((-Fraction(4, 9) + r / 3, Fraction(2, 3) * r * (1 - r)),
                         (Fraction(-2749, 9000), Fraction(81037, 500000)))
        self.assertEqual(m2["N2"]["CPL_tangent"]["wa"], "0.162074")
        self.assertQuoted(row("M2_positive_good_sector_gas", "M2", 6))
        m3 = models["M3_positive_extra_time_mode"]
        self.assertEqual((m3["N2_tangent_exact"]["w0"], m3["N2_tangent_exact"]["wa"]), ("-3583/9000", "-196963/4500000"))
        s = Fraction(417, 1417)
        self.assertEqual(-Fraction(4, 9) + Fraction(1, 9) * s / (1 - s), Fraction(-3583, 9000))
        self.assertEqual(-Fraction(2, 27) * s / (1 - s) ** 2, Fraction(-196963, 4500000))
        self.assertQuoted(row("M3_positive_extra_time_mode", "M3", 6))
        self.assertEqual(m3["turning_point_a_star"]["exact"], "(1417/417)^(3/2)")
        a3 = fixed((1417 / 417) ** 1.5, 4)
        self.assertQuoted(f"$a_* = (1417/417)^{{3/2}} = {a3}$")
        m4 = models["M4_condensate_plus_extra_time_mode"]
        self.assertEqual((m4["parameters"]["s"], m4["parameters"]["Omega_q"]), ("264037/403037", "57963/264037"))
        self.assertQuoted(row("M4_condensate_plus_extra_time_mode", "M4", 6))
        self.assertEqual(m4["min_w_N2_on_(0,1]"], "-0.443913275792")
        self.assertGreaterEqual(Fraction(m4["min_w_N2_on_(0,1]"]), Fraction(-4, 9))
        a4 = fixed(float(m4["turning_point_a_star"]), 4)
        self.assertQuoted(f"at $a_* = {a4}$ and then grows")
        m5 = models["M5_with_ghost_component"]
        self.assertQuoted(row("M5_with_ghost_component", "M5", 4))
        p = m5["parameters"]
        self.assertEqual(p["G"], "3/10")
        self.assertQuoted(f"$s = {fixed(float(p['s']), 4)}$, $\\Omega_q = {fixed(float(p['Omega_q']), 4)}$, "
                          f"condensate fraction $\\Omega_c = {fixed(float(p['Omega_c']), 4)}$")
        a5 = fixed(float(m5["turning_point_a_star"]), 4)
        self.assertQuoted(f"its turning point is at $a_* = {a5}$")
        self.assertQuoted(f"(M3: {a3}, M4: {a4}, M5: {a5})")
        self.assertQuoted(f"(M3: {a3}, M4: {a4})")
        self.assertQuoted("$G = 3/10$ of the total at $a = 1$")
        fit5 = m5["N2"]["fit_a_1/2_to_1"]
        self.assertQuoted(f"its fit over $[1/2, 1]$ is ({fit5['w0']}, {fit5['wa']})")
        self.assertIn("G >= 3749/3000", m5["unite"])
        for name in ("M2_positive_good_sector_gas", "M3_positive_extra_time_mode",
                     "M4_condensate_plus_extra_time_mode", "M5_with_ghost_component"):
            self.assertEqual(models[name]["N2"]["crossings_of_minus_1_in_[1/3,1]"], [], name)
        m2n1 = m2["N1"]["CPL_tangent"]
        self.assertQuoted(f"tangent $({m2n1['w0']}, {m2n1['wa']})$")
        # today's values of section 9.2
        w0_m2 = fixed(float(m2["N2"]["CPL_tangent"]["w0"]), 4)
        w0_m3 = fixed(float(m3["N2"]["CPL_tangent"]["w0"]), 4)
        self.assertEqual(m3["N2"]["CPL_tangent"]["w0"], m4["N2"]["CPL_tangent"]["w0"])
        self.assertQuoted(f"M2: {w0_m2}, M3 and M4: {w0_m3} today")
        self.assertQuoted(f"(M3: {fixed(float(m3['N2']['CPL_tangent']['wa']), 6)})")
        # the ghost fraction the Unite w0 would need, and the zero of the total energy of condensate + ghost
        g = Fraction(3749, 3000)
        self.assertEqual(-Fraction(4, 9) - g / 3, Fraction(-861, 1000))
        self.assertEqual(g / (1 + g), Fraction(3749, 6749))
        self.assertQuoted("$a = G/(1 + G) = 3749/6749$")
        self.assertIn("w_eff(N2) >= -(4 - 2 beta)/3 (= -4/9 on the history", load_json(EOS_THEORY)["wkb"]["theorem"])

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
        self.assertEqual((growth["a_star"], growth["numerical_rate"], growth["wkb_rate"]),
                         (6.2639848, 0.30909994, 0.3118201))
        self.assertQuoted(f"$10^{{{growth['log10_amplitude_growth_5.5_to_7.4']:.2f}}}$")
        self.assertQuoted(f"($\\rho/Q$ = {growth['rho_over_Q_at_7.4']!r} at $a = 7.4$")
        self.assertEqual(numerics["settings"]["eps_AH_over_m"], 0.001)
        self.assertQuoted("$H/m = 10^{-3}$")
        self.assertIn("sqrt(s a^(2/3) - 1) - (b4'/b4 - a4'/2)", check_detail(INDEPENDENT_NUMERICS, "B_growth_rate"))
        self.assertQuoted("$\\sqrt{sa^{2/3} - 1} - (b_4'/b_4 - a_4'/2) = 0.3118201$")
        self.assertEqual(numerics["models"]["M5_with_ghost_component"]["crossings_N2"], 0)
        self.assertEqual(numerics["independent_solves"], {"M3_s": 0.29428947, "positive_models_min_w_N2": -0.42931652})
        self.assertEqual(numerics["superposition"]["rho_pointwise_range"], 0.27738092)

    def test_implementation_b_invariants(self):
        drift, onshell, residual, deviation, dilution = [], [], [], [], []
        for check in load_json(INDEPENDENT_NUMERICS)["checks"]:
            detail = check["detail"]
            if check["name"].startswith("B_run_"):
                drift.append(re.search(r"Krein charge per coordinate volume e\^\(-a4\) b4\^2 Q: drift ([0-9.e+-]+);",
                                       detail).group(1))
                onshell.append(re.search(r"max \|L0\| \(on shell\) ([0-9.e+-]+);", detail).group(1))
                residual.append(re.search(r"relative residual ([0-9.e+-]+) ", detail).group(1))
            if check["name"].startswith("B_vs_A_M"):
                match = re.search(r"max deviation ([0-9.e+-]+)$", detail)
                if match:
                    deviation.append(match.group(1))
            if check["name"].startswith("B_dilution_equals_formula_M"):
                dilution.append(re.search(r"to within ([0-9.e+-]+)$", detail).group(1))
        self.assertEqual((len(drift), len(onshell), len(residual), len(deviation), len(dilution)), (6, 6, 6, 12, 4))
        largest = {key: max(values, key=float) for key, values in
                   (("drift", drift), ("onshell", onshell), ("residual", residual), ("deviation", deviation),
                    ("dilution", dilution))}
        self.assertEqual(largest, {"drift": "9.8449027e-14", "onshell": "1.2212453e-15", "residual": "5.542778e-08",
                                   "deviation": "2.2072418e-05", "dilution": "2.7779535e-05"})
        models = load_json(NUMERICS)["models"]
        self.assertEqual(max(m["N2_dilution_vs_formula_max_deviation"] for m in models.values()),
                         float(largest["dilution"]))
        for value in (f"drift at most {largest['drift']}", f"at most {largest['onshell']}",
                      f"relative residual at most {largest['residual']}", f"to within {largest['deviation']}",
                      f"agree to within {largest['dilution']}"):
            self.assertQuoted(value)
        self.assertQuoted("the Krein charge per coordinate volume $e^{-a_4}b_4^2Q$ is conserved")

    def test_history_required_source(self):
        """The source the author's equations need on a4 = H x4, b4 = e^((4/3) H x4) in the corrected metric (sections
        2.4, 6.1, 9.2, 13.1): recorded in a4-equations.json and in eos-theory.json (the same polynomials in
        xi = kk = e^((2/3) H x4)); exact arithmetic here: p0 = p_t, the conservation identity holds, the anisotropy is
        the recorded one, and the rendered formulas of the document are these polynomials."""
        src = load_json(EOS_THEORY)["condensate"]["historyRequiredSource"]
        self.assertIn("(Lambda = -10)", src["meaning"])
        self.assertIn("w1 = 1, w2 = 1/32, w3 = 1/1152", src["meaning"])
        self.assertIn("kk = e^((2/3) H x4)", src["meaning"])
        self.assertQuoted("$w_1 = 1$, $w_2 = 1/32$, $w_3 = 1/1152$ and $\\Lambda = -10$ ($H = 1$)")
        minus_rho, p3, p0, pt = (polynomial(src[key]) for key in ("minus_rho", "p3", "p0", "pt"))
        record = load_json(A4_EQUATIONS)["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
        self.assertIn("Lam = -10", load_json(A4_EQUATIONS)["exponentialHistory"]["authorWeights"]["weights"])
        samples = [Fraction(n, 7) for n in (3, 7, 11, 20, 35)]
        for key, function in (("minus_rho", minus_rho), ("p3", p3), ("p0", p0), ("pt", pt)):
            other = polynomial(record[key]["input"])
            self.assertTrue(all(other(x) == function(x) for x in samples), key)
        self.assertTrue(all(p0(x) == pt(x) for x in samples))                        # p0 = p_t
        # d rho/dx4 = -3 a4' (rho + p3) - 4 h4 (rho + p0) with a4' = H = 1, h4 = b4'/(2 b4) - a4' = -1/3 and
        # d xi/dx4 = (2/3) xi, for kappa T - Lambda delta (the Lambda terms cancel in rho + p)
        h = Fraction(1, 1000)
        for x in samples:
            d_minus_rho = (minus_rho(x + h) - minus_rho(x - h)) / (2 * h)            # exact for degree <= 2
            lhs = -Fraction(2, 3) * x * d_minus_rho
            rhs = -3 * (p3(x) - minus_rho(x)) - 4 * Fraction(-1, 3) * (p0(x) - minus_rho(x))
            self.assertEqual(lhs, rhs, x)
        aniso = re.search(r"kappa \(p3 - p0\) = (.+)$", check_detail(DERIVE_EOS, "history_required_source")).group(1)
        self.assertEqual(quadratic_coefficients(lambda x: p3(x) - p0(x)), quadratic_coefficients(polynomial(aniso)))
        self.assertEqual(quadratic_coefficients(lambda x: p3(x) - p0(x)),
                         (Fraction(-9, 16), Fraction(1069, 432), Fraction(2015, 972)))
        self.assertQuoted("-\\kappa\\rho - \\Lambda &= " + render_quadratic(quadratic_coefficients(minus_rho)) + " ,")
        self.assertQuoted("\\kappa p_3 - \\Lambda = " + render_quadratic(quadratic_coefficients(p3)) + " ,")
        self.assertQuoted("\\kappa p_0 - \\Lambda &= \\kappa p_t - \\Lambda = "
                          + render_quadratic(quadratic_coefficients(p0)) + " ,")
        self.assertQuoted("$\\kappa(p_3 - p_0) = " + render_quadratic(quadratic_coefficients(lambda x: p3(x) - p0(x)))
                          + " \\neq 0$")
        self.assertQuoted("\\xi = e^{2a_4}/b_4 = e^{(2/3)Hx_4}")
        # kappa rho = -(minus_rho) - Lambda = 10 - minus_rho, at a4 = 0 (xi = 1) and a4 = 2 (xi = e^(4/3))
        at0 = f"{float(10 - minus_rho(Fraction(1))):.6g}"
        at2 = f"{10 - float(minus_rho(Fraction(math.exp(4 / 3)))):.6g}"
        self.assertEqual((at0, at2), ("3.57407", "-7.63383"))
        detail = check_detail(KS_SOURCE, "ks_history_is_a_prescribed_background")
        self.assertIn(f"a4,0 = 0 (kk = 1): kappa rho = {at0}", detail)
        self.assertIn(f"kappa rho = {at2}", detail)
        self.assertIn("kappa rho > 0 at every slice: False", detail)
        self.assertQuoted(f"$\\kappa\\rho = {at0}$ at $a_4 = 0$ and $\\kappa\\rho = {at2}$ at $a_4 = 2$")
        # Wolfram reads the same source, finds it anisotropic and equal to the dirac16complex00 record
        d6 = check_detail(WOLFRAM, "D6_history_source_anisotropic")
        self.assertIn("2015/972 + (1069*kkv)/432 - (9*kkv^2)/16 != 0", d6)
        self.assertIn("the record of dirac16complex00 states the same source: True", d6)
        self.assertIn("no condensate is the source of the record's history (exact)",
                      check_detail(DERIVE_EOS, "condensate_cannot_source_history"))
        self.assertIn("the history is a PRESCRIBED background", check_detail(DERIVATION, "record_history_needs_a_source"))
        self.assertIn("Einstein gravity admits a diagonal source for every b4",
                      check_detail(DERIVATION, "einstein_no_mixed_component"))

    def test_exact_fock_variant_of_the_n8_states(self):
        """The negative E of the N = 8, lambda > 0 states is a property of the uniform-gas functional (section 4.7)."""
        with open(EXACT_FOCK, encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row["N"] == "8"]
        self.assertEqual(len(rows), 20)
        # the canonical energies are those of the dense history of the corrected metric
        dense = {}
        with open(D16 / "outputs" / "ks-history-dense.csv", encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                dense[(row["N"], row["lambda_tag"], float(row["a4"]))] = float(row["E_KS"])
        for row in rows:
            self.assertAlmostEqual(float(row["E_uniform_gas"]), dense[("8", row["lambda_tag"], float(row["a4"]))],
                                   delta=1e-12)
        largest = max(abs(float(row["E_exact_fock_scf"])) for row in rows)
        self.assertLessEqual(largest, 1e-11)
        mantissa, exponent = f"{largest:.2e}".split("e")
        self.assertEqual(f"{largest:.2e}", "4.98e-12")
        for row in rows:
            if float(row["lambda"]) > 0:
                canonical = float(row["E_uniform_gas"])
                first_order = float(row["E_uniform_gas_plus_deltaE_x"])
                self.assertLess(canonical, 0)
                self.assertLess(first_order, 0)
                self.assertLess(abs(first_order), abs(canonical))
        self.assertQuoted(f"the same $N = 8$ states have $\\lvert E\\rvert \\leq {mantissa} \\times 10^{{{int(exponent)}}}$")
        self.assertQuoted(f"$\\lvert E\\rvert \\leq {mantissa} \\times 10^{{{int(exponent)}}}$, section 4.7")
        self.assertQuoted("still leaves $E < 0$ for $\\lambda > 0$, of smaller magnitude")
        self.assertIn("scfTolerance = 1e-11", check_detail(KS_CROSSCHECK, "rust_refinement_applies_to_matrix_exx"))
        self.assertIn(self.exact_fock_slices_statement(rows), self.text)

    def exact_fock_slices_statement(self, rows):
        """The slices of the exact-Fock N = 8 rows and |E| below the solver's self-consistency tolerance 1e-11
        (ks-crosscheck.json) at each of them, as section 4.7 states them."""
        slices = sorted({float(row["a4"]) for row in rows})
        self.assertEqual(slices, [0.0, 0.5, 1.0, 1.5, 2.0])
        tags = sorted({row["lambda_tag"] for row in rows})
        self.assertEqual(tags, ["lamm1", "lamm2", "lamp1", "lamp2"])
        for tag in tags:
            energies = [float(row["E_exact_fock_scf"]) for row in rows if row["lambda_tag"] == tag]
            self.assertEqual(len(energies), len(slices), tag)
            self.assertTrue(all(abs(e) <= 1e-11 for e in energies), f"{tag}: E_exact_fock_scf above the tolerance")
        listed = ", ".join(f"{a:g}" for a in slices)
        return (f"(computed at the canonical slices $a_4 = {listed}$, below the solver's self-consistency tolerance "
                "$10^{-11}$ at each")

    def test_exact_fock_slices_detect_a_change(self):
        # negative controls: a changed slice list in the text, and a changed E at one slice in the data, are detected
        with open(EXACT_FOCK, encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.DictReader(handle) if row["N"] == "8"]
        statement = self.exact_fock_slices_statement(rows)
        self.assertNotIn(statement, self.text.replace("$a_4 = 0, 0.5, 1, 1.5, 2$", "$a_4 = 0, 1, 2$"))
        changed = [dict(row) for row in rows]
        changed[1]["E_exact_fock_scf"] = "-8.125852314700990e-10"
        with self.assertRaises(AssertionError):
            self.exact_fock_slices_statement(changed)
        dropped = [row for row in rows if float(row["a4"]) != 1.5]
        with self.assertRaises(AssertionError):
            self.exact_fock_slices_statement(dropped)

    def test_ks_source_conditions(self):
        data = load_json(KS_SOURCE)
        self.assertEqual(data["summary"], {"checks": 5, "pass": 5, "fail": 0})  # 5 for the corrected metric (W5)
        self.assertIn("the corrected metric of 2026-10-16 (version 2", data["metric"])
        self.assertIn("No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the corrected "
                      "metric", data["conclusion"])
        self.assertIn("C2 (p0 = p_t) holds exactly for the lambda = 0 states and fails for lambda != 0",
                      data["conclusion"])
        self.assertQuoted("No recorded Kohn-Sham state is an admissible source of the corrected metric")
        self.assertQuoted(f"(the {data['summary']['checks']} checks of "
                          "`Revision/field_equations_a4/reports/ks-source-conditions.json`")

    def test_bulk_band_and_fold_band(self):
        free = load_json(FREE_GAS)
        bulk = free["bulkBand_n2_1"]
        values = [entry["w_eff_A_B"] for entry in bulk]
        self.assertEqual((bulk[0]["a4"], bulk[-1]["a4"]), (-3.0, 4.0))
        self.assertTrue(all(b < a for a, b in zip(values, values[1:])))               # monotonically decreasing
        self.assertEqual((fixed(values[0], 6), fixed(values[-1], 6)), ("0.318721", "-0.081074"))
        signs = [(entry["a4"], entry["w_eff_A_B"] > 0) for entry in bulk]
        change = [signs[i][0] for i in range(1, len(signs)) if signs[i][1] != signs[i - 1][1]]
        self.assertEqual(change, [-0.25])
        self.assertQuoted("changes sign between $a_4 = -0.5$ and $a_4 = -0.25$")
        self.assertGreater(values[-1], -1 / 9)                                         # toward -1/9 from above
        self.assertTrue(all(abs(entry["w_eff_A_B"] - 1 / 3) < 1e-11 for entry in free["foldBand_n2_1"]))
        self.assertQuoted("falls monotonically from 0.318721 at $a_4 = -3$ to -0.081074 at $a_4 = 4$")
        self.assertQuoted("its $w_{\\rm eff}(A)$ falls from 0.318721 to -0.081074 for one shell")

    def test_abstract_numbers(self):
        abstract = self.text.split("## Abstract", 1)[1].split("## 1.", 1)[0]
        for value in ("615 instantaneous states", "[0.330585, 0.336132]", "from 0.318721 to -0.081074",
                      "$w_{\\rm eff}(A) = 1/3$ exactly at every slice", "$w_{\\rm eff}(C) = -1/9$",
                      "$\\lambda S/m = -382/441$", "(-0.861, -0.60)", "$w = -0.764$", "3749/3000",
                      "$w_{\\rm eff}(C) \\geq -4/9$", "closest distance 0.1604394909208",
                      "every verdict moves by exactly $-4/9$", "PRESCRIBED background",
                      "anisotropic source that grows with $x_4$"):
            self.assertIn(value, abstract, value)
        self.assertEqual(len(load_json(KS_HISTORY)["slices"]) * 15, 615)


if __name__ == "__main__":
    unittest.main()
