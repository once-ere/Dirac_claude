export const meta = {
  name: 'book-final-lenses-2026-10-14',
  description: 'The two book review lenses that never ran (cross-references, notebooks/figures) in small per-chapter-group agents, plus the residual findings of the continuation verifiers; skeptics; one fixer and verifier per chapter',
  phases: [
    { title: 'Review', detail: 'references and notebooks lenses, one agent per lens and chapter group' },
    { title: 'Skeptics', detail: 'two refutation attempts per finding' },
    { title: 'Fix', detail: 'one fixer per chapter (lens findings + residual verifier findings)' },
    { title: 'Verify', detail: 'adversarial verifier per chapter' },
  ],
}
const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/837d3989-831c-4131-a54e-de216022bedc/scratchpad'
const R = 'Revision'
const T = 'Revision/textbook'
const NOAGREE = "NEVER accept licence terms, source agreements, cookie banners or any other agreement on the user's machine or accounts (never pass --accept-source-agreements / --accept-package-agreements to winget, never run wolframscript -activate, never accept an EULA)."
const BOUND = `BOUNDED TASK (user rules: no hours-long agent jobs; never wait more than 60 s in one foreground command - run longer things detached with a done marker and do other checks meanwhile): small verified steps; after every step append one line to ${SP}/book_final/<your label with ':' replaced by '-'>.progress.md. Finish within about 30 minutes; if not finished, stop at a consistent, verified state and list exactly what remains. Never leave a half-edited file. Do not commit (the lead commits; a Stop hook may also commit WIP snapshots).`
const CTX = `${NOAGREE}
CONTEXT: repository ${ROOT} (git, branch main; Windows 11; Python 3.14 with numpy, sympy, mpmath, matplotlib, nbformat, nbclient; WolframScript 1.14 / Wolfram 15.0.1; Rust cargo 1.91; pdflatex). The machine is busy: long detached numerics (python ks_reference_*.py, dirac16complex_kohn_sham.exe) are running - NEVER stop, kill or touch those processes or their output folders (artifacts/dirac16complex/**, build/s5-rust-*). NEVER run git commands that change the index, the working tree history or the remote (read-only git is fine). The AUTHOR's notebooks are read only; never modify provenance/DIRAC16COMPLEX_TEXTBOOK.* or provenance/textbook/. The Revision record (${R}/ outside ${T}/) is FINAL: do not edit it; if the book disagrees with it, the book changes (report a suspected error of the record in open_items). Notebook 23a, chapter 23 and the assembled book ${T}/UNIVERSES_IN_PAIRS_TEXTBOOK.* are the lead's: do not rebuild or edit them (23a and chapter 23 are regenerated after this round; report their consequences in open_items). BINDING: ${R}/SPEC.md (the author's coordinates: x1..x3 space, x4 time, x5, x6, x7 the exponentially DEFLATING extra times, x8 hidden), ${R}/README.md, ${T}/TEXTBOOK_SPEC.md (R0-R6, deep-dive section 1, notebooks section 2, instructions section 3). HONESTY: numbers only from Revision outputs; nothing called proved that is not proved; the U(1) charge has a PROVED local law and its total is constant only under the ASSUMED no-flux condition at z = pi/2. Read files in chunks of at most 300 lines. Scratch only under ${SP}/book_final/<your label with ':' replaced by '-'>/.`
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const CHAPTER_OWNS = nn => `You own chapter ${nn} (${T}/chapters/${nn}-*.md) and its builders, notebooks, PROVENANCE files and figures (${T}/notebooks/src/${nn}*.py, ${T}/notebooks/${nn}*, ${T}/figures/${nn}*). Rebuild every notebook whose builder you change (python ${T}/tools/nbkit.py build <builder> --date 2026-10-14, then nbkit check <builder> --record 2026-10-14), run nbkit check on every notebook of the chapter, the walk-through audit (python ${T}/tools/audit/walkthrough_diff.py <chapter> <notebook> <id>), and python ${T}/tools/check_chapter.py <chapter> --scratch <your scratch> until chapter_check=OK with no problem= or latex_warning= lines. Every quoted code cell, printed number and figure caption of the chapter must equal the rebuilt notebook.`
const chOf = f => {
  const p = (f.file || '').replace(/\\/g, '/')
  const m = p.match(/textbook\/(?:chapters\/(\d\d)|notebooks\/(?:src\/)?(\d\d)|figures\/(\d\d)|data\/(\d\d))/)
  return m ? (m[1] || m[2] || m[3] || m[4]) : 'other'
}
const GROUPS = [['00', '01', '02', '03', '04', '05'], ['06', '07', '08', '09', '10', '11'], ['12', '13', '14', '15', '16', '17'], ['18', '19', '20', '21', '22', '23']]
const LENS = {
  references: g => `Every cross-reference in chapters ${g.join(', ')} (${T}/chapters/<nn>-*.md): "Section x.y", "Chapter n", "Figure NNx.k", "Notebook NNx", "In [k]", "Exercise n.m", equation numbers, file paths of the record. Each must point to something that exists and says what the reference claims (open the target and read it). For the whole-book reference check run once python ${T}/tools/assemble_textbook.py --allow-missing --output <your scratch>/book.md (never overwrite the committed book) and report the problems it prints that concern your chapters. Chapter 23 is regenerated later: for chapter 23 report only references that point to sections that no longer exist.`,
  notebooks: g => `Notebooks and figures of chapters ${g.filter(x => x !== '23').join(', ')}: every chapter has its notebooks, every notebook its builder (${T}/notebooks/src/), PROVENANCE file, a complete self-contained run-instruction paragraph before it in the chapter (never "see section X") and a walk-through after it; TEXTBOOK_SPEC targets: at least 4 figures per chapter (chapter 0 excepted), every figure referenced in the text with a teaching caption equal to ${T}/figures/<id>.captions.json; run python ${T}/tools/audit/walkthrough_diff.py for every notebook of these chapters and judge every report by hand (known conventions: captions shortened with '...)', docstrings omitted, the generated set-up cell); run python ${T}/tools/nbkit.py lint on every builder of these chapters.`,
}
const residual = (args && args.residual) || {}

