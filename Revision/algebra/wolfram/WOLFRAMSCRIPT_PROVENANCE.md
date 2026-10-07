# Provenance of the wolframscript set `Revision/algebra/wolfram/` (the gamma matrices of the 4 + 4 dimensional theory)

This file is written for a student who has never used Wolfram or a command line. It says what the set
computes, which files it reads and writes, how to run it from nothing on Windows, macOS or Linux, what
you will see, what the run changes on your computer, and how it was verified on 2026-10-02 and
re-verified on 2026-10-07 (section 6).

## 1. What this set is and what it computes

### 1.1 The set in one sentence

One WolframScript program, `verify_algebra.wls`, loads one Wolfram Language package,
`RevisionAlgebra.wl`, builds the author's eight real 16 x 16 gamma matrices and the matrices made from
them, proves 45 exact statements about them, and writes two files: the matrices
(`Revision/algebra/gammas.json`) and a report of the 45 checks
(`Revision/algebra/reports/wolfram-algebra.json`).

### 1.2 The physics, in plain words

The theory lives in eight dimensions with coordinates x1 ... x8: x1, x2, x3 are ordinary 3-space, x4 is
time, x5, x6, x7 are three extra times that deflate exponentially, and x8 is a hidden direction. A spinor
field (the 16-component field `Psi` of the theory) needs eight "gamma matrices" gamma^(x1), ...,
gamma^(x8) that square to plus or minus the identity and anticommute with one another:

    gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab I16,   eta = diag(+1, +1, +1, -1, -1, -1, -1, +1)

(order x1 ... x8; the four entries +1 belong to the space-like directions x1, x2, x3, x8 and the four
entries -1 to the time-like directions x4, x5, x6, x7: the signature (4, 4)). This rule is called the
Clifford relation. The author built such matrices, called `T16`, in his Mathematica notebook
`Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`. This set does NOT
open that notebook: the author's formulas were re-typed into `RevisionAlgebra.wl` (from the notebook's
input cells In[45], In[46], In[294], In[300], In[301], In[338], In[351], In[370], In[371], In[372]),
and the matrices are rebuilt from them in four steps:

1. 4 x 4 blocks `s4[h]` and `t4[h]` (h = 1, 2, 3) from the permutation sign `Signature[{h, p, q, 4}]`
   and Kronecker deltas;
2. 8 x 8 matrices `sigma`, `tau[A]` and `taubar[A]` (A = 0 ... 7) from the blocks;
3. 16 x 16 matrices `T16[A] = {{0, taubar[A]}, {tau[A], 0}}`;
4. the coordinate map gamma^(x1..x3) = T16[1..3], gamma^(x4) = T16[4], gamma^(x5..x7) = T16[5..7],
   gamma^(x8) = T16[0].

From the gammas it builds:

