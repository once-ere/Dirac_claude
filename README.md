# dirac16complex

A 16-component complex Grassmann (fermion) spinor field of Pin(4,4) in 4+4
dimensions: its Lagrangian, covariant field equations, canonical quantization,
energy-momentum tensor and equations of state, first in an arbitrary gravitational
field, then in the primordial pair-creation field of the author's notebook, and
finally a numerical investigation of whether its pressure and energy density
behave like dark matter and/or dark energy.

## The new revision UM-3 (2026-10-24): `universe_model_3/`

On 2026-10-24 the author ordered a major new revision and the permanent stop of every earlier stage (W8, old Stages 4 and
5, the follow-ups of UM-2; nothing was running, and every verified result was already on `main`; see `HANDOFF.md`
section 0.14). The revision is in [`universe_model_3/`](universe_model_3/README.md): the author's new notebook `4+4.nb`
(the eight real 16 x 16 Dirac matrices), its provenance `universe_model_3/dirac matrices.md`, the new metric with
b4(x4)^2 (b4 never identically 1), the Higgs doublet, the electroweak gauge fields W1, W2, W3, B, gluons, three
generations of quarks and leptons, and dirac16complex coupled to gravity and, with separate left-handed and
right-handed couplings, to every Standard-Model field, with the complete coupled field equations and a Kohn-Sham
approximate solution. Completed on 2026-10-25: the documents `MODEL`, `FIELD_EQUATIONS`, `SOLUTION`, `ANALYSIS` and
`PROVENANCE` (each as .md, .tex and .pdf, every equation written out and every symbol defined in each of them), with
167 verification checks in 13 modules, all passing. The solution covers the background and the metric as a power
series, the Higgs field in the ad hoc vacuum, the spectra along the hidden direction (the `x0` mass of the bound states),
the self-consistent Kohn-Sham states of dirac16complex, the neutrino flavours (Sun, supernova envelope, fast instability,
equipartition), the thermal history with the portals and direct detection, and the CMB (Planck 2018), BAO (DESI DR2) and
CNB. Its README states every part and its checks.

## The universe model UM-2: `universe_model_2/`

On 2026-10-17 the author ordered a new model of the Universe: Einstein-Lovelock gravity with the author's weights and
Lambda, the dirac16complex field (the dark-matter hypothesis) coupled through the canonical spin connection, photons,
neutrinos, electrons, quarks, gluons, W+ (charge +e), W- (charge -e) and Z, no Higgs particle, every mass from the x0
dependence of wave functions with period pi/(6H). On 2026-10-18 he ordered three neutrino flavours with mixing and flavour
conversion; version 2 of the model therefore has three full generations of quarks and leptons (anomaly free generation by
generation), the PMNS and CKM matrices from the x0 mechanism, and the flavour conversion of the neutrinos in vacuum, matter,
the Sun, the early Universe (N_eff), the cosmic neutrino background and supernovae. The model, its provenance, its coupled
field equations, an approximate solution with Kohn-Sham theory for dirac16complex, and the analysis of the x0 mass mechanism
and of the dark-matter and dark-energy associations are in [`universe_model_2/`](universe_model_2/README.md) (documents as
.md, .tex and .pdf; 235 verification checks, all passing). An independent review of version 2
found that the relic abundance of its dark matter (the heavy odd quanta of dirac16complex) cannot be produced by the
gauge-kinetic portal within perturbative unitarity. Version 3 (2026-10-18) adds the s-wave portal I13 (an x0-chiral vector
coupling of dirac16complex to the baryon-number current), with which each of the two dark-matter species leaves Omega h^2 =
0.060 within the unitarity limit, the thermal history with the freeze-in of the fold bands (Delta N_eff = 0.001), the coupled
Kohn-Sham solution in ten environments, and the metric as a power series of terms of decreasing magnitude. An independent
review of version 3 led to the I13 sum over the seven directions other than x0 (where its bilinear is Hermitian), the full
block response to the hot plasma, the order-alpha electroweak condensates and a bound on the self-interaction of dirac16complex.
Version 3 with these fixes was reproduced from a fresh clone of the repository on 2026-10-18 (commit 815db9e, all 235
checks passed, every stored number reproduced, the documents rebuilt byte-identical). Version 4 (2026-10-18) reorganises and
re-presents the model at the author's order: every one of the 841 display equations of the five documents is followed by the
complete list of its symbols (one meaning per symbol, generated from one registry and checked by a script), the 136 field
equations and 18 interaction terms are numbered and written out wherever they are used, and a new computation measures the
residual of the approximate solution in 26 field equations and its consistency across 26 links between them; reproduced from
a fresh clone (commit cec385b, 287 of 287 checks, every number identical, the documents byte-identical).