phase('Review')
const reviewed = await pipeline(
  Object.keys(LENS).flatMap(l => GROUPS.map(g => ({ l, g }))),
  ({ l, g }) => agent(`${CTX}\n${BOUND}\nTASK (reviewer, lens ${l}, chapters ${g.join('-')}; adversarial; do NOT edit files): ${LENS[l](g)} Report only real problems with concrete evidence (file, location, quoted text, what it should be, the exact fix).`, { label: `review:${l}:${g[0]}-${g[g.length - 1]}`, phase: 'Review', schema: FINDINGS }),
  (r, { l, g }) => parallel(((r && r.findings) || []).map((f, i) => () =>
    parallel([0, 1].map(j => () => agent(`${CTX}\nTASK (skeptic ${j + 1} of finding ${l}:${g[0]}#${i}; do NOT edit files; about 10 minutes): Try to REFUTE this finding by checking it yourself in the current files${j ? ' (look for evidence that the text is in fact correct, or that the finding misreads it)' : ' (re-check the target of the reference / the notebook independently)'}. Set refuted=true only if the finding is wrong or not a real problem. Finding: ${JSON.stringify(f)}`, { label: `skeptic:${l}:${g[0]}:${i}:${j}`, phase: 'Skeptics', schema: VERDICT })))
      .then(vs => ({ ...f, lens: l, refutations: vs.filter(Boolean).filter(v => v.refuted).length })))),
)
const all = reviewed.flat().filter(Boolean)
const confirmed = all.filter(f => f.refutations === 0)
log(`lens findings: ${confirmed.length} confirmed, ${all.length - confirmed.length} refuted`)

// barrier: one fixer per chapter must see the findings of both lenses and the residual verifier findings together
const byCh = {}
for (const f of confirmed) (byCh[chOf(f)] = byCh[chOf(f)] || { lens: [], residual: [] }).lens.push(f)
for (const [nn, fs] of Object.entries(residual)) (byCh[nn] = byCh[nn] || { lens: [], residual: [] }).residual.push(...fs)
const lead = byCh.other || null
delete byCh.other
if (byCh['23']) { log(`chapter 23 findings go to the lead: ${byCh['23'].lens.length + byCh['23'].residual.length}`) }
const ch23 = byCh['23'] || null
delete byCh['23']

phase('Fix')
const fixed = await pipeline(Object.keys(byCh).sort(),
  nn => agent(`${CTX}\n${BOUND}\nTASK (fixer of chapter ${nn}): ${CHAPTER_OWNS(nn)}\nFix at the root every item (complete JSON). (A) review findings confirmed by two skeptics: ${JSON.stringify(byCh[nn].lens)}\n(B) findings an adversarial verifier left after the previous fix round of this chapter: ${JSON.stringify(byCh[nn].residual)}\nRe-verify each against the current files and the Revision record before editing; reject with evidence if wrong. When you change a sentence, fix every other occurrence in the chapter and its notebooks. One line per item in key_results: FIXED / ALREADY FIXED / REJECTED (reason).`, { label: `fix:${nn}`, phase: 'Fix', schema: RESULT }),
  (fx, nn) => agent(`${CTX}\n${BOUND}\nTASK (adversarial verifier of the fix of chapter ${nn}; do NOT edit files): Items: ${JSON.stringify(byCh[nn]).slice(0, 40000)}\nFixer report: ${JSON.stringify(fx || {}).slice(0, 30000)}\nFor EVERY item check that the fix is real, correct, complete and broke nothing: re-run nbkit check of every notebook of the chapter, the walk-through audit and check_chapter.py (own scratch); look at git diff of the chapter's files for half-done edits. Report as findings only what is still wrong, each with the exact fix.`, { label: `verify:${nn}`, phase: 'Verify', schema: FINDINGS })
    .then(v => ({ chapter: nn, fixed: fx ? fx.key_results : null, failing: fx ? fx.failing : null, open_items: fx ? fx.open_items : null, remaining: v ? v.findings : null })),
)
return { fixed: fixed.filter(Boolean), for_lead: { other: lead, chapter23: ch23 }, refuted: all.filter(f => f.refutations > 0).map(f => ({ lens: f.lens, file: f.file, problem: f.problem })) }
