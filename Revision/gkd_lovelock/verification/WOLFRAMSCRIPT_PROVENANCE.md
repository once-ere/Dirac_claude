# WolframScript provenance: the Wolfram check of GKD and of the Lovelock tensors

Set: `Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls` with its package
`Revision/gkd_lovelock/verification/LovelockGKDCheck.wl`.

At a glance (verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and verified
again on 2026-10-07 at commit `a4c5eda1df069a43a55ff8b57148f5de8edd1670`, where every file of the set and every
input is unchanged; Windows 11, Wolfram 15.0.1, WolframScript 1.14.0, cargo/rustc 1.91.1):

* EXECUTES OK: exit code 0, `check_count=29`, `failed_check_count=0`, verdict `SUCCESS`, nothing on
  standard error.
* The one output of the default run, `Revision/gkd_lovelock/results/wolfram-gkd-report.json`, was
  reproduced BYTE FOR BYTE in every run: three runs from two fresh clones on 2026-10-02 and three more
  runs from two new fresh clones on 2026-10-07 (sha256 `de3678170c7d...` for the script as it was then).
  On 2026-10-08 the script was FIXED (see part 6.3): it no longer reports success when it cannot write
  its report.  The report records the script's own sha256, so the committed report changed in that one
  line; its sha256 is now `71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189`, and a run still leaves `git status` empty.
* Run time (the script's own `time_total`), on a shared 24-core machine: 95.3 s, 100.3 s and 111.9 s on
  2026-10-02; 128.2 s, 135.0 s and 117.3 s on 2026-10-07 (the machine was fully loaded by other jobs).
* Fixed on 2026-10-08: an output file that cannot be written now prints one `ERROR: cannot write <path> (...)`
  line and exits with code 2 (before, the run reported SUCCESS with exit code 0).  No discrepancy is open.

This file is for a student who has never used Wolfram Language, WolframScript or Rust. Every
instruction needed to run the check is written out below.

---

## 1. What this set is and what it computes

### 1.1 In plain words

The repository contains a Rust program (`Revision/gkd_lovelock/code`, the crate `lovelock_gkd`) that
computes two things exactly:

1. **GKD**, the generalized Kronecker delta. The author defined it in Mathematica by one line:

   ```text
   kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]
   ```

   In words: take two lists of coordinate labels of the same length p, build the p x p matrix whose
   entry (i, j) is 1 when the i-th lower label equals the j-th upper label and 0 otherwise, and take
   its determinant. The result is always +1, -1 or 0. The Rust function `GKD` gets the same number
   without computing a determinant (it finds the permutation and counts its inversions).

2. **The Lovelock tensors** P_(k)^h_j and A_(k)^{lh} (k = 1, 2, 3) of Lovelock's equation (4.38) for
   the author's 8-dimensional test metric

   ```text
   g = diag( E^(2 a4[x4]) Sin[6 H x8]^(1/3)   for x1, x2, x3,
             -1                               for x4,
             -E^(-2 a4[x4]) Sin[6 H x8]^(1/3) for x5, x6, x7,
             Cot[6 H x8]^2                    for x8 )
   ```

   P_(k)^h_j is a sum over products of k curvature components R^{ab}_{cd}, each product weighted by
   one generalized Kronecker delta with 2k + 1 upper and 2k + 1 lower indices; A_(k)^{lh} =
   sqrt(det g) g^{jl} P_(k)^h_j. P_(1) is -4 times the Einstein tensor; P_(4) vanishes in 8 dimensions,
   so k = 1, 2, 3 is the complete series.

This Wolfram set checks the Rust program **independently**, in Mathematica's own language, without
re-implementing the Rust rule:

* **GKD against the author's verbatim definition.** The script writes a tiny Rust program (an
  "exporter", whose source text is embedded in the script), compiles it with `cargo` against the
  UNCHANGED crate `Revision/gkd_lovelock/code`, and runs it. The exporter writes the GKD values of
  346,304 pairs of index lists to a binary file: every pair of lists of length 1, 2 and 3 over the
  labels 0..7 (64, 4,096 and 262,144 pairs) and 20,000 pseudo-random pairs of each length 4, 5, 6, 7.
  The script then evaluates the author's `kδ`, re-typed verbatim, on every pair and compares.
  Result: 0 mismatches.
* **The curvature from scratch.** Mathematica computes the Christoffel symbols and the Riemann tensor
  of the metric (Misner-Thorne-Wheeler sign convention) with its own `D`, `Inverse` and `Simplify`,
  and finds the same 156 nonzero R^{ab}_{cd} as the Rust file `curvature.json`.
* **The Lovelock tensors with the verbatim kδ.** k = 1 and k = 2: every k-tuple of the 156 nonzero
  curvature entries for each of the 64 components (9,984 and 1,557,504 calls of `kδ`, no shortcut).
  k = 3: index lists that repeat a label in a row are skipped (their determinant is 0 because two rows
  or two columns are equal) and `kδ` is called on every one of the 1,128,960 lists left. The
  difference with the Rust tensors of `lovelock-tensors.json` is then simplified with `FullSimplify`:
  it is exactly 0 for all 64 components of P_(k) and of A_(k), k = 1, 2, 3.
* **Identities and counters.** P_(1) = -4 G (Einstein tensor from the Ricci tensor computed here);
  the traces sum_h P_(k)^h_h = (8 - 2k) L_(k); the numbers of nonzero `kδ` terms (696, 32,640,
  495,360) equal the counters of the Rust report; the Mathematica text of every component in
  `lovelock-tensors.json` equals the expression rebuilt from its exact monomial list (384 components).
* **Two negative controls** show that the comparisons CAN fail: comparing against -GKD gives a
  mismatch at exactly every pair where GKD is nonzero, and a deliberately changed P_(2) component and
  A_(3) component are flagged, and only those.

The script never opens any notebook (`.nb` file) of the author, nor `Generalized_Kronecker_Delta.txt`,
nor any other file with the author's answers. It reads the definition of `kδ` from its own package and
checks that it is the text recorded in `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`.

### 1.2 The 29 checks of the default run

| # | check name | what it establishes |
| --- | --- | --- |
| 1 | `definition_is_the_authors_verbatim` | the kernel's definition of `kδ`, printed in InputForm, is exactly the author's line, and that line is the one recorded in `PROVENANCE_OF_THE_COMPUTATION.md` |
| 2 | `definition_unequal_lengths_stay_unevaluated` | `kδ[{0}, {0, 1}]` stays unevaluated (lengths differ); `kδ[{0, 1}, {1, 0}] = -1`; `kδ[{0, 1, 2}, {1, 2, 0}] = +1` |
| 3 | `gkd_values_file_layout` | the exporter wrote 64, 4096, 262144 and 4 x 20000 records, the first three in the order of `Tuples[Range[0, 7], 2 p]`; 3,161,984 bytes |
| 4-6 | `gkd_equals_kdelta_exhaustive_length_1` .. `_3` | `kδ` = GKD for every pair of lists of length 1, 2, 3 over 0..7 (0 mismatches) |
| 7-10 | `gkd_equals_kdelta_random_length_4` .. `_7` | `kδ` = GKD for 20,000 pseudo-random pairs of each length 4..7 (0 mismatches; the 10,000 permutation samples all give +1 or -1) |
| 11 | `negative_control_gkd_comparison_detects_a_sign_flip` | against -GKD the same test fails at exactly the nonzero pairs (8, 112, 2016, 10022, 10005, 10002, 10000) |
| 12 | `riemann_mixed_equals_rust_curvature` | the 156 nonzero R^{ab}_{cd} computed here equal `riemannMixedNonzero` of `curvature.json` |
| 13 | `sqrt_det_g_is_cos` | det g = Cos[6 H x8]^2 and sqrt(det g) = Cos[6 H x8] on 0 < 6 H x8 < Pi/2 |
| 14 | `lovelock_kdelta_values_are_integers` | every `kδ` call in the Lovelock sums returned an integer |
| 15-20 | `k1_P_equals_rust_all_64_components`, `k1_A_...`, `k2_P_...`, `k2_A_...`, `k3_P_...`, `k3_A_...` | `FullSimplify[wolfram - rust]` is 0 for all 64 components of P_(k) and of A_(k), k = 1, 2, 3 |
| 21 | `negative_control_tensor_comparison_detects_a_change` | adding H^4/1000 to the Rust P_(2) x3,x3 and multiplying the Rust A_(3) x8,x8 by 1001/1000 is detected, at exactly those components |
| 22 | `k1_equals_minus_4_einstein` | P_(1)^h_j = -4 G^h_j exactly |
| 23-25 | `k1_trace_equals_6_L1`, `k2_trace_equals_4_L2`, `k3_trace_equals_2_L3` | sum_h P_(k)^h_h = (8 - 2k) L_(k) with L_(k) of `lovelock-tensors.json` |
| 26-28 | `k1_nonzero_kdelta_terms_equal_rust_counter` .. `k3_...` | 696, 32,640 and 495,360 nonzero `kδ` terms, equal to the Rust counters; 9,984 = 64 x 156 and 1,557,504 = 64 x 156^2 calls; 1,128,960 calls = the Rust `leaves` counter |
| 29 | `rust_json_text_equals_its_monomials` | in `lovelock-tensors.json` the Mathematica text of all 384 components equals the expression rebuilt from its exact monomials |

