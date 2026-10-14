"""Old Stage 4, steps R2-R4 after the reference rerun R1 (HANDOFF 0.4u item 4).  Run from the repository root:
    python <this file>
Stops at the first failing step; every step's output goes to <this folder>/R*.log; a summary to summary.txt.
R2: replace artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0 with the R1 run directory, then
    ks_reference_solver.py --resume --skip-self-tests (rewrites the reference summary);
R3: check_dirac16complex_kohn_sham.py with the preserved repeat/refined Rust trees (python-check-report.json);
R4: notebook route B (run_notebook.py), route A (nbconvert into build/nbconvert), the notebook checker.
R5 (the tests) and the document/errata edits are done by the lead after reviewing these logs."""
import hashlib
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.dirname(HERE)
LABEL = "m1_L3_N1016_lamm2_T0"
R1 = os.path.join(SP, "stage4_R1")
KEEP = "C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad/stage4_keep"  # preserved Rust trees of 2026-10-08
TARGET = os.path.join("artifacts", "dirac16complex", "kohn-sham", "reference", LABEL)
SOLVER_SHA = "8dbedada523de6df7346921edf6c926058e97fe296ba9c2f24331524b0a60494"
env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")


def log_line(text):
    with open(os.path.join(HERE, "summary.txt"), "a", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(text, flush=True)


def run(name, command):
    started = time.time()
    with open(os.path.join(HERE, name + ".log"), "w", encoding="utf-8") as handle:
        code = subprocess.run(command, stdout=handle, stderr=subprocess.STDOUT, env=env).returncode
    log_line(f"{name} exit={code} {time.time() - started:.0f}s :: {' '.join(command)}")
    if code != 0:
        log_line("ALL DONE: stopped at " + name)
        sys.exit(1)


done = open(os.path.join(R1, "done.txt"), encoding="utf-8", errors="replace").read()
if "exit=0" not in done:
    log_line("R1 did not end with exit=0: " + done.strip())
    log_line("ALL DONE: not started")
    sys.exit(1)
with open(os.path.join("scripts", "ks_reference_solver.py"), "rb") as handle:
    sha = hashlib.sha256(handle.read()).hexdigest()
if sha != SOLVER_SHA:
    log_line("the reference solver changed since R1 started: " + sha)
    log_line("ALL DONE: not started")
    sys.exit(1)
source = os.path.join(R1, "out", LABEL)
if not os.path.isfile(os.path.join(source, "run.json")):
    log_line("no run.json in " + source)
    log_line("ALL DONE: not started")
    sys.exit(1)
# R2
backup = os.path.join(HERE, "previous_" + LABEL)
if not os.path.exists(backup):
    shutil.copytree(TARGET, backup)
shutil.rmtree(TARGET)
shutil.copytree(source, TARGET)
log_line("R2a replaced " + TARGET + " (previous copy in " + backup + ")")
run("R2b_resume", [sys.executable, "-B", "scripts/ks_reference_solver.py", "--resume", "--skip-self-tests"])
# R3
run("R3_checker", [sys.executable, "-B", "scripts/check_dirac16complex_kohn_sham.py", "--repeat",
                   os.path.join(KEEP, "repeat"), "--refined", os.path.join(KEEP, "refined")])
# R4
run("R4a_route_B", [sys.executable, "notebooks/run_notebook.py", "notebooks/dirac16complex_kohn_sham.ipynb"])
run("R4b_route_A", [sys.executable, "-m", "nbconvert", "--to", "notebook", "--execute",
                    "notebooks/dirac16complex_kohn_sham.ipynb", "--output-dir", "build/nbconvert"])
run("R4c_notebook_check", [sys.executable, "notebooks/check_dirac16complex_kohn_sham_notebook.py",
                           "notebooks/dirac16complex_kohn_sham.ipynb", "--also",
                           "build/nbconvert/dirac16complex_kohn_sham.ipynb", "--report",
                           "artifacts/dirac16complex/kohn-sham/notebook-report.json"])
log_line("ALL DONE: R2-R4 passed")
