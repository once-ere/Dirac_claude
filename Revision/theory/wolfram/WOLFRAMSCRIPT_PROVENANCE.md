# Provenance of the wolframscript set `Revision/theory/wolfram/` (the field theory of dirac16complex and dirac16complex00, and the scope of its statements)

Status: both scripts of this set were executed twice, each time in a fresh clone of
`https://github.com/once-ere/Dirac_claude.git` at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, on
2026-10-02. Both runs of both scripts finished with exit code 0 (84 of 84 and 15 of 15 checks PASS), and
every output file was byte-identical to the committed file and between the two runs. No fix was needed.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

Two WolframScript programs prove, with exact computer algebra, the mathematical statements of the
"Revision" field theory of the author's 16-component spinor field in the author's 8-dimensional primordial
gravitational field, and write the verdicts (and the exact formulas) to JSON files that the documents of
the repository quote.

### 1.2 The physics, in plain words

* The world of the theory has 8 coordinates, named as the author names them: `x1, x2, x3` are ordinary
  space; `x4` is ordinary time; `x5, x6, x7` are three extra TIME directions, which shrink ("deflate")
  exponentially while ordinary space expands; `x8` is a hidden space direction. The signature is 4 + 4
  (four space-like and four time-like directions).
* The gravitational field is the author's primordial metric. It depends on `x4` through a function
  `a4(x4)` and on `x8` through `z = 6 H x8` with a constant `H > 0` and `0 < z < Pi/2`.
* The matter field is a spinor with 16 complex components (a larger relative of the electron's Dirac
  field), in two versions: `dirac16complex`, whose components ANTICOMMUTE (Grassmann numbers; the scripts
  call this statistics `G`), and `dirac16complex00`, whose components commute (statistics `C`).
* The field is coupled to gravity through a vielbein (a "frame" at every point) and the canonical spin
  connection. The scripts derive the Lagrangian, the field equations, the conserved current, the
  energy-momentum tensor and the canonical quantisation, and test what each statement does and does not
  depend on.

### 1.3 How the scripts prove it

Nothing is computed with rounded (floating-point) numbers. Each statement is turned into an exact symbolic
computation (fractions, square roots, symbols such as `H`, `a4[x4]`, `m`, `lam`, and general unknown field
functions) whose result must be exactly zero or exactly `True`. Each such computation is a CHECK with a
name and a verdict `PASS` or `FAIL`. A script exits with code 0 only if every one of its checks passes.

`verify_field_theory.wls` (84 checks) loads the package `RevisionFieldTheory.wl` and works through these
sections (the names are printed on the screen while it runs):

| section (as printed) | checks | what is verified |
| --- | --- | --- |
| (before the first section) | 1 | the exact zero test used by all later checks returns True on identities and False on nonzero control expressions |
| `fixture` | 2 | the gamma matrices read from `Revision/algebra/gammas.json` satisfy `{gamma^a, gamma^b} = 2 eta^ab` with `eta = diag(1,1,1,-1,-1,-1,-1,1)`; the matrices `C`, `B`, `Gamma`, `S^ab` are the stated products |
| `geometry` | 8 | the diagonal vielbein reproduces the author's metric; `sqrt|det g| = Cos[z]`; `H = 0` is a degenerate limit; 25 nonzero Christoffel symbols; Ricci tensor and Ricci scalar `R = 6 (a4'^2 - 7 H^2)`; the metric is curved for every `H > 0` |
| `spin connection` | 7 | vielbein postulate, the 12 nonzero spin-connection components, covariant constancy of the gammas, spin curvature equals the Riemann tensor |
| `gamma^mu Omega_mu` | 3 | `gamma^mu Omega_mu = 3 H gamma^(x8)` exactly; the `a4'` terms of the 3 inflating and the 3 deflating directions cancel |
| `Lagrangian, both statistics` | 7 | explicit Grassmann algebra; the Lagrangian is real; symmetrised and unsymmetrised forms differ by a total divergence; the spin connection drops out of the symmetrised Lagrangian |
| `Euler-Lagrange equations` | 11 | the field equation `gamma^mu D_mu Psi = (m + U'(S)) Psi` and its adjoint, from the Euler-Lagrange derivative of every component; the explicit Dirac operator; the chiral block form; the first-order evolution form in `x4` |
| `non-triviality` | 3 | the gravitational terms do not drop out: `gamma^mu D_mu Psi - gamma^mu d_mu Psi = 3 H gamma^(x8) Psi`, nonzero for every `H > 0`; the spin connection vanishes only if `a4' = 0` and `H = 0` |
| `current and integrability` | 8 | the conserved current, its reality, the charge density `Psi^dagger B Psi` (an indefinite form), the Lichnerowicz identity |
| `Majorana-type Lg` | 2 | negative control: a Majorana-type Lagrangian with real anticommuting components is a total derivative (it gives no field equation) |
| `energy-momentum tensor by vielbein variation` | 4 | the energy-momentum tensor from the exact first-order vielbein variation, and its symmetric (Belinfante) part |
| `Noether identities` | 5 | the identities of coordinate invariance and local Lorentz invariance; conservation on shell |
| `EMT components` | 9 | diagonal components, trace, kinetic sum on shell, the `x4`-`x8` component, the energy-exchange equations |
| `exact solutions and conservation` | 5 | exact solutions (linear, and nonlinear homogeneous for both statistics) satisfy the field equation and the conservation of the energy-momentum tensor and of the current |
| `canonical quantisation` | 9 | canonical momentum, the anticommutator `{Psi, Psi^dagger} = B delta / sqrt|g|`, Heisenberg equation = field equation, no positive inner product (Krein space), mode Hamiltonian, explicit Fock-space example |

