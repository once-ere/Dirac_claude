# Provenance of the Revision notebook `dark_sector_hypotheses.ipynb`

The dark-sector hypotheses of dirac16complex and dirac16complex00 against the Unite values, for the corrected
primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1): in the author's coordinates x0..x7
(x0 the hidden direction, first), g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4}, e^{2 a4}, e^{2 a4}, -1,
-e^{-2 a4} b4 (sin^2 z)^{1/6} three times) with g44 = -1, x0 space-like and z = 6 H x0 real; a4 and b4 are
functions of x4, b4 is never 1. The earlier metrics are WITHDRAWN and appear here only as history (sections 5
and 7): the metric with b4(x4) of 2026-10-14 (the version of this notebook of 2026-10-15/16), version 1 of
2026-10-16 (g44 = -Sin^(1/3), never used by this notebook) and, before them, b4 = 1.

* Notebook: `Revision/notebooks/dark_sector_hypotheses.ipynb` (47 cells: 26 markdown, 21 code; 473375 bytes;
  sha256 `6d8a326a1c7cbff8f1452fa12b48742616e08089ff7850f5411ef9c9ffe1de71`).
* Builder: `Revision/notebooks/src/dark_sector_hypotheses.py`
  (sha256 `da4a59f817e7560b541920f6946ec30fcb3e08d755322f8c618afda784b6db62`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified for the corrected metric (version 2) on 2026-10-17 (section 7; earlier versions: the
  withdrawn metric with b4(x4) on 2026-10-15 and 2026-10-16, the withdrawn b4 = 1 on 2026-10-08 and 2026-10-14),
  Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6, matplotlib 3.11.0, nbformat 5.10.4,
  nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6, jupyterlab 4.4.10, cargo 1.91.1.

Honesty labels used by the notebook (binding: `Revision/SPEC.md` sections 8 and 11, `Revision/README.md`):
the history a4 = H x4, b4(x4) = b4(0) e^((4/3) H x4) (beta = d ln b4/d a4 = 4/3; with the author's weights this
history needs an ANISOTROPIC source, kappa (p3 - p0) = -9/16 kk^2 + 1069/432 kk + 2015/972 with kk = e^((2/3) H x4),
which neither the gas nor any condensate is) is a PRESCRIBED background (test field, no back-reaction); the filling
of both fold conditions is ASSUMED and the filling of the positive branch is the CONVENTION of
`Revision/kohn_sham/ks-theory.json`; the observer normalisation (A, B, C for dirac16complex; N1, N2 for
dirac16complex00) is an ASSUMPTION; a4_today, the gas fractions, the condensate value lambda S/m = -382/441 and
every parameter of the dirac16complex00 models M2 to M5 are CHOSEN (by construction, NOT predictions; they were
solved on the withdrawn b4 = 1 record to reproduce the Unite tangent or fit and are kept unchanged); the comparison
with the Unite numbers is an INTERPRETATION; the M5 component of negative classical energy is labelled ghost-like;
neither Hypothesis nor Hypothesis00 is established. The extra times x5, x6, x7 deflate exponentially (scale factor
e^{-a4} b4^{1/2} (sin^2 z)^{1/12}, ~ e^{-a4/3} on the history) at every slice, and the hidden direction x0 shrinks
with them (scale factor e^{-a4} b4^{1/2} |cot z|); no static or frozen extra times are used.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into the build folder `<cargo-target>` (section 2) and requires zero
   compiler warnings.
2. Runs `revision_ks_solver single --m 1 --lambda 157.7 --a4 0.0 --N 8 --out <output>/ks_runs/N8_lamp1_a000.json`
   (the arguments of `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`: the coupling is
   lambda_hat, the solver takes beta = 4/3 from ks-theory.json, uses the cell volume ell^3 v_t e^((5/3) a4) and the
   hidden scale f = e^(-a4/3), so the effective coupling is lambda_eff = lambda_hat e^(-(5/3) a4); working folder the
   repository) and prints the solver's four input checks (`theory_input_metric_forms`,
   `theory_input_coefficients`, `gamma_fixture_numeric`, `block_reduction_numeric`) and the parameter block of its
   result; checks H, m, L, dk, v_t, tip angle, T = 0 and the numerics tag against
   `Revision/kohn_sham/results/parameters.json`, the 41 slices against `reports/ks-history-run.json`, that the run
   report states the corrected metric, the PRESCRIBED history a4 = H x4, b4(x4) = e^((4/3) H x4), beta = 4/3, the
   coupling lambda_hat with the cell volume ell^3 v_t e^((5/3) a4) and the equivalent lambda_eff = lambda_hat
   e^(-(5/3) a4) (which the notebook's `lambda_eff` reproduces at all 41 slices), and that the solver ran with
   beta = 4/3 and, at a4 = 0, the hidden scale f = 1 and the cell volume `Vol7AtA4Zero` of `parameters.json`.
3. Solves the remaining 122 states of three series of the dense history (N2352_lam0, N592_lam0, N8_lamp1 with
   lambda_hat = lambda_1 = 157.7, i.e. lambda_eff = 157.7 e^(-(5/3) a4); a4 = 0, 0.05, ..., 2) with up to eight
   parallel solver processes; every run exits 0 with the final line SUCCESS and only the four PASS input checks on
   its error stream.
4. Rebuilds each row exactly as `run_ks_history.py` writes it (with the columns b4_over_b4_0 = e^((4/3) a4),
   lambda_eff, beta and Vol7; shortest round-trip floats, occupied-set fingerprint) and requires the text to equal the
   committed row of `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv`: 123 of 123 identical.
   Repeats the run report's checks for these series: occupied set fixed at all 41 slices (25, 11 and 2 occupied
   levels), hidden-direction conservation p0_y + 3 H (p0 - p_t) = 0 with the largest relative residual 5.029e-10
   (<= 1e-6), particle number to 2.220e-15.
