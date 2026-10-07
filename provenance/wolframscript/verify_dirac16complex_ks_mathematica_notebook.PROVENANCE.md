# Execution provenance: the headless verifier of the Stage-4 Mathematica notebook (WolframScript)

Set: `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`, which evaluates the notebook `notebooks/Dirac16ComplexKohnSham.nb` without opening a window (old Stage 4: the Mathematica cross-check of the Kohn-Sham solver).

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` with Wolfram 15.0.1, WolframScript 1.14.0 and Rust 1.91.1 on Windows 11. Verdict: **EXECUTES OK**. The two runs that the task asks for (R1 and R2, one after the other in the same fresh clone) both printed `dirac16complex_ks_mathematica_notebook=OK` with 94 of 94 notebook checks true and exit code 0, and took 658.9 s and 676.3 s. Both runs rewrote the report `artifacts/dirac16complex/kohn-sham/mathematica-report.json` and the 6 figures under `artifacts/dirac16complex/kohn-sham/figures/mathematica/`, and **all 7 files are byte-identical to the committed ones** after each run (and therefore also identical between the two runs). Three further runs confirmed the instructions and the failure mode: R3 (a second fresh clone, PowerShell, with `--`, an explicit notebook path and `--verbose`) and R5 (a third fresh clone, Git Bash) also passed and reproduced all 7 files byte for byte, and R4 (the third clone before the Rust program was built) failed as expected, with 10 false checks and exit code 1. All runs together: 4 successful runs, each with all 7 outputs byte-identical to the committed files. No fix was needed. No scientific discrepancy was found.

This file is written for a student who has never used Wolfram software, Rust or a terminal. Everything you need to run the set is in this file; you do not have to open any other file.

Contents:

1. What the set is and what it computes
2. Its files
3. How to run it (complete instructions)
4. The expected output
5. Side effects
6. Verification record

## 1. What the set is and what it computes

### 1.1 In plain words

"Stage 4" of the earlier `dirac16complex` work treats many quanta of the 16-component Dirac field `dirac16complex` in the **static** primordial gravitational field with a Kohn-Sham density-functional method (a "DFT"-type approximation). The main solver is a Rust program, `studies/dirac16complex_kohn_sham`. It finds every single-particle energy level by "shooting" (integrating an ordinary differential equation with the CVODE integrator and adjusting the energy until a boundary condition holds), and it iterates the Kohn-Sham equations until they are self-consistent. Its results are committed as CSV and JSON files under `artifacts/dirac16complex/kohn-sham/rust/`.

The Mathematica notebook `notebooks/Dirac16ComplexKohnSham.nb` checks these Rust results **independently** in the Wolfram Language: it derives the equations again symbolically, solves the simplest case exactly, recomputes the spectra with Mathematica's own integrator `NDSolve`, runs its own small self-consistent Kohn-Sham loop, and compares everything with the committed Rust files. It shares no code with the Rust program.

A notebook is a plain text file that holds one Wolfram Language expression, `Notebook[{cells...}, options...]`. This notebook has 77 cells: 1 title, 9 section headings, 5 subsection headings, 29 text cells (the explanations) and **33 Input cells** (the code). The committed notebook contains no results: its Input cells have never been evaluated in it.

**This set evaluates the notebook headless** (without a notebook window): the script `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` opens the notebook file, evaluates its 33 Input cells one after the other in a Wolfram kernel, and decides whether everything passed. While the cells run, they rewrite the report `artifacts/dirac16complex/kohn-sham/mathematica-report.json` and the 6 PNG figures in `artifacts/dirac16complex/kohn-sham/figures/mathematica/`. The script never changes the notebook file.

### 1.2 What the script does, step by step

1. It finds the repository root: the parent of the folder that holds the script. The folder you are in is not used for this.
2. It reads its command-line arguments. A literal `--` is ignored. `--verbose` switches on one extra line per cell. The first other argument, if there is one, is the path of the notebook to evaluate (relative to the folder you are in); without it, the script uses `notebooks/Dirac16ComplexKohnSham.nb` in the repository root.
3. If the notebook file does not exist, it prints `ERROR: missing notebook: <path>` and `dirac16complex_ks_mathematica_notebook=FAILED` and exits with code 2. If the file cannot be read as a notebook, it prints `ERROR: notebook import failed` and the same FAILED line, and exits with code 2.
4. It collects the Input cells. If there are not exactly 33, it prints `ERROR: expected 33 input cells, found <n>` and the FAILED line, and exits with code 1.
5. It sets the variable `$Dirac16RepositoryRoot` to the repository root (the notebook uses it to find every file) and evaluates the 33 cells in order. For each cell it records every message the Wolfram kernel issues (a "message" is the kernel's warning or error text, such as `Power::infy`), and whether the cell returned `$Failed` or a `Failure[...]` object.
6. It reads the association `notebookChecks` (94 named checks, each `True` or `False`) and the measurements of the report that the notebook built.
7. It prints one line `check_<name>=true|false` per check, one line `measurement_<name>=<value>` per measurement (43), then `check_count`, `failed_check_count`, `input_cell_count`, `failed_evaluation_count`, `message_count`, `report=<path>` and `elapsed_seconds`, and lists failed cells, messages and failed checks if there are any.
8. The verdict is OK only if no cell failed, no message was issued, there are exactly 94 checks and all of them are true. It prints `dirac16complex_ks_mathematica_notebook=OK` and exits with code 0, or `=FAILED` and exits with code 1. If the number of checks is not 94, it first prints the line `ERROR: expected 94 notebook checks, found <n>` (after the lines of step 7, just before the FAILED line).

### 1.3 What the notebook computes when the script evaluates it

The 33 Input cells, section by section (the number of checks of each group is in brackets; the check names in the printed output start with the group name):

1. **Repository, packages and committed outputs** (1 cell). Loads two Wolfram packages of the repository, `wolfram/Dirac16ComplexGeometry.wl` (symbolic curved-space geometry and the Dirac operator) and `wolfram/Dirac16ComplexKohnSham.wl` (the exact Stage-4 theory), creates the figure folder if it is missing, and reads the two `summary.json` files of the Rust outputs.
2. **The exact Kohn-Sham theory package** (1 cell; group `theory`, 1 check). Runs all 125 exact checks of `wolfram/Dirac16ComplexKohnSham.wl` (function `D16KSRun`) and requires every one to pass. This reads `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`, the committed exact gamma matrices.
3. **Symbolic derivation of the 2x2 Kohn-Sham block equations** (5 cells; groups `geometry` 6, `reduction` 6, `blocks` 7, `realForm` 10, `pruefer` 8). The metric of the static field ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2 a4} (dx1^2 + dx2^2 + dx3^2) - e^{-2 a4} (dx5^2 + dx6^2 + dx7^2)] and its curvature (Ricci scalar -42 H^2); the reduction of the 16-component Dirac equation with the ansatz Psi = e^{-i eps x4} e^{i k x1} e^{-3Hy} chi(y) to an ordinary differential equation in y; its exact splitting into eight 2 x 2 blocks of two types; the real two-component form that the Rust program integrates; the constants compiled into the Rust source `studies/dirac16complex_kohn_sham/src/generated.rs` (gamma matrices, block basis, fixture fingerprint), compared exactly with the packages; the Pruefer-angle form of the equations and its boundary conditions.
4. **The k = 0, lambda = 0 box problem: exact solution** (3 cells; groups `box` 11, `splitting` 3). The exact energy levels at zero momentum and zero coupling, the brane zero mode, the zero-mode splitting coefficient c = 2/(1 + e^{-3}) = 1.9051482536 at m = H = 1, L = 3, and the comparison of the exact levels with the k = 0 levels of the six Rust files `free-spectrum-m{1,3}-L{2,3,4}.csv`.
5. **NDSolve shooting for the k != 0 single-particle problem** (6 cells; group `shooting`, 13 checks). Recomputes all 2818 levels of the six Rust free-spectrum files with `NDSolve`, compares them level by level (eigenvalues, charges, momenta, multiplicities), checks the worst level of each file against a 32-digit reference computation, and recomputes the two closed-shell tables `closed-shells-m{1,3}-L3.csv`.
6. **A self-consistent Kohn-Sham loop in Wolfram Language** (5 cells; group `scf`, 14 checks). For N = 8 particles, temperature 0, L = 3, m = H = 1 at the coupling lambda_hat_2 = 0.0972989047, it runs its own self-consistent loop (Anderson mixing, 20 iterations to a residual below 1e-12) and compares energies, potentials, densities, the occupied orbital and the complete spectrum of 788 levels in 182 shells with the Rust run `rust/scf/m1_L3_N8_lamp2_T0/`.
7. **The Rust binary: print-config** (1 cell; group `engine`, 11 checks). Runs the compiled Rust program `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham` (`.exe` on Windows) with the command `print-config`, requires exit code 0 and `SUCCESS` as its last printed line, and compares the equations, tolerances and the fixture fingerprint that it prints with the derived ones. **This is why you must build the Rust program before you run the set** (Part 3.7). Without it, 10 of these 11 checks are false and the run fails (Part 6).
8. **Figures** (7 cells; group `figuresExported`, 1 check). Draws the 6 figures and writes them as PNG files. The PNG export starts a hidden notebook front end (Part 5). The notebook's own export code (defined in Input cell 23, the first code cell of this section) removes the PNG text field "Creation Time" from every figure, so that a repeated run gives byte-identical files. The script `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` does not touch the PNG files.
9. **Report and fail-fast verification** (4 cells; group `text`, 3 checks). Checks that the numbers quoted in the notebook's text cells agree with the committed files, collects all 94 checks in `notebookChecks`, writes the report `mathematica-report.json` (with the SHA-256 fingerprint of every file it read), and returns a `Failure` object if any check is false.

Altogether: 1 + 6 + 6 + 7 + 10 + 8 + 11 + 3 + 13 + 14 + 11 + 3 + 1 = **94 checks**.

**About charge conjugation.** The notebook neither defines nor performs a charge conjugation of the field. The 16 x 16 matrix called C in it (`D16GeoC`, C = gamma^0 gamma^1 gamma^2 gamma^3) is the Dirac-conjugation matrix of Psibar = Psi^dagger C, and B = -i C gamma^4 (`kreinB`) is used only to form the scalar-density operator B C. `Conjugate` and `ConjugateTranspose` appear only in inner products of the form chi^dagger M chi and in the change of basis to the blocks. In this repository the charge conjugation of the field is a **matrix** operation (a 16 x 16 matrix combined with complex conjugation), never plain complex conjugation Psi -> Psi*; this set does not use it.

### 1.4 Documents and programs that cite this set or its outputs

* `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md`, the Stage-4 document: its abstract ("all 94 checks of the Mathematica notebook pass"), Section 1 (the notebook as one of the independent checks), Section 3.3 (check `rustLabelSIsMinusJEigenvalue`), Section 5.5 (check `realFormIsBlockODEWithSMinusJ`) and Section 5.7 (checks `parityMinusIsTanPLMinusPOverM` and `splittingAtM1H1L3Is2Over1PlusExpMinus3`, and "the Mathematica notebook's NDSolve shooting agrees with the closed form to 1.6e-7", which is the measurement `zeroModeSlopeMaxDeviation = 1.6056e-7`).
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (with its `.tex` and `.pdf`), Chapter 19, Section 19.9, also stored as `provenance/textbook/chapters/19-reproducing-everything.md`: "the Mathematica notebook's `mathematica-report.json` has 94 of 94 checks true".
* `handoff/specs/STAGE4_SPEC.md`, the Stage-4 specification, which asks for this notebook with its builder and verifier.
* The Stage-4 gate `scripts/verify_stage4_kohn_sham.ps1` and its twin `scripts/verify_stage4_kohn_sham.sh`: step `stage4-30-mathematica-notebook` runs exactly the default command of this set, and step `stage4-31-mathematica-unchanged` requires the report (except its key `engine.binary`) and the figures to be rewritten byte for byte.
* `tests/test_d16c_kohn_sham_mathematica.py`: unit tests of the committed report and figures. They read the expected counts 33 and 94 from this script.
* `studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py`, the builder of the Stage-4 summary: it reads the report as an optional input (its verdict, its checks and its count of checks, which must agree, its `sourceSha256` fingerprints, which must still be those of the current files, and its list of figures).
* `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, which writes the notebook (a different set with its own provenance file; this set does not run it).

