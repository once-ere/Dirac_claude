# WolframScript provenance: the a4 field-equation verifier

**2026-10-16 (section 6.10): the corrected metric (version 2).**  On the user's order "go ahead with the recomputation
using the corrected metric" (`HANDOFF.md` 0.10, phase W2) the set computes the field equations of the corrected metric of
`Revision/SPEC.md` section 1, diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), for
general a4(x4), b4(x4) > 0 and EVERY real z = 6 H x0 (an exact zero test modulo Cos^2 + Sin^2 - 1, ww^12 - Sin^2,
Sign[Cot]^2 - 1 replaces the patch 0 < z < Pi/2 and PowerExpand).  Every Lovelock tensor is diagonal and free of x0
(three independent components x4, x1, x0 = x5); the source must have p0 = p_t and no off-diagonal component.  57 checks,
all PASS; the sympy twin `check_field_equations_a4.py` 69 of 69; `check_b4_block.py` (the key b4 of the metric of
2026-10-14) is retired.  The tables of section 2 give the files of 2026-10-16.  The text of sections 1 and 3 to 6.9
describes the earlier versions (the metric of 2026-10-14 and before); section 6.10 lists what changed.

Set: `Revision/field_equations_a4/wolfram/` (the script `verify_field_equations_a4.wls` and its
package `FieldEquationsA4.wl`), in the version of 2026-10-14: the user's metric with b4[x4] in the extra-time
components (commit `c26995c`) in the author's coordinates {x0, x1, ..., x7} (commit `fedf89c`; section 6.8). It
computes every spinor statement with the author's real 16 x 16 Dirac matrices T16. Sections 6.1 to 6.7 record the
verifications of earlier versions (52 checks, metric without b4, the withdrawn labels x1..x8 with the hidden
direction x8 listed last; the map to the author's labels is x8 -> x0, xk -> xk for k = 1..7). This file tells you what
the set computes, which files it reads and writes, exactly how to run it, what you should see,
what it changes on your computer, and how it was verified. Everything you need to run it is in
section 3 of this file.

## 1. What the set is and what it computes

In plain words: the author's theory lives in an 8-dimensional spacetime with the author's coordinates
x0 (a hidden direction, written through z = 6 H x0 with 0 < z < pi/2), x1, x2, x3 (ordinary 3-space), x4 (time)
and x5, x6, x7 (three extra time directions). Distances in 3-space carry the scale factor e^{a4(x4)} and distances
along the extra times the scale factor e^{-a4(x4)} b4(x4)^{1/2} (both times sin^{1/6} z), so when 3-space expands
the extra times shrink exponentially (they deflate). The unknown functions are a4(x4) and, since the metric of
2026-10-14, b4(x4); sections 1 to 6 of the script treat b4 = 1 (the metric before 2026-10-14), its section 7 the
general b4. The set answers: which equations must a4(x4) (and b4(x4)) obey, and what matter can drive them? The task is defined in `Revision/SPEC.md`, section 5; the Dirac matrices are
those of SPEC section 2.

Step by step, the script (with its package) does the following, using exact algebra only (no
floating-point numbers anywhere):

1. Geometry. It writes down the metric, g = diag(cot^2 z, e^{2 a4} s, e^{2 a4} s, e^{2 a4} s, -1,
   -e^{-2 a4} b4 s, -e^{-2 a4} b4 s, -e^{-2 a4} b4 s) in the order x0, x1, ..., x7, with s = sin^{1/3} z
   (b4 = 1 in sections 1 to 6 of the script), and computes from it
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
   kappa (p3 - p_t), an x0 equation, the algebraic condition p3 + p_t = 2 p0, the propagation of
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

6. The general b4 (section 7 of the script, 12 checks, key `b4` of `a4-equations.json`): the Lovelock
   tensors equal the set of `Revision/metric_b4`, the constraint stays first order, the off-diagonal
   equations kappa q40 = cot z (b4'/b4) Q and kappa q04 = -tan z (b4'/b4) Q, the identity that replaces
   p3 + p_t = 2 p0, the general conservation law, gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4),
   the condensate in the metric with b4 and the vacuum of the linear member with the author's weights.

Each of these statements is a named check with the verdict PASS or FAIL. There are 64 checks (52 for b4 = 1
and 12 for the general b4; the 52 are those of the earlier versions, five of them renamed with x0). The
script writes two files: `a4-equations.json` (every equation, in Wolfram InputForm and in TeX) and
`reports/wolfram-a4-report.json` (every check with name, verdict and a one-line explanation).

