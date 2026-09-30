#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Written for this repository on 2026-09-30 for the textbook specified in
# handoff/specs/TEXTBOOK_SPEC.md (section 2, "Assembler").
"""Assemble the dirac16complex textbook from its chapter files and check it.

Input: the chapter sources provenance/textbook/chapters/NN-short-name.md with
NN = 00..20 (always two digits) and a short name of lower-case ASCII letters
and digits joined by single hyphens.  Output: provenance/DIRAC16COMPLEX_TEXTBOOK.md,
which is the title block (the H1 title, the H2 subtitle and the abstract, all
defined below) followed by every chapter in the order of NN, one blank line
between chapters, UTF-8, LF line endings and exactly one final newline.  The
bytes depend only on the bytes of the chapter files and on this script (no
date, no path, no environment variable enters them), so two runs on the same
chapters write identical files.

Usage, from the repository root (PowerShell and Bash alike):

    python scripts/build_textbook.py                   # check, then write
    python scripts/build_textbook.py --check           # check only
    python scripts/build_textbook.py --check --allow-missing
    python scripts/build_textbook.py --check --verify-output

By default every planned chapter 00..20 must exist.  With --allow-missing the
chapters that exist so far are checked and assembled, each missing planned
chapter is reported as a missing_chapter line, and the draft is written to the
git-ignored build/textbook/DIRAC16COMPLEX_TEXTBOOK.md instead of provenance/
(unless --output is given), so that an incomplete book never replaces the
published one.  --verify-output (implies --check) also requires the existing
output file to be byte-identical to the assembly.

Checks (each printed as check_<name>=true|false; any false fails the run):
  chapterFileNames           every *.md file in the chapter directory is named
                             NN-short-name.md (other files are ignored)
  chapterNumbersUnique       no two chapter files share NN
  chapterNumbersInPlan       every NN is a planned chapter (00..20)
  chapterNumbersConsecutive  the chapter numbers are 0, 1, 2, ... without a gap
                             (not a check with --allow-missing)
  allPlannedChaptersPresent  every planned chapter exists (not a check with
                             --allow-missing; the gaps are reported instead)
  chapterEncoding            UTF-8 without byte-order mark, LF line endings (no
                             CR anywhere), not empty
  chapterHeadings            the first non-blank line is "## N. Title" with
                             N = int(NN) (no leading zero), and it is the only
                             level-2 heading of the file
  headingLevels              no "# " heading (the assembler adds the title) and
                             no heading deeper than "### "
  sectionNumbers             every "### " heading reads "### N.M Title" with N
                             the chapter number and M = 1, 2, 3, ... in order
  sectionNumbersUnique       no section number N.M occurs twice in the book
  crossReferencesResolve     every internal reference resolves (rules below)
  markdownConvertible        scripts/build_dissertation_tex.py converts the
                             assembled book (characters, tables with equal
                             cell counts, fenced code lines of at most 89
                             characters without tabs, figure lines whose PNG
                             exists under the repository root); its line
                             numbers are translated back to chapter:line
  outputWritten              (build mode only) the output file was written;
                             it is written only when every other check passed
  outputUpToDate             (--verify-output only) the existing output file
                             equals the assembly byte for byte
Headings are recognised as build_dissertation_tex.py recognises them: a line
whose stripped form starts with 1 to 6 "#" and a space, outside fenced code
(```) and outside display math ($$ lines).

Cross-references.  A reference is one of the capitalised words Chapter,
Chapters, Section or Sections followed by a number: "Chapter 3",
"Section 3.2", "Chapters 12 and 13", "Chapters 12 to 14", "Sections 3.2,
3.4 and 3.5", "Sections 3.2-3.4" (the plural forms take lists; "to", "-"
and the en dash denote ranges, which are expanded when both ends lie in the
same chapter).  Text inside fenced code, display math, inline math $...$ and
code spans `...` is not scanned.  Lower-case "section 7" is never a reference.
A reference is EXTERNAL (it points into another document and is not checked)
when
  (a) the word directly before the keyword (in the same sentence; a token
      made only of brackets, quotes or commas, such as "(", is skipped) names
      another document: it contains DIRAC16COMPLEX, a repository folder
      (provenance/, handoff/, artifacts/, scripts/, studies/, wolfram/,
      notebooks/), a file suffix .md .tex .pdf .json .nb .wl, SPEC,
      CONTRACT, HANDOFF, README, or one of the words document(s),
      specification(s), guide (either case of the first letter), for example
      "the Stage-1 document, Section 7.7", "(Stage-1 document, Section 7.7)",
      "the Stage-1 document (Section 7.7)", "the student guide, Section 6.4"
      or "`README.md` Section 3";
  (b) for Section only: the text directly before the keyword ends with a
      stage name "Stage 1", "Stage-1" (optionally followed by a comma), as in
      "Stage 1 Section 5";
  (c) the reference is directly followed by " of ", " in " or " from " and
      the rest of its clause (up to the next ",", sentence end or 120
      characters) names another document in the sense of (a) or starts with
      a stage name, as in "Section 7.7 of the Stage-1 document".
The words book, notebook, report and paper are deliberately not markers
("the whole book (Chapter 1)", "the notebook's metric (Chapter 9)" are
internal).  A chapter or section of any other work that these rules do not
recognise is written in lower case ("chapter 5 of Weinberg's book"), which
is never scanned.  Every other reference is INTERNAL: "Chapter N" must name
an existing chapter and "Section N.M" an existing section; a chapter
reference with a dotted number, or a section reference without exactly one
dot, is an error.  With --allow-missing a reference into a planned chapter
that does not exist yet is PENDING (reported, not an error).
--list-references prints every reference with its classification, so that
the external ones can be audited.

Prints problem=..., missing_chapter=..., measurement_<name>=<value>,
check_<name>=true|false, check_count, failed_check_count, the output path,
bytes and sha256, and a last line textbook_assembly=OK or FAILED.  Exit code 0
when every check passed, 1 when a check failed, 2 on a usage error.
"""

