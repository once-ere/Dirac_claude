# field_equations_a4/ks_source: the a4 field equations with the Kohn-Sham source (SPEC sections 5 and 7)

Revision code only. Inputs (read-only): `Revision/field_equations_a4/a4-equations.json` (the Einstein-Lovelock equations
for a4[x4]) and the Kohn-Sham results of `Revision/kohn_sham` (`results/parameters.json`, `results/ground/profiles/*.csv`,
`results/ground/emt-integrals.csv`, `results/adiabatic/adiabaticity.csv`, `results/adiabatic/history.json`,
`ks-theory.json`). The report records the sha256 digest of every input.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three extra times, which DEFLATE
EXPONENTIALLY when a4 increases (scale factor e^{-a4} sin^{1/6} z); x8 = the hidden direction (Kohn-Sham coordinate
y = ln(sin z)/(6H), sqrt|g| dx8 = e^{6Hy} dy).

| file | role |
| --- | --- |
| `ks_source_a4.py` | the analysis (sympy for the exact identities, plain Python floats for the numerics); writes the four outputs below; exit code 0 iff every check passes |
| `test_ks_source_a4.py` | unit tests, the reproducibility of the committed outputs, and two negative controls (tampered Kohn-Sham inputs must fail) |
| `results/ks-source-moments.csv` | per Kohn-Sham state: hidden-direction averages rho_bar, p3_bar, p_t_bar, p8_bar, the mismatch measures, the defects, the conservation residuals |
| `results/ks-source-a4-cases.csv` | per integration case (3 gravity theories x 5 source series x 7 parameter choices): kappa, Lambda, outcome, a4'(a4) at the slices, both integration methods, residuals |
| `reports/ks-source-a4.json` | every check (name, verdict, detail), the assumptions, the conclusions |
| `reports/ks-source-a4-summary.md` | the results in words and tables, generated from the same run |

Run from the repository root:

```text
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
```

Two runs of the script give byte-identical outputs (LF). Run time of the script: 3 s on an idle development machine, up
to about 20 s under load (2026-10-08).

## What is computed (all numbers in the report and the summary)

* **Exact (A, sympy).** From the record of the a4 equations: E^x1_x1 + E^x5_x5 = 2 E^x8_x8 for every Lovelock order, so
  the x1 + x5 - 2 x8 combination of the field equations is 0 = kappa (p3 + p_t - 2 p8) for every a4; the evolution
  equation is the x1 - x5 component, a4'' F(a4') = kappa (p3 - p_t); with P(X) = sum_k alpha_k E_(k)^x4_x4 at a4'^2 = X,
  3 F = 2 dP/dX, so the constraint P(a4'^2) + Lambda = -kappa rho propagates into the evolution equation for every source
  obeying d rho/d a4 = -3 (p3 - p_t); F and P are even in a4' (x4 -> -x4 exchanges deflation and inflation of the extra
  times); the x8 conservation identity in the Kohn-Sham coordinate, p8_y + 6 H p8 = 3 H (p3 + p_t), so
  p3 + p_t - 2 p8 = p8_y/(3H) on shell.
* **The wave-1 report verified (B0).** The numbers of `Revision/field_equations_a4/reports/ks-source-conditions.json` are
  re-derived independently from the same Kohn-Sham files and agree. One refinement: the recorded states SATISFY the x8
  conservation identity d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0; what they violate is p3 + p_t = 2 p8, which is that
  identity combined with x8-independence.
* **The source the equations need versus the computed profiles (B).** The recorded states conserve energy-momentum along
  x8 (checked on every profile); their violation of p3 + p_t = 2 p8 is therefore exactly the x8 dependence of p8. The
  mismatch with an x8-independent source is measured with the volume weight e^{6Hy} in two norms (L1 and L2; the
  x8-independent part of a profile is its weighted average): it is O(1) for every state.
* **Hidden-direction moments (C).** Integrating the field equations with sqrt|g| over the patch gives exact necessary
  conditions with the averaged source. The x4 moment and the x1 - x5 moment are mutually consistent for the Kohn-Sham
  history (averaged energy relation, no Fermi-level crossings); every set containing the x8 moment is not; the
  x1 + x5 - 2 x8 moment fails by an O(1) defect for every state.
* **Integration (D, an approximation, stated).** The truncated system (x4 moment + x1 - x5 moment) has the first
  integral P(a4'^2) + Lambda = -kappa rho_bar(a4). It is integrated over the computed range a4 in [0, 2] (initial rate
  a4'(0) = H) for Einstein gravity (alpha1 = 1), Einstein-Gauss-Bonnet (alpha2 H^2 = 1/80) and a cubic Einstein-Lovelock
  case (alpha2 H^2 = 1/80, alpha3 H^4 = 1/4000), with the source strength sigma0 = kappa rho_bar(0)/H^2 in
  {-10, -1, -1/10, 1/10, 1, 10} and with Lambda = 0, by two methods (first integral; RK4 of the evolution equation with
  an independently interpolated source) that agree to the stated tolerance. Outcomes: regular, turning point (a4' = 0:
  the deflation halts; the integration stops there and what follows is not computed) or branch point (F = 0: the
  evolution equation is not defined). Integrated series: N136_lam0, N688_lam0, N688_lamp2, N688_lamm2 (with
  3-momentum) and N8_lamp2; the other series of the Kohn-Sham record are not integrated.

## Answer to "does the dirac16complex source drive exponential deflation of the extra times?"

Exactly: the question has no solution to examine. No recorded Kohn-Sham state is an admissible source of the author's
metric (x8 dependence; the algebraic condition fails, also after averaging over the hidden direction), so nothing about
a4 is derived from the coupled equations. In the stated approximation the source does not start or select exponential
deflation. The initial rate and its sign are initial data, Lambda is fixed by them, and the gas changes a4'^2 only by a
bounded amount set by the energy it loses. It speeds the deflation up for kappa rho_bar > 0 and slows it down for
kappa rho_bar < 0. With Lambda = 0 the deflation halts (a4' = 0) inside the computed range for each of the four
integrated series with 3-momentum (N136_lam0, N688_lam0, N688_lamp2, N688_lamm2; the other six series with 3-momentum
were not integrated); the integration stops at that turning point, and what follows it is not computed. With
Gauss-Bonnet and kappa rho_bar > 0 the evolution reaches a branch point. A source that does not change with a4 (the
N = 8 interacting states) gives exactly the linear member a4 = A H x4 + a0 within the approximation: exponential
deflation at the rate chosen initially, allowed but not selected. The numbers, the residuals of the dropped equations (O(1), not small) and
what is not computed (a4 > 2, thermal states, the non-adiabatic problem) are in `reports/ks-source-a4.json`.
