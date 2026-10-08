"""Compare a chapter's walk-through of one notebook with the notebook's actual code cells.

Usage: python walkthrough_diff.py <chapter.md> <notebook.ipynb> <notebook id, e.g. 13a>
For every ```python block in the walk-through section of the notebook, find the notebook code cell
that contains it (after stripping the standard preamble); report blocks that match no cell, cells
that no block quotes, and the "In [k]" headings that disagree with the cell's execution count.
"""
import json
import re
import sys

chapter, nb_path, nid = sys.argv[1:4]
text = open(chapter, encoding="utf-8").read()
start = text.find(f"Line-by-line walk-through of Notebook {nid}")
if start < 0:
    sys.exit(f"no walk-through section for {nid}")
end = text.find("Line-by-line walk-through of Notebook", start + 10)
section = text[start:end if end > 0 else len(text)]
blocks = [(m.start(), m.group(1)) for m in re.finditer(r"```python\n(.*?)```", section, re.S)]
heads = [(m.start(), int(m.group(1)), m.group(0)) for m in re.finditer(r"\*\*In \[(\d+)\][^*]*\*\*", section)]
nb = json.load(open(nb_path, encoding="utf-8"))
cells = [(c.get("execution_count"), "".join(c["source"])) for c in nb["cells"] if c["cell_type"] == "code"]


DOCSTRING = re.compile(r'^[ \t]*(?:"""|\'\'\').*?(?:"""|\'\'\')[ \t]*\n', re.S | re.M)


def norm(s):
    # chapters quote functions without their docstrings (the prose explains them): drop docstrings on both sides
    s = DOCSTRING.sub("", s.strip("\n") + "\n")
    return "\n".join(line.rstrip() for line in s.strip("\n").split("\n"))


def pieces(block):
    """Split a quoted block at the chapters' abbreviation lines ('...' or '...)'); every piece must occur."""
    parts, cur = [], []
    for line in norm(block).split("\n"):
        if line.strip() in ("...", "...)", "...),", "... )"):
            if cur:
                parts.append("\n".join(cur))
            cur = []
        else:
            cur.append(line)
    if cur:
        parts.append("\n".join(cur))
    return [p for p in parts if p.strip()]


used = set()
print(f"walk-through blocks: {len(blocks)}; notebook code cells: {len(cells)}; In-headings: {len(heads)}")
for pos, b in blocks:
    nb_ = norm(b)
    parts = pieces(b)
    hits = [i for i, (_, src) in enumerate(cells) if parts and all(p in norm(src) for p in parts)]
    head = max((h for h in heads if h[0] < pos), default=None, key=lambda h: h[0])
    if not hits:
        if head and head[1] == 1:
            print(f"PREAMBLE  {nb_.splitlines()[0][:60]!r}")
            continue
        print(f"NO MATCH  (under heading {head[2] if head else '-'}): {nb_.splitlines()[0][:100]!r}")
        continue
    used.update(hits)
    count = cells[hits[0]][0]
    if head and head[1] != count:
        print(f"HEADING   {head[2]!r} but the quoted code is in cell In [{count}]: {nb_.splitlines()[0][:70]!r}")
for i, (count, src) in enumerate(cells):
    if i not in used and src.strip():
        first = [l for l in src.splitlines() if l.strip() and not l.lstrip().startswith("#")][:1]
        print(f"UNQUOTED  cell In [{count}]: {first[0][:100] if first else '(comments only)'!r}")
