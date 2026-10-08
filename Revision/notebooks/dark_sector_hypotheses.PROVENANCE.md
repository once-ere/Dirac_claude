# Provenance of the Revision notebook `dark_sector_hypotheses.ipynb`

The dark-sector hypotheses of dirac16complex and dirac16complex00 against the Unite values.

* Notebook: `Revision/notebooks/dark_sector_hypotheses.ipynb` (47 cells: 26 markdown, 21 code; 455344 bytes;
  sha256 `fadca750e38b16dcfa3f7687e52f8e0882639d09f49267c2429df722c86e8429`).
* Builder: `Revision/notebooks/src/dark_sector_hypotheses.py`
  (sha256 `1d89e3c5e8b9e50308f44e7e42a06ee0f54bd21eb517b455d89f5b6941e8f4bd`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.1.

Honesty labels used by the notebook (binding: `Revision/SPEC.md` sections 8 and 11, `Revision/README.md`):
the history a4 = A H x4 is a PRESCRIBED background (test field, no back-reaction); the observer
normalisation (A, B, C for dirac16complex; N1, N2 for dirac16complex00) is an ASSUMPTION; a4_today, the gas
fractions, the condensate value lambda S/m = -382/441 and every parameter of the dirac16complex00 models M2 to
M5 are CHOSEN (by construction, NOT predictions; M4 and M5 are solved so that they reproduce the Unite tangent
or fit); the M5 component of negative classical energy is labelled ghost-like; neither Hypothesis nor
Hypothesis00 is established. The extra times x5, x6, x7 deflate exponentially (scale factor e^{-a4} sin^{1/6} z)
at every slice; no static or frozen extra times are used.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into the build folder `<cargo-target>` (section 2) and requires zero
   compiler warnings.
2. Runs `revision_ks_solver single --m 1 --lambda 0.01946 --a4 0.0 --N 8 --out <output>/ks_runs/N8_lamp1_a000.json`
   (the arguments of `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`, working folder the
   repository) and prints the solver's three input checks (`theory_input_coefficients`,
   `gamma_fixture_numeric`, `block_reduction_numeric`) and the parameter block of its result; checks H, m, L,
   dk, v_t, tip angle, T = 0 and the numerics tag against `Revision/kohn_sham/results/parameters.json`, and the
   41 slices against `reports/ks-history-run.json`.
3. Solves the remaining 122 states of three series of the dense history (N688_lam0, N136_lam0, N8_lamp1 with
   lambda_1 = 0.01946; a4 = 0, 0.05, ..., 2) with up to eight parallel solver processes; every run exits 0
   with the final line SUCCESS and only the three PASS input checks on its error stream.
4. Rebuilds each row exactly as `run_ks_history.py` writes it (shortest round-trip floats, occupied-set
   fingerprint) and requires the text to equal the committed row of
   `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv`: 123 of 123 identical. Repeats the run
   report's checks for these series: occupied set fixed at all 41 slices (12, 6 and 2 occupied levels),
   hidden-direction conservation residual 2.225e-09 (<= 1e-6), particle number to 1.652e-15.
5. Recomputes, with the functions `deriv`, `interp` and `cpl_fit` copied from `compute/compute_eos.py`,
   X = P3 - Pt, w_eff(A) = w_eff(B) = X/E, w_eff(C) = X/E - 1, w3, wt, w8 and the derivatives d w_eff/d a4,
   d w3/d a4: 123 of 123 rows equal `outputs/eos-history.csv` character for character; conservation
   dE/da4 = -3X to 1.235e-07 (finite differences) and 1.903e-08 (Simpson); d(X/E)/da4 two ways to 6.251e-07.
   Checks that the gas (N = 688, 136) has X/E in [0.292906, 0.326398], rising toward 1/3, and that the
   N = 8, +lambda_1 zero modes have constant E = -0.000986842619 and P3 = Pt.
