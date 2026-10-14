# Provenance of the Revision notebook `kohn_sham_states.ipynb`

The Kohn-Sham states of dirac16complex in the author's deflating primordial field.

* Notebook: `Revision/notebooks/kohn_sham_states.ipynb` (33 cells: 19 markdown, 14 code; 516499 bytes;
  sha256 `42f9baa292ae958407b0e4f64482f11eb39ea6cf4270bcc09609c05fc0c05f82`).
* Builder: `Revision/notebooks/src/kohn_sham_states.py`
  (sha256 `66f5a892fa16eab2d0c0a2ba37d099ad7423f993215340d317b499270c08fa37`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08 and, in the author's coordinates x0..x7, on 2026-10-14 (section 7),
  Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/kohn_sham/solver` (`revision_ks_solver`, no external crates)
   with `cargo build --release` into the build folder `<cargo-target>` (section 2) and requires zero
   compiler warnings.
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
5. Tables of the lowest levels (N = 8 at the three slices), of E_KS, HOMO, LUMO, gap, P3/E, Pt/E, P0/E
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
   series along the history; the profiles of N136_lamp1_a10 (n, rho, and p3/rho, p_t/rho, p0/rho); E_KS
   and P3/E, P0/E along the history; the cross-check ratios |new - reference|/tolerance.
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
| `Revision/kohn_sham/ks-theory.json` | `a40cc2e2fa67039b87a30e5835acab57834f8cb83af8bbdc80f726237d128fd2` |
| `Revision/algebra/gammas.json` | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/kohn_sham/results/parameters.json` | `c91041b68b6520c7eec890bd18ffd361b260730c0ee4328eb1d90a8f91c83ebb` |
| `Revision/kohn_sham/results/ground/summary.csv` | `6a4b93a78def3b7db4e91907411c5727293e04024a7bdd11a9e59c6c1acee235` |
| `Revision/kohn_sham/results/ground/emt-integrals.csv` | `0d53384793d54961c64072f11368e7ca28be6ef5d036e66ee87a9545aa8e288c` |
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
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a00.csv` | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a10.csv` | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a20.csv` | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a00.csv` | `436d1e0c9dd30186573fae4d2a78329e6216e6668c73401d2630b98dacbe89bb` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a10.csv` | `1308a5dabd9b9b49f3192fc34c02c06b0160109d3506bdf4aef2edb0edfcf094` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a20.csv` | `842003b260de2d25b18c376f25fa401260c75f2fcdf1ea65c3fb8b22d2dde6b1` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a00.csv` | `8d252e88edb236dc1d09dc60dc11751379465d95f79d788193da083388744526` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a10.csv` | `dd651c2c24af6aeeecfe640d69b71812b7f1d6a5bf3f9b14d11e1c73fd9a9871` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a20.csv` | `ce43e55e92de129631d4fa9097e4a2ba411e12081d9571a442d72a179ba87a5d` |
| `Revision/kohn_sham/reports/ks-crosscheck-table.csv` | `2c92fc2134b97b869bcc27b5380a941321763b3be6cc2e1d17a3efc13b7fb7b6` |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | `21f7736e340618bf5405acb169bf5000f02c47a8f710ce5fd48d8658cbd1224d` |
| `Revision/kohn_sham/reports/ks-theory-python.json` | `d39256e3dd7bee6c203493bd08fd4b2f5f7494af0f07dbf69874706d4eb76784` |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | `59ec76aa382707beff4ef9f8f995ee54cc5f4201d163e67a55fb99e4f150bdd2` |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | `bda728a7d596b3d27b747e92289c9d4309a335041f7fc862bbcbc4c13c749796` |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | `35afda639a6a359937de77fe7ba513333dd09d2fb0ffae64fe010735b76a7982` |
| `Revision/kohn_sham/reports/ks-reference.json` | `b9943071f92f797c5ffa9ce7a174b5fddb4c89e7da742e279b8f7046f783c3cb` |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | `a5d1153a4e4d1b4a50f30313df081dc005f86a5632abc474c48d9b89f49daa3a` |

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/kohn_sham_states` in the repository, ignored by
git), identical in both verified builds and in the `check` run; the Rust build into
`<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-kohn_sham_states-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/figures/figure1_brane_band.png` | 86018 | `ab407444808dc130f25d6ec50b91d3855d7c5b12d97741a33a48a54dd3899e05` |
| `<output>/figures/figure2_profiles.png` | 64672 | `13077a82839687dcb2f5d3fe2c97ae74495f057e47b077014ea77935d4a7eff5` |
| `<output>/figures/figure3_history.png` | 79921 | `a994fc3158df4bf57c763da701d367885ba0d3330718c208d86f917d9dacfdfe` |
| `<output>/figures/figure4_crosscheck.png` | 95136 | `d4d4fd20c1d367ada8e095edb087eb8e08b0f1bb75dd955669345b27d8dfb6be` |
| `<output>/ks_runs/N136_lamp1_a00.csv` | 38057 | `436d1e0c9dd30186573fae4d2a78329e6216e6668c73401d2630b98dacbe89bb` (= record `results/ground/profiles/N136_lamp1_a00.csv`) |
| `<output>/ks_runs/N136_lamp1_a00.json` | 12834 | `35705769279ce9dcd0f521c276c77665cc92f5b9fbf421af4d9771c1b4990768` |
| `<output>/ks_runs/N136_lamp1_a10.csv` | 37922 | `1308a5dabd9b9b49f3192fc34c02c06b0160109d3506bdf4aef2edb0edfcf094` (= record `results/ground/profiles/N136_lamp1_a10.csv`) |
| `<output>/ks_runs/N136_lamp1_a10.json` | 28182 | `c86aed4263691f9414fff4177e06054b4329339d756c077fe800157a70114663` |
| `<output>/ks_runs/N136_lamp1_a10_T20.json` | 17420 | `57ff7767cf5ef073faac1e984c14bee7325867bf15639f940e7ddf624e17da44` |
| `<output>/ks_runs/N136_lamp1_a20.csv` | 38032 | `842003b260de2d25b18c376f25fa401260c75f2fcdf1ea65c3fb8b22d2dde6b1` (= record `results/ground/profiles/N136_lamp1_a20.csv`) |
| `<output>/ks_runs/N136_lamp1_a20.json` | 110731 | `586018ed7b9848b2d4d76bd7cbcdd6eed05090fa5162f6e3e2980cade518350f` |
| `<output>/ks_runs/N688_lam0_a00.csv` | 37158 | `8d252e88edb236dc1d09dc60dc11751379465d95f79d788193da083388744526` (= record `results/ground/profiles/N688_lam0_a00.csv`) |
| `<output>/ks_runs/N688_lam0_a00.json` | 21151 | `74f3da2d7bf421897d1c9d8f4d635a582003cb079024667c01d34fce8b7adaa0` |
| `<output>/ks_runs/N688_lam0_a10.csv` | 37038 | `dd651c2c24af6aeeecfe640d69b71812b7f1d6a5bf3f9b14d11e1c73fd9a9871` (= record `results/ground/profiles/N688_lam0_a10.csv`) |
| `<output>/ks_runs/N688_lam0_a10.json` | 40344 | `3eb83db5a2148590e738e6b52a53e00286ad3a13efceb815c0c0471ad7a84ef6` |
| `<output>/ks_runs/N688_lam0_a20.csv` | 37121 | `ce43e55e92de129631d4fa9097e4a2ba411e12081d9571a442d72a179ba87a5d` (= record `results/ground/profiles/N688_lam0_a20.csv`) |
| `<output>/ks_runs/N688_lam0_a20.json` | 133182 | `a6258f730ef14d595792b3f0aff18fc56c94316a15aac4ccaf5324e6b9602454` |
| `<output>/ks_runs/N8_lam0_a00.csv` | 36974 | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` (= record `results/ground/profiles/N8_lam0_a00.csv`) |
| `<output>/ks_runs/N8_lam0_a00.json` | 6587 | `5c103b42fb6cc027727ab7c68cc6fb4377f51e18719311b6b2b6fe8abad8f208` |
| `<output>/ks_runs/N8_lam0_a10.csv` | 36974 | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` (= record `results/ground/profiles/N8_lam0_a10.csv`) |
| `<output>/ks_runs/N8_lam0_a10.json` | 18455 | `a2a07e5a3c8e4ffda1000707aeee402d62a0c7be1bf2734598ba1e5399b50f21` |
| `<output>/ks_runs/N8_lam0_a20.csv` | 36974 | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` (= record `results/ground/profiles/N8_lam0_a20.csv`) |
| `<output>/ks_runs/N8_lam0_a20.json` | 89961 | `fe2cc57be4f479d57f70962d97f7fb7979c49ab2f144bd1d98ae65bea7711156` |
| `<cargo-target>/` | about 2.8 MB | the Rust build folder (compiler output; not compared) |

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
`.` for the repository itself, or as `<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11, 2026-10-08)

