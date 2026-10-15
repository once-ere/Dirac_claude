"""Wrap over-long lines of a notebook builder (cell lines at most 89 characters after the
4-space dedent, so source lines at most 93). Only the lines after "CELLS = [" are touched.
Markdown lines are split at a space; a code line that is exactly one string literal "..."
(optionally followed by a closing parenthesis) is split into two literals; any other long
line is reported and left alone."""
import re
import sys
from pathlib import Path

LIMIT = 93
path = Path(sys.argv[1])
lines = path.read_text(encoding="utf-8").split("\n")
start = next((i for i, l in enumerate(lines) if l.startswith("CELLS = [")), len(lines))
out, untouched = lines[:start], []
in_code = False
for line in lines[start:]:
    stripped = line.strip()
    if stripped.startswith(("code(r'''", "code('''")):
        in_code = True
    elif stripped.startswith(("md(r\"\"\"", "md(\"\"\"")):
        in_code = False
    while len(line) > LIMIT:
        indent = len(line) - len(line.lstrip(" "))
        literal = re.fullmatch(r'(\s*)"([^"\\]*(?:\\.[^"\\]*)*)"(\)?)', line)
        if literal:
            body = literal.group(2)
            cut = body.rfind(" ", 0, LIMIT - indent - 2)
            if cut <= 0:
                break
            out.append(" " * indent + '"' + body[:cut + 1] + '"')
            line = " " * indent + '"' + body[cut + 1:] + '"' + literal.group(3)
            continue
        if in_code or '"' in line or "'" in line and not line.lstrip().startswith(("-", "$")):
            untouched.append(line)
            break
        cut = line.rfind(" ", indent + 1, LIMIT - 1)
        if cut <= indent:
            untouched.append(line)
            break
        out.append(line[:cut])
        line = " " * indent + line[cut + 1:]
    out.append(line)
path.write_bytes("\n".join(out).encode("utf-8"))
print("long lines left:", [i + 1 for i, l in enumerate(out) if len(l) > LIMIT and i >= start])
for line in untouched:
    print("  NOT WRAPPED:", line.strip()[:120])
