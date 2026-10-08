# Execution provenance: the Stage-5 dirac16complex00 verifier (WolframScript)

Set: `scripts/verify_dirac16complex00.wls` with `wolfram/Dirac16Complex00.wl` (old Stage 5, "dirac16complex00": the field with 16 commuting complex components, side by side with the Grassmann field dirac16complex).

Verified on 2026-10-02 from fresh clones of https://github.com/once-ere/Dirac_claude.git at commits `45d47343ae480df46e06689ed822b8f9a88a8030` and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (identical files of this set and of all its inputs). Result: the set EXECUTES OK (exit code 0, 46 of 46 checks true, `failed_check_count=0`). As committed it did NOT reproduce its report byte for byte: one entry, `charPolyC`, contains a symbol name `x$NNNN` whose number changes from kernel start to kernel start. This execution defect was fixed on 2026-10-02 (Part 6.3: a change of `wolfram/Dirac16Complex00.wl`, 7 lines added and 2 removed, the two regenerated output files, and the regenerated report of the independent Python checker, which records the sha256 of both output files and whose records a unit test enforces); with the fix, every run reproduces both output files byte for byte. The fix was committed in `3f0a577c234501e0e073df1ec1640554bf93d764` (2026-10-02). On 2026-10-07 the set was verified again from fresh clones of commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, which contains the fix (Part 6.5): it EXECUTES OK (exit code 0, 46 of 46 checks true in each run), and two runs with the usage line (PowerShell 7 and Git Bash) and a third run with the student commands of Part 3.3 reproduced both committed output files byte for byte. The details are in Part 6.

This file is written for a student who has never used Wolfram software. Everything you need to run the set is in this file; you do not have to read any other file first.

## 1. What this set is and what it computes

**The physics in plain words.** The project studies fields in an 8-dimensional space-time with 4 space-like and 4 time-like directions. The coordinates are called x0, ..., x7; x4 is the time in which the fields evolve. The flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). A field here has 16 complex components (a "spinor" of the group Pin(4,4)); it is acted on by eight 16x16 matrices gamma^0, ..., gamma^7 (the "gamma matrices", with gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab), by the 16x16 matrix C = gamma^0 gamma^1 gamma^2 gamma^3 (which forms the "adjoint" Psibar = Psi^dagger C, where Psi^dagger is the complex-conjugate transpose), by B = -i C gamma^4 and by gamma^8 = gamma^0 gamma^1 ... gamma^7. Two fields are compared:

* **dirac16complex**: the 16 components are *Grassmann* (anticommuting) numbers, theta1 theta2 = -theta2 theta1. This is the quantum (fermion) field of the project's Stages 1 to 4.
* **dirac16complex00**: the 16 components are ordinary *commuting* complex numbers. This is the classical analogue of Dirac's original 4-component wave function.

Both fields have the same Lagrangian (the "action density"; m is the mass, U a potential, by default U = (lambda/2) S^2 with S = Psibar Psi, and g the metric of an arbitrary gravitational field described by a vielbein e_mu^a with spin connection Omega_mu and covariant derivative D_mu Psi = d_mu Psi + Omega_mu Psi):

```
L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m Psibar Psi - U(Psibar Psi) ]      (L1)
```

**What the computer does.** The package `wolfram/Dirac16Complex00.wl` proves, with exact arithmetic, the classical field theory of dirac16complex00 and compares it with dirac16complex wherever the statistics (commuting or anticommuting) matters. It never uses a floating-point number to decide anything: every decision is an exact zero test of integers, fractions, Gaussian fractions (p + i q), numbers of the form p + q cos z, or polynomials in symbols. It does not solve differential equations numerically. It works at exact test points of four test geometries:

* **G1**: a general non-diagonal vielbein, at three points with fractional coordinates;
* **G2**: the project's "primordial field" (built from cot z, sin(z)^(1/6) and exp(+-a4(t)) with an arbitrary function a4), at three exact points;
* **G3**: a homogeneous "Bianchi-I" universe that depends on the time x4 only, at three times;
* **G4**: a generic non-diagonal vielbein with integer entries.

The field values at the points are exact fractions from a fixed pseudo-random generator (a 64-bit linear congruential generator with fixed seeds), so every run computes the same numbers. The program runs through 14 steps; it prints the name of each step with the time of day when the step starts:

| Step (as printed) | Checks it decides | What is proved |
| --- | --- | --- |
| `fixture and algebra` | `C00_fixture_matchesStage1Construction`, `C00_algebra_leadFacts`, `C00_algebra_anticommutatorTotallyAntisymmetric`, `C00_algebra_pinModuleAndSpinInvariance` | the gamma matrices, C, B, gamma^8 and S^ab equal the committed Stage-1 data file; 20 facts about gamma^8, C and B (for example B is Hermitian with B^2 = 1 and eigenvalues +1 and -1 eight times each); C^16 is an irreducible Pin(4,4) module that splits into two halves under Spin(4,4) |
| `flat: Grassmann algebra, commuting polynomials, mass term, dispersion` | `C00_massTerm_grassmannNonzero`, `C00_lagrangian_grassmannFlatHermitianAndEL`, `C00_realRestriction_grassmannFlatTrivial`, `C00_realRestriction_grassmannComplexDecomposition`, `C00_realRestriction_commutingFlatDecomposition`, `C00_EL_commutingFlat`, `C00_massTerm_commutingExplicitSpinors`, `C00_massTerm_dispersionFlat` | in flat space: the mass term Psibar Psi is a nonzero element of the Grassmann algebra and takes the values -2, +2, 0 on explicit commuting spinors; the Euler-Lagrange (field) equations of (L1) have the same form for both statistics; for a REAL Grassmann field the original notebook's Lagrangian is a pure divergence (trivial), for a real commuting field it is not; the plane-wave dispersion relation k_4^2 + k_5^2 + k_6^2 + k_7^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2 = m^2 |
| `test geometries G1 (3 points), G2 (3 points), G4` | `C00_geometry_G4Generic` | builds the exact geometries; G4 has signature (4,4) and nonzero curvature |
| `Euler-Lagrange equations (commuting, curved)` | `C00_EL_commutingCurved`, `C00_connection_OmegaTermInFieldEquation`, `C00_EL_commutingGeneralSmoothU` | in curved space the field equations are gamma^mu D_mu Psi = (m + U'(S)) Psi and (D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar, also for an arbitrary smooth potential U; the spin-connection term is nonzero |
| `reality` | `C00_lagrangian_realCommuting`, `C00_lagrangian_coefficientHermiticity` | in curved space the Lagrangian is real for commuting components, and its coefficient matrices have the Hermitian structure that makes it Hermitian for Grassmann components as well |
| `real restriction` | `C00_realRestriction_commutingNonTrivial`, `C00_realRestriction_commutingNotebookContraction`, `C00_realRestriction_relationToL1`, `C00_realRestriction_grassmannCurvedTrivial` | in curved space: the notebook-type Lagrangian is non-trivial for a real commuting field and a pure divergence for a real Grassmann field; (L1) is the complexification of the real Lagrangian |
| `spin connection and gravity` | `C00_connection_nonTrivialCoupling` | the coupling to gravity is non-trivial: curvature of the spin connection, Lichnerowicz formula with the exact coefficient -1/4, second-order equation on shell |
| `EMT: vielbein variation (G1p1, G4p1, G3t1)` | `C00_EMT_vielbeinVariation` | the energy-momentum tensor T_mu_nu obtained by varying the vielbein (all components, general frames) equals the stated formula |
| `EMT: symmetry, reality, conservation, trace, current, general U` | `C00_EMT_symmetricAndReal`, `C00_EMT_conservationOnShell`, `C00_EMT_traceOnShell`, `C00_current_conservationAndReality`, `C00_EMT_generalSmoothU`, `C00_EMT_observerSplitGaussianNormal` | T_mu_nu is symmetric, real, conserved on shell, has trace -m S + 7 S U'(S) - 8 U(S); the current Psibar gamma^mu Psi is conserved; energy splits into kinetic and potential parts |
| `EMT: homogeneous equations of state (G3)` | `C00_EMT_homogeneousEquationsOfState` | for a homogeneous field: rho = m S + U, pressure p = S U' - U in all seven directions, w = p/rho |
| `commuting field: charge and energy` | `C00_charge_indefinite`, `C00_energy_unboundedBelow` | for the COMMUTING field the charge density Psi^dagger B Psi has no fixed sign and the classical energy is unbounded below (explicit exact solutions) |
| `primordial field (Stage-2 chart)` | `C00_primordial_geometryMatchesStage2`, `C00_primordial_ELcommuting`, `C00_primordial_homogeneousState`, `C00_primordial_staticFieldSourcedExactly` | in the primordial field: the field equations, an exact homogeneous solution, and a homogeneous commuting state whose T_mu_nu equals the Einstein tensor of the static primordial field exactly (rho = -21 H^2/kappa, p = 15 H^2/kappa, w = -5/7) |
| `static warped form and 2x2 blocks (Stage 4)` | `C00_static_geometryAndReducedEquation`, `C00_static_blocksFromStage4Theory`, `C00_static_classicalModeIsKreinWeightedKS`, `C00_static_classicalEnergyKreinSigned`, `C00_static_KSorbitalEnergySplit` | the Stage-4 static warped chart and its eight 2x2 blocks; the classical energy of a mode has the sign of its block (negative in four of the eight blocks) |
| `citations` | `C00_citation_stage1to4ReportsMatchSources` | the cited checks of the committed Stage-1, -2 and -4 Wolfram reports are true and each report's recorded sha256 of its source equals the sha256 of that file now |

Three further checks complete the 46: `C00_internal_noException` (no step threw an error), `C00_EL_identicalFormBothStatistics` (a combination of four checks above) and `C00_verifier_expectedCheckCount` (added by the script: the package returned exactly 45 checks, so no check was skipped silently).

**About "conjugation".** The set uses Hermitian conjugation (Psi^dagger, and in the Grassmann algebra (theta1 theta2)^* = theta2^* theta1^*). It does not define or use a charge-conjugation operation, and none of its 46 checks is about charge conjugation. (The matrix C above is the 16x16 matrix that forms Psibar; it is not a charge conjugation.)

Besides the checks the report records 32 "measurements" (exact values and descriptive statements per step, for example `massTerm.commutingExplicit` with the characteristic polynomial of C, (x - 1)^8 (x + 1)^8), and the script writes a second file, the "theory file", with the exact formulas and data of this Stage-5 theory for later programs.

**Documents that cite its results.**

* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and its `.tex` and `.pdf`) with its chapters `provenance/textbook/chapters/00-how-to-read.md`, `06-two-fields-and-lagrangians.md`, `07-field-equations-and-emt.md`, `14-kohn-sham-dirac16complex00.md`, `15-pairing-theorems.md`, `16-pairs-of-universes.md`, `18-open-problems.md`, `19-reproducing-everything.md` (Section 19.10 gives the command, a run time and the run-to-run difference of `charPolyC` that this verification fixed) and `20-glossary-and-check-index.md`. They quote "46 of 46" checks and use the results on the Lagrangian, the field equations, the energy-momentum tensor, the indefinite charge and the unbounded classical energy of dirac16complex00.
* `handoff/specs/STAGE5_SPEC.md` (the specification of Stage 5: its sections 1 to 3 define what this set proves, its section 6 names the set and its report as a Stage-5 deliverable) and `HANDOFF.md` (the status table).