from __future__ import annotations

import argparse
import bisect
import dataclasses
import hashlib
import re
import sys
from pathlib import Path

try:
    from scripts import build_dissertation_tex
except ModuleNotFoundError:
    import build_dissertation_tex


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIRECTORY_RELATIVE = Path("provenance/textbook/chapters")
OUTPUT_RELATIVE = Path("provenance/DIRAC16COMPLEX_TEXTBOOK.md")
DRAFT_OUTPUT_RELATIVE = Path("build/textbook/DIRAC16COMPLEX_TEXTBOOK.md")

TITLE = "dirac16complex: a textbook for students"
SUBTITLE = (
    "From school algebra to a 16-component spinor field in 4+4 dimensions: "
    "formalism, field equations, Kohn–Sham approximations, pairing "
    "theorems and open problems"
)
ABSTRACT = (
    "This book teaches, starting from school algebra and the calculus of one "
    "variable, everything that the dirac16complex project has set up, "
    "derived, proved and computed, and it says with equal care what the "
    "project has not established. The object of study is a field with "
    "sixteen complex components on an eight-dimensional space with four "
    "space-like and four time-like directions (signature (4,4), coordinates "
    "$x_0,\\dots,x_7$, time $x_4$), in two versions: dirac16complex, whose "
    "components are anticommuting (Grassmann) quantities, and "
    "dirac16complex00, whose components are ordinary commuting complex "
    "numbers. Part I builds the mathematics: vectors, matrices, complex "
    "numbers, indices, derivatives in several variables, metrics and "
    "signatures, Clifford algebras and spinors, split octonions, and curved "
    "space with its spin connection. Part II builds the field theory: "
    "Lagrangians, field equations, the energy–momentum tensor, kinetic and "
    "potential energy, pressure and equations of state in an arbitrary "
    "gravitational field, and canonical quantization, which in signature "
    "(4,4) leads to an indefinite (Krein) state space and to unstable modes "
    "along the extra times. Part III treats the primordial gravitational "
    "field of the author's notebook, the errors found in the notebook and "
    "their corrections, the numerical methods, and the numerical "
    "experiments on dark matter and dark energy. Part IV introduces density "
    "functional theory from zero and derives the Kohn–Sham approximation "
    "that is used for both fields in the primordial field, with its ground "
    "and first excited states. Part V presents the exact pairing statements "
    "that relate a universe of mass $+M$ to one of mass $-M$, and then "
    "examines two questions without overstatement: whether the big bang "
    "creates universes in pairs, and whether this theory explains the "
    "excess of matter over antimatter. Every statement carries one of five "
    "labels (proved, computed, assumed, hypothesis, open) in an honesty "
    "ledger, every number is copied from a committed report of the "
    "repository, and every proof is paired with the exact machine check "
    "that verifies it where one exists. The pairing statements make the "
    "creation of universe pairs consistent with the conservation laws, but "
    "no creation process, rate or amplitude is derived, and the theory as "
    "built does not contain the ingredients that an explanation of the "
    "matter–antimatter asymmetry requires; both points are stated as open "
    "problems."
)

