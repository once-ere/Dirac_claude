"""Chapter 17: the record's sixth check (every b4), the new gammas.json fingerprint, and a b4
statement."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/17-a4-equations-with-kohn-sham-source.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''- The three **source conditions**: no dependence on the hidden coordinate $x_0$ (C1, Section 17.4), the algebraic condition $p_3 + p_t = 2p_0$ (C2, Section 17.5), and, for the linear history $a_4 = AHx_4 + a_0$, equal pressures and a constant energy density (C3, Section 17.6).''',
     r'''- The three **source conditions**: no dependence on the hidden coordinate $x_0$ (C1, Section 17.4), the algebraic condition $p_3 + p_t = 2p_0$ (C2, Section 17.5), and, for the linear history $a_4 = AHx_4 + a_0$, equal pressures and a constant energy density (C3, Section 17.6). They are derived on the background $b_4 = 1$ of the author's metric of 2026-10-14, on which the Kohn-Sham states are computed; the record states that the verdict holds for every second function $b_4(x_4)$: C1 holds unchanged, so the $x_0$-dependent Kohn-Sham profiles are not an admissible source for any $b_4$ (`Revision/field_equations_a4/reports/ks-source-conditions.json`, check `ks_verdict_holds_for_every_b4`; Section 12.12 gives the field equations with $b_4$).'''),
    (r'''and reproduces every number of the five checks of `Revision/field_equations_a4/reports/ks-source-conditions.json`.''',
     r'''and reproduces every number of the five checks on the Kohn-Sham states of `Revision/field_equations_a4/reports/ks-source-conditions.json` (its sixth check, `ks_verdict_holds_for_every_b4`, is about the metric with $b_4$).'''),
    (r'''The cell prints the count and the record's conclusion, and checks that the record has 5 checks, all PASS. Output: RESULT checks of the record ks-source-conditions.json = 5 of 5 PASS,''',
     r'''The cell prints the count and the record's conclusion, and checks that the record has 6 checks, all PASS. Output: RESULT checks of the record ks-source-conditions.json = 6 of 6 PASS,'''),
]
s = strict_replace(s, pairs, "ch17")
n = s.count("95d8cbdd0682fd30")
s = s.replace("95d8cbdd0682fd30", "c99277bab4793c42")
p.write_bytes(s.encode("utf-8"))
print("ok, fingerprint replaced", n)
