# Provenance of the wolframscript set `Revision/kohn_sham/theory/` (the exact Kohn-Sham theory of dirac16complex)

This file tells a student who has never used Wolfram or Python what this set of scripts is, how to run
it from nothing, what it prints and writes, what it changes on the computer, and how it was verified on
2026-10-02. Every number below was measured on the verification machine or read from the files
themselves; nothing is copied from another document.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

`Revision/kohn_sham/theory/verify_ks_theory.wls` (with its package `KohnShamTheory.wl`) derives, with
exact computer algebra in the Wolfram Language, the Kohn-Sham equations of the author's 16-component
field dirac16complex in the author's primordial 8-dimensional field, checks 46 statements about them,
and writes the result twice: as a check report (`Revision/kohn_sham/reports/ks-theory-wolfram.json`) and
as the recipe of formulas that the numerical Kohn-Sham solvers read (`Revision/kohn_sham/ks-theory.json`).
The same folder holds an independent second engine, the Python/sympy program `check_ks_theory.py`
(57 checks, report `Revision/kohn_sham/reports/ks-theory-python.json`); it is documented here as an
optional companion (sections 3.6 and 4.5), because it reads the Wolfram output.

### 1.2 The physics, in plain words

* The field. The author's field Psi has 16 complex components and lives in 8 dimensions, named as the
  author names them: x1, x2, x3 are ordinary space; x4 is time; x5, x6, x7 are three extra time-like
  directions whose scale factor shrinks exponentially (they "deflate" while space inflates); x8 is a
  hidden direction. The 16 x 16 gamma matrices that define the field equation are read from the file
  `Revision/algebra/gammas.json` (made by another set, `Revision/algebra/wolfram/`).
* Kohn-Sham theory. A gas of many interacting particles is hard to solve. The Kohn-Sham method (the
  method behind "DFT", density functional theory, in chemistry and solid-state physics) replaces it by
  independent particles that move in an effective field, the mean field, which is itself computed from
  the particle densities; the two are made consistent by iteration ("self-consistent field"). This set
  does not solve the equations numerically. It derives, exactly, the equations that the numerical
  solvers (the Rust solver in `Revision/kohn_sham/solver/` and the Python reference in
  `Revision/kohn_sham/reference/`) then solve.
* What is derived and checked, in the order of the script (the check names are those printed on the
  screen):
  * A. The gamma matrices (3 checks: `fixture_input`, `clifford_relation`, `C_B_Gamma`). The matrices
    are read, the defining Clifford relation {gamma^a, gamma^b} = 2 eta^ab with the signature
    (+,+,+,-,-,-,-,+) is verified for all 64 pairs, and the three special matrices C (scalar density),
    B (number density) and Gamma (the chirality, the product of all eight gammas) are checked.
  * B. The geometry (6 checks). The hidden coordinate is replaced by the proper distance
    y = ln(sin 6 H x8)/(6 H) <= 0; the volume factor sqrt|g| is checked; the spin connection (how a
    spinor is carried along in the curved field) is computed from the metric and verified for all 64
    index pairs; the key result is that gamma^mu Omega_mu = 3 H gamma^(x8) exactly, for any time
    dependence a4(x4) of the scale factors, because the contributions of the 3 inflating and the
    3 deflating directions cancel.
  * C. The ansatz (3 checks). Writing Psi = e^{i k.x} W^{-3} chi(y, x4) with the warp W = e^{H y} removes
    the spin connection exactly and leaves a Schroedinger-like equation i d chi/dx4 = h chi with a
    Hermitian Hamiltonian h; without the factor W^{-3} a term survives.
  * D. The blocks (9 checks). Three commuting matrices J, K1, K2 split the 16 components into eight
    independent 2 x 2 blocks; an exact unitary basis V is constructed (entries 0, +-1, +-i divided by
    2 sqrt 2) and the Hamiltonian in every block is h_j = j[-i sigma1 d/dy + M sigma2 + kappa k sigma3] + v,
    j = +-1; the chirality Gamma maps a block of type j with mass M onto a block of type -j with mass -M;
    the spectra depend only on |k|.
  * E. The exchange (7 checks). For the interaction U = (lambda/2) S^2 the Hartree-Fock energy of a
    uniform gas is computed exactly (including an explicit integral over all directions of the
    momentum): e_x = -(lambda/32)(n^2 + S^2); this gives the Kohn-Sham potentials
    M_eff = m + (15/16) lambda S and v_v = -lambda n/16. The exact Fock exchange of a slab is computed by
    averaging over the 48-element spinor octahedral group.
  * F. The boundary conditions (8 checks). At the brane y = 0 a Z2 mirror construction is ASSUMED (the
    script labels it so): even parity chi2(0) = 0 or odd parity chi1(0) = 0; at the tip y = -L a family of
    conditions is allowed; the block Hamiltonian is shown to be self-adjoint with these ends; the exact
    k = 0 spectra are verified by substituting the closed-form eigenfunctions into the block equation
    (DSolve is called only to confirm that the system has one general solution).
  * G. The rescaling identity (1 check). The slice value a4,0 enters only through kappa k, so a slice at
    a4,0 is exactly a slice at 0 with rescaled momentum lattice and box.
  * H. The energy-momentum tensor and adiabaticity (8 checks). The energy-momentum tensor of one orbital
    is computed component by component; its trace identity, its conservation along y, and the law of
    energy change along x4 (nabla_mu T^mu_x4 = -d rho/dx4 - 3 a4'(p3 - p_t), checked for a general
    diagonal T; it is a law of change, not a conservation law) are verified; the adiabatic
    (slow-change) measure is checked on an explicit example; the slope of the brane band d eps/dk at
    k = 0 is given by an exact formula and confirmed by a numerical shooting computation (NDSolve at
    25 digits, Richardson extrapolation), which agrees with the formula to better than 1e-8.
  * Export (1 check: `ks_theory_json_written`). `ks-theory.json` is written, exported twice to make sure
    the text is identical, read back, and its key entries compared with what was computed. It records,
    among others, that the history a4 = A H x4 is a PRESCRIBED BACKGROUND (a test field without
    back-reaction), not a solution of the coupled field equations.

