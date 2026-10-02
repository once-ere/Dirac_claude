#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Assemble the textbook "Universes in Pairs" and check it (TEXTBOOK_SPEC section 4).

Written 2026-10-02.  Input: the chapter files Revision/textbook/chapters/NN-short-name.md
(NN = 00 ... 23, a short name of lower-case ASCII letters and digits joined by single
hyphens) and the abstract Revision/textbook/chapters/abstract.md (paragraphs only).
Output: Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md, which is

    # Universes in Pairs
    ## A Deep-Dive Course on the dirac16complex Fields in the Author's 4+4 Primordial
       Universe, with a Complete Jupyter Notebook for Every Example      (one line)
    ## Abstract
    <the abstract>
    <chapter 00> <chapter 01> ... <chapter 23>

(TEXTBOOK_SPEC rule R1), one blank line between the parts, every notebook marker
<!-- NOTEBOOK NNx --> replaced by its two sections (render_notebook.py), UTF-8, LF line
endings and exactly one final newline.  The bytes depend only on the chapter files, the
abstract, the stored notebooks and their captions files, and these tools: two runs write
identical files.

Usage, from the repository root:

    python Revision/textbook/tools/assemble_textbook.py            # check, then write
    python Revision/textbook/tools/assemble_textbook.py --check    # check only; also
                                                     # requires the stored output to equal
                                                     # the assembly byte for byte
    python Revision/textbook/tools/assemble_textbook.py --allow-missing --output FILE
                                                     # a draft of the chapters so far

By default every planned chapter 00 ... 23 must exist.  With --allow-missing the
chapters that exist are assembled, a missing chapter is reported (missing_chapter=NN),
references into missing chapters are PENDING (reported, not errors), and the output must
be given with --output (the official file is never replaced by a draft).

Checks (each printed as check_<name>=true|false; any false fails the run):
  chapterFiles             file names NN-short-name.md, NN unique and planned (00..23);
                           every planned chapter present (unless --allow-missing)
  chapterEncoding          UTF-8 without BOM, LF only, not empty, one final newline
  chapterHeadings          the first non-blank line is "## N. Title" with N = int(NN), the
                           only level-2 heading of the chapter; no "# " heading and no
                           heading deeper than "### "
  sectionNumbers           after the notebooks are expanded every "### " heading reads
                           "### N.M Title" with M = 1, 2, 3, ... in order (so the
                           authored numbers equal the numbers LaTeX prints)
  notebookMarkers          every marker resolves to one stored, executed notebook of the
                           same chapter with its PROVENANCE.md; no notebook is placed
                           twice; every stored notebook is placed (unless
                           --allow-missing, except for the chapters named by --only);
                           no other HTML comment
  runInstructionsFirst     every "Notebook X: complete text" section is directly preceded
                           by "How to run Notebook X" and directly followed by "Line-by-
                           line walk-through of Notebook X"
  crossReferencesResolve   "Chapter N", "Section N.M" (and lists and ranges) resolve
  forbiddenPhrases         no sentence says that complex conjugation is charge
                           conjugation (TEXTBOOK_SPEC rule R5)
  proseCharacters          outside fenced blocks and math no "--", "<<", ">>", "``" or
                           "''" (the PDF fonts print each pair as one other character,
                           also inside code spans)
  fencedLines              fenced code lines at most 89 characters wide (a non-ASCII
                           character counts twice: it is set in a wider font), no tabs
  figuresIncluded          every figure file exists; every PNG in Revision/textbook/figures
                           is shown in the book (unless --allow-missing, except for
                           the chapters named by --only)
  markdownConvertible      scripts/build_dissertation_tex.py converts the book with the
                           options of the PDF build (its line numbers are translated back
                           to chapter:line)
  outputWritten / outputUpToDate   the output was written / equals the assembly