The last section, `writing outputs`, writes the two output files of section 2.3.

`verify_scope.wls` (15 checks) is an independent program (it does not load `RevisionFieldTheory.wl`). It
tests the SCOPE of the statements: which values depend on the choice of frame and of field variables, what
holds only up to boundary terms, and what the indefinite structures imply.

| group | checks | what is verified |
| --- | --- | --- |
| `fixture_gammas` | 1 | the gammas of `Revision/algebra/gammas.json` satisfy the Clifford relation; `C` and `B` are the stated products |
| `boosted_frame_*` | 5 | a frame boosted in the `x4`-`x8` plane reproduces the same metric and its canonical connection satisfies the vielbein postulate; in it `gamma^mu Omega_mu` has a different value and vanishes for the rapidity `6 H x4 + b0`, while the spinor curvature stays nonzero |
| diagonal frame and field variables | 5 | the rescaling `Psi = Sin[z]^(-1/2) chi` removes the term `3 H gamma^(x8)` (for `U = 0`); this term does not see the deflation `a4`; the connection-free Lagrangian gives the same equations; the spin connection does enter the energy-momentum tensor |
| boundary terms | 2 | the curved mode operator is Hermitian only up to a boundary term at `z = Pi/2`; without a boundary condition it has complex frequencies |
| growth and energy | 2 | growth rates of extra-time modes are unbounded; the classical energy of `dirac16complex00` is unbounded below |

### 1.4 Which documents and programs use its results

* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 (record table:
  "Wolfram: 84 of 84 checks pass", "Wolfram: 15 of 15 checks pass"), formulas and check names throughout
  the text, section 16 (reproduction) and section 17 (index of formulas and checks).
* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 (record table),
  formula blocks generated from `Revision/theory/field-theory.json` (for example the 16 component field
  equations of section 5), section 14 (check index) and section 16 (reproduction; it records an earlier
  Wolfram run time of 1029 s for `verify_field_theory.wls`).
* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): section 9.1 (count table: 84
  checks, 84 PASS) and section 10 (reproduction).
* `Revision/README.md`: the row of the folder `theory/` ("Wolfram 84/84 ... scope Wolfram 15/15").
* `Revision/theory/python/check_field_theory.py` with `Revision/theory/python/compare_wolfram.py`: the
  independent sympy verifier reads `Revision/theory/field-theory.json` and
  `Revision/theory/reports/wolfram-field-theory.json` and compares them with its own derivation (section
  `comparison_with_wolfram` of `Revision/theory/reports/python-field-theory.json`).
* The publication tests `Revision/tests/test_dirac16complex_field_theory_publication.py`,
  `Revision/tests/test_dirac16complex00_field_theory_publication.py` and
  `Revision/tests/test_pair_creation_proofs_publication.py` re-read the reports and require every cited
  check to exist with verdict PASS and every quoted count to match.
* `Revision/lead_checks/charge_conjugation_and_u1.py` takes its conventions from the keys `Lagrangian`,
  `current` and `quantisation` of `Revision/theory/field-theory.json`.

## 2. Files

All files are plain text, UTF-8 (in fact pure ASCII), with LF line endings and a final newline. "Lines" is
the number of newline characters.

### 2.1 The scripts and the package

| file | role | lines | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `Revision/theory/wolfram/verify_field_theory.wls` | script: 84 checks; writes the field-theory report and the formula file | 734 | 73873 | `dafe62233cf76106e1dc7bca51ad3aafcf62762eaf37c3af9969f0c955014c9d` |
| `Revision/theory/wolfram/RevisionFieldTheory.wl` | package loaded by `verify_field_theory.wls` (geometry, Grassmann algebra, Lagrangian, Euler-Lagrange derivative, vielbein variation) | 292 | 18269 | `31528570831302199c15a5d6f95e8b95a3ed6532a1c3360c4fc526e8f9dad71d` |
| `Revision/theory/wolfram/verify_scope.wls` | script: 15 checks; writes the scope report | 205 | 17177 | `41b9e4a52dcbffe60e6decf62835ece0aef9f5c3388aac7d22236b7f20d6e499` |

Both scripts find their other files relative to their own location (`$InputFileName`), so they work from
any current folder; the usage line in their headers runs them from the repository root.

### 2.2 Inputs (read only, never modified)

