# Provenance of the Revision notebook `kohn_sham_states.ipynb`

The Kohn-Sham states of dirac16complex in the author's deflating primordial field.

* Notebook: `Revision/notebooks/kohn_sham_states.ipynb` (33 cells: 19 markdown, 14 code; 494302 bytes;
  sha256 `028f490cfb7b9fc2db9d7558efff1d9891e68b7021a3edc2c034378b766dacd9`).
* Builder: `Revision/notebooks/src/kohn_sham_states.py`
  (sha256 `1f1e0b29251f6a5bda1631102ef454471d57ac20c2862dba0972ca3ade211d36`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, in the author's coordinates x0..x7 on 2026-10-14, for the author's metric with
  b4(x4) on 2026-10-16, and for the corrected metric of 2026-10-16 (version 2; the Kohn-Sham record recomputed on
  2026-10-16/17, phase W5 of `HANDOFF.md`) on 2026-10-17, rebuilt the same day after the text corrections of
  the audit (phase W6; section 7),
  Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.1.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into the build folder `<cargo-target>` (section 2) and requires zero
   compiler warnings.
2. Runs `revision_ks_solver single --m 1 --lambda 0.0 --a4 0.0 --N 8 ... --root <repository>` and prints
   the solver's four input checks (`theory_input_metric_forms`: the forms of the corrected metric that the
   solver implements, read from `ks-theory.json`; `theory_input_coefficients`: M_eff = m + 0.9375 lambda S,
   v_v = -0.0625 lambda n from `ks-theory.json`; `gamma_fixture_numeric`: the author's gammas of
   `Revision/algebra/gammas.json`; `block_reduction_numeric`: the exact 2 x 2 block reduction) and the
   parameter block of its result; checks H, m, L, dk, v_t, tip angle and the numerics tag against
   `Revision/kohn_sham/results/parameters.json`.
3. Solves nine canonical zero-temperature states (N = 8, lambda = 0; N = 592, lambda = +lambda_1 =
   2.131, the solver's lambda_hat, held fixed along the history while Vol_7(a4,0) = ell^3 v_t e^((5/3) a4,0) grows;
   N = 2352, lambda = 0; each at a4,0 = 0, 1, 2 of the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)) with profiles, and
   the thermal state N592_lamp1_a10_T20 (T = 0.02 m).
4. Compares with the committed record: E_KS, E_band, E_int, iterations, residual, HOMO, LUMO
   (equal floating-point numbers) and the Kohn-Sham gap (within 1e-15 of the larger level, because
   the files record 16 significant digits and the solver forms the gap from unrounded levels) with
   `results/ground/summary.csv`; every level of `results/ground/levels/<id>.csv` equal (the command
   `single` lists, in addition, only empty levels of higher shells); the five EMT integrals with
   `results/ground/emt-integrals.csv`; the nine profile files byte for byte with
   `results/ground/profiles/<id>.csv`; mu, E and the entropy of the thermal state with
   `results/thermo/thermodynamics.csv`, and F = E - T S with its F to 1e-12 relative.
5. Tables of the lowest levels (N = 8 at the three slices), of E_KS, HOMO, LUMO, gap, P3/E, Pt/E, P0/E
   along the history; checks that the N = 8 gap is the n2 = 1 fold-band level 0.25 e^(-a4,0) exactly, that the
   free N = 2352 gas has P3/E = 1/3 (an exact fold-band gas) and that the interacting N = 592 gas stays just
   below 1/3.
6. Takes the 84 rows of `Revision/kohn_sham/reports/ks-crosscheck-table.csv` that belong to the ten
   states (nine quantities for each zero-temperature state; mu, E and the entropy for the thermal
   state): the column `rust` equals the new value to 16 digits (the gap within the rounding rule of
   item 4), |new - reference| is within the table's tolerance (largest ratio 0.3006) and the verdict
   is PASS.
7. Reads the seven committed reports and asserts their counts exactly as their JSON files give them:
   `ks-theory-wolfram.json` 51/51, `ks-theory-python.json` 61/61, `ks-rust-solver.json` 45/45,
   `ks-rust-determinism.json` 14/14, `ks-rust-mermin-roots.json` 5/5, `ks-reference.json` 39/39,
   `ks-crosscheck.json` 31/31 (0 failed in each; every listed check with verdict PASS).
8. Draws four figures: the fold band of N = 8 at a4,0 = 0, 1, 2 and the Kohn-Sham gap of the three
   series along the history; the profiles of N592_lamp1_a10 (n, rho, and p3/rho, p_t/rho, p0/rho); E_KS
   and P3/E, P0/E along the history; the cross-check ratios |new - reference|/tolerance.
