export const meta = {
  name: 'stage1-integrate-document-review',
  description: 'Stage 1: integrate verifiers, write the arbitrary-field provenance document, adversarially review, fix, final gate',
  phases: [
    { title: 'Integrate', detail: 'run all Stage-1 verifiers together, fix cross-agreement' },
    { title: 'Document', detail: 'DIRAC16COMPLEX_ARBITRARY_FIELD md/tex/pdf' },
    { title: 'Review', detail: 'four independent adversarial lenses' },
    { title: 'Fix', detail: 'apply confirmed findings' },
    { title: 'Gate', detail: 'clean end-to-end Stage-1 gate' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const ART = 'artifacts/dirac16complex/arbitrary-field'
const DOC = 'provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md'
const buildReports = '(read the full Stage-1 build reports from ' + SP + '/stage1_build_slim.json: a JSON list of {label, checks_failed, contract_problems, key_measurements, notes} for wolfram-algebra, wolfram-geometry, python-algebra, python-geometry, tooling)'

const COMMON = `
CONTEXT: repository ${ROOT} (git, branch main; do NOT commit or push; the lead does that). Binding physics/conventions: ${SP}/CONTRACT.md, corrected by any contract problems recorded in the Stage-1 build reports below (measured truth wins over the contract). Never modify ${ROOT}/dirac-main, the notebook .nb, vendor/. Other workflows are concurrently writing Stage-2 files (wolfram/Dirac16ComplexPrimordial.wl, scripts/*primordial*, artifacts/dirac16complex/primordial-field/, tests/test_d16c_primordial.py) and Stage-3 files (studies/, scripts/*exp*, artifacts/dirac16complex/numerics/): never touch those.
Stage-1 files: wolfram/Dirac16ComplexAlgebra.wl, wolfram/Dirac16ComplexGeometry.wl, scripts/verify_dirac16complex_algebra.wls, scripts/verify_dirac16complex_geometry.wls, scripts/d16c_exact.py, scripts/build_dirac16complex_fixture.py, scripts/check_dirac16complex_algebra.py, scripts/d16c_geometry_sympy.py, scripts/check_dirac16complex_geometry.py, scripts/grassmann_algebra.py, scripts/demo_grassmann_lagrangians.py, scripts/build_dissertation_tex.py, scripts/check_dissertation_pdf.py, scripts/check_provenance_pdf.py, scripts/build_provenance_pdf.py, scripts/run_logged.{ps1,sh}, scripts/verify_stage1_arbitrary_field.{ps1,sh}, tests/test_d16c_algebra.py, tests/test_d16c_geometry.py, tests/test_publication_tooling.py, NOTICE, ${ART}/*, ${DOC} (+ .tex/.pdf), provenance/pdf-specifications.json.
Stage-1 build reports (from the builders): ${buildReports}
Tools: wolframscript (Professional license), python 3.14 (stdlib, numpy, sympy, mpmath; NO scipy), pdflatex (MiKTeX, on PATH), Git Bash and PowerShell. Scratch only under ${SP}/stage1_doc_tmp/<label>/.
Notation hazard in the Gmail PDF (verified by the lead): it writes w(a)=w0+wa(1-a), so dw/da = -wa and "w increases with time" means wa < 0, yet its thawing/freezing table labels thawing "(wa > 0)" and freezing "(wa < 0)" - the reverse of what its own formula implies. Any document that mentions thawing/freezing must state this explicitly and use the formula-consistent signs. The PDF also uses signature (+,-,-,-) and L = (1/2) d_mu phi d^mu phi - V, whereas this project uses eta = diag(+,+,+,+,-,-,-,-) with x4 as time; both give rho = phidot^2/2 + V, P = phidot^2/2 - V.
Honesty rules: never claim a check passes unless it was run in this session; quote numbers only from the reports; label conventions as conventions and results as results.
`

const RESULT = {
  type: 'object',
  properties: {
    files_changed: { type: 'array', items: { type: 'string' } },
    commands_run: { type: 'array', items: { type: 'string' } },
    all_checks_pass: { type: 'boolean' },
    failing: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
  },
  required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'summary'],
}
const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['critical', 'major', 'minor'] },
          file: { type: 'string' },
          location: { type: 'string' },
          problem: { type: 'string' },
          evidence: { type: 'string', description: 'computation, command output or quotation proving the problem' },
          fix: { type: 'string' },
        },
        required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'],
      },
    },
    verified_ok: { type: 'array', items: { type: 'string' }, description: 'claims you independently confirmed' },
  },
  required: ['findings', 'verified_ok'],
}