# The chapter plan of TEXTBOOK_SPEC.md section 3 (ASCII, for the report only).
PLANNED_CHAPTERS: dict[int, str] = {
    0: "How to read this book; the honesty ledger",
    1: "Mathematical toolkit from zero",
    2: "Clifford algebras and spinors from zero",
    3: "Split octonions and the notebook's construction",
    4: "Curved space from zero",
    5: "Classical field theory from zero",
    6: "The two fields and their Lagrangians",
    7: "Field equations, energy-momentum tensor and equations of state",
    8: "Canonical quantization in 4+4",
    9: "The primordial gravitational field of the notebook",
    10: "Solving differential equations on a computer from zero",
    11: "The dark-sector experiments EXP-1 to EXP-5",
    12: "Many-body quantum mechanics and DFT from zero",
    13: "The Kohn-Sham approximation for dirac16complex",
    14: "The Kohn-Sham approximation for dirac16complex00",
    15: "The pairing theorems T1 to T3",
    16: "Does the big bang create universes in pairs?",
    17: "Matter and antimatter",
    18: "Open problems and how a student could attack them",
    19: "Reproducing everything",
    20: "Glossary and index of verifier checks",
}

FILE_NAME_PATTERN = re.compile(r"(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$")
CHAPTER_HEADING_PATTERN = re.compile(r"(0|[1-9]\d*)\. (\S.*)")
SECTION_HEADING_PATTERN = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*) (\S.*)")

REFERENCE_KEYWORD = re.compile(r"\b(Chapters|Chapter|Sections|Section)\b")
REFERENCE_GAP = re.compile(r"[ \t]*(?:\n[ \t]*)?")
REFERENCE_NUMBER = re.compile(r"\d+(?:\.\d+)*")
LIST_SEPARATOR = re.compile(
    r",[ \t]*(?:and|or)[ \t]+|,[ \t]*|[ \t]+(?:and|or|to)[ \t]+|[ \t]*[-–][ \t]*"
)
RANGE_SEPARATOR = re.compile(r"[ \t]+to[ \t]+|[ \t]*[-–][ \t]*")
SENTENCE_BOUNDARY = re.compile(r"[.;:!?](?=\s)|\n[ \t]*\n")
AFTER_BOUNDARY = re.compile(r"[,.;:!?](?=\s)|\n[ \t]*\n")
EXTERNAL_MARKER = re.compile(
    r"DIRAC16COMPLEX|provenance/|handoff/|artifacts/|scripts/|studies/|"
    r"wolfram/|notebooks/|\.md\b|\.tex\b|\.pdf\b|\.json\b|\.nb\b|\.wl\b|"
    r"SPEC|CONTRACT|HANDOFF|README|GUIDE|[Gg]uides?\b|"
    r"[Dd]ocuments?\b|[Ss]pecifications?\b"
)
STAGE_NAME_AT_END = re.compile(r"Stage[- ]?\d+[a-z]*[ \t]*,?[ \t]*$")
STAGE_NAME_AT_START = re.compile(r"(?:the[ \t]+)?Stage[- ]?\d+")
AFTER_PREPOSITION = re.compile(r"\s+(?:of|in|from)\s+")
THIS_BOOK = re.compile(r"\bthis (?:book|chapter)\b")
LINE_NUMBER_IN_MESSAGE = re.compile(r"(?<![A-Za-z])line (\d+)")

COMMON_CHECKS = (
    "chapterFileNames",
    "chapterNumbersUnique",
    "chapterNumbersInPlan",
    "chapterEncoding",
    "chapterHeadings",
    "headingLevels",
    "sectionNumbers",
    "sectionNumbersUnique",
    "crossReferencesResolve",
    "markdownConvertible",
)
STRICT_CHECKS = ("chapterNumbersConsecutive", "allPlannedChaptersPresent")


@dataclasses.dataclass
class Problem:
    check: str
    location: str
    message: str


@dataclasses.dataclass
class Section:
    chapter: int
    number: int
    title: str
    location: str


