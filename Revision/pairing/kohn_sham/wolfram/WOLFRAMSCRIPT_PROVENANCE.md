# Provenance of the wolframscript set `Revision/pairing/kohn_sham/wolfram/` (theorem T3 and its completion)

This file is written for a student who has never used Wolfram or a terminal before. It says what the two
scripts of the set do, which files they read and write, how to install everything and run them on Windows,
macOS or Linux, what you should see, what a run changes on your computer, and how and when it was verified.
Everything you need is in this file.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

The set is two WolframScript files in `Revision/pairing/kohn_sham/wolfram/`:

1. `verify_t3.wls` proves theorem T3 ("the Kohn-Sham level of the pairing of universes of masses +m and -m")
   by exact symbolic algebra (10 checks) and writes the theorem record `Revision/pairing/kohn_sham/t3-theory.json`
   and the check report `Revision/pairing/kohn_sham/reports/wolfram-t3.json`.
2. `verify_t3_completion.wls` adds three exact checks that complete T3 (statement S6 and the filling convention
   of the image) and writes the completion record `Revision/pairing/kohn_sham/t3-completion.json` and the check
   report `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`.

Neither script reads an output of the other (both read only `Revision/kohn_sham/ks-theory.json` and
`Revision/algebra/gammas.json`), so they may run in either order; this file runs `verify_t3.wls` first. The
two independent sympy checkers of section 3.8 are not part of the set but read its outputs.

### 1.2 The physics, in plain words

- The repository studies a field with 16 complex components (called `dirac16complex`) living in an
  8-dimensional space-time chosen by the author. The coordinates are named as the author names them:
  x1, x2, x3 are ordinary 3-space; x4 is time; x5, x6, x7 are three extra "times" that deflate exponentially;
  x8 is a hidden direction, written as y = ln(sin z)/(6 H) with y between -L and 0. The end y = 0 is called
  the brane, the end y = -L is called the tip.
- The Kohn-Sham method is the method behind density-functional theory (DFT). Instead of solving the full
  many-particle problem, every particle moves in an averaged field produced by the densities of all the
  particles; the averaged field depends on the densities, and the densities depend on the orbitals, so the
  problem must be solved "self-consistently" (repeat until nothing changes). In the Kohn-Sham problem of this
  repository (`Revision/kohn_sham/ks-theory.json`) the 16 components split into eight independent 2 x 2
  blocks. A block is labelled by a sign j = +1 or -1 (and two more signs, s2 and s3); in each block an
  orbital is a 2-component function chi(y) = (chi1(y), chi2(y)) of the hidden coordinate y, and the block
  Hamiltonian is h_j = j[-i sigma1 d/dy + M_eff(y) sigma2 + kappa(y) k sigma3] + v_v(y), with the Pauli
  matrices sigma1, sigma2, sigma3, the effective mass M_eff = m + (15/16) lambda S, the potential
  v_v = -lambda n/16, the bare mass m, the coupling lambda, the scalar density S and the particle density n.
  (Both scripts READ the coefficients 15/16 and -1/16 and the interaction energy
  e_int = (15/32) lambda S^2 - (1/32) lambda n^2 from `ks-theory.json`.)
- Theorem T3 says: take ANY self-consistent Kohn-Sham state of a universe with mass m, coupling lambda and
  tip angle theta. Replace every orbital chi of block j by sigma2 chi in block -j (in the 16-component
  language this is the chirality matrix Gamma), exchange the two brane parities and change the tip angle to
  pi - theta. The result is again a self-consistent Kohn-Sham state, of a universe with mass -m, the SAME
  coupling +lambda and tip angle pi - theta. All energy levels, occupations, the chemical potential, the
  particle number, the entropy, the Kohn-Sham energy, the grand potential, the free energy and the
  energy-momentum profiles are EQUAL; the densities S(y) and Q(y) change sign.
- The completion adds: (S6) with the expectation-value rule of the canonical quantisation (the Krein metric
  B), every component of the 16-component energy-momentum tensor and of the current is equal for the pair;
  and the filling convention (which levels count as particles) of the +M member is carried onto the -M
  member in its own boundary conditions.

### 1.3 How `verify_t3.wls` proves T3

The script does not solve any equation numerically. Each check builds an expression from arbitrary symbolic
functions (for example M(y), kappa(y), v(y), c1(y), c2(y)) and symbolic numbers, asks Wolfram to simplify it,
and passes only if the result is exactly zero. Five of the ten checks (checks 1, 3, 6, 7 and 8) also contain
a "control": a deliberately wrong variant that must NOT simplify to zero, which shows that the check is able
to detect a false statement. The other five checks (2, 4, 5, 9 and 10) have no control.

| # | check name | what is proved (in words) | control (must fail) |
| --- | --- | --- | --- |
| 1 | `T3_block_hamiltonian_map` | sigma2 h_j(M, k, v) chi = h_(-j)(-M, k, v)(sigma2 chi) for arbitrary functions M(y), kappa(y), v(y), any k, both j: an orbital with level eps goes to an orbital with the same level eps | the identity without M -> -M |
| 2 | `T3_ode_map` | the same statement for the first-order "shooting" form chi' = N chi: sigma2 N_j(M) sigma2 = N_(-j)(-M) | none |
| 3 | `T3_tip_condition_map` | the tip condition with angle theta becomes the tip condition with angle pi - theta (theta = 0 goes to theta = pi) | the image of (1, 0) violates the untransformed condition theta = 0 |
| 4 | `T3_brane_parities_exchanged` | the two brane parities (chi2(0) = 0 and chi1(0) = 0) are exchanged; the boundary current and the norm are unchanged | none |
| 5 | `T3_orbital_densities` | per orbital: n and t are unchanged, s and q change sign, c is unchanged (for arbitrary complex chi, both j) | none |
| 6 | `T3_mean_field_map` | the coefficients c_M, c_v of M_eff = m + c_M lambda S and v_v = c_v lambda n are READ from `ks-theory.json` (`exchange.kohnShamPotentials`), and c_S, c_n of e_int = c_S lambda S^2 + c_n lambda n^2 are parsed from its stated formula. Consistency: they are the values 15/16, -1/16, 15/32, -1/32 of hypothesis H2; the coefficient fields agree with the stated formulas `Meff` and `vv`; M_eff - m = d e_int/dS and v_v = d e_int/dn. Map: M_eff(-m, +lambda, -S) = -M_eff(m, lambda, S); with v_v written as a function v_v(m, lambda, n, S) of the four arguments of the self-consistency loop, its value at the image arguments (-m, +lambda, n, -S) equals its value at (m, lambda, n, S); e_int is unchanged when S -> -S | with (-m, -lambda): M_eff is not mapped to -M_eff (difference 2 c_M lambda S) and v_v(-m, -lambda, n, -S) differs from v_v(m, lambda, n, S) (difference -2 c_v lambda n) |
| 7 | `T3_energies_and_emt_profiles_equal` | for two general occupied orbitals of opposite block type: energy density, pressures p3, p_t, p8, the Kohn-Sham energy integrand, entropy terms and the exact-Fock diagnostic are equal; S and Q change sign (the same function v_v(m, lambda, n, S) of check 6 enters p8) | with (-m, -lambda) the energy integrand differs |
| 8 | `T3_exact_k0_spectra` | for k = 0, v = 0 and constant M the exact characteristic functions of the original and the image problem agree, so the spectra are equal level by level; the zero mode maps to the zero mode | the untransformed tip gives a different spectrum |
| 9 | `T3_Gamma_is_the_block_map` | with the block basis V read from `ks-theory.json` and the matrices read from `gammas.json`: V is unitary, Gamma = diag(-1 (8 times), +1 (8 times)), Gamma maps block (j, s2, s3) to block (-j, s2, s3) times s2 sigma2, and in every block gamma^(x8) = sigma3 and gamma^(x8) gamma^(x4) = j sigma1 | none |
| 10 | `T3_z2_mirror_copy_carries_minus_m_plus_lambda` | inside the ASSUMED Z2 mirror (orbifold) construction, the mirror copy of a self-consistent state carries (-m, +lambda) | none |

### 1.4 What `verify_t3_completion.wls` computes

| # | check name | what is proved (in words) |
| --- | --- | --- |
| 1 | `T3C_mean_field_coefficients_from_ks_theory` | the coefficients 15/16 (M_eff) and -1/16 (v_v) read from `ks-theory.json`, its formulas `Meff`, `vv` and `e_int` as stated text; M_eff - m = d e_int/dS, v_v = d e_int/dn; M_eff(-m, +lambda, -S) = -M_eff(m, lambda, S), e_int even in S, v_v free of S; control: with (-m, -lambda) M_eff is not mapped to -M_eff |
| 2 | `T3C_filling_convention_mapped` | the map commutes with the continuation in lambda of the filling convention (hypothesis H5) for any S(y), both j; the k = 0 brane zero mode (E^(M y), 0) goes to the zero mode (0, I E^(M y)) of the image problem in its own boundary conditions (odd parity, tip theta = pi); control: it violates the untransformed tip theta = 0 |
| 3 | `T3C_krein_rule_16_component` | with gamma^(x1..x8), B, C and Gamma read from `gammas.json` and the expectation rule rho = sum f u u^dagger B (`ks-theory.json` `exchange.expectationRule`): Gamma^2 = 1, Gamma B Gamma = -B, Gamma C Gamma = C, Gamma gamma^a Gamma = -gamma^a, Gamma S^ab Gamma = S^ab; rho' = -Gamma rho Gamma; n even, S and Q odd, all 8 + 512 kinetic bilinears even: every component of the energy-momentum tensor and of the current is equal for the pair (S6) |

The completion record `t3-completion.json` (and the detail text of its check 1) describes `verify_t3.wls` as
it was when the completion was written (2026-10-08, before the fix of section 1.5): "writes the coefficients
into the script" and "its v_v clause compares an expression with itself". That is the historical state that
the completion closed (gap 1); since the fix of section 1.5, `verify_t3.wls` reads the coefficients itself.
Unlike `verify_t3.wls`, the completion script has no `ERROR` exit: a missing input gives Wolfram messages and
`FAIL` lines (section 3.7).

### 1.5 The fix of 2026-10-08 in `verify_t3.wls`

