# Provenance of the Revision notebook `lovelock_gkd.ipynb`

The Lovelock tensors of the author's metric with the generalized Kronecker delta (GKD).

* Notebook: `Revision/notebooks/lovelock_gkd.ipynb` (35 cells: 20 markdown, 15 code; 412223 bytes;
  sha256 `4b48dba289e5abc40cafd083426a157fe083d25384a33e8dffc6cf6c68189076`).
* Builder: `Revision/notebooks/src/lovelock_gkd.py`
  (sha256 `a8992530a389d5dc0307f1d37cf51a453ae913b687a5fa56491be20af45c5fa7`).
* Build tool: `Revision/notebooks/tools/build_notebooks.py`
  (sha256 `99f18fc03902e0920d21e30cfe3d44df6d298583a8abb935b486f383acf345a0`).
* Pins: `Revision/notebooks/requirements.txt`
  (sha256 `ba6c2cab4048282eb64e9bad8d3b265660438e700815f019dd0592c6f67450bb`).
* Built and verified on 2026-10-08, Windows 11 Pro for Workstations, Python 3.14.5, numpy 2.4.6,
  matplotlib 3.11.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0, nbconvert 7.16.6,
  jupyterlab 4.4.10, cargo 1.91.

## 1. What it computes

1. Builds the Revision Rust crate `Revision/gkd_lovelock/code` (`lovelock_gkd`, pure Rust, no
   dependencies) with `cargo build --release` into the build folder `<cargo-target>` (section 2) and
   requires zero compiler warnings.
2. Runs `lovelock_gkd print-config` and checks that the recited metric occurs verbatim in the author's
   task quoted in `Revision/README.md`.
3. Defines two independent Python versions of the GKD (the rule: distinct indices, same set, sign of
   the permutation; and the author's determinant `Det[Outer[delta, lower, upper]]` by the Leibniz
   formula) and compares them exhaustively for all pairs of index lists of length 1, 2, 3 over eight
   values (64, 4096, 262144 pairs): 0 mismatches; non-zero counts 8, 112, 2016 = 8!/(8-p)! p!;
   +1 / -1 / 0 counts equal to `wolfram-gkd-report.json` `measurements.gkdComparison`, pair and
   mismatch counts equal to the rows p = 1, 2, 3 of `gkd-selftest.json`; the two values of
   `gkdSelfCheck` in `lovelock-report.json` are reproduced.
4. Runs `lovelock_gkd lovelock --output <output>/lovelock_run --brute-force-k2` (the command of the
   committed record): 19 checks, all PASS; the four files written are byte-identical to the committed
   `Revision/gkd_lovelock/results/` files.
5. Tables of the four independent diagonal components of P_(k) (k = 1, 2, 3) and of L_(k); exact
   Python re-checks (fractions, no rounding): the trace identity for k = 1, 2, 3, -P_(1)/4 equals
   `einsteinMixed` of `curvature.json` in all 64 components, A_(k)^hh = sqrt|det g| g^hh P_(k)^h_h;
   the normalised E_(k) = -P_(k)/2^(k+1) in a table, with the exact observations that
   E^x1_x1 - E^x5_x5 contains a4'' in every term and that at a4'' = 0 the x1, x5 and x8 components are
   equal.
6. Reads the five committed records and asserts their counts exactly as their JSON files give them:
   `lovelock-report.json` checkCount 19, failedCheckCount 0, verdict SUCCESS;
   `gkd-selftest.json` 9 rows, 0 mismatches, verdict SUCCESS (18043520 pairs in total);
   `python-lovelock-report.json` checkCount 49, failedCheckCount 0, verdict SUCCESS;
   `wolfram-gkd-report.json` checkCount 29 of expectedCheckCount 29, failedCheckCount 0, verdict SUCCESS;
   and that the input sha256 recorded by the sympy verifier (curvature.json, lovelock-tensors.json)
   and by the Wolfram verifier (curvature.json, lovelock-report.json, lovelock-tensors.json) equal the
   sha256 of the files the program has just written.
