## 0. How to read this book

This chapter is the map. It says what the book is about, which request it answers, how each statement is labelled so that you always know whether it is proved, computed, assumed, a hypothesis or an open question, which conventions hold on every page, and how you can check any statement yourself. It ends with the honesty ledger: a table of the main statements of the project with their status and the place where each one is verified. The ledger in this edition is a draft; the rows that depend on Stage 5 of the project are marked "to be completed after Stage 5".

### 0.1 What this book is about

Physics describes the world with **fields**. A field is a rule that attaches numbers to every point of space and time: the temperature in a room attaches one number to each point, the wind attaches three (its components along three directions). The field of this book attaches sixteen **complex numbers** to each point (complex numbers are introduced in Chapter 1), and the space it lives on has eight directions instead of the four of everyday space and time. Four of the eight directions behave like space and four behave like time. One of the four time-like directions, called $x_4$, is chosen as the time in which everything evolves; the other three are called the extra times.

The field is called **dirac16complex**. Its sixteen components are not ordinary numbers but anticommuting quantities, called Grassmann numbers (Chapter 5), because it is meant to describe fermions, particles of the kind of electrons and quarks. A second version, **dirac16complex00**, has the same sixteen components but they are ordinary commuting complex numbers; it is the analogue of the wave function that Dirac wrote down in 1928 before quantum field theory existed (Chapter 6).

The project that this book explains started from a Mathematica notebook by Patrick L. Nash, the file `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` in the repository root, which we call **the notebook**. The notebook proposes a gravitational field in eight dimensions in which ordinary 3-space inflates while the three extra times deflate, and it states the hypothesis that at time $x_4=0$ universes of masses $+M$ and $-M$ are created in pairs. The project wrote down the field theory of dirac16complex in any gravitational field, then in the notebook's field, checked every exact statement by computer algebra in two independent programs, found and corrected errors in the notebook, computed numerical solutions, built a density-functional (Kohn–Sham) approximation for many particles, and proved exact theorems about pairs of universes of masses $+M$ and $-M$.

You need school algebra and the calculus of one variable (derivatives and integrals of functions of one variable). Everything else is built from zero in Chapter 1 and the chapters after it.

### 0.2 The request and what can honestly be delivered

The book was written in answer to this request of the author (2026-09-30): "create a new teaching 'textbook' (.md, .tex, and .pdf files) for ignorant students that clearly and correctly describes, in entirety, each and every step in setting up the formalism, deriving the governing field equations, introducing and deriving 'DFT' type approximations, solving all equations (to the extent possible, given current knowledge), proving that the 'big bang' creates universes in pairs, this theory solves matter anti-matter mysteries."

Four parts of the request are delivered in full, or as far as present knowledge allows. The formalism is set up in Chapters 1 to 5 and 8. The governing field equations are derived in Chapters 6 and 7. The density-functional (DFT) approximations are introduced from zero in Chapter 12 and derived for the two fields in Chapters 13 and 14. The equations are solved exactly where that is possible and numerically elsewhere, in Chapters 9 to 11 and 13 to 15, and the places where they are not solved are listed as open problems in Chapter 18.

Two parts of the request are not established by this project, and a textbook that wrote them as established would teach something false. This book therefore follows one rule above every other, the **honesty rule**: it teaches exactly what the repository proves and computes, together with every assumption, and it never writes "proved" for a statement that is not proved.

