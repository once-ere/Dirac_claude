"""Re-map the quoted code blocks of a walk-through to the rebuilt notebook.

Usage: wt_remap.py CHAPTER NB_ID [--dry]
For each ```python block of the walk-through of notebook NB_ID: find it in the HEAD notebook's
cell, map its line range to the working-tree notebook's cell with difflib (equal runs exactly,
changed runs by a fuzzy line alignment), and replace the block of the working-tree chapter by the
mapped lines of the new cell. A block that quoted a docstring in HEAD quotes it again; a block
that omitted it omits it again. Overlaps of consecutive blocks are split at the first aligned
line of the later block; a block that ended at the end of its HEAD cell ends at the end of the
new cell. New lines quoted by no block and gaps between blocks that were adjacent are reported.
"""
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder
chapter_rel, nid = sys.argv[1], sys.argv[2]
DRY = "--dry" in sys.argv
nb_rel = next((REPO / "Revision/textbook/notebooks").glob(f"{nid}_*.ipynb")).relative_to(REPO).as_posix()


def git_show(rel):
    return subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


DOCSTRING = re.compile(r'^[ \t]*(?:"""|\'\'\').*?(?:"""|\'\'\')[ \t]*\n(?:[ \t]*\n)?', re.S | re.M)


class Cell:
    """Raw lines (right-stripped), a flag per line (inside a docstring or the blank line after
    it), and the list of indices of the other lines (the normalised view)."""

    def __init__(self, src):
        text = src.strip("\n") + "\n"
        self.raw = [line.rstrip() for line in text.rstrip("\n").split("\n")]
        starts, pos = [], 0
        for line in text.rstrip("\n").split("\n"):
            starts.append(pos)
            pos += len(line) + 1
        doc = set()
        for m in DOCSTRING.finditer(text):
            for i, st in enumerate(starts):
                if m.start() <= st < m.end():
                    doc.add(i)
        self.doc = doc
        self.keep = [i for i in range(len(self.raw)) if i not in doc]
        self.norm = [self.raw[i] for i in self.keep]


def cells_of(nb_text):
    nb = json.loads(nb_text)
    return {c.get("execution_count"): Cell("".join(c["source"]))
            for c in nb["cells"] if c["cell_type"] == "code"}


def section_span(text):
    start = text.find(f"Line-by-line walk-through of Notebook {nid}")
    start = text.rfind("\n### ", 0, start) + 1
    end = text.find("\n### ", start + 5)
    return start, (end + 1 if end > 0 else len(text))


def blocks_of(text):
    s0, s1 = section_span(text)
    sec = text[s0:s1]
    heads = [(m.start(), int(m.group(1))) for m in
             re.finditer(r"\*\*In \[(\d+)\](?:`[^`]*`|[^*`])*\*\*", sec)]
    out = []
    for m in re.finditer(r"```python\n(.*?)```", sec, re.S):
        head = max((h for h in heads if h[0] < m.start()), default=None)
        out.append((s0 + m.start(1), s0 + m.end(1), head[1] if head else None, m.group(1)))
    return out


ELL = ("...", "...)", "...),", "... )")


def segments(block_text):
    """('code', [lines]) and ('ell', line) segments of a block (lines right-stripped)."""
    segs, cur = [], []
    for line in [l.rstrip() for l in block_text.strip("\n").split("\n")]:
        if line.strip() in ELL:
            if cur:
                segs.append(("code", cur))
            segs.append(("ell", line))
            cur = []
        else:
            cur.append(line)
    if cur:
        segs.append(("code", cur))
    return segs


def find(sub, lines, start=0):
    for i in range(start, len(lines) - len(sub) + 1):
        if lines[i:i + len(sub)] == sub:
            return i
    return -1


