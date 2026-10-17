# Provenance of the wolframscript set `Revision/theory/wolfram/` (the field theory of dirac16complex and dirac16complex00, and the scope of its statements)

Status: both scripts of this set were executed twice, each time in a fresh clone of
`https://github.com/once-ere/Dirac_claude.git`, on two occasions: on 2026-10-02 at commit
`c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and again, after a restart of the verification, on 2026-10-07
at commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`. Every run of both scripts finished with exit code 0
(84 of 84 and 15 of 15 checks PASS), and every output file was byte-identical to the committed file and
between the two runs. One execution defect was fixed on 2026-10-02 (an output file that cannot be written
is now reported with exit code 2 instead of being ignored; section 6.6); the fix is part of commit
`a4c5eda`. Unless stated otherwise, the measured values in this file are those of 2026-10-07. On
2026-10-08 three statements of the text (sections 1.4 and 3.7) were corrected after an independent review;
no file of the set, its input or its outputs changed (section 6.6). Later on 2026-10-08 both scripts were
changed, in texts and file paths only (section 6.7): the details of three checks no longer call the U(1)
charge "the conserved charge" without qualification, and the repository root is normalised with
`ExpandFileName`. `verify_scope.wls` was then run twice again (15 of 15, exit code 0, the two reports
byte-identical, and different from the earlier committed report only in that detail text); the re-run of
`verify_field_theory.wls` (one run, 2026-10-08, 1783 s) passed 84 of 84 with exit code 0, and its report equals the
previous one except for the two changed detail texts (section 6.7).

**2026-10-14 (section 6.8).** The set now uses the author's own coordinates X = {x0, x1, ..., x7} (x0 = the hidden
direction, listed first, as in the author's notebooks); the labels x1..x8 with the hidden direction x8 listed last, used until
then, are withdrawn (map x8 -> x0, xk -> xk). Names derived from the old label of the hidden direction follow it:
`p8` -> `p0`, `w8` -> `w0`, `B48`/`B84` -> `B40`/`B04`, `k8` -> `k0`, `d8` -> `d0`; the checks
`gammaOmega_equals_3H_gamma_x8`, `T_x4_x8_component_*`, `exact_solution_x4_x8_*` and
`good_sector_x8_independent_modes_without_boundary_condition` are now named with `x0`. In the same change the three
slow sections of `verify_field_theory.wls` evaluate their exact zero tests on parallel subkernels, so that one run takes
about 5 minutes instead of 30 to 42 (section 6.8). The tables of section 2 give the files of 2026-10-14; the text
below describes the earlier runs where it says so.

**2026-10-15 (section 6.9): everything for the metric with b4(x4).** On the user's orders of 2026-10-15 ("b4 is
a function of x4; b4 is NEVER 1"; "move everything to b4(x4); b4 is never 1") the set proves every statement for the
author's metric with the second function b4(x4), g55 = g66 = g77 = -E^(-2 a4) b4 Sin[z]^(1/3), for GENERAL functions
a4(x4) and b4(x4) > 0; nothing is evaluated at b4 = 1, which appears only as the withdrawn earlier metric. The package
defines that metric; `verify_field_theory.wls` runs in six parts (`base`, `emt-G`, `emt-C`, `solutions`,
`solutions-G`, `quantisation`) and a `merge`, each well below the limit of 7 min 3 s for one calculation (longest
part 156 s); it again has 84 checks, all PASS, and writes 33 formula records. `verify_scope.wls` has 15 checks for
general b4, all PASS. Where this file describes earlier runs (sections 3 to 6.8) it describes the metric b4 = 1 of
those days; the instructions for the present version are in section 6.9.

**2026-10-16 (section 6.10): the corrected metric (version 2).** On the user's orders of 2026-10-16 (the remedy of
`Revision/metric_warped/`: x0 is a hypothetical space-like coordinate and x4 the time, `g44 = -1`, `z = 6 H x0` takes every
real value, `Sin[z]^(1/3) = (Sin[z]^2)^(1/6)`; "go ahead with the recomputation using the corrected metric") the set
proves every statement for the corrected metric `diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1,
-E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3))` for general `a4(x4)`, `b4(x4) > 0` and every real `z` (exact zero test modulo
`Cos^2 + Sin^2 - 1`, `w^12 - Sin^2` with `w = (Sin[z]^2)^(1/12)`, `sign(Cot z)^2 - 1`; no `PowerExpand`).
`verify_field_theory.wls` has 86 checks in the same six parts and the merge (longest part 179 s), all PASS, and writes
33 formula records; `verify_scope.wls` has 16 checks, all PASS. Both were run twice; the outputs of the two runs are
byte-identical. The supplements of 2026-10-14 for b4 are retired. The tables of section 2 give the files of
2026-10-16; the metric of 2026-10-15 is described in section 6.9 and withdrawn.

## 1. What this set is and what it computes

### 1.1 The set in one sentence

Two WolframScript programs prove, with exact computer algebra, the mathematical statements of the
"Revision" field theory of the author's 16-component spinor field in the author's 8-dimensional primordial
gravitational field, and write the verdicts (and the exact formulas) to JSON files that the documents of
the repository quote.

### 1.2 The physics, in plain words

* The world of the theory has 8 coordinates, named and ordered as the author names them: `x0` is a hidden
  space direction; `x1, x2, x3` are ordinary space; `x4` is ordinary time; `x5, x6, x7` are three extra TIME
  directions, which shrink ("deflate") exponentially while ordinary space expands. The signature is 4 + 4
  (four space-like and four time-like directions).
* The gravitational field is the corrected primordial metric of 2026-10-16 (`Revision/SPEC.md` section 1,
  version 2), `diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3))`. It depends on
  `x4` through two functions `a4(x4)` and `b4(x4) > 0` and on `x0` through `z = 6 H x0` with a constant `H > 0`;
  `z` takes every real value, and no sign of `Sin z` or `Cos z` is assumed. (Until 2026-10-16: the metric of
  2026-10-14 on `0 < z < Pi/2`, withdrawn; sections 3 to 6.9 describe the runs of those days.)
* The matter field is a spinor with 16 complex components (a larger relative of the electron's Dirac
  field), built on the author's eight real 16 x 16 Dirac matrices (read from the file
  `Revision/algebra/gammas.json`), in two versions: `dirac16complex`, whose components ANTICOMMUTE
  (Grassmann numbers; the scripts call this statistics `G`), and `dirac16complex00`, whose components
  commute (statistics `C`).
* The field is coupled to gravity through a vielbein (a "frame" at every point) and the canonical spin
  connection. The scripts derive the Lagrangian, the field equations, the conserved current, the
  energy-momentum tensor and the canonical quantisation, and test what each statement does and does not
  depend on.

### 1.3 How the scripts prove it

Nothing is computed with rounded (floating-point) numbers. Each statement is turned into an exact symbolic
computation (fractions, square roots, symbols such as `H`, `a4[x4]`, `m`, `lam`, and general unknown field
functions) whose result must be exactly zero or exactly `True`. Each such computation is a CHECK with a
name and a verdict `PASS` or `FAIL`. A script exits with code 0 only if every one of its checks passes.

`verify_field_theory.wls` (86 checks since 2026-10-16) loads the package `RevisionFieldTheory.wl` and works
through these sections (the names are printed on the screen while it runs; the table describes the corrected
metric of 2026-10-16, section 6.10):

| section (as printed) | checks | what is verified |
| --- | --- | --- |
| (before the first section) | 1 | the exact zero test used by all later checks (a normal form for every real `z`) returns True on identities and False on nonzero control expressions, among them `(Sin z^2)^(1/2) - Sin z` |
| `fixture` | 2 | the gamma matrices read from `Revision/algebra/gammas.json` satisfy `{gamma^a, gamma^b} = 2 eta^ab` with `eta = diag(1,1,1,1,-1,-1,-1,-1)` (order x0..x7); the matrices `C`, `B`, `Gamma`, `S^ab` are the stated products |
| `geometry` | 8 | the diagonal vielbein reproduces the corrected metric; `sqrt|det g| = rftSig E^-a4 b4^2 Cot[z] (Sin[z]^2)^(1/4)`; `H = 0` is a degenerate limit; 21 nonzero Christoffel symbols; the diagonal Ricci tensor and the Ricci scalar equal the sympy record of `Revision/metric_warped`; the metric is flat for `a4 = 0, b4 = H^2 x4^2` and curved on the record's history |
| `spin connection` | 7 | vielbein postulate, the 10 nonzero spin-connection components (`Omega_x0 != 0`, `Omega_x4 = 0`), covariant constancy of the gammas, spin curvature equals the Riemann tensor |
| `gamma^mu Omega_mu` | 3 | `gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)` exactly, independent of `x0`; per direction and the divergence form |
| `Lagrangian, both statistics` | 7 | explicit Grassmann algebra; the Lagrangian is real; symmetrised and unsymmetrised forms differ by a total divergence; the spin connection drops out of the symmetrised Lagrangian |
| `Euler-Lagrange equations` | 11 | the field equation `gamma^mu D_mu Psi = (m + U'(S)) Psi` and its adjoint, from the Euler-Lagrange derivative of every component; the explicit Dirac operator; the chiral block form; the first-order evolution form in `x4` |
| `non-triviality` | 3 | the gravitational terms do not drop out: `gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi`, nonzero for every `H > 0`; the spin connection vanishes only if `a4' = 0`, `b4' = 0` and `H = 0` |
| `current and integrability` | 8 | the conserved current, its reality, the charge density `Psi^dagger B Psi` (an indefinite form), the Lichnerowicz identity |
| `Majorana-type Lg` | 2 | negative control: a Majorana-type Lagrangian with real anticommuting components is a total derivative (it gives no field equation) |
| `energy-momentum tensor by vielbein variation` | 4 | the energy-momentum tensor from the exact first-order vielbein variation, and its symmetric (Belinfante) part |
| `Noether identities` | 5 | the identities of coordinate invariance and local Lorentz invariance; conservation on shell |
| `EMT components` | 9 | diagonal components, trace, kinetic sum on shell, the `x4`-`x0` component, the energy-exchange equations |
| `exact solutions and conservation` | 7 | exact solutions (linear: `m = 0` with any exponent `al`, and `al = -1/4` with any `m`; nonlinear homogeneous: commuting for every `m`, Grassmann for `m = 0`) satisfy the field equation and the conservation of the energy-momentum tensor and of the current |
| `canonical quantisation` | 9 | canonical momentum, the anticommutator `{Psi, Psi^dagger} = B delta / sqrt|g|`, Heisenberg equation = field equation, no positive inner product (Krein space), mode Hamiltonian, explicit Fock-space example |

The last section, `writing outputs`, writes the two output files of section 2.3.

`verify_scope.wls` (16 checks since 2026-10-16) is an independent program (it does not load
`RevisionFieldTheory.wl`; it has its own exact zero test for every real `z`). It tests the SCOPE of the statements:
which values depend on the choice of frame and of field variables, what holds only up to boundary terms, and what
the indefinite structures imply.