**Programs that read its output files.** `scripts/check_dirac16complex00.py`, the independent sympy checker of Stage 5, reads both output files by default, compares every exported number and formula with its own derivation (its check `S5_agreesWithWolfram`) and records the sha256 of both files in its report `artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json` (key `inputSha256`). The unit test `tests/test_d16c_stage5_dirac16complex00.py` enforces these records: its test `CommittedReportTests.test_committed_report_is_complete_true_and_current` requires that every `inputSha256` entry of the committed Python report equals the sha256 of that file now. Therefore, whenever the bytes of either output file of this set change, the Python report must be regenerated (with `python scripts/check_dirac16complex00.py`) and committed together with them; otherwise that test fails (measured on 2026-10-02, Part 6.3). The unit test `tests/test_d16c_textbook_publication.py` requires the count 46 for `wolfram-dirac16complex00-report.json`. No other program reads the two files.

## 2. Files

All files are pure ASCII with LF line endings. The repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values below are the same on Windows, macOS and Linux. The values are those of the fixed state of 2026-10-02 (Part 6.3); of the files of this set only the package and the two output files changed in the fix (the fix also regenerated the report of the Python checker, which is not part of this set), and their values before the fix are given in Part 6.3. Every value in this Part was measured again on 2026-10-07 at commit `a4c5eda` (and is the same at its successor `8cbd03a`, which changed only `HANDOFF.md` and a file in `Revision/workflows/`): all unchanged (Part 6.5).

