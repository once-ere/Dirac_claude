export const meta = {
  name: 'stage2-integrate-document-review',
  description: 'Stage 2: integrate primordial-field verifiers, write the primordial-field provenance document, review, fix, gate',
  phases: [
    { title: 'Integrate', detail: 'rerun both verifiers, cross-agreement, gate scripts' },
    { title: 'Document', detail: 'DIRAC16COMPLEX_PRIMORDIAL_FIELD md/tex/pdf' },
    { title: 'Review', detail: 'three adversarial lenses' },
    { title: 'Fix', detail: 'apply confirmed findings' },
    { title: 'Gate', detail: 'clean Stage-2 gate' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const ART = 'artifacts/dirac16complex/primordial-field'
const DOC = 'provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md'
const buildReports = args && args.buildReports ? JSON.stringify(args.buildReports).slice(0, 60000) : '(see ' + SP + '/stage2_build_result.json)'

const COMMON = `
CONTEXT: repository ${ROOT} (git, main; do NOT commit or push). Binding: ${SP}/CONTRACT.md INCLUDING its section 11 errata, and ${SP}/STAGE2_SPEC.md as corrected by the build reports below (measured truth wins: e.g. det g = +cos^2 z; p_(0) = L_s - K_0 is frozen only for K = 0 or eigenstates (Zitterbewegung at frequency 2E otherwise); the zeta plane wave is exact only for lambda = 0; Lichnerowicz (gamma^mu D_mu)^2 Psi = nabla^mu D_mu Psi - (R/4) Psi; F_mu_nu = (1/2) R_{ab mu nu} S^{ab}; on-shell T^mu_mu = -mS + 7SU' - 8U; T_4i vanishes on shell for homogeneous states in diagonal backgrounds; T_ij = (1/4) eps_i eps_j h_i h_j (H_i - H_j) Psibar g^i g^j g^4 Psi).
Stage-2 files (you may edit these only): wolfram/Dirac16ComplexPrimordial.wl, scripts/verify_dirac16complex_primordial.wls, scripts/check_dirac16complex_primordial.py, tests/test_d16c_primordial.py, ${ART}/*, ${DOC} (+ .tex/.pdf), tests/test_d16c_primordial_publication.py, scripts/verify_stage2_primordial_field.{ps1,sh}, and the provenance/pdf-specifications.json entry for dirac16complex-primordial-field (use scripts/build_provenance_pdf.py --register; do not touch other entries). Read-only: all Stage-1 files (wolfram/Dirac16Complex{Algebra,Geometry}.wl, scripts/*, the Stage-1 document provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md if present) and Stage-3 files (studies/, artifacts/dirac16complex/numerics/) which other workflows are editing concurrently.
Build reports: ${buildReports}
Tooling facts: WolframScript 1.14 drops arguments after "--" with -file: pass paths positionally (the verifiers accept positional arguments). The Markdown->LaTeX builder is scripts/build_dissertation_tex.py (read its header for the supported subset; pitfalls in ${SP}/survey_dirac-main-machinery.md); build PDFs only via python scripts/build_provenance_pdf.py <md> [--register].
Notation hazard in the Gmail PDF: its thawing/freezing table has the wa signs reversed relative to its own CPL formula (dw/da = -wa); mention only if relevant and then explicitly.
Tools: wolframscript, python 3.14 (stdlib, numpy, sympy; no scipy), pdflatex. Scratch only under ${SP}/stage2_doc_tmp/<label>/. Honesty: quote only numbers from the reports; label reconstructions as reconstructions (e.g. the cell-1058 diagnosis is a reconstruction confirmed by an exact 16/16 match, the notebook does not store useT16's value).
`
const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }

phase('Integrate')
const integ = await agent(`${COMMON}
TASK (integration): from ${ROOT}: wolframscript -file scripts/verify_dirac16complex_primordial.wls ${ART}/wolfram-primordial-report.json ; python scripts/check_dirac16complex_primordial.py (it must now find primordial-components.json and run P_EL_agreesWithWolfram; make sure its default invocation does so and records wolframAgreement=compared); python -m unittest discover -s tests -p "test_d16c_primordial*.py" -v. Fix the spec errors in the checks' expectations only where the measured truth is established (e.g. det g sign). Write the gate twins scripts/verify_stage2_primordial_field.{ps1,sh} (pattern of scripts/verify_stage1_arbitrary_field.*: run_logged steps into build/logs, positional wolframscript args, both verifiers, the tests, and the PDF verify step python scripts/build_provenance_pdf.py ${DOC}; final line stage2_primordial_field_verification=OK). Run them (the PDF step will fail until the document exists: report that).`, { label: 'integrate', phase: 'Integrate', schema: RESULT })

phase('Document')
const doc = await agent(`${COMMON}
Integration: ${JSON.stringify(integ).slice(0, 15000)}
TASK (author): write ${ROOT}/${DOC}: "dirac16complex in the primordial pair-creation gravitational field" (H1) with a mandatory H2 subtitle "Explicit components of the connection, field equations, energy-momentum tensor, quantization and equations of state". It repeats the Stage-1 calculations and records for the primordial field, with relabelled components x0..x7 and Psi_0..Psi_15. Required sections: Abstract; scope and non-claims; why this field is a reasonable primordial field (it is the field of the author's notebook Pair_Creation_of_Universes...nb: superluminal inflation of 3-space and deflation of the 3 extra times, hidden-space warp; state honestly what it requires as a source); the metric and vielbein (x-form, z = 6Hx0, t = Hx4, warped zeta form; det g = +cos^2 z, sqrt|g| = cos z; 7-volume constant in x4); Christoffel symbols (complete list, 37 nonzero); canonical spin connection (the 24 omega_{mu ab}; vielbein postulate: the total covariant derivative of the vielbein is zero, 512 components); Omega_mu closed forms; gamma^mu Omega_mu = 3H gamma^0 (a4 cancels) and D_mu gamma^nu = 0 (and the notebook contraction's failure, with an example component); the Lagrangian specialised to this field (formula and WolframScript form); the 16 component Euler-Lagrange equations written out explicitly (use primordial-components.json TeX strings; all eight coordinates), plus the (x0,x4) block form and the z,t evolution form; the comparison with the notebook's cell-1137 equations: identical term by term (M_notebook = -m/H) except the +-q yZ_j term, q = Q1 sinh(a4) a4' e^{-a4}, whose origin is the cell-1058 substitution rule (state the wrong rule and the correct one; state it is a reconstruction confirmed by an exact 16/16 reproduction of the stored cell-1079 eLa); energy-momentum tensor components (the 21 nonzero A_mu_nu; T_mu_nu in bilinears; off-diagonal structure); homogeneous sector: rho, p_(i) for every transverse direction, KE_L, PE_L, KE_H, PE_H, w, frozen in x4 and a4-independent (with the p_(0) Zitterbewegung caveat), conservation; modes (exact zeta reduction, E^2 = M^2 + K^2; non-separability of k != 0; WKB extra-time instability onset); Einstein tensor and the source this field would require in 8D Einstein gravity (rho_req = -3H^2(7 + a4'^2)/kappa < 0, pressures, energy conditions, a4 = t numbers, cell-150 alternatives), and the proof that the dirac16complex condensate cannot supply it; the gamma^8 (+-M) structural observation in this field (label as structural, not physical); canonical quantization in this field ({Psi, Psi^dagger} = B delta^7/cos z, Hamiltonian density, good sector); verification records (both implementations, check counts, 0 mismatches across 320 + 288 coefficients); exact PowerShell and Git Bash reproduction commands; limitations. Build with python scripts/build_provenance_pdf.py ${DOC} --register until warning-free and byte-identical; write tests/test_d16c_primordial_publication.py (md/tex sha256 pins, required phrases: "primordial", "pair-creation", "vielbein postulate", "canonical spin connection", "energy-momentum tensor", "equation of state", "cell 1058", "Krein").`, { label: 'document', phase: 'Document', schema: RESULT })

phase('Review')
const lenses = [
  ['physics', 'Independently recompute (own scripts) the connection, the 16 component equations (spot-check at least 4 components fully), the EMT components and homogeneous reductions, the Einstein tensor, energy conditions and the no-supply proof; refute anything wrong in the document or the code.'],
  ['notebook-comparison', 'Independently verify the notebook comparison: read ' + SP + '/nbo2.txt cells 1058, 1066, 1079, 1096, 1111, 1137, 583, 584; check the claimed wrong substitution rule, that the corrected equations differ from cell 1137 only by the q terms, and that the document states it fairly and precisely (reconstruction vs stored facts).'],
  ['evidence-and-publication', 'Audit every number/claim in the document against ' + ROOT + '/' + ART + '/*.json (checks that passed), the component labels (x0..x7, Psi_0..Psi_15, zero-based), the reproduction commands (run them), the PDF build (warning-free, registered), and the tests.'],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
TASK (adversarial reviewer, lens ${k}): ${t} Report only real problems with concrete evidence. Do not edit repository files.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log(`stage2 review findings: ${findings.length}`)

phase('Fix')
let fix = null
if (findings.length) {
  fix = await agent(`${COMMON}
TASK (fixer): findings: ${JSON.stringify(findings).slice(0, 60000)}
Re-verify each; fix confirmed ones (rerun verifiers, rebuild/register the PDF, update test pins); reject unconfirmed ones with evidence. Summary: one line per finding FIXED/REJECTED(reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}

phase('Gate')
const gate = await agent(`${COMMON}
TASK (gate): delete ${ROOT}/build/stage2* and the Stage-2 logs, then run powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify_stage2_primordial_field.ps1 and bash scripts/verify_stage2_primordial_field.sh; both must end with stage2_primordial_field_verification=OK. Fix genuine Stage-2 failures minimally and rerun. Report.`, { label: 'gate', phase: 'Gate', schema: RESULT })

return { integ, doc, findings, fix, gate }
