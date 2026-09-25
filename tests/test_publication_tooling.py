# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests of the publication tooling.

Covers scripts/build_dissertation_tex.py (determinism, backward
compatibility with the dirac-main origin, Greek and symbol handling, links,
tables, structural validation), scripts/check_provenance_pdf.py (the JSON
edition registry), scripts/check_dissertation_pdf.py (rejection of mutated
PDF bytes) and scripts/build_provenance_pdf.py (register and verify modes,
warning scan).  Tests that compile LaTeX are skipped when pdflatex is absent.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_dissertation_tex as builder  # noqa: E402
from scripts import build_provenance_pdf  # noqa: E402
from scripts import check_dissertation_pdf  # noqa: E402
from scripts import check_provenance_pdf  # noqa: E402

SCRIPTS = REPOSITORY_ROOT / "scripts"
DIRAC_MAIN = REPOSITORY_ROOT / "dirac-main"


def find_pdflatex() -> str | None:
    found = shutil.which("pdflatex")
    if found:
        return found
    fallback = build_provenance_pdf.PDFLATEX_FALLBACK
    return str(fallback) if fallback.exists() else None


PDFLATEX = find_pdflatex()

# (stem, strip_heading_numbers, developer_layout, markdown sha256, tex sha256)
# of the eight dirac-main documents whose committed .tex the origin builder
# produced; the extended builder must reproduce every one byte for byte.
DIRAC_MAIN_GOLDEN = (
    (
        "dissertation/dirac-triality", False, False,
        "44b76c2d872598ad1b038a8d4ad1293b18885ab228297c921579daa86eeb1381",
        "12df60627b5f11b09ccbbadd9ca38fd2ce7efcfccd769f69fd8280b78a6cec38",
    ),
    (
        "dissertation/Learn_dirac-triality", True, False,
        "ab6c653f6d0f2355411d61c9357d3c709ced8b9ac70167861e893a9029052676",
        "533eeaef0619d3b590d74fa03a4a81aaa76163fce289d659a1007d1b10b0e03e",
    ),
    (
        "provenance/CURVED_SPIN_BUNDLE", True, False,
        "83bb78934b9b4986d8ae755319d9fb654e1c68dfc5f05ab6217839689e4184f7",
        "55b94966a83b007c37543a6875210a83594165efad024f3e52571d7d4370469c",
    ),
    (
        "provenance/EINSTEIN_SPINOR_44", True, False,
        "0a38c49921735b27dc82e72acb8fa69ecb7f5e79c08d195a690dd00049c6fc5e",
        "58d55a27362add0a73b35e5561b0500c0a2fbfe20cd17a5891c789aee5877c6c",
    ),
    (
        "provenance/EINSTEIN_SPINOR_44_COMPONENTS_X0_X7", True, False,
        "aba76aabc2fce453aa1214b4b580555aa04045649279df2c9f796a27d3994502",
        "4249ed227b8b4ed1c6ad7b8ec9f4b122fc296f7f17e729c274f49b7914d802ee",
    ),
    (
        "provenance/EINSTEIN_SPINOR_44_NUMERICS_X0_X7", True, False,
        "1ea9958088af5044f8ceea67e44c1b3b634e581e0902c26c1f364f9efa9e8f49",
        "8465df163fb255c8b091365d543c604e6692d8b114921241e6cac5b39eb3a054",
    ),
    (
        "provenance/WEITZENBOCK_SPINOR_44", True, False,
        "cdffe26dd1d3bc67a656769d7defb2eb991da6cc34231bfad4d55876e98ee7fc",
        "735576ec52eb30477a6d1dc15ed5e0109ee47bafd389871075256554237046d0",
    ),
    (
        "DEVELOPER_SUMMARY", True, True,
        "ad56d4a4ab86326c4923228e4e84a102b92aecc874969e3083cbd9f2e7db8010",
        "ffa17fcf780cbe08e6104c23a840d6ce91e833272b884c01f6ee86a87360fe2b",
    ),
)