### 1.3 How the script proves it

Each statement is decided by exact computation with Wolfram Language expressions (matrices, derivatives,
integrals): `Simplify` must reduce a difference to exactly 0, two exact matrices must be equal, or an
exact count must come out right (for example the 48 elements of the octahedral group). Only the
brane-band slope uses floating-point numbers (25-digit working precision, tolerance 1e-8). Every
check prints `PASS` or `FAIL` with its name; the report lists every check with its verdict and a detail
text; the exit code is 0 only if all 46 pass and both output files were written. A missing input file
or an output file that cannot be written stops the run at once with a line beginning `ERROR` and exit
code 1 (this guard is the execution fix of 2026-10-02, section 6). The companion `check_ks_theory.py`
repeats the derivation independently with sympy (it shares no code with the Wolfram script) and in
addition compares its own results with `ks-theory.json`.

### 1.4 Which documents cite its results

* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): section 8 (Theorem T3 is proved for
  the Kohn-Sham problem of `Revision/kohn_sham/ks-theory.json`), section 9.1 (the table of report counts:
  `ks-theory-wolfram.json` 46 of 46, `ks-theory-python.json` 57 of 57), section 10 (the reproduction
  commands `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls` and
  `python Revision/kohn_sham/theory/check_ks_theory.py`).
* `Revision/tests/test_pair_creation_proofs_publication.py` reads both reports for the count table.
* The numerical Kohn-Sham programs that read `ks-theory.json`: the Rust solver
  (`Revision/kohn_sham/solver/src/theory.rs`, described in `Revision/kohn_sham/solver/README.md`; it refuses
  a `ks-theory.json` without the PRESCRIBED BACKGROUND label), the Python reference
  (`Revision/kohn_sham/reference/ks_fd.py`, `run_reference.py`, `README.md`) and the cross-check
  `Revision/kohn_sham/checker/crosscheck_ks.py`. The sha256 of `ks-theory.json`
  (`1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3`) is pinned in
  `Revision/kohn_sham/results/parameters.json` and `Revision/kohn_sham/reference/results/parameters.json`,
  and its first 16 hex digits are quoted in `Revision/kohn_sham/reports/ks-crosscheck.json`,
  `ks-reference.json` and `ks-rust-solver.json`.
* The T3 verifiers `Revision/pairing/kohn_sham/wolfram/verify_t3.wls` and
  `Revision/pairing/kohn_sham/python/check_t3.py` (with `Revision/pairing/kohn_sham/README.md`) read
  `ks-theory.json`.
* `Revision/field_equations_a4/python/check_ks_source_conditions.py` cites `ks-theory.json`
  (`adiabaticity.history`, `emt.energyChange`).
* `Revision/textbook/TEXTBOOK_SPEC.md` (chapter 14) lists `Revision/kohn_sham/theory`, `ks-theory.json` and
  the reports as sources.

## 2. Files

All files are stored byte for byte (the repository's `.gitattributes` sets `* -text`, so Git never changes
their line endings). Line counts are counts of line-feed characters (`wc -l`).

### 2.1 The script and the package

| File | sha256 | Lines | Bytes |
| --- | --- | --- | --- |
| `Revision/kohn_sham/theory/verify_ks_theory.wls` (the script you run) | `4ce71aaa2c8efd78c8e1508ab72a3223383e21900805c4a34e55a3d5f7deb50d` | 463 | 41295 |
| `Revision/kohn_sham/theory/KohnShamTheory.wl` (its package, loaded by the script with `Get`) | `554d726af9cff43c680ee9a4a70e7ffa28740a306c91581b6944cc668007f3cf` | 87 | 4575 |
| `Revision/kohn_sham/theory/check_ks_theory.py` (optional companion, Python/sympy) | `28c24832e73dbfc1fb133cabf477d3b6eb59e257e1042030dbbb3c3672e56b80` | 791 | 47119 |

The script's sha256 is that of the version with the execution fix of 2026-10-02 (section 6). The
commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` holds the earlier version (sha256
`d8df4e07976352d07c41c4b38a28ca09626f20d54a237cfba7ba942893596cab`, 455 lines, 40693 bytes). Both
versions perform the same 46 checks and write the same bytes; the earlier one does not stop when an
input file is missing or an output file cannot be written (section 3.7 describes what it does then).

### 2.2 Inputs (read only, never modified)

| Input | Read by | sha256 | Lines | Bytes |
| --- | --- | --- | --- | --- |
| `Revision/algebra/gammas.json` (the 8 gamma matrices and eta) | both | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 |
| `Revision/algebra/reports/python-gammas.json` (the same matrices rebuilt in Python) | companion only | `b6241910ade6cc282e0aaab75d90fc697247a0d68504618787f547447e2e458b` | 11639 | 94180 |
| `Revision/kohn_sham/ks-theory.json` (the Wolfram output) | the Wolfram script reads back what it has just written; the companion cross-checks it | see 2.3 | | |

The script finds the package and the inputs relative to its own location (`$InputFileName`), not relative
to the current folder. Before it reads the package and before it reads `gammas.json` it checks that the
file exists; if not, it prints `ERROR  input file not found: <full path>` and stops with exit code 1.

### 2.3 Outputs (rewritten on every run; UTF-8, LF line endings, no time stamps)

| Output | Written by | sha256 (committed and reproduced) | Lines | Bytes |
| --- | --- | --- | --- | --- |
| `Revision/kohn_sham/ks-theory.json` (the formulas for the solvers) | `verify_ks_theory.wls` | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` | 477 | 17278 |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` (46 checks) | `verify_ks_theory.wls` | `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6` | 56 | 10291 |
| `Revision/kohn_sham/reports/ks-theory-python.json` (57 checks) | `check_ks_theory.py` | `0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c` | 298 | 18572 |

If the folder `Revision/kohn_sham/reports` is missing, both scripts create it. If an output file cannot
be opened for writing (for example because it is read-only), the Wolfram script prints the Wolfram
message `OpenWrite::noopen: Cannot open <full path>.` and the line `ERROR  cannot write <full path>`, and
stops with exit code 1.

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, and an internet connection for the installation
  and the download (the script itself needs no network).
* About 600 MB of free disk space for the repository (a fresh clone measured 519 MB, of which 128 MB is
  the Git history) plus the space the Wolfram installer asks for.
* About 0.5 GB of free memory (the Wolfram kernel of this script peaked at 239 MB; the optional Python
  companion at 88 MB).
* A Wolfram kernel with WolframScript: either the free Wolfram Engine for Developers or a licensed
  Mathematica / Wolfram desktop installation. The verification used Wolfram 15.0.1 with WolframScript
  1.14.0; older versions were not tested.
* Git, to download the repository.
* Only for the optional companion (section 3.6): Python 3 with numpy, sympy and mpmath. Jupyter and Rust
  are NOT needed for this set.

### 3.2 Open a terminal

* Windows: press the Windows key, type `PowerShell`, and open "Windows PowerShell" or "PowerShell 7".
  All Windows commands below are typed there.
* macOS: open Finder, then Applications, Utilities, Terminal.
* Linux: open your distribution's Terminal application (often Ctrl+Alt+T).

Type each command exactly as shown and press Enter after each line.

### 3.3 Install Wolfram and WolframScript

Choose ONE option.

Option A, the free Wolfram Engine for Developers:

1. In a web browser open `https://www.wolfram.com/engine/`, follow its download link, and follow the
   page to obtain the free licence. You need a Wolfram ID (an account at `https://account.wolfram.com`);
   read the licence terms yourself before you accept them.