6. Recomputes the complete entries of the three series in `outputs/eos-summary.json` (ranges, d ln E/d a4,
   sign of E, CPL tangents at a4_today = 0.5, 1, 1.5, 2, least-squares fits over [1/2, 1] and [1/3, 1],
   conservation deviations): all three equal. Gas tangent wa in [-0.017750, -0.009049], fitted wa in
   [-0.026480, -0.019604] (thawing sign, far below the Unite 0.60).
7. Condensate with exact fractions: u = lambda S/m = -382/441 gives u/(2 + u) = -191/250 = -0.764 (CHOSEN, by
   construction); the phantom window -2 < u < -1 on 384 exact grid values; w_eff(A, B) = 0, w_eff(C) = -1.
   Closed formulas of `outputs/effective-formulas.json` with exact dual numbers (Fraction parts): the flat
   massive mode tangent x/(3(x + 1)), 2x/(3(x + 1)^2); radiation + condensate r0/(3(r0 + 1)),
   r0/(3(r0^2 + 2 r0 + 1)) with r0 = 417/583 giving w_eff(C) = -861/1000 exactly; the observer formulas.
8. Mixtures (gas N688_lam0 + condensate, today a4 = 2): the twelve mixtures, the gas fraction 0.436703 for
   w_eff(C) = -0.861 today (wa = +0.067014, freezing), the gas fraction 0.680715 for a constant-w fit of -0.764
   (CPL fit (-0.784092, +0.060277)), and the ratio-definition scan over 322404 mixtures (smallest wa 0 near
   w0 = -0.861; distance to the Unite pair at least 0.600001): all equal `outputs/eos-summary.json`.
9. Hypothesis00 (`Revision/dark_sector/dirac16complex00/eos-theory.json`), exact: N2 tangents M2
   (-861/1000, 81037/500000), M3 (-861/1000, -196963/500000), M4 (-861/1000, -3/5) = the Unite pair by
   construction; the M4 parameters s = 264037/403037, Omega_q = 57963/264037 re-derived from the two tangent
   conditions; the M5 crossing of w = -1 bracketed in exact arithmetic between a = 0.77909966357 and
   0.77909966377 (recorded 0.77909966367) with R > 0.3203, caused by its ghost-like component (positive
   components never cross); the Unite line crosses -1 at a = 461/600; the four models re-evaluated in floating
   point at a = 1/3, 1/2, 3/4, 1 agree with the recorded `w_at` values to 4.64e-12.
10. Reads the six committed dark-sector reports and asserts their counts exactly as their JSON files give them:
    `dirac16complex/reports/derivation-checks.json` 30/30, `ks-history-run.json` 5/5, `eos-checks.json` 13/13,
    `independent-checks.json` 9/9, `dirac16complex00/reports/python-derive-eos.json` 49/49,
    `python-independent-numerics.json` 28/28 (0 failed in each; every listed check with verdict PASS).
11. Draws four figures: w_eff under A = B and under C along the history for the three series with the Unite
    reference lines; w_eff(C) of gas + condensate mixtures against a = e^{a4 - 2} with the Unite CPL line;
    the dirac16complex00 populations M2 to M5 under N2 (with the Unite CPL line and the M5 crossing) and N1;
    all candidates in the (w0, wa) plane with the Unite pair.
12. Ends with "what this notebook showed, and what it did not show".

