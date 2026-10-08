# The tools of the textbook "Universes in Pairs"

Written 2026-10-02 (infra of the textbook workflow). These tools build, check and assemble the
book `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.{md,tex,pdf}` and its notebooks, following
`Revision/textbook/TEXTBOOK_SPEC.md` sections 2 to 4 and rule R6. Every command below is run
from the repository root, in PowerShell or bash alike.

| file | what it does |
| --- | --- |
| `nbkit.py` | builds a notebook from its builder, executes it, checks it, writes the `.ipynb` and its `.PROVENANCE.md`; `check` re-executes into scratch and compares byte for byte |
| `run_instructions.py` | the complete, self-contained run instructions of a notebook, in three renderings (book section, notebook markdown cell 2, `#` comments of the set-up cell); `--check-requirements` checks `requirements.txt` |
| `render_notebook.py` | turns a stored, executed notebook into the book's Markdown for a marker `<!-- NOTEBOOK NNx -->` |
| `assemble_textbook.py` | assembles the book from `chapters/` and checks it (every check of TEXTBOOK_SPEC section 4) |
| `check_chapter.py` | test-builds ONE chapter (or the current book) as a PDF in scratch, through `scripts/build_provenance_pdf.py`, with a throw-away registry copy |

The pinned packages are in `Revision/textbook/requirements.txt` ([direct]: the nine packages the
instructions install; [support]: their complete dependency closure, 93 packages).

## 1. The workflow of a chapter

1. Write one builder per worked example: `Revision/textbook/notebooks/src/NNx_short_name.py`
   (section 2 below).
2. `python Revision/textbook/tools/nbkit.py lint Revision/textbook/notebooks/src/NNx_short_name.py`
   until it prints `nbkit=OK` (static rules only, instant).
3. `python Revision/textbook/tools/nbkit.py build Revision/textbook/notebooks/src/NNx_short_name.py --date 2026-10-02 --scratch <your scratch folder>`
   executes the notebook, writes `Revision/textbook/notebooks/NNx_short_name.ipynb`, its figures,
   then executes it a SECOND time into the scratch folder and compares everything byte for byte,
   then writes `Revision/textbook/notebooks/NNx_short_name.PROVENANCE.md`. Success: the lines
   `check_NNx=PASSED` and `build_NNx=OK`. Several builders may be given at once.
4. Later, to re-verify without changing anything:
   `python Revision/textbook/tools/nbkit.py check Revision/textbook/notebooks/src/NNx_short_name.py --scratch <dir>`
   (`check_NNx=PASSED`; `nbkit.py --check ...` is the same command). With
   `--record YYYY-MM-DD` a passed check is stored as the new verification date in the
   provenance file. A change of `run_instructions.py` or of the set-up cell changes the
   text of EVERY notebook: then every notebook must be rebuilt with `nbkit.py build`.
5. Write the chapter `Revision/textbook/chapters/NN-short-name.md` with a marker line
   `<!-- NOTEBOOK NNx -->` for each notebook (section 5 below).
6. `python Revision/textbook/tools/check_chapter.py Revision/textbook/chapters/NN-short-name.md --scratch <dir>`
   until it prints `chapter_check=OK` (no `problem=` and no `latex_warning=` lines); it reports
   the page count (`measurement_pages=`). Every stored notebook of the chapter must be placed.
   While the chapter is a draft that does not yet place every notebook built for it, add
   `--allow-unplaced`: the unplaced notebooks and their figures are listed as `unplaced=`
   lines and the last line reads `chapter_check=OK_DRAFT` (never `OK`).