# A document of the origin's Markdown subset, and the sha256 of the ORIGIN
# builder's output for it (computed with dirac-main's
# scripts/build_dissertation_tex.py on 2026-09-25) for the three flag sets.
OLD_SUBSET_MARKDOWN = (
    "# Old subset title\n"
    "\n"
    "## Old subset subtitle\n"
    "\n"
    "### Abstract\n"
    "\n"
    "An abstract with **bold**, *emphasis*, `code_span^2`, $x^2$ and\n"
    "Weitzenb\u00f6ck \u201cquotes\u201d \u2013 dash.\n"
    "\n"
    "## 1. First section\n"
    "\n"
    "Text with 50% & #hash and_under {braces} ~tilde^caret.\n"
    "\n"
    "$$\n"
    "\\begin{aligned}\n"
    "a &= b,\\\\\n"
    "c &= d.\n"
    "\\end{aligned}\n"
    "$$\n"
    "\n"
    "### 1.1 A table\n"
    "\n"
    "| Name | Value |\n"
    "| --- | ---: |\n"
    "| `alpha` | $\\alpha$ |\n"
    "| beta | **2** |\n"
    "\n"
    "#### 1.1.1 Lists\n"
    "\n"
    "- first\n"
    "- second with `code`\n"
    "\n"
    "1. one\n"
    "2. two\n"
    "\n"
    "```text\n"
    "verbatim {braces} 100% #x\n"
    "```\n"
)
OLD_SUBSET_ORIGIN_SHA256 = {
    (False, False): (
        "0d341435550879032d38117803a7f16685acf6fff9647209627b75e6053ac79f"
    ),
    (True, False): (
        "6d8b874e6164dc481cd6f9611fcc23b13bfd1d1cb0564cc9169b36fc236c39d3"
    ),
    (True, True): (
        "c5d78c5aa98bfe9519a5feecc002bd8d3b905e0a2588d53225dc54caefb9336f"
    ),
}

# Exercises every extension; compiles warning-free (see PdfTests).
FEATURE_MARKDOWN = "\n".join(
    [
        "# Feature test for Ψ",
        "",
        "## Every extension of the Markdown subset",
        "",
        "### Abstract",
        "",
        "The field Ψ with $\\bar\\Psi = Ψ^† C$ and η = diag(+1, −1).",
        "",
        "## 1. Greek, symbols and $\\Omega_\\mu$ in a heading",
        "",
        "Prose: α, β, γ, ∂, ∇, ×, ≤, →, ⊕, ℝ, x², x₀ and Weitzenböck.",
        "Math: $Ψ^† γ^a ∂_μ Ψ$ and $α × β ≤ γ$.",
        "",
        "### 1.1 A [heading link](https://example.org/h)",
        "",
        "Links: [dirac](https://github.com/once-ere/dirac),"
        " [query](https://example.org/s?x=1&y=2#top),"
        " [percent](https://example.org/a%20b),"
        " **[bold](https://example.org/b)** and [1] without a target.",
        "",
        "## 2. Display math",
        "",
        "$$",
        "\\begin{aligned}",
        "Ω_μ &= \\tfrac12 ω_{μab} S^{ab},\\\\",
        "D_μ Ψ &= ∂_μ Ψ + Ω_μ Ψ .",
        "\\end{aligned}",
        "$$",
        "",
        "## 3. Table and lists",
        "",
        "| Quantity | Symbol | Note |",
        "| --- | --- | --- |",
        "| metric | $\\eta_{ab}$ | [link](https://example.org/t) |",
        "| [bracket] | γ⁸ | `a#b%c\\d{` |",
        "",
        "- [a link first](https://example.org/l)",
        "- [bracket] first",
        "",
        "## 4. Code",
        "",
        "Inline `Ψ_a` and `C:\\Users`.",
        "",
        "```text",
        "x" * builder.MAX_CODE_LINE_LENGTH,
        "{Ψ_a, Ψ_b^†} = B_ab δ^7(x-y)/√|g|   # 100% & more",
        "```",
        "",
    ]
)


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def minimal(body: str) -> str:
    return "# Title\n\n## Subtitle\n\n" + body


def body_of(latex: str) -> str:
    return latex.split("\\newpage\n", 1)[1]