9. Ends with "what this notebook showed, and what it did not show".

The notebook prints 24 PASS lines of its own (and the solver's four input checks, indented) and no
FAIL line; its last code cell prints `checks of this notebook: 24 passed, 0 failed`.

## 2. Files read and written

Read (sha256 at the time of the verified builds):

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
| `Revision/kohn_sham/ks-theory.json` | `34f7fa2a4543fd9192dbcf23592d57e60506fed862ab63505873c2965ca6de98` |
| `Revision/algebra/gammas.json` | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/kohn_sham/results/parameters.json` | `b320f560e84678a9b1e8d22db30f42a204dc53d8c2895703794033ddb371a6f6` |
| `Revision/kohn_sham/results/ground/summary.csv` | `b69f3fc17eb16b7a08213b8959094c7871356deb066a64211f94703dec850e03` |
| `Revision/kohn_sham/results/ground/emt-integrals.csv` | `4d2814cf1db3fe2e958fc77a55351f8f72b93cd496a95e9b0cf9eab7be8f09c6` |
| `Revision/kohn_sham/results/thermo/thermodynamics.csv` | `676963fbe2e79c908c92955ffe3e381d82a280a92c38e2c991f843875c80fb7b` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a00.csv` | `8f4da0814e9b2e92f44e3c3e1efaa9257e0d1b4244bc579768ea86eaff78e423` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a10.csv` | `b16a8ac2f203ea8418ae03c66b9d8c99aaf0c4cc1641c02394bc8394c6526619` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a20.csv` | `41a525930696b0a4e7eb1f73027fd5d9eedb950d8570beea5c891f3cb5f50f3f` |
| `Revision/kohn_sham/results/ground/levels/N592_lamp1_a00.csv` | `15c8de85d90257eb64e4ae740c14f591e595000ae22f67e4ff4286e58faeb0dc` |
| `Revision/kohn_sham/results/ground/levels/N592_lamp1_a10.csv` | `86cc87584d73f4546ce240a5baebeff719c9d682ede2b08b8b6d0807238878f9` |
| `Revision/kohn_sham/results/ground/levels/N592_lamp1_a20.csv` | `0caee6d3850b13b7ec553ba474f15bf8198210bf6bd4d2eed42d73c036b172f1` |
| `Revision/kohn_sham/results/ground/levels/N2352_lam0_a00.csv` | `2c421d5f8d71d9fcbe93680fdddef4970a6a9b07f23a63371dee4cd7ef54e696` |
| `Revision/kohn_sham/results/ground/levels/N2352_lam0_a10.csv` | `395aef2c2725717e9f85752c831fd7d48edbbd1c1f9990fa9c6772067a71ddd5` |
| `Revision/kohn_sham/results/ground/levels/N2352_lam0_a20.csv` | `1c4ba1d386e07e47ba5a6d2c28f2e3b2d56edc7da07ceaa81e2aec3b0d34b346` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a00.csv` | `a0cbb9e9d14f7bd4ccab958a6d168ef9c79e92c2f9a0308c5bd58901b2f92d4e` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a10.csv` | `532b79269a61a53ea75479e6890b349fae1bf86d6fe4b88d7695e6346ce3ec52` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a20.csv` | `99674812a6dfa87d202cc20879875090fb94c1f7a549d50b1d00a211e695b1e6` |
| `Revision/kohn_sham/results/ground/profiles/N592_lamp1_a00.csv` | `3ed3aa05f55eabbd3d9d88fe3c0302aabc61f6d200fb5f91406d17014b1f29eb` |
| `Revision/kohn_sham/results/ground/profiles/N592_lamp1_a10.csv` | `384d189c85680553456df46b14de465e3096ebeef171c36d4dcafed644f40272` |
| `Revision/kohn_sham/results/ground/profiles/N592_lamp1_a20.csv` | `46c9994924a227369ed36e2eaac3ccaa4f53f39ae8fafa7d1ec6f0d76ec5757b` |
| `Revision/kohn_sham/results/ground/profiles/N2352_lam0_a00.csv` | `03bfb7244004ac00efbabc8f6c78e3849115253fd919272530455d7429494a47` |
| `Revision/kohn_sham/results/ground/profiles/N2352_lam0_a10.csv` | `ae11b95c9c7a6389090c5bd2a11aae6a486e1b6dd04152f78bf0665017e829c2` |
| `Revision/kohn_sham/results/ground/profiles/N2352_lam0_a20.csv` | `fc74dac940f6f62b90695846bbb1be480761772487c822602c7d418fff77d4fe` |
| `Revision/kohn_sham/reports/ks-crosscheck-table.csv` | `d35e393e46d5f7cd343c1bfc3483c035e1da509ca0c2d3a8ea85be67107fe29e` |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | `ac7cc653d1d3242d628f8043ed48b3e67238ea0cc5fe0bf245109ab8116d0927` |
| `Revision/kohn_sham/reports/ks-theory-python.json` | `9fdb72adc94af56a8a535d506f1679907d03b0db74e1a136bc0307f4625ebe7f` |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | `a030a72a012167a9d1490d1cf0248c3d958a1faaa90e2ce8f22d17f8abdec49c` |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | `18c6dd8d6ea990b5bac90b8ccc32dfd072c16a5d813120048e85d605a3589e68` |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | `2d447423b81bbafc6542e28273e52b7a26f4646b37616472ff7675caa2d1144e` |
| `Revision/kohn_sham/reports/ks-reference.json` | `702c00a36aa3e3d3835d1c931b41cc3dd9a5612e76e18c8fbb02be2c268b725f` |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | `28cd52019d5bee86637d87d58f7a96d4e66deaf2e704d768b2eb91e626396e0f` |

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/kohn_sham_states` in the repository, ignored by
git), identical in both verified builds and in the `check` run; the Rust build into
`<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-kohn_sham_states-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/figures/figure1_fold_band.png` | 76851 | `1f6b119aab81b337c4b34c02334480b60a3f47eb5cd6ef941fd6b8bbec08df58` |
| `<output>/figures/figure2_profiles.png` | 69755 | `35b136324b5e9506497baba9c1a9449d280e200f79b1b85140231bc6ae930088` |
| `<output>/figures/figure3_history.png` | 65997 | `6cb56cb51543d0534777ceced78aa1ade7698040bdfed442f487402947e172fa` |
| `<output>/figures/figure4_crosscheck.png` | 94204 | `950f83a77c18ab7c159b49fc31c01c16f1c8fc398fb0cbd6ef3aab6e5fcf8e13` |
| `<output>/ks_runs/N2352_lam0_a00.csv` | 37224 | `03bfb7244004ac00efbabc8f6c78e3849115253fd919272530455d7429494a47` (= record `results/ground/profiles/N2352_lam0_a00.csv`) |
| `<output>/ks_runs/N2352_lam0_a00.json` | 40767 | `d9029e41ced2a0467e3d28fec4140fea7c25d42071dca124784f45f2817f8df8` |
| `<output>/ks_runs/N2352_lam0_a10.csv` | 38195 | `ae11b95c9c7a6389090c5bd2a11aae6a486e1b6dd04152f78bf0665017e829c2` (= record `results/ground/profiles/N2352_lam0_a10.csv`) |
| `<output>/ks_runs/N2352_lam0_a10.json` | 80555 | `5c25947ace35b84a832865123a6aa7965ff582af2af40ed4d3f1dcc397949fff` |
| `<output>/ks_runs/N2352_lam0_a20.csv` | 37790 | `fc74dac940f6f62b90695846bbb1be480761772487c822602c7d418fff77d4fe` (= record `results/ground/profiles/N2352_lam0_a20.csv`) |
| `<output>/ks_runs/N2352_lam0_a20.json` | 289920 | `2b139246a790574b71835edc9daeb2a8879b15b992c9630dda78703582422a1e` |
| `<output>/ks_runs/N592_lamp1_a00.csv` | 38434 | `3ed3aa05f55eabbd3d9d88fe3c0302aabc61f6d200fb5f91406d17014b1f29eb` (= record `results/ground/profiles/N592_lamp1_a00.csv`) |
| `<output>/ks_runs/N592_lamp1_a00.json` | 23035 | `83807bb2494eaf1fec6384628bd24a726c38798a990ac672eb5cb39816c9cbe3` |
| `<output>/ks_runs/N592_lamp1_a10.csv` | 38430 | `384d189c85680553456df46b14de465e3096ebeef171c36d4dcafed644f40272` (= record `results/ground/profiles/N592_lamp1_a10.csv`) |
| `<output>/ks_runs/N592_lamp1_a10.json` | 55682 | `d8829fddd16bca1b6e1e05473c79fb3ac5a34409ee4269b9c66a75752a84addc` |
| `<output>/ks_runs/N592_lamp1_a10_T20.json` | 44531 | `a6fd9de3fae413345c8ceb728dcb8893ff15802715601d6437ce003c4717877e` |
| `<output>/ks_runs/N592_lamp1_a20.csv` | 38427 | `46c9994924a227369ed36e2eaac3ccaa4f53f39ae8fafa7d1ec6f0d76ec5757b` (= record `results/ground/profiles/N592_lamp1_a20.csv`) |
| `<output>/ks_runs/N592_lamp1_a20.json` | 247396 | `a213177718587c576fbe63c71b8cf16982c697c2cc20575d2f4ae0162a0cb103` |
| `<output>/ks_runs/N8_lam0_a00.csv` | 37086 | `a0cbb9e9d14f7bd4ccab958a6d168ef9c79e92c2f9a0308c5bd58901b2f92d4e` (= record `results/ground/profiles/N8_lam0_a00.csv`) |
| `<output>/ks_runs/N8_lam0_a00.json` | 9155 | `6684656771cbd3f94def3ccd39a13e2f57b07e64073984b19ff29a7c6d5aa5ef` |
| `<output>/ks_runs/N8_lam0_a10.csv` | 37086 | `532b79269a61a53ea75479e6890b349fae1bf86d6fe4b88d7695e6346ce3ec52` (= record `results/ground/profiles/N8_lam0_a10.csv`) |
| `<output>/ks_runs/N8_lam0_a10.json` | 33960 | `613ee58be3a197f08c8ad264ddf03833d7862727accc8126317416d9cbab844e` |
| `<output>/ks_runs/N8_lam0_a20.csv` | 37086 | `99674812a6dfa87d202cc20879875090fb94c1f7a549d50b1d00a211e695b1e6` (= record `results/ground/profiles/N8_lam0_a20.csv`) |
| `<output>/ks_runs/N8_lam0_a20.json` | 204106 | `2f8f551a895bba8454464e042026c4728f072a2e73fc84fce4b58f104bfcb132` |
| `<cargo-target>/` | about 3.4 MB (3376109 bytes, 13 files, measured 2026-10-17) | the Rust build folder (compiler output; not compared) |

