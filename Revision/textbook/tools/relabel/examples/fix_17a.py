"""17a builder: the record ks-source-conditions.json has a sixth check since the metric
change of 2026-10-14 (ks_verdict_holds_for_every_b4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/17a_source_conditions.py"
s = p.read_text(encoding="utf-8")
s = strict_replace(s, [
    ('''    source conditions, prints its conclusion and checks that its five checks passed.
    """),''',
     '''    source conditions, prints its conclusion and checks that its six checks passed:
    the five on the Kohn-Sham states, which this notebook reproduces, and the sixth,
    `ks_verdict_holds_for_every_b4`, which states that the verdict holds for the
    author's metric with any second function $b_4(x_4)$ of 2026-10-14 (the conditions
    C1 to C3 below are derived on the background $b_4 = 1$).
    """),'''),
    ('''    check(summary == {"checks": 5, "pass": 5, "fail": 0},
          "the record on the Kohn-Sham source conditions has 5 checks, all PASS")''',
     '''    check(summary == {"checks": 6, "pass": 6, "fail": 0},
          "the record on the Kohn-Sham source conditions has 6 checks, all PASS")'''),
], "17a")
p.write_bytes(s.encode("utf-8"))
print("ok")
