# Provenance of the wolframscript set `Revision/pairing/kohn_sham/wolfram/` (the verifier of theorem T3)

This file is written for a student who has never used Wolfram or a terminal before. It says what the script
does, which files it reads and writes, how to install everything and run it on Windows, macOS or Linux, what
you should see, what the run changes on your computer, and how and when it was verified. Everything you need
is in this file.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

The set is one WolframScript file, `Revision/pairing/kohn_sham/wolfram/verify_t3.wls`. It proves theorem T3
("the Kohn-Sham level of the pairing of universes of masses +m and -m") by exact symbolic algebra and writes
two JSON files: the theorem record `Revision/pairing/kohn_sham/t3-theory.json` and the check report
`Revision/pairing/kohn_sham/reports/wolfram-t3.json`.

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
- Theorem T3 says: take ANY self-consistent Kohn-Sham state of a universe with mass m, coupling lambda and
  tip angle theta. Replace every orbital chi of block j by sigma2 chi in block -j (in the 16-component
  language this is the chirality matrix Gamma), exchange the two brane parities and change the tip angle to
  pi - theta. The result is again a self-consistent Kohn-Sham state, of a universe with mass -m, the SAME
  coupling +lambda and tip angle pi - theta. All energy levels, occupations, the chemical potential, the
  particle number, the entropy, the Kohn-Sham energy, the grand potential, the free energy and the
  energy-momentum profiles are EQUAL; the densities S(y) and Q(y) change sign.

### 1.3 How the script proves it

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
| 6 | `T3_mean_field_map` | M_eff(-m, +lambda, -S) = -M_eff(m, lambda, S); the interaction energy e_int is unchanged when S -> -S. Note on v_v: v_v = -lambda n/16 depends only on lambda and n, so it is unchanged because n is unchanged, which check 5 establishes; the script's v_v term (`vvf[lam, n] === vvf[lam, n]`, line 79 of the script) compares an expression with itself, so it is a consistency restatement, not an independent test | the same with (-m, -lambda) is NOT a symmetry |
| 7 | `T3_energies_and_emt_profiles_equal` | for two general occupied orbitals of opposite block type: energy density, pressures p3, p_t, p8, the Kohn-Sham energy integrand, entropy terms and the exact-Fock diagnostic are equal; S and Q change sign | with (-m, -lambda) the energy integrand differs |
| 8 | `T3_exact_k0_spectra` | for k = 0, v = 0 and constant M the exact characteristic functions of the original and the image problem agree, so the spectra are equal level by level; the zero mode maps to the zero mode | the untransformed tip gives a different spectrum |
| 9 | `T3_Gamma_is_the_block_map` | with the block basis V read from `ks-theory.json` and the matrices read from `gammas.json`: V is unitary, Gamma = diag(-1 (8 times), +1 (8 times)), Gamma maps block (j, s2, s3) to block (-j, s2, s3) times s2 sigma2, and in every block gamma^(x8) = sigma3 and gamma^(x8) gamma^(x4) = j sigma1 | none |
| 10 | `T3_z2_mirror_copy_carries_minus_m_plus_lambda` | inside the ASSUMED Z2 mirror (orbifold) construction, the mirror copy of a self-consistent state carries (-m, +lambda) | none |

What T3 does NOT establish (the theorem record says this explicitly): no creation process, rate or amplitude
(it maps solutions to solutions; it does not make a pair of universes); only instantaneous (adiabatic)
mean-field states (the time-dependent problem is open); the Z2 brane is an ASSUMPTION and the tip angle must
be transformed; no correlation beyond Hartree plus exchange; no statement about two independently quantised
universes; no back-reaction on the geometry. The pairing proved here is (m, lambda) -> (-m, +lambda) at
equal energies, not (m, lambda) -> (-m, -lambda).

### 1.4 Which documents cite its results

- `Revision/docs/PAIR_CREATION_PROOFS.md` and `Revision/docs/PAIR_CREATION_PROOFS.tex`: section 8 (theorem T3:
  hypotheses, statement, proof with the table of the 10 Wolfram check names), section 9.1 (the table row of
  `wolfram-t3.json`: 10 checks, 10 PASS, 0 FAIL) and the run commands.