* `C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)` (the notebook's `sigma16`): the matrix of the Dirac
  adjoint `Psibar = Psi^dagger C`;
* `Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7)` (the notebook's `T16[8]`): the chirality matrix,
  equal to `diag(-I8, I8)`;
* `B = -i C gamma^(x4)`: a Hermitian matrix with `B^2 = I16` and eigenvalues +1 (eight times) and -1
  (eight times);
* the 28 generators `S^ab = (1/4)(gamma^a gamma^b - gamma^b gamma^a)` of the rotations and boosts of
  the (4, 4) space, the Lie algebra of the group Spin(4,4).

A remark on charge conjugation, because the gammas are real. Charge conjugation is a MATRIX map: it acts
as `Psi^c = calC Psibar^T = calC C Psi*` (C is symmetric, `C^T = C`), where `calC` is a 16 x 16 matrix.
The lead check `Revision/lead_checks/charge_conjugation_and_u1.py` (report
`Revision/lead_checks/reports/charge-conjugation-and-u1.json`, 12 of 12 checks pass) solves exactly for
every such matrix that maps solutions of the field equation to solutions and finds exactly two:

* `calC_+ = C` (same mass m), which gives `Psi^c = Psi*`. For a REAL field (`Psi* = Psi`) it reduces to
  the identity, `Psi^c = Psi`: it is no conjugation at all (a real field is its own conjugate and carries
  no U(1) charge).
* `calC_- = Gamma C` (mass reversed, m -> -m), which gives `Psi^c = Gamma Psi*`. For a real field this is
  `Psi -> Gamma Psi` together with `m -> -m`: the nontrivial MATRIX charge conjugation of a real field,
  the map between matter and antimatter. `Gamma` is also the matrix that preserves the anticommutator
  `{Psi, Psi^dagger} = B delta` of the quantised field (`Gamma B^T Gamma^dagger = B`, whereas the
  identity matrix of the `calC_+` type turns `B` into `-B`).

These two matrices are derived and checked by that lead check, not by this set. This set verifies only
the properties of `C` and `Gamma` used there: `C_gamma_C_inverse` (`C gamma^a C^-1 = -(gamma^a)^T`),
`C_squared_identity` (`C^-1 = C`), `Gamma_diag` (`Gamma = diag(-I8, I8)`),
`Gamma_anticommutes_with_gammas` (`{Gamma, gamma^a} = 0`, `Gamma^2 = I16`) and `Gamma_commutes_with_C`
(`[Gamma, C] = 0`). Together they give `calC_-^-1 gamma^a calC_- = +(gamma^a)^T`, the property that
makes `Gamma C` reverse the mass.

### 1.3 How the script proves it

Every check uses exact integer or exact rational arithmetic (the gammas have entries -1, 0, +1; `S^ab`
has entries -1/2, 0, +1/2; `B` has entries 0 and +-i). Nothing is floating point, so a PASS is a proof
for these explicit matrices, not a numerical approximation. Linear-algebra statements (irreducibility)
are decided with `NullSpace` and `MatrixRank` over the rational numbers. The 45 checks, in the order
they are printed:

| # | check | what it establishes |
| --- | --- | --- |
| 1 | `s4_t4_entries_from_Signature_and_deltas` | every entry of s4[h], t4[h] equals the author's formula Signature[{h,p,q,4}] -+ (d_p4 d_qh - d_ph d_q4) |
| 2 | `s4_self_dual_t4_anti_self_dual` | (1/2) eps_pqrs s4_rs = s4 and (1/2) eps_pqrs t4_rs = -t4 |
| 3 | `s4_t4_quaternion_algebras` | {s4[h], s4[k]} = {t4[h], t4[k]} = -2 delta_hk I4, [s4, t4] = 0: two commuting copies of the imaginary quaternions |
| 4 | `sigma8_involution` | sigma^2 = I8, Tr sigma = 0, sigma symmetric |
| 5 | `tau_taubar_Clifford_relation` | tau[A] taubar[B] + tau[B] taubar[A] = 2 eta4488_AB I8 (and the other order) |
| 6 | `tau7_and_sigma_identities` | sigma = tau1 tau2 tau3 = tau4 tau5 tau6 tau7, sigma taubar[A] = (sigma tau[A])^T |
| 7 | `T16_block_form` | T16[A] = {{0, taubar[A]}, {tau[A], 0}} |
| 8 | `coordinate_map` | gamma^(x1..x8) = T16[1, 2, 3, 4, 5, 6, 7, 0] |
| 9 | `eta_in_author_order` | eta = diag(+1,+1,+1,-1,-1,-1,-1,+1) in the order x1..x8 |
| 10 | `Clifford_relation` | {gamma^a, gamma^b} = 2 eta^ab I16 for all 64 pairs |
| 11 | `reality` | every gamma is a real matrix with entries in {-1, 0, 1} |
| 12 | `signed_permutation_matrices` | one nonzero entry (+-1) in each row and column |
| 13 | `symmetry_pattern` | space-like gammas symmetric, time-like gammas antisymmetric |
| 14 | `C_definition` | C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) = T16[0] T16[1] T16[2] T16[3] |
| 15 | `C_real_symmetric` | C is a real (integer) symmetric matrix |
| 16 | `C_squared_identity` | C^2 = I16 |
| 17 | `C_gamma_real_antisymmetric` | C gamma^a is real and antisymmetric for every a |
| 18 | `C_gamma_C_inverse` | C gamma^a C^-1 = -(gamma^a)^T for every a |
| 19 | `Gamma_definition` | Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) = T16[8] |
| 20 | `Gamma_diag` | Gamma = diag(-I8, I8) |
| 21 | `Gamma_anticommutes_with_gammas` | {Gamma, gamma^a} = 0, Gamma^2 = I16 |
| 22 | `Gamma_commutes_with_C` | [Gamma, C] = 0 |
| 23 | `notebook_product_identity` | T16[0] T16[1] ... T16[8] = I16 |
| 24 | `B_definition` | B = -i C gamma^(x4) |
| 25 | `B_Hermitian` | B^dagger = B |
| 26 | `B_squared_identity` | B^2 = I16 |
| 27 | `B_signature_8_8` | eigenvalues of B: +1 (8 times), -1 (8 times), Tr B = 0 |
| 28 | `B_purely_imaginary` | B = i K with K a real antisymmetric integer matrix |
| 29 | `S_antisymmetric_in_ab` | S^ab = -S^ba, S^aa = 0 |
| 30 | `S_half_product` | S^ab = (1/2) gamma^a gamma^b for a != b |
| 31 | `S_real_entries_in_half_integers` | every S^ab is real with entries in {-1/2, 0, 1/2} |
| 32 | `S_gamma_commutator` | [S^ab, gamma^c] = eta^bc gamma^a - eta^ac gamma^b for all 512 triples |
| 33 | `S_Lorentz_algebra` | the S^ab close into the Lie algebra so(4,4) |
| 34 | `S_preserves_C` | S^T C + C S = 0: Psibar Psi = Psi^dagger C Psi is Spin(4,4) invariant |
| 35 | `S_preserves_B_only_off_x4` | S^dagger B + B S = 0 for the 21 generators without x4, and = i C gamma^b (not 0) for the 7 with x4 |
| 36 | `S_commutes_with_Gamma` | [S^ab, Gamma] = 0: every S^ab is block diagonal |
| 37 | `Clifford_basis_spans_full_matrix_algebra` | the 256 ordered products of gammas are linearly independent (span dimension 256 = 16^2) |
| 38 | `even_subalgebra_dimension` | the even products span dimension 128 = 2 x 8^2 |
| 39 | `Pin44_irreducible_commutant_dim_1` | only multiples of I16 commute with all gammas: the 16 components form one irreducible representation of Pin(4,4) |
| 40 | `Spin44_commutant_dim_2_chiral_projectors` | the matrices commuting with all S^ab are spanned by P_L = (I - Gamma)/2 and P_R = (I + Gamma)/2 |
| 41 | `chiral_halves_irreducible` | each 8-component half (rows 1..8 and 9..16) is irreducible under Spin(4,4) |
| 42 | `chiral_halves_inequivalent_intertwiners_0` | no nonzero matrix maps one half onto the other: the two halves are inequivalent |
| 43 | `Spin_Pin_reflection_swaps_halves` | every gamma^a is block off-diagonal: a reflection exchanges the two halves |
| 44 | `fixture_written_deterministically` | the text of gammas.json, generated twice in the same run, is identical; LF only; 76968 characters |
| 45 | `fixture_round_trip` | gammas.json read back and decoded reproduces gamma, C, Gamma, B, S and eta exactly |

### 1.4 Which documents cite its results

* `Revision/SPEC.md`, section 2 (Clifford algebra, Pin(4,4), Spin(4,4)): the binding specification
  that this set fulfils.
* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 ("Wolfram: 45 of
  45 checks pass") and section 16 (Reproduction, first command).
* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 (the report
  and the fixture), section 14 (Check index: 20 checks of this report cited by name, for example
  `Clifford_relation`, `B_signature_8_8`, `Pin44_irreducible_commutant_dim_1`,
  `chiral_halves_inequivalent_intertwiners_0`) and section 16 (Reproduction).
* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): section 9.1 (count table:
  `wolfram-algebra.json` 45 checks, 45 PASS, 0 FAIL) and section 10 (Reproduction, first command).
* The publication tests that re-read the report: `Revision/tests/test_pair_creation_proofs_publication.py`,
  `Revision/tests/test_dirac16complex_field_theory_publication.py`,
  `Revision/tests/test_dirac16complex00_field_theory_publication.py`.
* `Revision/textbook/TEXTBOOK_SPEC.md`, chapters 04 and 05 (sources: `Revision/algebra`), and the
  textbook notebooks under `Revision/textbook/notebooks/` that read `Revision/algebra/gammas.json` (for
  example `04a_t16_from_formulas.ipynb`, `05a_c_gamma_b.ipynb`, `05b_commutants.ipynb`; the textbook was
  still being written on 2026-10-07).
