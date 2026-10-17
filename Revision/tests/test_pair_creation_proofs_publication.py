#!/usr/bin/env python3
"""Publication test for Revision/docs/PAIR_CREATION_PROOFS.{md,tex,pdf}.

The document gives the exact proof results of the pairing theorems T1, T2 and the quantum-level
reading Q for dirac16complex and dirac16complex00 (Revision/SPEC.md section 9) and states exactly what
they do not establish.  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/PAIR_CREATION_PROOFS.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_pair_creation_proofs_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md (same options as the
    build command above), both files are UTF-8 with LF line endings, and their sha256 are pinned;
  * the PDF is registered in the Revision registry Revision/pdf-specifications.json (edition
    pair-creation-proofs: path, page count and sha256 of the committed PDF) and NOT in the registry of
    the earlier stages (provenance/pdf-specifications.json); the PDF is structurally sound;
  * title, subtitle and section headings; the last section is "What is proved and what is not";
  * the key statements are present, and overclaims are absent (the phrase "are created in pairs"
    occurs only inside the quoted request; pair creation is never called proved, and T3 is called
    proved only as a theorem under its stated hypotheses, never as a physical process);
  * no text of the withdrawn metrics appears as current (the Z2 orbifold and the brane only as
    withdrawn or absent, no sqrt|g| = b4^(3/2) cos z, no brane parity, no patch end);
  * every check name the document cites exists in a Revision report with the verdict PASS, and every
    check of the two pairing reports is listed (complete verification records);
  * the report-count table equals the counts recomputed from the reports;
  * the quoted data (the corrected-metric formulas of sections 2.1, 2.5, 5.4 and 9.4, reflection table,
    Krein signs, one-particle samples, the vacuum statements of the a4 and b4 equations, the Kohn-Sham
    self-test numbers, the Kohn-Sham source numbers, the numbers of the T3 completion and its two
    numerical demonstrations, the sha256 and run records of the pairing and T3 verifiers, the
    reproduction commands of the field-theory record, and further numbers) agree with the Revision
    reports and records;
  * OPTIONAL (only when REVISION_PDF_REBUILD=1; needs pdflatex, about 10 s): the PDF is rebuilt in
    verify mode and must match the registry.

After an intended edit of the document: rebuild in verify mode until warning-free, register it
(--register), and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

import sympy as sp

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

DOCS = REVISION / "docs"
MARKDOWN = DOCS / "PAIR_CREATION_PROOFS.md"
TEX = DOCS / "PAIR_CREATION_PROOFS.tex"
PDF = DOCS / "PAIR_CREATION_PROOFS.pdf"
EDITION = "pair-creation-proofs"
REGISTRY = REVISION / "pdf-specifications.json"
OLD_REGISTRY = ROOT / "provenance" / "pdf-specifications.json"
REBUILD = os.environ.get("REVISION_PDF_REBUILD") == "1"

MARKDOWN_SHA256 = "6123568fe2c17fc1ab3d0fb42df6bcaae7dbb5f27f18500bed0f50d057262ce2"
TEX_SHA256 = "a9f3126394893807046c55c520c9502b4cc106a6a5cee3ef3cbd405a54d2e017"

PAIRING_THEORY = REVISION / "pairing" / "pairing-theory.json"
WOLFRAM_PAIRING = REVISION / "pairing" / "reports" / "wolfram-pairing.json"
PYTHON_PAIRING = REVISION / "pairing" / "reports" / "python-pairing.json"
T3_THEORY = REVISION / "pairing" / "kohn_sham" / "t3-theory.json"
WOLFRAM_T3 = REVISION / "pairing" / "kohn_sham" / "reports" / "wolfram-t3.json"
PYTHON_T3 = REVISION / "pairing" / "kohn_sham" / "reports" / "python-t3.json"
T3_COMPLETION = REVISION / "pairing" / "kohn_sham" / "t3-completion.json"
WOLFRAM_T3C = REVISION / "pairing" / "kohn_sham" / "reports" / "wolfram-t3-completion.json"
PYTHON_T3C = REVISION / "pairing" / "kohn_sham" / "reports" / "python-t3-completion.json"
T3_RUST_DEMO = REVISION / "pairing" / "kohn_sham" / "reports" / "t3-rust-demo.json"
T3_REFERENCE_DEMO = REVISION / "pairing" / "kohn_sham" / "reports" / "t3-reference-demo.json"
KS_SOURCE_A4 = REVISION / "field_equations_a4" / "ks_source" / "reports" / "ks-source-a4.json"
KS_SOURCE_CONDITIONS = REVISION / "field_equations_a4" / "reports" / "ks-source-conditions.json"
KS_SOLVER = REVISION / "kohn_sham" / "reports" / "ks-rust-solver.json"
KS_THEORY = REVISION / "kohn_sham" / "ks-theory.json"
FIELD_THEORY_WOLFRAM = REVISION / "theory" / "reports" / "wolfram-field-theory.json"
FIELD_THEORY_PYTHON = REVISION / "theory" / "reports" / "python-field-theory.json"
SCOPE_WOLFRAM = REVISION / "theory" / "reports" / "wolfram-scope.json"
SCOPE_PYTHON = REVISION / "theory" / "reports" / "python-scope.json"
T3_PROVENANCE = REVISION / "pairing" / "kohn_sham" / "wolfram" / "WOLFRAMSCRIPT_PROVENANCE.md"
A4_WOLFRAM = REVISION / "field_equations_a4" / "reports" / "wolfram-a4-report.json"
A4_PYTHON = REVISION / "field_equations_a4" / "reports" / "python-a4-report.json"

# The reports of the count table (section 9.1), in the order of the table.
COUNTED_REPORTS = (
    "Revision/pairing/reports/wolfram-pairing.json",
    "Revision/pairing/reports/python-pairing.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
    "Revision/pairing/kohn_sham/reports/python-t3.json",
    "Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json",
    "Revision/pairing/kohn_sham/reports/t3-rust-demo.json",
    "Revision/pairing/kohn_sham/reports/t3-reference-demo.json",
    "Revision/pairing/kohn_sham/reports/python-t3-completion.json",
    "Revision/algebra/reports/wolfram-algebra.json",
    "Revision/algebra/reports/python-algebra.json",
    "Revision/theory/reports/wolfram-field-theory.json",
    "Revision/theory/reports/python-field-theory.json",
    "Revision/theory/reports/wolfram-scope.json",
    "Revision/theory/reports/python-scope.json",
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "Revision/field_equations_a4/reports/python-a4-report.json",
    "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
    "Revision/kohn_sham/reports/ks-theory-wolfram.json",
    "Revision/kohn_sham/reports/ks-theory-python.json",
    "Revision/kohn_sham/reports/ks-rust-solver.json",
)
# Every report whose check names the document may cite.
CITABLE_REPORT_GLOBS = (
    "algebra/reports/*.json",
    "theory/reports/*.json",
    "field_equations_a4/reports/*.json",
    "field_equations_a4/ks_source/reports/*.json",
    "pairing/reports/*.json",
    "pairing/kohn_sham/reports/*.json",
    "kohn_sham/reports/*.json",
)

TITLE = "Pairing of universes of masses +m and -m: exact proofs for dirac16complex and dirac16complex00"
SUBTITLE_START = "The pairing theorems T1, T2 and T3 and the quantum-level reading in the author's primordial"
SECTIONS = (
    "## Abstract",
    "## 1. The request and the exact answer",
    "## 2. Setting and conventions",
    "## 3. Algebraic lemmas",
    "## 4. Theorem T1: the chirality pairing (both fields)",
    "## 5. Theorem T2: the mirror pairing (both fields)",
    "## 6. The quantum-level reading (dirac16complex)",
    "## 7. Corollary C1: a T1 pair as the source of the field equations for $a_4$ and $b_4$",
    "## 8. Theorem T3: the Kohn-Sham level (dirac16complex)",
    "## 9. Verification records",
    "## 10. Reproduction",
    "## 11. What is proved and what is not",
)
REQUEST = "PROVE that Universes of masses {+mass, -mass} are created in pairs"
KEY_STATEMENTS = (
    REQUEST + " for each case of the dirac16complex and the dirac16complex00 fields.",
    "T1, T2, T3 and the quantum reading Q are proved, each under its stated hypotheses; the creation of pairs is not.",
    "That universes occur in pairs is not proved",
    "the corrected metric has no Z2 orbifold",
    "both fold conditions filled, ASSUMED",
    "identical one-particle ($\\lambda = 0$) spectra (flat space, or frozen coefficients at a point)",
    "No creation process, rate or amplitude follows from these equations.",
    "Not proved: that such universes are CREATED, in pairs or otherwise.",
    r"$\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$",
    r"$E_{m,\lambda}[\Gamma\Psi] = -\Gamma E_{-m,-\lambda}[\Psi]$",
    r"$T^{(-m,-\lambda)}_{\mu\nu}[\Gamma\Psi] = -T^{(m,\lambda)}_{\mu\nu}[\Psi]$",
    r"$\mathcal{L}_{m,\lambda}[\gamma^n\Psi;\,R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi;\,e]$",
    r"$E_{m,\lambda}[\gamma^n\Psi;\,R_ne] = -\gamma^nE_{-m,\lambda}[\Psi;\,e]$",
    "the energy density and every component without an $x_0$ index are EQUAL, not opposite",
    "The chirality image $\\chi = \\Gamma\\Psi$ carries the Krein metric $-B$",
    "no cancellation $P_1 + P_2 = 0$ follows",
    "The T2 image $\\gamma^0\\Psi$ keeps the anticommutator $+B$",
    "no junction condition or matching of the field across the fold is derived",
    "the same occupations, chemical potential, particle number and entropy, EQUAL Kohn-Sham energy",
    "for every REAL frequency ($w^2 > 0$, with or without extra-time momentum)",
    "The field is a fixed (test) background: it is NOT varied",
    "dirac16complex00 is a classical field and has no quantum reading.",
    "they neither use nor establish a positive-norm Fock space for either universe",
    "a T1 pair cannot by itself be the source of any exponential history in Einstein gravity or with the author's weights",
    "1. No creation process:",
    "2. No rate, probability or amplitude:",
    "3. No dynamical necessity:",
    "10. The Kohn-Sham level T3 holds for the instantaneous (adiabatic) mean-field Kohn-Sham states only",
    "### 8.5 Completion of T3 (2026-10-08)",
    "T3 and its statements S1 to S4 are unchanged.",
    r"the Kohn-Sham partner carries $+\lambda$",
    "the demonstrations of section 8.5 are numerical, not proofs",
    "the filling convention remains a CONVENTION whose justification is open",
    "that record establishes neither Hypothesis nor Hypothesis00",
    "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
    "`Revision/docs/LOVELOCK_GKD`",
)
FORBIDDEN = (
    r"creation (?:of (?:pairs|universes) )?(?:is|has been|was|are) (?:proved|proven|established|derived)",
    r"\bthe Z2 (?:brane|mirror) (?:is|has been|was) (?:derived|proved|proven)",
    r"\bwe (?:have )?prove[d]? that (?:the )?universes\b",
    r"\bproof of (?:the )?(?:pair )?creation\b",
)
# Text of the withdrawn metrics (2026-10-14 and version 1 of 2026-10-16) that must not reappear as current.
WITHDRAWN_METRIC_TEXT = (
    r"b_4^{3/2}\cos z",
    r"b_4^{3/2}",
    "Z2 brane",
    "brane parit",
    "patch end",
    r"> 0$; `nontriviality_1_dirac16complex`",  # G^2 > 0 without the range x4 >= 0
)
# The check that keeps its name from the withdrawn metric (its detail speaks of the degenerate points, the folds).
BRANE_NAMED_CHECK = "good_sector_hermiticity_up_to_the_brane_flux"
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
        if re.fullmatch(r"[0-9a-f]{64}", span):  # a sha256 digest (section 9.3), not a check name
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.*]*", span):
            names.append(span)
    return names


def report_checks() -> dict[str, list[str]]:
    """Check name -> list of verdicts (upper case) over every citable Revision report."""
    verdicts: dict[str, list[str]] = {}
    for pattern in CITABLE_REPORT_GLOBS:
        for path in sorted(REVISION.glob(pattern)):
            data = load_json(path)
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


def sign_text(value: int) -> str:
    return "+1" if value > 0 else "-1"


class MarkdownAndTex(unittest.TestCase):
    def test_tex_is_builder_output(self):
        markdown = markdown_text()
        expected = builder.convert(
            markdown,
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
        self.assertEqual(entry["path"], "Revision/docs/PAIR_CREATION_PROOFS.pdf")
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
        self.assertEqual(level2[-1], "## 11. What is proved and what is not")
        tex = TEX.read_text(encoding="utf-8")
        self.assertIn("\\section{What is proved and what is not}", tex)

    def test_key_statements(self):
        for statement in KEY_STATEMENTS:
            self.assertIn(statement, self.text, statement)

    def test_no_overclaims(self):
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)
        # "are created in pairs" only inside the quoted request
        self.assertEqual(self.text.count("are created in pairs"), self.text.count(REQUEST))
        self.assertGreaterEqual(self.text.count(REQUEST), 3)

    def test_no_withdrawn_metric_text(self):
        """The Z2 orbifold and the brane of the withdrawn metric occur only as absent or withdrawn."""
        for text in WITHDRAWN_METRIC_TEXT:
            self.assertNotIn(text, self.text, text)
        occurrences = list(re.finditer("Z2", self.text))
        self.assertGreaterEqual(len(occurrences), 4)
        for match in occurrences:
            window = self.text[max(0, match.start() - 200):match.end() + 200]
            self.assertTrue("no Z2 orbifold" in window or "withdrawn" in window, window)
        # "brane" only in the name of the one check that kept it, explained in the text, and in "no brane"
        self.assertIn(f"`{BRANE_NAMED_CHECK}`; the check keeps its name from the withdrawn metric of 2026-10-14, "
                      "while its detail and the corrected metric have no brane: these degenerate points are the "
                      "folds of section 2.1", self.text)
        for path in (SCOPE_WOLFRAM, SCOPE_PYTHON):
            detail = check_detail(path, BRANE_NAMED_CHECK)
            self.assertNotIn("brane", detail.lower(), path.name)
            self.assertIn("degenerate points z = ", detail, path.name)
        rest = self.text.replace(BRANE_NAMED_CHECK, "").replace("have no brane", "")
        self.assertNotIn("brane", rest.lower())

    def test_negative_controls(self):
        """The content checks are not vacuous: tampered statements are detected."""
        tampered = (
            "The creation of pairs is proved by T1.",
            "The Z2 brane is derived from the field equations.",
            "We have proved that universes are created.",
            "This section is the proof of pair creation.",
        )
        self.assertEqual(len(tampered), len(FORBIDDEN))
        for pattern, sentence in zip(FORBIDDEN, tampered):
            self.assertIsNotNone(re.search(pattern, sentence, re.IGNORECASE), pattern)
        self.assertNotIn("T1_Lagrangian_primordial_commutin", report_checks())
        total, passed, failed = count_report(WOLFRAM_PAIRING)
        wrong_row = f"| `Revision/pairing/reports/wolfram-pairing.json` | {total + 1} | {passed} | {failed} |"
        self.assertNotIn(wrong_row, self.text)
        doubled = self.text + "\nUniverses are created in pairs.\n"
        self.assertNotEqual(doubled.count("are created in pairs"), doubled.count(REQUEST))

    def test_no_material_of_the_earlier_stages(self):
        for marker in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            self.assertNotIn(marker, self.text, marker)

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

    def test_every_pairing_check_is_listed(self):
        cited = set(cited_check_names(self.text))
        for path in (WOLFRAM_PAIRING, PYTHON_PAIRING):
            for check in load_json(path)["checks"]:
                self.assertIn(check["name"], cited, f"{check['name']} of {path.name}")

    def test_report_count_table(self):
        for relative in COUNTED_REPORTS:
            total, passed, failed = count_report(ROOT / relative)
            row = f"| `{relative}` | {total} | {passed} | {failed} |"
            self.assertIn(row, self.text, row)
            self.assertEqual(failed, 0, relative)
            self.assertEqual(passed, total, relative)

    def test_pairing_theory_status_and_hypotheses(self):
        theory = load_json(PAIRING_THEORY)
        self.assertEqual(theory["status"], "all checks of the report passed")
        ids = [theorem["id"] for theorem in theory["theorems"]]
        self.assertEqual(ids, ["T1", "T2", "Q"])
        self.assertIn("not part of this file", theory["T3"])
        counts = {theorem["id"]: len(theorem["verification"]) for theorem in theory["theorems"]}
        self.assertIn(f"**T1, Wolfram** ({counts['T1']} checks)", self.text)
        self.assertIn(f"**T2, Wolfram** ({counts['T2']} checks)", self.text)
        self.assertIn(f"**Q, Wolfram** ({counts['Q']} checks)", self.text)


class QuotedData(unittest.TestCase):
    def setUp(self):
        self.text = markdown_text()
        self.theory = load_json(PAIRING_THEORY)

    def test_reflection_table(self):
        for row in self.theory["data"]["reflections"]:
            direction = row["direction"][1:]
            spacelike = row["eta_nn"] == 1
            self.assertEqual(row["character_of_P_n"], -row["eta_nn"])
            self.assertEqual(row["S_sign_under_gamma_n"], -row["eta_nn"])
            self.assertEqual(row["kinetic_sign_under_gamma_n_with_frame_reflection"], row["eta_nn"])
            if spacelike:
                expected = (f"| $x_{direction}$ | $+1$ | $-1$ | $-S$ | $+K$ | "
                            r"$(-m,\lambda)$, $+\mathcal{L}$ (T2) |")
                self.assertIn("(T2)", row["mass_coupling_map"])
            else:
                expected = (f"| $x_{direction}$ | $-1$ | $+1$ | $+S$ | $-K$ | "
                            r"$(-m,-\lambda)$, $-\mathcal{L}$ (T1-type) |")
                self.assertIn("T1-type", row["mass_coupling_map"])
            self.assertIn(expected, self.text, expected)

    def test_signs_of_P_n(self):
        signs = [sign_text(row["P_n_equals_sign_times_product_of_other_seven"])
                 for row in self.theory["data"]["reflections"]]
        self.assertIn("are $" + ", ".join(signs) + "$ for $n = x_0, \\dots, x_7$", self.text)

    def test_krein_signs(self):
        signs = {entry["map"]: entry["sign"] for entry in self.theory["data"]["Krein_signs_M_B_Mdagger"]}
        self.assertEqual(signs["Gamma"], -1)
        for name in ("gamma^x0", "gamma^x1", "gamma^x2", "gamma^x3", "gamma^x4"):
            self.assertEqual(signs[name], 1, name)
        for name in ("gamma^x5", "gamma^x6", "gamma^x7"):
            self.assertEqual(signs[name], -1, name)
        for n in range(8):
            self.assertEqual(signs[f"P_x{n}"], -signs[f"gamma^x{n}"], n)
        self.assertIn(r"$\sigma_{\gamma^n} = +1$ for $n = x_0, x_1, x_2, x_3, x_4$ and $-1$ for "
                      r"$n = x_5, x_6, x_7$", self.text)
        self.assertIn(r"$-1$ for $P_{x_0}, P_{x_1}, P_{x_2}, P_{x_3}, P_{x_4}$ and $+1$ for "
                      r"$P_{x_5}, P_{x_6}, P_{x_7}$", self.text)

    def test_one_particle_samples(self):
        data = self.theory["data"]["one_particle_flat"]
        self.assertEqual(data["hamiltonian"],
                         "h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != x4) k_a gamma^a")
        self.assertIn("(m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 - k7^2)", data["square"])
        for sample in data["samples"]:
            self.assertEqual((sample["dim_plus_w"], sample["dim_minus_w"]), (8, 8))
            self.assertEqual(sample["B_inertia_plus_w"], [4, 4])
            self.assertEqual(sample["B_inertia_minus_w"], [4, 4])
            w = sample["w"]
            w_tex = re.sub(r"Sqrt\[(\d+)\]", r"\\sqrt{\1}", w)
            k = ", ".join(str(value) for value in sample["k"])
            row = f"| ${sample['m']}$ | ({k}) | ${w_tex}$ | 8 and 8 | (4,4) and (4,4) |"
            self.assertIn(row, self.text, row)
            m, ks = sp.Integer(sample["m"]), [sp.Integer(value) for value in sample["k"]]
            # the author's order k0..k7: k0..k3 space-like, k4 unused, k5..k7 the extra times
            w_value = sp.sqrt(m**2 + ks[0]**2 + ks[1]**2 + ks[2]**2 + ks[3]**2
                              - ks[5]**2 - ks[6]**2 - ks[7]**2)
            self.assertEqual(sp.simplify(w_value - sp.sympify(re.sub(r"Sqrt\[(\d+)\]", r"sqrt(\1)", w))), 0)

    def test_corrected_metric_formulas(self):
        """Sections 2.1, 2.5, 5.4 and 9.4: the formulas of the corrected metric (version 2) are those of the
        theory, scope and pairing records (plain text in the record, LaTeX in the document)."""
        quoted = (
            (FIELD_THEORY_WOLFRAM, "sqrt_det_g", "sqrt|det g| = sig f0...f7 = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4)",
             r"$\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$"),
            (FIELD_THEORY_PYTHON, "sqrt_det_g", "= e^-a4 b4^2 |cot z| (sin^2 z)^(1/4)",
             r"$\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$"),
            (FIELD_THEORY_WOLFRAM, "metric_is_the_corrected_metric", "f(x0) = E^-a4 b4^(1/2) Cot[z] (signed)",
             r"$f_0 = e^{-a_4}b_4^{1/2}\cot z$"),
            (FIELD_THEORY_WOLFRAM, "metric_is_the_corrected_metric", "f(x1,x2,x3) = E^a4, f(x4) = 1",
             r"$f_1 = f_2 = f_3 = e^{a_4}$, $f_4 = 1$"),
            (FIELD_THEORY_WOLFRAM, "metric_is_the_corrected_metric", "f(x5,x6,x7) = E^-a4 b4^(1/2) (Sin[z]^2)^(1/12)",
             r"$f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$"),
            (FIELD_THEORY_PYTHON, "metric_from_vielbein_equals_SPEC", "g_x0x0 = b4(x4)*exp(-2*a4(x4))*cot(6*H*x0)**2",
             r"$g_{00} = e^{-2a_4}b_4\cot^2 z$"),
            (FIELD_THEORY_PYTHON, "metric_from_vielbein_equals_SPEC", "g_x4x4 = -1", r"$g_{44} = -1$"),
            (FIELD_THEORY_PYTHON, "metric_from_vielbein_equals_SPEC",
             "g_x5x5 = -b4(x4)*exp(-2*a4(x4))*Abs(sin(6*H*x0))**(1/3)", r"$g_{tt} = -e^{-2a_4}b_4(\sin^2 z)^{1/6}$"),
            (FIELD_THEORY_WOLFRAM, "omega_components", "exactly 10 independent nonzero omega_mu,ab",
             "has the 10 nonzero components"),
            (FIELD_THEORY_WOLFRAM, "omega_components", "omega_x0,(x0)(x4) = h4 sb Cot[z]",
             r"$\omega_{x_0,\,04} = h_4e^{-a_4}b_4^{1/2}\cot z$"),
            (FIELD_THEORY_WOLFRAM, "omega_components", "omega_t,(x0)(t) = H (Sin[z]^2)^(1/12)",
             r"$\omega_{x_t,\,0t} = H(\sin^2 z)^{1/12}$"),
            (FIELD_THEORY_WOLFRAM, "gammaOmega_per_direction", "h4 = b4'/(2 b4) - a4'",
             r"$h_4 = \frac{b_4'}{2b_4} - a_4'$"),
            (FIELD_THEORY_WOLFRAM, "gammaOmega_per_direction",
             "gamma^(xt) Omega_xt = (h4/2) gamma^(x4) + (H/2) E^a4 b4^(-1/2) gamma^(x0)",
             r"each extra time $\frac{h_4}{2}\gamma^4 + \frac{H}{2}e^{a_4}b_4^{-1/2}\gamma^0$"),
            (FIELD_THEORY_WOLFRAM, "gammaOmega_total",
             "gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)",
             r"\gamma^\mu\Omega_\mu = c_g\,\gamma^0 + v_g\,\gamma^4,\qquad c_g = \tfrac32He^{a_4}b_4^{-1/2},"
             r"\qquad v_g = \frac{b_4'}{b_4} - \frac{a_4'}{2}"),
            (FIELD_THEORY_PYTHON, "gamma_mu_Omega_mu_equals_hidden_block_terms",
             "gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)",
             r"c_g = \tfrac32He^{a_4}b_4^{-1/2}"),
            (FIELD_THEORY_WOLFRAM, "nontriviality_1_dirac16complex",
             "gamma^mu d_mu = E^a4 b4^(-1/2) Tan[z] gamma^(x0) d0 + E^-a4 gamma^(xi) d_i + gamma^(x4) d4",
             r"e^{a_4}b_4^{-1/2}\tan z\,\gamma^0\partial_0\Psi + e^{-a_4}\big(\gamma^1\partial_1+\gamma^2\partial_2"
             r"+\gamma^3\partial_3\big)\Psi + \gamma^4\partial_4\Psi"),
            (FIELD_THEORY_WOLFRAM, "nontriviality_1_dirac16complex", "E^a4 b4^(-1/2) (Sin[z]^2)^(-1/12) gamma^(xt) d_t",
             r"e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}\big(\gamma^5\partial_5"),
            (FIELD_THEORY_WOLFRAM, "nontriviality_1_dirac16complex", "cg = (3/2) H E^(H x4/3), vg = (5/6) H",
             r"$c_g = \frac32He^{Hx_4/3}$, $v_g = \frac56H$"),
            (FIELD_THEORY_WOLFRAM, "nontriviality_1_dirac16complex", "G^2 = H^2 ((9/4) E^(2 H x4/3) - 25/36)",
             r"$G^2 = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})I_{16}$, which is positive for $x_4 \geq 0$"),
            (FIELD_THEORY_WOLFRAM, "nontriviality_2_dirac16complex00", "G^2 = H^2 ((9/4) E^(2 H x4/3) - 25/36)",
             r"$G^2 = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})I_{16}$"),
            (FIELD_THEORY_PYTHON, "gravity_term_square", "M M = H^2 ((9/4) e^(2 H x4/3) - 25/36) I16",
             r"$G^2 = H^2(\frac94e^{2Hx_4/3} - \frac{25}{36})I_{16}$"),
            (FIELD_THEORY_WOLFRAM, "flat_member_and_curvature", "the corrected metric is FLAT for a4 = 0, b4 = H^2 x4^2",
             r"$a_4 = 0$, $b_4 = H^2x_4^2$ (`flat_member_and_curvature`)"),
            (FIELD_THEORY_PYTHON, "curvature_and_flat_member", "the metric is FLAT for a4 = 0, b4 = H^2 x4^2",
             r"$a_4 = 0$, $b_4 = H^2x_4^2$ (`flat_member_and_curvature`)"),
            (SCOPE_WOLFRAM, "rescaling_removes_the_connection_term", "Psi = E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) chi",
             r"$\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$"),
            (SCOPE_PYTHON, "rescaling_removes_the_connection_term", "Psi = e^(a4/2) b4^(-1) (sin^2 z)^(-1/8) chi",
             r"$\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$"),
            (SCOPE_WOLFRAM, "rescaled_equation_quadratic_potential", "lambda E^a4 S[chi]/(b4^2 |Sin z|^(1/2))",
             r"$\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$"),
            (SCOPE_WOLFRAM, BRANE_NAMED_CHECK, "the degenerate points z = Pi/2 + n Pi of g00",
             r"the degenerate points $z = \pi/2 + n\pi$"),
            (SCOPE_WOLFRAM, "good_sector_x0_independent_modes_without_boundary_condition",
             "wherever m^2 < cg^2 the instantaneous frequencies are imaginary",
             r"complex frequencies wherever $m^2 < c_g^2$"),
            (WOLFRAM_PAIRING, "T2_mirror_is_isometry", "x0 -> pi/(6H) - x0 (z -> pi - z)",
             r"$\phi: x_0 \mapsto \pi/(6H) - x_0$ ($z \mapsto \pi - z$"),
            (WOLFRAM_PAIRING, "T2_mirror_is_isometry", "(g_00 = e^-2a4 b4 cot^2 z = 0, sqrt|g| = 0)",
             r"($g_{00} = e^{-2a_4}b_4\cot^2 z = 0$ and $\sqrt{|g|} = 0$ there)"),
            (WOLFRAM_PAIRING, "T2_mirror_is_isometry", "sqrt|g| = e^-a4 b4^2 |cot z| sin^(1/2) z is invariant",
             r"($e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ is invariant"),
            (WOLFRAM_PAIRING, "T2_mirror_is_isometry", "(no Z2 orbifold)", "the corrected metric has no Z2 orbifold"),
        )
        for path, name, in_report, in_document in quoted:
            self.assertIn(in_report, check_detail(path, name), f"{name} of {path.name}")
            self.assertIn(in_document, self.text, in_document)
        # section 2.1: the history of the Kohn-Sham record, A = 1 and b4(0) = 1
        history = load_json(KS_THEORY)["adiabaticity"]["history"]
        for part in ("a4 = A H x4 (A = 1 canonical)", "b4 = b4(0) e^{beta A H x4} (beta = 4/3, b4(0) = 1)",
                     "f = e^{(beta/2 - 1) a4} = e^{-a4/3}"):
            self.assertIn(part, history, part)
        self.assertIn(r"$b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = 1$ and $b_4(0) = 1$ (`Revision/SPEC.md` section 1; "
                      r"`Revision/kohn_sham/ks-theory.json`, key adiabaticity), that is $a_4 = Hx_4$, "
                      r"$b_4 = e^{(4/3)Hx_4}$, on which the scale factor of the block is $b_4(0)^{1/2}e^{-a_4/3} = "
                      r"e^{-a_4/3}$", self.text)
        # the range of G^2 > 0 on the history: (9/4) e^(2 H x4/3) > 25/36 exactly where e^(2 H x4/3) > 25/81
        x = sp.Symbol("x", positive=True)
        self.assertEqual(sp.solve(sp.Rational(9, 4) * x - sp.Rational(25, 36), x), [sp.Rational(25, 81)])
        self.assertIn(r"vanishes where $e^{2Hx_4/3} = \frac{25}{81}$, at a negative $x_4$", self.text)

    def test_reproduction_commands(self):
        """Section 10: the field-theory record runs in parts (the usage of its two programs)."""
        wolfram = (REVISION / "theory" / "wolfram" / "verify_field_theory.wls").read_text(encoding="utf-8")
        python = (REVISION / "theory" / "python" / "check_field_theory.py").read_text(encoding="utf-8")
        block = self.text[self.text.index("## 10. Reproduction"):self.text.index("## 11. What is proved")]
        commands = [f"wolframscript -file Revision/theory/wolfram/verify_field_theory.wls {part}"
                    for part in ("base", "emt-G", "emt-C", "solutions", "solutions-G", "quantisation", "merge")]
        commands += ["python Revision/theory/python/check_field_theory.py --part nonlinear",
                     "python Revision/theory/python/check_field_theory.py"]
        for command in commands[:7]:
            self.assertIn(command + "\n", wolfram, command)
        self.assertIn(commands[7], python)
        positions = []
        for command in commands:
            self.assertIn("\n" + command + "\n", block, command)
            positions.append(block.index("\n" + command + "\n"))
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("\nwolframscript -file Revision/theory/wolfram/verify_field_theory.wls\n", block)
        self.assertLess(block.index("\n" + commands[-1] + "\n"),
                        block.index("\nwolframscript -file Revision/pairing/wolfram/verify_pairing.wls\n"))

    def test_t3_record_and_its_checks(self):
        theory = load_json(T3_THEORY)
        self.assertEqual(theory["status"], "all checks of the report passed")
        statement = " ".join(theory["statement"])
        self.assertIn("(-m, +lambda, Pi - theta)", statement)
        self.assertIn("EQUAL Kohn-Sham levels", statement)
        self.assertTrue(any("ASSUMED" in h for h in theory["hypotheses"]))
        cited = set(cited_check_names(self.text))
        for path in (WOLFRAM_T3, PYTHON_T3):
            total, passed, failed = count_report(path)
            self.assertEqual((passed, failed), (total, 0), path.name)
            for check in load_json(path)["checks"]:
                self.assertIn(check["name"], cited, f"{check['name']} of {path.name}")
        self.assertEqual(theory["verification"], [c["name"] for c in load_json(WOLFRAM_T3)["checks"]])

    def test_a4_vacuum_statements(self):
        """Corollary C1 for the corrected metric: the vacuum statements of the a4 and b4 equations."""
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("a4 = 0, b4 = H^2 (x4 - c)^2", check_detail(path, "einstein_flat_vacuum"), path.name)
            self.assertIn("Lambda = 0", check_detail(path, "einstein_flat_vacuum"), path.name)
        self.assertIn("is a vacuum solution, for any A, beta, Lambda", check_detail(A4_WOLFRAM, "einstein_no_exponential_vacuum"))
        self.assertIn("no solution with k > 0 for any Lambda", check_detail(A4_PYTHON, "einstein_no_exponential_vacuum"))
        self.assertIn(r"the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves the vacuum equations with $\Lambda = 0$, "
                      r"while no exponential history", self.text)
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("no exponential history is a vacuum solution",
                          check_detail(path, "author_weights_no_exponential_vacuum"), path.name)
        self.assertIn(r"no exponential history is a vacuum solution. (c)", self.text)
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("alpha2 = -1/(4 H^2 (A^2 - k", check_detail(path, "egb_exponential_vacuum_branches"), path.name)
        self.assertIn("where k varies there is no vacuum exponential history",
                      check_detail(A4_WOLFRAM, "egb_exponential_vacuum_branches"))
        self.assertIn("no solution with H != 0", check_detail(A4_PYTHON, "egb_no_vacuum_where_k_varies"))
        self.assertIn(r"there is no vacuum exponential history where $k$ varies", self.text)
        self.assertIn("the vacuum histories are exactly those with k0 != A^2",
                      check_detail(A4_WOLFRAM, "egb_exponential_vacuum_branches"))
        self.assertIn(r"the vacuum histories are exactly those with $k_0 \neq A^2$", self.text)
        self.assertIn(r"the tuned coupling $\alpha_2 = -1/(4H^2(A^2 - k_0))$", self.text)
        # Lambda is tuned as well (the x4 component at the history), not free
        self.assertIn("and Lambda = -E^x4_x4 at the history", check_detail(A4_WOLFRAM, "egb_exponential_vacuum_branches"))
        self.assertIn("a vacuum exists only for these tuned couplings",
                      check_detail(A4_WOLFRAM, "egb_exponential_vacuum_branches"))
        self.assertIn("determine alpha2 = -1/(4 H^2 (A^2 - k)) and Lambda",
                      check_detail(A4_PYTHON, "egb_exponential_vacuum_branches"))
        self.assertIn(r"and a tuned $\Lambda$, fixed by the $x_4$ component of the vacuum equations at the history: "
                      "a vacuum exists only for these tuned couplings.", self.text)
        self.assertIn("w = (1, 1/32, 1/1152)", check_detail(A4_WOLFRAM, "author_weights_history_source"))
        # the sign convention of Lambda: the record's Lam = -10 is the author's Lambda = 10 (SPEC section 1)
        self.assertIn("Lambda_author = 10, Lam = -10", check_detail(A4_WOLFRAM, "author_weights_history_source"))
        self.assertIn("Lambda = 10; the notebook's Out[134]/Out[135]", (REVISION / "SPEC.md").read_text(encoding="utf-8"))
        self.assertIn(r"$\Lambda = -10$ in the sign convention of the equations in (i), which is the author's "
                      r"$\Lambda = 10$ of `Revision/SPEC.md` section 1", self.text)
        self.assertIn(r"$\Lambda = -10$ (the sign convention of section 7)", self.text)

    def test_kohn_sham_self_test_numbers(self):
        detail = check_detail(KS_SOLVER, "t3_block_map_solver_selftest")
        self.assertIn("NOT a proof of T3", detail)
        for number in ("3.62e-13", "1e-9", "157.7", "-1.457144423225e-2", "140 levels", "-1.7604533053e0",
                       "2.131", "1.317651779781e2", "324 levels", "-8.1980434559e-1"):
            self.assertIn(number, detail, number)
            self.assertIn(number, self.text, number)
        self.assertIn("labelled in its report as NOT a proof of T3", self.text)

    def test_t3_completion_record_and_demonstrations(self):
        completion = load_json(T3_COMPLETION)
        self.assertEqual(completion["status"], "all checks of the report passed")
        self.assertTrue(any("CONVENTION" in item for item in completion["not_established"]))
        self.assertTrue(any("independently quantised" in item for item in completion["not_established"]))
        cited = set(cited_check_names(self.text))
        for path in (WOLFRAM_T3C, PYTHON_T3C):
            total, passed, failed = count_report(path)
            self.assertEqual((passed, failed), (total, 0), path.name)
            for check in load_json(path)["checks"]:
                self.assertIn(check["name"], cited, f"{check['name']} of {path.name}")
        rust = {check["name"]: check["detail"] for check in load_json(T3_RUST_DEMO)["checks"]}
        reference = {check["name"]: check["detail"] for check in load_json(T3_REFERENCE_DEMO)["checks"]}
        # the numbers of the corrected metric (2026-10-17); the earlier editions are in the git history
        quoted = (
            (rust, "history_is_a_prescribed_background", "a4,0 = [0.0, 0.5, 1.0, 1.5, 2.0]",
             r"at the slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$"),
            (rust, "plus_and_image_runs_converged", "210 states (75 ground, 135 thermal)", "210 states: all 75 ground and 135 Mermin states"),
            (rust, "t3_equal_ground_states", "N = [8.0, 592.0, 2352.0]", "$N$ = 8, 592, 2352"),
            (rust, "plus_reproduces_canonical_matrix", "worst deviation 1.916e-10", "to 1.916e-10"),
            (rust, "t3_equal_ground_states", "worst deviation 1.853e-12, tolerance 1e-09", "1.853e-12 (ground)"),
            (rust, "t3_equal_thermal_states", "worst deviation 3.502e-12, tolerance 1e-09", "3.502e-12 (thermal), tolerance 1e-9"),
            (rust, "negative_control_untransformed_tip", "at least 4.657e-01", "at least 4.657e-01 of its maximum"),
            (rust, "negative_control_untransformed_tip", "in the 210 states where the solver found a self-consistent control state",
             "in all 210 states, in each of which the solver found a self-consistent control state"),
            (rust, "negative_control_untransformed_tip", "in 0 states (none) the solver found none",
             "in each of which the solver found a self-consistent control state"),
            (rust, "negative_control_untransformed_tip", "(e^(-f m y), 0) are localised at the tip instead of the fold",
             "$(e^{-fmy}, 0)$ are localised at the tip instead of the fold"),
            (rust, "negative_control_lambda_sign", "all 150 states", r"in all 150 states with $\lambda \neq 0$"),
            (rust, "negative_control_lambda_sign", "smallest deviation 5.120e-02", "at least 5.120e-02"),
            (reference, "all_members_converged", "18 states", "18 states, finite differences"),
            (reference, "image_frame_theta_pi", "max |difference| 2.80e-14", "exact $k = 0$ image spectra to 2.80e-14"),
            (reference, "t3_equal_ground_states", "13 ground states", "13 ground and 5 Mermin states"),
            (reference, "t3_equal_thermal_states", "5 Mermin states", "13 ground and 5 Mermin states"),
            (reference, "t3_equal_ground_states", "worst 1.332e-14", "1.332e-14 in the ground states"),
            (reference, "t3_equal_thermal_states", "worst 3.159e-14", "3.159e-14 in the Mermin states"),
            (reference, "t3_equal_ground_states", "differ by up to 1.81e-04", "differ by up to 1.81e-04"),
            (reference, "negative_control_untransformed_tip", "at least 3.776e+00", "at least 3.776e+00 of its maximum"),
            (reference, "reference_image_equals_rust_image", "agree to 7.311e-11", "agree to 7.311e-11"),
            (reference, "reference_image_equals_rust_image",
             "in 18 of 18 states: E_KS, the EMT integrals and (thermal) mu and Omega agree to 7.311e-11",
             r"(their $E_{KS}$, energy-momentum integrals and, for the Mermin states, $\mu$ and $\Omega$) "
             "agree to 7.311e-11 in all 18 states"),
            (reference, "reference_image_equals_rust_image", "tolerance 1e-08", "in all 18 states, tolerance 1e-8"),
        )
        for details, name, in_report, in_document in quoted:
            self.assertIn(in_report, details[name], name)
            self.assertIn(in_document, self.text, in_document)
        # the reference demonstration solves the slices a4,0 = 0, 1, 2 only
        reference_slices = set(re.findall(r"_a(\d\d)", reference["t3_equal_ground_states"]
                                          + reference["t3_equal_thermal_states"]))
        ground = reference["t3_equal_ground_states"]
        self.assertIn("a4,0 = 0, 1, 2", ground)
        self.assertIn("a4,0 = 0, 2", ground)
        self.assertTrue(reference_slices <= {"00", "10", "20"}, reference_slices)
        self.assertIn(r"the reference demonstration at $a_{4,0} = 0, 1, 2$", self.text)
        self.assertEqual(load_json(T3_RUST_DEMO)["states"], 210)
        self.assertEqual(load_json(T3_REFERENCE_DEMO)["states"], 18)
        self.assertIn("Vol_7(a4,0) = ell^3 v_t e^{(5/3) a4,0}", load_json(T3_RUST_DEMO)["background"])
        self.assertIn(r"$\mathrm{Vol}_7(a_{4,0}) = \ell^3v_te^{(5/3)a_{4,0}}$", self.text)

    def test_ks_source_numbers(self):
        """The Kohn-Sham states as sources of the a4 and b4 equations (corrected metric, section 8.4)."""
        report = load_json(KS_SOURCE_A4)
        self.assertIn("corrected primordial metric of 2026-10-16 (version 2", report["metric"])
        self.assertEqual(report["summary"], {"checks": 19, "pass": 19, "fail": 0})
        self.assertIn("`Revision/field_equations_a4/ks_source/reports/ks-source-a4.json`, 19 of 19 checks", self.text)
        self.assertIn("No recorded Kohn-Sham state is an admissible source of the corrected metric",
                      report["conclusions"][0])
        self.assertTrue(any("APPROXIMATION" in item for item in report["assumptions"]))
        self.assertIn("a dimensional reduction that it labels an APPROXIMATION", self.text)
        conditions = load_json(KS_SOURCE_CONDITIONS)
        self.assertIn("corrected metric of 2026-10-16 (version 2", conditions["metric"])
        self.assertEqual(conditions["summary"], {"checks": 5, "pass": 5, "fail": 0})
        self.assertIn("`Revision/field_equations_a4/reports/ks-source-conditions.json` (5 of 5 checks)", self.text)
        self.assertIn("No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the corrected metric",
                      conditions["conclusion"])
        self.assertIn("prescribed background without back-reaction", conditions["conclusion"])
        self.assertIn("is therefore a PRESCRIBED background without back-reaction", self.text)
        details = {check["name"]: check["detail"] for check in conditions["checks"]}
        details.update({check["name"]: check["detail"] for check in report["checks"]})
        quoted = (
            ("ks_profiles_depend_on_x0", "75 ground-state profiles", "Of the 75 recorded ground states, 70 have"),
            ("ks_profiles_depend_on_x0", "(70 with a nonzero energy-momentum tensor)", "70 have a nonzero energy-momentum tensor"),
            ("ks_profiles_depend_on_x0", "(max rho - min rho)/max|T| >= 0.456213",
             r"$(\max\rho - \min\rho)/\max|T| \geq 0.456213$"),
            ("ks_hidden_pressure_condition", "for exactly the 10 nonzero states with lambda = 0",
             r"for the 10 nonzero states with $\lambda = 0$"),
            ("ks_hidden_pressure_condition", "fails (> 1e-06) for every one of the 60 states with lambda != 0",
             r"fails for all 60 states with $\lambda \neq 0$"),
            ("ks_zero_source_states_listed", "5 states have an identically vanishing energy-momentum tensor",
             "the 5 states with an identically vanishing tensor"),
            ("ks_history_is_a_prescribed_background", "a4,0 = 0 (kk = 1): kappa rho = 3.57407",
             r"$\kappa\rho$ = 3.57407 at $a_{4,0} = 0$"),
            ("ks_history_is_a_prescribed_background", "a4,0 = 2 (kk = 3.79367): kappa rho = -7.63383",
             r"-7.63383 at $a_{4,0} = 2$"),
            ("ks_history_is_a_prescribed_background", "kappa rho > 0 at every slice: False",
             "a source whose energy density changes sign"),
            ("ks_history_is_a_prescribed_background", "differ from the needed ones by at least 1.3733",
             "differ from the needed ones by at least 1.3733"),
            ("B3_hidden_direction_mismatch", "mu1_rho in [0.147738, 0.738255]", "between 0.147738 and 0.738255"),
            ("C3_record_history_not_sourced_by_the_gas", "run from 16.5276 to -7311.81", "run from 16.5276 to -7311.81"),
            ("C3_record_history_not_sourced_by_the_gas", "of the free gas N = 2352 is positive at every slice",
             r"of the free gas with $N = 2352$ is positive at every slice"),
        )
        for name, in_report, in_document in quoted:
            self.assertIn(in_report, details[name], name)
            self.assertIn(in_document, self.text, in_document)

    def test_reverification_record(self):
        """Section 9.3: the sha256 of the pairing record equal the committed files and the provenance entry."""
        provenance = (REVISION / "pairing" / "wolfram" / "WOLFRAMSCRIPT_PROVENANCE.md").read_text(encoding="utf-8")
        entry = provenance[provenance.index("* **The corrected metric of 2026-10-16, version 2 (2026-10-17):**"):]
        for path in (PAIRING_THEORY, WOLFRAM_PAIRING, PYTHON_PAIRING,
                     REVISION / "pairing" / "wolfram" / "verify_pairing.wls",
                     REVISION / "pairing" / "wolfram" / "RevisionPairing.wl",
                     REVISION / "pairing" / "python" / "check_pairing.py"):
            digest = sha256_file(path)
            self.assertIn(digest, entry, path.name)
            self.assertIn(f"`{digest}` (`", self.text, path.name)
        for statement in ("`verify_pairing.wls` `102/102 checks passed; time 82.33 s` (85 s of wall time)",
                          "`check_pairing.py` 67 PASS, 0 FAIL in 177.9 s (179 s of wall time)"):
            self.assertIn(statement, entry, statement)
        self.assertIn("`verify_pairing.wls` 102 of 102 checks in 82.33 s of kernel time (85 s of wall time)", self.text)
        self.assertIn("`check_pairing.py` 67 of 67 in 177.9 s (179 s of wall time)", self.text)
        self.assertEqual(count_report(WOLFRAM_PAIRING), (102, 102, 0))
        self.assertEqual(count_report(PYTHON_PAIRING), (67, 67, 0))
        readme = (REVISION / "pairing" / "kohn_sham" / "README.md").read_text(encoding="utf-8")
        self.assertIn("in four parts of 88, 91, 76 and 67 s and an assembly of 2 s", readme)
        self.assertIn("in four parts of 88, 91, 76 and 67 s and an assembly of 2 s", self.text)
        self.assertIn("in six parts of 219, 170, 78, 122, 115 and 91 s", readme)
        self.assertIn("in six parts of 219, 170, 78, 122, 115 and 91 s", self.text)

    def test_t3_reverification_record(self):
        """Section 9.3 item 2: the T3 runs are those of sections 6.9 and 6.10 of the T3 provenance."""
        provenance = T3_PROVENANCE.read_text(encoding="utf-8")
        start = provenance.index("### 6.9 The corrected metric of 2026-10-16 (version 2) (2026-10-17)")
        middle = provenance.index("### 6.10 Text-only corrections of the W6 audit (2026-10-17)")
        following = re.search(r"\n#{2,3} ", provenance[middle + 1:])
        end = middle + 1 + following.start() if following else len(provenance)
        runs = " ".join(provenance[start:middle].split())
        regeneration = " ".join(provenance[middle:end].split())
        text = " ".join(self.text.split())
        # section 6.9: the runs that reproduced the outputs of commit 6e228a8
        for statement in ("`verify_t3.wls` `9/9 checks passed` (5.8 s of wall time)",
                          "`check_t3.py` 12 of 12 (1.3 s)",
                          "`verify_t3_completion.wls` `3/3 checks passed` (2.9 s)",
                          "`check_t3_completion.py` 7 of 7 (0.9 s)"):
            self.assertIn(statement, runs, statement)
        reproduced = ("reproduced the committed `t3-theory.json`, `reports/wolfram-t3.json`, `reports/python-t3.json` "
                      "and `reports/wolfram-t3-completion.json` of commit `6e228a8` byte for byte")
        self.assertIn(reproduced, runs)
        self.assertIn(reproduced, text)
        self.assertIn("`verify_t3.wls` 9 of 9 checks (5.8 s of wall time), `check_t3.py` 12 of 12 (1.3 s), "
                      "`verify_t3_completion.wls` 3 of 3 (2.9 s) and `check_t3_completion.py` 7 of 7 (0.9 s)", text)
        readme = (REVISION / "pairing" / "kohn_sham" / "README.md").read_text(encoding="utf-8")
        self.assertIn("the T3 verifiers 5.8 s and 1.3 s, the completion 2.9 s and 0.9 s", " ".join(readme.split()))
        # section 6.10: the single regeneration run that wrote the committed T3 reports (commit 0a0be28)
        for statement in ("`9/9 checks passed; time 0.30000000000000004 s` (4.6 s)", "`pass 12 fail 0` (1.2 s)",
                          "ending `3/3 checks passed` (2.9 s)", "`pass 7 fail 0` (0.8 s)",
                          "No check, verdict or count changed",
                          "the four changed outputs committed in `0a0be28`",
                          "A second run of the four scripts at 13:53 PDT, in the same order and under the same limit "
                          "(3.1 s, 1.5 s, 2.8 s, 0.9 s; the same counts), left every output of sections 2.3 and 2.4 "
                          "byte for byte unchanged"):
            self.assertIn(statement, regeneration, statement)
        for path in (WOLFRAM_T3, PYTHON_T3, WOLFRAM_T3C, T3_COMPLETION):
            self.assertIn(f"-> `{sha256_file(path)}`", regeneration, path.name)
        unchanged = regeneration[regeneration.index("Unchanged:"):]
        for path in (T3_THEORY, PYTHON_T3C):
            self.assertIn(f"`{sha256_file(path)}`", unchanged, path.name)
        self.assertIn("one further run of each script, with the same counts (4.6 s, 1.2 s, 2.9 s and 0.8 s of wall "
                      "time), wrote the four changed outputs `reports/wolfram-t3.json`, `reports/python-t3.json`, "
                      "`reports/wolfram-t3-completion.json` and `t3-completion.json` committed in `0a0be28`", text)
        self.assertIn("a second run of the four scripts at 13:53 PDT (3.1 s, 1.5 s, 2.8 s and 0.9 s; the same counts) "
                      "left every output of the T3 verifiers and checkers byte for byte unchanged", text)
        self.assertEqual([count_report(path) for path in (WOLFRAM_T3, PYTHON_T3, WOLFRAM_T3C, PYTHON_T3C)],
                         [(9, 9, 0), (12, 12, 0), (3, 3, 0), (7, 7, 0)])
        # the run times of an earlier draft (13:16 PDT; 3.1 s, 1.2 s, 2.8 s, 0.8 s) are in no record
        self.assertNotIn("13:16", self.text)
        self.assertNotIn("in 2.8 s", self.text)

    def test_further_quoted_numbers(self):
        wolfram = {check["name"]: check["detail"] for check in load_json(WOLFRAM_PAIRING)["checks"]}
        pairs = (
            ("pointwise_field_is_general", "1411/6561", "$\\det e = 1411/6561$"),
            ("pointwise_field_is_general", "448 of the 512", "448 of the 512 connection components"),
            ("Q_one_particle_general_field", "-2307429/1990921", "-\\frac{2307429}{1990921}"),  # -2269482 before 2026-10-14
            ("T1_Lagrangian_primordial_commuting", "408 monomials", "(408 monomials)"),
            ("T1_Lagrangian_primordial_grassmann", "392 monomials", "(392 monomials)"),
            ("T1_kernel_connection", "all 512 triples", "(all 512 triples)"),
        )
        for name, in_report, in_document in pairs:
            self.assertIn(in_report, wolfram[name], name)
            self.assertIn(in_document, self.text, in_document)
        python = {check["name"]: check["detail"] for check in load_json(PYTHON_PAIRING)["checks"]}
        self.assertIn("456 kinetic and connection basis matrices", python["T1.general_field.matrix_identities"])
        self.assertIn("(456 kinetic and connection basis matrices)", self.text)
        self.assertIn("[('-m', 16), ('m', 16)]", python["Q.no_cancellation_independent_universes"])
        self.assertIn("has the eigenvalues $-m$ and $m$, each 16 times", self.text)


if __name__ == "__main__":
    unittest.main()