Documents and programs that cite or read these results (found on 2026-10-08, for your information
only; you do not need them to run this set; the counts they quote are those of 2026-10-08):

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
with gamma^(xk) = T16[k] for k = 0, 1, ..., 7 (gamma^(x0) = T16[0] is the hidden direction). They are
re-constructed by `Revision/algebra/wolfram/RevisionAlgebra.wl` (from the tau matrices of the notebook) and
stored, in the author's order x0, x1, ..., x7, in `Revision/algebra/gammas.json` by
`Revision/algebra/wolfram/verify_algebra.wls`.

This set follows that instruction: `FieldEquationsA4.wl` (lines 133-193) reads `gammas.json` when
it is loaded, with strict parsing (every matrix entry must be a JSON integer or a string "p/q" in
lowest terms; anything else, or a missing file or key, stops the run with a line `ERROR  ...` and
exit code 1, section 3.6; there is no fallback to other matrices). The primary matrices are
`FEGammaFrame` = the fixture's eight gammas (gamma^(xk) = T16[k], k = 0..7, at Wolfram position k + 1) and
`FEC` = gamma^x0 gamma^x1 gamma^x2 gamma^x3 (the notebook's sigma16). The checks
`fixture_author_T16_read`, `clifford_relations_author_T16` ({gamma^a, gamma^b} = 2 eta^ab with
eta = diag(1, 1, 1, 1, -1, -1, -1, -1) in the order x0..x7) and `C_properties_author_T16` (C equals
the fixture's C, is real symmetric, C^2 = 1, C gamma^a antisymmetric) record this; every spinor
check after them uses these matrices.

The package also builds, in lines 195-203, a comparison representation `FEGammaFrameComparison`
(with `FECComparison`), from Kronecker products of the real 2 x 2 matrices s1 = [[0,1],[1,0]],
e = [[0,1],[-1,0]] and w = s1 e = [[-1,0],[0,1]] (1 = the 2 x 2 unit matrix):

| direction | matrix (`FEGammaFrameComparison`) | square |
| --- | --- | --- |
| x0 (hidden direction) | w(x)w(x)w(x)s1 | +1 |
| x1, x2, x3 (3-space) | s1(x)1(x)1(x)1, w(x)s1(x)1(x)1, w(x)w(x)s1(x)1 | +1 |
| x4 (time) | e(x)1(x)1(x)1 | -1 |
| x5, x6, x7 (extra times) | w(x)e(x)1(x)1, w(x)w(x)e(x)1, w(x)w(x)w(x)e | -1 |

(Each coordinate has the same matrix as before 2026-10-14; only the list order changed.)

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
| script (the file you run) | `Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` | 52056 | 511 | `8dd70aafb9bfd2ee291af4a4ec8a1e5192125cdfcbab94f1d30379bf9f54797e` |
| package (loaded by the script with `Get`) | `Revision/field_equations_a4/wolfram/FieldEquationsA4.wl` | 17909 | 254 | `20d49bfcfc83bfc6aead0a3d266ba0f2b97e5688d3062601fc077e1a3143ea71` |
| input 1 (read by the package with `Import[..., "RawJSON"]`) | `Revision/algebra/gammas.json` | 76894 | 1405 | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| input 2 (read by the script, section 2) | `Revision/gkd_lovelock/results/lovelock-tensors.json` | 164399 | 405 | `611a60543bcf36261e54d1304a2eb216efc39596ba2ad8fc33c353a740787343` |
| input 3 (read by the script, sections 3 and 4) | `Revision/metric_warped/results/warped-metric.json` | 5508 | 74 | `c6167b356838f9ce4708f8826c561c001060b512acc73a101df4581f62c01aa6` |
| output 1 (written, committed) | `Revision/field_equations_a4/a4-equations.json` | 64220 | 837 | `fba6e3af9c56f5e6c61819762a1fccfede5f6ab4875f3e4fa736d2afb13df72d` |
| output 2 (written, committed) | `Revision/field_equations_a4/reports/wolfram-a4-report.json` | 21797 | 294 | `ad4777d477e93f04a4d70f21775f49b2fcd8132f7ad170b1ae724b1b44cda434` |

The table gives the version of 2026-10-16 (section 6.10: the corrected metric).  The version of 2026-10-15 (section
6.9, withdrawn): script 51887 bytes, 531 lines, sha256 `19ab567d4786c17cb67246053f434629d4620ce36132be549237228ee63ef58d`;
package 16131 bytes, 229 lines, sha256 `19cd007b0300b1641c753a139ed6afb000ca83c274c6d2e6b20a6ce0f3e037a4`; input 3 was
`Revision/metric_b4/results/metric-b4.json` (sha256 `7a57e570...`); output 1 100062 bytes, 935 lines, sha256
`fa2acb5d9b55d49bbee79be2e5551a1efc3c9a78daad101eb3e12f441d47ad00`; output 2 22186 bytes, 304 lines, sha256
`31bf1893d2a1d5a6f9e2165b67d67b2d5b5fca825fa11a2b3fdae2ef016eee49`. The version of 2026-10-14
(section 6.8): script 53312 bytes, 551 lines, sha256 `82c224295feed0aaf0653c5615b0f4dfb2ac9d302431368153a4da7437b45ad5`;
output 1 68631 bytes, 922 lines, sha256 `dba03bf4f09c3ac080b3abb6fc34e528bb9ba32e52d21b508c630b6479ba759d`; output 2
19869 bytes, 329 lines, sha256 `7caf8938f0c3854c3f90ab0400fd16e044d410bc02c4c24e3dbdb41068e4f5f9`. The paragraph that
follows describes the versions of 2026-10-08 (sections 6.3 to 6.7).

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
`gammas.json` (`FileHash`, package line 177) and writes it into the detail of the check
`fixture_author_T16_read`. Both inputs are produced by other sets (`gammas.json` by
`Revision/algebra/wolfram/verify_algebra.wls`, `lovelock-tensors.json` by the Rust program in
`Revision/gkd_lovelock/code`); they are committed, so you need neither to run this set. The two
outputs are deterministic: LF line endings, no time stamps, no machine names, fixed key order. The
script and the package contain no random numbers, no dates, no parallel computation and no network
functions; the script writes only through its function `writeJSON` (one `OpenWrite`, script line
44), which it calls twice (line 523 for `a4-equations.json`, then line 528 for the report). Since the metric of
2026-10-14 the script also reads `Revision/metric_b4/results/metric-b4.json` (input 3; if it is missing the run
stops with `ERROR  <path>: not found (run Revision/metric_b4/wolfram/verify_metric_b4.wls)` and exit code 1).

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
* All 64 checks pass but `git status` shows `a4-equations.json` or `wolfram-a4-report.json` (or
  both) as modified: you are probably using a Wolfram version other than 15.0.1, whose TeX or
  InputForm formatting differs. Both files contain expressions formatted by Wolfram:
  `a4-equations.json` in InputForm and TeX, and the explanations in `wolfram-a4-report.json` in
  InputForm (for example `"detail": "L_(1) = 12*ad1^2 - 84*H^2"`). The mathematics (the 64 checks)
  is what matters; only Wolfram 15.0.1 was verified to reproduce the committed bytes. Restore both
  committed files with
  `git checkout -- Revision/field_equations_a4/a4-equations.json Revision/field_equations_a4/reports/wolfram-a4-report.json`.

## 4. Expected output

Printed on the screen (standard output), exactly one line (the version of 2026-10-14; the earlier versions
printed `checks: 52, failed: 0`):

```text
checks: 64, failed: 0
```

Nothing is printed on the error stream, no `FAIL` or `ERROR` line appears, and the exit code is `0`
(`$LASTEXITCODE` in PowerShell, `echo $?` in bash/zsh). If a check failed, the line would read
`checks: 64, failed: <n>`, each failed check would be listed on a line
`FAIL <name>: <explanation>`, and the exit code would be `1`.

Files written (both are overwritten on every run that reaches its end):

1. `Revision/field_equations_a4/a4-equations.json` (68631 bytes, 922 lines). Its top-level keys
   are `title`, `producer`, `conventions`, `lovelockTensors`, `generalSource`, `einstein`,
   `linearMember`, `fields`, `b4`, `checksSummary`; its second line begins
   `  "title": "Einstein-Lovelock field equations for a4[x4] and b4[x4] in the primordial metric (Revision/SPEC.md section 5); the keys lovelockTensors .. fields are the restriction b4 = 1`.
   For example `generalSource.evolution_F.input` is
   `2*alpha1 - 48*ad1^2*alpha2 + 720*ad1^4*alpha3 - 80*alpha2*H^2 + 864*ad1^2*alpha3*H^2 + 720*alpha3*H^4`
   (ad1 = a4').
2. `Revision/field_equations_a4/reports/wolfram-a4-report.json` (19869 bytes, 329 lines). Its first
   six lines are:

   ```text
   {
     "producer": "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls",
     "spec": "Revision/SPEC.md section 5",
     "checkCount": 64,
     "failedCount": 0,
     "verdict": "PASS",
   ```

   Show them with `Get-Content Revision/field_equations_a4/reports/wolfram-a4-report.json -TotalCount 6`
   (PowerShell) or `head -n 6 Revision/field_equations_a4/reports/wolfram-a4-report.json`
   (macOS/Linux). If Python is installed, this prints `64 0 PASS`:
   `python -c "import json; r=json.load(open('Revision/field_equations_a4/reports/wolfram-a4-report.json')); print(r['checkCount'], r['failedCount'], r['verdict'])"`
   (use `python3` on macOS/Linux).

How to check that you reproduced the committed results exactly:

* With git: `git status --porcelain` prints nothing (both outputs are byte-identical to the
  committed files, so git does not see a change).
* With checksums: `Get-FileHash Revision/field_equations_a4/a4-equations.json, Revision/field_equations_a4/reports/wolfram-a4-report.json -Algorithm SHA256`
  (PowerShell; it prints the hash in capital letters, compare ignoring case),
  `shasum -a 256 <file>` (macOS) or `sha256sum <file>` (Linux), and compare with the sha256 of
  the two output rows in section 2.

The 64 checks, in the order of the report (all PASS):

| section | checks |
| --- | --- |
| geometry (4) | `metric_is_SPEC_section_1`, `sqrt_abs_det_g_is_cos_z`, `mixed_riemann_free_of_warp_and_a4`, `riemann_pair_antisymmetry` |
| Lovelock tensors (17) | `P1_direct_equals_minus_4_Einstein`; for k = 1, 2, 3: `Pk_direct_equals_gkd_branch_monomials`, `Lk_direct_equals_gkd_branch`, `Pk_trace_identity`, `Pk_structure`; `P4_vanishes_pigeonhole`, `E1_divergence_free`, `E2_divergence_free`, `E3_divergence_free` |
| field equations, general source (7) | `independent_components`, `evolution_factorises_a4pp_times_F`, `evolution_F_not_identically_zero`, `algebraic_identity_x1_plus_x5_minus_2x0`, `x0_component_contains_no_a4pp`, `constraint_propagation_bianchi`, `conservation_components` |
| Einstein case (3) | `einstein_components`, `einstein_null_energy_x0`, `einstein_no_vacuum_solution` |
| linear member (3) | `linear_member_equal_pressures`, `linear_member_vacuum_factor`, `einstein_gauss_bonnet_vacuum_linear` |
| spinor sources (18) | the author's T16: `fixture_author_T16_read`, `clifford_relations_author_T16`, `C_properties_author_T16`; comparison representation: `clifford_relations_own_rep`, `C_properties_own_rep`, `representations_equivalent_author_T16_own_rep`; in T16: `spin_connection_antisymmetric`, `Omega_x0_Omega_x4_vanish`, `gamma_mu_anticommutes_with_Omega_mu_no_sum`, `gravity_term_gamma_mu_Omega_mu`, `condensate_equation_x0_consistent`, `condensate_S_constant`, `condensate_adjoint_equation`, `condensate_kinetic_tensor_diagonal`, `condensate_offdiagonal_are_three_gamma_bilinears`, `offdiagonal_coefficients_representation_independent`, `condensate_einstein_quadratic_U`, `condensate_diagonal_witness_exact` |
| general b4 (12) | `b4_lovelock_equals_metric_b4_set`, `b4_constraint_first_order`, `b4_offdiagonal_factorises`, `b4_einstein_offdiagonal_forces_b4_constant`, `b4_identity_x1_plus_x5_minus_2x0`, `b4_einstein_second_order_system`, `b4_conservation_components`, `b4_gravity_term`, `b4_condensate_equation`, `b4_condensate_kinetic_diagonal`, `b4_condensate_offdiagonal_bilinears`, `b4_author_weights_vacuum` |

Five names carry the hidden label: before 2026-10-14 they read `algebraic_identity_x1_plus_x5_minus_2x8`,
`x8_component_contains_no_a4pp`, `einstein_null_energy_x8`, `Omega_x4_Omega_x8_vanish`,
`condensate_equation_x8_consistent` (and, in the b4 section of commit `c26995c`, `b4_identity_x1_plus_x5_minus_2x8`).

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
6.8 records the version of 2026-10-14 (the metric with b4, the author's coordinates x0..x7, 64 checks). 6.9 makes every
section general in b4 (2026-10-15), 6.10 records the corrected metric of 2026-10-16 (version 2) and 6.11 the
Kohn-Sham source parts for it (phase W5); from 6.8 on the newest section comes first.

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

### 6.11 The Kohn-Sham source parts for the corrected metric (2026-10-16/17, `HANDOFF.md` 0.10, phase W5)

* Why. Phase W2 (section 6.10) removed the keys of the metric of 2026-10-14 that `python/check_ks_source_conditions.py`
  and `ks_source/ks_source_a4.py` read (generalSource.identity_*, offDiagonal_*, exponentialHistory.*.Q); both evaluate the
  Kohn-Sham states, which were recomputed for the corrected metric in phase W5 (`Revision/kohn_sham`: N_mid = 592,
  N_large = 2352, kappa = e^{-a4} constant in y, P = e^{-3Hy}/Vol_7, the lambda = 0 states exact fold-band gases).
* `python/check_ks_source_conditions.py` (rewritten, 5 checks; the Wolfram verifier and its sympy twin are unchanged):
  C1 every component independent of x0 (generalSource.x0_dependence), C2 p0 = p_t (hiddenEqualsExtraTimes), C3 no
  off-diagonal component (offDiagonal; the eigen-orbitals have T^x4_y = 0), C4 the source that the record's history needs
  with the author's weights (exponentialHistory.authorWeights.historySource_kappaT_minus_Lam), and the list of the zero
  states. Result (5 of 5): No Kohn-Sham state recorded in Revision/kohn_sham is an admissible source of the corrected metric: C1 fails for every nonzero state, for every a4(x4) and b4(x4); C2 (p0 = p_t) holds exactly for the lambda = 0 states and fails for lambda != 0; C3 holds; the states are not the source C4 that the history needs (no constant kappa reproduces its ratios).  The Kohn-Sham history a4 = H x4, b4 = e^((4/3) H x4) is a prescribed background without back-reaction.
* `ks_source/ks_source_a4.py` (rewritten, 19 checks; `ks_source/README.md`): A1 to A6 exact (sympy, from
  a4-equations.json), B0 to B3 the profiles, C1 to C4 the hidden-direction moments, D0 to D4 the integration of the
  x0-averaged second-order system with the averaged free fold-band gas (an APPROXIMATION, stated). Result (19 of 19): No recorded Kohn-Sham state is an admissible source of the corrected metric: every nonzero state depends on x0 (B3), and the interacting states violate p0 = p_t also after averaging (C1); the off-diagonal condition holds. The free (lambda = 0) gas is an exact fold-band gas: averaged over x0 it is rho_bar = C b4^{-2}, p3 = rho/3, p0 = p_t = 0, a source that conserves energy for every a4, b4 (A5, D0). The record's history a4 = H x4, b4 = e^{(4/3) H x4} needs a source that changes sign along it (A6, C3); the Kohn-Sham gas does not supply it: the history is a prescribed background without back-reaction. With the averaged free gas as the source, the x0-averaged equations started on the record's history evolve differently (D2, D4; outcomes in results/ks-source-a4-cases.csv).
* Mistakes found by the runs and corrected before the commit (`claude_failures.md` H10): the first restated C4 claimed
  that the N = 8 states have rho_bar with the sign of lambda and rho_bar + p3_bar = 0; the data give the sign of -lambda
  and 0 < p3_bar/rho_bar < 1 (the check states the measured relation). Three texts stated facts that were not computed
  (the sign of kappa in D2, the sign change and the positivity in C3, the slice count in C2); they now follow the
  computed values. The first run on the new dense history failed D3 (the x4 constraint along the integrated solutions,
  tolerance 1e-8 relative): fixed RK4 steps did not resolve the runaway solutions and the approach to det J = 0
  (residual 1.2e-2 and 4e-6 there, 1e-12 elsewhere); the integration now covers every base step with step-doubling
  substeps (local error 1e-12) and detects the singular surface at 1e-6 of det J(0); D3 is unchanged and gives 8.9e-11
  (`claude_failures.md` H13). The unit test asked for at least 20 checks of a record that has 19; it now pins the 19
  names.
* Runs (2026-10-17, development machine, Windows 11, from the repository root, each under `timeout -k 5 423`):
  `python Revision/field_equations_a4/python/check_ks_source_conditions.py`: 5 of 5, 0.7 s.
  `python Revision/field_equations_a4/ks_source/ks_source_a4.py`: 19 of 19, 4.4 to 4.5 s (two runs, outputs
  byte-identical); `python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v`: 9 tests OK
  (19.8 s; the rerun test reproduces the committed outputs byte for byte, the two negative controls fail as they must).
  Inputs: the Kohn-Sham record of `Revision/kohn_sham` (the Rust solver of phase W5) and the dense history
  `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` (`run_ks_history.py` in three parts of 23 s and
  an assembly of 0.7 s; 615 runs, 8 of 8 checks).
* Not done: a run in a fresh clone (planned after the last phase of `HANDOFF.md` 0.10).

### 6.10 The corrected metric of 2026-10-16 (version 2)

* Why. The user's orders of 2026-10-16 (`Revision/SPEC.md` section 1, version 2; `Revision/metric_warped/`; "go ahead
  with the recomputation using the corrected metric", `HANDOFF.md` 0.10, phase W2).  The metric of 2026-10-14 has the
  off-diagonal Lovelock component E^x4_x0 ~ cot z b4'/b4, which no diagonal source can match; the corrected metric
  diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)) (x0 space-like, x4 the time,
  z = 6 H x0 real) has none.
* Changes, package (`FieldEquationsA4.wl`): the metric and the vielbein (e^x0 = E^(-a4) b4^(1/2) Cot z, signed; e^xi =
  E^a4; e^x4 = 1; e^xt = E^(-a4) b4^(1/2) (Sin^2)^(1/12)); `FENormal` is now an exact normal form for EVERY real z
  (Sin -> sv, Cos -> cv signed, (Sin^2)^k -> ww^(12 k), |Sin|^k -> ww^(6 k), |Cot| -> sgn cv/sv, Sign[Cot] -> sgn;
  numerator and denominator reduced modulo the Groebner basis {cv^2 + sv^2 - 1, ww^12 - sv^2, sgn^2 - 1}; an unmapped
  trigonometric function of x0 stops the run); the patch rules `FETrigToCC` (0 < z < Pi/2, cc > 0) and `PowerExpand`
  are removed; `FEUVK` writes an x0-free expression in the variables of the field equations (ad1, ad2, uu = b4'/b4,
  vv = (b4'/b4)', kk = E^(2 a4)/b4) and refuses anything else; the monomial reader takes the 14 exponents of the GKD
  branch (since 2026-10-16) and refuses 13.
* Changes, script: section 1: `sqrt_abs_det_g` (E^-a4 b4^2 |cot z| (sin^2 z)^(1/4)), `mixed_riemann_free_of_x0`,
  `mixed_riemann_only_sectional`, `flat_member` (a4 = 0, b4 = H^2 (x4 - c)^2: R = 0).  Section 2: `P<k>_structure`
  (diagonal, x0-free, x1 = x2 = x3, x0 = x5 = x6 = x7), `lovelock_variables` (polynomials in H, a4', a4'', u, v, k).
  Section 3: `independent_components` (three components; p0 = p_t and no off-diagonal source), `constraint_first_order`,
  `second_order_system_a4pp_vv` (Einstein J = {{2, -2}, {0, -3/2}}), `constraint_propagation_bianchi` (d4 E^x4_x4 =
  3 a4' (E^x1_x1 - E^x4_x4) + 4 h4 (E^x0_x0 - E^x4_x4), h4 = b4'/(2 b4) - a4'), `conservation_components` (with a
  general off-diagonal pair), `einstein_equals_metric_warped_record` (input 3 replaces `metric-b4.json`),
  `einstein_components`, `einstein_null_combinations`, `einstein_flat_vacuum`, `einstein_no_exponential_vacuum`,
  `einstein_second_order_system`.  Section 4 (exponential histories, k = k0 e^((2 - beta) A H x4)):
  `exponential_history_required_source`, `author_weights_history_source` (equal to warped-metric.json, key
  history_source), `author_weights_no_exponential_vacuum`, `egb_exponential_vacuum_branches` (only constant k, beta = 2,
  alpha2 = -1/(4 H^2 (A^2 - k0))).  Section 5 (fields): `Omega_x4_vanishes_Omega_x0_does_not`, the gravity term
  (3/2) H e^{a4} b4^{-1/2} gamma^x0 + (b4'/b4 - a4'/2) gamma^x4, the condensate Phi = e^{a4/2} b4^{-1} chi with chi' = B chi,
  `condensate_S_law` (S = e^{a4} b4^{-2} S0), the kinetic tensor, 24 off-diagonal three-gamma bilinears (36 ordered
  pairs), `condensate_witness_constant_k_exact` (exact witnesses for histories with constant k and constant M; for k not
  constant not decided), `condensate_source_equal_pressures` (Einstein: none on the exponential histories; the author's
  weights: only constant k, k0 = (16 + 2 A^2)/(2 + A^2) at beta = 2 and k0 = 8 at A = 0).  Removed: the off-diagonal
  pair and its factor Q, the identity x1 + x5 - 2 x0, the key b4 and the checks of the metric of 2026-10-14.  57 checks.
* `a4-equations.json`: keys conventions, lovelockTensors (x0x0, x1x1, x4x4, x5x5 in ad1, ad2, uu, vv, kk), generalSource
  (constraint_x4, space_x1_eq_x2_eq_x3, hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7, hiddenEqualsExtraTimes, offDiagonal,
  secondOrderJacobian(Det), x0_dependence, conservation_x4, conservation_x0, energyExchange, constraint_propagation,
  sourceRequiredByGivenHistory, nullCombinations), einstein, exponentialHistory (requiredSource, einstein, authorWeights
  with historySource_kappaT_minus_Lam, einsteinGaussBonnetVacuum), fields.  The keys b4, generalSource.offDiagonal_*,
  offDiagonalFactor_Q, identity_x1_plus_x5_minus_2x0, extraTime_x5_eq_x6_eq_x7, hidden_x0 and exponentialHistory.*.Q are
  gone; their readers (the Kohn-Sham source conditions, `ks_source/`, the dark sector, the lead checks, the documents
  and the textbook) are redone in the later phases of `HANDOFF.md` 0.10.
* Runs (2026-10-16, development machine, Windows 11, Wolfram 15.0.1, from the repository root, each under
  `timeout -k 5 423`): `checks: 57, failed: 0`, exit code 0, 20 s and 19 s; the two runs wrote both outputs byte for
  byte (sha256 in section 2).  Mistakes found by the runs and corrected before the commit: the guard of `FENormal`
  first refused the general source functions p0[x4, x0] (it now refuses only unmapped trigonometric functions of x0);
  the condensate check first claimed no equal-pressure history for the author's weights, and Reduce showed the two
  constant-k families above (the check now states them).
* The sympy twin `check_field_equations_a4.py` (rewritten: symbols Ee, Bq, Cc signed, Ww = (sin^2)^(1/12) with
  Ww^12 (1 + Cc^2) = 1; the ring QQ[H, a4', a4'', u, v, k]; GKD as a permutation sign; its own off-diagonal
  decomposition and witness): 69 of 69, 8 s, twice, byte-identical report (sha256
  `38aa38710df9ffc0ffb50814aa54ff8723ff4396145d60527df65367c32ddedb`) and summary.  Two of its checks failed in the
  first run and were corrected: the Einstein-Gauss-Bonnet coefficients of (alpha2, Lambda) are the same in the x4 and
  x1 equations at beta = 2 (the pair x4, x0 determines them), and the root k = -A^2 of the equal-pressure condition is
  not positive.

### 6.9 Every section for general b4 (2026-10-15)

* Why. The user's orders of 2026-10-15: "b4 is a function of x4; b4 is NEVER 1" and "yes, move everything to b4(x4);
  b4 is never 1" (`HANDOFF.md` 0.9). Until then the script's sections 3 to 6 restricted the tensors to b4 = 1 (`FEB4One`).
* Changes. The package is unchanged (it computes for general b4). The script: no restriction to b4 = 1 any more;
  section 3 (general source) states the components for general a4 and b4 (in u = b4'/b4, v = u'), the off-diagonal pair
  E^x4_x0 = cot z u Q, E^x0_x4 = -tan z u Q, the second-order system in (a4'', v) with its Jacobian, the identity
  x1 + x5 - 2 x0, the Bianchi identity with b4 (d4 E^x4_x4 = 3 a4' (E^x1_x1 - E^x5_x5) + (3/2) u (E^x5_x5 - E^x4_x4) +
  6 H u Q), the conservation law, the Einstein case (Q = 3 H/2: a source without T^x4_x0 forces b4' = 0; no vacuum);
  section 4 replaces the linear member by the exponential histories a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) (the
  required source; the author's weights: Q = 3 beta (3 beta - 4)/(64 H) at A = 1, the history beta = 4/3 of SPEC
  section 1 with the source kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27); vacuum only for beta = 0; the
  Einstein-Gauss-Bonnet vacuum branches beta = 4 and beta = 2 (1 + A^2)/A^2); section 5 (fields) for general b4 (the
  condensate Phi = b4^(-3/4) chi, b4^(3/2) S constant, the witnesses for every b4, the condensate as a source with b4
  not constant). `a4-equations.json`: the keys lovelockTensors, generalSource, einstein, exponentialHistory (new,
  replaces linearMember) and fields are general; the key b4 keeps the formulas of 2026-10-14 for its readers (the dark
  sector). 59 checks (64 before; the 12 checks of section 7 are merged into sections 3 to 5).
* A mistake found by the run: the second Einstein-Gauss-Bonnet branch was first written with alpha2 = A^2/(4 H^2 (A^2 -
  1)^2); Reduce showed the sign is negative; corrected before the commit.
* Runs (2026-10-15/16, Windows 11, Wolfram 15.0.1, from the repository root, each under `timeout 423`): `checks: 59,
  failed: 0`, exit code 0, wall 45 s; a second run gave both outputs byte for byte. The sympy twin
  `check_field_equations_a4.py` (rewritten for general b4: its own ring with b4^(1/2), u, v): 65 of 65, 8 s;
  `check_b4_block.py` 11 of 11 and `check_ks_source_conditions.py` 6 of 6 with unchanged outputs. `ks_source/ks_source_a4.py`
  reads keys of the restriction b4 = 1 (lovelockTensors in that form, evolution_F) and stops with a KeyError until it is
  moved to b4 in phase 5 of `HANDOFF.md` 0.9.

### 6.8 The metric with b4 and the author's coordinates x0..x7 (2026-10-14)

* Why. (1) On 2026-10-14 the user gave the metric with b4[x4] in the extra-time components,
  diag(Cot[6 H x0]^2, E^(2 a4) Sin^(1/3) (x1, x2, x3), -1, -E^(-2 a4) b4 Sin^(1/3) (x5, x6, x7)); (2) the same day the
  user ordered that their coordinates X = {x0, x1, ..., x7} be used throughout (x0 = the hidden direction, listed
  first); this set had named them x1..x8 with the hidden direction x8 listed last. Sections 6.1 to 6.7 record the
  earlier version (52 checks, metric without b4, labels x1..x8).
* Changes. Commit `c26995c`: `FieldEquationsA4.wl` builds the metric and the vielbein with b4 (symbols `bb`, `bd1`, ...;
  `FEB4One` restricts to b4 = 1); the script's sections 3 to 6 are the restriction b4 = 1 and every earlier statement
  holds there byte for byte; the new section 7 (12 checks, key `b4` of `a4-equations.json`) treats the general b4 and
  reads `Revision/metric_b4/results/metric-b4.json` (input 3). Commit `fedf89c`: the coordinates `FECoords = {x0, ...,
  x7}`, the metric, vielbein and eta in the author's order, `FEC = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)` with the
  fixture's gamma[k] = gamma^(xk), the comparison representation in the new order (the same matrix for every
  coordinate), every position in the script (hidden direction at position 1, x4 at 5); the keys of `a4-equations.json`
  `x8x8`, `x4x8`, `x8x4`, `hidden_x8`, `conservation_x8` and the symbols `p8`, `q48`, `q84`, `d8...` are now `x0x0`,
  `x4x0`, `x0x4`, `hidden_x0`, `conservation_x0`, `p0`, `q40`, `q04`, `d0...`; five check names carry x0 (section 4).
  On 2026-10-14 also: `python/check_ks_source_conditions.py` and `ks_source/` relabelled (they read the relabelled
  Kohn-Sham outputs, where the hidden-direction pressure is now `p0`).
* Runs (2026-10-14, Windows 11, Wolfram 15.0.1, from the repository root, other jobs of this work on the machine):
  `checks: 64, failed: 0`, exit code 0, wall 45 s (run of commit `fedf89c`) and 51 s (a second run on the working
  tree on top of commit `fedf89c`, with only documents of this set changed): both outputs byte-identical to the
  committed ones (sha256 in section 2). The sympy twins: `check_field_equations_a4.py` 63 of 63, `check_b4_block.py`
  11 of 11; `check_ks_source_conditions.py` 6 of 6; `ks_source/ks_source_a4.py` 23 of 23 (2 s) and its 10 unit tests
  (9 s).
* Same physics. A comparison of the new `a4-equations.json` with the one committed before the relabel (in commit `cae873a`; exact, in WolframScript,
  after renaming x8 -> x0, p8 -> p0, q48 -> q40, q84 -> q04, d8 -> d0, k8 -> k0 and the keys x8x8, x4x8, x8x4): all 78
  `input` expressions are equal, and the 42 off-diagonal kinetic coefficients are equal component by component (with
  the sign of the permutation where a three-gamma bilinear is now listed in the new coordinate order). The report has
  the same 64 checks with the same verdicts in the same order.