* `provenance/dirac matrices.md` (generated by `provenance/dirac_matrices/build_dirac_matrices_md.py`):
  it evaluates the author's input cells directly from the notebook file and confirms, in its check
  `fixture_Revision_algebra_gammas_json`, that `Revision/algebra/gammas.json` equals the author's
  matrices entry by entry. That is an independent confirmation, at the level of the notebook itself, of
  what this set builds from the re-typed formulas.

The fixture `Revision/algebra/gammas.json` is the reference copy of the gamma matrices. These programs
read it as their input: `Revision/theory/wolfram/verify_field_theory.wls`,
`Revision/theory/wolfram/verify_scope.wls`, `Revision/theory/python/check_field_theory.py` (through
`Revision/theory/python/gammas_io.py`), `Revision/theory/python/check_scope.py`,
`Revision/pairing/wolfram/verify_pairing.wls`, `Revision/pairing/kohn_sham/wolfram/verify_t3.wls`,
`Revision/pairing/kohn_sham/python/check_t3.py`, `Revision/kohn_sham/theory/verify_ks_theory.wls` (it
records the sha256 of `gammas.json` in its report), the Rust solver
`Revision/kohn_sham/solver/src/theory.rs` (it records the sha256 too),
`Revision/field_equations_a4/python/check_field_equations_a4.py` (for the author's T16, next to a gamma
representation of its own), and the lead checks `Revision/lead_checks/emt_divergence_and_spin_connection.py`
and `Revision/lead_checks/charge_conjugation_and_u1.py`.

Not every gamma matrix in `Revision/` comes from this set, on purpose: some Python checkers rebuild the
gammas independently from the author's formulas and confirm that they equal `gammas.json` entry by entry.
`Revision/algebra/python/check_algebra.py` does so and saves its own construction as
`Revision/algebra/reports/python-gammas.json`; `Revision/pairing/python/check_pairing.py` does so too
(check `gammas.equal_wolfram_fixture`). The independent Python copy `python-gammas.json` is read for
comparison by `Revision/theory/python/check_field_theory.py` (check
`gammas_json_equals_python_construction`) and by `Revision/kohn_sham/theory/check_ks_theory.py`, which
uses it as its preferred input and only compares `gammas.json` with it.

## 2. Files

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone` creates).
Line counts are numbers of LF line endings; every file below uses LF line endings only.

### 2.1 The script and the package

| file | role | sha256 | lines | bytes |
| --- | --- | --- | --- | --- |
| `Revision/algebra/wolfram/verify_algebra.wls` | the driver you run; it loads the package, runs the 45 checks, writes the two outputs, prints the verdicts and exits | `99ff3c1fc6e1c7720cd00ef4141a0fc950ba4906d4153770d3ffd6c5840022ff` | 281 | 17599 |
| `Revision/algebra/wolfram/RevisionAlgebra.wl` | the package (context ``RevisionAlgebra` ``): the author's formulas, the exact linear algebra (commutants, intertwiners, span dimension) and the JSON writer and reader | `fd1aaea5edd6c230da859156bf496ee624e3f569475454ef0e1384cb2d29c881` | 260 | 15089 |

The driver above is the version with the write-failure fix of section 6.3 (an output file that cannot
be written now stops the run with exit code 1). It was committed in `3f0a577` on 2026-10-02 at
07:35:37 -0700 and is the driver that was re-verified on 2026-10-07 (section 6.4). The version committed
up to commit `c2b33cc` had sha256 `75b9f95d5fc7c1e748579f798838427401dd23fcd5b3b7ee3159238512b8369a`
(275 lines, 17185 bytes); it computes the same 45 checks and writes byte-identical outputs, and differs
only in what happens when an output cannot be written (section 3.7).

### 2.2 Inputs (read only, never modified)

| input | sha256 | how it is read |
| --- | --- | --- |
| `Revision/algebra/wolfram/RevisionAlgebra.wl` | `fd1aaea5edd6c230da859156bf496ee624e3f569475454ef0e1384cb2d29c881` | `Get` from the folder of the driver (`$InputFileName`), so it is found from any working directory |

There is no other input. The author's notebook is not read (its formulas are re-typed in the package).
The script reads `Revision/algebra/gammas.json` back with `Import[..., "RawJSON"]` for check 45, but only
AFTER it has overwritten that file with its own new text, so the committed content of `gammas.json`
never influences the result (if the file cannot be overwritten, the run stops with exit code 1 before
any check is reported, section 3.7).

### 2.3 Outputs (written on every successful run; LF line endings, UTF-8, no time stamps, deterministic)

| output | content | sha256 of the committed file (and of every verified run) | lines | bytes |
| --- | --- | --- | --- | --- |
| `Revision/algebra/gammas.json` | the fixture: `description`, `producer`, `encoding`, `definitions`, `coordinates`, `notebookFrameIndex`, `eta` (8 numbers), `gamma` (8 matrices 16 x 16), `C`, `Gamma` (16 x 16), `B` (as `{"re": ..., "im": ...}`), `S` (8 x 8 matrices 16 x 16; entries 1/2 written as the string `"1/2"`) | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 |
| `Revision/algebra/reports/wolfram-algebra.json` | the report: `report`, `producer`, `package`, `fixture`, `coordinates`, `summary`, `checks` (45 objects with `name`, `verdict`, `detail`) | `2167774a0bd0a2794fd5999ac485717c0e725f974826b2bb70b5d46d9598a6a3` | 55 | 9295 |

The script also prints to the screen (standard output); nothing is written to standard error.

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, and an internet connection for the installation
  and the download (the script itself needs no network).
* About 800 MB of free disk space for the repository (a fresh clone of commit `a4c5eda` measured 667 MB,
  of which 195 MB is the git history; the repository grows over time) plus the space the Wolfram
  installer asks for.
* About 0.5 GB of free memory (the Wolfram kernel of this script peaked at 398 MiB).
* A Wolfram kernel with WolframScript: either the free Wolfram Engine for Developers or a licensed
  Mathematica / Wolfram desktop installation. The verification used Wolfram 15.0.1 with WolframScript
  1.14.0; older versions were not tested.
* Git, to download the repository. Python, Jupyter and Rust are NOT needed for this set.

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
`2`. If the second asks for activation, do step 4 of option A.

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

