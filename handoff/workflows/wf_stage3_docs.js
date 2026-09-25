export const meta = {
  name: 'stage3-notebooks-documents-review',
  description: 'Stage 3: Jupyter + Mathematica notebooks, figures, dark-sector results document, student guide, adversarial review, gate',
  phases: [
    { title: 'Integrate', detail: 'whole-crate fmt/clippy/test, print-config, canonical outputs' },
    { title: 'Notebooks', detail: 'Jupyter (rustSolveIt template), Mathematica cross-check, builder figure support' },
    { title: 'Documents', detail: 'scientific results + student guide' },
    { title: 'Review', detail: 'four adversarial lenses' },
    { title: 'Fix', detail: 'apply confirmed findings' },
    { title: 'Gate', detail: 'clean end-to-end Stage-3 gate' },
  ],
}

const ROOT = 'C:/Users/nsh/Developer/github/Dirac_claude'
const SP = 'C:/Users/nsh/AppData/Local/Temp/claude/C--Users-nsh-Developer-github-Dirac-claude/cc75e05b-1dc1-4a82-a1dd-e65cb8479099/scratchpad'
const NUM = 'artifacts/dirac16complex/numerics'
const engine = '(read the full engine reports from ' + SP + '/stage3_engine_slim.json: core + exp2/exp3/exp4 key results and the contract problems they measured; EXP-1/EXP-5 details are in the core entry)'

const COMMON = `
CONTEXT: repository ${ROOT} (git, main; do NOT commit/push). Binding: ${SP}/CONTRACT.md (read its ERRATA section 11), ${SP}/NUMERICS_CONTRACT.md. The Rust study studies/dirac16complex_cosmology (CVODE from the pinned rustSolveIt engine in vendor/rustSolveIt, fetched by scripts/setup_solver.{ps1,sh}) and its checkers scripts/check_dirac16complex_exp{1..5}.py, scripts/analyze_dirac16complex_exp3.py, with outputs under ${NUM}/exp{1..5}/, are finished. Engine report: ${engine}
Stage-1/2 physics (read for the documents): provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md and provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md if present, the reports under artifacts/dirac16complex/{arbitrary-field,primordial-field}/.
The Gmail PDF (input, NOT to be committed; it is git-ignored): ${ROOT}/Gmail - w = equation of state parameter =w = -0.764 = forcing the Unite supernova data by itself to fit a flat, non-evolving dark energy model.pdf — CPL w(a)=w0+wa(1-a), Unite w0=-0.861 (~-0.86), wa=-0.60, constant-w wCDM fit w=-0.764 (about 2 sigma from -1), phantom past w0+wa=-1.46, quintessence rho=phidot^2/2+V, P=phidot^2/2-V, KG phiddot+3H phidot+V'=0, thawing vs freezing (CAUTION: the PDF's table writes thawing "(wa > 0)" and freezing "(wa < 0)", but with its own formula dw/da = -wa, so a thawing field whose w rises from -1 has wa < 0; state this discrepancy explicitly and use the formula-consistent signs), canonical fields w>=-1, phantom crossing needs non-canonical physics; LCDM table (radiation 1/3, matter 0, DM 0, Lambda -1).
Verified fact to state in the documentation: none of the three rustSolveIt repositories (Win11 a8fdff45, macOS 5360157f, Linux 6f58e02e) contains a Mathematica notebook (.nb/.wl/.wls): verified by listing their full git trees; each has 294 Jupyter notebooks. The Jupyter notebook is adapted from rustSolveIt planet_Mercury/notebook (build_notebook.py md()/code() helpers, find_binary()/run() with the last-line SUCCESS contract, a gauntlet() of asserts, run_notebook.py headless stdlib executor, check_notebook.py auditor) — copy with attribution (BSD-3-Clause per the rustSolveIt Cargo manifests; author once-ere). The Mathematica notebook is new, modelled on dirac-main notebooks/DiracTriality.nb + scripts/build_mathematica_notebook.wls / verify_mathematica_notebook.wls (RunProcess + Import CSV/RawJSON).
Tools: python 3.14 with numpy, matplotlib 3.11, nbformat, nbclient, ipykernel (python -m nbconvert works; the user-site Scripts dir is not on PATH), sympy; NO scipy; wolframscript (Professional); pdflatex (MiKTeX); cargo. Never modify dirac-main, the .nb input, vendor/. Scratch under ${SP}/stage3_doc_tmp/<label>/. Honesty: every number in notebooks and documents must come from the committed outputs/reports; say plainly what is model-dependent, assumed, or not established.
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
    findings: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' },
      problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } },
      required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } },
    verified_ok: { type: 'array', items: { type: 'string' } },
  },
  required: ['findings', 'verified_ok'],
}

phase('Integrate')
const integ = await agent(`${COMMON}
TASK (crate integration engineer; you may edit any file under studies/dirac16complex_cosmology/ and the Stage-3 checkers scripts/check_dirac16complex_exp*.py, scripts/analyze_dirac16complex_exp3.py, scripts/generate_dirac16complex_constants.py): (1) make main.rs print-config chain the config_lines() of every experiment (exp1..exp5); make "all" run every experiment; (2) make the WHOLE crate clean: cargo fmt --check, cargo clippy --all-targets -- -D warnings, cargo test --release (fix lints in any module without changing numerics; if a lint fix could change floating-point results, verify byte-identical outputs before/after); (3) rebuild in release, run every subcommand into ${NUM}/ (canonical) and again into a scratch dir, confirm byte identity; run every checker with its --repeat and --refined options and confirm all pass; (4) write ${NUM}/numerics-summary.json collecting, per experiment, the check counts (Rust self-checks and Python checks), solver stats, and the key physics numbers (copy from each summary.json / fits.json). Report any genuine failure honestly.`, { label: 'integrate', phase: 'Integrate', schema: RESULT })

phase('Notebooks')
const nb = await parallel([
  () => agent(`${COMMON}
