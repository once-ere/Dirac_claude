## 19. Reproducing everything

Every proof of this book is paired with an exact machine check, and every number is copied from a committed file of the repository. This appendix shows how to regenerate those files and checks on your own computer, starting from nothing but an internet connection. It gives every command twice, once for PowerShell (the command shell of Windows) and once for Bash (the shell of Git Bash on Windows, of macOS and of Linux), it says what each command prints when it succeeds and how long it took on the computer that produced the committed files, and it states plainly which stages can be checked completely today and which cannot yet.

The commands of this appendix were run for this edition from a fresh clone of the public repository at commit `4cd47fe` (2026-09-30), on the computer described in Section 19.2, unless a paragraph says otherwise. Where a run takes hours, the appendix does not repeat it; it quotes the wall time recorded in the committed gate logs, in the headers of the gate scripts, in `README.md` or in `HANDOFF.md`, and names the source.

### 19.1 What reproducing means, and the state of each stage

**Three levels.** Section 0.8 described three levels of checking a statement: following the derivation, reading the committed report of the machine check, and running the programs again. This appendix is about the third level. Running a program again means: the program recomputes a result from its inputs, writes a new report, and the new report is compared with the committed one. Two kinds of agreement are used. For exact computations (integers, fractions, symbols) and for the numerical outputs of a fixed program on a fixed engine, the new file must be **byte-identical** to the committed one: the two files are the same sequence of bytes. For numerical results computed in another way (a finer grid, tighter tolerances, a different solver) the new numbers must agree with the old ones within a stated tolerance.

**Gates.** For each finished stage the repository contains a **gate**: a script that runs every program of the stage in a fixed order, stops at the first failure, compares every output with the committed file, and ends with one line that says `OK` or `FAILED`. Each gate exists twice, as a PowerShell script (`.ps1`) and as a Bash script (`.sh`); the two are called twins, run the same steps and print the same final line.

**The state on 2026-09-30.** The table lists what can be checked. The column "gate" names the scripts in the folder `scripts/`.

| Stage | Gate | Final line of a successful run | State on 2026-09-30 |
| --- | --- | --- | --- |
| 1: the field in an arbitrary gravitational field | `verify_stage1_arbitrary_field` | `stage1_arbitrary_field_verification=OK` | complete; both twins passed from fresh public clones |
| 2: the primordial field | `verify_stage2_primordial_field` | `stage2_primordial_field_verification=OK` | complete; both twins passed from fresh public clones |
| 3: dark-sector numerics | `verify_stage3_dark_sector` | `stage3_dark_sector_verification=OK` | complete; both twins passed from fresh public clones of earlier commits; at `4cd47fe` its last-but-one step, all unit tests, fails for reasons outside Stage 3 (Sections 19.8 and 19.11) |
| 4: Kohn–Sham states | `verify_stage4_kohn_sham` | `stage4_kohn_sham_verification=OK` | not finished: the gate has never been run to the end and cannot pass yet (Section 19.9) |
| 5: dirac16complex00 and the pairing theorems | none yet | none | exact theory committed and checked; Kohn–Sham pair numerics partial; documents and gate not written (Section 19.10) |
| matter and antimatter | none | none | exact theory committed and checked; document built and registered (Section 19.10) |
| this textbook | the assembler and the PDF builder | `textbook_assembly=OK`, `provenance_pdf=OK` | Section 19.12 |

The sources of this table are `README.md` (section "Stages and documents"), `HANDOFF.md` (section 2), the committed gate logs in `handoff/reviews/`, and the committed reports named in Sections 19.6 to 19.12. The rest of this appendix goes through the stages one by one.

### 19.2 The computer and the tools

**The test computer.** The committed outputs and every timing of this appendix come from one computer: an Intel Core Ultra 9 275HX processor with 24 logical processors, running Windows 11 Pro for Workstations (build 10.0.26200). While the commands of this edition were timed, other jobs of the project were running on the same computer and kept its processor busy (Windows reported a load near 100 percent); the timings are therefore upper values, and an otherwise idle computer is faster. The Stage-3 programs were also tested on Ubuntu 24.04 running inside Windows (student guide `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md`, §2).

**The tools.** Six programs are needed. The versions are the ones that produced the committed files.

| Tool | Version used | Needed for |
| --- | --- | --- |
| Git | 2.51.2 | cloning the repository and the numerical engine; all stages |
| Python, with numpy, sympy, matplotlib, nbformat, nbclient, nbconvert, ipykernel | Python 3.14.5; numpy 2.4.6, sympy 1.14.0, matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, nbconvert 7.16.6, ipykernel 7.1.0 | every stage and the textbook |
| WolframScript with the Wolfram Language (a Wolfram Engine or Mathematica) | WolframScript 1.14.0, Wolfram Language 15.0.1 | the exact Wolfram verifiers of Stages 1, 2, 4 and 5 and of the matter–antimatter analysis; optional in Stages 3 and 4 |
| A TeX distribution with pdflatex | MiKTeX 26.5 (pdfTeX 4.27) | every PDF |
| Rust with cargo, rustfmt and clippy | rustc and cargo 1.91.1 | Stages 3, 4 and 5 (the numerical programs) |
| PowerShell 7 (on Windows) | 7.6.6 | the `.ps1` gates |

On macOS and Linux the Bash twins are used and PowerShell is not needed; there, TeX Live takes the place of MiKTeX. Python, Git, Rust and a TeX distribution are free programs; WolframScript needs an installed and activated Wolfram Engine or Mathematica. Without WolframScript the Stage-3 and Stage-4 gates skip their Wolfram steps and say so in their output; the Stage-1 and Stage-2 gates stop with a message that WolframScript was not found.

**Installing the Python packages.** The file `requirements-stage3.txt` in the repository root pins six of the packages; the seventh, nbconvert, is needed by the notebook steps of the Stage-3 and Stage-4 gates. In either shell, from the repository root:

```
python -m pip install -r requirements-stage3.txt
python -m pip install nbconvert==7.16.6
```

With other versions of the packages every check still passes, but the last digits of some files written by Python (for example the EXP-3 fits and the executed notebooks) can differ from the committed ones, and then the byte-for-byte comparisons of the Stage-3 gate fail (student guide, §3.5 and §14). On macOS and Linux, install the packages into a virtual environment, as the student guide explains in its §3.5.

**Checking the tools.** Each tool reports its version. In either shell:

```
git --version
python --version
python -c "import numpy, sympy; print(numpy.__version__, sympy.__version__)"
wolframscript -version
pdflatex --version
cargo --version
```

On the test computer these printed, in order, `git version 2.51.2.windows.1`, `Python 3.14.5`, `2.4.6 1.14.0`, `WolframScript 1.14.0 for Microsoft Windows (64-bit)`, a first line containing `MiKTeX-pdfTeX 4.27 (MiKTeX 26.5)` and `cargo 1.91.1 (ea2d97820 2025-10-10)`. In PowerShell, `$PSVersionTable.PSVersion` shows the version of PowerShell itself (here 7.6.6).

### 19.3 Two shells: PowerShell and Bash

**What a shell is.** A shell is a program in which you type commands, one per line; pressing Enter runs the command. The shell always works in one folder, the **current folder**; a file named without a folder, such as `README.md`, means the file of that name in the current folder, and a **relative path** such as `scripts/setup_solver.sh` means the file `setup_solver.sh` in the subfolder `scripts` of the current folder. Every command of this appendix is to be typed in the **repository root**, the folder that contains `README.md`. A program ends with an **exit code**, a whole number: 0 means success, anything else means failure. PowerShell shows the exit code of the last program when you type `$LASTEXITCODE`; Bash shows it when you type `echo $?`.

**Six differences that matter here.**

1. *Running a script.* In PowerShell a script in the current tree is run by its path, `.\scripts\setup_solver.ps1`, or, for the gates, by PowerShell 7 explicitly: `pwsh -NoProfile -File scripts/verify_stage2_primordial_field.ps1`. In Bash a script is given to the Bash program: `bash scripts/setup_solver.sh`.
2. *Environment variables.* An environment variable is a named setting that programs started from the shell can read. PowerShell sets one with `$env:PYTHONUTF8 = "1"`, Bash with `export PYTHONUTF8=1`. The setting lasts until the shell is closed. `PYTHONUTF8=1` makes Python read and write text as UTF-8, so that Greek letters in the output of the checkers survive; the gates set it themselves, and for single commands you set it once per shell.
3. *Continuing a long command.* A command that does not fit on one line can be continued: in PowerShell the line ends with a backtick character (the grave accent) after a space, in Bash with a backslash. Every command box of this appendix whose lines end in one of these two characters is one single command.
4. *Program names.* On Windows a compiled program ends in `.exe`, and PowerShell runs a program whose path is stored in a variable with the call operator `&`, as in `& $bin exp5`. In Bash the `.exe` may be left out in Git Bash and does not exist on macOS and Linux.
5. *Paths.* Python, cargo and WolframScript accept forward slashes on every system, so the paths inside the commands are written with `/` in both shells.
6. *Windows PowerShell 5.1.* Windows also contains an older PowerShell, version 5.1, started by the command `powershell`. The gates need PowerShell 7 (the command `pwsh`); started from version 5.1, each gate starts itself again under PowerShell 7 and passes on its exit code, or stops with a message if PowerShell 7 is not installed (header of each `.ps1` gate).