The tool writes `Revision/notebooks/kohn_sham_states.ipynb` (`build`) or
`<output>/kohn_sham_states.ipynb` (`check`). The notebook has no long mode.

## 3. How to run it

The complete, self-contained instructions for Windows 11 (PowerShell), macOS on Apple silicon (zsh)
and Linux (bash) are section 2 of the notebook: install Git, Python 3.12 or newer and Rust (rustup);
`git clone https://github.com/once-ere/Dirac_claude.git`; create a private environment OUTSIDE the
repository (`python -m venv $HOME\venvs\revision-nb` on Windows, `python3 -m venv ~/venvs/revision-nb`
on macOS and Linux); install the pins with `<environment python> -m pip install -r
Revision/notebooks/requirements.txt`; then either

```text
<environment python> -m jupyterlab Revision/notebooks/kohn_sham_states.ipynb
```

(choose the kernel "Python 3 (ipykernel)", press Shift+Enter cell by cell or Run All Cells), or
headless

```text
<environment python> -m nbconvert --to notebook --execute Revision/notebooks/kohn_sham_states.ipynb --output-dir ../revision-nb-runs
```

or, to rebuild and compare with the committed file (from the repository root):

```text
<environment python> Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out <new folder>
<environment python> Revision/notebooks/tools/build_notebooks.py check kohn_sham_states --out <new folder>
```

