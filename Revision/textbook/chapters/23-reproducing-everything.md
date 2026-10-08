## 23. Reproducing everything

### 23.1 What this chapter does

Every result of this book comes from a file that a program wrote, and every one of those programs can be run again. This chapter gives every command that reproduces the book and the Revision record behind it, in the order in which they depend on each other, for Windows 11 (PowerShell), macOS (zsh) and Linux (bash). For each command it says what the command runs, what it prints when it works, how long it took on the development machine (Windows 11, 24 processor threads), and what to do when it fails. Every time quoted here is a MEASURED time read from a provenance file, from the step table of the Revision gate, or from a run made for this chapter on 2026-10-08, and it is labelled as measured or expected; on another computer the times differ, the results do not.

The chapter's example, Notebook 23a, is the bookkeeping of the whole book. By default it READS the recorded checks of the other 90 notebooks from their provenance files; it does NOT re-run them. It prints a table of every notebook, draws the run times, reads the step table of the Revision gate, and builds the index of every check of every report of the Revision record together with the chapters that cite it. With the environment variable `BOOK_RERUN_ALL` set to `1` it also re-runs every other notebook (Section 23.9 gives its measured time and the commands). The chapter ends with the two indexes of the book (Sections 23.13 and 23.14) and with the glossary.

### 23.2 The words of this chapter

- **Command**: one line typed into a terminal and run by pressing Enter. A **terminal** is the window in which commands are typed: on Windows the app Windows PowerShell or Terminal, on macOS the app Terminal (its shell is zsh), on Linux any terminal (its shell is bash).
- **Repository**: the folder Dirac_claude with every file of this project, downloaded with the program Git. The **repository root** is that folder itself; every command of this chapter is typed there.
- **Verifier** and **checker**: a program of the Revision record that recomputes a result (exactly, with Wolfram or with sympy, or numerically, with Rust or Python) and writes a **report**: a JSON file that lists named **checks**, each with a **verdict** such as PASS.
- **Gate**: the script `Revision/verify_revision.sh` (for bash) and its twin `Revision/verify_revision.ps1` (for PowerShell 7). It re-runs every verifier and checker in **dependency order** (a program that reads the output of another runs after it), then demands that every committed output is unchanged byte for byte and that every report passes.
- **Step**: one command of the gate, with a name such as `algebra-wolfram`. A **long step** is one documented as longer than 5 minutes.
- **Builder**: the Python file `Revision/textbook/notebooks/src/NNx_name.py` from which the tool `nbkit` builds Notebook NNx.
- **nbkit check**: re-executing a notebook into a scratch folder and comparing the result byte for byte with the stored notebook, its files and its provenance file. A **scratch folder** is a folder for throw-away files.
- **Provenance file**: `NNx_name.PROVENANCE.md`, next to each notebook. Its last line records the measured facts of the notebook's last verified run, among them the date, result and seconds of its last nbkit check.
- **Assembly**: joining the 24 chapter files, with every notebook expanded, into the one file `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md`.
- **Wall time**: the time a clock on the wall shows between the start and the end of a command.
- **Environment variable**: a named piece of text that a terminal hands to every program it starts.

### 23.3 What you need, and the set-up in every new terminal

The notebooks need Git and Python 3.12 or newer with the nine pinned packages; the run-instruction section before every notebook of this book gives the complete installation for the three systems, and the installation commands are repeated here so that this chapter can be followed on its own. Install Git and Python as described there, then download the repository, create the private environment `dirac-book-env` and install the packages:

Windows (PowerShell):

```text
cd $HOME
git clone https://github.com/once-ere/Dirac_claude.git
py -3 -m venv "$HOME\dirac-book-env"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
& "$HOME\dirac-book-env\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install numpy==2.4.6 sympy==1.14.0 mpmath==1.3.0 matplotlib==3.11.0
python -m pip install jupyterlab==4.4.10 nbformat==5.10.4 nbclient==0.10.2
python -m pip install ipykernel==7.1.0 nbconvert==7.16.6
```

macOS (zsh) and Linux (bash):

```text
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
python3 -m venv ~/dirac-book-env
source ~/dirac-book-env/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy==2.4.6 sympy==1.14.0 mpmath==1.3.0 matplotlib==3.11.0
python -m pip install jupyterlab==4.4.10 nbformat==5.10.4 nbclient==0.10.2
python -m pip install ipykernel==7.1.0 nbconvert==7.16.6
```

In every new terminal, activate the environment and go to the repository root before any command of this chapter:

Windows (PowerShell):

```text
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
& "$HOME\dirac-book-env\Scripts\Activate.ps1"
cd "$HOME\Dirac_claude"
```

macOS (zsh) and Linux (bash):

```text
source ~/dirac-book-env/bin/activate
cd ~/Dirac_claude
```

The Revision gate needs four more programs, which the notebooks do not need.

- **Rust** (the command `cargo`), for the Rust programs of the GKD and Kohn-Sham records and for the notebooks that run them: install it from https://rustup.rs and open a new terminal.
- **WolframScript** (the command `wolframscript`), for the exact Wolfram verifiers. It must be installed AND activated by you, with your own Wolfram licence; the gate never activates it.
- **pdflatex**, for the six documents of the Revision record and for the book's PDF: on Windows MiKTeX (https://miktex.org), on macOS MacTeX (https://tug.org/mactex), on Linux the TeX Live packages of your distribution.
- On Windows, **PowerShell 7** (the command `pwsh`), from https://aka.ms/powershell, for the PowerShell twin of the gate; Git for Windows also brings bash, so the bash form of the gate works there too.

### 23.4 The order of everything

The five stages below must be run in this order, because each reads what the stages before it wrote and checked.

1. The Revision record: the gate re-runs every verifier and checker (Section 23.5).
2. The notebooks of the book: each nbkit check re-executes one notebook (Section 23.6). The notebooks read the committed Revision record, so they come after it.
3. Notebook 23a: it reads the provenance files of all other notebooks and the reports of the Revision record, so it comes after both (Sections 23.9 to 23.12).
4. The assembly of the book from its chapters and notebooks (Section 23.7).
5. The PDF of the book, built from the assembled file (Section 23.7).

Stages 1 and 2 only VERIFY: they change no committed file when everything agrees. Stages 4 and 5 rewrite the book's files; run them only when you have changed a chapter or a notebook.

### 23.5 Stage 1: the Revision gate, step by step

First look at what the gate would do, without running anything. The option dry-run prints every selected step with its expected wall time and its command, and the last line `revision_verification=NOT-RUN`:

Windows (PowerShell 7):

```text
pwsh -NoProfile -File Revision/verify_revision.ps1 --dry-run
```

macOS (zsh), Linux (bash), and Git Bash on Windows:

```text
bash Revision/verify_revision.sh --dry-run
```

The full gate is the same command without any option; the fast option skips the long steps; the option steps runs only the named steps (the two audits `committed-unchanged` and `reports-pass` always run):

```text
bash Revision/verify_revision.sh
bash Revision/verify_revision.sh --fast
bash Revision/verify_revision.sh --steps algebra-wolfram,algebra-sympy
pwsh -NoProfile -File Revision/verify_revision.ps1
pwsh -NoProfile -File Revision/verify_revision.ps1 --fast
pwsh -NoProfile -File Revision/verify_revision.ps1 --steps algebra-wolfram,algebra-sympy
```

**What it runs.** Notebook 23a prints the gate's complete step table in Out [9] of Section 23.11, one line per step with its expected wall time and the program it runs, and draws it as Figure 23a.6. In order, the 63 steps are these groups.

