"""Report the quoted blocks of a walk-through whose lines are not one contiguous run of lines
of their notebook cell (after wt_remap.py a fuzzy alignment can drop or misplace a line).

Usage: wt_contiguous.py CHAPTER NB_ID
Blocks with an ellipsis ("...") are checked piece by piece."""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder
chapter_rel, nid = sys.argv[1], sys.argv[2]
nb_path = next((REPO / "Revision/textbook/notebooks").glob(f"{nid}_*.ipynb"))
nb = json.loads(nb_path.read_text(encoding="utf-8"))
cells = {c.get("execution_count"): [l.rstrip() for l in "".join(c["source"]).split("\n")]
         for c in nb["cells"] if c["cell_type"] == "code"}
text = (REPO / chapter_rel).read_text(encoding="utf-8")
start = text.find(f"Line-by-line walk-through of Notebook {nid}")
start = text.rfind("\n### ", 0, start) + 1
end = text.find("\n### ", start + 5)
sec = text[start:end if end > 0 else len(text)]
first_line = text[:start].count("\n") + 1
heads = [(m.start(), int(m.group(1))) for m in
         re.finditer(r"\*\*In \[(\d+)\](?:`[^`]*`|[^*`])*\*\*", sec)]
bad = 0
for m in re.finditer(r"```python\n(.*?)```", sec, re.S):
    head = max((h for h in heads if h[0] < m.start()), default=None)
    n = head[1] if head else None
    raw = cells.get(n, [])
    lines = [l.rstrip() for l in m.group(1).strip("\n").split("\n")]
    pieces, cur = [], []
    for l in lines:
        if l.strip().startswith("..."):
            if cur:
                pieces.append(cur)
            cur = []
        else:
            cur.append(l)
    if cur:
        pieces.append(cur)
    for piece in pieces:
        ok = any(raw[i:i + len(piece)] == piece for i in range(len(raw) - len(piece) + 1))
        if not ok:
            bad += 1
            line_no = first_line + sec[:m.start()].count("\n")
            missing = [l for l in piece if l not in raw]
            print(f"chapter line {line_no}, In [{n}]: block piece of {len(piece)} lines is not "
                  f"contiguous in the cell; lines not in the cell: {missing[:3]}")
print(f"{nid}: {bad} non-contiguous block piece(s)")
