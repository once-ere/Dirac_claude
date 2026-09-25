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
| 1. Arbitrary gravitational field | `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD` | see the table below |
| 2. Primordial pair-creation field | `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD` | see the table below |
| 3. Dark-sector numerics | `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS`, `provenance/DIRAC16COMPLEX_STUDENT_GUIDE` | see the table below |

Status at this push (work in progress; the documentation, review and gate phases
are still running): the exact verifiers of Stages 1 and 2 pass (Wolfram algebra
20/21 with one check encoding a since-corrected design claim, Wolfram geometry 43/43,
Python algebra 21/21, Python geometry 51/51, Grassmann demonstration 16/16, Wolfram
primordial 114/114, Python primordial 14/14 with 0 coefficient mismatches); the
Stage-3 Rust study builds cleanly and its five experiments pass their independent
checkers (25/25, 34/34, 31/31, 51/51, 21/21).  PDFs and notebooks that are not yet
present in this commit are still being produced.

## Reproducing

Windows 11 (PowerShell), from the repository root:

```powershell
.\scripts\setup_solver.ps1 -Platform win11
.\scripts\verify_stage1_arbitrary_field.ps1
```

Git Bash, macOS or Linux:

```bash
bash scripts/setup_solver.sh
bash scripts/verify_stage1_arbitrary_field.sh
```

`setup_solver` clones the pinned pure-Rust SUNDIALS 7.8.0 engine from
`once-ere/rustSolveIt_{Win11,macos-silicon,linux}_SUNDIALS_7_8_0` into the
git-ignored `vendor/rustSolveIt`.  WolframScript (Wolfram Engine or Mathematica),
Python 3 with numpy and sympy, and a TeX distribution are needed for the exact
verifiers and the PDFs; the student guide lists every step.

## Repository map

- `wolfram/` exact Wolfram Language packages (algebra, geometry, primordial field).
- `scripts/` verifiers, independent exact Python checkers, the Grassmann-algebra
  demonstration, publication tooling and stage gates.
- `artifacts/dirac16complex/` exact fixtures and machine-readable reports.
- `provenance/` the documents (Markdown source, generated LaTeX, PDF).
- `studies/dirac16complex_cosmology/` the Rust CVODE study (Stage 3).
- `notebooks/` Jupyter and Mathematica notebooks (Stage 3).
- `tests/` unittest suites.
- `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`
  the author's original notebook (input; not modified).

## Scientific boundary

The (4,4) signature is not observed spacetime.  Canonical quantization in x4 gives
an indefinite-metric (Krein) state space; a positive Fock space exists in the sector
independent of the three extra times, while modes depending on them are unstable.
The cosmological computations are homogeneous backgrounds (mean field and mode
sums); perturbation stability and data likelihoods are not studied, and no
observational detection is claimed.

## Credits and licences

GPL-3.0-or-later (see `LICENSE`).  Original notebook and physical programme:
Patrick L. Nash.  Publication tooling derived from https://github.com/once-ere/dirac
(GPL-3.0-or-later).  The numerical engine is the pure-Rust SUNDIALS 7.8.0 port
(BSD-3-Clause, LLNL) from the rustSolveIt repositories, fetched at build time and
not redistributed here; see `NOTICE`.  Prepared with Claude Opus 5.5.
