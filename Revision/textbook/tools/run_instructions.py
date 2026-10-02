#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""The complete, self-contained run instructions of a textbook notebook.

Written 2026-10-02 for the textbook "Universes in Pairs" (Revision/textbook/TEXTBOOK_SPEC.md
section 3).  Every notebook of the book is preceded in the book by a section "How to run
Notebook NN<x>" whose text says, IN FULL and without referring the student to any other
place of the book or to any other file: what the notebook needs, how to get the
repository, how to create and activate a private Python environment and install the
pinned packages on Windows (PowerShell), macOS (zsh) and Linux (bash), how to install
Rust and build the Rust programs when the notebook needs them, how to start JupyterLab in
the notebooks folder and run all cells (or run the notebook headless), how long it takes,
which files it writes, which final lines the student must see, and how to fix the most
likely errors.

The same instructions appear in four places, generated here from ONE list of blocks so
that they never disagree:

  book_markdown(facts)      the body of the book section "How to run Notebook NN<x>"
                            (the Markdown subset of scripts/build_dissertation_tex.py:
                            bold step lines, paragraphs, one-line "- " list items and
                            fenced ```text command blocks; commands, paths and file
                            names inside sentences are code spans, which the PDF builder
                            may break at any character, so no line overflows);
  notebook_markdown(facts)  the notebook's markdown cell "## 2. How to run this
                            notebook" (lines of at most 89 characters; command blocks
                            indented by four spaces, because a notebook cell must never
                            contain ```, which would end the fenced block of the book);
  code_comments(facts)      the same text as "#" comment lines for the top of the
                            notebook's first code cell (at most 89 characters per line;
                            the code-span backticks are left out);
  the provenance file       Revision/textbook/tools/nbkit.py copies book_markdown(facts)
                            into the notebook's X.PROVENANCE.md.

All renderings are pure ASCII.  The facts are the FACTS dict of the notebook's builder
(every key is documented in FACTS_DOCUMENTATION below and in tools/README.md);
validate_facts() checks them.  The pinned package versions are read from the [direct]
block of Revision/textbook/requirements.txt.

Command line (from the repository root):
    python Revision/textbook/tools/run_instructions.py NOTEBOOK.ipynb [--format F]
