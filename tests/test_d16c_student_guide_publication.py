# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the Stage-3 student guide (setting up and solving every numerical solution).

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_student_guide_publication.py" -v

The document provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md is built with the builder's
DEVELOPER LAYOUT (ragged table columns, breakable code spans):
    python scripts/build_provenance_pdf.py --developer-layout provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md
into provenance/DIRAC16COMPLEX_STUDENT_GUIDE.{tex,pdf}; the edition
dirac16complex-student-guide is registered in provenance/pdf-specifications.json.  Without
--developer-layout the builder writes a different .tex (and the log is not warning-free).

The tests pin the sha256 of the Markdown and of the LaTeX file, require that the committed
.tex is exactly the builder's output for the committed .md, that the registered PDF edition
matches the committed PDF and that its typewriter font has no en-dash ligature and no curly
left quote (a student copies commands from it), and that every table, count, command path,
pinned commit and number the guide quotes agrees with the files it describes: the gamma,
C and B tables with the algebra fixture; the CSV column tables with the CSV headers; the
solver, self-check and checker tables with the summary.json and python-check-report.json
files under artifacts/dirac16complex/numerics/; the engine table with
scripts/setup_solver.{ps1,sh}; the notebook counts with notebook-report.json and the
Mathematica verifier; the exercise answers with the committed CSV files.

After an intended edit of the document: rebuild and register it with
    python scripts/build_provenance_pdf.py --register --developer-layout provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md
and update MARKDOWN_SHA256 and TEX_SHA256 below.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import subprocess
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
MARKDOWN = PROVENANCE / "DIRAC16COMPLEX_STUDENT_GUIDE.md"
TEX = PROVENANCE / "DIRAC16COMPLEX_STUDENT_GUIDE.tex"
PDF = PROVENANCE / "DIRAC16COMPLEX_STUDENT_GUIDE.pdf"
EDITION = "dirac16complex-student-guide"
NUMERICS = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "numerics"
FIXTURE = REPOSITORY_ROOT / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"
CRATE = REPOSITORY_ROOT / "studies" / "dirac16complex_cosmology"
EXPERIMENTS = ("exp1", "exp2", "exp3", "exp4", "exp5")

MARKDOWN_SHA256 = "3d4cda991e986338a16c0cc3fe2a2148adbf53274f5101e369eb32e5784b8ef3"
TEX_SHA256 = "38d57cf36abf1f2ae309d67047d487d5b10ccfa9146609d84fc46de986e142db"

TITLE = "A student's guide to the dirac16complex numerical solutions"
SUBTITLE = ("Installing, deriving, running and checking the five CVODE experiments of Stage 3 "
            "on Windows, macOS and Linux")
