# WolframScript provenance: the a4 field-equation verifier

Set: `Revision/field_equations_a4/wolfram/` (the script `verify_field_equations_a4.wls` and its
package `FieldEquationsA4.wl`). This file tells you what the set computes, which files it reads and
writes, exactly how to run it, what you should see, what it changes on your computer, and how it
was verified. Everything you need to run it is in section 3 of this file.

## 1. What the set is and what it computes

In plain words: the author's theory lives in an 8-dimensional spacetime with coordinates
x1, x2, x3 (ordinary 3-space), x4 (time), x5, x6, x7 (three extra time directions) and x8 (a
hidden direction, written through z = 6 H x8 with 0 < z < pi/2). Distances in 3-space carry the
scale factor e^{a4(x4)} and distances along the extra times the scale factor e^{-a4(x4)} (both
times sin^{1/6} z), so when 3-space expands the extra times shrink; the single unknown function
is a4(x4). The set answers: which equations must a4(x4) obey, and what matter can drive it? The
task is defined in `Revision/SPEC.md`, section 5.

Step by step, the script (with its package) does the following, using exact algebra only (no
floating-point numbers anywhere):

1. Geometry. It writes down the metric, g = diag(e^{2 a4} s, e^{2 a4} s, e^{2 a4} s, -1,
   -e^{-2 a4} s, -e^{-2 a4} s, -e^{-2 a4} s, cot^2 z) with s = sin^{1/3} z, and computes from it
   the Christoffel symbols, the Riemann curvature tensor (sign convention of Misner, Thorne and
   Wheeler), the Ricci tensor and the Einstein tensor.
2. Lovelock tensors. It computes the three Lovelock tensors P_(1), P_(2), P_(3) (the
   generalisations of the Einstein tensor that exist in 8 dimensions) directly from the
   generalized Kronecker delta (computed as the determinant of a matrix of Kronecker deltas, as in
   the author's notebook), and compares all 64 components of each with an independent computation
   by a separate Rust program (its result is the input file `lovelock-tensors.json`). It also
   proves that P_(4) vanishes in 8 dimensions and that each normalised tensor E_(k) is
   divergence-free.
3. Field equations. It writes the Einstein-Lovelock field equations
   sum_k alpha_k E_(k)^mu_nu + Lambda delta^mu_nu = kappa T^mu_nu with a general source T and
   reduces them: a constraint (x4 component), an evolution equation a4'' F(a4') =
   kappa (p3 - p_t), an x8 equation, the algebraic condition p3 + p_t = 2 p8, the propagation of
   the constraint (Bianchi identity) and the conservation law of the source.
4. Special cases. Pure Einstein gravity (alpha1 = 1, alpha2 = alpha3 = 0): no vacuum solution and
   a violated null energy condition. The linear member a4 = A H x4 + a0: equal pressures, the
   vacuum condition, and the Einstein-Gauss-Bonnet vacuum.
5. Spinor sources. It builds its own real 16 x 16 representation of the Clifford algebra Cl(4,4)
   (eight real 16 x 16 Dirac matrices, see "The Dirac matrices of this set" below), the spin
   connection of the metric, and a homogeneous spinor condensate; it shows which bilinears must
   vanish and gives exact solutions (witnesses) for which they do.

Each of these statements is a named check with the verdict PASS or FAIL. There are 47 checks. The
script writes two files: `a4-equations.json` (every equation, in Wolfram InputForm and in TeX) and
`reports/wolfram-a4-report.json` (every check with name, verdict and a one-line explanation).

Documents and programs that cite or read these results (for your information only; you do not
need them to run this set):

* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): lists 36 checks
  of `wolfram-a4-report.json` by name in its record table, quotes the count "wolfram-a4-report 47",
  and generates its a4 equations and its table of off-diagonal kinetic coefficients from
  `a4-equations.json`.
* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and `.tex`, `.pdf`): "Wolfram: 47 of 47 checks
  pass"; names 26 of the checks in its derivation of the a4 equations; renders its a4 equations
  from `a4-equations.json`.
* `Revision/docs/PAIR_CREATION_PROOFS.md` (and `.tex`, `.pdf`): the record-table row for
  `wolfram-a4-report.json` (47 checks, 47 pass, 0 fail) and the checks
  `einstein_no_vacuum_solution`, `linear_member_vacuum_factor` and
  `einstein_gauss_bonnet_vacuum_linear` (the vacuum statements used in a proof).
* `Revision/README.md` ("Wolfram 47/47") and `Revision/field_equations_a4/README.md`.
* Programs that read the outputs: `Revision/field_equations_a4/python/check_field_equations_a4.py`
  (an independent sympy re-derivation; it reads `a4-equations.json`, so the Wolfram set runs
  first), `Revision/lead_checks/einstein_gauss_bonnet_a4.py` (reads `a4-equations.json`), the
  publication tests `Revision/tests/test_dirac16complex00_field_theory_publication.py` and
  `Revision/tests/test_dirac16complex_field_theory_publication.py` (they read both outputs), and the
  publication test `Revision/tests/test_pair_creation_proofs_publication.py` (it reads only
  `wolfram-a4-report.json`).
* Also citing or reading the outputs (found on 2026-10-07): `Revision/lead_checks/README.md`,
  `Revision/field_equations_a4/python/check_ks_source_conditions.py` (names checks of the report
  in its header), `Revision/gkd_lovelock/verification/WOLFRAMSCRIPT_PROVENANCE.md`, and twelve
  textbook notebooks under `Revision/textbook/notebooks/` (sources in `src/`: `00b`, `00c`, `02c`,
  `03b`, `09a`, `09c`, `11c`, `12a`, `12b`, `12c`, `12d`, `17a`), which read `a4-equations.json`
  and/or `wolfram-a4-report.json`. The textbook was still being written on that date (committed
  as "IN PROGRESS, not yet verified"); it is not part of this verification.

### The Dirac matrices of this set

The set uses eight real 16 x 16 Dirac matrices, but it does NOT read the author's matrices from
`Revision/algebra/gammas.json`: `FieldEquationsA4.wl` (lines 119-128) builds its own, as Kronecker
products of the real 2 x 2 matrices s1 = [[0,1],[1,0]], e = [[0,1],[-1,0]] and w = s1 e =
[[-1,0],[0,1]] (1 = the 2 x 2 unit matrix):

| direction | matrix (`FEGammaFrame`) | square |
| --- | --- | --- |
| x1, x2, x3 (3-space) | s1(x)1(x)1(x)1, w(x)s1(x)1(x)1, w(x)w(x)s1(x)1 | +1 |
| x4 (time) | e(x)1(x)1(x)1 | -1 |
| x5, x6, x7 (extra times) | w(x)e(x)1(x)1, w(x)w(x)e(x)1, w(x)w(x)w(x)e | -1 |
| x8 (hidden direction) | w(x)w(x)w(x)s1 | +1 |

