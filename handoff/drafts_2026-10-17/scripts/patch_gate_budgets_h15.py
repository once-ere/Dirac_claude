"""H15: the gate budgets (expected wall time, rounded up to 5 s) of the Kohn-Sham steps from the measured times of the
H15 rerun (the step log of run_h15.sh), in both twins of the gate: the step table rows `name|budget|...` and the header
comment lines `#   name  budget s [long]`.  Usage: patch_gate_budgets_h15.py STEPLOG"""
import math
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\Developer\github\Dirac_claude\Revision")
steps = {}
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    m = re.match(r"(\S+) rc=0 ([0-9.]+) s", line)
    if m:
        steps[m.group(1)] = float(m.group(2))
MAP = {}
for i in (1, 2, 3):
    MAP["rust-repeat-p%d" % i] = "ks-rust-repeat-part%d" % i
MAP["rust-repeat"] = "ks-rust-repeat"
for i in (1, 2, 3, 4):
    MAP["rust-refined-p%d" % i] = "ks-rust-refined-part%d" % i
MAP["rust-refined"] = "ks-rust-refined"
MAP["rust-determinism"] = "ks-rust-determinism"
MAP["rust-refinement"] = "ks-rust-refinement"
for st in (1, 2):
    for i in range(1, 7):
        MAP["ref-s%dp%d" % (st, i)] = "ks-reference-s%d-part%d" % (st, i)
        MAP["cc-s%dp%d" % (st, i)] = "ks-crosscheck-repeat-s%d-part%d" % (st, i)
MAP["ref-assembly"] = "ks-reference"
MAP["crosscheck"] = "ks-crosscheck"
for i in range(1, 7):
    MAP["tip-scan-p%d" % i] = "ks-tip-convergence-scan-part%d" % i
for i in (1, 2, 3):
    MAP["tip-recal-p%d" % i] = "ks-tip-convergence-recal-part%d" % i
    MAP["hist-p%d" % i] = "dark16-ks-history-part%d" % i
MAP["tip-final"] = "ks-tip-convergence"
MAP["hist-assembly"] = "dark16-ks-history"
MAP["ks-source-conditions"] = "a4-ks-source-conditions"
MAP["ks-source"] = "a4-ks-source"
MAP["ks-source-test"] = "a4-ks-source-unittest"
budgets = {MAP[k]: max(5, int(math.ceil(v / 5.0)) * 5) for k, v in steps.items() if k in MAP}
over = {n: b for n, b in budgets.items() if b > 423}
assert not over, over
for twin in ("verify_revision.sh", "verify_revision.ps1"):
    p = ROOT / twin
    lines = p.read_text(encoding="utf-8").split("\n")
    done = set()
    for idx, line in enumerate(lines):
        for name, b in budgets.items():
            if line.startswith(name + "|"):
                parts = line.split("|")
                parts[1] = str(b)
                lines[idx] = "|".join(parts)
                done.add(("row", name))
            m = re.match(r"(#   )(\S+)(\s+)(\d+)( s.*)$", line)
            if m and m.group(2) == name:
                prefix = m.group(1) + name
                lines[idx] = prefix + str(b).rjust(44 - len(prefix)) + m.group(5)
                done.add(("comment", name))
    missing = [(k, n) for n in budgets for k in ("row", "comment") if (k, n) not in done]
    assert not missing, (twin, missing)
    p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print("patched", twin, len(budgets), "budgets")
for n in sorted(budgets):
    print(n, budgets[n])
