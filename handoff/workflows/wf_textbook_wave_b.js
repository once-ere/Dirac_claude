export const meta = {
  name: 'textbook-wave-b',
  description: 'Textbook wave B: chapters 06, 07, 14-20 and the final ledger (after Stage 5), assembly and PDF, four review lenses, fixer',
  phases: [
    { title: 'Chapters', detail: 'Stage-5-dependent chapters, final ledger, appendices' },
    { title: 'Assembly', detail: 'assemble, build and register the PDF, tests' },
    { title: 'Review', detail: 'correctness, honesty, pedagogy, reproducibility' },
    { title: 'Fix', detail: 'apply confirmed findings, rebuild, re-register' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const CH = 'provenance/textbook/chapters'

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main; do NOT commit, push, or run git commands that change the index or working tree). You are working on the TEXTBOOK for complete beginners about the dirac16complex project. BINDING, read fully first: ${ROOT}/handoff/specs/TEXTBOOK_SPEC.md (the request, the HONESTY RULE, audience, style, files, chapter plan), ${ROOT}/handoff/specs/STAGE5_SPEC.md and ${ROOT}/handoff/specs/STAGE5_DOC_OUTLINE.md, the Stage-5 reports and outputs under artifacts/dirac16complex/pair-creation/ (final), the Stage-5 documents provenance/DIRAC16COMPLEX00_FIELD_THEORY.md and provenance/DIRAC16COMPLEX_PAIR_CREATION.md if they exist, the chapters already written under ${CH}/ (read them all to keep notation, cross-references and style consistent), and every source the spec names for your chapters.
RULES: write ONLY the files assigned to you; never touch Stage 4/5 files or other chapters. Derivations complete and correct; worked examples; exercises with full answers; "What we proved / what we assumed" per chapter; beginners' language. Markdown subset of scripts/build_dissertation_tex.py (chapter "## N. Title", sections "### N.M Title", nothing deeper; figures only as a line ![caption](path.png) with an existing PNG path). Test-build each chapter alone in ${SP}/textbook_tmp/<label>/ (or a git-ignored copy under ${ROOT}/build/) with python scripts/build_provenance_pdf.py ... --developer-layout (verify mode) until warning-free. Chunks of at most 300 lines per tool call. HONESTY: numbers only from committed reports; theorems with their exact hypotheses; never "proved" for anything not proved; the pair-creation and matter-antimatter chapters follow TEXTBOOK_SPEC section 0 to the letter.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }

phase('Chapters')
const tasks = [
  ['fields', `Chapters 06 (the two fields and their Lagrangians: dirac16complex and dirac16complex00, explicit mass terms, reality, the real restriction versus the author's Lg[], the coupling to gravity and the spin connection) and 07 (field equations, energy-momentum tensor, kinetic and potential energy, pressure, energy density and equations of state in an arbitrary gravitational field, for both fields, and their specialisation to the primordial field) -> ${CH}/06-two-fields-and-lagrangians.md, ${CH}/07-field-equations-and-emt.md.`],
  ['dft00', `Chapter 14 (the Kohn-Sham approximation for dirac16complex00: the Wick sign of the statistics derived from zero, the exchange energy and potentials, the model's status, the computed ground and first excited states of both fields side by side) -> ${CH}/14-kohn-sham-dirac16complex00.md.`],
  ['pairs', `Chapter 15 (the pairing theorems T1-T3 with complete proofs, both fields, and the Kohn-Sham demonstration with tables and figures from the Stage-5 outputs) -> ${CH}/15-pairing-theorems.md.`],
  ['cosmos', `Chapters 16 (does the big bang create universes in pairs? - exactly what is proved, what is consistent, what is not derived; quote the notebook cells 6, 7, 17 through handoff/surveys/survey_notebook-physics.md and Stage 1's statement), 17 (matter and antimatter: the observed asymmetry and its measured value from the literature with citation, the Sakharov conditions derived in plain words, universe/anti-universe ideas with the Boyle-Finn-Turok citation, what this theory contributes and what it does not; TEXTBOOK_SPEC section 0) and 18 (open problems and how a student could attack them) -> ${CH}/16-pairs-of-universes.md, ${CH}/17-matter-and-antimatter.md, ${CH}/18-open-problems.md.`],
  ['back', `Appendices 19 (reproducing everything: every command in PowerShell and Bash, expected outputs, the stage gates and their wall times, from README.md, HANDOFF.md and the gate headers) and 20 (glossary of every term used in the book and an index of the verifier checks cited), and the FINAL honesty ledger: update ${CH}/00-how-to-read.md's ledger table with every Stage-5 row (status from the Stage-5 reports) - change only the ledger rows and the sentences that point to Stage 5 -> ${CH}/19-reproducing-everything.md, ${CH}/20-glossary-and-check-index.md, ${CH}/00-how-to-read.md (ledger only).`],
]
const chapters = await parallel(tasks.map(([label, task]) => () => agent(`${COMMON}
TASK (${label}): ${task}`, { label: 'chapter:' + label, phase: 'Chapters', schema: RESULT })))

phase('Assembly')
const assembly = await agent(`${COMMON}
All chapters 00-20 exist (reports of the wave-B writers, truncated: ${JSON.stringify(chapters.map(r => r ? r.summary : null)).slice(0, 6000)}).
TASK (assembly). Own: provenance/DIRAC16COMPLEX_TEXTBOOK.md (generated), .tex, .pdf, its entry in provenance/pdf-specifications.json (re-read before registering; change only your entry), tests/test_d16c_textbook_publication.py; you may fix cross-reference and numbering errors in the chapters (minimal edits). Run python scripts/build_textbook.py (fix what it reports), build the PDF with python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md --developer-layout until warning-free, then --register; write the publication test (pattern tests/test_d16c_student_guide_publication.py: the assembled md equals the assembler's output, the tex equals the builder's output, the PDF is registered, key statements of the honesty ledger are present); run it.`, { label: 'assembly', phase: 'Assembly', schema: RESULT })

phase('Review')
const lenses = [
  ['correctness', 'Check every derivation, formula and number of the book against the repository documents, specs and reports; re-derive the key steps yourself (Clifford facts, spin connection, Euler-Lagrange equations, energy-momentum tensor, the Kohn-Sham reduction and exchange, the pairing theorems).'],
  ['honesty', 'Hunt for overclaims: anything called proved that is not; the big-bang pair-creation and matter-antimatter chapters must follow TEXTBOOK_SPEC section 0 exactly; every hypothesis labelled; the honesty ledger complete and consistent with the chapters and the reports.'],
  ['pedagogy', 'Read the book as a beginner who knows school algebra and one-variable calculus: find every notion used before it is defined, every skipped step, every unclear passage, every exercise without a correct answer.'],
  ['reproducibility', 'From a fresh copy of the working tree in scratch, run every command of the book that finishes within about 20 minutes and compare the outputs with what the book says; rebuild the PDF in verify mode; run the textbook tests.'],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
The book is assembled. TASK (adversarial reviewer, lens ${k}): ${t} Report only real problems with concrete evidence (chapter, section, line); do not edit repository files.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log('textbook findings: ' + findings.length)

phase('Fix')
let fix = null
if (findings.length) {
  fix = await agent(`${COMMON}
TASK (fixer). Findings (JSON): ${JSON.stringify(findings).slice(0, 90000)}
Re-verify each; fix confirmed ones in the chapter sources, reassemble, rebuild and re-register the PDF, update the test; reject unconfirmed ones with evidence. One line per finding in key_results: FIXED / REJECTED (reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}
return { chapters, assembly, findings, fix }
