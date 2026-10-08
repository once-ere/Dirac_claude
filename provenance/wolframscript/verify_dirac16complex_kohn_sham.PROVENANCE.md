# Provenance of the WolframScript set `verify_dirac16complex_kohn_sham` (old Stage 4: the exact Kohn-Sham theory)

This file is written for a student who has never used Wolfram software. It explains one program of this repository: what it computes, which files it reads and writes, how to install everything it needs and run it on Windows, macOS or Linux, what it prints, what it changes on your computer, and how it was tested on 2026-10-02 and tested again from fresh downloads on 2026-10-07. Everything you need is in this file; you do not have to open any other file to run the program.

Contents:

1. What the set is and what it computes
2. Its files
3. How to run it (complete instructions)
4. The expected output
5. Side effects
6. Verification record

## 1. What the set is and what it computes

### 1.1 The two files of the set

The set consists of two plain-text files written in the Wolfram Language (the language of Mathematica and of the free Wolfram Engine):

- `scripts/verify_dirac16complex_kohn_sham.wls` is the **script**: the program you start. A `.wls` file is a WolframScript script.
- `wolfram/Dirac16ComplexKohnSham.wl` is the **package**: a library of Wolfram Language functions. The script loads it and calls its main entry point `D16KSRun`, which runs every check. The package exports two more public functions, `D16KSGammas` (the eight 16 x 16 gamma matrices) and `D16KSBlockBasis` (the exact block basis, which exists only after `D16KSRun` has run, because the run computes it; called before, it returns an unevaluated symbol); this script does not call them, but the Mathematica notebook builder `scripts/build_dirac16complex_ks_mathematica_notebook.wls` does.

Together they are the exact (symbolic) part of "Stage 4" of the earlier `dirac16complex` work: the Kohn-Sham treatment (a density-functional, "DFT"-type approximation) of the interacting 16-component Dirac field `dirac16complex` in the **static** primordial gravitational field (the member of the primordial family in which the function a4 is a constant), written in the hidden-space coordinate y = ln(sin z)/(6H), which runs over (-infinity, 0].

### 1.2 What it computes, in plain words

The program does **not** compute decimal numbers. It does exact algebra: every quantity is a formula or a fraction, and every test asks whether some expression simplifies to exactly zero (no floating point is used). It tests 125 statements; each one is printed as a line `check_<name>=true` or `check_<name>=false`. The checks fall into these groups (the number of checks of each group is in brackets):

