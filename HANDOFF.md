# HANDOFF — exact restart procedure after a session limit

This file is the complete restart kit for a fresh Claude Code session (or a human)
that has none of the previous conversation.  Everything a restart needs is committed
in this repository; nothing depends on the old session's scratch directory.

## 0. Exact restart procedure

### 0.1 Resume the same conversation (preferred: keeps all context)

```powershell
cd C:\Users\nsh\Developer\github\Dirac_claude
claude --continue
```

`claude --continue` (short: `claude -c`) reopens the most recent session started in
this directory.  If several exist, run `claude --resume` and choose the one whose
title mentions dirac16complex.  In the Claude desktop app: open the Code tab and
click the session in the sidebar.  After it opens, type:

```text
continue with all stages, do not stop
```

Background workflows do NOT survive a session limit.  The resumed session must
re-launch them (section 0.3); finished files are on disk and are reused.

### 0.2 Start a new session (if the old one cannot be resumed)

```powershell
cd C:\Users\nsh\Developer\github\Dirac_claude
claude
```

Paste this prompt verbatim as the first message:

```text
Read HANDOFF.md completely. Then read handoff/specs/CONTRACT.md (all sections,
including section 11), handoff/specs/STAGE4_SPEC.md (including sections 7 and 8),
handoff/specs/NUMERICS_CONTRACT.md (including its erratum) and
handoff/specs/STAGE2_SPEC.md. Run "git pull" and "bash scripts/setup_solver.sh".
Then continue every unfinished stage listed in HANDOFF.md section 2, in order,
using the Workflow tool with the scripts in handoff/workflows/ as described in
HANDOFF.md section 3. Never modify dirac-main/, vendor/, or the .nb notebook.
Do not stop between stages. Commit and push to origin main after every completed
stage and after every ~30 minutes of work, verify from a fresh clone, and never
take shortcuts or weaken a check.
```

### 0.3 How the new session re-launches the work

1. Copy the needed `handoff/workflows/*.js` into its own scratchpad directory and set
   `const SP = '<its scratchpad path>'` in each (keep `ROOT`; LF line endings only).
2. Launch each script with the Workflow tool (`scriptPath`).  A fresh session has no
   cached agent results (resume by run id works only inside the session that ran it),
   so every agent runs again; the prompts tell the agents that partial files exist and
   must be inspected and finished, not restarted from zero.
3. NEVER use blocking waits or sleep loops (the user forbids any delay): launch the
   workflows in the background, do real work meanwhile, and act on the completion
   notifications.  Commit and push after every milestone; the Stop hook
   (`.claude/settings.local.json` -> `.claude/hooks/stop_push_verify.py`, git-ignored,
   so it must be re-created in a new clone; see the memory note) commits, pushes and
   checks the repository every time the session stops.
4. When the user writes "pause" or "STOP": halt at once (create `.claude/ALLOW_STOP` in
   the same first action so the Stop hook allows the stop), push, report in a few lines.

### 0.4 State at the pause of 2026-09-30 15:05 and the exact order of work

The user's priority (2026-09-30 12:10): the TEXTBOOK first, then the other stages.

A. Textbook (`handoff/specs/TEXTBOOK_SPEC.md`; chapters in `provenance/textbook/chapters/`).
   * Chapters 00-05, 08-13: written and adversarially reviewed (198 findings, skeptic-
     verified, fixed; `handoff/workflows/wf_textbook_wave_a_review.js`); cross-chapter
     items the per-chapter fixers could not apply: `handoff/reviews/textbook_wave_a_carryover.json`.
   * Chapters 06, 07, 14, 15, 16, 17, 18: written, reviewed and fixed
     (`handoff/workflows/wf_textbook_wave_b_chapters.js`).
   * Chapters 19 and 20: the writer was still running at the pause.  After a restart:
     if `20-glossary-and-check-index.md` is missing or incomplete, run
     `wf_textbook_wave_b_chapters.js` with `TASKS` reduced to the `back` entry (writer,
     reviewer, fixer of chapters 19 and 20).  Chapter 19 had CRLF line endings: convert to LF.
   * Then run `handoff/workflows/wf_textbook_final.js` (carry-over items, final honesty
     ledger of Chapter 0 and Stage-4 status in Chapter 13, assembly with
     `scripts/build_textbook.py`, PDF with `--developer-layout --number-sections-from-zero`,
     registration, `tests/test_d16c_textbook_publication.py`, nine whole-book review
     lenses, skeptics, per-chapter fixers, rebuild and re-register).  Push.