| group | checks | what is verified |
| --- | --- | --- |
| `zero_test_controls`, `fixture_gammas` | 2 | the zero test of the file on identities and nonzero controls; the gammas of `Revision/algebra/gammas.json` satisfy the Clifford relation; `C` and `B` are the stated products |
| `boosted_frame_*` | 5 | a frame boosted in the `x4`-`x0` plane reproduces the same metric and its canonical connection satisfies the vielbein postulate; in it `gamma^mu Omega_mu` has a different value, its `gamma^(x0)` part vanishes for a rapidity with `b' = 3 H E^a4 b4^(-1/2)`, its `b4'/b4 - a4'/2` part for no boost, while the spinor curvature stays nonzero |
| diagonal frame and field variables | 5 | the rescaling `Psi = E^(a4/2) b4^(-1) (Sin[z]^2)^(-1/8) chi` removes the term `gamma^mu Omega_mu` (for `U = 0`); this term sees the hidden block (`E^a4 b4^(-1/2)`); the connection-free Lagrangian gives the same equations; the spin connection enters the energy-momentum tensor through the extra times (`K^x4_x5`), not through 3-space |
| boundary terms | 2 | the curved mode operator is Hermitian only up to a boundary term at the degenerate points `Cos z = 0`; without a boundary condition it has complex frequencies wherever `m^2 < (9/4) H^2 E^(2 a4)/b4` |
| growth and energy | 2 | growth rates of extra-time modes are unbounded; the classical energy of `dirac16complex00` is unbounded below |

### 1.4 Which documents and programs use its results