| file | read by | lines | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `Revision/algebra/gammas.json` | both scripts | 1405 | 76968 | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` |
| `Revision/theory/wolfram/RevisionFieldTheory.wl` | `verify_field_theory.wls` | (section 2.1) | | |

`gammas.json` holds the 8 gamma matrices (16 x 16, exact rational entries) and the derived matrices `C`,
`B`, `Gamma`, `S^ab` and `eta`. It is committed; it is produced by the separate set
`Revision/algebra/wolfram/` (`verify_algebra.wls`), which you do NOT need to run first. No other file is
read, and nothing is downloaded.

### 2.3 Outputs (rewritten in full on every run; LF, UTF-8, no time stamps, deterministic)

| file | written by | lines | bytes | sha256 of the committed (and reproduced) file |
| --- | --- | --- | --- | --- |
| `Revision/theory/reports/wolfram-field-theory.json` | `verify_field_theory.wls` | 95 | 35018 | `eed5e0fb01b281d58ccabe7dd84bde3b81574ae09a9c4b05e67f22f6a8065a7e` |
| `Revision/theory/field-theory.json` | `verify_field_theory.wls` | 68 | 24609 | `2a3c83e5db5e0ad3572791334a4797b8af549a22295bb6800739340f2c107f54` |
| `Revision/theory/reports/wolfram-scope.json` | `verify_scope.wls` | 25 | 6996 | `8a0bee2e9c0b536ed25c6dcb31272e6e0d7a49ae9e1f69a755899ce6efa021ce` |

* `wolfram-field-theory.json`: every check with its name, verdict and a sentence stating exactly what was
  verified, and the summary `{"passed": 84, "failed": 0, "total": 84}`.
* `field-theory.json`: 32 exact formula records (Wolfram `InputForm` text) for the documents, from
  `christoffel_nonzero` to `eta`, each verified by a named check.
* `wolfram-scope.json`: the 15 scope checks and the summary `{"passed": 15, "failed": 0, "total": 15}`.

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, and an internet connection for the installation,
  the activation and the download (the scripts themselves use no network).
* About 600 MB of free disk space for the repository (a fresh clone measured 519 MB including its git
  history) plus the space the Wolfram installer asks for.
* About 1 GB of free memory (the Wolfram kernel peaked at 578 MB for `verify_field_theory.wls` and at
  227 MB for `verify_scope.wls`).
* Time: `verify_scope.wls` takes about half a minute; `verify_field_theory.wls` takes about 17 to 30
  minutes (section 4.4). Keep the computer awake while it runs.
* A Wolfram kernel with WolframScript: either the free Wolfram Engine for Developers or a licensed
  Mathematica / Wolfram desktop installation. The verification used Wolfram 15.0.1 with WolframScript
  1.14.0; older versions were not tested.
* Git, to download the repository. Python, Jupyter and Rust are NOT needed for this set.

### 3.2 Open a terminal

* Windows: press the Windows key, type `PowerShell`, and open "Windows PowerShell" or "PowerShell 7". All
  Windows commands below are typed there.
* macOS: open Finder, then Applications, Utilities, Terminal.
* Linux: open your distribution's Terminal application (often Ctrl+Alt+T).

Type each command exactly as shown and press Enter after each line.

### 3.3 Install Wolfram and WolframScript

Choose ONE option.

Option A, the free Wolfram Engine for Developers:

1. In a web browser open `https://www.wolfram.com/engine/`, follow its download link, and follow the page
   to obtain the free licence. You need a Wolfram ID (an account at `https://account.wolfram.com`); read
   the licence terms yourself before you accept them.
2. Download the installer for your operating system and run it:
   * Windows: double-click the downloaded `.exe` and accept the defaults. WolframScript normally comes with
     it, in `C:\Program Files\Wolfram Research\WolframScript\` (the folder used on the verification
     machine); if the test below says "not recognized", use option C.
   * macOS: open the downloaded `.dmg` and follow its instructions (drag the application to Applications,
     and install WolframScript if the disk image offers it).
   * Linux: in the folder of the download run `sudo bash <name of the downloaded file>.sh` and accept the
     offer to create the command links in `/usr/local/bin`.
3. Close the terminal and open a new one, so that it finds the new program.
4. Activate the engine once: run `wolframscript -activate` and enter your Wolfram ID and password when
   asked (in your own terminal; never give them to anyone else).

Option B, Mathematica or the Wolfram desktop application (already licensed and activated): WolframScript
is part of the installation. On Windows it is in `C:\Program Files\Wolfram Research\WolframScript\`. On
macOS it is inside the application bundle (for example
`/Applications/Mathematica.app/Contents/MacOS/wolframscript` or
`/Applications/Wolfram.app/Contents/MacOS/wolframscript`, depending on the version); the simplest way to
make the plain command `wolframscript` work in Terminal is option C.

Option C, if `wolframscript` is still "not found": download the free WolframScript installer for your
system from `https://www.wolfram.com/wolframscript/`, install it, and open a new terminal.

Test the installation (all systems; type the single quotes):

```text
wolframscript -version
wolframscript -code '$Version'
```

The first prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`; the second prints
the version of the kernel, on the verification machine
`15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. If the second asks for activation, do step 4 of
option A. (With double quotes instead of single quotes, PowerShell and the macOS/Linux shells replace
`$Version` by an empty text before WolframScript sees it.)

### 3.4 Install Git and download the repository

Install Git if `git --version` does not print a version:

* Windows: download and run the installer from `https://git-scm.com/download/win` (or run
  `winget install --id Git.Git -e`), then open a new PowerShell window.
* macOS: run `xcode-select --install` (or, with Homebrew, `brew install git`).
* Linux: `sudo apt install git` (Debian, Ubuntu) or `sudo dnf install git` (Fedora).

Download the repository into your home folder and enter it.

Windows PowerShell:

