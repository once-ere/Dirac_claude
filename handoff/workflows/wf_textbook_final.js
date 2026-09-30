export const meta = {
  name: 'textbook-final',
  description: 'Textbook final: chapter-0 ledger and status refresh, assembly, PDF (numbered from 0), registration, publication test, whole-book adversarial review (9 lenses), skeptics, per-chapter fixers, rebuild and re-register',
  phases: [
    { title: 'Carry-over', detail: 'cross-chapter items the per-chapter fixers could not apply' },
    { title: 'Ledger', detail: 'final honesty ledger, stage table, status sentences, abstract' },
    { title: 'Assembly', detail: 'assemble, build, register, publication test' },
    { title: 'Review', detail: 'correctness per part, honesty, pedagogy, reproducibility' },
    { title: 'Verify', detail: 'one skeptic per chapter with findings' },
    { title: 'Fix', detail: 'one fixer per chapter' },
    { title: 'Rebuild', detail: 'reassemble, rebuild, re-register, tests' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const CH = 'provenance/textbook/chapters'
const BOOK = 'provenance/DIRAC16COMPLEX_TEXTBOOK.md'
const PDFCMD = `python scripts/build_provenance_pdf.py ${BOOK} --developer-layout --number-sections-from-zero`

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main). NEVER run git commands that change the index, the working tree or the remote; read-only git is fine. The TEXTBOOK for complete beginners about the dirac16complex project; binding spec ${ROOT}/handoff/specs/TEXTBOOK_SPEC.md (read it fully: the HONESTY RULE of section 0 overrides everything). All 21 chapters exist in ${ROOT}/${CH}/ (00-20). The assembler is scripts/build_textbook.py (read its docstring), which writes ${BOOK}; the PDF is built with ${PDFCMD} (verify mode) and registered by adding --register; provenance/pdf-specifications.json is shared: re-read it immediately before registering and change only the textbook's entry. Never modify dirac-main/, vendor/, the author's notebook Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb, or files outside the textbook unless your task names them. Read large files in chunks of at most 300 lines per tool call. Scratch under ${SP}/textbook_final/<label>/ or the git-ignored ${ROOT}/build/textbook_final/<label>/.
STATE OF THE PROJECT (for status sentences): Stages 1-3 complete and gate-verified from fresh public clones. Stage 4: exact theory 125/125 and 157/157; Rust solver complete; reference 56 runs; the final cross-checker artifacts/dirac16complex/kohn-sham/python-check-report.json (read it) gives 63 checks with 1 failed (canonical_eigenvalues on the 301-point smeared N = 1016, -lambda_hat_2 run, 2.2e-6 against 1.05e-6), the Stage-4 gate not yet run. Stage 5: exact theory reports under artifacts/dirac16complex/pair-creation/ (read their counts), numerics partial, documents not written. Matter-antimatter: provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md and its reports. The lead's notes: ${SP}/textbook_lead_review.md and ${SP}/stage5_lead_notes.md.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, checks: { type: 'array', items: { type: 'string' } }, all_ok: { type: 'boolean' }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'checks', 'all_ok', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { chapter: { type: 'string' }, severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, lens: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['chapter', 'severity', 'lens', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICTS = { type: 'object', properties: { verdicts: { type: 'array', items: { type: 'object', properties: { index: { type: 'integer' }, confirmed: { type: 'boolean' }, reason: { type: 'string' }, corrected_fix: { type: 'string' } }, required: ['index', 'confirmed', 'reason', 'corrected_fix'] } } }, required: ['verdicts'] }
const CHAPTERS = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

phase('Carry-over')
const carry = await agent(`${COMMON}
TASK (cross-chapter carry-over). Read ${ROOT}/handoff/reviews/textbook_wave_a_carryover.json: items that the per-chapter fixers of the wave-A review could not apply because they touch other chapters, and the final gaps of that review. For EACH item: re-verify it against the current chapter text (the wave-B chapters 06, 07, 14-20 now exist; some items may already be resolved), then apply it with minimal edits in whichever chapter files it concerns. In particular: (a) exercise labels - make Chapters 11, 12 and 13 (and any other chapter) use "Exercise N.M" / "Answer N.M" like Chapters 00-10, and update every reference to them anywhere in the book; (b) Chapter 5 section 5.14 "that Chapter 9 traces to" -> say that Chapter 9 reconstructs it (ledger row L20, a hypothesis); (c) the coordinate-index convention: Chapters 2 and 9 must follow the book rule of Chapter 1 section 1.8 (upper-index coordinates in formulas) or state their exception explicitly; (d) the Chapter 11 figure caption that Chapter 10 finding F13 asked to change; (e) Chapter 9 section 9.16 "mirror copy that carries gamma^8 Psi" - make it agree with Chapter 13 section 13.14 and Chapter 15 (the Kohn-Sham mirror map is (m, lambda) -> (-m, +lambda); the field-level gamma^8 map is (m, lambda) -> (-m, -lambda)); (f) the numeric Pauli names sigma_1, sigma_2, sigma_3 versus Chapter 2's sigma_x, sigma_y, sigma_z (Chapters 4 and 13): define the numeric names once in Chapter 2 and point to it; (g) Chapter 0 section 0.6: mention Chapter 13's use of j for the block type and l for 3-space directions; (h) Chapter 13 section 13.14: rename the dummy index lambda in the conservation formula (lambda is the coupling); (i) wave-B defects: convert any chapter file with CRLF line endings to LF (Chapter 19 was reported), and write references to sections of project documents with the section sign (Chapter 15 line ~32 "Section 7" of the matter-antimatter document -> "§7"). Then run python scripts/build_textbook.py --check --list-references and fix every unresolved reference. Report one line per item: APPLIED / ALREADY RESOLVED / REJECTED (reason).`, { label: 'carry-over', phase: 'Carry-over', schema: RESULT })

phase('Ledger')
const ledger = await agent(`${COMMON}
TASK (final honesty ledger and status). Edit ONLY ${CH}/00-how-to-read.md, ${CH}/13-kohn-sham-primordial.md (status paragraphs only) and the abstract/subtitle constants in scripts/build_textbook.py. (1) Chapter 0: make Section 0.9 final ("(draft)" removed): every row, especially L33-L43, with its status from the committed reports and the wave-B chapters 06, 07, 14-17 (read them), the chapter pointers correct; the stage table of Section 0.5 with the state of each stage exactly as in CONTEXT; Section 0.2 and row L42: replace "no CP violation" by the exact statement of provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md (dirac16complex has an exact CP and no exact C for m != 0; dirac16complex00 has an exact C; each field has an exact charge-reversing symmetry, so Sakharov's second condition fails; exact U(1), so the first fails). (2) Chapter 13: the sentences on the status of the Stage-4 cross-check (13.1, 13.12, 13.15 and wherever else) replaced by the final checker result from python-check-report.json with the E4.13 resolution of Delta-SCF and the one remaining eigenvalue failure stated as it is; the numbers of rust/determinism-report.json and the five rust/*/summary.json quoted exactly. (3) The abstract of build_textbook.py agrees with the book. Test-build the two chapters alone (copy under build/textbook_final/ledger/ with first lines "# Test" and "## Test build", ${PDFCMD.replace(BOOK, '<copy>')}) until warning-free.`, { label: 'ledger', phase: 'Ledger', schema: RESULT })

phase('Assembly')
const assembly = await agent(`${COMMON}
TASK (assembly). Own: ${BOOK} (generated), its .tex and .pdf, the textbook entry of provenance/pdf-specifications.json, tests/test_d16c_textbook_publication.py. You may make MINIMAL edits to chapter files to repair numbering and cross-reference errors reported by the assembler. Run python scripts/build_textbook.py (without --allow-missing; fix what it reports), then ${PDFCMD} until the log is warning-free (inspect the PDF text: chapter 0 must print as 0 and a sample "Section 13.2" must point to section 13.2), then register with --register. Write the publication test following tests/test_d16c_student_guide_publication.py: the assembled md equals the assembler's output (build_textbook.py --verify-output or equivalent), the tex equals the builder's output with --developer-layout --number-sections-from-zero, the PDF is registered with its sha256 and page count, the 21 chapter headings are present in order, key honesty statements of Section 0.2, of Chapter 16 and of Chapter 17 are present (quote them from the chapters), and no chapter claims that the theory solves the matter-antimatter problem or that the big bang is proved to create universes in pairs (a lint over the assembled text). Run the test and python -m unittest tests.test_d16c_textbook_assembler.`, { label: 'assembly', phase: 'Assembly', schema: RESULT })

phase('Review')
const PARTS = [
  ['correctness-I', 'Chapters 00-04', ['00', '01', '02', '03', '04']],
  ['correctness-II', 'Chapters 05-08', ['05', '06', '07', '08']],
  ['correctness-III', 'Chapters 09-11', ['09', '10', '11']],
  ['correctness-IV', 'Chapters 12-14', ['12', '13', '14']],
  ['correctness-V', 'Chapters 15-20', ['15', '16', '17', '18', '19', '20']],
]
const lenses = [
  ...PARTS.map(([k, what]) => [k, `CORRECTNESS of ${what} of the assembled book (read the chapter files in ${CH}/): re-derive every derivation and worked example yourself (sympy/numpy in scratch), compare every number and check name with the committed report it cites, check every exercise answer, and check that these chapters agree with the chapters they cite.`]),
  ['honesty', `HONESTY over the whole book: every claim of proof matches a derivation or a named true check with its hypotheses; checks at test points are not presented as general proofs; the honesty ledger of Section 0.9 agrees with every chapter and report; Chapters 15-17 and every other mention of pair creation or matter-antimatter follow TEXTBOOK_SPEC section 0 to the letter and agree with provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md and the Stage-5 reports; interpretation is labelled.`],
  ['pedagogy-1', `PEDAGOGY of Chapters 00-10 for a reader who knows only school algebra and one-variable calculus: every notion used before it is defined anywhere earlier in the book, every skipped step, every unclear passage, notation clashes across chapters, exercises without complete correct answers.`],
  ['pedagogy-2', `PEDAGOGY of Chapters 11-20 for a reader who knows only school algebra and one-variable calculus: every notion used before it is defined anywhere earlier in the book, every skipped step, every unclear passage, notation clashes across chapters, exercises without complete correct answers.`],
  ['reproducibility', `REPRODUCIBILITY: from a fresh copy of the working tree under scratch, run every command and code snippet of the book that finishes within about 10 minutes (Chapter 19 in particular, PowerShell and Bash forms where both are given) and compare with what the book says; check that every file path and figure path exists and every cited check name exists in the cited report; rebuild the PDF in verify mode (${PDFCMD}); run tests/test_d16c_textbook_publication.py and tests/test_d16c_textbook_assembler.py.`],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
The book is assembled and registered (assembly report, truncated: ${JSON.stringify(assembly).slice(0, 3000)}). TASK (adversarial reviewer, lens ${k}; do not edit any file): ${t} Report only real problems with concrete evidence; name the chapter as its two-digit number in the field chapter.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings || [])
log('whole-book review: ' + findings.length + ' findings (' + reviews.filter(r => !r).length + ' reviewers failed)')
const byCh = {}
for (const f of findings) {
  const m = String(f.chapter || '').match(/\d{1,2}/)
  const key = m ? m[0].padStart(2, '0') : 'xx'
  ;(byCh[key] = byCh[key] || []).push(f)
}
if (byCh.xx) log('findings without a chapter: ' + byCh.xx.length + ' (given to the rebuild agent)')
const work = CHAPTERS.filter(c => (byCh[c] || []).length)

const fixes = await pipeline(
  work,
  (c) => agent(`${COMMON}
TASK (skeptic for chapter ${c} in ${CH}/; do not edit any file). For EACH numbered finding try hard to REFUTE it (re-read, re-derive, open the report, run the command); confirmed=true only if real; give corrected_fix if the proposed fix is wrong or incomplete.
FINDINGS: ${JSON.stringify(byCh[c].map((f, i) => ({ index: i, ...f }))).slice(0, 60000)}`, { label: 'verify:' + c, phase: 'Verify', schema: VERDICTS }),
  (v, c) => {
    const list = byCh[c]
    const conf = ((v && v.verdicts) || []).filter(x => x.confirmed && list[x.index]).map(x => ({ ...list[x.index], fix: x.corrected_fix && x.corrected_fix.trim() ? x.corrected_fix : list[x.index].fix }))
    if (!conf.length) return { chapter: c, applied: 0, note: 'nothing confirmed' }
    return agent(`${COMMON}
TASK (fixer of the chapter file ${CH}/${c}-*.md ONLY). Apply every confirmed finding at its root, keeping numbering, cross-references, exercises/answers and the "What we proved and what we assumed" section consistent; test-build the chapter alone (copy under build/textbook_final/fix${c}/ with first lines "# Test" and "## Test build") until warning-free. One line per finding in checks: FIXED / NOT FIXED (reason).
CONFIRMED FINDINGS: ${JSON.stringify(conf).slice(0, 80000)}`, { label: 'fix:' + c, phase: 'Fix', schema: RESULT }).then(r => ({ chapter: c, applied: conf.length, ...(r || {}) }))
  },
)

phase('Rebuild')
const rebuild = await agent(`${COMMON}
TASK (rebuild). Findings without a chapter (apply if confirmed, minimal edits): ${JSON.stringify(byCh.xx || []).slice(0, 20000)}
Then run python scripts/build_textbook.py, rebuild the PDF with ${PDFCMD} until warning-free, re-register with --register (re-read the registry first; change only the textbook entry), update tests/test_d16c_textbook_publication.py pins if they changed, run it and tests/test_d16c_textbook_assembler.py and tests/test_publication_tooling.py, and report page count, sha256 and all test results. Fix results (truncated): ${JSON.stringify(fixes).slice(0, 20000)}`, { label: 'rebuild', phase: 'Rebuild', schema: RESULT })

return { carry, ledger, assembly, findingsTotal: findings.length, perChapter: Object.fromEntries(Object.entries(byCh).map(([k, v]) => [k, v.length])), fixes, rebuild }