2. Download the installer for your operating system and run it:
   * Windows: double-click the downloaded `.exe` and accept the defaults. WolframScript normally comes
     with it, in `C:\Program Files\Wolfram Research\WolframScript\` (the folder used on the verification
     machine); if the test below says "not recognized", use option C.
   * macOS: open the downloaded `.dmg` and follow its instructions (drag the application to
     Applications and install WolframScript if the disk image offers it).
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

Test the installation (all systems):

```text
wolframscript -version
wolframscript -code "1+1"
```

The first prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`; the second prints
`2`. If the second asks for activation, do step 4 of option A. To see which kernel version will run,
type (in all shells, with SINGLE quotes)

```text
wolframscript -code '$Version'
```

which prints, on the verification machine, `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. With
double quotes the shell replaces `$Version` by an empty text before WolframScript sees it. In
PowerShell 7 and in bash (and zsh) WolframScript then prints the kernel banner and opens an interactive
`In[1]:=` prompt instead (observed in PowerShell 7.6.6 and Git Bash); leave such a prompt by typing
`Quit[]` and pressing Enter. In Windows PowerShell 5.1 the same mistake prints
`Error: -code called with no argument.` and `Example format is 'wolframscript -code code'` instead
(observed in Windows PowerShell 5.1.26100); use single quotes.

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

The download took about 13 seconds on the verification machine. You are now in the repository root: the
folder that contains the folder `Revision`. Every command below is run from here. Do not open and save
the JSON files of section 2 with an editor: an editor may change their line endings, and then they are
no longer byte-identical to the committed files.

### 3.5 Run the script

Windows PowerShell (forward slashes and backslashes both work):

```powershell
wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
$LASTEXITCODE
```

macOS and Linux:

```bash
wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
echo "exit code: $?"
```

The second line shows the exit code of the run; type it immediately after the first, because it reports
the most recent command. The run takes about 40 seconds; the lines appear while it runs. Optional, to
measure the run time: in PowerShell
`Measure-Command { wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls | Out-Default }`
(the output is shown, then `TotalSeconds`), on macOS and Linux
`time wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`.

Then check the result:

1. The last printed line must begin with `46/46 checks passed`, the exit code must be `0`, and exactly
   47 lines must have been printed (46 lines beginning with `PASS` and the final line), none containing
   `::`. A line containing `::` is a Wolfram message (for example `OpenWrite::noopen`) and means that
   something went wrong even if the other checks below look right.
2. The report's summary line. Windows PowerShell:

   ```powershell
   Select-String -Pattern '"summary"' -Path Revision/kohn_sham/reports/ks-theory-wolfram.json
   ```

   prints `Revision\kohn_sham\reports\ks-theory-wolfram.json:7:  "summary": {"passed": 46, "failed": 0, "total": 46},`.
   macOS and Linux:

   ```bash
   grep '"summary"' Revision/kohn_sham/reports/ks-theory-wolfram.json
   ```

   prints `  "summary": {"passed": 46, "failed": 0, "total": 46},`.
3. The two outputs are byte-identical to the committed files. Windows PowerShell:

   ```powershell
   Get-FileHash Revision/kohn_sham/ks-theory.json, Revision/kohn_sham/reports/ks-theory-wolfram.json
   git status --porcelain
   ```

   macOS: `shasum -a 256 Revision/kohn_sham/ks-theory.json Revision/kohn_sham/reports/ks-theory-wolfram.json`,
   Linux: `sha256sum Revision/kohn_sham/ks-theory.json Revision/kohn_sham/reports/ks-theory-wolfram.json`,
   and on both `git status --porcelain`. The hashes must be (PowerShell prints them in capital letters)
   `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` for `ks-theory.json` and
   `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6` for `ks-theory-wolfram.json`, and
   `git status --porcelain` must print nothing at all (an empty answer means that no file of the
   repository differs from the committed version).

### 3.6 Optional: the companion Python checker

The companion repeats the derivation independently with sympy and cross-checks `ks-theory.json`. Run
the Wolfram script first (section 3.5); in a fresh clone the committed `ks-theory.json` is present
anyway, so the result is the same in either order.

1. Install Python 3 if `python --version` (Windows) or `python3 --version` (macOS, Linux) does not print
   a version: Windows, the installer from `https://www.python.org/downloads/` (tick "Add python.exe to
   PATH"; if `python` opens the Microsoft Store instead, use that installer); macOS, the installer from
   the same page or `brew install python`; Linux, the distribution's package (`sudo apt install python3
   python3-venv` on Debian and Ubuntu). The verification used Python 3.14.5.
2. Make a private environment NEXT TO the repository (not inside it, so that `git status` stays empty),
   install the exact package versions of the verification, and run the checker. Windows PowerShell,
   from the repository root:

   ```powershell
   python -m venv ..\ks-venv
   ..\ks-venv\Scripts\python.exe -m pip install numpy==2.4.6 sympy==1.14.0 mpmath==1.3.0
   ..\ks-venv\Scripts\python.exe Revision/kohn_sham/theory/check_ks_theory.py
   $LASTEXITCODE
   ```

   macOS and Linux, from the repository root:

   ```bash
   python3 -m venv ../ks-venv
   ../ks-venv/bin/python -m pip install numpy==2.4.6 sympy==1.14.0 mpmath==1.3.0
   ../ks-venv/bin/python Revision/kohn_sham/theory/check_ks_theory.py
   echo "exit code: $?"
   ```

   (Calling the environment's own `python` directly needs no "activation" step.) What you see: the
   `venv` line prints nothing (it took 6 to 16 s on the verification machine). A new environment
   contains only pip, so the `pip install` line downloads three package files of about 19 MB together
   (numpy 12.5 MB, sympy 6.3 MB, mpmath 0.5 MB) from the Python Package Index, or takes them from pip's
   local cache if this computer downloaded them before (then the lines say `Using cached ...`). It prints
   `Collecting ...` lines, `Installing collected packages: mpmath, sympy, numpy`, and must end with the
   line `Successfully installed mpmath-1.3.0 numpy-2.4.6 sympy-1.14.0`; it took 34 to 40 s on the
   verification machine (from the cache). Two kinds of extra lines are harmless and can be ignored: a
   notice `[notice] A new release of pip is available: ...` with a suggested upgrade command (you need not
   upgrade pip), and on some computers `WARNING: Cache entry deserialization failed, entry ignored` (pip
   ignores that cache entry and continues). If your Python is older than 3.14 and pip cannot find these exact
   versions, `pip install numpy sympy mpmath` installs versions for your Python; the verdicts are
   expected to be the same, but only the versions above were verified.
3. Check: the last line must be `{"passed": 57, "failed": 0, "other": 0, "total": 57}`, the exit code
   `0`, and the report `Revision/kohn_sham/reports/ks-theory-python.json` must have the sha256
   `0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c` (same hash commands as in
   section 3.5, step 3); `git status --porcelain` must again print nothing.

### 3.7 What to do if it fails

* `wolframscript : The term 'wolframscript' is not recognized ...` (PowerShell) or
  `wolframscript: command not found` (macOS, Linux): WolframScript is not installed or not on the PATH.
  Install it (section 3.3, option C) and open a NEW terminal. On Windows you can also run it by its full
  path: `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file Revision/kohn_sham/theory/verify_ks_theory.wls`.
* A request to activate, or a message that the kernel is not activated or the licence is invalid: run
  `wolframscript -activate` (section 3.3, option A, step 4).
* WolframScript cannot find a kernel: `wolframscript -configure` prints its settings file (normally
  WolframScript finds the newest installed kernel by itself, and the line `WOLFRAMSCRIPT_KERNELPATH` is
  commented out with `//`). Point it to the kernel program of your installation with
  `wolframscript -configure WOLFRAMSCRIPT_KERNELPATH=<full path of the kernel program>` (on the
  verification machine the kernel program is `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`;
  older versions call it `WolframKernel.exe` on Windows and `WolframKernel` on macOS and Linux), or
  reinstall the Wolfram Engine or Mathematica.