The download took 9 to 22 seconds on the verification machine. You are now in the repository root:
the folder that contains the folder `Revision`. Every command below is run from here.

### 3.5 Run the script

Windows PowerShell (forward slashes and backslashes both work):

```powershell
wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
$LASTEXITCODE
```

macOS and Linux:

```bash
wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
echo "exit code: $?"
```

The second line shows the exit code of the run; type it immediately after the first, because it reports
the most recent command. Optional, to measure the run time: in PowerShell
`Measure-Command { wolframscript -file Revision/algebra/wolfram/verify_algebra.wls | Out-Default }`
(the output is shown, then `TotalSeconds`), on macOS and Linux
`time wolframscript -file Revision/algebra/wolfram/verify_algebra.wls`.

### 3.6 Check the result

1. The screen shows exactly 46 lines: 45 lines `PASS  <name>` and the final line, and no other line (no
   empty line, no line containing `::`, which is how Wolfram prints a warning or error message, no line
   beginning with `ERROR`). The last printed line must begin with `45/45 checks passed`, and the exit code
   must be `0`. All three conditions matter: a message line means that something went wrong even if the
   last line reads `45/45` (section 3.7). To let the computer do the counting, run the script once more
   like this. Windows PowerShell:

   ```powershell
   $out = wolframscript -file Revision/algebra/wolfram/verify_algebra.wls
   $LASTEXITCODE
   $out.Count
   $out | Where-Object { $_ -notmatch '^PASS  ' }
   ```

   macOS and Linux (the output is saved in your home folder, outside the repository):

   ```bash
   wolframscript -file Revision/algebra/wolfram/verify_algebra.wls > ~/verify_algebra_run.txt; echo "exit code: $?"
   wc -l < ~/verify_algebra_run.txt
   grep -v '^PASS  ' ~/verify_algebra_run.txt
   ```

   The answers must be `0` (the exit code), `46` (the number of lines) and one single line, the final
   line `45/45 checks passed; time ... s`.
2. The report's summary line. Windows PowerShell:

   ```powershell
   Select-String -Pattern '"summary"' -Path Revision/algebra/reports/wolfram-algebra.json
   ```

   prints `Revision\algebra\reports\wolfram-algebra.json:7:  "summary": {"passed": 45, "failed": 0, "total": 45},`.
   macOS and Linux:

   ```bash
   grep '"summary"' Revision/algebra/reports/wolfram-algebra.json
   ```

   prints `  "summary": {"passed": 45, "failed": 0, "total": 45},`.
3. The two outputs are byte-identical to the committed files. Windows PowerShell:

   ```powershell
   Get-FileHash Revision/algebra/gammas.json, Revision/algebra/reports/wolfram-algebra.json
   git status --porcelain
   ```

   macOS: `shasum -a 256 Revision/algebra/gammas.json Revision/algebra/reports/wolfram-algebra.json`,
   Linux: `sha256sum Revision/algebra/gammas.json Revision/algebra/reports/wolfram-algebra.json`, and on
   both `git status --porcelain`. The hashes must be (PowerShell prints them in capital letters)
   `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` for `gammas.json` and
   `2167774a0bd0a2794fd5999ac485717c0e725f974826b2bb70b5d46d9598a6a3` for `wolfram-algebra.json`, and
   `git status --porcelain` must print nothing at all (an empty answer means that no file of the
   repository differs from the committed version).

### 3.7 What to do if it fails

* `wolframscript : The term 'wolframscript' is not recognized ...` (PowerShell) or
  `wolframscript: command not found` (macOS, Linux): WolframScript is not installed or not on the PATH.
  Install it (section 3.3, option C) and open a NEW terminal. On Windows you can also run it by its full
  path: `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file Revision/algebra/wolfram/verify_algebra.wls`.
* A request to activate, or a message that the kernel is not activated or the licence is invalid: run
  `wolframscript -activate` (option A, step 4).
* The only output is `Failed to open file at path: Revision/algebra/wolfram/verify_algebra.wls`: you are
  not in the repository root. CAUTION: in this case WolframScript still returns exit code 0 (observed
  during the verification), so always read the last line. The message is written to standard error,
  not to standard output: it appears on the screen even when the output is captured, and the checking
  commands of section 3.6 item 1 then report `0` lines (PowerShell `$out.Count`) or an empty file
  (`wc -l` prints `0`). Go to the folder that contains `Revision` (`cd $HOME\Dirac_claude` in PowerShell,
  `cd ~/Dirac_claude` on macOS and Linux) and run again.
* `Get::noopen` mentioning `RevisionAlgebra.wl` as the first message: the package file is missing or
  renamed. The run then prints many further messages (for example `Part::partd`), 45 lines
  `FAIL  <name>`, the last line `0/45 checks passed; time ... s`, and exits with code 1 (observed: about
  100 printed lines). It also OVERWRITES `Revision/algebra/reports/wolfram-algebra.json` with this failing
  report (summary `"passed": 0, "failed": 45`), so `git status --porcelain` then lists that file as
  modified; `gammas.json` is not rewritten. Restore the package with
  `git checkout -- Revision/algebra/wolfram/RevisionAlgebra.wl` and run the script again, which rewrites
  the report correctly (or restore the report as well with
  `git checkout -- Revision/algebra/reports/wolfram-algebra.json`).
* `OpenWrite::noopen` or "permission denied": an output file cannot be written (it is read-only, open in
  another program, or the folder is protected). The script then prints, after the Wolfram message, the
  line `ERROR  cannot write <path of the file>; the run is aborted with exit code 1 (no verdict is printed)`
  and exits with code 1 at once; no verdict line is printed and the file named in the message was NOT
  rewritten (when it is the report, `gammas.json` has already been rewritten, with the same content).
  Close any program that has `gammas.json` or `wolfram-algebra.json` open, make sure the files and the
  folder are not read-only (clone into your home folder, not into a protected or synchronised folder),
  and run again. CAUTION for older copies: the driver as committed up to commit `c2b33cc` (sha256
  `75b9f95d...`, section 2.1) did not stop. With a read-only `gammas.json` it printed the messages
  `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream` among its output, still ended with
  `45/45 checks passed`, and exited with code 0, although the file was NOT rewritten (check 45 then read
  the old file); that is why the first criterion of section 3.6 asks for exactly 46 lines and no message.
* A message that no licence or no more kernels are available: another Wolfram program is using the
  allowed kernels. Close other Mathematica windows and other `wolframscript` commands and run again.
