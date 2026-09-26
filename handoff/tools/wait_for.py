"""Block until background workflow tasks finish, or until a time budget expires.

Usage: python wait_for.py BUDGET_SECONDS TASK_ID [TASK_ID ...]
Prints one status line per task and exits 0 when ANY listed task has finished
(its output file exists and is non-empty), 3 when the budget expired.
Also prints per-workflow agent progress so a stall is visible.
"""
import os
import sys
import time
import glob

TASKS = r"C:\Users\nsh\AppData\Local\Temp\claude\C--Users-nsh-Developer-github-Dirac-claude\cc75e05b-1dc1-4a82-a1dd-e65cb8479099\tasks"
WF = r"C:\Users\nsh\.claude\projects\C--Users-nsh-Developer-github-Dirac-claude\cc75e05b-1dc1-4a82-a1dd-e65cb8479099\subagents\workflows"


def done(task):
    p = os.path.join(TASKS, task + ".output")
    return os.path.exists(p) and os.path.getsize(p) > 0


def progress():
    now = time.time()
    lines = []
    for d in sorted(glob.glob(os.path.join(WF, "wf_*"))):
        j = os.path.join(d, "journal.jsonl")
        if not os.path.exists(j):
            continue
        try:
            with open(j, encoding="utf-8", errors="replace") as f:
                txt = f.read()
            results = txt.count('"type":"result"')
            agents = glob.glob(os.path.join(d, "agent-*.jsonl"))
            ages = sorted(int(now - os.path.getmtime(a)) for a in agents)
            lines.append(f"{os.path.basename(d)} results={results} agents={len(agents)} idle_s={ages}")
        except OSError as exc:
            lines.append(f"{os.path.basename(d)} unreadable: {exc}")
    return lines


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    budget = float(sys.argv[1])
    tasks = sys.argv[2:]
    t0 = time.time()
    while True:
        try:
            finished = [t for t in tasks if done(t)]
        except OSError:
            finished = []
        if finished or time.time() - t0 > budget:
            for t in tasks:
                try:
                    state = "FINISHED" if done(t) else "running"
                except OSError:
                    state = "unknown"
                print(f"task {t}: {state}")
            try:
                for line in progress():
                    print(line)
            except Exception as exc:  # never let reporting kill the wait
                print(f"progress unavailable: {exc!r}")
            sys.exit(0 if finished else 3)
        time.sleep(15)


if __name__ == "__main__":
    main()