REQUIRED_SECTIONS = (
    "Abstract",
    "1. What you will compute and why",
    "2. How to use this guide",
    "3. Installing the tools",
    "4. Getting the code and the solver engine",
    "5. Building and testing the program",
    "6. The mathematics you need, from zero",
    "7. Running the experiments",
    "8. Reading the output files",
    "9. Checking the results with the Python checkers",
    "10. The Jupyter notebook",
    "11. The Mathematica notebook (optional)",
    "12. Rebuilding the PDF documents (optional)",
    "13. Changing parameters: exercises with answers",
    "14. Troubleshooting",
    "15. Glossary",
    "16. Credits, licences and verified facts",
)
REQUIRED_PHRASES = (
    "git clone https://github.com/once-ere/Dirac_claude.git",
    "rustc --version",
    "cargo build --release",
    "cargo test --release",
    "python -m pip install numpy matplotlib sympy nbformat nbclient ipykernel",
    "target-feature=+fma",
    "counted from 0",
    "vielbein postulate",
    "covariant derivative",
    "BDF",
    "Adams-Moulton",
    "Newton's method",
    "fixed-point iteration",
    "rtol",
    "atol",
    "max_step",
    "expectation-value rule",
    "Krein",
    "PYTHONUTF8",
    "cp1252",
    "not on PATH",
    "externally-managed-environment",
    "wolframscript",
    "MiKTeX",
    "TeX Live",
    "none of the three rustSolveIt repositories contains a Mathematica notebook",
    "294 Jupyter notebooks",
    "planet_Mercury/notebook",
    "BSD-3-Clause",
    "requirements-stage3.txt",
    "python -m pip install numpy==2.4.6 matplotlib==3.11.0 sympy==1.14.0",
    "python -m pip install nbformat==5.10.4 nbclient==0.10.2 ipykernel==7.1.0",
    "vendor/rustSolveIt is an incomplete checkout (an interrupted or failed download); remove it and rerun",
    "ERROR: pdflatex not found",
    "git restore provenance/DIRAC16COMPLEX_STUDENT_GUIDE.tex",
    "winget install --id Rustlang.Rustup -e -i",
)
ALLOWED_PROVENANCE_MARKDOWN = (
    "provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md",
    "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def markdown_text() -> str:
    return MARKDOWN.read_text(encoding="utf-8")


def csv_header(path: Path) -> list[str]:
    with open(path, encoding="utf-8", newline="") as handle:
        return next(csv.reader(handle))


def csv_rows(path: Path) -> list[dict]:
    with open(path, encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def data_row_count(path: Path) -> int:
    with open(path, encoding="utf-8", newline="") as handle:
        return sum(1 for _ in handle) - 1


def prose_lines(text: str):
    """(line number, line) of every line outside fenced code."""
    inside = False
    for number, line in enumerate(text.split("\n"), 1):
        if line.startswith("```"):
            inside = not inside
            continue
        if not inside:
            yield number, line


def fenced_blocks(text: str) -> list[list[str]]:
    blocks, current, inside = [], [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            if inside:
                blocks.append(current)
                current = []
            inside = not inside
            continue
        if inside:
            current.append(line)
    return blocks


def sections(text: str) -> dict[str, str]:
    """Map '8.2' (the number of a ### heading, or '8' of a ## heading) to its body."""
    result = {}
    pattern = re.compile(r"^(#{2,3}) (\d+(?:\.\d+)?)\.? ", re.M)
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(2)] = text[match.start():end]
    return result


def tables(text: str) -> list[list[list[str]]]:
    """Every Markdown table of text as a list of rows of cells (header first)."""
    found, current = [], []
    for line in text.split("\n"):
        if line.startswith("|"):
            current.append([cell.strip() for cell in line.strip().strip("|").split("|")])
        elif current:
            found.append(current)
            current = []
    if current:
        found.append(current)
    return [[row for row in table if not all(re.fullmatch(r":?-{3,}:?", c) for c in row)]
            for table in found]


def code_spans(cell: str) -> list[str]:
    return re.findall(r"`([^`]*)`", cell)


def column_names(cell: str) -> list[str]:
    """Code spans of a cell, with `u_re_0` to `u_re_15` expanded to the 16 names."""
    names = []
    for match in re.finditer(r"`(u_(?:re|im))_0` to `u_(?:re|im)_15`", cell):
        names.extend("%s_%d" % (match.group(1), n) for n in range(16))
    cell = re.sub(r"`u_(?:re|im)_0` to `u_(?:re|im)_15`", "", cell)
    names.extend(code_spans(cell))
    return names


def signed_permutation(matrix) -> list[str]:
    entries = []
    for row in matrix:
        nonzero = [(j, value) for j, value in enumerate(row) if value != 0]
        assert len(nonzero) == 1
        column, value = nonzero[0]
        assert value in (1, -1)
        entries.append(("+" if value > 0 else "-") + str(column))
    return entries


class GuideTestCase(unittest.TestCase):
    """assertIn with a short failure message for the long guide text."""

    def assertIn(self, member, container, msg=None):
        if isinstance(container, str) and len(container) > 400:
            if member not in container:
                self.fail(msg or "%r not found in the guide text" % (member,))
        else:
            super().assertIn(member, container, msg)


class PinTests(GuideTestCase):

    def test_markdown_sha256_pin(self):
        self.assertEqual(sha256_file(MARKDOWN), MARKDOWN_SHA256)

    def test_tex_sha256_pin(self):
        self.assertEqual(sha256_file(TEX), TEX_SHA256)

    def test_markdown_is_lf_only_utf8(self):
        content = MARKDOWN.read_bytes()
        self.assertNotIn(b"\r", content)
        content.decode("utf-8")

    def test_tex_is_the_builder_output_of_the_markdown_in_developer_layout(self):
        latex = builder.convert(markdown_text(), strip_heading_numbers=True, developer_layout=True,
                                image_root=REPOSITORY_ROOT)
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())

    def test_registered_edition_matches_the_committed_pdf(self):
        registry = check_provenance_pdf.load_specifications(
            check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH)
        self.assertIn(EDITION, registry)
        entry = registry[EDITION]
        self.assertEqual(entry["path"], "provenance/DIRAC16COMPLEX_STUDENT_GUIDE.pdf")
        content = PDF.read_bytes()
        self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(content)))
        self.assertTrue(content.startswith(b"%PDF-"))
        self.assertTrue(content.rstrip().endswith(b"%%EOF"))

    def test_figures_exist_and_are_notebook_figures(self):
        figures = builder.figure_paths(markdown_text())
        self.assertEqual(len(figures), 3)
        report = load_json(NUMERICS / "notebook-report.json")
        notebook_figures = {entry["file"]: entry["sha256"] for entry in report["figures"]}
        for figure in figures:
            with self.subTest(figure=figure):
                path = REPOSITORY_ROOT / figure
                self.assertTrue(path.read_bytes().startswith(builder.PNG_SIGNATURE))
                self.assertEqual(notebook_figures[figure], sha256_file(path))