with F = book (default), notebook or comments; the facts are read from the executed
notebook's metadata (key "textbook").  Exit code 1 when a rendering breaks a rule.
"""

from __future__ import annotations

import argparse
import json
import math
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
COMMAND_MAX = MAX_LINE - 6  # "#     " prefix of a command in the code comments
NAME_MAX = 25  # "jupyter nbconvert ... --inplace NAME.ipynb" must fit COMMAND_MAX
HEADLESS = "jupyter nbconvert --to notebook --execute --inplace"

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
# Characters that would change meaning in the book's Markdown subset ($ starts math,
# * emphasis, [ ] links) and are therefore not allowed in the free-text FACTS.
FORBIDDEN_PROSE_CHARACTERS = "$*[]\t"
# Character pairs that TeX's fonts print as ONE other character (a dash, a guillemet,
# a curly quote), also inside code spans: never in prose; commands that contain them
# (for example "--version") go into command blocks, which are printed verbatim.
LIGATURES = ("--", "<<", ">>", "``", "''")

FACTS_DOCUMENTATION = {
    "id": "two digits and a letter, e.g. '03b' (chapter 03, second example)",
    "name": "the notebook file name without .ipynb: the id, '_' and lower-case words "
            f"joined by '_', at most {NAME_MAX} characters, e.g. '03b_curvature'",
    "title": "one line: the notebook's title, e.g. 'The curvature of the author's metric'",
    "purpose": "one or more sentences: what the notebook computes and checks",
    "records": "list of [path, what]: every Revision record (file or folder under "
               "Revision/, not Revision/textbook/) the notebook reads or reproduces; "
               "[] when it uses none",
    "packages": "list of the pinned [direct] packages the notebook imports",
    "needs_rust": "list of {'manifest': 'Revision/.../Cargo.toml', 'binaries': [names "
                  "without .exe], 'build_minutes': number}; [] when Rust is not needed",
    "expected_seconds": "number: typical run time of the whole notebook in seconds",
    "timeout_seconds": "int: the limit per cell for nbkit (at least 2 x expected)",
    "files_written": "list of every repository-relative file the notebook writes "
                     "(figures, the captions sidecar, data files), in the order written",
    "final_lines": "list of the exact last lines printed by the last code cell",
    "troubleshooting": "list of [symptom, fix] or [symptom, fix, [command, ...]] "
                       "specific to this notebook ([] if none); a command is printed "
                       "verbatim in a command block after the fix",
    "allow_stderr": "optional bool: allow output on stderr (default False)",
    "network": "optional str: what the notebook downloads while it runs (default: "
               "nothing)",
}
REQUIRED_KEYS = {
    "id": str,
    "name": str,
    "title": str,
    "purpose": str,
    "records": list,
    "packages": list,
    "needs_rust": list,
    "expected_seconds": (int, float),
    "timeout_seconds": int,
    "files_written": list,
    "final_lines": list,
    "troubleshooting": list,
}
OPTIONAL_KEYS = {"allow_stderr": bool, "network": str}
RUST_KEYS = {"manifest": str, "binaries": list, "build_minutes": (int, float)}


# --------------------------------------------------------------------------- pins

PIN_PATTERN = re.compile(
    r"([A-Za-z0-9_.-]+)==([A-Za-z0-9_.+-]+)(?:\s*;\s*(\S.*))?")


def load_pins(path: Path = REQUIREMENTS) -> tuple[list[tuple[str, str]],
                                                   list[tuple[str, str]]]:
    """(direct, support) lists of (package, version) from requirements.txt.

    A pin is NAME==VERSION, optionally followed by "; <environment marker>"."""
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
        match = PIN_PATTERN.fullmatch(line)
        if match is None or block is None:
            raise ValueError(f"{path}: cannot read the pin {raw!r}")
        block.append((match.group(1), match.group(2)))
    if not direct:
        raise ValueError(f"{path}: no [direct] block")
    return direct, support


WINDOWS_ONLY_MARKERS = {"colorama": 'sys_platform == "win32"',
                        "pywinpty": 'os_name == "nt"'}


def _normalise_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def requirement_closure(direct_names: list[str]) -> dict[str, tuple[str, str]]:
    """{normalised name: (distribution name, installed version)} of every installed
    package that the packages direct_names need in order to run, extras included.

    Requirements whose environment marker is false on this computer are skipped; a
    requirement requested with extras (pkg[extra]) adds the extra's requirements."""
    import importlib.metadata as metadata
    from packaging.markers import default_environment
    from packaging.requirements import Requirement

    environment = default_environment()
    found: dict[str, tuple[str, str]] = {}
    visited: set[tuple[str, frozenset]] = set()
    stack = [(name, frozenset()) for name in direct_names]
    while stack:
        name, extras = stack.pop()
        key = _normalise_name(name)
        if (key, extras) in visited:
            continue
        visited.add((key, extras))
        distribution = metadata.distribution(name)
        found[key] = (distribution.metadata["Name"], distribution.version)
        for text in distribution.requires or []:
            requirement = Requirement(text)
            if requirement.marker is not None and not any(
                    requirement.marker.evaluate(dict(environment, extra=extra))
                    for extra in [""] + sorted(extras)):
                continue
            stack.append((requirement.name, frozenset(requirement.extras)))
    return found


def check_requirements(path: Path = REQUIREMENTS) -> list[str]:
    """Problems of requirements.txt against the installed packages (empty if none):
    every [direct] and [support] pin equals the installed version, [support] is the
    complete closure of [direct] minus [direct], and the Windows-only packages carry
    their environment markers."""
    import importlib.metadata as metadata

    problems: list[str] = []
    direct, support = load_pins(path)
    direct_names = [name for name, _ in direct]
    for name, version in direct + support:
        try:
            installed = metadata.version(name)
        except metadata.PackageNotFoundError:
            problems.append(f"{name} is pinned ({version}) but not installed")
            continue
        if installed != version:
            problems.append(f"{name} is pinned at {version} but {installed} is installed")
    closure = requirement_closure(direct_names)
    expected = {key for key in closure} - {_normalise_name(n) for n in direct_names}
    pinned = {_normalise_name(name) for name, _ in support}
    for key in sorted(expected - pinned):
        problems.append(f"{closure[key][0]}=={closure[key][1]} is needed but not pinned "
                        "in [support]")
    for key in sorted(pinned - expected):
        problems.append(f"{key} is pinned in [support] but not needed by [direct]")
    text = path.read_text(encoding="utf-8")
    for name, marker in WINDOWS_ONLY_MARKERS.items():
        if name in pinned and not re.search(
                rf"(?im)^{re.escape(name)}==\S+; {re.escape(marker)}$", text):
            problems.append(f"{name} must carry the marker '; {marker}'")
    return problems


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

