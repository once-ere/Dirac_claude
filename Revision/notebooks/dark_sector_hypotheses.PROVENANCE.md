# Provenance of the Revision notebook `dark_sector_hypotheses.ipynb`

The dark-sector hypotheses of dirac16complex and dirac16complex00 against the Unite values, for the
author's metric with b4(x4) (the user's metric of 2026-10-14; b4 is a function of x4, never 1).

* Notebook: `Revision/notebooks/dark_sector_hypotheses.ipynb` (47 cells: 26 markdown, 21 code; 472097 bytes;
  sha256 `ddee8168475df239cc0eade3fa5f50c933a344bb8b5c97f0d00227cc1460c2c8`).
* Builder: `Revision/notebooks/src/dark_sector_hypotheses.py`
  (sha256 `7f37406281a456ced16caff8abf76ca883e3e687cf1598b4f20d4a7bdbcae2e7`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified for the metric with b4(x4) on 2026-10-15 (section 7; earlier versions with the
  withdrawn b4 = 1 on 2026-10-08 and 2026-10-14), Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.1.

Honesty labels used by the notebook (binding: `Revision/SPEC.md` sections 8 and 11, `Revision/README.md`):
the history a4 = H x4, b4(x4) = b4(0) e^((4/3) H x4) (beta = d ln b4/d a4 = 4/3, the branch of the author's
weights for a source without T^x4_x0) is a PRESCRIBED background (test field, no back-reaction); the observer
normalisation (A, B, C for dirac16complex; N1, N2 for dirac16complex00) is an ASSUMPTION; a4_today, the gas
fractions, the condensate value lambda S/m = -382/441 and every parameter of the dirac16complex00 models M2 to
M5 are CHOSEN (by construction, NOT predictions; they were solved on the withdrawn b4 = 1 record to reproduce
the Unite tangent or fit and are kept unchanged); the M5 component of negative classical energy is labelled
ghost-like; neither Hypothesis nor Hypothesis00 is established. The extra times x5, x6, x7 deflate
exponentially (scale factor e^{-a4} b4^{1/2} sin^{1/6} z, ~ e^{-a4/3} on the history) at every slice; no static
or frozen extra times are used.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into the build folder `<cargo-target>` (section 2) and requires zero
   compiler warnings.
2. Runs `revision_ks_solver single --m 1 --lambda 0.01946 --a4 0.0 --N 8 --out <output>/ks_runs/N8_lamp1_a000.json`
   (the arguments of `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`: the coupling is
   lambda_eff = lambda_hat e^(-2 a4), equal to lambda_hat at a4 = 0; working folder the repository) and prints
   the solver's three input checks (`theory_input_coefficients`, `gamma_fixture_numeric`,
   `block_reduction_numeric`) and the parameter block of its result; checks H, m, L, dk, v_t, tip angle, T = 0
   and the numerics tag against `Revision/kohn_sham/results/parameters.json`, the 41 slices against
   `reports/ks-history-run.json`, and that the run report states the history with b4(x4), beta = 4/3 and the
   coupling rule, which the notebook's `lambda_eff` reproduces at all 41 slices.
3. Solves the remaining 122 states of three series of the dense history (N688_lam0, N136_lam0, N8_lamp1 with
   lambda_hat = lambda_1 = 0.01946; a4 = 0, 0.05, ..., 2; N8_lamp1 at lambda_eff = 0.01946 e^(-2 a4)) with up to
   eight parallel solver processes; every run exits 0 with the final line SUCCESS and only the three PASS input
   checks on its error stream.
4. Rebuilds each row exactly as `run_ks_history.py` writes it (with the columns b4_over_b4_0 = e^((4/3) a4)
   and lambda_eff; shortest round-trip floats, occupied-set fingerprint) and requires the text to equal the
   committed row of `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv`: 123 of 123 identical.
   Repeats the run report's checks for these series: occupied set fixed at all 41 slices (12, 6 and 2
   occupied levels), hidden-direction conservation residual 2.225e-09 (<= 1e-6), particle number to 1.998e-15.
