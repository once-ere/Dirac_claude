# WolframScript provenance: the a4 field-equation verifier

Set: `Revision/field_equations_a4/wolfram/` (the script `verify_field_equations_a4.wls` and its
package `FieldEquationsA4.wl`), in the version of commit `e377368` (2026-10-08), which computes
every spinor statement with the author's real 16 x 16 Dirac matrices T16. This file tells you what
the set computes, which files it reads and writes, exactly how to run it, what you should see,
what it changes on your computer, and how it was verified. Everything you need to run it is in
section 3 of this file.

## 1. What the set is and what it computes

In plain words: the author's theory lives in an 8-dimensional spacetime with coordinates
x1, x2, x3 (ordinary 3-space), x4 (time), x5, x6, x7 (three extra time directions) and x8 (a
hidden direction, written through z = 6 H x8 with 0 < z < pi/2). Distances in 3-space carry the
scale factor e^{a4(x4)} and distances along the extra times the scale factor e^{-a4(x4)} (both
times sin^{1/6} z), so when 3-space expands the extra times shrink exponentially (they deflate);
the single unknown function is a4(x4). The set answers: which equations must a4(x4) obey, and what
matter can drive it? The task is defined in `Revision/SPEC.md`, section 5; the Dirac matrices are
those of SPEC section 2.

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
5. Spinor sources. It reads the author's eight real 16 x 16 Dirac matrices T16 from
   `Revision/algebra/gammas.json` (see "The Dirac matrices of this set" below) and uses them for
   every spinor statement: the spin connection of the metric and a homogeneous spinor condensate;
   it shows which bilinears must vanish and gives exact solutions (witnesses) for which they do.
   It also builds a second real 16 x 16 representation of the Clifford algebra Cl(4,4), used only
   for comparison: it proves exactly that the two representations are equivalent and that the
   off-diagonal coefficients it writes do not depend on the representation.

Each of these statements is a named check with the verdict PASS or FAIL. There are 52 checks. The
script writes two files: `a4-equations.json` (every equation, in Wolfram InputForm and in TeX) and
`reports/wolfram-a4-report.json` (every check with name, verdict and a one-line explanation).

Documents and programs that cite or read these results (found on 2026-10-08, for your information
only; you do not need them to run this set):

* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): quotes the count
  "wolfram-a4-report 52"; 41 of the 52 check names appear in it; it generates its a4 equations and
  its table of off-diagonal kinetic coefficients from `a4-equations.json`.
* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and `.tex`, `.pdf`): "Wolfram: 52 of 52 checks
  pass"; 26 of the check names appear in its derivation of the a4 equations; it renders its a4
  equations from `a4-equations.json`.
* `Revision/docs/PAIR_CREATION_PROOFS.md` (and `.tex`, `.pdf`): the record-table row for
  `wolfram-a4-report.json` (52 checks, 52 pass, 0 fail) and the checks
  `einstein_no_vacuum_solution`, `linear_member_vacuum_factor` and
  `einstein_gauss_bonnet_vacuum_linear` (the vacuum statements used in a proof).
* `Revision/README.md` ("Wolfram 52/52") and `Revision/field_equations_a4/README.md`.
* Programs that read the outputs: `Revision/field_equations_a4/python/check_field_equations_a4.py`
  (an independent sympy re-derivation; it reads `a4-equations.json`, so the Wolfram set runs
  first), `Revision/lead_checks/einstein_gauss_bonnet_a4.py` (reads `a4-equations.json`), the
  publication tests `Revision/tests/test_dirac16complex00_field_theory_publication.py` and
  `Revision/tests/test_dirac16complex_field_theory_publication.py` (they read both outputs), and the
  publication test `Revision/tests/test_pair_creation_proofs_publication.py` (it reads only
  `wolfram-a4-report.json`).
