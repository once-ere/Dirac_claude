# Execution provenance: the Stage-1 geometry verifier (WolframScript)

Set: `scripts/verify_dirac16complex_geometry.wls` with `wolfram/Dirac16ComplexGeometry.wl` (old Stage 1, "the field in an arbitrary gravitational field").

Verified on 2026-10-02 at commit `45d47343ae480df46e06689ed822b8f9a88a8030` of https://github.com/once-ere/Dirac_claude.git. Result: the set EXECUTES OK (exit code 0, 43 of 43 checks true, `failed_check_count=0`) and reproduces its committed report byte for byte, in two runs from fresh clones. Re-verified the same day at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (two more runs from two more fresh clones, after a review of this file), and again on 2026-10-07 at commits `a4c5eda1df069a43a55ff8b57148f5de8edd1670` and `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` (four more runs from four more fresh clones, after the workflow that wrote this file had been interrupted by a session limit and restarted): every run executed OK with 43 of 43 checks true and reproduced the committed report byte for byte. The details are in Part 6.

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
* `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` and `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md`, which say that the Mathematica notebook `notebooks/Dirac16ComplexDarkSector.nb` loads the package.
* The execution-provenance files of the sets that use this set, in the folder `provenance/wolframscript/`: `verify_dirac16complex00.PROVENANCE.md`, `verify_dirac16complex_pairing.PROVENANCE.md` and `verify_dirac16complex_matter_antimatter.PROVENANCE.md` (they record the sha256 of the package and/or of the report), and `build_dirac16complex_mathematica_notebook.PROVENANCE.md`, `build_dirac16complex_ks_mathematica_notebook.PROVENANCE.md`, `verify_dirac16complex_mathematica_notebook.PROVENANCE.md` and `verify_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` (their notebooks load the package). `handoff/tools/WOLFRAMSCRIPT_PROVENANCE.md` (the provenance of the design-phase probes) names this set as the shipped verifier that proves the probes' statements again and lists the checks of the report that do so.

**Programs, tests and data files that depend on this set.** The following list is complete for the verified commits (`45d4734`, `c2b33cc` and `a4c5eda`, Part 6): it was made by searching every file of a fresh clone (except the documents `.md`, `.tex`, `.pdf`, `.txt` and the logs) for the names `Dirac16ComplexGeometry`, `wolfram-geometry-report` and `verify_dirac16complex_geometry` and for the three sha256 values of Part 2. (The search was repeated with `git grep` at `a4c5eda` on 2026-10-07: compared with `c2b33cc` it found no new program, test or data file, only the new documents named in the list of documents above.) If you change a program file of this set or the report, these programs and tests are affected.

