# Execution provenance: the Stage-2 primordial-field verifier (WolframScript)

Set: `scripts/verify_dirac16complex_primordial.wls` with `wolfram/Dirac16ComplexPrimordial.wl` (old Stage 2, "dirac16complex in the primordial pair-creation gravitational field").

Verified on 2026-10-02 at commits `45d47343ae480df46e06689ed822b8f9a88a8030` and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and verified again on 2026-10-07 at commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670` of https://github.com/once-ere/Dirac_claude.git (the files of this set, its inputs and its committed outputs are identical in all three commits; they have not changed since commit `fbec4d7` of 2026-09-25). Result: the set **EXECUTES OK** (exit code 0, 126 of 126 checks true, `failed_check_count=0`) and **reproduces both committed output files byte for byte** in every run. On 2026-10-02: two runs in two fresh clones as required, a third fresh clone with private temporary folders, a re-run in an already used clone, and two further fresh clones in which this file was followed literally (PowerShell and Git Bash, two runs each); after an independent review of this file, three more fresh clones re-verified the corrected statements (two more full runs, also byte-identical, and the failure cases). On 2026-10-07: two runs in two new fresh clones, a run of the PowerShell commands of this file in an already used clone, and the failure case of the first row of Part 3.4 measured again. One weakness of the error handling was found and is reported, not fixed (Part 3.4, first row, and Part 6). The details are in Part 6.

This file is written for a student who has never used Wolfram software. Everything you need to run the set is in this file; you do not have to read any other file first.

## 1. What this set is and what it computes

**The physics in plain words.** The project studies a field called "dirac16complex": a field with 16 complex components (a "spinor") that lives in an 8-dimensional space-time with 4 space-like and 4 time-like directions. The coordinates are called x0, ..., x7; x4 plays the role of the time in which the field evolves, and x5, x6, x7 are three extra times. The flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). The field values are not ordinary numbers but *Grassmann* numbers: two of them anticommute (theta1 theta2 = -theta2 theta1), as they must for a fermion field.

Stage 1 of the project wrote down how this field behaves in an *arbitrary* gravitational field. Stage 2, checked by this set, repeats those calculations for **one fixed gravitational field**: the "primordial" (pair-creation) field of the author's Mathematica notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`, whose metric is called MatrixMetric44 there. With the abbreviations z = 6 H x0 (0 < z < pi/2), t = H x4, s = sin z and an arbitrary function a4(t), the metric is diagonal,

```
g = diag( cot(z)^2,  s^(1/3) e^(2 a4)  (x1, x2, x3),  -1,  -s^(1/3) e^(-2 a4)  (x5, x6, x7) ),
```

with 4 positive and 4 negative entries. Ordinary 3-space (x1, x2, x3) and the three extra times (x5, x6, x7) are scaled in opposite directions by a4: when 3-space inflates, the extra times deflate.

**What the computer does.** The script loads the package and calls its function `D16PRun`, which computes everything with **exact symbolic algebra** in the Wolfram Language; it never uses floating-point numbers to decide anything. It

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
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/00-how-to-read.md`, `01-mathematical-toolkit.md`, `04-curved-space.md` ("wolfram-primordial-report.json 126 of 126 true"), `09-primordial-field.md`, `18-open-problems.md`, `19-reproducing-everything.md` (it quotes the sha256 prefixes `a0164273df62f2e1` of the report and `a5d8caa8cb226082` of the components file) and `20-glossary-and-check-index.md`.
* `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` (and `.tex`, `.pdf`), the Stage-1 document, which uses the notebook-cell numbering of the package's function `loadNotebookCells`.
* `README.md`, which names the Stage-2 gate (below).
* `notebooks/dirac16complex_dark_sector.PROVENANCE.md`, the provenance file of the dark-sector Jupyter notebook, which lists the report (190 lines, 13638 bytes, its sha256) among the inputs of that notebook.

**Programs that read its outputs or load its package.** `scripts/check_dirac16complex_primordial.py` reads `primordial-components.json` (its check `P_EL_agreesWithWolfram`) and records that file's sha256 in `artifacts/dirac16complex/primordial-field/python-primordial-report.json`; `tests/test_d16c_primordial.py` reads the components file; `tests/test_d16c_primordial_publication.py` reads both outputs and compares the numbers, TeX strings, hashes and the kernel version quoted in the Stage-2 document with them; the Stage-2 gate `scripts/verify_stage2_primordial_field.ps1` and `.sh` runs exactly the command of this set as its step `stage2-01-wolfram-primordial`; `wolfram/Dirac16Complex00.wl` (Stage 5) loads this package and cites the report's checks, requiring that the report's `sourceSha256` entry of the package equals the package's current sha256; `scripts/verify_dirac16complex00.wls` records the sha256 of the package and of the report in `artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json` and `dirac16complex00-theory.json`; the Jupyter notebook `notebooks/dirac16complex_dark_sector.ipynb` loads the report in its "verification gauntlet" (Section 11 of that notebook, the 21st of its 23 cells). This is why both outputs must be reproduced byte for byte.

## 2. Files

All files below are stored with LF line endings; the repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values are the same on Windows, macOS and Linux.

**Program files.**

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `scripts/verify_dirac16complex_primordial.wls` | the script you run: loads the package, calls `D16PRun`, writes the two JSON files, prints the verdict, sets the exit code | 82 | 4994 | `919928048f45fba3800c7755f9a8e26d6f8a1c4d3444f975c6d644c591d7f59e` |
| `wolfram/Dirac16ComplexPrimordial.wl` | the package (context ``Dirac16ComplexPrimordial` ``): gamma matrices, exact ring and zero tests, TeX and Python printers, the primordial field, the notebook reader and all checks; entry point `D16PRun[repoRoot]` | 1224 | 101130 | `0b95682601ace6343a89ad8eaf0f4896d071015041f15cccbeb3beac193d81a1` |

