"""Chapter 12: the order x0..x7 in 12.3, the names e00 and p0, code descriptions, and the
pointer to the b4 paragraph of Section 12.12."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/12-field-equations-a4.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''g = \mathrm{diag}\big(e^{2a_4}s,\ e^{2a_4}s,\ e^{2a_4}s,\ -1,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ \cot^2 z\big),''',
     r'''g = \mathrm{diag}\big(\cot^2 z,\ e^{2a_4}s,\ e^{2a_4}s,\ e^{2a_4}s,\ -1,\ -e^{-2a_4}s,\ -e^{-2a_4}s,\ -e^{-2a_4}s\big),'''),
    (r'''in the order $x_0, \dots, x_7$ (record check `metric_is_SPEC_section_1` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`).''',
     r'''in the order $x_0, \dots, x_7$, on the background $b_4 = 1$ of the author's metric of 2026-10-14 (record check `metric_is_SPEC_section_1` of `Revision/field_equations_a4/reports/wolfram-a4-report.json`, which states the metric with $b_4$; Section 12.12 says what a changing $b_4$ changes).'''),
    (r'''`algebraic_identity_x1_plus_x5_minus_2x8`''', r'''`algebraic_identity_x1_plus_x5_minus_2x0`'''),
    (r'''**In [5], the term 3H gamma8.**''', r'''**In [5], the term 3H gamma^(x0).**'''),
]
s = strict_replace(s, pairs, "ch12")
s = re.sub(r"e_\{88\}", "e_{00}", s)
s = re.sub(r"(?<![A-Za-z0-9_])e88(?![A-Za-z0-9_])", "e00", s)
s = re.sub(r"p_8(?![0-9])", "p_0", s)
s = re.sub(r"(?<![A-Za-z0-9_])kappa_p8(?![A-Za-z0-9_])", "kappa_p0", s)
p.write_bytes(s.encode("utf-8"))
print("ok", s.count("e_{00}"), s.count("p_8"))
