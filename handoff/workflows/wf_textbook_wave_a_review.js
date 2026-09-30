export const meta = {
  name: 'textbook-wave-a-review',
  description: 'Adversarial review of textbook wave A (chapters 00-05, 08-13): per-chapter correctness/pedagogy/reproducibility, cross-book honesty and consistency, skeptic verification, per-chapter fixers, assembler check',
  phases: [
    { title: 'Review', detail: '12 chapter reviewers + 2 cross-book reviewers' },
    { title: 'Verify', detail: 'one skeptic per chapter tries to refute every finding' },
    { title: 'Fix', detail: 'one fixer per chapter applies confirmed findings, test-builds' },
    { title: 'Final', detail: 'assembler check, tests, completeness critic' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const CH = 'provenance/textbook/chapters'
const CHAPTERS = [
  '00-how-to-read.md', '01-mathematical-toolkit.md', '02-clifford-algebras-and-spinors.md', '03-split-octonions.md',
  '04-curved-space.md', '05-classical-field-theory.md', '08-quantization.md', '09-primordial-field.md',
  '10-numerical-ode.md', '11-dark-sector-experiments.md', '12-density-functional-theory.md', '13-kohn-sham-primordial.md',
]

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main). NEVER run git commands that change the index, the working tree or the remote (no add/commit/checkout/reset/stash/push); read-only git (log, show, diff, ls-files) is fine. The textbook for complete beginners about the dirac16complex project: binding spec ${ROOT}/handoff/specs/TEXTBOOK_SPEC.md (read it fully first: the request, the HONESTY RULE of section 0, audience and style of section 1, the Markdown subset and build of section 2). Chapters live in ${ROOT}/${CH}/; wave A (00-05, 08-13) is written, wave B (06, 07, 14-20) is not written yet, so forward references to chapters 6, 7, 14-20 are expected and are NOT findings. Stage 4 (Kohn-Sham) is being finalised by the lead and Stage 5 (dirac16complex00, pairing theorems) and the matter-antimatter analysis are in progress: the Stage-4 cross-check STATUS sentences ("was still being completed", ledger rows L33-L35, L36-L43, the Stage-4/5 rows of the stage table) are refreshed by wave B and are NOT findings; but a number that disagrees with the COMMITTED report it cites IS a finding. Never modify dirac-main/, vendor/, the author's notebook Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb, or any file outside the textbook chapters. Large files: read in chunks of at most 300 lines per tool call. Scratch only under ${SP}/textbook_review/<your label>/ or the git-ignored ${ROOT}/build/textbook_review/<your label>/ (build_provenance_pdf.py refuses Markdown outside the repository, so test builds use a copy under build/ with a first line "# Test" and a second line "## Test build"). Test build command: python scripts/build_provenance_pdf.py build/textbook_review/<label>/<file>.md --developer-layout --number-sections-from-zero (verify mode; only the registry checks may fail for an unregistered test edition; the log must be warning-free).
`
const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          chapter: { type: 'string', description: 'chapter file name, e.g. 04-curved-space.md' },
          severity: { type: 'string', enum: ['critical', 'major', 'minor'] },
          lens: { type: 'string' },
          location: { type: 'string', description: 'section number and a verbatim quote of the offending text (<= 200 chars)' },
          problem: { type: 'string' },
          evidence: { type: 'string', description: 'the re-derivation, the report value, the command output, etc.' },
          fix: { type: 'string', description: 'the exact replacement or addition' },
        },
        required: ['chapter', 'severity', 'lens', 'location', 'problem', 'evidence', 'fix'],
      },
    },
    verified_ok: { type: 'array', items: { type: 'string' }, description: 'what you checked and found correct (short lines)' },
  },
  required: ['findings', 'verified_ok'],
}
const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          index: { type: 'integer' },
          confirmed: { type: 'boolean' },
          reason: { type: 'string' },
          corrected_fix: { type: 'string', description: 'the fix to apply if the proposed one is wrong or incomplete; empty if the proposed fix is right' },
        },
        required: ['index', 'confirmed', 'reason', 'corrected_fix'],
      },
    },
  },
  required: ['verdicts'],
}
const FIXRESULT = {
  type: 'object',
  properties: {
    applied: { type: 'array', items: { type: 'string' } },
    not_applied: { type: 'array', items: { type: 'string' } },
    test_build_warning_free: { type: 'boolean' },
    summary: { type: 'string' },
  },
  required: ['applied', 'not_applied', 'test_build_warning_free', 'summary'],
}

const LEAD_NOTES = {
  '00-how-to-read.md': [
    { chapter: '00-how-to-read.md', severity: 'major', lens: 'lead', location: 'Section 0.12, Answer 0.5(a): "conservation of charge and energy allows a photon of enough energy to turn into an electron and a positron"', problem: 'A single free photon cannot turn into an electron-positron pair in vacuum: energy and momentum cannot both be conserved. Physics error in a pedagogical example.', evidence: 'For a photon E = |p|; for the pair E^2 - p^2 >= (2 m_e)^2 > 0, so the invariant mass cannot match; pair creation needs a nucleus (or a second photon) to take up momentum.', fix: 'Say "allow a photon of enough energy passing near an atomic nucleus, which takes up the recoil momentum, to turn into an electron and a positron" (or use two photons).' },
    { chapter: '00-how-to-read.md', severity: 'minor', lens: 'lead', location: 'Section 0.9, ledger row L2: "(the task\'s expression [1])"', problem: 'A student does not know what "the task" or "[1]" is.', evidence: 'The phrase refers to the project contract, not introduced in the book.', fix: 'Replace by "(the combination $C\\gamma^a$ that appears in the notebook\'s Lagrangian)" or drop the parenthesis.' },
  ],
  '05-classical-field-theory.md': [
    { chapter: '05-classical-field-theory.md', severity: 'minor', lens: 'lead', location: 'end of Section 5.8: "the task\'s scalar-field reference"', problem: 'Meaningless to a student; the reference is a private PDF not in the repository.', evidence: 'The private reference PDF is git-ignored and not part of the book.', fix: 'Say "the standard scalar-field formulas" (and, if a source is wanted, a standard cosmology textbook).' },
  ],
  '13-kohn-sham-primordial.md': [
    { chapter: '13-kohn-sham-primordial.md', severity: 'minor', lens: 'lead', location: 'Section 13.1, "a repeated run is byte-identical in all 327 files compared, and a run with ten times tighter tolerances agrees to 6.0e-8 relative"', problem: 'The committed artifacts/dirac16complex/kohn-sham/rust/determinism-report.json was regenerated on 2026-09-30 08:37.', evidence: 'Read the committed determinism-report.json: repeat files compared and differing, refined runs, levels and max relative energy (the lead measured 330 files identical, 65 runs, 364829 levels, 5.96e-8).', fix: 'Quote the numbers of the committed report exactly; re-read the five rust/*/summary.json check counts as well.' },
  ],
}

// ---------------- Review ----------------
phase('Review')
const chapterReviewer = (file) => agent(`${COMMON}
TASK (adversarial reviewer of ONE chapter: ${CH}/${file}). Do not edit any repository file. Read the whole chapter, and the sources it names (project documents in provenance/, specs in handoff/specs/, the committed reports and outputs under artifacts/, the scripts it quotes). Apply three lenses and report only REAL problems with concrete evidence:
1. CORRECTNESS: re-derive every derivation step yourself (write small sympy/numpy scripts in scratch where useful); recompute every worked example, table entry and number; open every committed report the chapter cites and compare every quoted number and every check name (does the check exist in that report, is it true, does it say what the chapter claims); check every exercise answer.
2. PEDAGOGY for a reader who knows only school algebra and one-variable calculus: every notion used before it is defined (in this chapter or an earlier chapter 00-05, 08-13 - check where it is defined), every skipped step, every "it can be shown", every unclear sentence, every exercise without a complete correct answer.
3. REPRODUCIBILITY: every file path exists; every command and code snippet the chapter gives that finishes within about 5 minutes is run (from a scratch copy if it writes files) and its output compared with what the chapter says; figure paths exist.
Also check the Markdown subset rules of TEXTBOOK_SPEC section 2 (headings "## N. Title" / "### N.M Title", nothing deeper; fenced code lines <= 89 characters, no tabs; figure lines only; tables with equal cell counts) and test-build the chapter alone once (see CONTEXT) - a warning is a finding.
In verified_ok list what you checked and found correct.`, { label: 'review:' + file.slice(0, 2), phase: 'Review', schema: FINDINGS })

const crossReviewers = [
  ['honesty', `TASK (cross-book HONESTY reviewer over all wave-A chapters). Do not edit any file. Hunt for overclaims: every statement called proved, derived, shown, established, verified or confirmed must be proved in the book or by a named committed check, with its exact hypotheses; checks at test points must not be presented as general proofs; interpretation must be labelled; the pair-creation and matter-antimatter statements must follow TEXTBOOK_SPEC section 0 exactly (no claim that the big bang creates universes in pairs, no claim that the theory solves the matter-antimatter problem). Check every row of the honesty ledger of Chapter 0 (Section 0.9) against the chapters and the committed reports it names (status word, check names exist and are true, chapter pointers right) - except the Stage-4/5 status rows that wave B refreshes (see CONTEXT). Check each chapter's "What we proved and what we assumed" section against the chapter body. Report findings with chapter file names.`],
  ['consistency', `TASK (cross-book CONSISTENCY reviewer over all wave-A chapters). Do not edit any file. Check that the chapters agree with each other: notation for the same object (gamma matrices, C, B, gamma^8, the current J^mu = -i Psibar gamma^mu Psi and its sign, S = Psibar Psi, eta, the hidden coordinate (zeta, y, z), the Kohn-Sham block labels j and s = -j, index letters), sign conventions (energy-momentum tensor, Einstein equations, Israel junction), the same number quoted in two chapters, the same derivation done twice with different results, and every "Chapter N" / "Section N.M" cross-reference among wave-A chapters pointing to the content it claims (run python scripts/build_textbook.py --check --allow-missing --list-references). Report findings with chapter file names; for a notation clash say which chapter should change and why.`],
]

const reviewResults = await parallel([
  ...CHAPTERS.map(f => () => chapterReviewer(f)),
  ...crossReviewers.map(([k, t]) => () => agent(`${COMMON}\n${t}`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })),
])
const allFindings = reviewResults.filter(Boolean).flatMap(r => r.findings || [])
log('wave-A review: ' + allFindings.length + ' findings from ' + reviewResults.filter(Boolean).length + ' reviewers (' + reviewResults.filter(r => !r).length + ' reviewers failed)')

