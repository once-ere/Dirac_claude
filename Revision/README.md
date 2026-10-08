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
  positive Fock realisation with Psi^dagger = chi B exists. Both are stated. The good-sector statement was too
  broad and has been corrected after the work: the positive Fock realisation is constructed and checked only
  for single good-sector momenta with frozen coefficients (flat-frame plane waves, in which the deflation of
  the extra times does not enter; checks mode_hamiltonian_good_sector and Fock_space_good_sector_example of
  `theory/reports/wolfram-field-theory.json`, good_sector_positive_fock_realisation of
  `theory/reports/python-field-theory.json`). In the author's metric the curved good-sector mode operator is
  Hermitian only up to a boundary term at z = pi/2; the field-theory record imposes no boundary condition
  there (the Z2 brane is an ASSUMPTION, stated where it is used, e.g. in T2 and T3), and without one the good
  sector has complex frequencies (for U = 0) whenever m^2 < 9 H^2 (checks good_sector_hermiticity_up_to_the_brane_flux
  and good_sector_x8_independent_modes_without_boundary_condition of `theory/reports/wolfram-scope.json`). A
  positive-norm Hilbert space for the full field in the deflating background is not established.
  The energy-momentum tensor operator for lambda != 0 (U = (lambda/2) S^2) was checked after the work in a
  finite fermionic Fock model of one good-sector plane-wave mode set with frozen coefficients
  (`theory/fock_quartic/`, one Python/sympy checker, 21/21): its on-shell identity
  sum_mu <:K_mu:> = <:(m + U')S:>, and with it rho = m S + U and p = S U' - U, holds there as an exact
  operator identity if and only if the potential and the tensor are Wick (normal) ordered; with the other
  orderings tested it fails already in expectation values. Nothing is proved for the field on a whole slice,
  for the curved x8 dependence or for the extra-time sector, and symmetry and conservation of the quartic
  operator are not verified.
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
| `gkd_lovelock/` | GKD (pure-Rust generalized Kronecker delta) and the three Lovelock tensors of this metric | computed (commit 3e81eeb), 19/19 Rust checks; verified in `verification/`: sympy 49/49, Wolfram 29/29; compared with the author's stored outputs in `comparison/` (2026-10-08): 78 checks, 73 PASS, 0 FAIL, 5 NOT-AVAILABLE - the author's metric, Ricci scalar and Einstein tensor agree exactly; the author's notebooks hold no output for k = 2, 3 |
| `algebra/` | the author's gammas, C, Gamma, B, Pin(4,4) and Spin(4,4) facts | Wolfram 45/45, sympy 35/35 |
| `theory/` | Lagrangians, field equations, non-triviality, EMT, quantisation (Wolfram + sympy); scope checks (frame dependence, boundary terms, growth, sign of the energy) | Wolfram 84/84, sympy 70/70 (comparison with Wolfram: agree); scope Wolfram 15/15, sympy 14/14; EMT operator for lambda != 0 in a finite Fock model `theory/fock_quartic/` (sympy only) 21/21 (2026-10-08) |
| `field_equations_a4/` | the Einstein-Lovelock equations for a4[x4] with each field as source; the Kohn-Sham states as a source; `ks_source/`: the a4 equations with the Kohn-Sham source (exact identities, hidden-direction moments, the integration of a stated truncated system) | Wolfram 52/52, sympy 63/63; Kohn-Sham source conditions 5/5 (the recorded Kohn-Sham states are not admissible sources); `ks_source/` 23/23 (no recorded Kohn-Sham state is an admissible source, so nothing about a4 is derived from the coupled problem; in the stated approximation the source does not start or select the deflation of the extra times) |
| `kohn_sham/` | Kohn-Sham fermion gas in the deflating field (instantaneous states along the prescribed history a4 = A H x4): theory, Rust solver, independent reference, cross-check | theory Wolfram 46/46, sympy 58/58; Rust solver 42/42, determinism 14/14, Mermin roots 5/5; reference 37/37; full cross-check of the canonical matrix (Rust solver against the reference) 31/31 (2026-10-08); tip-cutoff study `kohn_sham/tip_convergence/` 7/7 (2026-10-08; L = 3 to 6: the free results with k != 0 converge and the recorded L = 3 values lie within 1.4% in E_KS; the interacting zero-mode results and N = 688 at a4,0 = 0 depend strongly on L, and L -> infinity is not established for them); document `docs/KOHN_SHAM_DEFLATING_FIELD` |
| `dark_sector/` | the two hypotheses against the Unite values: `dirac16complex/` (Hypothesis) and `dirac16complex00/` (Hypothesis00) | `dirac16complex/`: derivation 30/30, Kohn-Sham history 5/5, equation of state 13/13, independent implementation 9/9; `dirac16complex00/`: derivation and models 49/49, independent numerics 28/28. Neither Hypothesis nor Hypothesis00 is established (what each field can and cannot produce under the stated observer assumption: document `docs/DARK_SECTOR_HYPOTHESES`) |
| `pairing/` | the pairing theorems T1, T2, Q for both fields; `pairing/kohn_sham/`: T3 and its completion (2026-10-08: the Kohn-Sham potentials read from the Kohn-Sham record, the filling convention carried onto the -m member, the 16-component statement S6) with two numerical demonstrations | Wolfram 101/101, sympy 66/66; T3 Wolfram 10/10, sympy 13/13; completion Wolfram 3/3, sympy 7/7; demonstrations (not proofs) Rust solver 7/7 (210 states), reference solver 7/7 (18 states) |
| `notebooks/` | executed Jupyter notebooks of the Revision record, each with its provenance file and listed in `notebooks/README.md`, and the build, check and audit tool `tools/build_notebooks.py`: three notebooks, `lovelock_gkd.ipynb` (the Lovelock tensors with the GKD), `kohn_sham_states.ipynb` (the Kohn-Sham states in the deflating field) and `dark_sector_hypotheses.ipynb` (the two hypotheses against the Unite values) | each notebook re-checks its outputs against the committed records; test `tests/test_revision_notebooks.py`; the gate step notebooks-check audits and re-executes all three |
| `docs/` | md + tex + pdf documents, all six of SPEC section 10 | built and registered in `pdf-specifications.json`, each with its publication test `tests/test_*_publication.py`: DIRAC16COMPLEX_FIELD_THEORY (33 pages), DIRAC16COMPLEX00_FIELD_THEORY (37 pages) and PAIR_CREATION_PROOFS (33 pages), all three updated on 2026-10-08 with the results of wave 2; KOHN_SHAM_DEFLATING_FIELD (22 pages), DARK_SECTOR_HYPOTHESES (24 pages); LOVELOCK_GKD (24 pages; GKD and the Lovelock tensors k = 1, 2, 3, with the Rust 19/19, Wolfram 29/29 and sympy 49/49 records) |
| `lead_checks/` | the lead's independent checks, written from scratch (they import no other Revision code): the divergence of the energy-momentum tensor and gamma^mu Omega_mu, the Einstein-Gauss-Bonnet a4 equation, charge conjugation and U(1) (`lead_checks/README.md`) | run by the gate steps lead-*; every check of their three reports in `lead_checks/reports/` passes (gate step reports-pass) |
| `tests/` | the Revision unit tests: the publication test of each of the six documents, the GKD/Lovelock, lead-check, notebook and gate tests, and the textbook test | the gate step unit-tests runs all of them except the textbook test `test_universes_in_pairs_textbook.py`, which belongs to the textbook's own build |
| `textbook/` | the textbook "Universes in Pairs" (binding plan `textbook/TEXTBOOK_SPEC.md`): md + tex + pdf, the chapters in `chapters/`, executed notebooks in `notebooks/` (each with its provenance file), data, figures and the build tools in `tools/` | the pdf is registered in `pdf-specifications.json` (6082 pages); not run by the gate: its own build and its test `tests/test_universes_in_pairs_textbook.py` |
| `workflows/` | orchestration records, machine-specific: the workflow scripts of waves 1, 1b and 2 (`revision_wave_1.js`, `revision_wave_1b.js`, `revision_wave_1b_then_2.js`, `revision_wave_2.js`) and the wave-1 review record `wave1_review_and_fix.json` (its file paths are repository-relative); the scripts of the later work (the preparation of the author's gammas with `a4_patch/`, the Dirac-matrices audit, the execution provenance, the textbook, `completion/` with its review records), their restart copies in `restart/` and the saved workflow states in `state_2026-10-07/` and `state_restart/` | records, not verifiers; no result depends on them. `ROOT` is the location of the repository on the machine where the waves ran. `revision_wave_1.js`, `revision_wave_1b.js`, `revision_wave_2.js` and the `.js` scripts of `restart/` other than `restart/a4_apply_sync.js` (and their generator `restart/make_restart_scripts.py`) hold `SP` as the placeholder `<SCRATCHPAD OF THE RUNNING SESSION>`, which the session running a script sets to its own scratchpad directory (the script stops otherwise); the other `.js` scripts, `completion/make_phase1.py` and several saved states keep the scratchpad path of the session that ran them (`restart/merge_state.py` that session's workflow folder), as a record; the remaining Python helpers hold no session path |

## Reproduce everything

From the repository root, with Python (numpy, sympy, mpmath, matplotlib, nbformat, nbclient, ipykernel), git, Rust (cargo), WolframScript (activated by you) and pdflatex:

```text
bash Revision/verify_revision.sh                      # Git Bash, WSL, Linux, macOS
pwsh -NoProfile -File Revision/verify_revision.ps1    # PowerShell 7 (the twin: same steps, same checks, same final line)
```

The gate re-runs every verifier and checker of this folder in dependency order (65 steps: algebra, GKD/Lovelock with the author comparison, theory with the finite-Fock check of the quartic EMT operator, pairing, the a4 equations with the Kohn-Sham source, Kohn-Sham theory, Rust solver, reference, cross-check and tip-cutoff study, T3 with its completion and demonstrations, both parts of the dark sector, the lead's checks, the notebooks, the six documents in verify mode). It then requires every committed output to be byte for byte unchanged (git diff, with a list of the differing paths) and every report's checks to pass, and runs the Revision unit tests (except the textbook test, which has its own build). The last line is revision_verification=OK or =FAILED; logs are in build/logs/revision/. Options: --dry-run (the steps with their expected wall times), --fast (skips the 8 steps longer than 5 minutes and ks-rust-determinism, which needs one of them, and prints the 9 skipped steps; it runs 56 steps), --steps a,b,c. Measured on 2026-10-08: the 55 steps that --fast had then took about 20 min (theory-fock-quartic, about 10 s, was added afterwards); the full gate is expected (sum of the expected step times, 11142 s, not measured) to take about 3.1 h.

What has passed through the gate (2026-10-08): with bash, the 55 steps that --fast had then, in two parts (1169 s and 164 s), each ending with revision_verification=OK; with PowerShell 7, 49 of them in a scratch clone, ending OK (gkd-author-extract, gkd-author-compare, notebooks-check, the two field-theory pdf steps and unit-tests have not been run with the PowerShell twin). notebooks-check then covered lovelock_gkd and kohn_sham_states; dark_sector_hypotheses was added later. The two steps added afterwards, theory-fock-quartic and ks-tip-convergence, have not been run through the gate; their scripts were run directly with byte-identical outputs (fock_quartic three times, one of them with another PYTHONHASHSEED; tip_convergence three times, the last by the lead on 2026-10-08). The full gate has never run to the end, and the 9 long steps have never been run through the gate. Their committed reports come from individual runs (commit that last wrote each report): gkd-rust-selftest `gkd_lovelock/results/gkd-selftest.json` (content eb03ec8, moved by ad02ebb, 2026-10-01); theory-wolfram `theory/reports/wolfram-field-theory.json` (a9a1b70, 2026-10-01; re-run byte-identically in fresh clones on 2026-10-02 and 2026-10-07, `theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md`); ks-reference `kohn_sham/reports/ks-reference.json` (a9a1b70, 2026-10-01; repeated byte for byte inside the cross-check, check reference_repeat_byte_identical); ks-rust-refined with ks-rust-determinism `kohn_sham/reports/ks-rust-determinism.json` (c65bb82, 2026-10-07); ks-crosscheck `kohn_sham/reports/ks-crosscheck.json` (df89548, 2026-10-08); t3-rust-demo and t3-reference-demo `pairing/kohn_sham/reports/t3-rust-demo.json` and `t3-reference-demo.json` (c4d2b0a, 2026-10-08); ks-tip-convergence `kohn_sham/tip_convergence/tip-convergence.json` (a8eb09d, 2026-10-08). The step reports-pass reads these reports on every run, also with --fast; it does not re-run them.

The gate never overwrites uncommitted work: it stops at the precheck (revision_failed_step=precheck, exit code 3) when an output path of a selected step already differs from HEAD. Besides build/revision/ and build/logs/revision/, some verifiers write further files under build/, in the git-ignored target/ folders of the two Rust crates and in the system temporary directory (listed in the header of the gate; one of them, revision_gkd_export, is shared), so run only one gate at a time on a computer. Revision/tests/test_revision_gate.py checks the twins statically, checks that every file tracked under Revision/ is stored with LF line endings, and runs three failure paths of each twin on temporary copies (a failing step; the precheck stop; a Wolfram step whose wolframscript cannot open its script and exits with 0, which the gate fails with revision_wolfram_open_failure); with REVISION_GATE_FULL=1 it runs the gate with --fast.

Byte identity of the committed outputs was established on Windows 11 with Python 3.14.5 (numpy 2.4.6, sympy 1.14.0, matplotlib 3.11.0), Wolfram Language 15.0.1 (WolframScript 1.14), Rust/cargo 1.91.1 and MiKTeX pdfTeX 4.27; no Linux or macOS run was made, and other versions or platforms can change bytes (recorded version fields, last digits of floating-point numbers, PNG and PDF bytes) without changing a result. On Windows, clone into a short folder: WolframScript cannot open a script whose path has 260 or more characters (it then exits with 0, and the gate fails the step); the author-curvature extractor works for a repository folder of up to 179 characters.
