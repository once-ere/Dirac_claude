# Execution provenance: the builder of the Stage-4 Kohn-Sham Mathematica notebook (WolframScript)

Set: `scripts/build_dirac16complex_ks_mathematica_notebook.wls`. It writes `notebooks/Dirac16ComplexKohnSham.nb` (old Stage 4, the Kohn-Sham density-functional study).

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` with Wolfram 15.0.1 and WolframScript 1.14.0 on Windows 11.

Verdict: **EXECUTES OK**. There were 16 successful builds from three fresh clones, in two shells (PowerShell 7 and Git Bash), with three ways of giving the output path. In all 16 builds the notebook written was **byte-identical** to the committed one.

A re-verification on the same day, in a fourth fresh clone (clone D, Part 6), repeated the builds, the checks and the measurements, and added Windows PowerShell 5.1. Every notebook it hashed was again byte-identical. It corrected these statements of the first version of this file: which Windows shell the checks need (Part 3.0), the processes WolframScript starts, the peak memory, the side effects outside the repository, the exit code when the script file is not found, the size of the printed output and the line count of the fix.

One execution defect was found and fixed. If the output file could not be written, the script printed error messages but still exited with code 0. The fix (Part 6) does not change the bytes of the notebook.

## 1. What this set is and what it computes

**In plain words.** Stage 4 of this repository studies `dirac16complex`, a field with 16 complex Grassmann components in eight dimensions (four space-like and four time-like directions). It places the field in the static member of the author's primordial gravitational field and treats it with Kohn-Sham density-functional theory. Density-functional theory replaces many interacting particles by single particles that move in an effective potential, and that potential is computed self-consistently.

* **The Rust program** `studies/dirac16complex_kohn_sham` does the numerical work. It finds every single-particle energy level by "shooting" with the CVODE differential-equation solver. It then repeats the Kohn-Sham equations, with Anderson mixing, until they agree with themselves.
* **The Mathematica notebook** `notebooks/Dirac16ComplexKohnSham.nb` checks those Rust results independently in the Wolfram Language.

**This set does not evaluate that notebook. It only writes the notebook file.** The script holds the code of every notebook cell as unevaluated Wolfram Language. It turns that code into typeset notebook cells and writes them to the `.nb` file. The output is repeatable: on the same Wolfram version, a later run gives exactly the same bytes.

A notebook is a plain text file. It holds one Wolfram Language expression, `Notebook[{cells...}, options...]`. You can open it with the free Wolfram Player, with the desktop product Wolfram (formerly Mathematica), or as text with any text editor.

**What the script does, step by step.**

1. It finds the repository root: the parent of the folder that holds the script. It does not use the folder you are in for this.
2. It reads the optional output path from the command line. If you give none, it writes to `notebooks/Dirac16ComplexKohnSham.nb` in the repository root. If the arguments contain a literal `--`, the script ignores it.
3. It builds 77 cells:
   * 1 title;
   * 9 section headings and 5 subsection headings;
   * 29 text cells (the explanations);
   * 33 Input cells (the code).

   Each Input cell is made from code written in the script, using `ToBoxes[Unevaluated[code], StandardForm]`. The code becomes boxes and is **never evaluated**.
4. It wraps the cells in `Notebook[...]` with these options:
   * the window title `dirac16complex Kohn-Sham DFT: Mathematica cross-check`;
   * the default style sheet `Default.nb`;
   * a `TaggingRules` entry that names the builder (`scripts/build_dirac16complex_ks_mathematica_notebook.wls`) and the verifier (`scripts/verify_dirac16complex_ks_mathematica_notebook.wls`), and sets `SchemaVersion -> 1`.
5. It writes the expression with `Put` and reads the file back as text. It changes Windows line ends (CR LF) to LF and removes spaces and tabs at the ends of lines. Then it writes the result again as UTF-8 bytes. The final file is pure ASCII, has LF line ends and has no newline after its last line.
6. It prints `cell_count=77`, `input_cell_count=33` and `output=<absolute path of the file>`, and exits with code 0. With the fix of Part 6, a failed write step instead prints `ERROR: could not write the notebook (...)` and exits with code 1.

**What the notebook does when it is evaluated.** This builder never evaluates it. That is done by a separate script, or by you in Mathematica. Its 33 Input cells are arranged in 9 sections (1, 1, 5, 3, 6, 5, 1, 7 and 4 Input cells). In order, they:

* load the Stage-1 geometry package `wolfram/Dirac16ComplexGeometry.wl` and the Stage-4 package `wolfram/Dirac16ComplexKohnSham.wl`, and run the package's complete check suite `D16KSRun`. The committed report records 125 package checks.
* derive the geometry of the static field symbolically: `sqrt|g| = e^{6Hy}`, the Einstein tensor `H^2 diag(15,15,15,15,21,15,15,15)` and `R = -42 H^2`. They also derive the reduced Dirac equation and its exact block diagonalisation into eight 2 x 2 blocks, the real two-component form and the Pruefer-angle form with its boundary conditions. Each result is compared exactly with the constants of the Rust source file `studies/dirac16complex_kohn_sham/src/generated.rs`.
* solve the `k = 0`, `lambda = 0` box problem exactly, including the zero-mode splitting coefficient `c = 2/(1 + e^{-3})` at `m = H = 1`, `L = 3`.
* recompute, with `NDSolve` shooting, the six free-spectrum files and the two closed-shell tables of the Rust `spectrum/` output. The committed report records 2818 compared levels.
* run a self-consistent Kohn-Sham loop in the Wolfram Language for `N = 8`, `T = 0`, `L = 3`, `m = H = 1`. It compares the loop with the Rust run `m1_L3_N8_lamp2_T0`, including the complete spectrum of 788 levels of the final potential.
* run the compiled Rust program with the command `print-config`.
* draw 6 figures into `artifacts/dirac16complex/kohn-sham/figures/mathematica/`.
* write `artifacts/dirac16complex/kohn-sham/mathematica-report.json` with 94 checks. The committed report has 94 of 94 checks true and the verdict `SUCCESS`.

**The charge matrix.** Charge conjugation in this repository is a **matrix**. The notebook uses the 16 x 16 matrix `C = gamma^0 gamma^1 gamma^2 gamma^3` (the package symbol ``Dirac16Complex`Geometry`D16GeoC``) only for two things:

* to form the matrix `B = -i C gamma^4`;
* to form the scalar-density operator `B C`, which it checks to be `j sigma2` on every block.

The notebook applies no charge-conjugation operation to a field. `Conjugate[...]` appears only inside inner products of the form `chi^dagger M chi`, which give densities and currents.

Evaluating the notebook is the job of `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`, a different set with its own provenance file. That evaluation needs the compiled Rust program `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham` (`.exe` on Windows). **The builder needs none of this.**

**Documents and files that cite this set or its notebook.**

* `tests/test_d16c_kohn_sham_mathematica.py`:
  * The test `test_notebook_is_a_fresh_build` runs this builder into a temporary folder and requires the result to be byte-identical to the committed notebook. The test is skipped when `wolframscript` is not on the PATH.
  * The test `test_notebook_input_cell_count` requires 33 Input cells, no CR characters and no spaces at line ends.
* `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`: the verifier, which evaluates the notebook. It expects 33 Input cells (`expectedInputCount = 33`) and 94 checks (`expectedCheckCount = 94`).
* `scripts/verify_stage4_kohn_sham.ps1` and `scripts/verify_stage4_kohn_sham.sh`: the Stage-4 gates. Their step `stage4-30-mathematica-notebook` evaluates the committed notebook with the verifier. The gates never rebuild it.
* `artifacts/dirac16complex/kohn-sham/mathematica-report.json`: its `producer` field names this builder.
* `handoff/specs/STAGE4_SPEC.md`: lists the notebook with its builder and verifier as a Stage-4 deliverable.
* `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md`: the Stage-4 document. It cites checks of the notebook by name: `rustLabelSIsMinusJEigenvalue`, `realFormIsBlockODEWithSMinusJ`, `parityMinusIsTanPLMinusPOverM` and `splittingAtM1H1L3Is2Over1PlusExpMinus3`.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (with its `.tex` and `.pdf`), Section 19.9, and its chapter `provenance/textbook/chapters/19-reproducing-everything.md`. Both say: "the Mathematica notebook's `mathematica-report.json` has 94 of 94 checks true".

## 2. Files

| File | Role | sha256 | Lines |
| --- | --- | --- | --- |
| `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, as committed at `c2b33cc` (unchanged since commit `eac67e6` of 2026-09-30) | the script that was verified | `2bb0e133adfa86ff3ec8d63e49759e69d6fcb1a1c74805fc6aba7feccff1a982` | 999 (112327 bytes, ASCII, LF) |
| `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, with the exit-code fix of Part 6 (the version committed together with this file) | the script after the fix | `7432e599992eecab33a9caf62e5b7352c8a03e2d36d9eede86d66d9eab8868bb` | 1010 (113149 bytes, ASCII, LF) |
| `notebooks/Dirac16ComplexKohnSham.nb` (unchanged since commit `eac67e6`) | the only output (committed) | `7e91159dba0fd1875736e3101e69a2b174017b173539ad0df4b3348d4457b22f` | 5122 line-feed characters and no newline after the last line, so an editor shows 5123 lines (359236 bytes, ASCII) |

**Inputs.** The script reads no file of the repository except itself. It does not read the packages in `wolfram/`, the Rust outputs under `artifacts/dirac16complex/kohn-sham/rust/`, `generated.rs` or the Rust program. Those are read only when the notebook is *evaluated*, which this set never does.

The only other thing the output depends on is the Wolfram system. The way `ToBoxes` and `Put` format the cells, and wrap long lines (the longest line of the committed notebook has 79 characters), belongs to the Wolfram version (see Part 4.4).

**Outputs.** Exactly one file:

* By default, `notebooks/Dirac16ComplexKohnSham.nb`, which is overwritten.
* With the optional argument, the file you name. Missing folders are created.

## 3. How to run it

### 3.0 On Windows: use PowerShell 7

The Windows commands in this file were tested in **PowerShell 7** (version 7.6.6), the program `pwsh`. Windows 11 also comes with an older shell, **Windows PowerShell 5.1** (the program `powershell.exe`). Clicking "Windows PowerShell" in the Start menu usually opens that older shell.

* The build commands of Part 3.3 work in both shells.
* Windows PowerShell 5.1 does not pass on the double quotes `"` that stand *inside* a single-quoted argument. It does not protect them when it builds the program's command line, so they are lost on the way and the program never sees them. Checks 4 and 5 of Part 3.4 contain such inner quotes. In Windows PowerShell 5.1 they print error messages and wrong results, still with exit code 0 (Part 3.5).