## 2. Its files

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone` creates). "Line feeds" is the number of line-feed characters (what `wc -l` prints). All files below are ASCII text with LF line ends, except the PNG figures.

### 2.1 The files of the set

| Role | Path | SHA-256 | Line feeds | Bytes |
| --- | --- | --- | --- | --- |
| the script (you run it) | `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` | `0ad59e5df4b10df9a739d8035fb193e615d4811660d34a3c0fe1511235fc4e8f` | 89 | 5255 |
| the notebook it evaluates (read only) | `notebooks/Dirac16ComplexKohnSham.nb` | `7e91159dba0fd1875736e3101e69a2b174017b173539ad0df4b3348d4457b22f` | 5122 (no newline after the last line, so an editor shows 5123 lines) | 359236 |

Both are unchanged since commit `eac67e6` (2026-09-30); on 2026-10-07 the fresh clones at commits `d278c49` and `72fc9ff` had exactly these bytes. The notebook was written by `scripts/build_dirac16complex_ks_mathematica_notebook.wls` (SHA-256 `2bb0e133adfa86ff3ec8d63e49759e69d6fcb1a1c74805fc6aba7feccff1a982` at the verified commit), which this set does not run. Later on 2026-10-02 that builder received checks of its write steps (SHA-256 `7432e599992eecab33a9caf62e5b7352c8a03e2d36d9eede86d66d9eab8868bb`, in commit `d86e42d`); the notebook and the two files of this set did not change.

### 2.2 The inputs it reads

The notebook records the SHA-256 of every repository file it reads in the report (key `sourceSha256`). These are the 18 files below. On 2026-10-02, and again on 2026-10-07, every one of them in the fresh clones had exactly the recorded fingerprint.

| Input | Path | SHA-256 | Line feeds | Bytes |
| --- | --- | --- | --- | --- |
| geometry package | `wolfram/Dirac16ComplexGeometry.wl` | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` | 997 | 71636 |
| exact Stage-4 theory package | `wolfram/Dirac16ComplexKohnSham.wl` | `5f8d4703ad848f2d2ba5d33497d402da791584fe6777d668f7c626e7de35c65b` | 845 | 84969 |
| exact gamma-matrix fixture | `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 18440 | 213133 |
| Rust constants (source code) | `studies/dirac16complex_kohn_sham/src/generated.rs` | `3da13ff980a3d74060a8bb07d9fd8348d9b00eb3580bad08a9cc59e3039f9df6` | 324 | 21717 |
| Rust spectrum summary | `artifacts/dirac16complex/kohn-sham/rust/spectrum/summary.json` | `52d4eb13142740b90ad7aad1c2868748501291ecd9c103149ecc1dadb95c5091` | 291 | 8197 |
| Rust free spectrum m = 1, L = 2 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L2.csv` | `e85632681b02a51898b17e3e57b761b24aff8abcd4ebc7f2f5aaba878c685d71` | 219 | 85540 |
| Rust free spectrum m = 1, L = 3 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L3.csv` | `49970f6a02862ae063d258c2546eb1f8232fc05f5ede78de8c6122c8c784665a` | 241 | 94198 |
| Rust free spectrum m = 1, L = 4 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L4.csv` | `58bc76f6c90ae347874f0640d208368d59c4f4c4c5687aaf348f98276d4ab162` | 249 | 97340 |
| Rust free spectrum m = 3, L = 2 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L2.csv` | `9c94abada90670bd2f3fa4d3946ac2d6ffda3b115c1a7e5a39925e372815cc68` | 657 | 257298 |
| Rust free spectrum m = 3, L = 3 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L3.csv` | `c9d4b01371ca748bbeda5b06402cc3c8b7bf1f884de992cfb43d15b776f3c7d8` | 715 | 280020 |
| Rust free spectrum m = 3, L = 4 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L4.csv` | `574da21949cd87a904fec35da634b3edd6607654ac24684bc09c8c68f71e5626` | 743 | 290916 |
| Rust closed shells m = 1 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/closed-shells-m1-L3.csv` | `f0b13a0c234154f74c7e7530e1829a066f4ed062183797fbb962f23053d04d80` | 21 | 971 |
| Rust closed shells m = 3 | `artifacts/dirac16complex/kohn-sham/rust/spectrum/closed-shells-m3-L3.csv` | `398861d25ffc6f76b1f4f4dcced8637c1842b62e32124610d73601fd9e4e8dee` | 23 | 1067 |
| Rust self-consistent runs, summary | `artifacts/dirac16complex/kohn-sham/rust/scf/summary.json` | `44017474744f7f501b0a07f5d64a1bb1e8fc8e8412ddf10a3e23313a2a101759` | 3671 | 150624 |
| Rust run N = 8: parameters and results | `artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/run.json` | `7b2155d8e8a9e9eb3551819072b1bb4fe1fcf4efb8463cb01a1b6e514536fcb4` | 92 | 3530 |
| Rust run N = 8: profiles on the grid | `artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/profiles.csv` | `f9c8aa72c4a4c842795562d22c274c7fbfd038624ec4958ccf806655e76db0d0` | 302 | 125053 |
| Rust run N = 8: levels | `artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/levels.csv` | `a4a38b702c1873d3fc725cca91c0bdf28c4616be104739ccbe87b2b6545a1329` | 789 | 325987 |
| Rust run N = 8: iteration history | `artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/history.csv` | `e194b9db46810883a23cb1e9509ae6e1388ba47d664313ce7266e6737cbc47f9` | 20 | 3759 |

