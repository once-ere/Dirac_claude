"""Fill the gaps of a walk-through after wt_remap.py: lines of a notebook cell that no quoted
block contains, directly after the last line of a block, are appended to that block.

Usage: wt_fill.py CHAPTER NB_ID [--dry]
Only gaps between the end of a block and the start of the next block of the same cell (or the
end of the cell) are filled; lines inside docstrings and blocks with an ellipsis ("...") are
left alone. Every filled gap is printed; read the prose next to it afterwards."""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder
chapter_rel, nid = sys.argv[1], sys.argv[2]
DRY = "--dry" in sys.argv
nb_path = next((REPO / "Revision/textbook/notebooks").glob(f"{nid}_*.ipynb"))
DOCSTRING = re.compile(r'^[ \t]*(?:"""|\'\'\').*?(?:"""|\'\'\')[ \t]*\n', re.S | re.M)


def cell_lines(src):
    text = src.strip("\n") + "\n"
    raw = [line.rstrip() for line in text.rstrip("\n").split("\n")]
    starts, pos = [], 0
    for line in raw:
        starts.append(pos)
        pos += len(line) + 1
    doc = {i for m in DOCSTRING.finditer(text) for i, st in enumerate(starts)
           if m.start() <= st < m.end()}
    return raw, doc


nb = json.loads(nb_path.read_text(encoding="utf-8"))
cells = {c.get("execution_count"): cell_lines("".join(c["source"]))
         for c in nb["cells"] if c["cell_type"] == "code"}
path = REPO / chapter_rel
text = path.read_text(encoding="utf-8")
start = text.find(f"Line-by-line walk-through of Notebook {nid}")
start = text.rfind("\n### ", 0, start) + 1
end = text.find("\n### ", start + 5)
end = end + 1 if end > 0 else len(text)
sec = text[start:end]
heads = [(m.start(), int(m.group(1))) for m in
         re.finditer(r"\*\*In \[(\d+)\](?:`[^`]*`|[^*`])*\*\*", sec)]
blocks = []
for m in re.finditer(r"```python\n(.*?)```", sec, re.S):
    head = max((h for h in heads if h[0] < m.start()), default=None)
    blocks.append([m.start(1), m.end(1), head[1] if head else None, m.group(1)])


def locate(lines, raw, after):
    """First index >= after where the block's lines appear in a row in the cell, or -1."""
    for i in range(after, len(raw) - len(lines) + 1):
        if raw[i:i + len(lines)] == lines:
            return i
    return -1


spans = []  # (block index, cell number, first, last) for the blocks found in their cell
cursor = {}
for k, (b0, b1, n, body) in enumerate(blocks):
    lines = [l.rstrip() for l in body.strip("\n").split("\n")]
    if n not in cells or any(l.strip().startswith("...") for l in lines):
        continue
    raw, doc = cells[n]
    first = locate(lines, raw, cursor.get(n, 0))
    if first < 0:
        continue
    spans.append((k, n, first, first + len(lines) - 1))
    cursor[n] = first + len(lines)
additions = {}
for idx, (k, n, first, last) in enumerate(spans):
    raw, doc = cells[n]
    nxt = next((s for s in spans[idx + 1:] if s[1] == n), None)
    stop = nxt[2] if nxt else len(raw)
    gap = list(range(last + 1, stop))
    while gap and raw[gap[-1]] == "":
        gap.pop()
    if gap and not any(i in doc for i in gap) and any(raw[i] for i in gap):
        additions[k] = [raw[i] for i in gap]
        print(f"In [{n}] block {k}: +{len(gap)} line(s): " + " | ".join(raw[i].strip() for i in gap)[:300])
if additions and not DRY:
    for k in sorted(additions, reverse=True):
        b0, b1, n, body = blocks[k]
        new_body = body.rstrip("\n") + "\n" + "\n".join(additions[k]) + "\n"
        sec = sec[:b0] + new_body + sec[b1:]
    path.write_bytes((text[:start] + sec + text[end:]).encode("utf-8"))
print(f"{nid}: {len(additions)} gap(s) filled" + (" (dry run)" if DRY else ""))
