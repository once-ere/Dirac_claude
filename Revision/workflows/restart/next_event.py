"""Return as soon as any workflow agent finishes; print a short summary of each new result.

Usage: python next_event.py [max_seconds] [<session dir>/subagents/workflows]
Keeps per-journal line offsets in next_event_state.json next to this file, so each call reports only new results.
Exits immediately when results are already pending; otherwise polls every 2 s until one arrives or max_seconds pass.
"""
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

W = sys.argv[2] if len(sys.argv) > 2 else os.environ["WORKFLOW_JOURNALS"]  # the session's subagents/workflows folder
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "next_event_state.json")
MAX = float(sys.argv[1]) if len(sys.argv) > 1 else 540


def load():
    try:
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def scan(state):
    out = []
    for wf in sorted(os.listdir(W)):
        p = os.path.join(W, wf, "journal.jsonl")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            lines = f.read().splitlines()
        labels = {}
        for ln in lines:
            try:
                e = json.loads(ln)
            except ValueError:
                continue
            if e.get("type") == "started":
                labels[e.get("agentId")] = e.get("label")
        seen = state.get(wf, None)
        if seen is None:          # first sight of a workflow: report its results from now on only
            state[wf] = len(lines)
            continue
        for ln in lines[seen:]:
            try:
                e = json.loads(ln)
            except ValueError:
                continue
            if e.get("type") not in ("result", "error", "failed", "workflow_result", "done", "completed"):
                if e.get("type") != "started":
                    out.append(f"[{wf}] event type={e.get('type')}: {ln[:300]}")
                continue
            r = e.get("result")
            lab = labels.get(e.get("agentId"), e.get("agentId"))
            if isinstance(r, dict) and "findings" in r:
                sev = {}
                for f in r["findings"]:
                    sev[f.get("severity")] = sev.get(f.get("severity"), 0) + 1
                out.append(f"[{wf}] {lab}: findings {sev or 0}; " + " | ".join(
                    f"[{f.get('severity')}] {f.get('problem', '')[:160]}" for f in r["findings"] if f.get("severity") != "minor"))
            elif isinstance(r, dict) and "refuted" in r:
                out.append(f"[{wf}] {lab}: refuted={r['refuted']}: {r.get('reason', '')[:160]}")
            elif isinstance(r, dict) and "all_checks_pass" in r:
                out.append(f"[{wf}] {lab}: pass={r['all_checks_pass']} failing={[x[:120] for x in r.get('failing', [])][:4]} | {r.get('summary', '')[:200]}")
            else:
                out.append(f"[{wf}] {lab}: {str(r)[:300]}")
        state[wf] = len(lines)
    return out


t0 = time.time()
state = load()
while True:
    new = scan(state)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f)
    if new:
        print("\n".join(new))
        break
    if time.time() - t0 > MAX:
        print(f"no new results in {MAX:.0f} s")
        break
    time.sleep(2)