Scratch folders: always pass `--scratch` with a folder of your own (the default is a folder in
the system's temporary folder, shared by everyone who omits the option). Notebook builds of
different agents may run at the same time: nbkit only reports files changed by others as
`warning=... changed during the run (by another process?)`; such warnings are harmless.

## 2. A builder

A builder is a Python file that defines `FACTS` and `CELLS` and nothing that runs on import:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {...}          # section 2.1
CELLS = [md(...), ...]  # section 2.2

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))   # python <builder>.py lint|build|check ...
```

`md(text)` and `code(text)` make a markdown and a code cell; the text is dedented and leading
and trailing blank lines are dropped, so write cells as indented triple-quoted strings. Use
`r'''...'''` for code cells (then the code may contain `"""` docstrings and backslashes).

### 2.1 FACTS (every key is required unless marked optional)

| key | type | meaning |
| --- | --- | --- |
| `id` | str | two digits and a letter, `"03b"` |
| `name` | str | the file name without `.ipynb`: the id, `_`, lower-case words joined by `_`; at most 25 characters (`"03b_curvature"`) |
| `title` | str | one line, no final full stop |
| `purpose` | str | one or more sentences ending with a full stop: what the notebook computes and checks |
| `records` | list | `[[path, what], ...]`: every Revision record (under `Revision/`, not `Revision/textbook/`) the notebook reads or reproduces; `[]` if none |
| `packages` | list | the pinned [direct] packages the notebook imports, e.g. `["numpy", "sympy", "matplotlib"]` |
| `needs_rust` | list | `[]`, or `[{"manifest": "Revision/kohn_sham/solver/Cargo.toml", "binaries": ["revision_ks_solver"], "build_minutes": 2}]` |
| `expected_seconds` | number | typical run time of the whole notebook (the instructions print "about N seconds/minutes") |
| `timeout_seconds` | int | nbkit's limit per cell, at least twice `expected_seconds` |
| `files_written` | list | EVERY repository file the notebook writes, e.g. `Revision/textbook/figures/03b.captions.json` (always), each figure `Revision/textbook/figures/03b_<k>_<name>.png`, data files (only below `Revision/textbook/`) |
| `final_lines` | list | the exact last printed lines of the last code cell; the last one is `ALL <n> CHECKS PASSED (notebook 03b)` |
| `troubleshooting` | list | `[[symptom, fix], ...]` or `[[symptom, fix, [command, ...]], ...]` for notebook-specific problems; `[]` if none |
| `allow_stderr` | bool, optional | allow output on stderr (default False; fix warnings instead) |
| `network` | str, optional | what the notebook downloads while it runs (default: nothing) |

Free text in FACTS (title, purpose, record descriptions, troubleshooting, network) must be
ASCII and self-contained (no "see Chapter 3", "Section 3.2", "README", "this book"), may contain
`code spans` in backticks, and must not contain `$ * [ ]` or the character pairs `--`, `<<`,
`>>`, two backticks or two single quotes (the PDF fonts print each pair as one other character,
even inside code spans: `--version` would print as a dash). A command such as
`cargo build --release ...` goes into the third element of a troubleshooting entry, which is
printed verbatim. `run_instructions.py` validates all of this.

### 2.2 CELLS and the layout of a notebook

The builder's cells are, in order: the markdown cell `## 1. What this notebook computes`; the
markdown cell `## 3. The words used in this notebook`; the markdown cell
`## 4. The physical and mathematical situation`; then the computation in sections
`## 5. ...`, `## 6. ...`; and as the very last cell the markdown cell
`## N. What this notebook showed`. nbkit inserts after the first cell the markdown cell
`## 2. How to run this notebook` and the SET-UP code cell (the instructions as comments and
the standard preamble). The sections `## k. Title` must be numbered 1, 2, 3, ... in order.

Enforced by `nbkit lint` (and again by build/check):

- every code cell directly preceded by a markdown cell; no empty cell;
- every source line at most 89 characters, no tabs, no trailing blanks, ASCII only (write
  Greek as LaTeX `$\gamma$` in markdown; in code use names like `gamma`);
- no ``` and no HTML comment in any cell; no IPython magics (`%`, `!`) and no `get_ipython`;
- the last line of the last code cell is `all_checks_passed()`;
- `files_written` lists the captions file; figure file names `NNx_<k>_<name>.png`.

Enforced after execution (build and check):

- no error output; no stderr output (unless `allow_stderr`);
- every printed line at most 89 characters, plain ASCII, not starting with ```; at most 80
  output lines per cell (write longer results into a data file listed in `files_written`);
- no memory address (`0x7f...`) and no path of the build computer in any output (never print
  `REPO`, `OUTPUT_ROOT`, `Path.cwd()` or absolute paths; print repository-relative paths);
- every picture is shown by `save_figure`: a figure that is not passed to `save_figure`
  (or a `plt.show()`) is drawn by Jupyter at the end of the cell and fails the build;
- the value of the last line of a cell is printed by Jupyter: if that line is, for example,
  `ax.legend()`, Jupyter prints `<matplotlib.legend.Legend at 0x...>`, a memory address that
  differs from run to run and fails the build; end such a line with `;` (or do not make it the
  last line);
- each figure: 150 dpi, no PNG metadata, height at most 1.25 times its width (taller figures
  do not fit a page of the book), at least 300 pixels wide; numbered 1, 2, 3, ...;
- captions: one ASCII line ending with a full stop; math as `$...$`; no `[ ] * ` + backticks;
  none of the pairs `--`, `<<`, `>>`, two backticks, two single quotes;
- the files written are exactly `files_written` (in a check run: exactly these files appear in
  the scratch folder, and none of them changes in the repository);
- the last code cell ends with exactly `final_lines`; at least one PASS line;
- the second execution (check, with a different PYTHONHASHSEED) reproduces the notebook, every
  written file and the provenance file byte for byte. So: no time stamps, no random numbers
  without a fixed seed (`np.random.default_rng(12345)`), no printed order of a `set` of strings
  (sort it first), no timing measurements in printed output.

### 2.3 What the set-up cell gives every notebook

| name | meaning |
| --- | --- |
| `json`, `os`, `textwrap`, `Path`, `matplotlib`, `plt`, `Image`, `display` | imported |
| `NOTEBOOK_ID` | `"03b"` |
| `REPO` | the repository folder (never print it) |
| `OUTPUT_ROOT` | where files are written: `REPO`, or the scratch folder of `nbkit check` |
| `repository_file(rel)` | `REPO / rel`: read a Revision record, e.g. `json.loads(repository_file("Revision/algebra/reports/x.json").read_text(encoding="utf-8"))` |
| `output_file(rel)` | the path to WRITE the repository file `rel` (folders are made); every written file must go through it and be listed in `files_written` |
| `say(text)` | print text wrapped to 89 characters |
| `FIGURE_FOLDER` | `"Revision/textbook/figures"` |
| `save_figure(fig, name, caption)` | saves `Revision/textbook/figures/<id>_<k>_<name>.png` (dpi 150, tight margins, no metadata), records the caption in `<id>.captions.json`, shows the saved picture, closes the figure, prints `Figure <id>.<k> saved as ...`; `name`: lower-case letters, digits, `_` |
| `check(condition, name, record=None)` | raises `AssertionError("check failed: name")` if the condition is false, else prints `PASS name`; with `record="Revision/.../report.json, check <check name>"` it prints a second line `     reproduces ...` (use it whenever a number reproduces a Revision record) |
| `report(label, value, unit="")` | prints `RESULT label = value unit` (key numbers; they are listed in the provenance file) |
| `all_checks_passed()` | prints `ALL <n> CHECKS PASSED (notebook <id>)` |
| `rust_program(manifest, binary)` | only when `needs_rust` is not empty: runs `cargo build --release` for the crate (quiet; a second when up to date), prints `Rust program <binary> is built and ready.` and returns the program's path (with or without `.exe`); run it with `subprocess.run([str(path), ...], capture_output=True, text=True)` and never print its timing |

The caption given to `save_figure` IS the book's caption of the figure: write it as a teaching
caption (what is plotted, the axes and their units, what the student should see and why). The
book prints it under the figure followed by "(Notebook 03b, figure k.)".

## 3. The provenance file (rule R6)

`nbkit build` writes `Revision/textbook/notebooks/<name>.PROVENANCE.md`: what the notebook
computes and from which Revision records; the complete student instructions (the book's text);
the expected output (every PASS line with its cell, every RESULT line, the final lines, every
figure with its size and caption); the side effects (every file written with size and sha256,
the notebook file itself when run with `--inplace` or saved, `.ipynb_checkpoints`, Rust `target`
folders and binaries and whether cargo downloads anything, caches outside the repository,
network use, measured run time and peak memory of the build and the check run); the environment
(operating system, Python, package versions, cargo); the sha256 of the notebook, the builder and
every written file; the verification date and the `nbkit check` result. Everything that varies
from run to run is kept in the machine-readable last line `<!-- nbkit-record {...} -->`; the
rest is regenerated from it, so `nbkit check` (and the test suite) can require the file to be
exactly up to date. Never edit it by hand: rebuild.

## 4. Rust notebooks

Put the crate in `needs_rust` (manifest, binary names, typical first-build minutes) and call
`rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")` in a code cell
after a markdown cell that explains it. The instructions then contain the Rust installation
and the exact `cargo build --release --manifest-path ...` command. The build writes
`<crate>/target/` (ignored by git). The Revision crates have no dependencies, so cargo
downloads nothing. Print only deterministic summaries of the program's output.

## 5. Placing a notebook in a chapter

A chapter `Revision/textbook/chapters/NN-short-name.md` starts with `## N. Title` (N without a
leading zero) and has sections `### N.M Title` numbered 1, 2, 3, ... in order, and no other
heading levels. A notebook is placed by a line that holds exactly

```text
<!-- NOTEBOOK 03b -->
```

The assembler replaces it by two sections that continue the numbering: if the last section
before the marker is `### 3.4 ...`, they are `### 3.5 How to run Notebook 03b` (the complete
instructions) and `### 3.6 Notebook 03b: complete text` (every cell, its outputs and its
figures). The chapter's NEXT section must therefore be
`### 3.7 Line-by-line walk-through of Notebook 03b`, and the following ones continue with 3.8.
A notebook belongs to the chapter of its number and is placed exactly once; every stored
notebook must be placed. `python Revision/textbook/tools/render_notebook.py --chapter-file
Revision/textbook/chapters/03-x.md` prints the expanded chapter.

The Markdown of a chapter is the subset of `scripts/build_dissertation_tex.py` (read its
header). What the tests of 2026-10-02 showed (repeated 2026-10-07 with a probe document
built through `scripts/build_provenance_pdf.py` and read back with `pdftotext`: a code
span `--version` prints as an en dash and `version`, `<<x>>` as guillemets, `a''b` with
one closing quote; inside fenced blocks `--`, `<<` and `>>` print verbatim; a fenced
line of 20 Greek letters and 69 ASCII characters overflows by 18.5pt; a justified
paragraph with a long code-span path gives an Underfull warning):

- `$...$` and `$$` blocks (a line with only `$$` opens and closes) for math; Greek letters and
  the symbols of its MATH_CHARACTERS table may be typed directly in prose, math and captions;
- `**bold**`, `*emphasis*`, `` `code` `` (long code spans are broken anywhere, so they never
  overflow), links `[text](https://...)`; a lone `*` or `$` in prose starts emphasis or math;
- NEVER the pairs `--`, `<<`, `>>`, two backticks or two single quotes outside fenced blocks
  and math, not even in code spans (they print as a dash, a guillemet or a curly quote): put
  commands with options like `--release` into fenced blocks; write a dash as the character
  U+2013 or U+2014 (the assembler's check `proseCharacters`);
- in fenced blocks (```` ```text ```` / ```` ```python ````) everything is printed verbatim, but
  straight single quotes and backticks are printed as curly quotes (a limitation of the shared
  PDF builder, not of the book): write strings in code cells with double quotes, and never put
  a single quote into a command (the run instructions use `"=https"`, for example); lines at
  most 89 characters, a non-ASCII character counting twice (it is wider), no tabs;
- list items are single lines `- text` or `1. text`; a line in prose that starts with a number
  and a full stop becomes a list item, a line that starts with `#` a heading;
- tables: a header row, a separator row `| --- | --- |`, the same number of cells in every row;
- a figure is a line holding only `![caption](Revision/textbook/figures/NNx_k_name.png)`; a
  figure taller than the page fails the build (nbkit limits the aspect ratio);
- no HTML comments other than the notebook markers (the PDF would print them);
- references "Chapter N", "Section N.M", "Sections 3.2 to 3.4" are checked; a reference into
  another document is recognised when its sentence names the document (a `.md`/`.json` file,
  SPEC, README, a "document", the "original textbook", a `Revision/` path);
- never write that complex conjugation is charge conjugation (rule R5; the assembler's check
  `forbiddenPhrases`).

## 6. Test-building a chapter and assembling the book

`check_chapter.py CHAPTER.md --scratch DIR [--date "October 2026"] [--allow-unplaced]` runs
every assembler check on the chapter (references into chapters not yet written are listed as
`pending_reference=`; with `--allow-unplaced`, notebooks of the chapter that no marker places
yet are listed as `unplaced=` and the result is at best `chapter_check=OK_DRAFT`),
builds a test book in `DIR/chapter_NN/` (with one placeholder section per earlier chapter, so
the numbers are the book's) and runs `scripts/build_provenance_pdf.py` twice with the book's
options: `--register` into a throw-away copy of `Revision/pdf-specifications.json`, then verify
mode against it. Any LaTeX warning is printed as `latex_warning=` and fails. The repository is
not changed. `--book` test-builds all chapters written so far the same way.

`assemble_textbook.py` (no options) checks everything and writes
`Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md` (all 24 chapters must exist);
`--check` only checks and compares with the stored file; `--allow-missing --output FILE`
writes a draft of the chapters so far. The front matter is the title of TEXTBOOK_SPEC R1
(fixed in the assembler) and the abstract `Revision/textbook/chapters/abstract.md`. The book's
PDF is then built with

```text
python scripts/build_provenance_pdf.py Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md
    --developer-layout --number-sections-from-zero
    --specifications Revision/pdf-specifications.json --date "October 2026" [--register]
```

(one command line; `--date` sets the date under the title, otherwise the builder's default
"September 2026" would be printed).

## 7. Tests

`python -m unittest Revision/tests/test_universes_in_pairs_textbook.py -v` checks the pins
against the installed packages, the tools (renderings, the converter on a rendered notebook),
every builder against its stored notebook (static), every provenance file (regenerated from its
record), every fast notebook by a full `nbkit check` (all of them with
`REVISION_NOTEBOOKS_FULL=1`), every chapter alone as a draft, the example of section 8 (built
and checked in a throw-away copy of the tools), and, once they exist, the assembled book and
its registered PDF.

## 8. A complete minimal example

The builder `Revision/textbook/notebooks/src/02z_square_numbers.py` (an example only; it is not
part of the book):

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "02z",
    "name": "02z_square_numbers",
    "title": "Square numbers",
    "purpose": "It computes the squares of 1 to 10, checks the formula for their sum "
               "and draws them.",
    "records": [],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 5,
    "timeout_seconds": 60,
    "files_written": [
        "Revision/textbook/figures/02z.captions.json",
        "Revision/textbook/figures/02z_1_squares.png",
    ],
    "final_lines": ["PASS the sum of the squares", "ALL 1 CHECKS PASSED (notebook 02z)"],
    "troubleshooting": [],
}

CELLS = [
    md("""
    ## 1. What this notebook computes

    The squares $1, 4, 9, \\dots, 100$ and their sum.
    """),
    md("""
    ## 3. The words used in this notebook

    - **Square**: a number times itself, $n^2 = n \\cdot n$.
    """),
    md("""
    ## 4. The physical and mathematical situation

    The sum of the first $N$ squares is $N(N+1)(2N+1)/6$.
    """),
    md("""
    ## 5. The squares

    The next cell computes the squares, checks their sum and draws them.
    """),
    code(r'''
    import numpy as np

    n = np.arange(1, 11)  # the numbers 1, 2, ..., 10
    squares = n ** 2
    report("sum of the squares of 1 to 10", int(squares.sum()))
    fig, ax = plt.subplots()
    ax.plot(n, squares, "o-")
    ax.set_xlabel("$n$")
    ax.set_ylabel("$n^2$")
    save_figure(fig, "squares", "The squares $n^2$ of the numbers $n = 1$ to $10$; "
                "horizontal axis $n$, vertical axis $n^2$ (pure numbers). The points lie "
                "on a parabola.")
    check(int(squares.sum()) == 10 * 11 * 21 // 6, "the sum of the squares")
    all_checks_passed()
    '''),
    md("""
    ## 6. What this notebook showed

    The sum of the squares of 1 to 10 is 385, as the formula says.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
