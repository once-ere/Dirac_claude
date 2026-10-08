# Provenance of the wolframscript set `Revision/kohn_sham/theory/` (the exact Kohn-Sham theory of dirac16complex)

This file tells a student who has never used Wolfram or Python what this set of scripts is, how to run
it from nothing, what it prints and writes, what it changes on the computer, and how it was verified on
2026-10-02 and verified again, in new fresh clones, on 2026-10-07 (section 6; on 2026-10-08 the script's
folders were normalised and the script was re-run, section 6.5). Every number below was
measured on the verification machine or read from the files themselves; nothing is copied from another
document.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

`Revision/kohn_sham/theory/verify_ks_theory.wls` (with its package `KohnShamTheory.wl`) derives, with
exact computer algebra in the Wolfram Language, the Kohn-Sham equations of the author's 16-component
field dirac16complex in the author's primordial 8-dimensional field, checks 46 statements about them,
and writes the result twice: as a check report (`Revision/kohn_sham/reports/ks-theory-wolfram.json`) and
as the recipe of formulas that the numerical Kohn-Sham solvers read (`Revision/kohn_sham/ks-theory.json`).
The same folder holds an independent second engine, the Python/sympy program `check_ks_theory.py`
(58 checks since commit `3d22bc5` of 2026-10-07, 57 before; report
`Revision/kohn_sham/reports/ks-theory-python.json`); it is documented here as an optional companion
(sections 3.6 and 4.5), because it reads the Wolfram output.

### 1.2 The physics, in plain words

* The field. The author's field Psi has 16 complex components and lives in 8 dimensions, named as the
  author names them: x1, x2, x3 are ordinary space; x4 is time; x5, x6, x7 are three extra time-like
  directions whose scale factor shrinks exponentially (they "deflate" while space inflates); x8 is a
  hidden direction. The 16 x 16 gamma matrices that define the field equation are read from the file
  `Revision/algebra/gammas.json` (made by another set, `Revision/algebra/wolfram/`). They are the
  author's eight REAL 16 x 16 Dirac matrices: every entry is 0, +1 or -1 (read from the file on
  2026-10-07: 8 matrices of 16 x 16 integers, values {-1, 0, 1}); `provenance/dirac matrices.md` proves that
  they equal the matrices of the author's notebook entry by entry. This set checks their
  anticommutation relations itself (`clifford_relation`). The field's 16 components are complex numbers,
  and so are some matrices built from the real gammas: B = -i C gamma^(x4) and the block basis V below.
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
addition compares its own results with `ks-theory.json`; its last check (`ks_theory_json_history_label`,
added on 2026-10-07) also confirms that `ks-theory.json` labels the history a4 = A H x4 a PRESCRIBED
BACKGROUND for the reason recorded in `Revision/field_equations_a4/reports/ks-source-conditions.json`.

### 1.4 Which documents cite its results

* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): section 8 (Theorem T3 is proved for
  the Kohn-Sham problem of `Revision/kohn_sham/ks-theory.json`), section 9.1 (the table of report counts:
  `ks-theory-wolfram.json` 46 of 46, `ks-theory-python.json` 58 of 58 since commit `dc6904e`; before it the
  row said 57 of 57, out of date since commit `972cad1`, the discrepancy of section 6.3, resolved in 6.4),
  section 10 (the reproduction commands `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`
  and `python Revision/kohn_sham/theory/check_ks_theory.py`).
* `Revision/tests/test_pair_creation_proofs_publication.py` reads both reports for the count table (its
  test `test_report_count_table` failed from commit `972cad1` to commit `dc6904e` because of the
  out-of-date row; it passes again since `dc6904e`; sections 6.3 and 6.4).
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
  (`adiabaticity.history`, `emt.energyChange`); its report `ks-source-conditions.json` is in turn read by
  the companion (section 2.2).
* `Revision/textbook/TEXTBOOK_SPEC.md` (chapter 14) lists `Revision/kohn_sham/theory`, `ks-theory.json` and
  the reports as sources.
* `provenance/dirac matrices.md` (section "Calculations that use these matrices") lists the three program
  files of this set among the files that read `Revision/algebra/gammas.json`.
* The textbook that another workflow is writing (in progress on 2026-10-07, not yet verified): the
  notebooks `Revision/textbook/notebooks/` 00c, 02d, 03a, 13b, 13c, 14a to 14d, 15a to 15e, 16a, 16b and
  17a (with their `.PROVENANCE.md` files) read or quote `ks-theory.json` or the two reports, and the
  figure captions `Revision/textbook/figures/16b.captions.json` quote the brane-band slope formula of
  `ks-theory.json`.

## 2. Files

All files are stored byte for byte (the repository's `.gitattributes` sets `* -text`, so Git never changes
their line endings). Line counts are counts of line-feed characters (`wc -l`).

### 2.1 The script and the package

| File | sha256 | Lines | Bytes |
| --- | --- | --- | --- |
| `Revision/kohn_sham/theory/verify_ks_theory.wls` (the script you run) | `b2b9d397848c6d7e1ea5796634cc1a08f3d1a8912b47117804e2520a868e9944` | 463 | 41431 |
| `Revision/kohn_sham/theory/KohnShamTheory.wl` (its package, loaded by the script with `Get`) | `554d726af9cff43c680ee9a4a70e7ffa28740a306c91581b6944cc668007f3cf` | 87 | 4575 |
| `Revision/kohn_sham/theory/check_ks_theory.py` (optional companion, Python/sympy) | `e395b794e33c24700a4fcc81e0e7279a5317dc82163811043e4aaa08c8af1458` | 825 | 49831 |