def _prose_problems(label: str, text: str) -> list[str]:
    problems = []
    bad = sorted({c for c in text if c in FORBIDDEN_PROSE_CHARACTERS})
    if bad:
        problems.append(f"{label} contains {bad!r} (not allowed in run instructions; "
                        "write commands and paths as `code spans`)")
    if text.count("`") % 2:
        problems.append(f"{label} has an unpaired ` (code spans must be closed)")
    if "```" in text:
        problems.append(f"{label} contains ```")
    for sequence in LIGATURES:
        if sequence in text:
            problems.append(f"{label} contains {sequence!r}, which the PDF prints as "
                            "one other character (put such a command in the third "
                            "element of a troubleshooting entry)")
    if FORBIDDEN_REFERENCES.search(text):
        problems.append(f"{label} refers to another place "
                        f"({FORBIDDEN_REFERENCES.search(text).group()!r}); the run "
                        "instructions must be self-contained")
    return problems


def validate_facts(facts: dict) -> list[str]:
    """Problems with a FACTS dict (empty list when it is valid)."""
    problems: list[str] = []
    if not isinstance(facts, dict):
        return ["FACTS must be a dict"]
    for key, kind in REQUIRED_KEYS.items():
        if key not in facts:
            problems.append(f"FACTS lacks the key {key!r} ({FACTS_DOCUMENTATION[key]})")
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
    if not json.dumps(facts, ensure_ascii=False).isascii():
        problems.append("FACTS must be ASCII only")
    if not ID_PATTERN.fullmatch(facts["id"]):
        problems.append("FACTS['id'] must be two digits and a letter, e.g. '03b'")
    name = NAME_PATTERN.fullmatch(facts["name"])
    if name is None or name.group(1) != facts["id"]:
        problems.append(f"FACTS['name']: {FACTS_DOCUMENTATION['name']}")
    if len(facts["name"]) > NAME_MAX:
        problems.append(f"FACTS['name'] has {len(facts['name'])} characters; at most "
                        f"{NAME_MAX} (the headless command must fit one comment line)")
    for key in ("title", "purpose"):
        if "\n" in facts[key] or not facts[key].strip():
            problems.append(f"FACTS[{key!r}] must be one non-empty line")
        problems += _prose_problems(f"FACTS[{key!r}]", facts[key])
    if facts["title"].rstrip().endswith("."):
        problems.append("FACTS['title'] must not end with a full stop")
    if not facts["purpose"].rstrip().endswith("."):
        problems.append("FACTS['purpose'] must end with a full stop")
    for entry in facts["records"]:
        if not (isinstance(entry, (list, tuple)) and len(entry) == 2
                and all(isinstance(part, str) and part.strip() for part in entry)):
            problems.append("every records entry must be [path, what] (two strings)")
            continue
        path, what = entry
        if not REPO_PATH_PATTERN.fullmatch(path) or not path.startswith("Revision/") \
                or path.startswith("Revision/textbook/"):
            problems.append(f"record {path!r} must be a repository-relative path under "
                            "Revision/ (not Revision/textbook/)")
        elif not (ROOT / path.rstrip("/")).exists():
            problems.append(f"record {path!r} does not exist")
        problems += _prose_problems(f"the description of record {path!r}", what)
    try:
        direct, _ = load_pins()
    except (OSError, ValueError) as error:
        problems.append(str(error))
        direct = []
    pinned = [package for package, _ in direct]
    for package in facts["packages"]:
        if package not in pinned:
            problems.append(f"package {package!r} is not pinned in [direct] of "
                            "Revision/textbook/requirements.txt")
    if not facts["packages"]:
        problems.append("FACTS['packages'] is empty")
    if len(set(facts["packages"])) != len(facts["packages"]):
        problems.append("FACTS['packages'] lists a package twice")
    for entry in facts["needs_rust"]:
        if not isinstance(entry, dict):
            problems.append("every needs_rust entry must be a dict")
            continue
        for key, kind in RUST_KEYS.items():
            if key not in entry or not isinstance(entry[key], kind) or isinstance(
                    entry[key], bool):
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
            elif len(cargo_command(manifest)) > COMMAND_MAX:
                problems.append(f"the cargo command for {manifest!r} is longer than "
                                f"{COMMAND_MAX} characters")
        binaries = entry.get("binaries", [])
        if not isinstance(binaries, list) or not binaries:
            problems.append("needs_rust entry: 'binaries' must be a non-empty list")
            binaries = []
        for binary in binaries:
            if not isinstance(binary, str) or not re.fullmatch(r"[a-z0-9_-]+", binary):
                problems.append(f"binary name {binary!r} must be lower-case "
                                "letters, digits, '_' or '-' (without .exe)")
    if len(set(facts["files_written"])) != len(facts["files_written"]):
        problems.append("FACTS['files_written'] lists a file twice")
    for path in facts["files_written"]:
        if not isinstance(path, str) or not REPO_PATH_PATTERN.fullmatch(path) \
                or path.endswith("/"):
            problems.append(f"files_written entry {path!r} must be a "
                            "repository-relative file path with '/' separators")
        elif not path.startswith("Revision/textbook/"):
            problems.append(f"files_written entry {path!r}: a notebook writes only "
                            "below Revision/textbook/")
    if not facts["final_lines"]:
        problems.append("FACTS['final_lines'] is empty")
    for line in facts["final_lines"]:
        if not isinstance(line, str) or not line.isascii() or len(line) > COMMAND_MAX \
                or not line.strip() or "\n" in line or line != line.rstrip():
            problems.append(f"final line {line!r} must be one non-empty ASCII line of "
                            f"at most {COMMAND_MAX} characters without trailing blanks")
    for item in facts["troubleshooting"]:
        if not (isinstance(item, (list, tuple)) and len(item) in (2, 3)
                and all(isinstance(part, str) and part.strip() for part in item[:2])):
            problems.append("every troubleshooting entry must be [symptom, fix] or "
                            "[symptom, fix, [command, ...]] (non-empty strings)")
            continue
        problems += _prose_problems("a troubleshooting entry", item[0] + " " + item[1])
        if len(item) == 3:
            commands = item[2]
            if not (isinstance(commands, (list, tuple)) and commands and all(
                    isinstance(c, str) and c.strip() and c.isascii() and "\n" not in c
                    and len(c) <= COMMAND_MAX and "`" not in c and "'" not in c
                    for c in commands)):
                problems.append("the commands of a troubleshooting entry must be a "
                                f"non-empty list of ASCII lines of at most {COMMAND_MAX} "
                                "characters without ' and ` (the PDF prints them as "
                                "curly quotes; use double quotes)")
    if isinstance(facts.get("network"), str):
        problems += _prose_problems("FACTS['network']", facts["network"])
    if not facts["expected_seconds"] > 0:
        problems.append("FACTS['expected_seconds'] must be positive")
    if facts["timeout_seconds"] < 2 * facts["expected_seconds"]:
        problems.append("timeout_seconds must be at least twice expected_seconds")
    return problems


