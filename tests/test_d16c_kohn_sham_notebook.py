"""Unit tests for the Stage-4 Jupyter notebook: the builder's determinism and the audit.

Run from the repository root:
    python -m unittest discover -s tests -p "test_d16c_kohn_sham_notebook.py" -v

Nothing here executes the notebook or runs the solver (the Stage-4 gate does
that, steps stage4-33..38); the tests take well under a minute and write only
into tempfile directories.  They cover:

A. the builder notebooks/build_dirac16complex_kohn_sham_notebook.py: two builds
   in fresh processes (and from another working directory) are byte-identical,
   LF-only, nbformat 4.5 with the python3 kernel and stable cell ids; every
   quoted number is filled in and re-asserted by the gauntlet; the required
   figures are listed, described and drawn by the code; the committed notebook
   has exactly the builder's current cells;
B. the auditor notebooks/check_dirac16complex_kohn_sham_notebook.py on
   synthetic executed copies of the builder's cells: a complete copy passes
   every rule, and each rule fails on its own negative control (an error
   output, a FAIL line, a SKIP line, a missing ALL CHECKS PASSED, a wrong or
   missing figure, a missing embedded image, a changed cell, an unexecuted
   cell, an interactive tag, a short lead-in, a cross-reference, a wrong
   kernel); the executing runner is read from the notebook metadata;
C. the committed artifacts/dirac16complex/kohn-sham/notebook-report.json: its
   structure, its internal consistency, that it is current (the sha256 of the
   builder, auditor, runner and inputs it records equal the files, and the
   figures it lists are the PNG files on disk), that re-auditing the committed
   notebook reproduces its first execution, and its verdict.
"""

import base64
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BUILDER_PATH = REPO / "notebooks" / "build_dirac16complex_kohn_sham_notebook.py"
AUDITOR_PATH = REPO / "notebooks" / "check_dirac16complex_kohn_sham_notebook.py"
NOTEBOOK = REPO / "notebooks" / "dirac16complex_kohn_sham.ipynb"
REPORT = REPO / "artifacts" / "dirac16complex" / "kohn-sham" / "notebook-report.json"
FIGDIR = REPO / "artifacts" / "dirac16complex" / "kohn-sham" / "figures"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


_CACHE = {}


def builder():
    if "builder" not in _CACHE:
        _CACHE["builder"] = _load("_test_ks_nb_builder", BUILDER_PATH)
    return _CACHE["builder"]


def auditor():
    if "auditor" not in _CACHE:
        _CACHE["auditor"] = _load("_test_ks_nb_auditor", AUDITOR_PATH)
    return _CACHE["auditor"]


def built_cells():
    if "cells" not in _CACHE:
        _CACHE["cells"] = builder().build_notebook()["cells"]
    return copy.deepcopy(_CACHE["cells"])


def build_in_subprocess(output, cwd):
    result = subprocess.run([sys.executable, str(BUILDER_PATH), "--output", str(output)], cwd=str(cwd),
                            capture_output=True, text=True, encoding="utf-8", timeout=600)
    if result.returncode != 0:
        raise AssertionError(f"builder failed ({result.returncode}): {result.stdout[-2000:]} {result.stderr[-2000:]}")
    return Path(output).read_bytes()


def png_bytes(tag):
    """A minimal valid 1x1 PNG whose bytes depend on tag (a tEXt chunk)."""
    import struct
    import zlib

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    header = struct.pack(">IIBBBBB", 1, 1, 8, 0, 0, 0, 0)
    raw = zlib.compress(b"\x00\x00")
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"tEXt", b"Comment\x00" + tag.encode())
            + chunk(b"IDAT", raw) + chunk(b"IEND", b""))


