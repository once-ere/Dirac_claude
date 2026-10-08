#!/usr/bin/env python3
"""Publication test for Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY (md + tex + pdf).

Run from the repository root:
    python -m unittest Revision/tests/test_dirac16complex00_field_theory_publication.py -v

What is tested (nothing is rebuilt with pdflatex here; the committed files are never touched)
  * the committed .tex is exactly what scripts/build_dissertation_tex.py makes of the .md with the
    options that scripts/build_provenance_pdf.py --developer-layout passes (strip heading numbers,
    developer layout, default author and date, figures checked under the repository root); the
    conversion is deterministic (two runs equal) and md and tex are LF-only;
  * the PDF is registered in Revision/pdf-specifications.json (Revision's own registry) under the
    edition dirac16complex00-field-theory with this path, its page count and its sha256, and it has
    the PDF header, the end marker and US-letter media boxes;
  * the exact formula blocks of the document are the ones generated here from the Revision outputs
    (the 16 component field equations from Revision/theory/field-theory.json; the Lovelock components,
    the evolution factor, the Einstein case, the linear member and the off-diagonal kinetic
    coefficients from Revision/field_equations_a4/a4-equations.json);
  * every check name the document cites exists, with a passing verdict, in the Revision report the
    check index names, and every cited report passes as a whole;
  * key statements (Lagrangian, field equation, non-triviality [2], energy-momentum tensor, energy
    density, pressures, equations of state, the a4 equations, what is not claimed) are present, and
    the numbers the document quotes occur in the Revision outputs;
  * the document names no private input and uses only the characters the builder accepts.
Optional (REVISION_PDF_REBUILD=1, the switch shared by every Revision publication test; needs pdflatex): the PDF
is rebuilt in verify mode by scripts/build_provenance_pdf.py and must reproduce the registered edition.
"""

from __future__ import annotations

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
sys.path.insert(0, str(ROOT / "scripts"))
import build_dissertation_tex  # noqa: E402
import check_dissertation_pdf  # noqa: E402

STEM = "DIRAC16COMPLEX00_FIELD_THEORY"
DOCS = REVISION / "docs"
MD = DOCS / f"{STEM}.md"
TEX = DOCS / f"{STEM}.tex"
PDF = DOCS / f"{STEM}.pdf"
REGISTRY = REVISION / "pdf-specifications.json"
EDITION = "dirac16complex00-field-theory"
PDF_RELATIVE = f"Revision/docs/{STEM}.pdf"

FIELD_THEORY_JSON = REVISION / "theory" / "field-theory.json"
A4_JSON = REVISION / "field_equations_a4" / "a4-equations.json"

# Every report the document cites, with the key that holds its check list.
REPORTS = {
    "algebra/reports/wolfram-algebra.json": "checks",
    "algebra/reports/python-algebra.json": "checks",
    "theory/reports/wolfram-field-theory.json": "checks",
    "theory/reports/python-field-theory.json": "checks",
    "field_equations_a4/reports/wolfram-a4-report.json": "checks",
    "field_equations_a4/reports/python-a4-report.json": "checks",
    "pairing/reports/wolfram-pairing.json": "checks",
    "pairing/reports/python-pairing.json": "checks",
    "theory/reports/wolfram-scope.json": "checks",
    "theory/reports/python-scope.json": "checks",
    "dark_sector/dirac16complex00/reports/python-derive-eos.json": "checks",
    "dark_sector/dirac16complex00/reports/python-independent-numerics.json": "checks",
}
PASSING = {"PASS", "pass"}

PRIVATE_MARKERS = (
    "Gmail",
    "prompt_Dirac",
    "dirac-main",
    "vendor/",
    "Generalized_Kronecker_Delta",
)


# ---------------------------------------------------------------------------------------------
# readers
# ---------------------------------------------------------------------------------------------

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def report_checks(relative: str) -> dict[str, str]:
    data = load_json(REVISION / relative)
    return {c["name"]: c["verdict"] for c in data[REPORTS[relative]]}


def json_keys(value) -> set[str]:
    """All dictionary keys of a JSON value, recursively."""
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(key)
            keys |= json_keys(item)
    elif isinstance(value, list):
        for item in value:
            keys |= json_keys(item)
    return keys


def theory_formula(key: str):
    for entry in load_json(FIELD_THEORY_JSON)["formulas"]:
        if entry["key"] == key:
            return entry["wl"]
    raise KeyError(key)


# ---------------------------------------------------------------------------------------------
# generated formula blocks (the document must contain these lines verbatim)
# ---------------------------------------------------------------------------------------------

