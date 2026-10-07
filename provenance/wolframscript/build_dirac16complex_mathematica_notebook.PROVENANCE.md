# Execution provenance: the builder of the Stage-3 Mathematica notebook (WolframScript)

Set: `scripts/build_dirac16complex_mathematica_notebook.wls`, which writes `notebooks/Dirac16ComplexDarkSector.nb` (old Stage 3, the dark-sector numerics).

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` with Wolfram 15.0.1 and WolframScript 1.14.0 on Windows 11. Verdict: **EXECUTES OK**. There were 17 runs from three fresh clones, in two shells, with three ways of giving the output path. In all 15 runs whose output was fingerprinted, the notebook it writes is **byte-identical** to the committed one. One execution defect was found and fixed: when the output file could not be written, the script still exited with code 0. The fix (Part 6) does not change the bytes of the notebook. After an independent review, a fourth fresh clone (D) received the fixed script and 18 more runs were made in three shells, including Windows PowerShell 5.1. All 18 notebooks were byte-identical to the committed one. That re-check found that two of the optional check commands of Part 3.4 need a different quoting in Windows PowerShell 5.1; Part 3.4 now gives both forms.

**Re-verified on 2026-10-07** (after a session restart) in a fifth fresh clone (E) at commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, the head of `main` on GitHub at that time. The fixed script of Part 6 is committed there (since commit `3f0a577`), so nothing was copied into clone E. Seven builds were made in Git Bash, PowerShell 7.6.6 and Windows PowerShell 5.1, including the two default runs one after the other that this record requires: every build exited with code 0 and every notebook it wrote was **byte-identical** to the committed one (7 of 7). The two failure cases of the fix gave exit code 1 as documented, checks 4 and 5 of Part 3.4 printed exactly the expected lines in all three shells, and no file of the repository was changed. Verdict unchanged: **EXECUTES OK**. The details are in Part 6, "Re-verification of 2026-10-07".

## 1. What this set is and what it computes

**In plain words.** The Stage-3 study of this repository solves the field equation of `dirac16complex` in five model universes, called EXP-1 to EXP-5. `dirac16complex` is a field with 16 complex Grassmann components in eight dimensions: four space-like and four time-like directions. A Rust program, `studies/dirac16complex_cosmology`, does the solving with the CVODE solver. A Mathematica notebook, `notebooks/Dirac16ComplexDarkSector.nb`, checks those Rust results independently in the Wolfram Language. **This set does not evaluate that notebook. It only writes the notebook file.** The script holds the code of every notebook cell as unevaluated Wolfram Language. It turns that code into typeset notebook cells and writes them to the `.nb` file in a fixed, repeatable form: a later run on the same Wolfram version gives exactly the same bytes. A notebook is a plain text file that holds one Wolfram Language expression, `Notebook[{cells...}, options...]`. The free Wolfram Player and the desktop product Wolfram (formerly Mathematica) can open it, and any text editor can show it.

**What the script does, step by step.**

1. It finds the repository root: the parent of the folder that holds the script. The current folder is not used for this.
2. It reads the optional output path from the command line. If there is none, it writes to `notebooks/Dirac16ComplexDarkSector.nb` in the repository root. A literal `--` among the arguments is ignored.
3. It builds 72 cells: 1 title, 11 section headings, 23 text cells (the explanations) and 37 Input cells (the code). Each Input cell is made from code written in the script, using `ToBoxes[Unevaluated[code], StandardForm]`, so the code is turned into boxes and **never evaluated**.
4. It wraps the cells in `Notebook[...]` with the window title `dirac16complex dark sector: Mathematica cross-check`, the default style sheet and a `TaggingRules` entry. That entry names the builder (`scripts/build_dirac16complex_mathematica_notebook.wls`), the verifier (`scripts/verify_dirac16complex_mathematica_notebook.wls`) and `SchemaVersion -> 1`.
5. It writes the expression with `Put`, reads the file back as text, changes Windows line ends (CR LF) to LF, removes spaces and tabs at the ends of lines, and writes the result again as UTF-8 bytes. The final file is pure ASCII, has LF line ends and has no newline after the last line.
6. It prints `cell_count=72`, `input_cell_count=37` and `output=<absolute path of the file>`, and exits with code 0. With the fix of Part 6, it exits with code 1 and prints `ERROR: could not write the notebook (...)` if any write step fails.

**What the notebook does when it is evaluated** (by a separate script or in Mathematica; this builder never does it). The 37 Input cells:

* load the Stage-1 packages `wolfram/Dirac16ComplexAlgebra.wl` and `wolfram/Dirac16ComplexGeometry.wl`;
* check the Clifford algebra of the sixteen-by-sixteen gamma matrices;
* read the gamma matrices, `C`, the chirality matrix and `B` back from the Rust source file `studies/dirac16complex_cosmology/src/generated.rs`, and require them to equal the package matrices exactly. Here `C` (named `chargeC` in the code and `CHARGE` in the Rust constants) is a 16 x 16 **matrix**, `C = gamma^0 gamma^1 gamma^2 gamma^3`, used in the Dirac adjoint `Psibar = Psi^dagger C`. The notebook performs no charge-conjugation operation on fields. `Conjugate[u]` appears only in inner products of numerical spinors: the bilinears `u^dagger M u` (functions `scalarDensityN`, `expectN`, `hilbertN` and `kreinNormN`) and the phase overlap `u^dagger v` of two different spinors (function `alignedDistance`). `ConjugateTranspose` appears only on matrices: in the checks that `B` is Hermitian, that the Hamiltonian matrices are Hermitian (in the good sector) or Krein-pseudo-Hermitian, and that the EXP-5 Hamiltonian is not Hermitian;
* derive the reduced first-order equations of each experiment symbolically from the covariant field equation, and compare them exactly with the equations the Rust program integrates;
* re-integrate every experiment with `NDSolve` and compare the result with the committed CSV files in `artifacts/dirac16complex/numerics/exp1` to `exp5`;
* run the Rust program's `print-config` command;
* draw 8 figures into `artifacts/dirac16complex/numerics/figures/mathematica/`;
* write `artifacts/dirac16complex/numerics/mathematica-report.json` with 49 checks.

Evaluating the notebook is the job of `scripts/verify_dirac16complex_mathematica_notebook.wls`, which is a different set with its own provenance file. That evaluation needs the compiled Rust program. **The builder needs none of this.**

**Documents that cite this set or its notebook.**

* `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` (with its `.tex` and `.pdf`), Sections 5.4 and 11.2. Its file table lists the builder as the script that "writes it deterministically", and it reports that all 49 notebook checks are true.
* `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` (`.tex`, `.pdf`), Section 11 "The Mathematica notebook (optional)". It gives the builder command and says the builder "writes the same bytes again", which this verification confirms.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (`.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/10-numerical-ode.md`, `11-dark-sector-experiments.md` and `19-reproducing-everything.md`. They cite the function `fdCheck` of this script (the 9-point finite-difference test of the Rust solutions) and list the notebook with its 49 checks.
* `artifacts/dirac16complex/numerics/mathematica-report.json`. Its `generatedBy` field names this builder.
* `scripts/verify_dirac16complex_mathematica_notebook.wls`, which evaluates the notebook, and the Stage-3 gates `scripts/verify_stage3_dark_sector.ps1` and `.sh`. The gates read the committed notebook as an input but never rebuild it.
* `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, the Stage-4 builder, which was modelled on this one; the notebook it writes, `notebooks/Dirac16ComplexKohnSham.nb` (lines 36 and 5007); and that notebook's report, `artifacts/dirac16complex/kohn-sham/mathematica-report.json` (line 4, field `provenance`). The notebook says that it "follows", and the report that it was "modelled on", the Stage-3 notebook `notebooks/Dirac16ComplexDarkSector.nb` "and its builder/verifier".
* `HANDOFF.md.txt`, whose table of stages lists `notebooks/Dirac16ComplexDarkSector.nb` among the Stage-3 deliverables (lines 106, 264, 457 and 585).
* The workflow scripts `handoff/workflows/wf_stage3_docs.js`, `handoff/workflows/wf_stage4_notebooks_documents.js` and `Revision/workflows/execution_provenance.js` name the builder and the notebook as tasks. They are tooling, not documents, and cite no result.
* Other execution-provenance files in `provenance/wolframscript/` mention this set or its notebook: `verify_dirac16complex_mathematica_notebook.PROVENANCE.md` (the verifier that evaluates the notebook), `build_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` (the Stage-4 builder, which received the same exit-code fix as this one), `verify_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` (a test in which the Stage-4 verifier rejects this 37-Input-cell notebook) and `verify_dirac16complex_geometry.PROVENANCE.md` (which lists this builder and its notebook among the programs that load the geometry package; strictly, only the notebook loads it when it is evaluated, the builder only writes the `Get` call into a cell). These citing lines were found again on 2026-10-07, as were the citations listed above (for example `HANDOFF.md.txt` lines 106, 264, 457 and 585).

