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
# a heading may contain a code span with a "*" in it (e.g. `xorshift64*`): skip over code spans
heads = [(m.start(), int(m.group(1)), m.group(0))
         for m in re.finditer(r"\*\*In \[(\d+)\](?:`[^`]*`|[^*`])*\*\*", section)]
nb = json.load(open(nb_path, encoding="utf-8"))
cells = [(c.get("execution_count"), "".join(c["source"])) for c in nb["cells"] if c["cell_type"] == "code"]


# a docstring together with ONE blank line after it (a quote that omits the docstring omits that blank line too)
DOCSTRING = re.compile(r'^[ \t]*(?:"""|\'\'\').*?(?:"""|\'\'\')[ \t]*\n(?:[ \t]*\n)?', re.S | re.M)


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
# A cell may be explained by reference: "**In [k], ...** ... word for word In [j] of Notebook NNx". Accept it only when that
# cell of that notebook (in the same folder) has exactly the same code, so a cell that drifted from its model is reported.
for m in re.finditer(r"\*\*In \[(\d+)\][^\n]*?[Ww]ord for word,? In \[(\d+)\] of Notebook (\d\d[a-z])", section):
    k, j, other = int(m.group(1)), int(m.group(2)), m.group(3)
    import glob
    import os
    found = glob.glob(os.path.join(os.path.dirname(nb_path) or ".", f"{other}_*.ipynb"))
    if not found:
        continue
    ocells = {c.get("execution_count"): "".join(c["source"]) for c in json.load(open(found[0], encoding="utf-8"))["cells"]
              if c["cell_type"] == "code"}
    for i, (count, src) in enumerate(cells):
        if count == k and j in ocells and norm(ocells[j]) == norm(src):
            used.add(i)
for i, (count, src) in enumerate(cells):
    if i not in used and src.strip():
        first = [l for l in src.splitlines() if l.strip() and not l.lstrip().startswith("#")][:1]
        print(f"UNQUOTED  cell In [{count}]: {first[0][:100] if first else '(comments only)'!r}")