The script's sha256 is that of the version with the execution fix of 2026-10-02 (section 6); this
version is committed since commit `3f0a577c234501e0e073df1ec1640554bf93d764` and is the one re-verified on
2026-10-07. The commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` holds the earlier version (sha256
`d8df4e07976352d07c41c4b38a28ca09626f20d54a237cfba7ba942893596cab`, 455 lines, 40693 bytes). Both
versions perform the same 46 checks and write the same bytes; the earlier one does not stop when an
input file is missing or an output file cannot be written (section 3.7 describes what it does then).
On 2026-10-08 lines 21 and 22 were changed so that the two folders are normalised with `ExpandFileName`
(section 6.5); the table gives that version. The version before (sha256
`4ce71aaa2c8efd78c8e1508ab72a3223383e21900805c4a34e55a3d5f7deb50d`, 463 lines, 41295 bytes) is the one
verified in sections 6.1 to 6.3; both write the same bytes.

The companion was extended on 2026-10-07, outside this verification, by commit
`3d22bc54a15cbfbc1fc38a4860bc2b1a8f0613f1` (a WIP snapshot of another workflow): it gained one check,
`ks_theory_json_history_label`, and one input, `ks-source-conditions.json` (section 2.2); the commit
`972cad112832b9d60564f6c90e0b84b081cd7259` then committed the regenerated report with 58 checks. The
version described in this file is that extended one (verified in section 6.3). Sections 6.1 and 6.2
verified the earlier version (sha256 `28c24832e73dbfc1fb133cabf477d3b6eb59e257e1042030dbbb3c3672e56b80`,
791 lines, 47119 bytes, 57 checks, report sha256
`0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c`, 298 lines, 18572 bytes); the
57 checks of the earlier version are the first 57 checks of the extended one, in the same order and with
the same detail texts.

### 2.2 Inputs (read only, never modified)

| Input | Read by | sha256 | Lines | Bytes |
| --- | --- | --- | --- | --- |
| `Revision/algebra/gammas.json` (the 8 gamma matrices and eta) | both | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 |
| `Revision/algebra/reports/python-gammas.json` (the same matrices rebuilt in Python) | companion only | `b6241910ade6cc282e0aaab75d90fc697247a0d68504618787f547447e2e458b` | 11639 | 94180 |
| `Revision/kohn_sham/ks-theory.json` (the Wolfram output) | the Wolfram script reads back what it has just written; the companion cross-checks it | see 2.3 | | |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` (the a4 source conditions of the Kohn-Sham states, written by `Revision/field_equations_a4/python/check_ks_source_conditions.py`) | companion only (check `ks_theory_json_history_label`) | `0597509efe64e0686dcf3cc916121317aacca01c6e73d902edc16f434287361e` | 48 | 4150 |

The script finds the package and the inputs relative to its own location (`$InputFileName`), not relative
to the current folder. Before it reads the package and before it reads `gammas.json` it checks that the
file exists; if not, it prints `ERROR  input file not found: <full path>` and stops with exit code 1.

### 2.3 Outputs (rewritten on every run; UTF-8, LF line endings, no time stamps)

| Output | Written by | sha256 (committed and reproduced) | Lines | Bytes |
| --- | --- | --- | --- | --- |
| `Revision/kohn_sham/ks-theory.json` (the formulas for the solvers) | `verify_ks_theory.wls` | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` | 477 | 17278 |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` (46 checks) | `verify_ks_theory.wls` | `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6` | 56 | 10291 |
| `Revision/kohn_sham/reports/ks-theory-python.json` (58 checks) | `check_ks_theory.py` | `7ae5c6be4dbaf167093a7c0799d9c102d3a7d1d17ec93311a1b17ea5bc26cf9c` | 303 | 19402 |

If the folder `Revision/kohn_sham/reports` is missing, both scripts create it. If an output file cannot
be opened for writing (for example because it is read-only), the Wolfram script prints the Wolfram
message `OpenWrite::noopen: Cannot open <full path>.` and the line `ERROR  cannot write <full path>`, and
stops with exit code 1.

## 3. How to run it (complete instructions)

All times in this file were measured on one verification machine (section 4.4) while other jobs were
running on it; on your computer they can be shorter or longer.

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, and an internet connection for the installation
  and the download (the script itself needs no network).
* About 1 GB of free disk space for the repository (a fresh clone measured 519 MB, of which 128 MB is
  the Git history, on 2026-10-02, and 659 MB, of which 195 MB is the Git history, on 2026-10-07: the
  repository grows) plus the space the Wolfram installer asks for.
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

The download took 13 to 28 seconds on the verification machine (about 13 s on 2026-10-02; 15.8 s,
17.5 s, 24.9 s and 27.3 s on 2026-10-07, when the repository was larger). You are now in the
repository root: the
folder that contains the folder `Revision`. Every command below is run from here. Do not open and save
the JSON files of section 2 with an editor: an editor may change their line endings, and then they are
no longer byte-identical to the committed files.

### 3.5 Run the script

Windows PowerShell (forward slashes and backslashes both work):

```powershell
$out = wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls
$LASTEXITCODE
$out
$out.Count
($out | Select-String -SimpleMatch '::').Count
```

macOS and Linux:

```bash
out=$(wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls)
echo "exit code: $?"
echo "$out"
echo "$out" | wc -l
echo "$out" | grep -c '::'
```

What the five lines do:

* The first line runs the script and keeps every line it prints in the variable `out` instead of showing
  it. Nothing appears on the screen while it runs (nothing appeared in the verified runs); wait until the
  prompt comes back. The run takes about 40 to 85 seconds, longer on a busy computer. If a line does
  appear during this wait, it came on the error stream and is not kept in `out`; it means that something
  went wrong (section 3.7).
* The second line shows the exit code of the run. Type it immediately after the first line, because it
  reports the most recent program that ran.
* The third line shows the kept lines (section 4.1 lists them).
* The fourth line counts them. It must print `47` (on macOS `wc -l` puts spaces before the number).
* The fifth line counts the lines that contain `::`. It must print `0`.

These five lines write nothing into the repository, and the variable `out` is forgotten when you close the
terminal. Optional, to see the lines while the script runs and to measure its run time (this runs the
script once more): in PowerShell
`Measure-Command { wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls | Out-Default }`
(the output is shown, then `TotalSeconds`), on macOS and Linux
`time wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`.

Then check the result:

1. The last line shown by `$out` (or `echo "$out"`) must begin with `46/46 checks passed`, the exit code
   must be `0`, the line count must be `47` (46 lines beginning with `PASS` and the final line), and the
   count of lines containing `::` must be `0`. A line containing `::` is a Wolfram message (for example
   `OpenWrite::noopen`) and means that something went wrong even if the other checks below look right.
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
   `venv` line prints nothing (it took 6 to 17 s on the verification machine). A new environment
   contains only pip, so the `pip install` line downloads three package files of about 19 MB together
   (numpy 12.5 MB, sympy 6.3 MB, mpmath 0.5 MB) from the Python Package Index, or takes them from pip's
   local cache if this computer downloaded them before (then the lines say `Using cached ...`). It prints
   `Collecting ...` lines, `Installing collected packages: mpmath, sympy, numpy`, and must end with the
   line `Successfully installed mpmath-1.3.0 numpy-2.4.6 sympy-1.14.0`; it took 34 to 94 s on the
   verification machine (from the cache; the longer times on a busy day). Two kinds of extra lines are
   harmless and can be ignored: a notice `[notice] A new release of pip is available: ...` with a
   suggested upgrade command (you need not upgrade pip), and on some computers
   `WARNING: Cache entry deserialization failed, entry ignored` (pip ignores that cache entry and
   continues). If your Python is older than 3.14 and pip cannot find these exact versions,
   `pip install numpy sympy mpmath` installs versions for your Python; the verdicts are expected to be the
   same, but only the versions above were verified. The checker itself prints its lines while it runs and
   takes about 75 to 165 seconds, longer on a busy computer.
3. Check: the last line must be `{"passed": 58, "failed": 0, "other": 0, "total": 58}`, the exit code
   `0`, and the report `Revision/kohn_sham/reports/ks-theory-python.json` must have the sha256
   `7ae5c6be4dbaf167093a7c0799d9c102d3a7d1d17ec93311a1b17ea5bc26cf9c` (same hash commands as in
   section 3.5, step 3); `git status --porcelain` must again print nothing. The exit code `0` alone does
   not prove success: a run without `Revision/kohn_sham/ks-theory.json` also ends with exit code `0`
   (section 3.7), so always read the last line.

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
  verification machine WolframScript uses `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`;
  that folder also contains `WolframKernel.exe` and `MathKernel.exe`; older versions have only
  `WolframKernel.exe` on Windows and `WolframKernel` on macOS and Linux), or reinstall the Wolfram Engine
  or Mathematica.
* The only output is `Failed to open file at path: Revision/kohn_sham/theory/verify_ks_theory.wls`: you
  are not in the repository root. CAUTION: in this case WolframScript still returns exit code 0
  (observed during the verification), so always read the last line. WolframScript writes this message to
  the error stream, so with the commands of section 3.5 it appears on the screen at once, after about
  4 seconds, during the first line, and is NOT kept in `out`: `$out` (or `echo "$out"`) then shows
  nothing, the line count is `0` in PowerShell and `1` (an empty line) on macOS and Linux, and the `::`
  count is `0` (observed in PowerShell 7.6.6 and Git Bash). Go to the folder that contains
  `Revision` (`cd $HOME\Dirac_claude` in PowerShell, `cd ~/Dirac_claude` on macOS and Linux) and run
  again.