- `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` and `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.tex`: the
  record table ("Wolfram: 10 of 10 checks pass") and the run commands.
- `Revision/README.md`: the overview table ("T3 Wolfram 10/10").
- `Revision/pairing/kohn_sham/README.md`: the description of the two T3 verifiers.
- `Revision/pairing/pairing-theory.json` and `Revision/pairing/wolfram/verify_pairing.wls`: a pointer saying
  that T3 is proved here, not there.
- `Revision/pairing/kohn_sham/python/check_t3.py` (the independent sympy checker): it reads
  `t3-theory.json` as data and compares its theorem and its "not established" list with its own derivation
  (checks `compare.t3_theory.theorem` and `compare.t3_theory.not_established`); its report is
  `Revision/pairing/kohn_sham/reports/python-t3.json`.
- `Revision/tests/test_pair_creation_proofs_publication.py` (test `test_t3_record_and_its_checks`): it reads
  `t3-theory.json` (the status `all checks of the report passed`, the statement, the ASSUMED hypothesis, and
  that its list of check names equals the check names of `wolfram-t3.json`), and it reads `wolfram-t3.json`
  and `python-t3.json` (all checks pass and every check name is cited in `PAIR_CREATION_PROOFS.md`).
- `Revision/tests/test_dirac16complex_field_theory_publication.py`: it reads `wolfram-t3.json` (and
  `python-t3.json`), NOT `t3-theory.json`, and checks that `DIRAC16COMPLEX_FIELD_THEORY.md` quotes the counts
  as `Wolfram: 10 of 10 checks pass`.
- `provenance/dirac matrices.md`: lists `verify_t3.wls` among the files that read the author's gamma matrices
  from `Revision/algebra/gammas.json`; `Revision/algebra/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` and
  `Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md` name it as a consumer of their outputs.
- The textbook (`Revision/textbook/`, still being written by another workflow and not yet verified at the time
  of sections 6.3 and 6.4): `chapters/00-how-to-use-this-book.md` cites `wolfram-t3.json` (10 of 10) for
  theorem T3; the notebook source `notebooks/src/00c_honesty_ledger.py` counts the checks of `wolfram-t3.json`
  (10); its built notebook `notebooks/00c_honesty_ledger.ipynb` reads the same report and shows the count in
  its saved output (a table line naming `pairing/kohn_sham/reports/wolfram-t3.json`, `Wolfram` and
  `10 of  10`); its provenance file `notebooks/00c_honesty_ledger.PROVENANCE.md` lists `wolfram-t3.json` as a
  verifier report whose checks the notebook counts; and `notebooks/src/19a_t3_rust_pairs.py` lists
  `t3-theory.json` and `wolfram-t3.json` as records it reads.
- Left out on purpose: the workflow scripts `Revision/workflows/revision_wave_2.js` and
  `Revision/workflows/wave1_review_and_fix.json` also mention the set, but they are automation scripts that
  produced or reviewed it, not documents that cite its results.

## 2. Files

### 2.1 The script

| file | sha256 | lines | bytes |
| --- | --- | --- | --- |
| `Revision/pairing/kohn_sham/wolfram/verify_t3.wls` | `ea6c436f667c465727967c8b9664e2425227be0d71a55ca36a36e13a3da497d8` | 207 | 23070 |

There is no package file: the script loads no Wolfram package (`Get`/`Needs` are not used) and takes no
command-line arguments. It finds its input and output files relative to its own location (`$InputFileName`),
so it does not depend on the folder you run it from.

### 2.2 Inputs (read only, never modified)

