"""The lead's independent checks (Revision/lead_checks) pass and reproduce their committed report byte for byte."""
import os
import subprocess
import sys
import unittest

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
LC = os.path.join(ROOT, 'Revision', 'lead_checks')
CASES = [
    ('emt_divergence_and_spin_connection.py', 'emt-divergence-and-spin-connection.json', 10),
    ('einstein_gauss_bonnet_a4.py', 'einstein-gauss-bonnet-a4.json', 15),
    ('charge_conjugation_and_u1.py', 'charge-conjugation-and-u1.json', 12),
]


class LeadChecksTest(unittest.TestCase):
    def test_all_checks_pass_and_reproduce(self):
        for script, report, n in CASES:
            with self.subTest(script=script):
                path = os.path.join(LC, 'reports', report)
                with open(path, 'rb') as f:
                    committed = f.read()
                r = subprocess.run([sys.executable, os.path.join(LC, script)], cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
                self.assertIn('"passed": %d, "total": %d' % (n, n), r.stdout)
                with open(path, 'rb') as f:
                    self.assertEqual(f.read(), committed)


if __name__ == '__main__':
    unittest.main()