* The only output is the line
  `ERROR  input file not found: ...\Revision\algebra\gammas.json` (the dots stand
  for the full path of your repository folder; on macOS and Linux the path has forward slashes; observed
  2026-10-08 with the version of section 6.5, which normalises the folders; the version before it printed
  `...\Revision\kohn_sham\theory\..\..\algebra\gammas.json`, as in the run logs of sections 6.1 to 6.3), and the
  exit code is `1` (observed: after about 3 to 6 seconds): the input file `Revision/algebra/gammas.json` is
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
  `checks passed` line, and the exit code is `1` (observed; with the commands of section 3.5 the line
  count is `49` for the report and `48` for `ks-theory.json`, and the `::` count is `1`): an output file of
  section 2.3 is read-only, or the folder is not writable. The file is left unchanged. Make the file writable again (Windows
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
* Python companion: the line before the last is `[pending] ks_theory_json_basis  t=...s` and the last
  line is `{"passed": 54, "failed": 0, "other": 1, "total": 55}`, although the exit code is `0`
  (observed): the file `Revision/kohn_sham/ks-theory.json` is missing, so the companion skipped its
  cross-check of that file (it marks this `pending`, which does not count as a failure). The run has
  also OVERWRITTEN the committed `Revision/kohn_sham/reports/ks-theory-python.json` with this
  incomplete report. Restore `ks-theory.json` with `git checkout -- Revision/kohn_sham/ks-theory.json`
  (or run the Wolfram script of section 3.5, which writes it), restore the report with the command of
  section 5.4, and run the companion again.
* Python companion: a line `[FAIL] ks_theory_json_history_label  t=...s`, the last line
  `{"passed": 57, "failed": 1, "other": 0, "total": 58}` and exit code `1` (observed with the file
  `Revision/field_equations_a4/reports/ks-source-conditions.json` moved away): that input is missing or
  changed, or `ks-theory.json` no longer carries the PRESCRIBED BACKGROUND label. Restore both with
  `git checkout -- Revision/field_equations_a4/reports/ks-source-conditions.json Revision/kohn_sham/ks-theory.json`,
  restore the report with the command of section 5.4, and run again. If the files were not changed and
  the check still fails, do not edit anything; report the failing check name.

## 4. Expected output

### 4.1 Printed on the screen

The Wolfram script prints exactly 47 lines and nothing else (no warnings, no messages): one line per
check, in this order, of the form `PASS  <name>  t=<seconds>` (two spaces before and after the name),
then the final line. The seconds count from the start of the checks and vary from run to run; they can
show binary rounding such as `t=0.7000000000000001` or `t=26.700000000000003`, or a whole number written
with a trailing point such as `t=32.` (Wolfram's way of printing 32.0), which is normal. On
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

(This is recorded run 1 of 2026-10-02, section 6.) The runs of 2026-10-07 printed the same 47 lines in
the same order with larger `t=` values, because the machine was busier that day; the final lines of the
two recorded runs of section 6.2 were `46/46 checks passed; time 46.300000000000004 s` and
`46/46 checks passed; time 45.800000000000004 s`, those of the three complete runs of section 6.3
`46/46 checks passed; time 76.80000000000001 s`, `46/46 checks passed; time 67.2 s` and
`46/46 checks passed; time 64. s`.
The longest single step is the explicit angular integral of `gas_angular_average` (23 to 25 s on
2026-10-02, 30.4 and 30.7 s in section 6.2, 41.6 to 49.5 s in section 6.3), then the energy-momentum
components of `emt_orbital_components` (7 to 8 s; 10.5 and 8.8 s; 10.6 to 17.4 s) and the NDSolve
shooting of `brane_band_slope` (about 2 s; 2.6 and 2.7 s; 3.1 to 4.5 s).

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
Workstations. Other jobs were running Wolfram kernels on the same machine at the same time (on 2026-10-02
5, 8 and 9 of them at the three moments checked), so a quiet computer may be faster. The script starts no
parallel kernels.

* 2026-10-02, wall-clock time of the whole command: 36.6 to 46.6 s over 14 timed complete runs, of which 9
  with the script of commit `c2b33cc` and 5 with the fixed script (37.0 to 39.1 s; 37.2 s and 39.1 s for
  the two recorded runs of section 6.1); the script's own final `time` value: 33.1 to 42.9 s over 17 runs
  (fixed script: 33.6 to 35.2 s over 5 runs).
* 2026-10-02, peak memory (working set): the Wolfram kernel `wolfram.exe` 232 to 239 MB;
  `wolframscript.exe` 17 MB.
* Re-verification of 2026-10-07 (same script, same machine; other workflows were running Wolfram kernels
  at the same time, 14 and 16 `wolfram.exe` processes at two moments checked): wall clock 49.5 s and
  51.5 s for the two recorded runs (script time 46.3 s and 45.8 s), 55.0 s for the PowerShell commands of
  section 3.5 typed literally (script time 51.1 s), 52.7 s and 57.1 s for the two failure tests that run
  all checks (section 6.2); peak memory of the kernel 238 MB and 237 MB, of `wolframscript.exe` 17 MB, of
  the short licence query `wolfram.exe -wlbanner -licenseinfo` 53 MB and 54 MB.
* Third verification of 2026-10-07 (section 6.3; same script, same machine, still busier: 4 to 15
  `wolfram.exe` processes at the moments checked, and the companion of section 6.3 ran at the same time):
  wall clock 82.2 s for the PowerShell commands of section 3.5 typed literally (script time 76.8 s),
  73.8 s for the `Measure-Command` form (`TotalSeconds : 73.8468607`, script time 67.2 s), 69.5 s for the
  macOS/Linux commands of section 3.5 in Git Bash (script time 64. s), 58.1 s for the PowerShell commands
  of section 3.5 in Windows PowerShell 5.1 (script time 52.3 s), 72.5 s and 55.1 s for the failure tests
  with a read-only `ks-theory.json` and a read-only report, 4.3 s for the failure test with `gammas.json`
  missing.
* In all, over every complete run recorded in this file, the wall-clock time of the Wolfram script was
  36.6 to 82.2 s.

### 4.5 The optional Python companion

It prints 60 lines: 58 lines `[PASS] <name>  t=<seconds>s`, the line `shooting time <seconds> s` (right
after `[PASS] brane_band_slope`), and the final line

```text
{"passed": 58, "failed": 0, "other": 0, "total": 58}
```

The first three lines are `[PASS] fixture_input  t=0.0s`, `[PASS] fixture_python_equals_wolfram  t=0.0s`,
`[PASS] clifford_relation  t=0.0s`; the last four checks are `ks_theory_json_basis`,
`ks_theory_json_exchange`, `ks_theory_json_slope` (the cross-check of `ks-theory.json`) and
`ks_theory_json_history_label` (the PRESCRIBED BACKGROUND label, against `ks-source-conditions.json`).
Exit code `0` when no check fails, `1` if a check fails. Caution: an exit code `0` alone does not prove
success for the companion either. A check whose verdict is neither PASS nor FAIL (the verdict `pending`,
printed when `ks-theory.json` is missing) is counted as `"other"` and does not change the exit code
(section 3.7); so the last line must read exactly 58 of 58 as above. It writes
`Revision/kohn_sham/reports/ks-theory-python.json` (303 lines, 19402 bytes, sha256
`7ae5c6be4dbaf167093a7c0799d9c102d3a7d1d17ec93311a1b17ea5bc26cf9c`), whose `"summary"` block (lines 5
to 10) holds `"passed": 58`, `"failed": 0`, `"other": 0`, `"total": 58`. Run time of the extended version
(section 6.3): 134.3 s and 128.5 s wall clock (last time stamp 123.5 s and 119.3 s; `shooting time
38.6 s` and `42.5 s`), on a busy machine. The earlier 57-check version (sections 6.1 and 6.2) took 73.3 to
90.4 s wall clock over 4 timed runs on 2026-10-02 (the script's own last time stamp 65.3 to 88.4 s over 5
runs; the RK4 shooting, printed as `shooting time`, 28.5 to 39.7 s of it; peak memory 88 MB), and 111.1 s
and 101.6 s on 2026-10-07 (last time stamp 108.1 s and 97.9 s; `shooting time 47.1 s` and `39.5 s`; peak
memory 89 MB and 88 MB). The added check reads two small JSON files; its time stamp is at most 0.1 s
after that of the check before it.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

* The Wolfram script OVERWRITES two committed files on every run: `Revision/kohn_sham/ks-theory.json` and
  `Revision/kohn_sham/reports/ks-theory-wolfram.json` (their modification time changes; on the
  verification machine their bytes stayed identical to the committed ones). If the folder
  `Revision/kohn_sham/reports` is missing, the Wolfram script creates it (observed; the script of commit
  `c2b33cc` did not).
* The companion OVERWRITES `Revision/kohn_sham/reports/ks-theory-python.json` (it would create the folder
  `Revision/kohn_sham/reports` if it were missing). It does so on every run, also when an input is
  missing and the report is then incomplete (section 3.7); restore it as in section 5.4.
* Nothing else in the repository is created or changed: `git status --porcelain --untracked-files=all --ignored`
  printed nothing after the recorded runs of both scripts and at the end of all runs in both clones of
  the first pass (no new file, no ignored file, no `__pycache__` folder); in the clones of the second
  pass it printed only the line ` M Revision/kohn_sham/theory/verify_ks_theory.wls`, the fixed script
  that had been copied in (section 6). On 2026-10-07, with the fixed script committed, it printed nothing
  in all three fresh clones of section 6.2 and in all three fresh clones of section 6.3 after all runs.

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
  `wolfram.exe ... -linkmode Connect ... -mathlink`, although the installation folder also contains
  `WolframKernel.exe`; older versions have only `WolframKernel`), which ends
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
`Revision/docs/PAIR_CREATION_PROOFS.md` (with its test) quotes 46 and 58 (it quoted 57 from commit
`972cad1` until commit `dc6904e`; section 6.4). A run that reproduces the committed bytes (as verified) leaves all of these as they were; if
your run produced different bytes, restore the committed files (section 5.4) before running anything that
reads them.

### 5.4 How to restore the committed state

From the repository root (all systems):

```text
git checkout -- Revision/kohn_sham/ks-theory.json Revision/kohn_sham/reports/ks-theory-wolfram.json Revision/kohn_sham/reports/ks-theory-python.json
```

If you made the Python environment of section 3.6 and no longer need it: Windows PowerShell
`Remove-Item -Recurse -Force ..\ks-venv`, macOS and Linux `rm -rf ../ks-venv`.

## 6. Verification record

The set was verified on 2026-10-02 (section 6.1) and verified again on 2026-10-07 (section 6.2), after the
verification workflow had been interrupted by a session limit and relaunched: the earlier record was not
trusted unchecked but repeated in new fresh clones. Later on 2026-10-07 an independent review of this
file reported six minor findings; they were checked, and the set (with the companion as extended that
day) was verified a third time in new fresh clones (section 6.3). Sections 6.1 and 6.2 verified the
earlier, 57-check version of the companion (section 2.1); the fixed Wolfram script (second pass of
section 6.1, sections 6.2 and 6.3) and its two outputs are the same in all of them.

Until section 6.3, section 3.5 showed the run command in its plain form
(`wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`, then `$LASTEXITCODE` or
`echo "exit code: $?"`), without `$out =` / `out=$(...)` and the two counting lines; "the commands of
section 3.5 typed literally" in sections 6.1 and 6.2 means that plain form.

### 6.1 Verification of 2026-10-02

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
  * `ks-theory.json` read-only (clone C5): 45 lines `PASS` (the last is `brane_band_slope`), an empty line,
    then the same two lines for `...\Revision\kohn_sham\theory\..\ks-theory.json` (48 lines in all; the
    empty line was left out of this entry when it was first written and was counted when the test was
    repeated on 2026-10-07, section 6.3), exit code 1 (39.2 s); the file was not changed;
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

### 6.2 Re-verification of 2026-10-07

* Date: 2026-10-07 (the verification workflow of 2026-10-02 had been interrupted by a session limit and was
  relaunched; the runs, outputs, counts and failure behaviour were checked again against new runs; what
  was not repeated is listed at the end of this section).
* Commit verified: `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (the branch `main` of
  `https://github.com/once-ere/Dirac_claude.git` on that day), cloned fresh into two empty folders, clones A
  and B. A third fresh clone C, made later that day, received the newer commit
  `8cbd03a02f7771bce9e199f5d48cd41a979f1f06`, which changed only `HANDOFF.md` and
  `Revision/workflows/dirac_matrices_audit.js`; the files of this set and its inputs are the same in both
  commits. No uncommitted file was copied into any clone: the execution fix of section 6.1 is committed
  (since commit `3f0a577`), and the script, the package, the companion, the two inputs and the three outputs
  had exactly the sha256 values, line counts and byte counts that section 2 gave at that time (measured in
  clone B; for the script that is the version before section 6.5, sha256 `4ce71aaa...b50d`, see section 2.1).
* Environment: Windows 11 Pro for Workstations 10.0.26300 (`ver`: 10.0.26300.9457), Intel Core Ultra 9
  275HX (24 cores), 191 GB memory; WolframScript 1.14.0 with Wolfram 15.0.1 for Microsoft Windows (64-bit)
  (July 2, 2026), Professional licence; Python 3.14.5 (system installation `C:\Python314`) with numpy
  2.4.6, sympy 1.14.0, mpmath 1.3.0; Git 2.51.2.windows.1; PowerShell 7.6.6 and Git Bash. The recorded runs
  were started from the clone's repository root with PowerShell's `Start-Process` (standard output and
  error redirected to files); the process tree was sampled every 0.3 s for its working-set memory.
* The two recorded runs, both in clone A with `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`:

  | Run | Exit code | Printed verdict | Wall clock | Script time | Peak kernel memory |
  | --- | --- | --- | --- | --- | --- |
  | 1 | 0 | `46/46 checks passed; time 46.300000000000004 s` | 49.5 s | 46.3 s | 238 MB |
  | 2 | 0 | `46/46 checks passed; time 45.800000000000004 s` | 51.5 s | 45.8 s | 237 MB |

  Each run printed exactly 47 lines, each ending with a carriage return and a line feed (46 lines `PASS`
  in the order of section 4.1, no `FAIL`, no `ERROR`, no line containing `::`) and nothing on the error
  stream; the two printed outputs differ only in the `t=` values and in the time of the final line. Each
  run also started the short licence query `wolfram.exe -wlbanner -licenseinfo` (53 MB, 54 MB).
* Byte identity: after run 1 and after run 2, `ks-theory.json`
  (`1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3`) and `ks-theory-wolfram.json`
  (`5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6`) were byte-identical to the committed
  files (`cmp` against `git show HEAD:<file>`) and to each other between the two runs, although both files
  had been rewritten (their modification times changed with each run). Their content was checked as in
  section 4.3: line 7 of the report is `  "summary": {"passed": 46, "failed": 0, "total": 46},`, 46 checks,
  all `PASS`; `ks-theory.json` has 18 top-level keys from `description` to `solverChecklist`,
  `checksNumeric.braneBandSlope_M1_H1_L3_a0` is `"1.9051482536448664"`, and `adiabaticity.historyStatus`
  begins with `PRESCRIBED BACKGROUND`; the `brane_band_slope` detail ends exactly as quoted in section 4.3.
* The PowerShell commands of section 3.5 typed literally in clone C: `Measure-Command` printed
  `TotalSeconds : 55.0439534` after the 47 lines (final line `46/46 checks passed; time 51.1 s`);
  `$LASTEXITCODE` printed `0`; `Select-String` found line 7 `  "summary": {"passed": 46, "failed": 0, "total": 46},`;
  `Get-FileHash` printed `1BF41D79318A24A4BB0BD6C34F0499C399CC8054E8ADD69CA08D758C5D55AFE3` and
  `5D803AF6B270BC7DD93120907C13C28E855C4BA351CCDC3B411D7F8086112AE6`; `git status --porcelain` printed
  nothing.
* The failure tests of section 3.7, repeated in clone A with the committed (fixed) script; after each the
  moved or changed file was restored:
  * `Revision/algebra/gammas.json` moved away: the only output was
    `ERROR  input file not found: ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json`, exit code 1
    (5.3 s);
  * `Revision/kohn_sham/theory/KohnShamTheory.wl` moved away: the only output was
    `ERROR  input file not found: ...\Revision\kohn_sham\theory\KohnShamTheory.wl`, exit code 1 (5.2 s);
  * run from the folder `Revision` (not the repository root) with the command of section 3.5: the only
    output was `Failed to open file at path: Revision/kohn_sham/theory/verify_ks_theory.wls`, exit code 0
    (5.3 s);
  * report `ks-theory-wolfram.json` read-only: 49 lines (46 lines `PASS`, an empty line,
    `OpenWrite::noopen: Cannot open ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json.` and
    `ERROR  cannot write ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json`), no
    `checks passed` line, exit code 1 (57.1 s); the file kept its modification time and the committed
    sha256;
  * folder `Revision/kohn_sham/reports` moved away: 47 lines, `46/46 checks passed; time 47.400000000000006 s`,
    exit code 0 (52.7 s); the script created the folder, which then held only `ks-theory-wolfram.json`
    (10291 bytes) with the committed sha256.
* The companion `check_ks_theory.py`, twice in clone B with the system Python
  (`C:\Python314\python.exe Revision/kohn_sham/theory/check_ks_theory.py` from the repository root): both
  runs exit code 0, 59 lines (57 lines `[PASS]`, the `shooting time` line, the final line
  `{"passed": 57, "failed": 0, "other": 0, "total": 57}`), nothing on the error stream; 111.1 s and
  101.6 s wall clock (`shooting time 47.1 s` and `39.5 s`), peak memory 89 MB and 88 MB.
  `ks-theory-python.json` (`0f2dd2975db2af5b9e63453c6fe028c64e80aee3be921d4932c252acfb150f6c`) was
  byte-identical to the committed file after each run and between the two runs.
* Final state: after all runs `git status --porcelain --untracked-files=all --ignored` printed nothing in
  clones A, B and C (no file changed, created or left behind in the repository).
* Check counts: 46 of 46 (Wolfram) and 57 of 57 (companion), equal to the committed reports and to the
  count table of `Revision/docs/PAIR_CREATION_PROOFS.md` section 9.1.
* Not repeated in this second verification (recorded in section 6.1 only): the Git Bash commands of
  section 3.5, the private-environment commands of section 3.6, the read-only `ks-theory.json` test (these
  three were repeated in section 6.3), the monitoring of temporary files, settings file and network of
  section 5.2, and the failure tests of the script of commit `c2b33cc`.
* Fixes: none in this second verification; no file of the set was changed (only this provenance file was
  updated).
* Open discrepancies: none at commit `a4c5eda` (the companion was extended later that day; section 6.3).

### 6.3 Third verification of 2026-10-07 (after an independent review)

* Date: 2026-10-07. An independent review of this file, made on the same machine in fresh clones of the
  commits `c8f6022` and `565c9b0` (in which the set was still that of section 6.2), reported six minor
  findings. Each was checked again here in new fresh clones; the outcome is listed at the end of this
  section. In the meantime the companion had been extended (section 2.1), so the companion was verified
  anew.
* Commit verified: `772f7741660c758ba16ea3232aaa3bde22fb4888` (clone F1) and
  `d4431b20f839553b37eaadf1f0c12e869c7070b4` (clones F2 and F3, made a few minutes later; it differs
  from `772f774` only in `Revision/kohn_sham/solver/README.md`), each cloned fresh from
  `https://github.com/once-ere/Dirac_claude.git` into an empty folder. No uncommitted file was copied into
  any clone. The script, the package, the companion, the inputs and the outputs had exactly the sha256
  values, line counts and byte counts that section 2 gave at that time (measured in clone F1; for the script
  that is the version before section 6.5, sha256 `4ce71aaa...b50d`, see section 2.1).
* Environment: Windows 11 Pro for Workstations 10.0.26300, Intel Core Ultra 9 275HX (24 cores), 191 GB
  memory; WolframScript 1.14.0 with Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026),
  Professional licence; Python 3.14.5 (system installation `C:\Python314`); a private environment made
  with the commands of section 3.6 (pip 26.1.1, numpy 2.4.6, sympy 1.14.0, mpmath 1.3.0); Git
  2.51.2.windows.1; PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444 and Git Bash. The PowerShell
  commands were run from a script file
  (`pwsh -NoProfile -File ...`) that wrote everything printed to a log file; it contained the five
  PowerShell lines of section 3.5, the optional `Measure-Command` line, the `Select-String` and
  `Get-FileHash` lines and the `venv` and `pip install` lines of section 3.6 word for word, and ran the
  checker line of section 3.6 with its output kept in a variable for counting
  (`$out = ..\ks-venv\Scripts\python.exe Revision/kohn_sham/theory/check_ks_theory.py`). The five macOS/Linux
  lines of section 3.5 and the `grep` and `sha256sum` lines ran word for word from a `bash` script. Other
  workflows were running Wolfram kernels at the same time (4 to 15 `wolfram.exe` processes at the moments
  checked), and the companion runs of clone F2 overlapped with the Wolfram runs of clone F1.
