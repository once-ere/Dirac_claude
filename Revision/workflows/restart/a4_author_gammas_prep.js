export const meta = {
  name: 'a4-author-gammas-prep',
  description: 'Prepare (in a scratch clone only) the switch of the a4 field-equation engine and its Python twin to the author\'s T16 from Revision/algebra/gammas.json; adversarial review; verified patch file',
  phases: [
    { title: 'Implement', detail: 'scratch clone: edit, run both verifiers twice, compare outputs, write the patch' },
    { title: 'Review', detail: 'two adversarial lenses' },
    { title: 'Fix', detail: 'fix confirmed findings in the scratch clone, regenerate the patch' },
    { title: 'Verify', detail: 'apply the patch to a NEW fresh clone and re-run everything' },
  ],
}

const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
const WORK = SP + '/a4prep/clone'
const PATCH = SP + '/a4prep/a4_author_gammas.patch'
const A4 = 'Revision/field_equations_a4'

const COMMON = `
NEVER accept licence terms, source agreements, cookie banners or any other agreement on the user's machine or accounts (e.g. never pass --accept-source-agreements / --accept-package-agreements to winget, never run wolframscript -activate or accept an EULA); if a step needs that, stop that step and report it as an open item for the user.
CONTEXT: repository ${ROOT} (git, branch main; remote https://github.com/once-ere/Dirac_claude.git). You must NOT modify ANY file under ${ROOT}: other workflows are running there (one is right now documenting the CURRENT ${A4} code for its provenance file). All work happens in the scratch clone ${WORK} (create it with: git clone https://github.com/once-ere/Dirac_claude.git "${WORK}" if it does not exist) and under ${SP}/a4prep/. Read-only use of ${ROOT} is fine.
THE DECISION (lead, 2026-10-07; from an audit confirmed by skeptics): Revision/SPEC.md section 2 requires the AUTHOR's real 16 x 16 Dirac matrices T16 (Revision/algebra/gammas.json, gamma in the order x1..x8, eta = diag(+1,+1,+1,-1,-1,-1,-1,+1)). The a4 engine ${A4}/wolfram/FieldEquationsA4.wl builds its OWN basis Cl(1,1)^(x)4 (FEsig1/FEeps/FEGen/FEGammaFrame, lines 119-128; FEC, FESab, FEOmega, FEGammaCoord derive from it) and never reads gammas.json; its Python twin ${A4}/python/check_field_equations_a4.py runs its primary 'ownrep' spinor checks on a third basis own_rep() and the author's T16 only as a secondary run. Both bases are real 16x16 Cl(4,4) sets equivalent to T16 (intertwiner space of dimension 1, K^T K = c I16). TARGET: the AUTHOR's T16 from gammas.json becomes the PRIMARY representation in BOTH engines (FEGammaFrame := the fixture's gamma, read with the same strict parsing as the other Revision Wolfram code - look at Revision/algebra/wolfram/RevisionAlgebra.wl and Revision/theory/wolfram for how they read gammas.json; FEC must equal the fixture's C = sigma16 analogue in x-order); the tensor-product bases stay ONLY as clearly labelled comparison representations, with an explicit exact equivalence check (intertwiner dimension 1 and K^T K = c I) and the representation-independence check of the coefficients kept. Error handling: a missing or malformed gammas.json must give an ERROR line and exit code 1 (never a silent fallback). Never weaken or delete a check; renamed checks must keep their meaning; record measured truth.
OUTPUTS: ${A4}/a4-equations.json must stay BYTE-IDENTICAL (it holds only representation-independent coefficients); if anything in it changes, explain exactly why and treat it as a finding. The reports (wolfram-a4-report.json, python report) may change only by the representation labels and the added checks - list every changed line.
Wolfram: "/c/Program Files/Wolfram Research/WolframScript/wolframscript" (Bash). Read the header of each script for its usage and run time. Python with sympy/numpy installed.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }

phase('Implement')
const impl = await agent(`${COMMON}\nTASK (implementer): In ${WORK}: read Revision/SPEC.md sections 1, 2 and 5, ${A4}/README or headers, FieldEquationsA4.wl and verify_field_equations_a4.wls completely, and check_field_equations_a4.py completely. Make the change described above in both engines. Then run, in ${WORK}: the Wolfram verifier (exactly as its header says) TWICE and the Python checker TWICE; compare ${A4}/a4-equations.json with the committed blob (git show HEAD:${A4}/a4-equations.json | cmp) and the two runs with each other; diff the reports against HEAD and explain every changed line. Also run python -m unittest discover -s Revision/tests -p "test_*.py" -k a4 (or the tests that read a4 outputs) and any test of ${A4}. Finally write the patch: git -C "${WORK}" diff > "${PATCH}" (text, LF). Report the patch path, the check counts before and after, and the byte-identity result.`, { label: 'implement', phase: 'Implement', schema: RESULT })

phase('Review')
const lenses = [
  ['spec-and-checks', `Read ${PATCH} and the changed files in ${WORK}. Verify: the AUTHOR's T16 from gammas.json is now the primary representation in BOTH engines (trace every use of FEGammaFrame, FEC, FESab, FEOmega, FEGammaCoord and of the Python primary checks); the matrices loaded equal provenance/dirac_matrices/author_notebook_T16.json under the map x1..x3 -> T16A[1..3], x4 -> T16A[4], x5..x7 -> T16A[5..7], x8 -> T16A[0]; the tensor bases remain only as labelled comparisons with an exact equivalence check; NO check was weakened, deleted or made vacuous (compare the check lists before/after one by one); error handling for a missing/malformed fixture (try it: rename gammas.json in a COPY of the clone and run both); the comments and documentation in the changed files are accurate; Revision/SPEC.md section 2 is satisfied.`],
  ['reproduction', `In a NEW fresh clone under ${SP}/a4prep/review_clone: git apply "${PATCH}" (it must apply cleanly to origin/main HEAD); run the Wolfram verifier and the Python checker twice each; confirm a4-equations.json is byte-identical to HEAD's and between runs, the reports are identical between runs, run times are reasonable; run the Revision tests that read a4 outputs; check that every consumer of a4-equations.json and of the reports (grep the repository: Revision/lead_checks, Revision/kohn_sham, Revision/textbook/notebooks/src 12a-12d and 17a, Revision/docs) still gets what it expects (report keys/check names they read).`],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}\nTASK (adversarial reviewer, lens ${k}; do not edit ${WORK} or ${ROOT}): ${t}\nReport only real problems with concrete evidence.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log(`a4 prep review: ${findings.length} findings`)

