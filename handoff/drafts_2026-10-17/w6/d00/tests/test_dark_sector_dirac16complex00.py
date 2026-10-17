"""Tests of Revision/dark_sector/dirac16complex00: both implementations re-run into a temporary
directory reproduce the committed outputs byte for byte, every check passes, and the key numbers
stated in the README are the ones in the outputs.

Run from the repository root:
    python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
(about 12 s: implementation A about 4 s, implementation B about 8 s; the corrected primordial metric of 2026-10-16,
version 2, on the history a4 = H x4, b4 = e^((4/3) H x4))
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
OWN = os.path.normpath(os.path.join(HERE, ".."))
OUTPUTS = [
    "eos-theory.json",
    os.path.join("reports", "python-derive-eos.json"),
    os.path.join("results", "independent-numerics.json"),
    os.path.join("reports", "python-independent-numerics.json"),
]


def load(rel):
    with open(os.path.join(OWN, rel), encoding="utf-8") as fh:
        return json.load(fh)


class TestDarkSectorDirac16complex00(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        for script in ("derive_eos.py", "independent_numerics.py"):
            r = subprocess.run([sys.executable, os.path.join(OWN, "python", script), "--out", cls.tmp.name],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise AssertionError("%s failed: %s %s" % (script, r.stdout, r.stderr))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_reproduced_byte_for_byte(self):
        for rel in OUTPUTS:
            with open(os.path.join(OWN, rel), "rb") as a, open(os.path.join(self.tmp.name, rel), "rb") as b:
                self.assertEqual(a.read(), b.read(), rel)

    def test_every_check_passes(self):
        for rel in ("reports/python-derive-eos.json", "reports/python-independent-numerics.json"):
            rep = load(rel)
            self.assertTrue(rep["checks"], rel)
            for c in rep["checks"]:
                self.assertEqual(c["verdict"], "PASS", "%s: %s" % (rel, c["name"]))
            n = len(rep["checks"])
            self.assertEqual(rep["summary"], "%d/%d checks pass" % (n, n))

    def test_key_numbers(self):
        m = load("eos-theory.json")["models"]
        self.assertEqual(m["unite"]["crossing_of_minus_1"]["a"], "461/600")
        self.assertEqual(m["M2_positive_good_sector_gas"]["N2_tangent_exact"], {"w0": "-2749/9000", "wa": "81037/500000"})
        self.assertEqual(m["M3_positive_extra_time_mode"]["N2_tangent_exact"]["w0"], "-3583/9000")
        self.assertEqual(m["M3_positive_extra_time_mode"]["N2_tangent_exact"]["wa"], "-196963/4500000")
        m4 = m["M4_condensate_plus_extra_time_mode"]
        self.assertEqual(m4["parameters"]["s"], "264037/403037")
        self.assertEqual(m4["parameters"]["Omega_q"], "57963/264037")
        self.assertEqual(m4["N2"]["CPL_tangent"], {"w0": "-0.398111111111", "wa": "-0.0666666666667", "w0_plus_wa": "-0.464777777778"})
        self.assertEqual(m4["N2"]["crossings_of_minus_1_in_[1/3,1]"], [])
        m5 = m["M5_with_ghost_component"]
        self.assertEqual(m5["N2"]["fit_a_1/2_to_1"]["w0"], "-0.443790594178")
        self.assertEqual(m5["N2"]["fit_a_1/2_to_1"]["wa"], "-0.32308292878")
        self.assertEqual(m5["N2"]["crossings_of_minus_1_in_[1/3,1]"], [])
        b = load("results/independent-numerics.json")
        self.assertEqual(b["models"]["M5_with_ghost_component"]["crossings_N2"], 0)
        src = load("eos-theory.json")["condensate"]["historyRequiredSource"]
        self.assertEqual((src["minus_rho"], src["p3"], src["pt"], src["p0"]),
                         ("-9*kk**2/16 + 161*kk/24 + 121/432", "-9*kk**2/16 + 1601*kk/216 - 5359/3888",
                          "79*kk/16 - 497/144", "79*kk/16 - 497/144"))
        self.assertEqual(load("eos-theory.json")["beta"], "d ln b4/d a4 = 4/3")

    def test_readme_cites_the_numbers(self):
        with open(os.path.join(OWN, "README.md"), encoding="utf-8") as fh:
            text = fh.read()
        for s in ("461/600", "264037/403037", "57963/264037", "-382/441", "0.162074", "-0.0437696", "3749/3000", "-4/9",
                  "corrected", "b4"):
            self.assertIn(s, text, s)


if __name__ == "__main__":
    unittest.main()