5. Recomputes, with the functions `deriv`, `interp` and `cpl_fit` copied from `compute/compute_eos.py`,
   X = P3 - Pt, w_eff(A) = w_eff(B) = X/E + (beta/2) Pt/E, w_eff(C) = X/E - 1 + (beta/2)(Pt/E + 1), w3, wt, wx0
   and the derivatives d w_eff/d a4, d w3/d a4: 123 of 123 rows equal `outputs/eos-history.csv` character for
   character; conservation with the b4 term dE/da4 = -3X - 2Pt to 2.460e-06 (finite differences; the stencil's
   truncation error on the N = 8 series is about 6.7e-06) and 3.585e-07 (Simpson); the b4-free law
   dE/da4 = -3X of the withdrawn record misses the N = 8 series by 1.630 (of max|E|); d w_eff(A)/da4 two ways
   to 6.251e-07 (gas) and 3.150e-05 (N = 8, end slices). Checks that the gas (N = 688, 136; lambda = 0, Pt = 0)
   has w_eff(A) = X/E in [0.292906, 0.326398], rising toward 1/3, and w_eff(C) = w_eff(A) - 1/3 in
   [-0.040427, -0.006935]; and that the N = 8, +lambda_1 zero modes have X = 0, E < 0 with E(2)/E(0) = 0.018402
   (e^(-4) = 0.018316) and w_eff(A) = (2/3) Pt/E in [0.660463, 0.666665].
6. Recomputes the complete entries of the three series in `outputs/eos-summary.json` (ranges, d ln E/d a4,
   sign of E, CPL tangents at a4_today = 0.5, 1, 1.5, 2, least-squares fits over [1/2, 1] and [1/3, 1],
   conservation deviations): all three equal. Gas tangent wa in [-0.017750, -0.009049], fitted wa in
   [-0.026480, -0.019604] (thawing sign, far below the Unite 0.60).
7. Condensate with exact fractions: u = lambda S/m = -382/441 gives u/(2 + u) = -191/250 = -0.764 at one
   instant (CHOSEN, by construction); with b4(x4), u ~ e^(-2 a4) and the ratio drifts with
   wa = 4u/(2 + u)^2 = -84231/31250; w_eff(C) = -1/3 + (2/3) w_c = -316/375 with wa = -28077/15625; the phantom
   window -2 < u < -1 on 384 exact grid values, in which the observer also reads w_eff(C) < -1 (the drift carries
   u = -382/441 into it toward the past, from a = sqrt(382/441) = 0.9307 to a = sqrt(191/441) = 0.6581). Closed formulas of `outputs/effective-formulas.json` with exact
   dual numbers (Fraction parts): the flat massive mode tangent x/(3(x + 1)), 2x/(3(x + 1)^2); radiation +
   lambda = 0 condensate r0/(3(r0 + 1)), r0/(3(r0^2 + 2 r0 + 1)), whose C value w0 - 1/3 cannot reach -0.861
   (it would need r0/(3(1 + r0)) = -1583/3000); the observer formulas with beta.
8. Mixtures (gas N688_lam0 + condensate, today a4 = 2): the twelve mixtures with a lambda = 0 condensate equal
   `outputs/eos-summary.json`, and under C w_eff(C) >= -0.333015 >= -1/3 over 1000 gas fractions; the scans with
   a drifting condensate (ratio, A_B, C; 400 ratios x 201 gas fractions x 4 todays) equal `mixture_scan`: the
   closest point to the Unite pair is under C at distance 0.2910614215438 ((-0.58, -0.6758666666667), the pure
   condensate with w_c = -0.37 today), and every mixture with w0 within 0.1 of -0.861 has wa between
   -2.639515126434 and -1.41320438962 under C.