class SyntheticNotebook:
    """An executed-looking copy of the builder's cells with fabricated outputs and figures."""

    def __init__(self, folder):
        self.folder = Path(folder)
        self.figdir = self.folder / "figures"
        self.figdir.mkdir()
        self.required = list(builder().REQUIRED_FIGURES)
        self.hashes = {}
        for name in self.required:
            data = png_bytes(name)
            (self.figdir / name).write_bytes(data)
            self.hashes[name] = hashlib.sha256(data).hexdigest()
        cells = built_cells()
        count = 0
        gauntlet_index = None
        for i, cell in enumerate(cells):
            if cell["cell_type"] != "code":
                continue
            count += 1
            cell["execution_count"] = count
            cell["outputs"] = [{"output_type": "stream", "name": "stdout", "text": [f"cell {count} ran\n"]}]
            if "def gauntlet" in "".join(cell["source"]):
                gauntlet_index = i
        self.gauntlet_index = gauntlet_index
        # the figures are printed (and embedded) by the first code cell after the driver
        first = next(i for i, c in enumerate(cells) if c["cell_type"] == "code" and "def find_binary" in "".join(c["source"]))
        for name in self.required:
            cells[first]["outputs"].append({"output_type": "stream", "name": "stdout",
                                            "text": [f"figure {name} sha256 {self.hashes[name]}\n"]})
            cells[first]["outputs"].append({"output_type": "display_data", "metadata": {},
                                            "data": {"image/png": base64.b64encode(png_bytes(name)).decode("ascii"),
                                                     "text/plain": [f"<Figure {name}>"]}})
        cells[gauntlet_index]["outputs"] = [{"output_type": "stream", "name": "stdout",
                                             "text": ["PASS - alpha: fine\n", "PASS - beta: fine\n",
                                                      "\n", "gauntlet: 2 checks, 2 passed, 0 failed, 0 skipped\n",
                                                      "ALL CHECKS PASSED\n"]}]
        self.nb = {"cells": cells,
                   "metadata": {"kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python",
                                               "name": "python3"},
                                "language_info": {"name": "python"}},
                   "nbformat": 4, "nbformat_minor": 5}

    def write(self, nb=None, name="nb.ipynb"):
        path = self.folder / name
        path.write_text(json.dumps(nb if nb is not None else self.nb, indent=1, ensure_ascii=False) + "\n",
                        encoding="utf-8", newline="\n")
        return path

    def audit(self, nb=None, expected="builder"):
        path = self.write(nb)
        exp = built_cells() if expected == "builder" else expected
        return auditor().audit(path, exp, self.required, self.figdir)


# ---------------------------------------------------------------------------
# A. the builder
# ---------------------------------------------------------------------------