It also uses one program that is **not** in the repository and that you build yourself (Part 3.7): the Rust program `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham` (`.exe` on Windows), which it runs once with `print-config`. Building it needs the pinned CVODE engine in `vendor/rustSolveIt/` (fetched by `scripts/setup_solver.ps1` or `scripts/setup_solver.sh`, Part 3.6) and the crate sources in `studies/dirac16complex_kohn_sham/`. The program's printed text, not its bytes, is what the notebook compares: the program contains the folder name of the clone, so every build has another fingerprint (the four builds of 2026-10-02 gave four different SHA-256 values), and all of them passed (and so did the two builds of 2026-10-07).

Like every Wolfram kernel, it also reads the Wolfram system files and, if you have one, your personal kernel start-up file `Kernel/init.m` in your Wolfram user folder.

### 2.3 The outputs it writes

The paths are fixed: the notebook always writes into the repository it belongs to. All 7 files are committed, so every run **overwrites** committed files (Part 5).

| Output | Path | SHA-256 of the committed file | Size |
| --- | --- | --- | --- |
| report | `artifacts/dirac16complex/kohn-sham/mathematica-report.json` | `ac433ca6f891d51c4aca4fe00ebbae3ef8e847602a7e90329d05fc48a12e6a34` | 28046 bytes, 859 line feeds, ASCII, LF, tab indentation, ends with a newline |
| figure: free spectrum | `artifacts/dirac16complex/kohn-sham/figures/mathematica/free_spectrum_m1_L3.png` | `f1fd3d43ecbf030424b590b41ae630fae2e59f1e4eed64e27f0e16469c2a25cf` | 145743 bytes, 1162 x 837 pixels |
| figure: box levels | `artifacts/dirac16complex/kohn-sham/figures/mathematica/box_levels_vs_L.png` | `4f372e20c904d92f172c386f0c95a6c9753572b49b3fe615d06bc56b6da18d63` | 92936 bytes, 1162 x 837 pixels |
| figure: pseudo-potential | `artifacts/dirac16complex/kohn-sham/figures/mathematica/scf_pseudo_potential.png` | `d1a431834673a38de8ea23552cd43b44cfe87b0394010f551f7a1fc08e1f4d94` | 69554 bytes, 1162 x 837 pixels |
| figure: densities | `artifacts/dirac16complex/kohn-sham/figures/mathematica/scf_proper_densities.png` | `b3c0c108e71928018684ee03d38b0e0db55684976ba7ba09ac5a9019cd55933e` | 77573 bytes, 1162 x 837 pixels |
| figure: convergence | `artifacts/dirac16complex/kohn-sham/figures/mathematica/scf_convergence.png` | `7879158f27b3ffa5b1234b7d611b65909a853e041ff6dd7ee67044c30fe8f345` | 59576 bytes, 1162 x 837 pixels |
| figure: agreement overview | `artifacts/dirac16complex/kohn-sham/figures/mathematica/agreement_overview.png` | `88478d4dd8f3d4e980b8d98026f5ff4cd2b91dfd114318132ab78e931f6d6bd0` | 56324 bytes, 1162 x 617 pixels |

The report contains no date, no time and no folder name, so a correct run on the same platform reproduces it byte for byte. It does contain the Wolfram version (`"wolframVersion": 15.0`) and the platform-specific program name (`engine.binary`, `.../dirac16complex_kohn_sham.exe` on Windows), so a run on macOS or Linux differs from the committed report at least in that key (Part 4.5).

## 3. How to run it (complete instructions)

### 3.1 What you need

* A 64-bit computer with Windows 10 or 11, macOS, or Linux. Only Windows 11 was tested (Part 6).
* About 1.5 GB of free disk space: on 2026-10-07 the repository was about 195 MB to download and about 670 MB on disk (it grows as the project grows); the Rust engine adds about 84 MB and the compiled program about 18 MB; the Wolfram Engine itself needs several GB.
* About 1 GB of free memory: the Wolfram kernel used at most 575 MB in the tests.
* An internet connection for the installations, the repository and the Rust engine. The run itself does not need the network.
* Four programs: **Git**, **WolframScript with a Wolfram kernel**, the **Rust toolchain** (`cargo`), and, on Windows, the Microsoft C++ build tools that Rust needs. You do not need Python or Jupyter for this set.
* Patience: one run took 11 to 17 minutes on the verification machine, depending on how busy it was (Part 4.4).

### 3.2 Open a terminal

A terminal is a window in which you type commands. Type each command exactly as shown, one line at a time, and press Enter after each line.

* **Windows:** click Start, type `PowerShell`, and open "Windows PowerShell" (or "PowerShell 7", or "Terminal").
* **macOS:** open Finder, then Applications, then Utilities, then Terminal.
* **Linux:** open your distribution's terminal program (for example "Terminal" in Ubuntu).

After you install a program, close the terminal and open a new one, so that it finds the new program.

### 3.3 Install Git

* **Windows:** download the installer from https://git-scm.com/download/win, run it, and accept all default choices. Instead, you can type `winget install --id Git.Git -e` in PowerShell.
* **macOS:** type `xcode-select --install` and click Install. This installs Git and the C compiler tools that Rust needs on macOS.
* **Linux:** on Debian or Ubuntu type `sudo apt install git`; on Fedora type `sudo dnf install git`.

Check: `git --version` prints a line such as `git version 2.51.2.windows.1`.

### 3.4 Install a Wolfram kernel and WolframScript, and activate it

You need two programs. The first is the Wolfram Language *kernel*, the program that does the computing. The second is *WolframScript*, the command `wolframscript`, which runs a script file with the kernel. The verification used kernel version 15.0.1 and WolframScript 1.14.0.

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser, open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page. Create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded installer and accept the defaults. Instead, in PowerShell, you can type `winget install --id WolframResearch.WolframEngine -e`. The installer also installs WolframScript and adds it to the PATH.
   * macOS: open the downloaded `.dmg` file and follow its instructions: drag the application into Applications and open it once.
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/ (a `.msi` file for Windows, a `.pkg` file for macOS, a `.deb` file for Debian or Ubuntu, installed with `sudo apt install ./<file>.deb`, or a `.rpm` file for Fedora, installed with `sudo dnf install ./<file>.rpm`), then open a new terminal.
3. Activate it. Type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. If you see the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.

**Option 2: Wolfram (formerly Mathematica), the desktop product.** A licensed Wolfram or Mathematica installation contains the kernel, and on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately as in step 2 above. The verification machine used this option (Wolfram 15.0.1 with a Professional licence).

**Test the installation.** In a new terminal, type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux, because they stop the shell from replacing `$Version`; they are also correct in PowerShell. `wolframscript -version` prints the WolframScript version, for example `WolframScript 1.14.0 for Microsoft Windows (64-bit)`. (The verification machine already had Wolfram installed and activated; the installation steps above were not repeated for this record. The two test commands were run on 2026-10-02 and again on 2026-10-07, with the outputs shown.)

### 3.5 Install Rust

Rust is installed with the program `rustup`, which installs the compiler `rustc` and the build tool `cargo`. The verification used Rust 1.91.1 (`cargo 1.91.1`, `rustc 1.91.1`, toolchain `stable-x86_64-pc-windows-msvc`).

