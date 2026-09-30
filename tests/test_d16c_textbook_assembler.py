# SPDX-License-Identifier: GPL-3.0-or-later
"""Unit tests of scripts/build_textbook.py on synthetic chapters.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_textbook_assembler.py" -v

Every test writes its own small chapter files into a temporary directory and
calls the assembler there (the function assemble() with a three-chapter plan,
or main() with the real 21-chapter plan and --allow-missing), so the tests do
not depend on the chapters of the real book and take well under a second.
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import build_textbook  # noqa: E402

PLAN3 = {0: "Zero", 1: "One", 2: "Two"}
PNG_BYTES = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16


def chapter_text(
    number: int, title: str, sections: int = 2, extra: str = ""
) -> str:
    lines = [f"## {number}. {title}", "", f"Introduction to chapter {number}."]
    for index in range(1, sections + 1):
        lines += [
            "",
            f"### {number}.{index} Part {index}",
            "",
            f"Text of section {number}.{index}.",
        ]
    if extra:
        lines += ["", extra]
    return "\n".join(lines) + "\n"


class TextbookTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.root = Path(self._temporary.name)
        self.chapters = self.root / "chapters"
        self.chapters.mkdir()

    def tearDown(self) -> None:
        self._temporary.cleanup()

    def write(self, name: str, text: str | bytes) -> Path:
        path = self.chapters / name
        path.write_bytes(text if isinstance(text, bytes) else text.encode("utf-8"))
        return path

    def write_plan3(self, extra: dict[int, str] | None = None) -> None:
        extra = extra or {}
        for number, name in ((0, "zero"), (1, "one"), (2, "two")):
            self.write(
                f"0{number}-{name}.md",
                chapter_text(number, name.title(), extra=extra.get(number, "")),
            )

    def run_assemble(self, **options) -> build_textbook.Assembly:
        options.setdefault("planned", PLAN3)
        options.setdefault("image_root", self.root)
        options.setdefault("display_root", self.root)
        return build_textbook.assemble(self.chapters, **options)

    def failed(self, assembly: build_textbook.Assembly) -> set[str]:
        return {name for name, value in assembly.checks.items() if not value}

    def statuses(self, assembly: build_textbook.Assembly) -> list[tuple[str, str]]:
        return [(r.target, r.status) for r in assembly.references]

    def run_main(self, *arguments: str) -> tuple[int, str]:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = build_textbook.main(
                [
                    "--chapters-directory",
                    str(self.chapters),
                    "--repository-root",
                    str(self.root),
                    *arguments,
                ]
            )
        return code, buffer.getvalue()


class AssemblyTests(TextbookTestCase):
    def test_complete_book_assembles_in_order(self) -> None:
        self.write_plan3(
            {0: "See Chapter 1, Section 2.1 and Sections 1.1 and 1.2."}
        )
        assembly = self.run_assemble()
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        text = assembly.text
        self.assertTrue(
            text.startswith(
                "# dirac16complex: a textbook for students\n\n## "
                + build_textbook.SUBTITLE
                + "\n\n## Abstract\n\n"
            )
        )
        self.assertLess(text.index("## 0. Zero"), text.index("## 1. One"))
        self.assertLess(text.index("## 1. One"), text.index("## 2. Two"))
        self.assertNotIn("\r", text)
        self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"))
        self.assertIn(
            "Sections 1.1 and 1.2.\n\n## 1. One\n\nIntroduction", text
        )
        self.assertEqual(
            sorted(set(self.statuses(assembly))),
            [("1", "resolved"), ("1.1", "resolved"), ("1.2", "resolved"),
             ("2.1", "resolved")],
        )
        self.assertEqual(assembly.text, self.run_assemble().text)

    def test_strict_mode_requires_every_planned_chapter(self) -> None:
        self.write("00-zero.md", chapter_text(0, "Zero"))
        self.write("02-two.md", chapter_text(2, "Two"))
        assembly = self.run_assemble()
        self.assertEqual(assembly.missing, [1])
        self.assertEqual(
            self.failed(assembly),
            {"chapterNumbersConsecutive", "allPlannedChaptersPresent"},
        )

    def test_allow_missing_reports_gaps_and_pending_references(self) -> None:
        self.write("00-zero.md", chapter_text(0, "Zero", extra="Chapter 1 and Section 1.3."))
        self.write("02-two.md", chapter_text(2, "Two"))
        assembly = self.run_assemble(allow_missing=True)
        self.assertEqual(assembly.missing, [1])
        self.assertNotIn("chapterNumbersConsecutive", assembly.checks)
        self.assertNotIn("allPlannedChaptersPresent", assembly.checks)
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        self.assertEqual(
            self.statuses(assembly), [("1", "pending"), ("1.3", "pending")]
        )

    def test_reference_outside_the_plan_never_pending(self) -> None:
        self.write("00-zero.md", chapter_text(0, "Zero", extra="See Chapter 7."))
        assembly = self.run_assemble(allow_missing=True)
        self.assertEqual(self.failed(assembly), {"crossReferencesResolve"})
        self.assertEqual(self.statuses(assembly), [("7", "unresolved")])

    def test_missing_section_of_existing_chapter(self) -> None:
        self.write_plan3({0: "Details are in Section 1.5."})
        assembly = self.run_assemble()
        self.assertEqual(self.failed(assembly), {"crossReferencesResolve"})
        self.assertIn("1.1 to 1.2", assembly.problems[0].message)
        self.assertEqual(assembly.problems[0].location, "chapters/00-zero.md:13")

    def test_chapter_heading_must_match_file_number(self) -> None:
        self.write_plan3()
        self.write("01-one.md", chapter_text(2, "One").replace("### 2.", "### 1."))
        self.assertIn("chapterHeadings", self.failed(self.run_assemble()))

    def test_chapter_heading_without_leading_zero(self) -> None:
        self.write_plan3()
        self.write("01-one.md", chapter_text(1, "One").replace("## 1.", "## 01.", 1))
        self.assertIn("chapterHeadings", self.failed(self.run_assemble()))

    def test_first_line_must_be_the_chapter_heading(self) -> None:
        for prefix in ("Some text.\n\n", "```\ncode\n```\n\n", "$$\nx\n$$\n\n"):
            with self.subTest(prefix=prefix):
                self.write_plan3()
                self.write("01-one.md", prefix + chapter_text(1, "One"))
                self.assertIn("chapterHeadings", self.failed(self.run_assemble()))
        self.write_plan3()
        self.write("01-one.md", "\n\n" + chapter_text(1, "One"))
        assembly = self.run_assemble()
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        self.assertIn("\n\n## 1. One\n\nIntroduction to chapter 1.", assembly.text)

    def test_heading_levels(self) -> None:
        for extra, check in (
            ("# A title", "headingLevels"),
            ("#### Too deep", "headingLevels"),
            ("## 1. Again", "chapterHeadings"),
        ):
            with self.subTest(extra=extra):
                self.write_plan3({1: extra})
                self.assertIn(check, self.failed(self.run_assemble()))

    def test_hash_lines_inside_code_and_math_are_not_headings(self) -> None:
        extra = "```\n# a shell comment\n#### another\n```\n\n$$\nx\n$$"
        self.write_plan3({1: extra})
        self.assertEqual(self.failed(self.run_assemble()), set())

    def test_section_numbers_in_order_from_one(self) -> None:
        cases = (
            chapter_text(1, "One").replace("### 1.2", "### 1.3"),
            chapter_text(1, "One").replace("### 1.1", "### 1.0"),
            chapter_text(1, "One").replace("### 1.2", "### 2.2"),
            chapter_text(1, "One").replace("### 1.2 Part 2", "### Part 2"),
        )
        for text in cases:
            with self.subTest(text=text):
                self.write_plan3()
                self.write("01-one.md", text)
                self.assertIn("sectionNumbers", self.failed(self.run_assemble()))

    def test_duplicate_section_number(self) -> None:
        self.write_plan3()
        self.write("01-one.md", chapter_text(1, "One").replace("### 1.2", "### 1.1"))
        failed = self.failed(self.run_assemble())
        self.assertIn("sectionNumbersUnique", failed)
        self.assertIn("sectionNumbers", failed)

    def test_duplicate_chapter_number(self) -> None:
        self.write_plan3()
        self.write("01-uno.md", chapter_text(1, "Uno"))
        failed = self.failed(self.run_assemble())
        self.assertIn("chapterNumbersUnique", failed)
        self.assertIn("sectionNumbersUnique", failed)

    def test_file_names(self) -> None:
        # (no upper-case variant of an existing name: Windows file names are
        # case-insensitive, so it would overwrite 01-one.md)
        for name in ("1-one.md", "01_one.md", "05-Five.md", "01--one.md"):
            with self.subTest(name=name):
                for path in self.chapters.iterdir():
                    path.unlink()
                self.write_plan3()
                self.write(name, chapter_text(1, "One"))
                self.assertIn("chapterFileNames", self.failed(self.run_assemble()))
        for path in self.chapters.iterdir():
            path.unlink()
        self.write_plan3()
        self.write("notes.txt", "not a chapter")
        self.assertEqual(self.failed(self.run_assemble()), set())

    def test_chapter_number_outside_plan(self) -> None:
        self.write_plan3()
        self.write("03-three.md", chapter_text(3, "Three"))
        self.assertIn("chapterNumbersInPlan", self.failed(self.run_assemble()))

    def test_encoding(self) -> None:
        for content in (
            chapter_text(1, "One").replace("\n", "\r\n").encode("utf-8"),
            b"\xef\xbb\xbf" + chapter_text(1, "One").encode("utf-8"),
            "## 1. One\n\ncafé\n".encode("latin-1"),
            b"\n\n",
        ):
            with self.subTest(content=content[:12]):
                self.write_plan3()
                self.write("01-one.md", content)
                self.assertIn("chapterEncoding", self.failed(self.run_assemble()))


class ReferenceTests(TextbookTestCase):
    def references_of(self, sentence: str, **options) -> build_textbook.Assembly:
        self.write_plan3({0: sentence})
        return self.run_assemble(**options)

    def test_plural_lists_and_ranges(self) -> None:
        assembly = self.references_of(
            "Chapters 0 to 2 build on Sections 1.1-1.2, and Sections 1.1, "
            "1.2 and 2.1 are short; Chapters 1 and 2 as well."
        )
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        self.assertEqual(
            self.statuses(assembly),
            [("0", "resolved"), ("1", "resolved"), ("2", "resolved"),
             ("1.1", "resolved"), ("1.2", "resolved"),
             ("1.1", "resolved"), ("1.2", "resolved"), ("2.1", "resolved"),
             ("1", "resolved"), ("2", "resolved")],
        )

    def test_range_expansion_finds_a_missing_middle_section(self) -> None:
        assembly = self.references_of("Sections 1.1 to 1.3 differ.")
        self.assertEqual(
            self.statuses(assembly),
            [("1.1", "resolved"), ("1.2", "resolved"), ("1.3", "unresolved")],
        )

    def test_en_dash_range(self) -> None:
        assembly = self.references_of("Chapters 0–2 and Sections 1.1–1.2.")
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        self.assertEqual(
            [target for target, _ in self.statuses(assembly)],
            ["0", "1", "2", "1.1", "1.2"],
        )

    def test_singular_forms_take_one_number(self) -> None:
        assembly = self.references_of(
            "The gammas of Chapter 2, 16 by 16 matrices, and Section 1.2, 17 of them."
        )
        self.assertEqual(self.failed(assembly), set(), assembly.problems)
        self.assertEqual(self.statuses(assembly), [("2", "resolved"), ("1.2", "resolved")])

    def test_malformed_references(self) -> None:
        for sentence in ("See Chapter 1.2.", "See Section 1.", "See Section 1.1.1."):
            with self.subTest(sentence=sentence):
                assembly = self.references_of(sentence)
                self.assertEqual(self.failed(assembly), {"crossReferencesResolve"})

    def test_words_without_numbers_and_lower_case_are_ignored(self) -> None:
        assembly = self.references_of(
            "This Chapter is short; section 9 of the manual and chapter 5 of a "
            "book are not ours; a Section cell; Subsection 9.9 is no keyword."
        )
        self.assertEqual(assembly.references, [])
        self.assertEqual(self.failed(assembly), set())

    def test_code_math_and_code_spans_are_not_scanned(self) -> None:
        assembly = self.references_of(
            "Inline `Chapter 99` and $\\text{Section 9.9}$ are ignored.\n\n"
            "```\nChapter 99 in code\n```\n\n$$\nSection 9.9\n$$"
        )
        self.assertEqual(assembly.references, [])
        self.assertEqual(self.failed(assembly), set(), assembly.problems)

    def test_external_references_are_not_checked(self) -> None:
        sentences = (
            "Section 7.7 of the Stage-1 document proves it.",
            "It is in the Stage-1 document, Section 7.7.",
            "It is proved (Stage-1 document, Section 7.7).",
            "It is proved in the Stage-1 document (Section 7.7).",
            "See `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, Section 12.",
            "This is Stage 1 Section 5, Result 5.6.",
            "It was corrected (Stage 2, Section 15.5).",
            "It is Section 13.7 in `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md`.",
            "Read the student guide, Section 6.4.",
            "Read STAGE4_SPEC.md Section 7 first.",
            "See Sections 2-4 of the Stage-1 document.",
            "See Section 5 of Stage 1.",
            "It is in the Stage-2 document's Section 4.4.",
        )
        for sentence in sentences:
            with self.subTest(sentence=sentence):
                assembly = self.references_of(sentence)
                self.assertEqual(self.failed(assembly), set(), assembly.problems)
                self.assertEqual(
                    {status for _, status in self.statuses(assembly)}, {"external"}
                )

    def test_internal_references_near_document_words(self) -> None:
        sentences = (
            "Compare the Stage-1 document and Section 1.1.",
            "We use the conventions of the whole book (Chapter 1).",
            "The notebook's metric (Chapter 2) is static.",
            "The report of Chapter 2 counts checks.",
            "Chapter 1 of this book explains it.",
            "In Stage 4, Chapter 2 solves it.",
            "The Stage-1 document proves it. Section 1.1 repeats the proof.",
            "The class in `scripts/check.py` follows Sections 1.1 to 1.2 line by line.",
            "It is excluded (Stage-2 document §15.5, Chapter 2).",
            "The Stage-1 document and the student guide agree with Section 1.2.",
        )
        for sentence in sentences:
            with self.subTest(sentence=sentence):
                assembly = self.references_of(sentence)
                self.assertEqual(self.failed(assembly), set(), assembly.problems)
                self.assertEqual(
                    {status for _, status in self.statuses(assembly)}, {"resolved"}
                )
        assembly = self.references_of("The whole book (Chapter 7) is long.")
        self.assertEqual(self.failed(assembly), {"crossReferencesResolve"})


class ConversionTests(TextbookTestCase):
    def test_builder_errors_point_to_the_chapter_line(self) -> None:
        long_line = "x" * 95
        self.write_plan3({1: f"```\n{long_line}\n```"})
        assembly = self.run_assemble()
        self.assertEqual(self.failed(assembly), {"markdownConvertible"})
        message = assembly.problems[0].message
        self.assertIn("chapters/01-one.md:14", message)
        self.assertIn("95 characters", message)

    def test_unequal_table_rows_and_bad_characters(self) -> None:
        for extra in ("| a | b |\n| --- | --- |\n| 1 |", "A snowman ☃ here."):
            with self.subTest(extra=extra):
                self.write_plan3({2: extra})
                assembly = self.run_assemble()
                self.assertEqual(self.failed(assembly), {"markdownConvertible"})
                self.assertIn("chapters/02-two.md:", assembly.problems[0].message)

    def test_figures_must_exist_under_the_image_root(self) -> None:
        self.write_plan3({1: "![A figure](figures/plot.png)"})
        self.assertEqual(self.failed(self.run_assemble()), {"markdownConvertible"})
        (self.root / "figures").mkdir()
        (self.root / "figures" / "plot.png").write_bytes(PNG_BYTES)
        self.assertEqual(self.failed(self.run_assemble()), set())


class CommandLineTests(TextbookTestCase):
    def write_full_plan(self) -> None:
        for number in build_textbook.PLANNED_CHAPTERS:
            self.write(f"{number:02d}-part.md", chapter_text(number, f"Part {number}"))

    def test_check_mode_with_missing_chapters_writes_nothing(self) -> None:
        self.write_plan3()
        output = self.root / "book.md"
        code, printed = self.run_main(
            "--check", "--allow-missing", "--output", str(output)
        )
        self.assertEqual(code, 0, printed)
        self.assertFalse(output.exists())
        self.assertIn("missing_chapter=03 ", printed)
        self.assertIn("measurement_missingChapters=03,04,", printed)
        self.assertTrue(printed.rstrip().endswith("textbook_assembly=OK"))

    def test_strict_mode_fails_with_missing_chapters(self) -> None:
        self.write_plan3()
        output = self.root / "book.md"
        code, printed = self.run_main("--output", str(output))
        self.assertEqual(code, 1)
        self.assertFalse(output.exists())
        self.assertIn("check_allPlannedChaptersPresent=false", printed)
        self.assertIn("check_outputWritten=false", printed)

    def test_draft_goes_to_the_build_directory(self) -> None:
        self.write_plan3()
        code, printed = self.run_main("--allow-missing")
        self.assertEqual(code, 0, printed)
        draft = self.root / "build" / "textbook" / "DIRAC16COMPLEX_TEXTBOOK.md"
        self.assertTrue(draft.is_file())
        self.assertIn("output=build/textbook/DIRAC16COMPLEX_TEXTBOOK.md", printed)
        self.assertFalse((self.root / "provenance").exists())

    def test_complete_book_is_written_and_verified(self) -> None:
        self.write_full_plan()
        code, printed = self.run_main()
        self.assertEqual(code, 0, printed)
        output = self.root / "provenance" / "DIRAC16COMPLEX_TEXTBOOK.md"
        first = output.read_bytes()
        self.assertNotIn(b"\r", first)
        self.assertIn("check_outputWritten=true", printed)
        code, printed = self.run_main("--verify-output")
        self.assertEqual(code, 0, printed)
        self.assertIn("check_outputUpToDate=true", printed)
        code, _ = self.run_main()
        self.assertEqual(output.read_bytes(), first)
        output.write_bytes(first + b"\n")
        code, printed = self.run_main("--verify-output")
        self.assertEqual(code, 1)
        self.assertIn("check_outputUpToDate=false", printed)

    def test_missing_chapter_directory_is_a_usage_error(self) -> None:
        code, printed = self.run_main(
            "--check", "--chapters-directory", str(self.root / "absent")
        )
        self.assertEqual(code, 2)
        self.assertIn("usage_error=", printed)


class PlanTests(unittest.TestCase):
    def test_plan_and_title_follow_the_specification(self) -> None:
        self.assertEqual(sorted(build_textbook.PLANNED_CHAPTERS), list(range(21)))
        self.assertEqual(
            build_textbook.TITLE, "dirac16complex: a textbook for students"
        )
        self.assertEqual(
            build_textbook.OUTPUT_RELATIVE.as_posix(),
            "provenance/DIRAC16COMPLEX_TEXTBOOK.md",
        )


if __name__ == "__main__":
    unittest.main()