```powershell
cd $HOME
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

macOS and Linux:

```bash
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The download took 7 to 14 seconds on the verification machine. You are now in the repository root: the
folder that contains the folder `Revision`. Every command below is run from here. The repository stores
every file byte for byte (its file `.gitattributes` contains `* -text`), so the files are identical on
every system, whatever your Git line-ending setting is.

Optional: confirm that you have the verified versions of the three files of section 2.1. Windows
PowerShell (it prints the hashes in capital letters):

```powershell
Get-FileHash Revision/theory/wolfram/verify_field_theory.wls, Revision/theory/wolfram/RevisionFieldTheory.wl, Revision/theory/wolfram/verify_scope.wls
```

macOS: `shasum -a 256 Revision/theory/wolfram/verify_field_theory.wls Revision/theory/wolfram/RevisionFieldTheory.wl Revision/theory/wolfram/verify_scope.wls`;
Linux: the same with `sha256sum` instead of `shasum -a 256`. Compare with the table of section 2.1. If
they differ, the set was changed after this record was written; the instructions still apply, but the
expected output of section 4 may differ.

### 3.5 Run the scripts

Run the short script first (it shows within a minute that everything works), then the long one. The order
does not matter for the results: each script reads only `Revision/algebra/gammas.json` (and the field
script its package), never the output of the other. Run them one after the other, not at the same time
(each uses one Wolfram kernel).

Windows PowerShell (forward slashes and backslashes both work):

```powershell
wolframscript -file Revision/theory/wolfram/verify_scope.wls
$LASTEXITCODE
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
$LASTEXITCODE
```

macOS and Linux:

```bash
wolframscript -file Revision/theory/wolfram/verify_scope.wls
echo "exit code: $?"
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
echo "exit code: $?"
```

The line after each `wolframscript` command shows that command's exit code; type it immediately after the
script has finished, because it reports the most recent command. While `verify_field_theory.wls` runs, the
screen can show no new line for about 10 minutes (sections `energy-momentum tensor by vielbein
variation`, `Noether identities` and `exact solutions and conservation`); this is normal, do not stop it.

Optional, to measure the run time: in PowerShell
`Measure-Command { wolframscript -file Revision/theory/wolfram/verify_scope.wls | Out-Host }` (the output is
shown, then `TotalSeconds`; `$LASTEXITCODE` afterwards still gives the exit code), on macOS and Linux
`time wolframscript -file Revision/theory/wolfram/verify_scope.wls` (and the same for
`verify_field_theory.wls`).

### 3.6 Check the result

1. The last printed line of `verify_scope.wls` must begin with `15/15 checks passed`, the last line of
   `verify_field_theory.wls` with `84/84 checks passed`, no line may begin with `FAIL`, and both exit
   codes must be `0`.
2. The summary lines of the two reports. Windows PowerShell:

   ```powershell
   Select-String -Pattern '"summary"' -Path Revision/theory/reports/wolfram-field-theory.json, Revision/theory/reports/wolfram-scope.json
   ```

   prints

   ```text
   Revision\theory\reports\wolfram-field-theory.json:8:  "summary": {"passed": 84, "failed": 0, "total": 84},
   Revision\theory\reports\wolfram-scope.json:7:  "summary": {"passed": 15, "failed": 0, "total": 15},
   ```

   macOS and Linux:

   ```bash
   grep '"summary"' Revision/theory/reports/wolfram-field-theory.json Revision/theory/reports/wolfram-scope.json
   ```

   prints the same two lines in the form
   `Revision/theory/reports/wolfram-field-theory.json:  "summary": {"passed": 84, "failed": 0, "total": 84},`.
3. The three outputs are byte-identical to the committed files. Windows PowerShell:

   ```powershell
   Get-FileHash Revision/theory/reports/wolfram-field-theory.json, Revision/theory/field-theory.json, Revision/theory/reports/wolfram-scope.json
   git status --porcelain Revision/theory
   ```

   macOS: `shasum -a 256 Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json Revision/theory/reports/wolfram-scope.json`,
   Linux: the same with `sha256sum`, and on both `git status --porcelain Revision/theory`. The hashes
   must be those of the table in section 2.3 (PowerShell prints them in capital letters), and
   `git status --porcelain Revision/theory` must print nothing at all (an empty answer means that no file
   under `Revision/theory` differs from the committed version).

### 3.7 What to do if it fails

* `wolframscript : The term 'wolframscript' is not recognized ...` (PowerShell) or
  `wolframscript: command not found` (macOS, Linux): WolframScript is not installed or not on the PATH.
  Install it (section 3.3, option C) and open a NEW terminal. On Windows you can also run it by its full
  path: `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file Revision/theory/wolfram/verify_scope.wls`.
* A request to activate, or a message that the kernel is not activated or the licence is invalid, BEFORE
  any `PASS` line: run `wolframscript -activate` (section 3.3, option A, step 4).
* The message `The product exited because an error occurred. For a product older than 12.1, this can mean
  that the product is unregistered.` printed AFTER the normal output (for example after the result `2` of
  `wolframscript -code '1+1'`), with exit code 1: this was observed intermittently on the verification
  machine while 10 to 20 other Wolfram kernels were running (2 of 11 short `-code` tests; none of the 8
  complete `-file` runs of this set with its input present). If the last line still says `84/84 checks passed` or
  `15/15 checks passed` and the checks of section 3.6 succeed, the run is valid; otherwise run the script
  again.
