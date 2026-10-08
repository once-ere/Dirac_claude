export const meta = {
  name: 'stage5-documents-review-v2',
  description: 'Old Stage 5 (2026-10-08 completion): the two provenance documents, the Stage-5 gate, four adversarial review lenses, two skeptics per finding, one fixer and a fix-verifier',
  phases: [
    { title: 'Documents and gate', detail: 'DIRAC16COMPLEX00_FIELD_THEORY, DIRAC16COMPLEX_PAIR_CREATION (with figures), verify_stage5_pair_creation' },
    { title: 'Review', detail: 'proof rigour, physics, numerics, reproducibility' },
    { title: 'Skeptics', detail: 'two independent refutation attempts per finding' },
    { title: 'Fix', detail: 'one fixer for the confirmed findings, then an adversarial fix-verifier' },
  ],
}
// Revised from wf_stage5_docs_review.js (2026-09-30) for the completion of 2026-10-08: repository on D:, the errata
// E5.1-E5.3 of handoff/specs/STAGE5_SPEC.md section 9 are binding, old Stage 4 is being completed by the lead at the
// same time, a lock serialises the registrations, and every review finding must survive two skeptics.
const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
const ART = 'artifacts/dirac16complex/pair-creation'
const LOCK = `${SP}/stage5_tmp/registry.lock`

const COMMON = `
NEVER accept licence terms, source agreements or any other agreement (no --accept-source-agreements / --accept-package-agreements, no wolframscript -activate).
CONTEXT: repository ${ROOT} (git, branch main; do NOT commit, push, or run git commands that change the index or working tree; the lead commits). Old Stage 5 of the dirac16complex project. BINDING: ${ROOT}/handoff/specs/STAGE5_SPEC.md (task, honesty rule, theorems; section 9 errata E5.1 quantum reading of the T1 corollary - no cancellation between two independent quantised universes; E5.2 Rust y-grid uncertainty per member; E5.3 the deterministic guard of the reference pairs runs), ${ROOT}/handoff/specs/STAGE5_DOC_OUTLINE.md (document structure), ${ROOT}/handoff/specs/CONTRACT.md (section 11 errata), ${ROOT}/handoff/specs/STAGE4_SPEC.md (sections 8-9). The Stage-5 exact theory and numerics are FINAL: Wolfram wolfram/Dirac16Complex00.wl, wolfram/Dirac16ComplexPairing.wl with scripts/verify_dirac16complex00.wls (if present) and scripts/verify_dirac16complex_pairing.wls; sympy scripts/check_dirac16complex00.py (if present), scripts/check_dirac16complex_pairing.py; numerics: the pairs subcommand of studies/dirac16complex_kohn_sham, scripts/ks_reference_solver.py with scripts/ks_reference_pairs.py, the checker scripts/check_dirac16complex_pairs.py; all reports and outputs under ${ROOT}/${ART}/ (read every report before writing; never re-run the long numerics yourself).
CONSISTENCY: the later Revision record (Revision/, binding Revision/SPEC.md) answers the pair-creation request in Revision/docs/PAIR_CREATION_PROOFS.md section 11.3, and the matter-antimatter record provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md section 7.3 gives the Krein reading: the Stage-5 documents must not contradict them; where Stage 5 and the Revision record differ in scope (old Stage-2/4 frame versus the author's coordinates x1..x8 with the exponentially DEFLATING extra times x5..x7), say so explicitly.
OLD STAGE 4 IS BEING COMPLETED BY THE LEAD AT THE SAME TIME: never touch artifacts/dirac16complex/kohn-sham/**, scripts/ks_reference_solver.py, scripts/check_dirac16complex_kohn_sham.py, notebooks/*kohn_sham*, provenance/DIRAC16COMPLEX_KOHN_SHAM_*, tests/test_d16c_kohn_sham*. Never modify dirac-main/, vendor/, the author's .nb notebooks, provenance/DIRAC16COMPLEX_TEXTBOOK.* or provenance/textbook/.
Tooling: WolframScript 1.14 drops arguments after "--"; Python 3.14 (numpy, sympy, mpmath, matplotlib; no scipy); pdflatex (MiKTeX); PDFs only via python scripts/build_provenance_pdf.py <md> [--register] (read its header and the Markdown subset of scripts/build_dissertation_tex.py, which supports figure lines ![caption](path.png)); provenance/pdf-specifications.json is shared between the two document agents: hold the lock directory ${LOCK} (mkdir; retry every 10 s, each wait at most 60 s) around every --register, re-read the registry immediately before and change only your entry. User rules: never wait more than 60 s in one foreground command (run longer things detached with a done marker); aim to finish within about 45 minutes, else stop at a consistent verified state and list what remains; append one line per step to ${SP}/stage5_tmp/<your label>.progress.md. HONESTY: numbers only from the committed reports; theorems stated with their exact hypotheses; interpretation labelled as such; never write "proved" for anything not proved; nothing about the creation of universes is proved (no creation process, rate, amplitude or wave function). Large files in chunks of at most 300 lines per tool call. Scratch only under ${SP}/stage5_tmp/<your label>/.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }

phase('Documents and gate')
const firstWave = await parallel([
  () => agent(`${COMMON}
