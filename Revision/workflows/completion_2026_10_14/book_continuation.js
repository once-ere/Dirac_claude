export const meta = {
  name: 'book-continuation-2026-10-14',
  description: 'Finish the book fixes cut off by the weekly limit on 2026-10-08: skeptics for unverified findings, one fixer and one adversarial verifier per chapter',
  phases: [
    { title: 'Skeptics', detail: 'two refutation attempts for each book-review finding that never got its skeptics' },
    { title: 'Fix', detail: 'one fixer per chapter: interrupted residual items + confirmed book-review findings' },
    { title: 'Verify', detail: 'adversarial verifier per chapter' },
  ],
}
const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/837d3989-831c-4131-a54e-de216022bedc/scratchpad'
const OLD = 'C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad'
const R = 'Revision'
const T = 'Revision/textbook'
const ITEMS = `${SP}/book_items.json`
const NOAGREE = "NEVER accept licence terms, source agreements, cookie banners or any other agreement on the user's machine or accounts (never pass --accept-source-agreements / --accept-package-agreements to winget, never run wolframscript -activate, never accept an EULA)."
const BOUND = `BOUNDED TASK (user rules: no hours-long agent jobs; never wait more than 60 s in one foreground command - run longer things detached with a done marker and do other checks meanwhile): small verified steps; after every step append one line to ${SP}/book_cont/<your label with ':' replaced by '-'>.progress.md. Finish within about 30 minutes; if not finished, stop at a consistent, verified state and list exactly what remains. Never leave a half-edited file. Do not commit (the lead commits; a Stop hook may also commit WIP snapshots).`
const CTX = `${NOAGREE}
CONTEXT: repository ${ROOT} (git, branch main; Windows 11; Python 3.14 with numpy, sympy, mpmath, matplotlib, nbformat, nbclient; WolframScript 1.14 / Wolfram 15.0.1; Rust cargo 1.91; pdflatex). The machine is busy: long detached numerics (Stage-4 / Stage-5 solver runs: python ks_reference_*.py and dirac16complex_kohn_sham.exe) are running - NEVER stop, kill or touch those processes or their output folders (artifacts/dirac16complex/pair-creation/, build/s5-rust-*). NEVER run git commands that change the index, the working tree history or the remote (read-only git such as git diff / git show / git log is fine). The AUTHOR's notebooks are read only; never modify the original textbook provenance/DIRAC16COMPLEX_TEXTBOOK.* or provenance/textbook/. The Revision record (${R}/ outside ${T}/) is FINAL: do not edit it; if the book disagrees with it, the book changes (report a suspected error of the record in open_items instead). Notebook 23a, chapter 23 and the assembled book ${T}/UNIVERSES_IN_PAIRS_TEXTBOOK.* are the lead's: do not rebuild or edit them (report glossary/chapter-23 consequences in open_items). BINDING: ${R}/SPEC.md (the author's coordinates: x1..x3 space, x4 time, x5, x6, x7 the exponentially DEFLATING extra times, x8 hidden; the no-mixing rule; sections 7-11), ${R}/README.md, ${T}/TEXTBOOK_SPEC.md (R0-R6, deep-dive section 1, notebooks section 2, instructions section 3). HONESTY: numbers only from Revision outputs; hypotheses investigated, never assumed; interpretation labelled; nothing called proved that is not proved; the U(1) charge has a PROVED local law and its total is constant only under the ASSUMED no-flux condition at z = pi/2; the pair-creation request is answered exactly as in ${R}/docs/PAIR_CREATION_PROOFS.md section 11.3. Read files in chunks of at most 300 lines. Scratch only under ${SP}/book_cont/<your label with ':' replaced by '-'>/.`
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const CHAPTER_OWNS = nn => `You own chapter ${nn} (${T}/chapters/${nn}-*.md) and its builders, notebooks, PROVENANCE files and figures (${T}/notebooks/src/${nn}*.py, ${T}/notebooks/${nn}*, ${T}/figures/${nn}*). Rebuild every notebook whose builder you change (python ${T}/tools/nbkit.py build <builder> --date 2026-10-14, then nbkit check <builder> --record 2026-10-14), run nbkit check on every notebook of the chapter, the walk-through audit (python ${T}/tools/audit/walkthrough_diff.py <chapter> <notebook> <id>), and python ${T}/tools/check_chapter.py <chapter> --scratch <your scratch> until chapter_check=OK with no problem= or latex_warning= lines. Every quoted code cell, printed number and figure caption of the chapter must equal the rebuilt notebook.`
const INTERRUPTED = nn => `INTERRUPTED WORK: on 2026-10-08 a weekly usage limit killed the previous fixer of this chapter mid-way. Its partial edits may be in the working tree (see git diff -- ${T}/chapters/${nn}-* ${T}/notebooks/${nn}* ${T}/notebooks/src/${nn}* ${T}/figures/${nn}*; uncommitted edits exist at least for chapters 10, 15, 16 and notebooks 14c, 15a-15e PROVENANCE files) and its progress logs are under ${OLD}/phase3c_book/ (files whose names contain ${nn}, e.g. residual-${nn}.progress.md, refix2-${nn}.progress.md, ${nn}-refix.progress.md, residual-refix-${nn}.progress.md, refix-${nn}/). Inspect them first: keep what is correct and complete, finish or repair what is partial; never assume a partial edit is verified.`