* A line beginning with `FAIL`, a last line `N/45 checks passed` with N below 45, and exit code 1: do not
  edit anything. Run `git status` and `git diff Revision/algebra/wolfram` to see whether the script or
  the package were changed; if they were, restore them with
  `git checkout -- Revision/algebra/wolfram Revision/algebra/gammas.json Revision/algebra/reports/wolfram-algebra.json`
  and run again. If an unmodified clone still fails, note the failing check names, the details in
  `Revision/algebra/reports/wolfram-algebra.json` and the output of `wolframscript -code '$Version'`
  (type the single quotes: with double quotes PowerShell and the macOS/Linux shells replace `$Version`
  by an empty text), and report them: the verified result is 45 of 45.
* `git status --porcelain` lists `gammas.json` or `wolfram-algebra.json` although all checks passed: a
  program converted the line endings or changed the files. The repository stores every file byte for
  byte (`.gitattributes` contains `* -text`) and the script writes LF line endings on every system;
  restore with the `git checkout -- ...` command of section 5.4 and run again.

## 4. Expected output

### 4.1 Printed on the screen

Exactly 46 lines: 45 verdict lines, each `PASS`, two spaces and the check name, in this order, and one
final line:

```text
PASS  s4_t4_entries_from_Signature_and_deltas
PASS  s4_self_dual_t4_anti_self_dual
PASS  s4_t4_quaternion_algebras
PASS  sigma8_involution
PASS  tau_taubar_Clifford_relation
PASS  tau7_and_sigma_identities
PASS  T16_block_form
PASS  coordinate_map
PASS  eta_in_author_order
PASS  Clifford_relation
PASS  reality
PASS  signed_permutation_matrices
PASS  symmetry_pattern
PASS  C_definition
PASS  C_real_symmetric
PASS  C_squared_identity
PASS  C_gamma_real_antisymmetric
PASS  C_gamma_C_inverse
PASS  Gamma_definition
PASS  Gamma_diag
PASS  Gamma_anticommutes_with_gammas
PASS  Gamma_commutes_with_C
PASS  notebook_product_identity
PASS  B_definition
PASS  B_Hermitian
PASS  B_squared_identity
PASS  B_signature_8_8
PASS  B_purely_imaginary
PASS  S_antisymmetric_in_ab
PASS  S_half_product
PASS  S_real_entries_in_half_integers
PASS  S_gamma_commutator
PASS  S_Lorentz_algebra
PASS  S_preserves_C
PASS  S_preserves_B_only_off_x4
PASS  S_commutes_with_Gamma
PASS  Clifford_basis_spans_full_matrix_algebra
PASS  even_subalgebra_dimension
PASS  Pin44_irreducible_commutant_dim_1
PASS  Spin44_commutant_dim_2_chiral_projectors
PASS  chiral_halves_irreducible
PASS  chiral_halves_inequivalent_intertwiners_0
PASS  Spin_Pin_reflection_swaps_halves
PASS  fixture_written_deterministically
PASS  fixture_round_trip
45/45 checks passed; time 1.6 s
```

The number after `time` is the script's own computing time in seconds (it excludes the start of the
Wolfram kernel) and differs from run to run (the measured values are in section 4.4). It is rounded to
steps of 0.01 in floating point, so its printed form varies: usually like `1.6` or `1.57`, sometimes
with many digits (for example `time 1.6300000000000001 s` or `time 2.2800000000000002 s`), and, when the
rounded value is a whole number of seconds, with a trailing point and no digits after it (for example
`time 2. s`; `Round[1.999, 0.01]` prints `2.` in Wolfram 15.0.1). None of these forms is an error: only
the text before `; time` matters, and the time affects only the screen, not the output files. Nothing
else is printed and nothing is written to standard error.

### 4.2 Exit code

`0` when all 45 checks pass, `1` when any check fails (the failure path was confirmed on a scratch
copy of the driver with one added failing check: it printed `FAIL  forced_failure_test_only`,
`45/46 checks passed`, exited with 1 and wrote `"failed": 1` into the summary). Also `1`, at once and
without any verdict line, when an output file cannot be written (the line `ERROR  cannot write ...`,
section 3.7). Remember the exception of section 3.7: when the script file is not found, WolframScript
prints `Failed to open file at path: ...` and still exits with 0.

### 4.3 Files written

The two files of section 2.3, with exactly the sha256 values given there, and the summary line
`  "summary": {"passed": 45, "failed": 0, "total": 45},` (line 7 of the report). The fixture begins with
`{` and the key `"description"` and holds the matrices as lists of rows; for example `"eta": [1, 1, 1, -1, -1, -1, -1, 1],`
is one of its lines.

### 4.4 Run time and memory on the verification machine

Windows 11 Pro for Workstations, 24 logical processors, 191 GB memory, Wolfram 15.0.1. The times below
are SAMPLES, not bounds: they depend on how busy the machine is, and between 6 and 17 Wolfram kernels of
other jobs were running on the same machine during the measurements.

* Wall-clock time of the whole command (start of the kernel included): the first verification measured
  4.37, 4.89, 4.82, 4.74, 5.05, 5.56, 5.70, 5.83 and 5.31 s; the re-verification of 2026-10-02 measured
  4.76, 4.79, 4.39, 4.39, 4.07, 4.97, 5.55, 5.24 and 4.38 s; an independent verifier measured 4.40 to
  7.45 s; the re-verification of 2026-10-07 (12 to 13 Wolfram kernels of other jobs running at the
  same time) measured 5.98, 5.60, 7.25, 6.65, 6.80, 6.99, 7.40 and 6.34 s under the monitors of
  section 6.4, 8.19 s with `Measure-Command` and 6.88 s with `time` in Git Bash. Overall: 4.07 to
  8.19 s.
* The script's own time (the number printed after `time`): 1.6 to 2.07 s in the first verification, 1.43
  to 1.71 s in the re-verification, 1.45 to 3.78 s in the independent verifier's runs, 1.81 to 2.6 s on
  2026-10-07. Overall: 1.43 to 3.78 s.
* Memory: the Wolfram kernel process peaked at 395.7 to 398.3 MiB (working set) in the nine runs whose
  monitor read the kernel's peak working set until the end of the run (five on 2026-10-02, four on
  2026-10-07); `wolframscript` itself peaked at 16.6 to 17 MiB; for the short licence probe of section
  5.2 readings of 53.6 and 67.1 MiB were taken while it ran.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