5. Recomputes, with the functions `deriv`, `interp` and `cpl_fit` copied from `compute/compute_eos.py`,
   w_eff(A) = w_eff(B) = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E), w_eff(C) = w_eff(A) - (4 - 2 beta)/3 = w_eff(A) - 4/9,
   w3, wt, wx0 and the derivatives d w_eff/d a4, d w3/d a4: 123 of 123 rows equal `outputs/eos-history.csv`
   character for character; conservation with the terms of the deflating extra times and the shrinking hidden
   direction, dE/da4 = -3 P3 + Pt + P0/3, to 1.965e-06 (finite differences, interior slices) and 2.147e-07
   (Simpson), relative to max|E|; the law dE/da4 = -3 P3 of the inflating 3-space alone misses the N = 8 series by
   1.624 (of max|E|); d w_eff(A)/da4 two ways to 1.069e-06. Checks that the gas (N = 2352, 592; lambda = 0) is an
   exact fold-band gas: P3/E = 1/3 and Pt/E = P0/E = 0 to 7.8e-16 and E e^(a4) constant to 3.1e-15, so
   w_eff(A) = 1/3 (to 7.8e-16) and w_eff(C) = -1/9 (to 7.2e-16) at every slice; and that the N = 8, +lambda_1 zero
   modes have P3 = Pt, E < 0 with E(2)/E(0) = 0.184709 (e^(-10/3) = 0.035674), P0/E in [2.344884, 3.823722] and
   w_eff(A) in [0.239538, 0.400974].
6. Recomputes the complete entries of the three series in `outputs/eos-summary.json` (ranges, d ln E/d a4,
   sign of E, CPL tangents at a4_today = 0.5, 1, 1.5, 2, least-squares fits over [1/2, 1] and [1/3, 1],
   conservation deviations): all three equal. The gas has the constant w_eff(C) = -1/9: tangent wa in
   [-5.514e-14, 4.385e-14] and fitted wa in [-6.661e-16, 1.332e-15], zero to rounding (|wa| <= 1e-9), far from
   the Unite pair (-0.861, -0.60).
7. Condensate with exact fractions: u = lambda S/m = -382/441 gives u/(2 + u) = -191/250 = -0.764 at one
   instant (CHOSEN, by construction); on the history u ~ e^(-(5/3) a4) and the ratio drifts with
   wa = (10/3) u/(2 + u)^2 = -28077/12500 = -2.246160; w_eff(A) = (5/9) w_c = -191/450 and
   w_eff(C) = (5/9) w_c - 4/9 = -391/450, both with wa = -9359/7500; the phantom window -2 < u < -1 (63 of the 384
   exact grid values u = k/64 in [-4, 2]), in which the observer also reads w_eff(C) < -1 (the drift carries
   u = -382/441 into it toward the past, from a = (382/441)^(3/5) = 0.9174 to a = (191/441)^(3/5) = 0.6053). Closed
   formulas of `outputs/effective-formulas.json` with exact dual numbers (Fraction parts): the flat massive mode
   tangent x/(3(x + 1)), 2x/(3(x + 1)^2); fold-band gas + lambda = 0 condensate r0/(3(r0 + 1)),
   r0/(3(r0^2 + 2 r0 + 1)), whose C value w0 - 4/9 cannot reach -0.861 (it would need r0/(3(1 + r0)) = -3749/9000,
   outside [0, 1/3); such a mixture exists only for beta in (417/2000, 1417/2000]); the observer formulas with beta.
