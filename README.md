# dirac16complex

A 16-component complex Grassmann (fermion) spinor field of Pin(4,4) in 4+4
dimensions: its Lagrangian, covariant field equations, canonical quantization,
energy-momentum tensor and equations of state, first in an arbitrary gravitational
field, then in the primordial pair-creation field of the author's notebook, and
finally a numerical investigation of whether its pressure and energy density
behave like dark matter and/or dark energy.

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

- **Stages 1 and 2 are complete in content.** Their exact verifiers, documents and
  reviews are done.  The Stage 2 gate `scripts/verify_stage2_primordial_field.*`
  passed from a fresh public clone.  The Stage 1 gate
  `scripts/verify_stage1_arbitrary_field.*` passes on the author's machine, but a
  fresh public clone showed that it needs the private input folder `dirac-main/`,
  which is not in the repository; a public-clone mode is being added.
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
