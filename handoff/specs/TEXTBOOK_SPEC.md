# TEXTBOOK SPEC — "dirac16complex: a textbook for students" (binding for every writer)

## 0. The request and the honesty rule

The user (2026-09-30): "create a new teaching 'textbook' (.md, .tex, and .pdf files) for
ignorant students that clearly and correctly describes, in entirety, each and every step in
setting up the formalism, deriving the governing field equations, introducing and deriving
'DFT' type approximations, solving all equations (to the extent possible, given current
knowledge), proving that the 'big bang' creates universes in pairs, this theory solves
matter anti-matter mysteries."

HONESTY RULE (overrides everything): the book teaches what the repository PROVES and
COMPUTES, exactly, with every hypothesis.  Two items of the request are NOT established by
this project and must not be written as established:
* "the big bang creates universes in pairs": what is proved (Stage 5) are exact pairing
  theorems (the chirality map gamma^8, the mirror map across the Z2 brane, the Kohn–Sham
  level pairing) and their corollaries (a gamma^8 pair has zero total energy-momentum and
  charge in any gravitational field; the mirror universe of mass -M has the same Kohn–Sham
  ground and first excited states).  These make pair creation CONSISTENT with every
  conservation law and constraint; they do not compute a creation process, rate or
  amplitude, and no dynamical big bang is derived.  The chapter says exactly this, quotes the
  author's hypothesis (notebook cells 6, 7, 17) and Stage 1's statement (the pairing is "a
  structural property of the equations, not a claim that universes of masses +-M are created
  in pairs"), and marks the remaining step as an open problem.
* "this theory solves matter anti-matter mysteries": the book explains the observed
  matter–antimatter asymmetry from zero (the baryon-to-photon ratio, the Sakharov conditions:
  baryon-number violation, C and CP violation, departure from equilibrium) and states
  precisely what this theory contributes: a {+M, -M} pair with opposite charges and zero total
  charge (T1) is a global symmetry between two universes — the class of "universe/anti-
  universe" ideas (cite the published CPT-symmetric-universe proposal of Boyle, Finn and Turok,
  Phys. Rev. Lett. 121, 251301 (2018), as the known example of the class, without claiming
  anything it does not say).  The theory as built contains no Standard-Model baryons, no
  baryon-number-violating interaction, no CP violation and no departure-from-equilibrium
  computation, so it does NOT solve the matter–antimatter problem; the chapter lists what would
  be needed and labels every scenario as a hypothesis.
Numbers only from the committed reports/outputs (cite the file).  Derivations must be
correct and complete; where the repository proves something by a verifier, the book gives
the derivation in words and formulas AND names the check (file and check name).

## 1. Audience and style

Readers know school algebra and calculus of one variable, nothing else.  Every notion is
introduced before it is used (vector, matrix, index, sum convention, complex number,
derivative in several variables, metric, signature, group, representation, Lagrangian,
Grassmann number, operator, Fock space, density, etc.).  Each chapter: motivation in plain
words; definitions; derivations step by step (no "it can be shown"); worked examples with
small matrices/numbers; a box-free "What we proved / what we assumed" paragraph; exercises
with full answers at the end of the chapter; references to the repository files.  Counting
from 0; x = {x0, ..., x7}; x4 is time; eta = diag(+1,+1,+1,+1,-1,-1,-1,-1).

## 2. Files and build

* Chapter sources: provenance/textbook/chapters/NN-short-name.md (NN = 00..20), each
  starting with "## N. Title" (the book title is added by the assembler); sections
  "### N.M Title"; no deeper heading levels.  Markdown subset of scripts/build_dissertation_tex.py
  (read its header): $...$ and $$...$$ math, tables with equal cell counts, fenced code lines
  <= 89 characters without tabs, figures only as a line ![caption](path.png) with a path relative
  to the repository root (existing PNGs under artifacts/...), Greek letters allowed, links
  [text](url).
* Assembler: scripts/build_textbook.py concatenates the title block, the abstract and the
  chapters in order into provenance/DIRAC16COMPLEX_TEXTBOOK.md (deterministic, LF), checks
  cross-references "Chapter N" / "Section N.M" resolve, and fails on duplicate section numbers.
* PDF: python scripts/build_provenance_pdf.py provenance/DIRAC16COMPLEX_TEXTBOOK.md
  --developer-layout [--register]; warning-free; registered in provenance/pdf-specifications.json;
  pinned in tests/test_d16c_textbook_publication.py.
* Each chapter writer test-builds its chapter alone in scratch (wrap it with a "# " title line)
  with build_provenance_pdf.py in verify mode until warning-free.

## 3. Chapter plan and sources (the writer reads the sources fully)

