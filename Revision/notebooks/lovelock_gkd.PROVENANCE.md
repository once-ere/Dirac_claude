# Provenance of the Revision notebook `lovelock_gkd.ipynb`

The Lovelock tensors of the author's metric with the generalized Kronecker delta (GKD).

* Notebook: `Revision/notebooks/lovelock_gkd.ipynb` (37 cells: 21 markdown, 16 code; 467602 bytes;
  sha256 `5413520280394427cee4847c6a3a8ade3f0e0d60f64a17b28faeafd77696050f`).
* Builder: `Revision/notebooks/src/lovelock_gkd.py`
  (sha256 `170391a60b35d18c17b6a6abb8d776e14645f928125dc6b5f7b479468458d55d`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, in the author's coordinates x0..x7 on 2026-10-14, for general b4(x4) (b4 is
  never 1) on 2026-10-16, and for the corrected primordial metric of 2026-10-16 (version 2) on 2026-10-17 (section 7),
  Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/gkd_lovelock/code` (`lovelock_gkd`, pure Rust, no
   dependencies) with `cargo build --release` into the build folder `<cargo-target>` (section 2) and
   requires zero compiler warnings.
2. Runs `lovelock_gkd print-config` and checks that the recited metric equals, character for character apart from
   spaces, the corrected metric `g = ...` of `Revision/SPEC.md` section 1.
3. Defines two independent Python versions of the GKD (the rule: distinct indices, same set, sign of
   the permutation; and the author's determinant `Det[Outer[delta, lower, upper]]` by the Leibniz
   formula) and compares them exhaustively for all pairs of index lists of length 1, 2, 3 over eight
   values (64, 4096, 262144 pairs): 0 mismatches; non-zero counts 8, 112, 2016 = 8!/(8-p)! p!;
   +1 / -1 / 0 counts equal to `wolfram-gkd-report.json` `measurements.gkdComparison`, pair and
   mismatch counts equal to the rows p = 1, 2, 3 of `gkd-selftest.json`; the two values of
   `gkdSelfCheck` in `lovelock-report.json` are reproduced.
4. Runs `lovelock_gkd lovelock --output <output>/lovelock_run --brute-force-k2` (the command of the
   committed record): 27 checks, all PASS; the four files written are byte-identical to the committed
   `Revision/gkd_lovelock/results/` files.
5. Tables of the four independent diagonal components of P_(k) (k = 1, 2, 3) and of L_(k); every off-diagonal
   component of P_(k) is zero, x1 = x2 = x3 and x0 = x5 = x6 = x7 (the corrected metric of 2026-10-16, version 2).
   Exact Python re-checks (fractions, no rounding) for general a4(x4) and b4(x4) and every real z, with all 14
   symbols of the program (H, a4' ... a4'''', E = e^a4, W = (sin^2 z)^(1/12), C = cot z, Q = b4^(1/2), b4' ... b4'''',
   G = sign(cot z)): the trace identity for k = 1, 2, 3 (L_(k) parsed with its e^a4 and b4 terms), -P_(1)/4 equals
   `einsteinMixed` of `curvature.json` in all 64 components, A_(k)^hh = sqrt|det g| g^hh P_(k)^h_h with
   sqrt|det g| = G C E^-1 Q^4 W^3 = e^-a4 b4^2 |cot z| (sin^2 z)^(1/4). The normalised E_(k) = -P_(k)/2^(k+1): every
   term of its four diagonal components is a ratio of b4 derivatives to powers of b4 times k^n = e^(2 n a4)/b4^n, so
   E_(k) is a polynomial in H, a4', a4'', u = b4'/b4, v = u' and k = e^(2 a4)/b4; these polynomials equal those of
   `Revision/field_equations_a4/a4-equations.json` (key `lovelockTensors`) exactly, and E^x0_x0 = E^x5_x5; a table for
   k = 1, 2. E^x1_x1 - E^x5_x5 has terms without a4'', u or v (for k = 1: -2 (a4')^2 + 3 H^2 k). On the history of the
   Kohn-Sham record (a4' = H, a4'' = 0, u = 4H/3, v = 0) the values are polynomials in k, and with the author's
   weights alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152) the tensors give exactly the record's
   `historySource_kappaT_minus_Lam`: minus_rho = 121/432 + 161 k/24 - 9 k^2/16, p3 = -5359/3888 + 1601 k/216 -
   9 k^2/16, pt = p0 = -497/144 + 79 k/16 (H = 1).
6. Reads the five committed records and asserts their counts exactly as their JSON files give them:
   `lovelock-report.json` checkCount 27, failedCheckCount 0, verdict SUCCESS;
   `gkd-selftest.json` 9 rows, 0 mismatches, verdict SUCCESS (18043520 pairs in total);
   `python-lovelock-report.json` checkCount 56, failedCheckCount 0, verdict SUCCESS;
   `wolfram-gkd-report.json` checkCount 29 of expectedCheckCount 29, failedCheckCount 0, verdict SUCCESS;
   and that the input sha256 recorded by the sympy verifier (curvature.json, lovelock-tensors.json)
   and by the Wolfram verifier (curvature.json, lovelock-report.json, lovelock-tensors.json) equal the
   sha256 of the files the program has just written.
7. Draws three figures: scale factors of the directions on the history (a4 = x4, b4 = e^(4 x4/3), b4(0) = 1 for
   the picture: e^a4, f = e^-a4 b4^(1/2), the proper 7-volume e^-a4 b4^2) and the hidden-direction functions over one
   period of z; the diagonal components of E_(1), E_(2), E_(3) against a4'/H on the family b4 = b4(0) e^(4 a4/3) at
   k = 1, a4'' = 0 (the history a4' = H marked) and a4'' = 0.5 H^2; the work of the Lovelock sums (8^(4k+2) index lists, leaves, GKD
   evaluations, from the new report's counters) and the fraction of non-zero GKD values.
8. Ends with "what this notebook showed, and what it did not show".

The notebook prints 47 PASS lines of its own (and the program's 27, indented in its output) and no FAIL
line; its last code cell prints `checks of this notebook: 47 passed, 0 failed` (45 on 2026-10-16, 40 before).

## 2. Files read and written

Read (sha256 at the time of the verified builds):

| file | sha256 |
| --- | --- |
| `Revision/SPEC.md` | (only its existence is used, to find the repository) |
| `Revision/README.md` | (not pinned: the file changes as the record grows; the notebook only needs the author's metric text to occur in it and checks that it does) |
| `Revision/gkd_lovelock/code/Cargo.toml` | `c6719ffae8040c42034a903b7cf2aefbc2124fee7dd6750de0c455d7cb653d70` |
| `Revision/gkd_lovelock/code/Cargo.lock` | `41e4efb7365fc3c818a2a7d18ffd214d11d6856dd4f62ea970ca2a4e39115250` |
| `Revision/gkd_lovelock/code/src/geometry.rs` | `04bcabfa99ffe3a732aa12ef3d5554874cba0a1bcb821cf8e36bb05812efbc22` |
| `Revision/gkd_lovelock/code/src/gkd.rs` | `3be0169f6c03d0d6afbd8361e6d80c5b802defb0878ddc2ffeb62e3dde106dd4` |
| `Revision/gkd_lovelock/code/src/lib.rs` | `cccd024b5a559ce306d770e4a2674a1bc3eb7b6cf00e05dc0858fb3cc4991da6` |
| `Revision/gkd_lovelock/code/src/lovelock.rs` | `1ce0c7e3a16acd1509890b7f7029cd9e258e72d4816235a0df4bf2f99f1acd1b` |
| `Revision/gkd_lovelock/code/src/main.rs` | `a5a5c68115dd8e6b18dd6b7e123712a1fd6edc4c8141ece827785c4768b4d5e9` |
| `Revision/gkd_lovelock/code/src/output.rs` | `668921a2cf0ce4f19371981702794bcb3934945ffa9faed1f6a77c0254023759` |
| `Revision/gkd_lovelock/code/src/poly.rs` | `15a6ec3b0d3cc3d6531a409830f3ee95f13a53ed690ec863c59237861dc8773a` |
| `Revision/gkd_lovelock/code/src/rational.rs` | `a8e9b54a655dc9e1d15ef0f4203cb55eda168efd93e52b337573fb6d8c5384ba` |
| `Revision/gkd_lovelock/results/curvature.json` | `67b74b6d3cf92844a8eb48d28e73e5e3481c1f55a213c9c5c14f25adc1a39d47` |
| `Revision/gkd_lovelock/results/lovelock-tensors.json` | `611a60543bcf36261e54d1304a2eb216efc39596ba2ad8fc33c353a740787343` |
| `Revision/gkd_lovelock/results/lovelock-components.md` | `e245b4fa52d2dae64b673805c9adb8a4d6bc485de8899881af8db7e4c4dac51f` |
| `Revision/gkd_lovelock/results/lovelock-report.json` | `b350e20e49f9e4cafbd097a1d975b8fc673932050893988a9f867bbcfcf38811` |
| `Revision/gkd_lovelock/results/gkd-selftest.json` | `6cd72bd8d5d8d2f7acb4825ed0a975a26aaad343e323b9c96f6d1fc4f294d1dc` |
| `Revision/gkd_lovelock/results/python-lovelock-report.json` | `eea271208d08493a201bb123ebf0d2380388261741be9a903a69bb92f8b6407a` |
| `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | `98a5e3c830ed22beaf61510f351db44a1bcfddce31d7c696763366dcaf78c2c1` |
| `Revision/field_equations_a4/a4-equations.json` | `fba6e3af9c56f5e6c61819762a1fccfede5f6ab4875f3e4fa736d2afb13df72d` |

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/lovelock_gkd` in the repository, ignored by
git), identical in both verified builds and in the `check` runs; the Rust build into `<cargo-target>`
(the folder named by `REVISION_NB_CARGO_TARGET`, otherwise `revision-nb-lovelock_gkd-` followed by the
first 12 hexadecimal digits of the sha256 of the path of `<output>`, in the system's temporary
folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/lovelock_run/curvature.json` | 39730 | `67b74b6d3cf92844a8eb48d28e73e5e3481c1f55a213c9c5c14f25adc1a39d47` (= record) |
| `<output>/lovelock_run/lovelock-tensors.json` | 164399 | `611a60543bcf36261e54d1304a2eb216efc39596ba2ad8fc33c353a740787343` (= record) |
| `<output>/lovelock_run/lovelock-components.md` | 56688 | `e245b4fa52d2dae64b673805c9adb8a4d6bc485de8899881af8db7e4c4dac51f` (= record) |
| `<output>/lovelock_run/lovelock-report.json` | 5005 | `b350e20e49f9e4cafbd097a1d975b8fc673932050893988a9f867bbcfcf38811` (= record) |
| `<output>/figures/figure1_scale_factors.png` | 83819 | `3cc0a5ca2cde8a7450e1bc71eed71234835e61b8235e60d5d41e05ed3b630d0c` |
| `<output>/figures/figure2_lovelock_components.png` | 117175 | `8c21702537eda34d65bf4ee545e9e7e2a75e2d31698611e69ac4ff36fcd1b5a6` |
| `<output>/figures/figure3_gkd_work.png` | 57462 | `73709218be38a986eb3d5d9a2d0bf4688e7e37e982012ce4ff74a83021c4a3e1` |
| `<cargo-target>/` | about 2.6 MB | the Rust build folder (compiler output; not compared) |

