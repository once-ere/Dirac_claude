# HANDOFF — exact restart procedure after a session limit

This file is the complete restart kit for a fresh Claude Code session (or a human)
that has none of the previous conversation.  Everything a restart needs is committed
in this repository; nothing depends on the old session's scratch directory.

## 0. Exact restart procedure

### 0.1 Resume the same conversation (preferred: keeps all context)

```powershell
cd D:\Developer\github\Dirac_claude
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
cd D:\Developer\github\Dirac_claude
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

### 0.4g STATE 2026-10-07 (new session, no cache)

New session 9e0a6725 (the old session's cache is gone).  User order of 2026-10-07 done first: `provenance/dirac matrices.md`
(commit fdba6bb) - the author's eight REAL 16 x 16 Dirac matrices, obtained by evaluating the author's own input cells of the
`.nb` in a fresh kernel (`provenance/dirac_matrices/extract_from_author_notebook.wls`), proved by
`provenance/dirac_matrices/build_dirac_matrices_md.py` (35/35 exact checks: real, Cl(4,4) anticommutation, S^AB = [G_A,G_B]/4
span spin(4,4) ~ so(4,4), exponentials = products of two unit vectors generating Spin_0(4,4); with Gamma_0 and Gamma_4 all four
components of Pin(4,4)); displays the 8 matrices, sigma16, T16A[8], the 28 pair products, all 256 products, P_L, P_R.
CORRECTION (audit finding 16, 2026-10-08): it is NOT true that every gamma source equals them - the Revision a4 engine
(FieldEquationsA4.wl and its Python twin) uses an equivalent Cl(1,1)^(x)4 basis until the a4 patch (0.4k) is applied; the regenerated
file measures this and answers 'Instruction followed: not completely' until then, 'yes' after the patch.  Test `tests/test_dirac_matrices_provenance.py`; verified from a fresh clone.
Then both workflows were RELAUNCHED from scratch with SP of this session: textbook run wf_bf3a3e31-ec0, execution provenance
run wf_f856ecb5-265 (agents inspect and finish the existing partial files).  After them: Revision wave 1b, then wave 2.
Also RUNNING: `Revision/workflows/dirac_matrices_audit.js` (run wf_5ccefead-ea3): adversarial audit of `provenance/dirac matrices.md`
(notebook fidelity incl. later redefinitions and stored Out cells; the mathematics incl. the Pin(4,4) argument; COVERAGE of every
gamma-matrix source in the repository incl. Rust and .nb; fresh-clone reproducibility), two skeptics per finding, one fixer owning
provenance/dirac_matrices/*, the .md and its test, then a fresh-clone verifier.  If lost: relaunch with the new SP.
Also RUNNING (user 2026-10-07: "continue with all stages, do not stop"): Revision wave 1b followed automatically by wave 2,
chained in `Revision/workflows/revision_wave_1b_then_2.js` (run wf_987b1061-79b; set SP in the session copies of
revision_wave_1b.js, revision_wave_2.js and the chain script, and copy wave1_review_and_fix.json to <SP>/w1_args.json).
Both wave scripts now carry a CONCURRENCY NOTE: never edit Revision/textbook/, the textbook test, provenance/, notebooks/, tests/
while the other workflows run; pdf-specifications.json is shared (re-read before any change).
DONE 2026-10-07 (was: LEAD DECISION PENDING): the runner of old-primordial found that scripts/verify_dirac16complex_primordial.wls does not
check that wolfram/Dirac16ComplexPrimordial.wl loaded and that D16PRun returned an Association: with the package missing, checks
is not an Association, Count[Values[checks], False] = 0 and the script can exit 0 after writing a garbage report (false success).
FIX IT (after the execution-provenance chain for old-primordial has finished, to avoid a concurrent edit): fail with an ERROR line and
exit 1 unless AssociationQ[result] && AssociationQ[result["checks"]] && Length > 0, and count every non-True check as failed;
then re-run the set twice in a fresh clone (byte identity of both outputs) and update its provenance file.
  -> FIXED by the lead: package-existence check, AssociationQ guard on D16PRun's result, ERROR + exit 1 when an output cannot be
  written, every non-True check counted as failed.  Two runs: 126/126, both outputs identical between runs; primordial-components.json
  byte-identical to the committed file; the report changes only in the script's own sha256 (919928...->f49606...).  Missing package ->
  ERROR, exit 1; unwritable output -> ERROR, exit 1.  The Stage-2 publication pins that sha: provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md
  updated, .tex/.pdf rebuilt with --register (38 pages, 11/11; register and verify builds byte-identical), test pins updated;
  tests/test_d16c_primordial{,_publication}.py 53/53.  The set's provenance file is updated by the execution-provenance fixer of
  old-primordial (it re-verifies against the fixed script).
LEAD DECISION PENDING (2026-10-07, from the dirac-matrices audit, coverage lens): Revision/field_equations_a4/wolfram/FieldEquationsA4.wl
(FEsig1/FEeps/FEGen/FEGammaFrame, lines 119-128) builds its OWN real 16x16 Cl(4,4) basis Cl(1,1)^(x)4 and never reads
Revision/algebra/gammas.json; check_field_equations_a4.py runs its primary checks on a third basis own_rep().  Both are real 16x16
Cl(4,4) sets equivalent to the author's T16 (intertwiner dim 1, K^T K = 2 I16) and a4-equations.json holds only representation-
independent coefficients, but SPEC section 2 requires the author's T16.  FIX (after the execution-provenance chain for rev-a4 has
finished): make both use the author's matrices from gammas.json as the PRIMARY representation, keep the tensor bases only as labelled
comparison representations with an explicit equivalence check; re-run both verifiers twice in a fresh clone; a4-equations.json must stay
byte-identical (any change explained); update Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md; regenerate
provenance/dirac matrices.md (its coverage section).
  PREPARATION RUNNING: `Revision/workflows/a4_author_gammas_prep.js` (run wf_da94d8ca-701) makes and verifies this change in a
  SCRATCH clone only and writes <SP>/a4prep/a4_author_gammas.patch (implementer, two adversarial reviewers, fixer, fresh-clone
  verifier).  Apply the verified patch to the repository once the execution-provenance chain of rev-a4 has finished.
  ALSO in this change (rev-a4 runner, 2026-10-07): verify_field_equations_a4.wls exits 0 when an output cannot be written and never
  finishes when its package is missing - make both an ERROR line with exit code 1 (keep the committed output bytes identical); README
  says 'about 15 s' (measured 19-34 s on a loaded machine).
FRESH-CLONE TEST RESULT (2026-10-07, clone of a4c5eda, no setup_solver.sh): python -m unittest discover -s Revision/tests: 82 tests,
every failure (25 F + 1 E) is in test_universes_in_pairs_textbook (book in progress; the textbook workflow rebuilds it); everything
else passes.  python -m unittest discover -s tests: 615 tests, 5 failures, all OLD-STAGE and PRE-EXISTING: (1) four
test_d16c_kohn_sham_notebook.TestCommittedReport tests - the committed artifacts/dirac16complex/kohn-sham/notebook-report.json has
verdict FAILURE since 2026-09-30 (gauntlet rust_vs_reference_{deltaSCF,eigenvalues,particleHole} failed, python_check_report skipped)
and reference-summary.json was regenerated after it (33c07a3): old Stage 4 was paused unfinished when the Revision replaced it;
(2) test_d16c_student_guide_publication path studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe - exists
only after bash scripts/setup_solver.sh.  The execution-provenance agent nb-kohn-sham must document (1) truthfully; decide with the
user whether old Stage 4 is to be finished or formally marked superseded by Revision/kohn_sham.
CROSS-WORKFLOW SYNC OBLIGATIONS (2026-10-07; must be done before any stage is declared complete):
  (1) wave 1b's Mermin repair (ks-mermin-fix: solver 42/42, determinism 14/14, Mermin roots 5/5, KS theory python 58/58, wolfram 46/46,
      cross-check 29/29) added a 58th KS-theory check: Revision/docs/PAIR_CREATION_PROOFS.md line 492 and .tex line 702 still say 57 ->
      update to 58, rebuild + re-register the PDF (Revision/pdf-specifications.json), re-pin MARKDOWN_SHA256/TEX_SHA256 in
      Revision/tests/test_pair_creation_proofs_publication.py; also list check_ks_source_conditions.py before check_ks_theory.py in its
      section 10 (new run-order dependency).  Owner: wave 1b's fix phase; verify it is done.
  (2) The thermal Kohn-Sham outputs changed (mu moved by up to 8.3e-10 in three N8 T10 states; new last column of thermodynamics.csv;
      larger mu_rounding_bound): textbook notebooks 15a, 15d, 16a, 19a read them -> after wave 1b/2 have finished, rebuild every textbook
      notebook whose Revision inputs changed and re-run nbkit --check; rebuild the book.
  (3) Revision/kohn_sham/theory/check_ks_theory.py changed: re-check that Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md records no
      stale hash of it; likewise every provenance file must be re-checked against the final state of the files it hashes (the index step).
INCIDENT (2026-10-07): the execution-provenance runner of old-nb-build-ks ran `winget show --accept-source-agreements` to read
package versions; if the winget source agreements were not yet accepted on this machine, that accepted them without the user's
permission.  Reported to the user.  Every workflow script in Revision/workflows/ now carries a rule forbidding the acceptance of any
agreement/licence/EULA (effective for future launches; the prompts of already-running runs cannot be changed).

### 0.4j RESTARTED 2026-10-07 20:35 (user: "continue, resume, restart --accept-source-agreements. continue all stages and do not stop")

The user approved the winget source agreements that an agent had accepted (the rule that agents never accept agreements stays).
Restarted from the 0.4i kit in the same session (SP = <session scratchpad>/restart; the a4 prep's partial scratch clone was carried over
and fast-forwarded): textbook_restart wf_a71f212d-1cf, execution_provenance_restart wf_148a1d48-af6, dirac_matrices_audit_fix_restart
wf_7dd6d253-9cf, revision_wave_1b_restart_then_2 wf_2b4c1c8c-a30, a4_author_gammas_prep wf_e7ec46e7-1bf.  If these are lost: merge
their journals into Revision/workflows/state_restart/ with merge_state.py (add these run ids) and regenerate the restart scripts.

### 0.4l FINAL STATE 2026-10-08 (user stopped all work; Claude handed over)

User, 2026-10-08: "NEVER wait more than 60 seconds ... KILL ALL OF THESE RIDICULOUSLY LONG AGENT JOBS ... push everything and verify
repo, and QUIT. GPT-5.6 will take over."  All workflows were stopped (TaskStop) and every agent process was killed (0 left).  Work
committed and pushed.  `.claude/ALLOW_STOP` exists (delete it to re-enable the Stop hook).  Lesson for the successor: the agent
tasks were posed far too large (single agents ran for hours); split work into small, checkable steps and never block on long waits.

DONE AND VERIFIED
* `provenance/dirac matrices.md` (user order of 2026-10-07): generator `provenance/dirac_matrices/build_dirac_matrices_md.py`,
  extractors `extract_from_author_notebook.wls` (the author's own cells, in the author's In[n] order) and
  `extract_repository_wolfram_gammas.wls`; 66/66 exact checks; adversarial audit complete (23/23 confirmed findings fixed; independent
  fresh-clone verifier: 5 MINOR findings left, listed in `Revision/workflows/state_restart/dirac_audit_verify_findings.json`).  It
  answers measured: "Instruction followed: not completely" - every calculation uses eight real 16x16 Cl(4,4) matrices and all but
  the Revision a4 engine use the author's T16 entry by entry; the a4 engine uses an exactly equivalent Cl(1,1)^(x)4 basis.  With the
  a4 patch applied (below) a scratch rerun gave 67/67 and "yes".
* Primordial verifier false-success fix (b980c80), verified from a fresh clone; its provenance file updated by its fixer.
* Execution provenance, sets fully through runner -> independent verifier -> fixer: rev-algebra, rev-ks-theory, rev-pairing-ks,
  rev-pairing, rev-theory, rev-gkd-notebook-reading, old-nb-build-dark, old-nb-build-ks, old-nb-verify-dark, old-nb-verify-ks,
  old-algebra, old-geometry, old-primordial, old-kohn-sham, old-00, old-pairing, old-matter-antimatter, nb-dark-sector, handoff-probes.

NOT DONE / IN PROGRESS (partial edits are committed and UNVERIFIED)
* Execution provenance: rev-gkd-verification - its verifier found a MAJOR false-success defect (verify_lovelock_gkd.wls exits 0 /
  SUCCESS when it cannot write the report) and wrong temp-file text; NOT fixed.  nb-kohn-sham - verified (9 minor), not fixed; the
  old Stage-4 notebook's gauntlet fails 2/60 by design (old Stage 4 unfinished: user decision pending - finish or mark superseded by
  Revision/kohn_sham).  rev-a4 - fix HELD for the a4 patch.  The index provenance/EXECUTION_PROVENANCE_INDEX.md and
  tests/test_execution_provenance.py were NOT written.  All findings: state_restart/state_execution_provenance.json + journals.
* a4 author-T16 patch: `Revision/workflows/a4_patch/a4_author_gammas.patch` is ready, reviewed (2 reviewers) but NOT applied.  Apply it
  only together with the downstream list of section 0.4k (three Revision publications + PDFs + test pins, Revision/README.md table,
  the rev-a4 provenance file, dirac matrices.md regeneration, textbook chapters 00/09/12/17 and notebooks 00c/09c/12a/17b).  A
  prepared workflow for the Revision part: Revision/workflows/restart/a4_apply_sync.js (too large as one run - split it).
* Textbook "Universes in Pairs": ASSEMBLED 2026-10-08 (Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md, assemble_textbook.py 13/13
  checks, chapters 00-23, 89 notebooks, 556 figures; chapter 23 is a marked PLACEHOLDER; .tex generated; PDF build: see the commit log).
  Every chapter's notebooks are built (00-22); chapter texts exist for 00-22 (chapter 21's text WAS written, 4891 lines, by the
  interrupted writer - not yet reviewed); adversarial reviews done for 00-10 and 12-16 with findings (several major: overclaims in 08, 10, 14; physics wording
  in 03, 05, 09, 13; numbers not asserted in 12; figure caption in 16); only chapter 04's fixer finished.  The six-lens book review and the book fix were NOT done.  Revision/tests/test_universes_in_pairs_textbook.py fails.
* Revision wave 1b: the Mermin-root repair is done and verified (solver 42/42, determinism 14/14, KS theory 58/58, cross-check 29/29).
  NOT done: theory-reconcile (partial edits may be in Revision/theory), the full KS cross-check, the reproduction gate, review, fix.
  Wave 2 NOT started.  Known failing test: test_pair_creation_proofs_publication (document quotes 57 KS-theory checks; the record has 58).
* Cross-workflow sync obligations: section 0.4h/0.4k lists (textbook notebooks reading changed KS outputs; provenance hashes).

### 0.4k A4 AUTHOR-T16 PATCH READY (2026-10-08 04:40; implementer of wf_e7ec46e7-1bf; its reviewers/verifier still running)

Patch <SP>/restart/a4prep/a4_author_gammas.patch (896 lines, sha256 7af48ee9..., 7 files under Revision/field_equations_a4/):
both engines take the author's T16 from gammas.json as the primary representation (strict reading; ERROR + exit 1 for every
malformed-fixture case, a missing package, an unwritable output); Cl(1,1)^(x)4 / own_rep kept only as labelled comparison
representations with exact intertwiner checks (dim 1; K^T K = 2 I16 resp. 8 I16; K C = C_T16 K) and the representation-independence
check.  a4-equations.json BYTE-IDENTICAL.  Wolfram 47 -> 52 checks, Python 61 -> 63, all pass, none removed.
APPLY it only together with ALL downstream updates, in one sync workflow, after the textbook chapter stages of 09, 12, 17 are done:
 (1) Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md (+tex/pdf): witness S = 51200, 28800, 51200 in the author's T16 (204800, 115200,
     204800 was the Cl(1,1)^4 normalisation; |v|^2 = 200 vs 400; w = {4,3,4} and S != 0 unchanged); index line 823: wolfram-a4 52,
     python-a4 63; Revision/tests/test_dirac16complex00_field_theory_publication.py line 476.
 (2) Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md line 17 (+tex line 47): 'Wolfram: 52 of 52; sympy: 63 of 63'.
 (3) Revision/docs/PAIR_CREATION_PROOFS.md lines 489-490 (52, 63) and line 492 (KS theory 58); section 10 run order.
     Rebuild + re-register each PDF (Revision/pdf-specifications.json), re-pin MARKDOWN_SHA256/TEX_SHA256 in the three tests.
 (4) Textbook: chapter 12 line ~757 (63 and 52); chapter 09 near line 2786 + notebook 09c (witness S; common factor 40000 instead of
     160000); 17b PROVENANCE counts; rebuild and nbkit --check every notebook that reads the a4 reports (00b, 00c, 02c, 03b, 09a, 09c,
     12a-12d, 17a, 17b, ...).
 (5) Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md (the HELD rev-a4 fix: new hashes, 52 checks, ERROR exits, run
     times 43-70 s, plus its verifier findings under verify:rev-a4 in state_execution_provenance.json).
 (6) Regenerate provenance/dirac matrices.md with its builder (the a4 engine then uses the author's T16).
 Open, out of scope of the patch: check_field_equations_a4.py ends with a traceback (not an ERROR line) when a report cannot be written.
 ADDED by the patch reviewers (2026-10-08): Revision/README.md line ~113 (a4 report counts; textbook notebook 00c asserts this table);
 DIRAC16COMPLEX00 doc rows ~786, 854, 860-861 must cite the author-T16 checks as primary evidence; a sentence that S depends on the
 null-vector normalisation; the rev-a4 provenance file's supplementary script must use FEGammaFrameComparison.  TEXTBOOK PART (run only
 after the textbook fixers of chapters 00, 09, 12, 17 are done): rebuild notebooks 00c (+figures), 09c, 12a, 17b and every notebook reading
 the a4 reports; chapter 00 lines ~1596 and ~3056 (947 / 382 / 458 totals); chapter 09 line ~2786 (record uses T16; factor 40000);
 chapter 12 line ~757 (63, 52); 09c prose 'own (equivalent) representation' -> the author's T16.
 SYNC WORKFLOW (Revision part): Revision/workflows/restart/a4_apply_sync.js (set SP); launch after the a4 prep and the dirac audit verifier finish.

### 0.4i RESTART KIT - PAUSED 2026-10-07 20:30 BEFORE A SESSION LIMIT

User, 2026-10-07: "pause NOW before session limit; push all and check repo; prepare to restart after a session limit; continue all
stages and do not stop".

State at the pause: ALL workflows were stopped (TaskStop) and every agent process was killed and checked (0 Wolfram, Python or Rust
processes left).  Everything is committed and pushed.  `.claude/ALLOW_STOP` exists: delete it on restart so that the Stop hook
works again.  The finished results of every run are in `Revision/workflows/state_restart/state_<family>.json` (families textbook,
execution_provenance, dirac_audit, wave_1b_2, a4_prep), plus `audit_confirmed.json` (the 23 skeptic-confirmed audit findings).
Agents stopped mid-task left partial, committed, UNVERIFIED edits; the restart scripts tell their agents to inspect and finish them.

RESTART (same conversation or a new session).  Do these steps in one go, then never end the turn while stages run.
1. `cd D:/Developer/github/Dirac_claude && git pull && rm -f .claude/ALLOW_STOP`
2. Copy `Revision/workflows/restart/*.js` and `Revision/workflows/restart/next_event.py` to the session scratchpad <SP>, and set SP
   in every .js file: `for f in <SP>/*.js; do sed -i "s|<SCRATCHPAD OF THE RUNNING SESSION>|<SP>|" "$f"; done` (keep ROOT; LF).
3. Launch with the Workflow tool (scriptPath = the <SP> copy), all five at once:
   a. `textbook_restart.js`: notebooks of chapters 11 and 21; writers of every chapter except 02 and 12; reviewers and fixers of all
      chapters; assembly; the six-lens book review with skeptics; book fix; fix verifier.
   b. `execution_provenance_restart.js`: fixers of the 13 verified-but-unfixed sets, the runner of nb-kohn-sham, the verifiers of
      handoff-probes, old-nb-verify-ks, rev-gkd-verification and rev-theory; rev-a4's fix stays HELD (step 4); then index and test.
   c. `dirac_matrices_audit_fix_restart.js`: one fixer for all 23 confirmed findings, then a fresh-clone verifier.
   d. `revision_wave_1b_restart_then_2.js` (it loads <SP>/revision_wave_1b_restart.js and <SP>/revision_wave_2.js): wave 1b from
      theory-reconcile on (the Mermin fix and the wave-1 fix verifier are done), then wave 2.
   e. `a4_author_gammas_prep.js`: the a4 author-T16 patch in a scratch clone, reviewed and verified, written to
      <SP>/a4prep/a4_author_gammas.patch.
4. LEAD ACTIONS while they run.  When (e) is verified: apply the patch to the repository, re-run both a4 engines
   (a4-equations.json must stay byte-identical), commit; then run one agent to update
   Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md (the held rev-a4 fix, including its verifier findings under key
   verify:rev-a4 in state_execution_provenance.json); regenerate `provenance/dirac matrices.md` with its builder; re-check textbook
   chapters 12 and 17 against the new a4 report counts.  Then the CROSS-WORKFLOW SYNC OBLIGATIONS recorded below (pair-creation
   count 57 -> 58; textbook notebooks that read changed Kohn-Sham outputs; provenance hashes).
5. Stay in the turn: `python <SP>/next_event.py 540 <session dir>/subagents/workflows` blocks until any agent finishes and prints
   its result; act on each result; commit and push a snapshot about every 15 minutes (the Stop hook does not run while the turn
   continues).
6. After another session limit: do NOT rely on resumeFromRunId for pipelined workflows (on 2026-10-07 it re-ran finished agents).
   Merge the journals into new state files with `Revision/workflows/restart/merge_state.py` (pre-resume results of resumed runs,
   all results of continuation runs; edit its run-id table) and regenerate the restart scripts with `make_restart_scripts.py`.

### 0.4h STATE 2026-10-07 20:15 (after the second session limit)

The session hit its usage limit at about 19:50 (reset 20:00 PDT); every running workflow lost its unfinished agents.  Resuming with
resumeFromRunId re-ran FINISHED agents too (the cached prefix breaks as soon as concurrent calls come back in another order), so the
lead STOPPED the resumed textbook, execution-provenance and audit runs and launched CONTINUATIONS that take the finished results
from the journals (saved in `Revision/workflows/state_2026-10-07/state_<run>.json`, copied to <SP>) and run only unfinished stages:
* `Revision/workflows/textbook_universes_in_pairs_cont.js` - run wf_1964f603-07f (notebooks of ch. 11 and 21; writers of every chapter
  except 02 and 12; reviewers and fixers of all; assembly; book review; book fix).
* `Revision/workflows/execution_provenance_cont.js` - run wf_5cf02970-bb6 (fixers of 13 verified sets, run of nb-kohn-sham, verifiers
  of handoff-probes, old-nb-verify-ks, rev-gkd-verification, rev-theory; rev-a4's fix is HELD until the a4 patch is applied; index).
* `Revision/workflows/dirac_matrices_audit_fix.js` - run wf_ff12b9f0-bb0 (fixer for the 23 skeptic-confirmed findings in
  state_2026-10-07/audit_confirmed.json, then a fresh-clone verifier).
Still running from before (resumed, they re-ran only failed agents): the wave 1b -> wave 2 chain wf_987b1061-79b and the a4 prep
wf_da94d8ca-701.  Lesson: for pipelined workflows never rely on resumeFromRunId after a session limit; write a continuation from the
journal.  The primordial false-success fix is DONE (b980c80, verified from a fresh clone).

### 0.4f STATE 2026-10-03 (after the session limit)

The session hit its usage limit on 2026-10-02 (resets 09:50 America/Los_Angeles); both workflows lost the
agents that were running (textbook 32 of 42, execution provenance 4 of 66).  Both were RESUMED in the same
session with resumeFromRunId (finished agents replay from cache): textbook run wf_4139c503-a3e and execution
provenance run wf_6845510e-6a4.  Snapshot 06c2d25 holds the partial files.  Known and expected until the
pipelines rebuild them: notebooks built before 4fc381d (the run-instruction list fix) fail
test_universes_in_pairs_textbook's three-renderings test.  If a NEW session must take over (no cache):
relaunch both scripts from Revision/workflows/ with the new SP (agents inspect and finish existing files),
then rebuild every textbook notebook with `python Revision/textbook/tools/nbkit.py build <builder>` and
check with `nbkit.py check`.

### 0.4e CURRENT TASK (user, 2026-10-02): the NEW deep-dive textbook "Universes in Pairs"

The user stopped all stages and ordered, first: preserve the original textbook
(`provenance/DIRAC16COMPLEX_TEXTBOOK.*`, never modified) and create an updated, correct, complete,
RE-NAMED teaching textbook (.md/.tex/.pdf) with a complete executed Jupyter notebook for EVERY
example, complete self-contained run instructions just before each notebook's text (and as comments
in the notebook), the deep-dive technique, and many more plots.  Binding spec:
`Revision/textbook/TEXTBOOK_SPEC.md` (honesty rule R3: the pairing theorems are proved; creation and a
solution of the matter-antimatter problem are not - the user was told this on 2026-10-02).
Workflow `Revision/workflows/textbook_universes_in_pairs.js` RUNNING (relaunched 2026-10-02 as run wf_4139c503-a3e after the
user's STOP and error report; spec rules R5 charge conjugation as a MATRIX and R6 a provenance file per notebook added): infra
(nbkit, run instructions, renderer, assembler, pilot) -> 23 chapters pipelined (notebooks -> writer ->
adversarial reviewer -> fixer) -> assembly (chapter 23, ledger, PDF, registration, test) -> six
whole-book review lenses with two skeptics per finding -> fixers -> rebuild -> fix verifier.
Outputs: `Revision/textbook/` (chapters/, notebooks/, notebooks/src/, figures/, tools/,
UNIVERSES_IN_PAIRS_TEXTBOOK.{md,tex,pdf}), test `Revision/tests/test_universes_in_pairs_textbook.py`.
If a restart finds the run gone: copy the script to the new scratchpad, set SP, relaunch; agents
inspect and finish existing files.
ERROR REPORT (user, 2026-10-02): "complex conjugation Psi -> Psi*" is not charge conjugation for real fields - a
MATRIX operator is needed.  Fixed: Revision/lead_checks/charge_conjugation_and_u1.py (12/12): calC_+ = C (sigma16),
calC_- = Gamma C; for real fields the nontrivial real map is Gamma with m -> -m; the quantised field's conjugation
preserving {Psi, Psi^dagger} = B delta is Gamma (mass reversed).  Spec rule R5.
SECOND NEW TASK (same message): test and verify every wolframscript set and every Jupyter notebook and write a
provenance file for each (student instructions, expected output, side effects).  Workflow
`Revision/workflows/execution_provenance.js` RUNNING (run wf_6845510e-6a4): 22 items (8 Revision Wolfram sets,
11 old scripts/*.wls sets, the handoff probes, the 2 notebooks/*.ipynb), each run twice in a fresh clone, documented,
then verified by an independent agent following the provenance file literally, fixed; index
provenance/EXECUTION_PROVENANCE_INDEX.md and tests/test_execution_provenance.py.  The textbook notebooks get their
provenance files from nbkit (R6).
STOPPED for it (resume afterwards, "continue with all stages"): Revision wave 1b (run wf_39a30fcf-75b,
stopped in its Fix phase; commit 667f153 holds the unverified partial edits of fix:science:0; resume
with resumeFromRunId in the same session, otherwise relaunch `revision_wave_1b.js`), then wave 2.

### 0.4d STATE 2026-10-01 (resumed session)

The repository now lives at `D:\Developer\github\Dirac_claude` (drive C: was nearly full).  The workflow
scripts in `Revision/workflows/` carry `ROOT = 'D:/Developer/github/Dirac_claude'` and the `SP` of the
session of 2026-10-01 afternoon; a new session copies them to its scratchpad and sets its own `SP`.

* Wave 1 (`revision_wave_1.js`, run wf_6f22a73c-e62): COMPLETE, commit 70fab64.  19 agents; every stage
  passes its checks; review 27 findings (10 major, 17 minor), all fixed (record:
  `Revision/workflows/wave1_review_and_fix.json`).  Physics corrections of the review: gamma^mu Omega_mu is
  frame dependent (non-triviality stated with its exact scope); the extra-time evolution is Hadamard
  ill-posed; the dirac16complex00 energy is unbounded below; the Kohn-Sham states violate the a4 source
  conditions (x8 dependence, p3 + p_t = 2 p8), so the Kohn-Sham history is a PRESCRIBED BACKGROUND; T3 proved.
* Fresh-clone check of 1c297d6 by the lead: all 12 verifiers exit 0; python-field-theory.json was stale
  (energy_exchange "DISAGREE"); the lead's own sympy derivation: nabla_mu T^mu_x4 gives
  d rho/d x4 = -3 a4' (p3 - p_t), nabla_mu T^mu_x8 gives d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0, all other
  components identically zero (both sides were right; they stated different components).
* Wave 1b (`revision_wave_1b.js`, run wf_39a30fcf-75b, RUNNING): Rust Mermin mu repair (rounding-limited
  in N8_lamm1_a00_T10), prescribed-background label in ks-theory.json, theory comparison verification,
  wave-1 fix verification, FULL-matrix Kohn-Sham cross-check, fresh-clone reproduction gate, two skeptics per
  item, per-area fixers, fix verifier.  It reads `<SP>/w1_args.json` (= the committed record above).
  Checkpoint 2026-10-01 (second pause request): snapshot a9a1b70 adds the full-matrix reference results
  (Revision/kohn_sham/reference/results, 338 files, 24 MB) and the repaired Rust outputs, still under review.
  Lead check 2: `Revision/lead_checks/einstein_gauss_bonnet_a4.py` (15/15).
  Checkpoint 2026-10-01 (pause request): snapshot commit daeb5ba holds its partial work (new
  `solver/src/mermin.rs`, the prescribed-background label in ks-theory.json, the theory comparison edits),
  NOT yet reviewed.  If a restart finds the run gone: relaunch `revision_wave_1b.js` (copy
  `Revision/workflows/wave1_review_and_fix.json` to `<SP>/w1_args.json` first); its agents inspect and
  finish the existing files.
* Lead's independent checks: `Revision/lead_checks/` (10/10; conservation identities, gamma^mu Omega_mu =
  3 H gamma^(x8), negative control with inflating extra times), test `Revision/tests/test_lead_checks.py`.
* NEXT: commit and push wave 1b; then `revision_wave_2.js` (dark sector with stated observer assumptions
  for the time-like extra times, a4 with the Kohn-Sham source starting from the source-condition
  violation, T3 verification and numerics, documents, notebooks, gate, five-lens review with skeptics).

### 0.4c CURRENT TASK (user, 2026-10-01, later): `Revision/` - a new, separate record

The author asked for a completely new record, in the new folder `Revision/`, of new calculations for the
author's primordial metric (x8 hidden, x4 time, x5..x7 deflating extra times): both Lagrangians with the
canonical spin connection, non-triviality tests [1] and [2], field equations, EMT operator, KE, PE,
pressure, energy density, EoS, canonical quantisation in 4+4, the field equations for a4[x4]
(Einstein-Lovelock with the GKD Lovelock tensors), Kohn-Sham ground and first excited states, the two
dark-sector hypotheses against the Unite values of the private PDF, the pairing proofs, md/tex/pdf.
Binding: `Revision/SPEC.md`; task verbatim in `Revision/README.md`.  NOTHING from the old stages is
mixed in.  The GKD work was moved into `Revision/gkd_lovelock/` (git mv).

### 0.4b CURRENT TASK (user, 2026-10-01): GKD and the Lovelock tensors (the user's test)

The user found the Lovelock treatment deficient and set a test: refactor the author's kδ
(`kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]`, notebook
`Generalized _Kronecker_Delta_4+4.nb`, now tracked at the user's request; `Generalized_Kronecker_Delta.*`
is ignored) into a pure-Rust `GKD`, use it to compute, with provenance, the three non-zero Lovelock
tensors of Lovelock's (4.38) (the user's In[68], an image cell) for the user's 8x8 test metric (x8 hidden,
x4 time, x5..x7 deflating extra times), write every component, PROVE the work was done here without
reading the user's answers, with student instructions, Jupyter notebooks (rustSolveIt style), md/tex/pdf.
DONE by the lead: `studies/lovelock_gkd` (GKD with proof, exact Laurent-polynomial engine, curvature,
Lovelock sums), outputs `artifacts/lovelock-gkd/` (19/19 checks; GKD = literal determinant on all
16,777,216 length-4 pairs; two runs byte-identical), committed BEFORE any comparison (commit 3e81eeb,
2026-10-01 07:15) with `PROVENANCE_OF_THE_COMPUTATION.md`.  RUNNING: `handoff/workflows/wf_lovelock_gkd.js`
(independent sympy checker, Wolfram GKD = kδ check, Jupyter notebook, provenance/LOVELOCK_GKD.*, reviews,
fixer).  NEXT: commit; THEN, in a separate commit, compare with the author's answers (convention-aware)
and add that section; then integrate the Lovelock tensors into Stage 2 / the textbook (ledger L25) and
resume 0.4a.

### 0.4a NEW TOP PRIORITY (user, 2026-09-30 ~18:40): the deflating extra times

The user: "x5, x6, x7 are the three extra times that exponentially deflate. Fix this everywhere
they appear, and fix your docs and provenances"; asked, the user chose "Redo the physics".
Binding: `handoff/specs/DEFLATION_SPEC.md` (a4 = A t for all t, A = 1, 2; EXP-1 without the
window, EXP-2 from the notebook's deflation, EXP-3/EXP-4 with exponentially deflating extra
times, Stages 4/5 as instantaneous (adiabatic) Kohn-Sham states along a4 = A H x4 with an
adiabaticity analysis, TDDFT OPEN; every document and the textbook updated).  State: the spec is
written (commit 2e02e5e) and under adversarial review (physics, faithfulness, feasibility;
`handoff/workflows/wf_deflation_spec_review.js`, read-only reviewers; it was still running at the
pause of 2026-10-01 ~00:00 - after a restart rerun it, amend the spec with the confirmed findings,
commit); then write and run the implementation workflows of DEFLATION_SPEC D14.  Feasibility
checked by the lead: the Kohn-Sham crate (geometry.rs, shooting.rs, runs.rs) and the reference
solver already take a4_0 != 0 and check the E4.10 rescaling identity, so the slice series of D8
reuses them via a new `deflating` subcommand.  The textbook built before this
correction (671 pages, commit 4ede502) describes the static/frozen/window models and must be
updated by D12.  Sections 0.4 A-E below describe the state before the correction and remain
the to-do list for the parts the correction does not replace.

### 0.4 State at the pause of 2026-09-30 15:05 and the exact order of work

The user's priority (2026-09-30 12:10): the TEXTBOOK first, then the other stages.

A. Textbook (`handoff/specs/TEXTBOOK_SPEC.md`; chapters in `provenance/textbook/chapters/`).
   * Chapters 00-05, 08-13: written and adversarially reviewed (198 findings, skeptic-
     verified, fixed; `handoff/workflows/wf_textbook_wave_a_review.js`); cross-chapter
     items the per-chapter fixers could not apply: `handoff/reviews/textbook_wave_a_carryover.json`.
   * Chapters 06, 07, 14, 15, 16, 17, 18: written, reviewed and fixed
     (`handoff/workflows/wf_textbook_wave_b_chapters.js`).
   * 18:28 (pause): `wf_textbook_final.js` phases Carry-over, Ledger and Assembly DONE: the book
     `provenance/DIRAC16COMPLEX_TEXTBOOK.{md,tex,pdf}` is assembled (21 chapters, 350 sections, 3610
     references resolved), the PDF is 671 pages, warning-free, byte-identical in two builds, numbered
     from 0, registered (`provenance/pdf-specifications.json` entry dirac16complex-textbook), pinned by
     `tests/test_d16c_textbook_publication.py`.  RUNNING at the pause: the nine whole-book review
     lenses; then skeptics, per-chapter fixers and the rebuild.  After a restart: rerun
     `wf_textbook_final.js` from its Review phase (comment out the Carry-over, Ledger and Assembly
     agents, or let them re-check: they only fix what they find), then push.
   * 15:55: chapters 19 and 20 written, reviewed and fixed; the whole book (21 chapters) passes
     `python scripts/build_textbook.py --check` (12/12); `wf_textbook_final.js` launched (run
     wf_0b6d5db2-c76).  If a restart finds it unfinished: rerun `wf_textbook_final.js` (its agents
     inspect and finish partial work).  The notes below are kept for reference.
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
   (the pairs checker scripts/check_dirac16complex_pairs.py on the partial outputs gave 71 checks,
   8 failed, at 15:10 - expected while the runs are incomplete)
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