So, on Windows:

1. **Install PowerShell 7** (once). In any terminal, type

   ```
   winget install --id Microsoft.PowerShell -e
   ```

   On 2026-10-02, `winget show` listed version 7.6.6.0 for this package. The installer itself was not run for this record, because PowerShell 7.6.6 was already installed. Instead of `winget`, you can download the `.msi` installer from https://github.com/PowerShell/PowerShell/releases.
2. **Open it.** Press the Windows key, type `pwsh` and press Enter, or choose "PowerShell 7" in the Start menu or in Windows Terminal.
3. **Check the version.** Type `$PSVersionTable.PSVersion` and press Enter. The column `Major` must show `7`. If it shows `5`, you are in Windows PowerShell 5.1: close it and open `pwsh`.

Git Bash, which is installed together with Git (Part 3.2), was also tested on Windows. In Git Bash you use the macOS and Linux commands. On macOS and Linux nothing in this part applies.

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs:

* the Wolfram Language *kernel*, the program that does the computing;
* *WolframScript*, the command `wolframscript`, which runs a script file with the kernel.

The verification used kernel version 15.0.1 and WolframScript 1.14.0. This builder starts one kernel. Just before the kernel, WolframScript also starts a short licence-information process, which ends before the kernel starts (Part 5).

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser, open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page. Create both when asked, and read the licence terms.
2. Install it:
   * **Windows:** run the downloaded installer and accept the defaults. Instead, in PowerShell, you can type `winget install --id WolframResearch.WolframEngine -e`. On 2026-10-02, `winget show` listed version 15.0.0 for this package; the installer itself was not run for this record. The installer also installs WolframScript and adds it to the PATH. Afterwards, close every PowerShell window and open a new one.
   * **macOS:** open the downloaded `.dmg` file and follow its instructions: drag the application into Applications and open it once.
   * **Linux:** open a terminal in the download folder, run `sudo bash <name of the downloaded file>.sh` and accept the defaults.
   * **If `wolframscript` is "not recognized" or "not found"** after the installation (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/, then open a new terminal. The download is:
     * a `.msi` file for Windows;
     * a `.pkg` file for macOS;
     * for Linux, a `.deb` file (install with `sudo apt install ./<file>.deb`) or a `.rpm` file (install with `sudo dnf install ./<file>.rpm`).
3. Activate it. In a terminal (PowerShell on Windows, Terminal on macOS and Linux), type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. If you see the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.

**Option 2: Wolfram (formerly Mathematica), the desktop product.**

* A licensed Wolfram or Mathematica installation contains the kernel. On Windows and Linux it also installs `wolframscript`.
* Start the desktop program once to activate it.
* If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/, as in step 2 above.
* With the desktop product you can also open the built notebook in a notebook window (Part 4.3).

**Test the installation.** In a new terminal, type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine.

* The single quotes matter on macOS and Linux, because they stop the shell from replacing `$Version`. They are also correct in PowerShell 7 and in Windows PowerShell 5.1. This command has no double quotes inside the single quotes, so the problem of Part 3.0 does not arise.
* `wolframscript -version` prints the WolframScript version, for example `WolframScript 1.14.0 for Microsoft Windows (64-bit)`.
* If several versions are installed, `wolframscript` uses the newest one. `wolframscript -configure` prints the kernel it uses.

### 3.2 Get the repository

**Install Git** if you do not have it:

* Windows: https://git-scm.com/download/win, or `winget install --id Git.Git -e`;
* macOS: type `xcode-select --install` in Terminal;
* Debian or Ubuntu Linux: `sudo apt install git`.

Then, in the folder where you want the repository, type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

On the verification machine the clone took 8.3 seconds. The Git data was 128 MB, and the clone occupied about 520 MB on disk (measured on 2026-10-02).

Type every command below in this folder, the *repository root*: the folder that contains `scripts`, `notebooks` and `wolfram`.

The repository stores every file byte for byte. Its `.gitattributes` file turns off line-end conversion (`* -text`), even when Git is set up with `core.autocrlf=true`, as it was on the verification machine. So the checked-out notebook has exactly the committed bytes.

### 3.3 Run it

The usage line in the script's header is

```
wolframscript -file scripts/build_dirac16complex_ks_mathematica_notebook.wls [output.nb]
```

The square brackets mean that the output path is optional. You do not type the brackets.

**Windows, PowerShell 7** (tested with PowerShell 7.6.6; these two lines also work in Windows PowerShell 5.1, tested with 5.1.26100.9444):

```
wolframscript -file scripts/build_dirac16complex_ks_mathematica_notebook.wls
$LASTEXITCODE
```

**macOS Terminal (zsh) or Linux terminal (bash)**, and also Git Bash on Windows (tested):

```
wolframscript -file scripts/build_dirac16complex_ks_mathematica_notebook.wls
echo $?
```

The second line prints the exit code, which must be `0`. **But exit code 0 alone does not prove success.** If WolframScript cannot find the script file, for example because you are not in the repository root, it prints only

```
Failed to open file at path: scripts/build_dirac16complex_ks_mathematica_notebook.wls
```

and still gives exit code 0, without writing anything. A run has succeeded only if it prints the three lines of Part 4.1.

The run takes about 2 to 7 seconds, depending on how busy the computer is (Part 4.4). To time it:

* in PowerShell, type `Measure-Command { wolframscript -file scripts/build_dirac16complex_ks_mathematica_notebook.wls | Out-Host }`;
* in bash or zsh, put `time ` in front of the command.

This default run **overwrites the committed notebook** `notebooks/Dirac16ComplexKohnSham.nb` with the newly built one. With Wolfram 15.0.1 the new file is byte-identical to the committed one, so Git sees no change. Part 5 says how to restore the file if it does change.

**Recommended for students: write the notebook to a scratch folder instead.** Then the committed file is never touched, and you can compare the two files. Git ignores the folder `build/` (rule `/build/` in `.gitignore`), and the script creates missing folders itself. The command is the same in all three shells:

```
wolframscript -file scripts/build_dirac16complex_ks_mathematica_notebook.wls build/rebuilt/Dirac16ComplexKohnSham.nb
```

Notes on this command:

* A relative output path is taken relative to the folder you are in, so run the command from the repository root, as shown.
* You may put `--` before the output path (`... .wls -- build/rebuilt/Dirac16ComplexKohnSham.nb`), but you do not need to.
* The verifier's header says that WolframScript 1.14 drops the arguments after `--`. For this builder that did not happen: the path after `--` arrived and was used, in Git Bash, in PowerShell 7.6.6 and in Windows PowerShell 5.1 (Part 6).

### 3.4 Check the result

Each of the following checks must succeed after a default run. After a run with an output path, put that path in place of `notebooks/Dirac16ComplexKohnSham.nb`.

1. **The printed lines and the exit code** must be as in Part 4.1.
2. **The sha256 fingerprint** of the file must be `7e91159dba0fd1875736e3101e69a2b174017b173539ad0df4b3348d4457b22f`. To print it:
   * Windows, PowerShell 7 or Windows PowerShell 5.1: `(Get-FileHash notebooks/Dirac16ComplexKohnSham.nb -Algorithm SHA256).Hash`. PowerShell prints the fingerprint in capital letters, `7E91159DBA0F...`; that is the same value.
   * macOS: `shasum -a 256 notebooks/Dirac16ComplexKohnSham.nb`
   * Linux and Git Bash: `sha256sum notebooks/Dirac16ComplexKohnSham.nb`
3. **Git sees no change** (after a default run). The command

   ```
   git status --porcelain -- notebooks/Dirac16ComplexKohnSham.nb
   ```

   must print nothing. Also, `git diff --quiet -- notebooks/Dirac16ComplexKohnSham.nb` must give the exit code 0 (shown by `$LASTEXITCODE` in PowerShell and by `echo $?` in bash and zsh). Git never shows a change of a `.nb` file line by line, only as "binary", because of the rule `*.nb -diff` in `.gitattributes`.
4. **The structure of the notebook** (optional). This command prints the head, the number of cells, the number of cells of each style and the tagging rules:

   ```
   wolframscript -code 'nb = Get["notebooks/Dirac16ComplexKohnSham.nb"]; {Head[nb], Length[nb[[1]]], Tally[nb[[1, All, 2]]], Lookup[Options[nb], TaggingRules]}'
   ```

   The expected output is one line (tested in PowerShell 7.6.6 and Git Bash):

   ```
   {Notebook, 77, {{Title, 1}, {Text, 29}, {Section, 9}, {Input, 33}, {Subsection, 5}}, <|GeneratedBy -> scripts/build_dirac16complex_ks_mathematica_notebook.wls, VerifiedBy -> scripts/verify_dirac16complex_ks_mathematica_notebook.wls, SchemaVersion -> 1|>}
   ```

   **In Windows PowerShell 5.1 this command does not work as written** (Part 3.0). In version 5.1 the inner double quotes are lost. The kernel then prints `Get::stream: ... is not a string, SocketObject, InputStream[ ] or OutputStream[ ].` together with `Part::partd` and `Tally::listrp` messages. It also prints the wrong line `{Symbol, 2, Tally[$Failed[[1,All,2]]], Missing[KeyAbsent, TaggingRules]}`, and the exit code is still 0. Use PowerShell 7. If you must use Windows PowerShell 5.1, write every inner `"` as `\"`:

   ```
   wolframscript -code 'nb = Get[\"notebooks/Dirac16ComplexKohnSham.nb\"]; {Head[nb], Length[nb[[1]]], Tally[nb[[1, All, 2]]], Lookup[Options[nb], TaggingRules]}'
   ```

   This form printed the expected line in Windows PowerShell 5.1.26100.9444. Do not use it in PowerShell 7, Git Bash, macOS or Linux: in PowerShell 7.6.6 and in Git Bash it gave `ToExpression::sntx: Invalid syntax` and `$Failed`.
5. **Same content, even if the bytes differ** (for example with another Wolfram version, Part 4.4). Build into `build/rebuilt/` as in Part 3.3, then type

   ```
   wolframscript -code 'With[{a = Get["build/rebuilt/Dirac16ComplexKohnSham.nb"], b = Get["notebooks/Dirac16ComplexKohnSham.nb"]}, Head[a] === Notebook && a === b]'
   ```

   It must print `True`. `True` means two things: the rebuilt file was read as a notebook (`Head[a] === Notebook`), and the two files hold the same Wolfram Language expression (`a === b`). This was tested in PowerShell 7.6.6 and Git Bash.

   * If a file cannot be read, `Get` gives `$Failed` and the command prints `False`, together with `Get::noopen: Cannot open ...`. This was tested with a missing file in PowerShell 7.6.6.
   * The check is written this way so that it cannot pass when nothing was read. The first version of this file used the shorter `Get[...] === Get[...]`. In Windows PowerShell 5.1 that form printed `True` after two `Get::stream` messages, because nothing was read and `$Failed === $Failed` is `True`. The form above printed `False` there.
   * For Windows PowerShell 5.1 only, write the inner quotes as `\"`, as in check 4:

     ```
     wolframscript -code 'With[{a = Get[\"build/rebuilt/Dirac16ComplexKohnSham.nb\"], b = Get[\"notebooks/Dirac16ComplexKohnSham.nb\"]}, Head[a] === Notebook && a === b]'
     ```

     This printed `True` in 5.1.26100.9444. In PowerShell 7.6.6 and in Git Bash it is a syntax error (`ToExpression::sntx`).
6. **The repository's own test** (optional; needs Python 3, standard library only). This test runs the builder into a temporary folder that it deletes afterwards. It compares the result byte for byte with the committed notebook, and it also checks the Input-cell count and the line ends:

   ```
   python -m unittest tests.test_d16c_kohn_sham_mathematica.ReportIsCurrent.test_notebook_is_a_fresh_build tests.test_d16c_kohn_sham_mathematica.ReportIsCurrent.test_notebook_input_cell_count -v
   ```

   It must end with `Ran 2 tests` and `OK`. On macOS and Linux, type `python3` if `python` is not found. If `wolframscript` is not on the PATH, the first test is reported as `skipped`, which means that nothing was rebuilt.

   **If Python 3 is not installed:**
   * Windows: type `winget install --id Python.Python.3.14 -e`, then open a new terminal. On 2026-10-02, `winget show` listed version 3.14.7 for this package; the verification used Python 3.14.5.
   * macOS: download and run the installer from https://www.python.org/downloads/.
   * Debian or Ubuntu Linux: `sudo apt install python3`.

   **Side effects of this check:**
   * Python stores the compiled test module as `tests/__pycache__/test_d16c_kohn_sham_mathematica.cpython-314.pyc`. The `314` is your Python version. It does not do this if the environment variable `PYTHONDONTWRITEBYTECODE` is set. Git ignores this folder (rule `__pycache__/` in `.gitignore`). To remove it, type `Remove-Item -Recurse -Force tests/__pycache__` in PowerShell, or `rm -rf tests/__pycache__` in bash or zsh.
   * The test creates a folder in the system's temporary directory (Python's `tempfile.TemporaryDirectory`; on Windows under `%TEMP%`). It writes `fresh.nb` there and deletes the folder at the end.