## 2. Files

| File | Role | sha256 | Lines |
| --- | --- | --- | --- |
| `scripts/build_dirac16complex_mathematica_notebook.wls` before the fix, as committed from `fbec4d7` to `c2b33cc` | the script verified first on 2026-10-02 (history only) | `126f18b974f332a055b42bac3708b5f31bc788d8f288401f5f9630f354243112` | 1045 (102127 bytes, ASCII, LF) |
| `scripts/build_dirac16complex_mathematica_notebook.wls` with the exit-code fix of Part 6, committed in `3f0a577` (2026-10-02) and unchanged at `a4c5eda` | **the current script**, re-verified on 2026-10-07 | `9b94c222646286785b6ac6fa6ba328fd0158ac74c91b3ab2ed69f16058a0e87d` | 1056 (102949 bytes, ASCII, LF) |
| `notebooks/Dirac16ComplexDarkSector.nb` | the only output (committed; unchanged since `fbec4d7`) | `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe` | 5048 line-feed characters and no newline after the last line, so an editor shows 5049 lines (354930 bytes, ASCII) |

**Inputs.** The script reads no file of the repository except itself and its own output, which it reads back right after writing it (step 5 of Part 1). The earlier contents of the output file are never used: if the first write fails, the fixed script stops with exit code 1 before reading anything back (Part 6). It does not read the packages in `wolfram/`, the CSV files, the Rust sources or the Rust program. Those are read only when the notebook is *evaluated*, which this set never does. The only other thing it depends on is the Wolfram system: the way `ToBoxes` and `Put` format the cells and wrap long lines (near 78 characters; the longest line of the committed notebook has 79) belongs to the Wolfram version (see Part 4.4).

**Outputs.** Exactly one file. By default it is `notebooks/Dirac16ComplexDarkSector.nb`, which is overwritten. With the optional argument, it is the file you name (missing folders are created).

## 3. How to run it

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs. The first is the Wolfram Language *kernel*, the program that does the computing. The second is *WolframScript*, the command `wolframscript`, which runs a script file with the kernel. The verification used kernel version 15.0.1 and WolframScript 1.14.0. This builder starts one kernel.

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser, open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page. Create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded installer and accept the defaults. Instead, in PowerShell, you can type `winget install --id WolframResearch.WolframEngine -e`. On 2026-10-02, `winget show` listed version 15.0.0 for this package; the installer was not executed for this record. The installer also installs WolframScript and adds it to the PATH. Afterwards, close every PowerShell window and open a new one.
   * macOS: open the downloaded `.dmg` file and follow its instructions: drag the application into Applications and open it once.
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/, then open a new terminal. The download is a `.msi` file for Windows and a `.pkg` file for macOS. For Linux it is a `.deb` file (install with `sudo apt install ./<file>.deb`) or a `.rpm` file (install with `sudo dnf install ./<file>.rpm`).
3. Activate it. In a terminal (PowerShell on Windows, Terminal on macOS and Linux), type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. Running `wolframscript` with no options on an engine that is not yet activated asks the same questions. If you see the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.

**Option 2: Wolfram (formerly Mathematica), the desktop product.** A licensed Wolfram or Mathematica installation contains the kernel, and on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/ as in step 2 above. With the desktop product you can also open the built notebook in a notebook window (Part 4.3).

**Test the installation.** In a new terminal, type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux, because they stop the shell from replacing `$Version`; they are also correct in PowerShell. `wolframscript -version` prints the WolframScript version, for example `WolframScript 1.14.0 for Microsoft Windows (64-bit)`. If several versions are installed, `wolframscript` uses the newest one, and `wolframscript -configure` prints the kernel it uses.