- **The algebra** (2 steps, expected 10 s and 5 s): the author's gamma matrices, C, Gamma and B, exactly with Wolfram (`verify_algebra.wls`) and with sympy (`check_algebra.py`); Chapters 4 and 5.
- **GKD and the Lovelock tensors** (10 steps): the Rust program `lovelock_gkd` is built (60 s), computes the curvature and the three Lovelock tensors (15 s) and runs its exhaustive self-test (900 s, long); Wolfram (110 s) and sympy (30 s) verify the result; four steps read the author's notebook and one compares it with the record (10 s, 5 s, 10 s, 120 s, 60 s); Chapter 11.
- **The field theory** (5 steps): the Lagrangians, field equations, energy-momentum tensor and quantisation with Wolfram (2700 s, long, the longest step) and sympy (240 s), the scope checks with Wolfram (60 s) and sympy (5 s), and a comparison of the two (2 s); Chapters 6 to 10.
- **The pairing theorems** (2 steps): Wolfram (280 s) and sympy (240 s); Chapter 18.
- **The a4 equations** (5 steps): Wolfram (70 s) and sympy (30 s), the Kohn-Sham source conditions (5 s), the a4 equations with the Kohn-Sham source (20 s) and its unit tests (30 s); Chapters 12 and 17.
- **The Kohn-Sham record** (13 steps): the theory with Wolfram and sympy (60 s each); the Rust solver built and tested (60 s each); the canonical matrix (250 s), the Mermin roots (30 s), a repeat run (250 s) and its byte comparison (5 s), a refined run (620 s, long) and the determinism report (30 s, long because it needs the refined run); the Python reference solver (750 s, long), the refinement measurement (90 s) and the cross-check (780 s, long); Chapters 14 to 16.
- **T3 and its completion** (6 steps): Wolfram (15 s, 20 s) and sympy (10 s, 10 s), and the two numerical demonstrations with the Rust solver (900 s, long) and the reference solver (600 s, long); Chapter 19.
- **The dark sector** (7 steps): four for dirac16complex (10 s, 150 s, 5 s, 180 s) and three for dirac16complex00 (30 s each); Chapter 22.
- **The lead's checks** (3 steps): the energy-momentum divergence (10 s), Einstein-Gauss-Bonnet (20 s) and the charge-conjugation matrices with the local U(1) law (15 s); Chapters 9, 12 and 21.
- **The Revision notebooks** (1 step, 90 s): every notebook of `Revision/notebooks` is audited and checked.
- **The six documents** (6 steps, 30 s each): each PDF is rebuilt in verify mode.
- **The audits** (3 steps): `committed-unchanged` (10 s) demands that no committed output changed; `reports-pass` (5 s) reads every report of the step table and demands that every check passes; `unit-tests` (150 s) runs the Revision unit tests, except the textbook test, which has its own build.

**How long it takes.** Out [9] adds up the step table: the expected wall time of the full gate is 10532 s, that is 2.93 hours, of which the 8 long steps take most (Figure 23a.6); with the fast option the expected times add up to 3252 s (54.2 minutes). The README of the Revision record states the MEASURED time of the fast option on 2026-10-08 as about 20 minutes (most steps ran faster than the expected times of the table) and expects about 3 hours for the full gate.

**What it prints when it works.** First the tools it found (`revision_tool_python=...` and, when needed, cargo, wolframscript, git and pdflatex), then `revision_selected_steps=63 expected_seconds=10532 skipped_steps=0` (with the fast option: 55 steps, 3252 s, 8 skipped, each skipped step named on a line `revision_skipped_step=...`), then the precheck line `revision_output_paths=... preexisting_changes=0`. For every step it prints `revision_step=NAME expected_seconds=N`, the step's own output, `revision_step_seconds=NAME n (expected N)` and `revision_step_ok=NAME`. The step `reports-pass` prints one line `revision_report=PATH checks=k/k passed` per report. The last two lines are `revision_gate_seconds=...` and

```text
revision_verification=OK
```

Every step's complete output is also written to a log file `build/logs/revision/STEP-bash.log` (or `STEP-pwsh.log`); the folder `build/` is ignored by Git.

**When it fails.** The gate stops at the first failing step and prints `revision_failed_step=NAME`, `revision_failed_log=PATH` and `revision_verification=FAILED`. Open the log file it names and read its last lines. The most likely causes:

- `revision_failed_step=tools` with "wolframscript was not found", "cargo was not found" or "pdflatex was not found": install the program (Section 23.3), open a new terminal and run the gate again; for WolframScript, also activate it with your licence.
- A Wolfram step whose log shows a licence or kernel-limit message: the gate retries it after 30 s, at most 3 times; if it still fails, close other Wolfram sessions and run that step alone with the option steps.
- `revision_failed_step=precheck`: an output file of a selected step already differs from the committed version, and the gate refuses to overwrite your work. Run it in a fresh clone of the repository, or leave those steps out with the option steps.
- `revision_failed_step=committed-unchanged`: a verifier wrote an output that differs from the committed one; the lines `revision_changed_output=PATH` name the files. Run `git diff` on them to see the difference; this is a real disagreement with the record and must be reported, not hidden.

### 23.6 Stage 2: every notebook of the book

One command checks all notebooks of one chapter. The first line of each pair below names the folder of the builders; the second runs nbkit check on the builders of chapter 00 into the scratch folder `book-check` in your home folder. For another chapter, replace `00` by its two-digit number, `01` to `23`.

Windows (PowerShell):

```text
$builders = (Get-ChildItem Revision/textbook/notebooks/src/00*.py).FullName
python Revision/textbook/tools/nbkit.py check $builders --scratch "$HOME\book-check"
```

macOS (zsh) and Linux (bash):

```text
src=Revision/textbook/notebooks/src
python Revision/textbook/tools/nbkit.py check $src/00*.py --scratch ~/book-check
```

To check every notebook of the book, one after the other, give the folder itself:

Windows (PowerShell):

```text
$src = "Revision/textbook/notebooks/src"
python Revision/textbook/tools/nbkit.py check $src --scratch "$HOME\book-check"
```

macOS (zsh) and Linux (bash):

```text
src=Revision/textbook/notebooks/src
python Revision/textbook/tools/nbkit.py check $src --scratch ~/book-check
```

**What it prints when it works.** For each notebook NNx four lines, for example for the first notebook

```text
check_00a_compared_files=3
check_00a_seconds=3.6
check_00a_peak_mb=174.0
check_00a=PASSED
```

(the seconds and megabytes differ from run to run), and at the end `nbkit_seconds=...` and `nbkit=OK`. A check changes no file of the repository.

**How long it takes.** The recorded check times of the notebooks of each chapter, added up, are printed by Notebook 23a in Out [6] of Section 23.11 and drawn in Figure 23a.5. On the development machine chapter 11 is the slowest, 385.1 s, almost all of it Notebook 11a (348.5 s, which runs the Rust GKD program on large cases); chapters 14, 15 and 16 take 135.1 s, 147.3 s and 152.1 s; every other chapter takes between 13.2 s (chapter 9) and 86.5 s (chapter 8). All 90 notebooks of chapters 0 to 22 take 1446.0 s, about 24 minutes, one after the other (Out [6]); Notebook 23a adds about 5 s. The seven notebooks that run a Rust program (11a, 11b, 15a, 15b, 15d, 16a and 19a) build it with cargo the first time, which takes a few minutes more.

**When it fails.** A failed check prints `check_NNx=FAILED` and, before it, lines that start with `problem=`. The most likely causes:

- A problem line saying that the notebook differs from the stored one: the new execution printed something else than the stored one. The new notebook is in the scratch folder, in the subfolder named after the notebook; compare it with the stored one (the line after the problem shows the first difference). A different package version is the usual cause: install exactly the pinned versions (Section 23.3).
- `cargo was not found`: install Rust (Section 23.3) and open a new terminal.
- A problem line saying that the provenance file differs from the provenance regenerated from its own record: someone edited the provenance file by hand or rebuilt the notebook without its provenance; rebuild the notebook with `nbkit.py build` and the date of the verified execution.

### 23.7 Stages 4 and 5: assembling the book and building its PDF

The assembler checks the whole book and compares it with the stored file, without writing anything, with the first command below; the second command writes the book's Markdown file `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md`. The commands are the same in PowerShell, zsh and bash:

```text
python Revision/textbook/tools/assemble_textbook.py --check
python Revision/textbook/tools/assemble_textbook.py
```