8. Mixtures (gas N2352_lam0 + condensate, today a4 = 2): the twelve mixtures with a lambda = 0 condensate equal
   `outputs/eos-summary.json`, and under C w_eff(C) >= -0.444111 >= -4/9 over 1000 gas fractions and all slices;
   the scans with a drifting condensate (ratio, A_B, C; 400 ratios x 201 gas fractions x 4 todays) equal
   `mixture_scan`: the closest point to the Unite pair is under C at distance 0.1604394909208
   ((-0.7055555555556, -0.6397222222222), the pure condensate with w_c = -0.47 today at a4_today = 0.5), and every
   mixture with w0 within 0.1 of -0.861 has wa between -1.779879740253 and -0.8286111111111 under C (ratio
   [-3.136, -2.159381216106], A_B [-4.447785313931, -3.006388888889]).
9. Hypothesis00 (`Revision/dark_sector/dirac16complex00/eos-theory.json`), exact on the history b4 ~ a^(4/3):
   N2 tangents M2 (-2749/9000, 81037/500000; freezing), M3 (-3583/9000, -196963/4500000), M4 with the parameters
   of the withdrawn tuning (-3583/9000, -1/15): no longer the Unite pair; positive components bounded by -4/9
   (turning points a_* = s^(-3/2): M3 6.264, M4 1.886, M5 2.337); the Unite w0 needs a ghost fraction
   G >= 3749/3000 (total energy zero at a = 3749/6749); M5 (G = 3/10) has no crossing of -1 on [1/3, 1]
   (minimum -0.908952); the Unite line crosses -1 at a = 461/600; the four models re-evaluated in floating
   point at a = 1/3, 1/2, 3/4, 1 (under N2, N1 and the ratio) agree with the recorded `w_at` values to 4.44e-13;
   the source the author's equations require on the history (kk = e^((2/3) H x4)) is ANISOTROPIC,
   kappa (p3 - p0) = -9/16 kk^2 + 1069/432 kk + 2015/972 and kappa p0 - Lambda = kappa p_t - Lambda =
   79/16 kk - 497/144, while every condensate has p3 = p_t = p0 and decays like e^(-(5/3) a4): no condensate is that
   source.
10. Reads the seven committed dark-sector reports and asserts their counts exactly as their JSON files give
    them: `dirac16complex/reports/derivation-checks.json` 37/37, `ks-history-run.json` 8/8,
    `eos-checks.json` 13/13, `independent-checks.json` 10/10, `dirac16complex00/reports/python-derive-eos.json`
    48/48, `python-independent-numerics.json` 32/32, `Revision/dark_sector/reports/wolfram-dark-sector.json`
    7/7 (0 failed in each; every listed check with verdict PASS). The Wolfram twin of the withdrawn metric,
    `wolfram-dark-sector-b4.json`, is not read.
11. Draws four figures: w_eff under A = B and under C along the history for the three series with the Unite
    reference lines; w_eff(C) of gas + lambda = 0 condensate mixtures and of the drifting condensate against
    a = e^{a4 - 2} with the Unite CPL line; the dirac16complex00 populations M2 to M5 under N2 (with the Unite
    CPL line and the bound -4/9) and N1; all candidates in the (w0, wa) plane with the Unite pair.
12. Ends with "what this notebook showed, and what it did not show".