| file | sha256 | lines | bytes | what is read | produced by |
| --- | --- | --- | --- | --- | --- |
| `Revision/kohn_sham/ks-theory.json` | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` | 477 | 17278 | `blockBasis.unnormalisedColumns2Sqrt2V` (the 16 x 16 block basis V times 2 sqrt 2) and `blockBasis.labels` (the (j, s2, s3) label of each block) | `Revision/kohn_sham/theory/verify_ks_theory.wls` |
| `Revision/algebra/gammas.json` | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` | 1405 | 76968 | `gamma` (the eight 16 x 16 matrices gamma^(x1) ... gamma^(x8)) and `Gamma` (the chirality) | `Revision/algebra/wolfram/verify_algebra.wls` |

Only check 9 (`T3_Gamma_is_the_block_map`) uses these inputs; checks 1 to 8 and 10 use only formulas written
in the script.

### 2.3 Outputs (written on every run, LF line endings, deterministic)

| file | sha256 of the committed (and regenerated) file | lines | bytes | content |
| --- | --- | --- | --- | --- |
| `Revision/pairing/kohn_sham/t3-theory.json` | `f1ae1e8ab2248bde43526fc2e1624f0a74aacbe4a0b7f3f3a8954a3048dbcdd7` | 55 | 7053 | the theorem record: document, producer, report, inputs, status, coordinates, hypotheses H1-H6, statement S1-S5, proof, relation to T1/T2, the 10 check names, the numerical confirmation, what is not established |
| `Revision/pairing/kohn_sham/reports/wolfram-t3.json` | `904fd1dcb77a6772f7ef21dcabe10d194d8086f509e17df54830bd7f7fb999ab` | 19 | 6448 | the report: `"summary": {"passed": 10, "failed": 0, "total": 10}` and, for each of the 10 checks, its name, verdict (`PASS` or `FAIL`) and a detailed explanation |

Both files contain only fixed text and the integer check counts (no dates, times, machine names or
floating-point numbers), so a passing run reproduces them byte for byte. If a check fails, the counts, the
verdict of that check and the `status` line of the theorem record change.

## 3. How to run it (complete instructions)

### 3.1 What you need

- A computer with Windows 10 or 11, macOS, or Linux, at least 10 GB of free disk space for the installed
  Wolfram program (the Wolfram 15.0.1 installation folder of the verification machine holds 54355 files with
  together about 9.3 GB = 8.7 GiB), plus room for the downloaded installer file itself (the download page
  shows its size; you can delete it after the installation), and an internet connection for the installation
  (the run itself needs no network).
- Wolfram: either the free Wolfram Engine for Developers or a Mathematica / Wolfram desktop licence. Both
  contain the command-line program `wolframscript`, which is what runs the script.
- Git, to download the repository.

The script uses only long-established Wolfram Language functions (associations, `Import` with the JSON
format `"RawJSON"`, `Simplify`, `ComplexExpand`, binary file writing). It was verified with Wolfram 15.0.1
and WolframScript 1.14.0 only (section 6); with another version the 10 checks are expected to pass and to
give the same two files, but that was not tested.

### 3.2 Install Wolfram

Option A, the free Wolfram Engine for Developers:

1. In a web browser open https://www.wolfram.com/engine/ and click the download button for your system. You
   may be asked to sign in with a Wolfram ID; if you have none, create one there (free; you type your own
   e-mail address and password - nobody else should do this for you).
2. Get the free licence: on the same page click "Get your license", sign in with your Wolfram ID and accept
   the terms of use (free); the page says that the free licence is obtained this way. The activation in
   section 3.3 needs this licence, so do this step before section 3.3.
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
prints a licensing error, run `wolframscript -activate` and then repeat `wolframscript -code 1+1`.

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

### 3.5 Run the script

Windows PowerShell (from the repository root):

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
$LASTEXITCODE
```

macOS or Linux Terminal (from the repository root):

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
echo $?
```

If you use the older Windows "Command Prompt" (cmd.exe) instead of PowerShell, the first line is the same
and the second line is `echo %ERRORLEVEL%`.

The first line runs the script (it takes about 2 to 8 seconds, typically 3 to 5, more on a busy machine;
usually most of it is starting Wolfram). On a heavily loaded machine (10 to 26 Wolfram processes of other
jobs running, 2026-10-07) a run took up to about 14 seconds; only the time changes, the printed result and
the two output files stay the same (sections 4.1 and 4.4). The second line
prints the exit code of the run: `0` means every check passed, `1` means at least one check failed. The run
needs no input from you and opens no window.

