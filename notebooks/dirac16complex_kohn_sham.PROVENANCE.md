# Provenance of the Jupyter notebook `notebooks/dirac16complex_kohn_sham.ipynb` (old Stage 4: Kohn-Sham DFT in the primordial gravitational field)

This file is written for a student who has never used Python, Jupyter or Rust. It explains one notebook of this repository: what it computes, which files it reads and writes, how to install everything it needs and run it on Windows, macOS or Linux, what it prints, what it changes on your computer, and how it was tested on 2026-10-02 and tested again on 2026-10-07 and 2026-10-08. Everything you need is in this file; you do not have to open any other file to run the notebook.

Contents:

1. What the notebook is and what it computes
2. Its files
3. How to run it (complete instructions)
4. The expected output
5. Side effects
6. Verification record

**The result of the test in one paragraph (read this first).** The notebook **executes**. It was tested in fresh clones on 2026-10-02 (runs 1 to 6, Windows and Linux), on the afternoon of 2026-10-07 (runs 7 to 9, Windows) and, after a session limit had interrupted that work, once more from new fresh clones on the evening of 2026-10-07 and the morning of 2026-10-08 (runs 10 and 11 on Windows, run 12 on Linux, run 13 the reproduction of the committed files; Section 6.3), so that every statement of this file was checked again instead of trusted; an independent verification of this file then found nine inaccuracies of the description (none of the results), which were re-checked in a further fresh clone (run 14, 2026-10-08) and corrected (Section 6.6). In every run every one of its 18 code cells ran in every route (the repository's own runner, Jupyter's `nbconvert`, the builder's `--execute`, and, in runs 5 and 8, JupyterLab in a browser). Its last cell, the "gauntlet" of 60 checks, prints **58 PASS and 2 FAIL** and therefore ends, on purpose, with an `AssertionError`; the audit program then reports `check_count=74`, `failed_check_count=4` and the verdict `FAILURE`. The two failed checks are not execution errors: they repeat an open scientific discrepancy that the repository already documents (two deep levels of one run of the Rust solver differ from the independent reference solver by about twice the tolerance; Section 6.6). The outputs of two runs on Windows with the package versions of Section 3.9 are byte-identical to each other (runs 1 and 5 on 2026-10-02, runs 7 and 8, and runs 10 and 11 on 2026-10-07): the executed copy of route C has the same bytes in all six runs, and so has the audit report wherever it was written with the paths of Section 3.10 (runs 5, 7, 8, 10 and 11). Compared with the committed files, all 15 re-computed spectrum files are byte-identical (on Windows and on Linux) and 13 of the 14 figures are byte-identical on Windows (on Linux they are identical pixel for pixel but compressed differently); the executed notebook, the notebook report and the figure `rust_vs_reference.png` are not, because the committed copies were made on 2026-09-30, before three of their input files changed; with those inputs restored to their state of that day, all three are reproduced **byte for byte** (runs 3, 9 and 13; Section 6.4). No file of the set and no committed output was changed by this verification, and no execution defect was found that needed a fix.

**Update of 2026-10-08 afternoon (stage4-fix; read this too).** The cause of the two failed gauntlet checks was found and fixed in the two programs the notebook imports (erratum E4.14 of `handoff/specs/STAGE4_SPEC.md`; Section 6.6): the cross-checker `scripts/check_dirac16complex_kohn_sham.py` now adds to the tolerance of every eigenvalue the measured Rust grid change of that level between the 301- and 601-point runs (the rule E4.12 already applied to the scalars), and the reference solver `scripts/ks_reference_solver.py` builds the Delta-SCF occupations of every grid level from that level's own ground state. Both files therefore no longer have the SHA-256 of Section 2.2 (their new values are given there). The notebook itself, its builder, runner, auditor and unit tests are unchanged, and so are the committed executed notebook (`7efa2270763af5224ec5c2c99e5d61d4d29c40c6a1d1007c4451defbecc6be99`), `notebook-report.json` and the figures: they were **not** refreshed, because two steps that must come first are open (Section 6.6): the reference rerun of one run under the new Delta-SCF rule (about 4.5 hours) and a decision on the preserved first-edition textbook, whose sentence "63 checks of which 1 failed" a unit test ties to the committed cross-check report. With the fixed programs, in a scratch copy of the repository (not committed), the cross-checker gave 63 checks, 0 failed, and the notebook's gauntlet 60 PASS, 0 FAIL, 0 SKIP (Section 6.6). Everything else in this file describes the committed state and the runs of 2026-10-02 to 2026-10-08 morning, which used the programs with the SHA-256 values of Section 2.2.

## 1. What the notebook is and what it computes

### 1.1 The files of the set

The set consists of four Python programs and the notebook itself:

- `notebooks/dirac16complex_kohn_sham.ipynb` is the **notebook**: a Jupyter notebook (a JSON file that holds explanatory text, Python code and the results of the code) with 43 cells, 25 of them text ("markdown") and 18 of them Python code. The committed copy contains the outputs of an earlier execution.
- `notebooks/build_dirac16complex_kohn_sham_notebook.py` is the **builder**: it writes the notebook from scratch. It reads the committed result files and fills every number quoted in the text of the notebook from them, so that the text cannot disagree with the files. With `--execute` it also executes the notebook (through `nbclient`, the library under Jupyter's executor).
- `notebooks/run_notebook.py` is the **runner**: a small executor that uses only the Python standard library. It runs every code cell in order and writes the results back into the notebook file **only if every cell succeeded**.
- `notebooks/check_dirac16complex_kohn_sham_notebook.py` is the **auditor** (the "checker"): it reads one or two executed copies of the notebook, checks 13 rules (headings, instructions, execution order, no error output, the gauntlet, the figures, the kernel, the format, and that the cells equal the builder's), compares the two copies, and writes a report.
- `tests/test_d16c_kohn_sham_notebook.py` holds 30 unit tests of the builder and the auditor, and of the committed report.

The notebook calls one compiled program, the Rust solver `studies/dirac16complex_kohn_sham` (it starts it twice), and it imports the independent cross-checker `scripts/check_dirac16complex_kohn_sham.py`, which in turn imports the reference solver `scripts/ks_reference_solver.py` (Section 2.2).

### 1.2 What it computes, in plain words

"Stage 4" of the earlier `dirac16complex` work treats a gas of N quanta of the field `dirac16complex` (a 16-component complex field of anticommuting numbers in eight dimensions) that is bound in the **static** primordial gravitational field, with a **Kohn-Sham density-functional** method (a "DFT-type" approximation in Mermin's finite-temperature form). It computes ground states, first excited states, thermodynamics and the energy-momentum tensor. The heavy computation (hours) was done earlier by the Rust solver, whose results are committed under `artifacts/dirac16complex/kohn-sham/rust/`. The notebook is the complete numerical documentation of that stage. In order, its cells

1. read every committed result file (cell 1);
2. find the Rust program, start it once to print its configuration (`print-config`), and set up a deterministic figure writer (cell 2);
3. **re-run** the cheapest subcommand of the Rust program, `spectrum` (about 45 seconds), into the scratch folder `build/notebook-kohn-sham/` and compare all 15 files it writes byte for byte with the committed ones (cell 3);
4. recompute the key quantities **independently** in Python: the exact reduction of the 16-component equation to eight 2 x 2 blocks from the integer gamma matrices, the exchange energy of the uniform gas against a tabulated double integral, the analytic k = 0 spectrum and the slope of the brane zero mode (by its own Runge-Kutta shooting), the particle numbers and energies of all 65 self-consistent runs, the Kohn-Sham gaps and particle-hole lists, the level crossing of the hardest run, entropy, free energy and heat capacity, the energy-momentum tensor and its conservation, the brane localisation and the convergence in the tip cutoff, the grid and the momentum lattice (cells 4 to 16);
5. compare the Rust results run by run with the **independent reference solver** (a matrix method on staggered grids) with exactly the rules and tolerances of the cross-checker (cell 17);
6. draw **14 figures** into `artifacts/dirac16complex/kohn-sham/figures/` (PNG files written without a time stamp or program name, so that on Windows the same input gave the same bytes in every run);
7. end with the **gauntlet**: 60 checks, each printed as one line `PASS - name: detail` or `FAIL - name: detail` (or `SKIP - ...` when an input file is absent). One of them re-reads all 171 numbers and strings quoted in the text from the committed files. If any check fails, the cell prints all of them and then raises an `AssertionError` (cell 18).

The notebook does **not** re-run the heavy subcommands of the Rust program (`scf`, `excited`, `thermo`, `emt`; about four hours); it reads their committed results and relies on the committed determinism report for their reproducibility.

### 1.3 About charge conjugation

This notebook neither defines nor uses a charge conjugation. The 16 x 16 matrices called C and B in it are the Dirac-conjugation matrix (C = gamma^0 gamma^1 gamma^2 gamma^3) and the matrix of the expectation-value rule (B = -i C gamma^4). In this repository the charge conjugation of the field is a matrix operation (a 16 x 16 matrix combined with complex conjugation), not plain complex conjugation of the field components.

### 1.4 Documents that cite its results

- `provenance/DIRAC16COMPLEX_TEXTBOOK.md` and `.tex` (the earlier teaching textbook; its chapters are also stored one per file in `provenance/textbook/chapters/`): Chapter 13 (`13-kohn-sham-primordial.md`) shows ten of the 14 figures of `artifacts/dirac16complex/kohn-sham/figures/` (block structure, Kohn-Sham spectrum, exchange of the uniform gas, density profiles, level crossing, self-consistency history, gap and Delta-SCF, thermodynamics, energy-momentum tensor, Einstein source) and names an eleventh, `ground_state_energy.png`; Chapter 19 (`19-reproducing-everything.md`) states that `notebook-report.json` has "68 of 74 checks true and the verdict FAILURE" and that "the notebook has not been executed again since"; Chapter 20 (`20-glossary-and-check-index.md`) lists `kohn-sham/notebook-report.json` under the abbreviation NB.
- `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md` (the Stage-4 document): names "a Jupyter notebook" among the independent verifications and `notebook-report.json` among its sources.
- `handoff/specs/STAGE4_SPEC.md` (the specification of Stage 4: the notebook is one of its deliverables) and `HANDOFF.md.txt`.
- `provenance/wolframscript/verify_dirac16complex_kohn_sham.PROVENANCE.md` (the provenance file of the Wolfram verifier of the exact Kohn-Sham theory, whose report `wolfram-kohn-sham-report.json` this notebook reads): names this notebook and this provenance file among the places that show results of that verifier.
- `HANDOFF.md` (the project's hand-over notes): its fresh-clone test of 2026-10-07 lists the four failing `TestCommittedReport` tests of `tests/test_d16c_kohn_sham_notebook.py` (Section 6.5) as an old, known failure of old Stage 4, and leaves open whether old Stage 4 is to be finished or formally marked as superseded by the newer Kohn-Sham work in `Revision/kohn_sham/` (Section 6.6).

Two neighbouring sets are **not** part of this one. The Mathematica version of Stage 4 (`notebooks/Dirac16ComplexKohnSham.nb`, built by `scripts/build_dirac16complex_ks_mathematica_notebook.wls` and evaluated by `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`, each with its own provenance file in `provenance/wolframscript/`) draws its six figures into the subfolder `artifacts/dirac16complex/kohn-sham/figures/mathematica/`, which this notebook neither reads nor writes. The newer Kohn-Sham work of the revision, `Revision/kohn_sham/`, is a separate set as well: this notebook reads no file in `Revision/` (Section 2.5), so the changes made there on 2026-10-07 (for example to `Revision/kohn_sham/theory/check_ks_theory.py` and to the thermal Kohn-Sham outputs) do not affect it.

### 1.5 Programs that run or read it

- The Stage-4 gate `scripts/verify_stage4_kohn_sham.ps1` / `scripts/verify_stage4_kohn_sham.sh` (steps `stage4-24` to `stage4-29`: it clears the outputs of a copy of the notebook, executes it with the runner and with `nbconvert`, audits both copies and compares the fresh report with the committed one, through `scripts/verify_stage4_kohn_sham_audit.py`). The gate had not been run when this file was written, and it was not run for the re-tests of 2026-10-07 and 2026-10-08 either: its notebook steps require exit code 0 from the runner and from `nbconvert` (without `--allow-errors`), which today is impossible because of the two failed gauntlet checks (Section 4.1). Its comparison step 28 was run on its own (Section 6.3, runs 7, 8, 10 and 11, and in the reproduction runs 9 and 13).
- The unit tests `tests/test_d16c_kohn_sham_notebook.py` (Section 6.5).

## 2. Its files

All paths are relative to the repository root (the folder `Dirac_claude` that `git clone` creates). "Lines" is the number of line-feed characters (what `wc -l` prints); all text files use LF line endings. The SHA-256 values are those of commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the commit tested on 2026-10-02); every value, line count and size in Section 2 was checked again on 2026-10-07 in the fresh clone of commit `d806b00cfd769141b9d3f2c6c46a72de5d8027a2`, and once more after the restart of that evening in the fresh clones of commits `b8a695d1faa7abe43b4b51eb666f25d250420fb7` and `603f1506a143f731ea1661a040110077c920b785` (runs 10 to 13), and is unchanged there: `git diff --name-only c2b33cc 603f150` lists no file of the set, no input and nothing in `artifacts/dirac16complex/kohn-sham/` or `studies/dirac16complex_kohn_sham/` (Section 6.1).

### 2.1 Program files of the set

| Role | Path | SHA-256 | Lines | Bytes |
|---|---|---|---|---|
| notebook (committed, executed on 2026-09-30) | `notebooks/dirac16complex_kohn_sham.ipynb` | `7efa2270763af5224ec5c2c99e5d61d4d29c40c6a1d1007c4451defbecc6be99` | 3759 | 1852018 |
| builder | `notebooks/build_dirac16complex_kohn_sham_notebook.py` | `e88f95cf6f5f582d5e09ac7c62b050590244a2e8bb0663cdf208d98e41cdecbb` | 3179 | 173650 |
| runner | `notebooks/run_notebook.py` | `ef5bbd8c082f2e17ed2c894788f5f9edd791a23ecb25ebe266881fe2d7cff40c` | 125 | 4503 |
| auditor | `notebooks/check_dirac16complex_kohn_sham_notebook.py` | `4ee6dfdca59b076bcec372dca4b82f1c84e00009b178a83ab835d7ad5e1d9c91` | 510 | 26591 |
| unit tests | `tests/test_d16c_kohn_sham_notebook.py` | `f25efb6ba1490b95c81ca6aeb313c22caf9a68fef5cabb02464bcc063aada39a` | 457 | 22741 |

### 2.2 Programs it starts or imports

| What | Path | SHA-256 | Lines | Bytes |
|---|---|---|---|---|
| cross-checker (imported by cell 17; its function `compare_canonical` does the run-by-run comparison) | `scripts/check_dirac16complex_kohn_sham.py` | `a2883b47fd5a4febbf19fe479c1b7afaa1ba001621a0455e946e1682c02294ee` | 1711 | 92129 |
| reference solver (imported by the cross-checker; nothing is solved, only its reading functions are used) | `scripts/ks_reference_solver.py` | `7e710f4afcf9ee33a470919714c6f3a7a9b492bf2b7fd6cc27badc821e7f6486` | 3391 | 173385 |
| Rust crate manifest (the notebook also uses the existence of this file to find the repository) | `studies/dirac16complex_kohn_sham/Cargo.toml` | `92ad9c198f3dc7e8cd3dd5329de490eb4a119f37927767bd587d42ddbf583220` | 18 | 725 |
| Rust lock file | `studies/dirac16complex_kohn_sham/Cargo.lock` | `2ce5ddf57f5243aef4cc43f0a08359f75cb4a25876bf86c2af5b782ccfd82a05` | 22 | 358 |
| compiler flag `-C target-feature=+fma` (the committed outputs assume it) | `.cargo/config.toml` | `99c33150307443ab865e8732017dda6cf2fae032e11ca50a7a386cacbb7f68ce` | 4 | 194 |
| solver set-up script (PowerShell) | `scripts/setup_solver.ps1` | `d50ad2cc8aeb9f1d316a736aa466712ab12eed76925ec3105cbc0c81fdc54fb3` | 61 | 2423 |
| solver set-up script (bash) | `scripts/setup_solver.sh` | `9100b589bcbf2ab3e51c7d06087a5f27d2eff51d121a968475d11d054e819a6a` | 75 | 3002 |

**Changed on 2026-10-08 after the runs of Section 6.3** (stage4-fix, erratum E4.14 of the Stage-4 specification): the cross-checker is now `scripts/check_dirac16complex_kohn_sham.py` = `49813762965d2381599eebc045475531dd675b3ba5fc217fb5c02b14869e7f0a` (1767 lines, 95512 bytes) and the reference solver `scripts/ks_reference_solver.py` = `249c22bc3c4d7c8c3a61250bc8e424e167b7fe74e5bdf4902c899b14ed602679` (3436 lines, 176052 bytes). Every run of Section 6.3 used the values in the table above, and so did the committed outputs. The notebook reads only the reading functions of the reference solver (nothing is solved), and of the cross-checker it uses `compare_canonical`, whose eigenvalue tolerance changed (Section 6.6).

The Rust program itself, `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham.exe` on Windows (without `.exe` on macOS and Linux), is **not** in the repository: you build it (Section 3.8) from the sources in `studies/dirac16complex_kohn_sham/src/` and from the pure-Rust SUNDIALS 7.8.0 engine, which `scripts/setup_solver.*` downloads into `vendor/rustSolveIt` (repository https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 at the pinned commit `a8fdff459adfe181573d7924b18bffbdf378fdb3`). The notebook starts it twice: `dirac16complex_kohn_sham print-config` and `dirac16complex_kohn_sham spectrum --output <repository root>/build/notebook-kohn-sham`. The built program file is not byte-identical between two clones (the compiler writes the full folder names of the source files, used in its error messages, and of its debug-symbol file into it); the files it writes are (Section 6).

### 2.3 Inputs it reads

The Python process of the notebook reads **459 committed input files** of the repository (listed in Section 2.5; 215282859 bytes in total). In addition it re-reads the files that it and the Rust program have just written, the 14 figures (to embed them and to check their hashes) and the 15 fresh spectrum files of `build/notebook-kohn-sham/spectrum/`, and Python reads its bytecode cache of the two imported programs (`scripts/__pycache__/check_dirac16complex_kohn_sham.cpython-314.pyc` and `ks_reference_solver.cpython-314.pyc`; `314` is the Python version) when that cache exists. The counts 459 and 461 below are of the committed inputs (and, for 461, the runner and the notebook); a recording on 2026-10-08 (run 14 of Section 6.3, a first execution in a fresh clone) that counted every repository file the process tried to open found 492: the 459 inputs (the same list SHA-256 `c2e956ee...`), the 14 figures, the 15 fresh spectrum files, the two bytecode files, the runner and the notebook. The 459 were first measured on 2026-10-02 by executing the 18 code cells in one Python process, as route B does, with a Python audit hook that recorded every file the process opened. The measurement was repeated on 2026-10-07 in the fresh clones of runs 7 and 8 (Section 6.3), this time by letting `notebooks/run_notebook.py` execute a copy of the notebook under the audit hook: the 18 code cells read exactly the same 459 files with the same SHA-256 (the list of Section 2.5 came out byte for byte identical); the runner itself reads two more files, its own source `notebooks/run_notebook.py` and the notebook file it executes. After the restart of that evening the measurement was made once more in the fresh clones of runs 10 and 11 (461 files read, 217139380 bytes: the same 459 files with the same SHA-256 and the same list SHA-256 `c2e956ee...`, plus the runner and the notebook). In those recordings the cache `scripts/__pycache__/` already existed (or, in run 7, Python was told not to write it), and the only repository files the Python process opened for writing were the 14 figures. On a **first** execution, when `scripts/__pycache__/` does not exist yet and the environment variable `PYTHONDONTWRITEBYTECODE` is not set, the process also writes the two bytecode files there (run 14: Python first tries to open them, then reads the two programs and writes the two files under temporary names that it then renames). The 15 spectrum files are written by the Rust program, a separate process. Outside the repository the Python process read only matplotlib's font cache (Section 5.2). The most important inputs:

| Input | Path | SHA-256 | Lines | Bytes |
|---|---|---|---|---|
| exact gamma-matrix fixture | `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 18440 | 213133 |
| exact theory (Wolfram) | `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json` | `5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a` | 4537 | 72176 |
| uniform-gas exchange table | `artifacts/dirac16complex/kohn-sham/exchange-table.json` | `42542b119b258f957e748861d30de7dbc8527f4c0a11f3a2cd6660d9ba98e0a3` | 11752 | 463846 |
| Wolfram theory report (125 checks) | `artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json` | `9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978` | 154 | 7079 |
| sympy theory report (157 checks) | `artifacts/dirac16complex/kohn-sham/python-theory-report.json` | `042ef6dc641fd3ec69cdc6d775832f824beb3b39f769e65eadfae8682a78356b` | 1219 | 44374 |
| cross-check report (63 checks, 1 failed) | `artifacts/dirac16complex/kohn-sham/python-check-report.json` | `a68a6466177d0dc485572dcc762115ba296e66594d3f51e3881ba75fab707ab8` | 11710 | 387714 |
| determinism report of the Rust runs | `artifacts/dirac16complex/kohn-sham/rust/determinism-report.json` | `3c65bc93ab53c13073e9bb07f8bc66c9b5327b170a2c14e2e67ee77cd9aa023c` | 501 | 16905 |
| reference-solver summary | `artifacts/dirac16complex/kohn-sham/reference/reference-summary.json` | `54d67b59bc06b599c37f1744b44de9a8d670f48addcae5230ee4d36917097ecf` | 50560 | 1745307 |
| Rust summary, `spectrum` | `artifacts/dirac16complex/kohn-sham/rust/spectrum/summary.json` | `52d4eb13142740b90ad7aad1c2868748501291ecd9c103149ecc1dadb95c5091` | 291 | 8197 |
| Rust summary, `scf` | `artifacts/dirac16complex/kohn-sham/rust/scf/summary.json` | `44017474744f7f501b0a07f5d64a1bb1e8fc8e8412ddf10a3e23313a2a101759` | 3671 | 150624 |
| Rust summary, `excited` | `artifacts/dirac16complex/kohn-sham/rust/excited/summary.json` | `99394347e61fd4b57f8bb38c60f542df9a46ab5151771ba443422c9f0d270a88` | 994 | 35087 |
| Rust summary, `thermo` | `artifacts/dirac16complex/kohn-sham/rust/thermo/summary.json` | `2d59bcec411c16a3dc4e4da71bced467f6c73dd113746a90c16c8a6c602f7fef` | 2696 | 111263 |
| Rust summary, `emt` | `artifacts/dirac16complex/kohn-sham/rust/emt/summary.json` | `d93d3d0879aa2f35685c610ca9c88fb77f1ac8600b9df3dd78a01573054ba6f7` | 1301 | 52330 |

The other 446 files are the per-run result files: the other 14 files of `rust/spectrum/`; `history.csv`, `levels.csv`, `profiles.csv` and `run.json` of each of the 33 runs in `rust/scf/`; `levels.csv`, `levels-excited.csv` and `particle-hole.csv` of each of the 16 runs in `rust/excited/` with `excitations.csv`; `levels.csv`, `profiles.csv` and `run.json` of the 22 runs in `rust/thermo/` (with `thermodynamics.csv`) and of the 10 runs in `rust/emt/` (with `emt-summary.csv`); `run.json`, `spectrum.csv` and `profiles.csv` of 50 runs in `reference/`; the two Python programs of Section 2.2; and `studies/dirac16complex_kohn_sham/tools/compare_runs.py` (its SHA-256 is compared with the determinism report). The complete list with every SHA-256 is in Section 2.5. The Rust program reads `kohn-sham-theory.json` and `exchange-table.json` itself as well; the gamma matrices are compiled into it (its source file `src/generated.rs` was generated from the fixture, which is what its configuration line `fixture source = fixture` says).

### 2.4 Outputs it writes

| Output | Path | Written by | SHA-256 of the committed file | Bytes |
|---|---|---|---|---|
| 14 figures | `artifacts/dirac16complex/kohn-sham/figures/*.png` (table below) | every execution of the notebook, always at this place (a copy of the notebook executed elsewhere still writes here) | see below | |
| 15 fresh spectrum files | `build/notebook-kohn-sham/spectrum/` (`build/` is ignored by Git) | cell 3 (the Rust program) | identical to the committed `artifacts/dirac16complex/kohn-sham/rust/spectrum/` files | |
| executed notebook | `notebooks/dirac16complex_kohn_sham.ipynb` in place, or a copy | the runner (only if every cell passes), the builder (default path), JupyterLab (when it saves) | `7efa2270763af5224ec5c2c99e5d61d4d29c40c6a1d1007c4451defbecc6be99` | 1852018 |
| executed copies | `build/nbconvert/dirac16complex_kohn_sham.ipynb`, `build/nbclient/dirac16complex_kohn_sham.ipynb` | `nbconvert`, the builder with `--output` | (not committed) | |
| notebook report | `artifacts/dirac16complex/kohn-sham/notebook-report.json` (committed), or the path given after `--report` | the auditor | `92822f2827d668f304efef0c4d93e48b35ba72310c53c12fdba4ff4254d68682` | 31065 |

The 14 figures (all PNG; the committed SHA-256):

| Figure | SHA-256 of the committed file | Bytes | Reproduced by a run on 2026-10-02 (and again on 2026-10-07) |
|---|---|---|---|
| `block_structure.png` | `5c5f5920db4ee7df2b5dcd24de2f645854973259f67d68556c9963f627189f6b` | 35851 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `brane_localisation.png` | `6664acfaf1399da98acd76be5c16449dab7236abf7d6c3991c6d077b719b14aa` | 66412 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `convergence.png` | `9eb2f88b2ae612604722d5977fa8dbe6ee993fe16a1b00930400d1ba41b61087` | 64834 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `density_profiles.png` | `896fa07f1873919c9103d851e53688d197c8969849b02b8c63acca260e67c3b8` | 190965 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `einstein_source.png` | `a99f04cbee0355b7b194fe2b98e1f70de9fa3b27d2aa624f0089f3a03074f24c` | 75000 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `emt_profiles.png` | `b5a3dfef0f3a5fa116aa08d022fda96259e33a633912507073c6e69383aeeaa8` | 142165 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `exchange_uniform_gas.png` | `883d4d70dabdf1a096f311d0676d9653e72bc31983232b97b4deb9db98b87f02` | 76865 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `fermi_level_N1016_lamm2.png` | `f08dd5ee9ac3b2716fd64a3a6f7c7e1e423138b25cb05c03f90faac4ed097ba2` | 47912 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `ground_state_energy.png` | `d0cd3b543b1d0de997534ef5e8cabeb026085a93548f4081e6720e02faf75f12` | 66171 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `ks_gap_delta_scf.png` | `9af7a6d79c51f98ff4e93f0aa1e427612b0c26d6465baf994760dc0c7f695906` | 105660 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `ks_spectrum.png` | `f468ecd9110e904511e7cbdeff9e5a6aef95920ee4a54f0f0da5340c6da3cdb4` | 73895 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `rust_vs_reference.png` | `b5bf9db23a8430af804d1270e74020aac4a4d18e80acfdde1d5465ca1f4e076b` | 70659 | no: a run on Windows writes `8d572f57621fc606df53454475caf9c24d63c61cfa616c192caddc3c2a1607b7` (74124 bytes), because its inputs changed (Section 6.4) |
| `scf_history.png` | `46efdfa00b517c5c2ffe04f159face0ff30dce71952b7b277782aabe8708aa03` | 69334 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |
| `thermodynamics.png` | `d6af59925692326c20963bd4c8495c01911ea9278a2eb456440d0e63aad36042` | 118644 | yes on Windows (byte-identical); on Linux the same pixels with other bytes |

The 15 files of the `spectrum` re-run (written into `build/notebook-kohn-sham/spectrum/`; each equal to the committed file of the same name in `artifacts/dirac16complex/kohn-sham/rust/spectrum/`):

| File | SHA-256 (committed and fresh) | Bytes |
|---|---|---|
| `closed-shells-m1-L3.csv` | `f0b13a0c234154f74c7e7530e1829a066f4ed062183797fbb962f23053d04d80` | 971 |
| `closed-shells-m3-L3.csv` | `398861d25ffc6f76b1f4f4dcced8637c1842b62e32124610d73601fd9e4e8dee` | 1067 |
| `exchange-check.json` | `0f72852a5384ce5f4279e00e6f3fec1dcb519032a3700c6156446a9eb84239a5` | 551 |
| `exchange-table-check.json` | `4fce3f82ef7f5b489f6b3f6cdde273f1a8816ae52e0c6fcc9e9b5d27827b9ec3` | 1225 |
| `free-spectrum-m1-L2.csv` | `e85632681b02a51898b17e3e57b761b24aff8abcd4ebc7f2f5aaba878c685d71` | 85540 |
| `free-spectrum-m1-L3.csv` | `49970f6a02862ae063d258c2546eb1f8232fc05f5ede78de8c6122c8c784665a` | 94198 |
| `free-spectrum-m1-L4.csv` | `58bc76f6c90ae347874f0640d208368d59c4f4c4c5687aaf348f98276d4ab162` | 97340 |
| `free-spectrum-m3-L2.csv` | `9c94abada90670bd2f3fa4d3946ac2d6ffda3b115c1a7e5a39925e372815cc68` | 257298 |
| `free-spectrum-m3-L3.csv` | `c9d4b01371ca748bbeda5b06402cc3c8b7bf1f884de992cfb43d15b776f3c7d8` | 280020 |
| `free-spectrum-m3-L4.csv` | `574da21949cd87a904fec35da634b3edd6607654ac24684bc09c8c68f71e5626` | 290916 |
| `geometry.json` | `8c1357007a865d02f1fa0b6c4275e1a7cfa5ae910e54a2f408819994a6bd2eba` | 2100 |
| `reduction.json` | `3d2081f6a12db3bba46788e748405fb9736b34ac6b5dedb7b612a7c7a1da2b9e` | 63894 |
| `summary.json` | `52d4eb13142740b90ad7aad1c2868748501291ecd9c103149ecc1dadb95c5091` | 8197 |
| `theory-agreement.json` | `42b47ef64141d57b96bdb2e23f66db34ce6a3e7c5a2d03f86c3d33cf20016448` | 2636 |
| `uniform-gas-table.csv` | `a70ea9fe71405d74d00b21f9bd0f5d4ff7d2a8ec4484d058b3a711ff0e4e0561` | 3918 |

### 2.5 Complete list of the input files read (SHA-256)

The list below has 459 lines, one per file, sorted by path, in the format of the `sha256sum` program (`<SHA-256>  <path>`). The SHA-256 of the list itself (the 459 lines, each ended by a line feed) is `c2e956ee44becdd0e132eac6a2c3379ab94b56ba5afd119b8f5e539a81dec7b9`.

<details>
<summary>Show the 459 input files and their SHA-256</summary>

```
8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b  artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
42542b119b258f957e748861d30de7dbc8527f4c0a11f3a2cd6660d9ba98e0a3  artifacts/dirac16complex/kohn-sham/exchange-table.json
5b150b36e13b903c32b86e8debbaeda48798e0beb0bc6a216e416d2671f4e01a  artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json
a68a6466177d0dc485572dcc762115ba296e66594d3f51e3881ba75fab707ab8  artifacts/dirac16complex/kohn-sham/python-check-report.json
042ef6dc641fd3ec69cdc6d775832f824beb3b39f769e65eadfae8682a78356b  artifacts/dirac16complex/kohn-sham/python-theory-report.json
6a0027515a2e312a62e2eb09477ab16461f91f6cdc16daae950cd728a221cddc  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lam0_T0/profiles.csv
1361f1233e3ba96c85b58a0d54ac14abf177caf483833cd1226228a035b337d7  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lam0_T0/run.json
03f4ef425995dd75cc48a4500ae68c102bb1e7b483d6e4ef802688ebb127de31  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lam0_T0/spectrum.csv
835a7e1c2bca7260997691ddfbf555331c4f0848b33ea8325dc0285d359dfc61  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lamp1_T0/profiles.csv
ae71578e2dd5054ccdaedb13d58f9c83b6f636d10f2aed527390ba57dad8e968  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lamp1_T0/run.json
137555001caa0957cb76999b49477e19acbbded17df6fa8d304f2c0e6e9e1a45  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N112_lamp1_T0/spectrum.csv
3b38e980407d7744eb58a5a195c47a0533d0097d1f65bf58c1c55adeb67dbb42  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lam0_T0/profiles.csv
7a8b1d2b42440eb6e65bdf7cc348ebe79242a93f5137ab834594f2b84902a155  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lam0_T0/run.json
23cc564d36884b6656eb144ba0f4aa60b94c4c35251fc8f0d388c7c286104025  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lam0_T0/spectrum.csv
6fa9c99742ea79a2310a4cdd95761c1e850bec6478a589005d7d917ba8a45640  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lamp1_T0/profiles.csv
3aba0292b7e4c67fa6a41b168810d6e383a78bb45987de0bce0813907e72f511  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lamp1_T0/run.json
2dca9ce05e4c5ff4cd8620125a92138322d610efc542af1bb60bd4f1b99a08f2  artifacts/dirac16complex/kohn-sham/reference/m1_L2_N8_lamp1_T0/spectrum.csv
51e91381799182cacef6d9d2ec53f610f8020efe34515b244c8d4ed47ebc1dc4  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lam0_T0/profiles.csv
812b88f7d68aad9c3447f8315cf34bf4340afa380316f6ebc261541d349631ff  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lam0_T0/run.json
21aa034da3432f5a1e078fc09c25a465e820c3688735d2400c8fc5730a920552  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lam0_T0/spectrum.csv
f5ccab73e026d3c83a83023ff4c66bd347f0200801c89fab14ca1340cc9e674d  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm1_T0/profiles.csv
93fd3a9bfe03f29f721e5052963dc2ca984fedaf7dff9bf1f221a5e3d759b790  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm1_T0/run.json
a193874985a456eb69c7d0da266e9740a7a844e5e6dfb970c6966c61867f21bf  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm1_T0/spectrum.csv
b365113ecae8131c46f682d62e5dc3471616b4eeaf9ece27af6ee881433c6953  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0/profiles.csv
98d74954f567e3a3299d13c82a1a89e125bbde0dd58b5aa430657fbbfd5cbe0c  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0/run.json
efff28a08973377ae0303bfa1b3305b844daf8c4dbf59cd688f36d85ad26cdc2  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0/spectrum.csv
a84c6212fd99a1a8072a09895d2de6af88fff8b99c655e5eef684c51910ff724  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp1_T0/profiles.csv
edaa4e2c68b0eb13b909b38686d9e7e65c04e125801557c902414aadae2b13fc  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp1_T0/run.json
348384451125cc5e95b776c1f0433c8ac60eb96852192fe74269f1c51dce1373  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp1_T0/spectrum.csv
616be768a5fd19b827020b1bd88ffe2b8e30b534cd2acd2b2573e47e839d1c31  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp2_T0/profiles.csv
2a79f202efa8b5ebb6d1858d5c7742c245c1725f82441a2e0a4e5202a7b29e3f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp2_T0/run.json
927c8d1a9869e1919cb0a8a9581fbf16ef44b5537adddb3635c9d4522fff02d7  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamp2_T0/spectrum.csv
0ef4198da9279bb6c311bd3042b6623571490c5adb2730c1634cd304d8872a39  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0/profiles.csv
b172b4319629f9c726cc55f6e5e0108811904203ec71bd66357ceff56b3a7e74  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0/run.json
4e5f4b00fb281b1a16c1202b6c2ef410776ce01c38153ad39fb960e4aed41a76  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0/spectrum.csv
f2e955307fd41d2f59d72e058fd2a72567f0bd47eb3a7cc9577450beca8587f4  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p1/profiles.csv
b79797d9a6f7dec19e8368a5ee329c45aaed71835ecde04f5670490ecec9e43f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p1/run.json
27617f025e9645ed97d317e6f01b33bc6a9ad042b56c37c385b695d422418acd  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p1/spectrum.csv
39c4fea830eb8f0747171ff54794263dcd7340a4f5df9723f88b00678e221e28  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p3/profiles.csv
f544ef26d50132fb41fd1a3635940df8476acb4b6f4e906a5ce5677a30600f2f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p3/run.json
26f349f8c063d465159c1f569d2d1593473d1ef335c6f40499a2900bdaa2be80  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T0p3/spectrum.csv
68b168d8d45f761edb3456e8e97baf9ae9c792bfe4c410881920d27383db91cc  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T1/profiles.csv
5a316bff8a439e324411b10f9edbd0d6e044f16ff67b02fbbd52810cb44372ce  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T1/run.json
5bbd023bd06153f8e70c762e0b984a4f2ab8bf644a5cfe3f8d7710eca427ef8a  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lam0_T1/spectrum.csv
6813b373df1a9a86e6b139790ac515a75e0ed7598d1a959bd7b393f9ddb0b9c9  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0/profiles.csv
0594c48399967e1a2de7604041f33b75162e43a37b30e331422496f1fc104400  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0/run.json
f49f7a778b447bb97bab5518504b58cf4c3fb98c79b9a526250cc3cf87d6166d  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0/spectrum.csv
9a82d89ce791beef02d3d60f39f9c0036f98f058caf6f587ba851109f093aba4  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p1/profiles.csv
732c2cb51b02ba3081c6e15848d1abf6dcbd0f92ae762912534c38f4df501b57  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p1/run.json
40fe62874d0841ecade4f322044ab77845a107f2b9ed00f6cf15ea40d8ac1035  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p1/spectrum.csv
a4157b1e40265acb94e2f7f19eb82345bb56d1d0c4fbb4fff43f1ca7e55a39c6  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p3/profiles.csv
67654da548c88c370fb508b0cac42f1a8abf9b04c18ba7e21231121c6ffc773b  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p3/run.json
e9661785abdb7aeb5475b008d94d9fd60afaac06ce0671de1f76b91bdc62e43d  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T0p3/spectrum.csv
cc4deaec4a0d43f1bcf03b246a486c4a5b4259d62a9fe5aea066a91ec262acb8  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T1/profiles.csv
39b9902cc50761e3727a1530ebbfb945cc47563322fc32893c64002c0a713a7f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T1/run.json
1a23eda26cab41bb5e151b5040443dc681da4bbf0c1c82169ebd81008a244860  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamh_T1/spectrum.csv
f65899fce0d2300727af77702e206c4e0dd5ce160c1bd4a9f1cf7bb40b71b21f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm1_T0/profiles.csv
77c3d9d2fa1f05db5e96951611050b5b5854bfbd7d2628a59379e365f7e5b8ca  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm1_T0/run.json
30a3d56113667b0145f631dd823b69049c0b7615118d775d3f4ceb5253ca16c6  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm1_T0/spectrum.csv
42b98ecec6ee75231d96ccc40a70d04546ec26a9c530e1c3cd0d2ea8674918ca  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm2_T0/profiles.csv
965a117c8c904fb95e5ac7f066a1b4bf39ba847e4d9a0bf350a6d1b3c2c03d16  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm2_T0/run.json
c806b3a2ffe89be33222908249a34d557aa93aac28758e50dc7c994db6f72173  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamm2_T0/spectrum.csv
727801fffcb437ce2dea62f113cb9152169cae6c7816f40268bac2004edfb4bd  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0/profiles.csv
d0840c979c9fb3671dc70c93e91ef8986db9c5bc20d0d62e45e3d46cea2bfcd4  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0/run.json
0e3c60ffef6af2500a6a7544b19424eaa0cb3ab5b2afd4a789d25462b42df3e9  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0/spectrum.csv
a9840f723e59191a81eb73efcdc15e8385fa4faeab00505a6f8f168e5aca225e  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0_a40p5/profiles.csv
ec642fa1a8fdb7dd675e34b269b28732d33e64d23dcf3c39976a07e0f6bc3549  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0_a40p5/run.json
17f82afc1dd43ae51da207649881d0df4ae45643132b6cbd07ac456fec9dbc70  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0_a40p5/spectrum.csv
230278e21a374746d764233ec84a6963fbf52b812d4d940058deadadee5b16ec  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p1/profiles.csv
40c05314e4d766c4796e6b34fede93d5ec0625b6c91db739c300d9a7670939cd  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p1/run.json
3767f12b4d70692bbd1842d5f04ad76634573763f25801fabd6683b7959f3c04  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p1/spectrum.csv
face038cd3f32f1e41c4ee3f129b82372237de3548f343536c615e6c3ac1b729  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p3/profiles.csv
c997b4e9f92c31eda070cd2ee8274ab3f5ba7e00f2e81b29dc17d80589d6734f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p3/run.json
25a76a51f164715181025b00d7815b8e9d41b90017a65fb71428e7be27ee68ba  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1_T0p3/spectrum.csv
84d4e0e8d39826dbda68533c86dcc745850fcb373aaf05d321add583b90feaf3  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/profiles.csv
c0e6bfc4a8fe5f081b02272a1dfd089add4f4b48d4ccbea932fab3984d0d6b37  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/run.json
ba5f9b972de15ecbea568a260012ec1555ec9e2a7f5055fbc0fc8a17e09c2ea1  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/spectrum.csv
250ca27e57c984fcae9a6ef1de992b0877165325685c9ae2b1453f454d966247  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp2_T0/profiles.csv
0ac94ada9e0a43045e6326bd971fad22276213007ef6db148e4f99689e088163  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp2_T0/run.json
6bed119fbe66904f60c8a94f28c1be3539b2964821d8b757f8bf07c66b7a4f21  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N112_lamp2_T0/spectrum.csv
5d3e2f2cd2cd716241ecd8de7746b62843f0df02f92d85fc9817557dc7a7f23b  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N896_lamp1_T0_dk0p125/profiles.csv
06742924897db1967eeaf83bae9d8459b4deb1635d0aac3bf03c575c58e94169  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N896_lamp1_T0_dk0p125/run.json
92a4f876cadcf18e6ddce0d611de13e3f08b176734f4d60614e8728f4049c9f9  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N896_lamp1_T0_dk0p125/spectrum.csv
40cc4fd221af4ed8d2c63f77d317d28436ec7c0e68b0aba458d9428a5de812fe  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0/profiles.csv
5c9ad935ca2f5192555d2f72fea9a1aff4bd49d3b492da60f823902c48b58b80  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0/run.json
798e750d9049b576605db93006d829acac56fd1e975fee524b38414f6f30bf37  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0/spectrum.csv
5bc65fb31c81d3dc5cdeea50de196af03a0d4b41ba5b5eb483fb3aee12f4bce7  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p1/profiles.csv
5015725561461db7b86801853031943192a8f65c2bfa16a9223af5fb8cdacf03  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p1/run.json
cfd28ad0ae48db628b0210019b02bca6d64e8a25fdc3f06bd8d224b1a17a4a59  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p1/spectrum.csv
328523b5e0771c55a57609939fc167311b02f9fb659cb7e26192e93b520212f2  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p3/profiles.csv
10152e291b7f1f3849bcb9ebe0398d8b7d62cac93111194f90ef00e689b46b21  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p3/run.json
93da7e10885ca145d1383a1a9405442554acddfdb11dcb5951a0d2f715bb94c5  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T0p3/spectrum.csv
c981dde2965acae8aa946531b38693abf9290146677aa32778b33eaa2e4e1bcb  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T1/profiles.csv
0a99f04c4ec672ab2f40b93718710975c1fbfa2b2352f7022831e40d6311b660  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T1/run.json
e5568a20286664613f6b93daac54d4a5a4170695af8012e062738b3a10464cc7  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lam0_T1/spectrum.csv
bb45302d06de35840254a5fb7a059a5735ace381ea15ce4a851e3ee3a033bb00  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0/profiles.csv
af36ca61146f6c8ef1a82b78dd7ad33f9d0a0cd48146a808845b64b5ddee09d1  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0/run.json
8f7fd1897a286364aaeb761d5eaa663c90ec5c9e630bafd034df4f4b2eb97289  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0/spectrum.csv
4e21b4da358b38b47445f2d7150f49f6ce8620c096e155f92d20be70832e139d  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p1/profiles.csv
bda36c713f97a8c26b7184358cf544d1c3f211a1c7668d115b9c1fe6a3e73008  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p1/run.json
74580ab854ef413018341f5ca4cfc32559b554536dedf8e4110732207ec5bc2b  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p1/spectrum.csv
dd627dfeebf1616cad53503185f1d999be31129c5f7e42d2a992f2afc0a0c7a2  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p3/profiles.csv
169a9dbc5cadc794c22c1cafa75152d5f5340d5729cd30b2d9281a46c0e01542  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p3/run.json
b0833795295ae958d51286674393ab20c08f6eb1af17752dec96ac440a7a7afd  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T0p3/spectrum.csv
e9a9209b17801188c192f45feb0715078ae7c72a270eb6b9e5f975be2a12cb11  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T1/profiles.csv
aa94a82d5d6e13bf261f0d4646d39ca3478df953bdc10de0964f2871b13ef9c7  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T1/run.json
0f1e95905f28c2729d65c67e8c0b3f6fec77bb7e8e845a7b707cbdbbdac2e111  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamh_T1/spectrum.csv
4cf810bb0994473212836e4d3f5dc8a8b33cd537e65c7ec151b2e3d7b9b568c8  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm1_T0/profiles.csv
7534524654799f24d04cc1eb7d3c059152572e2e1602235e2b469ba186f1b28e  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm1_T0/run.json
f03485a40b3373c9baac190da2a1ce5364e65a5dde0a37abfd6d11f548742a4e  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm1_T0/spectrum.csv
47d4f6826cbca31a8b95b1ed6c499c6d2a76edf0f19b8d9abb4de79a61beac90  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm2_T0/profiles.csv
b391b5089f2c356eca80e6ccfe9b5767ed40d4b71b750d97c0059eb24bfacb43  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm2_T0/run.json
6c9aa7a9ead48f38a29bd798f152984efef1cc4ff10050ae060e87b826011595  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamm2_T0/spectrum.csv
86d58c119cc5fafd2cce1af675c911b1b886bcb0cbac1de2d45cae2472b8c71f  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0/profiles.csv
2fa3490bb0ec1e65632fd40aa8581dab15c5de4da7a6fe9e593f23ddc8ab202b  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0/run.json
814b5b05dcf5ff4aa5941eed5ccbe317ae9c65c419a163cec59cd3b65781ed91  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0/spectrum.csv
1b70f2b9ab28ebc4ee42ed535538c8a134e008e19c5344dac535aeba4cffaf70  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p1/profiles.csv
916522ce2868c6f1ba092e4c2c623398d36e949cfc534718ea54449e4be84ab4  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p1/run.json
823f90e843082408099c524196025ecfcb3c6fa13732922edfa6c845d25ccb02  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p1/spectrum.csv
b26444f0def14c01a8c275ec09188c3185c6cbfc6a6abb9611466f1462564832  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p3/profiles.csv
9720fdf513e15dc118e96049bbc3fc54b29d9cb3bf41e41e4a0215b45bd4bcad  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p3/run.json
ad1c9572c9e5e4ac88a702b55f7b7f68314d6f2da8339642ab44c88d5dee96ce  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp1_T0p3/spectrum.csv
d6640e83a4267ef887c547945102ea5a2f4e9f1f5ef205b4cf055448fc93e854  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp2_T0/profiles.csv
45fd0179d40e54dd345e2680d5cb4deebe853ff1dcb019e3be3d8741673d5d3c  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp2_T0/run.json
fb965e5f598db1d87faeb9f25b1ab4cc1aa0392daef69be39f79649530d925ca  artifacts/dirac16complex/kohn-sham/reference/m1_L3_N8_lamp2_T0/spectrum.csv
356d8dc0aac891cef53f2a3e304e7cd28c00df898cfe693fce0be9fa10368ba7  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lam0_T0/profiles.csv
43097e33f65e5d61d71f0d778dfa59ced1dd772f94638bb0bea3a6133daee999  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lam0_T0/run.json
f74fa863d563b4286aa3c879747cf3313a38b3bef266add2cdf28b6039b36821  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lam0_T0/spectrum.csv
f92357915d799cbed4dc5db8c1fd235260ea29d9636bf4e64f3bc88c1652ae5e  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lamp1_T0/profiles.csv
ed32ef20908a1fc69dd69e75b3d9c8680473d3bae016e6d0940873101b32e151  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lamp1_T0/run.json
74c9bafbd7cf1e5642be0cf9c2538677472f638c34a139183544acf5ff30630e  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N112_lamp1_T0/spectrum.csv
3d846581ea85531d82685613810cb028d72eeab61229083fecab86321eb8668a  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lam0_T0/profiles.csv
bf4fa1105d2899b6325f790889c78f37738514e12b9f6dfdddd7ab529d905c29  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lam0_T0/run.json
9de3a8dbf3992cfd35a50b51db13aad8b571a9fe034e4460392c8b35f3f1890b  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lam0_T0/spectrum.csv
2571fbb99d064d54defbb8ab429df354e5441b32ca82d31c141653f4f32e9b3a  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lamp1_T0/profiles.csv
8824ef079c01682c5f756376170cfb9ebac24adf650ded07c79a013ffa9f9b2e  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lamp1_T0/run.json
7716576eb748cae512299d28ea500540b76ea76919606f901827b84acbb71b7c  artifacts/dirac16complex/kohn-sham/reference/m1_L4_N8_lamp1_T0/spectrum.csv
7c6f80aa24da0f4b54e507a34882a68cbcb168446497b279f3e2f88a0a41e52e  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lam0_T0/profiles.csv
bf0b05b1a8adb155210f32369d642d5b2348d1aeed0551cb5f73707cc81655cb  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lam0_T0/run.json
e9a4d96006eb8391d5dfe53a2be883b13cda4add36ad117a6cfe42a6cc271d3c  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lam0_T0/spectrum.csv
692ebe685e63f081765311c9ff7f3aac99c894acfd7719529a67415158aa759e  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamm1_T0/profiles.csv
16d2550c7ad7a6ccdd6e399697497ba63b71f27c4f2e9da09fdd6317c83023c6  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamm1_T0/run.json
3a1c03a29bbbac62e5516b60bf2376f278e928f0e7e2e5bfae6bb44dec87583e  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamm1_T0/spectrum.csv
92784b5f5efffcfbcb78c5c4e9e66d70a40933cef67102ed85fc858b3351df1d  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamp1_T0/profiles.csv
5ff4e02e39617ab0a9ffae202ce7d34bdf8f6fcc853685f8d53022d114217eb2  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamp1_T0/run.json
d9f5aa36571669cc0cea2011d2dcded2b34f38d61b8cc3efa2e1bb6e25049d57  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N112_lamp1_T0/spectrum.csv
c0bb7698138b1ca0bfd1fb7f6b6e0066e8859ed09b61d45135b4b5fde4697c3a  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lam0_T0/profiles.csv
353a6e36fdfc7bb8c14acfb57a773f9c0650082b35dbdbe72a34edcb9a39204b  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lam0_T0/run.json
78b6fa8ee7c8d6e476827770db1c44f49c777ad570dd33cd07d20a8c2a59f5aa  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lam0_T0/spectrum.csv
b3ded83d6a4a27e7cbe98e01bfc764a15be0f320749fa82ab9cd834082229bd7  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamm1_T0/profiles.csv
e26746a38b32a3b21e9e8dc5467e8efec8408f66cf99703f13501000643f15e0  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamm1_T0/run.json
7108004896fd9df1884f5730586e4ebaabb98307d93f989727ce5db077603aca  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamm1_T0/spectrum.csv
7c63a45c16678200e40c25a9d3ad74a47d5e597392390679f949572217028ae4  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamp1_T0/profiles.csv
51944005b2829cabd2600ed742ee65a4634349d6c8d31cce5eb0ceff49ae2517  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamp1_T0/run.json
6df4843f2739d9e0a0cf8083a832bcb22f6ce73f3636e52c2848bdcb31b34619  artifacts/dirac16complex/kohn-sham/reference/m3_L3_N8_lamp1_T0/spectrum.csv
54d67b59bc06b599c37f1744b44de9a8d670f48addcae5230ee4d36917097ecf  artifacts/dirac16complex/kohn-sham/reference/reference-summary.json
3c65bc93ab53c13073e9bb07f8bc66c9b5327b170a2c14e2e67ee77cd9aa023c  artifacts/dirac16complex/kohn-sham/rust/determinism-report.json
92c0ba84b588251a2c30285afd2cd3036899418a7351b0e371a098378c91a069  artifacts/dirac16complex/kohn-sham/rust/emt/emt-summary.csv
32d0766bd395e928c9c18ea63b64cd28aba90f4380fb9429a230ba01b9feac82  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lam0_T0/levels.csv
7d73423981bf9f172483498bcd0300f93f4964fb32e10c70d4d28ac2db4c623e  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lam0_T0/profiles.csv
f9f72c7ef62c0bbf50c7bb29bbdee1c60f90cb3bc19e04f5ee90170d0a7f5784  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lam0_T0/run.json
c7747963a0d3b0dd7b605274eb391b2b8882de0ee2f4211a0af84866ee35d74d  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamm1_T0/levels.csv
4afa99fdab2fc42229339d23fd2d2569140801ad0c24783862ff0133ccc494de  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamm1_T0/profiles.csv
2a8858b2394ce3267b988e65f86336fddbdd14b0bd09d02f2d45e3819189372c  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamm1_T0/run.json
2f1a2b2b9a4321924f38838ad84cf1b641e3db86ea917a4267088dbf0c8f1da6  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamp1_T0/levels.csv
60b508ba1cc856653389aca18b13ad31ec32063f6da21fecde89f8cc24f93a9a  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamp1_T0/profiles.csv
abcaba3c63b72d417f2a4a254ce0d0cd85fda0cb78feeef9db12e6a1ab74ab78  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N1016_lamp1_T0/run.json
70c5e3059ccb2f87c423ca4e0b215e67fe3d049c382c072fec3fa5114d499e16  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lam0_T0/levels.csv
87ffc9ef64fcb83dcde7063a8d36daeb360df0d4a484bd80195f4f0eeff6c922  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lam0_T0/profiles.csv
14d2d3b9155f8c78fd1208d516f7b64fb931b6daca8b2f741721fcb34cdfaf74  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lam0_T0/run.json
95780faca8e4a70313a26d4242f0b1bda8da569269b8971d16db89e841669693  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamm1_T0/levels.csv
b76455f2e5c22b3e67d303541c3a9f806063f60e6a087b37f3e3f59330f7b8fe  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamm1_T0/profiles.csv
931d827437b98f5fc74e3e06927aa760ddbfd224fc320d062839717907eeb2e0  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamm1_T0/run.json
06afe1ff14ffca71bc100343ee132bd028e71d3973f832320175d3670559ada5  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0/levels.csv
b4550e9fd93a48d7febf7fb310737d81ba64829432c57d33f609e023485db3b2  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0/profiles.csv
68a5940873aec1f956c4b5d0acd632f43ffb10f7e9d83140762f46cb12e514f2  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0/run.json
2dce00bbca278a63a57c64c22107e2cf297e5bca5a4c53c0701644b32320d3a1  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0p3/levels.csv
62002001c6787e77f5371660e8f418b7f097506d8d226bae203873d0b238bd02  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0p3/profiles.csv
3216d2da1c2adcc9ec4059bf121699a84a516a6db5050a64773add310470b82d  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N112_lamp1_T0p3/run.json
dac6f7c7b1f71d43c0f5773ab892edc071e232e7e96282cb8ea91055fe450270  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lam0_T0/levels.csv
63ec99ff595ed63f40d72504f37782c1b55d27a0f6e93933d7ca3050724cc679  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lam0_T0/profiles.csv
9e15994b199bf134b14be57201f2649af8247cf7ec4f66b60932ba879bc95bdf  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lam0_T0/run.json
e0a2ecf41b70a99d3148fdbf667bdb118ed89d46ef5e955073db52d5775a8631  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamm1_T0/levels.csv
88932ec13ae7b2ecd0d79a0697bd76cd77681b3f6e8f50e7e114da92b3bc66a7  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamm1_T0/profiles.csv
45b8f1ff1da30a79f3c6e01c4c63b090145436bd79641c3bc4e07b5c50424aca  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamm1_T0/run.json
5bd0f63c558bf59fd257ff1fed51fa5ee572a4ad31e31bd7500d60804b024419  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamp1_T0/levels.csv
7dcf60ffa8386925d83bccefcb447b67c3df0d3959ff54f74bc911e69b7832e1  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamp1_T0/profiles.csv
64624e2efa7b46f11ce37237e8b438faeb6c0d78820276b258a601ee887daac0  artifacts/dirac16complex/kohn-sham/rust/emt/m1_L3_N8_lamp1_T0/run.json
d93d3d0879aa2f35685c610ca9c88fb77f1ac8600b9df3dd78a01573054ba6f7  artifacts/dirac16complex/kohn-sham/rust/emt/summary.json
6bb61f8b77d09dd37312d035e5ae7f89acb2552549a6fdefc6070f653e992d2a  artifacts/dirac16complex/kohn-sham/rust/excited/excitations.csv
7774c32c7f8c1efd3465d67ab9c6fcf128ebe4aaa9e305d11bdd86ef5a377dda  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lam0_T0/levels-excited.csv
32d0766bd395e928c9c18ea63b64cd28aba90f4380fb9429a230ba01b9feac82  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lam0_T0/levels.csv
9519da300e058b7b2b2bdc1823295768e2ceb91edfecf0ab4fdc3da5c49599b3  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lam0_T0/particle-hole.csv
b2706172acc04892189e1257ed67ce8ecc13d7546b2098a8640e82c3081e5b28  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm1_T0/levels-excited.csv
c7747963a0d3b0dd7b605274eb391b2b8882de0ee2f4211a0af84866ee35d74d  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm1_T0/levels.csv
9fc7446c114034924f4902839185459ec9b3ebb6c5f584162f5aa6c306124b9c  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm1_T0/particle-hole.csv
74523ea3fbcbc531b7089d8fd69f53d58aba703c3b8101a65989d4789c25d619  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0/levels-excited.csv
7f69aa251cb7a56d1a9c9ab86207c41b06b0b15011cefd7b31054be4d138a83c  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0/levels.csv
db3e6c7364bab119b581f150e2d76a20ce82261dcd299d213b6c8dcc197b6b93  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0/particle-hole.csv
44572067c4a1e54e8daf72c923b44d37a56320ca5d311ad6a098f457bac0587e  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0_g601/levels-excited.csv
2bf695e85a234890a8110ea44c77a2d1f4a0b4f4ee2b40daa37a078365906140  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0_g601/levels.csv
80d24702ff92b2666c27223aba2e0474a7d610b48dc5ce671afe00d1e0c2d9a6  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamm2_T0_g601/particle-hole.csv
0719a2b1eaff82047baefe7af8c516f696e29944160c09d93c7c428eb106eb26  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp1_T0/levels-excited.csv
2f1a2b2b9a4321924f38838ad84cf1b641e3db86ea917a4267088dbf0c8f1da6  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp1_T0/levels.csv
8d81927e4189074b22c756f433027eff9db580b710ccd7e4fb028388e5b239c4  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp1_T0/particle-hole.csv
8003ea798e76c48c51861d0c5e5ca8b828cc1545f58257af6faf30ce648301ae  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp2_T0/levels-excited.csv
fb5412fc2416299d613f9f5c3553bf953b05e8b896535c3b66f8cbe72ecf05e4  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp2_T0/levels.csv
f551c6aed4136341df24c0a672866bdf2834407e6afe7cea6dfaae6e111b16fc  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N1016_lamp2_T0/particle-hole.csv
b892bd021022b9d13169fa6fd0ce95317fc91c4a9302568aaff108f762b3d4c9  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lam0_T0/levels-excited.csv
70c5e3059ccb2f87c423ca4e0b215e67fe3d049c382c072fec3fa5114d499e16  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lam0_T0/levels.csv
26fc024665fe3ee75a7d8d8881faf53b503e85eb166a8c4d22568372b4f8aef0  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lam0_T0/particle-hole.csv
dd76fdfb109dbd1972588e153117d0cc424eb276f0cc5050d36db796818d87f5  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm1_T0/levels-excited.csv
95780faca8e4a70313a26d4242f0b1bda8da569269b8971d16db89e841669693  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm1_T0/levels.csv
be299ea20c4c65388c3084470c0d9ef74850020dffb0bd5ae1f57317b7aa79f7  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm1_T0/particle-hole.csv
2863f86f211f2a0f53138c6bdfd224cc1b72d66abe0531f71518c48d5f682f80  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm2_T0/levels-excited.csv
104caf4b75a66f902b52cce01249dad4ba3eb2221d4e77ec96276739bdd606a3  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm2_T0/levels.csv
8f17b22639b62262fb76ed50e176f0614d9477de58add8c5a791001882b96db4  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamm2_T0/particle-hole.csv
3f4a9e0d3577328cbdd04ebdefbf678e063bef6dd3ad91574a5e6d303d9fc608  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp1_T0/levels-excited.csv
06afe1ff14ffca71bc100343ee132bd028e71d3973f832320175d3670559ada5  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp1_T0/levels.csv
619f1e87a168a1b022fec50ff0bdd7f32ac74c620f2fa810a726e64d6ebce05d  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp1_T0/particle-hole.csv
72ffafbd1b4e75559800a6b8d4340139238c5d17447e4735a972cc876e676934  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp2_T0/levels-excited.csv
cee99ec3720855cd68d3c21fa92611d91b1450226c721f82079fa49f6e8404bd  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp2_T0/levels.csv
e479e6ead05980749aaa2edd69e641c35821010fcfa0d963044e972a0579e4fe  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N112_lamp2_T0/particle-hole.csv
92f696a42af2832cdd7bda8f04c11dac83dc9e5096756539c2c4d4247871e344  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lam0_T0/levels-excited.csv
dac6f7c7b1f71d43c0f5773ab892edc071e232e7e96282cb8ea91055fe450270  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lam0_T0/levels.csv
bf5ead136d218b309749a30db62c4eba0aa42278f041fea59e96c5e21aa2d947  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lam0_T0/particle-hole.csv
4a39c1a9149e44f062841bdabb071f7bfdb71f67a1fe34fc1e7c7b927549250f  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm1_T0/levels-excited.csv
e0a2ecf41b70a99d3148fdbf667bdb118ed89d46ef5e955073db52d5775a8631  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm1_T0/levels.csv
47cf4bd338a58e8725ebf90f8f9e40c2dc7bb80f28d78c3419f93f5ce3b00164  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm1_T0/particle-hole.csv
72e8cab627918388bf3c4fb859c59c65c6c6b0ba80e8a53a7ee0fcb07fe3a07f  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm2_T0/levels-excited.csv
128d992a96b8831b1b0a582cc4c747252571ad44b3093b9ac7817392d3d2162d  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm2_T0/levels.csv
bdca7e1a39e7ba33c5a55ac74d4319ab7bf4d8c388cac73ebe8eeff21fffa237  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamm2_T0/particle-hole.csv
9b8dbac81383cfbf2ddfcb06feb253d88f655bb2ade7b5ade9071b042ad26b89  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp1_T0/levels-excited.csv
5bd0f63c558bf59fd257ff1fed51fa5ee572a4ad31e31bd7500d60804b024419  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp1_T0/levels.csv
397e218ceff39c7cfe6ab42d5d802b479a6800c304b6b978dd56d1c1b84dc886  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp1_T0/particle-hole.csv
843336694bdc89222814098ba1dc9aa0c115021a0308ddff33f545ddd90d5f51  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp2_T0/levels-excited.csv
a4a38b702c1873d3fc725cca91c0bdf28c4616be104739ccbe87b2b6545a1329  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp2_T0/levels.csv
7e54f01ca3d54a31182ca6d81f02f52a707a4bef8bbcf01bf5354d1eb537b816  artifacts/dirac16complex/kohn-sham/rust/excited/m1_L3_N8_lamp2_T0/particle-hole.csv
99394347e61fd4b57f8bb38c60f542df9a46ab5151771ba443422c9f0d270a88  artifacts/dirac16complex/kohn-sham/rust/excited/summary.json
57a4286e8a3a22e36e254dcb8de40c320cf5c72ad53b5f25158eff3dd9262ab7  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lam0_T0/history.csv
1a88a068036c240d8d8c0dc662e6846d1dae6e14848d2b0555d7e8d755dfbfbf  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lam0_T0/levels.csv
912c18e847d1d3dce816f4ba173b0d20586a71404048c87b1748d15a1002a7b5  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lam0_T0/profiles.csv
6ddf4dc0678baf8851d40b5b67e4d15422b2d668be3f796ada26e0f98d3e9cd8  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lam0_T0/run.json
b4fc1aa2572588232b3d7e630815ed2209ff28e4fbe90af464fe1035f2b2dd24  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lamp1_T0/history.csv
0cdb7f430f750c1a85bcad0c3776281c996a781ebe2a9ad1ffb481b5426a9fa6  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lamp1_T0/levels.csv
b4d0b7815b5b4c2e8e1ac15f67d6ecc89be130b968bbeebce33e7e201403a9e4  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lamp1_T0/profiles.csv
b32675500262d3414131358b7107e90057edd815ff51d38865dd70693a341406  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N112_lamp1_T0/run.json
7d9ced37a9c50d9881c98ef9c74b1c5f05ebaa59d13c0366944e3d56222d609d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lam0_T0/history.csv
b6e1691bc8e0f21f3a871a7c2ff520a2ac1bbde53d33318f1642104db00f96fb  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lam0_T0/levels.csv
da8ca0ad7f3225082db2a084e98c8dfa254f1f6c4ed6d98517490e29bafc477d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lam0_T0/profiles.csv
47106eb0c541615dbc9247f83821bb2753eb87c0b5afc94f7868390cf7d7f085  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lam0_T0/run.json
2b06b154ae98c268a63ac2cb94f000b5707b017fc7705b4f525fe11502be373b  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lamp1_T0/history.csv
97778b5dd05c2ca89cbd81a64c29d299c8a18381f4eec038e310fcd53d46458b  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lamp1_T0/levels.csv
7dbbb81b722e2cc018cd6d743949f4e2780c0a480c06e0d12627d8e8d398527f  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lamp1_T0/profiles.csv
eba140042b8a696731e979aa4fb1cc7428834b25caa0dc5b5db134434aca40a3  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L2_N8_lamp1_T0/run.json
0665560410d173979c0044df149440ce82bc5cbfca67efb2f5da5bafbdbed501  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lam0_T0/history.csv
32d0766bd395e928c9c18ea63b64cd28aba90f4380fb9429a230ba01b9feac82  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lam0_T0/levels.csv
7d73423981bf9f172483498bcd0300f93f4964fb32e10c70d4d28ac2db4c623e  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lam0_T0/profiles.csv
f9f72c7ef62c0bbf50c7bb29bbdee1c60f90cb3bc19e04f5ee90170d0a7f5784  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lam0_T0/run.json
d76ead231d776377774abead7f101ebd0e57c5faaa122d66125955f1c8714523  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm1_T0/history.csv
c7747963a0d3b0dd7b605274eb391b2b8882de0ee2f4211a0af84866ee35d74d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm1_T0/levels.csv
4afa99fdab2fc42229339d23fd2d2569140801ad0c24783862ff0133ccc494de  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm1_T0/profiles.csv
2a8858b2394ce3267b988e65f86336fddbdd14b0bd09d02f2d45e3819189372c  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm1_T0/run.json
332db5d28c514138f0131e40726e4470368339699cc0c204b953658f3167b2d0  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm2_T0/history.csv
7f69aa251cb7a56d1a9c9ab86207c41b06b0b15011cefd7b31054be4d138a83c  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm2_T0/levels.csv
488dc3875d65d2204ee657e190d4ed09a3c9fed4f591b569ecf200b07881534e  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm2_T0/profiles.csv
85b549ceb7f3af7052118318ab2191407739c3ada8b9b0deffa1ac25ecf23484  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamm2_T0/run.json
8e2c01e6d73279c14ba2619d2be9643a6f4e6fc3abc8680846853f7b1a697368  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp1_T0/history.csv
2f1a2b2b9a4321924f38838ad84cf1b641e3db86ea917a4267088dbf0c8f1da6  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp1_T0/levels.csv
60b508ba1cc856653389aca18b13ad31ec32063f6da21fecde89f8cc24f93a9a  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp1_T0/profiles.csv
abcaba3c63b72d417f2a4a254ce0d0cd85fda0cb78feeef9db12e6a1ab74ab78  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp1_T0/run.json
8e6acc8f2476e4d7e6a94424fc4a90dfd48af1b99b968e2f486e2de14deac4fb  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp2_T0/history.csv
fb5412fc2416299d613f9f5c3553bf953b05e8b896535c3b66f8cbe72ecf05e4  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp2_T0/levels.csv
ac3d1132831a39a7c7e38e39e002f4a2f287b3d9ddbad1d33abd7058375c43af  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp2_T0/profiles.csv
1eded3454990a8420a71f726285bc1649050a65ec89b5450de43d5ef9a487762  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N1016_lamp2_T0/run.json
681d4d2ea8ff6dfdc6dd5b856ed5952fa3e8e8aed840b7f4b98641c57b91cae9  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lam0_T0/history.csv
70c5e3059ccb2f87c423ca4e0b215e67fe3d049c382c072fec3fa5114d499e16  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lam0_T0/levels.csv
87ffc9ef64fcb83dcde7063a8d36daeb360df0d4a484bd80195f4f0eeff6c922  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lam0_T0/profiles.csv
14d2d3b9155f8c78fd1208d516f7b64fb931b6daca8b2f741721fcb34cdfaf74  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lam0_T0/run.json
62ee3e70eca93ebf46fcfcb79c42e1e5250f5976e743c69c9c43ab2b1fd94f83  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm1_T0/history.csv
95780faca8e4a70313a26d4242f0b1bda8da569269b8971d16db89e841669693  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm1_T0/levels.csv
b76455f2e5c22b3e67d303541c3a9f806063f60e6a087b37f3e3f59330f7b8fe  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm1_T0/profiles.csv
931d827437b98f5fc74e3e06927aa760ddbfd224fc320d062839717907eeb2e0  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm1_T0/run.json
fe4da8f667b6e4ca4b8130a38477d34ab15d8fc99b7614d423958c905bc298b9  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm2_T0/history.csv
104caf4b75a66f902b52cce01249dad4ba3eb2221d4e77ec96276739bdd606a3  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm2_T0/levels.csv
9c9638b51beb4ac1150988efc8b572b2cd82d401295488064214108a4007fc66  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm2_T0/profiles.csv
a97644cc9257546811aa8af6243b208804371bb5d8a58bdf632766eb4f86df8b  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamm2_T0/run.json
72fcd935d7a3237a6726c555c4ade2bb38f638b69797dfa59f4b70616ebbcf57  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0/history.csv
06afe1ff14ffca71bc100343ee132bd028e71d3973f832320175d3670559ada5  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0/levels.csv
b4550e9fd93a48d7febf7fb310737d81ba64829432c57d33f609e023485db3b2  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0/profiles.csv
68a5940873aec1f956c4b5d0acd632f43ffb10f7e9d83140762f46cb12e514f2  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0/run.json
5b09e8ba6f3198c7c8fd131f2f5f128a64a5faf342fc9d88417553e5c30afe6d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_a40p5/history.csv
87db849009d1abf7034123f2207454fb3c908c129cb141cc5a15054b36aba350  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_a40p5/levels.csv
7bb55435d6c6e732903cfbf1d756d7ce584dd3792bcad4165c59169ac0869066  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_a40p5/profiles.csv
0c65b9378a6e492d97a54c9618bf8198f44b6dcb1b93799f3f3b90544940138a  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_a40p5/run.json
f241fac38e3748bd6d14a112a47b72faf2b56dbfd1609e19c10f904437941a85  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_g601/history.csv
a81dd905527268e18fb24ba073755a92c58d049b5e8bae998152d1a3cbff145f  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_g601/levels.csv
18d328e56dcba3fb6716b72b712db0e6a1c3259d3b638d4d72769309d18920ab  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_g601/profiles.csv
f30b4c6f8b372bf79cabd007a30bf2e403a4ef720cd1376d8b1e081a4a77ab1e  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1_T0_g601/run.json
f9085d97126a75081440adc054111a98a218b41b44734b23c054c8462f2c2b40  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/history.csv
34adf6eed97a26970bb0ed1fe59fc055d16b99d04e4f52647de118c6a7785e3f  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/levels.csv
f26cbbde2a0eb5f9f5f0507af3b79d59b4cdbd2ee5b38aecfb216d28f848bdc7  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/profiles.csv
cd60e7f0daf1a372c3291ea3a71905361bd0186268c2e77d2e6765afb4e1b258  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836/run.json
d5bd2d706a41a1aadf3d0a6a9ba1435334cd6e21da5fbf841ea15bd3ecc7df4e  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp2_T0/history.csv
cee99ec3720855cd68d3c21fa92611d91b1450226c721f82079fa49f6e8404bd  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp2_T0/levels.csv
603b8cbd797772cda8563c136dba7811a4da7dbe7671978f895596182d0eabba  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp2_T0/profiles.csv
2acbd071a51a144319ac9d579bd9cf2cd6a2ea5780ff8f86a868a046bbf24860  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N112_lamp2_T0/run.json
f1617efce19be73b9a4acb0466b7dbf187a82b882a17ffbde5ee5f2a56906ea2  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N896_lamp1_T0_dk0p125/history.csv
629ca314ff8edb3a8c30f2fef1cc8b62142242423e3ec94af7a89ff060f3e9d1  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N896_lamp1_T0_dk0p125/levels.csv
39e4e6067e0d293e84e49e2b026bd43c24556d687f0a80d635be51a19b522850  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N896_lamp1_T0_dk0p125/profiles.csv
d515db63c97bb42cb942f7d833b2394cbdf6a922ed81742a3c633e139aeeb27f  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N896_lamp1_T0_dk0p125/run.json
3e8fff9d1540ae06671f98d29aa964be2acb2e72643b0391ace5e88d2c09b679  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lam0_T0/history.csv
dac6f7c7b1f71d43c0f5773ab892edc071e232e7e96282cb8ea91055fe450270  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lam0_T0/levels.csv
63ec99ff595ed63f40d72504f37782c1b55d27a0f6e93933d7ca3050724cc679  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lam0_T0/profiles.csv
9e15994b199bf134b14be57201f2649af8247cf7ec4f66b60932ba879bc95bdf  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lam0_T0/run.json
23417c19b7c439aaf00b013fbe28c43e096d16a86eb346d837f34109ec783106  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm1_T0/history.csv
e0a2ecf41b70a99d3148fdbf667bdb118ed89d46ef5e955073db52d5775a8631  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm1_T0/levels.csv
88932ec13ae7b2ecd0d79a0697bd76cd77681b3f6e8f50e7e114da92b3bc66a7  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm1_T0/profiles.csv
45b8f1ff1da30a79f3c6e01c4c63b090145436bd79641c3bc4e07b5c50424aca  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm1_T0/run.json
14ac345bf059c9f7bb6d74866a64165f138b053492493c5ca10504ffe5df36e6  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm2_T0/history.csv
128d992a96b8831b1b0a582cc4c747252571ad44b3093b9ac7817392d3d2162d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm2_T0/levels.csv
87698c7ddd2c00024a21913380e6b3c0be411992825b45f7a4469b836f061a77  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm2_T0/profiles.csv
102cb1f892e62885d8eb806317fa49559a98f2c4ffae46c5f4afce6a5965c037  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamm2_T0/run.json
5cf1983816a559533d3c3b0a08bd2c12dd38360ed511bd04d14efa04a83603c0  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp1_T0/history.csv
5bd0f63c558bf59fd257ff1fed51fa5ee572a4ad31e31bd7500d60804b024419  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp1_T0/levels.csv
7dcf60ffa8386925d83bccefcb447b67c3df0d3959ff54f74bc911e69b7832e1  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp1_T0/profiles.csv
64624e2efa7b46f11ce37237e8b438faeb6c0d78820276b258a601ee887daac0  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp1_T0/run.json
e194b9db46810883a23cb1e9509ae6e1388ba47d664313ce7266e6737cbc47f9  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/history.csv
a4a38b702c1873d3fc725cca91c0bdf28c4616be104739ccbe87b2b6545a1329  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/levels.csv
f9c8aa72c4a4c842795562d22c274c7fbfd038624ec4958ccf806655e76db0d0  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/profiles.csv
7b2155d8e8a9e9eb3551819072b1bb4fe1fcf4efb8463cb01a1b6e514536fcb4  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L3_N8_lamp2_T0/run.json
ef2b9b73587a23e4fd462c0cb0a284f992255f8a06f476903fa76457744bca89  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lam0_T0/history.csv
590748ba6dd5e42194afa4684c6d015d8bf47418e015f6692cc413ca9cfa888c  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lam0_T0/levels.csv
0d2f1f9bc6a6838ee70b071f01fd650b413a249e496bad733d4b51049a97b353  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lam0_T0/profiles.csv
20959886834add90e6a7d9ceff072a18e0c481ca4cec2ec747395430f5ed088d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lam0_T0/run.json
709d9529cf48423ce54da5154403c47e7f7e690d66d79e33cfeefe877db89163  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lamp1_T0/history.csv
dc51c511940f1ec8ada7c305fd0e25095458931561762dd12735861cc5108017  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lamp1_T0/levels.csv
2da5c71a7209c9ab481d98b7a84d5f2f70eec1ce18492fd2cc5a9f0259f38d50  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lamp1_T0/profiles.csv
7ef948eb6502008ddae257a67354d0089458f542842524373397bc1acbfeb820  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N112_lamp1_T0/run.json
89522350adf9013d5ec470c98f17568f959a8929531ad40e8fed9b6d23e5953d  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lam0_T0/history.csv
947905d3c517fd0fee0331d5494baa7dddca236a57dfed0e33f9360a43a2b7e7  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lam0_T0/levels.csv
a4840e45cca1b15bb1e50744cf1403470593b16e6d8b8f6107f427e0de074112  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lam0_T0/profiles.csv
a51f9b18524c49a60baa2906cf909bc4e026fe5e81be39985b34a6ba4a9837b3  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lam0_T0/run.json
61c9bd36094a310e92651853f34239d1c977f2ed606a8dd31200bbad5ada7b29  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lamp1_T0/history.csv
0096f0b322d279a180fbed02d0ebc0c769849e36811a016904ebadac1c32e94e  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lamp1_T0/levels.csv
e203c68397b37f44c3dc933e1e09222597a014880bf7f64284e681577ea7da72  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lamp1_T0/profiles.csv
809da901e122fb19fa6277e9666b613318a19d16b3b47c90b69cdbd1607578c1  artifacts/dirac16complex/kohn-sham/rust/scf/m1_L4_N8_lamp1_T0/run.json
901d3cffab75bdb9e3e2940a441618e3031a8e6074f58f8e22efded1147c85d9  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lam0_T0/history.csv
0d9fc9c8c8f75c0158ae2672d0dd12a8a759f4b1d44d754d661fc58512fa81ef  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lam0_T0/levels.csv
299670cc6a3f1ca722d7c4a578f3f03daf556d4fcb8cd6aa78fda404a5db0df1  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lam0_T0/profiles.csv
73d54200a670dd506f7b6778847dd68da299ced0aa0045fca5088778043baac5  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lam0_T0/run.json
a0944c26b328072fe1d823332b135a0665f1a33ea2269aa7fef10c5f159be48b  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamm1_T0/history.csv
f8de6855c63784e400f8c3b51d02e2cc46e99beab60e399b07f41b6bad92155f  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamm1_T0/levels.csv
f84ce008dee8f4fa974508c542fba812aec214dafb14fe364798fcfadcb8df02  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamm1_T0/profiles.csv
c238b3958b80e935cfc8ae9e945915cb6986b1a8ecb5588ac2308005c372d65d  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamm1_T0/run.json
d6ce528a560d1751ec894658f17c6ae8e8e7d85137a3b32e93f7f4aac8247c43  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamp1_T0/history.csv
eef73b8768587c0e2ba206a5007a3946f5bbf44de3d97b335fd4ceaf962bc563  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamp1_T0/levels.csv
ba7ab60c6b2afd26e8f5c781949688c3a77fe52f7eea16d6150a3668e3805a2c  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamp1_T0/profiles.csv
a79f1fecb3abe6ec852576a4615f27c6e1d2955446db08521a51e64a3eede6ff  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N112_lamp1_T0/run.json
270c97904502f0a015c5c3ac3031c5b7b08731f26f70005f260eefaba46b50e6  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lam0_T0/history.csv
1f56eb5fdf3e2e376ee51f550140693f9bddb1b59259d2e2d3a935519cc93d62  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lam0_T0/levels.csv
d5135cc77edcd30a4394e7a5c3022133b1c15765d8e8b25a91213d01a23c41ee  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lam0_T0/profiles.csv
329315695d965367200c9aaff95b53f0f7ed3bb8b84fa32d50db491af3060273  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lam0_T0/run.json
586ccf6eb0150785b068d17a028cafdb924e8e7ec56913ba8c6348e0d07dcc2f  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamm1_T0/history.csv
6c79caf4c5b525f06d541f9f66b17df34aa7dfa874efab9ea14e7b415eb2f8aa  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamm1_T0/levels.csv
4de65cd2d51adc000462db203fca95b8a798089cb2e2da35b2a2ed39c0057753  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamm1_T0/profiles.csv
4bfa8490ba02312fd8602d135be6064221a431c17bec970931aaa111b81d2bd2  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamm1_T0/run.json
fb74f1c9fdc355b1920d555c0f2a0837efd1b5ce0eea78100a32c8f5b8da8e11  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamp1_T0/history.csv
ebb5c8b5c9b7d53b722a4b06a434ada2f1369c5b4076b0fbad746fdfa6044244  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamp1_T0/levels.csv
e72fc56b3bfd2813788e30e1fef06f169aa5f669c074ee9e5cf346793be62527  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamp1_T0/profiles.csv
b2428e72d57f351b49c3e15d03ecb949c2bcef4a034a2655c7a4a18ea1549fc7  artifacts/dirac16complex/kohn-sham/rust/scf/m3_L3_N8_lamp1_T0/run.json
44017474744f7f501b0a07f5d64a1bb1e8fc8e8412ddf10a3e23313a2a101759  artifacts/dirac16complex/kohn-sham/rust/scf/summary.json
f0b13a0c234154f74c7e7530e1829a066f4ed062183797fbb962f23053d04d80  artifacts/dirac16complex/kohn-sham/rust/spectrum/closed-shells-m1-L3.csv
398861d25ffc6f76b1f4f4dcced8637c1842b62e32124610d73601fd9e4e8dee  artifacts/dirac16complex/kohn-sham/rust/spectrum/closed-shells-m3-L3.csv
0f72852a5384ce5f4279e00e6f3fec1dcb519032a3700c6156446a9eb84239a5  artifacts/dirac16complex/kohn-sham/rust/spectrum/exchange-check.json
4fce3f82ef7f5b489f6b3f6cdde273f1a8816ae52e0c6fcc9e9b5d27827b9ec3  artifacts/dirac16complex/kohn-sham/rust/spectrum/exchange-table-check.json
e85632681b02a51898b17e3e57b761b24aff8abcd4ebc7f2f5aaba878c685d71  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L2.csv
49970f6a02862ae063d258c2546eb1f8232fc05f5ede78de8c6122c8c784665a  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L3.csv
58bc76f6c90ae347874f0640d208368d59c4f4c4c5687aaf348f98276d4ab162  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L4.csv
9c94abada90670bd2f3fa4d3946ac2d6ffda3b115c1a7e5a39925e372815cc68  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L2.csv
c9d4b01371ca748bbeda5b06402cc3c8b7bf1f884de992cfb43d15b776f3c7d8  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L3.csv
574da21949cd87a904fec35da634b3edd6607654ac24684bc09c8c68f71e5626  artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m3-L4.csv
8c1357007a865d02f1fa0b6c4275e1a7cfa5ae910e54a2f408819994a6bd2eba  artifacts/dirac16complex/kohn-sham/rust/spectrum/geometry.json
3d2081f6a12db3bba46788e748405fb9736b34ac6b5dedb7b612a7c7a1da2b9e  artifacts/dirac16complex/kohn-sham/rust/spectrum/reduction.json
52d4eb13142740b90ad7aad1c2868748501291ecd9c103149ecc1dadb95c5091  artifacts/dirac16complex/kohn-sham/rust/spectrum/summary.json
42b47ef64141d57b96bdb2e23f66db34ce6a3e7c5a2d03f86c3d33cf20016448  artifacts/dirac16complex/kohn-sham/rust/spectrum/theory-agreement.json
a70ea9fe71405d74d00b21f9bd0f5d4ff7d2a8ec4484d058b3a711ff0e4e0561  artifacts/dirac16complex/kohn-sham/rust/spectrum/uniform-gas-table.csv
70c5e3059ccb2f87c423ca4e0b215e67fe3d049c382c072fec3fa5114d499e16  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0/levels.csv
87ffc9ef64fcb83dcde7063a8d36daeb360df0d4a484bd80195f4f0eeff6c922  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0/profiles.csv
14d2d3b9155f8c78fd1208d516f7b64fb931b6daca8b2f741721fcb34cdfaf74  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0/run.json
fc9c74fc68d1de91181266c823a7ad2f8819c07e64123887f23a4edfd07a23e6  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p1/levels.csv
a21a46f9ce84c5a4bc59ccd6fcff7e4eff012ac18651bb5dc475ddbfcd9bee17  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p1/profiles.csv
07de0a8b2dd12a1ba52e9a5a6bc80405ae547a26227877a36293e758e444bc98  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p1/run.json
6b3c508780e3f7a1ea82627665cfe42bcbdbd7c08c500a757fffe74626bc4d18  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p3/levels.csv
26af6746fcaee248d6fac28abbd0048fbd763220945c5eb23d2240092d920722  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p3/profiles.csv
b24b8f773fddcdc6dd14efcf54d1bbb3d161670f12d84f14e2afb918b60730e6  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T0p3/run.json
8de8dca366e53dcfda550d0ee8605a0a204dc58ef0df8a2b259b037d899c8a6d  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T1/levels.csv
ee5aab3a1f269c20eda74f8dd11b8102763847da8ec89fd0e7ac9b84a20a958a  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T1/profiles.csv
5c6207e0f1070fa989065374657c474e614303d6f62813f9ae519d1809c5ccd9  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lam0_T1/run.json
72dd1fde5c2f54ce64c5b336e44f46b8c2b87fbf7562c7f02e39c9ae3ca771bb  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0/levels.csv
bf474f9dbd36d692c9011e934da097d0442f80cd3d5f1fc0aae599461d12b4e5  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0/profiles.csv
cd63fb3f383bbdffb4460d818c5184b62f939baf70df3aede777de187bfebb3f  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0/run.json
808d769ff6f6b467f034f59576f0af4d24dfd392c18149250ac0b88ce7c58bdc  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p1/levels.csv
6df821216541853a5245258624c0a5cd0364b91d42c996c930e13b8c43f79769  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p1/profiles.csv
13aec08fcdf30ead3ff0d998ec7390687aaaa505de32ea7839e747995903d6c9  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p1/run.json
69ab09642012afa38235e60cc24ae151d93acb2be4b4d561d7d4ed36b4a1d03b  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p3/levels.csv
0f4eee8dcc933e3bff2eeeea7aab8bce815672bdd88885c4703dc22838a3e114  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p3/profiles.csv
cdad6238aaf17927d3ea68d94bc1b853d6c28cd2e816b8a1ec9dd4e4da8883c0  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T0p3/run.json
cfa4ce0ef1d5c3a0e0869efeba05337e1398d12e53f3db2c99334fbecd0cc391  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T1/levels.csv
97314c3e91d2acfeecf33dad394b75f291a03f25fb05e5f8e03f8781b0eadd85  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T1/profiles.csv
c3f2e680eca223beb97dcc869d5f81cee188e45307955fb18705dbace5a7f26a  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamh_T1/run.json
06afe1ff14ffca71bc100343ee132bd028e71d3973f832320175d3670559ada5  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0/levels.csv
b4550e9fd93a48d7febf7fb310737d81ba64829432c57d33f609e023485db3b2  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0/profiles.csv
68a5940873aec1f956c4b5d0acd632f43ffb10f7e9d83140762f46cb12e514f2  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0/run.json
58fb86b8e529ce04ec9db1ce69d35f2357e3c61b3c3209be429f28d1b5e78b8b  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p1/levels.csv
5764b1f2e3495a5ed6acb40579db34cc8038d87889b71852792018086fb07a76  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p1/profiles.csv
01786a95bb6cb09c85fa95ea4af2e31ddcc2b84e42ddd54e5016154748ab33d2  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p1/run.json
a4c3b0e488252335364c65b22ec311fdf022622b7ac10fdeabfc0416938bb53c  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p3/levels.csv
39db2bd871d6783f31f5eb9276c01d5afeb86c7bb4b01a3341cf627f1f823ba3  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p3/profiles.csv
aa748f31ae96f982e54ee45c970644f023e501c40c37261d3404247aaa26319b  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N112_lamp1_T0p3/run.json
dac6f7c7b1f71d43c0f5773ab892edc071e232e7e96282cb8ea91055fe450270  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0/levels.csv
63ec99ff595ed63f40d72504f37782c1b55d27a0f6e93933d7ca3050724cc679  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0/profiles.csv
9e15994b199bf134b14be57201f2649af8247cf7ec4f66b60932ba879bc95bdf  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0/run.json
f5f2e7f18c95dd16e2804146ff9f976f588f68c102f2372307639a9f49097b94  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p1/levels.csv
659a52cc3eeb15c1e2939f47ce0564bf9614390b8286fcf39889c73090192ab9  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p1/profiles.csv
8490921b66f94961af14430f0269cfda36fdf9d247999eb9a5546377a57a56a4  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p1/run.json
b309030a9b62677bd55ad4af63ef8c6c6e2f3142b487f15deeb9806289117d0a  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p3/levels.csv
e9b5423a68a4ebce10652305148143b09a73761e5e6fc24a2a49f2cd17e579c0  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p3/profiles.csv
b96903f2e6009cf3f443d878df20ad19c62f4c9b8bd669a42f77b6a917f1bc88  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T0p3/run.json
3a8fa7835ed952605a3bda05d789755a4c219ae28cf8ed05fcbbb160941dedc2  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T1/levels.csv
c77c11ee3c138edb210b69102a2da93760115e7e2fb1687e4c882330a190af71  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T1/profiles.csv
401fc850f56445844548b46e29ea50110f0a5d9f49331f3beb64191f4ac1a47c  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lam0_T1/run.json
7edf66cfb3d36c90d4ef290eb1f019259572810b93550f6151af9bfb7b9083ed  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0/levels.csv
e046371358f46bf7e70ffdd768b1c8eac4d4d3b1e97d656e0cd99a28b7fe7e39  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0/profiles.csv
7e685003409f092c895711d76de033a1466b21d3840d86f13d7b2b66c351416e  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0/run.json
90f1e33745c47f95fc97a6e6a78292f13d8743c44331eb352329bf6104b3158a  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p1/levels.csv
2bdeeb971fe4b101004fbea75417f289bf8d798bcbcf315de89fa73443a7019c  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p1/profiles.csv
1aed8b56c8cb40599e8ed2fcf453eb55acc95f5087a4f7fae937465e3ad6c81b  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p1/run.json
3db59aad201ddc907f59a38a973b1d9e35251b8350a72e3da27b43a8cb115d5e  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p3/levels.csv
f875edbf395298a02b11e8beb1365a6925d707f620d2ecc37c3bdd5bfff659c3  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p3/profiles.csv
b11a295e27b69af0e4b7eef87588268a07a78529ac18e261d7fe5ed0cab286c3  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T0p3/run.json
944b0850885aa4d2929a0b288dbbe2e17a04dada39e8a551ab851908a7fd1fd8  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T1/levels.csv
8497db2397405c7295fd2fe19a5461f3c0e63c0d5f4682613d35de11038d0bde  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T1/profiles.csv
b6c587bfae1eb25e2ec42653276605e73da66090df07923d87644c9c3b876dea  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamh_T1/run.json
5bd0f63c558bf59fd257ff1fed51fa5ee572a4ad31e31bd7500d60804b024419  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0/levels.csv
7dcf60ffa8386925d83bccefcb447b67c3df0d3959ff54f74bc911e69b7832e1  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0/profiles.csv
64624e2efa7b46f11ce37237e8b438faeb6c0d78820276b258a601ee887daac0  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0/run.json
ee594afe4736e9439dc10ed53af9fbfd17c78705d0f417b2a6e7283834875b8c  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p1/levels.csv
bc6bd2022cf1eb911fbe23df4ca451d91da9e2ffffa973bbe279ebb6fb109261  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p1/profiles.csv
5ae5211fa3aa93acd58b1dc0c049cd4cac647f952128a03b0d51a59cec9362ae  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p1/run.json
d40f2c30ce4d33c53644fd331a7e2ec0556d9f57f2f7bd8c9c645dc185e0681e  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p3/levels.csv
548ea2c27f1a33477bff3de5e610ab1d54ee3b66fedc45305a89b43afb80c68f  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p3/profiles.csv
d9478dfa9e105c25c32acf16527dec37fae886c270cdf85b47ed75040e056da7  artifacts/dirac16complex/kohn-sham/rust/thermo/m1_L3_N8_lamp1_T0p3/run.json
2d59bcec411c16a3dc4e4da71bced467f6c73dd113746a90c16c8a6c602f7fef  artifacts/dirac16complex/kohn-sham/rust/thermo/summary.json
54a4729cfba7c5f87d6a2c463475774cb4d7bde12ead3989d80fb0cfbde71287  artifacts/dirac16complex/kohn-sham/rust/thermo/thermodynamics.csv
9f04bc10b2e513a790ea6f317473caa8d245a98ee38cbdeb5997f17557fe8978  artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
a2883b47fd5a4febbf19fe479c1b7afaa1ba001621a0455e946e1682c02294ee  scripts/check_dirac16complex_kohn_sham.py
7e710f4afcf9ee33a470919714c6f3a7a9b492bf2b7fd6cc27badc821e7f6486  scripts/ks_reference_solver.py
82088af7fa49c16b764a8b7ad9fea9d1cc8079ad0bd1e9c630c9c37f9847059c  studies/dirac16complex_kohn_sham/tools/compare_runs.py
```

</details>

## 3. How to run it (complete instructions)

### 3.1 What you need

- A 64-bit computer with Windows 10 or 11, macOS, or Linux, and about 2 GB of free disk space: the repository takes about 730 MB after the download (measured on the evening of 2026-10-07: 226 MB of it is Git's history in the hidden folder `.git`, 506 MB the files; the repository grows as work is added), the solver engine 84 MB, the built program 18 MB and the private Python environment about 360 MB; a clone with everything built and run took 1.2 GB.
- About 1 GB of free memory (the whole run used at most about 410 MB on the test machine).
- An internet connection for the installation, for the download of the repository and the solver engine, and for the Python packages. The notebook itself does not use the network.
- Four programs: **Git**, **Python** 3.11 or newer (tested with 3.14.5 on Windows and 3.12.3 on Linux), **Rust** (tested with `cargo` 1.91.1 on Windows and 1.93.1 on Linux) and, on Windows, the **Microsoft C++ build tools** that Rust needs for linking. You do **not** need Wolfram software or Mathematica for this notebook.
- **macOS was not tested.** The macOS commands below follow the Linux ones but were never run on a Mac, and the results promised for Windows and Linux (the byte-identical `spectrum` re-run, the figures, the SHA-256 of the route-C copy) are unverified there; on a Mac with an Apple processor the compiler flag of `.cargo/config.toml` may not even apply (Section 6.1).

### 3.2 Open a terminal

A terminal is a window in which you type commands. Type each command exactly as shown (one line at a time) and press Enter.

- **Windows:** click Start, type `PowerShell`, and open "Windows PowerShell" (or "PowerShell 7", or "Terminal"). The Windows commands below were tested in Windows PowerShell 5.1 and in PowerShell 7.6.
- **macOS:** open Finder, then Applications, then Utilities, then Terminal.
- **Linux:** open your distribution's terminal program (for example "Terminal" in Ubuntu).

### 3.3 Install Git

- **Windows:** download the installer from https://git-scm.com/download/win, run it, and accept the default choices. Close the PowerShell window and open a new one.
- **macOS:** type `git --version`. If Git is missing, macOS offers to install the "command line developer tools"; click Install and wait, then type `git --version` again.
- **Linux:** on Debian or Ubuntu type `sudo apt install git`; on Fedora type `sudo dnf install git`.

Check: `git --version` prints a line such as `git version 2.51.2.windows.1`.

### 3.4 Install Python

- **Windows:** download the installer of Python 3.14 (or 3.12 or 3.13) from https://www.python.org/downloads/windows/, run it, tick **"Add python.exe to PATH"** on the first page, and click "Install Now". Close PowerShell and open a new window. Check: `python --version` prints `Python 3.14.5` (or your version). If Windows opens the Microsoft Store instead, the installer's PATH option was not ticked: run the installer again, choose "Modify", and tick it.
- **macOS:** download the macOS installer from https://www.python.org/downloads/macos/ and run it. Check: `python3 --version`.
- **Linux:** Python 3 is usually installed; you also need its `venv` module. On Debian or Ubuntu type `sudo apt install python3 python3-venv python3-pip`; on Fedora `sudo dnf install python3`. Check: `python3 --version`.

### 3.5 Install Rust

- **Windows:** download `rustup-init.exe` from https://rustup.rs and run it. If it says that the Microsoft C++ build tools are missing, let it install them (or install "Build Tools for Visual Studio" with the workload "Desktop development with C++" from https://visualstudio.microsoft.com/downloads/), then accept the default Rust installation. Close PowerShell and open a new window.
- **macOS:** type `xcode-select --install` (installs the compiler tools; skip if already installed), then `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and accept the default installation. Open a new Terminal window.
- **Linux:** on Debian or Ubuntu first type `sudo apt install build-essential curl`, then `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and accept the default installation. Open a new terminal window.

Check: `cargo --version` prints a line such as `cargo 1.91.1 (ea2d97820 2025-10-10)`.

### 3.6 Download the repository

**On Windows, use a short folder.** The Microsoft linker that Rust uses cannot open files whose full path is longer than 259 characters, and the deepest file it opens while building the program is 103 characters below the repository root. If the full path of the repository folder is longer than 156 characters, the build of Section 3.8 fails with `LNK1104: cannot open file` (this happened in the test, Section 6.3, run 4). A folder such as `C:\work` is safe:

```
mkdir C:\work
cd C:\work
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

(If `C:\work` already exists, `mkdir` prints an error that you can ignore.)

**On macOS and Linux**, go to the folder in which you want the repository (a new terminal starts in your home folder) and type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The download is about 230 MB and took 8 to 19 seconds on the test machine (on Linux under WSL2, into a folder on the Windows disk, several minutes; Section 4.4). The folder `Dirac_claude` is the **repository root**: every command below must be typed there. (If the folder already exists from an earlier download, type `cd Dirac_claude` and then `git pull` to update it.)

### 3.7 Download the solver engine

The Rust program uses a pure-Rust version of the SUNDIALS 7.8.0 solver library that is not stored in this repository. This command downloads it, at a fixed version, into the folder `vendor/rustSolveIt` (about 84 MB):

**Windows (PowerShell):**

```
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11
```

(`-ExecutionPolicy Bypass` allows this one script to run in this one command; it changes no setting of your computer.)

**macOS and Linux:**

```
bash scripts/setup_solver.sh win11
```

Use `win11` on every operating system: the committed result files were produced with the Windows 11 engine, and only this engine reproduces them byte for byte (it did so on Linux in the test, Section 6.3, run 6). The command prints three lines and ends with `solver_setup=OK`:

```
solver_platform=win11
solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3
solver_setup=OK
```

If you run it a second time it prints `solver_setup=ALREADY-PRESENT` instead, which is also fine.

### 3.8 Build the Rust program

The same three commands on every operating system:

```
cd studies/dirac16complex_kohn_sham
cargo build --release
cd ../..
```

The build takes 8 to 23 seconds and ends with a line such as ``Finished `release` profile [optimized] target(s) in 7.52s``. The program is then `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham.exe` (Windows) or `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham` (macOS, Linux). The last command takes you back to the repository root.

### 3.9 Create a private Python environment and install the packages

A "virtual environment" is a private copy of Python in one folder, so that the packages of this notebook do not mix with other Python software on your computer. Create it inside the folder `build/` of the repository (Git ignores that folder), then install the packages with the exact versions used in the test.

**Windows (PowerShell):**

```
python -m venv build/ks-venv
build/ks-venv/Scripts/python.exe -m pip install numpy==2.4.6 matplotlib==3.11.0 pillow==12.2.0 contourpy==1.3.3 kiwisolver==1.5.0 fonttools==4.63.0 pyparsing==3.3.2 nbformat==5.10.4 nbclient==0.10.2 nbconvert==7.16.6 ipykernel==7.1.0 ipython==9.7.0 jupyter_client==8.6.3 pyzmq==27.1.0 tornado==6.5.2 traitlets==5.14.3 pygments==2.19.2 jupyterlab==4.4.10
```

**macOS and Linux:**

```
python3 -m venv build/ks-venv
build/ks-venv/bin/python -m pip install numpy==2.4.6 matplotlib==3.11.0 pillow==12.2.0 contourpy==1.3.3 kiwisolver==1.5.0 fonttools==4.63.0 pyparsing==3.3.2 nbformat==5.10.4 nbclient==0.10.2 nbconvert==7.16.6 ipykernel==7.1.0 ipython==9.7.0 jupyter_client==8.6.3 pyzmq==27.1.0 tornado==6.5.2 traitlets==5.14.3 pygments==2.19.2 jupyterlab==4.4.10
```

The installation takes one to three minutes on Windows (51 to 160 seconds measured, with the packages already in pip's download cache; a first download takes longer) and ends with a line that begins `Successfully installed`. (A notice that a newer `pip` is available can be ignored.) pip also installs about 80 helper packages that the command does not name, in their newest versions; they can be newer on your computer than in the test. In the runs after the restart of 2026-10-07, two of them were newer than in the runs of that afternoon (`json5` 0.16.0 instead of 0.15.0, `platformdirs` 4.12.4 instead of 4.12.3), and no output changed by a single byte. What the packages are for: `numpy` (arrays and numerics) and `matplotlib` with `pillow`, `contourpy`, `kiwisolver`, `fonttools` and `pyparsing` (the figures); `nbformat`, `nbclient`, `nbconvert`, `ipykernel`, `ipython`, `jupyter_client`, `pyzmq`, `tornado` and `traitlets` (reading and executing notebooks: the "kernel" is the Python process that executes the cells); `pygments` (colours in error messages); `jupyterlab` (the browser interface). The versions are pinned because they matter: with `ipython` 9.17.1 instead of 9.7.0 the error message at the end of the notebook shows one more line of code context, so the executed notebook is no longer byte-identical (Section 6.4, run 2).

Check that the environment has the Jupyter kernel:

- Windows: `build/ks-venv/Scripts/python.exe -m jupyter kernelspec list`
- macOS, Linux: `build/ks-venv/bin/python -m jupyter kernelspec list`

It prints `Available kernels:` and one line `python3` followed by a path that ends in `build\ks-venv\share\jupyter\kernels\python3` (Windows) or `build/ks-venv/share/jupyter/kernels/python3`.

You do not need to "activate" the environment: every command below names its Python program directly (`build/ks-venv/Scripts/python.exe` on Windows, `build/ks-venv/bin/python` on macOS and Linux).

### 3.10 Run the notebook

There are four ways to execute the notebook. Route A is the recommended first run: it leaves the committed notebook untouched. Every route takes about one minute (up to two minutes on a busy computer; Section 4.4). Every route writes the 14 figures into `artifacts/dirac16complex/kohn-sham/figures/` (Section 5.1).

**Route A: Jupyter's executor, into a copy (recommended).** This executes all cells with the Jupyter kernel and writes the executed copy to `build/nbconvert/dirac16complex_kohn_sham.ipynb`. The option `--allow-errors` makes it write the copy even though the last cell ends with an error (Section 4.1); without it, nothing would be written.

Windows (PowerShell):

```
build/ks-venv/Scripts/python.exe -m nbconvert --to notebook --execute --allow-errors notebooks/dirac16complex_kohn_sham.ipynb --output-dir build/nbconvert
$LASTEXITCODE
```

macOS and Linux:

```
build/ks-venv/bin/python -m nbconvert --to notebook --execute --allow-errors notebooks/dirac16complex_kohn_sham.ipynb --output-dir build/nbconvert
echo $?
```

The second line prints the exit code. (`build/ks-venv/Scripts/jupyter.exe nbconvert ...` on Windows, or `build/ks-venv/bin/jupyter nbconvert ...` on macOS and Linux, with the same options, is the same program and gave the same result in the test.)

**Route B: the repository's standard-library runner, in place.** This is one of the three ways that section 2 of the notebook itself describes, and the executor the Stage-4 gate uses. It prints everything the cells print while they run. It writes the executed notebook back into `notebooks/dirac16complex_kohn_sham.ipynb` **only if every cell succeeds**; today the last cell fails (Section 4.1), so the file is left unchanged.

- Windows: `build/ks-venv/Scripts/python.exe notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb` and then `$LASTEXITCODE`
- macOS, Linux: `build/ks-venv/bin/python notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb` and then `echo $?`

**Route C: the builder with `--execute`, into a copy.** This writes the notebook from scratch (from the committed result files) into `build/nbclient/dirac16complex_kohn_sham.ipynb` and executes it there with `nbclient`. It writes the executed copy even when a cell fails. This is how the committed copy of the notebook was made (with the default output path, see Section 5.1).

- Windows: `build/ks-venv/Scripts/python.exe notebooks/build_dirac16complex_kohn_sham_notebook.py --execute --output build/nbclient/dirac16complex_kohn_sham.ipynb` and then `$LASTEXITCODE`
- macOS, Linux: `build/ks-venv/bin/python notebooks/build_dirac16complex_kohn_sham_notebook.py --execute --output build/nbclient/dirac16complex_kohn_sham.ipynb` and then `echo $?`

**Route D: the audit of two executed copies.** After routes A and C, this checks both copies and writes a report to `build/notebook-report.json`:

- Windows: `build/ks-venv/Scripts/python.exe notebooks/check_dirac16complex_kohn_sham_notebook.py build/nbclient/dirac16complex_kohn_sham.ipynb --also build/nbconvert/dirac16complex_kohn_sham.ipynb --report build/notebook-report.json` and then `$LASTEXITCODE`
- macOS, Linux: `build/ks-venv/bin/python notebooks/check_dirac16complex_kohn_sham_notebook.py build/nbclient/dirac16complex_kohn_sham.ipynb --also build/nbconvert/dirac16complex_kohn_sham.ipynb --report build/notebook-report.json` and then `echo $?`

**Route E: interactively in JupyterLab (in your web browser).**

- Windows: `build/ks-venv/Scripts/python.exe -m jupyterlab notebooks/dirac16complex_kohn_sham.ipynb`
- macOS, Linux: `build/ks-venv/bin/python -m jupyterlab notebooks/dirac16complex_kohn_sham.ipynb`

Your web browser opens JupyterLab with the notebook. Because the command names the notebook, JupyterLab serves the folder `notebooks` and not the repository root: its file browser on the left lists the files of `notebooks/` (its top folder `/` is `notebooks`), and the notebook opens at an address that ends in `/lab/tree/dirac16complex_kohn_sham.ipynb`. If JupyterLab asks for a kernel, choose **Python 3 (ipykernel)**. Click once into the notebook, then choose the menu **Run**, then **Run All Cells** (or click the first cell and press **Shift+Enter** repeatedly: this runs one cell and moves to the next). While a cell runs, its label shows `[*]`; the status bar at the bottom shows `Python 3 (ipykernel) | Busy` and then `Idle`. After about a minute the last cell shows the gauntlet and the `AssertionError` (Section 4.1). **JupyterLab saves the notebook automatically about every two minutes**, so after a run the committed file `notebooks/dirac16complex_kohn_sham.ipynb` contains your outputs; restore it afterwards (Section 5.6). To stop JupyterLab, choose the menu **File**, then **Shut Down**, and confirm; then close the browser tab. (Pressing Ctrl+C twice in the terminal also stops it.)

**Optional settings (environment variables).** The notebook reads four environment variables; you do not need any of them. `DIRAC16KS_BIN` names the Rust program file if it is not at the place of Section 3.8. `DIRAC16KS_NB_OUTPUT` names another scratch folder for the `spectrum` re-run (default `build/notebook-kohn-sham`). `DIRAC16KS_NB_SPECTRUM=0` skips the 45-second `spectrum` re-run; the gauntlet then prints a `SKIP` line, which the audit counts as a failure. `DIRAC16KS_REPO` names the repository when you execute a copy of the notebook that lies outside the repository. In PowerShell you set one for the current window with, for example, `$env:DIRAC16KS_NB_SPECTRUM = "0"` and remove it with `Remove-Item Env:DIRAC16KS_NB_SPECTRUM`; on macOS and Linux with `export DIRAC16KS_NB_SPECTRUM=0` and `unset DIRAC16KS_NB_SPECTRUM`.

### 3.11 Check the result

After routes A, B, C and D:

1. **Exit codes** (Section 4.2): route A `0`, route B `1`, route C `1`, route D `1`. Routes B, C and D return `1` because the gauntlet has two failed checks (Section 4.1); that is the expected result today, not a broken installation. Route A returns `0` because of `--allow-errors`, so for route A always read the gauntlet lines, not only the exit code.
2. **The audit's last lines** (route D) include exactly

   ```
   measurement_gauntletCount=60
   measurement_gauntletPassed=58
   measurement_gauntletFailed=["rust_vs_reference_eigenvalues", "python_check_report"]
   measurement_gauntletSkipped=[]
   check_count=74
   failed_check_count=4
   ```

   and end with `wrote build/notebook-report.json (verdict FAILURE)` and `notebook_audit=FAILURE`.
3. **The report.** PowerShell: `Select-String -Path build/notebook-report.json -Pattern '"verdict"|"checkCount"|"failedCheckCount"'`; macOS and Linux: `grep -E '"verdict"|"checkCount"|"failedCheckCount"' build/notebook-report.json`. Both print the three lines `"checkCount": 74,`, `"failedCheckCount": 4,` and `"verdict": "FAILURE"` (PowerShell puts the file name and line number in front of each).
4. **What changed in the repository:** on Windows, `git status --porcelain` prints exactly one line,

   ```
    M artifacts/dirac16complex/kohn-sham/figures/rust_vs_reference.png
   ```

   (the 13 other figures were rewritten with identical bytes, so Git does not list them). If you used route E, a second line ` M notebooks/dirac16complex_kohn_sham.ipynb` is expected as well. **On Linux (and probably on macOS) all 14 figures are listed**: their pictures are identical pixel for pixel to the committed ones, but the PNG files are compressed by a different version of the compression library `zlib` and therefore have other bytes (Section 6.4). That is expected, not an error.
5. **The figures' SHA-256** (Windows) are those of the table in Section 2.4 (13 equal to the committed files; `rust_vs_reference.png` equal to `8d572f57621fc606df53454475caf9c24d63c61cfa616c192caddc3c2a1607b7`):
   - PowerShell: `Get-FileHash -Algorithm SHA256 artifacts/dirac16complex/kohn-sham/figures/*.png | ForEach-Object { "$($_.Hash.ToLower())  $(Split-Path -Leaf $_.Path)" }` (one line per figure, the SHA-256 in small letters and the file name, as in the table of Section 2.4; a plain `Format-Table` of `Hash` and `Path` cuts the path off before the file name in a window 120 characters wide)
   - macOS: `shasum -a 256 artifacts/dirac16complex/kohn-sham/figures/*.png`
   - Linux: `sha256sum artifacts/dirac16complex/kohn-sham/figures/*.png`
6. **The executed copy of route C** has the SHA-256 `2bd96fe94a5478003620bf071ac9daf2bf0e68555236e556f336b6878505a4d8` when it was made on Windows with Python 3.14.5 and the package versions of Section 3.9. (On Linux it differs in the recorded Python version, the name of the program without `.exe`, the figures and their SHA-256, and the last digit of one printed round-off number; Section 6.4.) PowerShell: `Get-FileHash -Algorithm SHA256 build/nbclient/dirac16complex_kohn_sham.ipynb | ForEach-Object { "$($_.Hash.ToLower())  $(Split-Path -Leaf $_.Path)" }`; macOS `shasum -a 256 build/nbclient/dirac16complex_kohn_sham.ipynb`; Linux `sha256sum build/nbclient/dirac16complex_kohn_sham.ipynb`.

### 3.12 If it fails

| What you see | Cause | What to do |
|---|---|---|
| `git`, `python`, `python3` or `cargo` is "not recognized" (PowerShell) or "command not found" | The program is not installed, or the terminal was opened before the installation | Open a new terminal. Install the missing program (Sections 3.3 to 3.5). |
| `fatal: destination path 'Dirac_claude' already exists` | The repository was downloaded before | Type `cd Dirac_claude` and `git pull` instead of cloning again. |
| `vendor/rustSolveIt is at ..., expected ...; remove it and rerun` or `... is an incomplete checkout` | An earlier, different or interrupted download of the solver engine | Delete the folder (`Remove-Item -Recurse -Force vendor/rustSolveIt` in PowerShell, `rm -rf vendor/rustSolveIt` on macOS and Linux) and run Section 3.7 again. |
| `error: linking with link.exe failed: exit code: 1104` and `LNK1104: cannot open file '...\target\release\deps\libdirac16complex_kohn_sham-....rlib'` | The repository folder is too deep on Windows (path longer than 259 characters) | Clone the repository again into a short folder such as `C:\work` (Section 3.6). |
| `error: linker link.exe not found` (Windows) or `linker cc not found` (Linux) | The C/C++ build tools are missing | Install them (Section 3.5) and run `cargo build --release` again. |
| `error: failed to load manifest for dependency cvode_rs`, caused by `failed to read` the file `vendor/rustSolveIt/sundials_rs/crates/cvode_rs/Cargo.toml` (exit code 101; Windows prints the path with backslashes) | The solver engine was not downloaded | Run Section 3.7, then Section 3.8 again. |
| `No module named venv` or `ensurepip is not available` (Linux) | The `venv` module is missing | `sudo apt install python3-venv` (Debian, Ubuntu), then repeat Section 3.9. |
| `ERROR: Could not find a version that satisfies the requirement numpy==2.4.6` | Your Python is older than 3.11, or no internet connection | Install Python 3.12 or newer (Section 3.4) and repeat Section 3.9. |
| The notebook stops in cell 2 with `RuntimeError: dirac16complex_kohn_sham binary not found - build it first: ...` (route B prints `FAIL notebooks\dirac16complex_kohn_sham.ipynb (cell 2): RuntimeError(...)`) | The Rust program was not built, or the build failed | Do Sections 3.7 and 3.8; check that the program file of Section 3.8 exists. Route A still returns exit code `0` in this case (because of `--allow-errors`), so always read the outputs: in its copy cells 2 and 3 show this `RuntimeError`, the other cells still run (they still rewrite the 14 figures), and the last cell ends with `NameError: name 'CONFIG' is not defined` (re-tested on 2026-10-07 after the restart, with the program file renamed). |
| `RuntimeError: start the notebook inside the Dirac_claude repository ...` | The notebook was executed outside the repository | Execute it from the repository root, or set `DIRAC16KS_REPO` to the repository folder (Section 3.10). |
| `No such kernel named python3` | The kernel package is missing from the environment you used | Use the Python program of the environment (`build/ks-venv/...`) as written, and check Section 3.9 (`jupyter kernelspec list`). |
| `RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq ...` (Windows) | A harmless notice of the `pyzmq` package on Windows | Nothing; it appeared in every test run. |
| The gauntlet shows `FAIL - fresh_spectrum_byte_identical: .../15 files ...` | The solver engine is not the Windows 11 engine of Section 3.7, or the program was built without the `.cargo/config.toml` flag | Use `win11` in Section 3.7 (delete `vendor/rustSolveIt` first) and build again from inside `studies/dirac16complex_kohn_sham` (Section 3.8). |
| More than two `FAIL` lines, or `FAIL - prose_numbers_match_files`, or a `SKIP` line | A committed input file was changed or is missing | `git status` shows which; restore it with `git checkout -- <file>` and run again. |
| `git status --porcelain` lists more files than in Section 3.11 | A route that writes into committed files was used (Section 5.1); on macOS and Linux all 14 figures are listed anyway (Section 3.11, step 4) | Restore them (Section 5.6). |

## 4. The expected output

### 4.1 What is printed

**Route B (the runner)** prints everything the 18 code cells print while they run and then an empty line and its own two last lines, 343 lines in all in the test. The cells print, in this order:

1. `data loaded: theory, exchange table, Rust summaries {...} | runs: scf 33, excited 16, thermo 22, emt 10 | determinism report present | cross-check report present`
2. `repository : found ...`, `program    : studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham.exe` (without `.exe` on macOS and Linux), `fresh runs : build/notebook-kohn-sham | ...`, and the 24 configuration lines of the Rust program (`study = dirac16complex-kohn-sham` to `all = spectrum, scf, excited, thermo, emt`) ending with `SUCCESS`;
3. `== spectrum ==`, the 33 self-check lines of the Rust program (`PASS - reduction_exact_to_1e14: ...` to `PASS - coupling_scale_positive: ...`), `spectrum: solver_steps=39152872 rhs_evaluations=47587645 files=15 verdict=SUCCESS`, `SUCCESS`, and `15/15 freshly written spectrum files are byte-identical to artifacts/dirac16complex/kohn-sham/rust/spectrum/`;
4. cells 4 to 17: the recomputed quantities (for example `k = 0 box spectrum: max |eps_Rust - eps_exact| = 2.80e-10 ...`, `all 33 scf runs converged with both residuals < 1e-10: True`, the table of thermodynamics and the table of the energy-momentum tensor), the run-by-run comparison with the reference solver (`agree  canonical_E0: ...` and so on, with one line `DIFFER  canonical_eigenvalues: ...`), `python-check-report.json: 63 checks, 1 failed ['canonical_eigenvalues']; ...`, and one line `figure <name>.png sha256 <SHA-256>` for each of the 14 figures;
5. cell 18, the gauntlet, prints exactly the 62 lines below (identical in every route and every run of the test with the committed inputs: runs 1, 2, 5, 6, 7, 8, 10, 11, 12 and 14 of Section 6.3, on Windows and on Linux), and then fails with the error shown in the last line:

```
PASS - program_runs_success: 2 program runs (print-config, spectrum), every one exited 0 with SUCCESS as its last line
PASS - fixture_hash_consistent: print-config and 5 summaries name the algebra fixture sha256 8b4f15462ca4d61e...
PASS - fresh_spectrum_byte_identical: 15/15 files of the re-run spectrum subcommand equal the committed ones
PASS - rust_spectrum_self_checks: 33/33 checks of the program true, verdict SUCCESS
PASS - rust_scf_self_checks: 137/137 checks of the program true, verdict SUCCESS
PASS - rust_excited_self_checks: 65/65 checks of the program true, verdict SUCCESS
PASS - rust_thermo_self_checks: 102/102 checks of the program true, verdict SUCCESS
PASS - rust_emt_self_checks: 60/60 checks of the program true, verdict SUCCESS
PASS - determinism_report_current: repeat byte identity and refined convergence ['canonical_summaries_present', 'canonical_verdicts_success', 'refined_convergence', 'repeat_byte_identity']; summaries changed since the report was written: []
PASS - exact_theory_wolfram: 125/125 exact checks of scripts/verify_dirac16complex_kohn_sham.wls (wolfram/Dirac16ComplexKohnSham.wl) true
PASS - exact_theory_python_sympy: 157/157 exact checks of scripts/check_dirac16complex_kohn_sham_theory.py true
PASS - algebra_relations_exact: Clifford relations, C = g0g1g2g3, B = -iCg4, B^2 = 1 from the integer fixture: exact (0.0)
PASS - block_basis_exact: unitary 1.1e-16, off-block 7.0e-17, vs stored blocks 1.1e-16, vs closed forms 1.1e-16; two types j = +-1, 4 blocks each
PASS - block_ode_exact: g0[M - i kk g1 + i(eps - v) g4] -> M s3 - kk s2 + i j (eps - v) s1 in every block: 4.4e-16
PASS - exchange_closed_form: double quadrature vs -(n^2 + S^2)/32: 1.7e-14; v_v, v_s, n-only v_x columns: 1.7e-14; the table the Rust spectrum run checked is this file (sha256)
PASS - box_spectrum_analytic: k = 0 levels of 6 (m, L) x 2 parities x 2 types vs sqrt(M^2 + (n pi/L)^2), tan(pL) = -p/M: 2.8e-10
PASS - chiral_zero_mode: eps = 0 and zero scalar charge: 0.0e+00
PASS - zero_mode_splitting: in-cell RK4 shooting slope vs closed-form c: 1.5e-07 (12 cases); sign = -s (s = -j); program's Hellmann-Feynman slope vs closed form 1.2e-09
PASS - mirror_spectra_and_multiplicities: s = -1 levels = -(s = +1 levels): 0.0e+00; multiplicity 4 r3(n2) everywhere
PASS - particle_number: 65 runs: sum of weights 4.2e-11, density integral 7.3e-08 (vs the program's own 6.3e-16)
PASS - energy_recomputed: E_H 5.0e-19, E_x 2.6e-18, sum w eps 1.8e-14, E = sum w eps - E_H - E_x 1.8e-14
PASS - pseudo_potential_formula: M_eff = m + (15/16) lambda S_p: 2.5e-06, v_x = -lambda n_p/16: 9.0e-07 (relative to the potential scale; self-consistency of the last iteration)
PASS - profile_columns: n_c = e^(6Hy) n_p, volume factor, z = arcsin e^(6Hy): 2.2e-16
PASS - scf_converged: all 33 scf runs converged, residuals < 1e-10
PASS - closed_shells_and_aufbau: closed shells from the free spectrum vs closed-shells-m1-L3.csv 2.5e-12; aufbau E0 vs scf lambda = 0: 5.6e-12
PASS - first_order_coupling: +-lambda_hat_1: |(E0(lambda) - E0(0)) / (lambda dE/dlambda|0) - 1| = 0.025 < 0.05
PASS - ks_gap_recomputed: LUMO - HOMO from levels.csv vs the run records 0.0e+00, vs scf run.json 0.0e+00, vs excitations.csv 0.0e+00; records vs excitations.csv 0.0e+00
PASS - delta_scf_bookkeeping: E1 - E0 = Delta-SCF 0.0e+00; excited ground state = scf ground state; exactly one particle moved up 0.0e+00
PASS - delta_scf_equals_gap_free: lambda = 0: Delta-SCF = KS gap to 3.7e-10
PASS - particle_hole_lists: 16 lists rebuilt with the 1e-12 occupation floor: max deviation 0.0e+00; differing runs []
PASS - level_crossing_run_as_documented: smearing 1e-3 m at T = 0, F = E, exact occupations false; fractional levels = the 192-fold band (f = 0.9781) and the 8-fold k = 0 level (f = 0.5266); 4.213 particles moved; N = 1016 is a closed shell of the free aufbau
PASS - entropy_and_free_energy: S from the occupations vs run.json 1.1e-14; |E - TS - F| 0.0e+00
PASS - heat_capacity_forms: lambda = 0: the two fixed-spectrum forms agree to 5.7e-15, the central difference agrees with them to 7.5e-03 < 1e-2 (the checker's tolerance); lambda != 0: forms differ by 7.7e-04 (measured)
PASS - thermodynamic_monotonicity: F decreases and S increases with T in all six series
PASS - emt_recomputed: int rho dV = E 4.2e-10; proper volume (Simpson) vs l^3 (1 - e^(-6HL))/(6H): error / its leading-order value h^4 (6H)^4/180 = 0.9996; averages 4.5e-16; w 1.8e-15; p_t = L_s 1.0e-17; kappa needed 5.0e-16; E4.1 4.1e-16
PASS - emt_conservation: (e^(6Hy) p_y)' = 3H e^(6Hy)(p_3 + p_t), fourth-order stencil: 1.1e-06 < 1e-2 (program's own measure 2.1e-05)
PASS - einstein_source_mismatch: rho_req = -21 H^2/kappa < 0 while <rho> > 0 for every N > 8 run (kappa < 0 needed); E4.1 met in no run; <S_p> < 0 at lambda = 0
PASS - brane_fraction: within 1/H of the brane recomputed for 33 runs: 5.6e-16; tip 4.2e-17
PASS - l_convergence_trend: |X(L=4) - X(L=3)| <= |X(L=3) - X(L=2)| for E0 and the KS gap, 4 series
PASS - grid_convergence: 601 vs 301 grid points: 4.7e-11
PASS - a4_rescaling_exact: a4 = 0.5 vs its a4 = 0 partner: levels 1.6e-10, E0 4.6e-13
PASS - rust_vs_reference_E0: E_0 (lambda_hat-corrected): |dE| <= 1e-06 max(|E|, N m); 80 comparisons, worst 8.276e-07 (tolerance 2.400e-05, ratio 0.0345) at scf/m3_L3_N8_lamm1_T0 ; failures: []
PASS - rust_vs_reference_deltaSCF: Delta-SCF E_1 - E_0; 16 comparisons, worst 1.532e-06 (tolerance 1.938e-06, ratio 0.79) at excited/m1_L3_N1016_lamm2_T0 ; failures: []
PASS - rust_vs_reference_eigenvalueMatching: every level in the common window matched, same branch, same T = 0 occupation; 81 comparisons, worst 0.000e+00 (tolerance 5.000e-01, ratio 0) at scf/m1_L2_N112_lam0_T0 unmatched 0, branch mismatches 0, occupation mismatches 0, compared 460; failures: []
FAIL - rust_vs_reference_eigenvalues: eigenvalues per (q, parity, block type): |d eps| <= 1e-06 max(1, |eps|/m) m + dl max|V|; 58412 comparisons, worst 2.195e-06 (tolerance 1.054e-06, ratio 2.08) at scf/m1_L3_N1016_lamm2_T0 eps -1.05374908; failures: ['scf/m1_L3_N1016_lamm2_T0', 'scf/m1_L3_N1016_lamm2_T0', 'scf/m1_L3_N1016_lamm2_T0', 'scf/m1_L3_N1016_lamm2_T0', 'excited/m1_L3_N1016_lamm2_T0', 'excited/m1_L3_N1016_lamm2_T0', 'excited/m1_L3_N1016_lamm2_T0', 'excited/m1_L3_N1016_lamm2_T0']
PASS - rust_vs_reference_emtAverages: proper-volume EMT averages; 390 comparisons, worst 5.834e-05 (tolerance 1.318e-04, ratio 0.443) at thermo/m1_L3_N112_lam0_T1:rhoAvg ; failures: []
PASS - rust_vs_reference_fractions: brane and tip fractions; 130 comparisons, worst 1.618e-06 (tolerance 1.000e-05, ratio 0.162) at scf/m1_L4_N112_lam0_T0:braneFraction_within_1_over_H ; failures: []
PASS - rust_vs_reference_heatCapacity: C_V central difference and fixed-spectrum forms; 44 comparisons, worst 2.761e-05 (tolerance 1.000e-03, ratio 0.0276) at thermo/m1_L3_N112_lamh_T0p3:C_V_fd ; failures: []
PASS - rust_vs_reference_lambdaHat: couplings derived independently on both sides; 81 comparisons, worst 4.979e-08 (tolerance 2.000e-07, ratio 0.249) at scf/m1_L4_N8_lamp1_T0 ; failures: []
PASS - rust_vs_reference_muAndGap: mu, eps_HOMO-based KS gap: |d| <= 1e-06 max(m, |x|) + dl max|V|; 160 comparisons, worst 2.412e-07 (tolerance 3.002e-06, ratio 0.0803) at scf/m3_L3_N8_lamp1_T0:mu ; failures: []
PASS - rust_vs_reference_particleHole: lowest particle-hole excitation; 16 comparisons, worst 1.343e-08 (tolerance 1.000e-06, ratio 0.0134) at excited/m1_L3_N1016_lamp2_T0 ; failures: []
PASS - rust_vs_reference_profilesEnds: profiles on the two end nodes (O(h^3) reference end values); 610 comparisons, worst 3.063e-04 (tolerance 2.000e-03, ratio 0.153) at scf/m1_L3_N112_lamp2_T0:p_t ; failures: []
PASS - rust_vs_reference_profilesInterior: profiles on the interior common nodes (relative to the profile scale); 610 comparisons, worst 1.291e-05 (tolerance 2.000e-05, ratio 0.646) at scf/m3_L3_N8_lamm1_T0:p_3 ; failures: []
PASS - rust_vs_reference_sourcingConditions: E4.1 verdict and sign of <S_p> agree; 65 comparisons, worst 0.000e+00 (tolerance 5.000e-01, ratio 0) at scf/m1_L2_N112_lam0_T0 ; failures: []
PASS - rust_vs_reference_thermodynamics: E, F, S, mu at T > 0 after the correction for the Rust level set (f_cut window, shell cap); 68 comparisons, worst 4.093e-03 (tolerance 1.809e-02, ratio 0.226) at thermo/m1_L3_N112_lamh_T1:freeEnergy ; failures: []
PASS - rust_vs_reference_coverage: 81 Rust runs compared with the reference run of the same label; without a reference run: []; unreadable reference directories: []
PASS - reference_summary_complete: reference-summary.json: complete = True; labels compared here but not recorded in it: []
FAIL - python_check_report: 63 checks, failed ['canonical_eigenvalues']; inputs changed since it was written: []; not recorded: []
PASS - figures_written: 14 of 14 PNG figures in artifacts/dirac16complex/kohn-sham/figures, hashes re-read
PASS - prose_numbers_match_files: 171 numbers and strings quoted in the markdown re-read from the committed files

gauntlet: 60 checks, 58 passed, 2 failed, 0 skipped
AssertionError: gauntlet failed: rust_vs_reference_eigenvalues, python_check_report
```

After that the runner prints an empty line and then its own two lines:

```

FAIL notebooks\dirac16complex_kohn_sham.ipynb (cell 18): AssertionError('gauntlet failed: rust_vs_reference_eigenvalues, python_check_report')
0 ok, 1 failed
```

(with `/` instead of `\` on macOS and Linux).

**Route A (`nbconvert`)** prints only

```
[NbConvertApp] Converting notebook notebooks/dirac16complex_kohn_sham.ipynb to notebook
[NbConvertApp] Writing 1862498 bytes to build\nbconvert\dirac16complex_kohn_sham.ipynb
```

(on Windows also the harmless `RuntimeWarning` of Section 3.12, and the first time also `[NbConvertApp] Making directory build/nbconvert`; on macOS and Linux the path is printed with `/`). Without `--allow-errors` (Section 4.2) `nbconvert` instead prints a Python traceback that ends in `nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:`, followed by the source code of the gauntlet cell, the gauntlet lines above and the `AssertionError` (about 500 lines in all), and writes no copy. The number in the second line is the number of characters of the copy before it is written, and it changes by a few hundred from run to run (1862498 on 2026-10-02; 1862866 and 1862672 in the two launchers of run 7 on 2026-10-07; 1862672 and 1862769 in run 10, 1862672 for both launchers in run 11, 1862672 in run 14 on 2026-10-08), because the copy contains time stamps (Section 4.3). The outputs of the cells, including the gauntlet above, are inside the written copy. On Linux the number was 1999090, because the figures embedded in the copy are compressed differently there (Section 6.4).

**Route C (the builder)** prints `wrote build\nbclient\dirac16complex_kohn_sham.ipynb (43 cells, 18 code cells, 171 quoted numbers, 14 figures)`, then `FAIL: a cell raised an error during execution:` with the end of the gauntlet and the error, and finally `execution FAILED for build\nbclient\dirac16complex_kohn_sham.ipynb`.

**Route D (the audit)** prints 74 lines `check_<name>=true` or `check_<name>=false` (false: `check_r07_no_error_outputs`, `check_r07_gauntlet_passed`, `check_gauntlet_rust_vs_reference_eigenvalues`, `check_gauntlet_python_check_report`), 16 lines `measurement_...`, `check_count=74`, `failed_check_count=4`, one line `FAIL build/nbclient/dirac16complex_kohn_sham.ipynb (Jupyter kernel python3 through nbclient): 43 cells, 18 code cells, 60 gauntlet lines, 14 figures; code cell 17 has an error output (AssertionError); gauntlet FAIL lines: rust_vs_reference_eigenvalues, python_check_report; the gauntlet did not print ALL CHECKS PASSED` and the same line for the `build/nbconvert/` copy, then `wrote build/notebook-report.json (verdict FAILURE)` and `notebook_audit=FAILURE`. (The auditor counts code cells from 0, so its "code cell 17" is the 18th code cell, the gauntlet.)

**Why two checks fail.** `rust_vs_reference_eigenvalues`: of 58412 compared eigenvalues of the Rust solver and the independent reference solver, the worst differs by 2.195e-06 against its tolerance 1.054e-06 (ratio 2.08), at the deep level eps = -1.05374908 of the run `m1_L3_N1016_lamm2_T0` (the smeared ensemble at N = 1016 with the attractive coupling); all eight failures belong to that one run (two levels, both block types, its ground-state and excited-state records). `python_check_report`: the committed report of the cross-checker, `python-check-report.json`, contains the same failure (`63 checks, failed ['canonical_eigenvalues']`). The repository's textbook lists this as an open problem (Section 6.6). All 58 other checks pass, among them the byte identity of the re-run `spectrum`, every self-check of the Rust program (397 in five summaries), the 125 Wolfram and 157 sympy exact checks, all in-notebook recomputations and the 171 quoted numbers and strings.

### 4.2 Exit codes

| Route | Exit code on 2026-10-02, 2026-10-07 and 2026-10-08 | Meaning |
|---|---|---|
| A, `nbconvert --allow-errors` | `0` | the copy was written; `0` even when cells fail |
| A without `--allow-errors` | `1` | the last cell failed; **no** copy is written (the folder `build/nbconvert` is created empty) |
| B, `run_notebook.py` | `1` | a cell failed; the notebook was not written back (`0` only if every cell passes) |
| C, builder `--execute` | `1` | a cell failed; the copy was written anyway (`0` only if every cell passes) |
| D, audit | `1` | verdict `FAILURE` (`0` only for verdict `SUCCESS`) |
| unit tests (Section 6.5) | `1` | 26 of 30 tests pass |

### 4.3 Files written, and how to check them

- `artifacts/dirac16complex/kohn-sham/figures/*.png`: the 14 figures (Section 2.4). Check them as in Section 3.11, step 5.
- `build/notebook-kohn-sham/spectrum/`: the 15 files of the `spectrum` re-run, each byte-identical to the committed file of the same name in `artifacts/dirac16complex/kohn-sham/rust/spectrum/` (the gauntlet line `fresh_spectrum_byte_identical` checks this; you can also compare one file with `git diff --no-index --stat artifacts/dirac16complex/kohn-sham/rust/spectrum/summary.json build/notebook-kohn-sham/spectrum/summary.json`, which prints nothing when the files are equal).
- `build/nbconvert/dirac16complex_kohn_sham.ipynb` (route A): about 1.87 MB and about 4000 lines on Windows (1866867 bytes and 4001 lines in run 7; 1866659 bytes and 3987 lines in runs 10 and 11). On Windows `nbconvert` writes it with Windows line endings (carriage return and line feed), so the file has one byte per line more than the number it prints; on macOS and Linux it has plain line feeds. It is never byte-identical between two runs, because `nbconvert` writes the start and end time of every cell into it (cell metadata `execution`) and splits the printed text into pieces at the moments the kernel sent them; with these two things removed, the copies of all runs on Windows were identical (Section 6.4).
- `build/nbclient/dirac16complex_kohn_sham.ipynb` (route C): 3759 lines, 1856513 bytes, SHA-256 `2bd96fe94a5478003620bf071ac9daf2bf0e68555236e556f336b6878505a4d8` on Windows with Python 3.14.5 and the versions of Section 3.9; byte-identical in two runs.
- `build/notebook-report.json` (route D): about 30 KB of JSON with the top-level keys `schemaVersion`, `producer`, `notebook`, `builder`, `runner`, `adaptedFrom`, `kernel`, `fixtureSha256`, `cells` (43), `markdownCells` (25), `codeCells` (18), `executedCodeCells` (18), `rules`, `checks`, `checkCount` (74), `failedCheckCount` (4), `failed`, `measurements`, `sourceSha256`, `executions` (2), `crossExecution` (`identicalGauntletAndFigures`: true), `figures` (14), `gauntlet` (`count` 60, `passed` 58, `failed` 2, `skipped` 0), `verdict` (`FAILURE`). Its SHA-256 depends on the paths of the audited copies that it records; with the paths of Section 3.10 it was `152cd74397b16e88ed33489dac7ac31814ec8ee14f173f234cbe9444a5cea979`.

### 4.4 Run time and memory

On the test machine (24 logical processors, Windows 11) one execution of the notebook took **57 to 64 seconds** with the runner and with `nbconvert`, and **65 to 93 seconds** with the builder's `--execute` (`nbconvert` once took 74 seconds); 46 seconds of it is the `spectrum` re-run of cell 3 (it uses all 24 processors); every other cell takes less than 4 seconds (the longest, cell 17, the comparison with the reference solver, 3.5 seconds), and the rest is the start of Python and of the kernel. The interactive run in JupyterLab took about 70 seconds. The audit takes about 2 seconds, the 30 unit tests 5 to 7 seconds, the build of the Rust program 8 to 15 seconds, the package installation 51 to 68 seconds (with the packages already in pip's download cache; a first download takes longer). On Linux (WSL2) the times were longer, because the repository lay on the Windows disk, which WSL reaches through a slow file-sharing layer: clone 30 seconds, Section 3.7 14 seconds, build 8 seconds, `python3 -m venv` 23 seconds, package installation 874 seconds, route A 107 seconds, route B 102 seconds, route C 282 seconds, route D 4 seconds (run 6); and in run 12 on 2026-10-07 and 2026-10-08: clone 439 seconds, Section 3.7 58 seconds, build 21 seconds, `python3 -m venv` 74 seconds, package installation 913 seconds, route A 124 to 137 seconds, route B 85 seconds, route C 108 seconds, route D 5 seconds. (A clone inside the Linux file system of WSL, or on a real Linux computer, should not suffer from this file-sharing slowness; that was not measured.) Other verification jobs were running on the same machine at the same time, which explains part of the spread.

On 2026-10-07 (runs 7 and 8 of Section 6.3) the machine was busy with other jobs (seven Wolfram kernels of other verification jobs were running, and Windows reported 100 percent processor load when it was checked during run 7), and every step took longer: route A 88 to 118 seconds with `python -m nbconvert` and 98 to 112 seconds with `jupyter.exe nbconvert`, route A without `--allow-errors` 113 to 128 seconds, route B 95 to 107 seconds, route C 95 to 98 seconds, route D 5 seconds, the unit tests 9 to 13 seconds, the build 18 to 19 seconds, the package installation 142 to 149 seconds, the clone 14 to 16 seconds. After the restart of that evening (runs 10 and 11, one after the other) the machine was again fully loaded (Windows reported 100 percent processor load, with 14 Wolfram kernels of other verification jobs running): route A 94 to 115 seconds with `python -m nbconvert` and 108 to 129 seconds with `jupyter.exe nbconvert`, route A without `--allow-errors` 95 to 197 seconds, route B 85 to 86 seconds, route C 105 to 115 seconds, route D 5 to 11 seconds, the gate's comparison step 0.4 to 0.6 seconds, the unit tests 5 to 42 seconds (the first run in a new clone is the slowest), the recording of the files read 61 to 88 seconds, the clone 16.5 to 18.5 seconds, Section 3.7 7 to 8 seconds, the build 18 to 19 seconds, `python -m venv` 11 to 12 seconds and the package installation 88 to 160 seconds. On an idle machine expect the times of the first paragraph.

Memory (peak working set): the Jupyter kernel process 246 to 263 MB, the Rust program 19 to 20 MB, the whole process tree of one execution at most 363 MB; the runner (one Python process) 215 MB. Measured again on 2026-10-07 (every 0.4 seconds, the peak working set that Windows keeps for each process of the run, in MiB): the kernel 262 to 265, the `nbconvert` or builder process 111 to 123, the Rust program 19 to 21, the runner 210 to 215; the sum over all processes of one execution at most 362 to 375 (`python -m nbconvert`, builder) or 407 to 412 (`jupyter.exe nbconvert`, which starts two more small launcher processes). Runs 10 and 11 measured the same way: the kernel 261 to 265, the Rust program 18 to 20, the runner 210 to 211, the launchers 5 each; the sum at most 361 to 376 (`python -m nbconvert`, builder) and 399 to 406 (`jupyter.exe nbconvert`), 211 for the runner and 83 for the audit (one process).

## 5. Side effects

### 5.1 Files in the repository

| File or folder | Route(s) | Effect |
|---|---|---|
| `artifacts/dirac16complex/kohn-sham/figures/*.png` (committed) | every execution | **overwritten**. On Windows: 13 figures with identical bytes; `rust_vs_reference.png` with new bytes (`8d572f57...`, 74124 bytes instead of the committed `b5bf9db2...`, 70659 bytes), because its input files changed (Section 6.4); `git status` lists only this one file. On Linux: all 14 with other bytes but the same pixels (other `zlib` compression); `git status` lists all 14. |
| `notebooks/dirac16complex_kohn_sham.ipynb` (committed) | B only if every cell passes (not the case today); C **without** `--output` (the builder's default path); E when JupyterLab saves (automatically about every two minutes) | **overwritten** with the newly executed notebook |
| `artifacts/dirac16complex/kohn-sham/notebook-report.json` (committed) | D only if you give this path after `--report` (the notebook's own text shows such a command) | **overwritten** |
| `build/notebook-kohn-sham/spectrum/` (15 files) | every execution | created or overwritten (ignored by Git) |
| `build/nbconvert/`, `build/nbclient/`, `build/notebook-report.json` | A, C, D | created or overwritten (ignored by Git) |
| `build/ks-venv/` | Section 3.9 | created, about 360 MB (ignored by Git) |
| `vendor/rustSolveIt/` | Section 3.7 | created, about 84 MB (ignored by Git) |
| `studies/dirac16complex_kohn_sham/target/` | Section 3.8 | created, about 18 MB (ignored by Git) |
| `scripts/__pycache__/` | every execution of the notebook (A, B, C, E): cell 17 imports `scripts/check_dirac16complex_kohn_sham.py`, which imports `scripts/ks_reference_solver.py` | Python's compiled-code cache of these two programs (`check_dirac16complex_kohn_sham.cpython-314.pyc`, `ks_reference_solver.cpython-314.pyc`; `314` is the Python version) created on the first execution (ignored by Git); not created when the environment variable `PYTHONDONTWRITEBYTECODE` is set (as it was in run 7). Measured in run 14 for routes A, B and C; route E executes the same cell in the same kind of kernel as route A |
| `notebooks/__pycache__/` | D (the auditor loads the builder with `importlib`) and the unit tests (Section 6.5); **not** A, B, C or E | created (ignored by Git): `build_dirac16complex_kohn_sham_notebook.cpython-314.pyc` (route D), and also `check_dirac16complex_kohn_sham_notebook.cpython-314.pyc` (unit tests); the same exception (run 14) |
| `tests/__pycache__/` | the unit tests (Section 6.5) | created (ignored by Git), with the same exception |
| `notebooks/.ipynb_checkpoints/` | E (JupyterLab's checkpoint copy of the notebook) | created (ignored by Git) as soon as JupyterLab opens the notebook (run 14) |

No other file of the repository is created, changed or deleted. `git status --porcelain --ignored` after routes A to D showed, besides ` M artifacts/dirac16complex/kohn-sham/figures/rust_vs_reference.png`, only the ignored folders `build/`, `notebooks/__pycache__/`, `scripts/__pycache__/`, `studies/dirac16complex_kohn_sham/target/` and `vendor/` (and `tests/__pycache__/` after the unit tests, `notebooks/.ipynb_checkpoints/` after route E). This was confirmed on 2026-10-07 in runs 8, 10 and 11, where the list was exactly ` M artifacts/dirac16complex/kohn-sham/figures/rust_vs_reference.png`, `!! build/`, `!! notebooks/__pycache__/`, `!! scripts/__pycache__/`, `!! studies/dirac16complex_kohn_sham/target/`, `!! tests/__pycache__/`, `!! vendor/`.

### 5.2 Temporary files and files outside the repository

- While a Jupyter kernel runs (routes A, C, E), its connection file `kernel-<id>.json` exists in Jupyter's runtime folder (Windows `%APPDATA%\jupyter\runtime`, Linux `~/.local/share/jupyter/runtime`, macOS `~/Library/Jupyter/runtime`); it is deleted when the kernel stops. JupyterLab (route E) also writes `jpserver-<id>.json`, `jpserver-<id>-open.html` and, because the command of Section 3.10 names the notebook, `jpserver-file-to-run-<id>-open.html` (the page through which the browser opens the notebook) there while it runs (all three deleted when it is shut down; run 14), updates its notebook-trust database `nbsignatures.db` in the Jupyter data folder (Windows `%APPDATA%\jupyter`) when it saves the notebook, and keeps the window layout in `~/.jupyter/lab/workspaces/` (Windows `%USERPROFILE%\.jupyter\lab\workspaces`).
- matplotlib keeps a font cache (Windows `%USERPROFILE%\.matplotlib\fontlist-v3.11.0.json`, Linux `~/.cache/matplotlib`); it is created the first time and reused afterwards.
- pip keeps downloaded packages in its cache (Windows `%LOCALAPPDATA%\pip\cache`, Linux `~/.cache/pip`, macOS `~/Library/Caches/pip`); cargo and the Rust compiler use their own folders (`~/.cargo`, and short-lived files in the temporary folder).
- The first time a Jupyter kernel starts on a computer (routes A, C, E), IPython creates its profile folder `~/.ipython/profile_default/` (Windows `%USERPROFILE%\.ipython\profile_default`) with the empty folders `db`, `log`, `pid`, `security` and `startup` and the file `startup\README`; later runs reuse it. The headless routes write no command history there (`nbconvert` and the builder keep the kernel's history in memory). This was measured in run 11 with `IPYTHONDIR` pointed at an empty folder; on the test machine the profile already existed, and its files were unchanged by runs 10 and 11.
- The notebook itself creates no temporary files outside `build/`. (On 2026-10-07 every file that the Python process of route B opened was recorded, runs 7, 8, 10 and 11, with the bytecode cache already present or switched off: the only files it opened for writing were the 14 figures, and the only file outside the repository and the Python installation that it read was matplotlib's font cache. The recording of a first execution on 2026-10-08, run 14, found the same, except that the process also wrote the two bytecode files of `scripts/__pycache__/`; Sections 2.3 and 5.1.) In run 11 the variables `TEMP` and `TMP` pointed at an empty private folder for the whole sequence of Sections 3.6 to 3.11 (download, build, package installation, routes A to D, unit tests): it was still empty at the end, so nothing is left in the temporary folder.
- **No Wolfram software is started.** The notebook only reads the committed report `wolfram-kohn-sham-report.json`; it never runs WolframScript or a Wolfram kernel, so it leaves none of the `tmp_*` files that an interrupted WolframScript run leaves in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` on Windows (Section 5.3).

### 5.3 Processes

Routes A, C and E start one Jupyter kernel (a `python` process of the environment); route B runs everything in one `python` process. Cell 2 and cell 3 each start the Rust program once (`dirac16complex_kohn_sham.exe`); the `spectrum` run uses all processor cores for about 45 seconds. Every process ends when the route ends; in route E the kernel runs until you shut JupyterLab down. In runs 10 and 11 the process tree of every step was sampled every 0.4 seconds: it held only `python.exe` processes, `dirac16complex_kohn_sham.exe` and, for `jupyter.exe nbconvert`, the two small launchers `jupyter.exe` and `jupyter-nbconvert.exe`; no Wolfram process and no other program.

### 5.4 Network

The notebook makes **no** network access. The installation does: `git clone` and Section 3.7 download from GitHub, `rustup` from rust-lang.org, Section 3.9 from the Python Package Index (pypi.org). JupyterLab (route E) may also contact pypi.org to look for a newer JupyterLab version (it showed the notice "A new version of JupyterLab is available" in the test); ignore that notice.

### 5.5 Downstream programs

The 14 figures are shown in the earlier textbook (Section 1.4) and their SHA-256 are recorded in the committed `notebook-report.json`. Because `rust_vs_reference.png` is rewritten with new bytes, restore it (Section 5.6) before you build any document or run the unit tests or the Stage-4 gate.

### 5.6 How to restore the committed state

In the repository root (the same command in PowerShell, macOS and Linux):

```
git checkout -- artifacts/dirac16complex/kohn-sham/figures
```

This restores every committed figure of that folder (on Windows only `rust_vs_reference.png` has changed; `git checkout -- artifacts/dirac16complex/kohn-sham/figures/rust_vs_reference.png` does the same there; on Linux all 14 have changed). If you used route E, or route C without `--output`, also `git checkout -- notebooks/dirac16complex_kohn_sham.ipynb`; if you wrote the report to its committed path, also `git checkout -- artifacts/dirac16complex/kohn-sham/notebook-report.json`. Then `git status --porcelain` prints nothing. To delete the scratch files: PowerShell `Remove-Item -Recurse -Force build/nbconvert, build/nbclient, build/notebook-kohn-sham, build/notebook-report.json`; macOS and Linux `rm -rf build/nbconvert build/nbclient build/notebook-kohn-sham build/notebook-report.json`. Delete `build/ks-venv` the same way only when you no longer need the environment.

## 6. Verification record

### 6.1 Date, commit, environment

- **Dates:** 2026-10-02 (runs 1 to 6); 2026-10-07 in the afternoon (runs 7 to 9, a re-test from new fresh clones after the first verification had been interrupted); and, after a session limit had stopped the work of the afternoon in the middle, 2026-10-07 in the evening, 20:38 to 21:19 local time (runs 10, 11 and 13 and the setup and first routes of run 12), and 2026-10-08 from 04:13 (the routes of run 12 again, after the Linux virtual machine had stopped during its route B while the test session was paused overnight). These runs were made from new fresh clones to check this file again, including the records of the afternoon, and not to trust it. A Linux run started in the afternoon was stopped by that session limit after it had created its Python environment; it has no result and is not counted. On 2026-10-08 from 06:07 to 06:25 local time, run 14 checked the corrections of this file that an independent verification had asked for (Section 6.6), in a new fresh clone.
- **Commits verified:** on 2026-10-02 `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`; on 2026-10-07 `d806b00cfd769141b9d3f2c6c46a72de5d8027a2` (run 7), `a11befc261ce71d8b1843edf73de9286715ef296` (run 8), `c65bb82368c0f0188b2bbd7b9d93ff5c86762549` (run 9), `b8a695d1faa7abe43b4b51eb666f25d250420fb7` (runs 10 and 12) and `603f1506a143f731ea1661a040110077c920b785` (runs 11 and 13); on 2026-10-08 `477fa9bb12780395ce41db73cfdab294693c52c3` (run 14; `git diff --name-only c2b33cc 477fa9b` restricted to the set, `studies/dirac16complex_kohn_sham/`, `artifacts/dirac16complex/kohn-sham/`, the algebra fixture, `.cargo/config.toml`, the solver set-up scripts and the gate's audit program lists nothing). Each was the remote `main` of https://github.com/once-ere/Dirac_claude.git when its clone was made (other work kept adding commits that day). `git diff --name-only c2b33cc b8a695d` and `git diff --name-only c2b33cc 603f150` list none of the files of the set, none of the 459 inputs of Section 2.5, nothing in `studies/dirac16complex_kohn_sham/` or `artifacts/dirac16complex/kohn-sham/`, and neither `.cargo/config.toml` nor the solver set-up scripts nor the gate's audit program, so all these commits are the same as far as this notebook is concerned. No uncommitted file was copied into any clone: every file of the set and every input is committed.
- **Windows:** Windows 11 Pro for Workstations 10.0.26200; Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory; Python 3.14.5 (python.org, 64-bit); for runs 1 and 3 the Python installation's own packages (numpy 2.4.6, matplotlib 3.11.0, pillow 12.2.0, nbformat 5.10.4, nbclient 0.10.2, nbconvert 7.16.6, ipykernel 7.1.0, ipython 9.7.0, jupyter_client 8.6.3, jupyter_core 5.9.1, jupyterlab 4.4.10, pyzmq 27.1.0, tornado 6.5.2, traitlets 5.14.3, pygments 2.19.2), for runs 2, 4 and 5 a fresh private environment (Section 6.3); Rust `cargo` and `rustc` 1.91.1 with the Microsoft linker of Visual Studio (MSVC 14.51); Git for Windows 2.51.2 with its bash; Windows PowerShell 5.1.26100.9444 and PowerShell 7.6.6. On 2026-10-07 the same machine and the same versions, with Windows updated to build 10.0.26300.9457; runs 7 and 8 each used a fresh private environment made with the command of Section 3.9 (`pip freeze` showed the 18 pinned versions and `jupyter_core` 5.9.1, and its complete list of 99 packages was identical in the two runs). The commands were run by Windows PowerShell 5.1 scripts that time every step and record its output and exit code. In run 7 the environment variable `PYTHONDONTWRITEBYTECODE=1` was set by the test harness (Python then writes no `__pycache__` folders); in run 8 it was removed, as on a student's computer. It changes nothing else: every output of the two runs is identical (Section 6.4). In the evening (runs 10 to 13) the same machine and versions again (Windows 10.0.26300.9457); every run used a fresh private environment made with the command of Section 3.9 (`pip check`: `No broken requirements found.`; `pip freeze` again 99 packages with the 18 pinned versions and `jupyter_core` 5.9.1, identical in runs 10 and 11, and different from runs 7 and 8 only in the two unpinned helper packages `json5` 0.16.0 and `platformdirs` 4.12.4). Run 10 was driven by Windows PowerShell 5.1.26100.9444 scripts, run 11 by PowerShell 7.6.6 scripts, both timing every step and recording its output and exit code; `PYTHONDONTWRITEBYTECODE` was removed in every evening run. In run 11 the variables `TEMP` and `TMP` pointed at an empty private folder and `IPYTHONDIR` at an empty folder, to see every temporary file and the first-time IPython profile (Section 5.2). The repository paths were 154 characters long (Section 3.6). Other verification jobs kept the processor fully loaded during all evening runs.
- **Linux:** Ubuntu 24.04 under WSL2 (kernel 6.6.87.2) on the same machine; Python 3.12.3; `cargo` 1.93.1; Git 2.43.0 (in run 12 on 2026-10-07 and 2026-10-08 the same versions, Ubuntu 24.04.4, run by a non-login bash with a clean `PATH`, so that `python3` was the system `/usr/bin/python3` and no shell start-up file changed the environment; its fresh environment of Section 3.9 had the same 99 packages and versions as on Windows, except that `colorama` and `pywinpty` are Windows-only and `pexpect` and `ptyprocess` Linux-only; Pillow there uses the system `zlib` 1.3, Windows `zlib` 1.3.1.zlib-ng).
- **macOS: not tested.** No run was made on macOS; the macOS commands of Section 3 were written by analogy with the Linux ones and were never executed, so on macOS the build, the byte identity of the `spectrum` re-run (gauntlet check `fresh_spectrum_byte_identical`), the bytes of the figures and the SHA-256 of the route-C copy are unverified. On a Mac with an Apple processor (`aarch64-apple-darwin`) the committed `.cargo/config.toml` flag `-C target-feature=+fma` names a feature that the compiler does not know for that processor: `rustc --print target-features --target aarch64-apple-darwin` (rustc 1.91.1, checked on 2026-10-08) lists `neon` and `fp-armv8` but no `fma`, whereas the list for Intel Macs (`x86_64-apple-darwin`) has `fma`. rustc may therefore warn about the flag there; what it does was not tested.
- **Solver engine:** `rustSolveIt_Win11_SUNDIALS_7_8_0` at `a8fdff459adfe181573d7924b18bffbdf378fdb3` in every run (`solver_setup=OK`).

### 6.2 What was compared, and what was normalised

Every executed notebook, report, figure and spectrum file was compared byte for byte (SHA-256) with the committed file and between runs. Nothing was normalised for the notebooks written by `run_notebook.py` or by the builder, for the reports, the figures and the spectrum files. Only for the copies written by `nbconvert`, two things were removed before comparing them between runs, because `nbconvert` makes them differ in every run: the cell metadata `execution` (time stamps) and the division of the printed text into pieces (consecutive printed pieces of a cell were joined). The comparison reads both files as JSON and compares the JSON text written again with sorted keys, so the Windows line endings of the `nbconvert` copies play no role; in the evening runs it was made with the same small helper program as in runs 7 and 8 and gave the same normalised SHA-256 `8836527c...`. The normalised SHA-256 depends on how the JSON is written again; this short Python program (save it as `normalise.py` and run `build/ks-venv/Scripts/python.exe normalise.py build/nbconvert/dirac16complex_kohn_sham.ipynb`, or `build/ks-venv/bin/python` on macOS and Linux) prints it: it removes `metadata.execution` from every cell, joins the text of each stream output into one string and appends it to the previous output when that is a stream output of the same name (`stdout` or `stderr`), writes the JSON with `json.dumps(nb, sort_keys=True, ensure_ascii=False, indent=1)` and hashes its UTF-8 bytes. Run 14 (2026-10-08) re-checked it: for the route-A copy of that run it prints `8836527c2018ffa1b48ea583719ae5a52c2d4458a78fb8fb4a4c319032de70de`, the value of runs 7, 8, 10 and 11 (with `json.dumps(nb, sort_keys=True)`, that is ASCII escapes and no indentation, the same copy gives `55e8496f...`, and with the text kept as a list of lines `aa9dfb77...`).

```
import hashlib, json, sys
with open(sys.argv[1], encoding="utf-8") as f:
    nb = json.load(f)
for cell in nb["cells"]:
    cell.get("metadata", {}).pop("execution", None)
    if "outputs" not in cell:
        continue
    outs = []
    for out in cell["outputs"]:
        if out["output_type"] == "stream":
            out["text"] = "".join(out["text"])
            if outs and outs[-1]["output_type"] == "stream" and outs[-1]["name"] == out["name"]:
                outs[-1]["text"] += out["text"]
                continue
        outs.append(out)
    cell["outputs"] = outs
text = json.dumps(nb, sort_keys=True, ensure_ascii=False, indent=1)
print(hashlib.sha256(text.encode("utf-8")).hexdigest())
```

The repository's own auditor normalises nothing; it compares the gauntlet results and the figure hashes of two copies (its check `cross_execution_identical`).

### 6.3 The runs

| Run | Where and how | Steps (exit code, wall time) | Result |
|---|---|---|---|
| 1 | Fresh clone 1, Git Bash, solver from `bash scripts/setup_solver.sh win11`, build 14.6 s, the Python installation's packages | unit tests (1, 7.3 s); builder without execution into `build/` (0, 0.3 s; cells equal to the committed notebook's); route B (1, 60.7 s); route A without `--allow-errors` (1, 61.7 s; no copy written); route A (0, 63.9 s); route C with the default path (1, 68.2 s); audit of the route-C notebook and the route-A copy into the committed report path (1, 1.5 s) | gauntlet 58 PASS, 2 FAIL, 0 SKIP in every route; audit 74 checks, 4 false, verdict FAILURE |
| 2 | Fresh clone 2, Git Bash, solver 6 s, build 11.8 s, a private environment with only the seven main packages pinned (pip then chose ipython 9.17.1, pillow 12.3.0 and other newer helper packages) | the same seven steps: (1, 5.3 s), (0, 0.3 s), (1, 64.4 s), (1, 60.7 s), (0, 63.4 s), (1, 82.2 s), (1, 2.3 s) | identical to run 1 (below) except one line of the error output |
| 3 | Fresh clone 3, Git Bash: reproduction of the committed files (Section 6.4) | route C with the default path (1, 92.9 s); route A into a folder outside the clone (0, 74.2 s); audit into the committed report path (1, 1.6 s) | gauntlet 56 PASS, 3 FAIL, 1 SKIP, exactly as committed; all three committed outputs reproduced byte for byte |
| 4 | Fresh clone in a deep scratch folder (repository path 163 characters), Windows PowerShell 5.1, the commands of Sections 3.6 (`git clone`, `cd`) to 3.11 typed as written | clone (0, 8.6 s); Section 3.7 (0, 4.9 s); `cargo build --release` (**101**, 9.8 s: `LNK1104: cannot open file '...\libdirac16complex_kohn_sham-82a05df8d71b6039.rlib'`, a path of 266 characters); `python -m venv` (0, 7.2 s); pip (0, 68.1 s); route A (0, 21.2 s); route A with `jupyter.exe nbconvert` (0, 17.2 s); route B (1, 0.7 s); route C (1, 4.6 s); route D (1, 1.4 s) | without the program every route stops in cell 2 with `RuntimeError: dirac16complex_kohn_sham binary not found - build it first: ...`; route A still returned 0. This led to the short-folder rule of Section 3.6 and two rows of Section 3.12. |
| 5 | Fresh clone in a shorter scratch folder (repository path 156 characters, deepest linker path 259 characters), Windows PowerShell 5.1, the commands of Sections 3.6 (`git clone`, `cd`) to 3.11 and 5.6 (`git checkout -- .../rust_vs_reference.png`) typed as written, environment of Section 3.9 | clone (0, 7.6 s); Section 3.7 (0, 5.7 s); build (0, 7.5 s); `python -m venv` (0, 5.1 s); pip (0, 51.0 s); route A (0, 61.0 s); route A with `jupyter.exe nbconvert` (0, 57.3 s); route B (1, 56.6 s); route C (1, 64.7 s); route D (1, 2.0 s); then route E in JupyterLab (Run, Run All Cells: about 70 s) | gauntlet 58/2/0 in every route; route-C copy byte-identical to run 1; `git status --porcelain` printed only the `rust_vs_reference.png` line and, after Section 5.6, nothing |
| 6 | Fresh clone, Ubuntu 24.04 (WSL2) bash, the macOS and Linux commands of Sections 3.6 to 3.11 typed as written | clone (0, 29.7 s); `bash scripts/setup_solver.sh win11` (0, 13.7 s); build (0, 7.9 s); `python3 -m venv` (0, 23.4 s); pip (0, 873.7 s); route A (0, 107.3 s); route B (1, 102.2 s); route C (1, 281.9 s); route D (1, 3.9 s); then Section 5.6 | gauntlet 58/2/0 with exactly the same 62 lines as on Windows; `15/15 freshly written spectrum files are byte-identical`; audit 74 checks, 4 false, verdict FAILURE; all 14 figures identical pixel for pixel to the Windows ones but with other bytes, so `git status --porcelain` listed all 14 (and, after `git checkout -- artifacts/dirac16complex/kohn-sham/figures`, nothing) |
| 7 | 2026-10-07. Fresh clone of `d806b00` in a scratch folder (repository path 144 characters), the Windows commands of Sections 3.6 to 3.11 and 5.6 run by a Windows PowerShell 5.1 script exactly as written, a fresh environment of Section 3.9; `PYTHONDONTWRITEBYTECODE=1` set by the test harness | clone (0, 16.3 s); Section 3.7 (0, 8.1 s); build (0, 18.0 s); `python -m venv` (0, 11.3 s); pip (0, 141.9 s); audit of the committed notebook as it is (1, 3.9 s); builder without execution into `build/fresh/` (0, 0.5 s); route A without `--allow-errors` (1, 127.7 s; its folder created empty, no copy); route A (0, 117.6 s); route A with `jupyter.exe nbconvert` into another folder (0, 111.8 s); route B (1, 94.7 s); route C (1, 95.1 s); route D (1, 4.6 s); the gate's comparison step 28 on the route-D report (1, 0.2 s); unit tests right after the routes (1, 10.6 s) and again after Section 5.6 (1, 10.2 s); recording of the files read (Section 2.3; 109.9 s); Section 5.6 again | gauntlet 58/2/0 in every route with the 62 lines of Section 4.1 character for character; route B printed the 343 lines of Section 4.1; audit 74 checks, 4 false, verdict FAILURE; route-C copy `2bd96fe9...` and report `152cd743...`, the same bytes as in runs 1 and 5; `git status --porcelain` printed only the `rust_vs_reference.png` line and, after Section 5.6, nothing |
| 8 | 2026-10-07. Fresh clone of `a11befc` next to run 7, the same script and steps, `PYTHONDONTWRITEBYTECODE` removed; the unit tests also run first, on the untouched clone | clone (0, 13.9 s); Section 3.7 (0, 9.3 s); build (0, 18.8 s); `python -m venv` (0, 21.3 s); pip (0, 149.3 s); unit tests first (1, 9.2 s); audit of the committed notebook (1, 2.8 s); builder without execution (0, 0.8 s); route A without `--allow-errors` (1, 112.5 s); route A (0, 88.2 s); route A with `jupyter.exe nbconvert` (0, 97.9 s); route B (1, 107.2 s); route C (1, 97.5 s); route D (1, 5.4 s); step 28 (1, 0.5 s); unit tests after the routes (1, 13.4 s) and after Section 5.6 (1, 9.5 s); recording of the files read (87.3 s); then route E in JupyterLab (Run, Run All Cells: about 100 s) and Section 5.6 | every output and every printed line identical to run 7 (Section 6.4); `git status --porcelain --ignored` as in Section 5.1; route E as in run 5 (below) |
| 9 | 2026-10-07 (afternoon). Fresh clone of `c65bb82`, Windows PowerShell 5.1 scripts, setup of Sections 3.6 to 3.9, then the reproduction of the committed files as in run 3: the three changed inputs put back in their state of commit `4215a8f` with a read-only `git archive` (Section 6.4), `python-check-report.json` deleted, `DIRAC16KS_NB_OUTPUT` set to a folder outside the clone | clone (0, 19.3 s); Section 3.7 (0, 9.2 s); build (0, 22.6 s); `python -m venv` (0, 17.6 s); pip (0, 159.9 s); route C with the default path (1, 150.2 s); route A into a folder outside the clone (0, 84.4 s); audit of both into the committed report path (1, 1.2 s); the gate's comparison of the fresh with the committed report (1, 0.2 s) | gauntlet 56 PASS, 3 FAIL, 1 SKIP and audit 74 checks, 6 false, exactly as committed; the gate's comparison printed `stage4_notebook_report=equal to the committed report except the notebook paths: 2 executions, gauntlet 56/60, 14 figures with the committed sha256` (its exit code 1 only reflects the verdict `FAILURE`). The session limit stopped the work before this result was written down; after the restart the three files that the run had written, still in its clone, were checked: they have exactly the committed SHA-256 (`7efa2270...`, `92822f28...`, `b5bf9db2...`) |
| 10 | 2026-10-07 (evening, after the restart). Fresh clone of `b8a695d` in a scratch folder (repository path 154 characters), the Windows commands of Sections 3.6 to 3.11 and 5.6 run exactly as written by a Windows PowerShell 5.1 script, a fresh environment of Section 3.9 | clone (0, 18.5 s); Section 3.7 (0, 8.2 s); build (0, 19.0 s); `print-config` (0, 0.2 s); `python -m venv` (0, 11.5 s); pip (0, 159.9 s); `pip check` (0, 9.3 s); unit tests first, on the untouched clone (1, 42.2 s); audit of the committed notebook (1, 13.9 s); builder without execution (0, 3.0 s); route A without `--allow-errors` (1, 196.7 s; its folder created empty); route A (0, 115.1 s); route A with `jupyter.exe nbconvert` into another folder (0, 129.0 s); route B (1, 85.4 s); route C (1, 105.8 s); route D (1, 11.0 s); the gate's comparison step 28 (1, 0.4 s); unit tests after the routes (1, 13.7 s) and after Section 5.6 (1, 10.9 s); recording of the files read (87.7 s); Section 5.6 again | gauntlet 58/2/0 in every route with the 62 lines of Section 4.1 character for character; route B printed the 343 lines of Section 4.1; audit 74 checks, 4 false, verdict FAILURE; route-C copy `2bd96fe9...` and report `152cd743...`, the same bytes as in runs 1, 5, 7 and 8; `git status --porcelain` printed only the `rust_vs_reference.png` line and, after Section 5.6, nothing |
| 11 | 2026-10-07 (evening). Fresh clone of `603f150` next to run 10, the same steps run by a PowerShell 7.6.6 script, with `TEMP`, `TMP` and `IPYTHONDIR` pointing at empty private folders (Section 6.1) | clone (0, 16.5 s); Section 3.7 (0, 7.3 s); build (0, 18.0 s); `python -m venv` (0, 10.7 s); pip (0, 87.8 s); `pip check` (0, 2.3 s); unit tests first (1, 8.9 s); audit of the committed notebook (1, 2.6 s); builder without execution (0, 0.5 s); route A without `--allow-errors` (1, 95.2 s; folder created empty); route A (0, 93.8 s); `jupyter.exe nbconvert` (0, 108.4 s); route B (1, 85.7 s); route C (1, 115.2 s); route D (1, 5.4 s); step 28 (1, 0.6 s); unit tests after the routes (1, 10.5 s) and after Section 5.6 (1, 5.3 s); recording of the files read (60.5 s); Section 5.6 again | every output and the list of files read identical to run 10; every printed line identical to run 10 apart from the clone's folder name, the number of bytes printed by `jupyter.exe nbconvert` and the durations printed by the unit tests (Section 6.4); the private temporary folder still empty at the end; the new IPython profile of Section 5.2 |
| 12 | 2026-10-07 (evening) and 2026-10-08 (morning). Fresh clone of `b8a695d`, Ubuntu 24.04 (WSL2) bash with a clean `PATH`, the macOS and Linux commands of Sections 3.6 to 3.11 and 5.6 run as written by a bash script (the three build commands of Section 3.8 as one `bash -c 'cd studies/dirac16complex_kohn_sham && cargo build --release'`); the clone lay on the Windows disk (a scratch folder reached as `/mnt/c/...`), which makes every file operation slow | clone (0, 439.2 s); `bash scripts/setup_solver.sh win11` (0, 58.2 s); build (0, 20.8 s); `python3 -m venv` (0, 74.1 s); pip (0, 913.0 s); `pip check` (0, 10.5 s); unit tests first (1, 8.8 s); route A (0, 137.1 s); route B was interrupted after 131 printed lines, because the Linux virtual machine stopped while the test session was paused overnight. Resumed on 2026-10-08 in the same clone: the figures restored (Section 5.6), then route A (0, 124.0 s); route B (1, 84.8 s); route C (1, 107.7 s); route D (1, 4.7 s); Section 5.6 (0, 0.2 s); unit tests (1, 6.7 s) | gauntlet 58/2/0 with exactly the 62 lines of Section 4.1, in routes A, B and C; route B printed 343 lines, identical to the Windows ones except the program name without `.exe`, `/` instead of `\`, the 14 figure SHA-256 lines and one round-off digit (`columns 2.21e-16` instead of `2.22e-16`); the 15 spectrum files byte-identical to the committed ones after every route; audit 74 checks, 4 false, verdict FAILURE; the route-C copy `59e63aa4...`, the same bytes as in run 6 of 2026-10-02; all 14 figures with other bytes than on Windows (so `git status --porcelain` listed all 14, and after Section 5.6 nothing) but identical pixel for pixel to the Windows ones (13 compared with the committed files, `rust_vs_reference.png` with the copy embedded in the Windows route-C notebook of run 10); `rust_vs_reference.png` = `50e30d16...`, the bytes of run 6; 30 unit tests, 26 pass, 4 fail |
| 13 | 2026-10-07 (evening). Fresh clone of `603f150`, Windows PowerShell 5.1 scripts, setup of Sections 3.6 to 3.9, then the reproduction of the committed files as in runs 3 and 9 (three changed inputs put back with a read-only `git archive` of commit `4215a8f`, `python-check-report.json` deleted, `DIRAC16KS_NB_OUTPUT` set to a folder outside the clone), done three times in a row in the same clone | clone (0, 24.3 s); Section 3.7 (0, 9.1 s); build (0, 18.7 s); `python -m venv` (0, 13.3 s); pip (0, 107.4 s); `pip check` (0, 3.4 s); third pass: putting back the inputs (0, 0.6 s), route C with the default path (1, 69.0 s), route A into a folder outside the clone (0, 66.7 s), audit of both into the committed report path (1, 1.4 s), the gate's comparison of the fresh with the committed report and notebook (1, 0.1 s). The first two passes printed the same lines (only the number of bytes that `nbconvert` prints differed: 1858090, 1858187 and 1858187) and took about as long (route C 67 s, route A 65 s in the first pass); their exit codes were not recorded, because a log watcher of the test harness held the step-summary file open | gauntlet 56 PASS, 3 FAIL, 1 SKIP and audit 74 checks, 6 false, exactly as committed; after every pass `notebooks/dirac16complex_kohn_sham.ipynb`, `notebook-report.json` and `rust_vs_reference.png` had exactly the committed SHA-256 (`7efa2270...`, `92822f28...`, `b5bf9db2...`), so `git status --porcelain` listed only the nine files that had been put back or deleted before the run; the gate's comparison printed `stage4_notebook_report=equal to the committed report except the notebook paths: 2 executions, gauntlet 56/60, 14 figures with the committed sha256` and `stage4_notebook_executed_copy_byte_identical_to_committed=yes` (exit code 1 only because the verdict is `FAILURE`) |
| 14 | 2026-10-08 (morning). Fresh clone of `477fa9b` (repository path 144 characters), Windows, the commands of Sections 3.7 to 3.10, steps 4 to 6 of Section 3.11 and Section 5.6 run one by one from PowerShell 7.6.6 and Git Bash, a fresh environment of Section 3.9 (`pip freeze`: 99 packages, the versions of runs 10 and 11), `PYTHONDONTWRITEBYTECODE` removed; `scripts/__pycache__/` and `notebooks/__pycache__/` deleted before each step, to see which step creates them | clone (0); Section 3.7 (0, 5.4 s); build (0, 7.2 s); `python -m venv` (0, 5.6 s); pip (0, 54.4 s); route A (0, 65.7 s); route B under an audit hook that recorded every file opened (1, 52 s); route B (1, 115.1 s); route C (1, 73.8 s); route D (1, 1.4 s); Section 5.6, then the unit tests (1, 4.9 s); route E with the command of Section 3.10 (see below) | gauntlet 58/2/0, route B 343 lines with the 62 gauntlet lines of Section 4.1 character for character and the empty line before its `FAIL` line; route-C copy `2bd96fe9...`, report `152cd743...`, route-A copy 1866659 bytes and 3987 lines, normalised `8836527c...` (the program of Section 6.2); 30 unit tests, 26 pass, 4 fail; `scripts/__pycache__/` created by routes A, B and C, `notebooks/__pycache__/` only by route D and the unit tests, `tests/__pycache__/` by the unit tests (Section 5.1); the files read and written of Section 2.3; the PowerShell commands of Section 3.11, steps 5 and 6, give the same lines in Windows PowerShell 5.1 and PowerShell 7.6 |

Route E (run 5) was tested with `python -m jupyterlab --no-browser` and the server bound to 127.0.0.1 without a token, the notebook opened in a browser window at `http://127.0.0.1:8893/lab/tree/notebooks/dirac16complex_kohn_sham.ipynb`, the menu Run, Run All Cells chosen, and JupyterLab shut down through File, Shut Down. All 18 code cells were executed (execution counts 1 to 18), the gauntlet printed 60 lines, 58 passed, 2 failed, and the cell ended with the same `AssertionError`. JupyterLab saved the notebook automatically 2 minutes after the run started, so `git status --porcelain` then listed ` M notebooks/dirac16complex_kohn_sham.ipynb` as well; it also created `notebooks/.ipynb_checkpoints/`, updated `%APPDATA%\jupyter\nbsignatures.db` and `%USERPROFILE%\.jupyter\lab\workspaces\default-37a8.jupyterlab-workspace`, and removed its runtime files when it was shut down. The interactive clicking itself was done by an automated browser, not by hand. Route E was repeated in run 8 on 2026-10-07 in the same way (server on 127.0.0.1, port 8893, started with `python -m jupyterlab --no-browser --ServerApp.ip=127.0.0.1 --ServerApp.port=8893 --IdentityProvider.token=` from the repository root). The menu items of Run are greyed out until you have clicked into the notebook, which is why Section 3.10 says to click into it first. After Run, Run All Cells the kernel was busy for about 100 seconds on the busy machine; JupyterLab saved the notebook by itself twice, two minutes apart (once during the run and once 44 seconds after it), and the saved notebook had execution counts 1 to 18, the 62 gauntlet lines of Section 4.1 character for character and the same `AssertionError`; `git status --porcelain` listed the notebook and `rust_vs_reference.png`, `notebooks/.ipynb_checkpoints/` was created, File, Shut Down (with its confirmation) stopped the kernel and the server and removed its runtime files, and Section 5.6 restored the committed state (`git status --porcelain` then printed nothing).

Runs 5 and 8 started JupyterLab **without** naming the notebook, so it served the repository root and the notebook lay at `/lab/tree/notebooks/dirac16complex_kohn_sham.ipynb`. The command of Section 3.10 names the notebook, and JupyterLab then serves the folder `notebooks` instead. This was checked on 2026-10-08 (run 14) with exactly that command plus `--no-browser --ServerApp.ip=127.0.0.1 --ServerApp.port=8899 --IdentityProvider.token=`, started from the repository root: the server printed `Serving notebooks from local directory: ...\Dirac_claude\notebooks`; its file browser listed the files of `notebooks/`; the address `/lab/tree/dirac16complex_kohn_sham.ipynb` opened the notebook with the kernel `Python 3 (ipykernel)` (session path `dirac16complex_kohn_sham.ipynb`); a request for the path of runs 5 and 8 was answered with `404 ... No such file or directory: notebooks/dirac16complex_kohn_sham.ipynb`; the runtime folder held `jpserver-<id>.json`, `jpserver-<id>-open.html` and `jpserver-file-to-run-<id>-open.html` (its link points at `/lab/tree/dirac16complex_kohn_sham.ipynb`); and `notebooks/.ipynb_checkpoints/` was created as soon as the notebook was opened. The cells were not executed in that session of run 14 (the automated browser used for it could not operate JupyterLab's menus); the server was stopped through its shutdown request `/api/shutdown` (the request that File, Shut Down sends), which removed the three runtime files. The independent verification of this file executed the cells with the same command on 2026-10-08 in its own fresh clone: Run, Run All Cells gave execution counts 1 to 18 and the same gauntlet lines and `AssertionError` as in Section 4.1, the run took about 55 seconds, JupyterLab saved the notebook automatically about two minutes after it had been opened and created `notebooks/.ipynb_checkpoints/`, and File, Shut Down removed all runtime files.

Details of runs 7 and 8 (2026-10-07). The audit of the committed notebook as it is (`python notebooks/check_dirac16complex_kohn_sham_notebook.py notebooks/dirac16complex_kohn_sham.ipynb --report build/committed-reaudit.json`) printed 73 checks, 6 false, verdict `FAILURE`, with the committed gauntlet (56 PASS, 3 FAIL, 1 SKIP) and `check_r12_cells_match_builder=true`: the committed cells are still exactly the builder's. The builder without `--execute` wrote `build/fresh/dirac16complex_kohn_sham.ipynb` (`eb46e836ae2bf27e837b2c645554c78bd644f96916390bab31aac63ad85f2fb6`) in both runs. The gate's comparison step 28 (`python scripts/verify_stage4_kohn_sham_audit.py notebook --committed-report artifacts/dirac16complex/kohn-sham/notebook-report.json --fresh-report build/notebook-report.json --committed-notebook notebooks/dirac16complex_kohn_sham.ipynb --fresh-notebook build/nbclient/dirac16complex_kohn_sham.ipynb`) printed `stage4_notebook_executed_copy_byte_identical_to_committed=no`, `stage4_audit_problem=build/notebook-report.json verdict is 'FAILURE'`, `stage4_audit_problem=build/notebook-report.json differs from artifacts/dirac16complex/kohn-sham/notebook-report.json in ['checks', 'executions', 'failed', 'failedCheckCount', 'figures', 'gauntlet', 'measurements', 'sourceSha256']` and `stage4_audit_notebook=FAILED` (exit code 1), which is open discrepancy 2 of Section 6.6 seen through the gate's eyes. The unit tests gave 26 passed and 4 failed on the untouched clone and after Section 5.6 (the four tests of Section 6.5), but 25 passed and 5 failed right after the routes, because the fifth test, `test_figures_listed_are_the_files_on_disk`, compares the committed report with the figure files on disk, and a run rewrites `rust_vs_reference.png`; this is why Section 5.5 says to restore the figures before running the unit tests.

### 6.4 Byte identity of every output

The table gives the runs of 2026-10-02; the paragraphs below it add the runs of 2026-10-07 and 2026-10-08, which gave the same bytes for the spectrum files, the figures, the route-C copy (Windows and Linux), the report written with the paths of Section 3.10 and the printed output (the experiment of run 2 with another IPython version and the report written with the paths of run 1 were not repeated).

| Output | Two runs compared with each other | Compared with the committed file |
|---|---|---|
| 15 files of the `spectrum` re-run (`build/notebook-kohn-sham/spectrum/`) | identical (runs 1, 2, 5, 6 on Linux) | **identical** (15 of 15) in every run and every route |
| 13 of the 14 figures | identical (runs 1, 2, 5; run 6 on Linux: identical pixels, other bytes) | **identical** in every run on Windows; on Linux (run 6) identical pixels, other bytes |
| `rust_vs_reference.png` | identical (`8d572f57621fc606df53454475caf9c24d63c61cfa616c192caddc3c2a1607b7`, 74124 bytes; runs 1, 2, 5; run 6 on Linux: identical pixels, other bytes, `50e30d16bdb8e0d20f8f6a85d8400369eea52994ed27f5b90b2ca80d5833265a`) | different (committed `b5bf9db23a8430af804d1270e74020aac4a4d18e80acfdde1d5465ca1f4e076b`); reproduced byte for byte in run 3 |
| executed notebook written by the builder's `--execute` (route C) | identical, runs 1 and 5 (`2bd96fe94a5478003620bf071ac9daf2bf0e68555236e556f336b6878505a4d8`); run 2 differs only in one line of the traceback of the final `AssertionError` (IPython 9.17.1 shows code line 368 as an extra context line); run 6 on Linux (`59e63aa4d3f64e748a282354d7cfd79515d5a141eb7fc1fe98d1221a20ba910e`) differs from run 1 in 31 lines: the recorded Python version (3.12.3), the program name without `.exe`, the 14 figure SHA-256 lines and embedded figures, and the last digit of one printed round-off number of cell 7; its gauntlet text and error output are identical | different from the committed `7efa2270...` in 19 lines (explained below): `diff` finds 17 places where 19 lines of the committed file are replaced by 19 new lines, and prints these as 38 changed lines; compared position by position 21 lines differ, because one place shifts a line (counted again in run 14); reproduced byte for byte in run 3 |
| executed copy of route A (`nbconvert`) | not byte-identical by design (time stamps); after the normalisation of Section 6.2 identical in runs 1 and 5 (both launchers), run 2 differs only in the same traceback line | (no committed copy) |
| `notebook-report.json` | identical, runs 1 and 2 (`c6708242501884d71fa5909eca188ff3c8604308d2dd3b5ae484e21340ce4876`, written to the committed path with the paths of run 1); run 5 (paths of Section 3.10) `152cd74397b16e88ed33489dac7ac31814ec8ee14f173f234cbe9444a5cea979` | different from the committed `92822f28...`; reproduced byte for byte in run 3 |
| printed output of route B (343 lines) and of the audit | identical, runs 1 and 2 | (not committed) |

**Runs 7 and 8 (2026-10-07), compared with each other and with the runs of 2026-10-02.** Nothing was normalised except the `nbconvert` copies (Section 6.2). In both runs and after every route: the 15 spectrum files byte-identical to the committed ones (and to each other); 13 figures byte-identical to the committed ones, and `rust_vs_reference.png` = `8d572f57621fc606df53454475caf9c24d63c61cfa616c192caddc3c2a1607b7` (74124 bytes), the bytes of runs 1, 2 and 5. The route-C copy `2bd96fe94a5478003620bf071ac9daf2bf0e68555236e556f336b6878505a4d8` (3759 lines, 1856513 bytes) in both runs, the same bytes as runs 1 and 5. The route-D report `152cd74397b16e88ed33489dac7ac31814ec8ee14f173f234cbe9444a5cea979` (655 lines, 30594 bytes) in both runs, the same bytes as run 5. The re-audit report of the committed notebook (`fae981229a97ba4ed055558ead4f30228ae16d52278af3739294f1c3e8a6d674`) and the un-executed build (`eb46e836...`) identical in both runs. The `nbconvert` copies: raw bytes different in every run (time stamps), after the normalisation identical between the two runs and between the two launchers (`python -m nbconvert` and `jupyter.exe nbconvert`; normalised SHA-256 `8836527c2018ffa1b48ea583719ae5a52c2d4458a78fb8fb4a4c319032de70de`). The printed output of routes B, C and D, of the strict route A, of the builder, of the re-audit and of step 28 identical between the two runs (after removing the lines that contain the clone's folder name). The list of the files read (Section 2.5) identical in both runs and to the list of 2026-10-02. Compared with the committed files: the same three differences as on 2026-10-02 (executed notebook in 19 lines, report, `rust_vs_reference.png`), for the reasons explained in the next paragraph; nothing else.

**Runs 10 and 11 (the evening of 2026-10-07, after the restart), compared with each other and with the earlier runs.** Again nothing was normalised except the `nbconvert` copies, and the results are those of runs 7 and 8, byte for byte. After every route of both runs (the route A without `--allow-errors`, route A with both launchers, B and C): the 15 spectrum files byte-identical to the committed ones and between the runs; 13 figures byte-identical to the committed ones, `rust_vs_reference.png` = `8d572f57...` (74124 bytes); the figure hashes identical between the runs after every route. Identical between the two runs and equal to the values of runs 7 and 8: the route-C copy `2bd96fe9...` (3759 lines, 1856513 bytes), the route-D report `152cd743...` (655 lines, 30594 bytes), the re-audit report of the committed notebook `fae98122...` (640 lines, 29975 bytes), the un-executed build `eb46e836...` (3133 lines, 198975 bytes), the normalised `nbconvert` copies of both launchers `8836527c...` (raw: 1866659 bytes and 3987 lines with Windows line endings, different bytes in every run because of the time stamps), and the list of the files read (Section 2.5, `c2e956ee...`). The printed output of every route, of the audit, of the gate's step 28, of the builder and of the re-audit was identical between the two runs after removing the lines that contain the clone's folder name (route B: 343 lines, byte for byte); the only other differences were the number of bytes that `jupyter.exe nbconvert` prints (1862769 and 1862672) and the durations that the unit tests print.

**Run 12 (Linux, 2026-10-07 and 2026-10-08).** The same results as run 6 of 2026-10-02, byte for byte where bytes were compared: the route-C copy `59e63aa4d3f64e748a282354d7cfd79515d5a141eb7fc1fe98d1221a20ba910e` (3759 lines, 1992757 bytes) and `rust_vs_reference.png` = `50e30d16...` are the bytes of run 6; the 15 spectrum files are byte-identical to the committed ones after every route; the gauntlet text of routes A, B and C is identical to the Windows one; the 14 figures are identical pixel for pixel to the Windows figures but have other bytes (`zlib` 1.3 against 1.3.1.zlib-ng), and with them the figure lines of the printed output, the embedded figures of the executed copies and the report (`2623132a...`, 655 lines, 30594 bytes, with the paths of Section 3.10). The `nbconvert` copy on Linux has plain line feeds (1998916 bytes, 3987 lines; `nbconvert` printed `Writing 1999003 bytes` and `Writing 1998916 bytes` in the two executions of route A).

**Why the executed notebook, the report and `rust_vs_reference.png` differ from the committed files.** The committed copies were made on 2026-09-30: the notebook and the report were last changed in commit `4215a8f` (08:44), the figure `rust_vs_reference.png` in the earlier commit `faf108d` (08:35) of the same day (`git log -1` of each file). Since then three inputs of the notebook changed: the reference-solver run `m1_L3_N1016_lamm2_T0` and `reference/reference-summary.json` were recomputed on finer grids (six files in `artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0/` and the summary; erratum E4.13 of the Stage-4 specification), `scripts/ks_reference_solver.py` changed, and `artifacts/dirac16complex/kohn-sham/python-check-report.json` was committed for the first time (it was absent before). The committed execution also had the environment variable `DIRAC16KS_NB_OUTPUT` set. A fresh run therefore prints, compared with the committed notebook: `cross-check report present` instead of `absent`; `fresh runs : build/notebook-kohn-sham` instead of `DIRAC16KS_NB_OUTPUT`; the comparison lines `canonical_deltaSCF` and `canonical_particleHole` now `agree` (they were `DIFFER`) and `canonical_eigenvalues` still `DIFFER` but with other numbers (worst 2.195e-06, ratio 2.08, at `scf/m1_L3_N1016_lamm2_T0`, instead of 1.541e-06, ratio 1.46, at `excited/m1_L3_N1016_lamm2_T0_g601`); a different figure `rust_vs_reference.png`; and the gauntlet `58 passed, 2 failed, 0 skipped` instead of the committed `56 passed, 3 failed, 1 skipped` (the committed failures `rust_vs_reference_deltaSCF` and `rust_vs_reference_particleHole` now pass, `rust_vs_reference_eigenvalues` still fails, and `python_check_report` changed from SKIP to FAIL). Run 3 proved that nothing else changed: in a fresh clone, the reference folder and `scripts/ks_reference_solver.py` were restored to their state of commit `4215a8f` (`git checkout 4215a8f -- artifacts/dirac16complex/kohn-sham/reference scripts/ks_reference_solver.py`), `python-check-report.json` was deleted and `DIRAC16KS_NB_OUTPUT` was set; then route C with the default path, route A and the audit (into the committed report path) reproduced `notebooks/dirac16complex_kohn_sham.ipynb` (`7efa2270...`), `artifacts/dirac16complex/kohn-sham/notebook-report.json` (`92822f28...`) and `rust_vs_reference.png` (`b5bf9db2...`) **byte for byte**, and the Stage-4 gate's own comparison (`scripts/verify_stage4_kohn_sham_audit.py notebook`) printed `equal to the committed report except the notebook paths: 2 executions, gauntlet 56/60, 14 figures with the committed sha256` and `stage4_notebook_executed_copy_byte_identical_to_committed=yes`. Runs 9 (afternoon of 2026-10-07) and 13 (evening, three passes) repeated this reproduction in new fresh clones with the same result, putting the inputs back with the read-only command `git archive 4215a8f artifacts/dirac16complex/kohn-sham/reference scripts/ks_reference_solver.py | tar -x -f -` instead of `git checkout`. The program's own sources also changed after `4215a8f` (before `c2b33cc`: a new `pairs` subcommand in the new file `src/pairs.rs` and edits of seven other files of `studies/dirac16complex_kohn_sham/src/`), but the reproductions used the program built from the current sources, so these changes alter neither its configuration lines nor its `spectrum` files.

### 6.5 Check counts

- **Gauntlet** (cell 18): 60 checks; 58 PASS, 2 FAIL (`rust_vs_reference_eigenvalues`, `python_check_report`), 0 SKIP; identical in every route and run on Windows and on Linux, on 2026-10-02 and again on 2026-10-07 and 2026-10-08 (runs 7, 8, 10, 11, 12 and 14). (Committed copy: 56 PASS, 3 FAIL, 1 SKIP, which the reproduction runs 3, 9 and 13 obtain again with the inputs of 2026-09-30.)
- **Audit** (route D): 74 checks, 70 true, 4 false (`check_r07_no_error_outputs`, `check_r07_gauntlet_passed`, `check_gauntlet_rust_vs_reference_eigenvalues`, `check_gauntlet_python_check_report`), verdict `FAILURE`; the rule checks r01 to r06 and r08 to r12 are true, in particular `r12_cells_match_builder` (the committed notebook has exactly the cells the builder writes today) and `cross_execution_identical`; the same in runs 7, 8, 10, 11, 12 and 14 (in run 14 the report has the bytes `152cd743...` of runs 5, 7, 8, 10 and 11). (Committed report: 74 checks, 68 true, 6 false; the same in the reproduction runs 3, 9 and 13.) The audit of the committed notebook alone (runs 7, 8, 10 and 11) gives 73 checks, 6 false, verdict `FAILURE`, with `check_r12_cells_match_builder=true`.
- **Unit tests** (`python -m unittest discover -s tests -p "test_d16c_kohn_sham_notebook.py" -v`, runs 1 and 2, on 2026-10-07 runs 7, 8, 10 and 11, and on 2026-10-08 run 14, on a clone without rewritten figures): 30 tests, 26 pass, 4 fail, exit code 1 (right after a route, with `rust_vs_reference.png` rewritten, 25 pass and 5 fail; Section 6.3). The 4 failures all concern the committed report and repeat Section 6.4: `test_report_is_current` (the report records the SHA-256 `f6247add...` of the old `reference-summary.json`), `test_reaudit_of_the_committed_notebook_reproduces_the_first_execution` (the same SHA-256, and `python-check-report.json` recorded as absent), `test_verdict_success` (verdict `FAILURE`), `test_two_executions_with_identical_results` (the test expects the first execution to be made by `run_notebook.py`, but the runner never writes a failing notebook back, so the committed copy was made by the builder's `--execute`). The 13 auditor tests, the 10 builder tests and the other 3 tests of the committed report pass, among them the byte identity of two builds from different working folders.

### 6.6 Fixes and open discrepancies

- **Fixes made:** none, on 2026-10-02 and on 2026-10-07. No file of the set was changed. No execution defect was found: every route executes every cell. The one failed build (run 4) was caused by the length of the test folder, not by the repository; the instructions of Section 3.6 avoid it. The only change made on 2026-10-07 is to this provenance file (the re-test record, sizes and times, and the corrections of Sections 4.1 and 4.3 about the size that `nbconvert` prints). The evening runs 10 to 13 found no execution defect either, and again only this file was changed. On 2026-10-08 (run 14) again only this file was changed; the notebook, its programs and its committed outputs belong to old Stage 4, which is paused, and were left as they are.
- **Corrections of 2026-10-08 (after an independent verification of this file; each re-checked in run 14 before it was written):** (1) route E: the command of Section 3.10 makes JupyterLab serve `notebooks/` and open the notebook at `/lab/tree/dirac16complex_kohn_sham.ipynb`, which runs 5 and 8 (started without the notebook path) had not tested; Sections 3.10, 5.2 (the runtime file `jpserver-file-to-run-<id>-open.html`) and 6.3 now say so; (2) Section 3.11, steps 5 and 6: the PowerShell command `Format-Table -AutoSize Hash, Path` cut the file names off in a window 120 characters wide and was replaced by one that prints the SHA-256 in small letters and the file name; (3) Section 5.1: `scripts/__pycache__/` is created by every execution (routes A, B, C, E), `notebooks/__pycache__/` only by route D and the unit tests (the old row said "B, C, D" for both), and Sections 2.3 and 5.2 add that a first execution also writes the two bytecode files; (4) Section 2.3: the 459 files are the committed inputs; the process also re-reads the 14 figures, the 15 fresh spectrum files and its bytecode cache (492 files in all in run 14); (5) Section 6.4: the route-C copy differs from the committed notebook in 19 lines, not 38 (38 was the count of `diff`'s `<` and `>` lines); (6) Section 6.2: the normalised SHA-256 `8836527c...` is now reproducible with the program given there; (7) Sections 3.1 and 6.1: macOS was never tested, and the `+fma` flag is not a known feature on Apple processors; (8) Section 6.4: `rust_vs_reference.png` was last changed in commit `faf108d`, not `4215a8f`; (9) Section 4.1: route B prints an empty line before its `FAIL` line.
- **Corrections of the afternoon record (made in the evening of 2026-10-07):** the version of this file written in the afternoon said in its summary that runs 7 to 9 used three clones, "two on Windows, one on Linux", and gave commit `935ac73` for run 9. The logs of that afternoon show otherwise: the Linux run was stopped by the session limit before its packages were installed and has no result, and run 9 was the reproduction run on Windows at commit `c65bb82` (Section 6.3). Both statements were corrected, and the Linux route was run again in the evening (run 12).
- **Open discrepancy 1 (scientific, reported, not fixed):** the gauntlet check `rust_vs_reference_eigenvalues` fails: 2.195e-06 against the tolerance 1.054e-06 for two deep Dirac-sea levels at k = 0 of the 301-point Rust run `m1_L3_N1016_lamm2_T0`. The same failure is the one failed check `canonical_eigenvalues` of the committed cross-check report, which makes the gauntlet check `python_check_report` fail as well. The repository's textbook (`provenance/DIRAC16COMPLEX_TEXTBOOK.md`, claim L34 and Section 13.15) records it as open: the 601-point run of the same state agrees with the reference solver to 1.8e-07, and a grid error of the 301-point run is a hypothesis that has not been tested. The tolerance was not changed. **Update of 2026-10-08 afternoon:** the hypothesis was tested and the cause fixed in the programs (next item).
- **Fixes of 2026-10-08 afternoon (stage4-fix; erratum E4.14 of `handoff/specs/STAGE4_SPEC.md`).** (1) The diagnosis ran the Rust `excited` run `m1_L3_N1016_lamm2_T0` at 301, 601 and 1201 points in a scratch copy: the deep level deviates from the N0 = 120 reference by 2.195e-06, 1.83e-07 and 2.6e-08 (measured order 3.27), so the Rust levels converge to the reference and neither program is wrong; the eigenvalue tolerance lacked the measured Rust grid uncertainty that rule E4.12 already gave to E_0, mu, the gap, Delta-SCF and the particle-hole energies. `compare_canonical` now adds, level by level, |eps(601) - eps(301)| of the same level (for the run with a 601-point partner and for the `scf` run whose `levels.csv` is byte-identical to that partner's base run); four new unit tests, among them two negative controls (the uncertainty of another level does not count; an error of 1e-4 is still detected). This is not a wider fixed tolerance: a level without a measured partner keeps the old tolerance. (2) A real error of the reference solver was found on the way: its Delta-SCF used the occupations of the finest grid on all three grids, which for the smeared run leaves a bias of about +4.4e-07 in Delta-SCF; it now uses each grid's own occupations, as the Rust program does (integer-occupation runs are bit-identical; three new unit tests). The committed reference run `m1_L3_N1016_lamm2_T0` predates this rule, and `ks_reference_solver.py --resume` now recomputes exactly that run (about 4.5 hours; 16179.7 s measured on 2026-09-30); against the committed run the Delta-SCF check passes with ratio 0.79. (3) Verification in a scratch copy of the repository with the fixed programs (nothing of it committed): `python scripts/check_dirac16complex_kohn_sham.py --repeat <repeat> --refined <refined> --report <scratch>` (199.6 s) gave 63 checks, 0 failed (`canonical_eigenvalues` worst 2.195e-06 against the tolerance 3.066e-06, ratio 0.716; `canonical_deltaSCF` 0.79; `canonical_particleHole` 0.0134); route B with that report in place (exit code 0, 47 s) printed `gauntlet: 60 checks, 60 passed, 0 failed, 0 skipped` and the runner wrote the notebook back; ROUTE_A_AUDIT_RESULT. The builder without execution wrote cells identical to the committed notebook's (no quoted number changes). (4) Not done, and why: the refreshed outputs (python-check-report.json, the executed notebook, notebook-report.json, `rust_vs_reference.png`) were not copied into the repository, because they must be made after the reference rerun of (2), and because `tests/test_d16c_textbook_publication.py` (`test_stage4_cross_check_status_agrees_with_the_report`) requires the committed report to have 63 checks with 1 failed, as the preserved first-edition textbook (`provenance/DIRAC16COMPLEX_TEXTBOOK.*`, `provenance/textbook/`, not to be changed by the user's order of 2026-10-02) states; refreshing the report needs the user's decision on an erratum to that book or on that test. Until then the four unit tests of Section 6.5 still fail as described there.
- **Open discrepancy 2 (stale committed outputs, reported, not changed):** the committed `notebooks/dirac16complex_kohn_sham.ipynb`, `artifacts/dirac16complex/kohn-sham/notebook-report.json` and `artifacts/dirac16complex/kohn-sham/figures/rust_vs_reference.png` describe the inputs of 2026-09-30 (Section 6.4), and the four unit tests of Section 6.5 fail for that reason. Refreshing them (routes C, A and D with the committed paths) would still give the verdict `FAILURE` because of discrepancy 1.
- **Open decision for the owner of the repository:** `HANDOFF.md` records that old Stage 4 was paused unfinished when the revision (`Revision/kohn_sham/`) replaced it, and asks whether old Stage 4 is to be finished (discrepancy 1 resolved, then the three committed outputs refreshed) or formally marked as superseded. This verification records the state as it is and did neither.
- **Observations:** (a) with a different IPython version the error output of the last cell differs in its code context, hence the pinned versions of Section 3.9; (b) the builder's `--execute` asks `nbclient` to join all printed text of a cell, so in its copies (and in the committed notebook) text that a cell prints after a figure appears above the figure; (c) `nbconvert --allow-errors` returns exit code 0 even when cells fail; (d) the Rust program file is not byte-identical between clones (it contains the full folder names of its source files and of its debug-symbol file), while every file it writes is; (e) the figures are byte-reproducible on Windows only: Python and Pillow on Windows compress PNG files with `zlib` 1.3.1.zlib-ng, the Linux packages with the system `zlib` 1.3, so on Linux every figure has other bytes (5 to 11 percent larger) although all 14 are identical pixel for pixel to the Windows ones (checked by decoding both); the notebook's own checks are not affected (they compare each figure with the hash the same run printed); (f) on Linux one printed measurement of cell 7 differs in its last digit (`columns 2.21e-16` instead of `2.22e-16`, a round-off of the mathematical library); the gauntlet lines are identical; (g) section 2 of the notebook says that the committed copy was executed by the standard-library runner; run 3 shows that it was in fact made by the builder's `--execute` (the runner never writes back a notebook whose last cell fails), which is also what the committed report records (both executions `Jupyter kernel python3 through nbclient`). This is a sentence of the notebook's text, written by the builder; it was not changed (the builder and the notebook belong to the documented state); (h) on Windows `nbconvert` writes its copy with Windows line endings (carriage return and line feed), while the builder, the runner and the auditor write plain line feeds on every system; the number of bytes that `nbconvert` prints is therefore smaller than the file by one byte per line on Windows (found on 2026-10-07; the earlier text of Section 4.3 had given the printed number as the file size).
