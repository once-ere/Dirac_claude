"""Run the walk-through comparison for every notebook of the book; print a per-notebook summary."""
import glob
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
chapters = {os.path.basename(p)[:2]: p for p in glob.glob("Revision/textbook/chapters/[0-2][0-9]-*.md")}
rows = []
for nb in sorted(glob.glob("Revision/textbook/notebooks/*.ipynb")):
    nid = os.path.basename(nb)[:3]
    ch = chapters.get(nid[:2])
    if not ch:
        continue
    out = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "walkthrough_diff.py"), ch, nb, nid],
                         capture_output=True, text=True, encoding="utf-8").stdout
    nomatch = out.count("NO MATCH")
    heading = out.count("HEADING")
    unq = len([l for l in out.splitlines() if l.startswith("UNQUOTED") and "cell In [1]" not in l])
    missing = "no walk-through section" in out
    rows.append((nid, nomatch, heading, unq, missing))
bad = [r for r in rows if r[1] or r[2] or r[3] or r[4]]
print(f"notebooks: {len(rows)}; with drift: {len(bad)}")
for nid, a, b, c, m in bad:
    print(f"  {nid}: no-match {a}, wrong heading {b}, unquoted cells {c}{', NO WALK-THROUGH SECTION' if m else ''}")