* `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 (record table:
  "Wolfram: 84 of 84 checks pass", "Wolfram: 15 of 15 checks pass"), formulas and check names throughout
  the text, section 16 (reproduction) and section 17 (index of formulas and checks).
* `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` (and its `.tex` and `.pdf`): section 1 (sources),
  formula blocks generated from `Revision/theory/field-theory.json` (for example the 16 component field
  equations of section 5, from the record `field_equation_components`), section 14 (check index) and
  section 16 (reproduction; it records an earlier Wolfram run time of 1029 s for `verify_field_theory.wls`
  on the development machine).
* `Revision/docs/PAIR_CREATION_PROOFS.md` (and its `.tex` and `.pdf`): section 9.1 (count table: 84
  checks, 84 PASS) and section 10 (reproduction).
* `Revision/README.md`: the row of the folder `theory/` ("Wolfram 84/84 ... scope Wolfram 15/15").
* `Revision/theory/python/check_field_theory.py` with `Revision/theory/python/compare_wolfram.py`: the
  independent sympy verifier reads `Revision/theory/field-theory.json` and
  `Revision/theory/reports/wolfram-field-theory.json` and compares them with its own derivation (section
  `comparison_with_wolfram` of `Revision/theory/reports/python-field-theory.json`).
* The publication tests `Revision/tests/test_dirac16complex_field_theory_publication.py`,
  `Revision/tests/test_dirac16complex00_field_theory_publication.py` and
  `Revision/tests/test_pair_creation_proofs_publication.py` re-read the reports and require every cited
  check to exist with verdict PASS and every quoted count to match.
* `Revision/lead_checks/charge_conjugation_and_u1.py` takes its conventions from the keys `Lagrangian`,
  `current` and `quantisation` of `Revision/theory/field-theory.json`.
* `provenance/dirac matrices.md` (the record of the author's eight real 16 x 16 Dirac matrices) names
  `Revision/theory` among the users of `Revision/algebra/gammas.json`, the input of this set: row
  `fixture_Revision_algebra_gammas_json` of its table under the heading "Every gamma source in the
  repository, compared now" (state of commit `97236d2`, 2026-10-08; that file was still being revised at
  the time). Its earlier versions (for example at commit `af2c688`) listed the three files of this set by
  name; that list was removed in commit `389bcda`.
* The textbook notebooks of `Revision/textbook/notebooks/` (work in progress; the list grows while the
  textbook is written) read or quote checks and formulas of the three output files. At commit `97236d2`
  (2026-10-08) these are 25 notebooks, from `00b_eight_directions` to `21d_sakharov_scorecard`, and their
  25 sources in `Revision/textbook/notebooks/src/` (at commit `af2c688`: 20 notebooks, from
  `00b_eight_directions` to `10f_krein_along_history`). To list the notebooks of your copy, run from the
  repository root (section 3.4), in Windows PowerShell (one line; it prints one file name per notebook):

  ```powershell
  Select-String -CaseSensitive -List -Pattern 'wolfram-field-theory\.json|theory/field-theory\.json|wolfram-scope\.json' -Path Revision/textbook/notebooks/*.ipynb | ForEach-Object Filename
  ```

  and on macOS and Linux (it prints one path per notebook):

  ```bash
  grep -l -E 'wolfram-field-theory\.json|theory/field-theory\.json|wolfram-scope\.json' Revision/textbook/notebooks/*.ipynb
  ```

## 2. Files

All files are plain text, pure ASCII (hence also UTF-8), with LF line endings and a final newline.
"Lines" is the number of newline characters.

### 2.1 The scripts and the package

| file | role | lines | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `Revision/theory/wolfram/verify_field_theory.wls` | script: 86 checks in six parts and a merge; writes the part files, then the field-theory report and the formula file | 1036 | 106531 | `ea6f1a7ac8e54c0cf87aabfd40d354de4408ba041190790b98d3b8c088a538b7` |
| `Revision/theory/wolfram/RevisionFieldTheory.wl` | package loaded by `verify_field_theory.wls` (the corrected metric, geometry, the exact zero test for every real z, Grassmann algebra, Lagrangian, Euler-Lagrange derivative, vielbein variation) | 313 | 20516 | `71dd6044d6ac568f3f7edfb6ae0f1d9809e55baa8ffb28106bd7d55ea1482155` |
| `Revision/theory/wolfram/verify_scope.wls` | script: 16 checks; writes the scope report | 273 | 24039 | `740394da4aed51603749de8bd9deaced3e6ecbaa7b6abf0be88f5da01c1a5a05` |

These are the files of 2026-10-16 (the corrected metric, version 2, section 6.10). The files of 2026-10-15 (the
metric with b4(x4), section 6.9, withdrawn): `verify_field_theory.wls` 964 lines, 98520 bytes, sha256
`de089d562b1f91b4dd72c69e819f73014334636f0f86a6d7ebc00ca3d039bb67`; `RevisionFieldTheory.wl` 298 lines, 18951 bytes,
sha256 `3c33d736dbe4362472409b7ff2f007699da55dabac24cc1dd3aa55102975ee14`; `verify_scope.wls` 229 lines, 20900 bytes,
sha256 `7e8d11f58b958bfbec98a052304d8b6cbad291695d982080b06c1c10bfb6f3f3`. The files of 2026-10-14 (the author's
coordinates x0..x7 and parallel subkernels, section 6.8; the metric b4 = 1): `verify_field_theory.wls` 769 lines,
77938 bytes, sha256 `8165a797e117045d2b9f12761fe98a864242d9371c0ccabe697f4cd9cf70f9fd`; `RevisionFieldTheory.wl` 295
lines, 18614 bytes, sha256 `313e617d6df3cad7f1d389d9d85681af176e655f0a103a015bdb5b99c4c4e88f`; `verify_scope.wls` 212
lines, 18062 bytes, sha256 `f47348cab9eb8e2fb77b1089ff003eaf29a8427ff8d923ddb67b37fc5b86dbcb`. Before
2026-10-14 the two scripts were the versions of 2026-10-08 (section 6.7: `verify_field_theory.wls` 735 lines, 74225
bytes, sha256 `107f8803afaa7bb127ea7c6b7b470a7e58dd7199b6d072297a3267942a23cf46`; `verify_scope.wls` 206 lines, 17416
bytes, sha256 `282c4602470812ba678a5b19eb40602febac5f4b73c85fedb78d8bc76549ef54`) and the package the file of commit
`a4c5eda` (292 lines, 18269 bytes, sha256 `31528570831302199c15a5d6f95e8b95a3ed6532a1c3360c4fc526e8f9dad71d`).
The versions of commit `a4c5eda` (`verify_field_theory.wls`: 734 lines, 73931 bytes, sha256
`54064dfb85342e3defcbd28eb36a092b48890b6157d3120bc8160d2001161ac1`; `verify_scope.wls`: 205 lines, 17177
bytes, sha256 `41b9e4a52dcbffe60e6decf62835ece0aef9f5c3388aac7d22236b7f20d6e499`) compute exactly the same
checks with the same verdicts; they differ only in the normalised root and in the detail texts of three
checks (section 6.7). The value of commit `a4c5eda` for `verify_field_theory.wls` is that of the version
with the output-writing fix of section 6.6 (line 706 now stops the script with exit code 2 when an output
file cannot be written; in the version of 2026-10-08 this is line 707, and the same test of
`verify_scope.wls` is its line 203). The version of commit `c2b33cc` and earlier has 734 lines, 73873 bytes and
sha256 `dafe62233cf76106e1dc7bca51ad3aafcf62762eaf37c3af9969f0c955014c9d`; it computes and prints exactly
the same and writes exactly the same files, and differs only when an output cannot be written (section
3.7).

Both scripts find their other files relative to their own location (`$InputFileName`), so they work from
any current folder (tested from `Revision/theory/wolfram`, section 6.4); the usage line in their headers
runs them from the repository root.

### 2.2 Inputs (read only, never modified)

| file | read by | lines | bytes | sha256 |
| --- | --- | --- | --- | --- |
| `Revision/algebra/gammas.json` | both scripts | 1405 | 76894 | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/metric_warped/results/warped-metric.json` | `verify_field_theory.wls` | 74 | 5508 | `c6167b356838f9ce4708f8826c561c001060b512acc73a101df4581f62c01aa6` |
| `Revision/theory/wolfram/RevisionFieldTheory.wl` | `verify_field_theory.wls` | (section 2.1) | | |

`warped-metric.json` is the independent sympy record of the corrected metric (`Revision/metric_warped/python/`,
committed); `verify_field_theory.wls` compares its metric, Ricci tensor, Ricci scalar and gravity term with it (until
2026-10-15 this input was `Revision/metric_b4/results/metric-b4.json`). `gammas.json` holds the author's 8 real gamma matrices (16 x 16, exact entries -1, 0 and 1) and the
derived matrices `C`, `B` (complex), `Gamma`, `S^ab` and `eta`. It is committed; it is produced by the separate set
`Revision/algebra/wolfram/` (`verify_algebra.wls`), which you do NOT need to run first. No other file is
read, and nothing is downloaded.

### 2.3 Outputs (rewritten in full on every run; LF, ASCII, no time stamps, deterministic)

| file | written by | lines | bytes | sha256 of the committed (and reproduced) file |
| --- | --- | --- | --- | --- |
| `Revision/theory/reports/wolfram-field-theory.json` | `verify_field_theory.wls merge` | 98 | 46483 | `ba5baa1a2945c685d50765eab1eba675a8eed01ce258df2e25d7d81f25b5b61a` |
| `Revision/theory/field-theory.json` | `verify_field_theory.wls merge` | 69 | 31015 | `faee42f53b6ffcac5751cd9ff3e2bc7dcb805b1c61b3ec725540251fc946e21c` |
| `Revision/theory/reports/wolfram-scope.json` | `verify_scope.wls` | 27 | 9714 | `3973f59d0f6282a00a2ceea6d29d82f078b51496650b74f640f460b993eb0827` |

These are the outputs of 2026-10-16 (section 6.10; the corrected metric). The parts write
`build/theory-wolfram/<part>.json` (git-ignored, not committed; each records the sha256 of the script, the package,
`Revision/algebra/gammas.json` and `Revision/metric_warped/results/warped-metric.json`, and the merge refuses a part
file with other values). The outputs of 2026-10-15 (section 6.9; the metric with b4(x4), withdrawn):
`wolfram-field-theory.json` 96 lines, 41247 bytes, sha256 `f72453ef97ea1831ba1c6ac44dd6054bee0c953398b00ed2afd3f588336340a3`;
`field-theory.json` 69 lines, 29322 bytes, sha256 `eda8dfa2d69dbd74a6e09be063c3e7d15c406ec0a0dfa7c416c42ea09b4e544d`;
`wolfram-scope.json` 25 lines, 8802 bytes, sha256 `592920d595b366e1eef130a7b6dae4e9b1ed8a0f298e8436ae676e7119672c3c`.
The outputs of 2026-10-14 (section 6.8; the metric b4 = 1): `wolfram-field-theory.json` 95 lines,
35720 bytes, sha256 `88cd9ee66846a567b07062120c02a73f17ca73593ab657c0ae3b586457a6064d`; `field-theory.json` 68 lines,
24674 bytes, sha256 `536255e3a508bf59292f89dca6c949478e74564879039ea13c7c307c2cfc8e3b`; `wolfram-scope.json` 25 lines,
7244 bytes, sha256 `0224e5e5bbbdd7a5550f1a07865d841f5081d7d3ec3907b88150deb950afed52`. Before 2026-10-14:
`wolfram-field-theory.json` 35518 bytes, sha256 `35f33fb39ded42f510d22703ccb19a4984e372c016b3345bf620b95d0a43e57d`;
`field-theory.json` 24609 bytes, sha256 `2a3c83e5db5e0ad3572791334a4797b8af549a22295bb6800739340f2c107f54`;
`wolfram-scope.json` 7211 bytes, sha256 `ce8a923f85eb1cc7ff2c0740c4653ad9db3a65e2aa8cee3aed076dfb8e21a8ab`; the
history in this file refers to those. The value for `wolfram-scope.json` was that of the version of 2026-10-08 (section 6.7; before it: 6996 bytes,
sha256 `8a0bee2e9c0b536ed25c6dcb31272e6e0d7a49ae9e1f69a755899ce6efa021ce`). The values for the two outputs
of `verify_field_theory.wls` are those of the run of the 2026-10-08 version (section 6.7): `field-theory.json`
is unchanged from commit `a4c5eda`, and `wolfram-field-theory.json` differs from the file of `a4c5eda` (35018
bytes, sha256 `eed5e0fb01b281d58ccabe7dd84bde3b81574ae09a9c4b05e67f22f6a8065a7e`) only in the detail texts of
the two checks `charge_density_is_Krein_form_G` and `charge_density_is_Krein_form_C`.

* `wolfram-field-theory.json`: every check with its name, verdict and a sentence stating exactly what was
  verified, and the summary `{"passed": 86, "failed": 0, "total": 86}` (84 until 2026-10-15).
* `field-theory.json`: 33 exact formula records (Wolfram `InputForm` text) for the documents, from
  `christoffel_nonzero` to `quantisation`, each verified by a named check (32 until 2026-10-14; since 2026-10-15 the
  record `ricci_mixed_nonzero` replaces `ricci_mixed_diagonal`, because R^x4_x0 and R^x0_x4 are proportional to b4',
  and the record `evolution_form` is new; for the corrected metric of 2026-10-16 `ricci_mixed_nonzero` lists the
  diagonal entries only, because its Ricci tensor is diagonal).
* `wolfram-scope.json`: the 16 scope checks and the summary `{"passed": 16, "failed": 0, "total": 16}` (15 until
  2026-10-15).

## 3. How to run it (complete instructions)

### 3.1 What you need

* A computer with Windows 10 or 11, macOS, or Linux, and an internet connection for the installation,
  the activation and the download (the scripts themselves use no network).
* About 1 GB of free disk space for the repository (a fresh clone measured 690 MB including its git
  history on 2026-10-07; the repository grows over time) plus the space the Wolfram installer asks for.
* About 1 GB of free memory (the Wolfram kernel peaked at 577 MB for `verify_field_theory.wls` and at
  226 MB for `verify_scope.wls`).
* Time: `verify_scope.wls` takes about half a minute to one minute; `verify_field_theory.wls` takes about
  17 minutes on a quiet machine and up to about 45 minutes on a busy one (section 4.4). Keep the computer
  awake while it runs.
* A Wolfram kernel with WolframScript: either the free Wolfram Engine for Developers or a licensed
  Mathematica / Wolfram desktop installation. The verification used Wolfram 15.0.1 with WolframScript
  1.14.0; older versions were not tested.
* Git, to download the repository. Python, Jupyter and Rust are NOT needed for this set.

### 3.2 Open a terminal

* Windows: press the Windows key, type `PowerShell`, and open "Windows PowerShell" or "PowerShell 7". All
  Windows commands below are typed there.
* macOS: open Finder, then Applications, Utilities, Terminal.
* Linux: open your distribution's Terminal application (often Ctrl+Alt+T).

Type each command exactly as shown and press Enter after each line.

### 3.3 Install Wolfram and WolframScript

Choose ONE option.

Option A, the free Wolfram Engine for Developers:

1. In a web browser open `https://www.wolfram.com/engine/`, follow its download link, and follow the page
   to obtain the free licence. You need a Wolfram ID (an account at `https://account.wolfram.com`); read
   the licence terms yourself before you accept them.
2. Download the installer for your operating system and run it:
   * Windows: double-click the downloaded `.exe` and accept the defaults. WolframScript normally comes with
     it, in `C:\Program Files\Wolfram Research\WolframScript\` (the folder used on the verification
     machine); if the test below says "not recognized", use option C.
   * macOS: open the downloaded `.dmg` and follow its instructions (drag the application to Applications,
     and install WolframScript if the disk image offers it).
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

Test the installation (all systems; type the single quotes):

```text
wolframscript -version
wolframscript -code '$Version'
```

The first prints a line such as `WolframScript 1.14.0 for Microsoft Windows (64-bit)`; the second prints
the version of the kernel, on the verification machine
`15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. If the second asks for activation, do step 4 of
option A. (With double quotes instead of single quotes, PowerShell and the macOS/Linux shells replace
`$Version` by an empty text before WolframScript sees it.)

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

The download took 16.5 seconds on the verification machine. You are now in the repository root: the
folder that contains the folder `Revision`. Every command below is run from here. The repository stores
every file byte for byte (its file `.gitattributes` contains `* -text`), so the files are identical on
every system, whatever your Git line-ending setting is.

Optional: confirm that you have the verified versions of the three files of section 2.1. Windows
PowerShell (type the whole command on one line, including the ending `| Format-List Hash, Path`):

```powershell
Get-FileHash Revision/theory/wolfram/verify_field_theory.wls, Revision/theory/wolfram/RevisionFieldTheory.wl, Revision/theory/wolfram/verify_scope.wls | Format-List Hash, Path
```

For each file it prints two lines, `Hash : <64 hexadecimal digits, in capital letters>` and
`Path : <the full path of the file>` (a long path continues on the next line), for example
`Path : C:\Users\<your name>\Dirac_claude\Revision\theory\wolfram\verify_field_theory.wls`. Do not leave
out the ending `| Format-List Hash, Path`: without it PowerShell prints a table whose `Path` column is cut
off after about 30 characters (it ends in an ellipsis character or in `...`), so you cannot see which file
a hash belongs to; the rows of that table are in the order of the files in the command.

macOS: `shasum -a 256 Revision/theory/wolfram/verify_field_theory.wls Revision/theory/wolfram/RevisionFieldTheory.wl Revision/theory/wolfram/verify_scope.wls`;
Linux: the same with `sha256sum` instead of `shasum -a 256` (each line is the hash, two spaces, and the
file name). Compare with the table of section 2.1. If they differ, your copy is not the verified version:
if the two scripts have the hashes of commit `a4c5eda` given below the table of section 2.1, you have the
versions before the text change of 2026-10-08 (they compute the same checks; only three detail texts of
the reports differ, section 6.7); if only `verify_field_theory.wls` differs and its hash is
`dafe62233cf76106e1dc7bca51ad3aafcf62762eaf37c3af9969f0c955014c9d`, you have the version before the
output-writing fix (section 2.1; read the `OpenWrite::noopen` entry of section 3.7); otherwise the set was
changed after this record was written. The instructions still apply, but the expected output of section 4
may differ.

### 3.5 Run the scripts

**Since 2026-10-15 `verify_field_theory.wls` runs in parts** (section 6.9): instead of the single command below,
run, from the repository root and in this order, the seven commands

```text
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls base
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-G
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-C
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions-G
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls quantisation
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls merge
```

Each part ends with the line `part <name>: N/N checks passed; total time ... s` and the merge with
`merge: 84/84 checks passed`; judge a run by these lines (a syntax error can end wolframscript with exit code 0,
`claude_failures.md` G1). The parts emt-G, emt-C, solutions and solutions-G start 16 parallel subkernels (environment
variable `RFT_KERNELS`; 0 = serial). The text below describes the single command of the versions before 2026-10-15.

Run the short script first (it shows within about a minute that everything works), then the long one.
The order does not matter for the results: each script reads only `Revision/algebra/gammas.json` (and the
field script its package), never the output of the other. Run them one after the other: each uses one
Wolfram kernel, and the free Wolfram Engine licence allows only a small number of kernels at the same
time.

Windows PowerShell (forward slashes and backslashes both work):

```powershell
wolframscript -file Revision/theory/wolfram/verify_scope.wls
$LASTEXITCODE
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
$LASTEXITCODE
```

macOS and Linux:

```bash
wolframscript -file Revision/theory/wolfram/verify_scope.wls
echo "exit code: $?"
wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
echo "exit code: $?"
```

The line after each `wolframscript` command shows that command's exit code; type it immediately after the
script has finished, because it reports the most recent command. While `verify_field_theory.wls` runs, the
screen can show no new line for 10 minutes or longer (in the sections `energy-momentum tensor by vielbein
variation`, `Noether identities` and `exact solutions and conservation`); this is normal, do not stop it.

Optional, to measure the run time: in PowerShell
`Measure-Command { wolframscript -file Revision/theory/wolfram/verify_scope.wls | Out-Host }` (the output is
shown, then `TotalSeconds`; `$LASTEXITCODE` afterwards still gives the exit code), on macOS and Linux
`time wolframscript -file Revision/theory/wolfram/verify_scope.wls` (and the same for
`verify_field_theory.wls`).

### 3.6 Check the result

1. The last printed line of `verify_scope.wls` must begin with `15/15 checks passed`, the last line of
   `verify_field_theory.wls` with `84/84 checks passed`, and both exit codes must be `0`. Every other
   printed line must be one of the lines listed in section 4.1 (for `verify_scope.wls`) or section 4.2
   (for `verify_field_theory.wls`); only the numbers of seconds may differ. Compare line by line. In
   particular no line may begin with `FAIL` or with `cannot write`, and no Wolfram message may appear: a
   Wolfram message is a line of the form `Name::tag: text`, usually after an empty line, for example
   `OpenWrite::noopen: Cannot open ...`, `BinaryWrite::stream: ...`, `Close::stream: ...`,
   `Import::nffil: ...` or `Get::noopen: ...`. If any such line appears, the run is not valid even if the
   last line and the exit code look correct; read section 3.7. (The one exception is a message of
   WolframScript itself printed AFTER the verdict line, `The product exited because an error occurred.
   ...`; section 3.7 says what to do then.)
2. The summary lines of the two reports. Windows PowerShell:

   ```powershell
   Select-String -Pattern '"summary"' -Path Revision/theory/reports/wolfram-field-theory.json, Revision/theory/reports/wolfram-scope.json
   ```

   prints

   ```text
   Revision\theory\reports\wolfram-field-theory.json:8:  "summary": {"passed": 84, "failed": 0, "total": 84},
   Revision\theory\reports\wolfram-scope.json:7:  "summary": {"passed": 15, "failed": 0, "total": 15},
   ```

   macOS and Linux:

   ```bash
   grep '"summary"' Revision/theory/reports/wolfram-field-theory.json Revision/theory/reports/wolfram-scope.json
   ```

   prints the same two lines in the form
   `Revision/theory/reports/wolfram-field-theory.json:  "summary": {"passed": 84, "failed": 0, "total": 84},`.
3. The three outputs are byte-identical to the committed files. Windows PowerShell:

   ```powershell
   Get-FileHash Revision/theory/reports/wolfram-field-theory.json, Revision/theory/field-theory.json, Revision/theory/reports/wolfram-scope.json | Format-List Hash, Path
   git status --porcelain Revision/theory
   ```

   macOS: `shasum -a 256 Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json Revision/theory/reports/wolfram-scope.json`,
   Linux: the same with `sha256sum`, and on both `git status --porcelain Revision/theory`. The hashes
   must be those of the table in section 2.3. PowerShell prints them in capital letters, as pairs of lines
   `Hash : ...` and `Path : ...` (a long path continues on the next line); keep the ending
   `| Format-List Hash, Path`, because without it the `Path` column is cut off after about 30 characters
   and only the order of the rows (the order of the files in the command) tells which hash belongs to
   which file. `git status --porcelain Revision/theory` must print nothing at all (an empty answer means
   that no file under `Revision/theory` differs from the committed version).

### 3.7 What to do if it fails

* A message containing `The term 'wolframscript' is not recognized` (PowerShell; the rest of the message
  differs between versions: Windows PowerShell 5.1 prints `wolframscript : The term 'wolframscript' is not
  recognized as the name of a cmdlet, function, script file, or operable program.` and PowerShell 7 prints
  `wolframscript: The term 'wolframscript' is not recognized as a name of a cmdlet, function, script file,
  or executable program.`, both followed by further lines) or a message containing `command not found`
  (macOS and Linux: `zsh: command not found: wolframscript` in zsh, the standard shell of macOS;
  `bash: wolframscript: command not found` or `wolframscript: command not found` in bash): WolframScript
  is not installed or not on the PATH.
  Install it (section 3.3, option C) and open a NEW terminal. On Windows you can also run it by its full
  path: `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file Revision/theory/wolfram/verify_scope.wls`.
* A request to activate, or a message that the kernel is not activated or the licence is invalid, BEFORE
  any `PASS` line: run `wolframscript -activate` (section 3.3, option A, step 4).
* The message `The product exited because an error occurred. For a product older than 12.1, this can mean
  that the product is unregistered.` printed AFTER the normal output (for example after the result `2` of
  `wolframscript -code '1+1'`), with exit code 1: this was observed intermittently on 2026-10-02 while 10
  to 20 other Wolfram kernels were running (2 of 11 short `-code` tests; none of the complete `-file` runs
  of this set); on 2026-10-07 it did not occur (0 of 10 short `-code` tests at 100 percent CPU load, none
  of the 17 `-file` runs). If it appears and the line just BEFORE it is the verdict line
  `84/84 checks passed; ...` (or `15/15 checks passed; ...`), all other lines are as in section 4, and
  steps 2 and 3 of section 3.6 succeed, then the outputs are correct and the exit code 1 came from
  WolframScript after the script had ended; otherwise run the script again.
* The only output is `Failed to open file at path: Revision/theory/wolfram/verify_scope.wls` (or the same
  for `verify_field_theory.wls`): you are not in the repository root. CAUTION: WolframScript still returns
  exit code 0 in this case (observed in both verifications; the message goes to the error stream, which
  the terminal shows like any other line), so always read the last line. Go to the folder that contains
  `Revision` (`cd $HOME\Dirac_claude` in PowerShell, `cd ~/Dirac_claude` on macOS and Linux) and run
  again.
* `Import::nffil: File ...gammas.json not found during Import.` followed by many messages and `FAIL` lines:
  the input `Revision/algebra/gammas.json` is missing (an incomplete download, or the file was moved).
  Observed on 2026-10-07 with the file hidden on purpose: `verify_scope.wls` ended after 166 s with
  `4/15 checks passed` and exit code 1 AND OVERWROTE `Revision/theory/reports/wolfram-scope.json` with
  the failing verdicts (summary `{"passed": 4, "failed": 11, "total": 15}`); `verify_field_theory.wls`
  printed `RevisionFieldTheory.wl loaded`, the same `Import::nffil` message, further messages
  (`Part::partd`, `Part::partw`), `PASS  zero_test_sanity` and then `FAIL  fixture_Clifford_relation`,
  and was still running (in the section `Lagrangian, both statistics`) when it was stopped after 7
  minutes; it had written nothing, because the outputs are written only at the very end. Stop such a run
  with Ctrl+C (if the window does not react, close it). Restore the input and the outputs with
  `git checkout -- Revision/algebra/gammas.json Revision/theory/reports/wolfram-scope.json Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json`
  and run again.
* `Get::noopen: Cannot open ...RevisionFieldTheory.wl.` as the first message of `verify_field_theory.wls`
  (instead of the line `RevisionFieldTheory.wl loaded`): the package file
  `Revision/theory/wolfram/RevisionFieldTheory.wl` is missing or renamed. The script does NOT stop: it
  prints many further messages (for example `Part::partd: ...`) and `FAIL` lines, 166 lines in all (3
  `PASS`, 81 `FAIL`), ends after about 5 to 20 seconds with the last line `3/84 checks passed; total
  time <seconds> s` and exit code 1, and it OVERWRITES its two committed outputs
  `Revision/theory/reports/wolfram-field-theory.json` and `Revision/theory/field-theory.json` with these
  failing results (observed on 2026-10-02 and again on 2026-10-07: 15.7 s of wall time, summary
  `{"passed": 3, "failed": 81, "total": 84}`). Restoring only the package is therefore not enough.
  Restore the package AND the two outputs with
  `git checkout -- Revision/theory/wolfram/RevisionFieldTheory.wl Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json`,
  check that `git status --porcelain Revision/theory` prints nothing, and run the script again.
* `OpenWrite::noopen: Cannot open <path>.` followed by the line `cannot write <path>`, with NO verdict line
  (`N/84 checks passed` or `N/15 checks passed`) and exit code `2`: the script could not write the output
  file named in the message (it is read-only, open in another program, or in a folder you may not write
  to). Both scripts behave this way (observed on 2026-10-07 for both, with the output made read-only,
  section 6.4). The `PASS` lines before the message may all be there, but the run is NOT complete: the
  script stops at the first output it cannot write, so that file keeps its previous content (and when
  `Revision/theory/reports/wolfram-field-theory.json` cannot be written, `Revision/theory/field-theory.json`
  is not written either). Close any program that has the file open; make sure the file is not read-only
  (Windows PowerShell: `attrib -R <file>`; macOS and Linux: `chmod u+w <file>`) and that the folder is not
  read-only (clone into your home folder, not into a protected or synchronised folder); then run the
  script again. CAUTION for the older version of `verify_field_theory.wls` (sha256
  `dafe62233cf76106e1dc7bca51ad3aafcf62762eaf37c3af9969f0c955014c9d`, commit `c2b33cc` and earlier; section
  2.1): it does not check the writing. It prints `OpenWrite::noopen: Cannot open <path>.`,
  `BinaryWrite::stream: $Failed is not a string, SocketObject, InputStream[ ] or OutputStream[ ].` and
  `Close::stream: ...` (once per output file) and then STILL prints `84/84 checks passed; total time ...`
  and returns exit code 0, although it has NOT rewritten its outputs (observed with the complete old
  script on 2026-10-02, and its output-writing code alone on 2026-10-07, section 6.4). With that version,
  any of these messages means that the outputs were not written, whatever the last line and the exit code
  say.
* A message that no licence or no more kernels are available: another Wolfram program is using the
  allowed kernels. Close other Mathematica windows and other `wolframscript` commands and run again.
* The run was interrupted (Ctrl+C, window closed, computer asleep or switched off): the outputs are written
  only in the very last step (`writing outputs`), so an interrupted run changes no file of the repository
  (observed for every interrupted run of both verifications, sections 6.4 and 6.5). It leaves two
  WolframScript temporary files behind, outside the repository (section 5.2); they are harmless. Start the
  script again from the beginning.
* A line beginning with `FAIL`, a last line `N/84 checks passed` (or `N/15`) with N below the total, and
  exit code 1, although `gammas.json` is present: do not edit anything. Run `git status` and
  `git diff --stat` to see whether a file of the set or its input was changed; if so, restore them with
  `git checkout -- Revision/theory Revision/algebra/gammas.json` and run again. If an unmodified clone
  still fails, note the failing check names, their `detail` text in the report, and the output of
  `wolframscript -code '$Version'`, and report them: the verified result is 84 of 84 and 15 of 15 with
  Wolfram 15.0.1.
* `git status --porcelain Revision/theory` lists an output file although all checks passed: the file is
  not byte-identical to the committed one. Look at the difference with `git diff <file>`. The scripts
  write LF line endings on every system, so a program that converted line endings is the most likely
  cause; restore with the `git checkout -- ...` command of section 5.4 and run again. If the difference
  persists in a fresh clone, report it (on the verification machine every output was byte-identical).

## 4. Expected output

### 4.1 Printed on the screen by `verify_scope.wls`

16 lines: one `PASS` line per check, in this order, then the final verdict line. The numbers in brackets
are the seconds since the start and vary from run to run (also in their number of digits, for example
`[54.400000000000006 s]`); everything else is exactly as shown. Run 1 of 2026-10-07 printed:

```text
PASS  fixture_gammas  [0.2 s]
PASS  boosted_frame_reproduces_metric  [3.7 s]
PASS  boosted_frame_canonical_connection  [4.2 s]
PASS  boosted_frame_gammaOmega_formula  [4.9 s]
PASS  boosted_frame_gammaOmega_vanishes  [14.600000000000001 s]
PASS  boosted_frame_curvature_nonzero  [47.800000000000004 s]
PASS  rescaling_removes_the_connection_term  [49.400000000000006 s]
PASS  rescaled_equation_quadratic_potential  [49.400000000000006 s]
PASS  gammaOmega_blind_to_the_deflation  [49.400000000000006 s]
PASS  connection_free_lagrangian_same_equations  [51. s]
PASS  spin_connection_in_the_energy_momentum_tensor  [51.2 s]
PASS  good_sector_hermiticity_up_to_the_brane_flux  [52.6 s]
PASS  good_sector_x0_independent_modes_without_boundary_condition  [53.900000000000006 s]
PASS  extra_time_growth_rates_unbounded  [54. s]
PASS  commuting_field_energy_unbounded_below  [54.400000000000006 s]
15/15 checks passed; time 54.400000000000006 s
```

Final verdict line: `15/15 checks passed; time <seconds> s`. Exit code: `0`. Nothing is printed to the
error stream.

### 4.2 Printed on the screen by `verify_field_theory.wls`

103 lines: `RevisionFieldTheory.wl loaded`, then one `PASS` line per check (84), a line
`[<seconds> s] -> <section>` at the start of each section (15 lines; the number is the time spent in the
PREVIOUS section), two lines `   G vielbein variations: ...` and `   C vielbein variations: ...`, and the
final verdict line. The numbers vary from run to run; everything else is exactly as shown. Run 1 of
2026-10-07 printed the following (check names as of 2026-10-14; since 2026-10-14 two more lines are printed at
the start, `RevisionFieldTheory.wl loaded` and `subkernels: 16`, and the times of the three slow sections are
those of section 6.8):

```text
RevisionFieldTheory.wl loaded
PASS  zero_test_sanity
[0. s] -> fixture
PASS  fixture_Clifford_relation
PASS  fixture_C_B_S_consistent
[0. s] -> geometry
PASS  metric_is_the_authors
PASS  vielbein_inverse
PASS  sqrt_det_g_is_cos_z
PASS  degenerate_at_H_0
PASS  christoffel_count
PASS  ricci_scalar
PASS  ricci_mixed_components
PASS  never_flat_for_H_positive
[1.2000000000000002 s] -> spin connection
PASS  vielbein_postulate
PASS  omega_antisymmetric
PASS  omega_components
PASS  Omega_components
PASS  gamma_covariantly_constant
PASS  S_rotates_gamma_with_omega
PASS  spin_curvature_equals_Riemann
[2.3000000000000003 s] -> gamma^mu Omega_mu
PASS  gammaOmega_equals_3H_gamma_x0
PASS  gammaOmega_x4_terms_cancel
PASS  gammaOmega_divergence_form
[0.2 s] -> Lagrangian, both statistics
PASS  grassmann_algebra_structure
PASS  L_real_G
PASS  L_real_C
PASS  L_total_divergence_to_unsymmetrised_G
PASS  L_total_divergence_to_unsymmetrised_C
PASS  L_spin_connection_drops_out_G
PASS  L_spin_connection_drops_out_C
[5.5 s] -> Euler-Lagrange equations
PASS  EL_Psibar_G
PASS  EL_Psi_G
PASS  EL_Psibar_C
PASS  EL_Psi_C
PASS  adjoint_equation_is_Dirac_conjugate_G
PASS  adjoint_equation_is_Dirac_conjugate_C
PASS  Dirac_operator_explicit_G
PASS  Dirac_operator_explicit_C
PASS  block_form
PASS  evolution_form_G
PASS  evolution_form_C
[7.300000000000001 s] -> non-triviality
PASS  nontriviality_1_dirac16complex
PASS  nontriviality_2_dirac16complex00
PASS  Omega_vanishes_iff_a4prime_and_H_vanish
[0.7000000000000001 s] -> current and integrability
PASS  current_real_G
PASS  current_conservation_identity_G
PASS  charge_density_is_Krein_form_G
PASS  current_real_C
PASS  current_conservation_identity_C
PASS  charge_density_is_Krein_form_C
PASS  Lichnerowicz_identity_G
PASS  Lichnerowicz_identity_C
[24.700000000000003 s] -> Majorana-type Lg
PASS  Majorana_Lg_total_derivative_grassmann
PASS  Majorana_Lg_commuting_control
[2.6 s] -> energy-momentum tensor by vielbein variation
   G vielbein variations: 40.1 s
PASS  T_vielbein_variation_closed_form_G
PASS  T_symmetric_part_Belinfante_G
   C vielbein variations: 24.5 s
PASS  T_vielbein_variation_closed_form_C
PASS  T_symmetric_part_Belinfante_C
[444.5 s] -> Noether identities
PASS  Noether_identity_diffeomorphisms_G
PASS  Noether_identity_local_Lorentz_G
PASS  Noether_identity_diffeomorphisms_C
PASS  Noether_identity_local_Lorentz_C
PASS  conservation_on_shell_general
[910.8000000000001 s] -> EMT components
PASS  T_diagonal_components_G
PASS  EMT_trace_G
PASS  kinetic_sum_on_shell_G
PASS  T_diagonal_components_C
PASS  EMT_trace_C
PASS  kinetic_sum_on_shell_C
PASS  T_x4_x0_component_G
PASS  T_x4_x0_component_C
PASS  energy_exchange_equation
[72.2 s] -> exact solutions and conservation
PASS  solution_matrix_square
PASS  exact_solution_x4_x0_G
PASS  exact_solution_x4_x0_C
PASS  exact_solution_nonlinear_homogeneous_C
PASS  exact_solution_nonlinear_homogeneous_G
[1005.4000000000001 s] -> canonical quantisation
PASS  canonical_momentum
PASS  first_order_form_and_anticommutator
PASS  Heisenberg_equation_reproduces_field_equation
PASS  no_positive_inner_product
PASS  mode_hamiltonian_good_sector
PASS  mode_hamiltonian_Krein_selfadjoint
PASS  good_sector_hermiticity_curved
PASS  Krein_form_conserved_curved
PASS  Fock_space_good_sector_example
[12.600000000000001 s] -> writing outputs
84/84 checks passed; total time 2490.1000000000004 s
```

Final verdict line: `84/84 checks passed; total time <seconds> s`. Exit code: `0`. Nothing is printed to
the error stream. The second run printed the same lines with slightly different times (for example
`[915.8000000000001 s] -> EMT components` and `84/84 checks passed; total time 2508.4 s`); the printed
lines of 2026-10-02 were the same apart from the times.

### 4.3 Files written

The three files of section 2.3, each rewritten in full. After a correct run each is byte-identical to the
committed file: the sha256 values of section 2.3, and `git status --porcelain Revision/theory` prints
nothing. The summary lines are line 8 of `wolfram-field-theory.json`,
`  "summary": {"passed": 84, "failed": 0, "total": 84},`, and line 7 of `wolfram-scope.json`,
`  "summary": {"passed": 15, "failed": 0, "total": 15},`. `field-theory.json` has no summary line; it
begins with `{`, then a line beginning `  "description": "Exact formulas of the Revision field theory`, and
contains 32 records with the keys `christoffel_nonzero` ... `eta`.

### 4.4 Run time and memory on the verification machine

Since 2026-10-15 (the metric with b4, section 6.9): wall times of the parts on 2026-10-15 (24 logical processors,
16 subkernels): base 35 s, emt-G 156 s, emt-C 108 s, solutions 34 s, solutions-G 51 s, quantisation 11 s, merge
5 s; `verify_scope.wls` 29 s. The table below records the versions of 2026-10-02 and 2026-10-07 (the metric b4 = 1,
one run of the whole script).

Windows 11 Pro for Workstations, Intel Core Ultra 9 275HX (24 logical processors), 191 GB RAM. During
both verifications the machine was heavily loaded by other jobs: on 2026-10-07 the CPU load was 100
percent, 16 Wolfram processes (`wolframscript` and kernels, those of this verification included) were
running, and the field-theory runs 1 and 2 and a third field-theory run (the read-only experiment of
section 6.4) ran at the same time. On a quiet machine expect much shorter times: the document
`Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md` records 1029 s for an earlier run of
`verify_field_theory.wls` on the development machine.

| date | run | script | wall time | time printed by the script | peak memory of the kernel (working set) |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | 1 | `verify_field_theory.wls` | 2497.9 s | 2490.1 s | 577 MB |
| 2026-10-07 | 2 | `verify_field_theory.wls` | 2513.0 s | 2508.4 s | 577 MB |
| 2026-10-07 | 1 | `verify_scope.wls` | 63.9 s | 54.4 s | 226 MB |
| 2026-10-07 | 2 | `verify_scope.wls` | 69.9 s | 60.2 s | 171 MB (see below) |
| 2026-10-02 | 1 | `verify_field_theory.wls` | 1778.0 s | 1773.4 s | 578 MB |
| 2026-10-02 | 2 | `verify_field_theory.wls` | 1779.8 s | 1775.1 s | 578 MB |
| 2026-10-02 | 1 | `verify_scope.wls` | 37.9 s | 33.5 s | 227 MB |
| 2026-10-02 | 2 | `verify_scope.wls` | 39.9 s | 34.4 s | 221 MB |

The wall time includes about 5 to 10 s for starting the Wolfram kernel. In run 2 of `verify_scope.wls`
of 2026-10-07 the sampler saw two kernel processes under `wolframscript` (peaks 171 MB and 68 MB); in
all other runs it saw one. The `wolframscript` process itself used 17 MB. Further runs of
`verify_scope.wls` on 2026-10-07 (section 6.4) took 33.5 to 53.3 s of wall time. Time per section of
`verify_field_theory.wls` in run 1 of 2026-10-07: 444.5 s for `energy-momentum tensor by vielbein
variation`, 910.8 s for `Noether identities`, 72.2 s for `EMT components`, 1005.4 s for `exact solutions
and conservation`, 12.6 s for `canonical quantisation`, and 44.5 s for all other sections together.

## 5. Side effects

### 5.1 Files created or overwritten in the repository

* `verify_field_theory.wls` OVERWRITES `Revision/theory/reports/wolfram-field-theory.json` and
  `Revision/theory/field-theory.json`; `verify_scope.wls` OVERWRITES
  `Revision/theory/reports/wolfram-scope.json`. They are committed files. A correct run writes exactly the
  committed bytes, so Git sees no change.
* If the folder `Revision/theory/reports/` is missing, the scripts create it (tested for
  `verify_scope.wls`: with the folder deleted it was recreated and the report was byte-identical).
* A run in which checks fail (for example with a missing input or a missing package, section 3.7) still
  overwrites its outputs with the failing verdicts if it reaches the end. An interrupted run writes
  nothing. A run that cannot write an output file stops there with exit code 2 and leaves that file (and
  every output after it) unchanged (section 3.7).
* Nothing else is created, changed or deleted in the repository: after both scripts had run in each of the
  two fresh clones, `git status --porcelain --ignored` printed nothing (no modified, untracked or ignored
  file).

### 5.2 Outside the repository

* Processes: each `wolframscript` command starts a Wolfram kernel (on Windows the process `wolfram.exe`,
  a child of `wolframscript.exe`), which ends when the script ends. It uses one kernel of your licence.
* Temporary files: every `wolframscript -file ...` command creates TWO temporary files, each named
  `tmp_<10 letters and digits>`, in WolframScript's own folder (on Windows
  `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\`; on macOS and Linux the location was not
  examined). Observed on 2026-10-07 (section 6.4): the first file is EMPTY (0 bytes) and is created
  immediately (45 and 48 ms after the `wolframscript` process started); the second file is created a few
  seconds later, when the Wolfram kernel has started (3.8 and 4.2 s after the start), and receives every
  line the script prints (at the end its content was byte-identical to the printed output). When the
  script ends normally, WolframScript deletes BOTH files. After an interrupted run (Ctrl+C, closed window,
  killed process) BOTH stay behind: the empty one and the one with the lines printed so far. They are
  harmless and can be deleted; delete them only while no `wolframscript` command is running, because a
  running command keeps its own two files in the same folder.
* Nothing was written to the system temporary folder: for runs 1 and 2 of 2026-10-07 the variables
  `TEMP` and `TMP` pointed to two new, empty folders, and both folders were still empty after the runs.
* WolframScript rewrites its own settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` when
  it runs (observed for a `wolframscript -code` call on both dates: same content, new modification time).
  This is WolframScript's normal behaviour, not specific to this set.
* Network: none. On 2026-10-07 the TCP connections owned by `wolframscript` and by its kernel were
  sampled about every 3 to 5 s during runs 1 and 2 of both scripts: none was seen (on 2026-10-02, 404
  samples of TCP connections and UDP endpoints during the runs showed none either). A connection shorter
  than the sampling interval cannot be excluded by this method. The scripts contain no network function.
  (Activating the free Wolfram Engine needs the internet once; that is a property of the licence, not of
  these scripts.)

### 5.3 Effects on other parts of the repository

The outputs are inputs of `Revision/theory/python/check_field_theory.py` (its comparison with the Wolfram
record), of the publication tests and of the textbook notebooks listed in section 1.4. A correct run
leaves them byte-identical, so it changes nothing for them. A failed run (section 5.1) would make those
tests fail until the outputs are restored.

### 5.4 How to restore the committed state

From the repository root (all systems):

```text
git checkout -- Revision/theory/reports/wolfram-field-theory.json Revision/theory/field-theory.json Revision/theory/reports/wolfram-scope.json
git status --porcelain Revision/theory
```

The second command must then print nothing. To restore the input as well, add
`Revision/algebra/gammas.json` to the first command.

## 6. Verification record

### 6.1 What was verified, where and with what

* Dates: 2026-10-02 (first verification) and 2026-10-07 (re-verification after the verification had been
  interrupted by a session limit and restarted; every statement of the earlier record that this file keeps
  was checked again, or is marked with its date).
* Commits: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (2026-10-02) and
  `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (2026-10-07; the branch `main` of
  `https://github.com/once-ere/Dirac_claude.git` at the time). Between them only line 706 of
  `verify_field_theory.wls` changed (the fix of section 6.6, committed in `3f0a577`); the package, the
  scope script, the input and the outputs are identical in both commits. The commits that followed
  `a4c5eda` up to `af2c688` (the state of the working repository when this file was written) change no
  file of the set, its input or its outputs (other workflows changed the sympy side
  `Revision/theory/python/` in that time, which reads these outputs but is not part of this set). The files of the set were last changed in commits `3f0a577`
  (`verify_field_theory.wls`), `daeb5ba` (`verify_scope.wls`) and `2c61fb0` (the package), the input in
  `9ea68d4`, the outputs in `a9a1b70` (field theory) and `70fab64` (scope). On 2026-10-08, in a fresh
  clone at commit `97236d2fa7b61147e49e8a4d01cf4456c4acd56f` (the branch `main` at that time), the sha256
  values of the three files of section 2.1, the input of section 2.2 and the three outputs of section 2.3
  were again exactly those of the tables as they stood before the change of section 6.7 (the values of
  commit `a4c5eda`, now given below the tables). Sections 6.1 to 6.6 describe those versions; the runs of
  the 2026-10-08 versions are in section 6.7.
* Clones on 2026-10-07: two fresh clones made with `git clone https://github.com/once-ere/Dirac_claude.git`
  (runs 1 and 2) and two further fresh clones for the experiments of section 6.4. No uncommitted file was
  copied into them: the set, its input and its outputs were committed and unchanged in the working tree.
* Environment on 2026-10-07: Windows 11 Pro for Workstations 10.0.26300; Intel Core Ultra 9 275HX, 24
  logical processors, 191 GB RAM; WolframScript 1.14.0; Wolfram 15.0.1 for Microsoft Windows (64-bit)
  (July 2, 2026), Professional licence; Git 2.51.2.windows.1 with `core.autocrlf=true` in the system
  configuration (no effect: the repository's `.gitattributes` keeps every file byte for byte; all files of
  the set have LF line endings); PowerShell 7.6.6 and Windows PowerShell 5.1.26100; Git Bash. (On
  2026-10-02: the same machine with Windows 11 10.0.26200 and the same Wolfram, WolframScript and Git.)
* Commands: in each clone, from the repository root, `wolframscript -file
  Revision/theory/wolfram/verify_field_theory.wls` and then `wolframscript -file
  Revision/theory/wolfram/verify_scope.wls`, started from PowerShell 7 (`Start-Process` with the clone as
  working folder, recording wall time, exit code, the printed output and the error stream, the peak
  working set of every process in the tree below `wolframscript` and its TCP connections, about every 3
  to 5 s). Runs 1 and 2 ran at the same time, on a machine loaded by other jobs (section 4.4).

### 6.2 Results

| date | run | script | exit code | final line | checks |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | 1 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 2490.1000000000004 s` | 84 PASS, 0 FAIL |
| 2026-10-07 | 2 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 2508.4 s` | 84 PASS, 0 FAIL |
| 2026-10-07 | 1 | `verify_scope.wls` | 0 | `15/15 checks passed; time 54.400000000000006 s` | 15 PASS, 0 FAIL |
| 2026-10-07 | 2 | `verify_scope.wls` | 0 | `15/15 checks passed; time 60.2 s` | 15 PASS, 0 FAIL |
| 2026-10-02 | 1 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 1773.4 s` | 84 PASS, 0 FAIL |
| 2026-10-02 | 2 | `verify_field_theory.wls` | 0 | `84/84 checks passed; total time 1775.1000000000001 s` | 84 PASS, 0 FAIL |
| 2026-10-02 | 1 | `verify_scope.wls` | 0 | `15/15 checks passed; time 33.5 s` | 15 PASS, 0 FAIL |
| 2026-10-02 | 2 | `verify_scope.wls` | 0 | `15/15 checks passed; time 34.4 s` | 15 PASS, 0 FAIL |

The printed lines of all runs of a script are identical apart from the time values (103 lines for
`verify_field_theory.wls`, 16 for `verify_scope.wls`). Nothing was printed to the error stream.

### 6.3 Byte identity of the outputs

| output | committed sha256 | 2026-10-07 run 1 | 2026-10-07 run 2 | 2026-10-02 runs 1 and 2 |
| --- | --- | --- | --- | --- |
| `Revision/theory/reports/wolfram-field-theory.json` | `eed5e0fb01b281d58ccabe7dd84bde3b81574ae09a9c4b05e67f22f6a8065a7e` | identical | identical | identical |
| `Revision/theory/field-theory.json` | `2a3c83e5db5e0ad3572791334a4797b8af549a22295bb6800739340f2c107f54` | identical | identical | identical |
| `Revision/theory/reports/wolfram-scope.json` | `8a0bee2e9c0b536ed25c6dcb31272e6e0d7a49ae9e1f69a755899ce6efa021ce` | identical | identical | identical |

Each output was compared byte for byte (`cmp`) with the committed blob (`git show HEAD:<file>`) and between
the two runs: all identical. `git status --porcelain --ignored` printed nothing in either clone after both
scripts had run.

### 6.4 Further experiments (2026-10-07)

In a third fresh clone (commit `a4c5eda`, nothing changed); every experiment was undone with
`git checkout` and `attrib -R`, after which `git status --porcelain --ignored` printed nothing:

* `verify_scope.wls` started from a folder that is not the repository root: the error stream received
  `Failed to open file at path: Revision/theory/wolfram/verify_scope.wls`, nothing else was printed, exit
  code 0, 6.2 s.
* `verify_scope.wls` started from the folder `Revision/theory/wolfram` as `wolframscript -file
  verify_scope.wls`: 15/15, exit code 0, 47.7 s, output byte-identical (the scripts locate their files
  relative to themselves).
* The folder `Revision/theory/reports` deleted, then `verify_scope.wls` run from the root: the folder was
  recreated, 15/15, exit code 0, 41.1 s, `wolfram-scope.json` byte-identical (the other files of the
  folder were restored with `git checkout`).
* `Revision/algebra/gammas.json` hidden: `verify_scope.wls` printed `Import::nffil` and further messages,
  ended after 165.7 s with `4/15 checks passed; time 160.4 s`, exit code 1, and overwrote
  `wolfram-scope.json` (summary `{"passed": 4, "failed": 11, "total": 15}`); `verify_field_theory.wls`
  printed `RevisionFieldTheory.wl loaded`, the same message, `FAIL  fixture_Clifford_relation` and further
  `FAIL` lines, and was stopped (`taskkill /T /F`) after 421 s, still in the section `Lagrangian, both
  statistics`, without having written any output.
* `Revision/theory/wolfram/RevisionFieldTheory.wl` moved away, then `verify_field_theory.wls` run from the
  root: first `Get::noopen: Cannot open ...RevisionFieldTheory.wl.`, then `FAIL  zero_test_sanity` and
  many further messages, 166 lines (3 `PASS`: `degenerate_at_H_0`, `EL_Psibar_G`, `EL_Psi_G`; 81 `FAIL`),
  last line `3/84 checks passed; total time 8.6 s`, exit code 1, 15.7 s; it OVERWROTE
  `wolfram-field-theory.json` (summary `{"passed": 3, "failed": 81, "total": 84}`) and
  `field-theory.json`; the `git checkout` command of section 3.7 restored everything. (The same was
  observed on 2026-10-02 with both versions of the script.)
* `Revision/theory/reports/wolfram-scope.json` made read-only (`attrib +R`), then `verify_scope.wls` run:
  15 `PASS` lines, then an empty line, `OpenWrite::noopen: Cannot open
  ...\Revision\theory\wolfram\..\..\theory\reports\wolfram-scope.json.` and `cannot write
  ...\wolfram-scope.json`, NO verdict line, exit code 2, 53.3 s; the file kept its committed bytes.
* A normal run of `verify_scope.wls` (15/15, exit code 0, 40.8 s) while a `FileSystemWatcher` recorded
  WolframScript's temporary folder: `tmp_2dpknoUc6w` (0 bytes) was created 0.045 s after the start of the
  `wolframscript` process and `tmp_fHyZi6RXzR` 3.8 s after the start; the latter grew to 872 bytes, byte
  for byte the printed output; both were deleted together 40.76 s after the start, as the process ended.
  (The folder is shared with other Wolfram jobs; these two files are identified by their times and by the
  content of the second.)
* A run of `verify_scope.wls` killed after 10 s (`taskkill /T /F`, the whole process tree): it had printed
  4 `PASS` lines; exit code 1; no file of the repository changed. It left BOTH temporary files:
  `tmp_Qm4HgBEyVW`, 0 bytes, created 0.048 s after the start, and `tmp_yOuq6LmX5k`, created 4.2 s after
  the start, 209 bytes, byte for byte the run's printed output. Both were deleted by hand afterwards.

In a fourth fresh clone: `Revision/theory/reports/wolfram-field-theory.json` made read-only, then
`verify_field_theory.wls` run from the root (at the same time as runs 1 and 2): 84 `PASS` lines,
`[11.5 s] -> writing outputs`, an empty line, `OpenWrite::noopen: Cannot open
...\Revision\theory\wolfram\..\reports\wolfram-field-theory.json.` and `cannot write
...\wolfram-field-theory.json`, NO verdict line, exit code 2, 2568.3 s; both outputs kept their committed
bytes (`field-theory.json` was not written).

The output-writing code of the version before the fix (the function `writeLF` of commit `c2b33cc`), run
alone by a small script on a read-only file and followed, as in the old script, by the verdict line: it
printed `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, then the verdict line, exit code
0, and the file kept its content. (On 2026-10-02 the same was observed with the complete old script.)

The POSIX-shell forms of the check commands of section 3.6 were run in Git Bash on the verification
machine in clone 1 after its runs: `grep '"summary"' ...` printed the two summary lines, `sha256sum ...`
the hashes of section 2.3 (Git Bash marks each file name with `*`; on Linux the separator is two
spaces), and `git status --porcelain Revision/theory` printed nothing. The POSIX forms of the run
commands were run in Git Bash in the third clone: `time wolframscript -file
Revision/theory/wolfram/verify_scope.wls` (15/15, `real 0m33.498s`) and `wolframscript -file
Revision/theory/wolfram/verify_scope.wls` followed by `echo "exit code: $?"` (15/15, `exit code: 0`);
`git status --porcelain --ignored` printed nothing afterwards. None of the commands was executed on macOS
or Linux themselves. The PowerShell forms were run in PowerShell 7.6.6;
`Get-FileHash <three files>` without `| Format-List Hash, Path`, formatted at a width of 120 characters,
cut every path to 33 characters (`C:\Users\nsh\AppData\Local\Temp\` and an ellipsis character in 7.6.6,
`C:\Users\nsh\AppData\Local\Tem...` in Windows PowerShell 5.1), while `| Format-List Hash, Path` printed
the full paths, wrapped onto a second line where they were long. `wolframscript -code 'Exit[3]'`
followed by `$LASTEXITCODE` printed `3` in PowerShell 7.6.6.

### 6.5 Interrupted runs

On 2026-10-02 a first pair of runs of `verify_field_theory.wls` was stopped after less than 3 minutes (it
had been started under a tool time limit shorter than the run time) and restarted as runs 1 and 2 in the
same clones, which were still unmodified (`git status --porcelain --ignored` printed nothing before the
restart); those interrupted runs wrote no output file. On 2026-10-07 the two killed runs of section 6.4
wrote no output file either. No run of 2026-10-07 was interrupted other than these two deliberate
experiments.

### 6.6 Fixes and open discrepancies

* Fix (an execution defect, found and fixed on 2026-10-02, committed in `3f0a577`, verified again on
  2026-10-07): in `verify_field_theory.wls` the function `writeLF` ignored a failed `OpenWrite`. When an
  output file could not be written (read-only, locked, or in a folder without write permission), the old
  script printed the messages `OpenWrite::noopen`, `BinaryWrite::stream` and `Close::stream`, left the
  file unchanged, and still printed `84/84 checks passed` and exited with code 0, so a student could
  believe that the outputs had been regenerated. Diff (one line changed, line 706): before `BinaryWrite`
  the line now contains `If[s === $Failed, Print["cannot write ", path]; Exit[2]];`, the same treatment
  that `verify_scope.wls` already had (its lines 201-202). No check, tolerance, printed line of a correct
  run or output byte changed: the outputs of the fixed script are byte-identical to the committed files
  (section 6.3), and the failure case now ends with exit code 2 (section 6.4).
* No fix was made on 2026-10-07; no file of the set was changed.
* Corrections of this file on 2026-10-08 (after an independent review; no file of the set, its input or
  its outputs changed, so no script was run again): (1) section 1.4 said that `provenance/dirac
  matrices.md` lists the three files of this set; that list was removed from it in commit `389bcda`, and
  the bullet now cites what the file contains at commit `97236d2`. (2) Section 1.4 counted 18 textbook
  notebooks, the count at commit `a4c5eda` only; the bullet now gives the counts at `af2c688` (20) and at
  `97236d2` (25, measured in the fresh clone with both listing commands, which gave the same 25 notebooks
  in PowerShell 7.6.6, Windows PowerShell 5.1.26100 and Git Bash) and the commands to list the current
  set. (3) Section 3.7 quoted only the Windows PowerShell 5.1 wording of the "not recognized" error; it now
  names the common part and both wordings, measured with a nonexistent command name in Windows PowerShell
  5.1.26100 and PowerShell 7.6.6, and the "command not found" wordings of zsh 5.9 (`zsh:1: command not
  found: <name>` when run with `zsh -c`; without the `1:` in an interactive terminal) and bash 5.2.21
  (`bash: <name>: command not found`; Ubuntu's standard settings print `<name>: command not found`),
  measured on Ubuntu 24.04 under WSL; macOS itself was not tested.
* Open discrepancies: none for the versions of commit `a4c5eda` (every check passes and every output
  reproduces byte for byte) and none for the versions of 2026-10-08 (section 6.7; the field-theory
  verifier of that version was run once, not twice).
* Observations recorded for students (not defects of this set): WolframScript returns exit code 0 when it
  cannot open the script file; WolframScript occasionally printed `The product exited because an error
  occurred ...` with exit code 1 after a correct result while the machine was heavily loaded (2026-10-02
  only, section 3.7); the run time of `verify_field_theory.wls` depends strongly on the load of the
  machine (1029 s recorded earlier on the development machine, about 1775 s on 2026-10-02 and about
  2500 s on 2026-10-07 under heavy load).
* Correction of the earlier draft of this file (committed in the snapshots `3f0a577` and `cb7c01e`): it
  described the fix in section 2.1 but stated "No fix was needed" in its status line and "Fixes: none" in
  this section; this version records the fix consistently.

### 6.7 Text change and re-runs of 2026-10-08

What changed (texts and file paths only; no check, condition, verdict, tolerance or number):

* `verify_field_theory.wls` lines 18-19 and `verify_scope.wls` line 21: the repository root is wrapped in
  `ExpandFileName[...]`, so the scripts open and write paths without `..` components. These paths are
  shorter, which matters on Windows when the clone folder has a long path. The author-curvature extractor
  of `Revision/gkd_lovelock/comparison/` uses the same normalisation.
* The details of `charge_density_is_Krein_form_G` and `charge_density_is_Krein_form_C`
  (`verify_field_theory.wls` lines 305-306) and of `commuting_field_energy_unbounded_below`
  (`verify_scope.wls` lines 183-184) called the charge "the conserved charge" without qualification. They
  now say that only the local law `d_mu (Cos[z] J^mu) = 0` is proved, and that the total charge is
  constant in `x4` only if no charge flows through the boundary of the slice `x4 = const`, which at the
  brane `z = Pi/2` is an ASSUMED no-flux condition that the record does not impose. The same text change
  was made in the sympy checker `Revision/theory/python/check_scope.py` (not part of this set; its report
  `python-scope.json` differs from the committed one only in that detail, two runs byte-identical).
* New sizes and sha256 values: section 2.1. Both edited scripts parse (`SyntaxQ` True) into the same
  number of top-level expressions as the versions of commit `a4c5eda` (158 and 96).

Runs of `verify_scope.wls` (2026-10-08, in the working repository on the verification machine, not in a
fresh clone; other agents were changing other parts of the repository at the same time; from the
repository root, `wolframscript -file Revision/theory/wolfram/verify_scope.wls`, started detached through
`cmd.exe`):

| run | exit code | final line | checks |
| --- | --- | --- | --- |
| 1 | 0 | `15/15 checks passed; time 30.3 s` | 15 PASS, 0 FAIL |
| 2 | 0 | `15/15 checks passed; time 24.400000000000002 s` | 15 PASS, 0 FAIL |

The 16 printed lines of the two runs are identical apart from the time values. The two reports are
byte-identical (25 lines, 7211 bytes, sha256
`ce8a923f85eb1cc7ff2c0740c4653ad9db3a65e2aa8cee3aed076dfb8e21a8ab`). A JSON comparison with the
previously committed report (sha256 `8a0bee2e...`) finds exactly one differing value, the detail of
`commuting_field_energy_unbounded_below`; the summary, every name, every verdict and every other detail
are unchanged.

Run of `verify_field_theory.wls`: started detached on 2026-10-08 at 15:14:18 from the repository root,
followed in the same command file by `python Revision/theory/python/check_field_theory.py` (which reads
its outputs). Expected: exit code 0 with `84/84 checks passed`; `field-theory.json` unchanged (sha256
`2a3c83e5...`); `wolfram-field-theory.json` equal to the committed report with only the two detail texts
above replaced (95 lines, 35518 bytes, sha256
`35f33fb39ded42f510d22703ccb19a4984e372c016b3345bf620b95d0a43e57d`, computed by replacing the two strings in
the committed file); the sympy comparison status `agree`.

Result (recorded by the lead on 2026-10-08): `verify_field_theory.wls` printed `84/84 checks passed; total time
1783.3000000000002 s` and ended at 15:44:05 with exit code 0; `check_field_theory.py` wrote
`python-field-theory.json: 70/70 pass; comparison: agree` (293.4 s) and ended at 15:49:02 with exit code 0. The
checks of section 3.6 hold: the 103 printed lines equal those of section 4.2 apart from the seconds, with no
Wolfram message and no `FAIL` or `cannot write` line. `wolfram-field-theory.json` has 95 lines, 35518 bytes and
sha256 `35f33fb39ded42f510d22703ccb19a4984e372c016b3345bf620b95d0a43e57d`, byte-identical to the expected file;
`field-theory.json` (sha256 `2a3c83e5...`) and `python-field-theory.json` (sha256 `bb8f8db3...`) are
byte-identical to those of commit `af0fc19` (the commit before the change; `field-theory.json` is also
unchanged since `a4c5eda`, while `python-field-theory.json` was regenerated after `a4c5eda` by the snapshot
`6be66ce` of 2026-10-07, outside this set; at `a4c5eda` it had 1318 lines, 77402 bytes, sha256
`07b08bf4...`, and since `6be66ce` 1364 lines, 84769 bytes);
a JSON comparison with the report of `af0fc19` finds exactly the two changed detail texts. This is ONE run of the
2026-10-08 version, compared with an expected file; a second, independent run of this version has not been made
(the scope verifier of section 6.7 was run twice). The run was made in the working repository while other
agents edited other folders, not in a fresh clone. The check program is
`<scratchpad>/phase3c2/fix2-theory/verify_after_run.py` of the session (not part of the repository).

The read-only experiments of section 6.4 were not repeated; their recorded `OpenWrite::noopen` messages
show the paths of the versions of commit `a4c5eda`, with `..` components.

### 6.10 The corrected metric of 2026-10-16 (version 2)

* Why. The user's order of 2026-10-16: a diagonal metric is self-consistent only if every off-diagonal component of
  the sources vanishes; the metric of 2026-10-14 has off-diagonal Lovelock components E^x4_x0 ~ Cot z b4'/b4 that no
  diagonal source can match. The remedy is the corrected metric of `Revision/metric_warped/` (SPEC section 1,
  version 2), `diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3))`, with the user's
  rules of the same day: x0 is a hypothetical space-like coordinate and x4 the time, `z = 6 H x0` takes every real
  value, `Sin[z]^(1/3) = (Sin[z]^2)^(1/6)` (the positive branch). The order to recompute every primordial object
  ("go ahead with the recomputation using the corrected metric") is `HANDOFF.md` 0.10, phase W1. The files of commit
  d02ff19 (version 1 of the remedy, `g44 = -Sin[z]^(1/3)`, withdrawn) were replaced: the package and the driver were
  restored from commit 7897829 and then changed.
* Changes. `RevisionFieldTheory.wl`: the vielbein `f0 = E^-a4 b4^(1/2) Cot z` (signed), `f1..3 = E^a4`, `f4 = 1`,
  `f5..7 = E^-a4 b4^(1/2) (Sin z^2)^(1/12)`; `sqrt|g| = rftSig E^-a4 b4^2 Cot z (Sin z^2)^(1/4)` with the symbol
  `rftSig = sign(Cot z)` (`rftSig^2 = 1`, zero derivatives: constant between the degenerate points `z = n Pi/2`); the
  exact zero test for EVERY real z (Sin, Cos signed, `w = (Sin z^2)^(1/12) > 0`, reduction modulo
  `Cos^2 + Sin^2 - 1`, `w^12 - Sin^2`, `rftSig^2 - 1`; no `PowerExpand`, no `0 < z < Pi/2`). `verify_field_theory.wls`:
  the same parts; the changed statements: 21 Christoffel symbols; the Ricci tensor is diagonal and equal to the sympy
  record of `Revision/metric_warped` (input file `warped-metric.json` replaces `metric-b4.json`); the metric is flat
  for `a4 = 0, b4 = H^2 x4^2` (check `flat_member_and_curvature` replaces `never_flat_for_H_positive`, which does not
  hold for the corrected metric); 10 spin-connection components with `Omega_x0 != 0` and `Omega_x4 = 0`;
  `gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)`; the energy exchange
  `nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0)`, `h4 = b4'/(2 b4) - a4'`, and
  `nabla_mu T^mu_x0 = d0 p0 + 3 H Cot z (p0 - p_t)` (x0-independent entries need `p0 = p_t`); `T^x4_x0 =
  -(1/4)(B40 - f0 B04)`; the exact solutions: the reduced system `chi' = (-V gamma^(x4) + muA K) chi`,
  `muA = (3/2) H (4 al + 1) E^a4 b4^(-1/2)`, has closed forms only for `m = 0` (any `al`, check
  `exact_solution_x4_x0_m0_*`) and for `al = -1/4` (any `m`, `exact_solution_x4_x0_quarter_*`); the commuting nonlinear
  solutions for every `m` (substitution of the system, as before); the Grassmann nonlinear solution in closed form for
  `m = 0` only (scope stated in the check); the quantisation with the new measure (`d_x4 sqrt g = (2 b4'/b4 - a4')
  sqrt g`). `verify_scope.wls`: its own exact zero test for every real z (new check `zero_test_controls`); the boosted
  frame removes the `gamma^(x0)` part for a rapidity with `b' = 3 H E^a4 b4^(-1/2)` and never the part
  `b4'/b4 - a4'/2`; the rescaling `Psi = E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) chi`; `gamma^mu Omega_mu` contains `a4`
  (check `gammaOmega_sees_the_hidden_block` replaces `gammaOmega_blind_to_the_deflation`); the spin connection
  reaches the energy-momentum tensor through `K^x4_x5`, not `K^x4_x1`.
* Negative controls (scratch copies, not committed): a wrong scalar factor and a wrong `muA` make all seven solution
  checks fail; the Hermiticity identity without the `(3/2) H` term fails.
* Retired: the supplements of 2026-10-14 (`verify_field_theory_b4.wls`, `verify_field_theory_b4_emt.wls`,
  `Revision/theory/python/check_field_theory_b4.py`) and their outputs (`field-theory-b4.json`,
  `wolfram-field-theory-b4.json`, `wolfram-field-theory-b4-emt-C.json`, `wolfram-field-theory-b4-emt-G.json`,
  `python-field-theory-b4.json`) are removed from the repository and from the gate: they verified the withdrawn metric,
  and their statements for the corrected metric are part of this set and of its sympy twin.
* Runs (2026-10-16, development machine, Windows 11, 24 threads, Wolfram 14.3; each part under `timeout -k 5 423`,
  i.e. below the limit of 7 min 3 s for one calculation). First run: base 14 s, emt-C 57 s, emt-G 177 s, solutions
  39 s, solutions-G 17 s, quantisation 5 s, merge "86/86 checks passed", exit code 0 each; `verify_scope.wls` "16/16
  checks passed", 2 s. Second run of every part, the merge and the scope script (concurrently with the sympy twin):
  base 14 s, emt-C 57 s, emt-G 179 s, solutions 36 s, solutions-G 17 s, quantisation 5 s, merge 86/86, scope 16/16,
  exit code 0 each. The three outputs of the second run are byte-identical to those of the first (the sha256 of
  section 2.3). The sympy twin (`Revision/theory/python/`): `check_field_theory.py --part nonlinear` (PASS, 32 s),
  `check_field_theory.py` (72 of 72 PASS, comparison with this set: agree, 161 s and 148 s) and `check_scope.py` (15 of
  15 PASS, 2 s), run twice with byte-identical outputs (`python-field-theory.json` sha256
  `ba2eb78b29a1f63b6e486c3c02700383efb703984645fe4b72c84c17b452682d`, `python-scope.json` sha256
  `6779027163006c2f6d93850f9fc886b146b2fcdccf18409692d0777730b0edc6`).

### 6.9 Everything for the metric with b4(x4) (2026-10-15)

* Why. The user's orders of 2026-10-15: "b4 is a function of x4; b4 is NEVER 1" and "yes, move everything to b4(x4);
  b4 is never 1" (`HANDOFF.md` 0.9). Until then this set proved its statements for the withdrawn metric b4 = 1, and the
  supplements `verify_field_theory_b4.wls` and `verify_field_theory_b4_emt.wls` of 2026-10-14
  (`Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`) re-checked part of them for general b4.
* Changes. `RevisionFieldTheory.wl`: the metric with b4 (`rftF` with E^-a4 Sqrt[b4[x4]] Sin^(1/6) for x5, x6, x7,
  `rftMetricAuthor`, `rftAssumptions` with b4[x4] > 0, `rftSqrtG0 = b4^(3/2) Cos[z]`); every function is unchanged.
  `verify_field_theory.wls`: rewritten in parts (argument base, emt-G, emt-C, solutions, solutions-G, quantisation,
  merge); every statement for general a4 and b4. The changed statements: sqrt|g| = b4^(3/2) Cos z (check renamed
  `sqrt_det_g`); the Ricci tensor with its off-diagonal components R^x4_x0 = (3/2) H Cot z b4'/b4 and
  R^x0_x4 = -(3/2) H Tan z b4'/b4 and R = 6 (a4'^2 - 7 H^2) - 3 a4' b4'/b4 + 3 b4''/b4, compared also with
  `Revision/metric_b4/results/metric-b4.json`; the spin connection of the extra times with a4' - b4'/(2 b4); gamma^mu
  Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) (checks renamed `gammaOmega_total` and
  `gammaOmega_per_direction`: the b4' terms of the three extra times add, they do not cancel); the Dirac operator,
  the block form and the evolution form with the term -(3/4)(b4'/b4) Psi; non-triviality with the square
  (9 H^2 - (9/16)(b4'/b4)^2) I16 of the gravity term; `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`; the charge
  and the Lichnerowicz identity with the new measure and R; the energy exchange with -(3/2)(b4'/b4)(rho + p_t); the
  exact solutions with the factor b4^(-3/4) (the linear family in closed form; the commuting nonlinear solutions for
  EVERY solution of the reduced system, by substituting the system for the derivatives of 16 general functions; the
  Grassmann nonlinear solution with the three integrals I0, Ic, Is of b4^(-3/2)); the quantisation with
  sqrt|g| = b4^(3/2) Cos z and the anti-Hermitian term -i (3/4)(b4'/b4) of the mode operator, which compensates the x4
  dependence of the measure (`good_sector_hermiticity_curved`, `Krein_form_conserved_curved`). `verify_scope.wls`: the
  same metric; the boosted frame gives gamma'^mu Omega'_mu = ((6 H - beta)/2)(Cosh b gamma^(x0) - Sinh b gamma^(x4)) +
  (3/4)(b4'/b4)(Cosh b gamma^(x4) - Sinh b gamma^(x0)), for any rapidity function Cosh b c4 + Sinh b c0 = (3/4) b4'/b4,
  so no boost in the (x4, x0) plane removes the b4' part (check renamed `boosted_frame_removes_only_the_H_term`); the
  rescaling Psi = b4^(-3/4) Sin^(-1/2) chi; the Ricci components; the brane flux with the measure b4^(3/2) Cos z.
* The Grassmann nonlinear solution. Its first version evaluated the energy-momentum tensor in the explicit Grassmann
  algebra with the integrals; the part `solutions` was stopped by the limit of 423 s (`claude_failures.md` G2).
  The part `solutions-G` reduces every statement exactly to 16 x 16 matrix identities (header comment of the part);
  the field equation, S = b4^(-3/2) S0 and the contraction of the kinetic tensor are also checked directly in the
  explicit algebra with 16 generic complex constants per generator. It takes 51 s.
* Runs (2026-10-15, working tree on top of commit `58d6d78`, Windows 11, Wolfram 15.0.1, 24 logical processors), each
  under `timeout 423`: base 53 of 53 (35 s), emt-G 8 of 8 (156 s), emt-C 8 of 8 (108 s), solutions 4 of 4 (34 s),
  solutions-G 1 of 1 (51 s), quantisation 9 of 9 (11 s), merge 84 of 84 (5 s), every exit code 0; `verify_scope.wls`
  15 of 15 (29 s). The independent sympy twins (`Revision/theory/python`, also for general b4, in two runs since
  2026-10-15): `check_field_theory.py --part nonlinear` 209 s, `check_field_theory.py` 72 of 72 (128 s) with the
  comparison `agree` (33 of 33 formula records, 65 of 65 check pairs), `check_scope.py` 14 of 14.
* The supplements of 2026-10-14 (`verify_field_theory_b4.wls`, `verify_field_theory_b4_emt.wls`,
  `check_field_theory_b4.py`) are unchanged; their statements are now part of this set. They stay in the record, and
  in the gate, until the textbook no longer reads their outputs (`HANDOFF.md` 0.9, phase 9).

### 6.8 The author's coordinates x0..x7 and parallel subkernels (2026-10-14)

* Why. (1) On 2026-10-14 the user ordered that their coordinates X = {x0, x1, ..., x7} be used throughout (x0 = the
  hidden direction, listed first; `Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[48]); the Revision record had named them
  x1..x8 with the hidden direction x8 listed last. (2) The same day the user ruled that no single calculation may take
  longer than 7 min 3 s; the full `verify_field_theory.wls` took 1783 to 2508 s serially (section 4.4), its three slow
  sections 444.5 s, 910.8 s and 1005.4 s each.
* Changes. `RevisionFieldTheory.wl`: coordinates `rftX = {x0, ..., x7}`, `rftZ = 6 H x0`, `rftEta = diag(1,1,1,1,-1,-1,-1,-1)`,
  the vielbein factors `rftF = {Cot[z], E^a4 Sin^(1/6) (x3), 1, E^-a4 Sin^(1/6) (x3)}`, the metric and the trigonometric rules
  in `x0`. `verify_field_theory.wls`: every position of the old order replaced by the position of the same coordinate
  (x0 = Wolfram position 1, xk = position k + 1): `g[[8]]` -> `g[[1]]` (hidden), `g[[4]]` -> `g[[5]]` (time), the lists of
  space and extra-time positions, the expected Ricci diagonal, the spin-connection list (with a < b; the components
  omega_(xi),(x0)(xi) = -omega_(xi),(xi)(x0) are now listed with their sign), the energy-exchange identity with
  `p0[x4, x0]`, the exact-solution matrix `M = -m g[[5]] + mu g[[5]].g[[1]]`, the mode Hamiltonian, the curved
  Hermiticity check, the Fock example, every text. Parallel evaluation: `$DistributedContexts = None`, 16 subkernels
  (environment variable `RFT_KERNELS`; 0 = serial as before) each load the same package and fixture; in the sections
  `energy-momentum tensor by vielbein variation`, `Noether identities`, `EMT components` and `exact solutions and
  conservation` every test expression is built on the main kernel exactly as before and only its zero test
  (`sZeroQ`, `zeroQK`, the same functions) runs on a subkernel (`pS`, `pZeroQ`). No check, test expression or verdict
  changed. `verify_scope.wls`: the same relabelling (frame boost in the (x4, x0) plane, `F'_x1x0`, `M0`, `k0..k7`,
  `y0..y7`, the classical-energy example with `(k0, k1, k2, k3) = (4, 1, 2, 0)`).
* Runs (2026-10-14, working tree on top of commit `cae873a`, Windows 11, Wolfram 15.0.1, 24 logical processors):
  `verify_field_theory.wls` 84 of 84, exit code 0, `total time 299.8 s`, wall time 309 s; section times 58.3 s
  (energy-momentum tensor), 87.7 s (Noether identities), 10.3 s (EMT components), 113.1 s (exact solutions and
  conservation). `verify_scope.wls` 15 of 15, 14.9 s. The independent sympy twins: `check_field_theory.py` 70 of 70 with
  the comparison `agree` (32 of 32 formula records, 63 of 63 check pairs), `check_scope.py` 14 of 14.
* Same physics. A comparison of the new `field-theory.json` with the one of commit `bf555a9` (exact, in WolframScript,
  after renaming x8 -> x0 and p8 -> p0 and mapping the old position q to the new one: 8 -> 1, k -> k + 1): the 25
  Christoffel symbols, the Ricci diagonal and scalar, the 12 spin-connection components (with the sign of the swapped
  pairs), gamma^mu Omega_mu per direction and in total, the 16 component field equations, the chiral blocks, the energy
  exchange identity (all three entries), the metric, the vielbein, sqrt|det g| and eta are identical; the 19 prose
  records differ only in the relabelling. Both reports have the same checks with the same verdicts in the same order
  (five check names renamed, listed above).
* Wording, later on 2026-10-14: two comments of `RevisionFieldTheory.wl` and one of `verify_scope.wls` said "his
  order"; they now say "the author's order" (no gendered pronoun for the author). Only comments changed; no output of
  this set depends on them (the reports do not record these sha256). New sha256: `RevisionFieldTheory.wl`
  `313e617d6df3cad7f1d389d9d85681af176e655f0a103a015bdb5b99c4c4e88f`, `verify_scope.wls`
  `f47348cab9eb8e2fb77b1089ff003eaf29a8427ff8d923ddb67b37fc5b86dbcb` (tables of section 2).