class ConvertDeterminismTests(unittest.TestCase):
    def test_repeated_conversion_is_identical(self) -> None:
        first = builder.convert(FEATURE_MARKDOWN, True, False)
        second = builder.convert(FEATURE_MARKDOWN, True, False)
        self.assertEqual(first, second)

    def test_cli_output_is_independent_of_hash_seed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "doc.md"
            source.write_bytes(FEATURE_MARKDOWN.encode("utf-8"))
            outputs = []
            for seed in ("0", "1", "4242"):
                target = Path(directory) / f"doc-{seed}.tex"
                completed = subprocess.run(
                    [
                        sys.executable,
                        str(SCRIPTS / "build_dissertation_tex.py"),
                        "--strip-heading-numbers",
                        "--input",
                        str(source),
                        "--output",
                        str(target),
                    ],
                    env=dict(os.environ, PYTHONHASHSEED=seed),
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                outputs.append(target.read_bytes())
        self.assertEqual(len(set(outputs)), 1)
        content = outputs[0]
        self.assertNotIn(b"\r", content)
        self.assertTrue(content.endswith(b"\n"))
        self.assertEqual(
            content,
            builder.convert(FEATURE_MARKDOWN, True).encode("utf-8"),
        )

    def test_determinism_primitives_are_kept(self) -> None:
        latex = builder.convert(FEATURE_MARKDOWN)
        for primitive in (
            "\\pdfobjcompresslevel=0\n",
            "\\pdfinfoomitdate=1\n",
            "\\pdftrailerid{}\n",
            "\\pdfsuppressptexinfo=15\n",
        ):
            self.assertIn(primitive, latex)

    def test_positional_signature_and_default_author_and_date(self) -> None:
        latex = builder.convert(minimal("Text.\n"), True, False)
        self.assertIn(
            "\\author{dirac16complex project (with Claude Opus 5.5)}", latex
        )
        self.assertIn("\\date{September 2026}", latex)
        self.assertEqual(
            builder.DEFAULT_AUTHOR,
            "dirac16complex project (with Claude Opus 5.5)",
        )
        self.assertEqual(builder.DEFAULT_DATE, "September 2026")

    def test_author_and_date_are_escaped_and_may_use_greek(self) -> None:
        latex = builder.convert(
            minimal("Text.\n"), author="A & B_ψ", date="1 October 2026"
        )
        self.assertIn("\\author{A \\& B\\_ψ}", latex)
        self.assertIn("\\date{1 October 2026}", latex)
        self.assertIn(
            "\\DeclareUnicodeCharacter{03C8}{\\ensuremath{\\psi}}", latex
        )

    def test_cli_author_and_date_options(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "doc.md"
            source.write_bytes(minimal("Text.\n").encode("utf-8"))
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "build_dissertation_tex.py"),
                    "--input",
                    str(source),
                    "--author",
                    "Someone Else",
                    "--date",
                    "May 2027",
                ],
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            latex = source.with_suffix(".tex").read_text(encoding="utf-8")
        self.assertIn("\\author{Someone Else}", latex)
        self.assertIn("\\date{May 2027}", latex)

    def test_old_subset_output_equals_the_origin_builder(self) -> None:
        for flags, expected in OLD_SUBSET_ORIGIN_SHA256.items():
            with self.subTest(flags=flags):
                latex = builder.convert(
                    OLD_SUBSET_MARKDOWN,
                    *flags,
                    author=builder.ORIGIN_AUTHOR,
                )
                self.assertEqual(sha256(latex.encode("utf-8")), expected)
                self.assertNotIn("DeclareUnicodeCharacter", latex)
                self.assertNotIn("texorpdfstring", latex)

    @unittest.skipUnless(DIRAC_MAIN.is_dir(), "dirac-main reference absent")
    def test_dirac_main_documents_are_reproduced_byte_for_byte(self) -> None:
        for stem, strip, developer, markdown_hash, tex_hash in (
            DIRAC_MAIN_GOLDEN
        ):
            with self.subTest(document=stem):
                markdown_path = DIRAC_MAIN / f"{stem}.md"
                tex_path = DIRAC_MAIN / f"{stem}.tex"
                if not markdown_path.exists() or not tex_path.exists():
                    self.skipTest(f"{stem} absent from dirac-main")
                markdown_bytes = markdown_path.read_bytes()
                if sha256(markdown_bytes) != markdown_hash:
                    self.skipTest(f"{stem}.md is a different revision")
                self.assertEqual(sha256(tex_path.read_bytes()), tex_hash)
                latex = builder.convert(
                    markdown_bytes.decode("utf-8"),
                    strip,
                    developer,
                    author=builder.ORIGIN_AUTHOR,
                )
                self.assertEqual(sha256(latex.encode("utf-8")), tex_hash)

    def test_missing_title_or_subtitle_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "H1 title"):
            builder.convert("## Subtitle only\n")
        with self.assertRaisesRegex(ValueError, "H2 subtitle"):
            builder.convert("# Title only\n")