### 1.3 Documents that cite its results

* `Revision/README.md`, table "Folders", row `gkd_lovelock/`: "verified in `verification/`: sympy 49/49,
  Wolfram 29/29" (the 29/29 is this set).
* `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md`, section "Later note (2026-10-01)":
  "`verify_lovelock_gkd.wls` with `LovelockGKDCheck.wl`, report `wolfram-gkd-report.json`, 29 checks ...
  all pass".
* `Revision/SPEC.md`, section 10: `gkd_lovelock/` "(GKD, Lovelock tensors, done; its verification
  completed)".
* `Revision/tests/test_gkd_lovelock.py`: pins the sha256 of `wolfram-gkd-report.json`
  (`71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189`), requires its 29 checks to be PASS, and
  in its slow test `test_SLOW_wolfram_check_reproduces_the_report` runs this script once (report and export
  directory in a temporary folder) and requires the same sha256.
* `Revision/textbook/TEXTBOOK_SPEC.md` (the specification of the textbook "Universes in Pairs"),
  chapter 11 "GKD and the Lovelock tensors": its sources are "Revision/gkd_lovelock (all of it)".
* The textbook notebooks (work in progress at the time of the re-verification of 2026-10-07; they read
  the committed report, they do not run this script): `Revision/textbook/notebooks/00c_honesty_ledger.ipynb`
  (lists `wolfram-gkd-report.json` as "Wolfram 29 of 29" and checks the input digests it records),
  `01c_generalized_delta.ipynb` (the check `definition_unequal_lengths_stay_unevaluated` and the
  `gkdComparison` measurements), `01d_gkd_record_selftests.ipynb`, `11a_kronecker_delta_gkd.ipynb` (the
  `measurements` of the report) and `11b_lovelock_tensors.ipynb` ("`wolfram-gkd-report.json`, 29 checks").
* Indirectly, the Lovelock tensors that this set verifies (`lovelock-tensors.json`) are used by the
  field equations for a4 (`Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls`,
  `Revision/field_equations_a4/python/check_field_equations_a4.py`) and by the documents
  `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md` and `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md`.

(The same folder also holds `check_lovelock_gkd.py`, an independent sympy checker with its own report
`python-lovelock-report.json`, 49 checks. It is a Python program, not part of this WolframScript set.)

---

## 2. The files

All paths are relative to the repository root. The sha256 digests and sizes are those of commit
`c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and they were measured again, identical, in fresh clones of commit
`a4c5eda1df069a43a55ff8b57148f5de8edd1670` on 2026-10-07. Every file is stored byte for byte (the repository's `.gitattributes`
has `* -text`, so git never converts line endings); both scripts are pure ASCII with LF line endings.

### 2.1 The scripts of the set

| file | role | sha256 | lines | bytes |
| --- | --- | --- | --- | --- |
| `Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls` | the script you run (WolframScript); builds and runs the exporter, does the checks, writes the report | `bec6c8c5d25f62061b549a93fb5dc8e66c396cad1cd9bc6f08826129ae965a50` | 574 | 36,660 |
| `Revision/gkd_lovelock/verification/LovelockGKDCheck.wl` | the package it loads (context ``LovelockGKDCheck` ``): the verbatim `kδ`, the metric, the curvature, the Lovelock sums, the monomial reader | `2ea70c740c477fd7e89493d068d6f9e00e48e0faf354a9c50f5525560d0655f8` | 213 | 12,919 |

The script finds the package and all its inputs relative to its OWN location
(`ExpandFileName[$InputFileName]`), so the inputs are found whatever the current directory is; only
the report path you type is relative to the current directory.

### 2.2 Inputs it reads