The check `clifford_relations_own_rep` proves {g_a, g_b} = 2 eta_ab I16 with
eta = diag(1, 1, 1, -1, -1, -1, -1, 1) (x1..x8), and `C_properties_own_rep` the properties of
C = g_x8 g_x1 g_x2 g_x3. These matrices are not equal entry by entry to the author's (0 of 8 are
equal), but they are the author's matrices in another basis: an exact supplementary check made
during the verification of 2026-10-07 (the script is printed in section 6, with its output; it
needs a complete clone because it also reads `Revision/algebra/gammas.json`) constructs an integer
matrix S with S g_a S^-1 = G_a for all eight a (G_a = the author's matrices of `gammas.json`, same
eta and same coordinate order), S^T S = 128 I16 (so S/sqrt(128) is orthogonal) and
S C S^-1 = C_author (the author's sigma16) with S^T C_author S = 128 C. Hence every statement of
this set about spinors and bilinears holds word for word with the author's matrices (replace Phi by
S Phi / sqrt(128)). Independently, the Python companion `check_field_equations_a4.py` (not part of
this Wolfram set) repeats the spinor checks with the author's matrices (`authorT16_*`, all PASS in
`reports/python-a4-report.json`). The author's eight matrices themselves, their products and the
projectors are displayed and proved in `provenance/dirac matrices.md`.

## 2. The files of the set

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone`
creates). Every file is UTF-8 text with LF line endings, stored byte for byte by git
(`.gitattributes`: `* -text`).

| role | path | bytes | lines | sha256 |
| --- | --- | --- | --- | --- |
| script (the file you run) | `Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` | 34686 | 386 | `9cd8d9a1733102e1d57bdc6e3740972810793d3702a0b5e2b66ac7b3837d2965` |
| package (loaded by the script with `Get`) | `Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` | 8555 | 141 | `4ac40fef2a06d2f7587fdd4b0406d8399192ffb963312bceaea119ddd723c8f8` |
| input (read with `Import[..., "RawJSON"]`) | `Revision/gkd_lovelock/results/lovelock-tensors.json` | 55056 | 405 | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` |
| output 1 (written, committed) | `Revision/field_equations_a4/a4-equations.json` | 40843 | 788 | `98d3245d30e5c25f7bbdfcd186d5723aec2059a1feeaef4cc3c3249684de03b4` |
| output 2 (written, committed) | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 11814 | 244 | `2c070eda41303a6434a9860ce4bddd74510b2494e345332a8f82ddabee13857c` |

The script reads nothing else: no other file, no environment variable, no command-line argument,
no network resource. It finds its package and its input relative to its own location
(`$InputFileName`), so it does not depend on the folder you start it from. The input
`lovelock-tensors.json` is produced by a different set (the Rust program in
`Revision/gkd_lovelock/code`); it is committed, so you do not need Rust to run this set. The two
outputs are deterministic: LF line endings, no time stamps, no machine names, fixed key order.
The script contains no random numbers, no dates, no parallel computation and no network
functions; it writes only through its function `writeJSON` (one `OpenWrite`, script line 34),
which it calls twice (lines 378 and 383, one call per output).

