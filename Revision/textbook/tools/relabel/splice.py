"""Replace the text between two marker strings (start inclusive, end exclusive) of a file by the content of a file.
Usage: splice.py TARGET START_MARKER END_MARKER NEW_TEXT_FILE"""
import sys
from pathlib import Path

target, start, end, new_file = sys.argv[1:5]
p = Path(target)
s = p.read_text(encoding="utf-8")
new = Path(new_file).read_text(encoding="utf-8")
i = s.find(start)
if i < 0 or s.find(start, i + 1) >= 0:
    sys.exit(f"start marker not unique/found: {start!r}")
j = s.find(end, i + len(start))
if j < 0:
    sys.exit(f"end marker not found: {end!r}")
s = s[:i] + new + s[j:]
p.write_bytes(s.encode("utf-8"))
print(f"spliced {len(new)} characters into {p.name} (replaced {j - i})")
