# Execution provenance: the Stage-2 primordial-field verifier (WolframScript)

Set: `scripts/verify_dirac16complex_primordial.wls` with `wolfram/Dirac16ComplexPrimordial.wl` (old Stage 2, "dirac16complex in the primordial pair-creation gravitational field").

Verified on 2026-10-07 at commit `b8a695d1faa7abe43b4b51eb666f25d250420fb7` of https://github.com/once-ere/Dirac_claude.git, that is, after the script's error handling was fixed in commit `b980c803830541395603016613b2a48b454ca872` of 2026-10-07 ("Fix the primordial verifier's false-success path"; the files of this set and its committed outputs have not changed since that commit). Result: the set **EXECUTES OK** (exit code 0, 126 of 126 checks true, `failed_check_count=0`) and **reproduces both committed output files byte for byte**: two runs in two fresh clones, then the student commands of Part 3.3 for Windows PowerShell and for macOS/Linux (in Git Bash) in those two clones, and a run with `--` before the report path; all five runs wrote byte-identical outputs. The failure cases of Part 3.4 were measured with the fixed script (missing package, damaged package, missing notebook, missing fixture, an output file that cannot be written, a forced stop). The set was first verified on 2026-10-02 and again on 2026-10-07 before the fix; those runs used the same package, the same inputs and the same computation, and their report differs from today's committed report only in the line that records the script's own sha256. The details are in Part 6.

This file is written for a student who has never used Wolfram software. Everything you need to run the set is in this file; you do not have to read any other file first.

## 1. What this set is and what it computes

**The physics in plain words.** The project studies a field called "dirac16complex": a field with 16 complex components (a "spinor") that lives in an 8-dimensional space-time with 4 space-like and 4 time-like directions. The coordinates are called x0, ..., x7; x4 plays the role of the time in which the field evolves, and x5, x6, x7 are three extra times. The flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). The field values are not ordinary numbers but *Grassmann* numbers: two of them anticommute (theta1 theta2 = -theta2 theta1), as they must for a fermion field.

Stage 1 of the project wrote down how this field behaves in an *arbitrary* gravitational field. Stage 2, checked by this set, repeats those calculations for **one fixed gravitational field**: the "primordial" (pair-creation) field of the author's Mathematica notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`, whose metric is called MatrixMetric44 there. With the abbreviations z = 6 H x0 (0 < z < pi/2), t = H x4, s = sin z and an arbitrary function a4(t), the metric is diagonal,

```
g = diag( cot(z)^2,  s^(1/3) e^(2 a4)  (x1, x2, x3),  -1,  -s^(1/3) e^(-2 a4)  (x5, x6, x7) ),
```

with 4 positive and 4 negative entries. Ordinary 3-space (x1, x2, x3) and the three extra times (x5, x6, x7) are scaled in opposite directions by a4: when 3-space inflates, the extra times deflate.

**What the computer does.** The script checks that the package file exists, loads the package and calls its function `D16PRun`, which computes everything with **exact symbolic algebra** in the Wolfram Language; it never uses floating-point numbers to decide anything. It

* rebuilds the eight 16x16 gamma matrices gamma^0, ..., gamma^7 from the split-octonion recipe of the project and compares them with the committed Stage-1 fixture file;
* computes, for an arbitrary a4, the metric, the vielbein, the Christoffel symbols, the spin connection omega_mu_ab, the spinor connection Omega_mu = (1/2) omega_mu_ab S^ab, the 16 component field equations gamma^mu D_mu Psi = (m + lambda S) Psi (S = Psibar Psi), the energy-momentum tensor, the mode equations, the Einstein tensor, the question which field states can be the source of this gravitational field, the canonical quantization data, and the special case a4 = t;
* tests every identity exactly in two independent ways: (A) a complete zero test in the ring of rational functions of s^(1/6), cos z, e^a4, a4', a4'', ... modulo cos^2 z + sin^2 z = 1, and (B) exact point checks at sin z = 3/5 and sin z = 5/13 with fractional values of a4 and its derivatives;
* **reads** the author's notebook (it never writes it) and compares the outputs stored in the notebook cells 501, 583, 584, 1060, 1079, 1089, 1096, 1111 and 1137 with its own rebuild. It reproduces all 16 stored equations of cell 1137 and finds that they differ from the correct equations only by a term q = Q1 sinh(a4) a4' e^(-a4) in 8 of the 16 equations.

**The 126 checks.** Each check is `true` when the stated identity holds exactly. They come in 17 groups (the group is the second part of the name, `P_<group>_<name>`):

