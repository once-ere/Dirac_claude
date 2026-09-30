export const meta = {
  name: 'matter-antimatter',
  description: 'Matter and antimatter in the dirac16complex theory: exact theorems M1-M6 (Wolfram + independent sympy), the provenance document, review, fix',
  phases: [
    { title: 'Exact theory', detail: 'Wolfram package + verifier and independent sympy checker' },
    { title: 'Document', detail: 'provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.{md,tex,pdf}' },
    { title: 'Review', detail: 'rigour and honesty lenses' },
    { title: 'Fix', detail: 'apply confirmed findings' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const ART = 'artifacts/dirac16complex/matter-antimatter'

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main; do NOT commit, push, or run git commands that change the index or working tree). BINDING, read fully first: ${ROOT}/handoff/specs/MATTER_ANTIMATTER_SPEC.md (the request, the HONESTY RULE: the statement "the theory solves the matter-antimatter problem" is NOT provable and must not be written as proved; the theorems M1-M6), then ${ROOT}/handoff/specs/STAGE5_SPEC.md (the fields, the Lagrangian L1, T1-T3), ${ROOT}/handoff/specs/CONTRACT.md (section 11 errata E2, E3), the Stage-1 document provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md (current, U(1), chirality map, Pin characters, quantization), the exact fixture artifacts/dirac16complex/arbitrary-field/algebra-fixture.json, and the Stage-5 exact pairing results under artifacts/dirac16complex/pair-creation/ (wolfram-pairing-report.json, pairing-theory.json; they are being produced concurrently - use them if present and final, else say so). Reuse (read only): wolfram/Dirac16ComplexAlgebra.wl, wolfram/Dirac16ComplexGeometry.wl, scripts/d16c_exact.py, scripts/grassmann_algebra.py.
RULES: write only your own files; other agents are concurrently working on Stage 4, Stage 5 and the textbook - never touch their files; never modify dirac-main/, vendor/, the author's .nb notebook. Exact arithmetic (integers, rationals, Gaussian rationals, exact symbolic algebra); every checker prints check_<name>=true|false, measurement_<name>=..., check_count, failed_check_count, exits nonzero on failure and writes a JSON report {schemaVersion, producer, checks, measurements, sourceSha256}; WolframScript 1.14 drops arguments after "--" (pass paths positionally); Python 3.14 (numpy, sympy, mpmath; no scipy); deterministic LF outputs. Chunks of at most 300 lines per tool call. Scratch only under ${SP}/ma_tmp/<label>/. HONESTY: never report a check as passing unless computed; never write "proved" for anything not proved; label hypotheses.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }

phase('Exact theory')
const [wolf, py] = await parallel([
  () => agent(`${COMMON}
TASK (Wolfram). Own: wolfram/Dirac16ComplexMatterAntimatter.wl, scripts/verify_dirac16complex_matter_antimatter.wls, ${ART}/wolfram-matter-antimatter-report.json, ${ART}/matter-antimatter-theory.json. Prove exactly M1-M4 of the spec for both statistics (and the exact implication of M5): M1 the U(1) invariance of L for every U(S), the Noether current and its conservation in an arbitrary field (symbolic jets as in Stage 1), charge conservation; M2 every candidate charge conjugation Psi -> M Psi^* (and Psibar^T forms) with constant 16x16 M solving the intertwining conditions with the gammas exactly (find the solution spaces), their action on L (invariant / -L / -L with m -> -m, etc.), parity-like Pin reflections with coordinate reflections, time reversal (antilinear), and the CPT-like combination; M3 the exact classification of Spin(4,4)- and Pin(4,4)-invariant bilinear forms Psi^T M Psi and Psi^T M gamma^a d_a Psi (solve S^{ab T} M + M S^{ab} = 0 on the fixture), their symmetry (symmetric/antisymmetric), which survive for Grassmann and for commuting components, and their U(1) charge; M4 the charge flip j -> -j under gamma^8 and the pair total, and the Krein-level particle/antiparticle mapping from the Stage-5 pairing report if present (else record not-run). Export all matrices and results to matter-antimatter-theory.json. Run: wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls ${ART}/wolfram-matter-antimatter-report.json (positional).`, { label: 'wolfram-ma', phase: 'Exact theory', schema: RESULT }),
  () => agent(`${COMMON}
TASK (independent sympy; do NOT import the Wolfram outputs as truth). Own: scripts/check_dirac16complex_matter_antimatter.py, tests/test_d16c_matter_antimatter.py, ${ART}/python-matter-antimatter-report.json. Re-derive independently M1-M4 of the spec for both statistics (use scripts/grassmann_algebra.py for Grassmann computations): U(1) invariance and the conserved current on explicit exact jets; the solution spaces of the charge-conjugation intertwining conditions and their action on L; the classification of invariant bilinear forms (exact nullspaces of S^{ab T} M + M S^{ab} = 0), their symmetry and survival for each statistics; the gamma^8 charge flip. Add a check MA_agreesWithWolfram against ${ART}/matter-antimatter-theory.json when it exists (record not-run otherwise). Fast unittest subset under 60 s.`, { label: 'python-ma', phase: 'Exact theory', schema: RESULT }),
])

phase('Document')
const doc = await agent(`${COMMON}
The exact agents finished (reports, truncated): ${JSON.stringify([wolf, py].map(r => r ? { summary: r.summary, key_results: r.key_results, failing: r.failing, open_items: r.open_items } : null)).slice(0, 14000)}
TASK (document). Own: provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md, .tex, .pdf, its entry in provenance/pdf-specifications.json (re-read immediately before registering; change only your entry), tests/test_d16c_matter_antimatter_publication.py. Write the document of spec section 3: FIRST paragraph the honest answer (the requested statement is not provable; the theory as built conserves its charge exactly; what is proved instead); then the matter-antimatter problem from zero for a beginner with the literature citations of spec section 1 (no invented numbers; cite); the theorems M1-M4 with complete proofs and the names of the machine checks; M5 as a labelled hypothesis with its exact implication and every assumption named; the Sakharov scorecard M6 as a table; what would have to be added to the theory (from M3); verification records; reproduction commands (PowerShell and Bash); non-claims. Every number from the reports. Build the PDF with python scripts/build_provenance_pdf.py <md> (verify mode until warning-free), then --register; pin it in the test following tests/test_d16c_primordial_publication.py; run the test.`, { label: 'doc-ma', phase: 'Document', schema: RESULT })

phase('Review')
const lenses = [
  ['rigour', 'Re-derive every theorem and proof of the document yourself on the exact fixture (U(1), current conservation, charge conjugation solution spaces, invariant bilinear forms and their symmetry per statistics, the gamma^8 charge flip); check every statement against the two reports; flag any gap, sign error or unproved step.'],
  ['honesty', 'Hunt for any sentence that says or suggests that the theory solves, explains or predicts the matter-antimatter asymmetry, or that treats the hypotheses H1-H3 as established; check that the first paragraph gives the honest answer, that every literature number is cited, and that the Sakharov scorecard is correct.'],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
The document is written. TASK (adversarial reviewer, lens ${k}): ${t} Report only real problems with concrete evidence; do not edit repository files.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)

phase('Fix')
let fix = null
if (findings.length) {
  fix = await agent(`${COMMON}
TASK (fixer). Findings (JSON): ${JSON.stringify(findings).slice(0, 60000)}
Re-verify each; fix confirmed ones at their root (code, reports regenerated, document, PDF rebuilt and registered, test updated); reject unconfirmed ones with evidence. One line per finding in key_results: FIXED / REJECTED (reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}
return { wolf, py, doc, findings, fix }