```

Then `python Revision/textbook/notebooks/src/02z_square_numbers.py build --date 2026-10-02
--scratch DIR`, and in chapter 02 the marker line, followed by the section
`### 2.M Line-by-line walk-through of Notebook 02z`. The working pilot of the whole chain is
Notebook 00a (`notebooks/src/00a_check_installation.py`) and chapter 00.

## chapter23/ - regenerating chapter 23

Chapter 23 ("Reproducing everything") is generated, not written by hand: `generate_chapter.py` renders `ch23.template.md`
(+ `fills.json`) with the code cells and the printed numbers of the stored Notebook 23a and its data files
(`Revision/textbook/data/23a_*.csv`), and `extract.py`, `group.py`, `build.py` and `splice.py` rebuild its glossary from the
definitions of every chapter and the notebooks' "words used" sections (`exclude.txt`, `manual.json`).  Edit the TEMPLATE, never
the chapter above its glossary.  Commands (repository root):

```text
python Revision/textbook/tools/chapter23/run_all.py --check   # byte-for-byte comparison, writes nothing in the chapter
python Revision/textbook/tools/chapter23/run_all.py           # rewrite the chapter
```

Notebook 23a reads the recorded check of every other notebook, so it is rebuilt LAST (after every other notebook), then
`run_all.py`, then `check_chapter.py` on chapter 23.  Intermediate files go to `build/chapter23/` (git-ignored).