* Programs that *read* the committed report: `scripts/check_dirac16complex_geometry.py` (option `--wolfram-report`; it records the report's sha256 as `GEO_wolframReportSha256`), `scripts/build_stage1_summary.py`, `scripts/verify_stage1_public_clone_audit.py`, the Stage-1 gates `scripts/verify_stage1_arbitrary_field.ps1` and `scripts/verify_stage1_arbitrary_field.sh` (step `stage1-04-wolfram-geometry`), `wolfram/Dirac16Complex00.wl` (it cites 20 of the report's checks and requires the report's `sourceSha256` of the package to equal the package's current sha256) and `wolfram/Dirac16ComplexMatterAntimatter.wl` (it cites ten of the report's checks and records the report's sha256).
* Programs that compute the *sha256* of the package and/or the report: `scripts/verify_dirac16complex00.wls` (both the package and the report; it writes them into its report), `scripts/verify_dirac16complex_pairing.wls` (the package; it writes it into its report), `scripts/verify_dirac16complex_matter_antimatter.wls` (the package; it writes it into its report) and `scripts/check_dirac16complex_pairing.py` (the package; its check `sourcesCurrent` fails if the package's sha256 differs from the one recorded in the pairing reports).
* Programs that *load* the package: `wolfram/Dirac16Complex00.wl`, `wolfram/Dirac16ComplexPairing.wl`, `wolfram/Dirac16ComplexMatterAntimatter.wl`, `scripts/build_dirac16complex_mathematica_notebook.wls`, `scripts/build_dirac16complex_ks_mathematica_notebook.wls` and the notebooks `notebooks/Dirac16ComplexDarkSector.nb` and `notebooks/Dirac16ComplexKohnSham.nb`.
* Tests: `tests/test_d16c_arbitrary_field_publication.py` (the report is one of the five Stage-1 reports it checks), `tests/test_d16c_arbitrary_field_public_clone_audit.py` (it tests the audit program with small artificial files that carry the report's file name), `tests/test_d16c_kohn_sham_mathematica.py` (it requires the package's sha256 recorded by the Kohn-Sham notebook report to equal the package's current sha256) and `tests/test_d16c_matter_antimatter_publication.py` (it requires the package's sha256 recorded by the Wolfram matter-antimatter report to appear in the matter-antimatter document and to equal the package's current sha256).
* Committed data files that record the sha256 of the report: `artifacts/dirac16complex/arbitrary-field/python-geometry-report.json` and `stage1-summary.json`, `artifacts/dirac16complex/matter-antimatter/matter-antimatter-theory.json` and `wolfram-matter-antimatter-report.json`, `artifacts/dirac16complex/pair-creation/dirac16complex00-theory.json` and `wolfram-dirac16complex00-report.json`. Committed data files that record the sha256 of the package: the report itself, `artifacts/dirac16complex/kohn-sham/mathematica-report.json`, the two matter-antimatter files and the two `dirac16complex00` files just named, and `artifacts/dirac16complex/pair-creation/pairing-theory.json` and `wolfram-pairing-report.json`. Two more committed data files name the package without recording its sha256: `artifacts/dirac16complex/numerics/mathematica-report.json` (in a description of its method) and `artifacts/dirac16complex/pair-creation/python-pairing-report.json` (in the list of files compared by its check `sourcesCurrent`).
* The orchestration records `handoff/stage1_build_slim.json`, six workflow scripts under `handoff/workflows/` and `Revision/workflows/execution_provenance.js` also name these files; they record how the project was built and are not run by a student.

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

(The first line creates the folder for the saved screen output `stdout.txt`; without `> build/geometry-check/stdout.txt` the 341 lines are printed on the screen instead. The PowerShell commands of this file were tested with PowerShell 7; Windows PowerShell 5.1, which comes with Windows, has the same commands but was not tested.) The run takes about 5 to 7.5 minutes on the verification machine (Part 4.3) and prints nothing until the very end, because all lines are printed after the computation. Do not interrupt it.

Then compare the new report with the committed one. Windows PowerShell:

```
$new = (Get-FileHash -Algorithm SHA256 build/geometry-check/wolfram-geometry-report.json).Hash.ToLower()
$old = (Get-FileHash -Algorithm SHA256 artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json).Hash.ToLower()
$new; $old
if ($new -eq $old) { "identical" } else { "DIFFERENT" }
```

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
| `ERROR: D16GeoReport failed or produced messages` or `ERROR: JSON export failed`, exit code 2 | A warning occurred during the computation (for example the computer ran out of memory, or an untested Wolfram version behaves differently). The run needs about 0.65 GB of memory; close other programs and run again. Nothing was written (the report is written only after the computation). |
| A line `failed_checks=...`, `failed_check_count` larger than 0, exit code 1 | A check is false: the computed mathematics differs from the committed result. Do not edit anything to make it pass. Check the sha256 values of the program files (above); if they are the committed ones, report the failing check names and your Wolfram version. |
| The report appears in `artifacts/...` although you gave another path | You typed `--` before the path (Part 3.3). Remove it, and restore the committed file with `git checkout -- artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`. |
| The new report differs from the committed one, but all 43 checks are true | Most likely another Wolfram version: compare the `producer` lines (Part 4.4). If you edited a program file, its `sourceSha256` entry changes too. |
| PowerShell says the path to `stdout.txt` could not be found | The folder `build/geometry-check` does not exist yet: run the `New-Item` line first. |
| It runs much longer than 8 minutes | Slower computers need longer; the computation is exact and uses essentially one processor core, so more cores do not help. Let it finish. If you stop it with Ctrl+C, no report is written and the old one is left unchanged. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly 341 lines on the standard output and nothing on the error stream. On Windows the printed lines end with CR LF, also when the output is redirected into a file from PowerShell or Git Bash; on macOS and Linux they normally end with LF only (not tested here). The 341 lines are:

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

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GB RAM, Windows 11 Pro for Workstations 10.0.26200, Wolfram 15.0.1, WolframScript 1.14.0), with several other Wolfram kernels of other jobs running at the same time:

| Run | Report path | Wall time | Exit code | Peak working set of the kernel |
| --- | --- | --- | --- | --- |
| 1 | usage line (committed path) | 303.7 s | 0 | 635.6 MiB |
| 2 | usage line (committed path) | 366.4 s | 0 | 638.1 MiB |
| 3 | `build/geometry-check/...` | 364.4 s | 0 | 625.2 MiB (sampled after 236 s) |
| 4 | `build/geometry-check/...`, PowerShell block of Part 3.3 | 314.9 s | 0 | not measured |
| 5 | `build/geometry-check/...`, bash block of Part 3.3 | 314 s | 0 | not measured |
| 6 | `build/geometry-check/...`, PowerShell block of Part 3.3 (re-verification) | 301.4 s | 0 | not measured |
| 7 | `build/geometry-check/...`, bash block of Part 3.3 (re-verification) | 404.1 s | 0 | not measured |

Runs 2 and 3 overlapped in time, and so did runs 4 and 5, which made them slower than run 1; runs 6 and 7 did not overlap with each other, but other Wolfram jobs ran on the machine at the same time (a process list taken 39 s after the end of run 7 showed eleven other Wolfram kernels: one started before run 6, seven started during run 7); this is the most likely reason for the 404 s of run 7. Expect about 5 to 7 minutes on a similar machine. (Chapter 19.6 of the textbook, `provenance/textbook/chapters/19-reproducing-everything.md`, gives 409 s for the same step in a Bash run of the Stage-1 gate from a fresh clone made for that edition of the textbook; the committed Stage-1 gate logs of 2026-09-30 under `handoff/reviews/` record no time for this step.) The computation runs in one kernel and uses essentially one core (the kernel's processor time was about 1.04 times the wall time), so the time depends mainly on the speed of one core. The peak memory (working set) of the kernel process was about 0.64 GB; WolframScript itself used about 17 MB.

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

* With the usage line of Part 3.3 it **overwrites the committed file** `artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json`. With Wolfram 15.0.1 the new bytes are identical, so `git status --porcelain --untracked-files=all` prints nothing afterwards (measured in both verification runs).
* With the recommended scratch path it creates the folder `build/geometry-check/` (and `build/` if missing) and the report in it; `build/` is ignored by git, so `git status` stays empty. The saved screen output `build/geometry-check/stdout.txt` is created by your terminal, not by the script.
* No other file in the repository is created, changed or deleted. The script does not write a log file and leaves no partial file: the report is written in one piece after the computation has finished.

**Temporary files.** None in the system temporary folder: verification run 1 pointed `TEMP` and `TMP` at an empty private folder, which was still empty afterwards. On Windows WolframScript itself keeps a spool file for the kernel's printed output, `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\tmp_<10 random characters>`, for the duration of the run and deletes it when the run ends normally (measured in run 2), and it rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (238 bytes on the verification machine; only the modification time changed) at every start. On macOS and Linux WolframScript keeps the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process (`wolfram.exe` on the verification machine, started with `-linkmode Connect -linkname <name>_shm`, so it talks to WolframScript through shared memory), which runs for the whole computation and exits at the end. No further kernels are started (the package contains no parallel computation).

**Network.** None. The script and the package contain no network calls (no `URL...`, no web `Import`, no external programs). At a snapshot taken during runs 2 and 3 the kernels and WolframScript had no TCP connections and no UDP endpoints. (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of this script.)

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