The optional supplementary Dirac-matrix check of section 6 (not part of the set, not committed)
additionally reads `Revision/algebra/gammas.json` (sha256
`95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01`, the author's eight matrices)
and writes nothing.

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, with about 1 GB of free disk space for the
  repository (on 2026-10-07 the clone downloaded about 200 MB and then occupied about 690 MB, its
  hidden `.git` folder included; the repository grows over time, on 2026-10-02 it was 540 MB),
  several GB of free disk space for Wolfram itself (the Wolfram 15.0.1
  installation on the verification machine occupies about 9.3 GB) and about 0.3 GB of free memory
  for the Wolfram kernel.
* The Wolfram language engine with the command-line program `wolframscript`, either the free
  Wolfram Engine for Developers (option A) or a licensed Mathematica / Wolfram desktop product
  (option B). The verification used Wolfram 15.0.1 with WolframScript 1.14.0.
* Git, to download the repository.
* An internet connection for the downloads and for the one-time activation of Wolfram. The run
  itself does not use the network.

### 3.2 Install Wolfram

Option A, the free Wolfram Engine for Developers:

1. Open https://www.wolfram.com/engine/ in a web browser and choose the download for your
   operating system. You need a free Wolfram ID (an account at https://account.wolfram.com created
   with your own e-mail address). Read the licence terms on that page before you accept them.
2. Install it.
   * Windows: run the downloaded installer (`.exe`) and accept the default choices. It installs
     WolframScript into `C:\Program Files\Wolfram Research\WolframScript\` and adds it to the
     PATH. Close every open PowerShell window and open a new one afterwards, so that the new PATH
     is used.
   * macOS: open the downloaded `.dmg` and follow its instructions (drag the application into
     `Applications`; if the disk image also contains a WolframScript installer package, run it).
   * Linux: in a terminal, run the downloaded installer with `sudo bash <downloaded file name>.sh`
     and accept the default choices.
   * If after installation the command `wolframscript -version` (step 3.3) answers "not
     recognized" or "command not found", download WolframScript on its own from
     https://www.wolfram.com/wolframscript/ and install it.
3. Activate it once. In a terminal (PowerShell on Windows, Terminal on macOS or Linux) run
   `wolframscript -activate` (or simply `wolframscript`), and when asked, type your Wolfram ID and
   password. If you then see a prompt `In[1]:=`, type `Quit[]` and press Enter.

Option B, Mathematica or the Wolfram desktop product (licensed): WolframScript is installed
together with it. On Windows it is `C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`;
on macOS it is inside the application bundle: `/Applications/Wolfram.app/Contents/MacOS/wolframscript`
for the product named Wolfram (version 14.1 and later, which includes the verified Wolfram 15.0.1)
or `/Applications/Mathematica.app/Contents/MacOS/wolframscript` for older Mathematica versions
(the command `ls /Applications/*.app/Contents/MacOS/wolframscript` in Terminal shows which one you
have); on Linux the installer links it as `/usr/local/bin/wolframscript`. If the plain command
`wolframscript` is not found, use that full
path in place of `wolframscript` in every command below (in PowerShell put `& ` in front of a
quoted full path, for example `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -version`).

Do not run the script from inside a Mathematica notebook with `Get[...]`: its last line is
`Exit[...]`, which quits the notebook's kernel. Always use `wolframscript` in a terminal.

### 3.3 Check the installation

In a new terminal window type:

```text
wolframscript -version
wolframscript -code '$Version'
```

The first command prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`; the
second prints the Wolfram version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`.
(The single quotes around `$Version` are needed in PowerShell and in bash/zsh alike.) If the second
command asks for activation, do step 3 of option A.

### 3.4 Download the repository

Install Git from https://git-scm.com/downloads (on macOS, `git` is offered automatically the first
time you type `git` in Terminal; on Debian or Ubuntu Linux: `sudo apt install git`). Then, in a
terminal, in the folder where you keep your projects:

```text
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

From now on every command is typed in this folder, the repository root (it contains the folders
`Revision`, `scripts`, `wolfram`, `notebooks` and others, and the file `README.md`). A folder path
with spaces is fine; in `cd` commands put such a path in double quotes.

### 3.5 Run the set

Windows (PowerShell):

```powershell
cd C:\path\to\Dirac_claude
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
$LASTEXITCODE
```

macOS (Terminal, zsh or bash):

```bash
cd ~/path/to/Dirac_claude
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
echo $?
```

Linux (bash):

```bash
cd ~/path/to/Dirac_claude
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
echo $?
```

Replace `C:\path\to\Dirac_claude` or `~/path/to/Dirac_claude` with the folder that `git clone`
created. Forward slashes `/` in the script path work on all three systems (also in PowerShell).
The third line prints the exit code of the run. To also measure the time, use
`Measure-Command { wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls | Out-Default }`
in PowerShell, or put `time ` in front of the `wolframscript` command in bash/zsh.

The run prints nothing for about 20 to 35 seconds (it is computing) and then prints one line;
section 4 says exactly what to expect.

### 3.6 If it fails

* `wolframscript : The term 'wolframscript' is not recognized ...` (PowerShell) or
  `wolframscript: command not found` (macOS/Linux): Wolfram is not installed, or the terminal was
  opened before the installation. Open a new terminal; if that does not help, use the full path
  of `wolframscript` (option B in 3.2) or install WolframScript on its own (3.2, step 2).
* A request for a Wolfram ID and password, or a message that the engine is not activated or that
  the kernel could not be launched: activate it once with `wolframscript -activate` (needs
  internet).
* `Import::nffil: File ...lovelock-tensors.json not found during Import.`, followed by
  `Part::partd`, `Part::partw` and `General::stop` messages (all on standard output), the line
  `checks: 47, failed: 6` with six lines
  `FAIL P1_direct_equals_gkd_branch_monomials ...` to `FAIL L3_direct_equals_gkd_branch ...`, and
  exit code 1: the input file is missing, usually because only part of the repository was copied.
  Clone the whole repository (3.4). This failed run has overwritten the committed report with a
  FAIL report; restore it with
  `git checkout -- Revision/field_equations_a4/reports/wolfram-a4-report.json` (this exact failure
  was produced on purpose during the verification, section 6).
* `Get::noopen: Cannot open ...FieldEquationsA4.wl.` followed by many `Part::`, `ReplaceAll::`,
  `First::` and `General::stop` messages: the package file is missing. The run then does NOT
  finish by itself (during the verifications it was still running after 10 minutes, and in
  repeats after 3 minutes and after 2 minutes, and was stopped). Stop it by ending the Wolfram
  kernel process, which is how it was stopped during the verification: on Windows end
  `wolfram.exe` in the Task Manager (Details tab; if several are listed, end the one using CPU
  time); on macOS or Linux find the process number with `ps aux | grep -i wolfram` and end
  it with `kill <process number>`. Pressing Ctrl+C in the terminal may also work. After the kernel
  is ended, wolframscript prints the line `The product exited for an unknown reason.` (on the error
  stream) and ends with exit code `-1` (measured on Windows; `$LASTEXITCODE` then shows `-1`). This
  message only reports that you ended the kernel; it is not a new fault, and the two output files
  are not changed. Then restore the package with
  `git checkout -- Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` or clone again.
* `OpenWrite::noopen: Cannot open ...wolfram-a4-report.json.` (or `...a4-equations.json.`)
  followed by `BinaryWrite::stream` and `Close::stream`: the output folder is missing or the file
  is write-protected or open in a program that locks it. Note that the run may still print
  `checks: 47, failed: 0` and exit with code 0 although that file was NOT written (observed in
  both verifications with the `reports` folder deleted). Restore the folder with
  `git checkout -- Revision/field_equations_a4/reports`, close programs that hold the file, and run
  again.
* Any line beginning with `FAIL ` and a nonzero exit code although every file is present: a check
  did not pass. Write down the printed name, restore the outputs (section 5) and report it; do not
  edit the script. This did not happen in any verification run.
* The run takes much longer than a minute: a slow or busy computer (the measured kernel CPU time
  is about 20 to 23 s; see section 4). Wait; the computation needs no input from you.
* All 47 checks pass but `git status` shows `a4-equations.json` or `wolfram-a4-report.json` (or
  both) as modified: you are probably using a Wolfram version other than 15.0.1, whose TeX or
  InputForm formatting differs. Both files contain expressions formatted by Wolfram:
  `a4-equations.json` in InputForm and TeX, and the explanations in `wolfram-a4-report.json` in
  InputForm (for example `"detail": "L_(1) = 12*ad1^2 - 84*H^2"`). The mathematics (the 47 checks)
  is what matters; only Wolfram 15.0.1 was verified to reproduce the committed bytes. Restore both
  committed files with
  `git checkout -- Revision/field_equations_a4/a4-equations.json Revision/field_equations_a4/reports/wolfram-a4-report.json`.

## 4. Expected output

Printed on the screen (standard output), exactly one line:

```text
checks: 47, failed: 0
```

Nothing is printed on the error stream, no `FAIL` line appears, and the exit code is `0`
(`$LASTEXITCODE` in PowerShell, `echo $?` in bash/zsh). If a check failed, the line would read
`checks: 47, failed: <n>`, each failed check would be listed on a line
`FAIL <name>: <explanation>`, and the exit code would be `1`.

Files written (both are overwritten on every run):

1. `Revision/field_equations_a4/a4-equations.json` (40843 bytes, 788 lines). Its top-level keys
   are `title`, `producer`, `conventions`, `lovelockTensors`, `generalSource`, `einstein`,
   `linearMember`, `fields`, `checksSummary`; its second line is
   `  "title": "Einstein-Lovelock field equations for a4[x4] in the primordial metric (Revision/SPEC.md section 5)",`.
   For example `generalSource.evolution_F.input` is
   `2*alpha1 - 48*ad1^2*alpha2 + 720*ad1^4*alpha3 - 80*alpha2*H^2 + 864*ad1^2*alpha3*H^2 + 720*alpha3*H^4`
   (ad1 = a4').
2. `Revision/field_equations_a4/reports/wolfram-a4-report.json` (11814 bytes, 244 lines). Its first
   six lines are:

   ```text
   {
     "producer": "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls",
     "spec": "Revision/SPEC.md section 5",
     "checkCount": 47,
     "failedCount": 0,
     "verdict": "PASS",
   ```

   Show them with `Get-Content Revision/field_equations_a4/reports/wolfram-a4-report.json -TotalCount 6`
   (PowerShell) or `head -n 6 Revision/field_equations_a4/reports/wolfram-a4-report.json`
   (macOS/Linux). If Python is installed, this prints `47 0 PASS`:
   `python -c "import json; r=json.load(open('Revision/field_equations_a4/reports/wolfram-a4-report.json')); print(r['checkCount'], r['failedCount'], r['verdict'])"`
   (use `python3` on macOS/Linux).

How to check that you reproduced the committed results exactly:

* With git: `git status --porcelain` prints nothing (both outputs are byte-identical to the
  committed files, so git does not see a change).
* With checksums: `Get-FileHash Revision/field_equations_a4/a4-equations.json, Revision/field_equations_a4/reports/wolfram-a4-report.json -Algorithm SHA256`
  (PowerShell; it prints the hash in capital letters, compare ignoring case),
  `shasum -a 256 <file>` (macOS) or `sha256sum <file>` (Linux), and compare with the sha256 of
  the two output rows in section 2.

The 47 checks, in the order of the report (all PASS):

| section | checks |
| --- | --- |
| geometry (4) | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4`, `riemann_pair_antisymmetry` |
| Lovelock tensors (17) | `P1_direct_equals_minus_4_Einstein`; for k = 1, 2, 3: `Pk_direct_equals_gkd_branch_monomials`, `Lk_direct_equals_gkd_branch`, `Pk_trace_identity`, `Pk_structure`; `P4_vanishes_pigeonhole`, `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| field equations, general source (7) | `independent_components`, `evolution_factorises_a4pp_times_F`, `evolution_F_not_identically_zero`, `algebraic_identity_x1_plus_x5_minus_2x8`, `x8_component_contains_no_a4pp`, `constraint_propagation_bianchi`, `conservation_components` |
| Einstein case (3) | `einstein_components`, `einstein_null_energy_x8`, `einstein_no_vacuum_solution` |
| linear member (3) | `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `einstein_gauss_bonnet_vacuum_linear` |
| spinor sources (13) | `clifford_relations_own_rep`, `C_properties_own_rep`, `spin_connection_antisymmetric`, `Omega_x4_Omega_x8_vanish`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `gravity_term_gamma_mu_Omega_mu`, `condensate_equation_x8_consistent`, `condensate_S_constant`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears`, `condensate_einstein_quadratic_U`, `condensate_diagonal_witness_exact` |

Run time on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GB memory,
Windows 11 Pro for Workstations): on 2026-10-02, 18.9 s and 19.1 s (wall clock) for the two
fresh-clone runs and 20.4 s to 31.2 s for the repeat runs, with 20.1 s of kernel CPU time; on
2026-10-07, 33.6 s and 32.4 s for the two fresh-clone runs and 27.4 s to 33.7 s for the repeat
runs, with 21.8 s to 23.1 s of kernel CPU time. The machine was shared with other jobs during both
verifications (8 to 22 Wolfram kernels of other jobs running, CPU load 100 % during the runs of
2026-10-07), so these times are upper values for this machine; a slower laptop may need a minute
or two. Peak memory (working set): 226.5 MB to 227.0 MB for the Wolfram kernel and 16.7 MB to
17 MB for `wolframscript`.

## 5. Side effects

* Files in the repository OVERWRITTEN on every run that reaches its end (also when a check
  fails, see below): `Revision/field_equations_a4/a4-equations.json` and
  `Revision/field_equations_a4/reports/wolfram-a4-report.json`. On a successful run with Wolfram
  15.0.1 the new bytes are identical to the committed ones, so only the files' modification times
  change and `git status --porcelain` stays empty.
* A failed run overwrites the committed report with a report whose verdict is `FAIL` (and, if the
  equations came out differently, also `a4-equations.json`); `git status --porcelain` then shows
  ` M Revision/field_equations_a4/reports/wolfram-a4-report.json`.
* No other file in the repository is created, changed or deleted (checked with
  `git status --porcelain --ignored -uall`, which listed nothing after each checked successful
  run, and with a search for files written during a run). The script creates no folders and no
  temporary files of its own.
* Outside the repository, WolframScript itself (not this script) keeps small bookkeeping files in
  its per-user folders. On Windows these were written during the runs:
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\tmp_*` (files of 0 to about
  1.3 kB) and `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (both dates); also
  `%APPDATA%\Wolfram\Paclets\Temporary\pacletSiteData_15.lock` (2026-10-02) and
  `%APPDATA%\Wolfram\ApplicationData\ProcessLink\Streams\wl-stream-*` (2026-10-07) (macOS and
  Linux use the corresponding per-user Wolfram folders). Other Wolfram kernels were running at the same time on
  the verification machine, so these writes could not be attributed to this run alone. They are
  harmless and you never need to delete them.
* Processes: `wolframscript` starts two Wolfram processes one after the other (measured on
  2026-10-07 by listing the child processes of `wolframscript`): first a short licence query
  (`wolfram.exe -wlbanner -licenseinfo`, about 0.1 s of CPU time, it ends at once), then the
  kernel that runs the script (`wolfram.exe ... -linkmode Connect -linkname <name>_shm -mathlink`,
  connected to `wolframscript` through shared memory; on macOS and Linux the process name contains
  `wolfram` or `Wolfram`, for example `WolframKernel`). There are no parallel subkernels. The
  kernel quits at the end of the run (the script ends with `Exit[0]` or `Exit[1]`); no kernel was
  left running after any verification run.
* Network: none needed. The script contains no network functions. During a monitored run on
  2026-10-02 the only network connections of `wolframscript` and its kernel were local loopback
  connections (127.0.0.1) between the two programs; during a monitored run on 2026-10-07 (9
  samples of the TCP connections and UDP endpoints of `wolframscript` and both `wolfram.exe`
  processes) none was seen at all. The Wolfram licence on the verification machine is node-locked
  (`$NetworkLicense` is `False`), so no licence server was contacted.
* To restore the committed state after any run:

  ```text
  git checkout -- Revision/field_equations_a4/a4-equations.json Revision/field_equations_a4/reports/wolfram-a4-report.json
  git status --porcelain
  ```

  The second command must print nothing.

## 6. Verification record

The set was verified on 2026-10-02 (6.1) and verified again, from new fresh clones, on 2026-10-07
(6.2), after the workflow that wrote this file had been interrupted by a session limit; 6.3 lists
the open remarks. Both verifications give the same result: the set executes correctly and
reproduces both committed outputs byte for byte.

### 6.1 Verification of 2026-10-02

| item | value |
| --- | --- |
| date | 2026-10-02 |
| commits verified | run 1: `45d47343ae480df46e06689ed822b8f9a88a8030`; run 2: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the remote had advanced in between; the five files of section 2 are identical in both commits, `git diff 45d4734 c2b33cc` lists no change in them) |
| last commits that changed the files | `verify_field_equations_a4.wls` and `a4-equations.json`: `70fab64fca07c3e27d71355f308c09aeed560a9e`; `FieldEquationsA4.wl` and `wolfram-a4-report.json`: `2c61fb04bd4f607675b2d8122d60df933ecc8fa2`; `lovelock-tensors.json`: `ad02ebb5b3d944cb396ea6974679c528250818d7` (all 2026-10-01) |
| clones | two fresh `git clone https://github.com/once-ere/Dirac_claude.git` in a scratch folder, and a third one (commit `c2b33cc`) for the review corrections listed at the end of this section; no uncommitted file was copied in (none is needed by this set) |
| operating system | Windows 11 Pro for Workstations 10.0.26200, Intel Core Ultra 9 275HX (24 cores), 191 GB memory |
| Wolfram | Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence, `$ProcessorCount` 24, `$MaxLicenseProcesses` Infinity; WolframScript 1.14.0; kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe` |
| shells | PowerShell 7.6.6 and Git Bash (git 2.51.2.windows.1) |
| command | `wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` from the repository root |

Runs (all with the command above unless stated):

| run | where | exit code | printed line | wall time | peak memory (kernel) | outputs vs committed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | fresh clone 1 (commit 45d4734) | 0 | `checks: 47, failed: 0` | 18.9 s | 227.0 MB | both byte-identical |
| 2 | fresh clone 2 (commit c2b33cc) | 0 | `checks: 47, failed: 0` | 19.1 s | 226.2 MB | both byte-identical; also identical to run 1 |
| 1b | clone 1 again (over run 1's outputs) | 0 | `checks: 47, failed: 0` | 23.6 s | 227.0 MB | not compared on its own (run 1c overwrote its outputs before the comparison) |
| 1c | clone 1, started from the folder `Revision/field_equations_a4/wolfram` with `wolframscript -file verify_field_equations_a4.wls` | 0 | `checks: 47, failed: 0` | 20.4 s | not measured | both byte-identical |
| 3 | clone 2 again, network endpoints monitored | 0 | `checks: 47, failed: 0` | not measured | not measured | both byte-identical; loopback connections only |
| 4 | clone 1 again, CPU time measured | 0 | `checks: 47, failed: 0` | 27.8 s (kernel CPU 20.1 s; machine load 100 %, up to 22 kernels of other jobs) | not measured | both byte-identical |
| 5 | a minimal copy containing only the script, the package, the input and an empty `reports` folder (no outputs), in a folder whose path contains spaces | 0 | `checks: 47, failed: 0` | not measured | not measured | both written anew and byte-identical |
| 6 | fresh clone 3 (commit c2b33cc), after the repeated missing-package test below and the restore of the package, during the review of this file | 0 | `checks: 47, failed: 0` | 31.2 s (CPU load 100 %, 16 Wolfram kernels running) | not measured | both byte-identical; `git status --porcelain --ignored -uall` empty |

Byte identity, per output, over runs 1, 2, 1c, 3, 4, 5 and 6 (compared with `cmp` and `sha256sum`,
or with `git status`, which compares content because the files are stored byte for byte):

| output | sha256 in every run | identical to committed | identical between runs |
| --- | --- | --- | --- |
| `Revision/field_equations_a4/a4-equations.json` | `98d3245d30e5c25f7bbdfcd186d5723aec2059a1feeaef4cc3c3249684de03b4` | yes | yes |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `2c070eda41303a6434a9860ce4bddd74510b2494e345332a8f82ddabee13857c` | yes | yes |

The captured standard output of runs 1, 1b, 2, 3 and 4 was the 21 characters
`checks: 47, failed: 0` followed by the Windows console line ending CR LF (23 bytes in all); the
captured error stream of runs 1, 1b, 2 and 3 was empty (0 bytes). `git status --porcelain
--ignored -uall` in the clones was empty after runs 1, 2, 1c, 3 and 4. Check counts: 47 checks,
47 PASS, 0 FAIL.

Deliberate failure tests (in scratch copies, then restored), recorded so that section 3.6 states
measured behaviour:

* `lovelock-tensors.json` removed: `Import::nffil` message, `checks: 47, failed: 6` (the six
  comparisons with the Rust results: `P1/P2/P3_direct_equals_gkd_branch_monomials`,
  `L1/L2/L3_direct_equals_gkd_branch`), exit code 1, report overwritten with `"verdict": "FAIL"`;
  `a4-equations.json` was still byte-identical (it does not depend on that input). Restored with
  `git checkout`.
* `reports` folder removed: `OpenWrite::noopen`, `BinaryWrite::stream`, `Close::stream`; the
  report was not written, but the run printed `checks: 47, failed: 0` and exited with code 0.
* `FieldEquationsA4.wl` removed: `Get::noopen` and cascading messages; the run had not finished
  after 10 minutes (546 s of kernel CPU time) and was stopped by ending the kernel process.
  Repeated in a third fresh clone (commit `c2b33cc`) with the documented command: on standard
  output `Get::noopen` (1), `Part::partd` (3), `Part::partw` (3), `ReplaceAll::reps` (3),
  `Part::pkspec1` (1), `First::nofirst` (3) and `General::stop` (4) messages (1740 bytes); the run
  was still going after 188 s (128.7 s of kernel CPU time). Ending only this run's kernel
  (`wolfram.exe`, the child process of this run's `wolframscript`) made `wolframscript` exit within
  0.1 s with exit code -1 and the 42 bytes `The product exited for an unknown reason.` plus LF on
  the error stream. Both outputs were unchanged (sha256 as in section 2); `git checkout --
  Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` restored the package (sha256
  `4ac40fef...c8f8`) and `git status --porcelain` was then empty.

Fixes made: none. The set executes correctly and reproduces both committed outputs byte for byte;
no file of the set was changed.

Corrections to this provenance file after an independent review (2026-10-02), each re-checked in
fresh clone 3 (commit `c2b33cc`); none changes a result:

* Section 3.4: the repository root was described as containing `dirac-main`; that folder is
  ignored by `.gitignore` (line 282, `/dirac-main/`) and is not in a clone (`git ls-tree
  --name-only HEAD` lists `.cargo`, `.gitattributes`, `.gitignore`, the two author notebooks,
  `HANDOFF.md`, `HANDOFF.md.txt`, `LICENSE`, `NOTICE`, `README.md`, `Revision`, `artifacts`,
  `handoff`, `notebooks`, `provenance`, `requirements-stage3.txt`, `scripts`, `studies`, `tests`,
  `wolfram`). The text now names `Revision`, `scripts`, `wolfram`, `notebooks` and `README.md`.
* Section 3.1: disk space. Measured in the fresh clone: pack 126.99 MiB (`git count-objects -vH`),
  whole clone 538,056,938 bytes (`du -sb .`; 543,998,976 bytes allocated on disk), `.git`
  133,534,691 bytes, working tree without `.git` 404,522,247 bytes; the Wolfram 15.0.1
  installation folder 9,334,034,004 bytes. The text said 0.5 GB and 390 MB and gave no figure for
  Wolfram.
* Section 3.6, last item: `wolfram-a4-report.json` also holds InputForm-formatted expressions
  (its `detail` texts are built with `inp[...]`, script lines 94, 132, 186, 283-284), so it is now
  named and restored together with `a4-equations.json`; the two-file `git checkout` command was
  tested (both files altered, restored, `git status --porcelain` empty, sha256 as in section 2).
* Section 1, last item: `test_pair_creation_proofs_publication.py` reads only
  `wolfram-a4-report.json` (its line 77); the other two publication tests read both outputs.
* Section 3.6, missing-package item: the message and exit code after the kernel is ended (the
  repeated failure test above).
* Section 3.2, option B: the macOS path now gives `/Applications/Wolfram.app/...` (product named
  Wolfram) and `/Applications/Mathematica.app/...` (older Mathematica) and a command to find it.
  Evidence for `Wolfram.app`: the Wolfram 15.0.1 installation's own files use it, for example
  `SystemFiles/Components/KernelObjects/Kernel/Evaluators/SshKernels.wl` (default macOS kernel
  command `/Applications/Wolfram.app/Contents/MacOS/wolfram`) and
  `SystemFiles/Links/WSTPServer/wstpserver.conf-sample`
  (`/Applications/Wolfram.app/Contents/MacOS/WolframKernel`). Not verified on a Mac.

### 6.2 Re-verification of 2026-10-07

| item | value |
| --- | --- |
| date | 2026-10-07 |
| commits verified | clones 1 and 2: `a4c5eda1df069a43a55ff8b57148f5de8edd1670`; clone 3: `cb6e78fcd8fdd3f6b360cdd6ad9d8f51e6453bbd` (the remote had advanced in between; `git diff a4c5eda cb6e78f` changes no file of section 2, nor `Revision/algebra/gammas.json`). The five files of section 2 are unchanged since the verification of 6.1 (same sha256, same last commits) |
| clones | three fresh `git clone https://github.com/once-ere/Dirac_claude.git` in a scratch folder; no uncommitted file was copied in (none is needed by this set) |
| operating system | Windows 11 Pro for Workstations 10.0.26300, Intel Core Ultra 9 275HX (24 cores), 191 GB memory |
| Wolfram | Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence, `$ProcessorCount` 24, `$MaxLicenseProcesses` Infinity, `$NetworkLicense` False; WolframScript 1.14.0; kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe` |
| shells | PowerShell 7.6.6 (runs started with `Start-Process wolframscript -ArgumentList '-file', ...` from the clone root, standard output and error redirected to files, the child processes sampled every 0.2 s for memory and CPU time) and Git Bash (git 2.51.2.windows.1) for the comparisons |
| command | `wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` from the repository root |

Runs (machine load: CPU 99-100 % from other jobs, 8 to 17 other Wolfram kernels running):

| run | where | exit code | printed line | wall time | kernel CPU | peak memory (kernel / wolframscript) | outputs vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fresh clone 1 (`a4c5eda`) | 0 | `checks: 47, failed: 0` | 33.6 s | not measured | not measured / 16.7 MB | both byte-identical |
| 2 | fresh clone 2 (`a4c5eda`) | 0 | `checks: 47, failed: 0` | 32.4 s | 21.8 s | 226.8 MB / 16.7 MB | both byte-identical; also identical to run 1 |
| 3 | clone 1 again (over run 1's outputs) | 0 | `checks: 47, failed: 0` | 33.2 s | 23.1 s | 226.6 MB / 16.7 MB | both byte-identical |
| 4 | clone 2, started from the folder `Revision/field_equations_a4/wolfram` with `wolframscript -file verify_field_equations_a4.wls` | 0 | `checks: 47, failed: 0` | 27.4 s | 22.5 s | 227.0 MB / 16.8 MB | both byte-identical |
| 5 | fresh clone 3 (`cb6e78f`), after the three failure tests below and the restores | 0 | `checks: 47, failed: 0` | 32.4 s | 21.8 s | 226.5 MB / 16.7 MB | both byte-identical |
| 6 | clone 2 again, network endpoints monitored | 0 | `checks: 47, failed: 0` | 33.7 s | not measured | not measured | both byte-identical; no TCP connection or UDP endpoint seen |

In run 1 the sampler picked up the short licence-query process first (section 5, processes) and
lost the kernel, so its kernel memory and CPU time were not measured; the sampler was corrected
before run 2 (it then follows every child process of `wolframscript`).

Byte identity, per output, over runs 1 to 6 (compared with `cmp` against the committed bytes taken
with `git show HEAD:<path>`, with `sha256sum`, and with `git status --porcelain --ignored -uall`,
which was empty after every run; the modification times show that every run rewrote both files):

| output | sha256 in every run | identical to committed | identical between runs |
| --- | --- | --- | --- |
| `Revision/field_equations_a4/a4-equations.json` | `98d3245d30e5c25f7bbdfcd186d5723aec2059a1feeaef4cc3c3249684de03b4` | yes | yes |
| `Revision/field_equations_a4/reports/wolfram-a4-report.json` | `2c070eda41303a6434a9860ce4bddd74510b2494e345332a8f82ddabee13857c` | yes | yes |

The captured standard output of every run was the 23 bytes `checks: 47, failed: 0` plus CR LF; the
error stream was empty (0 bytes). Check counts: 47 checks, 47 PASS, 0 FAIL, in every run. The
kernel of each of runs 2 to 5 had ended when `wolframscript` returned (checked by its process
number).

Failure tests repeated in fresh clone 3 (each restored afterwards, `git status --porcelain
--ignored -uall` then empty), all with the behaviour stated in section 3.6:

* `lovelock-tensors.json` removed: `Import::nffil`, `Part::partd`, `Part::partw`, `General::stop`
  on standard output (2375 bytes in all), `checks: 47, failed: 6` and the six `FAIL` lines of the
  comparisons with the Rust results, exit code 1, 34.8 s; the report was overwritten with
  `"failedCount": 6` and `"verdict": "FAIL"` (` M` in `git status`), `a4-equations.json` stayed
  byte-identical. Restored with
  `git checkout -- Revision/field_equations_a4/reports/wolfram-a4-report.json Revision/gkd_lovelock/results/lovelock-tensors.json`.
* `reports` folder removed: `OpenWrite::noopen`, `BinaryWrite::stream`, `Close::stream` (461 bytes
  on standard output), then `checks: 47, failed: 0` and exit code 0 although the report was not
  written. Restored with `git checkout -- Revision/field_equations_a4/reports`.
* `FieldEquationsA4.wl` removed: `Get::noopen` (1), `Part::partd` (3), `Part::partw` (3),
  `ReplaceAll::reps` (3), `Part::pkspec1` (1), `First::nofirst` (3), `General::stop` (4) on standard
  output (1736 bytes); still running after 120.9 s (98.5 s of kernel CPU time); ending this run's
  kernel made `wolframscript` exit 0.13 s later with exit code -1 and the 42 bytes
  `The product exited for an unknown reason.` plus LF on the error stream; both outputs unchanged.
  Restored with `git checkout -- Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` (sha256
  `4ac40fef...c8f8` again).

Supplementary Dirac-matrix check (not part of the set; it answers whether this set computes with
eight real 16 x 16 Dirac matrices, see "The Dirac matrices of this set" in section 1). The script
below (50 lines, 4288 bytes, sha256
`f123a5d93d3ff93fd1a3ecc7564e18f2b81ef4d625331afd08a9aad5efacd7ab`, LF) was run from the root of
fresh clones 1 and 2 with `wolframscript -file <path>/dirac_crosscheck.wls`: exit code 0, about 5 s
(5.3 s measured), nothing written (`git status --porcelain --ignored -uall` empty). To run it
yourself, save the text between the fences as `dirac_crosscheck.wls` outside the repository (for
example in your home folder) and run the command above from the repository root.

```text
#!/usr/bin/env wolframscript
(* dirac_crosscheck.wls - optional supplementary check printed in section 6.2 of
   Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md; not part of the set.
   Usage: save this file outside the repository, then, from the repository root:
     wolframscript -file <path to>/dirac_crosscheck.wls
   Compares the real 16 x 16 representation built in FieldEquationsA4.wl (FEGammaFrame, FEC) with the
   author's eight real 16 x 16 Dirac matrices as stored in Revision/algebra/gammas.json, exactly.
   Writes nothing; exit code 0 iff every check passes. *)
root = Directory[];
Get[FileNameJoin[{root, "Revision", "field_equations_a4", "wolfram", "FieldEquationsA4.wl"}]];
js = Import[FileNameJoin[{root, "Revision", "algebra", "gammas.json"}], "RawJSON"];
gA = js["gamma"]; CA = js["C"]; etaA = js["eta"];
gF = FEGammaFrame; id = IdentityMatrix[16];
res = {};
chk[name_, ok_, det_] := (AppendTo[res, {name, TrueQ[ok]}]; Print[If[TrueQ[ok], "PASS ", "FAIL "], name, ": ", det]);

chk["own_rep_eight_real_16x16", Length[gF] == 8 && And @@ (Dimensions[#] == {16, 16} & /@ gF) &&
   Union[Flatten[gF]] === {-1, 0, 1}, "8 matrices, each 16 x 16, entries in {-1, 0, 1} (integers, hence real)"];
chk["own_rep_clifford", And @@ Flatten[Table[gF[[a]] . gF[[b]] + gF[[b]] . gF[[a]] == 2 FEEta[[a, b]] id, {a, 8}, {b, 8}]],
   "{g_a, g_b} = 2 eta_ab I16, eta = " <> ToString[Diagonal[FEEta]]];
chk["same_signature_and_order", Diagonal[FEEta] === etaA, "eta of FieldEquationsA4.wl = eta of gammas.json = " <> ToString[etaA] <> " (x1..x8)"];
chk["author_rep_eight_real_16x16", Length[gA] == 8 && Union[Flatten[gA]] === {-1, 0, 1} &&
   And @@ Flatten[Table[gA[[a]] . gA[[b]] + gA[[b]] . gA[[a]] == 2 etaA[[a]] KroneckerDelta[a, b] id, {a, 8}, {b, 8}]],
   "gammas.json: 8 real 16 x 16 matrices with {G_a, G_b} = 2 eta_ab I16"];
nEqual = Count[Table[gF[[a]] === gA[[a]], {a, 8}], True];
Print["INFO matrices equal entry by entry (own vs author): ", nEqual, " of 8"];
chk["transpose_pattern_both", And @@ Table[Transpose[gF[[a]]] === etaA[[a]] gF[[a]] && Transpose[gA[[a]]] === etaA[[a]] gA[[a]], {a, 8}],
   "g_a^T = eta_aa g_a for both sets (so every matrix is orthogonal)"];

(* intertwiner S = sum_I G_I X g_I^T over the 256 ordered products (g_I orthogonal, so g_I^-1 = g_I^T) *)
subsets = Subsets[Range[8]];
prod[m_, I_] := If[I === {}, id, Dot @@ (m[[#]] & /@ I)];
mk[X_] := Sum[prod[gA, I] . X . Transpose[prod[gF, I]], {I, subsets}];
S = Null; Do[With[{X = SparseArray[{{i, j} -> 1}, {16, 16}] // Normal}, Module[{t = mk[X]}, If[t =!= ConstantArray[0, {16, 16}], S = t; Print["INFO seed X = E_", i, ",", j]; Break[]]]], {i, 16}, {j, 16}];
Print["INFO S entries: ", Union[Flatten[S]]];
chk["intertwiner_invertible", S =!= Null && Det[S] =!= 0, "det S = " <> ToString[Det[S]]];
chk["intertwiner_maps_all_eight", And @@ Table[S . gF[[a]] === gA[[a]] . S, {a, 8}], "S g_a = G_a S for a = x1..x8, i.e. G_a = S g_a S^-1"];
lam = (Transpose[S] . S)[[1, 1]];
chk["intertwiner_orthogonal_up_to_scale", Transpose[S] . S === lam id, "S^T S = " <> ToString[lam] <> " I16 (so S/Sqrt[" <> ToString[lam] <> "] is orthogonal)"];
chk["C_maps_to_author_C", S . FEC . Inverse[S] === CA && Transpose[S] . CA . S === lam FEC,
   "S C S^-1 = C_author (gammas.json C = sigma16) and S^T C_author S = lam C: the bilinear form Phibar Psi = Phi^T C Psi is carried to the author's"];
signedPermQ[m_] := And @@ (Count[#, 0] == 15 &) /@ m && And @@ (Count[#, 0] == 15 &) /@ Transpose[m];
chk["own_rep_signed_permutations", And @@ (signedPermQ /@ gF), "each g_a has exactly one nonzero entry (+1 or -1) in every row and every column"];
compact[m_] := "[" <> StringRiffle[Table[With[{j = First[FirstPosition[m[[i]], x_ /; x != 0]]}, If[m[[i, j]] > 0, "+", "-"] <> ToString[j]], {i, 16}], ", "] <> "]";
coord = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
Do[Print["ROW g_", coord[[a]], " = ", compact[gF[[a]]]], {a, 8}];
Print["ROW C = g_x8 g_x1 g_x2 g_x3 = ", compact[FEC]];
Print["ROW S/8 rows (column:sign): ", StringRiffle[Table[StringRiffle[(ToString[#] <> ":" <> If[S[[i, #]] > 0, "+", "-"]) & /@ Flatten[Position[S[[i]], x_ /; x != 0]], " "], {i, 16}], " | "]];
Print["checks: ", Length[res], ", failed: ", Count[res, {_, False}]];
Exit[If[Count[res, {_, False}] == 0, 0, 1]];
```

Its output (identical in both clones; sha256 of the output with LF line endings
`c6e62f5d7d5a2ca2b9a2d8ead76ee28bf2a4b2fdc75a5e7ed5d498984412265b`):

```text
PASS own_rep_eight_real_16x16: 8 matrices, each 16 x 16, entries in {-1, 0, 1} (integers, hence real)
PASS own_rep_clifford: {g_a, g_b} = 2 eta_ab I16, eta = {1, 1, 1, -1, -1, -1, -1, 1}
PASS same_signature_and_order: eta of FieldEquationsA4.wl = eta of gammas.json = {1, 1, 1, -1, -1, -1, -1, 1} (x1..x8)
PASS author_rep_eight_real_16x16: gammas.json: 8 real 16 x 16 matrices with {G_a, G_b} = 2 eta_ab I16
INFO matrices equal entry by entry (own vs author): 0 of 8
PASS transpose_pattern_both: g_a^T = eta_aa g_a for both sets (so every matrix is orthogonal)
INFO seed X = E_1,1
INFO S entries: {-8, 0, 8}
PASS intertwiner_invertible: det S = 72057594037927936
PASS intertwiner_maps_all_eight: S g_a = G_a S for a = x1..x8, i.e. G_a = S g_a S^-1
PASS intertwiner_orthogonal_up_to_scale: S^T S = 128 I16 (so S/Sqrt[128] is orthogonal)
PASS C_maps_to_author_C: S C S^-1 = C_author (gammas.json C = sigma16) and S^T C_author S = lam C: the bilinear form Phibar Psi = Phi^T C Psi is carried to the author's
PASS own_rep_signed_permutations: each g_a has exactly one nonzero entry (+1 or -1) in every row and every column
ROW g_x1 = [+9, +10, +11, +12, +13, +14, +15, +16, +1, +2, +3, +4, +5, +6, +7, +8]
ROW g_x2 = [-5, -6, -7, -8, -1, -2, -3, -4, +13, +14, +15, +16, +9, +10, +11, +12]
ROW g_x3 = [+3, +4, +1, +2, -7, -8, -5, -6, -11, -12, -9, -10, +15, +16, +13, +14]
ROW g_x4 = [+9, +10, +11, +12, +13, +14, +15, +16, -1, -2, -3, -4, -5, -6, -7, -8]
ROW g_x5 = [-5, -6, -7, -8, +1, +2, +3, +4, +13, +14, +15, +16, -9, -10, -11, -12]
ROW g_x6 = [+3, +4, -1, -2, -7, -8, +5, +6, -11, -12, +9, +10, +15, +16, -13, -14]
ROW g_x7 = [-2, +1, +4, -3, +6, -5, -8, +7, +10, -9, -12, +11, -14, +13, +16, -15]
ROW g_x8 = [-2, -1, +4, +3, +6, +5, -8, -7, +10, +9, -12, -11, -14, -13, +16, +15]
ROW C = g_x8 g_x1 g_x2 g_x3 = [-16, -15, +14, +13, -12, -11, +10, +9, +8, +7, -6, -5, +4, +3, -2, -1]
ROW S/8 rows (column:sign): 1:+ 11:- | 7:+ 13:+ | 1:- 11:- | 7:+ 13:- | 6:- 16:+ | 4:- 10:- | 6:- 16:- | 4:+ 10:- | 2:- 12:+ | 8:- 14:- | 2:+ 12:+ | 8:- 14:+ | 5:- 15:+ | 3:- 9:- | 5:- 15:- | 3:+ 9:-
checks: 10, failed: 0
```

How to read the `ROW` lines: every matrix of this set has exactly one nonzero entry in each row,
so it is written as the list of its 16 rows, each entry giving the column of that row's nonzero
entry and its sign (for example `g_x1`: row 1 has +1 in column 9, ..., row 16 has +1 in column 8).
The last line lists, for each of the 16 rows of S/8, its two nonzero entries (column:sign).

Fixes made on 2026-10-07: none. No file of the set was changed (the sha256 of section 2 are those
of the committed files). Corrections to this provenance file on 2026-10-07 (none changes a result):
section 1 (the readers found on 2026-10-07; the subsection on the Dirac matrices of this set),
section 2 (the remark on random numbers, dates, parallel and network functions; the input of the
supplementary check), section 3.1 (clone size measured in fresh clone 3: pack 194.28 MiB,
whole clone 691,452,948 bytes, `.git` 204,183,417 bytes), sections 3.5 and 3.6 (run times and the
repeated failure tests), section 4 (run times and memory of 6.2), section 5 (the licence-query
process started by `wolframscript` before the kernel, which the earlier text missed when it said
"exactly one Wolfram kernel"; the files written in the Wolfram user folders; the network
observation of 2026-10-07) and this section.

### 6.3 Open discrepancies and remarks

Open discrepancies in the results: none. The 47 checks pass and both outputs are reproduced byte
for byte on both dates. Remarks that do not affect a run from a complete clone:

* (a) `Revision/field_equations_a4/README.md` states "about 15 s" for the Wolfram run; the
  measured wall times on the loaded verification machine were 18.9 s to 31.2 s (2026-10-02) and
  27.4 s to 33.7 s (2026-10-07), with 20.1 s to 23.1 s of kernel CPU time.
* (b) The script does not stop with an error message and a nonzero exit code when an output file
  cannot be written (it exits with code 0) or when its package is missing (it does not finish);
  see the failure tests of 6.1 and 6.2. Neither can happen in a complete clone, because the
  package and the `reports` folder are committed; the script was left unchanged so that the
  verified files are exactly the committed ones.
* (c) Dirac matrices: this set computes with its own eight real 16 x 16 matrices (built in
  `FieldEquationsA4.wl`), not with the author's matrices read from `Revision/algebra/gammas.json`.
  The supplementary check of 6.2 proves exactly that they are the author's matrices in an
  orthogonally changed basis, so no result of this set depends on the choice. The sentence of
  `provenance/dirac matrices.md` (section "Calculations that use these matrices") that "Every
  Revision calculation and every textbook notebook reads its gamma matrices from
  `Revision/algebra/gammas.json`" is therefore not literally true for this set; its list of the
  60 files that read `gammas.json` correctly does not include this set. That file was not changed
  by this verification.
