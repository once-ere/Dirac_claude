#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""The complete, self-contained run instructions of a textbook notebook.

Written 2026-10-02 for the textbook "Universes in Pairs" (Revision/textbook/TEXTBOOK_SPEC.md
section 3).  Every notebook of the book is preceded in the book by a section "How to run
Notebook NN<x>" whose text says, IN FULL and without referring the student to any other
place of the book or to any other file, what the notebook needs, how to get the repository,
how to create and activate a private Python environment and install the pinned packages on
Windows (PowerShell), macOS (zsh) and Linux (bash), how to install Rust and build the Rust
programs when the notebook needs them, how to start JupyterLab and run all cells (or run
the notebook headless), how long it takes, which files it writes, which final lines the
student must see, and how to fix the most likely errors.

The same instructions appear three times, generated here from ONE list of blocks so that
they never disagree:

  book_markdown(facts)      the body of the book section "How to run Notebook NN<x>"
                            (Markdown of the subset of scripts/build_dissertation_tex.py:
                            paragraphs, "- " lists and fenced ```text command blocks);
  notebook_markdown(facts)  the notebook's markdown cell "## 2. How to run this notebook"
                            (lines of at most 89 characters; command blocks indented by
                            four spaces, because a notebook cell must never contain ```);
  code_comments(facts)      the same text as "#" comment lines for the top of the
                            notebook's first code cell (at most 89 characters per line).

All three are pure ASCII.  The facts are the FACTS dict of the notebook's builder
(Revision/textbook/tools/README.md documents every key); validate_facts() checks them.
The pinned package versions are read from the [direct] block of
Revision/textbook/requirements.txt.

Command line (from the repository root):
    python Revision/textbook/tools/run_instructions.py NOTEBOOK.ipynb [--format F]
with F = book (default), notebook or comments; the facts are read from the executed
notebook's metadata (key "textbook").
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
TEXTBOOK = TOOLS.parent
ROOT = TEXTBOOK.parent.parent
REQUIREMENTS = TEXTBOOK / "requirements.txt"

REPOSITORY_URL = "https://github.com/once-ere/Dirac_claude.git"
REPOSITORY_FOLDER = "Dirac_claude"
ENVIRONMENT = "dirac-book-env"
NOTEBOOK_FOLDER = "Revision/textbook/notebooks"
PYTHON_MINIMUM = "3.12"
PYTHON_BUILT = "3.14.5"
CARGO_BUILT = "1.91.1"
MAX_LINE = 89
COMMAND_MAX = MAX_LINE - 6  # "#     " prefix in the code comments

ID_PATTERN = re.compile(r"(\d{2})([a-z])")
NAME_PATTERN = re.compile(r"(\d{2}[a-z])_([a-z0-9]+(?:_[a-z0-9]+)*)")
REPO_PATH_PATTERN = re.compile(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*/?")
# A run instruction must never send the student elsewhere: no "see the ...", "cf. ...",
# "Chapter N", "Section N.M", "Appendix", "page N", "README", "this book".
FORBIDDEN_REFERENCES = re.compile(
    r"\b(?:[Ss]ee|[Cc]f\.)\s+(?:the\s+)?(?:[Cc]hapter|[Ss]ection|[Aa]ppendix|file|"
    r"page|README|notebook|[Nn]otebooks|book|above|below|documentation)\b"
    r"|\b(?:Chapters?|Sections?|Appendix|[Pp]ages?)\s+[0-9A-Z]"
    r"|\bREADME\b|\bthis book\b|\bthe book's\b"
)

REQUIRED_KEYS = {
    "id": str,
    "name": str,
    "title": str,
    "purpose": str,
    "packages": list,
    "needs_rust": list,
    "run_time": str,
    "expected_seconds": (int, float),
    "timeout_seconds": int,
    "files_written": list,
    "final_lines": list,
    "troubleshooting": list,
}
OPTIONAL_KEYS = {"allow_stderr": bool}
RUST_KEYS = {"manifest": str, "binaries": list, "build_minutes": (int, float),
             "built_by_notebook": bool}


# --------------------------------------------------------------------------- pins

def load_pins(path: Path = REQUIREMENTS) -> tuple[list[tuple[str, str]],
                                                   list[tuple[str, str]]]:
    """(direct, support) lists of (package, version) from requirements.txt."""
    direct: list[tuple[str, str]] = []
    support: list[tuple[str, str]] = []
    block = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "# [direct]":
            block = direct
            continue
        if line == "# [support]":
            block = support
            continue
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z0-9_.-]+)==([A-Za-z0-9_.+-]+)", line)
        if match is None or block is None:
            raise ValueError(f"{path}: cannot read the pin {raw!r}")
        block.append((match.group(1), match.group(2)))
    if not direct:
        raise ValueError(f"{path}: no [direct] block")
    return direct, support