The tool writes `Revision/notebooks/lovelock_gkd.ipynb` (`build`) or `<output>/lovelock_gkd.ipynb`
(`check`). With `REVISION_NB_LONG=1` (not used for the committed notebook) the notebook also writes
`<output>/gkd_selftest/gkd-selftest.json` and compares it with the record.

## 3. How to run it

The complete, self-contained instructions for Windows 11 (PowerShell), macOS on Apple silicon (zsh)
and Linux (bash) are section 2 of the notebook: install Git, Python 3.12 or newer and Rust (rustup);
`git clone https://github.com/once-ere/Dirac_claude.git`; create a private environment OUTSIDE the
repository (`python -m venv $HOME\venvs\revision-nb` on Windows, `python3 -m venv ~/venvs/revision-nb`
on macOS and Linux); install the pins with `<environment python> -m pip install -r
Revision/notebooks/requirements.txt`; then either

```text
<environment python> -m jupyterlab Revision/notebooks/lovelock_gkd.ipynb
```

(choose the kernel "Python 3 (ipykernel)", press Shift+Enter cell by cell or Run All Cells), or
headless

```text
<environment python> -m nbconvert --to notebook --execute Revision/notebooks/lovelock_gkd.ipynb --output-dir ../revision-nb-runs
```

or, to rebuild and compare with the committed file (from the repository root):