Prints problem=..., pending_reference=..., missing_chapter=..., measurement_<name>=...,
check_<name>=..., and a last line textbook_assembly=OK or FAILED.  Exit code 0 when every
check passed, 1 when a check failed, 2 on a usage error.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
TEXTBOOK = TOOLS.parent
ROOT = TEXTBOOK.parent.parent
for _path in (TOOLS, ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import render_notebook  # noqa: E402
from scripts import build_dissertation_tex  # noqa: E402

CHAPTERS = TEXTBOOK / "chapters"
ABSTRACT = CHAPTERS / "abstract.md"
OUTPUT = TEXTBOOK / "UNIVERSES_IN_PAIRS_TEXTBOOK.md"
FIGURES = TEXTBOOK / "figures"
NOTEBOOKS = TEXTBOOK / "notebooks"
REGISTRY = ROOT / "Revision" / "pdf-specifications.json"
EDITION = "universes-in-pairs-textbook"
PLANNED = list(range(0, 24))
MAX_LINE = 89

TITLE = "Universes in Pairs"
SUBTITLE = ("A Deep-Dive Course on the dirac16complex Fields in the Author's 4+4 "
            "Primordial Universe, with a Complete Jupyter Notebook for Every Example")

FILE_NAME = re.compile(r"(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md")
HEADING = re.compile(r"^(#{1,6})\s+(.+)$")
CHAPTER_HEADING = re.compile(r"(0|[1-9]\d*)\. (\S.*)")
SECTION_HEADING = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*) (\S.*)")
NUMBER = r"\d+(?:\.\d+)*"
EN_DASH = chr(0x2013)  # a range may also be written with an en dash, "3.2" EN_DASH "3.4"
SEPARATOR = (r"(?:\s*,\s*and\s+|\s*,\s*|\s+and\s+|\s+to\s+|\s*-\s*|\s*" + EN_DASH
             + r"\s*)")
RANGE_SEPARATOR = re.compile(r"\s*(?:-|" + EN_DASH + r"|to)\s*")
REFERENCE = re.compile(
    rf"(?<![A-Za-z])(Chapters|Chapter|Sections|Section)\s+({NUMBER}(?:{SEPARATOR}"
    rf"{NUMBER})*)")
EXTERNAL_BEFORE = re.compile(
    r"(?:\.md|\.tex|\.pdf|\.json|\.py|\.nb|\.wl)\b|DIRAC16COMPLEX|SPEC\b|README|"
    r"HANDOFF|\b[Dd]ocuments?\b|\b[Ss]pecifications?\b|original textbook|"
    r"\bRevision/|provenance/|scripts/|studies/|artifacts/")
LIGATURES = ("--", "<<", ">>", "``", "''")
FORBIDDEN_PHRASES = [
    (re.compile(r"complex\s+conjugation\s+(?:is|equals|=|acts\s+as)\s+(?:the\s+|a\s+)?"
                r"charge\s+conjugation", re.IGNORECASE),
     "TEXTBOOK_SPEC R5: complex conjugation is never charge conjugation (for real "
     "fields it is the identity)"),
]
RUN_TITLE = re.compile(r"How to run Notebook (\d{2}[a-z])")
TEXT_TITLE = re.compile(r"Notebook (\d{2}[a-z]): complete text")
WALK_TITLE = "Line-by-line walk-through of Notebook {}"


@dataclass
class Chapter:
    number: int
    path: Path
    text: str = ""
    lines: list = field(default_factory=list)  # (line, origin) after expansion
    notebooks: list = field(default_factory=list)


@dataclass
class Result:
    checks: dict
    problems: list
    pending: list
    missing: list
    measurements: dict
    text: str
    origins: list


def display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path, problems: list[str]) -> str:
    data = path.read_bytes()
    label = display(path)
    if data.startswith(b"\xef\xbb\xbf"):
        problems.append(f"{label}: starts with a byte-order mark")
    if b"\r" in data:
        problems.append(f"{label}: contains CR characters (use LF line endings)")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        problems.append(f"{label}: not UTF-8 ({error})")
        return ""
    if not text.strip():
        problems.append(f"{label}: empty")
    elif not text.endswith("\n") or text.endswith("\n\n"):
        problems.append(f"{label}: must end with exactly one newline")
    return text.replace("\r\n", "\n")


def structural(lines: list[tuple[str, str]]):
    """Yield (index, line, origin) of the lines outside fenced code and display math."""
    in_code = in_math = False
    for index, (line, origin) in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped == "$$":
            in_math = not in_math
            continue
        if in_math:
            continue
        yield index, line, origin