def pip_commands(direct: list[tuple[str, str]]) -> list[str]:
    """python -m pip install commands, each at most COMMAND_MAX characters."""
    commands: list[str] = []
    current = "python -m pip install"
    count = 0
    for name, version in direct:
        item = f" {name}=={version}"
        if count and len(current) + len(item) > COMMAND_MAX:
            commands.append(current)
            current = "python -m pip install"
            count = 0
        current += item
        count += 1
    commands.append(current)
    return commands


# --------------------------------------------------------------------------- facts

def validate_facts(facts: dict) -> list[str]:
    """Problems with a FACTS dict (empty list when it is valid)."""
    problems: list[str] = []
    for key, kind in REQUIRED_KEYS.items():
        if key not in facts:
            problems.append(f"FACTS lacks the key {key!r}")
        elif not isinstance(facts[key], kind) or (
                isinstance(facts[key], bool) and kind is not bool):
            problems.append(f"FACTS[{key!r}] must be of type {kind}")
    for key in facts:
        if key not in REQUIRED_KEYS and key not in OPTIONAL_KEYS:
            problems.append(f"FACTS has the unknown key {key!r}")
    for key, kind in OPTIONAL_KEYS.items():
        if key in facts and not isinstance(facts[key], kind):
            problems.append(f"FACTS[{key!r}] must be of type {kind}")
    if problems:
        return problems
    if not ID_PATTERN.fullmatch(facts["id"]):
        problems.append("FACTS['id'] must be two digits and a letter, e.g. '03b'")
    name = NAME_PATTERN.fullmatch(facts["name"])
    if name is None or name.group(1) != facts["id"]:
        problems.append(
            "FACTS['name'] must be the id, '_' and lower-case words joined by '_', "
            "e.g. '03b_curvature' (it is the notebook's file name without .ipynb)"
        )
    try:
        direct, _ = load_pins()
    except (OSError, ValueError) as error:
        problems.append(str(error))
        direct = []
    pinned = {package for package, _ in direct}
    for package in facts["packages"]:
        if package not in pinned:
            problems.append(f"package {package!r} is not pinned in [direct] of "
                            "Revision/textbook/requirements.txt")
    if not facts["packages"]:
        problems.append("FACTS['packages'] is empty")
    for entry in facts["needs_rust"]:
        if not isinstance(entry, dict):
            problems.append("every needs_rust entry must be a dict")
            continue
        for key, kind in RUST_KEYS.items():
            if key not in entry or not isinstance(entry[key], kind):
                problems.append(f"needs_rust entry lacks {key!r} of type {kind}")
        for key in entry:
            if key not in RUST_KEYS:
                problems.append(f"needs_rust entry has the unknown key {key!r}")
        manifest = entry.get("manifest", "")
        if isinstance(manifest, str):
            if not manifest.endswith("/Cargo.toml") or not \
                    REPO_PATH_PATTERN.fullmatch(manifest):
                problems.append(f"manifest {manifest!r} must be a repository-relative "
                                "path ending in /Cargo.toml")
            elif not (ROOT / manifest).is_file():
                problems.append(f"manifest {manifest!r} does not exist")
        for binary in entry.get("binaries", []) or []:
            if not isinstance(binary, str) or not re.fullmatch(r"[a-z0-9_-]+", binary):
                problems.append(f"binary name {binary!r} must be lower-case "
                                "letters, digits, '_' or '-' (without .exe)")
    for path in facts["files_written"]:
        if not isinstance(path, str) or not REPO_PATH_PATTERN.fullmatch(path):
            problems.append(f"files_written entry {path!r} must be a "
                            "repository-relative path with '/' separators")
    if not facts["final_lines"]:
        problems.append("FACTS['final_lines'] is empty")
    for line in facts["final_lines"]:
        if not isinstance(line, str) or not line.isascii() or len(line) > COMMAND_MAX \
                or not line.strip() or "\n" in line:
            problems.append(f"final line {line!r} must be one non-empty ASCII line of "
                            f"at most {COMMAND_MAX} characters")
    for item in facts["troubleshooting"]:
        if not (isinstance(item, (list, tuple)) and len(item) == 2
                and all(isinstance(part, str) and part.strip() for part in item)):
            problems.append("every troubleshooting entry must be [symptom, fix] "
                            "(two non-empty strings)")
    if facts["timeout_seconds"] < 2 * facts["expected_seconds"]:
        problems.append("timeout_seconds must be at least twice expected_seconds")
    for key in ("title", "purpose", "run_time"):
        if "\n" in facts[key]:
            problems.append(f"FACTS[{key!r}] must be one line")
    text = json.dumps(facts, ensure_ascii=False)
    if not text.isascii():
        problems.append("FACTS must be ASCII only")
    for key in ("purpose", "run_time"):
        if FORBIDDEN_REFERENCES.search(facts[key]):
            problems.append(f"FACTS[{key!r}] refers to another place "
                            "(see/Chapter/Section/Appendix); the run instructions "
                            "must be self-contained")
    for symptom, fix in [tuple(item) for item in facts["troubleshooting"]
                         if isinstance(item, (list, tuple)) and len(item) == 2]:
        if FORBIDDEN_REFERENCES.search(str(symptom) + " " + str(fix)):
            problems.append("a troubleshooting entry refers to another place "
                            "(see/Chapter/Section/Appendix)")
    return problems