phase('Fix')
let fix = { files_changed: [], commands_run: [], all_checks_pass: true, failing: [], key_results: ['no findings'], open_items: [], summary: 'no findings' }
if (findings.length) {
  fix = await agent(`${COMMON}\nTASK (fixer, in ${WORK} only): Reviewer findings (JSON): ${JSON.stringify(findings).slice(0, 60000)}\nRe-verify each; fix confirmed ones in ${WORK}; reject unconfirmed with evidence. Re-run both engines twice, confirm byte identity of a4-equations.json, regenerate ${PATCH}. One line per finding: FIXED / REJECTED (reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}

phase('Verify')
const verify = await agent(`${COMMON}\nTASK (final verifier; do not edit ${WORK} or ${ROOT}): In a NEW fresh clone under ${SP}/a4prep/verify_clone apply "${PATCH}" (must apply cleanly to origin/main HEAD; if HEAD moved, report whether it still applies), run both engines twice, confirm byte identity of a4-equations.json with HEAD and between runs, confirm the author's T16 is the primary representation in both engines (load it and compare with provenance/dirac_matrices/author_notebook_T16.json), confirm no check was weakened (check lists before vs after), and run the a4-related Revision tests. Report anything wrong as findings; list what you verified in verified_ok.`, { label: 'verify', phase: 'Verify', schema: FINDINGS })
return { patch: PATCH, impl, findings: findings.length, fix, verify }