@dataclasses.dataclass
class Chapter:
    number: int
    path: Path
    display: str
    title: str = ""
    lines: list[str] = dataclasses.field(default_factory=list)
    sections: list[Section] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Reference:
    location: str
    kind: str
    target: str
    status: str
    text: str


@dataclasses.dataclass
class Assembly:
    checks: dict[str, bool]
    problems: list[Problem]
    chapters: list[Chapter]
    missing: list[int]
    references: list[Reference]
    text: str


def display_path(path: Path, root: Path) -> str:
    """Repository-relative POSIX path when possible, else absolute POSIX."""
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def read_chapter_text(
    raw: bytes, display: str, problems: list[Problem]
) -> str | None:
    """Decode one chapter; record chapterEncoding problems."""
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(
            Problem("chapterEncoding", display, "starts with a UTF-8 byte-order mark")
        )
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        problems.append(
            Problem("chapterEncoding", display, f"is not UTF-8 ({error})")
        )
        return None
    if "\r" in text:
        line = text[: text.index("\r")].count("\n") + 1
        problems.append(
            Problem(
                "chapterEncoding",
                f"{display}:{line}",
                "contains a CR character (use LF line endings)",
            )
        )
        return None
    if not text.strip():
        problems.append(Problem("chapterEncoding", display, "is empty"))
        return None
    return text


def blank_out(line: str) -> str:
    return " " * len(line)


def prose_mask(lines: list[str]) -> str:
    """The chapter text with fenced code, display math, inline math and code
    spans replaced by spaces (same length, newlines kept), so that offsets in
    the mask are offsets in the original text."""
    kept: list[str] = []
    in_fence = False
    in_display = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            kept.append(blank_out(line))
        elif in_fence:
            kept.append(blank_out(line))
        elif stripped == "$$":
            in_display = not in_display
            kept.append(blank_out(line))
        elif in_display:
            kept.append(blank_out(line))
        else:
            kept.append(line)
    text = "\n".join(kept)
    masked = list(text)
    paragraph_ends = [match.start() for match in re.finditer(r"\n[ \t]*\n", text)]
    paragraph_ends.append(len(text))
    index = 0
    while index < len(text):
        character = text[index]
        if character in "`$":
            limit = paragraph_ends[bisect.bisect_right(paragraph_ends, index)]
            end = text.find(character, index + 1, limit)
            if end >= 0:
                for position in range(index, end + 1):
                    if masked[position] != "\n":
                        masked[position] = " "
                index = end + 1
                continue
        index += 1
    return "".join(masked)


def structural_lines(lines: list[str]):
    """Yield (line_number, stripped) for lines outside fenced code and
    display math, as build_dissertation_tex.convert() sees them."""
    in_fence = False
    in_display = False
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped == "$$":
            in_display = not in_display
            continue
        if in_display:
            continue
        yield number, stripped


