#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Render an executed notebook as the book's Markdown (TEXTBOOK_SPEC section 4).

Written 2026-10-02 for the textbook "Universes in Pairs".  A chapter places a notebook
with a marker line

    <!-- NOTEBOOK 03a -->

(exactly this text on its own line; the id is two digits and a letter).  The marker is
replaced by two sections that continue the chapter's "### N.M" numbering: if the last
section before the marker is "### 3.4 ...", the marker becomes

    ### 3.5 How to run Notebook 03a       the complete run instructions
                                          (run_instructions.book_markdown)
    ### 3.6 Notebook 03a: complete text   every cell in order: a markdown cell as a
                                          fenced text block after the label "Text cell:",
                                          a code cell as a fenced python block after
                                          "In [k]:", its printed text as fenced text
                                          blocks after "Out [k]:", and each figure it
                                          saved as a book figure line whose caption is
                                          the caption from the sidecar
                                          Revision/textbook/figures/03a.captions.json

and the chapter's next section must be "### 3.7 Line-by-line walk-through of
Notebook 03a" (the assembler checks this).  The notebook is the stored, executed file
Revision/textbook/notebooks/03a_<short>.ipynb; nothing is executed here.

Command line (from the repository root):
    python Revision/textbook/tools/render_notebook.py NOTEBOOK.ipynb --chapter N
        --section M        prints the two sections, numbered N.M and N.(M+1)
    python Revision/textbook/tools/render_notebook.py --chapter-file CHAPTER.md
                           prints the chapter with every marker expanded
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import run_instructions  # noqa: E402

TEXTBOOK = TOOLS.parent
ROOT = TEXTBOOK.parent.parent
NOTEBOOKS = TEXTBOOK / "notebooks"
FIGURE_FOLDER = "Revision/textbook/figures"
MAX_LINE = 89
MARKER_PATTERN = re.compile(r"<!-- NOTEBOOK (\d{2}[a-z]) -->")
SECTION_PATTERN = re.compile(r"^### (\d+)\.(\d+) (\S.*)$")


class RenderError(Exception):
    """The notebook cannot be rendered (not executed, figure missing, ...)."""


def notebook_path(identifier: str) -> Path:
    """The stored notebook Revision/textbook/notebooks/<identifier>_*.ipynb."""
    matches = sorted(NOTEBOOKS.glob(f"{identifier}_*.ipynb"))
    if len(matches) != 1:
        raise RenderError(f"notebook {identifier}: expected one file "
                          f"{identifier}_*.ipynb in Revision/textbook/notebooks, found "
                          f"{[m.name for m in matches]}")
    return matches[0]


def _text(value) -> str:
    return "".join(value) if isinstance(value, list) else str(value)


def _output_parts(output) -> list[tuple[str, str]]:
    """[("text", text)] or [("figure", file name)] for one output."""
    kind = output["output_type"]
    if kind == "stream":
        return [("text", _text(output["text"]))]
    if kind in ("display_data", "execute_result"):
        data = output.get("data", {})
        if "image/png" in data:
            name = output.get("metadata", {}).get("textbook_figure")
            if not name:
                raise RenderError("a figure output without textbook_figure metadata")
            return [("figure", name)]
        if "text/plain" in data:
            return [("text", _text(data["text/plain"]))]
        return []
    if kind == "error":
        raise RenderError("the notebook holds an error output")
    return []


def _fenced(language: str, lines: list[str], where: str) -> list[str]:
    for line in lines:
        if len(line) > MAX_LINE or "\t" in line or line.lstrip().startswith("```"):
            raise RenderError(f"{where}: the line {line[:60]!r} breaks the rules of a "
                              "fenced block (at most 89 characters, no tab, no ```)")
    return [f"```{language}"] + lines + ["```", ""]


