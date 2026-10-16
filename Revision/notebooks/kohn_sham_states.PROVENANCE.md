# Provenance of the Revision notebook `kohn_sham_states.ipynb`

The Kohn-Sham states of dirac16complex in the author's deflating primordial field.

* Notebook: `Revision/notebooks/kohn_sham_states.ipynb` (33 cells: 19 markdown, 14 code; 521892 bytes;
  sha256 `826f987e44e67fbcae4d83257dbc52191dd61f68f8fcce2bedd9e9a88dc01576`).
* Builder: `Revision/notebooks/src/kohn_sham_states.py`
  (sha256 `5c43b073fb0ac2e6de850435bcb80030ac699b92425ad6ee265f20ddd0205392`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, in the author's coordinates x0..x7 on 2026-10-14, and for the author's metric with
  b4(x4) (the Kohn-Sham record moved to b4 on 2026-10-16) on 2026-10-16 (section 7),
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
   0.01206, the solver's lambda_hat, held fixed along the history while Vol_7(a4,0) grows; N = 688, lambda = 0;
   each at a4,0 = 0, 1, 2 of the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)) with profiles, and the thermal state
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
   item 4), |new - reference| is within the table's tolerance (largest ratio 0.2349) and the verdict
   is PASS.
7. Reads the seven committed reports and asserts their counts exactly as their JSON files give them:
   `ks-theory-wolfram.json` 51/51, `ks-theory-python.json` 63/63, `ks-rust-solver.json` 43/43,
   `ks-rust-determinism.json` 14/14, `ks-rust-mermin-roots.json` 5/5, `ks-reference.json` 38/38,
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
| `Revision/kohn_sham/solver/src/analysis.rs` | `09f90e3ece9e2f910670792e6900045c7d7f4634fdc25e0862f42f80ee84ad8d` |
| `Revision/kohn_sham/solver/src/json.rs` | `919be3b192ab81d62deb8429229aa065a50d8fd0f8df6877ac4e413909efdf05` |
| `Revision/kohn_sham/solver/src/main.rs` | `70b20addc1379ede2332e53838a8a5d3a63ad943fe767138e2369f6e47881c8d` |
| `Revision/kohn_sham/solver/src/mermin.rs` | `0be57b4defb8ec056b521c7585138f67d68fb95e3446b8a020b60312cbf6a094` |
| `Revision/kohn_sham/solver/src/model.rs` | `9cc74d27f5d7ab588768b2d842f75fdcb64935891cff0497a505031384e60073` |
| `Revision/kohn_sham/solver/src/report.rs` | `0a770aff24dde0de531d0578e968ab9cad3d5f42b7cda532f7c753633b7ff9c7` |
| `Revision/kohn_sham/solver/src/runs.rs` | `681aed269012d11f6d58904207632280e728723e563d8eeba64a8c12522f9619` |
| `Revision/kohn_sham/solver/src/scf.rs` | `d27060a8db753b8a933946d35eb3918ba3f982b201263435b448a6c702254dd7` |
| `Revision/kohn_sham/solver/src/sha256.rs` | `f44ed328e324b26d9b7c78f530e95be9ff1c88b179026ab4839ab38009e15122` |
| `Revision/kohn_sham/solver/src/shoot.rs` | `39c95fffea255d3977efa9ddadf87131e51c4fd47557bec3a6225fa05bf7d7f4` |
| `Revision/kohn_sham/solver/src/spectrum.rs` | `b52b6997e1418f094e1e7a5cca6064235b6d5ded6bcb534cce149e3a0d3622de` |
| `Revision/kohn_sham/solver/src/theory.rs` | `fdc77ba6601089f98b4bd7a3fff3d11b723687295992620bf29912218e7d393e` |
| `Revision/kohn_sham/ks-theory.json` | `e3e2869216e2744f83a2888067e5ed9599bf2ddff46cfd876da3fb7c729ba0f0` |
| `Revision/algebra/gammas.json` | `c99277bab4793c425bc26849421995fcb5aa8b2c865c0f505686a43654933c3c` |
| `Revision/kohn_sham/results/parameters.json` | `da5756aacb351ecc2691ac159cac7a2d34d6897717b8e877f5d2257d5a8e03a0` |
| `Revision/kohn_sham/results/ground/summary.csv` | `4cf94cfe7c8c372c217b8431d66c0f8dcfeefc86fd791feef6364a3c7fc28156` |
| `Revision/kohn_sham/results/ground/emt-integrals.csv` | `0673ad3e6b3c405a6eaf73310fad176d7129af16aece38b1ac256e4b84376b76` |
| `Revision/kohn_sham/results/thermo/thermodynamics.csv` | `2ff9b680dc62783d1ac4c2d05ea5adde1383261d967a87acf53d6b65eb21b427` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a00.csv` | `dcd43dfe7db6afbdfa1d09a61c8b0700d2d003445375395195c48a09e1231441` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a10.csv` | `7842c9c8d787498096f28fc73061fe0654cd65eb4b676d0728177f7bda64e469` |
| `Revision/kohn_sham/results/ground/levels/N8_lam0_a20.csv` | `8c82fe629f483632683b75e5e5613397fca2051f69fa2e5c238879ba29819c9a` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a00.csv` | `4da5ffd80614190c6c1d28b122106429da9a2c7111fd8d61fc105362045e56e5` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a10.csv` | `259d1e80fad8a71680c2c74adc42778780f854a897bef42513cf91b7c25a5ff6` |
| `Revision/kohn_sham/results/ground/levels/N136_lamp1_a20.csv` | `c02578637a7b705a822dfa7bacd596370b39dac9060ef0e7b7790e19959d1b27` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a00.csv` | `787a3b385ec7b992bc43046a545c65198ef9da3f27df0c6707ce6fc4fc87369b` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a10.csv` | `bbd4ad60d596a6877584eeac2889fb7c3f01902b4589d75c5f6981a7768397e2` |
| `Revision/kohn_sham/results/ground/levels/N688_lam0_a20.csv` | `1cbb17edfb3bbdeac0f4972c8a991d977ca70b45c66ad3273cd1827fb88241af` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a00.csv` | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a10.csv` | `0253807c66eb6bf2092b3c4504b3481c5042c6c82271ddc4e082a75f5151bfac` |
| `Revision/kohn_sham/results/ground/profiles/N8_lam0_a20.csv` | `ea13116a5d3173d73810bf4ecc89ad4005c551bdd68e10180de6b53d279fbe4c` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a00.csv` | `c51693aab17e7750dc25632bc0904e850f016f28aaef191458e0f30ae5e2dfd7` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a10.csv` | `13cc2bc78a6b2daac71ddb8eb43a092c6b78fbddbf95d025d403ac6f8b64bab2` |
| `Revision/kohn_sham/results/ground/profiles/N136_lamp1_a20.csv` | `6ee511544ef4927b8ece0aec566ce68587874433896ac99fc5c722e791c7b518` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a00.csv` | `8d252e88edb236dc1d09dc60dc11751379465d95f79d788193da083388744526` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a10.csv` | `f8208e47dc52a9eb0dccb36ad49fe71d6870b9612509ca476c9a8376a7ae9c27` |
| `Revision/kohn_sham/results/ground/profiles/N688_lam0_a20.csv` | `0b08adef015136c994fedc26654b10115ff02f9f7766364c112183028113b087` |
| `Revision/kohn_sham/reports/ks-crosscheck-table.csv` | `07ba6aef4fc934482b664c86e507466f3926ee74c11b270a46c5902fa2e339a9` |
| `Revision/kohn_sham/reports/ks-theory-wolfram.json` | `304bd5bf10182e07c76db69238c416fae39b9222fd25d3fb76ec901e7d51ebf8` |
| `Revision/kohn_sham/reports/ks-theory-python.json` | `f85b6303bc4812d55dbf7bd77e7efbf87a516cc84ebfe13831eefaebe4ccbe09` |
| `Revision/kohn_sham/reports/ks-rust-solver.json` | `0e9441d30efc74ddf3b6bc5746235b2c1d41a403044e4dc6e88b8de8dc643974` |
| `Revision/kohn_sham/reports/ks-rust-determinism.json` | `3d240a599ffda6a32b478115d306c557aa0ea8ee5d12bc9c99e4bdcfe6bf5048` |
| `Revision/kohn_sham/reports/ks-rust-mermin-roots.json` | `679295e1abe87f296ba31b5883ddd76ae7c26b707bf4b823ac19ab357ae3de06` |
| `Revision/kohn_sham/reports/ks-reference.json` | `a87bb124aaca6697a234d7c8e1b2563b52371d6a8b3ac7775335e558e24fedcc` |
| `Revision/kohn_sham/reports/ks-crosscheck.json` | `796d537884b8879b879e0ec2e810195cace27da36d5fda790d3c4474a1a0c6f1` |

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/kohn_sham_states` in the repository, ignored by
git), identical in both verified builds and in the `check` run; the Rust build into
`<cargo-target>` (the folder named by `REVISION_NB_CARGO_TARGET`, otherwise
`revision-nb-kohn_sham_states-` followed by the first 12 hexadecimal digits of the sha256 of the path of
`<output>`, in the system's temporary folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/figures/figure1_brane_band.png` | 86058 | `1a1b7e298711b8151c62e754cbefaf5a61fdddf269e1545eddbd26e1516dd2ef` |
| `<output>/figures/figure2_profiles.png` | 67608 | `c9b6b365d1d98b7541cacb641e33dbbc70a4aac47100d65b9dff37f6b0213e73` |
| `<output>/figures/figure3_history.png` | 79996 | `0410437a57d38bec80a012add446e0a279be22364026b84606fa78dba7d8ad1a` |
| `<output>/figures/figure4_crosscheck.png` | 95211 | `2955a4d36583423cd96561d5c041e51c3ccbc4442473e18bfc36fd2e95d89471` |
| `<output>/ks_runs/N136_lamp1_a00.csv` | 38052 | `c51693aab17e7750dc25632bc0904e850f016f28aaef191458e0f30ae5e2dfd7` (= record `results/ground/profiles/N136_lamp1_a00.csv`) |
| `<output>/ks_runs/N136_lamp1_a00.json` | 12900 | `79a2bfbf980dc3c9463578868a9917c23057ecc7bc7e7263e0280c992929fde3` |
| `<output>/ks_runs/N136_lamp1_a10.csv` | 38149 | `13cc2bc78a6b2daac71ddb8eb43a092c6b78fbddbf95d025d403ac6f8b64bab2` (= record `results/ground/profiles/N136_lamp1_a10.csv`) |
| `<output>/ks_runs/N136_lamp1_a10.json` | 28248 | `1ac946be4d087da2978fa53064b690ef7365773c53ce4165fb4ba9e106de079a` |
| `<output>/ks_runs/N136_lamp1_a10_T20.json` | 17486 | `884da140ac2053df504bf493698ba0c8f5247a63aca2328ee7c2458584af95cd` |
| `<output>/ks_runs/N136_lamp1_a20.csv` | 38420 | `6ee511544ef4927b8ece0aec566ce68587874433896ac99fc5c722e791c7b518` (= record `results/ground/profiles/N136_lamp1_a20.csv`) |
| `<output>/ks_runs/N136_lamp1_a20.json` | 110797 | `35145744f34ea3813e5e927d015f8a7c2ac0b09b1e66efb7ed092c7f60666d45` |
| `<output>/ks_runs/N688_lam0_a00.csv` | 37158 | `8d252e88edb236dc1d09dc60dc11751379465d95f79d788193da083388744526` (= record `results/ground/profiles/N688_lam0_a00.csv`) |
| `<output>/ks_runs/N688_lam0_a00.json` | 21217 | `755488e42b47e9c0f3ea5b9e138ab6c26a024af3cc8fd44a126f6b72dda351f9` |
| `<output>/ks_runs/N688_lam0_a10.csv` | 37218 | `f8208e47dc52a9eb0dccb36ad49fe71d6870b9612509ca476c9a8376a7ae9c27` (= record `results/ground/profiles/N688_lam0_a10.csv`) |
| `<output>/ks_runs/N688_lam0_a10.json` | 40410 | `a11ae5763a4ed85841c9b879437995ab46c44458ac6a59f41b8e07004f2dffb8` |
| `<output>/ks_runs/N688_lam0_a20.csv` | 37431 | `0b08adef015136c994fedc26654b10115ff02f9f7766364c112183028113b087` (= record `results/ground/profiles/N688_lam0_a20.csv`) |
| `<output>/ks_runs/N688_lam0_a20.json` | 133248 | `17a8638bd4d9e3bb091639d81dd995eb445c75543751fea679f7cfb88c9a6877` |
| `<output>/ks_runs/N8_lam0_a00.csv` | 36974 | `dc0971b3117558c8040f885556b8076b6c61c4b0e8cee38d5f9b8262c87bfe3f` (= record `results/ground/profiles/N8_lam0_a00.csv`) |
| `<output>/ks_runs/N8_lam0_a00.json` | 6653 | `b59f15130d3255819d766ab696753ef51322a067f902dc2af7c4be721924604f` |
| `<output>/ks_runs/N8_lam0_a10.csv` | 37024 | `0253807c66eb6bf2092b3c4504b3481c5042c6c82271ddc4e082a75f5151bfac` (= record `results/ground/profiles/N8_lam0_a10.csv`) |
| `<output>/ks_runs/N8_lam0_a10.json` | 18521 | `0f289afe466be69c1336a13e372dd7d3a3c0c1b02b83f65addcec82a0a161f9f` |
| `<output>/ks_runs/N8_lam0_a20.csv` | 37074 | `ea13116a5d3173d73810bf4ecc89ad4005c551bdd68e10180de6b53d279fbe4c` (= record `results/ground/profiles/N8_lam0_a20.csv`) |
| `<output>/ks_runs/N8_lam0_a20.json` | 90027 | `ef246fb58e97a464c255a15b9821ef2eb622b33248df464b409e1eb7b9ce8441` |
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
  beta 1.333333333333333, Vol7 15875.21366031351, lambda 0.0, N 8.0, T 0.0, tipTheta 0.0, exactFockVariant False),
  lambda_1 = 0.01946, 0.01206, 0.006645 for N = 8, 136, 688.