* The only output is `Failed to open file at path: Revision/theory/wolfram/verify_scope.wls` (or the same
  for `verify_field_theory.wls`): you are not in the repository root. CAUTION: WolframScript still returns
  exit code 0 in this case (observed during the verification), so always read the last line. Go to the
  folder that contains `Revision` (`cd $HOME\Dirac_claude` in PowerShell, `cd ~/Dirac_claude` on macOS and
  Linux) and run again.
* `Import::nffil: File ...gammas.json not found during Import.` followed by many messages and `FAIL` lines:
  the input `Revision/algebra/gammas.json` is missing (an incomplete download, or the file was moved).
  Observed during the verification with the file hidden on purpose: `verify_scope.wls` ended with
  `4/15 checks passed` and exit code 1 AND OVERWROTE `Revision/theory/reports/wolfram-scope.json` with
  the failing verdicts; `verify_field_theory.wls` printed the same message after `RevisionFieldTheory.wl
  loaded` and, a few lines later, `FAIL  fixture_Clifford_relation` (stop it with Ctrl+C; if the window
  does not react, close it). Restore the input and the outputs with
  `git checkout -- Revision/algebra/gammas.json Revision/theory/reports/wolfram-scope.json Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json`
  and run again.
* `Get::noopen` mentioning `RevisionFieldTheory.wl`: the package file is missing or renamed. Restore it
  with `git checkout -- Revision/theory/wolfram/RevisionFieldTheory.wl`.
* `OpenWrite::noopen`, `cannot write ...` or "permission denied": the outputs cannot be written. Close any
  program that has one of the output files open, make sure the folder is not read-only (clone into your
  home folder, not into a protected or synchronised folder), and run again.
* A message that no licence or no more kernels are available: another Wolfram program is using the
  allowed kernels. Close other Mathematica windows and other `wolframscript` commands and run again.
* The run was interrupted (Ctrl+C, window closed, computer asleep or switched off): the outputs are written
  only in the very last step (`writing outputs`), so an interrupted run changes no file of the repository
  (observed for three interrupted runs). Start the script again from the beginning.
* A line beginning with `FAIL`, a last line `N/84 checks passed` (or `N/15`) with N below the total, and
  exit code 1, although `gammas.json` is present: do not edit anything. Run `git status` and
  `git diff --stat` to see whether a file of the set or its input was changed; if so, restore them with
  `git checkout -- Revision/theory Revision/algebra/gammas.json` and run again. If an unmodified clone
  still fails, note the failing check names, their `detail` text in the report, and the output of
  `wolframscript -code '$Version'`, and report them: the verified result is 84 of 84 and 15 of 15 with
  Wolfram 15.0.1.
* `git status --porcelain Revision/theory` lists an output file although all checks passed: the file is
  not byte-identical to the committed one. Look at the difference with `git diff <file>`. The scripts
  write LF line endings on every system, so a program that converted line endings is the most likely
  cause; restore with the `git checkout -- ...` command of section 5.4 and run again. If the difference
  persists in a fresh clone, report it (on the verification machine every output was byte-identical).

## 4. Expected output

### 4.1 Printed on the screen by `verify_scope.wls`

16 lines: one `PASS` line per check, in this order, then the final verdict line. The numbers in brackets
are the seconds since the start and vary from run to run (also in their number of digits, for example
`[33.300000000000004 s]`); everything else is exactly as shown. Run 1 of the verification printed:

```text
PASS  fixture_gammas  [0.1 s]
PASS  boosted_frame_reproduces_metric  [1.5 s]
PASS  boosted_frame_canonical_connection  [1.7000000000000002 s]
PASS  boosted_frame_gammaOmega_formula  [2.1 s]
PASS  boosted_frame_gammaOmega_vanishes  [7.800000000000001 s]
PASS  boosted_frame_curvature_nonzero  [31.5 s]
PASS  rescaling_removes_the_connection_term  [32. s]
PASS  rescaled_equation_quadratic_potential  [32. s]
PASS  gammaOmega_blind_to_the_deflation  [32. s]
PASS  connection_free_lagrangian_same_equations  [32.4 s]
PASS  spin_connection_in_the_energy_momentum_tensor  [32.6 s]
PASS  good_sector_hermiticity_up_to_the_brane_flux  [32.9 s]
PASS  good_sector_x8_independent_modes_without_boundary_condition  [33.300000000000004 s]
PASS  extra_time_growth_rates_unbounded  [33.300000000000004 s]
PASS  commuting_field_energy_unbounded_below  [33.5 s]
15/15 checks passed; time 33.5 s
```

Final verdict line: `15/15 checks passed; time <seconds> s`. Exit code: `0`. Nothing is printed to the
error stream.

### 4.2 Printed on the screen by `verify_field_theory.wls`

103 lines: `RevisionFieldTheory.wl loaded`, then one `PASS` line per check (84), a line
`[<seconds> s] -> <section>` at the start of each section (15 lines; the number is the time spent in the
PREVIOUS section), two lines `   G vielbein variations: ...` and `   C vielbein variations: ...`, and the
final verdict line. The numbers vary from run to run; everything else is exactly as shown. Run 1 of the
verification printed:

