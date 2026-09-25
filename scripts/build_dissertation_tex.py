#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Origin: scripts/build_dissertation_tex.py of
# https://github.com/once-ere/dirac (GPL-3.0-or-later), copied into this
# repository on 2026-09-25 and modified.
#
# Changes relative to the origin:
#   * --author and --date options, and author=/date= keyword arguments of
#     convert().  Defaults: author "dirac16complex project (with Claude Opus
#     5.5)", date "September 2026".  The positional signature
#     convert(markdown, strip_heading_numbers, developer_layout) is unchanged.
#   * --input is required (the origin defaulted to a dissertation that does
#     not exist here); --output defaults to the input path with suffix .tex.
#   * The Markdown subset is extended, backward-compatibly:
#       - non-ASCII Greek letters and mathematical symbols (the table
#         MATH_CHARACTERS) may be written directly, in prose, headings, table
#         cells, list items, inline and display math, code spans and fenced
#         code.  Each character that occurs is declared in the preamble with
#         \DeclareUnicodeCharacter{XXXX}{\ensuremath{...}}; inside math it is
#         replaced by its LaTeX command (so $Ψ^†$ becomes $\Psi ^\dagger $).
#         Every other non-ASCII character must be one of the vetted Latin
#         letters and punctuation marks in TEXT_CHARACTERS; any other one is
#         rejected with a ValueError naming line and code point, instead of
#         failing later inside pdflatex.
#       - Markdown links [text](url) are rendered as \href{url}{text}; the URL
#         must be ASCII RFC 3986 characters; #, % and & are escaped.
#       - inline math and links in headings are wrapped in
#         \texorpdfstring{...}{plain text} so that the hyperref bookmarks
#         stay warning-free (bold, emphasis and code spans need no wrapper).
#       - code spans containing #, %, a backslash, unbalanced braces or a
#         non-ASCII character are escaped character by character instead of
#         being passed through \detokenize (which doubles # and cannot hold %).
#         In headings the same applies to spans containing _ ^ $ & ~ or
#         braces: the origin's \detokenize{x_y} is expanded into the .toc
#         file and re-read there as a subscript ("Missing $ inserted").
#       - list items and table data rows whose text starts with [ or * get a
#         leading {} so that \item and the \\ ending the previous row do not
#         read it as an optional argument.
#       - figures (added 2026-09-25): a line that consists of exactly one
#         Markdown image, ![caption text](relative/path.png), outside fenced
#         code and display math, becomes
#             \begin{figure}[htbp]
#             \centering
#             \includegraphics[width=0.92\linewidth]{relative/path.png}
#             \caption{caption text}
#             \end{figure}
#         The caption gets the inline markup of a heading (it is a moving
#         argument, written to the .aux file).  \usepackage{graphicx} is added
#         to the preamble, after fancyvrb, only when the document contains at
#         least one figure, so every document without one keeps its bytes.
#         The path is written verbatim and is RELATIVE TO THE REPOSITORY
#         ROOT: ASCII letters, digits, "-", "_" and "." in "/"-separated
#         segments, no "." or ".." segment, no leading "/", and a final
#         segment NAME.png with exactly one dot (PNG only; pdfTeX embeds a PNG
#         without any timestamp, so two builds stay byte-identical).  No
#         \graphicspath is emitted: it would have to depend on where the .tex
#         file lies, and build_provenance_pdf.py compiles two copies at
#         different places (D/X.tex and build/X/X-repeat.tex) that must be
#         byte-identical.  Instead pdflatex MUST run with the repository root
#         as its working directory (TeX looks a relative \includegraphics
#         path up in the current directory first), which is exactly how
#         build_provenance_pdf.py invokes it:
#             cd <root>; pdflatex -interaction=nonstopmode -halt-on-error
#               -jobname=X -output-directory=build/X/pdf-a D/X.tex
#         The command line checks every figure before writing the .tex: it
#         must be an existing file under --image-root (default: the
#         repository that contains this script; build_provenance_pdf.py
#         passes its --repository-root), spelled with the exact case of the
#         file system (Windows would find Fig.PNG for fig.png, Linux would
#         not), and it must start with the PNG signature.  convert() does the
#         same when image_root= is given and only the syntactic checks
#         otherwise.  A figure taller than the text block makes LaTeX warn
#         "Float too large", which the log scan of build_provenance_pdf.py
#         reports.  An image anywhere else (inside a paragraph, a list item,
#         a table cell or a heading) is still rejected.
#   * Structural validation (ValueError): unterminated fenced code or display
#     math, fenced-code lines longer than MAX_CODE_LINE_LENGTH (89) characters
#     or containing a tab (they would overflow the \small Verbatim line),
#     table rows whose cell count differs from the header, Markdown images
#     other than a figure line, figure lines with an empty caption or an
#     unsupported path.
#     The 89-character limit counts typewriter characters; a Unicode math
#     symbol inside fenced code is set in the math font and may be wider, so
#     such lines must be kept shorter (the log scan of build_provenance_pdf.py
#     reports any Overfull line).
#   * Unchanged: the preamble for documents that use none of the extensions,
#     and every determinism primitive (\pdfobjcompresslevel=0,
#     \pdfinfoomitdate=1, \pdftrailerid{}, \pdfsuppressptexinfo=15, LF-only
#     UTF-8 output).  With author="Reproducible exact-real implementation"
#     (ORIGIN_AUTHOR) the output is byte-identical to the origin's for every
#     document that avoids the constructs listed above.
#     tests/test_publication_tooling.py checks this for a built-in document
#     of the old subset and, when dirac-main/ is present, for the eight
#     dirac-main documents whose .tex the origin produced.
"""Convert a provenance or dissertation Markdown file to standalone LaTeX."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import unicodedata
from pathlib import Path


DEFAULT_AUTHOR = "dirac16complex project (with Claude Opus 5.5)"
DEFAULT_DATE = "September 2026"
ORIGIN_AUTHOR = "Reproducible exact-real implementation"
# \small Verbatim in an 11pt article with 1in margins: 469.75pt / 5.25pt.
MAX_CODE_LINE_LENGTH = 89
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

# Figure paths (see figure_line and validate_figure_path).
FIGURE_SEGMENT_PATTERN = re.compile(r"[A-Za-z0-9_.-]+")
FIGURE_FILE_PATTERN = re.compile(r"[A-Za-z0-9_-]+\.png")
FIGURE_WIDTH = r"0.92\linewidth"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# Characters that work everywhere: each is declared as
# \DeclareUnicodeCharacter{XXXX}{\ensuremath{<code>}} and replaced by <code>
# inside math.  Keys follow the unicode-math conventions (U+03B5 is
# \varepsilon, U+03F5 is \epsilon, U+03C6 is \varphi, U+03D5 is \phi).
MATH_CHARACTERS: dict[str, str] = {
    # Greek small letters and variants
    "α": r"\alpha",
    "β": r"\beta",
    "γ": r"\gamma",
    "δ": r"\delta",
    "ε": r"\varepsilon",
    "ζ": r"\zeta",
    "η": r"\eta",
    "θ": r"\theta",
    "ι": r"\iota",
    "κ": r"\kappa",
    "λ": r"\lambda",
    "μ": r"\mu",
    "ν": r"\nu",
    "ξ": r"\xi",
    "ο": "o",
    "π": r"\pi",
    "ρ": r"\rho",
    "ς": r"\varsigma",
    "σ": r"\sigma",
    "τ": r"\tau",
    "υ": r"\upsilon",
    "φ": r"\varphi",
    "χ": r"\chi",
    "ψ": r"\psi",
    "ω": r"\omega",
    "ϑ": r"\vartheta",
    "ϕ": r"\phi",
    "ϖ": r"\varpi",
    "ϰ": r"\varkappa",
    "ϱ": r"\varrho",
    "ϵ": r"\epsilon",
    "µ": r"\mu",
    # Greek capital letters
    "Α": r"\mathrm{A}",
    "Β": r"\mathrm{B}",
    "Γ": r"\Gamma",
    "Δ": r"\Delta",
    "Ε": r"\mathrm{E}",
    "Ζ": r"\mathrm{Z}",
    "Η": r"\mathrm{H}",
    "Θ": r"\Theta",
    "Ι": r"\mathrm{I}",
    "Κ": r"\mathrm{K}",
    "Λ": r"\Lambda",
    "Μ": r"\mathrm{M}",
    "Ν": r"\mathrm{N}",
    "Ξ": r"\Xi",
    "Ο": r"\mathrm{O}",
    "Π": r"\Pi",
    "Ρ": r"\mathrm{P}",
    "Σ": r"\Sigma",
    "Τ": r"\mathrm{T}",
    "Υ": r"\Upsilon",
    "Φ": r"\Phi",
    "Χ": r"\mathrm{X}",
    "Ψ": r"\Psi",
    "Ω": r"\Omega",
    # calculus and algebra
    "∂": r"\partial",
    "∇": r"\nabla",
    "√": r"\surd",
    "∞": r"\infty",
    "±": r"\pm",
    "∓": r"\mp",
    "×": r"\times",
    "÷": r"\div",
    "·": r"\cdot",
    "⋅": r"\cdot",
    "∘": r"\circ",
    "∗": r"\ast",
    "−": "-",
    "∑": r"\sum",
    "∏": r"\prod",
    "∫": r"\int",
    "∮": r"\oint",
    "⊕": r"\oplus",
    "⊗": r"\otimes",
    "⊖": r"\ominus",
    "⊙": r"\odot",
    "⋊": r"\rtimes",
    "⋉": r"\ltimes",
    "†": r"\dagger",
    "‡": r"\ddagger",
    "ℏ": r"\hbar",
    "ℓ": r"\ell",
    "⟨": r"\langle",
    "⟩": r"\rangle",
    "‖": r"\Vert",
    "∣": r"\mid",
    "⊥": r"\perp",
    "∥": r"\parallel",
    "⋯": r"\cdots",
    "⋮": r"\vdots",
    "□": r"\square",
    "′": r"^{\prime}",
    "″": r"^{\prime\prime}",
    "°": r"^{\circ}",
    # relations
    "≤": r"\leq",
    "≥": r"\geq",
    "≠": r"\neq",
    "≈": r"\approx",
    "≡": r"\equiv",
    "∼": r"\sim",
    "≃": r"\simeq",
    "≅": r"\cong",
    "∝": r"\propto",
    "≪": r"\ll",
    "≫": r"\gg",
    "≔": r"\coloneqq",
    # arrows
    "→": r"\to",
    "←": r"\leftarrow",
    "↔": r"\leftrightarrow",
    "⇒": r"\Rightarrow",
    "⇐": r"\Leftarrow",
    "⇔": r"\Leftrightarrow",
    "↦": r"\mapsto",
    "⟶": r"\longrightarrow",
    "↪": r"\hookrightarrow",
    # sets and logic
    "∈": r"\in",
    "∉": r"\notin",
    "∋": r"\ni",
    "⊂": r"\subset",
    "⊆": r"\subseteq",
    "⊃": r"\supset",
    "⊇": r"\supseteq",
    "∪": r"\cup",
    "∩": r"\cap",
    "∖": r"\setminus",
    "∅": r"\emptyset",
    "∀": r"\forall",
    "∃": r"\exists",
    "¬": r"\neg",
    "∧": r"\wedge",
    "∨": r"\vee",
    "ℝ": r"\mathbb{R}",
    "ℂ": r"\mathbb{C}",
    "ℤ": r"\mathbb{Z}",
    "ℕ": r"\mathbb{N}",
    "ℚ": r"\mathbb{Q}",
    "ℍ": r"\mathbb{H}",
    # superscripts and subscripts
    "⁰": "^{0}",
    "¹": "^{1}",
    "²": "^{2}",
    "³": "^{3}",
    "⁴": "^{4}",
    "⁵": "^{5}",
    "⁶": "^{6}",
    "⁷": "^{7}",
    "⁸": "^{8}",
    "⁹": "^{9}",
    "⁺": "^{+}",
    "⁻": "^{-}",
    "ⁿ": "^{n}",
    "₀": "_{0}",
    "₁": "_{1}",
    "₂": "_{2}",
    "₃": "_{3}",
    "₄": "_{4}",
    "₅": "_{5}",
    "₆": "_{6}",
    "₇": "_{7}",
    "₈": "_{8}",
    "₉": "_{9}",
    "₊": "_{+}",
    "₋": "_{-}",
}

# Characters that the T1 font encoding and the utf8 input encoding typeset
# natively in text (not in math).  They pass through unchanged.
TEXT_CHARACTERS = frozenset(
    "\u00a0"  # no-break space
    "¡§©«®»¿"
    "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
    "àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
    "ĀāĂăĄąĆćČčĎďĐđĒēĘęĚěĞğĪīİıĹĺĽľŁłŃńŇňŌōŐőŒœŔŕŘřŚśŞşŠšŢţŤťŪūŮůŰűŸŹźŻżŽž"
    "‘’“”–—…•"
)

TEXT_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "“": "``",
    "”": "''",
    "–": "--",
    "—": "---",
}

CODE_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "$": r"\$",
}

URL_PATTERN = re.compile(r"[A-Za-z0-9\-._~:/?#@!$&'()*+,;=%]+")
PERCENT_PATTERN = re.compile(r"%(?![0-9A-Fa-f]{2})")

# Reverse map used only for PDF-bookmark text of math in headings.
BOOKMARK_COMMANDS: dict[str, str] = {}
for _character, _code in MATH_CHARACTERS.items():
    if re.fullmatch(r"\\[A-Za-z]+", _code):
        BOOKMARK_COMMANDS.setdefault(_code[1:], _character)
BOOKMARK_COMMANDS.update(
    {
        "le": "≤",
        "ge": "≥",
        "ne": "≠",
        "sqrt": "√",
        "dots": "…",
        "ldots": "…",
        "rightarrow": "→",
    }
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument(
        "--output",
        type=Path,
        help="Output .tex path (default: the input path with suffix .tex).",
    )
    parser.add_argument(
        "--strip-heading-numbers",
        action="store_true",
        help=(
            "Remove authored numeric prefixes before LaTeX adds "
            "section numbers."
        ),
    )
    parser.add_argument(
        "--developer-layout",
        action="store_true",
        help=(
            "Use compact ragged tables and breakable long code spans for "
            "the repository-wide Developer Summary."
        ),
    )
    parser.add_argument("--author", default=DEFAULT_AUTHOR)
    parser.add_argument("--date", default=DEFAULT_DATE)
    parser.add_argument(
        "--image-root",
        type=Path,
        default=REPOSITORY_ROOT,
        help=(
            "Directory that figure paths are relative to and checked "
            "against (default: the repository containing this script); "
            "pdflatex must run with it as working directory."
        ),
    )
    return parser.parse_args()


def describe_character(character: str) -> str:
    name = unicodedata.name(character, "UNNAMED")
    return f"U+{ord(character):04X} {name}"


def validate_characters(text: str, label: str) -> None:
    """Reject every non-ASCII character that has no vetted rendering."""
    for line_number, line in enumerate(text.splitlines() or [text], 1):
        for character in line:
            if (
                ord(character) > 127
                and character not in MATH_CHARACTERS
                and character not in TEXT_CHARACTERS
            ):
                raise ValueError(
                    f"{label} line {line_number}: unsupported non-ASCII "
                    f"character {describe_character(character)}; write it "
                    "as LaTeX math (for example $\\psi$) or add it to "
                    "MATH_CHARACTERS"
                )


def unicode_declarations(text: str) -> list[str]:
    used = sorted(
        {character for character in text if character in MATH_CHARACTERS}
    )
    return [
        f"\\DeclareUnicodeCharacter{{{ord(character):04X}}}"
        f"{{\\ensuremath{{{MATH_CHARACTERS[character]}}}}}"
        for character in used
    ]


def math_markup(value: str) -> str:
    """Replace Unicode math characters by LaTeX commands inside math."""
    if all(ord(character) < 128 for character in value):
        return value
    result: list[str] = []
    for character in value:
        code = MATH_CHARACTERS.get(character)
        if code is None:
            result.append(character)
        elif re.fullmatch(r"\\[A-Za-z]+", code):
            result.append(code + " ")
        elif code.startswith("\\"):
            result.append("{" + code + "}")
        else:
            result.append(code)
    return "".join(result)


def escape_text(value: str) -> str:
    return "".join(
        TEXT_REPLACEMENTS.get(character, character) for character in value
    )


def escape_code(value: str) -> str:
    return "".join(
        CODE_REPLACEMENTS.get(character, character) for character in value
    )


def braces_balanced(value: str) -> bool:
    depth = 0
    for character in value:
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def render_code(
    value: str, break_long_code: bool, moving: bool = False
) -> str:
    """Typewriter code span.

    moving=True marks a heading: its text is written to the .toc file, where
    the expansion of \\detokenize{...} is re-read with normal catcodes, so
    _ ^ $ & ~ and braces must be escaped there as well.
    """
    unsafe_for_detokenize = (
        any(character in value for character in "#%\\")
        or not braces_balanced(value)
        or any(ord(character) > 127 for character in value)
        or (moving and any(character in value for character in "_^$&~{}"))
    )
    if not break_long_code or len(value) <= 8:
        if unsafe_for_detokenize:
            return r"\texttt{" + escape_code(value) + "}"
        return r"\texttt{\detokenize{" + value + "}}"
    chunks = [value[index:index + 8] for index in range(0, len(value), 8)]
    return (
        r"\texttt{"
        + r"\allowbreak{}".join(
            escape_text(chunk).replace("$", r"\$") for chunk in chunks
        )
        + "}"
    )


def validate_url(url: str) -> str:
    if not url:
        raise ValueError("empty link target in Markdown link")
    if not URL_PATTERN.fullmatch(url):
        bad = sorted({c for c in url if not URL_PATTERN.fullmatch(c)})
        raise ValueError(
            f"link target {url!r} contains characters outside the "
            f"supported ASCII URL set: {bad!r} (percent-encode them)"
        )
    if PERCENT_PATTERN.search(url):
        raise ValueError(
            f"link target {url!r} contains a '%' that does not start a "
            "percent-encoded octet"
        )
    return url.replace("#", r"\#").replace("%", r"\%").replace("&", r"\&")


def parse_link(value: str, index: int) -> tuple[str, str, int] | None:
    """Return (text, url, end) for a Markdown link starting at index."""
    close = value.find("]", index + 1)
    if close < 0 or not value.startswith("](", close):
        return None
    text = value[index + 1:close]
    if "[" in text:
        return None
    depth = 0
    position = close + 2
    while position < len(value):
        character = value[position]
        if character == "(":
            depth += 1
        elif character == ")":
            if depth == 0:
                return text, value[close + 2:position], position + 1
            depth -= 1
        position += 1
    return None


def math_bookmark(math_source: str) -> str:
    """Plain-text approximation of inline math for PDF bookmarks."""
    body = math_source.strip("$")
    body = re.sub(r"\\[,;:! ]", " ", body)

    def command(match: re.Match[str]) -> str:
        return BOOKMARK_COMMANDS.get(match.group(1), "")

    body = re.sub(r"\\([A-Za-z]+)\s*", command, body)
    body = re.sub(r"(?<!\\)[{}]", "", body)
    body = re.sub(r"\\([{}|])", r"\1", body)
    body = body.replace("\\", " ").replace("~", " ")
    body = re.sub(r"\s+", " ", body).strip()
    return escape_text(body)


def inline_markup(
    value: str, break_long_code: bool = False, heading: bool = False
) -> str:
    result: list[str] = []
    index = 0
    while index < len(value):
        if value.startswith("**", index):
            end = value.find("**", index + 2)
            if end >= 0:
                result.append(
                    r"\textbf{"
                    + inline_markup(
                        value[index + 2:end], break_long_code, heading
                    )
                    + "}"
                )
                index = end + 2
                continue
        if value[index] == "*":
            end = value.find("*", index + 1)
            if end >= 0:
                result.append(
                    r"\emph{"
                    + inline_markup(
                        value[index + 1:end], break_long_code, heading
                    )
                    + "}"
                )
                index = end + 1
                continue
        if value[index] == "`":
            end = value.find("`", index + 1)
            if end >= 0:
                result.append(
                    render_code(
                        value[index + 1:end], break_long_code, moving=heading
                    )
                )
                index = end + 1
                continue
        if value[index] == "$":
            end = value.find("$", index + 1)
            if end >= 0:
                math = math_markup(value[index:end + 1])
                if heading:
                    math = (
                        r"\texorpdfstring{"
                        + math
                        + "}{"
                        + math_bookmark(value[index:end + 1])
                        + "}"
                    )
                result.append(math)
                index = end + 1
                continue
        if value[index] == "[":
            link = parse_link(value, index)
            if link is not None and index > 0 and value[index - 1] == "!":
                raise ValueError(
                    "Markdown images are not supported inside a paragraph, "
                    "list item, table cell, heading or caption: "
                    f"{value[index - 1:link[2]]!r} (a figure is a line "
                    "that holds nothing but ![caption](path.png))"
                )
            if link is not None:
                text, url, end = link
                rendered = (
                    r"\href{"
                    + validate_url(url)
                    + "}{"
                    + inline_markup(text, break_long_code)
                    + "}"
                )
                if heading:
                    rendered = (
                        r"\texorpdfstring{"
                        + rendered
                        + "}{"
                        + inline_markup(text, break_long_code, heading)
                        + "}"
                    )
                result.append(rendered)
                index = end
                continue
        next_special = min(
            [
                position
                for position in (
                    value.find("**", index),
                    value.find("*", index),
                    value.find("`", index),
                    value.find("$", index),
                    value.find("[", index),
                )
                if position >= 0
            ]
            or [len(value)]
        )
        if next_special == index:
            result.append(escape_text(value[index]))
            index += 1
        else:
            result.append(escape_text(value[index:next_special]))
            index = next_special
    return "".join(result)


def guard_leading_bracket(latex: str) -> str:
    r"""Stop \item, or the \\ ending the previous row, reading [ or * ."""
    if latex.startswith(("[", "*")):
        return "{}" + latex
    return latex


def figure_line(stripped: str) -> tuple[str, str] | None:
    """Return (caption, path) when the stripped line is one image only.

    The caption ends at the "]" that balances the "![" (so it may contain
    a [link](url)); it must be followed directly by "(" and the path, which
    runs to the ")" that ends the line and contains no parenthesis.
    """
    if not (stripped.startswith("![") and stripped.endswith(")")):
        return None
    depth = 0
    for position in range(2, len(stripped)):
        character = stripped[position]
        if character == "[":
            depth += 1
        elif character == "]":
            if depth == 0:
                break
            depth -= 1
    else:
        return None
    if not stripped.startswith("](", position):
        return None
    path = stripped[position + 2:-1]
    if "(" in path or ")" in path:
        return None
    return stripped[2:position].strip(), path


def validate_figure_path(path: str, line_number: int) -> None:
    """Accept only a portable PNG path relative to the repository root."""
    segments = path.split("/")
    problem = None
    if not path:
        problem = "is empty"
    elif path.startswith("/"):
        problem = "is absolute (write it relative to the repository root)"
    elif any(not FIGURE_SEGMENT_PATTERN.fullmatch(s) for s in segments):
        problem = (
            "may contain only ASCII letters, digits, '-', '_' and '.' in "
            "'/'-separated segments (no spaces, backslashes or drive letters)"
        )
    elif any(set(segment) == {"."} for segment in segments):
        problem = "must not contain '.' or '..' segments"
    elif not FIGURE_FILE_PATTERN.fullmatch(segments[-1]):
        problem = (
            "must end in a file name NAME.png with exactly one dot "
            "(only PNG figures are supported)"
        )
    if problem is not None:
        raise ValueError(f"line {line_number}: figure path {path!r} {problem}")


def check_figure_file(path: str, image_root: Path, line_number: int) -> None:
    """Require an existing PNG at image_root/path, with exact spelling."""
    root = Path(image_root).resolve()
    directory = root
    for segment in path.split("/"):
        try:
            names = os.listdir(directory)
        except OSError:
            names = []
        if segment not in names:
            raise ValueError(
                f"line {line_number}: figure file {path!r} does not exist "
                f"under {root.as_posix()} (spelled with this exact case)"
            )
        directory = directory / segment
    if not directory.is_file():
        raise ValueError(
            f"line {line_number}: figure path {path!r} is not a file"
        )
    try:
        directory.resolve().relative_to(root)
    except ValueError:
        raise ValueError(
            f"line {line_number}: figure path {path!r} leaves "
            f"{root.as_posix()} through a link"
        ) from None
    with directory.open("rb") as handle:
        signature = handle.read(len(PNG_SIGNATURE))
    if signature != PNG_SIGNATURE:
        raise ValueError(
            f"line {line_number}: figure file {path!r} is not a PNG file"
        )


def figure_paths(markdown: str) -> list[str]:
    """Paths of the figure lines of markdown, in order, as convert() sees
    them (fenced code and display math are skipped; nothing is validated)."""
    paths = []
    in_code = False
    in_math = False
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
        elif in_code:
            continue
        elif stripped == "$$":
            in_math = not in_math
        elif not in_math:
            figure = figure_line(stripped)
            if figure is not None:
                paths.append(figure[1])
    return paths


def render_figure(
    caption: str, path: str, developer_layout: bool
) -> list[str]:
    return [
        "\\begin{figure}[htbp]",
        "\\centering",
        f"\\includegraphics[width={FIGURE_WIDTH}]{{{path}}}",
        "\\caption{"
        + inline_markup(caption, developer_layout, heading=True)
        + "}",
        "\\end{figure}",
    ]


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(
        re.fullmatch(r":?-{3,}:?", cell) for cell in cells
    )


def render_table(
    lines: list[str], developer_layout: bool = False
) -> list[str]:
    rows = [
        [
            inline_markup(cell.strip(), developer_layout)
            for cell in line.strip().strip("|").split("|")
        ]
        for line in lines
        if not is_table_separator(line)
    ]
    columns = len(rows[0])
    width = (0.80 if developer_layout else 0.92) / columns
    column_type = (
        f">{{\\raggedright\\arraybackslash}}p{{{width:.3f}\\linewidth}}"
        if developer_layout
        else f"p{{{width:.3f}\\linewidth}}"
    )
    specification = "@{}" + column_type * columns + "@{}"
    output = []
    if developer_layout:
        output.extend(["\\begingroup", "\\small"])
    output.extend([f"\\begin{{longtable}}{{{specification}}}", "\\toprule"])
    header = " & ".join(
        r"\textbf{" + cell + "}" for cell in rows[0]
    ) + r" \\"
    output.append(header)
    output.append("\\midrule")
    output.append("\\endfirsthead")
    output.append("\\toprule")
    output.append(header)
    output.append("\\midrule")
    output.append("\\endhead")
    for row in rows[1:]:
        output.append(guard_leading_bracket(" & ".join(row)) + r" \\")
    output.extend(["\\bottomrule", "\\end{longtable}"])
    if developer_layout:
        output.append("\\endgroup")
    return output


def validate_table(lines: list[str], first_line_number: int) -> None:
    expected = len(split_table_row(lines[0]))
    for offset, line in enumerate(lines):
        count = len(split_table_row(line))
        if count != expected:
            raise ValueError(
                f"line {first_line_number + offset}: table row has {count} "
                f"cells but the header has {expected}"
            )


def document_metadata(lines: list[str]) -> tuple[str, str, int, int]:
    title_index = next(
        (
            index
            for index, line in enumerate(lines)
            if re.match(r"^#\s+\S", line.strip())
        ),
        None,
    )
    if title_index is None:
        raise ValueError("Dissertation Markdown must contain an H1 title")
    subtitle_index = next(
        (
            index
            for index in range(title_index + 1, len(lines))
            if re.match(r"^##\s+\S", lines[index].strip())
        ),
        None,
    )
    if subtitle_index is None:
        raise ValueError("Dissertation Markdown must contain an H2 subtitle")
    title = lines[title_index].strip()[2:].strip()
    subtitle = lines[subtitle_index].strip()[3:].strip()
    return title, subtitle, title_index, subtitle_index


def convert(
    markdown: str,
    strip_heading_numbers: bool = False,
    developer_layout: bool = False,
    author: str = DEFAULT_AUTHOR,
    date: str = DEFAULT_DATE,
    image_root: Path | None = None,
) -> str:
    """Return the LaTeX document for markdown.

    image_root: when given, every figure file is also checked on disk
    (check_figure_file); figure paths are relative to it.
    """
    validate_characters(markdown, "Markdown")
    validate_characters(author, "author")
    validate_characters(date, "date")
    lines = markdown.splitlines()
    title, subtitle, title_index, subtitle_index = document_metadata(lines)
    body: list[str] = []
    paragraph: list[str] = []
    in_math = False
    in_code = False
    in_abstract = False
    block_start = 0
    list_kind: str | None = None
    figure_count = 0
    index = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            body.append(
                inline_markup(
                    " ".join(line.strip() for line in paragraph),
                    developer_layout,
                )
            )
            body.append("")
            paragraph = []

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            body.append(f"\\end{{{list_kind}}}")
            body.append("")
            list_kind = None

    def heading_markup(text: str) -> str:
        return inline_markup(text, developer_layout, heading=True)

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                body.extend(["\\end{Verbatim}", ""])
            else:
                body.append("\\begin{Verbatim}[fontsize=\\small]")
                block_start = index + 1
            in_code = not in_code
            index += 1
            continue
        if in_code:
            if "\t" in line:
                raise ValueError(
                    f"line {index + 1}: fenced code contains a tab"
                )
            if len(line) > MAX_CODE_LINE_LENGTH:
                raise ValueError(
                    f"line {index + 1}: fenced code line has {len(line)} "
                    f"characters; the limit is {MAX_CODE_LINE_LENGTH}"
                )
            body.append(line)
            index += 1
            continue
        if stripped == "$$":
            flush_paragraph()
            close_list()
            body.append("\\[" if not in_math else "\\]")
            if in_math:
                body.append("")
            else:
                block_start = index + 1
            in_math = not in_math
            index += 1
            continue
        if in_math:
            body.append(math_markup(line))
            index += 1
            continue
        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and is_table_separator(lines[index + 1])
        ):
            flush_paragraph()
            close_list()
            first_line_number = index + 1
            table_lines = [line, lines[index + 1]]
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            validate_table(table_lines, first_line_number)
            body.extend(render_table(table_lines, developer_layout))
            body.append("")
            continue
        figure = figure_line(stripped)
        if figure is not None:
            flush_paragraph()
            close_list()
            caption, path = figure
            if not caption:
                raise ValueError(
                    f"line {index + 1}: figure {stripped!r} has an empty "
                    "caption"
                )
            validate_figure_path(path, index + 1)
            if image_root is not None:
                check_figure_file(path, image_root, index + 1)
            body.extend(render_figure(caption, path, developer_layout))
            body.append("")
            figure_count += 1
            index += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            text = heading.group(2)
            if in_abstract:
                body.extend(["\\end{abstract}", ""])
                in_abstract = False
            if index in {title_index, subtitle_index}:
                index += 1
                continue
            if strip_heading_numbers:
                text = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", text)
            if text == "Abstract":
                body.append("\\begin{abstract}")
                in_abstract = True
            elif level == 2:
                body.extend([f"\\section{{{heading_markup(text)}}}", ""])
            elif level == 3:
                body.extend([f"\\subsection{{{heading_markup(text)}}}", ""])
            else:
                body.extend(
                    [f"\\subsubsection{{{heading_markup(text)}}}", ""]
                )
            index += 1
            continue
        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        unordered = re.match(r"^-\s+(.+)$", stripped)
        if ordered or unordered:
            flush_paragraph()
            wanted = "enumerate" if ordered else "itemize"
            if list_kind != wanted:
                close_list()
                body.append(f"\\begin{{{wanted}}}")
                list_kind = wanted
            body.append(
                "\\item "
                + guard_leading_bracket(
                    inline_markup(
                        (ordered or unordered).group(1), developer_layout
                    )
                )
            )
            index += 1
            continue
        if not stripped:
            flush_paragraph()
            close_list()
            index += 1
            continue
        paragraph.append(line)
        index += 1

    if in_code:
        raise ValueError(f"line {block_start}: fenced code is not closed")
    if in_math:
        raise ValueError(f"line {block_start}: display math is not closed")
    flush_paragraph()
    close_list()
    if in_abstract:
        body.append("\\end{abstract}")

    latex_title = (
        f"{chr(92)}title{{{inline_markup(title, developer_layout)}"
        f"{chr(92) * 2}[0.5em]\\large "
        f"{inline_markup(subtitle, developer_layout)}}}"
    )
    declarations = unicode_declarations(markdown + author + date)
    declaration_block = "".join(line + "\n" for line in declarations)
    # Only a document with a figure loads graphicx: the preamble of every
    # other document stays byte-identical to the origin's.
    graphics_block = "\\usepackage{graphicx}\n" if figure_count else ""
    preamble = rf"""\documentclass[11pt]{{article}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{lmodern}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{amsmath,amssymb,mathtools}}
\usepackage{{booktabs,longtable,array}}
\usepackage{{fancyvrb}}
{graphics_block}\usepackage[hidelinks]{{hyperref}}
\usepackage{{microtype}}
{declaration_block}\pdfobjcompresslevel=0
\pdfinfoomitdate=1
\pdftrailerid{{}}
\pdfsuppressptexinfo=15
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.65em}}
\setlength{{\emergencystretch}}{{3em}}
{latex_title}
\author{{{inline_markup(author, developer_layout)}}}
\date{{{inline_markup(date, developer_layout)}}}
\begin{{document}}
\maketitle
\tableofcontents
\newpage
"""
    return preamble + "\n".join(body) + "\n\\end{document}\n"


def main() -> int:
    arguments = parse_arguments()
    input_path = arguments.input.resolve()
    output_path = (
        arguments.output or arguments.input.with_suffix(".tex")
    ).resolve()
    latex = convert(
        input_path.read_text(encoding="utf-8"),
        strip_heading_numbers=arguments.strip_heading_numbers,
        developer_layout=arguments.developer_layout,
        author=arguments.author,
        date=arguments.date,
        image_root=arguments.image_root,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(latex, encoding="utf-8", newline="\n")
    print(f"input={input_path}")
    print(f"output={output_path}")
    print(f"output_bytes={output_path.stat().st_size}")
    print(
        "output_sha256="
        + hashlib.sha256(output_path.read_bytes()).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
