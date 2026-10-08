"""Merge the finished agent results of all journals of one workflow family into one state file.

Only results written before a run was resumed (the first repeated 'started' label) are taken from runs that were
resumed and then stopped (their later results may judge half-fixed files); continuation runs are taken whole.
Later runs override earlier ones for the same label.
"""
import json
import os
import sys

W = "C:/Users/nsh/.claude/projects/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/subagents/workflows"
OUT = sys.argv[1]

FAMILIES = {
    "textbook": [("wf_bf3a3e31-ec0", "pre-resume"), ("wf_1964f603-07f", "all")],
    "execution_provenance": [("wf_f856ecb5-265", "pre-resume"), ("wf_5cf02970-bb6", "all")],
    "dirac_audit": [("wf_5ccefead-ea3", "pre-resume"), ("wf_ff12b9f0-bb0", "all")],
    "wave_1b_2": [("wf_987b1061-79b", "all")],
    "a4_prep": [("wf_da94d8ca-701", "all")],
}


def results(run, mode):
    p = os.path.join(W, run, "journal.jsonl")
    lines = open(p, encoding="utf-8").read().splitlines()
    labels, seen, boundary = {}, set(), None
    for i, ln in enumerate(lines):
        e = json.loads(ln)
        if e.get("type") == "started":
            lab = e.get("label")
            if lab in seen and boundary is None:
                boundary = i
            seen.add(lab)
            labels[e["agentId"]] = lab
    upto = boundary if mode == "pre-resume" and boundary is not None else len(lines)
    out = {}
    for ln in lines[:upto]:
        e = json.loads(ln)
        if e.get("type") == "result" and e.get("result") is not None:
            out[labels.get(e["agentId"], e["agentId"])] = e["result"]
    return out


os.makedirs(OUT, exist_ok=True)
for fam, runs in FAMILIES.items():
    merged = {}
    for run, mode in runs:
        merged.update(results(run, mode))
    with open(os.path.join(OUT, f"state_{fam}.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(merged, f, indent=1, sort_keys=True)
        f.write("\n")
    print(fam, len(merged), sorted(merged))
