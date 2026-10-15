"""Print a chapter with its ```python blocks collapsed to one line, with line numbers.
Usage: prose.py CHAPTER [FROM] [TO]"""
import sys

path = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
lines = open(path, encoding="utf-8").read().split("\n")
i = 0
out = []
while i < len(lines):
    n = i + 1
    if lines[i].startswith("```python"):
        j = i + 1
        while j < len(lines) and not lines[j].startswith("```"):
            j += 1
        if lo <= n <= hi:
            first = lines[i + 1] if i + 1 < j else ""
            out.append(f"{n}: [code {j - i - 1} lines: {first[:70]}]")
        i = j + 1
        continue
    if lo <= n <= hi and lines[i].strip():
        out.append(f"{n}: {lines[i]}")
    i += 1
sys.stdout.reconfigure(encoding="utf-8")
print("\n".join(out))