* Also citing the set or its outputs: `Revision/lead_checks/README.md`,
  `Revision/field_equations_a4/python/check_ks_source_conditions.py` (names checks of the report in
  its header), `Revision/gkd_lovelock/verification/WOLFRAMSCRIPT_PROVENANCE.md`,
  `provenance/dirac matrices.md` (its script `provenance/dirac_matrices/extract_repository_wolfram_gammas.wls`
  loads `FieldEquationsA4.wl` to compare its matrices with the author's), `HANDOFF.md`, records
  under `Revision/workflows/`, and the textbook under `Revision/textbook/` (chapters and fifteen
  notebooks, sources in `notebooks/src/`: `00b`, `00c`, `02c`, `03b`, `09a`, `09c`, `11c`, `12a`,
  `12b`, `12c`, `12d`, `17a`, `17b`, `20a`, `20b`, which read `a4-equations.json` and/or
  `wolfram-a4-report.json`). The textbook is written and verified by another workflow; it is not
  part of this verification.

### The Dirac matrices of this set

`Revision/SPEC.md` section 2 (binding for every file under `Revision/`) requires the author's real
16 x 16 matrices T16 of the notebook, re-constructed in Revision code from the author's formulas,
with gamma^(x8) = T16[0], gamma^(x1..x3) = T16[1..3], gamma^(x4) = T16[4],
gamma^(x5..x7) = T16[5..7]. They are re-constructed by `Revision/algebra/wolfram/RevisionAlgebra.wl`
(from the tau matrices of the notebook) and stored, in the order x1..x8, in
`Revision/algebra/gammas.json` by `Revision/algebra/wolfram/verify_algebra.wls`.

This set follows that instruction: `FieldEquationsA4.wl` (lines 126-185) reads `gammas.json` when
it is loaded, with strict parsing (every matrix entry must be a JSON integer or a string "p/q" in
lowest terms; anything else, or a missing file or key, stops the run with a line `ERROR  ...` and
exit code 1, section 3.6; there is no fallback to other matrices). The primary matrices are
`FEGammaFrame` = the fixture's eight gammas (gamma^(x1..x7) = T16[1..7], gamma^(x8) = T16[0]) and
`FEC` = gamma^x8 gamma^x1 gamma^x2 gamma^x3 (the notebook's sigma16). The checks
`fixture_author_T16_read`, `clifford_relations_author_T16` ({gamma^a, gamma^b} = 2 eta^ab with
eta = diag(1, 1, 1, -1, -1, -1, -1, 1) in the order x1..x8) and `C_properties_author_T16` (C equals
the fixture's C, is real symmetric, C^2 = 1, C gamma^a antisymmetric) record this; every spinor
check after them uses these matrices.

The package also builds, in lines 187-194, a comparison representation `FEGammaFrameComparison`
(with `FECComparison`), from Kronecker products of the real 2 x 2 matrices s1 = [[0,1],[1,0]],
e = [[0,1],[-1,0]] and w = s1 e = [[-1,0],[0,1]] (1 = the 2 x 2 unit matrix):

| direction | matrix (`FEGammaFrameComparison`) | square |
| --- | --- | --- |
| x1, x2, x3 (3-space) | s1(x)1(x)1(x)1, w(x)s1(x)1(x)1, w(x)w(x)s1(x)1 | +1 |
| x4 (time) | e(x)1(x)1(x)1 | -1 |
| x5, x6, x7 (extra times) | w(x)e(x)1(x)1, w(x)w(x)e(x)1, w(x)w(x)w(x)e | -1 |
| x8 (hidden direction) | w(x)w(x)w(x)s1 | +1 |

It is used for no result. Its checks are `clifford_relations_own_rep`, `C_properties_own_rep`,
`representations_equivalent_author_T16_own_rep` (exactly, by `NullSpace` over the rationals: the
matrices K with K g_a = G_a K for all eight a, g_a the comparison matrices and G_a the author's,
form a space of dimension 1, K^T K = 2 I16 and K C_R = C_T16 K) and
`offdiagonal_coefficients_representation_independent` (the whole condensate pipeline run in the
comparison representation gives the same 42 nonzero off-diagonal kinetic components with exactly
the same coefficients). The condensate-witness values S = 51200, 28800, 51200 of the check
`condensate_diagonal_witness_exact` are those of T16; they scale with the normalisation of the null
vectors and differ in another basis (explained in `Revision/field_equations_a4/README.md`).

History: before commit `e377368` the set used the Kronecker-product matrices above as its only
matrices (named `FEGammaFrame` then) and did not read `gammas.json`. That departed from SPEC
section 2, and the earlier version of this file did not say so (finding of the independent
verifier of 2026-10-07, section 6.4). It was covered at the time by an exact intertwiner check and
by the Python companion's `authorT16_*` checks; the patch of commit `e377368` removed the
departure. The optional supplementary check of section 6.3 confirms, for the current files, that
`FEGammaFrame` and `FEC` are the matrices of `gammas.json` entry by entry (8 of 8) and that the
comparison representation is equivalent to them by a second, independent construction of the
intertwiner.

## 2. The files of the set

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone`
creates). Every file is UTF-8 text with LF line endings, stored byte for byte by git
(`.gitattributes`: `* -text`).

| role | path | bytes | lines | sha256 |
| --- | --- | --- | --- | --- |
| script (the file you run) | `Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` | 41911 | 445 | `e95be20d658a84bd6db189a16f452e8062329784b83e0217e3818fca81244e1b` |
| package (loaded by the script with `Get`, script line 25) | `Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` | 14903 | 220 | `f0292638c8d6dab9b7a05c744ba00a2ebe329e96ef927478cb73c7599e749c11` |
| input 1 (read by the package with `Import[..., "RawJSON"]`, package line 159) | `Revision/algebra/gammas.json` | 76968 | 1405 | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` |
| input 2 (read by the script with `Import[..., "RawJSON"]`, script line 89) | `Revision/gkd_lovelock/results/lovelock-tensors.json` | 55056 | 405 | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` |
| output 1 (written, committed) | `Revision/field_equations_a4/a4-equations.json` | 41869 | 788 | `9965d8c0a8d7d77c5a239d5c7d0576326ffd6143b09e68d4ffd8e467a456afd1` |
| output 2 (written, committed) | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 14190 | 269 | `27faceeebdcdb8dc97afbebe89e24e322e8308fb5679df19c88dc1c77af72e6b` |

Last commits that changed them: the package and output 2: `e377368` (2026-10-08); the script: `16d538f`
and output 1: `7daacf6` (automatic snapshots of 2026-10-08, section 6.7; the changes of section 6.6 were first
committed in `6779cd3`; before them the script was last changed by `e377368` and output 1 by `70fab64`, which
the patch left byte for byte unchanged); `gammas.json`: `9ea68d4` (2026-10-01); `lovelock-tensors.json`:
`ad02ebb` (2026-10-01). On 2026-10-08, after `e377368`, the script and output 1 were changed (section 6.6): the folders are normalised with `ExpandFileName`,
and the text `fields.dirac16complex.statement` of output 1 now reports what `Revision/theory/fock_quartic`
decided; later that day the opening of the text `fields.dirac16complex.kohnSham` was corrected (section
6.7). The table gives the version of section 6.7; the versions verified in sections 6.3 to 6.5 were the
script `d9db27d371eefbd6afc0f358fe9b150a21b82c8a58e5ce2741d71f652f9d1ce9` (40749 bytes) and output 1
`98d3245d30e5c25f7bbdfcd186d5723aec2059a1feeaef4cc3c3249684de03b4` (40843 bytes), and those of section 6.6
the script `340933007f94571fe9db57562a48d7309053381c56a6c1c4e44af1875eeb2a4c` (41876 bytes) and output 1
`b2f470d04a1d660430e5008e7aed1e8af91d5287fd2546a0cbeb82f983573d96` (41834 bytes).

The set reads nothing else: no other file, no environment variable, no command-line argument, no
network resource. The script finds its package and its second input relative to its own location
(`$InputFileName`), and the package finds `gammas.json` relative to its own location, so the set
does not depend on the folder you start it from. The package also computes the sha256 of
`gammas.json` (`FileHash`, package line 169) and writes it into the detail of the check
`fixture_author_T16_read`. Both inputs are produced by other sets (`gammas.json` by
`Revision/algebra/wolfram/verify_algebra.wls`, `lovelock-tensors.json` by the Rust program in
`Revision/gkd_lovelock/code`); they are committed, so you need neither to run this set. The two
outputs are deterministic: LF line endings, no time stamps, no machine names, fixed key order. The
script and the package contain no random numbers, no dates, no parallel computation and no network
functions; the script writes only through its function `writeJSON` (one `OpenWrite`, script line
41), which it calls twice (line 437 for `a4-equations.json`, then line 442 for the report).

The optional supplementary Dirac-matrix check of section 6.3 (not part of the set, not committed)
reads the same package and `gammas.json` and writes nothing.

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, with about 2 GB of free disk space for the
  repository (on 2026-10-08 the clone downloaded about 340 MB and then occupied about 956 MB, its
  hidden `.git` folder of 340 MB included; the repository grows over time), several GB of free
  disk space for Wolfram itself (the Wolfram 15.0.1 installation on the verification machine
  occupies about 9.3 GB) and about 0.3 GB of free memory for the Wolfram kernel.
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
   with your own e-mail address). Read the licence terms on that page; accepting them is your own
   decision.
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
`wolframscript` is not found, use that full path in place of `wolframscript` in every command
below (in PowerShell put `& ` in front of a quoted full path, for example
`& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -version`).

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
in PowerShell (it prints the time, then `$LASTEXITCODE` gives the exit code), or put `time ` in
front of the `wolframscript` command in bash/zsh.

The run prints nothing for about half a minute to one and a half minutes, or longer on a slow or
busy computer (it is computing; the time depends strongly on how busy the computer is, section 4),
and then prints one line; section 4 says exactly what to expect.

### 3.6 If it fails, or if you want to stop a run

* `wolframscript : The term 'wolframscript' is not recognized ...` (PowerShell) or
  `wolframscript: command not found` (macOS/Linux): Wolfram is not installed, or the terminal was
  opened before the installation. Open a new terminal; if that does not help, use the full path
  of `wolframscript` (option B in 3.2) or install WolframScript on its own (3.2, step 2).
* A request for a Wolfram ID and password, or a message that the engine is not activated or that
  the kernel could not be launched: activate it once with `wolframscript -activate` (needs
  internet).
* A single line beginning with `ERROR  ` (ERROR and two spaces), followed by nothing else, and exit
  code `1`. The run stopped on purpose and wrote no file, except in the last of these cases. In
  every line `<root>` stands for the full path of your repository folder; the lines are shown as
  printed on Windows by the script of section 2, which normalises its folders (section 6.6; the
  report line was observed with it in section 6.7, test 4; the versions before it printed
  `<root>\Revision\field_equations_a4\wolfram\..\` in the two `cannot write` lines, tests E and G
  of section 6.3); on macOS and Linux the separators are `/` (expected, not verified there):
  * `ERROR  <root>\Revision\algebra\gammas.json: input file not found`: the author's matrices are
    missing (usually only part of the repository was copied). Clone the whole repository (3.4), or
    restore the file with `git checkout -- Revision/algebra/gammas.json`.
  * `ERROR  <root>\Revision\algebra\gammas.json: not a JSON object (Import[..., "RawJSON"] failed)`,
    `...: missing keys ...`, `...: <name> is not a list of ...`, or
    `...: gamma[0][0][0] = 0.5 is not an exact rational in the fixture encoding (a JSON integer, or a string "p/q" in lowest terms with q > 1)`
    (the place and the value vary): `gammas.json` was changed or damaged. Restore it with
    `git checkout -- Revision/algebra/gammas.json`.
  * `ERROR  <root>\Revision\field_equations_a4\wolfram\FieldEquationsA4.wl: package not found`
    (or `...: Get failed`): the package is missing. Restore it with
    `git checkout -- Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` or clone again.
  * `ERROR  cannot write <root>\Revision\field_equations_a4\a4-equations.json`: the
    first output could not be opened for writing (write-protected, or open in a program that locks
    it); nothing was written. Make the file writable, close such programs and run again.
  * `ERROR  cannot write <root>\Revision\field_equations_a4\reports\wolfram-a4-report.json`:
    the folder `reports` is missing, or the report is write-protected or locked. In this case the
    run HAS already rewritten `a4-equations.json` (with the same bytes as before if everything else
    is in order) and then stopped without a `checks:` line. The folder `reports` also holds the
    Python outputs of this directory; restore it with
    `git checkout -- Revision/field_equations_a4/reports` and run again.
* `Import::nffil: File ...lovelock-tensors.json not found during Import.`, followed by
  `Part::partd`, `Part::partw` and `General::stop` messages (all on standard output), the line
  `checks: 52, failed: 6` with six lines
  `FAIL P1_direct_equals_gkd_branch_monomials ...` to `FAIL L3_direct_equals_gkd_branch ...`, and
  exit code 1: the second input is missing (this input is not read strictly; the six comparisons
  with the Rust results fail instead). Clone the whole repository (3.4). This failed run has
  overwritten the committed report with a FAIL report (`a4-equations.json` keeps its bytes);
  restore with
  `git checkout -- Revision/field_equations_a4/reports/wolfram-a4-report.json Revision/gkd_lovelock/results/lovelock-tensors.json`.
* Any line beginning with `FAIL ` and a nonzero exit code although every file is present: a check
  did not pass. Write down the printed name, restore the outputs (section 5) and report it; do not
  edit the script. This did not happen in any verification run.
* The run takes much longer than one and a half minutes: a slow or busy computer (the measured
  kernel CPU time of the runs that computed everything was 35 s to 46 s on 2026-10-08; see
  section 4). Wait; the computation needs no input from you.
* To stop a run that you do not want to wait for, end the Wolfram KERNEL, not `wolframscript`:
  * Windows: in the Task Manager (Details tab) end the `wolfram.exe` process that uses CPU time
    (each run has one; a second `wolfram.exe` of the run, a licence query, ends within a second
    after the start). `wolframscript` then prints `The product exited for an unknown reason.` on
    the error stream and ends with exit code `-1` (`$LASTEXITCODE` shows `-1`). This message only
    reports that you ended the kernel. Neither output is changed (both are written only at the
    very end of a run), and WolframScript removes its two temporary files (section 5).
  * macOS or Linux: `ps aux | grep -i wolfram` lists `wolframscript`, the kernel (`WolframKernel`
    or `wolfram`) and the `grep` command itself. End the `WolframKernel` (or `wolfram`) process
    with the high `%CPU` value, not `wolframscript`, with `kill <process number>`; if a kernel is
    still running after `wolframscript` has ended, end it too. (Measured on Windows only.)
  * If you end `wolframscript` itself instead (for example with End task in the Task Manager), the
    kernel ended together with it in the test of section 6.3 (no kernel was left running), the
    outputs are unchanged, but WolframScript's two temporary files stay behind (section 5). Pressing
    Ctrl+C in the terminal was not tested; afterwards check as above that no kernel is left running.
* All 52 checks pass but `git status` shows `a4-equations.json` or `wolfram-a4-report.json` (or
  both) as modified: you are probably using a Wolfram version other than 15.0.1, whose TeX or
  InputForm formatting differs. Both files contain expressions formatted by Wolfram:
  `a4-equations.json` in InputForm and TeX, and the explanations in `wolfram-a4-report.json` in
  InputForm (for example `"detail": "L_(1) = 12*ad1^2 - 84*H^2"`). The mathematics (the 52 checks)
  is what matters; only Wolfram 15.0.1 was verified to reproduce the committed bytes. Restore both
  committed files with
  `git checkout -- Revision/field_equations_a4/a4-equations.json Revision/field_equations_a4/reports/wolfram-a4-report.json`.

## 4. Expected output

Printed on the screen (standard output), exactly one line:

```text
checks: 52, failed: 0
```

Nothing is printed on the error stream, no `FAIL` or `ERROR` line appears, and the exit code is `0`
(`$LASTEXITCODE` in PowerShell, `echo $?` in bash/zsh). If a check failed, the line would read
`checks: 52, failed: <n>`, each failed check would be listed on a line
`FAIL <name>: <explanation>`, and the exit code would be `1`.

Files written (both are overwritten on every run that reaches its end):

1. `Revision/field_equations_a4/a4-equations.json` (41869 bytes, 788 lines). Its top-level keys
   are `title`, `producer`, `conventions`, `lovelockTensors`, `generalSource`, `einstein`,
   `linearMember`, `fields`, `checksSummary`; its second line is
   `  "title": "Einstein-Lovelock field equations for a4[x4] in the primordial metric (Revision/SPEC.md section 5)",`.
   For example `generalSource.evolution_F.input` is
   `2*alpha1 - 48*ad1^2*alpha2 + 720*ad1^4*alpha3 - 80*alpha2*H^2 + 864*ad1^2*alpha3*H^2 + 720*alpha3*H^4`
   (ad1 = a4').
2. `Revision/field_equations_a4/reports/wolfram-a4-report.json` (14190 bytes, 269 lines). Its first
   six lines are:

   ```text
   {
     "producer": "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls",
     "spec": "Revision/SPEC.md section 5",
     "checkCount": 52,
     "failedCount": 0,
     "verdict": "PASS",
   ```

   Show them with `Get-Content Revision/field_equations_a4/reports/wolfram-a4-report.json -TotalCount 6`
   (PowerShell) or `head -n 6 Revision/field_equations_a4/reports/wolfram-a4-report.json`
   (macOS/Linux). If Python is installed, this prints `52 0 PASS`:
   `python -c "import json; r=json.load(open('Revision/field_equations_a4/reports/wolfram-a4-report.json')); print(r['checkCount'], r['failedCount'], r['verdict'])"`
   (use `python3` on macOS/Linux).

How to check that you reproduced the committed results exactly:

* With git: `git status --porcelain` prints nothing (both outputs are byte-identical to the
  committed files, so git does not see a change).
* With checksums: `Get-FileHash Revision/field_equations_a4/a4-equations.json, Revision/field_equations_a4/reports/wolfram-a4-report.json -Algorithm SHA256`
  (PowerShell; it prints the hash in capital letters, compare ignoring case),
  `shasum -a 256 <file>` (macOS) or `sha256sum <file>` (Linux), and compare with the sha256 of
  the two output rows in section 2.

The 52 checks, in the order of the report (all PASS):

| section | checks |
| --- | --- |
| geometry (4) | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4`, `riemann_pair_antisymmetry` |
| Lovelock tensors (17) | `P1_direct_equals_minus_4_Einstein`; for k = 1, 2, 3: `Pk_direct_equals_gkd_branch_monomials`, `Lk_direct_equals_gkd_branch`, `Pk_trace_identity`, `Pk_structure`; `P4_vanishes_pigeonhole`, `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| field equations, general source (7) | `independent_components`, `evolution_factorises_a4pp_times_F`, `evolution_F_not_identically_zero`, `algebraic_identity_x1_plus_x5_minus_2x8`, `x8_component_contains_no_a4pp`, `constraint_propagation_bianchi`, `conservation_components` |
| Einstein case (3) | `einstein_components`, `einstein_null_energy_x8`, `einstein_no_vacuum_solution` |
| linear member (3) | `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `einstein_gauss_bonnet_vacuum_linear` |
| spinor sources (18) | the author's T16: `fixture_author_T16_read`, `clifford_relations_author_T16`, `C_properties_author_T16`; comparison representation: `clifford_relations_own_rep`, `C_properties_own_rep`, `representations_equivalent_author_T16_own_rep`; in T16: `spin_connection_antisymmetric`, `Omega_x4_Omega_x8_vanish`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `gravity_term_gamma_mu_Omega_mu`, `condensate_equation_x8_consistent`, `condensate_S_constant`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears`, `offdiagonal_coefficients_representation_independent`, `condensate_einstein_quadratic_U`, `condensate_diagonal_witness_exact` |

Run time and memory, measured on 2026-10-08 on the verification machine (Intel Core Ultra 9
275HX, 24 cores, 191 GB memory, Windows 11 Pro for Workstations), section 6.3: wall clock 36.3 s
to 85.8 s for the five successful runs; kernel CPU time 34.8 s and 43.7 s in the two monitored
successful runs (43.1 s to 46.0 s in the failure tests D, E and G, which also compute everything).
The wall time depends strongly on the load of the machine (it was shared with other jobs; CPU load
between 8 % and 100 % during the runs). A slower or busier computer may need a few minutes. Peak
memory (working set): 272.3 MB to 272.8 MB for the Wolfram kernel and 16.7 MB to 16.8 MB for
`wolframscript` (monitored runs and failure tests that computed everything). (The
version before the patch needed about 20 to 23 s of kernel CPU time and 226 to 227 MB; the patched
set also builds the intertwiner and runs the condensate pipeline a second time in the comparison
representation.)

## 5. Side effects

* Files in the repository OVERWRITTEN on every run that reaches its end (also when a check
  fails, see below): `Revision/field_equations_a4/a4-equations.json` and
  `Revision/field_equations_a4/reports/wolfram-a4-report.json`. On a successful run with Wolfram
  15.0.1 the new bytes are identical to the committed ones, so only the files' modification times
  change and `git status --porcelain` stays empty.
* A failed run (a `FAIL` line) overwrites the committed report with a report whose verdict is
  `FAIL` (and, if the equations came out differently, also `a4-equations.json`);
  `git status --porcelain` then shows ` M Revision/field_equations_a4/reports/wolfram-a4-report.json`.
* A run that stops with an `ERROR  ` line writes no file, except when the report cannot be written:
  then `a4-equations.json` has been written just before (section 3.6). A run whose kernel or
  `wolframscript` is ended before the end writes no file.
* No other file in the repository is created, changed or deleted (checked with
  `git status --porcelain --ignored -uall`, which listed nothing after each checked run). The
  script creates no folders and no temporary files of its own.
* Outside the repository, WolframScript itself (not this script) uses its per-user folders. On
  Windows, measured on 2026-10-08:
  * Every run creates two files `tmp_<10 random letters and digits>` in
    `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary`: one stays empty (0 bytes), the
    other collects what the run prints (in run 2 of section 6.3 it held exactly the 23 bytes
    `checks: 52, failed: 0` plus CR LF; in the failure test with `lovelock-tensors.json` missing,
    the 2372 bytes printed by that run). `wolframscript` deletes both when it ends by itself, also
    after an `ERROR  ` line, a `FAIL` line, or when you end the kernel (section 3.6).
  * If `wolframscript` itself is ended before it finishes (End task in the Task Manager, or a
    killed process), the two files stay behind (both 0 bytes in the test of section 6.3, because
    the run had not printed anything yet). They are harmless and are never read again by this set;
    you may delete `tmp_*` files there when no `wolframscript` is running. Several such left-over
    pairs of other jobs were present on the verification machine.
  * `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` (238 bytes) is rewritten at the start of
    a run (its modification time was the start time of test G of section 6.3), and the folder
    `%APPDATA%\Wolfram\Paclets\Temporary` was modified at the same moment; earlier verifications
    also saw `%APPDATA%\Wolfram\ApplicationData\ProcessLink\Streams\wl-stream-*` written. Other
    Wolfram jobs ran on the same machine, so the last two could not be attributed to this run
    alone.
  * macOS and Linux use the corresponding per-user Wolfram folders (not verified there).
* Processes: `wolframscript` starts two Wolfram processes one after the other (measured on
  2026-10-08 by listing the child processes of `wolframscript` every 0.2 s): first a short licence
  query (`wolfram.exe -wlbanner -licenseinfo`, 0.05 s to 0.12 s of CPU time, it ends at once),
  then the kernel that runs the script (`wolfram.exe -runfirst ... -linkmode Connect -linkname
  <name>_shm -mathlink`, connected to `wolframscript` through shared memory; on macOS and Linux the
  process name contains `wolfram` or `Wolfram`, for example `WolframKernel`). There are no parallel
  subkernels. The kernel quits at the end of the run (the script ends with `Exit[0]` or `Exit[1]`);
  no kernel was left running after any verification run, also not after `wolframscript` was ended.
* Network: none needed. The script and the package contain no network functions. During test G of
  section 6.3 (54 samples of the TCP connections and UDP endpoints of `wolframscript` and its two
  child processes) none was seen at all; earlier verifications (2026-10-02, 2026-10-07) saw only
  local loopback connections (127.0.0.1) between `wolframscript` and its kernel, or none. The
  Wolfram licence on the verification machine is node-locked (`$NetworkLicense` is `False`), so no
  licence server was contacted.
* To restore the committed state after any run:

  ```text
  git checkout -- Revision/field_equations_a4/a4-equations.json Revision/field_equations_a4/reports/wolfram-a4-report.json
  git status --porcelain
  ```

  The second command must print nothing.

## 6. Verification record

The set was verified on 2026-10-02 (6.1) and on 2026-10-07 (6.2) in the version BEFORE the patch
of commit `e377368`, and on 2026-10-08 (6.3) in the version of that commit. 6.4 lists the findings of the
independent verifier of 2026-10-07 and what was done with each; 6.5 the open remarks; 6.6 the change of
2026-10-08 after that commit (folders normalised, one text of output 1 updated) and its runs; 6.7 a second
text change of output 1 on the same day (the opening of `fields.dirac16complex.kohnSham`) and its runs.

### 6.1 Verification of 2026-10-02 (version before the patch)

Commits `45d4734` and `c2b33cc`, two fresh clones, Windows 11 Pro for Workstations 10.0.26200,
Wolfram 15.0.1, WolframScript 1.14.0. That version had 47 checks (it computed the spinor
statements with its own Kronecker-product matrices only) and its files had other sha256 (script
`9cd8d9a1...2965`, 34686 bytes; package `4ac40fef...c8f8`, 8555 bytes; report `2c070eda...857c`,
11814 bytes; `a4-equations.json` as now). Eight runs, each with exit code 0 and
`checks: 47, failed: 0`; in the seven runs whose outputs were compared, both outputs were
byte-identical to the committed files; wall times 18.9 s to 31.2 s, 20.1 s of kernel CPU time (one
measurement), kernel peak memory 226.2 MB to 227.0 MB. Failure tests: with `lovelock-tensors.json` missing,
`checks: 47, failed: 6` and exit code 1; with the `reports` folder missing, exit code 0 although
the report was not written; with the package missing, the run did not finish (stopped after 10
minutes by ending the kernel). The last two behaviours were changed by the patch (section 3.6).

### 6.2 Re-verification of 2026-10-07 (version before the patch)

Commits `a4c5eda` and `cb6e78f`, three fresh clones, Windows 11 10.0.26300, the same files as in
6.1. Six runs: exit code 0, `checks: 47, failed: 0`, both outputs byte-identical, wall times 27.4 s
to 33.7 s, 21.8 s to 23.1 s of kernel CPU time, kernel peak memory 226.5 MB to 227.0 MB; the three
failure tests of 6.1 repeated with the same behaviour. A supplementary exact check (10 of 10 PASS)
showed that the matrices of that version were the author's matrices in another basis (an integer
intertwiner S with S^T S = 128 I16). The independent verifier of that day measured wall times of
35.8 s to 64.0 s on the loaded machine (findings in 6.4).

### 6.3 Verification of 2026-10-08 (the version of commit `e377368`)

| item | value |
| --- | --- |
| date | 2026-10-08 |
| commit verified | `477fa9bb12780395ce41db73cfdab294693c52c3` (the remote `main` at the time; it contains the patch `e377368`, and the six files of section 2 had the sha256 that section 2 gave at that time; at that commit the script had sha256 `d9db27d371eefbd6afc0f358fe9b150a21b82c8a58e5ce2741d71f652f9d1ce9` (40749 bytes) and `a4-equations.json` `98d3245d30e5c25f7bbdfcd186d5723aec2059a1feeaef4cc3c3249684de03b4` (40843 bytes); section 2 now gives the versions of sections 6.6 and 6.7, the package, the two inputs and output 2 are unchanged) |
| clones | two fresh `git clone https://github.com/once-ere/Dirac_claude.git` in a scratch folder: clone 1 for the measurements and the failure tests, clone 2 (in a folder whose path contains a space) for following this file literally; no uncommitted file was copied in (none is needed by this set) |
| clone size | clone 1: 955,990,168 bytes (`du -sb`), `.git` 340,131,897 bytes, pack 323.89 MiB (`git count-objects -vH`) |
| operating system | Windows 11 Pro for Workstations 10.0.26300, Intel Core Ultra 9 275HX (24 cores), 191 GB memory |
| Wolfram | Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), WolframScript 1.14.0, kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe` |
| shells | PowerShell 7.6.6 and Git Bash (git 2.51.2.windows.1) |
| monitoring | in clone 1 every run was started with `Start-Process wolframscript -ArgumentList '-file', ...` (standard output and error redirected to files), and the child processes (working set, CPU time), the folder `WolframScriptTemporary`, the CPU load and the other Wolfram processes of the machine were sampled every 0.2 s |

Runs that must succeed:

| run | where, how | exit code | printed line | wall time | kernel CPU | peak memory (kernel / wolframscript) | outputs vs committed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | clone 1, from the root, monitored | 0 | `checks: 52, failed: 0` | 36.3 s (CPU load 8-40 %) | 34.8 s | 272.3 MB / 16.7 MB | both byte-identical |
| 2 | clone 1, from the folder `Revision/field_equations_a4/wolfram` with `wolframscript -file verify_field_equations_a4.wls`, monitored | 0 | `checks: 52, failed: 0` | 72.8 s (CPU load 85-100 %, from other jobs) | 43.7 s | 272.5 MB / 16.8 MB | both byte-identical |
| 3 | clone 2, the PowerShell commands of 3.5, literally | 0 | `checks: 52, failed: 0` | 85.8 s (CPU load 100 %, from other jobs) | not measured | not measured | both byte-identical |
| 4 | clone 2, the `Measure-Command` form of 3.5 | 0 | `checks: 52, failed: 0` | 72.8 s (as printed by `Measure-Command`) | not measured | not measured | both byte-identical |
| 5 | clone 2, the macOS/Linux commands of 3.5 in Git Bash, with `time` | 0 | `checks: 52, failed: 0` | 64.8 s (`real 1m4.762s`) | not measured | not measured | both byte-identical |

In runs 1 and 2 the standard output was the 23 bytes `checks: 52, failed: 0` plus CR LF and the
error stream was empty. The modification times show that both files were rewritten (checked after
runs 1, 2 and 3). `git status --porcelain` was empty after every run, and
`git status --porcelain --ignored -uall` after runs 1, 2 and 4 and after the restore that followed
run 5 (`cmp` had found both outputs of run 5 identical before). In run 2 no other Wolfram process
was running, so its two temporary files are certainly its own: `tmp_McbZ83OPNO` (0 bytes) and
`tmp_c4VUZkRVMo` (the 23 printed bytes); both were gone when `wolframscript` had ended.

Failure tests in clone 1 (each restored afterwards with `git checkout -- <path>`;
`git status --porcelain --ignored -uall` then empty; "outputs untouched" means the modification
times of both outputs did not change):

| test | change | exit code | wall time | printed (standard output; the error stream was empty unless stated) | files |
| --- | --- | --- | --- | --- | --- |
| A | `Revision/algebra/gammas.json` deleted | 1 | 6.4 s | `ERROR  <root>\Revision\algebra\gammas.json: input file not found` (199 bytes) | outputs untouched |
| B1 | one entry of `gammas.json` set to the float 0.5 | 1 | 7.5 s | `ERROR  <root>\Revision\algebra\gammas.json: gamma[0][0][0] = 0.5 is not an exact rational in the fixture encoding (a JSON integer, or a string "p/q" in lowest terms with q > 1)` | outputs untouched |
| B2 | `gammas.json` cut after 1000 bytes | 1 | 6.6 s | `ERROR  <root>\Revision\algebra\gammas.json: not a JSON object (Import[..., "RawJSON"] failed)` | outputs untouched |
| C | `FieldEquationsA4.wl` deleted | 1 | 3.6 s | `ERROR  <root>\Revision\field_equations_a4\wolfram\FieldEquationsA4.wl: package not found` (223 bytes) | outputs untouched |
| D | `lovelock-tensors.json` deleted | 1 | 54.4 s | `Import::nffil`, `Part::partd` (3), `Part::partw` (3), `General::stop` (2), `checks: 52, failed: 6` and the six `FAIL` lines of the comparisons with the Rust results (2372 bytes) | report overwritten (`52 6 FAIL`), `a4-equations.json` byte-identical |
| E | folder `Revision/field_equations_a4/reports` deleted | 1 | 44.4 s | `ERROR  cannot write <root>\Revision\field_equations_a4\wolfram\..\reports\wolfram-a4-report.json` (231 bytes; observed with the version before section 6.6, the current script prints the normalised path, section 3.6) | `a4-equations.json` rewritten, byte-identical |
| G | `a4-equations.json` made read-only | 1 | 48.6 s | `ERROR  cannot write <root>\Revision\field_equations_a4\wolfram\..\a4-equations.json` (218 bytes; observed with the version before section 6.6, the current script prints the normalised path, section 3.6) | outputs untouched (the report was not written either) |
| F1 | the kernel ended after 16.2 s (`Stop-Process` on the `wolfram.exe ... -mathlink` child) | -1 | 16.4 s | nothing; error stream: the 42 bytes `The product exited for an unknown reason.` plus LF | outputs untouched; both temporary files (`tmp_PBUgRdv4Zi`, `tmp_L4ysA0ZC8v`, 0 bytes) removed; no other Wolfram process was running |
| F2 | `wolframscript` ended after 15.3 s (`Stop-Process -Force`) | -1 | 15.5 s | nothing; error stream empty | outputs untouched; the kernel had ended 0.5 s later; both temporary files (`tmp_LqAexjlVjd`, `tmp_ej8pDdD6nX`, 0 bytes) left in `WolframScriptTemporary` (deleted by the verifier afterwards); no other Wolfram process was running |

In tests A, B1, B2 and C the line was printed within seconds, before any computation. In test D
the printed text (2372 bytes) was also found, while the run lasted, in one of WolframScript's two
temporary files. In test G no TCP connection or UDP endpoint of `wolframscript` or its children
was seen (54 samples).

Supplementary Dirac-matrix check (not part of the set). The script below (51 lines, 4680 bytes,
sha256 `c6fc3a6bf6c7b806116269ec142f374642e6f8d309ff102c1fad9f957e56f781`, LF) uses the package's
`FEGammaFrame` and `FEC` (the primary matrices) and `FEGammaFrameComparison` and `FECComparison`
(the comparison representation), reads `gammas.json` with a plain `Import` (independently of the
package's strict reader), and builds the intertwiner as a group average over the 256 ordered
products of the gammas (the set itself uses `NullSpace`). It was run from the root of clone 1 with
`wolframscript -file <path>/dirac_crosscheck.wls`: exit code 0, 12.8 s, nothing written
(`git status --porcelain --ignored -uall` empty). To run it yourself, save the text between the
fences as `dirac_crosscheck.wls` outside the repository (for example in your home folder) and run
that command from the repository root.

```text
#!/usr/bin/env wolframscript
(* dirac_crosscheck.wls - optional supplementary check printed in section 6.3 of
   Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md; not part of the set.
   Usage: save this file outside the repository, then, from the repository root:
     wolframscript -file <path to>/dirac_crosscheck.wls
   (1) The set's primary matrices FEGammaFrame and FEC (FieldEquationsA4.wl) are, entry by entry, the author's
   eight real 16 x 16 matrices T16 and C as stored in Revision/algebra/gammas.json (read here with a plain Import,
   independently of the package's strict reader). (2) The comparison representation FEGammaFrameComparison,
   FECComparison is equivalent to them, by an intertwiner built here as a group average (a second route; the set
   itself uses NullSpace). Exact integers only. Writes nothing; exit code 0 iff every check passes. *)
root = Directory[];
Get[FileNameJoin[{root, "Revision", "field_equations_a4", "wolfram", "FieldEquationsA4.wl"}]];
js = Import[FileNameJoin[{root, "Revision", "algebra", "gammas.json"}], "RawJSON"];
gA = js["gamma"]; CA = js["C"]; etaA = js["eta"];
gT = FEGammaFrame; gR = FEGammaFrameComparison; CR = FECComparison; id = IdentityMatrix[16];
res = {};
chk[name_, ok_, det_] := (AppendTo[res, {name, TrueQ[ok]}]; Print[If[TrueQ[ok], "PASS ", "FAIL "], name, ": ", det]);

chk["author_T16_from_json", Length[gA] == 8 && Union[Flatten[gA]] === {-1, 0, 1} && Dimensions[CA] == {16, 16} &&
   And @@ Flatten[Table[gA[[a]] . gA[[b]] + gA[[b]] . gA[[a]] == 2 etaA[[a]] KroneckerDelta[a, b] id, {a, 8}, {b, 8}]],
   "gammas.json (plain Import): 8 integer 16 x 16 matrices, entries in {-1, 0, 1}, {G_a, G_b} = 2 eta_ab I16, eta = " <> ToString[etaA]];
chk["primary_is_author_T16", Count[Table[gT[[a]] === gA[[a]], {a, 8}], True] == 8 && FEC === CA,
   "FEGammaFrame[[a]] = gammas.json gamma[a-1] for all 8 a (" <> ToString[Count[Table[gT[[a]] === gA[[a]], {a, 8}], True]] <> " of 8 equal entry by entry) and FEC = gammas.json C"];
chk["same_signature_and_order", Diagonal[FEEta] === etaA, "eta of FieldEquationsA4.wl = eta of gammas.json = " <> ToString[etaA] <> " (x1..x8)"];
chk["comparison_rep_clifford", Length[gR] == 8 && Union[Flatten[gR]] === {-1, 0, 1} &&
   And @@ Flatten[Table[gR[[a]] . gR[[b]] + gR[[b]] . gR[[a]] == 2 FEEta[[a, b]] id, {a, 8}, {b, 8}]],
   "FEGammaFrameComparison: 8 integer 16 x 16 matrices with {g_a, g_b} = 2 eta_ab I16"];
Print["INFO comparison matrices equal to the author's entry by entry: ", Count[Table[gR[[a]] === gA[[a]], {a, 8}], True], " of 8"];
chk["transpose_pattern_both", And @@ Table[Transpose[gR[[a]]] === etaA[[a]] gR[[a]] && Transpose[gA[[a]]] === etaA[[a]] gA[[a]], {a, 8}],
   "g_a^T = eta_aa g_a for both sets (so every matrix is orthogonal)"];

(* intertwiner S = sum_s G_s X g_s^T over the 256 ordered products (g_s orthogonal, so g_s^-1 = g_s^T) *)
subsets = Subsets[Range[8]];
prod[m_, s_] := If[s === {}, id, Dot @@ (m[[#]] & /@ s)];
mk[X_] := Sum[prod[gA, s] . X . Transpose[prod[gR, s]], {s, subsets}];
S = Null; Do[With[{X = Normal[SparseArray[{{i, j} -> 1}, {16, 16}]]}, Module[{t = mk[X]}, If[t =!= ConstantArray[0, {16, 16}], S = t; Print["INFO seed X = E_", i, ",", j]; Break[]]]], {i, 16}, {j, 16}];
Print["INFO S entries: ", Union[Flatten[S]]];
chk["intertwiner_invertible", S =!= Null && Det[S] =!= 0, "det S = " <> ToString[Det[S]]];
chk["intertwiner_maps_all_eight", And @@ Table[S . gR[[a]] === gA[[a]] . S, {a, 8}], "S g_a = G_a S for a = x1..x8, i.e. G_a = S g_a S^-1"];
lam = (Transpose[S] . S)[[1, 1]];
chk["intertwiner_orthogonal_up_to_scale", Transpose[S] . S === lam id, "S^T S = " <> ToString[lam] <> " I16 (so S/Sqrt[" <> ToString[lam] <> "] is orthogonal)"];
chk["C_maps_to_author_C", S . CR . Inverse[S] === CA && Transpose[S] . CA . S === lam CR,
   "S C_R S^-1 = C_author (gammas.json C = sigma16) and S^T C_author S = lam C_R: the bilinear form Phibar Psi = Phi^T C Psi is carried to the author's"];
signedPermQ[m_] := And @@ (Count[#, 0] == 15 &) /@ m && And @@ (Count[#, 0] == 15 &) /@ Transpose[m];
chk["signed_permutations_both", And @@ (signedPermQ /@ Join[gR, gA]), "each g_a and each G_a has exactly one nonzero entry (+1 or -1) in every row and every column"];
compact[m_] := "[" <> StringRiffle[Table[With[{j = First[FirstPosition[m[[i]], x_ /; x != 0]]}, If[m[[i, j]] > 0, "+", "-"] <> ToString[j]], {i, 16}], ", "] <> "]";
coord = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
Do[Print["ROW T16 gamma^", coord[[a]], " = ", compact[gT[[a]]]], {a, 8}];
Print["ROW T16 C = ", compact[FEC]];
Print["checks: ", Length[res], ", failed: ", Count[res, {_, False}]];
Exit[If[Count[res, {_, False}] == 0, 0, 1]];
```

Its output (23 lines; sha256 of the output with LF line endings
`c34f75414d29b5f6b1e49919a1c5d90dd38e3f32fb44b247abdfe3297a17b13f`, 2106 bytes):

```text
PASS author_T16_from_json: gammas.json (plain Import): 8 integer 16 x 16 matrices, entries in {-1, 0, 1}, {G_a, G_b} = 2 eta_ab I16, eta = {1, 1, 1, -1, -1, -1, -1, 1}
PASS primary_is_author_T16: FEGammaFrame[[a]] = gammas.json gamma[a-1] for all 8 a (8 of 8 equal entry by entry) and FEC = gammas.json C
PASS same_signature_and_order: eta of FieldEquationsA4.wl = eta of gammas.json = {1, 1, 1, -1, -1, -1, -1, 1} (x1..x8)
PASS comparison_rep_clifford: FEGammaFrameComparison: 8 integer 16 x 16 matrices with {g_a, g_b} = 2 eta_ab I16
INFO comparison matrices equal to the author's entry by entry: 0 of 8
PASS transpose_pattern_both: g_a^T = eta_aa g_a for both sets (so every matrix is orthogonal)
INFO seed X = E_1,1
INFO S entries: {-8, 0, 8}
PASS intertwiner_invertible: det S = 72057594037927936
PASS intertwiner_maps_all_eight: S g_a = G_a S for a = x1..x8, i.e. G_a = S g_a S^-1
PASS intertwiner_orthogonal_up_to_scale: S^T S = 128 I16 (so S/Sqrt[128] is orthogonal)
PASS C_maps_to_author_C: S C_R S^-1 = C_author (gammas.json C = sigma16) and S^T C_author S = lam C_R: the bilinear form Phibar Psi = Phi^T C Psi is carried to the author's
PASS signed_permutations_both: each g_a and each G_a has exactly one nonzero entry (+1 or -1) in every row and every column
ROW T16 gamma^x1 = [-16, -15, +14, +13, -12, -11, +10, +9, +8, +7, -6, -5, +4, +3, -2, -1]
ROW T16 gamma^x2 = [+15, -16, -13, +14, +11, -12, -9, +10, -7, +8, +5, -6, -3, +4, +1, -2]
ROW T16 gamma^x3 = [-14, +13, -16, +15, -10, +9, -12, +11, +6, -5, +8, -7, +2, -1, +4, -3]
ROW T16 gamma^x4 = [-14, +13, +16, -15, +10, -9, -12, +11, +6, -5, -8, +7, -2, +1, +4, -3]
ROW T16 gamma^x5 = [+15, +16, -13, -14, -11, -12, +9, +10, -7, -8, +5, +6, +3, +4, -1, -2]
ROW T16 gamma^x6 = [+16, -15, +14, -13, -12, +11, -10, +9, -8, +7, -6, +5, +4, -3, +2, -1]
ROW T16 gamma^x7 = [+9, +10, +11, +12, -13, -14, -15, -16, -1, -2, -3, -4, +5, +6, +7, +8]
ROW T16 gamma^x8 = [+9, +10, +11, +12, +13, +14, +15, +16, +1, +2, +3, +4, +5, +6, +7, +8]
ROW T16 C = [-5, -6, -7, -8, -1, -2, -3, -4, +13, +14, +15, +16, +9, +10, +11, +12]
checks: 10, failed: 0
```

How to read the `ROW` lines: every one of the author's matrices has exactly one nonzero entry in
each row (check `signed_permutations_both`), so it is written as the list of its 16 rows, each
entry giving the column of that row's nonzero entry and its sign (for example `gamma^x8`: row 1
has +1 in column 9, ..., row 16 has +1 in column 8). The intertwiner of this group average has
S^T S = 128 I16, the one of the set (`NullSpace`) K^T K = 2 I16: an intertwiner is unique up to a
factor (the space has dimension 1), so the two differ only by that factor.

Following this file literally (clone 2: a fresh `git clone` made exactly as in 3.4, inside a
folder whose path contains a space; commit `477fa9b`):

* The two commands of 3.3 printed `WolframScript 1.14.0 for Microsoft Windows (64-bit)` and
  `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. The repository root contained the
  folders and the file named in 3.4.
* The PowerShell commands of 3.5 (run 3) printed `checks: 52, failed: 0` and then `0`. The checks
  of section 4 then printed the six lines shown there, `52 0 PASS` (the `python` one-liner),
  nothing for `git status --porcelain`, and, with `Get-FileHash`, the two output sha256 that section 2 then gave in
  capital letters. The `Measure-Command` form (run 4) printed the line and the time, and
  `$LASTEXITCODE` then printed `0`.
* The macOS/Linux commands of 3.5, typed in Git Bash with `time` in front (run 5), printed the
  line, the time and `0`; `head -n 6` printed the six lines of section 4; `sha256sum` printed the
  two output sha256 that section 2 then gave; `cmp` against `git show HEAD:<path>` found both outputs identical. The
  `python3` form of section 4 could not be tested (on this Windows machine `python3` is only a
  Microsoft Store alias); the `python` form was tested in run 3.
* The restore commands of section 5 left `git status --porcelain` empty, and
  `git status --porcelain --ignored -uall` listed nothing.
* The supplementary script, cut out of this file between its fences and saved outside the
  repository, was byte-identical to the script run in clone 1 (sha256 above). Run from the root of
  clone 2 it exited with code 0 after 8.3 s, printed nothing on the error stream and wrote nothing,
  and its output (with CR LF turned into LF) was byte-identical to the output printed above.
* All six rows of the table of section 2 as it then was (bytes, lines, sha256, LF line endings only), the second
  line and the top-level keys of `a4-equations.json`, the value of `generalSource.evolution_F.input`
  quoted in section 4, the script and package line numbers cited in sections 1 and 2, and the
  completeness and order of the table of the 52 checks in section 4 were confirmed in clone 2 by a
  short Python script.

Fixes made on 2026-10-08: none to the set (the sha256 of section 2 were then those of the committed
files). This provenance file was rewritten for the patched set (sections 1 to 6).

### 6.4 Findings of the independent verifier of 2026-10-07 and what was done

* Major: the file did not state that the set departed from `Revision/SPEC.md` section 2 (it used
  its own matrices instead of the author's T16). The departure itself was removed by the patch of
  commit `e377368` (the set now reads T16 from `gammas.json`); section 1 ("The Dirac matrices of
  this set") now states the instruction, how the set follows it, and this history.
* Minor: the wall times of 2026-10-07 were called "upper values for this machine", which they were
  not (the verifier measured 35.8 s to 64.0 s under similar load). Sections 3.5, 3.6 and 4 now say
  that the wall time depends strongly on the load and give the measured ranges of 2026-10-08; the
  supplementary check is given with its measured time.
* Minor: the peak-memory range of section 4 did not include the 226.2 MB of the file's own record.
  Section 4 now gives the full measured range of 2026-10-08 (272.3 MB to 272.8 MB) and the range of
  the earlier version (226 to 227 MB).
* Minor: the macOS/Linux instruction for ending a run did not say which process to end. Section
  3.6 now says: end the `WolframKernel` (or `wolfram`) process with the high `%CPU` value, not
  `wolframscript`, and end a kernel that is still running after `wolframscript` has ended.

### 6.5 Open discrepancies and remarks

Open discrepancies in the results: none. The 52 checks pass and both outputs are reproduced byte
for byte. Remarks that do not affect a run from a complete clone:

* (a) The second input, `lovelock-tensors.json`, is not read strictly: when it is missing the run
  does not stop with an `ERROR  ` line but reports six FAIL checks, exits with code 1 and
  overwrites the committed report (test D). The nonzero exit code is correct; only the form differs
  from that of `gammas.json`.
* (b) When the report cannot be written, `a4-equations.json` has already been rewritten (test E).
  With an otherwise complete clone the rewritten bytes are the committed ones.
* (c) The earlier remarks of this file are settled: the run time of
  `Revision/field_equations_a4/README.md` (it now gives 43-70 s for the Wolfram run, measured on
  2026-10-07 "depending on the load"; 6.3 measured 36.3 s to 85.8 s, of the same order); the
  missing error exits (the patch added them,
  section 3.6); and the sentence of `provenance/dirac matrices.md` about this set (that file was
  regenerated with the patch and now states that `FEGammaFrame` equals the author's matrices).

### 6.6 Folders normalised and the `dirac16complex` statement updated (2026-10-08; first committed in the automatic snapshot `6779cd3`)

* Why (folders): a review of the reproducibility of the Revision gate (2026-10-08; it fixed the same pattern
  in `Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls`) found that lines 21 and 22 built
  the folders with `FileNameJoin[{..., ".."}]` without normalising them. The second input is then read as
  `<root>\Revision\field_equations_a4\wolfram\..\..\gkd_lovelock\results\lovelock-tensors.json`, the root
  plus 85 characters, and on Windows a path of 260 or more characters (MAX_PATH) is not found although the
  file exists, so the run failed from a clone folder of 175 characters or more (a computed figure).
* Why (text): `fields.dirac16complex.statement` said that the operator form of the trace identity
  sum_mu <:k_mu:> = <:(m + U'(S)) S:> was "assumed ... (to be confirmed by the theory branch)". The record
  `Revision/theory/fock_quartic` (commit `4f9e55e`; `reports/fock-quartic.json`, 21 of 21 checks PASS) now
  decides it in a finite model only (one good-sector plane-wave mode set with frozen coefficients, flat
  frame, volume 1, 16 modes, 2^16 states): there it is an exact operator identity for the Heisenberg field of
  the interacting operator field equation if the potential and the energy-momentum tensor are both Wick
  ordered, and it fails for every other tested combination; nothing is proved for the field on a whole slice.
  The statement now says this, and still calls the identity for the field on a whole slice ASSUMED.
* Change: lines 21 and 22 now read `$fieldDir = ExpandFileName[FileNameJoin[{$here, ".."}]];` (followed on
  the same line by a comment) and `$revDir = ExpandFileName[FileNameJoin[{$fieldDir, ".."}]];`; the string
  `"statement"` of the `dirac16complex` entry (line 429) was rewritten. No other line changed (still 445
  lines). New sha256 `340933007f94571fe9db57562a48d7309053381c56a6c1c4e44af1875eeb2a4c`, 41876 bytes (before:
  `d9db27d371eefbd6afc0f358fe9b150a21b82c8a58e5ce2741d71f652f9d1ce9`, 40749 bytes). The companion
  `Revision/field_equations_a4/python/check_field_equations_a4.py` received the matching qualification in
  the `dirac16complex` line of its summary `reports/a4-equations-summary.md` (line 39); its checks did not
  change.
* Runs, from the repository root `D:\Developer\github\Dirac_claude` (32 characters) in the working tree on
  top of commit `a8eb09d` or `ab84209` (both committed by others during this work; neither changed a file of
  this set, its inputs or its outputs), not in a fresh clone (other areas of the tree had uncommitted edits of
  other work, none in this folder or in its inputs); Windows 11 Pro for Workstations 10.0.26300, WolframScript
  1.14.0, Wolfram 15.0.1; each Wolfram run started detached from a `cmd.exe` batch file, one at a time:
  1. With only the folders normalised: `wolframscript -file
     Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` printed `checks: 52, failed: 0`,
     exit code 0, wall time 61 s. Both outputs were byte-identical to the committed ones
     (`git diff --quiet` on both succeeded).
  2. With the new statement: the same command, `checks: 52, failed: 0`, exit code 0, wall time 40 s.
     `wolfram-a4-report.json` was byte-identical to the committed one; `a4-equations.json` differed from it
     only in line 776 (`fields.dirac16complex.statement`) and then had sha256
     `b2f470d04a1d660430e5008e7aed1e8af91d5287fd2546a0cbeb82f983573d96`, 41834 bytes (changed again in section 6.7).
  3. The same command again: `checks: 52, failed: 0`, exit code 0, wall time 37 s; `a4-equations.json`
     byte-identical to run 2.
  4. `python Revision/field_equations_a4/python/check_field_equations_a4.py`, twice: `checks: 63, pass 63,
     fail 0, pending 0`, exit code 0, 6 s each; `python-a4-report.json` byte-identical to the committed one,
     `a4-equations-summary.md` identical between the two runs and different from the committed one only
     in line 39.
* Downstream: `Revision/field_equations_a4/ks_source/reports/ks-source-a4.json` records the sha256 of
  `a4-equations.json` among its inputs; `ks_source_a4.py` was re-run twice (23 of 23 PASS, byte-identical
  runs) and then recorded `b2f470d04a1d660430e5008e7aed1e8af91d5287fd2546a0cbeb82f983573d96` (section 6.7 gives the
  value recorded now).
* Fixes made: the normalisation and the text above. Open discrepancies: none in the results. Not done: a run
  of the changed script in a fresh clone, and a run from a long clone folder.

### 6.7 The opening of the `kohnSham` text corrected (2026-10-08; first committed in the automatic snapshots `16d538f` (script), `7daacf6` (`a4-equations.json`) and `7d1ee5a` (`ks-source-a4.json`))

* Why: the independent verifier of section 6.6 (2026-10-08) noted that the text
  `fields.dirac16complex.kohnSham` of output 1 began with "to be filled by Revision/kohn_sham", although the
  same text then reports the evaluated Kohn-Sham states (`reports/ks-source-conditions.json`). The source is
  computed by `Revision/kohn_sham` and its recorded states are evaluated, so nothing is left "to be filled".
* Change: in script line 432 (the string `"kohnSham"` of the `dirac16complex` entry) `to be filled by
  Revision/kohn_sham:` became `Kohn-Sham source (Revision/kohn_sham):`, and `; then constraint:` became
  `; with this source the equations read: constraint:`. The rest of the text and every other line are
  unchanged (still 445 lines). New sha256 `e95be20d658a84bd6db189a16f452e8062329784b83e0217e3818fca81244e1b`,
  41911 bytes (before: `340933007f94571fe9db57562a48d7309053381c56a6c1c4e44af1875eeb2a4c`, 41876 bytes, the
  version of section 6.6). The companion `check_field_equations_a4.py` carries no such text (it reads
  `fields.dirac16complex00.offDiagonalKinetic` only, not `fields.dirac16complex`) and was not changed.
* Runs, from the repository root `D:\Developer\github\Dirac_claude` (32 characters) in the working tree on top
  of commit `6779cd3` and the automatic snapshots after it (none of them changed the package or an input of
  this set), not in a fresh clone; Windows 11 Pro for Workstations 10.0.26300, WolframScript 1.14.0, Wolfram
  15.0.1; each Wolfram run started detached from a `cmd.exe` batch file, one at a time:
  1. `wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls`: `checks: 52,
     failed: 0`, exit code 0, error stream empty, wall time 49 s (15:45:07 to 15:45:56).
     `wolfram-a4-report.json` byte-identical to the committed one (also to the one of commit `af0fc19`);
     `a4-equations.json` differs from the version of section 6.6 only in line 782 (the two phrases above) and
     now has sha256 `9965d8c0a8d7d77c5a239d5c7d0576326ffd6143b09e68d4ffd8e467a456afd1`, 41869 bytes, 788 lines.
  2. The same command again: `checks: 52, failed: 0`, exit code 0, error stream empty, wall time 50 s
     (15:46:24 to 15:47:13); both outputs byte-identical to run 1.
  3. `python Revision/field_equations_a4/python/check_field_equations_a4.py`, twice: `checks: 63, pass 63,
     fail 0, pending 0`, exit code 0, 10.1 s and 13.3 s wall; `python-a4-report.json` and
     `a4-equations-summary.md` byte-identical between the two runs and to the committed ones.
  4. Failure test E with this script, in a scratch tree holding only the script, the package and the two
     inputs, with no folder `Revision/field_equations_a4/reports` (root of 152 characters): the single line
     `ERROR  cannot write <root>\Revision\field_equations_a4\reports\wolfram-a4-report.json` (233 bytes with
     the scratch root, CR LF included), exit code 1, error stream empty, about 50 s (15:49:19 to 15:50:09);
     `a4-equations.json` was written before and is byte-identical to the one of run 2. This is the normalised form that section 3.6 now quotes; the
     `cannot write` line for `a4-equations.json` comes from the same function `writeJSON` with the same
     normalised folder `$fieldDir` (not run separately with this version).
* Downstream: `Revision/field_equations_a4/ks_source/ks_source_a4.py` records the sha256 of
  `a4-equations.json` among its inputs. It was re-run twice: `pass 23/23`, exit code 0, 3.9 s and 3.8 s, all
  four outputs byte-identical between the runs. `ks_source/reports/ks-source-a4.json` differs from its
  previous version only in line 6, which now records
  `9965d8c0a8d7d77c5a239d5c7d0576326ffd6143b09e68d4ffd8e467a456afd1` (new sha256 of the report
  `a11e3f6e29fc33c8211ae0282f27b5b205998012b3696623739d88dc3c106588`, 20026 bytes); its summary and the two
  results CSV files are unchanged. `python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py`:
  10 tests OK (19.0 s).
* Fixes made: the text above. Open discrepancies: none in the results. Not done: a run of the changed script in
  a fresh clone.
