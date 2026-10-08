"""Rebuild and check every notebook of the textbook (after the tool patch of 2026-10-08).

For each builder Revision/textbook/notebooks/src/*.py (or the ones given): nbkit build --date DATE, then nbkit check
(a second, independent execution compared byte for byte, including the provenance regenerated from its record), then
nbkit check --record DATE (stores the check result in the provenance record).  JOBS builders run at the same time.
Logs: LOGDIR/<builder>.build.log, .check.log; one summary line per builder in LOGDIR/summary.txt, then 'ALL DONE'.
Exit status 0 only when every builder built and checked.

Usage (repository root):  python Revision/workflows/completion/rebuild_all_notebooks.py LOGDIR [--jobs N] [--date D] [BUILDER...]
"""
import argparse
import concurrent.futures as cf
import glob
import os
import subprocess
import sys
import time

ap = argparse.ArgumentParser()
ap.add_argument("logdir")
ap.add_argument("--jobs", type=int, default=5)
ap.add_argument("--date", default="2026-10-08")
ap.add_argument("builders", nargs="*")
args = ap.parse_args()
builders = args.builders or sorted(glob.glob("Revision/textbook/notebooks/src/[0-9][0-9][a-z]_*.py"))
os.makedirs(args.logdir, exist_ok=True)
env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
NBKIT = "Revision/textbook/tools/nbkit.py"


def run(cmd, log):
    with open(log, "w", encoding="utf-8") as f:
        return subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, env=env).returncode


def one(builder):
    name = os.path.basename(builder)[:-3]
    t = time.time()
    scratch = os.path.join(args.logdir, "scratch_" + name)
    rb = run([sys.executable, NBKIT, "build", builder, "--date", args.date, "--scratch", scratch],
             os.path.join(args.logdir, name + ".build.log"))
    rc = run([sys.executable, NBKIT, "check", builder, "--scratch", scratch, "--record", args.date],
             os.path.join(args.logdir, name + ".check.log")) if rb == 0 else -1
    line = f"{name} build={rb} check={rc} {time.time() - t:.0f}s"
    with open(os.path.join(args.logdir, "summary.txt"), "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return rb == 0 and rc == 0


with cf.ThreadPoolExecutor(args.jobs) as ex:
    ok = list(ex.map(one, builders))
with open(os.path.join(args.logdir, "summary.txt"), "a", encoding="utf-8") as f:
    f.write(f"ALL DONE: {sum(ok)} of {len(ok)} built and checked\n")
sys.exit(0 if all(ok) else 1)