The T3 completion found two defects in check 6 of `verify_t3.wls` (version sha256
`ea6c436f667c465727967c8b9664e2425227be0d71a55ca36a36e13a3da497d8`, 207 lines): it typed the Kohn-Sham
coefficients into the script (`meff`, `vvf`, `eint` at its line 77) instead of reading them from
`ks-theory.json`, and its clause `vvf[lam, n] === vvf[lam, n]` (line 79) compared an expression with itself,
so it was always true. Both were fixed (section 6.5): the coefficients are read from
`ks-theory.json` `exchange.kohnShamPotentials` exactly as `verify_t3_completion.wls` reads them (with the
consistency checks of the table in section 1.3), and the v_v clause is now the statement of the table. The
ten check names, the theorem record `t3-theory.json` (byte for byte) and the counts (10 of 10) are
unchanged; only the detail text of check 6 in `wolfram-t3.json` changed. Negative tests (section 6.5) show
that check 6 now FAILS when a coefficient in `ks-theory.json` is broken, while the old script passed 10/10
with the same broken input. The script also stops with an `ERROR` line (section 4.2) when an input is missing
or unreadable, instead of running on with Wolfram messages.

What T3 does NOT establish (the theorem record says this explicitly): no creation process, rate or amplitude
(it maps solutions to solutions; it does not make a pair of universes); only instantaneous (adiabatic)
mean-field states (the time-dependent problem is open); the Z2 brane is an ASSUMPTION and the tip angle must
be transformed; no correlation beyond Hartree plus exchange; no statement about two independently quantised
universes; no back-reaction on the geometry. The pairing proved here is (m, lambda) -> (-m, +lambda) at
equal energies, not (m, lambda) -> (-m, -lambda). The completion adds no creation process either; its
numerical demonstrations (computed elsewhere) use a PRESCRIBED BACKGROUND history a4 = A H x4 without
back-reaction.

### 1.6 Which files cite the set

