"""H15: the timings section of Revision/kohn_sham/reference/README.md from the H15 rerun: the step times of
run_h15.sh (STEPLOG) and the job seconds stored in the job cache build/revision/ks-reference-cache.
Usage: patch_ref_timings_h15.py STEPLOG"""
import pickle
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"D:\Developer\github\Dirac_claude")
p = ROOT / "Revision" / "kohn_sham" / "reference" / "README.md"
t = p.read_text(encoding="utf-8")
steps = {}
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    m = re.match(r"(\S+) rc=0 ([0-9.]+) s", line)
    if m:
        steps[m.group(1)] = float(m.group(2))
sec = defaultdict(float)
cnt = defaultdict(int)
longest = defaultdict(list)
for f in (ROOT / "build" / "revision" / "ks-reference-cache").glob("*.pkl"):
    d = pickle.load(open(f, "rb"))
    k = d.get("kind")
    s = float(d.get("seconds") or 0.0)
    sec[k] += s
    cnt[k] += 1
    longest[k].append((s, f.stem.split("__", 1)[-1]))
s1_kinds = ("thermo_main", "ground", "exx", "rescale", "validation", "crossing", "free")
s1 = sum(sec[k] for k in s1_kinds)
n1 = sum(cnt[k] for k in s1_kinds)
top = sorted((x for k in ("thermo_main", "ground") for x in longest[k]), reverse=True)[:3]
topnb = sorted(longest["thermo_nb"], reverse=True)[:2]
names = {"thermo_main": "thermal main states", "ground": "ground states", "exx": "exact-Fock variants", "rescale": "rescaling partners",
         "validation": "the validation state", "crossing": "the crossing demonstration", "free": "the free checks"}
i0 = t.index("## Timings (this machine, 24 cores, `--jobs 20`, 2026-10-17)")
i1 = t.index("\n## The corrected metric (2026-10-16/17)")
new = ("## Timings (this machine, 24 cores, `--jobs 20`, 2026-10-17, the record of H15)\n\n"
       "* Stage 1 (%d jobs, %.0f CPU-seconds: " % (n1, s1)
       + ", ".join("%d %s %.0f s" % (cnt[k], names[k], sec[k]) if cnt[k] > 1 else "%s %.0f s" % (names[k], sec[k]) for k in s1_kinds)
       + ") in six parts, the machine otherwise idle: " + ", ".join("%.1f" % steps["ref-s1p%d" % i] for i in range(1, 6))
       + " and %.1f s. The longest single jobs: " % steps["ref-s1p6"]
       + ", ".join("%s (%.1f s)" % (n, s) for s, n in top) + ".\n"
       "* Stage 2 (%d jobs, the temperature neighbours, %.0f CPU-seconds) in six parts: " % (cnt["thermo_nb"], sec["thermo_nb"])
       + ", ".join("%.1f" % steps["ref-s2p%d" % i] for i in range(1, 6)) + " and %.1f s. The longest single jobs: " % steps["ref-s2p6"]
       + ", ".join("%s (%.1f s)" % (n, s) for s, n in topnb) + ".\n"
       "* The assembly from the cache: %.1f s. One invocation without a cache would take about 30 minutes on 20 processes,\n"
       "  longer than the limit of 423 s for one calculation; it was not run.\n"
       "* Before H15 (every state at the SCF tolerance 1e-12 m except the a4 neighbours): stage 1 188.9, 170.9, 199.7, 202.6,\n"
       "  107.2 and 207.3 s (15258 CPU-seconds), stage 2 119.8 to 123.3 s per part, the assembly 4.5 s.\n" % steps["ref-assembly"])
t = t[:i0] + new + t[i1:]
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