* **Windows:** Rust needs the Microsoft C++ build tools. Open https://rustup.rs, download `rustup-init.exe` and run it (instead, you can type `winget install --id Rustlang.Rustup -e` and then run `rustup default stable` in a new terminal). If the installer says that the Visual Studio C++ build tools are missing, let it install them (or install "Build Tools for Visual Studio" from https://visualstudio.microsoft.com/visual-cpp-build-tools/ with the workload "Desktop development with C++"). Accept the default installation (option 1).
* **macOS:** after `xcode-select --install` (Part 3.3), type

  ```
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

  choose option 1 (the default), and then type `source "$HOME/.cargo/env"` (or open a new terminal).
* **Linux:** on Debian or Ubuntu type `sudo apt install build-essential curl` (on Fedora: `sudo dnf install gcc curl`), then the same `curl ... | sh` command as for macOS, option 1, and `source "$HOME/.cargo/env"`.

Check: in a new terminal, `cargo --version` prints a line such as `cargo 1.91.1 (ea2d97820 2025-10-10)`. (The verification machine already had Rust installed; the installation steps above were not repeated for this record. Any recent stable Rust should work; only 1.91.1 was tested.)

### 3.6 Get the repository and the Rust engine

**On Windows, put the repository in a folder with a short path**, for example `C:\work`. The Microsoft linker that Rust uses on Windows cannot open a file whose full path has 260 or more characters, and the longest file it opens during the build of Part 3.7 lies 103 characters below the repository folder (`studies\dirac16complex_kohn_sham\target\release\deps\libdirac16complex_kohn_sham-<16 hexadecimal digits>.rlib`). The full path of the repository folder `Dirac_claude` must therefore have **at most 156 characters**. This was measured on the verification machine, on 2026-10-02 and again on 2026-10-07: a repository path of 156 characters built, one of 157 characters failed with `LNK1104` (Part 3.10), even though long paths were enabled in Windows (`LongPathsEnabled = 1`). In Windows PowerShell, to make and enter such a folder, type:

```
mkdir C:\work
cd C:\work
```

(If `C:\work` already exists, `mkdir` prints an error saying so; ignore it and type the `cd` line.) On macOS and Linux the folder does not matter; your home folder is fine.

In the folder where you want the repository, type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

On Windows you can check the length of the path in PowerShell with `(Get-Location).Path.Length`, typed in the repository folder: it must print a number not larger than 156 (`C:\work\Dirac_claude` gives 20). The clone took 9 seconds on 2026-10-02 and 13 seconds on 2026-10-07 on the verification machine. Type every command below in this folder, the *repository root*: the folder that contains `scripts`, `notebooks`, `studies` and `wolfram`. The repository stores every file byte for byte (its `.gitattributes` turns off line-end conversion), so the checked-out notebook and inputs have exactly the committed bytes.

The Rust program uses a pure-Rust version of the SUNDIALS 7.8.0 CVODE integrator, which is not stored in this repository. A setup script downloads it, at a fixed ("pinned") commit, into the folder `vendor/rustSolveIt` (Git ignores this folder):

* **Windows PowerShell:**

  ```
  powershell -NoProfile -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11
  ```

  (`-ExecutionPolicy Bypass` allows this one script to run even if your PowerShell forbids scripts; it changes no setting.)
* **macOS and Linux** (and Git Bash on Windows):

  ```
  bash scripts/setup_solver.sh
  ```

  The script detects your platform (macOS, Linux, or `win11` in Git Bash on Windows).

The last line printed must be `solver_setup=OK` (or `solver_setup=ALREADY-PRESENT` if you run it a second time). The download took 5 to 8 seconds and occupies about 84 MB.

### 3.7 Build the Rust program

From the repository root, in any of the three shells:

```
cargo build --manifest-path studies/dirac16complex_kohn_sham/Cargo.toml --release
```

A first build took 8 to 20 seconds on the verification machine (six builds on two days); it ends with a line like ``Finished `release` profile [optimized] target(s) in 16.92s``. Run it from the repository root, so that the repository's `.cargo/config.toml` (which switches on the FMA instructions of the processor) applies. The program is written to `studies/dirac16complex_kohn_sham/target/release/`.

Check that it works:

* Windows PowerShell: `.\studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe print-config`
* macOS, Linux and Git Bash: `./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham print-config`

It prints 25 lines that describe the solver (for example `fixture sha256   = 8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b`); the last line must be `SUCCESS`. This command writes no file.

### 3.8 Run the set

The usage line in the script's header is

```
wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls [notebook.nb] [--verbose]
```

The square brackets mean that both arguments are optional; you do not type the brackets. The normal run uses neither.

Two lines below that usage line, the script's header (its line 23) says `(WolframScript 1.14 drops arguments after "--": pass the path positionally.)`. **That comment is outdated for this script; ignore it.** It is true only for a script whose first line is not `#!/usr/bin/env wolframscript`. This script starts with that line, and then WolframScript 1.14.0 passes `--` and every argument after it to the script, which ignores the `--`. Measured on 2026-10-02 with two two-line test scripts that print their arguments: with that first line, `wolframscript -file with.wls -- x.nb --verbose` gave the arguments `{with.wls, --, x.nb, --verbose}`; without it, the same command gave only `{without.wls}`; the same in Windows PowerShell 5.1, PowerShell 7.6.6 and Git Bash. The real script used both the path and `--verbose` written after `--` (Part 6). So the `--` forms shown under "Options" below work, and so does the positional form without `--`. The script itself is left unchanged.

**Windows PowerShell:**

```
wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls
$LASTEXITCODE
```

**macOS Terminal (zsh), Linux terminal (bash), or Git Bash on Windows:**

```
wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls
echo $?
```

Nothing is printed while the cells run: in the verification runs all 145 lines arrived at the very end, after 11 to 17 minutes on the verification machine (Part 4.4). Do not close the window in the meantime. The second line prints the exit code, which must be `0`. To time the run, type `Measure-Command { wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls | Out-Host }` in PowerShell, or put `time ` in front of the command in bash or zsh.

**Options.**

