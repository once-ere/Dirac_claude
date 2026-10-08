"""The execution-provenance index `provenance/EXECUTION_PROVENANCE_INDEX.md` is complete and current.

Run from the repository root (`python3` instead of `python` on macOS and Linux outside a virtual environment):
    python -m unittest discover -s tests -p "test_execution_provenance.py" -v
Checks, without running any Wolfram code:
  * every WolframScript file (.wls) and every Jupyter notebook (.ipynb) tracked by git, outside vendor/,
    dirac-main/, build/ and the textbook notebooks, is listed in the index;
  * every provenance file named in the index exists and is tracked by git;
  * every provenance file names the CURRENT sha256 of each script of its row (a script that changed without a
    new verification record fails here);
  * every textbook notebook Revision/textbook/notebooks/<name>.ipynb has its builder src/<name>.py and its
    provenance file <name>.PROVENANCE.md.
With EXECUTION_PROVENANCE_FULL=1 (and wolframscript on the PATH) it also re-runs the sets marked "(fast)" in the
index, in the working tree, and checks that each ends with exit code 0 and leaves every tracked file byte for byte
unchanged (the old-algebra set only when the private folder dirac-main/ is present, as its provenance file says).
Writes nothing in the repository except the scratch folder build/execution-provenance-test/ (ignored by git); the
test runner itself may write tests/__pycache__/ unless PYTHONDONTWRITEBYTECODE=1.
"""

import hashlib
import os
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "provenance" / "EXECUTION_PROVENANCE_INDEX.md"
EXCLUDED = re.compile(r"^(vendor|dirac-main|build)/|/target/|^Revision/textbook/notebooks/")
SCRATCH = "build/execution-provenance-test"


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def index_rows():
    """The rows of the index tables: (number, set, [scripts], provenance file)."""
    rows = []
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (\d+) \| ([^|]+) \| ([^|]+) \| `([^`]+)` \|", line)
        if m:
            scripts = re.findall(r"`([^`]+)`", m.group(3))
            rows.append((int(m.group(1)), m.group(2).strip(), scripts, m.group(4)))
    return rows


def sha256(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


class ExecutionProvenanceIndex(unittest.TestCase):
    def test_rows_are_numbered_and_unique(self):
        rows = index_rows()
        self.assertGreaterEqual(len(rows), 23)
        self.assertEqual([r[0] for r in rows], list(range(1, len(rows) + 1)))
        scripts = [s for r in rows for s in r[2]]
        self.assertEqual(len(scripts), len(set(scripts)), "a script is listed twice")

    def test_every_script_and_notebook_is_listed(self):
        listed = {s for r in index_rows() for s in r[2]}
        wanted = [p for p in tracked_files() if p.endswith((".wls", ".ipynb")) and not EXCLUDED.search(p)]
        self.assertTrue(wanted)
        missing = [p for p in wanted if p not in listed]
        self.assertEqual(missing, [], "tracked scripts or notebooks missing from the index")

    def test_every_listed_file_exists_and_is_tracked(self):
        tracked = set(tracked_files())
        for _, name, scripts, prov in index_rows():
            for rel in scripts + [prov]:
                self.assertIn(rel, tracked, f"{name}: {rel} is not a tracked file")

    def test_each_provenance_file_names_the_current_sha256_of_its_scripts(self):
        stale = []
        for _, name, scripts, prov in index_rows():
            text = (ROOT / prov).read_text(encoding="utf-8")
            for rel in scripts:
                if sha256(rel) not in text:
                    stale.append(f"{name}: {prov} does not name the current sha256 {sha256(rel)} of {rel}")
        self.assertEqual(stale, [], "scripts changed without a new verification record")

    def test_textbook_notebooks_have_builder_and_provenance(self):
        tracked = set(tracked_files())
        nbs = [p for p in tracked if re.match(r"^Revision/textbook/notebooks/[^/]+\.ipynb$", p)]
        self.assertGreaterEqual(len(nbs), 89)
        for nb in nbs:
            name = Path(nb).stem
            self.assertIn(f"Revision/textbook/notebooks/src/{name}.py", tracked, nb)
            self.assertIn(f"Revision/textbook/notebooks/{name}.PROVENANCE.md", tracked, nb)


def git_state():
    """The sha256 of the full binary diff of the tracked files against HEAD (an empty diff for a clean tree): equal
    before and after a run exactly when the run left every tracked file byte for byte as it was."""
    diff = subprocess.run(["git", "diff", "HEAD", "--binary"], cwd=ROOT, capture_output=True, check=True).stdout
    return hashlib.sha256(diff).hexdigest()


@unittest.skipUnless(os.environ.get("EXECUTION_PROVENANCE_FULL") == "1", "set EXECUTION_PROVENANCE_FULL=1 to re-run")
@unittest.skipUnless(shutil.which("wolframscript"), "wolframscript is not on the PATH")
class FastSetsReproduce(unittest.TestCase):
    def run_and_compare(self, commands, compare=()):
        before = git_state()
        for cmd in commands:
            r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=600)
            self.assertEqual(r.returncode, 0, f"{' '.join(cmd)}\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}")
        self.assertEqual(git_state(), before, "a run changed a tracked file")
        for built, committed in compare:
            self.assertEqual((ROOT / built).read_bytes(), (ROOT / committed).read_bytes(), f"{built} != {committed}")

    def test_rev_algebra(self):
        self.run_and_compare([["wolframscript", "-file", "Revision/algebra/wolfram/verify_algebra.wls"]])

    def test_rev_pairing_ks(self):
        self.run_and_compare([["wolframscript", "-file", "Revision/pairing/kohn_sham/wolfram/verify_t3.wls"]])

    @unittest.skipUnless((ROOT / "dirac-main").is_dir(), "the private folder dirac-main/ is not present")
    def test_old_algebra(self):
        self.run_and_compare([["wolframscript", "-file", "scripts/verify_dirac16complex_algebra.wls",
                               "artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json"]])

    def test_old_notebook_builders(self):
        dark, ks = f"{SCRATCH}/Dirac16ComplexDarkSector.nb", f"{SCRATCH}/Dirac16ComplexKohnSham.nb"
        self.run_and_compare([["wolframscript", "-file", "scripts/build_dirac16complex_mathematica_notebook.wls", dark],
                              ["wolframscript", "-file", "scripts/build_dirac16complex_ks_mathematica_notebook.wls", ks]],
                             [(dark, "notebooks/Dirac16ComplexDarkSector.nb"), (ks, "notebooks/Dirac16ComplexKohnSham.nb")])

    def test_handoff_probes(self):
        self.run_and_compare([["wolframscript", "-file", "handoff/tools/probe1.wls"],
                              ["wolframscript", "-file", "handoff/tools/probe2.wls"]])

    def test_dirac_matrices(self):
        self.run_and_compare([["wolframscript", "-file", "provenance/dirac_matrices/extract_from_author_notebook.wls"],
                              ["wolframscript", "-file", "provenance/dirac_matrices/extract_repository_wolfram_gammas.wls"],
                              [sys.executable, "-B", "provenance/dirac_matrices/build_dirac_matrices_md.py", "--check"]])


if __name__ == "__main__":
    unittest.main()