class GreekAndSymbolTests(unittest.TestCase):
    def test_prose_keeps_characters_and_declares_exactly_those_used(
        self,
    ) -> None:
        latex = builder.convert(minimal("Fields ψ and Ψ and ∂.\n"))
        self.assertIn("Fields ψ and Ψ and ∂.", body_of(latex))
        declarations = [
            line
            for line in latex.splitlines()
            if line.startswith("\\DeclareUnicodeCharacter")
        ]
        self.assertEqual(
            declarations,
            [
                "\\DeclareUnicodeCharacter{03A8}{\\ensuremath{\\Psi}}",
                "\\DeclareUnicodeCharacter{03C8}{\\ensuremath{\\psi}}",
                "\\DeclareUnicodeCharacter{2202}{\\ensuremath{\\partial}}",
            ],
        )
        preamble = latex.split("\\begin{document}")[0]
        self.assertLess(
            preamble.index("\\usepackage{microtype}"),
            preamble.index("\\DeclareUnicodeCharacter"),
        )
        self.assertLess(
            preamble.index("\\DeclareUnicodeCharacter"),
            preamble.index("\\pdfobjcompresslevel=0"),
        )

    def test_inline_math_gets_commands(self) -> None:
        latex = builder.convert(minimal("See $Ψ^† γ^a ∂_μ Ψ$ and $x²$.\n"))
        self.assertIn(
            "$\\Psi ^\\dagger  \\gamma ^a \\partial _\\mu  \\Psi $", latex
        )
        self.assertIn("$x^{2}$", latex)

    def test_compound_codes_are_braced_in_math(self) -> None:
        latex = builder.convert(minimal("$x ∈ ℝ^{4,4}$ and $Α$\n"))
        self.assertIn("$x \\in  {\\mathbb{R}}^{4,4}$", latex)
        self.assertIn("${\\mathrm{A}}$", latex)

    def test_display_math_gets_commands(self) -> None:
        latex = builder.convert(minimal("$$\nΩ_μ = ω_{μab}\n$$\n"))
        self.assertIn("\\[\n\\Omega _\\mu  = \\omega _{\\mu ab}\n\\]", latex)

    def test_code_span_with_greek_is_escaped_not_detokenized(self) -> None:
        latex = builder.convert(minimal("Code `Ψ_a^b` here.\n"))
        self.assertIn(
            "\\texttt{Ψ\\_a\\textasciicircum{}b}", latex
        )
        self.assertNotIn("\\detokenize{Ψ", latex)

    def test_fenced_code_keeps_characters(self) -> None:
        latex = builder.convert(minimal("```text\nΨ_0 = ψ\n```\n"))
        self.assertIn("\\begin{Verbatim}[fontsize=\\small]\nΨ_0 = ψ\n", latex)
        self.assertIn("DeclareUnicodeCharacter{03A8}", latex)

    def test_heading_keeps_unicode_for_bookmarks(self) -> None:
        latex = builder.convert(minimal("## The field Ψ\n"))
        self.assertIn("\\section{The field Ψ}", latex)

    def test_heading_math_is_wrapped_for_bookmarks(self) -> None:
        latex = builder.convert(minimal("## Connection $\\Omega_\\mu$\n"))
        self.assertIn(
            "\\section{Connection "
            "\\texorpdfstring{$\\Omega_\\mu$}{Ω\\_μ}}",
            latex,
        )

    def test_native_latin_letters_are_not_declared(self) -> None:
        latex = builder.convert(minimal("Weitzenböck and Łukasz.\n"))
        self.assertIn("Weitzenböck and Łukasz.", latex)
        self.assertNotIn("DeclareUnicodeCharacter", latex)

    def test_unsupported_characters_are_rejected_with_line(self) -> None:
        for character, code in (
            ("\u0304", "U+0304"),
            ("\u20ac", "U+20AC"),
            ("\U0001f600", "U+1F600"),
            ("\ufeff", "U+FEFF"),
        ):
            with self.subTest(code=code):
                with self.assertRaisesRegex(
                    ValueError, "line 5: .*" + re.escape(code)
                ):
                    builder.convert(minimal(f"Text {character}.\n"))
        with self.assertRaisesRegex(
            ValueError, "author line 1: .*" + re.escape("U+20AC")
        ):
            builder.convert(minimal("Text.\n"), author="\u20ac")

    def test_every_math_character_has_a_valid_code(self) -> None:
        for character, code in builder.MATH_CHARACTERS.items():
            with self.subTest(character=character):
                self.assertGreater(ord(character), 127)
                self.assertNotIn(character, builder.TEXT_CHARACTERS)
                self.assertTrue(code)
                self.assertTrue(builder.braces_balanced(code))
                self.assertTrue(all(ord(c) < 128 for c in code))