phase('Integrate')
const integ = await agent(`${COMMON}
LEAD DECISIONS (apply first): (1) QNT_unitaryAndKreinSubgroups has ONE canonical meaning in both Wolfram and Python: exactly 13 of the 28 S^ab commute with B (the 9 so(4)+so(3) ones plus the 4 Hermitian boosts S^{b4}, b=0..3); exactly 9 both commute with B and are anti-Hermitian (the unitarily implemented Spin(4)xSpin(3)); the 21 with a,b != 4 are Krein-unitary and the 7 S^{4b} are not. Update the Wolfram verifier's expectation to this (keep the literal "exactly 9 commute" claim recorded as a false measurement, as the Python checker does), rerun, and make ALG_wolframAgreement compare the same semantics. See CONTRACT.md section 11 (errata E1-E5). (2) WolframScript 1.14 drops arguments after "--" when used with -file: every script and gate must pass report/output paths as positional arguments WITHOUT "--" (the Wolfram verifiers already accept positional arguments and DIRAC16_* environment variables); fix scripts/verify_stage1_arbitrary_field.{ps1,sh} accordingly and verify that a non-default output path really is honoured.
TASK (integration engineer; you may edit any Stage-1 file listed above to fix integration bugs, but never weaken a check): from ${ROOT} run, in order, the full Stage-1 chain: python scripts/build_dirac16complex_fixture.py; wolframscript -file scripts/verify_dirac16complex_algebra.wls ${ART}/wolfram-algebra-report.json; wolframscript -file scripts/verify_dirac16complex_geometry.wls ${ART}/wolfram-geometry-report.json; python scripts/check_dirac16complex_algebra.py; python scripts/check_dirac16complex_geometry.py; python scripts/demo_grassmann_lagrangians.py; python -m unittest discover -s tests -p "test_d16c_*.py" -v; python -m unittest discover -s tests -p "test_publication_tooling.py" -v. Ensure the cross-implementation agreement checks run (Python must read the Wolfram reports and vice versa where designed) and pass. Compare the Wolfram and Python values of every shared measurement (K matrices, Lichnerowicz constant, EMT sign convention, dimensions, signatures) and record any disagreement as a failure to be resolved by finding the actual bug (recompute by hand/independently if needed). Then write ${ART}/stage1-summary.json: {schemaVersion, checks: union of all reports with producer prefix, counts per producer, agreed measurements}. Finally run the gate script scripts/verify_stage1_arbitrary_field.ps1 (PowerShell) up to (not including) the PDF step if the document does not exist yet, and report.`, { label: 'integrate', phase: 'Integrate', schema: RESULT })

phase('Document')
const doc = await agent(`${COMMON}
Integration result: ${JSON.stringify(integ).slice(0, 20000)}
TASK (author): write ${ROOT}/${DOC}, the complete provenance document for Stage 1, following ${SP}/DOC_OUTLINE_STAGE1.md exactly (all 14 sections), using ONLY numbers and statements backed by the reports in ${ROOT}/${ART}/ (cite check names). It must contain, explicitly and correctly: the definition of the 16-component complex Grassmann field dirac16complex and its representation theory (Pin(4,4) irreducible 16; Spin(4,4) = two inequivalent 8's); the compatibility of the Clifford and split-octonion pictures (intertwiners); the Christoffel connection, the canonical spin connection from the vielbein postulate (total covariant derivative of the vielbein is zero) and D_mu; expression [1] verbatim in WolframScript; the notebook's Lg[] verbatim in WolframScript and the theorem that it is empty (pure divergence) for a Grassmann field; the new Lagrangian (also written in WolframScript with the notebook's variable names); the covariant Euler-Lagrange equations in an arbitrary gravitational field and their non-triviality (spin connection pure gauge iff flat; Lichnerowicz term with the measured constant times R); the energy-momentum tensor operator (derivation, formula, properties); the kinetic energy, potential energy (both the Lagrangian split and the Hamiltonian split), pressure, energy density and equation of state, with the side-by-side comparison with the scalar-field formulas of the Gmail PDF (the PDF uses signature (+,-,-,-); state the notation map); canonical quantization in 4+4 dimensions (Dirac brackets, equal-x4 anticommutators in curved space, Krein structure with J = B, the good sector, Fock space, Dirac sea, which symmetries are unitary, the ultrahyperbolic caveat, the expectation-value rule <Psi^dag M Psi> = u^dag B M u); verification records; exact PowerShell and Git Bash reproduction commands; limitations. Obey the Markdown subset of scripts/build_dissertation_tex.py (read its header and the tooling agent's notes in the build reports; see also ${SP}/survey_dirac-main-machinery.md pitfalls). Then build: python scripts/build_provenance_pdf.py ${DOC} --register (or the tool's actual flags - read it), until the PDF builds warning-free and byte-identically twice. Also write tests/test_d16c_arbitrary_field_publication.py pinning the md/tex sha256 and required phrases (the phrases must include "dirac16complex", "Grassmann", "Pin(4,4)", "Spin(4,4)", "vielbein postulate", "canonical spin connection", "energy-momentum tensor", "equation of state", "Krein").`, { label: 'document', phase: 'Document', schema: RESULT })

