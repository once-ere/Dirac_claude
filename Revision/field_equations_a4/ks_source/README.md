# field_equations_a4/ks_source: the field equations for a4 and b4 with the Kohn-Sham source (SPEC sections 5 and 7)

Revision code only. The metric is the author's metric with b4(x4) in the three extra-time components (b4 a function of
x4, never 1; `Revision/SPEC.md`, section 1); the analysis was moved to it on 2026-10-16 (`HANDOFF.md` 0.9, phase 5).
Inputs (read-only): `Revision/field_equations_a4/a4-equations.json` (the Einstein-Lovelock equations for a4[x4] and
b4[x4], key generalSource), the Kohn-Sham results of `Revision/kohn_sham` (`results/parameters.json`,
`results/ground/profiles/*.csv`, `results/ground/emt-integrals.csv`, `results/adiabatic/adiabaticity.csv`,
`results/adiabatic/history.json`, `ks-theory.json`), the source-condition report
`Revision/field_equations_a4/reports/ks-source-conditions.json`, and the dense free-gas history of the same record
(`Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv`, 41 slices). The report records the sha256 digest of
every input.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three extra times, which DEFLATE
EXPONENTIALLY when a4 increases (scale factor e^{-a4} b4^{1/2} sin^{1/6} z); x0 = the hidden direction (Kohn-Sham
coordinate y = ln(sin z)/(6H), sqrt|g| dx0 = b4^{3/2} e^{6Hy} dy). u = b4'/b4.