The notebook prints 40 PASS lines of its own (and the solver's three input checks, indented) and no FAIL
line; its last code cell prints `checks of this notebook: 40 passed, 0 failed`.

## 2. Files read and written

Read (sha256 at the time of the verified builds):

| file | sha256 |
| --- | --- |
| `Revision/SPEC.md` | (only its existence is used, to find the repository) |
| `Revision/kohn_sham/solver/Cargo.toml` | `464d553adcfaa1943af53ec3b18324fcba99ee92b3d82efcb08d2dc74bca24b1` |
| `Revision/kohn_sham/solver/Cargo.lock` | `65b7ed2cbe76d4701a66287cfbdedc8d4a780ee3c9e672de0e4055eb4ae70738` |
| `Revision/kohn_sham/solver/src/analysis.rs` | `200b0c4640f5b02262518dab568fd2c77c0fe33ca72e9ab3a687fb8284ad8bcb` |
| `Revision/kohn_sham/solver/src/json.rs` | `919be3b192ab81d62deb8429229aa065a50d8fd0f8df6877ac4e413909efdf05` |
| `Revision/kohn_sham/solver/src/main.rs` | `6964c47f87c224d323a443471137c2ffa57b9c6d79e926cd14ddcc6e54efa18c` |
| `Revision/kohn_sham/solver/src/mermin.rs` | `0be57b4defb8ec056b521c7585138f67d68fb95e3446b8a020b60312cbf6a094` |
| `Revision/kohn_sham/solver/src/model.rs` | `391ac28244bc07ff246a8f4dcdd2fae74ff3571268187791e0ad8a88e7b486eb` |
| `Revision/kohn_sham/solver/src/report.rs` | `0a770aff24dde0de531d0578e968ab9cad3d5f42b7cda532f7c753633b7ff9c7` |
| `Revision/kohn_sham/solver/src/runs.rs` | `254d5fd638e9f619caab663472d34b7567951cbe1a64168156c2c9a4232d6446` |
| `Revision/kohn_sham/solver/src/scf.rs` | `0c624e4bf2a413a8e7be1ad7cb1f77342eda8360c657074a9e47e02b412b4e8d` |
| `Revision/kohn_sham/solver/src/sha256.rs` | `f44ed328e324b26d9b7c78f530e95be9ff1c88b179026ab4839ab38009e15122` |
| `Revision/kohn_sham/solver/src/shoot.rs` | `39c95fffea255d3977efa9ddadf87131e51c4fd47557bec3a6225fa05bf7d7f4` |
| `Revision/kohn_sham/solver/src/spectrum.rs` | `b52b6997e1418f094e1e7a5cca6064235b6d5ded6bcb534cce149e3a0d3622de` |
| `Revision/kohn_sham/solver/src/theory.rs` | `392d2fdd01cc9661451bc8d5f42561348c124ad9927fe0770a59b979c196c407` |
| `Revision/kohn_sham/ks-theory.json` (read by the solver) | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` |
| `Revision/algebra/gammas.json` (read by the solver) | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` |
| `Revision/kohn_sham/results/parameters.json` | `f35216c2bee5b0dc21db6343e640c89f0aebcefab0c6dd6efcec618e0bfae993` |
| `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` | `8a6afadf714a95c6e0e1dc1cf1e4bec2832e96385eef9db7565e5b9155d9685e` |
| `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` | `1acdf7574ef4d6e1661cb01dc3519f10b721f976a80908ba5b74698f4c93d278` |
| `Revision/dark_sector/dirac16complex/outputs/eos-summary.json` | `f3fa5775e31dd1b7801fe9d0995e0937a027b51a8b4a2e49dabb6964952a861a` |
| `Revision/dark_sector/dirac16complex/outputs/effective-formulas.json` | `88727cb7cb7162630f8e72d1c64afe5de1e5058a9d26801cc060aa0b76d70477` |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | `8127b0b148c1b6d5ac9f6cc66b3094e7f9b82da35e96ed1330fe8109f9e1a744` |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | `8a02a4e35981bdf34389207c24bb4710d6e9c396871981cfe7e6cee8c04d4f71` |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | `bd887ed06014f6a2114a47f7726dab6d9f0e7907c03838dede5893ec7ecf7639` |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | `129825058b03c2b698aadd43583e48564d9e34614e4b63c4444ce61658819ea6` |
| `Revision/dark_sector/dirac16complex00/eos-theory.json` | `6f2efb9889dd76b42b552458c63cda2a63158ee65f38d3471f37f49405152872` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `3b317106dfc268ee77afca696f1cff0d50e8e6b5f9360d1d764b73e329356022` |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | `ce3114a3e7e25d32d5bbca4e9ad5f6c6c087e41c70264dbf8d23a7e50c912f0c` |

Followed but not executed (the notebook reproduces their arithmetic; listed so that a change is noticed):
`Revision/dark_sector/dirac16complex/compute/run_ks_history.py` (sha256
`54feefb5e5f9c6317fc2bf8d2499f6f069db10d76887b3eb8d5ac0c2ef4edb9d`) and
`Revision/dark_sector/dirac16complex/compute/compute_eos.py` (sha256
`3bfc7301a0a77c3ed4031da3a908e3f351adac9111633994d973e02d86e632d5`).

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/dark_sector_hypotheses` in the repository, ignored by
git), identical in both verified builds and in the `check` run (129 files compared); the Rust build into
`<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-dark_sector_hypotheses-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/ks-history-dense-subset.csv` (header + the 123 reproduced rows of `ks-history-dense.csv`) | 28791 | `288265b470b968444dac96720b943f319a5a77eddc28088fe35cc7f455ac58b2` |
| `<output>/eos-history-subset.csv` (header + the 123 reproduced rows of `eos-history.csv`) | 37220 | `5c785a99674059b47f79524a49137f5f080e78763052f1ab945f9fc0e710090a` |
| `<output>/figures/figure1_w_eff_histories.png` | 60531 | `3dd746f892c0382b743ea36b5c7a5432dc49666eff32be4f4e2fc380f44a27fb` |
| `<output>/figures/figure2_mixtures.png` | 65481 | `b796eaa803b89a6c8ef074a13396a0476366893bc3474e6a04eaf66315aa3d05` |
| `<output>/figures/figure3_dirac16complex00_populations.png` | 79878 | `0d393d8b03382d2fd582be2d39f147824f9a2ffdf17c4171ed8ee296af6c243a` |
| `<output>/figures/figure4_w0_wa_plane.png` | 39932 | `55d56eac83e106647012ae3a1f952852cc26d5a684328bdfb48d2b382cbcfc0d` |
| `<output>/ks_runs/<id>.json` (123 solver result files, ids `N688_lam0_a000` ... `N8_lamp1_a200`) | 4873129 in total | combined `e0fa4f369f35112aee435cf721eeaeddeb72b4f3b52556d57b629c7951e718e8` (sha256 of the 123 lines `<sha256>  <file name>`, sorted by file name, LF) |
| `<cargo-target>/` | about 2.8 MB | the Rust build folder (compiler output; not compared) |

The tool writes `Revision/notebooks/dark_sector_hypotheses.ipynb` (`build`) or
`<output>/dark_sector_hypotheses.ipynb` (`check`). The notebook has no long mode.

## 3. How to run it

The complete, self-contained instructions for Windows 11 (PowerShell), macOS on Apple silicon (zsh)
and Linux (bash) are section 2 of the notebook: install Git, Python 3.12 or newer and Rust (rustup);
`git clone https://github.com/once-ere/Dirac_claude.git`; create a private environment OUTSIDE the
repository (`python -m venv $HOME\venvs\revision-nb` on Windows, `python3 -m venv ~/venvs/revision-nb`
on macOS and Linux); install the pins with `<environment python> -m pip install -r
Revision/notebooks/requirements.txt`; then either

```text
<environment python> -m jupyterlab Revision/notebooks/dark_sector_hypotheses.ipynb
```

(choose the kernel "Python 3 (ipykernel)", press Shift+Enter cell by cell or Run All Cells), or
headless

```text
<environment python> -m nbconvert --to notebook --execute Revision/notebooks/dark_sector_hypotheses.ipynb --output-dir ../revision-nb-runs
```

or, to rebuild and compare with the committed file (from the repository root):

```text
<environment python> Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses --out <new folder>
<environment python> Revision/notebooks/tools/build_notebooks.py check dark_sector_hypotheses --out <new folder>
```

`python -m jupyter ...` is not used: it fails where the jupyter executables are not on PATH.

## 4. Expected output

* Section 5: the Unite values (-0.764; (-0.861, -0.6)), `exit status: 0`, `compiler warnings: 0`.
* Section 6: the command `$ revision_ks_solver single --m 1 --lambda 0.01946 --a4 0.0 --N 8 --out
  <output>/ks_runs/N8_lamp1_a000.json`, the solver's three indented `PASS` input checks, `-> SUCCESS, exit
  status 0`, the parameter block (H 1.0, m 1.0, L 3.0, dk 0.25, v_t 1.0, a4 0.0, lambda 0.01946, N 8.0, T 0.0,
  tipTheta 0.0, exactFockVariant False), lambda_1 = 0.01946, 0.0009298, 0.0001846 for N = 8, 136, 688.
* Section 7: `all_runs_succeeded: 123 runs`, `dense_rows_bit_identical: 123 of 123 rows`, three
  `..._occupations_fixed` lines, the table of E, P3, Pt, P8 (for example N688_lam0 at a4 = 0: E =
  6.804412466e+02, P3 = 1.993052338e+02, P8 = 2.405597506e+02).
* Section 8: `eos_rows_identical: 123 of 123 rows`; the w table (N688_lam0: X/E = 0.292906 at a4 = 0 and
  0.318294 at a4 = 2; w_eff(C) = -0.707094 and -0.681706; w8 = 0.353535 and 0.648248).
* Section 9: three `..._summary_equals_record` lines and the tangent and fit tables (N688_lam0, today a4 = 2:
  tangent (-0.681706, -0.017750), fit over [1/2, 1] (-0.681157, -0.024238), constant w -0.687217).
* Sections 10 and 11: `u = lambda S/m = -382/441 | ratio u/(2 + u) = -191/250 = -0.764`; the dual-number
  checks; the mixture lines with 0.436703 / +0.067014 and 0.680715 / (-0.784092, +0.060277); the scan line
  (distance 0.600001).
* Section 12: the table of exact tangents (M2 81037/500000, M3 -196963/500000, M4 -3/5), the M5 bracket
  line, `unite_line_crossing: ... a = 461/600 = 0.768333`, `models_w_at_equal_record: ... 4.64e-12`.
* Section 13: the table of the six reports (30 / 5 / 13 / 9 / 49 / 28 checks, 0 failed).
* Section 14: four figures and `checks of this notebook: 40 passed, 0 failed`; the list of the written files.

No run time and no path of the computer is printed (paths are shown relative to the repository or as
`<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11, 2026-10-08)

