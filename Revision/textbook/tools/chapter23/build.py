"""Build the glossary text (section 23.17) from groups.json; validate its references.

Writes glossary.md (the body of the section, without its heading) and report.txt.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]  # the repository (tools/chapter23 -> tools -> textbook -> Revision -> root)

HERE = Path(__file__).resolve().parent
WORK = ROOT / "build" / "chapter23"  # intermediate files (git-ignored)
WORK.mkdir(parents=True, exist_ok=True)
TB = ROOT / "Revision" / "textbook"
SECTION = re.compile(r"^### (\d+)\.(\d+) ")
LOWER_NAMES = {"numpy", "sympy", "matplotlib", "mpmath", "nbkit", "dirac16complex",
               "dirac16complex00", "cargo", "git", "pdflatex", "json", "csv", "png",
               "wolframscript", "einsum", "jupyterlab", "sha256", "nbclient", "nbformat",
               "ipykernel", "pathlib", "xorshift64*"}
DEFINING = re.compile(r"^\s*(?:\$[^$]*\$\s*)?(?:\([^)]*\)\s*)?(?:is|are|means|:|,? or|"
                      r"\(|=|stands|counts|measures|gives|denotes)")
DEFINING_BEFORE = re.compile(r"(?:called|call|named|name|is|are|means|say|says|"
                             r"defined as|known as)\s+(?:a|an|the)?\s*$|\(\s*$")


def all_sections() -> set[str]:
    sections = set()
    for path in sorted((TB / "chapters").glob("[0-9][0-9]-*.md")):
        in_code = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            m = SECTION.match(line) if not in_code else None
            if m:
                sections.add(f"{int(m.group(1))}.{int(m.group(2))}")
    nb = json.loads((WORK / "nb_section.json").read_text(encoding="utf-8"))
    for text_section, _ in nb.values():
        ch, sec = text_section.split(".")
        sections.add(text_section)
        sections.add(f"{ch}.{int(sec) - 1}")
    return sections


NB_OF_SECTION: dict[str, list[str]] = {}
for _nb, (_text, _order) in json.loads((WORK / "nb_section.json").read_text(
        encoding="utf-8")).items():
    _ch, _sec = _text.split(".")
    # the walk-through of a notebook is the section right after its text section
    NB_OF_SECTION.setdefault(f"{_ch}.{int(_sec) + 1}", []).append(_nb)
    NB_OF_SECTION.setdefault(_text, []).append(_nb)


REPLACE = {
    "`n >> p & 1` reads that digit": "the program reads that digit by shifting $n$ to "
    "the right by $p$ binary places and keeping the last binary digit",
}


def sec_key(s: str):
    a, b = s.split(".")
    return int(a), int(b)


INCOMPLETE = re.compile(r"(?::|\b(?:is|are|reads|read|becomes|gives))\s*$")


def incomplete(text: str) -> bool:
    return bool(INCOMPLETE.search(text.rstrip()))


def complete(text: str, rec) -> str:
    """Append the displayed formula that the defining sentence leads into."""
    if incomplete(text) and rec.get("display"):
        return text.rstrip() + " $" + rec["display"].rstrip(" .,") + "$"
    if incomplete(text):
        return text.rstrip().rstrip(":") + " (the formula is displayed in that section)"
    return text


def priority(rec) -> int:
    if incomplete(rec["definition"]) and not rec.get("display"):
        return 3
    if rec.get("kind") == "head":
        return 0
    term = rec["term"]
    d = rec["definition"]
    plain = d.replace("**", "")
    i = d.find("**" + term + "**")
    if i >= 0:
        after = d[i + len(term) + 4:]
        before = d[:i].replace("**", "")
        if DEFINING.match(after) or DEFINING_BEFORE.search(before):
            return 1
    return 2


def sort_key(display: str) -> str:
    t = re.sub(r"\$[^$]*\$", "", display).replace("**", "").replace("`", "")
    t = t.replace("ü", "u").replace("ö", "o").replace("Γ", "gamma")
    t = re.sub(r"^[^A-Za-z0-9]+", "", t)
    t = re.sub(r"^(the|a|an)\s+", "", t, flags=re.I)
    return t.lower()


def clean(text: str) -> str:
    t = text.replace("**", "").strip()
    if t.startswith("- "):
        t = t[2:]
    t = re.sub(r"\s+", " ", t)
    if t and not t.endswith((".", "!", "?", ".)", "?)", "!)")):
        t = t.rstrip(";,") + "."
    return t


def contextual(text: str, rec) -> str:
    """Make phrases that point at the source's own context explicit."""
    chapter = str(int(rec["file"][:2]))
    if rec["source"] == "notebook":
        nb = rec["nb"]
        text = re.sub(r"\b[Tt]his notebook\b", f"Notebook {nb}", text)
        text = re.sub(r"\b([Ss]ection|[Ss]ections) (\d+)\b(?![.\d])",
                      lambda m: f"{m.group(1).lower()} {m.group(2)} of Notebook {nb}", text)
    else:
        nbs = [m for m in NB_OF_SECTION.get(rec["section"], [])]
        if len(nbs) == 1:
            text = re.sub(r"\b[Tt]his notebook\b", f"Notebook {nbs[0]}", text)
            text = re.sub(r"\b(section|sections) (\d+)\b(?![.\d])",
                          lambda m: f"{m.group(1)} {m.group(2)} of Notebook {nbs[0]}",
                          text)
    text = re.sub(r"\b([Ii]n|[Oo]f|[Aa]ll maps of) this chapter\b",
                  lambda m: f"{m.group(1)} Chapter {chapter}", text)
    text = re.sub(r"\bthis chapter\b", f"Chapter {chapter}", text)
    text = re.sub(r"(^|[.!?] )section (\d+) of Notebook (\w+)",
                  r"\1In Notebook \3, section \2", text)
    return text