**The two program files of the set.**

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `scripts/verify_dirac16complex00.wls` | the script you run: loads the package, calls `D16C00Run`, adds the check `C00_verifier_expectedCheckCount`, computes the sha256 of 11 files, writes the report and the theory file, prints the verdict, sets the exit code | 89 | 6470 | `3b143538660106ea25f7908640ff79fc11cf74e99d70405cd6083546da33a4e2` |
| `wolfram/Dirac16Complex00.wl` | the package (context ``Dirac16Complex00` ``): every check, the measurements and the exported theory; public function `D16C00Run[repoRoot]` | 1237 | 122169 | `62b6e269367dbb0554ab0a4a4a4b9a29a35e0ca210a98a7ba7b86bd3735ab880` |

**Packages it loads (read only).** The package loads three packages of earlier stages from the same folder `wolfram/` (with `Get`, only if they are not loaded yet) and calls some of their private functions:

| File | Stage | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `wolfram/Dirac16ComplexGeometry.wl` | 1 (exact jets of the geometry, Lagrangian and EMT jets, Grassmann algebra, test geometries G1, G2, G3) | 997 | 71636 | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` |
| `wolfram/Dirac16ComplexPrimordial.wl` | 2 (the primordial field in the chart z = 6 H x0, t = H x4) | 1224 | 101130 | `0b95682601ace6343a89ad8eaf0f4896d071015041f15cccbeb3beac193d81a1` |
| `wolfram/Dirac16ComplexKohnSham.wl` | 4 (the static warped chart, the 2x2 block basis) | 845 | 84969 | `5f8d4703ad848f2d2ba5d33497d402da791584fe6777d668f7c626e7de35c65b` |

**Data files it reads (read only).** The package imports six JSON files and computes the sha256 of a seventh file:

| File | Read by | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | step `fixture and algebra` (the exact gamma matrices, C, B, S^ab of Stage 1) | 18440 | 213133 | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` |
| `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` | steps `static warped form ...` (the 2x2 blocks) and `citations` | 4537 | 72176 | `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` |
| `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json` | step `citations` | 350 | 42018 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` |
| `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` | step `citations` | 2638 | 49440 | `d43adeeba580bdd8cec56fac5fa74906b7578c06c8589e52dbe3da1404cd49e7` |
| `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` | step `citations` | 190 | 13638 | `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` |
| `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` | step `citations` | 154 | 7079 | `9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978` |
| `wolfram/Dirac16ComplexAlgebra.wl` | step `citations` (only its sha256 is computed and compared with the algebra report; the file is not loaded) | 1299 | 82215 | `ba0d00c818fa3707f04f7b2a7478b0c635fbf9fdaaa08b2e036d2704180f2262` |

The step `citations` requires that the sha256 recorded in each cited report for its source package equals the sha256 of that package now; if one of these packages is changed without regenerating its report, the check `C00_citation_stage1to4ReportsMatchSources` becomes false.

The script computes the sha256 of 11 files and writes them into both output files as `sourceSha256`: the two program files, the three loaded packages, the fixture, `kohn-sham-theory.json` and the four cited reports. It reads nothing else: no other file, no environment variable, nothing from the network. The script finds the package relative to its own location (`<repository root>/wolfram/Dirac16Complex00.wl`), and the package finds the other packages next to itself and the data files below the repository root, so the files are found from any current directory.

**Outputs.** Two files. The first argument of the script is the report path; a relative path is taken relative to the **repository root** (the parent folder of `scripts/`), not to the current directory, and an absolute path is used as given. The theory file is always written next to the report, with the fixed name `dirac16complex00-theory.json`. Missing folders are created. Without an argument the report path is the committed one:

| File | Lines | Bytes | sha256 |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` | 1793 | 75677 | `572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261` |
| `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json` | 2613 | 59492 | `bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5` |

Both are JSON, pure ASCII, LF line endings, indented with tabs, with a final newline; exact fractions are written as strings such as `"125/6"` and complex numbers as pairs `["re", "im"]`. The report has the top-level keys `schemaVersion` (1), `producer` (the script, the package and the Wolfram Language version, here `15.0.1`), `checks` (46 entries), `measurements` (32 entries) and `sourceSha256` (11 entries). The theory file has `schemaVersion`, `producer`, `description`, `sourceSha256` and the 12 sections `conventions`, `fields`, `lagrangian`, `realRestriction`, `fieldEquations`, `emt`, `energySplits`, `commutingFieldSpecifics`, `primordial`, `static`, `testGeometries` and `exactValues`.

## 3. How to run it

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs: the Wolfram Language *kernel* (the computing engine) and *WolframScript* (the command `wolframscript`, which runs a script file with the kernel). The verification used the kernel version 15.0.1 and WolframScript 1.14.0. You do not need Python, Jupyter or any other program for this set (only git, Part 3.2).

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page; create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded `.exe` file and accept the defaults. The installer also installs WolframScript and adds it to the PATH. Close every PowerShell window and open a new one afterwards.
   * macOS: open the downloaded `.dmg` file and follow its instructions (drag the application into Applications and open it once).
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/ (Windows `.msi`, macOS `.pkg`, Linux `.deb` with `sudo apt install ./<file>.deb` or `.rpm` with `sudo dnf install ./<file>.rpm`), and open a new terminal.
3. Activate it. In a terminal (PowerShell on Windows, Terminal on macOS and Linux) type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. This needs an internet connection once. (Running `wolframscript` without options on a not yet activated engine asks the same questions. If it shows the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.)

**Option 2: Wolfram (formerly Mathematica), the desktop product.** If you have a licensed Wolfram or Mathematica installation, it contains the kernel; on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/ as in step 2 above.

**Test the installation.** In a new terminal type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux (they stop the shell from replacing `$Version`); in PowerShell they are also correct. If several versions are installed, `wolframscript` uses the newest one; `wolframscript -configure` prints its settings, whose line `WOLFRAMSCRIPT_KERNELPATH=...` names the kernel (a leading `//` means that this is the automatic choice). To use a particular installed kernel, add `-local "<path of that kernel>"` before `-file`, for example `wolframscript -local "C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -file ...` on the verification machine.

**Which version.** Both output files record the Wolfram Language version in their `producer` line. Only version 15.0.1 reproduces the committed files byte for byte. With another version the `producer` lines differ, and other lines may differ if that version prints expressions differently; then compare the check verdicts and the values instead of the bytes (Part 4.4). Versions other than 15.0.1 were not tested.

### 3.2 Get the repository

Install git if you do not have it (Windows: https://git-scm.com/download/win, accept the defaults; macOS: type `xcode-select --install` in Terminal; Debian/Ubuntu Linux: `sudo apt install git`; Fedora: `sudo dnf install git`). Then, in the folder where you want the repository (on Windows preferably a short one such as `C:\work`, because some file paths in the repository are long and Windows limits paths to 260 characters by default):

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone occupies about 700 MB on disk (691 MB, of which 204 MB in the folder `.git`, measured on 2026-10-07; 520 MB on 2026-10-02: the repository grows). Every command below is typed in this folder, the *repository root* (the folder that contains `scripts`, `wolfram` and `artifacts`). Check that the two program files are the ones described here (Part 2): in PowerShell `Get-FileHash -Algorithm SHA256 scripts/verify_dirac16complex00.wls, wolfram/Dirac16Complex00.wl`, on macOS `shasum -a 256 scripts/verify_dirac16complex00.wls wolfram/Dirac16Complex00.wl`, on Linux `sha256sum scripts/verify_dirac16complex00.wls wolfram/Dirac16Complex00.wl` (PowerShell prints the values in capital letters; compare them ignoring case). If `wolfram/Dirac16Complex00.wl` has the sha256 `91d2e47a80f18b953cfea262f6f85205eccbc7caf4dbc2bdf7ea840e6045015c` instead, your clone is from before the fix of 2026-10-02 (Part 6.3): bring it up to date with `git pull`.

### 3.3 Run it

The usage line in the script's header is

```
wolframscript -file scripts/verify_dirac16complex00.wls artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json
```

It is the same single line in Windows PowerShell, in the macOS Terminal (zsh) and in a Linux terminal (bash). It **overwrites the two committed output files** `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json` with the newly computed ones. With Wolfram 15.0.1 and the fixed package the new files are byte-identical to the committed ones, so nothing changes (Part 5 says how to restore the files if they do change).

**Recommended for students: write the output files to a scratch folder instead**, so that the committed files are never touched, and then compare. The folder `build/` is ignored by git (rule `/build/` in `.gitignore`), and the script creates missing folders itself; the theory file is written into the same folder as the report.

Windows PowerShell:

```
New-Item -ItemType Directory -Force build/s5-00 | Out-Null
wolframscript -file scripts/verify_dirac16complex00.wls build/s5-00/wolfram-dirac16complex00-report.json > build/s5-00/stdout.txt
"exit code: $LASTEXITCODE"
Get-Content build/s5-00/stdout.txt -Tail 6
```

macOS (Terminal, zsh) and Linux (bash):

```
mkdir -p build/s5-00
wolframscript -file scripts/verify_dirac16complex00.wls build/s5-00/wolfram-dirac16complex00-report.json > build/s5-00/stdout.txt
echo "exit code: $?"
tail -n 6 build/s5-00/stdout.txt
```

(The first line creates the folder for the saved screen output `stdout.txt`; without `> build/s5-00/stdout.txt` the 99 lines are printed on the screen instead.) The run takes about 4 to 7.5 minutes on the verification machine (257 to 398 s measured on 2026-10-02 and 420 to 426 s on 2026-10-07, depending on how many other programs were running; Part 4.3). The script prints one progress line at the start of each step, for example `[06:17:54] fixture and algebra`; the step `EMT: vielbein variation (G1p1, G4p1, G3t1)` alone takes about 1.5 to 2.5 minutes (93 to 146 s measured), and the check and measurement lines come at the very end. In bash and zsh the progress lines reach `stdout.txt` while the run goes on. In PowerShell 7 `stdout.txt` stays empty (0 bytes) until the run has ended and then receives all 99 lines at once. In Windows PowerShell 5.1, the version built into Windows, the progress lines appear in `stdout.txt` while the run goes on, and the file is written in UTF-16 (it starts with the two bytes FF FE) instead of plain text; `Get-Content` reads it correctly. (All three behaviours measured on 2026-10-02.) Do not interrupt it. (These commands were tested in PowerShell 7.6.6, in Windows PowerShell 5.1.26100 and in Git Bash.)

Then compare the two new files with the committed ones. Windows PowerShell:

```
foreach ($f in 'wolfram-dirac16complex00-report.json', 'dirac16complex00-theory.json') {
  $new = (Get-FileHash -Algorithm SHA256 "build/s5-00/$f").Hash.ToLower()
  $old = (Get-FileHash -Algorithm SHA256 "artifacts/dirac16complex/pair-creation/$f").Hash.ToLower()
  if ($new -eq $old) { "$f identical $new" } else { "$f DIFFERENT new $new committed $old" }
}
```

macOS:

```
shasum -a 256 build/s5-00/*.json artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json
cmp build/s5-00/wolfram-dirac16complex00-report.json artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json && echo "report identical"
cmp build/s5-00/dirac16complex00-theory.json artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json && echo "theory identical"
```

Linux: the same three lines with `sha256sum` instead of `shasum -a 256`.

PowerShell must print `wolfram-dirac16complex00-report.json identical 572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261` and `dirac16complex00-theory.json identical bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5`; on macOS and Linux the report's two sha256 values must both be `572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261`, the theory file's both `bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5`, and `cmp` must print `report identical` and `theory identical`.

**Important: never put `--` before the report path.** WolframScript 1.14 treats `--` as its option `-args`, and when it is combined with `-file` it drops `--` and every argument after it. The script then sees no path and writes to the committed paths. (The script removes a `--` that does arrive, but WolframScript drops the path before the script can see it.)

### 3.4 If it fails

| What you see | Cause and fix |
| --- | --- |
| PowerShell: `The term 'wolframscript' is not recognized`; macOS/Linux: `command not found: wolframscript` | WolframScript is not installed or not on the PATH. Open a new terminal after the installation. On Windows the program is in `C:\Program Files\Wolfram Research\WolframScript\`; add that folder to the PATH or install again. On macOS and Linux install WolframScript separately (Part 3.1, step 2). |
| A message containing "licence"/"license", "password", "activate", "kernel limit", "too many kernels", "maximum number of" or "could not launch/start/connect" | The kernel is not activated, or your licence allows fewer kernels at the same time than are running. Run `wolframscript -activate` again; close other Wolfram programs and notebooks; wait 30 seconds and run again. The first activation needs an internet connection. |
| `FATAL: module failed to load (or produced messages): <path>`, then `check_count=0`, `failed_check_count=1`, exit code 2 | The package `wolfram/Dirac16Complex00.wl` or one of the three packages it loads is missing, damaged or changed, or your Wolfram version prints a warning while loading it. Compare the sha256 values of the program files and packages with Part 2; if they differ, run `git checkout -- wolfram scripts/verify_dirac16complex00.wls` or clone again. No output file was written (only a missing output folder may already have been created). |
| `INTERNAL ERROR: ...` and `check_C00_internal_noException=false`, exit code 1 | A step was stopped by an internal `Throw` in one of the package's helper functions: the step met an equation system that is not linear where a linear one is expected (`Throw["nonlinear"]` in `wolfram/Dirac16Complex00.wl`, `Throw["nonlinear on-shell system"]` in `wolfram/Dirac16ComplexGeometry.wl`), or an exact-ring reduction of the Stage-2 or Stage-4 helpers failed (`Throw[{"ringIncomplete", ...}, ...]` and similar in `wolfram/Dirac16ComplexPrimordial.wl` and `wolfram/Dirac16ComplexKohnSham.wl`). Only these `Throw`s produce this line: the driver `D16C00Run` catches `Throw`, not Wolfram messages, so a missing or unreadable data file does NOT produce it (it produces message lines and a false check, next row). It means that a package was changed or that your Wolfram version computes differently (an untested version). Compare the sha256 values of the program files and packages with Part 2, restore changed files with `git checkout -- wolfram scripts/verify_dirac16complex00.wls`, and use Wolfram 15.0.1 if possible. The output files ARE written in this case, with the checks of the unfinished steps missing or false; restore them (Part 5) if you used the committed paths. |
| Lines `  CHECK FAILED: <name>`, a line `check_<name>=false`, `failed_check_count` larger than 0, exit code 1 | A check is false. If Wolfram message lines such as `Import::nffil: File ... not found during Import.` or `FileHash::noopen: Cannot open ...` appear (standard output then has more than 99 lines), a data file of Part 2 is missing or unreadable: restore it with `git checkout -- <file>` (or clone again) and run again. (Measured on 2026-10-02 with `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` deleted: the lines `Import::nffil: ...` and `Part::pkspec1: ...` after the first progress line, then `  CHECK FAILED: C00_fixture_matchesStage1Construction`, all 14 steps and `done in <n> s`, then `FileHash::noopen: Cannot open ...algebra-fixture.json.`; only `check_C00_fixture_matchesStage1Construction=false`, `check_C00_internal_noException=true`, `failed_check_count=1`, exit code 1, nothing on the error stream, and both output files written.) Without such message lines the computed mathematics differs from the committed result. Do not edit anything to make it pass. Check the sha256 values of every file in Part 2; if they are the listed ones, report the failing check names and your Wolfram version. If only `check_C00_citation_stage1to4ReportsMatchSources=false`: one of the cited Stage-1, -2 or -4 packages was changed without regenerating its report (Part 2). If only `check_C00_verifier_expectedCheckCount=false`: the line `module_check_count=` is not `45 (expected 45)`, so the package was changed. |
| `FATAL: D16C00Run did not return an Association ...` or `FATAL: JSON export failed for <path>`, exit code 2 | The package was changed or an untested Wolfram version behaves differently. Restore the files (`git checkout -- wolfram scripts`) and use Wolfram 15.0.1 if possible. |
| The output files appear in `artifacts/...` although you gave another path | You typed `--` before the path (Part 3.3). Remove it, and restore the committed files with `git checkout -- artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`. |
| The output files appear in `<repository root>/build/...` although you started the command in another folder | Expected: a relative report path is taken relative to the repository root, not to the current folder (Part 2). Give an absolute path if you want the files elsewhere. |
| The new files differ from the committed ones, but all 46 checks are true | Most likely another Wolfram version: compare the `producer` lines (Part 4.4). If the only difference in the report is the `charPolyC` line and it contains `x$` followed by a number, your package is the old one from before the fix of 2026-10-02 (sha256 `91d2e47a...`, Part 6.3): update the repository with `git pull`. If you edited a program file, its `sourceSha256` entries change too. |
| PowerShell says the path to `stdout.txt` could not be found | The folder `build/s5-00` does not exist yet: run the `New-Item` line first. |
| It runs much longer than 7.5 minutes | Slower or busier computers need longer; the computation is exact and runs in one kernel. Let it finish. If you stop it with Ctrl+C, no output file is written (they are written only after the computation) and the old ones are left unchanged. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly 99 lines on standard output (on Windows with CRLF line ends, on macOS and Linux with LF) and nothing on the error stream:

* 15 progress lines, printed while the computation runs: one per step, `[hh:mm:ss] <step name>` with the 14 step names of Part 1 in that order, from `[hh:mm:ss] fixture and algebra` to `[hh:mm:ss] citations`, and then `[hh:mm:ss] done in <n> s` (hh:mm:ss is the time of day; n was 257 to 395 on the verification machine on 2026-10-02 and 415 to 421 on 2026-10-07);
* 46 lines `check_<name>=true`, one per check, sorted by name in the Wolfram Language's order, from `check_C00_algebra_anticommutatorTotallyAntisymmetric=true` to `check_C00_verifier_expectedCheckCount=true`;
* 32 lines `measurement_<name>=<value>`, from `measurement_algebra.anticommutatorStructure=...` to `measurement_static.reducedEquation=...` (some are very long single lines of JSON; the longest has 25665 characters);
* the six final lines. With the usage line of Part 3.3 they are

```
module_check_count=45 (expected 45)
check_count=46
failed_check_count=0
elapsed_seconds=<n>
report=<repository root>/artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json
theory=<repository root>/artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json
```

where `<repository root>` is printed as the full path of your clone (on Windows with backslashes, for example `report=C:\work\Dirac_claude\artifacts\dirac16complex\pair-creation\wolfram-dirac16complex00-report.json`), and with the recommended scratch path the last two lines end in `build\s5-00\wolfram-dirac16complex00-report.json` and `build\s5-00\dirac16complex00-theory.json` (with `/` on macOS and Linux).

The exit code is **0**. It is 1 if a check is false or the package did not return exactly 45 checks (then lines `  CHECK FAILED: <name>` appear among the progress lines, the check lines show `=false` and `failed_check_count` is larger than 0), and 2 if the package cannot be loaded or the JSON cannot be produced (Part 3.4). In PowerShell the exit code is in `$LASTEXITCODE`, in bash and zsh in `$?` (read it immediately after the command).

Measurement values worth looking at in the report (the file): in the entry `massTerm.commutingExplicit` the values `"SMinus":-2`, `"SPlus":2`, `"SNull":0` and `"charPolyC":"(-1 + x)^8*(1 + x)^8"` (the characteristic polynomial of C); in `primordial.staticSource` the values `"rho":-21`, `"p":15`, `"w":"-5/7"`, `"KE_L":-3`, `"PE_L":-18`; in `algebra.pinModule` the values `"commutantOfGammas":1`, `"commutantOfSpinGenerators":2`; in `connection` the value `"lichnerowiczC":"-1/4"` at every point (7 times). **On the screen and in `stdout.txt` these values look slightly different.** The printed measurement lines (`measurement_<name>=...`) are written as compact one-line JSON in which every `/` inside a string is written as `\/` (the script prints them with the Wolfram Language's JSON export and does not undo this escaping, which it does undo for the two files). So the printed lines contain `"w":"-5\/7"` and `"lichnerowiczC":"-1\/4"` (7 times), and a search of the screen output or of `stdout.txt` for `"w":"-5/7"` or `"lichnerowiczC":"-1/4"` finds nothing; search for `-5\/7` and `-1\/4` instead. Values without a `/`, such as `"rho":-21`, `"SMinus":-2` and `"charPolyC":"(-1 + x)^8*(1 + x)^8"`, look the same in both. (Measured on 2026-10-07: the 99 printed lines of a run contain 210 occurrences of `\/` on 14 lines, the report contains none.)

### 4.2 The output files

The two files written at the given place must be byte-identical to the committed ones:

* `wolfram-dirac16complex00-report.json`: 75677 bytes, 1793 lines, sha256 `572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261`;
* `dirac16complex00-theory.json`: 59492 bytes, 2613 lines, sha256 `bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5`.

How to compare them: Part 3.3. The printed `check_` and `measurement_` lines carry the same entries as the report's `checks` and `measurements`, in the same order, but not as the same text: in the report each entry is spread over several lines indented with tabs and a `/` is written as `/`, while each printed measurement line is compact one-line JSON in which a `/` inside a string is written as `\/` (Part 4.1). Compare the files, not the printed lines, with the committed files.

To print a one-line summary of the report's checks (replace the path by the report you want to inspect):

Windows PowerShell:

```
$r = Get-Content -Raw build/s5-00/wolfram-dirac16complex00-report.json | ConvertFrom-Json
$c = @($r.checks.PSObject.Properties)
"checks=" + $c.Count + " true=" + @($c | Where-Object { $_.Value -eq $true }).Count
```

macOS and Linux:

```
wolframscript -code 'c = Import["build/s5-00/wolfram-dirac16complex00-report.json", "RawJSON"]["checks"]; "checks=" <> ToString[Length[c]] <> " true=" <> ToString[Count[Values[c], True]]'
```

Both must print `checks=46 true=46`. (Without Wolfram, `grep -c '"C00_[A-Za-z0-9_]*":true' build/s5-00/wolfram-dirac16complex00-report.json` must print 46 and the same command with `false` instead of `true` must print 0.)

### 4.3 Run time and memory

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 logical processors, 191 GB RAM, Windows 11 Pro for Workstations 10.0.26200, Wolfram 15.0.1, WolframScript 1.14.0), with about ten other Wolfram kernels of other jobs running at the same time (the CPU load was 93 % when it was measured during run 1):

| Run | Shell | Package | Wall time | Computation (`elapsed_seconds`) |
| --- | --- | --- | --- | --- |
| 1 | PowerShell 7.6.6 | before the fix | 319 s | 315 s |
| 2 | Git Bash | before the fix | 348 s | 345 s |
| 3 | PowerShell 7.6.6 | fixed | 351 s | 346 s |
| 4 | Git Bash | fixed | 350 s | 345 s |
| 5 | PowerShell 7.6.6 | fixed | 350 s | 344 s |
| 6 | PowerShell 7.6.6 (student commands, scratch folder) | fixed | 307 s | 305 s |
| 7 | Git Bash | fixed | 306 s | 302 s |
| 8 | Windows PowerShell 5.1.26100 (student commands, scratch folder) | fixed | 392 s | 387 s |
| 9 | PowerShell 7.6.6 (student commands, scratch folder) | fixed | 391 s | 386 s |
| 10 | Git Bash, `algebra-fixture.json` deleted (failure test, exit code 1) | fixed | 398 s | 395 s |

Runs 8, 9 and 10 ran at the same time as each other and as two runs of the Python checker (Part 6.3), next to the kernels of other jobs; that is why they took longer. An independent verifier ran the set five more times on the same machine on the same day, from fresh clones with the fix (runs A to E; run A in PowerShell 7.6.6, run B in Git Bash, run D in Git Bash with `algebra-fixture.json` deleted, run E in Windows PowerShell 5.1): `elapsed_seconds` 260, 260, 257, 259 and 270 s, wall times 263.5 s, about 263 s, 261.5 s, 263 s and 273.5 s. So a run takes 257 to 398 s on this machine, depending on its load.

On 2026-10-07 (Part 6.5; the same machine, now Windows 11 Pro for Workstations 10.0.26300, the same Wolfram and WolframScript) three runs ran at the same time as each other and next to about 14 Wolfram kernels of other jobs (17 `wolfram.exe` processes in all, CPU load 100 % when measured during the runs): run R1 (PowerShell 7.6.6, usage line) 425.9 s wall time, `elapsed_seconds=421`; run R2 (Git Bash, usage line) 425.0 s, `elapsed_seconds=420`; run R3 (PowerShell 7.6.6, the student commands of Part 3.3) `elapsed_seconds=415` (419.5 s for all its commands including the comparison and the summary). Where the time went in run R1: `fixture and algebra` 4 s, `flat: ...` 1 s, `test geometries ...` 19 s, `Euler-Lagrange equations ...` 78 s, `reality` 53 s, `real restriction` 59 s, `spin connection and gravity` 16 s, `EMT: vielbein variation ...` 145 s, `EMT: symmetry, ...` 36 s, `EMT: homogeneous ...` 3 s, `commuting field: ...` 1 s, `primordial field ...` 2 s, `static warped form ...` 2 s, `citations` 2 s; the first progress line came 4.3 s after the start of `wolframscript`. Peak memory of the kernel: 403.1 MB working set and 730.6 MB private memory (R1), 402.2 MB and 729.6 MB (R2); WolframScript 16.7 MB working set.

Where the time goes (run 3; in the other runs most steps took up to about 15 s more or less, the step `EMT: vielbein variation ...` 93 to 146 s): `fixture and algebra` 4 s, `flat: ...` 1 s, `test geometries ...` 16 s, `Euler-Lagrange equations ...` 66 s, `reality` 50 s, `real restriction` 40 s, `spin connection and gravity` 12 s, `EMT: vielbein variation ...` 116 s, `EMT: symmetry, ...` 33 s, `EMT: homogeneous ...` 3 s, `commuting field: ...` under 1 s, `primordial field ...` 2 s, `static warped form ...` 2 s, `citations` 1 s.

The computation runs in a single kernel; the time depends mainly on the speed of one core. The kernel process (`wolfram.exe`) reached a peak working set of about 0.40 GB (398 to 410 MB in the five runs where it was measured) and a peak private memory of about 0.73 GB (713 to 738 MB); WolframScript itself needs about 17 MB. Have at least 1 GB of free memory.

### 4.4 Comparing with a different Wolfram version

If you do not have version 15.0.1, the bytes of both files differ at least in the `producer` lines. Then check instead that (a) the exit code is 0, (b) the summary of Part 4.2 prints `checks=46 true=46`, and (c) the values agree with the committed files. In PowerShell, `Compare-Object (Get-Content artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json) (Get-Content build/s5-00/wolfram-dirac16complex00-report.json)` lists the differing lines (and the same with `dirac16complex00-theory.json`); on macOS and Linux use `diff artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json build/s5-00/wolfram-dirac16complex00-report.json`. With 15.0.1 there are no differing lines.

## 5. Side effects

**Files in the repository.** The script writes exactly two files, the report at the path you give and the theory file `dirac16complex00-theory.json` in the same folder.

* With the usage line of Part 3.3 it **overwrites the two committed files** `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`. With Wolfram 15.0.1 and the fixed package the new bytes are identical, so `git status --porcelain --untracked-files=all` prints nothing afterwards (measured in run 7 of Part 6, where the run left the bytes of both files unchanged, and again in runs R1 and R2 of 2026-10-07, Part 6.5). (Before the fix the report was rewritten with a different `charPolyC` line, so `git status` showed it as modified: measured in runs 1 and 2, Part 6.)
* With the recommended scratch path it creates the folder `build/s5-00/` (and `build/` if missing) and the two files in it; `build/` is ignored by git, so `git status` stays empty. The saved screen output `build/s5-00/stdout.txt` is created by your terminal, not by the script.
* No other file in the repository is created, changed or deleted (measured with `git status --porcelain --untracked-files=all` after every run). The script writes no log file and leaves no partial file when it is interrupted: both files are written after the computation has finished.
* If a run overwrites the committed output files with DIFFERENT bytes (for example with another Wolfram version), the unit test `tests/test_d16c_stage5_dirac16complex00.py` fails until you restore them (below), because the committed report of the Python checker records the sha256 of both files (Part 1). Restore the files; do not regenerate the Python report to make the test pass unless you intend to commit new output files.

**Temporary files.** None in the system temporary folder: in run 5 `TEMP` and `TMP` pointed at an empty private folder, which was watched every second and stayed empty (and again empty after run R1 of 2026-10-07, Part 6.5). On Windows WolframScript itself keeps a spool file for the kernel's printed output, `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\tmp_<10 random characters>` (it contains the progress lines while the run is going on), and deletes it when the run ends normally (measured: the spool files of runs 1 and 2 were gone after the runs; one left behind after an interrupted run can be deleted). At every start it also rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (238 bytes on the verification machine, unchanged content). While kernels started on the verification machine, an empty lock file `%APPDATA%\Wolfram\Paclets\Temporary\pacletSiteData_15.lock` appeared and was gone again shortly afterwards. On macOS and Linux WolframScript and the kernel keep the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process for the computation (`wolfram.exe` on the verification machine, started as `"C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`, so it talks to WolframScript through shared memory); it runs for the whole computation and exits at the end. In run 5 the watcher also saw a second, short-lived `wolfram.exe` below WolframScript whose command line could no longer be read; on the same machine WolframScript was seen starting such short-lived processes as `wolfram.exe -wlbanner -licenseinfo` (a licence query that ends at once). No parallel kernels are started: the package contains no parallel computation. One kernel licence is in use for about 4 to 7.5 minutes (the length of the run). (Re-measured on 2026-10-07 in the two runs of Part 6.5: the process tree was `wolframscript.exe` with exactly one `wolfram.exe` kernel, started with the same kind of command line, and a `conhost.exe` in the PowerShell run; no other Wolfram process.)

**Network.** None. The script and the packages contain no network calls (no `URL...` function, no web `Import`, no external program). During run 5 the whole process tree (WolframScript and the kernels) was watched every second and had no TCP connection and no UDP endpoint; the same was measured in runs R1 and R2 of 2026-10-07 (Part 6.5). (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of this script.)

**Restoring the committed state.** If the committed files were overwritten with different bytes (for example by another Wolfram version), restore them with

```
git checkout -- artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json
```

and remove the scratch folder with `Remove-Item -Recurse -Force build/s5-00` (PowerShell) or `rm -rf build/s5-00` (macOS, Linux). Afterwards `git status --porcelain` must print nothing.

## 6. Verification record

### 6.1 Date, commits, environment

* Date: 2026-10-02 (Parts 6.1 to 6.4). The set was verified again on 2026-10-07 at a later commit that contains the fix (Part 6.5).
* Commits verified: `45d47343ae480df46e06689ed822b8f9a88a8030` (run 1) and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (runs 2 to 10 and the Python checks of Part 6.3) of https://github.com/once-ere/Dirac_claude.git, branch `main`. Between the two commits only `Revision/tests/test_pair_creation_proofs_publication.py` changed; every file of Part 2 had the same sha256 in both commits (the package and the two output files with their values from before the fix, Part 6.3). Before the fix the package and the two output files had last been changed in commit `63598d50e41da3b256a2d153fda1c9918be26d7c` (2026-09-30), the script in `25747ff` (2026-09-30).
* Environment: Windows 11 Pro for Workstations 10.0.26200, Intel Core Ultra 9 275HX (24 logical processors), 191 GB RAM; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`, Professional licence; WolframScript 1.14.0; PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444 and Git Bash (GNU bash 5.2.37, git 2.51.2.windows.1); for the Python checks of Part 6.3 Python 3.14.5 with sympy 1.14.0, mpmath 1.3.0 and numpy 2.4.6. About ten Wolfram kernels of other jobs ran on the machine at the same time.
* Fresh clones: twelve separate `git clone https://github.com/once-ere/Dirac_claude.git` into empty scratch folders (`run1`, `run2`, `fix1` to `fix5`, and `c1` to `c5`), never the working copy of the author. Copied into the clones (and nothing else): for runs 3, 4 and 5 the fixed package `wolfram/Dirac16Complex00.wl` (sha256 `62b6e269...`); for runs 6 and 7, and into `c1` to `c4`, the fixed package and the two regenerated output files of Part 2; in `c2` (run 10) the file `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` was then deleted on purpose. Runs 1 and 2 used the clones exactly as cloned, and so did `c5` (the reference for the unit tests of Part 6.3). The fourth fix file, the regenerated Python report, was produced in `c1` (Part 6.3).

### 6.2 The runs

| Run | Clone, shell | Fix files in the clone | Command (from the clone root) | Exit code | Wall time | `elapsed_seconds` | Kernel peak memory (working set / private) | Report sha256 | Theory sha256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `run1` (commit `45d4734`), PowerShell 7.6.6, output to a file | none | usage line | 0 | 319.2 s | 315 | 399 MB / 726 MB | `bf233e49...` (differs from the committed `56022869...`) | `c0b1a3a9...` (= committed) |
| 2 | `run2` (commit `c2b33cc`), Git Bash, output to a file | none | usage line | 0 | 348.0 s | 345 | 410 MB / 738 MB | `bf233e49...` (= run 1, differs from the committed) | `c0b1a3a9...` (= committed) |
| 3 | `fix1` (`c2b33cc`), PowerShell 7.6.6 | fixed package | usage line | 0 | 350.8 s | 346 | 407 MB / 733 MB | `572dc150...` | `bb15900a...` |
| 4 | `fix2` (`c2b33cc`), Git Bash | fixed package | usage line | 0 | 349.9 s | 345 | 398 MB / 725 MB | `572dc150...` | `bb15900a...` |
| 5 | `fix3` (`c2b33cc`), PowerShell 7.6.6, private `TEMP`/`TMP`, network and process watch | fixed package | usage line | 0 | 350.1 s | 344 | not measured | `572dc150...` | `bb15900a...` |
| 6 | `fix4` (`c2b33cc`), PowerShell 7.6.6, the student commands of Part 3.3 typed literally | complete fix | scratch path `build/s5-00/wolfram-dirac16complex00-report.json` | 0 | 307.0 s | 305 | not measured | `572dc150...` (identical to the committed file) | `bb15900a...` (identical) |
| 7 | `fix5` (`c2b33cc`), Git Bash | complete fix | usage line (overwrites the committed paths) | 0 | 306.4 s | 302 | 402 MB / 713 MB | `572dc150...` (unchanged, = committed) | `bb15900a...` (unchanged) |
| 8 | `c3` (`c2b33cc`), Windows PowerShell 5.1.26100.9444, the student commands of Part 3.3 and the summary of Part 4.2 typed literally | the three Wolfram fix files | scratch path `build/s5-00/wolfram-dirac16complex00-report.json` | 0 | 392.3 s | 387 | not measured | `572dc150...` (identical) | `bb15900a...` (identical) |
| 9 | `c4` (`c2b33cc`), PowerShell 7.6.6, the same commands | the three Wolfram fix files | scratch path, as run 8 | 0 | 391.1 s | 386 | not measured | `572dc150...` (identical) | `bb15900a...` (identical) |
| 10 | `c2` (`c2b33cc`), Git Bash, `algebra-fixture.json` deleted (failure test for Part 3.4) | the three Wolfram fix files | scratch path, as run 8 | 1 | 398.5 s | 395 | not measured | `343da6ed...` (differs, as expected) | `804d3a89...` (differs, as expected) |

Runs 1 and 2 overlapped by 3 minutes; runs 3, 4 and 5 ran at the same time, and so did runs 6 and 7, and runs 8, 9 and 10 together with the two Python checker runs of Part 6.3 (each in its own clone and its own process), always next to the kernels of other jobs. Wall time is measured from the start of `wolframscript` to its exit; it includes about 3 to 5 seconds for starting the kernel and loading the packages. Memory was polled every second.

**Results.**

* Every run except the failure test run 10: exit code 0, nothing on the error stream, 99 lines on standard output, `module_check_count=45 (expected 45)`, `check_count=46`, `failed_check_count=0`, 46 lines `check_...=true`, 32 measurement lines. All 46 checks true in every report written.
* Before the fix (runs 1 and 2): the theory file was byte-identical to the committed one (`c0b1a3a9...`) in both runs. The report was byte-identical between run 1 and run 2 (`bf233e49...`) but NOT to the committed report (`56022869...`): the only difference was line 1560, `"charPolyC":"(-1 + x$5562)^8*(1 + x$5562)^8"` instead of the committed `"charPolyC":"(-1 + x$5558)^8*(1 + x$5558)^8"`. Correspondingly `git status --porcelain --untracked-files=all` showed ` M artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and nothing else.
* With the fixed package (runs 3 to 9): all seven reports were byte-identical to each other (`572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261`), all seven theory files likewise (`bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5`). Runs 6 and 7, which started from the complete fix, reproduced both fixed output files byte for byte: run 6 wrote them into the scratch folder and they were identical to the files in `artifacts/...`; run 7 wrote over the files in `artifacts/...` and left their bytes unchanged. In both clones `git status --porcelain --untracked-files=all` afterwards listed only the three copied fix files (the scratch folder of run 6 is ignored by git).
* The 99 printed lines of runs 3, 4 and 5 were identical apart from the times of day, `elapsed_seconds` and the folder names in the last two lines; they differed from the lines of runs 1 and 2 only in the measurement line `measurement_massTerm.commutingExplicit` (the `charPolyC` value).
* Run 5 (private `TEMP`/`TMP`, network and process watch): no temporary file appeared in the private temporary folder, no TCP connection and no UDP endpoint of WolframScript or the kernel; process tree as described in Part 5.
* Run 6 followed the student commands of Part 3.3 literally (PowerShell, scratch folder): exit code 0; the last six lines of `stdout.txt` were the six final lines of Part 4.1; both files `identical` with the sha256 values of Part 2; the summary printed `checks=46 true=46`; `git status --porcelain --untracked-files=all` listed only the three copied fix files. `stdout.txt` had 99 lines (CRLF) and was empty until the run ended.
* Runs 8 and 9 repeated the student commands of Part 3.3 and the summary of Part 4.2 in Windows PowerShell 5.1 and PowerShell 7: in both, `exit code: 0`, the six final lines of Part 4.1, both files `identical` with the sha256 values of Part 2, `checks=46 true=46`, 99 lines in `stdout.txt`, and `git status --porcelain --untracked-files=all` afterwards listed only the three copied fix files. The 99 printed lines of runs 8 and 9 were identical apart from the times of day, `elapsed_seconds` and the folder names. `stdout.txt` was polled every 10 seconds: in run 9 (PowerShell 7) it had 0 bytes until the run ended (last poll during the run at 07:07:25, run end 07:07:28.9) and then 65964 bytes of plain ASCII; in run 8 (Windows PowerShell 5.1) it started with the bytes FF FE (UTF-16 LE), grew while the run went on (352 bytes at 07:01:09, 564 bytes with six progress lines from `[07:01:00] fixture and algebra` to `[07:03:36] real restriction` at 07:03:52, 906 bytes at 07:06:54) and had 131930 bytes at the end.
* Run 10 (failure test, `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` deleted, Git Bash): 106 lines on standard output, nothing on the error stream (0 bytes), exit code 1. After the first progress line came `Import::nffil: File ...algebra-fixture.json not found during Import.`, `Part::pkspec1: The expression 1 + S[a] cannot be used as a part specification.` and `  CHECK FAILED: C00_fixture_matchesStage1Construction`; all 14 steps ran, `done in 395 s`, then `FileHash::noopen: Cannot open ...algebra-fixture.json.`; no `INTERNAL ERROR` line. The report (written to the scratch folder, as was the theory file) had 46 checks, 45 true, only `C00_fixture_matchesStage1Construction` false, `C00_internal_noException` true, and the `sourceSha256` entry of the missing file read `ToLowerCase[$Failed]`; the final lines were `module_check_count=45 (expected 45)`, `check_count=46`, `failed_check_count=1`. This is the behaviour described in Part 3.4: a missing data file produces Wolfram messages and a false check, not `INTERNAL ERROR`, because the driver `D16C00Run` catches only `Throw` (lines 1157 to 1173 of the package), not messages.

### 6.3 The fix made (execution defect: nondeterministic output formatting)

**Defect.** The committed report could not be reproduced byte for byte: its measurement entry `massTerm.commutingExplicit.charPolyC` (the characteristic polynomial of C) contains the name of a temporary symbol, `x$5558`, whose number differs from run to run. Runs 1 and 2 of this verification wrote `x$5562`; the textbook (`provenance/textbook/chapters/19-reproducing-everything.md`, Section 19.10) had already recorded reruns with `x$5557` and `x$5558`.

**Root cause, with evidence.** In `checkMassTermCommuting[]` of `wolfram/Dirac16Complex00.wl` the variable `x` of `CharacteristicPolynomial[Cm, x]` was declared as a local variable of `Module[...]`. The Wolfram kernel renames such a variable to `x$NNNN`, where NNNN is the current value of the kernel's counter `$ModuleNumber`, and the polynomial is printed with this name into the report. The counter's value is not determined by the script: a 7-line probe script printed `$ModuleNumber` at its first line as 3012, 3012, 3103, 3110 in four runs from Git Bash and 3012, 3110, 3110, 3110 in four runs from PowerShell, and after its first `Import[..., "RawJSON"]` the counter had grown by 272 in some runs and by 279 in another. The kernel's start-up work (which varies from start to start) therefore shifts every later Module number, and with it the printed name. The mathematics is unaffected: the check `C00_massTerm_commutingExplicitSpinors` compares the polynomial with (x - 1)^8 (x + 1)^8 using the same symbol and was true in every run.

**Change.** `wolfram/Dirac16Complex00.wl`, 7 lines added, 2 removed: `x` was removed from the list of local variables of `checkMassTermCommuting[]`, so the polynomial uses the package's private symbol `x` (never assigned anywhere in the package), which prints as plain `x`; a 5-line comment above the function explains why. No check, no number, no tolerance and no other line was changed. The diff:

```
-(* explicit commuting spinors for the mass term; flat dispersion *)
-checkMassTermCommuting[] := Module[{e, pm, pp, p0, sM, sP, s0, cp, x, kk, gk, disp, onK, ns, m0},
+(* explicit commuting spinors for the mass term; flat dispersion.
+   The variable x of the characteristic polynomial is deliberately NOT a Module local: the kernel
+   renames a Module local x to x$NNNN with NNNN = $ModuleNumber, a counter whose value depends on
+   the kernel's start-up history (from the same files, runs printed x$5557, x$5558 and, on
+   2026-10-02, x$5562), and the printed polynomial is written into the report as charPolyC.  The
+   package's private symbol x, which is never assigned, prints as plain x in every run. *)
+checkMassTermCommuting[] := Module[{e, pm, pp, p0, sM, sP, s0, cp, kk, gk, disp, onK, ns, m0},
```

**Regenerated files.** The two Wolfram output files were written by run 3 and installed in the repository; they were identical in runs 3 to 9. The Python report (fourth row) was regenerated as described below. The fix consists of these four files, which belong in one commit together with this provenance file (a clone of a commit that has this provenance file but not the four files fails the hash check of Part 3.2):

| File | Before the fix (commit `63598d5`) | After the fix | What changed |
| --- | --- | --- | --- |
| `wolfram/Dirac16Complex00.wl` | 1232 lines, 121699 bytes, `91d2e47a80f18b953cfea262f6f85205eccbc7caf4dbc2bdf7ea840e6045015c` | 1237 lines, 122169 bytes, `62b6e269367dbb0554ab0a4a4a4b9a29a35e0ca210a98a7ba7b86bd3735ab880` | the change above |
| `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` | 1793 lines, 75687 bytes, `56022869fa7f08338ba9f72cac239ecbc3f822a4e6ee536866c70958d944dc16` | 1793 lines, 75677 bytes, `572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261` | exactly 2 lines: line 1560 `"charPolyC":"(-1 + x)^8*(1 + x)^8",` (was `x$5558`) and line 1781, the `sourceSha256` entry of `wolfram/Dirac16Complex00.wl` |
| `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json` | 2613 lines, 59492 bytes, `c0b1a3a90481426f9e69e40cc43ca76b7bc259bd9b711757f5ee840223d81b5d` | 2613 lines, 59492 bytes, `bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5` | exactly 1 line: line 6, the `sourceSha256` entry of `wolfram/Dirac16Complex00.wl` |
| `artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json` (the report of the independent Python checker `scripts/check_dirac16complex00.py`; not a file of this set) | 2198 lines, 61256 bytes, `df094523942b569aa73fa076e8618260c4b87a0a812f4bdf98251ccd00736150` | 2198 lines, 61256 bytes, `d8d3b1b2f75e60d85e4fb81d2d5e3c6f0343154d2cfc86979ca49b8fd5a9df69` | exactly 2 lines: lines 2195 and 2196, the `inputSha256` entries of `dirac16complex00-theory.json` (was `c0b1a3a9...`, now `bb15900a...`) and `wolfram-dirac16complex00-report.json` (was `56022869...`, now `572dc150...`) |

**Why the Python report had to be regenerated, with evidence.** The Python checker records in `inputSha256` the sha256 of the two Wolfram output files it compared, and the unit test `tests/test_d16c_stage5_dirac16complex00.py` (test `CommittedReportTests.test_committed_report_is_complete_true_and_current`, the loop over `rep["inputSha256"]`) requires each recorded value to equal the sha256 of that file now. Changing the two output files without regenerating the Python report therefore breaks that test. Measured on 2026-10-02 with `D16C_FAST=1 python -m unittest tests.test_d16c_stage5_dirac16complex00 tests.test_d16c_textbook_publication` (in Git Bash; in PowerShell set the variable first with `$env:D16C_FAST = "1"`):

* fresh clone `c5` at `c2b33cc`, unchanged: `Ran 53 tests`, `OK (skipped=1)`;
* fresh clone `c1` with only the three Wolfram fix files: `FAILED (failures=1, skipped=1)`, the failure `AssertionError: 'bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5' != 'c0b1a3a90481426f9e69e40cc43ca76b7bc259bd9b711757f5ee840223d81b5d' : artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json`;
* the same clone with all four fix files: `Ran 53 tests`, `OK (skipped=1)`;
* the whole `tests/` folder (all 21 modules `tests/test_*.py`, 613 tests, `D16C_FAST=1`, about 305 s) gave the same result with all four fix files (`c1`) as without them (`c5`): `FAILED (failures=5, skipped=11)`, with the same five failures in both clones, all in tests of other sets (four in `tests/test_d16c_kohn_sham_notebook.py`, one in `tests/test_d16c_student_guide_publication.py`, which looks for a built Rust program `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe` that a fresh clone does not contain). With all four fix files, no test result differs from that of the unchanged clone.

**How it was regenerated.** In clone `c1` (the three Wolfram fix files in place), from the repository root, with Python 3.14.5 and the packages sympy 1.14.0, mpmath 1.3.0 and numpy 2.4.6 (a student installs them with `python -m pip install sympy mpmath numpy`; the checker imports all three):

```
python scripts/check_dirac16complex00.py
```

which rewrites `artifacts/dirac16complex/pair-creation/python-dirac16complex00-report.json`. Result: exit code 0, nothing on the error stream, `check_count=49`, `failed_check_count=0`, `check_S5_agreesWithWolfram=true` (the independent Python derivation agrees with the fixed Wolfram files) and `check_S5_internal_noException=true`, 402.9 s wall time. A second run at the same time in clone `c4` with `python scripts/check_dirac16complex00.py --output build/py00/python-dirac16complex00-report.json` (exit code 0, the same check lines, 400.3 s) wrote a byte-identical file; the report contains no time or path of the run, so it is deterministic. An earlier run in the clone of run 3 (349 s) had given the same sha256 `d8d3b1b2...`, and so had a run of the independent verifier (320 s). `git grep` in the clone at `c2b33cc` finds no committed file that records the old sha256 `df094523...` of the Python report, so replacing it breaks nothing else.

The script `scripts/verify_dirac16complex00.wls` and the checker `scripts/check_dirac16complex00.py` were not changed. All 46 Wolfram checks, all 49 Python checks and every measurement value other than the symbol name are unchanged.

### 6.4 Open items (no open discrepancy in the mathematics)

* **The Python report's sha256 records (resolved).** The report of the Python checker recorded the sha256 values of the two output files from before the fix, and the unit test `tests/test_d16c_stage5_dirac16complex00.py` enforces these records. The report was therefore regenerated as the fourth fix file (Part 6.3: `df094523...` to `d8d3b1b2...`, exactly the two `inputSha256` lines changed, 49 of 49 Python checks true, the 53 unit tests pass with one skipped). Nothing is open here.
* **The textbook describes the state before the fix.** `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`) and its chapter `provenance/textbook/chapters/19-reproducing-everything.md` (Section 19.10) say that the committed report contains `x$5558`, that a byte comparison of this report can fail on this entry, and that "a permanent fix ... has not been made". After this fix those statements describe the earlier commit. The textbook files were left unchanged (the original textbook is to be preserved).
* No open discrepancy: every check is true in every run with the complete set of files (run 10 deleted a data file on purpose and gave exactly the expected single false check), and with the fix both output files are reproduced byte for byte.

### 6.5 Re-verification on 2026-10-07 (after a session interruption)

The workflow that wrote this file on 2026-10-02 was interrupted by a session limit before its final verify and fix stages had run, so the whole set was run again from fresh clones; nothing of the earlier record was taken on trust. Every statement below was measured on 2026-10-07.

* **Commits.** `a4c5eda1df069a43a55ff8b57148f5de8edd1670` of https://github.com/once-ere/Dirac_claude.git, branch `main` (runs R1, R2 and R3; it contains the fix, committed in `3f0a577` together with this provenance file and the four fix files of Part 6.3), and its successor `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` (run R4 and the unit tests). `8cbd03a` was added on `main` while the runs went on; it changes only `HANDOFF.md` and `Revision/workflows/dirac_matrices_audit.js`, none of the files of Part 2, so all four runs used the same files of this set.
* **Environment.** The machine of Part 6.1, now with Windows 11 Pro for Workstations 10.0.26300; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), WolframScript 1.14.0, PowerShell 7.6.6, Git Bash (GNU bash 5.2.37, git 2.51.2.windows.1), Python 3.14.5 with sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6 (for the unit tests only). About 14 Wolfram kernels of other jobs ran at the same time (CPU load 100 % during the runs).
* **Files.** In the clones `r1`, `r2` and `r3` (after their runs) the sha256, line count and byte count of all 14 files of Part 2 (the two program files, the three loaded packages, the seven files read and the two output files) and of the Python report of Part 6.3 (2198 lines, 61256 bytes, `d8d3b1b2...`) were exactly the values listed there.
* **Fresh clones.** Four separate `git clone https://github.com/once-ere/Dirac_claude.git` into empty scratch folders (`r1` to `r4`); nothing was copied into them (the fix is committed). The clones `r1`, `r2` and `r3` are of commit `a4c5eda` (cloned at 15:18:33, 15:18:48 and 15:20:22 local time); the clone `r4` was made at 15:21:46, after `8cbd03a` had been pushed (15:21:16), and is of that successor of `a4c5eda`, which changes no file of Part 2 (it changes only `HANDOFF.md` and `Revision/workflows/dirac_matrices_audit.js`). Measured afterwards with `git reflog` in each clone (`a4c5eda HEAD@{0}: clone: ...` in `r1` to `r3`, `8cbd03a HEAD@{0}: clone: ...` in `r4`) and `git show --stat 8cbd03a`.

| Run | Clone, shell | Command (from the clone root) | Exit code | Wall time | `elapsed_seconds` | Kernel peak memory (working set / private) | Report sha256 | Theory sha256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | `r1` (`a4c5eda`), PowerShell 7.6.6, output to a file, `TEMP`/`TMP` set to an empty private folder, process and network watch | usage line (overwrites the committed paths) | 0 | 425.9 s | 421 | 403.1 MB / 730.6 MB | `572dc150...` (= committed) | `bb15900a...` (= committed) |
| R2 | `r2` (`a4c5eda`), Git Bash, output to a file, process and network watch | usage line (overwrites the committed paths) | 0 | 425.0 s | 420 | 402.2 MB / 729.6 MB | `572dc150...` (= committed) | `bb15900a...` (= committed) |
| R3 | `r3` (`a4c5eda`), PowerShell 7.6.6, the student commands of Part 3.3 and the summary of Part 4.2 as written there | scratch path `build/s5-00/wolfram-dirac16complex00-report.json` | 0 | 419.5 s (all commands) | 415 | not measured | `572dc150...` (identical) | `bb15900a...` (identical) |
| R4 | `r4` (`8cbd03a`), Git Bash, `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` deleted (failure test for Part 3.4) | scratch path, as R3 | 1 | 426.9 s | 421 | not measured | `343da6ed...` (differs, as expected) | `804d3a89...` (differs, as expected) |

R1, R2 and R3 started within two minutes of each other and ran at the same time; R4 started when R1 and R2 had ended and overlapped R3.

**Results.**

* **Byte identity.** In R1 and R2 the two files written over the committed paths were byte-identical (`cmp`) to the committed blobs of `HEAD` (`git show HEAD:<path>`) and to each other: report `572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261` (1793 lines, 75677 bytes), theory file `bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5` (2613 lines, 59492 bytes). `charPolyC` read `(-1 + x)^8*(1 + x)^8` in both reports. R3 wrote the same two sha256 values into `build/s5-00/`, and its comparison printed `identical` for both files.
* **Printed output.** R1 and R2: exit code 0, 0 bytes on the error stream, 99 lines on standard output (CRLF line ends, 99 CR and 99 LF bytes, 66010 bytes), of them 15 progress lines (the 14 steps of Part 1 in order and `done in 421 s` / `done in 420 s`), 46 lines `check_...=true` (none false, no `CHECK FAILED` line), 32 measurement lines (the longest line has 25665 characters), and the six final lines `module_check_count=45 (expected 45)`, `check_count=46`, `failed_check_count=0`, `elapsed_seconds=421` (R2: `420`), `report=<clone>\artifacts\dirac16complex\pair-creation\wolfram-dirac16complex00-report.json`, `theory=<clone>\artifacts\dirac16complex\pair-creation\dirac16complex00-theory.json`. After replacing the times of day, the `done in` and `elapsed_seconds` values and the clone folders, the standard outputs of R1 and R2 were identical. R3 printed `exit code: 0`, the same six final lines (with `elapsed_seconds=415` and the scratch paths), `wolfram-dirac16complex00-report.json identical 572dc150139ffb8f3203a7ae12d878be72b73f58fa57f1a975b063b3ffd3e261`, `dirac16complex00-theory.json identical bb15900aeba9302be79a431d15579cc490421e3e672d11e79fe81f0699191af5` and `checks=46 true=46`; its `stdout.txt` (99 lines, CRLF, 65956 bytes) was still 0 bytes about one minute before the run ended, as described in Part 3.3 for PowerShell 7. The macOS/Linux summary command of Part 4.2 (`wolframscript -code ...`, run in Git Bash on the committed report) printed `checks=46 true=46`, and the `grep -c` alternative printed 46 for `true` and 0 for `false`.
* **Side effects.** `git status --porcelain --untracked-files=all` printed nothing in `r1` and `r2` after the runs (the files written over the committed paths kept their bytes) and nothing in `r3` (`git status --ignored` listed only the three files in the ignored folder `build/s5-00/`). In R1 the private temporary folder stayed empty. The process watch (every second, the whole process tree below the shell that ran the command) saw, apart from the shell's own helper processes and the watcher, `wolframscript.exe` and exactly one `wolfram.exe` kernel (command line `"C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`), in R1 also a `conhost.exe`; no other Wolfram process, and no TCP connection and no UDP endpoint of the tree (polled every 5 seconds) in either run.
* **Failure test R4.** Exit code 1, 106 lines on standard output, 0 bytes on the error stream; after the first progress line `Import::nffil: File ...algebra-fixture.json not found during Import.`, `Part::pkspec1: The expression 1 + S[a] cannot be used as a part specification.` and `  CHECK FAILED: C00_fixture_matchesStage1Construction`; all 14 steps, `done in 421 s`, then `FileHash::noopen: Cannot open ...algebra-fixture.json.`; no `INTERNAL ERROR` line; `check_C00_internal_noException=true`, 45 checks true and only `check_C00_fixture_matchesStage1Construction=false`, `module_check_count=45 (expected 45)`, `check_count=46`, `failed_check_count=1`; the report's `sourceSha256` entry of the missing file read `ToLowerCase[$Failed]`. Both output files were written to the scratch folder, with exactly the sha256 values of run 10 of 2026-10-02 (`343da6ed238c005809bfd3e6965efce64c80d41ff2a2ab7f6c2090f2ed7948a8`, `804d3a8986ada1f7b917b1ce1694e4445727d57dcb17ec16a6f81b7264e2bee4`): Part 3.4 is confirmed.
* **Unit tests.** In the fresh clone `r4` (commit `8cbd03a`, before the failure test), `D16C_FAST=1 python -m unittest tests.test_d16c_stage5_dirac16complex00 tests.test_d16c_textbook_publication` gave `Ran 53 tests`, `OK (skipped=1)` (23 s): the committed Python report's `inputSha256` records match the two committed output files, and the textbook test finds the count 46.
* **Fix made on 2026-10-07:** none (no execution defect found). **Open discrepancy:** none. The only open item remains the textbook text of Part 6.4, which describes the state before the fix of 2026-10-02.