It checks every rule of the book's format: every reference "Chapter N" and "Section N.M" resolves, no section number repeats, every notebook marker resolves to an executed notebook and is preceded by its run instructions, every figure file exists, every code line fits. It prints one line `check_NAME=true` per check, then the measurements (`measurement_chapters=24`, the numbers of sections, notebooks, figures and lines, `measurement_pages=...`), `failed_check_count=0`, `output=...` and finally `textbook_assembly=OK`. A failed check prints `problem=...` lines that name the chapter, the reference or the file, and the last line `textbook_assembly=FAILED`. On the development machine the check took about 4 seconds (measured 2026-10-08).

The PDF is built from the assembled file with one command. In PowerShell, the first three lines put the parts of the command into variables (a list of texts after `=` is passed to the program as separate words), and the fourth runs it; in zsh and bash, the backslash at the end of a line continues the command on the next line:

Windows (PowerShell):

```text
$book = "Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md"
$layout = "--developer-layout", "--number-sections-from-zero", "--wide-page-numbers"
$more = "--specifications", "Revision/pdf-specifications.json", "--date", "October 2026"
python scripts/build_provenance_pdf.py $book $layout $more
```

macOS (zsh) and Linux (bash):

```text
python scripts/build_provenance_pdf.py Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md \
    --developer-layout --number-sections-from-zero --wide-page-numbers \
    --specifications Revision/pdf-specifications.json --date "October 2026"
```

Without further options it builds in VERIFY mode: it builds the PDF twice, demands that the two builds are byte for byte identical and that pdflatex printed no warning, and compares the result with the edition `universes-in-pairs-textbook` registered in `Revision/pdf-specifications.json` (6082 pages). With the option register added at the end it records a changed book as the new edition. It needs pdflatex. When it works it prints one line `check_NAME=true` per check, the measurements (among them the page count), `failed_check_count=0` and the last line `provenance_pdf=OK`; any LaTeX warning (an overfull line, a figure too large for a page) is printed and fails the build, and the message names the line of the `.tex` file, which belongs to the chapter text at the same place.

To try the PDF build without touching the registered book, `check_chapter.py` builds one chapter, or with the option book all chapters, into a scratch folder with a throw-away copy of the registry:

Windows (PowerShell):

```text
$chapter = "Revision/textbook/chapters/23-reproducing-everything.md"
python Revision/textbook/tools/check_chapter.py $chapter --scratch "$HOME\book-pdf"
python Revision/textbook/tools/check_chapter.py --book --scratch "$HOME\book-pdf"
```

macOS (zsh) and Linux (bash):

```text
chapter=Revision/textbook/chapters/23-reproducing-everything.md
python Revision/textbook/tools/check_chapter.py $chapter --scratch ~/book-pdf
python Revision/textbook/tools/check_chapter.py --book --scratch ~/book-pdf
```

It prints `chapter_check=OK` when the chapter builds without any problem and warning. A test build of the whole book made in this way on 2026-10-08, with the chapters as they stood that day, took 287 s for its first pass (two complete pdflatex builds of a book of 6289 pages, compared byte for byte); the second, verify pass repeats the builds.

### 23.8 What to do when something fails: the general rules

1. Read the LAST lines first: every tool of this chapter ends with one line that says OK or FAILED, and the lines just before it say why.
2. Make sure the environment is active (the prompt starts with `(dirac-book-env)`) and that you are in the repository root; most "file not found" messages come from a terminal in another folder.
3. Install exactly the pinned versions; a newer matplotlib draws a figure with different bytes, and a byte comparison then fails although the physics is the same.
4. Run the failing piece alone: one gate step with the option steps, one notebook with one nbkit check.
5. Never "fix" a failure by editing a report, a provenance file or a stored notebook by hand. A difference between a fresh run and the record is a finding; report it.

### 23.9 Example: the bookkeeping of the whole book (Notebook 23a)

Notebook 23a collects in one place what the other notebooks and the Revision record have recorded. By default it re-runs nothing: every table and figure it shows is read from files. It reads the provenance file of every other notebook and prints a table of all 90 with their checks, figures, last recorded check and section of the book; it adds them up per chapter and draws five figures of the counts and times; it reads the step table of the gate and draws its expected times; and it builds the index of the 1208 checks of the 39 reports of the Revision record, with the chapters that cite each, and writes it to a data file. With `BOOK_RERUN_ALL=1` its thirteenth part, "Re-running every notebook", re-runs the nbkit check of every other notebook, at most 8 at a time and the slowest first, into a scratch folder in the system's temporary folder, and prints the fresh results per chapter. On the development machine (24 threads, so 8 notebooks at a time) that re-run took 406 s of wall time on 2026-10-08 (the whole notebook, run headless, 414 s), and all 90 notebooks passed. To run it, set the variable in the terminal and run the notebook headless, writing the executed copy into the folder `book-rerun` of your home folder (so that the stored notebook is not overwritten); afterwards remove the variable again:

Windows (PowerShell):

```text
$nb = "Revision/textbook/notebooks/23a_reproduce_everything.ipynb"
$options = "--to", "notebook", "--execute", "--ExecutePreprocessor.timeout=3600"
$env:BOOK_RERUN_ALL = "1"
python -m nbconvert $options --output-dir "$HOME\book-rerun" $nb
Remove-Item Env:BOOK_RERUN_ALL
```

macOS (zsh) and Linux (bash):

```text
nb=Revision/textbook/notebooks/23a_reproduce_everything.ipynb
BOOK_RERUN_ALL=1 python -m nbconvert --to notebook --execute \
    --ExecutePreprocessor.timeout=3600 --output-dir ~/book-rerun $nb
```

(In zsh and bash, a variable written before a command on the same line holds only for that command.) It prints `[NbConvertApp] Writing ... bytes to ...`; the fresh table is in the executed copy, which you open in JupyterLab, and in the file `fresh_results.csv` whose path the notebook prints. To use JupyterLab directly instead, set the variable in the terminal first and then start JupyterLab from that same terminal.

<!-- NOTEBOOK 23a -->

### 23.12 Line-by-line walk-through of Notebook 23a

**In [1], the set-up cell.** It is the set-up cell of every notebook of this book, with the name `"23a"`. Its comment lines repeat the run instructions of Section 23.10. Its code finds the repository folder (`REPO`), decides where files are written (`OUTPUT_ROOT`: the repository, or a scratch folder during an nbkit check), and defines the helpers the later cells use: `repository_file(relative)` gives the path of a repository file for reading; `output_file(relative)` the path at which to write one; `say(text)` prints in lines of at most 89 characters; `save_figure(fig, name, caption)` saves a figure as `Revision/textbook/figures/23a_<k>_<name>.png`, records its caption in the dictionary `CAPTIONS` and the file `CAPTION_FILE`, shows it and prints where it was saved; `check(condition, name, record)` stops the notebook if the condition is false and otherwise prints PASS with the name (and a second line naming the Revision record when `record` is given); `report(label, value, unit)` prints a line RESULT label = value unit; `all_checks_passed()` prints the last line. `FIGURE_FOLDER` is `"Revision/textbook/figures"` and `NOTEBOOK_ID` is `"23a"`. The modules `json`, `os` and `Path` and the plotting module `plt` are imported there.

**In [2], the provenance records.**

```python
import csv  # reads and writes comma-separated tables
import re  # regular expressions: patterns that find pieces of text
```

Two modules of Python's standard library: `csv` reads and writes tables in which each line is a row and the cells are separated by commas; `re` provides **regular expressions**, patterns that describe pieces of text to be found.

```python
NOTEBOOKS = repository_file("Revision/textbook/notebooks")  # notebooks and records
RECORD = re.compile(r"nbkit-record (\{.*\}) -->")  # the record line
ALL_LINE = re.compile(r"ALL (\d+) CHECKS PASSED")  # the last line of a notebook
TITLE = re.compile(r"^# Provenance of Notebook \w+: (.+)$", re.MULTILINE)
```

`NOTEBOOKS` is the folder of the notebooks and their provenance files. `re.compile` turns a pattern into an object that can search text. In a pattern, `\{` and `\}` are the braces themselves, `.*` means "any characters", and the round brackets mark the piece to be returned: `RECORD` finds the record line and returns its JSON text; `\d+` means "one or more digits", so `ALL_LINE` finds the line `ALL n CHECKS PASSED` and returns n; `\w+` means "one or more letters or digits", `^` and `$` mean the start and the end of a line (with `re.MULTILINE`, of any line), so `TITLE` returns the title from the first line of a provenance file. The `r` before a string makes Python keep every backslash as it is.

