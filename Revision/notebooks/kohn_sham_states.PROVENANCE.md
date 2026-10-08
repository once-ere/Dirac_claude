# Provenance of the Revision notebook `kohn_sham_states.ipynb`

The Kohn-Sham states of dirac16complex in the author's deflating primordial field.

* Notebook: `Revision/notebooks/kohn_sham_states.ipynb` (33 cells: 19 markdown, 14 code; 512116 bytes;
  sha256 `954fa087209146cc70c3e6ded6c0f5537e815c2eaf13d4103b9085a6847095d3`).
* Builder: `Revision/notebooks/src/kohn_sham_states.py`
  (sha256 `7e894415915fa7e433775801ba1d9e4a26801ca8772dbbab9f758aafbc28ebed`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into `<output>/cargo-target` and requires zero compiler warnings.
2. Runs `revision_ks_solver single --m 1 --lambda 0.0 --a4 0.0 --N 8 ... --root <repository>` and prints
   the solver's three input checks (`theory_input_coefficients`: M_eff = m + 0.9375 lambda S,
   v_v = -0.0625 lambda n from `ks-theory.json`; `gamma_fixture_numeric`: the author's gammas of
   `Revision/algebra/gammas.json`; `block_reduction_numeric`: the exact 2 x 2 block reduction) and the
   parameter block of its result; checks H, m, L, dk, v_t, tip angle and the numerics tag against
   `Revision/kohn_sham/results/parameters.json`.
3. Solves nine canonical zero-temperature states (N = 8, lambda = 0; N = 136, lambda = +lambda_1 =
   0.0009298; N = 688, lambda = 0; each at a4,0 = 0, 1, 2) with profiles, and the thermal state
   N136_lamp1_a10_T20 (T = 0.02 m).
4. Compares with the committed record: E_KS, E_band, E_int, iterations, residual, HOMO, LUMO
   (equal floating-point numbers) and the Kohn-Sham gap (within 1e-15 of the larger level, because
   the files record 16 significant digits and the solver forms the gap from unrounded levels) with
   `results/ground/summary.csv`; every level of `results/ground/levels/<id>.csv` equal (the command
   `single` lists, in addition, only empty levels of higher shells); the five EMT integrals with
   `results/ground/emt-integrals.csv`; the nine profile files byte for byte with
   `results/ground/profiles/<id>.csv`; mu, E and the entropy of the thermal state with
   `results/thermo/thermodynamics.csv`, and F = E - T S with its F to 1e-12 relative.
5. Tables of the lowest levels (N = 8 at the three slices), of E_KS, HOMO, LUMO, gap, P3/E, Pt/E, P8/E
   along the history; checks that the N = 8 gap decreases and that P3/E rises and stays below 1/3 for
   N = 136 and 688.
6. Takes the 84 rows of `Revision/kohn_sham/reports/ks-crosscheck-table.csv` that belong to the ten
   states (nine quantities for each zero-temperature state; mu, E and the entropy for the thermal
   state): the column `rust` equals the new value to 16 digits (the gap within the rounding rule of
   item 4), |new - reference| is within the table's tolerance (largest ratio 0.2246) and the verdict
   is PASS.
7. Reads the seven committed reports and asserts their counts exactly as their JSON files give them:
   `ks-theory-wolfram.json` 46/46, `ks-theory-python.json` 58/58, `ks-rust-solver.json` 42/42,
   `ks-rust-determinism.json` 14/14, `ks-rust-mermin-roots.json` 5/5, `ks-reference.json` 37/37,
   `ks-crosscheck.json` 31/31 (0 failed in each; every listed check with verdict PASS).
8. Draws four figures: the brane band of N = 8 at a4,0 = 0, 1, 2 and the Kohn-Sham gap of the three
   series along the history; the profiles of N136_lamp1_a10 (n, rho, and p3/rho, p_t/rho, p8/rho); E_KS
   and P3/E, P8/E along the history; the cross-check ratios |new - reference|/tolerance.
9. Ends with "what this notebook showed, and what it did not show".

