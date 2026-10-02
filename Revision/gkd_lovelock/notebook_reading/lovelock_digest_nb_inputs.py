#!/usr/bin/env python3
"""Write the digest Revision/gkd_lovelock/results/notebook-input-cells.txt (deterministic, UTF-8, LF) from the full
input-cell text written by lovelock_extract_nb_inputs.wls: for every input cell, in file order, its label (as stored
in the notebook), the size of its InputForm text in characters and its first 160 characters.

Usage (from the repository root):
    wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
    python Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py [INPUT] [--out PATH]
INPUT defaults to $LOVELOCK_NB_INPUTS, else build/lovelock_nb_inputs.txt.
"""

import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE.parent / "results" / "notebook-input-cells.txt"
HEADER = (
    "Input cells of 'Generalized _Kronecker_Delta_4+4.nb' as read by "
    "Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls\n"
    "(label stored in the file, size of the InputForm text in characters, first 160 characters).\n"
    "Only INPUT cells were extracted; no output cell was read. The cell labelled In[101] in the file is the\n"
    "image of Lovelock's equation (4.38) (the author's In[68]); it was rendered by "
    "Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls\n"
    "to Revision/gkd_lovelock/results/notebook-in68-image.png. The cell labelled In[87] in the file is the author's\n"
    "In[54], the definition of k\u03b4.\n"
    "\n"
)


def cells(text):
    """Blocks '=== <label>\n<text>\n\n' in file order."""
    heads = list(re.finditer(r"^=== (.*)$", text, flags=re.M))
    out = []
    for i, h in enumerate(heads):
        start = h.end() + 1
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[start:end]
        if body.endswith("\n\n"):
            body = body[:-2]
        out.append((h.group(1), body))
    return out


def main():
    args = [a for a in sys.argv[1:]]
    out = OUT
    if "--out" in args:
        i = args.index("--out")
        out = Path(args[i + 1])
        del args[i:i + 2]
    src = Path(args[0]) if args else Path(os.environ.get("LOVELOCK_NB_INPUTS") or ROOT / "build" / "lovelock_nb_inputs.txt")
    text = src.read_text(encoding="utf-8")
    rows = [f"{label:<12}{len(body):>12}  {body[:160]!r}" for label, body in cells(text)]
    out.write_bytes((HEADER + "\n".join(rows) + "\n").encode("utf-8"))
    print(f"{len(rows)} input cells -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