* The only output is `Failed to open file at path: Revision/kohn_sham/theory/verify_ks_theory.wls`: you
  are not in the repository root. CAUTION: in this case WolframScript still returns exit code 0
  (observed during the verification), so always read the last line. Go to the folder that contains
  `Revision` (`cd $HOME\Dirac_claude` in PowerShell, `cd ~/Dirac_claude` on macOS and Linux) and run
  again.
* The only output is the line
  `ERROR  input file not found: ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json` (the dots stand
  for the full path of your repository folder; on macOS and Linux the path has forward slashes), and the
  exit code is `1` (observed: after about 3 seconds): the input file `Revision/algebra/gammas.json` is
  missing or renamed. Restore it with `git checkout -- Revision/algebra/gammas.json` and run again. If the
  line names `...\Revision\kohn_sham\theory\KohnShamTheory.wl` instead, the package is missing: restore
  it with `git checkout -- Revision/kohn_sham/theory/KohnShamTheory.wl`.
  The older script of commit `c2b33cc` (section 2.1) does not stop in this case. Its output (observed)
  begins with an empty line, then
  `Import::nffil: File ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json not found during Import.`,
  then further Wolfram messages, each after an empty line (`Diagonal::list`, `Set::shape`,
  `FileHash::noopen`, `StringJoin::string`, three times `Part::partw`, `General::stop`); NO
  `fixture_input` line is printed; then come `FAIL  clifford_relation`, `FAIL  C_B_Gamma`,
  `PASS  geometry_hidden_coordinate`, `PASS  geometry_sqrt_det`, and the run never ends (observed: still
  running after 167 and after 400 seconds). Press Ctrl+C to stop it, then restore the file as above.
* The output contains `OpenWrite::noopen: Cannot open ...\ks-theory-wolfram.json.` (or
  `...\ks-theory.json.`), followed by `ERROR  cannot write ...` with the same path, there is no
  `checks passed` line, and the exit code is `1` (observed): an output file of section 2.3 is read-only, or
  the folder is not writable. The file is left unchanged. Make the file writable again (Windows
  PowerShell: `Set-ItemProperty <file> -Name IsReadOnly -Value $false`, tested in PowerShell 7 and
  Windows PowerShell 5.1; macOS and Linux: `chmod u+w <file>`), or use a clone in a folder where you may
  write, and run again. A missing folder
  `Revision/kohn_sham/reports` is not an error: the script creates it (observed).
  The older script of commit `c2b33cc` (section 2.1) does NOT report this as a failure. With the report
  file read-only, and also with the folder `Revision/kohn_sham/reports` missing, it printed (observed)
  after `PASS  ks_theory_json_written` three Wolfram messages, each after an empty line:
  `OpenWrite::noopen: Cannot open ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json.`,
  `BinaryWrite::stream: $Failed is not a string, SocketObject, InputStream[ ] or OutputStream[ ].` and
  `Close::stream: $Failed is not a string, SocketObject, InputStream[ ] or OutputStream[ ].`; then the
  final line still read `46/46 checks passed` and the exit code was `0`, although the report was not
  written. With a read-only report even the hash and `git status` checks of section 3.5, step 3, pass
  (the old file stays in place). Only the `::` lines show the failure: this is why section 3.5, step 1,
  asks for exactly 47 lines and no `::`.
