#!/usr/bin/env python3
"""Publication test for Revision/docs/LOVELOCK_GKD.{md,tex,pdf}.

The document records the generalized Kronecker delta GKD (pure Rust) and the Lovelock tensors
P_(k), A_(k), L_(k), k = 1, 2, 3, of Lovelock's equation (4.38) for the author's primordial metric
(Revision/gkd_lovelock), their independent verifications (Wolfram, sympy), the comparison with the
author's notebooks (Revision/gkd_lovelock/comparison), their use by Revision/field_equations_a4, and
what is not established (Revision/SPEC.md section 10, document 6).  It is built and registered with

    python scripts/build_provenance_pdf.py Revision/docs/LOVELOCK_GKD.md \
        --developer-layout --specifications Revision/pdf-specifications.json [--register]

Run from the repository root:
    python -m unittest Revision/tests/test_lovelock_gkd_publication.py -v

What is tested
  * the committed .tex is exactly the builder's output for the committed .md (same options as the
    build command above), both files are UTF-8 with LF line endings, and their sha256 are pinned;
  * the PDF is registered in the Revision registry Revision/pdf-specifications.json (edition
    lovelock-gkd: path, page count and sha256 of the committed PDF) and NOT in the registry of the
    earlier stages (provenance/pdf-specifications.json); the PDF is structurally sound;
  * title, subtitle and section headings; the last section is "What is established and what is not";
  * key statements are present and overclaims are absent (with negative controls);
  * every identifier the document cites is a PASS check of a Revision report, a key of a JSON file
    of the record, a function or type of the Rust crate (`file.rs::name`), or one of a short list of
    other names that are checked where they come from; every check of the three reports of
    Revision/gkd_lovelock/results is listed;
  * the report-count table and the quoted check counts equal the JSON files;
  * every quoted number is read from its JSON report: the GKD self-test, the Rust, sympy and Wolfram
    counters, the brute-force deviations, the Christoffel and Riemann data, the Ricci and Einstein
    tensors, every listed component of P_(1), P_(2), P_(3), the scalars L_(k), the normalisation
    constants, the identity P^x1 + P^x5 = 2 P^x8, the factor F(a4') of the evolution equation and the
    E_(k) of Revision/field_equations_a4/a4-equations.json; the run times are those of the provenance
    files;
  * the comparison with the author's stored outputs (section 8.2): the counts, the verdict of every
    check in the result table, the mapping, the two worked examples, the controls, the cells used, the
    keyword-scan counts, the notebook and report sha256, the gate steps and the README run times are
    read from Revision/gkd_lovelock/comparison/ (author-comparison-report.json,
    author-curvature-outputs.json, README.md); compare_with_author.py is re-run into a temporary
    directory and must reproduce the committed report byte for byte (about 1 s; skipped when the
    author's notebook is not in the repository root);
  * OPTIONAL (only when REVISION_PDF_REBUILD=1; needs pdflatex, about a minute): the PDF is rebuilt
    in verify mode and must match the registry.

After an intended edit of the document: rebuild in verify mode until warning-free, register it
(--register), and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
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
MARKDOWN = DOCS / "LOVELOCK_GKD.md"
TEX = DOCS / "LOVELOCK_GKD.tex"
PDF = DOCS / "LOVELOCK_GKD.pdf"
EDITION = "lovelock-gkd"
REGISTRY = REVISION / "pdf-specifications.json"
OLD_REGISTRY = ROOT / "provenance" / "pdf-specifications.json"
REBUILD = os.environ.get("REVISION_PDF_REBUILD") == "1"

MARKDOWN_SHA256 = "3e056849126277ff3b07677e5a88d230d0b1109e6bdbc36ac9192f09932612d5"
TEX_SHA256 = "0b9fc2074a676beb42792fc9f3876eea0f52d7bd3e272a6c723ce538e71eb070"

GKD = REVISION / "gkd_lovelock"
RESULTS = GKD / "results"
CRATE_SRC = GKD / "code" / "src"
CURVATURE = RESULTS / "curvature.json"
TENSORS = RESULTS / "lovelock-tensors.json"
RUST_REPORT = RESULTS / "lovelock-report.json"
SELFTEST = RESULTS / "gkd-selftest.json"
PYTHON_REPORT = RESULTS / "python-lovelock-report.json"
WOLFRAM_REPORT = RESULTS / "wolfram-gkd-report.json"
PROVENANCE = RESULTS / "PROVENANCE_OF_THE_COMPUTATION.md"
NB_DIGEST = RESULTS / "notebook-input-cells.txt"
WOLFRAM_PROVENANCE = GKD / "verification" / "WOLFRAMSCRIPT_PROVENANCE.md"
NB_PROVENANCE = GKD / "notebook_reading" / "WOLFRAMSCRIPT_PROVENANCE.md"
CHECKER = GKD / "verification" / "check_lovelock_gkd.py"
WOLFRAM_PACKAGE = GKD / "verification" / "LovelockGKDCheck.wl"
GKD_TEST = REVISION / "tests" / "test_gkd_lovelock.py"
A4_EQUATIONS = REVISION / "field_equations_a4" / "a4-equations.json"
A4_WOLFRAM = REVISION / "field_equations_a4" / "reports" / "wolfram-a4-report.json"
A4_PYTHON = REVISION / "field_equations_a4" / "reports" / "python-a4-report.json"
COMPARISON = GKD / "comparison"
COMPARISON_README = COMPARISON / "README.md"
COMPARISON_REPORT = COMPARISON / "author-comparison-report.json"
AUTHOR_OUTPUTS = COMPARISON / "author-curvature-outputs.json"
COMPARE_PROGRAM = COMPARISON / "compare_with_author.py"
EXTRACTOR = COMPARISON / "extract_author_curvature_outputs.wls"
AUTHOR_NOTEBOOK = ROOT / "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"
GATES = (REVISION / "verify_revision.sh", REVISION / "verify_revision.ps1")

# The reports of the count table (section 10), in the order of the table.
COUNTED_REPORTS = (
    "Revision/gkd_lovelock/results/lovelock-report.json",
    "Revision/gkd_lovelock/results/wolfram-gkd-report.json",
    "Revision/gkd_lovelock/results/python-lovelock-report.json",
    "Revision/field_equations_a4/reports/wolfram-a4-report.json",
    "Revision/field_equations_a4/reports/python-a4-report.json",
)
# Every report whose check names the document may cite.
CITABLE_REPORTS = (RUST_REPORT, WOLFRAM_REPORT, PYTHON_REPORT, A4_WOLFRAM, A4_PYTHON)
# JSON files whose keys the document may cite.
KEYED_FILES = (CURVATURE, TENSORS, RUST_REPORT, SELFTEST, PYTHON_REPORT, WOLFRAM_REPORT, A4_EQUATIONS)

TITLE = "The generalized Kronecker delta and the Lovelock tensors of the author's primordial metric"
SUBTITLE_START = "GKD, the pure-Rust generalized Kronecker delta, and the exact Lovelock tensors of order k = 1, 2, 3"
SECTIONS = (
    "## Abstract",
    "## 1. The task and the result",
    "## 2. Setting and conventions",
    "## 3. The generalized Kronecker delta",
    "## 4. The Lovelock tensors",
    "## 5. How the code computes them",
    "## 6. Results",
    "## 7. Independent verifications",
    "## 8. The comparison with the author's notebooks",
    "## 9. How the field equations for $a_4$ use the Lovelock tensors",
    "## 10. Verification records",
    "## 11. Reproduction",
    "## 12. What is established and what is not",
)
KEY_STATEMENTS = (
    "which DEFLATE exponentially with the scale factor $e^{-a_4}\\sin^{1/6}z$ as $a_4(x_4)$ increases (they are never treated as static)",
    "kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]",
    "**Theorem (GKD).**",
    "E_{(k)}{}^h{}_j = -\\frac{P_{(k)}{}^h{}_j}{2^{k+1}},\\qquad E_{(1)} = G",
    "so $k = 1, 2, 3$ is the complete series in eight dimensions",
    "GKD is NOT re-implemented in Wolfram Language",
    "It shares no code with the Rust crate",
    "Its answers are in its output cells, which were not read for the computation",
    "that comparison is recorded in `Revision/gkd_lovelock/comparison/`",
    "Agreement with the author's own Lovelock tensors of order $k = 2$ and $k = 3$ is therefore not established.",
    "### 8.1 What was read for the computation",
    "### 8.2 The comparison with the author's stored outputs (2026-10-08)",
    "### 8.3 What the comparison does not establish",
    "The mapping (a definition stated before the comparison, not a fit).",
    "is an inference from the file, labelled as such",
    "The notebook was not re-run; its outputs are taken as stored.",
    "NOT-AVAILABLE means that the author's files hold nothing to compare with (it is not a failure)",
    "The $k = 1$ comparison carries no information beyond the Einstein-tensor comparison together with "
    "this record's own identity $P_{(1)} = -4G$",
    "a value stored under an unrelated name would not be found by it",
    "Nothing about field equations, sources, solutions or physical interpretation.",
    "1. No solution: this record gives the left-hand sides of the field equations only.",
    "2. The domain: only the patch $0 < z < \\pi/2$",
    "3. No comparison for $k = 2$ and $k = 3$:",
    "These two run times are measurements made while writing this document; they are not recorded in a report.",
    "(a reading of the digest, labelled as such)",
)
FORBIDDEN = (
    r"\bthe computation (?:read|used|opened) (?:the |an? )?(?:stored )?outputs?\b",
    r"\bconfirm(?:s|ed)? the author's (?:own )?(?:answers|results|tensors|Lovelock tensors)\b",
    r"\b(?:solutions?|a4) (?:of the field equations )?(?:is|are|was|were) (?:proved|derived|established) (?:here|in this (?:record|document))",
    r"\bagreement with the author's (?:own )?(?:Lovelock|Gauss-Bonnet|cubic)[^.]*?\bis (?:now )?established\b",
    r"\$k = [23]\$[^.]*\bagree(?:s|d)? with (?:the author|those of the author)",
    r"\boutput cells? of `?Generalized _Kronecker_Delta_4\+4\.nb`? (?:were|was|has been|have been) (?:read|opened|used|compared)\b",
)
FILE_SUFFIXES = (".json", ".py", ".wls", ".wl", ".md", ".tex", ".pdf", ".rs", ".csv", ".toml", ".txt", ".png", ".nb", ".exe")
# Other identifiers the document cites in code spans, with the file that must contain each.
OTHER_IDENTIFIERS = {
    "SUCCESS": RUST_REPORT,
    "canon": CHECKER,
    "D": WOLFRAM_REPORT,
    "Inverse": WOLFRAM_REPORT,
    "Simplify": WOLFRAM_REPORT,
    "FullSimplify": WOLFRAM_REPORT,
    "lovelock_gkd": GKD / "code" / "Cargo.toml",
    "i128": CRATE_SRC / "rational.rs",
    "delta11": NB_DIGEST,
    "delta22": NB_DIGEST,
    "delta33": NB_DIGEST,
    "delta55": NB_DIGEST,
    "time_total": WOLFRAM_PROVENANCE,
    # section 8.2 (the comparison with the author's stored outputs)
    "Get": COMPARISON_README,
    "MatrixMetric44": AUTHOR_OUTPUTS,
    "RS": AUTHOR_OUTPUTS,
    "EinsteinG": AUTHOR_OUTPUTS,
    "a4": AUTHOR_OUTPUTS,
    "x0": AUTHOR_OUTPUTS,
    "x1": COMPARISON_README,
    "x7": COMPARISON_README,
    "xk": COMPARISON_README,
    "P2": EXTRACTOR,
    "P3": EXTRACTOR,
    "P4": EXTRACTOR,
    "LovelockP": EXTRACTOR,
    "kd": EXTRACTOR,
    "AUTHOR_CURVATURE_OUTPUTS": EXTRACTOR,
}
COMPONENTS = ("x1,x1", "x4,x4", "x5,x5", "x8,x8")
A1, A2, H = sp.symbols("A1 A2 H")
ALPHA = sp.symbols("alpha1 alpha2 alpha3")


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


def cited_identifiers(text: str) -> list[str]:
    """Identifier-like code spans; sha256 values are excluded (each is checked by the test that quotes it)."""
    return [span for span in code_spans(text)
            if not span.endswith(FILE_SUFFIXES) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_.*]*", span)
            and not re.fullmatch(r"[0-9a-f]{64}", span)]


def rust_references(text: str) -> list[tuple[str, str]]:
    refs = []
    for span in code_spans(text):
        match = re.fullmatch(r"([a-z_]+\.rs)::([A-Za-z_][A-Za-z0-9_]*)", span)
        if match:
            refs.append((match.group(1), match.group(2)))
    return refs


def checks_of(path: Path) -> list[tuple[str, str]]:
    """(name, verdict) of every check; the Rust report stores {name: {passed, detail}}."""
    checks = load_json(path)["checks"]
    if isinstance(checks, dict):
        return [(name, "PASS" if entry["passed"] is True else "FAIL") for name, entry in checks.items()]
    return [(check["name"], str(check["verdict"]).upper()) for check in checks]


def report_verdicts() -> dict[str, list[str]]:
    verdicts: dict[str, list[str]] = {}
    for path in CITABLE_REPORTS:
        for name, verdict in checks_of(path):
            verdicts.setdefault(name, []).append(verdict)
    return verdicts


def json_keys(value, keys: set[str]) -> set[str]:
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(key)
            json_keys(item, keys)
    elif isinstance(value, list):
        for item in value:
            json_keys(item, keys)
    return keys


def count_report(path: Path) -> tuple[int, int, int]:
    verdicts = [verdict for _, verdict in checks_of(path)]
    return len(verdicts), verdicts.count("PASS"), verdicts.count("FAIL")


def detail_of(path: Path, name: str) -> str:
    checks = load_json(path)["checks"]
    if isinstance(checks, dict):
        return checks[name]["detail"]
    for check in checks:
        if check["name"] == name:
            return check["detail"]
    raise KeyError(f"{name} not in {path}")


def from_mathematica(text: str) -> sp.Expr:
    """The Mathematica text of a curvature or Lovelock component (no warp factors) as sympy."""
    text = text.replace("Derivative[2][a4][x4]", "A2").replace("Derivative[1][a4][x4]", "A1")
    text = text.replace("^", "**")
    return sp.sympify(text, locals={"A1": A1, "A2": A2, "H": H})


def from_ad(text: str) -> sp.Expr:
    """An expression of the field-equations branch (ad1 = a4', ad2 = a4'')."""
    text = text.replace("^", "**")
    names = {"ad1": A1, "ad2": A2, "H": H, "alpha1": ALPHA[0], "alpha2": ALPHA[1], "alpha3": ALPHA[2]}
    return sp.sympify(text, locals=names)


def normalise_math(text: str) -> str:
    """Remove the line-breaking marks of aligned displays and all white space."""
    return re.sub(r"\s+", "", text.replace("\\\\", "").replace("&\\quad", "").replace("&", ""))


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
        self.assertEqual(entry["path"], "Revision/docs/LOVELOCK_GKD.pdf")
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
        self.assertEqual(level2[-1], "## 12. What is established and what is not")
        self.assertIn("\\section{What is established and what is not}", TEX.read_text(encoding="utf-8"))

    def test_key_statements(self):
        for statement in KEY_STATEMENTS:
            self.assertIn(statement, self.text, statement)

    def test_no_overclaims(self):
        for pattern in FORBIDDEN:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE), pattern)
        self.assertNotRegex(self.text, r"\bproved\b")  # nothing is called proved except the GKD theorem's QED

    def test_negative_controls(self):
        """The content checks are not vacuous: tampered statements are detected."""
        tampered = (
            "The computation used the stored outputs of the author's notebook.",
            "This confirms the author's tensors.",
            "Solutions of the field equations are derived here.",
            "Agreement with the author's own Lovelock tensors is established.",
            "The tensors for $k = 2$ agree with the author.",
            "The output cells of `Generalized _Kronecker_Delta_4+4.nb` were compared.",
        )
        self.assertEqual(len(tampered), len(FORBIDDEN))
        for pattern, sentence in zip(FORBIDDEN, tampered):
            self.assertIsNotNone(re.search(pattern, sentence, re.IGNORECASE), pattern)
        self.assertNotIn("k1_equals_minus_4_einstei", report_verdicts())
        total, passed, failed = count_report(WOLFRAM_REPORT)
        wrong_row = f"| `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | {total + 1} | {passed} | {failed} |"
        self.assertNotIn(wrong_row, self.text)
        p3 = load_json(TENSORS)["P3_mixed_up_h_down_j"]["x8,x8"]["latex"].replace("1152", "1153")
        self.assertNotIn(normalise_math(p3), normalise_math(self.text))

    def test_no_material_of_the_earlier_stages(self):
        for marker in ("artifacts/", "provenance/", "studies/", "notebooks/", "dirac-main", "vendor/"):
            self.assertNotIn(marker, self.text, marker)

    def test_cited_identifiers_exist(self):
        verdicts = report_verdicts()
        keys: set[str] = set()
        for path in KEYED_FILES:
            json_keys(load_json(path), keys)
        cited = cited_identifiers(self.text)
        self.assertGreater(len(cited), 150)
        for name in cited:
            if name in verdicts:
                self.assertTrue(all(v == "PASS" for v in verdicts[name]), name)
            elif name in keys:
                continue
            else:
                self.assertIn(name, OTHER_IDENTIFIERS, name)
                self.assertIn(name, OTHER_IDENTIFIERS[name].read_text(encoding="utf-8"), name)

    def test_rust_references_exist(self):
        refs = rust_references(self.text)
        self.assertGreater(len(refs), 20)
        for file_name, name in refs:
            source = (CRATE_SRC / file_name).read_text(encoding="utf-8")
            self.assertRegex(source, rf"\b(?:fn|struct)\s+{re.escape(name)}\b", f"{file_name}::{name}")

    def test_every_check_of_the_three_reports_is_listed(self):
        cited = set(cited_identifiers(self.text))
        for path, count in ((RUST_REPORT, 19), (WOLFRAM_REPORT, 29), (PYTHON_REPORT, 49)):
            names = [name for name, _ in checks_of(path)]
            self.assertEqual(len(names), count, path.name)
            for name in names:
                self.assertIn(name, cited, f"{name} of {path.name}")

    def test_report_count_table_and_quoted_counts(self):
        for relative in COUNTED_REPORTS:
            total, passed, failed = count_report(ROOT / relative)
            row = f"| `{relative}` | {total} | {passed} | {failed} |"
            self.assertIn(row, self.text, row)
            self.assertEqual((passed, failed), (total, 0), relative)
        for path in (RUST_REPORT, WOLFRAM_REPORT, PYTHON_REPORT):
            data = load_json(path)
            self.assertEqual(data["failedCheckCount"], 0)
            self.assertEqual(data["verdict"], "SUCCESS")
            self.assertIn(f'`"checkCount": {data["checkCount"]}`', self.text, path.name)
            self.assertEqual(data["checkCount"], len(data["checks"]))
        self.assertEqual(load_json(WOLFRAM_REPORT)["expectedCheckCount"], 29)
        self.assertIn('`"expectedCheckCount": 29`', self.text)
        self.assertIn("19 of 19", self.text)
        self.assertIn("29 of 29", self.text)
        self.assertIn("49 of 49", self.text)


