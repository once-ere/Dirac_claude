# Execution provenance: the builder of the Stage-4 Kohn-Sham Mathematica notebook (WolframScript)

Set: `scripts/build_dirac16complex_ks_mathematica_notebook.wls`. It writes `notebooks/Dirac16ComplexKohnSham.nb` (old Stage 4, the Kohn-Sham density-functional study).

Verdict: **EXECUTES OK**. Every notebook it wrote was **byte-identical** to the committed one.

This set was verified twice, with Wolfram 15.0.1 and WolframScript 1.14.0 on Windows 11 (24 cores):

* **First verification, 2026-10-02**, at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, in four fresh clones (A to D; Part 6.2). It found one execution defect and fixed it (Part 6.3): if the output file could not be written, the script printed error messages but still exited with code 0. The fix was committed on 2026-10-02 in commit `3f0a577`. It does not change the bytes of the notebook.
* **Re-verification, 2026-10-07** (Part 6.1). The verification run was interrupted by a session limit and restarted, so the committed script, which now contains the fix, was verified again from the beginning in two new fresh clones:
  * clone E at commit `cb6e78fcd8fdd3f6b360cdd6ad9d8f51e6453bbd`;
  * clone F at commit `22fc7af2a4ffa9242fa9c8c1d49b37f28259f790`.

  Each was the head of `main` when the clone was made. The files of this set are the same in both commits. No file was copied into the clones. All 37 builds of that day ended with exit code 0. Each of the 27 notebooks that was compared one by one was byte-identical to the committed notebook, and so were the 2 notebooks hashed at the end of a group of builds.

