"""List the prose lines (outside ```python and ```text blocks) of a chapter that quote code
with a literal integer index or range, e.g. `gamma[3]`, `T[3, 0]`, `range(4, 7)`,
`weights[:, 7]`: after a relabel these descriptions must follow the new positions.

Usage: prose_indices.py CHAPTER"""
import re
import sys
from pathlib import Path

PATTERN = re.compile(r"`[^`\n]*(\[[^\]`]*\d[^\]`]*\]|range\(\d[^`]*\)|\(\d(, \d)+\))[^`\n]*`")
lines = Path(sys.argv[1]).read_text(encoding="utf-8").split("\n")
inside = False
for number, line in enumerate(lines, 1):
    if line.startswith("```"):
        inside = not inside
        continue
    if inside:
        continue
    found = [m.group(0) for m in PATTERN.finditer(line)]
    if found:
        print(f"{number}: " + "  ".join(found)[:300])