9. Hypothesis00 (`Revision/dark_sector/dirac16complex00/eos-theory.json`), exact on the history b4 ~ a^(4/3):
   N2 tangents M2 (-583/3000, 81037/500000; freezing), M3 (-287/1000, -196963/4500000), M4 with the parameters
   of the withdrawn tuning (-287/1000, -1/15): no longer the Unite pair; positive components bounded by -1/3
   (turning points a_* = s^(-3/2): M3 6.264, M4 1.886, M5 2.337); the Unite w0 needs a ghost fraction
   G >= 1583/1000 (total energy zero at a = 1583/2583); M5 (G = 3/10) has no crossing of -1 on [1/3, 1]
   (minimum -0.797841); the Unite line crosses -1 at a = 461/600; the four models re-evaluated in floating
   point at a = 1/3, 1/2, 3/4, 1 agree with the recorded `w_at` values to 4.90e-13; the source the author's
   equations require on the history, kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27), satisfies the
   conservation law with b4 and p3 + p_t = 2 p0 exactly.
10. Reads the seven committed dark-sector reports and asserts their counts exactly as their JSON files give
    them: `dirac16complex/reports/derivation-checks.json` 39/39, `ks-history-run.json` 7/7,
    `eos-checks.json` 15/15, `independent-checks.json` 10/10, `dirac16complex00/reports/python-derive-eos.json`
    49/49, `python-independent-numerics.json` 32/32, `Revision/dark_sector/reports/wolfram-dark-sector-b4.json`
    8/8 (0 failed in each; every listed check with verdict PASS).
11. Draws four figures: w_eff under A = B and under C along the history for the three series with the Unite
    reference lines; w_eff(C) of gas + lambda = 0 condensate mixtures and of the drifting condensate against
    a = e^{a4 - 2} with the Unite CPL line; the dirac16complex00 populations M2 to M5 under N2 (with the Unite
    CPL line and the bound -1/3) and N1; all candidates in the (w0, wa) plane with the Unite pair.
12. Ends with "what this notebook showed, and what it did not show".

