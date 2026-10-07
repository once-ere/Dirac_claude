#!/usr/bin/env python3
"""Test of the textbook "Universes in Pairs" (Revision/textbook/, TEXTBOOK_SPEC.md).

Initial version, 2026-10-02 (the infra stage: tools, requirements, pilot notebook 00a and the
draft chapter 00), extended 2026-10-07 (the README example built in a replica, the command
aliases, the per-chapter draft checks); the assembly stage completes it when the book is
assembled and registered.

Run from the repository root:
    python -m unittest Revision/tests/test_universes_in_pairs_textbook.py -v
Every notebook is re-executed (nbkit check, byte for byte) only with
    REVISION_NOTEBOOKS_FULL=1 (PowerShell: $env:REVISION_NOTEBOOKS_FULL = "1")
otherwise only the fast ones (expected run time at most FAST_SECONDS) are.

What is tested
  * requirements.txt: every [direct] and [support] pin equals the installed version, [support]
    is the complete dependency closure of [direct] (run_instructions.check_requirements);
  * the tools and the textbook sources are ASCII or UTF-8 with LF line endings only;
  * every notebook has its builder and its provenance file and vice versa; every builder
    passes nbkit lint and equals its stored notebook (cells and metadata, static);
  * the run instructions of every notebook are valid in their three renderings, and the stored
    notebook carries them (markdown cell 2, the comments of the set-up cell);
  * every provenance file equals the one regenerated from its own record and the stored files,
    and records a passed nbkit check;
  * every figure belongs to a captions file and vice versa;
  * every notebook renders as book Markdown that scripts/build_dissertation_tex.py accepts;
  * the validators reject what they must (references, the character pairs that the PDF fonts
    print as one other character, long lines);
  * the chapters written so far pass every assembler check (draft mode), together and each
    alone (as check_chapter.py --allow-unplaced assembles it);
  * the complete minimal example of tools/README.md builds and checks (nbkit build, byte for
    byte) in a throw-away replica of the textbook folder, and renders as book Markdown;
  * the fast notebooks (all with REVISION_NOTEBOOKS_FULL=1) rebuild byte for byte (nbkit check);
  * once they exist: the assembled book equals the assembler's output with every check passed,
    and its PDF is registered (edition universes-in-pairs-textbook) with page count and sha256.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REVISION = Path(__file__).resolve().parents[1]
ROOT = REVISION.parent
TEXTBOOK = REVISION / "textbook"
TOOLS = TEXTBOOK / "tools"
for _path in (ROOT, TOOLS):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import assemble_textbook  # noqa: E402
import nbkit  # noqa: E402
import render_notebook  # noqa: E402
import run_instructions  # noqa: E402
from scripts import build_dissertation_tex  # noqa: E402

NOTEBOOKS = TEXTBOOK / "notebooks"
SOURCES = NOTEBOOKS / "src"
FIGURES = TEXTBOOK / "figures"
REGISTRY = REVISION / "pdf-specifications.json"
EDITION = "universes-in-pairs-textbook"
FULL = os.environ.get("REVISION_NOTEBOOKS_FULL") == "1"
FAST_SECONDS = 60


def builders() -> list[Path]:
    return sorted(SOURCES.glob("*.py"))


class Requirements(unittest.TestCase):
    def test_pins_equal_installed_and_closure_complete(self) -> None:
        self.assertEqual(run_instructions.check_requirements(), [])

    def test_direct_block(self) -> None:
        direct, support = run_instructions.load_pins()
        self.assertEqual([name for name, _ in direct],
                         ["numpy", "sympy", "mpmath", "matplotlib", "jupyterlab",
                          "nbformat", "nbclient", "ipykernel", "nbconvert"])
        self.assertGreater(len(support), 50)
        self.assertNotIn("scipy", [name.lower() for name, _ in direct + support])


class Files(unittest.TestCase):
    def test_line_endings_and_encoding(self) -> None:
        paths = list(TOOLS.glob("*.py")) + [TOOLS / "README.md",
                                            TEXTBOOK / "requirements.txt"]
        paths += list(SOURCES.glob("*.py")) + list(NOTEBOOKS.glob("*.ipynb"))
        paths += list(NOTEBOOKS.glob("*.PROVENANCE.md")) + list(FIGURES.glob("*.json"))
        paths += list((TEXTBOOK / "chapters").glob("*.md"))
        for path in paths:
            data = path.read_bytes()
            with self.subTest(path=path.name):
                self.assertNotIn(b"\r", data)
                self.assertFalse(data.startswith(b"\xef\xbb\xbf"))
                data.decode("utf-8")
                self.assertTrue(data.endswith(b"\n"))
        for path in list(TOOLS.glob("*.py")) + list(SOURCES.glob("*.py")) + list(
                NOTEBOOKS.glob("*.PROVENANCE.md")) + [TEXTBOOK / "requirements.txt"]:
            with self.subTest(ascii=path.name):
                self.assertTrue(path.read_bytes().isascii())

    def test_notebooks_builders_provenance_correspond(self) -> None:
        stems = {p.stem for p in builders()}
        notebooks = {p.stem for p in NOTEBOOKS.glob("*.ipynb")}
        provenance = {p.name[:-len(".PROVENANCE.md")]
                      for p in NOTEBOOKS.glob("*.PROVENANCE.md")}
        self.assertEqual(stems, notebooks)
        self.assertEqual(stems, provenance)
        self.assertIn("00a_check_installation", stems)

    def test_figures_and_captions_correspond(self) -> None:
        listed = set()
        for sidecar in FIGURES.glob("*.captions.json"):
            captions = json.loads(sidecar.read_text(encoding="utf-8"))
            identifier = sidecar.name.split(".")[0]
            for name, caption in captions.items():
                with self.subTest(figure=name):
                    self.assertTrue(name.startswith(identifier + "_"))
                    self.assertTrue((FIGURES / name).is_file())
                    self.assertEqual(nbkit.caption_problems(name, caption), [])
                listed.add(name)
        self.assertEqual({p.name for p in FIGURES.glob("*.png")}, listed)


class Notebooks(unittest.TestCase):
    def test_builders_lint_and_match_stored_notebooks(self) -> None:
        for builder in builders():
            with self.subTest(builder=builder.name):
                self.assertEqual(nbkit.stored_notebook_matches_builder(builder), [])

    def test_run_instructions_in_three_renderings(self) -> None:
        for path in NOTEBOOKS.glob("*.ipynb"):
            notebook = json.loads(path.read_text(encoding="utf-8"))
            facts = notebook["metadata"]["textbook"]["facts"]
            with self.subTest(notebook=path.name):
                self.assertEqual(run_instructions.validate_facts(facts), [])
                self.assertEqual(run_instructions.check_renderings(facts), [])
                sources = ["".join(cell["source"]) for cell in notebook["cells"]]
                self.assertEqual(sources[1], run_instructions.notebook_markdown(facts))
                self.assertTrue(sources[2].startswith(
                    run_instructions.code_comments(facts) + "\n"))
                book = run_instructions.book_markdown(facts)
                self.assertNotRegex(book, r"\b[Ss]ee (?:the )?(?:Chapter|Section)")
                for needle in ("git clone https://github.com/once-ere/Dirac_claude.git",
                               "Windows (PowerShell):", "macOS (zsh):", "Linux (bash):",
                               "jupyter nbconvert --to notebook --execute --inplace",
                               "Run > Run All Cells"):
                    self.assertIn(needle, book)
                for line in facts["final_lines"]:
                    self.assertIn(line, book)

    def test_provenance_files_are_current(self) -> None:
        for builder in builders():
            with self.subTest(builder=builder.name):
                self.assertEqual(nbkit.provenance_is_current(builder), [])

    def test_rendered_notebooks_convert(self) -> None:
        for path in NOTEBOOKS.glob("*.ipynb"):
            with self.subTest(notebook=path.name):
                text, following = render_notebook.render(path, 9, 4)
                self.assertEqual(following, 6)
                self.assertTrue(text.startswith("### 9.4 How to run Notebook "))
                self.assertIn("### 9.5 Notebook ", text)
                document = "# T\n\n## S\n\n## 9. C\n\n" + text
                build_dissertation_tex.convert(document, strip_heading_numbers=True,
                                               developer_layout=True, image_root=ROOT,
                                               sections_from_zero=True)

    def test_notebooks_rebuild_byte_for_byte(self) -> None:
        selected = []
        for builder in builders():
            facts, _, _ = nbkit.load_builder(builder)
            if FULL or facts["expected_seconds"] <= FAST_SECONDS:
                selected.append(builder)
        if not selected:
            self.skipTest("no notebook selected")
        with tempfile.TemporaryDirectory() as scratch:
            for builder in selected:
                with self.subTest(builder=builder.name):
                    completed = subprocess.run(
                        [sys.executable, str(TOOLS / "nbkit.py"), "check", str(builder),
                         "--scratch", scratch], cwd=ROOT, capture_output=True, text=True)
                    self.assertEqual(completed.returncode, 0,
                                     completed.stdout[-3000:] + completed.stderr[-2000:])
                    self.assertIn("nbkit=OK", completed.stdout)


class Validators(unittest.TestCase):
    def facts(self) -> dict:
        facts, _, _ = nbkit.load_builder(SOURCES / "00a_check_installation.py")
        return facts

    def test_rejects_references_and_ligatures(self) -> None:
        for purpose in ("See Chapter 3 for the rest.", "Run it with --version.",
                        "It uses $x$ math."):
            facts = dict(self.facts(), purpose=purpose)
            with self.subTest(purpose=purpose):
                self.assertNotEqual(run_instructions.validate_facts(facts), [])

    def test_rejects_bad_captions(self) -> None:
        for caption in ("No full stop", "A dash -- here.", "A [bracket].", "Odd $x."):
            with self.subTest(caption=caption):
                self.assertNotEqual(nbkit.caption_problems("00a_1_x.png", caption), [])

    def test_reference_lists(self) -> None:
        dash = chr(0x2013)
        self.assertEqual(assemble_textbook.expand_list("Sections", "3.2" + dash + "3.4"),
                         (["3.2", "3.3", "3.4"], []))
        self.assertEqual(assemble_textbook.expand_list("Chapters", "12 to 14"),
                         (["12", "13", "14"], []))
        self.assertNotEqual(assemble_textbook.expand_list("Chapter", "3.1")[1], [])


class Tools(unittest.TestCase):
    def test_command_aliases(self) -> None:
        builder = str(SOURCES / "00a_check_installation.py")
        for command in ("lint", "--lint"):
            with self.subTest(command=command):
                completed = subprocess.run(
                    [sys.executable, str(TOOLS / "nbkit.py"), command, builder], cwd=ROOT,
                    capture_output=True, text=True)
                self.assertEqual(completed.returncode, 0, completed.stdout)
                self.assertIn("lint_00a=OK", completed.stdout)

    def test_readme_example_builds_in_a_replica(self) -> None:
        """The builder of tools/README.md section 8, built in a copy of the tools."""
        readme = (TOOLS / "README.md").read_text(encoding="utf-8")
        part = readme.split("## 8. A complete minimal example", 1)[1]
        source = re.search(r"```python\n(.*?)\n```", part, re.S).group(1) + "\n"
        name = re.search(r"notebooks/src/(\w+)\.py", part).group(1)
        with tempfile.TemporaryDirectory() as folder:
            replica = Path(folder) / "replica"
            tools = replica / "Revision" / "textbook" / "tools"
            tools.mkdir(parents=True)
            for path in TOOLS.glob("*.py"):
                shutil.copyfile(path, tools / path.name)
            shutil.copyfile(TEXTBOOK / "requirements.txt",
                            replica / "Revision" / "textbook" / "requirements.txt")
            builder = replica / "Revision" / "textbook" / "notebooks" / "src" / f"{name}.py"
            builder.parent.mkdir(parents=True)
            builder.write_text(source, encoding="utf-8", newline="\n")
            completed = subprocess.run(
                [sys.executable, str(builder), "build", "--date", "2026-10-07",
                 "--scratch", str(Path(folder) / "scratch")], cwd=replica,
                capture_output=True, text=True)
            self.assertEqual(completed.returncode, 0,
                             completed.stdout[-3000:] + completed.stderr[-2000:])
            identifier = name[:3]
            self.assertIn(f"check_{identifier}=PASSED", completed.stdout)
            self.assertIn(f"build_{identifier}=OK", completed.stdout)
            notebook = builder.parents[1] / f"{name}.ipynb"
            self.assertTrue(notebook.with_name(f"{name}.PROVENANCE.md").is_file())
            rendered = subprocess.run(
                [sys.executable, str(tools / "render_notebook.py"), str(notebook),
                 "--chapter", "2", "--section", "5"], cwd=replica, capture_output=True,
                text=True)
            self.assertEqual(rendered.returncode, 0, rendered.stderr)
            self.assertIn(f"### 2.5 How to run Notebook {identifier}", rendered.stdout)
            self.assertIn(f"### 2.6 Notebook {identifier}: complete text", rendered.stdout)
            self.assertIn("**Out [", rendered.stdout)
            self.assertIn(f"(Notebook {identifier}, figure 1.)]", rendered.stdout)


class Book(unittest.TestCase):
    def test_chapters_so_far_pass_every_check(self) -> None:
        result = assemble_textbook.assemble(None, allow_missing=True)
        self.assertEqual(result.problems, [])
        self.assertTrue(all(result.checks.values()), result.checks)

    def test_each_chapter_alone_passes_as_a_draft(self) -> None:
        for path in sorted(assemble_textbook.CHAPTERS.glob("[0-9][0-9]-*.md")):
            number = int(path.name[:2])
            with self.subTest(chapter=path.name):
                result = assemble_textbook.assemble([number], allow_missing=True,
                                                    placeholders=True,
                                                    allow_unplaced=True)
                self.assertEqual(result.problems, [])
                self.assertTrue(all(result.checks.values()), result.checks)

    def test_assembled_book_is_current(self) -> None:
        if not assemble_textbook.OUTPUT.is_file():
            self.skipTest("the book is not assembled yet (assembly stage)")
        result = assemble_textbook.assemble(None, allow_missing=False)
        self.assertEqual(result.problems, [])
        self.assertEqual(assemble_textbook.OUTPUT.read_bytes(),
                         result.text.encode("utf-8"))

    def test_pdf_registered(self) -> None:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        if EDITION not in registry:
            self.skipTest("the book's PDF is not registered yet (assembly stage)")
        entry = registry[EDITION]
        self.assertEqual(entry["path"],
                         "Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.pdf")
        pdf = ROOT / entry["path"]
        self.assertEqual(hashlib.sha256(pdf.read_bytes()).hexdigest(), entry["sha256"])
        self.assertGreater(entry["pages"], 0)


if __name__ == "__main__":
    unittest.main()