`python -m jupyter ...` is not used: it fails where the jupyter executables are not on PATH.

## 4. Expected output

As printed by the committed notebook (sha256 `028f490cfb7b9fc2...`, executed outputs read on 2026-10-17):

* Section 5: `exit status: 0`, `compiler warnings: 0`, and one PASS line (`solver_built`).
* Section 6: the solver's four indented `PASS` input checks, in this order `theory_input_metric_forms`
  (the forms of the corrected metric of 2026-10-16 that the solver implements: the hidden scale
  f = e^(-a4) b4^(1/2), kappa = e^(-a4) constant in y, Vol_7 = ell^3 v_t e^((2 beta - 1) a4,0), the
  y-conservation, the history identity and the fold-band slope c = e^(-a4,0); `entries not matching: none`),
  `theory_input_coefficients` (M_eff = m + 0.9375 lambda S, v_v = -0.0625 lambda n),
  `gamma_fixture_numeric` (max deviation 0e0) and `block_reduction_numeric` (to 1.1e-16); then
  `-> SUCCESS, exit status 0, input checks PASS: 4, other messages: 0`, the parameter block (H 1.0, m 1.0,
  L 3.0, dk 0.25, v_t 1.0, a4 0.0, beta 1.333333333333333, f 1.0, coordinateCell False, Vol7 15875.21366031351,
  lambda 0.0, N 8.0, T 0.0, tipTheta 0.0, exactFockVariant False), one PASS line (`parameters_equal_record`),
  lambda_1 = 157.7, 2.131, 0.5363 for N = 8, 592, 2352, and the honesty label of the record
  (`PRESCRIBED BACKGROUND: the history a4 = H x4, b4 = e^{(4/3) H x4} is prescribed, not solved for. ...`).