def check_structure(chapter: Chapter, problems: list[str]) -> list[str]:
    """Headings, section numbers, marker neighbourhood; returns the section numbers."""
    sections: list[str] = []
    headings = [(i, line, origin, HEADING.match(line.strip()))
                for i, line, origin in structural(chapter.lines)]
    headings = [(i, line, origin, m) for i, line, origin, m in headings if m]
    first = next((line for line, _ in chapter.lines if line.strip()), "")
    match = HEADING.match(first.strip())
    chapter_match = CHAPTER_HEADING.fullmatch(match.group(2)) if match and len(
        match.group(1)) == 2 else None
    if chapter_match is None or int(chapter_match.group(1)) != chapter.number:
        problems.append(f"{display(chapter.path)}: the first line must be "
                        f"'## {chapter.number}. Title'")
    expected = 1
    titles: list[tuple[int, str, str]] = []
    for index, line, origin, heading in headings:
        level = len(heading.group(1))
        text = heading.group(2)
        if level == 1:
            problems.append(f"{origin}: a '# ' heading (the assembler adds the title)")
        elif level == 2 and line.strip() != first.strip():
            problems.append(f"{origin}: a second '## ' heading in the chapter")
        elif level > 3:
            problems.append(f"{origin}: a heading deeper than '### '")
        elif level == 3:
            section = SECTION_HEADING.fullmatch(text)
            if section is None or int(section.group(1)) != chapter.number:
                problems.append(f"{origin}: '{line.strip()}' must read "
                                f"'### {chapter.number}.M Title'")
                continue
            number = int(section.group(2))
            if number != expected:
                problems.append(f"{origin}: section {chapter.number}.{number} should be "
                                f"{chapter.number}.{expected} (sections are numbered 1, "
                                "2, 3, ... in order, counting the two sections that "
                                "every notebook marker adds)")
            expected = number + 1
            sections.append(f"{chapter.number}.{number}")
            titles.append((index, section.group(3), origin))
    for position, (index, title, origin) in enumerate(titles):
        text_match = TEXT_TITLE.fullmatch(title)
        if not text_match:
            continue
        identifier = text_match.group(1)
        before = titles[position - 1][1] if position else ""
        after = titles[position + 1][1] if position + 1 < len(titles) else ""
        if RUN_TITLE.fullmatch(before) is None or RUN_TITLE.fullmatch(before).group(
                1) != identifier:
            problems.append(f"{origin}: the text of Notebook {identifier} is not "
                            "directly preceded by its run instructions")
        if after != WALK_TITLE.format(identifier):
            problems.append(f"{display(chapter.path)}: the section after the marker of "
                            f"Notebook {identifier} must be '### N.M "
                            f"{WALK_TITLE.format(identifier)}' (found {after!r})")
    return sections


def prose_mask(line: str) -> str:
    """The line with inline math and code spans blanked out (positions kept)."""
    result = list(line)
    for pattern in (r"`[^`]*`", r"\$[^$]*\$"):
        for match in re.finditer(pattern, "".join(result)):
            for position in range(match.start(), match.end()):
                result[position] = " "
    return "".join(result)


def expand_list(kind: str, body: str) -> tuple[list[str], list[str]]:
    """(targets, errors) of the number list of one reference."""
    tokens = re.split(rf"({SEPARATOR})", body)
    numbers = tokens[0::2]
    separators = tokens[1::2]
    targets: list[str] = []
    errors: list[str] = []
    singular = kind.rstrip("s")
    for number in numbers:
        if singular == "Chapter" and "." in number:
            errors.append(f"'{kind} {number}' has a dotted chapter number")
        if singular == "Section" and number.count(".") != 1:
            errors.append(f"'{kind} {number}' is not a section number N.M")
    for position, number in enumerate(numbers):
        targets.append(number)
        if position < len(separators) and RANGE_SEPARATOR.fullmatch(
                separators[position].strip() or separators[position]):
            following = numbers[position + 1]
            if singular == "Section" and number.count(".") == 1 and \
                    following.count(".") == 1 and number.split(".")[0] == \
                    following.split(".")[0]:
                chapter = number.split(".")[0]
                for value in range(int(number.split(".")[1]) + 1,
                                   int(following.split(".")[1])):
                    targets.append(f"{chapter}.{value}")
            elif singular == "Chapter" and number.isdigit() and following.isdigit():
                for value in range(int(number) + 1, int(following)):
                    targets.append(str(value))
    return targets, errors


