# Revision — a new, separate record for the author's primordial gravitational field

This folder holds a COMPLETELY NEW record of the calculations the author requested on 2026-10-01 for the
primordial gravitational field given below. Nothing in it is copied from, or mixed with, the earlier
stages of the repository (`artifacts/`, `provenance/`, `studies/`, ...): every result here is computed
anew by code in this folder. The binding plan is [`SPEC.md`](SPEC.md).

## The author's task (verbatim, 2026-10-01)

> USE the metric tensor
> {{exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},{0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},{0,0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},{0,0,0,-1,0,0,0,0},{0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},{0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},{0,0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},{0,0,0,0,0,0,0,Cot[6 H x8]^2}}
> for the primordial Gravitational Field.
>
> Work in a (new) folder named 'Revision', and write completely new record of these new calculations.
> You must NOT mix old with new, or otherwise adulterate our new findings.
>
> Read, clearly understand and remember "Gmail - w = equation of state parameter =w = -0.764 = forcing
> the Unite supernova data by itself to fit a flat, non-evolving dark energy model.pdf". [...]
>
> YOU MUST remember that dirac16complex is a 16-component fermi spinor field whose components are complex
> valued, anti-commuting, objects, that transform under a 16-dimensional irreducible representation
> (irrep) of Pin(4,4); and for the determinant 1 transformations, transform under a direct sum of two
> inequivalent 8x8 irreps of Spin(4,4); Pin(4,4) is the double cover of the orthogonal groups O(4,4)
> (Spin(4,4) is the double cover of the orthogonal groups SO(4,4)). Quantize dirac16complex using
> canonical quantization, extended to 4+4 dimensions.
>
> YOU MUST remember that dirac16complex00 is a set of 16 scalar fields that transform as a Pin(4,4) spinor.
>
> Write out and record (also provide .md, .tex, and .pdf provenance files) for the Lagrangian for
> dirac16complex and the Lagrangian for dirac16complex00, the energy-momentum tensor operator for each of
> dirac16complex and dirac16complex00, the kinetic energy, potential energy, pressure and energy density
> and equations of state for the covariant field equations (i.e., the Euler-Lagrange equations for
> dirac16complex and the Euler-Lagrange equations for dirac16complex00) for the case of interaction with
> the above primordial Gravitational Field. For each case, calculate and record (with provenance) the
> field equations for a4[x4].
>
> For the case of dirac16complex interacting with this new primordial Gravitational Field, above, plan and
> employ a DFT-motivated approximation similar to the one that you already created (recall and remember,
> if you forgot), with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT
> ground and first-excited-state computation, and
>
> Couple both dirac16complex and dirac16complex00 to the above primordial Gravitational Field using the
> canonical spin connection and the appropriate Lagrangian; i assume you know how to do this correctly.
> Correct me if i am wrong. Test and verify our two Lagrangians:
> [1]- the Lagrangian for dirac16complex must be non-trivial (i.e., the Euler-Lagrange equations for
> dirac16complex always possess non-zero contributions from gravity (through the canonical
> spin-connection, unless we are in flat 4+4 spacetime), must be self consistent, must be checked and
> verified).
> [2]- the Lagrangian for dirac16complex00 must be non-trivial (the same requirements).
>
> Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy
> equation of state and/or a possible physical mechanism for a time-varying dark matter equation of
> state, both of which you will investigate.
> Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.
>
> [Documents: md, tex and pdf provenance files with the exact, correct field equations, the
> energy-momentum tensor operator, the kinetic energy, potential energy, pressure, energy density and
> equations of state, for the fermion dirac16complex field and for the 'semi-classical' dirac16complex00
> field, in the presence of the above primordial Gravitational Field.]
>
> PROVE that Universes of masses {+mass, -mass} are created in pairs for each case of the dirac16complex
> and the dirac16complex00 fields. Create new provenance markdown file, latex, and pdf files, that contain
> the exact, correct, proof results for both [fields].
>
> push 'Revision' and any other new files (not listed in .gitignore) to
> https://github.com/once-ere/Dirac_claude.git. Check and verify this repo. DO NOT TAKE SHORTCUTS. [...]

(Bracketed passages abridge repeated sentences of the original message; nothing was changed in meaning.)

## Answers given to the author before the work started (2026-10-01)