class LinkTests(unittest.TestCase):
    def test_plain_link(self) -> None:
        latex = builder.convert(minimal("See [dirac](https://x.org/d).\n"))
        self.assertIn("See \\href{https://x.org/d}{dirac}.", latex)

    def test_url_special_characters(self) -> None:
        latex = builder.convert(
            minimal("[q](https://x.org/a_b~c?x=1&y=2%20#top)\n")
        )
        self.assertIn(
            "\\href{https://x.org/a_b~c?x=1\\&y=2\\%20\\#top}{q}", latex
        )

    def test_balanced_parentheses_in_url(self) -> None:
        latex = builder.convert(
            minimal("[spin](https://en.wikipedia.org/wiki/Spin_(physics)).\n")
        )
        self.assertIn(
            "\\href{https://en.wikipedia.org/wiki/Spin_(physics)}{spin}.",
            latex,
        )

    def test_link_text_markup_and_nesting_in_bold(self) -> None:
        latex = builder.convert(
            minimal("**[the $\\psi$ field](https://x.org/p)**\n")
        )
        self.assertIn(
            "\\textbf{\\href{https://x.org/p}{the $\\psi$ field}}", latex
        )

    def test_link_in_heading_is_wrapped_for_bookmarks(self) -> None:
        latex = builder.convert(minimal("## See [dirac](https://x.org/d)\n"))
        self.assertIn(
            "\\section{See "
            "\\texorpdfstring{\\href{https://x.org/d}{dirac}}{dirac}}",
            latex,
        )

    def test_brackets_without_target_stay_text(self) -> None:
        latex = builder.convert(minimal("Ref [1] (see) and [a]b.\n"))
        self.assertIn("Ref [1] (see) and [a]b.", latex)
        self.assertNotIn("\\href", body_of(latex))

    def test_invalid_targets_are_rejected(self) -> None:
        for target in (
            "https://x.org/a b",
            "https://x.org/a\\b",
            "https://x.org/ψ",
            "https://x.org/100%",
            "https://x.org/{x}",
            "",
        ):
            with self.subTest(target=target):
                with self.assertRaises(ValueError):
                    builder.convert(minimal(f"[t]({target})\n"))

    def test_images_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "images are not supported"):
            builder.convert(minimal("![alt](figure.png)\n"))

    def test_list_item_starting_with_bracket_is_guarded(self) -> None:
        latex = builder.convert(
            minimal("- [x] literal\n- [l](https://x.org/l)\n")
        )
        self.assertIn("\\item {}[x] literal", latex)
        self.assertIn("\\item \\href{https://x.org/l}{l}", latex)


class TableTests(unittest.TestCase):
    TABLE = (
        "| Quantity | Symbol | Note |\n"
        "| --- | :---: | ---: |\n"
        "| metric | $\\eta_{ab}$ | [l](https://x.org/t) |\n"
        "| [b] | γ⁸ | `a#b` |\n"
    )

    def test_table_rendering(self) -> None:
        latex = builder.convert(minimal(self.TABLE))
        self.assertIn(
            "\\begin{longtable}{@{}p{0.307\\linewidth}p{0.307\\linewidth}"
            "p{0.307\\linewidth}@{}}",
            latex,
        )
        header = (
            "\\textbf{Quantity} & \\textbf{Symbol} & \\textbf{Note} \\\\"
        )
        self.assertEqual(latex.count(header), 2)
        self.assertIn("\\endfirsthead", latex)
        self.assertIn("\\endhead", latex)
        self.assertIn(
            "metric & $\\eta_{ab}$ & \\href{https://x.org/t}{l} \\\\", latex
        )
        self.assertIn("{}[b] & γ⁸ & \\texttt{a\\#b} \\\\", latex)
        self.assertIn("\\bottomrule\n\\end{longtable}", latex)

    def test_developer_layout_table(self) -> None:
        latex = builder.convert(minimal(self.TABLE), developer_layout=True)
        self.assertIn(
            ">{\\raggedright\\arraybackslash}p{0.267\\linewidth}", latex
        )
        self.assertIn("\\begingroup\n\\small\n\\begin{longtable}", latex)

    def test_inconsistent_row_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "line 7: table row has 2"):
            builder.convert(
                minimal("| a | b | c |\n| --- | --- | --- |\n| 1 | 2 |\n")
            )