class TestBuilder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = Path(cls.tmp.name)
        cls.first = build_in_subprocess(root / "a.ipynb", REPO)
        other = root / "elsewhere"
        other.mkdir()
        cls.second = build_in_subprocess(root / "b.ipynb", other)
        cls.nb = json.loads(cls.first.decode("utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_two_builds_are_byte_identical_from_any_working_directory(self):
        self.assertEqual(self.first, self.second)

    def test_lf_only_and_trailing_newline(self):
        self.assertNotIn(b"\r", self.first)
        self.assertTrue(self.first.endswith(b"}\n"))

    def test_in_process_build_equals_the_written_file(self):
        self.assertEqual(builder().notebook_text(builder().build_notebook()).encode("utf-8"), self.first)

    def test_format_kernel_and_cell_ids(self):
        nb = self.nb
        self.assertEqual((nb["nbformat"], nb["nbformat_minor"]), (4, 5))
        self.assertEqual(nb["metadata"]["kernelspec"], {"display_name": "Python 3 (ipykernel)", "language": "python",
                                                        "name": "python3"})
        ids = [c["id"] for c in nb["cells"]]
        self.assertEqual(ids, [f"ks-{i:03d}" for i in range(len(ids))])
        for cell in nb["cells"]:
            if cell["cell_type"] == "code":
                self.assertIsNone(cell["execution_count"])
                self.assertEqual(cell["outputs"], [])

    def test_nbformat_schema(self):
        try:
            import nbformat
        except ImportError:
            self.skipTest("nbformat not installed")
        nbformat.validate(nbformat.reads(self.first.decode("utf-8"), as_version=4))

    def test_every_quote_is_filled_and_reasserted(self):
        b = builder()
        markdown = "".join("".join(c["source"]) for c in self.nb["cells"] if c["cell_type"] == "markdown")
        self.assertNotIn("«", markdown)
        self.assertNotIn("»", markdown)
        gauntlet = next("".join(c["source"]) for c in self.nb["cells"]
                        if c["cell_type"] == "code" and "def gauntlet" in "".join(c["source"]))
        self.assertGreater(len(b.QUOTES), 100)
        for key, (fmt, expr, text) in b.QUOTES.items():
            self.assertIn(f"({key!r}, {fmt!r}, lambda: {expr}, {text!r}),", gauntlet)
            self.assertEqual(fmt.format(eval(expr, b._namespace())), text)

    def test_required_figures_are_described_and_drawn(self):
        b = builder()
        self.assertEqual(len(b.REQUIRED_FIGURES), 14)
        self.assertEqual(sorted(b.FIGURE_DESCRIPTIONS), b.REQUIRED_FIGURES)
        code = "".join("".join(c["source"]) for c in self.nb["cells"] if c["cell_type"] == "code")
        for name in b.REQUIRED_FIGURES:
            self.assertEqual(code.count(f'save_figure(fig, "{name}")'), 1, name)
            self.assertTrue(b.FIGURE_DESCRIPTIONS[name].strip())
        self.assertIn(repr(b.REQUIRED_FIGURES), code)

    def test_driver_and_honesty_rules_in_the_code(self):
        code = "".join("".join(c["source"]) for c in self.nb["cells"] if c["cell_type"] == "code")
        for needle in ('run("print-config")', 'lines[-1] != "SUCCESS"', 'metadata={"Software": None}',
                       'matplotlib.use("Agg")', "def skip(", 'raise AssertionError("gauntlet failed: "',
                       "ALL CHECKS PASSED", "compare_canonical", "python_check_report"):
            self.assertIn(needle, code)
        # the heavy subcommands are never started by the notebook
        for sub in ("scf", "excited", "thermo", "emt", "all"):
            self.assertNotIn(f'run("{sub}"', code)

    def test_committed_notebook_has_the_builders_current_cells(self):
        committed = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        self.assertEqual(auditor().cell_signature(committed["cells"]), auditor().cell_signature(self.nb["cells"]),
                         "rebuild: python notebooks/build_dirac16complex_kohn_sham_notebook.py, then execute and audit")

    def test_committed_figures_are_deterministic_pngs(self):
        for name in builder().REQUIRED_FIGURES:
            data = (FIGDIR / name).read_bytes()
            self.assertTrue(data.startswith(b"\x89PNG\r\n\x1a\n"), name)
            self.assertNotIn(b"Software", data[:4096], name)


# ---------------------------------------------------------------------------
# B. the auditor on synthetic executed copies
# ---------------------------------------------------------------------------

class TestAuditor(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.syn = SyntheticNotebook(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def failing(self, nb, expected="builder"):
        ok, problems, facts = self.syn.audit(nb, expected)
        return sorted(name for name, passed in ok.items() if not passed), problems, facts

    def test_complete_copy_passes_every_rule(self):
        bad, problems, facts = self.failing(self.syn.nb)
        self.assertEqual(bad, [], problems)
        self.assertEqual([g["name"] for g in facts["gauntlet"]], ["alpha", "beta"])
        self.assertEqual(len(facts["figures"]), 14)
        self.assertEqual(facts["runner"], auditor().RUNNER_LABELS[0])

    def test_runner_is_read_from_the_metadata(self):
        nb = copy.deepcopy(self.syn.nb)
        nb["metadata"]["language_info"] = {"name": "python", "version": "3.14.0"}
        _, _, facts = self.failing(nb)
        self.assertEqual(facts["runner"], auditor().RUNNER_LABELS[1])

    def test_error_output_fails_r07(self):
        nb = copy.deepcopy(self.syn.nb)
        nb["cells"][self.syn.gauntlet_index]["outputs"].append(
            {"output_type": "error", "ename": "AssertionError", "evalue": "x", "traceback": []})
        self.assertIn("r07_no_error_outputs", self.failing(nb)[0])

    def test_fail_and_skip_lines_and_missing_final_line_fail_the_gauntlet_rule(self):
        for lines in (["FAIL - alpha: bad\n", "ALL CHECKS PASSED\n"],
                      ["PASS - alpha: fine\n", "SKIP - beta: input absent\n",
                       "ALL COMPUTED CHECKS PASSED; SKIPPED (inputs absent): beta\n"],
                      ["PASS - alpha: fine\n"],
                      []):
            nb = copy.deepcopy(self.syn.nb)
            nb["cells"][self.syn.gauntlet_index]["outputs"] = [{"output_type": "stream", "name": "stdout",
                                                               "text": lines}]
            self.assertIn("r07_gauntlet_passed", self.failing(nb)[0], lines)

    def test_gauntlet_lines_outside_the_gauntlet_cell_do_not_count(self):
        nb = copy.deepcopy(self.syn.nb)
        first_code = next(c for c in nb["cells"] if c["cell_type"] == "code")
        first_code["outputs"].append({"output_type": "stream", "name": "stdout", "text": ["FAIL - program_line: x\n"]})
        bad, _, facts = self.failing(nb)
        self.assertEqual(bad, [])
        self.assertNotIn("program_line", [g["name"] for g in facts["gauntlet"]])

    def test_figure_problems_fail_r08(self):
        # wrong hash on disk
        (self.syn.figdir / self.syn.required[0]).write_bytes(png_bytes("changed"))
        self.assertIn("r08_figures_match_disk", self.failing(self.syn.nb)[0])

    def test_missing_figure_and_missing_image_fail_r08(self):
        nb = copy.deepcopy(self.syn.nb)
        first = next(c for c in nb["cells"] if c["cell_type"] == "code" and "def find_binary" in "".join(c["source"]))
        first["outputs"] = [o for o in first["outputs"]
                            if not (o["output_type"] == "stream" and self.syn.required[1] in "".join(o["text"]))]
        self.assertIn("r08_figures_match_disk", self.failing(nb)[0])
        nb = copy.deepcopy(self.syn.nb)
        first = next(c for c in nb["cells"] if c["cell_type"] == "code" and "def find_binary" in "".join(c["source"]))
        outs = first["outputs"]
        del outs[max(i for i, o in enumerate(outs) if o["output_type"] == "display_data")]
        bad, problems, _ = self.failing(nb)
        self.assertEqual(bad, ["r08_figures_match_disk"])
        self.assertTrue(any("embedded images" in p for p in problems["r08_figures_match_disk"]))

    def test_changed_cell_fails_r12(self):
        nb = copy.deepcopy(self.syn.nb)
        md = next(c for c in nb["cells"] if c["cell_type"] == "markdown")
        md["source"] = ["".join(md["source"]).replace("Kohn-Sham", "Kohn Sham", 1)]
        bad = self.failing(nb)[0]
        self.assertIn("r12_cells_match_builder", bad)
        self.assertIn("r12_cells_match_builder", self.failing(self.syn.nb, expected=None)[0])

    def test_unexecuted_or_misnumbered_cells_fail_r06(self):
        nb = copy.deepcopy(self.syn.nb)
        next(c for c in nb["cells"] if c["cell_type"] == "code")["execution_count"] = None
        self.assertIn("r06_executed_in_order", self.failing(nb)[0])
        nb = copy.deepcopy(self.syn.nb)
        [c for c in nb["cells"] if c["cell_type"] == "code"][-1]["execution_count"] = 99
        self.assertIn("r06_executed_in_order", self.failing(nb)[0])

    def test_interactive_tag_and_input_fail_r05(self):
        nb = copy.deepcopy(self.syn.nb)
        next(c for c in nb["cells"] if c["cell_type"] == "code")["metadata"]["tags"] = ["interactive"]
        self.assertEqual(self.failing(nb)[0], ["r05_headless_driver"])

    def test_short_lead_in_fails_r03_and_cross_reference_fails_r02(self):
        nb = copy.deepcopy(self.syn.nb)
        i = next(i for i, c in enumerate(nb["cells"]) if c["cell_type"] == "code")
        nb["cells"].insert(i, {"cell_type": "markdown", "id": "short", "metadata": {}, "source": ["Next."]})
        self.assertIn("r03_markdown_lead_ins", self.failing(nb)[0])
        nb = copy.deepcopy(self.syn.nb)
        nb["cells"][0]["source"].append("\nSee the Stage-3 notebook dirac16complex_dark_sector.ipynb.\n")
        self.assertIn("r02_no_cross_references", self.failing(nb)[0])

    def test_wrong_kernel_fails_r09(self):
        nb = copy.deepcopy(self.syn.nb)
        nb["metadata"]["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python"}
        self.assertIn("r09_kernel_python3", self.failing(nb)[0])

    def test_unreadable_file_fails_every_rule(self):
        path = Path(self.tmp.name) / "broken.ipynb"
        path.write_text("{not json", encoding="utf-8")
        ok, _, _ = auditor().audit(path, built_cells(), self.syn.required, self.syn.figdir)
        self.assertFalse(any(ok.values()))


# ---------------------------------------------------------------------------
# C. the committed report
# ---------------------------------------------------------------------------

class TestCommittedReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))

    def test_structure(self):
        r = self.report
        for key in ("schemaVersion", "producer", "notebook", "builder", "runner", "adaptedFrom", "kernel",
                    "fixtureSha256", "cells", "codeCells", "rules", "checks", "checkCount", "failedCheckCount",
                    "failed", "measurements", "sourceSha256", "executions", "crossExecution", "figures", "gauntlet",
                    "verdict"):
            self.assertIn(key, r)
        self.assertEqual(r["producer"], "notebooks/check_dirac16complex_kohn_sham_notebook.py")
        self.assertEqual(r["notebook"], "notebooks/dirac16complex_kohn_sham.ipynb")
        self.assertIn("a8fdff459adfe181573d7924b18bffbdf378fdb3", r["adaptedFrom"])
        self.assertIn("BSD-3-Clause", r["adaptedFrom"])

    def test_internal_consistency(self):
        r = self.report
        self.assertEqual(r["checkCount"], len(r["checks"]))
        failed = sorted(k for k, v in r["checks"].items() if v is not True)
        self.assertEqual(sorted(r["failed"]), failed)
        self.assertEqual(r["failedCheckCount"], len(failed))
        self.assertEqual(r["verdict"], "SUCCESS" if not failed else "FAILURE")
        g = r["gauntlet"]
        self.assertEqual(g["count"], len(g["results"]))
        self.assertEqual(g["passed"] + g["failed"] + g["skipped"], g["count"])
        for item in g["results"]:
            self.assertEqual(r["checks"]["gauntlet_" + item["name"]], item["status"] == "PASS")
        for name in ("r01_how_to_run_needles", "r07_gauntlet_passed", "r08_figures_match_disk",
                     "r12_cells_match_builder"):
            self.assertIn(name, r["checks"])

    def test_report_is_current(self):
        a = auditor()
        src = self.report["sourceSha256"]
        self.assertEqual(src["builder"], a.sha256_file(BUILDER_PATH))
        self.assertEqual(src["auditor"], a.sha256_file(AUDITOR_PATH))
        self.assertEqual(src["runner"], a.sha256_file(REPO / "notebooks" / "run_notebook.py"))
        for name, digest in a.input_hashes().items():
            self.assertEqual(src.get(name), digest, f"{name} changed since the report was written")
        committed = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        self.assertEqual(src["notebookCells"], a.signature_sha256(committed["cells"]))
        self.assertEqual(self.report["fixtureSha256"],
                         a.sha256_file(REPO / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"))

    def test_figures_listed_are_the_files_on_disk(self):
        listed = {Path(f["file"]).name: f for f in self.report["figures"]}
        self.assertEqual(sorted(listed), builder().REQUIRED_FIGURES)
        for name, entry in listed.items():
            data = (FIGDIR / name).read_bytes()
            self.assertEqual(entry["sha256"], hashlib.sha256(data).hexdigest(), name)
            self.assertEqual(entry["bytes"], len(data), name)
            self.assertEqual(entry["description"], builder().FIGURE_DESCRIPTIONS[name])

    def test_reaudit_of_the_committed_notebook_reproduces_the_first_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report.json"
            with contextlib.redirect_stdout(io.StringIO()):
                auditor().main([str(NOTEBOOK), "--report", str(out)])
            fresh = json.loads(out.read_text(encoding="utf-8"))
        committed = self.report
        for key in ("gauntlet", "figures", "cells", "codeCells", "markdownCells", "executedCodeCells",
                    "fixtureSha256", "sourceSha256"):
            self.assertEqual(fresh[key], committed[key], key)
        first = dict(committed["executions"][0])
        mine = dict(fresh["executions"][0])
        first.pop("notebook")
        mine.pop("notebook")
        self.assertEqual(mine, first)

    def test_two_executions_with_identical_results(self):
        r = self.report
        self.assertEqual(len(r["executions"]), 2)
        self.assertTrue(r["crossExecution"]["compared"])
        self.assertEqual(r["executions"][0]["runner"], auditor().RUNNER_LABELS[0])
        self.assertEqual(r["executions"][1]["runner"], auditor().RUNNER_LABELS[1])

    def test_verdict_success(self):
        r = self.report
        self.assertEqual(r["verdict"], "SUCCESS",
                         f"failed checks {r['failed']}; gauntlet failed/skipped: "
                         f"{r['measurements'].get('gauntletFailed')}, {r['measurements'].get('gauntletSkipped')}")
        self.assertTrue(r["crossExecution"]["identicalGauntletAndFigures"])


if __name__ == "__main__":
    unittest.main()