### 3.6 Check the result

1. Read the check counts in the report.
   - Windows PowerShell:

     ```text
     (Get-Content Revision/pairing/kohn_sham/reports/wolfram-t3.json -Raw | ConvertFrom-Json).summary
     ```

     prints a small table with `passed failed total` and below it `10 0 10`.
   - macOS or Linux:

     ```text
     grep '"summary"' Revision/pairing/kohn_sham/reports/wolfram-t3.json
     ```

     prints `  "summary": {"passed": 10, "failed": 0, "total": 10},`.
   - Windows Command Prompt (cmd.exe; the PowerShell, `grep`, `sha256sum` and `shasum` commands of this
     section do not exist there):

     ```text
     findstr /c:"summary" Revision\pairing\kohn_sham\reports\wolfram-t3.json
     ```

     prints `  "summary": {"passed": 10, "failed": 0, "total": 10},`.
2. Confirm that the regenerated files are byte-identical to the committed ones (the same two commands in
   PowerShell, Command Prompt, macOS and Linux):

   ```text
   git status --porcelain
   git diff --exit-code --stat
   ```

   Both commands print nothing when the two output files are unchanged (the files are rewritten, but with the
   same bytes, so Git sees no change). The only exception: in a copy of the repository into which a newer,
   not yet committed version of this provenance file was copied by hand, `git status --porcelain` prints a
   single line naming it (`?? Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` if the file is
   new, ` M Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` if it replaces a committed
   version), and in the second case `git diff --exit-code --stat` also prints a line naming that file (its
   path may be shortened, for example `.../kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md | 57 +++++-----`)
   and then `1 file changed, ...` (and its exit code is `1`). This is fine as long as
   neither command names `t3-theory.json` or `wolfram-t3.json`.
3. Optionally compare the sha256 checksums with section 2.3: Windows PowerShell
   `Get-FileHash -Algorithm SHA256 Revision/pairing/kohn_sham/t3-theory.json, Revision/pairing/kohn_sham/reports/wolfram-t3.json`
   (it prints the hash in capital letters); Linux
   `sha256sum Revision/pairing/kohn_sham/t3-theory.json Revision/pairing/kohn_sham/reports/wolfram-t3.json`;
   macOS
   `shasum -a 256 Revision/pairing/kohn_sham/t3-theory.json Revision/pairing/kohn_sham/reports/wolfram-t3.json`;
   Windows Command Prompt (cmd.exe), one file per command:

   ```text
   certutil -hashfile Revision\pairing\kohn_sham\t3-theory.json SHA256
   certutil -hashfile Revision\pairing\kohn_sham\reports\wolfram-t3.json SHA256
   ```

   Each prints `SHA256 hash of <file>:`, then the hash in small letters (for example
   `f1ae1e8ab2248bde43526fc2e1624f0a74aacbe4a0b7f3f3a8954a3048dbcdd7` for `t3-theory.json`), then
   `CertUtil: -hashfile command completed successfully.`

### 3.7 What to do if it fails