def notebook_file(facts: dict) -> str:
    return f"{NOTEBOOK_FOLDER}/{facts['name']}.ipynb"


def _join(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]


def _binary_paths(entry: dict) -> list[str]:
    folder = entry["manifest"].rsplit("/", 1)[0]
    return [f"{folder}/target/release/{binary}" for binary in entry["binaries"]]


# --------------------------------------------------------------------------- blocks
# A block is ("step", text) | ("p", text) | ("list", [items]) | ("cmd", label, [lines]).

def blocks(facts: dict) -> list[tuple]:
    problems = validate_facts(facts)
    if problems:
        raise ValueError("invalid FACTS: " + "; ".join(problems))
    direct, _ = load_pins()
    pins = _join([f"{name} {version}" for name, version in direct])
    used = _join(list(facts["packages"]))
    nb_file = notebook_file(facts)
    nb_name = f"{facts['name']}.ipynb"
    rust = facts["needs_rust"]
    out: list[tuple] = []

    # Step 1 -------------------------------------------------------------------
    out.append(("step", "Step 1. What this notebook does and what it needs."))
    sentence = (
        f"Notebook {facts['id']} ({facts['title']}) is the file {nb_file} of the "
        f"repository {REPOSITORY_FOLDER}. {facts['purpose']} It needs a computer with "
        "Windows 11, macOS or Linux, an internet connection for the installation, the "
        f"program Git, and Python {PYTHON_MINIMUM} or newer (the book was built with "
        f"Python {PYTHON_BUILT}) with these packages at exactly these versions: {pins}. "
        f"The notebook itself imports {used}; the other packages run Jupyter, the "
        "program that shows and runs notebooks."
    )
    if rust:
        programs = _join([b for entry in rust for b in entry["binaries"]])
        sentence += (
            f" It also needs Rust (the program cargo, version {CARGO_BUILT} or newer), "
            f"because it runs the Rust program {programs}, which is part of the "
            "repository and is built on your computer in Step 5."
        )
    else:
        sentence += " It does not need Rust."
    out.append(("p", sentence))

    # Step 2 -------------------------------------------------------------------
    out.append(("step", "Step 2. Install Git and Python (once per computer)."))
    out.append(("list", [
        "Windows: download Git from https://git-scm.com/download/win and install it "
        "with the default choices. Download Python from "
        "https://www.python.org/downloads/ and run the installer; in its first window "
        "tick the box \"Add python.exe to PATH\" before you click \"Install Now\".",
        "macOS: open the app Terminal and run the command xcode-select --install "
        "(it installs Git and the compiler tools). Download Python from "
        "https://www.python.org/downloads/ and run the installer.",
        "Linux (Debian or Ubuntu; other distributions have packages of the same "
        "names): run sudo apt update and then sudo apt install git python3 "
        "python3-venv.",
    ]))
    out.append(("p",
        "Then open a terminal: on Windows the app Windows PowerShell (or Terminal), on "
        "macOS the app Terminal (it runs the shell zsh), on Linux any terminal (it runs "
        "the shell bash). Type every command below into this terminal exactly as "
        "printed, one line at a time, and press Enter after each line."))

    # Step 3 -------------------------------------------------------------------
    out.append(("step", "Step 3. Get the repository and install the packages "
                        "(once per computer)."))
    out.append(("p",
        f"The commands below download the repository into the folder "
        f"{REPOSITORY_FOLDER} inside your home folder, create a private Python "
        f"environment in the folder {ENVIRONMENT} inside your home folder (a private "
        "environment is a folder with its own copy of Python and of the packages, so "
        "that nothing else on your computer is changed), activate it (from then on the "
        "commands python and jupyter typed in this terminal are those of the "
        f"environment, and the prompt starts with ({ENVIRONMENT})), and install the "
        "packages at the pinned versions. If you have done this step before, for this "
        "or for another notebook, skip it and go to Step 4."))
    pip = ["python -m pip install --upgrade pip"] + pip_commands(direct)
    out.append(("cmd", "Windows (PowerShell):", [
        "cd $HOME",
        f"git clone {REPOSITORY_URL}",
        f"py -3 -m venv \"$HOME\\{ENVIRONMENT}\"",
        "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force",
        f"& \"$HOME\\{ENVIRONMENT}\\Scripts\\Activate.ps1\"",
    ] + pip))
    out.append(("p",
        "The line with Set-ExecutionPolicy allows PowerShell to run the activation "
        "script in this one window only; it changes nothing permanently."))
    unix = [
        "cd ~",
        f"git clone {REPOSITORY_URL}",
        f"python3 -m venv ~/{ENVIRONMENT}",
        f"source ~/{ENVIRONMENT}/bin/activate",
    ] + pip
    out.append(("cmd", "macOS (zsh):", list(unix)))
    out.append(("cmd", "Linux (bash):", list(unix)))

    # Step 4 -------------------------------------------------------------------
    out.append(("step", "Step 4. In every new terminal: activate the environment and "
                        "go into the repository folder."))
    out.append(("p",
        "Every later step starts in the repository folder with the environment active. "
        "Run these two or three lines whenever you open a new terminal (they do no "
        "harm if the environment is already active):"))
    out.append(("cmd", "Windows (PowerShell):", [
        "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force",
        f"& \"$HOME\\{ENVIRONMENT}\\Scripts\\Activate.ps1\"",
        f"cd \"$HOME\\{REPOSITORY_FOLDER}\"",
    ]))
    out.append(("cmd", "macOS (zsh) and Linux (bash):", [
        f"source ~/{ENVIRONMENT}/bin/activate",
        f"cd ~/{REPOSITORY_FOLDER}",
    ]))

    step = 5
    # Step 5: Rust ---------------------------------------------------------------
    if rust:
        out.append(("step", f"Step {step}. Install Rust and build the Rust program "
                            "(Rust once per computer, the build once per program)."))
        out.append(("p",
            "Windows: download rustup-init.exe from https://rustup.rs, run it and accept "
            "the default choices; if it reports that the Visual Studio C++ Build Tools "
            "are missing, let it install them (or install the workload \"Desktop "
            "development with C++\" from "
            "https://visualstudio.microsoft.com/visual-cpp-build-tools/ and run "
            "rustup-init.exe again). macOS and Linux: run the command below and accept "
            "the default choice (on Linux first run sudo apt install build-essential, "
            "which provides the linker that Rust needs)."))
        out.append(("cmd", "macOS (zsh) and Linux (bash):", [
            "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
        ]))
        out.append(("p",
            "Then close the terminal, open a new one, do Step 4 again, and check that "
            f"cargo --version prints {CARGO_BUILT} or a newer version. Build the "
            "program with the following command (the same on all three systems):"))
        commands: list[str] = []
        for entry in rust:
            commands.append(
                f"cargo build --release --manifest-path {entry['manifest']}")
        out.append(("cmd", "Windows, macOS and Linux:", commands))
        for entry in rust:
            paths = _binary_paths(entry)
            minutes = entry["build_minutes"]
            text = (
                f"The first build takes about {minutes:g} minute"
                f"{'' if minutes == 1 else 's'}; later builds reuse the result and take "
                "a few seconds. The program is then the file "
                f"{_join(paths)} (on Windows with the ending .exe). "
            )
            if entry["built_by_notebook"]:
                text += ("The notebook runs this build command itself when the program "
                         "is missing, so this step also checks that Rust works.")
            else:
                text += ("The notebook stops with a message that names this command "
                         "when the program is missing.")
            out.append(("p", text))
        step += 1

    # Step: JupyterLab -----------------------------------------------------------
    out.append(("step", f"Step {step}. Run the notebook in JupyterLab."))
    out.append(("p", "In the repository folder, with the environment active, run:"))
    out.append(("cmd", "Windows, macOS and Linux:", [f"jupyter lab {nb_file}"]))
    out.append(("p",
        "JupyterLab opens in your web browser and shows the notebook (if no browser "
        "window opens, copy the address that starts with http://localhost:8888/lab "
        "from the terminal into the address bar of your browser). The name at the top "
        "right of the notebook must read Python 3 (ipykernel). Choose the menu "
        "Run > Run All Cells. While a cell runs, the label to its left shows [*]; "
        "when it has finished, the label shows a number. The notebook has finished "
        f"when the last code cell shows a number; this takes {facts['run_time']}. "
        "Scroll to the end and compare the last printed lines with the lines in the "
        f"step \"What you must see\" below. To keep the results, save the notebook "
        "(menu File > Save Notebook). To stop JupyterLab, choose the menu "
        "File > Shut Down, or press Ctrl+C twice in the terminal."))
    step += 1

    # Step: headless ---------------------------------------------------------------
    out.append(("step", f"Step {step}. Or run the notebook without a browser "
                        "(headless)."))
    out.append(("p", "In the repository folder, with the environment active, run:"))
    out.append(("cmd", "Windows, macOS and Linux:", [
        f"jupyter nbconvert --to notebook --execute --inplace {nb_file}"]))
    out.append(("p",
        "This runs every cell from the top to the bottom and saves the results into "
        "the notebook file. Every check of the notebook stops it with an error "
        "message (AssertionError) when it fails. If the command ends with a line "
        f"that starts with [NbConvertApp] Writing and shows no error, every check "
        "passed; open the notebook with the command of the previous step (without "
        "running the cells again) to read the printed lines and see the figures."))
    step += 1

    # Step: what you must see --------------------------------------------------------
    out.append(("step", f"Step {step}. What the notebook writes and what you must "
                        "see."))
    files = list(facts["files_written"])
    figures = [path for path in files if path.endswith(".png")]
    out.append(("p",
        f"The notebook writes (or overwrites) these files: {_join(files)}. "
        + ("It changes no other file of the repository"
           + (" except the Rust build folder target next to each Cargo.toml it "
              "builds" if rust else "")
           + ". To get the original files of the repository back, run "
             "git checkout -- Revision/textbook in the repository folder.")))
    out.append(("p",
        "At the end of the notebook (the output of its last code cell) you must see "
        "exactly these lines:"))
    out.append(("cmd", "", list(facts["final_lines"])))
    out.append(("p",
        f"and the notebook must show {len(figures)} figure"
        f"{'' if len(figures) == 1 else 's'} below the cells that draw "
        f"{'it' if len(figures) == 1 else 'them'}."))
    step += 1

    # Step: troubleshooting --------------------------------------------------------
    out.append(("step", f"Step {step}. If something goes wrong."))
    trouble = [
        "\"ModuleNotFoundError: No module named ...\" in the notebook: JupyterLab was "
        "started without the environment. Stop it (menu File > Shut Down), do Step 4, "
        "and start it again.",
        "\"FileNotFoundError: The repository folder was not found\": the notebook was "
        "opened from a copy outside the repository. Open the file "
        f"{nb_file} inside the folder {REPOSITORY_FOLDER}.",
        "Windows: \"py is not recognized\": use python instead of py -3; \"python is "
        "not recognized\": install Python again and tick \"Add python.exe to PATH\".",
        "Linux: \"ensurepip is not available\" when the environment is created: run "
        "sudo apt install python3-venv and repeat Step 3.",
        "\"jupyter is not recognized\" or \"command not found: jupyter\": the "
        "environment is not active; do Step 4 (or type python -m jupyter instead of "
        "jupyter).",
        "An AssertionError names a check that failed: choose the menu Kernel > Restart "
        "Kernel and Run All Cells; if it fails again, install the packages again with "
        "the pip commands of Step 3, because a different package version can change "
        "the last digits of a result.",
    ]
    if rust:
        trouble += [
            "\"cargo is not recognized\" or \"command not found: cargo\": open a new "
            "terminal after installing Rust and do Step 4 again.",
            "\"linker link.exe not found\" (Windows) or \"linker cc not found\" "
            "(Linux): install the C++ Build Tools (Windows) or build-essential "
            "(Linux) as described in Step 5 and build again.",
        ]
    trouble += [f"{symptom}: {fix}" for symptom, fix in facts["troubleshooting"]]
    out.append(("list", trouble))
    return out


