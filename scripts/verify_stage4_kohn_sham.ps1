# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 4 gate (dirac16complex Kohn-Sham DFT in the primordial field).
# Twin of scripts/verify_stage4_kohn_sham.sh; the step list, the checks and
# the final line are the same.  Same pattern as the Stage 3 gate
# scripts/verify_stage3_dark_sector.ps1 (itself modelled on the
# verify_phase*.ps1 gates of https://github.com/once-ere/dirac,
# GPL-3.0-or-later).  The comparisons, and the launch of the Rust runs, are
# made by one program, scripts/verify_stage4_kohn_sham_audit.py, which both
# twins call, so that both apply exactly the same rules.
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1
# Started from Windows PowerShell 5.1 the gate re-runs itself under pwsh
# (PATH, else %ProgramFiles%\PowerShell\7\pwsh.exe) with the same arguments
# and exits with its exit code: scripts/run_logged.ps1 uses -Encoding
# utf8NoBOM, which Windows PowerShell 5.1 rejects.
#
# Options (the full gate uses none of them):
#   -DryRun          print every step with its expected wall time and command,
#                    run nothing; last line stage4_kohn_sham_verification=DRY-RUN
#   -Steps 03,04,..  run only the listed steps (two-digit numbers or full
#                    names; build/stage4 is kept unless step 00 is listed);
#                    the last line is then stage4_kohn_sham_verification=PARTIAL
#                    (exit 3), never OK
#   -RefinedThermo   also run "thermo --refined" in step 14 (adds about the
#                    canonical thermo time again, see TIMING) so that the
#                    refined tree is complete and the fresh determinism report
#                    must equal the committed one byte for byte
#   -SequentialRust  run the Rust processes of step 14 one after another
#                    instead of concurrently (same outputs, see TIMING)
#
# Needs: python (numpy, matplotlib, nbformat, nbclient, nbconvert,
# ipykernel), cargo with rustfmt and clippy, git, pdflatex (PATH or MiKTeX);
# wolframscript is optional: without it the two Wolfram steps (the exact
# theory verifier and the Mathematica notebook) are skipped with the message
# stage4_skipped_step=..., the sympy theory checker still compares with the
# committed kohn-sham-theory.json, and the line before the final line says
# which cross-checks were not run.  Every step runs through
# scripts/run_logged.ps1 with its log in build/logs/ (build/ is git-ignored;
# the gate deletes and recreates only build/stage4/); the Rust processes of
# step 14 write one log each, build/logs/stage4-14-rust-runs-<canonical|
# refined>-<subcommand>.log.  The gate stops at the first failing step and
# prints stage4_failed_step, stage4_failed_log and
# stage4_kohn_sham_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts.
# Never run two gates at once: both would delete and rewrite build/stage4.
#
# WHAT IS AND IS NOT RE-RUN
#   Re-run and compared byte for byte: the exact Wolfram theory verifier
#   (with wolframscript) and the sympy theory checker (their four files;
#   value by value at relative 1e-9 / absolute 1e-12 is also accepted, and
#   which rule matched is logged), the constants generator (generated.rs and
#   generator-report.json), the COMPLETE canonical Rust tree (all five
#   subcommands into build/stage4/run-a; every file listed by every committed
#   summary.json, and no other file; this is also the repeat-run determinism
#   check), the summary builder, the Jupyter notebook (twice: run_notebook.py
#   and nbconvert; its report must equal the committed one except the
#   notebook paths, its figures are rewritten byte for byte), the
#   Mathematica notebook (with wolframscript; its report modulo the
#   platform-specific engine.binary and its figures byte for byte), both
#   PDFs (verify mode of scripts/build_provenance_pdf.py: page count and
#   sha256 of the registered edition).
#   Re-run and compared within tolerances: the --refined Rust run of
#   spectrum, scf, excited and emt into build/stage4/refined (thermo only
#   with -RefinedThermo): compare_runs.py (energies relative 1e-7,
#   eigenvalues absolute 1e-7) and the cross-checker's
#   rust_refined_convergence.
#   Re-run in reduced form: the Python reference solver.  Its canonical run
#   (every run of reference-summary.json on the three grids N0, 2 N0, 4 N0,
#   N0 = 60, or 120 for m = 3; several hours with 8 to 12 worker processes)
#   is NOT repeated; the
#   gate runs "ks_reference_solver.py --quick" (its self-tests at N0 = 64
#   plus the reduced parameter set on the two quick grids N0 = 30, 60) into
#   build/stage4/reference-quick, and the cross-checker re-solves one
#   Rust scf parameter set (--max-reproductions 1: the first present of its
#   priority list, m1_L2_N8_lamp1_T0) with the reference solver on the
#   canonical grids at exactly the Rust lambda_hat, and runs its
#   stationarity (Hellmann-Feynman) identities with small self-consistent
#   reference runs.  The committed reference tree is compared with the
#   committed Rust tree (identical to run-a by step 15) run by run.
#   Not re-run at all: the canonical reference runs (see above) and,
#   without -RefinedThermo, thermo --refined (the committed
#   determinism-report.json then cannot be reproduced byte for byte; step 17
#   requires the same checks, all true, and the same repeat file count, and
#   prints the refined counts next to the committed ones).
#
# STEPS (expected wall time: TIMING below; -DryRun prints the same figures)
#   stage4-00-snapshot             copy the committed Stage-4 files into
#                                  build/stage4/snapshot
#   stage4-01-solver-setup         scripts/setup_solver.ps1 -Platform win11
#   stage4-02-solver-pin           the engine is exactly the pin, unmodified
#   stage4-03-theory-wolfram       wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls
#                                  build/stage4/theory/wolfram-kohn-sham-report.json
#                                  (writes kohn-sham-theory.json next to it)
#   stage4-04-theory-sympy         scripts/check_dirac16complex_kohn_sham_theory.py into
#                                  build/stage4/theory/ (it compares with the COMMITTED
#                                  kohn-sham-theory.json, whose path and sha256 its report
#                                  records; step 05 proves that the fresh Wolfram file is
#                                  identical to it)
#   stage4-05-theory-same          the four theory files equal the committed ones
#   stage4-06..08-constants        generate_dirac16complex_ks_constants.py --check; the
#                                  same generator into build/stage4/constants/; its
#                                  generated.rs and generator-report.json equal the
#                                  committed ones byte for byte
#   stage4-09..12-cargo            fmt --check; clippy --release --all-targets -D warnings;
#                                  test --release; build --release (from the repository
#                                  root so that .cargo/config.toml (+fma) applies)
#   stage4-13-print-config         the release binary answers print-config with SUCCESS
#   stage4-14-rust-runs            audit rust-run: the five subcommands --output
#                                  build/stage4/run-a and spectrum, scf, excited, emt
#                                  (+ thermo) --refined --output build/stage4/refined, as
#                                  concurrent processes (-SequentialRust: one after the
#                                  other); every process exits 0 with last line SUCCESS
#   stage4-15-rust-compare         every file listed by every committed summary.json is
#                                  byte-identical in build/stage4/run-a, no other file
#   stage4-16-determinism          tools/compare_runs.py --canonical (committed tree)
#                                  --repeat run-a --refined refined
#   stage4-17-determinism-audit    all checks true, same checks and repeat file count as
#                                  the committed determinism-report.json (byte identity
#                                  required with -RefinedThermo)
#   stage4-18-reference-quick      ks_reference_solver.py --quick into
#                                  build/stage4/reference-quick
#   stage4-19-reference-quick-audit  complete, self-tests present, every run converged
#   stage4-20-cross-check          check_dirac16complex_kohn_sham.py --rust (committed)
#                                  --repeat run-a --refined refined (reproduction and
#                                  stationarity runs of the reference solver) into
#                                  build/stage4/python-check-report.json
#   stage4-21-cross-check-audit    all checks true, the same check names and the same
#                                  comparisons not run as the committed
#                                  python-check-report.json
#   stage4-22/23-summary           build_kohn_sham_summary.py (committed inputs) into
#                                  build/stage4/kohn-sham-summary.json, byte-identical to
#                                  the committed kohn-sham-summary.json
#   stage4-24..28-notebook         a copy of notebooks/dirac16complex_kohn_sham.ipynb
#                                  without outputs is executed headless by
#                                  notebooks/run_notebook.py and by nbconvert, audited by
#                                  notebooks/check_dirac16complex_kohn_sham_notebook.py
#                                  (build/stage4/notebook-report.json), which must equal
#                                  the committed notebook-report.json except the paths
#   stage4-29-figures-unchanged    the notebook rewrote the committed figures byte for byte
#   stage4-30-mathematica-notebook wolframscript -file
#                                  scripts/verify_dirac16complex_ks_mathematica_notebook.wls
#                                  (skipped without wolframscript)
#   stage4-31-mathematica-unchanged mathematica-report.json (modulo engine.binary) and
#                                  figures/mathematica rewritten byte for byte
#   stage4-32/33-pdf-*             build_provenance_pdf.py (verify mode) for
#                                  DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md and, with
#                                  --developer-layout, DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE.md
#   stage4-34-committed-unchanged  every snapshotted committed file is byte-identical
#   stage4-35-unit-tests           python -m unittest discover -s tests
#                                  -p "test_d16c_kohn_sham*.py" -v
#   stage4-36-fresh-outputs        the gate's outputs were written during this run
# Only then does it print
#   stage4_kohn_sham_verification=OK
#