const idx = (args && args.chapters) || {}
const chapters = Object.keys(idx).sort()
if (!chapters.length) throw new Error('args.chapters missing')
log(`chapters: ${chapters.join(', ')}`)
const findingRef = (nn, i) => `the finding at index ${i} of the list book_review under the key "${nn}" of the JSON file ${ITEMS} (read it completely)`

const results = await pipeline(chapters,
  // stage 1: skeptics for findings that never got them (a finding survives only if neither skeptic refutes it)
  async nn => {
    const n = idx[nn].book || 0
    const out = await parallel(Array.from({ length: n }, (_, i) => async () => {
      if (!(idx[nn].skeptic || []).includes(i)) return { i, refuted_by: 0 }
      const vs = await parallel([0, 1].map(j => () => agent(`${CTX}\nTASK (skeptic ${j + 1} of book finding ${nn}#${i}; do NOT edit files; about 10 minutes): Try to REFUTE ${findingRef(nn, i)} by checking it yourself in the current files and records${j ? ' (look for evidence that the text is in fact correct, or that the finding misreads it; note it may already have been fixed)' : ' (re-derive or recompute the claim independently)'}. Set refuted=true only if the finding is wrong or not a real problem (an already-fixed finding is refuted=true with reason ALREADY FIXED). Give evidence either way.`, { label: `skeptic:${nn}:${i}:${j}`, phase: 'Skeptics', schema: VERDICT })))
      const ok = vs.filter(Boolean)
      return { i, refuted_by: ok.filter(v => v.refuted).length, verdicts: ok }
    }))
    return out.filter(Boolean)
  },
  // stage 2: one fixer per chapter
  async (judged, nn) => {
    const confirmed = judged.filter(f => f.refuted_by === 0).map(f => f.i)
    const rejected = judged.filter(f => f.refuted_by > 0)
    const nres = idx[nn].residual || 0
    if (!confirmed.length && !nres) return { chapter: nn, fix: null, confirmed, rejected }
    const fx = await agent(`${CTX}\n${BOUND}\nTASK (fixer of chapter ${nn}): ${CHAPTER_OWNS(nn)}\n${INTERRUPTED(nn)}\nFix at the root every item below. Read the JSON file ${ITEMS}, key "${nn}". (A) ${nres ? `ALL ${nres} entries of its list "residual": findings an adversarial verifier left after the previous fix round` : 'no residual entries'}. (B) ${confirmed.length ? `the entries at indices ${JSON.stringify(confirmed)} of its list "book_review": book-review findings confirmed by independent skeptics` : 'no book-review entries'}${rejected.length ? ` (indices ${JSON.stringify(rejected.map(f => f.i))} of book_review were refuted by a skeptic: do NOT apply them; reasons: ${JSON.stringify(rejected.map(f => (f.verdicts || []).filter(v => v.refuted).map(v => v.reason)))})` : ''}. Each entry has file, location, problem, evidence, fix.\nRe-verify each item against the current files and the Revision record before editing (some may already be fixed by the interrupted agent - then confirm and say so); if you find an item wrong after all, reject it with evidence. When you change a sentence, grep the chapter (and its notebooks' markdown) for the same statement elsewhere and fix every occurrence. One line per item in key_results: FIXED / ALREADY FIXED / REJECTED (reason).`, { label: `fix:${nn}`, phase: 'Fix', schema: RESULT })
    return { chapter: nn, fix: fx, confirmed, rejected }
  },
  // stage 3: adversarial verifier
  async (st, nn) => {
    if (!st || !st.fix) return st
    const v = await agent(`${CTX}\n${BOUND}\nTASK (adversarial verifier of the fix of chapter ${nn}; do NOT edit files): Items: in the JSON file ${ITEMS}, key "${nn}": every entry of "residual" and the entries at indices ${JSON.stringify(st.confirmed)} of "book_review".\nFixer report: ${JSON.stringify(st.fix).slice(0, 40000)}\nFor EVERY item check in the files that the fix is real, correct, consistent with the Revision record and complete (every occurrence), and that it broke nothing: re-run nbkit check of every notebook of the chapter, the walk-through audit and check_chapter.py (use your own scratch). Also look at git diff of the chapter's files for unrelated or half-done edits. Report as findings only what is still wrong, each with the exact fix.`, { label: `verify:${nn}`, phase: 'Verify', schema: FINDINGS })
    return { ...st, remaining: v }
  },
)
return results.filter(Boolean).map(r => ({ chapter: r.chapter, fixed: r.fix ? r.fix.key_results : null, all_checks_pass: r.fix ? r.fix.all_checks_pass : null, failing: r.fix ? r.fix.failing : null, open_items: r.fix ? r.fix.open_items : null, files_changed: r.fix ? r.fix.files_changed : null, rejected: (r.rejected || []).map(f => ({ index: f.i, why: (f.verdicts || []).filter(v => v.refuted).map(v => v.reason) })), remaining: r.remaining ? r.remaining.findings : null }))