* OVERWRITTEN on every successful run: `Revision/algebra/gammas.json` and
  `Revision/algebra/reports/wolfram-algebra.json`. Both are rewritten even when nothing changes, so their
  modification time changes; their content is byte-identical to the committed files, so
  `git status --porcelain` stays empty. In the failure cases of section 3.7 this is different: when an
  output cannot be written, the run stops with exit code 1 and that file is NOT rewritten (when the report
  is the one that fails, `gammas.json` has already been rewritten with the same content); when the
  package is missing, the report IS overwritten with a failing report (0 of 45) and `gammas.json` is not
  rewritten.
* CREATED only if missing: the folder `Revision/algebra/reports/` (tested: after removing it, the run
  re-created it and wrote a report identical to the committed one). That folder also holds the reports
  of the Python checker of this algebra (`python-algebra.json`, `python-gammas.json`); this script does
  not re-create them, so if you delete the folder, restore it with the command of section 5.4.
* Nothing else in the repository is created or changed: `git status --porcelain --ignored` printed
  nothing after runs A and B and after the last run in every clone of the first verification (no
  untracked and no ignored files appeared); in the re-verification clones it listed nothing, or only the
  fixed driver copied in on purpose (section 6.2).

### 5.2 Outside the repository

* Wolfram processes: `wolframscript` starts TWO processes of the Wolfram program one after the other (on
  Windows with Wolfram 15.0.1 the program is `wolfram.exe`; older versions call it `WolframKernel`).
  First a short licence probe, `wolfram.exe -wlbanner -licenseinfo`, which runs for about 0.3 s (in one
  run seen from +0.09 s to +0.41 s after the start; its peak working set was read as 53.6 and 67.1 MiB
  in two runs, readings taken while it ran, so lower bounds); then the ONE Wolfram kernel that
  runs the script, `wolfram.exe -runfirst ... -linkmode Connect -linkname <random>_shm -mathlink` (it
  talks to `wolframscript` through a shared-memory link), which ends when the script calls `Exit`. Both
  are child processes of `wolframscript`. No parallel kernels are launched. (The records of 2026-10-02
  named only the kernel; the probe was found on 2026-10-07, section 6.4.)
* Temporary files: none are left behind. With the variables `TEMP` and `TMP` pointed to an empty private
  folder, the folder was still empty after the run. On Windows, `wolframscript` creates TWO temporary
  files of its own in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (names like
  `tmp_` followed by 10 random letters). The first is empty and appears within about 0.1 s of the start
  (observed at +0.02 to +0.07 s). The second appears 2 to 4 s after the start, once the kernel runs
  (observed at +2.3 to +3.9 s), and holds a byte-for-byte copy of everything the script prints (1384 bytes
  when the last line reads `time 1.57 s`; about 1.4 KB in general). Both are deleted when `wolframscript`
  finishes: in the monitored runs they were still present at the last look before the process ended and
  gone at the first look after it. Observation method: a monitor listed the folder about every 15 ms (a
  10 ms pause between looks), copied every new non-empty file, and compared the copy with the captured
  output (`cmp`: identical); files of other programs that appeared in the same folder at the same time
  were told apart by their content. Only Windows was observed; on macOS and Linux the location of these
  files was not verified.
* `wolframscript` re-saves its settings file (`%APPDATA%\Wolfram\WolframScript\WolframScript.conf` on
  Windows): its modification time changed during the runs, its content did not (same sha256 before and
  after).
* Network: none. While the script ran, the only network endpoints owned by `wolframscript` and its kernel
  were short-lived TCP connections of the kernel with itself on the loopback address `127.0.0.1` (both
  ends belong to the kernel). One to three such connections per run were seen; in the two runs where
  their duration was recorded, each was seen at a single look of the monitor only, so each lasted a
  fraction of a second. Windows also lists the local port of such a connection a second time, in state
  `Bound` on `0.0.0.0`, with no remote address. No UDP endpoint, no endpoint owned by `wolframscript`
  itself and no connection to any other computer was seen. Observation method: a monitor read the
  system's TCP and UDP tables (IPv4 and IPv6) again and again during the run (every 0.12 s on average in
  two runs, every 0.37 s in a third) and kept every entry owned by `wolframscript` or by its kernel; the
  `Bound` entries were seen in a fourth run with the PowerShell command `Get-NetTCPConnection`. The
  activation of the free Wolfram Engine (section 3.3) needs the internet once; the script does not.

### 5.3 Effects on other parts of the repository

The fixture `gammas.json` is read by the programs listed in section 1.4. Because a correct run
rewrites it byte for byte, nothing downstream changes. If it ever changed, the downstream reports
would no longer match and those programs would have to be re-run; restore the committed state instead
(section 5.4). Two of those reports record the sha256 of `gammas.json` itself:
`Revision/kohn_sham/reports/ks-theory-wolfram.json` (check `fixture_input`, written by
`Revision/kohn_sham/theory/verify_ks_theory.wls`) and `Revision/kohn_sham/results/parameters.json` (key
`gammasSha256`, written by the Rust solver).

### 5.4 How to restore the committed state

From the repository root, on every system:

```text
git checkout -- Revision/algebra/gammas.json Revision/algebra/reports/wolfram-algebra.json
```

If the folder `Revision/algebra/reports` was deleted, use `git checkout -- Revision/algebra/reports`
instead. Afterwards `git status --porcelain` prints nothing.

## 6. Verification record

* Date: 2026-10-02 (first verification, then a re-verification after an independent review on the same
  day, sections 6.1 to 6.3), and 2026-10-07 (a further re-verification after the verification workflow
  was interrupted by a session limit and restarted, section 6.4).