```text
RevisionFieldTheory.wl loaded
PASS  zero_test_sanity
[0. s] -> fixture
PASS  fixture_Clifford_relation
PASS  fixture_C_B_S_consistent
[0. s] -> geometry
PASS  metric_is_the_authors
PASS  vielbein_inverse
PASS  sqrt_det_g_is_cos_z
PASS  degenerate_at_H_0
PASS  christoffel_count
PASS  ricci_scalar
PASS  ricci_mixed_components
PASS  never_flat_for_H_positive
[1. s] -> spin connection
PASS  vielbein_postulate
PASS  omega_antisymmetric
PASS  omega_components
PASS  Omega_components
PASS  gamma_covariantly_constant
PASS  S_rotates_gamma_with_omega
PASS  spin_curvature_equals_Riemann
[3.2 s] -> gamma^mu Omega_mu
PASS  gammaOmega_equals_3H_gamma_x8
PASS  gammaOmega_x4_terms_cancel
PASS  gammaOmega_divergence_form
[0.2 s] -> Lagrangian, both statistics
PASS  grassmann_algebra_structure
PASS  L_real_G
PASS  L_real_C
PASS  L_total_divergence_to_unsymmetrised_G
PASS  L_total_divergence_to_unsymmetrised_C
PASS  L_spin_connection_drops_out_G
PASS  L_spin_connection_drops_out_C
[7.300000000000001 s] -> Euler-Lagrange equations
PASS  EL_Psibar_G
PASS  EL_Psi_G
PASS  EL_Psibar_C
PASS  EL_Psi_C
PASS  adjoint_equation_is_Dirac_conjugate_G
PASS  adjoint_equation_is_Dirac_conjugate_C
PASS  Dirac_operator_explicit_G
PASS  Dirac_operator_explicit_C
PASS  block_form
PASS  evolution_form_G
PASS  evolution_form_C
[8. s] -> non-triviality
PASS  nontriviality_1_dirac16complex
PASS  nontriviality_2_dirac16complex00
PASS  Omega_vanishes_iff_a4prime_and_H_vanish
[0.7000000000000001 s] -> current and integrability
PASS  current_real_G
PASS  current_conservation_identity_G
PASS  charge_density_is_Krein_form_G
PASS  current_real_C
PASS  current_conservation_identity_C
PASS  charge_density_is_Krein_form_C
PASS  Lichnerowicz_identity_G
PASS  Lichnerowicz_identity_C
[19.8 s] -> Majorana-type Lg
PASS  Majorana_Lg_total_derivative_grassmann
PASS  Majorana_Lg_commuting_control
[1.8 s] -> energy-momentum tensor by vielbein variation
   G vielbein variations: 30.5 s
PASS  T_vielbein_variation_closed_form_G
PASS  T_symmetric_part_Belinfante_G
   C vielbein variations: 17.7 s
PASS  T_vielbein_variation_closed_form_C
PASS  T_symmetric_part_Belinfante_C
[371.3 s] -> Noether identities
PASS  Noether_identity_diffeomorphisms_G
PASS  Noether_identity_local_Lorentz_G
PASS  Noether_identity_diffeomorphisms_C
PASS  Noether_identity_local_Lorentz_C
PASS  conservation_on_shell_general
[633.9000000000001 s] -> EMT components
PASS  T_diagonal_components_G
PASS  EMT_trace_G
PASS  kinetic_sum_on_shell_G
PASS  T_diagonal_components_C
PASS  EMT_trace_C
PASS  kinetic_sum_on_shell_C
PASS  T_x4_x8_component_G
PASS  T_x4_x8_component_C
PASS  energy_exchange_equation
[46.800000000000004 s] -> exact solutions and conservation
PASS  solution_matrix_square
PASS  exact_solution_x4_x8_G
PASS  exact_solution_x4_x8_C
PASS  exact_solution_nonlinear_homogeneous_C
PASS  exact_solution_nonlinear_homogeneous_G
[673.1 s] -> canonical quantisation
PASS  canonical_momentum
PASS  first_order_form_and_anticommutator
PASS  Heisenberg_equation_reproduces_field_equation
PASS  no_positive_inner_product
PASS  mode_hamiltonian_good_sector
PASS  mode_hamiltonian_Krein_selfadjoint
PASS  good_sector_hermiticity_curved
PASS  Krein_form_conserved_curved
PASS  Fock_space_good_sector_example
[6.2 s] -> writing outputs
84/84 checks passed; total time 1773.4 s
```

Final verdict line: `84/84 checks passed; total time <seconds> s`. Exit code: `0`. Nothing is printed to
the error stream. The second run printed the same lines with slightly different times (for example
`[370.3 s] -> Noether identities` and `84/84 checks passed; total time 1775.1000000000001 s`).

### 4.3 Files written

The three files of section 2.3, each rewritten in full. After a correct run each is byte-identical to the
committed file: the sha256 values of section 2.3, and `git status --porcelain Revision/theory` prints
nothing. The summary lines are line 8 of `wolfram-field-theory.json`,
`  "summary": {"passed": 84, "failed": 0, "total": 84},`, and line 7 of `wolfram-scope.json`,
`  "summary": {"passed": 15, "failed": 0, "total": 15},`. `field-theory.json` has no summary line; it
begins with `{`, then a line beginning `  "description": "Exact formulas of the Revision field theory`, and
contains 32 records with the keys `christoffel_nonzero` ... `eta`.

### 4.4 Run time and memory on the verification machine