class ContentTests(GuideTestCase):

    def test_title_and_subtitle(self):
        lines = markdown_text().split("\n")
        self.assertEqual(lines[0], "# " + TITLE)
        self.assertEqual(lines[2], "## " + SUBTITLE)
        self.assertEqual(sum(1 for line in lines if line.startswith("# ")), 1)

    def test_required_sections_in_order(self):
        headings = [line[3:] for line in markdown_text().split("\n") if line.startswith("## ")]
        self.assertEqual(headings[0], SUBTITLE)
        self.assertEqual(headings[1:], list(REQUIRED_SECTIONS))

    def test_subsection_numbers_are_consecutive(self):
        current, expected = None, 1
        for line in markdown_text().split("\n"):
            major = re.match(r"^## (\d+)\. ", line)
            minor = re.match(r"^### (\d+)\.(\d+) ", line)
            if major:
                current, expected = int(major.group(1)), 1
            elif minor:
                self.assertEqual((int(minor.group(1)), int(minor.group(2))), (current, expected), line)
                expected += 1

    def test_required_phrases(self):
        text = markdown_text()
        for phrase in REQUIRED_PHRASES:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_no_placeholders_or_todo_and_no_other_provenance_documents(self):
        text = markdown_text()
        self.assertIsNone(re.search(r"@@[A-Z0-9_]+@@", text))
        self.assertNotIn("TODO", text)
        self.assertNotIn("FIXME", text)
        rest = text
        for allowed in ALLOWED_PROVENANCE_MARKDOWN:
            rest = rest.replace(allowed, "")
        self.assertIsNone(re.search(r"provenance/[A-Za-z0-9_]+\.md", rest))

    def test_every_fenced_code_line_fits_and_has_no_tab_or_backtick(self):
        # a backtick in Verbatim is set as a curly left quote in the typewriter font
        for block in fenced_blocks(markdown_text()):
            for line in block:
                self.assertLessEqual(len(line), builder.MAX_CODE_LINE_LENGTH, line)
                self.assertNotIn("\t", line)
                self.assertNotIn("`", line)

    def test_no_double_hyphen_in_inline_code_and_no_straight_quotes_in_prose(self):
        # pdflatex joins -- into an en dash in \texttt, which would break copied commands
        for number, line in prose_lines(markdown_text()):
            for span in code_spans(line):
                self.assertNotIn("--", span, "line %d" % number)
            prose = re.sub(r"`[^`]*`|\$[^$]*\$", "", line)
            self.assertNotIn('"', prose, "line %d" % number)

    def test_thawing_freezing_signs_are_formula_consistent(self):
        text = markdown_text()
        self.assertIn("but its own formula gives $dw/da=-w_a$", text)
        self.assertIn("A thawing field, whose $w$ rises from $-1$ as the universe expands, therefore "
                      "has $w_a<0$, and a freezing field has $w_a>0$", text)
        self.assertIn("(freezing, $w_a>0$) or rises from $-1$ (thawing, $w_a<0$)", text)

    def test_every_repository_path_in_code_exists(self):
        text = markdown_text()
        pattern = re.compile(r"^(?:scripts|notebooks|studies|artifacts|provenance|wolfram|tests)/"
                             r"[A-Za-z0-9_./-]*$")
        paths = set()
        for _, line in prose_lines(text):
            paths.update(span for span in code_spans(line) if pattern.match(span))
        for block in fenced_blocks(text):
            for line in block:
                paths.update(word for word in re.split(r"[\s\"]+", line) if pattern.match(word))
        generated = ("DIRAC16COMPLEX_STUDENT_GUIDE",)
        checked = 0
        for path in sorted(paths):
            if "expN" in path or path.endswith("/") and not (REPOSITORY_ROOT / path).is_dir():
                continue
            if any(name in path for name in generated) and not (REPOSITORY_ROOT / path).exists():
                continue
            with self.subTest(path=path):
                self.assertTrue((REPOSITORY_ROOT / path).exists(), path)
                checked += 1
        self.assertGreater(checked, 30)

    def test_quoted_self_check_names_exist(self):
        text = markdown_text()
        summaries = {e: load_json(NUMERICS / e / "summary.json") for e in EXPERIMENTS}
        for name in ("exact_solution_all_runs", "rho_frozen_all_runs",
                     "pressures_and_S_frozen_eigenstate_runs", "hilbert_norm_conserved",
                     "krein_norm_conserved", "lambda_run_meff_constant"):
            self.assertIn(name, summaries["exp1"]["checks"])
            self.assertIn("`%s`" % name, text)
        self.assertIn("late_time_isotropic_dust", summaries["exp2"]["checks"])
        self.assertIn("`late_time_isotropic_dust` FAILS", text)

    def test_pinned_python_packages_match_the_requirements_file(self):
        lines = (REPOSITORY_ROOT / "requirements-stage3.txt").read_text(encoding="utf-8").splitlines()
        pins = dict(line.split("==") for line in lines if "==" in line and not line.startswith("#"))
        self.assertEqual(sorted(pins), sorted(["numpy", "matplotlib", "sympy", "nbformat", "nbclient",
                                               "ipykernel"]))
        text = markdown_text()
        for name, version in pins.items():
            with self.subTest(package=name):
                self.assertIn("%s==%s" % (name, version), text)
                self.assertIn("%s %s" % (name, version), text)

    def test_unit_test_count(self):
        count = sum(path.read_text(encoding="utf-8").count("#[test]")
                    for path in (CRATE / "src").glob("*.rs"))
        self.assertEqual(count, 25)
        self.assertIn("The crate has 25 unit tests", markdown_text())
        self.assertIn("running 25 tests", markdown_text())