The notebook prints 46 PASS lines of its own (and the solver's four input checks, indented) and no FAIL
line; its last code cell prints `checks of this notebook: 46 passed, 0 failed`.

## 2. Files read and written

Read (sha256 at the time of the verified builds of 2026-10-17, the corrected metric, version 2):

| file | sha256 |
| --- | --- |
| `Revision/SPEC.md` | (only its existence is used, to find the repository) |
| `Revision/kohn_sham/solver/Cargo.toml` | `464d553adcfaa1943af53ec3b18324fcba99ee92b3d82efcb08d2dc74bca24b1` |
| `Revision/kohn_sham/solver/Cargo.lock` | `65b7ed2cbe76d4701a66287cfbdedc8d4a780ee3c9e672de0e4055eb4ae70738` |
| `Revision/kohn_sham/solver/src/analysis.rs` | `94fd05fcfc98eb8fab929f4b6d73b54db940c2c9f36b0acb64cab7ed39552dbc` |
| `Revision/kohn_sham/solver/src/cache.rs` | `ca8387adaa0a62d76c5cc4593a29c5fb27f62c5aa62f9ad42e7938f8a943e87f` |
| `Revision/kohn_sham/solver/src/json.rs` | `919be3b192ab81d62deb8429229aa065a50d8fd0f8df6877ac4e413909efdf05` |
| `Revision/kohn_sham/solver/src/main.rs` | `0266bca239916d7e55143cd1b485fa7010169b200fa6548db6844617e0b841f0` |
| `Revision/kohn_sham/solver/src/mermin.rs` | `b6c7de3c00a149ba197cc795af770f011822a2023b2dc78dbc8af362827555a5` |
| `Revision/kohn_sham/solver/src/model.rs` | `10de235da72d082635ef3fdf4cdd2b00094294f90a2f1a2cc1260bc8d6f2a3e1` |
| `Revision/kohn_sham/solver/src/report.rs` | `0a770aff24dde0de531d0578e968ab9cad3d5f42b7cda532f7c753633b7ff9c7` |
| `Revision/kohn_sham/solver/src/runs.rs` | `3375ad314e07930e43ce1580735a79aafe2ded36ac4b491dc0e34739be30d819` |
| `Revision/kohn_sham/solver/src/scf.rs` | `0b5b97a082248096d37d186327b95ea4d520fb4fe197c2ee1bb948ffb5448ef5` |
| `Revision/kohn_sham/solver/src/sha256.rs` | `f44ed328e324b26d9b7c78f530e95be9ff1c88b179026ab4839ab38009e15122` |
| `Revision/kohn_sham/solver/src/shoot.rs` | `0671d70af830caabcd6c90d15ed7773fd7f3df814270d9eb4e9b8fd6b2d0d346` |
| `Revision/kohn_sham/solver/src/spectrum.rs` | `f88228658ad1145d67f55d7a9d33a50a50c0ae7df6b5fc62e5797ea05ba99034` |
| `Revision/kohn_sham/solver/src/theory.rs` | `0fb725199bbda618d22f2225cf2fdc273af47fe46a3863ec0f1df2a25939ffed` |
| `Revision/kohn_sham/ks-theory.json` (read by the solver) | `34f7fa2a4543fd9192dbcf23592d57e60506fed862ab63505873c2965ca6de98` |
| `Revision/algebra/gammas.json` (read by the solver) | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/kohn_sham/results/parameters.json` | `b320f560e84678a9b1e8d22db30f42a204dc53d8c2895703794033ddb371a6f6` |
| `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` | `658454be04dead5ef1c2037327fe9d80f4882a72457571d7325379ff4d44ff9b` |
| `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` | `77639409ba6846da06fa5e648d8fdaee3471cb04b17d936ab42d5aa2d294d5e4` |
| `Revision/dark_sector/dirac16complex/outputs/eos-summary.json` | `c6a56e2f76331d6bbd5171e9069efcf24d827670bb9a1b152fb554cea79d07a7` |
| `Revision/dark_sector/dirac16complex/outputs/effective-formulas.json` | `07c00451e84fd0642be3092d1ac734ffbe6f8ee55f0b0a5a0b19253283024ebe` |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | `89fe8cdffcf01c2edad22f313d0130e5195e92a0d7c1e84fbb410476a6cbc9cd` |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | `50c671fa0b5a681661685eae46b5ab73b565bcb02f6d6b470e6c6470aa6fb70f` |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | `443f48736bbe7901430b59f3deeff38efdc7687eb7b7d18c3f92b441f6293cd3` |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | `226d0457e9944183fecea1971aef5a4ed12b3f0d6eb8ab1b020c56fa79289a7e` |
| `Revision/dark_sector/dirac16complex00/eos-theory.json` | `f24a778b9af3c81ed4c6b05b0157db36096c1ec2f04266cb439d9430c02418a1` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | `ef39d9fb0319f060a7abd07a5c3dc5e1f74b591e912ccc7a41a95fe170625981` |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | `ca3e2014f23b367f9ef1a91f2dc5039327ed35bf4fee9ab82b678731d21f5b9b` |
| `Revision/dark_sector/reports/wolfram-dark-sector.json` | `1fdc801742c2fbf9f345253fe6d61b8d90b4230af01adf9151ba2722cd16385e` |

Every file of this table was last written before the first build of 2026-10-17 started (the newest, the
regenerated reports of the dark-sector record, at 13:44 local time; build A of this notebook started after
13:45:55) and is unchanged since. The solver source files are also compiled into the solver (`cache.rs` embeds
them to key its job cache).

Followed but not executed (the notebook reproduces their arithmetic; listed so that a change is noticed):
`Revision/dark_sector/dirac16complex/compute/run_ks_history.py` (sha256
`49afb3120643be1302a4450a802affe1eeef3ee62836918f853b3231b1704bfc`) and
`Revision/dark_sector/dirac16complex/compute/compute_eos.py` (sha256
`f61cf567245e0dca1921e310e6543fc2b266999a681d822001dcac831702bee2`).

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/dark_sector_hypotheses` in the repository, ignored by
git), identical in builds A and B and in the `check` run of 2026-10-17 (129 files compared, section 7); the Rust
build into `<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-dark_sector_hypotheses-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/ks-history-dense-subset.csv` (header + the 123 reproduced rows of `ks-history-dense.csv`) | 36209 | `e0ddbccc7c994a650afadf8ff74927174b08db00d04656969b8e351f7c7f2a5f` |
| `<output>/eos-history-subset.csv` (header + the 123 reproduced rows of `eos-history.csv`) | 37425 | `2fcb8c982353eec1d252a6ead846bcebaa307b5325ead6b42785ecf0ac1c3b40` |
| `<output>/figures/figure1_w_eff_histories.png` | 66128 | `73cb58c355facfa5a07400af3039fa5f7456a14aa6cc32efdf8d5c3baac77abb` |
| `<output>/figures/figure2_mixtures.png` | 58223 | `40b6a974c487373462fa7c5ac464824e18fa46d1630bb91a40b10983f23766f3` |
| `<output>/figures/figure3_dirac16complex00_populations.png` | 68670 | `68c616466474b56f84925cf77ef98e0b4541a2c2fc080b737f2fb0d3376da931` |
| `<output>/figures/figure4_w0_wa_plane.png` | 44179 | `83c3d336375343bb334608625242662588d91eeef68d3be53198480176d45ca0` |
| `<output>/ks_runs/<id>.json` (123 solver result files, ids `N2352_lam0_a000` ... `N8_lamp1_a200`) | 10052338 in total | combined `bcb05421bb591dea824902f45cc9f0f1b401082e48955ee19f4dcec202761d41` (sha256 of the 123 lines `<sha256>  <file name>`, sorted by file name, LF) |
| `<cargo-target>/` | 6748159 (13 files) after each run of 2026-10-17 | the Rust build folder (compiler output; not compared) |

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