# --------------------------------------------------------------------------- render

def book_markdown(facts: dict) -> str:
    """Body of the book section "How to run Notebook NN<x>" (no heading)."""
    lines: list[str] = []
    for block in blocks(facts):
        kind = block[0]
        if kind == "step":
            lines += [f"**{block[1]}**", ""]
        elif kind == "p":
            lines += [block[1], ""]
        elif kind == "list":
            lines += [f"- {item}" for item in block[1]] + [""]
        elif kind == "cmd":
            if block[1]:
                lines += [block[1], ""]
            lines += ["```text"] + list(block[2]) + ["```", ""]
    return "\n".join(lines).rstrip("\n") + "\n"


def _wrap(text: str, width: int, first: str = "", rest: str = "") -> list[str]:
    return textwrap.wrap(text, width=width, initial_indent=first,
                         subsequent_indent=rest, break_long_words=False,
                         break_on_hyphens=False) or [first.rstrip()]


def notebook_markdown(facts: dict) -> str:
    """The notebook's markdown cell "## 2. How to run this notebook"."""
    lines = ["## 2. How to run this notebook", ""]
    for block in blocks(facts):
        kind = block[0]
        if kind == "step":
            lines += _wrap(f"**{block[1]}**", MAX_LINE) + [""]
        elif kind == "p":
            lines += _wrap(block[1], MAX_LINE) + [""]
        elif kind == "list":
            for item in block[1]:
                lines += _wrap(item, MAX_LINE, "- ", "  ")
            lines += [""]
        elif kind == "cmd":
            if block[1]:
                lines += _wrap(block[1], MAX_LINE) + [""]
            lines += ["    " + command for command in block[2]] + [""]
    lines += _wrap(
        "The first code cell below (the set-up cell) repeats these instructions as "
        "comments; then it imports the packages, finds the repository folder and "
        "defines the helpers save_figure (saves and shows a figure), check (an assert "
        "statement that prints a PASS line) and all_checks_passed (prints the last "
        "line).", MAX_LINE)
    return "\n".join(lines).rstrip("\n")