TERM_PATTERNS = (
    ("x4", re.compile(r'^dd\["x4", Psi\[(\d+)\]\]$')),
    ("mass", re.compile(r"^3\*H\*Psi\[(\d+)\]$")),
    ("space", re.compile(
        r'^dd\["x([123])", Psi\[(\d+)\]\]/\(E\^a4\[x4\]\*Sin\[6\*H\*x8\]\^\(1/6\)\)$')),
    ("time", re.compile(
        r'^\(E\^a4\[x4\]\*dd\["x([567])", Psi\[(\d+)\]\]\)/Sin\[6\*H\*x8\]\^\(1/6\)$')),
    ("hidden", re.compile(r'^dd\["x8", Psi\[(\d+)\]\]\*Tan\[6\*H\*x8\]$')),
)


def parse_component_equation(text: str) -> dict:
    """Split one Wolfram component equation of field-theory.json into its typed terms."""
    lhs, rhs = text.split(" == ")
    target = re.fullmatch(r"V\*Psi\[(\d+)\]", rhs)
    if target is None:
        raise ValueError(f"unexpected right-hand side {rhs!r}")
    pieces = re.split(r" (?=[+-] )", lhs.strip())
    terms = {"space": {}, "time": {}}
    for piece in pieces:
        sign = 1
        piece = piece.strip()
        if piece.startswith("+ "):
            piece = piece[2:]
        elif piece.startswith("- "):
            sign, piece = -1, piece[2:]
        elif piece.startswith("-"):
            sign, piece = -1, piece[1:]
        for kind, pattern in TERM_PATTERNS:
            match = pattern.fullmatch(piece)
            if match is None:
                continue
            if kind in ("space", "time"):
                terms[kind][int(match.group(1))] = (sign, int(match.group(2)))
            else:
                terms[kind] = (sign, int(match.group(1)))
            break
        else:
            raise ValueError(f"unrecognised term {piece!r}")
    terms["target"] = int(target.group(1))
    return terms


def signed(sign: int, body: str, first: bool) -> str:
    if first:
        return ("-" if sign < 0 else "") + body
    return (" - " if sign < 0 else " + ") + body


def component_equation_lines() -> list[tuple[str, str]]:
    """The 16 component equations as pairs of LaTeX lines (aligned rows) for the document."""
    lines = []
    for text in theory_formula("field_equation_components"):
        t = parse_component_equation(text)
        if t["mass"] != (1, t["hidden"][1]) or t["hidden"][0] != 1:
            raise ValueError("the 3 H and tan z d8 terms must act on the same component with +")
        s4, i4 = t["x4"]
        space = "".join(
            signed(t["space"][d][0], rf"\partial_{d}\Phi_{{{t['space'][d][1]}}}", d == 1)
            for d in (1, 2, 3)
        )
        time = "".join(
            signed(t["time"][d][0], rf"\partial_{d}\Phi_{{{t['time'][d][1]}}}", d == 5)
            for d in (5, 6, 7)
        )
        first = (
            rf"({t['target']})\;\; & "
            + signed(s4, rf"\partial_4\Phi_{{{i4}}}", True)
            + rf" + u\,({space}) \\"
        )
        second = (
            rf"& + v\,({time}) + (t\,\partial_8 + 3H)\,\Phi_{{{t['hidden'][1]}}}"
            + rf" = V\,\Phi_{{{t['target']}}}"
        )
        lines.append((first, second))
    return lines


def lovelock_component_tex() -> dict[tuple[str, str], str]:
    """(E1|E2|E3, x1x1|x4x4|x5x5|x8x8) -> tex of a4-equations.json."""
    tensors = load_json(A4_JSON)["lovelockTensors"]
    return {
        (k, c): tensors[k][c]["tex"]
        for k in ("E1", "E2", "E3")
        for c in ("x1x1", "x4x4", "x5x5", "x8x8")
    }


def notation(tex: str) -> str:
    """The only notational changes applied to the tex of a4-equations.json: (cot z)^2 is
    written \\cot^2 z, and a thin space separates a radical from a following factor H."""
    return tex.replace(r"\cot z^2", r"\cot^2 z").replace(r"+1} H", r"+1}\, H")


SPACE = ("x1", "x2", "x3")
EXTRA_TIMES = ("x5", "x6", "x7")


def index_class(index: str) -> str:
    """x1..x3 -> x_i (3-space), x5..x7 -> x_t (extra times), x4 -> x_4, x8 -> x_8."""
    if index in SPACE:
        return "x_i"
    if index in EXTRA_TIMES:
        return "x_t"
    return "x_" + index[1:]


