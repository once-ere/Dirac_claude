export const meta = {
  name: 'completion-phase-3c-book',
  description: 'Completion phase 3c (book): whole-book review with 5 lenses (consistency, references, honesty R3, notebooks and figures, deep-dive); 2 skeptics per finding; fixers per chapter; fix-verifiers',
  phases: [
    { title: 'Review', detail: 'Revision lenses: correctness, honesty, physics, reproducibility, completeness; book lenses: cross-chapter consistency, cross-references, honesty R3, figures and notebooks, deep-dive spot checks, fresh-clone reproducibility' },
    { title: 'Skeptics', detail: 'two independent refutation attempts per finding; a finding survives only if neither refutes it' },
    { title: 'Fix', detail: 'one fixer per owner area with its confirmed findings' },
    { title: 'Verify', detail: 'adversarial fix-verifier per area' },
  ],
}
const ROOT = 'D:/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad'
const R = 'Revision'
const T = 'Revision/textbook'
const NOAGREE = "NEVER accept licence terms, source agreements, cookie banners or any other agreement on the user's machine or accounts (never pass --accept-source-agreements / --accept-package-agreements to winget, never run wolframscript -activate, never accept an EULA)."
const BOUND = `BOUNDED TASK (user rule: no hours-long agent jobs): small verified steps; after every step append one line to ${SP}/phase3c/<your label with ':' replaced by '-'>.progress.md. Aim to finish within about 45 minutes; if not finished, stop at a consistent, verified state and list exactly what remains. Never leave a half-edited file. Do not commit (the lead commits).`
const CTX = `${NOAGREE}
CONTEXT: repository ${ROOT} (git, branch main; Windows 11; Python 3.14 with numpy, sympy, mpmath, matplotlib, nbformat, nbclient; WolframScript 1.14 / Wolfram 15.0.1; Rust cargo 1.91; pdflatex). NEVER run git commands that change the index, the working tree history or the remote (read-only git and clones into scratch are fine). The AUTHOR's notebooks are read only; never modify the original textbook provenance/DIRAC16COMPLEX_TEXTBOOK.* or provenance/textbook/. BINDING: ${R}/SPEC.md (the author's coordinates: x1..x3 space, x4 time, x5, x6, x7 the exponentially DEFLATING extra times, x8 hidden; the no-mixing rule; sections 7-11), ${R}/README.md, ${T}/TEXTBOOK_SPEC.md (R0-R6, deep-dive section 1, notebooks section 2, instructions section 3). HONESTY: numbers only from Revision outputs; hypotheses investigated, never assumed; interpretation labelled; nothing called proved that is not proved; the pair-creation request is answered exactly as in ${R}/docs/PAIR_CREATION_PROOFS.md section 11.3. Read files in chunks of at most 300 lines. Scratch only under ${SP}/phase3c/<your label>/.`
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }

const LENSES = [
  ['book-consistency', 'the textbook', `Cross-chapter consistency of ${T}/chapters/*.md: the same quantity, count or statement quoted in several chapters (check counts of the Revision reports, the U(1) charge statement, the T3 statement, the dark-sector verdicts, the a4 conclusions, the KS cross-check 31/31, the status labels PROVED/COMPUTED/ASSUMED/OPEN) must agree with each other and with the records; list every disagreement.`],
  ['book-references', 'the textbook', `Every cross-reference in ${T}/chapters/*.md ("Section x.y", "Chapter n", "Figure NNx.k", "Notebook NNx", "In [k]", "Exercise n.m", equation numbers) must point to something that exists and says what the reference claims; assemble the book with python ${T}/tools/assemble_textbook.py (into scratch if it supports it; otherwise read its code first and do NOT overwrite the committed book) and report its problems.`],
  ['book-honesty', 'the textbook', `R3 over the WHOLE book (${T}/chapters/*.md and every notebook's markdown and printed text): no sentence may claim that universes are created in pairs, that matter-antimatter asymmetry is explained, that dark energy or dark matter is explained, that the total U(1) charge is conserved without the no-flux condition, or that anything is proved that the Revision record does not prove; R5 (charge conjugation is a matrix). Search systematically (grep for proved, prove, created, creation, explain, conserved, solves, establish, dark energy, dark matter, asymmetry) and judge each hit in context.`],
  ['book-notebooks', 'the textbook', `Notebooks and figures: every chapter has its notebooks, every notebook has its builder, PROVENANCE file, run-instruction paragraph before it in the chapter and a walk-through after it; TEXTBOOK_SPEC targets: at least 4 figures per chapter (chapters 0 and 23 excepted) and at least 100 in the book, every figure with a teaching caption; run python ${T}/tools/audit/walkthrough_all.py and judge every report by hand; run python ${T}/tools/nbkit.py lint on every builder.`],
  ['book-deepdive', 'the textbook', `Deep-dive spot checks (TEXTBOOK_SPEC section 1): pick at least 4 derivations from each of chapters 01-22 (spread over each chapter) and check that every line is written out with the rule that produced it (no "it can be shown", no "similarly", no skipped algebra), every technical word is defined at first use, and the exercises have complete worked answers; report only real gaps with their location.`],
]

