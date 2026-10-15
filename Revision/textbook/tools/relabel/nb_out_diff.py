"""Compare the text outputs of rebuilt notebooks with those committed at HEAD.
Usage: nb_out_diff.py NBID... (e.g. 01g 02c); prints, per notebook, the output lines that changed (old -> new)."""
import difflib
import glob
import json
import subprocess
import sys


def outputs(nb):
    lines = []
    for c in nb["cells"]:
        if c["cell_type"] != "code":
            continue
        k = c.get("execution_count")
        for o in c.get("outputs", []):
            t = "".join(o.get("text", "")) or "".join(o.get("data", {}).get("text/plain", ""))
            for line in t.splitlines():
                lines.append(f"[{k}] {line}")
    return lines


for nid in sys.argv[1:]:
    paths = glob.glob(f"Revision/textbook/notebooks/{nid}_*.ipynb")
    if not paths:
        print(f"== {nid}: no notebook")
        continue
    path = paths[0].replace("\\", "/")
    old = subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True)
    if old.returncode:
        print(f"== {nid}: not at HEAD")
        continue
    a = outputs(json.loads(old.stdout.decode("utf-8")))
    b = outputs(json.load(open(path, encoding="utf-8")))
    diff = [d for d in difflib.unified_diff(a, b, lineterm="", n=0) if d[:1] in "+-" and d[:3] not in ("+++", "---")]
    print(f"== {nid}: {len(diff)} changed output lines")
    for d in diff:
        print("  " + d[:220])