B. Matter-antimatter (`provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.*`): COMPLETE 2026-09-30 15:40 -
   Wolfram 44/44 (twice, byte-identical), Python 77/77 (twice, byte-identical), all 49 tests of
   tests/test_d16c_matter_antimatter*.py pass, PDF 36 pages registered; 17 of the 18 review findings
   fixed, the 18th (Chapter 0 'no CP violation') belongs to the textbook final workflow.  When the
   Stage-5 documents and gate are complete, change the PROVISIONAL status strings in
   wolfram/Dirac16ComplexMatterAntimatter.wl (stage5Krein, M4/M5 statements) and
   scripts/check_dirac16complex_matter_antimatter.py, rerun both, rebuild the PDF.
C. Stage 5: exact theory COMPLETE (Wolfram 00 46/46, pairing 141/141; sympy 00 49/49,
   pairing 172/172, all under `artifacts/dirac16complex/pair-creation/`).  Numerics partial:
   `rust/pairs/` has run folders but no `summary.json`; `scripts/ks_reference_pairs.py
   --workers 10 --resume` was stopped at 12:12 (partial `reference/`).  After the textbook:
   rerun the `rust-pairs` and `reference-pairs` agents of `wf_stage5_theory_numerics.js`
   (and its checker), then `handoff/workflows/wf_stage5_docs_review.js` (documents
   DIRAC16COMPLEX00_FIELD_THEORY and DIRAC16COMPLEX_PAIR_CREATION, the gate
   `scripts/verify_stage5_pair_creation.*`, four review lenses, fixer), then the gate from a
   fresh clone.
   Stage-5 correction required (found by the matter-antimatter review, finding F1, confirmed by
   MA_M4_imageFieldFockModel): `pairing-theory.json` T1krein.imageField says the image universe carries
   'energy -|eps| and charge -1 per quantum' and T1krein.consequence 'T^pair = 0 at the operator level';
   under the image field's own anticommutator (-B) those operators are minus its x4-translation
   generator and minus its charge, so the physical reading must be corrected in
   wolfram/Dirac16ComplexPairing.wl and scripts/check_dirac16complex_pairing.py (see
   provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md section 7.3) before the Stage-5 documents are written.
D. Stage 4: cross-check final state 63 checks, 1 failed (canonical_eigenvalues, section 2
   Stage-4 row); analyse it (Rust 301 vs 601 grid error of the deep state), then rerun the
   documents phase of `wf_stage4_notebooks_documents.js` (it was at doc-main/doc-student when
   the previous session ended), then `wf_stage4_review.js`, then the gate
   `scripts/verify_stage4_kohn_sham.{ps1,sh}` from a fresh clone (both twins; hours).
E. Final: README.md, HANDOFF.md and the memory notes; `python -m unittest discover -s tests
   -p "test_*.py"`; every stage's gate from fresh public clones; push.

## 1. What this repository is