```python
def by_name(paths):
    """Sort paths by their repository-relative name, the same on every system."""
    return sorted(paths, key=lambda path: path.relative_to(REPO).as_posix())
```

`by_name` sorts a list of paths by their names relative to the repository, written with forward slashes. `lambda path: ...` is a small function without a name that gives each path its sorting key. Sorting by this text gives the same order on Windows, macOS and Linux, so that the printed tables never depend on the computer.

```python
ROWS = []  # one dictionary per notebook
for path in by_name(NOTEBOOKS.glob("*.PROVENANCE.md")):
    name = path.name.removesuffix(".PROVENANCE.md")  # e.g. 00a_check_installation
    if name.startswith(NOTEBOOK_ID):
        continue  # this notebook's own record changes whenever it is built
```

`ROWS` starts as an empty list. The loop visits every file whose name ends in `.PROVENANCE.md`, in name order. `removesuffix` cuts the ending off the name, leaving for example `00a_check_installation`. `continue` jumps to the next file when the name starts with `"23a"`: this notebook's own record changes every time it is built, so it cannot list itself.

```python
    text = path.read_text(encoding="utf-8")
    record = json.loads(RECORD.search(text).group(1))
    captions = json.loads(repository_file(
        f"{FIGURE_FOLDER}/{name[:3]}.captions.json").read_text(encoding="utf-8"))
    ROWS.append({"id": name[:3], "chapter": int(name[:2]), "name": name,
                 "title": TITLE.search(text).group(1),
                 "checks": int(ALL_LINE.search(text).group(1)),
                 "figures": len(captions), "figure_files": sorted(captions),
                 "date": record["check"]["date"],
                 "result": record["check"]["result"],
                 "seconds": record["check"]["seconds"],
                 "builder": f"Revision/textbook/notebooks/src/{name}.py"})
```

The file is read as text; `RECORD.search(text).group(1)` is the JSON text of the record line, and `json.loads` turns it into a dictionary. The caption file of the notebook, `Revision/textbook/figures/NNx.captions.json`, holds one entry per figure; `name[:3]` is the id (the first three characters). `ROWS.append` adds one dictionary per notebook: the id, the chapter number (`int` turns the text `"05"` into the number 5), the name, the title, the number of checks, the number of figures and the sorted list of figure files, the date, result and seconds of the last recorded check (`record["check"]`), and the path of the builder.

```python
builders = [path.stem for path in by_name(NOTEBOOKS.glob("src/*.py"))
            if not path.stem.startswith(NOTEBOOK_ID)]
say(f"{len(ROWS)} provenance files read, {len(builders)} builders found.")
```

`builders` lists the names of the builder files (`path.stem` is a file name without its ending `.py`), again without this notebook. The line printed by `say` is the first line of Out [2]: 90 provenance files and 90 builders.

```python
check([row["name"] for row in ROWS] == builders,
      "every builder has a provenance file and every provenance file a builder")
check(all(row["result"] == "passed" for row in ROWS),
      "the last recorded nbkit check of every notebook passed")
check(all(repository_file(f"{FIGURE_FOLDER}/{figure}").is_file()
          for row in ROWS for figure in row["figure_files"]),
      "every figure named in a caption file exists")
```

Three checks. The first compares the two lists of names: every builder has a provenance file and every provenance file a builder, in the same order. The second demands that every recorded check passed (`all` is true when the condition holds for every row). The third demands that every figure named in a caption file exists. Each prints a PASS line in Out [2].

**In [3], where each notebook is printed.**

```python
CHAPTERS = [path for path in by_name(repository_file("Revision/textbook/chapters")
                                     .glob("[0-9][0-9]-*.md"))
            if int(path.name[:2]) <= 22]  # the chapter files 00 to 22
HEADING = re.compile(r"^### (\d+)\.(\d+) ")  # a section heading such as ### 3.4
MARKER = re.compile(r"^<!-{2} NOTEBOOK (\w+) -->$")  # a notebook marker line
PLACED = {}  # notebook id -> list of (chapter file name, section of its instructions)
```

`CHAPTERS` is the list of the chapter files of chapters 0 to 22 (`[0-9][0-9]-*.md` matches every file name that starts with two digits and a hyphen and ends in `.md`; the condition `int(path.name[:2]) <= 22` leaves out this chapter 23, so that its own text cannot change the results). `HEADING` finds a section heading such as `### 3.4` and returns its two numbers. `MARKER` finds a notebook marker line and returns the id; `-{2}` means "the character - two times", which lets the cell describe the marker without containing one. `PLACED` will hold, for each notebook id, the list of places where it is placed.

```python
for chapter in CHAPTERS:
    section = None
    for line in chapter.read_text(encoding="utf-8").splitlines():
        if HEADING.match(line):
            section = HEADING.match(line).groups()  # e.g. ("3", "4")
        elif MARKER.match(line):
            number = f"{section[0]}.{int(section[1]) + 1}"  # the next section
            PLACED.setdefault(MARKER.match(line).group(1), []).append(
                (chapter.name, number))
```

For each chapter, `section` remembers the last heading seen. Each line is tested: a heading updates `section` (`.groups()` returns the two numbers as texts); a marker records the chapter's file name and the section number one higher than the last heading, `N.(M+1)`, which is the number the assembler gives the notebook's run-instruction section. `setdefault` creates an empty list for an id seen for the first time.

```python
for row in ROWS:
    places = PLACED.get(row["id"], [])
    row["section"] = places[0][1] if len(places) == 1 else "?"
say(f"{len(CHAPTERS)} chapter files read, {len(PLACED)} notebook markers found.")
check(all(len(PLACED.get(row["id"], [])) == 1
          and PLACED[row["id"]][0][0].startswith(row["id"][:2] + "-")
          for row in ROWS),
      "every notebook is placed exactly once, in the chapter of its number")
```

Each row receives its section, or `"?"` when the notebook is not placed exactly once. The printed line is Out [3]: 23 chapter files and 90 markers. The check demands that each notebook has exactly one marker and that the marker is in the chapter file whose name starts with the notebook's own two digits.

**In [4], the table, chapters 0 to 10.**

```python
def show_table(first, last):
    print("id  title                              checks figs checked    result "
          "   sec section")
    for row in ROWS:
        if first <= row["chapter"] <= last:
            title = row["title"]
            if len(title) > 34:
                title = title[:31] + "..."
            print(f"{row["id"]:3} {title:34} {row["checks"]:6d} {row["figures"]:4d} "
                  f"{row["date"]:10} {row["result"]:6} {row["seconds"]:6.1f} "
                  f"{row["section"]:>7}")
```

`show_table(first, last)` prints a header line and then one line per notebook of the chapters `first` to `last`. A title longer than 34 characters is cut to 31 characters and three dots. In an **f-string** (a string with `f` before it) every `{...}` is replaced by the value inside; after the colon, `:3` and `:34` fill the value to that width, `:6d` writes a whole number in 6 places, `:6.1f` a number with one decimal in 6 places, and `:>7` puts the text at the right end of 7 places.

```python
show_table(0, 10)
```

prints the first part of the table, Out [4]: the 50 notebooks of chapters 0 to 10. The last column is the section of the run instructions; for example Notebook 05c is placed in Section 5.31, and its complete text is Section 5.32.

**In [5], the table, chapters 11 to 22, and the data file.**

```python
show_table(11, 22)
COLUMNS = ["id", "chapter", "title", "checks", "figures", "date", "result",
           "seconds", "section", "builder"]
NOTEBOOK_TABLE = "Revision/textbook/data/23a_notebooks.csv"
```

The second part of the table is printed (Out [5], 40 notebooks). `COLUMNS` names the columns of the data file, and `NOTEBOOK_TABLE` its path.