**Which PowerShell (Windows only).** Windows 11 comes with *Windows PowerShell 5.1* (the Start-menu entry "Windows PowerShell"). The newer *PowerShell 7* is a separate program (the Start-menu entry "PowerShell 7", or type `pwsh`). To see which one you are in, type

```
$PSVersionTable.PSVersion
```

It prints a table whose first two columns (`Major`, `Minor`) are `5` and `1` in Windows PowerShell 5.1 and `7` and a minor version in PowerShell 7. The two pass double quotes inside an argument to a program differently. This matters only for the two optional checks 4 and 5 of Part 3.4, whose Wolfram code contains double quotes; Part 3.4 gives a separate form of each for Windows PowerShell 5.1. Every other command of this file works the same in both (tested with 5.1.26100.9444 and 7.6.6). If you want PowerShell 7, type `winget install --id Microsoft.PowerShell -e` (on 2026-10-02, `winget show` listed version 7.6.6.0 for this package; the installer was not executed for this record), then open "PowerShell 7" from the Start menu or type `pwsh`.

### 3.2 Get the repository

Install Git if you do not have it: on Windows, https://git-scm.com/download/win or `winget install --id Git.Git -e`; on macOS, type `xcode-select --install` in Terminal; on Debian or Ubuntu Linux, `sudo apt install git`. Then, in the folder where you want the repository, type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone took 8 seconds on the verification machine. It downloads about 130 MB and occupies about 520 MB on disk (measured on 2026-10-02). On 2026-10-07 the clone took 17 seconds, and `du -sh` reported 473 MB for the clone folder, 195 MB of it in the hidden folder `.git`. Type every command below in this folder, the *repository root*: the folder that contains `scripts`, `notebooks` and `wolfram`. The repository stores every file byte for byte: its `.gitattributes` turns off line-end conversion, even when Git is set up with `core.autocrlf=true` (as on the verification machine). So the checked-out notebook has exactly the committed bytes.

### 3.3 Run it

The usage line in the script's header is

```
wolframscript -file scripts/build_dirac16complex_mathematica_notebook.wls [output.nb]
```

The square brackets mean that the output path is optional. You do not type the brackets.

**PowerShell on Windows** (Windows PowerShell 5.1 or PowerShell 7; tested with 5.1.26100.9444 and 7.6.6):

```
wolframscript -file scripts/build_dirac16complex_mathematica_notebook.wls
$LASTEXITCODE
```

**macOS Terminal (zsh) or Linux terminal (bash)**, and also Git Bash on Windows (tested):

```
wolframscript -file scripts/build_dirac16complex_mathematica_notebook.wls
echo $?
```

The second line prints the exit code, which must be `0`. The run takes about 2 to 7 seconds, depending on how busy the machine is; most runs on the verification machine took 3 to 5 seconds (Part 4.4). To time it, type `Measure-Command { wolframscript -file scripts/build_dirac16complex_mathematica_notebook.wls | Out-Host }` in PowerShell, or put `time ` in front of the command in bash or zsh.

This default run **overwrites the committed notebook** `notebooks/Dirac16ComplexDarkSector.nb` with the newly built one. With Wolfram 15.0.1 the new file is byte-identical to the committed one, so Git sees no change. Part 5 says how to restore the file if it does change.

**Recommended for students: write the notebook to a scratch folder instead**, so that the committed file is never touched, and then compare the two files. Git ignores the folder `build/` (rule `/build/` in `.gitignore`), and the script creates missing folders itself. The command is the same in every shell named above:

```
wolframscript -file scripts/build_dirac16complex_mathematica_notebook.wls build/rebuilt/Dirac16ComplexDarkSector.nb
```

A relative output path is taken relative to the folder you are in. Run the command from the repository root, as shown. You may put `--` before the output path (`... .wls -- build/rebuilt/Dirac16ComplexDarkSector.nb`), but you do not need to. The path after `--` arrives because this script's first line is `#!/usr/bin/env wolframscript`, and the script ignores the `--` itself. This was tested in Git Bash, in PowerShell 7.6.6 and in Windows PowerShell 5.1 (Part 6).

### 3.4 Check the result

Each of the following checks must succeed after a default run. After a run with an output path, put that path in place of `notebooks/Dirac16ComplexDarkSector.nb`.

1. **The printed lines and the exit code** must be as in Part 4.1.
2. **The sha256 fingerprint** of the file must be `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe`. To print it:
   * PowerShell (5.1 or 7): `(Get-FileHash notebooks/Dirac16ComplexDarkSector.nb -Algorithm SHA256).Hash`. PowerShell prints the fingerprint in capital letters, `708804E7F4BB...`; that is the same value.
   * macOS: `shasum -a 256 notebooks/Dirac16ComplexDarkSector.nb`
   * Linux and Git Bash: `sha256sum notebooks/Dirac16ComplexDarkSector.nb`
3. **Git sees no change** (after a default run):

   ```
   git status --porcelain -- notebooks/Dirac16ComplexDarkSector.nb
   ```

   must print nothing. `git diff --quiet -- notebooks/Dirac16ComplexDarkSector.nb` must give the exit code 0 (shown by `$LASTEXITCODE` in PowerShell and by `echo $?` in bash and zsh). Git shows a change of a `.nb` file only as "binary", never line by line, because of the rule `*.nb -diff` in `.gitattributes`.

**Quoting for checks 4 and 5.** These two commands contain double quotes inside the Wolfram code, so their exact form depends on the shell. Use the first form in PowerShell 7 (version 7.3 or later), in the macOS and Linux terminals and in Git Bash. Use the second form, in which every inner `"` is written `\"`, only in Windows PowerShell 5.1. Part 3.1 says how to tell which PowerShell you are in. Do not mix them up:

* Typed in Windows PowerShell 5.1, the first form loses its inner double quotes on the way to WolframScript. Wolfram then prints messages that begin with `Get::stream:` and say that the file name `is not a string, SocketObject, InputStream[ ] or OutputStream[ ]` (the file name is drawn as a fraction across three lines). Whatever follows those messages is meaningless.
* Typed in PowerShell 7.6.6 or in Git Bash, the second form gives `ToExpression::sntx: Invalid syntax in or before "..."` and then `$Failed`.
* PowerShell 7.0 to 7.2 still passed quotes the old way, like Windows PowerShell 5.1; the change came with PowerShell 7.3 (not tested here). Install the current PowerShell 7 instead (Part 3.1).