The notebook prints 46 PASS lines of its own (and the solver's three input checks, indented) and no FAIL
line; its last code cell prints `checks of this notebook: 46 passed, 0 failed`.

## 2. Files read and written

Read (sha256 at the time of the verified builds of 2026-10-15):

| file | sha256 |
| --- | --- |
| `Revision/SPEC.md` | (only its existence is used, to find the repository) |
| `Revision/kohn_sham/solver/Cargo.toml` | `464d553adcfaa1943af53ec3b18324fcba99ee92b3d82efcb08d2dc74bca24b1` |
| `Revision/kohn_sham/solver/Cargo.lock` | `65b7ed2cbe76d4701a66287cfbdedc8d4a780ee3c9e672de0e4055eb4ae70738` |
| `Revision/kohn_sham/solver/src/analysis.rs` | `43d69cb108e37b58beca76b613b6d5c80d5a4456884a6b4cbebbe76da598a487` |
| `Revision/kohn_sham/solver/src/json.rs` | `919be3b192ab81d62deb8429229aa065a50d8fd0f8df6877ac4e413909efdf05` |
| `Revision/kohn_sham/solver/src/main.rs` | `6964c47f87c224d323a443471137c2ffa57b9c6d79e926cd14ddcc6e54efa18c` |
| `Revision/kohn_sham/solver/src/mermin.rs` | `0be57b4defb8ec056b521c7585138f67d68fb95e3446b8a020b60312cbf6a094` |
| `Revision/kohn_sham/solver/src/model.rs` | `391ac28244bc07ff246a8f4dcdd2fae74ff3571268187791e0ad8a88e7b486eb` |
| `Revision/kohn_sham/solver/src/report.rs` | `0a770aff24dde0de531d0578e968ab9cad3d5f42b7cda532f7c753633b7ff9c7` |
| `Revision/kohn_sham/solver/src/runs.rs` | `5e944987088de64b10559d42474569ca18cb188aae13bae0d7a474a17df19f55` |
| `Revision/kohn_sham/solver/src/scf.rs` | `d27060a8db753b8a933946d35eb3918ba3f982b201263435b448a6c702254dd7` |
| `Revision/kohn_sham/solver/src/sha256.rs` | `f44ed328e324b26d9b7c78f530e95be9ff1c88b179026ab4839ab38009e15122` |
| `Revision/kohn_sham/solver/src/shoot.rs` | `39c95fffea255d3977efa9ddadf87131e51c4fd47557bec3a6225fa05bf7d7f4` |
| `Revision/kohn_sham/solver/src/spectrum.rs` | `b52b6997e1418f094e1e7a5cca6064235b6d5ded6bcb534cce149e3a0d3622de` |
| `Revision/kohn_sham/solver/src/theory.rs` | `cfde16d6fa442f797ac0e5684227e192394bc4aa75f3d89f78ea00d05965bbb4` |
| `Revision/kohn_sham/ks-theory.json` (read by the solver) | `a40cc2e2fa67039b87a30e5835acab57834f8cb83af8bbdc80f726237d128fd2` |
| `Revision/algebra/gammas.json` (read by the solver) | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/kohn_sham/results/parameters.json` | `c91041b68b6520c7eec890bd18ffd361b260730c0ee4328eb1d90a8f91c83ebb` |
| `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` | `5eee937e5d2626a77ffa5d04abe1fd6440a8a475653202340da5f86c96a92642` |
| `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` | `1ab8d52364fa8ede9ba6ff0459a9dabfea882fdff43d34f58d06a858695eb4f2` |
| `Revision/dark_sector/dirac16complex/outputs/eos-summary.json` | `ee2ad6074ac7fe45d3c1bce0e6c9c9de51d18267208a0fb54ababef480d9e66c` |
| `Revision/dark_sector/dirac16complex/outputs/effective-formulas.json` | `aa15a8198973517ea0c206b12377afa0f29246ea4c19503dd28c37f5785a8c2c` |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | `67427eaa3e496e4e07adde7bf560b932b68a35a40e54e83b2d8c00e5d054a1a1` |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | `873aa221ea313cf1be4425e3b1558ffb44b7f7e71a1a1f931b0f7ea0b075c9f0` |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | `b0dce83a31874eb2c77fc790ec2f425544e56256249c1631378a41327fc05059` |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | `bb475ad3f21db751bc002a6589d2a87af6b21fe29c5c04cb116f2238eb728232` |
| `Revision/dark_sector/dirac16complex00/eos-theory.json` | `7ab0fcbd8bd4fdc39be91b8fa39ff76c83715e7bdd08b8326eb9809249ecd2ac` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `0ed88e5a872621e0054651a43a5d5588c0ea7b4d9e33920653839837ea73e784` |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | `e620b2c0bf97f06ef081078bee1b26a84798b0acdc8979f3f5838d6ccb22e40a` |
| `Revision/dark_sector/reports/wolfram-dark-sector-b4.json` | `273e91939ba39dd8baa8b6f687e1e0110d927a1ec6de2250e90217032e3734f1` |

Followed but not executed (the notebook reproduces their arithmetic; listed so that a change is noticed):
`Revision/dark_sector/dirac16complex/compute/run_ks_history.py` (sha256
`469a21c70115ca9e6f5f78dfd03733612c2ecf03f6cc07b6c604e23428f99d0e`) and
`Revision/dark_sector/dirac16complex/compute/compute_eos.py` (sha256
`1bc9d9e2110e5365ddbbe1d042d2abffb76875eebc0e41abfac11c23625ed5b1`).

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/dark_sector_hypotheses` in the repository, ignored by
git), identical in both verified builds and in the `check` run (129 files compared); the Rust build into
`<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-dark_sector_hypotheses-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/ks-history-dense-subset.csv` (header + the 123 reproduced rows of `ks-history-dense.csv`) | 32204 | `550fa4d29ae7833353933be471d5c06c802f4c96db711efb6fe7003ae835ea7d` |
| `<output>/eos-history-subset.csv` (header + the 123 reproduced rows of `eos-history.csv`) | 37104 | `7c35cb6163ea86ad1c3dbef146713b8ee5200007eb850d523684796c3edfadf3` |
| `<output>/figures/figure1_w_eff_histories.png` | 68781 | `3c75b7bb710d24756dff7fddba2840b81d316c9f75f9b63ee3f30bb85ceb02f8` |
| `<output>/figures/figure2_mixtures.png` | 60227 | `e2ec39477b1eab5f6617daf5f4ad2016ba3bc43f52efef3a42aa84ed1a26103e` |
| `<output>/figures/figure3_dirac16complex00_populations.png` | 67182 | `8a6d3f54dafcc79638efb859a22552090455419d20ab8f1dac1725ef78054029` |
| `<output>/figures/figure4_w0_wa_plane.png` | 46861 | `e0c2a2751b8b885f6a08cb4813d206c47071560da90b106c7d04f91fc7726c1b` |
| `<output>/ks_runs/<id>.json` (123 solver result files, ids `N688_lam0_a000` ... `N8_lamp1_a200`) | 4873152 in total | combined `0a5af5bebdc46ce5845c0b4ef6594fab432630229d134af60ff84b992d33ce11` (sha256 of the 123 lines `<sha256>  <file name>`, sorted by file name, LF) |
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
  tipTheta 0.0, exactFockVariant False), `history_with_b4_equals_record`, lambda_hat = lambda_1 = 0.01946,
  0.0009298, 0.0001846 for N = 8, 136, 688, and the run report's history and coupling texts.
