#!/usr/bin/env python3
"""Tests for the Revision notebooks (Revision/notebooks/).

Run from the repository root:
    python -m unittest Revision/tests/test_revision_notebooks.py -v
    REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py -v
    (PowerShell: $env:REVISION_NOTEBOOKS_FULL = "1"; python -m unittest Revision/tests/test_revision_notebooks.py -v)

What is tested
  * ALWAYS (static, no execution, about a second):
      - every builder Revision/notebooks/src/<name>.py loads and defines NAME, TITLE and cells();
      - the committed notebook Revision/notebooks/<name>.ipynb exists and passes the structure
        audit of Revision/notebooks/tools/build_notebooks.py (normalised form, LF only, required
        sections, complete run instructions without `-m jupyter`, a markdown lead-in before every
        code cell, every code cell executed without error or stderr, no machine-specific path);
      - the committed notebook's cells are exactly the builder's cells (kind and source);
      - its provenance file Revision/notebooks/<name>.PROVENANCE.md exists and records the current
        sha256 of the notebook, of its builder and of the build tool;
      - Revision/notebooks/README.md lists the notebook; requirements.txt pins exactly the
        packages named in the notebook's run instructions;
      - lovelock_gkd: the executed notebook printed the check counts of the committed Revision
        reports exactly as their JSON files give them, and no FAIL line;
      - kohn_sham_states: the same for the seven Kohn-Sham reports, the ten states equal to the
        committed record and the 84 reproduced rows of the cross-check table;
      - dark_sector_hypotheses: the same for the six dark-sector reports, the 123 rows of the dense
        history and of the equation-of-state history reproduced character for character, the three
        series entries of eos-summary.json, the mixtures, and the exact (Fraction) dirac16complex00
        tangents and M5 crossing.
  * FULL (only when REVISION_NOTEBOOKS_FULL=1; about a minute per notebook; needs cargo and the
    pinned packages): the installed package versions equal the pins, and
    `build_notebooks.py check <name>` re-executes every notebook in a fresh temporary folder
    (under $REVISION_SCRATCH when that is set) and must reproduce the committed notebook byte for
    byte.  Nothing in the repository is written.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NB_DIR = REPO / "Revision" / "notebooks"
TOOL_PATH = NB_DIR / "tools" / "build_notebooks.py"
RECORD = REPO / "Revision" / "gkd_lovelock" / "results"
KS_REPORTS = REPO / "Revision" / "kohn_sham" / "reports"
DARK = REPO / "Revision" / "dark_sector"
FULL = os.environ.get("REVISION_NOTEBOOKS_FULL") == "1"


def load_tool():
    spec = importlib.util.spec_from_file_location("revision_build_notebooks", TOOL_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


TOOL = load_tool()
NAMES = TOOL.builder_names()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def notebook(name: str) -> dict:
    return json.loads((NB_DIR / f"{name}.ipynb").read_text(encoding="utf-8"))


def all_output_text(nb: dict) -> str:
    parts = []
    for cell in nb["cells"]:
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                parts.append("".join(out["text"]))
    return "".join(parts)


class StaticTests(unittest.TestCase):
    def test_builders_exist(self):
        self.assertIn("lovelock_gkd", NAMES)
        self.assertIn("kohn_sham_states", NAMES)
        self.assertIn("dark_sector_hypotheses", NAMES)
        for name in NAMES:
            module = TOOL.load_builder(name)
            self.assertEqual(module.NAME, name)
            self.assertTrue(module.TITLE)
            cells = module.cells()
            self.assertTrue(cells)
            self.assertTrue(all(kind in ("markdown", "code") for kind, _ in cells))

    def test_audit_passes(self):
        for name in NAMES:
            with self.subTest(name=name):
                self.assertEqual(TOOL.audit(name), [])

    def test_audit_detects_problems(self):
        """Negative controls: the audit must reject a CR, `-m jupyter` and an unexecuted cell."""
        name = "lovelock_gkd"
        text = (NB_DIR / f"{name}.ipynb").read_text(encoding="utf-8")
        self.assertTrue(TOOL.audit_text(text.replace("\n", "\r\n", 1), name))
        nb = json.loads(text)
        md = next(c for c in nb["cells"] if c["cell_type"] == "markdown")
        md["source"].append("\npython -m jupyter lab\n")
        bad = TOOL.normalise(nb, name, nb["metadata"]["revision"]["title"])
        self.assertTrue(any(p.startswith("A3: forbidden") for p in TOOL.audit_text(bad, name)))
        nb = json.loads(text)
        next(c for c in nb["cells"] if c["cell_type"] == "code")["execution_count"] = None
        bad = TOOL.normalise(nb, name, nb["metadata"]["revision"]["title"])
        self.assertTrue(any(p.startswith("A6") for p in TOOL.audit_text(bad, name)))

    def test_cells_equal_builder(self):
        for name in NAMES:
            with self.subTest(name=name):
                built = [(k, t.strip("\n")) for k, t in TOOL.load_builder(name).cells()]
                committed = [(c["cell_type"], "".join(c["source"])) for c in notebook(name)["cells"]]
                self.assertEqual(committed, built)

    def test_provenance_records_current_digests(self):
        for name in NAMES:
            with self.subTest(name=name):
                prov = NB_DIR / f"{name}.PROVENANCE.md"
                self.assertTrue(prov.is_file(), prov)
                text = prov.read_text(encoding="utf-8")
                self.assertNotIn("\r", text)
                for path in (NB_DIR / f"{name}.ipynb", NB_DIR / "src" / f"{name}.py", TOOL_PATH):
                    self.assertIn(sha256(path), text, f"{path.name}: sha256 not recorded in {prov.name}")

    def test_readme_and_requirements(self):
        readme = (NB_DIR / "README.md").read_text(encoding="utf-8")
        reqs = [line.strip() for line in (NB_DIR / "requirements.txt").read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.startswith("#")]
        pins = dict(line.split("==") for line in reqs)
        self.assertEqual(set(pins), {"numpy", "matplotlib", "jupyterlab", "nbformat", "nbclient", "ipykernel", "nbconvert"})
        for name in NAMES:
            self.assertIn(f"{name}.ipynb", readme)
            md = "".join("".join(c["source"]) for c in notebook(name)["cells"] if c["cell_type"] == "markdown")
            for package, version in pins.items():
                self.assertIn(f"{package} {version}", md, f"{name}: the run instructions do not name {package} {version}")

    def test_lovelock_record_counts_printed(self):
        out = all_output_text(notebook("lovelock_gkd"))
        self.assertNotIn("FAIL", out)
        rust = json.loads((RECORD / "lovelock-report.json").read_text(encoding="utf-8"))
        python = json.loads((RECORD / "python-lovelock-report.json").read_text(encoding="utf-8"))
        wolfram = json.loads((RECORD / "wolfram-gkd-report.json").read_text(encoding="utf-8"))
        self.assertEqual((rust["checkCount"], python["checkCount"], wolfram["checkCount"]), (19, 49, 29))
        self.assertIn("checkCount 19, failedCheckCount 0, verdict SUCCESS", out)
        self.assertIn("checkCount 49, failedCheckCount 0, verdict SUCCESS", out)
        self.assertIn("checkCount 29 of expectedCheckCount 29, failedCheckCount 0, verdict SUCCESS", out)
        self.assertIn("check_count=19", out)
        identical = re.findall(r"^PASS - ([\w.\-]+)_byte_identical", out, re.MULTILINE)
        self.assertEqual(sorted(identical), ["curvature.json", "lovelock-components.md",
                                             "lovelock-report.json", "lovelock-tensors.json"])
        self.assertRegex(out, r"checks of this notebook: \d+ passed, 0 failed")

    def test_kohn_sham_record_counts_printed(self):
        out = all_output_text(notebook("kohn_sham_states"))
        self.assertNotIn("FAIL", out)
        expected = {"ks-theory-wolfram.json": 46, "ks-theory-python.json": 58, "ks-rust-solver.json": 42,
                    "ks-rust-determinism.json": 14, "ks-rust-mermin-roots.json": 5, "ks-reference.json": 37,
                    "ks-crosscheck.json": 31}
        for name, n in expected.items():
            rep = json.loads((KS_REPORTS / name).read_text(encoding="utf-8"))
            self.assertEqual(len(rep["checks"]), n, name)
            self.assertEqual(sum(c["verdict"] == "PASS" for c in rep["checks"]), n, name)
            self.assertIn(f"{name}: {n}/{n} checks pass, 0 fail, {n} listed checks with verdict PASS", out)
        states = re.findall(r"^PASS - (N\d+_\w+?)_equals_record", out, re.MULTILINE)
        self.assertEqual(len(states), 10, states)
        self.assertIn("N136_lamp1_a10_T20", states)
        self.assertIn("PASS - crosscheck_rows_reproduced: 84 rows", out)
        self.assertRegex(out, r"checks of this notebook: \d+ passed, 0 failed")

    def test_dark_sector_record_counts_printed(self):
        out = all_output_text(notebook("dark_sector_hypotheses"))
        self.assertNotIn("FAIL", out)
        expected = {("dirac16complex", "derivation-checks.json"): 30, ("dirac16complex", "ks-history-run.json"): 5,
                    ("dirac16complex", "eos-checks.json"): 13, ("dirac16complex", "independent-checks.json"): 9,
                    ("dirac16complex00", "python-derive-eos.json"): 49,
                    ("dirac16complex00", "python-independent-numerics.json"): 28}
        for (folder, name), n in expected.items():
            rep = json.loads((DARK / folder / "reports" / name).read_text(encoding="utf-8"))
            self.assertEqual(len(rep["checks"]), n, name)
            self.assertEqual(sum(c["verdict"] == "PASS" for c in rep["checks"]), n, name)
            self.assertIn(f"{name}: {n}/{n} checks pass, 0 fail, {n} listed checks with verdict PASS", out)
        self.assertIn("PASS - all_runs_succeeded: 123 runs", out)
        self.assertIn("PASS - dense_rows_bit_identical: 123 of 123 rows", out)
        self.assertIn("PASS - eos_rows_identical: 123 of 123 rows", out)
        for sid in ("N688_lam0", "N136_lam0", "N8_lamp1"):
            self.assertIn(f"PASS - {sid}_summary_equals_record:", out)
        for name in ("mixtures_equal_record", "mixture_C_w0_unite_has_positive_wa",
                     "mixture_C_constant_w_unite_only_with_freezing_cpl", "ratio_mixture_scan_cannot_reach_unite_wa",
                     "condensate_ratio_exact", "M2_tangent_exact", "M3_tangent_exact",
                     "M4_parameters_and_tangent_exact", "M5_crossing_exact_bracket", "positive_components_never_cross"):
            self.assertIn(f"PASS - {name}:", out)
        self.assertIn("u = -382/441 gives the ratio -191/250 = -0.764 exactly", out)
        self.assertIn("M4: s = 264037/403037 and Omega_q = 57963/264037", out)
        self.assertIn("the tangent is (-861/1000, -3/5) = the Unite pair EXACTLY", out)
        self.assertRegex(out, r"checks of this notebook: \d+ passed, 0 failed")


@unittest.skipUnless(FULL, "set REVISION_NOTEBOOKS_FULL=1 to re-execute the notebooks")
class FullTests(unittest.TestCase):
    def test_installed_versions_equal_pins(self):
        for line in (NB_DIR / "requirements.txt").read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                package, version = line.strip().split("==")
                self.assertEqual(importlib.metadata.version(package), version, package)

    def test_reexecution_byte_identical(self):
        parent = os.environ.get("REVISION_SCRATCH") or None
        if parent:
            Path(parent).mkdir(parents=True, exist_ok=True)
        for name in NAMES:
            with self.subTest(name=name):
                out = Path(tempfile.mkdtemp(prefix=f"revnb-{name}-", dir=parent)) / "run"
                proc = subprocess.run([sys.executable, str(TOOL_PATH), "check", name, "--out", str(out)],
                                      capture_output=True, text=True, encoding="utf-8", errors="replace")
                self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
                self.assertIn(f"check {name}: PASS", proc.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