`git grep -l -E 'verify_t3|t3-theory|wolfram-t3|t3-completion'` at commit `fe2d80c` lists, besides the set's
own files: the documents `Revision/docs/PAIR_CREATION_PROOFS.md` and `.tex` (theorem T3, its check tables and
counts, the completion), `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` and `.tex` (record table "Wolfram: 10
of 10 checks pass"), `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md` and `.tex`; `Revision/README.md` does not
match the pattern but quotes `T3 Wolfram 10/10`; `Revision/pairing/kohn_sham/README.md`;
`Revision/pairing/pairing-theory.json` and `Revision/pairing/wolfram/verify_pairing.wls` (a pointer saying
that T3 is proved here); the sympy checkers `Revision/pairing/kohn_sham/python/check_t3.py` (reads
`t3-theory.json`) and `check_t3_completion.py` (reads `wolfram-t3.json`, `t3-theory.json`, `t3-completion.json`
and `wolfram-t3-completion.json`) with their reports `python-t3.json` and `python-t3-completion.json`; the
numerical demonstrations `Revision/pairing/kohn_sham/numerics/t3_rust_demo.py`, `t3_reference_demo.py` and
the report `t3-rust-demo.json`; the publication tests `Revision/tests/test_pair_creation_proofs_publication.py`
(reads `t3-theory.json`, `wolfram-t3.json` and `python-t3.json`), `test_dirac16complex_field_theory_publication.py`
(reads `wolfram-t3.json` and `python-t3.json`) and `test_kohn_sham_deflating_field_publication.py`; the
provenance files `Revision/algebra/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` and
`Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md` (name the set as a consumer of their outputs); the index `provenance/EXECUTION_PROVENANCE_INDEX.md` (row 5) and its test
`tests/test_execution_provenance.py`; the textbook (`Revision/textbook/`: chapters 00, 13, 19, 20 and 22,
`UNIVERSES_IN_PAIRS_TEXTBOOK.md` and `.tex`, and the notebooks 00c, 13b, 19a and 19b with their sources and
provenance files); `HANDOFF.md`. Left out on purpose: the workflow scripts and records under
`Revision/workflows/`, which produced or reviewed the set and do not cite its results. None of these files
quotes the sha256 or the detail text of `wolfram-t3.json` (`git grep` for its old sha256 `904fd1dc` finds only
workflow records and this file, and for the phrase `v_v unchanged, e_int unchanged` of its old detail text
nothing).

## 2. Files

### 2.1 The scripts

| file | sha256 | lines | bytes |
| --- | --- | --- | --- |
| `Revision/pairing/kohn_sham/wolfram/verify_t3.wls` | `0cde8c8f36914fbdcc991e11ae44bf26a17f7177d9c9757e58a37cd29ab787c8` | 250 | 27280 |
| `Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls` | `35605f5c29bb7e44a7ec10dd6f4e34f3aa5bec37c12d3bc9cd2fc1537fb2d227` | 140 | 17486 |

There is no package file: neither script loads a Wolfram package (`Get`/`Needs` are not used) and neither
takes command-line arguments. Each finds its input and output files relative to its own location
(`$InputFileName`), so it does not depend on the folder you run it from - but `wolframscript` must find the
script itself, so the commands of section 3.5 are typed in the repository root.

### 2.2 Inputs (read only, never modified)

| file | sha256 | lines | bytes | what is read | produced by |
| --- | --- | --- | --- | --- | --- |
| `Revision/kohn_sham/ks-theory.json` | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` | 477 | 17278 | both scripts: `exchange.kohnShamPotentials` (`Meff_coefficient_of_lambda_S` = `15/16`, `vv_coefficient_of_lambda_n` = `-1/16`, the formulas `Meff`, `vv`, `e_int`); `verify_t3.wls` also `blockBasis.unnormalisedColumns2Sqrt2V` and `blockBasis.labels`; the completion also `exchange.expectationRule` | `Revision/kohn_sham/theory/verify_ks_theory.wls` |
| `Revision/algebra/gammas.json` | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 | `gamma` (gamma^(x1) ... gamma^(x8)) and `Gamma` (the chirality); the completion also `B` and `C` | `Revision/algebra/wolfram/verify_algebra.wls` |

In `verify_t3.wls` checks 6, 7 and 10 use the Kohn-Sham coefficients read from `ks-theory.json` and check 9
uses the block basis and the matrices; checks 1 to 5 and 8 use only formulas written in the script. Note: the
file `ks-theory.json` writes every `/` as `\/` (for example `"15\/16"`); a JSON reader turns this back into
`15/16`.

### 2.3 Outputs (written on every run, LF line endings, deterministic)

| file | written by | sha256 | lines | bytes | content |
| --- | --- | --- | --- | --- | --- |
| `Revision/pairing/kohn_sham/t3-theory.json` | `verify_t3.wls` | `f1ae1e8ab2248bde43526fc2e1624f0a74aacbe4a0b7f3f3a8954a3048dbcdd7` | 55 | 7053 | the theorem record: hypotheses H1-H6, statement S1-S5, proof, the 10 check names, what is not established; line 9 `  "status": "all checks of the report passed",` |
| `Revision/pairing/kohn_sham/reports/wolfram-t3.json` | `verify_t3.wls` | `b0903ca4ffd2520b5dfaa68e5cd9e67b2a6e393722f49139077f275287a8f7c6` | 19 | 7193 | the report; line 6 `  "summary": {"passed": 10, "failed": 0, "total": 10},`; name, verdict and detail of each check |
| `Revision/pairing/kohn_sham/t3-completion.json` | `verify_t3_completion.wls` | `2999ced97a67713cb4be6ebb05531d45fabb9bdc2712c39ebd6fe32227156373` | 38 | 7222 | the completion record: S6, the filling convention for the pair, the PRESCRIBED BACKGROUND, the adversarial verification, the 3 check names, what is not established; line 6 `  "status": "all checks of the report passed",` |
| `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json` | `verify_t3_completion.wls` | `91bd5b86273d617d5a2722947ec033426b4a4c0cd7603a18544013fc81b07b7f` | 12 | 3309 | the report; line 6 `  "summary": {"passed": 3, "failed": 0, "total": 3},` |

The four files contain only fixed text and integer check counts (no dates, times, machine names or
floating-point numbers), so a passing run reproduces them byte for byte. If a check fails, the counts, the
verdict of that check and the `status` line of the record change. `wolfram-t3.json` had the sha256
`904fd1dcb77a6772f7ef21dcabe10d194d8086f509e17df54830bd7f7fb999ab` (6448 bytes) before the fix of section 1.5.

### 2.4 Downstream files (not part of the set; section 3.8)

| file | sha256 | lines | bytes |
| --- | --- | --- | --- |
| `Revision/pairing/kohn_sham/python/check_t3.py` | `7458fcb9b3b563e79554333a1acb5d3c9b80f4c6b66b3d7ecaa93d7c52723bca` | 324 | 20491 |
| `Revision/pairing/kohn_sham/python/check_t3_completion.py` | `3318070471cf03f178e07958bb5d0192d89b93981220956545f11677da7d163e` | 223 | 14131 |
| `Revision/pairing/kohn_sham/reports/python-t3.json` (written by `check_t3.py`) | `4924b8ebd2d294c53eab12977012880446759d6ff53526620b3764dd9d875481` | 85 | 7634 |
| `Revision/pairing/kohn_sham/reports/python-t3-completion.json` (written by `check_t3_completion.py`) | `c80011b6ea374832572e8a39a918064f00a4c27a5f8c19cedea1b187c73487c3` | 49 | 4839 |

`check_t3.py` also reads `Revision/kohn_sham/reports/ks-rust-solver.json`; `check_t3_completion.py` also reads
`Revision/pairing/kohn_sham/reports/t3-rust-demo.json` and `t3-reference-demo.json` (committed results of the
numerical demonstrations, produced by `Revision/pairing/kohn_sham/numerics/`, not by this set).

## 3. How to run it (complete instructions)

### 3.1 What you need

- A computer with Windows 10 or 11, macOS, or Linux, at least 10 GB of free disk space for the installed
  Wolfram program (the Wolfram 15.0.1 installation folder of the verification machine holds 54355 files with
  together about 9.3 GB = 8.7 GiB), plus room for the downloaded installer file itself (the download page
  shows its size; you can delete it after the installation), and an internet connection for the installation
  (the runs themselves need no network).
- Wolfram: either the free Wolfram Engine for Developers or a Mathematica / Wolfram desktop licence. Both
  contain the command-line program `wolframscript`, which is what runs the scripts.
- Git, to download the repository.

The scripts use only long-established Wolfram Language functions (associations, `Import` with the JSON
format `"RawJSON"`, `ToExpression`, `StringCases`, `Simplify`, `ComplexExpand`, binary file writing). They
were verified with Wolfram 15.0.1 and WolframScript 1.14.0 only (section 6); with another version the checks
are expected to pass and to give the same four files, but that was not tested.

### 3.2 Install Wolfram

Option A, the free Wolfram Engine for Developers:

1. In a web browser open https://www.wolfram.com/engine/ and click the download button for your system. You
   may be asked to sign in with a Wolfram ID; if you have none, create one there (free; you type your own
   e-mail address and password - nobody else should do this for you).
2. Get the free licence: on the same page click "Get your license", sign in with your Wolfram ID and accept
   the terms of use yourself (free); the page says that the free licence is obtained this way. The activation
   in section 3.3 needs this licence, so do this step before section 3.3.
3. Install the downloaded program:
   - Windows: run the downloaded `.exe` installer and accept the defaults. It installs WolframScript and
     puts it on the PATH (the default folder is `C:\Program Files\Wolfram Research\WolframScript\`).
   - macOS: open the downloaded `.dmg` file and follow its instructions (drag the application into
     `Applications`).
   - Linux: open a terminal in the folder of the download and run `sudo bash ./<name of the downloaded .sh file>`,
     accepting the defaults.
4. If, after the installation, `wolframscript -version` (section 3.3) says that the command is not found,
   download WolframScript itself from https://www.wolfram.com/wolframscript/ , install it, close the
   terminal and open a new one.

Option B, Mathematica or the Wolfram desktop application: install it as its licence describes. WolframScript
comes with it. On macOS it lies inside the application bundle (`Contents/MacOS/wolframscript`); if the
command is not found, install WolframScript from https://www.wolfram.com/wolframscript/ as in step 4 above.

### 3.3 Open a terminal and activate WolframScript

- Windows: press the Windows key, type `PowerShell`, press Enter.
- macOS: press Cmd + Space, type `Terminal`, press Enter.
- Linux: open the application "Terminal".

Type the following two commands, pressing Enter after each:

```text
wolframscript -version
wolframscript -code 1+1
```

The first prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)` (your version and
system may differ). The second must print `2`. With the free Wolfram Engine the first `wolframscript -code`
asks you to activate: type your Wolfram ID (e-mail) and password yourself when asked. If it does not ask but
prints a licensing error, run `wolframscript -activate` yourself and then repeat `wolframscript -code 1+1`.

### 3.4 Install Git and download the repository

1. Install Git: Windows: download it from https://git-scm.com/downloads and accept the defaults; macOS: type
   `git --version` in the Terminal and accept the offer to install the command-line tools; Linux: install the
   package `git` with your distribution's package manager (for example `sudo apt install git`).
   Windows: a PowerShell (or Command Prompt) window that was already open during the Git installation does
   not yet know the new program, because an installer changes the search path (PATH) only for programs started
   afterwards. So after installing Git close PowerShell, open a new PowerShell window (Windows key, type
   `PowerShell`, Enter) and check with `git --version`; it must print a line such as
   `git version 2.51.2.windows.1` (your version may differ).
2. In the terminal, go to the folder where you want the repository (for example your home folder) and type:

```text
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The second command moves you into the repository root, the folder that contains the folder `Revision`. All
commands below are typed in this folder. (The repository stores every file byte for byte; no line-ending
conversion happens, even on Windows.)

### 3.5 Run the two scripts

Windows PowerShell (from the repository root):

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
$LASTEXITCODE
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
$LASTEXITCODE
```

macOS or Linux Terminal (from the repository root):

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
echo $?
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
echo $?
```

If you use the older Windows "Command Prompt" (cmd.exe) instead of PowerShell, the `wolframscript` lines are
the same and the other two lines are `echo %ERRORLEVEL%`.

Each `wolframscript` line runs one script; each takes about 3 to 5 seconds on a quiet machine (most of it is
starting Wolfram) and up to about 14 seconds on a heavily loaded one (section 4.4); only the time changes,
the printed result and the output files stay the same. The line after it prints the exit code of the run:
`0` means every check passed, `1` means at least one check failed or the run stopped with an `ERROR` line
(section 4.2). The runs need no input from you and open no window.

### 3.6 Check the result

1. Read the check counts in the two reports.
   - Windows PowerShell:

     ```text
     (Get-Content Revision/pairing/kohn_sham/reports/wolfram-t3.json -Raw | ConvertFrom-Json).summary
     (Get-Content Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json -Raw | ConvertFrom-Json).summary
     ```

     print a small table with the columns `passed failed total` and the values `10 0 10` and `3 0 3`.
   - macOS or Linux:

     ```text
     grep '"summary"' Revision/pairing/kohn_sham/reports/wolfram-t3.json Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json
     ```

     prints `Revision/pairing/kohn_sham/reports/wolfram-t3.json:  "summary": {"passed": 10, "failed": 0, "total": 10},`
     and `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json:  "summary": {"passed": 3, "failed": 0, "total": 3},`.
   - Windows Command Prompt (cmd.exe; the PowerShell, `grep`, `sha256sum` and `shasum` commands of this
     section do not exist there):

     ```text
     findstr /c:"summary" Revision\pairing\kohn_sham\reports\wolfram-t3.json Revision\pairing\kohn_sham\reports\wolfram-t3-completion.json
     ```

     prints the same two lines with backslashes in the file names.
2. Confirm that the regenerated files are byte-identical to the committed ones (the same two commands in
   PowerShell, Command Prompt, macOS and Linux):

   ```text
   git status --porcelain
   git diff --exit-code --stat
   ```

   Both commands print nothing when the four output files are unchanged (the files are rewritten, but with the
   same bytes, so Git sees no change). The only exception: in a copy of the repository into which newer, not
   yet committed versions of files of this set (this provenance file, a script) were copied by hand,
   `git status --porcelain` prints one line for each such file (`?? <file>` if it is new, ` M <file>` if it
   replaces a committed version), `git diff --exit-code --stat` also names those files (paths may be
   shortened, for example `.../kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md | 57 +++++-----`) and then
   `<n> files changed, ...` (exit code `1`), and an output that a newer script writes differently appears as
   well. Compare such an output with the sha256 of section 2.3 (step 3) instead.
3. Optionally compare the sha256 checksums with section 2.3: Windows PowerShell

   ```text
   Get-FileHash -Algorithm SHA256 Revision/pairing/kohn_sham/t3-theory.json, Revision/pairing/kohn_sham/reports/wolfram-t3.json, Revision/pairing/kohn_sham/t3-completion.json, Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json
   ```

   (it prints the hashes in capital letters); Linux
   `sha256sum Revision/pairing/kohn_sham/t3-theory.json Revision/pairing/kohn_sham/reports/wolfram-t3.json Revision/pairing/kohn_sham/t3-completion.json Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`;
   macOS the same with `shasum -a 256` instead of `sha256sum`; Windows Command Prompt (cmd.exe), one file per
   command:

   ```text
   certutil -hashfile Revision\pairing\kohn_sham\t3-theory.json SHA256
   certutil -hashfile Revision\pairing\kohn_sham\reports\wolfram-t3.json SHA256
   certutil -hashfile Revision\pairing\kohn_sham\t3-completion.json SHA256
   certutil -hashfile Revision\pairing\kohn_sham\reports\wolfram-t3-completion.json SHA256
   ```

   Each prints `SHA256 hash of <file>:`, then the hash in small letters (for example
   `f1ae1e8ab2248bde43526fc2e1624f0a74aacbe4a0b7f3f3a8954a3048dbcdd7` for `t3-theory.json`), then
   `CertUtil: -hashfile command completed successfully.`

### 3.7 What to do if it fails

| what you see | cause | what to do |
| --- | --- | --- |
| `wolframscript : The term 'wolframscript' is not recognized as the name of a cmdlet, ...` (Windows PowerShell 5.1, the one that opens by default) or `wolframscript: The term 'wolframscript' is not recognized as a name of a cmdlet, ...` (PowerShell 7); `'wolframscript' is not recognized as an internal or external command, operable program or batch file.` (Command Prompt); `zsh: command not found: wolframscript` (macOS Terminal, whose shell is zsh); `bash: wolframscript: command not found` (Linux with bash; some distributions print a longer "command not found" hint instead) | WolframScript is not installed or not on the PATH | install it (section 3.2, step 4), then close the terminal and open a new one |
| the same messages for `git` instead of `wolframscript` (for example `git : The term 'git' is not recognized ...`, `zsh: command not found: git`) | Git is not installed, or (Windows) the terminal window was already open when Git was installed | install Git (section 3.4, step 1), close the terminal, open a new one and check with `git --version` |
| a request to activate, or a message about a missing or invalid licence | WolframScript is not activated | run `wolframscript -activate` yourself, sign in with your own Wolfram ID, then repeat section 3.3 |
| a message that no licence or no kernel is available | another Wolfram program uses the kernel(s) your licence allows | close other Wolfram programs and notebooks and run again (each script starts one kernel) |
| `Failed to open file at path: Revision/pairing/kohn_sham/wolfram/verify_t3.wls` (or `.../verify_t3_completion.wls`) | you are not in the repository root | `cd` into the folder `Dirac_claude` (the one that contains `Revision`) and run again. Note: in this case `wolframscript` still returns exit code `0` although nothing was run, so always look for the line `10/10 checks passed` (or `3/3 checks passed`) |
| `verify_t3.wls` prints only `ERROR  input file not found: <path>` or `ERROR  input file is not a JSON object: <path>`, exit code `1` | `Revision/kohn_sham/ks-theory.json` or `Revision/algebra/gammas.json` is missing, moved or damaged; nothing was written | restore it with `git checkout -- Revision/kohn_sham/ks-theory.json Revision/algebra/gammas.json` and run again |
| `verify_t3.wls` prints only `ERROR  cannot read the Kohn-Sham potentials (exchange.kohnShamPotentials: ...) as exact numbers from <path>`, exit code `1` | the coefficients or the formula `e_int` in `ks-theory.json` were changed into something that is not an exact number or not of the form `(p/q) lambda S^2 - (p/q) lambda n^2`; nothing was written | restore `ks-theory.json` as in the previous row |
| `verify_t3.wls` prints the check lines and then `ERROR  cannot write <path>`, exit code `1` | an output file cannot be written (read-only, locked by another program, or a folder of that name is in its place); `t3-theory.json` is written before the report, so it may already have been rewritten | make the file writable or remove what blocks it, restore the outputs (section 5.4) and run again |
| `verify_t3_completion.wls` prints `Import::nffil: File ...ks-theory.json not found during Import.` (or `...gammas.json...`) and further messages (`ToExpression::notstrbox`, `Part::partw`, ...), `FAIL` lines, `1/3 checks passed` (`ks-theory.json` missing) or `2/3 checks passed` (`gammas.json` missing), exit code `1` | an input file is missing or was moved; the completion has no `ERROR` exit and writes its two outputs with the failing counts | restore the input as above, restore the outputs (section 5.4) and run again |
| any other `FAIL  ...` line, fewer than `10/10` (or `3/3`), exit code `1` | an input or a script differs from the committed version, or a different Wolfram version simplifies an expression differently | run `git status` to see which files changed; restore changed files with `git checkout -- <file>`; if the failure remains with the committed files, do not edit anything: record the Wolfram version and report the failing check name. To print the version: PowerShell, macOS and Linux: `wolframscript -code '$Version'` (with the single quotes); Command Prompt: `wolframscript -code $Version` (no quotes; with single quotes Command Prompt prints `ToExpression::sntx: Invalid syntax ...` and `$Failed`). It prints a line such as `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` |
| `git status --porcelain` lists an output after a run that printed `10/10` (or `3/3`) | a script file was changed (for example opened and saved in the Wolfram desktop application) | compare its sha256 with section 2.1; restore it with `git checkout -- <script>` and run again |

Do not run the scripts from inside a Wolfram notebook: their last line is `Exit[...]`, which would close the
notebook's kernel. Use the terminal as described above.

### 3.8 Optional next step: the independent sympy checkers

They are not part of this set, but they read its outputs. They need Python 3 and the Python package sympy.
Run them AFTER the two Wolfram scripts, in this order (`check_t3_completion.py` reads `python-t3.json`, which
`check_t3.py` writes). They were verified with Python 3.14.5 and sympy 1.14.0 (with mpmath 1.3.0) on Windows;
`check_t3.py` also with Python 3.14.6 (Homebrew) and sympy 1.14.0 on Ubuntu 24.04 (under WSL, 2026-10-02).

1. Get Python (skip this if `python --version` on Windows or `python3 --version` on macOS/Linux already
   prints `Python 3.` followed by a version number; a message that Python or the command was not found means
   that Python is not installed):
   - Windows: download the installer from https://www.python.org/downloads/ and run it; if it offers the
     option "Add python.exe to PATH", tick it. Then close PowerShell, open a new PowerShell window and check
     with `python --version`.
   - macOS: download the macOS installer from https://www.python.org/downloads/ and run it; then check with
     `python3 --version` in a new Terminal window.
   - Linux: install your distribution's packages `python3` and `python3-venv` (Debian, Ubuntu, Kali:
     `sudo apt install python3 python3-venv`). Without `python3-venv` the next step fails with
     `The virtual environment was not created successfully because ensurepip is not available.`
2. Create a private Python environment (a folder `.venv` in the repository root), install sympy into it and
   run the checkers, from the repository root. Do not install sympy into the system's Python with a plain
   `pip install`: on current Linux distributions and with Homebrew Python this is refused with
   `error: externally-managed-environment`.
   - Windows PowerShell or Command Prompt:

     ```text
     python -m venv .venv
     .venv\Scripts\python -m pip install sympy==1.14.0
     .venv\Scripts\python Revision/pairing/kohn_sham/python/check_t3.py
     .venv\Scripts\python Revision/pairing/kohn_sham/python/check_t3_completion.py
     ```

   - macOS or Linux:

     ```text
     python3 -m venv .venv
     .venv/bin/python -m pip install sympy==1.14.0
     .venv/bin/python Revision/pairing/kohn_sham/python/check_t3.py
     .venv/bin/python Revision/pairing/kohn_sham/python/check_t3_completion.py
     ```

   These commands call the Python of the private environment directly, so you do not need to "activate"
   it. (If you prefer to activate it: macOS/Linux `. .venv/bin/activate`, Windows PowerShell
   `.venv\Scripts\Activate.ps1`; on a new Windows computer PowerShell may refuse the latter with a message
   that running scripts is disabled; then simply use the commands above. After activating, `python` alone
   means the environment's Python.) If Python with sympy is already installed on your computer, you may run
   the two checkers with it instead (`python` on Windows, `python3` on macOS/Linux).

The `pip install` line downloads sympy (6.3 MB) and mpmath (536 kB) from the internet (22 to 28 s on the
verification machine) and prints `Successfully installed mpmath-1.3.0 sympy-1.14.0`; a note
`[notice] A new release of pip is available ...` may also appear and can be ignored.
`check_t3.py` prints 13 lines such as `[   0.1s] PASS T3.block_hamiltonian_map` and as its last line
`pass 13 fail 0; <time>s; wrote <full path of the repository>\Revision\pairing\kohn_sham\reports\python-t3.json`
(Windows, backslashes; macOS/Linux with forward slashes), exits with `0` and rewrites `python-t3.json`
byte-identically. `check_t3_completion.py` prints 7 `PASS` lines (`T3C.mean_field_coefficients_from_ks_theory`,
`T3C.filling_convention_mapped`, `T3C.krein_rule_16_component`, `T3C.t3_reports_pass`,
`T3C.rust_demo_numerical_demonstration`, `T3C.reference_demo_numerical_demonstration`, `compare.t3_completion`)
and `pass 7 fail 0; <time>s; wrote <...>python-t3-completion.json`, exits with `0` and rewrites
`python-t3-completion.json` byte-identically (sha256 of both in section 2.4). Each checker takes about 1 to
2 seconds (longer on a busy machine or on the first run after installing). The folder `.venv` stays in the
repository root; Python 3.13 and newer put a file `.gitignore` inside it, so `git status` does not show it
(with an older Python, `git status` shows `?? .venv/`). You may delete the folder `.venv` when you no longer
need it.

## 4. Expected output

### 4.1 Printed on the screen

`verify_t3.wls` prints exactly these 11 lines (nothing is printed as an error):

```text
PASS  T3_block_hamiltonian_map
PASS  T3_ode_map
PASS  T3_tip_condition_map
PASS  T3_brane_parities_exchanged
PASS  T3_orbital_densities
PASS  T3_mean_field_map
PASS  T3_energies_and_emt_profiles_equal
PASS  T3_exact_k0_spectra
PASS  T3_Gamma_is_the_block_map
PASS  T3_z2_mirror_copy_carries_minus_m_plus_lambda
10/10 checks passed; time 0.4 s
```

Only the time `<t>` in the last line `10/10 checks passed; time <t> s` changes from run to run: it is the
computing time inside Wolfram, without the start of Wolfram (0.4 to 0.5 s on a quiet machine on 2026-10-08;
up to 7.2 s on a heavily loaded machine, section 4.4). Wolfram prints the rounded number in its own way, for
example `time 0.5 s`, `time 1. s`, `time 0.30000000000000004 s` or `time 1.2000000000000002 s`. This is
harmless: the time is printed only on the screen and never enters a file.

`verify_t3_completion.wls` prints exactly these 4 lines (no time):

```text
PASS  T3C_mean_field_coefficients_from_ks_theory
PASS  T3C_filling_convention_mapped
PASS  T3C_krein_rule_16_component
3/3 checks passed
```

The lines appear one after the other while the checks run.

### 4.2 Exit codes and the ERROR exits

Both scripts exit with `0` when all their checks pass and with `1` when at least one fails. In addition
`verify_t3.wls` stops with exit code `1` and a single line starting with `ERROR  ` in these cases (verified
in section 6.5):

- `ERROR  input file not found: <path>` - `ks-theory.json` or `gammas.json` is missing; nothing is written;
- `ERROR  input file is not a JSON object: <path>` - an input is not valid JSON; nothing is written;
- `ERROR  cannot read the Kohn-Sham potentials (exchange.kohnShamPotentials: Meff_coefficient_of_lambda_S, vv_coefficient_of_lambda_n, e_int) as exact numbers from <path>`
  - nothing is written;
- `ERROR  cannot write <path>` - after the check lines, when an output cannot be written (`t3-theory.json`
  is written first, so it may already be rewritten when the report cannot be).

`verify_t3_completion.wls` has no `ERROR` exit (section 3.7). Caution for both: a wrong script path gives
exit code `0` (section 3.7).

### 4.3 Files written

The four files of section 2.3, with the sha256, lines and bytes given there. After a failing check the
`status` line of the record reads `"status": "SOME CHECKS FAILED - see the report",` and the summary line of
the report shows the failure count.

### 4.4 Run time and memory

On the verification machine (Windows 11, 24 logical cores), 2026-10-08, quiet (0 to 2 Wolfram processes of
other jobs): `verify_t3.wls` 2.97 to 3.92 s wall-clock time per run (printed time 0.4 to 0.5 s; the
negative-test runs of section 6.5, which stop earlier or fail a check, 2.4 to 4.7 s);
`verify_t3_completion.wls` 3.01 to 3.44 s; `check_t3.py` 1.11 to 1.15 s; `check_t3_completion.py` 0.72 to
0.74 s. The exact list is in section 6.5. Earlier measurements of `verify_t3.wls` (sections 6.1 to 6.4, the
version before the fix, which does the same computation): about 2 to 8 seconds, typically 3 to 5, and on a
heavily loaded machine (10 to 26 Wolfram processes of other jobs) up to about 14 seconds with printed times up
to 7.2 s.

Peak memory (working set), 2026-10-08, both scripts alike: the Wolfram kernel 167.0 to 167.1 MB, the
short-lived licence query 74.5 to 74.6 MB, `wolframscript` 19.0 to 19.1 MB (section 6.5; read through the
open process handle after each process ended, which gives the exact peak). Earlier values for
`verify_t3.wls`: kernel 148 to 157 MB, licence query about 68 MB, `wolframscript` about 17 MB (sections 6.1
to 6.4).

## 5. Side effects

### 5.1 Files created or overwritten in the repository

- OVERWRITTEN on every run (all four are committed files): `verify_t3.wls` rewrites
  `Revision/pairing/kohn_sham/t3-theory.json` and `Revision/pairing/kohn_sham/reports/wolfram-t3.json`;
  `verify_t3_completion.wls` rewrites `Revision/pairing/kohn_sham/t3-completion.json` and
  `Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json`. A passing run writes the same bytes, so
  only their modification times change and `git status` stays clean.
- CREATED only if missing: the folder `Revision/pairing/kohn_sham/reports/` (each script creates it before
  writing its report).
- Nothing else in the repository is created, changed or deleted (verified with `git status --porcelain --ignored`
  and with the sha256 of every file of a clone before and after the runs, section 6.5).

### 5.2 Outside the repository

- Processes: `wolframscript` first starts a short-lived `wolfram.exe` that queries the licence
  (`wolfram.exe -wlbanner -licenseinfo`; it lived 0.105 to 0.134 s in the quiet runs of 2026-10-08, up to
  0.477 s in another run, peak working set about 75 MB) and then the Wolfram kernel (on Windows the process
  `wolfram.exe` of Wolfram 15, started as `wolfram.exe -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`;
  older versions call the kernel `WolframKernel`), 0.17 to 0.22 s after its own start in the four monitored
  complete runs of section 6.5 (0.55 s in one of the kill tests). Each
  script starts one kernel. When `wolframscript` is started without a console window (as by the monitor of
  section 6.5), Windows also attaches a console host `conhost.exe` (8.2 MB) to it. The kernel ends when the
  script ends; no process is left running (verified in every monitored run of sections 6.1 to 6.5).
- Interrupted run: if you stop a run by killing `wolframscript` (tested with `Process.Kill` 1.0 and 2.3 s
  after the start, both scripts, section 6.5; and in sections 6.2 and 6.3 for the earlier version), the
  kernel ends as well and no Wolfram process is left running; no output file is written or changed (the
  scripts write their outputs only at the very end), and the empty temporary file described next stays
  behind.
- Temporary files: on every run `wolframscript` creates two temporary files in the folder
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (on the verification machine
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`), each named `tmp_` followed
  by 10 random letters and digits (for example `tmp_NnpCUtx4xQ`): an empty one right when it starts (20 to
  45 ms after the start), and one that receives the printed output while the checks run (2.09 to 2.51 s after
  the start; at the end 354 bytes for `verify_t3.wls` when the time is printed as `0.4` or `0.5`, other
  lengths for other printed times, and 141 bytes for the completion). It deletes both when the run ends
  normally. If a run is interrupted, the empty file remains (seen after every kill test of 2026-10-08), and a
  partly filled output file can remain too (seen on 2026-10-02: a 166-byte file with the first six `PASS`
  lines after a kill 3 s after the start); they are harmless and may be deleted by hand. The same folder may
  also hold leftover `tmp_*` files of other, earlier `wolframscript` calls. The corresponding folder on macOS
  and Linux was not verified. Nothing of these runs was found in the system temporary folder (`%TEMP%`;
  sections 6.1 and 6.2).
