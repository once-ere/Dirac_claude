# Execution provenance: the Stage-1 geometry verifier (WolframScript)

Set: `scripts/verify_dirac16complex_geometry.wls` with `wolfram/Dirac16ComplexGeometry.wl` (old Stage 1, "the field in an arbitrary gravitational field").

Verified on 2026-10-02 at commit `45d47343ae480df46e06689ed822b8f9a88a8030` of https://github.com/once-ere/Dirac_claude.git. Result: the set EXECUTES OK (exit code 0, 43 of 43 checks true, `failed_check_count=0`) and reproduces its committed report byte for byte, in two runs from fresh clones. Re-verified the same day at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (two more runs from two more fresh clones, after a review of this file), and again on 2026-10-07 at commits `a4c5eda1df069a43a55ff8b57148f5de8edd1670` and `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` (four more runs from four more fresh clones, after the workflow that wrote this file had been interrupted by a session limit and restarted), and finally on 2026-10-07 at commits `b8a695d1faa7abe43b4b51eb666f25d250420fb7` and `603f1506a143f731ea1661a040110077c920b785` (four more runs from four more fresh clones, two of them with Windows PowerShell 5.1, and three deliberately interrupted runs, after a second independent review of this file whose four findings concerned this file only): every complete run executed OK with 43 of 43 checks true and reproduced the committed report byte for byte. The details are in Part 6.

This file is written for a student who has never used Wolfram software. Everything you need to run the set is in this file; you do not have to read any other file first.

## 1. What this set is and what it computes

**The physics in plain words.** The project studies a field called "dirac16complex": a field with 16 complex components (a "spinor") that lives in an 8-dimensional space-time with 4 space-like and 4 time-like directions. The coordinates are called x0, ..., x7, and x4 plays the role of the time in which the field evolves. The flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). The field values are not ordinary numbers but *Grassmann* numbers: two of them anticommute (theta1 theta2 = -theta2 theta1), as they must for a fermion field.

Stage 1 of the project wrote down how this field behaves in an *arbitrary* gravitational field. Gravity is described by a "vielbein" (a frame) e_mu^a, from which one builds the metric, the Christoffel symbols, the spin connection Omega_mu, the covariant derivative D_mu, the curvature, the Lagrangian of the field, its field equations, its energy-momentum tensor T_mu_nu and its canonical (quantum) structure. The derivations are in the Stage-1 document. This set is the **exact computer check** of those derivations, written in the Wolfram Language.

**What the computer does.** It does not solve differential equations. It checks identities *exactly* (with integers, fractions, and in one geometry with numbers of the form p + q cos z) at chosen test points of three test geometries, and every check is decided with exact numbers. Floating-point numbers appear in only three places: a 30-digit numerical value of det e chooses the sign of sqrt|g| (unless the calculation fixes that sign in advance; the computation then continues exactly with the chosen sign), a 30-digit numerical value selects the entry of largest absolute value reported by the measurements whose names end in `MaxAbs`, and 24 measurements (names ending in `Decimal`) also show a value as a 20-digit decimal. The three test geometries are:

* **G1**: a general, non-diagonal polynomial vielbein, at three points with fractional coordinates;
* **G2**: the "primordial field" of the project (a diagonal vielbein built from cot z, sin(z)^(1/6) and exp(+-a4(t)), with an arbitrary function a4), at three exact points;
* **G3**: a homogeneous "Bianchi-I" (minisuperspace) vielbein that depends on the time x4 only, at three times.

At each point the vielbein, its first and its second derivatives are exact numbers, and every derived object is carried as an exact value together with its eight first derivatives (a "jet"). The Euler-Lagrange equations, the canonical momentum and the original notebook's Lagrangian `Lg[]` are checked in a genuine Grassmann algebra that the package implements itself. The field values at the points are exact fractions from a fixed pseudo-random generator, so every run computes the same numbers.

**The 43 checks.** Each check is `true` when the stated identity holds exactly at every point of the geometry named in its suffix (`_G1`, `_G2`, `_G3`).

