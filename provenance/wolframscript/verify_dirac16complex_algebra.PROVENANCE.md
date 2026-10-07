# Provenance: the WolframScript set `verify_dirac16complex_algebra` (old Stage 1, exact algebra)

| Item | Value |
|---|---|
| Set | `scripts/verify_dirac16complex_algebra.wls` with the package `wolfram/Dirac16ComplexAlgebra.wl` |
| Verdict | EXECUTES OK: exit code 0, `check_count=21`, `failed_check_count=0` |
| Reproduction | byte-identical to the committed report (sha256 `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7`) in all 8 runs with the reference folder `dirac-main/` present, in all 15 compared runs of the re-verification after review, and in every run with `dirac-main/` present of the re-verification of 2026-10-07 (Part 6); without it the report differs in exactly 13 lines, all caused by the missing folder (Part 4.3) |
| Run time | 12.1 to 13.4 s wall clock per run in the five timed runs of 2026-10-02 (the script itself reports `elapsed_seconds=9` or `10`); 16.9 to 19.0 s (`elapsed_seconds` 12 to 14) in the four timed runs of 2026-10-07, when 13 to 18 other Wolfram kernels kept the processor 100 % busy; overall about 11 to 22 s (`elapsed_seconds` 8 to 16) (Part 4.4) |
| Verified | 2026-10-02, commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`; re-verified 2026-10-07, commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (the files of the set are the same in both); Windows 11, WolframScript 1.14.0, Wolfram 15.0.1 |

This file is written for a student who has never used Wolfram software. Parts 1 to 6 explain what the set is, its files, how to run it, what it prints and writes, what else it changes on your computer, and how it was verified.

## 1. What this set is and what it computes

### 1.1 In plain words

The author's theory describes a field with 16 complex components (a "spinor") on an 8-dimensional space-time whose metric has 4 plus signs and 4 minus signs, eta = diag(+1,+1,+1,+1,-1,-1,-1,-1). The field is built from eight 16 by 16 matrices gamma^0, ..., gamma^7 (the "gamma matrices"; in the author's Mathematica notebook they are called `T16^A[0]` ... `T16^A[7]`). Everything later in the theory (the Lagrangian, the field equations, the quantization) uses these matrices and a few matrices made from them.

This set builds all of these matrices from scratch and proves 21 statements about them. Every proof is an exact computation with whole numbers, fractions and complex numbers whose real and imaginary parts are fractions; no decimal (floating point) number is used anywhere, so a "true" result is a proof for the finite statement checked, not an approximation. Linear algebra questions (for example "which matrices commute with all eight gammas?") are answered by computing the exact null space of an integer matrix.

The script `scripts/verify_dirac16complex_algebra.wls` loads the package `wolfram/Dirac16ComplexAlgebra.wl`, runs every check, compares the result with an independent exact data file written by a separate Python program (`artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`), compares with three data files of the separately published reference project dirac-main when that folder is present, writes one JSON report and prints one line per check and per measurement.

Matrices used below: C = gamma^0 gamma^1 gamma^2 gamma^3 (the adjoint matrix, Psibar = Psi^dagger C, which is also the charge-conjugation matrix calC_+, Part 1.3); S^{ab} = (1/4)[gamma^a, gamma^b] (the 28 generators of Spin(4,4)); gamma^8 = gamma^0 gamma^1 ... gamma^7 (the chirality matrix); P_-/+ = (I -/+ gamma^8)/2; B = -i C gamma^4 (the matrix of the equal-time anticommutator).

### 1.2 The 21 checks

| # | Check | What it proves (plain words) |
|---|---|---|
| 1 | `ALG_clifford` | The eight integer 16 by 16 matrices satisfy gamma^a gamma^b + gamma^b gamma^a = 2 eta^{ab} I16 for all 64 pairs; the squares are +1 (a = 0..3) and -1 (a = 4..7). |
| 2 | `ALG_gammaTransposeSymmetry` | gamma^0..gamma^3 are symmetric matrices, gamma^4..gamma^7 are antisymmetric. |
| 3 | `ALG_chargeMatrix` | C = gamma^0 gamma^1 gamma^2 gamma^3 equals diag(-sigma, sigma), is symmetric, C^2 = I16, has eigenvalues -1 (8 times) and +1 (8 times); characteristic polynomial (x-1)^8 (x+1)^8. |
| 4 | `ALG_expression1` | The notebook expression `\[Sigma]16.(T16^A)[#]==-Transpose[\[Sigma]16.(T16^A)[#]]&/@Range[0,7]` (`\[Sigma]16` is the notebook's sigma16 = C) gives eight times `True`. The notebook's own definition cells (stored as text inside the package, not read from the .nb file) are evaluated verbatim in an isolated context, in two ways of reading the notation `T16^A`, and their matrices are compared with the package's. |
| 5 | `ALG_spinTransposeProperties` | C S^{ab} is antisymmetric, C {gamma^c, S^{ab}} is symmetric and C [gamma^c, S^{ab}] is antisymmetric, for all index values (the transpose properties the Lagrangian needs); the so(4,4) commutation relations are also recorded. |
| 6 | `ALG_chirality` | gamma^8 = diag(-I8, +I8), (gamma^8)^2 = I16, gamma^8 anticommutes with every gamma^a and commutes with every S^{ab} and with C. |
| 7 | `ALG_faithful` | The 256 ordered products of distinct gammas are linearly independent (rank 256); the 128 even products have rank 128. |
| 8 | `ALG_pinIrreducibleComplex` | Only multiples of the identity commute with all eight gammas (commutant dimension 1), so C^16 is an irreducible complex module of Pin(4,4). |
| 9 | `ALG_spinDecomposition` | Under Spin(4,4), C^16 splits into two irreducible, inequivalent 8-dimensional pieces (chirality -1: components 0..7; chirality +1: components 8..15). |
| 10 | `ALG_cliffordPictureIntertwiner` | There is exactly one (up to a factor) matrix K_clifford with gammaHat^a K = K gamma^a, where gammaHat^a are dirac-main's tensor-product gammas; it is an invertible integer matrix (rank 16) and K C K^-1 = C_dm. With `dirac-main/` present, dirac-main's stored generators and volume element are also compared. |
| 11 | `ALG_octonionPictureIntertwiner` | The split octonions are built from Zorn data (unit law, worked products, the associator (e1 e2) e4 - e1 (e2 e4) = 2 e7, norm = eta quadratic form, the norm is multiplicative, conjugation reverses products, 64 nonzero structure constants); gammas built from octonion multiplication satisfy the same Clifford relations; the intertwiner to the notebook gammas is unique and invertible. With `dirac-main/` present, the multiplication tensor, the octonion Clifford generators and dirac-main's canonical intertwiner are also compared. |
| 12 | `ALG_chargeFormB` | B = -i C gamma^4 is Hermitian, B^2 = I16, eigenvalues -1 (8 times) and +1 (8 times), B commutes with C and B C = -i gamma^4. |
| 13 | `ALG_invariantForms` | The Spin(4,4)-invariant bilinear forms are exactly the combinations of C P_- and C P_+; for every invariant Hermitian form the charge-density matrix has eigenvalues +\|k\| (8 times) and -\|k\| (8 times): it is indefinite unless it is zero. |
| 14 | `ALG_gamma8Map` | The real matrix map Psi -> gamma^8 Psi turns the free Lagrangian with mass m into minus the Lagrangian with mass -m; with a self-coupling (lambda/2) S^2 the sign of lambda flips as well. |
| 15 | `ALG_pinLiftCharacter` | For Psi -> u Psi with a unit vector u, Psibar Psi -> -n(u) Psibar Psi (n(u) = +1 or -1 is the norm of u); the sign of the kinetic term for both lifts of the vector action; for products of two vectors the sign is the spinor norm. |
| 16 | `QNT_curvedAnticommutatorMatrix` | (C gamma^4)(gamma^4 C) = g^44 I16 for an arbitrary symbolic vielbein, so (C gamma^4)^-1 = gamma^4 C / g^44; checked also at three exact rational points of a general non-diagonal test vielbein and for the primordial field, where i (C gamma^4)^-1 = B. |
| 17 | `QNT_flatModeHamiltonian` | For the flat-space mode Hamiltonian h_k = -i m gamma^4 - gamma^4 sum_j k_j gamma^j: h_k^2 = (m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 - k7^2) I16; its anti-Hermitian part and its commutator with B are given exactly. |
| 18 | `QNT_kreinSignature` | B maps each 8-dimensional frequency eigenspace of the flat mode Hamiltonian into itself and squares to the identity there; the form defined by B has signature (4,4) on the rest-frame positive-frequency space (required by the check) and also, as measured, on the rest-frame negative-frequency space and on the three eigenspaces of two moving examples. |
| 19 | `QNT_unitaryAndKreinSubgroups` | Exactly 13 of the 28 S^{ab} commute with B; exactly 9 commute with B and are anti-Hermitian (Spin(4) x Spin(3)); the 21 with a, b different from 4 are Krein-unitary, the 7 S^{4b} are not. (The older claim "exactly 9 commute with B" is false and is recorded as such.) |
| 20 | `QNT_currentHermiticity` | The current matrices -i C gamma^mu are Hermitian and -i C gamma^4 = B. |
| 21 | `ALG_fixtureAgreement` | All 75 matrices in the independent Python data file `algebra-fixture.json` equal the matrices built here (75 agree by name, 0 disagree, 0 unmatched). |

### 1.3 A note on charge conjugation

Every gamma^a here is a REAL matrix, so plain complex conjugation Psi -> Psi* does nothing to a real field and cannot be charge conjugation. Charge conjugation is a MATRIX: a matrix calC acts as Psi^c = calC C Psi* (with C^T = C), and the matrix calC_+ that keeps the mass is defined by calC_+^-1 gamma^a calC_+ = -(gamma^a)^T for every a.

This set proves that C itself is that matrix. Check 3 proves C^T = C and C^2 = I16, so C^-1 = C (report keys `ALG_chargeMatrix.symmetric` and `ALG_chargeMatrix.squareIsIdentity`, both `true`). Check 4 proves (C gamma^a)^T = -C gamma^a for a = 0..7 (`ALG_expression1.list`, eight times `true`). Together these give C^-1 gamma^a C = -(gamma^a)^T. So C is the charge-conjugation matrix calC_+ as well as the adjoint matrix of Psibar = Psi^dagger C. This is why the package's usage text calls C "the charge/adjoint matrix", and why its fixture alias table also accepts the names `charge`, `chargematrix` and `chargeconjugation` for it. With calC_+ = C the charge conjugate is Psi^c = calC_+ C Psi* = C^2 Psi* = Psi*. For a REAL field calC_+ therefore acts as the identity: a real field is its own charge conjugate and carries no U(1) charge.

The nontrivial real matrix map is calC_- C = gamma^8, where calC_- = gamma^8 C is the second charge-conjugation matrix (calC_-^-1 gamma^a calC_- = +(gamma^a)^T). It is the map Psi -> gamma^8 Psi, and it reverses the mass. This set checks the properties of gamma^8 that make the map work. Check 6 proves gamma^8 = diag(-I8, +I8) (a real matrix), (gamma^8)^2 = I16, and that gamma^8 anticommutes with every gamma^a and commutes with C and with every S^{ab}. Check 14 proves the resulting map of the Lagrangian, L_m[gamma^8 Psi] = -L_{-m}[Psi], with lambda -> -lambda for the self-coupling. The relation calC_-^-1 gamma^a calC_- = +(gamma^a)^T follows from checks 3, 4 and 6, but the set does not record it as a value of its own. Nor does the set treat the quantised field. Because the gammas are real, the condition M (gamma^a)* = s gamma^a M on a charge-conjugation matrix reads M gamma^a = s gamma^a M. Check 8 (only multiples of I16 commute with every gamma^a) together with check 6 then leaves only M = I16 (s = +1, giving calC_+ = C) and M = gamma^8 (s = -1, giving calC_- = gamma^8 C), up to a factor.

The full construction is in `Revision/lead_checks/charge_conjugation_and_u1.py`. It solves for every such M exactly and builds both charge-conjugation matrices, their action on the bilinears, the quantised Grassmann field (where only M = gamma^8 preserves the anticommutator) and U(1) charge conservation. It gave 12 checks, all PASS, on 2026-10-02 at commit `c2b33cc`. Its gamma^(x1) ... gamma^(x7) are this set's gamma^1 ... gamma^7 and its gamma^(x8) is this set's gamma^0. Its C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) and its Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) are therefore exactly this set's C and gamma^8, which was checked exactly against `Revision/algebra/gammas.json` and `algebra-fixture.json`.