- Wolfram's own housekeeping, not caused by the scripts themselves (sections 6.1 to 6.3): every
  `wolframscript` call rewrote its settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` with the
  same 238 bytes, and the kernel start touched the folder `%APPDATA%\Wolfram\Paclets\Temporary` (only its
  time stamp changed). On macOS and Linux the corresponding Wolfram user folder is used.
- Network: neither script contains a network command. In the socket-monitored runs of `verify_t3.wls`
  (sections 6.1 to 6.3) the kernel held only loopback connections 127.0.0.1 <-> 127.0.0.1 (its internal link)
  and, with the same port, a TCP socket in state `Bound` on 0.0.0.0 (not listening, no remote end), for
  example `127.0.0.1:52970 -> 127.0.0.1:52971 Established`, `127.0.0.1:52971 -> 127.0.0.1:52970 Established`
  and `0.0.0.0:52971 -> 0.0.0.0:0 Bound`; no UDP endpoint and no connection to another computer.
  The completion script was not socket-monitored. (Activating WolframScript, section 3.3, does use the
  internet; that is a one-time step, not part of a run.)

### 5.3 Effects on other parts of the repository

The readers of section 1.6 read the committed outputs; a passing run changes nothing for them. A failing run
leaves a record with the status `SOME CHECKS FAILED - see the report` and a report with fewer passes; restore
them (section 5.4) before running the sympy checkers or the publication tests.

### 5.4 How to restore the committed state

From the repository root:

```text
git checkout -- Revision/pairing/kohn_sham/t3-theory.json Revision/pairing/kohn_sham/reports/wolfram-t3.json Revision/pairing/kohn_sham/t3-completion.json Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json
```

If you deleted the folder `Revision/pairing/kohn_sham/reports/`, restore the whole folder with
`git checkout -- Revision/pairing/kohn_sham/reports`.

## 6. Verification record

Sections 6.1 to 6.4 are the record of the EARLIER version of `verify_t3.wls` (sha256
`ea6c436f667c465727967c8b9664e2425227be0d71a55ca36a36e13a3da497d8`, 207 lines, 23070 bytes; its report
`wolfram-t3.json` then had sha256 `904fd1dcb77a6772f7ef21dcabe10d194d8086f509e17df54830bd7f7fb999ab`, 19
lines, 6448 bytes); they are kept unchanged as history. Where they say "section 2" they mean those values
(the theorem record `t3-theory.json` and the two inputs are unchanged since). Where they discuss the `v_v`
term of check 6 (line 79), they describe the defect fixed in section 6.5. The completion script did not
exist then. Section 6.5 is the verification of the whole set as it is now.

### 6.1 First verification

- Date: 2026-10-02.
- Commits verified: `45d47343ae480df46e06689ed822b8f9a88a8030` (fresh clone 1) and
  `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (fresh clone 2; the remote `main` at the time of verification).
  The only file that differs between the two commits is `Revision/tests/test_pair_creation_proofs_publication.py`,
  so the script, its two inputs and its two committed outputs are identical (same sha256 as in section 2) in
  both.