## The current record: `Revision/`

Since 2026-10-01 the authoritative record of the author's primordial gravitational field is the
separate folder [`Revision/`](Revision/README.md) (binding plan [`Revision/SPEC.md`](Revision/SPEC.md)),
written anew and not mixed with the earlier stages described further below, which are kept unchanged.
It uses the author's metric with the second function b4(x4) (the change of 2026-10-14; b4 is a
function of x4, never 1). In particular, the dark-sector hypotheses of dirac16complex and
dirac16complex00 are investigated there for that metric: the record is
[`Revision/dark_sector/`](Revision/dark_sector/), the provenance of its change to b4(x4) is
[`Revision/dark_sector/B4_PROVENANCE.md`](Revision/dark_sector/B4_PROVENANCE.md), and the document is
[`Revision/docs/DARK_SECTOR_HYPOTHESES.md`](Revision/docs/DARK_SECTOR_HYPOTHESES.md) (neither hypothesis
is established). The textbook "Universes in Pairs" is in [`Revision/textbook/`](Revision/textbook/).
The Stage-3 dark-sector numerics below were computed before the Revision (completed 2026-09-30, on
homogeneous backgrounds without b4, with static extra times in two of the five experiments) and are
superseded by that record.

**Work in progress (2026-10-16): everything in `Revision/` moves to b4(x4).** The order of 2026-10-15 ("move
everything to b4(x4); b4 is never 1") is carried out in nine phases ([`HANDOFF.md`](HANDOFF.md), section 0.9;
the rule is in [`Revision/SPEC.md`](Revision/SPEC.md), section 1: exact results for general b4(x4), numerical
work on the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4}, a prescribed background). Done and pushed: phase 1
(`Revision/theory/`: Wolfram 84/84, sympy 72/72, scope 15/15 and 14/14, all for general a4 and b4), phases 2
and 3 (`Revision/field_equations_a4/`: Wolfram 59/59, sympy 65/65; `Revision/lead_checks/`: 10/10, 14/14,
12/12). In progress: phase 4, the Kohn-Sham record (`Revision/kohn_sham/`). Still open: phases 5 to 9 (the
Kohn-Sham source, pairing, the Revision notebooks, the documents and the textbook). Until they are done, the
records of those folders still describe b4 = 1, the gate steps a4-ks-source and a4-ks-source-unittest stop, and
the publication tests of three Revision documents fail (they quote the b4 = 1 check names); the dark sector
(`Revision/dark_sector/`) was already computed with b4(x4) on 2026-10-15.

Everything is counted from 0: coordinates `x = {x0,...,x7}`, frame indices
`a = 0..7`, spinor components `Psi_0..Psi_15`.  The tangent metric is
`eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)` and `x4` is the evolution time.

## The object

`dirac16complex` is a section `Psi` of the complexified rank-16 spinor bundle
`S_C = P_Spin(M) x_rho (C (x) (Delta_- (+) Delta_+))` whose components are complex,
anticommuting (Grassmann-odd) fields.  Under Pin(4,4) (double cover of O(4,4))
`C^16` is irreducible; under Spin(4,4) (double cover of SO(4,4), the determinant-1
transformations) it is the direct sum of two inequivalent irreducible
8-dimensional representations.  Both statements are proved by exact commutant and
intertwiner computations.

The gamma matrices are the author's eight REAL 16 x 16 Dirac matrices `T16^A[0..7]`,
taken by evaluating the author's own notebook cells.  `provenance/dirac matrices.md`
proves that they are real and satisfy `{T16^A[a], T16^A[b]} = 2 eta_ab I16`.  It proves
that the scaled commutators `(1/4)[T16^A[a], T16^A[b]]` span spin(4,4) and generate
Spin_0(4,4); together with `T16^A[0]` and `T16^A[4]` they generate Pin(4,4).  It
displays the matrices, their products and the projectors `P_L`, `P_R`, and checks that
every gamma source in the repository equals them.