def notebook_file(facts: dict) -> str:
    return f"{NOTEBOOK_FOLDER}/{facts['name']}.ipynb"


def cargo_command(manifest: str) -> str:
    return f"cargo build --release --manifest-path {manifest}"


def run_time_text(seconds: float) -> str:
    """'about 10 seconds', 'about 1 minute', 'about 3 minutes'."""
    if seconds < 55:
        value = max(5, 5 * math.ceil(seconds / 5))
        return f"about {value} seconds"
    minutes = max(1, math.ceil(seconds / 60))
    return f"about {minutes} minute{'' if minutes == 1 else 's'}"


def _join(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]


def _binary_paths(entry: dict) -> list[str]:
    folder = entry["manifest"].rsplit("/", 1)[0]
    return [f"`{folder}/target/release/{binary}`" for binary in entry["binaries"]]


# --------------------------------------------------------------------------- blocks
# A block is ("step", text) | ("p", text) | ("list", [items]) | ("cmd", label, [lines]).
# Free text may contain `code spans`; they are kept in the book and notebook renderings
# and their backticks are dropped in the code comments.

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
        f"Notebook {facts['id']} ({facts['title']}) is the file `{nb_file}` of the "
        f"repository {REPOSITORY_FOLDER}. {facts['purpose']} It needs a computer with "
        "Windows 11, macOS or Linux, an internet connection for the installation, the "
        f"program Git, and Python {PYTHON_MINIMUM} or newer (the notebooks were built "
        f"with Python {PYTHON_BUILT}) with these packages at exactly these versions: "
        f"{pins}. The notebook itself imports {used}; the other packages run Jupyter, "
        "the program that shows and runs notebooks."
    )
    if rust:
        programs = _join([b for entry in rust for b in entry["binaries"]])
        plural = sum(len(entry["binaries"]) for entry in rust) > 1
        sentence += (
            f" It also needs Rust (the program cargo, version {CARGO_BUILT} or newer), "
            f"because it runs the Rust program{'s' if plural else ''} {programs}, which "
            f"{'are' if plural else 'is'} part of the repository and "
            f"{'are' if plural else 'is'} built on your computer."
        )
    else:
        sentence += " It does not need Rust."
    out.append(("p", sentence))

    # Step 2 -------------------------------------------------------------------
    out.append(("step", "Step 2. Install Git and Python (once per computer)."))
    out.append(("p",
        "A terminal is the window in which you type commands: on Windows the app "
        "Windows PowerShell (or Terminal), on macOS the app Terminal (it runs the shell "
        "zsh), on Linux any terminal (it runs the shell bash). Type every command of "
        "this section into a terminal exactly as printed, one line at a time, and press "
        "Enter after each line."))
    out.append(("p",
        "Windows: download Git from https://git-scm.com/download/win and install it "
        "with the default choices. Download Python from "
        "https://www.python.org/downloads/ and run the installer; in its first window "
        "tick the box \"Add python.exe to PATH\" before you click \"Install Now\"."))
    out.append(("p",
        "macOS: download Python from https://www.python.org/downloads/ and run the "
        "installer. Then open the app Terminal and run this command, which installs Git "
        "and the compiler tools:"))
    out.append(("cmd", "macOS (zsh):", ["xcode-select --install"]))
    out.append(("p",
        "Linux (Debian or Ubuntu; other distributions have packages of the same names): "
        "run these two commands:"))
    out.append(("cmd", "Linux (bash):",
                ["sudo apt update", "sudo apt install git python3 python3-venv"]))
    out.append(("p",
        "Then close the terminal and open a NEW one (a terminal opened before the "
        "installation does not know the new programs), and check the version of "
        f"Python; it must print {PYTHON_MINIMUM} or a higher number:"))
    out.append(("cmd", "Windows (PowerShell):", ["py -3 --version"]))
    out.append(("cmd", "macOS (zsh) and Linux (bash):", ["python3 --version"]))
    out.append(("p",
        "If an older Linux prints a lower number (Ubuntu 22.04 has Python 3.10), "
        "install Python 3.12 with the following three commands, and in Step 3 type "
        "`python3.12` instead of `python3` in the command that creates the "
        "environment:"))
    out.append(("cmd", "Linux (bash), only when the version is too low:", [
        "sudo add-apt-repository ppa:deadsnakes/ppa",
        "sudo apt update",
        "sudo apt install python3.12 python3.12-venv",
    ]))

    # Step 3 -------------------------------------------------------------------
    out.append(("step", "Step 3. Get the repository and install the packages "
                        "(once per computer)."))
    out.append(("p",
        f"The commands below download the repository (about 130 MB; the folder then "
        f"takes about 400 MB of disk space) into the folder "
        f"{REPOSITORY_FOLDER} inside your home folder, create a private Python "
        f"environment in the folder {ENVIRONMENT} inside your home folder (a private "
        "environment is a folder with its own copy of Python and of the packages, so "
        "that nothing else on your computer is changed), activate it (from then on the "
        "commands `python` and `jupyter` typed in this terminal are those of the "
        f"environment, and the prompt starts with ({ENVIRONMENT})), and install the "
        "packages at the pinned versions (this downloads about 90 MB and takes a few "
        "minutes; the environment takes about 400 MB of disk space). If you have done "
        "this step before, for this or for another notebook, "
        "skip it and go to Step 4; to get the newest version of the repository, run "
        "`git pull` in the repository folder after Step 4."))
    pip = ["python -m pip install --upgrade pip"] + pip_commands(direct)
    out.append(("cmd", "Windows (PowerShell):", [
        "cd $HOME",
        f"git clone {REPOSITORY_URL}",
        f"py -3 -m venv \"$HOME\\{ENVIRONMENT}\"",
        "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force",
        f"& \"$HOME\\{ENVIRONMENT}\\Scripts\\Activate.ps1\"",
    ] + pip))
    out.append(("p",
        "The line with `Set-ExecutionPolicy` allows PowerShell to run the activation "
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
        "Run these lines whenever you open a new terminal (they do no harm if the "
        "environment is already active):"))
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
            "Windows: download `rustup-init.exe` from https://rustup.rs, run it and "
            "accept the default choices; if it reports that the Visual Studio C++ Build "
            "Tools are missing, let it install them (or install the workload \"Desktop "
            "development with C++\" from "
            "https://visualstudio.microsoft.com/visual-cpp-build-tools/ and run "
            "`rustup-init.exe` again). macOS and Linux: run the command below and accept "
            "the default choice (on Linux first run `sudo apt install build-essential`, "
            "which provides the linker that Rust needs)."))
        out.append(("cmd", "macOS (zsh) and Linux (bash):", [
            # Double quotes: the PDF prints a straight single quote as a curly one, and
            # zsh would expand an unquoted =https.
            'curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh',
        ]))
        out.append(("p",
            "Then close the terminal, open a new one, do Step 4 again, and check the "
            f"version of cargo; it must print {CARGO_BUILT} or a newer version:"))
        out.append(("cmd", "Windows, macOS and Linux:", ["cargo --version"]))
        out.append(("p",
            "Build the program with the following command, in the repository folder "
            "(the same command on all three systems):"))
        out.append(("cmd", "Windows, macOS and Linux:",
                    [cargo_command(entry["manifest"]) for entry in rust]))
        for entry in rust:
            minutes = entry["build_minutes"]
            out.append(("p",
                f"The first build takes about {minutes:g} minute"
                f"{'' if minutes == 1 else 's'}; later builds reuse the result and take "
                "a few seconds. The program is then the file "
                f"{_join(_binary_paths(entry))} (on Windows with the ending `.exe`). "
                "The notebook runs the same build command itself before it uses the "
                "program (it takes a second when the program is up to date), so the "
                "notebook also works if you skip this build; building here first shows "
                "any problem with Rust before the notebook starts."))
        step += 1

    # Step: JupyterLab -----------------------------------------------------------
    out.append(("step", f"Step {step}. Run the notebook in JupyterLab."))
    out.append(("p", "In the repository folder, with the environment active, run these "
                     "two lines (the first one goes into the folder of the notebooks):"))
    out.append(("cmd", "Windows, macOS and Linux:",
                [f"cd {NOTEBOOK_FOLDER}", f"jupyter lab {nb_name}"]))
    out.append(("p",
        "JupyterLab opens in your web browser and shows the notebook (if no browser "
        "window opens, copy the address that starts with `http://localhost:8888/lab` "
        "from the terminal into the address bar of your browser). The name at the top "
        "right of the notebook must read Python 3 (ipykernel). Choose the menu "
        "Run > Run All Cells. While a cell runs, the label to its left shows `[*]`; "
        "when it has finished, the label shows a number. The notebook has finished "
        "when the last code cell shows a number; this takes "
        f"{run_time_text(facts['expected_seconds'])} on a typical laptop. Scroll to "
        "the end and compare the last printed lines with the lines in the step "
        "\"What the notebook writes and what you must see\" below. To keep the "
        "results, save the notebook (menu File > Save Notebook). To stop JupyterLab, "
        "choose the menu File > Shut Down, or press Ctrl+C twice in the terminal."))
    step += 1

    # Step: headless ---------------------------------------------------------------
    out.append(("step", f"Step {step}. Or run the notebook without a browser "
                        "(headless)."))
    out.append(("p", "In the repository folder, with the environment active, run:"))
    out.append(("cmd", "Windows, macOS and Linux:",
                [f"cd {NOTEBOOK_FOLDER}", f"{HEADLESS} {nb_name}"]))
    out.append(("p",
        "This runs every cell from the top to the bottom and saves the results into "
        "the notebook file. A failed check stops it with an error message that "
        "contains AssertionError and the name of the check. If the command ends with a "
        "line that starts with `[NbConvertApp] Writing` and shows no error, every "
        f"check passed; open the notebook with `jupyter lab {nb_name}` (in the same "
        "folder, without running the cells again) to read the printed lines and see "
        "the figures."))
    step += 1

    # Step: what you must see --------------------------------------------------------
    out.append(("step", f"Step {step}. What the notebook writes and what you must "
                        "see."))
    files = list(facts["files_written"])
    figures = [path for path in files if path.endswith(".png")]
    if files:
        written = ("The notebook writes (or overwrites) these files: "
                   + _join([f"`{path}`" for path in files]) + ".")
    else:
        written = "The notebook writes no file."
    network = facts.get("network", "")
    out.append(("p",
        written
        + " It changes no other file of the repository"
        + (" except the Rust build folder `target` next to each `Cargo.toml` it "
           "builds" if rust else "")
        + "; running it headless or saving it in JupyterLab also rewrites the notebook "
          "file itself. "
        + (f"While it runs it uses the internet: {network} " if network else
           "It does not use the internet while it runs. ")
        + "The files it writes are the same files that are stored in the repository "
          "(on another computer a figure may differ in a few bytes, which is harmless). "
          "To get the stored versions back, run this command in the repository folder "
          "(it also undoes every change you made yourself in the folder "
          "Revision/textbook):"))
    out.append(("cmd", "Windows, macOS and Linux:",
                ["git checkout -- Revision/textbook"]))
    out.append(("p",
        "Every check of the notebook prints a line that starts with PASS. At the end "
        "of the notebook (the output of its last code cell) you must see exactly these "
        "lines:"))
    out.append(("cmd", "", list(facts["final_lines"])))
    if figures:
        out.append(("p",
            f"and the notebook must show {len(figures)} figure"
            f"{'' if len(figures) == 1 else 's'} below the cells that draw "
            f"{'it' if len(figures) == 1 else 'them'}."))
    else:
        out.append(("p", "The notebook draws no figure."))
    step += 1

    # Step: troubleshooting --------------------------------------------------------
    out.append(("step", f"Step {step}. If something goes wrong."))
    # Every item is (text, commands); the commands are printed as a command block.
    trouble: list[tuple[str, list[str]]] = [
        ("\"ModuleNotFoundError: No module named ...\" in the notebook: JupyterLab was "
         "started without the environment. Stop it (menu File > Shut Down), do Step 4, "
         "and start it again. If the error remains, another Python installation has "
         "registered its own kernel called python3; with the environment active, run "
         "the following command and start JupyterLab again:",
         ["python -m ipykernel install --user --name python3"]),
        ("\"FileNotFoundError: The repository folder was not found\": the notebook was "
         "opened from a copy outside the repository. Open the file "
         f"`{nb_file}` inside the folder {REPOSITORY_FOLDER}.", []),
        ("\"fatal: destination path 'Dirac_claude' already exists\" in Step 3: the "
         "repository was downloaded before; skip the line with `git clone`.", []),
        ("Windows: \"running scripts is disabled on this system\": run the line with "
         "`Set-ExecutionPolicy` and then the activation line again. \"py is not "
         "recognized\": use `python` instead of `py -3`; \"python is not recognized\": "
         "install Python again and tick \"Add python.exe to PATH\".", []),
        ("Linux: \"ensurepip is not available\" when the environment is created: run "
         "`sudo apt install python3-venv` and repeat Step 3.", []),
        ("\"jupyter is not recognized\" or \"command not found: jupyter\": the "
         "environment is not active; do Step 4 (or type `python -m jupyter` instead of "
         "`jupyter`).", []),
        ("Windows: the headless run prints a RuntimeWarning that mentions the "
         "\"Proactor event loop\" and zmq: this is a message of the package pyzmq, not "
         "an error; the run continues normally.", []),
        ("A red box with \"Matplotlib is building the font cache; this may take a "
         "moment.\" in the first run after the installation: this is a message, not an "
         "error; the run continues and the message does not come again.", []),
        ("An AssertionError names a check that failed: choose the menu Kernel > Restart "
         "Kernel and Run All Cells; if it fails again, install the packages again with "
         "the pip commands of Step 3, because a different package version can change "
         "the last digits of a result.", []),
    ]
    if rust:
        trouble += [
            ("\"cargo is not recognized\" or \"command not found: cargo\" or \"cargo was "
             "not found\": open a new terminal after installing Rust, do Step 4 again, "
             "and start JupyterLab from this terminal.", []),
            ("\"linker link.exe not found\" (Windows) or \"linker cc not found\" "
             "(Linux): install the C++ Build Tools (Windows) or build-essential "
             "(Linux) as described in Step 5 and build again.", []),
        ]
    for entry in facts["troubleshooting"]:
        commands = list(entry[2]) if len(entry) == 3 else []
        trouble.append((f"{entry[0]}: {entry[1]}", commands))
    out.append(("list", trouble))
    return out