* Section 5: the Unite values (-0.764; (-0.861, -0.6)), `exit status: 0`, `compiler warnings: 0`,
  `solver_built`.
* Section 6: the command `$ revision_ks_solver single --m 1 --lambda 157.7 --a4 0.0 --N 8 --out
  <output>/ks_runs/N8_lamp1_a000.json`, the solver's four indented `PASS` input checks
  (`theory_input_metric_forms`, `theory_input_coefficients`, `gamma_fixture_numeric`, `block_reduction_numeric`),
  `-> SUCCESS, exit status 0`, the parameter block (H 1.0, m 1.0, L 3.0, dk 0.25, v_t 1.0, a4 0.0,
  beta 1.333333333333333, f 1.0, coordinateCell False, Vol7 15875.21366031351, lambda 157.7, N 8.0, T 0.0,
  tipTheta 0.0, exactFockVariant False), `parameters_equal_record`, `history_equals_record`,
  `lambda_hat = lambda_1 per N (results/parameters.json): {8: 157.7, 592: 2.131, 2352: 0.5363}`, and the run
  report's solver, history and coupling texts.
* Section 7: `all_runs_succeeded: 123 runs`, `dense_rows_bit_identical: 123 of 123 rows`, three
  `..._occupations_fixed` lines (25, 11 and 2 occupied levels), `y_conservation_and_particle_number` (5.029e-10,
  2.220e-15), the table of b4/b4(0), lambda_eff, E, P3, Pt, P0 (for example N2352_lam0 at a4 = 0:
  E = 2.288388233e+03, P3 = 7.627960778e+02, Pt = P0 = 0.000000000e+00; N8_lamp1 at a4 = 2: b4/b4(0) = 14.391916,
  lambda_eff = 5.625789e+00, E = -6.979530633e-03).
