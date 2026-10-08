"""Extract every defined technical word of the textbook (chapters + notebook word lists).

Read-only on the repository.  Writes candidates.json and nb_section.json into build/chapter23/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]  # the repository (tools/chapter23 -> tools -> textbook -> Revision -> root)

TB = ROOT / "Revision" / "textbook"
HERE = Path(__file__).resolve().parent
WORK = ROOT / "build" / "chapter23"  # intermediate files (git-ignored)
WORK.mkdir(parents=True, exist_ok=True)

SECTION = re.compile(r"^### (\d+)\.(\d+) (.*)$")
MARKER = re.compile(r"^<!-- NOTEBOOK (\d{2}[a-z]) -->\s*$")
BOLD = re.compile(r"\*\*(.+?)\*\*")
ABBREV = ("e.g.", "i.e.", "cf.", "Fig.", "No.", "vs.", "etc.", "approx.", "St.")


def mask(line: str) -> str:
    """Blank out code spans and inline math (keep positions)."""
    out = list(line)
    for pattern in (r"`[^`]*`", r"\$[^$]*\$"):
        for m in re.finditer(pattern, "".join(out)):
            for p in range(m.start(), m.end()):
                out[p] = "\x00" if out[p] != " " else " "
    return "".join(out)


def sentences(line: str) -> list[tuple[int, int]]:
    """(start, end) spans of the sentences of one paragraph line."""
    masked = mask(line)
    spans = []
    start = 0
    for m in re.finditer(r"(?:(?<=[.!?])|(?<=[.!?]\*\*))\s+(?=[A-Z(*$`\x00\"])", masked):
        before = masked[start:m.start()]
        if any(before.endswith(a) for a in ABBREV):
            continue
        if len(before) >= 2 and before[-1] == "." and before[-2].isupper() and (
                len(before) == 2 or not before[-3].isalnum()):
            continue  # an initial such as "D." of a name
        # do not split inside bold
        if masked[start:m.start()].count("**") % 2:
            continue
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(line)))
    return spans


def bolds(line: str):
    masked = mask(line).replace("\x00", "#")
    # bold may contain math: find ** pairs in a line where code is masked but math kept
    code_masked = list(line)
    for m in re.finditer(r"`[^`]*`", line):
        for p in range(m.start(), m.end()):
            code_masked[p] = "#"
    code_masked = "".join(code_masked)
    for m in BOLD.finditer(code_masked):
        yield m.start(), m.end(), line[m.start() + 2:m.end() - 2]


def next_display(lines, lineno):
    """The one-line display formula right after paragraph line lineno, if any."""
    k = lineno  # index of the next line (lines is 0-based, lineno 1-based)
    while k < len(lines) and not lines[k].strip():
        k += 1
    if k >= len(lines) or lines[k].strip() != "$$":
        return None
    body = []
    k += 1
    while k < len(lines) and lines[k].strip() != "$$":
        body.append(lines[k].strip())
        k += 1
    formula = " ".join(body).strip()
    if (len(body) != 1 or len(formula) > 150 or "\\\\" in formula or "&" in formula
            or "begin" in formula or "tag" in formula):
        return None
    return formula


def chapter_records():
    records = []
    nb_section = {}
    order = 0
    for path in sorted((TB / "chapters").glob("[0-9][0-9]-*.md")):
        number = int(path.name[:2])
        section = f"{number}.0"
        in_code = in_math = False
        all_lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(all_lines, 1):
            s = line.strip()
            if s.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if s == "$$":
                in_math = not in_math
                continue
            if in_math:
                continue
            m = SECTION.match(s)
            if m:
                section = f"{m.group(1)}.{m.group(2)}"
                last = int(m.group(2))
                continue
            m = MARKER.match(s)
            if m:
                nb = m.group(1)
                ch, sec = section.split(".")
                nb_section[nb] = (f"{ch}.{int(sec) + 2}", order)
                order += 1
                continue
            if number == 23 and section == "23.17":
                continue
            for b0, b1, term in bolds(line):
                records.append(dict(term=term, line=line, b0=b0, b1=b1, file=path.name,
                                    display=next_display(all_lines, lineno),
                                    lineno=lineno, section=section, order=order,
                                    source="chapter"))
            order += 1
    return records, nb_section


def notebook_records(nb_section):
    records = []
    for nbpath in sorted((TB / "notebooks").glob("[0-9][0-9][a-z]_*.ipynb")):
        nb = nbpath.name[:3]
        data = json.loads(nbpath.read_text(encoding="utf-8"))
        cell = None
        for c in data["cells"]:
            src = "".join(c["source"]) if isinstance(c["source"], list) else c["source"]
            if c["cell_type"] == "markdown" and src.lstrip().startswith("## 3."):
                cell = src
                break
        if cell is None:
            print("no words section", nb, file=sys.stderr)
            continue
        items = []
        for raw in cell.splitlines()[1:]:
            if raw.startswith("- "):
                items.append(raw[2:].strip())
            elif raw.startswith("  ") and items:
                items[-1] += " " + raw.strip()
            elif raw.strip() and items:
                items[-1] += " " + raw.strip()
        section, order = nb_section.get(nb, (None, None))
        for k, item in enumerate(items):
            for b0, b1, term in bolds(item):
                records.append(dict(term=term, line=item, b0=b0, b1=b1,
                                    file=nbpath.name, lineno=k, section=section,
                                    order=(order if order is not None else 10**6) + k
                                    * 1e-3, source="notebook", nb=nb))
            if not item.startswith("**"):
                records.append(dict(term=None, line=item, b0=0, b1=0, file=nbpath.name,
                                    lineno=k, section=section, order=order,
                                    source="notebook-nonbold", nb=nb))
    return records


def definition(rec) -> tuple[str, str]:
    """(head, definition) for one record."""
    line, b0, b1 = rec["line"], rec["b0"], rec["b1"]
    body = line[2:] if line.startswith("- ") else line
    off = 2 if line.startswith("- ") else 0
    masked = mask(line)
    # list-item head: the bold term at the start of the item, then text up to a colon
    if (line.startswith("- **") and b0 == 2) or b0 == 0:
        colon = masked.find(":", b1)
        if colon != -1 and colon - b1 <= 90:
            head = line[b0:colon].strip()
            rest = line[colon + 1:].strip()
            head_bolds = {t for _, _, t in bolds(head)}
            out = []
            for s0, s1 in sentences(rest):
                sent = rest[s0:s1]
                other = [t for _, _, t in bolds(sent) if t not in head_bolds]
                if other and out:
                    break
                out.append(sent)
            rec["kind"] = "head"
            return head, " ".join(out)
    for s0, s1 in sentences(line):
        if s0 <= b0 < s1 + 1:
            sent = line[s0:s1].strip()
            if sent.startswith("- "):
                sent = sent[2:]
            return rec["term"], sent
    return rec["term"], line


def main():
    chapter, nb_section = chapter_records()
    notebook = notebook_records(nb_section)
    out = []
    for rec in chapter + notebook:
        if rec["term"] is None:
            out.append(dict(rec, head=None, definition=rec["line"]))
            continue
        head, d = definition(rec)
        out.append(dict(rec, head=head, definition=d))
    for r in out:
        r.pop("line")
    (WORK / "candidates.json").write_text(json.dumps(out, indent=1, ensure_ascii=False),
                                          encoding="utf-8", newline="\n")
    (WORK / "nb_section.json").write_text(json.dumps(nb_section, indent=1),
                                          encoding="utf-8", newline="\n")
    print("records", len(out), "chapter", len(chapter), "notebook", len(notebook))
    print("notebooks placed", len(nb_section))


if __name__ == "__main__":
    main()