TASK (document A). Own: provenance/DIRAC16COMPLEX00_FIELD_THEORY.md, .tex, .pdf, its entry in provenance/pdf-specifications.json, tests/test_d16c_stage5_field_theory_publication.py. Write document A of STAGE5_DOC_OUTLINE.md completely (every section; every formula as verified in the reports; every number from them), build the PDF (verify mode until warning-free), register it, pin it in the test following tests/test_d16c_primordial_publication.py, run the test.`, { label: 'doc-field-theory', phase: 'Documents and gate', schema: RESULT }),
  () => agent(`${COMMON}
TASK (document B). Own: provenance/DIRAC16COMPLEX_PAIR_CREATION.md, .tex, .pdf, its entry in provenance/pdf-specifications.json, figures under ${ART}/figures/ (deterministic matplotlib, Agg, metadata Software None, generated by a script you own: scripts/build_dirac16complex_pairs_figures.py), tests/test_d16c_stage5_pair_creation_publication.py. Write document B of STAGE5_DOC_OUTLINE.md completely: the theorems with full proofs (as verified), the KS model of both fields, the numerical demonstration with tables and figures (the runs the guard of E5.3 stopped and the controls that both solvers refuse are reported as such, with their recorded reasons; no invented numbers), the verification records (the pairs checker report), reproduction commands, and an explicit final section separating what is proved from interpretation (the notebook's hypothesis quoted). Cite and reconcile the Stage-1 statement (provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md, summary item 6 and Section 7.7: the chirality pairing is 'a structural property of the equations, not a claim that universes of masses +-M are created in pairs'): say precisely what Stage 5 adds (the pair corollaries and the KS-level results, with their hypotheses, read per E5.1) and what remains unclaimed (a creation rate, amplitude or wave function). Build the PDF (verify mode until warning-free), register it, pin it, run the test.`, { label: 'doc-pair-creation', phase: 'Documents and gate', schema: RESULT }),
  () => agent(`${COMMON}
TASK (gate). Own: scripts/verify_stage5_pair_creation.ps1, scripts/verify_stage5_pair_creation.sh, scripts/verify_stage5_pair_creation_audit.py (if needed), tests/test_d16c_stage5_gate.py. Write the Stage-5 gate twins following the Stage-3 gate pattern exactly (tool resolution, run_logged, snapshot audit of committed paths, re-exec under PowerShell 7, never two gates at once, a step whose wolframscript prints 'Failed to open file' fails even with exit code 0, final line stage5_pair_creation_verification=OK): the two Wolfram verifiers (optional when wolframscript is absent, stated), the two sympy checkers, cargo fmt/clippy/test/build of the crate, the Rust pairs subcommand into build/ with byte comparison against the committed ${ART}/rust/, the reference pairs runner into build/ (or its checker's reproduction mode if a full run is long; state exactly what is re-run), the pairs checker, the figures script with a byte comparison, both PDFs in verify mode, a committed-unchanged audit, and python -m unittest discover -s tests -p "test_d16c_stage5*.py" -v. Test the scripts on the fast steps (a --steps or --dry-run option like the Stage-4 gate); document the expected wall time per step. Do not run the full gate; the lead runs it from a fresh clone.`, { label: 'gate', phase: 'Documents and gate', schema: RESULT }),
])