class StructureValidationTests(unittest.TestCase):
    def test_code_line_limit(self) -> None:
        limit = builder.MAX_CODE_LINE_LENGTH
        self.assertEqual(limit, 89)
        builder.convert(minimal("```\n" + "x" * limit + "\n```\n"))
        with self.assertRaisesRegex(ValueError, "line 6: fenced code line"):
            builder.convert(minimal("```\n" + "x" * (limit + 1) + "\n```\n"))

    def test_tab_in_code_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "tab"):
            builder.convert(minimal("```\na\tb\n```\n"))

    def test_unclosed_blocks_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "fenced code is not closed"):
            builder.convert(minimal("```\ncode\n"))
        with self.assertRaisesRegex(ValueError, "display math is not closed"):
            builder.convert(minimal("$$\nx\n"))

    def test_code_spans_unsafe_for_detokenize(self) -> None:
        latex = builder.convert(
            minimal("`a#b` `50%` `C:\\x` `{a` `ok_{b}`\n")
        )
        self.assertIn("\\texttt{a\\#b}", latex)
        self.assertIn("\\texttt{50\\%}", latex)
        self.assertIn("\\texttt{C:\\textbackslash{}x}", latex)
        self.assertIn("\\texttt{\\{a}", latex)
        self.assertIn("\\texttt{\\detokenize{ok_{b}}}", latex)


class RegistryTests(unittest.TestCase):
    def test_built_in_registry_is_empty(self) -> None:
        self.assertEqual(check_provenance_pdf.SPECIFICATIONS, {})

    def test_repository_registry_is_valid_and_canonical(self) -> None:
        path = check_provenance_pdf.DEFAULT_SPECIFICATIONS_PATH
        self.assertTrue(path.exists())
        registry = check_provenance_pdf.load_specifications(path)
        self.assertEqual(
            path.read_bytes(),
            check_provenance_pdf.dump_specifications(registry).encode(
                "utf-8"
            ),
        )

    def test_registered_pdfs_are_self_consistent(self) -> None:
        registry = check_provenance_pdf.load_specifications()
        for edition, specification in registry.items():
            with self.subTest(edition=edition):
                report = check_dissertation_pdf.verify_pdf(
                    REPOSITORY_ROOT / str(specification["path"]),
                    None,
                    int(specification["pages"]),
                    612.0,
                    792.0,
                    str(specification["sha256"]),
                )
                self.assertEqual(
                    [n for n, ok in report["checks"].items() if not ok], []
                )

    def test_register_round_trip_and_canonical_dump(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "provenance" / "specs.json"
            check_provenance_pdf.register_edition(
                path, "zeta-doc", "provenance/Z.pdf", 3, "b" * 64
            )
            check_provenance_pdf.register_edition(
                path, "alpha-doc", "provenance/A.pdf", 2, "a" * 64
            )
            check_provenance_pdf.register_edition(
                path, "zeta-doc", "provenance/Z.pdf", 4, "c" * 64
            )
            content = path.read_bytes()
            registry = check_provenance_pdf.load_specifications(path)
        self.assertEqual(list(registry), ["alpha-doc", "zeta-doc"])
        self.assertEqual(
            registry["zeta-doc"],
            {"path": "provenance/Z.pdf", "pages": 4, "sha256": "c" * 64},
        )
        self.assertNotIn(b"\r", content)
        self.assertTrue(content.endswith(b"}\n"))
        self.assertEqual(
            json.loads(content),
            {
                "alpha-doc": {
                    "path": "provenance/A.pdf",
                    "pages": 2,
                    "sha256": "a" * 64,
                },
                "zeta-doc": {
                    "path": "provenance/Z.pdf",
                    "pages": 4,
                    "sha256": "c" * 64,
                },
            },
        )

    def test_invalid_entries_are_rejected(self) -> None:
        good = {"path": "provenance/X.pdf", "pages": 1, "sha256": "0" * 64}
        cases = {
            "Bad_Name": good,
            "extra-key": dict(good, note="x"),
            "missing-key": {"path": "provenance/X.pdf", "pages": 1},
            "bad-sha": dict(good, sha256="A" * 64),
            "short-sha": dict(good, sha256="0" * 63),
            "absolute": dict(good, path="/provenance/X.pdf"),
            "drive": dict(good, path="C:/X.pdf"),
            "parent": dict(good, path="../X.pdf"),
            "backslash": dict(good, path="provenance\\X.pdf"),
            "not-pdf": dict(good, path="provenance/X.tex"),
            "zero-pages": dict(good, pages=0),
            "bool-pages": dict(good, pages=True),
        }
        for edition, entry in cases.items():
            with self.subTest(edition=edition):
                with self.assertRaises(check_provenance_pdf.SpecificationError):
                    check_provenance_pdf.validate_specification(
                        edition, entry
                    )

    def test_duplicate_keys_and_non_object_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "specs.json"
            path.write_bytes(b'{"a": {}, "a": {}}\n')
            with self.assertRaisesRegex(
                check_provenance_pdf.SpecificationError, "duplicate"
            ):
                check_provenance_pdf.load_specifications(path)
            path.write_bytes(b"[]\n")
            with self.assertRaises(check_provenance_pdf.SpecificationError):
                check_provenance_pdf.load_specifications(path)

    def test_cli_rejects_unregistered_edition(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "specs.json"
            path.write_bytes(b"{}\n")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "check_provenance_pdf.py"),
                    "--edition",
                    "not-registered",
                    "--specifications",
                    str(path),
                ],
                capture_output=True,
                check=False,
            )
        self.assertEqual(completed.returncode, 2)
        self.assertIn(b"not registered", completed.stderr)


