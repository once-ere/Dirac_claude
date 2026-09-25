export const meta = {
  name: 'stage2-build-primordial',
  description: 'Stage 2: exact Wolfram and independent sympy derivation of dirac16complex in the notebook primordial (pair-creation) field',
  phases: [{ title: 'Build', detail: 'Wolfram package+verifier and independent sympy checker' }],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const ART = 'artifacts/dirac16complex/primordial-field'

const COMMON = `
CONTEXT:
- Repository root ${ROOT} (git repo on main; do not commit/push). Never modify ${ROOT}/dirac-main, the .nb notebook, vendor/, or files you do not own.
- BINDING: ${SP}/CONTRACT.md and ${SP}/STAGE2_SPEC.md (read both fully). Stage-1 agents are concurrently writing wolfram/Dirac16ComplexAlgebra.wl, wolfram/Dirac16ComplexGeometry.wl and reports under artifacts/dirac16complex/arbitrary-field/; you may READ them (e.g. the Stage-1 EMT sign finding, the Lichnerowicz constant) when they exist, but your code must be self-contained (construct gammas etc. yourself from CONTRACT section 1; copy code from ${SP}/probe1.wls and ${SP}/probe2.wls which already passed) so it does not break while Stage-1 files change. The exact fixture ${ROOT}/artifacts/dirac16complex/arbitrary-field/algebra-fixture.json (committed, 20/20 exact checks) may be used as the source of the gamma matrices, verifying them on load.
- Notebook context: ${SP}/survey_notebook-physics.md (cell numbers, the La[] production Lagrangian cell 1066, spinCoefficients cell 499, omegaMuIJ cell 501, the cell-1137 coupled block equations, q = Q1 Sinh[a4] a4'/E^a4) and the text dumps ${SP}/nbo2.txt (with outputs) / ${SP}/nb_clean.txt; the notebook's own stored Einstein tensor (cell 584) must be compared with yours.
- Efficiency: do NOT FullSimplify big 16x16 matrices with arbitrary functions (a previous attempt ran > 45 min). The metric is diagonal, so use the exact diagonal-vielbein closed forms and verify them; for matrix identities with the arbitrary function a4, substitute exact rational values for a4, a4', a4'', a4''' and exact trig values (sin z = 3/5, cos z = 4/5 and sin z = 5/13, cos z = 12/13; keep s^(1/6) as an exact radical) at >= 2 points, in addition to any cheap symbolic proofs.
- Output: UTF-8, LF, trailing newline; JSON deterministic (Wolfram: ExportString RawJSON then replace CRLF by LF, write bytes; Python: json.dumps(indent=2, ensure_ascii=True)+newline). Verifiers print check_<name>=true|false, measurement_<name>=..., check_count, failed_check_count, exit nonzero on failure. Reports: {schemaVersion, producer, checks, measurements, sourceSha256}.
- Scratch only under ${SP}/stage2_tmp/<label>/. Honesty: unimplemented checks must not appear as true; if STAGE2_SPEC.md or CONTRACT.md is wrong, record the measured truth and explain.
`

const REPORT = {
  type: 'object',
  properties: {
    files_written: { type: 'array', items: { type: 'string' } },
    commands_run: { type: 'array', items: { type: 'string' } },
    checks_passed: { type: 'array', items: { type: 'string' } },
    checks_failed: { type: 'array', items: { type: 'string' } },
    key_results: { type: 'array', items: { type: 'string' } },
    contract_problems: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
  required: ['files_written', 'commands_run', 'checks_passed', 'checks_failed', 'key_results', 'contract_problems', 'notes'],
}

phase('Build')
const tasks = [
  { label: 'wolfram-primordial', prompt: `${COMMON}
YOU OWN: ${ROOT}/wolfram/Dirac16ComplexPrimordial.wl, ${ROOT}/scripts/verify_dirac16complex_primordial.wls, ${ROOT}/${ART}/wolfram-primordial-report.json, ${ROOT}/${ART}/primordial-components.json.
TASK: implement every check of STAGE2_SPEC.md (names P_metric, P_zeta, P_christoffel, P_spinconn, P_Omega, P_gammaConst, P_EL, P_blocks, P_notebookCompare, P_EMT, P_modes, P_einstein, P_quant, P_a4linear; split into sub-checks as needed, e.g. P_EL_componentsMatchOperator). primordial-components.json must contain, for direct use in the LaTeX document: (i) the nonzero Christoffel symbols, (ii) the 24 nonzero omega_{mu ab}, (iii) Omega_mu for each mu as a list of nonzero (row,col,value) entries, (iv) the 16 component Euler-Lagrange equations, each as a list of terms {component index n, derivative index mu or "none", coefficient} AND as a TeX string using \\partial_{\\mu} and \\Psi_{n} with coefficients written with \\tan z, e^{\\pm a_4}, s^{-1/6} etc. (keep every TeX line short: break sums over several lines if long; the document builder cannot handle lines of fenced code > 89 chars, but TeX math is fine), (v) the (x0,x4) block decomposition and its comparison with the notebook's coupling sets, (vi) the homogeneous-sector rho, p_i, KE_L, PE_L, KE_H, PE_H, w closed forms, (vii) G^mu_nu and the required source. For P_notebookCompare: rebuild the notebook's La[] from cell 1066 exactly (its useT16, useDSQRT = Cos[6Hx0], omegaMuIJ from spinCoefficients (cell 499) with its sign convention, (Q1/2)*Sum omegaMuIJ[[A1,B1]] SAB[[A1,B1]], (H*M) sigma16 mass term, commuting f16[k][x0,x4]), derive its EL equations with the notebook's eL[] logic, transform to z = 6 H x0, t = H x4 and the yZ relabelling of cell 1111, and compare term-by-term with the stored cell-1137 blocks (read them from nbo2.txt); then derive the CORRECT equations (Grassmann-correct Lagrangian of CONTRACT section 5, which for these fields gives gamma^mu D_mu Psi = (m + U') Psi with m = -H M) in the same variables and list the differences, identifying the source of the q-term. Run: wolframscript -file scripts/verify_dirac16complex_primordial.wls -- ${ART}/wolfram-primordial-report.json from the repo root, target runtime < 30 min.` },
  { label: 'python-primordial', prompt: `${COMMON}
YOU OWN: ${ROOT}/scripts/check_dirac16complex_primordial.py, ${ROOT}/${ART}/python-primordial-report.json, ${ROOT}/tests/test_d16c_primordial.py.
TASK: an INDEPENDENT sympy/stdlib implementation (do not import Wolfram outputs as truth) of the same STAGE2_SPEC.md checks where feasible: P_metric, P_zeta, P_christoffel (list + count), P_spinconn (24 components + vielbein postulate), P_Omega (slash = 3 H gamma^0 exactly), P_gammaConst (+ notebook contraction failure), P_EL (build the 16 component equations yourself from the covariant operator; if ${ROOT}/${ART}/primordial-components.json exists, add check P_EL_agreesWithWolfram comparing every coefficient exactly after substituting the same exact sample values; if absent, record measurement "wolframAgreement": "not-run"), P_blocks, P_EMT (homogeneous sector closed forms and their x4-independence and a4-independence), P_modes (exact reduction and E^2 = M^2 + K^2), P_einstein (Ricci scalar, G^mu_nu; compare with the notebook's stored cell-584 EinsteinG converted to mixed components), P_quant (B, sqrt|g| = cos z), P_a4linear. tests/test_d16c_primordial.py: a fast subset (< 60 s) in unittest, discoverable by python -m unittest discover -s tests from the repo root (import via "from scripts import X" with fallback "import X"; no __init__.py). Run your checker and tests until they pass or you document a genuine failure.` },
]
const res = await parallel(tasks.map(t => () => agent(t.prompt, { label: t.label, phase: 'Build', schema: REPORT })))
return tasks.map((t, i) => ({ label: t.label, report: res[i] }))