**Worked example.** Setting the environment variable and counting the checks of a report, first in PowerShell:

```
$env:PYTHONUTF8 = "1"
python -c "
import json, sys
c = json.load(open(sys.argv[1], encoding='utf-8'))['checks']
print(sum(c.values()), len(c))
" artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
```

The lines from `python -c "` to the closing `"` and the path after it form one command: the three lines between the double quotes are a small Python program, which Python receives as one piece of text, and the path after the closing quote is handed to that program as `sys.argv[1]` (the first word after the program). Both shells allow a quoted text to continue over several lines, so in Bash only the first line differs:

```
export PYTHONUTF8=1
```

Both shells print `141 141`: all 141 checks of the Stage-5 pairing report are true. This is the method of Section 0.8 written as one command; replace the path to count the checks of any other report.

### 19.4 A fresh clone and the numerical engine

**Cloning.** A **clone** is a complete copy of the repository, with its whole history, made by Git. Choose a folder for it and type, in either shell:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
git log --oneline -1
```

The first command downloads the repository into the new folder `Dirac_claude` (about 410 megabytes; 31 seconds on the test computer), the second makes that folder the current folder, and the third prints the commit you have, a short hexadecimal name followed by its message. All later commands are typed in this folder. Some folders are deliberately missing from a clone: `build/` (scratch output), `vendor/` (the numerical engine, fetched below) and the private reference folder `dirac-main/` of Stage 1 (Section 19.6). The file `.gitignore` lists them, and Git never records their contents.

**The numerical engine.** The Rust programs of Stages 3, 4 and 5 use CVODE, the solver of the pure-Rust translation of SUNDIALS 7.8.0 (Chapter 10). It is not stored in this repository; a setup script downloads it at a fixed commit (a **pin**) into `vendor/rustSolveIt`. PowerShell:

```
.\scripts\setup_solver.ps1 -Platform win11
```

Bash (Git Bash, macOS, Linux):

```
bash scripts/setup_solver.sh win11
```

Expected output of the first run (6 seconds on the test computer):

```
solver_platform=win11
solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3
solver_setup=OK
```

A second run finds the engine and prints `solver_setup=ALREADY-PRESENT` instead of `solver_setup=OK`. If the folder holds a different commit, the script refuses to continue and asks you to remove `vendor/rustSolveIt` and run it again; an interrupted download is reported in the same way. If PowerShell refuses to run the script with the message that running scripts is disabled on this system, run it as `pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11`; the option `-ExecutionPolicy Bypass` applies to this one command only.

**Which engine.** There are three engines, `win11`, `macos` and `linux`, in three repositories (Section 10.9 lists their pinned commits). The committed numerical files were produced with the `win11` engine, and that engine reproduces them byte for byte on Windows and on Linux; the `macos` and `linux` engines contain a different mathematical library, so with them all checks pass but some files differ in their last digits (Section 10.10; `README.md`, section "Reproducing"). This is why every command of this appendix, and every gate, uses `win11`, also on macOS and Linux. Without an argument the Bash script chooses the engine from the operating system, which is not what the byte comparisons need.

### 19.5 Reading what a verifier prints, and rerunning one without touching committed files

**Verifiers and checkers.** A **verifier** in this book is a program that recomputes exact statements and writes a report; the Wolfram Language ones are called verifiers (file names `scripts/verify_*.wls`), the independent Python ones checkers (`scripts/check_*.py`). Every one of them prints a line for each check and for each measurement (some also print progress lines with the elapsed time) and ends with two summary lines:

```
check_ALG_clifford=true
check_ALG_gammaTransposeSymmetry=true
...
measurement_ALG_cliffordPairsVerified=64
measurement_ALG_chargeMatrixSignature=[8,8,0]
...
check_count=20
failed_check_count=0
```

(This is the Python algebra checker of Stage 1; `...` marks omitted lines in every output box of this appendix.) A check is a statement that is either true or false; a measurement is a recorded value, such as a count or a matrix; here 64 ordered pairs of gamma matrices were tested and the charge matrix has 8 positive, 8 negative and 0 zero eigenvalues. The program exits with code 0 when every check is true and with a nonzero code otherwise (some verifiers also refuse, with a nonzero code, when the number of checks differs from the number they expect). The same checks and measurements are written into the report, a JSON file whose entry `checks` holds the true or false values (Section 0.8).

**What a gate prints.** A gate prints the tools it found (lines `stageN_tool_...=`), then for each step a line `stageN_step=<name>` when the step starts and `stageN_step_ok=<name>` when it has succeeded, with the full output of the step in between. After the steps it audits the reports and prints their check counts and the sha256 of every output file (the **sha256** is a 64-digit hexadecimal fingerprint of a file's bytes: two files have the same sha256 exactly when they are byte-identical, for every practical purpose). The last line is the verdict. When a step fails, the gate stops and prints instead, for example in Stage 2,

```
stage2_failed_step=stage2-02-check-primordial
stage2_failed_log=build/logs/stage2-02-check-primordial-bash.log
stage2_primordial_field_verification=FAILED
```

and exits with a nonzero code; the other gates print the same three lines with their own stage number and name. Every step writes its complete output into a **log file** in `build/logs/` (the Bash twins add `-bash` to the file name so that the logs of the two twins do not overwrite each other); the log begins with the start time and the command and ends with the finish time and the exit code.

**Rerunning one program into a scratch folder.** Many verifiers write their report into the committed folder by default. To check a single statement without changing any committed file, write the report into the folder `build/`, which Git ignores. Two rules make this work:

1. The Wolfram verifiers take the report path as a plain argument after the script name, never after a separator `--`: with WolframScript 1.14, `wolframscript -file s.wls -- r.json` loses the path, while `wolframscript -file s.wls r.json` passes it (the headers of all gates record this test). Some Wolfram verifiers also write a theory file next to the report; with a report path in `build/` that file goes to `build/` as well.
2. The Python checkers take the report path from an option, `--output` for most of them. Two Stage-1 programs write to a fixed path; for them the helper `scripts/run_with_report_path.py` redirects the report (Section 19.6).

After any rerun, `git status --short` lists every committed file that has changed; it prints nothing when all committed files are unchanged. To put the committed version of the artifacts back, type `git restore artifacts`.

**Worked example: one Stage-1 checker.** PowerShell:

```
$env:PYTHONUTF8 = "1"
python scripts/check_dirac16complex_algebra.py --wolfram-report= `
    --output build/textbook/python-algebra-report.json
```

Bash:

```
export PYTHONUTF8=1
python scripts/check_dirac16complex_algebra.py --wolfram-report= \
    --output build/textbook/python-algebra-report.json
```

Both print 20 check lines and end with `check_count=20`, `failed_check_count=0` and the line `report=build/textbook/python-algebra-report.json`; the committed report has 21 checks, because the empty option `--wolfram-report=` switches off the comparison with the Wolfram report (Section 2.16). On the test computer the run took 2 seconds, and `git status --short` printed nothing afterwards.

### 19.6 Stage 1: the field in an arbitrary gravitational field

**What the gate does.** The Stage-1 gate runs thirteen steps (header of `scripts/verify_stage1_arbitrary_field.sh`); each writes its log into `build/logs/`:

