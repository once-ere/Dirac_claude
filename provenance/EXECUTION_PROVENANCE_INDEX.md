# Execution provenance: index of every WolframScript and notebook set

Written 2026-10-08. This file lists every executable WolframScript file (`.wls`) and every Jupyter
notebook (`.ipynb`) of the repository, outside `vendor/`, `dirac-main/` (private, never committed) and
`build/` (scratch output, never committed). For each one it names the execution-provenance file that
tells a student how to run it from nothing, what it prints, what it writes, how long it takes, what it
changes on the computer, and how it was verified. The facts in the table are summaries; the numbers,
the commands and the measured evidence are in the provenance files themselves (the part named in the
column "latest record").

`tests/test_execution_provenance.py` checks this index mechanically on every run: every `.wls` and
`.ipynb` of the repository (with the exclusions above) is listed here; every provenance file named here
exists; and every provenance file names the CURRENT sha256 of each script of its row, so a script that
changes without a new verification record makes the test fail. With the environment variable
`EXECUTION_PROVENANCE_FULL=1` (and `wolframscript` on the PATH) it also re-runs the fast sets (marked
"fast" below) in the working tree and checks that each ends with exit code 0 and leaves every committed
file byte for byte unchanged.

Meaning of the columns:

* **checks**: the pass/fail checks the set computes, as recorded in its committed report (some sets
  have no checks of their own; then the column says what is compared instead).
* **byte identity**: whether two independent runs (in fresh clones) reproduced every committed output
  byte for byte.
* **run time**: as measured on the verification machine (24 logical processors, Windows 11, usually
  shared with other jobs); a slower or busier computer needs longer.
* **open discrepancies**: what the latest record leaves open. "none" means no failed check, no output
  that differs from the committed one and no known execution defect.

## 1. The Revision sets