| what you see | cause | what to do |
| --- | --- | --- |
| `wolframscript : The term 'wolframscript' is not recognized as the name of a cmdlet, ...` (Windows PowerShell 5.1, the one that opens by default) or `wolframscript: The term 'wolframscript' is not recognized as a name of a cmdlet, ...` (PowerShell 7); `'wolframscript' is not recognized as an internal or external command, operable program or batch file.` (Command Prompt); `zsh: command not found: wolframscript` (macOS Terminal, whose shell is zsh); `bash: wolframscript: command not found` (Linux with bash; some distributions print a longer "command not found" hint instead) | WolframScript is not installed or not on the PATH | install it (section 3.2, step 4), then close the terminal and open a new one |
| the same messages for `git` instead of `wolframscript` (for example `git : The term 'git' is not recognized ...`, `zsh: command not found: git`) | Git is not installed, or (Windows) the terminal window was already open when Git was installed | install Git (section 3.4, step 1), close the terminal, open a new one and check with `git --version` |
| a request to activate, or a message about a missing or invalid licence | WolframScript is not activated | run `wolframscript -activate`, sign in with your own Wolfram ID, then repeat section 3.3 |
| a message that no licence or no kernel is available | another Wolfram program uses the kernel(s) your licence allows | close other Wolfram programs and notebooks and run again (this script starts one kernel) |
| `Failed to open file at path: Revision/pairing/kohn_sham/wolfram/verify_t3.wls` | you are not in the repository root | `cd` into the folder `Dirac_claude` (the one that contains `Revision`) and run again. Note: in this case `wolframscript` still returns exit code `0` although nothing was run, so always look for the line `10/10 checks passed` |
| `Import::nffil: File ...ks-theory.json not found during Import.` (or `...gammas.json...`), followed by many `Part::...` messages, `FAIL  T3_Gamma_is_the_block_map`, `9/10 checks passed`, exit code `1` | an input file is missing or was moved | restore it with `git checkout -- Revision/kohn_sham/ks-theory.json Revision/algebra/gammas.json`, restore the outputs (section 5.4) and run again |
| any other `FAIL  ...` line, fewer than `10/10`, exit code `1` | an input or the script differs from the committed version, or a different Wolfram version simplifies an expression differently | run `git status` to see which files changed; restore changed files with `git checkout -- <file>`; if the failure remains with the committed files, do not edit anything: record the Wolfram version and report the failing check name. To print the version: PowerShell, macOS and Linux: `wolframscript -code '$Version'` (with the single quotes); Command Prompt: `wolframscript -code $Version` (no quotes; with single quotes Command Prompt prints `ToExpression::sntx: Invalid syntax ...` and `$Failed`). It prints a line such as `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` |
| `git status --porcelain` lists `t3-theory.json` or `wolfram-t3.json` after a run that printed `10/10` | the script file was changed (for example opened and saved in the Wolfram desktop application) | compare its sha256 with section 2.1; restore it with `git checkout -- Revision/pairing/kohn_sham/wolfram/verify_t3.wls` and run again |

Do not run the script from inside a Wolfram notebook: its last line is `Exit[...]`, which would close the
notebook's kernel. Use the terminal as described above.

### 3.8 Optional next step: the independent sympy checker