* One or more lines begin with `FAIL`, the last line reads `k/46 checks passed` with k smaller than 46,
  and the exit code is `1`: a check did not hold on your computer. Do not edit the files. Check that the
  sha256 values of the script, the package and `gammas.json` equal those of section 2 (if they differ,
  this record does not apply to your copy), note your Wolfram version (`wolframscript -code '$Version'`,
  single quotes), and report the failing check names.
* All 46 checks pass but `git status --porcelain` lists `Revision/kohn_sham/reports/ks-theory-wolfram.json`:
  on another operating system or Wolfram version some detail texts can differ in the last digits (the
  12-digit NDSolve slopes of `brane_band_slope`) or in how an expression is printed (the coefficients of
  `spin_connection_time_terms_cancel`). This was not observed on the verification machine and was not
  tested elsewhere; the verdicts and the summary are what matter. Inspect the difference with
  `git diff Revision/kohn_sham/reports/ks-theory-wolfram.json` and restore with the command of section 5.4.
* Python companion: `ModuleNotFoundError: No module named 'sympy'` (or `numpy`) means the packages are
  not installed in the Python you ran; repeat the `pip install` line of section 3.6 with the same
  `python` you use to run the checker.

## 4. Expected output

### 4.1 Printed on the screen

The Wolfram script prints exactly 47 lines and nothing else (no warnings, no messages): one line per
check, in this order, of the form `PASS  <name>  t=<seconds>` (two spaces before and after the name),
then the final line. The seconds count from the start of the checks and vary from run to run; they can
show binary rounding such as `t=0.7000000000000001` or `t=26.700000000000003`, which is normal. On
Windows each line ends with a carriage return and a line feed; this is also normal.

```text
PASS  fixture_input  t=0.6000000000000001
PASS  clifford_relation  t=0.6000000000000001
PASS  C_B_Gamma  t=0.6000000000000001
PASS  geometry_hidden_coordinate  t=0.7000000000000001
PASS  geometry_sqrt_det  t=0.7000000000000001
PASS  spin_connection_compatibility  t=0.9
PASS  spin_connection_slash_3H  t=0.9
PASS  spin_connection_time_terms_cancel  t=0.9
PASS  spin_connection_slash_3H_x8_chart  t=1.3
PASS  ansatz_removes_spin_connection  t=1.3
PASS  ansatz_without_W3_term_survives  t=1.4000000000000001
PASS  hamiltonian_16_hermitian  t=1.4000000000000001
PASS  blocks_commuting_set  t=1.4000000000000001
PASS  blocks_basis_unitary  t=1.4000000000000001
PASS  blocks_forms  t=1.5
PASS  blocks_relation_to_Gamma  t=1.5
PASS  block_hamiltonian  t=1.5
PASS  block_ode_equivalent  t=1.5
PASS  block_type_relation  t=1.5
PASS  block_Gamma_map  t=1.5
PASS  rotation_invariance  t=1.5
PASS  gas_mode_projector  t=1.5
PASS  gas_angular_average  t=24.5
PASS  gas_densities  t=24.5
PASS  exchange_uniform_gas  t=24.5
PASS  ks_potentials  t=24.5
PASS  ks_onshell_lagrangian  t=24.5
PASS  exchange_slab_exact_fock  t=25.1
PASS  bc_mirror_map_PA  t=25.1
PASS  bc_mirror_parities_of_densities  t=25.1
PASS  bc_brane_parity_conditions  t=25.1
PASS  bc_self_adjoint_boundary_term  t=25.1
PASS  bc_tip_family  t=25.1
PASS  bc_current_conserved_along_y  t=25.1
PASS  bc_exact_k0_spectra  t=25.1
PASS  bc_tip_asymptotics  t=25.1
PASS  rescaling_identity  t=25.1
PASS  emt_orbital_components  t=31.8
PASS  emt_trace_identity  t=31.8
PASS  emt_y_conservation_orbital  t=31.8
PASS  emt_y_conservation_selfconsistent  t=31.8
PASS  emt_x4_component  t=31.8
PASS  adiabatic_hellmann_feynman  t=31.8
PASS  adiabatic_offdiagonal_identity  t=31.8
PASS  brane_band_slope  t=33.6
PASS  ks_theory_json_written  t=33.6
46/46 checks passed; time 33.6 s
```

(This is recorded run 1 of the verification, section 6.) The longest single step is the explicit
angular integral of `gas_angular_average` (23 to 25 s), then the energy-momentum components of
`emt_orbital_components` (7 to 8 s) and the NDSolve shooting of `brane_band_slope` (about 2 s).

### 4.2 Exit code

`0` when all 46 checks pass and both output files were written; `1` when at least one check fails, when
an input file is missing, or when an output file cannot be written (in the last two cases a line
beginning `ERROR` is printed and the final `checks passed` line is missing; section 3.7). Caution: an
exit code `0` alone does not prove success. WolframScript also returns `0` when it cannot open the script
file at all (section 3.7), and the older script of commit `c2b33cc` (section 2.1) returned `0`, with the
final line `46/46 checks passed`, even when it could not write its outputs. So always also check that
exactly 47 lines were printed and that none contains `::` (section 3.5, step 1).

### 4.3 Files written