* Section 7: `all_runs_succeeded: 123 runs`, `dense_rows_bit_identical: 123 of 123 rows`, three
  `..._occupations_fixed` lines, the table of b4/b4(0), lambda_eff, E, P3, Pt, P0 (for example N688_lam0 at
  a4 = 0: E = 6.804412466e+02, P3 = 1.993052338e+02, P0 = 2.405597506e+02; N8_lamp1 at a4 = 2: b4/b4(0) =
  14.391916, lambda_eff = 3.564223e-04, E = -1.816014714e-05).
* Section 8: `eos_rows_identical: 123 of 123 rows`, `conservation_with_b4_term`,
  `conservation_without_b4_term_fails`; the w table (N688_lam0: w_eff(A) = X/E = 0.292906 at a4 = 0 and
  0.318294 at a4 = 2; w_eff(C) = -0.040427 and -0.015039; wx0 = 0.353535 and 0.648248; N8_lamp1: w_eff(A) =
  0.660463 and 0.666665).
* Section 9: three `..._summary_equals_record` lines and the tangent and fit tables (N688_lam0, today a4 = 2,
  under C: tangent (-0.015039, -0.017750), fit over [1/2, 1] (-0.014490, -0.024238), constant w -0.020550).
* Sections 10 and 11: `u = lambda S/m = -382/441 | ratio u/(2 + u) = -191/250 = -0.764 | wa = 4u/(2 + u)^2 =
  -84231/31250 = -2.695392`; the dual-number checks; `mixture_C_cannot_reach_unite_w0` (-0.333015); the scan
  line (C: (-0.58, -0.6758666666667), distance 0.2910614215438).
* Section 12: the table of exact tangents (M2 -583/3000, 81037/500000; M3 -287/1000, -196963/4500000; M4
  -287/1000, -1/15), `unite_w0_requires_dominant_ghost` (1583/1000, 1583/2583), the turning points 6.264,
  1.886, 2.337, `M5_no_crossing` (-0.797841), `unite_line_crossing: ... a = 461/600 = 0.768333`,
  `models_w_at_equal_record: ... 4.90e-13`, `branch_required_source`.
* Section 13: the table of the seven reports (39 / 7 / 15 / 10 / 49 / 32 / 8 checks, 0 failed).
* Section 14: four figures and `checks of this notebook: 46 passed, 0 failed`; the list of the written files.