def scan_headings(chapter: Chapter, problems: list[Problem]) -> None:
    """Check the chapter heading, the heading levels and the section numbers;
    record the sections of the chapter."""
    first_line = next(
        (index + 1 for index, line in enumerate(chapter.lines) if line.strip()),
        None,
    )
    if first_line is None:
        problems.append(
            Problem("chapterHeadings", chapter.display, "has no heading")
        )
        return
    first = chapter.lines[first_line - 1].strip()
    heading = HEADING_PATTERN.match(first)
    chapter_heading = (
        CHAPTER_HEADING_PATTERN.fullmatch(heading.group(2))
        if heading and len(heading.group(1)) == 2
        else None
    )
    if chapter_heading is None:
        problems.append(
            Problem(
                "chapterHeadings",
                f"{chapter.display}:{first_line}",
                f"the first line must be '## {chapter.number}. Title', "
                f"found {first[:60]!r}",
            )
        )
    else:
        if int(chapter_heading.group(1)) != chapter.number:
            problems.append(
                Problem(
                    "chapterHeadings",
                    f"{chapter.display}:{first_line}",
                    f"heading number {chapter_heading.group(1)} does not "
                    f"match the file number {chapter.number:02d}",
                )
            )
        chapter.title = chapter_heading.group(2).strip()
    expected_section = 1
    for number, stripped in structural_lines(chapter.lines):
        location = f"{chapter.display}:{number}"
        if number == first_line and chapter_heading is not None:
            continue
        heading = HEADING_PATTERN.match(stripped)
        if heading is None:
            continue
        level = len(heading.group(1))
        text = heading.group(2)
        if level == 1:
            problems.append(
                Problem(
                    "headingLevels",
                    location,
                    "level-1 heading; the assembler adds the book title",
                )
            )
        elif level == 2:
            problems.append(
                Problem(
                    "chapterHeadings",
                    location,
                    "a second level-2 heading; a chapter has exactly one",
                )
            )
        elif level > 3:
            problems.append(
                Problem(
                    "headingLevels",
                    location,
                    f"level-{level} heading; the deepest allowed level is '### '",
                )
            )
        else:
            section = SECTION_HEADING_PATTERN.fullmatch(text)
            if section is None:
                problems.append(
                    Problem(
                        "sectionNumbers",
                        location,
                        f"section heading must read '### {chapter.number}.M Title',"
                        f" found {stripped[:60]!r}",
                    )
                )
                continue
            chapter_number = int(section.group(1))
            section_number = int(section.group(2))
            if chapter_number != chapter.number:
                problems.append(
                    Problem(
                        "sectionNumbers",
                        location,
                        f"section {chapter_number}.{section_number} lies in "
                        f"chapter {chapter.number}",
                    )
                )
            elif section_number != expected_section:
                problems.append(
                    Problem(
                        "sectionNumbers",
                        location,
                        f"section {chapter_number}.{section_number} where "
                        f"{chapter.number}.{expected_section} was expected "
                        "(sections are numbered 1, 2, 3, ... in order)",
                    )
                )
            if chapter_number == chapter.number:
                expected_section = section_number + 1
            chapter.sections.append(
                Section(
                    chapter_number,
                    section_number,
                    section.group(3).strip(),
                    location,
                )
            )


def line_starts(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))
    return starts


def is_external(text: str, start: int, end: int, base: str) -> bool:
    """Rules (a), (b) and (c) of the module docstring."""
    before = text[max(0, start - 120):start]
    boundaries = list(SENTENCE_BOUNDARY.finditer(before))
    if boundaries:
        before = before[boundaries[-1].end():]
    before = THIS_BOOK.sub(" ", before)
    for token in reversed(before.split()):
        if not token.strip("()[]*,`'\""):
            continue
        if EXTERNAL_MARKER.search(token):
            return True
        break
    if base == "Section" and STAGE_NAME_AT_END.search(before.replace("(", " ")):
        return True
    after = text[end:end + 120]
    preposition = AFTER_PREPOSITION.match(after)
    if preposition:
        rest = after[preposition.end():]
        cut = AFTER_BOUNDARY.search(rest)
        if cut:
            rest = rest[:cut.start()]
        rest = THIS_BOOK.sub(" ", rest)
        if EXTERNAL_MARKER.search(rest) or STAGE_NAME_AT_START.match(
            rest.lstrip("`( ")
        ):
            return True
    return False


def expand_targets(
    items: list[tuple[str, bool]], base: str
) -> list[tuple[str, str | None]]:
    """(target, error message or None) for every number of one reference;
    a range whose two ends lie in one chapter is expanded."""
    targets: list[tuple[str, str | None]] = []
    previous: list[int] | None = None
    for number, is_range in items:
        parts = [int(part) for part in number.split(".")]
        wanted = 1 if base == "Chapter" else 2
        if len(parts) != wanted:
            message = (
                "a chapter reference takes a whole number (write 'Section N.M' "
                "for a section)"
                if base == "Chapter"
                else "a section reference takes the form N.M (write "
                "'Chapter N' for a chapter)"
            )
            targets.append((number, message))
            previous = None
            continue
        if is_range and previous is not None:
            if base == "Chapter":
                targets.extend(
                    (str(value), None)
                    for value in range(previous[0] + 1, parts[0])
                )
            elif previous[0] == parts[0]:
                targets.extend(
                    (f"{parts[0]}.{value}", None)
                    for value in range(previous[1] + 1, parts[1])
                )
        targets.append((".".join(str(part) for part in parts), None))
        previous = parts
    return targets