Windows 11 Pro for Workstations, Intel Core Ultra 9 275HX (24 logical processors), 191 GB RAM. During the
two verification runs the machine was heavily loaded by other jobs (CPU load 88 to 100 percent, 6 to 22
other Wolfram kernels running), and the two runs ran at the same time; on a quiet machine expect shorter
times (the document `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` records 1029 s for an earlier run of
`verify_field_theory.wls` on the development machine).

| run | script | wall time | time printed by the script | CPU time of the kernel | peak memory of the kernel (working set) |
| --- | --- | --- | --- | --- | --- |
| 1 | `verify_field_theory.wls` | 1778.0 s | 1773.4 s | about 1549 s | 578 MB |
| 2 | `verify_field_theory.wls` | 1779.8 s | 1775.1 s | about 1549 s | 578 MB |
| 1 | `verify_scope.wls` | 37.9 s | 33.5 s | about 25 s | 227 MB |
| 2 | `verify_scope.wls` | 39.9 s | 34.4 s | about 25 s | 221 MB |

Three further, timed runs of `verify_scope.wls` with the input present (section 6.4) took 24.0 to 29.1 s of
wall time, on the same loaded machine but not concurrently with each other. The `wolframscript`
process itself used 17 MB. Time per section of `verify_field_theory.wls` in run 1: about 371 s for
`energy-momentum tensor by vielbein variation`, 634 s for `Noether identities`, 47 s for `EMT components`,
673 s for `exact solutions and conservation`, 6 s for `canonical quantisation`, and less than 45 s for all
other sections together.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

* `verify_field_theory.wls` OVERWRITES `Revision/theory/reports/wolfram-field-theory.json` and
  `Revision/theory/field-theory.json`; `verify_scope.wls` OVERWRITES
  `Revision/theory/reports/wolfram-scope.json`. They are committed files. A correct run writes exactly the
  committed bytes, so Git sees no change.
* If the folder `Revision/theory/reports/` is missing, the scripts create it (tested for
  `verify_scope.wls`: with the folder deleted it was recreated and the report was byte-identical).
* A run that fails (for example with a missing input, section 3.7) still overwrites its outputs with the
  failing verdicts. An interrupted run writes nothing.
* Nothing else is created, changed or deleted in the repository: after both scripts had run in each of the
  two fresh clones, `git status --porcelain --ignored` printed nothing (no modified, untracked or ignored
  file).

### 5.2 Outside the repository

* Processes: each `wolframscript` command starts one Wolfram kernel (on Windows the process `wolfram.exe`,
  a child of `wolframscript.exe`), which ends when the script ends. It uses one kernel of your licence.
