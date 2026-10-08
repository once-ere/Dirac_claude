"""The provenance file `provenance/dirac matrices.md` is correct and up to date.

Run from the repository root:
    python -m unittest discover -s tests -p "test_dirac_matrices_provenance.py" -v
Runs provenance/dirac_matrices/build_dirac_matrices_md.py --check (every exact check on the author's
eight real 16 x 16 Dirac matrices and on every other copy of them in the repository, then a comparison
with the committed Markdown); writes nothing.
"""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "provenance" / "dirac_matrices" / "build_dirac_matrices_md.py"
MD = ROOT / "provenance" / "dirac matrices.md"
N_CHECKS = 58
# 8 Dirac matrices + sigma16 and T16A[8] + 28 pairwise products + the 256-product listing
# + 7 projection blocks (P_L, P_R, Q_+, Q_-, Im B, Im Pi_+, Im Pi_-)
N_TEXT_BLOCKS = 8 + 2 + 28 + 1 + 7


class DiracMatricesProvenance(unittest.TestCase):
    def test_all_checks_pass_and_file_up_to_date(self):
        run = subprocess.run([sys.executable, str(BUILDER), "--check"], cwd=ROOT,
                             capture_output=True, text=True, timeout=900)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn(f"{N_CHECKS} of {N_CHECKS} checks pass", run.stdout)
        self.assertIn("is up to date", run.stdout)

    def test_matrices_come_from_the_author_notebook_in_the_authors_order(self):
        text = MD.read_text(encoding="utf-8")
        rows = ("| 257 | In[338] | `tau[0..7]` |",
                "| 285 | In[370] | `sigma16 = T16A[0].T16A[1].T16A[2].T16A[3] (T16A not yet defined)` |",
                "| 286 | In[371] | `T16A[0..7] = {{0, taubar}, {tau, 0}}` |")
        for row in rows:
            self.assertIn(row, text)
        self.assertLess(text.index(rows[1]), text.index(rows[2]))
        self.assertEqual(text.count("```text"), N_TEXT_BLOCKS)

    def test_document_does_not_depend_on_a_directory_listing(self):
        text = MD.read_text(encoding="utf-8")
        self.assertNotIn("Files that read `gammas.json` (", text)
        run = subprocess.run([sys.executable, str(BUILDER), "--list-consumers"], cwd=ROOT,
                             capture_output=True, text=True, timeout=300)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("mention gammas.json", run.stdout)

    def test_scaled_commutators_claim_is_not_overstated(self):
        text = MD.read_text(encoding="utf-8")
        self.assertIn("generate exactly the identity component Spin_0(4,4), not all of Pin(4,4)", text)
        self.assertNotIn("(A < B): the scaled commutators", text)


if __name__ == "__main__":
    unittest.main()