* **`--verbose`** prints, before the 145 lines, one line per cell with its wall time, for example `cell 2 time=9.52 failed=False messages=0`. Each of these lines appears as soon as its cell has finished (measured on 2026-10-07 with the output written to a file: 19 of them were there after about 8 minutes, while cell 20 was still running), so you can follow the progress. Write it after `--`, as in `wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls -- --verbose`. Without the `--`, WolframScript also takes `--verbose` as its own option and prints three extra lines of its own on the error output, beginning with `Performing '-file' parsing.`; they are harmless. (The script ignores the `--`. Because the script's first line is `#!/usr/bin/env wolframscript`, WolframScript 1.14.0 passes the `--` and everything after it to the script; this was tested in PowerShell 7.6.6, Windows PowerShell 5.1 and Git Bash.)
* **A notebook path** evaluates another copy of the notebook, for example `wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls -- notebooks/Dirac16ComplexKohnSham.nb`. A relative path is taken relative to the folder you are in. The copy must have exactly 33 Input cells. Whatever notebook you give, the outputs are always written to the fixed paths of Part 2.3 of the repository that contains the script.

### 3.9 Check the result

1. **The last printed line** must be `dirac16complex_ks_mathematica_notebook=OK`, the lines before it must include `check_count=94`, `failed_check_count=0`, `input_cell_count=33`, `failed_evaluation_count=0` and `message_count=0`, and the exit code must be `0` (Part 4.1).
2. **The report's summary.** One of these commands prints the verdict, the number of checks and the number of failed checks of the report:
   * Windows PowerShell: `$r = Get-Content -Raw artifacts/dirac16complex/kohn-sham/mathematica-report.json | ConvertFrom-Json; "$($r.verdict) $($r.checkCount) failed=$($r.failedChecks.Count)"` must print `SUCCESS 94 failed=0`.
   * macOS, Linux, Git Bash or PowerShell 7, with WolframScript: `wolframscript -code 'r = Import["artifacts/dirac16complex/kohn-sham/mathematica-report.json", "RawJSON"]; {r["verdict"], r["checkCount"], r["failedChecks"]}'` must print `{SUCCESS, 94, {}}`.

     **Not in Windows PowerShell 5.1.** The program called "Windows PowerShell" (the one that opens when you type `PowerShell` in the Start menu, and the usual default of the Windows 11 "Terminal") is version 5.1; the command `$PSVersionTable.PSVersion.ToString()` prints your version, for example `5.1.26100.9444` (Windows PowerShell 5.1) or `7.6.6` (PowerShell 7). Windows PowerShell 5.1 removes the double quotes inside the single-quoted code when it starts `wolframscript`, so `Import` receives no valid file name. The command then prints `Import::chtype: First argument ... is not a valid file, directory or URL specification.` and `{$Failed[verdict], $Failed[checkCount], $Failed[failedChecks]}`, and the exit code is still `0`. This does **not** mean that the run failed. In Windows PowerShell 5.1 use the `ConvertFrom-Json` command above, which works in every PowerShell. (In 5.1 only, you can also write each inner double quote as `\"`, that is `wolframscript -code 'r = Import[\"artifacts/dirac16complex/kohn-sham/mathematica-report.json\", \"RawJSON\"]; {r[\"verdict\"], r[\"checkCount\"], r[\"failedChecks\"]}'`, which prints `{SUCCESS, 94, {}}` there; in PowerShell 7 that form fails with `ToExpression::sntx` and prints `$Failed`.)
3. **Git sees no change.** Type

   ```
   git status --porcelain
   ```

   It must print nothing: the run rewrote the report and the 6 figures with exactly the committed bytes. (The folders `vendor/` and `studies/dirac16complex_kohn_sham/target/` are ignored by Git and are not listed.)
4. **The fingerprints** (optional) must be those of Part 2.3. To print them:
   * Windows PowerShell: `Get-FileHash artifacts/dirac16complex/kohn-sham/mathematica-report.json, artifacts/dirac16complex/kohn-sham/figures/mathematica/*.png -Algorithm SHA256 | Format-Table Hash, Path`. PowerShell prints them in capital letters; that is the same value.
   * macOS: `shasum -a 256 artifacts/dirac16complex/kohn-sham/mathematica-report.json artifacts/dirac16complex/kohn-sham/figures/mathematica/*.png`
   * Linux and Git Bash: `sha256sum artifacts/dirac16complex/kohn-sham/mathematica-report.json artifacts/dirac16complex/kohn-sham/figures/mathematica/*.png`

### 3.10 If it fails

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `wolframscript` is not recognized / `command not found` | WolframScript is not installed or not on the PATH | Install it (Part 3.4). On Windows you can add its folder for the current session with `$env:Path += ";C:\Program Files\Wolfram Research\WolframScript"`. On macOS and Linux, find it with `find / -name wolframscript -type f 2>/dev/null` and add its folder with `export PATH="<folder>:$PATH"`. |
| A request for a Wolfram ID, or a message that the kernel is not activated or that no licence is available | The engine was never activated, or its licence has expired | Run `wolframscript -activate` (Part 3.4) and run the set again. |
| A message that too many kernels are running, or that no kernel licence is free | Your licence (the free licence in particular) may limit how many kernels can run at the same time | Close other Wolfram programs and run again. This set runs one kernel for 11 to 17 minutes (WolframScript first starts a short licence-check kernel for a moment); near the end the PNG export briefly starts a hidden notebook front end with a second, sandboxed kernel (Part 5). |
| `ERROR: missing notebook: <path>`, then `...=FAILED`, exit code 2 | The notebook path you gave does not exist (a relative path is taken relative to the folder you are in) | Give the right path, or no path at all. |
| `ERROR: expected 33 input cells, found <n>`, then `...=FAILED`, exit code 1 (after about 4 seconds) | You gave another notebook, or the notebook was changed, for example by saving it in Mathematica after evaluating it | Restore it with `git checkout -- notebooks/Dirac16ComplexKohnSham.nb`, and give no path. |
| `ERROR: expected 94 notebook checks, found <n>` just before `...=FAILED`, exit code 1 | The notebook has 33 Input cells but does not define exactly 94 checks: you gave another notebook, or the notebook was changed. If `failed_cells=` or `messages=` lines are also printed, a failing cell stopped the checks from being collected (see the row about `message_count=` below). | Restore the notebook with `git checkout -- notebooks/Dirac16ComplexKohnSham.nb`, and give no path. (Measured with a test notebook of 33 trivial Input cells that defines a single check: `found 1`, exit code 1, after 4.8 s.) |
| After 10 to 17 minutes: `check_engine_binaryFound=false` and nine more `check_engine_...=false` lines, `failed_check_count=10`, `failed_evaluation_count=1`, `failed_cells=33`, `failed_checks=engine_binaryFound,...`, then `...=FAILED`, exit code 1 | The Rust program was not built (Parts 3.6 and 3.7), or its build failed | Build it, restore the report (it was overwritten with verdict `FAILURE`) with `git checkout -- artifacts/dirac16complex/kohn-sham/mathematica-report.json artifacts/dirac16complex/kohn-sham/figures/mathematica`, and run the set again. This was measured in run R4 of Part 6.1 (no engine and no build: 594 s, then exit code 1) and in run V3 of Part 6.2 (a build that failed with `LNK1104`: 1020 s on a fully loaded machine, then exit code 1). |
| `cargo build` fails with `failed to read ... vendor/rustSolveIt/.../Cargo.toml` | The Rust engine was not downloaded | Run the setup script of Part 3.6 and build again. |
| `cargo build` fails with `linker 'link.exe' not found` (Windows) or `linker 'cc' not found` (macOS, Linux) | The C/C++ build tools are missing | Install them (Part 3.5: the Visual Studio C++ build tools on Windows, `xcode-select --install` on macOS, `build-essential` on Linux) and build again. |
| `cargo build` fails (exit code 101) with `` error: linking with `link.exe` failed: exit code: 1104 `` and `LINK : fatal error LNK1104: cannot open file '<repository folder>\studies\dirac16complex_kohn_sham\target\release\deps\libdirac16complex_kohn_sham-<16 hexadecimal digits>.rlib'` (Windows), although that file exists | The path of the repository folder is too long: more than 156 characters, so the path of that file has 260 or more characters, which the Microsoft linker cannot open | Clone the repository again into a folder with a short path, for example `C:\work` (Part 3.6), and repeat Parts 3.6 and 3.7 there. If you run the set without a successful build, it fails after about 10 minutes with 10 false `engine` checks (the row beginning "After about 10 minutes" above). Measured: a repository path of 157 characters failed in 8.7 s, one of 156 characters built in 9.1 s (2026-10-02); again on 2026-10-07, 157 characters failed (exit code 101, 20 s) and 156 characters built (20 s). |
| `setup_solver.ps1 cannot be loaded because running scripts is disabled on this system` | You started the script without `-ExecutionPolicy Bypass` | Use the exact command of Part 3.6. |
| `vendor\rustSolveIt is at <commit>, expected <commit>; remove it and rerun`, or `... is an incomplete checkout` | An older or interrupted download is in the way | Delete the folder `vendor/rustSolveIt` (Windows PowerShell: `Remove-Item -Recurse -Force vendor/rustSolveIt`; macOS and Linux: `rm -rf vendor/rustSolveIt`) and run the setup script again. |
| `message_count=` larger than 0, with a line `messages=cell <n>: ...`, or `failed_cells=...`, and `...=FAILED` | A Wolfram message or a failed evaluation in that cell, for example with another Wolfram version, or a changed input file | Read the message. Check with `git status --porcelain` that no input file was changed, and restore changed files with `git checkout -- <file>`. Note the Wolfram version (`wolframscript -code '$Version'`); only 15.0.1 was tested. |
| The WolframScript check command of Part 3.9 prints `Import::chtype: First argument ... is not a valid file, directory or URL specification.` and `{$Failed[verdict], $Failed[checkCount], $Failed[failedChecks]}` | You typed it in Windows PowerShell 5.1, which removes the double quotes inside the single-quoted code; the run itself is not affected | Use the `ConvertFrom-Json` command of Part 3.9 (it must print `SUCCESS 94 failed=0`), or type the WolframScript command in PowerShell 7 or Git Bash. |
| `OK`, but `git status --porcelain` lists the report or figures as modified (` M ...`) | Another Wolfram version or another platform computed slightly different floating-point numbers or drew the figures with other fonts (Part 4.5) | The checks decide correctness, not the bytes. Look at the difference with `git diff artifacts/dirac16complex/kohn-sham/mathematica-report.json` and restore the committed files with the `git checkout` command of Part 5. |
| Nothing is printed for many minutes | This is normal: the script prints only at the end | Wait. The verification machine needed 11 minutes when it was moderately busy and 17 minutes when all its 24 cores were busy; a slower computer can need longer. Use `-- --verbose` (Part 3.8) to see each cell finish. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly 145 lines on standard output and nothing on standard error: 94 `check_` lines, 43 `measurement_` lines and 8 summary lines. In all seven successful verification runs (R1, R2, R3 and R5 of Part 6.1, V1, V2 and V4 of Part 6.2) the 145 lines were identical except the lines `report=` and `elapsed_seconds=`. On Windows the lines end with CR LF.

```
check_theory_packageChecksAllPass=true
check_geometry_gammasEqualGeometryPackage=true
check_geometry_christoffelAgreesWithPackage=true
check_geometry_sqrtDetIsE6Hy=true
check_geometry_einsteinTensorIsDiag15_21=true
check_geometry_ricciScalarMinus42H2=true
check_geometry_requiredSourceRhoMinus21PPlus15=true
check_reduction_reducedEquationIsLinear=true
check_reduction_derivativeMatrixIsGamma0=true
check_reduction_restMatrixIsIKappaKGamma1MinusIEpsGamma4MinusM=true
check_reduction_odeFormAtZeroExchange=true
check_reduction_withoutW3the3HGamma0TermRemains=true
check_reduction_flatMeasure=true
check_blocks_basisUnitary=true
check_blocks_basisDiagonalisesJ=true
check_blocks_odeMatrixBlockDiagonal=true
check_blocks_blocksEqualNj=true
check_blocks_twoInequivalentTypesFourEach=true
check_blocks_hMinusIsMinusHPlus=true
check_blocks_scalarDensityOperatorIsJSigma2=true
check_realForm_realFormIsBlockODEWithSMinusJ=true
check_realForm_sMinusOneIsMirrorOfSPlusOne=true
check_realForm_scalarDensityIsMinus2sab=true
check_realForm_numberDensityIsA2PlusB2=true
check_realForm_rustGammasEqualPackage=true
check_realForm_rustFixtureHashIsFixture=true
check_realForm_rustBasisUnitary=true
check_realForm_rustBasisBlockDiagonalisesWithJMinusS=true
check_realForm_rustLabelSIsMinusJEigenvalue=true
check_realForm_rustLabelC1IsIGamma2Gamma3=true
check_pruefer_pruferEquation=true
check_pruefer_variationalCoefficient=true
check_pruefer_pruferMonotoneInEps=true
check_pruefer_bagIsThetaZero=true
check_pruefer_parityPlusTargetsNPi=true
check_pruefer_parityMinusTargetsHalfPiPlusNPi=true
check_pruefer_currentVanishesForEitherComponentZero=true
check_pruefer_standingWaveCarriesNoCurrent=true
check_box_boxSolutionSolvesODE=true
check_box_boxSolutionSatisfiesTipBag=true
check_box_parityPlusIsSinPL=true
check_box_parityMinusIsTanPLMinusPOverM=true
check_box_parityMinusBracketSignChange=true
check_box_zeroModeSolvesODEBothTypes=true
check_box_zeroModeNormalisableOnHalfLine=true
check_box_belowThresholdParityPlusOnlyAtEpsZero=true
check_box_belowThresholdNoParityMinusLevel=true
check_box_belowThresholdAtEpsZeroIsZeroMode=true
check_box_thresholdIsNoLevel=true
check_splitting_splittingEqualsPackageClosedForm=true
check_splitting_splittingAtM1H1L3Is2Over1PlusExpMinus3=true
check_splitting_splittingPositiveProductForm=true
check_shooting_boxExactLevelsEqualRustK0=true
check_shooting_shootingToolReproducesExactBox=true
check_shooting_zeroModeSlopeEqualsMinusSC=true
check_shooting_freeSpectraSameLevelKeys=true
check_shooting_freeSpectraEigenvalues=true
check_shooting_freeSpectraCharges=true
check_shooting_freeSpectraKAndMultiplicityColumns=true
check_shooting_freeSpectraK0NDSolveEqualsExactBox=true
check_shooting_freeSpectraLinearMatchingResiduals=true
check_shooting_notebookEigenvaluesWithin1e11OfHighPrecisionReference=true
check_shooting_closedShellTablesEqualRust=true
check_shooting_closedShellStoppingRuleSupported=true
check_shooting_closedShellNumbersEqualRust=true
check_scf_scfSetup=true
check_scf_scfLoopConverged=true
check_scf_scfEpsHomoEqualsRust=true
check_scf_scfEnergyEqualsRust=true
check_scf_scfEnergyPartsEqualRust=true
check_scf_scfMeffEqualsRust=true
check_scf_scfVxEqualsRust=true
check_scf_scfDensitiesEqualRust=true
check_scf_scfHomoProfileEqualsRust=true
check_scf_scfSpectrumSameLevelKeys=true
check_scf_scfSpectrumEigenvalues=true
check_scf_scfSpectrumBranches=true
check_scf_scfAufbauReproducesLoopOccupation=true
check_scf_scfGapLumoSeaTopEqualRust=true
check_engine_binaryFound=true
check_engine_exitCodeZero=true
check_engine_lastLineSUCCESS=true
check_engine_printedFixtureHashMatches=true
check_engine_summariesRecordFixtureHash=true
check_engine_printedTolerancesMatchSummaries=true
check_engine_printedRealSystemIsDerivedForm=true
check_engine_printedBoundaryConditionsAreDerived=true
check_engine_printedExchangeClosedFormAndPotentials=true
check_engine_printedPseudoPotentialIsHartreePlusExchange=true
check_engine_printedMixingMatchesRun=true
check_text_freeSpectraWindowFourMAndShellsUpTo16=true
check_text_closedShellTablesStopAbove1300=true
check_text_scfParameterSetAsStated=true
check_figuresExported=true
measurement_theoryPackageCheckCount=125
measurement_zeroModeSplittingC_m1_H1_L3=1.9051482536448665
measurement_zeroModeSlopeMaxDeviation=1.6056268070663293e-7
measurement_boxExactLevelCount=352
measurement_boxExactVsRustMaxAbsDeviation=2.795825793100448e-10
measurement_boxNDSolveVsExactMaxAbsDeviation=5.151434834260726e-12
measurement_freeSpectraLevelCount=2818
measurement_freeSpectraMaxAbsDeviation=1.1656222653755322e-9
measurement_freeSpectraMaxScalarChargeDeviation=1.3035827972629477e-10
measurement_freeSpectraMaxPressureChargeDeviation=1.019888618003506e-9
measurement_freeSpectraMaxPressureChargeRelativeDeviation=3.25344295418429e-10
measurement_freeSpectraMaxMatchingResidual=2.198192730331134e-11
measurement_worstLevelNotebookMinusReferenceMax=4.050093593832571e-13
measurement_worstLevelRustMinusReferenceMax=1.1660148402370396e-9
measurement_closedShellEntries_m1_L3=20
measurement_closedShellEntries_m3_L3=22
measurement_closedShellsMaxAbsDeviation=5.309841455414244e-11
measurement_scfLambdaHat=0.09729890470551315
measurement_scfIterations=20
measurement_scfFinalResidual=6.141878133450352e-13
measurement_scfEpsHomo=-0.0016857932845794252
measurement_scfEpsHomoDeviation=1.1668183780288999e-14
measurement_scfEnergy=-0.007830391951227303
measurement_scfEnergyDeviation=3.3831808882167635e-12
measurement_scfEnergyRelativeDeviation=4.3205766809984125e-10
measurement_scfKsSumDeviation=9.334547024231199e-14
measurement_scfHartreeDeviation=4.644505700174273e-12
measurement_scfExchangeDeviation=1.1679806427578043e-12
measurement_scfMeffMaxAbsDeviation=1.1150205869725482e-8
measurement_scfMeffTolerance=6.059253086493244e-6
measurement_scfVxMaxAbsDeviation=3.171492846121282e-9
measurement_scfVxTolerance=4.039502057662163e-7
measurement_scfNcMaxDeviationOverD=4.833343092323775e-11
measurement_scfScMaxDeviationOverD=1.4819984043319827e-12
measurement_scfHomoProfileMaxDeviation=8.856307354143667e-11
measurement_scfSpectrumLevelCount=788
measurement_scfSpectrumShells=182
measurement_scfSpectrumMaxAbsDeviation=5.440079497986972e-10
measurement_scfEpsFreeMaxAbsDeviation=1.2815659644616062e-10
measurement_scfKsGap=0.43189869708317685
measurement_scfKsGapDeviation=4.953482068970061e-12
measurement_scfEpsLumoDeviation=4.941824727211497e-12
measurement_scfSeaTopDeviation=4.575784195992583e-13
check_count=94
failed_check_count=0
input_cell_count=33
failed_evaluation_count=0
message_count=0
report=<repository root>\artifacts\dirac16complex\kohn-sham\mathematica-report.json
elapsed_seconds=<seconds>
dirac16complex_ks_mathematica_notebook=OK
```

`<repository root>` stands for the absolute path of your clone, for example `C:\Users\you\Dirac_claude` (on macOS and Linux with `/` instead of `\`). `<seconds>` is the run time measured by the script itself (657, 670, 592 and 728 in the runs R1, R2, R3 and R5 of 2026-10-02; 997, 991 and 1024 in the runs V1, V2 and V4 of 2026-10-07, on a fully loaded machine). **The exit code is 0.**

With `--verbose`, 33 lines `cell <n> time=<seconds> failed=False messages=0` come first. In runs R3 and V4 they came before the 145 lines, which were otherwise the same. The two slow cells are cell 20 (the complete spectrum of the self-consistent potential: 472 s in R3, 789 s in V4) and cell 13 (the 2818 levels of the free spectra: 76 s in R3, 132 s in V4); Part 6 lists the others.

### 4.2 The meaning of the most important numbers

* `check_count=94`, `failed_check_count=0`: all 94 notebook checks are true.
* `measurement_theoryPackageCheckCount=125`: the exact theory package passed its 125 checks.
* `measurement_freeSpectraLevelCount=2818` and `measurement_freeSpectraMaxAbsDeviation=1.1656222653755322e-9`: 2818 Rust energy levels were recomputed with `NDSolve`, and the largest difference is 1.2e-9 (in units of the mass m; the tolerance is 1e-8). The worst level of each file differs from a 32-digit reference by at most 4.1e-13 in the notebook and 1.2e-9 in Rust, so the small differences come from the Rust side.
* `measurement_scfEnergy=-0.007830391951227303` and `measurement_scfEnergyDeviation=3.3831808882167635e-12`: the self-consistent ground-state energy E_0 of N = 8 particles agrees with Rust to 3.4e-12.
* `measurement_scfSpectrumLevelCount=788`, `measurement_scfSpectrumShells=182`, `measurement_scfSpectrumMaxAbsDeviation=5.440079497986972e-10`: the complete spectrum of the self-consistent potential agrees with Rust to 5.4e-10.
* `measurement_zeroModeSplittingC_m1_H1_L3=1.9051482536448665`: the exact coefficient c = 2/(1 + e^{-3}).

### 4.3 The output files and how to check them

The report and the 6 figures of Part 2.3 are rewritten; with Wolfram 15.0.1 on Windows they have exactly the fingerprints listed there. The report's summary keys are `"checkCount": 94`, `"failedChecks": []` and `"verdict": "SUCCESS"` (Part 3.9 shows commands that print them). Its key `figures` lists the 6 PNG files, and its key `sourceSha256` lists the 18 inputs of Part 2.2 with their fingerprints. You can open the PNG files in any image viewer: they show the free spectrum (Rust as dots, `NDSolve` as lines), the k = 0 box levels against L, the self-consistent pseudo-potential and densities, the convergence of both self-consistent loops, and a bar chart of the digits of agreement of each comparison.

### 4.4 Run time and memory

**Run time.** All times are wall-clock times on the verification machine (24 cores, Windows 11), which was never idle: parallel verification jobs of the same project were running.

* 2026-10-02 (Part 6.1): 658.9 s (R1) and 676.3 s (R2), about 11 minutes, with 9 to 11 other Wolfram kernels running and an average CPU load of 89.5 % and 94.6 % during the two runs. The further runs took 596.1 s (R3) and 593.6 s (R4), which ran at the same time as each other, and 731.0 s (R5).
* 2026-10-07 (Part 6.2): 1009.3 s (V1) and 1006.4 s (V2), about 17 minutes, with 4 to 18 Wolfram kernels on the machine (this run's and other jobs') and an average CPU load of 100 % (every core busy) during both runs. The further runs took 1020.3 s (V3, without a working Rust program) and 1040.5 s (V4), both at the same time as V1 and V2.

On an idle machine the run is expected to be faster than 11 minutes (not measured). The time is spent almost entirely in two cells (Part 4.1).

**Memory.** The Wolfram kernel `wolfram.exe` reached a peak working set of 560.7 MB (R1), 561.5 MB (R2) and 563.0 MB (R3) on 2026-10-02, and 557.9 MB (V1), 558.1 MB (V2), 574.2 MB (V3) and 562.5 MB (V4) on 2026-10-07. The other processes of a run were much smaller (Part 5).

### 4.5 Other Wolfram versions and other platforms

Only Wolfram 15.0.1 on Windows 11 was tested, and it reproduces the committed files exactly. On macOS or Linux the report differs at least in `engine.binary` (the program has no `.exe` there), and another platform or Wolfram version may compute floating-point numbers that differ in the last digits and may draw the figures with other fonts, so the bytes may differ while all 94 checks still pass. The checks, not the bytes, decide whether the run is correct. The Stage-4 gate of the repository therefore ignores the key `engine.binary` when it compares the report.

## 5. Side effects

* **Overwritten in the repository (committed files):** `artifacts/dirac16complex/kohn-sham/mathematica-report.json` and the 6 files `artifacts/dirac16complex/kohn-sham/figures/mathematica/*.png`. They are rewritten in every run that gets that far, also when checks fail: their modification times change. With Wolfram 15.0.1 on Windows the bytes stay the same and `git status` stays empty. A run that **fails** writes a report with `"verdict": "FAILURE"` over the committed one (measured in run R4 of Part 6.1 and run V3 of Part 6.2). Any change you made to these files yourself is lost.
* **Created in the repository:** nothing else. The folder `figures/mathematica` is created only if it is missing. After every successful run, `git status --porcelain --untracked-files=all` printed nothing, and `git status --porcelain --untracked-files=all --ignored` listed only the folders made by Part 3.6 and 3.7, `vendor/rustSolveIt/` and `studies/dirac16complex_kohn_sham/target/`. The notebook file is only read, never written. The Rust program's `print-config` writes no file.
* **Created by the preparation (Parts 3.6 and 3.7), ignored by Git:** `vendor/rustSolveIt/` (about 84 MB) and `studies/dirac16complex_kohn_sham/target/` (about 18 MB).
* **Temporary files.** The set leaves no file in the temporary folder: in run R3 (2026-10-02) and in runs V1 to V4 (2026-10-07) the temporary folder of the run (the variable `TEMP`, which the kernel uses as `$TemporaryDirectory`) was a private, empty folder, and it was still empty after the run. On Windows, while it runs, WolframScript keeps the relayed console output in a temporary file in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\` (named `tmp_` plus 10 random characters); other WolframScript jobs used the same folder at the same time, so these files could not be attributed to this run one by one. The hidden notebook front end appended 25 lines to its log file `%LOCALAPPDATA%\Wolfram\Logs\FrontEnd\system.log`: its version, its command line, the folders it uses (among them the folder of your clone) and 9 start-up lines `[info] [Startup] ...` (counted on 2026-10-07 for the front ends of V1, V2 and V3). None of these files belongs to the repository.
* **Processes.** One `wolframscript.exe` (17 MB) first starts a short licence-check kernel, `wolfram.exe -wlbanner -licenseinfo` (54 to 67 MB; seen only at the start of runs V1, V3 and V4 of 2026-10-07, and too short-lived to be caught in V2), and then the Wolfram kernel, `wolfram.exe -runfirst ... -linkmode Connect ...` (peak 558 to 574 MB), which runs for the whole run. The kernel starts two converter helpers, `NBImport.exe` (15 MB, to read the notebook) and `XML.exe` (14 MB). In the last 10 to 20 seconds of the run, the PNG export starts a hidden notebook front end, `WolframNB.exe /b /min -server ...` (137 to 160 MB), which starts a sandboxed kernel `wolfram -pacletreadonly -sandbox -noinit ...` (127 MB) and a console host `conhost.exe` (7 MB). The kernel also starts the Rust program `dirac16complex_kohn_sham.exe print-config` for less than a second. All of them end with the run.
* **Network.** The set itself makes no network access. During R1, R2 and R3 (2026-10-02) and V1 to V4 (2026-10-07) the processes of the run were polled about once a second for TCP connections: R1, R3 and V1 to V4 showed none, and R2 showed only connections of the kernel to the local computer itself (`127.0.0.1`, two established connections and one bound socket `0.0.0.0:0`). Wolfram's helper processes talk to the kernel through shared memory (`-linkprotocol "SharedMemory"` in their command lines). No connection to another computer was seen. WolframScript or the kernel may contact Wolfram's licence server, for example when the free Engine renews its licence.
* **Restoring the committed state:**

  ```
  git checkout -- artifacts/dirac16complex/kohn-sham/mathematica-report.json artifacts/dirac16complex/kohn-sham/figures/mathematica
  ```

  To remove what the preparation created: Windows PowerShell `Remove-Item -Recurse -Force vendor/rustSolveIt, studies/dirac16complex_kohn_sham/target`; macOS and Linux `rm -rf vendor/rustSolveIt studies/dirac16complex_kohn_sham/target`. Both commands were tested, on 2026-10-02 and again on 2026-10-07: the `git checkout` command after the failed runs R4 and V3 (all 7 fingerprints were the committed ones again, and `git status --porcelain --untracked-files=all` printed nothing), and the PowerShell removal command in clone D (2026-10-02) and clone C (2026-10-07) (afterwards `git status --porcelain --untracked-files=all --ignored` printed nothing).

## 6. Verification record

The set was verified twice, from fresh clones each time: first on 2026-10-02 (Part 6.1, runs R1 to R5 and E1, E2), and again on 2026-10-07 (Part 6.2, runs V1 to V6), after the verification workflow had been interrupted by a session limit and restarted; the second verification re-checked every statement of this file that it could measure instead of trusting the first one. Both found the same: the set executes correctly, all 94 checks pass, and the 7 outputs are byte-identical to the committed ones.

### 6.1 First verification (2026-10-02)

* **Date:** 2026-10-02.
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of `main` on https://github.com/once-ere/Dirac_claude.git when the fresh clones were made (checked with `git ls-remote`). The two files of the set and the 7 committed outputs were last changed in commit `eac67e6` (2026-09-30); the 18 inputs were last changed between 2026-09-25 and 2026-09-26 (commits `78b4a5f`, `4718e9c`, `fbec4d7`, `6c0bfad`, `34b9fd4`, `e1904bb`, `5b0702a`, `328306f`), before that commit. Four fresh clones (A, B, C, D) were made in a scratch folder outside the working tree. **No uncommitted file was copied into any clone**: the set needs none (the uncommitted changes of the working tree on that day concern other files, which this set does not read).
* **Environment:**
  * Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 cores;
  * Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence; WolframScript 1.14.0;
  * Rust: `cargo 1.91.1 (ea2d97820 2025-10-10)`, `rustc 1.91.1 (ed61e7d7e 2025-11-07)`, toolchain `stable-x86_64-pc-windows-msvc`; the engine `vendor/rustSolveIt` at the pinned commit `a8fdff459adfe181573d7924b18bffbdf378fdb3` (Windows 11 engine);
  * PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444, Git 2.51.2.windows.1 with its Git Bash.

  Python 3.14.5 was used only for the measurement helpers (fingerprints, comparisons of the printed lines), not by this set.
* **Preparation of the clones** (Parts 3.6 and 3.7):

  | Clone | Engine download | Build of the Rust program | Used for |
  | --- | --- | --- | --- |
  | A | `pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`: `solver_setup=OK`, 6.9 s | PowerShell 7.6.6: exit 0, 14.5 s; `print-config` ends with `SUCCESS` | R1, R2 |
  | B | the same: `solver_setup=OK` | PowerShell 7.6.6: exit 0, 13.4 s; `print-config` ends with `SUCCESS` | R3 |
  | C | none before R4; after R4: `bash scripts/setup_solver.sh` in Git Bash: `solver_platform=win11`, `solver_setup=OK`, 4.8 s | after R4, in Git Bash: exit 0, 7.7 s; `print-config` ends with `SUCCESS` | R4 (without engine and program), R5 |
  | D | Windows PowerShell 5.1: `.\scripts\setup_solver.ps1 -Platform win11` gave `solver_setup=OK`; then the exact command of Part 3.6 gave `solver_setup=ALREADY-PRESENT`, exit 0 | Windows PowerShell 5.1: exit 0, 11.7 s; `print-config` ends with `SUCCESS` | E1, E2 |

* **How the runs were made.** All runs were started from the repository root of a fresh clone. R1 to R3 were started from PowerShell 7.6.6 with `Start-Process` (standard output and standard error redirected to files) and watched: every second the script listed every process under `wolframscript.exe`, their peak working sets and their TCP connections, and every 10 seconds the CPU load of the machine. R3 was given a private, empty folder as `TEMP` and `TMP` (the kernel uses it as `$TemporaryDirectory`; this was checked). R4 and R5 were started from Git Bash and timed with `time`. "Identical" means byte-identical to the committed file of Part 2.3. During all runs other verification jobs of the same project were running on the machine (8 to 11 other Wolfram kernels).

  | Run | Clone | Shell | Command (after `wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls`) | Exit | Last line | Checks | Wall time | Peak kernel memory | Report | 6 figures |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | R1 | A | PowerShell 7, watched | (nothing: the default) | 0 | `=OK` | 94 of 94 true | 658.9 s (script: 657 s), CPU load 89.5 % | 560.7 MB | identical | identical |
  | R2 | A | PowerShell 7, watched | (nothing: the default) | 0 | `=OK` | 94 of 94 true | 676.3 s (script: 670 s), CPU load 94.6 % | 561.5 MB | identical, and identical to R1 | identical, and identical to R1 |
  | R3 | B | PowerShell 7, watched, private TEMP | `-- notebooks/Dirac16ComplexKohnSham.nb --verbose` | 0 | `=OK` | 94 of 94 true | 596.1 s (script: 592 s), CPU load 89.2 %, at the same time as R4 | 563.0 MB | identical | identical |
  | R4 | C, without engine and without the Rust program | Git Bash | (nothing: the default) | 1 | `=FAILED` | 84 of 94 true | 593.6 s (script: 590 s), at the same time as R3 | not measured | rewritten with `"verdict": "FAILURE"` (35 lines inserted, 24 deleted) | identical |
  | R5 | C, after engine download and build | Git Bash | (nothing: the default) | 0 | `=OK` | 94 of 94 true | 731.0 s (script: 728 s); the 145 lines appeared only at the end | not measured | identical | identical |
  | E1 | D | Git Bash | `notebooks/NoSuchNotebook.nb` | 2 | `=FAILED` after `ERROR: missing notebook: <path>` | none | 3.5 s | not measured | not written | not written |
  | E2 | D | Git Bash | `notebooks/Dirac16ComplexDarkSector.nb` (the Stage-3 notebook) | 1 | `=FAILED` after `ERROR: expected 33 input cells, found 37` | none | 3.9 s | not measured | not written | not written |

  **The two runs that the task asks for are R1 and R2.** They were made in the same fresh clone A, one after the other. Both printed the 145 lines of Part 4.1, both exited with code 0, and after each of them all 7 output files were byte-identical to the committed ones; so the outputs of R2 are also byte-identical to those of R1 (this was also checked directly, file by file). The standard output of R1, R2, R3 and R5 was the same 145 lines apart from `report=` and `elapsed_seconds=` (R3 printed the 33 `cell` lines of `--verbose` before them). Standard error was empty in every run.

  After R1, R2, R3 and R5, `git status --porcelain --untracked-files=all` printed nothing, and `git status --porcelain --untracked-files=all --ignored` listed only `vendor/rustSolveIt/` and files under `studies/dirac16complex_kohn_sham/target/`. After R4 it printed ` M artifacts/dirac16complex/kohn-sham/mathematica-report.json`; `git checkout -- artifacts/dirac16complex/kohn-sham/mathematica-report.json artifacts/dirac16complex/kohn-sham/figures/mathematica` restored the committed bytes (all 7 fingerprints checked), and R5 then ran in the same clone. After R3 the private TEMP folder was empty. After E1 and E2, `git status --porcelain` printed nothing.
* **R4 in detail (the most likely mistake: running the set without building the Rust program).** All cells ran; the cell `print-config` found no program, so the 10 checks `engine_binaryFound`, `engine_exitCodeZero`, `engine_lastLineSUCCESS`, `engine_printedFixtureHashMatches`, `engine_printedTolerancesMatchSummaries`, `engine_printedRealSystemIsDerivedForm`, `engine_printedBoundaryConditionsAreDerived`, `engine_printedExchangeClosedFormAndPotentials`, `engine_printedPseudoPotentialIsHartreePlusExchange` and `engine_printedMixingMatchesRun` were false (only `engine_summariesRecordFixtureHash` stayed true). The script printed `failed_check_count=10`, `failed_evaluation_count=1`, `message_count=0`, `failed_cells=33` (the last cell returns a `Failure` object when a check is false), `failed_checks=engine_binaryFound,...` and `dirac16complex_ks_mathematica_notebook=FAILED`, 147 lines in total, and exited with code 1. All 43 measurements were the same as in R1. The report was overwritten: `"exitCode": -1`, `"lastLine": ""`, the 10 checks false, `"failedChecks"` with the 10 names, `"verdict": "FAILURE"`; the figures were rewritten with the committed bytes.
* **Per-cell run times** (R3, `--verbose`; the machine was busy, and R4 ran at the same time): cell 20 (the complete spectrum of the self-consistent potential, 788 levels in 182 shells) 471.9 s; cell 13 (the 2818 levels of the six free spectra) 76.0 s; cell 24 (the first figure, which starts the hidden front end) 10.3 s; cell 2 (the 125 checks of the exact theory package) 9.5 s; cell 14 (the 32-digit reference levels) 7.9 s; cell 18 (the self-consistent loop, 20 iterations) 6.0 s; cell 10 (the exact box levels) 5.1 s; every other cell under 1.5 s. The `--verbose` lines print these times as `Round[t, 0.01]`, so some appear as `0.8300000000000001`, `6.` or `0.`.
* **Check counts:** 94 notebook checks (in the groups of Part 1.3), all true in R1, R2, R3 and R5; 84 of 94 in R4, as designed. The 33 Input cells evaluated without a message and without a failure in every successful run.
* **Fix made:** none. The set executed correctly as committed; no file of the set was changed.
* **Open discrepancies:** none. No number differed from the committed report.

  Two notes about the command line, both measured with a three-line test script on 2026-10-02:
  * The comments of the Stage-4 gate, and line 23 of this script's own header (`(WolframScript 1.14 drops arguments after "--": pass the path positionally.)`), say that WolframScript 1.14 drops `--` and every argument after it. That is true only for a script **without** the first line `#!/usr/bin/env wolframscript`. This script has that line, so WolframScript passes `--` and the arguments after it (`{"<script>", "--", "x.nb", "--verbose"}` in `$ScriptCommandLine`), in PowerShell 7.6.6, Windows PowerShell 5.1 and Git Bash, and the script ignores the `--` (R3).
  * Without `--`, the argument `--verbose` is also read by WolframScript as its own option: it then prints `Performing '-file' parsing. File-><script>`, `Local Evaluation` and `Using wolfram.exe at:"<path>"` on standard error, in addition to passing `--verbose` to the script. This is why Part 3.8 recommends `-- --verbose`.