* Temporary file: while a script runs, WolframScript keeps its printed output in a temporary file
  `tmp_<10 letters and digits>` in its own folder (on Windows
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\`; on macOS and Linux the location was not
  examined). Observed on the verification machine: the file appeared 0.1 s after the start and was
  deleted when the script ended normally; after an interrupted run it stays behind (it contains the lines
  printed so far; it is harmless and can be deleted).
* Nothing was written to the system temporary folder (`%TEMP%`) by these runs: a listing before and after
  showed no new or changed entry belonging to Wolfram (the changes there belonged to other programs).
* WolframScript rewrites its own settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` when
  it starts (observed for a `wolframscript -code` call: same content, new modification time). This is
  WolframScript's normal behaviour, not specific to this set. The paclet configuration file of the Wolfram
  user folder (`%APPDATA%\Wolfram\Paclets\Configuration\`) changed once during the verification period, at
  a moment when many other Wolfram jobs were running and no kernel of this set was starting; it is not
  attributed to this set.
* Network: none. No network connection (TCP) or endpoint (UDP) owned by `wolframscript` or by the kernel
  was seen in 404 samples (about one every 4 s) from 2 minutes 21 s after the start of the field-theory
  runs to the end of the scope runs; a connection shorter than the sampling interval cannot be excluded
  by this method. The scripts contain no network function. (Activating the free Wolfram Engine needs the
  internet once; that is a property of the licence, not of these scripts.)

### 5.3 Effects on other parts of the repository

The outputs are inputs of `Revision/theory/python/check_field_theory.py` (its comparison with the Wolfram
record) and of the publication tests listed in section 1.4. A correct run leaves them byte-identical, so it
changes nothing for them. A failed run (section 5.1) would make those tests fail until the outputs are
restored.

### 5.4 How to restore the committed state

From the repository root (all systems):

```text
git checkout -- Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json Revision/theory/reports/wolfram-scope.json
git status --porcelain Revision/theory
```

The second command must then print nothing. To restore the input as well, add
`Revision/algebra/gammas.json` to the first command.

## 6. Verification record

### 6.1 What was verified, where and with what

* Date: 2026-10-02.
* Commit: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the branch `main` of
  `https://github.com/once-ere/Dirac_claude.git` at the time). The files of the set were last changed in
  commits `daeb5ba` (both scripts) and `2c61fb0` (the package), the input in `9ea68d4`, the outputs in
  `a9a1b70` (field theory) and `70fab64` (scope).
* Clones: two fresh clones made with `git clone https://github.com/once-ere/Dirac_claude.git` (runs 1 and
  2), and a third fresh clone for the experiments of section 6.4. No uncommitted file was copied into them:
  the set, its input and its outputs were committed and unchanged in the working tree.
* Environment: Windows 11 Pro for Workstations 10.0.26200; Intel Core Ultra 9 275HX, 24 logical
  processors, 191 GB RAM; WolframScript 1.14.0; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2,
  2026), Professional licence; Git 2.51.2.windows.1 with the global setting `core.autocrlf=true` (no
  effect: the repository's `.gitattributes` keeps every file byte for byte; all files of the set have LF
  line endings); PowerShell 7.6.6.
* Commands: in each clone, from the repository root, `wolframscript -file
  Revision/theory/wolfram/verify_field_theory.wls` and then `wolframscript -file
  Revision/theory/wolfram/verify_scope.wls`, started from PowerShell (`Start-Process` with the clone as
  working folder, recording wall time, exit code and the peak working set of the child processes; separate
  samplers recorded the kernels' CPU time and their network endpoints). Runs 1 and 2 ran at the same time,
  on a machine loaded by other jobs (section 4.4).

### 6.2 Results

| run | script | exit code | final line | checks |
| --- | --- | --- | --- | --- |
| 1 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 1773.4 s` | 84 PASS, 0 FAIL |
| 2 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 1775.1000000000001 s` | 84 PASS, 0 FAIL |
| 1 | `verify_scope.wls` | 0 | `15/15 checks passed; time 33.5 s` | 15 PASS, 0 FAIL |
| 2 | `verify_scope.wls` | 0 | `15/15 checks passed; time 34.4 s` | 15 PASS, 0 FAIL |

The printed lines of the two runs are identical apart from the time values. Nothing was printed to the
error stream.

### 6.3 Byte identity of the outputs

| output | committed sha256 | run 1 | run 2 |
| --- | --- | --- | --- |
| `Revision/theory/reports/wolfram-field-theory.json` | `eed5e0fb01b281d58ccabe7dd84bde3b81574ae09a9c4b05e67f22f6a8065a7e` | identical | identical |
| `Revision/theory/field-theory.json` | `2a3c83e5db5e0ad3572791334a4797b8af549a22295bb6800739340f2c107f54` | identical | identical |
| `Revision/theory/reports/wolfram-scope.json` | `8a0bee2e9c0b536ed25c6dcb31272e6e0d7a49ae9e1f69a755899ce6efa021ce` | identical | identical |

Each output was compared byte for byte (`cmp`) with the committed blob (`git show HEAD:<file>`) and between
the two runs: all identical. `git status --porcelain --ignored` printed nothing in either clone after the
field-theory script and again after the scope script.

### 6.4 Further experiments (third fresh clone, same commit)

* `verify_scope.wls` started from the folder `Revision/theory/wolfram` as `wolframscript -file
  verify_scope.wls`: 15/15, exit code 0, output byte-identical (the scripts locate their files relative to
  themselves). WolframScript's temporary file was created at the start and deleted at the end (section
  5.2).
* The folder `Revision/theory/reports` deleted, then `verify_scope.wls` run from the root: the folder was
  recreated, 15/15, exit code 0, `wolfram-scope.json` byte-identical; restored with `git checkout`.
* `Revision/algebra/gammas.json` hidden: `verify_scope.wls` printed `Import::nffil` and ended with
  `4/15 checks passed`, exit code 1, and overwrote `wolfram-scope.json`; `verify_field_theory.wls`
  printed the same message and `FAIL  fixture_Clifford_relation` and was stopped after 60 s without
  writing any output. Everything was restored with `git checkout` and `git status --porcelain --ignored`
  printed nothing.
* The POSIX-shell forms of the commands of sections 3.5 and 3.6 were tested in Git Bash on the
  verification machine (`time wolframscript -file Revision/theory/wolfram/verify_scope.wls`, a run followed
  by `echo` of `$?`, `sha256sum`, `grep '"summary"'`, `git status --porcelain Revision/theory`): 15/15,
  exit code 0, the hashes and summary lines of sections 2.3 and 4.3, empty status. They were not executed
  on macOS or Linux themselves. The PowerShell forms were tested in PowerShell 7.6.6.
* `wolframscript -file Revision/theory/wolfram/verify_scope.wls` from a folder that is not the repository
  root printed `Failed to open file at path: Revision/theory/wolfram/verify_scope.wls` with exit code 0
  (section 3.7).

### 6.5 Interrupted runs

A first pair of runs of `verify_field_theory.wls` was stopped after less than 3 minutes (it had been
started under a tool time limit shorter than the run time) and restarted as runs 1 and 2 in the same
clones, which were still unmodified (`git status --porcelain --ignored` printed nothing before the restart). Those interrupted runs and the interrupted missing-input run of section 6.4 wrote no
output file; each left one WolframScript temporary file (section 5.2), which was deleted afterwards.

### 6.6 Fixes and open discrepancies

* Fixes: none. No execution defect was found; no file of the set was changed.
* Open discrepancies: none. Every check passes and every output reproduces byte for byte.
* Observations recorded for students (not defects of this set): WolframScript returns exit code 0 when it
  cannot open the script file; WolframScript occasionally printed `The product exited because an error
  occurred ...` with exit code 1 after a correct result while the machine was heavily loaded (section
  3.7); the run time of `verify_field_theory.wls` under that load was about 1778 s, against 1029 s
  recorded earlier on the development machine.