This is not part of this set, but it consumes its theorem record. It needs Python 3 and the Python package
sympy. It was verified with Python 3.14.5 and sympy 1.14.0 (with mpmath 1.3.0) on Windows and with Python
3.14.6 (Homebrew) and sympy 1.14.0 on Ubuntu 24.04 (under WSL on the verification machine).

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
   run the checker, from the repository root, AFTER the Wolfram script. Do not install sympy into the
   system's Python with a plain `pip install`: on current Linux distributions and with Homebrew Python this
   is refused with `error: externally-managed-environment`.
   - Windows PowerShell or Command Prompt:

     ```text
     python -m venv .venv
     .venv\Scripts\python -m pip install sympy==1.14.0
     .venv\Scripts\python Revision/pairing/kohn_sham/python/check_t3.py
     ```

   - macOS or Linux:

     ```text
     python3 -m venv .venv
     .venv/bin/python -m pip install sympy==1.14.0
     .venv/bin/python Revision/pairing/kohn_sham/python/check_t3.py
     ```

   These commands call the Python of the private environment directly, so you do not need to "activate"
   it. (If you prefer to activate it: macOS/Linux `. .venv/bin/activate`, Windows PowerShell
   `.venv\Scripts\Activate.ps1`; on a new Windows computer PowerShell may refuse the latter with a message
   that running scripts is disabled; then simply use the commands above. After activating, `python` alone
   means the environment's Python.)

The `pip install` line downloads sympy (6.3 MB) and mpmath (536 kB) from the internet (it took 22 to 28 s
on the verification machine) and prints `Successfully installed mpmath-1.3.0 sympy-1.14.0`; a note
`[notice] A new release of pip is available ...` may also appear and can be ignored. The checker prints 13 lines such as
`[   0.1s] PASS T3.block_hamiltonian_map`, and its last line is
`pass 13 fail 0; <time>s; wrote <full path of the repository>\Revision\pairing\kohn_sham\reports\python-t3.json`
on Windows (with backslashes) or `... wrote <full path of the repository>/Revision/pairing/kohn_sham/reports/python-t3.json`
on macOS/Linux (with forward slashes). It exits with `0` and rewrites
`Revision/pairing/kohn_sham/reports/python-t3.json` byte-identically (sha256
`4924b8ebd2d294c53eab12977012880446759d6ff53526620b3764dd9d875481`). A repeated run takes about 1.3 to 1.6
seconds on a quiet machine (3.3 to 3.4 s were measured while about 14 other Wolfram processes of other jobs
were running, section 6.3); the first run after installing can take longer (4.3 s measured with no
precompiled Python files, 8.2 s for one cold first run). The folder `.venv` stays in the repository root;
Python 3.13 and newer put a file `.gitignore` inside it, so `git status` does not show it (with an older
Python, `git status` shows `?? .venv/`). You may delete the folder `.venv` when you no longer need it.

## 4. Expected output

### 4.1 Printed on the screen

Exactly these 11 lines (nothing is printed as an error):

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
10/10 checks passed; time 0.5 s
```

The final verdict line is `10/10 checks passed; time <t> s`. Only `<t>` changes from run to run: it is the
computing time inside Wolfram, without the start of Wolfram; on the verification machine it was 0.4 to 2
seconds (the larger values when the machine was busy with other work), and on a heavily loaded machine
(10 to 26 Wolfram processes of other jobs running, 2026-10-07) up to 7.2 seconds (printed, for example,
`time 3.2 s`, `time 3.7 s` and `time 7.2 s`). Only this number changes: the ten `PASS` lines, the
`10/10 checks passed` and the two output files stay exactly the same. It is rounded to 0.1 s, but Wolfram
prints the rounded number in its own way: the verification runs printed, for example, `time 0.5 s`,
`time 1. s`, `time 2. s`, `time 0.7000000000000001 s` and `time 1.2000000000000002 s`. This is harmless:
the time is printed only on the screen and never enters a file. The lines appear one after the other while
the checks run.

### 4.2 Exit code

`0` when all 10 checks pass; `1` when at least one fails (verified: a run with a missing input exited with
`1`). Caution: a wrong file path also gives `0` (section 3.7).

### 4.3 Files written

- `Revision/pairing/kohn_sham/t3-theory.json`: 55 lines, 7053 bytes, sha256
  `f1ae1e8ab2248bde43526fc2e1624f0a74aacbe4a0b7f3f3a8954a3048dbcdd7`; its line 9 reads
  `  "status": "all checks of the report passed",` (after a failure: `SOME CHECKS FAILED - see the report`).
- `Revision/pairing/kohn_sham/reports/wolfram-t3.json`: 19 lines, 6448 bytes, sha256
  `904fd1dcb77a6772f7ef21dcabe10d194d8086f509e17df54830bd7f7fb999ab`; its summary line (line 6) reads
  `  "summary": {"passed": 10, "failed": 0, "total": 10},` and each of its 10 check lines contains
  `"verdict": "PASS"`.

### 4.4 Run time and memory on the verification machine

Windows 11, 24 logical cores: about 2 to 8 seconds wall-clock time per run, typically 3 to 5 seconds, of
which 0.4 to 2 s is computation and the rest is starting and stopping Wolfram. While the machine was busy
with many other Wolfram jobs a run took about 4 to 9 seconds, and on a heavily loaded machine up to about 14
seconds, with up to 7.2 s of computation. All measurements (seconds):

- first verification (runs 1 to 8 of section 6.1): 4.56, 4.65, 4.13, 3.57, 3.23, 4.15, 4.64, 4.80;
- review of this file, unmonitored runs: 2.09, 2.07, 2.26, 4.04, 3.92, 6.08; runs under process, file or
  socket monitoring: 2.31, 5.81, 8.18;
- re-verification after the review (section 6.2), unmonitored runs: 5.18 (run A), 3.80 (run B, Command
  Prompt), 3.09 (run C), 3.46, 3.36, 4.59 (PowerShell), 4.72, 3.21 (Git Bash); runs under monitoring:
  5.85, 3.31, 4.73, 3.73, 6.40, 4.63, 3.68, 3.80, 3.46, 3.62, 3.34.
  During these runs the machine was also running up to about ten other Wolfram kernels of other jobs.
- re-verification after the restart (section 6.3, 2026-10-07, the machine busy with 7 to 14 Wolfram
  processes of other jobs): 3.71, 6.45 (clone 1, runs 1 and 2), 7.44, 5.90, 6.18, 6.55 (clone 2, runs 3 to 6),
  5.99 (socket-monitored run).
- independent review of section 6.3 (2026-10-07, a heavily loaded machine with 10 to 20 Wolfram processes of
  other jobs; the printed time, written here to 0.1 s, in brackets): 13.89 (3.2), 6.83 (1.4), 13.34 (7.2),
  8.42 (1.5), 11.08 (3.7), 4.96 (0.9), 5.49 (1.4), 7.26 (1.6), 7.59 (1.4), 5.75 (1.1), 5.27 (1.1), 4.66 (0.7,
  Windows PowerShell 5.1); a Command Prompt run printed `time 5.5 s`. Every one of these runs printed
  `10/10 checks passed` and exited with `0`.
- re-verification after that review (section 6.4, 2026-10-07, 20 to 26 Wolfram processes of other jobs, all
  24 cores at 100 % load): monitored runs 6.55, 7.02, 7.21, 6.08, 5.96, 5.90; unmonitored PowerShell runs
  5.25, 5.16, 6.65, 8.74, 7.46, 6.60, 6.19; Git Bash run 8.28 (printed times 0.8 to 2 s).

So on a heavily loaded machine a run can take up to about 14 seconds and print a time of up to about 7
seconds; only the time changes, while the 11 printed lines (apart from the time) and the two output files
stay identical.

Peak memory (working set): about 148 to 157 MB for the Wolfram kernel (measured 148.1 to 149.1 MB on
2026-10-02 and 156.2 to 156.7 MB on 2026-10-07), about 68 MB for the short-lived licence query (68.3 to
68.4 MB in the six runs of section 6.4, read from the process right after it ended, which gives its exact
peak; the independent review found 66.7 to 68.3 MB by sampling it while it ran) and about 17 MB for
`wolframscript` (16.6 to 16.8 MB). The value 9.8 MB that section 6.3 first gave for the licence query was a
single sample taken early in that process's life by slow polling, not its peak.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

- OVERWRITTEN on every run (both are committed files): `Revision/pairing/kohn_sham/t3-theory.json` and
  `Revision/pairing/kohn_sham/reports/wolfram-t3.json`. A passing run writes the same bytes, so only their
  modification times change and `git status` stays clean.
- CREATED only if missing: the folder `Revision/pairing/kohn_sham/reports/` (the script creates it before
  writing the report).
- Nothing else in the repository is created, changed or deleted (verified with `git status --porcelain --ignored`
  and with a full listing of every file of the clone before and after a run).

### 5.2 Outside the repository

- Processes: `wolframscript` starts one Wolfram kernel (on Windows the process `wolfram.exe` of Wolfram 15,
  started as `wolfram.exe -runfirst ... -linkmode Connect -linkname <name>_shm -mathlink`; older versions call
  the kernel `WolframKernel`). Before the kernel it starts a second, short-lived `wolfram.exe` that queries
  the licence (`wolfram.exe -wlbanner -licenseinfo`, peak working set about 68 MB); it lives only a fraction
  of a second (0.18 to 0.53 s measured on 2026-10-07, section 6.4; the kernel was started 0.15 to 0.9 s after
  it). On the verification machine this licence query was seen in every run in which process creation was
  recorded by events (5 of 5 runs, section 6.2); runs observed only by polling every 30 ms usually missed it
  because it is so short-lived. The kernel ends when the script ends; no process is left running (verified for
  runs 1 to 4 of section 6.1 and every monitored run of sections 6.2 to 6.4). If you interrupt a run by
  killing `wolframscript` (tested with `Stop-Process -Force` 1, 1.5 and 3 s after the start), the kernel also
  ends; no kernel was left running.
- Temporary files: on every run `wolframscript` creates two temporary files in the folder
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (on the verification machine
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`), each named `tmp_` followed
  by 10 random letters and digits (for example `tmp_NnpCUtx4xQ`): an empty one right when it starts, and one
  that receives the printed output while the checks run (a few hundred bytes at the end: 354 to 369 bytes
  observed, depending on how the time is printed). It deletes both when the run ends normally. If a run is
  interrupted (tested by killing the `wolframscript` process), such files can remain (seen: the empty
  file, and an output file of 166 bytes holding the first six `PASS` lines, after killing `wolframscript`
  3 s after the start); they are harmless and may be deleted by hand. The same folder may also hold
  leftover `tmp_*` files of other, earlier `wolframscript` calls. The corresponding folder on macOS and
  Linux was not verified. Nothing new was found in the system temporary folder (`%TEMP%`,
  `C:\Users\<you>\AppData\Local\Temp`) that belongs to this run (its contents were listed before and after
  runs 1 and 2 of section 6.1 and the four monitored runs of section 6.2; the only new entries there, files
  such as `tmpb9gl5qav.json`, appeared in only 2 of the 4 runs, are named like the temporary files of Python
  programs, were deleted again shortly afterwards, and came from other programs that were running at the
  same time).
