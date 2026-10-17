#!/usr/bin/env python3
"""Revision/universe_model/tools/build_pdfs.py - build the PDFs of Revision/universe_model from their Markdown sources:
md2tex.py writes NAME.tex next to NAME.md, pdflatex runs twice (table of contents) in build/universe_model/, and the
PDF is copied next to the source.  The output is deterministic (md2tex writes no dates; the preamble suppresses the
PDF dates and trailer id), so a rebuild of an unchanged source reproduces the committed .tex and .pdf byte for byte.

Usage (from the repository root): python Revision/universe_model/tools/build_pdfs.py [NAME ...]
NAME is a document stem (MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION); default: every *.md of the folder except
README.  Every pdflatex call runs under a 120 s timeout.  Exit code 0 iff every PDF was built without an overfull box."""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
ROOT = DOCS.parent.parent
sys.path.insert(0, str(HERE))
import md2tex  # noqa: E402

BUILD = ROOT / "build" / "universe_model"


def build(name):
    src, tex = DOCS / (name + ".md"), DOCS / (name + ".tex")
    gdir = Path(os.path.relpath(src.resolve().parent, ROOT)).as_posix()
    tex.write_text(md2tex.convert(src.read_text(encoding="utf-8"), None, gdir), encoding="utf-8", newline="\n")
    BUILD.mkdir(parents=True, exist_ok=True)
    rel = Path(os.path.relpath(tex, ROOT)).as_posix()
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=" + str(BUILD), rel],
                           cwd=ROOT, capture_output=True, text=True, encoding="latin-1", timeout=120)
        if r.returncode != 0:
            log = (BUILD / (name + ".log")).read_text(encoding="latin-1")
            err = [l for l in log.splitlines() if l.startswith("!")]
            print("pdflatex FAILED for %s: %s" % (name, err[:3]))
            return False
    shutil.copyfile(BUILD / (name + ".pdf"), DOCS / (name + ".pdf"))
    log = (BUILD / (name + ".log")).read_text(encoding="latin-1")
    overfull = log.count("Overfull")
    m = re.search(r"Output written on [^(]*\((\d+) pages?", log.replace("\n", ""))
    print("%s.pdf: %s pages, overfull boxes: %d" % (name, m.group(1) if m else "?", overfull))
    return overfull == 0


def main(names):
    if not names:
        names = sorted(p.stem for p in DOCS.glob("*.md") if p.stem != "README")
    ok = all([build(n) for n in names])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