def offdiagonal_rows() -> list[tuple[str, str, str]]:
    """The 42 off-diagonal kinetic components of the condensate, grouped by index class:
    (component, bilinear, coefficient); every member of a group must give the same bilinear
    pattern (its own 3-space index i and extra-time index t substituted) and the same coefficient."""
    entries = load_json(A4_JSON)["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    groups: dict[tuple[str, str], tuple[str, str]] = {}
    sizes: dict[tuple[str, str], int] = {}
    for entry in entries:
        (term,) = entry["terms"]
        upper, lower = re.fullmatch(r"K\^(x\d)_(x\d) \(symmetrised\)", entry["component"]).groups()
        pattern = term["bilinear"]
        for index in (upper, lower):
            if index in SPACE + EXTRA_TIMES:
                pattern = pattern.replace(f"gamma^{index} ", f"gamma^{index_class(index)} ")
        if re.search(r"gamma\^x[1235-7] ", pattern):
            raise ValueError(f"{entry['component']}: a free index remains in {pattern!r}")
        value = (pattern, notation(term["coefficient"]["tex"]))
        key = (index_class(upper), index_class(lower))
        if groups.setdefault(key, value) != value:
            raise ValueError(f"{entry['component']}: the group {key} is not uniform")
        sizes[key] = sizes.get(key, 0) + 1
    if sum(sizes.values()) != 42:
        raise ValueError("expected 42 ordered off-diagonal components")
    rows = []
    for (upper, lower), (pattern, coefficient) in groups.items():
        latex = (
            pattern.replace("Phibar ", r"\bar\Phi ")
            .replace(" Phi", r" \Phi")
            .replace("gamma^x_i", r"\gamma^{x_i}")
            .replace("gamma^x_t", r"\gamma^{x_t}")
            .replace("gamma^x4", r"\gamma^{x_4}")
            .replace("gamma^x8", r"\gamma^{x_8}")
        )
        rows.append((rf"$K^{{{upper}}}{{}}_{{{lower}}}$", f"${latex}$", f"${coefficient}$"))
    return rows


def offdiagonal_table_lines() -> list[str]:
    return [f"| {a} | {b} | {c} |" for a, b, c in offdiagonal_rows()]


# ---------------------------------------------------------------------------------------------
# normalisation for formula comparison
# ---------------------------------------------------------------------------------------------

def squash(text: str) -> str:
    """Remove line-break markup and spaces so that a formula may be split over aligned rows."""
    text = text.replace(r"\\", "").replace("&", "")
    text = re.sub(r"\\q?quad", "", text)
    return re.sub(r"\s+", "", text)


def markdown_text() -> str:
    return MD.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------------------------
# tests
# ---------------------------------------------------------------------------------------------

class TestFilesAndBuild(unittest.TestCase):
    def test_files_exist_lf_only(self):
        for path in (MD, TEX, PDF):
            self.assertTrue(path.is_file(), f"missing {path}")
        for path in (MD, TEX):
            self.assertNotIn(b"\r", path.read_bytes(), f"{path} must use LF line endings")

    def test_tex_equals_builder_output(self):
        latex = build_dissertation_tex.convert(
            markdown_text(),
            strip_heading_numbers=True,
            developer_layout=True,
            author=build_dissertation_tex.DEFAULT_AUTHOR,
            date=build_dissertation_tex.DEFAULT_DATE,
            image_root=ROOT,
        )
        self.assertEqual(latex.encode("utf-8"), TEX.read_bytes())
        again = build_dissertation_tex.convert(
            markdown_text(),
            strip_heading_numbers=True,
            developer_layout=True,
            image_root=ROOT,
        )
        self.assertEqual(latex, again)

    def test_pdf_registered(self):
        registry = load_json(REGISTRY)
        self.assertIn(EDITION, registry, "edition not registered in Revision/pdf-specifications.json")
        entry = registry[EDITION]
        self.assertEqual(sorted(entry), ["pages", "path", "sha256"])
        data = PDF.read_bytes()
        self.assertEqual(entry["path"], PDF_RELATIVE)
        self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(entry["pages"], len(check_dissertation_pdf.PAGE_PATTERN.findall(data)))
        self.assertTrue(data.startswith(b"%PDF-"))
        self.assertTrue(data.rstrip().endswith(b"%%EOF"))
        self.assertEqual(
            check_dissertation_pdf.parse_media_boxes(data), [(0.0, 0.0, 612.0, 792.0)]
        )

    def test_only_builder_characters_and_no_private_inputs(self):
        text = markdown_text()
        build_dissertation_tex.validate_characters(text, "Markdown")
        for marker in PRIVATE_MARKERS:
            self.assertNotIn(marker, text, f"private input named: {marker}")


class TestGeneratedFormulaBlocks(unittest.TestCase):
    def test_sixteen_component_equations(self):
        text = markdown_text()
        lines = component_equation_lines()
        self.assertEqual(len(lines), 16)
        for first, second in lines:
            self.assertIn(first, text)
            self.assertIn(second, text)

    def test_lovelock_components(self):
        text = squash(markdown_text())
        for (k, c), tex in lovelock_component_tex().items():
            index = c[:2].replace("x", "x_")
            label = f"E_{{({k[1]})}}{{}}^{{{index}}}{{}}_{{{index}}}"
            wanted = squash(label) + "=" + squash(tex)
            position = text.find(wanted)
            self.assertGreaterEqual(position, 0, f"{k} {c}")
            # the component must end there (no further terms appended)
            self.assertIn(text[position + len(wanted)], ",.;$", f"{k} {c}")

    def test_a4_equations_and_special_cases(self):
        data = load_json(A4_JSON)
        text = squash(markdown_text())
        wanted = [
            data["generalSource"]["evolution_F"]["tex"],
            data["generalSource"]["algebraic_condition"]["tex"],
            data["einstein"]["constraint_x4"]["tex"],
            data["einstein"]["space_x1"]["tex"],
            data["einstein"]["extraTime_x5"]["tex"],
            data["einstein"]["hidden_x8"]["tex"],
            data["einstein"]["evolution"]["tex"],
            data["einstein"]["nullEnergy"]["tex"],
            data["linearMember"]["rho"]["tex"],
            data["linearMember"]["p"]["tex"],
            data["linearMember"]["vacuumFactor"]["tex"],
        ]
        for tex in wanted:
            self.assertIn(squash(tex), text, tex)

    def test_offdiagonal_coefficients(self):
        text = markdown_text()
        lines = offdiagonal_table_lines()
        self.assertEqual(len(lines), 10)
        for line in lines:
            self.assertIn(line, text)


class TestCitedChecks(unittest.TestCase):
    def test_reports_pass(self):
        for relative in REPORTS:
            verdicts = report_checks(relative)
            self.assertTrue(verdicts, relative)
            failing = [n for n, v in verdicts.items() if v not in PASSING]
            self.assertEqual(failing, [], relative)

    def test_check_index_names_exist_and_pass(self):
        text = markdown_text()
        index = text.split("## 14. Check index", 1)[1].split("\n## ", 1)[0]
        cited = 0
        for line in index.splitlines():
            match = re.match(r"\|\s*`Revision/([^`]+)`\s*\|(.*)\|\s*$", line)
            if not match:
                continue
            relative, names = match.group(1), match.group(2)
            self.assertIn(relative, REPORTS, relative)
            verdicts = report_checks(relative)
            for name in re.findall(r"`([^`]+)`", names):
                cited += 1
                self.assertIn(name, verdicts, f"{name} not in {relative}")
                self.assertIn(verdicts[name], PASSING, f"{name} in {relative}")
        self.assertGreater(cited, 60)

    def test_check_counts_quoted_in_the_index(self):
        text = markdown_text()
        sentence = text.split("Counts at the time of writing:", 1)[1].split("\n", 1)[0]
        quoted = re.findall(r"((?:wolfram|python)-[a-z0-9-]+) (\d+)", sentence)
        self.assertEqual(len(quoted), len(REPORTS))
        by_stem = {Path(relative).stem: relative for relative in REPORTS}
        for stem, count in quoted:
            self.assertIn(stem, by_stem)
            self.assertEqual(len(report_checks(by_stem[stem])), int(count), stem)

    def test_every_cited_identifier_is_known(self):
        known = set()
        for relative in REPORTS:
            known.update(report_checks(relative))
        known.update(entry["key"] for entry in load_json(FIELD_THEORY_JSON)["formulas"])
        for source in (A4_JSON, REVISION / "pairing" / "pairing-theory.json"):
            known.update(json_keys(load_json(source)))
        for relative in REPORTS:
            known.update(load_json(REVISION / relative))  # top-level sections of the reports
        text = markdown_text()
        unknown = []
        for token in re.findall(r"`([^`\s]+)`", text):
            if "/" in token or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*_[A-Za-z0-9_.]*", token):
                continue
            if token.endswith((".json", ".md", ".py", ".wls", ".wl", ".tex", ".pdf", "_")):
                continue  # file names and name prefixes such as commuting_
            if token not in known:
                unknown.append(token)
        self.assertEqual(unknown, [])


class TestKeyStatements(unittest.TestCase):
    STATEMENTS = (
        "16 complex commuting components",
        r"\mathcal{L} = \sqrt{|g|}\,\Big[\tfrac12\big(\bar\Phi\gamma^\mu D_\mu\Phi"
        r" - (D_\mu\bar\Phi)\gamma^\mu\Phi\big) - m\,S - U(S)\Big]",
        r"\gamma^\mu D_\mu\Phi = \big(m + U'(S)\big)\,\Phi",
        r"\gamma^\mu\Omega_\mu = 3H\,\gamma^{(x_8)}",
        r"\sqrt{|g|} = \cos z",
        r"R = 6\big((a_4')^2 - 7H^2\big)",
        r"R^{x_8}{}_{x_8} = -6H^2",
        "NON-TRIVIALITY [2]",
        r"\rho = -T^{x_4}{}_{x_4}",
        r"\rho = m S + U(S)",
        r"p_3 = p_t = p_8 = S\,U'(S) - U(S)",
        r"w = \frac{\lambda S}{2m + \lambda S}",
        r"\frac{d\rho}{dx_4} = -3\,a_4'\,(p_3 - p_t)",
        r"a_4 = A H x_4 + a_0",
        r"\kappa\, m S = -(36H^2 + 2\Lambda)",
        r"6(A^2 + 1)H^2 = -\kappa\, S\,(m + \lambda S)",
        "is not quantised",
        "## 15. What is not claimed",
        "no creation process",
        "**Scope of [2] (exact).**",
        "The value $\\gamma^\\mu\\Omega_\\mu = 3H\\gamma^{(x_8)}$ belongs to the diagonal vielbein",
        "What cannot be removed in any frame is $\\Omega_\\mu$ itself",
        "The classical energy of dirac16complex00 is unbounded below already for $U = 0$",
        "This does not make the Cauchy problem well posed",
        "which is a choice of sign and is not selected by the equations",
        "are interpretations",
        "That record establishes neither Hypothesis nor Hypothesis00",
        "because its two free parameters were CHOSEN to solve the two tangent conditions",
        "a crossing of $w = -1$ occurs only with a component of negative classical energy",
        r"the tuned value $\lambda S/m = -382/441$",
        "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
        "`Revision/docs/LOVELOCK_GKD`",
        "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    )

    def test_statements_present(self):
        text = markdown_text()
        for statement in self.STATEMENTS:
            self.assertIn(statement, text, statement)

    def test_quoted_numbers_occur_in_the_outputs(self):
        a4_report = (REVISION / "field_equations_a4/reports/wolfram-a4-report.json").read_text(
            encoding="utf-8"
        )
        for number in ("51200", "28800", "{4, 3, 4}", "(5, 4/3)"):
            self.assertIn(number, a4_report)
            self.assertIn(number.strip("{}").replace(", ", ", "), markdown_text())
        derive = (REVISION / "dark_sector/dirac16complex00/reports/python-derive-eos.json").read_text(
            encoding="utf-8"
        )
        for in_report, in_document in (
            ("lambda S/m = -382/441", r"$\lambda S/m = -382/441$"),
            ("= (-0.861, -0.600) = the Unite CPL values", "$(w_0, w_a) = (-0.861, -0.60)$"),
            ("= w_eff(N1) - 1", "differ by exactly $-1$"),
        ):
            self.assertIn(in_report, derive)
            self.assertIn(in_document, markdown_text())


@unittest.skipUnless(os.environ.get("REVISION_PDF_REBUILD") == "1", "set REVISION_PDF_REBUILD=1 to rebuild the PDF in verify mode")
class TestPdfRebuild(unittest.TestCase):
    def test_rebuild_in_verify_mode(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_provenance_pdf.py"), f"Revision/docs/{STEM}.md",
             "--developer-layout", "--specifications", "Revision/pdf-specifications.json"],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, timeout=1800)
        output = completed.stdout.decode("utf-8", "replace")
        self.assertEqual(completed.returncode, 0, output[-3000:])
        self.assertIn("check_logWarningFree=true", output)
        self.assertIn("provenance_pdf=OK", output)


if __name__ == "__main__":
    unittest.main()