YOU OWN: ${ROOT}/notebooks/build_dirac16complex_notebook.py, ${ROOT}/notebooks/run_notebook.py, ${ROOT}/notebooks/check_notebook.py, ${ROOT}/notebooks/dirac16complex_dark_sector.ipynb, ${ROOT}/${NUM}/figures/*.png, ${ROOT}/${NUM}/notebook-report.json.
TASK: build the Jupyter notebook (python3 kernel) adapted from ${ROOT}/vendor/rustSolveIt/planet_Mercury/notebook/ (read build_notebook.py, run_notebook.py, check_notebook.py, mercury_tidal_locking.ipynb). Sections (markdown >= 80 chars before every code cell): 1 what this computes; 2 how to run (setup_solver, cargo build --release, python notebooks/run_notebook.py ...); 3 glossary (every symbol); 4 physics: the dirac16complex field, Lagrangian, field equations, EMT, KE/PE splits, the five experiments' first-order systems exactly as handed to CVODE (state vector layout, RHS); 5 driver cell (find_binary via env DIRAC16_BIN or studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology(.exe); run() streams output, requires last line SUCCESS); 6-10 one section per experiment: run the subcommand, load its CSV/JSON (csv module + numpy), recompute the key physics independently in the cell, plot with matplotlib (Agg backend; savefig to ${NUM}/figures/<exp>_<name>.png with metadata={'Software': None} and fixed dpi, so bytes are deterministic), print the key numbers; required plots at least: EXP-1 rho,p,KE,PE,w vs x4 (frozen) and rho_req; EXP-2 H_i(t), V, rho, p, w, w_eff, constraint residual; EXP-3 w(a) for all x0 with the Unite CPL band/curve and w=-0.764 line, rho_psi(a) with sign change, KE_L/PE_L, distance-modulus difference vs CPL-Unite, fitted (w0,wa) scatter vs Unite point; EXP-4 rho(a) a^4 and a^3 scalings, w(a) from 1/3 to 0, KE_H/PE_H, |beta_k|^2 spectra vs k for each m, produced density; EXP-5 u^dag u growth vs WKB, Krein norm; 11 gauntlet(): asserts on every acceptance criterion (read the checkers' reports); 12 conclusions on dark matter and dark energy with the honest caveats; 13 lessons. Execute headless with your run_notebook.py (stdlib exec, write back only if all cells pass) AND confirm python -m nbconvert --to notebook --execute works on it; audit with check_notebook.py (rules adapted: needles, markdown lead-ins, required headings, executed counts). Write notebook-report.json (cells, code cells, figures list with sha256, gauntlet results).`, { label: 'jupyter', phase: 'Notebooks', schema: RESULT }),
  () => agent(`${COMMON}
YOU OWN: ${ROOT}/scripts/build_dirac16complex_mathematica_notebook.wls, ${ROOT}/scripts/verify_dirac16complex_mathematica_notebook.wls, ${ROOT}/notebooks/Dirac16ComplexDarkSector.nb, ${ROOT}/${NUM}/mathematica-report.json, ${ROOT}/${NUM}/figures/mathematica/*.png.
TASK: a Mathematica notebook generated deterministically by the .wls builder (pattern of dirac-main/scripts/build_mathematica_notebook.wls: Input cells from code strings via ToBoxes, Text/Section cells for explanations, TaggingRules, trailing-whitespace strip, UTF-8 BinaryWrite) and verified headless by the verifier (pattern of dirac-main/scripts/verify_mathematica_notebook.wls: evaluate every Input cell with $Dirac16RepositoryRoot set, fail on messages/$Failed/false checks). Content: (1) locate the repo, load wolfram/Dirac16ComplexAlgebra.wl and wolfram/Dirac16ComplexGeometry.wl; (2) for each experiment derive symbolically from the covariant field equations the reduced first-order system in its background (FRW-(4,4), primordial zeta reduction, Bianchi Einstein equations with the constraint) and check it equals the Rust RHS by comparing with the RHS the Rust binary encodes (evaluate both at several sample states: use the CSV samples and finite differences, or add nothing to Rust and instead compare against five-point derivatives of the CSV solution); (3) re-integrate each experiment independently with NDSolve (WorkingPrecision/AccuracyGoal chosen sensibly; smaller k-grids for EXP-4) and compare with the Rust CSV columns: record max deviations; (4) RunProcess[{binary, "print-config"}] and require last line SUCCESS; (5) plots exported to ${NUM}/figures/mathematica/ ; (6) a final notebookChecks association of booleans. Report the deviations in mathematica-report.json. Runtime target < 30 min.`, { label: 'mathematica', phase: 'Notebooks', schema: RESULT }),
  () => agent(`${COMMON}
YOU OWN: ${ROOT}/scripts/build_dissertation_tex.py (extension only), ${ROOT}/tests/test_publication_tooling.py (extension only).
TASK: extend the Markdown->LaTeX builder, BACKWARD COMPATIBLY (existing documents provenance/*.md must produce byte-identical .tex; verify by rebuilding each committed provenance .md and comparing with its committed .tex), with an image directive: a line of the form ![caption text](relative/path.png) becomes \\begin{figure}[htbp]\\centering\\includegraphics[width=0.92\\linewidth]{path}\\caption{escaped caption}\\end{figure} (add \\usepackage{graphicx} only when the document contains an image, so documents without images keep identical bytes; paths are relative to the repository root and must be passed to pdflatex so it finds them - use \\graphicspath or absolute-free relative paths resolved from the repo root; document how build_provenance_pdf.py must invoke pdflatex, and update scripts/build_provenance_pdf.py minimally if needed (you may edit it)). PNG embedding must remain deterministic (two builds byte-identical). Add unit tests. Run the whole publication test module.`, { label: 'builder-figures', phase: 'Notebooks', schema: RESULT }),
])

phase('Documents')
const docs = await parallel([
  () => agent(`${COMMON}
Notebook phase results: ${JSON.stringify(nb).slice(0, 30000)}
YOU OWN: ${ROOT}/provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md (+ .tex/.pdf via scripts/build_provenance_pdf.py --register), ${ROOT}/tests/test_d16c_numerics_publication.py.
TASK: the precise scientific document of the Stage-3 investigation: "In detail, investigate and determine and discuss (use numerical solutions and graphs) the physical behavior and changing nature of pressure and energy density in this framework; answer: is there any connection to dark matter and/or dark energy?" Include: the framework summary (field, Lagrangian, field equations, EMT, KE/PE, w); for EACH experiment the exact equations solved, initial data, parameters, solver settings and stats, verification results (checker counts, deviations, convergence, determinism, Mathematica cross-check deviations), the graphs (embed the PNG figures with the new image directive), and the physical interpretation; then a synthesis section with explicit, honest answers: (i) dark matter: what behaves like DM (w -> 0, KE_H/PE_H), the time-varying DM EoS (relativistic -> dust), gravitational pair creation yields; (ii) dark energy: which mechanisms give negative pressure / w < -1/3 / phantom crossing (attractive four-fermion interaction: KE_L < 0; frozen density in the primordial field; deflating extra times), and the quantitative comparison with Unite (w0,wa)=(-0.861,-0.60) and w=-0.764, including where the model FAILS (rapid evolution, negative rho_psi beyond the zero, 8D-Einstein bound, G_N variation, sound speed c_s^2 = dp/drho sign, Krein/extra-time instability, homogeneous mean-field only, no perturbations or data likelihood). Tables of the fitted (w0,wa) and constant w per scenario. Limitations and non-claims. Obey the builder's Markdown subset. Build warning-free, register the edition, pin hashes/phrases in the test.`, { label: 'doc-numerics', phase: 'Documents', schema: RESULT }),
  () => agent(`${COMMON}
Notebook phase results: ${JSON.stringify(nb).slice(0, 30000)}
YOU OWN: ${ROOT}/provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md (+ .tex/.pdf via scripts/build_provenance_pdf.py --register), ${ROOT}/tests/test_d16c_student_guide_publication.py.
TASK: precise documentation giving an IGNORANT STUDENT detailed instructions for setting up and solving ALL the numerical solutions, in entirety: (1) what the student will compute and why, in plain language; (2) prerequisites and installation, step by step, for Windows 11 (PowerShell and Git Bash), macOS and Linux: Git, Rust via rustup (exact commands, checking rustc --version), Python 3 and pip packages (numpy, matplotlib, nbformat, nbclient, ipykernel, sympy), Jupyter optional, Wolfram Engine/Mathematica optional (wolframscript), a TeX distribution optional (MiKTeX/TeX Live) for PDFs; (3) getting the code: git clone https://github.com/once-ere/Dirac_claude.git, scripts/setup_solver.{ps1,sh} with the platform argument, what it fetches (the three rustSolveIt repositories and pinned commits), how to check it; (4) building: cargo build --release in studies/dirac16complex_cosmology (the +fma note), running cargo test; (5) the mathematics needed, from zero: spinors as 16-component columns counted from 0, gamma matrices, the covariant derivative, how the field equation reduces to a first-order ODE system u' = f(t,u) for each experiment (derive each one step by step, show the state-vector layout index by index, the RHS formula, initial conditions and why), what CVODE/BDF/Adams, Newton, tolerances mean; (6) running each experiment (exact commands, expected output lines, where files go, how long it takes), reading the CSV columns (a table per experiment), checking with the Python checkers (expected check counts), running the Jupyter notebook (headless and interactive), running the Mathematica notebook (optional), rebuilding the PDFs; (7) how to change parameters and what to expect (exercises with answers, e.g. change x0 and predict w0 from w=x0/(1+x0)); (8) troubleshooting (FMA, cp1252 encodings, PATH for user-site Scripts, locked target dirs, wolframscript not found, pdflatex warnings); (9) glossary. Obey the builder's Markdown subset; build warning-free; register; pin in test. Every command you write must actually be run by you at least once in this session (from a scratch clone or the repo) and must work.`, { label: 'doc-student-guide', phase: 'Documents', schema: RESULT }),
])

phase('Review')
const lenses = [
  ['physics', 'Are the reduced ODE systems exactly the dirac16complex Euler-Lagrange equations (and the 8D Einstein equations) in each background? Re-derive them independently. Are the EMT expectation values, KE/PE splits, pressures, w and the mean-field condensate treated correctly (expectation-value rule u^dag B M u, S propto 1/V, Pauli counting 8+8, normal ordering)? Are physical conclusions about dark matter/dark energy supported, overstated, or wrong?'],
  ['numerics', 'Rerun the binary (cargo build --release; each subcommand into a scratch --output), the checkers with --repeat/--refined, and compare with committed outputs byte-for-byte. Check tolerances, step statistics, convergence evidence, conservation diagnostics, the adequacy of the EXP-4 k-grid and oscillation resolution, the Nelder-Mead fits (re-fit independently), and the Mathematica cross-check deviations.'],
  ['observations', 'Check every statement comparing with Unite/DESI/LCDM against the Gmail PDF content and against standard cosmology (CPL definition, w0,wa values, -0.764 as constant-w SN-only fit, phantom divide, thawing/freezing classification sign conventions: with the PDF formula w(a)=w0+wa(1-a), dw/da = -wa, so "w increases with time" means wa < 0; the PDF table labels thawing "(wa > 0)" and freezing "(wa < 0)", which is the REVERSE of what its own formula implies (standard literature: thawing wa < 0, freezing wa > 0). Verify this by reading the PDF yourself; the documents must state the discrepancy explicitly, use the formula-consistent convention, and never silently adopt the signs printed in the table). Check the distance-modulus fits are computed correctly (units, H0 marginalisation or not, redshift range), and that no observational detection is claimed.'],
  ['student-and-reproducibility', 'Follow the STUDENT GUIDE literally from a fresh clone of the working tree into a scratch dir (git clone ' + ROOT + ' <scratch>; then its steps: setup_solver, build, run, check, notebooks). Report every step that fails, is ambiguous, or assumes knowledge not explained. Check both notebooks execute headless and their checks pass; the PDFs build warning-free and match the registered specs.'],
]
const reviews = await parallel(lenses.map(([k, t]) => () => agent(`${COMMON}
TASK (adversarial reviewer, lens ${k}): ${t} Report only real problems with concrete evidence. Do not edit repository files; scratch only.`, { label: 'review:' + k, phase: 'Review', schema: FINDINGS })))
const findings = reviews.filter(Boolean).flatMap(r => r.findings)
log(`stage3 review findings: ${findings.length}`)

phase('Fix')
let fix = null
if (findings.length) {
  fix = await agent(`${COMMON}
TASK (fixer): findings: ${JSON.stringify(findings).slice(0, 60000)}
Re-verify each; fix confirmed ones (code, outputs regenerated deterministically, notebooks re-executed, figures regenerated, documents updated and PDFs rebuilt/registered, test pins updated); reject unconfirmed ones with evidence. Summary: one line per finding FIXED/REJECTED(reason).`, { label: 'fix', phase: 'Fix', schema: RESULT })
}

phase('Gate')
const gate = await agent(`${COMMON}
TASK (release gate): write scripts/verify_stage3_dark_sector.{ps1,sh} (twins, same pattern as scripts/verify_stage1_arbitrary_field.*: logged steps into build/logs, final line stage3_dark_sector_verification=OK) that: check vendor/rustSolveIt is at the pinned commit (run setup_solver if absent), cargo fmt --check, cargo clippy -D warnings, cargo test --release, cargo build --release, run all experiments into build/stage3/run-a and build/stage3/run-b and compare byte-identical with each other AND with the committed ${NUM}/exp*/ outputs, run every checker (with --repeat and --refined), execute the Jupyter notebook headless and audit it, run the Mathematica verifier (skip with a clear message if wolframscript is absent), rebuild both Stage-3 PDFs and check them against provenance/pdf-specifications.json, and run python -m unittest discover -s tests -v. Then run BOTH gate scripts from a clean build/ and fix genuine failures minimally. Report.`, { label: 'gate', phase: 'Gate', schema: RESULT })

return { integ, nb, docs, findings, fix, gate }