* The private PDF was read and understood (CPL w(a) = w0 + wa (1 - a); Unite constant-w fit w = -0.764;
  (w0, wa) = (-0.861, -0.60); quintessence formulas). One inconsistency in it is handled explicitly: its
  thawing/freezing table gives the signs of wa opposite to its own formula (thawing means wa < 0 in this
  convention). Its notation H (Hubble rate) and a (scale factor) differ from the metric's H and a4.
* Coupling through the canonical spin connection is correct for both fields (both are Pin(4,4)
  spinors). The non-trivial Lagrangian is the Dirac-type one with Psibar = Psi^dagger C; the notebook's
  real Majorana-type Lg[] is a total derivative for anticommuting fields. In this metric, in the diagonal
  vielbein, the time-direction spin-connection terms of the 3 inflating and 3 deflating directions cancel
  exactly, while a hidden-direction term 3 H gamma^(x8) survives. Non-triviality [1], [2] holds in the
  qualified sense stated in the correction below (this sentence was written as a plan before the work and
  has been corrected after it).
* Canonical quantisation in 4 + 4: when Psi^dagger is realised as the Hilbert adjoint, the canonical
  anticommutator forces an indefinite (Krein) inner product; in the good sector (no extra-time momentum) a
  positive Fock realisation with Psi^dagger = chi B exists. Both are stated.
* "PROVE that Universes ... are created in pairs": the pairing theorems T1, T2 (both fields), the quantum
  reading Q (dirac16complex) and the Kohn-Sham-level theorem T3 (dirac16complex) are proved, each under its
  stated hypotheses (T2 and T3 with the ASSUMED Z2 brane; verified after the work, see
  `docs/PAIR_CREATION_PROOFS`); that universes occur in pairs, or are created, is not proved: no creation
  process, rate or amplitude follows from these equations, and the documents say so.

**Correction for the author (2026-10-01, after the review; you asked to be corrected where you are wrong).**
Non-triviality [1] and [2] are true only in a qualified sense. In this metric the canonical spin connection
drops out of the Lagrangian, so the Euler-Lagrange equations are those of the connection-free symmetric
Lagrangian; the surviving term 3 H gamma^(x8) is its half-density (volume and vielbein divergence) term. Its
value belongs to the diagonal vielbein: in a frame boosted in the (x4, x8) plane with rapidity 6 H x4 the term
gamma^mu Omega_mu vanishes identically, and the rescaling Psi = sin^(-1/2)(z) chi removes it (completely for
U = 0). The deflation a4 contributes nothing to gamma^mu Omega_mu; it enters through the vielbein factors
e^(-+a4). What is frame-independent: Omega_mu vanishes in no frame (its curvature is the Riemann tensor,
R^x8_x8 = -6 H^2), the vielbein factors enter every derivative term, and the metric is curved for every
H > 0; the spin connection also enters the energy-momentum tensor. The exact checks are in
`theory/reports/wolfram-scope.json` and `theory/reports/python-scope.json`.

## Folders

State on 2026-10-08 (waves 1 and 2; every count is that of the report named):