class LogScanTests(unittest.TestCase):
    def test_warning_pattern_matches_like_the_gates(self) -> None:
        log = "\n".join(
            [
                "This is pdfTeX",
                "LaTeX Font Info:    External font `lmex10' loaded",
                "! Undefined control sequence.",
                "Overfull \\hbox (1.0pt too wide) in paragraph",
                "Package hyperref Warning: Token not allowed",
                "LaTeX Warning: Reference `x' undefined",
                "underfull \\vbox (badness 10000)",
                "Package microtype Info: done",
            ]
        )
        self.assertEqual(
            build_provenance_pdf.scan_log(log),
            [
                "! Undefined control sequence.",
                "Overfull \\hbox (1.0pt too wide) in paragraph",
                "Package hyperref Warning: Token not allowed",
                "LaTeX Warning: Reference `x' undefined",
                "underfull \\vbox (badness 10000)",
            ],
        )
        self.assertEqual(build_provenance_pdf.scan_log("clean\nlog\n"), [])


def run_pdflatex(tex: Path, output_directory: Path, passes: int) -> None:
    output_directory.mkdir(parents=True, exist_ok=True)
    for _ in range(passes):
        completed = subprocess.run(
            [
                PDFLATEX,
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-jobname=feature",
                f"-output-directory={output_directory}",
                str(tex),
            ],
            cwd=tex.parent,
            capture_output=True,
            timeout=600,
            check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(
                completed.stdout.decode("utf-8", "replace")[-2000:]
            )


@unittest.skipUnless(PDFLATEX, "pdflatex is not installed")
class PdfTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.directory = tempfile.TemporaryDirectory()
        root = Path(cls.directory.name)
        tex = root / "feature.tex"
        tex.write_bytes(
            builder.convert(FEATURE_MARKDOWN, True).encode("utf-8")
        )
        run_pdflatex(tex, root / "a", 3)
        run_pdflatex(tex, root / "b", 3)
        cls.root = root
        cls.pdf_a = root / "a" / "feature.pdf"
        cls.pdf_b = root / "b" / "feature.pdf"
        cls.log_a = (root / "a" / "feature.log").read_bytes().decode(
            "latin-1"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_feature_document_compiles_warning_free(self) -> None:
        self.assertEqual(build_provenance_pdf.scan_log(self.log_a), [])

    def test_two_builds_are_byte_identical_letter_pdfs(self) -> None:
        content = self.pdf_a.read_bytes()
        report = check_dissertation_pdf.verify_pdf(
            self.pdf_a,
            self.pdf_b,
            len(check_dissertation_pdf.PAGE_PATTERN.findall(content)),
            612.0,
            792.0,
            sha256(content),
        )
        self.assertTrue(all(report["checks"].values()), report)
        self.assertGreaterEqual(report["measurements"]["pageCount"], 2)

    def test_checker_rejects_mutated_bytes(self) -> None:
        content = self.pdf_a.read_bytes()
        pages = len(check_dissertation_pdf.PAGE_PATTERN.findall(content))
        position = content.index(b"/Producer")
        flipped = bytearray(content)
        flipped[position + 3] ^= 0x01
        mutations = {
            "flipped-byte": bytes(flipped),
            "appended-byte": content + b"\n",
            "truncated": content[:-64],
        }
        for label, mutated in mutations.items():
            with self.subTest(mutation=label):
                path = self.root / f"{label}.pdf"
                path.write_bytes(mutated)
                report = check_dissertation_pdf.verify_pdf(
                    path, self.pdf_a, pages, 612.0, 792.0, sha256(content)
                )
                self.assertFalse(report["checks"]["canonicalHash"])
                self.assertFalse(report["checks"]["repeatByteIdentity"])
        truncated = check_dissertation_pdf.verify_pdf(
            self.root / "truncated.pdf", None, pages, 612.0, 792.0,
            sha256(content),
        )
        self.assertFalse(truncated["checks"]["endMarker"])

    def test_provenance_checker_cli_with_a_temporary_registry(self) -> None:
        content = self.pdf_a.read_bytes()
        registry = self.root / "specs.json"
        check_provenance_pdf.register_edition(
            registry,
            "feature",
            "a/feature.pdf",
            len(check_dissertation_pdf.PAGE_PATTERN.findall(content)),
            sha256(content),
        )
        command = [
            sys.executable,
            str(SCRIPTS / "check_provenance_pdf.py"),
            "--edition",
            "feature",
            "--specifications",
            str(registry),
            "--repository-root",
            str(self.root),
        ]
        passed = subprocess.run(
            command + ["--repeat", str(self.pdf_b)],
            capture_output=True,
            check=False,
        )
        self.assertEqual(passed.returncode, 0, passed.stdout)
        self.assertIn(b"failed_check_count=0", passed.stdout)
        mutated = self.root / "mutated.pdf"
        mutated.write_bytes(content + b" ")
        failed = subprocess.run(
            command + [str(mutated)], capture_output=True, check=False
        )
        self.assertEqual(failed.returncode, 1)
        self.assertIn(b"check_canonicalHash=false", failed.stdout)


@unittest.skipUnless(PDFLATEX, "pdflatex is not installed")
class BuildProvenancePdfTests(unittest.TestCase):
    def run_builder(self, root: Path, *extra: str) -> tuple[int, str]:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "build_provenance_pdf.py"),
                str(root / "provenance" / "FEATURE_DOC.md"),
                "--repository-root",
                str(root),
                *extra,
            ],
            capture_output=True,
            timeout=1800,
            check=False,
        )
        return completed.returncode, completed.stdout.decode("utf-8")

    def test_register_verify_and_reject(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "provenance").mkdir()
            markdown = root / "provenance" / "FEATURE_DOC.md"
            markdown.write_bytes(FEATURE_MARKDOWN.encode("utf-8"))
            registry = root / "provenance" / "pdf-specifications.json"
            registry.write_bytes(b"{}\n")

            code, output = self.run_builder(root)
            self.assertEqual(code, 1, output)
            self.assertIn("check_editionRegistered=false", output)
            self.assertFalse((root / "provenance" / "FEATURE_DOC.pdf").exists())

            code, output = self.run_builder(root, "--register")
            self.assertEqual(code, 0, output)
            self.assertIn("provenance_pdf=OK", output)
            entry = check_provenance_pdf.load_specifications(registry)[
                "feature-doc"
            ]
            pdf = root / "provenance" / "FEATURE_DOC.pdf"
            self.assertEqual(entry["path"], "provenance/FEATURE_DOC.pdf")
            self.assertEqual(entry["sha256"], sha256(pdf.read_bytes()))
            self.assertTrue((root / "provenance" / "FEATURE_DOC.tex").exists())
            report = json.loads(
                (
                    root / "build" / "FEATURE_DOC" / "build-provenance-pdf.json"
                ).read_bytes()
            )
            self.assertEqual(report["schemaVersion"], 1)
            self.assertTrue(all(report["checks"].values()))

            code, output = self.run_builder(root)
            self.assertEqual(code, 0, output)
            self.assertIn("check_registeredSha256=true", output)
            self.assertIn("check_texRepeatByteIdentity=true", output)
            self.assertIn("check_pdfRepeatByteIdentity=true", output)

            markdown.write_bytes(
                FEATURE_MARKDOWN.replace("Feature test", "Changed test").encode(
                    "utf-8"
                )
            )
            code, output = self.run_builder(root)
            self.assertEqual(code, 1, output)
            self.assertIn("check_registeredSha256=false", output)
            self.assertIn("check_provenancePdfCopy=false", output)
            self.assertEqual(entry["sha256"], sha256(pdf.read_bytes()))

            markdown.write_bytes(
                minimal("Overfull " + "x" * 200 + "\n").encode("utf-8")
            )
            code, output = self.run_builder(root, "--register")
            self.assertEqual(code, 1, output)
            self.assertIn("check_logWarningFree=false", output)
            self.assertIn("latex_warning=pdf-a: Overfull", output)
            self.assertEqual(
                check_provenance_pdf.load_specifications(registry)[
                    "feature-doc"
                ],
                entry,
            )


if __name__ == "__main__":
    unittest.main()
