#!/usr/bin/env python3
"""Execute every code cell of a Jupyter notebook in order and embed the real outputs.

Origin and licence
------------------
Adapted from planet_Mercury/notebook/run_notebook.py of the rustSolveIt
engine (https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 at
commit a8fdff459adfe181573d7924b18bffbdf378fdb3; author: once-ere;
BSD-3-Clause, as declared in the rustSolveIt Cargo manifests).  See NOTICE,
section 2d.

Kept from the original: cells are exec()'d in one shared namespace with
stdout/stderr captured; cells tagged "interactive" are skipped (outputs
blanked); the file is written back ONLY if every executed cell succeeded;
standard library only; exit code 0 only if every notebook ran.

Changed: (1) figures - the namespace receives a hook __nb_display_png__(path)
that the notebook's save_figure() calls; the PNG is embedded as an
image/png display_data output at that point of the cell's output, so text
and figures interleave as in Jupyter; (2) progress - captured text is also
echoed to the terminal while a cell runs, because some cells run the
simulator for minutes; (3) the cell's working directory is the directory
the runner was started from (the notebook locates the repository itself);
(4) stream outputs are split into one stdout output per contiguous block.

Usage:  python notebooks/run_notebook.py notebooks/dirac16complex_dark_sector.ipynb
"""

import base64
import io
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


class _Tee(io.TextIOBase):
    """Capture into a buffer and echo to the real terminal."""

    def __init__(self, buffer, echo):
        self.buffer, self.echo = buffer, echo

    def write(self, text):
        self.buffer.write(text)
        if self.echo is not None:
            try:
                self.echo.write(text)
                self.echo.flush()
            except (OSError, ValueError, UnicodeEncodeError):
                pass
        return len(text)

    def flush(self):
        pass


def _stream(text):
    return {"output_type": "stream", "name": "stdout", "text": text.splitlines(keepends=True)}


def run(path: Path, echo: bool = True) -> bool:
    nb = json.loads(path.read_text(encoding="utf-8"))
    ns: dict = {"__name__": "__main__"}
    count = 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        tags = cell.get("metadata", {}).get("tags", [])
        src = "".join(cell.get("source", []))
        if "interactive" in tags:
            cell["outputs"] = []
            cell["execution_count"] = None
            continue
        count += 1
        buf = io.StringIO()
        outputs = []

        def flush_text():
            text = buf.getvalue()
            if text:
                outputs.append(_stream(text))
            buf.seek(0)
            buf.truncate()

        def display_png(png_path):
            flush_text()
            data = base64.b64encode(Path(png_path).read_bytes()).decode("ascii")
            outputs.append({
                "output_type": "display_data",
                "data": {"image/png": data, "text/plain": [f"<Figure {Path(png_path).name}>"]},
                "metadata": {},
            })

        ns["__nb_display_png__"] = display_png
        tee = _Tee(buf, sys.__stdout__ if echo else None)
        try:
            with redirect_stdout(tee), redirect_stderr(tee):
                exec(compile(src, f"<cell {count}>", "exec"), ns)
        except BaseException as exc:  # noqa: BLE001 - report and fail loudly
            if not echo and buf.getvalue():
                print("--- captured output of the failing cell ---")
                print(buf.getvalue())
            print(f"\nFAIL {path} (cell {count}): {exc!r}")
            return False
        flush_text()
        cell["execution_count"] = count
        cell["outputs"] = outputs
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"ok {path} ({count} cells)")
    return True


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--quiet"]
    paths = [Path(p) for p in args]
    if not paths:
        print("usage: run_notebook.py [--quiet] <notebook.ipynb> [...]")
        return 2
    ok = sum(1 for p in paths if run(p, echo="--quiet" not in sys.argv[1:]))
    print(f"{ok} ok, {len(paths) - ok} failed")
    return 0 if ok == len(paths) else 1


if __name__ == "__main__":
    sys.exit(main())
