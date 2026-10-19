"""Static staleness report of the textbook chapters against the stored notebooks.

For every chapter and every notebook marker: the walk-through section after the marker is read; every fenced
python block in it is compared line by line with the code cells of the stored notebook (a quoted line counts as
found when it occurs, stripped, in some code cell; lines that are only '...' are skipped).  Also: the claimed
number of code cells ("The notebook has N code cells") against the notebook, and In [k] references beyond the
last code cell.  Prints one line per walk-through and a list of missing lines (first 8) per walk-through.
Usage: python stale_walk.py [chapter-prefix ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/claude/dirac_claude/Revision/textbook")


def notebook_code_lines(nb_id):
    nbs = sorted((ROOT / "notebooks").glob(f"{nb_id}_*.ipynb"))
    if not nbs:
        return None, 0
    nb = json.loads(nbs[0].read_text(encoding="utf-8"))
    lines = set()
    ncode = 0
    for c in nb["cells"]:
        if c["cell_type"] == "code":
            ncode += 1
            for ln in "".join(c["source"]).split("\n"):
                s = ln.strip()
                if s:
                    lines.add(s)
    return lines, ncode


def walkthroughs(text):
    """Yield (nb_id, walkthrough_text) for every marker."""
    parts = re.split(r"^<!-- NOTEBOOK (\d\d[a-z]) -->\s*$", text, flags=re.M)
    # parts: [before, id1, after1, id2, after2, ...]
    for i in range(1, len(parts), 2):
        nb_id = parts[i]
        after = parts[i + 1]
        # the walk-through runs until the next section that is not part of it: we take everything up to the next
        # marker (already split) but stop at a section heading that is not the walk-through's own heading
        m = re.search(r"^### \d+\.\d+ Line-by-line walk-through of Notebook " + nb_id + r".*$", after, flags=re.M)
        if not m:
            yield nb_id, None
            continue
        rest = after[m.end():]
        n = re.search(r"^### ", rest, flags=re.M)
        yield nb_id, rest[: n.start()] if n else rest


def main():
    prefixes = sys.argv[1:]
    for ch in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.md")):
        if prefixes and not any(ch.name.startswith(p) for p in prefixes):
            continue
        text = ch.read_text(encoding="utf-8")
        for nb_id, wt in walkthroughs(text):
            lines, ncode = notebook_code_lines(nb_id)
            if lines is None:
                print(f"{ch.name[:2]} {nb_id}: NO NOTEBOOK")
                continue
            if wt is None:
                print(f"{ch.name[:2]} {nb_id}: NO WALK-THROUGH HEADING after the marker")
                continue
            blocks = re.findall(r"^```python\n(.*?)^```", wt, flags=re.M | re.S)
            quoted = []
            for b in blocks:
                for ln in b.split("\n"):
                    s = ln.strip()
                    if s and not re.fullmatch(r"\.\.\.[)\],;]*(\s*#.*)?", s):
                        quoted.append(s)
            missing = [q for q in quoted if q not in lines]
            claim = re.search(r"The notebook has (\d+) code cells", wt)
            claimed = int(claim.group(1)) if claim else None
            ins = [int(k) for k in re.findall(r"In \[(\d+)\]", wt)]
            beyond = sorted({k for k in ins if k > ncode})
            flag = "OK" if not missing and (claimed in (None, ncode)) and not beyond else "STALE"
            print(f"{ch.name[:2]} {nb_id}: {flag} code_cells={ncode} claimed={claimed} quoted={len(quoted)} "
                  f"missing={len(missing)} In_beyond={beyond[:5]}")
            for q in missing[:8]:
                print(f"      missing: {q[:110]}")


if __name__ == "__main__":
    main()