```python
with output_file(NOTEBOOK_TABLE).open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(COLUMNS)
    writer.writerows([row[column] for column in COLUMNS] for row in ROWS)
say(f"The table of {len(ROWS)} notebooks was written to {NOTEBOOK_TABLE}.")
```

`with ... as handle` opens the file for writing (`"w"`) and closes it at the end of the indented block; `newline=""` and `lineterminator="\n"` make every line end with a single line-feed character on every system. `writer.writerow` writes the header and `writer.writerows` one row per notebook, each the list of the values of the columns. The last line prints where the table was written.

**In [6], the totals per chapter.**

```python
PER_CHAPTER = {}  # chapter number -> its totals
for row in ROWS:
    total = PER_CHAPTER.setdefault(row["chapter"], {"notebooks": 0, "checks": 0,
                                                    "figures": 0, "seconds": 0.0})
    total["notebooks"] += 1
    total["checks"] += row["checks"]
    total["figures"] += row["figures"]
    total["seconds"] += row["seconds"]
```

`PER_CHAPTER` gets, for each chapter, a dictionary of four totals, created with zeros the first time the chapter appears (`setdefault`). `+=` adds the row's value to the total.

```python
print("chapter notebooks checks figures  seconds")
for chapter, total in sorted(PER_CHAPTER.items()):
    print(f"{chapter:7d} {total["notebooks"]:9d} {total["checks"]:6d} "
          f"{total["figures"]:7d} {total["seconds"]:8.1f}")
```

The header and one line per chapter, in chapter order (`sorted` sorts the pairs of the dictionary by the chapter number). This is the table of Out [6].

```python
ALL_SECONDS = sum(row["seconds"] for row in ROWS)
report("notebooks (without 23a)", len(ROWS))
report("checks in these notebooks", sum(row["checks"] for row in ROWS))
report("figures of these notebooks", sum(row["figures"] for row in ROWS))
report("recorded check time, one after the other", f"{ALL_SECONDS:.1f}", "s")
check(sorted(PER_CHAPTER) == list(range(23)),
      "every chapter 0 to 22 has at least one notebook")
```

`ALL_SECONDS` is the sum of all recorded check times. The four RESULT lines of Out [6]: 90 notebooks, 2236 checks, 563 figures and 1446.0 s, the time of all checks one after the other. The check demands that the chapter numbers are exactly 0 to 22 (`list(range(23))` is the list 0, 1, ..., 22).

**In [7], two figures of the run times.**

```python
ids = [row["id"] for row in ROWS]
seconds = [row["seconds"] for row in ROWS]
fig, ax = plt.subplots(figsize=(12, 4.5))
ax.bar(range(len(ROWS)), seconds, color="#2a78d6")
ax.set_yscale("log")  # equal steps on the axis are equal factors
ax.set_xticks(range(len(ROWS)), ids, rotation=90, fontsize=6)
ax.set_xlim(-1, len(ROWS))
ax.set_xlabel("notebook")
ax.set_ylabel("recorded nbkit check time (s)")
ax.grid(axis="y", which="both", alpha=0.3)
```

`ids` and `seconds` are the ids and recorded times in book order. `plt.subplots(figsize=(12, 4.5))` makes a figure 12 inches wide and 4.5 inches high with one drawing area `ax`. `ax.bar` draws one bar per notebook at the positions 0, 1, 2, ...; `set_yscale("log")` makes the vertical axis logarithmic, so that 1 s, 10 s and 100 s are equally far apart; `set_xticks` writes the ids under the bars, turned by 90 degrees; `set_xlim` leaves half a bar of space at both ends; the two labels name the axes, and `grid` draws light horizontal lines.

```python
save_figure(fig, "check_time_per_notebook",
            "The wall time in seconds of the last recorded nbkit check of every "
            "notebook of chapters 0 to 22 (one bar each, in book order), on a "
            "logarithmic vertical axis. Most notebooks take a few seconds; a few, "
            "which run the Rust programs or long numerical scans, take minutes.")
```

`save_figure` saves the figure as Figure 23a.1 with the caption given. It shows that most notebooks take a few seconds and a few take minutes; the tallest bar is Notebook 11a.

```python
slowest = sorted(seconds, reverse=True)
shares = [100 * sum(slowest[:k]) / ALL_SECONDS for k in range(len(slowest) + 1)]
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(range(len(shares)), shares, color="#eb6834", marker="o", markersize=3)
ax.set_xlabel("number of notebooks, slowest first")
ax.set_ylabel("share of the total check time (%)")
ax.grid(alpha=0.3)
```

`slowest` is the list of times sorted from the largest down (`reverse=True`). `shares[k]` is the percentage of the total time taken by the k slowest notebooks: `slowest[:k]` is the list of the first k entries, `sum` adds them, and the result is divided by `ALL_SECONDS` and multiplied by 100; `k` runs from 0 to 90, so `shares[0]` is 0 and `shares[90]` is 100. `ax.plot` draws the points joined by lines, with small circles (`marker="o"`).

```python
save_figure(fig, "cumulative_check_time",
...)
report("share of the three slowest notebooks", f"{shares[3]:.1f}", "%")
```

The figure is saved as Figure 23a.2, and the RESULT line of Out [7] gives `shares[3]`: the three slowest notebooks take 39.6 % of the whole time.

**In [8], checks, figures and time per chapter.**

```python
chapters = sorted(PER_CHAPTER)
for key, name, label, colour, caption in [
        ("checks", "checks_per_chapter", "checks", "#1baf7a",
...),
        ("figures", "figures_per_chapter", "figures", "#eda100",
...),
        ("seconds", "check_time_per_chapter", "recorded check time (s)", "#4a3aa7",
...)
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.bar(chapters, [PER_CHAPTER[chapter][key] for chapter in chapters],
           color=colour)
    ax.set_xticks(chapters)
    ax.set_xlabel("chapter")
    ax.set_ylabel(label)
    ax.grid(axis="y", alpha=0.3)
    save_figure(fig, name, caption)
```

`chapters` is the sorted list of chapter numbers. The loop goes through a list of three groups of five values; in each pass `key` is the total to draw (`"checks"`, `"figures"` or `"seconds"`), `name` the figure's file name, `label` the text of the vertical axis, `colour` the colour of the bars and `caption` the caption (the three captions are printed with the figures). Each pass draws one bar per chapter of the chosen total, writes every chapter number under the axis, labels the axes and saves the figure: Figures 23a.3, 23a.4 and 23a.5.

**In [9], the steps of the gate.**

```python
gate = repository_file("Revision/verify_revision.sh").read_text(encoding="utf-8")
table = gate.split("REVISION_GATE_STEPS")[1]  # the text between the two marks
STEPS = [line.split("|") for line in table.splitlines() if line.count("|") == 6]
```

The gate script is read as text. `gate.split("REVISION_GATE_STEPS")` cuts it at every appearance of that word; the piece with index 1 is the text between the first and the second appearance, which is the step table. `STEPS` keeps every line of it that has exactly six `|` characters, that is seven fields, split into a list of the seven fields.

```python
def short_command(command):
    """What a step runs: the script file for python and wolframscript, else the
    first two words of the command that are not options."""
    words = [word.strip("{}").rsplit("/", 1)[-1] for word in command.split()
             if not word.startswith("-")]
    if words[0] in ("python", "wolframscript"):
        return next(word for word in words[1:] if "." in word)
    return " ".join(words[:2])
```

`short_command` makes a short form of a step's command for the table. It splits the command into words (`split()`), leaves out the options (words that start with `-`), removes the braces of the placeholders such as `{python}`, and keeps of every path only the part after the last `/`. For a command run by `python` or `wolframscript` it returns the first later word with a `.` in it, the script file; `next` returns the first item of such a sequence. For any other command it returns the first two words, such as `cargo build`.

```python
print(f"{"step":33} {"sec":>5} {"kind":4} command")
for name, expected, kind, _, _, _, command in STEPS:
    mark = {"1": "long", "A": "all"}.get(kind, "")
    print(f"{name:33} {int(expected):5d} {mark:4} {short_command(command)}")
```

The header and one line per step: the seven fields are unpacked into seven names (`_` marks fields not used here); `mark` is `long` for kind `1`, `all` for kind `A` (the audits that always run) and empty otherwise. This is the table of Out [9].