4. **The structure of the notebook** (optional). This command prints the head, the number of cells, the number of cells of each style and the tagging rules.

   PowerShell 7, macOS, Linux and Git Bash:

   ```
   wolframscript -code 'nb = Get["notebooks/Dirac16ComplexDarkSector.nb"]; {Head[nb], Length[nb[[1]]], Tally[nb[[1, All, 2]]], Lookup[Options[nb], TaggingRules]}'
   ```

   Windows PowerShell 5.1 only:

   ```
   wolframscript -code 'nb = Get[\"notebooks/Dirac16ComplexDarkSector.nb\"]; {Head[nb], Length[nb[[1]]], Tally[nb[[1, All, 2]]], Lookup[Options[nb], TaggingRules]}'
   ```

   The expected output is one line:

   ```
   {Notebook, 72, {{Title, 1}, {Text, 23}, {Section, 11}, {Input, 37}}, <|GeneratedBy -> scripts/build_dirac16complex_mathematica_notebook.wls, VerifiedBy -> scripts/verify_dirac16complex_mathematica_notebook.wls, SchemaVersion -> 1|>}
   ```

   If the line begins with `{Symbol, 2, ...` instead, the shell removed the double quotes (see above), and the file was never read.
5. **Same content, even if the bytes differ** (for example with another Wolfram version, Part 4.4). Build into `build/rebuilt/` as in Part 3.3, then type the following. It reads both files and prints the head of each and whether the two are the same expression.

   PowerShell 7, macOS, Linux and Git Bash:

   ```
   wolframscript -code 'a = Get["build/rebuilt/Dirac16ComplexDarkSector.nb"]; b = Get["notebooks/Dirac16ComplexDarkSector.nb"]; {Head[a], Head[b], a === b}'
   ```

   Windows PowerShell 5.1 only:

   ```
   wolframscript -code 'a = Get[\"build/rebuilt/Dirac16ComplexDarkSector.nb\"]; b = Get[\"notebooks/Dirac16ComplexDarkSector.nb\"]; {Head[a], Head[b], a === b}'
   ```

   It must print exactly

   ```
   {Notebook, Notebook, True}
   ```

   which means that both files were read as notebooks and hold the same Wolfram Language expression. `{Notebook, Notebook, False}` means that the two notebooks differ. Anything else means that the check did not work: in particular `{Symbol, Symbol, True}`, after `Get::stream` messages, means that neither file was read (both reads gave `$Failed`, and `$Failed === $Failed` is `True`). It says nothing about the notebooks. Both forms were tested in their own shell against the rebuilt notebook (`{Notebook, Notebook, True}`) and against a deliberately different notebook (`{Notebook, Notebook, False}`), and the first form in Git Bash too (Part 6).