| File | How to check it |
| --- | --- |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | line 7 is `  "summary": {"passed": 46, "failed": 0, "total": 46},`; 46 entries under `"checks"`, each `"verdict": "PASS"`; sha256 `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6` |
| `Revision/kohn_sham/ks-theory.json` | 18 top-level keys from `"description"` to `"solverChecklist"`; `checksNumeric.braneBandSlope_M1_H1_L3_a0` is `"1.9051482536448664"`; `adiabaticity.historyStatus` begins with `PRESCRIBED BACKGROUND`; sha256 `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` |

The detail of `brane_band_slope` in the report reads, on the verification machine,
`... c = 2/(1+E^-3) = 1.905148253644866; NDSolve shooting (WorkingPrecision 25, k = +-1e-3, +-2e-3, Richardson): 1.90514825252 (a4,0 = 0), 1.15553082704 (a4,0 = 1/2; exact 1.15553082713)`.

### 4.4 Run time and memory on the verification machine

Verification machine: 24 cores (Intel Core Ultra 9 275HX), 191 GB memory, Windows 11 Pro for
Workstations. Other jobs were running Wolfram kernels on the same machine at the same time (5, 8 and 9
of them at the three moments checked), so a quiet computer may be faster. The script starts no parallel
kernels.

* Wall-clock time of the whole command: 36.6 to 46.6 s over 14 timed complete runs, of which 9 with the
  script of commit `c2b33cc` and 5 with the fixed script (37.0 to 39.1 s; 37.2 s and 39.1 s for the two
  recorded runs of section 6); the script's own final `time` value: 33.1 to 42.9 s over 17 runs (fixed
  script: 33.6 to 35.2 s over 5 runs).
* Peak memory (working set): the Wolfram kernel `wolfram.exe` 232 to 239 MB; `wolframscript.exe` 17 MB.

### 4.5 The optional Python companion

It prints 59 lines: 57 lines `[PASS] <name>  t=<seconds>s`, the line `shooting time <seconds> s` (right
after `[PASS] brane_band_slope`), and the final line

```text
{"passed": 57, "failed": 0, "other": 0, "total": 57}
```

The first three lines are `[PASS] fixture_input  t=0.0s`, `[PASS] fixture_python_equals_wolfram  t=0.0s`,
`[PASS] clifford_relation  t=0.0s`; the last three checks are `ks_theory_json_basis`,
`ks_theory_json_exchange`, `ks_theory_json_slope` (the cross-check of `ks-theory.json`). Exit code `0`
(`1` if a check fails). It writes `Revision/kohn_sham/reports/ks-theory-python.json` (298 lines, 18572
bytes, sha256 `0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c`), whose `"summary"`
block (lines 5 to 10) holds `"passed": 57`, `"failed": 0`, `"other": 0`, `"total": 57`. Run time 73.3 to
90.4 s wall clock over 4 timed runs (the script's own last time stamp 65.3 to 88.4 s over 5 runs; the
RK4 shooting, printed as `shooting time`, 28.5 to 39.7 s of it); peak memory 88 MB.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

* The Wolfram script OVERWRITES two committed files on every run: `Revision/kohn_sham/ks-theory.json` and
  `Revision/kohn_sham/reports/ks-theory-wolfram.json` (their modification time changes; on the
  verification machine their bytes stayed identical to the committed ones). If the folder
  `Revision/kohn_sham/reports` is missing, the Wolfram script creates it (observed; the script of commit
  `c2b33cc` did not).
* The companion OVERWRITES `Revision/kohn_sham/reports/ks-theory-python.json` (it would create the folder
  `Revision/kohn_sham/reports` if it were missing).
* Nothing else in the repository is created or changed: `git status --porcelain --untracked-files=all --ignored`
  printed nothing after the recorded runs of both scripts and at the end of all runs in both clones of
  the first pass (no new file, no ignored file, no `__pycache__` folder); in the clones of the second
  pass it printed only the line ` M Revision/kohn_sham/theory/verify_ks_theory.wls`, the fixed script
  that had been copied in (section 6).

### 5.2 Outside the repository

* WolframScript keeps the printed output in a temporary file
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\tmp_<10 random letters and digits>`
  (Windows; about 2 kB) and deletes it when the run ends normally (observed). If the run is interrupted
  (Ctrl+C, or a killed process) the file stays behind (observed: 1217 bytes, exactly the text printed
  until then) and may be deleted by hand. Where WolframScript keeps this file on macOS and Linux was not
  examined.
* WolframScript has its own settings file, on Windows `%APPDATA%\Wolfram\WolframScript\WolframScript.conf`;
  its content (sha256) was the same before and after a monitored run.
* Nothing is written to the system temporary folder: with `TEMP` and `TMP` pointed to an empty private
  folder, the folder was still empty after the run (both the Wolfram script and the companion).
* Processes: `wolframscript.exe` starts ONE Wolfram kernel (on Wolfram 15.0.1 the program
  `wolfram.exe ... -linkmode Connect ... -mathlink`; older versions call it `WolframKernel`), which ends
  with the run; in 4 of 6 monitored runs WolframScript also started a second, short-lived `wolfram.exe`
  (60 to 68 MB); where its command line was captured it was `wolfram.exe -wlbanner -licenseinfo`, a
  licence query. No parallel subkernels are launched. When the run was killed, its kernel ended as well
  (no kernel was left behind). The companion runs one `python` process.
* Network: none. The scripts contain no network call; during a monitored run the Wolfram process tree
  held only one local socket pair between two ports of `127.0.0.1` (the computer itself) and no
  connection to another computer; the companion had no network endpoint at all. The installation and the
  activation of section 3.3 do need the internet once.

### 5.3 Effects on other parts of the repository

The sha256 of `ks-theory.json` is pinned in `Revision/kohn_sham/results/parameters.json` and
`Revision/kohn_sham/reference/results/parameters.json`, and the count table of
`Revision/docs/PAIR_CREATION_PROOFS.md` (with its test) quotes 46 and 57. A run that reproduces the
committed bytes (as verified) leaves all of these valid; if your run produced different bytes, restore the
committed files (section 5.4) before running anything that reads them.

### 5.4 How to restore the committed state

From the repository root (all systems):

```text
git checkout -- Revision/kohn_sham/ks-theory.json Revision/kohn_sham/reports/ks-theory-wolfram.json Revision/kohn_sham/reports/ks-theory-python.json
```

If you made the Python environment of section 3.6 and no longer need it: Windows PowerShell
`Remove-Item -Recurse -Force ..\ks-venv`, macOS and Linux `rm -rf ../ks-venv`.

## 6. Verification record

* Date: 2026-10-02. The set was verified in two passes on that day: a first pass of the script as
  committed, and a second pass after a review, in which two execution defects of the script were fixed
  (see "Fixes" below) and the fixed script was verified again.
* Commit verified: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the branch `main` of
  `https://github.com/once-ere/Dirac_claude.git` on that day), cloned fresh for every pass into separate
  empty folders: clones A and B in the first pass, clones C1 to C5 in the second pass. First pass: no
  uncommitted file was copied into the clones (the set needs none). Second pass: the only file copied in
  was the fixed `Revision/kohn_sham/theory/verify_ks_theory.wls` (sha256
  `4ce71aaa2c8efd78c8e1508ab72a3223383e21900805c4a34e55a3d5f7deb50d`) from the working tree of the
  author's repository, into clones C2 to C5 (C1 kept the committed script; C2 and C3 ran the committed
  script first and the fixed one afterwards).