const area = f => {
  const p = (f.file || '').replace(/\\/g, '/').replace(/^.*Dirac_claude\//, '')
  const m = p.match(/^Revision\/textbook\/(?:chapters\/(\d\d)|notebooks\/(?:src\/)?(\d\d)|figures\/(\d\d))/)
  if (m) { const nn = m[1] || m[2] || m[3]; return `chapter-${nn}` }
  if (p.startsWith('Revision/textbook/')) return 'textbook-other'
  if (p.startsWith('Revision/docs/')) return 'revision-docs'
  const r = p.match(/^Revision\/([a-z0-9_]+)\//)
  if (r) return `revision-${r[1]}`
  if (p.startsWith('Revision/')) return 'revision-top'
  return 'other'
}
const AREA_OWNS = a => a.startsWith('chapter-')
  ? `You own chapter ${a.slice(8)} (${T}/chapters/${a.slice(8)}-*.md) and its builders, notebooks, PROVENANCE files and figures (${T}/notebooks/src/${a.slice(8)}*.py, ${T}/notebooks/${a.slice(8)}*, ${T}/figures/${a.slice(8)}*). Rebuild every notebook whose builder you change (python ${T}/tools/nbkit.py build <builder> --date 2026-10-08), run nbkit check on every notebook of the chapter, the walk-through audit, and python ${T}/tools/check_chapter.py until chapter_check=OK with no problem= or latex_warning= lines.`
  : a === 'revision-docs'
    ? `You own ${R}/docs/*.{md,tex,pdf}, their entries in ${R}/pdf-specifications.json (re-read right before each --register) and their publication tests ${R}/tests/test_*_publication.py: rebuild every changed document (verify mode until warning-free, two builds byte-identical, then --register) and run its test with REVISION_PDF_REBUILD=1.`
    : `You own the files of the area ${a} (${a.startsWith('revision-') ? R + '/' + a.slice(9) + '/' : 'the files named in the findings'}): fix them, re-run the programs that produce any changed output and require byte-identical re-runs, run the tests that cover them, and list every downstream document or notebook that quotes a changed output (do not edit those; put them in open_items).`

phase('Review')
const judged = await pipeline(LENSES,
  ([key, subject, task]) => agent(`${CTX}\n${BOUND}\nTASK (reviewer ${key} of ${subject}; adversarial; do NOT edit files): ${task} Report only real problems with concrete evidence (file, location, quoted text, the record or computation that contradicts it, the exact fix).`, { label: `review:${key}`, phase: 'Review', schema: FINDINGS }),
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
const fixes = await pipeline(Object.entries(byArea),
  ([a, fs]) => agent(`${CTX}\n${BOUND}\nTASK (fixer of area ${a}): ${AREA_OWNS(a)} Fix every one of these findings, each confirmed by two independent skeptics, at the root (JSON): ${JSON.stringify(fs).slice(0, 60000)}\nRe-verify each before editing; if you find a finding wrong after all, reject it with evidence. One line per finding in key_results: FIXED / REJECTED (reason).`, { label: `fix:${a}`, phase: 'Fix', schema: RESULT }),
  (fx, [a, fs]) => agent(`${CTX}\n${BOUND}\nTASK (fix-verifier of area ${a}; adversarial; do NOT edit files): Findings: ${JSON.stringify(fs).slice(0, 30000)}\nFixer report: ${JSON.stringify(fx || {}).slice(0, 30000)}\nFor EVERY finding check in the files that the fix is real and correct and broke nothing (re-run the checks, notebooks, builds and tests of the area). Report as findings only what is still wrong.`, { label: `verify-fix:${a}`, phase: 'Verify', schema: FINDINGS })
    .then(v => ({ area: a, findings: fs.length, fix: fx, remaining: v })),
)
return { confirmed, rejected: rejected.map(f => ({ lens: f.lens, file: f.file, problem: f.problem, why: f.skeptics.filter(s => s.refuted).map(s => s.reason) })), fixes }
