export const meta = {
  name: 'completion-phase-3c-book-v2',
  description: 'Completion phase 3c (book), revised: sweep of the chapters affected by the final Revision record; whole-book review with 5 lenses; 2 skeptics per finding; fixers per chapter in size-bounded parts; fix-verifiers',
  phases: [
    { title: 'Sweep', detail: 'one fixer per chapter with the collected items (Revision changes quoted in the book, failing notebook checks), then a verifier' },
    { title: 'Review', detail: 'book lenses: cross-chapter consistency, cross-references, honesty R3, notebooks and figures, deep-dive spot checks' },
    { title: 'Skeptics', detail: 'two independent refutation attempts per finding; a finding survives only if neither refutes it' },
    { title: 'Fix', detail: 'one fixer per owner area, its confirmed findings in parts of at most about 40000 characters (nothing is cut)' },
    { title: 'Verify', detail: 'adversarial fix-verifier per part' },
  ],
}
// Revised from completion_phase_3c_book.js (2026-10-08): (1) the first version passed a fixer at most 60000 characters
// of its findings, and phase 3c-rev showed that this silently drops findings (its docs fixer saw 8 of 15); here the
// findings of an area are split into parts that fit, and every part gets its own fixer and verifier, one after the
// other; (2) a sweep stage first brings the chapters in line with the final Revision record (args.sweep: chapter ->
// list of items; args.failing: chapter -> notebooks whose nbkit check failed); (3) Notebook 23a and chapter 23 are NOT
// rebuilt here (23a reads every other notebook's recorded check: the lead rebuilds it last).
const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
const R = 'Revision'
const T = 'Revision/textbook'
const NOAGREE = "NEVER accept licence terms, source agreements, cookie banners or any other agreement on the user's machine or accounts (never pass --accept-source-agreements / --accept-package-agreements to winget, never run wolframscript -activate, never accept an EULA)."
const BOUND = `BOUNDED TASK (user rules: no hours-long agent jobs; never wait more than 60 s in one foreground command - run longer things detached with a done marker): small verified steps; after every step append one line to ${SP}/phase3c_book/<your label with ':' replaced by '-'>.progress.md. Aim to finish within about 45 minutes; if not finished, stop at a consistent, verified state and list exactly what remains. Never leave a half-edited file. Do not commit (the lead commits).`
const CTX = `${NOAGREE}
CONTEXT: repository ${ROOT} (git, branch main; Windows 11; Python 3.14 with numpy, sympy, mpmath, matplotlib, nbformat, nbclient; WolframScript 1.14 / Wolfram 15.0.1; Rust cargo 1.91; pdflatex). NEVER run git commands that change the index, the working tree history or the remote (read-only git and clones into scratch are fine). The AUTHOR's notebooks are read only; never modify the original textbook provenance/DIRAC16COMPLEX_TEXTBOOK.* or provenance/textbook/. The Revision record (${R}/ outside ${T}/) is FINAL: do not edit it; if the book disagrees with it, the book changes (report a suspected error of the record in open_items instead). Notebook 23a, chapter 23 and the assembled book ${T}/UNIVERSES_IN_PAIRS_TEXTBOOK.* are the lead's: do not rebuild or edit them. BINDING: ${R}/SPEC.md (the author's coordinates: x1..x3 space, x4 time, x5, x6, x7 the exponentially DEFLATING extra times, x8 hidden; the no-mixing rule; sections 7-11), ${R}/README.md, ${T}/TEXTBOOK_SPEC.md (R0-R6, deep-dive section 1, notebooks section 2, instructions section 3). HONESTY: numbers only from Revision outputs; hypotheses investigated, never assumed; interpretation labelled; nothing called proved that is not proved; the U(1) charge has a PROVED local law and its total is constant only under the ASSUMED no-flux condition at z = pi/2; the pair-creation request is answered exactly as in ${R}/docs/PAIR_CREATION_PROOFS.md section 11.3. Read files in chunks of at most 300 lines. Scratch only under ${SP}/phase3c_book/<your label>/.`
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }

const CHAPTER_OWNS = nn => `You own chapter ${nn} (${T}/chapters/${nn}-*.md) and its builders, notebooks, PROVENANCE files and figures (${T}/notebooks/src/${nn}*.py, ${T}/notebooks/${nn}*, ${T}/figures/${nn}*). Rebuild every notebook whose builder you change (python ${T}/tools/nbkit.py build <builder> --date 2026-10-08, then nbkit check <builder> --record 2026-10-08), run nbkit check on every notebook of the chapter, the walk-through audit (python ${T}/tools/audit/walkthrough_diff.py <chapter> <notebook> <id>), and python ${T}/tools/check_chapter.py <chapter> --scratch <your scratch> until chapter_check=OK with no problem= or latex_warning= lines. Every quoted code cell, printed number and figure caption of the chapter must equal the rebuilt notebook.`
const area = f => {
  const p = (f.file || '').replace(/\\/g, '/').replace(/^.*Dirac_claude\//, '')
  const m = p.match(/^Revision\/textbook\/(?:chapters\/(\d\d)|notebooks\/(?:src\/)?(\d\d)|figures\/(\d\d))/)
  if (m) { const nn = m[1] || m[2] || m[3]; return `chapter-${nn}` }
  if (p.startsWith('Revision/textbook/')) return 'textbook-other'
  return 'outside-book'
}
const AREA_OWNS = a => a.startsWith('chapter-') ? CHAPTER_OWNS(a.slice(8))
  : a === 'textbook-other' ? `You own the files of ${T}/ named in the findings, except Notebook 23a, chapter 23 and the assembled book. Run the tools' own tests and checks after every change.`
    : `These findings name files outside the book. Do NOT edit them: re-verify each finding and report it in open_items for the lead (the Revision record is final).`
// Split a list of findings into parts whose JSON fits into maxChars (a single larger finding forms its own part).
const parts = (list, maxChars) => {
  const out = []
  let cur = []
  for (const f of list) {
    if (cur.length && JSON.stringify(cur.concat([f])).length > maxChars) { out.push(cur); cur = [] }
    cur.push(f)
  }
  if (cur.length) out.push(cur)
  return out
}

const sweep = (args && args.sweep) || {}
const failing = (args && args.failing) || {}
const chapters = Array.from(new Set(Object.keys(sweep).concat(Object.keys(failing)))).sort()

phase('Sweep')
const swept = await pipeline(chapters,
  nn => agent(`${CTX}\n${BOUND}\nTASK (sweep of chapter ${nn}): ${CHAPTER_OWNS(nn)}\nBring the chapter in line with the final Revision record. Items collected by the lead (each re-verify against the record before editing; reject with evidence if wrong): ${JSON.stringify(sweep[nn] || [])}\nNotebooks of this chapter whose nbkit check failed in the lead's check pass (find the cause in their check logs under ${SP}/vc_sweep*/ and fix it at the root; usually a changed Revision file that the notebook reads): ${JSON.stringify(failing[nn] || [])}\nAlso grep the chapter and its builders for statements that the Revision changes of 2026-10-08 made inexact ('never crosses -1', 'at every a', 'conserved charge', 're-inflate', 'positive Fock realisation' without its scope, 'not verified by a Revision check' for the lambda != 0 EMT operator, report counts, step counts of the gate) and fix them. One line per item in key_results: FIXED / REJECTED (reason) / OPEN (why).`, { label: `sweep:${nn}`, phase: 'Sweep', schema: RESULT }),
  (fx, nn) => agent(`${CTX}\n${BOUND}\nTASK (verifier of the sweep of chapter ${nn}; adversarial; do NOT edit files): Items: ${JSON.stringify(sweep[nn] || [])}; failing notebooks: ${JSON.stringify(failing[nn] || [])}\nFixer report: ${JSON.stringify(fx || {}).slice(0, 40000)}\nCheck every item in the files, re-run nbkit check of every notebook of the chapter, the walk-through audit and check_chapter.py. Report as findings only what is still wrong.`, { label: `sweep-verify:${nn}`, phase: 'Sweep', schema: FINDINGS })
    .then(v => ({ chapter: nn, fix: fx, remaining: v })),
)

const LENSES = [
  ['book-consistency', `Cross-chapter consistency of ${T}/chapters/*.md (chapter 23 excepted, it is regenerated later): the same quantity, count or statement quoted in several chapters (check counts of the Revision reports, the U(1) charge statement, the T3 statement, the dark-sector verdicts, the a4 conclusions, the KS cross-check 31/31, the tip-cutoff study, the finite-Fock result for lambda != 0, the status labels PROVED/COMPUTED/ASSUMED/OPEN) must agree with each other and with the records; list every disagreement.`],
  ['book-references', `Every cross-reference in ${T}/chapters/*.md ("Section x.y", "Chapter n", "Figure NNx.k", "Notebook NNx", "In [k]", "Exercise n.m", equation numbers) must point to something that exists and says what the reference claims; assemble the book with python ${T}/tools/assemble_textbook.py --allow-missing --output <scratch file> (never overwrite the committed book) and report its problems.`],
  ['book-honesty', `R3 over the WHOLE book (${T}/chapters/*.md and every notebook's markdown and printed text): no sentence may claim that universes are created in pairs, that matter-antimatter asymmetry is explained, that dark energy or dark matter is explained, that the total U(1) charge is conserved without the no-flux condition, or that anything is proved that the Revision record does not prove; R5 (charge conjugation is a matrix). Search systematically (grep for proved, prove, created, creation, explain, conserved, solves, establish, dark energy, dark matter, asymmetry, converge) and judge each hit in context.`],
  ['book-notebooks', `Notebooks and figures: every chapter has its notebooks, every notebook has its builder, PROVENANCE file, run-instruction paragraph before it in the chapter and a walk-through after it; TEXTBOOK_SPEC targets: at least 4 figures per chapter (chapters 0 and 23 excepted) and at least 100 in the book, every figure with a teaching caption; run python ${T}/tools/audit/walkthrough_all.py (if present; else walkthrough_diff.py per notebook) and judge every report by hand; run python ${T}/tools/nbkit.py lint on every builder.`],
  ['book-deepdive', `Deep-dive spot checks (TEXTBOOK_SPEC section 1): pick at least 4 derivations from each of chapters 01-22 (spread over each chapter) and check that every line is written out with the rule that produced it (no "it can be shown", no "similarly", no skipped algebra), every technical word is defined at first use, and the exercises have complete worked answers; report only real gaps with their location.`],
]

phase('Review')
const judged = await pipeline(LENSES,
  ([key, task]) => agent(`${CTX}\n${BOUND}\nTASK (reviewer ${key} of the textbook; adversarial; do NOT edit files): ${task} Report only real problems with concrete evidence (file, location, quoted text, the record or computation that contradicts it, the exact fix).`, { label: `review:${key}`, phase: 'Review', schema: FINDINGS }),
  (r, [key]) => parallel(((r && r.findings) || []).map((f, i) => () =>
    parallel([0, 1].map(j => () => agent(`${CTX}\nTASK (skeptic ${j + 1} of finding ${key}#${i}; do NOT edit files): Try to REFUTE this finding by checking it yourself in the files and records${j ? ' (look for evidence that the text is in fact correct, or that the finding misreads it)' : ' (re-derive or recompute the claim independently)'}. Set refuted=true only if the finding is wrong or not a real problem; give evidence either way. Finding: ${JSON.stringify(f)}`, { label: `skeptic:${key}:${i}:${j}`, phase: 'Skeptics', schema: VERDICT })))
      .then(vs => ({ ...f, lens: key, refutations: vs.filter(Boolean).filter(v => v.refuted).length, skeptics: vs.filter(Boolean) })))),
)
const confirmed = judged.flat().filter(Boolean).filter(f => f.refutations === 0)
const rejected = judged.flat().filter(Boolean).filter(f => f.refutations > 0)
log(`findings: ${confirmed.length} confirmed by both skeptics, ${rejected.length} refuted by at least one`)

phase('Fix')
const byArea = {}
for (const f of confirmed) { (byArea[area(f)] = byArea[area(f)] || []).push(f) }
const fixes = await pipeline(Object.entries(byArea), async ([a, fs]) => {
  const results = []
  const ps = parts(fs, 40000)
  if (ps.length > 1) log(`area ${a}: ${fs.length} findings in ${ps.length} parts`)
  for (const [n, part] of ps.entries()) {
    const label = ps.length > 1 ? `${a}:part${n + 1}` : a
    const fx = await agent(`${CTX}\n${BOUND}\nTASK (fixer of area ${label}): ${AREA_OWNS(a)} Fix every one of these ${part.length} findings (part ${n + 1} of ${ps.length} of this area), each confirmed by two independent skeptics, at the root (JSON, complete): ${JSON.stringify(part)}\nRe-verify each before editing; if you find a finding wrong after all, reject it with evidence. One line per finding in key_results: FIXED / REJECTED (reason).`, { label: `fix:${label}`, phase: 'Fix', schema: RESULT })
    const v = await agent(`${CTX}\n${BOUND}\nTASK (fix-verifier of area ${label}; adversarial; do NOT edit files): Findings (complete): ${JSON.stringify(part)}\nFixer report: ${JSON.stringify(fx || {}).slice(0, 40000)}\nFor EVERY finding check in the files that the fix is real and correct and broke nothing (re-run the checks, notebooks, builds and tests of the area). Report as findings only what is still wrong.`, { label: `verify-fix:${label}`, phase: 'Verify', schema: FINDINGS })
    results.push({ area: label, findings: part.length, fix: fx, remaining: v })
  }
  return results
})
return { swept, confirmed, rejected: rejected.map(f => ({ lens: f.lens, file: f.file, problem: f.problem, why: f.skeptics.filter(s => s.refuted).map(s => s.reason) })), fixes }