| Check | What must hold |
| --- | --- |
| `ALG_cliffordRelations` | {gamma^a, gamma^b} = 2 eta^ab for the eight 16x16 gamma matrices; gamma^0..gamma^3 are symmetric, gamma^4..gamma^7 antisymmetric |
| `ALG_chargeMatrix` | the 16x16 matrix C = gamma^0 gamma^1 gamma^2 gamma^3 is symmetric with C C = 1; C gamma^a and C S^ab are antisymmetric; gamma^0 ... gamma^7 = diag(-1 (8 times), +1 (8 times)) |
| `ALG_grassmannLemmas` | in the Grassmann algebra: derivatives of the quartic term S^2/2 (S = Psibar Psi), S commutes with Psi, Psi^T C Psi = 0 but Psi^T C gamma^0 Psi is not 0 |
| `GEO_frameNondegenerate_G1`, `_G2` | det e is not 0, the metric has 4 positive and 4 negative eigenvalues, g^44 is not 0 |
| `GEO_vielbeinPostulate_G1`, `_G2` | d_mu e_nu^a - Gamma^rho_mu_nu e_rho^a + omega_mu^a_b e_nu^b = 0 (512 values and 4096 first derivatives) |
| `GEO_omegaAntisymmetry_G1`, `_G2` | omega_mu_ab = -omega_mu_ba |
| `GEO_gammaCovariantConstancy_G1`, `_G2` | D_mu gamma^nu = 0 with Omega_mu = (1/2) omega_mu_ab S^ab |
| `GEO_notebookContractionFails_G1`, `_G2` | with the original notebook's contraction (1/2) omega_mu^a_b S^ab instead, D_mu gamma^nu is NOT 0 |
| `GEO_divergenceIdentity_G1`, `_G2` | d_mu(sqrt\|g\| gamma^mu) = sqrt\|g\| Sum_mu [gamma^mu, Omega_mu] and d_mu sqrt\|g\| = sqrt\|g\| Gamma^rho_rho_mu |
| `GEO_curvature_G1`, `_G2` | F_mu_nu = d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu] equals +(1/2) R_mu_nu_ab S^ab (and not the forms with -1/2 or with mixed indices); F is not 0 |
| `GEO_lichnerowicz_G1`, `_G2` | (gamma^mu D_mu)^2 Psi = (spinor Laplacian) Psi + c R Psi with c exactly -1/4 |
| `GEO_diagonalSlashFormula_G2` | for the primordial field gamma^mu Omega_mu equals the diagonal-frame formula and equals 3 H gamma^0 |
| `GEO_primordialInvariants_G2` | sqrt\|g\| = cos z, R = 6 H^2 (a4'^2 - 7), the Einstein tensor has its closed form, exactly 24 nonzero omega_mu_ab |
| `GEO_symbolicJetAgreement_G2` | the fully symbolic geometry of the primordial frame, evaluated at the point, equals the exact jet geometry |
| `LAG_hermiticity_G1`, `_G2` | (C gamma^a)^dagger = -C gamma^a, C^dagger = C, and the Lagrangian density is Hermitian |
| `LAG_eulerLagrangePsibar_G1`, `_G2` | the Grassmann Euler-Lagrange equation for Psi^dagger is sqrt\|g\| C (gamma^mu D_mu Psi - (m + lambda S) Psi) = 0, obtained in two independent ways |
| `LAG_eulerLagrangePsi_G1`, `_G2` | the Grassmann Euler-Lagrange equation for Psi is -sqrt\|g\| ((D_mu Psibar) gamma^mu + (m + lambda S) Psibar) = 0 |
| `LAG_notebookLgGrassmannTrivial_G1`, `_G2` | the original notebook's `Lg[]` for a real Grassmann field: the mass term vanishes and the Euler-Lagrange equation has no derivative terms, so it is not a wave equation |
| `LAG_localSpinInvariance_G1`, `_G2` | finite and infinitesimal local Spin(4,4) transformations: Omega' = R Omega R^-1 - (dR) R^-1, gamma' = R gamma R^-1, g' = g, and the Lagrangian transforms as stated |
| `EMT_conservation_G1`, `_G2` | nabla^mu T_mu_nu = 0 for exact solutions of the field equations at the point, and not 0 off shell |
| `EMT_trace_G1`, `_G2` | on shell T^mu_mu = -m S + 7 S U'(S) - 8 U(S) = -m S + 3 lambda S^2 |
| `EMT_symmetricHermitian_G1`, `_G2` | T_mu_nu is symmetric and Hermitian |
| `EMT_variation_G3` | in minisuperspace, varying the action with respect to the lapse and the scale factors gives the covariant T_mu_nu; rho = m S + U |
| `EMT_homogeneousReduction_G3` | ten sub-checks of the homogeneous reduction: rho = m S + U, pressure S U' - U on shell, kinetic and potential parts, T_ij, T_4i, the continuity equation, conservation, trace |
| `QNT_canonicalMomentum_G1`, `_G2` | in the Grassmann algebra the canonical momentum is Pi_a = sqrt\|g\| (Psi^dagger C gamma^4)_a and Psi^dagger has no momentum; the matrix i gamma^4 C/(g^44 sqrt\|g\|) of the anticommutator {Psi, Psi^dagger} equals i (sqrt\|g\| C gamma^4)^-1 and is Hermitian; at G2 the matrix B = -i C gamma^4 is Hermitian with B^2 = 1 and trace 0 |
| `NEG_notebookConnectionDetected_G2` | negative control: with Omega replaced by the notebook's contraction, all 11 connection-sensitive checks fail, as they must |

A note on the name "charge matrix": in this set C is a 16x16 matrix, C = gamma^0 gamma^1 gamma^2 gamma^3 (called sigma16 in the original notebook), used to form Psibar = Psi^dagger C. It is not a charge-conjugation operation, and this set makes no statement about charge conjugation.

Besides the 43 checks the report records 295 "measurements": the conventions used, the exact values at every point (for example `G1.p1.lichnerowiczC=-1/4` and `G2.p1.scalarCurvature=-2672/147`) and descriptive texts.

**Documents that cite its results.**

* `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (and its `.tex` and `.pdf`), the Stage-1 document: Section 11.2 lists the 43 checks, Section 11.7 records the sha256 of the report and of both files of this set, Section 12 gives the commands.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/00-how-to-read.md`, `04-curved-space.md`, `05-classical-field-theory.md`, `08-quantization.md`, `19-reproducing-everything.md`, `20-glossary-and-check-index.md`.
* `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md` (and `.tex`, `.pdf`), which cites `GEO_divergenceIdentity_G1` and `_G2` and the report's sha256.
* `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` (its `.tex` does not mention the package) and `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` (and its `.tex` and `.pdf`), which say that the Mathematica notebook `notebooks/Dirac16ComplexDarkSector.nb` loads the package.
* `provenance/dirac matrices.md`, the audit of the Dirac matrices (generated by `provenance/dirac_matrices/build_dirac_matrices_md.py`; committed on 2026-10-07 as work in progress of another workflow), whose row `old_stage_wolfram_packages` states that the matrices gamma, C, chirality, eta and S held by the package equal the matrices of the author's notebook entry by entry.
* The execution-provenance files of the sets that use this set, in the folder `provenance/wolframscript/`: `verify_dirac16complex00.PROVENANCE.md`, `verify_dirac16complex_pairing.PROVENANCE.md` and `verify_dirac16complex_matter_antimatter.PROVENANCE.md` (they record the sha256 of the package and/or of the report), and `build_dirac16complex_mathematica_notebook.PROVENANCE.md`, `build_dirac16complex_ks_mathematica_notebook.PROVENANCE.md`, `verify_dirac16complex_mathematica_notebook.PROVENANCE.md` and `verify_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` (their notebooks load the package). `handoff/tools/WOLFRAMSCRIPT_PROVENANCE.md` (the provenance of the design-phase probes) names this set as the shipped verifier that proves the probes' statements again and lists the checks of the report that do so.

**Programs, tests and data files that depend on this set.** The following list is complete for the verified commits (`45d4734`, `c2b33cc`, `a4c5eda` and `b8a695d`, Part 6): it was made by searching every file of a fresh clone (except the documents `.md`, `.tex`, `.pdf`, `.txt` and the logs) for the names `Dirac16ComplexGeometry`, `wolfram-geometry-report` and `verify_dirac16complex_geometry` and for the three sha256 values of Part 2. (The search was repeated with `git grep` at `a4c5eda` on 2026-10-07: compared with `c2b33cc` it found no new program, test or data file, only the new documents named in the list of documents above. It was repeated again at `b8a695d` on 2026-10-07: compared with `a4c5eda` it found the three files of the Dirac-matrices audit under `provenance/dirac_matrices/` and the document `provenance/dirac matrices.md`, all added to the lists, and new orchestration records.) If you change a program file of this set or the report, these programs and tests are affected.

* Programs that *read* the committed report: `scripts/check_dirac16complex_geometry.py` (option `--wolfram-report`; it records the report's sha256 as `GEO_wolframReportSha256`), `scripts/build_stage1_summary.py`, `scripts/verify_stage1_public_clone_audit.py`, the Stage-1 gates `scripts/verify_stage1_arbitrary_field.ps1` and `scripts/verify_stage1_arbitrary_field.sh` (step `stage1-04-wolfram-geometry`), `wolfram/Dirac16Complex00.wl` (it cites 20 of the report's checks and requires the report's `sourceSha256` of the package to equal the package's current sha256) and `wolfram/Dirac16ComplexMatterAntimatter.wl` (it cites ten of the report's checks and records the report's sha256).
* Programs that compute the *sha256* of the package and/or the report: `scripts/verify_dirac16complex00.wls` (both the package and the report; it writes them into its report), `scripts/verify_dirac16complex_pairing.wls` (the package; it writes it into its report), `scripts/verify_dirac16complex_matter_antimatter.wls` (the package; it writes it into its report) and `scripts/check_dirac16complex_pairing.py` (the package; its check `sourcesCurrent` fails if the package's sha256 differs from the one recorded in the pairing reports).
* Programs that *load* the package: `wolfram/Dirac16Complex00.wl`, `wolfram/Dirac16ComplexPairing.wl`, `wolfram/Dirac16ComplexMatterAntimatter.wl`, `scripts/build_dirac16complex_mathematica_notebook.wls`, `scripts/build_dirac16complex_ks_mathematica_notebook.wls`, the notebooks `notebooks/Dirac16ComplexDarkSector.nb` and `notebooks/Dirac16ComplexKohnSham.nb`, and `provenance/dirac_matrices/extract_repository_wolfram_gammas.wls` (it loads the package and writes the matrices it holds into `provenance/dirac_matrices/repository_wolfram_gammas.json`, which `provenance/dirac_matrices/build_dirac_matrices_md.py` compares with the author's matrices).
* Tests: `tests/test_d16c_arbitrary_field_publication.py` (the report is one of the five Stage-1 reports it checks), `tests/test_d16c_arbitrary_field_public_clone_audit.py` (it tests the audit program with small artificial files that carry the report's file name), `tests/test_d16c_kohn_sham_mathematica.py` (it requires the package's sha256 recorded by the Kohn-Sham notebook report to equal the package's current sha256) and `tests/test_d16c_matter_antimatter_publication.py` (it requires the package's sha256 recorded by the Wolfram matter-antimatter report to appear in the matter-antimatter document and to equal the package's current sha256).
* Committed data files that record the sha256 of the report: `artifacts/dirac16complex/arbitrary-field/python-geometry-report.json` and `stage1-summary.json`, `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json` and `wolfram-matter-antimatter-report.json`, `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json` and `wolfram-dirac16complex00-report.json`. Committed data files that record the sha256 of the package: the report itself, `artifacts/dirac16complex/kohn-sham/mathematica-report.json`, the two matter-antimatter files and the two `dirac16complex00` files just named, and `artifacts/dirac16complex/pair-creation/pairing-theory.json` and `wolfram-pairing-report.json`. Three more committed data files name the package without recording its sha256: `artifacts/dirac16complex/numerics/mathematica-report.json` (in a description of its method), `artifacts/dirac16complex/pair-creation/python-pairing-report.json` (in the list of files compared by its check `sourcesCurrent`) and `provenance/dirac_matrices/repository_wolfram_gammas.json` (it records the matrices eta, gamma, C, chirality and 4 S held by the package).
* The orchestration records `handoff/stage1_build_slim.json`, six workflow scripts under `handoff/workflows/`, `Revision/workflows/execution_provenance.js`, `Revision/workflows/execution_provenance_cont.js`, `Revision/workflows/restart/execution_provenance_restart.js` and the workflow state files under `Revision/workflows/state_2026-10-07/` and `Revision/workflows/state_restart/` also name these files; they record how the project was built and are not run by a student.

This is why the report must be reproduced byte for byte.

## 2. Files

The program files (all stored with LF line endings and pure ASCII; the repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values below are the same on Windows, macOS and Linux):

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `scripts/verify_dirac16complex_geometry.wls` | the script you run: loads the package, runs every check, writes the JSON report, prints the verdict, sets the exit code | 94 | 4817 | `81b1b0febf1a5d6956f042179dff4eed949718cc15955e0753c71606f3f09953` |
| `wolfram/Dirac16ComplexGeometry.wl` | the package (context ``Dirac16Complex`Geometry` ``): gamma matrices, exact jets, Grassmann algebra, test geometries, the function `D16GeoReport[]` that computes all checks | 997 | 71636 | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` |

**Inputs.** The script reads only the two files above: it loads the package with `Get` and computes the sha256 of both files with `FileHash` (they are written into the report as `sourceSha256`). It reads no data file, no other package and nothing from the network. The script finds the package relative to its own location (`<repository root>/wolfram/Dirac16ComplexGeometry.wl`), so the package is found from any current directory. The only optional input is the environment variable `DIRAC16_GEOMETRY_REPORT`, which sets the report path when no path is given on the command line.

**Output.** One file, the JSON report, written at the path given as the first argument (relative paths are relative to the current directory; without an argument and without the environment variable it is the committed path below):

| File | Lines | Bytes | sha256 (committed) |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json` | 350 | 42018 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` |

The report is pure ASCII with LF line endings, indented with tabs, and ends with a newline. Its top-level keys are `schemaVersion` (1), `producer` (names the script, the package and the Wolfram Language version, here `15.0.1`), `checks` (43 entries, all `true`), `measurements` (295 entries) and `sourceSha256` (the sha256 of the two program files). The script also prints 341 lines on standard output (Part 4).

## 3. How to run it

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs: the Wolfram Language *kernel* (the computing engine) and *WolframScript* (the command `wolframscript`, which runs a script file with the kernel). The verification used the kernel version 15.0.1 and WolframScript 1.14.0.

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page; create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded `.exe` file and accept the defaults. The installer normally also installs WolframScript and adds it to the PATH. Close every PowerShell window and open a new one afterwards.
   * macOS: open the downloaded `.dmg` file and follow its instructions (drag the application into Applications and open it once).
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/ (Windows `.msi`, macOS `.pkg`, Linux `.deb` with `sudo apt install ./<file>.deb` or `.rpm` with `sudo dnf install ./<file>.rpm`), and open a new terminal.
3. Activate it. In a terminal (PowerShell on Windows, the Terminal application on macOS, a terminal window on Linux) type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. (Running `wolframscript` without options on a not yet activated engine normally asks the same questions. If it shows the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.)

**Option 2: Wolfram (formerly Mathematica), the desktop product.** If you have a licensed Wolfram or Mathematica installation, it contains the kernel; on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/ as in step 2 above.

**Test the installation.** In a new terminal type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux (they stop the shell from replacing `$Version`); in PowerShell they are also correct. If several versions are installed, `wolframscript` uses the newest one; `wolframscript -configure` prints its settings file, whose line `WOLFRAMSCRIPT_KERNELPATH=...` names the kernel (a leading `//` means that this is the automatic choice). To use a particular installed kernel, add `-local "<path of that kernel>"` before `-file`, for example `wolframscript -local "C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -file ...` on the verification machine.

**Which version.** The report records the Wolfram Language version in its `producer` line. Only version 15.0.1 reproduces the committed report byte for byte. With another version the `producer` line differs, and other lines may differ if that version prints numbers differently; then compare the check verdicts and the measurement values instead of the bytes (Part 4.4). Versions other than 15.0.1 were not tested.

### 3.2 Get the repository

Install git if you do not have it (Windows: https://git-scm.com/download/win; macOS: type `xcode-select --install` in Terminal; Debian/Ubuntu Linux: `sudo apt install git`). Then, in the folder where you want the repository:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone downloads about 200 MB and occupies about 670 MB on disk (measured on 2026-10-07: the git data in `.git` were 195 MB, the whole folder 667 MB; the repository grows with every commit). Every command below is typed in this folder, the *repository root* (the folder that contains `scripts`, `wolfram` and `artifacts`). (Instead of git you may also download the ZIP archive from the GitHub page, button "Code", "Download ZIP", and unpack it; then `git status` and `git checkout` below are not available.)

### 3.3 Run it

The usage line in the script's header is

```
wolframscript -file scripts/verify_dirac16complex_geometry.wls artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
```

It is the same single line in Windows PowerShell, in the macOS Terminal (zsh) and in a Linux terminal (bash). It **overwrites the committed report** with the newly computed one. With Wolfram 15.0.1 the new file is byte-identical to the committed one, so nothing changes (Part 5 says how to restore the file if it does change).

**Recommended for students: write the report to a scratch folder instead**, so that the committed file is never touched, and then compare the two files. The folder `build/` is ignored by git (rule `/build/` in `.gitignore`), and the script creates missing folders itself.

Windows PowerShell:

```
New-Item -ItemType Directory -Force build/geometry-check | Out-Null
wolframscript -file scripts/verify_dirac16complex_geometry.wls build/geometry-check/wolfram-geometry-report.json > build/geometry-check/stdout.txt
"exit code: $LASTEXITCODE"
Get-Content build/geometry-check/stdout.txt -Tail 3
```

macOS (Terminal, zsh) and Linux (bash):

```
mkdir -p build/geometry-check
wolframscript -file scripts/verify_dirac16complex_geometry.wls build/geometry-check/wolfram-geometry-report.json > build/geometry-check/stdout.txt
echo "exit code: $?"
tail -n 3 build/geometry-check/stdout.txt
```

(The first line creates the folder for the saved screen output `stdout.txt`; without `> build/geometry-check/stdout.txt` the 341 lines are printed on the screen instead. The PowerShell commands of this file were tested with PowerShell 7 and with Windows PowerShell 5.1, which comes with Windows. In Windows PowerShell 5.1 the `>` saves `stdout.txt` as UTF-16 text, two bytes per character with a byte-order mark at the start, instead of the bytes that WolframScript prints; every command of this file still reads it correctly.) The run prints nothing until the very end, because all lines are printed after the computation. How long it takes depends on the speed of the computer and on how busy it is: on the verification machine it took between 5 and 10.5 minutes (measured 301 to 634 s, Part 4.3); the shorter runs were made while fewer other programs were running, the longest (about 10.5 minutes) while two other runs of this set and 8 to 14 Wolfram kernels of other jobs were running at the same time. Do not interrupt it.

Then compare the new report with the committed one. Windows PowerShell:

```
$new = (Get-FileHash -Algorithm SHA256 build/geometry-check/wolfram-geometry-report.json).Hash.ToLower()
$old = (Get-FileHash -Algorithm SHA256 artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json).Hash.ToLower()
$new; $old
if ($new -and $new -eq $old) { "identical" } else { "DIFFERENT" }
```

(The `$new -and` makes sure that `identical` is printed only when a sha256 was actually computed: if neither file can be read, for example because the commands are typed outside the repository root, both values are empty and the line prints `DIFFERENT`.)

macOS:

```
shasum -a 256 build/geometry-check/wolfram-geometry-report.json artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
cmp build/geometry-check/wolfram-geometry-report.json artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json && echo identical
```

Linux: the same two lines with `sha256sum` instead of `shasum -a 256`.

Both sha256 values must be `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac`, and the last command must print `identical`.

**Important: never put `--` before the report path.** With `-file`, WolframScript 1.14 silently drops `--` and every argument after it. The script then sees no path and writes the report to the committed path. (Verified on 2026-10-02 with WolframScript 1.14.0 and Wolfram 15.0.1, in PowerShell 7 and in bash: a test script that prints its command line, started as `wolframscript -file s.wls -- out.json`, sees only `{s.wls}`; started as `wolframscript -file s.wls out.json` or as `wolframscript -file s.wls -args out.json` it sees `{s.wls, out.json}`.)

### 3.4 If it fails

| What you see | Cause and fix |
| --- | --- |
| PowerShell: `The term 'wolframscript' is not recognized`; macOS/Linux: `command not found: wolframscript` | WolframScript is not installed or not on the PATH. Open a new terminal after the installation. On Windows the program is in `C:\Program Files\Wolfram Research\WolframScript\`; add that folder to the PATH or install again. On macOS and Linux install WolframScript separately (Part 3.1, step 2). |
| A message containing "licence"/"license", "password", "activate", "kernel limit", "too many kernels", "maximum number of" or "could not launch/start/connect" | The kernel is not activated, or your licence allows fewer kernels at the same time than are running. Run `wolframscript -activate` again; close other Wolfram programs and notebooks; wait 30 seconds and run again. (The project's Stage-1 gate runs this step up to three times in total, waiting 30 seconds before each retry, when the step's log contains one of these messages; the gate's list is the same except that it does not contain "activate".) The first activation needs an internet connection. |
| `ERROR: missing package ...` and exit code 2 | The file `wolfram/Dirac16ComplexGeometry.wl` is missing next to the `scripts` folder: the repository is incomplete. Clone it again. |
| `ERROR: package load produced messages: ...` and exit code 2 | The package produced a warning while loading: it was changed, damaged, or your Wolfram version cannot read it. Compare the sha256 values of both program files with Part 2 (`Get-FileHash -Algorithm SHA256 <file>` in PowerShell, `shasum -a 256 <file>` on macOS, `sha256sum <file>` on Linux); if they differ, run `git checkout -- scripts/verify_dirac16complex_geometry.wls wolfram/Dirac16ComplexGeometry.wl` or clone again. |
| `ERROR: D16GeoReport failed or produced messages` or `ERROR: JSON export failed`, exit code 2 | A warning occurred during the computation (for example the computer ran out of memory, or an untested Wolfram version behaves differently). The run needs about 0.65 to 0.67 GB of memory (Part 4.3); close other programs and run again. Nothing was written (the report is written only after the computation). |
| A line `failed_checks=...`, `failed_check_count` larger than 0, exit code 1 | A check is false: the computed mathematics differs from the committed result. Do not edit anything to make it pass. Check the sha256 values of the program files (above); if they are the committed ones, report the failing check names and your Wolfram version. |
| The report appears in `artifacts/...` although you gave another path | You typed `--` before the path (Part 3.3). Remove it, and restore the committed file with `git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`. |
| The new report differs from the committed one, but all 43 checks are true | Most likely another Wolfram version: compare the `producer` lines (Part 4.4). If you edited a program file, its `sourceSha256` entry changes too. |
| PowerShell says the path to `stdout.txt` could not be found | The folder `build/geometry-check` does not exist yet: run the `New-Item` line first. |
| The PowerShell comparison prints `You cannot call a method on a null-valued expression` and then `DIFFERENT` | A file could not be read: you are not in the repository root (`cd` into the folder `Dirac_claude`), or the run did not write the report (look at its exit code and its last lines). |
| It runs much longer than 10 minutes | A slower computer, or a busy one, needs longer: other Wolfram kernels or other programs running at the same time slow it down (on the verification machine the same run took 5 minutes with fewer other programs running and up to 10.5 minutes while two other runs of this set and 8 to 14 Wolfram kernels of other jobs were running, Part 4.3). The computation is exact and uses essentially one processor core, so more cores do not help. Close other programs if you can, and let it finish. If you stop it with Ctrl+C, no report is written and the old one is left unchanged; WolframScript then leaves two empty temporary files behind (Part 5). |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly 341 lines on the standard output and nothing on the error stream. On Windows the printed lines end with CR LF, also when the output is redirected into a file from PowerShell 7 or Git Bash; such a file is pure ASCII. Windows PowerShell 5.1 saves a redirected file differently: as UTF-16 text with a byte-order mark (the bytes `ff fe` at the start, two bytes per character, so CR LF is stored as the four bytes `0d 00 0a 00`); the 341 lines are the same, and every command of this file reads such a file correctly, but its bytes and its sha256 differ from those of the PowerShell 7 or Git Bash file. On macOS and Linux the lines normally end with LF only (not tested here). The 341 lines are:

* 43 lines `check_<name>=true`, one per check, sorted by name in the Wolfram Language's order, from `check_ALG_chargeMatrix=true` to `check_QNT_canonicalMomentum_G2=true`;
* 295 lines `measurement_<name>=<value>`, starting with `measurement_convention.grassmann=...` and ending with `measurement_emt.trace=on-shell T^mu_mu = -m S + 7 S U'(S) - 8 U(S) = -m S + 3 lambda S^2`;
* the three final verdict lines. With the usage line of Part 3.3 they are

```
check_count=43
failed_check_count=0
report=artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
```

and with the recommended scratch path the last line is `report=build/geometry-check/wolfram-geometry-report.json`. (A report path outside the repository is printed in full.)

The exit code is **0**. It is 1 if a check is false or the number of checks is not 43 (then a fourth line `failed_checks=<names>` follows), and 2 if the package cannot be loaded, the computation produces a warning, or the JSON cannot be produced.

Some measurement lines worth looking at: `measurement_G1.p1.lichnerowiczC=-1/4` (the same at all six points of G1 and G2), `measurement_G1.p1.metricInertia={4, 4, 0}`, `measurement_G2.p1.scalarCurvature=-2672/147`, `measurement_G1.p1.notebookLgResidualXRank=16`, `measurement_G1.p1.spinInvariance.spacelikeTimelikePair.LprimeOverL=-1`, `measurement_G3.p1.homogeneous.subchecks={True, True, True, True, True, True, True, True, True, True}`.

### 4.2 The report file

The report written at the given path must be byte-identical to the committed `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`: 42018 bytes, 350 lines, sha256 `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` (how to compare: Part 3.3). The printed check and measurement lines are the same entries as the report's `checks` and `measurements`, in the same order.

To print a one-line summary of the report's checks (replace the path by the report you want to inspect):

Windows PowerShell:

```
$r = Get-Content -Raw build/geometry-check/wolfram-geometry-report.json | ConvertFrom-Json
$c = $r.checks.PSObject.Properties
"checks=" + @($c).Count + " true=" + @($c | Where-Object { $_.Value -eq $true }).Count
```

macOS and Linux:

```
wolframscript -code 'c = Import["build/geometry-check/wolfram-geometry-report.json", "RawJSON"]["checks"]; "checks=" <> ToString[Length[c]] <> " true=" <> ToString[Count[Values[c], True]]'
```

Both must print `checks=43 true=43`.

### 4.3 Run time and memory

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GB RAM, Windows 11 Pro for Workstations 10.0.26200 for runs 1 to 7 and 10.0.26300 for runs 8 to 19, Wolfram 15.0.1, WolframScript 1.14.0), always with other Wolfram kernels of other jobs running at the same time (the machine was never idle). Runs 12 to 15 were made by the independent review of this file on 2026-10-07 (fresh clones at commit `af2c688`), runs 16 to 19 by the re-verification after that review (Part 6):

| Run | Report path | Wall time | Exit code | Peak working set of the kernel |
| --- | --- | --- | --- | --- |
| 1 | usage line (committed path) | 303.7 s | 0 | 635.6 MiB |
| 2 | usage line (committed path) | 366.4 s | 0 | 638.1 MiB |
| 3 | `build/geometry-check/...` | 364.4 s | 0 | 625.2 MiB (sampled after 236 s) |
| 4 | `build/geometry-check/...`, PowerShell block of Part 3.3 | 314.9 s | 0 | not measured |
| 5 | `build/geometry-check/...`, bash block of Part 3.3 | 314 s | 0 | not measured |
| 6 | `build/geometry-check/...`, PowerShell block of Part 3.3 (re-verification) | 301.4 s | 0 | not measured |
| 7 | `build/geometry-check/...`, bash block of Part 3.3 (re-verification) | 404.1 s | 0 | not measured |
| 8 | usage line (committed path), 2026-10-07 | 432.7 s | 0 | 625 MiB |
| 9 | usage line (committed path), 2026-10-07 | 411.7 s | 0 | 629 MiB |
| 10 | `build/geometry-check/...`, PowerShell block of Part 3.3, 2026-10-07 | about 424 s | 0 | not measured |
| 11 | `build/geometry-check/...`, bash block of Part 3.3, 2026-10-07 | about 429 s | 0 | not measured |
| 12 | `build/geometry-check/...`, PowerShell block of Part 3.3, review | 615.2 s | 0 | not measured |
| 13 | `build/geometry-check/...`, bash block of Part 3.3, review | 617.2 s | 0 | not measured |
| 14 | usage line (committed path), review | 633.5 s | 0 | not measured |
| 15 | usage line (committed path), review | 474.2 s | 0 | 617.8 MiB |
| 16 | usage line (committed path), re-verification after the review | 547.8 s | 0 | 637.6 MiB |
| 17 | `build/geometry-check/...`, PowerShell block of Part 3.3 in Windows PowerShell 5.1, re-verification after the review | 457.2 s | 0 | 623.3 MiB |
| 18 | `build/geometry-check/...`, bash block of Part 3.3, re-verification after the review | 459.5 s | 0 | 618.7 MiB |
| 19 | `build/geometry-check/...`, PowerShell block of Part 3.3 in Windows PowerShell 5.1 (module path of a new window), re-verification after the review | 454.6 s | 0 | 628.4 MiB |

Runs 2 and 3 overlapped in time, and so did runs 4 and 5, which made them slower than run 1; runs 6 and 7 did not overlap with each other, but other Wolfram jobs ran on the machine at the same time (a process list taken 39 s after the end of run 7 showed eleven other Wolfram kernels: one started before run 6, seven started during run 7); this is the most likely reason for the 404 s of run 7. Runs 8 to 11 ran while about a dozen kernels of other jobs were running (a process list taken about 80 s after the start of run 8 showed thirteen other Wolfram kernels), and runs 9, 10 and 11 overlapped with each other (runs 10 and 11 started about 50 s after run 9). Runs 12, 13 and 14 were started together while 8 to 14 kernels of other jobs were running, and run 15 ran on its own while about 11 kernels of other jobs were running (process lists of the review). Run 16 ran while 10 to 23 other Wolfram kernels were running (18.7 on average; the kernels were counted about every 2 s; the count includes the kernels of three short, deliberately interrupted runs of this set, Part 6, which overlapped with run 16); runs 17 and 18 were started together while 8 to 19 other kernels were running (14.2 on average, including the kernel of the other run), and run 19 ran on its own while 5 to 9 kernels of other jobs were running (6.7 on average). The run time therefore depends strongly on how busy the machine is: on this machine it ranged from 301 s to 634 s (5 to 10.5 minutes). Expect at least 5 minutes on a similar machine, and up to about 11 minutes or more when other Wolfram kernels or other programs are running at the same time; a slower computer needs longer. (Chapter 19.6 of the textbook, `provenance/textbook/chapters/19-reproducing-everything.md`, gives 409 s for the same step in a Bash run of the Stage-1 gate from a fresh clone made for that edition of the textbook; the committed Stage-1 gate logs of 2026-09-30 under `handoff/reviews/` record no time for this step.) The computation runs in one kernel and uses essentially one core (the kernel's processor time was about 1.04 times the wall time in run 1; in runs 8 and 9 it was at least 0.94 and 0.99 times the wall time, measured by a sample taken at most about 6 s before the end), so the time depends mainly on the speed of one core. On a busy machine the kernel gets less than one full core and its own processor time also grows: in run 15 it was 419.0 s of 474.2 s, in run 16 411.6 s of 547.8 s, in run 17 418.8 s of 457.2 s and in run 19 415.1 s of 454.6 s (samples taken at most about 5 s before the end), against about 316 s in run 1. The peak memory (working set) of the kernel process was about 0.65 to 0.67 GB (617.8 to 638.1 MiB, that is 648 to 669 million bytes; 1 MiB = 1,048,576 bytes); WolframScript itself used about 17 MB.

### 4.4 Comparing with a different Wolfram version

If you do not have version 15.0.1, the bytes of the report differ at least in the `producer` line. Then check instead that (a) the exit code is 0, (b) the summary of Part 4.2 prints `checks=43 true=43`, and (c) the measurement values agree with the committed report.

To list the differing lines, use git. The command is the same single line in Windows PowerShell, in the macOS Terminal and in a Linux terminal:

```
git --no-pager diff --no-index artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json build/geometry-check/wolfram-geometry-report.json
```

When the two files are identical it prints nothing and its exit code is 0 (`$LASTEXITCODE` in PowerShell, `echo $?` on macOS and Linux). Otherwise it prints every differing line, with the lines of the committed report marked `-` and the lines of your report marked `+`, and its exit code is 1. It sees every difference: of letter case (`true` against `True`), of order (lines that have only moved), of line endings (LF against CR LF) and a missing final newline. (`--no-pager` makes git print everything at once instead of opening a page viewer; `--no-index` lets git compare any two files, also one in the ignored folder `build/`.)

Without git (for example after downloading the ZIP archive), use on macOS and Linux

```
diff artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json build/geometry-check/wolfram-geometry-report.json
```

which also sees every difference and prints nothing (exit code 0) for identical files, and in Windows PowerShell

```
Compare-Object -CaseSensitive -SyncWindow 0 (Get-Content artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json) (Get-Content build/geometry-check/wolfram-geometry-report.json)
```

Both options are necessary: without `-CaseSensitive` PowerShell ignores differences of letter case, and without `-SyncWindow 0` it ignores lines that have only moved, so that "no output" would not mean "equal". With `-SyncWindow 0` it compares line 1 with line 1, line 2 with line 2, and so on, and marks the lines of the committed report with `<=` and yours with `=>`; one inserted or missing line therefore makes it list every later line of both files (measured: a copy of the report with its line 11 removed gave 679 output lines, 340 with `<=` and 339 with `=>`). Even with both options, `Get-Content` removes the line endings, so this command does not see differences of line endings (LF against CR LF) or a missing final newline; the sha256 comparison of Part 3.3 sees every byte.

With 15.0.1 there are no differing lines: all three commands print nothing.

## 5. Side effects

**Files in the repository.** The script writes exactly one file, the report at the path you give.

* With the usage line of Part 3.3 it **overwrites the committed file** `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`. With Wolfram 15.0.1 the new bytes are identical, so `git status --porcelain --untracked-files=all` prints nothing afterwards (measured after verification runs 1, 2, 8, 9 and 16).
* With the recommended scratch path it creates the folder `build/geometry-check/` (and `build/` if missing) and the report in it; `build/` is ignored by git, so `git status` stays empty. The saved screen output `build/geometry-check/stdout.txt` is created by your terminal, not by the script.
* No other file in the repository is created, changed or deleted. The script does not write a log file and leaves no partial file: the report is written in one piece after the computation has finished.

**Temporary files.** None in the system temporary folder: verification runs 1 and 8 pointed `TEMP` and `TMP` at an empty private folder, which was still empty afterwards. On Windows WolframScript itself creates two files named `tmp_<10 random characters>` in the folder `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (on the verification machine `C:\Users\<your name>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`): one when WolframScript starts, and a second one a few seconds later that the kernel keeps open while it runs, for its printed output. Both stay empty (0 bytes) during this run, because the script prints only at the end. When the run ends normally, both files are deleted (measured in runs 2, 8 and 16). **An interrupted run leaves both files behind**: measured on 2026-10-07 with a run stopped by Ctrl+C after about 33 s and with a run whose WolframScript process was terminated (as when you close the window) after about 40 s; in both cases WolframScript and the kernel ended, no report was written, and the two `tmp_` files were still there afterwards. They are harmless; you may delete them when no Wolfram program is running, in PowerShell with `Remove-Item "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary\tmp_*"` (do not delete them while another WolframScript run is in progress, because the files of that run are in the same folder). WolframScript also rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (238 bytes on the verification machine; only the modification time changed) at every start. On macOS and Linux WolframScript keeps the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process (`wolfram.exe` on the verification machine, started with, among other options, `-linkmode Connect -linkname <name>_shm`, so it talks to WolframScript through shared memory), which runs for the whole computation and exits at the end. No further kernels are started (the package contains no parallel computation).

**Network.** None. The script and the package contain no network calls (no `URL...`, no web `Import`, no external programs). At a snapshot taken during runs 2 and 3 the kernels and WolframScript had no TCP connections and no UDP endpoints; during runs 8 and 9 the same was found in every snapshot (14 in run 8, 13 in run 9, taken about every 32 s). (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of this script.)

**Restoring the committed state.** If the committed report was overwritten with different bytes (for example by another Wolfram version), restore it with

```
git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
```

and remove the scratch folder with `Remove-Item -Recurse -Force build/geometry-check` (PowerShell) or `rm -rf build/geometry-check` (macOS, Linux). Afterwards `git status --porcelain` must print nothing.

## 6. Verification record

* Date: 2026-10-02.
* Commit verified: `45d47343ae480df46e06689ed822b8f9a88a8030` of https://github.com/once-ere/Dirac_claude.git (branch `main`). The two program files and the committed report have not changed since commit `6c0bfad164a41941ab8df332f7e748f97790849f` (2026-09-25).
* Environment: Windows 11 Pro for Workstations 10.0.26200 (build 26200), Intel Core Ultra 9 275HX (24 cores), 191 GB RAM; Wolfram 15.0.1 for Microsoft Windows (64-bit) (kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`), WolframScript 1.14.0; PowerShell 7.6.6 and Git Bash (git 2.51.2). Professional Wolfram licence; other Wolfram jobs ran on the machine at the same time.
* Fresh clones: two separate `git clone https://github.com/once-ere/Dirac_claude.git` into empty scratch folders (`run1`, `run2`). No file was copied into them: the author's working tree had no uncommitted change to the set's files (the script, the package and the committed report; `git status --porcelain -- scripts/verify_dirac16complex_geometry.wls wolfram/Dirac16ComplexGeometry.wl artifacts/dirac16complex/arbitrary-field/` printed nothing), and the set needs no file outside the repository. (The working tree did have uncommitted changes to other files, among them `wolfram/Dirac16Complex00.wl`, which loads the package, and the two `pair-creation` JSON files that record the report's sha256; none of them is read by this set.) The clone of run 2 was made after a later, unrelated commit (`c2b33cc`, a change of `Revision/tests/test_pair_creation_proofs_publication.py` only) had been pushed; it was checked out at `45d4734` so that both runs used the same commit. In both clones the two program files and the committed report had the sha256 values of Part 2.
* Command (both runs, from the clone root, exactly the usage line of the script header): `wolframscript -file scripts/verify_dirac16complex_geometry.wls artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`. Run 1 with `TEMP` and `TMP` pointing at an empty private folder, run 2 with the normal environment. An additional run 3 in the clone of run 1 used the scratch path of Part 3.3 (`build/geometry-check/wolfram-geometry-report.json`, folder not existing before) to test the student instructions.

| Run | Clone | Started (local time, UTC-7) | Wall time | Exit code | Printed lines (stderr) | Report sha256 | Report vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `run1` | 06:00:36 | 303.7 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 2 | `run2` | 06:05:53 | 366.4 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 3 | `run1`, scratch path | 06:07:10 | 364.4 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 4 | `run1`, PowerShell block of Part 3.3 | 06:13 | 314.9 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 5 | `run2`, bash block of Part 3.3 (Git Bash) | 06:13 | 314 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |

Runs 1 and 2 are the two required runs from fresh clones with the exact usage line. Run 3 tested the scratch path in a folder that did not exist before (the script created it). Runs 4 and 5 executed the student command blocks of Part 3.3 exactly as printed (PowerShell 7 with `pwsh -NoProfile -File`, and `bash`), each after deleting `build/`; both printed `exit code: 0` and the three verdict lines with `report=build/geometry-check/wolfram-geometry-report.json`. The comparison commands of Part 3.3, the summaries of Part 4.2 (both printed `checks=43 true=43`), the line comparisons of Part 4.4 as first written (`Compare-Object` without options in PowerShell, which the review showed to be unreliable, and `diff` in bash; no differing lines) and the restore and clean-up commands of Part 5 (afterwards `git status --porcelain --ignored` printed nothing) were then executed as printed, PowerShell in `run1` and bash in `run2`.

* Byte identity: the only output file, the report, was rewritten by every run (its modification time is the end time of the run) and is byte-identical (`cmp`) to the committed file (taken with `git show HEAD:artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`) and between the runs: run 1 = run 2 = run 3 = run 4 = run 5 = committed, sha256 `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac`, 42018 bytes.
* Check counts: 43 checks, 43 true, `failed_check_count=0` in every run (by prefix: 19 `GEO`, 10 `LAG`, 8 `EMT`, 3 `ALG`, 2 `QNT`, 1 `NEG`); 295 measurements (247 texts, 48 integers). Every printed `check_` and `measurement_` line equals the corresponding entry of the report, in the same order.
* Printed output: the standard output of runs 1 and 2 is byte-identical (341 lines, CRLF, sha256 `4571a38dd0bab3403d8e6cd3b0c5bd463b57dee324b845d8535426d599d3b878`); run 3 differs only in its last line (`report=build/geometry-check/wolfram-geometry-report.json`). Apart from that last line, the output is identical to the output of the step `stage1-04-wolfram-geometry` recorded in the Stage-1 gate log `handoff/reviews/stage1_gate_2026-09-30_public_ps1.log`. The error stream was empty in every run.
* `git status --porcelain --untracked-files=all` in both clones after the runs: empty. After run 3, `git status --porcelain --ignored` shows only `!! build/`. A search for files modified during the runs (outside `.git`) found only the report itself.
* Temporary files: run 1 ran with `TEMP` and `TMP` set to an empty private folder, which stayed empty; in run 2 no new entry appeared in the normal `%TEMP%` folder, and the WolframScript spool files created at the start of the run (`%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\tmp_...`) no longer existed after the run had ended. `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` keeps its content (same sha256) and only gets a new modification time at each start of `wolframscript`.
* Processes and network: one `wolframscript.exe` with one child `wolfram.exe` per run (`-linkmode Connect -linkname <name>_shm`); a snapshot during runs 2 and 3 showed no TCP connection and no UDP endpoint of either process.
* Fixes made to the set: none. No execution defect was found; no file of the set was changed.
* Open discrepancies: none.

**Re-verification after a review of this file (2026-10-02).** An independent review found seven statements of this file that were inaccurate; none concerned the set itself. Each was re-checked in two new fresh clones (`git clone https://github.com/once-ere/Dirac_claude.git`, folders `clone1` and `clone2`, at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`; no file copied in; the three files of Part 2 had the sha256 values of Part 2) and corrected in this file:

1. Part 4.4: `Compare-Object` without options ignores letter case and line order (measured with PowerShell 7.6.6: a copy of the report with `"EMT_trace_G1":true` changed to `True` and two lines swapped gave 0 differences). Replaced by `git --no-pager diff --no-index` (same command in PowerShell, macOS and Linux), `diff`, and `Compare-Object -CaseSensitive -SyncWindow 0`; on that altered copy all three listed the changed and the moved lines, and `git diff --no-index` and `diff` also detected a CR LF copy and a copy without its final newline, which `Compare-Object` does not (stated in Part 4.4).
2. Part 3.3: the false explanation that WolframScript treats `--` as its option `-args` was removed; the measured behaviour (`--` and everything after it dropped with `-file`; `-args` and a plain argument passed through) is stated.
3. Part 6: the fresh-clone bullet now says that the working tree had no uncommitted change to the set's files (and names the uncommitted changes to other files).
4. Part 4.3: the 409 s is now attributed to its real source, Chapter 19.6 of the textbook; the committed gate logs record no time for this step.
5. Part 3.4: the Stage-1 gate makes at most three attempts in total (at most two retries), and its message list does not contain "activate".
6. Part 1: the statement about floating-point numbers now names the three places where 30-digit or 20-digit numerical values are used.
7. Part 1: the list of dependent programs, tests and data files was completed by a search of the whole clone.

| Run | Clone | Started (local time, UTC-7) | Wall time | Exit code | Printed lines | Report sha256 | Report vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | `clone1`, PowerShell block of Part 3.3 (`pwsh -NoProfile -File`) | 06:54:00 | 301.4 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 7 | `clone2`, bash block of Part 3.3 (Git Bash) | 06:59:55 | 404.1 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |

Both printed `exit code: 0` and the three verdict lines `check_count=43`, `failed_check_count=0`, `report=build/geometry-check/wolfram-geometry-report.json`. The printed output of run 6 (`stdout.txt`, 341 lines, CR LF) is byte-identical to that of run 3 and to that of run 7 (sha256 `50e67d16dc25cf23b38afccad7f06590b90fb88c612057c25af4734194a8e55f` for all three), and its first 340 lines equal the output of the step `stage1-04-wolfram-geometry` in `handoff/reviews/stage1_gate_2026-09-30_public_ps1.log`. Afterwards the comparison commands of Part 3.3 (`identical`), the summaries of Part 4.2 (`checks=43 true=43`) and the corrected line comparisons of Part 4.4 were executed as printed, PowerShell in `clone1` (`git --no-pager diff --no-index` and `Compare-Object -CaseSensitive -SyncWindow 0`) and bash in `clone2` (`git --no-pager diff --no-index` and `diff`); all four printed nothing, and the exit codes of `git diff --no-index` and `diff` were 0. Then the restore and clean-up commands of Part 5 were executed (afterwards `git status --porcelain` and `git status --porcelain --ignored` printed nothing in either clone).

**Re-verification after the session-limit restart (2026-10-07).** The workflow that wrote this file was interrupted by a session limit and restarted in a new session, so this file and the set were checked again instead of being trusted. Every statement of Parts 1 to 5 was re-checked against the program files and the committed report (the check names and counts, the 295 measurements, the line and byte counts, the `.gitattributes` and `.gitignore` rules, the Stage-1 gate's retry rule, the 409 s of Chapter 19.6), and the set was run four more times:

* Commits: `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (clones `clone1` and `clone2`, runs 8 and 9) and `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` (clones `clone3` and `clone4`, made a few minutes later, runs 10 and 11; this commit only adds a workflow script under `Revision/workflows/` and a note in `HANDOFF.md`). Each clone was a new `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder; no file was copied into it, because the author's working tree had no uncommitted change at all when the clones were made (`git status --porcelain` printed nothing). In all four clones the three files of Part 2 had the sha256 values of Part 2; they have not changed since commit `6c0bfad`.
* Environment: as above, except Windows 11 Pro for Workstations 10.0.26300 (build 26300). Wolfram 15.0.1, WolframScript 1.14.0, PowerShell 7.6.6, Git Bash with git 2.51.2. About a dozen kernels of other jobs ran at the same time (Part 4.3).
* Commands: runs 8 and 9 exactly the usage line of the script header, from the clone root (run 8 with `TEMP` and `TMP` pointing at an empty private folder, run 9 with the normal environment); runs 10 and 11 the student command blocks of Part 3.3 exactly as printed, PowerShell 7 with `pwsh -NoProfile -File` in `clone3` and Git Bash in `clone4`, each followed by the comparison commands of Part 3.3, the summaries of Part 4.2 and the line comparisons of Part 4.4, as printed (in Git Bash the Linux line with `sha256sum`).

| Run | Clone | Started (local time, UTC-7) | Wall time | Exit code | Printed lines (stderr) | Report sha256 | Report vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | `clone1`, usage line | 15:19:07 | 432.7 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 9 | `clone2`, usage line | 15:26:20 | 411.7 s | 0 | 341 (0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 10 | `clone3`, PowerShell block of Part 3.3 | 15:27:11 | about 424 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 11 | `clone4`, bash block of Part 3.3 | 15:27:13 | about 429 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |

* Byte identity: in runs 8 and 9 the report was rewritten (its modification time is the end of the run) and is byte-identical (`cmp`) to the committed file (taken with `git show HEAD:artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`) and to the report of the other run; the reports written to `build/geometry-check/` in runs 10 and 11 are identical to it as well: run 8 = run 9 = run 10 = run 11 = committed, sha256 `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac`, 42018 bytes.
* Printed output: the standard output of runs 8 and 9 is byte-identical to each other and to that of runs 1 and 2 (341 lines, CR LF, sha256 `4571a38dd0bab3403d8e6cd3b0c5bd463b57dee324b845d8535426d599d3b878`); its first 340 lines equal the output of the step `stage1-04-wolfram-geometry` in `handoff/reviews/stage1_gate_2026-09-30_public_ps1.log`, and its 338 `check_` and `measurement_` lines equal the entries of the committed report, in the same order. The `stdout.txt` of runs 10 and 11 is byte-identical to that of runs 3, 6 and 7 (sha256 `50e67d16dc25cf23b38afccad7f06590b90fb88c612057c25af4734194a8e55f`). The error stream of runs 8 and 9 was empty.
* Check counts: 43 checks, 43 true, `failed_check_count=0` in every run; 295 measurements.
* Student commands (runs 10 and 11): both blocks printed `exit code: 0` and the three verdict lines `check_count=43`, `failed_check_count=0`, `report=build/geometry-check/wolfram-geometry-report.json`. The comparison of Part 3.3 printed the same sha256 twice and `identical` in both shells; the summaries of Part 4.2 printed `checks=43 true=43` in both shells; `git --no-pager diff --no-index` (both shells), `Compare-Object -CaseSensitive -SyncWindow 0` (PowerShell) and `diff` (bash) printed nothing, and the exit codes of `git diff --no-index` and `diff` were 0. Then the restore and clean-up commands of Part 5 were executed as printed, PowerShell in `clone3` and bash in `clone4`; afterwards `git status --porcelain` and `git status --porcelain --ignored` printed nothing in either clone.
* Side effects: after runs 8 and 9, `git status --porcelain --untracked-files=all --ignored` printed nothing in either clone, and a search for files changed since the start of run 8 (outside `.git`) found only the report itself. Runs 10 and 11 created only `build/geometry-check/` with the report and `stdout.txt` (ignored by git). In run 8 the private `TEMP` folder stayed empty; in run 9 no new entry appeared in the normal `%TEMP%` folder; the WolframScript spool file created at the start of run 8 (`WolframScriptTemporary\tmp_wqoAUV7HfQ`) no longer existed after the run.
* Processes, memory and network: one `wolframscript.exe` with one child `wolfram.exe` per run (command line `-runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`); peak working set of the kernel 625 MiB (run 8) and 629 MiB (run 9); no TCP connection and no UDP endpoint of either process in any of the 14 (run 8) and 13 (run 9) snapshots taken about every 32 s.
* Dependents: the search of Part 1 was repeated at `a4c5eda`; it found no new program, test or data file, only new documents (the sibling execution-provenance files and `handoff/tools/WOLFRAMSCRIPT_PROVENANCE.md`), which were added to the list of documents in Part 1.
* Changes to this file in the re-verification: the summary at the top, the list of documents and the commit list of the dependent-file search in Part 1, the clone size in Part 3.2 (about 200 MB download, about 670 MB on disk, measured on 2026-10-07), the expected run time (5 to 7.5 minutes instead of 5 to 7) in Parts 3.3, 3.4 and 4.3, runs 8 to 11 in Part 4.3, Parts 5 and 6 (new measurements). No statement about the set itself had to be corrected.
* Fixes made to the set: none. No execution defect was found; no file of the set was changed.
* Open discrepancies: none.

**Re-verification after the second review (2026-10-07).** A second independent review of this file (fresh clones at commit `af2c6881e379f6fd28f45a5ff07b0d5b98a44c3e`; runs 12 to 15 of Part 4.3, all with exit code 0, 43 of 43 checks true and a report byte-identical to the committed one) made four findings, all about statements of this file and none about the set. Each was re-checked in new fresh clones: `git clone https://github.com/once-ere/Dirac_claude.git` into the empty scratch folders `cloneA`, `cloneB` and `cloneC` at commit `b8a695d1faa7abe43b4b51eb666f25d250420fb7`, and `cloneD` at commit `603f1506a143f731ea1661a040110077c920b785` (made later; that commit changes no file of the set). No file was copied into the clones (the author's working tree had uncommitted changes only in `Revision/textbook/` and in provenance files, none of them read by the set). In every clone the three files of Part 2 had the sha256 values of Part 2. Results:

1. Run time (confirmed and corrected). The review measured 474 to 634 s, more than the "about 5 to 7.5 minutes" stated before, and this file named only a slower computer as a cause of a longer run. Runs 16 to 19 took 455 to 548 s while 5 to 23 other Wolfram kernels were running. Parts 3.3, 3.4 and 4.3 now give the measured range (301 to 634 s) and name the load of the machine (other Wolfram kernels and other programs) as a cause next to a slower computer; the Part 3.4 row now starts at 10 minutes.
2. Memory figures (confirmed and corrected). 625 MiB are 0.655 GB, so "about 0.63 to 0.67 GB (625 to 638 MiB)" did not match, and the review measured 617.8 MiB in run 15. Runs 16 to 19 measured 618.7 to 637.6 MiB. Part 4.3 now says about 0.65 to 0.67 GB (617.8 to 638.1 MiB, 648 to 669 million bytes), and Part 3.4 says about 0.65 to 0.67 GB.
3. Windows PowerShell 5.1 (confirmed and corrected). Runs 17 and 19 executed the PowerShell block of Part 3.3 in Windows PowerShell 5.1.26100.9444. In both, `stdout.txt` was UTF-16 with a byte-order mark: 86410 bytes, starting with `ff fe`, CR LF stored as `0d 00 0a 00`, sha256 `146e5e3155b1b5fa1d5c9fe9a8160a33b660b36780a300f95a52446267132d12`; decoded, it is exactly the 341-line file of PowerShell 7 and Git Bash (sha256 `50e67d16dc25cf23b38afccad7f06590b90fb88c612057c25af4734194a8e55f`), and `Get-Content -Tail 3` printed the three verdict lines correctly. Parts 3.3 and 4.1 now say so. This test also found a weakness of the instructions, fixed in this file. In run 17 the test program started Windows PowerShell 5.1 directly from a PowerShell 7 process (through .NET, not by typing `powershell`), so it inherited the module path of PowerShell 7 and reported `The term 'Get-FileHash' is not recognized`; a student does not meet this, because typing `powershell` in PowerShell 7, or opening Windows PowerShell from the Start menu, gives Windows PowerShell its own module path (measured: `Get-FileHash` was found). But the old comparison line `if ($new -eq $old)` then printed `identical` although no sha256 had been computed, and the same happens when the comparison is typed outside the repository root (measured: in a folder without the two files the old line printed `identical`, the new line `if ($new -and $new -eq $old)` printed `DIFFERENT`). Part 3.3 now uses the new line, and Part 3.4 has a row for the error messages. With the module path of a new Windows PowerShell window, the comparison commands of Part 3.3, the summary of Part 4.2, `git --no-pager diff --no-index` and `Compare-Object -CaseSensitive -SyncWindow 0` all worked in Windows PowerShell 5.1. This was measured first on the files of run 17 and then in run 19, which executed the whole block with the new comparison line. Run 19 printed `exit code: 0`, the three verdict lines, the same sha256 twice, `identical` and `checks=43 true=43`; `git diff --no-index` printed nothing (exit code 0) and so did `Compare-Object`.
4. Documents (confirmed and corrected). `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.tex` (line 865) also says that the notebook loads the package, and the `.pdf` exists; Part 1 now names both. The `.tex` of the student guide does not mention the package (none of its lines contains "geometry"), and Part 1 now says this too. Repeating the search for dependents at `b8a695d` also found the files of the Dirac-matrices audit (`provenance/dirac_matrices/extract_repository_wolfram_gammas.wls`, which loads the package, `repository_wolfram_gammas.json`, `build_dirac_matrices_md.py` and the document `provenance/dirac matrices.md`) and new orchestration records; all were added to Part 1.

| Run | Clone | Started (local time, UTC-7) | Wall time | Exit code | Printed lines | Report sha256 | Report vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | `cloneA`, usage line | 20:38:51 | 547.8 s | 0 | 341 (stderr 0) | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 17 | `cloneB`, PowerShell block of Part 3.3 in Windows PowerShell 5.1 (started through .NET from a PowerShell 7 process) | 20:50:23 | 457.2 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 18 | `cloneC`, bash block of Part 3.3 (Git Bash) | 20:50:24 | 459.5 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |
| 19 | `cloneD`, PowerShell block of Part 3.3 in Windows PowerShell 5.1 (module path of a new window) | 21:00:09 | 454.6 s | 0 | 341 | `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac` | byte-identical |

(The wall times of runs 17 to 19 run from the creation of `build/geometry-check` to the last write of `stdout.txt`.)

* Byte identity: run 16 rewrote the committed report (its modification time is the end of the run) with identical bytes (`cmp` against `git show HEAD:artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`), and the reports of runs 17, 18 and 19 are identical to it: run 16 = run 17 = run 18 = run 19 = committed, sha256 `cec9ee0d577c4e7f0e82efd404d412a503140ccb1547118ab48a78a3d773f0ac`, 42018 bytes.
* Printed output: the standard output of run 16 is byte-identical to that of runs 1, 2, 8 and 9 (341 lines, CR LF, sha256 `4571a38dd0bab3403d8e6cd3b0c5bd463b57dee324b845d8535426d599d3b878`), and its error stream was empty. The `stdout.txt` of run 18 is byte-identical to that of runs 3, 6, 7, 10 and 11 (sha256 `50e67d16dc25cf23b38afccad7f06590b90fb88c612057c25af4734194a8e55f`); the UTF-16 files of runs 17 and 19 are identical to each other and equal to it after decoding (item 3).
* Check counts: 43 checks, 43 true, `failed_check_count=0` in every run; the summaries of Part 4.2 printed `checks=43 true=43` (Windows PowerShell 5.1 in runs 17 and 19, WolframScript in run 18).
* Student commands: in run 18 (Git Bash) the comparison printed the same sha256 twice and `identical`, `git --no-pager diff --no-index` and `diff` printed nothing and exited with 0. Then the restore and clean-up commands of Part 5 were executed as printed: Windows PowerShell 5.1 in `cloneB` and `cloneD`, Git Bash in `cloneC`, and the `git checkout` line in `cloneA`. Afterwards `git status --porcelain` and `git status --porcelain --ignored` printed nothing in any of the four clones.
* Side effects: after run 16, `git status --porcelain --untracked-files=all --ignored` printed nothing. Runs 17 to 19 created only `build/geometry-check/` with the report and `stdout.txt` (ignored by git). WolframScript deleted the two spool files of run 16 (`tmp_Oc2ywmcdgR`, created at the start of `wolframscript.exe`, and `tmp_uCLi0yOVBV`, held open by the kernel) at the normal end of the run.
* Interrupted runs: three runs of the usage line with a scratch report path (`build/interrupt-.../`) in `cloneC` were interrupted deliberately. Two were stopped by Ctrl+C, sent to the console of the run after about 45 s and about 33 s, and one by terminating `wolframscript.exe` (as when the window is closed) after about 40 s. Each time WolframScript and its kernel ended within 20 s, no report was written and `stdout.txt` stayed empty. In the second and third run, the two spool files of the run were identified while it was running: the file created in the same second as `wolframscript.exe`, and the file that the Windows Restart Manager showed as held open by the kernel. Both were still in `WolframScriptTemporary` after the interrupt (0 bytes each); they were deleted by hand afterwards. Part 5 and the Ctrl+C sentence of Part 3.4 now say this. The clean-up command of Part 5, `Remove-Item "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary\tmp_*"`, was tested in PowerShell 7 and in Windows PowerShell 5.1 with `LOCALAPPDATA` pointing at a scratch folder that held two `tmp_` files and one other file: it removed exactly the two `tmp_` files.
* New comparison line in PowerShell 7 (`cloneA`, with a copy of the committed report at the scratch path): it printed the same sha256 twice and `identical`; for a copy with `"EMT_trace_G1":true` changed to `True` it printed two different sha256 values and `DIFFERENT`. Afterwards `git status --porcelain --ignored` printed nothing.
* Processes and memory: one `wolframscript.exe` with one child `wolfram.exe` per run (in run 18 a second, short one for the summary of Part 4.2); peak working set of the kernel 637.6 MiB (run 16), 623.3 MiB (run 17), 618.7 MiB (run 18) and 628.4 MiB (run 19), sampled about every 2 s.
* Changes to this file in this re-verification: the summary at the top; in Part 1 the documents (DARK_SECTOR_NUMERICS `.tex` and `.pdf`, `provenance/dirac matrices.md`) and the dependents (Dirac-matrices audit files, orchestration records, commit list); in Part 3.3 the Windows PowerShell 5.1 note, the run time and the hardened comparison line; in Part 3.4 the memory, the run-time row and a new row; in Part 4.1 the UTF-16 note; in Part 4.3 runs 12 to 19, the run-time and memory statements; in Part 5 the run list and the temporary files of interrupted runs; this subsection.
* Fixes made to the set: none. No execution defect was found; no file of the set was changed.
* Open discrepancies: none.