* Whole notebook, executed by `build_notebooks.py`: 32.7 s (build A), 42.6 s (build B) and 44.0 s (`check`)
  of execution while other work ran on the computer (the first builds of this notebook took 15.4 s to
  15.9 s), including the fresh `cargo build --release` of the solver into `<cargo-target>`
  and the 123 solver runs (8 parallel processes; measured separately with the same arguments: 9.3 s of wall
  time for the 123 runs, the longest single run 2.4 s).
* Not part of the notebook: the committed dense history (615 states, `run_ks_history.py`) took about 2 min,
  the independent free-gas implementation about 2.5 min (`Revision/dark_sector/dirac16complex/README.md`).

## 6. Side effects

* Writes only into `<output>` and `<cargo-target>` (and the tool writes the notebook file named in section 2). The committed
  records `Revision/dark_sector/`, `Revision/kohn_sham/results/` and `Revision/kohn_sham/reports/` are only
  read; the notebook raises an error if `<output>` or `<cargo-target>` would place its files there. The
  crate's own `target/` folder is not used (the build goes to `<cargo-target>`).
* By default `<cargo-target>` is a new folder of about 2.8 MB in the system's temporary folder for
  every new `<output>` (every `build` and `check` of the tool uses a new `<output>`); nothing deletes
  it, it can be deleted by hand. It is placed there, short and outside the repository, because on
  Windows the MSVC linker `link.exe` cannot open a file whose path is longer than 259 characters
  (MAX_PATH; section 7).