- Environment: Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 logical cores; WolframScript
  1.14.0; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), `$SystemID` `Windows-x86-64`,
  Professional licence; Git 2.51.2.windows.1; for the optional checker of section 3.8: Python 3.14.5 with
  sympy 1.14.0 (the machine's installation, not a fresh virtual environment).
- Each clone was made with `git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch
  folder; no uncommitted file was copied in (none is needed by this set), except a copy of this provenance
  file into clone 3, to follow its instructions literally.

| run | clone | how | exit code | printed verdict | wall time | outputs vs committed | outputs vs the other run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 (`45d4734`) | PowerShell, repository root, command of section 3.5 | 0 | 10 PASS lines, `10/10 checks passed; time 0.5 s` | 4.56 s | both byte-identical | - |
| 2 | 1 (`45d4734`) | same, second run on top of run 1 | 0 | `10/10 checks passed; time 0.4 s` | 4.65 s | both byte-identical | both identical to run 1 |
| 3 | 2 (`c2b33cc`) | PowerShell, repository root, after DELETING `t3-theory.json` and the folder `reports/` | 0 | `10/10 checks passed; time 0.7000000000000001 s` | 4.13 s | both byte-identical (folder recreated) | - |
| 4 | 2 (`c2b33cc`) | PowerShell, repository root, after `git checkout -- Revision/pairing/kohn_sham` | 0 | `10/10 checks passed; time 0.5 s` | 3.57 s | both byte-identical | both identical to runs 1 and 3 |
| 5 | 2 (`c2b33cc`) | Git Bash, run from inside `Revision/pairing/kohn_sham/wolfram/` as `wolframscript -file verify_t3.wls` | 0 | `10/10 checks passed; time 0.4 s` | not measured | both byte-identical | - |
| 6 | 2 (`c2b33cc`) | PowerShell, repository root, the commands of sections 3.5 and 3.6 (then once more under `Measure-Command`) | 0 (`$LASTEXITCODE`) | `10/10 checks passed; time 0.5 s` | 3.23 s and 4.15 s | both byte-identical (`git status --porcelain` and `git diff --exit-code` empty, `Get-FileHash` as in section 2.3) | - |
| 7 | 3 (`c2b33cc`, a third fresh clone plus a copy of this file) | PowerShell, repository root, following sections 3.5 and 3.6 literally | 0 (`$LASTEXITCODE`) | `10/10 checks passed; time 1. s` | 4.64 s | both byte-identical (summary table `10 0 10`, `git diff --exit-code` empty, `Get-FileHash` as in section 2.3; `git status --porcelain` showed only `?? ...WOLFRAMSCRIPT_PROVENANCE.md`) | identical to runs 1 to 6 |
| 8 | 3 (`c2b33cc`) | Git Bash, repository root, following the macOS/Linux commands of sections 3.5 and 3.6 literally (`echo $?`, `grep '"summary"'`, `sha256sum`) | 0 | `10/10 checks passed; time 1.1 s` | 4.80 s | both byte-identical (the `grep` printed `  "summary": {"passed": 10, "failed": 0, "total": 10},`) | identical to run 7 |

- Check counts: 10 of 10 PASS in every run (report summary `{"passed": 10, "failed": 0, "total": 10}`).
  Standard error was empty in every run. After every passing run in clones 1 and 2,
  `git status --porcelain --ignored` was empty.
- Peak working set (runs 1 to 4, polled every 0.1 s): Wolfram kernel 148.1 to 148.2 MB, `wolframscript`
  16.7 MB.
- Run 9 (clone 3, Windows Command Prompt cmd.exe, repository root, the command of section 3.5 followed by
  `echo %ERRORLEVEL%`): `10/10 checks passed; time 1. s`, then `0`; outputs byte-identical.
- Failure tests (in a separate scratch copy, restored afterwards): (a) `ks-theory.json` moved away: the
  messages `Import::nffil` and `Part::...`, `FAIL  T3_Gamma_is_the_block_map`, `9/10 checks passed`, exit
  code 1, report summary `{"passed": 9, "failed": 1, "total": 10}`, theorem status
  `SOME CHECKS FAILED - see the report`; (b) `gammas.json` moved away: the same, `9/10 checks passed`, exit
  code 1; (c) run from a folder that is not the repository root: `Failed to open file at path: ...`, exit
  code 0, nothing written.
- Downstream: in clone 2 after run 5, `python Revision/pairing/kohn_sham/python/check_t3.py` gave `pass 13 fail 0`, exit
  code 0, 1.39 s, and rewrote `Revision/pairing/kohn_sham/reports/python-t3.json` byte-identically
  (sha256 `4924b8ebd2d294c53eab12977012880446759d6ff53526620b3764dd9d875481`).
- Fixes made: none (no execution defect was found; the script, its inputs and its outputs are unchanged).
- Open discrepancies: none. Not verified: macOS and Linux (the script uses only portable path functions,
  `FileNameJoin` and `DirectoryName`, and was also run from Git Bash on Windows), and Wolfram versions other
  than 15.0.1.

### 6.2 Re-verification after the review of this file

An independent review of this file (2026-10-02) reported 12 points about the text (not about the script or
its results). Each point was re-checked in fresh clones and this file was corrected; the script, its inputs
and its committed outputs were not changed.

- Date: 2026-10-02. Commit verified: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the remote `main` at that
  time), two new fresh clones (`git clone https://github.com/once-ere/Dirac_claude.git`; clone A used for the
  measurements, clone B plus a copy of this corrected file used to follow sections 3.5, 3.6 and 3.8
  literally). No other uncommitted file was copied in. The sha256 of the script, its two inputs and its two
  committed outputs were again exactly those of section 2.
