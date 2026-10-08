"""The provenance file `provenance/dirac matrices.md` is correct and up to date.

Run from the repository root (`python3` instead of `python` on macOS and Linux outside a virtual environment):
    python -m unittest discover -s tests -p "test_dirac_matrices_provenance.py" -v
Runs provenance/dirac_matrices/build_dirac_matrices_md.py --check (every exact check on the author's eight real
16 x 16 Dirac matrices and on every gamma source of the repository, then a byte-for-byte comparison with the
committed Markdown), checks that the comparison is byte-exact, that wrong matrices give FAIL lines and no
traceback (on a corrupted copy of the extracted JSON in a temporary folder), and that the survey of the files
that name a gamma source is printed only.  Writes nothing in the repository (the test runner itself may write
tests/__pycache__/ unless PYTHONDONTWRITEBYTECODE=1).
"""

import contextlib
import importlib.util
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "provenance" / "dirac_matrices" / "build_dirac_matrices_md.py"
MD = ROOT / "provenance" / "dirac matrices.md"
# The number of checks when this test was written.  Checks may be added (for example the a4 engine's comparison
# basis once the engine uses the author's T16), never silently dropped: the committed file must list at least these.
MIN_CHECKS = 66
# 8 Dirac matrices + sigma16 and T16A[8] + 28 pairwise products + the 256-product listing
# + 7 projection blocks (P_L, P_R, Q_+, Q_-, Im B, Im Pi_+, Im Pi_-)
N_TEXT_BLOCKS = 8 + 2 + 28 + 1 + 7


def n_checks_in_file():
    """The number of rows of the proofs table of the committed file."""
    text = MD.read_text(encoding="utf-8")
    proofs = text.split("## The proofs (every check, exact)", 1)[1].split("\n### ", 1)[0]
    return len(re.findall(r"^\| \d+ \| `", proofs, flags=re.M))


def load_builder():
    """A fresh copy of the builder module (its own check registry); importing it runs nothing and writes no
    bytecode cache into provenance/dirac_matrices/."""
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("build_dirac_matrices_md_under_test", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_main(module, *args):
    """module.main() with the given arguments; returns (exit code, printed text)."""
    out, argv = io.StringIO(), sys.argv
    sys.argv = [str(BUILDER), *args]
    try:
        with contextlib.redirect_stdout(out):
            code = module.main()
    finally:
        sys.argv = argv
    return code, out.getvalue()


class DiracMatricesProvenance(unittest.TestCase):
    def test_all_checks_pass_and_file_up_to_date(self):
        run = subprocess.run([sys.executable, str(BUILDER), "--check"], cwd=ROOT,
                             capture_output=True, text=True, timeout=900)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        n = n_checks_in_file()
        self.assertGreaterEqual(n, MIN_CHECKS)
        self.assertIn(f"{n} of {n} checks pass", run.stdout)
        self.assertIn("is up to date", run.stdout)
        self.assertNotIn("FAIL", run.stdout)

    def test_check_compares_bytes(self):
        builder = load_builder()
        text = MD.read_bytes().decode("utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "copy.md"
            copy.write_bytes(text.encode("utf-8"))
            self.assertTrue(builder.same_bytes(copy, text))
            copy.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
            self.assertFalse(builder.same_bytes(copy, text), "CRLF line endings must make --check fail")
            self.assertFalse(builder.same_bytes(Path(tmp) / "missing.md", text))

    def test_wrong_matrices_give_fail_lines_and_no_traceback(self):
        builder = load_builder()
        data = json.loads(builder.NB_JSON.read_text(encoding="utf-8"))
        row = data["T16A"][1][0]
        j = next(k for k, x in enumerate(row) if x)
        row[j] = 2  # Gamma_1 is then neither Clifford nor a signed permutation
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "author_notebook_T16.json"
            bad.write_text(json.dumps(data), encoding="utf-8")
            builder.NB_JSON = bad
            builder.OUT = Path(tmp) / "never written.md"
            code, text = run_main(builder)
            self.assertFalse(builder.OUT.exists())
        self.assertEqual(code, 1, text)
        self.assertIn("FAIL clifford_anticommutation:", text)
        self.assertIn("FAIL real_integer_entries:", text)
        self.assertIn("checks FAILED", text)
        self.assertNotIn("Traceback", text)
        # the later groups still ran and reported
        self.assertIn("FAIL fixture_Revision_algebra_gammas_json", text)

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
        run = subprocess.run([sys.executable, str(BUILDER), "--survey"], cwd=ROOT,
                             capture_output=True, text=True, timeout=300)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("files that mention gammas.json (", run.stdout)
        self.assertIn("Printed only", run.stdout)

    def test_scaled_commutators_claim_is_not_overstated(self):
        text = MD.read_text(encoding="utf-8")
        self.assertIn("generate exactly the identity component Spin_0(4,4), not all of Pin(4,4)", text)
        self.assertNotIn("(A < B): the scaled commutators", text)

    def test_answer_states_the_measured_truth_about_the_a4_engine(self):
        text = MD.read_text(encoding="utf-8")
        answer = text.split("## Answer in one paragraph", 1)[1].split("## How to reproduce", 1)[0]
        followed = "**Instruction followed: yes.**" in answer
        partly = "**Instruction followed: not completely.**" in answer
        self.assertTrue(followed != partly, "exactly one verdict")
        self.assertIn("FieldEquationsA4.wl", answer)
        if partly:
            self.assertIn("NOT the author's T16", answer)
            self.assertIn("Revision/SPEC.md section 2", answer)


if __name__ == "__main__":
    unittest.main()