| # | set | scripts | provenance file | latest record | checks | byte identity | run time | open discrepancies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | rev-algebra (fast) | `Revision/algebra/wolfram/verify_algebra.wls` | `Revision/algebra/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` | 6.4 (2026-10-07, `a4c5eda`), 6.5 (`b980c80`) | 45 of 45 | yes (`gammas.json`, `wolfram-algebra.json`) | about 4 to 9 s (part 4.4) | none |
| 2 | rev-theory | `Revision/theory/wolfram/verify_scope.wls`<br>`Revision/theory/wolfram/verify_field_theory.wls` | `Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` | 6.6 (2026-10-07) | 15 of 15 and 84 of 84 | yes | scope about 0.5 to 1 min; field theory about 17 min (quiet) to 45 min (busy) (part 4.4) | none |
| 3 | rev-a4 | `Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls` | `Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` | 6.3 (2026-10-08, the version on the author's T16, commit `e377368`), 6.4, 6.5 | 52 of 52 (the companion `check_field_equations_a4.py`: 63 of 63) | yes (`a4-equations.json`, `wolfram-a4-report.json`) | about 36 to 86 s (part 6.3) | none in the results; two remarks on failure paths (part 6.5: a missing `lovelock-tensors.json` gives six FAIL checks and exit code 1 instead of an `ERROR` line; when the report cannot be written, `a4-equations.json` has already been rewritten) |
| 4 | rev-pairing | `Revision/pairing/wolfram/verify_pairing.wls` | `Revision/pairing/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` | part 6 (2026-10-07) | 101 of 101 | yes | about 2 to 5 min (part 4.4) | none |
| 5 | rev-pairing-ks (fast) | `Revision/pairing/kohn_sham/wolfram/verify_t3.wls` | `Revision/pairing/kohn_sham/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` | 6.4 (2026-10-07) | 10 of 10 | yes | about 2 to 8 s, up to 14 s on a heavily loaded machine (part 4.4) | none |
| 6 | rev-ks-theory | `Revision/kohn_sham/theory/verify_ks_theory.wls` | `Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md` | 6.3 (2026-10-07), 6.4 (2026-10-08) | 46 of 46 (the companion `check_ks_theory.py`: 58 of 58) | yes | Wolfram about 40 to 85 s; companion about 75 to 165 s (part 4.4) | none (the 57/58 count-table mismatch was resolved by `dc6904e`, part 6.4) |
| 7 | rev-gkd-verification | `Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls` | `Revision/gkd_lovelock/verification/WOLFRAMSCRIPT_PROVENANCE.md` | 6.3 (2026-10-08) | 29 of 29 | yes (the report; only its `sourceSha256` line changed with the fix of 6.3) | about 1 to 4 min (68 to 135 s measured, part 4.4) | none |
| 8 | rev-gkd-notebook-reading | `Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls`<br>`Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls` | `Revision/gkd_lovelock/notebook_reading/WOLFRAMSCRIPT_PROVENANCE.md` | part 6 (2026-10-07) | no checks of its own; the printed counts (58 cells, 58 inputs, image {1372, 435}) are compared | yes (`notebook-input-cells.txt`, `notebook-in68-image.png`) | about 2 to 15 s per script; up to about 24 s on a fully loaded machine (part 4.4) | none |

## 2. The sets of the first edition (Stages 1 to 5)

| # | set | scripts | provenance file | latest record | checks | byte identity | run time | open discrepancies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | old-algebra (fast) | `scripts/verify_dirac16complex_algebra.wls` | `provenance/wolframscript/verify_dirac16complex_algebra.PROVENANCE.md` | part 6 (2026-10-07, `a4c5eda`, `b8a695d`) | 21 of 21 | yes | about 11 to 54 s, depending on the load (part 4.4) | none |
| 10 | old-geometry | `scripts/verify_dirac16complex_geometry.wls` | `provenance/wolframscript/verify_dirac16complex_geometry.PROVENANCE.md` | part 6 (2026-10-07) | 43 of 43 (and 295 measurements) | yes | about 5 to 10 min (301 to 615 s measured; part 4.3) | none |
| 11 | old-primordial | `scripts/verify_dirac16complex_primordial.wls` | `provenance/wolframscript/verify_dirac16complex_primordial.PROVENANCE.md` | part 6 (2026-10-07, `b8a695d`, after the fix of commit `b980c80`) | 126 of 126 | yes | about 1 to 2.5 min (part 4.3) | none in the set (part 6.4) |
| 12 | old-kohn-sham | `scripts/verify_dirac16complex_kohn_sham.wls` | `provenance/wolframscript/verify_dirac16complex_kohn_sham.PROVENANCE.md` | 6.3 (2026-10-07) | 125 of 125 | yes | about 13 to 34 s (part 4.4) | none |
| 13 | old-00 | `scripts/verify_dirac16complex00.wls` | `provenance/wolframscript/verify_dirac16complex00.PROVENANCE.md` | 6.6 (2026-10-07) | 46 of 46 (45 module checks) | yes | about 4 to 12 min (up to 714 s measured under load; part 4.3) | none |
| 14 | old-pairing | `scripts/verify_dirac16complex_pairing.wls` | `provenance/wolframscript/verify_dirac16complex_pairing.PROVENANCE.md` | 6.2 (2026-10-07), 6.4 (2026-10-07, evening) | 141 of 141 | yes | about 4 to 12 min (part 4.5) | none |
| 15 | old-matter-antimatter | `scripts/verify_dirac16complex_matter_antimatter.wls` | `provenance/wolframscript/verify_dirac16complex_matter_antimatter.PROVENANCE.md` | 6.7 (2026-10-07) | 44 of 44 | yes | about 7 to 8.5 min; about 13 min on a fully loaded machine (part 4.4) | none in the results (the Windows path-length limit of part 6.4 is an environment condition, documented) |
| 16 | old-nb-build-dark (fast) | `scripts/build_dirac16complex_mathematica_notebook.wls` | `provenance/wolframscript/build_dirac16complex_mathematica_notebook.PROVENANCE.md` | part 6 (2026-10-07) | no checks of its own; the built notebook is compared byte for byte with the committed one | yes | about 2 to 12 s (part 4.4) | none |
| 17 | old-nb-verify-dark | `scripts/verify_dirac16complex_mathematica_notebook.wls` | `provenance/wolframscript/verify_dirac16complex_mathematica_notebook.PROVENANCE.md` | part 6 (2026-10-07) | 49 of 49 notebook checks, 37 of 37 cells | yes (9 output files) | about 4 to 7 min; 8 to 12 min when busy (part 4.4) | none in the results |
| 18 | old-nb-build-ks (fast) | `scripts/build_dirac16complex_ks_mathematica_notebook.wls` | `provenance/wolframscript/build_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` | 6.6 (2026-10-07) | no checks of its own; the built notebook is compared byte for byte with the committed one | yes | about 5 to 11 s (part 4.4) | none |
| 19 | old-nb-verify-ks | `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` | `provenance/wolframscript/verify_dirac16complex_ks_mathematica_notebook.PROVENANCE.md` | 6.2 (2026-10-07), 6.3 (2026-10-08) | 94 of 94 notebook checks | yes (7 output files) | about 10 to 18 min (part 4.4) | none |
| 20 | nb-dark-sector | `notebooks/dirac16complex_dark_sector.ipynb` | `notebooks/dirac16complex_dark_sector.PROVENANCE.md` | 6.7 (2026-10-07) | the runner: 140 `PASS` lines (71 of them the gauntlet), 0 `FAIL`, `ALL CHECKS PASSED` | yes (the notebook, `notebook-report.json` and 17 figures) | see part 4.8 | none (part 6.8; the macOS and Linux routes were not run) |
| 21 | nb-kohn-sham | `notebooks/dirac16complex_kohn_sham.ipynb` | `notebooks/dirac16complex_kohn_sham.PROVENANCE.md` | see the file | see the file | see the file | about 1 to 2 min per execution; up to about 3.5 min on a fully loaded machine (part 4.4) | see the file (part 6.6) |

## 3. Early design probes and the Dirac-matrix proof

| # | set | scripts | provenance file | latest record | checks | byte identity | run time | open discrepancies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | handoff-probes (fast) | `handoff/tools/probe1.wls`<br>`handoff/tools/probe2.wls` | `handoff/tools/WOLFRAMSCRIPT_PROVENANCE.md` | 6.2 (2026-10-07), 6.3 | no checks; the printed lines are compared with part 4 | yes (printed output) | about 3 to 10 s each (part 4.5) | probe1's printed line 15 is garbled (operator precedence; part 4.3); the statement it was meant to show is true; the throw-away probe is kept unchanged on purpose, as a record |
| 23 | dirac-matrices (fast) | `provenance/dirac_matrices/extract_from_author_notebook.wls`<br>`provenance/dirac_matrices/extract_repository_wolfram_gammas.wls` | `provenance/dirac matrices.md` | its section "How to reproduce" (2026-10-08) | 67 of 67 exact checks (`build_dirac_matrices_md.py`) | yes (both JSON files and the Markdown file, `--check`) | 4 to 11 s and 6 to 16 s for the two extractions; 13 to 22 s for the builder | none ("Instruction followed: yes") |

## 4. The notebooks of the textbook "Universes in Pairs"

The 89 notebooks `Revision/textbook/notebooks/<name>.ipynb` are not listed one by one: each has its own
execution-provenance file `Revision/textbook/notebooks/<name>.PROVENANCE.md`, written by the notebook
tool from the builder `Revision/textbook/notebooks/src/<name>.py` (Revision/textbook/TEXTBOOK_SPEC.md,
rule R6). `python Revision/textbook/tools/nbkit.py check Revision/textbook/notebooks/src/<name>.py`
executes a notebook again in a scratch folder and compares the notebook, every file it writes and its
provenance file byte for byte; `Revision/tests/test_universes_in_pairs_textbook.py` checks the book.
`tests/test_execution_provenance.py` checks that every textbook notebook has its builder and its
provenance file.