def code_comments(facts: dict) -> str:
    """The instructions as "#" comment lines (top of the first code cell)."""
    width = MAX_LINE
    lines = [f"# HOW TO RUN NOTEBOOK {facts['id']} (complete instructions)", "#"]
    for block in blocks(facts):
        kind = block[0]
        if kind == "step":
            lines += _wrap(block[1].upper(), width, "# ", "# ")
        elif kind == "p":
            lines += _wrap(block[1], width, "# ", "# ")
        elif kind == "list":
            for item in block[1]:
                lines += _wrap(item, width, "# - ", "#   ")
        elif kind == "cmd":
            if block[1]:
                lines += _wrap(block[1], width, "# ", "# ")
            lines += ["#     " + command for command in block[2]]
        lines.append("#")
    lines.append("# " + "-" * (width - 2))
    return "\n".join(lines)


def check_renderings(facts: dict) -> list[str]:
    """Problems of the three renderings (line length, ASCII, references)."""
    problems: list[str] = []
    renderings = {
        "book": book_markdown(facts),
        "notebook": notebook_markdown(facts),
        "comments": code_comments(facts),
    }
    for label, text in renderings.items():
        if not text.isascii():
            problems.append(f"{label}: not ASCII")
        if "\t" in text:
            problems.append(f"{label}: contains a tab")
        if FORBIDDEN_REFERENCES.search(text):
            match = FORBIDDEN_REFERENCES.search(text)
            problems.append(f"{label}: refers to another place ({match.group()!r})")
        limit_lines = text.splitlines() if label != "book" else [
            line for line in _fenced_lines(text)]
        for number, line in enumerate(limit_lines, 1):
            if len(line) > MAX_LINE:
                problems.append(f"{label}: line {number} has {len(line)} characters")
    if "```" in renderings["notebook"] or "```" in renderings["comments"]:
        problems.append("notebook/comments rendering contains ```")
    return problems


def _fenced_lines(text: str) -> list[str]:
    inside = False
    lines = []
    for line in text.splitlines():
        if line.strip().startswith("```"):
            inside = not inside
            continue
        if inside:
            lines.append(line)
    return lines


def facts_from_notebook(path: Path) -> dict:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return notebook["metadata"]["textbook"]["facts"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--format", choices=("book", "notebook", "comments"),
                        default="book")
    arguments = parser.parse_args(argv)
    facts = facts_from_notebook(arguments.notebook)
    render = {"book": book_markdown, "notebook": notebook_markdown,
              "comments": code_comments}[arguments.format]
    sys.stdout.write(render(facts).rstrip("\n") + "\n")
    problems = check_renderings(facts)
    for problem in problems:
        print(f"problem={problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