The first of the two parts is "the big bang creates universes in pairs". The notebook states it as a hypothesis, and its own words make that clear. Cell 6 says: "HYPOTHESIS: If, employing the Einstein eqs (or Einstein-Lovelock eqs), superluminal inflation/deflation exists, then at time x4 = 0 ... a pair of universes with MASSES ± M is created". Cell 7 asks: "Are Universe (s) of masses ± M created in pairs at time x4 = 0 (before the particles of the standard model exist) ?". Cell 17 records the task: "TODO: prove Universe(s) of masses ±M are created in pairs!" (the three cells are quoted from the survey `handoff/surveys/survey_notebook-physics.md`). What the project proves are exact **pairing theorems**: a map of the field (the chirality map $\gamma^8$ of Chapter 2) that turns every solution with mass $+m$ into a solution with mass $-m$, a mirror map across the brane of the primordial field, and the corresponding statement for the Kohn–Sham states. Their consequences are strong but limited. A pair related by $\gamma^8$ carries zero total energy, momentum and charge in any gravitational field, so the creation of such a pair from nothing violates no conservation law and no field equation. But no creation process, no rate and no probability amplitude is derived, and no dynamical big bang is computed. Stage 1 of the project said it in one sentence, which this book repeats: the pairing of the masses $\pm m$ is "a structural property of the equations, not a claim that universes of masses $\pm M$ are created in pairs" (Stage-1 document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md`, Section 1.3, item 6). Chapter 16 states exactly what is proved, what is merely consistent and what is not derived; the missing step is an open problem.

The second part is "this theory solves matter anti-matter mysteries". The observed universe contains matter but almost no antimatter, and explaining this requires, according to the conditions found by Sakharov in 1967, interactions that change the number of baryons, a violation of the symmetries called C and CP, and a period out of thermal equilibrium (Chapter 17 explains all of this from zero). The theory as built contains no baryons of the Standard Model of particle physics, no interaction that changes baryon number, no CP violation and no computation of a departure from equilibrium. It therefore does not solve the matter–antimatter problem. What it does contribute is a precise symmetry between a universe of mass $+M$ and one of mass $-M$ with opposite charges, which places it in the family of "universe and anti-universe" ideas; Chapter 17 describes that family, lists what would be needed to turn such an idea into an explanation, and labels every scenario as a hypothesis.

### 0.3 Five words for the status of a statement

Every statement of this book that matters has one of five labels. They are defined here once, and the ledger of Section 0.9 uses them.

**PROVED** means: the statement follows from its stated definitions and assumptions by a complete derivation, and this book gives that derivation step by step. Where the repository contains an exact machine check (a computation with exact integers, fractions or symbols, done in Wolfram Language and independently in Python), the check is named: the report file and the name of the check inside it. One distinction matters. When a statement is about a finite list of definite objects, for example "these eight matrices of integers satisfy these 64 equations", an exact computation of all cases is itself a complete proof. When a statement is about infinitely many objects, for example "for every gravitational field", the proof is the general derivation; an exact check at a few test points then confirms the derivation (and would have caught many errors), but it is not the proof. The ledger says which of the two applies.

**COMPUTED** means: the statement is a number, a table or a curve produced by a numerical program, with floating-point arithmetic, finite grids and error tolerances. Computed results are reproducible from the repository and are compared with independent programs, but they are not proofs; each carries an accuracy, and the book states it.

**ASSUMED** means: the statement is a starting point that is not derived. There are three kinds: conventions (counting from 0, the sign pattern of the metric, the sign of the energy–momentum tensor), physical inputs (for example, that the gravitational field of the notebook is given and not computed from its source), and approximations (for example, that the sixteen field components can be replaced by average numbers, the mean-field approximation). A proved statement is often proved under assumptions; the ledger names the important ones.

**HYPOTHESIS** means: a physical claim that someone has proposed and that the book states, but that is neither proved nor computed here. The notebook's pair-creation hypothesis is the main example.

**OPEN** means: a question that this project has not answered. Chapter 18 collects the open questions and suggests how a student could attack them.

A small example shows how the labels work. The statement "the matrix $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ satisfies $A^2=I$" is PROVED by multiplying out (Chapter 1 shows how). The statement "in the numerical experiment EXP-4 a gas of dirac16complex quanta ends with the equation-of-state parameter $w=0.0359$" is COMPUTED (the number is the key `thermal.wAtAEnd` of `artifacts/dirac16complex/numerics/exp4/summary.json`, rounded). The statement "we count from 0" is ASSUMED. The statement "the big bang creates universes in pairs" is a HYPOTHESIS. The question "what process creates such a pair, and with what probability?" is OPEN.

### 0.4 The map of the book

The book has five parts and two appendices. Each chapter uses only what earlier chapters have built, with the exceptions named in the chapter itself.

Part I, Foundations.

- Chapter 0 (this chapter): how to read the book, and the honesty ledger.
- Chapter 1: the mathematical toolkit from zero: vectors, matrices, complex numbers, indices and the summation convention, derivatives in several variables, metrics and signatures, the (4,4) world of this book.
- Chapter 2: Clifford algebras and spinors from zero, from the Pauli matrices to the sixteen-dimensional representation of Pin(4,4), its chirality and its two eight-dimensional halves.
- Chapter 3: split octonions and the notebook's construction of the gamma matrices, and how it is related to the other standard construction.
- Chapter 4: curved space from zero: metric, Christoffel symbols, curvature, the Einstein and Einstein–Lovelock equations, the vielbein, the spin connection, and why the notebook's spin-connection contraction is wrong.

Part II, Field theory.

- Chapter 5: classical field theory from zero: action, Euler–Lagrange equations, symmetries and conserved currents, the energy–momentum tensor, Grassmann numbers, and why the notebook's Lagrangian gives no equations for a real Grassmann field.
- Chapter 6: the two fields dirac16complex and dirac16complex00 and their Lagrangians with explicit mass terms and coupling to gravity.
- Chapter 7: field equations, energy–momentum tensor, kinetic and potential energy, pressure, energy density and equations of state in an arbitrary gravitational field.
- Chapter 8: canonical quantization in 4+4 dimensions: the Hamiltonian, anticommutators, the Krein space, the good sector and the unstable extra-time modes.

Part III, The primordial universe.

- Chapter 9: the primordial gravitational field of the notebook, what it requires as a source, the notebook errata, the static warped form and the mirror brane.
- Chapter 10: solving differential equations on a computer from zero.
- Chapter 11: the dark-sector experiments EXP-1 to EXP-5 and what they show.

Part IV, Density functional theory.

- Chapter 12: many-body quantum mechanics and density functional theory from zero: Hartree, Hartree–Fock, Hohenberg–Kohn, Kohn–Sham, the local density approximation, finite temperature, and excited states.
- Chapter 13: the Kohn–Sham approximation for dirac16complex in the primordial field, with its ground and first excited states.
- Chapter 14: the Kohn–Sham approximation for dirac16complex00.

Part V, Pairs of universes, matter and antimatter.

- Chapter 15: the pairing theorems T1 to T3 with complete proofs, and their Kohn–Sham demonstration.
- Chapter 16: does the big bang create universes in pairs? What is proved, what is consistent, what is not derived.
- Chapter 17: matter and antimatter: the observed asymmetry, the Sakharov conditions, universe and anti-universe ideas, and what this theory does and does not contribute.
- Chapter 18: open problems and how a student could attack them.

Appendices.

- Chapter 19: reproducing everything: the commands, the expected outputs and the verification gates.
- Chapter 20: glossary and index of the verifier checks.

If you are in a hurry, read Chapters 0, 1, 2, 5 and 7 for the field theory, Chapters 12 and 13 for the Kohn–Sham approximation, and Chapters 15 to 17 for the questions about pairs of universes and antimatter. If you want to understand every step, read the chapters in order and do the exercises.

### 0.5 The stages of the project

The project was carried out in five stages. Each stage has a document in the folder `provenance/` (a Markdown source, a LaTeX file generated from it, and a PDF) and machine-readable reports under `artifacts/dirac16complex/`. The book is built on these documents and reports, and it quotes numbers only from the reports.

| Stage | Question | Document | State on 2026-09-30 |
| --- | --- | --- | --- |
| 1 | the field in an arbitrary gravitational field | `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md` | complete in content; 153 of 153 exact checks |
| 2 | the field in the primordial field of the notebook | `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md` | complete; 126 of 126 Wolfram and 16 of 16 Python checks |
| 3 | pressure, energy density, dark matter and dark energy from numerical solutions | `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` and `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` | complete |
| 4 | Kohn–Sham ground and first excited states in the primordial field | documents not yet written | exact theory complete (125 of 125 and 157 of 157 checks); the numerical cross-check was being completed |
| 5 | dirac16complex00 and the pairing of universes of masses $+M$ and $-M$ | documents not yet written | in progress |

The check counts are those of the following reports (Stage 1 in the first line, Stage 2 in the next two, Stage 4 in the last two):

```
artifacts/dirac16complex/arbitrary-field/stage1-summary.json
artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
artifacts/dirac16complex/primordial-field/python-primordial-report.json
artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
artifacts/dirac16complex/kohn-sham/python-theory-report.json
```

The state of each stage is recorded in `README.md` and, in more detail, in `HANDOFF.md` section 2.

### 0.6 Conventions used everywhere

These conventions hold on every page of the book. They are choices, not results (status ASSUMED), and they are the conventions of every document of the project.

- **Counting from 0.** Coordinates are $x=(x_0,x_1,\dots,x_7)$, the components of the field are $\Psi_0,\dots,\Psi_{15}$, frame indices run over $0,\dots,7$, and the first entry of every list is entry 0. The exceptions are the numbers of chapters, sections, exercises, results and table rows of this book and of the project documents, the cell numbers of the notebook, and the lists of Mathematica (which start at 1); where such a 1-based number appears, the text says so.
- **The roles of the coordinates.** $x_0$ is a hidden space direction, $x_1,x_2,x_3$ are ordinary 3-space, $x_4$ is the time in which everything evolves, and $x_5,x_6,x_7$ are the three extra times.
- **The flat metric.** $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: the directions 0 to 3 are space-like and the directions 4 to 7 are time-like (Chapter 1 explains what this means). The signature is (4,4).
- **Index letters.** Greek letters $\mu,\nu,\rho,\sigma,\lambda$ run over the coordinates $0,\dots,7$ (curved indices), Latin letters $a,b,c$ over the frame directions $0,\dots,7$, and spinor indices over $0,\dots,15$. In the primordial field, $i$ runs over $1,2,3$ and $j$ over $5,6,7$.
- **Units.** Planck's constant and the speed of light are set to 1 ($\hbar=c=1$). Numerical work sets one more scale to 1 (for example $H=1$ or $m=1$) and says which.
- **Names.** "The notebook" is the author's Mathematica notebook named in Section 0.1. "The Stage-N document" is the document of Stage N listed in Section 0.5. A file is always named by its path relative to the repository root, written in typewriter type, for example `README.md`.

### 0.7 How each chapter is built and how to study it

Every chapter has the same parts. It begins with the motivation in plain words: what problem the chapter solves and why it is needed. Then come the definitions, each introduced before it is used. Then the derivations, step by step, with no step left to "it can be shown"; where a standard mathematical fact is used without proof, the text says so and the "What we proved and what we assumed" section of the chapter lists it. Then worked examples with small matrices and small numbers, which you should redo with pencil and paper. The chapter ends with the "What we proved and what we assumed" section, exercises, and complete answers to the exercises.

References inside the book are written "Chapter 1" or "Section 0.3". References to files of the repository are written in typewriter type. A reference to a section of one of the project documents names the document, as in "Stage-1 document, Section 7.7".

Three pieces of advice. First, do the exercises before you read the answers; mathematics is learned by doing it. Second, when a symbol is unfamiliar, look it up in the glossary of Chapter 20 or in the chapter where it was defined. Third, when a statement surprises you, find it in the ledger of Section 0.9 and check it with the method of Section 0.8.

### 0.8 How to check a statement yourself

You can check a statement at three levels.

The first level is the derivation in the book. Follow it line by line. If a line does not follow from the lines before it, you have found either a gap in your understanding or an error in the book; both are worth finding.

The second level is the report of the machine check. Every exact check writes its result into a JSON file under `artifacts/dirac16complex/`. JSON is a plain-text format for lists and tables that Python reads directly. Each report has an entry `checks`, which maps the name of every check to `true` or `false`. For example, to count the checks of Stage 1, start Python in the repository root (type `python` in PowerShell, in Git Bash, or in the Terminal of macOS or Linux) and type the lines after the prompt `>>>`:

```
>>> import json
>>> path = "artifacts/dirac16complex/arbitrary-field/stage1-summary.json"
>>> checks = json.load(open(path, encoding="utf-8"))["checks"]
>>> sum(checks.values()), len(checks)
(153, 153)
```

The last line is Python's answer: 153 checks are true out of 153. In Python, `True` counts as 1 and `False` as 0 when added, so `sum(checks.values())` is the number of true checks. To look at one named check, for example the check `ALG_gamma8Map` of the chirality map in the Wolfram algebra report:

```
>>> path = "artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json"
>>> json.load(open(path, encoding="utf-8"))["checks"]["ALG_gamma8Map"]
True
```

Type `exit()` to leave Python. Each report also has an entry `measurements` with the numbers that the check measured, and an entry `producer` that names the program that wrote it.

The third level is to run the programs again. Each stage has a gate, a script that reruns every verifier of the stage and compares the results with the committed reports; it ends with a line such as `stage2_primordial_field_verification=OK`. The gates need Python, WolframScript and, for the numerical stages, the Rust toolchain; some run for minutes, some for hours. Chapter 19 lists all commands for PowerShell and for Bash with their expected outputs.

### 0.9 The honesty ledger (draft)

The ledger lists the main statements of the project, each with its status (Section 0.3) and the place where it is verified. A report named without a folder lies in the folder named at the start of its group. "Derivation only" means that the statement is proved by a derivation that is not itself a machine check. Every symbol in the ledger is defined in the chapter named in the last column; on a first reading you may skip the formulas and read only the words and the status. This is a draft: the rows marked "to be completed after Stage 5" receive their final status when Stage 5 is finished, and the rows on Stage 4 are revised when its cross-check and documents are complete.

**Algebra and representations** (reports in `artifacts/dirac16complex/arbitrary-field/`).

| Statement | Status | Where verified |
| --- | --- | --- |
| L1. The eight $16\times16$ integer matrices $\gamma^0,\dots,\gamma^7$ of the notebook satisfy $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$. | PROVED (finite exact computation) | `ALG_clifford` in `wolfram-algebra-report.json` and `python-algebra-report.json`; Chapter 2 |
| L2. $C=\sigma_{16}=\gamma^0\gamma^1\gamma^2\gamma^3$ is symmetric with $C^2=I_{16}$, and every $C\gamma^a$ is antisymmetric (the task's expression [1]). | PROVED (finite exact computation) | `ALG_chargeMatrix`, `ALG_expression1` in both algebra reports; Chapter 2 |
| L3. The chirality $\gamma^8=\gamma^0\gamma^1\cdots\gamma^7=\mathrm{diag}(-I_8,I_8)$ anticommutes with every $\gamma^a$. | PROVED (finite exact computation) | `ALG_chirality` in both algebra reports; Chapter 2 |
| L4. $\mathbb C^{16}$ is irreducible under Pin(4,4); under Spin(4,4) it is the sum of two inequivalent irreducible 8-dimensional parts. | PROVED (exact commutant dimensions 1 and 2, cross-intertwiner dimension 0) | `ALG_pinIrreducibleComplex`, `ALG_spinDecomposition`; Chapter 2 |
| L5. The notebook's split-octonion gammas and the tensor-product (Clifford) gammas describe one module; the intertwiners K_clifford and K_octonion are unique up to a factor. | PROVED; the comparison with the published dirac-main files needs the private folder `dirac-main/` | `ALG_cliffordPictureIntertwiner`, `ALG_octonionPictureIntertwiner`; Chapter 3 |

**Curved space and field theory in an arbitrary gravitational field** (reports in `artifacts/dirac16complex/arbitrary-field/`; G1, G2 and G3 are the exact test geometries of the Stage-1 document).

| Statement | Status | Where verified |
| --- | --- | --- |
| L6. With the canonical spin connection $\omega_{\mu ab}=\eta_{ac}\,\omega_\mu{}^c{}_b$ the curved gamma matrices are covariantly constant. | PROVED in general by derivation; exact checks at test points | `GEO_gammaCovariantConstancy_G1`, `GEO_gammaCovariantConstancy_G2` in `wolfram-geometry-report.json` and `python-geometry-report.json`; Chapter 4 |
| L7. The notebook's contraction of $\omega_\mu{}^a{}_b$ with $S^{ab}$ lacks one metric factor: with it the gammas are not covariantly constant. | PROVED (a counterexample proves a "not") | `GEO_notebookContractionFails_G1`, `GEO_notebookContractionFails_G2`; Chapter 4 |
| L8. For a real anticommuting field the notebook's Lagrangian Lg[] is a total derivative, so its field equations are empty. | PROVED | `LAG_notebookLgGrassmannTrivial_G1`, `LAG_notebookLgGrassmannTrivial_G2`; `GR_notebookLgPureDivergence` in `grassmann-demo-report.json`; Chapter 5 |
| L9. The Euler–Lagrange equation of the dirac16complex Lagrangian is $\gamma^\mu D_\mu\Psi=(m+U'(S))\Psi$ with $S=\bar\Psi\Psi$. | PROVED in general by derivation; exact checks at test points | `LAG_eulerLagrangePsibar_G1`, `LAG_eulerLagrangePsi_G1` (and the G2 checks); `GR_complexQuarticEL`; Chapter 7 |
| L10. The energy–momentum tensor is symmetric, Hermitian and conserved when the field equations hold, with trace $-mS+7SU'-8U$. | PROVED by derivation; conservation checked with exact solutions at points, not as an identity | `EMT_symmetricHermitian_G1`, `EMT_conservation_G1`, `EMT_trace_G1` (and G2); Chapter 7 |
| L11. In homogeneous diagonal backgrounds the energy density is $\rho=mS+U$ and the pressure is $p=SU'-U$ in all seven directions other than $x_4$. | PROVED, with the field products read as average numbers (mean field, ASSUMED) | `EMT_homogeneousReduction_G3`; Chapter 7 |
| L12. Canonical quantization with the time $x_4$ gives a state space with an indefinite inner product (a Krein space), and this is forced by the signature (4,4). | PROVED | `ALG_invariantForms`, `QNT_kreinSignature`; Chapter 8 |
| L13. Modes with momentum along $x_5,x_6,x_7$ grow exponentially when $k_5^2+k_6^2+k_7^2>m^2+k_0^2+\dots+k_3^2$. | PROVED (exact dispersion relation); also COMPUTED in EXP-5 | `QNT_flatModeHamiltonian`; `artifacts/dirac16complex/numerics/exp5/`; Chapters 8 and 11 |
| L14. In the sector without momenta along the extra times the particles have an ordinary positive Fock space. | PROVED (derivation only) | Stage-1 document, Sections 10.6 and 10.7; Chapter 8 |
| L15. An interacting quantum field theory of dirac16complex (interacting states, renormalization). | OPEN | Chapter 18 |
| L16. The chirality map $\Psi\mapsto\gamma^8\Psi$ gives $\mathcal L_{m,\lambda}[\gamma^8\Psi]=-\mathcal L_{-m,-\lambda}[\Psi]$ and turns every solution with $(m,\lambda)$ into one with $(-m,-\lambda)$. | PROVED | `ALG_gamma8Map` in both algebra reports; Chapters 6 and 15 |

**The primordial field of the notebook** (Stage-2 reports in `artifacts/dirac16complex/primordial-field/`, Stage-4 geometry in `artifacts/dirac16complex/kohn-sham/`).

| Statement | Status | Where verified |
| --- | --- | --- |
| L17. For the notebook's metric $\det g=+\cos^2z$, and the spin connection enters the Dirac operator only through $\gamma^\mu\Omega_\mu=3H\gamma^0$, which does not depend on the free function $a_4$. | PROVED (exact symbolic computation) | `P_metric_detG_equals_plus_cos2z`, `P_Omega_gammaSlash3Hgamma0` in `wolfram-primordial-report.json`; Chapter 9 |
| L18. The substitution rule of notebook cell 1058 is wrong: $1/\sqrt{\sin^{1/3}z/e^{2a_4}}$ equals $e^{a_4}/\sin^{1/6}z$, not $1/(e^{a_4}\sin^{1/6}z)$. | PROVED (school algebra; Exercise 1.3 of Chapter 1) | Chapter 1; Chapter 9 |
| L19. The notebook's stored cell-1137 equations agree with the correct equations except for a term $q=Q_1\sinh(a_4)\,a_4'\,e^{-a_4}$. | PROVED (exact reproduction of all 16 stored equations) | `P_notebookCompare_cell1137Reproduced16of16`, `P_notebookCompare_correctVsStoredDifferOnlyByQ`; Chapter 9 |
| L20. The $q$ term was produced by the wrong rule of cell 1058. | HYPOTHESIS (a reconstruction that reproduces the stored output exactly; a literal re-execution of cell 1058 gives no $q$ term) | `P_notebookCompare_reconstructionReproducesStoredEla`; Stage-2 document, Section 11.3; Chapter 9 |
| L21. Eight-dimensional Einstein gravity needs the negative energy density $\rho_{\mathrm{req}}=-3H^2(7+a_4'^2)/\kappa$ to produce this field. | PROVED | `P_einstein_requiredSource`, `P_einstein_rhoRequiredNegative`; Chapter 9 |
| L22. For linear $a_4$ a dirac16complex condensate that does not depend on $x_0$ is an exact source, with negative energy density; for $a_4''\ne0$ no state that depends on $x_0$ and $x_4$ only is a source. | PROVED, with the field products read as numbers (mean field, ASSUMED) | `P_source_x0IndependentSourceConditions`, `P_source_einsteinTransverseDifferenceIs2H2a4pp`; Chapter 9 |
| L23. The static member of the field ($a_4$ constant), written in the warped coordinate $y$: $R=-42H^2$, $\rho_{\mathrm{req}}=-21H^2/\kappa$, $p_{\mathrm{req}}=+15H^2/\kappa$; the mirror brane at $y=0$ carries the stress $S^\mu{}_\mu=-10H/\kappa$ (no sum) for $\mu=1,2,3,5,6,7$ and $S^4{}_4=-12H/\kappa$. | PROVED | `KS_geometry_ricciScalarMinus42H2`, `KS_geometry_requiredSource`, `KS_geometry_israelStress` in `wolfram-kohn-sham-report.json`; Chapter 9 |
| L24. The continuation of the field across $y=0$ as a mirror copy (the $Z_2$ extension, the notebook's "pair of universes" picture). | ASSUMED (a construction chosen to model the hypothesis) | Chapter 9 |
| L25. The primordial field solves Einstein–Lovelock gravity with a physically acceptable source; what determines $a_4$. | OPEN (the Lovelock terms are not computed) | Chapter 18 |

**Numerical experiments of Stage 3** (outputs in `artifacts/dirac16complex/numerics/`).

| Statement | Status | Where verified |
| --- | --- | --- |
| L26. A thermal gas of dirac16complex quanta has $w=0.3329$ at $T=10m$ and $w=0.0359$ after the scale factor of 3-space has grown a hundredfold. | COMPUTED | `exp4/summary.json`, keys `thermal.wAtA1` and `thermal.wAtAEnd`; Chapter 11 |
| L27. Dark matter: the gas has the equation of state of dark matter and is created by the expansion for $m>0$, but no dark-matter model is established (abundance, darkness and the stabilization of the extra dimensions are not computed). | COMPUTED (the behaviour); OPEN (a model) | `exp4/summary.json`, `exp4/python-check-report.json`; Chapter 11 |
| L28. Dark energy: tuned to $w_0=-0.861$ today, the condensate has $w_a=-4.81$; within everything computed the framework gives no viable dark energy. | COMPUTED | `exp3/fits.json`, key `scan.tangentWaAtUniteW0`; Chapter 11 |
| L29. The five experiments pass 69 self-checks of the Rust program, 167 checks of five independent Python checkers, 71 assertions of the Jupyter notebook and 49 checks of the Mathematica notebook. | COMPUTED | the `summary.json` and `python-check-report.json` of `exp1` to `exp5`, `notebook-report.json`, `mathematica-report.json`; Chapter 11 |

**Kohn–Sham approximation, Stage 4** (reports in `artifacts/dirac16complex/kohn-sham/`: `wolfram-kohn-sham-report.json` with 125 of 125 checks and `python-theory-report.json` with 157 of 157).

| Statement | Status | Where verified |
| --- | --- | --- |
| L30. In the static primordial field the Kohn–Sham equation reduces exactly to eight $2\times2$ first-order systems; four of the blocks carry the negated spectrum of the other four. | PROVED | `KS_reduction_blockODEMatrix`, `KS_reduction_hMinusEqualsMinusHPlus`; Chapter 13 |
| L31. The exchange energy of the contact interaction is exactly local: $e_x=-(\lambda/32)(n^2+S^2)$ at every temperature. | PROVED | `KS_exchange_uniformGasClosedForm`, `KS_exchange_angularAverageOfPdotQVanishes`; Chapter 13 |
| L32. The Kohn–Sham model: a static mean field of finitely many quanta in the fixed field, with exact exchange, no correlation term and no back-reaction on the metric. | ASSUMED (an approximation) | `README.md`, "Scientific boundary"; Chapters 12 and 13 |
| L33. Kohn–Sham spectra, densities, ground and first excited states, gaps, thermodynamics and energy–momentum tensor. | COMPUTED by the Rust solver | `artifacts/dirac16complex/kohn-sham/rust/`; Chapter 13 |
| L34. Agreement of the Rust solver with the independent Python reference solver. | OPEN in this draft: 65 of 69 cross-checks agreed in the last recorded run; the four disagreements were diagnosed and reruns were in progress | `handoff/reviews/stage4_crosscheck_quick_2026-09-30.log`; `HANDOFF.md` section 2 |
| L35. Whether a Kohn–Sham state can supply the source that the static field requires, $mS=-36H^2/\kappa$ and $\lambda S^2=30H^2/\kappa$. | OPEN in this draft (to be answered from the Stage-4 results) | `handoff/specs/STAGE4_SPEC.md`, erratum E4.1; Chapter 13 |

**Pairs of universes, matter and antimatter** (Stage 5 and beyond).

| Statement | Status | Where verified |
| --- | --- | --- |
| L36. dirac16complex00 has a non-trivial Lagrangian with an explicit mass term and a non-trivial coupling to the spin connection; its field equations, energy–momentum tensor and equations of state. | to be completed after Stage 5 | Chapters 6 and 7 |
| L37. Theorem T1: a pair $\Psi$ with $(m,\lambda)$ and $\gamma^8\Psi$ with $(-m,-\lambda)$ has zero total energy–momentum and zero total charge in any gravitational field. | to be completed after Stage 5 (the map itself is L16) | Chapter 15 |
| L38. Theorem T2: the mirror map $(m,\lambda)\mapsto(-m,\lambda)$ across the brane. | to be completed after Stage 5 | Chapter 15 |
| L39. Theorem T3: the Kohn–Sham ground and first excited states of the universes of masses $+M$ and $-M$ are images of each other. | to be completed after Stage 5 | Chapter 15 |
| L40. The Kohn–Sham approximation for dirac16complex00, whose exchange term has the opposite sign, $e_x^{00}=+(\lambda/32)(n^2+S^2)$. | to be completed after Stage 5 | Chapter 14 |
| L41. "The big bang creates universes of masses $\pm M$ in pairs" (notebook cells 6, 7 and 17). | HYPOTHESIS; the pairing theorems can at most show that such a creation is consistent with the conservation laws; a creation process, rate or amplitude is OPEN (to be completed after Stage 5) | `handoff/surveys/survey_notebook-physics.md`; Chapter 16 |
| L42. "This theory explains why the universe contains more matter than antimatter." | not established: the theory as built has no Standard-Model baryons, no baryon-number violation, no CP violation and no out-of-equilibrium computation; every scenario is a HYPOTHESIS and the problem is OPEN | Chapter 17 |
| L43. Signature (4,4) as a description of the observed world, which has one time. | ASSUMED as the setting of the model; the relation to observed spacetime is OPEN | `README.md`, "Scientific boundary"; Chapter 18 |

### 0.10 What we proved and what we assumed

This chapter proves nothing new; it organizes. It fixes the conventions of the book (counting from 0, the roles of the coordinates, the metric $\eta=\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$, units with $\hbar=c=1$), all of which are ASSUMED choices. It defines the five status words and applies them in the ledger. The status of every ledger row is taken from the committed reports and project documents named in its last column; the rows on Stages 4 and 5 describe the state of 2026-09-30 and will be revised when those stages are finished. The two items of the request that the project has not established, pair creation of universes by the big bang and the explanation of the matter–antimatter asymmetry, are recorded as a HYPOTHESIS and as not established, and Chapters 16 and 17 treat them in full.

### 0.11 Exercises

Exercise 0.1. Give each statement one of the five status words and one sentence of reason. (a) The matrix $\gamma^4$ of the notebook satisfies $(\gamma^4)^2=-I_{16}$. (b) In EXP-3 the condensate tuned to $w_0=-0.861$ has $w_a=-4.81$. (c) The field lives on an eight-dimensional space of signature (4,4). (d) At $x_4=0$ a pair of universes of masses $+M$ and $-M$ is created. (e) Which physical law fixes the function $a_4$ of the primordial field?

Exercise 0.2. The covariant constancy of the gamma matrices (ledger row L6) was checked exactly at a few test points. (a) Why do these checks alone not prove it for every gravitational field, and what does prove it? (b) The failure of the notebook's contraction (row L7) was also found only at test points. Why is row L7 nevertheless completely proved?

Exercise 0.3. With the method of Section 0.8, count the true checks of the two Stage-2 reports

```
artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
artifacts/dirac16complex/primordial-field/python-primordial-report.json
```

and compare with the table of Section 0.5.

Exercise 0.4. Counting from 0. (a) What is the entry $\eta_{44}$ of the metric $\eta$, and what is $\eta_{33}$? (b) Which coordinate is the fifth entry of the list $(x_0,x_1,\dots,x_7)$, and what is its role? (c) Mathematica counts from 1, so the notebook's matrix entry SAB[[a,b]] with $a,b=1,\dots,8$ is the book's $S^{a-1\,b-1}$. Which $S^{ab}$ is SAB[[3,5]]? (d) How many components does the field have, and what is the label of the last one?

Exercise 0.5. Row L41 of the ledger is a HYPOTHESIS. (a) Explain why a theorem that maps every solution with mass $+m$ to a solution with mass $-m$, and shows that the pair has zero total energy, momentum and charge, cannot by itself turn L41 into a PROVED statement. (b) Name one kind of calculation that would be needed in addition.

Exercise 0.6. The Stage-4 row of the table in Section 0.5 contains results of two different kinds. Name them and give the status of each.

### 0.12 Answers to the exercises

Answer 0.1. (a) PROVED: it is one of the 64 equations $\{\gamma^a,\gamma^b\}=2\eta^{ab}I_{16}$ of row L1 (take $a=b=4$: $2(\gamma^4)^2=2\eta^{44}I_{16}=-2I_{16}$), and a finite computation with integers is a complete proof. (b) COMPUTED: it is the result of a numerical solution (row L28), reproducible but not a proof, and it holds within the accuracy of the solver. (c) ASSUMED: it is the setting of the model, chosen by the notebook, not derived (row L43). (d) HYPOTHESIS: it is the notebook's proposal (row L41); nothing in the project derives it. (e) OPEN: no computation of the project determines $a_4$ (row L25).

Answer 0.2. (a) Row L6 is a statement about every metric, that is about infinitely many cases; checks at finitely many points can only confirm it, since an error could show up at a point that was not tested. It is proved by the general derivation of Chapter 4, which uses only the definitions of the spin connection and of the covariant derivative. The checks confirm that derivation exactly and would have detected many kinds of error. (b) Row L7 says that the notebook's contraction does NOT make the gammas covariantly constant in general. To disprove "for every metric, X holds" one example of a metric in which X fails is enough, and the exact checks exhibit such examples (in G1 all 64 pairs of indices fail). A single counterexample is a complete proof of a "not".

Answer 0.3. Following Section 0.8 with the two paths gives `(126, 126)` for the Wolfram report and `(16, 16)` for the Python report: all 126 and all 16 checks are true, as the table of Section 0.5 says.

Answer 0.4. (a) The diagonal of $\eta$ is $(+1,+1,+1,+1,-1,-1,-1,-1)$ with the entries numbered $0,1,\dots,7$. Entry 4 is the fifth one, $-1$, so $\eta_{44}=-1$; entry 3 is the fourth one, $+1$, so $\eta_{33}=+1$. (b) The fifth entry is $x_4$, the time in which everything evolves. (c) SAB[[3,5]] is $S^{3-1\,5-1}=S^{24}$. (d) Sixteen components, $\Psi_0,\dots,\Psi_{15}$; the last one is $\Psi_{15}$.

Answer 0.5. (a) Such a theorem says: if a universe of mass $+M$ exists as a solution, then a partner of mass $-M$ exists as a solution, and the two together carry nothing that a conservation law would forbid to appear from an empty state. That is a statement about which configurations are allowed, not about which configurations occur, when, or how often. The same situation exists in ordinary physics: conservation of charge and energy allows a photon of enough energy to turn into an electron and a positron, but whether it happens, and with which probability, is computed from the dynamics (quantum electrodynamics), not from the conservation laws. (b) One needs a dynamical calculation: for example a quantum amplitude, or a probability per unit time, for the transition from a state without universes to a state with the pair, or a classical solution of the coupled field and gravity equations that evolves from an initial singular state into the pair. Neither is derived in this project (Chapter 16 and Chapter 18).

Answer 0.6. The exact theory of Stage 4 (the reduction of the Kohn–Sham equation to $2\times2$ blocks, the exchange formula and the other exact statements, 125 of 125 Wolfram and 157 of 157 Python checks) is PROVED (rows L30 and L31). The numerical Kohn–Sham results are COMPUTED (row L33), and their agreement with the independent reference solver was OPEN at the time of this draft (row L34).