* 2026-10-14 (the author's coordinates; other jobs of this work on the computer): 11.5 s (`build`) and 11.6 s (`check`) of execution.
* Whole notebook, executed by `build_notebooks.py` (current version): 33.0 s (build A), 26.0 s
  (build B) and 28.6 s (`check`) of execution while other work ran on the computer (the previous
  version: 21.7 s to 38.0 s under load, section 7; the first builds of this notebook took 12.2 s to
  12.5 s), including the fresh `cargo build --release` of the solver into `<cargo-target>`
  and the ten solver runs (each under one second when timed separately: 0.06 s for N = 8, 0.5 s for
  N136_lamp1_a10, 0.9 s for N688_lam0_a20).
* Not part of the notebook: the canonical matrix of the solver (`revision_ks_solver all`) took 78.1 s
  on an idle machine and 178.4 s to 244.1 s while other jobs ran (`Revision/kohn_sham/solver/README.md`).

## 6. Side effects

* Writes only into `<output>` and `<cargo-target>` (and the tool writes the notebook file named in section 2). The
  committed record `Revision/kohn_sham/results/` and the reports `Revision/kohn_sham/reports/` are only
  read; the notebook raises an error if `<output>` or `<cargo-target>` would place its files there.
  The crate's own `target/` folder is not used (the build goes to `<cargo-target>`).
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
* Runs `cargo` (needs the Rust toolchain on PATH) and the built solver; no network access during the
  run, no Wolfram Language, no installation.

## 7. Verification record

* 2026-10-08, the reason for the current version (a review of the previous version, two findings):
  (1) the final list of written files left out only `<cargo-target>`, so a folder `<output>/cargo-target`
  left in a reused `<output>` by an earlier version was listed file by file; it is now left out as
  well. (2) On Linux the default `<cargo-target>` lies in the shared `/tmp` under a predictable name,
  and the notebook runs the solver built there; on macOS and Linux the folder is now created private
  and an existing folder that is not private is refused (section 6). In the notebook only the sources
  of cell 1 (section 2.6), cell 5 (the folder set-up) and cell 31 (the final list) changed; every
  output is identical to the previous version.
* 2026-10-08, the private-folder check: the exact code of the builder, run under WSL Ubuntu 24.04 with
  Python 3.12.3 (scratch script), created a new folder with mode 0700, accepted an existing own folder
  of mode 0755, refused folders of mode 0777 and 0775, a symbolic link and a folder of another user
  (`/usr`), and was skipped with `REVISION_NB_CARGO_TARGET` set (21 of 21 cases as expected for the three
  builders). The notebook itself was not executed on Linux.
* Current version, all runs with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch
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
* 2026-10-08, tests of the current version: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
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
  change) and passed with the current ones (byte-identical, 514141 bytes, 38.0 s). A review had found the same failure for the notebook
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
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