- Wolfram's own housekeeping, not caused by the script itself: on the verification machine every
  `wolframscript` call rewrote its settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` with the
  same 238 bytes, and the kernel start touched the folder `%APPDATA%\Wolfram\Paclets\Temporary` (only its
  time stamp changed). On macOS and Linux the corresponding Wolfram user folder is used.
- Network: the script contains no network command. During runs 1 to 4 of section 6.1 (sockets polled every
  0.1 s) the kernel's recorded connections were all loopback (127.0.0.1 to 127.0.0.1). The two
  socket-monitored runs of the review and the four of section 6.2 (polled every 0.1 s and 30 ms) recorded
  the complete picture: the kernel held one or two loopback connections 127.0.0.1 <-> 127.0.0.1 (its
  internal link) and, with the same port as one end of such a connection, a TCP socket in state `Bound` on
  0.0.0.0 (all addresses; not listening, no remote end); for example
  `127.0.0.1:52970 -> 127.0.0.1:52971 Established`, `127.0.0.1:52971 -> 127.0.0.1:52970 Established` and
  `0.0.0.0:52971 -> 0.0.0.0:0 Bound`. It had no UDP endpoints. No connection to another computer was seen.
  The short-lived licence query process could not be polled for sockets (it ends too quickly).
  (Activating WolframScript, section 3.3, does use the internet; that is a one-time step, not part of the run.)

### 5.3 Effects on other parts of the repository

The sympy checker `Revision/pairing/kohn_sham/python/check_t3.py` reads `t3-theory.json`; the publication test
`Revision/tests/test_pair_creation_proofs_publication.py` reads both outputs, and
`Revision/tests/test_dirac16complex_field_theory_publication.py` reads `wolfram-t3.json`. A passing run
changes nothing for them. A failing run leaves a
theorem record with the status `SOME CHECKS FAILED - see the report` and a report with fewer passes; restore
both (section 5.4) before running the checker or the tests.

### 5.4 How to restore the committed state

From the repository root:

```text
git checkout -- Revision/pairing/kohn_sham/t3-theory.json Revision/pairing/kohn_sham/reports/wolfram-t3.json
```

If you deleted the folder `Revision/pairing/kohn_sham/reports/`, restore the whole folder with
`git checkout -- Revision/pairing/kohn_sham/reports`.

## 6. Verification record

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