| Step | Command (from the log of the run described below) | Time |
| --- | --- | --- |
| `stage1-01-build-fixture` | `python scripts/build_dirac16complex_fixture.py --output build/stage1/algebra-fixture.json` | 3 s |
| `stage1-02-check-algebra` | `python scripts/check_dirac16complex_algebra.py --wolfram-report= --output build/stage1/python-algebra-report.json` | 7 s |
| `stage1-03-wolfram-algebra` | `wolframscript -file scripts/verify_dirac16complex_algebra.wls build/stage1/wolfram-algebra-report.json` | 49 s |
| `stage1-04-wolfram-geometry` | `wolframscript -file scripts/verify_dirac16complex_geometry.wls build/stage1/wolfram-geometry-report.json` | 535 s |
| `stage1-05-check-geometry` | `python scripts/run_with_report_path.py build/stage1/python-geometry-report.json scripts/check_dirac16complex_geometry.py --wolfram-report build/stage1/wolfram-geometry-report.json` | 337 s |
| `stage1-06-grassmann-demo` | `python scripts/run_with_report_path.py build/stage1/grassmann-demo-report.json scripts/demo_grassmann_lagrangians.py` | 43 s |
| `stage1-07-check-algebra-crosscheck` | `python scripts/check_dirac16complex_algebra.py --wolfram-report build/stage1/wolfram-algebra-report.json --output build/stage1/python-algebra-report.json` | 1 s |
| `stage1-08-python-tests` | `python -m unittest discover -s tests -p "test_d16c_[ag]*.py" -v` (99 tests) | 51 s |
| `stage1-09-publication-tests` | `python -m unittest discover -s tests -p test_publication_tooling.py -v` (68 tests) | 55 s |
| `stage1-10-summary` | `python scripts/build_stage1_summary.py --output build/stage1/stage1-summary.json --reports-directory build/stage1` | under 1 s |
| `stage1-11-provenance-pdf` | `python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` | 10 s |
| `stage1-12-publication-recheck` | `python -m unittest discover -s tests -p test_d16c_arbitrary_field_publication.py -v` (27 tests) | under 1 s |
| `stage1-13-public-clone-audit` | `python scripts/verify_stage1_public_clone_audit.py --committed artifacts/dirac16complex/arbitrary-field --regenerated build/stage1` | under 1 s |

Steps 02 and 07 run the same Python checker twice: first alone, then again with the comparison against the Wolfram algebra report that step 03 has just written (check `ALG_wolframAgreement`). Step 05 compares the Python geometry with the Wolfram geometry of step 04 (check `GEO_wolframAgreement`). The helper `scripts/run_with_report_path.py` is needed because the geometry checker and the Grassmann demonstration write their reports to a fixed path and have no output option; the helper runs the committed code unchanged and only redirects the report (its header explains why no option was added: the sha256 of the two scripts is recorded in the committed reports).