* The Wolfram script, complete runs:

  | Run | Clone | Commands | Exit code | Printed verdict | Line count / `::` count | Wall clock |
  | --- | --- | --- | --- | --- | --- | --- |
  | 1 | F1 | PowerShell, section 3.5 | 0 | `46/46 checks passed; time 76.80000000000001 s` | `47` / `0` (printed by the commands) | 82.2 s |
  | 2 | F1 | PowerShell, the optional `Measure-Command` line of section 3.5 | 0 | `46/46 checks passed; time 67.2 s` | 47 / 0 (counted in the log) | 73.8 s (`TotalSeconds : 73.8468607`) |
  | 3 | F3 | Git Bash, the macOS/Linux commands of section 3.5 | 0 (`exit code: 0`) | `46/46 checks passed; time 64. s` | `47` / `0` (printed by the commands) | 69.5 s |
  | 4 | F3 | Windows PowerShell 5.1.26100.9444, the PowerShell commands of section 3.5 | 0 | `46/46 checks passed; time 52.300000000000004 s` | `47` / `0` (printed by the commands) | 58.1 s |

  Each run printed the 46 `PASS` lines in the order of section 4.1 and nothing else. After each run
  `ks-theory.json` and `ks-theory-wolfram.json` were byte-identical to the committed files (`cmp` against
  `git show HEAD:<file>`), and the outputs of runs 1 and 2 were identical to each other; `Get-FileHash`
  (runs 1 and 4) and `sha256sum` (run 3) printed the two hashes of section 3.5, step 3; `Select-String`
  (run 2) and `grep` (run 3) found line 7 `  "summary": {"passed": 46, "failed": 0, "total": 46},`;
  `git status --porcelain` printed nothing after each run.
