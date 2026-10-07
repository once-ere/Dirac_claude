#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""nbkit - build, execute, check and document the notebooks of the textbook.

Written 2026-10-02 for the textbook "Universes in Pairs" (Revision/textbook/TEXTBOOK_SPEC.md
sections 2 and 3 and rule R6).  Every notebook of the book is defined by a BUILDER, the
Python file Revision/textbook/notebooks/src/<name>.py, which holds two names:

  FACTS  the facts of the notebook (Revision/textbook/tools/run_instructions.py,
         FACTS_DOCUMENTATION, documents every key);
  CELLS  the list of its cells, made with md("...") (a markdown cell) and code("...")
         (a code cell).  The first cell is the markdown cell "## 1. What this notebook
         computes"; then come "## 3. The words used in this notebook", "## 4. The physical
         and mathematical situation", the computation, and as the last cell "## N. What
         this notebook showed".

nbkit inserts after the first cell the markdown cell "## 2. How to run this notebook"
(run_instructions.notebook_markdown) and the SET-UP code cell: the same instructions as
"#" comments (run_instructions.code_comments) followed by the standard preamble (imports,
the repository folder, and the helpers output_file, repository_file, say, save_figure,
check, report, all_checks_passed and, when the notebook needs Rust, rust_program).

Commands (from the repository root; BUILDER is the builder file):

  python Revision/textbook/tools/nbkit.py lint  BUILDER...
      the static rules only (FACTS, cell layout, line lengths, ASCII), no execution.
  python Revision/textbook/tools/nbkit.py build BUILDER... --date YYYY-MM-DD
      [--no-verify] [--scratch DIR]
      executes the notebook with nbclient (kernel python3, working folder
      Revision/textbook/notebooks, MPLBACKEND = the inline backend, PYTHONHASHSEED=0;
      the check run uses PYTHONHASHSEED=1, so hash-order dependence is caught),
      checks the outputs and the files written, normalises the notebook (fixed cell ids,
      no timing metadata, fixed kernelspec and language_info, sorted keys, LF) and writes
      Revision/textbook/notebooks/<name>.ipynb; then (unless --no-verify) runs the check
      below; then writes the provenance file <name>.PROVENANCE.md (TEXTBOOK_SPEC R6) with
      the given date as the date of the verified execution.
  python Revision/textbook/tools/nbkit.py check BUILDER... [--scratch DIR]
      [--record YYYY-MM-DD]          (also written: nbkit.py --check BUILDER...)
      executes the notebook again with every file written into a scratch folder
      (environment variable TEXTBOOK_OUTPUT_ROOT), and compares byte for byte: the
      notebook, every file written, and the provenance file regenerated from its own
      record; the repository is not changed.  With --record (and only when every
      comparison passed) the check result and its measurements are stored in the
      provenance file's record.

