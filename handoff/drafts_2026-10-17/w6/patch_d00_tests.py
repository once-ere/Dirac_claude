"""W6 draft: Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py for the corrected metric
(applied to the copy argv[1]): the key numbers of the draft implementation A (scratchpad/w6/d00/eos-theory.json, 48/48)
and the README citations (the README itself is rewritten in W6; the list of cited numbers is completed then)."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''(about 10 s: implementation A about 4 s, implementation B about 7 s; the metric with b4(x4), the history
b4 ~ a^(4/3) of the author's weights)''',
    '''(about 12 s: implementation A about 4 s, implementation B about 8 s; the corrected primordial metric of 2026-10-16,
version 2, on the history a4 = H x4, b4 = e^((4/3) H x4))''')
rep('''        self.assertEqual(m["M2_positive_good_sector_gas"]["N2_tangent_exact"], {"w0": "-583/3000", "wa": "81037/500000"})
        self.assertEqual(m["M3_positive_extra_time_mode"]["N2_tangent_exact"]["w0"], "-287/1000")''',
    '''        self.assertEqual(m["M2_positive_good_sector_gas"]["N2_tangent_exact"], {"w0": "-2749/9000", "wa": "81037/500000"})
        self.assertEqual(m["M3_positive_extra_time_mode"]["N2_tangent_exact"]["w0"], "-3583/9000")''')
rep('''        self.assertEqual(m4["N2"]["CPL_tangent"], {"w0": "-0.287", "wa": "-0.0666666666667", "w0_plus_wa": "-0.353666666667"})''',
    '''        self.assertEqual(m4["N2"]["CPL_tangent"], {"w0": "-0.398111111111", "wa": "-0.0666666666667", "w0_plus_wa": "-0.464777777778"})''')
rep('''        self.assertEqual(m5["N2"]["fit_a_1/2_to_1"]["w0"], "-0.332679483067")''',
    '''        self.assertEqual(m5["N2"]["fit_a_1/2_to_1"]["w0"], "-0.443790594178")''')
rep('''        src = load("eos-theory.json")["condensate"]["branchRequiredSource"]
        self.assertEqual((src["kappa_rho"], src["kappa_p3"], src["kappa_pt"], src["kappa_p0"]), ("-2/27", "-2/9", "-22/27", "-14/27"))''',
    '''        src = load("eos-theory.json")["condensate"]["historyRequiredSource"]
        self.assertEqual((src["minus_rho"], src["p3"], src["pt"], src["p0"]),
                         ("-9*kk**2/16 + 161*kk/24 + 121/432", "-9*kk**2/16 + 1601*kk/216 - 5359/3888",
                          "79*kk/16 - 497/144", "79*kk/16 - 497/144"))''')
rep('''        for s in ("461/600", "264037/403037", "57963/264037", "-382/441", "0.162074", "-0.0437696", "-2/27", "1583/1000",
                  "6.264", "b4"):''',
    '''        for s in ("461/600", "264037/403037", "57963/264037", "-382/441", "0.162074", "-0.0437696", "3749/3000", "-4/9",
                  "corrected", "b4"):''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