7. Draws three figures: scale factors of the eight directions (illustrative a4 = x4) and the
   hidden-direction functions; the diagonal components of E_(1), E_(2), E_(3) against a4'/H at
   a4'' = 0 and a4'' = 0.5 H^2; the work of the Lovelock sums (8^(4k+2) index lists, leaves, GKD
   evaluations, from the new report's counters) and the fraction of non-zero GKD values.
8. Ends with "what this notebook showed, and what it did not show".

The notebook prints 40 PASS lines and no FAIL line; its last code cell prints
`checks of this notebook: 40 passed, 0 failed`.

## 2. Files read and written

Read (sha256 at the time of the verified builds):

| file | sha256 |
| --- | --- |
| `Revision/SPEC.md` | (only its existence is used, to find the repository) |
| `Revision/README.md` | (not pinned: the file changes as the record grows; the notebook only needs the author's metric text to occur in it and checks that it does) |
| `Revision/gkd_lovelock/code/Cargo.toml` | `c6719ffae8040c42034a903b7cf2aefbc2124fee7dd6750de0c455d7cb653d70` |
| `Revision/gkd_lovelock/code/Cargo.lock` | `41e4efb7365fc3c818a2a7d18ffd214d11d6856dd4f62ea970ca2a4e39115250` |
| `Revision/gkd_lovelock/code/src/geometry.rs` | `ea7a77cef471610b909ba6f0300e78f582506bfc1125c36c1b2a772fefd96678` |
| `Revision/gkd_lovelock/code/src/gkd.rs` | `3be0169f6c03d0d6afbd8361e6d80c5b802defb0878ddc2ffeb62e3dde106dd4` |
| `Revision/gkd_lovelock/code/src/lib.rs` | `cccd024b5a559ce306d770e4a2674a1bc3eb7b6cf00e05dc0858fb3cc4991da6` |
| `Revision/gkd_lovelock/code/src/lovelock.rs` | `1ce0c7e3a16acd1509890b7f7029cd9e258e72d4816235a0df4bf2f99f1acd1b` |
| `Revision/gkd_lovelock/code/src/main.rs` | `ac56bbce5e2482caf57b316691ea8326ebd05bbd13cb7184bc07b900e91d66ac` |
| `Revision/gkd_lovelock/code/src/output.rs` | `b33a257109e1cdc528fb32c08aa59d6e541d0791da235256258b94ae0cd59e15` |
| `Revision/gkd_lovelock/code/src/poly.rs` | `c0e91c8b0ba8d4dcb542f48385b6e637b61373d6dcaf22913c70a7e54212b36d` |
| `Revision/gkd_lovelock/code/src/rational.rs` | `a8e9b54a655dc9e1d15ef0f4203cb55eda168efd93e52b337573fb6d8c5384ba` |
| `Revision/gkd_lovelock/results/curvature.json` | `d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e` |
| `Revision/gkd_lovelock/results/lovelock-tensors.json` | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` |
| `Revision/gkd_lovelock/results/lovelock-components.md` | `65f95810d3b7b6696227670f03241c20758bcee4e408743803200cae68a1b8e7` |
| `Revision/gkd_lovelock/results/lovelock-report.json` | `5c919ea827a5e6822a7196bb66ead64fa0a3e70f01f35b2bbfb99a65ae028bb8` |
| `Revision/gkd_lovelock/results/gkd-selftest.json` | `6cd72bd8d5d8d2f7acb4825ed0a975a26aaad343e323b9c96f6d1fc4f294d1dc` |
| `Revision/gkd_lovelock/results/python-lovelock-report.json` | `a4d6c0d5e2d063ce01611c06a98a4ba9cff0d61616b480b0b5828e2f3eee4d52` |
| `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | `71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189` |

Written: the result files and figures into the output folder `<output>` (the folder named by
`REVISION_NB_OUT`, otherwise `build/revision_notebooks/lovelock_gkd` in the repository, ignored by
git), identical in both verified builds and in the `check` runs; the Rust build into `<cargo-target>`
(the folder named by `REVISION_NB_CARGO_TARGET`, otherwise `revision-nb-lovelock_gkd-` followed by the
first 12 hexadecimal digits of the sha256 of the path of `<output>`, in the system's temporary
folder; on macOS and Linux created private, section 6):

| file | bytes | sha256 |
| --- | --- | --- |
| `<output>/lovelock_run/curvature.json` | 28162 | `d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e` (= record) |
| `<output>/lovelock_run/lovelock-tensors.json` | 55056 | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` (= record) |
| `<output>/lovelock_run/lovelock-components.md` | 19604 | `65f95810d3b7b6696227670f03241c20758bcee4e408743803200cae68a1b8e7` (= record) |
| `<output>/lovelock_run/lovelock-report.json` | 3154 | `5c919ea827a5e6822a7196bb66ead64fa0a3e70f01f35b2bbfb99a65ae028bb8` (= record) |
| `<output>/figures/figure1_scale_factors.png` | 72361 | `f2e19dd62b8515b200e6c6dcd46397322474848795c60faf087d8687f3252e9e` |
| `<output>/figures/figure2_lovelock_components.png` | 111384 | `7a180d388d97d88ae5149aa4aea9e33e0b1ad8445ef33be90332b7fb49758a42` |
| `<output>/figures/figure3_gkd_work.png` | 57413 | `f602fb8a3078c891a31c8a6c6b2440c1c5732a10e4b42396a30ec72ff4159954` |
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
  `{{exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},...`.
* Section 7: the table `p = 1, 2, 3`: pairs 64 / 4096 / 262144, mismatches 0, +1: 8 / 56 / 1008,
  -1: 0 / 56 / 1008, 0: 56 / 3984 / 260128; the committed self-test table (9 rows, verdict SUCCESS).
* Section 8.1: 19 PASS lines of the program, `check_count=19`, `failed_check_count=0`,
  `lovelock: SUCCESS (<t> s)`, and four `identical to the record` lines.
* Section 8.4, for example: at a4'' = 0, E_(1)^x1_x1 = E_(1)^x5_x5 = E_(1)^x8_x8 = 15 H^2 - 3 (a4')^2;
  E_(1)^x1_x1 - E_(1)^x5_x5 = 2 a4''.
* Section 9: the table of the four reports (19 / 9 rows / 49 / 29 checks, 0 failed, SUCCESS).
* Section 10.4: `checks of this notebook: 40 passed, 0 failed` and the seven files listed above.

Run times printed by the program are masked as `<t>`; no path of the computer is printed (paths are
shown relative to the repository or as `<output>/...` and `<cargo-target>/...`). The printed text
does not depend on where `<output>` and `<cargo-target>` are, so the notebook is byte-identical with
or without `REVISION_NB_CARGO_TARGET`.

## 5. Measured run time (Windows 11, 2026-10-08)

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
* Not verified here: the run instructions on macOS and Linux (written for them, executed only on
  Windows 11); byte-identity across different computers or package versions (the PNG figures depend on
  the matplotlib version).