* Section 7: nine solver runs (ten states with the run of section 6; `states solved: 10`), each
  `-> SUCCESS, exit status 0, input checks PASS: 4, other messages: 0`; eleven PASS lines of the comparison,
  for example `N592_lamp1_a10_equals_record: E_KS = 131.7651779780565, ...`, and for the thermal state
  mu = 0.2929430552286682, E = 135.5651077811065, S = 387.8116964450197 and F = E - T S = 127.8088738522061.
* Section 8: the N = 8 gap 0.2500000, 0.0919699, 0.0338338 at a4,0 = 0, 1, 2 (the fold-band level 0.25 e^(-a4,0)); P3/E = 0.3281, 0.3279, 0.3262
  (N = 592, +lambda_1) and 0.333333333333334, 0.333333333333334, 0.333333333333333 (N = 2352, lambda = 0: 1/3, the exact fold-band gas);
  three PASS lines.
* Section 9: `crosscheck_rows_reproduced: 84 rows ... (largest ratio 0.3006)`; the table of the seven
  reports (51 / 61 / 45 / 14 / 5 / 39 / 31 checks, 0 failed) with one PASS line each (eight PASS lines).
* Section 10: the four figures, each with its sha256 as in section 2; section 10.2 also prints
  `max |M_eff - m| = 1.347e-02 m, max |v_v| = 7.461e-02 m`.
* Section 10.5: `checks of this notebook: 24 passed, 0 failed` and the 23 files listed above.

The 24 PASS lines of the notebook's own (counted in the executed outputs: lines that begin with `PASS`) are
1 (section 5) + 1 (section 6) + 11 (section 7) + 3 (section 8) + 8 (section 9); the solver's four input checks
are printed indented, once, in section 6 and are not among them. No line contains `FAIL`; no cell has
stderr or error output.

