#!/usr/bin/env python3
"""Build, check and audit the Revision notebooks (Revision/notebooks/<name>.ipynb).

Every Revision notebook is defined by a deterministic BUILDER, the Python file
Revision/notebooks/src/<name>.py.  A builder defines

    NAME   = "<name>"                      (the notebook file is <name>.ipynb)
    TITLE  = "<one-line title>"
    def cells() -> list[tuple[str, str]]   (("markdown" | "code", text), in order)

This tool turns the cells into a notebook, executes it with nbclient in a fresh output folder,
normalises the executed notebook and writes it.  Normalisation makes two executions on the same
computer byte-identical:

  * fixed cell ids cell-000, cell-001, ...;
  * no timing metadata (nbclient runs with record_timing=False and any "execution" metadata is
    removed); cell metadata keeps only "tags";
  * consecutive stream outputs of the same name are merged (the kernel may split one print stream
    into several messages);
  * notebook metadata is fixed (kernelspec python3, language_info {"name": "python"}, and a
    "revision" block naming the builder);
  * JSON with sorted keys, indent 1, UTF-8, LF line ends, one final newline.

Commands (run from any folder; paths are found from this file's location):

    python Revision/notebooks/tools/build_notebooks.py list
    python Revision/notebooks/tools/build_notebooks.py build <name> [--out DIR] [--timeout S]
    python Revision/notebooks/tools/build_notebooks.py check <name> [--out DIR] [--timeout S]
    python Revision/notebooks/tools/build_notebooks.py audit <name>

build   executes the notebook with its outputs in DIR (default: a new folder under
        <repository>/build/revision_notebooks/, which git ignores) and writes
        Revision/notebooks/<name>.ipynb.
check   executes it again with its outputs in DIR (default: a new folder, as above), writes the
        executed notebook into DIR and compares it byte for byte with the committed
        Revision/notebooks/<name>.ipynb; exit status 0 only if they are identical.
audit   checks the structure rules of the committed notebook without executing it (also used by
        Revision/tests/test_revision_notebooks.py).

DIR must not exist or be empty: the tool never deletes anything.  The kernel receives the
environment variable REVISION_NB_OUT=DIR (the notebook writes every output file there) and
PYTHONHASHSEED=0.  The execution time is printed on the console, never stored in the notebook.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import re
import sys
import tempfile
import time
import warnings
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
NB_DIR = TOOLS_DIR.parent                     # Revision/notebooks
SRC_DIR = NB_DIR / "src"
REPO = NB_DIR.parent.parent                   # the repository root
DEFAULT_OUT_PARENT = REPO / "build" / "revision_notebooks"

REQUIRED_HEADINGS = [
    "## 1. What this notebook computes",
    "## 2. How to run this notebook",
    "## 3. The words used in this notebook",
    "## 4. The physical and mathematical situation",
]
FINAL_HEADING_PATTERN = re.compile(r"^## \d+\. What this notebook showed", re.MULTILINE)
RUN_NEEDLES = [
    "Windows 11",
    "macOS (Apple silicon",
    "Linux",
    "-m venv",
    "-m pip install -r Revision/notebooks/requirements.txt",
    "rustup",
    "git clone",
    "-m jupyterlab",
    "-m nbconvert --to notebook --execute",
    "Shift+Enter",
    "Python 3 (ipykernel)",
]
# `python -m jupyter <subcommand>` fails where the jupyter executables are not on PATH, so the
# instructions use `-m jupyterlab` and `-m nbconvert` only.
FORBIDDEN_RUN_TEXT = re.compile(r"-m jupyter(?![\w-])")
TEXT_MIME_SPLIT = ("text/plain", "text/markdown", "text/html", "text/latex")


# --------------------------------------------------------------------------------------------
# builders
# --------------------------------------------------------------------------------------------
def builder_names() -> list[str]:
    return sorted(p.stem for p in SRC_DIR.glob("*.py") if not p.name.startswith("_"))


def load_builder(name: str):
    path = SRC_DIR / f"{name}.py"
    if not path.is_file():
        raise SystemExit(f"no builder {path.relative_to(REPO).as_posix()} (known: {', '.join(builder_names())})")
    spec = importlib.util.spec_from_file_location(f"revision_nb_builder_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if getattr(module, "NAME", None) != name:
        raise SystemExit(f"builder {path.name}: NAME must be {name!r}")
    return module


def unexecuted_notebook(name: str):
    import nbformat

    module = load_builder(name)
    nb = nbformat.v4.new_notebook()
    for kind, text in module.cells():
        text = text.strip("\n") + "\n"
        if kind == "markdown":
            nb.cells.append(nbformat.v4.new_markdown_cell(text.rstrip("\n")))
        elif kind == "code":
            nb.cells.append(nbformat.v4.new_code_cell(text.rstrip("\n")))
        else:
            raise SystemExit(f"builder {name}: unknown cell kind {kind!r}")
    nb.metadata = fixed_metadata(name, module.TITLE)
    return nb


def fixed_metadata(name: str, title: str) -> dict:
    return {
        "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
        "revision": {
            "builder": f"Revision/notebooks/src/{name}.py",
            "tool": "Revision/notebooks/tools/build_notebooks.py",
            "title": title,
        },
    }


# --------------------------------------------------------------------------------------------
# normalisation
# --------------------------------------------------------------------------------------------
def _lines(text) -> list[str]:
    if isinstance(text, list):
        text = "".join(text)
    return text.splitlines(keepends=True)


def _merge_streams(outputs: list) -> list:
    merged: list = []
    for out in outputs:
        if (
            out.get("output_type") == "stream"
            and merged
            and merged[-1].get("output_type") == "stream"
            and merged[-1].get("name") == out.get("name")
        ):
            prev = merged[-1]
            prev["text"] = "".join(_lines(prev["text"])) + "".join(_lines(out["text"]))
        else:
            merged.append(out)
    return merged


def normalise(nb, name: str, title: str) -> str:
    """Return the canonical text of an executed notebook (sorted keys, LF, fixed ids)."""
    data = json.loads(json.dumps(nb))          # plain dicts and lists
    data["metadata"] = fixed_metadata(name, title)
    data["nbformat"], data["nbformat_minor"] = 4, 5
    for i, cell in enumerate(data["cells"]):
        cell["id"] = f"cell-{i:03d}"
        meta = cell.get("metadata", {})
        cell["metadata"] = {k: meta[k] for k in ("tags",) if k in meta}
        cell["source"] = _lines(cell.get("source", ""))
        if cell["cell_type"] != "code":
            cell.pop("outputs", None)
            cell.pop("execution_count", None)
            continue
        outs = []
        for out in _merge_streams(copy.deepcopy(cell.get("outputs", []))):
            out.pop("transient", None)
            if out.get("output_type") == "stream":
                out["text"] = _lines(out["text"])
            for key in ("data",):
                if key in out:
                    for mime in list(out[key]):
                        if mime in TEXT_MIME_SPLIT:
                            out[key][mime] = _lines(out[key][mime])
            outs.append(out)
        cell["outputs"] = outs
    text = json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    return text.replace("\r\n", "\n")


# --------------------------------------------------------------------------------------------
# execution
# --------------------------------------------------------------------------------------------
def fresh_out_dir(name: str, out: str | None) -> Path:
    if out:
        path = Path(out).resolve()
        if path.exists() and any(path.iterdir()):
            raise SystemExit(f"output folder {path} is not empty (this tool never deletes; choose a new one)")
        path.mkdir(parents=True, exist_ok=True)
        return path
    DEFAULT_OUT_PARENT.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=f"{name}-", dir=DEFAULT_OUT_PARENT)).resolve()


def execute(name: str, out_dir: Path, timeout: int) -> tuple[str, float]:
    import nbformat
    from nbclient import NotebookClient

    module = load_builder(name)
    nb = unexecuted_notebook(name)
    # pyzmq warns on Windows that the default (Proactor) event loop lacks add_reader and that it
    # starts a selector thread instead; harmless, and it would only clutter the console.
    warnings.filterwarnings("ignore", message="Proactor event loop does not implement add_reader",
                            category=RuntimeWarning)
    os.environ["REVISION_NB_OUT"] = str(out_dir)
    # The committed notebook is always the normal run (section 2.6 of the notebooks).
    os.environ.pop("REVISION_NB_LONG", None)
    os.environ["PYTHONHASHSEED"] = "0"
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    t0 = time.perf_counter()
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        allow_errors=False,
        record_timing=False,
        resources={"metadata": {"path": str(NB_DIR)}},
    )
    client.execute()
    seconds = time.perf_counter() - t0
    text = normalise(nb, name, module.TITLE)
    nbformat.validate(nbformat.reads(text, as_version=4))
    return text, seconds


def write_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# --------------------------------------------------------------------------------------------
# audit (static structure rules; no execution)
# --------------------------------------------------------------------------------------------
def audit_text(text: str, name: str) -> list[str]:
    problems: list[str] = []
    if "\r" in text:
        problems.append("A0: the file contains CR characters (LF only)")
    try:
        nb = json.loads(text)
    except ValueError as exc:
        return [f"A0: not JSON: {exc}"]
    title = nb.get("metadata", {}).get("revision", {}).get("title", "")
    if normalise(nb, name, title) != text:
        problems.append("A1: the file is not in normalised form (ids, metadata, sorted keys, LF)")
    cells = nb.get("cells", [])
    md_text = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
    all_src = "\n".join("".join(c["source"]) for c in cells)
    for h in REQUIRED_HEADINGS:
        if not re.search(r"^" + re.escape(h) + r"\b", md_text, re.MULTILINE):
            problems.append(f"A2: missing heading {h!r}")
    if not FINAL_HEADING_PATTERN.search(md_text):
        problems.append("A2: missing the final heading '## N. What this notebook showed ...'")
    for needle in RUN_NEEDLES:
        if needle not in md_text:
            problems.append(f"A3: the run instructions lack {needle!r}")
    for m in FORBIDDEN_RUN_TEXT.finditer(all_src):
        problems.append(f"A3: forbidden instruction {m.group(0)!r} (fails where jupyter is not on PATH)")
    for m in re.findall(r"\b[\w\-]+\.ipynb\b", md_text):
        if m != f"{name}.ipynb":
            problems.append(f"A4: the markdown names another notebook file {m}")
    prev = None
    n_code = 0
    for i, c in enumerate(cells):
        if c["cell_type"] == "code":
            n_code += 1
            if prev is None or prev["cell_type"] != "markdown" or len("".join(prev["source"]).strip()) < 80:
                problems.append(f"A5: code cell {i} lacks a markdown lead-in of at least 80 characters")
            if c.get("execution_count") is None:
                problems.append(f"A6: code cell {i} was not executed")
            for out in c.get("outputs", []):
                if out.get("output_type") == "error":
                    problems.append(f"A6: code cell {i} has an error output")
                if out.get("output_type") == "stream" and out.get("name") == "stderr":
                    problems.append(f"A6: code cell {i} wrote to stderr")
        prev = c
    if n_code == 0:
        problems.append("A6: the notebook has no code cell")
    home = str(Path.home())
    for needle in {str(REPO), str(REPO).replace("\\", "/"), str(REPO).replace("\\", "\\\\"), home, home.replace("\\", "/")}:
        if needle and needle in text:
            problems.append(f"A7: the notebook contains a machine-specific path ({needle})")
    return problems


def audit(name: str) -> list[str]:
    path = NB_DIR / f"{name}.ipynb"
    if not path.is_file():
        return [f"A0: {path.relative_to(REPO).as_posix()} does not exist (run: build {name})"]
    return audit_text(path.read_bytes().decode("utf-8"), name)


# --------------------------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------------------------
def first_difference(a: str, b: str) -> str:
    la, lb = a.splitlines(), b.splitlines()
    for i, (x, y) in enumerate(zip(la, lb), start=1):
        if x != y:
            return f"line {i}:\n  committed: {x[:200]}\n  new:       {y[:200]}"
    return f"the files differ in length ({len(la)} and {len(lb)} lines)"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build, check and audit the Revision notebooks.")
    ap.add_argument("command", choices=["list", "build", "check", "audit"])
    ap.add_argument("name", nargs="?")
    ap.add_argument("--out", help="output folder for the run (must not exist or be empty)")
    ap.add_argument("--timeout", type=int, default=1800, help="per-cell timeout in seconds (default 1800)")
    args = ap.parse_args(argv)

    if args.command == "list":
        for n in builder_names():
            state = "built" if (NB_DIR / f"{n}.ipynb").is_file() else "not built"
            print(f"{n}  ({state})")
        return 0
    if not args.name:
        ap.error("a notebook name is required")
    name = args.name
    target = NB_DIR / f"{name}.ipynb"

    if args.command == "audit":
        problems = audit(name)
        for p in problems:
            print("FAIL", p)
        print(f"audit {name}: {'PASS' if not problems else 'FAIL'} ({len(problems)} problems)")
        return 0 if not problems else 1

    out_dir = fresh_out_dir(name, args.out)
    print(f"{args.command} {name}: executing with outputs in {out_dir}")
    text, seconds = execute(name, out_dir, args.timeout)
    print(f"{args.command} {name}: executed in {seconds:.1f} s")
    if args.command == "build":
        write_lf(target, text)
        problems = audit(name)
        for p in problems:
            print("FAIL", p)
        print(f"build {name}: wrote {target.relative_to(REPO).as_posix()} ({len(text.encode('utf-8'))} bytes); "
              f"audit {'PASS' if not problems else 'FAIL'}")
        return 0 if not problems else 1
    # check
    candidate = out_dir / f"{name}.ipynb"
    write_lf(candidate, text)
    if not target.is_file():
        print(f"check {name}: FAIL - {target.relative_to(REPO).as_posix()} does not exist")
        return 1
    committed = target.read_bytes().decode("utf-8")
    if committed == text:
        print(f"check {name}: PASS - the re-executed notebook is byte-identical to "
              f"{target.relative_to(REPO).as_posix()} ({len(text.encode('utf-8'))} bytes)")
        return 0
    print(f"check {name}: FAIL - the re-executed notebook differs; first difference at {first_difference(committed, text)}")
    print(f"check {name}: the re-executed notebook is {candidate}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
