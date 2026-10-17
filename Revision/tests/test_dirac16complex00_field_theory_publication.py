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
    for the corrected metric of 2026-10-16 (version 2) (the 16 component field equations, with the
    gravity terms (3/2) H e^a4 b4^(-1/2) gamma^(x0) and (b4'/b4 - a4'/2) gamma^(x4), from
    Revision/theory/field-theory.json; the Lovelock components in a4', a4'', u = b4'/b4, v = u',
    k = e^(2 a4)/b4, the Einstein case, the sources required by the exponential histories and by the
    background history, and the off-diagonal kinetic coefficients of the condensate from
    Revision/field_equations_a4/a4-equations.json);
  * every check name the document cites exists, with a passing verdict, in the Revision report the
    check index names, and every cited report passes as a whole;
  * key statements (Lagrangian, field equation, non-triviality [2], energy-momentum tensor, energy
    density, pressures, equations of state, the a4 and b4 equations, what is not claimed) are
    present, no statement of the withdrawn metrics (2026-10-14 and version 1 of 2026-10-16) is left
    as a result, and the numbers the document quotes occur in the Revision outputs;
  * the document names no private input and uses only the characters the builder accepts.
Optional (REVISION_PDF_REBUILD=1, the switch shared by every Revision publication test; needs pdflatex): the PDF
is rebuilt in verify mode by scripts/build_provenance_pdf.py and must reproduce the registered edition.
"""

from __future__ import annotations

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

GRAVITY = r"\(-1/2\*Derivative\[1\]\[a4\]\[x4\] \+ Derivative\[1\]\[b4\]\[x4\]/b4\[x4\]\)"
TERM_PATTERNS = (
    ("x4", re.compile(r'^dd\["x4", Psi\[(\d+)\]\]$')),
    # the hidden-block term (3/2) H e^a4 b4^(-1/2) gamma^(x0) of the spin connection
    ("mass", re.compile(r"^\(3\*E\^a4\[x4\]\*H\*Psi\[(\d+)\]\)/\(2\*Sqrt\[b4\[x4\]\]\)$")),
    ("space", re.compile(r'^dd\["x([123])", Psi\[(\d+)\]\]/E\^a4\[x4\]$')),
    ("time", re.compile(  # the extra-time factor e^{a4} b4^{-1/2} (sin^2 z)^{-1/12}
        r'^\(E\^a4\[x4\]\*dd\["x([567])", Psi\[(\d+)\]\]\)/\(Sqrt\[b4\[x4\]\]\*\(Sin\[6\*H\*x0\]\^2\)\^\(1/12\)\)$')),
    ("hidden", re.compile(  # x0: the hidden direction, factor e^{a4} b4^{-1/2} tan z
        r'^\(E\^a4\[x4\]\*dd\["x0", Psi\[(\d+)\]\]\*Tan\[6\*H\*x0\]\)/Sqrt\[b4\[x4\]\]$')),
    ("b4", re.compile(  # the term (b4'/b4 - a4'/2) gamma^(x4) of the spin connection
        r"^Psi\[(\d+)\]\*" + GRAVITY + "$")),
)
SPACE_TERM = re.compile(r'dd\["x[123]", Psi\[\d+\]\]/E\^a4\[x4\]')


def top_level_terms(text: str) -> list[str]:
    """Split a Wolfram InputForm sum at the separators ' + ' and ' - ' outside brackets."""
    pieces, depth, start, i = [], 0, 0, 0
    while i < len(text):
        ch = text[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif depth == 0 and text.startswith((" + ", " - "), i):
            pieces.append(text[start:i])
            start = i + 1
            i += 2
            continue
        i += 1
    pieces.append(text[start:])
    return pieces


def parse_component_equation(text: str) -> dict:
    """Split one Wolfram component equation of field-theory.json into its typed terms."""
    lhs, rhs = text.split(" == ")
    target = re.fullmatch(r"V\*Psi\[(\d+)\]", rhs)
    if target is None:
        raise ValueError(f"unexpected right-hand side {rhs!r}")
    terms = {"space": {}, "time": {}}
    for piece in top_level_terms(lhs.strip()):
        sign = 1
        piece = piece.strip()
        if piece.startswith("+ "):
            piece = piece[2:]
        elif piece.startswith("- "):
            sign, piece = -1, piece[2:]
        elif piece.startswith("-"):
            sign, piece = -1, piece[1:]
        if piece.startswith("(") and piece.endswith(")") and SPACE_TERM.fullmatch(piece[1:-1]):
            piece = piece[1:-1]
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
    """The 16 component equations as pairs of LaTeX lines (aligned rows) for the document;
    hat-d4 = d4 + (b4'/b4 - a4'/2): the term v_g gamma^(x4) acts on the same component as d4, with the
    same sign; the term c_g gamma^(x0) acts on the component of the hidden-direction derivative."""
    lines = []
    for text in theory_formula("field_equation_components"):
        t = parse_component_equation(text)
        if t["mass"] != (1, t["hidden"][1]) or t["hidden"][0] != 1:
            raise ValueError("the (3/2) H and tan z d0 terms must act on the same component with +")
        if t["b4"] != t["x4"]:
            raise ValueError("the v_g term must act on the component of d4 with the sign of d4")
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
            + signed(s4, rf"\hat\partial_4\Phi_{{{i4}}}", True)
            + rf" + \epsilon_s\,({space}) \\"
        )
        second = (
            rf"& + \epsilon_t\,({time}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{{{t['hidden'][1]}}}"
            + rf" = V\,\Phi_{{{t['target']}}}"
        )
        lines.append((first, second))
    return lines


def lovelock_component_tex() -> dict[tuple[str, str], str]:
    """(E1|E2|E3, x0x0|x1x1|x4x4) -> tex of a4-equations.json (x5x5 equals x0x0, tested separately)."""
    tensors = load_json(A4_JSON)["lovelockTensors"]
    return {
        (k, c): tensors[k][c]["tex"]
        for k in ("E1", "E2", "E3")
        for c in ("x0x0", "x1x1", "x4x4")
    }


def notation(tex: str) -> str:
    """The only notational changes applied to the tex of a4-equations.json: (cot z)^2 is written
    \\cot^2 z, (sin z)^2 inside the off-diagonal coefficients \\sin^2 z, and a thin space separates a
    radical from a following factor H."""
    return (tex.replace(r"\cot z^2", r"\cot^2 z")
            .replace(r"\left(\sin z^2-1\right)", r"\left(\sin^2 z-1\right)")
            .replace(r"+1} H", r"+1}\, H"))


SPACE = ("x1", "x2", "x3")
EXTRA_TIMES = ("x5", "x6", "x7")


def index_class(index: str) -> str:
    """x1..x3 -> x_i (3-space), x5..x7 -> x_t (extra times), x4 -> x_4, x0 -> x_0."""
    if index in SPACE:
        return "x_i"
    if index in EXTRA_TIMES:
        return "x_t"
    return "x_" + index[1:]


def offdiagonal_rows() -> list[tuple[str, str, str]]:
    """The 36 off-diagonal kinetic components of the condensate, grouped by index class: one row
    (component, bilinear, coefficient) per term; every member of a group must give the same terms
    (its own 3-space index i and extra-time index t substituted) with the same coefficients."""
    entries = load_json(A4_JSON)["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    groups: dict[tuple[str, str], list[tuple[str, str]]] = {}
    sizes: dict[tuple[str, str], int] = {}
    for entry in entries:
        upper, lower = re.fullmatch(r"K\^(x\d)_(x\d) \(symmetrised\)", entry["component"]).groups()
        value = []
        for term in entry["terms"]:
            pattern = term["bilinear"]
            for index in (upper, lower):
                if index in SPACE + EXTRA_TIMES:
                    pattern = pattern.replace(f"gamma^{index} ", f"gamma^{index_class(index)} ")
            if re.search(r"gamma\^x[1235-7] ", pattern):
                raise ValueError(f"{entry['component']}: a free index remains in {pattern!r}")
            value.append((pattern, notation(term["coefficient"]["tex"])))
        key = (index_class(upper), index_class(lower))
        if groups.setdefault(key, value) != value:
            raise ValueError(f"{entry['component']}: the group {key} is not uniform")
        sizes[key] = sizes.get(key, 0) + 1
    if sum(sizes.values()) != 36:
        raise ValueError("expected 36 ordered off-diagonal components")
    rows = []
    for (upper, lower), value in groups.items():
        for pattern, coefficient in value:
            latex = (
                pattern.replace("Phibar ", r"\bar\Phi ")
                .replace(" Phi", r" \Phi")
                .replace("gamma^x_i", r"\gamma^{x_i}")
                .replace("gamma^x_t", r"\gamma^{x_t}")
                .replace("gamma^x4", r"\gamma^{x_4}")
                .replace("gamma^x0", r"\gamma^{x_0}")
            )
            rows.append((rf"$K^{{{upper}}}{{}}_{{{lower}}}$", f"${latex}$", f"${coefficient}$"))
    return rows


def offdiagonal_table_lines() -> list[str]:
    return [f"| {a}: {b} | {c} |" for a, b, c in offdiagonal_rows()]


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

    def test_component_parser_detects_a_changed_term(self):
        # negative control: a term with another factor is not recognised
        text = theory_formula("field_equation_components")[0].replace("(3*E^a4[x4]*H*", "(3*H*")
        with self.assertRaises(ValueError):
            parse_component_equation(text)

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

    def test_hidden_component_equals_extra_time_component(self):
        tensors = load_json(A4_JSON)["lovelockTensors"]
        for k in ("E1", "E2", "E3"):
            self.assertEqual(tensors[k]["x5x5"]["input"], tensors[k]["x0x0"]["input"], k)
        self.assertIn(r"$E_{(k)}{}^{x_5}{}_{x_5} = E_{(k)}{}^{x_0}{}_{x_0}$ for $k = 1, 2, 3$", markdown_text())

    def test_a4_equations_and_special_cases(self):
        data = load_json(A4_JSON)
        text = squash(markdown_text())
        einstein = data["einstein"]
        history = data["exponentialHistory"]
        wanted = [einstein[key]["tex"] for key in ("constraint_x4", "space_x1", "hidden_x0", "nullEnergy_x0",
                                                   "nullEnergy_x1")]
        wanted += [history["einstein"][key]["tex"] for key in ("rho", "p3", "p0")]
        for key in ("historySource_kappaT_minus_Lam", "einsteinHistorySource_kappaT_minus_Lam"):
            source = history["authorWeights"][key]
            self.assertEqual(source["p0"]["input"], source["pt"]["input"], key)
            wanted += [source[entry]["tex"] for entry in ("minus_rho", "p3", "p0")]
        for tex in wanted:
            self.assertIn(squash(tex), text, tex)
        self.assertIn(squash(r"\kappa p_0 - \Lambda = \kappa p_t - \Lambda &= "
                             + history["authorWeights"]["historySource_kappaT_minus_Lam"]["p0"]["tex"]), text)
        # the field equations need p0 = p_t and no off-diagonal source (record statements)
        self.assertIn("p0 = p_t", data["generalSource"]["hiddenEqualsExtraTimes"])
        self.assertIn("T^x4_x0 = T^x0_x4 = 0", data["generalSource"]["offDiagonal"])

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

    def test_every_check_named_in_the_sections_is_in_the_index(self):
        text = markdown_text()
        index = text.split("## 14. Check index", 1)[1].split("\n## ", 1)[0]
        body = text.split("## 14. Check index", 1)[0] + text.split("## 15. What is not claimed", 1)[1]
        indexed = set(re.findall(r"`([^`]+)`", index))
        names = set()
        for relative in REPORTS:
            names.update(report_checks(relative))
        missing = sorted(t for t in set(re.findall(r"`([^`\s]+)`", body)) if t in names and t not in indexed)
        self.assertEqual(missing, [])

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
        r"\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\,\gamma^{(x_0)} + \big(u - \tfrac12a_4'\big)\,\gamma^{(x_4)}",
        r"\big(\gamma^\mu\Omega_\mu\big)^2 = \big(\tfrac94H^2k - (u - \tfrac12a_4')^2\big)\,I_{16}",
        r"H^2\big(\tfrac94e^{2Hx_4/3} - \tfrac{25}{36}\big)I_{16} > 0",
        r"\sqrt{|g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}",
        r"R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4\frac{b_4''}{b_4} + u^2",
        r"for $a_4 = 0$, $b_4 = H^2x_4^2$ all 4096 Riemann components vanish",
        "21 independent nonzero Christoffel symbols",
        "Exactly 10 components with $a < b$ are nonzero",
        "$b_4$ is never 1",
        "NON-TRIVIALITY [2]",
        r"\rho = -T^{x_4}{}_{x_4}",
        r"\rho = m S + U(S)",
        r"p_3 = p_t = p_0 = S\,U'(S) - U(S)",
        r"w = \frac{\lambda S}{2m + \lambda S}",
        r"\frac{d\rho}{dx_4} = -3\,a_4'\,(\rho + p_3) - 4\,h_4\,(\rho + p_t), \qquad p_0 = p_t",
        r"e^{-a_4}b_4^{2}S = S_0",
        r"a_4 = A H x_4 + a_0",
        r"a_4 = Hx_4,\quad b_4 = b_4(0)\,e^{(4/3)Hx_4}",
        r"\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}",
        "they require $p_0 = p_t$ and a source without off-diagonal components",
        "is not quantised",
        "## 15. What is not claimed",
        "no creation process",
        "**Scope of [2] (exact).**",
        "belongs to the diagonal vielbein",
        "no boost in this plane removes",
        "What cannot be removed in any frame where the metric is curved is $\\Omega_\\mu$ itself",
        "The classical energy of dirac16complex00 is unbounded below already for $U = 0$",
        "This does not make the Cauchy problem well posed",
        "is a choice of sign and is not selected by the equations",
        "are interpretations",
        "That record establishes neither Hypothesis nor Hypothesis00",
        r"the tuned value $\lambda S/m = -382/441$",
        "no condensate is the source of the background history",
        "the corrected metric has no $Z_2$ orbifold",
        "`Revision/docs/DARK_SECTOR_HYPOTHESES`",
        "`Revision/docs/LOVELOCK_GKD`",
        "`Revision/docs/KOHN_SHAM_DEFLATING_FIELD`",
    )

    # statements of the withdrawn metrics that must not reappear as results
    STALE = (
        r"\sqrt{|g|} = \cos z",
        r"\sqrt{|g|} = b_4^{3/2}\cos z",
        r"3H\,\gamma^{(x_0)} + \tfrac34u",
        r"R^{x_0}{}_{x_0} = -6H^2",
        r"R = 6(a_4')^2 - 3a_4'u + 3u^2 + 3v - 42H^2",
        r"R = 6\big((a_4')^2 - 7H^2\big)",
        r"b_4^{3/2}S = S_0",
        "offDiagonalFactor_Q",
        "F(a_4')",
        "linear member",
        "sections 2 to 16 are written for it",
        "Not recomputed for general",
        "the case $b_4 = 1$",
        "-583/3000",
        "1583/1000",
        "never_flat_for_H_positive",
    )

    def test_statements_present(self):
        text = markdown_text()
        for statement in self.STATEMENTS:
            self.assertIn(statement, text, statement)
        for statement in self.STALE:
            self.assertNotIn(statement, text, statement)

    def test_quoted_numbers_occur_in_the_outputs(self):
        a4_report = (REVISION / "field_equations_a4/reports/wolfram-a4-report.json").read_text(
            encoding="utf-8"
        )
        for number in ("51200", "28800", "{4, 3, 4}", "(5, 4/3, 4)"):
            self.assertIn(number, a4_report)
            self.assertIn(number.strip("{}"), markdown_text())
        derive = (REVISION / "dark_sector/dirac16complex00/reports/python-derive-eos.json").read_text(
            encoding="utf-8"
        )
        for in_report, in_document in (
            ("lambda S/m = -382/441", r"$\lambda S/m = -382/441$"),
            ("returns (w0, wa) = (-0.861, -0.60)", "$(w_0, w_a) = (-0.861, -0.60)$"),
            ("w_eff = w_eff(N1) - (4 - 2 beta)/3", r"$w_{\rm eff}(N2) = w_{\rm eff}(N1) - (4 - 2\beta)/3$"),
            ("(-2749/9000, 81037/500000)", "$(-2749/9000, 81037/500000)$"),
            ("(-3583/9000, -196963/4500000)", "$(-3583/9000, -196963/4500000)$"),
            ("(-0.398111111111, -0.0666666666667)", "$(-0.398111111111, -0.0666666666667)$"),
            ("needs G >= 3749/3000", r"$G \geq 3749/3000$"),
            ("(-0.443790594178, -0.32308292878)", "$(-0.443790594178, -0.32308292878)$"),
            ("-28077/12500 = -2.24616", "$w_a = -28077/12500 = -2.24616$"),
            ("-9*kk**2/16 + 1069*kk/432 + 2015/972",
             r"\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972}"),
        ):
            self.assertIn(in_report, derive)
            self.assertIn(in_document, markdown_text())

    @staticmethod
    def turning_points_statement(models) -> str:
        """The turning points a_* of M3 and M4 as section 10 quotes them, from eos-theory.json."""
        m3 = models["M3_positive_extra_time_mode"]["turning_point_a_star"]
        match = re.fullmatch(r"\((\d+/\d+)\)\^\(3/2\)", m3["exact"])  # a_* = s^(-3/2)
        if match is None:
            raise AssertionError(f"M3 turning point: unexpected exact form {m3['exact']!r}")
        exact = Fraction(match.group(1))
        if abs(math.sqrt(exact) ** 3 - float(m3["decimal"])) >= 1e-10:
            raise AssertionError(f"M3 turning point: decimal and exact value differ: {m3}")
        m4 = float(models["M4_condensate_plus_extra_time_mode"]["turning_point_a_star"])
        return f"(M3: $a_* = {float(m3['decimal']):.4f}$, M4: $a_* = {m4:.4f}$)"

    def test_turning_points_from_the_record(self):
        models = load_json(REVISION / "dark_sector/dirac16complex00/eos-theory.json")["models"]
        self.assertIn(self.turning_points_statement(models), markdown_text())

    def test_turning_points_detect_a_change(self):
        # negative controls: a changed turning point in the record or in the text is detected
        models = load_json(REVISION / "dark_sector/dirac16complex00/eos-theory.json")["models"]
        statement = self.turning_points_statement(models)
        self.assertNotIn(statement, markdown_text().replace("M4: $a_* = 1.8859$", "M4: $a_* = 1.8860$"))
        self.assertNotIn(statement, markdown_text().replace("M3: $a_* = 6.2640$", "M3: $a_* = 6.2639$"))
        models["M4_condensate_plus_extra_time_mode"]["turning_point_a_star"] = "1.88599"
        self.assertNotIn(self.turning_points_statement(models), markdown_text())
        models["M3_positive_extra_time_mode"]["turning_point_a_star"] = {"decimal": "6.26398476691",
                                                                         "exact": "(1417/418)^(3/2)"}
        with self.assertRaises(AssertionError):
            self.turning_points_statement(models)


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