def scan_references(lines: list[tuple[str, str]], chapters: set[int],
                    sections: set[str], allow_missing: bool,
                    problems: list[str], pending: list[str]) -> int:
    count = 0
    previous = ""
    for _index, line, origin in structural(lines):
        masked = prose_mask(line)
        if not line.strip():
            previous = ""
            continue
        for match in REFERENCE.finditer(masked):
            kind, body = match.group(1), match.group(2).rstrip(" ,.-")
            before = (previous + " " + masked[:match.start()])[-160:]
            sentence = re.split(r"[.;:!?]\s", before)[-1]
            after = masked[match.end():match.end() + 120]
            if EXTERNAL_BEFORE.search(sentence) or (
                    re.match(r"\s+(?:of|in|from)\s+", after)
                    and EXTERNAL_BEFORE.search(re.split(r"[,.;:!?]\s", after)[0])):
                continue
            targets, errors = expand_list(kind, body)
            for error in errors:
                problems.append(f"{origin}: {error}")
            for target in targets:
                count += 1
                if kind.startswith("Chapter"):
                    if not target.isdigit():
                        continue
                    number = int(target)
                    if number in chapters:
                        continue
                    if allow_missing and number in PLANNED:
                        pending.append(f"{origin}: Chapter {number}")
                    else:
                        problems.append(f"{origin}: 'Chapter {number}' does not exist")
                else:
                    if target in sections:
                        continue
                    chapter_number = int(target.split(".")[0])
                    if allow_missing and chapter_number in PLANNED and \
                            chapter_number not in chapters:
                        pending.append(f"{origin}: Section {target}")
                    else:
                        problems.append(f"{origin}: 'Section {target}' does not exist")
        previous = masked
    return count


def chapter_files(only: list[int] | None, problems: list[str]) -> list[Chapter]:
    chapters: dict[int, Chapter] = {}
    for path in sorted(CHAPTERS.glob("*.md")):
        if path == ABSTRACT:
            continue
        match = FILE_NAME.fullmatch(path.name)
        if match is None:
            problems.append(f"{display(path)}: not named NN-short-name.md")
            continue
        number = int(match.group(1))
        if number not in PLANNED:
            problems.append(f"{display(path)}: chapter {number} is not planned (00..23)")
            continue
        if number in chapters:
            problems.append(f"{display(path)}: a second file of chapter {number}")
            continue
        if only is None or number in only:
            chapters[number] = Chapter(number, path)
    return [chapters[n] for n in sorted(chapters)]


def title_block(abstract: str) -> list[tuple[str, str]]:
    lines = [(f"# {TITLE}", "title"), ("", "title"), (f"## {SUBTITLE}", "title"),
             ("", "title"), ("## Abstract", "title"), ("", "title")]
    for number, line in enumerate(abstract.rstrip("\n").split("\n"), 1):
        lines.append((line, f"{display(ABSTRACT)}:{number}"))
    return lines