| Group | Checks | What must hold |
| --- | --- | --- |
| `P_internal` | 2 | the exact zero test works (sanity cases); no internal exception occurred during the run |
| `P_fixture` | 4 | the rebuilt gamma matrices, C and the chirality matrix equal the committed fixture; {gamma^a, gamma^b} = 2 eta^ab; C = gamma^0 gamma^1 gamma^2 gamma^3; every row of every gamma matrix has exactly one nonzero entry |
| `P_metric` | 6 | g = e eta e^T for the vielbein e; signature (4,4); det g = +cos^2 z; sqrt\|det g\| = cos z; the notebook's cell 1060; exact point checks |
| `P_zeta` | 4 | the coordinate zeta = ln(sin z)/(6H): g_zeta_zeta = 1, the warp factor e^(2 H zeta), the range (-infinity, 0), the warped form of the metric |
| `P_christoffel` | 3 | all 512 Christoffel symbols in closed form; 37 are nonzero (25 with mu <= nu); point checks |
| `P_spinconn` | 6 | the vielbein postulate (512 components); omega_mu_ab = -omega_mu_ba; closed forms; 24 nonzero components; the notebook's cell 501; point checks |
| `P_Omega` | 8 | closed forms of Omega_mu; Omega_0 = Omega_4 = 0; Omega_mu is block diagonal (does not mix the two chiralities); gamma^mu Omega_mu = 3 H gamma^0 and Omega_mu gamma^mu = -3 H gamma^0, independent of a4; agreement with the general formula for a diagonal vielbein; point checks |
| `P_gammaConst` | 7 | D_mu gamma^nu = 0 for all 64 pairs; with the notebook's contraction (1/2) omega_mu^a_b S^ab instead it fails (15 pairs, 288 entries, closed forms); d_mu(sqrt\|g\| gamma^mu) = sqrt\|g\| [gamma^mu, Omega_mu] = 6 H cos z gamma^0 |
| `P_EL` | 7 | the 16 component field equations: ten terms each, the evolution form, the derivation from the Lagrangian (varying Psi^dagger and Psi), the zeta form, point checks |
| `P_blocks` | 3 | for fields of x0 and x4 only, the 16 equations split into four closed blocks {0,5,8,13}, {1,4,9,12}, {2,7,10,15}, {3,6,11,14}, the same as the notebook's coupling sets |
| `P_notebookCompare` | 16 | the notebook's source cells are as rebuilt; the stored outputs of cells 1079, 1089, 1096, 1111 and 1137 (16 of 16 equations) are reproduced; the correct equations differ from the stored ones only by +-q yZ_j in yZ_0..yZ_7; the q term is traced to non-Clifford "curved gammas" for x5, x6, x7 (a reconstruction of cell 1058) |
| `P_EMT` | 18 | the energy-momentum tensor: symmetric; its Omega part; the homogeneous sector (rho = m S + U - K_0, the pressures); on-shell relations; conservation on shell and its failure off shell; the (x0, x4) sector |
| `P_modes` | 7 | the dispersion relation h^2 = (M_eff^2 + K^2) 1, the spectrum +-E (8 times each), the exact reduction, non-separability for nonzero transverse momenta, the local (WKB) dispersion, Hermiticity only without x5 momentum, the onset of the instability |
| `P_einstein` | 10 | R = 6 H^2 (a4'^2 - 7); the mixed Einstein tensor in closed form, off-diagonal part zero; the notebook's cells 583 and 584; R_44; the required source with energy density rho_req = -3 H^2 (7 + a4'^2)/kappa < 0; the energy conditions |
| `P_source` | 11 | which field states can source G^mu_nu = kappa T^mu_nu: no state of (x0, x4) when a4'' is not 0; never a plane wave with real K; the x0-independent state Psi = u(x4) when a4'' = 0, with two exact examples (A: a4 = sqrt(5) t; B: a4 = t) |
| `P_quant` | 11 | the matrix B = -i C gamma^4 (Hermitian, B^2 = 1, eigenvalues +1 and -1 eight times each); the anticommutator {Psi_a, Psi_b^dagger} = B_ab delta/cos z; the canonical momentum and Hamiltonian density; the Heisenberg equation reproduces the field equations; Hermiticity in the "good" sector; the x5, x6, x7 momenta are not Hermitian; the map Psi -> gamma^8 Psi |
| `P_a4linear` | 3 | a4 = t: R = -36 H^2, G = diag(12, 12, 12, 12, 24, 12, 12, 12) H^2, rho_req = -24 H^2/kappa, w = -1/2; isotropy whenever a4'' = 0; the two slopes listed in the notebook's cell 150 also give rho_req < 0 |

**A note on matrices named C, B and gamma^8.** In this set C is a 16x16 matrix, C = gamma^0 gamma^1 gamma^2 gamma^3 (called sigma16 in the notebook), used to form Psibar = Psi^dagger C; B = -i C gamma^4 is the 16x16 matrix in the canonical anticommutator. Neither is a charge conjugation, and this set makes no statement about charge conjugation. The only discrete map it checks is the **matrix** map Psi -> gamma^8 Psi with the 16x16 matrix gamma^8 = gamma^0 gamma^1 ... gamma^7 = diag(-1 (8 times), +1 (8 times)), which turns solutions with (m, lambda) into solutions with (-m, -lambda) (checks `P_quant_gamma8MapsMtoMinusM` and `P_quant_gamma8LagrangianSign`).

**The 41 measurements.** Besides the checks, the report records 41 "measurements": conventions, counts and descriptive texts. Examples: `notebookNonOutputCellCount` = 1279, `christoffelNonzeroCount` = 37, `omegaLowNonzeroCount` = 24, `notebookContraction_DmuGammaNu_nonzeroEntries` = 288, `x0x4BlocksCorrectEquations` = {{0, 5, 8, 13}, {1, 4, 9, 12}, {2, 7, 10, 15}, {3, 6, 11, 14}}, `condensateWronskian_1_invS_invS2` = -2*Cot[z]^3*Csc[z]^3, `source_x0Independent_Meff` = (-6*H^2*(1 + Derivative[1][a4][t]^2))/(kap*SS). Two measurements contain the version string of the Wolfram kernel that ran the script: `notebookSessionEvidence` and `cell1058LiteralThisKernel_version` (Part 4.4).

**The components file.** The second output, `primordial-components.json`, contains every computed component as a TeX string and as a string that the Python library sympy can parse: the Christoffel symbols, the spin connection, the 16x16 matrices Omega_mu, the 16 field equations in four presentations and in evolution form, the four blocks, the equation-by-equation comparison with the notebook, the energy-momentum tensor, the modes, the Einstein tensor, the source analysis, the quantization data and the case a4 = t (17 top-level keys).

**Documents that cite its results.**

* `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` (and its `.tex` and `.pdf`), the Stage-2 document: its formulas are taken from `primordial-components.json`; Section 18 lists the check groups and, in 18.4, the sha256 of the notebook, the fixture, both files of this set and the components file; Section 19 gives the commands.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/00-how-to-read.md`, `01-mathematical-toolkit.md`, `04-curved-space.md` ("wolfram-primordial-report.json 126 of 126 true"), `09-primordial-field.md`, `18-open-problems.md`, `19-reproducing-everything.md` (it quotes the sha256 prefix `a5d8caa8cb226082` of the components file, which is current, and the prefix `a0164273df62f2e1` of the report as it was before the fix of 2026-10-07; the current report begins `f8731e0eaba15a0f`, Part 6) and `20-glossary-and-check-index.md`.
* `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (and `.tex`, `.pdf`), the Stage-1 document, which uses the notebook-cell numbering of the package's function `loadNotebookCells`.
* `README.md`, which names the Stage-2 gate (below).
* `notebooks/dirac16complex_dark_sector.PROVENANCE.md`, the provenance file of the dark-sector Jupyter notebook, which lists the report (190 lines, 13638 bytes) among the inputs of that notebook, with the report's sha256 from before the fix of 2026-10-07 (Part 6).

**Programs that read its outputs or load its package.** `scripts/check_dirac16complex_primordial.py` reads `primordial-components.json` (its check `P_EL_agreesWithWolfram`) and records that file's sha256 in `artifacts/dirac16complex/primordial-field/python-primordial-report.json`; `tests/test_d16c_primordial.py` reads the components file; `tests/test_d16c_primordial_publication.py` reads both outputs and compares the numbers, TeX strings, hashes and the kernel version quoted in the Stage-2 document with them; the Stage-2 gate `scripts/verify_stage2_primordial_field.ps1` and `.sh` runs exactly the command of this set as its step `stage2-01-wolfram-primordial`; `wolfram/Dirac16Complex00.wl` (Stage 5) loads this package and cites the report's checks, requiring that the report's `sourceSha256` entry of the package equals the package's current sha256; `scripts/verify_dirac16complex00.wls` records the sha256 of the package and of the report in `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and `dirac16complex00-theory.json` (the committed copies of these two files still record the report's sha256 from before the fix of 2026-10-07, Part 6); the Jupyter notebook `notebooks/dirac16complex_dark_sector.ipynb` loads the report in its "verification gauntlet" (Section 11 of that notebook, the 21st of its 23 cells). This is why both outputs must be reproduced byte for byte.

## 2. Files

All files below are stored with LF line endings; the repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values are the same on Windows, macOS and Linux.

**Program files.**

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `scripts/verify_dirac16complex_primordial.wls` | the script you run: checks that the package file exists, loads the package, calls `D16PRun`, checks that it returned its checks, measurements and components, writes the two JSON files (stopping with an `ERROR:` line if a file cannot be written), prints the verdict, sets the exit code | 91 | 5754 | `f49606ba044ace6eb0ebc5e7661a7823f826416f234fce756acd9a2ccab958f9` |
| `wolfram/Dirac16ComplexPrimordial.wl` | the package (context ``Dirac16ComplexPrimordial` ``): gamma matrices, exact ring and zero tests, TeX and Python printers, the primordial field, the notebook reader and all checks; entry point `D16PRun[repoRoot]` | 1224 | 101130 | `0b95682601ace6343a89ad8eaf0f4896d071015041f15cccbeb3beac193d81a1` |

**Inputs.** The package reads two data files, and the script computes the sha256 of all four files below and writes them into the report as `sourceSha256`:

| File | How it is read | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `Import[..., "RawJSON"]`: the committed Stage-1 gamma matrices, C and chirality | 18440 | 213133 | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` |
| `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` | `Get[...]`: the author's notebook, read as an expression (never opened in a front end, never written) | 471194 | 24489589 | `5ee5cb2a95146136ee65636a4aef174f303b6c41da130d2c57e4684f9c8ff69f` |
| `scripts/verify_dirac16complex_primordial.wls` | hashed only | 91 | 5754 | `f49606ba044ace6eb0ebc5e7661a7823f826416f234fce756acd9a2ccab958f9` |
| `wolfram/Dirac16ComplexPrimordial.wl` | `Get[...]` (the package) and hashed | 1224 | 101130 | `0b95682601ace6343a89ad8eaf0f4896d071015041f15cccbeb3beac193d81a1` |

Because the report records the script's own sha256, every edit of the script changes the report; this is why the fix of 2026-10-07 changed exactly one line of the committed report (Part 6). Nothing else is read: no other package, no environment variable, nothing from the network. The script finds the repository root from its own location (the folder above `scripts`), so all inputs are found from any current folder.

**Outputs.** Two files, written into the folder of the report path you give (the folder is created if it does not exist). A relative report path is taken relative to the repository root, not to the current folder; a path starting with `/` or with a drive letter such as `C:` is used as it is. Without a path argument the script uses the committed path below. With the usage line of Part 3.3 the outputs are the committed files:

| File | Lines | Bytes | sha256 (committed) |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` | 190 | 13638 | `f8731e0eaba15a0fa05f4e3193dd9b2a7f3311a0f995d05352e5a2486d230bd3` |
| `artifacts/dirac16complex/primordial-field/primordial-components.json` | 6981 | 191740 | `a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` |

The components file always gets the name `primordial-components.json` and is written next to the report, whatever name you give the report. Both files are pure ASCII JSON with LF line endings, indented with tabs, ending with a newline. The report's top-level keys are `schemaVersion` (1), `producer`, `checks` (126 entries, all `true`), `measurements` (41 entries) and `sourceSha256` (the four sha256 values above). The output paths do not appear inside the files, so a report written to another folder is byte-identical to the committed one. The files are written only after the whole computation has finished, the report first and then the components file; a run that stops with an `ERROR:` line before that point writes neither file (Part 3.4).

## 3. How to run it

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs: the Wolfram Language *kernel* (the computing engine) and *WolframScript* (the command `wolframscript`, which runs a script file with the kernel). The verification used the kernel "Wolfram 15.0.1" and WolframScript 1.14.0.

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

   and enter your Wolfram ID and password when asked. (Running `wolframscript` without options on a not yet activated engine asks the same questions. If it shows the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.) The activation needs an internet connection once.

**Option 2: Wolfram (formerly Mathematica), the desktop product.** A licensed Wolfram or Mathematica installation contains the kernel; on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/ as in step 2 above.

**Test the installation.** In a new terminal type

```
wolframscript -code '$Version'
```

It must print the kernel version, on the verification machine `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. Keep the single quotes: on macOS and Linux they stop the shell from replacing `$Version`, and in PowerShell they are correct too. If several versions are installed, `wolframscript` uses the newest one; `wolframscript -configure` prints its settings, whose line `WOLFRAMSCRIPT_KERNELPATH=...` names the kernel (a leading `//` means that this is the automatic choice). To use a particular installed kernel, add `-local "<path of that kernel>"` before `-file`, for example `wolframscript -local "C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -file ...` on the verification machine.

**Which version.** The verification used version 15.0.1 on Windows, and only that combination is known to reproduce the committed report byte for byte, because the report contains the kernel's version string (Part 4.4). Other versions and operating systems were not tested.

### 3.2 Get the repository

Install git if you do not have it (Windows: https://git-scm.com/download/win; macOS: type `xcode-select --install` in Terminal; Debian/Ubuntu Linux: `sudo apt install git`). Then, in the folder where you want the repository:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone occupies about 740 MB on disk (measured on 2026-10-07 at commit `b8a695d`; it was about 520 MB on 2026-10-02 and grows as the repository grows). On the verification machine a clone took about 35 seconds. Every command below is typed in this folder, the *repository root* (the folder that contains `scripts`, `wolfram` and `artifacts`). (Instead of git you may download the ZIP archive from the GitHub page, button "Code", "Download ZIP", and unpack it; then `git status` and `git checkout` below are not available, and you compare files with the sha256 commands of Part 3.3 instead.)

### 3.3 Run it

The usage line in the script's header is

```
wolframscript -file scripts/verify_dirac16complex_primordial.wls artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
```

It is the same single line in Windows PowerShell, in the macOS Terminal (zsh) and in a Linux terminal (bash). It **overwrites the two committed files** `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` and `artifacts/dirac16complex/primordial-field/primordial-components.json` with the newly computed ones. With Wolfram 15.0.1 on Windows the new files are byte-identical to the committed ones, so nothing changes. Afterwards check with

```
git status --porcelain
```

which must print nothing (Part 5 says how to restore the files if it prints something; files that you added to the folder yourself, if any, are listed with `??`, but the two files of this set must not appear).

**Recommended for students: write the outputs to a scratch folder instead**, so that the committed files are never touched, and then compare. The folder `build/` is ignored by git (rule `/build/` in `.gitignore`), and the script creates missing folders itself.

Windows PowerShell (Windows PowerShell 5.1 or PowerShell 7):

```
New-Item -ItemType Directory -Force build/primordial-check | Out-Null
wolframscript -file scripts/verify_dirac16complex_primordial.wls build/primordial-check/wolfram-primordial-report.json > build/primordial-check/stdout.txt
"exit code: $LASTEXITCODE"
Get-Content build/primordial-check/stdout.txt -Tail 5
```

macOS (Terminal, zsh) and Linux (bash):

```
mkdir -p build/primordial-check
wolframscript -file scripts/verify_dirac16complex_primordial.wls build/primordial-check/wolfram-primordial-report.json > build/primordial-check/stdout.txt
echo "exit code: $?"
tail -n 5 build/primordial-check/stdout.txt
```

(The first line creates the folder for the saved screen output `stdout.txt`; without `> build/primordial-check/stdout.txt` the 192 lines are printed on the screen instead, the first 20 of them while the computation runs.) The run took between one and two and a half minutes on the verification machine, depending on how busy the machine was (Part 4.3); with the redirection nothing appears on the screen until it has finished. Do not interrupt it.

Then compare the two new files with the committed ones. Windows PowerShell:

```
foreach ($f in "wolfram-primordial-report.json", "primordial-components.json") {
  $new = (Get-FileHash -Algorithm SHA256 "build/primordial-check/$f").Hash.ToLower()
  $old = (Get-FileHash -Algorithm SHA256 "artifacts/dirac16complex/primordial-field/$f").Hash.ToLower()
  if ($new -eq $old) { "$f identical $new" } else { "$f DIFFERENT new=$new committed=$old" }
}
```

macOS and Linux:

```
for f in wolfram-primordial-report.json primordial-components.json; do
  cmp "build/primordial-check/$f" "artifacts/dirac16complex/primordial-field/$f" && echo "$f identical"
done
```

and, to see the sha256 values, `shasum -a 256 build/primordial-check/*.json` on macOS or `sha256sum build/primordial-check/*.json` on Linux. You must see `identical` for both files, and the sha256 values must be `f8731e0eaba15a0fa05f4e3193dd9b2a7f3311a0f995d05352e5a2486d230bd3` for the report and `a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` for the components file.

**About `--` before the report path.** Pass the report path directly after the script name, as above. With WolframScript 1.14.0, `wolframscript -file s.wls -- r.json` drops `--` and everything after it for a script file that does not start with a `#!` line; this script starts with `#!/usr/bin/env wolframscript`, and for it the verification measured that `--` and the path do arrive and that the script removes the `--`, so both forms wrote to the same scratch folder (measured again on 2026-10-07 with the fixed script: `wolframscript -file scripts/verify_dirac16complex_primordial.wls -- build/dashdash/wolfram-primordial-report.json` wrote both files, byte-identical to the committed ones, into `build/dashdash/`). Do not rely on that: if the path is ever dropped, the script writes to the committed paths instead.

### 3.4 If it fails

| What you see | Cause and fix |
| --- | --- |
| After a few seconds (4 to 6 s on the verification machine) a single line `ERROR: package not found: <your repository folder>\wolfram\Dirac16ComplexPrimordial.wl` (on macOS and Linux with `/` instead of `\`), nothing on the error stream, **exit code 1** | The package file `wolfram/Dirac16ComplexPrimordial.wl` is missing (for example an incomplete download, or a file moved away). Nothing was computed and **no output file was written**: with the usage line of Part 3.3 the committed files are untouched; only the folder of the report path is created if it did not exist (with the scratch path an empty `build/primordial-check`). Restore the package with `git checkout -- wolfram/Dirac16ComplexPrimordial.wl` (or clone again) and run again. |
| After a few seconds (5 s measured) a single line ``ERROR: Dirac16ComplexPrimordial`D16PRun did not return an Association with checks, measurements and components (the package did not load or did not run)``, nothing on the error stream, **exit code 1** | The package file exists but is damaged or incomplete (measured with an empty package file), or an edited copy contains an error, so the function `D16PRun` is not defined. Nothing was computed and no output file was written. Compare the package's sha256 with Part 2 (`Get-FileHash -Algorithm SHA256 wolfram/Dirac16ComplexPrimordial.wl` in PowerShell, `shasum -a 256 wolfram/Dirac16ComplexPrimordial.wl` on macOS, `sha256sum wolfram/Dirac16ComplexPrimordial.wl` on Linux), restore it with `git checkout -- wolfram/Dirac16ComplexPrimordial.wl` (or clone again) and run again. |
| PowerShell: `The term 'wolframscript' is not recognized`; macOS/Linux: `command not found: wolframscript` | WolframScript is not installed or not on the PATH. Open a new terminal after the installation. On Windows the program is in `C:\Program Files\Wolfram Research\WolframScript\`; add that folder to the PATH or install again. On macOS and Linux install WolframScript separately (Part 3.1, step 2). |
| A message containing "licence"/"license", "password", "activate", "kernel limit", "too many kernels", "maximum number of" or "could not launch/start/connect" | The kernel is not activated, or your licence allows fewer kernels at the same time than are running. Run `wolframscript -activate` again; close other Wolfram programs and notebooks; wait 30 seconds and run again. (The project's Stage-2 gate, `scripts/verify_stage2_primordial_field.ps1` and its twin `.sh`, makes up to three attempts of this step, i.e. retries it up to twice after 30 seconds, when the step fails with a nonzero exit code and its log contains licence/license, password, kernel limit, maximum number of, too many kernels or could not launch/start/connect; "activate" is not in its list, so the gate does not retry for that message alone.) |
| Lines `  CHECK FAILED: <name>` (indented by two spaces) among the progress lines, `failed_check_count` larger than 0, exit code 1 | A check is false: the computed mathematics differs from the committed result. Do not edit anything to make it pass. Compare the sha256 values of the program files and inputs with Part 2 (`Get-FileHash -Algorithm SHA256 <file>` in PowerShell, `shasum -a 256 <file>` on macOS, `sha256sum <file>` on Linux); if they differ, run `git checkout -- <file>` or clone again. If they are the committed ones, report the failing check names and your Wolfram version. |
| A line `INTERNAL ERROR: ...` followed by `  CHECK FAILED: P_internal_noException`, then `check_P_internal_noException=false`, fewer than 126 checks, exit code 1 | The package stopped with an internal error (for example an untested Wolfram version that simplifies an expression differently); the checks computed up to that point are still printed and written. (This case is read from the code; it did not occur in the verification.) Report the line and your Wolfram version. |
| After the whole computation (1 to 2.5 minutes), either (a) `Get::noopen` naming `Pair_Creation_of_...-Nash.nb` right after the progress line `loading notebook (read only)`, among many other error messages (measured: `Part::partd`, `StringRiffle::list`, `StringJoin::string`, `General::stop`, `Table::iterb`, `ConnectedComponents::graph`, `Part::partw`, and after the progress line `done in <N> s` `FileHash::noopen` naming the notebook), 17 `  CHECK FAILED: ...` lines (every check that compares with a stored notebook output), `check_count=126`, `failed_check_count=17`, 253 lines in all instead of 192; or (b) `Import::nffil` naming `algebra-fixture.json` right after the progress line `fixture`, then `  CHECK FAILED: P_fixture_gammasMatchCommittedFixture` and `  CHECK FAILED: P_fixture_CAndChiralityMatch`, after the progress line `done in <N> s` `FileHash::noopen` naming the fixture, `check_count=126`, `failed_check_count=2`, 198 lines in all; in both cases exit code 1 | An input file is missing: the repository is incomplete. The two output files **are still written**, with the failed checks (and, measured for the missing fixture, with `ToLowerCase[$Failed]` instead of the missing file's sha256 in the report's `sourceSha256`); with the usage line of Part 3.3 they replaced the committed files. Restore the missing file and the outputs with `git checkout -- <missing file> artifacts/dirac16complex/primordial-field/` (or clone again) and run again. (Both cases were measured on 2026-10-07 with the fixed script.) |
| After the whole computation (the 20 progress lines, 1 to 2.5 minutes), one line `ERROR: could not write <full path of the file>`, nothing on the error stream, exit code 1 | The output file cannot be written: it is read-only, or another program (an editor, a JSON viewer) holds it open and locked, or the folder is not writable. The script writes the report first and then the components file; the file named in the line keeps its old content and the files after it are not written (measured with a read-only report file: it kept its old content and no components file was written). Close the program that holds the file, remove the read-only attribute (PowerShell: `Set-ItemProperty <file> -Name IsReadOnly -Value $false`; macOS/Linux: `chmod u+w <file>`), or give another report path, and run again. |
| The new report (and possibly the components file) differs from the committed one, but `check_count=126` and `failed_check_count=0` | Most likely another Wolfram version or operating system: the report contains the kernel's version string (Part 4.4). |
| PowerShell 7: `OpenError: ... Could not find a part of the path '...\build\primordial-check\stdout.txt'.` (Windows PowerShell 5.1: `out-file : Could not find a part of the path ...stdout.txt'.`); macOS/Linux: `bash: build/primordial-check/stdout.txt: No such file or directory` (zsh on macOS: `zsh: no such file or directory: build/primordial-check/stdout.txt`); the prompt returns at once | The folder `build/primordial-check` for the saved screen output does not exist yet, so the shell could not open `stdout.txt`. **wolframscript was not started at all** (nothing was computed and no file was written; in PowerShell `"exit code: $LASTEXITCODE"` then prints no number or an old one, in bash/zsh `echo "exit code: $?"` prints 1). Run the `New-Item` line (PowerShell) or the `mkdir -p` line (macOS/Linux) first, then repeat the `wolframscript` line. |
| It runs longer than 2.5 minutes | Slower or busier computers need longer; the computation is exact and runs in one kernel. On the verification machine a normal run took 1 to 2.5 minutes, the longer times while many other Wolfram jobs were running (Part 4.3); a run that takes somewhat longer than 2 minutes is not a failure. Let it finish. The progress lines (Part 4.1) show where it is; the longest step is `P_EMT` (27 to 68 seconds on the verification machine, depending on its load). If you stop it (Ctrl+C, closing the window), the output files are not written and the old ones are left unchanged (they are written only after the computation), but WolframScript can leave a temporary file behind (Part 5). |
| The machine runs out of memory | The kernel needs about 330 MiB (Part 4.3). Close other programs and run again. |

## 4. Expected output

### 4.1 Printed lines and exit code

The script prints exactly **192 lines** on standard output (on Windows with CRLF line ends; on macOS and Linux, which were not tested, LF line ends are expected) and nothing on the error stream:

1. 20 progress lines, printed while the computation runs, each starting with the local clock time:

   ```
   [hh:mm:ss] zero-test sanity
   [hh:mm:ss] fixture
   [hh:mm:ss] loading notebook (read only)
   [hh:mm:ss] geometry
   [hh:mm:ss] P_metric
   [hh:mm:ss] P_zeta
   [hh:mm:ss] P_christoffel
   [hh:mm:ss] P_spinconn
   [hh:mm:ss] P_Omega
   [hh:mm:ss] P_gammaConst
   [hh:mm:ss] P_EL
   [hh:mm:ss] P_blocks
   [hh:mm:ss] P_notebookCompare
   [hh:mm:ss] P_EMT
   [hh:mm:ss] P_modes
   [hh:mm:ss] P_einstein
   [hh:mm:ss] P_source
   [hh:mm:ss] P_quant
   [hh:mm:ss] P_a4linear
   [hh:mm:ss] done in <N> s
   ```

2. 126 check lines, in this order:

   ```
   check_P_internal_zeroTestSanity=true
   check_P_fixture_gammasMatchCommittedFixture=true
   check_P_fixture_CAndChiralityMatch=true
   check_P_fixture_cliffordAndC=true
   check_P_fixture_gammaRowsSignedPermutations=true
   check_P_metric_vielbeinProduct=true
   check_P_metric_signature44=true
   check_P_metric_detG_equals_plus_cos2z=true
   check_P_metric_sqrtAbsDetG_cosz=true
   check_P_metric_notebookCell1060Det=true
   check_P_metric_pointCheck=true
   check_P_zeta_gZetaZetaIsOne=true
   check_P_zeta_warpFactor=true
   check_P_zeta_range=true
   check_P_zeta_warpedMetric=true
   check_P_christoffel_closedForms512=true
   check_P_christoffel_count=true
   check_P_christoffel_pointCheck=true
   check_P_spinconn_vielbeinPostulate512=true
   check_P_spinconn_antisymmetry=true
   check_P_spinconn_closedForms=true
   check_P_spinconn_count24=true
   check_P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega=true
   check_P_spinconn_pointCheck=true
   check_P_Omega_closedForms=true
   check_P_Omega_zeroForX0X4=true
   check_P_Omega_blockDiagonalChirality=true
   check_P_Omega_gammaSlash3Hgamma0=true
   check_P_Omega_OmegaGammaAndAnticommutator=true
   check_P_Omega_slashA4Independent=true
   check_P_Omega_contractDiagonalFormula=true
   check_P_Omega_pointCheck=true
   check_P_gammaConst_DmuGammaNuZero64=true
   check_P_gammaConst_notebookContractionFails=true
   check_P_gammaConst_notebookContractionClosedForms=true
   check_P_gammaConst_divergenceIdentity=true
   check_P_gammaConst_divergenceIdentityFailsNotebookContraction=true
   check_P_gammaConst_divergenceLhsValue=true
   check_P_gammaConst_pointCheck=true
   check_P_EL_componentsMatchOperator=true
   check_P_EL_tenTermsPerEquation=true
   check_P_EL_pointCheck=true
   check_P_EL_evolutionFormEquivalent=true
   check_P_EL_fromLagrangianPsiDagger=true
   check_P_EL_fromLagrangianPsi=true
   check_P_EL_zetaFormChainRule=true
   check_P_blocks_fourBlocksOfFour=true
   check_P_blocks_closedUnderCoupling=true
   check_P_blocks_matchNotebookSets=true
   check_P_notebookCompare_sourceCellsAsRebuilt=true
   check_P_notebookCompare_spinCoefficientsCell499EqualsOmegaMuIJ=true
   check_P_notebookCompare_storedEla16=true
   check_P_notebookCompare_commutingQ1DropsOutCliffordGammas=true
   check_P_notebookCompare_reconstructionReproducesStoredEla=true
   check_P_notebookCompare_literalRebuildResidualIsExactlyQTerms=true
   check_P_notebookCompare_qTermFromNonCliffordExtraTimeGammas=true
   check_P_notebookCompare_qVectorIs2HqAtCell1079=true
   check_P_notebookCompare_reconstructedGamma5NotClifford=true
   check_P_notebookCompare_reconstructedGammaForm=true
   check_P_notebookCompare_eLaztCell1096=true
   check_P_notebookCompare_couplingSetsCell1089=true
   check_P_notebookCompare_relabelCell1111=true
   check_P_notebookCompare_cell1137Reproduced16of16=true
   check_P_notebookCompare_correctVsStoredDifferOnlyByQ=true
   check_P_notebookCompare_qOnlyInYZ0to7=true
   check_P_EMT_anticommutatorsAreThreeGammaProducts=true
   check_P_EMT_OmegaPartIsMinusQuarterPsibarAPsi=true
   check_P_EMT_symmetric=true
   check_P_EMT_homogeneous_rhoOffShell=true
   check_P_EMT_homogeneous_LsOffShell=true
   check_P_EMT_homogeneous_pressuresOffShell=true
   check_P_EMT_homogeneous_KEH_equals_minusK0=true
   check_P_EMT_T44equals_mSplusU_zeroMode=true
   check_P_EMT_homogeneous_onShell_K4plusK0_equals_MeffS=true
   check_P_EMT_reductionSolvesDiracEquation=true
   check_P_EMT_homogeneous_frozenInX4=true
   check_P_EMT_homogeneous_a4Independent=true
   check_P_EMT_homogeneous_conservationOnShell=true
   check_P_EMT_homogeneous_conservationFailsOffShell=true
   check_P_EMT_x0x4EvolutionEquationIsEL=true
   check_P_EMT_conservationOnShellX0X4Sector=true
   check_P_EMT_conservationFailsOffShellX0X4Sector=true
   check_P_EMT_homogeneous_offDiagonalTransverseFromA=true
   check_P_modes_dispersion=true
   check_P_modes_spectrumPlusMinusE8each=true
   check_P_modes_exactReduction=true
   check_P_modes_kqNonzeroNotSeparable=true
   check_P_modes_localWKBDispersion=true
   check_P_modes_localHermitianIffQZero=true
   check_P_modes_instabilityOnset=true
   check_P_einstein_ricciScalar=true
   check_P_einstein_GmixedClosedForms=true
   check_P_einstein_offDiagonalZero=true
   check_P_einstein_pointCheck=true
   check_P_einstein_notebookCell584=true
   check_P_einstein_notebookCell583=true
   check_P_einstein_R44=true
   check_P_einstein_requiredSource=true
   check_P_einstein_rhoRequiredNegative=true
   check_P_einstein_energyConditionForms=true
   check_P_source_transversePressuresEqualForEveryX0X4State=true
   check_P_source_einsteinTransverseDifferenceIs2H2a4pp=true
   check_P_source_realKDiagonalIsC1OverSPlusC2OverS2=true
   check_P_source_realKPlaneWaveCannotSource=true
   check_P_source_x0IndependentStateSolvesDiracExactly=true
   check_P_source_x0IndependentDiagonalOnShell=true
   check_P_source_x0IndependentOffDiagonalAre15Bilinears=true
   check_P_source_x0IndependentSourceConditions=true
   check_P_source_x0IndependentConstruction=true
   check_P_source_x0IndependentExactExamples=true
   check_P_source_x0IndependentNormalizableRealKNot=true
   check_P_quant_Bproperties=true
   check_P_quant_anticommutatorMatrix=true
   check_P_quant_momentum=true
   check_P_quant_hamiltonianHasNoTimeDerivatives=true
   check_P_quant_hamiltonianDensityClosedForm=true
   check_P_quant_heisenbergReproducesEL=true
   check_P_quant_goodSectorHermitian=true
   check_P_quant_extraTimeMomentaNonHermitian=true
   check_P_quant_singleParticleOperatorMatchesEvolution=true
   check_P_quant_gamma8MapsMtoMinusM=true
   check_P_quant_gamma8LagrangianSign=true
   check_P_a4linear_values=true
   check_P_a4linear_isotropicWhenA4ppZero=true
   check_P_a4linear_cell150AlternativesRhoNegative=true
   check_P_internal_noException=true
   ```

3. 41 measurement lines `measurement_<name>=<value>`, in the order storedOutputsSource, exactnessMethod, notebookNonOutputCellCount, notebookCellNumbering, notebookCitedCellLabels, notebookSessionEvidence, metricDiagonalSigns, detG, specDiscrepancy_detG, christoffelNonzeroCount, christoffelNonzeroCountMuLeNu, omegaLowNonzeroCount, omegaMixedSymmetricPairs, notebookContraction_DmuGammaNu_nonzeroPairs, notebookContraction_DmuGammaNu_nonzeroEntries, notebookContraction_DmuGammaNu_pairs, notebookContraction_sample_D1gamma4, notebookContraction_closedForms, divergenceIdentity_lhs, x0x4BlocksCorrectEquations, notebookSourceCellsMatched, cell1058LiteralThisKernel_curvedGammaStatus, cell1058LiteralThisKernel_version, notebookEla_minus_cliffordRebuild_nonzeroComponents, cell1058LiteralThisKernel_reproducesStoredEla, notebookEla_qVectorRows_sign_partner, reconstructedGammaX5Squared, reconstructedGammaX5_anticommutesWithGammaX6, reconstructedGammaX5_anticommutesWithGammaX0, reconstructedGammaX5_form, qTermSignsByYZ, EMT_anticommutatorNonzeroPairsMuLeNu, EMT_homogeneous_offDiagonalNonzeroOffShell, contractNote_homogeneousReduction, contractNote_TiiHomogeneous, modes_hLocalMinusAdjoint, condensateWronskian_1_invS_invS2, source_x0Independent_Meff, source_x0Independent_examples, contractNote_condensateSource, contractNote_gamma8Map. Some values are long single lines. Examples: `measurement_notebookNonOutputCellCount=1279`, `measurement_christoffelNonzeroCount=37`, `measurement_omegaLowNonzeroCount=24`, `measurement_cell1058LiteralThisKernel_curvedGammaStatus={correct, correct, correct, correct, correct, uniform e^{-a4} (wrong), uniform e^{-a4} (wrong), uniform e^{-a4} (wrong)}`, `measurement_qTermSignsByYZ={{0, 1}, {1, -1}, {2, -1}, {3, 1}, {4, 1}, {5, -1}, {6, -1}, {7, 1}, {8, 0}, {9, 0}, {10, 0}, {11, 0}, {12, 0}, {13, 0}, {14, 0}, {15, 0}}`.

4. The five final lines, the verdict:

   ```
   check_count=126
   failed_check_count=0
   elapsed_seconds=<N>
   report=<full path of the report>
   components=<full path of the components file>
   ```

   `<N>` is the computing time in whole seconds (57 to 133 in the verification runs of 2026-10-02 and 2026-10-07, depending on the load of the machine). The two paths are printed in full, with the separators of your operating system; with the usage line of Part 3.3 on Windows they end in `\artifacts\dirac16complex\primordial-field\wolfram-primordial-report.json` and `\artifacts\dirac16complex\primordial-field\primordial-components.json`, with the scratch path in `\build\primordial-check\wolfram-primordial-report.json` and `\build\primordial-check\primordial-components.json`.

The **exit code is 0**. It is 1 if at least one check is not `true` (the run then also prints `  CHECK FAILED: <name>` lines, indented by two spaces, among the progress lines), and 1 after every `ERROR:` line (Part 3.4). Since the fix of 2026-10-07 the script cannot report success without checks: it stops with an `ERROR:` line and exit code 1 if the package file is missing or `D16PRun` does not return its checks, measurements and components, it counts every check whose value is not exactly `true` as failed, and it exits with 0 only if there is at least one check and none failed. A complete run has `check_count=126`; compare it with 126 as well.

The printed `check_` and `measurement_` lines are the same entries as the report's `checks` and `measurements`, in the same order. Apart from the clock times, `<N>` and the two paths, the printed lines were identical in every verification run (Part 6).

### 4.2 The two output files

Both files written at the given place must be byte-identical to the committed ones (how to compare: Part 3.3):

* the report: 13638 bytes, 190 lines, sha256 `f8731e0eaba15a0fa05f4e3193dd9b2a7f3311a0f995d05352e5a2486d230bd3`;
* the components file: 191740 bytes, 6981 lines, sha256 `a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52`.

To count the true and false checks in a report (replace the path by the report you want to inspect):

Windows PowerShell:

```
$r = "build/primordial-check/wolfram-primordial-report.json"
"true: " + (Select-String -Path $r -Pattern '"P_[A-Za-z0-9_]+":true').Count
"false: " + (Select-String -Path $r -Pattern '"P_[A-Za-z0-9_]+":false').Count
```

macOS and Linux:

```
grep -cE '"P_[A-Za-z0-9_]+":true' build/primordial-check/wolfram-primordial-report.json
grep -cE '"P_[A-Za-z0-9_]+":false' build/primordial-check/wolfram-primordial-report.json
```

They must print 126 true and 0 false.

### 4.3 Run time and memory

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GiB RAM, Windows 11 Pro for Workstations, build 10.0.26200 on 2026-10-02 and 10.0.26300 on 2026-10-07, Wolfram 15.0.1, WolframScript 1.14.0) while other jobs were running on it (on 2026-10-07 between about 5 and 20 Wolfram kernels of other jobs). Runs F1 to F5 used the fixed script of 2026-10-07; the other runs used the script before the fix, which performs exactly the same computation (Part 6):

| Run | Date, script | Wall-clock time of `wolframscript` | Printed `elapsed_seconds` | Peak working set of the kernel |
| --- | --- | --- | --- | --- |
| 1 (fresh clone) | 2026-10-02, before the fix | 61.0 s | 57 | 328.3 MiB |
| 2 (fresh clone) | 2026-10-02, before the fix | 77.3 s | 71 | 328.5 MiB |
| 3 (fresh clone, private temporary folders) | 2026-10-02, before the fix | 92.5 s | 88 | 328.2 MiB |
| 4 (second run in the clone of run 1) | 2026-10-02, before the fix | 88.8 s | 83 | 328.4 MiB |
| 5a (fresh clone, PowerShell: usage line) | 2026-10-02, before the fix | 69.3 s | 65 | not measured |
| 5b (same clone, PowerShell: scratch path) | 2026-10-02, before the fix | 63.3 s | 59 | not measured |
| 6a (fresh clone, Git Bash: usage line) | 2026-10-02, before the fix | 75.6 s | 67 | not measured |
| 6b (same clone, Git Bash: scratch path) | 2026-10-02, before the fix | 62.9 s | 58 | not measured |
| R3 (fresh clone, private temporary folders) | 2026-10-02, before the fix | 74.2 s | 70 | not measured |
| R4 (fresh clone, private temporary folders) | 2026-10-02, before the fix | 78.2 s | 74 | not measured |
| V1 (fresh clone) | 2026-10-07, before the fix | 74.3 s | 68 | 328 MiB |
| V2 (fresh clone, private `TEMP`/`TMP`) | 2026-10-07, before the fix | 114.2 s | 108 | 327.8 MiB |
| V3 (clone of V1, PowerShell: scratch path) | 2026-10-07, before the fix | 102.1 s | 97 | not measured |
| A to D (independent review, four runs in two fresh clones) | 2026-10-07, before the fix | 112.1 to 132.8 s | 104 to 123 | 327.7 MiB (as reported by the review) |
| F1 (fresh clone, usage line) | 2026-10-07, fixed script | 117.3 s | 110 | 327.6 MiB |
| F2 (fresh clone, usage line, private `TEMP`/`TMP`) | 2026-10-07, fixed script | 118.4 s | 111 | 327.4 MiB |
| F3 (clone of F1, PowerShell: scratch path) | 2026-10-07, fixed script | 142.5 s (all commands of Parts 3.3 and 4.2) | 133 | not measured |
| F4 (clone of F2, Git Bash: scratch path) | 2026-10-07, fixed script | 143.8 s (all commands of Parts 3.3 and 4.2) | 133 | not measured |
| F5 (fourth clone, `--` before the report path) | 2026-10-07, fixed script | 129.3 s | 122 | 327.7 MiB |

The computation runs in one kernel; the longest steps are `P_EMT` (27 to 68 s), `P_source` (15 to 35 s) and `P_quant` (10 to 20 s), measured from the progress line of the step to the next progress line. The spread of the run times comes from the varying load of the other jobs on the machine; the outputs are the same in every run (apart from the script's own sha256 in the report, which changed with the fix). Under heavy load a normal run took up to about two and a half minutes; that is not a failure. WolframScript itself needs about 17 MiB (16.5 MiB measured in V2, F1 and F2). The Stage-2 document (its Section 18.1) reports about 39 s, measured on 2026-09-25 without the parallel load; on a machine without other load expect from well under one minute to about one minute; slower computers need longer. The failure cases of Part 3.4 end after 4 to 6 s (missing or damaged package) or after the whole computation, 73 to 142 s (missing notebook or fixture, output that cannot be written; 73 s on 2026-10-02, 110 to 142 s on 2026-10-07).

### 4.4 Comparing with a different Wolfram version or operating system

The report contains the version string of the kernel that ran it, `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, in the two measurements `notebookSessionEvidence` (its end, "verifier kernel: ...") and `cell1058LiteralThisKernel_version`. With another version, or with 15.0.1 on macOS or Linux, these two lines of the report differ, so the report's sha256 differs; other lines may differ too if that version simplifies or prints expressions differently (for example `cell1058LiteralThisKernel_curvedGammaStatus`, which records how this kernel re-executes the notebook's cell 1058). The components file contains no version string. In that case check instead that (a) the exit code is 0, (b) `check_count=126` and `failed_check_count=0`, (c) the counts of Part 4.2 are 126 and 0, and (d) only the expected lines differ: in PowerShell `Compare-Object (Get-Content artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json) (Get-Content build/primordial-check/wolfram-primordial-report.json)`, on macOS and Linux `diff artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json build/primordial-check/wolfram-primordial-report.json` (and the same for `primordial-components.json`). With 15.0.1 on Windows there are no differing lines. Note that the test `tests/test_d16c_primordial_publication.py` requires the version string of the verification machine in the committed report; do not commit a report made with another version.

## 5. Side effects

**Files in the repository.** The script writes at most two files, the report at the path you give and `primordial-components.json` next to it.

* With the usage line of Part 3.3 it **overwrites the two committed files** `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` and `artifacts/dirac16complex/primordial-field/primordial-components.json` (their modification times change). With Wolfram 15.0.1 on Windows the new bytes are identical, so `git status --porcelain --untracked-files=all` prints nothing afterwards (measured after every verification run).
* With the recommended scratch path it creates the folder `build/primordial-check/` (and `build/` if missing) with the two files in it; `build/` is ignored by git, so `git status` stays empty. The saved screen output `build/primordial-check/stdout.txt` is created by your terminal, not by the script.
* The folder of the report path is created at the very start, before the package is looked for; so even a run that stops at once leaves that folder behind (empty). With the usage line the folder exists already.
* In the failure cases of Part 3.4: a missing or damaged package and an interrupted run write no output file; an output that cannot be written leaves that file unchanged and writes no file after it; a missing notebook or fixture still writes both files, with failed checks (with the usage line they replace the committed files; restore them as below).
* No other file in the repository is created, changed or deleted. In particular the author's notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` and `algebra-fixture.json` are only read (their sha256 values were unchanged after every run). The script writes no log file.

**Temporary files.**

* The system temporary folder is not used: in runs 3, R3, R4, V2 and F2 (Part 6) `TEMP` and `TMP` pointed at empty private folders, which were still empty during and after the runs.
* On Windows, WolframScript keeps a spool file for the kernel's printed output in the folder `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary`, normally `C:\Users\<your user name>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`. The file is named `tmp_` followed by 10 random letters and digits and holds the lines printed so far. It is created at the start of the run and **deleted when the run ends normally**, also when the run ends with an `ERROR:` line or with failed checks (observed in runs 4, R4, V2, F1 and F2 and in the failure measurement M1: for example F1's file `tmp_4wyz4wTGSL`, whose first line `[20:38:02] zero-test sanity` was the first line of F1's own output, and F2's file `tmp_JWy2N1K7GV`, first line `[20:38:05] zero-test sanity`; both were gone after the runs).
* **An interrupted run leaves its spool file behind.** In measurement M7 the run was stopped by force after 30 s (`taskkill /PID <process number of wolframscript> /T /F`, which also ended the kernel); its spool file `tmp_VPNpqqhcz2` (331 bytes, the 14 progress lines printed until then) was still in the folder afterwards (it was then deleted by hand). A run stopped with Ctrl+C or by closing its window can leave its file in the same way (not measured separately). Such leftover files are small and harmless. To remove them, first make sure that no WolframScript run and no other Wolfram program is running (a running WolframScript needs its own file), then in PowerShell: `Remove-Item "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary\tmp_*"`. On the verification machine this folder held 86 such files at the start of the verification on 2026-10-07, far more than the 5 Wolfram kernels then running, so most of them were left behind by runs of other jobs that had not ended normally.
* WolframScript finds the spool folder itself and **ignores the `LOCALAPPDATA` environment variable**: in run 3 and in the re-verification runs R2, R3 and R4 `LOCALAPPDATA` pointed at an empty private folder, which stayed empty, while the spool file was created in the real folder (R2 and R4, where the real folder was watched; confirmed by the independent review of 2026-10-07). So changing `LOCALAPPDATA` neither moves nor prevents this file.
* WolframScript also rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` at every start (238 bytes on the verification machine; only the modification time changes, the content stays the same).
* On macOS and Linux WolframScript keeps the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process (`wolfram.exe` on the verification machine, started with `-runfirst Unprotect[$EvaluationEnvironment];$EvaluationEnvironment="Script";Protect[$EvaluationEnvironment]; -linkmode Connect -linkname <name>_shm -mathlink`, so it talks to WolframScript through shared memory; command line read in V1, V2, F1, F2 and M1), which runs for the whole computation and exits at the end. WolframScript usually also starts a short-lived second `wolfram.exe` process at the start of the run (seen in runs 2, 3, 4, V1, V2, F1, F2, F5 and M4 to M7; peak 50 to 68 MiB where it could be measured): in runs 2 and V2 its command line was `wolfram.exe -wlbanner -licenseinfo`, i.e. it only reads the licence information; in the other runs it had exited before its command line could be read. It belongs to WolframScript, not to this set. The package itself starts no further kernels (it contains no parallel computation) and no external programs. After the forced stop of M7 (with `/T`, the whole process tree) no process of the run was left. If you ever stop a run in another way, check that no `wolfram.exe` of it keeps running (Task Manager on Windows; `ps aux | grep -i wolfram` on macOS and Linux) and end it.

**Network.** None expected and none observed. The script and the package contain no network calls (no `URL...` function, no web `Import`, no external programs), and no connection to another computer was ever observed. What was seen of the processes started by `wolframscript` differs between runs: in runs 2, 3 and 4 (polled every half second), V2 (every 0.4 s) and F1 and F2 (about every 2 s) the kernel owned one pair of connected TCP sockets on 127.0.0.1, both ends owned by the same `wolfram.exe` (in V2, F1 and F2 Windows also listed one socket of that `wolfram.exe` in the state "Bound" on the local port of that pair, with no remote address); in the independent review of 2026-10-07 (one run polled about every 1.5 s) and in the run F5 and the failure measurements M1 and M4 to M7 (polled about every 2 to 3 s) no TCP or UDP socket of these processes was seen at all. 127.0.0.1 is the local loopback address, which never leaves the computer. (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of this script.)

**Restoring the committed state.** If the committed files were overwritten with different bytes (for example by another Wolfram version, or by a run with a missing notebook or fixture, Part 3.4), restore them with

```
git checkout -- artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json artifacts/dirac16complex/primordial-field/primordial-components.json
```

and remove the scratch folder with `Remove-Item -Recurse -Force build/primordial-check` (PowerShell) or `rm -rf build/primordial-check` (macOS, Linux). Afterwards `git status --porcelain` must print nothing. A spool file left by an interrupted run is outside the repository; remove it as described under "Temporary files" above.

## 6. Verification record

### 6.1 Verification of the fixed script (2026-10-07)

* Date: 2026-10-07 (runs F1 to F5, failure measurements M1 to M8, between 20:37 and 20:55 local time). The set was first verified on 2026-10-02, with the script as it was before the fix (Section 6.3).
* Commit verified: `b8a695d1faa7abe43b4b51eb666f25d250420fb7` of https://github.com/once-ere/Dirac_claude.git, branch `main` (the local working copy and the remote were at this commit when the clones were made). The script and the committed report were last changed by the fix, commit `b980c803830541395603016613b2a48b454ca872` (Section 6.2); the package and the components file have not changed since commit `fbec4d76da9b728f6443cd2d9486d6192d5fd7d0` (2026-09-25), the fixture since `78b4a5f` and the notebook since `30b9ab3` (both 2026-09-25).
* Environment: Windows 11 Pro for Workstations 10.0.26300 (build 26300), Intel Core Ultra 9 275HX (24 cores), 191 GiB RAM; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026) (product "Wolfram", kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`), WolframScript 1.14.0; PowerShell 7.6.6; Git Bash (GNU bash 5.2.37); Python 3.14.5 (only to inspect the JSON files). Professional Wolfram licence without a kernel limit; between about 5 and 20 Wolfram kernels of other jobs ran at the same time.
* Clones: four fresh clones, P-clone1 to P-clone4, each made with `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder (three of them at the same time, in 34 s). In all four the program files, the inputs and the committed outputs had the sha256 values, line counts and byte counts of Part 2, and `git status --porcelain --untracked-files=all` was empty. No uncommitted file was copied in (the set needs only committed files); this provenance file was read from outside the clones.
* Runs, all from the clone root:

| Run | Clone | Command | Exit code | `check_count` / `failed_check_count` | Report | Components file | `git status --porcelain --untracked-files=all` afterwards |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | P-clone1 (fresh) | exactly the usage line, started from PowerShell 7.6.6 through .NET with both standard streams redirected to files; processes, sockets and the spool folder polled | 0 | 126 / 0 | byte-identical to the committed file (`cmp` with `git show HEAD:<file>`), sha256 `f8731e0e...` | byte-identical, sha256 `a5d8caa8...` | empty |
| F2 | P-clone2 (fresh) | as F1, with `TEMP` and `TMP` pointing at an empty private folder | 0 | 126 / 0 | byte-identical to the committed file and to F1 | byte-identical to the committed file and to F1 | empty |
| F3 | P-clone1, after F1 | the PowerShell commands of Part 3.3 (scratch path, `foreach` comparison), the counts of Part 4.2 and `git status --porcelain`, copied as written into a script file and run with PowerShell 7.6.6 | `exit code: 0` | 126 / 0 | the loop printed `wolfram-primordial-report.json identical f8731e0eaba15a0fa05f4e3193dd9b2a7f3311a0f995d05352e5a2486d230bd3` | the loop printed `primordial-components.json identical a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` | empty (the counts printed `true: 126` and `false: 0`) |
| F4 | P-clone2, after F2 | the macOS/Linux commands of Part 3.3 (with `sha256sum`) and of Part 4.2 and `git status --porcelain`, copied as written into a script file and run with Git Bash | `exit code: 0` | 126 / 0 | `cmp` printed `identical`; `sha256sum` printed the value of Part 2 | `cmp` printed `identical`; `sha256sum` as in Part 2 | empty (the counts printed 126 and 0) |
| F5 | P-clone4, after M5 and M7 (restored, `git status` empty) | `wolframscript -file scripts/verify_dirac16complex_primordial.wls -- build/dashdash/wolfram-primordial-report.json` | 0 | 126 / 0 | written into `build/dashdash/`, sha256 `f8731e0e...` | written into `build/dashdash/`, sha256 `a5d8caa8...` | empty |

* Byte identity: in all five runs both outputs were byte-identical to the committed files, and therefore identical between the runs.
* Check counts: 126 checks, 126 true, `failed_check_count=0` in every run; 41 measurements.
* Printed output: 192 lines on standard output with CRLF line ends and an empty error stream (F1, F2, F5; F3 and F4 saved the 192 lines in `stdout.txt`). After removing the clock times, `done in <N> s`, `elapsed_seconds` and the two path lines, the standard output of F1, F2, F3, F4 and F5 was identical line for line. The 126 check lines and the order of the 41 measurement names are exactly the lists of Part 4.1, and the example values quoted in Parts 1 and 4.1 were printed as quoted (for example `measurement_notebookNonOutputCellCount=1279`, `measurement_christoffelNonzeroCount=37`, `measurement_omegaLowNonzeroCount=24`, `measurement_cell1058LiteralThisKernel_version=15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`).
* Side effects (F1, F2): the private `TEMP`/`TMP` folder of F2 stayed empty; the spool files of F1 and F2 were deleted at the end of the runs (Part 5); processes `wolframscript.exe` (peak 16.5 MiB), the kernel `wolfram.exe` (peak 327.6 and 327.4 MiB) and the short-lived second `wolfram.exe`; TCP sockets only on 127.0.0.1, no UDP socket (Part 5); `WolframScript.conf` 238 bytes.
* Failure measurements with the fixed script (scratch output paths unless stated; afterwards every clone was restored, `git status` empty, all sha256 values as in Part 2):
  * M1 (P-clone3): package moved out of the clone, the usage line, started and observed like F1. Exit code 1 after 4.2 s; one line `ERROR: package not found: <clone>\wolfram\Dirac16ComplexPrimordial.wl`; empty error stream; the committed outputs were not touched (modification time unchanged, `git status` listed only the moved package).
  * M2 (P-clone3): the same with the scratch path `build/nopkg/wolfram-primordial-report.json` in PowerShell: exit code 1 after 5.8 s, the same single line; the folder `build/nopkg` was created and stayed empty.
  * M3 (P-clone3): the package replaced by an empty file: exit code 1 after 5.0 s; one line ``ERROR: Dirac16ComplexPrimordial`D16PRun did not return an Association with checks, measurements and components (the package did not load or did not run)``; empty error stream; the folder `build/emptypkg` created and empty.
  * M4 (P-clone3): notebook moved out: exit code 1, 134.5 s wall clock (`elapsed_seconds=126`); 253 lines on standard output, empty error stream; `Get::noopen` for the notebook after the progress line `loading notebook (read only)`, then the messages `Part::partd` (3 times), `StringRiffle::list` (3), `StringJoin::string` (3), `General::stop` (4), `Table::iterb` (2), `ConnectedComponents::graph` (2), `Part::partw` (3), and `FileHash::noopen` for the notebook after the progress line `done in <N> s`; 17 lines `  CHECK FAILED: <name>` (indented by two spaces; the names are 13 of the 16 checks `P_notebookCompare_...`, all except `commutingQ1DropsOutCliffordGammas`, `reconstructedGamma5NotClifford` and `reconstructedGammaForm`, and `P_metric_notebookCell1060Det`, `P_spinconn_notebookCell501OmegaMuIJEqualsMixedOmega`, `P_einstein_notebookCell584` and `P_einstein_notebookCell583`); `check_count=126`, `failed_check_count=17`; both output files written.
  * M5 (P-clone4): `algebra-fixture.json` moved out: exit code 1, 140.9 s (`elapsed_seconds=130`); 198 lines, empty error stream; `Import::nffil` for the fixture after the progress line `fixture`, `  CHECK FAILED: P_fixture_gammasMatchCommittedFixture`, `  CHECK FAILED: P_fixture_CAndChiralityMatch`, `FileHash::noopen` for the fixture after the progress line `done in <N> s`; `check_count=126`, `failed_check_count=2`; both output files written.
  * M6 (P-clone3): the report path `build/ro/wolfram-primordial-report.json` pointing at an existing read-only file: exit code 1, 142.2 s (`elapsed_seconds=131`); 21 lines: the 20 progress lines and `ERROR: could not write <clone>\build\ro\wolfram-primordial-report.json`; empty error stream; the read-only file kept its old content and no components file was written.
  * M7 (P-clone4): the usage line, stopped by force after 30 s with `taskkill /PID <wolframscript> /T /F`: 14 progress lines (up to `P_EMT`), then the end of both processes (exit code 1, given by `taskkill`), 34.8 s; no process of the run was left; the committed outputs were not touched (modification time unchanged, `git status` empty); the spool file `tmp_VPNpqqhcz2` with the 14 lines remained in the spool folder (Part 5) and was then deleted by hand.
  * M8 (P-clone3): M5 repeated, to inspect the files it writes: exit code 1 after 110.1 s (`elapsed_seconds=104`); Python's `json.load` read the report with 124 true and 2 false checks, 41 measurements and `ToLowerCase[$Failed]` as the fixture's `sourceSha256` entry, and the components file as an object with 17 keys.
* Statements about other files, checked at commit `b8a695d`: the `/build/` rule of `.gitignore` (its line 284); the retry logic of the Stage-2 gate, `scripts/verify_stage2_primordial_field.ps1` lines 116 to 152 (`$maximumAttempts = 3`, retry only after a nonzero exit code and only if the log matches `licen[cs]e|password|kernel limit|maximum number of|too many kernels|could not (launch|start|connect)`, 30 s pause) and `scripts/verify_stage2_primordial_field.sh` lines 133 to 169 (the same pattern with `grep -Ei`, `maximum_attempts=3`); the gate runs this set as its step `stage2-01-wolfram-primordial` (`.ps1` lines 173 to 174, `.sh` lines 188 to 190); `tests/test_d16c_primordial_publication.py` requires the kernel version string in the report (its line 461); `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` Section 18.4 lists the script's new sha256 `f49606ba...`.

### 6.2 The fix of 2026-10-07

The earlier verification (Section 6.3) found that the script could report success without checks: with the package file missing it printed `check_count=1` and `failed_check_count=0`, exited with code 0 and wrote two files that were valid JSON with meaningless content. The project lead fixed the script in commit `b980c803830541395603016613b2a48b454ca872` ("Fix the primordial verifier's false-success path", 2026-10-07). The diff of `scripts/verify_dirac16complex_primordial.wls` (82 to 91 lines, 4994 to 5754 bytes, sha256 `919928048f45fba3800c7755f9a8e26d6f8a1c4d3444f975c6d644c591d7f59e` to `f49606ba044ace6eb0ebc5e7661a7823f826416f234fce756acd9a2ccab958f9`):

* before `Get[modulePath]`: `If[! FileExistsQ[modulePath], Print["ERROR: package not found: ", modulePath]; Exit[1]]`;
* after `D16PRun`: an `ERROR:` line and `Exit[1]` unless the result is an Association whose `checks` (non-empty), `measurements` and `components` are Associations;
* in `writeJSON`: `Quiet[OpenWrite[...]]`, and an `ERROR: could not write <path>` line and `Exit[1]` if no output stream was opened;
* `failed = Count[Values[checks], v_ /; ! TrueQ[v]]` instead of `Count[Values[checks], False]`, so every check that is not exactly `true` counts as failed;
* two more lines in the header comment.

The same commit updated the committed report in exactly one line, the script's entry in `sourceSha256` (report sha256 `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` to `f8731e0eaba15a0fa05f4e3193dd9b2a7f3311a0f995d05352e5a2486d230bd3`, size unchanged), the sha256 in Section 18.4 of `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` (with its rebuilt `.tex` and `.pdf` and the entry in `provenance/pdf-specifications.json`) and the hash pins of `tests/test_d16c_primordial_publication.py`. The package, the components file and the computation did not change. This verification (Section 6.1) confirmed the fix from fresh clones: normal runs are byte-identical, and the false-success case now ends with an `ERROR:` line and exit code 1 without writing anything (M1, M2). This provenance file was then updated for the fixed script (Parts 2 to 6; the row of Part 3.4 that described the false success was replaced by the measured `ERROR:` cases). No file of the set was changed by this verification.

### 6.3 Earlier verifications, before the fix

These runs used the script before the fix (sha256 `919928048f45fba3800c7755f9a8e26d6f8a1c4d3444f975c6d644c591d7f59e`) with the same package, inputs and components file as Part 2; the committed report was then `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2`, which differs from today's only in the script's `sourceSha256` entry.

* 2026-10-02, commits `45d47343ae480df46e06689ed822b8f9a88a8030` (runs 1 and 4) and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (runs 2, 3, 5 and 6; it differs from 45d4734 only in `Revision/tests/test_pair_creation_proofs_publication.py`); Windows 11 Pro for Workstations 10.0.26200, otherwise the environment of Section 6.1. Runs 1 to 3 in fresh clones (run 3 with `TEMP`, `TMP` and `LOCALAPPDATA` pointing at empty private folders), run 4 a second run in the clone of run 1, runs 5 and 6 in fresh clones following this file literally in PowerShell (5a usage line, 5b scratch path) and in Git Bash (6a, 6b). Every run: exit code 0, 126 / 0, both outputs byte-identical to the then committed files, 192 lines on standard output, empty error stream, `git status` empty; the standard output of runs 2 to 6 was identical after masking times and paths. Further measurements: with the `#!` first line, `--` and the report path reach the script (a one-line test script printed `{"sub/argtest2.wls", "--", "a.json"}`; without the `#!` line, `{"argtest.wls"}`); a missing notebook gave 17 and a missing fixture 2 failed checks, both after 73 s.
* Re-verification after an independent review of this file, 2026-10-02, commit `c2b33cc`, three more fresh clones: R1 the package missing (the false success described in Section 6.2, exit code 0 after 5.5 s); R2 a marker test showing that WolframScript writes its spool file in the real profile folder and ignores `LOCALAPPDATA`; R3 and R4 full runs with private `TEMP`, `TMP` and `LOCALAPPDATA` (exit code 0, 126 / 0, byte-identical, private folders empty; R4's spool file `tmp_I7bApxbCQ3` was deleted at the end of the run); R5 the scratch-path command without its first line (PowerShell 7.6.6: `OpenError: ... Could not find a part of the path ...`, Windows PowerShell 5.1.26100: `out-file : Could not find a part of the path ...`, Git Bash: `No such file or directory`, each back in under 0.3 s without starting wolframscript).
* 2026-10-07, commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, Windows build 26300: V1 and V2 in fresh clones (exit code 0, 126 / 0, both outputs byte-identical; V2 with private `TEMP`/`TMP`, its spool file `tmp_hUt1heuKvx` deleted at the end, TCP sockets only on 127.0.0.1), V3 the PowerShell commands of Part 3.3 in the clone of V1 (`identical` for both files), V4 the false success measured again (exit code 0 after 4.5 s).
* Independent review of this file, 2026-10-07, commits `565c9b0` and `22fc7af` (the files of the set identical to `a4c5eda`), two fresh clones: runs A to D (the usage line, the PowerShell commands and the macOS/Linux commands in Git Bash), each exit code 0, 126 / 0, both outputs byte-identical; the failure cases re-measured. Its five findings were handled in this update:
  1. the run-time ranges were narrower than the times measured under heavy load (up to 132.8 s wall clock, `elapsed_seconds` up to 123, `P_EMT` up to 66 s, missing inputs up to 111 s): confirmed (this verification measured up to 143.8 s wall clock, `elapsed_seconds` 133 and `P_EMT` 68 s, and 140.9 s for a missing input); FIXED, the ranges of Parts 3.3, 3.4, 4.1 and 4.3 now include all measured values;
  2. the loopback socket pair of Part 5 could not be reproduced (no socket seen): confirmed that it is not seen in every run (also not in F5 and M1, M4 to M7 here), but it was seen again in F1 and F2; FIXED, Part 5 now states what was observed in which runs;
  3. the row for a missing notebook or fixture named only the first message: confirmed by M4 and M5; FIXED, the row now lists the other messages, the line counts, the two-space indent of the `CHECK FAILED` lines and that the outputs are still written;
  4. the open discrepancy said that the false-success weakness awaited a decision, while the lead had decided to fix it: confirmed, and the fix has since landed (Section 6.2); FIXED, this file now describes the fixed script;
  5. the line range of the retry logic in `scripts/verify_stage2_primordial_field.sh` ended one line early: confirmed, `run_step` closes at line 169; FIXED (Section 6.1).

### 6.4 Open discrepancies

* No scientific discrepancy: all 126 checks are true, and both outputs are reproduced byte for byte.
* No open execution defect in this set.
* Outside this set, at commit `b8a695d` the following files still quote the sha256 of the report from before the fix, `a0164273df62f2e1...`, instead of `f8731e0eaba15a0f...`: `provenance/textbook/chapters/19-reproducing-everything.md` (its line 286) and the assembled `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (line 14328) with its `.tex` (line 15925); `notebooks/dirac16complex_dark_sector.PROVENANCE.md` (line 158); `provenance/wolframscript/verify_dirac16complex00.PROVENANCE.md` (line 88; its uncommitted working copy, being updated by the provenance work for that set, already gives the new value); and the committed Stage-5 outputs `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` (line 1790) and `dirac16complex00-theory.json` (line 15). `scripts/verify_dirac16complex00.wls` hashes the current report when it runs (its line 44), so, read from its code, a re-run of the Stage-5 set would now write the new sha256 into those two files and no longer reproduce them byte for byte until they are regenerated and committed. These files belong to other sets and documents and were not changed here; they are reported for the owners of those files.
* Status of that list on 2026-10-08: the Stage-5 outputs `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and `dirac16complex00-theory.json` were regenerated and now record `f8731e0eaba15a0f...` (part 6.6 of `provenance/wolframscript/verify_dirac16complex00.PROVENANCE.md`; a re-run reproduces them byte for byte); that file and `notebooks/dirac16complex_dark_sector.PROVENANCE.md` give the new value. The original textbook (`provenance/DIRAC16COMPLEX_TEXTBOOK.md`, `.tex`, `.pdf` and `provenance/textbook/chapters/`) keeps the earlier value in its sample output of the Stage-2 gate (recorded on 2026-09-30): the user ordered on 2026-10-02 that this textbook be preserved and never modified (`HANDOFF.md`, section 0.4e); its successor is the textbook "Universes in Pairs" in `Revision/textbook/`. A student who runs the gate today sees `stage2_sha256=f8731e0eaba15a0f...` for this report.