### 3.5 If it fails

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `wolframscript` is not recognized / `command not found` | WolframScript is not installed or not on the PATH | Install it (Part 3.1). On Windows you can add its folder for the current session with `$env:Path += ";C:\Program Files\Wolfram Research\WolframScript"`. On macOS and Linux, find it with `find / -name wolframscript -type f 2>/dev/null` and add its folder with `export PATH="<folder>:$PATH"`. |
| A request for a Wolfram ID, or a message that the kernel is not activated or that no licence is available | The engine was never activated, or its licence has expired | Run `wolframscript -activate` yourself (Part 3.1) and run the builder again. |
| A message that too many kernels are running, or that no kernel licence is free | Your licence (the free licence in particular) may limit how many kernels can run at the same time | Close other Wolfram programs and run again. This builder needs one kernel for a few seconds (2 to 7 s measured, Part 4.4). |
| `Failed to open file at path: scripts/build_dirac16complex_mathematica_notebook.wls` | You are not in the repository root | `cd` into the `Dirac_claude` folder (Part 3.2) and run again. Careful: WolframScript 1.14.0 gave exit code 0 even in this case (tested), so a run counts as successful only if it prints the three lines of Part 4.1. |
| `Put::noopen: Cannot open ...`, followed by `ERROR: could not write the notebook (Put): <path>` and exit code 1 | The output file is read-only, is locked by another program, or its folder cannot be created (for example because a file has the folder's name) | Close the program that holds the file. Remove the read-only flag (Windows: `attrib -r <file>`; macOS and Linux: `chmod u+w <file>`), or choose another output path. Before the fix of Part 6, the same situation printed `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, and then *also* the normal `output=` line with exit code 0, although nothing had been written. Always read the messages. |
| The fingerprint differs from Part 3.4 | Another Wolfram version formats or wraps the cells differently (Part 4.4), or the committed notebook had already been changed before the run (for example by saving it from Mathematica) | Run check 5 of Part 3.4, in the form for your shell. If it prints `{Notebook, Notebook, True}`, the content is the same. A bare `True` or `{Symbol, Symbol, True}` after `Get::stream` messages proves nothing (next row). Restore the committed bytes with `git checkout -- notebooks/Dirac16ComplexDarkSector.nb`. |
| Check 4 or 5 prints `Get::stream: ... is not a string, SocketObject, InputStream[ ] or OutputStream[ ].` (the file name drawn as a fraction across three lines), then `{Symbol, 2, ...}` (check 4) or `{Symbol, Symbol, True}` (check 5), with exit code 0 | You typed the first form in Windows PowerShell 5.1, which removed the double quotes from the Wolfram code, so no file was read. The `True` of check 5 then only says that two failed reads are equal; it says nothing about the notebooks | Type the Windows PowerShell 5.1 form of the check (every inner `"` written `\"`), or open PowerShell 7 (`pwsh`) and type the first form (Part 3.1). |
| Check 4 or 5 prints `ToExpression::sntx: Invalid syntax in or before "..."` and then `$Failed` | You typed the Windows PowerShell 5.1 form (with `\"`) in PowerShell 7, macOS, Linux or Git Bash (tested in PowerShell 7.6.6 and Git Bash) | Type the first form of the check instead. |
| A path with spaces is cut off | Quoting | Put the path in quotes, for example `"build/my folder/Dirac16ComplexDarkSector.nb"`. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly three lines on standard output and nothing on standard error:

```
cell_count=72
input_cell_count=37
output=<repository root>\notebooks\Dirac16ComplexDarkSector.nb
```

`<repository root>` stands for the absolute path of your clone, for example `C:\Users\you\Dirac_claude`. On macOS and Linux the path uses `/` instead of `\` (expected; not tested). With an output path argument, the third line shows that file as an absolute path. On Windows the lines end with CR LF; the file printed in the third line has LF line ends. **The exit code is 0.**

This set has no pass/fail checks of its own: it prints no verdict line and no check count. Its correctness check is the byte comparison of Part 3.4: the built notebook must equal the committed one. The 49 checks of the notebook are evaluated by the verifier `scripts/verify_dirac16complex_mathematica_notebook.wls`, not by this builder. The builder's numbers are consistent with what the verifier expects: it reports 37 Input cells, the same number that the verifier prints as `input_cell_count=37`.

### 4.2 The output file

`notebooks/Dirac16ComplexDarkSector.nb`, or the file you named:

* 354930 bytes, sha256 `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe`;
* pure ASCII, LF line ends, no spaces or tabs at line ends, no newline after the last line (5048 line feeds);
* begins with `Notebook[{Cell["dirac16complex dark sector: symbolic reduction and NDSolve \` and ends with `"SchemaVersion" -> 1|>]`;
* 72 cells: Title 1, Section 11, Text 23, Input 37. The Input cells are unevaluated, so the notebook has no Output cells.

### 4.3 Looking at the notebook

* In any text editor: the file is readable text, but the code is stored as typeset boxes (`RowBox[{...}]`), not as you would type it.
* In the desktop product Wolfram/Mathematica: choose File, Open. You see the title, the sections, the explanations and the code. Do not save the notebook from there. Saving rewrites the file in the notebook window's own format, and adds output cells if you evaluated it, so it changes the committed file. If that happens, restore it with `git checkout -- notebooks/Dirac16ComplexDarkSector.nb`. Evaluating it needs the compiled Rust program. The verifier script mentioned in Part 1 evaluates it without a window.
* The free Wolfram Player (https://www.wolfram.com/player/) displays notebooks but cannot evaluate them. The free Wolfram Engine has no notebook window.

### 4.4 Run time, memory, and other Wolfram versions

**Run time.** Expect about 2 to 7 seconds of wall-clock time, depending on how busy the machine is. Most of that time is the start of the kernel. On 2026-10-02, all 38 timed runs on the verification machine (24 cores, Windows 11) took 1.87 to 6.32 s (median 3.84 s), and 31 of them took 3 to 5 s; the re-verification of 2026-10-07 added 7 timed runs (last item below). Other verification jobs were running on the same machine throughout:

* the 14 timed runs of the first verification (clones A to C): 1.87 to 5.06 s, median 3.9 s; up to 12 other Wolfram kernels were counted at one moment. The two fastest runs, 1.87 s and 2.74 s, were the last two made; the machine's load was not measured at that time;
* the 9 timed runs of the independent review (its own fresh clone, 11 to 18 other Wolfram processes running): 3.69 to 6.32 s, median 4.66 s; the three slowest runs took 6.11, 6.24 and 6.32 s;
* the 15 timed runs of the re-check in fresh clone D (5 to 8 other `wolfram.exe` processes at the start of the 11 runs where they were counted): 3.25 to 5.44 s, median 3.56 s;
* the 7 timed runs of the re-verification of 2026-10-07 in fresh clone E (another workflow was running Wolfram kernels at the same time; 1 and 6 other Wolfram kernel processes at the start of the two watched runs): 3.92 to 6.66 s, median 5.56 s.

Over all 45 timed runs, the run time was 1.87 to 6.66 s.

**Memory.** The kernel process `wolfram.exe` reached a peak working set of 150 to 155 MB, and `wolframscript.exe` about 17 MB (the independent review measured 152.4 and 152.5 MB, and 16.9 MB; the two watched runs of 2026-10-07 measured 151.9 and 151.8 MB, and 16.9 MB both times).

**Other Wolfram versions.** Only version 15.0.1 was tested, and it reproduces the committed bytes exactly. Another version may wrap long lines or form some boxes differently. That would change the bytes, but not the meaning. Check 5 of Part 3.4 tells you whether the content is still the same.

## 5. Side effects

* **Overwritten in the repository:** `notebooks/Dirac16ComplexDarkSector.nb` (default run only). The file is rewritten even when its content does not change: its modification time changes, its bytes stay the same, and `git status` stays empty. Any changes you made to this file yourself are lost.
* **Created in the repository:** nothing else. After every default run in the fresh clones A and B, `git status --porcelain --untracked-files=all` printed nothing. After the scratch folders of the output-path runs were deleted, the same command with `--ignored` added printed nothing either. In particular, the builder does not touch `artifacts/`: the report `mathematica-report.json` and the 8 figures are written only when the notebook is evaluated. With an output path argument, that file and any missing parent folders are created, and the committed notebook is left untouched. A fresh clone has no folder `build/`. The recommended run of Part 3.3 therefore creates two folders, `build/` and `build/rebuilt/`; only `build/rebuilt/` if `build/` already existed (tested in clone D: `Test-Path build` printed `False` before the run and `True` after it, in Windows PowerShell 5.1 and in PowerShell 7.6.6). Git ignores `build/` and everything in it.
* **Temporary files.** On Windows, while it runs, WolframScript keeps the relayed console output in a temporary file in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\` (named `tmp_` plus 10 random characters), plus a zero-byte companion file. For this script, the output file measured 236 bytes, exactly the size of the three printed lines (that size depends on the length of the clone's path, which the third line prints). Other WolframScript runs were active at the same time, so this file was matched to this script by its size and its creation time. Both files were deleted when the run ended. The locations on macOS and Linux were not examined. During the runs, the modification time of WolframScript's own settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` changed, with the size unchanged. Other WolframScript runs were active at the same time, so this change cannot be attributed to this script with certainty. Neither file belongs to the repository.
* **Processes.** One `wolframscript.exe` starts one Wolfram kernel, `wolfram.exe -runfirst ... -linkmode Connect ...`. In 6 of the 8 runs that were watched process by process on 2026-10-02, a second, short-lived `wolfram.exe -wlbanner -licenseinfo` was also seen: a licence query, 15 to 68 MB. On 2026-10-07 it was seen in the first watched run (57.9 MB); in the second, a short-lived second `wolfram.exe` of 66.1 MB was seen whose command line could not be read in time. Once, a `conhost.exe` console host (10 MB) was seen. All of them end with the run.
* **Network.** The script itself makes no network access. WolframScript or the kernel may contact Wolfram's licence server for licence checks. Network traffic was not monitored.
* **Restoring the committed state:**

  ```
  git checkout -- notebooks/Dirac16ComplexDarkSector.nb
  ```

  If you used an output path, delete that file and the folders the run created yourself. After the recommended run of Part 3.3 in a fresh clone, that is the whole folder `build` (PowerShell: `Remove-Item -Recurse -Force build`; macOS, Linux and Git Bash: `rm -rf build`). If `build/` already existed before your run and holds other files you want to keep, delete only `build/rebuilt` (PowerShell: `Remove-Item -Recurse -Force build/rebuilt`; macOS, Linux and Git Bash: `rm -rf build/rebuilt`). Afterwards, if you started from a fresh clone, `git status --porcelain --untracked-files=all --ignored` must print nothing (tested in clone D in Windows PowerShell 5.1, PowerShell 7.6.6 and Git Bash; there it printed only the fixed script that had been copied in).

## 6. Verification record

* **Date:** 2026-10-02; re-verified on 2026-10-07 (last item of this part).
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of `main` on https://github.com/once-ere/Dirac_claude.git when the fresh clones were made (re-verification of 2026-10-07: `a4c5eda1df069a43a55ff8b57148f5de8edd1670`). The two files of this set are unchanged since commit `fbec4d7` (2026-09-25). No uncommitted file was copied into clones A and B. Clones C and D received only the fixed script (sha256 `9b94c222646286785b6ac6fa6ba328fd0158ac74c91b3ab2ed69f16058a0e87d`), copied from the working tree.
* **Environment:**
  * Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 cores;
  * Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence;
  * WolframScript 1.14.0;
  * PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444 (clone D only), Git 2.51.2.windows.1 with its Git Bash.

  Python 3.14.5 was used only for the measurement helpers, not by this set.
* **How the runs were made.** In clones A to C, "PowerShell" means PowerShell 7.6.6. Runs marked "PowerShell, watched" were started from PowerShell 7.6.6 with `Start-Process` and polled every 0.25 s for the peak working set of every process under `wolframscript.exe`. The other PowerShell runs were typed directly and timed with `Measure-Command`. The Git Bash runs were timed with `date`. In clone D, the PowerShell runs were made from `.ps1` files run with `powershell.exe -File` (Windows PowerShell 5.1) or `pwsh -File` (PowerShell 7.6.6), which pass arguments to programs exactly as typed commands do, and were timed with `Measure-Command`. All runs were made from the repository root of a fresh clone. "Identical" means byte-identical to the committed notebook, sha256 `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe`.

| Run | Clone | Shell | Command form | Exit | Wall time | Peak kernel memory | Notebook |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | A | PowerShell, watched | default | 0 | 4.19 s | 155.0 MB | identical |
| R2 | A | PowerShell, watched | default | 0 | 3.86 s | 150.0 MB | identical, and identical to R1 |
| R3 | B | PowerShell, watched | default | 0 | 3.60 s | 150.3 MB | identical |
| R4 | B | Git Bash | default | 0 | 3.62 s | not measured | identical |
| R5 | B | Git Bash | output path `build/nbcheck/...` (folder did not exist) | 0 | 3.39 s | not measured | identical |
| R6 | B | Git Bash | `-- build/dashdash/...` | 0 | not timed | not measured | written to `build/dashdash/`, not fingerprinted (repeated as R13); committed notebook not rewritten (its modification time was unchanged) |
| R7 | B | PowerShell | `-- build/dashdash-ps/...` | 0 | 3.78 s | not measured | written to `build/dashdash-ps/`, not fingerprinted (repeated as R14); committed notebook not rewritten |
| R8 | B | PowerShell | default | 0 | 3.89 s | not measured | identical |
| R9, R10, R11 | B | PowerShell, watched | default | 0 | 4.36, 5.06, 4.90 s | 154.9, 155.4, 155.0 MB | identical |
| R12 | B | PowerShell | output path `build/rebuilt/...` | 0 | not timed | not measured | identical; the old form of check 5 (`Get[...] === Get[...]`, a bare `True` or `False`) printed `True` in PowerShell 7.6.6 and in Git Bash |
| R13 | B | Git Bash | `-- build/dashdash/...` | 0 | 2.74 s | not measured | identical; committed notebook not rewritten |
| R14 | B | PowerShell | `-- build/dashdash-ps/...` | 0 | 1.87 s | not measured | identical; committed notebook not rewritten |
| R15, R16 | C (fixed script) | PowerShell, watched | default | 0 | 4.44, 4.94 s | 154.8, 149.9 MB | identical, and identical to each other |
| R17 | C (fixed script) | PowerShell | output path `build/new/deeper/...` (two new folders) | 0 | not timed | not measured | identical |
| R18 | D (fixed script) | Windows PowerShell 5.1 | default | 0 | 3.25 s | not measured | identical |
| R19 | D (fixed script) | Windows PowerShell 5.1 | output path `build/rebuilt/...` (`build/` did not exist; `build/` and `build/rebuilt/` were created) | 0 | 4.60 s | not measured | identical |
| R20 | D (fixed script) | Windows PowerShell 5.1 | `-- build/dashdash51/...` | 0 | not timed | not measured | identical, written to `build/dashdash51/` |
| R21 | D (fixed script) | PowerShell 7.6.6 | default | 0 | 3.37 s | not measured | identical |
| R22 | D (fixed script) | PowerShell 7.6.6 | output path `build/rebuilt/...` (`build/` did not exist) | 0 | 3.38 s | not measured | identical |
| R23 | D (fixed script) | Git Bash | output path `build/rebuilt/...` (`build/` did not exist) | 0 | 3.56 s | not measured | identical |
| R24 to R27 | D (fixed script) | PowerShell 7.6.6 | default | 0 | 5.44, 3.82, 3.39, 3.66 s | not measured | identical (first 12 hex digits of the sha256 printed after each run; `git status` showed no change of the notebook afterwards) |
| R28 to R30 | D (fixed script) | Windows PowerShell 5.1 | default | 0 | 3.51, 3.45, 3.79 s | not measured | identical (as R24 to R27) |
| R31 to R33 | D (fixed script) | Git Bash | default (standard output discarded) | 0 | 3.98, 3.33, 3.80 s | not measured | identical (as R24 to R27) |
| R34 | D (fixed script) | Windows PowerShell 5.1 | output path `"build/my folder/..."` (quoted, with a space) | 0 | not timed | not measured | identical |
| R35 | D (fixed script) | PowerShell 7.6.6 | output path `"build/my folder/..."` (quoted, with a space) | 0 | not timed | not measured | identical |

  The two repeated runs from one fresh clone that this record requires are R1 and R2. They were made in clone A, one after the other. Both notebooks are identical to the committed one and to each other. Clone D repeats this with the fixed script: R18, R21 and R24 to R33 are 12 default runs in one fresh clone, all identical to the committed notebook.

  In every run, standard output was the three lines of Part 4.1, and standard error was empty. Within one clone these lines were byte-identical from run to run (R1 = R2; R3 = R4 = R9 = R10 = R11; R15 = R16); between clones they differed only in the folder name. After every run in clones A and B in which the default path was used, `git status --porcelain --untracked-files=all` printed nothing. In clone C it printed only ` M scripts/build_dirac16complex_mathematica_notebook.wls`, the fixed script that had been copied in, and no change to the notebook. After the scratch folders were deleted, `git status --porcelain --untracked-files=all --ignored` printed nothing either. In clone D, every run whose standard output was kept printed the three lines of Part 4.1, and after every restore (`Remove-Item -Recurse -Force build` or `rm -rf build`) `git status --porcelain --untracked-files=all --ignored` printed only ` M scripts/build_dirac16complex_mathematica_notebook.wls`.
* **Check counts:** the set has no checks of its own (Part 4.1). The byte comparison passed in every run whose output was fingerprinted: 15 of 15 in clones A to C and 18 of 18 in clone D, 33 of 33 on 2026-10-02; 7 of 7 in clone E on 2026-10-07; 40 of 40 in all.
* **Re-check after the independent review (clone D, 2026-10-02).** The review reported that checks 4 and 5 of Part 3.4, as they were then written, fail in Windows PowerShell 5.1, and that the old check 5 (`Get[...] === Get[...]`, which printed a bare `True` or `False`) then prints a false `True`. Confirmed in clone D:
  * Windows PowerShell 5.1, old check 4 as written: one `Get::stream` message, two `Part::partd` messages and one `Tally::listrp` message, then `{Symbol, 2, Tally[$Failed[[1,All,2]]], Missing[KeyAbsent, TaggingRules]}`, exit code 0.
  * Windows PowerShell 5.1, old check 5 as written: two `Get::stream` messages and then `True`, both for the rebuilt notebook and for a deliberately different notebook `build/different/Dirac16ComplexDarkSector.nb` containing `Notebook[{Cell["a different notebook", "Text"]}]`.
  * Windows PowerShell 5.1, the new check 5 (which prints the heads) in its first form: `{Symbol, Symbol, True}` after two `Get::stream` messages, exit code 0, so the failure is now visible.
  * Windows PowerShell 5.1, the forms with `\"`: check 4 printed the expected line of Part 3.4; check 5 printed `{Notebook, Notebook, True}` for the rebuilt notebook and `{Notebook, Notebook, False}` for the different one.
  * PowerShell 7.6.6 (`$PSNativeCommandArgumentPassing` = `Windows`) and Git Bash, the first forms: check 4 printed the expected line; check 5 printed `{Notebook, Notebook, True}` for the rebuilt notebook and `{Notebook, Notebook, False}` for the different one.
  * PowerShell 7.6.6 and Git Bash, the forms with `\"`: `ToExpression::sntx: Invalid syntax in or before "..."`, then `$Failed`, exit code 0; never a false `True`.
  * In Windows PowerShell 5.1, `wolframscript -code '$Version'`, `Get-FileHash`, `$LASTEXITCODE`, `Measure-Command`, `git status --porcelain -- <file>`, `git diff --quiet -- <file>` (exit code 0), the `--` form (R20) and a quoted output path with a space (R34) worked as in PowerShell 7.
  * Final text test: the build command of Part 3.3 and the commands of checks 4 and 5 were copied byte for byte from this file into a `.ps1` file for each PowerShell and a `.sh` file for Git Bash (the `\"` forms for Windows PowerShell 5.1, the first forms otherwise) and run in clone D, followed by the restore command of Part 5. In all three shells, check 4 printed exactly the expected line of Part 3.4, check 5 printed `{Notebook, Notebook, True}`, and `build` was gone afterwards. These three output-path runs are not counted among R18 to R35; their notebooks were compared only by check 5.

  Part 3.1 now explains the two PowerShells, Part 3.4 gives both forms of checks 4 and 5 and the new check 5 prints `{Head[a], Head[b], a === b}`, so that a check in which no file was read can no longer look like a pass. Part 3.5 has rows for both quoting mistakes. These are corrections of this file only; the builder script was not changed again.
* **Fix made (execution defect, not science).** When the output file could not be written, the unfixed script printed `Put::noopen`, `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`. It then still printed `cell_count=72`, `input_cell_count=37` and `output=<path>`, and exited with code 0. This was reproduced in clone B with a read-only output file, which kept its old content.

  Now each write step is checked: `Put` must not return `$Failed`, the read-back must be a string, `OpenWrite` must return an `OutputStream`, and the written size must equal the number of bytes intended. If a check fails, the script prints `ERROR: could not write the notebook (<step>): <path>` and exits with code 1.

  Diff summary: 13 insertions and 2 deletions (two lines changed, eleven added), all in the write section at the end of the script. The cell code and the notebook expression are untouched. The script's sha256 changes from `126f18b974f332a055b42bac3708b5f31bc788d8f288401f5f9630f354243112` (1045 lines) to `9b94c222646286785b6ac6fa6ba328fd0158ac74c91b3ab2ed69f16058a0e87d` (1056 lines).

  The fix was re-verified in fresh clone C, into which only the fixed script was copied:
  * R15 and R16 (default): exit 0, notebook identical;
  * R17 (new nested folder): exit 0, notebook identical;
  * a read-only output file: `ERROR: could not write the notebook (Put): ...`, exit 1, old file kept;
  * an output folder whose parent is a file: `ERROR: could not write the notebook (Put): ...`, exit 1.
* **Other observation (WolframScript, not this script).** When the command was typed in a wrong folder (`notebooks/` instead of the repository root), WolframScript 1.14.0 printed `Failed to open file at path: scripts/build_dirac16complex_mathematica_notebook.wls` and still gave exit code 0. Part 3.5 therefore tells students to look for the three printed lines, not only at the exit code.
* **Open discrepancies:** none. No number or physics check is involved in this set.

  The comments of the Stage-3 gates say that WolframScript 1.14.0 drops `--` and every argument after it. A control test explains when that happens:
  * A test script that starts with `#!/usr/bin/env wolframscript` (as this builder does) received `{"<script>", "--", "out/x.nb"}` in `$ScriptCommandLine`.
  * The same test without that first line received only `{"<script>"}`.

  So with this builder, `--` before the output path is harmless (R6, R7, R13, R14). For a script without that first line, the argument would be lost. This note concerns only how the command line is passed, not any result.
* **Re-verification of 2026-10-07 (fresh clone E).** The earlier verification was interrupted by a session limit before it was finished, so this file and the fix were checked again instead of being trusted.
  * **Commit:** `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, the head of `main` on https://github.com/once-ere/Dirac_claude.git when clone E was made (the local repository was at the same commit). In clone E the script had the sha256 `9b94c222646286785b6ac6fa6ba328fd0158ac74c91b3ab2ed69f16058a0e87d` (1056 lines, the fixed script of the item "Fix made" above) and the notebook `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe`, the same as in the working tree of the local repository. No file was copied into clone E. Directly after the clone, `git status --porcelain --untracked-files=all --ignored` printed nothing.
  * **Environment:** Windows 11 Pro for Workstations 10.0.26300 (build 26300.9457; the machine had been updated from build 26200 since 2026-10-02), 24 cores; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence; WolframScript 1.14.0; PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444; Git 2.51.2.windows.1 with its Git Bash (`core.autocrlf=true`, made harmless by `.gitattributes`, Part 3.2). Python 3.14.5 was used only to inspect the bytes of the output.
  * **Runs.** All from the repository root of clone E. "Watched" means started from PowerShell 7.6.6 with `Start-Process` and polled every 0.25 s for the peak working set of every process under `wolframscript.exe`. The Git Bash runs were timed with `date`, the two PowerShell runs E6 and E7 with `Measure-Command` inside a `.ps1` file run with `powershell.exe -File` or `pwsh -File`. "Identical" means byte-identical to the committed notebook (compared with `cmp` against the blob of `HEAD` and with sha256).

    | Run | Shell | Command form | Exit | Wall time | Peak kernel memory | Notebook |
    | --- | --- | --- | --- | --- | --- | --- |
    | E1 | PowerShell 7.6.6, watched | default | 0 | 3.98 s | 151.9 MB | identical |
    | E2 | PowerShell 7.6.6, watched | default | 0 | 3.92 s | 151.8 MB | identical, and identical to E1 |
    | E3 | Git Bash | default | 0 | 4.88 s | not measured | identical |
    | E4 | Git Bash | output path `build/rebuilt/...` (`build/` did not exist) | 0 | 6.66 s | not measured | identical, written to `build/rebuilt/` |
    | E5 | Git Bash | `-- build/dashdash/...` | 0 | 5.56 s | not measured | identical, written to `build/dashdash/` |
    | E6 | Windows PowerShell 5.1 | default | 0 | 5.71 s | not measured | identical |
    | E7 | PowerShell 7.6.6 | default | 0 | 5.68 s | not measured | identical |

    E1 and E2 are the two runs one after the other from one fresh clone that this record requires: both notebooks are byte-identical to the committed one and to each other, and their standard output (236 bytes each, the three lines of Part 4.1 with CR LF) is byte-identical too. In every run, standard output was the three lines of Part 4.1 (`cell_count=72`, `input_cell_count=37`, `output=<absolute path>`) and standard error was empty. In E1 and E2 the modification time of the committed notebook changed while its bytes stayed the same (Part 5).
  * **Repository state.** After E1 and E2, `git status --porcelain --untracked-files=all` printed nothing; after E3, E6 and E7 the same command with `--ignored` added printed nothing. After E4, `git status --porcelain --untracked-files=all` still printed nothing, and with `--ignored` added it printed only `!! build/rebuilt/Dirac16ComplexDarkSector.nb`, the ignored scratch output. After E5 and the failure tests of the fix below, `git status --porcelain --untracked-files=all` still printed nothing. After `rm -rf build`, `git status --porcelain --untracked-files=all --ignored` printed nothing.
  * **Checks of Part 3.4** (after E4, with `build/rebuilt/` present). The commands were copied from Part 3.4 into a `.ps1` file for each PowerShell, and typed in Git Bash. Check 4 printed exactly the expected line of Part 3.4 and check 5 printed `{Notebook, Notebook, True}`, both with exit code 0, in PowerShell 7.6.6 (first forms), Windows PowerShell 5.1 (the forms with `\"`) and Git Bash (first forms). In PowerShell 7.6.6, `Get-FileHash` printed `708804E7F4BB902221418EBCFCBBB5E91ABCC9BF4773F067BFA61E6F2E304FFE`, `git status --porcelain -- notebooks/Dirac16ComplexDarkSector.nb` printed nothing and `git diff --quiet` gave exit code 0.
  * **Format of the output** (inspected byte by byte): 354930 bytes, pure ASCII, 5048 LF, no CR, no spaces or tabs before a line end, no newline after the last line, longest line 79 characters, first bytes `Notebook[{Cell["dirac16complex dark sector: symbolic reduction and NDSolve \`, last bytes `"SchemaVersion" -> 1|>]`. All as in Part 4.2.
  * **The fix, checked again** (Git Bash, clone E): a read-only output file `build/ro/x.nb` gave `Put::noopen: Cannot open ...` and `ERROR: could not write the notebook (Put): <path>`, exit code 1, and the file kept its old content; an output path below a file (`build/afile/sub/x.nb`, where `build/afile` is a file) gave the same `ERROR` line and exit code 1. Started in the wrong folder (`notebooks/`), WolframScript 1.14.0 printed `Failed to open file at path: scripts/build_dirac16complex_mathematica_notebook.wls` and again gave exit code 0, as Part 3.5 says.
  * **Fixes made on 2026-10-07:** none. The script was not changed; this file was updated with the new record (and the history of the script in Part 2).
  * **Open discrepancies:** none.