class AlgebraTablesTests(GuideTestCase):

    @classmethod
    def setUpClass(cls):
        cls.fixture = load_json(FIXTURE)
        cls.section = sections(markdown_text())

    def test_gamma_tables_are_the_fixture(self):
        found = tables(self.section["6.3"])
        self.assertEqual(len(found), 2)
        expected = [signed_permutation(matrix) for matrix in self.fixture["gamma"]]
        for part, table in enumerate(found):
            columns = list(range(4 * part, 4 * part + 4))
            self.assertEqual(table[0], ["$i$"] + ["$\\gamma^%d$" % a for a in columns])
            self.assertEqual(len(table), 17)
            for i, row in enumerate(table[1:]):
                self.assertEqual(row, [str(i)] + [expected[a][i] for a in columns])

    def test_c_and_b_tables_are_the_fixture(self):
        table = tables(self.section["6.4"])[0]
        self.assertEqual(table[0], ["$i$", "$C$", "$B/i$"])
        charge = signed_permutation(self.fixture["C"])
        self.assertTrue(all(value == 0 for row in self.fixture["B"]["real"] for value in row))
        b_imag = signed_permutation(self.fixture["B"]["imag"])
        for i, row in enumerate(table[1:]):
            self.assertEqual(row, [str(i), charge[i], b_imag[i]])
        self.assertEqual(len(table), 17)

    def test_worked_examples_follow_from_the_tables(self):
        gamma4 = signed_permutation(self.fixture["gamma"][4])
        self.assertEqual(gamma4[0], "-13")
        self.assertEqual(gamma4[13], "+0")
        self.assertEqual(signed_permutation(self.fixture["B"]["imag"])[0], "+9")
        text = markdown_text()
        self.assertIn("$(\\gamma^4u)_0=-u_{13}$", text)
        self.assertIn("$(\\gamma^4v)_{13}=+v_0$", text)
        self.assertIn("$(Bu)_0=i\\,u_9$", text)

    def test_rest_eigenvector_is_the_committed_initial_spinor(self):
        text = markdown_text()
        self.assertIn("u_0=\\tfrac12\\bigl(e_0-e_4-i\\,e_9-i\\,e_{13}\\bigr)", text)
        for path, pick in ((NUMERICS / "exp2" / "run_x0_0.csv", lambda rows: [r for r in rows if float(r["t"]) == 0.0][0]),
                           (NUMERICS / "exp1" / "run_A1_K0_pos_Bp.csv", lambda rows: rows[0]),
                           (NUMERICS / "exp3" / "run_x0_0_mu3.csv", lambda rows: [r for r in rows if float(r["N"]) == 0.0][0])):
            row = pick(csv_rows(path))
            vector = [complex(float(row["u_re_%d" % n]), float(row["u_im_%d" % n])) for n in range(16)]
            expected = [0j] * 16
            expected[0], expected[4], expected[9], expected[13] = 0.5, -0.5, -0.5j, -0.5j
            with self.subTest(path=path.name):
                self.assertTrue(all(abs(a - b) < 1e-15 for a, b in zip(vector, expected)))


