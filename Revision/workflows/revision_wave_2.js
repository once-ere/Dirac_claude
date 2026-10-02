export const meta = {
  name: 'revision-wave-2',
  description: 'Revision/ wave 2: the two dark-sector hypotheses against the Unite values, a4 equations with the Kohn-Sham source, Kohn-Sham pairing T3, the remaining documents, Jupyter notebooks, the Revision gate, reviews, fixer',
  phases: [
    { title: 'Science', detail: 'dark sector (both fields), a4 with the KS source, KS pairing T3' },
    { title: 'Documents', detail: 'Kohn-Sham, dark sector, Lovelock/GKD; update the three wave-1 documents' },
    { title: 'Notebooks and gate', detail: 'Jupyter notebooks (rustSolveIt style), verify_revision.{ps1,sh}' },
    { title: 'Review', detail: 'five lenses, two skeptics per finding' },
    { title: 'Fix', detail: 'per-area fixers, fix verifier, second round' },
  ],
}

const ROOT = 'D:/Developer/github/Dirac_claude'
// ROOT: the repository on the machine where these waves ran; SP: the scratchpad directory of the session that
// runs the script (set it in the session's own copy before launching; see Revision/README.md, workflows/).
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
const R = 'Revision'

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main). NEVER run git commands that change the index, the working tree or the remote; read-only git is fine. You work ONLY inside ${ROOT}/${R}/ (plus scratch). BINDING: ${ROOT}/${R}/SPEC.md (read it fully: the no-mixing rule, the author's metric and coordinate roles - x5, x6, x7 are the exponentially DEFLATING extra times - and sections 7, 8, 9, 11) and ${ROOT}/${R}/README.md. Read every wave-1 result first: ${R}/algebra, ${R}/theory, ${R}/field_equations_a4, ${R}/pairing, ${R}/gkd_lovelock, ${R}/kohn_sham, ${R}/docs. NO-MIXING RULE: nothing from the old stages is used as a Revision result. HONESTY: numbers only from Revision outputs; hypotheses investigated, never assumed; interpretation labelled; never "proved" for anything not proved. The author's private PDF (never committed, never quoted beyond these numbers): the Supernovae Unite constant-w fit w = -0.764 (Unite SN alone, about 2 sigma from -1); the time-evolving CPL fit w(a) = w0 + wa (1 - a) with (w0, wa) = (-0.861, -0.60) (deep past w0 + wa = -1.46, phantom); quintessence rho = phidot^2/2 + V, P = phidot^2/2 - V; thawing means wa < 0 in this convention (the PDF's table states the opposite signs; the formula decides). Tooling as in wave 1 (PDFs via python scripts/build_provenance_pdf.py <md> --developer-layout --specifications ${R}/pdf-specifications.json [--register]). Deterministic outputs; checks in JSON reports. Read files in chunks of at most 300 lines. Scratch only under ${SP}/revision2/<label>/.
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const run = (label, ph, task) => agent(`${COMMON}\nTASK (${label}): ${task}`, { label, phase: ph, schema: RESULT })

phase('Science')
const science = await parallel([
  () => run('dark-sector-dirac16complex', 'Science', `Own ${R}/dark_sector/dirac16complex/ (code, outputs, reports). Investigate the Hypothesis for dirac16complex (SPEC sections 8 and 11): the equation of state a 3-space observer infers as the extra times deflate and 3-space inflates (a = e^{a4}), for (i) the Kohn-Sham fermion gas of ${R}/kohn_sham (instantaneous states along a4; the 3-space pressure p3, the extra-time pressure p_t, the hidden pressure p8, rho; the 4-dimensional effective density rho_4 obtained by integrating over the hidden direction and the extra times, the dilution-inferred w_eff = -1 - (1/3) d ln rho_4 / d ln a and the ratio w = p3/rho), (ii) homogeneous condensates (the exact solutions of the field equations in this metric), (iii) mixtures; derive every effective formula exactly (sympy) before computing; the extra times x5..x7 are TIME-LIKE: integrating over them to define rho_4 (a compact range of time-like coordinates means closed time-like directions; a non-compact range needs a normalisation per unit extra-time volume) is an ASSUMPTION about the observer - state it, give the alternatives (per unit proper 7-volume, per unit extra-time coordinate volume) and show how the verdict depends on the choice; use the exact conservation identities nabla_mu T^mu_x4: d rho/d x4 = -3 a4' (p3 - p_t) and nabla_mu T^mu_x8: d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0 (re-derive them) as checks of every source you use; compute w(a), its CPL tangent at a = 1 and fits over stated ranges of a, compare with w = -0.764 and (w0, wa) = (-0.861, -0.60); say exactly where a time-varying DARK-MATTER equation of state appears (expected: the gas, 1/3 -> 0) and whether any time-varying DARK-ENERGY equation of state near the Unite values appears, with the reasons; checks and an independent second implementation of the key numbers.`),
  () => run('dark-sector-dirac16complex00', 'Science', `Own ${R}/dark_sector/dirac16complex00/. Investigate Hypothesis00 for the semi-classical dirac16complex00 field: classical solutions in the deflating field (homogeneous condensates, superpositions of good-sector modes, wave packets; the indefinite (Krein-signed) classical energy of modes of both Krein signs; the extra-time-momentum modes whose growth is driven by the deflation), the 3-space observer's equation of state as in the dirac16complex task (rho_4, w_eff, w = p3/rho) with the same stated observer assumptions and conservation checks, whether negative classical energy densities allow w < -1 (phantom) and a crossing of w = -1 near the Unite trajectory, and what that would require (a classical field with negative-energy components is a ghost-like sector: say so); CPL tangent and fits; comparison with w = -0.764 and (w0, wa) = (-0.861, -0.60); exact derivations (sympy) before numerics; checks and an independent second implementation of the key numbers.`),
  () => run('a4-with-ks-source', 'Science', `Own ${R}/field_equations_a4/ks_source/. Specialise the a4 field equations of ${R}/field_equations_a4/a4-equations.json to the Kohn-Sham states of ${R}/kohn_sham (the instantaneous energy-momentum tensor profiles as the source; the hidden-direction dependence the source must have versus the profiles actually computed - quantify the mismatch honestly) (the wave-1 fixer already showed in ${R}/field_equations_a4/reports/ks-source-conditions.json that every nonzero Kohn-Sham state depends on x8 and violates p3 + p_t = 2 p8, i.e. the x8 conservation identity d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0 - start from that, verify it, and decide what, if anything, can still be integrated: e.g. hidden-direction averages with the violation quantified, stated as an approximation), for Einstein gravity and for Einstein-Lovelock with stated alpha_2, alpha_3, and integrate the a4 evolution equation where it is well defined (state the assumptions); does the dirac16complex source drive exponential deflation of the extra times? Report what the equations allow.`),
  () => run('ks-pairing-T3', 'Science', `Own ${R}/pairing/kohn_sham/. T3 was already proved exactly by the wave-1 fixer there (Wolfram 10/10, sympy 13/13, t3-theory.json): verify that proof adversarially and complete it where needed, then make sure everything below exists. Prove T3 (the Kohn-Sham level pairing: the block map with the transformed boundary conditions maps the instantaneous Kohn-Sham problem with (m, lambda) to the one with (-m, +lambda) with equal energies and energy-momentum tensors) exactly (sympy/Wolfram) for the Revision Kohn-Sham model, and demonstrate it numerically with the Revision Rust solver and reference (+M and -M universes on the deflating slice series; the untransformed boundary condition as the negative control). The Kohn-Sham history a4 = A H x4 is a PRESCRIBED BACKGROUND (the states violate the a4 source conditions; ${R}/field_equations_a4/reports/ks-source-conditions.json): say so wherever it is used.`),
])

phase('Documents')
const docs = await parallel([
  ['doc-kohn-sham', `${R}/docs/KOHN_SHAM_DEFLATING_FIELD.md (+ tex, pdf, registered): the Kohn-Sham model of dirac16complex in the author's primordial field with the deflating extra times, the instantaneous ground and first excited states along the history, the thermodynamic effective potential, the adiabaticity, the cross-check, the energy-momentum tensor, what is not done (TDDFT).`],
  ['doc-dark-sector', `${R}/docs/DARK_SECTOR_HYPOTHESES.md (+ tex, pdf, registered): the two hypotheses, the method, the results for each field, the comparison with the Unite values (constant w = -0.764; CPL (-0.861, -0.60)), the verdict for dark energy and for dark matter for each field, stated exactly and honestly.`],
  ['doc-lovelock', `${R}/docs/LOVELOCK_GKD.md (+ tex, pdf, registered): GKD (the author's kδ, its proof and tests), the construction of the three Lovelock tensors of (4.38) for the author's metric step by step for an ignorant student, every component, the checks, the independent verifications, the provenance of the computation (what was read; the commit order), and the field equations for a4[x4].`],
  ['doc-updates', `Update the wave-1 documents ${R}/docs/DIRAC16COMPLEX_FIELD_THEORY.md, DIRAC16COMPLEX00_FIELD_THEORY.md and PAIR_CREATION_PROOFS.md with the wave-2 results (the a4 equations with the Kohn-Sham source, T3, the dark-sector verdicts, pointers to the new documents); rebuild and re-register their PDFs; update their publication tests.`],
].map(([label, task]) => () => run(label, 'Documents', `Write ${task} Numbers and formulas only from the Revision reports. Build the PDF (verify mode until warning-free), register it in ${R}/pdf-specifications.json (re-read first; change only your entry), write or update ${R}/tests/test_<document>_publication.py and run it.`)))

phase('Notebooks and gate')
const nbgate = await parallel([
  () => run('notebooks', 'Notebooks and gate', `Own ${R}/notebooks/. Jupyter notebooks in the style of the author's rustSolveIt repositories (read ${ROOT}/vendor/rustSolveIt/planet_Mercury/notebook/*.ipynb first: numbered sections - what it computes, how to run it on Windows (rustSolveIt_Win11), macOS (rustSolveIt_macos-silicon) and Linux (rustSolveIt_linux), the words used, the physical situation, a Python driver cell that builds and runs the Revision Rust programs with subprocess, the program reciting its configuration, tables and checks): (1) the Lovelock tensors with GKD, (2) the Kohn-Sham states in the deflating field, (3) the dark-sector hypotheses; deterministic builders, executed with nbclient so the committed notebooks contain outputs, and tests that re-execute them.`),
  () => run('gate', 'Notebooks and gate', `Own ${R}/verify_revision.ps1 and ${R}/verify_revision.sh (twins) and ${R}/tests/test_revision_gate.py. Following the pattern of the repository's stage gates (read one, e.g. scripts/verify_stage3_dark_sector.sh, for the structure only), re-run every Revision verifier, checker, solver run and figure/PDF build into build/revision/, compare with the committed outputs byte for byte, run python -m unittest discover -s Revision/tests, and print revision_verification=OK at the end; a --dry-run and a --steps option; document the expected wall time per step; test the fast steps.`),
])

// ---------------- Review: lenses -> adversarial skeptics per finding (pipeline, no barrier) ----------------
phase('Review')
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, reason: { type: 'string' }, evidence: { type: 'string' } }, required: ['refuted', 'reason', 'evidence'] }
const lenses = [
  ['correctness', 'Check every derivation, formula and number of all Revision documents against the reports; re-derive the key steps of the dark-sector effective formulas (rho_4, w_eff, w = p3/rho, the CPL tangent) and of T3 yourself.'],
  ['honesty', 'Hunt for overclaims (the hypotheses, the pair creation, the Kohn-Sham approximation, the a4 dynamics, the Unite comparison) and for any mixing with the old stages.'],
  ['physics', 'Judge the physics of the dark-sector investigation (rho_4, the 3-space observer, the extra-time and hidden pressures, the Krein-signed energies, phantom crossing, the Unite comparison), of the a4 equations with the Kohn-Sham source and of the deflation.'],
  ['reproducibility', 'From a fresh git clone of the committed state plus a copy of the uncommitted Revision files in scratch, run the Revision gate fast steps, every checker, the notebooks and the PDF builds in verify mode; compare byte for byte; look for absolute paths, nondeterminism, missing files.'],
  ['completeness', 'Compare Revision/README.md (the task verbatim) and SPEC sections 0-11 item by item with what Revision/ now contains; list every requested item that is missing, partial or only asserted.'],
]
const judged = await pipeline(
  lenses,
  ([k, t]) => agent(`${COMMON}\nTASK (adversarial reviewer, lens ${k}; do not edit files): ${t} Report only real problems with concrete evidence.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS }),
  (rev, [k]) => parallel(((rev && rev.findings) || []).map((f, i) => () =>
    parallel(['re-derive it independently', 'check the cited evidence in the files'].map((how, j) => () =>
      agent(`${COMMON}\nTASK (skeptic ${j + 1}, do not edit files): try to REFUTE this ${k} finding by trying to ${how}. Finding: ${JSON.stringify(f)}. Set refuted=true only if the finding is wrong or not a real problem; give concrete evidence either way.`, { label: `skeptic:${k}:${i}:${j}`, phase: 'Review', schema: VERDICT })))
      .then(vs => ({ ...f, lens: k, votes: vs.filter(Boolean), confirmed: vs.filter(Boolean).filter(v => !v.refuted).length >= 1 })))),
)
const allFindings = judged.filter(Boolean).flat().filter(Boolean)
const confirmed = allFindings.filter(f => f.confirmed)
log(`review: ${allFindings.length} findings, ${confirmed.length} survived the skeptics, ${allFindings.length - confirmed.length} refuted by both`)

// ---------------- Fix: per area, science before documents before notebooks/gate; then verify the fixes ----------------
phase('Fix')
const area = f => /(^|\/)docs\//.test(f.file || '') ? 'docs' : /(notebooks\/|verify_revision|(^|\/)tests\/)/.test(f.file || '') ? 'other' : 'science'
const fixRound = async (items, round) => {
  const out = []
  for (const a of ['science', 'docs', 'other']) {
    const mine = items.filter(f => area(f) === a)
    if (!mine.length) continue
    const payload = JSON.stringify(mine)
    if (payload.length > 90000) log(`fix ${a} round ${round}: findings JSON ${payload.length} chars, split into chunks`)
    for (let c = 0; c * 90000 < payload.length; c++) {
      const chunk = mine.slice(Math.floor(c * mine.length / Math.ceil(payload.length / 90000)), Math.floor((c + 1) * mine.length / Math.ceil(payload.length / 90000)))
      out.push(await run(`fix:${a}:${round}:${c}`, 'Fix', `Confirmed findings with skeptic votes (JSON): ${JSON.stringify(chunk)}\nRe-verify each; fix confirmed ones at their ROOT inside ${R}/ (regenerate reports deterministically, rebuild and re-register PDFs, rerun the affected tests and notebooks; a science fix must propagate to every document and notebook that quotes the changed number); reject only with evidence. One line per finding in key_results: FIXED / REJECTED (reason).`))
    }
  }
  return out
}
let fixes = confirmed.length ? await fixRound(confirmed, 1) : []
let fixCheck = null
if (confirmed.length) {
  fixCheck = await agent(`${COMMON}\nTASK (fix verifier, do not edit files): The fixers report (JSON): ${JSON.stringify(fixes).slice(0, 60000)}\nFor every finding marked FIXED, check in the files that it is really fixed at the root and that the fix introduced no inconsistency (numbers in documents, notebooks, tests and reports agree; tests pass: python -m unittest discover -s ${R}/tests). For every REJECTED one, judge the rejection. Report remaining problems as findings.`, { label: 'fix-verifier', phase: 'Fix', schema: FINDINGS })
  const rest = (fixCheck && fixCheck.findings) || []
  if (rest.length) fixes = fixes.concat(await fixRound(rest.map(f => ({ ...f, lens: 'fix-verifier' })), 2))
}
return { science, docs, nbgate, findings: allFindings, confirmed: confirmed.length, fixes, fixCheck }