**Two modes: with and without dirac-main.** Three exact data files of the separately published reference implementation dirac-main (https://github.com/once-ere/dirac) are compared with the Stage-1 matrices (Chapter 3). The folder `dirac-main/` that would hold them is not part of this repository, so a fresh clone lacks it. The gate first prints `stage1_dirac_main=present` or `stage1_dirac_main=absent`. With `absent` it runs in the **public-clone mode**: every regenerated file goes into `build/stage1/` and the committed reports stay untouched; the verifiers record the dirac-main comparisons as "not-run"; and the extra step 13 requires every regenerated file to equal the committed one, byte for byte or value for value, except for exactly the entries that the missing folder changes (its log lists each allowed difference in a line `stage1_audit_allowed=`). With `present` the gate rewrites the committed reports in place, runs the dirac-main comparisons as well, and needs no step 13. Both modes were run from fresh public clones on 2026-09-30 and ended with the OK line: the Bash and PowerShell twins without dirac-main, and the Bash twin with a copy of the folder (`handoff/reviews/stage1_gate_2026-09-30_public_sh.log`, `..._public_ps1.log` and `..._private_sh.log`).

**Running it.** PowerShell:

```
pwsh -NoProfile -File scripts/verify_stage1_arbitrary_field.ps1
```

Bash:

```
bash scripts/verify_stage1_arbitrary_field.sh
```

The last lines of a successful run in the public-clone mode (sha256 values cut after 16 digits):

```
stage1_report_checks=build/stage1/wolfram-algebra-report.json 21 true
stage1_report_checks=build/stage1/wolfram-geometry-report.json 43 true
stage1_report_checks=build/stage1/python-algebra-report.json 21 true
stage1_report_checks=build/stage1/python-geometry-report.json 52 true
stage1_report_checks=build/stage1/grassmann-demo-report.json 16 true
stage1_sha256=39cc390b53266bda...  build/stage1/wolfram-algebra-report.json
...
stage1_sha256=83252f8478aa1f05...  provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf
stage1_skipped=dirac-main cross-checks (dirac-main/ is a git-ignored reference ...
stage1_arbitrary_field_verification=OK
```

The eight sha256 lines cover the five reports, `stage1-summary.json` and the `.tex` and `.pdf` of the Stage-1 document; the `stage1_skipped` line is longer on the screen and names the log in which the audit lists the comparisons that were not run. The five reports hold $21+43+21+52+16=153$ checks, the 153 of 153 of Chapter 0. The first sha256 differs from that of the committed Wolfram algebra report, and that is expected: the report records the dirac-main comparisons as "not-run", which is one of the allowed differences. The PDF line shows the sha256 of the registered edition, because the PDF is rebuilt byte for byte.

**Wall time.** The Bash twin, run for this edition from the fresh clone of Section 19.4 (public-clone mode), took 1133 seconds, about 19 minutes; the table above gives the time of each step. The two exact geometry programs dominate. In the committed runs of 2026-09-30 the Python geometry checker took 190 seconds (Bash) and 227 seconds (PowerShell) without dirac-main and 621 seconds with it (the line `runtime_seconds=` of each log), so the whole gate needs roughly 10 to 20 minutes, depending on the load of the computer.

**Single programs.** Each row of the table is an ordinary command and can be typed on its own, in either shell (after setting `PYTHONUTF8` as in Section 19.3); the gate's folder `build/stage1/` can be replaced by any folder below `build/`. The Wolfram verifiers print progress lines, their checks and measurements, and end with `check_count=21` (algebra) and `check_count=43` (geometry); the Python geometry checker ends with `check_count=52`, the Grassmann demonstration with `check_count=16`, all with `failed_check_count=0`. Run step 04 before step 05 and step 03 before step 07, because the later steps read the reports of the earlier ones.

### 19.7 Stage 2: the primordial field

**What the gate does.** The Stage-2 gate has four steps (header of `scripts/verify_stage2_primordial_field.sh`):

| Step | Program | What it does |
| --- | --- | --- |
| `stage2-01-wolfram-primordial` | `scripts/verify_dirac16complex_primordial.wls` | the exact Wolfram verifier of Chapter 9; writes `wolfram-primordial-report.json` and `primordial-components.json` |
| `stage2-02-check-primordial` | `scripts/check_dirac16complex_primordial.py` | the independent sympy checker; compares its field equations with the components written by step 1 |
| `stage2-03-python-tests` | `python -m unittest` with the files `tests/test_d16c_primordial*.py` | the unit tests of Stage 2 |
| `stage2-04-provenance-pdf` | `scripts/build_provenance_pdf.py` | rebuilds `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf` and compares it with the registered edition |

The gate writes its reports over the committed ones in `artifacts/dirac16complex/primordial-field/`; when everything agrees the new files are byte-identical, so `git status --short` shows nothing afterwards. It then requires every check to be true and requires the Python report to have compared its equations with the components of this very run.

**Running it.** PowerShell:

```
pwsh -NoProfile -File scripts/verify_stage2_primordial_field.ps1
```

Bash:

```
bash scripts/verify_stage2_primordial_field.sh
```

The last lines of a successful run (the folder `artifacts/dirac16complex/primordial-field/` is shortened to `.../` here, and each sha256 line ends with the file name):

```
stage2_step_ok=stage2-04-provenance-pdf
stage2_report_checks=.../wolfram-primordial-report.json 126 true
stage2_report_checks=.../python-primordial-report.json 16 true, wolframAgreement=compared
stage2_sha256=a0164273df62f2e1...  .../wolfram-primordial-report.json
stage2_sha256=a5d8caa8cb226082...  .../primordial-components.json
stage2_sha256=2d9cc593bd7812be...  .../python-primordial-report.json
stage2_sha256=c1cd3773ef2f15c4...  provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.tex
stage2_sha256=a6f6d7b813591412...  provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf
stage2_primordial_field_verification=OK
```

(the sha256 values are cut after 16 digits here; the gate prints all 64).

**Wall time.** The Bash twin, run for this edition from the fresh clone of Section 19.4, took 320 seconds: 142 for the Wolfram verifier, 9 for the Python checker, 74 for the 53 unit tests and 41 for the PDF, the rest for the audits. The committed logs of the earlier fresh-clone runs (`handoff/reviews/stage2_gate_2026-09-30_fresh_clone_OK.log` for Bash and `stage2_gate_ps1_2026-09-30_fresh_clone_OK.log` for PowerShell, both ending with the OK line) record 88 and 121 seconds for the Wolfram step and 32 seconds for the unit tests.

**Single programs.** To rerun the two verifiers into the scratch folder `build/textbook/stage2/`, in PowerShell:

```
$env:PYTHONUTF8 = "1"
$s = "build/textbook/stage2"
wolframscript -file scripts/verify_dirac16complex_primordial.wls `
    "$s/wolfram-primordial-report.json"
python scripts/check_dirac16complex_primordial.py `
    --output "$s/python-primordial-report.json" `
    --wolfram-components "$s/primordial-components.json"
```

and in Bash:

```
export PYTHONUTF8=1
s=build/textbook/stage2
wolframscript -file scripts/verify_dirac16complex_primordial.wls \
    "$s/wolfram-primordial-report.json"
python scripts/check_dirac16complex_primordial.py \
    --output "$s/python-primordial-report.json" \
    --wolfram-components "$s/primordial-components.json"
```

The variable `s` only abbreviates the folder. The Wolfram verifier prints one progress line per group of checks (from `zero-test sanity` to `P_a4linear`), then its checks and measurements, and ends with `check_count=126`, `failed_check_count=0` and `elapsed_seconds=`; it writes the report and, next to it, `primordial-components.json`. It took 79 seconds. The Python checker ends with `check_count=16` and `failed_check_count=0` after 10 seconds. The two Wolfram files it wrote were byte-identical to the committed ones.

### 19.8 Stage 3: the dark-sector experiments

**What the gate does.** The Stage-3 gate runs 32 steps (header of `scripts/verify_stage3_dark_sector.sh`). In groups:

| Steps | What they do |
| --- | --- |
| 00 | copy the committed Stage-3 files into `build/stage3/snapshot`, to prove at the end that they did not change |
| 01, 02 | install the `win11` engine (Section 19.4) and check that it is exactly the pinned commit, unmodified |
| 03 to 06 | `cargo fmt --check`, `cargo clippy` with every warning treated as an error, `cargo test --release`, `cargo build --release` for the crate `studies/dirac16complex_cosmology` |
| 07, 08 | run all five experiments twice, into `build/stage3/run-a` and `build/stage3/run-b`; each run must end with `SUCCESS` |
| 09 | the 62 output files of the experiments must be byte-identical in both runs and in the committed folders `artifacts/dirac16complex/numerics/exp1/` to `exp5/` |
| 10, 11 | the EXP-3 fit analysis `scripts/analyze_dirac16complex_exp3.py`, compared with the committed fit files |
| 12 to 17 | the five independent checkers `scripts/check_dirac16complex_exp1.py` to `..._exp5.py`, each with a repeat run and a run with tightened tolerances, and an audit of their reports |
| 18, 19 | the collected summary `numerics-summary.json`, compared with the committed one |
| 20 to 25 | the Jupyter notebook, executed twice without any stored output, audited, and required to rewrite the committed figures byte for byte |
| 26, 27 | the Mathematica notebook (skipped without WolframScript) |
| 28, 29 | the two Stage-3 PDFs, rebuilt and compared with their registered editions |
| 30 to 32 | every snapshotted file unchanged; all unit tests of the repository; every output written during this run |

**Running it.** It needs everything of Section 19.2 except that WolframScript is optional. PowerShell:

```
pwsh -NoProfile -File scripts/verify_stage3_dark_sector.ps1
```

Bash:

```
bash scripts/verify_stage3_dark_sector.sh
```

A successful run ends with

```
stage3_audit_fresh=OK
stage3_step_ok=stage3-32-fresh-outputs
stage3_dark_sector_verification=OK
```

Without WolframScript, two more lines appear: `stage3_skipped_step=stage3-26-mathematica-notebook,...` where step 26 would run, and `stage3_mathematica=SKIPPED (...)` just before the final line, which then still reads OK, because every other step passed.

**Wall time, and the state at this edition's commit.** The Bash twin took 28 minutes from a fresh clone of commit `1fb83c3` on 2026-09-30, from 06:09 to 06:37, including 316 seconds for the 323 unit tests of that commit (`handoff/reviews/stage3_gate_2026-09-30_fresh_clone_OK.log`, which ends with the OK line). The PowerShell twin also ended with OK, from a fresh clone of commit `348c2e1` (`handoff/reviews/stage3_gate_ps1_2026-09-30_fresh_clone_OK.log`; that run was suspended for about 40 minutes at the user's request, so its duration is not a measurement). The two complete runs of the experiments (steps 07 and 08) and the notebook executions take most of the time; `README.md` summarizes it as "tens of minutes".

The gate was not repeated for this edition, and at commit `4cd47fe` it would not end with OK: its step 31 runs every unit test of the repository, and ten of the 578 tests of that commit fail. The failing tests belong to Stage 4 and to the matter–antimatter analysis, not to Stage 3 (Section 19.11). The programs, outputs, checkers and gates of Stage 3 did not change between the commit of the OK run and this edition's commit; the following command, in either shell, prints nothing:

```
git log --oneline 1fb83c3..4cd47fe -- studies/dirac16complex_cosmology \
    artifacts/dirac16complex/numerics scripts/verify_stage3_dark_sector.sh \
    scripts/verify_stage3_dark_sector.ps1 notebooks/dirac16complex_dark_sector.ipynb
```

(In PowerShell, end the continued lines with a backtick instead of the backslash.) The single programs below, run for this edition, reproduce every Stage-3 output file byte for byte.

**Single programs.** The student guide (`provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md`) explains the Stage-3 programs step by step and was itself tested by replaying all of its command boxes; here are the essential commands, run for this edition from the fresh clone after Section 19.4. Build the program (in either shell):

```
cd studies/dirac16complex_cosmology
cargo build --release
cd ../..
```

(20 seconds on the test computer; the last line of the output begins with `Finished`, and any compiler warning would stop the build, because the crate forbids warnings). Then run EXP-1 and EXP-5 into a scratch folder and check them, in PowerShell:

```
$env:PYTHONUTF8 = "1"
$bin = ".\studies\dirac16complex_cosmology\target\release\dirac16complex_cosmology.exe"
& $bin exp1 --output build/textbook
& $bin exp5 --output build/textbook
python scripts/check_dirac16complex_exp1.py --output build/textbook
python scripts/check_dirac16complex_exp5.py --output build/textbook
```

and in Bash:

```
export PYTHONUTF8=1
bin=./studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology
$bin exp1 --output build/textbook
$bin exp5 --output build/textbook
python scripts/check_dirac16complex_exp1.py --output build/textbook
python scripts/check_dirac16complex_exp5.py --output build/textbook
```

The program prints one line `PASS - name: detail` per self-check and ends with

```
exp1: solver_steps=33866 rhs_evaluations=34950 files=29 verdict=SUCCESS
SUCCESS
```

for EXP-1 (1 second) and with `exp5: solver_steps=2548 rhs_evaluations=4800 files=5 verdict=SUCCESS` and `SUCCESS` for EXP-5 (under 1 second). The 29 and 5 files it wrote into `build/textbook/exp1/` and `build/textbook/exp5/` were byte-identical to the committed ones. The checkers end with `check_count=23` (EXP-1, 2 seconds) and `check_count=19` (EXP-5, 5 seconds), each with `failed_check_count=0`. The committed checker reports have 25 and 21 checks: the two missing checks, `repeatByteIdentity` and `refinedConvergence`, need a repeat run and a run with tightened tolerances, which the checker performs itself when it is given the options `--repeat` and `--refined`, each followed by a scratch folder (student guide, §9). All five experiments at once:

```
$bin all --output build/textbook/all
```

(in PowerShell `& $bin all --output build/textbook/all`) ran 99 seconds on the busy test computer and wrote the 62 output files of the five experiments, every one byte-identical to the committed file of the same name; the student guide measured 80 to 90 seconds for the same run (its §7.4).

### 19.9 Stage 4: the Kohn–Sham states, and why its gate cannot pass yet

**What exists and what it gives.** Stage 4 (Chapter 13) has five layers. The state of each on 2026-09-30, read from the committed files:

| Layer | Program | Committed result |
| --- | --- | --- |
| exact theory, Wolfram | `scripts/verify_dirac16complex_kohn_sham.wls` | `wolfram-kohn-sham-report.json`: 125 of 125 checks true |
| exact theory, sympy | `scripts/check_dirac16complex_kohn_sham_theory.py` | `python-theory-report.json`: 157 of 157 checks true |
| Rust Kohn–Sham solver | `studies/dirac16complex_kohn_sham` | own checks all true: 33 (`spectrum`), 137 (`scf`), 65 (`excited`), 102 (`thermo`), 60 (`emt`), in the `summary.json` of each folder of `rust/`; a repeat run byte-identical in all 330 files compared, and a run with tolerances divided by 10 agreeing to $5.96\times10^{-8}$ relative in the energies of 65 runs and to $2.8\times10^{-8}$ in 364829 levels (`rust/determinism-report.json`, 4 of 4 checks true) |
| independent reference solver | `scripts/ks_reference_solver.py` | 56 runs in `reference/` (`reference/reference-summary.json`) |
| cross-checker, Rust against reference | `scripts/check_dirac16complex_kohn_sham.py` | `python-check-report.json`: 63 checks, 62 true, 1 false |

All files of the table lie in `artifacts/dirac16complex/kohn-sham/`. The one false check is `canonical_eigenvalues`. Its measurement `canonical_eigenvalues_detail` records 58412 comparisons of Kohn–Sham levels between the two solvers; the worst one, a deep level at $\varepsilon=-1.0537\,m$ of the smeared $N=1016$ ensemble at $-\hat\lambda_2$ (Section 13.11), differs by $2.195\times10^{-6}\,m$, while the tolerance there is $1.054\times10^{-6}\,m$ (ratio 2.08). All eight failing comparisons belong to this one run (four in its ground-state record and four in its excited-state record); every other run passes. The Delta-SCF excitation energy of that ensemble, which was the open comparison when Chapter 13 was written, now agrees within its tolerance (check `canonical_deltaSCF`, worst ratio 0.79), after the reference was run on twice finer grids for this one case (erratum E4.13 of `handoff/specs/STAGE4_SPEC.md`). The report also records one comparison that did not run, the reference solver's self-tests (`comparisonsNotRun`).

Two more Stage-4 reports belong to the notebooks: the Mathematica notebook's `mathematica-report.json` has 94 of 94 checks true, and the Jupyter notebook's `notebook-report.json` has 68 of 74 checks true and the verdict FAILURE. Its six false checks (their names begin with `gauntlet_` and `r07_`) repeat the cross-check comparisons as they stood when the notebook was last executed, before the reruns that closed the Delta-SCF comparison and before the final cross-check report existed (the notebook report itself records that it found `python-check-report.json` absent); the notebook has not been executed again since.

**Why the gate cannot pass yet.** The gate `scripts/verify_stage4_kohn_sham.{ps1,sh}` exists and was tested in parts, but it has never been run to the end. It cannot end with OK at present, for four reasons that the gate itself detects:

- Documents are missing. Step 00 copies every committed Stage-4 file that the gate must leave unchanged, among them `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.tex` and `.pdf` and the three files of the Stage-4 student guide `provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE`, and fails because these do not exist yet (the partial run below); steps 32 and 33 build the two PDFs and compare them with registered editions, and no Stage-4 edition is registered in `provenance/pdf-specifications.json`.
- The collected summary `artifacts/dirac16complex/kohn-sham/kohn-sham-summary.json`, with which step 23 compares its fresh summary, does not exist yet (its dry run below prints `missing now:` for it).
- Step 21 requires every check of the fresh cross-check report to be true, and `canonical_eigenvalues` is false.
- Step 35 runs the unit tests of Stage 4, and four of them, which test the committed report of the Jupyter notebook, fail (Section 19.11).

The numbers of Chapter 13 are therefore those of the Rust solver with its own checks and with the cross-check status just described.

**The dry run.** The option `-DryRun` (PowerShell) or `--dry-run` (Bash) prints every step with its expected wall time and its command, runs nothing, and ends with `stage4_kohn_sham_verification=DRY-RUN`:

```
pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1 -DryRun
```

```
bash scripts/verify_stage4_kohn_sham.sh --dry-run
```

It lists 37 steps, `stage4-00-snapshot` to `stage4-36-fresh-outputs`, and took 2 seconds. The header of the PowerShell twin explains each step and records the measured time of each part (its paragraph TIMING): about 4 hours in total, most of it in step 14, which recomputes the complete canonical Rust tree (about 3 hours, dominated by the `thermo` subcommand; an estimate, since this step has not yet been run as a whole).

**A partial run.** The option `-Steps` (PowerShell) or `--steps` (Bash) runs only the listed steps and then ends with `stage4_kohn_sham_verification=PARTIAL` and the exit code 3, never with OK. Steps 01 to 13 (engine, exact theory, generated constants, the four cargo steps and the configuration check) need no long Rust run:

```
pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1 `
    -Steps 01,02,03,04,05,06,07,08,09,10,11,12,13
```

```
bash scripts/verify_stage4_kohn_sham.sh \
    --steps 01,02,03,04,05,06,07,08,09,10,11,12,13
```

For this edition the Bash command was run from the fresh clone. All thirteen selected steps passed in 804 seconds, and the run ended with

```
stage4_selected_steps=01,02,03,04,05,06,07,08,09,10,11,12,13
stage4_kohn_sham_verification=PARTIAL
```

and the exit code 3. The exact Wolfram theory (step 03) took 20 seconds and the sympy theory (step 04) 199 seconds; step 05 found their four output files byte-identical to the committed ones; steps 06 to 08 regenerated the Rust file of exact constants, `studies/dirac16complex_kohn_sham/src/generated.rs`, and its report byte for byte; and step 11 ran the 49 Rust tests of the solver (47 passed, and the 2 timing probes that are marked to be skipped in a normal run were skipped). Step 11 took 522 seconds instead of the 35 to 79 seconds recorded in the header, because the computer was busy (Section 19.2). The PowerShell command, run afterwards in the same clone, also passed all thirteen steps and ended with the same two lines, after 430 seconds (step 11: 151 seconds). In both runs the log of step 11 contains one line that begins with `[ERROR]` and ends with `the right-hand side routine failed in an unrecoverable manner`. The engine prints such a line whenever one integration stops with an error; the solver is written to handle such errors (for example, the function `profile` in `studies/dirac16complex_kohn_sham/src/shooting.rs` repeats a failed integration with other settings), and the line `test result: ok. 47 passed; 0 failed; 2 ignored` shows that no test failed.

Step 00 is left out of the list because at this commit it fails. With the list `00,01,...,13` the same run stopped after 3 seconds. It first named the missing file, in the line `stage4_audit_problem=cannot snapshot missing file` followed by the path `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.tex`, and then printed

```
stage4_audit_snapshot=FAILED
stage4_failed_step=stage4-00-snapshot
stage4_failed_log=build/logs/stage4-00-snapshot-bash.log
stage4_kohn_sham_verification=FAILED
```

The snapshot step copies, among other files, the LaTeX and PDF files of the Stage-4 document and the Markdown, LaTeX and PDF files of the Stage-4 student guide, so that the gate can prove at the end that they did not change; none of these five files exists yet (the first reason above).

**Single programs.** The exact theory into a scratch folder, in PowerShell:

```
$env:PYTHONUTF8 = "1"
$k = "build/textbook/stage4"
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls `
    "$k/wolfram-kohn-sham-report.json"
python scripts/check_dirac16complex_kohn_sham_theory.py `
    --output "$k/python-theory-report.json" --table "$k/exchange-table.json"
```

and in Bash:

```
export PYTHONUTF8=1
k=build/textbook/stage4
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls \
    "$k/wolfram-kohn-sham-report.json"
python scripts/check_dirac16complex_kohn_sham_theory.py \
    --output "$k/python-theory-report.json" --table "$k/exchange-table.json"
```

These are the programs of steps 03 and 04 of the gate, with a scratch folder instead of `build/stage4/theory`. In the partial run above they printed `check_count=125` (Wolfram, 20 seconds) and `check_count=157` (sympy, 199 seconds), each with `failed_check_count=0`. The Wolfram verifier writes the theory file `kohn-sham-theory.json` next to its report, and the sympy checker writes the exchange table given after `--table`; all four files were byte-identical to the committed ones in `artifacts/dirac16complex/kohn-sham/`.

The Rust solver is built and run like the Stage-3 program (in either shell; in PowerShell call the program as `& $ks` with the path ending in `.exe`):

```
cargo build --release --manifest-path studies/dirac16complex_kohn_sham/Cargo.toml
ks=./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham
$ks print-config
$ks spectrum --output build/textbook/ks
```

The line `ks=...` is Bash; in PowerShell write `$ks = ".\studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe"`. For this edition the build, which compiles the engine and the solver, took 6 seconds, `print-config` ended with `SUCCESS`, and `spectrum` ran 37 seconds and ended with

```
spectrum: solver_steps=39152872 rhs_evaluations=47587645 files=15 verdict=SUCCESS
SUCCESS
```

Its 15 files in `build/textbook/ks/spectrum/` were byte-identical to the committed ones in `artifacts/dirac16complex/kohn-sham/rust/spectrum/`. The other subcommands, `scf`, `excited`, `thermo` and `emt`, take from minutes to hours (the TIMING paragraph named above); `all` runs the five of them.

### 19.10 Stage 5 and the matter–antimatter analysis

**What exists.** Stage 5 (Chapters 6, 7, 14 and 15) and the matter–antimatter analysis (Chapter 17) have no gate yet. Their exact theory is committed, each part in two independent implementations, and every check of the committed reports is true:

| Part | Program | Committed report (checks true) |
| --- | --- | --- |
| dirac16complex00, Wolfram | `scripts/verify_dirac16complex00.wls` with `wolfram/Dirac16Complex00.wl` | `wolfram-dirac16complex00-report.json` (46 of 46) and `dirac16complex00-theory.json` |
| dirac16complex00, sympy | `scripts/check_dirac16complex00.py` | `python-dirac16complex00-report.json` (49 of 49) |
| pairing theorems, Wolfram | `scripts/verify_dirac16complex_pairing.wls` with `wolfram/Dirac16ComplexPairing.wl` | `wolfram-pairing-report.json` (141 of 141) and `pairing-theory.json` |
| pairing theorems, sympy | `scripts/check_dirac16complex_pairing.py` | `python-pairing-report.json` (172 of 172) |
| matter and antimatter, Wolfram | `scripts/verify_dirac16complex_matter_antimatter.wls` with `wolfram/Dirac16ComplexMatterAntimatter.wl` | `wolfram-matter-antimatter-report.json` (44 of 44) and `matter-antimatter-theory.json` |
| matter and antimatter, sympy | `scripts/check_dirac16complex_matter_antimatter.py` | `python-matter-antimatter-report.json` (75 of 75) |

The Stage-5 reports lie in `artifacts/dirac16complex/pair-creation/`, the matter–antimatter reports in `artifacts/dirac16complex/matter-antimatter/`. The matter–antimatter document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` is written, and its PDF is registered in `provenance/pdf-specifications.json` (edition `dirac16complex-matter-antimatter`, 32 pages).

**What does not exist yet.** The two Stage-5 documents `provenance/DIRAC16COMPLEX00_FIELD_THEORY` and `provenance/DIRAC16COMPLEX_PAIR_CREATION` and the gate `scripts/verify_stage5_pair_creation.{ps1,sh}` planned in `handoff/specs/STAGE5_SPEC.md` (its §6) are not written. The Kohn–Sham demonstration of the pairing (Chapter 15) is **partial**:

- The Rust solver has the new subcommand `pairs` (file `studies/dirac16complex_kohn_sham/src/pairs.rs`). Its committed outputs, in `artifacts/dirac16complex/pair-creation/rust/pairs/`, cover 18 parameter sets of dirac16complex, each with the three universes $+M$, $-M$ and the $-M$ control and a file `pairing.json`: mass $m=1$ with $N=8$ at the five couplings $0,\pm\hat\lambda_1,\pm\hat\lambda_2$ ($T=0$) and $N=112$ at the same five couplings at $T=0$ and $T=0.1\,m$, and mass $m=3$ with $N=8$ at the couplings $0$ and $\pm\hat\lambda_1$. There are no committed Rust runs of dirac16complex00 and none with $m=3$, $N=112$.
- The reference runs of the independent solver (`scripts/ks_reference_pairs.py`, outputs in `artifacts/dirac16complex/pair-creation/reference/`) are marked incomplete in their summary `reference-pairs-summary.json` (entry `complete` is false): of the 49 runs recorded there, 17 converged (10 of dirac16complex, 7 of dirac16complex00), 2 did not converge, 6 failed and 24 were not attempted, and 131 runs of the planned matrix are listed as pending.
- The checker `scripts/check_dirac16complex_pairs.py` (Rust against reference, pairing identities, pair totals) exists, but no report of it is committed.
- One Stage-5 numerical report is complete: `artifacts/dirac16complex/pair-creation/rust/stage4-identity-report.json`, 9 of 9 checks true, which shows that adding the subcommand `pairs` left the Stage-4 outputs byte-identical (a fresh `spectrum` run and quick `scf` and `excited` runs).

**Rerunning the exact theory.** Into the scratch folder `build/textbook/s5`, in PowerShell:

```
$env:PYTHONUTF8 = "1"
$o = "build/textbook/s5"
python scripts/check_dirac16complex00.py `
    --output "$o/python-dirac16complex00-report.json"
python scripts/check_dirac16complex_pairing.py --output "$o/python-pairing-report.json"
python scripts/check_dirac16complex_matter_antimatter.py `
    --output "$o/python-matter-antimatter-report.json"
wolframscript -file scripts/verify_dirac16complex00.wls `
    "$o/wolfram-dirac16complex00-report.json"
wolframscript -file scripts/verify_dirac16complex_pairing.wls `
    "$o/wolfram-pairing-report.json"
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls `
    "$o/wolfram-matter-antimatter-report.json"
```

and in Bash:

```
export PYTHONUTF8=1
o=build/textbook/s5
python scripts/check_dirac16complex00.py \
    --output "$o/python-dirac16complex00-report.json"
python scripts/check_dirac16complex_pairing.py --output "$o/python-pairing-report.json"
python scripts/check_dirac16complex_matter_antimatter.py \
    --output "$o/python-matter-antimatter-report.json"
wolframscript -file scripts/verify_dirac16complex00.wls \
    "$o/wolfram-dirac16complex00-report.json"
wolframscript -file scripts/verify_dirac16complex_pairing.wls \
    "$o/wolfram-pairing-report.json"
wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls \
    "$o/wolfram-matter-antimatter-report.json"
```

The three Python checkers compare their own results with the committed Wolfram theory files (they never use them as truth, only in their agreement checks), so they can run first. Each Wolfram verifier writes its theory file next to its report, here into `build/textbook/s5/`. For this edition these six commands were run from the fresh clone, one after the other:

| Command | Wall time | Final lines | New files against the committed ones |
| --- | --- | --- | --- |
| `check_dirac16complex00.py` | 289 s | `check_count=49`, `failed_check_count=0` | report byte-identical |
| `check_dirac16complex_pairing.py` | 122 s | `check_count=172`, `failed_check_count=0` | report byte-identical |
| `check_dirac16complex_matter_antimatter.py` | 53 s | `check_count=77`, `failed_check_count=0` | report differs: two more checks (below) |
| `verify_dirac16complex00.wls` | 541 s | `check_count=46`, `failed_check_count=0` | report and theory file byte-identical |
| `verify_dirac16complex_pairing.wls` | 507 s | `check_count=141`, `failed_check_count=0` | report and theory file byte-identical |
| `verify_dirac16complex_matter_antimatter.wls` | 681 s | `check_count=44`, `failed_check_count=0` | report and theory file byte-identical |

Together they took 37 minutes on the busy test computer. Every check of every report was true, and eleven of the twelve new files were byte-identical to the committed files of the same name. The twelfth, the sympy report of the matter–antimatter analysis, has 77 checks instead of the committed 75: the checker of this commit contains two checks, `MA_M2_cpScopeInCurvedFields` and `MA_M4_imageFieldFockModel`, that the committed report does not have, and the 75 checks of the committed report are all present and true in the new one. The committed report was written by an earlier version of the checker: it records for its checker the sha256 `20914546...`, while the checker file of this commit has the sha256 `ef1a00dc...`. Regenerating the committed report is part of the unfinished work of the matter–antimatter analysis (Section 19.11).

**The matter–antimatter PDF.** In either shell:

```
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md
```

The builder converts the Markdown twice, runs pdflatex three times on each copy, requires both logs to be free of warnings and the two PDFs to be byte-identical, and compares the result with the registered edition (Section 19.12 describes it in detail). It ran 8 seconds and ended with

```
measurement_pageCount=32
...
check_count=14
failed_check_count=0
provenance_pdf=OK
```

and the rebuilt PDF was byte-identical to the committed one (sha256 `0b064200babdb2be...`).

### 19.11 The unit tests

**What they test.** Besides the verifiers, the repository contains unit tests in the folder `tests/`: small programs that test the tools (the Markdown converter, the PDF builder, the textbook assembler, the gates) and pin the committed evidence (for example, that the check counts, numbers and sha256 values quoted in a document agree with the reports). Python's module `unittest` finds and runs them. One file of tests, in either shell:

```
python -m unittest discover -s tests -p "test_d16c_textbook_assembler.py" -v
```

This runs the 34 tests of the textbook assembler (4 seconds) and ends with `OK`. The pattern after `-p` chooses the files; the gates use their own patterns (Sections 19.6 to 19.8). All tests of the repository:

```
python -m unittest discover -s tests -v
```

For this edition this command ran 578 tests in 1280 seconds (21 minutes) from the fresh clone and ended with

```
Ran 578 tests in 1280.371s

FAILED (failures=10, skipped=2)
```

The two skipped tests need the folder `dirac-main/` (Section 19.6). The ten failures lie in two files, and all of them concern committed records of unfinished work, not the tools or the results of Stages 1 to 3:

- Four tests of `tests/test_d16c_kohn_sham_notebook.py` test the committed report of the Stage-4 Jupyter notebook. Its verdict is FAILURE (Section 19.9); the file `artifacts/dirac16complex/kohn-sham/reference/reference-summary.json`, on which it depends, has changed since the report was written; and the report names an older way of executing the notebook. The notebook has to be executed again once the cross-check is settled.
- Six tests of `tests/test_d16c_matter_antimatter_publication.py` compare the matter–antimatter document with the files it cites. The sha256 values that the document records for its sympy checker, its Wolfram package, its Wolfram report and its theory file are those of earlier versions of these files (compare Section 19.10), and one status sentence of the Wolfram report now calls the cited Stage-5 values provisional until the Stage-5 gate passes, which the test does not yet expect. The document has to be updated to the current files.

Every test that the gates of Stages 1 and 2 run passed (Sections 19.6 and 19.7). The Stage-3 gate, however, runs all 578 tests in its step 31 and therefore cannot end with OK at this commit (Section 19.8), and the Stage-4 gate runs the four failing notebook tests in its step 35.

### 19.12 Building this textbook

**The two programs.** The book is written as 21 chapter files, one per chapter, in the folder of the first line below. The assembler (second line) checks them and joins them, with the title and the abstract, into the one Markdown file of the third line; the PDF builder (fourth line) turns that file into LaTeX and the LaTeX into the PDF:

```
provenance/textbook/chapters/     00-how-to-read.md ... 20-glossary-and-check-index.md
scripts/build_textbook.py         the assembler
provenance/DIRAC16COMPLEX_TEXTBOOK.md   the assembled book (.tex and .pdf beside it)
scripts/build_provenance_pdf.py   the PDF builder
``` In PowerShell:

```
python scripts/build_textbook.py
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md `
    --developer-layout --number-sections-from-zero
```

In Bash:

```
python scripts/build_textbook.py
python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md \
    --developer-layout --number-sections-from-zero
```

The option `--developer-layout` chooses the layout of the student guides (smaller tables with ragged right margins, code that may break inside long names), and `--number-sections-from-zero` makes LaTeX number the chapters from 0, as the book does; without it every chapter would be printed with a number one too high (the header of `scripts/build_dissertation_tex.py`).

**What the assembler checks.** Before it writes anything, the assembler runs up to fourteen checks and prints each as `check_<name>=true|false`: the chapter file names and numbers (00 to 20, no gaps, no duplicates), UTF-8 text with line feeds only, exactly one heading `## N. Title` per chapter and headings `### N.M Title` numbered 1, 2, 3, ... in order, no section number twice, every internal reference of the form "Chapter N" or "Section N.M" pointing to an existing chapter or section, and the Markdown convertible by the LaTeX converter (tables with equal numbers of cells, code lines of at most 89 characters, figures that exist). Only when all of them pass does it write the output; it then prints the output path, its size and its sha256, and ends with `textbook_assembly=OK`. The output depends only on the chapter files and on the assembler, so two runs give the same bytes. Three options change what it does:

- `--check` runs the checks and writes nothing;
- `--check --allow-missing` accepts a book whose planned chapters are not all written yet: it reports each missing chapter, reports the references into missing chapters as "pending" instead of failing, and (without `--check`) writes a draft into `build/textbook/` instead of `provenance/`;
- `--check --verify-output` also requires the existing `provenance/DIRAC16COMPLEX_TEXTBOOK.md` to equal the assembly byte for byte.

For this edition the assembler ran from the fresh clone of Section 19.4 with `--check --allow-missing` in less than a second; the clone contained the twelve chapters then committed, and the run ended with `check_count=10`, `failed_check_count=0` and `textbook_assembly=OK`, after listing the chapters and references that were still missing.

**What the PDF builder checks.** For a Markdown file `D/X.md` the builder (its header lists the steps) converts the file twice, into `D/X.tex` and a second copy, with two different settings of Python's hash seed, and requires the two to be byte-identical; runs pdflatex three times on each copy, in two fresh folders below `build/X/`; searches both final logs for warnings (lines containing `LaTeX Warning`, a package warning, `Overfull`, `Underfull` or `Undefined control sequence`, or beginning with the error mark `!`) and fails on any; requires the two PDFs to be byte-identical and to have US-letter pages; and, in its default **verify mode**, compares the page count and the sha256 of the PDF with the edition registered for this file in `provenance/pdf-specifications.json`. Only then does it copy the PDF to `D/X.pdf` and print `provenance_pdf=OK`. The PDF is reproducible because the LaTeX preamble written by the converter switches off everything that would make two runs differ: the date, the random file identifier and the compression of the PDF objects.

**Registering an edition.** After an edit of the book the maintainers rebuild it with the option `--register`, which writes the new page count and sha256 into the registry instead of comparing with it, and then update the sha256 pins of the book's publication test (`tests/test_d16c_textbook_publication.py`, planned by `handoff/specs/TEXTBOOK_SPEC.md`, §2). A reader never needs `--register`: in verify mode a rebuilt book must reproduce the registered edition byte for byte, and that is the check. Until the textbook edition is registered, the verify mode reports its registry checks as failed while all other checks can pass.

For this edition the same command was run on the draft of the twelve chapters committed at that time, assembled with `--allow-missing` into `build/textbook/DIRAC16COMPLEX_TEXTBOOK.md` (in Bash: `python scripts/build_textbook.py --allow-missing`, then the builder with that path). It took 49 seconds and produced a PDF of 311 pages; both pdflatex logs were free of warnings and the two PDFs were byte-identical. As expected for a file without a registered edition, it ended with

```
check_count=14
failed_check_count=5
failed_checks=editionRegistered,registeredPath,registeredPageCount,registeredSha256,...
```

(the fifth failed check, `provenancePdfCopy`, means that the PDF is not copied to its final place when a check fails), and with the exit code 1.

### 19.13 A complete session from a fresh clone

The commands below collect, in order, the gates and checks of this appendix. They assume the tools of Section 19.2. PowerShell:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
python -m pip install -r requirements-stage3.txt
python -m pip install nbconvert==7.16.6
.\scripts\setup_solver.ps1 -Platform win11
pwsh -NoProfile -File scripts/verify_stage1_arbitrary_field.ps1
pwsh -NoProfile -File scripts/verify_stage2_primordial_field.ps1
pwsh -NoProfile -File scripts/verify_stage3_dark_sector.ps1
pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1 -DryRun
python scripts/build_textbook.py --check
git status --short
```

Bash (Git Bash, macOS, Linux):

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
python -m pip install -r requirements-stage3.txt
python -m pip install nbconvert==7.16.6
bash scripts/setup_solver.sh win11
bash scripts/verify_stage1_arbitrary_field.sh
bash scripts/verify_stage2_primordial_field.sh
bash scripts/verify_stage3_dark_sector.sh
bash scripts/verify_stage4_kohn_sham.sh --dry-run
python scripts/build_textbook.py --check
git status --short
```

Then run the partial Stage-4 gate and the single programs of Sections 19.9 and 19.10 for Stages 4 and 5 and the matter–antimatter analysis. Expected results at commit `4cd47fe`: the Stage-1 and Stage-2 gates end with their OK lines after about 20 and 5 minutes; the Stage-3 gate runs for about half an hour and stops in its step 31 with `stage3_dark_sector_verification=FAILED`, because of the ten failing unit tests of Section 19.11 (at a commit where they pass, it ends with OK, as it did at the commits of its committed logs); the Stage-4 dry run ends with `DRY-RUN`; the assembler ends with `textbook_assembly=OK` once all 21 chapters are committed (before that, add `--allow-missing`); and the last command prints nothing, because the gates write their work into the git-ignored folder `build/`, and every committed file that a gate rewrites in place (the Stage-2 gate rewrites its reports and its PDF) is rewritten with the same bytes. The full Stage-4 gate, which would take about 4 hours, cannot pass yet (Section 19.9), and Stage 5 has no gate yet (Section 19.10).

### 19.14 What we proved and what we assumed

This appendix proves no theorem. It records **measurements of reproducibility**, each made for this edition from a fresh public clone of commit `4cd47fe` on the test computer of Section 19.2, or quoted from a committed log or script header that is named where it is used: the Stage-1 and Stage-2 gates ended with their OK lines (after 1133 and 320 seconds); the Stage-2 verifiers, the Stage-3 programs and checkers, steps 01 to 13 of the Stage-4 gate and its `spectrum` subcommand, the six exact programs of Stage 5 and the matter–antimatter analysis, and two PDFs were rerun, and every file that should be byte-identical was byte-identical, except the one sympy report of the matter–antimatter analysis explained in Section 19.10; and the complete unit-test suite ran 578 tests, of which 10 failed and 2 were skipped (Section 19.11). It also records, from the committed files and these runs, the **state of the stages**: Stages 1 and 2 are complete, and the Bash twins of their gates passed at this commit; Stage 3 is complete and its gate passed at earlier commits, but at this commit its unit-test step fails for reasons outside Stage 3; the Stage-4 gate cannot pass yet, for the four reasons of Section 19.9, among them one false check of the cross-checker; Stage 5 has its exact theory but only part of its Kohn–Sham numerics, no documents and no gate; and the committed records of the matter–antimatter analysis (its sympy report and the hashes quoted in its document) lag behind its current files.

It **assumes**: that the tools behave as their versions say (a different version of Python's packages, of pdflatex or of the Rust compiler can change the last digits or bytes of some files without changing any check, as Sections 19.2 and 19.4 explain); that the `win11` engine is used for every byte comparison; that the reader's computer has the processor feature FMA (Section 10.10); and that the wall times, measured on a busy computer, are upper values for that computer and only indications for another. A byte-identical rerun shows that a program reproduces its committed output; it does not show that the output is correct. Correctness rests on the derivations of the chapters and on the independent checks named there.

### 19.15 Exercises

**Exercise 19.1.** Rewrite this Bash command for PowerShell:

```
export PYTHONUTF8=1
python scripts/check_dirac16complex_exp3.py \
    --output build/textbook
```

**Exercise 19.2.** A run of the Stage-3 gate ends with

```
stage3_failed_step=stage3-09-compare-outputs
stage3_failed_log=build/logs/stage3-09-compare-outputs-bash.log
stage3_dark_sector_verification=FAILED
```

What did the failed step compare, what is the most likely cause when every earlier step passed, and is any number of Chapter 11 wrong because of it?

**Exercise 19.3.** Use the one-command counter of Section 19.3 on the five Stage-1 reports of Section 19.6 and add the results. Which number of Chapter 0 do you obtain?

**Exercise 19.4.** Why does the Stage-1 gate write its reports into `build/stage1/` when the folder `dirac-main/` is missing, instead of into the committed folder as in the other mode?

**Exercise 19.5.** The Python algebra checker of Section 19.5 printed `check_count=20`, the committed report has 21 checks, and the EXP-5 checker of Section 19.8 printed `check_count=19` against 21. Name the missing checks in each case and say what has to be added to the command line to obtain them.

**Exercise 19.6.** Compute the sha256 of `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf` in both shells and compare it with the value registered for the edition `dirac16complex-matter-antimatter` in `provenance/pdf-specifications.json`.

**Exercise 19.7.** Add the step times of the Stage-1 run in the table of Section 19.6, counting the steps that took under a second as 0, and compare the sum with the total of 1133 seconds. Where did the rest of the time go?

**Exercise 19.8.** (a) The false Stage-4 check `canonical_eigenvalues` compares a difference of $2.195\times10^{-6}\,m$ with a tolerance of $1.054\times10^{-6}\,m$. Compute the ratio. (b) List the four reasons why the Stage-4 gate cannot end with OK today, and for each say what would have to be done.

**Exercise 19.9.** You changed one sentence of Chapter 7 and want to know, within a second and without building a PDF, whether every "Section N.M" reference of the book still resolves. Which command do you run, and which line of its output answers the question?

**Exercise 19.10.** A friend reruns the matter–antimatter checker from a fresh clone and reports: "77 checks, all true, but the committed report has 75: the repository is broken." Explain what the two numbers mean and whether the friend's conclusion is right.

### 19.16 Answers to the exercises

**Answer 19.1.** The environment variable is set with `$env:`, and the backslash at the end of a continued line becomes a backtick:

```
$env:PYTHONUTF8 = "1"
python scripts/check_dirac16complex_exp3.py `
    --output build/textbook
```

(The command is short enough to be written on one line as well.) Before it, run EXP-3 into the same folder, for example `& $bin exp3 --output build/textbook` with `$bin` from Section 19.8, and the EXP-3 analysis `python scripts/analyze_dirac16complex_exp3.py --output build/textbook`, because the checker reads their files (student guide, §9.3). In this order the three commands printed `SUCCESS`, `check_count=10` and `check_count=30` for this edition.

**Answer 19.2.** Step 09 compares the 62 output files of the five experiments, from the two complete runs of steps 07 and 08, with each other and with the committed files, byte for byte; its log names every file that differs. Steps 01 and 02 have already made sure that the pinned `win11` engine is installed and unmodified, and steps 07 and 08 ended with `SUCCESS`, so the program passed all its self-checks. The pinned engine is known to reproduce the committed files byte for byte on Windows 11 and on Ubuntu 24.04 (Section 10.10). A difference therefore points to one of three things: a system on which byte identity has not been established (for example macOS), a build that did not use the FMA setting of `.cargo/config.toml` (Section 10.10), or a committed file that was changed in the working tree (`git status --short` shows it). No number of Chapter 11 becomes wrong through such a difference: the self-checks and the independent checkers test the results against exact solutions and conservation laws, not against bytes, and a difference in the last digits is far below every tolerance. The byte comparison tests reproducibility, not correctness.

**Answer 19.3.** For the five reports in the folder `artifacts/dirac16complex/arbitrary-field/` the counter prints:

```
wolfram-algebra-report.json     21 21
wolfram-geometry-report.json    43 43
python-algebra-report.json      21 21
python-geometry-report.json     52 52
grassmann-demo-report.json      16 16
```

The sum is $21+43+21+52+16=153$: the 153 of 153 exact Stage-1 checks of the table in Section 0.5.

**Answer 19.4.** Without `dirac-main/` the verifiers cannot run the comparisons with the three dirac-main files and record them as "not-run". Their reports therefore differ from the committed ones in those entries and in the hashes that depend on them. Writing them over the committed reports would change committed evidence; writing them into `build/stage1/` keeps the committed files unchanged, and step 13 then proves that the regenerated reports agree with the committed ones everywhere except in exactly the entries that the missing folder explains.

**Answer 19.5.** The algebra checker lacks `ALG_wolframAgreement`, its comparison with the Wolfram algebra report; the empty option `--wolfram-report=` switches it off, and the option `--wolfram-report` followed by the path of a Wolfram report switches it on (step 07 of the Stage-1 gate). The EXP-5 checker lacks `repeatByteIdentity` and `refinedConvergence`. With the option `--repeat` followed by a folder below `build/`, the checker runs the program once more into that folder and requires every file to be byte-identical; with `--refined` followed by another folder, it runs the program with ten times tighter tolerances and requires the errors to shrink (student guide, §9.1). For example `python scripts/check_dirac16complex_exp5.py --output build/textbook --repeat build/repeat --refined build/refined`, written with a line continuation in either shell, printed `check_repeatByteIdentity=true`, `check_refinedConvergence=true` and `check_count=21` after 17 seconds for this edition.

**Answer 19.6.** PowerShell: `Get-FileHash -Algorithm SHA256 provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf` prints, in upper-case letters, `0B064200BABDB2BEE194E73CD0E0CAA4266D722D19E0CCE59CC8C543FC6BA6C3`. Bash: `sha256sum provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.pdf` prints the same 64 digits in lower case, followed by the file name (macOS: `shasum -a 256` instead of `sha256sum`). The registry entry holds `0b064200babdb2bee194e73cd0e0caa4266d722d19e0cce59cc8c543fc6ba6c3` and 32 pages: the same number, since upper and lower case denote the same hexadecimal digits.

**Answer 19.7.** $3+7+49+535+337+43+1+51+55+0+10+0+0=1091$ seconds. The remaining 42 seconds lie between the steps: the gate looks up the tools (on Windows through PowerShell), removes and creates `build/stage1/`, starts a new process for every step, audits the five reports with short Python programs and computes the eight sha256 values.

**Answer 19.8.** (a) $2.195/1.054=2.08$, the ratio recorded in the measurement `canonical_eigenvalues_detail`. (b) First, the Stage-4 document has no LaTeX file, no PDF and no registered edition, and the Stage-4 student guide does not exist (steps 00, 32 and 33): both documents have to be finished, built and registered. Second, `kohn-sham-summary.json` does not exist (step 23): it has to be generated from the final results and committed. Third, the fresh cross-check report must have all checks true (step 21), and `canonical_eigenvalues` is false for one level of the smeared $N=1016$ ensemble: the disagreement between the two solvers has to be resolved, by a finer computation that brings them together or by a justified tolerance for this case. Fourth, the Jupyter notebook has to be executed again, so that its committed report is current and all its checks are true, which the unit tests of step 35 require. Only after that can the gate run through step 14, the reproduction of the complete Rust tree (about 3 hours), to the OK line.

**Answer 19.9.** `python scripts/build_textbook.py --check` (add `--allow-missing` while chapters are missing). The line `check_crossReferencesResolve=true` answers it; any unresolved reference is printed before it as a line beginning with `problem=`. The option `--list-references` prints every reference with its classification.

**Answer 19.10.** The committed report was written by an earlier version of the checker, which had 75 checks; the checker in the same commit has two more, `MA_M2_cpScopeInCurvedFields` and `MA_M4_imageFieldFockModel`, and all 77 are true (Section 19.10). Nothing is broken in the sense of a false check: every committed check is reproduced as true, and two more checks pass. What the friend has found is that the committed report is not the newest one; regenerating it would change its check count and its recorded hashes, not any conclusion.