// group by chapter; lead notes are included and pre-verified by the lead but still go through the skeptic
const byChapter = {}
for (const f of allFindings) {
  const key = CHAPTERS.find(c => (f.chapter || '').includes(c.slice(0, 2) + '-')) || CHAPTERS.find(c => (f.chapter || '').includes(c)) || 'unassigned'
  ;(byChapter[key] = byChapter[key] || []).push(f)
}
for (const [c, notes] of Object.entries(LEAD_NOTES)) (byChapter[c] = byChapter[c] || []).push(...notes)
if (byChapter.unassigned) log('unassigned findings (no chapter file recognised): ' + byChapter.unassigned.length)
const work = CHAPTERS.filter(c => (byChapter[c] || []).length)
log('chapters with findings: ' + work.map(c => c.slice(0, 2) + ':' + byChapter[c].length).join(', '))

// ---------------- Verify + Fix (pipeline per chapter) ----------------
const fixed = await pipeline(
  work,
  (file) => agent(`${COMMON}
TASK (skeptic for ${CH}/${file}). Do not edit any file. Below are numbered findings against this chapter. For EACH one, try hard to REFUTE it: re-read the exact text, re-derive, open the cited report, run the command. confirmed=true only if the problem is real; if the proposed fix is wrong, incomplete or would introduce an error, give the correct fix in corrected_fix. Findings marked lens "lead" come from the lead and are expected to be right, but still check them.
FINDINGS (JSON, index = position): ${JSON.stringify(byChapter[file].map((f, i) => ({ index: i, ...f }))).slice(0, 60000)}`, { label: 'verify:' + file.slice(0, 2), phase: 'Verify', schema: VERDICTS }),
  (verdict, file) => {
    const list = byChapter[file]
    const confirmed = (verdict && verdict.verdicts ? verdict.verdicts : []).filter(v => v.confirmed && list[v.index]).map(v => ({ ...list[v.index], skeptic: v.reason, fix: v.corrected_fix && v.corrected_fix.trim() ? v.corrected_fix : list[v.index].fix }))
    const rejected = (verdict && verdict.verdicts ? verdict.verdicts : []).filter(v => !v.confirmed).length
    if (!confirmed.length) return { file, applied: [], not_applied: [], test_build_warning_free: true, summary: 'no confirmed findings (' + rejected + ' rejected)' }
    return agent(`${COMMON}
TASK (fixer for ${CH}/${file} ONLY; edit no other file). Apply every confirmed finding below at its root, keeping the chapter's style, numbering (sections "### N.M", exercises and answers), cross-references and the Markdown subset; when a fix changes a number or statement that the chapter's "What we proved and what we assumed" section, its exercises or its answers repeat, update those too. Do not touch the Stage-4/5 status sentences that wave B refreshes (see CONTEXT). Then test-build the chapter alone (see CONTEXT) until warning-free. In applied / not_applied give one line per finding (with the reason for anything not applied).
CONFIRMED FINDINGS (JSON): ${JSON.stringify(confirmed).slice(0, 80000)}`, { label: 'fix:' + file.slice(0, 2), phase: 'Fix', schema: FIXRESULT }).then(r => ({ file, rejected, ...(r || {}) }))
  },
)

// ---------------- Final ----------------
phase('Final')
const final = await agent(`${COMMON}
TASK (final check and completeness critic; you may make MINIMAL edits to the wave-A chapter files only to repair a numbering, cross-reference or build problem you find). Run python scripts/build_textbook.py --check --allow-missing (and --list-references) and python -m unittest tests.test_d16c_textbook_assembler -v; test-build every wave-A chapter alone once more (see CONTEXT) and report any warning. Then act as a completeness critic: which lens or chapter was not really covered, which claim was not verified, which cited report was not opened? Fix-results of this workflow (JSON, truncated): ${JSON.stringify(fixed).slice(0, 30000)}`, { label: 'final', phase: 'Final', schema: { type: 'object', properties: { assembler_ok: { type: 'boolean' }, tests_ok: { type: 'boolean' }, all_chapters_warning_free: { type: 'boolean' }, edits: { type: 'array', items: { type: 'string' } }, gaps: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['assembler_ok', 'tests_ok', 'all_chapters_warning_free', 'edits', 'gaps', 'summary'] } })

return { findingsTotal: allFindings.length, perChapter: Object.fromEntries(Object.entries(byChapter).map(([k, v]) => [k, v.length])), fixed, final }
