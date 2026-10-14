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

