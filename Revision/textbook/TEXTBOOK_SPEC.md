# SPEC — "Universes in Pairs": the deep-dive student textbook with Jupyter notebooks (binding)

## 0. The request (verbatim, 2026-10-02) and the rules that override everything

The user: "Preserve your original 'textbook', which is excellent, except that you SHOULD HAVE
included many more plots and graphs.  Create an updated and correct and complete and re-named
teaching 'textbook' (.md, .tex, and .pdf files) for ignorant students that clearly and correctly
describes, in entirety, each and every step in setting up the formalism, deriving the governing
field equations, introducing and deriving 'DFT' type approximations, solving all equations (to the
extent possible, given current knowledge), proving that the 'big bang' creates universes in pairs,
this theory solves matter anti-matter mysteries.  In this version you MUST include a complete
Jupyter notebook for each example, along with complete instructions for executing this Jupyter
notebook that are implemented as comments in the Jupyter notebook as well as instructions in the
updated and re-named teaching 'textbook'.  You must employ a 'deep dive' technique, line by line and
word by word precise and correct.  Your complete instructions MUST NOT refer the student to other
locations in the textbook or other reference files; you MUST give full and complete instructions,
in their entirety, for running the Jupyter notebook in a paragraph just before the text for the
complete Jupyter notebook is presented.  You must also include many more plots and graphs in your
updated and re-named teaching 'textbook'."

R0 PRESERVE: the original textbook `provenance/DIRAC16COMPLEX_TEXTBOOK.{md,tex,pdf}` and its
   chapters `provenance/textbook/chapters/*` are NEVER modified.  It may be READ for pedagogy,
   wording and method.
R1 THE NEW BOOK: `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.{md,tex,pdf}`, title
   "Universes in Pairs — A Deep-Dive Course on the dirac16complex Fields in the Author's 4+4
   Primordial Universe, with a Complete Jupyter Notebook for Every Example".
R2 CORRECT PHYSICS = the Revision record.  The author's coordinates and roles (Revision/SPEC.md
   section 1): x1, x2, x3 = 3-space (inflating, scale factor e^{a4} sin^{1/6} z); x4 = the time;
   x5, x6, x7 = the three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor
   e^{-a4} sin^{1/6} z); x8 = the hidden space direction, z = 6 H x8 in (0, pi/2), g88 = cot^2 z;
   signature (4,4); eta = diag(+,+,+,-,-,-,-,+) in the order x1..x8.  NEVER the old static /
   frozen / window models, never the old numbering x0..x7 (the original textbook used it: when
   you reuse its pedagogy, translate every index).  Every formula and number comes from a
   Revision record (Revision/algebra, theory, field_equations_a4, pairing (incl. kohn_sham/),
   gkd_lovelock, kohn_sham, lead_checks, docs) or is computed by the book's own notebooks; old
   stages (artifacts/, provenance/ results, studies/, wolfram/, notebooks/) are never a source of
   a result.