def assemble(only: list[int] | None = None, allow_missing: bool = False,
             placeholders: bool = False) -> Result:
    """Assemble and check.  only: the chapter numbers to include (None: all files);
    placeholders: add an empty section for every chapter before the first one included
    (so that a single chapter keeps its number in a test build)."""
    problems: list[str] = []
    pending: list[str] = []
    checks: dict[str, bool] = {}
    measurements: dict[str, object] = {}

    count = len(problems)
    chapters = chapter_files(only, problems)
    present = [c.number for c in chapters]
    wanted = PLANNED if only is None else sorted(only)
    missing = [n for n in wanted if n not in present]
    if missing and not allow_missing:
        problems += [f"chapter {n:02d} is missing" for n in missing]
    checks["chapterFiles"] = len(problems) == count

    count = len(problems)
    abstract = read_text(ABSTRACT, problems) if ABSTRACT.is_file() else ""
    if not ABSTRACT.is_file():
        problems.append(f"{display(ABSTRACT)} does not exist")
    for line in abstract.split("\n"):
        if HEADING.match(line.strip()):
            problems.append(f"{display(ABSTRACT)}: the abstract holds no heading")
    for chapter in chapters:
        chapter.text = read_text(chapter.path, problems)
    checks["chapterEncoding"] = len(problems) == count

    marker_problems: list[str] = []
    for chapter in chapters:
        chapter.lines, chapter.notebooks, found = render_notebook.expand_markers(
            chapter.text.rstrip("\n"), chapter.number, display(chapter.path))
        marker_problems += found
        for identifier in chapter.notebooks:
            if int(identifier[:2]) != chapter.number:
                marker_problems.append(f"{display(chapter.path)}: Notebook {identifier} "
                                       "belongs to another chapter")
            stored = sorted(NOTEBOOKS.glob(f"{identifier}_*.ipynb"))
            for path in stored:
                provenance = path.with_name(path.stem + ".PROVENANCE.md")
                if not provenance.is_file():
                    marker_problems.append(f"{display(provenance)} does not exist")
    placed = [i for c in chapters for i in c.notebooks]
    for identifier in sorted({i for i in placed if placed.count(i) > 1}):
        marker_problems.append(f"Notebook {identifier} is placed more than once")
    stored_ids = sorted(p.name[:3] for p in NOTEBOOKS.glob("*.ipynb"))
    unplaced = [i for i in stored_ids if i not in placed and (
        only is None or int(i[:2]) in only)]
    if unplaced and (not allow_missing or only is not None):
        marker_problems += [f"Notebook {i} is stored but placed in no chapter"
                            for i in unplaced]
    problems += marker_problems
    checks["notebookMarkers"] = not marker_problems

    heading_problems: list[str] = []
    section_problems: list[str] = []
    order_problems: list[str] = []
    sections: set[str] = set()
    for chapter in chapters:
        found: list[str] = []
        numbers = check_structure(chapter, found)
        sections.update(numbers)
        for problem in found:
            if "section" in problem and "should be" in problem or "must read '###" \
                    in problem:
                section_problems.append(problem)
            elif "preceded" in problem or "walk-through" in problem:
                order_problems.append(problem)
            else:
                heading_problems.append(problem)
    problems += heading_problems + section_problems + order_problems
    checks["chapterHeadings"] = not heading_problems
    checks["sectionNumbers"] = not section_problems
    checks["runInstructionsFirst"] = not order_problems

    lines = title_block(abstract)
    if placeholders and chapters:
        for number in range(0, chapters[0].number):
            lines += [("", "placeholder"),
                      (f"## {number}. (chapter {number} is not part of this test build)",
                       "placeholder"), ("", "placeholder"),
                      ("This test build contains one chapter only.", "placeholder")]
    for chapter in chapters:
        lines.append(("", "separator"))
        lines += chapter.lines
    while lines and not lines[-1][0].strip():
        lines.pop()

    count = len(problems)
    reference_count = scan_references(lines, set(present), sections, allow_missing,
                                      problems, pending)
    checks["crossReferencesResolve"] = len(problems) == count

    count = len(problems)
    for line, origin in lines:
        for pattern, reason in FORBIDDEN_PHRASES:
            if pattern.search(line):
                problems.append(f"{origin}: {reason}")
    checks["forbiddenPhrases"] = len(problems) == count

    count = len(problems)
    for _index, line, origin in structural(lines):
        if build_dissertation_tex.is_table_separator(line) and line.strip().startswith(
                "|"):
            continue  # the row | --- | --- | under a table header
        prose = re.sub(r"\$[^$]*\$", " ", line)  # math may hold any characters
        for sequence in LIGATURES:
            if sequence in prose:
                problems.append(f"{origin}: {sequence!r} outside a fenced block prints "
                                "as one other character (a dash, a guillemet or a curly "
                                "quote), also inside `code`; put commands with -- into a "
                                "fenced block, write a dash as the character U+2013 "
                                "or U+2014")
    checks["proseCharacters"] = len(problems) == count

    count = len(problems)
    fenced_lines = 0
    in_code = False
    for line, origin in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            fenced_lines += 1
            # A non-ASCII (math) character is set in a wider font than the typewriter
            # characters: tested 2026-10-02, 20 Greek letters + 69 ASCII fit, 20 + 49
            # more do not.  So each one counts twice.
            width = len(line) + sum(1 for c in line if ord(c) > 127)
            if width > MAX_LINE or "\t" in line:
                problems.append(f"{origin}: fenced line of width {width} (characters, "
                                "non-ASCII ones counted twice; at most 89) or with a tab")
    checks["fencedLines"] = len(problems) == count

    text = "\n".join(line for line, _ in lines) + "\n"
    count = len(problems)
    figure_paths = build_dissertation_tex.figure_paths(text)
    for path in figure_paths:
        if not (ROOT / path).is_file():
            problems.append(f"figure {path} does not exist")
    shown = {p.rsplit("/", 1)[-1] for p in figure_paths}
    orphans = sorted(p.name for p in FIGURES.glob("*.png") if p.name not in shown and (
        only is None or int(p.name[:2]) in only))
    if orphans and (not allow_missing or only is not None):
        problems += [f"figure {name} is in Revision/textbook/figures but not in the book"
                     for name in orphans]
    checks["figuresIncluded"] = len(problems) == count

    count = len(problems)
    try:
        build_dissertation_tex.convert(text, strip_heading_numbers=True,
                                       developer_layout=True, image_root=ROOT,
                                       sections_from_zero=True)
    except ValueError as error:
        message = str(error)
        match = re.search(r"(?<![A-Za-z])line (\d+)", message)
        if match and 0 < int(match.group(1)) <= len(lines):
            origin = lines[int(match.group(1)) - 1][1]
            message = f"{origin}: {message}"
        problems.append(f"the PDF builder rejects the book: {message}")
    checks["markdownConvertible"] = len(problems) == count

    measurements.update({
        "chapters": len(chapters),
        "sections": len(sections),
        "notebooks": len(placed),
        "figures": len(figure_paths),
        "references": reference_count,
        "fencedLines": fenced_lines,
        "lines": len(lines),
        "bytes": len(text.encode("utf-8")),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    })
    return Result(checks, problems, pending, missing, measurements, text, lines)


