"""Wrap over-long lines of a notebook builder (cell lines at most 89 characters after the
4-space dedent, so source lines at most 93). Markdown lines are split at a space; a code
line that is one string literal "..." is split into two literals."""
import re
import sys
from pathlib import Path

LIMIT = 93
path = Path(sys.argv[1])
lines = path.read_text(encoding="utf-8").split("\n")
out = []
for line in lines:
    while len(line) > LIMIT:
        indent = len(line) - len(line.lstrip(" "))
        literal = re.fullmatch(r'(\s*)"(.*)"(\)?)', line)
        cut = line.rfind(" ", indent + 1, LIMIT - 1)
        if literal:
            body = literal.group(2)
            limit = LIMIT - indent - 2
            cut = body.rfind(" ", 0, limit)
            first, rest = body[:cut + 1], body[cut + 1:]
            out.append(" " * indent + '"' + first + '"')
            line = " " * indent + '"' + rest + '"' + literal.group(3)
            continue
        if cut <= indent:
            break
        out.append(line[:cut])
        line = " " * indent + line[cut + 1:]
    out.append(line)
path.write_bytes("\n".join(out).encode("utf-8"))
print("long lines left:", [i + 1 for i, l in enumerate(out) if len(l) > LIMIT])