def render(path: Path, chapter: int, first_section: int) -> tuple[str, int]:
    """The two sections for the notebook at path, numbered chapter.first_section and
    chapter.(first_section + 1); returns (markdown, next free section number)."""
    notebook = json.loads(Path(path).read_text(encoding="utf-8"))
    try:
        facts = notebook["metadata"]["textbook"]["facts"]
    except KeyError:
        raise RenderError(f"{path}: no textbook facts in the metadata (build it with "
                          "nbkit)") from None
    identifier = facts["id"]
    nb_file = run_instructions.notebook_file(facts)
    if Path(path).name != f"{facts['name']}.ipynb":
        raise RenderError(f"{path}: the file name differs from FACTS['name']")
    caption_file = ROOT / FIGURE_FOLDER / f"{identifier}.captions.json"
    if not caption_file.is_file():
        raise RenderError(f"{caption_file.relative_to(ROOT).as_posix()} does not exist")
    captions = json.loads(caption_file.read_text(encoding="utf-8"))
    lines = [f"### {chapter}.{first_section} How to run Notebook {identifier}", ""]
    lines += run_instructions.book_markdown(facts).rstrip("\n").split("\n") + [""]
    lines += [f"### {chapter}.{first_section + 1} Notebook {identifier}: complete text",
              ""]
    lines += [
        f"This section prints the complete text of the notebook file `{nb_file}`: every "
        "cell in order, with the output that the stored, executed notebook holds. A text "
        "cell (Jupyter calls it a markdown cell) is printed in a frame after the label "
        "Text cell. A code cell is printed after the label In [k], where k is the number "
        "that Jupyter gives the cell when it runs it; the text that the cell prints "
        "follows after the label Out [k], and every figure that the cell draws follows "
        "as a figure with its caption.", ""]
    shown: list[str] = []
    for index, cell in enumerate(notebook["cells"], 1):
        source = _text(cell["source"])
        where = f"notebook {identifier} cell {index}"
        if cell["cell_type"] == "markdown":
            lines += ["**Text cell:**", ""]
            lines += _fenced("text", source.split("\n"), where)
            continue
        if cell["cell_type"] != "code":
            raise RenderError(f"{where}: unsupported cell type {cell['cell_type']}")
        count = cell.get("execution_count")
        if count is None:
            raise RenderError(f"{where}: the code cell was not executed")
        lines += [f"**In [{count}]:**", ""]
        lines += _fenced("python", source.split("\n"), where)
        pending: list[str] = []

        def flush() -> None:
            if any(line.strip() for line in pending):
                lines.extend([f"**Out [{count}]:**", ""])
                lines.extend(_fenced("text", pending, where))
            pending.clear()

        for output in cell.get("outputs", []):
            for kind, value in _output_parts(output):
                if kind == "text":
                    pending.extend(value.rstrip("\n").split("\n"))
                    continue
                flush()
                if value not in captions:
                    raise RenderError(f"{where}: figure {value} has no caption in "
                                      f"{caption_file.name}")
                if not (ROOT / FIGURE_FOLDER / value).is_file():
                    raise RenderError(f"{where}: figure file {value} does not exist")
                number = value.split("_")[1]
                lines += [f"![{captions[value]} (Notebook {identifier}, figure "
                          f"{number}.)]({FIGURE_FOLDER}/{value})", ""]
                shown.append(value)
        flush()
    if sorted(shown) != sorted(captions):
        raise RenderError(f"notebook {identifier}: the captions file lists "
                          f"{sorted(captions)} but the notebook shows {sorted(shown)}")
    return "\n".join(lines).rstrip("\n") + "\n", first_section + 2


def expand_markers(text: str, chapter: int, label: str = "chapter"
                   ) -> tuple[list[tuple[str, str]], list[str], list[str]]:
    """Expand every marker of a chapter.

    Returns (lines, notebooks, problems): lines is a list of (line, origin) where origin
    names the source ("<label>:<line number>" or "Notebook <id> (generated)"); notebooks
    lists the ids in order."""
    result: list[tuple[str, str]] = []
    notebooks: list[str] = []
    problems: list[str] = []
    last_section = 0
    in_code = False
    for number, line in enumerate(text.split("\n"), 1):
        origin = f"{label}:{number}"
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
        if not in_code:
            section = SECTION_PATTERN.match(line)
            if section and int(section.group(1)) == chapter:
                last_section = int(section.group(2))
            marker = MARKER_PATTERN.fullmatch(stripped)
            if marker:
                identifier = marker.group(1)
                if line != stripped:
                    problems.append(f"{origin}: the marker must start the line")
                try:
                    rendered, last = render(notebook_path(identifier), chapter,
                                            last_section + 1)
                except (RenderError, OSError, ValueError, KeyError) as error:
                    problems.append(f"{origin}: {error}")
                    result.append((line, origin))
                    continue
                last_section = last - 1
                notebooks.append(identifier)
                for generated in rendered.rstrip("\n").split("\n"):
                    result.append((generated, f"Notebook {identifier} (generated)"))
                continue
            if "<!--" in line:
                problems.append(f"{origin}: an HTML comment other than a notebook marker "
                                "(the PDF builder would print it as text)")
        result.append((line, origin))
    return result, notebooks, problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("notebook", type=Path, nargs="?")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--section", type=int)
    parser.add_argument("--chapter-file", type=Path)
    arguments = parser.parse_args(argv)
    if arguments.chapter_file:
        match = re.match(r"(\d{2})-", arguments.chapter_file.name)
        if not match:
            parser.error("the chapter file must be named NN-short-name.md")
        lines, _, problems = expand_markers(
            arguments.chapter_file.read_text(encoding="utf-8"), int(match.group(1)),
            arguments.chapter_file.name)
        sys.stdout.write("\n".join(line for line, _ in lines))
        for problem in problems:
            print(f"problem={problem}", file=sys.stderr)
        return 1 if problems else 0
    if arguments.notebook is None or arguments.chapter is None or \
            arguments.section is None:
        parser.error("give NOTEBOOK --chapter N --section M, or --chapter-file")
    try:
        text, _ = render(arguments.notebook, arguments.chapter, arguments.section)
    except RenderError as error:
        print(f"problem={error}", file=sys.stderr)
        return 1
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