* Failure tests of the Wolfram script (clone F1, with the PowerShell commands of section 3.5; after each
  the file was restored):
  * `Revision/kohn_sham/ks-theory.json` read-only: exit code 1; the counting lines printed `48` and `1`;
    the 48 lines were 45 lines `PASS` (the last `PASS  brane_band_slope  t=66.8`), one empty line,
    `OpenWrite::noopen: Cannot open ...\Revision\kohn_sham\theory\..\ks-theory.json.` and
    `ERROR  cannot write ...\Revision\kohn_sham\theory\..\ks-theory.json`; 72.5 s; the file kept its
    sha256 and its modification time;
  * report `Revision/kohn_sham/reports/ks-theory-wolfram.json` read-only: exit code 1; the counting lines
    printed `49` and `1`; the 49 lines were 46 lines `PASS` (the last `PASS  ks_theory_json_written`), one
    empty line, `OpenWrite::noopen: Cannot open ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json.`
    and `ERROR  cannot write ...\Revision\kohn_sham\theory\..\reports\ks-theory-wolfram.json`; 55.1 s; the
    report kept its sha256 and its modification time;
  * `Revision/algebra/gammas.json` moved away: exit code 1; the only line was
    `ERROR  input file not found: ...\Revision\kohn_sham\theory\..\..\algebra\gammas.json` (count `1`);
    4.3 s;
  * run from the folder `Revision` (not the repository root): exit code 0 after 4.2 s;
    `Failed to open file at path: Revision/kohn_sham/theory/verify_ks_theory.wls` appeared on the error
    stream, `out` stayed empty, and the counting lines printed `0` and `0` in PowerShell, `1` and `0` in
    Git Bash.
