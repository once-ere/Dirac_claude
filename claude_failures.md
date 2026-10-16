# claude_failures.md - computations not completed within 7 min 3 s (423 s)

The user's order of 2026-10-14: "NEVER wait more than 7 minutes and 3 seconds for the completion of an individual calculation; if a wait time is longer than 7 minutes and 3 seconds then YOU ARE COMPUTING INCORRECTLY; kILL ALL OF THESE RIDICULOUSLY LONG AGENT JOBS." and "make a careful and exact note of each computation that you are unable to complete in the allotted time of 7 minutes and 3 seconds".

Rule applied here: every individual calculation (a script, solver, notebook, test suite, PDF build, or an agent job) whose wall time exceeds 423 s is listed, whether it was killed or finished late. Times are wall-clock on this machine (Windows 11, Intel Core Ultra 9 275HX, 24 cores, 191 GB), Pacific time, 2026-10-14 unless stated. Entries are appended as they occur; nothing is removed.

## A. Killed at 2026-10-14 ~12:05 by the order above (all started by Claude in this session)

All four workflows were stopped with TaskStop and every process tree they or the lead had started was killed with `taskkill /T /F`; a process listing afterwards showed none left (the user's own Wolfram front end, WolframNB.exe pid 22652 with its kernel, was not touched).

| # | Calculation | Started | Killed / ended | Wall time | State reached | Status |
|---|---|---|---|---|---|---|
| A1 | Old Stage 4 reference rerun R1 `m1_L3_N1016_lamm2_T0` (`python -B scripts/ks_reference_solver.py --config <old scratchpad>/stage4_keep/refsmear120-config.json`), estimated about 4.5 h by the 2026-10-08 record | 11:32:01 | ~12:05:20 | ~33 min | first pass at level 2 (N = 480) of 3 levels; no run.json written | KILLED, not completed |
| A2 | Old Stage 5 reference pairs (`python -B scripts/ks_reference_pairs.py --workers 8 --resume`): 180 runs, 45 kept from earlier | 11:32:01 | ~12:05:20 | ~33 min | 3 more runs finished, each itself over 423 s: d16c_m1_L3_N112_lamm1_T0p1/plusM 1341 s, d16c_m1_L3_N112_lamp1_T0p1/plusM 1750 s, .../minusM 1757 s; the rest not computed | KILLED, not completed |
| A3 | Old Stage 5 Rust pairs canonical (`dirac16complex_kohn_sham.exe pairs`, 8 cores; no resume; summary only at the end) | 11:32:01 | ~12:05:20 | ~33 min | 49 universe lines of the matrix logged; no summary.json | KILLED, not completed |
| A4 | Old Stage 5 Rust pairs repeat (`... pairs --output build/s5-rust-repeat`, 8 other cores) | 11:32:01 | ~12:05:20 | ~33 min | 52 universe lines; no summary.json | KILLED, not completed |
| A5 | Revision unit tests (`python -m unittest discover -s Revision/tests`) | 11:33:55 | ~12:05:20 | > 31 min | not finished (2 failures printed so far, not yet reported in full) | KILLED, not completed |
| A6 | Root unit tests (`python -m unittest discover -s tests`) | 11:33:55 | 11:50:12 | 976 s (16 min 16 s) | finished: 661 tests, 8 failures (4 old-Stage-4 notebook report, 4 matter-antimatter hash pins), 6 skipped | FINISHED LATE (over 423 s) |
| A7 | One Stage-5 reference run re-computed for a byte check (`ks_reference_pairs.py --runs d16c_m3_L3_N112_lam0_T0/plusM --workers 1`) | 11:51:24 | 12:01:17 | 592 s | finished; physics identical to the committed run.json (the only differing key is `memoryGuard`, added by erratum E5.3) | FINISHED LATE (over 423 s) |

### A8. Agent jobs of the four workflows that ran longer than 423 s

39 of 56 agents exceeded 423 s (16 of them were killed unfinished at ~12:05; the others finished late). Times are from the agents' own transcript timestamps (first to last entry).

| Workflow | Agent | Start | End | Seconds | Status |
|---|---|---|---|---|---|
| old Stage 5 documents prep (wf_4f461ffd-f21) | docA:part1 | 11:38:59 | 12:04:42 | 1543 | FINISHED LATE (over 423 s) |
| old Stage 5 documents prep (wf_4f461ffd-f21) | docB:part1 | 11:38:59 | 12:00:40 | 1301 | FINISHED LATE (over 423 s) |
| old Stage 5 documents prep (wf_4f461ffd-f21) | gate | 11:38:59 | 12:05:01 | 1562 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:notebooks:00-05 | 11:45:46 | 12:05:04 | 1158 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:references:12-17 | 11:45:46 | 12:05:04 | 1158 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:notebooks:18-23 | 11:45:46 | 12:05:01 | 1156 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:references:00-05 | 11:45:46 | 12:05:01 | 1156 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:notebooks:12-17 | 11:45:46 | 12:05:04 | 1159 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:references:06-11 | 11:45:46 | 12:05:04 | 1159 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:notebooks:06-11 | 11:45:46 | 12:05:06 | 1160 | KILLED (unfinished) |
| book lens reviews (wf_6589331b-eed) | review:references:18-23 | 11:45:46 | 12:05:02 | 1156 | KILLED (unfinished) |
| errata E5.1 (wf_951c252f-588) | errata-writer | 11:54:50 | 12:05:04 | 614 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | fix:11 | 11:36:25 | 11:52:05 | 940 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:12 | 11:36:25 | 11:43:30 | 425 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:10 | 11:36:25 | 11:44:24 | 479 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:13 | 11:36:25 | 11:44:58 | 512 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:16 | 11:36:25 | 11:44:58 | 513 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:09 | 11:36:25 | 11:50:14 | 829 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:17 | 11:36:25 | 11:51:03 | 878 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:07 | 11:36:25 | 11:56:06 | 1181 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:15 | 11:38:49 | 11:57:27 | 1118 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:05 | 11:38:58 | 11:56:13 | 1035 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:18 | 11:39:28 | 11:54:15 | 887 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:20 | 11:39:30 | 11:50:20 | 649 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:21 | 11:41:01 | 12:01:51 | 1251 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | fix:14 | 11:41:03 | 11:59:02 | 1079 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:00 | 11:41:52 | 11:54:54 | 782 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:12 | 11:43:30 | 11:52:43 | 552 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:10 | 11:44:24 | 11:59:29 | 905 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:13 | 11:44:58 | 11:59:57 | 899 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:16 | 11:44:58 | 12:01:07 | 969 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:09 | 11:50:14 | 12:03:16 | 782 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:20 | 11:50:20 | 12:03:02 | 762 | FINISHED LATE (over 423 s) |
| book continuation (wf_dce5cca3-aa8) | verify:17 | 11:51:03 | 12:05:04 | 841 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | verify:11 | 11:52:05 | 12:05:00 | 775 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | verify:18 | 11:54:15 | 12:05:07 | 652 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | verify:07 | 11:56:06 | 12:05:00 | 535 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | verify:05 | 11:56:13 | 12:05:01 | 529 | KILLED (unfinished) |
| book continuation (wf_dce5cca3-aa8) | verify:15 | 11:57:27 | 12:05:00 | 453 | KILLED (unfinished) |

Follow-up of 2026-10-16 (user order: suspend the 423 s limit for the 23 agents that finished late and let them contribute correctly; the user performs the 16 killed tasks by hand): `A8_LATE_AND_KILLED_AGENTS.md` lists what each of the 23 produced and where it enters the project, and gives one task formulation for each of the 16.

Agents of these workflows that stayed within 423 s: docB:part2 (261 s, KILLED (unfinished)), docA:part2 (19 s, KILLED (unfinished)), skeptic:05:0:0 (140 s, finished), fix:00 (328 s, finished), skeptic:05:0:1 (82 s, finished), skeptic:18:1:0 (80 s, finished), skeptic:15:0:1 (107 s, finished), skeptic:14:0:1 (278 s, finished), skeptic:14:0:0 (144 s, finished), skeptic:15:0:0 (97 s, finished), skeptic:18:1:1 (73 s, finished), skeptic:20:3:0 (103 s, finished), skeptic:20:3:1 (87 s, finished), skeptic:21:0:0 (153 s, finished), skeptic:21:0:1 (137 s, finished), verify:14 (359 s, KILLED (unfinished)), verify:21 (189 s, KILLED (unfinished)).

## B. Calculations of the project whose recorded wall time already exceeds 423 s

Measured or estimated in the records of 2026-10-08 (HANDOFF.md sections 0.4u-0.4z, the old scratchpad's stage5_plan_final.md). They have not been run in this session; each one that the metric change of 2026-10-14 requires to be re-run, and that again exceeds 423 s, will be entered in section C.

| Calculation | Recorded time | Kind |
|---|---|---|
| Full Revision gate `Revision/verify_revision.ps1` / `.sh` (65 steps, 9 of them "long") | about 3 h | estimate in HANDOFF 0.4u |
| `Revision/theory/wolfram/verify_field_theory.wls` | about 45 min | measured 2026-10-08 (HANDOFF 0.4y) |
| Old Stage 4 R1 reference run | about 4.5 h | estimate (HANDOFF 0.4r) |
| Old Stage 5 reference pairs, full matrix at 8 workers | about 4.5 h (1.6-9.3 h) | estimate (stage5_plan_final.md) |
| One Stage-5 reference run of the largest class (d16c_m3_L3_N112_lamm2_T0/plusM) | 1925.7 s | measured 2026-10-08 |
| Rust pairs canonical / repeat / refined | about 1.7 h / 1.7 h / unmeasured | estimate |
| One Rust pairs universe d16c_m3_L3_N8_lamp2_T0 plusM | 6640.1 s | measured 2026-10-08 |

## C. Calculations of the metric change of 2026-10-14 that do not finish within 423 s

(appended as they occur)

Since the kill of section A (about 12:05) every calculation of this work was started with `timeout 423`; none was
killed by that limit, and no wall time exceeded 423 s (the longest: the refined-tolerance Rust run of the Kohn-Sham
solver, 328 s; checked in the run logs and the session transcript on 2026-10-14 at about 15:55; in the gate run of
C7 its batch, with the two audits, took 341 s).

| # | Calculation | Status | What was done instead / what remains |
|---|---|---|---|
| C1 | `Revision/theory/wolfram/verify_field_theory.wls` for GENERAL b4: its sections Noether identities, exact solutions and conservation, canonical quantisation | NOT COMPUTED (not attempted): serially these sections took 910.8 s, 1005.4 s and the whole verifier 1783-2508 s at b4 = 1 (2026-10-08) | The b4 = 1 verifier (84 checks) was re-run on 2026-10-14 in the author's coordinates with its slow zero tests on 16 parallel subkernels: 309 s and 310 s. For general b4 only the supplements `verify_field_theory_b4.wls` (19 checks) and `verify_field_theory_b4_emt.wls` C, G (4 + 4 checks) exist; the general-b4 Noether identities, exact solutions and canonical quantisation REMAIN UNCOMPUTED. |
| C2 | `Revision/kohn_sham/reference/run_reference.py` as ONE run (578.3 s on 2026-10-01) | NOT RUN in one piece | Run in four parts with the new job cache (`--cache DIR --part i/4`, 12 processes): 234 s, 225 s, 258 s, 268 s, then the assembly from the cache, 3 s; outputs equal to a single run (pure jobs, fixed write order). |
| C3 | `Revision/kohn_sham/checker/crosscheck_ks.py` with its own reference repeat in one run (721-777 s on 2026-10-08) | NOT RUN in one piece | The repeat computed beforehand in four parts into a separate job cache (`run_reference.py --cache DIR --part i/4`), the checker run with `--repeat-cache DIR`: parts 239 s, 232 s, 262 s, 267 s; checker 21 s, 31 of 31 PASS, the repeat byte-identical to the committed reference; report and table equal to those of 2026-10-08 after the renaming. |
| C4 | `Revision/kohn_sham/tip_convergence/tip_convergence.py` at its former cap of 8 workers (541-553 s on 2026-10-08) | not run at 8 workers | Cap raised to 22 workers (outputs independent of it): 196 s, 7 of 7. |
| C5 | Rust refined-tolerance Kohn-Sham run (618.6 s on 2026-10-07, in parallel with the repeat) | finished within the limit when run alone | 328 s. |
| C6 | `gkd_lovelock` `gkd-selftest --exhaustive-max 4` (gate step, up to 900 s) | not run on 2026-10-14 | Not affected by the metric change or the relabelling (the generalized Kronecker delta is coordinate free); its committed result stands. |
| C7 | The full Revision gate `verify_revision.ps1` / `.sh` (85 steps, expected 8057 s by its own table) | not run as one calculation | Run on 2026-10-14 from about 16:49 to 18:15 as 37 batches `bash Revision/verify_revision.sh --steps ...`, each under `timeout 423`: the 82 work steps other than `gkd-rust-selftest` (C6), with the two audits `committed-unchanged` and `reports-pass` in every batch; every batch ended with `revision_verification=OK`, none was stopped; batch times 1 s to 341 s (the longest, `ks-rust-refined`), 5114 s in all. The step `gkd-rust-selftest` (expected 900 s) was not run: see C6. |

## D. The textbook relabel of 2026-10-14/15 (the 333-minute window, from 19:42 to 01:15)

| # | Calculation | Status | What happened / what remains |
|---|---|---|---|
| D1 | `git push origin main` of commit fccfdb3 (textbook chapter 16), started at about 20:57 on 2026-10-14 without a time limit | OVER 423 s: it hung for 26816 s (7 h 27 min) and ended with "Connection timed out" at 04:25 on 2026-10-15; the machine was most likely asleep | The tool moved the command to the background after 120 s, and nothing ran in between. Retried at 04:25 with `timeout 120 git push`: done in seconds, and origin/main equals HEAD. Because of this hang the 01:15 deadline was overrun, and the work planned after chapter 16 (chapters 11, 12 and 17-23) was NOT done. |
| D2 | `python -m unittest Revision.tests.test_universes_in_pairs_textbook` (all classes, serially), started at about 20:10 under `timeout 423` | KILLED at 423 s (exit 124), not completed | Each class was run separately: Requirements, Files, Validators, Tools, Notebooks (static) and Book.test_chapters_so_far / each_chapter_alone / pdf_registered are OK. `Book.test_assembled_book_is_current` FAILS until the whole book is re-assembled (the last assembled edition still has the old labels). The serial byte-for-byte rebuild test (`test_notebooks_rebuild_byte_for_byte`) takes longer than 423 s; `Revision/textbook/tools/relabel/check_all.py` replaces it (nbkit check, 8 in parallel, each under 423 s). |
| D3 | Textbook chapters 11, 12 and 17-23 (relabel to x0..x7, b4 statements, notebook rebuilds) | NOT DONE in the window | HANDOFF.md section 0.6 lists, for each failing notebook, the reason measured by `check_all.py`, and the procedure. Chapter 11 needs b4 variables in 11b's exact polynomial engine, because the Rust Lovelock program was rerun with the b4 metric. |
| D4 | Full book assembly and PDF, TEXTBOOK_SPEC.md, EXECUTION_PROVENANCE_INDEX rows for the b4 scripts, a fresh-clone verification | NOT DONE | See HANDOFF.md section 0.6, item 8. |

Every notebook build and check of this window ran under `timeout 423`. The longest was 16a_reference_crosscheck, 193 s for the build together with its check; 11a's check took 362 s.

D3 and D4 were done on 2026-10-15 (section E; HANDOFF.md section 0.7).

## E. The continuation of 2026-10-15 (chapters 11, 12 and 17-23, the book, the PDF; times are PDT)

| # | Calculation or step | Status | What happened / what was done |
|---|---|---|---|
| E1 | Notebook 11a, `nbkit.py build` (its cell ran the Rust GKD self-test `lovelock_gkd gkd-selftest --exhaustive-max 4`, which checks every pair of index lists up to length 4, 16777216 pairs at length 4), started 05:25 under `timeout 423` | KILLED at 423 s (exit 124), not completed | The self-test alone takes longer than the limit (the record: 7 to 13 minutes). |
| E2 | The Rust self-test alone, started 05:39 under `timeout 300` to measure it | KILLED at 300 s, not completed | It had printed the PASS lines up to length 3; length 4 had not finished. |
| E3 | Notebook 11a, `nbkit.py build` again, started 05:46 under `timeout 423` (my edit script for the fix had failed, so the old builder ran) | KILLED at 423 s (exit 124), not completed | Fixed: Notebook 11a no longer runs the self-test. It prints the command to repeat it and reads the committed record `Revision/gkd_lovelock/results/gkd-selftest.json` (verdict SUCCESS; lengths 1 to 9 with 0 mismatches; length 4 exhaustive). Its build now takes 17 s, its check 7.6 s. |
| E4 | Two edit scripts written as bash heredocs (the 11a fix and a chapter 11 text fix) | FAILED | The heredoc changed backslashes (`\rho` became a carriage return plus `ho`). `strict_replace` stopped both before anything was written. Both scripts were rewritten with a file-writing tool. Rule: never write text with backslashes through a heredoc. |
| E5 | Python fix scripts with `'''` inside an `r'''` string | FAILED (syntax error, nothing written) | Rewritten with `r"""` strings or placeholders. |
| E6 | The label scanners `scan_old.py` and `risk_scan.py` | MISSED labels | Old labels glued to a digit or a letter (`2p_8`, `6q_8`, `ip_8`, check names with `2x8`, `e_{88}`, `dx8`, `M_8`) were found later by grep and fixed in the chapter commits. The README of the relabel tools now names this gap. |
| E7 | Relabel artifacts in the chapter text, not caught by any scanner | FOUND BY READING, fixed | `f_0f_2\cdots f_7`; "c = x_0 ... x_6"; "x_0x_1 to x_7x_0"; diagonal lists said to be in the order x0..x7 that listed x0 last (chapters 11 and 21, the markdown of 12a); "P_{x_0}, ..., P_{x_3} and P_{x_7}"; and in chapter 07 row 1 of the frame gammas was still listed in the old order (x1..x7, x0). Fixed in the chapter commits and in 04f9bbb. |
| E8 | Builders that failed after the relabel, because of literal lists in the old order | FAILED at build, fixed | 18a product signs; 18c the lists LAM and k; 21b the Omega record text; 11b counters (8 against 10 components); 23a printed more than 80 lines (now it writes `Revision/textbook/data/23a_gate_steps.csv` and prints only the long steps and the audits). |
| E9 | The first PDF build of the whole book (06:16, 284 s) | FAILED: 18 LaTeX warnings (9 Overfull displays, 9 Underfull lines), not registered | The relabel and the b4 text had made 9 displays too wide and 9 lines underfull. Fixed in 04f9bbb. The second build (06:29, 293 s) passed 11 of 11 checks: 0 warnings, 6539 pages, both builds byte-identical, registered. |
| E10 | The light b4 WolframScript re-run (06:30): I edited its bash runner while bash was executing it | ABORTED, re-run | The task was stopped and the `wolframscript` tree it had started killed (`taskkill /T`). That stray run had already finished two short scripts, out of order. No committed file changed (`git status` clean). Everything was re-run from a frozen copy of the runner (section 9 of `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`). |

No calculation of this continuation waited longer than 423 s, apart from E1 and E3, which were killed at 423 s.

## F. The dark sector with b4 (2026-10-15)

| # | Calculation or step | Status | What happened / what was done |
|---|---|---|---|
| F0 | The metric change of 2026-10-14 (b4(x4)) | NOT CARRIED INTO THE DARK SECTOR until the user's order of 2026-10-15 | The dark-sector record, its document, its notebook and the textbook chapter 22 still used b4 = 1. The user: "the Dark-sector hypotheses, which you never updated". Done on 2026-10-15 (HANDOFF.md 0.8; `Revision/dark_sector/B4_PROVENANCE.md`); the textbook is still open (HANDOFF.md 0.8, items 1 to 6). |
| F1 | I first treated b4 = 1 as the background of the dark sector | CORRECTED by the user | "b4 is a function of x4; b4 is NEVER 1." Everything was recomputed with a non-constant b4 on the history beta = 4/3; b4 = 1 appears only as the withdrawn record. |
| F2 | `python -m unittest Revision/tests/test_universes_in_pairs_textbook.py` (all classes), started under `timeout 423` | KILLED at 423 s (exit 124), not completed | The same mistake as D2. Its classes run separately in seconds (Files 0 s, the static notebook tests 1 to 2 s). |
| F3 | Three edit scripts written through bash heredocs with backslashes (one earlier in this work, the fix of the notebook test with a regular expression, and the first insertion of this section) | the first and the third FAILED (the strict assertion stopped them, nothing written); the second wrote the intended text, with a Python warning | The rule of E4 again. The scripts were rewritten with the file-writing tool. |
| F4 | The first build of the Revision notebook for b4 | figures with overlapping labels, and the condensate pole drawn as a vertical line | Found by looking at the four figures; fixed before the commit (legend of figure 1, the pole of figure 2 masked and marked, labels of figures 3 and 4). |
| F5 | A run time I quoted for `run_ks_history.py` in a draft provenance (24 s, from memory) | CORRECTED before the commit | The README says about 25 s; the re-run measured 34.9 s; the provenance quotes the README and the measurement. |

| F6 | My own first statements of the b4 record: "phantom only at an instant", "not the observer's w_eff" and "no crossing in M1 to M5" (derive_eos.py text, both READMEs, the document, the notebook) | WRONG for a condensate with lambda < 0, found while writing chapter 22 | With b4(x4) the observer reads w_eff(C) = -1/3 + (2/3) w_c, below -1 while the drifting ratio lies in (-2, -1). Corrected in 1d77417 (text only; the checks condensate_phantom_interval and condensate_observer_b4 already proved it). |
| F7 | "A drifting condensate reaches w0 = -0.861 only with w_a <= -2.64" (document, README) | WRONG reading: the record stored the MINIMUM of w_a near the Unite w0, not a bound | compute_eos.py now records the maximum too (C: -1.413); corrected in 3d9d25c. |
| F8 | Notebook 22b (textbook) as first written: "crossing of -1: no computed state and no model" | WRONG, seen in its own Figure 22b.3 (the drifting condensate crosses -1 under C at a = 0.9307) | Fixed before the commit e78d882 (a check of the crossing added). |
| F9 | A bash heredoc with backslashes for the 09b edit | FAILED (assertion; nothing written); the next command re-ran the unchanged builder, which rewrote only its provenance date | Redone with a script written by the file tool; the rule of E4 again. |
| F10 | The README table cell with "(4/3)" | would have broken the ledger of Notebook 00c (its pattern counts every "digit/digit" as a check count) | Reworded before the commit; the table quotes 50 counts. |

No other calculation of this work waited longer than 423 s; every producer, test and gate step was
run under `timeout 423` (the longest: the independent free gas, 77.0 s).

## G. Moving everything to b4(x4) (2026-10-15, HANDOFF.md 0.9)

| # | Calculation or step | Status | What happened / what was done |
|---|---|---|---|
| G1 | The first run of the rewritten `verify_field_theory.wls base` | FAILED at once (syntax), but wolframscript returned exit code 0 | A comment contained `emt-*)`, which closed the comment early. Fixed; the parts are judged by their summary line and the part file, never by the exit code alone. |
| G2 | `verify_field_theory.wls solutions` (exact solutions with b4), started under `timeout 423` while a sympy run competed for the processors | KILLED at 423 s (exit 124), not completed | The explicit Grassmann solution with the three integrals of b4^(-3/2) was too large for one part. Restructured (section G3 below); not re-run as it was. |
| G3 | A cProfile run of the sympy Grassmann solution check (`grassmann_solution.verify` with b4), started under `timeout 423` | KILLED at 423 s, not completed | The unprofiled run had taken about 230 s of the 364 s of the whole checker, too close to the limit. Restructured, not re-run as it was. |
| G4 | The control of the commuting nonlinear solution in `check_field_theory.py` (S0 set to 0 everywhere) | WRONG control (it is self-consistent, so it cannot fail), the check reported FAIL | Replaced by a control that uses the field equation with the mass m while the flow keeps S0. |
| G5 | The first general-b4 version of `Revision/lead_checks/einstein_gauss_bonnet_a4.py` (sympy `simplify` on the functions a4(x4), b4(x4) in eight dimensions), started under `timeout 423` | NOT STOPPED by `timeout 423` (a native Windows python process; the tool's own limit of 440 s came first), killed by hand | Rewritten with an exact ring calculus (no `simplify`); since then every run uses `timeout -k 5 423` (KILL 5 s after TERM). |
| G6 | The first run of the b4 version of `Revision/kohn_sham/theory/check_ks_theory.py` | 1 check FAILED (`emt_orbital_components`: K^x4_x4 and K_x4y) | sympy does not know that the derivative of the real function b4(x4) is real, so conjugate(b4') did not cancel against b4'. Fixed by the substitution conjugate(b4') -> b4' (helper `real_b4`); 63/63. The Wolfram twin passed at once (it uses b4 = E^(2 q[x4]) with real q). |
| G7 | The first canonical Rust run with the recalibrated couplings (`revision_ks_solver all`, 77 s) | 1 thermal state FAILED (N688_lamm1_a00_T10: Mermin SCF diverged, residual 0.197 after 400 iterations); then the Mermin-roots tool failed on the same state through `single` | A numerical consequence of the 13 to 36 times stronger couplings, not a time-limit problem. The Mermin states and `single` at T > 0 now use the coupling continuation of the ground states as fallback (check `thermo_scf_path`; used for this state only). |
| G8 | The first refined comparison (`compare_runs.py`) after the change | 1 check FAILED (`refined_adiabatic_derivatives`, 1.9e-6 against 1e-6) | dE/da4 of N8_lamp1_a20 is only 3.6e-5 with b4; the canonical difference quotient was 7.0e-11 off because the a4 neighbours were converged only to scf_tol. The tolerance was kept; the neighbours are now converged to scf_tol/10 (1.4e-7). The refined run took 340.6 s, below 423 s. |
| G9 | `run_reference.py --part 2/6` (the Python reference of the b4 record), under `timeout -k 5 423` | FAILED after 68 s (RuntimeError: Mermin SCF of N688_lamm1_a00_T10 not converged, residual 6.4e-2) | The same state as G7, now in the independent reference. The reference got its own coupling-continuation fallback (`ks_fd.solve_state_robust`, check `scf_paths`); because the job cache is tied to the sha256 of the code, the running chain was stopped (`TaskStop`, then the remaining python processes) and all six parts were recomputed (120 to 232 s each). |
| G10 | The first `crosscheck_ks.py` run of the b4 record | 7 checks FAILED | I ran it before `measure_rust_refinement.py`, against the order of the gate, so it compared with the refinement runs of the former couplings; in addition the float text of beta (16 digits against the shortest repr) and the exact tie of the N = 8 Q_max pairs (new with b4) were not handled. After the refinement run and the two checker fixes: 31/31. |
| G11 | The first b4 run of `tip_convergence.py` (187 s) | FAILED at the analysis (KeyError 'Vol7') | The solver's `parameters.json` now names the cell volume at a4,0 = 0 `Vol7AtA4Zero`; the study was changed to read it (it uses it only at a4,0 = 0) and rerun: 7/7 in 187 s. |
| G12 | The first b4 version of `Revision/field_equations_a4/ks_source/ks_source_a4.py` | 2 checks FAILED, then 1 | (1) `D6`: on one Gauss-Bonnet branch b4 collapses and the rates run away (a4'/H ~ 7.5e3 at a4 = 2), where the adiabaticity measure exceeds 1: the integration now stops there (outcome adiabaticity_lost; a physical limit of the instantaneous-state source, not a bug). (2) `D1`: Newton failed at the author's start point (det J = -0.0139, near a fold: the step cannot fall below eps/|det|); the convergence test now accepts a step below 1e-11 with the residual at the rounding level. (3) `D1` again: with the record's 5 slices the two source interpolations differed by 0.7% in one sensitive case; the source is now the record's dense free-gas history (41 slices), agreement 3.3e-4 with the tolerance unchanged. Every run 2 s under `timeout -k 5 423`. |
| G13 | `Revision/pairing/kohn_sham/numerics/t3_reference_demo.py`, check `all_members_converged` (written on 2026-10-08) | PASS with a WRONG detail text, found on 2026-10-16 | The detail said "18 states x 3 members (plus, image, control) ... converged", although the reference finds no self-consistent control state in 3 of the 18 states (with b4: N8_lamm2_a10, N8_lamm2_a20, N136_lamm2_a20; with b4 = 1 also 3 states); the verdict was right (the controls are not required to converge), the sentence was not. The detail now names the plus and image members of every state and the controls of 15 states, and points to `negative_control_untransformed_tip` for the other 3. The T3 Rust demonstration with b4 took 316 s of wall time (630 `single` runs; two diverging controls, N136_lamm2_a20 and N688_lamm2_a20, ran last through the coupling continuation), within 423 s; its gate time was raised from 285 s to 320 s. |
| G14 | `Revision/tests/test_revision_notebooks.py`, test `test_dark_sector_record_counts_printed` | FAILED since commit `1964b7b` (2026-10-16), found on 2026-10-16 | The dark-sector rerun with lambda_hat gave `ks-history-run.json` 8 checks (the notebook prints 8/8), but the test still expected 7: I did not run this test file after that commit. Fixed (7 -> 8); the static tests of the file pass again (9 OK, 2 skipped). |
| G15 | The first build of the rewritten notebook `Revision/notebooks/lovelock_gkd` (general b4), under `timeout -k 5 423` | FAILED at the new check `blocks_differ_on_the_history` (22 s) | I expected the ordinary-space and extra-time blocks of every E_(k) to differ on the history a4' = H, u = 4H/3; for k = 3 they agree: E_(3)^x1_x1 - E_(3)^x5_x5 contains the factor (H - a4')(H + a4') at a4'' = v = 0 and vanishes there for every u. The check was rewritten to state what the computation shows (`blocks_on_the_history`: k = 1, 2 differ, k = 3 agrees for every u), and the texts with it; a second build was stopped by me after 3 s to correct one more sentence (its orphaned program run ended by itself); the third build and the check passed (45/45, byte-identical). |
| G16 | `Revision/tests/test_revision_gate.py`, test `test_table_is_well_formed` (step t3-rust-demo) | FAILED since phase 6 (2026-10-16), found on 2026-10-16 when the Revision unit tests were run for phase 8 | When I raised the gate time of t3-rust-demo from 285 s to 320 s (G13) I did not mark the step long, although the gate marks every step above 300 s as long (skipped by `--fast`) and its own test requires it. Fixed in both twins (kind 1, header "long"); `--fast` now skips 4 steps and runs 95 (dry run checked); README updated; the gate test passes (16 tests). |
| G17 | Two patch scripts of phase 8 written through a Git Bash heredoc (a layout fix and a wording fix of the dirac16complex00 document) | FAILED at their own assertions (the heredoc turned the backslashes of the LaTeX into escapes), no file was changed by them | The rule of E4 (and F3, F9) again, which I already knew; I noticed only after a PDF page still showed the old wording. The fixes were made with the editor instead, the document regenerated, rebuilt (42 pages, no warnings) and registered; its test passes. Patch scripts are written with the editor tool, never through a heredoc. |
| G18 | Phase 9, notebook 07b: a small fix of my patch script (two match strings with LaTeX backslashes) written through a Git Bash heredoc on 2026-10-16 | Python printed SyntaxWarnings for the escapes, the fix itself applied correctly | The rule of G17 broken once more. I checked the result in the builder line by line (single backslashes, as intended) and made every later fix with the editor tool. |
