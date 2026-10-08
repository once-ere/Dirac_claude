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
check_00a_compared_files=4
check_00a_seconds=3.6
check_00a_peak_mb=174.0
check_00a=PASSED
```

(the seconds and megabytes differ from run to run), and at the end `nbkit_seconds=...` and `nbkit=OK`. The number of compared files counts the notebook itself together with the files it writes: Notebook 00a writes three files, so nbkit compares 3 + 1 = 4 files with the stored ones. A check changes no file of the repository.

**How long it takes.** The recorded check times of the notebooks of each chapter, added up, are printed by Notebook 23a in Out [6] of Section 23.11 and drawn in Figure 23a.5. On the development machine chapter 11 is the slowest, 385.1 s, almost all of it Notebook 11a (348.5 s, which runs the Rust GKD program on large cases); chapters 14, 15 and 16 take 135.1 s, 147.3 s and 152.1 s; every other chapter takes between 13.2 s (chapter 9) and 86.5 s (chapter 8). All 90 notebooks of chapters 0 to 22 take 1446.0 s, about 24 minutes, one after the other (Out [6]); Notebook 23a adds about 6.5 s (its recorded check). The seven notebooks that run a Rust program (11a, 11b, 15a, 15b, 15d, 16a and 19a) build it with cargo the first time, which takes a few minutes more.

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

Without further options it builds in VERIFY mode: it builds the PDF twice, demands that the two builds are byte for byte identical and that pdflatex printed no warning, and compares the result with the edition `universes-in-pairs-textbook` registered in `Revision/pdf-specifications.json` (the registry entry holds the page count of the PDF and its sha256, a fingerprint of its bytes). The option date sets the date printed under the title, so it is part of the PDF: the comparison succeeds only with the date with which the registered edition was built. The book's edition is built with the date "October 2026", as in the commands above; without the option the builder prints its default date, "September 2026", and the PDF then differs from the edition built with October. With the option register added at the end it records a changed book as the new edition. It needs pdflatex. When it works it prints one line `check_NAME=true` per check, the measurements (among them the page count), `failed_check_count=0` and the last line `provenance_pdf=OK`; any LaTeX warning (an overfull line, a figure too large for a page) is printed and fails the build, and the message names the line of the `.tex` file, which belongs to the chapter text at the same place.

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

It prints `chapter_check=OK` when the chapter builds without any problem and warning. A test build of the whole book made in this way on 2026-10-08, with the chapters as they stood that day, took 287 s for its first pass (two complete pdflatex builds of a book of 6289 pages, compared byte for byte), and that pass ended FAILED: pdflatex printed warnings for the text of other chapters as it stood then, so the second, verify pass, which repeats the builds, did not run. A warning-free build of the whole book had not yet been measured when this chapter was written.

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

Both find the row `Revision/lead_checks/reports/charge-conjugation-and-u1.json,u1_noether_matrix_identity,PASS,0 5 10 18 20 21 22`. grep prints the row alone; Select-String prints in front of it the path of the file and the number of the line in the file, each followed by a colon. A check that no chapter cites (497 of the 1208) is still part of the record and still verified by the gate; the book teaches the results it needs and cites the checks that establish them, and the other checks guard the computations from which those results come (inputs read correctly, intermediate identities, the Rust programs' own tests).

### 23.14 The index of the notebooks

The index of the notebooks is the table of Out [4] and Out [5] in Section 23.11, also written to `Revision/textbook/data/23a_notebooks.csv`: for each notebook its id, title, number of checks, number of figures, last recorded check, and in the last column the section that holds its run instructions; its complete text is the section after it, and its line-by-line walk-through the section after that. Notebook 23a itself is printed in Sections 23.10 and 23.11 and explained in Section 23.12. All 90 recorded checks of the other notebooks are dated 2026-10-08 and passed.

### 23.15 What we proved, what we computed, what we assumed

- PROVED: nothing new about physics; this chapter is bookkeeping. Notebook 23a checks facts about files: every builder has a provenance file, every notebook is placed exactly once in its own chapter, every recorded nbkit check passed, every report named by the gate is in the index, and every one of the 1208 checks of the 39 reports is PASS or NOT-AVAILABLE (the 5 NOT-AVAILABLE checks are outputs that the author's notebook does not store).
- COMPUTED (counted from files on 2026-10-08): 90 notebooks in chapters 0 to 22 with 2236 checks and 563 figures; their recorded checks take 1446.0 s one after the other, and the three slowest take 39.6 % of it; the gate has 63 steps, 8 of them long, with expected wall times of 10532 s in full and 3252 s with the fast option; 711 checks of the record are cited by at least one chapter. MEASURED once with `BOOK_RERUN_ALL=1` on 2026-10-08: all 90 other notebooks passed a fresh nbkit check, 8 at a time, in 406 s of wall time; the fresh time of each chapter was between 0.89 and 1.50 times its recorded time (chapter 8: 129.9 s against 86.5 s), because 8 notebooks shared the processor.
- MEASURED elsewhere and quoted: the recorded check times (provenance files), the gate's expected times (its step table, from the folder READMEs and provenance files), the fast option's measured 20 minutes (Revision README), the assembler's 4 seconds and the 287 s of the first pass of the whole-book test build, a pass that ended FAILED on LaTeX warnings in the text of other chapters as it stood then (runs made for this chapter on 2026-10-08).
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

This glossary lists, in alphabetical order, the technical words that the book defines: the words printed in bold where a chapter first explains them, the words of section 3, "The words used in this notebook", of every notebook, the words of the lists "The words of this chapter", and a few words that a notebook defines elsewhere, such as Sakharov's three conditions. Each entry gives the meaning in plain words, taken from a place that defines the word, and then, in brackets, every section where the word is defined or explained. A section titled "Notebook NNx: complete text" means section 3 of that notebook; "the opening of Chapter N" means the paragraphs before its first section. Where a word is defined in several places, the entry quotes the first of them that has the form of a definition (a list entry "word: meaning", or a sentence such as "a word is ..."); the other sections listed explain the same word again, often for a particular case. For a few central words (among them the five status labels, the extra times, the U(1) charge and the word universe) the entry is written from all its defining sections. A word that is defined together with others in one bold phrase (for example "Eigenvalue, eigenvector") is listed under that phrase when it has no entry of its own. The words in capitals PROVED, COMPUTED, ASSUMED, HYPOTHESIS and OPEN are the five status labels of the book; each has its own entry.

**0-9**

- **0/1 matrix**: A 0/1 matrix has only the entries 0 and 1. (Section 11.8.)
- **2 × 2 matrix**: A 2 × 2 matrix is a table of four numbers in two rows and two columns. (Section 1.12.)
- **3-momentum $k$**: the momentum along ordinary 3-space; on the coordinate torus of size $\ell$ the allowed vectors are $\Delta k\,(n_1, n_2, n_3)$ with integers $n_i$ and $\Delta k = 2\pi/\ell = 0.25$ (in units of $H$). (Section 14.24.)
- **3-space**: $x_1, x_2, x_3$ are ordinary 3-space; it inflates, with the scale factor $e^{a_4}\sin^{1/6}z$. (Section 3.1.)
- **A 3-space direction**: A 3-space direction, $\mu = x1$ (the same for $x2$ and $x3$). (Section 6.8.)
- **40 digits**: Double precision: the computer's usual numbers, with about 16 significant digits; 40 digits: mpmath's numbers with as many digits as asked for. (Section 15.29.)
- **40-digit arithmetic**: numbers with 40 significant decimal digits, computed by the package mpmath (slow, but exact far beyond what is needed here). (Section 16.23.)

**A**

- **Absolute value** $|x|$: $x$ without its sign; $\sqrt{x^2} = |x|$. (Sections 1.5 and 1.8.)
- **Acceleration**: Its velocity is $\dot q = dq/dt$ and its acceleration $\ddot q = d^2q/dt^2$ (a dot over a letter is the derivative with respect to the time $t$). (Sections 7.2 and 7.8.)
- **Action** $S[q] = \int_0^T L(q(t), \dot q(t))\,dt$: one number for a whole path. (Sections 7.2, 7.8 and 9.4.)
- **Activated regime**: When a gap is many times $T$ the state is in the activated regime: only very few quanta are thermally lifted across it. (Sections 16.20 and 16.23.)
- **Adiabatic**: a change of the Hamiltonian slow enough that a system in an eigenstate stays in the eigenstate that continues it (the adiabatic theorem). (Sections 14.3, 15.24, 22.2 and 22.11.)
- **Adiabatic limit**: At a very small rate the particle stays in its instantaneous level, up to the dressing (the adiabatic limit). (Section 22.8.)
- **Adiabatic theorem**: A system whose Hamiltonian changes slowly enough stays in the eigenstate that continues its initial one (the adiabatic theorem of quantum mechanics; Chapter 14 introduced this adiabatic picture); a system whose Hamiltonian changes too fast is kicked into higher levels. (Section 15.21.)
- **Adiabatically continued state**: Adiabatically continued state: the state that keeps the occupations of the first slice. (Section 15.24.)
- **Adiabaticity**: how well an evolution is adiabatic, that is so slow that every particle stays in its instantaneous level. It is measured by the adiabaticity measure $Q_{max}$ (see that entry): a small $Q_{max}$ means that the slow-change approximation holds. (Sections 16.11 and 22.2.)
- **Adiabaticity measure** $Q_{nm} = A H |\langle n|\partial_a h|m\rangle| / (\varepsilon_n - \varepsilon_m)^2$: the first-order amplitude of the jump $n \to m$; $Q_{max}$ is the largest over all allowed pairs. (Sections 15.21, 15.24, 22.2 and 22.11.)
- **Adjoint**: Adjoint $\bar\Phi = \Phi^\dagger C$ with $C = \gamma^{(x_8)}\gamma^{(x_1)} \gamma^{(x_2)}\gamma^{(x_3)}$; $\Phi^\dagger$ is the row of complex conjugates. (Section 12.29.)
- **Admissible source**: a source for which the field equations of the author's metric can hold. (Sections 17.2, 17.10 and 17.20.)
- **Algebraic condition**: The evolution equation is the 3-space equation minus the extra-time equation; the algebraic condition is $p_3 + p_t = 2p_8$. (Sections 12.2 and 12.9.)
- **Amplification factor** $R(z)$: for the test equation $y' = \lambda y$, one step of a method multiplies $y$ by a number $R(z)$ that depends only on $z = \lambda h$. (Sections 2.5 and 2.10.)
- **Amplitude** and **probability**: when an orbital is written as a sum $\sum_n c_n\varphi_n$ of instantaneous orbitals, the complex number $c_n$ is the amplitude of level $n$ and $|c_n|^2$ the probability to find the particle in level $n$. (Sections 15.24, 20.2, 20.20, 21.30, 22.2 and 22.11.)
- **Anderson mixing**: a mixing that uses several earlier steps to estimate the slope of $G$ (for one variable it is close to the secant method). (Sections 13.21, 13.24, 15.5, 15.8 and 15.13.)
- **Angle**: The number $\theta$ is called the angle of a rotation and the rapidity of a boost. (Section 5.18.)
- **Angular frequency**: where $\omega > 0$ is a fixed number, the angular frequency of the spring. (Section 7.2.)
- **Anisotropic stress**: the difference $p_3 - p_t$ between the 3-space pressure and the extra-time pressure. (Sections 12.2 and 12.24.)
- **Annihilates**: give $bb^* = \mathrm{diag}(1, 0)$ and $b^*b = \mathrm{diag}(0, 1)$, whose sum is the identity; $b|1\rangle = |0\rangle$ (it annihilates the fermion), $b^*|0\rangle = |1\rangle$ (it creates one), and $b^*|1\rangle = 0$: a second fermion cannot be created. (Section 10.11.)
- **Annihilation and creation operators** $f_p$, $f_p^*$: $f_p$ empties mode $p$ (and gives zero if it is empty), $f_p^*$ fills it (zero if it is full), each with a sign $(-1)^{(\text{number of occupied modes below } p)}$. (Section 5.37.)
- **Annihilation operator**: Creation operator $a_p^\dagger$, annihilation operator $a_p$: add or remove a fermion in orbital $p$, with the sign $(-1)^{\nu_p}$, where $\nu_p$ is the number of occupied orbitals before $p$; on the 16 occupation-number states they are $16 \times 16$ matrices. (Sections 5.34, 13.4, 13.13, 21.26 and 21.29.)
- **Annotation**: Tick marks, labels, the vertical range, and an annotation: a text in a white box with an arrow pointing at the place $(2.5\pi, 0)$, where two curves lie on the axis and would otherwise be hard to see. (Section 5.33.)
- **Ansatz**: An ansatz is a guessed form of the solution with unknown parts to be determined. (Section 14.3.)
- **Anti-Hermitian**: A matrix is Hermitian if it equals its conjugate transpose, $M^\dagger = M$, and anti-Hermitian if $M^\dagger = -M$. (Sections 8.17, 8.35 and 10.4.)
- **Anticommutator**: $\{M, N\} = MN + NM$. (Sections 1.28, 1.32, 4.7, 5.9, 5.34, 5.37, 6.13, 8.3, 8.14, 10.11, 10.18, 13.4, 13.13, 17.21, 18.4, 21.25 and 21.29.)
- **Anticommutator matrix**: for two lists of operators $X_1, \dots, X_n$ and $Y_1, \dots, Y_n$ whose anticommutators are numbers, the matrix with entries $\{X_i, Y_j\}$. (Section 10.48.)
- **Anticommute**: $AB = -BA$, that is $\{A, B\} = AB + BA = 0$. (Sections 1.28, 4.1, 4.2, 4.9, 4.11, 4.19, 5.2, 5.9, 5.34, 7.1, 7.10, 7.16, 7.32, 8.2, 14.10, 18.8 and 21.7.)
- **Anticommuting**: The components of dirac16complex are anticommuting numbers, also called Grassmann numbers after the mathematician who introduced them: exchanging two of them in a product costs a sign, $\Psi_r\Psi_c = -\Psi_c\Psi_r$, and in particular $\Psi_r\Psi_r = -\Psi_r\Psi_r$, so $\Psi_r\Psi_r = 0$. (Sections 1.10, 5.29, 8.2, 21.2 and 21.7.)
- **Antimatter**: matter made of antiparticles; the antiparticle of a particle has the same mass and the opposite charge, as the positron has for the electron (Chapter 21). (Sections 0.2, 20.23 and 21.2.)
- **Antiparticle**: A particle $b_s^*|0\rangle$ and an antiparticle $d_s^*|0\rangle$ (a hole in the filled sea) both have the energy $+E > 0$. (Sections 5.28, 10.20, 10.25, 20.17 and 20.23.)
- **Antiquark**: An antiquark ($\bar u$, $\bar d$) has the opposite numbers. (Section 21.35.)
- **Antisymmetric**: changing sign when two particles are exchanged. (Sections 1.28, 1.32, 4.2, 4.7, 5.2, 5.9, 6.7, 6.13, 6.27, 7.16, 13.13, 18.8, 21.2, 21.7 and 21.14.)
- **Antisymmetric part**: Write $M$ as the sum of its symmetric part $\tfrac12(M + M^T)$ and its antisymmetric part $\tfrac12(M - M^T)$. (Section 7.12.)
- **Antisymmetry**: (i) Antisymmetry: exchanging the particles $i$ and $j$ exchanges the rows $i$ and $j$ of the table, which changes the sign of the determinant (rule 3). (Section 13.3.)
- **Argument** (or **phase angle**): the angle between the arrow and the positive real axis, measured counterclockwise in radians ($\pi$ radians $= 180$ degrees). (Sections 1.11, 1.16 and 2.11.)
- **Array**: `np.linspace(-1.0, 3.0, 401)` makes an array (numpy's list of numbers) of 401 numbers from $-1$ to $3$ with equal steps of $4/400 = 0.01$. (Sections 0.13, 1.9, 2.11, 3.13, 13.14, 15.9, 17.11, 21.15, 22.12 and 22.23.)
- **Assembly**: joining the 24 chapter files, with every notebook expanded, into the one file `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md`. (Section 23.2.)
- **Associative**: Products are associative, $(AB)D = A(BD)$ (both sides are $\sum_{k,l} A_{ik}B_{kl}D_{lj}$), so brackets may be left out. (Sections 1.18 and 4.2.)
- **ASSUMED**: a status label: the statement is used but not derived; it is a starting point of the book (a convention, a physical input or an approximation), and everything that depends on it says so. Example: the Z2 mirror at the edge of the hidden direction. (Sections 0.3, 0.20, 0.26, 1.55, 2.29, 3.1, 3.36, 4.21, 5.40, 6.1, 6.30, 7.34, 8.1, 11.28, 12.31, 14.32, 15.31 and 22.27.)
- **Asymptotic regime**: A ratio close to 4 shows that the grids are fine enough for the $h^2$ term to dominate (the asymptotic regime), which is what Richardson extrapolation needs. (Section 16.4.)
- **Atan2(b, a)**: the angle of the point $(a, b)$ between $-\pi$ and $\pi$. (Section 2.27.)
- **Aufbau**: filling the lowest levels with the $N$ particles. (Sections 13.6, 14.21, 14.24 and 15.24.)
- **The author's second route** (Section 11.5): a determinant identity for the Levi-Civita symbol; raising all labels of the Levi-Civita tensor of a metric gives the factor $\sqrt{|\det g|}/\det g$, so the product of two Levi-Civita tensors is the sign of $\det g$ times the product of two symbols; for the author's metric $\det g = \cos^2z > 0$ (record `python-lovelock-report.json`, check `sqrt_abs_det_g`), the sign is $+1$, and the author's second route gives the generalized delta without an extra sign. (Section 11.28.)
- **Average**: The ratio $\int E\xi\,dt/\int\xi\,dt$ is an average of $E$ over the bump. (Section 7.3.)
- **Axes**: `plt.subplots(1, 3, ...)` makes a figure `fig` with one row of three panels, the axes (drawing areas) `axes[0]`, `axes[1]`, `axes[2]`, 10.5 by 3.9 inches in all. (Sections 5.10, 11.9, 14.11, 17.11, 19.16 and 20.11.)

**B**

- **Back-reaction**: Back-reaction: the effect of the matter's own gravity on the metric; a test field has none. (Sections 17.2, 17.10, 17.20, 17.22 and 22.2.)
- **Band level**: The label $n$ is the integer that numbers the levels of one sector in order: $n = 0$ is the band level (bound to the brane; the occupied level of the Fermi shell), $n = 1, 2, \ldots$ are the bulk levels above it, and $n = -1, -2, \ldots$ are the levels of negative energy, the negative branch, which the record's filling convention treats as the normal-ordered sea that holds no particles. (Sections 22.2 and 22.11.)
- **Bare mass** $m$: the mass in the Lagrangian; effective mass $M_{eff}(y)$: the mass seen by an orbital, $m$ plus the mean-field term. (Section 19.20.)
- **Barrier**: a region that the classical equations forbid, for example a region of too high energy; tunnelling is a quantum transition through it, with a small but nonzero probability. (Section 20.2.)
- **Baryogenesis**: Explaining how is the matter-antimatter problem, also called baryogenesis. (Section 21.4.)
- **Baryon**: a particle made of three quarks, such as the proton $p = uud$ and the neutron $n = udd$ ($B = 1$); a meson (pion $\pi$) is a quark and an antiquark ($B = 0$). (Sections 21.2 and 21.35.)
- **Baryon number**: The baryon number counts protons and neutrons minus antiprotons and antineutrons. (Sections 20.23, 21.2 and 21.35.)
- **Baryon-to-photon ratio** $\eta_B$: the number of baryons minus antibaryons per photon of the microwave background (Section 21.4). The letter $\eta$ with two indices, $\eta_{ab}$ or $\eta^{ab}$, is the frame metric; $\eta(K)$ without a subscript is the efficiency of the rate model of Section 21.6. (Sections 21.2 and 21.4.)
- **Basic operators**: Every operator used here is a combination of 32 basic operators $O_i$: $O_p = F_p$ and $O_{16+p} = F_p^\ast$ for $p = 0, \dots, 15$, where $F_p = b_{p+1} = f_p$ for $p < 8$ (particles) and $F_p = d_{p-7}^\ast = f_p^\ast$ for $p \geq 8$ (antiparticles appear in $\Psi$ through their creation operators), and $F_p^\ast$ is the Hilbert adjoint of $F_p$. (Section 5.38.)
- **Basis**: a set of orbitals in which every orbital is written as a sum. (Sections 4.13, 4.15, 5.16, 5.23, 7.29, 22.2 and 22.11.)
- **Bianchi identities**: $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$ (first) and $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$ (contracted): identities that every metric satisfies; checking them checks the computation. (Sections 3.29, 11.26, 12.2, 12.15, 17.2 and 17.20.)
- **Bilinear**: an expression $\Psi^\dagger K \Psi = \sum_{r,c}\Psi_r^* K_{rc} \Psi_c$ with a fixed matrix $K$. (Sections 5.1, 5.29, 5.32, 8.35, 9.2, 12.29, 18.2, 18.4, 18.8, 21.2 and 21.14.)
- **Bilinear form**: an expression $\sum_{A,B} x_A M_{AB} y_B$ that contains one factor from the column $x$ and one from the column $y$ in every term. (Sections 7.12, 7.16, 10.33 and 10.37.)
- **Bilinear operator**: $\Psi^\dagger K\Psi = \sum_{A,C}\Psi^\dagger_A K_{AC} \Psi_C$ for a fixed $16 \times 16$ matrix $K$. (Section 5.37.)
- **Binary**: the way of writing numbers with the two digits 0 and 1, in powers of 2 instead of powers of 10: binary 101 is $4 + 0 + 1 = 5$, and binary 0.11 is $1/2 + 1/4 = 3/4$. (Sections 0.22, 0.24, 1.49 and 1.53.)
- **Binary digits**: The computer stores a pattern of occupations as a whole number $n$ whose binary digits are the occupations: digit $q$ (counted from 0, from the right) is the occupation of mode $q$. (Section 5.38.)
- **Binomial coefficient** $\binom{n}{k}$ ("n choose k"): the number of subsets with $k$ elements of a set with $n$ elements; $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ with $n! = 1 \cdot 2 \cdots n$ and $0! = 1$. For example $\binom{8}{2} = 28$. (Sections 4.13, 4.15, 7.10 and 10.20.)
- **Birthday problem**: This is the birthday problem: the chance that $p$ people have $p$ different birthdays, with 8 "days" instead of 365. (Sections 1.50 and 11.4.)
- **Bisection**: halving an interval that contains the number again and again, keeping the half that still contains it. (Sections 1.3, 1.8, 2.16, 10.43, 13.14, 13.24, 13.26, 13.30, 14.14, 14.17, 14.18, 15.3, 15.8, 15.9, 16.3, 16.18, 16.23, 17.21, 19.16, 22.11, 22.12 and 22.23.)
- **Bisection method**: `bisection` finds the same time independently, by the bisection method: start with an interval $[-30, 30]$ in which $E^2$ changes sign; look at the middle; if $E^2$ is still positive there, the onset is later and the middle becomes the new left end, otherwise the new right end; after 200 halvings the interval is far smaller than the rounding of the numbers, and its middle is returned. (Section 8.29.)
- **Bit mask**: To test this quickly it stores a set of labels as a bit mask, the whole number $\sum 2^{\text{label}}$: the set $\{x_1, x_3\}$ (numbers 0 and 2) is $2^0 + 2^2 = 5$. (Section 11.12.)
- **Bits**: the 16 components are numbered $j = 8b_1 + 4b_2 + 2b_3 + b_4$ with four binary digits (bits) $b_1, b_2, b_3, b_4$, each 0 or 1, one per slot; for example $j = 5$ has the bits 0101. (Sections 0.22, 0.24, 1.4, 1.49, 1.53, 4.17, 4.19 and 21.30.)
- **Block**: a $16 \times 16$ matrix cut into four $8 \times 8$ pieces; rows and columns 1 to 8 form the first half, 9 to 16 the second half. $\mathrm{diag}(X, Y)$ is the matrix with the blocks $X$ (top left) and $Y$ (bottom right) and zeros elsewhere. (Sections 4.2, 5.9, 14.10, 19.2 and 19.15.)
- **Block diagonal**: a $16 \times 16$ matrix whose upper-right and lower-left $8 \times 8$ blocks are zero; block off-diagonal: one whose upper-left and lower-right blocks are zero. (Sections 4.2, 4.15 and 5.5.)
- **Block equation**: in each of eight $2\times2$ blocks the Kohn-Sham equation is $h_j\chi = \varepsilon\chi$ with $h_j = j[-i\sigma_1\,d/dy + M\sigma_2 + \kappa k\,\sigma_3] + v$, where $j = \pm1$ is the block type, $M$ the (effective) mass, $\kappa k$ the weighted 3-momentum and $v$ the vector potential. (Section 14.17.)
- **Block equation in real form**: Its level $\varepsilon$ and the two functions obey the block equation in real form (`Revision/kohn_sham/ks-theory.json`, blockEquation.realForm; checks block_hamiltonian and block_ode_equivalent): $a' = M a - \big(\kappa k + j(\varepsilon - v)\big)\,b, \qquad b' = \big(j(\varepsilon - v) - \kappa k\big)\,a - M b$. (Section 15.2.)
- **Block matrix**: a big matrix cut into smaller matrices (blocks). For example $\begin{pmatrix} 0 & B \\ D & 0 \end{pmatrix}$ has the zero matrix as its upper-left and lower-right blocks. (Section 4.7.)
- **Block off-diagonal**: A matrix whose two off-diagonal blocks are zero is block diagonal; one whose two diagonal blocks are zero is block off-diagonal. (Sections 4.2, 4.15 and 5.5.)
- **Block type** $j = \pm 1$ and **brane parity** (even or odd): labels of the orbitals (explained in section 4 of Notebook 19a). (Sections 16.18, 19.2 and 19.20.)
- **Blueshifted**: The frame velocity along an extra time grows like $e^{a_4}$: motion along the extra times is blueshifted, because they deflate. (Section 3.31.)
- **Bogoliubov coefficient**: in a quantum field on a gravitational field that changes in time, a number that says how much of a wave that oscillates with positive frequency at early times has turned into a wave of negative frequency at late times; its squared modulus is the mean number of particles created in that wave. It is the standard measure of particle creation by a changing background. (Sections 10.45, 18.2 and 20.2.)
- **Bogoliubov method**: a way to count the quanta of a field that a changing background creates: one compares the modes of the field before and after the change, and the part of a positive-energy mode of the start that has turned into negative-energy modes of the end measures the creation. It is quoted in Chapter 22, not derived or applied. (Section 22.2.)
- **Bonding**: For $\epsilon = -t$ the first row of $(h + t)\phi = 0$ reads $t\phi_L - t\phi_R = 0$, so $\phi_L = \phi_R$, and normalised $\phi = (1, 1)/\sqrt2$ (the bonding orbital, lower energy); for $\epsilon = +t$ we get $(1, -1)/\sqrt2$ (antibonding). (Section 13.2.)
- **Boolean mask**: `energies[dirac_svals < 1e-9]` keeps the energies at which it is below $10^{-9}$ (zero up to rounding): a boolean mask, an array of True/False that selects entries. (Section 4.12.)
- **Boost**: the matrix with rows $(\cosh\varphi, \sinh\varphi)$ and $(\sinh\varphi, \cosh\varphi)$ acting on a pair $(t, x)$ of a time-like and a space-like coordinate; it keeps $x^2 - t^2$. (Sections 1.13, 1.16, 4.13, 5.12, 5.18, 5.21, 5.26, 6.21, 8.3, 8.14, 10.34 and 10.37.)
- **Boost pair**: Kinds of pairs $\{a, b\}$ of two different frame directions: space-space (both space-like), time-time (both time-like) and boost pair (one space-like and one time-like). (Section 6.27.)
- **Bosons**: Nature realises this in two ways: for bosons $\Psi$ itself is unchanged, for fermions it changes sign: $\Psi(\dots, x_i\sigma_i, \dots, x_j\sigma_j, \dots) = -\,\Psi(\dots, x_j\sigma_j, \dots, x_i\sigma_i, \dots) \qquad \text{(fermions)}$. (Section 13.3.)
- **Bound**: If all of them had their largest size and the same sign, their total would be about $N \epsilon = \epsilon/h$ times the size of the solution; this is a pessimistic bound, the scale of the worst case. (Section 2.6.)
- **Bound state**: A bound state is a solution with $-V_0 < E < 0$ that decays to zero far away on both sides; its energy is an eigenvalue. (Section 2.13.)
- **Boundary conditions**: at the tip $b(-L) = 0$ (the *regular tip*, a choice of the model); at the brane $b(0) = 0$ (*even* orbitals) or $a(0) = 0$ (*odd* orbitals), which follow from the ASSUMED mirror symmetry of the model (the record labels it ASSUMED). (Sections 0.2, 2.27, 10.27, 10.31 and 14.17.)
- **Boundary terms**: An operator $A$ is called antisymmetric for the weight $w(x_8)$ when $\int w\,p\,(Aq)\,dx_8 = -\int w\,(Ap)\,q\,dx_8$ for all functions $p$, $q$, up to boundary terms (values at the ends of the interval). (Sections 6.24, 7.3, 7.8, 8.32, 8.35, 10.27 and 20.22.)
- **Boundary value**: We call the numerator, divided by $1 - e^{-6HL}$, the boundary value of $p_8$. (Section 17.15.)
- **Boundary-value problem**: a differential equation with conditions at two different points (here at both ends of an interval), instead of all conditions at the start. (Sections 2.12 and 2.16.)
- **Bracket**: two guesses at which $F$ has opposite signs; a continuous $F$ has a zero between them. (Sections 2.12, 2.16, 2.27, 15.3, 15.8 and 19.16.)
- **Branch point**: Branch point: a value of $a_4'$ where $F(a_4') = 0$, so that the evolution equation cannot be solved for $a_4''$. (Sections 17.2 and 17.17.)
- **Branching probability**: the probability that a decaying particle decays in one particular way (one channel). (Section 21.35.)
- **Brane**: a boundary surface of spacetime; in this book the end $z = \pi/2$ of the hidden direction (in the hidden coordinate $y = \ln(\sin z)/(6H)$ the end $y = 0$), where the author's coordinate patch ends and $g_{88} = \cot^2 z = 0$. In the ASSUMED Z2 construction the patch $0 < z < \pi/2$ is glued there to its mirror patch $\pi/2 < z < \pi$. (Sections 2.24, 5.6, 8.31, 8.35, 14.2, 15.1, 15.13, 16.1, 17.2, 17.10, 17.20, 18.2, 18.19, 18.26, 19.2, 19.15, 19.20, 20.2, 20.10, 20.15, 21.2, 21.22, 22.1 and 22.2.)
- **Brane band**: the even-parity level of label 0 in the blocks $j = +1$, which is the zero mode at $k = 0$ and rises with $k$. (Sections 14.19, 14.24, 15.2, 15.4, 16.15, 16.18, 19.2 and 19.12.)
- **Brane parity**: even means $\chi_2(0) = 0$, odd means $\chi_1(0) = 0$; both kinds of orbitals belong to every state. (Sections 19.2, 19.15 and 19.20.)
- **Brane tension**: Brane tension: an energy per unit area carried by such a surface itself (for the brane, per unit of its seven-dimensional area). (Section 18.2.)
- **Brane value**: A level is a value of $\varepsilon$ at which this brane value is zero. (Sections 16.11 and 19.16.)
- **Brane zero mode**: So $\chi = (Ae^{My}, 0)$ is an orbital with $\varepsilon = 0$, for every $L$: the brane zero mode, largest at the brane. (Section 14.13.)
- **Breakdown**: a point where $F(a_4') = 0$, so that the evolution equation can no longer be solved for $a_4''$. (Sections 12.24 and 22.2.)
- **Breakdown rate**: a rate at which the probability that a particle is NOT in its instantaneous level stops being small. (Section 22.11.)
- **Broadcasting**: `lowers[:, :, None] == uppers[:, None, :]` compares every lower label with every upper label of the same pair at once (numpy broadcasting: the inserted axes of length 1 are stretched to match), giving one matrix `Outer` of True and False per pair. (Sections 1.48, 5.33, 18.27 and 22.12.)
- **Brute force**, **literal sum**: a computation that tries every case without any shortcut. (Section 11.18.)
- **Bubble sort**: `sort_with_sign(generators)` sorts a list of generator numbers by the method called bubble sort and counts the exchanges. (Section 7.17.)
- **Builder**: the Python file `Revision/textbook/notebooks/src/NNx_name.py` from which the tool `nbkit` builds Notebook NNx. (Sections 0.9, 23.2 and 23.11.)
- **Bulk band**: In the author's metric the record finds this law for the massive bulk band (odd brane parity; its edge at zero momentum is $\varepsilon(0) = 1.292292828069$): the lowest odd-parity level of the shell $n_2 = 1$ has $w_{\rm eff}(A)$ falling monotonically from 0.239626 at $a_4 = -3$ to $2.268 \times 10^{-3}$ at $a_4 = 4$, while the brane-band level of the same shell stays between 0.291594 and 0.333275, tending to $1/3$ (`Revision/dark_sector/dirac16complex/reports/independent-checks.json`, checks `bulk_band_dark_matter_law` and `brane_band_radiation_law`; Notebook 22b, In [5] and Figure 22b.2). (Section 22.18.)
- **Bulk edge**: the lowest level that is not on the brane band (here a $k = 0$ level of the odd parity). (Sections 14.19, 14.24, 15.2 and 16.13.)
- **Bulk levels**: The label $n$ is the integer that numbers the levels of one sector in order: $n = 0$ is the band level (bound to the brane; the occupied level of the Fermi shell), $n = 1, 2, \ldots$ are the bulk levels above it, and $n = -1, -2, \ldots$ are the levels of negative energy, the negative branch, which the record's filling convention treats as the normal-ordered sea that holds no particles. (Sections 22.2 and 22.11.)
- **Bump**: a smooth shape that is positive on a small interval and zero outside. (Sections 7.3 and 7.8.)
- **Byte**: 8 bits, a whole number from 0 to 255. (Sections 0.24, 0.25, 1.49 and 1.53.)
- **Byte for byte**: Byte for byte: two files equal in every byte. (Sections 11.2, 11.8 and 11.18.)
- **Byte for byte identical**: Byte for byte identical: two files that agree in every character. (Section 16.11.)
- **Byte-identical**: two files with exactly the same bytes. (Section 0.24.)

**C**

- **C** (charge conjugation): the exchange of particles and antiparticles; CP: C combined with a mirror reflection of space. (Sections 21.35 and 22.17.)
- **C1** (a consequence of T1): a T1 pair taken as the complete classical source of the author's metric is a zero source, and Einstein's equations then have no solution for $H > 0$. (Sections 0.2 and 17.20.)
- **C2**: Source conditions (from the $a_4$ equations): C1 no component of the source depends on $x_8$ and $q_{48} = q_{84} = 0$; C2 $p_3 + p_t = 2p_8$; C3 for the linear member $a_4 = AHx_4 + a_0$: $p_3 = p_t = p_8$ and a constant $\rho$. (Section 17.20.)
- **C3**: Source conditions (from the $a_4$ equations): C1 no component of the source depends on $x_8$ and $q_{48} = q_{84} = 0$; C2 $p_3 + p_t = 2p_8$; C3 for the linear member $a_4 = AHx_4 + a_0$: $p_3 = p_t = p_8$ and a constant $\rho$. (Section 17.20.)
- **Cancellation**: the loss of digits when two nearly equal numbers are subtracted. (Sections 1.4 and 1.8.)
- **Canonical**: The canonical one is fixed by the vielbein postulate (below). (Section 6.13.)
- **Canonical anticommutation relations**: Because of this sign, operators of different modes anticommute; together these rules give the canonical anticommutation relations. (Sections 5.34 and 5.37.)
- **Canonical anticommutator**: the rule $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$ (times the delta function) that canonical quantisation of the Lagrangian gives. (Sections 10.12, 21.25 and 21.29.)
- **Canonical conjugate**: the operator $\Psi^\dagger_A$ that the Lagrangian pairs with $\Psi_A$; the question of the notebook is whether it equals the Hilbert adjoint $\Psi_A^*$. (Sections 5.37 and 10.18.)
- **Canonical Hartree-Fock equations**: It depends on the occupied orbitals only through $\rho$, which does not change when the occupied orbitals are mixed among themselves by a unitary matrix; such a mixing can make the Hermitian matrix $\Lambda$ diagonal, which gives the canonical Hartree-Fock equations $\hat F\phi_a = \epsilon_a\phi_a$. (Section 13.6.)
- **Canonical history**: the author's metric leaves the function $a_4(x_4)$ free; the author requires only that the extra times deflate ($a_4' > 0$). The linear member with the constant rate $a_4' = AH$ and $A = 1$ is the canonical history of the Revision record (ASSUMED, a prescribed choice); Notebook 12c also uses the faster member $A = 2$. (Sections 12.2, 12.12 and 12.24.)
- **Canonical matrix**: the fixed list of states the solver computes: particle numbers $N = 8, 136, 688$; couplings $\lambda = 0, \pm\lambda_1, \pm\lambda_2$; slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$; and temperatures $T = 0.01, 0.02, 0.05$ (in units of the mass $m$) for $\lambda = 0, \pm\lambda_1$. (Sections 15.1, 15.13 and 16.3.)
- **Canonical numerics** of the Rust solver: $G = 900$ RK4 steps and its standard tolerances. (Sections 16.6 and 16.11.)
- **Canonical quantisation**: After canonical quantisation (Chapter 10) the 16 components of the field dirac16complex are no longer numbers but operators $\Psi_A$, $A = 1, \dots, 16$: rules that turn one state of the quantum system into another. (Section 21.25.)
- **Canonical spin connection** $\omega_{\mu ab}$: the connection that makes the gammas $\gamma^\mu = e^\mu{}_a\gamma^{(a)}$ covariantly constant (the *vielbein postulate*); it is antisymmetric in $a, b$. $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ enters the covariant derivative $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$. (Sections 6.4, 7.18, 7.26, 8.4, 8.14 and 18.19.)
- **Capture**: `re.search` looks for a pattern in that text: `\d+` matches one or more digits, round brackets around a part of the pattern capture what that part matches, `.*?` matches any text up to the next part of the pattern, and `\(` matches a round bracket itself. (Section 12.25.)
- **cargo**: cargo is Rust's program that turns the Rust code of a program into a program that the computer can run (it builds it). (Sections 0.8 and 0.12.)
- **Carry a representation**: One says that the 16 components carry a representation of the group. (Section 5.11.)
- **Cauchy problem**: This is the initial-value problem, also called the Cauchy problem. (Section 8.16.)
- **Cells**: Every worked example of the book is a Jupyter notebook: a file (with the ending `.ipynb`) that holds text and Python code in cells, together with everything the code printed and drew when it ran. (Sections 0.7, 16.14 and 16.18.)
- **Central difference**: The central difference: $\frac{f(x + h) - f(x - h)}{2h} = f'(x) + \frac{h^2}{6} f'''(x) + \dots$. (Sections 2.18, 3.30, 6.14, 7.9 and 21.23.)
- **Central finite differences**: They are replaced by central finite differences, $\partial F \approx (F(x + h) - F(x - h))/(2h)$, whose error falls like $h^2$ as the step $h$ shrinks (the Taylor series: the terms of first and third order of $F(x + h)$ and $F(x - h)$ cancel in the difference, up to the error term $\frac{h^2}{6}F'''$). (Section 9.30.)
- **Centred average**: So the centred difference and the centred average of the two neighbours half a cell away are second-order approximations of $f'$ and $f$ at the midpoint, and their errors contain only even powers of $h$ (the next terms are $h^4$, $h^6$, ...). (Section 16.14.)
- **Centred difference**: The growth rate at the end of the run is computed by a centred difference, the change of $\ln(u^\dagger u)$ over the last two steps divided by their length, which approximates the derivative at the middle point; the first-order prediction is evaluated at that middle point. (Sections 8.29 and 16.14.)
- **Chain matrix**: The $3 \times 3$ chain matrix $T_3$ has 2 on the diagonal, $-1$ just above and just below it, and 0 elsewhere. (Section 1.34.)
- **Chain rule**: if $f$ depends on $z$ and $z$ on $x_8$, then $\partial f/\partial x_8 = (df/dz)(\partial z/\partial x_8)$. (Sections 2.22 and 3.2.)
- **Change of basis**: two sets of matrices are related by a change of basis when an invertible matrix $Q$ gives $\gamma^a = Q\,\hat\gamma^a Q^{-1}$ for every $a$. Writing the column $\Psi = Q\chi$ then turns every equation written with one set into the same equation written with the other. (Section 4.19.)
- **Channel**: Branching probability: the probability that a decaying particle decays in one particular way (one channel). (Section 21.35.)
- **Character** of a map $M$: the sign $\chi$ in $M^\dagger CM = \chi C$. It says whether $S$ keeps ($\chi = +1$) or reverses ($\chi = -1$) its sign under $\Psi \to M\Psi$. (Sections 18.2 and 18.8.)
- **Characteristic function**: a function of $\varepsilon$ whose zeros are exactly the levels. (Sections 19.2, 19.12 and 19.15.)
- **Characteristic polynomial**: $p(\lambda) = \det(M - \lambda I)$, a polynomial in $\lambda$ whose roots are the eigenvalues. (Sections 1.34, 1.40 and 4.9.)
- **Charge** $Q$ and **charge current** $J$: a number carried by a field whose density obeys an exact local conservation law, so that the charge of a region changes only by what flows through the boundary of the region (the law is proved at every point with $0 < z < \pi/2$; at the edge $z = \pi/2$ the no-flux condition, that no charge flows through the edge, is ASSUMED, not derived, and only under it is the total charge of a universe constant), and the flow of this number through space (Chapters 10, 18 and 21). (Sections 0.2, 10.25, 20.2, 21.2 and 21.22.)
- **Charge balance**: Flux: the amount of charge that flows through a surface per unit time; charge balance: the charge inside a region changes exactly by the flux through its boundary. (Sections 21.18 and 21.22.)
- **Charge conjugation**: a map that turns a field into a field of the opposite charge. (Sections 5.28, 7.29, 7.32 and 21.8.)
- **Charge current**: charge $Q$ and charge current $J$: a number carried by a field whose density obeys an exact local conservation law, so that the charge of a region changes only by what flows through the boundary of the region (the law is proved at every point with $0 < z < \pi/2$; at the edge $z = \pi/2$ the no-flux condition, that no charge flows through the edge, is ASSUMED, not derived, and only under it is the total charge of a universe constant), and the flow of this number through space (Chapters 10, 18 and 21). (Section 0.2.)
- **Charge density**: What is the charge density of a spinor field, the quantity whose total stays constant in time when no charge flows in or out through the edges of space? (Sections 5.1, 5.6, 5.32, 7.28, 18.26, 20.2, 20.10, 20.12, 20.15, 21.2 and 21.22.)
- **Charge matrix**: The charge matrix is the product of the four space-like gammas. (Sections 5.4, 20.2, 21.2, 21.7 and 21.14.)
- **The charge of the conjugated field**: The charge of the conjugated field, line by line, for $\Psi' = \Gamma\Psi^{\dagger T}$. (Section 21.26.)
- **Charge operator**: Charge operator $Q = \sum_{A,C}\Psi^\dagger_A B_{AC}\Psi_C$ (the integral of the charge density $\Psi^\dagger B\Psi$ for one point). (Section 21.29.)
- **Charge sloshing**: the loop moves the charge back and forth between regions instead of settling. (Sections 13.21 and 13.24.)
- **Charge-conjugation matrix** $\mathcal{C}$: a constant matrix for which $M = \mathcal{C}C$ obeys the intertwiner condition (the definition of the Revision record); same mass for $s = +1$, mass reversed for $s = -1$. In Notebook 05c, section 4 shows that then $\Psi^c = \mathcal{C}\bar\Psi^T$ solves the field equation with $V$ (same mass) or with $-V$ (mass reversed) whenever $\Psi$ solves it. (Sections 5.1, 5.28, 5.32, 7.29, 7.32, 21.2, 21.8 and 21.14.)
- **Chart**: A chart is a choice of coordinates. (Section 17.20.)
- **Chebyshev interpolation**: the polynomial through the values of a function at the Chebyshev nodes $s_j = 1 + \cos\theta_j$, $\theta_j = \pi(j + 1/2)/N$; for smooth functions it is accurate to many digits. (Section 22.11.)
- **Chebyshev nodes**: The Chebyshev nodes are the slices $s_j = 1 + \cos\theta_j$ with $\theta_j = \pi(j + \tfrac12)/56$, $j = 0, \ldots, 55$ (`0.5 * END` is 1). (Section 22.12.)
- **Check**: a statement that must be true. The helper `check(condition, name)` of the set-up cell stops the notebook with an *AssertionError* when the condition is false, and prints `PASS name` when it is true. (Sections 0.4, 0.7, 0.12, 0.20, 5.9 and 23.2.)
- **Checker**: Verifier and checker: a program of the Revision record that recomputes a result (exactly, with Wolfram or with sympy, or numerically, with Rust or Python) and writes a report: a JSON file that lists named checks, each with a verdict such as PASS. (Section 23.2.)
- **Chemical potential** $\mu$: the energy that fixes the average particle number. (Sections 13.9, 13.26, 13.30, 15.26, 15.29, 16.23, 21.2, 21.5 and 21.35.)
- **Chiral halves**: the components 1 to 8 (chirality $\Gamma = -1$) and 9 to 16 ($\Gamma = +1$); $P_- = \mathrm{diag}(1_8, 0)$ and $P_+ = \mathrm{diag}(0, 1_8)$. (Sections 5.1, 5.5, 5.16, 18.2 and 18.8.)
- **Chiral projectors**: $P_\mp = \frac12(I \mp \Gamma)$ with the chirality $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$; $P_-$ keeps components 1 to 8, $P_+$ components 9 to 16. (Sections 10.37 and 18.2.)
- **Chirality** $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$: the product of all eight gammas in the author's order. (Sections 0.2, 4.5, 5.5, 10.9, 18.2, 18.8, 19.15, 19.20, 20.2, 20.10, 20.15, 21.2, 21.7 and 21.14.)
- **Chirality image**: for a field $\Psi$, the field $\chi = \Gamma\Psi$. Because $\Gamma^2 = I_{16}$, also $\Psi = \Gamma\chi$: the image carries exactly the same information, written in other variables. (Section 10.48.)
- **Chirality matrix** $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$: the product of all eight gammas; it anticommutes with every $\gamma^{(a)}$ and $\Gamma^2 = 1$. (Sections 7.32 and 14.10.)
- **Chirality partner**: $\Gamma\Psi$. (Sections 21.2 and 21.22.)
- **Chirality product**: the product $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)} \cdots \gamma^{(x_7)}$ of all eight gammas, in this order (the author's order); the Revision record calls it the chirality. Here it is only a product of eight matrices. (Section 4.19.)
- **Christoffel symbols** $\Gamma^a{}_{bc}$: numbers built from first partial derivatives of the metric; the geometry of the book explains their meaning. Here they are only an exercise in partial derivatives. (Sections 2.19, 2.22, 3.15, 3.21, 3.29, 6.3, 6.13, 7.18, 7.26, 8.4, 8.14, 9.9, 9.16, 11.2, 11.18, 12.2, 12.15, 17.2, 17.20 and 18.19.)
- **Circle of latitude**: A circle of latitude $\theta = \theta_0$ with $0 < \theta_0 < \pi/2$, run through at unit speed, is NOT a geodesic: along it $d^2\theta/ds^2 = 0$, while the right side is $\sin\theta_0\cos\theta_0\,(d\varphi/ds)^2 = \sin\theta_0\cos\theta_0/(a^2\sin^2\theta_0) = \cot\theta_0/a^2 \ne 0$ (unit speed means $a\sin\theta_0\,d\varphi/ds = 1$). (Section 3.16.)
- **Class**: A class is a recipe for objects that carry their own data: `XorShift64Star(seed)` makes a generator object, and the function `__init__` (run when the object is made) stores the seed as its state `self.state`. (Sections 1.54, 7.17, 15.9 and 18.20.)
- **Classical bilinears**: A pair made of a solution $\Psi$ with $(m, \lambda)$ and its partner $\Gamma\Psi$ with $(-m, -\lambda)$, both in the same gravitational field, has total current zero and total charge zero, as classical bilinears (ordinary numbers for dirac16complex00, elements of the Grassmann algebra for dirac16complex). (Sections 19.11 and 21.19.)
- **Classical field**: a field whose values are numbers, as everywhere in Chapter 0, and not the operators of quantum theory (Chapter 7). (Section 0.2.)
- **Classical fourth-order Runge-Kutta method (RK4)**: The Rust program of the Revision record solves them by the shooting method: it guesses an energy, integrates the equations from one end to the other with the classical fourth-order Runge-Kutta method (RK4) in 900 steps, measures by how much the condition at the far end fails, and corrects the energy with Newton's method. (Section 2.1.)
- **Classical Runge-Kutta method of fourth order**: `rk4` is the classical Runge-Kutta method of fourth order (Chapter 2). (Section 18.27.)
- **Clifford algebra** Cl(4,4): the set of all real combinations of products of eight matrices that satisfy the Clifford relation with four signs $+1$ and four signs $-1$. (Sections 4.3 and 4.15; the opening of Chapter 4.)
- **Clifford product**: a product $\gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ of $k$ *different* gammas, taken in the order $x1, \dots, x8$; $k$ is its degree; it is even or odd with $k$. The degree-0 product is $1$. (Section 5.16.)
- **Clifford relation**: $\gamma^a \gamma^b + \gamma^b \gamma^a = 2 \eta^{ab} I_{16}$ for all $a, b$: each gamma matrix squares to $+I_{16}$ (space-like direction) or $-I_{16}$ (time-like direction), and two different gamma matrices anticommute. (Sections 1.28, 1.32, 4.1, 4.3, 4.7, 4.11, 4.19, 5.2, 6.13, 8.2, 17.20, 21.7 and 21.14.)
- **Closed shell**: A particle number $N$ is a closed shell when the filling ends exactly at the end of a group of degenerate levels (levels equal within $10^{-9}$), so that the state is unique. (Sections 14.21, 14.24, 15.2 and 17.2.)
- **Closed-shell slab**: the Kohn-Sham states of the model, uniform along 3-space but not along the hidden coordinate $y$, with complete lattice shells filled. (Section 14.30.)
- **Cobweb diagram**: a picture of an iteration: go vertically to the curve $G$, horizontally to the diagonal, vertically again, and so on. (Sections 13.24 and 13.25.)
- **Code**: We describe such a matrix by the code of each row: the code $+5$ in row 2 means that the only nonzero entry of row 2 is $+1$ in column 5, so $(Mu)_2 = +u_5$; the code $-0$ means $-u_0$. (Section 4.2.)
- **Code cell**: A markdown cell holds text; a code cell holds Python code. (Section 0.7.)
- **Coefficient**: A linear expression in some variables $p, q, \dots$ is a sum of the variables, each multiplied by a fixed number (or, below, a fixed matrix), its coefficient: $\alpha p + \beta q$ is linear, while $p^2$, $pq$ and $\sqrt{p^2 + q^2}$ are not. (Sections 4.1, 7.10 and 7.16.)
- **Coefficient functions**: This form shows the structure that every proof below uses: $K$ is a sum of coefficient functions of the gravitational field ($e^\mu{}_a$, $\omega_{\mu bc}$; and $\sqrt{|g|}$ in front of $\mathcal{L}$) times bilinears whose kernels are $C\gamma^{(a)}$ and $C\gamma^{(a)}S^{bc}$, $CS^{bc}\gamma^{(a)}$, products of one or three gammas after $C$. (Section 18.4.)
- **Coefficient matrix**: A *system* is a list of such equations; its coefficients form the coefficient matrix $A$ (one row per equation), and the system reads $Ay = 0$. (Section 5.16.)
- **Coefficient ring**: the symbols $E = e^{a_4}$, $s = \sin^{1/6}z$, $c = \cos z$, $A_1 = a_4'$ and the second and third derivatives $A_2 = a_4^{\prime\prime}$, $A_3 = a_4^{\prime\prime\prime}$, together with $H$, $m$, $\lambda$, in which every coefficient is written; with the rule $c^2 = 1 - s^{12}$ it allows an exact test whether an expression is zero. (Sections 7.26 and 7.32.)
- **Cofactor**: $C_{rc}$, the cofactor, contains no entry of row $r$. (Section 11.13.)
- **Cofactor expansion**: (The record's sympy verifier ran a different exhaustive comparison on the same 266,304 pairs: the literal determinant against a determinant computed by an independent method, the cofactor expansion, which writes a determinant as a sum over the entries of its first row, each entry times the determinant of the smaller matrix left when its row and column are removed, with the signs $+, -, +, \dots$ in turn; its check is `gkd_literal_equals_cofactor_expansion` in `python-lovelock-report.json`. (Section 1.48.)
- **Colour bar**: The tick labels are the names $x1$ to $x8$, the axes are the frame indices $a$ (rows) and $b$ (columns), and each panel gets its own colour bar (`fig.colorbar`), the scale that translates colours into numbers. (Sections 6.14 and 17.11.)
- **Colour map**: Two tools of matplotlib: a colour map made of a short list of colours, and a coloured square for a legend. (Sections 0.17, 1.25, 5.10 and 21.15.)
- **Colour scale**: A colour scale turns a number into a colour: `DIVERGING` runs from dark blue for $-1$ through light grey for 0 to red for $+1$, and `SEQUENTIAL` from almost white for 0 to dark blue for large values. (Sections 10.10 and 18.9.)
- **Column**: A column $u$ is a list of $n$ numbers $u_0, \dots, u_{n-1}$ written one below the other; the matrix acts on it by $(Mu)_i = \sum_j M_{ij} u_j$. (Section 4.2.)
- **Combination**: A combination of matrices $M_1, \dots, M_N$ is $c_1M_1 + \dots + c_NM_N$ with numbers $c_j$; the span is the set of all combinations. (Section 5.11.)
- **Command**: one line typed into a terminal and run by pressing Enter. (Section 23.2.)
- **Comment**: A line that starts with `#` is a comment: Python skips it; it is there for the reader. (Sections 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 14.11, 15.9, 17.11, 20.11 and 21.15.)
- **Comment lines**: Its first part repeats the complete run instructions of Section 0.11 as comment lines: every line that starts with `#` is a comment, which Python skips. (Sections 0.13, 4.8, 13.14, 16.12, 18.9, 19.16 and 22.12.)
- **Commutant**: all matrices $X$ that commute with every matrix of a list. (Sections 5.11, 5.16 and 14.30.)
- **Commutative**: They are not commutative: in general $AB \neq BA$. (Section 4.2.)
- **Commutator**: where $[A, B] = AB - BA$ is the commutator. (Sections 1.28, 1.32, 4.7, 5.18, 5.21, 5.26, 6.7, 6.13, 7.28, 8.4, 10.11 and 14.11.)
- **Commute**: The components of the field dirac16complex00 are ordinary (complex) numbers, which commute: $\Psi_r\Psi_c = \Psi_c\Psi_r$. (Sections 1.10, 1.28, 4.2, 4.9, 5.9, 5.29, 7.32, 14.10 and 18.8.)
- **Commute with all gammas**: $X\gamma^a = \gamma^a X$ for all eight $a$. (Section 4.19.)
- **Commuting** and **complex conjugation**: ordinary numbers are commuting, the order of a product does not matter ($ab = ba$), while the anticommuting numbers of Chapter 7 have $ab = -ba$; complex conjugation changes the sign of the imaginary part of every complex number, $a + i b \to a - i b$ (Chapter 1). (Sections 0.2, 1.28, 21.2 and 21.7.)
- **Commuting, anticommuting components**: the components of dirac16complex00 are ordinary numbers ($\Psi_r\Psi_c = \Psi_c\Psi_r$); those of dirac16complex are *anticommuting* (Grassmann) numbers, $\Psi_r\Psi_c = -\Psi_c\Psi_r$, so that exchanging two factors in a product costs a sign. We write $\epsilon = +1$ for commuting and $\epsilon = -1$ for anticommuting components. (Sections 5.32 and 21.14.)
- **Completeness**: Then $W$ is invertible with $W^{-1} = W^\dagger$, and so also $WW^\dagger = I_{16}$, which written out is the completeness relation $\sum_s u_su_s^\dagger + \sum_s v_sv_s^\dagger = I_{16}$. (Sections 10.20 and 10.25.)
- **Completion** (of theorem T3): the completion record of T3 (2026-10-08). An adversarial verification found no error in the statement or the proof of T3, but gaps in its verification; the completion record closes the three exact ones: the Kohn-Sham coefficients read from the record in both engines (Section 19.8), the filling convention carried onto the partner (Section 19.9), and statement S6, the 16-component expectation rule (Section 19.10). Its Wolfram report passes 3 of 3 checks and its Python report 7 of 7. (Section 19.1.)
- **Complex conjugate**: for a complex number $z = a + ib$ ($a$, $b$ real) it is $z^* = a - ib$. (Sections 1.10, 1.40, 2.7, 4.9, 5.9, 5.32, 7.4, 10.9, 21.2 and 21.14.)
- **Complex conjugation**: replacing every number by its complex conjugate ($i \to -i$). On a real column it changes nothing: it is the identity. (Sections 0.2 and 7.32.)
- **Complex number**: $z = a + ib$ with real numbers $a$ (the real part, $\mathrm{Re}\,z$) and $b$ (the imaginary part, $\mathrm{Im}\,z$). (Sections 1.10, 1.16, 2.7, 4.9 and 4.11.)
- **Complex plane**: the plane in which $z = a + ib$ is the point (or the arrow from the origin to the point) $(a, b)$; horizontal axis $\mathrm{Re}$, vertical axis $\mathrm{Im}$. (Section 1.16.)
- **Component**: one number of a tensor, such as $E^{x_1}{}_{x_1}$; a diagonal component has $h = j$. (Sections 1.18, 1.24, 11.2, 11.26 and 21.2.)
- **The components along the deflating history**: The components along the deflating history (Sections 11.20 to 11.27). (Section 11.1.)
- **COMPUTED**: a status label: the statement is a number from a numerical (floating-point) computation, given with its measured uncertainty and the file that holds it. (Sections 0.3, 0.20, 3.1, 4.21, 5.40, 6.1, 6.30, 8.1, 11.28, 12.31, 13.38, 14.32, 15.31, 16.26, 17.23 and 22.27.)
- **Condensate**: a configuration that depends only on the time $x_4$. (Sections 9.18, 9.24, 9.29, 12.2, 12.19, 12.29, 20.12 and 20.15.)
- **The condition**: The condition, line by line. (Sections 21.25 and 21.32.)
- **Conditional expression**: `tiny == 1` is True when exactly one is that small; `x if condition else y` is a conditional expression, which gives `x` when the condition is True and `y` otherwise. (Sections 0.17 and 1.41.)
- **Conditioning**: how strongly a result reacts to small errors of the input. (Sections 15.29 and 16.23.)
- **Configuration**: any field $\Psi$, that is, 16 components $\Psi_1(x), \dots, \Psi_{16}(x)$ given at every point $x$, whether or not it obeys the field equations. (Sections 18.2, 20.2 and 20.10.)
- **Conjugate** $z^* = a - ib$: the mirror image of $z$ in the real axis. (Sections 1.16 and 7.11.)
- **Conjugate transpose** $M^\dagger$: transpose $M$ and replace every entry $x + iy$ by $x - iy$. (Sections 1.36, 1.40, 4.9, 4.11, 5.9, 5.32, 8.22, 20.16, 21.2 and 21.14.)
- **Conjugation**: the rule that turns an element $F$ into $F^*$. For complex Grassmann numbers the generators come in pairs $\theta$ and $\bar\theta = \theta^*$; the conjugation exchanges the two members of every pair, replaces every coefficient by its complex conjugate and REVERSES the order of every product: $(FG)^* = G^* F^*$. (Sections 7.11 and 7.16.)
- **Connection coefficients**: The $n^3$ numbers $\Gamma^a{}_{bc}$ at each point are the connection coefficients; they are chosen so that $\nabla_b V^a$ is a tensor, which fixes how they change between systems of coordinates (we do not need that rule). (Section 3.15.)
- **Conservation**: Conservation means $\nabla_\mu T^\mu{}_\nu = 0$ for all eight. (Sections 9.9, 9.16, 11.2, 12.2, 12.15, 12.24 and 17.2.)
- **Conservation law**: the statement $\nabla_\mu T^\mu{}_\nu = 0$ (the covariant divergence vanishes): energy and momentum are neither created nor destroyed, they only flow. (Sections 9.9, 15.19, 17.20 and 20.20.)
- **Conservation law along $y$**: This is the conservation law along $y$ (ks-theory.json, emt.conservationY). (Section 15.16.)
- **Conserved**: Conserved: the same number at every point of the path. (Section 3.34.)
- **Conserved number**: a number whose total before a process equals its total after it, in every process that happens. (Section 21.35.)
- **Conserved quantity**: a number whose value does not change in time for every solution. (Sections 20.2 and 20.22.)
- **Consistent**: If $MM^\ast = 1$ this is automatically true, and the condition is called consistent; otherwise it forces further conditions on $\Psi$ (possibly $\Psi = 0$). (Sections 5.29 and 21.10.)
- **Constant**: They are constant: the same matrices at every point and at every time. (Sections 4.4 and 21.18.)
- **Constraint**: an equation with no second derivative $a_4''$. (Sections 11.21, 12.2, 12.15, 12.24, 17.2 and 17.20.)
- **Constraint propagation**: The derivative of the constraint is $3a_4'$ times the evolution factor: this is the constraint propagation of the record (`a4-equations.json`, key `generalSource`, entry `constraint_propagation`; `python-a4-report.json`, check `bianchi_x4`). (Section 11.22.)
- **Contact interaction**: $w(\mathbf r, \mathbf r') = g_c\,\delta(\mathbf r - \mathbf r')$; it acts only when two particles are at the same point. (Sections 13.19, 13.35 and 14.30.)
- **Contour map**: `ax.contourf(A, B, E_map, levels=30, ...)` colours the plane of the angles $(\alpha, \beta)$ in 30 bands of equal energy (a contour map: each band joins the points with nearly the same value), and the colour scale is labelled with the energy and its unit $t$. (Section 13.14.)
- **Contracted Bianchi identity**: For every metric the Einstein tensor has zero divergence, $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$ for each $\nu$ (the divergence is the covariant derivative with its index $\mu$ set equal to the upper index of $G$ and summed; a standard theorem, the contracted Bianchi identity; quoted, ASSUMED in general). (Section 3.25.)
- **Contraction**: setting an upper and a lower index equal and summing over it, as in $\delta^a_a$ or $v^a w_a$. (Sections 1.26, 1.32, 1.47 and 3.14.)
- **Control**: a comparison case computed with the same method as the case under test; a negative control (see that entry) is one in which the effect must NOT occur. In Chapter 19 the control C is the universe of mass $-M$ with the UNtransformed tip, and the wrong partner D the one with the reversed coupling. (Sections 19.2, 19.10 and 19.12.)
- **Control metric**: Suppose instead the extra times also inflated, with the scale factor $e^{+a_4}\sin^{1/6}z$ (a control metric, not the author's). (Section 21.17.)
- **The conventions of the book**: The conventions of the book (Revision record, `Revision/SPEC.md` section 4; record formula `equation_of_state_definitions`): the energy density and the pressures are (the formula is displayed in that section). (Section 9.4.)
- **Convergence**: Basis: the set of instantaneous levels in which the evolving orbital is expanded; a truncated basis keeps only some of them, and convergence means the result stops changing when more are kept. (Section 22.11.)
- **Convergence factor**: Error: the distance $x - x^*$ from the fixed point; convergence factor: the number by which one step multiplies the error near the fixed point. (Sections 13.21 and 13.24.)
- **Convergence order**: the power $q$ in "error $\approx$ constant $\times h^q$"; halving $h$ divides the error by $2^q$. (Section 12.24.)
- **Convergence ratio**: So the convergence ratio $(x(h) - x(h/2))/(x(h/2) - x(h/4))$ is 4 up to a correction of order $h^2$. (Section 16.4.)
- **Coordinate**: a number that says where a point is along one direction. The author's universe has eight coordinates, named $x_1, x_2, \dots, x_8$. (Sections 0.16, 3.2, 3.12, 3.21, 3.34, 4.9, 6.13, 6.27, 7.26, 8.14, 8.22, 8.28, 8.35, 9.16, 11.2, 11.18, 11.26, 12.2, 12.15, 12.29, 14.10, 17.2, 17.10, 17.20, 19.15, 19.20, 20.10, 20.15 and 21.2.)
- **Coordinate covariant derivative**: They enter the coordinate covariant derivative of a vector field, $\nabla_\mu V^\nu = \partial_\mu V^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}V^\lambda$, the derivative that compares the vector at two points correctly although the coordinate directions change between them. (Section 6.3.)
- **Coordinate density**: Coordinate density: the same per unit of the coordinate $y$ (it contains the volume factor $e^{6Hy}$). (Sections 15.13, 15.19 and 19.20.)
- **Coordinate gammas**: The coordinate gammas are $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (the frame gamma of the same direction divided by its frame factor); they obey $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$ with the inverse metric $g^{\mu\mu} = \eta_{\mu\mu}/f_\mu^2$. (Sections 7.18, 7.26, 8.2 and 9.2.)
- **Coordinate index**: The lower index $\mu$ is a coordinate index: it numbers the coordinates. (Sections 6.2 and 6.13.)
- **Coordinate label**: the name of one of the eight coordinates $x_1, \dots, x_8$ of the author's metric ($x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times, which deflate exponentially, $x_8$ the hidden direction). Programs number them $0, 1, \dots, 7$: the number 0 stands for $x_1$, the number 7 for $x_8$. (Section 11.8.)
- **Coordinate momenta**: Take a wave $\Psi = u(x_4)\,e^{i(q_1x_1 + q_5x_5)}$ with the coordinate momenta $q_1$ (along 3-space) and $q_5$ (along an extra time). (Section 10.39.)
- **Coordinate momentum** $q_a$ and **frame momentum** $k_a$: a wave $e^{iq_ax_a}$ has the coordinate momentum $q_a$; measured with proper lengths its momentum is $k_a = q_a/f_a$, the frame momentum. (Sections 10.3 and 10.42.)
- **Coordinate plane**: With $a$ before $b$ in the order $x1, \dots, x8$ there are $8 \cdot 7/2 = 28$ generators, one for each coordinate plane $(a, b)$. (Section 5.12.)
- **Coordinate wave number** $q_a$ and **frame momentum** $k_{(a)} = q_a/f_a$, where $f_a$ is the scale factor: the wave $e^{iq_a x_a}$ has $q_a$ radians of phase per unit of coordinate length and $k_{(a)}$ radians per unit of proper length. (Sections 8.24 and 8.28.)
- **Coordinates on the sphere** of radius $a$: $\theta$ (from $0$ at the north pole to $\pi$ at the south pole) and $\varphi$ (around the axis); the point is $(a\sin\theta\cos\varphi,\ a\sin\theta\sin\varphi,\ a\cos\theta)$. (Section 3.21.)
- **Corollary**: a statement that follows from a theorem in a few lines; corollary C1 of Chapter 20 is an example. (Sections 20.2 and 20.10.)
- **Correlation energy**: the exact ground-state energy minus the Hartree-Fock energy (never positive). (Sections 13.7 and 13.13.)
- **Cosmic microwave background**: The universe is filled with the photons of the cosmic microwave background, the thermal radiation left over from the hot early universe, today at the temperature 2.7255 K (D. J. Fixsen, Astrophys. (Section 21.4.)
- **Cosmological constant**: Couplings: $\alpha_1, \alpha_2, \alpha_3$ weigh the three Lovelock tensors; $\Lambda$ is the cosmological constant; $\kappa > 0$ measures the strength of gravity. (Sections 3.26, 3.29, 12.2, 17.2, 20.2 and 20.10.)
- **Cosmological-constant-like**: Radiation-like: $w_{\rm eff} = 1/3$; dust-like (dark-matter-like): $w_{\rm eff} = 0$; cosmological-constant-like: $w = -1$; phantom: $w < -1$. (Section 22.22.)
- **Coulomb interaction**: $w = 1/|\mathbf r - \mathbf r'|$, the repulsion of two electrons (atomic units). (Section 13.19.)
- **Counting**: Counting: for each of the six directions $i \in \{x_1, x_2, x_3, x_5, x_6, x_7\}$ there are $\Gamma^i{}_{ix_4}$, $\Gamma^i{}_{x_4i}$, $\Gamma^i{}_{ix_8}$, $\Gamma^i{}_{x_8i}$, $\Gamma^{x_4}{}_{ii}$ and $\Gamma^{x_8}{}_{ii}$: $6 \times 6 = 36$ symbols, plus $\Gamma^{x_8}{}_{x_8x_8}$: 37 nonzero symbols of the 512, of which 25 are different. (Section 12.4.)
- **Couplings**: $\alpha_1, \alpha_2, \alpha_3$ weigh the three Lovelock tensors; $\Lambda$ is the cosmological constant; $\kappa > 0$ measures the strength of gravity. (Sections 12.2, 12.15, 12.19, 17.2, 19.20 and 20.15.)
- **Covariant constancy**: Defining property of a spinor connection: $[\Omega_\mu, \gamma^a] = -\sum_b \omega_\mu{}^a{}_b\gamma^b$; covariant constancy of the curved gammas $\gamma^\mu = \sum_a e_a{}^\mu\gamma^a$: $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$. (Section 6.27.)
- **Covariant derivative along the curve**: The right side needs $V$ only on the curve, so it defines the covariant derivative along the curve for any $V(\lambda)$. (Section 3.16.)
- **Covariant derivative** of a spinor: $D_\mu \Psi = \partial_\mu \Psi + \Omega_\mu \Psi$ ($\partial_\mu$ is the partial derivative with respect to $x^\mu$). (Sections 3.21, 5.28, 6.1, 6.13, 6.21, 7.18, 7.26 and 8.35.)
- **Covariant divergence** $\nabla_\mu T^\mu{}_\nu$: the derivative of the tensor summed over its upper index, corrected by the Christoffel symbols. (Sections 9.9, 9.16, 9.29, 11.26, 17.2 and 17.20.)
- **Covariantly constant**: It makes the gammas covariantly constant: $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$ for all 64 pairs $(\mu, \nu)$ (PROVED; `python-field-theory.json`, check `covariant_constancy_D_mu_gamma_nu`). (Sections 8.4 and 14.11.)
- **Covector**: A covector is a set of $n$ numbers $W_a$ for every system of coordinates that changes by this rule. (Section 3.14.)
- **CP**: C (charge conjugation): the exchange of particles and antiparticles; CP: C combined with a mirror reflection of space. (Section 21.35.)
- **CPL**: $w(a) = w_0 + w_a(1 - a)$. (Section 22.22.)
- **CPL parametrisation**: CPL parametrisation: the formula $w(a) = w_0 + w_a(1 - a)$ for an equation of state that changes with the scale factor $a$ of the observed universe. (Section 22.2.)
- **Crate**: Rust, cargo, program: Rust is a programming language; cargo builds a Rust crate (a folder with a file `Cargo.toml` and source files) into a program file that the computer runs. (Sections 11.8, 15.14 and 19.21.)
- **Creation**: Creation of a universe: a process whose initial state has fewer universes than its final state. (Section 20.2.)
- **Creation operator** $a_p^\dagger$, **annihilation operator** $a_p$: add or remove a fermion in orbital $p$, with the sign $(-1)^{\nu_p}$, where $\nu_p$ is the number of occupied orbitals before $p$; on the 16 occupation-number states they are $16 \times 16$ matrices. (Sections 5.34, 13.4, 13.13, 21.26 and 21.29.)
- **Critical rate**: The right-hand side grows without limit, but $G$ has a largest value at the critical rate $v_c = \sqrt{(2 - 80\alpha_2)/(48\alpha_2)}$, where $G' = F = 0$. (Section 12.21.)
- **Cross-check**: The Revision record answers it with a second program that shares no code with the first and solves the same equations by a different method (the reference solver), and with a third program that compares the two, number by number, with a rule for the allowed difference that was written down before any comparison was made (the cross-check). (the opening of Chapter 16.)
- **Cross-section**: a number, with the units of an area, that measures how likely a collision or a reaction is. No cross-section for the creation of universes is computed or implied in this book. (Sections 18.2, 20.2 and 20.20.)
- **CSV**: a text table, one row per line, the cells separated by commas. (Sections 16.11 and 23.11.)
- **CSV file**: The Rust solver's record of the partner problems, a CSV file (comma-separated values: a table as text, one row per line, the cells separated by commas, the first line the column names). (Section 14.11.)
- **Cubic Hermite interpolation**: the value in the middle of a step from the values and the derivatives at its two ends. (Sections 2.24, 14.18, 15.8, 17.2, 17.20 and 22.12.)
- **Cubic Lovelock density** $L_{(3)}$: the third Lovelock scalar, of third order in the curvature: $L_{(3)} = 8(2T_1 + 8T_2 + 24T_3 + 3T_4 + 24T_5 + 16T_6 - 12T_7 + T_8)$, where $T_1, \dots, T_8$ are the eight cubic invariants made of three factors of the Riemann tensor, the Ricci tensor and the Ricci scalar (each written out in that section). (Section 11.15.)
- **Current** $J^a = -i\bar\Psi\gamma^{(a)}\Psi$: the conserved current of the phase symmetry $\Psi \to e^{i\alpha}\Psi$; its time component gives the charge. (Sections 5.4, 5.32, 7.28, 7.32, 14.12, 14.17, 18.26, 19.3, 20.2, 20.10, 21.2, 21.14 and 21.22.)
- **The current part**: The current part, line by line. (Section 21.19.)
- **Curvature**: What does not depend on the frame is curvature. (Sections 1.43, 6.17 and 8.4.)
- **Curvature of a plane** $K(a, b) = R^{ab}{}_{ab}$ (no sum): the curvature of the surface spanned by the directions $x_a$ and $x_b$. (Section 11.18.)
- **Curvature of that plane**: For the coordinate plane of $x_a$ and $x_b$, $\sigma(a, b) = R^{ab}{}_{ab}$ (no sum) is the curvature of that plane (the sectional curvature). (Section 3.29.)
- **Curvature of the coordinate plane**: is the curvature of the coordinate plane of $x_a$ and $x_b$ (its sectional curvature; "plane" means here the plane of the two directions $x_a$ and $x_b$ at one point). (Section 3.17.)
- **Curvature of the spinor connection** $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$: the 16 x 16 matrix with $D_\mu D_\nu\Psi - D_\nu D_\mu\Psi = F_{\mu\nu}\Psi$. (Sections 6.5 and 6.21.)
- **The curvature that the sums use** (Section 11.10): the mixed components $R^{x_4k}{}_{x_8k} = \sigma_kHa_4'\cot z$ carry the sign $\sigma_k = \pm 1$ of inflation or deflation, not of the space-like or time-like character, and $R^{x_4}{}_{x_8} = 0$ because three inflating and three deflating directions cancel; every nonzero $R^{ab}{}_{cd}$ has the weight 2. (Section 11.28.)
- **Curve**: A curve is a point that moves with a parameter $\lambda$ (a time, or a length along the curve): $x^a(\lambda)$. (Section 3.14.)
- **Curved Clifford relation**: They obey the curved Clifford relation. (Section 6.2.)
- **Curved gamma**: The constant gamma matrix of a direction carries the direction in parentheses, $\gamma^{(x4)}$; a gamma without parentheses, $\gamma^{x4}$ or $\gamma^\mu$, is a curved gamma (Section 6.2). (Sections 6.1, 6.13, 6.21 and 14.11.)
- **Cyclic property**: It has the cyclic property $\mathrm{tr}(AB) = \mathrm{tr}(BA)$. (Section 4.2.)

**D**

- **Dagger**: Take a column $\Psi$ of $n$ complex Grassmann components with generators $\psi_A = \Psi_A$ and the conjugate row $\Psi^\dagger$ with generators $\chi_A = \psi_A^*$ (the dagger $\dagger$ means transpose and conjugate). (Sections 7.12, 10.9 and 18.8.)
- **Dark energy**: Dark energy is the name for the unknown cause of the observed speeding-up of the expansion of the universe, and dark matter for the unseen matter that is detected only through its gravity. (Section 9.1.)
- **Dark matter**: Dark energy is the name for the unknown cause of the observed speeding-up of the expansion of the universe, and dark matter for the unseen matter that is detected only through its gravity. (Section 9.1.)
- **Data**: A field equation that contains the time derivative $\partial_4\Psi$ is used like this: one gives the field on the slice $x_4 = 0$ (a seven-dimensional set with the coordinates $x_1, x_2, x_3, x_5, x_6, x_7, x_8$), the data, and asks for the field at later times. (Section 8.16.)
- **Decorator**: The line `@lru_cache(maxsize=None)` above the function is a decorator: it wraps the function so that a result, once computed for some $n_2$, is remembered and returned at once the next time. (Section 16.24.)
- **Deep dive**: the way this book is written: every notion is defined, in plain words, before it is used; every derivation is written out line by line, each line followed by the rule that produced it from the line before; every worked example is a complete Jupyter notebook, printed in full, with the complete instructions for running it just before it and the explanation of every line of its code just after it; every number in the text names the notebook cell that computes it and, where it reproduces the Revision record, the record file and the check. (Section 0.1.)
- **Default value**: `exact_solutions(A)` returns a basis of all solutions of $Ay = 0$, each turned back into a $16 \times 16$ matrix, as `solution_basis` of Notebook 05b does (Section 5.17, In [3]): sympy's `DomainMatrix` over the rational numbers `QQ` finds the solutions by exact elimination, `nullspace()` returns one solution per row, and `reshape(n, n)` restores the matrix (`n=16` is a default value: the argument may be left out). (Sections 5.33, 9.30, 10.43, 13.25, 14.18 and 15.9.)
- **Defining property** of a spinor connection: $[\Omega_\mu, \gamma^a] = -\sum_b \omega_\mu{}^a{}_b\gamma^b$; covariant constancy of the curved gammas $\gamma^\mu = \sum_a e_a{}^\mu\gamma^a$: $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$. (Sections 6.7 and 6.27.)
- **Deflate**: The author's metric (the rule that gives the length of a small step in each direction; Section 0.14 introduces it from zero) makes ordinary space grow (inflate) and the three extra times shrink (deflate) exponentially as the time $x_4$ runs. (Sections 0.1, 0.14, 0.16, 3.12, 4.4, 8.2, 11.26 and 14.2.)
- **Deflate exponentially**: Coordinates (the author's names): $x_1, x_2, x_3$ = ordinary 3-space, which inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ = the time; $x_5, x_6, x_7$ = the three extra times, which deflate exponentially (scale factor $e^{-a_4}\sin^{1/6}z$, with $a_4$ increasing); $x_8$ = the hidden space direction, with $z = 6Hx_8$ between $0$ and $\pi/2$. (Sections 1.1, 2.1, 3.1, 3.5, 7.1, 11.2, 12.1, 17.2, 17.10, 17.20, 19.15, 19.20 and 21.2.)
- **Deflating**: shrinking. When $a_4$ grows, $e^{-a_4}$ shrinks: the extra times deflate exponentially while 3-space inflates. (Sections 8.28, 12.15 and 14.10.)
- **Deflating history**: the time dependence $a_4 = AHx_4$ with $A = 1$; as $x_4$ grows, 3-space inflates and the extra times deflate, both exponentially. (Sections 10.42, 18.26 and 20.1.)
- **Deflation rate**: the rate $a_4'$. While $a_4' > 0$ the scale factor $e^{-a_4}$ of the extra times shrinks exponentially, at the momentary rate $a_4'$. (Section 12.24.)
- **Degeneracy** $g$: the number of different orbitals that share one level. (Sections 15.2, 15.13, 16.20, 16.23, 19.2 and 19.20.)
- **Degree**: The number $k$ of factors is the degree of $\gamma_A$; the product is even if $k$ is even and odd if $k$ is odd. (Sections 4.13, 4.15, 5.3, 5.16, 7.10, 7.16 and 21.10.)
- **Delta function** $\delta^7(x - y)$: an idealised object that is zero whenever the point $x$ differs from $y$ and whose integral over the seven coordinates other than the time is 1. (Sections 5.34, 5.37 and 10.12.)
- **Delta-SCF**: the excitation energy as the difference of two self-consistent energies, with one particle moved from the highest occupied orbital (H) to the lowest empty one (L). (Sections 13.27, 13.30, 13.35, 15.13 and 16.11.)
- **Density** $S = \bar\Phi\Phi$, a real number. **Bilinear**: a number $\bar\Phi X \Phi$ with a 16 by 16 matrix $X$; a three-gamma bilinear has $X = \gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$ with three different directions. (Sections 11.2, 11.11, 12.29, 13.1, 13.24, 13.35, 14.30, 19.20 and 20.15.)
- **Density functional theory**: This chapter builds, from zero, the tool with which Chapters 14 to 16 compute the states of many quanta of the field dirac16complex in the author's primordial field: density functional theory, DFT for short, in the form of Kohn and Sham. (the opening of Chapter 13.)
- **Density matrix** $\rho(x, x')$: $\sum_a \phi_a(x)\,\phi_a^*(x')$ over the occupied orbitals; its diagonal $\rho(x, x)$ is the density. (Sections 13.13 and 13.19.)
- **Density operator** $\hat\rho$: a Hermitian matrix with eigenvalues between 0 and 1 that add up to 1; it describes a mixture of states with these probabilities. (Sections 13.26 and 13.30.)
- **Dependency order**: It re-runs every verifier and checker in dependency order (a program that reads the output of another runs after it), then demands that every committed output is unchanged byte for byte and that every report passes. (Section 23.2.)
- **Derivative**: $y'(t) = dy/dt$ is the rate of change of $y$ at time $t$, the slope of the graph of $y$. (Section 2.10.)
- **Determinant**: one number computed from a square matrix. For a diagonal matrix it is the product of the diagonal entries. (Sections 0.14, 0.16, 1.12, 1.20, 1.24, 1.40, 2.19, 3.6, 3.12, 5.3, 11.2, 11.8 and 12.3.)
- **Determinant of a diagonal matrix**: the product of its diagonal entries. (Section 2.22.)
- **Diagonal**: The rules of this book are diagonal: each squared step is multiplied by its own number $g_{ii}$, called the entry of the metric for the direction $x_i$, and the results are added: $ds^2 = g_{11}\, dx_1^2 + g_{22}\, dx_2^2 + \cdots + g_{88}\, dx_8^2$. (Sections 0.14, 1.5, 1.20, 2.19, 3.3, 11.2, 12.2 and 12.15.)
- **Diagonal / off-diagonal entry**: the entry $T^\nu{}_\mu$ with $\nu = \mu$ / with $\nu \neq \mu$. Off-diagonal entries describe flows of energy and momentum (for example $T^{x_4}{}_{x_1}$ is a flow of momentum along $x_1$) and stresses that shear. (Section 9.29.)
- **Diagonal frame**, scale factors $f_a$: $f_{1,2,3} = e^{a_4}\sin^{1/6}z$, $f_4 = 1$, $f_{5,6,7} = e^{-a_4}\sin^{1/6}z$, $f_8 = \cot z$; $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. (Sections 7.18, 8.2 and 8.35.)
- **Diagonal matrix**: a square table of numbers that is zero everywhere except on the line from the top left to the bottom right (the *diagonal*). The author's metric is an $8 \times 8$ diagonal matrix with the entries $g_{11}, \dots, g_{88}$. (Sections 0.16 and 4.19.)
- **Diagonal metric**: $g_{\mu\nu} = 0$ whenever $\mu \ne \nu$; then $ds^2 = \sum_\mu g_{\mu\mu} (dx^\mu)^2$. (Section 3.12.)
- **Diagonal vielbein**: The diagonal vielbein is $e^a{}_\mu = f_\mu\delta^a_\mu$, its inverse $e^\mu{}_a = \delta^\mu_a/f_a$, and the curved gammas are $\gamma^\mu = e^\mu{}_a\gamma^{(a)} = \gamma^{(\mu)}/f_\mu$ (no sum) and $\gamma_\mu = g_{\mu\mu}\gamma^\mu = \eta_{\mu\mu}f_\mu\gamma^{(\mu)}$. (Section 18.3.)
- **Dictionary**: The braces `{...}` make a dictionary: pairs of a key and a value, written `key: value`. (Sections 0.13, 0.20, 1.9, 2.11, 3.13, 3.22, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15, 22.12 and 22.23.)
- **Dictionary comprehension**: A dictionary comprehension: for every check of the report it stores the detail text under the name of the check, so that, for example, `details["representation_real"]` is the detail of the check `representation_real`. (Sections 0.21, 0.25, 1.9, 2.11, 3.22, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 12.25, 13.14, 14.18, 15.9, 16.12, 17.11, 18.9, 20.11, 21.15 and 22.12.)
- **Difference formula**: On the grid the second derivative is replaced by the difference formula $(\phi_{k+1} - 2\phi_k + \phi_{k-1})/h^2$, which follows from the Taylor expansions $\phi_{k\pm1} = \phi_k \pm h\,\phi'_k + \tfrac12 h^2\phi''_k \pm \tfrac16 h^3 \phi'''_k + O(h^4)$: adding them, the odd powers cancel, and the error is of order $h^2$. (Section 13.2.)
- **Difference quotient**: The heat capacity is also computed as $dE/dT$, a difference quotient: energies at the temperatures $T \pm dT$ (and $T \pm 2dT$) are subtracted and divided by multiples of $dT = 0.01\,T$. (Section 16.7.)
- **Dimension**: The span of a list of matrices is the set of all their combinations; a basis of a space is an independent list that spans it, and the number of its elements is the dimension of the space. (Sections 4.13, 4.15, 4.19, 5.11, 5.16, 7.10, 8.17 and 21.14.)
- **Dirac adjoint** $\bar\Psi = \Psi^\dagger C$: a row of 16 numbers. (Sections 5.4, 5.32, 7.19, 8.2, 9.2, 18.2, 21.2 and 21.14.)
- **Dirac conjugate**: It is not a new equation: it is the Dirac conjugate of the field equation. (Section 7.21.)
- **Dirac operator**: Dirac operator: $\gamma^\mu D_\mu = \sum_\mu \gamma^\mu D_\mu$. (Section 6.13.)
- **Dirac sea**: the picture in which every negative-energy level is filled in the vacuum. Its energy, $-E$ for each of the 8 negative levels, is $-8E$. (Sections 10.20 and 10.25.)
- **Dirac's exchange energy**: With $n_\sigma = n/2$ and $k_F = (3\pi^2 n)^{1/3}$ this is Dirac's exchange energy (1930). (Section 13.15.)
- **dirac16complex** has components that **anticommute**: for two of its components $\Psi_A\Psi_B = -\Psi_B\Psi_A$. (Sections 0.1 and 7.1.)
- **dirac16complex00**: the second field of the theory, with 16 COMMUTING complex components; it is a classical field (it is not quantised). (Sections 0.1, 7.1 and 10.25.)
- **Discrete symmetry**: a symmetry that is a single operation, such as a reflection, and not a continuous family of operations such as the multiplications of the U(1) symmetry (Chapter 21). (Section 0.2.)
- **Discretisation error**: The discretisation error: the program replaces the continuous interval $-L \le y \le 0$ by finitely many points, so it solves a nearby problem, not the exact one. (Section 16.2.)
- **Dispersion relation**: the dispersion relation: the wave oscillates in time for every $k$ (PROVED; Notebook 07d, In [14]). (Sections 7.5 and 7.8.)
- **Distributive**: The product is, however, associative, $(AB)C = A(BC)$, because both sides have the entries $\sum_j\sum_k A_{ij}B_{jk}C_{kl}$, and distributive, $A(B + C) = AB + AC$ (multiply out inside the sum). (Section 1.18.)
- **Divergence** $\nabla_h P^h{}_j$: the curved-space form of "change plus outflow"; zero divergence means conservation. (Sections 3.25, 11.1, 11.2, 12.2 and 21.22.)
- **Divergence form**: the theory record writes the term $\gamma^\mu\Omega_\mu$ as a sum of derivatives: it equals $1/(2\sqrt{|g|})$ times the sum over $\mu$ of $\partial_\mu(\sqrt{|g|}\,\gamma^{(\mu)}/f_\mu)$, computed on both patches; the coefficient of $\gamma^{(\mu)}$ is $\partial_\mu(\sqrt{|g|}/f_\mu)/(2\sqrt{|g|})$. (Section 18.27.)
- **Docstring**: Two kinds of lines are text for the reader and are not executed: a comment is everything after a `#` sign on a line, and a docstring is a text in triple quotes `"""..."""` directly below a `def` line, which says in words what the function does (Python stores it with the function and skips it when the function runs). (Sections 0.13, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15 and 22.12.)
- **Domain**: A `DomainMatrix` is sympy's fast matrix of exact numbers from a chosen domain: the rational numbers `QQ` (fractions) or the integers `ZZ`. (Section 21.15.)
- **Dot product**: The dot product of two vectors with $n$ components is the number. (Sections 1.18, 2.18 and 20.17.)
- **Double**: the ordinary number of a computer, with 53 binary digits (about 16 decimal digits). (Sections 16.20 and 16.23.)
- **Double cover**: two spinor matrices, $R$ and $-R$, move the vectors in the same way. (Sections 5.12, 5.18 and 5.21.)
- **Double occupancy**: the probability that both electrons sit on the same site. (Sections 13.7 and 13.13.)
- **Double precision**: the computer's usual numbers, with about 16 significant digits; 40 digits: mpmath's numbers with as many digits as asked for. (Section 15.29.)
- **Double-counting formula**: This double-counting formula gives the same energy as the direct sum of the four parts, which the notebook checks. (Section 13.32.)
- **Doubled system**: The weight $w = \tfrac12$ belongs to the doubled system: the Z2 mirror makes a copy of the patch, every orbital is normalised on the patch, $\int_{-L}^{0}(a^2 + b^2)\,dy = 1$, and the particle number $N = \sum g f$ counts the quanta of the patch and of its mirror copy together; one patch holds $N/2$. (Section 15.2.)
- **Dressing**: the small admixture of other levels that a particle carries while the background keeps moving. (Sections 22.2 and 22.11.)
- **Drift**: The drift is the largest change of the Krein form, divided by $\max(u^\dagger u, 1)$: rounding errors grow with the size of the numbers, so the change is measured relative to it. (Section 8.23.)
- **Dual**: The dual of an antisymmetric $4 \times 4$ matrix $M$ is $(\star M)_{pq} = \tfrac12\sum_{r,s}\epsilon_{pqrs} M_{rs}$, where the Levi-Civita symbol $\epsilon_{pqrs}$ is the permutation sign of $(p, q, r, s)$. (Section 4.5.)
- **Dummy**: A summed index is called a dummy index (its name does not matter: $A_{ij}B_{jk} = A_{il}B_{lk}$), an index that is not summed a free index (the formula holds for each of its values). numpy's function `einsum` reads this convention literally: `np.einsum("ij,jk->ik", A, B)` says "the first factor has the indices $i, j$, the second $j, k$; $j$ appears twice and is summed; the result has the indices $i, k$". (Sections 1.18, 1.24 and 1.26.)
- **Dummy index**: an index that appears twice in one term, once up and once down; it is summed over all its values. Its name does not matter. (Section 1.32.)
- **Duration**: A step $dt$ alone has $ds^2 = -dt^2 < 0$: it is not a length but a duration, and the time that a clock carried along the step shows, its proper time, is $d\tau = \sqrt{-ds^2} = dt$. (Section 3.4.)
- **Dust-like**: Radiation-like: $w_{\rm eff} = 1/3$; dust-like (dark-matter-like): $w_{\rm eff} = 0$; cosmological-constant-like: $w = -1$; phantom: $w < -1$. (Section 22.22.)

**E**

- **E-fold**: a growth by the factor $e$; a growth of $a_4$ by $\ln 2 \approx 0.693$ doubles $e^{a_4}$ and halves $e^{-a_4}$. (Sections 1.5, 1.8, 22.2 and 22.11.)
- **Effective mass** $V = m + U'(S) = m + \lambda S$: the number that multiplies $\Phi$ on the right side of the field equation. (Sections 7.19, 9.2, 9.24, 12.26, 12.29, 14.3, 15.2, 19.20, 20.12 and 20.15.)
- **Effective potential**: Kohn-Sham state: an approximate state of $N$ identical fermions built from one-particle wave functions (orbitals) that each solve a one-particle equation in a common effective potential; the potential depends on the densities of the occupied orbitals, so the equations are solved self-consistently (repeat until nothing changes). (Section 19.20.)
- **Efficiency**: The final asymmetry is $a(\infty) = \epsilon\,\eta(K)$ with the efficiency. (Section 21.6.)
- **Eigen-orbital**: Words of the Kohn-Sham method used again here (Chapters 13 to 15 define them in full): an orbital is the wave of one quantum, and an eigen-orbital one that solves the Kohn-Sham equation with a definite energy; the Fermi level is the energy that separates the occupied orbitals from the empty ones; a state is self-consistent when the potentials computed from its own density are the potentials its orbitals were computed with; the good sector is the set of orbitals that do not depend on the extra times $x_5, x_6, x_7$; the Z2 mirror is the ASSUMED rule that the hidden direction continues beyond the brane as a mirror image of the computed patch, with the field there fixed by the field on the computed side (Chapter 14 states the rule; record `Revision/kohn_sham/ks-theory.json`, key `boundaryConditions.brane`). (Section 17.2.)
- **Eigenfunctions**: Often it contains a number that is not known in advance, and it has a solution that is not zero everywhere only for special values of that number: these values are the eigenvalues and the solutions the eigenfunctions. (Section 2.12.)
- **Eigenspace**: The set of all eigenvectors of one eigenvalue (with the zero column) is its eigenspace, and the number of independent ones is its dimension. (Sections 8.17, 10.5 and 10.9.)
- **Eigenstate**: A state with $h\phi = \epsilon\,\phi$ is an eigenstate (a stationary state) with the energy $\epsilon$, an eigenvalue of $h$. (Section 13.2.)
- **Eigenvalue and eigenvector**: a number $\lambda$ and a nonzero column $u$ with $M u = \lambda u$. (Section 4.11.)
- **Eigenvalue** and **eigenvector**: a number $\varepsilon$ and a column $z \ne 0$ with $T z = \varepsilon z$. A symmetric matrix of size $n$ has $n$ real eigenvalues. (Sections 1.34, 1.40, 2.12, 4.9, 4.19, 5.3, 5.9, 8.17, 8.22, 9.25, 10.9, 13.2, 13.35, 16.18 and 18.26.)
- **Eigenvalue, eigenfunction**: a value of the number $\lambda$ (or the energy $E$) for which the boundary-value problem has a solution that is not zero everywhere; that solution is an eigenfunction. (Section 2.16.)
- **Eigenvector, joint eigenvector**: a column $v$ with $Mv = \mu v$ for a number $\mu$ (the eigenvalue); a joint eigenvector of several matrices is an eigenvector of each of them. (Section 9.29.)
- **Eigenvectors**: So the energies of the fields of one momentum $k$ are the eigenvalues of the $16 \times 16$ matrix $h$, and the columns $u$ are its eigenvectors (the columns $v \neq 0$ with $hv = Ev$, Rule 6 of Section 5.3). (Sections 1.34, 1.40, 4.9, 4.19, 5.9, 5.34, 8.17, 8.22, 9.25, 10.9, 13.35, 16.18 and 18.26.)
- **Einstein equations** with cosmological constant $\Lambda$ and coupling $\kappa$: $G^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$. (Sections 12.29 and 20.15.)
- **Einstein gravity**: Einstein gravity: $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$. (Sections 12.2, 12.15, 12.19, 17.2 and 20.2.)
- **Einstein tensor**: Ricci tensor $R^a{}_b = \sum_c R^{ac}{}_{bc}$, Ricci scalar $R = \sum_a R^a{}_a$, Einstein tensor $G^a{}_b = R^a{}_b - \tfrac12 \delta^a{}_b R$: the averages of the curvature that enter Einstein's field equations. (Sections 3.17, 3.29, 11.2, 11.18, 12.2, 12.15 and 20.10.)
- **Einstein's equations**: the field equations of gravity, which say how the source shapes the metric (Chapter 12). (Section 0.2.)
- **Einstein's field equations** $G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\, T^\mu{}_\nu$: the Einstein tensor plus a constant $\Lambda$ (the cosmological constant) times $\delta^\mu{}_\nu$ equals a positive constant $\kappa$ times the energy-momentum tensor $T^\mu{}_\nu$ of the matter. (Section 3.29.)
- **Einstein-Gauss-Bonnet gravity**: Einstein-Gauss-Bonnet gravity: $\alpha_1 = 1$, $\alpha_3 = 0$. (Sections 12.2 and 20.2.)
- **Einstein-Hilbert Lagrangian**: the Lagrangian density $\sqrt{|g|}R$ of the geometry, with $R$ the Ricci scalar; varying its action with respect to the metric gives Einstein's equations without a source. (Sections 22.2 and 22.4.)
- **Einstein-Lovelock equations**: $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$, with the three Lovelock tensors $E_{(k)}$ (Chapter 12), couplings $\alpha_k$, the cosmological constant $\Lambda$ and the gravitational coupling $\kappa$. (Section 20.2.)
- **Einstein-Lovelock gravity**: We use the most general gravity theory that keeps the field equations of second order in eight dimensions, Einstein-Lovelock gravity, and its special case, Einstein gravity. (Section 12.1.)
- **einsum**: numpy's function that evaluates a product written with the summation convention, for example `np.einsum("ij,jk->ik", A, B)`. (Sections 1.24 and 1.32.)
- **Electric charge**: Electric charge $Q_{\mathrm{el}}$, in units of the proton charge. (Section 21.2.)
- **Electron, positron**: two particles of the same mass $m$ and opposite electric charge $-1$ and $+1$. (Section 20.20.)
- **Elimination**: Computers therefore use elimination: by rule 6 one may subtract multiples of rows from other rows without changing the determinant, and doing so step by step makes every entry below the diagonal zero, which needs about $n^3/3$ multiplications. (Section 1.21.)
- **Ellipse**: So the unit circle becomes an ellipse whose longest and shortest half-axes have the lengths $\sqrt 9 = 3$ and $\sqrt 1 = 1$, the two eigenvalues, and lie along the two eigenvectors (Figure 01g.1). (Section 1.34.)
- **Empty set**: A set is a collection of different objects, written in braces, for example $A = \{x_2, x_5\}$; the empty set $\{\}$ has no element. (Section 4.13.)
- **Empty state**: A system may have several conserved quantities, and each forbids on its own: the conservation laws allow a transition only when EVERY conserved quantity has the same value in A and in B. The empty state of the classical theory is the configuration in which every field is zero everywhere; all its bilinears, and hence all its conserved quantities, are zero. (Section 20.22.)
- **End angle** $\Phi(\varepsilon) = \theta(0)$: the angle reached at the brane when we shoot with the energy $\varepsilon$. (Section 2.27.)
- **Energy**: a column that depends on the time as $e^{-iE\,x4}$ ($E$ real) has the energy $E$. (Sections 2.2, 4.9, 5.34, 5.37, 7.4, 7.8 and 20.20.)
- **Energy density** $\rho = -T^{x_4}{}_{x_4}$: energy per unit (proper) volume. (Sections 3.26, 3.29, 5.34, 5.37, 9.1, 9.16, 9.24, 10.25, 12.2, 15.16, 15.19, 17.2, 17.10, 20.2 and 20.10.)
- **Energy exchange**: the change of the energy density in time caused by work done by the inflating 3-space and the deflating extra times. (Section 9.24.)
- **Energy kernel**: at the one-particle level the energy of a plane wave is $\Psi^\dagger\mathcal{E}_m(k)\Psi$ with the energy kernel $\mathcal{E}_m(k) = Bh_m(k)$; the evolution is $i\partial_4\Psi$ = (anticommutator matrix) times (energy kernel) times $\Psi$, that is $i\partial_4\Psi = B\mathcal{E}_m\Psi = h_m\Psi$. (Section 18.23.)
- **Energy level** $\varepsilon$: a value of the energy for which the equations have a solution with all boundary conditions; an eigenvalue. Unit: the mass $m$ (in units with $m = H = 1$). (Sections 2.1 and 2.27.)
- **Energy-change law**: This is the energy-change law (ks-theory.json, emt.energyChange; PROVED, check emt_x4_component; COMPUTED for all 75 states against differences of the self-consistent energies at neighbouring slices with fixed occupations, check emt_energy_change_dE_da4, worst $1.5 \times 10^{-10}$). (Section 15.16.)
- **Energy-momentum profiles**: the energy density $\rho(y)$ and the pressures $p_3(y)$ (3-space), $p_t(y)$ (extra times), $p_8(y)$ (hidden direction). (Section 19.20.)
- **Energy-momentum tensor** $T$: the table of the energy and the momentum that a field carries and of the pressures it exerts (Chapter 9). (Sections 0.2, 3.26, 3.29, 9.16, 12.2, 12.15, 12.29, 15.16, 15.19, 17.2, 17.10, 17.20, 18.26, 20.2, 20.10 and 20.15.)
- **Engine**: the program that did the computation: Wolfram Language (the language of Mathematica, run with wolframscript), Python (with the packages sympy, numpy and mpmath), or Rust (a fast compiled language). The *lead's independent checks* are short Python programs that share no code with the other verifiers. (Sections 0.20 and 0.21.)
- **Ensemble**: The Revision solver uses an ensemble form: one particle is moved from the highest occupied group of equal levels to the lowest empty group, spread evenly over each group, which keeps the symmetries of its reduction (`Revision/kohn_sham/results/parameters.json`, conventions deltaScf). (Sections 13.27 and 15.5.)
- **Entropy** $S = -\sum g[f\ln f + (1 - f)\ln(1 - f)]$: a measure of how many microscopic arrangements the gas can take. (Sections 13.26, 13.30, 15.26 and 15.29.)
- **Entry**: $A_{ij}$ is the entry in row $i$ and column $j$. (Sections 1.24, 4.2, 10.9 and 18.8.)
- **Envelope theorem**: (i) $dF/dT = -S_s$ (the envelope theorem). (Section 13.26.)
- **Environment variable**: a named setting that a program receives from the computer when it starts. (Sections 0.13, 0.22, 0.24, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15, 22.12, 23.2 and 23.11.)
- **Equation of state** $w = p/\rho$: pressure divided by energy density. With different pressures along different directions there is one such ratio for each: $w_3 = p_3/\rho$ (3-space), $w_t = p_t/\rho$ (the extra times) and $w_8 = p_8/\rho$ (the hidden direction); these are the equations of state of Section 9.4. (Sections 9.1, 9.4, 9.16, 9.24, 12.2, 12.19, 22.2 and 22.22.)
- **Equator**: The equator $\theta = \pi/2$, $\varphi = s/a$ is a geodesic: $d^2\theta/ds^2 = 0$ and $\sin(\pi/2)\cos(\pi/2) = 0$, and $d^2\varphi/ds^2 = 0$ with $d\theta/ds = 0$. (Section 3.16.)
- **Equilibrium density**: For an external potential $v$ write $\hat H_v = \hat T + \hat W + \hat V$, its grand potential $\Omega_v[\hat\rho] = \mathrm{Tr}[\hat\rho\,(\hat H_v - \mu\hat N)] - T\,S[\hat\rho]$, its Gibbs state $\hat\rho_v$, and $n_v$ for the density of $\hat\rho_v$, the equilibrium density. (Section 13.26.)
- **Error**: the computed value minus the exact value (we print its size, the *absolute value*). (Sections 2.6, 2.10, 13.24 and 16.2.)
- **Error function**: (the error function $\operatorname{erf}(u) = \tfrac{2}{\sqrt\pi}\int_0^u e^{-t^2}dt$ gives $\int_{u_0}^{u_1}e^{-t^2}dt = \tfrac{\sqrt\pi}{2}(\operatorname{erf}u_1 - \operatorname{erf}u_0)$, and erf is odd, $\operatorname{erf}(-u) = -\operatorname{erf}u$). (Section 12.21.)
- **Euler characteristic**: The name comes from a classical theorem that this book quotes and does not prove (ASSUMED): in a space of even dimension $n = 2m$ the Lovelock scalar of order $m$ is called the Euler density, because for a closed space (finite and without an edge, like the surface of a ball) with a positive-definite metric (every squared length positive, unlike the author's metric) its integral over the whole space, with the volume factor $\sqrt{|\det g|}$, is a constant times the Euler characteristic: a whole number that depends only on the shape of the space (2 for the surface of a ball, 0 for the surface of a ring) and does not change when the metric is deformed (the Chern-Gauss-Bonnet theorem). (Sections 11.2 and 11.11.)
- **Euler density**: in a space of even dimension $n = 2m$, the Lovelock scalar of order $m$ (in eight dimensions $L_{(4)}$). (Sections 11.2 and 11.11.)
- **Euler's formula**: $e^{i\theta} = \cos\theta + i \sin\theta$ for real $\theta$. (Sections 1.11 and 1.16.)
- **Euler, midpoint, RK4**: three rules that compute the value after one step from the value before it (the formulas are in section 4 of Notebook 02a). (Section 2.10.)
- **Euler-Lagrange equation**: the field equation obtained from a Lagrangian $L$ by requiring that the action does not change, to first order, when the field is changed a little. (Sections 7.8, 7.16 and 7.26; the opening of Chapter 7.)
- **Euler-Lagrange expression**: $\partial\mathcal{L}/\partial\Psi^*_A - \sum_\mu\partial_\mu\big(\partial\mathcal{L}/\partial(\partial_\mu\Psi^*_A)\big)$; the field equations say it is zero. (Sections 7.3, 7.8 and 18.19.)
- **Even**: So $u(-x) = c\, u(x)$, and applying this twice gives $c^2 = 1$: every bound state is even, $u(-x) = u(x)$, or odd, $u(-x) = -u(x)$. (Sections 1.19, 1.24, 2.13, 2.16, 3.30, 4.13, 4.15, 5.5, 5.12, 5.16, 7.11, 7.16, 11.2, 11.8 and 16.18.)
- **Even function**: $f(-u) = f(u)$. (Section 11.26.)
- **Evolution equation**: This difference is the only combination in which $a_4''$ survives; in the field equations it is the evolution equation, which decides how $a_4$ changes (Chapter 12). (Sections 3.26, 11.21, 12.2, 12.9, 12.15, 17.2, 17.3 and 17.20.)
- **Evolution form**: and because $(\gamma^{(4)})^2 = -1$ and $f_4 = 1$ it can be solved for the time derivative (the evolution form; multiply by $-\gamma^{(4)}$): $\partial_4\Phi = -\gamma^{(4)}\Big[V\Phi - \sum_{a \neq 4}\frac{1}{f_a}\,\gamma^{(a)}\partial_a\Phi - 3H\gamma^{(8)}\Phi\Big]$. (Section 9.2.)
- **Exact arithmetic**: computing with fractions, never rounding. The package sympy does this (`DomainMatrix` over `QQ`, the rational numbers). (Section 5.16.)
- **Exact** computation: with symbols and fractions (sympy), not with rounded decimal numbers; an exact check that an expression is zero proves it for ALL values of the symbols. (Sections 1.24, 6.13, 6.21, 6.27, 11.2, 11.18, 16.18 and 18.8.)
- **Exact local conservation law**: It obeys an exact local conservation law: in the author's metric, for every history $a_4(x_4)$, in particular the one in which ordinary space inflates and the three extra times $x_5, x_6, x_7$ deflate exponentially, the charge of a region changes only by what flows through its boundary (PROVED, Sections 21.16 and 21.17). (Section 21.1; the opening of Chapter 21.)
- **Exactly rounded**: The module `math` of Python provides `math.fsum`, which adds stored numbers exactly and rounds only once, at the end (the exactly rounded sum), and $\pi$. (Section 0.25.)
- **Exchange**: (The index $C'$ carries a prime so that it is not confused with the matrix $C$.) The first product is the direct (Hartree) term, the second the exchange (Fock) term. (Sections 13.4 and 14.26.)
- **Exchange energy**: $E_x$ is the exchange energy (the Fock term); it has no classical analogue, it comes from the antisymmetry of $\Phi$, and for a repulsive $w$ it lowers the energy. (Sections 13.5 and 13.19.)
- **Exchange hole**: the dip in the probability of finding a second fermion near a first one, caused by the Pauli principle. (Sections 13.15 and 13.19.)
- **Exchange potential**: Hartree potential: the potential that one particle feels from the average density of all particles; exchange potential: the correction that comes from the Pauli principle (equal-label particles avoid each other). (Section 13.35.)
- **Exchange-correlation energy**: The price is one quantity, the exchange-correlation energy, that is not known exactly and must be approximated. (Sections 13.1 and 13.10.)
- **Exchange-only**: So this is an exchange-only Kohn-Sham scheme, which for a contact interaction is the same as the Hartree-Fock approximation: an approximation to the true ground state, whose error is the correlation energy (Section 13.7 showed how large it can be on two sites). (Section 13.32.)
- **Exclusive or** (XOR, `x ^ y`): the two numbers are compared bit by bit, and a result bit is 1 when exactly one of the two bits is 1. Applying the same exclusive or twice gives back the number: for single bits, $(a \oplus b) \oplus b = a$ in all four cases ($b = 0$ changes nothing twice; $b = 1$ flips the bit twice), so it holds bit by bit. That is why an XOR step loses nothing. (Sections 1.49 and 1.53.)
- **Exhaustive check**: a check of *every* possible case, not of examples. (Section 1.47.)
- **Exhaustive test**: a test of every possible case. (Section 11.8.)
- **Expansion rate** (Hubble rate) of a direction: $\partial_{x_4} \ln h_\mu$, the fraction by which its lengths grow per unit of time $x_4$. (Section 3.12.)
- **Expectation value**: $\langle\phi|X|\phi\rangle$ in a normalised state $\phi$. (Sections 5.37, 9.13, 10.25, 13.2 and 19.11.)
- **Expectation-value rule**: for one quantum in the mode $u$, $\langle\Psi^\dagger X\Psi\rangle = u^\dagger BXu$; for many, $\langle\Psi^\dagger X\Psi\rangle = \mathrm{Tr}(X\rho)$ with the one-body matrix $\rho = \sum_{\rm occupied} f\,uu^\dagger B$ ($f$ the occupation). (Sections 10.21 and 14.30.)
- **Expected number**: The expected number of events in a list is the average number of them that happen, taken over very many repetitions; it equals the sum of the probabilities of the single events, whether or not they are independent (a rule of the theory of chance that we use without proof). (Section 0.18.)
- **Expected value**: For $N$ tries that each succeed with probability $q$, the number of successes is about $Nq$, its expected value, typically within one standard deviation $\sqrt{Nq(1 - q)}$ of it (ASSUMED from probability theory). (Sections 1.50 and 1.53.)
- **Exponent**: The caption quotes the count for $n = 16$ as computed, not typed: `f"{x:.1e}"` writes $16!$ as the text 2.1e+13, and `.split("e")` cuts it at the letter e into the mantissa 2.1 and the exponent +13 (both are still texts). (Section 1.25.)
- **Exponential**: the function $e^{t}$; $e^{-t} = 1 / e^{t}$. (Sections 0.16, 5.18 and 5.26.)
- **Exponential function** $e^x$ and **natural logarithm** $\ln x$, which undoes it: $\ln(e^x) = x$. The number $e = 2.71828\dots$. (Sections 1.5 and 1.8.)
- **Exponential of a matrix**: $\exp(M) = 1 + M + \tfrac12 M^2 + \tfrac16 M^3 + \dots = \sum_{k \ge 0} M^k/k!$, the same power series as for $e^x$. (Sections 5.21 and 10.31.)
- **Exponential wall**: This growth is called the exponential wall of the many-body problem. (Section 13.1.)
- **Exponentially**: A quantity whose rate of change is a fixed negative multiple of itself decreases exponentially: in every interval of time of length $1/(AH)$ it is multiplied by the same factor $e^{-1} = 0.3679$. (Section 0.14.)
- **Exporter**: the small Rust program, held as text inside the Wolfram check Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls, that wrote the GKD values into a file for the Wolfram check. (Sections 1.49 and 1.53.)
- **Extra times** $x_5$, $x_6$, $x_7$: the three time-like directions of the author's space-time besides the time $x_4$. They are time-like like $x_4$, and they deflate exponentially: lengths along them carry the scale factor $e^{-a_4}\sin^{1/6}z$, which shrinks while $a_4$ grows, whereas ordinary space, with the scale factor $e^{a_4}\sin^{1/6}z$, inflates. (Sections 0.1, 1.1, 2.1, 3.1, 3.12, 3.34, 4.1, 6.8, 6.13, 6.27, 7.1, 7.26, 8.2, 9.2, 11.2, 12.1, 12.15, 17.2, 17.10, 17.20, 19.15, 19.20 and 21.2.)
- **The extra-time component**: The extra-time component is found in the same way (three 3-space pairs, one extra-time pair, six mixed pairs, three space-time pairs, two extra-time-time pairs, five with $x_8$): $\sum = 3(a_4')^2 - 15H^2 + a_4''$ and $G^{x_5}{}_{x_5} = -a_4'' - 3(a_4')^2 + 15H^2$. (Section 12.6.)
- **Extra-time momentum** $k_5, k_6, k_7$: the momentum along the extra times; the good sector has $k_5 = k_6 = k_7 = 0$. (Section 21.29.)

**F**

- **F-string**: A string that starts with `f` is an f-string: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/00a.captions.json"`. (Sections 0.13, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15, 22.12, 22.23 and 23.12.)
- **Factorial**: Here $n! = 1 \cdot 2 \cdot 3 \cdots n$ (with $0! = 1$) is the factorial. (Sections 1.16, 2.3, 4.13 and 7.10.)
- **Falling factorial** $n!/(n-p)! = n (n-1) \cdots (n-p+1)$: the number of ways to choose $p$ different labels from $n$ in order (`math.perm(n, p)`). (Sections 1.43 and 1.47.)
- **False vacuum**: a state that has the lowest energy only among its neighbouring states; vacuum decay is its quantum transition into a state of still lower energy. (Section 20.2.)
- **Fermi level**: Words of the Kohn-Sham method used again here (Chapters 13 to 15 define them in full): an orbital is the wave of one quantum, and an eigen-orbital one that solves the Kohn-Sham equation with a definite energy; the Fermi level is the energy that separates the occupied orbitals from the empty ones; a state is self-consistent when the potentials computed from its own density are the potentials its orbitals were computed with; the good sector is the set of orbitals that do not depend on the extra times $x_5, x_6, x_7$; the Z2 mirror is the ASSUMED rule that the hidden direction continues beyond the brane as a mirror image of the computed patch, with the field there fixed by the field on the computed side (Chapter 14 states the rule; record `Revision/kohn_sham/ks-theory.json`, key `boundaryConditions.brane`). (Section 17.2.)
- **Fermi shell**: Fermi shell: the highest occupied shell of a state. (Sections 22.2 and 22.11.)
- **Fermi sphere, Fermi wave number** $k_F$: the ground state of the free gas fills every plane wave with $|\mathbf k| < k_F$, once per label. (Section 13.19.)
- **Fermi wave number**: The non-interacting ground state fills all $\mathbf k$ with $|\mathbf k| < k_F$ (the Fermi wave number), once for each of the $g$ labels. (Section 13.15.)
- **Fermi-Dirac**: each orbital is an independent two-state system, occupied with the Fermi-Dirac probability $f_a$ (the second step multiplies numerator and denominator by $e^{(\epsilon_a - \mu)/T}$). (Sections 13.26, 15.26 and 21.5.)
- **Fermi-Dirac occupation** $f(\epsilon) = 1/(e^{(\epsilon - \mu)/T} + 1)$: the probability that an orbital of energy $\epsilon$ is occupied. (Sections 13.30, 15.29, 16.23, 21.2 and 21.35.)
- **Fermi-level crossing**: Fermi-level crossing: an empty level comes down below an occupied one along the history, so the aufbau filling changes. (Sections 15.21 and 15.24.)
- **Fermion**: a particle of a kind that obeys the Pauli principle: two identical fermions with the same label never occupy the same one-particle state. (Sections 7.10, 13.3 and 13.35.)
- **Fermion mode**: A fermion mode is a place that holds zero or one particle. (Sections 5.34, 10.18 and 21.26.)
- **Fermion modes, occupation**: a fermion mode is either empty (0) or occupied (1); 16 modes have $2^{16} = 65536$ states, each a list of 16 zeros and ones. (Section 21.29.)
- **Field**: a function of several coordinates, here $\phi(x_1, x_4)$ or $\phi(x_5, x_4)$, with the author's names: $x_1$ a direction of 3-space, $x_4$ the time, $x_5$ one of the three extra times. (Sections 0.1, 7.5 and 7.8.)
- **Field equation** (the Euler-Lagrange equation of the Revision record): $(\gamma^\mu D_\mu - V)\Psi = 0$ with $V = m + U'(S)$ a real function, $m$ the mass, $D_\mu = \partial_\mu + \Omega_\mu$ the covariant derivative with the spin connection $\Omega_\mu$. (Sections 5.32, 7.21, 9.2, 12.2, 21.7 and 21.14.)
- **The field equations of Einstein-Lovelock gravity**: The field equations of Einstein-Lovelock gravity are $\sum_{k=1}^{3}\alpha_k\,E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu$. (Section 12.8.)
- **Field equations of gravity**: $\sum_{k=1}^{3}\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu = \kappa\,T^\mu{}_\nu$. (Sections 12.1 and 17.2.)
- **Field operators**: $\Psi_A = \sum_s \big((u_s)_A b_s + (v_s)_A d_s^*\big)$ for $A = 1, \dots, 16$, with $\chi_A$ its Hilbert adjoint and the canonical conjugate $\Psi^\dagger_A = \sum_C \chi_C B_{CA}$. (Section 5.37.)
- **Field-equation expression**: Define the field-equation expression $E = \gamma^\mu D_\mu\Phi - V\Phi$ and its adjoint $\bar E = (D_\mu\bar\Phi)\gamma^\mu + V\bar\Phi$ (sums over $\mu$); a configuration is on shell exactly when $E = 0$, and then $\bar E = 0$ too. (Section 9.8.)
- **Figure, plot, axis**: a figure is a picture; a plot draws numbers as points or lines; the horizontal axis and the vertical axis are the two number lines of the plot. (Section 0.12.)
- **Fine grid**: One RK4 step needs the coefficients $M$, $v$ and $\kappa$ at the start, the middle and the end of the step, so the potentials are stored on the fine grid of the $2G + 1 = 1801$ step ends and midpoints, $y_i = -L + i\,h/2$. (Sections 15.3 and 22.12.)
- **Fingerprint**: To tie the two together, a report writes down a fingerprint of each file it read. (Sections 0.18, 0.20 and 0.24.)
- **Finite difference**: an approximation of a derivative from values of the function at nearby points, with a small spacing $h$. (Sections 2.22, 3.29, 9.17, 9.29, 11.26, 15.19, 17.2 and 17.20.)
- **First Bianchi identity**: (S2) The first Bianchi identity $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$. (Section 3.17.)
- **First integral**: an equation with only first derivatives that every solution of a second-order equation obeys; here $a_4'^2$ as a function of $a_4$. (Sections 17.2 and 17.20.)
- **First jet**: At one point $x$, every quantity of the theory (the Lagrangian, the 16 components of the field operator, the 36 components of $T_{\mu\nu}$, the 8 of $J^\mu$) is a polynomial in the 288 numbers of the first jet: the 16 values $\Psi_A$, the 16 values $\Psi_A^*$ and the $2 \times 8 \times 16 = 256$ first derivatives $\partial_\mu\Psi_A$, $\partial_\mu\Psi_A^*$. (Section 18.20.)
- **First order**: an approximation that keeps only terms linear in the small amplitudes. (Section 22.11.)
- **First variation**: The first variation is its slope at $\epsilon = 0$: $S_1 = \frac{d}{d\epsilon}S[q + \epsilon\xi]\Big|_{\epsilon = 0}$. (Sections 7.2 and 7.8.)
- **First-order Lagrangian**: a Lagrangian that contains the velocities only to the first power, like the Lagrangians of the fields of this book. (Section 7.8.)
- **First-order mean-field potential**: More words of the Kohn-Sham computations: a shell is a group of orbitals with the same energy, and a closed shell is a particle number $N$ that fills every orbital up to some energy completely and none above it (so the ground state is unique); the first-order mean-field potential is the potential that one quantum feels from the others when the interaction is counted once, to first order in the coupling $\lambda$, with the density of the free gas; fixed occupations means that the same orbitals stay filled when $a_4$ is changed a little, even if their energies move. (Section 17.2.)
- **First-order system**: the second-order equation written as two first-order ones, $\frac{d}{dx_4}a_4 = v$ and $\frac{d}{dx_4}v = \kappa(p_3 - p_t)/F(v)$, with $v = a_4'$. (Section 12.24.)
- **Fisher-Yates shuffle**: a way to put a list into a random order by swapping entries one after the other. (Sections 1.49 and 1.53.)
- **Fit**: Fit: the least-squares straight line in $1 - a$ over a range of $a$. (Section 22.22.)
- **The five labels**: PROVED (exact; the book gives the complete proof and, where the Revision record contains an exact computer check of the statement, names the report file and the check), COMPUTED (a number from a numerical computation, with its measured uncertainty and the file that holds it), ASSUMED (a starting point that the book does not derive: a convention, a physical input or an approximation), HYPOTHESIS (an idea that is stated and examined but not established), OPEN (a question that neither the Revision record nor the book answers). (Section 0.20.)
- **Fixed occupations**: More words of the Kohn-Sham computations: a shell is a group of orbitals with the same energy, and a closed shell is a particle number $N$ that fills every orbital up to some energy completely and none above it (so the ground state is unique); the first-order mean-field potential is the potential that one quantum feels from the others when the interaction is counted once, to first order in the coupling $\lambda$, with the density of the free gas; fixed occupations means that the same orbitals stay filled when $a_4$ is changed a little, even if their energies move. (Section 17.2.)
- **Fixed point** of a map $G$: a number $x^*$ with $G(x^*) = x^*$. (Sections 13.21, 13.24 and 19.4.)
- **Flat**: A space whose Riemann tensor is zero everywhere is flat; conversely, near each point of a space with zero Riemann tensor there are coordinates in which the metric is constant (a standard theorem, quoted, ASSUMED). (Section 3.17.)
- **Flat 4+4 space**: space-time with the constant metric $\eta$, whose diagonal entries are $+1$, $+1$, $+1$, $-1$, $-1$, $-1$, $-1$, $+1$ in the order $x_1, \dots, x_8$: no gravity, no inflation, no deflation. (Sections 4.9 and 4.11.)
- **Floating-point number**: the way the computer stores a number with a fraction part: a whole number of at most 53 binary digits times a power of 2. Python's `float` and numpy's `float64` are such numbers. They have about 16 significant decimal digits. (Sections 0.22, 0.24, 1.4, 1.8, 1.24, 4.11, 14.11 and 18.27.)
- **Floor**: The second term, $2\cdot10^{-12}$ times the size of $R$ (at least 1), is a floor for the rounding errors of the computer, which do not shrink with $h$. (Section 16.5.)
- **Flux**: the value of the bracket at an end; a nonzero flux at $z = \pi/2$ means that something flows through the patch end (in or out). (Sections 5.6, 8.32, 10.2, 10.27, 10.31, 21.17 and 21.22.)
- **Fock operator**: $\hat F$ is the Fock operator. (Section 13.6.)
- **Fock space**: all combinations of the 65536 basis states. (Sections 5.34, 5.37, 10.11, 10.18 and 10.25.)
- **Format string**: The three curves are $W$, $W^2$ and $W^6$ with $H = 1$; the third argument of `semilogy`, a short text called a format string, sets the line style: two hyphens draw a dashed line and a colon a dotted one (the plain `plot` lines of this book use the same format strings); `legend` shows the `label` texts in a box. (Section 14.11.)
- **Former measure**: `\w+` is one or more letters, digits or underscores (the name of a state, such as N8_lam0_a00_T10), `\S+` a number, and `\(` and `\)` are round brackets themselves; the four bracketed parts are the name of the state, the error of the old method, the former measure (the difference between the two runs when both used the old method) and the present measure (the difference seen by the present refined run). (Section 0.25.)
- **Forward difference**: The forward difference: $\frac{f(x + h) - f(x)}{h} = f'(x) + \frac{h}{2} f''(x) + \dots$. (Section 2.18.)
- **Fourth-order central difference**: `slope` estimates the derivative of a tabulated function with the fourth-order central difference of step $\delta = sh$: $f'(y) \approx \frac{-f(y + 2\delta) + 8f(y + \delta) - 8f(y - \delta) + f(y - 2\delta)}{12\,\delta}$. (Sections 17.21 and 22.23.)
- **Fraction** (rational number): $p/q$ with whole numbers $p$ and $q \neq 0$. (Sections 1.2 and 1.8.)
- **Frame**: Such a set is a frame, and the matrix $e^a{}_\mu$ that converts coordinate steps into frame components is the vielbein (German for "many legs"): the metric is $g_{\mu\nu} = \sum_{a,b} e^a{}_\mu\,\eta_{ab}\,e^b{}_\nu$. (Sections 3.7, 4.4, 4.9, 6.1, 8.2 and 8.14.)
- **Frame current** $q_8$: for a homogeneous field, the number $q_8 = -i\bar\Psi\gamma^{(x_8)}\Psi$, which depends on $x_4$ only; the hidden-direction charge current is $J^{x_8} = \tan z\,q_8$, so the flux through the brane is $\sqrt{|g|}J^{x_8} = \sin z\,q_8$. It is NOT the charge $Q$. (Section 18.21.)
- **Frame factors**: These factors are the frame factors: they carry the metric into every derivative term. (Sections 4.4, 7.18 and 8.2.)
- **Frame gamma matrices** $\gamma^{(a)}$: the author's eight real $16\times16$ matrices with $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} = 2\eta^{ab}$, $\eta = \mathrm{diag}(1,1,1,-1,-1,-1,-1,1)$. (Section 7.26.)
- **Frame index**: The upper index $a$ is a frame index: it numbers the eight frame directions. (Sections 6.2 and 6.13.)
- **Frame metric** $\eta_{ab}$: the diagonal table $\mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$; $\eta^{ab}$ (upper indices) is its inverse. (Sections 1.9, 1.13, 1.27, 1.32, 4.7, 6.13, 6.27 and 8.2.)
- **Frame momenta**: What carries over is the algebra of the frame: in a region so small that the metric functions change little across it, waves with frame momenta $k_a$ obey the same matrix algebra; the Revision record uses this local plane-wave reading with the coefficients of the equation held fixed. (Sections 4.9 and 8.17.)
- **Frame momentum**: Coordinate momentum $q_a$ and frame momentum $k_a$: a wave $e^{iq_ax_a}$ has the coordinate momentum $q_a$; measured with proper lengths its momentum is $k_a = q_a/f_a$, the frame momentum. (Sections 8.28, 10.3, 10.39 and 10.42.)
- **Frame rotation** (local Lorentz transformation): a new vielbein $e'^a{}_\mu = \sum_b \Lambda^a{}_b(x)\,e^b{}_\mu$ with a matrix $\Lambda(x)$ that keeps $\eta$: $\Lambda^T\eta\Lambda = \eta$. It describes the same metric. (Section 6.21.)
- **Frame velocity**: Scale factor $h_a = \sqrt{|g_{aa}|}$ and frame velocity $\hat u^a = h_a u^a$: the proper length (along an extra time: the proper duration) that the body covers along $x_a$ per unit of its own proper time, measured with the rulers and clocks of an observer at rest at its place; divided by $u^4$ it is the velocity that this observer measures. (Sections 3.31 and 3.34.)
- **Frame-dependent**: a quantity whose value changes when the vielbein is changed (such as $\gamma^\mu\Omega_\mu$). (Sections 6.15 and 6.21.)
- **Frame-independent**: Frame-independent: a statement that holds in every vielbein (such as "$F_{\mu\nu}$ is not zero"). (Section 6.21.)
- **Free**: A summed index is a dummy index (its name does not matter); an index that is not summed is a free index. (Sections 1.18, 1.24 and 1.26.)
- **Free energy**: Free energy $F = E - TS$; heat capacity $C_V = dE/dT$ at a fixed particle number. (Sections 13.30, 15.26 and 15.29.)
- **Free fall**: motion under no force other than the geometry. (Sections 3.16 and 3.34.)
- **Free index**: an index that appears once in every term of a formula; the formula holds for each of its values, so a formula with $k$ free indices over 8 coordinates stands for $8^k$ equations. (Section 1.32.)
- **Freezing**: The mixture is freezing: as the gas redshifts, $w$ moves toward the condensate's value (check `mixture_radiation_condensate_cpl`). (Sections 22.18 and 22.22.)
- **Frequency**: the number $\varepsilon$ in $e^{-i\varepsilon t}$; for real $\varepsilon$ the real and imaginary parts oscillate like $\cos$ and $\sin$. (Sections 1.13, 1.16, 8.17, 9.29, 10.3, 10.9, 12.29, 20.12, 20.15 and 21.29.)
- **Frozen coefficients**: in a curved space the factors in front of the derivatives change from point to point and in time; near one point and for a short time one replaces them by their values at that point. The momenta measured with these factors are the *frame momenta* $k_a$. This is a device of the analysis near one point (labelled MODEL); it does NOT say that the extra times stop deflating: in the author's metric they always deflate exponentially, and Notebook 08b follows a wave along the deflating history. (Sections 8.17 and 8.22.)
- **Frozen-coefficient model**: The end of this section defines the frozen-coefficient model of the author's universe, which has the same equation with the derivatives divided by scale factors; it is an ASSUMPTION, because it also leaves out two terms of the author's field equation. (Section 10.3.)
- **Function**: `def` defines a function: a named piece of code that runs when it is called. (Sections 0.13, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15 and 22.12.)
- **Function of a Hermitian matrix**: A function of a Hermitian matrix $A = \sum_i a_i\,u_iu_i^\dagger$ (eigenvalues $a_i$, orthonormal eigenvectors $u_i$) is defined through its eigenvalues, $f(A) = \sum_i f(a_i)\,u_iu_i^\dagger$; for $f = \exp$ this agrees with the power series, because $A^m = \sum_i a_i^m u_iu_i^\dagger$. (Section 13.26.)
- **Function of several variables**: a rule $f(x, y)$ that gives a number for every pair of numbers $(x, y)$ (or for every list $x_1, \dots, x_8$). (Section 2.22.)
- **Functional**: The square brackets in $S[q]$ say that $S$ depends on the whole function $q$, not on one number; a rule that takes a function and gives a number is called a functional. (Sections 7.2, 7.8 and 13.9.)
- **Functional derivative**: for every $\eta$, the function $\delta F/\delta n(x)$ is the functional derivative of $F$ at $n$. (Sections 13.6 and 13.9.)
- **Fundamental symmetry**: A Krein space is a space with a Hermitian form $[u, v]$ that is *nondegenerate* (no nonzero $u$ has $[u, v] = 0$ for all $v$) but *indefinite* (it takes both signs), together with a matrix $J$, the fundamental symmetry, with $J^\dagger = J = J^{-1}$, such that $[u, Jv]$ is a positive inner product. (Sections 10.13 and 10.18.)
- **Fundamental theorem of algebra**: The fundamental theorem of algebra (ASSUMED) says that a polynomial of degree $n$ has exactly $n$ roots $\lambda_1, \dots, \lambda_n$ when complex numbers are allowed and a repeated root is counted as often as it appears, its multiplicity. (Section 1.34.)

**G**

- **Gamma matrices**: eight fixed $16 \times 16$ matrices of the author, one for each direction, from which the equations of both fields are built (Chapter 4). (Sections 0.2, 1.1, 1.32, 6.13, 8.22, 12.29, 14.10, 17.20, 18.8, 19.15, 19.20, 20.10, 20.15, 21.2 and 21.14; the opening of Chapter 4.)
- **Gap**: an energy interval without levels. (Sections 14.20, 16.20 and 16.23.)
- **Gate**: the script `Revision/verify_revision.sh` (for bash) and its twin `Revision/verify_revision.ps1` (for PowerShell 7). (Sections 23.2 and 23.11.)
- **Gauss-Bonnet**: Lovelock tensors $E_{(1)}, E_{(2)}, E_{(3)}$: the three curvature tensors built with the GKD; $E_{(1)}$ is the Einstein tensor and $E_{(2)}$ the Gauss-Bonnet tensor. (Section 12.2.)
- **Gauss-Bonnet scalar**: $\mathrm{GB} = R^2 - 4R^a{}_bR^b{}_a + R^{ab}{}_{cd}R^{cd}{}_{ab}$ is the classical Gauss-Bonnet scalar. (Section 11.15.)
- **Gauss-Bonnet tensor**: Gauss-Bonnet tensor: the classical name of the order-2 Lovelock tensor. (Sections 11.2 and 11.18.)
- **Gaussian curvature**: A space of two dimensions has a single coordinate plane, and its curvature $\sigma(1, 2)$ is the Gaussian curvature. (Sections 3.17 and 3.21.)
- **Gaussian integers**: `random_matrix` is a $4\times4$ sympy matrix with random Gaussian integers (whole numbers $a + bi$ with $a, b$ from $-3$ to 3; the `lambda i, j: ...` is a small unnamed function that gives the entry in row `i` and column `j`). (Sections 4.16 and 7.17.)
- **Generalized Kronecker delta**: $\delta^{u_1\dots u_p}_{l_1\dots l_p} = \det[\delta(l_i, u_j)]$, the author's `kδ[lower, upper]`. (Sections 1.1, 1.42, 1.47, 11.1, 11.2, 11.8, 11.18, 11.28, 12.2 and 12.15; the opening of Chapter 11.)
- **Generator expression**: The generator expression counts 1 for every nonzero symbol with $\mu \le \nu$ (the symbols are symmetric in the two lower indices, so the pairs with $\nu < \mu$ are not new); the count is printed as a RESULT line: 25. (Sections 7.9, 8.15 and 18.9.)
- **Generator, Spin(4,4)**: the 28 matrices $S^{ab}$ ($a < b$) generate the spin transformations $R = \exp(\theta S^{ab})$, which turn the frame of the eight directions; their products form Spin(4,4). Spin(4,3) is the part generated by the 21 $S^{ab}$ with $a, b \neq x_4$ (the transformations that leave the time $x_4$ alone). (Section 10.37.)
- **Generators** $S^{ab} = \tfrac14[\gamma^a, \gamma^b] = \tfrac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$: the 28 matrices ($a < b$) from which every element of the part of Spin(4,4) connected to 1 is built as a product of exponentials $\exp(\theta S^{ab})$. (Sections 4.13, 5.12, 5.16, 5.21, 7.10, 7.16, 8.4, 10.33, 10.48, 16.24, 17.11, 17.21, 18.8, 18.19, 21.2, 21.7 and 22.12.)
- **Geodesic**: a curve whose velocity is parallel transported along itself: the straightest possible curve. Its equation is $d^2x^a/ds^2 + \sum_{b,c}\Gamma^a{}_{bc}\,(dx^b/ds)(dx^c/ds) = 0$. (Sections 3.16, 3.21 and 3.29.)
- **Geodesic deviation equation**: In general the distance $\xi(s)$ between two neighbouring geodesics of a surface obeys the geodesic deviation equation $d^2\xi/ds^2 = -\sigma\,\xi$ with the Gaussian curvature $\sigma = \sigma(1, 2)$ of Section 3.17 (a standard theorem, quoted, ASSUMED; on the sphere we have just verified it, with $\sigma = 1/a^2$). (Section 3.18.)
- **Geodesic equation**: $du^a/d\tau = -\sum_{b,c} \Gamma^a{}_{bc}\, u^b u^c$, with the Christoffel symbols $\Gamma^a{}_{bc}$ of the metric; its solutions are the paths of free fall. (Section 3.34.)
- **Ghost-like**: A component of negative classical energy is called ghost-like; it is not an established physical state. (Section 22.19.)
- **Ghost-like component**: a component of negative classical energy. (Section 22.22.)
- **Gibbs state**: In a finite-dimensional state space $\Omega$ has exactly one minimiser, the Gibbs state $\hat\rho_0 = e^{-(\hat H - \mu\hat N)/T}/Z$ with $Z = \mathrm{Tr}\,e^{-(\hat H - \mu\hat N)/T}$, and $\Omega[\hat\rho_0] = -T\ln Z$. (Sections 13.26 and 13.30.)
- **Git**: Git is the program that downloads the repository and keeps track of the versions of its files. (Section 0.8.)
- **GKD**: the Revision record's program (written in the language Rust) that computes the generalized delta without a determinant. (Sections 1.47, 11.2, 11.8 and 11.18; the opening of Chapter 11.)
- **Global U(1) transformation**: Multiplying every component of $\Psi$ by the same $e^{i\alpha}$ is a global U(1) transformation (U(1) is the name of the group of these phases). (Section 21.22.)
- **Good sector**: the fields that do not depend on $x_5, x_6, x_7$ ($k_5 = k_6 = k_7 = 0$). (Sections 4.9, 5.34, 5.37, 8.17, 8.22, 8.35, 10.4, 10.9, 10.20, 10.25, 10.42, 15.16, 17.2 and 21.29.)
- **Gradient**: the arrow $(\partial f/\partial x, \partial f/\partial y)$. It points in the direction in which $f$ grows fastest and is perpendicular to the level curve through its point. (Sections 2.18, 2.22 and 3.14.)
- **Gram matrix**: The 256 numbers $\mathrm{tr}(\gamma_A^T\gamma_B)$ therefore form the table $16\,\delta_{AB}$; this table is called the Gram matrix. (Sections 4.13, 10.5, 14.31 and 15.5.)
- **Gram-Schmidt method**: This is the Gram-Schmidt method. (Section 10.10.)
- **Gram-Schmidt procedure**: The Gram-Schmidt procedure: it goes through the columns of a matrix $P$ (the rows of `P.T`), subtracts from each column its parts along the columns already kept ($e^\dagger v$ is the size of the part of $v$ along the unit column $e$), and keeps it, divided by its length, when the length that remains is not zero. (Section 5.38.)
- **Grand potential**: When the particle number is fixed only on average by a chemical potential $\mu$, the equilibrium state at the temperature $T$ minimises the grand potential. (Sections 13.26, 13.30, 15.26 and 15.29.)
- **Grassmann**: Statistics: dirac16complex has complex ANTICOMMUTING components, called Grassmann numbers ($\theta_1\theta_2 = -\theta_2\theta_1$, so $\theta\theta = 0$); dirac16complex00 has complex COMMUTING components (ordinary complex numbers). (Section 18.2.)
- **Grassmann algebra**: all sums of ordinary numbers times monomials, with the rules above. (Sections 7.10 and 7.16.)
- **Grassmann generators**: symbols that anticommute, $\theta_1\theta_2 = -\theta_2\theta_1$, so $\theta_1\theta_1 = 0$. They model the anticommuting components of dirac16complex. (Section 18.19.)
- **Grassmann numbers**: The components of dirac16complex are anticommuting numbers, also called Grassmann numbers after the mathematician who introduced them: exchanging two of them in a product costs a sign, $\Psi_r\Psi_c = -\Psi_c\Psi_r$, and in particular $\Psi_r\Psi_r = -\Psi_r\Psi_r$, so $\Psi_r\Psi_r = 0$. (Sections 5.29, 7.1, 7.10 and 7.16.)
- **Gravitational field**: in this book, the author's metric of Section 0.1, the rule for the lengths of small steps; since Einstein, gravity is described by such a rule (Chapter 3). (Section 0.2.)
- **Great circle**: Great circle: a circle on the sphere whose centre is the centre of the sphere (the equator, the meridians, and all their rotations). (Sections 3.16 and 3.21.)
- **Greatest common divisor** $\gcd(p, q)$: the largest whole number that divides both $p$ and $q$ (`math.gcd`). (Sections 1.2 and 1.8.)
- **Grid**: the equally spaced times $t_n = nh$, $n = 0, 1, \dots, N$, with step $h = T/N$. (Sections 7.3, 7.8, 16.11 and 16.18.)
- **Grid error**: the difference between a number computed on a grid and the exact number. For the reference it shrinks like $h^2$. (Section 16.11.)
- **Grid, finite differences**: the line is replaced by equally spaced points; the second derivative is replaced by the difference formula $(f_{k+1} - 2 f_k + f_{k-1})/h^2$. (Section 13.35.)
- **Ground states**: Ground states ($T = 0$): three particle numbers $N = 8, 136, 688$, five couplings and five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$, that is $3 \cdot 5 \cdot 5 = 75$ states. (Sections 13.1 and 15.2.)
- **The ground states without interaction** (Notebook 15a, Out [7]; `Revision/kohn_sham/results/ground/summary.csv`):  (Section 15.15.)
- **Group**: a set of invertible matrices that contains the products and the inverses of its members. (Sections 5.11, 5.16 and 19.21.)
- **Group, Pin(4,4)**: a group is a collection of transformations that can be combined and undone; Pin(4,4) is the group of the transformations of the sixteen components of a field that go with the rotations and reflections of the eight directions, rotations in a wide sense that includes the mixing of space-like and time-like directions (Chapter 5). (Section 0.2.)
- **Growth rate**: $\kappa$ is the growth rate. (Sections 7.5, 8.18 and 8.22.)
- **Guide line**: For each ground state (`zip` pairs the colours with the ids) the left axes draw the distances $|E_{KS}(G) - R|$ against $h$ with logarithmic axes (`loglog`: equal distances on the axis are equal factors), as circles joined by lines (`"o-"`, line width 1.5, marker size 6), and a dashed guide line proportional to $h^2$ that starts a factor 3 below the first point. (Section 16.12.)

**H**

- **Half nodes**: The cell ends, the nodes, are $y_i = -L + i\,h$ for $i = 0, \dots, G$; the cell centres, the half nodes, are $y_{p+1/2} = -L + (p + \tfrac12)\,h$ for $p = 0, \dots, G - 1$. (Sections 16.14 and 16.18.)
- **Half-density term**: The record calls it the half-density term (volume and vielbein divergence). (Sections 6.29 and 8.5.)
- **Hamiltonian**: The energy operator of one particle in an external potential $v(x)$ is the Hamiltonian. (Sections 10.11 and 13.2.)
- **Hamiltonian density**: The rest of the Lagrangian has no $x_4$-derivative; the Revision record writes it as $-\mathcal{H}$ with the Hamiltonian density $\mathcal{H} = \cos z\,[\Psi^\dagger(mC - \sum_{\mu \neq x_4}C\gamma^\mu D_\mu)\Psi + U(S)]$, so that $\mathcal{L} = \Psi^\dagger K\partial_4\Psi - \mathcal{H}$ exactly, up to the total derivative (`python-field-theory.json`, check `hamiltonian_form_and_heisenberg_equation`). (Section 10.12.)
- **Harmonic trap**: the external potential $v(x) = x^2/2$, a parabola; a particle in it has the levels $1/2, 3/2, 5/2, \dots$ (in the units below). (Sections 13.32 and 13.35.)
- **Hartree**: The first term is a Hartree (direct) term, the second an exchange term. (Sections 13.4 and 14.26.)
- **Hartree approximation**: The older Hartree approximation keeps $v_H$ and drops the exchange integral, and with it the cancellation of the self-interaction. (Section 13.6.)
- **Hartree energy**: $E_H$ is the Hartree energy: the classical energy of the cloud $n$ with itself. (Sections 13.5 and 13.19.)
- **Hartree only**: (b) Hartree only: drop the exchange, $v_s = v + g_c n$; every fermion is then also repelled by its own density (the self-interaction of Section 13.5). (Section 13.32.)
- **Hartree potential**: the potential that one particle feels from the average density of all particles; exchange potential: the correction that comes from the Pauli principle (equal-label particles avoid each other). (Sections 13.6 and 13.35.)
- **Hartree term, exchange term**: the direct and the exchange part of the interaction energy. (Section 14.30.)
- **Hartree-Fock**: Hartree-Fock: keeping both, for a quasi-free state. (Sections 13.13 and 14.30.)
- **Hartree-Fock approximation**: The Hartree-Fock approximation takes the best single determinant: it minimises $\langle\Phi|\hat H|\Phi\rangle$ over all choices of $N$ orthonormal orbitals. (Section 13.6.)
- **Hash values**: When Python prints a set, the order of its members depends on their hash values, numbers computed from the names with a secret key that Python chooses anew every time it starts, unless the environment variable `PYTHONHASHSEED` (a named setting that a program receives when it starts) fixes the key. (Section 0.22.)
- **Headless**: A notebook can also be run without a browser (headless) with `jupyter nbconvert`; the run instructions print the exact command. (Section 0.8.)
- **Heat capacity** $C_V = dE/dT = T\,dS/dT$ at fixed $N$: how much energy one unit of temperature costs. (Sections 13.26, 13.30, 15.26 and 15.29.)
- **Heat map**: a picture of a matrix in which every entry is a coloured square. (Sections 0.16, 1.18, 1.24, 4.7, 5.9, 6.13, 6.21, 6.27, 7.17, 9.16, 9.17, 10.10, 13.14, 14.11, 15.24, 16.19, 17.2, 18.9, 19.15 and 20.11.)
- **Heisenberg equation**: Differentiating with the product rule, and using that $H$ commutes with $e^{\pm iHx_4}$ (both are power series in $H$), gives the Heisenberg equation. (Section 10.11.)
- **Hellmann-Feynman rule**: for a normalised eigenvector, the derivative of the level is the expectation value of the derivative of the Hamiltonian: $d\varepsilon/dk = \langle\chi|\,\partial h/\partial k\,|\chi\rangle$. (Sections 14.24 and 19.2.)
- **Hellmann-Feynman theorem**: the derivative of a level with respect to a parameter equals the matrix element of the derivative of the Hamiltonian. (Sections 15.21, 15.24 and 16.15.)
- **Hermitian**: $M^\dagger = M$. A Hermitian matrix has real eigenvalues. (Sections 1.36, 4.9, 4.11, 5.4, 5.9, 7.12, 7.16, 8.17, 8.22, 8.35, 9.25, 10.4, 10.9, 10.11, 13.2, 13.6, 14.4, 21.2, 21.14 and 22.6.)
- **Hermitian form, charge density**: a form $\Psi^\dagger X\Psi$ with a Hermitian matrix $X$; it is real for every $\Psi$. A charge density is the time component of a current. (Section 10.37.)
- **Hermitian matrix**: $H^\dagger = H$; a real Hermitian matrix is a symmetric matrix. (Sections 1.40 and 14.10.)
- **Hermitian part, anti-Hermitian part**: every matrix is $h = h_H + h_A$ with $h_H = \frac12(h + h^\dagger)$ Hermitian and $h_A = \frac12(h - h^\dagger)$ anti-Hermitian ($h_A^\dagger = -h_A$). (Section 10.42.)
- **Hex code**: Each colour is written as a hex code: `#` and three pairs of hexadecimal digits for the amounts of red, green and blue. (Section 3.13.)
- **Hexadecimal**: writing a number with the 16 digits `0`-`9` and `A`-`F` (worth 10 to 15); Python writes such a number with the prefix `0x`. One hexadecimal digit is exactly 4 bits. (Sections 0.18, 0.20, 0.24, 1.49 and 1.53.)
- **Hexadecimal colour codes**: The colours are written as hexadecimal colour codes: after `#`, three pairs of hexadecimal digits give the amounts of red, green and blue (from 00, none, to ff, 255). (Sections 0.17 and 17.11.)
- **Hidden**: The last one, $x_8$, is a hidden direction of space. (Sections 0.1, 3.1, 3.12, 3.34, 7.26, 8.2, 9.2, 12.1, 12.15 and 21.2.)
- **Hidden angle** $z = 6Hx_8$: the metric depends on $x_8$ only through $z$, which runs from $0$ to $\pi/2$ (the patch). $H > 0$ is a constant of the author's metric with the unit of an inverse length. (Section 12.2.)
- **Hidden coordinate** $y$: the book's coordinate along the hidden direction $x_8$, $y = \ln(\sin z)/(6H)$ with $z = 6 H x_8$; $y = 0$ is the end of the patch $z = \pi/2$ (the *brane*), and the interval is cut off at $y = -L$ (the *tip*). (Sections 2.24, 2.27, 3.12, 3.34, 8.28, 8.35, 14.10, 14.17, 17.2, 17.10, 17.20, 19.2, 19.15 and 19.20.)
- **Hidden direction**: Coordinates $x1, \dots, x8$: the eight numbers that name a point, with the author's names: $x1, x2, x3$ ordinary 3-space; $x4$ the time; $x5, x6, x7$ the three extra times; $x8$ the hidden direction. (Sections 6.13, 6.27 and 10.31.)
- **Hidden equation**: Their four independent parts are the constraint (time, $x_4$), the 3-space equation, the extra-time equation and the hidden equation ($x_8$). (Section 12.2.)
- **Hidden position** $y$: the coordinate $y = \ln(\sin z)/(6H)$ by which the Kohn-Sham record measures the hidden direction, so that $\sin^{1/6}z = e^{Hy}$. The patch end $z = \pi/2$ is $y = 0$, and $y < 0$ lies towards the tip. (Section 10.42.)
- **Hilbert adjoint** $X^*$ of an operator: the conjugate transpose of its matrix (with the ordinary, positive inner product of the Fock space). (Sections 5.34, 5.37, 10.11, 10.18 and 21.29.)
- **Hilbert norm**: The ordinary size of a column $u$ is the Hilbert norm $u^\dagger u = |u_1|^2 + \dots + |u_{16}|^2$. (Sections 8.19, 8.22 and 8.28.)
- **Hilbert space**: A space of states with a positive inner product is a Hilbert space. (Sections 10.11 and 10.18.)
- **Histogram**: bars that show how many numbers fall into each interval. (Sections 0.21, 1.32, 9.24, 9.25, 10.19 and 21.23.)
- **History** $a_4 = AHx_4$: the time dependence of the metric used for the numbers, the one of the Revision Kohn-Sham work ($A = 1$, $H = 1$); with $A > 0$ the extra times deflate. (Sections 3.34, 8.28, 11.2, 11.26, 14.24, 15.13, 17.10, 17.20 and 22.11.)
- **Hohenberg-Kohn theorem**: the ground-state density determines the external potential (up to a constant); Kohn-Sham inversion: finding the potential of NON-interacting electrons that gives the same density. (Section 13.13.)
- **Hole**: an empty place in a level that is normally occupied. (Sections 13.27 and 15.29.)
- **Holonomy** (turning angle): the angle by which a parallel-transported vector is turned after going once around a closed curve. (Section 3.21.)
- **HOMO**: `homo_lumo` returns the highest occupied level (HOMO: occupation above one half) and the lowest empty one (LUMO). (Sections 13.35, 15.13, 16.11, 19.20 and 19.21.)
- **Homogeneous**: Take a homogeneous configuration: one that depends on the time $x_4$ only, so that $\partial_\mu\Phi = 0$ for every $\mu \neq x_4$. (Sections 9.12 and 18.21.)
- **Homogeneous configuration**: A condensate (also called a homogeneous configuration) is a field that is the same at every place: it depends on the time $x_4$ only, not on $x_1, x_2, x_3, x_5, x_6, x_7, x_8$. (Section 9.18.)
- **Homogeneous field**: a field that does not depend on $x_1, x_2, x_3, x_5, x_6, x_7, x_8$, only on the time $x_4$. (Section 18.26.)
- **Homogeneous of degree 2**: $e_{\rm int}$ is homogeneous of degree 2: doubling both densities multiplies it by 4. (Section 14.27.)
- **Honesty ledger**: The honesty ledger is the table of the main statements of the book, each with its label (Section 0.3), a short note where one is needed, and the reports of the Revision record that verify it. (Section 0.18.)
- **Honesty rule**: The book therefore follows one rule above every other, the honesty rule: it teaches exactly what the Revision record proves and computes, with every assumption, and it never writes "proved" for a statement that is not proved. (Section 0.2.)
- **Hyperbola**: Since $\cosh^2t - \sinh^2t = 1$, the points $(\pm\cosh t, \sinh t)$ lie on the hyperbola $a^2 - b^2 = 1$ (blue, the columns of Krein norm $+1$) and the points $(\sinh t, \pm\cosh t)$ on $a^2 - b^2 = -1$ (orange). (Sections 1.13, 6.16 and 10.19.)
- **Hyperbolic cosine**: the function $\cosh\varphi = (e^{\varphi} + e^{-\varphi})/2$. (Section 1.13.)
- **Hyperbolic functions**: $\cosh\varphi = (e^{\varphi} + e^{-\varphi})/2$ and $\sinh\varphi = (e^{\varphi} - e^{-\varphi})/2$; they satisfy $\cosh^2\varphi - \sinh^2\varphi = 1$. (Sections 1.16, 5.21, 6.21 and 8.3.)
- **Hyperbolic sine**: the function $\sinh\varphi = (e^{\varphi} - e^{-\varphi})/2$. (Section 1.13.)
- **Hyperbolic sine and cosine**: We use the hyperbolic sine and cosine, $\sinh t = (e^t - e^{-t})/2$ and $\cosh t = (e^t + e^{-t})/2$: each is the derivative of the other, $\sinh 0 = 0$, and both are positive for $t > 0$. (Section 16.13.)
- **Hypotheses** (`Revision/pairing/kohn_sham/t3-theory.json`, hypotheses H1 to H6, in words):  (Sections 19.10, 20.5 and 20.7.)
- **HYPOTHESIS**: a status label: an idea, such as a proposed mechanism or scenario, that is stated and examined but that this book does not establish. Example: the author's Hypothesis P, that the big bang creates universes of masses $+M$ and $-M$ in pairs (Section 20.3). (Sections 0.3, 0.20, 5.39, 12.31, 15.31, 20.3, 21.19, 21.37, 22.2 and 22.27.)
- **Hypothesis P**: Hypothesis P ("the big bang creates universes of masses $+M$ and $-M$ in pairs") therefore remains what it was: a HYPOTHESIS. (Section 20.26.)

**I**

- **Identity**: The identity $1$ has ones on the diagonal and zeros elsewhere: $1A = A1 = A$. (Sections 4.19, 10.9 and 21.14.)
- **Identity in the jets**: a polynomial whose every coefficient is zero. It is zero for EVERY value of the jet, that is, for every field at every point, whether the field solves the field equations or not (*off shell*). An identity off shell holds in particular for solutions (*on shell*). (Section 18.19.)
- **Identity matrix** $I$: the square matrix with 1 on the diagonal and 0 elsewhere. (Sections 1.12, 1.18, 1.24, 4.2, 4.7 and 5.9.)
- **If**: Hence the total charge $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ of one solution is constant in time if its current flux through the boundary of the seven other directions vanishes (Section 5.6); this is a conditional statement, and its condition is not established (next list). (Section 5.39.)
- **Ill-conditioned**: The problem is ill-conditioned: its answer reacts strongly to small errors of its input. (Section 16.20.)
- **Illinois method**: All brackets are refined together, 16 rounds, by the Illinois method. (Section 19.16.)
- **Image**: the orbital, state or problem obtained by applying the map of T3. (Sections 5.11, 19.2 and 19.10.)
- **Imaginary part**: The number $a = \mathrm{Re}\,z$ is its real part and $b = \mathrm{Im}\,z$ its imaginary part. (Sections 1.10 and 1.16.)
- **Imaginary unit** $i$: a new number with $i^2 = -1$. Python writes it `1j`, sympy writes it `I`. (Sections 1.10 and 1.16.)
- **Indefinite**: a quadratic expression that can take both signs. (Sections 1.37, 5.34 and 21.22.)
- **Indefinite (Krein) metric**: a rule for the squared length of a quantum state that can also give negative numbers (Chapter 10). (Section 0.2.)
- **Independent universes**: two quantum fields $\Psi_1, \Psi_2$ on one state space with $\{\Psi_{1A}, \Psi_{2C}^\dagger\} = 0$ and $\{\Psi_{1A}, \Psi_{2C}\} = 0$: nothing done to one changes the anticommutation rules of the other. (Section 10.48.)
- **Index**: a letter such as $i$, $j$ or $k$ that numbers the components of a vector or the rows and columns of a matrix. In mathematics rows and columns are numbered $1, 2, 3, \dots$; Python numbers them $0, 1, 2, \dots$, so the entry $A_{11}$ (row 1, column 1) is `A[0, 0]` in Python. (Sections 1.18, 1.24, 1.26, 1.32 and 3.2.)
- **Index list**: an ordered list of labels, such as $(x_1, x_3, x_3)$; its length is the number of entries (here 3). (Sections 1.42, 1.47, 11.2 and 11.8.)
- **Index notation**: $a, b, c, \dots$ each run over the eight coordinates $x_1, \dots, x_8$; an upper and a lower index are positions in a table of numbers; $\partial_c$ means the partial derivative $\partial/\partial x_c$. (Sections 1.26 and 3.29.)
- **Index up, index down**: a tensor component carries upper and lower coordinate labels, such as $R^{ab}{}_{cd}$; a label is raised with the inverse metric. (Sections 11.18 and 12.2.)
- **Inertia**: On an eigenspace of a real frequency $E \neq 0$, by contrast, the Krein form has four positive and four negative directions: its inertia is (4,4) (PROVED in the pairing record for every real frequency; `python-pairing.json`, checks `Q.one_particle_Krein_inertia_proof` and, for an exact sample, `Q.one_particle_Krein_inertia`). (Sections 8.19 and 10.9.)
- **Inflate**: The author's metric (the rule that gives the length of a small step in each direction; Section 0.14 introduces it from zero) makes ordinary space grow (inflate) and the three extra times shrink (deflate) exponentially as the time $x_4$ runs. (Sections 0.1, 0.14, 0.16, 3.5, 3.12, 4.4, 8.2, 11.26 and 14.2.)
- **Inflating**: Inflating means growing, deflating shrinking. (Sections 8.28 and 14.10.)
- **Initial values**: Given the values at one point (the initial values) it fixes the functions everywhere. (Section 15.8.)
- **Initial-value (Cauchy) problem**: find the field at later times $x_4$ from its values at $x_4 = 0$ (the *data*). (Section 8.22.)
- **Initial-value problem**: an ODE together with the starting value $y(0)$. Exactly one solution belongs to it (for the smooth $f$ of Notebook 02a). (Sections 2.2, 2.10, 8.16 and 12.24.)
- **Inner product**: The inner product of two states $\phi$ and $\psi$ is the complex number. (Sections 10.11, 10.18 and 13.2.)
- **Instability**: An imaginary part of a frequency is the mathematical sign of an instability; Chapter 8 meets it in the waves along the extra times. (Section 1.13.)
- **Instantaneous**: computed with the coefficients of one instant, as if they did not change. (Sections 10.39, 10.42, 15.21, 19.2 and 22.2.)
- **Instantaneous (adiabatic) state**: the ground state of the Hamiltonian $h(a_{4,0})$ of one instant of the history (one slice $a_{4,0}$); the history itself keeps moving, with 3-space inflating and the extra times deflating. (Section 15.24.)
- **Instantaneous level and orbital**: a solution $h\varphi = \varepsilon\varphi$ of the Hamiltonian $h$ of one slice. (Section 22.11.)
- **Integers**: The whole numbers (or integers) are $\dots, -2, -1, 0, 1, 2, \dots$. (Section 1.2.)
- **Integral over the patch** $\int X$: the total amount of a density $X$ in the computed region, $2\,\mathrm{Vol}_7\int_{-3}^{0}e^{6Hy}X\,dy$ (Section 17.7). (Sections 17.2 and 17.10.)
- **Integration by parts**: the product rule $\frac{d}{dt}(fg) = \dot f g + f\dot g$ integrated from $0$ to $T$: $\int_0^T f\dot g\,dt = [fg]_0^T - \int_0^T \dot f g\,dt$, where $[fg]_0^T = f(T)g(T) - f(0)g(0)$ is the boundary term. (Sections 7.2 and 7.8.)
- **Interaction**: The interaction $-U(S) = -\tfrac{\lambda}{2}S^2$ with a real coupling $\lambda$ is quartic in the field. (Section 7.19.)
- **Interaction energy density** $e_{int} = \lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$: the energy of the contact interaction per proper 7-volume. (Sections 15.19 and 19.4.)
- **Intermediate value theorem**: If $F$ is continuous, it has a zero between them: this is the intermediate value theorem of calculus (ASSUMED: quoted without proof). (Section 2.12.)
- **Intertwiner**: a matrix $X$ with $\gamma^a X = X \hat\gamma^a$ for every $a$. (Sections 4.17, 4.19, 5.11 and 5.16.)
- **Intertwiner condition**: A charge-conjugation matrix is a constant $16 \times 16$ matrix $\mathcal{C}$ for which the matrix $M = \mathcal{C}C$ obeys the intertwiner condition. (Sections 5.28 and 5.32.)
- **Invariant**: Three facts follow from the definition, by the computation just made: a contraction of one upper with one lower index of a tensor is again a tensor (with two fewer indices); a product of tensors is a tensor; and a quantity in which every index is contracted, an invariant (or scalar), has the same value in every system of coordinates. (Sections 3.14, 3.29, 5.11, 10.33 and 10.37.)
- **Invariant mass** $\mu$ of a collection of bodies: $\mu^2 = E_{\rm tot}^2 - |\vec p_{\rm tot}|^2$, computed from the totals. Because the totals are conserved, so is $\mu$. For one body $\mu$ is its mass. (Sections 20.17 and 20.20.)
- **Inverse** $M^{-1}$: the matrix with $M M^{-1} = M^{-1} M = 1$. When $MM = 1$, the matrix is its own inverse. (Sections 1.19, 4.2, 5.9 and 6.13.)
- **Inverse metric**: Metric $g_{\mu\nu}$, inverse metric $g^{\mu\nu}$ (the inverse matrix: $\sum_\lambda g^{\mu\lambda} g_{\lambda\nu} = \delta^\mu{}_\nu$, which is $1$ when $\mu = \nu$ and $0$ otherwise). (Sections 3.29, 11.2 and 11.18.)
- **Inverse vielbein**: The inverse vielbein $e_a{}^\mu$ is the inverse matrix, $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ (1 when $a = b$, 0 otherwise). (Section 6.2.)
- **Inversion**: a pair of places in a permutation whose two entries stand in the wrong order (the larger one first). (Sections 1.19, 1.24, 1.47, 4.2, 11.2, 11.8 and 18.9.)
- **Invertible**: A square matrix $M$ is invertible if there is a matrix $M^{-1}$ with $MM^{-1} = M^{-1}M = I$; then the equation $Mv = w$ can be undone, $v = M^{-1}w$. (Section 1.20.)
- **Involution**: A map is an involution when applying it twice gives back the start. (Sections 19.2 and 19.9.)
- **Irrational**: A number that is not a fraction is called irrational; its decimal digits never end and never repeat (by the formula of Section 1.2, a number whose digits end or repeat is a fraction). (Sections 1.3 and 1.8.)
- **Irreducible**: The representation is irreducible when there is no other invariant subspace: the 16 components cannot be cut into smaller pieces that the group keeps apart. (Sections 5.11, 5.16 and 21.9.)
- **Isometry**: a change of coordinates that does not change the metric. (Sections 18.2, 18.19 and 20.22.)
- **Isotropic**: For a configuration that looks the same in the three directions of 3-space (such a configuration is called isotropic in 3-space), $T^{x_1}{}_{x_1} = T^{x_2}{}_{x_2} = T^{x_3}{}_{x_3} = p_3$, and likewise $p_t$ for a configuration isotropic in the extra times. (Section 9.4.)
- **Iteration**: One iteration: (1) from the input $x$, solve every level of the label set (Section 15.3); (2) fill them (aufbau at $T = 0$, Fermi-Dirac at $T > 0$); (3) build the densities $n$ and $S$ and from them the output potentials $x_{out} = \big(\tfrac{15}{16}\lambda S,\ -\tfrac{1}{16}\lambda n\big)$; (4) the residual is $r = x_{out} - x$, and its size is its largest entry in absolute value. (Sections 13.35 and 15.5.)

**J**

- **Jacobi identity**: Multiplying out shows the Jacobi identity $[[X, Y], Z] = [X, [Y, Z]] - [Y, [X, Z]]$ for any three matrices (both sides are $XYZ - YXZ - ZXY + ZYX$). (Section 5.23.)
- **Jacobi's formula** for the derivative of the volume factor of a diagonal metric:  (Section 2.19.)
- **Jacobian matrix**: The $n \times n$ table of partial derivatives $\partial x'^a/\partial x^b$ is the Jacobian matrix of the change. (Section 3.14.)
- **Janak's theorem**: the derivative of the self-consistent energy with respect to the occupation $f_a$ of an orbital is its level $\epsilon_a$. (Section 13.30.)
- **Jet**: the value of a field component and its derivatives at one point, treated as independent symbols ($\psi_A$, $\partial_\mu\psi_A$, ...). (Sections 7.13, 7.26, 7.32, 9.17, 18.2, 18.19 and 20.10.)
- **Jet at a point**: the values of the field and of its eight first derivatives at one point. The energy-momentum tensor needs nothing else. (Section 9.16.)
- **Jitter**: `rng.uniform(-0.28, 0.28, size=...)` gives one random number between $-0.28$ and $0.28$ per ratio; adding it to the class's position spreads the dots a little sideways so that they do not hide one another (jitter). (Section 16.12.)
- **Job**: A ground-state job (one unit of work of the program) solves the state, its Delta-SCF excited state (one quantum moved from the highest occupied to the lowest empty group of levels), four neighbouring slices $a_{4,0} \pm 0.002$ and $a_{4,0} \pm 0.004$ at fixed occupations (for the derivative $dE/da_4$ and the adiabaticity measure of Chapter 15), and the list of the lowest particle-hole excitations, each on the three grids. (Section 16.3.)
- **Jordan-Wigner**: The sign rule that makes them anticommute is the Jordan-Wigner rule: acting on mode $j$ gives the factor $(-1)$ to the power of the number of occupied modes before $j$. (Sections 21.26 and 21.29.)
- **JSON** and **CSV**: two text formats for stored numbers (JSON: named entries in braces; CSV: a table, one line per row, entries separated by commas). (Sections 0.16, 16.11 and 23.11.)
- **Junction condition**: an equation that says how the fields and the geometry must match across a surface, here across the brane $z = \pi/2$. The junction conditions at the brane are not derived in this book: the Z2 mirror continuation is ASSUMED, and deriving the conditions is an open problem (OPEN, Section 22.15). (Sections 18.2, 22.2 and 22.15.)
- **Jupyter notebook**: Every worked example of the book is a Jupyter notebook: a file (with the ending `.ipynb`) that holds text and Python code in cells, together with everything the code printed and drew when it ran. (Section 0.7.)
- **JupyterLab** shows a notebook in your web browser and runs it: with the environment active, in the folder `Revision/textbook/notebooks`, the command `jupyter lab` followed by the name of the notebook file opens it, and the menu Run > Run All Cells runs every cell from the top. (Section 0.8.)

**K**

- **Kernel**: The kernel is the running Python program that executes the code cells one after the other. (Sections 0.7, 5.11 and 18.2.)
- **Key**: `read_levels` reads the level table of one state and returns a dictionary whose key is the key of a level, the four numbers (shell $n_2$, block type $j$, parity, Pruefer label $l$), and whose value is the pair (level, occupation). (Section 15.14.)
- **Key rule**: With line 10 this gives the key rule for all 64 pairs $A, B = 0, \dots, 7$: $\tau_A\bar\tau_B + \tau_B\bar\tau_A = \bar\tau_A\tau_B + \bar\tau_B\tau_A = 2\,\mathrm{eta4488}_{AB}\, I_8$. (Section 4.5.)
- **Kinetic numbers**: The eight kinetic numbers $\Psi^TC\gamma^a\Phi$ are computed before and after the map $\Gamma$, and so is the scalar: $S = \Psi^TC\Psi$ before and $(\Gamma\Psi)^TC(\Gamma\Psi)$ after. (Section 21.15.)
- **Kinetic part**: The terms with derivatives (the $K$'s) form the kinetic part; the terms without derivatives, $mS + U(S)$, form the potential part. (Section 9.7.)
- **Kinetic term** $K_\mu$: the part of the Lagrangian that holds the derivative along the direction $\mu$; potential energy: $mS + U(S)$, the part without derivatives. (Sections 7.19, 9.16 and 18.4.)
- **Kinetic term of the direction**: The number $K_\mu$ (no sum) is called the kinetic term of the direction $x_\mu$: the part of the Lagrangian that holds the derivative along $x_\mu$. (Section 9.3.)
- **Kinetic-sum identity**: This kinetic-sum identity holds off shell (PROVED; check `kinetic_sum_on_shell_C`). (Section 9.8.)
- **Kink**: Kink: a point where a function is continuous but its slope jumps. (Section 22.2.)
- **Klein's inequality**: $D = \mathrm{Tr}[\hat\rho(\ln\hat\rho - \ln\hat\sigma)] \ge 0$ for two density operators, with equality only when they are equal. (Sections 13.26 and 13.30.)
- **Klein-Gordon equation**: So $\partial_4^2\phi = \partial_1^2\phi - m^2\phi$: the wave equation with a mass, called the Klein-Gordon equation. (Section 7.5.)
- **Kohn-Sham**: The spinor fields of Chapters 4 to 10 need its vielbein (the scale factors of Section 3.7); the energy-momentum tensor of Chapter 9 needs its Christoffel symbols (Section 3.23); the field equations of the metric function $a_4$ in Chapter 12 need its Einstein tensor (Section 3.25); the Kohn-Sham model of Chapters 14 to 17 (Kohn-Sham: an approximation of density functional theory that replaces many interacting particles by independent particles, each moving in one common effective potential; Chapter 13 teaches it from zero) is written in the hidden coordinate $y$ of Section 3.9. (Section 3.1.)
- **Kohn-Sham approximation**: Rows 8, 9, 12 and 13 rest on the Kohn-Sham approximation, which is ASSUMED, not derived. (Section 0.18.)
- **Kohn-Sham energy**: and the Kohn-Sham energy of the doubled system is $E_{KS} = \sum g\,f\,\varepsilon - 2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}e_{int}\,dy$. (Section 15.2.)
- **Kohn-Sham equations**: one-particle Schroedinger equations in an effective potential $v_s(x)$ chosen so that their orbitals give the density of the interacting system. (Sections 13.10 and 13.35.)
- **Kohn-Sham gap** $\Delta_{KS}$: the smallest cost of moving one particle from an occupied Kohn-Sham orbital to an empty one, $\Delta_{KS} = \epsilon_{LUMO} - \epsilon_{HOMO}$ (lowest unoccupied minus highest occupied level). In an interacting system the levels move when the occupations change, so $\Delta_{KS}$ is only a first estimate of the lowest excitation energy. (Sections 13.27, 15.13 and 19.20.)
- **Kohn-Sham inversion**: Hohenberg-Kohn theorem: the ground-state density determines the external potential (up to a constant); Kohn-Sham inversion: finding the potential of NON-interacting electrons that gives the same density. (Section 13.13.)
- **Kohn-Sham potential**: the derivative of the interaction energy density with respect to a density; it enters the one-quantum equation. (Sections 13.10 and 14.30.)
- **Kohn-Sham state**: an approximate state of many identical fermions, built from one-particle wave functions (*orbitals*) that each solve a one-particle equation in a common *effective potential*; the potential depends on the densities of the occupied orbitals, so the equations must be solved *self-consistently*. (Sections 15.13, 17.2, 17.10, 17.20, 19.2 and 19.20; the opening of Chapter 19.)
- **Kohn-Sham universe**: a solution of the equations of the density-functional approximation, in which the field moves in a potential computed from its own density; self-consistent means that this potential and this density fit each other; the mass of the field in this model is written $M$ (Chapters 13 to 15). (Section 0.2.)
- **Krein**: Because $B$ has eight eigenvalues $+1$ and eight $-1$, the state space carries an indefinite Krein form when $\Psi^\dagger$ is read as the ordinary adjoint (Chapter 10). (Section 18.22.)
- **Krein (indefinite) form**: the form $\Phi^\dagger B\Phi$ built with the matrix $B$, which has eight eigenvalues $+1$ and eight eigenvalues $-1$; it can be positive or negative. (Section 9.24.)
- **Krein boost**: A Krein boost of a pair, $u_1' = \cosh t\,u_1 + \sinh t\,u_9$ and $u_9' = \sinh t\,u_1 + \cosh t\,u_9$ (with $Bu_1 = u_1$, $Bu_9 = -u_9$, both of length 1 and orthogonal), keeps the Krein norms, because $\cosh^2t - \sinh^2t = 1$, and keeps the two modes Krein-orthogonal, because $\cosh t\,\sinh t - \sinh t\,\cosh t = 0$; but it changes the ordinary squared length to $\cosh^2t + \sinh^2t$. (Section 10.14.)
- **Krein form**: the number $u^\dagger B v$ for two columns $u, v$. Because $B$ is Hermitian, $u^\dagger B u$ is real, but it can be positive, negative or zero. In the theory it is the charge of the wave $u$. (Sections 8.19, 8.22, 8.28, 10.2, 10.9, 10.18 and 21.29.)
- **Krein form, Krein charge**: $\int\cos z\,u^\dagger Bv\,dx_8$; for $u = v = \Psi$ it is the charge of the wave. (Section 10.31.)
- **Krein inertia** of a set of columns: how many independent directions have a positive and how many a negative Krein norm. (Sections 9.21, 10.5, 10.42, 18.26, 21.26 and 21.29.)
- **Krein matrix** $B = -iC\gamma^{(x_4)}$: the charge density is $\Psi^\dagger B\Psi$, and $B$ is the matrix of the canonical anticommutator of the quantised field (Chapter 10). (Sections 18.2, 20.2, 21.2, 21.7, 21.14 and 21.29.)
- **Krein norm** of a column $u$: the real number $u^\dagger Bu$, which can be positive or negative because $B$ has eight eigenvalues $+1$ and eight $-1$. (Sections 10.2, 18.2 and 18.26.)
- **Krein self-adjoint**: In words, $h$ is Krein self-adjoint: $Bh = h^\dagger B$. (Section 10.4.)
- **Krein sign** $\sigma$ of a map $M$: the sign in $MBM^\dagger = \sigma B$. (Sections 14.5, 18.2, 18.8 and 19.2.)
- **Krein space**: a space with an *indefinite* inner product (some vectors have a negative norm). (Sections 1.37, 5.34, 5.37, 10.13, 10.18 and 21.25.)
- **Krein-neutral**: So the Krein form vanishes identically on the eigenspace of a growing frequency: the eigenspace is Krein-neutral (PROVED by the argument just given; the pairing record proves the same and checks it on exact samples, `Revision/pairing/reports/python-pairing.json`, check `Q.one_particle_complex_frequency_Krein_neutral`). (Sections 8.19, 10.5, 10.42, 18.23, 18.27, 21.26 and 21.29.)
- **Krein-orthonormal modes**: columns $u_n$ with $u_n^\dagger B u_m = \epsilon_n \delta_{nm}$, $\epsilon_n = +1$ or $-1$. A *Krein boost* mixes a mode of Krein norm $+1$ with one of $-1$ by the numbers $\cosh t$ and $\sinh t$; it keeps the Krein form but changes the ordinary length. (Section 10.18.)
- **Krein-unitary**: We call such an $R$ Krein-unitary. (Sections 10.34 and 10.37.)
- **Kretschmann scalar** $K = \sum_{a,b,c,d} R^{ab}{}_{cd} R^{cd}{}_{ab}$: one number per point, the same in every coordinate system (an invariant). (Sections 3.17, 3.21 and 3.29.)
- **Kronecker delta** $\delta^a_b$: 1 if $a = b$ and 0 otherwise; as a table it is the identity matrix $I$. (Sections 1.18, 1.24, 1.32, 1.42, 1.47, 4.2, 4.7, 11.2 and 11.8.)
- **Kronecker product** `np.kron(L, R)`: the big matrix whose block in block row $r$ and block column $k$ is $L_{rk}$ times the whole matrix $R$. (Sections 4.17, 4.19, 5.13, 5.16, 10.38 and 21.15.)
- **KS gap**: HOMO, LUMO: the highest occupied and lowest unoccupied level; the KS gap is their difference. (Section 16.11.)

**L**

- **L1 measure**: The record measures the remaining part in two ways: $\mu_1 = \int e^{6Hy}|X - \bar X|\,dy/\int e^{6Hy}|X|\,dy$ (the L1 measure) and $\mu = \sqrt{D(\bar X)/D(0)}$ (the L2 measure); both are 0 for a flat profile. (Section 17.17.)
- **L2 measure**: The record measures the remaining part in two ways: $\mu_1 = \int e^{6Hy}|X - \bar X|\,dy/\int e^{6Hy}|X|\,dy$ (the L1 measure) and $\mu = \sqrt{D(\bar X)/D(0)}$ (the L2 measure); both are 0 for a flat profile. (Section 17.17.)
- **Label**: a name of a coordinate, here $x_1, \dots, x_8$. The computer often numbers them $0, \dots, 7$; only the question "are two labels equal?" matters below, so the names do not change any result. (Sections 1.42, 1.47, 2.24, 2.27, 11.2, 13.19, 13.35, 14.13, 14.14, 14.24, 15.8, 16.11, 19.21, 22.2 and 22.11.)
- **Label set**: For a state of the gas the solver chooses the sectors and labels it will solve, its label set. (Section 15.4.)
- **Lagrange multiplier**: The number $\lambda$ is a Lagrange multiplier; with several conditions one takes one multiplier for each. (Section 13.6.)
- **Lagrangian**: the function from which the equations of a field follow (Chapter 7). (Sections 0.2, 7.2, 7.8 and 10.48; the opening of Chapter 7.)
- **Lagrangian density** $L$: the function whose integral (the action) must not change to first order when the field is varied; that requirement is the Euler-Lagrange equation, the field equation. (Sections 7.5, 7.8 and 7.26.)
- **Lambda**: A lambda is a function written in one line without a name: `lambda e: ...` takes an entry `e`, multiplies it out, replaces every $w^2$ by $m^2 + k_s^2 - k_t^2$ (the expression `w2_sym` of In [6]) and multiplies out again. (Sections 10.10, 16.12 and 16.19.)
- **Laplace's rule**: Laplace's rule for determinants of every size, and the expansion of every Lovelock tensor along the column of its free upper label, $P_{(k)} = \delta\,L_{(k)} - 2k\,Y_{(k)}$ (Section 11.13; Notebook 11b, In [21]). (Section 11.28.)
- **Laurent polynomial**: The program represents every quantity as an exact Laurent polynomial (a sum of monomials that may contain negative powers, such as $\cot^{-1}z$) in $H$, $a_4'$, $a_4''$ (and the higher derivatives), $e^{a_4}$, $\sin^{1/3}z$ and $\cot z$, with coefficients that are exact fractions of whole numbers (the files `poly.rs` and `rational.rs` of the crate; every operation that would overflow stops the program instead of rounding). (Sections 11.12, 11.18 and 12.16.)
- **Laws of powers**: Power $a^p$ and root $a^{1/n}$; the laws of powers $a^p a^q = a^{p+q}$, $(a^p)^q = a^{pq}$, $(ab)^p = a^p b^p$, $a^{-p} = 1/a^p$ for positive $a, b$. (Section 1.8.)
- **Lax-Mizohata theorem**: a standard theorem of the theory of partial differential equations (P. D. Lax, 1957; S. Mizohata, 1961), quoted in this book without proof and therefore ASSUMED: if the initial-value problem of a linear system of first-order equations with smooth coefficients is well posed near a point, then at that point the frequencies of its principal part are real for every real momentum. (Section 8.18.)
- **Lead checks**: short independent Python programs of the Revision record (folder `Revision/lead_checks`), written from scratch by the coordinator of the Revision work (the "lead") without importing any other Revision code; each writes a report with a list of named checks and their verdicts. (Sections 3.7, 3.12 and 3.29.)
- **Lead report**: The lead report is the file `emt-divergence-and-spin-connection.json` in the folder `Revision/lead_checks/reports`, written by an independent program of the lead of the Revision work. (Section 6.1.)
- **Leaf**, **pruning** (skipping): a complete combination of $k$ curvature entries in the computer's search; pruning means leaving out combinations known to give zero. (Sections 11.2 and 11.12.)
- **Least squares**: the straight line through a set of points that makes the sum of the squared vertical distances of the points from the line as small as possible. (Sections 2.6, 13.21, 17.2 and 17.20.)
- **Ledger**: the table of the statements, their labels and the reports that verify them. (Section 0.20.)
- **Left (right) derivative** $\partial_L F / \partial \theta_k$ ($\partial_R F / \partial \theta_k$): move $\theta_k$ to the far left (right) of every monomial that contains it, collecting a $-1$ for every generator it passes, and then delete it. (Section 7.16.)
- **Left derivative**: The left derivative $\partial_L F/\partial\theta_k$: in every monomial that contains $\theta_k$, move $\theta_k$ to the far left, collecting a $-1$ for every generator it passes, and then delete it; monomials without $\theta_k$ give nothing. (Sections 7.11 and 18.20.)
- **Left multiplication**: For a fixed quaternion $u$ the right multiplication $R_u$ maps $q$ to $q\,u$ and the left multiplication $L_u$ maps $q$ to $u\,q$. (Section 4.5.)
- **Legend**: `plot` draws a curve through the points; `lw` is the line width, `ls` the line style (two hyphens in quotes mean dashed, a colon `":"` dotted), and `label` the text for the legend (the box that names the curves), which `legend` draws in the upper right corner. (Section 19.16.)
- **Legendre transform**: the rule that turns a Lagrangian into the energy (Hamiltonian) density: for each field, its time derivative times its canonical momentum, summed over the fields, minus the Lagrangian. (Section 18.2.)
- **Leibniz formula**: the sum over all $n!$ permutations $\sigma$ of $1, \dots, n$ (the Leibniz formula). (Section 1.20.)
- **Lemma**: a proved statement that is a step towards others (Notebook 20c). Compare Proposition and Schur's lemma. (Section 20.20.)
- **Length**: Length (norm) of a vector, $|v| = \sqrt{v_1^2 + \dots + v_n^2}$; a unit vector has length 1. (Sections 1.36, 1.40, 1.42, 1.47, 2.18, 10.11, 11.2 and 11.8.)
- **Length factor**: the number $f_i = \sqrt{|g_{ii}|}$; a small step $dx_i$ along $x_i$ has the size $f_i \, |dx_i|$. (Sections 0.14, 0.16 and 1.5.)
- **Lepton number** $L$: $+1$ for the electron and its neutrino $\nu_e$, $-1$ for the positron and the antineutrino $\bar\nu_e$, $0$ for quarks and photons. It is not the Lagrangian $\mathcal{L}$. (Sections 21.2 and 21.35.)
- **Level**: an allowed energy $\varepsilon$ of the one-particle equation. (Sections 14.3, 14.17, 14.24, 15.13, 16.18, 16.23, 19.2, 19.15, 19.20 and 22.2.)
- **Level curve**: A level curve (contour) is a curve on which $f$ has one fixed value. (Sections 2.18 and 2.22.)
- **Level key** `n2:j:parity:rank`: the shell $n_2 = |\vec n|^2$ of the 3-space momentum, the block type $j = \pm 1$, the brane parity (even or odd), and the rank, the position of the level among the particle levels of its sector (0 = the lowest). (Section 16.11.)
- **Level ladder**: For each case a level ladder at the horizontal place $x_0 = 0, 3, 6$: every exact level is a short horizontal line (from $x_0 + \text{shift} - 0.4$ to $x_0 + \text{shift} + 0.4$), even parity at the left and odd parity $1.2$ further right, and the numerical level is a marker in its middle. (Section 14.18.)
- **Levi-Civita symbol** $\varepsilon_{i_1 \dots i_n}$: the sign of the list $(i_1, \dots, i_n)$ if it is a re-ordering of all $n$ labels, and 0 otherwise. (Sections 1.44, 1.47, 4.5 and 11.2.)
- **Levi-Civita tensors**: The author's notebook builds the generalized delta also in a second way, from two Levi-Civita tensors, in the cell In[32] (record `Revision/gkd_lovelock/results/notebook-input-cells.txt`). (Section 11.5.)
- **Lie algebra so(4,4)**: the commutation rules $[S^{ab}, S^{cd}] = \eta^{bc}S^{ad} - \eta^{ac}S^{bd} - \eta^{bd}S^{ac} + \eta^{ad}S^{bc}$ of the 28 generators. (Sections 5.18 and 5.21.)
- **Light line**: One square panel. 200 rapidities from $-1.4$ to $1.4$ trace the two unit hyperbolas: $(\cosh b, \sinh b)$, where $t^2 - y^2 = 1$ (blue), and $(\sinh b, \cosh b)$, where $y^2 - t^2 = 1$ (orange); the dotted diagonal is the light line $t = y$. (Section 6.22.)
- **Light-like** vector: $v \neq 0$ with $Q(v) = 0$ (notebook 01e). (Sections 1.13, 1.27, 1.32 and 1.40.)
- **Line**: Two wrong paths with the same end values are the line $q = t$ and the parabola $q = t^2$. (Section 7.2.)
- **Line continuation**: The second statement is broken over two lines by a backslash at the end of the first (a line continuation); it tests that $(\Gamma r)^TC(\Gamma r) - r^TCr$ is exactly zero, so $\Gamma$ keeps $S$. (Section 21.15.)
- **Line element**: the formula for $ds^2$. (Sections 1.29, 1.32, 3.3 and 3.12.)
- **Linear**: The map $v \mapsto Av$ is linear: $A(v + w) = Av + Aw$ and $A(cv) = c\,Av$, because $\sum_j A_{ij}(v_j + w_j) = \sum_j A_{ij}v_j + \sum_j A_{ij}w_j$ and $\sum_j A_{ij}(c v_j) = c\sum_j A_{ij}v_j$ (multiply out inside the sum; a common factor comes out of a sum). (Sections 1.18 and 4.2.)
- **Linear combination**: $c_1 M_1 + c_2 M_2 + \dots$ with numbers $c_j$. (Sections 4.2 and 4.15.)
- **Linear equation, system**: an equation of the form $c_1 y_1 + c_2 y_2 + \dots + c_n y_n = 0$ for unknown numbers $y_1, \dots, y_n$ with given coefficients $c_j$. (Section 5.16.)
- **Linear equations**: So $LX - XR = 0$ is a list of $nm$ linear equations for the $nm$ entries of $X$: in the equation $(r, c)$ the unknown $X_{kc}$ has the coefficient $L_{rk}$ and the unknown $X_{rk}$ the coefficient $-R_{kc}$. (Section 5.13.)
- **Linear expression**: A linear expression in some variables $p, q, \dots$ is a sum of the variables, each multiplied by a fixed number (or, below, a fixed matrix), its coefficient: $\alpha p + \beta q$ is linear, while $p^2$, $pq$ and $\sqrt{p^2 + q^2}$ are not. (Section 4.1.)
- **Linear history** $a_4 = A H x_4$ with a constant number $A$: then $a_4' = AH$ and $a_4'' = 0$, and the extra times shrink like $e^{-AHx_4}$: exponential deflation for $A > 0$. (Sections 3.8, 11.2 and 11.26.)
- **Linear member**: the history $a_4 = AHx_4 + a_0$ with a constant slope $A$. For $A > 0$ the extra times deflate as $e^{-AHx_4}$. (Sections 12.2, 12.19, 12.29, 17.2, 17.10, 20.10 and 20.15.)
- **Linear mixing**: Plain iteration: $x \leftarrow G(x)$; linear mixing: $x \leftarrow (1 - \beta)\,x + \beta\,G(x)$ with the mixing parameter $\beta$. (Sections 13.21, 13.24, 15.5 and 15.8.)
- **Linearly dependent**: We use one fact of linear algebra without proof (ASSUMED): more than $n$ vectors with $n$ components are linearly dependent, that is, some combination $c_1u_1 + c_2u_2 + \cdots$ with numbers $c_i$ not all 0 gives the zero vector. (Section 1.36.)
- **Linearly independent**: Multiplying from the left by $\gamma_A^T$ and taking the trace gives $\sum_B c_B\,\mathrm{tr}(\gamma_A^T\gamma_B) = 16\,c_A = 0$, so every coefficient is 0: the 256 products are linearly independent (no combination of them with coefficients not all zero gives the zero matrix). (Sections 4.13, 4.15, 5.11 and 8.6.)
- **Linearly independent matrices**: no one of them is a combination of the others. Writing each $16 \times 16$ matrix as one row of 256 numbers, $N$ matrices are independent when these $N$ rows have rank $N$. (Section 5.16.)
- **List**: `here.parents` lists the parent folder, its parent, and so on up to the top of the disk; `[here, *here.parents]` is the list (an ordered collection, written in square brackets) that starts with `here` and continues with all of them. (Sections 0.13, 0.20, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15, 21.23 and 22.12.)
- **List comprehension**: The line `different = [...]` is a list comprehension: it collects every package `p` whose installed version differs from its pinned version `v` (`!=` means "is not equal to"). (Sections 0.13, 1.9, 3.13, 4.8, 4.12, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 19.16, 20.11 and 22.23.)
- **Literal sum**: Brute force, literal sum: a computation that tries every case without any shortcut. (Section 11.18.)
- **Local**: What this theory proves is: the charge of each field obeys an exact local conservation law (it follows from an exact U(1) symmetry), so no process creates or destroys charge at any point inside a universe off its edge (at every point with $0 < z < \pi/2$, where the law is proved): charge can only flow from one place to another; the total charge $Q$ of a universe is constant only if no charge flows out through the edge $z = \pi/2$ of the hidden direction, and this no-flux condition is ASSUMED, not derived (whether a boundary condition at the edge supplies it is OPEN; Chapters 10, 18 and 21 show exact solutions through whose edge charge does flow, so that their total charge changes); the discrete symmetries of the theory are derived exactly (Chapter 21), among them its two charge conjugations, which are matrices, $\mathcal{C}_+ = C$ and $\mathcal{C}_- = \Gamma C$; and a T1 partner (mass $-m$, self-coupling $-\lambda$) carries the opposite charge, so a T1 pair $\{+m, -m\}$ has total charge zero as classical fields (for two universes that are quantised independently of each other there is no such cancellation; this is part of Q). (Sections 0.2, 14.26 and 21.22.)
- **Local conservation law**: The Revision record proves a local conservation law: for every solution of the field equation. (Sections 0.2, 5.6 and 10.2.)
- **Local density approximation**: The local density approximation (LDA) treats each small volume as a piece of uniform gas with the local density: $E_{xc}^{LDA}[n] = \int e_{xc}\big(n(\mathbf r)\big)\,d^3r, \qquad v_{xc}^{LDA}(\mathbf r) = \frac{de_{xc}}{dn}\Big|_{n(\mathbf r)}$. (Section 13.15.)
- **Local frame rotation**: Such a point-dependent turning of the frame is a local frame rotation (a rotation, or a boost when it mixes a space-like with a time-like direction; Chapter 5). (Section 6.2.)
- **Local-frame model**: the equation $i\,du/dx_4 = h(x_4)u$ in which the frame momenta change with $x_4$ as the history prescribes, while the hidden position is held fixed (section 4 of Notebook 08b). (Sections 8.25, 8.28 and 10.42.)
- **Log-log plot**: A log-log plot marks both axes in powers of ten, so the errors of a method of order $p$ lie on a straight line of slope $p$, and the order can be read off as a slope. (Sections 2.6 and 2.10.)
- **Log-sum-exp**: The solver solves $\ln(P + d_-) - \ln(H_l + d_+) = 0$ with $d_\pm = \max(\pm d, 0)$, adding each sum in the form $\ln\sum e^{t_i} = t_{max} + \ln\sum e^{t_i - t_{max}}$ (the log-sum-exp, which never overflows or underflows), by Newton's method in a bracket and then bisection down to neighbouring double-precision numbers (`Revision/kohn_sham/solver/src/mermin.rs`). (Section 15.26.)
- **Logarithm**: The logarithm $\log_{10} x$ is the power to which 10 must be raised to give $x$; for example $\log_{10} 1000 = 3$ and $\log_{10} 0.001 = -3$. (Sections 2.6 and 2.10.)
- **Logarithmic**: `ax.set_yscale("log")` makes the vertical axis logarithmic: equal distances on it mean equal factors (0.1, 1, 10, 100). (Sections 0.17, 4.12 and 19.21.)
- **Logarithmic axes**: The right panel draws the size of the errors (`np.abs`) against the width on logarithmic axes (`loglog`), one marker shape per centre, and a grey dashed reference line proportional to $w^2$, which on these axes is a straight line of slope 2. (Sections 7.9 and 16.12.)
- **Logarithmic axis**: an axis on which equal steps mean equal *factors* (1, 10, 100, ...) instead of equal differences; on it $e^{t}$ and $e^{-t}$ are straight lines. (Sections 0.16, 1.5, 1.8, 9.17 and 11.9.)
- **Logarithmic derivative** $\partial \ln s/\partial x = (\partial s/\partial x)/s$: the rate of growth of $s$ per unit of $x$, as a fraction of $s$ itself. (Sections 2.19 and 2.22.)
- **Logarithmic vertical axis**: `semilogy` draws with a logarithmic vertical axis: equal distances mean equal factors (each tick is ten times the one below). (Section 14.11.)
- **Long division**: the school method that produces the decimal digits of $p/q$ one after the other from the remainders. (Section 1.8.)
- **Long step**: A long step is one documented as longer than 5 minutes. (Section 23.2.)
- **Lovelock equations**: In eight dimensions the field equations of gravity that the author's theory uses are the Lovelock equations (Chapters 11 and 12). (Section 1.42.)
- **Lovelock scalar**: $L_{(1)}$ is the first Lovelock scalar: the Revision record builds the field equations from three curvature scalars $L_{(1)}, L_{(2)}, L_{(3)}$, made from products of one, two or three Riemann tensors with the generalized Kronecker delta of Chapter 1, and the first of them is exactly twice the Ricci scalar, $L_{(1)} = 2R$ (Chapter 11 treats all three). (Sections 3.30, 11.2, 11.11, 11.18 and 11.26.)
- **Lovelock scalars and tensors**: curvature quantities built from products of one, two or three Riemann tensors with the generalized Kronecker delta; the first Lovelock scalar is $L_{(1)} = 2R$ and the first Lovelock tensor is $P_{(1)} = -4G$. A later chapter treats them in full. (Section 3.29.)
- **Lovelock tensors**: combinations of the curvature of spacetime that enter the field equations of gravity in more than four dimensions; the Revision record computes three of them for the author's metric, with GKD as the weight of every term. (Sections 1.43, 1.47, 3.26, 11.2, 11.11, 11.18, 11.26, 12.2, 12.7, 12.15, 17.2 and 20.10; the opening of Chapter 11.)
- **Lower**: A pair of index lists is a lower list $(l_1, \dots, l_p)$ and an upper list $(u_1, \dots, u_p)$ of the same length. (Sections 11.2 and 11.8.)
- **Lower incomplete gamma function**: In the second substitute $u = Ky$ ($dy = du/K$, limits $0$ and $K$): $\int_0^1y^{K - 1}e^{-Ky}dy = \int_0^K(u/K)^{K - 1}e^{-u}du/K = K^{-K}\gamma(K, K)$, where $\gamma(s, x) = \int_0^xu^{s - 1}e^{-u}du$ is the lower incomplete gamma function. (Section 21.6.)
- **Lower index**: A second list of eight numbers that belongs to the same vector, $v_1, \dots, v_8$, carries a lower index; Section 1.27 says how one list is made from the other. (Section 1.26.)
- **Lowering**: So lowering an index keeps the four space-like components and changes the sign of the four time-like ones: for $v^a = (1, 2, \dots, 8)$, $v_a = (1, 2, 3, -4, -5, -6, -7, 8)$. (Sections 1.27 and 6.27.)
- **Lowering and raising**: $v_a = \eta_{ab} v^b$ and $v^a = \eta^{ab} v_b$. (Section 1.32.)
- **Lowest terms**: The spelling is in lowest terms when $p$ and $q$ have no common factor larger than 1. (Sections 1.2 and 1.8.)
- **LUMO**: HOMO, LUMO: the highest occupied and lowest unoccupied level; the KS gap is their difference. (Sections 13.35, 15.13, 16.11, 19.20 and 19.21.)

**M**

- **Machine epsilon** $\epsilon$: the gap between 1 and the next larger floating-point number, $\epsilon = 2^{-52} \approx 2.22 \times 10^{-16}$. (Sections 0.22, 0.24, 1.4, 1.8, 2.6, 2.10, 16.18, 16.20 and 16.23.)
- **Majorana**: A field equal to its own conjugate obeys $\Psi = M\Psi^\ast$; such a requirement is called a Majorana or reality condition, after the physicist who first used one. (Section 5.29.)
- **Majorana (reality) condition**: the requirement $\Psi^c = \Psi$. (Sections 5.32, 7.29, 7.32, 21.2 and 21.14.)
- **Majorana-type**: built with the transpose $\Theta^T$ instead of the Dirac adjoint (a Lagrangian of this kind is called Majorana-type, after the physicist Ettore Majorana, who studied real spinor fields). (Section 7.28.)
- **Majorana-type Lagrangian** $L_g$: the Lagrangian of the author's notebook, built with the transpose $\Theta^T$ of a real column instead of the Dirac adjoint $\bar\Psi = \Psi^\dagger C$. (Section 7.32.)
- **Majorana-type mass terms**: The simplest candidates are Majorana-type mass terms $\Psi^TM\Psi$ with a constant $16 \times 16$ matrix $M$, built from $\Psi$ twice and without $\Psi^\dagger$. (Section 21.32.)
- **Majorana-type term**: a term $\Psi^TM\Psi$ built from $\Psi$ twice, without $\Psi^\dagger$ (Section 21.32). (Sections 21.2 and 21.35.)
- **Manifest**: a file that lists other files with their fingerprints. (Sections 0.22, 0.24 and 15.13.)
- **Mantissa**: The caption quotes the count for $n = 16$ as computed, not typed: `f"{x:.1e}"` writes $16!$ as the text 2.1e+13, and `.split("e")` cuts it at the letter e into the mantissa 2.1 and the exponent +13 (both are still texts). (Section 1.25.)
- **Map**: a rule that turns a field $\Psi$ into a new field $\Psi'$. All maps of Chapter 18 are of the form $\Psi'(x) = M\Psi(x)$ with a constant $16 \times 16$ matrix $M$, possibly combined with a change of the coordinate $x_8$. (Sections 4.2 and 18.2.)
- **Map between solution sets**: a rule that takes EVERY solution of one theory to a solution of another theory (here: multiply the field by a fixed matrix, possibly together with a change of the coordinate $x_8$). (Section 20.2.)
- **Map between two sets of solutions**: This is a map between two sets of solutions. (Section 21.1.)
- **Maps between sets of solutions**: All of these are exact statements about maps between sets of solutions of the field equations. (Section 5.39.)
- **Maps between solution sets**: They are exact maps between solution sets: if a configuration of the field is a solution of the equations, its image under the map is a solution of the equations with the mapped parameters (for T1, of the equations with $(-m, -\lambda)$ in place of $(m, \lambda)$). (Sections 0.2 and 20.1.)
- **Margins**: The eight measured largest differences are below their tolerances by factors (margins) between 4.7 and 7692 (COMPUTED: `Revision/kohn_sham/reports/ks-rust-determinism.json`; the measured values are quoted by `Revision/kohn_sham/reports/ks-crosscheck.json`, key `rust_matrix_wide_uncertainties`). (Sections 0.22, 0.25, 16.12 and 19.17.)
- **Markdown cell**: A markdown cell holds text; a code cell holds Python code. (Section 0.7.)
- **Mask**: The same selection by hand, to draw it: `d1` and `d2` are the two differences of every level (numpy subtracts arrays entry by entry), `keep` is a mask, an array of truth values that is true where both differences exceed the floor (`&` combines two masks with "and"), and `energies` are the Richardson values of the kept levels (`array[keep]` keeps the entries where the mask is true). (Section 16.12.)
- **Mass** $m$: a number in the equations of a field; for a field that describes particles it is their mass (Chapter 7). (Sections 0.2, 2.27, 12.29, 20.15 and 21.14.)
- **Mass gap**: the energies $-m < \varepsilon < m$, where a free particle of mass $m$ has no level. (Sections 19.2 and 19.15.)
- **Mass reversed**: solves the field equation of the same form, either with the same $V$ (same mass) or with $-V$ (mass reversed). (Sections 5.28, 5.32 and 21.8.)
- **Mass shell** (or *dispersion relation*): the relation between $E$, the $k_a$ and the mass $m$ that a plane wave must obey. (Sections 4.3, 4.9 and 4.11.)
- **Mass term**: The mass term $-mS = -m\bar\Psi\Psi$ is linear in the mass $m$ (a real number) and quadratic in the field: every term contains one component of $\Psi^\dagger$ and one of $\Psi$. (Sections 7.19 and 18.4.)
- **matplotlib**: sympy: the Python package for exact algebra with symbols; numpy: arrays of numbers; matplotlib: plots. (Section 3.12.)
- **The matrices** $C$, $\Gamma$ **and** $B$: three fixed $16 \times 16$ matrices built from gamma matrices: $C$ is the product of the four space-like ones, $\Gamma$ (the chirality) the product of all eight, and $B$ the product of $C$ and the gamma matrix of the time $x_4$, times $-i$; $B$ enters the quantum theory (Chapter 5). (Sections 0.2, 0.14, 1.18, 1.24, 2.19, 4.2, 4.7, 4.19, 5.9, 5.28, 7.16, 10.9, 16.18, 18.8, 19.15, 21.8 and 21.14; the opening of Chapter 21.)
- **Matrix element** $\langle n|X|m\rangle$: for orbitals $\chi_n = (a_n, i b_n)$ the integral $\int \chi_n^\dagger X \chi_m\,dy$; for $X = \sigma_3$ it is $\int (a_n a_m - b_n b_m)\,dy$. (Sections 15.24 and 22.11.)
- **Matrix exponential**: for a square matrix $M$ the matrix $e^{Mx_4} = 1 + Mx_4 + \frac{1}{2}M^2x_4^2 + \dots$; the column $e^{Mx_4}\chi$ solves $\frac{d}{dx_4}\Phi = M\Phi$ with $\Phi(0) = \chi$. When $M^2 = k^2$ times the unit matrix, the series sums to $\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M$. (Sections 8.18, 9.18 and 9.24.)
- **Matrix identity**: *Line 5 (the matrix identity).* So $\partial_\mu(\cos z\,J^\mu) = -i\cos z\,(\Psi^\dagger CE - E^\dagger C\Psi)$ holds for every field as soon as the first part of line 1 equals line 4, that is (dividing by $-i$) as soon as the $16 \times 16$ matrix identity. (Section 21.17.)
- **Matrix product**: $(AB)_{ik} = \sum_j A_{ij} B_{jk}$: entry $(i, k)$ of $AB$ is row $i$ of $A$ times column $k$ of $B$, entry by entry, added up. (Sections 1.24 and 5.9.)
- **Matrix, entry, row, column**: a matrix is a rectangle of numbers; the number in row $i$ and column $j$ is the entry $M_{ij}$. (Section 11.8.)
- **Matter**: Matter is what stars, planets and we are made of: protons, neutrons and electrons. (Section 20.23.)
- **The matter-antimatter problem**: The matter-antimatter problem is the question why the universe contains baryons but essentially no antibaryons. (Section 21.3.)
- **Max|T|**: the largest absolute value of $\rho$, $p_3$, $p_t$ and $p_8$ of a state over the whole patch. We divide by it to compare states of very different size. (Sections 17.2 and 17.10.)
- **Mean field**: each electron feels the other one only through its average density; here an electron on a site feels $U$ times the density of the other label on that site, i.e. $U n_L/2$ on L and $U n_R/2$ on R. (Sections 13.24 and 19.2.)
- **Mean value theorem**: (by the mean value theorem of calculus, $g(\phi) - g(\omega) = (\phi - \omega)\, g'(\xi)$ for some $\xi$ between $\omega$ and $\phi$; applied to $g = \tan$, whose derivative is $1 + \tan^2$, it gives $\tan\phi - \tan\omega = (\phi - \omega)(1 + \tan^2\xi)$, and $1 + \tan^2\xi = 1 + \dots$ for small angles). (Section 2.24.)
- **Mean-field potential** $w(x)$: here the Hartree plus exchange potential, so that $v_s = v + w$. (Sections 13.32 and 13.35.)
- **Median**: The median is the middle value of the sorted list: `len(ratios) // 2` is the position of the middle (`//` divides and drops the remainder; with 39 ratios it is the 20th value, position 19 counting from 0). (Sections 14.18, 15.9 and 16.12.)
- **Mermin condition**: $N(\mu) = \sum_i g_i\,f(x_i) = N$, the equation that fixes $\mu$. (Sections 16.20 and 16.23.)
- **Meson**: Baryon: a particle made of three quarks, such as the proton $p = uud$ and the neutron $n = udd$ ($B = 1$); a meson (pion $\pi$) is a quark and an antiquark ($B = 0$). (Section 21.35.)
- **Metric**: the rule that turns a small step in the coordinates into its size. For the author's metric the rule is $ds^2 = g_{11} dx_1^2 + g_{22} dx_2^2 + \dots + g_{88} dx_8^2$, where $dx_i$ is the small step along $x_i$ and $g_{ii}$ is the $i$-th entry of the metric. (Sections 0.1, 0.14, 0.16, 1.1, 1.24, 1.32, 3.3, 3.12, 3.21, 3.29, 6.13, 7.26, 8.14, 11.2, 11.18, 12.2, 12.15, 14.10, 17.2 and 18.19.)
- **Metric function**: where $z = 6 H x_8$, $H > 0$ is a constant of the author, and $a_4$ is a function of the time $x_4$ alone, the metric function (its own field equations are the subject of Chapter 12). (Sections 0.14, 3.1 and 8.2.)
- **Metric product**: The metric product is $\eta(u, v) = \sum_a \eta_{aa}u_a v_a$; $u$ is a unit vector when $\eta(u, u) = +1$ or $-1$. (Sections 5.12 and 5.21.)
- **Metric, diagonal entries** $g_{aa}$: the eight numbers (functions of $x_4$ and $x_8$) that turn coordinate distances into true distances in the author's 8-dimensional world; positive for the space directions $x_1, x_2, x_3, x_8$ and negative for the time directions $x_4, x_5, x_6, x_7$. (Section 2.22.)
- **Milne wedge**: the part $t > |y|$ of the flat plane with one time $t$ and one space direction $y$, $ds^2 = -dt^2 + dy^2$, described by $\tau = \sqrt{t^2 - y^2}$ and $\theta$ with $t = \tau\cosh\theta$, $y = \tau\sinh\theta$; its metric is $ds^2 = -d\tau^2 + \tau^2 d\theta^2$. (Sections 6.23 and 6.27.)
- **Minimum**: For $T < \pi/\omega$ the bracket is positive, so $S_2 > 0$ and the action of $q + \epsilon\xi_1$ is $S_0 + S_2\epsilon^2$ with a positive $S_2$: the true path is a minimum along this shape. (Section 7.2.)
- **Minor**: Minor $M^{(rc)}$: the matrix left when row $r$ and column $c$ of $M$ are removed. (Sections 11.2 and 11.18.)
- **Mirror patch**: The map $z \to \pi - z$ takes it to the mirror patch $\pi/2 < z < \pi$. (Sections 18.2, 18.19, 18.26, 20.2 and 20.15.)
- **Mismatch**: 3. see where the "shot" lands at the right end: the mismatch $F(\lambda) = u(1; \lambda)$. (Section 2.12.)
- **Mixed**: $T^\mu{}_\nu$ has one of each and is called mixed. (Sections 2.18, 12.2 and 17.2.)
- **Mixed components**: Its components $\omega_\mu{}^a{}_b$, with the first frame index up, are called the mixed components. (Sections 6.4, 6.27 and 12.2.)
- **Mixed partial derivative**: $\partial^2 f/\partial x \partial y$, first with respect to $y$, then $x$ (or the other way round). Schwarz's theorem: for a function with continuous second derivatives the order does not matter. (Section 2.22.)
- **Mixed-product rule**: The mixed-product rule $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ holds. (Section 4.17.)
- **Mixing**: feeding only part of the change back (linear mixing) or a combination of several earlier passes (Anderson mixing) to make the loop converge. (Sections 13.35 and 15.8.)
- **Mode Hamiltonian** $h$: the $16 \times 16$ matrix with $E\,u = h\,u$ for the field $u\,e^{i(k\,x1 - E\,x4)}$ of one momentum; its eigenvalues are the energies of the fields of that momentum (section 8 of Notebook 05e derives it). (Sections 5.34, 5.37, 10.3, 10.25 and 10.42.)
- **Mode matrix** $h_k$: the $16 \times 16$ complex matrix with $E u = h_k u$. (Sections 8.17, 8.22 and 8.28.)
- **Mode operator** $h$: the field equation written as $i\,\partial_4\Psi = h\Psi$; for fields that depend only on $x_4$ and $x_8$ (and $U = 0$), $h = -im\gamma^{(4)} + i\gamma^{(4)}\gamma^{(8)}(\tan z\,\partial_8 + 3H)$. (Sections 8.32 and 8.35.)
- **Mode, occupation, pattern**: a fermion *mode* is a place that holds zero or one particle. With 16 modes a basis state is a *pattern* of 16 occupations (0 or 1); the computer stores it as a whole number $n$ whose binary digit $p$ is the occupation of mode $p$ ($p = 0, \dots, 15$). There are $2^{16} = 65536$ patterns. (Section 5.37.)
- **Module**: `import` loads a module (a part of Python or of a package) so that the code can use it; the text after `#` on each line is a comment. (Sections 0.13, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15 and 22.12.)
- **Modulus** $|z| = \sqrt{a^2 + b^2}$: the length of the arrow. (Sections 1.10 and 1.16.)
- **Moment equation**: A moment equation is a field equation multiplied by $e^{6Hy}$ and integrated over the patch. (Section 17.20.)
- **Moment** of a field equation: the equation multiplied by the volume weight $e^{6Hy}$ and integrated over the patch; it involves the source only through its weighted means $\bar\rho$, $\bar p_3$, $\bar p_t$, $\bar p_8$. (Sections 17.2, 17.17 and 17.20.)
- **Momenta**: The metric does not depend on the six transverse coordinates, so by Section 3.16 the six momenta $p_k = g_{kk}u^k$ (no sum) do not change during free fall: $p_i = h_i^2\,u^i, \qquad p_j = -h_j^2\,u^j \qquad\text{(both constant)}$. (Sections 3.31, 4.9 and 10.3.)
- **Momentum** $p_a = g_{aa} u^a$ (no sum) of a direction $x_a$. **Conserved**: the same number at every point of the path. (Sections 3.16, 3.34, 5.34, 5.37, 8.17, 10.9, 20.17, 20.20 and 20.22.)
- **Momentum weight**: The factor $e^{-Hy - a_4}$ is exactly the momentum weight $\kappa(y, x_4) = e^{-Hy - a_4(x_4)}$ (the Revision record's name for it; this $\kappa(y, x_4)$, always written in Chapter 3 with its two arguments, is a function and has nothing to do with the constant $\kappa$ of Einstein's equations in Section 3.26) that the Revision Kohn-Sham record uses to turn a conserved 3-space momentum into the momentum seen at height $y$ and time $x_4$ (`Revision/kohn_sham/ks-theory.json`, key `geometry.kappa`; PROVED here; Notebook 03d, In [5]). (Sections 3.31, 14.2 and 19.3.)
- **Monomial**: a product of different generators written in increasing order, such as $\theta_0 \theta_2 \theta_5$; the empty product is the number 1. (Sections 7.10, 7.16, 7.26, 11.18, 12.16, 18.19 and 18.20.)
- **Monotone (increasing)**: a function that grows whenever its argument grows. (Section 2.27.)
- **mpmath**: a Python package that computes with as many decimal digits as requested (here 50). (Sections 1.8 and 1.16.)
- **Multiple of the identity**: A number $c$ times a matrix multiplies every entry by $c$; $c I_n$ is called a multiple of the identity. (Section 4.2.)
- **Multiplicity**: The fundamental theorem of algebra (ASSUMED) says that a polynomial of degree $n$ has exactly $n$ roots $\lambda_1, \dots, \lambda_n$ when complex numbers are allowed and a repeated root is counted as often as it appears, its multiplicity. (Sections 1.34, 1.40, 4.9, 4.11, 4.19 and 5.3.)

**N**

- **Natural logarithm**: The exponential function $e^t$ is defined for every real $t$, is always positive and grows; its inverse is the natural logarithm $\ln x$, defined for $x > 0$: $\ln(e^t) = t$ and $e^{\ln x} = x$. (Sections 1.5 and 1.8.)
- **nbkit**: The book's tool nbkit (the file `Revision/textbook/tools/nbkit.py`) turns a builder into a notebook in two steps. (Section 0.9.)
- **nbkit check**: re-executing a notebook into a scratch folder and comparing the result byte for byte with the stored notebook, its files and its provenance file. (Sections 23.2 and 23.11.)
- **Negative branch**: Label $n$: the integer that numbers the levels of a sector: $n = 0$ is the band level (bound to the brane, occupied in the Fermi shell), $n = 1, 2, ...$ the bulk levels above it (empty), $n = -1, -2, ...$ the levels of negative energy, the negative branch (in the record's convention the normal-ordered sea, not populated). (Sections 22.2 and 22.11.)
- **Negative control**: a deliberately changed case in which the effect must NOT occur (or must occur differently); it shows that a check can fail and that the result depends on the feature that was changed. (Sections 0.22, 1.50, 6.1, 6.13, 7.28, 7.32, 9.26, 9.29, 18.2, 18.13, 18.19, 19.2, 19.20, 20.11, 21.15, 21.17 and 22.3.)
- **Neutral subspace**: a subspace on which $u^\dagger B v = 0$ for all $u, v$ in it. (Section 10.9.)
- **Newton's method**: replace a function by its tangent line at the current guess and take the zero of that line as the next guess. (Sections 2.27, 15.8, 16.20 and 16.23.)
- **Nilpotent**: For a light-like $v \neq 0$, $\gamma(v)$ is not the zero matrix, because $\mathrm{tr}(\gamma(v)\gamma^b) = v_a\,\mathrm{tr}(\gamma^a\gamma^b) = 16\,v_a\eta^{ab} = 16\,v^b$ (the third contraction of Section 1.28; raising the index) is not 0 for a component $v^b \neq 0$; but $\gamma(v)^2 = 0$: a matrix with a power equal to 0 is called nilpotent, and all its eigenvalues are 0 ($\lambda^2v = \gamma(v)^2v = 0$ gives $\lambda = 0$); its characteristic polynomial is $\lambda^{16}$. (Sections 1.37 and 8.10.)
- **Nilpotent matrix**: a matrix $N \neq 0$ with $N^k = 0$ for some power $k$; all its eigenvalues are 0. (Section 1.40.)
- **No-boundary proposal**: a proposed boundary condition (J. B. Hartle and S. W. Hawking) that picks one solution of the Wheeler-DeWitt equation. It is named in Chapter 22, not used, and is not formulated for this 8-dimensional theory. (Sections 22.2 and 22.4.)
- **No-flux condition**: the condition that no charge flows through the edge $z = \pi/2$ of the hidden direction (the brane). The local conservation law is proved at every point with $0 < z < \pi/2$; the no-flux condition is ASSUMED, not derived, and only under it is the total charge of a universe constant. Exact solutions exist through whose edge charge does flow, so that their total charge changes. (Sections 0.2, 5.6, 5.39, 18.21, 20.22, 21.1 and 21.17.)
- **No-flux condition at the brane**: the condition $\sqrt{|g|}J^{x_8} = 0$ at $z = \pi/2$ (for the homogeneous solutions, $q_8 = 0$): no charge flows out through the brane. Only under it is the total charge of a universe constant. It is ASSUMED wherever it is used, not derived; it holds for some exact solutions and fails for others (Notebook 18c), and whether the junction condition at the brane implies it is OPEN. (Section 18.28.)
- **Node**: a point where the eigenfunction changes sign. (Sections 2.16, 2.17, 2.24, 16.14 and 16.18.)
- **Noether identity**: On every solution of the field equation the tensor is conserved: this is a theorem, proved in the record from the invariance of the action under a change of coordinates (the Noether identity; PROVED, see the table below). (Section 9.9.)
- **Noether's construction**: This is Noether's construction. (Section 21.16.)
- **Noether's theorem**: a continuous symmetry of the Lagrangian gives a current whose divergence vanishes on every solution (Section 21.16). (Sections 21.2 and 21.22.)
- **Non-characteristic**: So the time derivative of every component is fixed by the field and its derivatives along the other seven directions at the same time $x_4$: the slices $x_4 = $ const are non-characteristic (PROVED; Notebook 07b, In [19]; Wolfram checks `evolution_form_G` and `evolution_form_C`). (Sections 7.22 and 8.16.)
- **Non-interacting $v$-representability**: The Kohn-Sham scheme ASSUMES that the density of interest is the ground-state density of some non-interacting system in some potential $v_s$ (non-interacting $v$-representability). (Section 13.10.)
- **Non-trivial**: The author asked that the Lagrangians of both fields be non-trivial: their Euler-Lagrange equations must always contain nonzero contributions from gravity through the canonical spin connection, unless space-time is flat 4+4 space ([1] for dirac16complex, [2] for dirac16complex00), and must be self-consistent. (Section 7.23.)
- **Nondegenerate**: Such a form is called nondegenerate on the eigenspace: its Gram matrix has no zero eigenvalue. (Section 10.5.)
- **Nonlinear**: They look like one-particle equations, but $\hat F$ contains the unknown orbitals: they are nonlinear and are solved by iteration, starting from a guess and repeating until nothing changes any more (self-consistency, Section 13.21). (Section 13.6.)
- **Norm** of a field in the hidden direction: $\int \cos z\,\Psi^\dagger\Psi\,dx_8$ ($\cos z = \sqrt{|g|}$ is the volume factor). It is *finite* when the integral does not diverge at the ends. (Sections 8.16 and 8.35.)
- **Normal ordering**: writing every product with the annihilators to the right, by definition dropping the constant that the reordering produces (here $-8E$ for the energy). The normal-ordered value of an operator $X$ in a state is its value minus the vacuum value. (Sections 5.34, 5.37, 10.20, 10.25 and 14.30.)
- **Normal random numbers**: random numbers whose histogram is the bell curve $e^{-x^2/2}/\sqrt{2\pi}$; numpy's `normal` draws them. (Sections 1.25, 1.27 and 1.32.)
- **Normal-ordered**: After canonical quantisation (Chapter 10; the field becomes an operator, a rule that acts on the quantum states) the tensor becomes an operator too: every bilinear is replaced by the normal-ordered product of the quantised field (the product rearranged so that the operators that remove a particle stand to the right of those that create one, which gives the empty state the energy zero; Chapter 10 defines it exactly), $\hat T^\nu{}_\mu = {:}T^\nu{}_\mu[\hat\Psi, \hat{\bar\Psi}]{:}$, and the numbers are expectation values (the average value that measurements of the operator give in a given quantum state) (record `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 12). (Section 9.13.)
- **Normal-ordered energy**: the energy of a state minus the energy of the vacuum (the filled sea), as in the third notebook of Chapter 10. (Section 10.48.)
- **Normal-ordered square**: Its normal-ordered square puts all creation operators to the left: ${:}S^2{:} = \sum V_{pq}V_{rs}\,a_p^\dagger a_r^\dagger a_s a_q$. (Section 13.4.)
- **Normalisation**: multiplying an orbital by a number so that $\int_{-L}^{0} (a^2 + b^2)\,dy = 1$. (Section 15.8.)
- **Normalised**: The function $u$ is the wave function: $u(x)^2$ is the probability density of finding the particle at $x$, so $u$ is normalised, $\int u^2\, dx = 1$. (Sections 2.13, 10.11, 10.14, 13.2 and 22.12.)
- **Normalised Lovelock tensor**: Normalised Lovelock tensor $E_{(k)} = -P_{(k)}/2^{k+1}$; $E_{(1)}$ is the Einstein tensor. (Sections 11.2 and 11.26.)
- **NOT COMPUTED**: a label used next to the five status labels in Chapters 20 and 21: no computation of the quantity exists in the Revision record or in this book (for example the rate of a process that violates C or CP). (Sections 20.23, 21.1, 21.2, 21.4, 21.31, 21.36 and 21.38.)
- **Nucleus**: A photon of energy $E_\gamma$ that hits a nucleus (the heavy centre of an atom) of mass $M$ at rest can make an electron-positron pair, the nucleus remaining in the final state, only if $E_\gamma \ge 2m(1 + m/M)$. (Sections 20.17 and 20.20.)
- **Null**: A vector $v \neq 0$ is space-like if $Q(v) > 0$, time-like if $Q(v) < 0$ and light-like (or null) if $Q(v) = 0$. (Sections 1.27, 1.32, 3.4 and 5.12.)
- **Null combination** $\rho + p_8$: the energy density plus the pressure along $x_8$. (Sections 20.2, 20.10 and 20.15.)
- **Null energy condition** (NEC) along $x_8$: $\rho + p_8 \ge 0$. Ordinary matter satisfies it; a source with $w < -1$ and $\rho > 0$ (called *phantom*) violates it. (Sections 3.26, 12.2, 12.15, 12.19 and 22.2.)
- **Null lines**: The right picture draws the two hyperbola branches and the two dotted null lines $v_4 = \pm v_1$, on which $v_1^2 - v_4^2 = 0$. (Section 5.22.)
- **Null space**: The columns $v$ with $Av = -i\omega v$ are the solutions of $(A + i\omega)v = 0$, the null space of $A + i\omega$. (Sections 9.30 and 20.16.)
- **Null vector**: a direction of zero length, such as the frame direction $x_4 + x_8$ (time-like plus space-like). (Sections 12.2 and 12.11.)
- **Number density**: (Check gas_densities.) The three densities that matter are the number density (the U(1) charge density, whose integral counts the quanta), the scalar density and a third density $Q$ (the formula is displayed in that section). (Section 19.4.)
- **Number operator**: The number operator $\hat n_p = a_p^\dagger a_p$ gives $n_p$, and $\hat N = \sum_p \hat n_p$ counts the particles of a state. (Sections 10.11 and 13.4.)
- **The numerical parameters** (parameters.json, numerics): $G = 900$ steps of the Runge-Kutta method on $[-L, 0]$, a root tolerance of $10^{-13}\,m$ for each level, a self-consistency tolerance of $10^{-11}\,m$ with at most 400 iterations, Anderson mixing with depth 6 and $\beta = 0.4$, the step $\delta = 0.002$ in $a_4$ for derivatives along the history, and levels closer than $10^{-9}\,m$ count as equal (one degenerate group). (Section 15.2.)
- **Numerics**: The cross-check is a test of the numerics: of the discretisation, the rounding and the programming of the Rust solver, against a second program that differs in all three. (Section 16.25.)
- **numpy**: sympy: the Python package for exact algebra with symbols; numpy: arrays of numbers; matplotlib: plots. (Sections 3.12, 10.9 and 20.11.)

**O**

- **O(4,4)**: the real $8 \times 8$ matrices $\Lambda$ with $\Lambda^T\eta\Lambda = \eta$ (they keep the metric product); SO(4,4): those with determinant $+1$. (Sections 5.12 and 5.26.)
- **O(4,4), SO(4,4)**: the real $8 \times 8$ matrices $\Lambda$ with $\Lambda^T\eta \Lambda = \eta$ (they keep the metric product); SO(4,4): those with determinant $+1$. (Section 5.21.)
- **Observer**: Observer: someone who, like us, measures only the three space directions $x_1, x_2, x_3$ and the time $x_4$. (Section 22.22.)
- **Occupation**: Level $\varepsilon$: an allowed energy of the one-particle equation; occupation $f$: how many particles sit in an orbital of that level ($0$ to $1$); degeneracy $g$: how many orbitals share the level. (Sections 10.18, 19.2 and 19.20.)
- **Occupation numbers**: A determinant built from some of them is fixed, up to its sign, by the occupation numbers $n_p \in \{0, 1\}$, $n_p = 1$ when $\phi_p$ is used. (Section 13.4.)
- **Occupation-number state** $|n_0 n_1 n_2 n_3\rangle$: the determinant that uses the orbitals $p$ with $n_p = 1$; there are $2^4 = 16$ of them for four orbitals. (Section 13.13.)
- **Occupied**: A level is occupied if particles sit in it ($f = 1$) and empty if not ($f = 0$). (Section 15.13.)
- **Odd**: The doubled problem is therefore mirror-symmetric only if the mass is odd across the brane. (Sections 1.19, 2.13, 2.16, 4.13, 4.15, 5.5, 5.12, 5.16, 7.11, 7.16, 11.2, 11.8, 14.12, 16.18 and 19.11.)
- **Off shell**: A configuration that satisfies the field equation is said to be on shell; one that need not satisfy it is off shell. (Sections 9.2, 9.16, 18.2, 20.2 and 20.10.)
- **Off-diagonal**: Besides these 27 nonzero diagonal components there are 12 nonzero off-diagonal ones. (Section 12.5.)
- **On shell**: on solutions of the field equation. (Sections 7.26, 9.2, 9.16, 18.2, 20.2 and 20.10.)
- **One momentum**: A field of one momentum $k$ along $x1$ is a field of the form $\Psi = \psi\,e^{ik\,x1}$: a column $\psi$ (which may still depend on the time) times the number $e^{ik\,x1} = \cos(k\,x1) + i\sin(k\,x1)$, which goes once around the circle of complex numbers of size 1 each time $x1$ grows by $2\pi/k$. (Section 5.34.)
- **One-body density matrix**: Both formulas are summarised by the one-body density matrix $\rho = \sum_{a\in O}|\phi_a\rangle\langle\phi_a|$, whose matrix elements are $\rho_{qp} = \langle a_p^\dagger a_q\rangle$: $\langle a_p^\dagger a_q\rangle = \rho_{qp}, \qquad \langle a_p^\dagger a_q^\dagger a_s a_r\rangle = \rho_{rp}\,\rho_{sq} - \rho_{sp}\,\rho_{rq}$. (Section 13.4.)
- **One-body matrix**: The $16 \times 16$ matrix $\rho$ is the one-body matrix of the state. (Section 14.26.)
- **One-particle Hamiltonian** $h_m(k)$: the $16 \times 16$ matrix that gives the time evolution $i\,\partial_4 u = h_m(k)u$ of a plane wave $u\,e^{ik\cdot x}$ in flat 4+4 space; its eigenvalues are the frequencies $\pm w$. (Sections 21.26 and 21.29.)
- **One-particle matrix**: The frequencies $w$ are the eigenvalues of the one-particle matrix $h_m(k)$. (Section 18.22.)
- **One-sided fourth-order difference**: At the last slice there are no neighbours on the right, so the derivative uses the one-sided fourth-order difference $f'(x) \approx [3f(x - 4h) - 16f(x - 3h) + 36f(x - 2h) - 48f(x - h) + 25f(x)]/(12h)$, the same stencil as the record; `w_mix[-5]` is the fifth entry from the end. (Section 22.23.)
- **One-step value**: The one-step value $r(h)$ has no $h^2$ error left; its error starts with $h^4$. (Section 16.5.)
- **Onset**: So along the history (where $X$ grows with the time) $E^2$ crosses zero exactly once and stays negative afterwards; the moment of the crossing is the onset. (Sections 8.24 and 8.28.)
- **Onset time** $x_4^\ast$: the time at which $w^2$ changes from positive (the wave oscillates) to negative (the wave grows). (Sections 10.39 and 10.42.)
- **OPEN**: a status label: a question that neither the Revision record nor this book answers; it is not settled. Example: whether the big bang creates universes in pairs is, as a question of this book, OPEN: it is not proved. (Sections 0.3, 0.20, 3.1, 3.31, 8.1, 12.31, 15.31 and 22.27.)
- **Open problem**: a question that neither the Revision record nor this book answers, put precisely enough that one can recognise an answer. (Section 22.2.)
- **Open shell**: a degenerate group of levels only partly filled. (Sections 15.4 and 15.24.)
- **Operator**: a rule that turns a state into another state, here a big matrix that acts on columns of numbers. Operators are multiplied by doing one after the other; the order matters. (Sections 5.34, 5.37, 9.13, 10.11, 10.18, 13.2, 21.25 and 21.29.)
- **Orbifold**: The Revision theory ASSUMES a Z2 mirror (also called an orbifold): the patch $y \le 0$ is glued at $y = 0$ to a mirror copy of itself, with the warp $e^{-H|y|}$ on both sides, and a field on the doubled interval obeys $\Psi(-y) = \pm\gamma^{(x_8)}\Psi(y)$. (Sections 14.12 and 22.2.)
- **Orbital**: a single-particle state of the Kohn-Sham model. Here it is described by two real functions $a(y)$ and $b(y)$, its *components*. (Sections 2.1, 2.27, 13.3, 13.13, 13.35, 14.1, 14.12, 14.17, 14.24, 15.8, 16.18, 17.2, 19.2, 19.15, 19.20 and 22.2.)
- **Orbital relaxation**: At $\tau = 0$ the integrand is $\Delta_{KS}$; the difference $\Delta_{SCF} - \Delta_{KS}$ measures how much the levels move when the particle is transferred (the orbital relaxation). (Sections 13.27 and 15.5.)
- **Order** $p$: a method has order $p$ when its error at a fixed end time is close to $C h^p$ for small $h$, with a number $C$ that does not depend on $h$. Halving $h$ then divides the error by $2^p$. (Sections 2.6, 2.10, 11.2, 11.11 and 18.27.)
- **Order of accuracy**: Its order of accuracy $p$: its error falls like $h^p$ when the step $h$ shrinks. (Sections 17.2 and 17.20.)
- **Order of convergence**: the power $q$ in an error $\approx C h^q$; the reference has $q = 2$. (Sections 7.8, 16.4 and 16.18.)
- **An ordinary differential equation**: An ordinary differential equation (ODE) is an equation of the form. (Sections 2.2, 2.10, 12.21, 12.24, 15.8 and 18.26.)
- **Orthogonal**: two functions with $\int u_m u_n\,dx = 0$. (Sections 1.28, 2.13, 2.16, 4.2, 4.19, 7.29 and 13.2.)
- **Orthogonal matrix**: a real matrix $O$ with $O^T O = I$, so $O^T = O^{-1}$. (Sections 1.32, 1.40 and 4.15.)
- **Orthogonal projection**: So the closest flat profile is the weighted mean $\bar X$ of Section 17.7; it is called the orthogonal projection of $X$ on the flat functions. (Section 17.17.)
- **Orthonormal basis**: `eigenspace` returns, as columns, all right singular vectors of $h_k - \lambda I$ whose singular value is below $10^{-9}$: an orthonormal basis (columns of length 1, perpendicular to each other) of the eigenspace of $\lambda$. (Section 8.23.)
- **Orthonormal columns**: columns of length 1 with $u^\dagger v = 0$ for any two different ones. (Section 4.11.)
- **Orthonormal** columns: each has length 1 ($u^\dagger u = 1$) and every two are perpendicular ($u^\dagger w = 0$). (Sections 4.9, 5.34, 5.37, 10.10, 10.25, 13.2 and 22.6.)
- **Oscillation and growth**: $e^{-iEx_4}$ oscillates (its size stays 1) when $E$ is real; when $E = \pm i\kappa$ with $\kappa > 0$ it is $e^{\pm\kappa x_4}$, which grows or decays exponentially. (Section 8.22.)
- **Oscillator**: For the oscillator, a particle of mass 1 on a spring, it is the kinetic energy minus the potential energy: $L(q, \dot q) = \tfrac12\dot q^2 - \tfrac12\omega^2 q^2$. (Section 7.2.)
- **Out of equilibrium**: An asymmetry can only be made while the universe is out of equilibrium, for example in decays that happen too late for the inverse processes to keep up. (Section 21.5.)
- **Outer**: Mathematica's name for the operation that builds that matrix, `Outer[delta, lower, upper]`. The author's function is called `k\[Delta]` (Mathematica's plain-text spelling of "k" followed by the Greek letter delta). (Section 1.47.)
- **Outer[delta, lower, upper]**: the author's Mathematica name for the $p \times p$ matrix with the entries $M_{ij} = \delta(l_i, u_j)$: row $i$ belongs to the lower label $l_i$, column $j$ to the upper label $u_j$. (Section 11.8.)

**P**

- **Package**: a collection of Python code that someone else wrote and that we *import* (load) to use it: numpy (arrays of numbers and matrices), sympy (exact algebra and calculus with symbols), mpmath (numbers with as many digits as we want), matplotlib (plots). (Section 0.12.)
- **Pair**: a solution together with one partner. (Sections 7.12, 11.2, 11.8, 20.2 and 20.10.)
- **Pair creation of particles**: This is the pair creation of particles, an observed process of ordinary physics, in which the total electric charge stays the same because the two members carry opposite charges. (Section 21.3.)
- **Pair curvature**: Pair curvature $K_{ab} = R^{ab}{}_{ab}$ (no sum): the curvature of the plane spanned by the directions $a$ and $b$ (a name used in Chapter 12). (Sections 12.2 and 12.5.)
- **Paired**: Two universes are paired when an explicit invertible rule takes every solution of the theory with mass $m$ to a solution of the theory with mass $-m$, and takes its Lagrangian, its energy-momentum tensor and its current to stated multiples of those of the partner. (Section 18.1.)
- **Pairwise summation**: `np.sum` adds in pairs, then pairs of pairs, and so on (pairwise summation). (Section 0.25.)
- **Panel**: `draw_signs` draws one matrix into one panel `ax` (a pair of axes) of a figure. (Section 4.8.)
- **Parabola**: Two wrong paths with the same end values are the line $q = t$ and the parabola $q = t^2$. (Section 7.2.)
- **Parallel transport** along a curve $x^a(t)$: carrying a vector so that its covariant derivative along the curve is zero, $dV^a/dt + \sum_{b,c} \Gamma^a{}_{bc}\, (dx^b/dt)\, V^c = 0$ ("not turning"). (Section 3.21.)
- **Parallel transported**: A vector is parallel transported along the curve when $DV^a/d\lambda = 0$: it is carried along without turning. (Section 3.16.)
- **Parameter set** $(m, \lambda)$: the mass and the coupling of the potential $U(S) = \frac{\lambda}{2}S^2$. The theory with $(m, \lambda)$ and the theory with $(-m, -\lambda)$ are two DIFFERENT theories: their Lagrangians are different functions of the field. (Section 20.2.)
- **Parameters**: the mass $m$ and the coupling $\lambda$ of the potential $U(S) = \frac{\lambda}{2}S^2$. The theory with the parameters $(m, \lambda)$ and the theory with $(-m, -\lambda)$ are two DIFFERENT theories: their Lagrangians are different functions of the field. (Sections 3.13 and 18.2.)
- **Parity**: the condition at the brane $y = 0$: even $b(0) = 0$, odd $a(0) = 0$ (the ASSUMED $Z_2$ brane). (Sections 14.12, 15.2, 16.18 and 21.24.)
- **Partial derivative** $\partial f/\partial x$: the ordinary derivative with respect to $x$ while all the other variables are held fixed. We also write $\partial_x f$, and for the author's coordinates $\partial_4 = \partial/\partial x_4$ and $\partial_8 = \partial/\partial x_8$. (Sections 2.1, 2.18, 2.22, 3.2 and 7.2.)
- **Partial sum**: A series is an endless sum $t_0 + t_1 + t_2 + \cdots$; its partial sum $S_N = t_0 + \dots + t_N$ adds the terms up to number $N$, and the series converges to a number $S$ when the error $|S_N - S|$ becomes as small as we like for large $N$. (Sections 1.11 and 1.16.)
- **Particle**: A particle $b_s^*|0\rangle$ and an antiparticle $d_s^*|0\rangle$ (a hole in the filled sea) both have the energy $+E > 0$. (Sections 10.20, 10.25, 13.27, 14.21 and 16.13.)
- **Particle and antiparticle operators**: $b_s = f_{s-1}$ for $s = 1, \dots, 8$ (modes 0 to 7) and $d_s = f_{s+7}$ (modes 8 to 15). (Section 5.37.)
- **Particle branch, sea**: by a CONVENTION of the Revision theory, the levels that are positive in the free problem (and the $k = 0$ zero modes) are particle levels; the negative branch is the filled, normal-ordered sea. (Section 14.24.)
- **Partner**: the image of a state under the map of theorem T3. (Sections 19.2, 19.20 and 20.2.)
- **Partner block**: So $\Gamma v$ lies in the block $(-j, s_2, s_3)$: the partner block, with the opposite type and the same $s_2$, $s_3$ (check blocks_relation_to_Gamma). (Section 19.5.)
- **PASS line**: a printed line that says a check passed; "reproduces" names the Revision record (report file and check name) that found the same result. (Section 12.15.)
- **Patch**: the range $0 < z < \pi/2$ on which the metric is used. (Sections 0.14, 3.5, 3.12, 12.2, 17.2, 18.2, 18.19, 18.26, 20.2, 20.15 and 21.2.)
- **Patch and mirror patch**: the author's metric is used on $0 < z < \pi/2$ (the patch). The map $z \to \pi - z$ carries it onto $\pi/2 < z < \pi$ (the mirror patch). (Section 20.10.)
- **Patch end**: Its end $z = \pi/2$ is the patch end; the end $z \to 0$ is the tip. (Sections 3.5, 3.12, 3.34, 8.2, 8.31, 10.27 and 10.31.)
- **Path** (or motion): a function $q(t)$ that gives the position $q$ of a particle on a line at every time $t$ between a start time and an end time. Here the times run from $0$ to $T$. (Sections 7.2 and 7.8.)
- **Path integral**: a way to compute a quantum amplitude by adding one contribution for every possible history of the fields. It is named in the list of what is NOT established (Section 18.28) and not used. (Section 18.2.)
- **Pattern**: With $n$ modes a basic state is a pattern of $n$ occupations, each 0 or 1, so there are $2^n$ patterns; all combinations of them form the Fock space. (Sections 1.48, 5.34, 10.11, 10.25 and 12.25.)
- **Pattern as a whole number**: the program stores a pattern as one whole number $n$ whose binary digit number $p$ (counted from 0) is the occupation of mode $p$; the program reads that digit by shifting $n$ to the right by $p$ binary places and keeping the last binary digit. (Section 10.18.)
- **Pauli**: (ii) Pauli: if two orbitals are equal, $\phi_a = \phi_b$ with $a \ne b$, the columns $a$ and $b$ of the table are equal; the transposed table then has two equal rows, so its determinant is 0 (rule 4), and the determinant of the table is the same number (rule 2): $\Phi = 0$. (Section 13.3.)
- **Pauli matrices** $\sigma_1, \sigma_2, \sigma_3$: the three $2 \times 2$ matrices $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$. (Sections 4.3, 14.1, 14.10, 19.15 and 19.20.)
- **Pauli principle**: This is the Pauli principle, and it follows from the anticommutator alone. (Section 10.11.)
- **pdflatex**, for the six documents of the Revision record and for the book's PDF: on Windows MiKTeX (https://miktex.org), on macOS MacTeX (https://tug.org/mactex), on Linux the TeX Live packages of your distribution. (Section 23.3.)
- **Perfect fluid (at rest)**: matter whose energy-momentum tensor is diagonal, with the energy density and the pressures on the diagonal. (Section 9.29.)
- **Perfect fluid at rest**: That does not yet make it a perfect fluid at rest, which has a diagonal energy-momentum tensor: Section 9.12 showed that the spin connection puts entries off the diagonal. (Section 9.26.)
- **Period**: The length of the repeating block is the period; for $1/7$ it is 6. (Sections 1.2 and 1.8.)
- **Period-doubling bifurcation**: This splitting of one fixed point into a cycle of period 2 is called a period-doubling bifurcation. (Section 13.25.)
- **Periodic box**: Put the gas in a cube of side $\ell$ and volume $V = \ell^3$ whose opposite faces are glued together (a periodic box). (Section 13.15.)
- **Permutation**: a re-ordering of the numbers $0, 1, \dots, n-1$ (or of any $n$ different objects). There are $n! = 1 \cdot 2 \cdots n$ of them. (Sections 1.19, 1.24, 1.47, 11.2 and 11.8.)
- **Permutation matrix**: the matrix with exactly one 1 in every row and every column and 0 elsewhere; row $i$ has its 1 in column $\sigma(i)$ for a permutation $\sigma$. (Sections 1.19 and 1.24.)
- **Permutation sign** (Mathematica's *Signature*): for a list of different numbers, $+1$ if the number of *inversions* (pairs of positions in which the larger number stands first) is even, $-1$ if it is odd; for a list with a repeated number, 0. (Sections 4.2, 4.7 and 18.9.)
- **Perpendicular** (orthogonal) vectors: $u^T w = \sum_i u_i w_i = 0$. (Sections 1.36 and 1.40.)
- **Phantom**: | $-2 < x < -1$ | $w < -1$ (called phantom) | $2 + x > 0$, and $x < -(2 + x)$ means $x < -1$ |. (Sections 9.19, 12.2, 22.2, 22.16 and 22.22.)
- **Phase**: a complex number $e^{i\alpha} = \cos\alpha + i\sin\alpha$ of modulus 1. (Section 21.22.)
- **Phase angle**: Every complex number $z \neq 0$ can be written as $z = r e^{i\varphi}$ with $r = |z|$ and a real angle $\varphi$, its argument (or phase angle): the point $(a/r, b/r)$ lies on the unit circle, so it is $(\cos\varphi, \sin\varphi)$ for some angle $\varphi$ (school trigonometry, ASSUMED), and then $z = r(\cos\varphi + i\sin\varphi) = re^{i\varphi}$. (Sections 1.11 and 1.16.)
- **Phase factor**: So $\lambda 1$ gives $-|\lambda|^2B$, which is never $B$ (that would need $(1 + |\lambda|^2)B = 0$), and $\lambda\Gamma$ gives $|\lambda|^2B$, which is $B$ exactly when $|\lambda| = 1$, that is when $\lambda = e^{i\alpha}$ is a phase factor (a complex number of size 1). (Section 5.34.)
- **Phase function** $\Phi(\varepsilon)$: $j$ times the Pruefer angle at the brane. It increases strictly with $\varepsilon$. (Section 15.8.)
- **Phase portrait**: the curve traced by the point $(x, v)$ (position, velocity) as time goes on. (Section 2.10.)
- **Photon**: the particle of light (Chapter 21). (Sections 0.2, 20.17 and 20.20.)
- **Pigeonhole principle**: if more than $n$ objects are put into $n$ boxes, some box gets at least two of them. (Sections 1.43, 1.47, 11.2 and 11.8.)
- **Pin(4,4)**: all products $\gamma(u_1)\cdots\gamma(u_k)$ of unit vectors; Spin(4,4): those with an even number $k$ of factors. (Sections 5.12, 5.21, 5.26, 18.2 and 18.8.)
- **Pinned**: The nine packages are installed with Python's installer pip at fixed (pinned) versions, the versions with which the book was built: numpy 2.4.6 (arrays of numbers, matrices), sympy 1.14.0 (exact algebra and calculus with symbols), mpmath 1.3.0 (numbers with as many digits as we ask for), matplotlib 3.11.0 (plots), and jupyterlab 4.4.10, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0 and nbconvert 7.16.6 (the programs that show, store and run notebooks). (Section 0.8.)
- **Pinned version**: the exact version of a package with which the book was built. Another version may print slightly different numbers or pictures. (Section 0.12.)
- **Pivots**: Write $T - x\,\mathbb{1}$ (where $\mathbb{1}$ is the unit matrix) as a product $\mathcal{L} D \mathcal{L}^T$, with $\mathcal{L}$ (a script letter, because $L$ is the length 3 of the interval) having ones on its diagonal and one band below it, and $D$ diagonal with entries $q_1, \dots, q_n$, the pivots. (Section 16.15.)
- **Plain iteration**: $x \leftarrow G(x)$; linear mixing: $x \leftarrow (1 - \beta)\,x + \beta\,G(x)$ with the mixing parameter $\beta$. (Sections 13.21 and 13.24.)
- **Plane curvature**: Christoffel symbol $\Gamma^a{}_{bc}$, Riemann tensor $R^a{}_{bcd}$ and $R^{ab}{}_{cd} = g^{bb}R^a{}_{bcd}$, plane curvature $K(a, b) = R^{ab}{}_{ab}$ (no sum), Ricci tensor $R^h{}_j = \sum_c R^{hc}{}_{jc}$, Ricci scalar $R = \sum_h R^h{}_h$, Einstein tensor $G^h{}_j = R^h{}_j - \frac12\delta^h_jR$: Chapter 3 (Sections 3.15 and 3.17) defines them. (Section 11.2.)
- **Plane wave**: a solution of the form $u\, e^{i(k \cdot x - E x_4)}$, with a constant column $u$; $E$ is its *energy* (frequency in the time $x_4$) and the $k_a$ are its *momenta* (wave numbers in the other directions). (Sections 4.9, 4.11, 7.5, 7.8, 8.17, 8.22, 9.21, 10.3, 10.9, 13.15 and 13.19.)
- **PNG**: PNG is the file format in which the figures are saved. (Section 0.12.)
- **Polar coordinates**: Polar coordinates of the plane: the distance $r$ from the origin and the angle $\varphi$ from the horizontal axis; $x = r\cos\varphi$, $y = r\sin\varphi$. (Section 3.21.)
- **Polar form**: $z = r e^{i\varphi}$ with $r = |z|$ and $\varphi$ the argument. (Section 1.16.)
- **Polarisation**: With the polarisation $\zeta = (n_\uparrow - n_\downarrow)/n$, so $n_\uparrow = \tfrac{n}{2}(1 + \zeta)$ and $n_\downarrow = \tfrac{n}{2}(1 - \zeta)$: one label alone ($g = 1$) has the kinetic energy $\tfrac{3}{10}(6\pi^2)^{2/3}n_\sigma^{5/3}$ per volume (the formula above with $g = 1$), and the contact interaction gives $g_c\,n_\uparrow n_\downarrow$ (Section 13.5). (Section 13.15.)
- **Polarization** $\zeta = (n_{up} - n_{down})/n$: how unequally two labels are occupied. (Section 13.19.)
- **Polynomial**: By the Leibniz formula every term of $\det(M - \lambda I)$ is a product of $n$ entries, of which at most $n$ (the diagonal ones) contain $\lambda$; so $p$ is a polynomial (a sum of powers of $\lambda$ with number coefficients) of degree $n$. (Sections 1.34, 2.5, 11.18 and 12.16.)
- **Populations**: The right panel shows the populations of M5: the energy density of each of its three parts, computed by calling `model` with a list that holds only that part (`[0]` takes the first of the two returned sums, the energy density), in the colours from the fifth on (`PALETTE[4:]`), and their total in black, with the zero line. (Section 22.23.)
- **Positive branch**: the levels whose value without interaction ($\lambda = 0$) at the same slice is positive. By the filling convention of the Kohn-Sham record, particles occupy the positive branch together with the zero modes at $k = 0$ (the levels $\varepsilon = 0$ of the free problem); the levels of the negative branch form the normal-ordered sea and are never occupied, not even at a temperature. (Section 15.2.)
- **Positive representation**: Because $B$ has eight eigenvalues $+1$ and eight $-1$, $\Psi^\dagger$ cannot be the Hilbert adjoint of $\Psi$; the Revision record realises it as $\Psi^\dagger = b^*B$ (the positive representation: $\Psi_A = b_A$, $\Psi^\dagger_C = \sum_D b^*_D B_{DC}$). (Sections 21.25 and 21.29.)
- **Potential**: In quantum mechanics the allowed energies $E$ of a particle in one dimension, moving in a potential $V(x)$ (its potential energy at the position $x$), are the eigenvalues of the Schrödinger equation; in units in which Planck's constant divided by $2\pi$ (written $\hbar$) and the mass $m$ are both 1, it reads $-\frac12\, u''(x) + V(x)\, u(x) = E\, u(x)$. (Sections 2.13, 12.29, 15.2 and 18.4.)
- **Potential energy**: Kinetic term $K_\mu$: the part of the Lagrangian that holds the derivative along the direction $\mu$; potential energy: $mS + U(S)$, the part without derivatives. (Section 9.16.)
- **Potential part**: The terms with derivatives (the $K$'s) form the kinetic part; the terms without derivatives, $mS + U(S)$, form the potential part. (Section 9.7.)
- **Potential well, bound state**: a region where $V$ is lower than outside; a bound state is a solution with $E$ below the outside value of $V$ that decays to zero far away. Its energy is an eigenvalue. (Section 2.16.)
- **Power**: Power $a^p$ and root $a^{1/n}$; the laws of powers $a^p a^q = a^{p+q}$, $(a^p)^q = a^{pq}$, $(ab)^p = a^p b^p$, $a^{-p} = 1/a^p$ for positive $a, b$. (Section 1.8.)
- **Power iteration**: multiply a vector by $M$ again and again and rescale it to length 1; it turns towards the eigenvector of the eigenvalue of largest size. (Sections 1.37 and 1.40.)
- **PowerShell 7**: on Windows, the program PowerShell 7 (the command `pwsh`), downloaded from the address aka.ms/powershell, which runs the PowerShell twin of the gate; Git for Windows also brings bash, so the bash form of the gate works there too. (Section 23.3.)
- **Prescribed background**: a metric that is given and not solved for from field equations. (Sections 0.2, 0.14, 3.12, 3.34, 14.1, 14.32, 15.16, 17.1, 17.2, 17.10, 17.20, 21.31 and 22.2.)
- **Prescribed source**: a source chosen by hand to see what the equations do. It is ASSUMED, not derived from a field. (Sections 12.2 and 12.24.)
- **Present measure**: `\w+` is one or more letters, digits or underscores (the name of a state, such as N8_lam0_a00_T10), `\S+` a number, and `\(` and `\)` are round brackets themselves; the four bracketed parts are the name of the state, the error of the old method, the former measure (the difference between the two runs when both used the old method) and the present measure (the difference seen by the present refined run). (Section 0.25.)
- **Pressure**: Cosmologists describe the matter of the universe, at each moment, by two numbers: the energy density $\rho$ (energy per unit volume) and the pressure $p$ (the push per unit area, which is also energy per unit volume). (Sections 3.26, 3.29, 9.1, 9.16, 9.24, 12.2, 15.16, 15.19, 17.2, 17.10 and 20.2.)
- **Prime**: $a_4' = da_4/dx_4$ and $a_4'' = d^2a_4/dx_4^2$. The code writes them as the symbols `ad1` and `ad2`. (Sections 12.2 and 17.2.)
- **Prime number**: a whole number larger than 1 that only 1 and itself divide. (Sections 1.2 and 1.8.)
- **Principal part**: of a system of first-order partial differential equations at a point: the derivative terms alone, with their coefficients taken at that point. For the field equation with $U = 0$ it is the mode matrix without the mass term, with the frame momenta of that point. (Section 8.18.)
- **The principle of stationary action** (ASSUMED: it is the starting principle of classical mechanics and of classical field theory, not derived from anything simpler). Among all paths with the same end values $q(0) = q_A$ and $q(T) = q_B$, the particle follows one whose action does not change to first order when the path is changed a little. (Sections 7.2 and 7.8; the opening of Chapter 7.)
- **Private environment**: a folder with its own copy of Python and of the packages, so that installing them changes nothing else on the computer. (Section 0.12.)
- **A private Python environment**: A private Python environment is a folder with its own copy of Python and of the packages, so that installing the packages changes nothing else on your computer. (Section 0.8.)
- **Probability**: Amplitude and probability: when an orbital is written as a sum $\sum_n c_n\varphi_n$ of instantaneous orbitals, the complex number $c_n$ is the amplitude of level $n$ and $|c_n|^2$ the probability to find the particle in level $n$. (Sections 0.18, 20.2 and 22.2.)
- **Probability amplitude**: the number from which quantum theory computes how likely a process is (Chapter 10). (Section 0.2.)
- **Process**: a solution of a dynamical equation that connects an initial state with a different final state. (Section 20.2.)
- **Product** $\gamma_A$: for a set $A$ of directions, the product of their gamma matrices in increasing order, for example $\gamma_{\{x_2, x_5\}} = \gamma^{(x_2)}\gamma^{(x_5)}$; for the empty set, $\gamma_{\{\}} = I_{16}$. (Sections 1.12, 1.34, 4.15, 4.19, 18.8 and 21.5.)
- **Product Fock space**: the Fock space of the modes of both universes together, here $16 + 16 = 32$ fermion modes ($2^{32}$ occupation patterns). (Section 10.48.)
- **Product of a set of directions** $\gamma_A$: for a set $A$ of directions, the product of their gammas in increasing order, for example $\gamma_{\{x_2, x_5\}} = \gamma^{(x_2)}\gamma^{(x_5)}$; $\gamma_{\{\}} = I_{16}$. There are $2^8 = 256$ sets, so 256 products; they are a *basis* of all real $16 \times 16$ matrices when every such matrix is exactly one combination $\sum_A c_A\gamma_A$. (Section 4.19.)
- **Product of different gammas**: a product $P = \gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ of $k$ gammas of $k$ different directions $a_1, \dots, a_k$; the number $k$ is its degree. (Section 5.3.)
- **Product of matrices**: $(AB)_{ij} = \sum_k A_{ik} B_{kj}$ (row $i$ of $A$ times column $j$ of $B$, entry by entry, added up). In Python it is written `A @ B`. The order matters: in general $AB \neq BA$. (Section 4.7.)
- **Product rule**: For commutators the product rule $[A, BC] = [A, B]C + B[A, C]$ holds, because both sides are $ABC - BCA$ (on the right, $ABC - BAC + BAC - BCA$). (Sections 5.18 and 7.3.)
- **Profile**: a density as a function of $y$, stored at the 151 points $y = -3 + 0.02\,i$. (Sections 16.11, 17.2, 17.7 and 17.10.)
- **Projector**: a matrix $P$ with $PP = P$. It maps every column into one subspace, its range, and leaves the columns of that range unchanged; its eigenvalues are 0 or 1, so its trace is the number of eigenvalues 1. (Sections 5.5, 5.9, 8.25, 9.26, 9.29, 9.30, 10.5, 10.9, 14.5, 14.10, 14.26, 18.2, 18.8 and 21.18.)
- **Proper**: Densities: the particle density $n(y)$, the scalar density $S(y)$ and the density $Q(y)$; proper means per unit of proper 7-volume; the coordinate density $e^{6Hy}n(y)$ is the density per unit of $y$. (Sections 15.2 and 19.20.)
- **Proper density**: a number of particles (or an energy) per unit of proper 7-volume. (Sections 15.13, 15.19, 17.2 and 17.10.)
- **Proper time** $\tau$: the time shown by a clock carried by the body. (Sections 3.4, 3.16 and 3.34.)
- **Proposition**: a proved statement (Notebook 20c); a lemma is a proposition that serves as a step towards others. (Section 20.20.)
- **PROVED**: a status label: the statement is exact. The book gives the complete proof and, where the Revision record contains an exact computer check of the statement, names it: the report file that the verifier wrote and the name of the check in it. A statement is proved by an exact computation of every case, by an exact symbolic computation that holds for every value of its symbols, or by a general derivation in the book (Section 0.3). (Sections 0.3, 0.20, 3.1, 4.21, 5.40, 6.1, 6.30, 8.1, 12.31, 13.38, 14.32, 15.31, 16.26, 17.23 and 22.27.)
- **Provenance file**: `NNx_name.PROVENANCE.md`, next to each notebook. Its last line records the measured facts of the notebook's last verified run, among them the date, result and seconds of its last nbkit check. (Sections 0.7, 23.2 and 23.11.)
- **Pruefer angle** $\theta(y)$: the angle of the point $(a, b)$ seen from the origin, $a = r \cos\theta$, $b = r \sin\theta$ with $r > 0$; we count every full turn, so $\theta$ can grow beyond $2\pi$ (*winding*). $r$ is the distance of the point from the origin, $r^2 = a^2 + b^2$. (Sections 2.1, 2.24, 2.27, 14.14, 14.17, 15.8 and 22.12.)
- **Pruning**: Leaf, pruning (skipping): a complete combination of $k$ curvature entries in the computer's search; pruning means leaving out combinations known to give zero. (Section 11.2.)
- **Pseudo-random generator**: a formula that turns a number (its state) into a new state and an output, again and again; the outputs look random but are completely fixed by the first state, the seed. (Sections 1.49 and 1.53.)
- **Pseudo-random numbers**: Pseudo-random numbers: numbers made by a fixed recipe that look random; the recipe starts from a number called the seed, and the same seed gives the same numbers on every computer. (Section 11.8.)
- **Purely imaginary**: A real number $a$ is the complex number $a + i0$; a number $ib$ with real part 0 is called purely imaginary. (Section 1.10.)
- **Python**: the programming language of the notebooks. A *version number* such as 3.14.5 names one release of a program: the first number (3) changes rarely, the second (14) for new features, the third (5) for corrections. (Sections 0.8, 0.12 and 0.20.)
- **Python dictionary**: a table that maps keys to values; here monomials (tuples of generator numbers) to coefficients. (Section 7.16.)

**Q**

- **Q** (dirac16complex): the quantum reading of T1; the image field carries the indefinite (Krein) metric $-B$ and is the same quantum system written in other variables, and there is no cancellation between two universes that are quantised independently of each other. (Section 0.2; the opening of Chapter 18.)
- **QR factorisation**: `rng.normal(size=(M, M))` is a $4 \times 4$ table of random numbers, `1j` is the imaginary unit $i$, so the argument is a random complex matrix; `np.linalg.qr(...)[0]` is the first factor of its QR factorisation, a unitary matrix $U$ (its columns are orthonormal). (Section 13.14.)
- **Quadratic convergence**: The new error is proportional to the square of the old one (quadratic convergence): once the error is small, the number of correct digits roughly doubles at every step. (Section 16.20.)
- **Quadratic form** of a symmetric matrix $S$: the number $Q(v) = v^T S v = S_{ab} v^a v^b$. (Sections 1.36, 1.40, 4.1, 4.11 and 5.4.)
- **Quantise**: To quantise dirac16complex means to replace its 16 components $\Psi_A$ by operators and to fix their anticommutators. (Section 10.12.)
- **Quantised**: turned into a quantum theory, in which the field becomes an operator, a rule that turns one state of the system into another (Chapter 10). (Sections 0.2 and 5.34; the opening of Chapter 21.)
- **Quantised field, anticommutator**: after quantisation the components are operators with $\{\Psi_r, \Psi_c^\dagger\} = B_{rc}\,\delta$ ($\delta$ the delta function of the positions); a conjugation of the quantised field must preserve this rule. (Section 5.32.)
- **Quantum cosmology**: a quantum theory in which a few numbers that describe the whole geometry, such as a scale factor, are quantum variables; its wave function (the wave function of the universe) is a function of these numbers and obeys the Wheeler-DeWitt equation. It is named in Chapter 22, not used. (Sections 22.2 and 22.4.)
- **Quantum electrodynamics**: That pairs are really made above the threshold, and how often, was computed from quantum electrodynamics, the quantum theory of electrons and light, by Bethe and Heitler (H. Bethe and W. Heitler, Proc. (Section 20.17.)
- **Quantum reading Q**: The Revision pairing record answers with five statements, the quantum reading Q (record `Revision/pairing/pairing-theory.json`, theorem entry `Q`; Revision proof document, section 6). (Section 10.44.)
- **Quantum state**: In the examples of Chapter 10 a quantum state is a column $\psi = (\psi_1, \dots, \psi_n)$ of $n$ complex numbers. (Section 10.11.)
- **Quark**: a constituent of protons and neutrons. (Section 21.35.)
- **Quasi-free state, Wick's rule**: a Slater determinant or a thermal state of independent quanta; the expectation of four field operators is a sum of products of two-operator expectations (a "direct" and an "exchange" term). (Section 14.30.)
- **Quaternion**: *The blocks are quaternion multiplications.* A quaternion is $q = q_4 + q_1\mathbf{i} + q_2\mathbf{j} + q_3\mathbf{k}$ with four real numbers; we store it as the list $(q_1, q_2, q_3, q_4)$, the real part last, to match the blocks. (Section 4.5.)

**R**

- **Radians**: with $\theta$ in radians (the angle measured as the length of the arc on the circle of radius 1; $\pi$ radians are 180 degrees). (Section 1.11.)
- **Radiation-like**: $w_{\rm eff} = 1/3$; dust-like (dark-matter-like): $w_{\rm eff} = 0$; cosmological-constant-like: $w = -1$; phantom: $w < -1$. (Section 22.22.)
- **Radius**: So every eigenvalue lies within the radius $\rho_r$ of some diagonal entry (Gershgorin's theorem), and the interval from $\min(d - \rho) - 1$ to $\max(d + \rho) + 1$ contains them all. (Section 16.15.)
- **Raising**: Raising with $\eta^{ab}$ undoes it: $\eta^{ab}v_b = \eta^{ab}\eta_{bc}v^c = \delta^a{}_c v^c = v^a$ (insert the lowered list; the inverse rule; the delta renames). (Section 1.27.)
- **Random numbers with a seed**: Random numbers with a seed: numbers that look random but are the same in every run, because the generator starts from a fixed number. (Section 4.11.)
- **Random walk**: a path that takes a step of $+1$ or $-1$ at random, again and again. (Sections 0.24 and 0.25.)
- **Random-number generator**: `rng` is a random-number generator with a fixed starting value (the seed 12345), so that the "random" numbers it gives are the same in every run and the figure is the same byte for byte. (Sections 0.24, 1.25, 4.12 and 16.12.)
- **Rank** of a list of matrices: the largest number of independent matrices in it, which is the dimension of its span. sympy computes it exactly with fractions. (Sections 4.13, 4.15, 4.16, 4.19, 5.11, 5.16, 5.26, 8.15, 9.29, 9.30, 10.10, 10.48, 14.5, 16.11, 16.12, 16.13 and 21.15.)
- **Rapidity** $b$: the "angle" of a boost. (Sections 1.13, 1.16, 5.18, 6.16, 6.21 and 8.3.)
- **Rapidity rate**: The rapidity may change from point to point; we take $b = \beta x_4 + b_0$ with two constants $\beta$ (the rapidity rate) and $b_0$, a different boost at every time. (Section 8.3.)
- **Rate** $K$: a number of events per unit time. (Sections 20.2, 20.20, 21.2, 21.35, 22.2 and 22.11.)
- **Ratio**: The right side is the tolerance, and the left side divided by the right side is the ratio. (Sections 16.2, 16.7, 16.11 and 16.23.)
- **Rational number**: A fraction (or rational number) is a quotient $p/q$ of two whole numbers with $q \neq 0$. (Section 1.2.)
- **Raw string**: A string that starts with `r` is a raw string: its backslashes are kept as they are, which the mathematical titles (typeset by matplotlib between dollar signs) need. (Sections 0.17, 5.10, 11.9 and 21.15.)
- **Real**: The author's gamma matrices are real: every entry is $-1$, $0$ or $+1$. (Sections 4.1, 5.28, 5.32, 7.11, 7.16, 8.2, 9.2, 19.15, 21.2, 21.8, 21.11 and 21.14.)
- **Real field**: a column $\Phi$ whose 16 components are real ($\Phi^* = \Phi$); for Grassmann components, a column of real generators ($\theta^* = \theta$). (Sections 7.28 and 7.32.)
- **Real form**: writing $\chi = (a, ib)$ with real $a$, $b$ makes all coefficients real. (Sections 14.17, 19.3 and 22.6.)
- **Real matrix**: a matrix whose entries are real numbers (no $i$). The author's gammas are even simpler: every entry is $-1$, $0$ or $+1$. (Section 18.8.)
- **Real number**: a number on the number line; it may need infinitely many digits that do not repeat, like $\sqrt 2$ or $\pi$. (Sections 1.3 and 1.8.)
- **Real part**: The number $a = \mathrm{Re}\,z$ is its real part and $b = \mathrm{Im}\,z$ its imaginary part. (Sections 1.10 and 1.16.)
- **Reality**: (ii) Reality: every entry of every $\gamma^a$ is $-1$, 0 or $+1$, by (i). (Section 4.5.)
- **Reality condition**: A field equal to its own conjugate obeys $\Psi = M\Psi^\ast$; such a requirement is called a Majorana or reality condition, after the physicist who first used one. (Section 5.29.)
- **Record**: short for the Revision record (see that entry): the committed files of the folder Revision, from which every formula and number of the book comes. A record file is one of them, for example a report whose numbers a notebook reproduces. (Sections 0.16, 5.9 and 16.11.)
- **Recursive**: A function that calls itself is recursive: it goes down into the nested structure until it reaches single values. (Section 16.12.)
- **Redshift**: a 3-momentum $k$ acts like $k\,e^{-a_{4,0}}$ at the slice $a_{4,0}$: momenta shrink as 3-space inflates. (Section 14.24.)
- **Redshift, blueshift**: the decrease, increase of a frame velocity (or momentum) caused by the expansion, contraction of the space it points along. (Section 3.34.)
- **Redshifted**: At a fixed height $y$, along a deflating history ($a_4$ increasing), the frame velocity in 3-space falls like $e^{-a_4}$: motion in 3-space is redshifted, because 3-space inflates and stretches it out. (Sections 3.31, 14.2 and 15.4.)
- **Redshifted momentum** $q = ke^{-a_{4,0}}$: the 3-momentum as the deflating history sees it (Section 22.7). (Sections 22.2, 22.7 and 22.11.)
- **The reference solver**: The reference solver (`Revision/kohn_sham/reference/run_reference.py` with the module `ks_fd.py` in the same folder). (Sections 16.3 and 16.11; the opening of Chapter 16.)
- **Refined numerics**: Refined numerics: $G = 1800$ steps and ten times smaller tolerances. (Sections 16.6 and 16.11.)
- **Refined run**: `Revision/kohn_sham/reports/ks-rust-determinism.json` (14 checks, all PASS) compares a second run with the canonical one (all 244 files, the 243 result files and the manifest, byte-identical; check repeat_byte_identical) and a refined run with twice the RK4 steps and ten times smaller tolerances, against tolerances fixed before the comparison ($10^{-8}$ for levels, energies and thermodynamics, $10^{-6}$ for profiles and derived quantities): for example $E_{KS}$ agrees to $1.9 \times 10^{-12}$ relative (check refined_ground_energies) and 23724 levels agree label by label to $2.1 \times 10^{-9}\,m$ (check refined_eigenvalues). (Section 15.10.)
- **Reflection** $R_u$ along a unit vector $u$: $R_u v = v - 2\,\eta(u, v)\,u/ \eta(u, u)$; it reverses $u$ and keeps every direction orthogonal to $u$. (Sections 5.12, 5.21, 5.26, 18.2 and 18.8.)
- **Regular**: The decaying branch, $\sigma_2\chi = -\chi$ for $k > 0$, is the regular one. (Section 14.12.)
- **Regular expression**: A regular expression is a pattern that describes a family of texts: in `(\d+)/(\d+)`, `\d` means one digit, `+` means one or more of what stands before it, and the round brackets mark the parts to return. (Sections 0.21, 1.48, 2.28, 7.9, 9.30, 11.9, 14.18, 15.20, 16.12, 19.21 and 23.12.)
- **Regular tip**: the chosen condition $b(-L) = 0$ at the cutoff. (Sections 14.12 and 14.17.)
- **Relative difference**: $|a - b|/\max(|a|, 1)$; numbers that agree to the last digits of a computer have relative differences near $10^{-15}$. (Section 19.20.)
- **Relative error**: $|$computed $-$ exact$|$ divided by $|$exact$|$. (Section 1.8.)
- **Remainder**: The last term is the remainder: it shows that the error of keeping only the terms up to $h^n$ is proportional to $h^{n+1}$ when $h$ is small. (Sections 1.2 and 2.3.)
- **Repeating decimal**: a decimal whose digits repeat a block for ever, written with the block in brackets: $1/7 = 0.(142857)$. (Section 1.8.)
- **Report**: a JSON file of the Revision record that holds a list (or table) of named checks, each with a verdict such as PASS. (Sections 0.4, 0.16, 0.20, 3.13, 4.7, 13.20, 23.2 and 23.11.)
- **Repository**: the folder Dirac_claude with every file of this project, downloaded with the program Git. (Sections 0.1, 0.8 and 23.2.)
- **Repository root**: The repository root is that folder itself; every command of Chapter 23 is typed there. (Section 23.2.)
- **Representation, invariant subspace, irreducible**: a group of $16 \times 16$ matrices *represents* the group on columns of 16 numbers. A set of columns that every group matrix maps into itself is *invariant*. (Section 5.16.)
- **Required source**: the $\rho$ and $p$ that the field equations demand for a given $a_4$; we read them off the equations instead of assuming a kind of matter. (Sections 12.1 and 12.19.)
- **Rescaling**: writing the field as a known function times a new field, $\Psi = w(x)\,\chi$, and deriving the equation that $\chi$ obeys. (Sections 6.21 and 8.35.)
- **Residual**: in the self-consistent loop, the largest change of the potential from one iteration to the next; the loop stops when it is below $10^{-11}$. (Sections 5.33, 9.25, 13.32, 13.35, 15.5, 15.8, 15.13, 16.23 and 20.15.)
- **Rest energies**: For a heavy nucleus the threshold approaches the two rest energies $2m$: for $M = 1000m$ it is $1001m/500 = 2.002m$, and for $M = 1836m$ (about the mass of a proton) $1837m/918 \approx 2.001089m$. (Section 20.17.)
- **Rest state**: A rest state $\Psi = u\,e^{-imx_4}$ with $-i\gamma^{(x4)}u = u$ solves it: $\gamma^{(x4)}\partial_4\Psi = \gamma^{(x4)}(-im)u\,e^{-imx_4} = m(-i\gamma^{(x4)}u)e^{-imx_4} = m\Psi$. (Section 21.18.)
- **Restricted**: Hartree-Fock (HF): the best single determinant; restricted (both labels in the same orbital) or unrestricted (each label its own orbital). (Section 13.13.)
- **Return code**: Every program ends with a return code, 0 for success. (Sections 11.9, 15.14, 16.12 and 19.21.)
- **Revision record**: the computations stored in the folder Revision of the repository, done anew for the author's metric. Every number of the book comes from it or from a notebook of the book. (Sections 0.1, 0.20, 1.1, 1.24, 4.7, 11.8, 11.18 and 14.10.)
- **Ricci scalar**: Riemann tensor $R^a{}_{bcd}$ (the MTW convention of the Revision records), Gaussian curvature $\sigma = R^{\theta\varphi}{}_{\theta\varphi}$ of a surface, Ricci scalar $R$, Kretschmann scalar $K$: the measures of curvature. (Sections 3.17, 3.21, 3.29, 6.21, 11.2, 11.18, 12.2 and 12.15.)
- **Ricci tensor** $R^h{}_j$, **Ricci scalar** $R$, **Einstein tensor** $G^h{}_j$: sums of Riemann components defined in Section 12.6. (Sections 3.17, 3.29, 6.21, 11.2, 11.18, 12.2 and 12.15.)
- **Richardson extrapolation**: combining two finite-difference estimates so that their leading errors cancel. (Sections 14.19, 14.24, 15.9, 16.3, 16.5, 16.11, 16.18 and 19.16.)
- **Richardson's rule**: an estimate of the error made from two computations with the step sizes $h$ and $h/2$. (Section 2.10.)
- **Riemann tensor** $R^\rho{}_{\sigma\mu\nu}$: the measure of curvature, built from the Christoffel symbols and their derivatives; it is zero everywhere only for a flat space. (Sections 3.21, 3.29, 6.21, 8.14, 11.2, 11.18, 12.2 and 12.15.)
- **Right derivative**: The right derivative $\partial_R F/\partial\theta_k$ moves $\theta_k$ to the far right instead. (Section 7.11.)
- **Right multiplication**: For a fixed quaternion $u$ the right multiplication $R_u$ maps $q$ to $q\,u$ and the left multiplication $L_u$ maps $q$ to $u\,q$. (Section 4.5.)
- **Right-hand side**: for an unknown function $y(t)$, where $f$ is a known rule that produces a number from $t$ and $y$, the right-hand side. (Section 2.2.)
- **RK4**: the classical Runge-Kutta method of order 4 for solving $dy/dt = f(t, y)$ step by step. (Sections 3.21, 3.34, 8.22, 8.28, 12.24, 14.17, 15.8 and 22.11.)
- **RK4 step count** $G$: the number of RK4 steps on $-L \le y \le 0$; the step is $h = L/G$. (Section 2.27.)
- **Root** (or zero) of a polynomial: a number where it is 0. (Sections 1.8, 1.34, 1.40, 15.8 and 16.23.)
- **Root of unity**: a complex number $z$ with $z^n = 1$ for a whole number $n \geq 1$. (Section 1.16.)
- **Root-mean-square width**: The root-mean-square width $\sqrt{\int x^2 n\,dx/N}$ measures how far the cloud spreads; `.format(*widths)` puts the three numbers into the three braces of the string. (Section 13.36.)
- **Roots of unity**: They are the roots of unity of order $n$, the corners of a regular polygon with $n$ sides on the unit circle. (Section 1.12.)
- **Rotation**: turning the plane about the origin by an angle; it keeps every length. (Sections 1.12, 1.16, 4.13, 5.12, 5.18, 5.21, 5.26, 10.34 and 10.37.)
- **Rotation matrix**: The matrix of $e^{i\alpha} = \cos\alpha + i\sin\alpha$ is the rotation matrix. (Sections 1.12 and 1.16.)
- **Round half to even**: If it lies exactly halfway between two neighbours, the rule is to take the neighbour whose $m$ is even (round half to even). (Section 0.22.)
- **Rounding**: replacing a number by the nearest floating-point number. It happens after every addition, multiplication and division. (Sections 0.22 and 0.24.)
- **Rounding bound**: Rounding bound: an upper limit for the error of a computed root. (Section 16.23.)
- **Rounding error**: the difference between the exact result of an operation and the double that the computer stores. (Sections 2.10, 16.2 and 16.23.)
- **Rounding floor**: For RK4 on Problem A this rounding floor is near $10^{-16}$, and with more steps the error grows again but stays 524 to 3709 times below the bound $N\epsilon e^{-1}$ (COMPUTED, Notebook 02a, In [10]). (Section 2.6.)
- **Runge-Kutta method**: The classical fourth-order Runge-Kutta method (Chapter 2): from the start $n = 1$, $a = 0$, each step evaluates the slopes at the beginning, twice in the middle and at the end of the step, and advances with their weighted average; the error over a fixed time falls like $dt^4$. (Sections 9.24, 9.25, 18.26, 19.16 and 21.36.)
- **Runge-Kutta rule of order 4**: Then comes the classical Runge-Kutta rule of order 4 (RK4, Chapter 2): the first slope `p1` from the equation at the start; a half step with it to the midpoint and the second slope `p2` there; a half step with `p2` and the third slope `p3`, again at the midpoint; a full step with `p3` and the fourth slope `p4` at the end; and the new values as the start plus one step times the weighted mean $(p_1 + 2p_2 + 2p_3 + p_4)/6$. (Section 22.12.)
- **Running sum**: Two panels with a shared vertical axis (`sharey=True`); the loop draws in each a bar chart with blue bars for 3-space, grey for $x_4$ and $x_8$ and red for the extra times, and the running sum (`np.cumsum`, the sum of the first one, two, three, ... values) as black dots joined by lines. (Sections 1.33 and 7.27.)
- **Rust**: Rust is a second programming language. (Sections 0.8, 0.12, 0.20 and 23.3.)
- **The Rust solver**: The Rust solver (Chapter 15). (Sections 15.10, 16.3 and 16.11.)
- **Rust uncertainty**: Rule: multiply by $\tfrac{16}{15}$; the size of the canonical error is the Rust uncertainty. (Section 16.6.)
- **Rust, cargo, program**: Rust is a programming language; cargo builds a Rust crate (a folder with a file `Cargo.toml` and source files) into a program file that the computer runs. (Section 11.8.)

**S**

- **Saddle**: For $T > \pi/\omega$ the coefficient is negative: the true path is still stationary ($S_1 = 0$), but along $\xi_1$ the action is a maximum, while along faster shapes ($\xi_n$ with large $n$) it is still a minimum; such a point is called a saddle. (Sections 7.2 and 13.32.)
- **Safeguarded Newton-bisection**: The Revision Rust solver finds the root of the same function $\Phi$ with fewer evaluations, by the safeguarded Newton-bisection of Section 2.24 (the function find_level of `Revision/kohn_sham/solver/src/shoot.rs`): it widens a bracket around a first guess until $\Phi - $ target changes sign, then takes Newton steps with the derivative $d\Phi/d\varepsilon = \int r^2dy/r(0)^2$ derived above, takes the midpoint of the bracket instead whenever a Newton step would leave the bracket or the last step has not at least halved the mismatch $|\Phi - \text{target}|$, and stops when the bracket, or its last Newton step, is shorter than the tolerance $10^{-13}$ (rootTolerance of `Revision/kohn_sham/results/parameters.json`). (Section 14.14.)
- **Sakharov's three conditions**: the three ingredients that, as A. D. Sakharov showed in 1967, any process must contain that makes more matter than antimatter from a start with equal amounts: (1) some process changes the baryon number; (2) C and CP are violated; (3) these processes happen out of thermal equilibrium. In the theory of this book the only number of this kind is the U(1) charge; Section 21.31 applies the three conditions to the theory as built. (Sections 21.5, 21.31 and 21.35.)
- **Same mass**: solves the field equation of the same form, either with the same $V$ (same mass) or with $-V$ (mass reversed). (Sections 5.28, 5.32 and 21.8.)
- **Sample point**: `at_sample(expr)` gives the decimal value of an expression at the sample point $H = 1$, $z = \pi/4$, $a_4 = \frac12$, $a_4' = \frac12$, $a_4'' = 0$. (Section 6.14.)
- **Scalar**: Its Dirac adjoint is the row $\bar\Phi = \Phi^\dagger C$ (the dagger means: transpose and take the complex conjugate of every entry), and the scalar is the number $S = \bar\Phi\Phi = \Phi^\dagger C\Phi$. (Sections 5.4, 5.32, 9.2, 18.2, 18.26, 21.2 and 21.14.)
- **Scalar density** $S = \bar\Psi\Psi = \Psi^\dagger C \Psi$: the bilinear that the mass term and the potential of the Lagrangian contain. (Sections 7.12, 7.16, 7.19 and 19.4.)
- **Scale**: where $U_{ref}$ is the Richardson uncertainty of the reference, $U_{Rust}$ the measured uncertainty of the Rust solver, and the scale $s$ is $\max(1, |x_{ref}|)$ for a single number and the largest value of the profile for a point of a profile. (Section 16.7.)
- **Scale factor** $s_a = \sqrt{|g_{aa}|}$: the factor by which a coordinate length along $x_a$ is multiplied to give a true length. (Sections 2.1, 2.22, 3.7, 3.12, 3.34, 7.26, 8.2, 8.28, 10.42, 12.2, 12.15, 12.24, 14.2, 14.10, 17.2 and 21.7.)
- **Scaled commutator**: For two directions $a$ and $b$ the scaled commutator. (Section 5.12.)
- **Schroedinger equation**: the equation of quantum mechanics that gives the allowed energies $E$ of a particle in a potential $V(x)$; here, for one dimension and in units with $\hbar = m = 1$ ($\hbar$ is Planck's constant divided by $2\pi$, $m$ the mass), $-\frac{1}{2} u''(x) + V(x) u(x) = E u(x)$. We take it as given. (Sections 2.13 and 2.16.)
- **Schur's lemma** (used here, proved in the text): when the matrices of a representation span all matrices, the representation is irreducible and its commutant is the multiples of 1; an intertwiner between two irreducible representations is zero or invertible. (Section 5.16.)
- **Schwarz's theorem**: This is Schwarz's theorem: for a function whose second partial derivatives are continuous, the order of differentiation does not matter (ASSUMED: a standard theorem of calculus, quoted without proof; Notebook 02c confirms it for this example, and Section 2.24 uses it). (Section 2.18.)
- **Scientific notation**: The `say` line prints the errors in scientific notation (`{e:+.3e}` gives three decimals and a power of ten) and the ratios with four decimals; `", ".join(...)` joins the texts with commas. (Section 7.9.)
- **Scratch folder**: A scratch folder is a folder for throw-away files. (Section 23.2.)
- **Sea**: the levels of the negative branch, which the filling CONVENTION of the record leaves out (normal ordering); sea holes would be thermal antiparticles. (Sections 5.34, 14.21, 15.2 and 15.29.)
- **Sea holes**: Sea: the levels of the negative branch, which the filling CONVENTION of the record leaves out (normal ordering); sea holes would be thermal antiparticles. (Section 15.29.)
- **Secant method**: For one variable and two remembered passes the combined residual can be made exactly zero, and the next input is the point where the straight line through the two last (input, residual) pairs crosses zero: the secant method, which estimates the slope of $G$ from the history. (Section 13.21.)
- **Secant rule**: draw the straight line through the last two points $(\lambda, F(\lambda))$ and take its zero as the next guess. (Section 2.16.)
- **Second difference quotient**: The bracket is $E = -\ddot q - \omega^2q$ with $\ddot q$ replaced by the second difference quotient $(q_{n+1} - 2q_n + q_{n-1})/h^2$. (Section 7.3.)
- **Second order**: Such a method is said to be of second order (or to have order of convergence 2), because for small $h$ the first term $c\,h^2$ dominates: halving $h$ divides the error by about $2^2 = 4$. (Section 16.4.)
- **Second quantisation**: Second quantisation labels a determinant only by which orbitals it uses. (Section 13.4.)
- **Sectional curvature**: is the curvature of the coordinate plane of $x_a$ and $x_b$ (its sectional curvature; "plane" means here the plane of the two directions $x_a$ and $x_b$ at one point). (Section 3.17.)
- **Sector** of a Hermitian matrix $B$ with $B^2 = I$: the columns $u$ with $Bu = u$ (the sector $B = +1$), or those with $Bu = -u$ (the sector $B = -1$). (Sections 4.9, 4.11, 9.26, 9.29, 15.2, 15.24, 22.2 and 22.11.)
- **Seed**: It starts from a number called the seed, and the same seed always gives the same sequence. (Sections 0.22, 0.24, 1.25, 1.49, 1.53, 4.12, 5.17, 7.9, 8.23, 9.17, 11.8, 13.14, 14.11, 16.12, 18.9, 20.11 and 21.15.)
- **Self-adjoint**: the Hamiltonian satisfies $\int\varphi^\dagger h\chi\,dy = \int(h\varphi)^\dagger\chi\,dy$; then the levels are real. (Section 14.17.)
- **Self-adjoint for the Krein form**: The mode matrix satisfies $Bh_k = h_k^\dagger B$ for every momentum (PROVED; `python-field-theory.json`, check `mode_hamiltonian_B_selfadjoint_dispersion`; a matrix with this property is called self-adjoint for the Krein form). (Section 8.19.)
- **Self-consistency**: the potential makes the orbitals, the orbitals make the density, the density makes the potential; a solution is self-consistent when the potential that comes out equals the potential that went in. (Sections 13.1, 13.6, 13.35 and 15.8.)
- **Self-consistent**: the orbitals reproduce the mean field that made them. A computer finds such a state by repeating "densities, then mean field, then orbitals, then densities" until nothing changes. (Sections 0.2, 17.2 and 19.2.)
- **Self-consistent state**: (v) So the densities that the partner problem computes from its own orbitals and occupations are $(n, -S)$, the densities we started from in (ii): B is a fixed point of the partner's loop, a self-consistent state. (Section 19.9.)
- **Self-consistently**: Kohn-Sham state: an approximate state of $N$ identical fermions built from one-particle wave functions (orbitals) that each solve a one-particle equation in a common effective potential; the potential depends on the densities of the occupied orbitals, so the equations are solved self-consistently (repeat until nothing changes). (Section 19.20.)
- **Self-coupling** $\lambda$: the strength with which a field acts on itself (Chapter 7). (Sections 0.2 and 12.29.)
- **Series**: A series is an endless sum $t_0 + t_1 + t_2 + \cdots$; its partial sum $S_N = t_0 + \dots + t_N$ adds the terms up to number $N$, and the series converges to a number $S$ when the error $|S_N - S|$ becomes as small as we like for large $N$. (Sections 1.11 and 1.16.)
- **Set**: an unordered collection of different things, written `{"x1", "x2"}` in Python. Python keeps the names of a set in an order decided by their *hash values*: numbers computed from the names with a secret key that Python chooses anew each time it starts, unless the *environment variable* PYTHONHASHSEED fixes the key. (Sections 0.22, 0.24, 1.41, 2.28, 4.8, 4.13, 4.15, 5.10, 6.14, 8.23, 9.30, 10.43, 11.9, 14.11, 15.14, 17.11, 20.16, 21.15 and 22.23.)
- **Set comprehension**: A set comprehension (braces) keeps each bilinear once, `sorted` puts them in order: 42 components, 15 distinct three-gamma bilinears. (Sections 12.20 and 19.16.)
- **Set-up cell**: The first code cell, the set-up cell, repeats the instructions as comment lines and prepares the helpers that every notebook uses. (Sections 0.7 and 1.1.)
- **sha256**: The fingerprint used here is sha256: a fixed recipe that turns the bytes of a file, however many there are, into a number of 256 binary digits, written as 64 hexadecimal characters. (Sections 0.18 and 15.13.)
- **sha256 fingerprint**: a 64-digit hexadecimal number computed from a file by the method SHA-256; two different files have different fingerprints for all practical purposes, so equal fingerprints mean equal files, byte for byte. (Sections 1.50, 1.53, 17.2 and 17.20.)
- **Shape**: To make "changed a little" precise, take a fixed shape $\xi(t)$ with $\xi(0) = \xi(T) = 0$ (so that the changed path keeps the end values) and a small number $\epsilon$, and form the varied path $q + \epsilon\xi$. (Section 7.2.)
- **Shell**: all lattice vectors with the same $n^2 = n_1^2 + n_2^2 + n_3^2$; $r_3(n^2)$ is their number (for example $r_3(1) = 6$). (Sections 14.21, 14.24, 15.2, 15.13, 17.2 and 19.3.)
- **Shell structure**: Thomas-Fermi uses no orbitals, so it cannot show the four bumps of the Kohn-Sham density (its shell structure). (Section 13.32.)
- **Shift left** by $k$ places (two less-than signs): $k$ zero bits are appended, which multiplies by $2^k$ (every bit moves to a place worth $2^k$ times more). (Section 1.49.)
- **Shift right** by $k$ places (Python writes it with the operator made of two greater-than signs): the last $k$ bits are dropped. This is whole-number division by $2^k$: writing $x = 2^k q + r$ with $0 \leq r < 2^k$, the last $k$ bits of $x$ are the bits of $r$, and the bits before them are those of $q$. (Section 1.49.)
- **Shoelace formula**: The signed area of a polygon with the corners $(x_1, y_1), \dots, (x_K, y_K)$, listed in order, is given by the shoelace formula. (Section 1.21.)
- **Shooting**: solve from one end with the conditions there and a guessed eigenvalue (like aiming a cannon), measure the *mismatch* at the other end (where the shot lands), and change the guess until the mismatch is zero. (Sections 2.16, 14.14, 14.17, 15.8, 19.15 and 19.16.)
- **Shooting function** $F$: the mismatch as a function of the guess; the eigenvalues are its zeros. (Sections 2.12, 2.16 and 14.14.)
- **Shooting method**: The Rust program of the Revision record solves them by the shooting method: it guesses an energy, integrates the equations from one end to the other with the classical fourth-order Runge-Kutta method (RK4) in 900 steps, measures by how much the condition at the far end fails, and corrects the energy with Newton's method. (Section 2.1.)
- **Sign convention**: Energy-momentum tensor $T^\mu{}_\nu$: the energy density $\rho = -T^{x_4}{}_{x_4}$, the pressures $p_\mu = T^\mu{}_\mu$ (no sum), and the mixed components; sign convention $\sigma_T = +1$ of the Revision record. (Section 12.29.)
- **Sign of a permutation**: $\mathrm{sign}(\sigma) = (-1)^{N}$, where $N$ is the number of inversions: $+1$ for an even permutation (even $N$), $-1$ for an odd one. (Section 11.8.)
- **Sign** of a permutation: $+1$ if it has an even number of inversions (an even permutation), $-1$ if odd. (Sections 1.19, 1.24, 1.47 and 11.2.)
- **Sign of a reordering**: putting the factors of a product into increasing order by exchanging neighbours; every exchange of two generators gives a factor $-1$. The total factor is $+1$ for an even and $-1$ for an odd number of exchanges. (Section 7.16.)
- **Sign pattern** of $g$: the pair $(\mathrm{sign}\det A, \mathrm{sign}\det D)$. (Sections 5.23 and 5.26.)
- **Signature**: the numbers of positive and of negative entries of the metric. Here it is (4,4): four space-like and four time-like directions. (Sections 0.5, 0.14, 0.16, 1.27, 1.32, 1.36, 1.40, 2.19, 3.4, 3.12, 4.4, 5.4, 5.9, 6.13, 7.26, 10.2, 10.9, 12.2 and 21.14.)
- **Signed area**: The signed area of a polygon with the corners $(x_1, y_1), \dots, (x_K, y_K)$, listed in order, is given by the shoelace formula. (Section 1.21.)
- **Signed byte**: A signed byte uses the same 8 bits for the numbers $-128$ to 127: a negative number $-m$ is stored as $256 - m$ (the two's complement). (Sections 1.49 and 1.53.)
- **Signed permutation matrix**: a square matrix with exactly one nonzero entry in every row and in every column, that entry being $+1$ or $-1$. Acting on a column it puts the components into a new order and changes some of their signs. Every gamma matrix of the author, and the matrix $C$, is one. (Sections 1.19, 1.24, 4.2, 4.5, 4.7, 4.17, 4.19, 5.2, 5.9, 7.12, 17.20, 17.21, 18.2, 18.8, 19.15, 19.16 and 21.7.)
- **The signs of the directions**: the table $\eta$ whose diagonal entries are $+1$, $+1$, $+1$, $-1$, $-1$, $-1$, $-1$, $+1$ in the order $x_1, \ldots, x_8$: the directions $x_1, x_2, x_3, x_8$ are space-like and $x_4, x_5, x_6, x_7$ time-like; the signature is (4,4). (Section 0.5.)
- **Similar**: Matrices related in this way ($N = SMS^{-1}$) are called similar, and similar matrices have the same eigenvalues. (Sections 10.6, 20.12 and 21.26.)
- **Similar matrices**: $N = PMP^{-1}$; they have the same spectrum. (Section 18.26.)
- **Simpson's rule**: an integration rule with the weights $1, 4, 2, 4, \dots, 4, 1$ times (step/3). (Sections 13.15, 14.17, 14.18, 15.8, 17.2, 17.20, 17.21 and 22.12.)
- **Singular value decomposition**: The singular value decomposition (`np.linalg.svd`) writes a matrix $A$ as $U\Sigma V^\dagger$ with a list of numbers $\Sigma$ (the singular values, sorted from large to small) and two matrices $U$ and $V$ whose columns have length 1 and are perpendicular; a column of $V$ whose singular value is zero solves $Au = 0$. numpy returns $V^\dagger$ as `vh`, so the last row of `vh`, conjugated, is the last column of $V$. (Sections 8.23, 9.30, 18.27 and 21.30.)
- **Singular values**: for a matrix $M$ the square roots of the eigenvalues of $M^TM$. The number of zero singular values of $M$ is the number of independent solutions of $Mx = 0$. (Sections 5.27 and 10.37.)
- **Singularity**: "The big bang." In cosmology the big bang is the hot, dense early phase from which the observed expansion started; in the classical solutions of Einstein's equations that describe it, the scale factor of space goes to zero at a finite time in the past, and the equations break down there (a singularity). (Section 20.3.)
- **Size**: The size of a matrix (the largest factor by which it stretches the length of a column) is therefore exactly $k_5$ for $h_A$: $\lVert h_Au\rVert^2 = u^\dagger h_A^\dagger h_Au = k_5^2\,u^\dagger u$. (Section 10.39.)
- **Size of a matrix (spectral norm)**: the largest factor by which the matrix stretches the length of a column; in code `np.linalg.norm(M, 2)`. (Section 10.42.)
- **Slater determinant**: the antisymmetric state of $N$ fermions built from $N$ orthonormal orbitals, $\Phi = \det[\phi_a(x_i)]/\sqrt{N!}$. (Sections 13.3 and 13.13.)
- **Slice**: the function of ONE variable obtained by holding the others fixed; the partial derivative is the slope of its graph. (Sections 2.18, 2.22, 3.8, 4.8, 5.10, 14.3, 14.10, 14.24, 15.1, 15.13, 16.1, 17.2, 17.10, 17.20, 18.27, 19.2, 19.16, 19.20, 22.1, 22.11 and 22.23.)
- **Slope $c$**: $d\varepsilon/dk$ of the brane band at $k = 0$. (Sections 2.6, 3.8, 11.2, 12.2, 12.19, 14.24, 16.18 and 17.2.)
- **Smallest singular value** of a square matrix $M$: the smallest length of $Mu$ over all columns $u$ of length 1. It is 0 exactly when some nonzero $u$ has $Mu = 0$. numpy computes it with `np.linalg.svd`. (Sections 4.9 and 4.11.)
- **So(4,4)**: the real $8 \times 8$ matrices $X$ with $X^T\eta + \eta X = 0$ (the *Lie algebra* of O(4,4)). (Sections 5.12, 5.23 and 5.26.)
- **Sobolev norm of order $s$**: a way to measure the size of data that also counts how fast they wiggle; for one wave of momentum $K$ and amplitude $\epsilon$ it is $\epsilon\,(1 + K^2)^{s/2}$. Larger $s$ punishes wiggly data more. (Sections 8.18 and 8.22.)
- **Solution space**: the set of all solutions $X$ of a list of linear equations without constant terms; its dimension is the number of free parameters. (Sections 4.19, 5.16 and 21.14.)
- **Solution**, **boundary condition**: a solution of a field's equations is a field that satisfies them at every point; a boundary condition is a further condition that a solution must satisfy at the edge of the region in which it is defined (Chapters 2 and 14). (Sections 0.2, 18.1 and 20.2.)
- **Solver**: a program that computes the solution of equations. (Section 16.11.)
- **Source**: the energy-momentum tensor of the fields as it enters the equations of gravity (Chapter 12). (Sections 0.2, 12.2, 12.15, 12.19, 17.2, 17.10 and 17.20.)
- **Source conditions** (from the $a_4$ equations): C1 no component of the source depends on $x_8$ and $q_{48} = q_{84} = 0$; C2 $p_3 + p_t = 2p_8$; C3 for the linear member $a_4 = AHx_4 + a_0$: $p_3 = p_t = p_8$ and a constant $\rho$. (Sections 17.1, 17.2 and 17.20.)
- **Source strength**: In Einstein gravity, with the initial rate $a_4'(0) = H$ (the rate of the history on which the states were computed) and the source strength $\sigma_0 = \kappa\bar\rho(0)/H^2$, the constraint at $a_4 = 0$ fixes $\Lambda$: $3H^2 + 21H^2 + \Lambda = -\sigma_0H^2 \quad\Longrightarrow\quad \Lambda = -24H^2 - \sigma_0H^2$. (Section 17.17.)
- **Space block**: $A$ is the space block and $D$ the time block (the primes distinguish the other two blocks from the matrices $B$ and $C$). (Sections 5.23 and 5.26.)
- **Space-like and time-like**: two kinds of direction. Along a space-like direction a step is measured like a distance; along a time-like direction it is measured like a duration. In the metric a space-like direction has a positive entry and a time-like direction a negative entry. (Section 0.16.)
- **Space-like** and **time-like**: a direction along which a step is measured like a distance, or like a duration; $x_1$, $x_2$, $x_3$ and $x_8$ are space-like, $x_4$ to $x_7$ time-like (Section 0.14). (Sections 0.2, 0.14, 1.5, 1.13, 1.27, 1.32, 3.4, 3.12, 4.3, 4.4, 5.1, 6.13 and 6.27.)
- **Space-like, time-like direction**: $\eta_{nn} = +1$ ($x_1, x_2, x_3$ and the hidden direction $x_8$), respectively $\eta_{nn} = -1$ (the time $x_4$ and the three EXTRA TIMES $x_5, x_6, x_7$, which deflate exponentially in the author's metric). (Section 18.8.)
- **Space-space**: The factor $\frac12(\eta_{aa} + \eta_{bb})$ is $+1$ for a pair of two space-like directions (space-space), $-1$ for a pair of two time-like directions (time-time) and $0$ for a boost pair. (Sections 6.23 and 6.27.)
- **Span**: all combinations of a list of matrices. (Sections 4.15, 5.11, 5.16 and 5.26.)
- **Spectral theorem**: Symmetry matters: a real symmetric matrix has only real eigenvalues and an orthonormal set of eigenvectors (the spectral theorem, quoted from linear algebra), as the levels of a self-adjoint problem must; and the counting method of Section 16.15 works only for symmetric matrices. (Section 16.14.)
- **Spectrum**: the list of all eigenvalues of a matrix. (Sections 1.34, 1.40 and 5.9.)
- **Spin**: The spin-statistics rule of ordinary four-dimensional quantum field theory says that particles of half-integer spin (the spin is the intrinsic angular momentum of a particle, measured in units of Planck's constant divided by $2\pi$; the electron has spin $\frac12$), which are the fermions of Chapter 7, must be described by anticommuting fields; described by commuting fields, as dirac16complex00 is, the energy of a spinor field has no lower bound, and this is exactly what the plane waves above show. (Section 9.21.)
- **Spin connection** $\omega_\mu{}^a{}_b$: the numbers that say how the vielbein turns when one moves along $x^\mu$. (Sections 5.28, 6.1, 6.4, 6.13, 6.21, 8.35, 9.16, 12.29, 14.10, 18.3 and 21.22.)
- **Spin density**: The last term comes from the change of the spin connection; the record calls the bilinear in it the totally antisymmetric spin density (it changes sign when two of its three indices are exchanged). (Section 9.6.)
- **Spin generators**: With the spin generators $S^{ab} = \tfrac14(\gamma^{(a)}\gamma^{(b)} - \gamma^{(b)}\gamma^{(a)})$, which equal $\tfrac12\gamma^{(a)}\gamma^{(b)}$ for $a \neq b$ (the two products differ only in sign) and 0 for $a = b$ (Chapter 5), the spinor connection is $\Omega_\mu = \tfrac12\,\omega_{\mu ab}S^{ab} = \sum_{a<b}\omega_{\mu ab}S^{ab}$. (Section 7.18.)
- **Spin transformation**: A spin transformation is a $16 \times 16$ matrix $R$ that acts on the components, $\Psi \to R\Psi$, and at the same time turns the eight directions into each other. (Sections 5.18 and 7.19.)
- **Spin(4,3)**: the spin group of the seven slice directions $x_1, x_2, x_3, x_5, x_6, x_7, x_8$ (every direction except the time $x_4$: four space-like, three time-like). In Chapter 10 it is generated by the 21 generators $S^{ab}$ whose pair of directions does not contain $x_4$; exactly these 21 generators are Krein-unitary. (Sections 10.34 and 10.37.)
- **Spin(4,4)**: the subgroup of Pin(4,4) (see that entry) made of the products $\gamma(u_1)\cdots\gamma(u_k)$ of an EVEN number $k$ of unit vectors. Under it the 16 components split into two inequivalent halves of 8 (PROVED, Section 5.13), while under Pin(4,4) they are irreducible. (Sections 5.12, 5.13, 5.21 and 5.26.)
- **Spin-statistics**: This is the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian. (Section 9.21.)
- **Spin-statistics rule**: The spin-statistics rule of ordinary four-dimensional quantum field theory says that particles of half-integer spin (the spin is the intrinsic angular momentum of a particle, measured in units of Planck's constant divided by $2\pi$; the electron has spin $\frac12$), which are the fermions of Chapter 7, must be described by anticommuting fields; described by commuting fields, as dirac16complex00 is, the energy of a spinor field has no lower bound, and this is exactly what the plane waves above show. (Section 9.21.)
- **Spin-statistics theorem**: In ordinary 3+1 dimensional physics this choice is not free: the spin-statistics theorem of quantum field theory shows that, if the energy is to be bounded below and measurements at two points that no signal can connect are not to disturb each other, fields of half-integer spin (such as the electron's) must be quantised with anticommutators and fields of whole-number spin with commutators. (Section 10.12.)
- **Spinor** $\Phi$: a column of 16 complex numbers (here: functions of $x_4$). dirac16complex00 is a field of such spinors whose components are ordinary (commuting) complex numbers. (Sections 7.1, 12.29 and 20.15.)
- **Spinor boost** $R(x)$: a 16 x 16 matrix that turns spinors when the frame is boosted; it covers $\Lambda$ when $R^{-1}\gamma^a R = \sum_b \Lambda^a{}_b \gamma^b$ for every $a$. (Sections 6.21 and 6.27.)
- **Spinor connection** $\Omega_\mu = \frac12 \sum_{a,b}\omega_{\mu ab} S^{ab}$: a 16 x 16 matrix for every $\mu$. (Sections 6.7, 6.13, 6.21, 6.27, 7.18, 7.26, 8.2 and 8.14.)
- **Spinor curvature**: Spinor curvature $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$, where $[A, B] = AB - BA$ (the *commutator*); the record proves $F_{\mu\nu} = \frac14\sum R_{\rho\sigma\mu\nu}\gamma^\rho \gamma^\sigma$. (Section 8.14.)
- **Spinor field** $\Psi$: at every point of spacetime a column of 16 numbers $\Psi_1, \dots, \Psi_{16}$ (its *components*). (Sections 5.32, 21.2 and 21.14.)
- **Spinor norm**: Spinor norm $N(g) = \eta(u_1, u_1)\cdots\eta(u_k, u_k)$ of such a product. (Section 5.21.)
- **Spread**: For a state with a nonzero source the record computes the spread of the energy density. (Section 17.4.)
- **Square**: It is square if $m = n$. (Sections 1.18 and 1.24.)
- **Square root of a quadratic form**: an expression $L$, linear in the variables, whose square is the quadratic form: $L^2 = p^2 + q^2$ (times the identity matrix when $L$ is a matrix). (Section 4.11.)
- **Squared length**: The squared length of a vector is $Q(v) = \eta_{ab}v^a v^b = v^a v_a = (v^1)^2 + (v^2)^2 + (v^3)^2 - (v^4)^2 - (v^5)^2 - (v^6)^2 - (v^7)^2 + (v^8)^2$. (Sections 1.27, 1.32 and 3.4.)
- **Squared length of the velocity**: $g(u, u) = \sum_a g_{aa} (u^a)^2$ (the metric is diagonal). For a body with mass it equals $-1$ when $\tau$ is its proper time. (Section 3.34.)
- **Stack**: The stack is a list of partial combinations still to be extended, each a tuple of the chosen entry numbers with the two masks; it starts with the empty combination. (Section 11.19.)
- **Stacked bar chart**: A stacked bar chart: for each field the bars of the three types are drawn on top of each other (`bottom=bottoms` starts each new bar where the previous one ended), the counts are written into the bars and the totals above them (`"\n"` in a label is a line break). (Section 7.27.)
- **Staggered**: Such a grid, on which the two components live on alternating points, is called staggered. (Section 16.14.)
- **Staggered grid**: $a$ is stored at the half nodes, $b$ at the nodes. (Sections 16.3 and 16.18.)
- **Standard deviation**: A measured fraction $p$ from $N$ tries is expected to scatter around the true value by about one standard deviation $\sqrt{p(1-p)/N}$ (ASSUMED from probability), here $\sqrt{0.25/200000} \approx 0.0011$ for the first; both measurements lie within 4 standard deviations of $1/2$ and of $1/2 + 1/\pi$ (Figure 01e.2). (Sections 1.27, 1.50, 1.53 and 11.4.)
- **State**: In quantum theory a state is a column of numbers, and an operator is a rule that turns a state into another state; here every operator is a (big) matrix acting on columns. (Sections 1.49, 1.53, 5.34, 5.37, 10.18 and 22.2.)
- **State id**: a name such as `N136_lamp2_a20`: $N = 136$ particles, coupling $+\lambda_2$ (`lam0`: $\lambda = 0$; `lamp1`, `lamm1`: $\pm\lambda_1$; `lamp2`, `lamm2`: $\pm\lambda_2$), slice $a_{4,0} = 2.0$ (the digits are ten times $a_{4,0}$). A thermal state ends with `_T10`, `_T20` or `_T50`: the temperature $T = 0.01$, $0.02$ or $0.05$ (in units of the mass $m$). (Sections 16.11 and 16.23.)
- **Stationary**: A path is stationary if $S_1 = 0$ for every shape $\xi$; the principle says that the true motion is stationary. (Sections 5.6 and 7.2.)
- **Stationary path**: a path whose first variation is zero for every variation. (Section 7.8.)
- **Stationary state**: So $\Psi_0 = \sin z\,e^{iwx_4}\chi_0$ has a single frequency: a stationary state. (Section 21.18.)
- **Statistics**: whether the components of a field commute (the field dirac16complex00) or anticommute (the field dirac16complex, whose components are Grassmann numbers). (Sections 7.26 and 18.2.)
- **Status labels**: PROVED (exact, by a derivation or by exact computation, with the record file and check), COMPUTED (numerical, with its accuracy), ASSUMED, HYPOTHESIS, OPEN. (Sections 11.2, 12.2, 12.19, 17.10, 17.20, 21.2 and 21.35.)
- **Status words**: PROVED (exact, for all values), CHECKED (exact or to rounding, for the values shown), REPRODUCED (agrees with a Revision record), NOT ESTABLISHED (not shown by these equations). (Section 10.48.)
- **Step**: one command of the gate, with a name such as `algebra-wolfram`. (Sections 15.8 and 23.2.)
- **Step rule**: A step rule says how to compute $y_{n+1}$ from $y_n$. (Section 2.4.)
- **Step size**: It chooses a step size $h$, the times $t_n = n h$, and computes numbers $y_n$ that approximate $y(t_n)$, one step after the other. (Section 2.4.)
- **Storage rule**: We call this the storage rule: a number between $2^{k}$ and $2^{k+1}$ is stored as $m \cdot 2^{k-52}$ with a 53-digit $m$. (Section 0.22.)
- **Strictly increasing**: So $\Phi(\varepsilon)$ is strictly increasing: each target value $l\pi$ or $\pi/2 + l\pi$ is reached for exactly one energy. (Section 2.24.)
- **String**: A variable is a name for a value; this line gives the name `NOTEBOOK_ID` to the text `"00a"` (a text in quotes is called a string). (Sections 0.13, 0.21, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 13.14, 14.11, 15.9, 16.12, 17.11, 18.9, 19.16, 20.11, 21.15 and 22.12.)
- **Sturm count** $c(x)$: the number of eigenvalues of $T$ below a number $x$. (Sections 16.3, 16.15 and 16.18.)
- **Subgroup**: A subgroup is a subset that is itself a group. (Section 5.11.)
- **Subprocess**: a program that another program starts and whose printed output it reads. (Section 0.24.)
- **Subset**: A subset of a set $S$ is a set whose elements all belong to $S$. (Sections 4.13, 4.15 and 16.9.)
- **Subspace**: A subspace is a set of columns that contains every sum and every multiple of its members (for example all columns whose components 9 to 16 are zero). (Section 5.11.)
- **Sudden**: Sudden: so fast that the orbital has no time to change at all. (Section 22.11.)
- **Sudden limit**: the limit of an infinitely fast change, in which the orbital has no time to change at all (Section 22.8). (Section 22.2.)
- **Sum**: Comparing the two: the sum of the eigenvalues is the trace. (Section 1.34.)
- **Sum convention**: the summation convention (see that entry). Chapter 12 writes every sum with $\sum$ or in words, except in the definitions of Section 12.7 and in the formulas quoted from the record, where an index that appears once up and once down is summed over its eight values; "no sum" marks the exceptions. (Sections 5.28 and 12.2.)
- **Summation convention**: an index that appears twice in one product is summed over all its values without writing $\sum$; so $A_{ij} B_{jk}$ means $\sum_j A_{ij} B_{jk}$. (Sections 1.24, 1.26 and 1.32.)
- **Summed label**: in Chapter 11 a label that appears once up and once down inside one term is summed over its eight values, unless "no sum" is said; the free labels $h$ and $j$ are never summed. (Section 11.2.)
- **Sylvester's law of inertia**: the matrices $S$ and $P^T S P$ ($P$ invertible) have the same signature. (Sections 1.40, 3.4 and 16.15.)
- **Symbol** (sympy): a letter that stands for any number, so that sympy can compute exactly with formulas instead of with decimal numbers. (Sections 0.16, 4.11, 4.12, 11.5 and 17.11.)
- **Symmetric (Belinfante) energy-momentum tensor**: the symmetric part $\frac12(T_{\rm var}^{\nu\rho} + T_{\rm var}^{\rho\nu})$ of the variation tensor $T_{\rm var}$ (the energy-momentum tensor obtained by changing the metric in the action), named after the physicist F. J. Belinfante, who showed how to make the energy-momentum tensor of a spinor field symmetric. The record proves its formula for every configuration, solution or not (PROVED; check `T_symmetric_part_Belinfante_C`). (Section 9.6.)
- **Symmetric** array: $S_{ab} = S_{ba}$; antisymmetric array: $A_{ab} = -A_{ba}$ (its diagonal is 0). (Sections 1.28, 1.32, 3.3, 4.2, 4.7, 5.2, 5.9, 6.4, 6.7, 6.23, 7.16, 16.14, 16.18, 18.8, 21.2 and 21.14.)
- **Symmetric difference** $A \triangle B$: the directions that lie in exactly one of the sets $A$ and $B$. (Sections 4.13 and 4.15.)
- **Symmetric logarithmic**: The vertical axis is symmetric logarithmic (`"symlog"`): linear between $-0.001$ and 0.001 and logarithmic outside, so that large and small values of both signs fit. (Sections 1.41, 5.27, 8.15 and 15.14.)
- **Symmetric logarithmic axis**: logarithmic for large positive and negative values and linear near zero, so that both signs fit on one axis. (Sections 15.19 and 17.2.)
- **Symmetric matrix**: $S^T = S$. (Section 1.40.)
- **Symmetric operator (formally Hermitian)**: an operator $h$ with $\int\cos z\,u^\dagger(hv)\,dx_8 = \int\cos z\,(hu)^\dagger v\,dx_8$ for all wave functions $u, v$. A *boundary term* is a part of the integrand that is a derivative, $\partial_8(\ldots)$; its integral is the difference of the bracket at the two ends, so the operator is symmetric when that difference vanishes. (Section 10.31.)
- **Symmetric part**: Write $M$ as the sum of its symmetric part $\tfrac12(M + M^T)$ and its antisymmetric part $\tfrac12(M - M^T)$. (Sections 7.12 and 9.4.)
- **The symmetries C and CP**: C exchanges every particle with its antiparticle, P reflects space as in a mirror, and CP does both (Chapter 21). (Section 0.2.)
- **Symmetrised**: It is symmetrised: the derivative acts once on $\Psi$ and once on $\bar\Psi$, with opposite signs (Section 7.20 shows why). (Section 7.19.)
- **Symmetry**: A symmetry maps the solutions of one theory to solutions of the SAME theory. (Sections 18.13 and 21.22.)
- **Symmetry of the dynamics**: A transformation is a symmetry of the dynamics if it turns every possible history of the system into another possible history that runs in the same direction of time. (Section 21.5.)
- **Symmetry of the metric**: Such a change of coordinates that leaves the metric unchanged is a symmetry of the metric (an isometry). (Section 20.22.)
- **Symmetry pattern**: (iii) The symmetry pattern $(\gamma^a)^T = \eta_{aa}\gamma^a$: symmetric for the space-like $x_1, x_2, x_3, x_8$, antisymmetric for the time-like $x_4, \dots, x_7$. (Sections 4.5 and 21.7.)
- **sympy**: the Python package for exact algebra with symbols; numpy: arrays of numbers; matplotlib: plots. (Sections 3.12, 4.11, 10.9, 14.10, 18.20, 19.15 and 20.11.)
- **sympy symbol**: a letter that stands for any number; `ad1` and `ad2` stand for $a_4' = da_4/dx_4$ and $a_4'' = d^2a_4/dx_4^2$. (Section 12.15.)
- **Sympy, Rational**: sympy computes with exact fractions such as $-1/32$, so its checks are exact, not rounded. (Section 13.19.)
- **System**: Several unknown functions that change together, say a position $x(t)$ and a velocity $v(t)$, form a system. (Section 2.2.)
- **System of ODEs**: several unknown functions changing together, for example a position $x$ and a velocity $v$; $y$ is then a list (a *vector*) of numbers. (Section 2.10.)

**T**

- **T1** (both fields, every gravitational field): a fixed $16 \times 16$ matrix $\Gamma$, the chirality, turns every solution with $(m, \lambda)$ into a solution with $(-m, -\lambda)$; the Lagrangian (the function from which the equations follow) changes as $L_{m,\lambda}[\Gamma\Psi] = -L_{-m,-\lambda}[\Psi]$, the energy-momentum tensor $T$ (the table of the energy and momentum that the field carries) changes into $-T$, and the charge current $J$ into $-J$. (Section 0.2; the opening of Chapter 18.)
- **T1 pair**: A T1 pair has opposite energy-momentum tensors; a T2 pair has equal ones. (Section 20.2.)
- **T1 partner**: T1 partner: $\Gamma\Psi$ with $(-m, -\lambda)$ at the same point. (Sections 20.2 and 20.10.)
- **T2** (both fields): $\Gamma$ combined with the reflection of one space-like direction (an element of the group Pin(4,4)) turns $(m, \lambda)$ into $(-m, \lambda)$, with the same self-coupling; in the author's universe the reflection is the Z2 mirror across the edge $z = \pi/2$ of the hidden direction (a choice of boundary condition, which is ASSUMED, not derived), and the energy-momentum tensor of the image is equal to that of the original (reflected across the mirror), not opposite to it. (Section 0.2; the opening of Chapter 18.)
- **T2 mirror copy**: T2 mirror copy: $\gamma^{(x_8)}\Psi$ placed at the mirror point $\pi - z$, with $(-m, \lambda)$. (Sections 20.2 and 20.10.)
- **T2 pair**: A T1 pair has opposite energy-momentum tensors; a T2 pair has equal ones. (Section 20.2.)
- **T3** (dirac16complex, the Kohn-Sham level: within the Kohn-Sham approximation, which is ASSUMED (Section 0.18), with the ASSUMED Z2 mirror and the correspondingly transformed boundary conditions): every self-consistent Kohn-Sham universe with $(M, \lambda)$ has a partner with $(-M, \lambda)$, and the two have equal energies and equal energy-momentum tensors. (Section 0.2; the opening of Chapter 19.)
- **The table of the plane curvatures** (PROVED; Notebook 03b computes all 28 and finds these six formulas, In [16]):  (Section 3.24.)
- **Tangent**: the straight line that touches a curve at one point; its slope is the derivative there. (Sections 15.19 and 22.22.)
- **Taylor's theorem** (ASSUMED: a standard theorem of one-variable calculus, quoted without proof). If $y$ has $n + 1$ continuous derivatives, then for every step $h$. (Section 2.3.)
- **Temperature** $T$: measured as an energy (Boltzmann's constant is set to 1). (Sections 13.30, 15.29 and 21.2.)
- **Temporary folder**: `tempfile.mkdtemp` creates a new, empty temporary folder in the place the operating system keeps for temporary files (outside the repository; its name starts with `textbook_16a_` and ends with random characters) and returns its name, which `Path` turns into a path: `RUN_FOLDER`. (Section 16.12.)
- **Tension**: Tension: the energy per unit area of a surface, which acts like a negative pressure along it. (Section 22.2.)
- **Tensor** $T^\nu{}_\mu$: a table of $8 \times 8$ numbers at every point, one for each pair of directions $(\nu, \mu)$. The upper index $\nu$ is the row, the lower index $\mu$ the column. Lowering the upper index with the metric gives $T_{\nu\mu} = g_{\nu\nu} T^\nu{}_\mu$ (the metric here is diagonal). (Sections 1.43, 3.14, 9.16 and 11.5.)
- **A terminal** is the window in which you type commands: on Windows the app Windows PowerShell (or Terminal), on macOS the app Terminal (it runs the shell zsh), on Linux any terminal (it runs the shell bash). A command is typed exactly as printed and sent with the Enter key. The commands are printed in framed blocks, one command per line; where they differ between the systems, the block is labelled with the system. (Sections 0.8 and 23.2.)
- **Test equation**: To understand the accuracy of a method we apply it to the simplest equation of all, the test equation. (Section 2.5.)
- **Test field** and **back-reaction**: a field that is computed in a gravitational field given in advance, which the field itself does not change, is a test field. The change of the gravitational field caused by the energy and momentum of the field is its back-reaction. All Kohn-Sham results of the record are test-field results. (Sections 14.3, 15.16, 17.1, 17.2, 17.10, 17.20, 17.22 and 22.2.)
- **Test particle**: A test particle is a body so small that it does not change the metric (ASSUMED: the particles of this section are test particles). (Sections 3.31 and 3.34.)
- **Text buffer**: `io.StringIO()` is a text buffer, a piece of memory that collects printed text. (Section 10.10.)
- **Thawing**: Thawing: $w_a < 0$; freezing: $w_a > 0$. (Section 22.22.)
- **The theorem of the linear history** (PROVED; record entry `theoremLinear`, see the table). Its hypotheses are four: (1) $\Phi$ is a homogeneous condensate of the commuting field that solves its field equation; (2) it meets the off-diagonal conditions above; (3) $a_4$ is twice continuously differentiable ($a_4'$ and $a_4''$ exist and are continuous functions of $x_4$); (4) the three Lovelock couplings $\alpha_1, \alpha_2, \alpha_3$ of Chapter 12 are not all zero. Its conclusion: if the author's metric with this $a_4$ solves the field equations of gravity with the condensate as the source, then $a_4 = AHx_4 + a_0$ with real constants $A$ and $a_0$. The argument uses, besides (3) and (4), the equality $p_3 = p_t$ of a condensate and one equation of the record (the formula is displayed in that section). (Section 9.26.)
- **Thermal ensemble**: It also holds, with occupations $f_a$ between 0 and 1 in place of 0 and 1, for a thermal ensemble of non-interacting fermions (Section 13.26 shows that the occupations of different orbitals are then independent, which is all the proof needs). (Section 13.4.)
- **Thermal equilibrium**: a state in which every process runs forwards as often as backwards, so that on average nothing changes (Chapter 21). (Sections 0.2, 21.2, 21.5 and 21.35.)
- **Thermal hole**: If the sea were treated thermally, each of its orbitals would be empty with the probability $1 - f\big((-\varepsilon_{band} - \mu)/T\big) = f\big((\varepsilon_{band} + \mu)/T\big) = 1/(1 + e^{(\mu + \varepsilon_{band})/T})$; such an empty sea orbital is a thermal hole, which a full quantum treatment would count as an antiparticle of the same universe. (Sections 15.26, 16.20 and 16.23.)
- **Thermal particles**: Thermal holes $H_{th} = \sum_{\varepsilon_i < \mu} g_i\,(1 - f(x_i))$ (missing particles below $\mu$) and thermal particles $P = \sum_{\varepsilon_i > \mu} g_i\,f(x_i)$ (particles above $\mu$). (Sections 16.20 and 16.23.)
- **Thermal states**: Thermal states: the same three $N$, the three couplings $0, \pm\lambda_1$, the five slices and three temperatures $T = 0.01, 0.02, 0.05$, that is $3\cdot3\cdot5\cdot3 = 135$ states. (Section 15.2.)
- **Thomas-Fermi**: (c) Thomas-Fermi: the kinetic energy of each small piece of the line is that of a uniform gas with the local density. (Sections 13.15 and 13.32.)
- **Thomas-Fermi approximation**: the kinetic energy of each small piece of the line is taken from a uniform gas of the same density. (Section 13.35.)
- **The three Lovelock tensors**: The three Lovelock tensors (Sections 11.10 to 11.19). (Section 11.1.)
- **Three rules for moving gammas**: Three rules for moving gammas, each derived from the Clifford relation. (Section 21.7.)
- **Three-gamma bilinear**: the number $\bar\Phi\gamma^{(a)}\gamma^{(b)} \gamma^{(c)}\Phi$ for three different directions $a$, $b$, $c$. (Sections 9.26, 9.29, 12.26, 12.29 and 20.12.)
- **Threshold**: the smallest energy at which a process is allowed. (Sections 20.17 and 20.20.)
- **The time**: $x_4$ is the time. (Section 3.1.)
- **Time block**: $A$ is the space block and $D$ the time block (the primes distinguish the other two blocks from the matrices $B$ and $C$). (Sections 5.23 and 5.26.)
- **Time reversal**: Reflecting a space-like direction ($x_1, x_2, x_3$ or $x_8$) is a parity-type operation (P); reflecting the time $x_4$ is time reversal (T); reflecting an extra time $x_5, x_6, x_7$ is a time-reversal-type operation of an extra time. (Section 21.24.)
- **Time-dependent Kohn-Sham problem**: the problem in which the orbitals evolve in the time $x_4$ under the Hamiltonian of each moment, with the potentials recomputed at every moment from the evolving densities. (Section 22.2.)
- **Time-derivative kernel** $N$: the matrix in the terms of a Lagrangian that contain $\partial_4$, written as $\frac{i}{2}(\Psi^\dagger N\partial_4\Psi - \partial_4\Psi^\dagger N\Psi)$. Canonical quantisation turns it into the anticommutator $\{\Psi_A, \Psi^\dagger_C\} = (N^{-1})_{AC}$ (at one point; derived in the second notebook of Chapter 10). (Section 10.48.)
- **Time-like**: space-like and time-like: a direction along which a step is measured like a distance, or like a duration; $x_1$, $x_2$, $x_3$ and $x_8$ are space-like, $x_4$ to $x_7$ time-like (Section 0.14). (Sections 0.2, 0.14, 1.5, 1.13, 1.27, 1.32, 3.4, 3.12, 4.3, 4.4, 5.1, 6.13 and 6.27.)
- **Time-time**: The factor $\frac12(\eta_{aa} + \eta_{bb})$ is $+1$ for a pair of two space-like directions (space-space), $-1$ for a pair of two time-like directions (time-time) and $0$ for a boost pair. (Sections 6.23 and 6.27.)
- **Tip**: Its end $z \to 0$ is the tip and its end $z = \pi/2$ the patch end. (Sections 2.24, 3.5, 3.12, 3.34, 5.6, 8.2, 8.31, 10.27, 10.31, 14.2, 15.1, 15.13, 16.1, 17.2, 17.10, 19.2, 19.15, 19.20 and 22.1.)
- **Tip angle** $\theta$: the angle of the boundary condition at the tip. (Sections 19.2, 19.15 and 19.20.)
- **Tip condition**: the condition $(1 - Q(\theta))\chi(-L) = 0$ at the cutoff $y = -L$; $\theta = 0$ ($b(-L) = 0$) is the canonical choice. (Section 14.24.)
- **Tip cutoff**: The Kohn-Sham computations stop at $y = -L = -3$, the tip cutoff; the region $-3 \le y \le 0$ is the patch. (Sections 17.2, 17.10 and 17.20.)
- **Tip value**: Brane value and tip value: its values at $y = 0$ and $y = -3$. (Section 16.11.)
- **Tolerance**: the largest difference between two numbers that a check accepts as agreement. (Sections 0.22, 0.24, 15.13, 16.2, 16.7, 16.11, 16.23 and 18.27.)
- **Torus**: The three directions of 3-space are taken as a torus of coordinate size $\ell$: a quantum leaving the box on one side comes back on the other, so the allowed coordinate momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with whole numbers $n_1, n_2, n_3$ and $\Delta k = 2\pi/\ell$. (Section 14.3.)
- **Total charge**: The total charge is the integral of the charge density over the seven directions other than the time. (Section 5.6.)
- **Total derivative**: $\frac{d}{dt}F(q(t), t)$ for some function $F$. (Sections 7.4, 7.8, 7.13, 7.26 and 7.32.)
- **Total derivative on jets**: Jet, total derivative on jets, coefficient ring: as in Notebook 07b: the field components and their derivatives at one point are symbols, and every coefficient is written with $E = e^{a_4}$, $s = \sin^{1/6}z$, $c = \cos z$, $A_1 = a_4'$, $A_2$, $A_3$ (higher derivatives of $a_4$), $H$, $m$, $\lambda$. (Section 7.32.)
- **Toy fluid (ILLUSTRATION)**: a source with assumed pressures $p_3 = w_3\rho$ and $p_t = w_t\rho$, used only to show what the conservation identity does; it is not a solution of the field equations of this book. (Section 9.24.)
- **Trace** $\mathrm{tr}\,M$: the sum of the diagonal entries of a matrix; it obeys $\mathrm{tr}(PR) = \mathrm{tr}(RP)$. (Sections 1.18, 1.26, 1.32, 1.40, 1.44, 2.19, 4.11, 4.15, 5.3, 5.9, 6.8, 6.13, 7.27, 8.14, 8.15, 8.17, 9.8, 9.16, 9.26, 9.29, 10.9, 12.32, 14.11, 14.30 and 18.20.)
- **Transcendental equation**: an equation such as $\tan(pL) = -p/M$ that has no solution formula and is solved numerically. (Sections 2.13 and 2.27.)
- **Transition**: a jump of a particle from an occupied level $n$ to an empty level $m$; its amplitude is a number whose square is the probability of the jump. (Section 15.24.)
- **Transition state**: The midpoint value $\epsilon_{LUMO}(\tfrac12) - \epsilon_{HOMO}(\tfrac12)$ (Slater's transition state) is a good estimate of the integral when the integrand is nearly a straight line in $\tau$. (Section 13.27.)
- **Transpose** $A^T$: the matrix with rows and columns exchanged, $(A^T)_{ij} = A_{ji}$. (Sections 1.12, 1.18, 1.24, 4.7, 4.19, 5.9, 5.32, 7.12, 7.16, 10.9, 18.8, 21.2 and 21.14.)
- **Transposition**: A transposition exchanges two objects. (Section 11.8.)
- **Transverse**: The six transverse scale factors (those of $x_1, x_2, x_3, x_5, x_6, x_7$) multiply to. (Sections 3.7, 3.12 and 3.23.)
- **Trapezoid rule**: the integral over one step approximated by the step length times the average of the two end values. (Sections 2.24, 2.27, 15.3 and 22.12.)
- **Trapezoidal rule**: The flux is added up over time by the trapezoidal rule: on each step the area under the curve is the step times the mean of the two end values, `(fluxes[1:] + fluxes[:-1]) / 2` (`fluxes[1:]` drops the first value and `fluxes[:-1]` the last); `np.cumsum` forms the running sums, and a 0 is put in front for the time 0. (Section 10.32.)
- **Triangle inequality**: Rule: the triangle inequality $|p - q| \le |p| + |q|$ for any two numbers $p$, $q$. (Section 16.7.)
- **Triangular**: For a matrix with zeros below the diagonal (a triangular matrix) only the term of the identity survives in the Leibniz formula, because every other permutation $\sigma$ has some row $i$ with $\sigma(i) < i$ (the numbers $\sigma(i) - i$ add up to 0 and are not all 0, so one of them is negative), and the entry $A_{i\sigma(i)}$ below the diagonal is 0. (Section 1.21.)
- **Tridiagonal**: In the order of the unknowns each row couples only to its two neighbours in the list (a $u$ to the $w$ on either side, a $w$ to the $u$ on either side), so the matrix $T$ of the problem $T z = \varepsilon z$ is tridiagonal; at $k = 0$ its diagonal is zero. (Sections 16.14 and 16.18.)
- **Tridiagonal matrix**: The differential equations then become the eigenvalue problem of a symmetric tridiagonal matrix with $2G - 1$ rows (a matrix whose only nonzero entries are on the main diagonal and its two neighbours). (Section 16.3.)
- **True path**: The true path is $q(t) = \sin t/\sin 1$: it has $\ddot q = -\sin t/\sin 1 = -q$ (the second derivative of $\sin t$ is $-\sin t$), which is Newton's law $\ddot q = -\omega^2 q$ for the spring, and $q(0) = 0$, $q(1) = \sin 1/\sin 1 = 1$. (Section 7.2.)
- **Truncated**: A truncated basis keeps only some of them; a computation converges when its result stops changing as more are kept. (Sections 22.2 and 22.11.)
- **Tunnelling**: a quantum transition through a region that the classical equations forbid (a barrier), with a small but nonzero probability; proposals in which a universe appears by tunnelling are of this kind (Section 20.25). (Sections 18.2 and 20.2.)
- **Tunnelling proposal**: a proposed boundary condition (A. Vilenkin) that picks one solution of the Wheeler-DeWitt equation, in which a universe appears by tunnelling. It is named in Chapter 22, not used, and is not formulated for this 8-dimensional theory. (Sections 22.2 and 22.4.)
- **Tuple**: The loop runs over a tuple (a list in round brackets that cannot be changed) of the two figure names and checks that each file exists. (Sections 0.13, 0.21, 0.25, 2.17, 7.9, 11.9, 12.25, 13.25, 14.11, 14.18, 16.12, 17.11, 19.16, 22.12 and 22.23.)
- **Turning point**: the instant at which the $x_4$ velocity $u^4$ passes through zero, so that $x_4$ stops growing. (Sections 3.31, 3.34, 17.2, 17.20 and 22.19.)
- **Twisted**: For $g$ in Pin(4,4) put $\alpha(g) = g$ if $g$ is even and $\alpha(g) = -g$ if it is odd (the twisted action). (Section 5.12.)
- **The two conservation identities** (Section 11.22), from zero divergence: $\frac{d}{dx_4}E^{x_4}{}_{x_4} = 3a_4'(E^{x_1}{}_{x_1} - E^{x_5}{}_{x_5})$ (I) and $E^{x_8}{}_{x_8} = \frac12(E^{x_1}{}_{x_1} + E^{x_5}{}_{x_5})$ (II), and the constraint propagation $\partial E^{x_4}{}_{x_4}/\partial a_4' = 3a_4'F_k$ (record `python-a4-report.json`, check `bianchi_x4`; Notebook 11c, In [4] and In [5]). (Section 11.28.)
- **Two's complement**: A signed byte uses the same 8 bits for the numbers $-128$ to 127: a negative number $-m$ is stored as $256 - m$ (the two's complement). (Sections 1.49 and 1.53.)
- **Two-site model**: two places L and R, one orbital each, two labels (up, down); hopping $t$ between the sites, repulsion $U$ when both electrons sit on the same site. (Sections 13.13 and 13.24.)

**U**

- **U(1)**: The group of these phases is called U(1). (Section 21.7.)
- **U(1) charge** $Q$: the number that belongs to the phase symmetry $\Psi \to e^{i\alpha}\Psi$ of the field, $Q = \int\cos z\,\Psi^\dagger B\Psi\,d^7x$ (the integral over the seven directions other than $x_4$); it is the only number of the theory that could play the role of matter minus antimatter. It obeys an exact LOCAL conservation law, $\sum_\mu\partial_\mu(\cos z\,J^\mu) = 0$ for every solution of the field equation: the charge of a region changes only by what flows through its boundary (PROVED; lead check `u1_noether_matrix_identity`). The TOTAL charge of a universe is constant only if no charge flows through the brane $z = \pi/2$; this no-flux condition is ASSUMED, not derived (OPEN), and Section 21.18 shows an exact solution whose charge changes by exactly what flows out through the brane. (Sections 21.1, 21.7, 21.16, 21.17, 21.18 and 21.35.)
- **U(1) symmetry**: the multiplication of every component of a field by one and the same complex number of absolute value 1, which changes no equation; it is the reason why the charge obeys its local conservation law: at no point with $0 < z < \pi/2$ is charge created or destroyed, it can only flow from one place to another (Chapter 21). (Sections 0.2 and 20.22.)
- **Ulp**: A difference of one gap is called one unit in the last place, one ulp. (Section 0.22.)
- **Uncertainty**: What each can do is measure an uncertainty: a number $U$ that, for reasons given in Sections 16.5 and 16.6, should be at least as large as the size $|x - X|$ of its error. (Sections 16.2 and 16.11.)
- **Undetermined function**: `sp.Function(name)(y)` makes an undetermined function of $y$: sympy knows nothing about it except that it depends on $y$, so an identity proved with it holds for every function. (Section 19.16.)
- **Uniform gas**: infinitely many fermions spread with the same density everywhere; it is studied in a large periodic box (a box whose opposite faces are glued together), whose volume is then made infinite. (Sections 13.15, 13.19 and 14.30.)
- **Unit circle**: First, $|e^{i\theta}|^2 = \cos^2\theta + \sin^2\theta = 1$ (the modulus of $a + ib$ with $a = \cos\theta$, $b = \sin\theta$; then $\cos^2 + \sin^2 = 1$): the number $e^{i\theta}$ lies on the circle of radius 1, the unit circle, at the angle $\theta$. (Section 1.11.)
- **Unit columns**: Proof, line by line, with the unit columns $e_1, \dots, e_n$ ($e_j$ has 1 in place $j$ and 0 elsewhere) (the formula is displayed in that section). (Section 4.2.)
- **Unit in the last place**: A difference of one gap is called one unit in the last place, one ulp. (Section 0.22.)
- **Unit vector**: eight numbers $v = (v_{x1}, \dots, v_{x8})$ with metric product $\eta(v, v) = \sum_a \eta_{aa} v_a^2 = +1$ (*space-like*) or $-1$ (*time-like*); $\eta_{aa} = +1$ for $x1, x2, x3, x8$ and $-1$ for $x4, x5, x6, x7$. The basic unit vectors are $e_{x1}, \dots, e_{x8}$ (one entry 1, the others 0). (Sections 1.40, 5.12, 5.21 and 5.26.)
- **Unitary**: an evolution that keeps the total probability equal to 1. (Sections 10.34, 10.37, 14.5, 14.10 and 22.11.)
- **Unite values**: the supernova fits quoted by the record, $w = -0.764$ (constant $w$) and $(w_0, w_a) = (-0.861, -0.60)$. (Sections 22.16 and 22.22.)
- **Units**: the plots use $H = 1$ and $\kappa = 1$, so $\kappa\rho$, $\kappa p$ and $\Lambda$ are in units of $H^2$; $\alpha_2 H^2$ and $\alpha_3 H^4$ are pure numbers. (Sections 12.19, 12.24, 12.29, 13.35, 17.2, 20.15 and 20.20.)
- **Universal**: $F$ is universal: it does not depend on $v$. (Section 13.8.)
- **Universe** (of mass $m$): a solution of the field equation with the mass parameter $m$ of the field's Lagrangian, in the author's gravitational field. The sign of $m$ alone does not say which of two physically different kinds of universe one has: theorem T2 shows that the image of a solution with $(-m, \lambda)$ under the reflection of one space-like frame direction is a solution with $(m, \lambda)$ with the same energy-momentum tensor. Section 20.12 builds one example, a solution of the commuting field dirac16complex00 that is by itself the complete source of the author's metric. (Sections 20.3 and 20.12.)
- **Unpack**: The first two lines unpack the four components of each. (Section 4.8.)
- **Unrestricted**: Hartree-Fock (HF): the best single determinant; restricted (both labels in the same orbital) or unrestricted (each label its own orbital). (Sections 13.7 and 13.13.)
- **Unspecified function**: Eight real symbols for the coordinates (`x[0]` is $x_1$, `x[3]` is $x_4$, `x[7]` is $x_8$), a positive symbol $H$, and an unspecified function $a_4(x_4)$: sympy knows nothing about it except that it depends on $x_4$, so every result below holds for every history, the deflating one included. (Section 21.23.)
- **Unsymmetrised**: Call $K_u = \bar\Psi\gamma^\mu D_\mu\Psi = \Psi^\dagger(C\gamma^\mu)(D_\mu\Psi)$ the unsymmetrised kinetic term. (Section 7.20.)
- **Upper**: A pair of index lists is a lower list $(l_1, \dots, l_p)$ and an upper list $(u_1, \dots, u_p)$ of the same length. (Sections 11.2 and 11.8.)
- **Upper and lower index**: $v^a$ and $v_a$ are two lists of eight numbers that belong to the same vector (section 6 of Notebook 01e says how one is made from the other). An upper index is a label, not a power: $v^3$ is a component, and its square is written $(v^3)^2$. (Section 1.32.)
- **Upper index**: A vector $v$ has the components $v^1, \dots, v^8$, written with an upper index: the component of $v$ along $x_3$ is $v^3$, which Python stores as `v[2]`. (Section 1.26.)

**V**

- **Vacuum**: in quantum theory, the state with no particles: every mode empty, written $|0\rangle$. In gravity (Section 20.2), a solution of the vacuum equations, the field equations of gravity with zero source. (Sections 5.34, 5.37, 10.11, 10.18, 10.20, 10.25, 12.2, 12.15, 12.19, 13.4, 18.2 and 20.2.)
- **Vacuum decay**: the quantum transition of a state that has the lowest energy only among its neighbouring states (a false vacuum) into a state of still lower energy; its rate per unit volume is computed from the quantum theory. (Sections 18.2 and 20.2.)
- **Vacuum equations**: the field equations of gravity with zero source, $\sum_k\alpha_kE_{(k)}{}^\mu{}_\nu + \Lambda\delta^\mu_\nu = 0$. (Sections 20.2 and 20.10.)
- **Vacuum value**: Vacuum value $\langle 0|X|0\rangle$ of an operator $X$ and normal ordering $:\!X\!: = X - \langle 0|X|0\rangle$ (for an operator built from two field operators; for products of $b$, $b^*$, $d$, $d^*$ this is the same as moving every creation operator to the left of every annihilation operator, with a sign $-1$ for each exchange). (Section 5.37.)
- **Validation**: a test of a stated uncertainty against a more accurate number. (Section 16.11.)
- **Variable**: A variable is a name for a value; this line gives the name `NOTEBOOK_ID` to the text `"00a"` (a text in quotes is called a string). (Sections 0.13, 1.9, 2.11, 3.13, 4.8, 5.10, 6.14, 7.9, 8.15, 9.17, 10.10, 11.9, 12.16, 14.11, 15.9, 17.11, 18.9, 20.11 and 21.15.)
- **Variation**: a shape $\xi(t)$ with $\xi(0) = \xi(T) = 0$; the varied path is $q + \epsilon\xi$ with a small number $\epsilon$. (Section 7.8.)
- **Variation tensor**: Its result, which we call the variation tensor $T_{\rm var}$, is (the formula is displayed in that section). (Section 9.6.)
- **Variational form**: The solver also computes the variational form, $\sum gf\varepsilon - \langle (M_{in} - m)S_{out} + v_{in}n_{out}\rangle + \langle e_{int}(S_{out}, n_{out})\rangle$, with the input potentials and output densities of the last iteration; the two agree to $2.2 \times 10^{-13}$ relative in all 75 ground states (check ground_energy_two_forms). (Section 15.5.)
- **The variational principle for the density**: (We ASSUME that the minimum is attained.) The variational principle for the density then reads $E_0 = \min_n\Big(F[n] + \int v\,n\,dx\Big)$. (Section 13.8.)
- **Varied path**: To make "changed a little" precise, take a fixed shape $\xi(t)$ with $\xi(0) = \xi(T) = 0$ (so that the changed path keeps the end values) and a small number $\epsilon$, and form the varied path $q + \epsilon\xi$. (Section 7.2.)
- **Vector**: an ordered list of numbers, such as $v = (1, 2, 0)$. (Sections 1.18, 1.24, 2.2, 3.14, 5.12 and 5.21.)
- **Vector components**: a vector $V = V^r e_r + V^\varphi e_\varphi$ is written with the coordinate basis vectors $e_r$ (length 1) and $e_\varphi$ (length $r$). (Section 3.21.)
- **Vector matrix** $\Lambda(g)$: the $8 \times 8$ matrix with $\alpha(g)\gamma^c g^{-1} = \sum_d \Lambda_{dc}\gamma^d$, where $\alpha(g) = g$ for an even and $-g$ for an odd $g$ (the *twisted* action). (Sections 5.12 and 5.26.)
- **Vector potential**: where the effective mass $M_{\rm eff} = m + \tfrac{15}{16}\lambda S$ and the vector potential $v_v = -\tfrac{1}{16}\lambda n$ are made by all the quanta through their scalar density $S$ and number density $n$. (Section 14.3.)
- **Vector rule**: Chapter 5 proved the vector rule $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$. (Section 6.7.)
- **Vectorised**: Vectorised: one numpy operation acts on whole arrays of cases at once. (Sections 22.11 and 22.12.)
- **Vectorized computation**: numpy applies one operation to millions of numbers in an array at once, much faster than a Python loop. (Section 1.47.)
- **Velocity** $u^a = dx^a/d\tau$: how fast each coordinate changes per unit of proper time. (Sections 3.14, 3.34, 7.2 and 7.8.)
- **Velocity kernel**: so the Lagrangian contains $\frac{i}{2}\sqrt{|g|}\,\Psi^\dagger N\partial_4\Psi$ (plus its partner term) with the velocity kernel $N = B$. (Section 18.22.)
- **Verdict**: A report lists its checks; each check has a name, a verdict (PASS or FAIL) and a detail text that says exactly what was verified. (Sections 0.4, 0.20 and 23.2.)
- **Verifier** and **checker**: a program of the Revision record that recomputes a result (exactly, with Wolfram or with sympy, or numerically, with Rust or Python) and writes a report: a JSON file that lists named checks, each with a verdict such as PASS. (Sections 0.20 and 23.2.)
- **Version number**: A version number such as 3.14.5 names one release of a program: the first number changes rarely, the second for new features, the third for corrections. (Section 0.8.)
- **Vertex**: the matrix that sits between the field components in an interaction; for dirac16complex the contact interaction is $(\lambda/2)\,S^2$ with $S = \bar\Psi\Psi = \Psi^\dagger C\,\Psi$, so the vertex is the $16 \times 16$ matrix $C$. (Sections 13.4 and 13.19.)
- **Vielbein** $e^a{}_\mu$: a matrix with $g_{\mu\nu} = \sum_{a,b} e^a{}_\mu \eta_{ab} e^b{}_\nu$; for a diagonal metric the diagonal matrix of the scale factors. (Sections 3.7, 3.12, 5.28, 6.2, 6.13, 6.21, 7.18, 7.26, 8.2, 12.30, 14.2, 18.19 and 21.22.)
- **Vielbein factors**: The author's metric is diagonal, $g_{\mu\mu} = \eta_{\mu\mu} f_\mu^2$ with the positive vielbein factors (Chapter 3 calls them scale factors $h_a$; they are the same numbers). (Sections 6.2, 9.2 and 18.3.)
- **Vielbein postulate**: The canonical one is fixed by the vielbein postulate (below). (Sections 6.4, 6.13, 7.18, 8.4, 18.3 and 21.23.)
- **Violation**: the violation of C2. (Section 17.5.)
- **Volume element**: $\sqrt{|g|} = \cos z$; an integral over the hidden direction is $\int \cos z\,(\ldots)\,dx_8$. (Section 10.31.)
- **Volume factor**: This number is the volume factor: a small box with the coordinate sides $dx_1, \ldots, dx_8$ has the sides $f_1\, dx_1, \ldots, f_8\, dx_8$ in length, so its volume is $f_1 f_2 \cdots f_8 \, dx_1 \cdots dx_8$, and the product of the length factors is $f_1 \cdots f_8 = \sqrt{|g_{11}| \cdots |g_{88}|} = \sqrt{|\det g|}$ (a product of square roots is the square root of the product). (Sections 0.14, 2.19, 3.6 and 7.18.)

**W**

- **Wall time**: the time a clock on the wall shows between the start and the end of a command. (Sections 23.2 and 23.11.)
- **Warp factor** $W = \sin^{1/6} z$: the factor that the scale factors of the six transverse directions $x_1, x_2, x_3, x_5, x_6, x_7$ share; the six transverse entries $g_{11}, g_{22}, g_{33}, g_{55}, g_{66}, g_{77}$ of the metric contain its square $W^2 = \sin^{1/3} z$. (Sections 3.7, 3.12, 14.2 and 14.10.)
- **Warped form**: Inserting $dy^2$ and $W^2$ into the line element of Section 3.5 gives the warped form. (Sections 3.9 and 14.2.)
- **Wave function** $u(x)$: the eigenfunction of the Schroedinger equation; $u(x)^2$ is the probability density of finding the particle at $x$, so we *normalise* it: $\int u^2\,dx = 1$. (Sections 2.13, 2.16, 13.1 and 13.2.)
- **Wave function of the universe**: in quantum cosmology, a quantum state assigned to a whole universe, its geometry included: a function of the few numbers that describe the whole geometry, such as a scale factor. It must obey the Wheeler-DeWitt equation. None is formulated for this 8-dimensional theory. (Sections 18.2, 22.2 and 22.4.)
- **Wave number**: A plane wave $\phi = \cos(kx_1)\cos(\omega x_4)$, with wave number $k$ and angular frequency $\omega$, has $\partial_1^2\phi = -k^2\phi$ and $\partial_4^2\phi = -\omega^2\phi$, so $E = (-k^2 + \omega^2 - m^2)\phi$, which vanishes exactly when. (Sections 7.5 and 7.8.)
- **Weighted average over the hidden direction** $\bar X$ (also called the **moment** of $X$): the integral of $e^{6Hy}X$ over the patch divided by the integral of $e^{6Hy}$. (Section 17.20.)
- **Weighted mean**: $\int e^{6Hy}p_8\,dy / \int e^{6Hy}dy$, the average of $p_8$ over the proper volume. (Sections 17.2, 17.7 and 17.20.)
- **Weighted variance**: The bracket is $\sum_a w_a$ times the weighted variance of the numbers $\epsilon_a - \mu$ with the weights $w_a$, which is never negative (it equals $\sum_a w_a(\epsilon_a - \bar\epsilon)^2$ with the weighted mean $\bar\epsilon$, a sum of non-negative terms). (Section 13.26.)
- **Well posed**: A problem of the kind "given the field at one time, find it at later times" is called well posed (in the sense of the mathematician Jacques Hadamard) when a solution exists, is unique, and changes only a little when the given data change a little. (Sections 4.9 and 8.16.)
- **Wheeler-DeWitt equation**: the equation that the wave function of the universe must obey in quantum cosmology: the analogue, for a geometry, of the Schroedinger equation of a particle. It needs a boundary condition to fix its solution. It is named in this book, not used. (Sections 22.2 and 22.4.)
- **Whole numbers** (integers): $\dots, -2, -1, 0, 1, 2, \dots$. Python computes with them exactly, however large they are. (Sections 1.2 and 1.8.)
- **Wick's theorem**: $\langle a_p^\dagger a_q^\dagger a_s a_r\rangle = \rho_{rp}\rho_{sq} - \rho_{sp}\rho_{rq}$ for determinants and thermal ensembles of non-interacting fermions. (Sections 13.4 and 13.13.)
- **Winding**: So $\theta$ is defined everywhere, and we let it grow continuously, counting every full turn (winding), so that it can exceed $2\pi$. (Section 2.24.)
- **Witness**: an explicit example that proves that something exists. (Sections 9.26, 9.29 and 12.29.)
- **WKB approximation** (after Wentzel, Kramers and Brillouin): when the growth rate $\kappa$ changes slowly, the size grows like $e^{2W}$ with $W = \int\kappa\,dx_4$. (Sections 8.25 and 8.28.)
- **Wolfram Language**: Engine: the program that did the computation: Wolfram Language (the language of Mathematica, run with wolframscript), Python (with the packages sympy, numpy and mpmath), or Rust (a fast compiled language). (Section 0.20.)
- **WolframScript**: WolframScript (the command `wolframscript`), for the exact Wolfram verifiers. (Section 23.3.)
- **Word**: A word is a list of items in the order of the matrix product: an exponential `("exp", a, b, theta)` or a gamma `("gamma", e)`. (Section 5.27.)
- **Wrapper**: Such a function, which calls another and adds something around it, is called a wrapper. (Section 16.12.)

**Z**

- **Z2 brane** (Z2 mirror brane): the brane $z = \pi/2$ together with the ASSUMED Z2 construction: the patch is glued there to a mirror copy of itself (the map $z \to \pi - z$; Z2 is the group of two elements, doing nothing and reflecting), and the mirror fixes a boundary condition for the field at that surface (the even or the odd brane parity). It is ASSUMED, not derived; the junction condition at the brane is OPEN. (Sections 8.31, 14.17, 18.2 and 20.2.)
- **Z2 construction**: Gluing the mirror patch to the patch at the brane is the Z2 construction of the Revision record; it is ASSUMED. (Sections 18.2 and 20.2.)
- **Z2 mirror**: a reflection across the edge $z = \pi/2$ of the hidden direction, imposed as a boundary condition; Z2 is the group of two elements, doing nothing and reflecting (Chapter 14). (Sections 0.2, 5.6, 14.12, 17.2 and 22.2.)
- **Z2 mirror brane**: the ASSUMED picture that the patch $y \le 0$ is glued at $y = 0$ to a mirror copy; it gives the even parity ($b(0) = 0$) and the odd parity ($a(0) = 0$). (Section 14.17.)
- **Zero modes, $N = 8$**: the eight brane-bound orbitals at zero 3-momentum, $\chi = (a, 0)$ with $a \propto e^{My}$; filling them gives the state $N = 8$. (Sections 2.24, 14.30, 15.2, 15.3, 16.13, 16.18, 19.2, 19.12 and 19.20.)