```python
FULL = sum(int(step[1]) for step in STEPS)
FAST = sum(int(step[1]) for step in STEPS if step[2] != "1")
report("gate steps", len(STEPS))
report("long steps (skipped by --fast)", sum(step[2] == "1" for step in STEPS))
report("expected wall time of the full gate", f"{FULL} s = {FULL / 3600:.2f} h")
report("expected wall time with --fast", f"{FAST} s = {FAST / 60:.1f} min")
```

`FULL` adds up the expected seconds of all steps, `FAST` those of the steps that are not long. The RESULT lines of Out [9]: 63 steps, 8 of them long, 10532 s (2.93 h) for the full gate and 3252 s (54.2 min) with the fast option.

**In [10], the figure of the gate.**

```python
fig, ax = plt.subplots(figsize=(12, 5))
colours = ["#e34948" if step[2] == "1" else "#2a78d6" for step in STEPS]
ax.bar(range(len(STEPS)), [int(step[1]) for step in STEPS], color=colours)
ax.set_yscale("log")
ax.set_xticks(range(len(STEPS)), [step[0] for step in STEPS], rotation=90,
              fontsize=6)
ax.set_xlim(-1, len(STEPS))
ax.set_ylabel("expected wall time (s)")
ax.grid(axis="y", which="both", alpha=0.3)
```

`colours` gives each bar a colour: red (`"#e34948"`) for a long step, blue otherwise; the expression `A if condition else B` chooses between two values. The bars are the expected seconds on a logarithmic axis, with the step names written under them.

```python
save_figure(fig, "gate_step_times",
...)
```

saves Figure 23a.6.

**In [11], the reports of the Revision record.**

```python
def check_list(document):
    """The (name, verdict) pairs of a report, or [] if it is not a report."""
    if not isinstance(document, dict):
        return []
    checks, results = document.get("checks"), document.get("results")
    if isinstance(checks, list):
        return [(item["name"], str(item["verdict"]).upper()) for item in checks]
```

`check_list` turns a JSON document into a list of pairs (check name, verdict). `isinstance(document, dict)` asks whether the document is a dictionary; if not, it is not a report and the empty list is returned. `document.get("checks")` is the value stored under `checks`, or `None` if there is none. When `checks` is a list, each item is a dictionary with a `name` and a `verdict`; `str(...).upper()` writes the verdict in capital letters, so that `pass` and `PASS` count alike.

```python
    if isinstance(checks, dict) and all(isinstance(item, (bool, dict))
                                        for item in checks.values()):
        return [(name, "PASS" if item is True or (isinstance(item, dict) and (
            item.get("passed") is True or
            str(item.get("verdict", "")).upper() == "PASS")) else "FAIL")
            for name, item in checks.items()]
```

When `checks` is a dictionary whose values are all `True`/`False` or dictionaries, each entry is a named check: it is PASS when its value is `True`, or a dictionary with `passed` equal to `True` or with the verdict PASS; otherwise FAIL. (A dictionary of plain numbers, such as a summary `{"total": 13, "pass": 13}`, is not a list of checks and is skipped.)

```python
    if isinstance(results, list) and results and all(
            isinstance(item, dict) and "mismatches" in item for item in results):
        return [(", ".join(f"{key}={value}" for key, value in item.items()
                           if key != "mismatches"),
                 "PASS" if item["mismatches"] == 0 else "FAIL") for item in results]
    return []
```

The GKD self-test stores a list `results` of cases, each with a number of `mismatches`. Each case becomes a check named by its other entries (for example `p=1, mode=exhaustive, pairs=64`), PASS when it has no mismatch. Any other document gives the empty list.

```python
REPORTS = {}  # report path -> list of (check name, verdict)
for path in by_name(repository_file("Revision").rglob("*.json")):
    relative = path.relative_to(REPO).as_posix()
    if relative.startswith("Revision/textbook/") or "/target/" in relative:
        continue
    pairs = check_list(json.loads(path.read_text(encoding="utf-8")))
    if pairs:
        REPORTS[relative] = pairs
```

`rglob("*.json")` finds every JSON file in the folder `Revision` and all folders below it. Files of the textbook and of the Rust build folders (`target`) are skipped. Each file is read and turned into its list of checks; a file with at least one check is kept in `REPORTS`, under its repository path.

```python
gate_reports = {path for step in STEPS for path in step[5].split(",") if path != "-"}
say(f"{len(REPORTS)} reports found with {sum(map(len, REPORTS.values()))} checks; "
    f"the gate's step table names {len(gate_reports)} reports.")
check(gate_reports <= set(REPORTS),
      "every report named in the gate's step table is in the index")
check(all(verdict in ("PASS", "NOT-AVAILABLE")
          for pairs in REPORTS.values() for _, verdict in pairs),
      "every check of every report is PASS or NOT-AVAILABLE")
```

`gate_reports` is the set of the report paths named in the sixth field of the gate's steps (`"-"` means none). The printed line of Out [11]: 39 reports with 1208 checks, and the gate names 39 reports. The first check demands that every report of the gate is in the index (`<=` between two sets means "is contained in"); the second, that every verdict is PASS or NOT-AVAILABLE. NOT-AVAILABLE occurs only in the comparison with the author's notebook, for 5 outputs that the author's notebook does not store; this is the same rule as the gate's step `reports-pass`.

**In [12], the chapters that cite each check.**

```python
BLOCKS = {}  # chapter number -> its paragraphs and the outputs of its notebooks
for chapter in CHAPTERS:
    number = int(chapter.name[:2])  # the chapter number, e.g. 5
    text = chapter.read_text(encoding="utf-8")
    blocks = [block for block in re.split(r"\n\s*\n", text) if block.strip()]
```

For each chapter of 0 to 22, `BLOCKS` will hold a list of text blocks. `re.split(r"\n\s*\n", text)` cuts the chapter at every empty line (a line break, possibly blanks, another line break), giving its paragraphs; empty pieces are dropped.

```python
    for row in ROWS:
        if row["chapter"] == number:
            notebook = json.loads((NOTEBOOKS / f"{row["name"]}.ipynb").read_text(
                encoding="utf-8"))
            for cell in notebook["cells"]:
                outputs = [output.get("text", "") for output in cell.get("outputs", [])]
                blocks.append("".join("".join(item) for item in outputs))
    BLOCKS[number] = blocks
```

For each notebook of the chapter, the stored notebook file is read as JSON. A notebook is a dictionary whose entry `cells` is the list of its cells; a code cell has a list `outputs`, and a printed output has its text under `text` (a list of lines). The printed text of all outputs of one cell is joined into one block and added. `BLOCKS[number]` stores the chapter's blocks.

```python
CITED = {}  # (report, check name) -> set of chapter numbers
for number, blocks in BLOCKS.items():
    for block in blocks:
        for report_path, pairs in REPORTS.items():
            if report_path.rsplit("/", 1)[1] not in block:
                continue
            for check_name, _ in pairs:
                word = r"(?<![\w.-])" + re.escape(check_name) + r"(?![\w-])"
                if re.search(word, block):
                    CITED.setdefault((report_path, check_name), set()).add(number)
say(f"{len(CITED)} (report, check) pairs are cited by at least one chapter.")
```

For every block, every report whose file name (the part of its path after the last `/`) occurs in the block is examined, and each of its check names is searched for as a whole word: `re.escape` makes any special character of the name an ordinary character, and the two conditions `(?<![\w.-])` and `(?![\w-])` demand that the name is not part of a longer word (no letter, digit, `_`, `.` or `-` just before it, no letter, digit, `_` or `-` just after it). Each hit adds the chapter number to the set of the pair (report, check) in `CITED`. Out [12]: 711 pairs are cited at least once.

**In [13], the index of the checks.**