- Environment: as in section 6.1 (Windows 11 Pro for Workstations 10.0.26200, 24 logical cores,
  WolframScript 1.14.0, Wolfram 15.0.1, Professional licence; PowerShell 7.6.6 and Windows PowerShell
  5.1.26100; Python 3.14.5 with sympy 1.14.0 in a new private environment `.venv`); for the Linux side of
  section 3.8: Ubuntu 24.04 under WSL with Homebrew Python 3.14.6 and sympy 1.14.0 in a new private
  environment, and Kali Linux 2026.1 under WSL (Python 3.13.12, zsh 5.9) for the error messages.
- Run A (clone B, PowerShell, the commands of sections 3.5 and 3.6 literally): the 11 lines of section 4.1
  ending `10/10 checks passed; time 1. s`, `$LASTEXITCODE` `0`, 5.18 s; summary table `10 0 10`;
  `git status --porcelain` showed only `?? Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`;
  `git diff --exit-code --stat` empty (exit code 0); `Get-FileHash` gave the two sha256 of section 2.3.
- Run B (clone B, Command Prompt cmd.exe, the commands of sections 3.5 and 3.6 literally, including
  `findstr` and `certutil`): `10/10 checks passed; time 0.6000000000000001 s`, `echo %ERRORLEVEL%` `0`,
  3.80 s; `findstr` printed `  "summary": {"passed": 10, "failed": 0, "total": 10},`; `certutil` printed the
  two sha256 of section 2.3; `wolframscript -code $Version` printed
  `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`.
- Run C (clone B, Git Bash, the macOS/Linux commands of sections 3.5 and 3.6 literally, with the final
  version of this file): `10/10 checks passed; time 0.5 s`, `echo $?` `0`, 3.09 s; the `grep` printed
  `  "summary": {"passed": 10, "failed": 0, "total": 10},`; `git diff --exit-code --stat` empty;
  `sha256sum` gave the two sha256 of section 2.3.
- Byte identity: the two outputs after run A and after run B were byte-identical to each other and to the
  committed files (`cmp` against `git show HEAD:<file>`), and so were those after run C. In clone A, 16 more
  complete runs (PowerShell, Git Bash, monitored and unmonitored) all printed `10/10 checks passed` and
  exited with `0`; their outputs were checked after every unmonitored run (sha256) and after every batch of
  monitored runs (`git status --porcelain`, which lists every changed file, was empty) and were always
  byte-identical to the committed files. Standard error was empty in the 6 runs in which it was captured
  separately, and no error line appeared in any run.
- Check counts: 10 of 10 PASS in every run (report summary `{"passed": 10, "failed": 0, "total": 10}`).
- Processes (recorded with process-creation events in 5 runs): every run started
  `wolfram.exe -wlbanner -licenseinfo` and then the kernel `wolfram.exe -runfirst ... -mathlink`
  0.15 to 0.9 s later; no Wolfram process was left running after any run. Killing `wolframscript` after
  1, 1.5 and 3 s ended the kernel too; git status stayed clean (nothing had been written yet).
- Temporary files (folder polled every 20 to 50 ms in 6 runs): each run created an empty `tmp_*` file in
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` 15 to 40 ms after `wolframscript` started and
  a second `tmp_*` file that held the printed output (354 to 369 bytes); both were deleted at the end. After
  killing `wolframscript` after 1 s the empty file remained; after 3 s the empty file and a 166-byte output
  file (the first six `PASS` lines) remained. These leftover files of the test were deleted afterwards.
- Network (4 runs, polled every 30 ms): as described in section 5.2 (loopback connections plus a `Bound`
  socket on 0.0.0.0 with the same port; no UDP; no remote address).
- Command Prompt: `wolframscript -code '$Version'` printed `ToExpression::sntx: Invalid syntax in or before
  "'$Version'".` and `$Failed` with `ERRORLEVEL` 0; `wolframscript -code $Version` and
  `wolframscript -code "$Version"` printed the version. An unknown command printed
  `'notacommandxyz' is not recognized as an internal or external command, operable program or batch file.`
  (`ERRORLEVEL` 9009).
- Command-not-found messages: Windows PowerShell 5.1 `<name> : The term '<name>' is not recognized as the name
  of a cmdlet, ...`; PowerShell 7.6 `<name>: The term '<name>' is not recognized as a name of a cmdlet, ...`;
  zsh 5.9 at an interactive prompt without start-up files `zsh: command not found: wolframscript` (zsh is
  the default shell of macOS; macOS itself was not available); bash `bash: wolframscript: command not found`.
- Section 3.8 (clone B, Windows, literally): `python -m venv .venv` (6.2 s),
  `.venv\Scripts\python -m pip install sympy==1.14.0` (`Successfully installed mpmath-1.3.0 sympy-1.14.0`,
  21.7 s), `.venv\Scripts\python Revision/pairing/kohn_sham/python/check_t3.py` twice: 13 PASS lines,
  `pass 13 fail 0; ...; wrote C:\...\Revision\pairing\kohn_sham\reports\python-t3.json`, exit code 0, 1.55 s
  and 1.34 s; `python-t3.json` byte-identical (sha256 `4924b8eb...5481` as in section 3.8); `git status
  --porcelain --ignored` showed `!! .venv/` (ignored through the `.gitignore` that Python 3.14 writes into
  the environment). The same three commands in Command Prompt also worked. Ubuntu 24.04 (WSL, Homebrew Python
  3.14.6): `python3 -m pip install sympy==1.14.0` outside an environment printed
  `error: externally-managed-environment`; in a new environment the install worked and the checker printed
  `pass 13 fail 0; ...; wrote /mnt/c/.../Revision/pairing/kohn_sham/reports/python-t3.json` (forward
  slashes), exit code 0, 1.31 s and 1.30 s, output byte-identical. Kali Linux 2026.1 (WSL, Python 3.13.12):
  the plain `pip install` printed `error: externally-managed-environment`, and `python3 -m venv .venv`
  printed `The virtual environment was not created successfully because ensurepip is not available.`
  (the package `python3-venv` is not installed there; it was not installed for this test). A run of the
  checker with no precompiled Python files (an empty `PYTHONPYCACHEPREFIX`) took 4.27 s.
- Installation size: `wolframscript -code '$InstallationDirectory'` gave
  `C:\Program Files\Wolfram Research\Wolfram\15.0.1`; its 54355 files hold 9334034004 bytes (9.334 GB =
  8.693 GiB; about 9.465 GB if every file is rounded up to 4096-byte clusters).
- Web page: https://www.wolfram.com/engine/ (read on 2026-10-02) says that the free licence is obtained by
  signing in and accepting the terms of use, with a separate "Get your license" button (section 3.2).
- The two publication tests: `grep` showed that `test_dirac16complex_field_theory_publication.py` refers to
  `wolfram-t3.json` and `python-t3.json` only (its lines 87 and 88), while
  `test_pair_creation_proofs_publication.py` reads `t3-theory.json`, `wolfram-t3.json` and `python-t3.json`
  (its lines 73 to 75, used in lines 431 to 444) (section 1.4).
- Corrections made to this file (no change to the script, its inputs or outputs): section 1.3 (five of the
  ten checks have a control; the v_v part of check 6 is a restatement, see the table); section 1.4 (which
  test reads which file); section 3.1 (installation size 9.3 GB); section 3.2 (the "Get your license" step);
  section 3.4 (reopen PowerShell after installing Git); section 3.5 (run time 2 to 8 s); section 3.6
  (Command Prompt commands `findstr` and `certutil`); section 3.7 (the exact command-not-found messages of
  each shell, a row for Git, the `$Version` command per shell); section 3.8 (Python installation, private
  environment, Windows path with backslashes, run times); sections 4.1 and 4.4 (all measured times);
  section 5.2 (licence query process, the temporary files of `wolframscript`, the `Bound` socket).
- Fixes made to the script or other files of the set: none (no execution defect was found).
- Open discrepancies: none. Not verified: macOS (no Mac was available), Linux with Wolfram (no Linux
  installation of Wolfram was available; the folder that `wolframscript` uses for temporary files on macOS
  and Linux is therefore not known), and Wolfram versions other than 15.0.1.

### 6.3 Re-verification after the restart of the verification workflow

The verification workflow was interrupted by a session limit and restarted in a new session. Nothing of the
earlier record was taken on trust: every statement of sections 1 to 5 that can be tested was tested again.

- Date: 2026-10-07 (sections 6.1 and 6.2 are the verification of 2026-10-02).
- Commit verified: `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (the remote `main` at that time). Between
  `c2b33cc` (section 6.2) and `a4c5eda` no file of this set, no input and no committed output changed (under
  `Revision/pairing/` only this provenance file and the provenance file of another set were added); the
  sha256, line counts and byte counts of the script, its two inputs and its two committed outputs are exactly
  those of section 2. The next commit, `8cbd03a` (made by another workflow during this re-verification),
  changes no file of this set, no input and no output. Every file is checked out byte for byte
  (`.gitattributes` `* -text`), although Git for
  Windows on this machine has `core.autocrlf true`; the outputs contain no carriage return.
