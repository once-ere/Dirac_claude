"""Filter the candidate bold terms and group them by a normalised key.

Writes groups.json (key -> list of records in book order) and terms.txt for review.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]  # the repository (tools/chapter23 -> tools -> textbook -> Revision -> root)

HERE = Path(__file__).resolve().parent
WORK = ROOT / "build" / "chapter23"  # intermediate files (git-ignored)
WORK.mkdir(parents=True, exist_ok=True)
EXCLUDE_FILE = HERE / "exclude.txt"

STOP_START = ("In [", "Out [", "Exercise", "Answer", "Step ", "Example", "Case ",
              "Proof", "Theorem", "Lemma", "Corollary", "Definition", "Check ", "Note",
              "Warning", "Why", "What", "How", "Result", "Reading", "Rule ")
EMPHASIS = set("""not no never only every all each any exactly same different before after
must cannot does is are also both none one two three four five six seven eight true false
yes and or but more less same opposite once twice first second third last zero nonzero
always both together independently differ differs equal unequal fails holds
""".split())
VERBISH = re.compile(r"\b(is|are|was|were|has|have|does|do|did|solves|gives|turns|must|"
                     r"cannot|can|will|would|should|shows|holds|fails|changes|equals|"
                     r"means|makes|follows|vanishes|reverses|exchanges|preserves)\b")


def strip_math(text: str) -> str:
    return re.sub(r"\$[^$]*\$", "", text).strip()


def key_of(term: str) -> str:
    t = strip_math(term)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = t.lower().replace("ü", "ue").replace("ö", "oe").strip(" ,;:()[]'\"")
    t = re.sub(r"^(the|a|an)\s+", "", t)
    t = re.sub(r"[\s\-]+", " ", t).strip()
    return t


def keep(term: str) -> bool:
    raw = term.strip()
    if not raw:
        return False
    if raw[-1] in ".:?!":
        return False
    if raw.startswith(STOP_START):
        return False
    plain = strip_math(raw)
    if not re.search(r"[A-Za-z]", plain):
        return False
    words = plain.split()
    if len(words) > 6:
        return False
    if len(words) == 1 and plain.lower() in EMPHASIS:
        return False
    if all(w.lower() in EMPHASIS for w in words):
        return False
    if VERBISH.search(plain.lower()) and len(words) > 2:
        return False
    return True


def main():
    data = json.loads((WORK / "candidates.json").read_text(encoding="utf-8"))
    exclude = set()
    if EXCLUDE_FILE.exists():
        exclude = {line.strip() for line in EXCLUDE_FILE.read_text(
            encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}
    groups: dict[str, list] = {}
    for rec in data:
        if rec["term"] is None or not keep(rec["term"]):
            continue
        if rec["file"].startswith("23-") and rec["section"] == "23.5":
            continue  # refix:23: the bold labels of the gate's step groups are no words
        k = key_of(rec["term"])
        if not k or k in exclude:
            continue
        groups.setdefault(k, []).append(rec)
    # merge plurals into singulars
    keys = sorted(groups)
    for k in keys:
        if k not in groups:
            continue
        for singular in (k[:-1] if k.endswith("s") else None,
                         k[:-2] if k.endswith("es") else None,
                         k[:-3] + "y" if k.endswith("ies") else None,
                         k[:-4] + "ix" if k.endswith("ices") else None):
            if singular and singular != k and singular in groups:
                groups[singular].extend(groups.pop(k))
                break
    # merge space/hyphen-less variants
    compact: dict[str, str] = {}
    for k in sorted(groups):
        c = k.replace(" ", "")
        if c in compact and compact[c] in groups:
            groups[compact[c]].extend(groups.pop(k))
        else:
            compact[c] = k
    for k in groups:
        groups[k].sort(key=lambda r: r["order"])
    (WORK / "groups.json").write_text(json.dumps(groups, indent=1, ensure_ascii=False),
                                      encoding="utf-8", newline="\n")
    with open(WORK / "terms.txt", "w", encoding="utf-8", newline="\n") as f:
        for k in sorted(groups):
            r = groups[k][0]
            f.write(f"{k}\t{len(groups[k])}\t{r['section']}\n")
    print("groups", len(groups))


if __name__ == "__main__":
    main()
