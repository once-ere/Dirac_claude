"""The provenance file `provenance/dirac matrices.md` is correct and up to date.

Run from the repository root:
    python -m unittest discover -s tests -p "test_dirac_matrices_provenance.py" -v
Runs provenance/dirac_matrices/build_dirac_matrices_md.py --check (every exact check on the author's
eight real 16 x 16 Dirac matrices, then a comparison with the committed Markdown); writes nothing.
"""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "provenance" / "dirac_matrices" / "build_dirac_matrices_md.py"


class DiracMatricesProvenance(unittest.TestCase):
    def test_all_checks_pass_and_file_up_to_date(self):
        run = subprocess.run([sys.executable, str(BUILDER), "--check"], cwd=ROOT,
                             capture_output=True, text=True, timeout=900)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("35 of 35 checks pass", run.stdout)
        self.assertIn("is up to date", run.stdout)

    def test_matrices_come_from_the_author_notebook(self):
        text = (ROOT / "provenance" / "dirac matrices.md").read_text(encoding="utf-8")
        for cell in ("| 257 | `tau[0..7]` |", "| 286 | `T16A[0..7] = {{0, taubar}, {tau, 0}}` |"):
            self.assertIn(cell, text)
        self.assertEqual(text.count("```text"), 8 + 2 + 28 + 1 + 2)


if __name__ == "__main__":
    unittest.main()