def scan_references(
    chapter: Chapter,
    present: set[int],
    sections: dict[tuple[int, int], str],
    planned: set[int],
    allow_missing: bool,
    references: list[Reference],
    problems: list[Problem],
) -> None:
    text = "\n".join(chapter.lines)
    masked = prose_mask(chapter.lines)
    starts = line_starts(text)
    section_counts: dict[int, int] = {}
    for chapter_number, section_number in sections:
        section_counts[chapter_number] = max(
            section_counts.get(chapter_number, 0), section_number
        )
    for keyword in REFERENCE_KEYWORD.finditer(masked):
        kind = keyword.group(1)
        base = "Chapter" if kind.startswith("Chapter") else "Section"
        gap = REFERENCE_GAP.match(masked, keyword.end())
        if gap is None or gap.end() == keyword.end():
            continue
        first = REFERENCE_NUMBER.match(masked, gap.end())
        if first is None:
            continue
        items = [(first.group(), False)]
        end = first.end()
        if kind.endswith("s"):
            while True:
                separator = LIST_SEPARATOR.match(masked, end)
                if separator is None:
                    break
                following = REFERENCE_NUMBER.match(masked, separator.end())
                if following is None:
                    break
                items.append(
                    (
                        following.group(),
                        RANGE_SEPARATOR.fullmatch(separator.group()) is not None,
                    )
                )
                end = following.end()
        line = bisect.bisect_right(starts, keyword.start())
        location = f"{chapter.display}:{line}"
        matched = " ".join(text[keyword.start():end].split())
        if is_external(text, keyword.start(), end, base):
            references.append(
                Reference(
                    location,
                    base,
                    ",".join(number for number, _ in items),
                    "external",
                    matched,
                )
            )
            continue
        for target, message in expand_targets(items, base):
            status = "resolved"
            if message is not None:
                status = "unresolved"
            elif base == "Chapter":
                number = int(target)
                if number not in present:
                    if allow_missing and number in planned:
                        status = "pending"
                    else:
                        status = "unresolved"
                        message = f"chapter {number} does not exist"
            else:
                chapter_number, section_number = (
                    int(part) for part in target.split(".")
                )
                if (chapter_number, section_number) not in sections:
                    if (
                        chapter_number not in present
                        and allow_missing
                        and chapter_number in planned
                    ):
                        status = "pending"
                    else:
                        status = "unresolved"
                        if chapter_number in present:
                            last = section_counts.get(chapter_number, 0)
                            message = (
                                f"section {target} does not exist (chapter "
                                f"{chapter_number} has sections "
                                f"{chapter_number}.1 to {chapter_number}.{last})"
                            )
                        else:
                            message = (
                                f"section {target} lies in chapter "
                                f"{chapter_number}, which does not exist"
                            )
            references.append(Reference(location, base, target, status, matched))
            if status == "unresolved":
                problems.append(
                    Problem(
                        "crossReferencesResolve",
                        location,
                        f"{matched!r}: {message}",
                    )
                )


def translate_line_numbers(
    message: str, book_offsets: list[tuple[int, Chapter, int]]
) -> str:
    """Replace "line N" of the assembled book by the chapter file and line."""
    first_lines = [first for first, _, _ in book_offsets]

    def replace(match: re.Match[str]) -> str:
        book_line = int(match.group(1))
        index = bisect.bisect_right(first_lines, book_line) - 1
        if index < 0:
            return f"line {book_line} (title block)"
        first, chapter, removed = book_offsets[index]
        return (
            f"line {book_line} of the book "
            f"({chapter.display}:{book_line - first + 1 + removed})"
        )

    return LINE_NUMBER_IN_MESSAGE.sub(replace, message)


def title_block() -> list[str]:
    return ["# " + TITLE, "", "## " + SUBTITLE, "", "## Abstract", "", ABSTRACT]