| file | why it is read | sha256 | lines | bytes |
| --- | --- | --- | --- | --- |
| `Revision/gkd_lovelock/results/PROVENANCE_OF_THE_COMPUTATION.md` | must contain the author's definition of `kδ`, in backquotes | `eb7011d650683737868b43422cfc6c6e311aa1647a3d2608af1c2fb4c8df3759` | 73 | 4,868 |
| `Revision/gkd_lovelock/results/curvature.json` | the Rust curvature, `riemannMixedNonzero` | `d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e` | 325 | 28,162 |
| `Revision/gkd_lovelock/results/lovelock-tensors.json` | the Rust P_(k), A_(k), L_(k) (exact monomial lists and Mathematica text) | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` | 405 | 55,056 |
| `Revision/gkd_lovelock/results/lovelock-report.json` | the Rust counters `gkdNonzero` and `leaves` | `5c919ea827a5e6822a7196bb66ead64fa0a3e70f01f35b2bbfb99a65ae028bb8` | 34 | 3,154 |
| `Revision/gkd_lovelock/code/Cargo.toml` | the crate compiled by cargo as a path dependency of the exporter | `c6719ffae8040c42034a903b7cf2aefbc2124fee7dd6750de0c455d7cb653d70` | 16 | 400 |
| `Revision/gkd_lovelock/code/src/geometry.rs` | crate source (compiled) | `ea7a77cef471610b909ba6f0300e78f582506bfc1125c36c1b2a772fefd96678` | 225 | 8,157 |
| `Revision/gkd_lovelock/code/src/gkd.rs` | crate source: the function `GKD` | `3be0169f6c03d0d6afbd8361e6d80c5b802defb0878ddc2ffeb62e3dde106dd4` | 205 | 7,488 |
| `Revision/gkd_lovelock/code/src/lib.rs` | crate source (compiled) | `cccd024b5a559ce306d770e4a2674a1bc3eb7b6cf00e05dc0858fb3cc4991da6` | 15 | 645 |
| `Revision/gkd_lovelock/code/src/lovelock.rs` | crate source (compiled) | `1ce0c7e3a16acd1509890b7f7029cd9e258e72d4816235a0df4bf2f99f1acd1b` | 204 | 7,396 |
| `Revision/gkd_lovelock/code/src/main.rs` | crate source (hashed; it is the crate's own program, not used by the exporter) | `ac56bbce5e2482caf57b316691ea8326ebd05bbd13cb7184bc07b900e91d66ac` | 263 | 15,411 |
| `Revision/gkd_lovelock/code/src/output.rs` | crate source (compiled) | `b33a257109e1cdc528fb32c08aa59d6e541d0791da235256258b94ae0cd59e15` | 71 | 2,445 |
| `Revision/gkd_lovelock/code/src/poly.rs` | crate source (compiled) | `c0e91c8b0ba8d4dcb542f48385b6e637b61373d6dcaf22913c70a7e54212b36d` | 425 | 13,018 |
| `Revision/gkd_lovelock/code/src/rational.rs` | crate source (compiled) | `a8e9b54a655dc9e1d15ef0f4203cb55eda168efd93e52b337573fb6d8c5384ba` | 141 | 3,716 |

All thirteen digests are written into the report (`inputSha256`), together with the digests of the two
scripts (`sourceSha256`), so the report states exactly what it checked. The crate's own
`Revision/gkd_lovelock/code/Cargo.lock` is NOT read (the exporter has its own lock file), and the
crate's own `target` folder is NOT used or created.

### 2.3 Outputs it writes

| output | where | content |
| --- | --- | --- |
| the JSON report | the path given as the argument; the documented command writes the committed file `Revision/gkd_lovelock/results/wolfram-gkd-report.json` | 344 lines, 18,135 bytes, UTF-8 (it contains the letter δ), LF line endings, tab indentation, final newline; sha256 `71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189` for the default run |
| the exporter crate | `<export directory>/Cargo.toml` and `<export directory>/src/main.rs` (rewritten only when their text changes) | `main.rs` sha256 `b5130177e38adba151c043fd5048f023b2ab6521acc32f620efcc2b8e794a372` (recorded in the report as `exporterMainRsSha256`); `Cargo.toml` contains the absolute path of YOUR clone's crate, so its digest depends on where you cloned |
| cargo's files | `<export directory>/Cargo.lock`, `<export directory>/target/` | written by `cargo build --release`; after a first build the whole export directory holds 24 files, about 5.3 MB on disk (on Windows; a tool that adds up file sizes, such as PowerShell's `Measure-Object`, shows 6.8 MB, because the exporter's `.exe` and `.pdb` in `target/release` are hard links to the same files in `target/release/deps`). Each later build from a clone in ANOTHER folder adds 7 more files (about 0.66 MB) under `target/`, so the folder grows; delete it to reclaim the space |
| the GKD values | `<export directory>/gkd-values.bin` | deleted and rewritten on every run; 3,161,984 bytes; sha256 `3ddccfa744b3708bbd3e251852236b0a2d3370e957c67bae8d94168de6d2d695` (recorded in the report as `valuesFileSha256`) |
| standard output | your terminal | the `time_...`, `check_...` and summary lines listed in part 4 |

The export directory is, unless you set `LOVELOCK_GKD_EXPORT_DIR`, the folder `revision_gkd_export`
inside Wolfram's temporary directory `$TemporaryDirectory` (on Windows
`C:\Users\<you>\AppData\Local\Temp\revision_gkd_export`; on macOS and Linux print the temporary directory
with `wolframscript -code '$TemporaryDirectory'`). It is deliberately a SHORT path outside the
repository: inside the repository, cargo's nested folders can exceed the 260-character path limit of
Windows.

---

## 3. How to run it (complete instructions)

You need four things: git, a Wolfram kernel with WolframScript, a Rust toolchain (cargo) with its C
linker, and a copy of the repository. About 1 GB of free memory is enough for the default run (the
kernel peaked at about 0.5 GB of working set and 0.7 GB of private memory; the optional `diagonal`
mode of part 3.5 needs about 2 GB), plus about 800 MB of disk for the repository (about 520 MB of files and about 250 MB of git history; measured 2026-10-08) and 6 MB for the
export directory (about 0.7 MB more for each further clone folder you run it from).

### 3.1 Install git

* Windows: install "Git for Windows" from https://git-scm.com/download/win (accept the defaults), or in
  PowerShell: `winget install --id Git.Git -e`. Close and reopen PowerShell afterwards.
* macOS: in Terminal run `xcode-select --install` (this installs git and the C linker that Rust needs
  later).
* Linux (Debian or Ubuntu): `sudo apt update` then `sudo apt install git build-essential curl`
  (build-essential is the C linker that Rust needs later). On Fedora: `sudo dnf install git gcc curl`.

Check: `git --version` prints a version.

### 3.2 Install a Wolfram kernel and WolframScript

Either of these works; the verification used Wolfram 15.0.1 with WolframScript 1.14.0.

* **The free Wolfram Engine for Developers.** Open https://www.wolfram.com/engine/ in a browser, click
  the download button, sign in with (or create, yourself) a free Wolfram ID, accept the licence for
  personal, non-production use, and download the installer for your system.
  * Windows: run the downloaded `.exe` and accept the defaults. WolframScript is installed with it and
    put on the PATH.
  * macOS: open the downloaded `.dmg` and follow its instructions (drag the application to
    Applications and install the WolframScript package it contains).
  * Linux: in a terminal, `sudo bash WolframEngine_<version>_LINUX.sh` (the file you downloaded) and
    accept the defaults; WolframScript goes to `/usr/local/bin`.
  * If `wolframscript` is still not found afterwards, download the separate WolframScript installer
    for your system from https://www.wolfram.com/wolframscript/ and run it.
  * Activate the engine once (this needs the internet): `wolframscript -activate`, then type your
    Wolfram ID (e-mail address) and password when asked.
* **Mathematica / Wolfram (desktop product).** If it is installed and activated, WolframScript comes
  with it. On Windows it is on the PATH (`C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe`).
  On macOS, if `wolframscript` is not found, install it from https://www.wolfram.com/wolframscript/.

Check, in a NEW terminal window (Windows: PowerShell; macOS: Terminal; Linux: any shell):

```text
wolframscript -version
wolframscript -code '$Version'
```

The first prints for example `WolframScript 1.14.0 for Microsoft Windows (64-bit)`, the second for
example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)`. Keep the single quotes around
`$Version` (in PowerShell and in bash they stop the shell from treating `$Version` as one of its own
variables).

### 3.3 Install Rust (cargo) 1.87 or newer

The script compiles a small Rust program, so `cargo` must be on the PATH of the terminal from which you
start `wolframscript`. Rust 1.87 or newer is required: the crate uses `is_multiple_of`, which became
stable in Rust 1.87 (the verification used 1.91.1). The crate has no dependencies, so cargo downloads
nothing.