**Inputs.** The package reads two data files, and the script computes the sha256 of all four files below and writes them into the report as `sourceSha256`:

| File | How it is read | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `Import[..., "RawJSON"]`: the committed Stage-1 gamma matrices, C and chirality | 18440 | 213133 | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` |
| `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` | `Get[...]`: the author's notebook, read as an expression (never opened in a front end, never written) | 471194 | 24489589 | `5ee5cb2a95146136ee65636a4aef174f303b6c41da130d2c57e4684f9c8ff69f` |
| `scripts/verify_dirac16complex_primordial.wls` | hashed only | 82 | 4994 | `919928048f45fba3800c7755f9a8e26d6f8a1c4d3444f975c6d644c591d7f59e` |
| `wolfram/Dirac16ComplexPrimordial.wl` | `Get[...]` (the package) and hashed | 1224 | 101130 | `0b95682601ace6343a89ad8eaf0f4896d071015041f15cccbeb3beac193d81a1` |

Nothing else is read: no other package, no environment variable, nothing from the network. The script finds the repository root from its own location (the folder above `scripts`), so all inputs are found from any current folder.

**Outputs.** Two files, written into the folder of the report path you give (the folder is created if it does not exist). A relative report path is taken relative to the repository root, not to the current folder; a path starting with `/` or with a drive letter such as `C:` is used as it is. Without a path argument the script uses the committed path below. With the usage line of Part 3.3 the outputs are the committed files:

| File | Lines | Bytes | sha256 (committed) |
| --- | --- | --- | --- |
| `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` | 190 | 13638 | `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` |
| `artifacts/dirac16complex/primordial-field/primordial-components.json` | 6981 | 191740 | `a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` |

The components file always gets the name `primordial-components.json` and is written next to the report, whatever name you give the report. Both files are pure ASCII JSON with LF line endings, indented with tabs, ending with a newline. The report's top-level keys are `schemaVersion` (1), `producer`, `checks` (126 entries, all `true`), `measurements` (41 entries) and `sourceSha256` (the four sha256 values above). The output paths do not appear inside the files, so a report written to another folder is byte-identical to the committed one.

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

The clone occupies about 670 MB on disk (measured on 2026-10-07 at commit `a4c5eda`; it was about 520 MB on 2026-10-02 and grows as the repository grows). Every command below is typed in this folder, the *repository root* (the folder that contains `scripts`, `wolfram` and `artifacts`). (Instead of git you may download the ZIP archive from the GitHub page, button "Code", "Download ZIP", and unpack it; then `git status` and `git checkout` below are not available, and you compare files with the sha256 commands of Part 3.3 instead.)

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

(The first line creates the folder for the saved screen output `stdout.txt`; without `> build/primordial-check/stdout.txt` the 192 lines are printed on the screen instead, the first 20 of them while the computation runs.) The run takes about one to two minutes on the verification machine (Part 4.3); with the redirection nothing appears on the screen until it has finished. Do not interrupt it.

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

and, to see the sha256 values, `shasum -a 256 build/primordial-check/*.json` on macOS or `sha256sum build/primordial-check/*.json` on Linux. You must see `identical` for both files, and the sha256 values must be `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` for the report and `a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` for the components file.

**About `--` before the report path.** Pass the report path directly after the script name, as above. With WolframScript 1.14.0, `wolframscript -file s.wls -- r.json` drops `--` and everything after it for a script file that does not start with a `#!` line; this script starts with `#!/usr/bin/env wolframscript`, and for it the verification measured that `--` and the path do arrive and that the script removes the `--`, so both forms wrote to the same scratch folder. Do not rely on that: if the path is ever dropped, the script writes to the committed paths instead.

### 3.4 If it fails

| What you see | Cause and fix |
| --- | --- |
| After only a few seconds (3 to 6 s), 19 lines (six of them empty) and nothing on the error stream, in this order: `Get::noopen: Cannot open ...Dirac16ComplexPrimordial.wl.`, `FileHash::noopen: Cannot open ...Dirac16ComplexPrimordial.wl.` (the package cannot be hashed), `Join::incpt: Incompatible elements in Join[...] cannot be joined.` (one very long line), `Keys::invrl: The argument ...[checks] is not a valid Association or a list of rules.`, a line like ``check_Dirac16ComplexPrimordial`D16PRun[...][checks]=false``, `Keys::invrl` again (for `[measurements]`), a line like ``measurement_Dirac16ComplexPrimordial`D16PRun[...][measurements]=...``, `Values::invrl`, and then `check_count=1`, `failed_check_count=0`, `elapsed_seconds=0`, the `report=` and `components=` lines and **exit code 0** | The package file `wolfram/Dirac16ComplexPrimordial.wl` is missing or unreadable. **Despite exit code 0 this run is invalid.** The two files it wrote are *syntactically valid JSON with meaningless content*: in the report, `checks` and `measurements` are single strings (the unevaluated text ``Dirac16ComplexPrimordial`D16PRun["<your repository folder>"]["checks"]`` and the same with `"measurements"`) instead of 126 results and 41 measurements, and the package's `sourceSha256` entry is `ToLowerCase[$Failed]`; the components file is one single JSON string, the unevaluated Wolfram expression that begins with `Join[` (instead of an object with 17 keys). A JSON parser (a JSON viewer, Python's `json.load`) accepts both files without complaint, so parsing them does **not** reveal the failure. (With the usage line of Part 3.3 they replaced the committed files.) This is a known weakness of the script (Part 6): always check that the printed `check_count` is 126; the counts of Part 4.2 also reveal it (they print 0 true and 0 false for such a report instead of 126 and 0). Restore the files with `git checkout -- wolfram/Dirac16ComplexPrimordial.wl artifacts/dirac16complex/primordial-field/` (or clone again) and run again. |
| PowerShell: `The term 'wolframscript' is not recognized`; macOS/Linux: `command not found: wolframscript` | WolframScript is not installed or not on the PATH. Open a new terminal after the installation. On Windows the program is in `C:\Program Files\Wolfram Research\WolframScript\`; add that folder to the PATH or install again. On macOS and Linux install WolframScript separately (Part 3.1, step 2). |
| A message containing "licence"/"license", "password", "activate", "kernel limit", "too many kernels", "maximum number of" or "could not launch/start/connect" | The kernel is not activated, or your licence allows fewer kernels at the same time than are running. Run `wolframscript -activate` again; close other Wolfram programs and notebooks; wait 30 seconds and run again. (The project's Stage-2 gate, `scripts/verify_stage2_primordial_field.ps1` and its twin `.sh`, makes up to three attempts of this step, i.e. retries it up to twice after 30 seconds, when the step fails with a nonzero exit code and its log contains licence/license, password, kernel limit, maximum number of, too many kernels or could not launch/start/connect; "activate" is not in its list, so the gate does not retry for that message alone.) |
| Lines `CHECK FAILED: <name>` during the run, `failed_check_count` larger than 0, exit code 1 | A check is false: the computed mathematics differs from the committed result. Do not edit anything to make it pass. Compare the sha256 values of the program files and inputs with Part 2 (`Get-FileHash -Algorithm SHA256 <file>` in PowerShell, `shasum -a 256 <file>` on macOS, `sha256sum <file>` on Linux); if they differ, run `git checkout -- <file>` or clone again. If they are the committed ones, report the failing check names and your Wolfram version. |
| A line `INTERNAL ERROR: ...`, `check_P_internal_noException=false`, fewer than 126 checks, exit code 1 | The package stopped with an internal error (for example an untested Wolfram version that simplifies an expression differently); the checks computed up to that point are still printed and written. (This case is read from the code; it did not occur in the verification.) Report the line and your Wolfram version. |
| `Get::noopen` naming `Pair_Creation_of_...-Nash.nb` with 17 `CHECK FAILED` lines, or `Import::nffil` naming `algebra-fixture.json` with 2 `CHECK FAILED` lines (`P_fixture_gammasMatchCommittedFixture`, `P_fixture_CAndChiralityMatch`); `failed_check_count` 17 or 2; exit code 1 | An input file is missing: the repository is incomplete. Restore it with `git checkout -- <file>` or clone again. (Both cases were measured.) |
| The new report (and possibly the components file) differs from the committed one, but `check_count=126` and `failed_check_count=0` | Most likely another Wolfram version or operating system: the report contains the kernel's version string (Part 4.4). |
| PowerShell 7: `OpenError: ... Could not find a part of the path '...\build\primordial-check\stdout.txt'.` (Windows PowerShell 5.1: `out-file : Could not find a part of the path ...stdout.txt'.`); macOS/Linux: `bash: build/primordial-check/stdout.txt: No such file or directory` (zsh on macOS: `zsh: no such file or directory: build/primordial-check/stdout.txt`); the prompt returns at once | The folder `build/primordial-check` for the saved screen output does not exist yet, so the shell could not open `stdout.txt`. **wolframscript was not started at all** (nothing was computed and no file was written; in PowerShell `"exit code: $LASTEXITCODE"` then prints no number or an old one, in bash/zsh `echo "exit code: $?"` prints 1). Run the `New-Item` line (PowerShell) or the `mkdir -p` line (macOS/Linux) first, then repeat the `wolframscript` line. |
| It runs much longer than 2 minutes | Slower or busier computers need longer; the computation is exact and runs in one kernel. Let it finish. The progress lines (Part 4.1) show where it is; the longest step is `P_EMT` (27 to 57 seconds on the verification machine, depending on its load). If you stop it with Ctrl+C, the output files are not written and the old ones are left unchanged (they are written only after the computation). |
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

   `<N>` is the computing time in whole seconds (57 to 108 in the verification runs of 2026-10-02 and 2026-10-07). The two paths are printed in full, with the separators of your operating system; with the usage line of Part 3.3 on Windows they end in `\artifacts\dirac16complex\primordial-field\wolfram-primordial-report.json` and `\artifacts\dirac16complex\primordial-field\primordial-components.json`, with the scratch path in `\build\primordial-check\wolfram-primordial-report.json` and `\build\primordial-check\primordial-components.json`.

The **exit code is 0**. It is 1 if at least one check is false (the run then also prints `CHECK FAILED: <name>` lines among the progress lines). Exit code 0 is valid only together with `check_count=126` and `failed_check_count=0` (Part 3.4, first row).

The printed `check_` and `measurement_` lines are the same entries as the report's `checks` and `measurements`, in the same order. Apart from the clock times, `<N>` and the two paths, the printed lines were identical in every verification run (Part 6).

### 4.2 The two output files

Both files written at the given place must be byte-identical to the committed ones (how to compare: Part 3.3):

* the report: 13638 bytes, 190 lines, sha256 `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2`;
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

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GiB RAM, Windows 11 Pro for Workstations, build 10.0.26200 on 2026-10-02 and 10.0.26300 on 2026-10-07, Wolfram 15.0.1, WolframScript 1.14.0), while up to about fifteen Wolfram kernels of other jobs were running at the same time:

| Run | Wall-clock time of `wolframscript` | Printed `elapsed_seconds` | Peak working set of the kernel |
| --- | --- | --- | --- |
| 1 (fresh clone) | 61.0 s | 57 | 328.3 MiB |
| 2 (fresh clone) | 77.3 s | 71 | 328.5 MiB |
| 3 (fresh clone, private temporary folders) | 92.5 s | 88 | 328.2 MiB |
| 4 (second run in the clone of run 1) | 88.8 s | 83 | 328.4 MiB |
| 5a (fresh clone, this file followed literally in PowerShell: usage line) | 69.3 s | 65 | not measured |
| 5b (same clone, PowerShell: scratch path) | 63.3 s | 59 | not measured |
| 6a (fresh clone, this file followed literally in Git Bash: usage line) | 75.6 s | 67 | not measured |
| 6b (same clone, Git Bash: scratch path) | 62.9 s | 58 | not measured |
| R3 (re-verification, fresh clone, private temporary folders) | 74.2 s | 70 | not measured |
| R4 (re-verification, fresh clone, private temporary folders) | 78.2 s | 74 | not measured |
| V1 (2026-10-07, fresh clone) | 74.3 s | 68 | 328 MiB |
| V2 (2026-10-07, fresh clone, private `TEMP`/`TMP`, about fifteen other kernels running) | 114.2 s | 108 | 327.8 MiB |
| V3 (2026-10-07, clone of V1, PowerShell commands of Part 3.3: scratch path) | 102.1 s | 97 | not measured |

Runs 1 to R4 are those of 2026-10-02, V1 to V3 those of 2026-10-07 (Part 6). The computation runs in one kernel; the longest steps are `P_EMT` (27 to 57 s), `P_source` (15 to 31 s) and `P_quant` (10 to 17 s), and the spread of the run times most likely comes from the varying load of the other jobs on the machine (the outputs are the same in every run). WolframScript itself needs about 17 MiB (16.5 MiB measured in V2). The Stage-2 document (its Section 18.1) reports about 39 s, measured on 2026-09-25 without the parallel load; on a machine without other load expect well under one minute to about one minute; slower computers need longer.

### 4.4 Comparing with a different Wolfram version or operating system

The report contains the version string of the kernel that ran it, `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, in the two measurements `notebookSessionEvidence` (its end, "verifier kernel: ...") and `cell1058LiteralThisKernel_version`. With another version, or with 15.0.1 on macOS or Linux, these two lines of the report differ, so the report's sha256 differs; other lines may differ too if that version simplifies or prints expressions differently (for example `cell1058LiteralThisKernel_curvedGammaStatus`, which records how this kernel re-executes the notebook's cell 1058). The components file contains no version string. In that case check instead that (a) the exit code is 0, (b) `check_count=126` and `failed_check_count=0`, (c) the counts of Part 4.2 are 126 and 0, and (d) only the expected lines differ: in PowerShell `Compare-Object (Get-Content artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json) (Get-Content build/primordial-check/wolfram-primordial-report.json)`, on macOS and Linux `diff artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json build/primordial-check/wolfram-primordial-report.json` (and the same for `primordial-components.json`). With 15.0.1 on Windows there are no differing lines. Note that the test `tests/test_d16c_primordial_publication.py` requires the version string of the verification machine in the committed report; do not commit a report made with another version.

## 5. Side effects

**Files in the repository.** The script writes exactly two files, the report at the path you give and `primordial-components.json` next to it.

* With the usage line of Part 3.3 it **overwrites the two committed files** `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` and `artifacts/dirac16complex/primordial-field/primordial-components.json` (their modification times change). With Wolfram 15.0.1 on Windows the new bytes are identical, so `git status --porcelain --untracked-files=all` prints nothing afterwards (measured after every verification run).
* With the recommended scratch path it creates the folder `build/primordial-check/` (and `build/` if missing) with the two files in it; `build/` is ignored by git, so `git status` stays empty. The saved screen output `build/primordial-check/stdout.txt` is created by your terminal, not by the script.
* No other file in the repository is created, changed or deleted. In particular the author's notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` and `algebra-fixture.json` are only read (their sha256 values were unchanged after every run). The script writes no log file. The two output files are written only after the whole computation has finished, so an interrupted run leaves the old files unchanged.

**Temporary files.** None in the system temporary folder: verification run 3, the re-verification runs R3 and R4 and run V2 (Part 6) pointed `TEMP` and `TMP` at empty private folders, which were still empty during and after the runs. On Windows WolframScript itself keeps a spool file for the kernel's printed output, `C:\Users\<your user name>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary\tmp_<10 random characters>` (the `Wolfram\WolframScript\WolframScriptTemporary` folder inside your user profile's Local AppData folder, normally the folder that `%LOCALAPPDATA%` names), for the duration of the run, and deletes it when the run ends (observed in run 4: the file holding these 192 lines existed from the first progress line to the end and was then gone; the same in re-verification run R4). WolframScript finds this folder itself and **ignores the `LOCALAPPDATA` environment variable**: in run 3 and in the re-verification runs R2, R3 and R4, `LOCALAPPDATA` pointed at an empty private folder, which stayed empty, and in R2 and R4, where the real folder was watched for it, the spool file was still created in the real profile folder `C:\Users\nsh\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary` (run R4: the file `tmp_I7bApxbCQ3`, whose first line `[07:08:42] zero-test sanity` was also the first line of R4's own output; it was gone after the run; run V2 on 2026-10-07: the file `tmp_hUt1heuKvx`, first line `[15:21:56] zero-test sanity`, the first line of V2's own output, gone after the run). So changing `LOCALAPPDATA` neither moves nor prevents this file. WolframScript also rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` at every start (238 bytes on the verification machine; only the modification time changed, the content stayed the same). On macOS and Linux WolframScript keeps the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process (`wolfram.exe` on the verification machine, started with `-runfirst Unprotect[$EvaluationEnvironment];$EvaluationEnvironment="Script";Protect[$EvaluationEnvironment]; -linkmode Connect -linkname <name>_shm -mathlink`, so it talks to WolframScript through shared memory; command line read in V1 and V2), which runs for the whole computation and exits at the end. In runs 2, 3, 4, V1 and V2 WolframScript also started a short-lived second `wolfram.exe` process (peak 50 to 68 MiB where it could be measured): in runs 2 and V2 its command line was `wolfram.exe -wlbanner -licenseinfo`, i.e. it only reads the licence information; in runs 3, 4 and V1 it had already exited before its command line could be read. It belongs to WolframScript, not to this set. The package itself starts no further kernels (it contains no parallel computation) and no external programs.

**Network.** None. The script and the package contain no network calls (no `URL...` function, no web `Import`, no external programs). While polling every half second during runs 2, 3 and 4 (and every 0.4 s during V2), the only TCP sockets of the processes started by `wolframscript` were one pair of connected sockets on 127.0.0.1, both ends owned by `wolfram.exe` (in V2 Windows also listed one socket of `wolfram.exe` in the state "Bound" on the local port 55561 of that pair, with no remote address) (127.0.0.1 is the local loopback address, which never leaves the computer); there was no connection to another computer. (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of this script.)

**Restoring the committed state.** If the committed files were overwritten with different bytes (for example by another Wolfram version, or by a run with a missing package, Part 3.4), restore them with

```
git checkout -- artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json artifacts/dirac16complex/primordial-field/primordial-components.json
```

and remove the scratch folder with `Remove-Item -Recurse -Force build/primordial-check` (PowerShell) or `rm -rf build/primordial-check` (macOS, Linux). Afterwards `git status --porcelain` must print nothing.

## 6. Verification record

* Dates: 2026-10-02 (runs 1 to 6 and the re-verification R1 to R5) and 2026-10-07 (runs V1 to V3, measurement V4).
* Commits verified: `45d47343ae480df46e06689ed822b8f9a88a8030` (run 1 and run 4) and `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (runs 2, 3, 5 and 6) of https://github.com/once-ere/Dirac_claude.git, branch `main`; c2b33cc differs from 45d4734 only in `Revision/tests/test_pair_creation_proofs_publication.py`. In every clone the program files, the inputs and the committed outputs had the sha256 values of Part 2. None of them has changed since commit `fbec4d76da9b728f6443cd2d9486d6192d5fd7d0` (2026-09-25, "Stage 2: dirac16complex in the primordial pair-creation field"). No uncommitted file was copied into the clones for the runs (the set needs only committed files); in runs 5 and 6 this provenance file was read from outside the clone.
* Environment: Windows 11 Pro for Workstations 10.0.26200 (build 26200), Intel Core Ultra 9 275HX (24 cores), 191 GiB RAM; Wolfram 15.0.1 for Microsoft Windows (64-bit) (product "Wolfram", kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`), WolframScript 1.14.0; PowerShell 7.6.6, Git Bash (GNU bash 5.2.37, git 2.51.2.windows.1). Professional Wolfram licence without a kernel limit; other Wolfram jobs ran on the machine at the same time.
* Fresh clones: each run except run 4 used its own `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder.
* Commands, all from the clone root:
  * runs 1 to 4, exactly the usage line of the script header: `wolframscript -file scripts/verify_dirac16complex_primordial.wls artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json`, started from PowerShell with the standard streams redirected to files; run 3 with `TEMP`, `TMP` and `LOCALAPPDATA` pointing at empty private folders (WolframScript ignores `LOCALAPPDATA`, Part 5), the other runs with the normal environment; run 4 in the clone of run 1, whose outputs run 1 had already rewritten;
  * run 5: the PowerShell commands of Parts 3.1 (`wolframscript -code '$Version'`), 3.2, 3.3 and 4.2, typed exactly as written: 5a the usage line followed by `git status --porcelain`, 5b the scratch-path variant, the comparison loop and the counts; only additions: the screen output of 5a was saved to a file outside the clone, and the clock was read before and after each run;
  * run 6: the same for the macOS/Linux commands in Git Bash (with `sha256sum`), 6a and 6b.

| Run | Clone, commit | Exit code | `check_count` / `failed_check_count` | Report sha256 | Components sha256 | `git status --porcelain --untracked-files=all` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | fresh, 45d4734 | 0 | 126 / 0 | `a0164273...` identical | `a5d8caa8...` identical | empty |
| 2 | fresh, c2b33cc | 0 | 126 / 0 | identical | identical | empty |
| 3 | fresh, c2b33cc | 0 | 126 / 0 | identical | identical | empty |
| 4 | clone of run 1 | 0 | 126 / 0 | identical | identical | empty |
| 5a, 5b | fresh, c2b33cc | 0, 0 | 126 / 0, 126 / 0 | identical (5b: the `foreach` loop of Part 3.3 printed `identical`) | identical | empty after 5a and after 5b |
| 6a, 6b | fresh, c2b33cc | 0, 0 | 126 / 0, 126 / 0 | identical (6b: `cmp` printed `identical`, `sha256sum` as in Part 2) | identical | empty after 6a and after 6b |

* Byte identity: in every run both outputs were byte-identical to the committed files (`cmp` and sha256), and therefore also identical between the runs.
* Check counts: 126 checks, 126 true, `failed_check_count=0` in every run; 41 measurements.
* Printed output: 192 lines on standard output, empty error stream, in every run. After removing the clock times, `done in <N> s`, `elapsed_seconds` and the two path lines, the standard output of runs 2, 3, 4, 5a, 5b, 6a and 6b was identical line for line. (Run 1's capture used an event-based reader that does not preserve the order of lines; its set of lines was the same.)
* Additional measurements: (a) with the package file renamed (in a scratch clone, scratch output path) the script printed the messages `Get::noopen`, `FileHash::noopen`, `Join::incpt`, `Keys::invrl`, a ``check_...D16PRun[...][checks]=false`` line, `Keys::invrl`, a ``measurement_...D16PRun[...][measurements]=...`` line and `Values::invrl`, then `check_count=1`, `failed_check_count=0`, wrote two files that are syntactically valid JSON with meaningless content (the report's `checks` and `measurements` are strings, its `sourceSha256` entry of the package is `ToLowerCase[$Failed]`, the components file is a single JSON string), and **exited with code 0** after 3 s (re-measured in the re-verification below, with the usage line: 5.5 s); (b) `wolframscript -file scripts/verify_dirac16complex_primordial.wls -- build/dashdash/wolfram-primordial-report.json` wrote both files into `build/dashdash/` and left the committed files untouched (exit code 0, 126/0), while a one-line test script printing `$ScriptCommandLine` received no arguments after `--` without a `#!` first line (`{"argtest.wls"}`) and received them with the first line `#!/usr/bin/env wolframscript` (`{"sub/argtest2.wls", "--", "a.json"}`) (Part 3.3); (c) with the notebook file renamed (scratch output path) the script printed `Get::noopen` for the notebook, 17 `CHECK FAILED` lines (every check that compares with a stored notebook output), `check_count=126`, `failed_check_count=17` and exited with code 1 after 73 s; (d) with `algebra-fixture.json` renamed the script printed `Import::nffil`, `CHECK FAILED: P_fixture_gammasMatchCommittedFixture` and `CHECK FAILED: P_fixture_CAndChiralityMatch`, `failed_check_count=2`, and exited with code 1 after 73 s. Every scratch clone was restored afterwards (`git status` empty, all sha256 values as in Part 2).
* Re-verification after an independent review of this file (2026-10-02, commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, three further fresh clones R-clone1, R-clone2 and R-clone3 made with `git clone https://github.com/once-ere/Dirac_claude.git`, no uncommitted file copied in). The review found five inaccuracies in the text of this file; all five were confirmed (four by measurement, the one about the Stage-2 gate by reading the gate's code) and corrected, and no file of the set was changed:
  * R1 (R-clone1, PowerShell 7.6.6): package `wolfram/Dirac16ComplexPrimordial.wl` moved out of the clone, then the usage line of Part 3.3. Exit code 0 after 5.5 s; standard output 19 lines (six empty) in this order: `Get::noopen`, `FileHash::noopen`, `Join::incpt`, `Keys::invrl`, ``check_Dirac16ComplexPrimordial`D16PRun[...][checks]=false``, `Keys::invrl`, ``measurement_Dirac16ComplexPrimordial`D16PRun[...][measurements]=...``, `Values::invrl`, `check_count=1`, `failed_check_count=0`, `elapsed_seconds=0`, the `report=` and `components=` lines; error stream empty. Both committed outputs were overwritten (report 1136 bytes, components file 1484 bytes; the sizes depend on the length of the clone's folder path, which is embedded in the content). Python's `json.load` accepted both: the report is an object with the keys `schemaVersion`, `producer`, `checks`, `measurements`, `sourceSha256`, where `checks` is the string ``Dirac16ComplexPrimordial`D16PRun["<clone folder>"]["checks"]``, `measurements` the same with `"measurements"`, and `sourceSha256` maps the package to `ToLowerCase[$Failed]` (the other three sha256 values are correct); the components file is a single JSON string beginning `Join[<|"schemaVersion" -> 1, ...`. The counts of Part 4.2 printed `true: 0` and `false: 0` in PowerShell and 0 and 0 in bash. Restored with `git checkout`; `git status` empty, sha256 values as in Part 2.
  * R2 (PowerShell 7.6.6): a three-line test script that prints a unique marker, waits 12 s and prints a second line, run with `TEMP`, `TMP` and `LOCALAPPDATA` pointing at empty private folders. The marker appeared in the spool file `tmp_ZlgGqrokhJ` in the real `C:\Users\nsh\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary` (the folder that .NET reports as the profile's Local AppData folder), the private folders stayed empty, and the spool file was deleted at the end (exit code 0).
  * R3 (R-clone2) and R4 (R-clone3): the usage line, started from PowerShell 7.6.6 with `TEMP`, `TMP` and `LOCALAPPDATA` pointing at empty private folders, while the real spool folder and the private folders were polled every 0.5 s (R3) and 0.25 s (R4). Both: exit code 0, `check_count=126`, `failed_check_count=0`, 41 measurements, 192 lines on standard output, empty error stream, both outputs byte-identical to the committed files (sha256 as in Part 2), `git status --porcelain --untracked-files=all` empty, no file in any private folder at any poll or afterwards; standard output of R3 and R4 identical after removing the clock times, `done in <N> s`, `elapsed_seconds` and the two path lines. In R4 the spool file of the run, `tmp_I7bApxbCQ3`, was found in the real profile folder (created 2.7 s after the start; first line `[07:08:42] zero-test sanity`, the first line of R4's own output; it was locked against plain reads while the kernel wrote to it and could be read with shared access) and was gone after the run. In R3 the poller could not attribute a spool file because it read files without shared access and kept only the last content; this was corrected for R4.
  * R5 (R-clone1, no `build/` folder): the scratch-path command of Part 3.3 without its first line (`New-Item` / `mkdir -p`). PowerShell 7.6.6: `OpenError: ... Could not find a part of the path '...\build\primordial-check\stdout.txt'.`, `$?` False, `$LASTEXITCODE` empty, back after 0.16 s. Windows PowerShell 5.1.26100: `out-file : Could not find a part of the path '...\build\primordial-check\stdout.txt'.` (DirectoryNotFoundException), `$LASTEXITCODE` empty, back after 0.25 s. Git Bash (GNU bash 5.2.37, run from a script, hence the prefix `/usr/bin/bash: line 25:` instead of the interactive `bash:`): `build/primordial-check/stdout.txt: No such file or directory`, exit code 1, back after 55 ms. In all three cases `build/` did not exist afterwards; the script creates the report folder `build/primordial-check` (script line 24) before it even loads the package, and the shell returned far sooner than WolframScript can start a kernel (a few seconds), so wolframscript was not started. zsh (macOS) was not available on the verification machine; its message `zsh: no such file or directory: ...` in Part 3.4 is its standard form, not a measurement.
  * The Stage-2 gate (finding about Part 3.4, third row) was checked by reading the code: `scripts/verify_stage2_primordial_field.ps1` lines 116 to 152 (`$maximumAttempts = 3`, retry only after a nonzero exit code and only if the log matches `licen[cs]e|password|kernel limit|maximum number of|too many kernels|could not (launch|start|connect)`, 30 s pause) and `scripts/verify_stage2_primordial_field.sh` lines 133 to 164 (the same pattern with `grep -Ei`, `maximum_attempts=3`).
* Second verification on 2026-10-07 (the provenance workflow was interrupted by a session limit and restarted; nothing of the earlier record was taken on trust). Commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670` of https://github.com/once-ere/Dirac_claude.git (branch `main`; the local working copy was clean and equal to the remote). Environment as above except Windows 11 Pro for Workstations 10.0.26300 (build 26300) and Python 3.14.5 (used only to inspect the JSON files); `$Version` of the kernel, as written by the runs: `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. About five (V1) to fifteen (V2) Wolfram kernels of other jobs ran at the same time. Two new fresh clones, V-clone1 and V-clone2, each made with `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder; no uncommitted file was copied in. In both clones the program files, inputs and committed outputs had the sha256 values, line counts and byte counts of Part 2.
  * V1 (V-clone1) and V2 (V-clone2): exactly the usage line of the script header, started from PowerShell 7.6.6 through .NET with both standard streams redirected to files, the started processes polled for their memory; V2 additionally with `TEMP` and `TMP` pointing at an empty private folder, and with the spool folder, the private folder and the TCP sockets of the started processes polled every 0.4 s.
  * V3 (V-clone1, after V1): the PowerShell commands of Part 3.3 (scratch path `build/primordial-check`, the `foreach` comparison loop) and the counts of Part 4.2, copied as written into a script file and run with PowerShell 7.6.6, followed by `git status --porcelain --untracked-files=all`.

| Run | Clone | Exit code | `check_count` / `failed_check_count` | Report | Components file | `git status --porcelain --untracked-files=all` |
| --- | --- | --- | --- | --- | --- | --- |
| V1 | V-clone1 (fresh) | 0 | 126 / 0 | byte-identical to the committed file (`cmp`), sha256 `a0164273...` | byte-identical, sha256 `a5d8caa8...` | empty |
| V2 | V-clone2 (fresh) | 0 | 126 / 0 | byte-identical to the committed file and to V1 | byte-identical to the committed file and to V1 | empty |
| V3 | V-clone1 (used) | 0 | 126 / 0 | the loop printed `identical a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` | the loop printed `identical a5d8caa8cb2260824c29dcdb1ed0e62ec22079c297682939a277a6b98dfa3e52` | empty (the scratch files are in the ignored folder `build/`) |

  * In V1, V2 and V3: 192 lines on standard output with CRLF line ends, empty error stream; 126 checks (counts of Part 4.2: `true: 126`, `false: 0`), 41 measurements; the 126 check lines and the order of the 41 measurement names are exactly the lists of Part 4.1, and the example values quoted in Parts 1 and 4.1 were printed as quoted. After removing the clock times, `done in <N> s`, `elapsed_seconds` and the two path lines, the standard output of V1, V2 and V3 was identical line for line. Both outputs are pure ASCII with LF line ends and a final newline; the report has the five top-level keys of Part 2, the components file the 17 top-level keys of Part 1. So both outputs were byte-identical to the committed files in every run, and identical between the runs.
  * V2 side effects: the private `TEMP`/`TMP` folder stayed empty during and after the run; the WolframScript spool file of the run was `tmp_hUt1heuKvx` in `C:\Users\nsh\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary` (first line `[15:21:56] zero-test sanity`, the first line of V2's own output) and was gone after the run (the other spool files seen there belonged to the other jobs); the processes were `wolframscript.exe` (peak 16.5 MiB), the kernel `wolfram.exe` (peak 327.8 MiB, command line in Part 5) and the short-lived `wolfram.exe -wlbanner -licenseinfo`; TCP sockets only on 127.0.0.1 (Part 5).
  * V4 (V-clone2, after V2): the first row of Part 3.4 measured again, with the package `wolfram/Dirac16ComplexPrimordial.wl` moved out of the clone and the scratch path `build/nopkg/wolfram-primordial-report.json`, run from Git Bash. Exit code 0 after 4.5 s; 19 lines on standard output in the order of Part 3.4 (`Get::noopen`, `FileHash::noopen`, `Join::incpt`, `Keys::invrl`, a ``check_Dirac16ComplexPrimordial`D16PRun[...]`` line, `Keys::invrl`, a ``measurement_Dirac16ComplexPrimordial`D16PRun[...]`` line, `Values::invrl`, `check_count=1`, `failed_check_count=0`, `elapsed_seconds=0`, the two path lines), empty error stream; Python's `json.load` accepted both files (the report's `checks` is a string, its `sourceSha256` entry of the package is `ToLowerCase[$Failed]`, the components file is a single string beginning `Join[<|"schemaVersion" -> 1, "producer"`); the count of `true` checks in that report was 0. The package was moved back and `build/nopkg` removed; `git status` empty, the package's sha256 as in Part 2. The weakness is unchanged (open discrepancy below).
  * Argument passing (Part 3.3) measured again with one-line test scripts that print `$ScriptCommandLine`: `wolframscript -file argtest.wls -- a.json` without a `#!` first line printed `{argtest.wls}`; `wolframscript -file sub/argtest2.wls -- a.json` with the first line `#!/usr/bin/env wolframscript` printed `{sub/argtest2.wls, --, a.json}`, and the same without `--` printed `{sub/argtest2.wls, a.json}`.
  * The statements of Parts 1 to 5 about other files were checked again at commit `a4c5eda`: the documents and programs that cite or read the outputs (Part 1; the dark-sector notebook and its provenance file were added to the lists), the `/build/` rule of `.gitignore` (its line 284), the retry logic of the Stage-2 gate (`scripts/verify_stage2_primordial_field.ps1` lines 116 to 152 and `scripts/verify_stage2_primordial_field.sh` lines 133 to 168; the gate runs this set as its step `stage2-01-wolfram-primordial`, lines 173 to 174 and 188 to 189), and the kernel version string required by `tests/test_d16c_primordial_publication.py` (its line 461). The clone size (about 670 MB) and the run-time statements (Parts 3.3, 3.4, 4.1 and 4.3) were updated to the new measurements.
* Fixes made: none to the set; no file of the set was changed, neither on 2026-10-02 nor on 2026-10-07. On 2026-10-07 only this provenance file was updated (the new verification record, the clone size, the run times, the kernel command line, the dark-sector notebook among the readers of the report). On 2026-10-02 this provenance file was corrected after the review: Part 3.4 (the row for a missing package: the full list of messages and the fact that the outputs are valid JSON with meaningless content; the row for licence messages: the gate makes up to three attempts, i.e. two retries, and its pattern lacks "activate"; the row for a missing `build/primordial-check` folder: the messages of PowerShell 5.1/7, bash and zsh, and that wolframscript is not started), Part 5 (WolframScript ignores `LOCALAPPDATA`), and in Part 6 measurement (a) and the open discrepancy.
* Open discrepancies: no scientific discrepancy. One robustness weakness of the script (an execution defect of its error handling, not of the computation): it does not verify that the package loaded and that `D16PRun` returned an Association before it writes the files and computes the exit code; with a missing or unloadable package it writes outputs that are syntactically valid JSON with meaningless content (the report's `checks` and `measurements` are strings instead of results, its `sourceSha256` entry of the package is `ToLowerCase[$Failed]`, the components file is a single JSON string) and exits with 0 (measurement (a) above, measured again as V4 on 2026-10-07). A JSON parser does not detect this failure; only the printed `check_count` (1 instead of 126) and the counts of Part 4.2 (0 true, 0 false) do, so the student must check `check_count=126`. A guard like the one in `scripts/verify_dirac16complex00.wls` (print a FATAL line and `Exit[2]` without writing) would fix it, but any edit of the script changes its sha256, which the committed report records in `sourceSha256` and the Stage-2 document quotes in its Section 18.4 (checked by `tests/test_d16c_primordial_publication.py`); the committed report would then no longer be reproducible byte for byte, and the report's own sha256 is quoted in the original textbook (`provenance/DIRAC16COMPLEX_TEXTBOOK.md`, chapter 19) and recorded in the Stage-5 files `wolfram-dirac16complex00-report.json` and `dirac16complex00-theory.json`. The fix was therefore not made; it is reported for a decision.
