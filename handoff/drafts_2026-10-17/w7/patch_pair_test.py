"""Update Revision/tests/test_pair_creation_proofs_publication.py for the corrected metric (version 2): key statements
(the fold, no Z2 orbifold), corollary C1 (the vacuum statements of the corrected metric), the solver self-test
numbers of the corrected record.  The demonstration numbers and the Kohn-Sham source numbers are patched after the
records are regenerated (patch_pair_test_numbers.py)."""
from pathlib import Path

p = Path(r"D:\Developer\github\Dirac_claude\Revision\tests\test_pair_creation_proofs_publication.py")
t = p.read_text(encoding="utf-8")


def rep(a, b):
    global t
    assert t.count(a) == 1, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''    "with the ASSUMED Z2 mirror construction",
''', '''    "the corrected metric has no Z2 orbifold",
    "both fold conditions filled, ASSUMED",
''')
rep('''    "the ASSUMED Z2 construction of `Revision/SPEC.md` section 7",
''', '''    "no junction condition or matching of the field across the fold is derived",
''')
rep('''    "a T1 pair cannot by itself be the source of the author's metric in Einstein gravity",
''', '''    "a T1 pair cannot by itself be the source of any exponential history in Einstein gravity or with the author's weights",
''')
rep('''    "T3 and its statements S1 to S5 are unchanged.",
''', '''    "T3 and its statements S1 to S4 are unchanged.",
''')
i0 = t.index("    def test_a4_vacuum_polynomial(self):")
i1 = t.index("    def test_kohn_sham_self_test_numbers(self):")
t = t[:i0] + '''    def test_a4_vacuum_statements(self):
        """Corollary C1 for the corrected metric: the vacuum statements of the a4 and b4 equations."""
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("a4 = 0, b4 = H^2 (x4 - c)^2", check_detail(path, "einstein_flat_vacuum"), path.name)
            self.assertIn("Lambda = 0", check_detail(path, "einstein_flat_vacuum"), path.name)
        self.assertIn("is a vacuum solution, for any A, beta, Lambda", check_detail(A4_WOLFRAM, "einstein_no_exponential_vacuum"))
        self.assertIn("no solution with k > 0 for any Lambda", check_detail(A4_PYTHON, "einstein_no_exponential_vacuum"))
        self.assertIn(r"the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves the vacuum equations with $\\Lambda = 0$, "
                      r"while no exponential history", self.text)
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("no exponential history is a vacuum solution",
                          check_detail(path, "author_weights_no_exponential_vacuum"), path.name)
        self.assertIn(r"no exponential history is a vacuum solution. (c)", self.text)
        for path in (A4_WOLFRAM, A4_PYTHON):
            self.assertIn("alpha2 = -1/(4 H^2 (A^2 - k", check_detail(path, "egb_exponential_vacuum_branches"), path.name)
        self.assertIn("no vacuum exponential history where k varies", check_detail(A4_WOLFRAM, "egb_exponential_vacuum_branches"))
        self.assertIn(r"the tuned coupling $\\alpha_2 = -1/(4H^2(A^2 - k_0))$", self.text)
        self.assertIn("w = (1, 1/32, 1/1152)", check_detail(A4_WOLFRAM, "author_weights_history_source"))

''' + t[i1:]
rep('''        for number in ("8.35e-14", "1e-9", "0.01946", "-1.341747939926e-4", "-1.341747939933e-4",
                       "80 levels", "-1.6232217540e0", "0.01206", "3.239983783344e1",
                       "160 levels", "2.9056626386e1"):''',
    '''        for number in ("3.62e-13", "1e-9", "157.7", "-1.457144423225e-2", "140 levels", "-1.7604533053e0",
                       "2.131", "1.317651779781e2", "324 levels", "-8.1980434559e-1"):''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
