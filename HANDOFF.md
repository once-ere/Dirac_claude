# HANDOFF — how to restart this project after a session limit

This file is the complete restart kit.  It is written for a fresh Claude Code
session (or a human) that has none of the previous conversation.  Everything a
restart needs is in this repository; nothing depends on the old session's scratch
directory.

## 0. Exact restart procedure (do this first)

1. Open a terminal in the repository:
   `cd C:\Users\nsh\Developer\github\Dirac_claude`
2. Try to resume the previous conversation first (keeps all context):
   `claude --continue`   (resumes the most recent session in this directory)
   or `claude --resume` and pick the session titled with "dirac16complex".
   In the Claude desktop app: reopen the same session from the sidebar.
3. If resuming is not possible (session limit reached, transcript gone), start a
   NEW session in the same directory and paste this prompt verbatim:

   ```text
   Read HANDOFF.md, then handoff/specs/CONTRACT.md (all sections incl. 11),
   handoff/specs/STAGE4_SPEC.md (incl. section 7), handoff/specs/NUMERICS_CONTRACT.md.
   Git pull first. Continue every unfinished stage listed in HANDOFF.md section 2,
   in order, using the Workflow tool with the scripts in handoff/workflows/ (copy
   each to your scratchpad, set SP to your scratchpad path, keep LF line endings,
   no "--" before wolframscript arguments). Never modify dirac-main/, vendor/ or the
   .nb notebook. Do not stop between stages; commit and push to origin main after
   every completed stage and verify from a fresh clone. Do not take shortcuts.
   ```
4. Before anything else the new session must run:
   `bash scripts/setup_solver.sh` (or `.\scripts\setup_solver.ps1`) to refetch the
   git-ignored solver engine, then `python -m unittest discover -s tests -v`.

## 1. What this repository is

`dirac16complex`: a 16-component complex Grassmann spinor field of Pin(4,4) in 4+4
dimensions.  Stages: (1) arbitrary gravitational field; (2) the notebook's primordial
pair-creation field; (3) dark-sector numerics (five CVODE experiments); (4) Kohn–Sham
DFT ground and first excited states in the primordial field.  README.md gives the
map; provenance/*.md are the documents; artifacts/dirac16complex/* the reports.

## 2. State at the last push (commit noted in git log) and what remains

| Stage | Done | Remaining |
|---|---|---|
| 1 arbitrary field | exact Wolfram + Python verifiers (all checks pass), Grassmann demo, publication tooling, document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{md,tex,pdf}` (41 pp, registered), 4-lens review with fixes applied | run the gate `scripts/verify_stage1_arbitrary_field.{ps1,sh}` to OK; fix anything it reports |
| 2 primordial field | COMPLETE and gated (`scripts/verify_stage2_primordial_field.{ps1,sh}` → OK), pushed | nothing |
| 3 dark-sector numerics | Rust crate `studies/dirac16complex_cosmology` (5 experiments, all checkers pass), Jupyter notebook, Mathematica notebook, figures, builder image support | documents `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` and `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` (may be partially present: check `ls provenance`), their PDFs (`python scripts/build_provenance_pdf.py <md> --register`), 4-lens review, fixes, gate `scripts/verify_stage3_dark_sector.{ps1,sh}` (create if absent, pattern of the Stage-1/2 gates) |
| 4 Kohn–Sham DFT | spec `handoff/specs/STAGE4_SPEC.md`; build phase was running: `wolfram/Dirac16ComplexKohnSham.wl`, `scripts/check_dirac16complex_kohn_sham_theory.py`, `studies/dirac16complex_kohn_sham` (Rust), `scripts/ks_reference_solver.py`, `scripts/check_dirac16complex_kohn_sham.py` — check which exist and pass | whatever is missing from `handoff/workflows/wf_stage4.js` phases Build → Integrate → Notebooks → Documents (`provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.*`, `provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE.*`) → Review → Fix → Gate (`scripts/verify_stage4_kohn_sham.{ps1,sh}`) |
| final | — | README status table; `python -m unittest discover -s tests -v` all green; fresh-clone verification (`git clone` into a scratch dir, run setup_solver, the gates); push |

How to tell what exists: `git log --stat -3`, `ls provenance artifacts/dirac16complex/*`,
`python -m unittest discover -s tests -v`.  Every verifier prints
`check_count`/`failed_check_count`; every gate ends with `stageN_..._verification=OK`.

## 3. Binding conventions (never change silently)

- Counting from 0; `eta = diag(+,+,+,+,-,-,-,-)`; `x4` is time; gammas are the
  notebook's `T16^A` in the split-octonion block basis (exact fixture
  `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`); `C = sigma16`;
  `Psibar = Psi^dagger C`; `B = -i C gamma^4`; `Omega_mu = (1/8) omega_{mu ab}[gamma^a,gamma^b]`
  with `omega_{mu ab} = eta_ac omega_mu^c_b` (the notebook's `omega_mu^a_b S^{ab}` is wrong).
- Lagrangian, field equations, energy–momentum tensor, KE/PE splits, quantization:
  `handoff/specs/CONTRACT.md` sections 5–8 with the errata in section 11.
- Stage-2 corrections: `det g = +cos^2 z`; the condensate CAN source the field for
  `a4'' = 0` (`handoff/specs/STAGE4_SPEC.md` section 7).
- Tooling: WolframScript 1.14 drops arguments after `--` (pass paths positionally);
  PDFs only via `scripts/build_provenance_pdf.py`; outputs deterministic (LF,
  `fmt_e(v,17)`); numbers in documents only from reports.

## 4. Workflow scripts

`handoff/workflows/*.js` are the exact Workflow-tool scripts used.  Each defines
`const SP = ...` (scratch path) and `ROOT`; update `SP` to the new session's
scratchpad.  `wf_stage4.js` covers all of Stage 4 end to end; `wf_stage3_docs.js`
covers Stage 3 documents/review/gate; `wf_stage1_doc.js` the Stage-1 gate.  Agents
find existing files and should skip finished work (tell them so in the prompt).
`handoff/tools/wait_for.py` blocks a turn until a background task finishes (so the
session never returns control while work is running).

## 5. Private inputs (never commit)

`prompt_Dirac_claude*.txt`, the Gmail PDF, `dirac-main/`, `dirac-main_2.zip`,
`vendor/` are git-ignored on purpose.  The task statements are in the ignored
prompt files; their substance is summarised in section 2 above and in the specs.