# --------------------------------------------------------------------------- render

def _items(block: tuple) -> list[tuple[str, list[str]]]:
    """The items of a "list" block as (text, commands)."""
    return [(item, []) if isinstance(item, str) else (item[0], list(item[1]))
            for item in block[1]]


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
            # Consecutive items form one list; an item with commands is followed by a
            # fenced block (which ends the list; the next item starts a new one).
            for text, commands in _items(block):
                lines.append(f"- {text}")
                if commands:
                    lines += ["", "```text"] + commands + ["```", ""]
            if lines[-1] != "":
                lines.append("")
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
            for text, commands in _items(block):
                lines += _wrap(text, MAX_LINE, "- ", "  ")
                if commands:  # a code block inside the list item: six blanks
                    lines += [""] + ["      " + command for command in commands] + [""]
            if lines[-1] != "":
                lines.append("")
        elif kind == "cmd":
            if block[1]:
                lines += _wrap(block[1], MAX_LINE) + [""]
            lines += ["    " + command for command in block[2]] + [""]
    lines += _wrap(
        "The first code cell below (the set-up cell) repeats these instructions as "
        "comments; then it imports the packages, finds the repository folder and "
        "defines the helpers `save_figure` (saves a figure and shows it), `check` "
        "(stops with an AssertionError when a check fails, prints a PASS line when it "
        "passes), `report` (prints a key number as a RESULT line) and "
        "`all_checks_passed` (prints the last line).", MAX_LINE)
    return "\n".join(lines).rstrip("\n")