* Commits verified: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` on 2026-10-02 (sections 6.1 and 6.2) and
  `a4c5eda1df069a43a55ff8b57148f5de8edd1670` on 2026-10-07 (section 6.4; the fix of section 6.3 is
  committed there). The commit, environment and files of 2026-10-07 are listed in section 6.4; the two
  items below describe 2026-10-02.
* Commit verified on 2026-10-02: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (branch `main` of
  `https://github.com/once-ere/Dirac_claude.git`). The most recent commit that changed a file of this set
  is `9ea68d4ec75ebb3e74e33ea6a63248e2689541a5` (2026-10-01 12:55:44 -0700; driver, fixture and report);
  the package `RevisionAlgebra.wl` was last changed in `40168e94a6b4b11d957f6714cbfb10106f7fb63d`
  (2026-10-01 08:24:04 -0700) (`git log -1 -- <file>` for each file, in a fresh clone). The commit
  `45d47343ae480df46e06689ed822b8f9a88a8030`, current when the verification started, has the same files
  (`git diff 45d4734 c2b33cc -- Revision/algebra` is empty). The driver described in section 2.1 is the
  committed driver plus the fix of section 6.3, made in the working tree on 2026-10-02 after commit
  `c2b33cc`.
* Environment on 2026-10-02: Windows 11 Pro for Workstations 10.0.26200, 24 logical processors, 191 GB
  memory; WolframScript 1.14.0; `$Version` = `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`,
  Professional licence (not a network licence: `$NetworkLicense` is `False`); Git 2.51.2.windows.1;
  PowerShell 7.6.6 and Git Bash (MSYS2 MINGW64). Files copied into the clones: none in the first
  verification and none in clones 4 and 5 (the set needs only committed files); into clones 6 and 7 only
  the fixed driver `Revision/algebra/wolfram/verify_algebra.wls` from the working tree (sha256
  `99ff3c1fc6e1c7720cd00ef4141a0fc950ba4906d4153770d3ffd6c5840022ff`; after the runs `cmp` confirmed that
  the copies still equal the working-tree file).

### 6.1 First verification (the driver as committed, sha256 `75b9f95d...`)

* Two fresh clones of the repository were made in a scratch folder (`git clone`, nothing else copied).
  Run A in the first clone and run B in the second (both started from PowerShell under a monitor of
  wall time and memory; run B with `TEMP` and `TMP` pointed to an empty private folder), then run C, a
  second run in the first clone, from Git Bash with `time`:

  | run | clone | exit code | checks | wall time | script time | kernel peak memory |
  | --- | --- | --- | --- | --- | --- | --- |
  | A | 1 (fresh) | 0 | 45/45 PASS | 4.37 s | 1.6 s | 398.3 MiB |
  | B | 2 (fresh) | 0 | 45/45 PASS | 4.89 s | 1.62 s | 397.6 MiB |
  | C | 1 (second run) | 0 | 45/45 PASS | 4.82 s | 1.6 s | not measured |

* Byte identity: after runs A, B and C, `Revision/algebra/gammas.json`
  (`95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01`) and
  `Revision/algebra/reports/wolfram-algebra.json`
  (`2167774a0bd0a2794fd5999ac485717c0e725f974826b2bb70b5d46d9598a6a3`) were byte-identical to the
  committed files (`git show HEAD:<path>` has the same sha256) and the outputs of run A and run B were
  byte-identical to each other (`cmp`); the modification times showed that both files had been rewritten.
  The 45 verdict lines printed by runs A and B were identical. Standard error was empty.
* Further runs of the unmodified script, all with exit code 0, 45/45 PASS and the same output hashes
  checked at the end: the PowerShell commands of section 3.5 with forward slashes (4.74 s) and with
  backslashes (5.05 s), the commands of sections 3.5 and 3.6 as printed at that time (5.56 s), a run from
  the folder `Revision` with the path `algebra/wolfram/verify_algebra.wls`, a run after deleting
  `Revision/algebra/reports` (re-created, identical report), a run under a network monitor, a run under a
  monitor of the Wolfram user folders, two runs comparing the WolframScript settings file before and
  after, one run with `LOCALAPPDATA` pointed to an empty private folder (nothing was written there), and
  three runs under a monitor of the WolframScript temporary folder (5.70, 5.83, 5.31 s). A third fresh
  clone was then used to type the commands of sections 3.3 (test), 3.5 and 3.6 literally, in Git Bash
  (the macOS/Linux form, with `sha256sum` and `grep`; two runs) and in PowerShell (one run): each ended
  with `45/45 checks passed` and exit code 0 (46 printed lines counted in the second Git Bash run and in
  the PowerShell run) and gave the summary line and the hashes of section 2.3.
  In total 19 runs of the unmodified script; after all of them every clone had an empty
  `git status --porcelain --ignored`. The macOS and Linux commands were run in Git Bash on Windows, not on
  a Mac or a Linux machine.
* Negative tests (scratch clone only, then restored from `git show HEAD:<path>`): running from a wrong
  folder prints `Failed to open file at path: Revision/algebra/wolfram/verify_algebra.wls` with exit
  code 0; a copy of the driver with one added failing check exits with 1 and reports
  `"failed": 1`.

### 6.2 Re-verification after the review (committed driver: clones 4, 5; fixed driver: clones 6, 7)

* Four more fresh clones of `c2b33cc` (each `git clone` took 9 to 12 s). Clones 4 and 5 were left as
  cloned; into clones 6 and 7 the fixed driver was copied. Runs 1 to 8 were started from PowerShell with
  `Start-Process` (output captured to files) under a monitor; run 9 was started from Git Bash with
  `time`:

  | run | clone | driver | monitor | exit code | checks | lines printed | wall time | script time | kernel peak memory |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 4 (fresh) | committed | temporary folder | 0 | 45/45 PASS | 46 | 4.76 s | 1.57 s | not measured |
  | 2 | 5 (fresh) | committed | connections (`Get-NetTCPConnection`) | 0 | 45/45 PASS | 46 | 4.79 s | 1.6 s | 397.7 MiB |
  | 3 | 5 | committed | temporary folder | 0 | 45/45 PASS | 46 | 4.39 s | 1.53 s | not measured |
  | 4 | 4 | committed | TCP/UDP tables | 0 | 45/45 PASS | 46 | 4.39 s | 1.54 s | 396.5 MiB |
  | 5 | 5 | committed | TCP/UDP tables | 0 | 45/45 PASS | 46 | 4.07 s | 1.43 s | 398.1 MiB |
  | 6 | 6 (fresh) | fixed | temporary folder | 0 | 45/45 PASS | 46 | 4.97 s | 1.67 s | not measured |
  | 7 | 7 (fresh) | fixed | TCP/UDP tables | 0 | 45/45 PASS | 46 | 5.55 s | 1.54 s | incomplete reading |
  | 8 | 7 | fixed | TCP/UDP tables and child processes | 0 | 45/45 PASS | 46 | 5.24 s | 1.48 s | incomplete reading |
  | 9 | 6 | fixed | none (Git Bash `time`) | 0 | 45/45 PASS | 46 | 4.38 s | 1.52 s | not measured |

  In runs 7 and 8 the monitor did not read the kernel's peak working set until the end of the run (it
  recorded 56.2 and 148.3 MiB); these two readings are not the peak and are not used in section 4.4.