* The companion (clone F2, PowerShell commands of section 3.6): `python -m venv ..\ks-venv` printed
  nothing, exit code 0, 16.2 s; the `pip install` line printed four lines
  `WARNING: Cache entry deserialization failed, entry ignored`, the `Collecting` and `Using cached` lines
  of the three packages (`numpy-2.4.6-cp314-cp314-win_amd64.whl (12.5 MB)`,
  `sympy-1.14.0-py3-none-any.whl (6.3 MB)`, `mpmath-1.3.0-py3-none-any.whl (536 kB)`),
  `Installing collected packages: mpmath, sympy, numpy`,
  `Successfully installed mpmath-1.3.0 numpy-2.4.6 sympy-1.14.0` and the notice
  `[notice] A new release of pip is available: 26.1.1 -> 26.2.1`; exit code 0, 94.0 s. Two runs of the
  checker: exit code 0, 60 lines (58 lines `[PASS]`, the `shooting time` line, the final line
  `{"passed": 58, "failed": 0, "other": 0, "total": 58}`), nothing on the error stream, 134.3 s and
  128.5 s (`shooting time 38.6 s` and `42.5 s`); after each run `ks-theory-python.json` was
  byte-identical to the committed file
  (`7ae5c6be4dbaf167093a7c0799d9c102d3a7d1d17ec93311a1b17ea5bc26cf9c`), and the two reports were
  identical to each other; `git status --porcelain` printed nothing.
* Failure tests of the companion (clone F2; after each, the moved file was put back and the report
  restored with `git checkout -- Revision/kohn_sham/reports/ks-theory-python.json`):
  * `Revision/kohn_sham/ks-theory.json` moved away: exit code 0, 57 lines (54 lines `[PASS]`, the
    `shooting time` line, then `[pending] ks_theory_json_basis  t=150.6s` and
    `{"passed": 54, "failed": 0, "other": 1, "total": 55}`); 161.3 s. `git status --porcelain` then printed
    ` D Revision/kohn_sham/ks-theory.json` and ` M Revision/kohn_sham/reports/ks-theory-python.json`: the
    committed report had been overwritten by an incomplete one (55 checks; sha256
    `7b30817ca1a0d5316d10713d1620ed3b5ebae42586c6a31b81471b7b4c029f44`, 288 lines, 18215 bytes);
  * `Revision/field_equations_a4/reports/ks-source-conditions.json` moved away: exit code 1, 60 lines,
    `[FAIL] ks_theory_json_history_label  t=109.8s`, last line
    `{"passed": 57, "failed": 1, "other": 0, "total": 58}`; 137.7 s; the report was overwritten (restored).
* The kernel folder: `C:\Program Files\Wolfram Research\Wolfram\15.0.1\` contains `wolfram.exe` (65768
  bytes), `WolframKernel.exe` (248552 bytes) and `MathKernel.exe` (248552 bytes);
  `wolframscript -configure` lists `//WOLFRAMSCRIPT_KERNELPATH=C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`
  (commented out).