def code_comments(facts: dict) -> str:
    """The instructions as "#" comment lines (top of the first code cell)."""
    width = MAX_LINE
    lines = [f"# HOW TO RUN NOTEBOOK {facts['id']} (the complete instructions)", "#"]
    for block in blocks(facts):
        kind = block[0]
        if kind == "step":
            lines += _wrap(block[1].upper(), width, "# ", "# ")
        elif kind == "p":
            lines += _wrap(block[1].replace("`", ""), width, "# ", "# ")
        elif kind == "list":
            for text, commands in _items(block):
                lines += _wrap(text.replace("`", ""), width, "# - ", "#   ")
                lines += ["#     " + command for command in commands]
        elif kind == "cmd":
            if block[1]:
                lines += _wrap(block[1], width, "# ", "# ")
            lines += ["#     " + command for command in block[2]]
        lines.append("#")
    lines.append("# " + "-" * (width - 2))
    return "\n".join(lines)


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


def check_renderings(facts: dict) -> list[str]:
    """Problems of the three renderings (line length, ASCII, references, markup)."""
    problems: list[str] = []
    renderings = {
        "book": book_markdown(facts),
        "notebook": notebook_markdown(facts),
        "comments": code_comments(facts),
    }
    for label, text in renderings.items():
        if not text.isascii():
            problems.append(f"{label}: not ASCII")
        if "\t" in text or "\r" in text:
            problems.append(f"{label}: contains a tab or a carriage return")
        match = FORBIDDEN_REFERENCES.search(text)
        if match:
            problems.append(f"{label}: refers to another place ({match.group()!r})")
        limit_lines = _fenced_lines(text) if label == "book" else text.splitlines()
        for number, line in enumerate(limit_lines, 1):
            if len(line) > MAX_LINE:
                problems.append(f"{label}: line {number} has {len(line)} characters")
    if "```" in renderings["notebook"] or "```" in renderings["comments"]:
        problems.append("notebook/comments rendering contains ```")
    if "`" in renderings["comments"]:
        problems.append("comments rendering contains a backtick")
    commands = [line for block in blocks(facts) if block[0] == "cmd" and block[1]
                for line in block[2]]
    commands += [line for block in blocks(facts) if block[0] == "list"
                 for _, lines in _items(block) for line in lines]
    for line in commands:
        if "'" in line or "`" in line:
            problems.append(f"command {line!r}: the PDF prints ' and ` as curly quotes; "
                            "use double quotes")
    inside = False
    for line in renderings["book"].splitlines():
        if line.startswith("```"):
            inside = not inside
            continue
        if inside:
            continue
        if "$" in line:
            problems.append(f"book: a sentence contains $ (it would start math): {line}")
        for sequence in LIGATURES:
            if sequence in line:
                problems.append(f"book: a sentence contains {sequence!r}, which the PDF "
                                f"prints as one other character: {line[:60]}")
        if line.count("`") % 2:
            problems.append(f"book: unpaired backtick in: {line[:60]}")
        if re.match(r"\d+\.\s", line) or line.startswith("#"):
            problems.append(f"book: a line would become a list item or heading: "
                            f"{line[:60]}")
    return problems


def facts_from_notebook(path: Path) -> dict:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return notebook["metadata"]["textbook"]["facts"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("notebook", type=Path, nargs="?")
    parser.add_argument("--format", choices=("book", "notebook", "comments"),
                        default="book")
    parser.add_argument("--check-requirements", action="store_true",
                        help="check requirements.txt against the installed packages")
    arguments = parser.parse_args(argv)
    if arguments.check_requirements:
        problems = check_requirements()
        for problem in problems:
            print(f"problem={problem}")
        direct, support = load_pins()
        print(f"pins_direct={len(direct)}")
        print(f"pins_support={len(support)}")
        print(f"requirements={'OK' if not problems else 'FAILED'}")
        return 1 if problems else 0
    if arguments.notebook is None:
        parser.error("give a notebook, or --check-requirements")
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