The notebook prints 24 PASS lines of its own (and the solver's three input checks, indented) and no
FAIL line; its last code cell prints `checks of this notebook: 24 passed, 0 failed`.

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
| `Revision/kohn_sham/ks-theory.json` | `1bf41d79318a24a4bb0bd6c34f0499c399cc8054e8add69ca08d758c5d55afe3` |
| `Revision/algebra/gammas.json` | `95d8cbdd0682fd30988b4a21fabc2c6b286a1a35c2f9c02c9d91f56bf5b1fd01` |
| `Revision/kohn_sham/results/parameters.json` | `f35216c2bee5b0dc21db6343e640c89f0aebcefab0c6dd6efcec618e0bfae993` |
| `Revision/kohn_sham/results/ground/summary.csv` | `6a4b93a78def3b7db4e91907411c5727293e04024a7bdd11a9e59c6c1acee235` |
| `Revision/kohn_sham/results/ground/emt-integrals.csv` | `24a9cb2037c00d7e6f359c070d1290feaff5ba14397bd89b360d4b4986c13ebb` |
| `Revision/kohn_sham/results/thermo/thermodynamics.csv` | `420b7482dd8dd3552fb63bb23da2eacb18a12048f33ce5fd25894622f1063200` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a00.csv` | `dcd43dfe7db6afbdfa1d09a61c8b0700d2d003445375395195c48a09e1231441` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a10.csv` | `7842c9c8d787498096f28fc73061fe0654cd65eb4b676d0728177f7bda64e469` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a20.csv` | `8c82fe629f483632683b75e5e5613397fca2051f69fa2e5c238879ba29819c9a` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a00.csv` | `f67885312d5b48552c7c7cb0b1ef2b355ab24ee8d0138b9136c2fd31a5959d95` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a10.csv` | `d1f3727674518ffa35ec7e7b6528ed758f15120243823f6ff18d57baafc1df5c` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a20.csv` | `49c505b48f5d0c3dd367fed08de26e2662a0f978bf1faeefc6d6a36721812ef1` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a00.csv` | `787a3b385ec7b992bc43046a545c65198ef9da3f27df0c6707ce6fc4fc87369b` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a10.csv` | `bbd4ad60d596a6877584eeac2889fb7c3f01902b4589d75c5f6981a7768397e2` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a20.csv` | `1cbb17edfb3bbdeac0f4972c8a991d977ca70b45c66ad3273cd1827fb88241af` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a00.csv` | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a10.csv` | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a20.csv` | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a00.csv` | `bf2488b59b4734b50a568a6cddd15bc608d69377ce6a199fa048ea6da233b41d` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a10.csv` | `5fb30971555a9e4731dfce33206597750db276f92745c9f210b76c4d0a3d863e` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a20.csv` | `e87d3edf011bd9dbb93cdbadfe7a8a697ebf2edbfa088ee7d3e3251b23a38cc2` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a00.csv` | `6ba8dab2edb88eac7b526527e1eb46e2f0ac0b2a980868e3cd6c6c39958920a5` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a10.csv` | `f17db2b22ef69816f0bdf3de075bd0aee8cbe68c285c21b864dad780734f49b0` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a20.csv` | `49a5d1cb855dc7e5c2c9788cabd40213fbe91057672314facdf3af61564c5889` |
| `Revision/kohn_sham/reports/ks-crosscheck-table.csv` | `69dd7a96e622900155678c876fe10669008f8f0bcd8218a28a43b969103d4dba` |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | `5d803af6b270bc7dd93120907c13c28e855c4ba351ccdc3b411d7f8086112ae6` |
| `Revision/kohn_sham/reports/ks-theory-python.json` | `7ae5c6be4dbaf167093a7c0799d9c102d3a7d1d17ec93311a1b17ea5bc26cf9c` |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | `63ab1f1fe69fe7809b0690260b76f9bd4b0e7cb781c65af412e8bd82b14a436a` |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | `a55c6866eda66ba754798f3b233203e16b31b01eb11220cc45c3e1de6305b679` |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | `35afda639a6a359937de77fe7ba513333dd09d2fb0ffae64fe010735b76a7982` |
| `Revision/kohn_sham/reports/ks-reference.json` | `5eb5f0ada9d392a4cf01d672ed00d2a174439bfec196a24dbce3965c2c559c35` |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | `f0d918e923847703b761d5cd0eae440df877a5f0671f6dadfa9e9110206490ea` |

Written, all into the output folder `<output>` (the folder named by `REVISION_NB_OUT`, otherwise
`build/revision_notebooks/kohn_sham_states` in the repository, ignored by git); identical in both
verified builds:

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/figures/figure1_brane_band.png` | 86018 | `ab407444808dc130f25d6ec50b91d3855d7c5b12d97741a33a48a54dd3899e05` |
| `<output>/figures/figure2_profiles.png` | 64480 | `19a9faee574767cb041a3dce43f6f6a429c507baf6fdf1da3dbf5c95d7faafb7` |
| `<output>/figures/figure3_history.png` | 80021 | `bb156c2d7e822b6d4e0dfabce155e6ced1008fb62465da5d1ba9ed2491cb7623` |
| `<output>/figures/figure4_crosscheck.png` | 95134 | `da9d08900b2cf2d1966e45b8174121d87c7822e9aaec28b9c8144ca2c9129d7f` |
| `<output>/ks_runs/N136_lamp1_a00.csv` | 38057 | `bf2488b59b4734b50a568a6cddd15bc608d69377ce6a199fa048ea6da233b41d` (= record `results/ground/profiles/N136_lamp1_a00.csv`) |
| `<output>/ks_runs/N136_lamp1_a00.json` | 12834 | `7189a015430b2ddfdd6a2a17a62377871ffe6b3017709b779be77e80744cdee0` |
| `<output>/ks_runs/N136_lamp1_a10.csv` | 37922 | `5fb30971555a9e4731dfce33206597750db276f92745c9f210b76c4d0a3d863e` (= record `results/ground/profiles/N136_lamp1_a10.csv`) |
| `<output>/ks_runs/N136_lamp1_a10.json` | 28182 | `1857f491a98d06d091c2f5d30feeb31ed7e164ec2cc68d057aebd42788573361` |
| `<output>/ks_runs/N136_lamp1_a10_T20.json` | 17420 | `6f34491c9d677a94a5e39b26007291b61f05498f4ee352237c28d88fec9b7aa4` |
| `<output>/ks_runs/N136_lamp1_a20.csv` | 38032 | `e87d3edf011bd9dbb93cdbadfe7a8a697ebf2edbfa088ee7d3e3251b23a38cc2` (= record `results/ground/profiles/N136_lamp1_a20.csv`) |
| `<output>/ks_runs/N136_lamp1_a20.json` | 110731 | `9c74d1cbd8f15f82bb5ac9aca7968190c0fd912f3048910ed3be06a0a1a8975e` |
| `<output>/ks_runs/N688_lam0_a00.csv` | 37158 | `6ba8dab2edb88eac7b526527e1eb46e2f0ac0b2a980868e3cd6c6c39958920a5` (= record `results/ground/profiles/N688_lam0_a00.csv`) |
| `<output>/ks_runs/N688_lam0_a00.json` | 21151 | `9ac4dd738b1aebe3cfef5c461b0d748d75ca18818bbed3a0fcbfacfd33ac2493` |
| `<output>/ks_runs/N688_lam0_a10.csv` | 37038 | `f17db2b22ef69816f0bdf3de075bd0aee8cbe68c285c21b864dad780734f49b0` (= record `results/ground/profiles/N688_lam0_a10.csv`) |
| `<output>/ks_runs/N688_lam0_a10.json` | 40344 | `a45e1528cf61829320dfd060830073645f4eca9bb5110adf72a165f4d4971849` |
| `<output>/ks_runs/N688_lam0_a20.csv` | 37121 | `49a5d1cb855dc7e5c2c9788cabd40213fbe91057672314facdf3af61564c5889` (= record `results/ground/profiles/N688_lam0_a20.csv`) |
| `<output>/ks_runs/N688_lam0_a20.json` | 133182 | `ad4637d417b22ae9aa55f6a163de3f2ffb8143a46b2c633b82076ab9a23a073e` |
| `<output>/ks_runs/N8_lam0_a00.csv` | 36974 | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` (= record `results/ground/profiles/N8_lam0_a00.csv`) |
| `<output>/ks_runs/N8_lam0_a00.json` | 6587 | `399661ef140477f1d36e0bc4f110863cba0e62feed529b23a2cc972547abfa8d` |
| `<output>/ks_runs/N8_lam0_a10.csv` | 36974 | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` (= record `results/ground/profiles/N8_lam0_a10.csv`) |
| `<output>/ks_runs/N8_lam0_a10.json` | 18455 | `4de1b5e4507440ea71b2c413850af9909b02fff55a0a43b7a5bd542ad66bf79e` |
| `<output>/ks_runs/N8_lam0_a20.csv` | 36974 | `a26b1acc40eb20783a077f41a917fda8e5c96cb0536624e270d56d3d7b5e923e` (= record `results/ground/profiles/N8_lam0_a20.csv`) |
| `<output>/ks_runs/N8_lam0_a20.json` | 89961 | `02e0b82557cc4eedf4e7325b07527de3411e988535643fb4911c4b4048853681` |
| `<output>/cargo-target/` | | the Rust build folder (compiler output; not compared) |

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

* Section 5: `exit status: 0`, `compiler warnings: 0`.
* Section 6: the solver's three indented `PASS` input checks, `-> SUCCESS, exit status 0, input checks
  PASS: 3, other messages: 0`, the parameter block (H 1.0, m 1.0, L 3.0, dk 0.25, v_t 1.0, a4 0.0,
  lambda 0.0, N 8.0, T 0.0, tipTheta 0.0, exactFockVariant False), lambda_1 = 0.01946, 0.0009298,
  0.0001846 for N = 8, 136, 688.
* Section 7: ten solver runs, each `-> SUCCESS`; eleven PASS lines of the comparison, for example
  `N136_lamp1_a10_equals_record: E_KS = 32.39294915318298, ...`, and for the thermal state
  mu = 0.3246592752780658, E = 33.31968443444271, S = 86.5540070269009.
* Section 8: the N = 8 gap 0.4307337, 0.1703493, 0.0641594 at a4,0 = 0, 1, 2; P3/E = 0.2966, 0.3101,
  0.3270 (N = 136, +lambda_1) and 0.2929, 0.3018, 0.3183 (N = 688, lambda = 0).
* Section 9: `crosscheck_rows_reproduced: 84 rows ... (largest ratio 0.2246)`; the table of the seven
  reports (46 / 58 / 42 / 14 / 5 / 37 / 31 checks, 0 failed).
* Section 10.5: `checks of this notebook: 24 passed, 0 failed` and the 23 files listed above.

No run time and no path of the computer is printed (paths are shown relative to the repository, as
`.` for the repository itself, or as `<output>/...`).

## 5. Measured run time (Windows 11, 2026-10-08)

* Whole notebook, executed by `build_notebooks.py`: 12.5 s (build A) and 12.2 s (build B) of
  execution, including the fresh `cargo build --release` of the solver into `<output>/cargo-target`
  and the ten solver runs (each under one second when timed separately: 0.06 s for N = 8, 0.5 s for
  N136_lamp1_a10, 0.9 s for N688_lam0_a20).
* Not part of the notebook: the canonical matrix of the solver (`revision_ks_solver all`) took 78.1 s
  on an idle machine and 178.4 s to 244.1 s while other jobs ran (`Revision/kohn_sham/solver/README.md`).

## 6. Side effects

* Writes only into `<output>` (and the tool writes the notebook file named in section 2). The
  committed record `Revision/kohn_sham/results/` and the reports `Revision/kohn_sham/reports/` are only
  read; the notebook raises an error if `<output>` would place its files there. The crate's own
  `target/` folder is not used (the build goes to `<output>/cargo-target`).
* Runs `cargo` (needs the Rust toolchain on PATH) and the built solver; no network access during the
  run, no Wolfram Language, no installation.

## 7. Verification record

* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build kohn_sham_states --out
  <scratch>/ksFinalA` - executed in 12.5 s, wrote 512116 bytes, audit PASS, sha256
  `954fa087209146cc70c3e6ded6c0f5537e815c2eaf13d4103b9085a6847095d3`.
* 2026-10-08, build B: the same command with `--out <scratch>/ksFinalB` - executed in 12.2 s; the
  notebook written is byte-identical to build A (same sha256), and the 23 files of the two output
  folders are byte-identical (table of section 2).
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check kohn_sham_states --out
  <scratch>/ksCheck1` - a third independent execution (12.4 s): `check kohn_sham_states: PASS - the
  re-executed notebook is byte-identical to Revision/notebooks/kohn_sham_states.ipynb (512116 bytes)`.
* 2026-10-08, tests: `python -m unittest Revision/tests/test_revision_notebooks.py -v` - 8 static tests
  OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 10 tests OK in 29.8 s (the installed versions equal
  the pins; `check` re-executions of `lovelock_gkd` and `kohn_sham_states` in temporary folders are
  byte-identical to the committed notebooks; run concurrently with the headless run below).
* 2026-10-08, headless instruction of section 2.5: `python -m nbconvert --to notebook --execute
  Revision/notebooks/kohn_sham_states.ipynb --output-dir <scratch>` with `REVISION_NB_OUT=<scratch>` -
  exit status 0, no error output, no stderr output in the executed notebook,
  `checks of this notebook: 24 passed, 0 failed` (nbconvert's own file is not normalised, so it is not
  compared byte for byte; nbconvert itself printed pyzmq's harmless Proactor event-loop warning on the
  console).
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