- Environment: Windows 11 Pro for Workstations, which now reports version 10.0.26300 (26H2, build
  26300.9457; section 6.1 recorded 10.0.26200, build 26200.9457), 24 logical cores; WolframScript 1.14.0;
  Wolfram `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`, `$SystemID` `Windows-x86-64`,
  `$LicenseType` `Professional`; PowerShell 7.6.6; Git 2.51.2.windows.1; Python 3.14.5 with sympy 1.14.0
  and mpmath 1.3.0 (the machine's installation). The machine was busy: 7 to 14 Wolfram processes of other
  jobs ran during the runs, which is why the times are longer than in section 6.1.
- Two fresh clones (`git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder);
  no uncommitted file was copied in (none is needed; this provenance file is committed at `a4c5eda`).

| run | clone | how | exit code | printed verdict | wall time | outputs vs committed | outputs vs the other runs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | PowerShell harness, repository root, the command of section 3.5, standard output and error captured separately | 0 | 10 PASS lines, `10/10 checks passed; time 0.6000000000000001 s` | 3.71 s | both byte-identical (`cmp` against `git show HEAD:<file>`) | - |
| 2 | 1 | the same, second run on top of run 1 | 0 | `10/10 checks passed; time 1.2000000000000002 s` | 6.45 s | both byte-identical | both identical to run 1 |
| 3 | 2 | the same harness, after DELETING `t3-theory.json` and the folder `reports/` | 0 | `10/10 checks passed; time 1.6 s` | 7.44 s | both byte-identical (folder recreated) | identical to run 1 |
| 4 | 2 | PowerShell, the commands of sections 3.5 and 3.6 literally | 0 (`$LASTEXITCODE`) | `10/10 checks passed; time 1.1 s` | 5.90 s | summary table `10 0 10`; `git status --porcelain` and `git diff --exit-code --stat` empty; `Get-FileHash` as in section 2.3 | identical |
| 5 | 2 | Git Bash, the macOS/Linux commands of sections 3.5 and 3.6 literally | 0 (`echo $?`) | `10/10 checks passed; time 1.3 s` | 6.18 s | `grep` printed `  "summary": {"passed": 10, "failed": 0, "total": 10},`; `sha256sum` as in section 2.3 | identical |
| 6 | 2 | Command Prompt (cmd.exe), the commands of sections 3.5 and 3.6 literally (`echo %ERRORLEVEL%`, `findstr`, `certutil`) | 0 | `10/10 checks passed; time 1.6 s` | 6.55 s | `findstr` and `certutil` printed exactly what section 3.6 says; `git status --porcelain` empty | identical |

- Check counts: 10 of 10 PASS in every run (report summary `{"passed": 10, "failed": 0, "total": 10}`);
  standard output exactly the 11 lines of section 4.1 (354 to 369 bytes, depending on how the time is
  printed); standard error empty (0 bytes) in runs 1 to 3.
- Side effects in the repository: in clone 1 the sha256 of every file outside `.git` (2994 files) and the
  list of all 380 folders were recorded before run 1 and after run 2: identical; `git status --porcelain
  --ignored` empty after every run; the two outputs had new modification times (they are rewritten with the
  same bytes).
- Processes (attributed by parent process id, because other jobs started Wolfram processes at the same time):
  `wolframscript` (peak working set 16.7 MB) started `wolfram.exe -wlbanner -licenseinfo` (seen 0.53 s after
  the start in run 2 by a single slow poll, whose one sample showed 9.8 MB; that was an early sample, NOT the
  peak, which is about 68 MB, see sections 4.4 and 6.4; missed by polling in the other runs because it is so
  short-lived) and the kernel `wolfram.exe -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`
  (seen 0.66 to 0.83 s after the start, peak working set 156.2 MB in runs 2 and 3, the runs in which the
  processes were attributed by parent process id). No child process was left running after any run. Killing
  `wolframscript` 3 s after the start ended its kernel as well (not running 2 s later).
- Temporary files: in every monitored run the `tmp_*` file in the folder
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` that held this run's printed output
  (identified by its content; 354 or 369 bytes) was deleted at the end of the run. Other `tmp_*` files
  appeared and remained in that folder during the runs, but other jobs were running `wolframscript` at the
  same time, so they could not be attributed to this run; section 5.2 (measured on a quieter machine)
  stands. One new entry of the system temporary folder, `tmp1z2x9wlc.json`, appeared during run 2 and was
  gone shortly afterwards (a Python-style temporary file of another program, as in section 5.2).
  `WolframScript.conf` still holds 238 bytes.
- Network (one run, sockets polled continuously): the kernel held `127.0.0.1:60712 -> 127.0.0.1:60713
  Established`, `127.0.0.1:60713 -> 127.0.0.1:60712 Established` and `0.0.0.0:60713 -> 0.0.0.0:0 Bound`;
  no UDP endpoint; `wolframscript` itself held no socket; no remote address.
- Failure tests (in a copy of clone 2, restored afterwards; `git status --porcelain --ignored` empty at the
  end): (a) `ks-theory.json` moved away: `Import::nffil` and many `Part::...` messages (on standard output;
  standard error stayed empty), `FAIL  T3_Gamma_is_the_block_map`, `9/10 checks passed`, exit code 1, report
  summary `{"passed": 9, "failed": 1, "total": 10}`, theorem status `SOME CHECKS FAILED - see the report`;
  (b) `gammas.json` moved away: the same, `9/10 checks passed`, exit code 1; (c) run from the folder
  `Revision` instead of the repository root:
  `Failed to open file at path: Revision/pairing/kohn_sham/wolfram/verify_t3.wls`, exit code 0, nothing
  written. Section 3.7 is confirmed.
- Downstream: `python Revision/pairing/kohn_sham/python/check_t3.py` (the machine's Python, not a new private
  environment; the private-environment steps of section 3.8 were verified on 2026-10-02 and not repeated)
  gave `pass 13 fail 0`, exit code 0, in clone 1 (1.4 s inside the checker) and twice in clone 2 (3.39 s and
  3.34 s wall), and rewrote `python-t3.json` byte-identically (sha256 `4924b8eb...5481`).
- Section 1.4 was re-checked with `grep` over the whole clone: the documents listed there still cite the
  set and did not change between `c2b33cc` and `a4c5eda`; the line numbers quoted for the two publication
  tests (73 to 75 and 431 to 444; 87 and 88) and for the `v_v` term of the script (line 79) are unchanged;
  the newer citing files were added to section 1.4.
- Installation size re-measured: `C:\Program Files\Wolfram Research\Wolfram\15.0.1`, 54355 files,
  9334034004 bytes, as in section 6.2.
- Corrections made to this file: section 1.4 (newer citing files), section 3.6 (the `git status` exception
  now that this file is committed), sections 3.8 and 4.4 (the run times and peak memory of 2026-10-07),
  section 5.2 (reference to this section), and this section.
- Fixes made to the script or other files of the set: none (no execution defect was found).
- Open discrepancies: none. The scientific results are unchanged: 10 of 10 checks pass and both outputs are
  byte-identical to the committed files in all six runs. Not verified: macOS, Linux with Wolfram, and Wolfram
  versions other than 15.0.1.

### 6.4 Re-verification after the independent review of section 6.3

An independent review of section 6.3 (2026-10-07) reported four points: (1) the peak memory given for the
licence query (9.8 MB) was wrong; (2) the run times given were not upper bounds on a heavily loaded machine;
(3) section 1.4 left out two committed textbook files that cite `wolfram-t3.json`; (4) a status note of the
verification workflow (not this file) still said that this file was not yet committed, although the version
with section 6.3 had already been committed. Each point was re-checked in fresh clones.

- Date: 2026-10-07.
- Commit verified: `fdab20615409434e030193880d01fb2d0c685baf` (the remote `main` at that time). Between
  `c8f6022` (the commit the review used) and `fdab206` no file under `Revision/pairing/kohn_sham/`, no input
  and no committed output changed; the sha256, line counts and byte counts of the script, its two inputs and
  its two committed outputs are exactly those of section 2. The version of this file with section 6.3 is
  committed (`72fc9ff`, a work-in-progress snapshot made before the independent review had finished); the
  corrections listed below were made on top of `fdab206`.
- Environment: as in section 6.3 (Windows 11 Pro for Workstations 10.0.26300, 24 logical cores;
  WolframScript 1.14.0; Wolfram 15.0.1, Professional licence; PowerShell 7.6.6; Git 2.51.2.windows.1). The
  machine was heavily loaded: 20 to 26 Wolfram processes of other jobs were running and the processor load
  (`Win32_Processor` `LoadPercentage`) was 100 %.
- Clone 1 (`git clone https://github.com/once-ere/Dirac_claude.git` into an empty scratch folder; no
  uncommitted file copied in): 6 monitored runs and 6 unmonitored PowerShell runs of the command of section
  3.5. The monitor was a small C# program that started `wolframscript`, found its child processes by their
  parent process id, read their peak working set while they ran (one pass of its loop every 23 to 38 ms on the
  loaded machine) and once more, through the still open process handle, after they had ended (which gives the
  exact peak). All 12 runs: exit code `0`, the 11 lines of section 4.1 ending
  `10/10 checks passed; time <t> s` with `<t>` = `1.3`, `1.4000000000000001`, `1.3`, `1.`, `1.1`,
  `1.4000000000000001` (monitored) and `1.`, `0.8`, `1.7000000000000002`, `2.`, `1.4000000000000001`,
  `1.2000000000000002` (unmonitored); standard error 0 bytes and standard output 353 bytes (when the time is
  printed as `1.`), 354 bytes (`1.1`, `1.3`) or 369 bytes (`1.4000000000000001`) in the monitored runs; both
  outputs byte-identical to the committed files after every run (sha256 as in section 2.3);
  `git status --porcelain --ignored` empty after every run; `git diff --exit-code --stat` empty with exit code
  0 at the end. Wall times: section 4.4.
- Processes (monitored runs): `wolframscript` started `"C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe" -wlbanner -licenseinfo`
  0.046 to 0.138 s after its own start; this licence query lived 0.250 to 0.474 s and its peak working set
  was 68.3 to 68.4 MB (10 to 13 samples while it ran; the value read after it ended equalled the largest
  sample). The kernel (`wolfram.exe -runfirst ... -mathlink`) started 0.324 to 0.676 s after
  `wolframscript`, lived 5.52 to 6.45 s and peaked at 156.3 to 156.7 MB; `wolframscript` peaked at 16.6 to
  16.8 MB. No child process was running 0.3 s after the end of any run.
- Point 1 confirmed: the licence query peaks at about 68 MB, not 9.8 MB; the 9.8 MB of section 6.3 was a
  single early sample. Corrected in sections 4.4, 5.2 and 6.3.
- Point 2 confirmed: in this re-verification the wall time reached 8.74 s, above the range of about 6 to 7.5 s
  that section 4.4 gave for a busy machine before this correction, and the review measured up to 13.89 s and
  printed times up to 7.2 s (section 4.4). Corrected in sections 3.5, 4.1 and 4.4; the 10 checks, the printed
  result apart from the time, and the two output files did not change in any run.
- Point 3 confirmed: `git grep -l -E 'verify_t3|t3-theory|wolfram-t3' <commit> -- Revision/textbook` lists the
  same five files at `a4c5eda`, `c8f6022` and `fdab206`: `chapters/00-how-to-use-this-book.md`,
  `notebooks/00c_honesty_ledger.PROVENANCE.md`, `notebooks/00c_honesty_ledger.ipynb`,
  `notebooks/src/00c_honesty_ledger.py` and `notebooks/src/19a_t3_rust_pairs.py`; the two `00c` files that
  were missing were added to section 1.4. The same `git grep` over the whole clone at `fdab206` finds,
  besides these and the files of section 1.4, only the set's own files, the sympy report `python-t3.json`
  and the two workflow scripts under `Revision/workflows/`, which section 1.4 now names as left out on
  purpose. (`Revision/README.md` does not match the pattern, but its line 116 still quotes
  `T3 Wolfram 10/10`.) The documents of section 1.4 outside the textbook did not change between `c8f6022`
  and `fdab206`; four of the five textbook files did (another workflow is writing them), and at `fdab206`
  they still cite the set as section 1.4 describes.
- Point 4 confirmed as a fact about the workflow's status note, not about this file: `git log` shows the
  commit `72fc9ff`, and before the corrections of this section the file in the working repository was equal
  to the committed one. No change to this file was needed for it.
- Clone 2 (a second fresh clone plus a copy of this file as corrected for points 1 to 3, before the correction
  of section 3.6 that this run led to), following sections 3.5 and 3.6 literally. PowerShell: the 11 lines
  ending `10/10 checks passed; time 1.1 s`, `$LASTEXITCODE` `0`, 6.19 s; summary table `10 0 10`;
  `git status --porcelain` printed only ` M Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`,
  and `git diff --exit-code --stat` printed only that file (shortened to
  `.../kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`) and `1 file changed, ...` with exit code 1, which
  section 3.6 did not say and now says; `Get-FileHash` gave the two sha256 of section 2.3. Git Bash (the
  macOS/Linux commands): `10/10 checks passed; time 1.8 s`, `echo $?` `0`, 8.28 s, standard error empty;
  `grep` printed `  "summary": {"passed": 10, "failed": 0, "total": 10},`; `sha256sum` gave the two sha256 of
  section 2.3; both outputs byte-identical to `git show HEAD:<file>` (`cmp`).
- Corrections made to this file: section 1.4 (the two `00c` textbook files; the workflow scripts left out on
  purpose), section 3.5 (run time on a heavily loaded machine), section 3.6 (what `git diff --exit-code
  --stat` prints when a newer copy of this file replaces the committed one), section 4.1 (printed time up to
  7.2 s), section 4.4 (all new wall times; the peak memory of the licence query, the kernel and
  `wolframscript`), section 5.2 (the licence query's peak memory and lifetime), section 6.3 (the 9.8 MB
  sample marked as not the peak) and this section.
- Fixes made to the script or other files of the set: none (no execution defect was found).
- Open discrepancies: none. The scientific results are unchanged: 10 of 10 checks pass and both outputs are
  byte-identical to the committed files in all 14 runs of this section. Not verified: macOS, Linux with
  Wolfram, and Wolfram versions other than 15.0.1.

### 6.5 The fix of `verify_t3.wls` and the verification of the whole set (2026-10-08)

- Date: 2026-10-08. Environment: Windows 11 Pro for Workstations 10.0.26300, 24 logical cores; WolframScript
  1.14.0; Wolfram 15.0.1 for Microsoft Windows (64-bit); PowerShell 7.6.6; Git 2.51.2.windows.1; Python 3.14.5
  with sympy 1.14.0 and mpmath 1.3.0 (the machine's installation). The machine was quiet: 0 to 2 Wolfram
  processes of other jobs during the measured runs.
- The fix (section 1.5). The defect was found by the T3 completion (`t3-completion.json`, gap 1). A first
  edit (committed unverified in the work-in-progress commit `42abf71`, script sha256
  `ab196c6dcbda9190e0d9a6a5657943324728e3a72b819153f1e995ef9979eb25`) read the coefficients and replaced the
  tautology by a v_v function derived from e_int; it was re-checked line by line against `ks-theory.json` and
  `verify_t3_completion.wls` and then finished: v_v is now the function `vvf[m, lambda, n, S] = c_v lambda n`
  of the coefficient read from `ks-theory.json` (the same function enters the energy-momentum profiles of
  check 7), and the coefficient fields are compared with the stated formulas `Meff` and `vv` as the
  completion does. Result: the script of section 2.1 (sha256 `0cde8c8f...87c8`, 250 lines, 27280 bytes).
- The first negative tests of the earlier, interrupted attempt (07:29) were INVALID and are not used: they
  edited `ks-theory.json` with `sed` on `"15/16"`, but the file writes `"15\/16"`, so nothing was changed
  (the edit counter printed `0`) and the 10/10 of those runs proves nothing. They were redone (next item).
- Negative tests (scratch trees holding only the script and its two inputs; every input edit made with a
  JSON reader and writer and checked by re-reading the file; a diagnostic line printing the five parts
  {H2 values, formula text, consistency, map, control} of check 6 was added to the scratch copy only):

  | test | change | result |
  | --- | --- | --- |
  | 1 | `Meff_coefficient_of_lambda_S` = `7/8` | `FAIL  T3_mean_field_map` (parts False, False, False, True, True), `9/10 checks passed`, exit 1 |
  | 2 | `vv_coefficient_of_lambda_n` = `1/16` | `FAIL  T3_mean_field_map` (False, False, False, True, True), `9/10`, exit 1 |
  | 2b | `vv_coefficient_of_lambda_n` = `0` | `FAIL  T3_mean_field_map` (False, False, False, True, False: the control fails), `9/10`, exit 1 |
  | 2c | a different but self-consistent functional: v_v coefficient `-1/8`, `vv` = `-lambda n(y)/8`, `e_int` with `(1/16) lambda n^2` | `FAIL  T3_mean_field_map` (False, True, True, True, True: only the comparison with hypothesis H2 fails), `9/10`, exit 1 |
  | 3 | the OLD script (sha256 `ea6c436f...97d8`) with the input of test 2 | `10/10 checks passed`, exit 0: the defect |
  | 4 | script mutation `vvf[...] := cVv ll nn + ll ss/16` (an S-odd term) | `FAIL  T3_mean_field_map` (True, True, False, False, True) and `FAIL  T3_energies_and_emt_profiles_equal`, `8/10`, exit 1 |
  | 4b | script mutation `vvf[...] := cVv ll nn + mm/16` (an m-odd term) | the same two FAILs, `8/10`, exit 1 |
  | 4c | script mutation: the map clause evaluated at (-m, -lambda) instead of (-m, +lambda) | `FAIL  T3_mean_field_map` (True, True, True, False, True), `9/10`, exit 1 |
  | 5 | `ks-theory.json` deleted | `ERROR  input file not found: <path>`, exit 1, nothing written |
  | 6 | `gammas.json` deleted | `ERROR  input file not found: <path>`, exit 1, nothing written |
  | 7 | `Meff_coefficient_of_lambda_S` = `fifteen/16` | `ERROR  cannot read the Kohn-Sham potentials ...`, exit 1, nothing written |
  | 7b | `e_int` with `+ (1/32) lambda n^2` | the same `ERROR`, exit 1, nothing written |
  | 7c | `ks-theory.json` cut after 1000 bytes | `ERROR  input file is not a JSON object: <path>`, exit 1, nothing written |
  | 8 | a folder named `wolfram-t3.json` in `reports/` | the 10 check lines, then `ERROR  cannot write <path>`, exit 1; `t3-theory.json` was written |
  | 9 | run from the folder `Revision` | `Failed to open file at path: Revision/pairing/kohn_sham/wolfram/verify_t3.wls` on standard error, exit 0, nothing written |
  | 10 | completion, `ks-theory.json` deleted | `Import::nffil`, `ToExpression::notstrbox`, ..., 2 FAIL lines, `1/3 checks passed`, exit 1, both outputs written |
  | 11 | completion, `gammas.json` deleted | `Import::nffil`, `Part::partw`, ..., `FAIL  T3C_krein_rule_16_component`, `2/3 checks passed`, exit 1, both outputs written |
  | 12 | completion, `Meff_coefficient_of_lambda_S` = `7/8` | `FAIL  T3C_mean_field_coefficients_from_ks_theory`, `2/3`, exit 1 |
  | 13 | completion, unchanged inputs | `3/3 checks passed`, exit 0, both outputs byte-identical to the committed ones |

  So every part of check 6 can fail, check 6 fails for a broken coefficient for the right reason, and the
  old script did not detect it.
- Runs in the working repository (outputs compared with `git show HEAD:<file>` and between runs):
  `verify_t3.wls` twice (3.57 s and 3.92 s wall, `time 0.4 s` both, exit 0, standard error empty):
  `t3-theory.json` byte-identical to the committed file; `wolfram-t3.json` identical in both runs, sha256
  `b0903ca4...f7c6` (only the detail of check 6 differs from the committed versions). Then twice each:
  `verify_t3_completion.wls` (3.44 s, 3.35 s; `3/3 checks passed`, exit 0, standard error empty),
  `check_t3.py` (1.11 s, 1.15 s; `pass 13 fail 0`, exit 0), `check_t3_completion.py` (0.72 s, 0.74 s;
  `pass 7 fail 0`, exit 0): `t3-completion.json`, `wolfram-t3-completion.json`, `python-t3.json` and
  `python-t3-completion.json` byte-identical to the committed files after every run (sha256 of section 2).
  The sympy checker `check_t3.py` reads `t3-theory.json` (unchanged) and `check_t3_completion.py` reads only the
  summary and the check names of `wolfram-t3.json` (unchanged), so the fix changes neither report.
- Monitored runs (a small C# program started `wolframscript`, found its child processes by parent process id
  every 17 to 22 ms, read their working set while they ran and once more through the open process handle
  after they had ended, which gives the exact peak, and listed the folder `WolframScriptTemporary`): two runs
  of each script in the working repository. `verify_t3.wls`: 3.42 s and 2.97 s, `time 0.5 s` and
  `time 0.4 s`, exit 0, standard output 354 bytes, standard error 0 bytes; `verify_t3_completion.wls`: 3.21 s
  and 3.01 s, exit 0, standard output 141 bytes. Children in every run: `conhost.exe` (8.2 MB; the monitor
  starts `wolframscript` without a console window), the licence query `wolfram.exe` (lived 0.105 to 0.134 s,
  peak 74.5 to 74.6 MB), the kernel `wolfram.exe` (started 0.17 to 0.22 s after `wolframscript`, lived 2.75 to
  3.23 s, peak 167.0 to 167.1 MB); `wolframscript` peaked at 19.0 to 19.1 MB. No child was alive 0.3 s after
  the end. Temporary files: in the three runs with no other Wolfram process running, exactly two new `tmp_*`
  files (an empty one 20 to 26 ms after the start and the output file, 354 or 141 bytes) and both were
  deleted at the end; in the first run (2 Wolfram processes of other jobs running) a third, empty `tmp_*`
  file appeared at 1.57 s and stayed - it could not be attributed to this run.
- Kill tests (scratch trees; the C# program killed `wolframscript` after 1.0 s and 2.3 s for `verify_t3.wls`
  and after 2.3 s for the completion): exit code -1; the kernel was not alive 2 s later; no output file was
  written; the empty `tmp_*` file of each run remained (three files of 0 bytes, deleted by hand afterwards).
- Fixes made: `verify_t3.wls` (check 6, the `ERROR` exits of section 4.2, the header comment); its report
  `wolfram-t3.json` (detail of check 6); this file (extended to the whole set). No other file of the set was
  changed; `t3-theory.json`, `verify_t3_completion.wls` and its outputs are unchanged.