class EngineAndCommandTests(GuideTestCase):

    def test_engine_table_matches_both_setup_scripts(self):
        table = tables(sections(markdown_text())["4.3"])[0]
        self.assertEqual(table[0], ["Argument", "Repository", "Pinned commit"])
        rows = {code_spans(row[0])[0]: (code_spans(row[1])[0], code_spans(row[2])[0]) for row in table[1:]}
        self.assertEqual(sorted(rows), ["linux", "macos", "win11"])
        shell = (REPOSITORY_ROOT / "scripts" / "setup_solver.sh").read_text(encoding="utf-8")
        power = (REPOSITORY_ROOT / "scripts" / "setup_solver.ps1").read_text(encoding="utf-8")
        for platform, (url, commit) in rows.items():
            with self.subTest(platform=platform):
                self.assertRegex(shell, r"%s\) url=%s\.git\s+pin=%s" % (platform, re.escape(url), commit))
                self.assertRegex(power, r"%s = @\('%s\.git',\s+'%s'\)" % (platform, re.escape(url), commit))
        self.assertIn("solver_commit=%s" % rows["win11"][1], markdown_text())

    def test_engine_tree_ids_when_the_win11_engine_is_present(self):
        vendor = REPOSITORY_ROOT / "vendor" / "rustSolveIt"
        if not (vendor / ".git").exists():
            self.skipTest("vendor/rustSolveIt is not fetched")
        head = subprocess.run(["git", "-C", str(vendor), "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
        if head != "a8fdff459adfe181573d7924b18bffbdf378fdb3":
            self.skipTest("vendor/rustSolveIt holds another engine")
        tree = subprocess.run(["git", "-C", str(vendor), "rev-parse", "HEAD:sundials_rs"],
                              capture_output=True, text=True, check=True).stdout.strip()
        self.assertTrue(tree.startswith("eeaa0cad"), tree)
        self.assertIn("(tree `eeaa0cad`)", markdown_text())
        self.assertIn("`47d654d5`", markdown_text())

    def test_fma_block_is_the_cargo_config(self):
        config = (REPOSITORY_ROOT / ".cargo" / "config.toml").read_text(encoding="utf-8")
        self.assertIn('[build]\nrustflags = ["-C", "target-feature=+fma"]', config)
        self.assertIn('```\n[build]\nrustflags = ["-C", "target-feature=+fma"]\n```', markdown_text())

    def test_print_config_fixture_hash(self):
        generated = (CRATE / "src" / "generated.rs").read_text(encoding="utf-8")
        digest = sha256_file(FIXTURE)
        self.assertIn(digest, generated)
        self.assertIn("fixture sha256   = %s" % digest, markdown_text())

    def test_usage_block_is_the_program_usage(self):
        main = (CRATE / "src" / "main.rs").read_text(encoding="utf-8")
        doc = [line[4:] if line.startswith("//! ") else "" for line in main.split("\n")
               if line.startswith("//!")]
        start = doc.index("```text") + 1
        usage = doc[start:doc.index("```", start)]
        block = [b for b in fenced_blocks(markdown_text()) if b and b[0].startswith("dirac16complex_cosmology <")][0]
        self.assertEqual(block, usage)

    def test_checker_options_exist(self):
        for number in range(1, 6):
            source = (REPOSITORY_ROOT / "scripts" / ("check_dirac16complex_exp%d.py" % number)).read_text(encoding="utf-8")
            for option in ("--output", "--repeat", "--refined"):
                self.assertIn('parser.add_argument("%s"' % option, source)


class OutputTablesTests(GuideTestCase):

    @classmethod
    def setUpClass(cls):
        cls.section = sections(markdown_text())

    def assert_columns(self, table, path, extra_ok=()):
        names = [name for row in table[1:] for name in column_names(row[0])]
        self.assertEqual(len(names), len(set(names)), names)
        self.assertEqual(sorted(set(names) - set(extra_ok)), sorted(csv_header(path)))

    def test_exp1_tables(self):
        found = tables(self.section["8.2"])
        self.assert_columns(found[0], NUMERICS / "exp1" / "background_A1.csv")
        self.assert_columns(found[1], NUMERICS / "exp1" / "run_A1_K0_pos_Bp.csv")
        summary = load_json(NUMERICS / "exp1" / "summary.json")
        self.assertIn("(folder `exp1`, %d files)" % len(summary["files"]), self.section["8.2"])
        self.assertEqual(data_row_count(NUMERICS / "exp1" / "background_A1.csv"), 201)
        runs = [f for f in summary["files"] if f.startswith("run_")]
        self.assertEqual(len(runs), 26)
        self.assertIn("The 26 run files", self.section["8.2"])

    def test_exp2_table(self):
        self.assert_columns(tables(self.section["8.3"])[0], NUMERICS / "exp2" / "run_x0_0.csv")
        for name in ("run_x0_0.csv", "run_x0_m0p4.csv", "run_x0_0p5.csv"):
            self.assertEqual(data_row_count(NUMERICS / "exp2" / name), 511)
        self.assertIn("(511 rows each", self.section["8.3"])

    def test_exp3_tables(self):
        found = tables(self.section["8.4"])
        self.assert_columns(found[0], NUMERICS / "exp3" / "run_x0_0_mu3.csv")
        self.assert_columns(found[1], NUMERICS / "exp3" / "fits_scan.csv")
        runs = [f for f in load_json(NUMERICS / "exp3" / "summary.json")["files"] if f.startswith("run_")]
        self.assertEqual(len(runs), 10)
        expected = {"run_x0_%s_mu%d.csv" % (x, mu) for x in ("0", "m0p2", "m0p3", "m0p433107", "m0p462654")
                    for mu in (3, 7)}
        self.assertEqual(set(runs), expected)

    def test_exp4_tables(self):
        found = tables(self.section["8.5"])
        files, modes = found[0], found[1]
        summary = load_json(NUMERICS / "exp4" / "summary.json")
        listed = {code_spans(row[0])[0]: row for row in files[1:]}
        self.assertEqual(sorted(listed), sorted(f for f in summary["files"] if f.endswith(".csv")))
        for name, row in listed.items():
            with self.subTest(file=name):
                self.assertEqual(int(row[1]), data_row_count(NUMERICS / "exp4" / name))
                spans = code_spans(row[2])
                if spans:
                    self.assertEqual(spans, csv_header(NUMERICS / "exp4" / name))
        mode_names = [n for row in modes[1:] for n in column_names(row[0])]
        thermal = csv_header(NUMERICS / "exp4" / "thermal_modes.csv")
        pair = csv_header(NUMERICS / "exp4" / "pair_modes.csv")
        self.assertEqual(sorted(mode_names), sorted(set(thermal) | set(pair)))
        self.assertEqual(set(pair) - set(thermal), {"m"})
        self.assertEqual(set(thermal) - set(pair), {"s"})
        for name in ("thermal_spin.csv", "thermal_antiparticle.csv", "thermal_adiabatic_vacuum.csv"):
            self.assertEqual(csv_header(NUMERICS / "exp4" / name), thermal)
        self.assertEqual(csv_header(NUMERICS / "exp4" / "pair_antiparticle.csv"), pair)

    def test_exp5_table(self):
        self.assert_columns(tables(self.section["8.6"])[0], NUMERICS / "exp5" / "run_q0p05_Cp.csv")
        runs = [f for f in load_json(NUMERICS / "exp5" / "summary.json")["files"] if f.startswith("run_")]
        self.assertEqual(sorted(runs), ["run_q0p05_Cm.csv", "run_q0p05_Cp.csv", "run_q0p1_Cm.csv",
                                        "run_q0p1_Cp.csv"])
        for name in runs:
            self.assertEqual(data_row_count(NUMERICS / "exp5" / name), 601)

    def test_state_layout_tables(self):
        text = markdown_text()
        self.assertIn("| 6 to 21 | $\\mathrm{Re}\\,u_0,\\dots,\\mathrm{Re}\\,u_{15}$ |", text)
        self.assertIn("| 22 to 37 | $\\mathrm{Im}\\,u_0,\\dots,\\mathrm{Im}\\,u_{15}$ |", text)
        self.assertIn("| 34 | $\\ln\\sigma$ |", text)
        exp2 = load_json(NUMERICS / "exp2" / "summary.json")["stateLayout"]
        self.assertTrue(exp2.startswith("ln_b, ln_a, ln_c, H_b, H_a, H_c, u_re_0..u_re_15, u_im_0..u_im_15"))
        exp3 = load_json(NUMERICS / "exp3" / "summary.json")["stateLayout"]
        self.assertTrue(exp3.startswith("H0t = H0 (t - t0), D_C (c/H0), u_re_0..u_re_15, u_im_0..u_im_15, ln_sigma"))


class CountsAndSolverTests(GuideTestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.section = sections(cls.text)
        cls.summaries = {e: load_json(NUMERICS / e / "summary.json") for e in EXPERIMENTS}
        cls.reports = {e: load_json(NUMERICS / e / "python-check-report.json") for e in EXPERIMENTS}

    def test_solver_table(self):
        table = tables(self.section["6.16"])[0]
        self.assertEqual(table[0], ["Experiment", "Method", "rtol, atol", "max_step", "Steps", "RHS calls"])
        methods = {"BDF + Newton + dense": "CVODE BDF + Newton + dense direct linear solver (DQ Jacobian)",
                   "Adams + fixed point": "CVODE Adams-Moulton + fixed-point (functional) iteration"}
        for row, experiment in zip(table[1:], EXPERIMENTS):
            summary = self.summaries[experiment]
            with self.subTest(experiment=experiment):
                self.assertEqual(row[0], "EXP-" + experiment[-1])
                self.assertEqual(methods[row[1]], summary["solver"])
                rtol, atol = (float(x) for x in row[2].split(", "))
                self.assertEqual((rtol, atol, float(row[3])),
                                 (summary["tolerances"]["rtol"], summary["tolerances"]["atol"],
                                  summary["tolerances"]["maxStep"]))
                self.assertEqual((int(row[4]), int(row[5])),
                                 (summary["solverTotals"]["steps"], summary["solverTotals"]["rhsEvaluations"]))

    def test_expected_summary_lines_and_self_check_counts(self):
        table = tables(self.section["7.3"])[0]
        total = 0
        for row, experiment in zip(table[1:], EXPERIMENTS):
            summary = self.summaries[experiment]
            line = "%s: solver_steps=%d rhs_evaluations=%d files=%d verdict=SUCCESS" % (
                experiment, summary["solverTotals"]["steps"], summary["solverTotals"]["rhsEvaluations"],
                len(summary["files"]))
            with self.subTest(experiment=experiment):
                self.assertEqual(row[0], experiment)
                self.assertEqual(int(row[1]), len(summary["checks"]))
                self.assertEqual(code_spans(row[2]), [line])
                self.assertEqual(int(row[3]), len(summary["files"]))
                self.assertTrue(all(summary["checks"].values()))
                self.assertEqual(summary["verdict"], "SUCCESS")
            total += len(summary["checks"])
        self.assertEqual(total, 69)
        self.assertIn("That is 69 self-checks in total.", self.text)
        exp1 = self.summaries["exp1"]["solverTotals"]
        self.assertIn("exp1: solver_steps=%d rhs_evaluations=%d files=29 verdict=SUCCESS"
                      % (exp1["steps"], exp1["rhsEvaluations"]), "\n".join(sum(fenced_blocks(self.text), [])))

    def test_checker_table_and_quick_form_counts(self):
        table = tables(self.section["9.2"])[0]
        rows = {code_spans(row[0])[0]: row for row in table[1:]}
        fits = load_json(NUMERICS / "exp3" / "fits.json")
        self.assertEqual(int(rows["analyze_dirac16complex_exp3.py"][1]), len(fits["validation"]["checks"]))
        self.assertEqual(len(fits["validation"]["checks"]), 10)
        total = 0
        for experiment in EXPERIMENTS:
            report = self.reports[experiment]
            row = rows["check_dirac16complex_%s.py" % experiment]
            with self.subTest(experiment=experiment):
                self.assertEqual(int(row[1]), report["checkCount"])
                self.assertEqual(int(row[2]), report["failedCheckCount"])
                self.assertEqual(report["failedCheckCount"], 0)
                self.assertTrue(report["checks"]["repeatByteIdentity"])
                self.assertTrue(report["checks"]["refinedConvergence"])
            total += report["checkCount"]
        self.assertEqual(total, 162)
        self.assertIn("That is $25+34+31+51+21=162$ checker checks.", self.text)
        quick = [self.reports[e]["checkCount"] - 2 for e in EXPERIMENTS]
        self.assertEqual(quick, [23, 32, 29, 49, 19])
        self.assertIn("fitsConsistent", self.reports["exp3"]["checks"])
        section = self.section["9.3"]
        self.assertIn("`check_count=23`", section)
        self.assertIn("the checker `check_count=29`", section)
        self.assertIn("give 32, 49 and 19 checks in the quick form", section)
        self.assertIn("(28 in the quick form, 30 in the full form)", section)
        summary = load_json(NUMERICS / "numerics-summary.json")["totals"]
        self.assertEqual((summary["rustChecks"], summary["pythonChecks"], summary["analysisChecks"]),
                         (69, 162, 10))

    def test_notebook_counts(self):
        report = load_json(NUMERICS / "notebook-report.json")
        self.assertEqual((report["cells"], report["codeCells"], report["gauntlet"]["count"],
                          len(report["figures"])), (23, 8, 71, 17))
        self.assertEqual(report["gauntlet"]["failed"], 0)
        self.assertIn("is a Python 3 notebook of 23 cells, 8 of them code", self.text)
        self.assertIn("draws 17 figures", self.text)
        self.assertIn("a gauntlet of 71 assertions", self.text)
        names = [r["name"] for r in report["gauntlet"]["results"]]
        self.assertIn("fresh_program_outputs_byte_identical", names)
        self.assertIn("fresh_analysis_outputs_numerically_equal", names)
        self.assertIn("`AssertionError('fresh_program_outputs_byte_identical')`", self.text)
        self.assertIn("prose_numbers_match_reports", names)

    def test_mathematica_counts(self):
        verifier = (REPOSITORY_ROOT / "scripts" / "verify_dirac16complex_mathematica_notebook.wls").read_text(encoding="utf-8")
        self.assertIn("expectedInputCount = 37", verifier)
        self.assertIn("expectedCheckCount = 49", verifier)
        report = load_json(NUMERICS / "mathematica-report.json")
        self.assertEqual(report["checkCount"], 49)
        self.assertTrue(all(report["checks"].values()))
        self.assertEqual(len(report["figures"]), 8)
        self.assertIn("input_cell_count=37\n", "\n".join("\n".join(b) for b in fenced_blocks(self.text)))
        self.assertIn("draws 8 figures", self.text)
        self.assertIn("ends with 49 checks", self.text)
        self.assertIn("294 Jupyter notebooks", report["provenance"])


class PhysicsNumbersTests(GuideTestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = markdown_text()
        cls.summaries = {e: load_json(NUMERICS / e / "summary.json") for e in EXPERIMENTS}

    def test_section_1_results(self):
        thermal = self.summaries["exp4"]["thermal"]
        self.assertEqual(round(thermal["wAtA1"], 4), 0.3329)
        self.assertEqual(round(thermal["wAtAEnd"], 4), 0.0359)
        model = self.summaries["exp3"]["models"][0]
        self.assertEqual(model["x0"], -0.462654)
        self.assertEqual(round(model["waTangent"], 2), -4.81)
        self.assertEqual(round(model["zBounce"], 3), 0.388)
        self.assertAlmostEqual(model["waTangent"] / -0.60, 8.0, delta=0.05)
        for phrase in ("$w=0.3329$ at $a=1$", "$w=0.0359$ at $a=100$", "$w_a=-4.81$",
                       "bounces at redshift $z=0.388$"):
            self.assertIn(phrase, self.text)

    def test_exp1_values(self):
        parameters = self.summaries["exp1"]["parameters"]
        self.assertIn("$M_*=%r$" % parameters["lambdaSelfConsistentMass"], self.text)
        self.assertEqual((parameters["windowT1"], parameters["windowT2"], parameters["windowWidth"]),
                         (2.0, 7.0, 0.5))
        self.assertEqual(parameters["hiddenMomenta"], [0.0, 0.5, 2.0])
        self.assertEqual(self.summaries["exp1"]["grid"]["sampleCount"], 201)
        self.assertEqual(len(self.summaries["exp1"]["runs"]), 26)

    def test_exp2_initial_data(self):
        runs = {run["x0"]: run for run in self.summaries["exp2"]["runs"]}
        for x0, s0, lam in ((0.0, 1.32, 0.0), (-0.4, 2.2, -0.363636), (0.5, 0.88, 1.136364)):
            with self.subTest(x0=x0):
                self.assertAlmostEqual(runs[x0]["S0"], s0, places=12)
                self.assertAlmostEqual(runs[x0]["lambda"], lam, places=6)
                self.assertAlmostEqual(runs[x0]["constraintLhs0"], 1.32, places=12)
                self.assertAlmostEqual(runs[x0]["exact"]["alpha"], 7 * s0 / 12, places=12)
                self.assertAlmostEqual(runs[x0]["exact"]["theta0"], 2.4, places=12)
        self.assertIn("$S_0=1.32$, $2.2$, $0.88$ and $\\lambda=0$, $-0.363636$, $1.136364$", self.text)

    def test_exp3_parameters_and_closed_forms(self):
        parameters = self.summaries["exp3"]["parameters"]
        self.assertEqual((parameters["OmegaR"], parameters["OmegaM"], parameters["OmegaPsi"]),
                         (0.00009, 0.305, 0.69491))
        self.assertEqual(parameters["x0Values"], [-0.462654, -0.433107, -0.3, -0.2, 0.0])
        self.assertEqual(parameters["muValues"], [3.0, 7.0])
        for w0, x0 in ((-0.861, -0.462654), (-0.764, -0.433107)):
            self.assertAlmostEqual(w0 / (1 - w0), x0, places=6)

    def test_exercise_13_3_answers(self):
        rows = csv_rows(NUMERICS / "exp1" / "run_A1_K2_pos_Bp.csv")
        energy = math.sqrt(5.0)
        expected = {"energy_mode": energy, "rho": energy, "p_0": 4 / energy, "p_mean": 4 / energy / 7,
                    "w": 4 / 35, "KE_L": energy / 2, "PE_L": energy / 2}
        for key, value in expected.items():
            for row in (rows[0], rows[-1]):
                self.assertAlmostEqual(float(row[key]), value, delta=1e-8)
        for phrase in ("$E=\\sqrt{1+4}=2.23607=\\varepsilon=\\rho$", "$p_0=K^2/E=1.78885$",
                       "$\\bar p=p_0/7=0.25555$", "$w=K^2/(7E^2)=4/35=0.11429$",
                       "$KE_L=PE_L=E/2=1.11803$"):
            self.assertIn(phrase, self.text)

    def test_exercise_13_5_answers(self):
        rows = csv_rows(NUMERICS / "exp3" / "fits_scan.csv")
        row = [r for r in rows if abs(float(r["x0"]) + 0.25) < 1e-9][0]
        self.assertAlmostEqual(float(row["w0_tangent"]), -1 / 3, places=12)
        self.assertAlmostEqual(float(row["wa_tangent"]), -4 / 3, places=12)
        self.assertEqual(round(float(row["z_zero"]), 5), 0.58740)
        self.assertEqual(round(float(row["z_cross"]), 5), 0.25992)
        self.assertEqual(round(float(row["z_bounce"]), 5), 0.74542)
        self.assertEqual(round(0.25 ** (1 / 3), 5), 0.62996)
        self.assertEqual(round(0.5 ** (1 / 3), 5), 0.79370)
        for phrase in ("$z=1/a-1=0.58740$", "$z=0.25992$", "$z_b=0.74542$",
                       "$a=\\lvert x_0\\rvert^{1/3}=0.62996$", "$a=(2\\lvert x_0\\rvert)^{1/3}=0.79370$"):
            self.assertIn(phrase, self.text)
        row = [r for r in rows if abs(float(r["x0"]) + 0.474) < 1e-9][0]
        self.assertEqual(round(float(row["w0_tangent"]), 5), -0.90114)
        self.assertEqual(round(float(row["wa_tangent"]), 4), -5.1396)
        x0 = -0.9 / 1.9
        self.assertEqual(round(x0, 5), -0.47368)
        self.assertEqual(round(3 * x0 / (1 + x0) ** 2, 2), -5.13)
        self.assertIn("gives $w_0=-0.90114$, $w_a=-5.1396$", self.text)

    def test_exercise_13_4_and_13_6_predictions(self):
        c0 = 3 * 1.0 + 3 * 0.3 ** 2 + 9 * 1.0 * (-0.3)
        self.assertAlmostEqual(c0, 0.57, places=12)
        self.assertAlmostEqual(0.57 / 6, 0.095, places=12)
        self.assertEqual(round(0.3 / 0.095, 3), 3.158)
        self.assertEqual(round(math.log(5.0), 5), 1.60944)
        self.assertIn("$t^*=\\ln(1/0.2)=\\ln5=1.60944$", self.text)
        for q, run in ((0.05, "q0p05_Cp"), (0.1, "q0p1_Cp")):
            record = [r for r in self.summaries["exp5"]["runs"] if r["id"] == run][0]
            self.assertAlmostEqual(record["tStar"], math.log(1 / q), places=12)

    def test_exercise_13_7_pair_numbers(self):
        masses = {entry["m"]: entry["nA3"] for entry in self.summaries["exp4"]["pair"]["masses"]}
        self.assertLess(masses[0.0], 1e-23)
        self.assertEqual(float("%.2g" % masses[0.1]), 1.5e-3)
        self.assertEqual(round(masses[0.1], 5), 0.00145)
        self.assertEqual(round(masses[0.5], 5), 0.00499)
        self.assertIn("$na^3=1.8\\times10^{-24}$", self.text)
        self.assertEqual(float("%.2g" % masses[0.0]), 1.8e-24)
        self.assertIn("$1.45\\times10^{-3}$ for $m=0.1$ and $4.99\\times10^{-3}$ for $m=0.5$", self.text)


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


class PdfGlyphTests(GuideTestCase):
    """pdflatex does not warn about these substitutions, so the PDF itself is checked: no
    '--' en-dash ligature and no curly left quote in the typewriter font (commands are copied
    from it), and no \\mathbb 1 (msbm slot 49 is 'notforces')."""

    def test_no_endash_quoteleft_or_notforces(self):
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