* Environment: Windows 11 Pro for Workstations 10.0.26200, Intel Core Ultra 9 275HX (24 cores), 191 GB
  memory; WolframScript 1.14.0 with Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026),
  Professional licence; Python 3.14.5 (system installation `C:\Python314`, whose own pip is 26.1.2 in the
  user's site folder) with numpy 2.4.6, sympy 1.14.0, mpmath 1.3.0; a new private environment made with
  `python -m venv` contains pip 26.1.1; Git 2.51.2.windows.1; PowerShell 7.6.6, Windows PowerShell
  5.1.26100 and Git Bash.
* The two recorded runs, with the fixed script, both in clone C4 from its repository root with
  `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`:

  | Run | Exit code | Printed verdict | Wall clock | Script time | Peak kernel memory |
  | --- | --- | --- | --- | --- | --- |
  | 1 | 0 | `46/46 checks passed; time 33.6 s` | 37.2 s | 33.6 s | 239 MB |
  | 2 | 0 | `46/46 checks passed; time 35.2 s` | 39.1 s | 35.2 s | 238 MB |

  Each run printed exactly 47 lines (46 lines `PASS`, no `FAIL`, no `ERROR`, no line containing `::`);
  the two printed outputs differ only in the `t=` values and in the time of the final line.
* Byte identity, Wolfram script: after run 1 and after run 2, `ks-theory.json`
  (`1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3`) and `ks-theory-wolfram.json`
  (`5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6`) were byte-identical to the committed
  files (`cmp` against `git show HEAD:<file>`) and to each other between the two runs, although both files
  had been rewritten (new modification times). The fix therefore changes no output byte.
* Further complete runs of the fixed script, all with exit code 0, 47 lines, `46/46 checks passed` and
  both outputs byte-identical to the committed files: the PowerShell commands of section 3.5 typed
  literally in clone C5 (`Measure-Command` 37.0 s; `$LASTEXITCODE` printed `0`; `Select-String` printed
  `Revision\kohn_sham\reports\ks-theory-wolfram.json:7:  "summary": {"passed": 46, "failed": 0, "total": 46},`;
  `Get-FileHash` printed the two hashes in capital letters), the Git Bash commands of section 3.5 typed
  literally in clone C3 (`time` 37.3 s; `exit code: 0`; `grep` and `sha256sum` printed the expected
  summary line and hashes), and the run with the folder `Revision/kohn_sham/reports` moved away in
  clone C2 (38.2 s; the script created the folder, which then held only `ks-theory-wolfram.json` with the
  committed sha256). After the two literal runs `git status --porcelain` printed only
  ` M Revision/kohn_sham/theory/verify_ks_theory.wls` (the copied fix, which is not in commit `c2b33cc`).
* Deliberate failure tests of the fixed script (second pass; after each, the moved or changed file was
  restored and the clone was clean except for the copied fix):
  * report `ks-theory-wolfram.json` read-only (clone C3): 46 lines `PASS`, an empty line,
    `OpenWrite::noopen: Cannot open ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json.`,
    `ERROR  cannot write ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json`, no
    `checks passed` line, exit code 1 (38.9 s); the file was not changed (same modification time and
    sha256);
  * `ks-theory.json` read-only (clone C5): 45 lines `PASS` (the last is `brane_band_slope`), then the same
    two lines for `...\Revision\kohn_sham\theory\..\ks-theory.json`, exit code 1 (39.2 s); the file was
    not changed;
  * `Revision/algebra/gammas.json` moved away (clone C5): the only output was
    `ERROR  input file not found: ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json`, exit code 1
    (3.3 s);
  * `Revision/kohn_sham/theory/KohnShamTheory.wl` moved away (clone C3): the only output was
    `ERROR  input file not found: ...\Revision\kohn_sham\theory\KohnShamTheory.wl`, exit code 1 (4.9 s);
  * from a folder that is not the repository root: the only output was
    `Failed to open file at path: Revision/kohn_sham/theory/verify_ks_theory.wls`, exit code 0 (this is
    WolframScript's own behaviour; the script is never read).
* Failure tests of the script of commit `c2b33cc` (second pass, to confirm the review's findings):
  * folder `Revision/kohn_sham/reports` moved away (clone C2): after `PASS  ks_theory_json_written`
    three messages, each after an empty line
    (`OpenWrite::noopen: Cannot open ...\reports\ks-theory-wolfram.json.`, `BinaryWrite::stream: ...`,
    `Close::stream: ...`), then `46/46 checks passed; time 50.5 s`, exit code 0 (55.7 s); 53 lines in
    all; the folder was not created;
  * report `ks-theory-wolfram.json` read-only (clone C3): the same three messages, then
    `46/46 checks passed; time 49.6 s`, exit code 0; the file was not rewritten (modification time
    unchanged), its sha256 was still the committed
    `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6`, and `git status --porcelain`
    printed nothing: the success checks of exit code, final line, hashes and `git status` did not detect
    the failure;
  * `Revision/algebra/gammas.json` moved away (clone C1): the output began with an empty line and
    `Import::nffil: File ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json not found during Import.`,
    followed by `Diagonal::list`, `Set::shape`, `FileHash::noopen`, `StringJoin::string`, three
    `Part::partw` and `General::stop` (each after an empty line), no `fixture_input` line, then
    `FAIL  clifford_relation`, `FAIL  C_B_Gamma`, `PASS  geometry_hidden_coordinate`,
    `PASS  geometry_sqrt_det`; it was still running after 167 s (kernel 171 MB), when `wolframscript.exe`
    was killed; its kernel ended with it; the 1217-byte temporary file it left (identical to the printed
    output) was deleted.
* PowerShell quoting of section 3.3: in Windows PowerShell 5.1.26100, `wolframscript -code "$Version"`
  printed `Error: -code called with no argument.` and `Example format is 'wolframscript -code code'`
  (`$LASTEXITCODE` -1); in PowerShell 7.6.6 the same command printed the kernel banner and `In[1]:=`.
* First pass, script of commit `c2b33cc` (sha256 `d8df4e07...896cab`), all runs with exit code 0,
  `46/46 checks passed` and both outputs byte-identical to the committed files: two recorded runs in
  clone A (`46/46 checks passed; time 37. s`, 39.7 s wall clock, peak kernel 238 MB;
  `46/46 checks passed; time 35.300000000000004 s`, 38.5 s, 238 MB; the outputs identical to each other
  and to `git show HEAD:<file>`); two runs in clone A typed literally in Git Bash as in sections 3.5 and
  5.4 (`time` 43.2 s; `exit code: 0`; expected summary line and hashes; empty `git status --porcelain`;
  the `git checkout -- ...` line of section 5.4 ran without error); in clone B the PowerShell command of
  section 3.5 typed literally (42.7 s), the same with backslashes (46.6 s), Git Bash from the folder
  `Revision` with `wolframscript -file kohn_sham/theory/verify_ks_theory.wls` (44.4 s; the script finds
  its files from any current folder), and six monitored runs (temporary files, process tree, network).
  Failure tests in clone B: the non-root folder (as above) and `gammas.json` moved away (as above; still
  running after 400 s when stopped; the temporary file it left was deleted).
* The companion `check_ks_theory.py`. First pass: twice in clone A with the system Python (exit 0, 57/57,
  74.8 s and 90.4 s, peak 88 MB); once in clone B with a private environment that had been made with
  `python -m venv --system-site-packages` (its `pyvenv.cfg` says `include-system-site-packages = true`),
  which is NOT the command of section 3.6: that environment sees the packages of the system Python, so
  the `pip install` line found them already installed and downloaded nothing (exit 0, 57/57, 73.3 s);
  once more in clone B monitored for network use (exit 0, 57/57). Second pass: the first two commands of
  section 3.6 typed literally in PowerShell from the root of clone C2. `python -m venv ..\ks-venv`
  printed nothing, exit 0, 16.1 s; the new environment contained only pip 26.1.1. The `pip install`
  line printed one line `WARNING: Cache entry deserialization failed, entry ignored`, `Collecting` and
  `Using cached` lines for
  `numpy-2.4.6-cp314-cp314-win_amd64.whl (12.5 MB)`, `sympy-1.14.0-py3-none-any.whl (6.3 MB)` and
  `mpmath-1.3.0-py3-none-any.whl (536 kB)`, `Installing collected packages: mpmath, sympy, numpy`,
  `Successfully installed mpmath-1.3.0 numpy-2.4.6 sympy-1.14.0` and
  `[notice] A new release of pip is available: 26.1.1 -> 26.2.1`; exit 0, 34.4 s. (An independent
  reviewer typing the same commands in another fresh clone on the same machine measured 6.4 s and 39.6 s,
  saw the cache warning twice, and got the same final line.) The checker, run with this environment in
  clone C4: exit 0, 59 lines, last line `{"passed": 57, "failed": 0, "other": 0, "total": 57}`, 77.6 s
  (`shooting time 28.5 s`). Every time `ks-theory-python.json` was byte-identical to the committed file
  (`0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c`) and between runs. pip took the
  package files from its local cache; a download from the Python Package Index on a computer without
  that cache was not exercised.
* Final state: after all runs `git status --porcelain --untracked-files=all --ignored` printed nothing in
  clones A, B and C1, and only ` M Revision/kohn_sham/theory/verify_ks_theory.wls` in clones C2 to C5; the
  three outputs of section 2.3 had the committed sha256 values in every clone.
* Check counts: 46 of 46 (Wolfram) and 57 of 57 (companion), equal to the committed reports and to the
  count table of `Revision/docs/PAIR_CREATION_PROOFS.md` section 9.1.
* Fixes (execution only; no check, tolerance or output changed), in
  `Revision/kohn_sham/theory/verify_ks_theory.wls` (455 lines, sha256 `d8df4e07...896cab` before;
  463 lines, sha256 `4ce71aaa...deb50d` after; `git diff --stat`: 11 lines inserted, 3 deleted):
  1. `writeLF` ignored a failed `OpenWrite`, so a read-only output file or a missing folder
     `Revision/kohn_sham/reports` still ended with `46/46 checks passed` and exit code 0 although the file
     was not written. Now `writeLF` creates a missing folder (`CreateDirectory` with
     `CreateIntermediateDirectories -> True`) and, if the file cannot be opened, prints
     `ERROR  cannot write <path>` and exits with code 1.
  2. A missing input file let the script run on with `$Failed` in place of the gamma matrices, and it
     never finished. Now the script checks that `KohnShamTheory.wl` and `Revision/algebra/gammas.json`
     exist before it reads them; if not, it prints `ERROR  input file not found: <path>` and exits with
     code 1.
  The header comment states the new exit-code rule.
* Open discrepancies: none. Observations for students (not reproduction failures): WolframScript returns
  exit code 0 when it cannot open the script file; byte identity of the detail texts was verified only on
  Windows with Wolfram 15.0.1.