class QuotedData(unittest.TestCase):
    def setUp(self):
        self.text = markdown_text()
        self.flat = normalise_math(self.text)
        self.tensors = load_json(TENSORS)
        self.curvature = load_json(CURVATURE)

    def test_gkd_selftest_table(self):
        data = load_json(SELFTEST)
        self.assertEqual(data["verdict"], "SUCCESS")
        self.assertEqual([row["p"] for row in data["results"]], list(range(1, 10)))
        for row in data["results"]:
            self.assertEqual(row["mismatches"], 0)
            nonzero = f" {row['nonzero']} " if row["mode"] == "random" else " "
            line = f"| {row['p']} | {row['mode']} | {row['pairs']} |{nonzero}| 0 |"
            self.assertIn(line, self.text, line)
        self.assertEqual(data["results"][3]["pairs"], 16777216)
        self.assertIn("16,777,216", self.text)
        self.assertIn("200,000", self.text)
        self.assertEqual(data["definition"],
                         "kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]")
        self.assertEqual(load_json(RUST_REPORT)["gkdSelfCheck"], {"length3Pair": 1, "transposition": -1})

    def test_rust_counters_and_brute_force(self):
        report = load_json(RUST_REPORT)
        for row in report["counters"]:
            line = (f"| {row['k']} | {row['leaves']} | {row['gkdCalls']} | {row['gkdNonzero']} | "
                    f"{row['scalarGkdCalls']} | {row['nonzeroComponents']} |")
            self.assertIn(line, self.text, line)
        for name, lists, deviation in (("k1_brute_force_numeric", "262144", "1.40e-15"),
                                       ("k2_brute_force_numeric", "1073741824", "4.41e-14")):
            detail = detail_of(RUST_REPORT, name)
            for number in (lists, deviation, "H = 0.23, a4 = 0.17, a4' = 0.61, a4'' = -0.37, x8 = 0.41"):
                self.assertIn(number, detail, name)
            self.assertIn(f"{lists} index lists", self.text)
            self.assertIn(deviation, self.text)
        self.assertIn("$H = 0.23$, $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$, $x_8 = 0.41$", self.text)
        self.assertIn("all 4096 index lists", detail_of(RUST_REPORT, "riemann_first_bianchi"))
        self.assertIn("for all 4096 index lists", self.text)

    def test_sympy_counters_and_numbers(self):
        report = load_json(PYTHON_REPORT)
        counters = report["counters"]
        for row in counters["lovelockSums"]:
            line = (f"| {row['k']} | {row['products']} | {row['kdeltaCalls']} | {row['kdeltaNonzero']} | "
                    f"{row['distinctMultisets']} |")
            self.assertIn(line, self.text, line)
        self.assertIn(f"with {counters['kdeltaCallsTotal']} determinant calls in all and "
                      f"{counters['distinctOuterMatricesDeterminedBySympy']} distinct 0/1 matrices", self.text)
        self.assertEqual(len(report["randomPoints"]), 5)
        pairs = (
            ("k1_unpruned_literal_sum_agrees", "10140 kdelta calls", "(10140 calls)"),
            ("k2_unpruned_literal_sum_agrees", "1581840 kdelta calls", "(1581840 calls)"),
            ("k3_pruned_terms_vanish_literally", "20000 random", "20000 random terms"),
            ("k3_pruned_terms_vanish_literally", "19900 have a repeated index", "19900 of them"),
            ("k4_terms_vanish_literally", "300 random", "300 random 9-index lists"),
            ("gkd_literal_equals_cofactor_expansion", "266304 pairs", "266304 pairs"),
            ("gkd_literal_equals_cofactor_expansion", "7500 random pairs of length 4..8", "7500 random pairs of lengths 4 to 8"),
            ("normalisation_L3_cubic_derived", "c = [16, 64, 192, 24, 192, 128, -96, 8] = 8 x [2, 8, 24, 3, 24, 16, -12, 1]",
             "c = [16, 64, 192, 24, 192, 128, -96, 8] = 8 x [2, 8, 24, 3, 24, 16, -12, 1]"),
            ("normalisation_L3_cubic_derived", "rank 8", "rank 8"),
            ("normalisation_P1_derived_minus_4", "[-4]", "the single value $-4$ in $d = 4$"),
            ("normalisation_P2_derived_minus_8", "[-8]", "the single value $-8$ in $d = 5$"),
            ("L3_equals_8_cubic_lovelock_density", "8 (2 T1 + 8 T2 + 24 T3 + 3 T4 + 24 T5 + 16 T6 - 12 T7 + T8)",
             "8(2T_1 + 8T_2 + 24T_3 + 3T_4 + 24T_5 + 16T_6 - 12T_7 + T_8)"),
            ("rust_k3_mixed_components_agree", "60 digits", "60 digits at 5 random rational points"),
        )
        for name, in_report, in_document in pairs:
            self.assertIn(in_report, detail_of(PYTHON_REPORT, name), name)
            self.assertIn(in_document, self.text, in_document)

    def test_wolfram_numbers(self):
        report = load_json(WOLFRAM_REPORT)
        self.assertIn("Wolfram Language 15.0.1", report["producer"])
        self.assertIn("Wolfram Language 15.0.1", self.text)
        comparison = report["measurements"]["gkdComparison"]
        self.assertEqual(sum(row["pairs"] for row in comparison), 346304)
        self.assertTrue(all(row["mismatches"] == 0 for row in comparison))
        self.assertEqual([row["pairs"] for row in comparison], [64, 4096, 262144, 20000, 20000, 20000, 20000])
        flips = ", ".join(str(row["mismatchesAgainstMinusGKD"]) for row in comparison)
        self.assertIn(f"({flips} pairs for lengths 1 to 7)", self.text)
        self.assertEqual(report["gkdValuesSource"]["valuesFileBytes"], 3161984)
        self.assertIn("values file of 3161984 bytes", self.text)
        self.assertIn("346304 pairs", self.text)
        use = " ".join(report["verbatimKDeltaUse"])
        for number in ("9984", "1557504", "1128960"):
            self.assertIn(number, use)
        self.assertIn("(9984 and 1557504 calls)", self.text)
        self.assertIn("(1128960 calls)", self.text)
        rust = {row["k"]: row["gkdNonzero"] for row in load_json(RUST_REPORT)["counters"]}
        for k in (1, 2, 3):
            self.assertIn(f"number of nonzero kδ terms here: {rust[k]}",
                          detail_of(WOLFRAM_REPORT, f"k{k}_nonzero_kdelta_terms_equal_rust_counter"))
        self.assertIn(f"{rust[1]}, {rust[2]} and {rust[3]}, equal the Rust counters", self.text)
        self.assertIn("156 nonzero entries", detail_of(WOLFRAM_REPORT, "riemann_mixed_equals_rust_curvature"))

    def test_curvature(self):
        christoffels = self.curvature["christoffelNonzero_b_le_c"]
        self.assertEqual(len(christoffels), 25)
        self.assertIn("lists 25 nonzero Christoffel symbols", self.text)
        riemann = self.curvature["riemannMixedNonzero"]
        self.assertEqual(len(riemann), 156)
        self.assertIn("has 156 nonzero entries", self.text)
        space, extra = {"x1", "x2", "x3"}, {"x5", "x6", "x7"}
        expected = {
            "same": A1**2 - H**2, "mixed": -A1**2 - H**2, "i4": A2 + A1**2, "4t": -A2 + A1**2, "8": -H**2,
        }
        for entry in riemann:
            (a, b), (c, d) = entry["up"], entry["down"]
            if (a, b) != (c, d):
                continue
            value = from_mathematica(entry["value"]) if "Cot" not in entry["value"] else None
            pair = {a, b}
            if pair <= space or pair <= extra:
                self.assertEqual(sp.expand(value - expected["same"]), 0, entry)
            elif len(pair & space) == 1 and len(pair & extra) == 1:
                self.assertEqual(sp.expand(value - expected["mixed"]), 0, entry)
            elif "x4" in pair and pair & space:
                self.assertEqual(sp.expand(value - expected["i4"]), 0, entry)
            elif "x4" in pair and pair & extra:
                self.assertEqual(sp.expand(value - expected["4t"]), 0, entry)
            elif "x8" in pair:
                self.assertEqual(sp.expand(value - expected["8"]), 0, entry)
        self.assertFalse(any(set(e["up"]) == {"x4", "x8"} for e in riemann))
        for line in ("| $R^{x_ix_t}{}_{x_ix_t}$ | $-(a_4')^2 - H^2$ |", "| $R^{x_ix_4}{}_{x_ix_4}$ | $a_4'' + (a_4')^2$ |",
                     "| $R^{x_4x_t}{}_{x_4x_t}$ | $-a_4'' + (a_4')^2$ |",
                     "| $R^{x_ix_8}{}_{x_ix_8}$ and $R^{x_tx_8}{}_{x_tx_8}$ | $-H^2$ |"):
            self.assertIn(line, self.text, line)
        cot = [e for e in riemann if "Cot" in e["value"]]
        self.assertEqual(len(cot), 156 - sum(1 for e in riemann if "Cot" not in e["value"]))
        values = {e["value"] for e in cot}
        self.assertEqual(values, {"H*Derivative[1][a4][x4]*Cot[6*H*x8]", "-H*Derivative[1][a4][x4]*Cot[6*H*x8]",
                                  "H*Derivative[1][a4][x4]*Cot[6*H*x8]^(-1)", "-H*Derivative[1][a4][x4]*Cot[6*H*x8]^(-1)"})
        self.assertEqual(from_mathematica(self.curvature["ricciScalar"]), 6*A1**2 - 42*H**2)
        self.assertIn("$R = 6(a_4')^2 - 42H^2$", self.text)
        ricci = {"x1,x1": A2 - 6*H**2, "x4,x4": 6*A1**2, "x5,x5": -A2 - 6*H**2, "x8,x8": -6*H**2}
        einstein = {"x1,x1": A2 - 3*A1**2 + 15*H**2, "x4,x4": 3*A1**2 + 21*H**2,
                    "x5,x5": -A2 - 3*A1**2 + 15*H**2, "x8,x8": -3*A1**2 + 15*H**2}
        for key in COMPONENTS:
            self.assertEqual(sp.expand(from_mathematica(self.curvature["ricciMixed"][key]["mathematica"]) - ricci[key]), 0)
            self.assertEqual(sp.expand(from_mathematica(self.curvature["einsteinMixed"][key]["mathematica"]) - einstein[key]), 0)
        for text in ("$R^{x_i}{}_{x_i} = a_4'' - 6H^2$", "$R^{x_4}{}_{x_4} = 6(a_4')^2$", "$R^{x_t}{}_{x_t} = -a_4'' - 6H^2$",
                     "$R^{x_8}{}_{x_8} = -6H^2$"):
            self.assertIn(text, self.text, text)
        for text in ("G^{x_i}{}_{x_i} = a_4'' - 3(a_4')^2 + 15H^2", "G^{x_4}{}_{x_4} = 3(a_4')^2 + 21H^2",
                     "G^{x_t}{}_{x_t} = -a_4'' - 3(a_4')^2 + 15H^2", "G^{x_8}{}_{x_8} = -3(a_4')^2 + 15H^2"):
            self.assertIn(text, self.text, text)
        self.assertEqual(self.curvature["sqrtAbsDetG"], "Sin[6*H*x8]*Cot[6*H*x8]")
        self.assertEqual(self.curvature["metricDiagonal"][3], "-1")

    def test_every_listed_lovelock_component(self):
        for k in (1, 2, 3):
            tensor = self.tensors[f"P{k}_mixed_up_h_down_j"]
            for key, entry in tensor.items():
                h, j = key.split(",")
                if h != j:
                    self.assertEqual(entry["mathematica"], "0", key)
            for a, b in (("x2,x2", "x1,x1"), ("x3,x3", "x1,x1"), ("x6,x6", "x5,x5"), ("x7,x7", "x5,x5")):
                self.assertEqual(tensor[a]["mathematica"], tensor[b]["mathematica"])
            for key in COMPONENTS:
                latex = tensor[key]["latex"]
                index = key.split(",")[0][1]
                head = f"P_{{({k})}}{{}}^{{x_{index}}}{{}}_{{x_{index}}}&="
                self.assertIn(normalise_math(head + latex), self.flat, f"P_({k}) {key}")
        self.assertIn("all 56 off-diagonal components of each tensor vanish", self.text)

    def test_lovelock_scalars(self):
        expected = {
            "L1": (12*A1**2 - 84*H**2, r"L_{(1)} &= 12\,(a_4')^{2} - 84\,H^{2}"),
            "L2": (-96*A1**4 - 2112*H**2*A1**2 + 3360*H**4,
                   r"L_{(2)} &= -96\,(a_4')^{4} - 2112\,H^{2}\,(a_4')^{2} + 3360\,H^{4}"),
            "L3": (1152*A1**6 + 31104*H**2*A1**4 + 100224*H**4*A1**2 - 40320*H**6,
                   r"L_{(3)} &= 1152\,(a_4')^{6} + 31104\,H^{2}\,(a_4')^{4} + 100224\,H^{4}\,(a_4')^{2} - 40320\,H^{6}"),
        }
        for key, (value, latex) in expected.items():
            self.assertEqual(sp.expand(from_mathematica(self.tensors[key]) - value), 0, key)
            self.assertIn(latex, self.text, key)
        for k in (1, 2, 3):
            tensor = self.tensors[f"P{k}_mixed_up_h_down_j"]
            trace = sum(from_mathematica(tensor[f"x{i},x{i}"]["mathematica"]) for i in range(1, 9))
            self.assertEqual(sp.expand(trace - (8 - 2*k)*from_mathematica(self.tensors[f"L{k}"])), 0, k)
        self.assertEqual(self.tensors["k4"], "identically zero (GKD of 9 indices in 8 dimensions)")
        self.assertIn("“identically zero (GKD of 9 indices in 8 dimensions)”", self.text)

    def test_identity_and_einstein_relation(self):
        for k in (1, 2, 3):
            p = {key: from_mathematica(self.tensors[f"P{k}_mixed_up_h_down_j"][key]["mathematica"]) for key in COMPONENTS}
            self.assertEqual(sp.expand(p["x1,x1"] + p["x5,x5"] - 2*p["x8,x8"]), 0, k)
            self.assertFalse(p["x4,x4"].has(A2) or p["x8,x8"].has(A2), k)
            self.assertEqual(sp.expand(p["x1,x1"].coeff(A2) + p["x5,x5"].coeff(A2)), 0, k)
        for key in COMPONENTS:
            p1 = from_mathematica(self.tensors["P1_mixed_up_h_down_j"][key]["mathematica"])
            g = from_mathematica(self.curvature["einsteinMixed"][key]["mathematica"])
            self.assertEqual(sp.expand(p1 + 4*g), 0, key)
        self.assertIn("$P_{(k)}^{x_1}{}_{x_1} + P_{(k)}^{x_5}{}_{x_5} = 2P_{(k)}^{x_8}{}_{x_8}$", self.text)
        a1x4 = self.tensors["A1_contravariant_l_h"]["x4,x4"]["latex"]
        self.assertIn(f"$A_{{(1)}}{{}}^{{x_4x_4}} = {a1x4}$", self.text)

    def test_field_equations_use(self):
        """E_(k) of a4-equations.json = -P_(k)/2^(k+1) of this record; the factor F(a4')."""
        lovelock = load_json(A4_EQUATIONS)["lovelockTensors"]
        f_value = 0
        for k in (1, 2, 3):
            tensor = self.tensors[f"P{k}_mixed_up_h_down_j"]
            for key in COMPONENTS:
                e_k = from_ad(lovelock[f"E{k}"][key.replace(",", "")]["input"])
                p_k = from_mathematica(tensor[key]["mathematica"])
                self.assertEqual(sp.expand(e_k + p_k / 2**(k + 1)), 0, f"E{k} {key}")
            difference = -(from_mathematica(tensor["x1,x1"]["mathematica"])
                           - from_mathematica(tensor["x5,x5"]["mathematica"])) / 2**(k + 1)
            f_value += ALPHA[k - 1] * sp.cancel(difference / A2)
        a1, a2, a3 = ALPHA
        document_f = (2*a1 - 48*a2*A1**2 - 80*a2*H**2 + 720*a3*A1**4 + 864*a3*A1**2*H**2 + 720*a3*H**4)
        self.assertEqual(sp.expand(f_value - document_f), 0)
        self.assertIn(r"F(a_4') = 2\alpha_1 - 48\alpha_2(a_4')^2 - 80\alpha_2H^2 + 720\alpha_3(a_4')^4 "
                      r"+ 864\alpha_3(a_4')^2H^2 + 720\alpha_3H^4", self.text)
        detail = detail_of(A4_WOLFRAM, "evolution_factorises_a4pp_times_F")
        reported = from_ad(detail.split("F = ", 1)[1])
        self.assertEqual(sp.expand(reported - document_f), 0)
        for name in ("P1_direct_equals_gkd_branch_monomials", "P2_direct_equals_gkd_branch_monomials",
                     "P3_direct_equals_gkd_branch_monomials"):
            self.assertIn("Revision/gkd_lovelock/results/lovelock-tensors.json", detail_of(A4_WOLFRAM, name))
        self.assertIn("x4-x8", detail_of(A4_PYTHON, "other_components_vanish"))

    def test_notebook_reading(self):
        provenance = PROVENANCE.read_text(encoding="utf-8")
        sha = "23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb"
        self.assertIn(sha, provenance)
        self.assertIn(sha, self.text)
        self.assertIn("The comparison with the author's own answers is done afterwards", provenance)
        digest = NB_DIGEST.read_text(encoding="utf-8")
        for label in ("In[29]:=", "In[87]:=", "In[101]:=", "In[102]:=", "In[105]:=", "In[108]:="):
            self.assertIn(label, digest)
        for name in ("kδ33", "kδ55", "kδ77"):
            self.assertIn(name, digest)
            self.assertIn(f"`{name}`", self.text)
        self.assertIn("DefMetric[{4, 4, 0}", digest)
        nb_provenance = NB_PROVENANCE.read_text(encoding="utf-8")
        self.assertIn("input cells written: 58", nb_provenance)
        self.assertIn("(1372 x 435 pixels)", nb_provenance)
        self.assertIn("58 INPUT cells", self.text)
        self.assertIn("(1372 x 435 pixels)", self.text)
        self.assertIn("`definition_is_the_authors_verbatim`", self.text)

    def test_run_times_from_the_provenance_files(self):
        wolfram = WOLFRAM_PROVENANCE.read_text(encoding="utf-8")
        for in_provenance, in_document in (
            ("| `time_total` | 68.4 |", "`time_total` 68.4 s"),
            ("`time_total` was 68-135 s (seven runs)", "68-135 s over seven runs"),
            ("the k = 2 step took 26-43 s and the k = 3 step 35-77 s", "took 26-43 s and the $k = 3$ sum 35-77 s"),
            ("`time_total=1637.7`", "took 1637.7 s"),
            ("working set 480.7 / 485.5 / 486.2 MB", "about 486 MB working set"),
        ):
            self.assertIn(in_provenance, wolfram, in_provenance)
            self.assertIn(in_document, self.text, in_document)
        notebook = re.sub(r"\s+", " ", NB_PROVENANCE.read_text(encoding="utf-8"))
        phrase = "The whole set takes about 10 to 25 seconds, and up to about 40 seconds on a fully loaded machine"
        self.assertIn(phrase, notebook)
        self.assertIn("the whole set takes about 10 to 25 seconds, and up to about 40 seconds on a fully loaded machine",
                      self.text)
        self.assertIn("several minutes", GKD_TEST.read_text(encoding="utf-8"))
        self.assertIn("several minutes (`Revision/tests/test_gkd_lovelock.py`", self.text)