R3 HONESTY (overrides the wording of the request; the user was told this on 2026-10-02):
   * "the big bang creates universes in pairs": PROVED are the pairing theorems T1 (chirality map
     Gamma: L_{m,lambda}[Gamma Psi] = -L_{-m,-lambda}[Psi], T -> -T, J -> -J), T2 (Gamma with a
     Pin(4,4) reflection and the ASSUMED Z2 mirror: (m,lambda) -> (-m,lambda) at equal T), Q (the
     quantum reading, Krein metric) and T3 (Kohn-Sham level: the +M and -M universes have equal
     energies and energy-momentum tensors), and corollary C1; these are exact MAPS BETWEEN
     SOLUTION SETS.  NOT proved: that any universe is CREATED, in pairs or otherwise; no creation
     process, rate, amplitude or big-bang dynamics follows from these equations.  The chapter is
     titled honestly ("Do universes come in pairs? What the equations prove") and gives the
     complete proofs of what is proved and a precise list of what is not.
   * "this theory solves matter anti-matter mysteries": the book teaches the observed asymmetry
     from zero (baryon-to-photon ratio, Sakharov's three conditions), proves in this theory the
     exact LOCAL U(1) conservation law d_mu(cos z J^mu) = 0 on shell (lead check
     u1_noether_matrix_identity: no process creates or destroys charge at any point, so no net
     charge is made locally inside one universe), states that the TOTAL charge of a universe is
     constant only if no charge flows through the brane z = pi/2 - an ASSUMED no-flux condition,
     not derived, which fails on the exact homogeneous solutions of chapter 18 (OPEN; corrected
     2026-10-08) -, the discrete symmetries, and the pair-level statement (a T1 partner carries the opposite
     charge, so a {+m, -m} pair has zero total charge: the universe/anti-universe class of ideas;
     cite Boyle, Finn and Turok, Phys. Rev. Lett. 121, 251301 (2018) as the published example of
     the class without attributing to it anything it does not say), and states precisely that the
     theory as built does NOT solve the matter-antimatter problem (no baryons, no baryon-number
     violation, no CP violation, no departure-from-equilibrium computation) and what would be
     needed.  Every scenario is labelled HYPOTHESIS.
   * Every statement carries its status: PROVED (exact, with the verifier file and check name),
     COMPUTED (numerical, with the output file and its measured uncertainty), ASSUMED, HYPOTHESIS,
     OPEN.  The Kohn-Sham history a4 = A H x4 is a PRESCRIBED BACKGROUND (the Kohn-Sham states
     violate the a4 source conditions: Revision/field_equations_a4/reports/ks-source-conditions.json).
R4 PRIVATE inputs (the Gmail PDF, prompt files, dirac-main/, vendor/, Generalized_Kronecker_Delta.*)
   are never copied or committed; the Unite numbers may be quoted only as in Revision/README.md.

R5 CHARGE CONJUGATION IS A MATRIX (the user's error report of 2026-10-02): the author's gammas are REAL, so for a
   REAL field plain complex conjugation is the identity and is NOT charge conjugation.  The book derives, step by
   step and with notebooks, the charge-conjugation MATRICES: every matrix M with M (gamma^a)* = s gamma^a M is a
   multiple of 1 (s = +1) or of Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7) (s = -1); hence the two
   charge-conjugation matrices calC_+ = C (the author's sigma16; calC_+^-1 gamma^a calC_+ = -(gamma^a)^T; same
   mass; Psi^c = calC_+ Psibar^T = Psi*) and calC_- = Gamma C (calC_-^-1 gamma^a calC_- = +(gamma^a)^T; mass
   reversed; Psi^c = Gamma Psi*); both Majorana (reality) conditions are consistent; for REAL commuting fields
   J = 0 and calC_+ acts as the identity (a real field is its own conjugate), and the nontrivial REAL matrix map
   is Gamma with (m, lambda) -> (-m, -lambda), which reverses J and the kinetic term (T1); the signs of S and J
   for commuting and Grassmann components (classically and after normal ordering); for the QUANTISED Grassmann
   field the conjugation preserving {Psi, Psi^dagger} = B delta is Psi -> Gamma Psi^{dagger T} (M B^T M^dagger = B
   holds for M = Gamma and fails for M = 1): it reverses the mass.  Source: Revision/lead_checks/
   charge_conjugation_and_u1.py and its report (12 checks); the old analysis provenance/DIRAC16COMPLEX_MATTER_
   ANTIMATTER.md (theorem M2) may be read for method only.  Chapters 05 (the matrices), 07 (the fields, real
   fields), 10 (the quantum statement), 18 (T1 as the mass-reversing matrix conjugation) and 21 (matter and
   antimatter) must present this exactly; NEVER write "complex conjugation is charge conjugation".
R6 PROVENANCE FILE FOR EVERY NOTEBOOK: next to every notebook X.ipynb the file X.PROVENANCE.md, generated by
   nbkit from the FACTS and from the recorded execution, gives: what the notebook computes and from which
   Revision records; COMPLETE, self-contained instructions for the student to execute it (Windows, macOS, Linux;
   the same text as the book's run-instruction paragraph); the EXPECTED OUTPUT (every PASS line, every figure
   file with its caption, the key printed numbers); the SIDE EFFECTS (every file created or overwritten: figures,
   sidecars, data files, the Rust build directories and binaries, caches; network access if any; run time and
   peak memory measured); the environment it was executed with (versions); the sha256 of the executed notebook
   and of every figure; the date of the verified execution and the nbkit --check result.

## 1. Audience, the deep-dive technique, style

Readers know school algebra and one-variable calculus, nothing else.  Every notion is introduced
before it is used.  DEEP DIVE means: (a) every derivation is written out line by line, each line
followed by one sentence saying which rule turned the previous line into this one (no "it can be
shown", no "similarly", no skipped algebra); (b) every technical word is defined at first use, in
plain words, and again in the glossary; (c) every code cell of every notebook is explained line by
line in the book text that follows the notebook ("Line-by-line walk-through": for each code cell,
quote each line or small group of lines and say exactly what it does, why, and what it prints or
draws); (d) every number in the text is traced to the cell that computes it and to the Revision
record it reproduces.  Each chapter ends with "What we proved, what we computed, what we assumed"
and with exercises (at least 5) WITH COMPLETE WORKED ANSWERS.

## 2. Notebooks: one complete notebook for EVERY example

* Every worked example of the book has its own notebook `Revision/textbook/notebooks/NN<letter>_<short>.ipynb`
  (NN = chapter, letter a, b, c ...).  The notebook is BUILT by a deterministic Python builder
  `Revision/textbook/notebooks/src/NN<letter>_<short>.py` that uses the shared kit
  `Revision/textbook/tools/nbkit.py` (cells defined in the builder, executed with nbclient,
  normalised: no timestamps, no timing metadata, fixed kernel name `python3`, LF), so that two
  builds are byte-identical.  The executed notebook (with outputs and embedded figures) is committed.
* Notebook layout (rustSolveIt style, numbered sections): (1) "What this notebook computes";
  (2) "How to run this notebook" — the COMPLETE instructions (below), also repeated as `#` comments
  at the top of the first code cell; (3) "The words used in this notebook"; (4) "The physical and
  mathematical situation"; (5..) the computation in small cells, each preceded by a markdown cell
  saying what the next cell does; every code line commented where it is not obvious; checks as
  `assert` statements with a printed PASS line naming the check and, where it reproduces a Revision
  record, the record file and check name; plots; (last) "What this notebook showed".
* Figures: every notebook draws plots with matplotlib (Agg backend inside the build), saves each
  figure as `Revision/textbook/figures/NN<letter>_<k>_<short>.png` (dpi 150, metadata stripped:
  `savefig(..., metadata={'Software': None})`), and also shows it inline.  The book includes every
  saved figure with a caption that says what is plotted, the axes and units, and what the student
  should see.  TARGET: at least 4 figures per chapter (chapters 0 and 23 excepted), at least 100 in
  the book; prefer plots that teach (scale factors versus time, matrices as heat maps, spectra,
  densities, profiles, convergence curves, error histograms, parameter scans, phase portraits).
* Software for students: Python 3.12 or newer with numpy, sympy, mpmath, matplotlib, jupyterlab,
  nbformat, nbclient, ipykernel (pinned in `Revision/textbook/requirements.txt` to the versions the
  book was built with); Rust (cargo) only for the notebooks that run the Revision Rust programs
  (GKD/Lovelock, Kohn-Sham solver); NO Wolfram, NO scipy.  The notebooks run on Windows 11
  (PowerShell), macOS (zsh) and Linux (bash); paths are built with pathlib; Rust binaries are found
  with and without `.exe`.
* Notebook text limits (the PDF builder): every source line <= 89 characters, no tabs; outputs are
  short (print summaries, not arrays of thousands of numbers); long outputs are written to files.

## 3. The run-instruction paragraph (just before each notebook's text) — COMPLETE, SELF-CONTAINED

Immediately before the text of each notebook the book has a section "How to run Notebook NN<x>"
whose paragraph(s) give, IN FULL and WITHOUT referring to any other place in the book or any other
file: what the notebook needs (Python packages with versions; whether Rust is needed); how to get
the repository (`git clone https://github.com/once-ere/Dirac_claude.git`) and where the notebook is;
how to create and activate a private Python environment and install the packages, with the exact
commands for Windows PowerShell, macOS and Linux; if Rust is needed, how to install it
(https://rustup.rs) and the exact `cargo build --release --manifest-path ...` command; how to start
JupyterLab in the right folder, open the notebook and run all cells (menu Run > Run All Cells), or
run it headless (`jupyter nbconvert --to notebook --execute --inplace <file>`); how long it takes;
what files it writes; what the student must see at the end (the final PASS lines and figures); the
two or three most likely errors and their fixes.  The same instructions are the first markdown
cell's section 2 and the `#` comments at the top of the first code cell.  These paragraphs are
generated from one template by `Revision/textbook/tools/run_instructions.py` with per-notebook
facts (file, packages, Rust crates, run time, outputs, final lines), so they are complete and
identical in wording across the book; a writer may append notebook-specific troubleshooting.

## 4. Files and build

* Chapters: `Revision/textbook/chapters/NN-short-name.md` (NN = 00..23), each starting with
  "## N. Title"; sections "### N.M Title"; no deeper headings.  Markdown subset of
  scripts/build_dissertation_tex.py (read its header): $...$ and $$...$$ math, tables with equal
  cell counts, fenced code lines <= 89 characters without tabs, figures only as a line
  `![caption](Revision/textbook/figures/....png)`, links [text](url).
* A notebook is placed in a chapter by a marker line `<!-- NOTEBOOK NN<x> -->`; the assembler
  replaces it by: the section "How to run Notebook NN<x>" (the generated paragraph), then the
  section "Notebook NN<x>: complete text" (every cell in order: markdown cells as fenced `text`
  blocks, code cells as fenced `python` blocks headed "In [k]:", text outputs as fenced `text`
  blocks headed "Out [k]:", figures as the book's figure lines).  The writer puts the
  "Line-by-line walk-through" section right after the marker.
* Assembler: `Revision/textbook/tools/assemble_textbook.py` builds
  `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md` deterministically (LF): title block, abstract,
  chapters in order with notebooks expanded; it checks: cross-references "Chapter N" / "Section N.M"
  resolve; no duplicate section numbers; every marker resolves to an executed notebook; every
  figure file exists; every notebook is preceded by its run-instruction section; line lengths in
  fenced blocks; it prints counts (chapters, sections, notebooks, figures, pages after the build).
* PDF: `python scripts/build_provenance_pdf.py Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md
  --developer-layout --number-sections-from-zero --wide-page-numbers --specifications
  Revision/pdf-specifications.json [--register]` (--wide-page-numbers, added 2026-10-08, widens the
  contents' page-number box: the book has over 6000 pages and four-digit page numbers otherwise
  overflow it), warning-free, two builds byte-identical; registered as edition
  `universes-in-pairs-textbook`; pinned in `Revision/tests/test_universes_in_pairs_textbook.py`
  (assembler output equals the committed .md; every notebook rebuilds byte-identically — fast ones
  in the default run, all with REVISION_NOTEBOOKS_FULL=1; the PDF is registered).
* Each chapter writer test-builds its chapter alone in scratch (with its notebooks expanded) in
  verify mode until warning-free.

## 5. Chapter plan (Part, chapter, its examples = notebooks, the Revision sources to read fully)

Part I — Getting ready
00 How to use this book; installing the software (full, all three systems); how the notebooks are
   built; the honesty ledger (table: statement, status, where verified).  NB 00a check the
   installation (versions; a first plot).  Sources: this spec, Revision/README.md, Revision/SPEC.md.
01 Mathematics from zero I: numbers, complex numbers, vectors, matrices, index notation, the sum
   convention, determinants, the generalized Kronecker delta.  NB 01a matrices and determinants
   (heat maps); NB 01b complex numbers and rotations (plots); NB 01c the generalized Kronecker
   delta as a determinant (counts, plots).  Sources: Revision/gkd_lovelock (GKD definition).
02 Mathematics from zero II: functions of several variables, partial derivatives, ODEs, numerical
   integration (Euler, RK4), convergence order, the shooting method for eigenvalues.  NB 02a RK4
   convergence (log-log plot); NB 02b shooting for a quantum well (plots of the shooting function
   and eigenfunctions).
03 Spacetime geometry: metric, signature (4,4), the author's metric, scale factors, Christoffel
   symbols, Riemann, Ricci, Einstein tensors.  NB 03a the author's metric (plots of e^{a4},
   e^{-a4}, sin^{1/6} z, cot^2 z, proper volumes); NB 03b its curvature (sympy; plots of the
   components and of the Kretschmann scalar versus z).  Sources: Revision/SPEC.md s.1,
   Revision/gkd_lovelock/results/curvature.json, Revision/lead_checks.
Part II — Spinors and fields
04 Clifford algebra Cl(4,4) and the author's T16: Pauli -> Dirac -> Cl(4,4); the s4/t4 blocks,
   tau, sigma, taubar, T16; the coordinate map.  NB 04a build T16 from the author's formulas and
   verify the Clifford relation (heat maps of the 8 gammas, the anticommutator table).  Sources:
   Revision/algebra (both engines' reports, gammas.json).
05 C, Gamma, B, S^ab; Pin(4,4) irreducible, Spin(4,4) splits into two inequivalent halves; the
   charge-conjugation MATRICES calC_+ = C and calC_- = Gamma C (R5).  NB 05a C, Gamma, B and their
   properties (spectra, heat maps); NB 05b commutant dimensions (rank plots); NB 05c the
   charge-conjugation matrices.  Sources: Revision/algebra, Revision/lead_checks.
06 Spinors in curved 4+4 space: vielbein, spin connection, covariant derivative, gamma^mu Omega_mu
   = 3 H gamma^(x8), the negative control, frame dependence.  NB 06a.  Sources: Revision/theory,
   Revision/lead_checks.
07 The two fields and their Lagrangians: Grassmann numbers from zero; dirac16complex (Grassmann) and
   dirac16complex00 (commuting); reality; Euler-Lagrange equations written out in the author's
   metric; the Majorana-type negative control.  NB 07a a Grassmann algebra by hand; NB 07b the
   Euler-Lagrange equations in the author's metric.  Sources: Revision/theory, docs.
08 Non-triviality, its exact scope, and well-posedness: frame dependence of gamma^mu Omega_mu, the
   rescaling that removes it, the extra-time growth rates (Hadamard ill-posedness).  NB 08a (plots
   of growth rates versus extra-time momentum).  Sources: Revision/theory (scope checks), docs.
09 The energy-momentum tensor: kinetic and potential energy, energy density, the pressures p3, p_t,
   p8, equations of state, the two conservation identities (x4: energy exchange between 3-space and
   the extra times; x8).  NB 09a the EMT and the identities; NB 09b condensates (w versus
   parameters; energy exchange plots).  Sources: Revision/theory, lead_checks, docs.
10 Canonical quantisation in 4+4: the Krein space, the indefinite form, the good sector, Krein
   inertia.  NB 10a one-particle spectra and Krein signatures (plots).  Sources: Revision/theory
   (quantum checks), docs, pairing (Q).
Part III — Gravity's field equations
11 GKD and the Lovelock tensors: the author's kdelta, its proof as a determinant, the three Lovelock
   tensors of (4.38) for the author's metric.  NB 11a GKD in Python and the Rust program (timing,
   counts); NB 11b the Lovelock tensors (run lovelock_gkd; plots of components).  Sources:
   Revision/gkd_lovelock (all of it, incl. PROVENANCE_OF_THE_COMPUTATION.md).
12 The field equations for a4: Einstein and Einstein-Lovelock; constraint, evolution, hidden and
   off-diagonal components; no vacuum for H > 0; the null energy condition along x8; the linear
   member a4 = A H x4 (A -> -A symmetry: deflation is a choice of sign); the source each choice
   requires.  NB 12a the equations (sympy); NB 12b required source versus A, alpha_2, alpha_3
   (plots); NB 12c integrating the a4 evolution equation for given sources (plots of a4(x4) and of
   the scale factors).  Sources: Revision/field_equations_a4, lead_checks.
Part IV — Density functional theory
13 Many-body quantum mechanics and DFT from zero: Hartree, Hartree-Fock, Hohenberg-Kohn, Kohn-Sham,
   LDA, Mermin, Delta-SCF.  NB 13a a one-dimensional Kohn-Sham toy with self-consistency (plots of
   density, potential, convergence); NB 13b exchange of a contact interaction in a uniform gas
   (plots).
14 The Kohn-Sham model of dirac16complex in the deflating primordial field: the hidden coordinate y,
   the warped form, the stationary-slice (adiabatic) ansatz, the removal of the spin connection, the
   2x2 blocks, boundary conditions (Z2 mirror ASSUMED, regular tip), the exact rescaling identity,
   the exact local exchange.  NB 14a block reduction and rescaling identity (checks, plots); NB 14b
   free-field spectra, analytic versus numerical (plots).  Sources: Revision/kohn_sham/theory,
   ks-theory.json, reports.
15 Solving the Kohn-Sham equations: the Rust solver (shooting with a Pruefer count, Anderson mixing,
   Mermin), the ground and first excited states along the deflating history, Delta-SCF, the
   energy-momentum profiles, adiabaticity, thermodynamics.  NB 15a run the canonical matrix (plots:
   levels versus a4,0, densities, gaps); NB 15b energy-momentum profiles and the y-conservation
   check (plots); NB 15c adiabaticity along the history (plots); NB 15d thermodynamics (mu, C_V, F
   versus T, plots).  Sources: Revision/kohn_sham (solver README, results, reports).
16 Checking the solution independently: the Python reference solver, Richardson extrapolation, the
   cross-check with tolerances fixed in advance.  NB 16a run a reference subset and the checker
   (plots: agreement ratios, convergence).  Sources: Revision/kohn_sham/reference, checker, reports.
17 The a4 equations with the Kohn-Sham source: why the Kohn-Sham history is a prescribed
   background (x8 dependence, p3 + p_t != 2 p8).  NB 17a (plots of the violation profiles).
   Sources: Revision/field_equations_a4/reports/ks-source-conditions.json and its checker.
Part V — Pairs of universes, matter and antimatter
18 The pairing theorems T1, T2 and Q with complete proofs.  NB 18a T1 and T2 verified symbolically
   and numerically (plots of mapped spectra and currents).  Sources: Revision/pairing.
19 T3: the Kohn-Sham universes of mass +M and -M.  NB 19a run the Rust solver for +M and -M with
   the transformed boundary conditions and the negative control (overlay plots).  Sources:
   Revision/pairing/kohn_sham, Revision/kohn_sham.
20 Do universes come in pairs? What the equations prove (T1-T3, C1) and what they do not (creation,
   rate, amplitude, big-bang dynamics); the author's hypothesis stated as a hypothesis.  NB 20a
   corollary C1 and the zero-source no-solution result (plots).  Sources: Revision/pairing,
   docs/PAIR_CREATION_PROOFS.md, lead_checks.
21 Matter and antimatter from zero: observations, Sakharov's conditions, the exact local U(1)
   conservation law in this theory (the total charge is constant only under the ASSUMED no-flux
   condition at the brane), the charge-conjugation MATRICES calC_+ and calC_- (R5), real
   fields, the quantum (unitary-type) conjugation Gamma, P/T and chirality, the pair-level zero
   total charge, the scorecard, what would be needed.  NB 21a the charge-conjugation matrices
   solved exactly from the Revision gammas (heat maps of C, Gamma, Gamma C; the solution-space
   dimensions; the bilinear sign table); NB 21b local U(1) charge conservation, the brane flux and the pair-level
   charge bookkeeping (plots); NB 21c the quantised field's conjugation (M B^T M^dagger = B).
   These are NEW Revision computations; they must reproduce Revision/lead_checks/
   charge_conjugation_and_u1.py's report.
22 Open problems: the creation question, TDDFT beyond the adiabatic history, the a4 back-reaction,
   the Z2 brane junction, the dark-sector hypotheses (being investigated; no results claimed), how
   a student could attack each.  NB 22a the adiabaticity breakdown estimate (plots).
Appendices
23 Reproducing everything (all commands, all notebooks, the PDF), glossary, index of checks and of
   notebooks.  NB 23a run every notebook headless and compare (a table and a timing bar chart).

## 6. Process (workflow `Revision/workflows/textbook_universes_in_pairs.js`)

Infra (nbkit, run_instructions, assembler, requirements, a pilot chapter end-to-end through the PDF)
-> per chapter, pipelined: notebooks author -> chapter writer -> adversarial reviewer (re-executes
every notebook from a clean copy, checks physics against the Revision records, the deep-dive
standard, the instructions rule, the figures) -> fixer -> assembly, PDF, registration, tests ->
whole-book review lenses (correctness, honesty, pedagogy/deep dive, instructions and notebook
completeness, reproducibility from a fresh clone, figures) -> two skeptics per finding -> fixers ->
rebuild -> fix verifier.  Commit and push after every milestone.