No run time and no path of the computer is printed (paths are shown relative to the repository, as
`.` for the repository itself, or as `<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11)

* 2026-10-17, rebuild after the audit (phase W6; the current notebook): 18.6 s (build A), 18.8 s (build B) and
  18.5 s (`check`) of execution as `build_notebooks.py` printed it; 19.7 s, 19.9 s and 19.5 s for the whole
  command (the step log). The three commands ran one after the other, before the builds of
  `dark_sector_hypotheses`.
* 2026-10-17, first build for the corrected metric (the machine otherwise idle): 18.8 s (`build`) and 20.4 s
  (`check`) of execution.
* 2026-10-16 (the metric with b4(x4); other jobs of this work on the computer): 14.6 s (`build`) and 14.4 s (`check`) of execution.
* 2026-10-14 (the author's coordinates; other jobs of this work on the computer): 11.5 s (`build`) and 11.6 s (`check`) of execution.
* Whole notebook, version of 2026-10-08 (the withdrawn record with N = 136, 688), executed by
  `build_notebooks.py`: 33.0 s (build A), 26.0 s (build B) and 28.6 s (`check`) of execution while other
  work ran on the computer (the version before: 21.7 s to 38.0 s under load, section 7; the first builds
  of this notebook took 12.2 s to 12.5 s), including the fresh `cargo build --release` of the solver into
  `<cargo-target>` and the ten solver runs (each under one second when timed separately: 0.06 s for
  N = 8, 0.5 s for N136_lamp1_a10, 0.9 s for N688_lam0_a20).
* Not part of the notebook: the canonical matrix of the solver took 284.5 s in one invocation
  (`revision_ks_solver all`, no cache) and, as the record is built, 134.6 s + 130.5 s in two parts plus
  5.4 s for the assembly (2026-10-16; a repeat in three parts on 2026-10-17: 76.7 s, 70.4 s, 85.7 s,
  assembly 5.7 s) (`Revision/kohn_sham/solver/README.md`, Timings).

## 6. Side effects

* Writes only into `<output>` and `<cargo-target>` (and the tool writes the notebook file named in section 2). The
  committed record `Revision/kohn_sham/results/` and the reports `Revision/kohn_sham/reports/` are only
  read; the notebook raises an error if `<output>` or `<cargo-target>` would place its files there.
  The crate's own `target/` folder is not used (the build goes to `<cargo-target>`).
* By default `<cargo-target>` is a new folder of about 3.4 MB in the system's temporary folder for
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
* Runs `cargo` (needs the Rust toolchain on PATH) and the built solver; no network access during the
  run, no Wolfram Language, no installation.

## 7. Verification record

* 2026-10-08, the reason for the version of 2026-10-08 (a review of the version before, two findings):
  (1) the final list of written files left out only `<cargo-target>`, so a folder `<output>/cargo-target`
  left in a reused `<output>` by an earlier version was listed file by file; it is now left out as
  well. (2) On Linux the default `<cargo-target>` lies in the shared `/tmp` under a predictable name,
  and the notebook runs the solver built there; on macOS and Linux the folder is now created private
  and an existing folder that is not private is refused (section 6). In the notebook only the sources
  of cell 1 (section 2.6), cell 5 (the folder set-up) and cell 31 (the final list) changed; every
  output is identical to the version before.
* 2026-10-08, the private-folder check: the exact code of the builder, run under WSL Ubuntu 24.04 with
  Python 3.12.3 (scratch script), created a new folder with mode 0700, accepted an existing own folder
  of mode 0755, refused folders of mode 0777 and 0775, a symbolic link and a folder of another user
  (`/usr`), and was skipped with `REVISION_NB_CARGO_TARGET` set (21 of 21 cases as expected for the three
  builders). The notebook itself was not executed on Linux.
* Version of 2026-10-08, all runs with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch
  folder:
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out
  <scratch>/buildA` - executed in 33.0 s, wrote 515946 bytes, audit PASS, sha256
  `4c63d360f8dc808afe6f6db60b240bd9bf65a946273470567da97bcd5d06ae71`.
* 2026-10-08, build B: the same command with `--out <scratch>/buildB` - executed in 26.0 s; the
  notebook written is byte-identical to build A (same sha256), and the 23 files of the two output
  folders are byte-identical and equal to the table of section 2.
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check kohn_sham_states --out
  <scratch>/check1` - a third independent execution (28.6 s): `check kohn_sham_states: PASS - the
  re-executed notebook is byte-identical to Revision/notebooks/kohn_sham_states.ipynb (515946 bytes)`;
  its 23 files equal the table of section 2.
* 2026-10-08, reused output folder with an old-layout build folder: `python -m nbconvert --to notebook
  --execute Revision/notebooks/kohn_sham_states.ipynb --output-dir <scratch>` with `REVISION_NB_OUT=<scratch>/out`,
  where `<scratch>/out/cargo-target/release/deps/old.rlib` and `<scratch>/out/cargo-target/release/old.d`
  existed beforehand (the reviewer's reproduction) - exit status 0, no error or stderr output in the
  executed notebook, `checks of this notebook: 24 passed, 0 failed`, and the final list holds only the
  23 files of section 2, no `cargo-target` path (34.5 s wall time including nbconvert start).
* 2026-10-08, tests of the version of 2026-10-08: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
  - 9 static tests OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 91.7 s (the installed
  versions equal the pins; `check` of all three notebooks in temporary folders is byte-identical);
  `build_notebooks.py audit` PASS (0 problems) for all three notebooks.
* Previous version (notebook sha256 `451587216e92819278076431902f3942bddf752a6bc40ca9f931dd636fee554d`,
  514141 bytes), recorded below:
* 2026-10-08, the reason for the previous version: on Windows the MSVC linker `link.exe` cannot open
  a file whose path is longer than 259 characters (MAX_PATH). With the former build folder
  `<output>/cargo-target` and the default `<output>` of the tool
  (`build/revision_notebooks/kohn_sham_states-XXXXXXXX/`), the solver program
  `cargo-target/release/deps/revision_ks_solver.exe` that the linker writes lies 100 characters
  below the repository folder, so `check` failed with `LNK1104` for a repository folder longer than
  159 characters. Measured with `cargo build --release` of the solver and this folder layout: a
  repository folder of 159 characters links, one of 160 characters fails with `LNK1104` on the
  260-character path of the program. In a copy of the needed files below a folder of 170
  characters, `check kohn_sham_states` without `--out` (as the gate step notebooks-check runs it)
  failed with `LNK1104` with the previous builder and notebook (those of the last commit before this
  change) and passed with the new ones (byte-identical, 514141 bytes, 38.0 s). A review had found the same failure for the notebook
  `lovelock_gkd` (above 148 characters); all three notebooks were changed in the same way. Since then
  the build goes to `<cargo-target>` (sections 2 and 6); the results and the figures are unchanged.
* All runs below with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch folder of
  154 characters.
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out
  <scratch>/kohn_sham_states_A` - executed in 21.7 s, wrote 514141 bytes, audit PASS, sha256
  `451587216e92819278076431902f3942bddf752a6bc40ca9f931dd636fee554d`.
* 2026-10-08, build B: the same command with `--out <scratch>/kohn_sham_states_B` - executed in 21.7 s;
  the notebook written is byte-identical to build A (same sha256), and the 23 files of the two output
  folders are byte-identical and equal to the table of section 2.
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check kohn_sham_states --out
  <scratch>/kohn_sham_states_check1` - a third independent execution (28.9 s): `check kohn_sham_states:
  PASS - the re-executed notebook is byte-identical to Revision/notebooks/kohn_sham_states.ipynb
  (514141 bytes)`; its 23 files equal the table of section 2.
* 2026-10-08, tests: `python -m unittest Revision/tests/test_revision_notebooks.py -v` - 9 static tests OK, 2 skipped; with
  `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 109.1 s (the installed versions equal the pins; `check` of all three notebooks in
  temporary folders is byte-identical).
* 2026-10-08, headless instruction of section 2.5: `python -m nbconvert --to notebook --execute
  Revision/notebooks/kohn_sham_states.ipynb --output-dir <scratch>` with `REVISION_NB_OUT=<scratch>/out` -
  exit status 0, no error output, no stderr output in the executed notebook,
  `checks of this notebook: 24 passed, 0 failed` (nbconvert's own file is not normalised, so it is not
  compared byte for byte; nbconvert itself printed pyzmq's harmless Proactor event-loop warning on the
  console).
* 2026-10-14, the author's coordinates x0..x7 (ordered by the user on 2026-10-14; the record had named them x1..x8 with the hidden direction x8 last): the coordinate definition and section 4.1 (the user's metric with b4; the recorded states are at b4 = 1), the hidden-direction pressure p0, P0 (was p8, P8) in the texts, tables and figures. `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states` - executed in 11.5 s, wrote 516499 bytes, audit PASS, sha256 `42f9baa292ae958407b0e4f64482f11eb39ea6cf4270bcc09609c05fc0c05f82` (the version before: 515946 bytes, `4c63d360f8dc808a...`; builder before `f97211bb1e3c5c70...`); `check kohn_sham_states` - a second independent execution (11.6 s): PASS, the re-executed notebook is byte-identical; the 23 files of the two output folders are byte-identical and equal to the table of section 2 (refreshed from them). The notebook's own checks pass as before (no FAIL line). Tests: `REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py` - 11
  tests OK in 48.6 s (the installed versions equal the pins; `check` of all three notebooks byte-identical). Every run
  with `timeout 423`.