def assemble(
    chapter_directory: Path,
    *,
    allow_missing: bool = False,
    planned: dict[int, str] | None = None,
    image_root: Path = REPOSITORY_ROOT,
    display_root: Path = REPOSITORY_ROOT,
    validate_markdown: bool = True,
) -> Assembly:
    """Check the chapter files of chapter_directory and assemble the book.

    planned: the chapter plan (default PLANNED_CHAPTERS); tests pass a
    smaller one.  image_root: the directory that figure paths are relative
    to.  display_root: paths in messages are written relative to it.
    """
    plan = PLANNED_CHAPTERS if planned is None else planned
    planned_numbers = sorted(plan)
    planned_set = set(planned_numbers)
    problems: list[Problem] = []
    directory_display = display_path(chapter_directory, display_root)
    chapters: list[Chapter] = []
    names = sorted(
        path.name
        for path in chapter_directory.iterdir()
        if path.is_file() and path.suffix == ".md"
    )
    if not names:
        problems.append(
            Problem("chapterFileNames", directory_display, "contains no .md file")
        )
    for name in names:
        path = chapter_directory / name
        display = display_path(path, display_root)
        match = FILE_NAME_PATTERN.fullmatch(name)
        if match is None:
            problems.append(
                Problem(
                    "chapterFileNames",
                    display,
                    "is not named NN-short-name.md (two digits, a hyphen, "
                    "lower-case ASCII letters and digits joined by single "
                    "hyphens)",
                )
            )
            continue
        chapter = Chapter(int(match.group(1)), path, display)
        text = read_chapter_text(path.read_bytes(), display, problems)
        if text is not None:
            chapter.lines = text.split("\n")
            if chapter.lines[-1] == "":
                chapter.lines.pop()
            scan_headings(chapter, problems)
        else:
            chapter.lines = []
        chapters.append(chapter)
    chapters.sort(key=lambda chapter: (chapter.number, chapter.path.name))

    by_number: dict[int, list[Chapter]] = {}
    for chapter in chapters:
        by_number.setdefault(chapter.number, []).append(chapter)
    for number, group in sorted(by_number.items()):
        if len(group) > 1:
            problems.append(
                Problem(
                    "chapterNumbersUnique",
                    ", ".join(chapter.display for chapter in group),
                    f"{len(group)} files share the chapter number {number:02d}",
                )
            )
    for chapter in chapters:
        if chapter.number not in planned_set:
            problems.append(
                Problem(
                    "chapterNumbersInPlan",
                    chapter.display,
                    f"chapter {chapter.number:02d} is not in the plan "
                    f"({planned_numbers[0]:02d} to {planned_numbers[-1]:02d})",
                )
            )
    present = set(by_number)
    missing = [number for number in planned_numbers if number not in present]
    if not allow_missing:
        top = max(present) if present else -1
        gaps = [number for number in range(0, top + 1) if number not in present]
        if not present or gaps:
            problems.append(
                Problem(
                    "chapterNumbersConsecutive",
                    directory_display,
                    "there is no chapter"
                    if not present
                    else "the chapter numbers skip "
                    + ", ".join(f"{number:02d}" for number in gaps),
                )
            )
        if missing:
            problems.append(
                Problem(
                    "allPlannedChaptersPresent",
                    directory_display,
                    "missing planned chapters: "
                    + ", ".join(f"{number:02d}" for number in missing),
                )
            )

    sections: dict[tuple[int, int], str] = {}
    for chapter in chapters:
        for section in chapter.sections:
            key = (section.chapter, section.number)
            if key in sections:
                problems.append(
                    Problem(
                        "sectionNumbersUnique",
                        section.location,
                        f"section {key[0]}.{key[1]} already occurs at "
                        f"{sections[key]}",
                    )
                )
            else:
                sections[key] = section.location

    references: list[Reference] = []
    for chapter in chapters:
        if chapter.lines:
            scan_references(
                chapter,
                present,
                sections,
                planned_set,
                allow_missing,
                references,
                problems,
            )

    lines = title_block()
    book_offsets: list[tuple[int, Chapter, int]] = []
    for chapter in chapters:
        body = list(chapter.lines)
        removed = 0
        while body and not body[0].strip():
            body.pop(0)
            removed += 1
        while body and not body[-1].strip():
            body.pop()
        if not body:
            continue
        lines.append("")
        book_offsets.append((len(lines) + 1, chapter, removed))
        lines.extend(body)
    text = "\n".join(lines) + "\n"

    if validate_markdown:
        try:
            build_dissertation_tex.convert(
                text,
                strip_heading_numbers=True,
                developer_layout=True,
                image_root=image_root,
            )
        except ValueError as error:
            problems.append(
                Problem(
                    "markdownConvertible",
                    "book",
                    translate_line_numbers(str(error), book_offsets),
                )
            )

    names_checked = COMMON_CHECKS + (() if allow_missing else STRICT_CHECKS)
    failed = {problem.check for problem in problems}
    checks = {name: name not in failed for name in names_checked}
    return Assembly(checks, problems, chapters, missing, references, text)