### 3.5 If it fails

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `wolframscript` is not recognized / `command not found` | WolframScript is not installed or not on the PATH | Install it (Part 3.1). On Windows you can add its folder for the current session with `$env:Path += ";C:\Program Files\Wolfram Research\WolframScript"`. On macOS and Linux, find it with `find / -name wolframscript -type f 2>/dev/null` and add its folder with `export PATH="<folder>:$PATH"`. |
| A request for a Wolfram ID, or a message that the kernel is not activated or that no licence is available | The engine was never activated, or its licence has expired | Run `wolframscript -activate` yourself (Part 3.1) and run the builder again. |
| A message that too many kernels are running, or that no kernel licence is free | Your licence (the free licence in particular) may limit how many kernels can run at the same time | Close other Wolfram programs and run again. This builder needs one kernel for about 2 to 7 seconds. Just before the kernel, WolframScript starts a second, short-lived `wolfram.exe` with the options `-wlbanner -licenseinfo`, which reads the licence information and runs for about 0.1 to 0.5 seconds. It ended before the kernel started in every run that was timed (Part 5), so the two never ran at the same time, but both appear in Task Manager or `ps`. |
| `Failed to open file at path: scripts/build_dirac16complex_ks_mathematica_notebook.wls` (on standard error), and nothing else. **The exit code is 0 here**, so `$LASTEXITCODE` or `echo $?` alone does not show the failure | You are not in the repository root, so the relative path of the script does not exist | `cd` into the `Dirac_claude` folder (Part 3.2) and run again. A run counts as successful only if the three lines of Part 4.1 are printed. |
| Check 4 or 5 of Part 3.4 prints `Get::stream: ... is not a string, SocketObject, InputStream[ ] or OutputStream[ ].`, check 4 prints a line beginning with `{Symbol, 2, ...`, or check 5 prints `False` | You typed the check in Windows PowerShell 5.1, in which the inner double quotes are lost (Part 3.0) | Open PowerShell 7 (`pwsh`) and type the check again, or use the `\"` form given for 5.1 in checks 4 and 5. |
| `Put::noopen: Cannot open ...`, followed by `ERROR: could not write the notebook (Put): <path>` and exit code 1 | The output file is read-only or locked by another program, or its folder cannot be created (for example because a file has the folder's name) | Close the program that holds the file, or remove the read-only flag (Windows: `attrib -r <file>`; macOS and Linux: `chmod u+w <file>`), or choose another output path. Before the fix of Part 6, the same situation printed `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream` messages. It then *also* printed the normal three lines and gave exit code 0, although nothing had been written, so always read the messages. |
| The fingerprint differs from Part 3.4 | Another Wolfram version formats or wraps the cells differently (Part 4.4), or the committed notebook was changed before the run (for example by saving it from Mathematica) | Run check 5 of Part 3.4. If it prints `True`, the content is the same. Restore the committed bytes with `git checkout -- notebooks/Dirac16ComplexKohnSham.nb`. |
| A path with spaces is cut off | Quoting | Put the path in quotes, for example `"build/my folder/Dirac16ComplexKohnSham.nb"`. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly three lines on standard output and nothing on standard error:

```
cell_count=77
input_cell_count=33
output=<repository root>\notebooks\Dirac16ComplexKohnSham.nb
```

* `<repository root>` stands for the absolute path of your clone, for example `C:\Users\you\Dirac_claude`.
* On macOS and Linux the path is expected to use `/` instead of `\` (not tested).
* With an output path argument, the third line shows that file as an absolute path.
* On Windows the printed lines end with CR LF, in PowerShell and in Git Bash alike. The file named in the third line has LF line ends.
* The size of the printed output is 45 bytes plus the length of the absolute path in the third line, so your count will differ. On the verification machine it was 227 bytes in clones A to C (a path of 182 characters) and 231 bytes in clone D (186 characters).

**The exit code is 0.** But exit code 0 alone is not proof of success. When WolframScript cannot open the script file, it prints only `Failed to open file at path: ...` and also exits with 0 (Part 3.5). The run succeeded only if the three lines above are printed.

This set has no pass/fail checks of its own: it prints no verdict line and no check count. Its correctness check is the byte comparison of Part 3.4: the built notebook must equal the committed one.

The 94 checks of the notebook are evaluated by the verifier `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`, not by this builder. The builder's count agrees with what the verifier expects: 33 Input cells (`expectedInputCount = 33`).

### 4.2 The output file

`notebooks/Dirac16ComplexKohnSham.nb`, or the file you named:

* 359236 bytes, sha256 `7e91159dba0fd1875736e3101e69a2b174017b173539ad0df4b3348d4457b22f`;
* pure ASCII, LF line ends (5122 line feeds), no spaces or tabs at line ends, no newline after the last line;
* begins with `Notebook[{Cell["dirac16complex Kohn-Sham DFT in the static primordial field: \` and ends with `"SchemaVersion" -> 1|>]`;
* 77 cells: Title 1, Section 9, Subsection 5, Text 29, Input 33. The Input cells are unevaluated, so the notebook has no Output cells.

### 4.3 Looking at the notebook

* **In any text editor:** the file is readable text, but the code is stored as typeset boxes (`RowBox[{...}]`), not as you would type it.
* **In the desktop product Wolfram/Mathematica:** choose File, Open. You see the title, the sections, the explanations and the code.
  * Do not save the notebook after you evaluate it there. Saving adds output cells and changes the committed file (restore it with `git checkout -- notebooks/Dirac16ComplexKohnSham.nb`).
  * Evaluating it also overwrites the committed report `artifacts/dirac16complex/kohn-sham/mathematica-report.json` and the 6 PNG figures, and it needs the compiled Rust program.
  * The verifier named in Part 1 evaluates the notebook without a window.
* **The free Wolfram Player** (https://www.wolfram.com/player/) displays notebooks but cannot evaluate them. The free Wolfram Engine has no notebook window.

### 4.4 Run time, memory, and other Wolfram versions

**Run time.** These are wall-clock times on the verification machine (24 cores, Windows 11). Most of the time is the start of the kernel, and the time grows when the computer is busy:

* First verification (clones A to C): 1.8 to 4.2 seconds, median 2.3 seconds, over 12 timed runs. About 11 other Wolfram kernels of parallel verification jobs were running on the same machine.
* Re-verification (clone D), with about 12 other Wolfram kernels running:
  * 6 unmonitored runs in PowerShell 7 took 3.6 to 6.3 seconds;
  * 32 runs under process monitoring took 3.7 to 6.7 seconds;
  * one run in Windows PowerShell 5.1 took 5.0 seconds.

Expect about 2 to 7 seconds.

**Memory.** The figure given is the peak working set: the largest amount of physical memory a process used at any one time. 1 MiB = 1,048,576 bytes and 1 MB = 1,000,000 bytes. Windows keeps this peak for the whole life of a process. In 32 runs of the re-verification, the monitor opened a handle on each process while it was running and kept it. After the process had ended, it read the final peak through that handle. So no part of the run was missed:

* the kernel `wolfram.exe -runfirst ...`: 155.4 to 156.1 MiB (163.0 to 163.7 MB);
* the short licence-information process `wolfram.exe -wlbanner -licenseinfo` (Part 5): 68.4 to 68.6 MiB (71.7 to 71.9 MB), in the 29 runs in which a handle on it was opened before it ended;
* `wolframscript.exe`: 17.1 to 17.3 MiB (about 18 MB).

The first verification gave 143.6 to 143.8 for the kernel and 17.2 for `wolframscript.exe` (runs 1, 2, 9 and 10 of Part 6). It wrote these as "MB", but they were MiB. That method sampled the processes only between full process listings plus a 40 ms pause, about every 0.1 s, so it missed the last part of the run. In that part the kernel writes and reads back the notebook and reaches its peak. Those kernel values are therefore lower bounds. For comparison, a kernel that only evaluates `1+1` (`wolframscript -code 1+1`) peaked at 148.2 to 148.4 MiB.

**Other Wolfram versions.** Only version 15.0.1 was tested, and it reproduces the committed bytes exactly. Another version may wrap long lines or form some boxes differently. That would change the bytes, but not the meaning. Check 5 of Part 3.4 tells you whether the content is still the same.

## 5. Side effects

* **Overwritten in the repository:** `notebooks/Dirac16ComplexKohnSham.nb` (default run only). The file is rewritten even when its content does not change: its modification time changes, its bytes stay the same and `git status` stays empty. Any changes you made to this file yourself are lost.
* **Created in the repository:** nothing else.
  * After every default run, `git status --porcelain --untracked-files=all --ignored` printed nothing in the fresh clones.
  * The builder does not touch `artifacts/`: the report `mathematica-report.json` and the 6 figures are written only when the notebook is evaluated.
  * With an output path argument, that file and any missing parent folders are created, and the committed notebook is left untouched (its modification time did not change). For example, `build/rebuilt/` is created; Git lists it only as ignored (`!! build/rebuilt/Dirac16ComplexKohnSham.nb` with `--ignored`).
* **Created by check 6 of Part 3.4 (the Python test), not by the builder:** the ignored file `tests/__pycache__/test_d16c_kohn_sham_mathematica.cpython-314.pyc`, and a temporary folder outside the repository that the test deletes again. Check 6 says how to remove the `__pycache__` folder.
* **Files outside the repository (Windows).** These were watched in two ways:
  * with file-system notifications on `%APPDATA%\Wolfram`, `%LOCALAPPDATA%\Wolfram` and `C:\ProgramData\Wolfram` and all their subfolders, during 20 runs;
  * by listing the folder `%APPDATA%\Wolfram\Paclets\Temporary` every millisecond during 5 more runs.

  None of these files belongs to the repository, and none needs to be restored.
  * *WolframScript's console files.* In `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\`, WolframScript keeps the console output that it relays in files named `tmp_` plus 10 random characters. In a run with no other WolframScript active, two such files were created, one at the start and one near the end, and both were deleted when the run ended.
  * *WolframScript's settings file.* Every run rewrites `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` at its start, with the same content. Only the modification time changes.
    * In each of the 20 watched runs, the file was written 0.03 to 0.10 s after this run's `wolframscript.exe` started. In 9 of those runs, no other WolframScript started during the run.
    * In 2 of the 5 polled runs, no other WolframScript started within 2 s, and the file was written at +0.036 and +0.037 s.
    * Other WolframScript runs on the machine wrote the file at their own start in the same way.
    * Its size (238 bytes) and its sha256 (`AD439D17632B7FB8D0CDA9C9EAFFB10278B7995838EA3C588AD9B88C2800216C` on the verification machine) were the same before and after every run.
  * *The kernel's paclet lock files.* About 0.7 to 1.3 s after it starts, the kernel creates 0-byte lock files in `%APPDATA%\Wolfram\Paclets\Temporary\` and deletes each of them again within about 0.3 s. The files are `pacletData_15.0.1.0_<number>.pmd3.lock`, `managerData_15.0.1.0.pmd2.lock` and `pacletSiteData_15.lock`. The four other, older files in that folder kept their names and sizes, and after each run the folder held the same files as before. Other Wolfram jobs on the machine produced the same lock files at other times.
  * *Other changes.* In 2 of the 20 watched runs, a few other changes were seen, and they did not repeat in the other 18 runs:
    * one run changed the front-end cache file `FrontEnd\15.0 Caches\...\CharacterEncodings\UTF-8.pbf`;
    * another changed the front-end log `Logs\FrontEnd\system.log` and created a file in `ApplicationData\ProcessLink\Streams\`, both at the very end of the run or just after it.

    This builder starts no front end (see *Processes* below), and other Wolfram jobs, which do use one, were running at the same time. So these changes are not attributed to this builder.
  * The locations on macOS and Linux were not examined.
* **Processes.** One `wolframscript.exe` starts two `wolfram.exe` processes, one after the other. This was counted exactly in 12 runs: the monitor ran inside a Windows job object, which counts every process that the run creates, and each run created exactly 3 processes.
  1. `wolfram.exe -wlbanner -licenseinfo`, a short licence-information process. It starts 0.03 to 0.05 s after `wolframscript.exe` and runs for 0.11 to 0.28 s (up to 0.45 s in two runs), with exit code 0.
  2. The kernel, `wolfram.exe -runfirst ...`. It starts 0.02 to 0.05 s after the first one has ended and runs until the end of the run. The kernel process ends with exit status 3 in every run, while `wolframscript.exe` gives 0. This is how WolframScript ends its kernel: `wolframscript -code 1+1` showed the same 3 processes and the same exit status 3.

  So at most one `wolfram.exe` of this run is alive at any moment, and all three processes have ended when the command returns.

  The licence-information process appeared in every run in which processes were counted exactly (12 of 12). Process listings (WMI, one listing every 0.15 to 0.2 s) caught it in 19 of 20 other runs; in the remaining run it ended between two listings. The first verification listed processes about every 0.1 s plus the time of each listing, and did not see it in its 4 watched runs. An independent check that also used polling saw it in 6 of 12 runs. Exact counting found it in every run, so the lower counts from polling are most likely due to its short life.
* **Network.** The script itself makes no network access. WolframScript or the kernel may contact Wolfram's licence server, for example when the free Engine renews its licence. Network traffic was not monitored.
* **Restoring the committed state:**

  ```
  git checkout -- notebooks/Dirac16ComplexKohnSham.nb
  ```

  If you used an output path, delete that file and its folder yourself, for example the folder `build/rebuilt`:
  * Windows (PowerShell 7 or Windows PowerShell 5.1): `Remove-Item -Recurse -Force build/rebuilt`
  * macOS and Linux: `rm -rf build/rebuilt`

## 6. Verification record

* **Date:** 2026-10-02.
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of `main` on https://github.com/once-ere/Dirac_claude.git when the fresh clones were made. The two files of this set are unchanged since commit `eac67e6` (2026-09-30).
* **Clones:**
  * Clones A and C: no uncommitted file was copied in.
  * Clone B: received only the fixed script, from the working tree.
  * Clone D (the re-verification, made later the same day from the same commit `c2b33cc`): received only the fixed script (sha256 `7432e599...68bb`), from the working tree.
* **Environment:**
  * Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 cores;
  * Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence;
  * WolframScript 1.14.0;
  * PowerShell 7.6.6; in clone D also Windows PowerShell 5.1.26100.9444;
  * Git 2.51.2.windows.1 with its Git Bash (GNU bash 5.2.37).

  Python 3.14.5 was used only for the repository test of check 6 and for the monitoring, not by this set.
* **Runs in clones A to C.** All runs were made from the repository root of a fresh clone. "Identical" means byte-identical to the committed notebook, sha256 `7e91159d...7b22f`. "PowerShell" means PowerShell 7.6.6.

  The memory column is the polled kernel peak of the first method, in MiB (the file first wrote "MB"). These values are lower bounds; Part 4.4 gives the exact peak, 155.4 to 156.1 MiB.

| Run | Clone | Shell | Command form | Exit | Wall time | Peak kernel memory, polled (MiB, lower bound) | Notebook |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A | PowerShell | default | 0 | 2.83 s | 143.6 | identical |
| 2 | A | PowerShell | default | 0 | 1.96 s | 143.7 | identical, and identical to run 1 |
| 3 | A | Git Bash | default | 0 | 2.18 s | not measured | identical |
| 4 | A | Git Bash | output path `build/rebuilt/...` (the folder did not exist) | 0 | 3.49 s | not measured | identical; committed file untouched |
| 5 | A | Git Bash | `-- build/dashdash/...` | 0 | 4.16 s | not measured | identical; written to `build/dashdash`, committed file untouched |
| 6 | A | PowerShell | `-- build/dashdash-ps/...` | 0 | 2.02 s | not measured | identical |
| 7 | A | PowerShell | default | 0 | 2.02 s | not measured | identical; the first form of check 5, `Get[...] === Get[...]`, against run 4 printed `True` |
| 8 | A | Python test (check 6) | builder into a temporary folder | 0 | 2.34 s (2 tests) | not measured | identical; `Ran 2 tests`, `OK` |
| 9, 10 | B (fixed script) | PowerShell | default | 0 | 2.47, 2.33 s | 143.7, 143.8 | identical, and identical to each other |
| 11 | B (fixed script) | Git Bash | output path `build/new/deeper/...` (two new folders) | 0 | not timed | not measured | identical |
| 12 | B (fixed script) | Git Bash | `-- build/dd/...` | 0 | not timed | not measured | identical |
| 13 | B (fixed script) | Python test (check 6) | builder into a temporary folder | 0 | 2.79 s (2 tests) | not measured | identical; `Ran 2 tests`, `OK` |
| 14 | B (fixed script) | PowerShell | output path `build/rebuilt/...` | 0 | 4.21 s | not measured | identical |
| 15, 16 | C | Git Bash | default | 0 | 1.93, 1.83 s | not measured | identical, and identical to each other |

The structure check of Part 3.4 (check 4) was also run, in Git Bash in clone A and in PowerShell 7.6.6 in clone C. It is not a build, and both times it printed the expected line.

* **Runs in clone D (re-verification).** All runs were made from the repository root, except the three marked "outside". Every notebook that was compared or hashed was byte-identical to the committed one.
  * *Shells and checks 4 and 5.* A build into `build/rebuilt/` was made in Windows PowerShell 5.1 and again in PowerShell 7.6.6, each with exit 0. Then checks 4 and 5 were run in Windows PowerShell 5.1, PowerShell 7.6.6 and Git Bash, with the results quoted in Part 3.4:
    * PowerShell 7.6.6 and Git Bash: the expected line and `True`.
    * Windows PowerShell 5.1, as written: check 4 printed the wrong line; the first form of check 5 printed a false `True`; the new form printed `False`.
    * Windows PowerShell 5.1 with `\"`: the expected line and `True`.
    * PowerShell 7.6.6 and Git Bash with `\"`: `ToExpression::sntx`.
    * Finally, every `wolframscript -code` command of this file was taken from the file itself and run in all three shells. Each printed what this file says it prints in that shell.
    * A form with PowerShell's stop-parsing token `--%` printed `True` in 5.1 but `$Failed` in 7.6.6, so it is not offered.
  * *Windows PowerShell 5.1 builds.* A default build (5.0 s) and `-- build/dd51/...` each gave exit 0 and the committed sha256.
  * *20 default builds under WMI process listing and file-system watching* (PowerShell 7.6.6). Each gave exit 0, standard output 231 bytes, standard error 0 bytes, and a notebook with the full committed sha256, recorded after each run. They took 3.7 to 6.7 s.
  * *12 default builds under exact process counting* (job object, Part 5). Each gave exit 0 and exactly 3 processes. They took 3.7 to 4.9 s.
  * *5 default builds* while `%APPDATA%\Wolfram\Paclets\Temporary` was polled every millisecond. Each gave exit 0.
  * *6 unmonitored default builds* (PowerShell 7.6.6) took 3.6 to 6.3 s. Each gave exit 0, and the sha256 began `7E91159DBA0F` after each.
  * *Git Bash, default.* Exit 0. Standard output was 231 bytes with 3 CR and 3 LF, which is 45 bytes plus the 186 characters of the path. Standard error was 0 bytes.
  * *Outside: from the folder above the clone*, in Git Bash, PowerShell 7.6.6 and Windows PowerShell 5.1. Each printed `Failed to open file at path: scripts/build_dirac16complex_ks_mathematica_notebook.wls` with exit code 0 and wrote nothing. In Git Bash, standard output was 0 bytes and standard error 86 bytes, and the notebook's modification time did not change.
  * *Check 6* (Python 3.14.5, with `PYTHONDONTWRITEBYTECODE` unset): `Ran 2 tests in 3.816s` and `OK`, exit 0. It created `tests/__pycache__/test_d16c_kohn_sham_mathematica.cpython-314.pyc`. The first verification did not report this file. The shells of the verification harness set `PYTHONDONTWRITEBYTECODE=1`, which prevents it, so it had to be unset for this run.
  * *Two final builds* into `build/final1/` and `build/final2/` took 5.5 and 5.6 s. Both gave exit 0, standard output 234 bytes and standard error 0 bytes. Both notebooks were byte-identical (`cmp`) to the committed notebook taken with `git show HEAD:notebooks/Dirac16ComplexKohnSham.nb`. The two outputs were identical apart from the folder name.
  * *A last default build* (5.3 s) was byte-identical, and `git diff --quiet` gave 0. The earlier outputs `build/rebuilt/` and `build/dd51/` were also byte-identical.
  * *At the end*, `git status --porcelain --untracked-files=all --ignored` printed:
    * ` M scripts/build_dirac16complex_ks_mathematica_notebook.wls`, the copied fix;
    * the ignored `build/` outputs;
    * the ignored `.pyc` of check 6.
  * *3 runs of `wolframscript -code 1+1`* under exact process counting, for comparison (Part 5).
  * Three more default builds were started by two attempts of the monitor that stopped because of bugs in the monitoring script itself, not in the builder. They are not counted above. Every later hash of `notebooks/Dirac16ComplexKohnSham.nb` in this clone was still the committed one.

* **Standard output and the repository.** In every successful run, standard output was the three lines of Part 4.1. Within one clone these lines were byte-identical from run to run (compared for runs 1 and 2 and for runs 15 and 16). Standard error was empty. After every default run, `git status --porcelain --untracked-files=all` printed nothing, except the intended modification of the script in clones B and D.
* **Check counts.** The set has no checks of its own (Part 4.1). The byte comparison passed in every build that was compared:
  * clones A to C: 16 of 16 notebooks (runs 1 to 16);
  * clone D: 27 of 27 notebooks, with a full sha256 or `cmp`:
    * 20 monitored builds;
    * 2 Windows PowerShell 5.1 builds;
    * the 2 final builds;
    * the last default build;
    * `build/rebuilt/`;
    * the build of check 6.

    The sha256 prefix also matched in the 6 unmonitored timed builds.
* **Fix made (an execution defect, not science).**
  * *The defect.* When the output file could not be written, the unfixed script still printed `cell_count=77`, `input_cell_count=33` and `output=<path>`, and exited with code 0. This was reproduced in clone A in two ways:
    * With a read-only output file, the script printed `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, and the file kept its old content.
    * With an output folder below a *file*, the script printed `Put::noopen`, `Import::nffil`, `StringReplace::strse`, `OpenWrite::noopen`, `ToCharacterCode::strse`, `BinaryWrite::stream` and `Close::stream`.

    All of these messages went to standard output.
  * *The fix.* Each write step is now checked:
    * `Put` must not return `$Failed`;
    * the read-back must be a string;
    * `OpenWrite` must return an `OutputStream`;
    * the written size must equal the number of bytes intended.

    If a check fails, the script prints `ERROR: could not write the notebook (<step>): <path>` and exits with code 1. This is the same fix that was made to the Stage-3 builder `scripts/build_dirac16complex_mathematica_notebook.wls`.
  * *The diff.* 11 lines added and 2 lines changed, in the write section at the end of the script only. Git counts this as 13 insertions and 2 deletions, because it counts a changed line as one deletion plus one insertion.
    * The 11 added lines are 6 comment lines, the definition of `failWrite`, the `StringQ` check, `outputBytes`, the `OutputStream` check and the `FileByteCount` check.
    * The 2 changed lines are the `Put` line and the `BinaryWrite` line.

    The cell code and the notebook expression are untouched. The script's sha256 changed from `2bb0e133...ff1a982` (999 lines) to `7432e599...68bb` (1010 lines = 999 + 11).
  * *Re-verification* in fresh clone B, with only the fixed script copied in:
    * runs 9 to 14: exit 0, notebook identical;
    * a read-only output file: `ERROR: could not write the notebook (Put): ...` and exit code 1, in both Git Bash and PowerShell; the old file was kept;
    * an output folder below a file: `ERROR: could not write the notebook (Put): ...` and exit code 1.
* **Open discrepancies:** none. This set involves no number and no physics check.

  One note concerns only how the command line is passed, not any result. The verifier's header (`scripts/verify_dirac16complex_ks_mathematica_notebook.wls`) says that WolframScript 1.14 drops the arguments after `--`. For this builder that was not observed: the output path after `--` arrived and was used, in Git Bash and in PowerShell 7.6.6 (runs 5, 6 and 12), and in Windows PowerShell 5.1 (clone D).