```python
print(f"{"report (under Revision/, without .json)":63} {"checks":>6} {"PASS":>4} "
      f"{"N/A":>3} {"cited":>5}")
INDEX = []  # one row per check: report, check, verdict, citing chapters
for report_path, pairs in REPORTS.items():
    for check_name, verdict in pairs:
        chapters = sorted(CITED.get((report_path, check_name), set()))
        INDEX.append([report_path, check_name, verdict,
                      " ".join(str(chapter) for chapter in chapters)])
    short = report_path.removeprefix("Revision/").removesuffix(".json")
    print(f"{short:63} {len(pairs):6d} "
          f"{sum(verdict == "PASS" for _, verdict in pairs):4d} "
          f"{sum(verdict == "NOT-AVAILABLE" for _, verdict in pairs):3d} "
          f"{sum((report_path, name) in CITED for name, _ in pairs):5d}")
```

The header, then for each report: one row per check is added to `INDEX`, with the citing chapters written as numbers separated by blanks; `short` is the report path without `Revision/` at the start (`removeprefix`) and without `.json` at the end; the printed line gives the numbers of checks, of PASS, of NOT-AVAILABLE and of cited checks (`sum` of true conditions counts them). This is the table of Out [13].

```python
CHECK_INDEX = "Revision/textbook/data/23a_check_index.csv"
with output_file(CHECK_INDEX).open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(["report", "check", "verdict", "cited_by_chapters"])
    writer.writerows(INDEX)
with output_file(CHECK_INDEX).open(encoding="utf-8", newline="") as handle:
    read_back = list(csv.reader(handle))
report("reports", len(REPORTS))
report("checks in the index", len(INDEX))
report("checks cited by at least one chapter", sum(bool(row[3]) for row in INDEX))
check(read_back[1:] == INDEX, "the index file holds exactly one row per check")
```

The index is written to the data file `Revision/textbook/data/23a_check_index.csv` with the header `report, check, verdict, cited_by_chapters`, then read back with `csv.reader`. The RESULT lines of Out [13]: 39 reports, 1208 checks, 711 of them cited by at least one chapter. The check demands that the rows read back, after the header (`read_back[1:]`), are exactly the rows written.

**In [14], one report as an example.**

```python
EXAMPLE = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
print(f"{"check":44} {"verdict":7} cited by chapters")
for report_path, check_name, verdict, chapters in INDEX:
    if report_path == EXAMPLE:
        print(f"{check_name:44} {verdict:7} {chapters or "-"}")
check(sum(row[0] == EXAMPLE for row in INDEX) == 12,
      "the example report holds 12 checks",
      record=f"{EXAMPLE}, all checks")
```

The rows of the report of the charge-conjugation matrices and the local U(1) law are printed with their citing chapters (`chapters or "-"` prints a dash when no chapter cites the check). Out [14] shows its 12 checks, all PASS, each cited by at least four chapters; the check `u1_noether_matrix_identity`, the exact local conservation law of Chapter 21, is cited by chapters 0, 5, 10, 18, 20, 21 and 22. The check demands that the report holds 12 checks, and its second line names the record it reproduces.

**In [15], the re-run of every notebook.**

```python
RERUN = os.environ.get("BOOK_RERUN_ALL") == "1"  # the switch of this section
if not RERUN:
    say("BOOK_RERUN_ALL is not set to 1, so no other notebook was re-run: every "
        "table and figure above shows the RECORDED results of the provenance files.")
```

`os.environ.get("BOOK_RERUN_ALL")` is the value of the environment variable, or `None` when it is not set; `RERUN` is true only when the value is the text `"1"`. When it is not, the cell prints the sentence of Out [15] and does nothing else; this is what happened when the stored notebook was built.

```python
else:
    import subprocess  # starts other programs
    import sys  # sys.executable is the Python program of this notebook
    import tempfile  # makes a new folder in the system's temporary folder
    import time  # a clock, for the wall time of the re-run
    from concurrent.futures import ThreadPoolExecutor  # several at a time

    scratch = Path(tempfile.mkdtemp(prefix="book_rerun_"))
    environment = {key: value for key, value in os.environ.items()
                   if key not in ("BOOK_RERUN_ALL", "TEXTBOOK_OUTPUT_ROOT")}
    nbkit = str(repository_file("Revision/textbook/tools/nbkit.py"))
```

With `BOOK_RERUN_ALL=1` the cell imports four more modules: `subprocess` starts other programs, `sys.executable` is the Python program that runs this notebook, `tempfile.mkdtemp` makes a new, empty folder in the system's temporary folder (its name starts with `book_rerun_`), `time.perf_counter` is a clock. `ThreadPoolExecutor` runs a function on several items at the same time. `environment` is a copy of the environment variables without `BOOK_RERUN_ALL` (so that the notebooks started now do not start the re-run themselves) and without the output folder of an nbkit check. `nbkit` is the path of the tool.

```python
    def rerun(row):
        done = subprocess.run(
            [sys.executable, nbkit, "check", str(repository_file(row["builder"])),
             "--scratch", str(scratch)], capture_output=True, text=True,
            encoding="utf-8", errors="replace", cwd=REPO, env=environment)
        values = dict(line.split("=", 1) for line in done.stdout.splitlines()
                      if "=" in line)
        fresh = values.get(f"check_{row["id"]}_seconds", "")
        return {"id": row["id"], "chapter": row["chapter"],
                "result": values.get(f"check_{row["id"]}", "FAILED"),
                "seconds": float(fresh) if fresh[:1].isdigit() else 0.0,
                "recorded": row["seconds"]}
```

`rerun(row)` runs the nbkit check of one notebook's builder, with the new scratch folder as its scratch folder (the command of Section 23.6), from the repository root (`cwd=REPO`), keeping its printed output (`capture_output=True`, as text). Every printed line of nbkit has the form `key=value`; `line.split("=", 1)` cuts it at the first `=`, and `dict(...)` collects the pairs. The function returns the id, the chapter, the result (`FAILED` if nbkit printed none), the fresh seconds (0 when nbkit printed no number) and the recorded seconds.

```python
    workers = max(1, min(8, (os.cpu_count() or 2) // 2))
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        FRESH = list(pool.map(rerun, sorted(ROWS, key=lambda row: -row["seconds"])))
    wall = time.perf_counter() - start
    FRESH.sort(key=lambda item: item["id"])
```

`workers` is half the number of processor threads, at least 1 and at most 8. The notebooks are handed to the pool slowest first (sorted by minus their recorded time), so that the longest ones start at once and the short ones fill the gaps. `pool.map` returns the results in the order of the input; afterwards they are sorted by id. `wall` is the wall time of the whole re-run.

```python
    print("chapter notebooks passed  fresh s recorded s")
    for chapter in sorted(PER_CHAPTER):
        items = [item for item in FRESH if item["chapter"] == chapter]
        print(f"{chapter:7d} {len(items):9d} "
              f"{sum(item["result"] == "PASSED" for item in items):6d} "
              f"{sum(item["seconds"] for item in items):8.1f} "
              f"{sum(item["recorded"] for item in items):10.1f}")
```

One line per chapter: the number of notebooks, how many passed, and their fresh and recorded seconds added up.

```python
    failed = [item["id"] for item in FRESH if item["result"] != "PASSED"]
    for item_id in failed:
        say(f"FAILED {item_id}: run its nbkit check alone to see the problem lines")
    with (scratch / "fresh_results.csv").open("w", encoding="utf-8",
                                              newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["id", "chapter", "result", "seconds", "recorded"])
        writer.writerows([item[key] for key in ("id", "chapter", "result",
                                                "seconds", "recorded")]
                         for item in FRESH)
    say(f"Re-run of {len(FRESH)} notebooks, {workers} at a time: {wall:.0f} s.")
    print(f"Fresh results: {scratch / "fresh_results.csv"}")
    assert not failed, f"nbkit check failed for {failed}"
    say(f"RERUN all {len(FRESH)} other notebooks passed their nbkit check.")
```

`failed` lists the ids of the notebooks that did not pass; each is named on a line. The fresh results are written to `fresh_results.csv` in the scratch folder (never into the repository). The cell prints the number of notebooks, the number run at a time and the wall time, and on a line of its own (with `print`, so that the path is never broken) where the CSV file is; then it stops with an error message (`assert`) if any notebook failed; otherwise it prints that all passed. The figures of the notebook keep showing the RECORDED times. On the development machine this cell, run once with `BOOK_RERUN_ALL=1` on 2026-10-08, printed all 90 notebooks as passed and a wall time of 406 s.