* Section 7: ten solver runs, each `-> SUCCESS`; eleven PASS lines of the comparison, for example
  `N136_lamp1_a10_equals_record: E_KS = 32.39983783343836, ...`, and for the thermal state
  mu = 0.3247437533489824, E = 33.32682376769655, S = 86.58220633830562.
* Section 8: the N = 8 gap 0.4307337, 0.1703493, 0.0641594 at a4,0 = 0, 1, 2; P3/E = 0.2966, 0.3102,
  0.3265 (N = 136, +lambda_1) and 0.2929, 0.3018, 0.3183 (N = 688, lambda = 0).
* Section 9: `crosscheck_rows_reproduced: 84 rows ... (largest ratio 0.2349)`; the table of the seven
  reports (51 / 63 / 43 / 14 / 5 / 38 / 31 checks, 0 failed).
* Section 10.5: `checks of this notebook: 24 passed, 0 failed` and the 23 files listed above.

No run time and no path of the computer is printed (paths are shown relative to the repository, as
`.` for the repository itself, or as `<output>/...` and `<cargo-target>/...`).

## 5. Measured run time (Windows 11, 2026-10-08)

* 2026-10-16 (the metric with b4(x4); other jobs of this work on the computer): 14.6 s (`build`) and 14.4 s (`check`) of execution.
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
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
