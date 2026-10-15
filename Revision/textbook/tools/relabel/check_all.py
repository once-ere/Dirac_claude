"""Run `nbkit.py check` on the textbook builders of the given chapters, 8 at a time, each with
a hard limit of 423 s, and write one line per notebook: name, status, seconds, first problem.
Usage: check_all.py OUT.tsv CHAPTER_PREFIX..."""
import concurrent.futures
import re
import subprocess
import tempfile
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder
SCRATCH = Path(tempfile.gettempdir()) / "textbook_check_all"  # outside the repository
out_path = Path(sys.argv[1])
prefixes = sys.argv[2:]
builders = sorted(b for b in (REPO / "Revision/textbook/notebooks/src").glob("*.py")
                  if any(b.name.startswith(p) for p in prefixes))
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def run(builder):
    scratch = SCRATCH / builder.stem
    start = time.time()
    try:
        done = subprocess.run([sys.executable, "-B", "Revision/textbook/tools/nbkit.py", "check",
                               str(builder), "--scratch", str(scratch)], cwd=REPO,
                              capture_output=True, text=True, timeout=423, encoding="utf-8",
                              errors="replace")
        text = ANSI.sub("", done.stdout + done.stderr)
        status = "OK" if done.returncode == 0 and "nbkit=OK" in text else "FAILED"
        problem = ""
        for pattern in (r"AssertionError: (check failed: [^\n]*)", r"(\w*Error: [^\n]*)",
                        r"(problem=[^\n]*)", r"(differ[^\n]*)"):
            m = re.search(pattern, text)
            if m:
                problem = m.group(1)[:300]
                break
    except subprocess.TimeoutExpired:
        status, problem = "TIMEOUT", "killed at 423 s"
    return builder.stem, status, round(time.time() - start, 1), problem


with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool, \
        open(out_path, "w", encoding="utf-8") as out:
    for name, status, seconds, problem in pool.map(run, builders):
        out.write(f"{name}\t{status}\t{seconds}\t{problem}\n")
        out.flush()
print("done", len(builders))