* Runs `cargo` (needs the Rust toolchain on PATH) and the built solver (up to eight processes at a time,
  working folder the repository, which the solver only reads); no network access during the run, no
  Wolfram Language, no installation.

## 7. Verification record

* 2026-10-08, the reason for the current version: on Windows the MSVC linker `link.exe` cannot open
  a file whose path is longer than 259 characters (MAX_PATH). With the former build folder
  `<output>/cargo-target` and the default `<output>` of the tool
  (`build/revision_notebooks/dark_sector_hypotheses-XXXXXXXX/`), the solver program
  `cargo-target/release/deps/revision_ks_solver.exe` that the linker writes lies 106 characters
  below the repository folder, so `check` failed with `LNK1104` for a repository folder longer than
  153 characters. Measured: with this folder layout below a repository folder of 200 characters,
  `cargo build --release` of the solver fails with `LNK1104` on the 306-character path of the
  program (the limit of 153 characters is computed from the 106 characters below the repository
  folder; the reviewer's clone of 153 characters passed). In a copy of the needed files below a
  folder of 170 characters, `check dark_sector_hypotheses` without `--out` (as the gate step
  notebooks-check runs it) failed with `LNK1104` with the previous builder and notebook (those of the
  last commit before this change) and passed with the current ones (byte-identical, 455344 bytes,
  47.8 s). A review had found the same failure for the notebook
  `lovelock_gkd` (above 148 characters); all three notebooks were changed in the same way. Since then
  the build goes to `<cargo-target>` (sections 2 and 6); the results and the figures are unchanged.
* All runs below with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch folder of
  154 characters.
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses --out
  <scratch>/dark_sector_hypotheses_A` - executed in 32.7 s, wrote 455344 bytes, audit PASS, sha256
  `fadca750e38b16dcfa3f7687e52f8e0882639d09f49267c2429df722c86e8429`.
* 2026-10-08, build B: the same command with `--out <scratch>/dark_sector_hypotheses_B` - executed in
  42.6 s; the notebook written is byte-identical to build A (same sha256), and the 129 files of the two
  output folders are byte-identical and equal to the table of section 2.
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check dark_sector_hypotheses --out
  <scratch>/dark_sector_hypotheses_check1` - a third independent execution (44.0 s): `check
  dark_sector_hypotheses: PASS - the re-executed notebook is byte-identical to
  Revision/notebooks/dark_sector_hypotheses.ipynb (455344 bytes)`; its 129 files equal the table of
  section 2.
* 2026-10-08, headless instruction of section 2.5: `python -m nbconvert --to notebook --execute
  Revision/notebooks/dark_sector_hypotheses.ipynb --output-dir <scratch>` with
  `REVISION_NB_OUT=<scratch>/out` - exit status 0, no error output and no stderr output in the executed
  notebook, `checks of this notebook: 40 passed, 0 failed`, no FAIL line (nbconvert's own file is not
  normalised, so it is not compared byte for byte).
* Before these builds, every comparison was prototyped in scratch scripts against the committed record with
  a separately built solver (123 of 123 dense rows and 123 of 123 equation-of-state rows identical, the three
  eos-summary entries, the mixtures and the exact dirac16complex00 fractions equal).
* 2026-10-08, tests: `python -m unittest Revision/tests/test_revision_notebooks.py -v` - 9 static tests OK, 2 skipped; with
  `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 109.1 s (the installed versions equal the pins; `check` of all three notebooks in
  temporary folders is byte-identical).
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