def display_head(rec) -> str:
    if rec.get("kind") == "head":
        head = rec["head"].strip()
    else:
        head = "**" + rec["term"].strip() + "**"
    # capitalise the first plain word
    m = re.match(r"^(\*\*)([a-z])", head)
    if m:
        first = re.match(r"\*\*([^*]*)\*\*", head).group(1)
        if first.split()[0].lower() not in LOWER_NAMES and not first.startswith("`"):
            head = "**" + head[2].upper() + head[3:]
    return head


def main():
    groups = json.loads((WORK / "groups.json").read_text(encoding="utf-8"))
    extra = json.loads((HERE / "manual.json").read_text(encoding="utf-8")) \
        if (HERE / "manual.json").exists() else {}
    # merge combined keys "x, y" / "x (y" into components that exist on their own
    for k in sorted(groups):
        # refix:23: only a FINAL parenthesis after a space ("x (y") is a qualifier;
        # "spin(4,3" and "symmetric (belinfante) energy momentum tensor" are words
        base = re.sub(r"\s+\([^()]*\)?$", "", k).strip()
        parts = [p.strip() for p in re.split(r",\s*|\s*/\s*", base) if p.strip()]
        if len(parts) > 1 and all(p in groups for p in parts):
            for p in parts:
                for r in groups[k]:
                    groups[p].append(dict(r, combined=True))
            del groups[k]
        elif len(parts) == 1 and base != k and base in groups:
            for r in groups[k]:
                groups[base].append(dict(r, combined=True))
            del groups[k]
    for k in extra:
        groups.setdefault(k, [])
    sections = all_sections()
    entries = []
    report = []
    for k, recs in groups.items():
        recs.sort(key=lambda r: r["order"])
        if k in extra:
            head, definition = extra[k]["head"], extra[k]["definition"]
            locs = extra[k].get("sections") or []
        else:
            standalone = [r for r in recs if not r.get("combined")] or recs
            best = min(standalone, key=lambda r: (priority(r), r["order"]))
            head = display_head(best)
            definition = contextual(clean(complete(best["definition"], best)), best)
            for a, z in REPLACE.items():
                definition = definition.replace(a, z)
            locs = []
        for r in recs:
            if r["section"] and r["section"] not in locs:
                locs.append(r["section"])
        locs = sorted(set(locs), key=sec_key)
        for s in locs:
            if s not in sections and not s.endswith(".0"):
                report.append(f"missing section {s} for {k}")
        openings = [s.split(".")[0] for s in locs if s.endswith(".0")]
        secs = [s for s in locs if not s.endswith(".0")]
        parts = []
        if len(secs) == 1:
            parts.append(f"Section {secs[0]}")
        elif secs:
            parts.append("Sections " + ", ".join(secs[:-1]) + " and " + secs[-1])
        for c in openings:
            parts.append(f"the opening of Chapter {c}")
        where = "(" + "; ".join(parts) + ".)"
        entries.append((sort_key(head), head, definition, where, k))
    entries.sort(key=lambda e: (e[0], e[1]))
    lines = []
    letter = None
    for key, head, definition, where, k in entries:
        first = key[:1].upper() if key[:1].isalpha() else "0-9"
        if first != letter:
            if lines:
                lines.append("")
            lines.append(f"**{first}**")
            lines.append("")
            letter = first
        lines.append(f"- {head}: {definition} {where}")
        for pat in (r"(?<![A-Za-z])[Ss]ection \d+(?![\d.])", "--", "<<", ">>", "``", "''",
                    r"\bthis notebook\b", r"\bthis chapter\b", r"In \[\d+\]",
                    r"Out \[\d+\]", r"\bbelow\b", r"\babove\b"):
            if re.search(pat, re.sub(r"\$[^$]*\$", "", definition)):
                report.append(f"pattern {pat!r} in {k}: {definition[:160]}")
    text = "\n".join(lines) + "\n"
    (WORK / "glossary.md").write_text(text, encoding="utf-8", newline="\n")
    (WORK / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8",
                                     newline="\n")
    print("entries", len(entries), "report lines", len(report), "chars", len(text))


if __name__ == "__main__":
    main()
