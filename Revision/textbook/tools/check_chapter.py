#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Test-build one chapter of the textbook alone (or the current book) as a PDF.

Written 2026-10-02 for the textbook "Universes in Pairs" (TEXTBOOK_SPEC section 4: "Each
chapter writer test-builds its chapter alone in scratch, with its notebooks expanded, in
verify mode until warning-free").  Steps:

 1. assemble_textbook.assemble() checks the chapter with every check of the assembler
    (references into other chapters are PENDING, not errors) and expands its notebook
    markers; for chapter N > 0 the test book starts with one placeholder section per
    earlier chapter, so that LaTeX numbers the chapter N as in the book;
 2. a scratch ROOT is made (default: a folder in the system's temporary folder; give
    --scratch to choose it) holding the test book Revision/textbook/<STEM>.md, a copy of
    every figure it shows, and a THROW-AWAY copy of the registry
    Revision/pdf-specifications.json (the repository's registry is never changed);
 3. scripts/build_provenance_pdf.py builds the PDF with the book's options
    (--developer-layout --number-sections-from-zero, --repository-root ROOT,
    --specifications <the copy>) twice: first with --register into the throw-away copy,
    then in VERIFY mode against it.  Each build compiles the .tex twice (into pdf-a and
    pdf-b) and requires both PDFs to be byte-identical; the verify build also requires
    its PDF to equal the first build's.  Every LaTeX warning (Overfull, Underfull, ...)
    fails the build and is printed as latex_warning=...

Usage, from the repository root:
    python Revision/textbook/tools/check_chapter.py Revision/textbook/chapters/03-x.md
        [--scratch DIR] [--date "October 2026"] [--keep]
    python Revision/textbook/tools/check_chapter.py --book [--scratch DIR] ...
        (the book of all chapters written so far, with the official stem
        UNIVERSES_IN_PAIRS_TEXTBOOK, still in scratch with a throw-away registry)

Prints problem=..., pending_reference=..., latex_warning=..., measurement_<name>=...,
and a last line chapter_check=OK or FAILED.  Exit code 0 when everything passed.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import assemble_textbook  # noqa: E402
from assemble_textbook import ROOT  # noqa: E402
from scripts import build_dissertation_tex  # noqa: E402

BUILDER = ROOT / "scripts" / "build_provenance_pdf.py"
REGISTRY = ROOT / "Revision" / "pdf-specifications.json"
DEFAULT_SCRATCH = Path(tempfile.gettempdir()) / "universes-in-pairs-check"
DEFAULT_DATE = "October 2026"


def build_pdf(markdown: Path, root: Path, registry: Path, date: str, register: bool,
              log: Path) -> tuple[int, list[str], dict[str, str]]:
    """Run scripts/build_provenance_pdf.py; (exit code, warnings, key=value lines)."""
    command = [sys.executable, str(BUILDER), str(markdown), "--developer-layout",
               "--number-sections-from-zero", "--repository-root", str(root),
               "--specifications", str(registry), "--date", date]
    if register:
        command.append("--register")
    completed = subprocess.run(command, cwd=root, capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
    log.write_text(completed.stdout + "\n" + completed.stderr, encoding="utf-8")
    warnings = [line.split("=", 1)[1] for line in completed.stdout.splitlines()
                if line.startswith("latex_warning=")]
    values = {}
    for line in completed.stdout.splitlines():
        if "=" in line and not line.startswith("latex_warning="):
            key, value = line.split("=", 1)
            values[key] = value
    if completed.returncode == 2 or "ERROR" in completed.stderr:
        warnings.append("builder error: " + completed.stderr.strip()[-2000:])
    return completed.returncode, warnings, values


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("chapter", type=Path, nargs="?")
    parser.add_argument("--book", action="store_true",
                        help="test-build all chapters written so far")
    parser.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH)
    parser.add_argument("--date", default=DEFAULT_DATE,
                        help=f"the date printed under the title (default {DEFAULT_DATE})")
    parser.add_argument("--keep", action="store_true",
                        help="keep an existing scratch folder (default: start afresh)")
    arguments = parser.parse_args(argv)
    if arguments.book == (arguments.chapter is not None):
        parser.error("give one chapter file, or --book")
    start = time.perf_counter()
    if arguments.book:
        result = assemble_textbook.assemble(None, allow_missing=True)
        stem = "UNIVERSES_IN_PAIRS_TEXTBOOK"
        label = "book"
    else:
        match = assemble_textbook.FILE_NAME.fullmatch(arguments.chapter.name)
        if match is None:
            parser.error("the chapter file must be named NN-short-name.md")
        number = int(match.group(1))
        if arguments.chapter.resolve().parent != assemble_textbook.CHAPTERS.resolve():
            parser.error("the chapter must lie in Revision/textbook/chapters/")
        result = assemble_textbook.assemble([number], allow_missing=True,
                                            placeholders=True)
        stem = f"UNIVERSES_IN_PAIRS_CHAPTER_{number:02d}"
        label = f"chapter_{number:02d}"
    for item in result.pending:
        print(f"pending_reference={item}")
    for problem in result.problems:
        print(f"problem={problem}")
    for name, value in result.checks.items():
        print(f"check_{name}={str(value).lower()}")
    for name, value in result.measurements.items():
        print(f"measurement_{name}={value}")
    if result.problems:
        print("chapter_check=FAILED")
        return 1

    root = arguments.scratch.resolve() / label
    if root.exists() and not arguments.keep:
        shutil.rmtree(root)
    markdown = root / "Revision" / "textbook" / f"{stem}.md"
    markdown.parent.mkdir(parents=True, exist_ok=True)
    markdown.write_bytes(result.text.encode("utf-8"))
    for figure in build_dissertation_tex.figure_paths(result.text):
        target = root / figure
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / figure, target)
    registry = root / "Revision" / "pdf-specifications.json"
    shutil.copyfile(REGISTRY, registry)
    edition = stem.lower().replace("_", "-")
    registry_data = json.loads(registry.read_text(encoding="utf-8"))
    registry_data.pop(edition, None)  # a throw-away copy: start without this edition
    registry.write_text(json.dumps(registry_data, indent=1) + "\n", encoding="utf-8",
                        newline="\n")
    logs = root / "logs"
    logs.mkdir(exist_ok=True)

    failed = False
    pages = sha = None
    for register in (True, False):
        mode = "register" if register else "verify"
        build_start = time.perf_counter()
        code, warnings, values = build_pdf(markdown, root, registry, arguments.date,
                                           register, logs / f"build-{mode}.log")
        print(f"measurement_{mode}_seconds={time.perf_counter() - build_start:.1f}")
        for warning in warnings:
            print(f"latex_warning={mode}: {warning}")
        print(f"measurement_{mode}_exit_code={code}")
        for key in ("failed_checks", "measurement_pageCount", "measurement_pdfSha256",
                    "measurement_stoppedAfter"):
            if key in values:
                print(f"{mode}_{key}={values[key]}")
        pages = values.get("measurement_pageCount", pages)
        if sha is not None and values.get("measurement_pdfSha256") not in (None, sha):
            print("problem=the verify build differs from the first build")
            failed = True
        sha = values.get("measurement_pdfSha256", sha)
        if code != 0 or warnings:
            failed = True
            break
    pdf = markdown.with_suffix(".pdf")
    print(f"measurement_pages={pages}")
    print(f"measurement_pdf={pdf.as_posix() if pdf.is_file() else 'not built'}")
    print(f"measurement_pdf_sha256={sha}")
    print(f"measurement_logs={logs.as_posix()}")
    print(f"measurement_seconds={time.perf_counter() - start:.1f}")
    print(f"chapter_check={'FAILED' if failed else 'OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