| folder | content | state |
| --- | --- | --- |
| `gkd_lovelock/` | GKD (pure-Rust generalized Kronecker delta) and the three Lovelock tensors of this metric | computed (commit 3e81eeb), 19/19 Rust checks; verified in `verification/`: sympy 49/49, Wolfram 29/29 |
| `algebra/` | the author's gammas, C, Gamma, B, Pin(4,4) and Spin(4,4) facts | Wolfram 45/45, sympy 35/35 |
| `theory/` | Lagrangians, field equations, non-triviality, EMT, quantisation (Wolfram + sympy); scope checks (frame dependence, boundary terms, growth, sign of the energy) | Wolfram 84/84, sympy 70/70 (comparison with Wolfram: agree); scope Wolfram 15/15, sympy 14/14 |
| `field_equations_a4/` | the Einstein-Lovelock equations for a4[x4] with each field as source; the Kohn-Sham states as a source; `ks_source/`: the a4 equations with the Kohn-Sham source (exact identities, hidden-direction moments, the integration of a stated truncated system) | Wolfram 52/52, sympy 63/63; Kohn-Sham source conditions 5/5 (the recorded Kohn-Sham states are not admissible sources); `ks_source/` 23/23 (no recorded Kohn-Sham state is an admissible source, so nothing about a4 is derived from the coupled problem; in the stated approximation the source does not start or select the deflation of the extra times) |
| `kohn_sham/` | Kohn-Sham fermion gas in the deflating field (instantaneous states along the prescribed history a4 = A H x4): theory, Rust solver, independent reference, cross-check | theory Wolfram 46/46, sympy 58/58; Rust solver 42/42, determinism 14/14, Mermin roots 5/5; reference 37/37; full cross-check of the canonical matrix (Rust solver against the reference) 31/31 (2026-10-08); document `docs/KOHN_SHAM_DEFLATING_FIELD` |
| `dark_sector/` | the two hypotheses against the Unite values: `dirac16complex/` (Hypothesis) and `dirac16complex00/` (Hypothesis00) | `dirac16complex/`: derivation 30/30, Kohn-Sham history 5/5, equation of state 13/13, independent implementation 9/9; `dirac16complex00/`: derivation and models 49/49, independent numerics 28/28. Neither Hypothesis nor Hypothesis00 is established (what each field can and cannot produce under the stated observer assumption: document `docs/DARK_SECTOR_HYPOTHESES`) |
| `pairing/` | the pairing theorems T1, T2, Q for both fields; `pairing/kohn_sham/`: T3 and its completion (2026-10-08: the Kohn-Sham potentials read from the Kohn-Sham record, the filling convention carried onto the -m member, the 16-component statement S6) with two numerical demonstrations | Wolfram 101/101, sympy 66/66; T3 Wolfram 10/10, sympy 13/13; completion Wolfram 3/3, sympy 7/7; demonstrations (not proofs) Rust solver 7/7 (210 states), reference solver 7/7 (18 states) |
| `notebooks/` | executed Jupyter notebooks of the Revision record, each with its provenance file and listed in `notebooks/README.md`, and the build, check and audit tool `tools/build_notebooks.py`; the first notebook is `lovelock_gkd.ipynb` (the Lovelock tensors with the GKD) | each notebook re-checks its outputs against the committed records; test `tests/test_revision_notebooks.py` |
| `docs/` | md + tex + pdf documents, all six of SPEC section 10 | built and registered in `pdf-specifications.json`, each with its publication test `tests/test_*_publication.py`: DIRAC16COMPLEX_FIELD_THEORY (32 pages), DIRAC16COMPLEX00_FIELD_THEORY (37 pages) and PAIR_CREATION_PROOFS (32 pages), all three updated on 2026-10-08 with the results of wave 2; KOHN_SHAM_DEFLATING_FIELD (22 pages), DARK_SECTOR_HYPOTHESES (23 pages); LOVELOCK_GKD (20 pages; GKD and the Lovelock tensors k = 1, 2, 3, with the Rust 19/19, Wolfram 29/29 and sympy 49/49 records) |
| `workflows/` | orchestration records, machine-specific: the workflow scripts of waves 1, 1b and 2 and the wave-1 review record `wave1_review_and_fix.json` (its file paths are repository-relative) | records, not verifiers; no result depends on them. `ROOT` is the location of the repository on the machine where the waves ran; `SP` is a placeholder that the session running a script sets to its own scratchpad directory (the script stops otherwise) |

## Reproduce everything

From the repository root, with Python (numpy, sympy, mpmath, matplotlib, nbformat, nbclient, ipykernel), git, Rust (cargo), WolframScript (activated by you) and pdflatex:

```text
bash Revision/verify_revision.sh                      # Git Bash, WSL, Linux, macOS
pwsh -NoProfile -File Revision/verify_revision.ps1    # PowerShell 7 (the twin: same steps, same checks, same final line)
```

The gate re-runs every verifier and checker of this folder in dependency order (63 steps: algebra, GKD/Lovelock with the author comparison, theory, pairing, the a4 equations with the Kohn-Sham source, Kohn-Sham theory, Rust solver, reference and cross-check, T3 with its completion and demonstrations, both parts of the dark sector, the lead's checks, the notebooks, the six documents in verify mode). It then requires every committed output to be byte for byte unchanged (git diff, with a list of the differing paths) and every report's checks to pass, and runs the Revision unit tests (except the textbook test, which has its own build). The last line is revision_verification=OK or =FAILED; logs are in build/logs/revision/. Options: --dry-run (the steps with their expected wall times), --fast (skips the 8 steps longer than 5 minutes and prints them), --steps a,b,c. Measured on 2026-10-08: --fast about 20 min; the full gate is expected to take about 3 h. The gate never overwrites uncommitted work: it stops at the precheck when an output path of a selected step already differs from HEAD. Revision/tests/test_revision_gate.py checks the twins statically; with REVISION_GATE_FULL=1 it runs the gate with --fast.