def parse_arguments(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the chapters and the assembly; write nothing",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help=(
            "accept missing planned chapters (reported), treat references "
            "into them as pending, and write the draft to "
            f"{DRAFT_OUTPUT_RELATIVE.as_posix()} unless --output is given"
        ),
    )
    parser.add_argument(
        "--verify-output",
        action="store_true",
        help=(
            "also require the existing output file to equal the assembly "
            "byte for byte (implies --check)"
        ),
    )
    parser.add_argument(
        "--list-references",
        action="store_true",
        help="print every reference with its classification",
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=REPOSITORY_ROOT,
        help="figure paths are relative to it; default paths lie under it",
    )
    parser.add_argument(
        "--chapters-directory",
        type=Path,
        help=f"default: <root>/{CHAPTER_DIRECTORY_RELATIVE.as_posix()}",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help=(
            f"default: <root>/{OUTPUT_RELATIVE.as_posix()} (with "
            f"--allow-missing: <root>/{DRAFT_OUTPUT_RELATIVE.as_posix()})"
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    arguments = parse_arguments(argv)
    root = arguments.repository_root.resolve()
    chapter_directory = (
        arguments.chapters_directory or root / CHAPTER_DIRECTORY_RELATIVE
    ).resolve()
    if arguments.output is not None:
        output = arguments.output.resolve()
    elif arguments.allow_missing:
        output = root / DRAFT_OUTPUT_RELATIVE
    else:
        output = root / OUTPUT_RELATIVE
    check_only = arguments.check or arguments.verify_output
    mode = "check" if check_only else "build"
    print(f"mode={mode}")
    print(f"allow_missing={'true' if arguments.allow_missing else 'false'}")
    print(f"chapter_directory={display_path(chapter_directory, root)}")
    if not chapter_directory.is_dir():
        print("usage_error=the chapter directory does not exist")
        print("textbook_assembly=FAILED")
        return 2

    assembly = assemble(
        chapter_directory,
        allow_missing=arguments.allow_missing,
        image_root=root,
        display_root=root,
    )
    for chapter in assembly.chapters:
        print(
            f"chapter={chapter.number:02d} file={chapter.display} "
            f"sections={len(chapter.sections)} lines={len(chapter.lines)}"
        )
    for number in assembly.missing:
        print(
            f"missing_chapter={number:02d} "
            f"{PLANNED_CHAPTERS.get(number, '(not in the plan)')}"
        )
    for reference in assembly.references:
        if arguments.list_references or reference.status in (
            "pending",
            "unresolved",
        ):
            print(
                f"reference={reference.status} {reference.location} "
                f"{reference.kind} {reference.target} [{reference.text}]"
            )
    for problem in assembly.problems:
        print(f"problem={problem.check} {problem.location}: {problem.message}")

    checks = dict(assembly.checks)
    written = False
    if not check_only:
        if all(checks.values()):
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(assembly.text.encode("utf-8"))
            written = True
        else:
            print("problem=outputWritten the output was not written because a check failed")
        checks["outputWritten"] = written
    if arguments.verify_output:
        up_to_date = (
            output.is_file()
            and output.read_bytes() == assembly.text.encode("utf-8")
        )
        if not up_to_date:
            print(
                "problem=outputUpToDate "
                f"{display_path(output, root)} differs from the assembly "
                "(run python scripts/build_textbook.py to rewrite it)"
            )
        checks["outputUpToDate"] = up_to_date

    statuses = [reference.status for reference in assembly.references]
    measurements = {
        "chapterCount": len(assembly.chapters),
        "sectionCount": sum(len(chapter.sections) for chapter in assembly.chapters),
        "missingChapters": ",".join(f"{number:02d}" for number in assembly.missing)
        or "none",
        "resolvedReferences": statuses.count("resolved"),
        "pendingReferences": statuses.count("pending"),
        "unresolvedReferences": statuses.count("unresolved"),
        "externalReferences": statuses.count("external"),
        "bookLines": assembly.text.count("\n"),
    }
    for name, value in measurements.items():
        print(f"measurement_{name}={value}")
    for name, value in checks.items():
        print(f"check_{name}={'true' if value else 'false'}")
    failed = sum(1 for value in checks.values() if not value)
    print(f"check_count={len(checks)}")
    print(f"failed_check_count={failed}")
    encoded = assembly.text.encode("utf-8")
    print(f"output={display_path(output, root)}")
    print(f"output_written={'true' if written else 'false'}")
    print(f"assembly_bytes={len(encoded)}")
    print(f"assembly_sha256={hashlib.sha256(encoded).hexdigest()}")
    print(f"textbook_assembly={'OK' if failed == 0 else 'FAILED'}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