* Section 8: `eos_rows_identical: 123 of 123 rows`, `conservation_with_deflation_terms` (1.965e-06, Simpson
  2.147e-07), `conservation_of_3_space_alone_fails` (1.624e+00), `derivative_two_ways` (1.069e-06); the w table
  (N2352_lam0 and N592_lam0: w_eff(A) = 0.333333 and w_eff(C) = -0.111111 at every listed slice; N8_lamp1:
  w_eff(A) = 0.400974 at a4 = 0 and 0.258448 at a4 = 2, w_eff(C) = -0.043470 and -0.185996, wx0 = 2.344884 and
  3.667694); `gas_exact_fold_band`, `gas_C_minus_one_ninth`, `n8_interacting_zero_modes` (E(2)/E(0) = 0.184709).
* Section 9: three `..._summary_equals_record` lines, the tangent and fit tables (N2352_lam0, today a4 = 2,
  under C: tangent (-0.111111, 4.385e-14), fit over [1/2, 1] (-0.111111, 0.000e+00), constant w -0.111111;
  N8_lamp1, today a4 = 2: tangent (-0.185996, -5.667e-02), fit over [1/2, 1] (-0.187982, -4.054e-02)) and
  `gas_cpl_constant`.
* Sections 10 and 11: `u = lambda S/m = -382/441 | ratio u/(2 + u) = -191/250 = -0.764 | wa = (10/3) u/(2 + u)^2 =
  -28077/12500 = -2.24616`; `condensate_ratio_exact`, `condensate_drift_exact` (-191/450, -391/450, -9359/7500),
  `condensate_phantom_window` (0.9174, 0.6053); the dual-number checks (`flat_mode_tangent_formulas`,
  `fold_band_gas_condensate_mixture_formulas` with -3749/9000 and (417/2000, 1417/2000], `observer_formulas`);
  `mixtures_equal_record`; `mixture_C_cannot_reach_unite_w0` (-0.444111); the scan line (C:
  (-0.7055555555556, -0.6397222222222), distance 0.1604394909208).
* Section 12: the table of exact tangents (M2 -2749/9000, 81037/500000; M3 -3583/9000, -196963/4500000; M4
  -3583/9000, -1/15), `unite_w0_requires_dominant_ghost` (3749/3000, 3749/6749), `positive_components_bounded`
  (turning points 6.264, 1.886, 2.337), `M5_no_crossing` (-0.908952), `unite_line_crossing: ... a = 461/600 =
  0.768333`, `models_w_at_equal_record: ... 4.44e-13`, `history_required_source`.
* Section 13: the table of the seven reports (37 / 8 / 13 / 10 / 48 / 32 / 7 checks, 0 failed).
* Section 14: four figures and `checks of this notebook: 46 passed, 0 failed`; the list of the written files
  (`<output>/ks_runs/*.json: 123 result files, 10052338 bytes` and the six files of section 2).