`dirac16complex`: a 16-component complex Grassmann spinor field of Pin(4,4) in 4+4
dimensions.  Stages: (1) arbitrary gravitational field; (2) the notebook's primordial
pair-creation field; (3) dark-sector numerics (five CVODE experiments); (4) Kohn–Sham
DFT ground and first excited states in the primordial field.  README.md gives the
map; provenance/*.md are the documents; artifacts/dirac16complex/* the reports.

## 2. State at the last push and what remains

| Stage | Done (verified) | Remaining |
|---|---|---|
| 1 arbitrary field | COMPLETE: 153/153 exact checks in five reports, cross-implementation agreement, document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{md,tex,pdf}` (45 pp), 4-lens review + fixes, gate `scripts/verify_stage1_arbitrary_field.{ps1,sh}` = OK | nothing. (2026-09-30) public-clone mode added and VERIFIED: fresh public clone, sh and ps1 twins OK (153 checks true, 4 files identical, 3 with only the dirac-main differences), and sh with dirac-main OK (logs handoff/reviews/stage1_gate_2026-09-30_*.log) |
| 2 primordial field | COMPLETE: 126/126 + 16/16 checks, document `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.{md,tex,pdf}` (38 pp), 3-lens review + 21 fixes, gate `scripts/verify_stage2_primordial_field.{ps1,sh}` = OK | nothing |
| 3 dark-sector numerics | COMPLETE: Rust crate `studies/dirac16complex_cosmology` (5 experiments), both notebooks, figures, documents `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS` and `provenance/DIRAC16COMPLEX_STUDENT_GUIDE`, two review rounds with all fixes (`handoff/reviews/stage3_review_round2_findings.json`); gate `scripts/verify_stage3_dark_sector.{ps1,sh}` = OK from a fresh clone of 1fb83c3 (`handoff/reviews/stage3_gate_2026-09-30_fresh_clone_OK.log`, 28 min) | nothing |
| 4 Kohn–Sham DFT | exact theory `wolfram/Dirac16ComplexKohnSham.wl` + verifier (125/125); `scripts/check_dirac16complex_kohn_sham_theory.py` (sympy, 157/157) with `artifacts/dirac16complex/kohn-sham/{kohn-sham-theory.json,exchange-table.json,python-theory-report.json}`; Rust crate `studies/dirac16complex_kohn_sham` COMPLETE (fmt/clippy clean, 35 tests; canonical tree `artifacts/dirac16complex/kohn-sham/rust/` with own checks spectrum 33, scf 137, excited 65 (with the g601 refinement), thermo 102, emt 60, all SUCCESS; a repeat run is byte-identical over 327 files; a refined run agrees to 6.0e-8 relative; `rust/determinism-report.json`); `scripts/ks_reference_solver.py` (55 reference runs in `artifacts/dirac16complex/kohn-sham/reference/`) and `scripts/check_dirac16complex_kohn_sham.py` written | (2026-09-30, later) The 4 cross-check failures were diagnosed and fixed in code (commit b22a558): (a) particle-hole pairs of T = 0 runs use an occupation floor of 1e-12 in both solvers (holes f > 1e-12, particles f < 1 - 1e-12; commit after b22a558, which had first tried an aufbau rule and misdescribed the case). The smeared N = 1016, -lambda_hat_2 run: the aufbau count closes at the 192-fold k = 0.935 band, the smeared ensemble moves about 4.2 particles into the 8-fold k = 0 level 3.7e-3 m above it; its KS gap and Delta-SCF refer to that ensemble; (b) the checker gives excited records the scf parameters (smeared f were compared as exact T = 0); (c) the reference's stale lamh_T0p3 run (own coupling) and its a4 rescaling partner (wrong lambda; now `lamp1rescaled`, lambda_hat_1 e^1.5 as in Rust) are recomputed, and the missing `m1_L3_N112_lamh_T1` is computed, by `python scripts/ks_reference_solver.py --resume --skip-self-tests --workers 8`; the Rust excited tree is regenerated with the fixed binary (canonical, repeat, refined). Open: the Delta-SCF of the smeared run differs by 3.3e-6 (tolerance 1e-6); the reference's own extrapolation spread there is about 2.5e-6, so a finer-grid reference run (N0 = 120) decides it. Delta-SCF investigation (N = 1016, -lambda_hat_2, 07:05): Rust 301 points 0.0436184212, 601 points 0.0436193591 (continuum ~0.0436197); reference (60/120/240 grids, (h^2,h^3) elimination) 0.0436216925, admissible three-grid extrapolations 0.0436207-0.0436232; experiment: reference on 120/240/480 grids with explicit smearing 1e-3 (scratch stage4_tmp/refsmear120); if it converges to the same ensemble and approaches Rust, adopt that grid for this run as a documented override (like N0 = 120 for m = 3). State at 06:50 on 2026-09-30: code fixes committed (414d11e, 936c75d, 80a8095: occupation-floor particle-hole rule, excited records with parameters, a 601-point refinement of the hardest Delta-SCF, the measured Rust grid uncertainty in the checker tolerances); reruns in progress: Rust `excited` (canonical, then repeat and refined in the scratch trees), reference `--resume` (lamh_T0p3, lamh_T1, lamp1rescaled) and the reference `--config` rerun of m1_L3_N1016_lamm2_T0; after them run `python scripts/ks_reference_solver.py --resume --skip-self-tests` once more (rewrites reference-summary.json) and the full checker `python scripts/check_dirac16complex_kohn_sham.py --repeat <repeat tree> --refined <refined tree>`. State at 08:40 on 2026-09-30: the Rust `excited` reruns are done with binary sha 3bbc395a (canonical in `rust/`, repeat and refined in the session scratch `stage4_tmp/rust/{repeat,refined}`); `rust/determinism-report.json` regenerated: 330 repeat files byte-identical, refined 65 runs / 364829 levels with max relative energy 5.96e-8 (4/4 checks); the reference `--resume` pass finished (56 runs, none failed; lamh_T1 E0 = 46815.4294); the quick checker gave 63 checks, 4 failed: canonical_deltaSCF, canonical_eigenvalues (g601) and canonical_particleHole, all on the smeared N = 1016 run (waiting for the N0 = 60 floor-rule rerun `stage4_tmp/ref1016`, which writes into `reference/`, and the N0 = 120 experiment `stage4_tmp/refsmear120`, whose ground energies 120/240/480 extrapolate to 1126.8581 against Rust 1126.85809); reproduce_m1_L2_N8_lamp1_T0 failed only on the coarse --quick grids. The full checker (canonical grids, with the repeat and refined trees, 08:42) gives 63 checks, 3 failed, all three on the smeared N = 1016 run (canonical_deltaSCF ratio 1.69, canonical_eigenvalues g601 ratio 1.46, canonical_particleHole pending the floor-rule reference). 08:52: the floor-rule rerun of m1_L3_N1016_lamm2_T0 finished (E0 1126.858099431928, gap 0.0412551026; ground 60/120/240 extrapolation agrees with Rust 1126.858089 to 1e-8 relative), the `--resume` summary pass kept all 56 runs, and the full checker gives 63 checks, 2 failed: canonical_deltaSCF (reference 60/120/240: 0.0436218 against Rust 601 0.0436194 and the Rust 301/601 estimate 0.0436197; the reference's own levels 0.0430172, 0.0434646, 0.0435817 have the ratio 3.8, not yet asymptotic) and canonical_eigenvalues at g601 (1.54e-6 against 1.05e-6; the 601-point Rust eigenvalue moves away from the reference). Both wait for `stage4_tmp/refsmear120` (the same run on 120/240/480 grids with the smearing 1e-3 given directly); if it moves to Rust, the run gets the documented override N0 = 120 and smearing 1e-3 in `ks_reference_solver.py`, its output is copied into `reference/`, and the summary pass and the checker are repeated. 09:03: refsmear120 ground state converged at 480: the 120/240/480 (h^2, h^3) extrapolation gives E0 = 1126.858089105 against Rust 601 1126.858089030 (8e-8 absolute), while the 60/120/240 one gave 1126.858099432 (1e-5 off): the N0 = 60 grids bias this run's extrapolation; the excited state on 120/240/480 follows. 11:33: RESOLVED (STAGE4_SPEC E4.13): refsmear120 finished, Delta-SCF 0.0436199531 (E1 levels 1126.97662, 1126.92066, 1126.90648, order 1.98) against Rust 601 0.0436193591 and the Rust 301/601 extrapolation 0.0436196717; the canonical run list now gives this run N0 = 120 and smearing 1e-3 m (`canonical_runs` in ks_reference_solver.py), its output replaced `reference/m1_L3_N1016_lamm2_T0/` (the N0 = 60 run is kept in the session scratch stage4_tmp/ref1016_N0_60_backup), and the `--resume` summary pass kept all 56 runs; the full checker then writes `artifacts/dirac16complex/kohn-sham/python-check-report.json`. The full checker (11:58) gives 63 checks, 1 failed: canonical_eigenvalues (the 301-point smeared run's deep state eps -1.0537 differs from the N0 = 120 reference by 2.2e-6 against 1.05e-6; with N0 = 60 it was the 601-point run that failed) - OPEN, to be analysed (the Rust grid error of that state, 301 versus 601 points) before the gate. Also OPEN (found by the textbook review): the Rust `theory-agreement.json` note labelRelation reports 0 blocks for both j = -J and j = +J, i.e. its theory-label lookup matches nothing (studies/dirac16complex_kohn_sham/src/theory.rs); the relation s = -j itself is established by the Python theory checker. The notebooks, summary builder, gate scripts and both documents are written by `handoff/workflows/wf_stage4_notebooks_documents.js`; then `handoff/workflows/wf_stage4_review.js` (four review lenses + fixer); then the gate `scripts/verify_stage4_kohn_sham.{ps1,sh}` from a fresh clone |
| 5 dirac16complex00 and {+M,-M} pairing | spec `handoff/specs/STAGE5_SPEC.md` (2026-09-30) | exact theory (wolfram/Dirac16Complex00.wl, wolfram/Dirac16ComplexPairing.wl + verifiers), independent sympy checkers, Rust `pairs` subcommand + reference options + checker (`handoff/workflows/wf_stage5_theory_numerics.js`), then the documents `provenance/DIRAC16COMPLEX00_FIELD_THEORY.*` and `provenance/DIRAC16COMPLEX_PAIR_CREATION.*`, review, gate `scripts/verify_stage5_pair_creation.*`. Stage 4 was PAUSED at the user's request on 2026-09-30 (processes suspended; PIDs in the session scratch `suspended_pids.txt`; after a restart they are gone: rerun the Stage-4 reruns as listed in the Stage-4 row) |
| textbook | spec `handoff/specs/TEXTBOOK_SPEC.md` (2026-09-30) | wave A (chapters 00-05, 08-13 and the assembler `scripts/build_textbook.py` with `tests/test_d16c_textbook_assembler.py`, `handoff/workflows/wf_textbook_wave_a.js`) COMPLETE 2026-09-30 09:00 (7 agents, every chapter warning-free alone; the lead's review notes for the wave-B fixer are in the session scratch `textbook_lead_review.md`: ch00 Answer 0.5 photon pair creation needs a nucleus, ch00 L2 'the task's expression', ch05 'the task's scalar-field reference', ch13 numbers to refresh from the final Stage-4 reports); the PDF option `--number-sections-from-zero` (builder and build_provenance_pdf.py, opt-in, test in `tests/test_publication_tooling.py`) makes LaTeX print chapter N as N; wave B (chapters 06, 07, 14-18, final ledger, appendices 19-20) after Stage 5; then `provenance/DIRAC16COMPLEX_TEXTBOOK.{md,tex,pdf}`, review, register, test, push. Stage 4 was RESUMED on 2026-09-30 ("continue with all stages") 2026-09-30 12:15 (user: the textbook is the ONLY priority now; Stage 5 numerics and the Stage-4 documents were stopped, their orphan processes killed; resume them afterwards): running in parallel (disjoint files) `handoff/workflows/wf_textbook_wave_a_review.js` resumed from run wf_438d8253-305 (chapters 00-05, 08-13: 14 reviewers, skeptics, fixers) and `handoff/workflows/wf_textbook_wave_b_chapters.js` (chapters 06, 07, 14-20: writer, adversarial reviewer, fixer per chapter; run wf_feb9b915-2ef); then `handoff/workflows/wf_textbook_final.js` (chapter-0 ledger update, assembly, PDF with --developer-layout --number-sections-from-zero, four whole-book review lenses, fixer, registration, publication test). |
| matter-antimatter | spec `handoff/specs/MATTER_ANTIMATTER_SPEC.md` (2026-09-30; the requested "proof that the theory solves the matter-antimatter problem" is not provable: exact U(1) charge conservation) | exact theorems M1-M6 (Wolfram + sympy), document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.{md,tex,pdf}`, review, fix: `handoff/workflows/wf_matter_antimatter.js` running |
| final | — | README status table; `python -m unittest discover -s tests -v` all green; fresh-clone verification (clone into a scratch dir, `setup_solver`, run every gate); push |

How to tell what exists: `git log --stat -5`, `ls provenance scripts artifacts/dirac16complex/*`,
`python -m unittest discover -s tests -v`.  Every verifier prints
`check_count`/`failed_check_count`; every gate ends with `stageN_..._verification=OK`.

## 3. Workflow scripts (handoff/workflows/)

| Script | Covers | Launch when |
|---|---|---|
| `wf_stage3_docs.js` | Stage 3 integrate → notebooks → documents → review → fix → gate | the Stage-3 gate is not yet OK (finished phases are redone quickly because the files exist) |
| `wf_stage4.js` | all of Stage 4 (build → integrate → notebooks → documents → review → fix → gate) | always, until `stage4_kohn_sham_verification=OK` |
| `wf_stage1_doc.js`, `wf_stage2_doc.js` | Stage 1 / Stage 2 document, review, gate | only if their gates stop passing |
| `stage1-build-*.js`, `stage2-build-*.js`, `stage3-rust-engine-*.js`, `understand-*.js` | the original build phases (already complete) | never, unless rebuilding from scratch |

Each script defines `const SP = ...` (scratch path) and `ROOT`; update `SP`.
`handoff/tools/wait_for.py` is the blocking wait helper (section 0.3).

## 4. Binding conventions (never change silently)

- Counting from 0; `eta = diag(+,+,+,+,-,-,-,-)`; `x4` is time; gammas are the
  notebook's `T16^A` in the split-octonion block basis (exact fixture
  `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`); `C = sigma16`;
  `Psibar = Psi^dagger C`; `B = -i C gamma^4`; `Omega_mu = (1/8) omega_{mu ab}[gamma^a,gamma^b]`
  with `omega_{mu ab} = eta_ac omega_mu^c_b` (the notebook's `omega_mu^a_b S^{ab}` is wrong).
- Lagrangian, field equations, energy–momentum tensor, KE/PE splits, quantization:
  `handoff/specs/CONTRACT.md` sections 5–8 with the errata in section 11.
- Stage-2 corrections: `det g = +cos^2 z`; the condensate CAN source the field for
  `a4'' = 0` (`handoff/specs/STAGE4_SPEC.md` section 7); Stage-4 theory errata in
  its section 8 (p_req = +15H^2/kappa; 4-fold degeneracy per j-type; current matrix
  gamma^0 gamma^4; exchange is exactly local: e_x = -(lambda/32)(n^2 + S^2)).
- Engines: the committed numerical outputs come from the Win11 rustSolveIt engine
  (commit a8fdff45); macOS/Linux engines differ in their math library
  (`handoff/specs/NUMERICS_CONTRACT.md` erratum).
- Tooling: WolframScript 1.14 drops arguments after `--` (pass paths positionally);
  Windows PowerShell 5.1 cannot run the gates (they re-exec under PowerShell 7);
  PDFs only via `scripts/build_provenance_pdf.py <md> [--register]`; outputs
  deterministic (LF, `fmt_e(v,17)`); numbers in documents only from reports; large
  files written in chunks of ≤ 300 lines per tool call (64k output-token limit).

## 5. Private inputs (never commit)

`prompt_Dirac_claude*.txt`, the Gmail PDF, `dirac-main/`, `dirac-main_2.zip`,
`vendor/` are git-ignored on purpose.  The task statements are in the ignored
prompt files; their substance is in section 2 above and in the specs.