### 1.4 Documents and programs that use its results

- The Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (with its `.tex` and `.pdf`): Section 1.1 (list of reports), Section 3 (the Clifford module, charge matrix, expression [1], chirality and the intertwiners; its verification record 3.4), Section 4 (irreducibility and the Spin(4,4) decomposition), Section 7.7 (the chirality map and the Pin characters), Section 10 (canonical quantization: B, Krein structure, modes, symmetries, current), Section 11 (11.1 lists this set and its 21 checks, 11.7 records the report's sha256), Section 12 (reproduction commands).
- The earlier textbook `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (with `.tex` and `.pdf`) and its chapter sources `provenance/textbook/chapters/`: chapters 00 (claims table), 02 (Clifford algebras and spinors), 03 (split octonions), 04 (curved space), 05, 08 (quantization), 18 (open problems), 19 (reproducing everything; its step `stage1-03-wolfram-algebra`), 20 (check index).
- `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (with `.tex` and `.pdf`), which cites `QNT_currentHermiticity` and `ALG_gamma8Map` and records the report's sha256.
- Programs that read the report or record its sha256: `scripts/check_dirac16complex_algebra.py` (writes `python-algebra-report.json`, field `wolframReportSha256`), `scripts/build_stage1_summary.py` (`stage1-summary.json`), `scripts/verify_dirac16complex00.wls` with `wolfram/Dirac16Complex00.wl` (`artifacts/dirac16complex/pair-creation/`), `wolfram/Dirac16ComplexMatterAntimatter.wl` (`artifacts/dirac16complex/matter-antimatter/`), the Stage-1 gate `scripts/verify_stage1_arbitrary_field.sh` / `.ps1`, `scripts/verify_stage1_public_clone_audit.py` and the tests in `tests/`.
- The provenance files `provenance/wolframscript/verify_dirac16complex00.PROVENANCE.md` and `provenance/wolframscript/verify_dirac16complex_matter_antimatter.PROVENANCE.md`, which record the report's sha256 as an input of those sets.
- Programs that load the PACKAGE `wolfram/Dirac16ComplexAlgebra.wl` (not the report): `scripts/build_dirac16complex_mathematica_notebook.wls` and the Mathematica notebook it builds, `notebooks/Dirac16ComplexDarkSector.nb` (described in `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md`, `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` and the provenance files `build_dirac16complex_mathematica_notebook.PROVENANCE.md` and `verify_dirac16complex_mathematica_notebook.PROVENANCE.md` in `provenance/wolframscript/`). `handoff/tools/WOLFRAMSCRIPT_PROVENANCE.md` cites the check `ALG_clifford` of the report as the shipped proof of the Clifford relations.

### 1.5 The eight real 16 by 16 Dirac matrices are the author's

The provenance file `provenance/dirac matrices.md` displays the author's eight real 16 by 16 Dirac matrices `T16A[0]` ... `T16A[7]`, evaluated directly from the author's notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` and stored in `provenance/dirac_matrices/author_notebook_T16.json` (sha256 `b4bdec86878f11d874e276bd30e3a9ca6ae0d607368dafabd71bde7e8e2de334`). On 2026-10-07 the matrices of this set's package were compared with that file exactly, entry by entry (Wolfram `===` on integer arrays), in clone A of Part 6:

| Package (this set) | Author's notebook (`author_notebook_T16.json`) | Equal |
|---|---|---|
| `D16Gammas` = gamma^0 ... gamma^7 | `T16A[0]` ... `T16A[7]` | yes, all eight |
| `D16C` = C | `sigma16` | yes |
| `D16Chirality` = gamma^8 | `T16A_8` = `T16A[0]` ... `T16A[7]` | yes |
| 2 `D16ProjMinus` = I - gamma^8 | `twice_PL` = 2 P_L | yes |
| 2 `D16ProjPlus` = I + gamma^8 | `twice_PR` = 2 P_R | yes |
| `D16Eta` | `eta4488` | yes |

All entries of the eight gammas are -1, 0 or +1, so they are real. This set therefore computes with exactly the author's eight real 16 by 16 matrices. In the report: check 1 (`ALG_clifford`) proves the anticommutation relations with eta = diag(+1,+1,+1,+1,-1,-1,-1,-1) and `ALG_clifford.integerEntries` = `true`; the measurement `ALG_spinTransposeProperties.supplementaryLieRelationsHold` = `true` records that the 28 S^{ab} = (1/4)[gamma^a, gamma^b] satisfy the so(4,4) commutation relations (recorded, not part of the pass condition of check 5); check 7 proves that the 256 products are linearly independent; and check 8 proves that C^16 is an irreducible complex module of Pin(4,4). The comparison program was a scratch file, not part of the repository. Its whole content is the `Get` of the package, an `Import` of the JSON file and the six comparisons of the table.

## 2. Files

### 2.1 Programs of the set

| File | Role | sha256 | Lines | Bytes |
|---|---|---|---|---|
| `scripts/verify_dirac16complex_algebra.wls` | the script you run | `86904ac07e1237cf0dec14431a3707d7bf24f951e12def504705d331c934949a` | 134 | 6427 |
| `wolfram/Dirac16ComplexAlgebra.wl` | the package it loads (context ``Dirac16Complex`Algebra` ``) | `ba0d00c818fa3707f04f7b2a7478b0c635fbf9fdaaa08b2e036d2704180f2262` | 1299 | 82215 |

Both files were last changed in commit `6c0bfad` (2026-09-25). The script records both hashes in its report (`sourceSha256`), so any edit to either file changes the report.

### 2.2 Inputs it reads

| File | Required? | sha256 | Lines | Bytes | Origin |
|---|---|---|---|---|---|
| `wolfram/Dirac16ComplexAlgebra.wl` | yes (exit code 2 without it) | as above | 1299 | 82215 | this repository |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | no; without it check 21 is skipped and `check_count=20` | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 18440 | 213133 | committed; written by `scripts/build_dirac16complex_fixture.py` |
| `dirac-main/artifacts/exact/cl44-seed.json` | no; without it the comparisons are recorded as `"not-run"` | `52e7a73b14467435d7986b33bf29547510b321853ffbd76121896d70b796d133` | 3355 | 23366 | https://github.com/once-ere/dirac, commit `a21f593a464cf85e90e9271f2ace4df67f50d68e` |
| `dirac-main/artifacts/exact/split-octonion.json` | no (as above) | `cbc28db6709ec1fc35ccfcc26353d1952b42bb516f6c50d6a52e2d6d355be710` | 1533 | 10722 | same |
| `dirac-main/artifacts/exact/triality44.json` | no (as above) | `a8c31c07809fc884ae0495d91f4105fac0909c954bb185c643306c57699cd395` | 41675 | 295953 | same |

The folder `dirac-main/` is NOT part of this repository (it is listed in `.gitignore`), so a fresh clone does not contain it. The three hashes above are those of the files with LF line endings, exactly as stored in the dirac repository. The script also hashes itself. It does not open the author's Mathematica notebooks; the notebook cells it evaluates for check 4 are stored as text inside the package.

### 2.3 Outputs it writes

| File | When | sha256 of the committed file | Lines | Bytes |
|---|---|---|---|---|
| `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` | every run with the documented command (it is OVERWRITTEN) | `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7` | 2638 | 49440 |

The report path is the first argument; a second optional argument replaces the fixture path. Instead of arguments you may set the environment variables `DIRAC16_ALGEBRA_REPORT` and `DIRAC16_ALGEBRA_FIXTURE`. Without either, the report goes to the committed path above. No other file is written. The printed lines (Part 4.1) go to the terminal only.

## 3. How to execute it

Everything you need is in this part. Commands are shown for Windows (PowerShell), macOS (Terminal) and Linux (a terminal with bash). Type each command on one line and press Enter.

How to open the terminal window in which you type the commands:

- Windows: open the Start menu, type `PowerShell` and click "Windows PowerShell" (or "PowerShell 7" if you installed it, or "Terminal").
- macOS: press Command+Space to open Spotlight, type `Terminal` and press Enter.
- Linux: press Ctrl+Alt+T (Ubuntu and most desktops), or open "Terminal" from the applications menu.

### 3.1 What you need

- A computer with Windows 10/11, macOS or Linux, about 1 GB of free memory (the run uses about 0.43 GB) and about 1 GB of free disk space (a clone of the repository took 520 MB on 2026-10-02 and 667 MB on 2026-10-07, and `dirac-main/` 27 MB).
- An internet connection for installing the software and downloading the repository (the run itself needs none).
- Git (to download the repository).
- Wolfram Engine (free for developers and students) or Mathematica, together with the command-line program `wolframscript`. The set was verified with Wolfram 15.0.1 and WolframScript 1.14.0.
- Optional: Python 3 (any recent version; 3.14.5 was used) only for the one-line check of the report in Part 4.3. No Python package needs to be installed for it.

### 3.2 Install Git

- Windows: download "Git for Windows" from https://git-scm.com/download/win and run the installer with its default choices. It also installs "Git Bash".
- macOS: open Terminal and type `xcode-select --install` (this installs Apple's command-line tools, which include git), or install Homebrew and type `brew install git`.
- Linux (Debian/Ubuntu): `sudo apt install git`. (Fedora: `sudo dnf install git`.)

Check: `git --version` prints a version number.

### 3.3 Install Wolfram Engine (or Mathematica) and activate wolframscript

1. Go to https://www.wolfram.com/engine/ and click the download button. You need a free Wolfram ID (an account at wolfram.com); create it yourself on that page and accept the licence terms yourself. Download the installer for your operating system.
2. Install it:
   - Windows: run the downloaded `.exe` installer with its default choices. It installs Wolfram Engine and `wolframscript` (usually in `C:\Program Files\Wolfram Research\WolframScript\`) and adds `wolframscript` to the PATH.
   - macOS: open the downloaded `.dmg` and drag "Wolfram Engine" into Applications. If the disk image also contains a WolframScript installer package, run it; otherwise download WolframScript for macOS from https://www.wolfram.com/wolframscript/ and install it. `wolframscript` is then in `/usr/local/bin`.
   - Linux: in a terminal, in the folder that holds the download, run `sudo bash <name of the downloaded file>.sh` and accept the default answers. `wolframscript` is then in `/usr/local/bin`.
   - If you have Mathematica instead, `wolframscript` is installed with it on Windows and Linux; on macOS install WolframScript from https://www.wolfram.com/wolframscript/ . Mathematica's activation is enough; skip step 3.
3. Close the terminal, open a NEW one (so that the new PATH is used) and activate:

   ```
   wolframscript -activate
   ```

   Type your Wolfram ID (e-mail address) and your password when asked. This is done once per computer.
4. Check that it works:

   ```
   wolframscript -code '$Version'
   ```

   On the verification machine this printed `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. Any 15.0.1 line is what was verified; another version will most likely work, but the report's line `"producer"` then names your version and the report is no longer byte-identical (Part 4.3).

### 3.4 Download the repository (and the optional reference folder)

The first `git clone` downloads the newest version of the repository. The `git checkout` line after it moves to the exact version (commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, re-verified on 2026-10-07) that was verified for this file. It is recommended: if the repository changes later, a newer version may print or write something different from Part 4. Git then prints `HEAD is now at a4c5eda HANDOFF 0.4g: dirac matrices provenance done; ...`. That is normal: you are looking at the verified version, which Git calls a "detached HEAD". To go back to the newest version later, type `git switch main`.

The second `git clone` downloads the separately published reference project dirac into the folder `dirac-main/` inside the repository. It is optional: without it the run still passes all 21 checks, but the report then differs from the committed one (Part 4.3). The option `--config core.autocrlf=false` matters on Windows: without it Git for Windows converts the line endings of the three reference files to CRLF, their sha256 values change, and the report differs in those three values.

The last line computes the sha256 fingerprints of the two program files and the three reference files, so you can check that you have exactly the verified files before you run anything.

Windows (PowerShell):

```
cd $HOME
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
git -c advice.detachedHead=false checkout a4c5eda1df069a43a55ff8b57148f5de8edd1670
git clone --config core.autocrlf=false https://github.com/once-ere/dirac.git dirac-main
git -C dirac-main -c advice.detachedHead=false checkout a21f593a464cf85e90e9271f2ace4df67f50d68e
Get-FileHash -Algorithm SHA256 scripts/verify_dirac16complex_algebra.wls, wolfram/Dirac16ComplexAlgebra.wl, dirac-main/artifacts/exact/cl44-seed.json, dirac-main/artifacts/exact/split-octonion.json, dirac-main/artifacts/exact/triality44.json | ForEach-Object { $_.Hash.ToLower() }
```

macOS (Terminal):

```
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
git -c advice.detachedHead=false checkout a4c5eda1df069a43a55ff8b57148f5de8edd1670
git clone --config core.autocrlf=false https://github.com/once-ere/dirac.git dirac-main
git -C dirac-main -c advice.detachedHead=false checkout a21f593a464cf85e90e9271f2ace4df67f50d68e
shasum -a 256 scripts/verify_dirac16complex_algebra.wls wolfram/Dirac16ComplexAlgebra.wl dirac-main/artifacts/exact/cl44-seed.json dirac-main/artifacts/exact/split-octonion.json dirac-main/artifacts/exact/triality44.json
```

Linux (bash):

```
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
git -c advice.detachedHead=false checkout a4c5eda1df069a43a55ff8b57148f5de8edd1670
git clone --config core.autocrlf=false https://github.com/once-ere/dirac.git dirac-main
git -C dirac-main -c advice.detachedHead=false checkout a21f593a464cf85e90e9271f2ace4df67f50d68e
sha256sum scripts/verify_dirac16complex_algebra.wls wolfram/Dirac16ComplexAlgebra.wl dirac-main/artifacts/exact/cl44-seed.json dirac-main/artifacts/exact/split-octonion.json dirac-main/artifacts/exact/triality44.json
```

The last command must print these five fingerprints in this order (on macOS and Linux each is followed by the file name):

```
86904ac07e1237cf0dec14431a3707d7bf24f951e12def504705d331c934949a
ba0d00c818fa3707f04f7b2a7478b0c635fbf9fdaaa08b2e036d2704180f2262
52e7a73b14467435d7986b33bf29547510b321853ffbd76121896d70b796d133
cbc28db6709ec1fc35ccfcc26353d1952b42bb516f6c50d6a52e2d6d355be710
a8c31c07809fc884ae0495d91f4105fac0909c954bb185c643306c57699cd395
```

If one of the first two differs, you do not have the verified version of the program: repeat the `git -c advice.detachedHead=false checkout a4c5eda...` line. If one of the last three differs, the reference files are not the verified ones (most often CRLF line endings): remove the folder with `Remove-Item -Recurse -Force dirac-main` (PowerShell) or `rm -rf dirac-main` (macOS/Linux), then repeat the two `dirac-main` lines above.

You are now in the repository root (the folder `Dirac_claude`, which contains the folders `scripts`, `wolfram` and `artifacts`). Every command below must be typed in this folder. If you close the terminal and come back later, first go there again with `cd $HOME\Dirac_claude` (PowerShell) or `cd ~/Dirac_claude` (macOS/Linux).

### 3.5 Run the set

Windows (PowerShell), from the repository root:

```
wolframscript -file scripts/verify_dirac16complex_algebra.wls artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
echo "exit code: $LASTEXITCODE"
git status --short
(Get-FileHash -Algorithm SHA256 artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json).Hash.ToLower()
```

macOS (Terminal), from the repository root:

```
wolframscript -file scripts/verify_dirac16complex_algebra.wls artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
echo "exit code: $?"
git status --short
shasum -a 256 artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
```

Linux (bash), from the repository root:

```
wolframscript -file scripts/verify_dirac16complex_algebra.wls artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
echo "exit code: $?"
git status --short
sha256sum artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
```

What you should see: a wait of about 11 to 21 seconds on the verification machine (the whole block took up to 28 s when the computer was busy with other jobs, and 15.5 to 19.1 s on 2026-10-07 with the processor 100 % busy; allow up to a minute on a slower computer). Then come 240 printed lines ending with `report_path=artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`, `elapsed_seconds=...`, `check_count=21` and `failed_check_count=0`. Then `exit code: 0`, then NO output from `git status --short` (the report was rewritten with identical bytes), then the hash `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7` (on macOS and Linux followed by the file name). Part 4 explains every line.

Success means BOTH `exit code: 0` AND the final lines `check_count=21` and `failed_check_count=0`. `wolframscript` also returns exit code 0 when it cannot find the script file at all. In that case nothing runs, and the only printed line is `Failed to open file at path: scripts/verify_dirac16complex_algebra.wls` (Part 3.7, first row).

On macOS and Linux the same bytes are expected, but this was not tested on those systems: only Windows PowerShell and Git Bash on Windows were run (Part 6). The expectation rests on three facts. The report contains no platform-dependent text (paths are stored relative to the repository with forward slashes, the Wolfram version is stored without the operating system, and the line endings are written as LF). The repository stores its files byte-exact. And the `wolframscript` command is the same on every system.

Do not put `--` between the script and the report path. The script's header warns that WolframScript 1.14 can drop `--` and every argument after it; on the verification machine the form with `--` happened to work, but only the form shown above was verified for this file.

### 3.6 Variant that leaves the committed report untouched

If you do not have `dirac-main/`, or you only want to look, write the report somewhere else and compare it with the committed one. `build/` is ignored by Git, and the script creates the folders `build/` and `build/old-algebra/` if they do not exist (Part 5 says how to remove them). The same three lines work in PowerShell, macOS and Linux:

```
wolframscript -file scripts/verify_dirac16complex_algebra.wls build/old-algebra/wolfram-algebra-report.json
git diff --no-index --stat artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json build/old-algebra/wolfram-algebra-report.json
git diff --no-index artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json build/old-algebra/wolfram-algebra-report.json
```

If the two files are identical, both `git diff` commands print nothing. The report's content does not depend on where it is written (the report path is printed but not stored in the file): this variant gave the committed bytes on the verification machine.

### 3.7 If it fails

| What you see | Cause | What to do |
|---|---|---|
| `Failed to open file at path: scripts/verify_dirac16complex_algebra.wls`, then `exit code: 0` (the exit code is still 0), then from the next lines of the block `fatal: not a git repository (or any of the parent directories): .git` and a "file not found" error from the hash command (PowerShell: `Cannot find path '...wolfram-algebra-report.json' because it does not exist.` and `You cannot call a method on a null-valued expression.`; macOS/Linux: `shasum: artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json: No such file or directory`, or the same with `sha256sum:`) | you are not in the repository root, so the relative path `scripts/...` points nowhere; nothing was run and no file was written | go into the folder `Dirac_claude` (the one that contains `scripts`, `wolfram` and `artifacts`): `cd $HOME\Dirac_claude` (PowerShell) or `cd ~/Dirac_claude` (macOS/Linux) if you followed Part 3.4; then run the block again |
| `wolframscript : The term 'wolframscript' is not recognized` (PowerShell) or `wolframscript: command not found` | the program is not installed or the terminal was opened before installing | open a new terminal; repeat Part 3.3; on Windows you can run it with its full path `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file ...` |
| a request for a Wolfram ID, or a message about a licence, activation or "unable to connect to kernel" | wolframscript is not activated, or the licence limits how many kernels may run at once | run `wolframscript -activate` (Part 3.3); close other Mathematica or Wolfram programs and try again; activation needs internet |
| `ERROR: missing package ...` and exit code 2 | you are not in a complete copy of the repository | check that `wolfram/Dirac16ComplexAlgebra.wl` exists; clone again (Part 3.4) |
| `ERROR: package load produced messages: ...` and exit code 2 | the package file was changed, or your Wolfram version cannot read it | compare its sha256 with Part 2.1 (`git checkout -- wolfram/Dirac16ComplexAlgebra.wl` restores it); use Wolfram 15.0.1 if possible |
| `ERROR: JSON export failed` and exit code 2 | the Wolfram installation is damaged | reinstall Wolfram Engine |
| a line `check_...=false`, `failed_check_count` above 0, exit code 1 | a mathematical check failed | do not edit anything; check the sha256 of every file in Part 2; restore the files of the set with `git checkout -- scripts/verify_dirac16complex_algebra.wls wolfram/Dirac16ComplexAlgebra.wl artifacts/dirac16complex/arbitrary-field/`; if the hashes are right and a check still fails, report it with the full printed output |
| `check_count=20` and `measurement_fixtureAgreement=not-run` | `algebra-fixture.json` is missing (or the second argument names a missing file) | restore it: `git checkout -- artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` |
| `git status --short` shows ` M artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` | `dirac-main/` is missing or different, or your Wolfram version is not 15.0.1 | look at `git diff`; the expected differences are listed in Part 4.3; restore with `git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` |
| `git diff` shows only the three `dirac-main/...` hashes in `"sourceSha256"` changed | the three reference files have CRLF line endings | from the repository root, delete the folder with `Remove-Item -Recurse -Force dirac-main` (PowerShell) or `rm -rf dirac-main` (macOS/Linux), then clone it again with the two `dirac-main` lines of Part 3.4 (`git clone --config core.autocrlf=false https://github.com/once-ere/dirac.git dirac-main` and `git -C dirac-main -c advice.detachedHead=false checkout a21f593a464cf85e90e9271f2ace4df67f50d68e`); restore the report with `git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` and run again |
| the checks pass, but the line `report_path=` is not exactly `report_path=artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`: it shows a full path (for example `C:/Users/.../artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`) or a path such as `scripts/artifacts/...`, and `git status --short` may show `?? scripts/artifacts/` | the script was started with its path given relative to another folder, for example `wolframscript -file ../scripts/verify_dirac16complex_algebra.wls artifacts/...` from a subfolder, `wolframscript -file verify_dirac16complex_algebra.wls artifacts/...` from inside `scripts`, or `wolframscript -file Dirac_claude/scripts/verify_dirac16complex_algebra.wls artifacts/...` from the folder above. The script finds its package next to itself, so it runs, but the report path is taken from the current folder, and the report (with any missing folders on its path) is written under the current folder | the committed report was not touched. ONLY if the current folder is not the repository root (it must not contain both `scripts` and `wolfram`), delete the stray report and the folders that are now empty, in the current folder. PowerShell: `Remove-Item artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`, then `Remove-Item artifacts/dirac16complex/arbitrary-field`, `Remove-Item artifacts/dirac16complex` and `Remove-Item artifacts`. If PowerShell asks whether to remove a folder that "has children", answer `N`: that folder held other files before the run. macOS/Linux: `rm artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`, then `rmdir artifacts/dirac16complex/arbitrary-field artifacts/dirac16complex artifacts`. `rmdir` removes only empty folders, so it never deletes anything else. Then `cd` to the repository root and run the documented command |

## 4. Expected output

### 4.1 What is printed

Exactly 240 lines on standard output and nothing on standard error:

- 21 lines `check_<name>=true`, in this order: `check_ALG_clifford`, `check_ALG_gammaTransposeSymmetry`, `check_ALG_chargeMatrix`, `check_ALG_expression1`, `check_ALG_spinTransposeProperties`, `check_ALG_chirality`, `check_ALG_faithful`, `check_ALG_pinIrreducibleComplex`, `check_ALG_spinDecomposition`, `check_ALG_cliffordPictureIntertwiner`, `check_ALG_octonionPictureIntertwiner`, `check_ALG_chargeFormB`, `check_ALG_invariantForms`, `check_ALG_gamma8Map`, `check_ALG_pinLiftCharacter`, `check_QNT_curvedAnticommutatorMatrix`, `check_QNT_flatModeHamiltonian`, `check_QNT_kreinSignature`, `check_QNT_unitaryAndKreinSubgroups`, `check_QNT_currentHermiticity`, `check_ALG_fixtureAgreement`;
- 215 lines `measurement_<name>=<value>` (values are numbers, words, or compact JSON; the longest line has 7405 characters, so lines wrap on the screen). Examples: `measurement_ALG_clifford.pairsSatisfied=64`, `measurement_ALG_chargeMatrix.characteristicPolynomial=(-1 + x)^8*(1 + x)^8`, `measurement_ALG_pinIrreducibleComplex.commutantDimension=1`, `measurement_QNT_unitaryAndKreinSubgroups.countCommutingWithB=13`, `measurement_fixtureAgreement.summary={"agree":true,"matricesFound":75,"agreeByName":75,"agreeByValue":0,"disagreeByName":0,"unmatched":0,"vectorsNotCompared":0}`;
- the four final lines:

```
report_path=artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
elapsed_seconds=9
check_count=21
failed_check_count=0
```

`elapsed_seconds` is the computing time measured by the script itself. It varies from run to run and from machine to machine: on the verification machine it was 9 or 10 in the five timed runs of 2026-10-02, 12 to 14 in the four timed runs of 2026-10-07, and 8 to 16 overall, depending on the other jobs running at the same time (Part 4.4). Every other printed line is the same in every run. Without `dirac-main/` eight printed lines differ: the seven `measurement_..._matchesDiracMain...`, `..._gammasFromDiracMain...` and `..._diracMainCanonicalIntertwiner...` lines show `not-run` instead of `true`, and `measurement_referenceFilesPresent` shows `false` for the three dirac-main files. The check lines and the four final lines are unchanged.

### 4.2 Exit code

`0` when every check is true (the verified result); `1` if any check is false; `2` if the package is missing, prints messages while loading, or the JSON cannot be produced.

`wolframscript` ALSO returns `0` when it cannot open the script file, for example when the command is typed outside the repository root. It then prints only `Failed to open file at path: scripts/verify_dirac16complex_algebra.wls` (on standard error, as measured in Git Bash), runs nothing and writes nothing. This was measured with Windows PowerShell 5.1, PowerShell 7.6.6 and Git Bash. So success means exit code `0` AND the final lines `check_count=21` and `failed_check_count=0`.

### 4.3 The report file

`artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` (or the path you gave): plain ASCII text (Greek letters are written as Wolfram escapes, for example `\[Sigma]`, which JSON stores as `\\[Sigma]`), LF line endings, indented with tabs, 2638 lines, 49440 bytes, sha256 `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7` with `dirac-main/` present. Its top-level keys are `schemaVersion` (1), `producer` (``scripts/verify_dirac16complex_algebra.wls with wolfram/Dirac16ComplexAlgebra.wl (context Dirac16Complex`Algebra`), Wolfram Language 15.0.1``), `checks` (21 entries, all `true`), `measurements` (everything the checks measured, exact numbers written as integers or as strings such as `"1/7"`) and `sourceSha256` (the hashes of the programs and inputs of Part 2).

How to check it:

- the hash: the last command of Part 3.5 must print `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7`;
- the count of true checks, in PowerShell:

  ```
  $r = Get-Content artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json -Raw | ConvertFrom-Json
  @($r.checks.PSObject.Properties | Where-Object { $_.Value -eq $true }).Count
  $r.measurements.'fixtureAgreement.summary' | ConvertTo-Json -Compress
  ```

  prints `21` and `{"agree":true,"matricesFound":75,"agreeByName":75,"agreeByValue":0,"disagreeByName":0,"unmatched":0,"vectorsNotCompared":0}`;
- the same with Python on any system (`python3` instead of `python` on macOS and Linux):

  ```
  python -c "import json; c=json.load(open('artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json'))['checks']; print(sum(v is True for v in c.values()), 'of', len(c))"
  ```

  prints `21 of 21`.

Without `dirac-main/` (a plain clone): the report has 49130 bytes and sha256 `39cc390b53266bda09549faf5e099bc8ebcfb49bef19cff4701987716c13a709` (the same in two runs), all 21 checks are still true, and it differs from the committed report in exactly 13 lines: the seven dirac-main comparison values in `measurements` change from `true` to `"not-run"` (`ALG_cliffordPictureIntertwiner.matchesDiracMainCl44SeedGenerators`, `...matchesDiracMainCl44SeedVolumeElement`, `ALG_octonionPictureIntertwiner.matchesDiracMainSplitOctonionMultiplicationTensor`, `...gammasFromDiracMainSplitOctonionJsonEqualRebuilt`, `...matchesDiracMainTriality44OctonionCliffordGenerators`, `...diracMainCanonicalIntertwinerEqualsPrimitiveKcliffordKoctonion`, `...diracMainCanonicalIntertwinerVerified`), the three dirac-main entries of `referenceFilesPresent` change from `true` to `false`, and the three dirac-main lines of `sourceSha256` are absent.

With `dirac-main/` checked out with CRLF line endings: sha256 `fd337739bc60cef5ddcfc55e0a3f19ab8f9929c21d0f7276a713224323d498d8`; only the three dirac-main hashes in `sourceSha256` differ (they become `0660e436...`, `25044ea1...`, `5985f5c0...`), all checks and comparisons are true.

With a Wolfram version other than 15.0.1 the line `"producer"` names that version, so the bytes differ in at least that line; this was not tested.

### 4.4 Run time and memory

On the verification machine (24 logical processors, Windows 11, other Wolfram jobs running at the same time): 12.1 to 13.4 seconds of wall-clock time per run in the five timed runs of Part 6, including the start of the Wolfram kernel; the script's own `elapsed_seconds` was 9 or 10. The run time depends on the other jobs on the computer. Over all measured runs on the same machine, about 8 other Wolfram kernels were running and the processor was 85 to 100 % busy. Under that load `elapsed_seconds` was 8 to 16, and `wolframscript` alone took 11.3 to 18.2 s where it was timed separately. The whole Part 3.5 block, including `git status` and the hash, took 11.9 to 21.5 s, and up to 28.1 s including the start of a new shell. The 21.5 s block was the one with `elapsed_seconds=16`. With four runs at the same time on top of that load, each took 14.7 to 15.4 s (`elapsed_seconds=11`). On a slower computer allow up to a minute. Peak memory (Windows peak working set): 413.2 to 413.6 MiB for the Wolfram kernel and 16.5 MiB for `wolframscript`.

On 2026-10-07 (re-verification, Part 6) the machine was busier: 13 to 18 other Wolfram kernels were running and the processor was 100 % busy before and after every run. The four timed runs took 16.9 to 19.0 s of wall-clock time with `elapsed_seconds` 12 to 14, and the Part 3.5 block typed by the student procedure took 15.5 to 19.1 s (`elapsed_seconds` 11 to 15). Peak memory was 412.8 to 413.0 MiB for the Wolfram kernel and 16.5 to 16.6 MiB for `wolframscript`.

## 5. Side effects

- **Files overwritten in the repository:** only `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`. With `dirac-main/` present (LF line endings) and Wolfram 15.0.1 it is rewritten with identical bytes and `git status` stays clean. Otherwise it is modified (Part 4.3).
- **Files and folders created:** none with the documented command typed in the repository root. With another report path (Part 3.6) the script creates that file and any missing folders on its path: in a fresh clone both `build/` and `build/old-algebra/`, which Git ignores. Git does not show an empty folder, so `git status` does not reveal a `build/` folder left behind. If the script is started from another folder with a path to it, the report and its folders are created under that folder (Part 3.7, last row). If the script file cannot be found (Part 3.7, first row), nothing is created. Part 3.4 creates the folder `dirac-main/` (ignored by Git).
- **Files only read:** the package, the fixture and the three dirac-main files (Part 2.2). Nothing is deleted. The author's notebooks are not opened.
- **Temporary files:** none. In every measured run the folder given to the run as `TEMP`/`TMP` was still empty at the end. `wolframscript` itself (not this script) keeps small bookkeeping files in your user profile (on Windows `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` and `%APPDATA%\Wolfram\WolframScript\WolframScript.conf`). Files there changed during the verification runs, but other `wolframscript` programs were running at the same time, so they cannot be assigned to this run alone. They are outside the repository and harmless.
- **Wolfram kernels:** one kernel per run (the process `wolfram.exe` of Wolfram 15.0.1 on Windows; on macOS and Linux the Wolfram kernel process, usually named `WolframKernel`), started by `wolframscript` and ended by the script's `Exit`. The kernel process of each of the five timed runs was checked afterwards and had ended. It uses one kernel of your licence while it runs.
- **Network:** the script makes no network access. It contains no URL, cloud, paclet-install or process-launch function and reads only local files. Activating Wolfram Engine (Part 3.3) and downloading the repository (Part 3.4) need the internet; the Wolfram licence may contact Wolfram's servers on its own schedule.
- **Downstream consistency:** 13 committed files record this report's full sha256 `d43adeeba580bdd8...` (found with `git grep -l d43adeeba580bdd8` at commit `c2b33cc`; at commit `a4c5eda` the same command lists 16 files: these 13, this provenance file, and `provenance/wolframscript/verify_dirac16complex00.PROVENANCE.md` and `provenance/wolframscript/verify_dirac16complex_matter_antimatter.PROVENANCE.md`):
  - `artifacts/dirac16complex/arbitrary-field/python-algebra-report.json`
  - `artifacts/dirac16complex/arbitrary-field/stage1-summary.json`
  - `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json`
  - `artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json`
  - `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`
  - `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json`
  - `handoff/reviews/stage1_gate_2026-09-30_private_sh.log`, `handoff/reviews/stage1_gate_2026-09-30_public_ps1.log`, `handoff/reviews/stage1_gate_2026-09-30_public_sh.log`
  - `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.tex`
  - `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md`, `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.tex`

  The earlier textbook (`provenance/DIRAC16COMPLEX_TEXTBOOK.md`, `.tex` and its chapter `provenance/textbook/chapters/19-reproducing-everything.md`) cites the first eight characters `d43adeeb...`. If your run changes the report, these records no longer match it until you restore it.
- **Restoring the committed state** (from the repository root). This restores the report on all systems:

  ```
  git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
  git status --short
  ```

  `git status --short` must then print nothing. To also remove the files of Part 3.6: if the folder `build/` did not exist before you ran Part 3.6 (it does not exist in a fresh clone), remove it completely. Use `Remove-Item -Recurse -Force build` (PowerShell) or `rm -rf build` (macOS/Linux). If `build/` existed before and holds other files you want to keep, remove only `build/old-algebra`: `Remove-Item -Recurse -Force build/old-algebra` (PowerShell) or `rm -rf build/old-algebra` (macOS/Linux). To also remove the reference folder of Part 3.4 (the report then no longer reproduces the committed bytes, Part 4.3), use `Remove-Item -Recurse -Force dirac-main` (PowerShell) or `rm -rf dirac-main` (macOS/Linux). `-Force` is needed on Windows because Git marks some files inside `dirac-main/.git` as read-only. After these commands the folder is exactly what the first `git clone` and `git checkout` of Part 3.4 gave you. To check this, `git status --short --ignored` must print nothing (it also lists ignored folders such as `dirac-main/`, but not empty folders). Also, `Test-Path build` (PowerShell) must print `False`, and `ls -d build` (macOS/Linux) must report `No such file or directory`.

## 6. Verification record

- **Date:** 2026-10-02 (first verification: every item of this part except the item "Re-verification on 2026-10-07"). Re-verified on 2026-10-07 at commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, after the verification workflow had been interrupted by a session limit and restarted (item "Re-verification on 2026-10-07" below).
- **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (2026-10-02 06:00:22 -0700) of https://github.com/once-ere/Dirac_claude.git; the set's files are unchanged since `6c0bfad` (2026-09-25). Every run used a fresh `git clone`; no uncommitted file of the working copy was used, except the three reference files listed for clone A.
- **Environment:** Windows 11 Pro for Workstations 10.0.26200, Intel Core Ultra 9 275HX (24 logical processors), 191 GB RAM; WolframScript 1.14.0, Wolfram 15.0.1 (Professional licence); Git 2.51.2.windows.1 (system-wide `core.autocrlf=true`, the Git for Windows installer default, set in `C:/Program Files/Git/etc/gitconfig`; there is no global or repository value; the repository's `.gitattributes` line `* -text` keeps its own files byte-exact); PowerShell 7.6.6; Python 3.14.5 (for the report check only). Each run was started from the clone root with the documented command, with `TEMP` and `TMP` pointing at an empty folder, and the process tree's peak working set was sampled every 0.25 s.
- **Clones:**
  - A: fresh clone plus a copy of the three files `dirac-main/artifacts/exact/{cl44-seed,split-octonion,triality44}.json` from the author's working copy (sha256 equal to Part 2.2);
  - B: fresh clone without `dirac-main/` (what a plain clone gives);
  - C: fresh clone plus `git clone --config core.autocrlf=false https://github.com/once-ere/dirac.git dirac-main` at commit `a21f593a464cf85e90e9271f2ace4df67f50d68e` (the procedure of Part 3.4).

| Run | Clone | Command | Exit | Wall time | elapsed_seconds | Checks | Report sha256 | Same as committed |
|---|---|---|---|---|---|---|---|---|
| A-run1 | A | documented (in place) | 0 | 12.25 s | 9 | 21 / 0 failed | `d43adeeb...cd49e7` | yes, byte-identical |
| A-run2 | A | documented (in place) | 0 | 12.26 s | 9 | 21 / 0 failed | `d43adeeb...cd49e7` | yes, byte-identical |
| C-run1 | C | documented (in place) | 0 | 12.97 s | 9 | 21 / 0 failed | `d43adeeb...cd49e7` | yes, byte-identical |
| B-run1 | B | documented (in place) | 0 | 13.43 s | 9 | 21 / 0 failed | `39cc390b...13a709` | no: the 13 expected lines (Part 4.3) |
| B-run2 | B | documented (in place) | 0 | 12.13 s | 9 | 21 / 0 failed | `39cc390b...13a709` | no: same 13 lines; byte-identical to B-run1 |

- **Byte identity:** A-run1 = A-run2 = C-run1 = committed report; B-run1 = B-run2. With the Git Bash run and the four runs of the student procedure below, all 8 runs with `dirac-main/` present wrote the committed bytes. The printed output of A-run1, A-run2 and C-run1 was identical except for `elapsed_seconds`, and so was that of B-run1 and B-run2. Standard error was empty in every run. `git status --porcelain` after the runs: clones A and C clean (only the ignored `dirac-main/`); clone B ` M artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json`.
- **Additional runs (not timed):**
  - Git Bash, clone A, report written to `build/old-algebra/wolfram-algebra-report.json`: exit 0, 21/0, byte-identical to the committed report; the folder was created.
  - Clone B with an explicit missing fixture path: exit 0, `check_count=20`, `failed_check_count=0`, `measurement_fixtureAgreement=not-run`.
  - Clone B with the three reference files checked out with CRLF line endings: exit 0, 21/0, only the three dirac-main hashes differ (`fd337739...`).
  - Clone B with `--` before the report path, from Git Bash and from PowerShell 7.6.6: exit 0, the report went to the requested path. The drop described in the script's header did not occur on this machine. The header's advice is still followed in Part 3.5.
- **The student procedure itself:** the commands of Parts 3.4, 3.5 (Windows block), 3.6, 4.3 and 5 were typed verbatim into a script and run in Windows PowerShell 5.1.26100 (`powershell.exe`) in a new empty folder; the commands of Parts 3.4, 3.5 (Linux block), 3.6, 4.3 (Python line) and 5 were run the same way in Git Bash. Only the starting folder (`cd $HOME` / `cd ~`) was changed. Both cloned commit `c2b33cc` and dirac `a21f593`. Both ended with exit code 0 and printed `check_count=21` and `failed_check_count=0` twice. The hash was `d43adeeb...cd49e7`, `git status --short` printed nothing, both `git diff --no-index` commands printed nothing (exit 0), and the checks printed `21`, the fixture summary and `21 of 21`. After the restore commands of that time, `git status --porcelain --ignored` listed only the ignored `dirac-main/`. An empty `build/` folder also remained, which Git does not list. The review found it, and Part 5 now removes it (below). Each took 34 to 36 s in total, including both downloads. Neither the macOS block nor any step on macOS or Linux was run: the Linux block ran only in Git Bash on Windows.
- **Peak memory:** Wolfram kernel 413.2 to 413.6 MiB, wolframscript 16.5 MiB; temporary files in the private `TEMP`: 0 in every timed run.
- **Re-verification after an independent review** (2026-10-02, same commit `c2b33cc` (still the head of `main`), same machine, PowerShell 7.6.6 unless stated). It used a fresh clone D with `dirac-main/` cloned as in Part 3.4. No file of the working copy was used, and the five fingerprints of Part 3.4 matched.
  - Three timed in-place runs with the documented command, with 8 or 9 other Wolfram kernels running and the processor 85 to 94 % busy. Each gave exit code 0, 240 lines, 21 / 0 failed, a clean `git status` and report `d43adeeb...cd49e7`. Wall times were 13.7, 12.1 and 11.8 s, and `elapsed_seconds` 10, 9 and 9.
  - Four runs at the same time, writing to `build/conc1` ... `build/conc4`, on top of that load. Each gave exit code 0 and 21 / 0, took 14.7 to 15.4 s with `elapsed_seconds=11`, and wrote a report byte-identical to the committed one.
  - The Part 3.5 block typed outside the repository root (Part 3.7, first row), in Windows PowerShell 5.1.26100, PowerShell 7.6.6 and Git Bash. Each printed `Failed to open file at path: scripts/verify_dirac16complex_algebra.wls`, then exit code 0, and wrote no file anywhere. Git Bash, which captured the two output streams separately, showed that the message goes to standard error and standard output is empty.
  - The script started through a path relative to another folder (Part 3.7, last row): from a sibling folder with `../D/scripts/...`, and from inside `scripts/`. Both gave exit code 0 and 21 / 0. `report_path=` showed a full path in the first case and `scripts/artifacts/...` in the second. The report (`d43adeeb...`) was written under the current folder and the committed report was untouched; in the second case `git status` showed `?? scripts/artifacts/`. The cleanup commands of that row removed the stray file and its folders. With a file `artifacts/keep.txt` placed there beforehand, they left it in place: PowerShell refused to remove the non-empty folder without `-Recurse`, and `rmdir` reported `Directory not empty`.
  - Part 3.6 followed by the earlier Part 5 restore left an empty `build/` folder. `Remove-Item -Recurse -Force build` and `Remove-Item -Recurse -Force dirac-main` (Windows PowerShell 5.1), and `rm -rf build dirac-main` (Git Bash), removed both folders, including the read-only pack files in `dirac-main/.git`.
  - The updated student procedure was extracted by a program from this file: the code blocks of Parts 3.4, 3.5, 3.6, 4.3 and 5, plus the inline commands of Part 3.7 (first-row recovery) and Part 5. It was run verbatim, with only the starting folder changed, in three new empty folders: Windows PowerShell 5.1.26100 with the Windows blocks (58 s in total), Git Bash with the Linux blocks (42 s), and Git Bash with the macOS blocks (43 s, using `shasum` from Git for Windows; this checks the commands, not macOS). Each also ran the Part 3.5 block once from the folder above the clone before the real run. All three printed:
    - the five fingerprints of Part 3.4;
    - outside the root, the first-row messages of Part 3.7 and `exit code: 0`;
    - then, in both the in-place run and the Part 3.6 run, 240 printed lines ending with `check_count=21` and `failed_check_count=0`; the in-place run also printed `exit code: 0`.

    In the in-place run, `elapsed_seconds` was 16, 9 and 9 and the Part 3.5 block took 21.5, 12.7 and 12.8 s. `git status --short` was empty, the hash was `d43adeeb...cd49e7` and both `git diff --no-index` commands printed nothing. The checks of Part 4.3 printed `21`, the fixture summary and `21 of 21` (PowerShell), and `21 of 21` (Git Bash). After Part 5, `git status --short --ignored` printed nothing and `build/` and `dirac-main/` were gone. Nothing was written in the starting folders. The 239 printed lines other than `elapsed_seconds` were identical in the three runs.
  - The charge-conjugation statements of Part 1.3 were checked exactly with sympy, using the fixture files of clone D. C^-1 gamma^a C = -(gamma^a)^T and calC_+ C = C^2 = I16. (gamma^8 C)^-1 gamma^a (gamma^8 C) = +(gamma^a)^T and (gamma^8 C) C = gamma^8. The solutions of M gamma^a = s gamma^a M form a 1-dimensional space, spanned by I16 for s = +1 and by gamma^8 for s = -1. The lead check's gammas (relabelled), C and Gamma equal this set's gammas, C and gamma^8. `Revision/lead_checks/charge_conjugation_and_u1.py` ran in clone D in 6.6 s, gave 12 / 12 PASS, and rewrote its committed report with identical bytes.
  - `git config --show-origin --show-scope --get-all core.autocrlf` printed only `system file:C:/Program Files/Git/etc/gitconfig true`, and `git config --global --get core.autocrlf` printed nothing.
- **Re-verification on 2026-10-07.** Commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (2026-10-07 15:17:26 -0700), the head of `main` on GitHub at the time. Between `c2b33cc` and `a4c5eda` none of these files changed: the two programs of the set, everything in `artifacts/dirac16complex/arbitrary-field/` (the fixture and the committed report included), `.gitignore` and `.gitattributes` (`git diff --stat c2b33cc a4c5eda` with these paths listed only this provenance file). Same machine, now Windows 11 Pro for Workstations 10.0.26300.9457; WolframScript 1.14.0, Wolfram 15.0.1; Git 2.51.2.windows.1 with the same system-wide `core.autocrlf=true`; PowerShell 7.6.6 and Windows PowerShell 5.1.26100.9444; Python 3.14.5. No file of the working copy was used. Two new fresh clones:
  - A2: fresh clone plus `dirac-main/` cloned from GitHub exactly as in Part 3.4 (dirac commit `a21f593`). The five fingerprints of Part 3.4 matched, and the three reference files were also identical to those of the author's working copy;
  - B2: fresh clone without `dirac-main/` (what a plain clone gives).

  | Run | Clone | Command | Exit | Wall time | elapsed_seconds | Checks | Report sha256 | Same as committed |
  |---|---|---|---|---|---|---|---|---|
  | A2-run1 | A2 | documented (in place) | 0 | 18.87 s | 13 | 21 / 0 failed | `d43adeeb...cd49e7` | yes, byte-identical |
  | A2-run2 | A2 | documented (in place) | 0 | 18.98 s | 14 | 21 / 0 failed | `d43adeeb...cd49e7` | yes, byte-identical |
  | B2-run1 | B2 | documented (in place) | 0 | 16.93 s | 12 | 21 / 0 failed | `39cc390b...13a709` | no: the 13 expected lines (Part 4.3) |
  | B2-run2 | B2 | documented (in place) | 0 | 18.67 s | 13 | 21 / 0 failed | `39cc390b...13a709` | no: same 13 lines; byte-identical to B2-run1 |

  - Every run printed 240 lines and nothing on standard error. The private `TEMP` folder was empty at the end, and the kernel process `wolfram.exe` had ended. Peak working set: kernel 412.8 to 413.0 MiB, `wolframscript` 16.5 to 16.6 MiB. At the start of the four runs 13, 14, 15 and 18 other Wolfram kernels were running, and the processor was 100 % busy before and after every run.
  - `git status --porcelain --ignored` after the runs: clone A2 printed only `!! dirac-main/`; clone B2 printed ` M artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` (10 insertions, 13 deletions: exactly the 13 lines of Part 4.3). The printed output of A2-run1 and A2-run2 differed only in `elapsed_seconds`, and so did that of B2-run1 and B2-run2. A2 and B2 differed in the eight lines named in Part 4.1 and in `elapsed_seconds`.
  - The student procedure was run again, with the new commit pin `a4c5eda` of Part 3.4. A program extracted the code blocks of Parts 3.4, 3.5, 3.6, 4.3 and 5 and the inline removal commands of Part 5 from this file. They were run verbatim, with only the starting folder changed, in three new empty folders: Windows PowerShell 5.1.26100.9444 with the Windows blocks (51.4 s in total), Git Bash with the Linux blocks (65.3 s), and Git Bash with the macOS blocks (55.8 s, using `shasum` from Git for Windows; this checks the commands, not macOS). Each first ran the Part 3.5 block from the folder above the clone. Each time it printed `Failed to open file at path: scripts/verify_dirac16complex_algebra.wls`, `exit code: 0` and the first-row messages of Part 3.7, and wrote no file. All three then printed:
    - the five fingerprints of Part 3.4, `HEAD is now at a4c5eda HANDOFF 0.4g: dirac matrices provenance done; ...` and `HEAD is now at a21f593 Record Developer Summary public verification`;
    - in the in-place run and in the Part 3.6 run, 240 printed lines ending with `check_count=21` and `failed_check_count=0`; the in-place run also printed `exit code: 0`, an empty `git status --short` and the hash `d43adeeb...cd49e7`;
    - nothing from either `git diff --no-index` command;
    - for Part 4.3: `21`, the fixture summary and `21 of 21` (PowerShell), and `21 of 21` (Git Bash).

    The Part 3.5 block took 15.5, 19.1 and 16.8 s (`elapsed_seconds` 11, 15 and 12). After Part 5, `git status --short --ignored` printed nothing, `Test-Path build` printed `False` and `ls -d build` reported `No such file or directory`. Each starting folder then held only the folder `Dirac_claude`. The 239 printed lines other than `elapsed_seconds` were identical in the three shells and identical to those of A2-run1.
  - The cross-check of Part 1.5 (the package's gammas, C, gamma^8, the two projectors and eta against the author's matrices in `provenance/dirac_matrices/author_notebook_T16.json`) ran in clone A2 in 7.5 s. All six comparisons were `True`, and all entries of the eight gammas are -1, 0 or +1.
  - `Revision/lead_checks/charge_conjugation_and_u1.py` (Part 1.3) ran in clone A2 in 15.4 s under the load above. It printed 12 PASS lines and `{"passed": 12, "total": 12}`, and rewrote its committed report with identical bytes (`git status` stayed clean).
  - Not repeated on 2026-10-07, because the set and the WolframScript version are unchanged: the variants with CRLF reference files, with a missing fixture and with `--`, the concurrent runs, and the runs started through a path relative to another folder.
- **Fixes made:** none to the set. No execution defect was found, and no file of the set or of its outputs was changed, neither on 2026-10-02 nor on 2026-10-07. On 2026-10-07 this provenance file was updated: the commit pin and Git's message in Part 3.4 (`c2b33cc` -> `a4c5eda`), Part 1.4 (the newer files that cite the report or load the package), the new Part 1.5, the clone size (Part 3.1), the run times (header and Parts 3.5, 4.1 and 4.4), the list of files that record the report's hash (Part 5) and this record. This provenance file was corrected after the review of 2026-10-02:
  - Part 1.3: C is the charge-conjugation matrix calC_+, and gamma^8 = calC_- C is the nontrivial real map;
  - the run times (header, Parts 3.5, 4.1 and 4.4);
  - the case of the command typed outside the repository root, where the exit code is still 0 (Parts 3.5, 3.7 and 4.2);
  - the row of Part 3.7 for a report written to another folder;
  - the commit pin and the fingerprint check (Part 3.4);
  - how to open a terminal (Part 3);
  - the note that macOS and Linux were not tested (Parts 3.5 and 6);
  - the restore and removal commands and the full list of files that record the report's hash (Parts 3.7 and 5);
  - the origin of `core.autocrlf` (Part 6).
- **Open discrepancies:** none. All 21 checks are true and the committed report is reproduced byte for byte, on 2026-10-02 and again on 2026-10-07. The only conditions are the reference folder `dirac-main/` with LF line endings and Wolfram 15.0.1.