Every number in this file was measured again on 2026-10-07, unless the text says that it is a result of 2026-10-02.

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
6. Each write step is checked. If one fails, the script prints `ERROR: could not write the notebook (<step>): <path>` and exits with code 1 (the fix of Part 6.3).
7. Otherwise it prints `cell_count=77`, `input_cell_count=33` and `output=<absolute path of the file>`, and exits with code 0.

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
| `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, with the exit-code fix of Part 6.3: committed in `3f0a577` (2026-10-02) and unchanged at `cb6e78f` and `22fc7af` | the script, verified on 2026-10-07 | `7432e599992eecab33a9caf62e5b7352c8a03e2d36d9eede86d66d9eab8868bb` | 1010 (113149 bytes, ASCII, LF) |
| the same script before the fix, as committed from `eac67e6` (2026-09-30) to `c2b33cc` | the version verified first on 2026-10-02 | `2bb0e133adfa86ff3ec8d63e49759e69d6fcb1a1c74805fc6aba7feccff1a982` | 999 (112327 bytes, ASCII, LF) |
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

   On 2026-10-02 and again on 2026-10-07, `winget show` listed version 7.6.6.0 for this package. The installer itself was not run for this record, because PowerShell 7.6.6 was already installed. Instead of `winget`, you can download the `.msi` installer from https://github.com/PowerShell/PowerShell/releases.
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
   * **Windows:** run the downloaded installer and accept the defaults. Instead, in PowerShell, you can type `winget install --id WolframResearch.WolframEngine -e`. On 2026-10-02 and on 2026-10-07, `winget show` listed version 15.0.0 for this package; the installer itself was not run for this record. The installer also installs WolframScript and adds it to the PATH. Afterwards, close every PowerShell window and open a new one.
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

On 2026-10-07 the clone took 20 seconds on the verification machine. Git received 222 MiB, and the clone held 689 MiB (723 MB) of files, the Git data included. The repository grows with every commit.

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

On the verification machine the run took 1.8 to 10 seconds, depending on how busy the computer was (Part 4.4). To time it:

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
   * Windows: type `winget install --id Python.Python.3.14 -e`, then open a new terminal. On 2026-10-02 and on 2026-10-07, `winget show` listed version 3.14.7 for this package; the verification used Python 3.14.5.
   * macOS: download and run the installer from https://www.python.org/downloads/.
   * Debian or Ubuntu Linux: `sudo apt install python3`.

   **Side effects of this check:**
   * Python stores the compiled test module as `tests/__pycache__/test_d16c_kohn_sham_mathematica.cpython-314.pyc`. The `314` is your Python version. It does not do this if the environment variable `PYTHONDONTWRITEBYTECODE` is set (both cases were tested on 2026-10-07). Git ignores this folder (rule `__pycache__/` in `.gitignore`). To remove it, type `Remove-Item -Recurse -Force tests/__pycache__` in PowerShell, or `rm -rf tests/__pycache__` in bash or zsh.
   * The test creates a folder in the system's temporary directory (Python's `tempfile.TemporaryDirectory`; on Windows under `%TEMP%`). It writes `fresh.nb` there and deletes the folder at the end.

### 3.5 If it fails

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `wolframscript` is not recognized / `command not found` | WolframScript is not installed or not on the PATH | Install it (Part 3.1). On Windows you can add its folder for the current session with `$env:Path += ";C:\Program Files\Wolfram Research\WolframScript"`. On macOS and Linux, find it with `find / -name wolframscript -type f 2>/dev/null` and add its folder with `export PATH="<folder>:$PATH"`. |
| A request for a Wolfram ID, or a message that the kernel is not activated or that no licence is available | The engine was never activated, or its licence has expired | Run `wolframscript -activate` yourself (Part 3.1) and run the builder again. |
| A message that too many kernels are running, or that no kernel licence is free | Your licence (the free licence in particular) may limit how many kernels can run at the same time | Close other Wolfram programs and run again. This builder needs one kernel for about 2 to 10 seconds. Just before the kernel, WolframScript starts a second, short-lived `wolfram.exe` with the options `-wlbanner -licenseinfo`, which reads the licence information and runs for about 0.1 to 2 seconds. It ended before the kernel started in every run that was timed (Part 5), so the two never ran at the same time, but both appear in Task Manager or `ps`. |
| `Failed to open file at path: scripts/build_dirac16complex_ks_mathematica_notebook.wls` (on standard error), and nothing else. **The exit code is 0 here**, so `$LASTEXITCODE` or `echo $?` alone does not show the failure | You are not in the repository root, so the relative path of the script does not exist | `cd` into the `Dirac_claude` folder (Part 3.2) and run again. A run counts as successful only if the three lines of Part 4.1 are printed. |
| Check 4 or 5 of Part 3.4 prints `Get::stream: ... is not a string, SocketObject, InputStream[ ] or OutputStream[ ].`, check 4 prints a line beginning with `{Symbol, 2, ...`, or check 5 prints `False` | You typed the check in Windows PowerShell 5.1, in which the inner double quotes are lost (Part 3.0) | Open PowerShell 7 (`pwsh`) and type the check again, or use the `\"` form given for 5.1 in checks 4 and 5. |
| `Put::noopen: Cannot open ...`, followed by `ERROR: could not write the notebook (Put): <path>` and exit code 1 | The output file is read-only or locked by another program, or its folder cannot be created (for example because a file has the folder's name) | Close the program that holds the file, or remove the read-only flag (Windows: `attrib -r <file>`; macOS and Linux: `chmod u+w <file>`), or choose another output path. A version of the script from before 2026-10-02 (without the fix of Part 6.3) prints `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream` messages instead, *also* prints the normal three lines and gives exit code 0, although nothing was written. |
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
* The size of the printed output is 45 bytes plus the length of the absolute path in the third line, so your count will differ. On 2026-10-07 it was 232 bytes (a path of 187 characters); on 2026-10-02 it was 227 and 231 bytes.

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

**Run time.** These are wall-clock times on the verification machine (24 cores, Windows 11). Most of the time is the start of WolframScript and the kernel: on 2026-10-07 a script file that only prints `1+1` took 3.9 to 5.0 seconds (3 runs) at the same time as the builds below. The builder's kernel used 2.2 to 2.8 seconds of processor time. The wall-clock time grows when the computer is busy:

* 2026-10-07: 34 timed builds took 4.9 to 10.0 seconds, median 6.2 seconds. During these runs 8 to 13 other `wolfram.exe` processes of parallel verification jobs were running, and the processor load was 88 percent when it was read before the runs.
* 2026-10-02: 1.8 to 4.2 seconds (median 2.3) with about 11 other kernels running, and 3.6 to 6.7 seconds in the later re-check with about 12.

Expect about 2 to 10 seconds.

**Memory.** The figure given is the peak working set: the largest amount of physical memory a process used at any one time. 1 MiB = 1,048,576 bytes and 1 MB = 1,000,000 bytes. Windows keeps this peak for the whole life of a process. In 11 builds on 2026-10-07, the monitor started the run inside a Windows job object and opened a handle on each process of the job while it was running. After the process had ended, it read the final peak through that handle, so no part of the run was missed:

* the kernel `wolfram.exe -runfirst ...`: 155.3 to 156.3 MiB (162.9 to 163.9 MB);
* the short licence-information process `wolfram.exe -wlbanner -licenseinfo` (Part 5): 68.1 to 68.3 MiB (71.4 to 71.6 MB);
* `wolframscript.exe`: 17.1 to 17.3 MiB (17.9 to 18.2 MB).

With the same method, a kernel that only evaluates `1+1` peaked at 156.2 to 156.3 MiB, both with `wolframscript -code 1+1` (3 runs) and with a script file that only prints `1+1` (3 runs). That is as high as the builder's kernel. So the peak is what the kernel needs for its own start; building the notebook adds nothing measurable.

The re-check of 2026-10-02 (clone D), with the same method, gave 155.4 to 156.1 MiB for the kernel, 68.4 to 68.6 MiB for the licence process and 17.1 to 17.3 MiB for `wolframscript.exe`. The first verification of 2026-10-02 sampled the processes only about every 0.1 s and gave lower values for the kernel (143.6 to 143.8 MiB); those were lower bounds. The first version of this file also gave 148.2 to 148.4 MiB for a `1+1` kernel and explained the difference to the builder's kernel by a peak while the notebook is written and read back. The measurements of 2026-10-07 do not support that explanation, so it was removed; why the `1+1` value of 2026-10-02 was lower is not known.

**Other Wolfram versions.** Only version 15.0.1 was tested, and it reproduces the committed bytes exactly. Another version may wrap long lines or form some boxes differently. That would change the bytes, but not the meaning. Check 5 of Part 3.4 tells you whether the content is still the same.

## 5. Side effects

* **Overwritten in the repository:** `notebooks/Dirac16ComplexKohnSham.nb` (default run only). The file is rewritten even when its content does not change: its modification time changes, its bytes stay the same and `git status` stays empty. Any changes you made to this file yourself are lost.
* **Created in the repository:** nothing else.
  * After every default run, `git status --porcelain --untracked-files=all --ignored` printed nothing in the fresh clones.
  * The builder does not touch `artifacts/`: the report `mathematica-report.json` and the 6 figures are written only when the notebook is evaluated.
  * With an output path argument, that file and any missing parent folders are created, and the committed notebook is left untouched (its modification time did not change). For example, `build/rebuilt/` is created; Git lists it only as ignored (`!! build/rebuilt/Dirac16ComplexKohnSham.nb` with `--ignored`).
* **Created by check 6 of Part 3.4 (the Python test), not by the builder:** the ignored file `tests/__pycache__/test_d16c_kohn_sham_mathematica.cpython-314.pyc` (unless `PYTHONDONTWRITEBYTECODE` is set), and a temporary folder outside the repository that the test deletes again. Check 6 says how to remove the `__pycache__` folder.
* **Files outside the repository (Windows).** On 2026-10-07 these were watched with file-system notifications on `%APPDATA%\Wolfram`, `%LOCALAPPDATA%\Wolfram` and `C:\ProgramData\Wolfram` and all their subfolders, during 8 default builds; in 4 of them each event was timed when it happened. Other Wolfram jobs ran at the same time and caused the same kinds of events. The clearest of the timed runs showed only one set of the lock files described below, and no other `wolframscript.exe` that had started during it was still running at its end. None of these files belongs to the repository, and none needs to be restored.
  * *WolframScript's console files.* In `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\`, WolframScript keeps the console output that it relays in files named `tmp_` plus 10 random characters. In the clearest run, one such file was created at +0.06 s, a second one at +4.0 s, and both were deleted at +5.24 s, as the run ended (it took 5.26 s).
  * *WolframScript's settings file.* Every run rewrites `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` at its start, with the same content. Only the modification time changes. In the clearest run it was written at +0.07 s. Its size (238 bytes) and its sha256 (`AD439D17632B7FB8D0CDA9C9EAFFB10278B7995838EA3C588AD9B88C2800216C` on the verification machine) were the same before and after the runs, as on 2026-10-02.
  * *The kernel's paclet lock files.* About 0.6 to 1.7 s after the run starts (1.08 to 1.66 s in the clearest run), the kernel creates 0-byte lock files in `%APPDATA%\Wolfram\Paclets\Temporary\` and deletes each of them again within 0.2 s. The files are `pacletData_15.0.1.0_<number>.pmd3.lock`, `managerData_15.0.1.0.pmd2.lock` and `pacletSiteData_15.lock`. The other files in that folder (10 on 2026-10-07) kept their names and sizes; the folder held the same files before and after the runs.
  * *Other changes.* None in the 4 timed runs of 2026-10-07. On 2026-10-02, in 2 of 20 watched runs, a front-end cache file, the front-end log and a file in `ApplicationData\ProcessLink\Streams\` changed. This builder starts no front end (see *Processes* below), and other Wolfram jobs, which do use one, were running at the same time, so those changes are not attributed to this builder.
  * The locations on macOS and Linux were not examined.
* **Processes.** One `wolframscript.exe` starts two `wolfram.exe` processes, one after the other. The job object of Part 4.4 counts every process that a run creates. In each of the 11 builds of 2026-10-07 (and in 12 builds of 2026-10-02) it counted exactly 3 processes:
  1. `wolfram.exe -wlbanner -licenseinfo`, a short licence-information process. On 2026-10-07 it started 0.05 to 0.27 s after `wolframscript.exe`, ran for 0.24 to 1.75 s and ended with exit code 0. On 2026-10-02 it ran for 0.11 to 0.45 s.
  2. The kernel, started as `"C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`. It started 0.03 to 0.17 s after the first one had ended and ran until the end of the run. The kernel process ends with exit status 3 in every run, while `wolframscript.exe` gives 0. This is how WolframScript ends its kernel: `wolframscript -code 1+1` showed the same 3 processes and the same exit status 3.

  So at most one `wolfram.exe` of this run is alive at any moment, and all three processes have ended when the command returns. WolframScript talks to the kernel through shared memory (`-linkname <name>_shm`), not through a network port.
* **Network.** The script itself makes no network access. WolframScript or the kernel may contact Wolfram's licence server, for example when the free Engine renews its licence. On 2026-10-07 the open TCP connections and UDP endpoints of the three processes were listed during 2 builds, 5 or 6 times per build: none was seen. A connection shorter than the interval between the listings (about 1.4 s) would have been missed; the traffic itself was not recorded.
* **Restoring the committed state:**

  ```
  git checkout -- notebooks/Dirac16ComplexKohnSham.nb
  ```

  If you used an output path, delete that file and its folder yourself, for example the folder `build/rebuilt`:
  * Windows (PowerShell 7 or Windows PowerShell 5.1): `Remove-Item -Recurse -Force build/rebuilt`
  * macOS and Linux: `rm -rf build/rebuilt`

## 6. Verification record

### 6.1 Re-verification of 2026-10-07 (the committed script with the fix)

* **Date:** 2026-10-07.
* **Commits verified:**
  * clone E: `cb6e78fcd8fdd3f6b360cdd6ad9d8f51e6453bbd`;
  * clone F: `22fc7af2a4ffa9242fa9c8c1d49b37f28259f790`.

  Each was the head of `main` on https://github.com/once-ere/Dirac_claude.git when the clone was made. In both, the script has the sha256 `7432e599...68bb` and the notebook `7e91159d...7b22f` of Part 2. `.gitattributes`, `.gitignore` and `tests/test_d16c_kohn_sham_mathematica.py` are also the same in both. No uncommitted file was copied into either clone.
* **Environment:**
  * Windows 11 Pro for Workstations, version 10.0.26300 (build 26300.9457), 24 logical processors;
  * Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence;
  * WolframScript 1.14.0;
  * PowerShell 7.6.6 and Windows PowerShell 5.1.26100.9444;
  * Git 2.51.2.windows.1 with its Git Bash (GNU bash 5.2.37), `core.autocrlf=true`;
  * Python 3.14.5, used only for check 6 and for the monitoring, not by this set.
* **Runs.** All runs were made from the repository root of the clone, except the two marked "outside". "Identical" means byte-identical (`cmp` or full sha256) to the committed notebook `7e91159d...7b22f`; `git show HEAD:notebooks/Dirac16ComplexKohnSham.nb` was used as the reference.

| Runs | Clone | Shell | Command form | Exit | Wall time | Notebook |
| --- | --- | --- | --- | --- | --- | --- |
| E1, E2 | E | PowerShell 7.6.6 | default | 0, 0 | 5.20, 5.34 s | identical, and identical to each other; standard error empty |
| E3, E4 | E | Git Bash | default | 0, 0 | 5.72, 6.28 s | identical, and identical to each other; standard output 232 bytes (3 CR, 3 LF), byte-identical between the two runs; standard error 0 bytes |
| E5, E6 | E | Git Bash | `build/rebuilt1/...`, `build/rebuilt2/...` (`build/` did not exist) | 0, 0 | 6.61, 4.95 s | identical, and identical to each other; the committed notebook's modification time did not change |
| E7 | E | Git Bash | `-- build/dashdash/...` | 0 | 5.15 s | identical |
| E8, E9 | E | PowerShell 7.6.6 | `build/rebuilt/...`; `-- build/dashdash-ps/...` | 0, 0 | 4.93, 7.00 s | identical |
| E10, E11 | E | Windows PowerShell 5.1 | default; `-- build/dd51/...` | 0, 0 | 8.65, 8.24 s | identical |
| E12 | E | Python test (check 6), `PYTHONDONTWRITEBYTECODE` unset | builder into a temporary folder | 0 | `Ran 2 tests in 10.380s`, `OK` | identical (inside the test); created the `.pyc` of Part 5 |
| E13 to E23 | E | job-object monitor (Python), 11 default builds | default | 0 each | 5.16 to 9.30 s | identical after each build (full sha256); exactly 3 processes each; standard output 232 bytes, byte-identical in all 11; standard error 0 bytes |
| E24 to E31 | E | PowerShell 7.6.6 under file-system watching, 8 default builds | default | 0 each | 5.04 to 7.03 s | sha256 of the notebook taken after the last of them: identical |
| E32, E33 | E | PowerShell 7.6.6, network sockets listed | default | 0, 0 | 8.64, 7.61 s | sha256 after the second: identical |
| F1, F2 | F | Git Bash | default | 0, 0 | 10.04, 8.90 s | identical, and identical to each other; standard output byte-identical between the two runs; `git status` empty after each |
| F3 | F | Python test (check 6), `PYTHONDONTWRITEBYTECODE=1` | builder into a temporary folder | 0 | `Ran 2 tests in 6.028s`, `OK` | identical (inside the test); no `.pyc`; `git status --ignored` empty afterwards |
| F4 | F | Git Bash | `build/final/...` | 0 | not timed | identical |

* **Comparison runs (not builds)**, under the job-object monitor in clone E's parent folder: 3 runs of `wolframscript -code 1+1` and 3 runs of a script file that only prints `1+1` (3.9 to 5.0 s). Each had exactly 3 processes and exit code 0 (Part 4.4 and Part 5).
* **The checks of Part 3.4**, run on 2026-10-07 in clone E:
  * check 2 (sha256) and check 3 (`git status` empty, `git diff --quiet` exit 0) after default runs, in PowerShell 7.6.6 and Git Bash;
  * checks 4 and 5 as written: the expected line and `True` in PowerShell 7.6.6 and in Git Bash; check 5 with a missing file printed `Get::noopen` and `False` (PowerShell 7.6.6);
  * checks 4 and 5 as written in Windows PowerShell 5.1: `Get::stream`, `Part::partd`, `Tally::listrp` and the wrong `{Symbol, 2, ...}` line; `False` for check 5; the old form `Get[...] === Get[...]` printed `True` after two `Get::stream` messages;
  * the `\"` forms: the expected line and `True` in Windows PowerShell 5.1, `ToExpression::sntx` and `$Failed` in PowerShell 7.6.6 and in Git Bash;
  * every one of these printed exit code 0.
* **Failure paths** (2026-10-07, clone E, the committed fixed script):
  * read-only output file `build/ro/locked.nb`: `Put::noopen` and `ERROR: could not write the notebook (Put): <path>` on standard output, exit code 1, the file kept its old content, in Git Bash and in PowerShell 7.6.6;
  * output folder below a *file* (`build/afile/sub/out.nb`): the same two lines and exit code 1 (Git Bash);
  * outside: from the folder above the clone, in Git Bash and PowerShell 7.6.6: only `Failed to open file at path: scripts/build_dirac16complex_ks_mathematica_notebook.wls` (in Git Bash: 0 bytes of standard output, 86 bytes of standard error), exit code 0, nothing written; the notebook's modification time did not change;
  * for comparison, the script before the fix (`git show c2b33cc:...`, sha256 `2bb0e133...`, written temporarily as an untracked file into `scripts/` of clone E and deleted afterwards) with the same read-only file: `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream`, `Close::stream`, then the normal three lines and exit code 0. This reproduces the defect of Part 6.3.
* **At the end**, `git status --porcelain --untracked-files=all --ignored` printed in clone E only ignored files: the `build/` outputs listed above (including `build/ro/locked.nb` and `build/afile` of the failure tests) and the `.pyc` of E12. In clone F it printed only `!! build/final/Dirac16ComplexKohnSham.nb`. No tracked file was changed in either clone.
* **Check counts.** The set has no checks of its own (Part 4.1). On 2026-10-07 there were 37 builds, each with exit code 0 (E1 to E33 and F1 to F4). The byte comparison passed for every notebook that was compared: 27 of 27 compared one by one (E1 to E23, F1 to F4) and the 2 group-end hashes (after E24 to E31 and after E32 to E33).
* **Fix made on 2026-10-07:** none. The fix of Part 6.3 was already committed.
* **Open discrepancies:** none. This set involves no number and no physics check. See also the note on `--` in Part 6.4.

### 6.2 First verification of 2026-10-02 (clones A to D)

* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of `main` when the clones were made. The two files of this set were unchanged since commit `eac67e6` (2026-09-30).
* **Clones:** A and C received no uncommitted file. B and D (D was a re-check later that day) received only the fixed script (sha256 `7432e599...68bb`), copied from the working tree before it was committed.
* **Environment as recorded then:** Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 cores; Wolfram 15.0.1 (Professional licence); WolframScript 1.14.0; PowerShell 7.6.6 and, in clone D, Windows PowerShell 5.1.26100.9444; Git 2.51.2.windows.1 with GNU bash 5.2.37; Python 3.14.5.
* **Runs in clones A to C.** "Identical" means byte-identical to the committed notebook. The memory column is the polled kernel peak, a lower bound (Part 4.4).

| Run | Clone | Shell | Command form | Exit | Wall time | Peak kernel memory, polled (MiB, lower bound) | Notebook |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A | PowerShell 7.6.6 | default | 0 | 2.83 s | 143.6 | identical |
| 2 | A | PowerShell 7.6.6 | default | 0 | 1.96 s | 143.7 | identical, and identical to run 1 |
| 3 | A | Git Bash | default | 0 | 2.18 s | not measured | identical |
| 4 | A | Git Bash | output path `build/rebuilt/...` (the folder did not exist) | 0 | 3.49 s | not measured | identical; committed file untouched |
| 5 | A | Git Bash | `-- build/dashdash/...` | 0 | 4.16 s | not measured | identical; written to `build/dashdash`, committed file untouched |
| 6 | A | PowerShell 7.6.6 | `-- build/dashdash-ps/...` | 0 | 2.02 s | not measured | identical |
| 7 | A | PowerShell 7.6.6 | default | 0 | 2.02 s | not measured | identical |
| 8 | A | Python test (check 6) | builder into a temporary folder | 0 | 2.34 s (2 tests) | not measured | identical; `Ran 2 tests`, `OK` |
| 9, 10 | B (fixed script) | PowerShell 7.6.6 | default | 0 | 2.47, 2.33 s | 143.7, 143.8 | identical, and identical to each other |
| 11 | B (fixed script) | Git Bash | output path `build/new/deeper/...` (two new folders) | 0 | not timed | not measured | identical |
| 12 | B (fixed script) | Git Bash | `-- build/dd/...` | 0 | not timed | not measured | identical |
| 13 | B (fixed script) | Python test (check 6) | builder into a temporary folder | 0 | 2.79 s (2 tests) | not measured | identical; `Ran 2 tests`, `OK` |
| 14 | B (fixed script) | PowerShell 7.6.6 | output path `build/rebuilt/...` | 0 | 4.21 s | not measured | identical |
| 15, 16 | C | Git Bash | default | 0 | 1.93, 1.83 s | not measured | identical, and identical to each other |

* **Clone D (re-check, fixed script).** 27 notebooks were compared with a full sha256 or `cmp`, all byte-identical: 20 builds under process listing and file-system watching (3.7 to 6.7 s each), 2 Windows PowerShell 5.1 builds, 2 final builds into `build/final1/` and `build/final2/`, a last default build, `build/rebuilt/` and the build of check 6 (`Ran 2 tests in 3.816s`, `OK`). 12 more builds under exact process counting (3.7 to 4.9 s) each had exactly 3 processes, and 6 unmonitored builds took 3.6 to 6.3 s. Checks 4 and 5 gave the results described in Part 3.4, in all three shells. Runs from outside the repository root printed `Failed to open file at path: ...` with exit code 0.
* **Standard output** was the three lines of Part 4.1 in every successful run, byte-identical within a clone, and standard error was empty.

### 6.3 Fix made (an execution defect, not science; found and fixed on 2026-10-02)

* *The defect.* When the output file could not be written, the unfixed script still printed `cell_count=77`, `input_cell_count=33` and `output=<path>`, and exited with code 0. This was reproduced in clone A in two ways, and again on 2026-10-07 in clone E (Part 6.1):
  * With a read-only output file, the script printed `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, and the file kept its old content.
  * With an output folder below a *file*, the script printed `Put::noopen`, `Import::nffil`, `StringReplace::strse`, `OpenWrite::noopen`, `ToCharacterCode::strse`, `BinaryWrite::stream` and `Close::stream`.

  All of these messages went to standard output.
* *The fix.* Each write step is now checked:
  * `Put` must not return `$Failed`;
  * the read-back must be a string;
  * `OpenWrite` must return an `OutputStream`;
  * the written size must equal the number of bytes intended.

  If a check fails, the script prints `ERROR: could not write the notebook (<step>): <path>` and exits with code 1. This is the same fix that was made to the Stage-3 builder `scripts/build_dirac16complex_mathematica_notebook.wls`.
* *The diff* (`git diff eac67e6 3f0a577`). 11 lines added and 2 lines changed, in the write section at the end of the script only. Git counts this as 13 insertions and 2 deletions, because it counts a changed line as one deletion plus one insertion.
  * The 11 added lines are 6 comment lines, the definition of `failWrite`, the `StringQ` check, `outputBytes`, the `OutputStream` check and the `FileByteCount` check.
  * The 2 changed lines are the `Put` line and the `BinaryWrite` line.

  The cell code and the notebook expression are untouched. The script's sha256 changed from `2bb0e133...ff1a982` (999 lines) to `7432e599...68bb` (1010 lines = 999 + 11).
* *Re-verification* in fresh clone B on 2026-10-02 (runs 9 to 14: exit 0, notebook identical; read-only file and folder below a file: `ERROR: could not write the notebook (Put): ...` and exit code 1), in clone D, and on 2026-10-07 in clones E and F with the committed fix (Part 6.1).

### 6.4 Note on `--`

This note concerns only how the command line is passed, not any result. The verifier's header (`scripts/verify_dirac16complex_ks_mathematica_notebook.wls`) says that WolframScript 1.14 drops the arguments after `--`. For this builder that was not observed: the output path after `--` arrived and was used, in Git Bash, in PowerShell 7.6.6 and in Windows PowerShell 5.1, on 2026-10-02 (runs 5, 6, 12 and clone D) and on 2026-10-07 (E7, E9, E11).