def registered_pages() -> str:
    try:
        entry = json.loads(REGISTRY.read_text(encoding="utf-8")).get(EDITION)
    except (OSError, ValueError):
        return "unknown"
    if not entry:
        return "not registered"
    pdf = ROOT / entry["path"]
    if pdf.is_file() and hashlib.sha256(pdf.read_bytes()).hexdigest() == entry["sha256"]:
        return str(entry["pages"])
    return "registered PDF differs from the stored PDF"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="check only")
    parser.add_argument("--allow-missing", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--only", type=int, nargs="+", metavar="NN",
                        help="assemble only these chapters (implies --allow-missing)")
    arguments = parser.parse_args(argv)
    allow_missing = arguments.allow_missing or arguments.only is not None
    if allow_missing and not arguments.check and arguments.output is None:
        parser.error("a draft (--allow-missing or --only) needs --output FILE")
    if arguments.output is not None and arguments.output.resolve() == OUTPUT.resolve() \
            and allow_missing:
        parser.error("a draft must not replace the official book")
    result = assemble(arguments.only, allow_missing)
    output = (arguments.output or OUTPUT).resolve()
    if arguments.check:
        if not allow_missing:
            result.checks["outputUpToDate"] = output.is_file() and \
                output.read_bytes() == result.text.encode("utf-8")
            if not result.checks["outputUpToDate"]:
                result.problems.append(f"{display(output)} differs from the assembly")
    else:
        ok = all(result.checks.values())
        if ok:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(result.text.encode("utf-8"))
        result.checks["outputWritten"] = ok
    for number in result.missing:
        print(f"missing_chapter={number:02d}")
    for item in result.pending:
        print(f"pending_reference={item}")
    for problem in result.problems:
        print(f"problem={problem}")
    for name, value in result.measurements.items():
        print(f"measurement_{name}={value}")
    print(f"measurement_pages={registered_pages()}")
    failed = [name for name, value in result.checks.items() if not value]
    for name, value in result.checks.items():
        print(f"check_{name}={str(value).lower()}")
    print(f"check_count={len(result.checks)}")
    print(f"failed_check_count={len(failed)}")
    print(f"output={display(output)}")
    print(f"textbook_assembly={'OK' if not failed else 'FAILED'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