Its Lagrangian density, loosely based on the notebook's `Lg[]`, is

    L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
                  - m Psibar Psi - U(Psibar Psi) ],        Psibar = Psi^dagger sigma16,

with the canonical (Levi-Civita) spin connection
`D_mu = d_mu + (1/8) omega_{mu ab} [gamma^a, gamma^b]` fixed by the vielbein
postulate (the total covariant derivative of the vielbein vanishes).  Its
Euler–Lagrange equation is `gamma^mu D_mu Psi = (m + U'(Psibar Psi)) Psi`.

Three findings about the notebook's `Lg[]` motivated this construction (each is
proved exactly, in Wolfram Language and independently in Python):

1. `sigma16` is symmetric and `sigma16 . T16^A` antisymmetric (the task's
   expression [1]); for an anticommuting real `Psi16` the mass term vanishes and the
   kinetic term is a total divergence, so `Lg[]` has empty Euler–Lagrange
   equations (0 = 0).  A complex field with the Dirac adjoint is required.
2. `Lg[]` contracts the mixed `omega_mu^a_b` with `SAB[[a,b]] = S^{ab}`: one metric
   factor is missing.  With that contraction the gamma matrices are not covariantly
   constant; with `omega_{mu ab} = eta_ac omega_mu^c_b` they are.
3. In the notebook's cell 1058 the rule
   `1/Sqrt[Sin[6Hx0]^(1/3)/E^(2a4)] -> 1/(E^a4 Sin[6Hx0]^(1/6))` is wrong (the correct
   right-hand side is `E^a4/Sin[6Hx0]^(1/6)`); a reconstruction with it reproduces
   the stored cell-1137 equations exactly, including a spurious term
   `q = Q1 Sinh[a4] a4' E^-a4`.  The correct equations differ from cell 1137 only by
   that term.

## Stages and documents

| Stage | Document (Markdown, LaTeX, PDF) | Status |
|---|---|---|
| 1. Arbitrary gravitational field | `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD` | see the status list below |
| 2. Primordial pair-creation field | `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD` | see the status list below |
| 3. Dark-sector numerics | `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS`, `provenance/DIRAC16COMPLEX_STUDENT_GUIDE` | see the status list below |
| 4. Kohn–Sham DFT, ground and first excited states | `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL`, `provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE` (not yet written) | see the status list below |
| 5. dirac16complex00 (commuting spinor field) and the {+M, −M} pairing | `provenance/DIRAC16COMPLEX00_FIELD_THEORY`, `provenance/DIRAC16COMPLEX_PAIR_CREATION` (in progress) | see the status list below |

Status at this push (2026-09-30; HANDOFF.md section 2 is the authoritative,
per-stage list):

- **Stages 1 and 2 are complete.** Their exact verifiers, documents and reviews are
  done, and both gate twins of each stage pass from fresh public clones.  The Stage 1
  gate needs nothing private: without the git-ignored reference folder `dirac-main/`
  it runs in a public-clone mode that regenerates every file into `build/stage1/`,
  requires the regenerated files to equal the committed ones except for the
  dirac-main cross-checks, which it reports as skipped; with `dirac-main/` it also
  reproduces those cross-checks.
- **Stage 3 is complete.** The engine, the five experiments and their checkers,
  both notebooks, the figures and both documents are committed; the 21 problems of
  the second review round are fixed; both gate twins `scripts/verify_stage3_dark_sector.{sh,ps1}`
  passed from fresh public clones (all 32 steps, 323 unit tests).
- **Stage 4 is not finished.** The exact Kohn–Sham theory (Wolfram 125/125, sympy
  157/157) and the Rust Kohn–Sham solver `studies/dirac16complex_kohn_sham` are
  complete and reproducible.  The independent Python reference agrees on 65 of 69
  cross-checks; 4 disagreements remain (`handoff/reviews/stage4_crosscheck_quick_2026-09-30.log`).
  The Stage-4 notebooks, documents, review and gate do not exist yet.
