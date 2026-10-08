"""Regenerate chapter 23 ("Reproducing everything") of the textbook: its text and numbers from the template and the stored
Notebook 23a, then its glossary from the definitions of every chapter.

Usage (repository root):
    python Revision/textbook/tools/chapter23/run_all.py           rewrite Revision/textbook/chapters/23-reproducing-everything.md
    python Revision/textbook/tools/chapter23/run_all.py --check   regenerate, compare byte for byte with the stored chapter,
                                                                  restore the stored chapter; exit 0 only when identical
Steps: generate_chapter.py (ch23.template.md + fills.json + the stored 23a notebook and its data files), extract.py (terms and
their definitions from the chapters and the notebooks' "words used" sections), group.py (exclude.txt), build.py (manual.json),
splice.py (the glossary section).  Intermediate files go to build/chapter23/ (git-ignored).  Run it after every rebuild of
Notebook 23a and after any chapter changes a definition; Notebook 23a itself must be rebuilt LAST, after every other notebook.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHAPTER = ROOT / "Revision/textbook/chapters/23-reproducing-everything.md"
STEPS = ["generate_chapter.py", "extract.py", "group.py", "build.py", "splice.py"]

check = "--check" in sys.argv[1:]
stored = CHAPTER.read_bytes()
try:
    for step in STEPS:
        result = subprocess.run([sys.executable, "-B", str(HERE / step)], cwd=ROOT, capture_output=True, text=True,
                                encoding="utf-8", errors="replace")
        if result.returncode != 0:
            sys.exit(f"step {step} failed (exit {result.returncode}):\n{result.stdout[-2000:]}\n{result.stderr[-2000:]}")
        print(f"step {step}: OK")
    new = CHAPTER.read_bytes()
finally:
    if check:
        CHAPTER.write_bytes(stored)
if check:
    if new == stored:
        print("chapter23=UP-TO-DATE (regenerated chapter is byte-identical to the stored one)")
    else:
        sys.exit("chapter23=DIFFERS: run without --check to rewrite it, then review the diff")
else:
    print(f"chapter23=WRITTEN ({'unchanged' if new == stored else 'changed'})")