The notebook may also be run by a student in JupyterLab or with
"jupyter nbconvert --to notebook --execute --inplace"; nbkit is only the tool that builds
and checks the stored, executed copy.  Exit code 0 when everything passed, 1 otherwise,
2 on usage errors.  Every line nbkit prints is "<key>=<value>" or a problem line.
"""

from __future__ import annotations

import argparse
import base64
import copy
import datetime
import hashlib
import importlib.util
import json
import os
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import textwrap
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
if __name__ == "__main__":  # builders "import nbkit": give them this very module
    sys.modules.setdefault("nbkit", sys.modules["__main__"])

import run_instructions  # noqa: E402

TEXTBOOK = TOOLS.parent
ROOT = TEXTBOOK.parent.parent
NOTEBOOKS = TEXTBOOK / "notebooks"
SOURCES = NOTEBOOKS / "src"
FIGURE_FOLDER = "Revision/textbook/figures"
NOTEBOOK_FOLDER = "Revision/textbook/notebooks"

MAX_LINE = 89
MAX_OUTPUT_LINES = 80  # per code cell; long results belong in files
MAX_ASPECT = 1.25  # height / width of a figure; a taller one does not fit a book page
FIGURE_DPI = 150
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_FORBIDDEN_CHUNKS = {b"tEXt", b"zTXt", b"iTXt", b"tIME", b"eXIf"}
KERNEL_NAME = "python3"
INLINE_BACKEND = "module://matplotlib_inline.backend_inline"
KERNELSPEC = {"display_name": "Python 3 (ipykernel)", "language": "python",
              "name": KERNEL_NAME}
LANGUAGE_INFO = {
    "codemirror_mode": {"name": "ipython", "version": 3},
    "file_extension": ".py",
    "mimetype": "text/x-python",
    "name": "python",
    "nbconvert_exporter": "python",
    "pygments_lexer": "ipython3",
    "version": run_instructions.PYTHON_BUILT,
}
TEXT_MIME_TYPES = ("text/plain", "text/latex", "text/markdown")
SECTION_TITLES = {
    1: "What this notebook computes",
    2: "How to run this notebook",
    3: "The words used in this notebook",
    4: "The physical and mathematical situation",
}
LAST_SECTION_TITLE = "What this notebook showed"
SNAPSHOT_SKIP = {".git", "target", "__pycache__", ".ipynb_checkpoints", "node_modules",
                 "dirac-main", "vendor"}
SNAPSHOT_SKIP_TOP = {"build"}
ADDRESS_PATTERN = re.compile(r"\b0x[0-9a-fA-F]{6,}\b")
RECORD_PATTERN = re.compile(r"^<!-- nbkit-record (\{.*\}) -->$", re.MULTILINE)
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
DEFAULT_SCRATCH = Path(tempfile.gettempdir()) / "universes-in-pairs-nbkit"


class NotebookError(Exception):
    """A notebook breaks a rule, or its execution failed."""


# =========================================================================== cells

def _clean(text: str) -> str:
    return textwrap.dedent(text).strip("\n")


def md(text: str) -> dict:
    """A markdown cell (the text is dedented; leading and trailing blank lines dropped)."""
    return {"cell_type": "markdown", "source": _clean(text)}


def code(text: str) -> dict:
    """A code cell (the text is dedented; leading and trailing blank lines dropped)."""
    return {"cell_type": "code", "source": _clean(text)}


# =========================================================================== builder

def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def load_builder(path: Path) -> tuple[dict, list[dict], str]:
    """(FACTS, CELLS, builder path relative to the repository) of a builder file."""
    path = Path(path).resolve()
    if not path.is_file():
        raise NotebookError(f"builder {path} does not exist")
    try:
        builder_relative = relative(path)
    except ValueError:
        raise NotebookError(f"builder {path} is not inside the repository") from None
    if path.parent != SOURCES.resolve():
        raise NotebookError(f"builder {builder_relative} must lie in "
                            f"{relative(SOURCES)}/")
    name = "textbook_builder_" + re.sub(r"\W", "_", path.stem)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for key in ("FACTS", "CELLS"):
        if not hasattr(module, key):
            raise NotebookError(f"builder {builder_relative} does not define {key}")
    facts = copy.deepcopy(module.FACTS)
    cells = [dict(cell) for cell in module.CELLS]
    return facts, cells, builder_relative


# =========================================================================== preamble

PREAMBLE = r'''
# =======================================================================================
# THE SET-UP (the same in every notebook of this book; it computes no physics)
# =======================================================================================
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
@@RUST_IMPORTS@@
NOTEBOOK_ID = "@@ID@@"  # this notebook: chapter @@CHAPTER@@, example @@LETTER@@


def find_repository_root():
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")


# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))


def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))


matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})

FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")


def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")


PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")


def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")
@@RUST_HELPER@@

say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
'''

RUST_IMPORTS = '''import shutil  # finds the program cargo
import subprocess  # runs cargo and the Rust programs
'''

RUST_HELPER = r'''

def rust_program(manifest, binary):
    """Build the Rust program binary of the crate whose Cargo.toml is manifest (a
    repository path) with "cargo build --release" (about a second when it is up to date;
    minutes the first time) and return the path of the program."""
    if shutil.which("cargo") is None:
        raise FileNotFoundError(
            "cargo was not found: install Rust from https://rustup.rs, open a new "
            "terminal, activate the environment and start JupyterLab again")
    crate = (REPO / manifest).parent  # the folder that holds Cargo.toml
    completed = subprocess.run(
        ["cargo", "build", "--release", "--manifest-path", str(REPO / manifest),
         "--target-dir", str(crate / "target")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if completed.returncode != 0:  # show the end of cargo's error message
        print(completed.stderr[-3000:])
        raise RuntimeError(f"cargo build failed for {manifest}")
    for file_name in (binary, binary + ".exe"):  # Linux and macOS; Windows
        path = crate / "target" / "release" / file_name
        if path.is_file():
            say(f"Rust program {binary} is built and ready.")
            return path
    raise FileNotFoundError(f"cargo built {manifest} but {binary} is missing")'''


def preamble(facts: dict) -> str:
    rust = bool(facts["needs_rust"])
    text = PREAMBLE.strip("\n")
    text = text.replace("@@RUST_IMPORTS@@", RUST_IMPORTS if rust else "")
    text = text.replace("@@RUST_HELPER@@", RUST_HELPER if rust else "")
    text = text.replace("@@ID@@", facts["id"])
    text = text.replace("@@CHAPTER@@", facts["id"][:2]).replace("@@LETTER@@",
                                                                facts["id"][2])
    return text


def generated_cells(facts: dict) -> tuple[dict, dict]:
    """The markdown cell "## 2. How to run this notebook" and the set-up code cell."""
    how = {"cell_type": "markdown",
           "source": run_instructions.notebook_markdown(facts)}
    setup = {"cell_type": "code",
             "source": run_instructions.code_comments(facts) + "\n" + preamble(facts)}
    return how, setup


def full_cells(facts: dict, cells: list[dict]) -> list[dict]:
    how, setup = generated_cells(facts)
    return [cells[0], how, setup] + list(cells[1:])


# =========================================================================== lint

HEADING = re.compile(r"^## (\d+)\. (\S.*)$")


def lint(facts: dict, cells: list[dict], builder_relative: str) -> list[str]:
    """Problems of a builder (empty list when it follows every static rule)."""
    problems = run_instructions.validate_facts(facts)
    if problems:
        return problems
    problems += [f"run instructions: {p}"
                 for p in run_instructions.check_renderings(facts)]
    if Path(builder_relative).stem != facts["name"]:
        problems.append(f"the builder must be named {facts['name']}.py")
    if not isinstance(cells, list) or not cells:
        return problems + ["CELLS must be a non-empty list"]
    for index, cell in enumerate(cells, 1):
        if not (isinstance(cell, dict) and cell.get("cell_type") in ("markdown", "code")
                and isinstance(cell.get("source"), str)):
            problems.append(f"CELLS[{index - 1}] is not made with md(...) or code(...)")
    if problems:
        return problems
    everything = full_cells(facts, cells)
    numbers = []
    for index, cell in enumerate(everything, 1):
        label = f"cell {index} ({cell['cell_type']})"
        source = cell["source"]
        if not source.strip():
            problems.append(f"{label} is empty")
        if not source.isascii():
            bad = sorted({c for c in source if ord(c) > 127})
            problems.append(f"{label} contains non-ASCII characters {bad!r} (write "
                            "LaTeX such as $\\gamma$ in markdown, \\u escapes in code)")
        if "```" in source:
            problems.append(f"{label} contains ``` (it would end the book's code block)")
        if "<!--" in source:
            problems.append(f"{label} contains an HTML comment")
        for number, line in enumerate(source.split("\n"), 1):
            if len(line) > MAX_LINE:
                problems.append(f"{label} line {number} has {len(line)} characters "
                                f"(at most {MAX_LINE})")
            if "\t" in line or "\r" in line:
                problems.append(f"{label} line {number} contains a tab or a CR")
            if line != line.rstrip():
                problems.append(f"{label} line {number} ends with blanks")
            if cell["cell_type"] == "code" and re.match(r"\s*[%!]", line):
                problems.append(f"{label} line {number}: no IPython magics or shell "
                                "commands (% or !); write plain Python")
        if cell["cell_type"] == "code":
            if index == 1 or everything[index - 2]["cell_type"] != "markdown":
                problems.append(f"{label} is not preceded by a markdown cell")
            if "get_ipython" in source:
                problems.append(f"{label} uses get_ipython (write plain Python)")
        else:
            match = HEADING.match(source.split("\n", 1)[0])
            if match:
                numbers.append((int(match.group(1)), match.group(2), index))
    expected = list(range(1, len(numbers) + 1))
    if [n for n, _, _ in numbers] != expected:
        problems.append("the markdown sections '## N. Title' must be numbered 1, 2, 3, "
                        f"... in order; found {[n for n, _, _ in numbers]}")
    titles = {n: title for n, title, _ in numbers}
    for number, title in SECTION_TITLES.items():
        if titles.get(number) != title:
            problems.append(f"section {number} must be '## {number}. {title}'")
    if not numbers or numbers[-1][1] != LAST_SECTION_TITLE or \
            numbers[-1][2] != len(everything):
        problems.append(f"the last cell must be the markdown cell '## N. "
                        f"{LAST_SECTION_TITLE}'")
    if HEADING.match(cells[0]["source"].split("\n", 1)[0]) is None or \
            not cells[0]["source"].startswith(f"## 1. {SECTION_TITLES[1]}"):
        problems.append(f"the first cell must be '## 1. {SECTION_TITLES[1]}'")
    code_cells = [c for c in everything if c["cell_type"] == "code"]
    last_code = code_cells[-1]["source"].rstrip().split("\n")[-1].strip()
    if len(code_cells) < 2 or last_code != "all_checks_passed()":
        problems.append("the last line of the last code cell must be "
                        "all_checks_passed()")
    final = f"ALL {{n}} CHECKS PASSED (notebook {facts['id']})"
    if not re.fullmatch(re.escape(final).replace(r"\{n\}", r"\d+"),
                        facts["final_lines"][-1]):
        problems.append(f"the last of FACTS['final_lines'] must read {final!r} with "
                        "n the number of checks")
    figures = [p for p in facts["files_written"] if p.endswith(".png")]
    sidecar = f"{FIGURE_FOLDER}/{facts['id']}.captions.json"
    if sidecar not in facts["files_written"]:
        problems.append(f"FACTS['files_written'] must list {sidecar} (the set-up cell "
                        "always writes it)")
    for path in figures:
        if not re.fullmatch(rf"{FIGURE_FOLDER}/{facts['id']}_[1-9]\d*_[a-z0-9]+"
                            r"(?:_[a-z0-9]+)*\.png", path):
            problems.append(f"figure {path!r} must be {FIGURE_FOLDER}/"
                            f"{facts['id']}_<k>_<name>.png (lower-case name)")
    if figures and "matplotlib" not in facts["packages"]:
        problems.append("a notebook with figures must list matplotlib in packages")
    return problems


# =========================================================================== notebook

def new_notebook(facts: dict, cells: list[dict], builder_relative: str):
    import nbformat

    notebook = nbformat.v4.new_notebook()
    for index, cell in enumerate(full_cells(facts, cells), 1):
        if cell["cell_type"] == "markdown":
            node = nbformat.v4.new_markdown_cell(cell["source"])
        else:
            node = nbformat.v4.new_code_cell(cell["source"])
        node["id"] = f"{facts['id']}-{index:02d}"
        notebook.cells.append(node)
    notebook.metadata = metadata(facts, builder_relative)
    return notebook


def metadata(facts: dict, builder_relative: str) -> dict:
    return {
        "kernelspec": dict(KERNELSPEC),
        "language_info": copy.deepcopy(LANGUAGE_INFO),
        "textbook": {
            "builder": builder_relative,
            "facts": copy.deepcopy(facts),
            "generator": "Revision/textbook/tools/nbkit.py",
        },
    }


def _peak_memory_mb(pid: int | None) -> float | None:
    """Peak memory of the process pid in MiB (Windows: peak working set; Linux: VmHWM;
    elsewhere the current resident size, sampled after every cell)."""
    if pid is None:
        return None
    status = Path(f"/proc/{pid}/status")
    try:
        if status.is_file():
            for line in status.read_text().splitlines():
                if line.startswith("VmHWM:"):
                    return int(line.split()[1]) / 1024
        import psutil

        info = psutil.Process(pid).memory_info()
        peak = getattr(info, "peak_wset", None) or info.rss
        return peak / 2 ** 20
    except Exception:  # noqa: BLE001 - a measurement must never fail a build
        return None


def execute(notebook, facts: dict, output_root: Path | None) -> dict:
    """Execute the notebook in place; return the measurements.  The build run uses
    PYTHONHASHSEED=0 and the check run (output_root set) PYTHONHASHSEED=1, so that an
    output that depends on the order of a set or on hash values fails the check."""
    import warnings

    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError, CellTimeoutError

    # pyzmq warns on Windows that the default (proactor) event loop needs a helper
    # thread; that concerns nbkit's own process, not the notebook.
    warnings.filterwarnings("ignore", message="Proactor event loop does not implement",
                            category=RuntimeWarning)
    peaks: list[float] = []
    state: dict = {}

    def sample(**_ignored) -> None:
        provisioner = getattr(state.get("client").km, "provisioner", None)
        value = _peak_memory_mb(getattr(provisioner, "pid", None))
        if value is not None:
            peaks.append(value)

    saved = dict(os.environ)
    os.environ.update({"PYTHONHASHSEED": "0" if output_root is None else "1",
                       "MPLBACKEND": INLINE_BACKEND,
                       "PYDEVD_DISABLE_FILE_VALIDATION": "1",
                       "JUPYTER_PLATFORM_DIRS": "1"})
    if output_root is None:
        os.environ.pop("TEXTBOOK_OUTPUT_ROOT", None)
    else:
        os.environ["TEXTBOOK_OUTPUT_ROOT"] = str(output_root)
    client = NotebookClient(
        notebook, kernel_name=KERNEL_NAME, timeout=facts["timeout_seconds"],
        startup_timeout=180, record_timing=False, allow_errors=False,
        resources={"metadata": {"path": str(NOTEBOOKS)}}, on_cell_executed=sample)
    state["client"] = client
    start = time.perf_counter()
    try:
        client.execute()
    except (CellExecutionError, CellTimeoutError) as error:
        raise NotebookError(f"execution failed:\n{error}") from None
    finally:
        os.environ.clear()
        os.environ.update(saved)
    seconds = time.perf_counter() - start
    kernel_version = notebook.metadata.get("language_info", {}).get("version", "")
    return {"seconds": round(seconds, 1),
            "peak_mb": round(max(peaks), 0) if peaks else None,
            "kernel_python": kernel_version}


def _text(value) -> str:
    return "".join(value) if isinstance(value, list) else str(value)


def normalise_outputs(outputs: list) -> list:
    """Merge consecutive stream outputs of the same name, drop transient data, LF."""
    import nbformat

    result: list = []
    for output in outputs:
        output = copy.deepcopy(output)
        output.pop("transient", None)
        if output["output_type"] == "stream":
            text = _text(output["text"]).replace("\r\n", "\n")
            if result and result[-1]["output_type"] == "stream" and \
                    result[-1]["name"] == output["name"]:
                result[-1]["text"] = result[-1]["text"] + text
                continue
            output = nbformat.v4.new_output("stream", name=output["name"], text=text)
        result.append(output)
    return result


def normalise(notebook, facts: dict, builder_relative: str) -> str:
    """The deterministic text of the executed notebook (sorted keys, LF, final newline)."""
    import nbformat

    notebook.metadata = metadata(facts, builder_relative)
    notebook.nbformat, notebook.nbformat_minor = 4, 5
    for index, cell in enumerate(notebook.cells, 1):
        cell["id"] = f"{facts['id']}-{index:02d}"
        cell["metadata"] = {}
        if cell["cell_type"] == "code":
            cell["outputs"] = normalise_outputs(cell.get("outputs", []))
    nbformat.validate(notebook)
    text = nbformat.writes(notebook, version=4).replace("\r\n", "\n")
    return text if text.endswith("\n") else text + "\n"


# =========================================================================== outputs

def output_texts(output) -> list[str]:
    """The text of an output as the book prints it (empty for a pure figure)."""
    kind = output["output_type"]
    if kind == "stream":
        return [_text(output["text"])]
    if kind in ("display_data", "execute_result"):
        data = output.get("data", {})
        if "image/png" in data:
            return []
        if "text/plain" in data:
            return [_text(data["text/plain"])]
    return []


def figure_of(output) -> str | None:
    if output["output_type"] == "display_data" and "image/png" in output.get("data", {}):
        return output.get("metadata", {}).get("textbook_figure")
    return None


def png_facts(data: bytes) -> dict:
    """width, height, dpi (from pHYs) and the chunk types of a PNG file."""
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("not a PNG file")
    position, chunks, info = 8, [], {}
    while position < len(data):
        length, kind = struct.unpack(">I4s", data[position:position + 8])
        body = data[position + 8:position + 8 + length]
        chunks.append(kind)
        if kind == b"IHDR":
            info["width"], info["height"] = struct.unpack(">II", body[:8])
        elif kind == b"pHYs":
            x, y, unit = struct.unpack(">IIB", body[:9])
            if unit == 1:
                info["dpi"] = round(x * 0.0254)
        position += 12 + length
    info["chunks"] = chunks
    return info


def validate_executed(notebook, facts: dict, output_root: Path,
                      forbidden_strings: list[str]) -> tuple[list[str], dict]:
    """Problems of the executed notebook and the facts of its outputs."""
    problems: list[str] = []
    figures: list[str] = []
    passes: list[tuple[int, str]] = []
    results: list[tuple[int, str]] = []
    forbidden = [s.lower() for s in forbidden_strings if s]
    code_cells = [cell for cell in notebook.cells if cell["cell_type"] == "code"]
    for cell in code_cells:
        count = cell.get("execution_count")
        label = f"In [{count}]"
        if count is None:
            problems.append(f"a code cell was not executed: {cell['source'][:60]!r}")
            continue
        lines_in_cell = 0
        for output in cell.get("outputs", []):
            kind = output["output_type"]
            if kind == "error":
                problems.append(f"{label}: error output {output.get('ename')}")
                continue
            if kind == "stream" and output["name"] == "stderr" and \
                    not facts.get("allow_stderr", False):
                problems.append(f"{label}: output on stderr (warnings must be fixed, "
                                f"not printed): {_text(output['text'])[:200]!r}")
            if kind in ("display_data", "execute_result"):
                data = output.get("data", {})
                extra = sorted(set(data) - set(TEXT_MIME_TYPES) - {"image/png"})
                if extra:
                    problems.append(f"{label}: output of unsupported type {extra}")
                if "image/png" in data:
                    name = figure_of(output)
                    if not name:
                        problems.append(f"{label}: a figure was shown without "
                                        "save_figure (close every figure with "
                                        "save_figure; end plotting lines with ;)")
                    else:
                        figures.append(name)
                elif "text/plain" not in data:
                    problems.append(f"{label}: output without text/plain")
            for text in output_texts(output):
                lines = text.rstrip("\n").split("\n")
                lines_in_cell += len(lines)
                for line in lines:
                    if len(line) > MAX_LINE:
                        problems.append(f"{label}: output line of {len(line)} "
                                        f"characters (at most {MAX_LINE}): {line[:50]!r}")
                    if not line.isascii() or "\t" in line or "\r" in line:
                        problems.append(f"{label}: output line not plain ASCII: "
                                        f"{line[:50]!r}")
                    if line.lstrip().startswith("```"):
                        problems.append(f"{label}: output line starts with ```")
                    if ADDRESS_PATTERN.search(line):
                        problems.append(f"{label}: output contains a memory address "
                                        f"(differs from run to run): {line[:60]!r}")
                    lowered = line.lower().replace("\\\\", "\\")
                    for value in forbidden:
                        if value in lowered:
                            problems.append(f"{label}: output contains a path of this "
                                            f"computer: {line[:60]!r}")
                if output["output_type"] == "stream" and output["name"] == "stdout":
                    current = None
                    for line in lines:
                        if line.startswith("PASS "):
                            passes.append((count, line))
                            current = passes
                        elif line.startswith("RESULT "):
                            results.append((count, line))
                            current = results
                        elif current is not None and line.startswith(" "):
                            current.append((count, line))
                        else:
                            current = None
        if lines_in_cell > MAX_OUTPUT_LINES:
            problems.append(f"{label}: {lines_in_cell} output lines (at most "
                            f"{MAX_OUTPUT_LINES}; write long results to a file)")
    if code_cells:
        last = "".join(_text(o["text"]) for o in code_cells[-1].get("outputs", [])
                       if o["output_type"] == "stream" and o["name"] == "stdout")
        tail = last.rstrip("\n").split("\n")[-len(facts["final_lines"]):]
        if tail != list(facts["final_lines"]):
            problems.append(f"the last code cell ends with {tail!r}, but "
                            f"FACTS['final_lines'] is {facts['final_lines']!r}")
    if not passes:
        problems.append("the notebook prints no PASS line (it has no check)")
    # figures and captions
    sidecar_relative = f"{FIGURE_FOLDER}/{facts['id']}.captions.json"
    sidecar = output_root / sidecar_relative
    captions: dict = {}
    if not sidecar.is_file():
        problems.append(f"{sidecar_relative} was not written")
    else:
        raw = sidecar.read_bytes()
        try:
            captions = json.loads(raw.decode("utf-8"))
        except ValueError:
            problems.append(f"{sidecar_relative} is not valid JSON")
        if b"\r" in raw:
            problems.append(f"{sidecar_relative} contains CR characters")
    if len(set(figures)) != len(figures):
        problems.append(f"a figure was shown twice: {figures}")
    expected_names = [f"{facts['id']}_{k}_" for k in range(1, len(figures) + 1)]
    for prefix, name in zip(expected_names, sorted(
            figures, key=lambda n: int(n.split("_")[1]))):
        if not name.startswith(prefix):
            problems.append(f"figure numbers must be 1, 2, 3, ...; found {figures}")
            break
    if sorted(captions) != sorted(set(figures)):
        problems.append(f"the captions file lists {sorted(captions)} but the notebook "
                        f"shows {sorted(set(figures))}")
    for name, caption in captions.items():
        problems += caption_problems(name, caption)
    listed_figures = sorted(p.rsplit("/", 1)[1] for p in facts["files_written"]
                            if p.endswith(".png"))
    if listed_figures != sorted(set(figures)):
        problems.append(f"FACTS['files_written'] lists the figures {listed_figures} "
                        f"but the notebook saves {sorted(set(figures))}")
    for name in figures:
        path = output_root / FIGURE_FOLDER / name
        if not path.is_file():
            problems.append(f"figure file {name} was not written")
            continue
        try:
            info = png_facts(path.read_bytes())
        except (ValueError, struct.error) as error:
            problems.append(f"figure {name}: {error}")
            continue
        if info.get("dpi") != FIGURE_DPI:
            problems.append(f"figure {name}: saved with {info.get('dpi')} dpi, not "
                            f"{FIGURE_DPI}")
        if set(info["chunks"]) & PNG_FORBIDDEN_CHUNKS:
            problems.append(f"figure {name}: the PNG holds metadata "
                            f"{sorted(c.decode() for c in set(info['chunks']) & PNG_FORBIDDEN_CHUNKS)}")
        if info["height"] > MAX_ASPECT * info["width"]:
            problems.append(f"figure {name}: {info['width']} x {info['height']} pixels; "
                            f"the height may be at most {MAX_ASPECT} x the width")
        if info["width"] < 300:
            problems.append(f"figure {name}: only {info['width']} pixels wide")
    found = {"figures": figures, "captions": captions, "passes": passes,
             "results": results}
    return problems, found


def caption_problems(name: str, caption) -> list[str]:
    problems = []
    if not isinstance(caption, str) or not caption.strip():
        return [f"figure {name}: empty caption"]
    if not caption.isascii() or "\n" in caption or "\t" in caption:
        problems.append(f"figure {name}: the caption must be one line of ASCII text")
    if len(caption) > 900:
        problems.append(f"figure {name}: the caption has {len(caption)} characters "
                        "(at most 900)")
    bad = sorted({c for c in caption if c in "[]`*"})
    if bad:
        problems.append(f"figure {name}: the caption contains {bad} (write math as "
                        "$...$, no brackets, backticks or asterisks)")
    if caption.count("$") % 2:
        problems.append(f"figure {name}: the caption has an unpaired $")
    for sequence in run_instructions.LIGATURES:
        if sequence in caption:
            problems.append(f"figure {name}: the caption contains {sequence!r}, which "
                            "the PDF prints as one other character")
    if caption != caption.strip() or not caption.rstrip().endswith("."):
        problems.append(f"figure {name}: the caption must end with a full stop and "
                        "have no surrounding blanks")
    return problems


# =========================================================================== files

def snapshot(root: Path) -> dict[str, tuple[int, int]]:
    """{repository-relative path: (size, mtime_ns)} of the files of the repository,
    without .git, build folders and caches."""
    found: dict[str, tuple[int, int]] = {}
    stack = [root]
    while stack:
        folder = stack.pop()
        try:
            entries = list(os.scandir(folder))
        except OSError:
            continue
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                if entry.name in SNAPSHOT_SKIP or (
                        folder == root and entry.name in SNAPSHOT_SKIP_TOP):
                    continue
                stack.append(entry.path)
            elif entry.is_file(follow_symlinks=False):
                stat = entry.stat(follow_symlinks=False)
                found[Path(entry.path).relative_to(root).as_posix()] = (
                    stat.st_size, stat.st_mtime_ns)
    return found


def changed_files(before: dict, after: dict) -> set[str]:
    return {path for path in set(before) | set(after) if before.get(path) != after.get(path)}


def own_file(facts: dict, path: str) -> bool:
    """Is path a file that only this notebook may write?"""
    name = path.rsplit("/", 1)[-1]
    return path.startswith("Revision/textbook/") and (
        name.startswith(f"{facts['id']}_") or name.startswith(f"{facts['id']}."))


def listed_output_files(output_root: Path) -> set[str]:
    return {p.relative_to(output_root).as_posix() for p in output_root.rglob("*")
            if p.is_file()}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def crate_dependencies(manifest: Path) -> list[str]:
    """Names in the [dependencies] table of a Cargo.toml (empty: no download)."""
    names, inside = [], False
    for line in manifest.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("["):
            inside = stripped in ("[dependencies]", "[build-dependencies]")
            continue
        if inside and stripped and not stripped.startswith("#") and "=" in stripped:
            names.append(stripped.split("=", 1)[0].strip())
    return names


# =========================================================================== provenance

def environment_record() -> dict:
    import importlib.metadata as metadata_module

    direct, _ = run_instructions.load_pins()
    packages = {}
    for name, _ in direct:
        try:
            packages[name] = metadata_module.version(name)
        except metadata_module.PackageNotFoundError:
            packages[name] = "not installed"
    try:
        cargo = subprocess.run(["cargo", "--version"], capture_output=True, text=True,
                               timeout=60).stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        cargo = None
    return {
        "os": f"{platform.system()} {platform.release()} ({platform.version()})",
        "machine": platform.machine(),
        "python": platform.python_version(),
        "packages": packages,
        "support_pins_equal_installed": not run_instructions.check_requirements(),
        "cargo": cargo,
    }


def _fence(lines: list[str]) -> list[str]:
    return ["```text"] + lines + ["```"]


def provenance_markdown(facts: dict, builder_relative: str, notebook_text: str,
                        found: dict, files: dict[str, bytes], record: dict) -> str:
    """The provenance file X.PROVENANCE.md (deterministic: everything that varies from
    run to run comes from record)."""
    nb_file = run_instructions.notebook_file(facts)
    builder_bytes = (ROOT / builder_relative).read_bytes()
    notebook = json.loads(notebook_text)
    cells = notebook["cells"]
    sections = [cell_source for cell_source in
                ("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
                if HEADING.match(cell_source.split("\n", 1)[0])]
    code_count = sum(1 for c in cells if c["cell_type"] == "code")
    check = record.get("check") or {}
    build = record.get("build") or {}
    environment = record.get("environment") or {}
    figures = [name for name in found["figures"]]
    lines: list[str] = []
    add = lines.append
    add(f"# Provenance of Notebook {facts['id']}: {facts['title']}")
    add("")
    add(f"This file is the provenance record of the notebook `{nb_file}` of the textbook "
        "\"Universes in Pairs\" (TEXTBOOK_SPEC rule R6). It was generated by "
        f"`Revision/textbook/tools/nbkit.py` from the notebook's builder "
        f"`{builder_relative}` and from the recorded, verified execution of the "
        "notebook; it is regenerated by nbkit and never edited by hand.")
    add("")
    add(f"- Date of the verified execution: {record.get('date', 'not recorded')}.")
    add(f"- Result of `nbkit check`: {check_sentence(check)}")
    add("")
    add("## 1. What the notebook computes")
    add("")
    add(facts["purpose"])
    add("")
    if facts["records"]:
        add("It reads or reproduces these Revision records:")
        add("")
        for path, what in facts["records"]:
            add(f"- `{path}`: {what}")
    else:
        add("It reads and reproduces no Revision record.")
    add("")
    add(f"The notebook has {len(cells)} cells ({len(cells) - code_count} markdown cells "
        f"and {code_count} code cells) in these sections:")
    add("")
    for source in sections:
        add(f"- {source.split(chr(10), 1)[0][3:]}")
    add("")
    pass_count = sum(1 for _, line in found["passes"] if line.startswith("PASS "))
    result_count = sum(1 for _, line in found["results"] if line.startswith("RESULT "))
    add(f"It prints {plural(pass_count, 'PASS line')} (one per check), "
        f"{plural(result_count, 'RESULT line')} (key numbers) and draws "
        f"{plural(len(figures), 'figure')}.")
    add("")
    add("## 2. How to execute it (the complete instructions for the student)")
    add("")
    add("These are the same instructions that the book prints just before the text of the "
        "notebook, that the notebook's markdown cell \"2. How to run this notebook\" "
        "contains, and that the first code cell repeats as comments.")
    add("")
    lines.extend(run_instructions.book_markdown(facts).rstrip("\n").split("\n"))
    add("")
    add("To repeat the verification of the book's maintainers (a second, independent "
        "execution whose notebook and files are compared byte for byte with the stored "
        "ones; it writes only into a scratch folder), run in the repository folder:")
    add("")
    lines.extend(_fence([f"python Revision/textbook/tools/nbkit.py check "
                         f"{builder_relative}"]))
    add("")
    add("## 3. Expected output")
    add("")
    add("### 3.1 Check lines")
    add("")
    add("Every check prints a PASS line (a check that fails stops the notebook with an "
        "AssertionError instead). The notebook prints these lines, in this order; the "
        "label In [k] is the number of the code cell that prints the line:")
    add("")
    lines.extend(_fence([f"In [{count}]  {line}" for count, line in found["passes"]]))
    add("")
    add("### 3.2 Key numbers")
    add("")
    if found["results"]:
        add("The key numbers are printed as RESULT lines:")
        add("")
        lines.extend(_fence([f"In [{count}]  {line}" for count, line in
                             found["results"]]))
    else:
        add("The notebook prints no RESULT line; its numbers are the versions and "
            "values printed in its cells.")
    add("")
    add("### 3.3 The last lines")
    add("")
    add("The last code cell ends with exactly these lines:")
    add("")
    lines.extend(_fence(list(facts["final_lines"])))
    add("")
    add("### 3.4 Figures")
    add("")
    if figures:
        add(f"The notebook shows {len(figures)} figure{'' if len(figures) == 1 else 's'}"
            ", each below the cell that draws it, and saves each as a PNG file (150 dots "
            "per inch, no metadata):")
        add("")
        for name in sorted(figures, key=lambda n: int(n.split("_")[1])):
            data = files.get(f"{FIGURE_FOLDER}/{name}", b"")
            info = png_facts(data) if data else {"width": "?", "height": "?"}
            add(f"- `{FIGURE_FOLDER}/{name}` ({info['width']} x {info['height']} "
                f"pixels): {found['captions'].get(name, '')}")
    else:
        add("The notebook draws no figure.")
    add("")
    add("## 4. Side effects")
    add("")
    add("### 4.1 Files written in the repository")
    add("")
    add("The notebook writes (creates, or overwrites with the same bytes) exactly these "
        "files and no other file of the repository; each is written below the "
        "repository folder, or below the folder named by the environment variable "
        "TEXTBOOK_OUTPUT_ROOT when it is set (`nbkit check` sets it to a scratch "
        "folder):")
    add("")
    add("| file | bytes | sha256 |")
    add("| --- | --- | --- |")
    for path in facts["files_written"]:
        data = files.get(path)
        if data is None:
            add(f"| `{path}` | missing | missing |")
        else:
            add(f"| `{path}` | {len(data)} | `{sha256(data)}` |")
    add("")
    add("Running the notebook headless with `--inplace`, or saving it in JupyterLab, "
        f"also rewrites the notebook file `{nb_file}` itself (with new outputs; "
        "JupyterLab's copy differs from the stored one in its metadata). JupyterLab "
        "also keeps a checkpoint copy in the folder "
        "`Revision/textbook/notebooks/.ipynb_checkpoints`, which git ignores.")
    add("")
    add("### 4.2 Rust programs")
    add("")
    if facts["needs_rust"]:
        for entry in facts["needs_rust"]:
            crate = entry["manifest"].rsplit("/", 1)[0]
            dependencies = crate_dependencies(ROOT / entry["manifest"])
            add(f"- `{run_instructions.cargo_command(entry['manifest'])}` (run by the "
                "notebook through `rust_program`, and by the student in the step that "
                f"builds the program) creates or updates the folder `{crate}/target` "
                "(ignored by git) and the program"
                f"{'s' if len(entry['binaries']) > 1 else ''} "
                + ", ".join(f"`{crate}/target/release/{b}`" for b in entry["binaries"])
                + " (with the ending `.exe` on Windows). "
                + ("The crate has no dependencies, so the build downloads nothing."
                   if not dependencies else
                   "On the first build cargo downloads the crates "
                   + ", ".join(dependencies) + " from https://crates.io."))
    else:
        add("None: the notebook runs no Rust program.")
    add("")
    add("### 4.3 Outside the repository")
    add("")
    add("- matplotlib keeps a font cache in its cache folder (the folder named by "
        "`matplotlib.get_cachedir()`, for example `.matplotlib` in the home folder); "
        "it is built on the first import of matplotlib.")
    add("- IPython creates its settings folder `.ipython` in the home folder when the "
        "first kernel starts; Jupyter writes a connection file for every kernel into its "
        "runtime folder (`jupyter --runtime-dir` names it) and deletes it when the "
        "kernel stops.")
    add("- JupyterLab (not the headless run) stores its window layout in the folder "
        "`.jupyter/lab/workspaces` of the home folder.")
    add("- Nothing else is written outside the repository.")
    add("")
    add("### 4.4 Network")
    add("")
    if facts.get("network"):
        add(f"While it runs the notebook uses the internet: {facts['network']}")
    else:
        add("The notebook does not use the network while it runs. The installation "
            "(git clone, pip install, and Rust when it is needed) downloads from "
            "https://github.com, https://pypi.org and https://rustup.rs.")
    add("")
    add("### 4.5 Run time and memory")
    add("")
    add(f"Expected run time: {run_instructions.run_time_text(facts['expected_seconds'])} "
        f"(FACTS: {facts['expected_seconds']:g} s); nbkit stops a cell after "
        f"{facts['timeout_seconds']} s. Measured on the computer of section 5, "
        "including the start of the kernel:")
    add("")
    add(f"- the build run: {measure_text(build)};")
    add(f"- the check run: {measure_text(check)}.")
    add("")
    add("## 5. Environment of the verified execution")
    add("")
    if environment:
        add(f"- Operating system: {environment.get('os')}, machine "
            f"{environment.get('machine')}.")
        add(f"- Python {environment.get('python')} (the kernel reported "
            f"{build.get('kernel_python') or 'unknown'}).")
        packages = environment.get("packages", {})
        # The order of the [direct] pins (the record is stored with sorted keys, so the
        # text must not depend on the order of the dictionary).
        order = [name for name, _ in run_instructions.load_pins()[0]]
        names = [n for n in order if n in packages] + sorted(
            n for n in packages if n not in order)
        add("- Packages: " + ", ".join(f"{n} {packages[n]}" for n in names) + ".")
        add("- Every other package pinned in `Revision/textbook/requirements.txt` "
            "([support]) was installed at its pinned version: "
            f"{'yes' if environment.get('support_pins_equal_installed') else 'no'}.")
        add(f"- Rust: {environment.get('cargo') or 'cargo not installed'}"
            f"{'' if facts['needs_rust'] else ' (not used by this notebook)'}.")
    else:
        add("Not recorded.")
    add("")
    add("## 6. Fingerprints (sha256)")
    add("")
    add(f"- `{nb_file}`: `{sha256(notebook_text.encode('utf-8'))}`")
    add(f"- `{builder_relative}`: `{sha256(builder_bytes)}`")
    for path in facts["files_written"]:
        if path in files:
            add(f"- `{path}`: `{sha256(files[path])}`")
    add("")
    add("## 7. Verification")
    add("")
    add(f"- Verified execution: {record.get('date', 'not recorded')}.")
    add(f"- `nbkit check`: {check_sentence(check)}")
    add("- `nbkit build` and `nbkit check` also enforce the notebook rules of "
        "TEXTBOOK_SPEC section 2: no error and no stderr output, every printed line at "
        "most 89 characters of plain ASCII, no memory address and no path of the build "
        "computer in the output, every figure saved by `save_figure` (150 dpi, no PNG "
        "metadata, at most 1.25 times as high as wide) with a caption, the files "
        "written equal to the list in the FACTS, and the final lines as listed.")
    add("")
    add("<!-- nbkit-record "
        + json.dumps(record, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
        + " -->")
    text = "\n".join(lines) + "\n"
    if not text.isascii():
        raise NotebookError("the provenance text is not ASCII")
    return text


def plural(count: int, noun: str) -> str:
    return f"{count} {noun}{'' if count == 1 else 's'}"


def measure_text(measure: dict) -> str:
    if not measure or measure.get("seconds") is None:
        return "not measured"
    text = f"{measure['seconds']:.1f} s"
    if measure.get("peak_mb") is not None:
        text += f", peak memory of the kernel process {measure['peak_mb']:.0f} MiB"
    return text


def check_sentence(check: dict) -> str:
    if not check:
        return "not run yet."
    if check.get("result") == "passed":
        return (f"PASSED on {check.get('date')}: a second, independent execution "
                f"reproduced the notebook and the {plural(check.get('files', 0), 'file')} "
                "it writes byte for byte, and the provenance file regenerated from this "
                "record was identical.")
    return f"{check.get('result')}."


def read_record(path: Path) -> dict | None:
    if not path.is_file():
        return None
    match = RECORD_PATTERN.search(path.read_text(encoding="utf-8"))
    return json.loads(match.group(1)) if match else None


def provenance_path(facts: dict) -> Path:
    return NOTEBOOKS / f"{facts['name']}.PROVENANCE.md"


# =========================================================================== build/check

def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _emit(key: str, value) -> None:
    print(f"{key}={value}")


def _forbidden_strings(*extra: Path) -> list[str]:
    values = []
    for path in (ROOT, Path.home(), Path(tempfile.gettempdir()), *extra):
        for variant in (str(path), path.as_posix()):
            values.append(variant)
    return sorted(set(values), key=len, reverse=True)


def run_once(facts: dict, cells: list[dict], builder_relative: str,
             output_root: Path | None) -> tuple[str, dict, dict, list[str], list[str]]:
    """Execute once.  output_root None: write into the repository.  Returns
    (notebook text, found, measurement, problems, warnings)."""
    notebook = new_notebook(facts, cells, builder_relative)
    before = snapshot(ROOT)
    start_ns = time.time_ns()
    measurement = execute(notebook, facts, output_root)
    after = snapshot(ROOT)
    target = ROOT if output_root is None else output_root
    forbidden = _forbidden_strings(*( [output_root] if output_root else []))
    problems, found = validate_executed(notebook, facts, target, forbidden)
    warnings: list[str] = []
    if measurement.get("kernel_python") and \
            measurement["kernel_python"] != platform.python_version():
        problems.append(f"the kernel runs Python {measurement['kernel_python']}, nbkit "
                        f"runs {platform.python_version()}: the kernelspec python3 "
                        "points to another Python")
    expected = set(facts["files_written"])
    changed = changed_files(before, after)
    if output_root is None:
        for path in sorted(expected):
            if path not in after:
                problems.append(f"{path} is listed in files_written but was not written")
            elif after[path][1] < start_ns - 2_000_000_000 or path not in changed:
                problems.append(f"{path} is listed in files_written but was not "
                                "written by this run")
        for path in sorted(changed - expected):
            if own_file(facts, path):
                problems.append(f"{path} was written but is not in files_written")
            else:
                warnings.append(f"{path} changed during the run (by another process?)")
    else:
        written = listed_output_files(output_root)
        for path in sorted(expected - written):
            problems.append(f"{path} is listed in files_written but was not written")
        for path in sorted(written - expected):
            problems.append(f"{path} was written but is not in files_written")
        for path in sorted(changed):
            if path in expected or own_file(facts, path):
                problems.append(f"{path} in the repository changed during a check run: "
                                "write files only through output_file(...)")
            else:
                warnings.append(f"{path} changed during the run (by another process?)")
    text = normalise(notebook, facts, builder_relative) if not problems else ""
    return text, found, measurement, problems, warnings


def _report_problems(label: str, problems: list[str], warnings: list[str]) -> None:
    for warning in warnings:
        _emit("warning", f"{label}: {warning}")
    for problem in problems:
        _emit("problem", f"{label}: {problem}")


def check_notebook(facts: dict, cells: list[dict], builder_relative: str,
                   scratch: Path, record: dict | None) -> tuple[bool, dict, str]:
    """Execute again into scratch and compare.  Returns (passed, check measurement,
    the regenerated provenance text or "")."""
    label = facts["id"]
    out_root = scratch / facts["name"] / "out"
    shutil.rmtree(out_root, ignore_errors=True)
    out_root.mkdir(parents=True, exist_ok=True)
    text, found, measurement, problems, warnings = run_once(
        facts, cells, builder_relative, out_root)
    _report_problems(label, problems, warnings)
    if problems:
        return False, measurement, ""
    passed = True
    notebook_path = NOTEBOOKS / f"{facts['name']}.ipynb"
    _write_bytes(scratch / facts["name"] / f"{facts['name']}.ipynb", text.encode("utf-8"))
    if not notebook_path.is_file() or notebook_path.read_bytes() != text.encode("utf-8"):
        passed = False
        _emit("problem", f"{label}: the notebook differs from {relative(notebook_path)} "
                         f"(the new one is in {scratch / facts['name']})")
        _diff_hint(notebook_path, text)
    files = {}
    for path in facts["files_written"]:
        new = (out_root / path).read_bytes()
        files[path] = new
        stored = ROOT / path
        if not stored.is_file() or stored.read_bytes() != new:
            passed = False
            _emit("problem", f"{label}: {path} differs from the stored file")
    _emit(f"check_{label}_compared_files", len(files) + 1)
    provenance_text = ""
    if record is not None:
        provenance_text = provenance_markdown(facts, builder_relative, text, found,
                                              files, record)
        stored = provenance_path(facts)
        if not stored.is_file() or stored.read_bytes() != provenance_text.encode("utf-8"):
            passed = False
            _emit("problem", f"{label}: {relative(stored)} differs from the provenance "
                             "regenerated from its own record")
    else:
        passed = False
        _emit("problem", f"{label}: {relative(provenance_path(facts))} is missing or has "
                         "no nbkit-record line")
    measurement["files"] = len(files)
    return passed, measurement, provenance_text


def _diff_hint(stored: Path, text: str) -> None:
    if not stored.is_file():
        return
    old = stored.read_text(encoding="utf-8").split("\n")
    new = text.split("\n")
    for number, (a, b) in enumerate(zip(old, new), 1):
        if a != b:
            _emit("first_difference_line", number)
            _emit("stored", a[:120])
            _emit("new", b[:120])
            return
    _emit("first_difference_line", min(len(old), len(new)) + 1)


def command_lint(builders: list[Path]) -> int:
    failed = 0
    for builder in builders:
        facts, cells, builder_relative = load_builder(builder)
        problems = lint(facts, cells, builder_relative)
        _report_problems(builder_relative, problems, [])
        _emit(f"lint_{facts.get('id', builder.stem)}", "OK" if not problems else "FAILED")
        failed += bool(problems)
    return 1 if failed else 0


def command_build(builders: list[Path], date: str, verify: bool, scratch: Path) -> int:
    failed = 0
    for builder in builders:
        facts, cells, builder_relative = load_builder(builder)
        label = facts.get("id", builder.stem)
        problems = lint(facts, cells, builder_relative)
        if problems:
            _report_problems(builder_relative, problems, [])
            _emit(f"build_{label}", "FAILED")
            failed += 1
            continue
        try:
            text, found, measurement, problems, warnings = run_once(
                facts, cells, builder_relative, None)
        except NotebookError as error:
            _emit("problem", f"{label}: {error}")
            _emit(f"build_{label}", "FAILED")
            failed += 1
            continue
        _report_problems(label, problems, warnings)
        _emit(f"build_{label}_seconds", measurement["seconds"])
        _emit(f"build_{label}_peak_mb", measurement["peak_mb"])
        if problems:
            _emit(f"build_{label}", "FAILED")
            failed += 1
            continue
        notebook_path = NOTEBOOKS / f"{facts['name']}.ipynb"
        _write_bytes(notebook_path, text.encode("utf-8"))
        keep = {p.rsplit("/", 1)[1] for p in facts["files_written"]}
        for stale in sorted((ROOT / FIGURE_FOLDER).glob(f"{facts['id']}_*.png")):
            if stale.name not in keep:
                stale.unlink()
                _emit("removed_stale_figure", relative(stale))
        files = {p: (ROOT / p).read_bytes() for p in facts["files_written"]}
        record = {"date": date, "build": measurement, "check": None,
                  "environment": environment_record()}
        provenance = provenance_markdown(facts, builder_relative, text, found, files,
                                         record)
        _write_bytes(provenance_path(facts), provenance.encode("utf-8"))
        _emit(f"build_{label}_figures", len(found["figures"]))
        _emit(f"build_{label}_checks", sum(1 for _, l in found["passes"]
                                           if l.startswith("PASS ")))
        _emit(f"build_{label}_notebook", relative(notebook_path))
        _emit(f"build_{label}_notebook_sha256", sha256(text.encode("utf-8")))
        if verify:
            try:
                passed, check_measure, _ = check_notebook(
                    facts, cells, builder_relative, scratch, record)
            except NotebookError as error:
                _emit("problem", f"{label}: check run: {error}")
                passed, check_measure = False, {}
            _emit(f"check_{label}_seconds", check_measure.get("seconds"))
            if passed:
                record["check"] = {"date": date, "result": "passed",
                                   "seconds": check_measure["seconds"],
                                   "peak_mb": check_measure["peak_mb"],
                                   "files": check_measure["files"]}
                provenance = provenance_markdown(facts, builder_relative, text, found,
                                                 files, record)
                _write_bytes(provenance_path(facts), provenance.encode("utf-8"))
            else:
                failed += 1
            _emit(f"check_{label}", "PASSED" if passed else "FAILED")
        _emit(f"provenance_{label}", relative(provenance_path(facts)))
        _emit(f"build_{label}", "OK" if verify else "OK (not verified)")
    return 1 if failed else 0


def command_check(builders: list[Path], scratch: Path, record_date: str | None) -> int:
    failed = 0
    for builder in builders:
        facts, cells, builder_relative = load_builder(builder)
        label = facts.get("id", builder.stem)
        problems = lint(facts, cells, builder_relative)
        if problems:
            _report_problems(builder_relative, problems, [])
            _emit(f"check_{label}", "FAILED")
            failed += 1
            continue
        record = read_record(provenance_path(facts))
        try:
            passed, measure, _ = check_notebook(facts, cells, builder_relative,
                                                scratch, record)
        except NotebookError as error:
            _emit("problem", f"{label}: {error}")
            passed, measure = False, {}
        _emit(f"check_{label}_seconds", measure.get("seconds"))
        _emit(f"check_{label}_peak_mb", measure.get("peak_mb"))
        if passed and record_date:
            record["check"] = {"date": record_date, "result": "passed",
                               "seconds": measure["seconds"],
                               "peak_mb": measure["peak_mb"],
                               "files": measure["files"]}
            record["date"] = record_date
            text = (NOTEBOOKS / f"{facts['name']}.ipynb").read_text(encoding="utf-8")
            files = {p: (ROOT / p).read_bytes() for p in facts["files_written"]}
            notebook = json.loads(text)
            found = found_from_notebook(notebook, facts)
            provenance = provenance_markdown(facts, builder_relative, text, found,
                                             files, record)
            _write_bytes(provenance_path(facts), provenance.encode("utf-8"))
            _emit(f"recorded_{label}", record_date)
        _emit(f"check_{label}", "PASSED" if passed else "FAILED")
        failed += not passed
    return 1 if failed else 0


def found_from_notebook(notebook: dict, facts: dict) -> dict:
    """The PASS/RESULT lines, figures and captions of a stored notebook (the same as
    validate_executed finds, without executing)."""
    import nbformat

    node = nbformat.from_dict(notebook)
    _, found = validate_executed(node, facts, ROOT, [])
    return found


def provenance_is_current(builder: Path) -> list[str]:
    """Problems of the stored provenance file of a builder's notebook, without
    executing anything (used by the test suite)."""
    facts, _, builder_relative = load_builder(builder)
    path = provenance_path(facts)
    record = read_record(path)
    if record is None:
        return [f"{relative(path)} is missing or has no nbkit-record line"]
    notebook_path = NOTEBOOKS / f"{facts['name']}.ipynb"
    text = notebook_path.read_text(encoding="utf-8")
    files = {}
    for p in facts["files_written"]:
        if not (ROOT / p).is_file():
            return [f"{p} is missing"]
        files[p] = (ROOT / p).read_bytes()
    found = found_from_notebook(json.loads(text), facts)
    expected = provenance_markdown(facts, builder_relative, text, found, files, record)
    if path.read_bytes() != expected.encode("utf-8"):
        return [f"{relative(path)} differs from the provenance regenerated from its "
                "record and the stored files"]
    if (record.get("check") or {}).get("result") != "passed":
        return [f"{relative(path)}: nbkit check has not passed"]
    return []


def stored_notebook_matches_builder(builder: Path) -> list[str]:
    """Problems when the stored notebook's cells or metadata differ from the builder
    (static comparison, no execution)."""
    facts, cells, builder_relative = load_builder(builder)
    problems = lint(facts, cells, builder_relative)
    if problems:
        return problems
    path = NOTEBOOKS / f"{facts['name']}.ipynb"
    if not path.is_file():
        return [f"{relative(path)} does not exist"]
    stored = json.loads(path.read_text(encoding="utf-8"))
    sources = ["".join(c["source"]) for c in stored["cells"]]
    expected = [c["source"] for c in full_cells(facts, cells)]
    if sources != expected:
        return [f"{relative(path)}: the cells differ from the builder (rebuild it)"]
    if stored["metadata"] != json.loads(json.dumps(metadata(facts, builder_relative))):
        return [f"{relative(path)}: the metadata differs from the builder (rebuild it)"]
    return []


def builders_of(arguments: list[str]) -> list[Path]:
    paths: list[Path] = []
    for argument in arguments:
        path = Path(argument)
        if path.is_dir():
            paths += sorted(path.glob("*.py"))
        else:
            paths.append(path)
    return paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=("lint", "build", "check"))
    parser.add_argument("builders", nargs="+",
                        help="builder files (or the folder of the builders)")
    parser.add_argument("--date", help="build: date of the verified execution, "
                                       "YYYY-MM-DD (required)")
    parser.add_argument("--no-verify", action="store_true",
                        help="build: skip the second (check) execution")
    parser.add_argument("--record", metavar="DATE",
                        help="check: store a passed check in the provenance record")
    parser.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH,
                        help=f"scratch folder for check runs (default {DEFAULT_SCRATCH})")
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] in ("--lint", "--build", "--check"):
        argv[0] = argv[0][2:]  # "nbkit.py --check BUILDER" means "nbkit.py check BUILDER"
    arguments = parser.parse_args(argv)
    builders = builders_of(arguments.builders)
    for date in (arguments.date, arguments.record):
        if date is not None and not DATE_PATTERN.fullmatch(date):
            parser.error("dates are written YYYY-MM-DD")
    if arguments.command == "build" and not arguments.date:
        parser.error("build needs --date YYYY-MM-DD (the date of the verified execution)")
    start = time.perf_counter()
    try:
        if arguments.command == "lint":
            code_ = command_lint(builders)
        elif arguments.command == "build":
            code_ = command_build(builders, arguments.date, not arguments.no_verify,
                                  arguments.scratch.resolve())
        else:
            code_ = command_check(builders, arguments.scratch.resolve(),
                                  arguments.record)
    except NotebookError as error:
        _emit("problem", str(error))
        return 2
    _emit("nbkit_seconds", f"{time.perf_counter() - start:.1f}")
    _emit("nbkit", "OK" if code_ == 0 else "FAILED")
    return code_


def run_builder(builder_file: str) -> int:
    """For the end of a builder: python <builder>.py [lint|build|check] [options]."""
    argv = sys.argv[1:] or ["lint"]
    command, options = argv[0], argv[1:]
    return main([command, builder_file, *options])


if __name__ == "__main__":
    raise SystemExit(main())
