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
    occurs only inside the quoted request; T3 and pair creation are never called proved);
  * every check name the document cites exists in a Revision report with the verdict PASS, and every
    check of the two pairing reports is listed (complete verification records);
  * the report-count table equals the counts recomputed from the reports;
  * the quoted data (reflection table, Krein signs, one-particle samples, the a4 vacuum polynomial,
    the Kohn-Sham self-test numbers, the numbers of the T3 completion and its two numerical
    demonstrations, and further numbers) agree with the Revision reports;
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

MARKDOWN_SHA256 = "f0afa9193f210b228f7976846f76388696044b328ac7a42e9a47b01dfddffc68"
TEX_SHA256 = "a5641fcfb8a9477989ddcbf8addd474436fa20d4e064c65ee1068f257d191d2b"

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
KS_SOLVER = REVISION / "kohn_sham" / "reports" / "ks-rust-solver.json"
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
    "## 7. Corollary C1: a T1 pair as the source of the field equations for $a_4$",
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
    "with the ASSUMED Z2 mirror construction",
    "identical one-particle ($\\lambda = 0$) spectra (flat space, or frozen coefficients at a point)",
    "No creation process, rate or amplitude follows from these equations.",
    "Not proved: that such universes are CREATED, in pairs or otherwise.",
    r"$\mathcal{L}_{m,\lambda}[\Gamma\Psi] = -\mathcal{L}_{-m,-\lambda}[\Psi]$",
    r"$E_{m,\lambda}[\Gamma\Psi] = -\Gamma E_{-m,-\lambda}[\Psi]$",
    r"$T^{(-m,-\lambda)}_{\mu\nu}[\Gamma\Psi] = -T^{(m,\lambda)}_{\mu\nu}[\Psi]$",
    r"$\mathcal{L}_{m,\lambda}[\gamma^n\Psi;\,R_ne] = +\mathcal{L}_{-m,\lambda}[\Psi;\,e]$",
    r"$E_{m,\lambda}[\gamma^n\Psi;\,R_ne] = -\gamma^nE_{-m,\lambda}[\Psi;\,e]$",
    "the energy density and every component without an $x_8$ index are EQUAL, not opposite",
    "The chirality image $\\chi = \\Gamma\\Psi$ carries the Krein metric $-B$",
    "no cancellation $P_1 + P_2 = 0$ follows",
    "The T2 image $\\gamma^8\\Psi$ keeps the anticommutator $+B$",
    "the ASSUMED Z2 construction of `Revision/SPEC.md` section 7",
    "the same occupations, chemical potential, particle number and entropy, EQUAL Kohn-Sham energy",
    "for every REAL frequency ($w^2 > 0$, with or without extra-time momentum)",
    "The field is a fixed (test) background: it is NOT varied",
    "dirac16complex00 is a classical field and has no quantum reading.",
    "they neither use nor establish a positive-norm Fock space for either universe",
    "a T1 pair cannot by itself be the source of the author's metric in Einstein gravity",
    "1. No creation process:",
    "2. No rate, probability or amplitude:",
    "3. No dynamical necessity:",
    "10. The Kohn-Sham level T3 holds for the instantaneous (adiabatic) mean-field Kohn-Sham states only",
    "### 8.5 Completion of T3 (2026-10-08)",
    "T3 and its statements S1 to S5 are unchanged.",
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
        self.assertIn("are $" + ", ".join(signs) + "$ for $n = x_1, \\dots, x_8$", self.text)

    def test_krein_signs(self):
        signs = {entry["map"]: entry["sign"] for entry in self.theory["data"]["Krein_signs_M_B_Mdagger"]}
        self.assertEqual(signs["Gamma"], -1)
        for name in ("gamma^x1", "gamma^x2", "gamma^x3", "gamma^x4", "gamma^x8"):
            self.assertEqual(signs[name], 1, name)
        for name in ("gamma^x5", "gamma^x6", "gamma^x7"):
            self.assertEqual(signs[name], -1, name)
        for n in range(1, 9):
            self.assertEqual(signs[f"P_x{n}"], -signs[f"gamma^x{n}"], n)
        self.assertIn(r"$\sigma_{\gamma^n} = +1$ for $n = x_1, x_2, x_3, x_4, x_8$ and $-1$ for "
                      r"$n = x_5, x_6, x_7$", self.text)
        self.assertIn(r"$-1$ for $P_{x_1}, P_{x_2}, P_{x_3}, P_{x_4}, P_{x_8}$ and $+1$ for "
                      r"$P_{x_5}, P_{x_6}, P_{x_7}$", self.text)

    def test_one_particle_samples(self):
        data = self.theory["data"]["one_particle_flat"]
        self.assertEqual(data["hamiltonian"],
                         "h_m(k) = -i m gamma^(x4) - gamma^(x4) sum_(a != x4) k_a gamma^a")
        self.assertIn("(m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2)", data["square"])
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
            w_value = sp.sqrt(m**2 + ks[0]**2 + ks[1]**2 + ks[2]**2 + ks[7]**2
                              - ks[4]**2 - ks[5]**2 - ks[6]**2)
            self.assertEqual(sp.simplify(w_value - sp.sympify(re.sub(r"Sqrt\[(\d+)\]", r"sqrt(\1)", w))), 0)

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

    def test_a4_vacuum_polynomial(self):
        a1, a2, a3, h, a = sp.symbols("alpha1 alpha2 alpha3 H AA")
        document_v = a1 - 40*a2*h**2 - 8*a**2*a2*h**2 + 360*a3*h**4 + 144*a**2*a3*h**4 + 72*a**4*a3*h**4
        self.assertIn(r"V = \alpha_1 - 40\alpha_2H^2 - 8A^2\alpha_2H^2 + 360\alpha_3H^4 "
                      r"+ 144A^2\alpha_3H^4 + 72A^4\alpha_3H^4", self.text)
        for path in (A4_WOLFRAM, A4_PYTHON):
            detail = check_detail(path, "linear_member_vacuum_factor")
            match = re.search(r"V = ([^;]+?)(?:;|$)", detail)
            self.assertIsNotNone(match, path.name)
            expression = sp.sympify(match.group(1).replace("^", "**"),
                                    locals={"alpha1": a1, "alpha2": a2, "alpha3": a3, "H": h, "AA": a})
            self.assertEqual(sp.expand(expression - document_v), 0, path.name)
        detail = check_detail(A4_WOLFRAM, "einstein_no_vacuum_solution")
        self.assertIn("36 H^2 + 2 Lambda = 0", detail)
        self.assertIn("6 a4'^2 + 6 H^2 = 0", detail)
        self.assertIn(r"$36H^2 + 2\Lambda = 0$ and $6(a_4')^2 + 6H^2 = 0$", self.text)
        detail = check_detail(A4_WOLFRAM, "einstein_gauss_bonnet_vacuum_linear")
        self.assertIn("A^2 = (1 - 40 alpha2 H^2)/(8 alpha2 H^2)", detail)
        self.assertIn("0 < alpha2 H^2 <= 1/40", detail)
        self.assertIn(r"$A^2 = (1 - 40\alpha_2H^2)/(8\alpha_2H^2)$", self.text)
        self.assertIn(r"$0 < \alpha_2H^2 \leq 1/40$", self.text)

    def test_kohn_sham_self_test_numbers(self):
        detail = check_detail(KS_SOLVER, "t3_block_map_solver_selftest")
        self.assertIn("NOT a proof of T3", detail)
        for number in ("9.95e-14", "1e-9", "0.01946", "-9.868426190876e-4", "-9.868426190868e-4",
                       "80 levels", "-2.0145243719e0", "0.0009298", "3.239294915318e1",
                       "160 levels", "2.9283751318e1"):
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
        quoted = (
            (rust, "plus_and_image_runs_converged", "210 states (75 ground, 135 thermal)", "210 states: all 75 ground and 135 Mermin states"),
            (rust, "plus_reproduces_canonical_matrix", "2.538e-10", "2.538e-10"),
            (rust, "t3_equal_ground_states", "worst deviation 2.179e-13, tolerance 1e-09", "2.179e-13 (ground)"),
            (rust, "t3_equal_thermal_states", "worst deviation 3.877e-12, tolerance 1e-09", "3.877e-12 (thermal), tolerance 1e-9"),
            (rust, "negative_control_untransformed_tip", "at least 4.750e+00", "at least 4.750e+00 of its maximum"),
            (rust, "negative_control_untransformed_tip", "in the 196 states", "196 states with a converged control"),
            (rust, "negative_control_untransformed_tip", "in 14 states", r"in 14 states, all with $\lambda < 0$"),
            (rust, "negative_control_lambda_sign", "all 150 states", r"in all 150 states with $\lambda \neq 0$"),
            (rust, "negative_control_lambda_sign", "smallest deviation 1.210e-02", "at least 1.210e-02"),
            (reference, "all_members_converged", "18 states", "18 states, finite differences"),
            (reference, "t3_equal_ground_states", "worst 2.043e-14", "2.043e-14 in the ground states"),
            (reference, "t3_equal_ground_states", "up to 2.23e-04", "differ by up to 2.23e-04"),
            (reference, "negative_control_untransformed_tip", "at least 5.296e+00", "at least 5.296e+00 of its maximum"),
            (reference, "reference_image_equals_rust_image", "agree to 1.255e-11", "agree to 1.255e-11"),
        )
        for details, name, in_report, in_document in quoted:
            self.assertIn(in_report, details[name], name)
            self.assertIn(in_document, self.text, in_document)
        # the 14 states without a converged control all have lambda < 0 (tag lamm)
        detail = rust["negative_control_untransformed_tip"]
        states = re.search(r"in 14 states \(([^)]*)\)", detail).group(1).split(", ")
        self.assertEqual(len(states), 14)
        self.assertTrue(all("_lamm" in state for state in states), states)

    def test_ks_source_numbers(self):
        report = load_json(KS_SOURCE_A4)
        self.assertEqual(report["summary"], {"checks": 23, "pass": 23, "fail": 0})
        self.assertIn("23 of 23 checks", self.text)
        self.assertIn("EXACT: no recorded Kohn-Sham state is an admissible source", report["conclusions"][0])

    def test_further_quoted_numbers(self):
        wolfram = {check["name"]: check["detail"] for check in load_json(WOLFRAM_PAIRING)["checks"]}
        pairs = (
            ("pointwise_field_is_general", "1411/6561", "$\\det e = 1411/6561$"),
            ("pointwise_field_is_general", "448 of the 512", "448 of the 512 connection components"),
            ("Q_one_particle_general_field", "-2269482/1990921", "-\\frac{2269482}{1990921}"),
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