* 2026-10-16, the author's metric with b4(x4) (the user's order of 2026-10-15, "move everything to b4(x4); b4 is never
  1"; the Kohn-Sham record moved to b4 on 2026-10-16: ks-theory.json, the solver with lambda_hat and Vol_7(a4,0), the
  recalibrated couplings, the recomputed canonical matrix and reports): sections 1, 4.1 to 4.4 and 11 of the notebook
  describe the history a4 = H x4, b4 = b4(0) e^((4/3) H x4), the deflation e^(-a4) b4^(1/2) sin^(1/6) z, the growing
  cell volume, that b4 does not enter h_j, the couplings lambda_hat and the a4 and b4 equations; the expected counts
  of the seven reports are 51, 63, 43, 14, 5, 38 and 31 (before 46, 58, 42, 14, 5, 37, 31); no code of the notebook
  changed otherwise. `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states` - executed in 14.6 s,
  wrote 521892 bytes, audit PASS; `check kohn_sham_states` - executed in 14.4 s, PASS, byte-identical; the files of the
  two output folders are byte-identical and equal to the table of section 2 (the nine profile files equal the
  record's). `checks of this notebook: 24 passed, 0 failed`. The test file `Revision/tests/test_revision_notebooks.py`
  (expected counts updated, and the dark-sector count of `ks-history-run.json` corrected from 7 to 8): 9 static
  tests OK, 2 skipped. Every run with `timeout 423`, from the repository root in the working tree on top of commit
  `abfb3c7` (not a fresh clone).
* 2026-10-17, the corrected metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1; the Kohn-Sham record
  recomputed in phase W5 of `HANDOFF.md`: the hidden scale f = e^(-a4) b4^(1/2), kappa = e^(-a4) constant in y, the
  cell volume e^((5/3) a4), the fold joining the two halves of a cell, the new particle numbers 8, 592, 2352 and
  couplings): the builder `src/kohn_sham_states.py` describes the corrected metric (sections 1, 3, 4 and 11 of the
  notebook), solves N = 592 (+lambda_1) and N = 2352 (lambda = 0) instead of N = 136 and 688, checks the N = 8 gap
  against the fold-band level and P3/E = 1/3 of the free N = 2352 gas, and expects the counts
  51, 61, 45, 14, 5, 39, 31 of the seven reports (before 51, 63, 43, 14, 5, 38, 31).
  `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out <scratch>` - executed in 18.8 s, wrote
  494159 bytes, audit PASS; `check kohn_sham_states --out <scratch>` - executed in 20.4 s, PASS, byte-identical;
  the 23 files of the two output folders are byte-identical and equal to the table of section 2 (the nine profile
  files equal the record's). `checks of this notebook: 24 passed, 0 failed`. Every run with `timeout -k 5 423`, from
  the repository root in the working tree (not a fresh clone). That version (notebook sha256
  `5e68de31c1b994f8ded8220e6cf5fdc7996eeb5f7263f20807e7f128974cbb81`, builder sha256
  `a84d512314664155e24b9d7842e412874e92d1ee00e3639ab8b023030f70c7de`) is replaced by the rebuild below.
* 2026-10-17, rebuild after the text corrections of the audit (phase W6 of `HANDOFF.md`): the texts of the
  builder spoke of three input checks of the solver, which prints four (the first is `theory_input_metric_forms`,
  the forms of the corrected metric), and wrote the hidden coordinate as y = ln(sin z)/(6H). Compared with the
  version before (notebook `5e68de31c1b994f8...`), only the sources of four markdown cells changed (cells 0, 2, 8
  and 32: section 1 item 1, the word list of section 3, now y = ln|sin z|/(6H), the introduction of section 6
  and the first item of section 11); no code cell, no output and no metadata changed. Builder sha256
  `1f1e0b29251f6a5bda1631102ef454471d57ac20c2862dba0972ca3ade211d36`; the build tool
  (`99f18fc03902e092...`) and the pins (`ba6c2cab4048282e...`) are unchanged. Two builds and one check, one
  after the other, from the repository root in the working tree (not a fresh clone):
  * build A: `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out <scratch>/kohn_sham_states_buildA`
    - exit status 0, executed in 18.6 s (19.7 s for the command), wrote `Revision/notebooks/kohn_sham_states.ipynb`
    (494302 bytes), audit PASS;
  * build B: the same command with `--out <scratch>/kohn_sham_states_buildB` - exit status 0, executed in 18.8 s
    (19.9 s for the command), wrote 494302 bytes, audit PASS;
  * check: `python Revision/notebooks/tools/build_notebooks.py check kohn_sham_states --out <scratch>/kohn_sham_states_check`
    - exit status 0, executed in 18.5 s (19.5 s for the command): `check kohn_sham_states: PASS - the re-executed
    notebook is byte-identical to Revision/notebooks/kohn_sham_states.ipynb (494302 bytes)`.
  * The notebook written by build A, by build B and by the check has the same sha256
    `028f490cfb7b9fc2db9d7558efff1d9891e68b7021a3edc2c034378b766dacd9` (the step log; the committed notebook and
    `<scratch>/kohn_sham_states_check/kohn_sham_states.ipynb` have it on disk). The output folders compared file by
    file (sha256 and bytes): build A and build B hold the same 23 files (1675672 bytes), byte-identical; the check
    folder holds the same 23 files, byte-identical to them, plus the re-executed notebook; all 23 equal the table of
    section 2 (bytes and sha256; the nine profile files equal the record's), and the 47 read files of section 2
    have the recorded sha256.
  * The executed outputs of the committed notebook: the solver's four input checks PASS (printed indented in
    section 6, `input checks PASS: 4` for each of the ten runs), 24 PASS lines of the notebook's own (counted:
    1 + 1 + 11 + 3 + 8, section 4), no FAIL line, no stderr or error output, `checks of this notebook: 24 passed,
    0 failed`.
  * Tests: `python -m unittest Revision/tests/test_revision_notebooks.py` (light; `REVISION_NOTEBOOKS_FULL` not set)
    - 11 tests in 0.050 s, the 2 full tests skipped; every test passes for this notebook (among them
    `test_cells_equal_builder`, `test_audit_passes`, `test_kohn_sham_record_counts_printed` and the subtest
    `kohn_sham_states` of `test_provenance_records_current_digests`, which finds the sha256 of the notebook, the
    builder and the build tool in this file). The run as a whole reported `FAILED (failures=1, skipped=2)`: the one
    failure is the subtest `dark_sector_hypotheses` of `test_provenance_records_current_digests` (its provenance
    file did not yet record the sha256 `6d8a326a1c7cbff8...` of that notebook, rebuilt in the same step); that file
    is kept by its own step of W6, not by this one.
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
