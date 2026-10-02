"""The lead's independent checks (Revision/lead_checks) pass and reproduce their committed report byte for byte."""
import os
import subprocess
import sys
import unittest

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SCRIPT = os.path.join(ROOT, 'Revision', 'lead_checks', 'emt_divergence_and_spin_connection.py')
REPORT = os.path.join(ROOT, 'Revision', 'lead_checks', 'reports', 'emt-divergence-and-spin-connection.json')


class LeadChecksTest(unittest.TestCase):
    def test_all_checks_pass_and_reproduce(self):
        with open(REPORT, 'rb') as f:
            committed = f.read()
        r = subprocess.run([sys.executable, SCRIPT], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('"passed": 10, "total": 10', r.stdout)
        with open(REPORT, 'rb') as f:
            self.assertEqual(f.read(), committed)


if __name__ == '__main__':
    unittest.main()