No run time and no path of the computer is printed (paths are shown relative to the repository or as
`<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11)

* 2026-10-17 (the corrected metric, version 2): 21.1 s and 20.7 s (`build`, builds A and B) and 20.8 s
  (`check`) of execution as the tool printed them (22.2 s, 21.7 s and 21.9 s wall time of the three commands),
  including the fresh `cargo build --release` of the solver into a new `<cargo-target>` and the 123 solver runs
  (up to 8 parallel processes). The time of a single solver run was not measured (the result files carry no
  time, and no log of these builds records one). The run-time sentence of the notebook's section 2.4 (about 15 s
  to 50 s for the whole notebook; a few hundredths of a second to about two seconds per solver run) is the text of
  the earlier versions; the measured whole-notebook times above lie inside its range, its per-run part is not
  re-measured here.
* Earlier versions (the withdrawn metric with b4(x4)): 2026-10-16 12.4 s (`build`) and 12.6 s (`check`);
  2026-10-15 15.1 s and 12.9 s (`build`), 12.8 s (`check`), then 13.5 s and 13.5 s (builds A and B) and 13.1 s
  (`check`) of execution.
* Earlier versions (b4 = 1, withdrawn): 13.4 s to 47.8 s of execution depending on the load (section 7).
* Not part of the notebook: the committed dense history (615 states, `run_ks_history.py`) runs in three parts of
  about 22 s each and an assembly of 0.7 s (2026-10-17, 22 workers), the independent free-gas implementation
  about 85 s (`Revision/dark_sector/dirac16complex/README.md`).

## 6. Side effects

* Writes only into `<output>` and `<cargo-target>` (and the tool writes the notebook file named in section 2). The committed
  records `Revision/dark_sector/`, `Revision/kohn_sham/results/` and `Revision/kohn_sham/reports/` are only
  read; the notebook raises an error if `<output>` or `<cargo-target>` would place its files there. The
  crate's own `target/` folder is not used (the build goes to `<cargo-target>`).
* By default `<cargo-target>` is a new folder of about 6.7 MB (6748159 bytes in 13 files at the runs of
  2026-10-17) in the system's temporary folder for every new `<output>` (every `build` and `check` of the tool
  uses a new `<output>`); nothing deletes it, it can be deleted by hand. It is placed there, short and outside the
  repository, because on Windows the MSVC linker `link.exe` cannot open a file whose path is longer than 259
  characters (MAX_PATH; section 7).
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

* 2026-10-17, the reason for the current version: the corrected primordial metric of 2026-10-16 (version 2;
  `Revision/SPEC.md` section 1; phase W6 of `HANDOFF.md` 0.10). The Kohn-Sham record (`Revision/kohn_sham`) and the
  dark-sector record (`Revision/dark_sector/`) were recomputed for it, and the builder was rewritten to reproduce
  them: the three series N2352_lam0, N592_lam0 and N8_lamp1 (lambda_hat = lambda_1 = 157.7) with the cell volume
  ell^3 v_t e^((5/3) a4) and the hidden scale f = e^(-a4/3); the solver's four input checks
  (`theory_input_metric_forms` added); the observer formulas w_eff(A) = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E),
  w_eff(C) = w_eff(A) - 4/9 and the conservation law dE/da4 = -3 P3 + Pt + P0/3; the exact fold-band gas
  (w_eff(A) = 1/3, w_eff(C) = -1/9); the condensate drift u ~ e^(-(5/3) a4); the bound -4/9 of positive-energy
  models, the ghost fraction G >= 3749/3000 and the anisotropic source the history requires; section 13 reads
  `wolfram-dark-sector.json` (7 checks) instead of the Wolfram twin of the withdrawn metric. Still 46 checks of
  the notebook. Every table of sections 2 and 4 was rewritten from the files of these builds.
* 2026-10-17, two builds and one check, each command under `timeout -k 5 423`, the system's temporary folder
  unchanged (default `<cargo-target>`, a new one for each `<output>`), started after the regeneration of the
  record (section 2):
  build A: `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses --out
  <scratch>/dark_sector_hypotheses_buildA` - executed in 21.1 s (22.2 s wall time), exit status 0, wrote
  473375 bytes, audit PASS, sha256 `6d8a326a1c7cbff8f1452fa12b48742616e08089ff7850f5411ef9c9ffe1de71`;
  build B: the same command with `--out <scratch>/dark_sector_hypotheses_buildB` - executed in 20.7 s (21.7 s
  wall time), exit status 0, wrote 473375 bytes, audit PASS, the same sha256;
  check: `python Revision/notebooks/tools/build_notebooks.py check dark_sector_hypotheses --out
  <scratch>/dark_sector_hypotheses_check` - a third independent execution (20.8 s, 21.9 s wall time), exit
  status 0: `check dark_sector_hypotheses: PASS - the re-executed notebook is byte-identical to
  Revision/notebooks/dark_sector_hypotheses.ipynb (473375 bytes)`; the copy it wrote,
  `<scratch>/dark_sector_hypotheses_check/dark_sector_hypotheses.ipynb`, has the same sha256 `6d8a326a...`.
  The three runs wrote the same notebook (sha256 above, measured after each command) and the same output
  files: the folders of build A, build B and the check hold the same 129 files (123 solver result files, two
  subset CSVs, four figures; the check folder in addition its notebook copy), byte-identical file by file and
  equal to the table of section 2 (ids `N2352_lam0_a000` ... `N8_lamp1_a200`, 10052338 bytes, combined
  `bcb05421...`). The committed `Revision/notebooks/dark_sector_hypotheses.ipynb` is this build output (sha256
  `6d8a326a...`, 47 cells). Its executed outputs: 46 PASS lines of its own and the solver's four indented
  input checks, no FAIL line, no error output and no stderr output, `checks of this notebook: 46 passed, 0 failed`.
  The four figures were looked at: they show what sections 14.1 to 14.4 of the notebook describe (cosmetic
  only: in figure 1 the legend of the right panel covers part of the N = 8 curve; in figure 3 the label of the
  bound -4/9 lies on the M3 and M4 curves; in figure 4 the gas points at (-1/9, 0) lie under the mixture point
  of gas fraction 1).
* 2026-10-17, tests, after this file was rewritten: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
  (`REVISION_NOTEBOOKS_FULL` not set) - 11 tests in 0.050 s: OK, 9 static tests passed (among them
  `test_cells_equal_builder`, `test_provenance_records_current_digests` and `test_dark_sector_record_counts_printed`),
  2 skipped (the full re-execution tests).
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
* Earlier versions, for the withdrawn metric with b4(x4) of 2026-10-14, kept as the record of their verification
  (their sha256 values, sizes and "the table of section 2" refer to the tables of those versions, not to the
  current ones):
* 2026-10-16, the Kohn-Sham record moved to b4(x4) (`HANDOFF.md` 0.9, phase 4; `Revision/dark_sector/B4_PROVENANCE.md`, section 10): the solver's `single --lambda` now means lambda_hat with the cell volume ell^3 v_t e^{2 a4}, and the record's couplings were recalibrated on the history. Builder changes: `run_one` passes lambda_hat (as `run_ks_history.py`), the dense rows carry the new columns `beta` and `Vol7`, the check `history_with_b4_equals_record` reads the new coupling text of the run report and the solver's beta and cell volume, the expected count of `ks-history-run.json` is 8, and the texts of sections 2 (glossary), 4.5, 5.2, 6, 7.2 and 7.3 describe lambda_hat, the growing cell and the equivalent lambda_eff. `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses` - executed in 12.4 s, wrote 473860 bytes, audit PASS, sha256 `14994bb5cbfd629cd1a28c6f978038f357c2cc08b98609e0e6797c765f3fd922` (builder `99464e21eac070240b67c27f438f06a5bb2061df486c179f531cb65992911f60`), `checks of this notebook: 46 passed, 0 failed`, the 123 dense rows and the 123 equation-of-state rows equal the committed ones character for character; `check dark_sector_hypotheses` - a second independent execution (12.6 s): PASS, byte-identical; the 129 output files of the two folders are byte-identical and the tables of section 2 were refreshed from them. Every run with `timeout -k 5 423`.
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
* 2026-10-15, the reason for that version: the user's metric with b4(x4) (b4 is a function of x4,
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
* 2026-10-14, the author's coordinates x0..x7 (ordered by the user on 2026-10-14; the record had named them x1..x8 with the hidden direction x8 last): the coordinate definition and section 4.1 (the user's metric with b4; the recorded states are at b4 = 1), the hidden-direction pressure P0 = T^x0_x0 (was P8), the ratio w_x0 = P0/E (code `wx0`, was w8), every x8 in the texts. `python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses` - executed in 14.1 s, wrote 458105 bytes, audit PASS, sha256 `f339eb3ff22561b9e9f1b3dda9bb2cda04a522457b6883c8e51f154ad5883c49` (the version before: 457652 bytes, `30d2e843921159fa...`; builder before `12d5cad95338f4ff...`); `check dark_sector_hypotheses` - a second independent execution (13.4 s): PASS, the re-executed notebook is byte-identical; the 129 files of the two output folders are byte-identical and equal to the table of section 2 (refreshed from them). The notebook's own checks pass as before (no FAIL line). Tests: `REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py` - 11
  tests OK in 48.6 s (the installed versions equal the pins; `check` of all three notebooks byte-identical). Every run
  with `timeout 423`.
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
* The version of 2026-10-08, all runs with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch
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
  execution; the same 129 files); they differ from the notebook of that version only in the heading of section
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
* 2026-10-08, tests of that version: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
  - 9 static tests OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 91.7 s (the installed
  versions equal the pins; `check` of all three notebooks in temporary folders is byte-identical);
  `build_notebooks.py audit` PASS (0 problems) for all three notebooks.
* The version before it (notebook sha256 `fadca750e38b16dcfa3f7687e52f8e0882639d09f49267c2429df722c86e8429`,
  455344 bytes), recorded below:
* 2026-10-08, the reason for that version: on Windows the MSVC linker `link.exe` cannot open
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
  last commit before this change) and passed with the current ones of that time (byte-identical, 455344 bytes,
  47.8 s). A review had found the same failure for the notebook
  `lovelock_gkd` (above 148 characters); all three notebooks were changed in the same way. Since then
  the build goes to `<cargo-target>` (sections 2 and 6); the results and the figures were unchanged.
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