```text
<environment python> Revision/notebooks/tools/build_notebooks.py build lovelock_gkd --out <new folder>
<environment python> Revision/notebooks/tools/build_notebooks.py check lovelock_gkd --out <new folder>
```

`python -m jupyter ...` is not used: it fails where the jupyter executables are not on PATH.

## 4. Expected output

* Section 5: `exit status: 0`, `compiler warnings: 0`.
* Section 6: the program's six configuration lines; the metric line begins
  `{{E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2,0,0,0,0,0,0,0},{0,E^(2 a4[x4]),...` (the corrected primordial metric of
  2026-10-16, version 2; before it the line began `{{Cot[6 H x0]^2,0,...` (the metric of 2026-10-14)).
* Section 7: the table `p = 1, 2, 3`: pairs 64 / 4096 / 262144, mismatches 0, +1: 8 / 56 / 1008,
  -1: 0 / 56 / 1008, 0: 56 / 3984 / 260128; the committed self-test table (9 rows, verdict SUCCESS).
* Section 8.1: 27 PASS lines of the program, `check_count=27`, `failed_check_count=0`,
  `lovelock: SUCCESS (<t> s)`, and four `identical to the record` lines.
* Section 8.4: the lines `k<k>_depends_on_b4_ratios_and_k`, `k<k>_equals_a4_equations_record` and
  `k<k>_hidden_equals_extra_times_python`; the table of E_(1), E_(2) in H, a4', a4'', u, v, k; `E_(3): x0x0 17 terms,
  x1x1 23 terms, x4x4 8 terms, x5x5 17 terms`; the three `k<k>_space_differs_from_extra_times` lines; the values on the
  history as polynomials in k; and `kappa T - Lambda delta, minus_rho from the Rust tensors: (121/432) k^0 + (161/24)
  k^1 + (-9/16) k^2` (p3, pt, p0 likewise), equal to the record's `historySource_kappaT_minus_Lam`.
* Section 9: the table of the four reports (27 / 9 rows / 56 / 29 checks, 0 failed, SUCCESS).
* Section 10.4: `checks of this notebook: 47 passed, 0 failed` and the seven files listed above.

Run times printed by the program are masked as `<t>`; no path of the computer is printed (paths are
shown relative to the repository or as `<output>/...` and `<cargo-target>/...`). The printed text
does not depend on where `<output>` and `<cargo-target>` are, so the notebook is byte-identical with
or without `REVISION_NB_CARGO_TARGET`.

## 5. Measured run time (Windows 11, 2026-10-08)

* 2026-10-17 (the corrected metric; other jobs of this work on the computer, among them the Kohn-Sham reference
  with 20 processes): 30.6 s (`build`) and 29.6 s (`check`) of execution.
* 2026-10-16 (general b4; other jobs of this work on the computer): 22.0 s (`build`) and 21.9 s (`check`) of execution.
* 2026-10-14 (the author's coordinates; other jobs of this work on the computer): 24.1 s (`build`) and 20.6 s (`check`) of execution.
* Whole notebook, executed by `build_notebooks.py` (current version): 24.7 s (build A), 22.8 s
  (build B) and 21.1 s (`check`) of execution, 26.9 s wall time for build A including kernel start.
  The previous version took 24.8 s to 30.5 s in its builds and checks (section 7).
* Inside it: the fresh `cargo build --release` about 3 s; `lovelock --brute-force-k2` 13.6 s as the
  program reports it in a separate run (4.4 s without `--brute-force-k2`); the exhaustive Python GKD
  comparison a few seconds.
* Not part of the normal run: the program's complete `gkd-selftest --exhaustive-max 4` took 697.5 s
  (11 min 37.6 s wall time, measured while other jobs ran) and wrote a `gkd-selftest.json`
  byte-identical to the record; this is why it runs only with `REVISION_NB_LONG=1`.

## 6. Side effects

* Writes only into `<output>` and `<cargo-target>` (and the tool writes the notebook file named in
  section 2). The committed record `Revision/gkd_lovelock/results/` is only read; the notebook raises
  an error if `<output>` or `<cargo-target>` would place the program's files there. The crate's own
  `target/` folder is not used (the build goes to `<cargo-target>`).
* By default `<cargo-target>` is a new folder of about 2.6 MB in the system's temporary folder for
  every new `<output>` (every `build` and `check` of the tool uses a new `<output>`); nothing deletes
  it, it can be deleted by hand. It is placed there, short and outside the repository, because on
  Windows the MSVC linker `link.exe` cannot open a file whose path is longer than 259 characters
  (MAX_PATH): with the former build folder `<output>/cargo-target`, the default `<output>` of the tool
  (`build/revision_notebooks/lovelock_gkd-XXXXXXXX/`) and a repository folder longer than 148
  characters (the part of the path below the repository folder is 111 characters), the library file `liblovelock_gkd-<16 hexadecimal digits>.rlib` that the linker must open
  had a path of 260 or more characters, and `check` failed with `LNK1104` (section 7).
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
* Runs `cargo` (needs the Rust toolchain on PATH) and the built program; no network access during the
  run, no Wolfram Language, no installation.

## 7. Verification record

* 2026-10-08, the reason for the current version (a review of the previous version, two findings):
  (1) the final list of written files left out only `<cargo-target>`, so a folder `<output>/cargo-target`
  left in a reused `<output>` by an earlier version was listed file by file (reproduced by the
  reviewer); it is now left out as well. (2) On Linux the default `<cargo-target>` lies in the shared
  `/tmp` under a predictable name, and the notebook runs the program built there; on macOS and Linux
  the folder is now created private and an existing folder that is not private is refused (section 6).
  In the notebook only the sources of cell 1 (section 2.6), cell 5 (the folder set-up) and cell 33
  (the final list) changed; every output is identical to the previous version.
* 2026-10-08, the private-folder check: the exact code of the builder, run under WSL Ubuntu 24.04 with
  Python 3.12.3 (scratch script), created a new folder with mode 0700, accepted an existing own folder
  of mode 0755, refused folders of mode 0777 and 0775, a symbolic link and a folder of another user
  (`/usr`), and was skipped with `REVISION_NB_CARGO_TARGET` set (21 of 21 cases as expected for the three
  builders). The notebook itself was not executed on Linux.
* Current version, all runs with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch
  folder:
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build lovelock_gkd --out
  <scratch>/buildA` - executed in 24.7 s, wrote 412223 bytes, audit PASS, sha256
  `4b48dba289e5abc40cafd083426a157fe083d25384a33e8dffc6cf6c68189076`.