No run time and no path of the computer is printed (paths are shown relative to the repository or as
`<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11)

* 2026-10-15 (the metric with b4(x4)): 15.1 s and 12.9 s (`build`), 12.8 s (`check`), then 13.5 s and 13.5 s
  (builds A and B) and 13.1 s (`check`) of execution, including the fresh `cargo build --release` of the
  solver into `<cargo-target>` and the 123 solver runs (8 parallel processes).
* Earlier versions (b4 = 1, withdrawn): 13.4 s to 47.8 s of execution depending on the load (section 7).
* Not part of the notebook: the committed dense history (615 states, `run_ks_history.py`) takes about 25 s,
  the independent free-gas implementation about 1.3 min (`Revision/dark_sector/dirac16complex/README.md`).

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
* On macOS and Linux the default `<cargo-target>` is created readable and writable only by the current
  user (mode 0700), and the notebook raises an error if a folder of that name already exists and is a
  symbolic link, belongs to another user or can be written by group or others: its name is predictable,
  a shared temporary folder such as `/tmp` can be written by every user, and the notebook runs the
  program built there. On Windows the temporary folder (`%TEMP%`) belongs to the user, and the folder is
  used as it is. A folder named by `REVISION_NB_CARGO_TARGET` is used as given (choose one of your own).
  The exact code of this check was exercised under WSL Ubuntu 24.04 with Python 3.12.3 (section 7); the
  notebook itself was executed only on Windows 11.
* The list of written files at the end of the notebook leaves out `<cargo-target>` and also a folder
  `<output>/cargo-target` that an earlier version of this notebook (which built there) left in a reused
  `<output>`.
* Runs `cargo` (needs the Rust toolchain on PATH) and the built solver (up to eight processes at a time,
  working folder the repository, which the solver only reads); no network access during the run, no
  Wolfram Language, no installation.

## 7. Verification record

* 2026-10-15, later the same day: the record's scan with a drifting condensate now also records the LARGEST
  wa among the mixtures with w0 within 0.1 of the Unite w0 (`compute_eos.py`, key
  `max_wa_with_w0_within_0p1_of_unite`; the check `mixture_scan_three_definitions_b4` requires it below -1).
  The document had read the recorded smallest wa as a bound ("only with wa <= -2.64"), which it is not: the
  range under C is [-2.639515126434, -1.41320438962]. The notebook's scan computes the same key and its check
  `mixture_scan_equals_record` prints the ranges. `build --out <scratch>/buildD` (13.2 s) wrote 472097 bytes,
  sha256 `ddee8168475df239cc0eade3fa5f50c933a344bb8b5c97f0d00227cc1460c2c8`; `check --out <scratch>/check3`:
  PASS, byte-identical; the 129 output files equal those of build A.
* 2026-10-15, later the same day: a text correction. With b4(x4) the observer's w_eff(C) = -1/3 + (2/3) w_c of a
  condensate is below -1 while its drifting ratio lies in the phantom window, so the detail of the check
  `condensate_phantom_window` no longer calls the phantom ratio an 8-dimensional ratio "at one instant", and
  sections 1 and 15 say "no model M2 to M5" where they said "no model". The record's producer `derive_eos.py`
  was corrected the same way (only the text `ghost` of `eos-theory.json` changed, new sha256 in section 2; every
  number is unchanged). `build_notebooks.py build dark_sector_hypotheses --out <scratch>/buildC` (13.1 s) wrote
  471489 bytes, sha256 `49194dbca88dd728aa791e93bf9bca93a453164b1c290dedad75e841b54c36eb`; `check --out
  <scratch>/check2`: PASS, byte-identical; the 129 output files of both runs equal those of build A (section 2).
* 2026-10-15, the reason for the current version: the user's metric with b4(x4) (b4 is a function of x4,
  never 1). The whole dark-sector record was recomputed on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)
  (commits e9d1751 to 65d954c), and this notebook was rewritten to reproduce it: the solver runs at
  lambda_eff = lambda_hat e^(-2 a4) (`run_one`, as `run_ks_history.py`); the dense rows carry b4/b4(0) and
  lambda_eff; the equation of state, the conservation law and the derivative identity carry the beta terms
  (as `compute_eos.py`); the condensate drifts; the mixture scans have the drifting condensate in three
  definitions; Hypothesis00 has the exact tangents on the b4 history, the bound -1/3, the ghost fraction
  1583/1000, no crossing of -1 and the required branch source; section 13 reads seven reports (the Wolfram
  verification added). Sections 1, 3, 4 (now 4.1 to 4.6), 5.2, 6, 7.2, 7.3 and 8 to 15 changed; sections 2 and
  5.1 and the run instructions are unchanged. 46 checks of the notebook (was 40).
* 2026-10-15, all runs with `timeout 423`: `python Revision/notebooks/tools/build_notebooks.py build
  dark_sector_hypotheses` - executed in 15.1 s, audit PASS (first version of the figures; the legend of
  figure 1, the condensate pole of figure 2 and two labels of figures 3 and 4 were then moved), then again in
  12.9 s and `check` in 12.8 s - PASS, byte-identical (470855 bytes). With TMP, TEMP and TMPDIR set to a
  scratch folder: build A `--out <scratch>/buildA` (13.5 s) and build B `--out <scratch>/buildB` (13.5 s)
  wrote the same notebook, sha256 `15e0bf953b2662e1d83bc98d4abc0d961851f86a54e6ee1466b93d1e37cfe1ab`;
  `check dark_sector_hypotheses --out <scratch>/check1` (13.1 s): `PASS - the re-executed notebook is
  byte-identical to Revision/notebooks/dark_sector_hypotheses.ipynb (470855 bytes)`; the 129 files of the
  three output folders are byte-identical and equal to the table of section 2. The four figures were looked at.
* Earlier versions (with the withdrawn b4 = 1), kept as the record of their verification:
* 2026-10-08, the reason for that version (reviews of the previous version): (1) the final list
  of written files left out only `<cargo-target>`, so a folder `<output>/cargo-target` left in a reused
  `<output>` by an earlier version was listed file by file; it is now left out as well. (2) On Linux
  the default `<cargo-target>` lies in the shared `/tmp` under a predictable name, and the notebook
  runs the solver built there; on macOS and Linux the folder is now created private and an existing
  folder that is not private is refused (section 6). (3) The markdown of section 12.1 said that M2, M3
  and M4 never cross -1 at any a; it now says that the bound w >= -1 holds for M3 and M4 only before the
  turning point a_* of their extra-time mode (M3 1.8434, M4 1.2355; for M4 checked on a in [1/300, 1]),
  as `Revision/docs/DARK_SECTOR_HYPOTHESES.md` does. (4) The run-time sentence of section 2.4 now gives
  about 15 s to 50 s instead of about 15 s. In the notebook only the sources of cell 1 (section 2),
  cell 5 (the folder set-up), cell 32 (section 12.1) and cell 45 (the final list) changed; every output
  is identical to the previous version. Three inputs of section 2 have new sha256 values because their
  producers were re-run with qualified check texts only (`derivation-checks.json`: detail of
  `phantom_condition`; `eos-theory.json` and `python-derive-eos.json`: the M3/M4 turning-point, charge-conservation and
  Einstein linear-member wording); every count and number the notebook reads from them is unchanged.
* 2026-10-08, the private-folder check: the exact code of the builder, run under WSL Ubuntu 24.04 with
  Python 3.12.3 (scratch script), created a new folder with mode 0700, accepted an existing own folder
  of mode 0755, refused folders of mode 0777 and 0775, a symbolic link and a folder of another user
  (`/usr`), and was skipped with `REVISION_NB_CARGO_TARGET` set (21 of 21 cases as expected for the three
  builders). The notebook itself was not executed on Linux.
* Current version, all runs with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch
  folder:
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses --out
  <scratch>/buildA` - executed in 23.0 s, wrote 457652 bytes, audit PASS, sha256
  `30d2e843921159fa285901db19796585d0434204b8b7bbb03eb6ec9b15574f25`.
* 2026-10-08, build B: the same command with `--out <scratch>/buildB` - executed in 24.3 s; the notebook
  written is byte-identical to build A (same sha256), and the 129 files of the two output folders are
  byte-identical and equal to the table of section 2.
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check dark_sector_hypotheses --out
  <scratch>/check1` - a third independent execution (25.8 s): `check dark_sector_hypotheses: PASS - the
  re-executed notebook is byte-identical to Revision/notebooks/dark_sector_hypotheses.ipynb (457652 bytes)`;
  its 129 files equal the table of section 2.
* 2026-10-08, after the re-run of `derive_eos.py` committed in the snapshot `95525a6` (15:41; then
  `eos-theory.json` sha256 `d8e5c02e...` and `python-derive-eos.json` `1c3d233d...`; text fields only):
  `check dark_sector_hypotheses --out <scratch>/check2` - PASS, byte-identical (457652 bytes, 31.2 s); its
  129 files are byte-identical to those of `check1`.
* 2026-10-08, after the re-runs of `derive_effective.py` and `derive_eos.py` with corrected texts committed
  in the snapshot `f3d347e` (15:57; new sha256 of `derivation-checks.json` `4188953d...` and of
  `eos-theory.json` `e7586528...` in section 2; a JSON comparison with the previous commit finds one
  changed text field in each file, nothing else: `derivation-checks.json`, the detail of `phantom_condition`;
  `eos-theory.json`, `condensate/einstein`): `check dark_sector_hypotheses --out <scratch>/nbcheck`,
  with TMP, TEMP and TMPDIR set to a scratch folder - PASS, `the re-executed notebook is byte-identical to
  Revision/notebooks/dark_sector_hypotheses.ipynb (457652 bytes)`, executed in 39.6 s (43 s wall time); its
  129 files equal the table of section 2 (the six files by sha256 and size, the 123 solver files by the
  combined sha256 and 4873129 bytes in total).
* 2026-10-08, two intermediate versions of this change were each built twice and checked the same way
  (byte-identical; 457610 bytes in 38.8 s, 40.3 s, 32.6 s and 457641 bytes in 24.6 s, 26.5 s, 24.4 s of
  execution; the same 129 files); they differ from the current notebook only in the heading of section
  12.1 and, the first of them, in the run-time sentence of section 2.4.
* 2026-10-08, reused output folder with an old-layout build folder: `python -m nbconvert --to notebook
  --execute Revision/notebooks/dark_sector_hypotheses.ipynb --output-dir <scratch>` with
  `REVISION_NB_OUT=<scratch>/out`, where `<scratch>/out/cargo-target/release/deps/old.rlib` and
  `<scratch>/out/cargo-target/release/old.d` existed beforehand (the reviewer's reproduction), run with the
  second intermediate notebook (sha256 `6f419044a7d84137cfc6bf4fe4cfe5ff89cd80e99a0dfd49db127ddb01614f9f`,
  identical code cells; it differs only in the heading of section 12.1) - exit status 0, no error or
  stderr output in the executed notebook, `checks of this notebook: 40 passed, 0 failed`, and the final
  list holds only the summary line of the 123 solver files and the six files of section 2, no
  `cargo-target` path (38.1 s wall time including nbconvert start).
* 2026-10-08, tests of the current version: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
  - 9 static tests OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 91.7 s (the installed
  versions equal the pins; `check` of all three notebooks in temporary folders is byte-identical);
  `build_notebooks.py audit` PASS (0 problems) for all three notebooks.
* Previous version (notebook sha256 `fadca750e38b16dcfa3f7687e52f8e0882639d09f49267c2429df722c86e8429`,
  455344 bytes), recorded below:
* 2026-10-08, the reason for the previous version: on Windows the MSVC linker `link.exe` cannot open
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
* 2026-10-14, the author's coordinates x0..x7 (ordered by the user on 2026-10-14; the record had named them x1..x8 with the hidden direction x8 last): the coordinate definition and section 4.1 (the user's metric with b4; the recorded states are at b4 = 1), the hidden-direction pressure P0 = T^x0_x0 (was P8), the ratio w_x0 = P0/E (code `wx0`, was w8), every x8 in the texts. `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses` - executed in 14.1 s, wrote 458105 bytes, audit PASS, sha256 `f339eb3ff22561b9e9f1b3dda9bb2cda04a522457b6883c8e51f154ad5883c49` (the version before: 457652 bytes, `30d2e843921159fa...`; builder before `12d5cad95338f4ff...`); `check dark_sector_hypotheses` - a second independent execution (13.4 s): PASS, the re-executed notebook is byte-identical; the 129 files of the two output folders are byte-identical and equal to the table of section 2 (refreshed from them). The notebook's own checks pass as before (no FAIL line). Tests: `REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py` - 11
  tests OK in 48.6 s (the installed versions equal the pins; `check` of all three notebooks byte-identical). Every run
  with `timeout 423`.
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