- **KS_fixture (4) and KS_internal (2).** The eight 16 x 16 gamma matrices are rebuilt from the split-octonion recipe and compared entry by entry with the committed matrices in `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`; the Clifford relations {gamma^a, gamma^b} = 2 eta^ab; the matrix C = gamma^0 gamma^1 gamma^2 gamma^3 and the matrix B = -i C gamma^4 (B Hermitian, B^2 = 1); a sanity test of the exact zero test itself; and, as the last check, that no internal error interrupted the run.
- **KS_geometry (18).** The metric ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4}(dx1^2 + dx2^2 + dx3^2) - e^{-2a4}(dx5^2 + dx6^2 + dx7^2)]; sqrt|g| = e^{6Hy}; exactly 18 nonzero Christoffel symbols; Ricci scalar R = -42 H^2; Einstein tensor G^mu_nu = diag(15, 15, 15, 15, 21, 15, 15, 15) H^2; the curvature invariants 84 H^4 and 252 H^4 are constants; the seven directions y, x1, x2, x3, x5, x6, x7 form a space of constant curvature -H^2; the source the Einstein equations require (energy density -21 H^2/kappa, pressures +15 H^2/kappa); the extrinsic curvature K^i_j = H; and, for the mirror (Z2) copy glued at y = 0, the Israel junction conditions with brane energy density +12 H/kappa and pressure -10 H/kappa.
- **KS_reduction (32).** With the ansatz Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} chi(y) the 16-component Dirac equation becomes an ordinary differential equation in y; an exact basis is constructed in which it splits into eight independent 2 x 2 blocks; the 2 x 2 matrices, the block types, the exact spectrum at k = 0 (the zero mode e^{My} and the levels plus or minus sqrt(M^2 + (n pi/L)^2)) and the first-order splitting of the zero mode for small k.
- **KS_boundary (18).** The current along y (matrix gamma^0 gamma^4) is conserved along y; the parity condition at the brane y = 0 and the bag condition at y = -L make it vanish, so the problem is self-adjoint; two mirror symmetries: P_A (a symmetry exactly when the mass function is odd, i.e. the mirror copy carries mass -m) and P_B (for an even mass function).
- **KS_exchange (20).** The Hartree-Fock energy of the contact interaction U = (lambda/2) S^2 (Wick's theorem checked on an exact 4-mode fermion Fock space); the filled-shell result E_x = -E_H/8; the exchange kernel; the uniform-gas exchange energy density e_x = -(lambda/32)(n^2 + S^2); zero-temperature closed forms; the mass dimension -6 of lambda in eight dimensions.
- **KS_functional (9).** The Mermin-Kohn-Sham free-energy functional: its stationarity conditions give the Kohn-Sham equation and Fermi-Dirac occupations; the double-counting form of the total energy; the Hellmann-Feynman identities (checked on a small model with symbolic entries).
- **KS_emt (22).** The energy-momentum tensor of one Kohn-Sham orbital, written with four densities of a block (number n, scalar s, k-current t, y-current c), for example rho = eps n - (Meff - m) s - v_v n.

It also prints 16 **measurements**: exact results such as the number of nonzero Christoffel symbols (18), the Kretschmann invariant (`84*H^4`) and the zero-mode splitting coefficient.

It writes two files (Section 2.3): a **report** with the 125 check results, the 16 measurements and the SHA-256 fingerprints of its three input files; and a **theory file** with every exact formula and matrix (numbers as fraction strings such as `"-1/2"`, complex numbers as pairs `["re", "im"]`), which other programs of the repository read.

**About charge conjugation.** This set neither defines nor uses a charge conjugation. The 16 x 16 matrix called C in it is the Dirac-conjugation matrix (Psibar = Psi^dagger C, C = gamma^0 gamma^1 gamma^2 gamma^3). The sentence "complex conjugation gives the same map (real structure)" in the theory file (key `reduction` -> `blockODE` -> `spectrumRelations`; check `KS_reduction_sigma3ConjugationFlipsK`) is a statement about the 2 x 2 coefficient matrix N of the reduced y-equation (the complex conjugate of N(k, j) equals N(-k, -j)); it is not a charge conjugation of the field. In this repository the charge conjugation of the field is a matrix operation (a 16 x 16 matrix combined with complex conjugation), not plain complex conjugation Psi -> Psi*.

### 1.3 Documents that cite its results

- `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (the earlier teaching textbook; its chapters are also stored one per file in `provenance/textbook/chapters/`, and its LaTeX version is `provenance/DIRAC16COMPLEX_TEXTBOOK.tex`): "How to read" (the claims table: 125 of 125 checks), Chapter 4 (the required source of the static field: `KS_geometry_ricciScalarMinus42H2`, `KS_geometry_einsteinMixedDiag`, `KS_geometry_requiredSource`), Chapter 9 (the static member, its constant curvature and the brane: `KS_geometry_*`, `geometry_israelSignConvention`), Chapter 13 (the Kohn-Sham theory: block basis, exchange, functional, energy-momentum tensor; keys of `kohn-sham-theory.json`), Chapter 15 (pairing theorems: the block basis of `kohn-sham-theory.json`, block index 4), Chapter 18 (open problems), Chapter 19 (reproducing everything: "125 of 125 checks true", the commands, 19 seconds), Chapter 20 (check index, abbreviation WK).
- `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md` (the Stage-4 document: its numbers are copied from `wolfram-kohn-sham-report.json` and `kohn-sham-theory.json`; the Israel sign convention; the block basis).
- `HANDOFF.md` (the Stage-4 row: exact theory, 125 of 125).

### 1.4 Programs that read its outputs or load its package

- `scripts/check_dirac16complex_kohn_sham_theory.py` (independent sympy check, 157 checks; compares with `kohn-sham-theory.json`).
- The Rust solver `studies/dirac16complex_kohn_sham` (`src/theory.rs` reads `kohn-sham-theory.json`) and its summary tool `studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py` (reads both outputs and compares recorded SHA-256 values).
- `scripts/check_dirac16complex_kohn_sham.py`, `scripts/check_dirac16complex_pairing.py`, `scripts/check_dirac16complex00.py` (read `kohn-sham-theory.json`).
- `wolfram/Dirac16ComplexPairing.wl` with `scripts/verify_dirac16complex_pairing.wls`, `wolfram/Dirac16ComplexMatterAntimatter.wl` with `scripts/verify_dirac16complex_matter_antimatter.wls` (read `kohn-sham-theory.json`), and `wolfram/Dirac16Complex00.wl` with `scripts/verify_dirac16complex00.wls` (loads the package and reads both outputs).
- `scripts/build_dirac16complex_ks_mathematica_notebook.wls` (loads the package to build `notebooks/Dirac16ComplexKohnSham.nb`) and `notebooks/build_dirac16complex_kohn_sham_notebook.py` (the Jupyter notebook builder; reads both outputs).
- The Stage-4 gate `scripts/verify_stage4_kohn_sham.ps1` / `scripts/verify_stage4_kohn_sham.sh` (its step `stage4-03-theory-wolfram` runs this script into `build/stage4/theory/` and compares both outputs byte for byte with the committed ones).
- The tests `tests/test_d16c_kohn_sham_gate.py`, `tests/test_d16c_kohn_sham_mathematica.py`, `tests/test_d16c_kohn_sham_theory.py`.
- `provenance/dirac_matrices/extract_repository_wolfram_gammas.wls` (loads the package to record its gamma matrices, among those of other programs, for the comparison in `provenance/dirac matrices.md`; present since 2026-10-07).

Several of these programs record the SHA-256 of `kohn-sham-theory.json`; that is why a run must reproduce it byte for byte (it does: Section 6).

The Jupyter notebook `notebooks/dirac16complex_kohn_sham.ipynb` (with its own provenance file `notebooks/dirac16complex_kohn_sham.PROVENANCE.md`, its checker `notebooks/check_dirac16complex_kohn_sham_notebook.py`) and the Mathematica notebook `notebooks/Dirac16ComplexKohnSham.nb` also show results of this set; the specification it was written to is `handoff/specs/STAGE4_SPEC.md`.

### 1.5 The Dirac matrices it uses

The eight 16 x 16 gamma (Dirac) matrices gamma^0, ..., gamma^7 that the package builds (in package lines 98 to 113, as the list `gamL`) and returns (function `D16KSGammas`, defined in package line 124) are **real**: every entry is -1, 0 or +1. They are the author's eight real Dirac matrices `T16A[0]`, ..., `T16A[7]` of the notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`, which are displayed and proved (real, Cl(4,4) anticommutation relations, Pin(4,4)) in `provenance/dirac matrices.md`. Two of the set's own checks concern them: `KS_fixture_gammasMatchCommittedFixture` (the rebuilt matrices equal, entry by entry, the committed matrices of `algebra-fixture.json`) and `KS_fixture_cliffordAndC` ({gamma^a, gamma^b} = 2 eta^ab times the 16 x 16 identity, eta = diag(+1, +1, +1, +1, -1, -1, -1, -1), and C = gamma^0 gamma^1 gamma^2 gamma^3). On 2026-10-07 an additional check, run outside the repository on the fresh download (Section 6.2), confirmed 11 of 11 statements: the package returns eight 16 x 16 matrices; their entries are in {-1, 0, 1}; each equals its complex conjugate (real); they equal entry by entry the author's `T16A[0..7]` stored in `provenance/dirac_matrices/author_notebook_T16.json` and the `gamma` matrices of `algebra-fixture.json`; they satisfy all 64 anticommutation relations; the author's metric `eta4488` is diag(+1, +1, +1, +1, -1, -1, -1, -1); the author's `sigma16` equals gamma^0 gamma^1 gamma^2 gamma^3 and the author's `T16A[8]` equals gamma^0 ... gamma^7; the 28 scaled commutators [gamma^a, gamma^b]/4 (a < b) are linearly independent (the 28 generators of spin(4,4), the Lie algebra of Pin(4,4)). Later the same day a rewritten check on another fresh download (Section 6.3; commit `b8a695d`, whose `author_notebook_T16.json` has SHA-256 `1ab8ef7589bbe72a5511942da871bb7f6d21b3dbb67cd5a60263f36d1682f9fb`) confirmed these eleven statements again and six more: the package's matrices C and B equal gamma^0 gamma^1 gamma^2 gamma^3 and -i C gamma^4; `D16KSBlockBasis[]` is an unevaluated symbol before `D16KSRun` has run (Section 1.1); after the run it is a 16 x 16 matrix, it is unitary, and its entries multiplied by 2 sqrt(2) are exactly -1, 0, +1, -i and +i (next paragraph). Result: 17 of 17 true.

The name `dirac16complex` refers to the **field**, not to the matrices: the field Psi has 16 complex components, and the set builds complex matrices from the real gamma matrices, for example B = -i C gamma^4 (purely imaginary; confirmed by the same additional check), the unitary block basis returned by `D16KSBlockBasis` (package line 285), whose entries are 0, +-1 and +-i divided by 2 sqrt(2) (the package's own description, package line 65; confirmed by the repeated check of Section 6.3: 2 sqrt(2) times the basis has exactly the entries -1, 0, +1, -i, +i, and the basis is unitary), and the factors e^{-i eps x4} e^{i k x1} of the ansatz.

## 2. Its files

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone` creates). "Lines" is the number of line-feed characters (what `wc -l` prints); all files use LF line endings.

### 2.1 Program files

| Role | Path | SHA-256 | Lines | Bytes |
|---|---|---|---|---|
| script (you run it) | `scripts/verify_dirac16complex_kohn_sham.wls` | `ed6dbaa5a52668f1bb448a84d6b5529902b08a8c5e3f7a7b5d2cffdd2fd7672f` | 72 | 4452 |
| package (loaded by the script) | `wolfram/Dirac16ComplexKohnSham.wl` | `5f8d4703ad848f2d2ba5d33497d402da791584fe6777d668f7c626e7de35c65b` | 845 | 84969 |

### 2.2 Inputs it reads

| Input | Path | SHA-256 | Lines | Bytes |
|---|---|---|---|---|
| exact gamma-matrix fixture (written earlier by `scripts/build_dirac16complex_fixture.py`) | `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 18440 | 213133 |

The script also reads its own two program files once more to record their SHA-256 in the outputs. It reads nothing else from the repository: on 2026-10-02 it was run in a folder that contained only these three files and produced byte-identical outputs (Section 6). Like every Wolfram kernel, it also reads the Wolfram system files and, if you have one, your personal kernel start-up file `Kernel/init.m` in your Wolfram user folder.

### 2.3 Outputs it writes

The script takes one optional argument, the path of the report. If you give no argument, the report path is `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json`. A relative path is taken relative to the **repository root** (not to the folder you are in); a path that starts with `/` or with a drive letter such as `C:` is used as it is. The folder of the report is created if it does not exist, together with every missing folder above it (for example both `build/` and `build/kohn-sham-check/` in a freshly downloaded repository). The script creates this folder before it loads the package, so the folder appears even when the run stops with an error. The theory file is always written next to the report, with the fixed name `kohn-sham-theory.json`.

| Output | Default path (committed in the repository) | SHA-256 of the committed file | Lines | Bytes |
|---|---|---|---|---|
| report | `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` | `9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978` | 154 | 7079 |
| theory file | `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` | `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` | 4537 | 72176 |

Both outputs are UTF-8 JSON with LF line endings and contain no date, no time and no folder name, so a correct run reproduces them byte for byte wherever you run it.

## 3. How to run it (complete instructions)

### 3.1 What you need

- A 64-bit computer with Windows 10 or 11, macOS, or Linux.
- At least 2 GB of free disk space for the repository, in addition to the space that the Wolfram installation of Section 3.4 needs (its installer tells you how much). The repository keeps growing: on 2026-10-07 (commit `b8a695d`) a fresh download transferred about 240 MB (Git reported `size-pack: 237.41 MiB`) and the downloaded folder took about 745 MB on disk (238 MB of them in its hidden `.git` folder), against about 130 MB and 520 MB on 2026-10-02.
- About 1 GB of free memory (the Wolfram kernel used at most about 300 MB in the test).
- An internet connection for the installation and for the download of the repository. The script itself does not use the network.
- Two programs: **Git** (to download the repository) and **WolframScript with a Wolfram kernel** (to run the script). You do not need Python, Rust or a Jupyter installation for this set.

### 3.2 Open a terminal

A terminal is a window in which you type commands. Type each command exactly as shown (one line at a time, unless a block is shown) and press Enter.

- **Windows:** click Start, type `PowerShell`, and open "Windows PowerShell" (or "PowerShell 7", or "Terminal"). These Windows commands were typed exactly as written, in both Windows PowerShell 5.1 and PowerShell 7.6 (Section 6): every command of Sections 3.5 to 3.9 and 5.6, the checks `git --version` (Section 3.3) and `wolframscript -version` (Section 3.4), and the commands of the three rows of Section 3.10 that begin with `Failed to open file at path`, `fatal: destination path` and `FATAL: module failed to load`. The installation and activation steps of Sections 3.3 and 3.4 (the installers, `winget`, `brew`, `apt` and `wolframscript -activate`) were **not** run, because the test machine already had Git and an activated Wolfram installation.
- **macOS:** open Finder, then Applications, then Utilities, then Terminal.
- **Linux:** open your distribution's terminal program (for example "Terminal" in Ubuntu).

The macOS and Linux commands below (from Section 3.5 on) are ordinary POSIX shell commands; they were tested in the Bash of Git for Windows on the verification machine (Section 6, runs 11, 15, 20, 21, 26, 27, 30 and 31), not on a Mac or on a Linux computer.

### 3.3 Install Git

- **Windows:** download the installer from https://git-scm.com/download/win, run it, and accept all default choices. Close the PowerShell window and open a new one.
- **macOS:** type `git --version`. If Git is missing, macOS offers to install the "command line developer tools"; click Install and wait, then type `git --version` again.
- **Linux:** on Debian or Ubuntu type `sudo apt install git`; on Fedora type `sudo dnf install git`.

Check: `git --version` prints a line such as `git version 2.51.2.windows.1`.

### 3.4 Install a Wolfram kernel and WolframScript, and activate it

You need either the free **Wolfram Engine for Developers** (option A) or **Mathematica** (option B). Both contain the Wolfram Language kernel that does the computation; WolframScript is the command-line program that starts the kernel and runs a script.

**Option A: Wolfram Engine for Developers (free).**

1. **Create a Wolfram ID.** A Wolfram ID is an e-mail address and a password registered with Wolfram Research. If you have none, create one at https://account.wolfram.com (the "Create one" link on the sign-in page).
2. **Get the free licence.** In a web browser open https://www.wolfram.com/engine/free-license/ and click the button "Get your license". Sign in with your Wolfram ID and accept the terms of use (read them first; the free licence is meant for developing software that is not yet in production). This step attaches a Wolfram Engine licence to your Wolfram ID. Without it, the activation of step 5 fails even with a correct Wolfram ID and password.
3. **Download and install the Wolfram Engine.** The page https://www.wolfram.com/engine/ offers a download button and, on 2026-10-02, also showed these one-line installation commands; use one route for your system:
   - **Windows:** either run the installer downloaded with the button (a `.exe` file) and accept the default choices, or type in PowerShell `winget install WolframEngine` (on 2026-10-02 `winget search WolframEngine` listed the package `WolframResearch.WolframEngine`, version 15.0.0). Either route installs the Wolfram Engine and WolframScript and makes the command `wolframscript` available. Afterwards close PowerShell and open a new PowerShell window.
   - **macOS:** either type in Terminal `brew install --cask wolfram-engine` (this needs the package manager Homebrew from https://brew.sh; on 2026-10-02 its page for this package said that it installs "Wolfram Engine" into the Applications folder together with the command `wolframscript`, and that it needs macOS 13 or later), or, if the download button gave you a `.dmg` file, open that file and drag the Wolfram Engine into the Applications folder, as its window shows. Afterwards open a new Terminal window.
   - **Linux (Debian, Ubuntu and their relatives):** type `cd /tmp && wget https://wolfr.am/wolfram-engine.deb && sudo apt install ./wolfram-engine.deb` (the command shown on the page; it downloads the package `wolfram-engine.deb` and installs it). The kernel is then installed under `/opt/Wolfram/WolframEngine/15.0/`. Afterwards open a new terminal window.
   - **Other Linux, or if the download button gave you a file whose name ends with `.sh`:** in the terminal go to the folder of the download (usually `cd ~/Downloads`) and run that file: `sudo bash WolframEngine_*.sh` (replace the name by the name of your file if it is different). Accept the default answers. Afterwards open a new terminal window.

   None of these installation routes was run on the verification machine, which already had Wolfram 15.0.1 installed; they are taken from the official pages as they were on 2026-10-02. The macOS and Linux steps in particular were **not** tested at all (Section 6 tested only Windows). If the page has changed, follow the instructions it shows for your system.
4. **Check that `wolframscript` is there.** Type `wolframscript -version`; it prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`. If the terminal answers that the command is not found (this can happen on macOS and with some installations), download WolframScript by itself from https://www.wolfram.com/wolframscript/ (choose your operating system), install it, open a new terminal window and type `wolframscript -version` again.
5. **Activate the engine once.** Type `wolframscript -activate` and, when asked, enter your Wolfram ID (the e-mail address) and your password. Activation needs the internet. This step was not re-run on the verification machine, whose Wolfram installation was already activated.

**Option B: Mathematica.** If Mathematica (version 13 or later is a safe choice; this set was tested only with version 15.0.1) is installed and activated on your computer, WolframScript normally comes with it. Type `wolframscript -version`; if the command is not found, install WolframScript by itself as in step 4 of option A. If Mathematica has never been activated, start Mathematica once and follow its activation dialog, or type `wolframscript -activate`.

### 3.5 Check that WolframScript works

Type these two commands (the single quotes are part of the commands; they are the same in PowerShell, macOS and Linux):

```
wolframscript -code '2+2'
wolframscript -code '$Version'
```

The first prints `4`. The second prints the version of your Wolfram kernel, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. The first command after an installation can take a little longer while the kernel starts for the first time.

### 3.6 Download the repository

In the terminal, go to the folder in which you want the repository (for example your home folder, which is where a new terminal starts), then type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The first command downloads the repository into a new folder `Dirac_claude` (about 240 MB on 2026-10-07, and growing; 8 to 97 seconds on the test machine, depending mostly on the speed of the internet connection; while it works it prints `Cloning into 'Dirac_claude'...` and progress lines). The second command enters that folder. This folder is the **repository root**: every command below must be typed there. (If the folder already exists from an earlier download, `git clone` refuses with `fatal: destination path 'Dirac_claude' already exists and is not an empty directory.`; then type `cd Dirac_claude` and `git pull` to update it, which prints `Already up to date.` when nothing has changed.)

### 3.7 Run the script

This is the command from the script's own header. It writes the two outputs to their committed places (Section 2.3), replacing the committed files with files that a correct run makes byte for byte identical.

**Windows (PowerShell):**

```
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
$LASTEXITCODE
```

**macOS and Linux (Terminal):**

```
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
echo $?
```

The first line runs the script and prints 155 lines (Section 4.1). How long it takes depends on how busy your computer is: on the test machine a run took 12.7 to 18.2 seconds on 2026-10-02 and 18.7 to 33.9 seconds on 2026-10-07, when all its processors were busy with other programs (Section 4.4). These are typical values, not limits: a slower run is not a sign of an error, and the progress lines (Section 4.1) show that the program is working. What decides success are the final lines (Section 3.9). The second line prints the exit code of the run, which must be `0`. Forward slashes `/` in the paths work on Windows too. Do not type `--` before the report path (see the problem table in Section 3.10).

The command `wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls` without the report path does exactly the same, because the path above is the default.

### 3.8 Optional: run it without touching the committed files

If you prefer not to rewrite the committed files, give a report path inside the folder `build/`, which Git ignores in this repository.

First find out whether the folder `build/` exists already (you need this for the clean-up at the end). In a freshly downloaded repository it does not exist; other programs of the repository may have created it.

- PowerShell: `Test-Path build` prints `False` when the folder does not exist and `True` when it does.
- macOS and Linux: `ls -d build` prints `build` when the folder exists, and an error message ending in `No such file or directory` when it does not.

Then run:

```
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls build/kohn-sham-check/wolfram-kohn-sham-report.json
```

(the same in PowerShell, macOS and Linux). The script creates the missing folders, that is `build/kohn-sham-check/` and, if it was missing, `build/` itself, and writes `wolfram-kohn-sham-report.json` and `kohn-sham-theory.json` there. Compare them with the committed files:

```
git diff --no-index --stat artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json build/kohn-sham-check/wolfram-kohn-sham-report.json
git diff --no-index --stat artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json build/kohn-sham-check/kohn-sham-theory.json
```

Each of these two commands prints **nothing** and ends with exit code 0 when the two files are identical. If they differ, it prints two lines and ends with exit code 1: first the file name (shortened with `...` and `{... => ...}`) with the number of changed lines and a row of `+` and `-` signs, for example `| 2 +-`, then a summary line such as ` 1 file changed, 1 insertion(+), 1 deletion(-)`.

Delete the scratch output afterwards:

- If `build/` did **not** exist before (`Test-Path build` printed `False`, or `ls -d build` printed an error), delete the whole folder: `Remove-Item -Recurse -Force build` (PowerShell) or `rm -rf build` (macOS, Linux). Afterwards `Test-Path build` prints `False` again (PowerShell), and `ls -d build` prints the `No such file or directory` error (macOS, Linux).
- If `build/` existed before, delete only the folder of this run: `Remove-Item -Recurse -Force build/kohn-sham-check` (PowerShell) or `rm -rf build/kohn-sham-check` (macOS, Linux).

If you delete only `build/kohn-sham-check` although `build/` did not exist before, an empty folder `build/` stays behind. It is harmless (Git ignores it, and an empty folder never appears in `git status`), and you can delete it with the first command.

### 3.9 Check the result

After the run of Section 3.7, check these four things:

1. The last lines printed include exactly `check_count=125` and `failed_check_count=0`, and no line contains `=false` or `CHECK FAILED`.
2. The exit code printed by `$LASTEXITCODE` (PowerShell) or `echo $?` (macOS, Linux) is `0`.
3. `git status --porcelain` prints **nothing**. This shows that the two rewritten files are byte for byte identical to the committed ones (Git compares the contents, not the dates).
4. The SHA-256 fingerprints of the two outputs are the ones in Section 2.3:
   - PowerShell: `Get-FileHash -Algorithm SHA256 artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json, artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json | Format-List Hash, Path` (PowerShell prints the fingerprints in capital letters, beginning `9F04BC10` and `5B150B36`).
   - macOS: `shasum -a 256 artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json`
   - Linux: `sha256sum artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json`

You can also count the passed checks inside the report. Each check is one line of the form `"KS_...":true,`:

- PowerShell: `(Select-String -SimpleMatch -Pattern '":true' -Path artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json).Count` prints `125`, and the same command with `'":false'` prints `0`.
- macOS and Linux: `grep -c '":true' artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` prints `125`, and `grep -c '":false' artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` prints `0`.

### 3.10 If it fails

| What you see | Cause | What to do |
|---|---|---|
| The terminal says it does not know the command `wolframscript`. Windows PowerShell 5.1 prints `wolframscript : The term 'wolframscript' is not recognized as the name of a cmdlet, ...`; PowerShell 7 prints `wolframscript: The term 'wolframscript' is not recognized as a name of a cmdlet, ...`; Linux with Bash prints `bash: wolframscript: command not found` (some distributions print only `wolframscript: command not found` or suggest packages); macOS, whose standard terminal shell is zsh, prints `zsh: command not found: wolframscript` (the PowerShell and Bash forms were seen on the test machine, Section 6.3; the zsh form is zsh's standard message and was not tested) | WolframScript is not installed, or the terminal was opened before the installation | Open a new terminal. If it still fails, install WolframScript by itself (Section 3.4, option A, step 4). |
| `wolframscript -activate` refuses your Wolfram ID and password, or says that no licence or no entitlement was found for it | Your Wolfram ID has no Wolfram Engine licence yet: the "Get your license" step was skipped | Do Section 3.4, option A, step 2: open https://www.wolfram.com/engine/free-license/, click "Get your license", sign in with the same Wolfram ID and accept the terms of use. Then type `wolframscript -activate` again. |
| WolframScript asks for a Wolfram ID and password, or reports that the engine is not activated or that no licence is available | The kernel was never activated, the activation expired, or too many Wolfram kernels are running at once | Type `wolframscript -activate` and enter your Wolfram ID and password (if this is refused, see the previous row). Close other Mathematica or Wolfram sessions and try again. |
| `Failed to open file at path: scripts/verify_dirac16complex_kohn_sham.wls` (and the exit code is **0**, although nothing ran) | The terminal is not in the repository root | Type `cd` followed by the path of the `Dirac_claude` folder and run again. WolframScript returns exit code 0 here, so always check the `check_count` lines, not only the exit code. |
| `fatal: destination path 'Dirac_claude' already exists and is not an empty directory` | The repository was downloaded before | Type `cd Dirac_claude` and `git pull` instead of cloning again. |
| `FATAL: module failed to load: ...` with `check_count=0` and `failed_check_count=1`, exit code 1 (when the package file is missing, the line `Get::noopen: Cannot open ...` comes first) | The package `wolfram/Dirac16ComplexKohnSham.wl` is missing or damaged | Check its SHA-256 (Section 2.1). Restore it with `git checkout -- wolfram/Dirac16ComplexKohnSham.wl`, or download the repository again. No report is written, but the folder of the report path has already been created and stays behind empty (for the default path it already exists; for a path under `build/`, delete it as in Section 3.8). |
| One or more lines `CHECK FAILED: <name>` and `check_<name>=false`, `failed_check_count` larger than 0, exit code 1 | An input file differs from the committed one, or your Wolfram version computes something differently | Do not edit the checks. Run `git status` to see whether an input was changed and compare the SHA-256 values of Sections 2.1 and 2.2. With unchanged inputs, note your Wolfram version (`wolframscript -code '$Version'`) and the failing check names; the test was made with version 15.0.1. |
| `INTERNAL ERROR: ...` and `check_KS_internal_noException=false` | An exact simplification did not reach the expected form (for example with a much older Wolfram version) | As in the previous row. |
| Error messages about `FileHash`, `RawJSON` or `ExportString` | A very old Wolfram version | Install a current Wolfram Engine (Section 3.4). |
| `git status --porcelain` lists `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` or `kohn-sham-theory.json` | The run produced different bytes | See which lines differ with `git diff artifacts/dirac16complex/kohn-sham/`. Restore the committed files with the command of Section 5.6. If the only differing lines are the three lines under `sourceSha256` (the fingerprints of the script, the package and the fixture) in each file, then those three files differ from the committed bytes, most often because they were given Windows line endings (CR LF), for example by an editor; `git status` then lists them as changed too. Restore them with `git checkout -- scripts/verify_dirac16complex_kohn_sham.wls wolfram/Dirac16ComplexKohnSham.wl artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` and run again (runs 30 and 31 of Section 6.3 show this case and its repair). |
| You typed `--` before the report path | The script's header warns that some WolframScript versions drop `--` and everything after it; the report would then go to the default path | Type the command without `--`. (With WolframScript 1.14.0 on the test machine the `--` arrived and the script removed it, so the report went to the given path.) |

## 4. The expected output

### 4.1 What is printed

The program prints exactly 155 lines (on Windows the lines end with CR LF). First come nine progress lines, each beginning with the time of day in the form `[hh:mm:ss]`; then the 125 check lines; then the 16 measurement lines; then five summary lines. Below is the complete output of the test run; the times of day are replaced by `[hh:mm:ss]`, the durations by `N`, and the folder of your repository by `<repository root>` (on Windows the printed paths use backslashes `\`). The duration `N` (the computation itself, without the start of the kernel) was 9 to 14 seconds on the test machine on 2026-10-02 and 12 to 25 seconds on 2026-10-07, when all its processors were busy with other programs; these are typical values, not limits (Section 4.4).

```
[hh:mm:ss] fixture
[hh:mm:ss] geometry (y chart, a4 constant)
[hh:mm:ss] KS_geometry
[hh:mm:ss] KS_reduction
[hh:mm:ss] KS_boundary
[hh:mm:ss] KS_exchange
[hh:mm:ss] KS_functional
[hh:mm:ss] KS_emt
[hh:mm:ss] done in N s
check_KS_fixture_gammasMatchCommittedFixture=true
check_KS_fixture_CAndChiralityMatch=true
check_KS_fixture_cliffordAndC=true
check_KS_fixture_Bproperties=true
check_KS_internal_zeroTestSanity=true
check_KS_geometry_sqrtDetG_W6=true
check_KS_geometry_signature44=true
check_KS_geometry_notebookChart=true
check_KS_geometry_christoffelCount18=true
check_KS_geometry_christoffelClosedForms=true
check_KS_geometry_ricciScalarMinus42H2=true
check_KS_geometry_einsteinMixedDiag=true
check_KS_geometry_ricciMixed=true
check_KS_geometry_kretschmannConstant=true
check_KS_geometry_constantCurvatureSevenSpace=true
check_KS_geometry_ricciSquareConstant=true
check_KS_geometry_requiredSource=true
check_KS_geometry_rhoRequiredNegative=true
check_KS_geometry_extrinsicCurvature=true
check_KS_geometry_israelJump=true
check_KS_geometry_israelStress=true
check_KS_geometry_braneEnergyPositive=true
check_KS_geometry_inducedMetricFlat=true
check_KS_reduction_vielbeinPostulate512=true
check_KS_reduction_omegaCount12=true
check_KS_reduction_OmegaClosedForms=true
check_KS_reduction_gammaSlashOmega3Hgamma0=true
check_KS_reduction_divergenceIdentity=true
check_KS_reduction_ansatzRemoves3H=true
check_KS_reduction_reducedEquationODEForm=true
check_KS_reduction_withoutW3the3HTermSurvives=true
check_KS_reduction_flatMeasure=true
check_KS_reduction_mirrorPatchSameForm=true
check_KS_reduction_a4IsMomentumRescaling=true
check_KS_reduction_JK1K2commute=true
check_KS_reduction_projectorsRank2=true
check_KS_reduction_basisUnitary=true
check_KS_reduction_basisIsJointEigenbasis=true
check_KS_reduction_fiveMatricesBlockDiagonal=true
check_KS_reduction_blocksA0A1A4=true
check_KS_reduction_blocksBC=true
check_KS_reduction_reconstructFromBlocks=true
check_KS_reduction_gamma2gamma3NotBlockDiagonal=true
check_KS_reduction_gamma8SwapsJ=true
check_KS_reduction_algebraDim8=true
check_KS_reduction_commutantDims=true
check_KS_reduction_blockTypes=true
check_KS_reduction_blockODEMatrix=true
check_KS_reduction_blockHamiltonianEquivalentToODE=true
check_KS_reduction_hMinusEqualsMinusHPlus=true
check_KS_reduction_sigma3ConjugationFlipsK=true
check_KS_reduction_rotationalSymmetry=true
check_KS_reduction_k0ZeroMode=true
check_KS_reduction_k0MassiveLevels=true
check_KS_reduction_zeroModeSplitting=true
check_KS_boundary_currentMatrix=true
check_KS_boundary_currentConservedAlongY=true
check_KS_boundary_hilbertNormNotConservedAlongY=true
check_KS_boundary_currentBlockForm=true
check_KS_boundary_parityProjectorsBlockForm=true
check_KS_boundary_parityKillsCurrent=true
check_KS_boundary_bagFamily=true
check_KS_boundary_bagThetaZeroIsEvenParity=true
check_KS_boundary_bagIn16=true
check_KS_boundary_currentKilledByAnticommutingProjector=true
check_KS_boundary_selfAdjointBoundaryTerm=true
check_KS_boundary_tipAsymptotics=true
check_KS_boundary_parityA_symmetryIffMassOdd=true
check_KS_boundary_parityB_symmetryForEvenMass=true
check_KS_boundary_parityB_couplesJBlocks=true
check_KS_boundary_parityOperatorsKillCurrent=true
check_KS_boundary_densityParities=true
check_KS_boundary_parityB_pairBlocks=true
check_KS_exchange_fockModelCAR=true
check_KS_exchange_fockVacuum=true
check_KS_exchange_wickTheoremHF=true
check_KS_exchange_modeHamiltonian=true
check_KS_exchange_projectorRank8=true
check_KS_exchange_filledShellScalarDensity=true
check_KS_exchange_kernelPlusPlus=true
check_KS_exchange_kernelPlusMinus=true
check_KS_exchange_filledShellOneEighth=true
check_KS_exchange_angularAverageOfPdotQVanishes=true
check_KS_exchange_blockFormOfFockTerm=true
check_KS_exchange_uniformGasClosedForm=true
check_KS_exchange_antiparticleConvention=true
check_KS_exchange_T0_density=true
check_KS_exchange_T0_scalarDensity=true
check_KS_exchange_T0_kineticEnergyDensity=true
check_KS_exchange_T0_dSdn=true
check_KS_exchange_T0_vxTotalDerivative=true
check_KS_exchange_restGasLimit=true
check_KS_exchange_couplingDimension=true
check_KS_functional_stationarityGivesKSEquation=true
check_KS_functional_stationarityConjugate=true
check_KS_functional_fermiDiracOccupations=true
check_KS_functional_totalEnergyDoubleCounting=true
check_KS_functional_hellmannFeynmanLambda=true
check_KS_functional_hellmannFeynmanTemperature=true
check_KS_functional_hellmannFeynmanMass=true
check_KS_functional_merminStructure=true
check_KS_functional_variantV=true
check_KS_emt_staticAnticommutators=true
check_KS_emt_phasesCancel=true
check_KS_emt_bilinearExtractionExact=true
check_KS_emt_blockBasisOrthogonal=true
check_KS_emt_basis32TraceOrthogonal=true
check_KS_emt_offBlockComponentsVanishPerOrbital=true
check_KS_emt_diagonalAndY1Y4X1ComponentsBlockDiagonal=true
check_KS_emt_diagonalComponentsPhysicalDensitiesOnly=true
check_KS_emt_rho=true
check_KS_emt_py=true
check_KS_emt_p1=true
check_KS_emt_p2p3=true
check_KS_emt_pt=true
check_KS_emt_Ty4ProportionalToCurrent=true
check_KS_emt_Ty1ProportionalToCurrent=true
check_KS_emt_T41form=true
check_KS_emt_T41cancelsOverShell=true
check_KS_emt_symmetric=true
check_KS_emt_trace=true
check_KS_emt_onShellLagrangian=true
check_KS_emt_restStateDustExplicit=true
check_KS_emt_densityParityTable=true
check_KS_internal_noException=true
measurement_geometry_christoffelNonzeroCount=18
measurement_geometry_kretschmann=84*H^4
measurement_specDiscrepancy_pReqSign=STAGE4_SPEC section 1 writes p_req = -15H^2/kappa; the exact mixed components give T^i_i = G^i_i/kappa = +15H^2/kappa for all seven transverse directions (y, x1, x2, x3, x5, x6, x7) and rho_req = -T^4_4 = -21H^2/kappa < 0.
measurement_geometry_israelSignConvention=[K_ij] - h_ij [K] = -kappa S_ij with [X] = X(0+) - X(0-), n = +partial_y pointing from y<0 to y>0, K_ij = h_i^mu h_j^nu nabla_mu n_nu = (1/2) partial_y g_ij; with W = e^{-H|y|} on both sides: K^i_j(0-) = +H, K^i_j(0+) = -H on the six warped directions, 0 on x4; [K] = -12H; S^i_j = -(10,10,10,12,10,10,10) H/kappa on (x1,x2,x3,x4,x5,x6,x7); rho_brane = -S^4_4 = +12H/kappa, p_brane = -10H/kappa (the same convention gives the Randall-Sundrum brane a positive tension 6k/kappa).
measurement_reduction_omegaNonzeroCount=12
measurement_reduction_algebraDim_A0A1A4=8
measurement_reduction_commutantDim_A0A1A4=32
measurement_reduction_commutantDim_A0A1A4BC=16
measurement_reduction_inequivalentBlockTypes_yEquation=2
measurement_reduction_inequivalentBlockTypes_withBandC=4
measurement_reduction_zeroModeSplittingCoefficient=(-2*(-1 + E^(LL*(H - 2*M)))*M)/(E^a4c*(-1 + E^(-2*LL*M))*(H - 2*M))
measurement_exchange_filledShellRatio=1/8
measurement_emt_anticommutatorNonzeroPairs={{1, 4}, {2, 4}, {3, 4}, {4, 5}, {4, 6}, {4, 7}}
measurement_emt_Ty4_coefficientOfCurrent=(-2*eps + vv[y])/2
measurement_emt_Ty1_coefficientOfCurrent=kk
measurement_emt_T41_coefficients_n_s_t_js={kk/2, 0, (E^(a4c + H*y)*eps)/2, (E^(a4c + H*y)*H)/4}
check_count=125
failed_check_count=0
elapsed_seconds=N
report=<repository root>/artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
theory=<repository root>/artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json
```

The final verdict lines are

```
check_count=125
failed_check_count=0
```

### 4.2 Exit code

`0` when every check is true (the case above). The script exits with `1` if any check is false, if the package cannot be loaded, or if the package does not return its results. (Exception: when WolframScript cannot find the script file at all, it prints `Failed to open file at path: ...` and still returns `0`; see Section 3.10.)

### 4.3 Files written, and how to check them

- `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` (or the path you gave): 154 lines, 7079 bytes, SHA-256 `9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978`. It has the keys `schemaVersion` (1), `producer`, `checks` (125 entries, all `true`), `measurements` (16 entries) and `sourceSha256` (the SHA-256 of the script, the package and the fixture, exactly the values of Sections 2.1 and 2.2). The quickest checks are those of Section 3.9.
- `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` (next to the report): 4537 lines, 72176 bytes, SHA-256 `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a`. Its top-level keys, in this order, are `schemaVersion`, `producer`, `description`, `sourceSha256`, `conventions`, `geometry`, `reduction`, `boundary`, `exchange`, `functional`, `emt`; `reduction` -> `blockDiagonalisation` -> `blocks` lists the eight 2 x 2 blocks.

Nothing else is written by the script, apart from the missing folders of the report path that it creates (Section 5.1).

### 4.4 Run time

The run time depends on how busy the computer is, so the figures below are typical values, not limits: a slower run is not a sign of an error. On the test machine (24 logical processors, Windows 11, Wolfram 15.0.1) one run took 12.7 to 33.9 seconds from the start of `wolframscript` to its end (measured with a stopwatch around the command); the computation itself (the `elapsed_seconds` line) took 9 to 25 seconds and the rest was the start of the kernel. Other programs were running on the same machine at the same time, which explains the spread:

- 2026-10-02 (Section 6.1): 12.7 to 18.2 seconds (`elapsed_seconds` 9 to 14).
- 2026-10-07, second verification (Section 6.2, about 28 Wolfram processes of other programs running): 18.9 to 21.8 seconds (`elapsed_seconds` 12 to 16).
- 2026-10-07, the independent review of this file (the same load): 20.7 to 24.5 seconds (`elapsed_seconds` 15 to 18) for the commands of Sections 3.7 and 3.8, and `elapsed_seconds=21` for a run in a folder holding only the three files of Section 2.
- 2026-10-07, third verification (Section 6.3, processor load 100 %, 14 to 18 Wolfram kernels of other programs running): 18.7 to 33.9 seconds (`elapsed_seconds` 14 to 25).

The times of day of the progress lines show where the time goes. In run 1 (Section 6.1) the largest parts were KS_reduction (about 3 seconds) and KS_geometry, KS_exchange and KS_emt (about 2 seconds each); in run 24 (Section 6.3, under full load) KS_geometry and KS_reduction took about 8 seconds each, KS_exchange about 6 seconds and KS_emt about 3 seconds. The Wolfram kernel process needed at most 296 MB of memory (peak working set: 296 MB in runs 1 and 2, 295.7 and 295.8 MB in runs 18 and 19, 289.5 and 287.6 MB in runs 24 and 25), WolframScript itself 16 to 17 MB.

## 5. Side effects

### 5.1 Files in the repository

- With the command of Section 3.7 (or with no argument) the run **overwrites** the two committed files `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` and `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json`. A correct run writes exactly the same bytes, so only their modification dates change and `git status --porcelain` stays empty.
- With a report path elsewhere (Section 3.8) the run creates the folder of the report and every missing folder above it, and writes the two files there; the committed files are not touched. In a freshly downloaded repository the path `build/kohn-sham-check/wolfram-kohn-sham-report.json` therefore creates **two** folders, `build/` and `build/kohn-sham-check/` (`build/` is not part of the repository). Everything under `build/` is ignored by Git (`git status --porcelain` prints nothing; `git status --porcelain --ignored` prints `!! build/` while `build/` holds files). Deleting only `build/kohn-sham-check/` afterwards leaves an empty `build/`, which no `git status` command shows; Section 5.6 says how to remove it.
- The folders are created **before** the package is loaded (the script creates the folder of the report in its line 23 and loads the package in line 26). A run that stops with `FATAL: module failed to load` therefore still leaves the new, empty folder(s) behind.
- A run that is interrupted before its end does not touch the two outputs: the script writes them only after all checks are done (script lines 61 and 62). In run 29 (Section 6.3), stopped after 12 seconds, both committed outputs kept their bytes and their modification times and `git status --porcelain --ignored` printed nothing. As with `FATAL`, the folder of the report path has already been created at that point, so with a path under `build/` an interrupted run can leave an empty folder there.
- No other file or folder of the repository is created, changed or deleted.

### 5.2 Temporary files

The script itself creates no temporary files, but WolframScript does. On Windows this was measured in Section 6.3:

- While a run is going on, WolframScript keeps a copy of everything the program has printed so far in a file whose name is `tmp_` followed by ten random letters and digits (for example `tmp_8VLVIfZ2UC`), in the folder `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (in PowerShell the same folder is `$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary`). The file is locked while the run lasts, and WolframScript deletes it when the run ends normally (runs 24 and 25 left no such file behind).
- If a run is **interrupted** before its end, the file stays behind. In run 29 the `wolframscript` process was ended by force after 12 seconds; afterwards the folder held the file `tmp_8VLVIfZ2UC` (113 bytes: the four progress lines printed before the interruption). Whether stopping a run with Ctrl+C leaves such a file too was not tested. A left-over file is small and harmless; you may delete it by hand (for example in File Explorer) when no Wolfram program is running. Files of Wolfram programs that are still running are locked and cannot be deleted. The folder may also hold left-over files of other Wolfram programs.
- WolframScript also updates its settings file (`%APPDATA%\Wolfram\WolframScript\WolframScript.conf`), and the kernel touches a lock file of its package manager (`%APPDATA%\Wolfram\Paclets\Temporary\pacletSiteData_15.lock`), which exists while a kernel runs. These two were seen to change during the test runs while other Wolfram programs were also running, so they cannot be attributed to this script with certainty.

On macOS and Linux WolframScript keeps its working files in folders of its own in your user account; this was not tested. None of these files is in the repository.

### 5.3 Processes

`wolframscript` starts two Wolfram processes, one after the other (on Windows with version 15.0.1 both appear in the Task Manager as `wolfram.exe`; on other systems or versions they may be called `WolframKernel`): first a short-lived one that only queries the licence (command-line options `-wlbanner -licenseinfo`, peak memory 16 to 25 MB), then the kernel that runs the script (peak memory about 290 MB; Section 4.4). The script starts no parallel sub-kernels. The kernel ends when the script ends (the script's last command is `Exit`); when the `wolframscript` process was ended by force (run 29 of Section 6.3), both `wolfram.exe` processes were gone 3 seconds later. A running kernel counts against the number of kernels your licence allows.

### 5.4 Network

The script makes no network access: it reads three local files and writes two. The Wolfram system itself may contact Wolfram servers, for example for licence activation or for updates of its own components; the script does not need this.

### 5.5 Downstream programs

The theory file is read by the programs listed in Section 1.4, several of which record its SHA-256. Because a correct run reproduces it byte for byte, rerunning the script does not disturb them. If a run ever produced different bytes, restore the committed files (Section 5.6) before running any of those programs.

### 5.6 How to restore the committed state

In the repository root (the same command in PowerShell, macOS and Linux):

```
git checkout -- artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json
```

and, if you used Section 3.8 (or a run stopped with `FATAL` while writing under `build/`), delete the scratch output:

- if `build/` did not exist before the run (as in a freshly downloaded repository): `Remove-Item -Recurse -Force build` (PowerShell) or `rm -rf build` (macOS, Linux);
- if `build/` existed before and holds files of other programs: `Remove-Item -Recurse -Force build/kohn-sham-check` (PowerShell) or `rm -rf build/kohn-sham-check` (macOS, Linux).

Check: `git status --porcelain --ignored` prints nothing, and in a freshly downloaded repository `Test-Path build` prints `False` (PowerShell) or `ls -d build` prints a `No such file or directory` error (macOS, Linux). Only the second check shows that no empty `build/` folder is left, because Git never lists empty folders. After an interrupted run you may also delete the left-over `tmp_` file of Section 5.2; it is outside the repository and Git does not see it.

## 6. Verification record

The set was verified three times: first on 2026-10-02 (Section 6.1, runs 1 to 17), then again on 2026-10-07 from a new fresh download after the work was interrupted and resumed (Section 6.2, runs 18 to 23), and once more on 2026-10-07 from two further fresh downloads after an independent review of this file (Section 6.3, runs 24 to 31). All three verifications gave the same result: the set executes correctly and reproduces both committed outputs byte for byte.

### 6.1 First verification (2026-10-02)

- **Date:** 2026-10-02.
- **Commits verified:** `45d47343ae480df46e06689ed822b8f9a88a8030` (runs 1 to 9) and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (runs 10 to 17), each equal to the remote `main` of https://github.com/once-ere/Dirac_claude.git when its clone was made. Between the two commits the script, the package, the fixture and the two committed outputs did not change (`git diff --stat` between them over these five files is empty).
- **Fresh clones:** five clones made with `git clone https://github.com/once-ere/Dirac_claude.git` into empty scratch folders: two for runs 1 to 12 (the second one made by following Sections 3.3, 3.5 to 3.9, 5.6 and the wrong-folder row of 3.10 literally in Windows PowerShell 5.1), and three for the re-verification after an independent review of this file (runs 13 to 17; the third made in Git Bash with the extra option `-q`, which only hides the progress lines; the fourth and fifth made by typing Section 3.6 as written, in Windows PowerShell 5.1 and in PowerShell 7.6). No uncommitted file was copied into any clone (the script, the package, the fixture and the two committed outputs are all committed, and their SHA-256 values in every clone are the ones of Section 2).
- **Environment:** Windows 11 Pro for Workstations 10.0.26200; Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory; WolframScript 1.14.0; Wolfram `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, Professional licence; PowerShell 7.6.6 and Windows PowerShell 5.1.26100; Git for Windows 2.51.2 with its Bash.

| Run | Shell and command (from the repository root of the fresh clone) | Exit code | Wall time | `elapsed_seconds` | Checks | Outputs vs committed |
|---|---|---|---|---|---|---|
| 1 | PowerShell 7: the command of Section 3.7 | 0 | 12.7 s | 9 | 125 true, 0 false | both byte-identical |
| 2 | PowerShell 7: the command of Section 3.7, again in the same clone | 0 | 13.0 s | 10 | 125 true, 0 false | both byte-identical; also byte-identical to run 1 |
| 3 | Git Bash: the command without the report path (default path) | 0 | 13.5 s | 10 | 125 true, 0 false | both byte-identical |
| 4 | Git Bash: the command of Section 3.8 (`build/kohn-sham-check/`) | 0 | 14.9 s | 11 | 125 true, 0 false | both byte-identical (`git diff --no-index` empty) |
| 5 | Git Bash: with `--` before a `build/` report path | 0 | not timed | 9 | 125 true, 0 false | report went to the given path: `--` arrived and the script removed it |
| 6 | PowerShell 7: with `--` before a `build/` report path | 0 | not timed | 10 | 125 true, 0 false | as run 5 |
| 7 | Git Bash, started in `scripts/` instead of the root | 0 | - | - | none | `Failed to open file at path: scripts/verify_dirac16complex_kohn_sham.wls`; nothing written |
| 8 | Git Bash: one entry of a gamma matrix in the fixture of the scratch clone changed on purpose, report into `build/` | 1 | not timed | 10 | 124 true, 1 false (`KS_fixture_gammasMatchCommittedFixture`, with the line `CHECK FAILED: KS_fixture_gammasMatchCommittedFixture`) | shows that a failure is detected and gives exit code 1; the fixture was restored afterwards (SHA-256 checked) |
| 9 | Git Bash: a folder whose path contains spaces and that holds only the script, the package and the fixture | 0 | not timed | 12 | 125 true, 0 false | both byte-identical (the folder of the report was created) |
| 10 | Windows PowerShell 5.1, second fresh clone: Sections 3.5, 3.6, 3.7, 3.9 (all four checks and both counts), 3.8 (both `git diff --no-index --stat` printed nothing, exit code 0), 5.6 and the wrong-folder row of 3.10, typed exactly as written | 0 | 18.2 s (3.7) | 14 (3.7), 14 (3.8) | 125 true, 0 false (both runs) | both byte-identical in both runs; `git status --porcelain` empty; wrong folder: `Failed to open file at path: ...`, exit code 0. The clean-up then written in 5.6 (delete only `build/kohn-sham-check`) left an empty `build/` folder, which Git does not list; this was found in run 13 and the clean-up was corrected |
| 11 | Git Bash, second fresh clone: the macOS and Linux commands of Sections 3.7 and 3.9 (`echo $?`, `sha256sum`, `grep -c`) | 0 | 15.5 s | 11 | 125 true, 0 false (`grep -c` printed 125 and 0) | both byte-identical; `git status --porcelain` empty |
| 12 | PowerShell 7.6, second fresh clone: Sections 3.5, 3.8 (with both `git diff --no-index --stat`, which printed nothing, exit code 0), 3.9 (`Get-FileHash`, both `Select-String` counts) and 5.6, typed exactly as written | 0 | 13.9 s | 11 | 125 true, 0 false | both byte-identical; `git status --porcelain --ignored` empty after 5.6, but, as in run 10, an empty `build/` folder remained (Git does not list it) |
| 13 | Windows PowerShell 5.1.26100.9444, third fresh clone: Section 3.8 as it was written before the review, ending with `Remove-Item -Recurse -Force build/kohn-sham-check` | 0 | 13.2 s | 10 | 125 true, 0 false | both byte-identical (both `git diff --no-index --stat` printed nothing, exit code 0). A copy of the report with one `true` changed to `false` gave the two lines ` .../kohn-sham-check/modified.json \| 2 +-` and ` 1 file changed, 1 insertion(+), 1 deletion(-)`, exit code 1 (the wording of 3.8 was corrected). After the old clean-up `Test-Path build` printed `True` (an empty folder) while `git status --porcelain --ignored` printed nothing; `Remove-Item -Recurse -Force build` then gave `False` |
| 14 | Git Bash, third fresh clone: the package moved out of the clone, report path `build/fataltest/wolfram-kohn-sham-report.json` | 1 | - | - | `check_count=0`, `failed_check_count=1` | printed `Get::noopen: Cannot open ...` and `FATAL: module failed to load: ...`; no report written, but the empty folders `build/` and `build/fataltest/` had been created; package moved back (SHA-256 `5f8d4703...` checked) and `build/` deleted |
| 15 | Git Bash, third fresh clone: the commands of Section 3.5 (`4` and the version line) and the macOS and Linux commands of the corrected Sections 3.8 (`ls -d build` before and after, `rm -rf build`), 3.7 (`echo $?`), 3.9 (`sha256sum`, `grep -c`) and 5.6 | 0 | 13 s (3.8), 13 s (3.7) | 9 (3.8), 10 (3.7) | 125 true, 0 false (both runs; `grep -c` printed 125 and 0) | both byte-identical in both runs; `ls -d build` printed `ls: cannot access 'build': No such file or directory` before 3.8, after `rm -rf build` and after 5.6; `git status --porcelain --ignored` printed `!! build/` while the folder held files and nothing after 5.6; the modified-copy test of run 13 repeated with the same two-line output and exit code 1 |
| 16 | Windows PowerShell 5.1.26100.9444, fourth fresh clone, the corrected file typed as written: `git --version` (3.3), `wolframscript -version` (3.4, printed `WolframScript 1.14.0 for Microsoft Windows (64-bit)`), 3.5 (`4` and the version line), 3.6 (clone 8.4 s), the `fatal: destination path` row (a second `git clone` printed that message with exit code 128; `git pull` printed `Already up to date.`), 3.7, 3.9, 3.8 with `build/` absent before (`Test-Path build` `False`, then `Remove-Item -Recurse -Force build`, then `False`), 5.6, 3.8 with `build/` existing before (only `build/kohn-sham-check` deleted, another file in `build/` kept), the wrong-folder row and the `FATAL` row (package deleted, then restored with `git checkout -- wolfram/Dirac16ComplexKohnSham.wl`) | 0 (3.7, 3.8); 0 (wrong folder); 1 (FATAL) | 12.9 s (3.7), 13.2 s (3.8) | 9 (3.7), 9 (3.8) | 125 true, 0 false (all three full runs; 155 printed lines, no `=false`, no `CHECK FAILED`; `Select-String` counts 125 and 0) | both byte-identical in every full run (`git status --porcelain` empty, `Get-FileHash` `9F04BC10...` and `5B150B36...`, both `git diff --no-index --stat` empty with exit code 0); FATAL: `Get::noopen` and `FATAL` lines, `check_count=0`, `failed_check_count=1`, an empty `build/kohn-sham-check/` left behind, package restored with SHA-256 `5F8D4703...`; at the end `git status --porcelain --ignored` printed nothing and `Test-Path build` printed `False` |
| 17 | PowerShell 7.6.6, fifth fresh clone: exactly the sequence of run 16 (both ran at the same time) | as run 16 | 13.0 s (3.7), 13.0 s (3.8) | 9 (3.7), 9 (3.8) | as run 16 | as run 16 (clone 10.0 s) |

- **Byte identity:** in runs 1, 2, 3, 4, 9, 10 (both runs), 11, 12, 13, 15 (both runs), 16 (all three full runs) and 17 (all three full runs) both outputs had exactly the SHA-256 values of Section 2.3; runs 1 and 2 were also compared with each other byte by byte (`cmp`): identical. After the runs in a clone, `git status --porcelain` showed nothing; with `--ignored` it showed only the ignored `build/` folder of runs 4 to 6 (removed before run 8 and again after it) and, in runs 15 to 17, `!! build/` while the scratch outputs were there and nothing after the corrected clean-up.
- **Printed output:** apart from the times of day, the durations and the paths, the printed output of runs 1 and 2 was identical line by line (155 lines, as in Section 4.1).
- **Peak memory:** kernel `wolfram.exe` 296 MB in runs 1 and 2; `wolframscript.exe` 16 to 17 MB.
- **Fixes made:** none to the set. The set executed correctly as committed; no file of the set was changed. This provenance file itself was corrected on 2026-10-02 after an independent review, and the corrected instructions were re-tested in runs 15 to 17: (1) Sections 2.3, 3.8, 4.3, 5.1, 5.6 and the `FATAL` row of 3.10 now say that the run creates every missing folder of the report path (including `build/` itself in a fresh clone), even when it stops with `FATAL`, and the clean-up deletes the whole `build/` folder when it did not exist before (the earlier clean-up left an empty `build/`); (2) Section 3.4 gained the separate "Get your license" step and a 3.10 row for an activation without a licence; (3) Section 3.4 now gives the installation routes shown on the official page on 2026-10-02 (`winget install WolframEngine`, `brew install --cask wolfram-engine`, the `.deb` package for Debian and Ubuntu) and says that the macOS and Linux installation steps were not tested; (4) Section 3.2 now names exactly which commands were tested; (5) Section 3.8 now describes the two-line output and exit code 1 of `git diff --no-index --stat` for differing files; (6) Section 1.1 now names all three public functions of the package.
- **Open discrepancies:** none. Three observations: (a) the script header's warning that WolframScript 1.14 drops `--` and everything after it was not reproduced on this machine (runs 5 and 6); the script handles both cases, and the instructions above do not use `--`; (b) WolframScript returns exit code 0 when it cannot open the script file (run 7), so a successful run must be recognised by the line `failed_check_count=0` together with `check_count=125`, not by the exit code alone; (c) the script creates the folder of the report (script line 23) before it loads the package (line 26), so a run that stops with `FATAL` leaves an empty folder behind (runs 14, 16, 17). This was documented (Sections 3.10 and 5.1), not changed: changing the script would change its SHA-256, which both committed outputs record under `sourceSha256`, and therefore the bytes of `kohn-sham-theory.json`, whose SHA-256 other programs of the repository record (Section 1.4).

### 6.2 Second verification (2026-10-07, from a new fresh download)

- **Date:** 2026-10-07.
- **Commit verified:** `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, equal to the remote `main` of https://github.com/once-ere/Dirac_claude.git when the clone was made. Between `45d47343ae480df46e06689ed822b8f9a88a8030` (Section 6.1) and this commit the script, the package, the fixture and the two committed outputs did not change (`git diff --stat` over these five files is empty), and their SHA-256 values, line counts and byte counts in the clone are exactly those of Sections 2.1 to 2.3.
- **Fresh clone:** one clone made with `git clone -q https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder outside the working copy (31 s). No uncommitted file was copied into it: every file the set reads or writes is committed. Before the first run `git status --porcelain --ignored` printed nothing and `build/` did not exist.
- **Environment:** Windows 11 Pro for Workstations 10.0.26300 (version 26H2, build 26300.9457); Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory; WolframScript 1.14.0; Wolfram `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, Professional licence; PowerShell 7.6.6 and Windows PowerShell 5.1.26100.9444; Git for Windows 2.51.2 with its Bash. About 28 Wolfram processes of other programs were running at the same time.

| Run | Shell and command (from the repository root of the fresh clone) | Exit code | Wall time | `elapsed_seconds` | Checks | Outputs vs committed |
|---|---|---|---|---|---|---|
| 18 | PowerShell 7.6.6: the command of Section 3.7, started with `Start-Process` (output to a file) while the peak memory of WolframScript and of its kernel was sampled every 0.2 s | 0 | 21.84 s | 16 | 125 true, 0 false (155 printed lines, no `=false`, no `CHECK FAILED`, empty error stream) | both overwritten (new modification times) and byte-identical (`sha256sum` `9f04bc10...` and `5b150b36...`; `cmp` against `git show HEAD:<file>` identical); `git status --porcelain --ignored` empty |
| 19 | PowerShell 7.6.6: the same command again in the same clone, measured the same way | 0 | 18.91 s | 15 | 125 true, 0 false | both byte-identical to the committed files and, by `cmp`, to the outputs of run 18 (saved outside the clone after run 18); `git status --porcelain --ignored` empty; printed output identical to run 18 line by line apart from the times of day and the durations |
| 20 | Git Bash: the macOS and Linux commands of Sections 3.7 (`echo $?`) and 3.9 (`sha256sum`, `grep -c`) | 0 | 21.22 s | 15 | 125 true, 0 false (`grep -c` printed 125 and 0) | both byte-identical; `git status --porcelain` empty; the saved output had 155 lines ending in CR LF |
| 21 | Git Bash: Section 3.8 (`ls -d build` printed the `No such file or directory` error before; report path `build/kohn-sham-check/wolfram-kohn-sham-report.json`; `rm -rf build`) | 0 | 20.32 s | 15 | 125 true, 0 false | both `git diff --no-index --stat` printed nothing, exit code 0; the run created `build/` and `build/kohn-sham-check/` holding the two files; `git status --porcelain` empty, `--ignored` printed `!! build/`; after `rm -rf build` `ls -d build` printed the error again and `git status --porcelain --ignored` printed nothing |
| 22 | Windows PowerShell 5.1.26100.9444: Sections 3.7 (`$LASTEXITCODE`) and 3.9 (`git status --porcelain`, `Get-FileHash`, both `Select-String` counts) as written, then the wrong-folder row of 3.10 (the command typed in `scripts/`) | 0; 0 (wrong folder) | 19.82 s | 15 | 125 true, 0 false (155 lines, no `=false`, no `CHECK FAILED`; `Select-String` counts 125 and 0) | both byte-identical (`Get-FileHash` `9F04BC10...` and `5B150B36...`; `git status --porcelain` empty); wrong folder: `Failed to open file at path: scripts/verify_dirac16complex_kohn_sham.wls`, exit code 0, nothing written |
| 23 | Git Bash: with `--` before the report path `build/dashtest/wolfram-kohn-sham-report.json` | 0 | not timed | 12 | 125 true, 0 false | the report went to the given path (the `--` arrived and the script removed it); both files byte-identical to the committed ones; `build/` deleted afterwards and `git status --porcelain --ignored` empty |

- **Byte identity:** in runs 18 to 23 both outputs had exactly the SHA-256 values of Section 2.3 (`9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978` for the report, `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` for the theory file); the outputs of the two runs 18 and 19 of the header command were identical to each other byte by byte (`cmp`).
- **Files created or overwritten:** runs 18, 19, 20 and 22 overwrote the two committed outputs with identical bytes (only their modification times changed); runs 21 and 23 created `build/` with one sub-folder holding the two outputs, deleted afterwards. No other file of the clone was created or changed (`git status --porcelain --ignored` empty at the end). The script wrote no temporary files of its own; WolframScript's own working folders outside the repository (Section 5.2) were in use by the other Wolfram programs running at the same time, so changes there cannot be attributed to these runs.
- **Peak memory:** kernel `wolfram.exe` 295.7 MB (run 18) and 295.8 MB (run 19); `wolframscript.exe` 16.5 and 16.6 MB.
- **The Dirac matrices (Section 1.5):** a separate check script, kept outside the repository, loaded the package of the clone and compared `D16KSGammas[]` with `provenance/dirac_matrices/author_notebook_T16.json` and with `algebra-fixture.json`: 11 of 11 statements true, exit code 0, 5.6 s. It changed no file of the clone.
- **Fixes made:** none. The set executed correctly as committed; no file of the set was changed. This provenance file was updated on 2026-10-07 only to add this record, Section 1.5, the citing notebooks of Section 1.4 and the longer run times measured under load (Sections 3.6, 3.7, 4.1, 4.4).
- **Open discrepancies:** none. The observations (a) to (c) of Section 6.1 still hold: (a) was seen again in run 23, (b) in run 22.

### 6.3 Third verification (2026-10-07, after an independent review)

- **Date:** 2026-10-07.
- **Commit verified:** `b8a695d1faa7abe43b4b51eb666f25d250420fb7`, equal to the remote `main` of https://github.com/once-ere/Dirac_claude.git when both clones were made (`git ls-remote`). Between `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (Section 6.2) and this commit the script, the package, the fixture and the two committed outputs did not change (`git diff --stat` over these five files is empty). In both clones their SHA-256 values, line counts and byte counts are exactly those of Sections 2.1 to 2.3, and none of the five files contains a CR byte.
- **Fresh clones:** two clones made in empty scratch folders outside the working copy. Clone A was made with `git clone https://github.com/once-ere/Dirac_claude.git` in PowerShell 7 (97 s, exit code 0). In it, `git count-objects -vH` printed `size-pack: 237.41 MiB`, and `du -sm` gave 238 MB for `.git` and 743 MB for the whole folder. Clone B was made with `git clone -q https://github.com/once-ere/Dirac_claude.git` in Git Bash. No uncommitted file was copied into either clone, and before the first run `git status --porcelain --ignored` printed nothing in both.
- **Environment:** Windows 11 Pro for Workstations 10.0.26300 (build 26300.9457); Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory; WolframScript 1.14.0; Wolfram `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, Professional licence; PowerShell 7.6.6 and Windows PowerShell 5.1.26100.9444; Git for Windows 2.51.2 with its Bash. The processor load was 100 % whenever it was measured (before and after runs 24 and 25), and 14 to 18 Wolfram kernels (`wolfram.exe`) of other programs were running.

| Run | Shell and command (from the repository root of the fresh clone) | Exit code | Wall time | `elapsed_seconds` | Checks | Outputs vs committed |
|---|---|---|---|---|---|---|
| 24 | PowerShell 7.6.6, clone A: the command of Section 3.7, started with `Start-Process` (output to a file). The peak memory and the child processes of `wolframscript` were sampled every 0.2 s, and the folder of Section 5.2 was watched | 0 | 33.94 s | 25 | 125 true, 0 false (155 printed lines ending in CR LF, no `=false`, no `CHECK FAILED`, empty error stream) | both overwritten and byte-identical (`Get-FileHash` `9F04BC10...` and `5B150B36...`); `git status --porcelain --ignored` empty. After the times of day, the durations and the repository root were replaced, the printed output was equal to the listing of Section 4.1. Two child processes `wolfram.exe`: the licence query (`-wlbanner -licenseinfo`, peak 16 MB) and the kernel (peak 289.5 MB), both gone after the run; no `tmp_` file of the run was left behind |
| 25 | PowerShell 7.6.6, clone A: the same command again, measured the same way | 0 | 27.00 s | 20 | 125 true, 0 false | both byte-identical to the committed files (`cmp` with `git show HEAD:<file>`) and to the outputs of run 24 (`cmp`); printed output equal to Section 4.1 after the same replacements; kernel peak 287.6 MB, licence query 24.5 MB; no `tmp_` file left behind; `git status --porcelain --ignored` empty |
| 26 | Git Bash, clone B: the macOS and Linux commands of Sections 3.7 (`echo $?`) and 3.9 (`sha256sum`, `grep -c`, `git status --porcelain`) | 0 | 28.45 s | 22 | 125 true, 0 false (`grep -c` printed 125 and 0) | both byte-identical; `git status --porcelain` empty; 155 printed lines, empty error stream |
| 27 | Git Bash, clone B: Section 3.8 (`ls -d build` printed `ls: cannot access 'build': No such file or directory` before; report path `build/kohn-sham-check/wolfram-kohn-sham-report.json`; both `git diff --no-index --stat`; `rm -rf build`) | 0 | 18.72 s | 14 | 125 true, 0 false | both `git diff --no-index --stat` printed nothing, exit code 0; the run created `build/` and `build/kohn-sham-check/` holding the two files; `git status --porcelain` empty, `--ignored` printed `!! build/`; after `rm -rf build`, `ls -d build` printed the error again and `git status --porcelain --ignored` printed nothing |
| 28 | Windows PowerShell 5.1.26100.9444, clone B: Sections 3.7 (`$LASTEXITCODE`) and 3.9 (`git status --porcelain`, `Get-FileHash ... \| Format-List Hash, Path`, both `Select-String` counts) as written, then the wrong-folder row of 3.10 (the command typed in `scripts/`) | 0; 0 (wrong folder) | 22.99 s | 17 | 125 true, 0 false (`Select-String` counts 125 and 0) | both byte-identical (`9F04BC10...`, `5B150B36...`); `git status --porcelain` empty; wrong folder: `Failed to open file at path: scripts/verify_dirac16complex_kohn_sham.wls`, exit code 0, nothing written |
| 29 | PowerShell 7.6.6, clone B: the command of Section 3.7, started with `Start-Process`; the `wolframscript` process was ended by force (`Stop-Process -Force`) after 12 seconds, during KS_reduction | - (ended by force) | - | - | none (4 progress lines printed) | the two committed outputs untouched (same bytes and same modification times as after run 28); `git status --porcelain --ignored` empty; both `wolfram.exe` processes were gone 3 s after the kill; the file `tmp_8VLVIfZ2UC` (113 bytes, the four progress lines) stayed behind in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (Section 5.2) |
| 30 | Git Bash, clone B: the script, the package and the fixture converted on purpose to CR LF line endings, then the command of Section 3.7 | 0 | 23.72 s | 17 | 125 true, 0 false | `git status --porcelain` listed the three inputs and both outputs. `git diff --stat artifacts/dirac16complex/kohn-sham/` showed 3 changed lines in each output, and these were exactly the three `sourceSha256` lines (the `git status` row of Section 3.10) |
| 31 | Git Bash, clone B: the repair of that row (`git checkout --` of the three inputs), the restore command of Section 5.6, then the command of Section 3.7 again | 0 | 20.01 s | 15 | 125 true, 0 false | after the two `git checkout --` commands `git status --porcelain --ignored` printed nothing; after the run both outputs were byte-identical (`sha256sum`) and `git status --porcelain --ignored` was still empty |

- **Byte identity:** in runs 24, 25, 26, 28 and 31 both committed outputs had exactly the SHA-256 values of Section 2.3 after the run, and in run 27 so did both files written under `build/`. The outputs of runs 24 and 25 (the header command twice in clone A) were identical to each other byte by byte (`cmp`). Run 30 differed, as intended, only in the three `sourceSha256` lines of each output.
- **Files created or overwritten:** runs 24, 25, 26, 28, 30 and 31 overwrote the two committed outputs (with identical bytes, except run 30, whose outputs were restored by run 31); run 27 created `build/` with one sub-folder, deleted afterwards; run 29 changed nothing in the clone. At the end `git status --porcelain --ignored` printed nothing in both clones.
- **Temporary files:** in runs 24 and 25 no `tmp_` file of the run was left in WolframScript's temporary folder. The interrupted run 29 left `tmp_8VLVIfZ2UC`. Two short test scripts that only print a line and wait confirmed the mechanism: while the script ran, its `tmp_` file (23 bytes, the length of the printed line) was locked; it was deleted at the normal end, and when `wolframscript` was ended by force it stayed behind, holding the printed line.
- **"Command not found" messages (Section 3.10):** typing a command name that does not exist printed, in PowerShell 7.6.6, `<name>: The term '<name>' is not recognized as a name of a cmdlet, function, script file, or executable program.`; in Windows PowerShell 5.1, `<name> : The term '<name>' is not recognized as the name of a cmdlet, function, script file, or operable program.`; in interactive Git Bash, `bash: <name>: command not found`. zsh is not installed on the test machine.
- **The Dirac matrices (Sections 1.1 and 1.5):** a rewritten check script, kept outside the repository, loaded the package of clone A, compared `D16KSGammas[]` with `provenance/dirac_matrices/author_notebook_T16.json` (SHA-256 `1ab8ef75...` at this commit) and with `algebra-fixture.json`, and examined `D16KSBlockBasis[]` before and after `D16KSRun`. Result: 17 of 17 statements true, exit code 0, 17.8 s; it changed no file of the clone. The package line numbers quoted in Section 1.5 (98 to 113, 124, 65 and 285) were read from the package of the clone.
- **The independent review and what was done:** the review of 2026-10-07 (made on commit `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6`, where the five files of the set are the same as here) confirmed the instructions and found five points in this file, each corrected here: (1) the introduction of Section 6 named runs 18 to 22 for Section 6.2 instead of 18 to 23; (2) the repository sizes of Sections 3.1 and 3.6 were out of date (now measured on this commit); (3) the run times of Sections 3.7, 4.1 and 4.4 read like limits and were exceeded under load (now given per day as typical values, including the review's own figures and those of this section); (4) Section 1.5 did not give the package line of `D16KSGammas` (124) and left out the factor 1/(2 sqrt(2)) of the block basis; (5) the "command not found" texts of Section 3.10 did not match PowerShell 7 and macOS (now all forms are given). This verification also added the measured `tmp_` files and the interrupted run (Sections 5.1, 5.2, 5.6), the two `wolfram.exe` processes (Section 5.3), one more program that loads the package (Section 1.4) and the LaTeX version of the textbook (Section 1.3).
- **Fixes made:** none to the set. The set executed correctly as committed; no file of the set was changed.
- **Open discrepancies:** none. The observations (b) and (c) of Section 6.1 still hold ((b) was seen again in run 28). One more observation: an interrupted run leaves a `tmp_` file of WolframScript behind (run 29, Section 5.2); it is outside the repository and harmless.