def fuzzy(old, new):
    """Monotone alignment of two short line lists maximising the summed similarity."""
    n1, n2 = len(old), len(new)
    sim = [[difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() for b in new] for a in old]
    best = [[0.0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            take = sim[i][j] + best[i + 1][j + 1] if sim[i][j] > 0.45 else -1
            best[i][j] = max(take, best[i + 1][j], best[i][j + 1])
    pairs, i, j = [], 0, 0
    while i < n1 and j < n2:
        if sim[i][j] > 0.45 and best[i][j] == sim[i][j] + best[i + 1][j + 1]:
            pairs.append((i, j))
            i, j = i + 1, j + 1
        elif best[i][j] == best[i + 1][j]:
            i += 1
        else:
            j += 1
    return pairs


old_text, new_text = git_show(chapter_rel), (REPO / chapter_rel).read_text(encoding="utf-8")
old_cells, new_cells = cells_of(git_show(nb_rel)), cells_of((REPO / nb_rel).read_text(encoding="utf-8"))
old_blocks, new_blocks = blocks_of(old_text), blocks_of(new_text)
assert len(old_blocks) == len(new_blocks), (len(old_blocks), len(new_blocks))
assert [b[2] for b in old_blocks] == [b[2] for b in new_blocks]

opcache, partners = {}, {}


def opcodes(n):
    """Opcodes and partners on the RAW lines of cell n."""
    if n not in opcache:
        o, w = old_cells[n].raw, new_cells[n].raw
        opcache[n] = difflib.SequenceMatcher(None, o, w, autojunk=False).get_opcodes()
        part = {}
        for tag, i1, i2, j1, j2 in opcache[n]:
            if tag == "equal":
                part.update({i1 + d: j1 + d for d in range(i2 - i1)})
            elif tag == "replace":
                part.update({i1 + a: j1 + b for a, b in fuzzy(o[i1:i2], w[j1:j2])})
        partners[n] = part
    return opcache[n]


def map_range(n, s, e):
    """Old raw range [s, e) -> new raw range: whole changed regions at the ends."""
    ns = ne = None
    for tag, i1, i2, j1, j2 in opcodes(n):
        if ns is None and i1 <= s < i2:
            ns = j1 + (s - i1) if tag == "equal" else j1
        if i1 <= e - 1 < i2:
            ne = j1 + (e - 1 - i1) + 1 if tag == "equal" else j2
    if e == len(old_cells[n].raw):  # the block ended the HEAD cell: end the new cell too
        ne = len(new_cells[n].raw)
    if ns is not None and ne is not None and ne <= ns:
        ne = ns + 1
    return ns, ne


def first_partner(n, s, e):
    hit = [partners[n][i] for i in range(s, e) if i in partners[n]]
    return min(hit) if hit else None


report, plan, ranges = [], [], {}
for k, ob in enumerate(old_blocks):
    n = ob[2]
    if n not in old_cells or n not in new_cells:
        report.append(f"block {k}: In [{n}] has no cell")
        plan.append(None)
        continue
    oc = old_cells[n]
    items, pos = [], 0
    for kind, seg in segments(ob[3]):
        if kind == "ell":
            items.append(("ell", seg))
            continue
        with_doc = any('"""' in l or "'''" in l for l in seg)
        if with_doc:  # the block quotes a docstring: match the raw lines
            i = find(seg, oc.raw, pos)
            if i < 0:
                i = find(seg, oc.raw, 0)
            s, e = i, i + len(seg)
        else:  # match the normalised lines, then convert to raw indices
            seg_n = [l for l in seg if l.strip() or True]
            i = find(seg_n, oc.norm, 0)
            if i >= 0:
                s, e = oc.keep[i], oc.keep[i + len(seg_n) - 1] + 1
        if i < 0:
            report.append(f"block {k} In [{n}]: segment not found in HEAD cell: {seg[0][:80]}")
            items = None
            break
        pos = e
        ns, ne = map_range(n, s, e)
        if ns is None or ne is None:
            report.append(f"block {k} In [{n}]: no mapping for old {s}..{e - 1}")
            items = None
            break
        r = [ns, ne]
        items.append(("seg", n, r, s, e, with_doc))
        ranges.setdefault(n, []).append((r, k, s, e))
    plan.append(items)

for n, rs in ranges.items():
    rs.sort(key=lambda t: t[2])
    for (ra, ka, ia, ea), (rb, kb, ib, eb) in zip(rs, rs[1:]):
        if rb[0] < ra[1]:
            cut = first_partner(n, ib, eb)
            if cut is None or cut <= ra[0]:
                report.append(f"In [{n}]: OVERLAP of blocks {ka} and {kb} not resolved")
                continue
            ra[1], rb[0] = cut, cut
            rb[1] = max(rb[1], rb[0])
        elif rb[0] > ra[1] and ea == ib:
            report.append(f"In [{n}]: GAP between adjacent blocks {ka} and {kb}: "
                          + " | ".join(new_cells[n].raw[ra[1]:rb[0]])[:300])

replacements, changed, covered = [], [], {}
for k, items in enumerate(plan):
    if items is None:
        continue
    ob, nb_ = old_blocks[k], new_blocks[k]
    out = []
    for item in items:
        if item[0] == "ell":
            out.append(item[1])
            continue
        _, n, r, s, e, with_doc = item
        nc = new_cells[n]
        idx = [j for j in range(r[0], r[1]) if with_doc or j not in nc.doc]
        while idx and not nc.raw[idx[0]].strip():
            idx.pop(0)
        while idx and not nc.raw[idx[-1]].strip():
            idx.pop()
        out += [nc.raw[j] for j in idx]
        covered.setdefault(n, set()).update(range(r[0], r[1]))
    new_block = "\n".join(out) + "\n"
    if new_block.strip("\n") != ob[3].strip("\n"):
        changed.append(k)
    if new_block != nb_[3]:
        replacements.append((nb_[0], nb_[1], new_block))

for n, c in new_cells.items():
    if n not in covered:
        continue
    new_only = set()
    for tag, i1, i2, j1, j2 in opcodes(n):
        if tag in ("insert", "replace"):
            new_only.update(range(j1, j2))
    flagged = [i for i, l in enumerate(c.raw) if l.strip() and i not in covered[n]
               and i in new_only and i not in c.doc]
    if flagged:
        report.append(f"In [{n}]: new lines quoted by no block: "
                      + " | ".join(c.raw[i] for i in flagged)[:300])

text = new_text
for s, e, nbk in sorted(replacements, reverse=True):
    text = text[:s] + nbk + text[e:]
print(f"{nid}: blocks {len(new_blocks)}, replaced {len(replacements)}, code changed {len(changed)}")
print("changed blocks (index:In):", " ".join(f"{k}:{old_blocks[k][2]}" for k in changed))
for r in report:
    print("REPORT", r)
if not DRY:
    (REPO / chapter_rel).write_bytes(text.encode("utf-8"))