**In [16], the last check.**

```python
check(all(output_file(path).is_file() for path in
          [f"{FIGURE_FOLDER}/{name}" for name in CAPTIONS]
          + [NOTEBOOK_TABLE, CHECK_INDEX, CAPTION_FILE]),
      "every file this notebook writes exists")
all_checks_passed()
```

The check demands that every file this notebook writes exists: the six figures (`CAPTIONS` holds their names), the two data files and the caption file. `all_checks_passed()` prints the last line, `ALL 10 CHECKS PASSED (notebook 23a)`.

### 23.13 The index of the checks of the Revision record

The index of the checks is the file `Revision/textbook/data/23a_check_index.csv`, written by In [13] of Notebook 23a: one row for each of the 1208 checks of the 39 reports of the Revision record, with the report's path, the check's name, its verdict and the chapters (of 0 to 22) that cite it. Out [13] in Section 23.11 is its summary, one line per report, and Out [14] shows the rows of one report in full. To find a check by name, open the file in any spreadsheet program, or search it in the terminal:

Windows (PowerShell):

```text
Select-String -Path Revision/textbook/data/23a_check_index.csv -Pattern u1_noether
```

macOS (zsh) and Linux (bash):

```text
grep u1_noether Revision/textbook/data/23a_check_index.csv
```

Both print the row `Revision/lead_checks/reports/charge-conjugation-and-u1.json,u1_noether_matrix_identity,PASS,0 5 10 18 20 21 22`. A check that no chapter cites (497 of the 1208) is still part of the record and still verified by the gate; the book teaches the results it needs and cites the checks that establish them, and the other checks guard the computations from which those results come (inputs read correctly, intermediate identities, the Rust programs' own tests).

### 23.14 The index of the notebooks

The index of the notebooks is the table of Out [4] and Out [5] in Section 23.11, also written to `Revision/textbook/data/23a_notebooks.csv`: for each notebook its id, title, number of checks, number of figures, last recorded check, and in the last column the section that holds its run instructions; its complete text is the section after it, and its line-by-line walk-through the section after that. Notebook 23a itself is printed in Sections 23.10 and 23.11 and explained in Section 23.12. All 90 recorded checks of the other notebooks are dated 2026-10-08 and passed.

### 23.15 What we proved, what we computed, what we assumed

- PROVED: nothing new about physics; this chapter is bookkeeping. Notebook 23a checks facts about files: every builder has a provenance file, every notebook is placed exactly once in its own chapter, every recorded nbkit check passed, every report named by the gate is in the index, and every one of the 1208 checks of the 39 reports is PASS or NOT-AVAILABLE (the 5 NOT-AVAILABLE checks are outputs that the author's notebook does not store).
- COMPUTED (counted from files on 2026-10-08): 90 notebooks in chapters 0 to 22 with 2236 checks and 563 figures; their recorded checks take 1446.0 s one after the other, and the three slowest take 39.6 % of it; the gate has 63 steps, 8 of them long, with expected wall times of 10532 s in full and 3252 s with the fast option; 711 checks of the record are cited by at least one chapter. MEASURED once with `BOOK_RERUN_ALL=1` on 2026-10-08: all 90 other notebooks passed a fresh nbkit check, 8 at a time, in 406 s of wall time; the fresh time of each chapter was between 0.89 and 1.50 times its recorded time (chapter 8: 129.9 s against 86.5 s), because 8 notebooks shared the processor.
- MEASURED elsewhere and quoted: the recorded check times (provenance files), the gate's expected times (its step table, from the folder READMEs and provenance files), the fast option's measured 20 minutes (Revision README), the assembler's 4 seconds and the 287 s of the whole-book test build (runs made for this chapter on 2026-10-08).
- ASSUMED: that the files read are the committed ones. The notebook reads whatever is in the working folder; after any other notebook is rebuilt or any chapter changes a citation, Notebook 23a must be rebuilt, or its nbkit check fails because its outputs changed.
- What "cited" means is a DEFINITION of this chapter (one paragraph, or one cell's output, names both the report's file name and the check), not a reading of the author's intention; a chapter may discuss a check in other words without being counted.

### 23.16 Exercises with worked answers

**Exercise 1.** You have a fresh clone and want to know, before waiting hours, how long the gate will take on the development machine with and without the fast option. Which command answers this without running anything, and what numbers do you expect?

*Answer.* The dry run, which runs nothing:

```text
bash Revision/verify_revision.sh --dry-run
bash Revision/verify_revision.sh --dry-run --fast
```

(or the PowerShell twin with the same options). The first prints every step with its expected wall time and the line `revision_selected_steps=63 expected_seconds=10532 skipped_steps=0`; the second prints `revision_selected_steps=55 expected_seconds=3252 skipped_steps=8`. These are the sums of the step table that Notebook 23a prints in Out [9]: 10532 s = 2.93 h and 3252 s = 54.2 min. The measured time of the fast option was about 20 minutes, less than the expected sum, because the table's times are generous upper estimates.

**Exercise 2.** Using Out [6], how long does the nbkit check of all notebooks of chapters 14, 15 and 16 take, one after the other, and what fraction of the whole book's check time is that?

*Answer.* The three chapter totals are 135.1 s, 147.3 s and 152.1 s; their sum is $135.1 + 147.3 + 152.1 = 434.5$ s. The whole book takes 1446.0 s, so the fraction is $434.5 / 1446.0 = 0.3005$, about 30 %: three chapters of the Kohn-Sham part take almost a third of the time, because their notebooks run the Rust solver and the reference solver.

**Exercise 3.** Why does Notebook 23a leave itself out of its table, and why does it leave chapter 23 out of the citation search? What would go wrong otherwise?

*Answer.* Its own provenance file is rewritten every time it is built, with the new check result and seconds; if the notebook printed its own record, the printed table would differ from the record it was built from, and the second (check) execution would print yet another time, so the byte comparison of nbkit check would fail. Chapter 23 quotes the notebook's own outputs and check names; if the notebook counted citations in chapter 23, every edit of this chapter would change the notebook's output, which the chapter quotes again: a loop with no fixed point. Leaving both out breaks the loop.

**Exercise 4.** In In [12] a check is cited by a block only when the block contains both the report's file name and the check name as a whole word. Give an example of why the file name is required, and one of why "whole word" is required.

*Answer.* The same check name can occur in two reports: `fixture_input` is a check of both `ks-theory-python.json` and `ks-theory-wolfram.json`; without the file name, a paragraph about the Wolfram report would also count as citing the Python one. Whole words: a check named `T3` (if one existed) would otherwise be "found" inside `T3C`, inside the word `T3_block_hamiltonian_map` or inside a path; the conditions `(?<![\w.-])` and `(?![\w-])` refuse a name that is part of a longer word.

**Exercise 5.** You run Notebook 23a with `BOOK_RERUN_ALL=1` on a computer with 4 processor threads. How many notebooks run at the same time, and can the re-run take less time than the slowest notebook, 11a, alone?

*Answer.* `workers = max(1, min(8, 4 // 2)) = max(1, min(8, 2)) = 2`: two at a time (`//` divides and drops the remainder). No: every notebook runs on one worker from start to end, so the re-run lasts at least as long as the slowest notebook, 348.5 s on the development machine. That is why the slowest are started first: with two workers, 11a runs on one while the other works through the rest, and the total is close to the larger of 348.5 s and half of the total time, $1446.0 / 2 \approx 723$ s, plus the time the two workers slow each other down.

**Exercise 6.** The gate prints `revision_failed_step=precheck`. What happened, what must you NOT do, and what are two correct ways forward?

*Answer.* An output file of a selected step already differs from the committed version: the gate verifies the committed record and refuses to overwrite uncommitted work. Do not delete or reset the changed files without knowing what they are; they may be your own work. Either run the gate in a fresh clone of the repository (`git clone` into a new folder), or leave the steps whose outputs differ out with the option steps; after you have committed or set aside your changes, the full gate runs.

### 23.17 Glossary

The glossary follows.
