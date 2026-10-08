"""Generate chapter 23 from its template.

@@k a-b@@ lines become quoted code of In [k] of the stored Notebook 23a; {{NAME}} placeholders
are filled with the numbers that the stored Notebook 23a printed (read back from its two data
files and its outputs), so that the chapter always quotes the notebook's own numbers.
Run after every rebuild of Notebook 23a through run_all.py (it also regenerates the glossary).
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # the repository (tools/chapter23 -> tools -> textbook -> Revision -> root)
HERE = Path(__file__).resolve().parent
template = (HERE / "ch23.template.md").read_text(encoding="utf-8")
fills = json.loads((HERE / "fills.json").read_text(encoding="utf-8"))
for key, value in fills.items():
    template = template.replace(key, value)
notebook = json.loads((ROOT / "Revision/textbook/notebooks/23a_reproduce_everything.ipynb")
                      .read_text(encoding="utf-8"))
cells = {c["execution_count"]: "".join(c["source"]).split("\n")
         for c in notebook["cells"] if c["cell_type"] == "code"}
outputs = "\n".join("".join(o.get("text", "")) for c in notebook["cells"]
                    for o in c.get("outputs", []))

with open(ROOT / "Revision/textbook/data/23a_notebooks.csv", encoding="utf-8", newline="") as h:
    rows = list(csv.DictReader(h))
with open(ROOT / "Revision/textbook/data/23a_check_index.csv", encoding="utf-8", newline="") as h:
    index = list(csv.DictReader(h))
seconds = [float(r["seconds"]) for r in rows]
total = sum(seconds)
per = {}
for r in rows:
    per[int(r["chapter"])] = per.get(int(r["chapter"]), 0.0) + float(r["seconds"])
slowest = sorted(seconds, reverse=True)
others = {c: v for c, v in per.items() if c not in (11, 14, 15, 16)}
minc = min(others, key=lambda c: others[c])
maxc = max(others, key=lambda c: others[c])
ch = {c: f"{per[c]:.1f}" for c in per}
ex2 = float(ch[14]) + float(ch[15]) + float(ch[16])
tot = f"{total:.1f}"
u1 = [r for r in index if r["check"] == "u1_noether_matrix_identity"][0]["cited_by_chapters"]
u1words = u1.split()
example = [r for r in index if r["report"].endswith("charge-conjugation-and-u1.json")]
words = "zero one two three four five six seven eight nine ten".split()
sec = [r for r in rows if r["id"] == "05c"][0]["section"]
gate = re.search(r"the gate's step table names (\d+) reports", outputs).group(1)
# the gate numbers of Out [9] (its RESULT lines), quoted in Sections 23.5 and 23.11
gsteps = int(re.search(r"^RESULT gate steps = (\d+)$", outputs, re.M).group(1))
glong = int(re.search(r"^RESULT long steps \(skipped by --fast\) = (\d+)$", outputs, re.M).group(1))
gfull = re.search(r"^RESULT expected wall time of the full gate = (\d+) s = ([\d.]+) h$", outputs, re.M)
gfast = re.search(r"^RESULT expected wall time with --fast = (\d+) s = ([\d.]+) min$", outputs, re.M)
values = {
    "NNB": str(len(rows)), "NCHK": str(sum(int(r["checks"]) for r in rows)),
    "NFIG": str(sum(int(r["figures"]) for r in rows)), "TOTAL": tot,
    "TOTALMIN": str(round(total / 60)), "CH11": ch[11], "CH14": ch[14], "CH15": ch[15],
    "CH16": ch[16], "S11A": f"{[float(r['seconds']) for r in rows if r['id'] == '11a'][0]:.1f}",
    "MINV": ch[minc], "MINC": str(minc), "MAXV": ch[maxc], "MAXC": str(maxc),
    "SHARE3": f"{100 * sum(slowest[:3]) / total:.1f}",
    "EX2SUM": f"{ex2:.1f}", "EX2FRAC": f"{ex2 / float(tot):.4f}",
    "EX2PCT": str(round(100 * ex2 / float(tot))), "HALF": str(round(float(tot) / 2)),
    "NIDX": str(len(index)), "NREP": str(len({r["report"] for r in index})),
    "NCITED": str(sum(bool(r["cited_by_chapters"]) for r in index)),
    "NUNCITED": str(sum(not r["cited_by_chapters"] for r in index)), "NGATE": gate,
    "U1CHS": u1, "U1CHW": ", ".join(u1words[:-1]) + " and " + u1words[-1],
    "U1MIN": words[min(len(r["cited_by_chapters"].split()) for r in example)],
    "SEC05C": sec, "SEC05CNEXT": f"{sec.split('.')[0]}.{int(sec.split('.')[1]) + 1}",
    "GSTEPS": str(gsteps), "GLONG": str(glong), "GFASTN": str(gsteps - glong),
    "GFULLS": gfull.group(1), "GFULLH": gfull.group(2), "GFASTS": gfast.group(1), "GFASTMIN": gfast.group(2),
}
for key, value in values.items():
    template = template.replace("{{" + key + "}}", value)
assert "{{" not in template, re.findall(r"\{\{\w+\}\}", template)

DIRECTIVE = re.compile(r"^@@(\d+) (\d+)-(\d+)@@$")
ELLIPSIS = ("...)", "...),")
out, block = [], []


def flush():
    if block:
        out.append("```python")
        out.extend(block)
        out.append("```")
        block.clear()


for line in template.split("\n"):
    match = DIRECTIVE.match(line)
    if match:
        k, a, b = map(int, match.groups())
        block.extend(cells[k][a - 1:b])
    elif line in ELLIPSIS and block:
        block.append(line)
    else:
        flush()
        out.append(line)
flush()
text = "\n".join(out)
assert "@@" not in text, "unfilled placeholder"
(ROOT / "Revision/textbook/chapters/23-reproducing-everything.md").write_text(
    text, encoding="utf-8", newline="\n")
print("written", len(text.splitlines()), "lines;", json.dumps(values)[:400])