- **Stage 4 is paused** at the user's request (2026-09-30).
- **Stage 5 is in progress** (specification `handoff/specs/STAGE5_SPEC.md`): the
  classical commuting 16-component Pin(4,4) spinor field dirac16complex00, the
  Lagrangians of both fields with explicit mass terms, their energy-momentum tensors
  and equations of state in an arbitrary and in the primordial field, the Kohn–Sham
  ground and first excited states of both fields, and exact theorems on pairs of
  universes of masses +M and −M.

## Reproducing

Windows 11 (PowerShell), from the repository root:

```powershell
.\scripts\setup_solver.ps1 -Platform win11
.\scripts\verify_stage1_arbitrary_field.ps1
.\scripts\verify_stage2_primordial_field.ps1
.\scripts\verify_stage3_dark_sector.ps1
.\scripts\verify_stage4_kohn_sham.ps1
```

Git Bash, macOS or Linux:

```bash
bash scripts/setup_solver.sh win11
bash scripts/verify_stage1_arbitrary_field.sh
bash scripts/verify_stage2_primordial_field.sh
bash scripts/verify_stage3_dark_sector.sh
bash scripts/verify_stage4_kohn_sham.sh
```

Each gate ends with the line `stageN_..._verification=OK`.  The Stage 3 gate
reruns all five experiments twice and executes both notebooks (tens of minutes).
The Stage 4 gate reproduces the Rust Kohn–Sham outputs byte for byte, which takes
hours; its header lists the wall time of every step.

`setup_solver` clones the pinned pure-Rust SUNDIALS 7.8.0 engine from
`once-ere/rustSolveIt_{Win11,macos-silicon,linux}_SUNDIALS_7_8_0` into the
git-ignored `vendor/rustSolveIt`.  The committed numerical outputs were produced
with the Win11 engine (commit `a8fdff45`), which reproduces them byte for byte on
Windows and Linux; the macOS/Linux engines carry a different mathematical library,
so their results agree to solver tolerance rather than byte for byte.  WolframScript (Wolfram Engine or Mathematica),
Python 3 with numpy and sympy, and a TeX distribution are needed for the exact
verifiers and the PDFs; the student guide lists every step.

## Repository map

- `wolfram/` exact Wolfram Language packages (algebra, geometry, primordial field,
  Kohn–Sham reduction).
- `scripts/` verifiers, independent exact Python checkers, the Grassmann-algebra
  demonstration, publication tooling and stage gates.
- `artifacts/dirac16complex/` exact fixtures and machine-readable reports.
- `provenance/` the documents (Markdown source, generated LaTeX, PDF).
- `studies/dirac16complex_cosmology/` the Rust CVODE study (Stage 3).
- `studies/dirac16complex_kohn_sham/` the Rust Kohn–Sham solver: CVODE shooting of
  the reduced 2×2 block equations and self-consistent field iteration (Stage 4).
- `notebooks/` Jupyter and Mathematica notebooks (Stages 3 and 4).
- `handoff/` the restart kit (specifications, workflow scripts, review records);
  see `HANDOFF.md`.
- `tests/` unittest suites.
- `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`
  the author's original notebook (input; not modified).

## Scientific boundary

The (4,4) signature is not observed spacetime.  Canonical quantization in x4 gives
an indefinite-metric (Krein) state space; a positive Fock space exists in the sector
independent of the three extra times, while modes depending on them are unstable.
The cosmological computations are homogeneous backgrounds (mean field and mode
sums); perturbation stability and data likelihoods are not studied, and no
observational detection is claimed.  The Kohn–Sham computations of Stage 4 are
static mean-field states of a finite number of quanta in the fixed primordial
field (no back-reaction on the metric), with the exact Hartree–Fock exchange of
the contact interaction and no correlation term.

## Credits and licences

GPL-3.0-or-later (see `LICENSE`).  Original notebook and physical programme:
Patrick L. Nash.  Publication tooling derived from https://github.com/once-ere/dirac
(GPL-3.0-or-later).  The numerical engine is the pure-Rust SUNDIALS 7.8.0 port
(BSD-3-Clause, LLNL) from the rustSolveIt repositories, fetched at build time and
not redistributed here; see `NOTICE`.  Prepared with Claude (Opus 5.5 and Fable 5.1).
