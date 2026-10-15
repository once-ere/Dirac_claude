"""Flag lines of textbook files that may still use the old numbering 1..8 of the directions or the old order.
Usage: risk_scan.py FILE... [--context N]"""
import re
import sys
from pathlib import Path

FILES = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]
RISK = {
    "tensor index 8": r"(?:\^|_)\{?8\}?\{\}|(?:\^|_)\{[0-7]*8[0-7]*\}|\{\}_\{?[0-8]*8|\^8\b|_8\b(?![0-9])",
    "sum 1..8": r"\\sum_\{[a-z\\]+ ?= ?1\}\^\{?8\}?|= ?1, ?\\dots, ?8|from 1 to 8|1 to 8\b|1, 2, \\dots, 8|\(1, 2, \\dots, 8\)",
    "index 1..8 words": r"\b(?:indices|index|entries|entry|values|directions) 1 to 8\b|\bnumbered 1\b",
    "position 7/last": r"\bindex 7\b|\bentry 7\b|\bposition 7\b|(?<!In )(?<!Out )\[7\]|\blast (?:direction|coordinate|entry|one)\b|\beighth (?:direction|coordinate|entry|component)|listed last|comes last|at the end of the list",
    "x1 first": r"\bfirst (?:direction|coordinate|entry)\b.{0,40}x_?1\b|\bx_?\{?1\}?\b.{0,30}\bfirst\b",
    "old 7-list": r"x_?\{?1\}?, ?x_?\{?2\}?, ?\\dots, ?x_?\{?7\}?\b|x_?1\.\.x_?7\b",
    "pair with 0 last": r"\(x_?\{?[1-7]\}?, ?x_?\{?0\}?\)",
    "cot last": r"-e\^\{-2 ?a_4\}[^$]{0,40}\\cot\^2|\[sp\.cot\(z\) \*\* 2\]\)?\s*$|\+ \[sp\.cot",
    "eta old": r"\+1, \+1, \+1, -1|1, 1, 1, -1, -1, -1, -1, 1",
}
for f in FILES:
    lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
    hits = []
    for i, line in enumerate(lines, 1):
        for k, p in RISK.items():
            m = re.search(p, line)
            if m:
                a = max(0, m.start() - 90)
                hits.append((i, k, line[a:m.end() + 90].replace("\n", " ")))
                break
    print(f"== {f.name}: {len(hits)} flagged lines")
    for i, k, t in hits:
        print(f"  {i} [{k}] {t}")