* Byte identity: after run 1, `gammas.json` and `wolfram-algebra.json` had the sha256 of section 2.3;
  after runs 8 and 9 the outputs of clones 6 and 7 (fixed driver, two fresh clones) were byte-identical
  (`cmp`) to each other and to `git show HEAD:<path>`, so the fix changes no output; and after the last
  run in each of the four clones (including the reruns after the negative tests below) both outputs were
  byte-identical to `git show HEAD:<path>`. The 45 verdict lines of all nine runs were identical
  (`cmp`), standard error was empty in every run, and the modification times (read after runs 1, 8 and
  9) showed that both files had been rewritten.
* The checking commands of section 3.6 item 1, typed as printed: in PowerShell with the committed driver
  (clone 5) and with the fixed driver (clone 6, 5.16 s with `Measure-Command`), and in the macOS/Linux
  form in Git Bash with the fixed driver (clone 6): each printed `0`, `46` and the single final line. After
  all runs, clones 4 and 5 had an empty `git status --porcelain --ignored`, and clones 6 and 7 listed only
  ` M Revision/algebra/wolfram/verify_algebra.wls` (the fixed driver copied in on purpose).
* The temporary files and the network were observed as described in section 5.2: runs 1, 3 and 6 showed
  two temporary files of `wolframscript` each, the second byte-identical to the captured output (a third,
  24-byte file that appeared during run 6 contained text written by another program and was not
  `wolframscript`'s); runs 4, 5 and 8 showed only loopback connections of the kernel with itself (three,
  one and one of them; the monitor of run 7 recorded no entry at all), and run 2 a `Bound` entry on
  `0.0.0.0` with no remote address. The printed time `2.` was confirmed with `wolframscript -code`
  printing `Round[1.999, 0.01]`.
* Negative tests (scratch clones only; files restored from `git show HEAD:<path>` or by a correct rerun):
  * committed driver, `gammas.json` made read-only (`attrib +R`, clone 5): 52 printed lines, among them
    `OpenWrite::noopen: Cannot open ...\gammas.json.`, `BinaryWrite::stream: $Failed is not a string, ...`
    and `Close::stream: ...` (each after an empty line); last line `45/45 checks passed; time 1.71 s`;
    exit code 0; `gammas.json` was not rewritten and `git status --porcelain` was empty. This is the
    execution defect fixed in section 6.3. The PowerShell commands of section 3.6 item 1 printed `0`, `52`
    and seven lines (three empty lines, the three messages and the final line), so they reveal the
    problem.
  * committed driver, package renamed (clone 5): first message `Get::noopen: Cannot open
    ...\RevisionAlgebra.wl.`, then `Part::partd` and other messages, 45 `FAIL` lines, last line
    `0/45 checks passed; time 0.38 s`, exit code 1; the report was overwritten (summary
    `"passed": 0, "failed": 45, "total": 45`; `git status --porcelain` listed it as modified) and
    `gammas.json` was not rewritten.
  * fixed driver, `gammas.json` read-only (clone 7): 3 printed lines (an empty line,
    `OpenWrite::noopen: Cannot open ...\gammas.json.` and
    `ERROR  cannot write ...\gammas.json; the run is aborted with exit code 1 (no verdict is printed)`),
    exit code 1, the report not rewritten (modification time unchanged).
  * fixed driver, the report read-only (clone 7): the same 3 lines for `wolfram-algebra.json`, exit code 1;
    `gammas.json` had been rewritten (same content, new modification time).
  * fixed driver, package renamed (clone 7): the same behaviour as the committed driver (45 `FAIL` lines,
    `0/45 checks passed; time 0.34 s`, exit code 1, report overwritten); after the package was restored a
    rerun printed `45/45 checks passed; time 1.52 s` with exit code 0, and the report was again identical
    to the committed one.
  * fixed driver, wrong folder: `Failed to open file at path: Revision/algebra/wolfram/verify_algebra.wls`,
    exit code 0 (WolframScript's own behaviour, unchanged).

### 6.3 Fix made (execution defect) and corrections of this file

* Fix, `Revision/algebra/wolfram/verify_algebra.wls` (9 lines inserted, 3 deleted; 275 -> 281 lines;
  sha256 `75b9f95d5fc7c1e748579f798838427401dd23fcd5b3b7ee3159238512b8369a` ->
  `99ff3c1fc6e1c7720cd00ef4141a0fc950ba4906d4153770d3ffd6c5840022ff`). Root cause: the helper `writeLF`,
  which writes both outputs, did not check the result of `OpenWrite`. When a file could not be opened,
  `BinaryWrite` and `Close` only printed messages; check 45 (`fixture_round_trip`) then re-imported the OLD
  `gammas.json`, which equals the committed one, and passed; so the run reported 45/45 with exit code 0
  although the file had not been written. Now `writeLF` checks that `OpenWrite` returned an output stream
  and that `BinaryWrite` did not fail, closes the stream only if it was opened, and otherwise prints
  `ERROR  cannot write <path>; the run is aborted with exit code 1 (no verdict is printed)` and calls
  `Exit[1]`; the header comment of the driver says so. No check, tolerance, check name or output byte
  changed (verified in section 6.2).
* Corrections of this file after the review: the charge-conjugation remark of section 1.2 (`calC_+ = C`
  acts as the identity on a real field; the nontrivial matrix charge conjugation of a real field is
  `Gamma` together with `m -> -m`); the list of programs that read `gammas.json` (section 1.4: some
  checkers rebuild the gammas independently); the second temporary file and the network details (section
  5.2); the printed time format and the measured times as samples (sections 4.1 and 4.4); the failure
  cases of a missing package and of an output that cannot be written (sections 3.6, 3.7, 4.2 and 5.1);
  the commits of section 6; the reports that record the sha256 of `gammas.json` (section 5.3).
* Open discrepancies: none. No scientific result changed: 45 of 45 checks pass and both outputs are
  byte-identical to the committed files. The only caveat is the behaviour of WolframScript itself
  described in section 3.7 (exit code 0 when the script file is not found).