phase('Review')
const lenses = [
  ['proof-rigour', 'Check every theorem and proof of document B and every derivation of document A line by line against the Wolfram and sympy reports and re-derive the key steps yourself (the gamma^8 facts, the Lagrangian and EMT relations, the Pin reflection, the block map and the boundary-condition transformation, the expectation-rule signs, the Wick sign of the statistics, the Krein reading of E5.1). Flag any statement called proved that is not, any hidden hypothesis, any sign error, any overclaim about "creation".'],
  ['physics', 'Judge the physics: the definition and status of dirac16complex00, the reality and non-triviality claims, the real restriction versus the notebook, the KS model of the commuting field and its stated status, the meaning of the pair corollaries (zero total energy-momentum versus mirror pairs of equal energy; E5.1), consistency with Stages 1-4, with the notebook (quote cells), with Revision/docs/PAIR_CREATION_PROOFS.md and with provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md.'],
  ['numerics', 'Re-run the cheap parts (the pairs subcommand for a subset into scratch, the reference runner for a subset, the checker), audit every number and figure quoted in both documents against the outputs, and test the pairing identities, the E5.3 guard and the untransformed-BC control yourself.'],
  ['reproducibility', 'From a fresh copy of the working tree in scratch (copy the tree including uncommitted files), run every command the documents give that finishes within about 20 minutes (detached when longer than 60 s), build both PDFs in verify mode, run the fast steps of the Stage-5 gate and the Stage-5 unit tests. Report every failing or ambiguous step.'],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
Documents, gate and code are written. TASK (adversarial reviewer, lens ${k}): ${t} Report only real problems with concrete evidence; do not edit repository files.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log('stage5 findings: ' + findings.length)

phase('Skeptics')
const judged = await parallel(findings.map((f, i) => () =>
  parallel([0, 1].map(j => () => agent(`${COMMON}
TASK (skeptic ${j + 1} of finding ${i}; do NOT edit files): Try to REFUTE this finding by checking it yourself in the files and reports${j ? ' (look for evidence that the text is in fact correct)' : ' (re-derive or recompute the claim independently)'}. Set refuted=true only if the finding is wrong or not a real problem. Finding: ${JSON.stringify(f)}`, { label: `skeptic:${i}:${j}`, phase: 'Skeptics', schema: VERDICT })))
    .then(vs => ({ ...f, refutations: vs.filter(Boolean).filter(v => v.refuted).length }))))
const confirmed = judged.filter(Boolean).filter(f => f.refutations === 0)
log(`confirmed by both skeptics: ${confirmed.length} of ${findings.length}`)

phase('Fix')
let fix = null
let verify = null
if (confirmed.length) {
  const parts = []
  for (let i = 0; i < confirmed.length; i += 12) parts.push(confirmed.slice(i, i + 12))
  fix = []
  for (const [n, part] of parts.entries()) {
    fix.push(await agent(`${COMMON}
TASK (fixer, part ${n + 1} of ${parts.length}). Findings, each confirmed by two skeptics (JSON): ${JSON.stringify(part)}
Re-verify each; fix confirmed ones at their root (regenerate outputs deterministically, rebuild figures and PDFs, register, update pins); reject unconfirmed ones with evidence. Report one line per finding in key_results: FIXED / REJECTED (reason) / NEEDS-RERUN (command).`, { label: `fix:${n + 1}`, phase: 'Fix', schema: RESULT }))
  }
  verify = await agent(`${COMMON}
TASK (fix-verifier; adversarial; do NOT edit files): Findings: ${JSON.stringify(confirmed).slice(0, 40000)}
Fixer reports: ${JSON.stringify(fix).slice(0, 40000)}
For EVERY finding check in the files that the fix is real, correct and complete and broke nothing (rebuild the PDFs into scratch and compare, run the Stage-5 tests and the fast gate steps). Report as findings only what is still wrong.`, { label: 'verify-fix', phase: 'Fix', schema: FINDINGS })
}
return { firstWave, findings, confirmed, fix, verify }