* The count table of `Revision/docs/PAIR_CREATION_PROOFS.md`: in clone F3,
  `python -B Revision/tests/test_pair_creation_proofs_publication.py -k test_report_count_table` ended with
  `FAILED (failures=1)`: the row
  ``| `Revision/kohn_sham/reports/ks-theory-python.json` | 58 | 58 | 0 |`` is not in the document, whose
  section 9.1 still has 57.
* Final state: after all runs `git status --porcelain --untracked-files=all --ignored` printed nothing in
  clones F1, F2 and F3.
* Check counts: 46 of 46 (Wolfram) and 58 of 58 (companion), equal to the committed reports. The count
  table of `Revision/docs/PAIR_CREATION_PROOFS.md` section 9.1 has 46 (equal) and 57 (not equal).
* Review findings and their outcome:
  1. Run times exceeded on a busy machine: confirmed (this verification measured up to 82.2 s for the
     Wolfram script, 94.0 s for `pip install` and 161.3 s for the companion); sections 3.4 to 3.7, 4.4
     and 4.5 now give the measured ranges and say that the times come from one busy machine.
  2. The companion ends with exit code 0 when `ks-theory.json` is missing: confirmed (also with the
     extended companion, whose `sys.exit` line is now line 825); documented in sections 3.6, 3.7, 4.5 and
     5.1. The program was not changed (the verdict `pending` is its intended behaviour before the Wolfram
     export exists).
  3. No command to count the 47 lines and the `::` lines: confirmed; section 3.5 now gives such commands
     for PowerShell and for macOS/Linux; they were run above (printed `47`/`0`, and `48`/`1` and `49`/`1`
     in the two read-only tests); section 3.7 says what they print when the script file cannot be found.
  4. The read-only `ks-theory.json` entry of section 6.1 left out the empty line: confirmed (48 lines
     above); section 6.1 corrected.
  5. The kernel-path bullet implied that Wolfram 15.0.1 has no `WolframKernel.exe`: confirmed; sections
     3.7 and 5.2 corrected.
  6. A summary of the earlier run said that this file was uncommitted: confirmed as stale (the file is
     committed since commit `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6`); it concerned no text of this file,
     so nothing in it needed to change for this finding.
* Fixes: none to the files of the set; only this provenance file was updated.
* Open discrepancies: the count table of `Revision/docs/PAIR_CREATION_PROOFS.md` section 9.1 (and so its
  test `test_report_count_table`) still quotes 57 checks for `ks-theory-python.json`, while the committed
  report has 58 since commit `972cad1`. This set's outputs are reproduced exactly; the document belongs to
  another set and was not changed here.

### 6.4 Resolution of the count-table discrepancy (2026-10-08)

* The open discrepancy of section 6.3 is resolved by commit `dc6904e` ("PAIR_CREATION_PROOFS: Kohn-Sham
  theory record now has 58 checks (was quoted as 57); run order in section 10"). Section 9.1 of
  `Revision/docs/PAIR_CREATION_PROOFS.md` now has the row
  ``| `Revision/kohn_sham/reports/ks-theory-python.json` | 58 | 58 | 0 |``, its section 10 runs
  `python Revision/field_equations_a4/python/check_ks_source_conditions.py` before
  `python Revision/kohn_sham/theory/check_ks_theory.py` (the companion reads the report of the first), and
  its PDF was rebuilt and re-registered.
* Checked on 2026-10-08: `python -B Revision/tests/test_pair_creation_proofs_publication.py -k
  test_report_count_table` printed `Ran 1 test` and `OK`.
* No file of this set changed; the committed reports are the ones verified in section 6.3.
* Open discrepancies: none.

### 6.5 Folders normalised (2026-10-08; first committed in the automatic snapshot `6779cd3`)

* Why: a review of the reproducibility of the Revision gate (2026-10-08; it fixed the same pattern in
  `Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls`) found that the script built its
  folders with `FileNameJoin[{..., ".."}]` without normalising them, so every path built from them kept the
  text `\..`; on Windows a path of 260 or more characters (MAX_PATH) is not found although the file exists, so
  the unnormalised `..` lowered the length of the clone folder at which a run fails.
* Change: lines 21 and 22 now read `$ks = ExpandFileName[FileNameJoin[{$here, ".."}]];` (followed on the same
  line by a comment) and `$rev = ExpandFileName[FileNameJoin[{$ks, ".."}]];`; no other line changed (still 463
  lines). New sha256 `b2b9d397848c6d7e1ea5796634cc1a08f3d1a8912b47117804e2520a868e9944`, 41431 bytes (before:
  `4ce71aaa2c8efd78c8e1508ab72a3223383e21900805c4a34e55a3d5f7deb50d`, 41295 bytes).
* Run: `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`, started detached from a `cmd.exe`
  batch file; Windows 11 Pro for Workstations 10.0.26300, WolframScript 1.14.0, Wolfram 15.0.1; run from the
  repository root `D:\Developer\github\Dirac_claude` (32 characters) in the working tree on top of commit
  `a8eb09d` or `ab84209` (both committed by others during this work; neither changed a file of this set, its
  inputs or its outputs), not in a fresh clone (other areas of the tree had uncommitted edits of other work,
  none in the folders of this set or in its inputs and outputs). Exit code 0, `46/46 checks passed; time 37.5
  s`, wall time 41 s (15:12:54 to 15:13:36). `git diff --quiet -- Revision/kohn_sham/ks-theory.json
  Revision/kohn_sham/reports` succeeded: `ks-theory.json` and `ks-theory-wolfram.json` are byte-identical to
  the committed ones (the sha256 of section 2.3). The companion `check_ks_theory.py` did not change and was
  not re-run.
* Fixes made: the normalisation above. Open discrepancies: none. Not done: a run of the changed script in a
  fresh clone, and a run from a long clone folder.
* Added later on 2026-10-08 (after an independent verification of this section): section 3.7 still quoted the
  missing-`gammas.json` line with the unnormalised path of the version before. With this version, in a scratch
  tree holding only the script and the package (no `Revision/algebra/gammas.json`), run from its root with
  `wolframscript -file Revision/kohn_sham/theory/verify_ks_theory.wls`, the only output was
  `ERROR  input file not found: <scratch root>\Revision\algebra\gammas.json`, error stream empty, exit code 1,
  5.6 s wall. Section 3.7 now quotes this form and keeps the old one as history; no script changed.