phase('Review')
const lenses = [
  { key: 'physics-derivations', text: 'Re-derive, independently and by hand/CAS (write your own small scripts), the Lagrangian Hermiticity, the Euler-Lagrange equations (including the step using the divergence identity), the energy-momentum tensor from the tetrad variation (sign and symmetrisation, the g_mu_nu L term, on-shell value of L), its conservation and trace, and the homogeneous reductions (rho, p, KE_L, PE_L, KE_H, PE_H, w). Refute anything wrong in the document or the code.' },
  { key: 'representations-compatibility', text: 'Independently verify the representation-theory claims (Pin(4,4) irreducibility of C^16, the inequivalent 8+8 Spin(4,4) split and why "determinant 1 transformations" means Spin(4,4) = preimage of SO(4,4)), the Clifford/split-octonion compatibility (both intertwiners), expression [1], the Grassmann triviality theorem for Lg[], the notebook index-contraction diagnosis (is it really an error, or a convention that the notebook compensates elsewhere? check the notebook text dump ' + SP + '/nbo2.txt cells 499-501, 529-535, 1062-1066), and the Pin-lift character statements.' },
  { key: 'quantization', text: 'Independently verify the canonical quantization section: constraint analysis, Dirac brackets, the equal-time anticommutator in curved space, B and its (8,8) signature, the claim that every Spin-invariant Hermitian form is chirality-even so the charge is indefinite, the J = B Hilbert structure, the good-sector Hermiticity of h_k, the particle/antiparticle counting (8+8 per momentum), which subgroups are unitary vs Krein-unitary, the dispersion relation with extra-time momenta, and the expectation-value rule. Look for physically wrong or overstated claims.' },
  { key: 'evidence-and-publication', text: 'Audit the document against the evidence: every number and every "verified" statement must match a check/measurement in ' + ROOT + '/' + ART + '/*.json that actually passed; notation dictionary correctness against the notebook (' + SP + '/nb_clean.txt, nbo2.txt), dirac-main and the Gmail PDF (' + ROOT + '/Gmail - w = equation of state parameter =w = -0.764 = forcing the Unite supernova data by itself to fit a flat, non-evolving dark energy model.pdf); zero-based counting; reproduction commands actually work (run them); the PDF (open provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf text via python or by reading the .tex) renders all sections, tables and math; no TODO/FIXME; builder warnings; the gate script.' },
]
const reviews = await parallel(lenses.map(l => () => agent(`${COMMON}
Document and code are written. TASK (adversarial reviewer, lens: ${l.key}): ${l.text}
Report only real problems with concrete evidence (a computation, a command output, or an exact quotation). Do not edit repository files (you may write scratch scripts under ${SP}/stage1_doc_tmp/review-${l.key}/).`, { label: 'review:' + l.key, phase: 'Review', schema: FINDINGS })))

const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log(`review findings: ${findings.length} (critical ${findings.filter(f => f.severity === 'critical').length}, major ${findings.filter(f => f.severity === 'major').length})`)

phase('Fix')
let fix = null
if (findings.length) {
  fix = await agent(`${COMMON}
TASK (fixer): the reviewers reported these findings: ${JSON.stringify(findings).slice(0, 60000)}
For EACH finding: first re-verify it independently (it may be wrong); if confirmed, fix the code and/or the document, rerun the affected verifiers, rebuild the PDF with python scripts/build_provenance_pdf.py ${DOC} --register (or the correct flags) and update tests/test_d16c_arbitrary_field_publication.py pins; if not confirmed, explain why with evidence. Return in summary a line per finding: FIXED / REJECTED(reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}

phase('Gate')
const gate = await agent(`${COMMON}
TASK (release gate): from a clean state (delete ${ROOT}/build/ first), run the complete Stage-1 gate: powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify_stage1_arbitrary_field.ps1 and then bash scripts/verify_stage1_arbitrary_field.sh. Both must end with the line stage1_arbitrary_field_verification=OK. Then run python -m unittest discover -s tests -v (all tests; Stage-2/Stage-3 tests written concurrently by other workflows may fail or be absent - report them separately and do NOT fix them). Report every failing Stage-1 item. If a Stage-1 failure is a genuine bug, fix it (smallest change), rerun, and report what you changed.`, { label: 'gate', phase: 'Gate', schema: RESULT })

return { integ, doc, findings, fix, gate }
