"""Mark in Revision/README.md which documents are on the corrected metric (W7, 2026-10-17)."""
import sys
from pathlib import Path

p = Path(r"D:\Developer\github\Dirac_claude\Revision\README.md")
s = p.read_text(encoding="utf-8")
old = ("all six in the author's coordinates x0..x7 and for the metric with b4(x4), general a4 and b4 (b4 never 1; the four "
       "documents that still described b4 = 1 were moved on 2026-10-16, `HANDOFF.md` 0.9, phase 8)")
new = ("all six in the author's coordinates x0..x7; rewritten for the corrected metric of 2026-10-16 (version 2, every "
       "real z) in phase W7 of `HANDOFF.md` 0.10/0.11: LOVELOCK_GKD and DIRAC16COMPLEX00_FIELD_THEORY (2026-10-17); "
       "the other four still describe the metric of 2026-10-14 and are rewritten after the records they cite (W5, W6)")
if old in s:
    s = s.replace(old, new)
    print("row rewritten")
elif new in s:
    print("already rewritten")
else:
    sys.exit("anchor not found")
extra = sys.argv[1] if len(sys.argv) > 1 else None
if extra:
    done_old = "LOVELOCK_GKD and DIRAC16COMPLEX00_FIELD_THEORY (2026-10-17)"
    assert done_old in s
p.write_text(s, encoding="utf-8", newline="\n")