Part I — Foundations
00 How to read this book; the honesty ledger (a table: statement, status PROVED / COMPUTED /
   ASSUMED / HYPOTHESIS / OPEN, where verified).  Sources: this spec, README.md, HANDOFF.md,
   all provenance documents' summaries.
01 Mathematical toolkit from zero: vectors, matrices, complex numbers, indices and the sum
   convention, derivatives in several variables, metrics and signatures, (4,4), counting from 0.
02 Clifford algebras and spinors from zero: Pauli -> Dirac -> Cl(4,4); the notebook's T16^A
   gammas; C = sigma16; chirality gamma^8; B; Pin(4,4) vs Spin(4,4); the 16-dimensional
   irreducible representation and its two inequivalent 8-dimensional halves (with the proof).
   Sources: provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md Sections 2-4, the algebra reports.
03 Split octonions and the notebook's construction: tau matrices, the Clifford and octonion
   pictures, the intertwiners K_clifford and K_octonion (Stage 1 results, errata E4-E5).
04 Curved space from zero: metric, Christoffel symbols, curvature, Einstein (and
   Einstein–Lovelock) equations, vielbein, spin connection, the vielbein postulate, the
   covariant derivative of spinors, why the notebook's omega contraction is wrong (Stage 1
   Section 5, Result 5.6).
Part II — Field theory
05 Classical field theory from zero: action, Euler–Lagrange equations, symmetries and
   Noether currents, the energy–momentum tensor; Grassmann numbers from zero; why the author's
   Lg[] is trivial for real Grassmann fields (Stage 1).
06 The two fields and their Lagrangians: dirac16complex (second quantized, Grassmann) and
   dirac16complex00 (classical, commuting); the explicit mass terms; reality; the real
   restriction; the coupling to gravity and the spin connection (Stage 1 + Stage 5 A).
07 Field equations, energy–momentum tensor, kinetic and potential energy, pressure, energy
   density and equations of state in an arbitrary gravitational field, for both fields
   (Stage 1 + Stage 5 A).
08 Canonical quantization in 4+4: Hamiltonian form, anticommutators, the Krein space, the good
   sector and the unstable extra-time modes (Stage 1 Sections 10-11).
Part III — The primordial universe
09 The primordial gravitational field of the notebook: the metric, the Einstein–Lovelock
   equations, what the field requires as a source, the notebook errata (det g, the cell-1058
   rule and the q-term), the static warped form and the Z2 brane (Stage 2, Stage 4 Section 1).
10 Solving differential equations on a computer from zero: ODEs, stiffness, BDF/CVODE,
   tolerances, reproducibility, independent checkers (Stage 3 numerics document).
11 The dark-sector experiments EXP-1..EXP-5 and what they show (dark matter: a qualified yes;
   dark energy: no) (Stage 3 documents).
Part IV — Density functional theory
12 Many-body quantum mechanics and DFT from zero: the many-fermion problem, Hartree and
   Hartree–Fock, Hohenberg–Kohn, Kohn–Sham, LDA, Mermin's finite-temperature functional,
   Delta-SCF and the Kohn–Sham gap.
13 The Kohn–Sham approximation for dirac16complex in the primordial field: the reduction to
   2x2 blocks, boundary conditions, the exact local exchange of the contact interaction, the
   fermion-gas thermodynamic pseudo-potential, shooting and self-consistency, the ground and
   first excited states, thermodynamics, the energy–momentum tensor and the Einstein source
   (Stage 4: STAGE4_SPEC incl. sections 8-9, the exact theory reports, the Rust outputs and
   README of studies/dirac16complex_kohn_sham; the cross-check status stated honestly).
14 The Kohn–Sham approximation for dirac16complex00: the statistics sign of exchange and its
   consequences (Stage 5).
Part V — Pairs of universes, matter and antimatter
15 The pairing theorems T1-T3 with complete proofs and the Kohn–Sham demonstration (Stage 5 B).
16 Does the big bang create universes in pairs? Exactly what is proved, what is consistent,
   what is not derived (Section 0 above).
17 Matter and antimatter: the observed asymmetry, the Sakharov conditions, universe/anti-
   universe ideas, what this theory contributes and what it does not (Section 0 above).
18 Open problems and how a student could attack them.
Appendices
19 Reproducing everything: commands (PowerShell and Bash), expected outputs, gates.
20 Glossary and index of verifier checks.

## 4. Process

Wave A (now): chapters 00 (draft ledger), 01-05, 08-13 and the assembler.  Wave B (after the
Stage-5 exact theory and numerics are final): chapters 06, 07, 14-18, the final ledger in 00,
appendices 19-20.  Then assembly, the PDF, four adversarial review lenses (correctness of every
derivation; honesty and overclaim; pedagogy for a beginner; reproducibility of every command
and number), one fixer, registration, tests, push, fresh-clone check.