* Windows: download `rustup-init.exe` from https://rustup.rs and run it. When it says that the Visual
  Studio C++ build tools are missing, accept its offer to install them (or install "Build Tools for
  Visual Studio" with the workload "Desktop development with C++" from
  https://visualstudio.microsoft.com/visual-cpp-build-tools/); Rust needs their linker `link.exe`.
  Then accept the default installation.
* macOS and Linux: after the C linker of part 3.1, run
  `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and accept the default
  installation, then run `. "$HOME/.cargo/env"` (or open a new terminal).

Check, in a NEW terminal window: `cargo --version` prints `cargo 1.87.0` or a later version (for
example `cargo 1.91.1 (ea2d97820 2025-10-10)`). If the version is older: `rustup update`.

### 3.4 Get the repository

Windows (PowerShell; a short folder such as `C:\work` avoids the Windows path-length limit):

```powershell
New-Item -ItemType Directory -Force C:\work
Set-Location C:\work
git clone https://github.com/once-ere/Dirac_claude.git
Set-Location C:\work\Dirac_claude
```

macOS and Linux:

```bash
mkdir -p ~/work
cd ~/work
git clone https://github.com/once-ere/Dirac_claude.git
cd ~/work/Dirac_claude
```

The checkout is about 520 MB. You are now in the **repository root** (the folder that contains
`Revision`); every command below is typed there.

### 3.5 Run the check

Windows PowerShell (from the repository root):

```powershell
wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json
$LASTEXITCODE
```

macOS and Linux (from the repository root):

```bash
wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json
echo $?
```

The command is the same on all three systems (forward slashes work on Windows too). The second line
prints the exit code: `0` means every check passed.

What you see: nothing for a few seconds (the Wolfram kernel starts), then the `time_...` lines one by
one; the two long pauses are the k = 2 sum (about 35-45 s) and the k = 3 sum (about 50-80 s). After
about 1.5 to 2.5 minutes the 29 `check_...` lines and the summary appear. Part 4 shows the exact output.

Important details:

* Type the report path as a plain argument. Do NOT put `--` in front of it: WolframScript 1.14 drops
  `--` and every argument after it (the report would then go to the default path, which is the same
  committed file).
* The documented command OVERWRITES the committed report `Revision/gkd_lovelock/results/wolfram-gkd-report.json`.
  With Wolfram 15.0.1 the new file is byte-identical, so git sees no change. To leave the committed
  file untouched, give a path outside the repository instead, for example
  `$env:TEMP\wolfram-gkd-report.json` in PowerShell or `/tmp/wolfram-gkd-report.json` on macOS and Linux,
  and compare it with the committed file as shown in part 4.3.
* Run only ONE copy at a time with the default export directory: two runs started at the same time
  would both write `revision_gkd_export/gkd-values.bin`. If you must run two at once, give each its own
  export directory with the variable `LOVELOCK_GKD_EXPORT_DIR` (table below).

Optional settings (environment variables; none is needed for the default run):

| variable | effect |
| --- | --- |
| `LOVELOCK_GKD_EXPORT_DIR` | where the exporter is written and built (default `<$TemporaryDirectory>/revision_gkd_export`); keep it short on Windows, for example `C:\gkdx` |
| `LOVELOCK_GKD_K3_UNPRUNED` | `none` (default, 29 checks; this is the committed report) or `diagonal`: also recomputes the 8 diagonal k = 3 components with NO skip at all (156^3 = 3,796,416 calls of `kδ` each) and adds the check `k3_diagonal_unpruned_equals_skip_sum` (30 checks). It takes much longer (part 4.5) and its report differs from the committed one, so write it to a path outside the repository |
| `LOVELOCK_GKD_WOLFRAM_REPORT` | the report path used when NO argument is given |

Setting a variable for one run:

```powershell
# Windows PowerShell
$env:LOVELOCK_GKD_K3_UNPRUNED = 'diagonal'
wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls "$env:TEMP\wolfram-gkd-report-diagonal.json"
Remove-Item Env:LOVELOCK_GKD_K3_UNPRUNED
```

```bash
# macOS and Linux
LOVELOCK_GKD_K3_UNPRUNED=diagonal wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls /tmp/wolfram-gkd-report-diagonal.json
```

### 3.6 If it fails

| what you see | likely cause | what to do |
| --- | --- | --- |
| `wolframscript` is "not recognized" / "command not found" | WolframScript is not installed or not on the PATH | install it (part 3.2), then open a NEW terminal; or call it by its full path, for example `& "C:\Program Files\Wolfram Research\WolframScript\wolframscript.exe" -file ...` in PowerShell |
| a request to activate, or a licence error | the Wolfram Engine is not activated | `wolframscript -activate` and sign in with your Wolfram ID |
| `ERROR: cargo build of the GKD exporter failed`, exit code 2 | cargo is not on the PATH of this terminal, the C linker is missing (`link.exe not found` on Windows, `linker cc not found` on Linux/macOS), or Rust is older than 1.87 (`use of unstable library feature` ... `is_multiple_of`) | check `cargo --version` in the SAME terminal; install the build tools / `xcode-select --install` / `build-essential` (parts 3.1 and 3.3); `rustup update`. To tell the causes apart, look at the lines around the message (all on standard output; the run stops after a few seconds, having written only `Cargo.toml` and `src/main.rs` into the export directory, which is harmless): if cargo is NOT on the PATH, the line just ABOVE the ERROR line reads `RunProcess::pnfd: Program cargo not found. Check Environment["PATH"].` and nothing follows the ERROR line; if cargo is found but the build fails, cargo's own error text (lines starting with `error:`) follows the ERROR line |
| an error about a path that is too long (Windows) | `LOVELOCK_GKD_EXPORT_DIR` points to a deep folder | unset it, or use a short folder such as `C:\gkdx` |
| `ERROR: the GKD exporter failed`, exit code 2 | the compiled exporter could not run (for example blocked by antivirus software) | allow the program `lovelock_gkd_export` in the export directory, or delete the export directory and run again |
| `ERROR: cannot write <path> (...)`, exit code 2 | the report path (or the export directory) is in a folder that cannot be created, is itself a folder, is read-only, or the disk is full | give a writable path (the documented command writes into the repository, which must not be read-only); nothing else is written after this line |
| `ERROR: missing input ...` or `ERROR: missing package ...`, exit code 2 | the repository is incomplete or you ran a copy of the script outside the repository | run the script that is inside a complete clone (part 3.4) |
| `ERROR: LOVELOCK_GKD_K3_UNPRUNED must be diagonal or none`, exit code 2 | that variable has another value | remove it (`Remove-Item Env:LOVELOCK_GKD_K3_UNPRUNED` in PowerShell, `unset LOVELOCK_GKD_K3_UNPRUNED` in bash) |
| a `check_...=false` line, `failed_checks=...` at the end, exit code 1 | an input file differs from the committed one (for example you edited `lovelock-tensors.json`) | `git status` shows the changed files; restore them with `git checkout -- <file>` and run again |
| the report differs from the committed one but every check passes | you use another Wolfram version: the report records the version in its `producer` line (`Wolfram Language 15.0.1`), and it stores the 24 diagonal components of P_(1), P_(2), P_(3) computed here as Mathematica text (`InputForm`, under `measurements` -> `wolframComponents`), whose term order and formatting can change between versions | expected (only Wolfram 15.0.1 was tested): at least the `producer` line differs, and the `InputForm` text under `wolframComponents` may differ too; all 29 checks must still be PASS (`"verdict":"SUCCESS"`, exit code 0). Look at the differences with `git diff -- Revision/gkd_lovelock/results/wolfram-gkd-report.json`, then restore with `git checkout -- Revision/gkd_lovelock/results/wolfram-gkd-report.json` |
| the report file appears in an unexpected place | the report path is relative to the CURRENT folder | run from the repository root, or give an absolute path |

---

## 4. Expected output

### 4.1 Standard output

Exactly these lines, in this order; only the numbers after `time_` change from run to run (these are
the times of the first verification run). Nothing is printed on standard error.

```text
time_definition=0.0
time_build_and_run_gkd_exporter=1.6
time_read_gkd_values=1.5
time_compare_gkd_with_kdelta=3.7
time_curvature=0.6
time_lovelock_k1_unpruned_64_components=0.1
time_lovelock_k2_unpruned_64_components=34.9
time_lovelock_k3_skip_repeated_64_components=49.3
time_compare_with_rust_tensors=2.8
time_identities_and_counters=0.1
check_definition_is_the_authors_verbatim=true
check_definition_unequal_lengths_stay_unevaluated=true
check_gkd_values_file_layout=true
check_gkd_equals_kdelta_exhaustive_length_1=true
check_gkd_equals_kdelta_exhaustive_length_2=true
check_gkd_equals_kdelta_exhaustive_length_3=true
check_gkd_equals_kdelta_random_length_4=true
check_gkd_equals_kdelta_random_length_5=true
check_gkd_equals_kdelta_random_length_6=true
check_gkd_equals_kdelta_random_length_7=true
check_negative_control_gkd_comparison_detects_a_sign_flip=true
check_riemann_mixed_equals_rust_curvature=true
check_sqrt_det_g_is_cos=true
check_lovelock_kdelta_values_are_integers=true
check_k1_P_equals_rust_all_64_components=true
check_k1_A_equals_rust_all_64_components=true
check_k2_P_equals_rust_all_64_components=true
check_k2_A_equals_rust_all_64_components=true
check_k3_P_equals_rust_all_64_components=true
check_k3_A_equals_rust_all_64_components=true
check_negative_control_tensor_comparison_detects_a_change=true
check_k1_equals_minus_4_einstein=true
check_k1_trace_equals_6_L1=true
check_k2_trace_equals_4_L2=true
check_k3_trace_equals_2_L3=true
check_k1_nonzero_kdelta_terms_equal_rust_counter=true
check_k2_nonzero_kdelta_terms_equal_rust_counter=true
check_k3_nonzero_kdelta_terms_equal_rust_counter=true
check_rust_json_text_equals_its_monomials=true
check_count=29
failed_check_count=0
time_total=95.3
report=Revision/gkd_lovelock/results/wolfram-gkd-report.json
```

The final verdict lines are `check_count=29` and `failed_check_count=0`; a failure would add a last
line `failed_checks=<names>`.

### 4.2 Exit code

`0` (all 29 checks passed and there are exactly 29). `1` if a check failed or the number of checks is
not the expected one; `2` on a load, build or input/output error (a line starting with `ERROR:` says
which); this includes a report or exporter file that cannot be written (`ERROR: cannot write <path>
(...)`; since the fix of 2026-10-08 the script never reports success without its report).

### 4.3 The report, and how to check it

`Revision/gkd_lovelock/results/wolfram-gkd-report.json` (or the path you gave) ends with these lines
(the indentation is a tab):

```text
	"checkCount":29,
	"expectedCheckCount":29,
	"failedCheckCount":0,
	"verdict":"SUCCESS"
}
```

Each of its 29 entries under `"checks"` has `"verdict":"PASS"` and a `"detail"` sentence with the
numbers (for example `0 mismatches; +1: 1008, -1: 1008, 0: 260128` for length 3). Ways to check it:

```powershell
# Windows PowerShell, from the repository root
Get-Content Revision/gkd_lovelock/results/wolfram-gkd-report.json -Tail 5
$r = Get-Content -Raw -Encoding utf8 Revision/gkd_lovelock/results/wolfram-gkd-report.json | ConvertFrom-Json; "$($r.verdict) $($r.checkCount) $($r.failedCheckCount)"
(Get-FileHash -Algorithm SHA256 Revision/gkd_lovelock/results/wolfram-gkd-report.json).Hash
git status --porcelain
```

```bash
# macOS and Linux, from the repository root
tail -n 5 Revision/gkd_lovelock/results/wolfram-gkd-report.json
shasum -a 256 Revision/gkd_lovelock/results/wolfram-gkd-report.json   # macOS
sha256sum Revision/gkd_lovelock/results/wolfram-gkd-report.json       # Linux
git status --porcelain
```

Expected (PowerShell): `SUCCESS 29 0`. Expected (macOS/Linux): the last five lines of the report end with
`"checkCount":29`, `"failedCheckCount":0` and `"verdict":"SUCCESS"` (in that order, each on its own line). In both: the digest `71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189`
(PowerShell prints it in capitals: `71C3F34F2F84662FBED6733379BEA115FFAD460DBAE38F641C692C6824399189`); and
`git status --porcelain` prints NOTHING (the regenerated report equals the committed one). If you wrote
the report to a path outside the repository, compare it with the committed file:
`git diff --no-index -- Revision/gkd_lovelock/results/wolfram-gkd-report.json <your path>` prints
nothing when they are identical.

The values file can be checked too: `<export directory>/gkd-values.bin` has 3,161,984 bytes and sha256
`3ddccfa744b3708bbd3e251852236b0a2d3370e957c67bae8d94168de6d2d695`, the value the report records under
`"valuesFileSha256"`.

### 4.4 Measured run time and memory (verification machine)

Machine: 24 logical cores, 191 GB RAM, Windows 11 Pro for Workstations. The machine was SHARED: up to 19
other Wolfram kernels of other jobs ran at the same time (CPU load about 97 %), which is why the k = 3
step varies. Times in seconds, from the script's `time_...` lines; "wall" is measured outside, from
the start of `wolframscript` to its exit (it includes the kernel start).

| step | run 1 | run 2 | run 3 |
| --- | --- | --- | --- |
| `definition` | 0.0 | 0.0 | 0.0 |
| `build_and_run_gkd_exporter` | 1.6 (rebuild: new clone path) | 0.7 (up to date) | 2.5 (first build in an empty folder) |
| `read_gkd_values` | 1.5 | 1.7 | 1.8 |
| `compare_gkd_with_kdelta` | 3.7 | 3.7 | 3.9 |
| `curvature` | 0.6 | 0.6 | 0.7 |
| `lovelock_k1_unpruned_64_components` | 0.1 | 0.1 | 0.1 |
| `lovelock_k2_unpruned_64_components` | 34.9 | 34.0 | 32.7 |
| `lovelock_k3_skip_repeated_64_components` | 49.3 | 56.5 | 66.4 |
| `compare_with_rust_tensors` | 2.8 | 2.1 | 2.7 |
| `identities_and_counters` | 0.1 | 0.1 | 0.1 |
| `time_total` | 95.3 | 100.3 | 111.9 |
| wall (incl. kernel start) | 98.1 | 103.4 | 115.5 |

Peak memory of the Wolfram kernel process (`wolfram.exe`): working set 480.7 / 485.5 / 486.2 MB,
private (pagefile-backed) memory 700.6 / 700.4 / 700.9 MB. `wolframscript.exe` itself: about 17 MB;
cargo about 16 MB, rustup about 28 MB, the console host `conhost.exe` about 7 MB.

Re-verification of 2026-10-07 (commit `a4c5eda`, three runs, the documented command; the machine was
again shared and fully loaded: 15 other Wolfram kernels of other jobs were running, CPU load 100 %, so
every step is slower than on 2026-10-02):

| step | run 4 | run 5 | run 6 |
| --- | --- | --- | --- |
| `definition` | 0.0 | 0.0 | 0.0 |
| `build_and_run_gkd_exporter` | 4.9 (first build in an empty folder) | 1.0 (up to date) | 3.4 (rebuild: new clone path) |
| `read_gkd_values` | 2.3 | 3.2 | 2.4 |
| `compare_gkd_with_kdelta` | 4.9 | 5.6 | 5.3 |
| `curvature` | 0.7 | 1.8 | 2.0 |
| `lovelock_k1_unpruned_64_components` | 0.1 | 0.2 | 0.2 |
| `lovelock_k2_unpruned_64_components` | 40.8 | 42.5 | 39.5 |
| `lovelock_k3_skip_repeated_64_components` | 71.4 | 77.3 | 61.2 |
| `compare_with_rust_tensors` | 2.3 | 2.7 | 2.3 |
| `identities_and_counters` | 0.1 | 0.1 | 0.1 |
| `time_total` | 128.2 | 135.0 | 117.3 |
| wall (incl. kernel start) | 133.3 | 139.9 | 121.6 |

Peak memory (Windows' own per-process peak counters, read every 0.25 s): the kernel `wolfram.exe`
485 / 485 / 486 MB working set and 700 / 700 / 700 MB private memory, the same as on 2026-10-02;
`wolframscript.exe` 17 MB; `rustc.exe` up to 116 MB working set (156 MB private) during a build. A
student's computer with 1 GB of free memory is therefore enough for the default run.

### 4.5 The optional `diagonal` mode

This mode is NOT the committed report; it is an extra, much longer check that the skip rule used for
k = 3 changes nothing. It was run once for this record (clone 1, `LOVELOCK_GKD_K3_UNPRUNED=diagonal`,
`LOVELOCK_GKD_EXPORT_DIR` set to a separate scratch folder, report written to a path OUTSIDE the
repository):

* exit code 0, nothing on standard error, `check_count=30`, `failed_check_count=0`;
* after `time_lovelock_k3_skip_repeated_64_components` it prints eight more lines
  `time_lovelock_k3_unpruned_component_x1_x1=...` .. `..._x8_x8=...` (180.9, 189.4, 194.2, 199.7, 191.0,
  178.6, 190.7 and 204.0 s on the shared machine), and the check list has one more line,
  `check_k3_diagonal_unpruned_equals_skip_sum=true`, right after
  `check_negative_control_tensor_comparison_detects_a_change=true`;
* `time_total=1637.7` (27.3 minutes; wall 1641.1 s); peak kernel memory 1,295.6 MB working set,
  1,513.9 MB private, so allow about 2 GB of free memory for this mode;
* the report (355 lines, 18,738 bytes, sha256
  `d55e3a7b7a84961196e8196e7cbf28a5cc78a3e47176c3c9f08add4bf26e892b`) differs from the committed one in
  exactly four places: one more line in `verbatimKDeltaUse` ("k = 3, the 8 diagonal components again:
  every 3-tuple of the 156 nonzero R^ab_cd (30371328 calls), no skip"), the extra check
  `k3_diagonal_unpruned_equals_skip_sum` (PASS: 156^3 = 3,796,416 calls of `kδ` per component,
  30,371,328 in all, the same P_(3) and the same 426,240 nonzero `kδ` terms as with the skip), an extra
  entry `"3_unpruned"` under `lovelockKDeltaCalls`, and `"checkCount":30`, `"expectedCheckCount":30`;
* its `gkd-values.bin` had the same sha256 `3ddccfa744b3708bbd3e251852236b0a2d3370e957c67bae8d94168de6d2d695`, and the
  clone was still clean afterwards.

---

## 5. Side effects

What a run of the documented command creates, overwrites or starts:

* **In the repository:** it OVERWRITES `Revision/gkd_lovelock/results/wolfram-gkd-report.json` (the
  committed file; with Wolfram 15.0.1 the bytes are identical, so git reports no change). It creates
  and changes NOTHING else: after each verification run, `git status --porcelain --ignored
  --untracked-files=all` in the clone printed nothing at all (no new, changed or ignored file; in
  particular no `target` folder appears in `Revision/gkd_lovelock/code`).
* **In the export directory** (default `<$TemporaryDirectory>/revision_gkd_export`, on Windows
  `C:\Users\<you>\AppData\Local\Temp\revision_gkd_export`): created if it does not exist;
  `Cargo.toml` and `src/main.rs` written (rewritten only when their text changes; `Cargo.toml` changes
  whenever you run from a clone in another folder, which makes cargo rebuild); `Cargo.lock` and
  `target/` written by cargo; `gkd-values.bin` deleted and rewritten (3,161,984 bytes). After a first
  build in an empty folder the export directory held 24 files, about 5.3 MB on disk (Windows; 6.8 MB
  if the two hard-linked files, the exporter's `.exe` and `.pdb`, are counted twice, as PowerShell's
  `Measure-Object` does). The folder is NOT deleted at the end; it is reused by the next run. The
  default folder is SHARED by every clone on the computer, and each rebuild for a clone in another
  folder adds a further set of build files under `target/` (7 files, about 0.66 MB: one more
  `lovelock_gkd-<hash>` fingerprint folder and its `.rlib`, `.rmeta` and `.d` files in `deps`), which
  are never removed: measured, 24 files after a first build and 31 files (about 6.0 MB on disk) after
  a second build from another clone; on the verification machine, after builds from four clone folders,
  the default folder held 45 files, about 7.3 MB on disk. Delete the folder to reclaim the space (the
  next run rebuilds it, in a few seconds). The compiled
  `lovelock_gkd_export.exe` is not byte-identical between builds (Windows executables carry
  build-specific data); this does not matter, because the values it writes are identical.
* **Temporary files of WolframScript:** on Windows, every run of `wolframscript` creates TWO files in
  `C:\Users\<you>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary\`: `tmp_<10 letters>`, empty,
  at the start, and a second `tmp_<10 letters>`, created when the kernel starts, that holds a copy of
  everything the script prints (about 1.8 KB for a full run of this script).  A normal exit removes both.
  A run that is interrupted (Ctrl+C, closing the window, a killed process) leaves BOTH behind; they are
  harmless and can be deleted with
  `Remove-Item "$env:LOCALAPPDATA\Wolfram\WolframScript\WolframScriptTemporary\tmp_*"` (PowerShell) when no
  other wolframscript is running.  Like every start of a Wolfram kernel, the kernel may also update its
  own settings and caches under the Wolfram user folders (on Windows `C:\Users\<you>\AppData\Roaming\Wolfram`
  and `...\AppData\Local\Wolfram`); these are outside the repository and not specific to this script.
* **Processes started:** one Wolfram kernel (the process `wolfram.exe` with Wolfram 15 on Windows; on
  other versions and systems its name may differ, for example `WolframKernel`) for the whole run,
  started and stopped by `wolframscript` (on Windows a second, short-lived `wolfram.exe` of about
  16 MB was also seen during the first second); NO parallel subkernels (the script uses no
  `Parallel...` function); `cargo` (through the `rustup` proxy) and `rustc` for the build; on Windows
  also a console host `conhost.exe` (about 7 MB) for these console child processes (observed as a
  child of `rustup.exe`, which the kernel starts); and the compiled exporter `lovelock_gkd_export`
  once, for under a second. All of them end before the script does.
* **Network:** none needed. The crate has no dependencies, so cargo downloads nothing; the script
  contains no internet function. Observed during the runs (all TCP and UDP endpoints of every process
  of the run, polled every 0.4 s): only loopback connections `127.0.0.1` <-> `127.0.0.1` inside the
  kernel process, no other address, no UDP. In the re-verification of 2026-10-07 (endpoints polled about
  once a second) the kernel was also seen holding a LISTENING socket on `0.0.0.0:<port>` (an
  operating-system-chosen port, for example 55639; remote end `0.0.0.0:0`) together with its own
  loopback connection to it, `127.0.0.1:<another port>` <-> `127.0.0.1:<port>` (observed in two of the
  three runs; in the third no endpoint was caught at all); this is the kernel's internal link, which a firewall may
  report as a program "listening for connections". No connection to any address other than `127.0.0.1`
  was seen, and no UDP. (Activating the Wolfram Engine, part 3.2, needs the internet once; this script
  does not.)
* **To restore the committed state** (from the repository root):
  `git checkout -- Revision/gkd_lovelock/results/wolfram-gkd-report.json`; to remove the export
  directory: `Remove-Item -Recurse -Force "$env:TEMP\revision_gkd_export"` (PowerShell) or
  `rm -rf "<the folder printed by wolframscript -code '$TemporaryDirectory'>/revision_gkd_export"`
  (macOS and Linux); after an interrupted run, also delete the WolframScript temporary files named above.

---

## 6. Verification record

* **Date:** 2026-10-02 (first verification); verified again on 2026-10-07 at commit `a4c5eda` (see
  "Re-verification after a restart" below).
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (main, equal to
  https://github.com/once-ere/Dirac_claude.git at the time). `verify_lovelock_gkd.wls`, the committed
  report and `PROVENANCE_OF_THE_COMPUTATION.md` were last changed in commit `70fab64`,
  `LovelockGKDCheck.wl` in `2c61fb0`, and the other inputs (`curvature.json`, `lovelock-tensors.json`,
  `lovelock-report.json` and the crate files `Revision/gkd_lovelock/code/Cargo.toml` and
  `Revision/gkd_lovelock/code/src/*.rs`) in `ad02ebb`, all on 2026-10-01 (as printed by
  `git log -1 --format=%h -- <path>` in a fresh clone); their digests are those of part 2.
* **Environment:** Windows 11 Pro for Workstations 10.0.26200, 24 logical cores, 191 GB RAM; WolframScript
  1.14.0, Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence (no kernel
  limit); cargo 1.91.1 (ea2d97820 2025-10-10), rustc 1.91.1 (ed61e7d7e 2025-11-07); PowerShell 7.6.6.
  Python is not used by this set.
* **Fresh clones:** two clones made with `git clone https://github.com/once-ere/Dirac_claude.git` into an
  empty scratch folder. No uncommitted file was copied into them: the working tree had no uncommitted
  change in `Revision/gkd_lovelock/`.
* **Runs** (each the documented command, from the clone root, report to the committed path):
  * run 1: clone 1, default export directory (it already existed from an earlier verification with a
    different clone path, so `Cargo.toml` was rewritten and the exporter rebuilt);
  * run 2: clone 1 again, default export directory (up to date, no rebuild);
  * run 3: clone 2, with `TEMP` and `TMP` pointed to a new empty folder, so that Wolfram's
    `$TemporaryDirectory`, and with it the export directory, started EMPTY (a first build from nothing,
    as on a student's computer). Only `revision_gkd_export` appeared in that temporary folder.
* **Results:**

  | run | exit code | stderr | checks | failed | `time_total` (s) | wall (s) | report sha256 | identical to committed |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 1 | 0 | empty | 29 | 0 | 95.3 | 98.1 | `de3678170c7d...e86bb1` | yes |
  | 2 | 0 | empty | 29 | 0 | 100.3 | 103.4 | `de3678170c7d...e86bb1` | yes |
  | 3 | 0 | empty | 29 | 0 | 111.9 | 115.5 | `de3678170c7d...e86bb1` | yes |

  Byte identity per output: `wolfram-gkd-report.json` identical in runs 1, 2, 3 and identical to the
  committed file (full digest `de3678170c7d62114f4d8f8e0d8024ec688bb0be3f2f4a870333243851e86bb1`);
  `gkd-values.bin` identical in all runs (`3ddccfa744b3708bbd3e251852236b0a2d3370e957c67bae8d94168de6d2d695`, hashed
  directly after runs 2 and 3, and recorded as `valuesFileSha256` in the identical reports of all three
  runs); the exporter source `src/main.rs` identical
  (`b5130177e38adba151c043fd5048f023b2ab6521acc32f620efcc2b8e794a372` = `exporterMainRsSha256`); the
  standard output identical in all runs apart from the `time_...` numbers; `git status --porcelain
  --ignored --untracked-files=all` empty in both clones after every run.
* **Check counts:** 29 checks, 29 PASS, 0 FAIL (expected 29) in every default run.
* **The repository's own test of this set** also passed in clone 2 (Python 3.14.5, sympy 1.14.0,
  `PYTHONDONTWRITEBYTECODE=1`, temporary files under a scratch folder):
  `python -m unittest Revision.tests.test_gkd_lovelock.TestCommittedOutputs Revision.tests.test_gkd_lovelock.TestSlowRuns.test_SLOW_wolfram_check_reproduces_the_report -v`
  ran 6 tests, all OK, in 114.0 s; its slow test ran this script a fourth time (report and export
  directory in a temporary folder) and found the pinned sha256 `de3678170c7d...e86bb1`. The clone was
  still clean afterwards.
* **Optional `diagonal` mode** (run once, clone 1, report outside the repository, own export folder):
  exit code 0, 30 checks, 0 failed, `time_total` 1637.7 s; its report differs from the committed one
  exactly by the four additions listed in part 4.5.
* **Re-verification after review** (same day, same commit, two NEW fresh clones, nothing copied into
  them; each run with its own scratch export directory set by `LOVELOCK_GKD_EXPORT_DIR`, and every
  process started under `wolframscript.exe` recorded with its parent, polled every 0.2 s):
  * run A: clone 1, export directory empty at the start: exit code 0, standard error empty, 29 checks,
    0 failed, `time_total` 96.6 s (wall 100.0 s); afterwards the export directory held 24 files,
    6,815,606 bytes when the sizes are added (the exporter's `.exe`, 151,040 bytes, and `.pdb`,
    1,339,392 bytes, are each counted twice because `target/release` and `target/release/deps` hold
    hard links to the same file), that is 5,325,174 bytes on disk. Processes: `wolfram.exe` (twice:
    a short start-up process of 16.5 MB, then the kernel, peak working set 484.7 MB), `rustup.exe`
    (13.3 MB) started by the kernel, `cargo.exe` (16.2 MB) and `conhost.exe` (7.4 MB) both children of
    `rustup.exe`, two `rustc.exe` (up to 79.3 MB) and the linker `link.exe` (56.3 MB). (The exporter
    itself ran for less than one poll interval and was not caught.)
  * run B: clone 2 with the SAME export directory: exit code 0, standard error empty, 29 checks,
    0 failed, `time_total` 102.9 s (wall 106.5 s); cargo rebuilt the crate for the new path, and the
    export directory grew to 31 files, 7,480,485 bytes added up, 5,990,053 bytes on disk (one more
    `lovelock_gkd-<hash>` set). Processes: `wolfram.exe`, `rustup.exe`, `cargo.exe`, `rustc.exe`,
    `conhost.exe` (7.4 MB, child of `rustup.exe`).
  * In both runs the report was byte-identical to the committed one (`de3678170c7d...e86bb1`), the
    standard output was identical apart from the `time_...` numbers, `gkd-values.bin` had sha256
    `3ddccfa7...d2d695`, `src/main.rs` had sha256 `b5130177...e794a372`, and `git status --porcelain
    --ignored --untracked-files=all` was empty in both clones afterwards. The shared default export
    folder on this machine held, at that time, 45 files: 8,798,311 bytes added up, 7,307,879 bytes on
    disk (`du -sb`), after builds from four different clone folders.
  * cargo NOT on the PATH (every PATH entry containing `cargo` removed, so `Get-Command cargo` found
    nothing; clone 1, new empty export directory): standard output `time_definition=0.0`, an empty
    line, `RunProcess::pnfd: Program cargo not found. Check Environment["PATH"].`, then
    `ERROR: cargo build of the GKD exporter failed`; standard error empty; exit code 2 after 7.0 s
    (wall); the export directory then held only `Cargo.toml` and `src/main.rs`; the clone stayed clean.
  * cargo found but the build failing (forced with `RUSTFLAGS=--bogus-flag-xyz`; clone 1, new empty
    export directory): standard output `time_definition=0.0`, then
    `ERROR: cargo build of the GKD exporter failed`, then cargo's own text, starting with
    ``error: failed to run `rustc` to learn about target-specific information`` and ending with
    `error: Unrecognized option: 'bogus-flag-xyz'`; standard error empty; exit code 2 after 3.7 s
    (wall); a `conhost.exe` was started as a child of `rustup.exe` here too.
  * These runs corrected four statements of the first version of this file (the commits that last
    changed each file, part 6; the messages of a failed cargo build, part 3.6; what may differ on
    another Wolfram version, part 3.6; the growth of the export directory and the `conhost.exe`
    process, parts 2.3, 3, 4.4 and 5). No file of the set was changed.
* **Re-verification after a restart (2026-10-07).** The verification workflow was interrupted by a
  session limit and relaunched; nothing written earlier was trusted, everything was measured again.
  * Commit verified: `a4c5eda1df069a43a55ff8b57148f5de8edd1670` (main, equal to
    https://github.com/once-ere/Dirac_claude.git at the time). Between `c2b33cc` and `a4c5eda` no file of
    the set, no input and not the committed report changed (`git diff --stat` over
    `Revision/gkd_lovelock` shows only the two provenance files added); in fresh clones of `a4c5eda` all
    fifteen digests of part 2 and the report digest were measured again and are the same; `git log -1`
    gives the same last-change commits as above (`70fab64`, `2c61fb0`, `ad02ebb`). The snapshot commits
    made while this re-verification ran (up to `72fc9ff`) changed no file of the set, no input and not
    the report (only provenance files, among them a partial copy of this file).
  * Environment: Windows 11 Pro for Workstations 10.0.26300, 24 logical cores; WolframScript 1.14.0,
    Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence; cargo 1.91.1
    (ea2d97820 2025-10-10), rustc 1.91.1 (ed61e7d7e 2025-11-07); PowerShell 7.6.6; Python 3.14.5 with
    sympy 1.14.0 (only for the repository test below).
  * Fresh clones: two new clones made with `git clone https://github.com/once-ere/Dirac_claude.git` into
    an empty scratch folder; NO uncommitted file was copied into them (the working tree had no
    uncommitted change in `Revision/gkd_lovelock/`). Every run was the documented command
    `wolframscript -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json`
    from the clone root, with no `LOVELOCK_GKD_...` variable set, and with `TEMP` and `TMP` pointed to
    a new, empty scratch folder, so that Wolfram's `$TemporaryDirectory`, and with it the default export
    directory `revision_gkd_export`, started EMPTY and was private to these runs (verified: it was the
    only entry that appeared in that folder).
  * run 4: clone 1, export directory empty (a first build from nothing); run 5: clone 1 again, same
    export directory (up to date, no rebuild); run 6: clone 2, same export directory (`Cargo.toml`
    rewritten with the new crate path, so cargo rebuilt the crate).

    | run | exit code | stderr | checks | failed | `time_total` (s) | wall (s) | report sha256 | identical to committed |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | 4 | 0 | empty | 29 | 0 | 128.2 | 133.3 | `de3678170c7d...e86bb1` | yes |
    | 5 | 0 | empty | 29 | 0 | 135.0 | 139.9 | `de3678170c7d...e86bb1` | yes |
    | 6 | 0 | empty | 29 | 0 | 117.3 | 121.6 | `de3678170c7d...e86bb1` | yes |

  * Byte identity per output: `wolfram-gkd-report.json` byte-identical between runs 4, 5 and 6 and to the
    committed file (`cmp` against `git show HEAD:...`; full sha256
    `de3678170c7d62114f4d8f8e0d8024ec688bb0be3f2f4a870333243851e86bb1`, 344 lines, 18,135 bytes);
    `gkd-values.bin` 3,161,984 bytes with sha256
    `3ddccfa744b3708bbd3e251852236b0a2d3370e957c67bae8d94168de6d2d695` after every run (hashed directly
    after each run, and equal to `valuesFileSha256` in the report); the exporter's `src/main.rs`
    identical (`b5130177e38adba151c043fd5048f023b2ab6521acc32f620efcc2b8e794a372` = `exporterMainRsSha256`);
    the exporter's `Cargo.toml` differs between the two clones only by the crate path, as expected
    (part 2.3); standard output identical in all three runs apart from the `time_...` numbers (43 lines;
    on Windows the lines end with CR LF) and equal, line by line, to the listing of part 4.1;
    `git status --porcelain --ignored --untracked-files=all` empty in both clones after every run, and no
    `target` folder in `Revision/gkd_lovelock/code`.
  * Export directory: 24 files after run 4 (6,815,718 bytes added up, 5,325,286 bytes on disk with
    `du -sb`), the same 24 files after run 5, and 31 files after run 6 (7,480,703 bytes added up,
    5,990,271 on disk): the rebuild for clone 2 added the 7 files of one more `lovelock_gkd-<hash>` set
    (`.rlib` 590,136 bytes, `.rmeta` 68,005 bytes, `.d` and four fingerprint files), as described in
    parts 2.3 and 5. (The sizes differ by about a hundred bytes from 2026-10-02 because cargo's
    fingerprint files hold the clone path, which was longer here.)
  * Processes seen under `wolframscript.exe` (polled every 0.25 s): two `wolfram.exe` (a short start-up
    process of about 50 MB, then the kernel, peak 485-486 MB working set, 700 MB private), `rustup.exe`
    started by the kernel, `cargo.exe` and `conhost.exe` as children of `rustup.exe`, and `rustc.exe`
    under `cargo.exe` during the builds of runs 4 and 6 (none in run 5, where nothing was rebuilt). No
    parallel subkernel.
  * Check counts: 29 checks, 29 PASS, 0 FAIL (expected 29) in every run; the numbers in the details are
    those quoted in parts 1.2 and 4.3 (for example 0 mismatches and +1: 1008, -1: 1008, 0: 260128 for
    length 3; 696, 32,640 and 495,360 nonzero `kδ` terms; 1,128,960 calls for k = 3).
  * The repository's own test, in clone 2 (`PYTHONDONTWRITEBYTECODE=1`, `TEMP`/`TMP` in a scratch folder):
    `python -m unittest Revision.tests.test_gkd_lovelock.TestCommittedOutputs Revision.tests.test_gkd_lovelock.TestSlowRuns.test_SLOW_wolfram_check_reproduces_the_report -v`
    ran 6 tests, all OK, in 128.5 s (exit code 0); its slow test ran this script a seventh time (report
    and export directory in a temporary folder, removed by the test afterwards: the scratch `TEMP`
    folder was empty again) and found the pinned sha256 `de3678170c7d...e86bb1`. The clone was still clean.
  * The optional `diagonal` mode (part 4.5, 27 minutes) was not run again: none of its inputs changed.
* **Fixes made (2026-10-07):** none. The set executed correctly as committed; no file of the set was changed.
* **Open discrepancies:** none. Note for other installations: the report records the Wolfram version
  in its `producer` line, so byte identity with the committed report holds on Wolfram 15.0.1; on another
  version expect at least that line to differ, and possibly the `InputForm` text of the 24 components
  under `measurements` -> `wolframComponents` (not tested here); all 29 checks must still pass. The
  macOS and Linux commands are the same command line as on Windows, but only Windows was available for
  this verification.

### 6.3 Fix and re-verification of 2026-10-08

* **Defect (found by the independent verifier of 2026-10-08):** the script reported SUCCESS and exited 0
  even when it could not write its report (the same false-success class as the defect fixed in
  `scripts/verify_dirac16complex_primordial.wls`, commit b980c80).
* **Fix:** `writeBytes` now checks that the folder can be created, that the file opens for writing, and
  that the written file exists with the expected number of bytes; otherwise it prints
  `ERROR: cannot write <path> (...)` and exits with code 2.  Script sha256 `bec6c8c5d25f62061b549a93fb5dc8e66c396cad1cd9bc6f08826129ae965a50` (574 lines,
  36,660 bytes; it was `2a3bb5fa612f74d7de7bbc0d47e3b029d9e00a4dccb36d1624329f0b1a23f943`).
* **Effect on the committed report:** only the line `sourceSha256` -> `verify_lovelock_gkd.wls` changed.
  New report sha256 `71c3f34f2f84662fbed6733379bea115ffad460dbae38f641c692c6824399189` (344 lines, 18135 bytes).  The pinned digest in
  `Revision/tests/test_gkd_lovelock.py` was updated.  All 29 checks pass (verdict SUCCESS, exit code 0);
  `time_total` of the regeneration run 68.4 s on a loaded machine.
* **Failure path, measured:** a report path below an existing FILE (so its folder cannot be created)
  gives the single line `ERROR: cannot write ...` and exit code 2; nothing is written.
* Also corrected in this file on 2026-10-08: the temporary files of WolframScript (two files, and what an
  interrupted run leaves), the disk space of a clone, the expected output on macOS/Linux, the failure table.