* 2026-10-08, build B: the same command with `--out <scratch>/buildB` - executed in 22.8 s; the
  notebook written is byte-identical to build A (same sha256), and the seven files of the two output
  folders are byte-identical and equal to the table of section 2.
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check lovelock_gkd --out
  <scratch>/check1` - a third independent execution (21.1 s): `check lovelock_gkd: PASS - the
  re-executed notebook is byte-identical to Revision/notebooks/lovelock_gkd.ipynb (412223 bytes)`; its
  seven files equal the table of section 2.
* 2026-10-08, reused output folder with an old-layout build folder: `python -m nbconvert --to notebook
  --execute Revision/notebooks/lovelock_gkd.ipynb --output-dir <scratch>` with `REVISION_NB_OUT=<scratch>/out`,
  where `<scratch>/out/cargo-target/release/deps/old.rlib` and `<scratch>/out/cargo-target/release/old.d`
  existed beforehand (the reviewer's reproduction) - exit status 0, no error or stderr output in the
  executed notebook, `checks of this notebook: 40 passed, 0 failed`, and the final list holds only the
  seven files of section 2, no `cargo-target` path (31.0 s wall time including nbconvert start).
* 2026-10-08, tests of the current version: `python -m unittest Revision/tests/test_revision_notebooks.py -v`
  - 9 static tests OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 91.7 s (the installed
  versions equal the pins; `check` of all three notebooks in temporary folders is byte-identical);
  `build_notebooks.py audit` PASS (0 problems) for all three notebooks.
* Previous version (notebook sha256 `e4066a453826082a0e0d9761b2cff8f0d0af92871551dc121aaebcf40c19cce0`,
  410418 bytes), recorded below:
* 2026-10-08, the reason for the previous version: a review found that `build_notebooks.py check
  lovelock_gkd` failed in a fresh clone whose repository folder had 153 characters (`LINK : fatal error
  LNK1104` on the 264-character path of `liblovelock_gkd-<16 hexadecimal digits>.rlib` under
  `<output>/cargo-target`; the gate step notebooks-check failed). Reproduced here before the change:
  `cargo build --release` of `Revision/gkd_lovelock/code` with the former folder layout below a
  155-character folder ended with exit status 101 and `LNK1104` (.rlib path 266 characters). The
  crate has a library (`src/lib.rs`) and a program (`src/main.rs`), so the linker must open the .rlib.
  The other two notebooks (crate `Revision/kohn_sham/solver`, no library) failed in the same way at
  longer repository folders, on the path of the program the linker writes (above 153 and 159
  characters; their provenance files, section 7); all three were changed in the same way. Since then
  the build goes to `<cargo-target>` (sections 2 and 6); the results and the figures are unchanged.
* All runs below with the system's temporary folder set (TMP, TEMP, TMPDIR) to a scratch folder of
  154 characters, so `<cargo-target>` had a path of 192 characters and the .rlib one of 243.
* 2026-10-08, build A: `python Revision/notebooks/tools/build_notebooks.py build lovelock_gkd --out
  <scratch>/buildA` - executed in 26.8 s, wrote 410418 bytes, audit PASS, sha256
  `e4066a453826082a0e0d9761b2cff8f0d0af92871551dc121aaebcf40c19cce0`.
* 2026-10-08, build B: the same command with `--out <scratch>/buildB` - executed in 30.5 s; the
  notebook written is byte-identical to build A (same sha256), and the seven files of the two output
  folders are byte-identical (table of section 2).
* 2026-10-08, check: `python Revision/notebooks/tools/build_notebooks.py check lovelock_gkd --out
  <scratch>/check1` - a third independent execution (25.4 s): `check lovelock_gkd: PASS - the
  re-executed notebook is byte-identical to Revision/notebooks/lovelock_gkd.ipynb (410418 bytes)`; its
  seven files equal those of builds A and B.
* 2026-10-08, deep repository folder: the files the notebook needs (`Revision/SPEC.md`,
  `Revision/README.md`, the crate's `Cargo.toml`, `Cargo.lock` and `src/`, `Revision/gkd_lovelock/results/`,
  `Revision/notebooks/`) copied below a folder of 170 characters and `check lovelock_gkd` run there
  without `--out`, as the gate step notebooks-check runs it: with the previous builder and notebook
  (those of the last commit before this change) exit status 1 with `LNK1104`; with the current ones
  `check lovelock_gkd: PASS - ... byte-identical ... (410418 bytes)` (26.0 s).
* 2026-10-08, `REVISION_NB_CARGO_TARGET=<scratch>/ct` with `check lovelock_gkd --out <scratch>/check2`:
  PASS, byte-identical (24.8 s); the build went to `<scratch>/ct`.
* 2026-10-08, tests: `python -m unittest Revision/tests/test_revision_notebooks.py -v` - 9 static tests
  OK, 2 skipped; with `REVISION_NOTEBOOKS_FULL=1` - 11 tests OK in 109.1 s (the installed versions
  equal the pins; `check` of all three notebooks in temporary folders is byte-identical).
* 2026-10-08, headless instruction of section 2.5: `python -m nbconvert --to notebook --execute
  Revision/notebooks/lovelock_gkd.ipynb --output-dir <scratch>` with `REVISION_NB_OUT=<scratch>/out` -
  exit status 0, no error output, no stderr, `checks of this notebook: 40 passed, 0 failed`
  (nbconvert's own file is not normalised, so it is not compared byte for byte).
* 2026-10-14, the author's coordinates x0..x7 (ordered by the user on 2026-10-14; the record had named them x1..x8 with the hidden direction x8 last): the coordinate list of the builder is x0..x7 (x0 the hidden direction, first), section 4.1 states the user's metric with b4 (b4 = 1 is the metric before), the tables and figures label the components x0, x1, x4, x5, and the program run of section 8 writes the result files of `Revision/gkd_lovelock/results` of 2026-10-14 (the table of section 2 had still listed the files from before the metric with b4). `python Revision/notebooks/tools/build_notebooks.py build lovelock_gkd` - executed in 24.1 s, wrote 419435 bytes, audit PASS, sha256 `adfc95b1c2c0e8152172900f596a60492fab24cc635678c7b1fbcaf23df71395` (the version before: 412223 bytes, `4b48dba289e5abc4...`; builder before `a8992530a389d5dc...`); `check lovelock_gkd` - a second independent execution (20.6 s): PASS, the re-executed notebook is byte-identical; the 7 files of the two output folders are byte-identical and equal to the table of section 2 (refreshed from them). The notebook's own checks pass as before (no FAIL line). Tests: `REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py` - 11
  tests OK in 48.6 s (the installed versions equal the pins; `check` of all three notebooks byte-identical). Every run
  with `timeout 423`.
* 2026-10-16, general b4(x4) (the user's order of 2026-10-15, "move everything to b4(x4); b4 is never 1"): until then
  sections 8.3, 8.4 and the figures restricted the polynomials to b4 = 1 (the identities were checked on that
  restriction, the table and the figures showed b4 = 1). Now: the identities of section 8.3 with all 13 symbols (the
  Lovelock scalars parsed with their b4 terms); section 8.4 rewritten (the components in H, a4', a4'', u = b4'/b4,
  v = u'; the comparison with `a4-equations.json` lovelockTensors; the blocks on the history; the history source from
  the GKD tensors with the author's weights); figures 1 and 2 on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)
  (b4(0) = 1 for the picture) and on the family b4 = b4(0) e^(4 a4/3); sections 1, 4.1, 4.4, 8.2 and 11 of the
  notebook. A first build stopped at the new check `blocks_differ_on_the_history`: my expectation that the
  ordinary-space and extra-time blocks differ on the history for every k was wrong for k = 3 (the difference
  E_(3)^x1_x1 - E_(3)^x5_x5 vanishes at a4' = H, a4'' = v = 0 for every u); the check and the texts now state what
  the computation shows (`blocks_on_the_history`). `python Revision/notebooks/tools/build_notebooks.py build
  lovelock_gkd` - executed in 22.0 s, wrote 460163 bytes, audit PASS, `checks of this notebook: 45 passed, 0
  failed`; `check lovelock_gkd` - executed in 21.9 s, PASS, byte-identical; the files of the two output folders are
  byte-identical and equal to the table of section 2 (the four program outputs equal the record). Every run with
  `timeout 423`, from the repository root in the working tree on top of commit `c3f4bb7` (not a fresh clone).
  `REVISION_NOTEBOOKS_FULL=1 python -m unittest Revision/tests/test_revision_notebooks.py`: 11 tests OK in 56.9 s (the
  installed versions equal the pins; `check` of all three notebooks in temporary folders is byte-identical).
* 2026-10-17, the corrected primordial metric of 2026-10-16 (version 2; phase W6 of `HANDOFF.md` 0.10): the program of
  `Revision/gkd_lovelock` (phase W4) computes the corrected metric with 14 symbols per monomial (W = (sin^2 z)^(1/12)
  replaces sin^(1/3) z, and G = sign(cot z) is new) and runs 27 checks; the sympy verification has 56 checks. The
  builder was rewritten for it: sections 1, 4.1, 4.4, 6 (the recited metric is now compared with SPEC section 1, split
  at " (the corrected"), 8.2 (every off-diagonal component is zero; x0 = x5 = x6 = x7), 8.3 (14 symbols; the
  Lovelock scalars parsed with E^(n*a4[x4]); sqrt|det g| = G C E^-1 Q^4 W^3), 8.4 (the components in H, a4', a4'', u,
  v and k = e^(2 a4)/b4, compared with `a4-equations.json`; E^x0_x0 = E^x5_x5; the blocks differ also for constant
  b4; the history source as a polynomial in k, compared with `historySource_kappaT_minus_Lam`), 9 (counts 27, 56,
  29), 10 (figures 1 and 2) and 11. Before the patch every planned check was probed against the record in a scratch
  script (all true). `python Revision/notebooks/tools/build_notebooks.py build lovelock_gkd` - executed in 30.6 s,
  wrote 467602 bytes, audit PASS, `checks of this notebook: 47 passed, 0 failed`; `check lovelock_gkd` - a second
  independent execution (29.6 s): PASS, byte-identical; the four program outputs equal the record (table of
  section 2). Every run with `timeout 423`, from the repository root in the working tree on top of commit `6e228a8`.
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