def from_compare(text: str) -> sp.Expr:
    """An expression of the comparison report (sympy text; a4_rev_d<n>(x4) = a4^(n))."""
    for n, symbol in ((1, "A1"), (2, "A2")):
        text = text.replace(f"a4_rev_d{n}(x4)", symbol)
    return sp.sympify(text, locals={"A1": A1, "A2": A2, "H": H})


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text)


class AuthorComparison(unittest.TestCase):
    """Section 8.2: every quoted number and verdict is read from Revision/gkd_lovelock/comparison/."""

    def setUp(self):
        self.text = markdown_text()
        self.report = load_json(COMPARISON_REPORT)
        self.author = load_json(AUTHOR_OUTPUTS)
        self.checks = {check["name"]: check for check in self.report["checks"]}
        self.readme = COMPARISON_README.read_text(encoding="utf-8")
        start = self.text.index("\n### 8.2 ")
        self.section = self.text[start:self.text.index("\n### 8.3 ", start)]

    def counts(self) -> dict[str, int]:
        verdicts = [check["verdict"] for check in self.report["checks"]]
        counts = {verdict: verdicts.count(verdict) for verdict in ("PASS", "FAIL", "NOT-AVAILABLE")}
        self.assertEqual(sum(counts.values()), len(verdicts))
        self.assertEqual(self.report["summary"], dict(counts, total=len(verdicts)))
        return dict(counts, total=len(verdicts))

    def test_counts_are_quoted_from_the_report(self):
        c = self.counts()
        self.assertEqual(c["FAIL"], 0)
        self.assertIsNone(self.report["stopped"])
        self.assertIn(f"{c['total']} checks: {c['PASS']} PASS, {c['FAIL']} FAIL, {c['NOT-AVAILABLE']} NOT-AVAILABLE",
                      self.text.split("\n## 1. ")[0])
        self.assertIn(f"`author-comparison-report.json` has {c['total']} checks: {c['PASS']} PASS, {c['FAIL']} FAIL, "
                      f"{c['NOT-AVAILABLE']} NOT-AVAILABLE", squash(self.section))
        row = (f"| `Revision/gkd_lovelock/comparison/author-comparison-report.json` | {c['total']} | {c['PASS']} | "
               f"{c['FAIL']} | {c['NOT-AVAILABLE']} |")
        self.assertIn(row, self.text)
        self.assertIn(f"of the {c['total']} checks {c['PASS']} pass, none fails and {c['NOT-AVAILABLE']} are "
                      "NOT-AVAILABLE", self.text)
        self.assertIn(f"`checks: {c['total']}; PASS {c['PASS']}, FAIL {c['FAIL']}, NOT-AVAILABLE {c['NOT-AVAILABLE']}`",
                      self.text)
        einstein = [name for name in self.checks if name.startswith("einstein-mixed-")]
        self.assertEqual(len(einstein), 64)
        self.assertIn(f"all {len(einstein)} components of the author's Einstein tensor", self.text)
        self.assertIn(f"all {len(einstein)} components of the Einstein tensor `Out[536]`", self.text)
        self.assertIn('"checks: %d; PASS %d, FAIL %d, NOT-AVAILABLE %d"', COMPARE_PROGRAM.read_text(encoding="utf-8"))

    def test_result_table_lists_every_check_with_its_verdict(self):
        header = "| check | what is compared | verdict |"
        self.assertIn(header, self.section)
        rows = []
        for line in self.section[self.section.index(header):].split("\n")[2:]:
            if not line.startswith("| `"):
                break
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            rows.append((re.fullmatch(r"`([^`]+)`", cells[0]).group(1), cells[1], cells[-1]))
        listed = set()
        for name, what, verdict in rows:
            if name == "einstein-mixed-<h>,<j>":
                group = [check for key, check in self.checks.items() if key.startswith("einstein-mixed-")]
                self.assertTrue(all(check["verdict"] == verdict for check in group))
                self.assertIn(f"({len(group)} checks)", what)
                listed.update(check["name"] for check in group)
            else:
                self.assertIn(name, self.checks, name)
                self.assertEqual(self.checks[name]["verdict"], verdict, name)
                listed.add(name)
        self.assertEqual(listed, set(self.checks))
        self.assertEqual(len(rows), len(self.checks) - 64 + 1)

    def test_mapping_and_normalisations(self):
        mapping = self.report["mapping"]
        self.assertIn("author array position 1 (x0, hidden) -> Revision x8", mapping["coordinates"])
        self.assertIn("The author's `x0` becomes $x_8$ of this record and the author's `xk` becomes $x_k$ for "
                      "$k = 1, \\dots, 7$", self.section)
        self.assertIn("a4_Revision(x4) := a4_author(H*x4)", mapping["function"])
        self.assertIn("a4_author^(n)(H*x4) = H^(-n) a4_Revision^(n)(x4) (chain rule; n = 0, 1, 2)", mapping["function"])
        self.assertIn("$a_4(x_4) := a_4^{\\mathrm{author}}(Hx_4)$", self.section)
        self.assertIn("$(a_4^{\\mathrm{author}})^{(n)}(Hx_4) = H^{-n}a_4^{(n)}(x_4)$ for $n = 0, 1, 2$", self.section)
        self.assertIn("only the argument H*x4 occurs in the author's outputs (checked)", mapping["function"])
        self.assertIn("the program checks that no other argument of `a4` occurs in the author's outputs", self.section)
        self.assertEqual(mapping["constant"], "H is the same constant on both sides")
        self.assertIn("$H$ is the same constant on both sides", self.section)
        self.assertIn("nothing is fitted", mapping["status"])
        notes = " ".join(self.report["normalisations"])
        for phrase in ("no factor", "with the author's own (mapped) inverse metric", "P_(1)^h_j = -4 G^h_j",
                       "= 2 R"):
            self.assertIn(phrase, notes)
        self.assertIn("The Ricci scalar is compared with no factor.", self.section)
        self.assertIn("with the author's own (mapped) inverse metric", self.section)
        self.assertIn("$P_{(1)} = -4G$ and $L_{(1)} = 2R$", self.section)
        conventions = self.report["authorConventions"]
        self.assertIn("G = Ric - (1/2) g RS (indices down)", conventions["rt"])
        self.assertIn("R^mu_{nu alpha beta} = d_alpha Gamma^mu_{nu beta} - d_beta Gamma^mu_{nu alpha} + "
                      "Gamma^mu_{s alpha} Gamma^s_{nu beta} - Gamma^mu_{s beta} Gamma^s_{nu alpha}", conventions["rt"])
        for label in conventions["storedOutputsUsed"]:
            self.assertIn(f"`{label}`", self.section)

    def test_examples_and_controls(self):
        scalar = self.checks["ricci-scalar-author-Out535-vs-curvature-json"]["detail"]
        self.assertTrue(scalar["author"].startswith("HoldForm[") and scalar["author"].endswith("]"))
        self.assertIn(f"`{scalar['author'][len('HoldForm['):-1]}`", self.section)
        self.assertEqual(sp.expand(from_compare(scalar["authorMapped"]) - (6*A1**2 - 42*H**2)), 0)
        self.assertIn("which the mapping turns into $6(a_4')^2 - 42H^2$, the value $R$ of section 6.1", self.section)
        g44 = self.checks["einstein-mixed-x4,x4"]
        self.assertEqual(g44["verdict"], "PASS")
        self.assertEqual(sp.simplify(from_compare(g44["detail"]["authorLowerMapped"]) - (-3*H**2*(7 + A1**2/H**2))), 0)
        self.assertEqual(sp.expand(from_compare(g44["detail"]["authorMixed"]) - (3*A1**2 + 21*H**2)), 0)
        self.assertEqual(sp.expand(from_compare(g44["detail"]["authorMixed"])
                                   + from_compare(g44["detail"]["authorLowerMapped"])), 0)  # g^{x4 x4} = -1
        self.assertIn("$G_{x_4x_4}$ becomes $-3H^2\\big(7 + (a_4')^2/H^2\\big)$, and raised with $g^{x_4x_4} = -1$ it is "
                      "$3(a_4')^2 + 21H^2 = G^{x_4}{}_{x_4}$", squash(self.section))
        chain = self.checks["control-mapping-without-chain-rule-is-detected"]
        self.assertEqual(chain["verdict"], "PASS")
        self.assertIs(chain["detail"]["differenceIsZero"], False)
        self.assertTrue(chain["detail"]["result"].startswith("nonzero: "))
        difference = from_compare(chain["detail"]["result"][len("nonzero: "):])
        self.assertEqual(sp.expand(difference - 6*(H**2 - 1)*A1**2), 0)
        self.assertIn("the difference of the Ricci scalars is $6(H^2 - 1)(a_4')^2$", self.section)
        raising = self.checks["control-einstein-without-index-raising-is-detected"]
        self.assertEqual(raising["verdict"], "PASS")
        self.assertIs(raising["detail"]["differenceIsZero"], False)
        self.assertTrue(raising["detail"]["result"].startswith("nonzero: "))
        self.assertIn("G_{x1 x1}", raising["detail"]["variant"])
        self.assertIn("the difference of the $x_1x_1$ components is nonzero", self.section)

    def test_notebook_cells_and_inference(self):
        sha = self.author["notebookSha256"]
        inputs = {entry["path"]: entry["sha256"] for entry in self.report["inputs"]}
        self.assertEqual(inputs[AUTHOR_NOTEBOOK.name], sha)
        self.assertEqual(self.author["notebook"], AUTHOR_NOTEBOOK.name)
        self.assertIn(f"`{AUTHOR_NOTEBOOK.name}` in the repository root (sha256 `{sha}`)", self.section)
        scan = {entry["file"]: entry for entry in self.author["keywordScan"]}
        main = scan[AUTHOR_NOTEBOOK.name]
        self.assertEqual(main["sha256"], sha)
        self.assertIn(f"Of its {main['cells']} cells ({main['styleCounts']['Input']} Input, "
                      f"{main['styleCounts']['Output']} Output)", self.section)
        labels = {entry["label"] for entry in self.author["inputCells"] + self.author["outputCells"]}
        for label in ("In[79]:=", "In[82]:=", "In[214]:=", "In[238]:=",
                      "Out[235]=", "Out[245]=", "Out[535]=", "Out[536]="):
            self.assertIn(label, labels)
            self.assertIn(f"`{label.rstrip(':=')}`", self.section)
        outputs = {entry["label"]: entry for entry in self.author["outputCells"]}
        self.assertTrue(all(entry["parsed"] is True for entry in outputs.values()))
        self.assertEqual(outputs["Out[536]="]["dimensions"], [8, 8])
        self.assertEqual(outputs["Out[235]="]["dimensions"], [8, 8])
        assigning = [entry["label"] for entry in self.author["inputCellsMentioningRSorEinsteinG"]
                     if "EinsteinG" in entry["assigns"]]
        self.assertEqual(assigning, ["In[238]:="])
        self.assertIn("only `In[238]` assigns the global symbols `RS` and `EinsteinG`", squash(self.readme))
        self.assertIn("only `In[238]` assigns the global symbols `RS` and `EinsteinG`", self.section)
        for name in ("christoffel-components", "riemann-components", "ricci-tensor-components"):
            self.assertEqual(self.checks[name]["verdict"], "NOT-AVAILABLE")
            self.assertIs(self.checks[name]["detail"]["In238EndsWithSemicolon"], True)
        self.assertIn("but `In[238]` ends with a semicolon, so no value of them is stored there", self.section)

    def test_keyword_scan(self):
        for k in (2, 3):
            check = self.checks[f"lovelock-k{k}-P{k}-and-L{k}"]
            self.assertEqual(check["verdict"], "NOT-AVAILABLE")
        evidence = self.checks["lovelock-k2-P2-and-L2"]["detail"]["keywordScan"]
        main = evidence[AUTHOR_NOTEBOOK.name]
        gkd = evidence["Generalized _Kronecker_Delta_4+4.nb"]
        self.assertEqual(main["outputCellsContainingLovelock"], main["outputCellsContainingLovelockThatAreOnlyStrings"])
        self.assertIn(f"In the main notebook {main['cellsContainingLovelock']} cells contain the word; the "
                      f"{main['outputCellsContainingLovelock']} Output cells among them hold only strings", self.section)
        self.assertEqual(gkd["outputCellsContainingLovelock"], 0)
        self.assertIn(f"In the Kronecker-delta notebook {gkd['cellsContainingLovelock']} cells contain the word, none of "
                      "them an Output cell", self.section)
        scan = {entry["file"]: entry for entry in self.author["keywordScan"]}
        self.assertEqual(scan[AUTHOR_NOTEBOOK.name]["cellsWithTokenP2P3P4kdelta"], [])
        self.assertIn("none of its cells contains one of the tokens", self.section)
        token_styles = {cell["style"] for cell in scan["Generalized _Kronecker_Delta_4+4.nb"]["cellsWithTokenP2P3P4kdelta"]}
        self.assertEqual(token_styles, {"Input", "Text"})
        self.assertIn("the cells with the token `kδ` are Input and Text cells", self.section)
        self.assertIn('{"P2", "P3", "P4", "LovelockP", "kd", "k\\[Delta]"}', EXTRACTOR.read_text(encoding="utf-8"))
        self.assertIn("`P2`, `P3`, `P4`, `LovelockP`, `kd` and `kδ`", self.section)

    def test_record_files_gate_and_run_times(self):
        sha = sha256_file(COMPARISON_REPORT)
        self.assertIn(f"| `author-comparison-report.json` | `{sha}` |", self.readme)
        self.assertIn(f"the report has the sha256 `{sha}`", self.section)
        for path in (COMPARISON_README, EXTRACTOR, AUTHOR_OUTPUTS, COMPARE_PROGRAM, COMPARISON_REPORT):
            self.assertIn(f"`{path.name}`", self.section, path.name)
        self.assertIn("It does not change any file of `results/`, `code/`, `verification/` or `notebook_reading/`.",
                      self.readme)
        provenance = squash(PROVENANCE.read_text(encoding="utf-8"))
        self.assertIn("The comparison with the author's own answers is done afterwards, in a separate, later commit",
                      provenance)
        self.assertIn("announces that the comparison with the author's own answers is done afterwards, in a separate, "
                      "later commit", self.section)
        for gate in GATES:
            source = gate.read_text(encoding="utf-8")
            self.assertIn("\ngkd-author-extract|", source, gate.name)
            self.assertIn("\ngkd-author-compare|", source, gate.name)
            self.assertIn("Revision/gkd_lovelock/comparison/compare_with_author.py", source, gate.name)
        self.assertIn("as the steps `gkd-author-extract` and `gkd-author-compare`", self.text)
        readme = squash(self.readme)
        self.assertIn("Run time 4.4 to 6.0 s (seven runs,", readme)
        self.assertIn("Run time 0.7 to 0.9 s.", readme)
        self.assertIn("the extractor 4.4 to 6.0 s (seven runs), the comparison 0.7 to 0.9 s", self.text)
        extractor = EXTRACTOR.read_text(encoding="utf-8")
        for printed in ("cells: ", "inputs parsed: ", "outputs parsed: "):
            self.assertIn(printed, extractor)
        self.assertEqual(len(self.author["inputCells"]), 8)
        self.assertEqual(len(self.author["outputCells"]), 4)
        main = {entry["file"]: entry for entry in self.author["keywordScan"]}[AUTHOR_NOTEBOOK.name]
        self.assertIn(f"`cells: {main['cells']}`, `inputs parsed: 8/8` and `outputs parsed: 4/4`", self.text)

    @unittest.skipUnless(AUTHOR_NOTEBOOK.exists(), "the author's notebook is not in the repository root")
    def test_comparison_reproduces_the_committed_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "author-comparison-report.json"
            completed = subprocess.run([sys.executable, str(COMPARE_PROGRAM), "--output", str(output)], cwd=ROOT,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=600)
            text = completed.stdout.decode("utf-8", "replace")
            self.assertEqual(completed.returncode, 0, text[-3000:])
            self.assertEqual(output.read_bytes(), COMPARISON_REPORT.read_bytes())
        c = self.counts()
        self.assertIn(f"checks: {c['total']}; PASS {c['PASS']}, FAIL {c['FAIL']}, NOT-AVAILABLE {c['NOT-AVAILABLE']}",
                      text)


if __name__ == "__main__":
    unittest.main()