| file | role |
| --- | --- |
| `ks_source_a4.py` | the analysis (sympy for the exact identities, plain Python floats for the numerics); writes the four outputs below; exit code 0 iff every check passes |
| `test_ks_source_a4.py` | unit tests, the reproducibility of the committed outputs, and two negative controls (tampered Kohn-Sham inputs must fail) |
| `results/ks-source-moments.csv` | per Kohn-Sham state: hidden-direction averages rho_bar, p3_bar, p_t_bar, p0_bar (per proper cell volume, in units of b4(0)^{-3/2}), the mismatch measures, the defects, the conservation residuals |
| `results/ks-source-a4-cases.csv` | per integration case (the author's weights: 2 series; Gauss-Bonnet: 2 series x 2 branches x 7 parameter choices): Lambda, outcome, a4'(a4) and u(a4) at the slices, both integration methods, the residuals of the dropped equations, the adiabaticity measure |
| `reports/ks-source-a4.json` | every check (name, verdict, detail), the assumptions, the conclusions |
| `reports/ks-source-a4-summary.md` | the results in words and tables, generated from the same run |

Run from the repository root (after `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`, whose dense history
is an input):

```text
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
```

Two runs of the script give byte-identical outputs (LF). Run time of the script: about 2 s (2026-10-16); of the test file
about 12 s (2026-10-16, idle machine).

## What is computed (all numbers in the report and the summary; 22 checks)

* **Exact (A, sympy).** From the record of the a4 and b4 equations: the x1 + x5 - 2 x0 combination reads
  kappa (p3 + p_t - 2 p0) = I(a4', a4'', u, v); I vanishes for b4 constant (the identity of the withdrawn metric) and on
  the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4} with the author's weights, but it is not an identity for general b4.
  The off-diagonal equation is kappa q40 = cot z u Q(a4', u): every Kohn-Sham state has q40 = 0, so a history with b4
  not constant needs Q = 0 at every instant; in Einstein gravity Q = 3H/2, so there is no such history at all. The x4
  component is a constraint (first order); its propagation (the x4 component of the Bianchi identity) holds with the
  u terms; the x0 conservation identity in the Kohn-Sham coordinate is p0_y + 6 H p0 = 3 H (p3 + p_t) for every b4. The
  real branches of Q(H, u) = 0: none for Einstein, u = 4/3 H for the author's weights (u = 0 is the excluded constant
  b4; this is the record's history), u = (-6 +- 2 sqrt 5) H for the stated Gauss-Bonnet case (alpha2 H^2 = 1/80), none
  for the stated cubic Lovelock case.
* **The source-condition report verified (B0).** The numbers of `../reports/ks-source-conditions.json` are re-derived
  independently from the same Kohn-Sham files and agree. The recorded states SATISFY the x0 conservation identity; what
  they violate is x0-independence.
* **The source the equations need versus the computed profiles (B).** The recorded states conserve energy-momentum
  along x0 (checked on every profile); their violation of p3 + p_t = 2 p0 is therefore exactly the x0 dependence of p0.
  The mismatch with an x0-independent source (L1 and L2 with the volume weight) is O(1) for every state.
* **Hidden-direction moments along the record's history (C).** The x1 + x5 - 2 x0 moment fails by an O(1) defect; the
  averaged energy relation holds with the b4 term (dE/da4 = -3 (P3 - P_t) - 2 P_t); the x4 moment of the author's
  equations needs the constant source kappa rho = -2/27 (H = 1) at every slice, while the Kohn-Sham rho_bar changes by
  factors 336 to 2967 along the history: the record's history is not a solution even of the x4 moment.
* **Integration (D, an approximation, stated).** The truncated system "x4 moment + off-diagonal equation" (both exact
  necessary conditions) is, for a given source, two algebraic equations for (a4', u). It is integrated in a4 over
  [0, 2] from a4'(0) = H on every real branch, for the free gas (N136_lam0, N688_lam0), whose averaged source is known on
  any (a4, b4) path (rho_bar = E(a4)/(cell volume b4^{3/2}), E independent of b4; E from the dense record history), by
  two methods (Hermite with the exact slopes and RK4 step 1e-3; a spline of ln E and step 2e-3), which agree to 3.3e-4.
  One combination of the dropped second-order equations holds by the propagation identity (checked to 7e-16); the
  other residuals are O(1). Outcomes: regular (through a4 = 2), fold (the real solution of the two algebraic equations
  ends), adiabaticity_lost (the adiabaticity measure of the free gas reaches 1: the instantaneous states are no longer
  a valid source).

## Answer to "does the dirac16complex source drive exponential deflation of the extra times?"

Exactly: no. No recorded Kohn-Sham state is an admissible source of the author's metric with b4 (x0 dependence, for
every a4 and b4), and in Einstein gravity no source without T^x4_x0 (every Kohn-Sham state) is compatible with any
history in which b4 changes. In the stated approximation, with the author's weights and Lambda = -10, the start on the
record's history needs kappa rho_bar(0) = -2/27 H^2 (kappa < 0 for the gas); as the gas dilutes, the solution leaves
that history and reaches a fold of the algebraic system almost at once (a4 = 0.024 for both series): the record's
history is not continued by the gas. With the stated Gauss-Bonnet coupling, the branch u0 = (-6 + 2 sqrt 5) H runs
through a4 = 2 for kappa rho_bar(0) <= 0 (8 regular cases) and ends at a fold for kappa rho_bar(0) > 0; on the branch
u0 = (-6 - 2 sqrt 5) H b4 collapses, the rates grow until the adiabaticity measure reaches 1 (8 cases) or a fold is
reached. In every case the initial rate and the branch of Q = 0 are initial data and Lambda (or the source strength) is
fixed by the constraint: the source does not select the deflation. The numbers, the residuals of the dropped equations
(O(1), not small) and what is not computed (the interacting series, a4 > 2, thermal states, the non-adiabatic problem)
are in `reports/ks-source-a4.json` and `reports/ks-source-a4-summary.md`.

## History

Until 2026-10-16 this folder analysed the withdrawn metric b4 = 1 (the x1 + x5 - 2 x0 identity, the first integral
P(a4'^2) + Lambda = -kappa rho_bar(a4), Einstein, Gauss-Bonnet and cubic Lovelock with the source strength as a
parameter; 23 checks). The b4 version replaces the first integral by the two algebraic equations of the x4 moment and
the off-diagonal equation; Einstein gravity and the stated cubic Lovelock case drop out exactly (no history with
a4'(0) = H), and the author's weights are added. Two numerical points found while it was written: Newton at the
author's start point (det J = -0.0139, near a fold) needed a convergence test at the rounding level of the residual;
and with the 5 slices of the record the two interpolations of the source differed by 0.7% in one sensitive
Gauss-Bonnet case, so the source is the dense history of the record (41 slices) instead (agreement 3.3e-4, tolerance
5e-3 unchanged).
