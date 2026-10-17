# field_equations_a4/ks_source: the field equations for a4 and b4 with the Kohn-Sham source (SPEC sections 5 and 7)

Revision code only. The metric is the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md`
section 1): diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real, b4 a function
of x4. The analysis was rewritten for it on 2026-10-16/17 (`HANDOFF.md` 0.10, phase W5).
Inputs (read-only): `Revision/field_equations_a4/a4-equations.json` (the Einstein-Lovelock equations for a4[x4] and
b4[x4] in the corrected metric, key generalSource, and exponentialHistory.authorWeights), the Kohn-Sham results of
`Revision/kohn_sham` (`results/parameters.json`, `results/ground/profiles/*.csv`, `results/ground/emt-integrals.csv`,
`results/ground/levels/*.csv`, `results/adiabatic/adiabaticity.csv`, `results/adiabatic/history.json`,
`ks-theory.json`), the source-condition report `Revision/field_equations_a4/reports/ks-source-conditions.json`, and the
dense history of the same record (`Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv`, 15 series x 41 slices a4,0 = 0, 0.05, ..., 2 with fixed occupations). The
report records the sha256 digest of every input.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three
extra times, which DEFLATE EXPONENTIALLY when a4 increases (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); x0 = the
hidden direction (Kohn-Sham coordinate y = ln|sin z|/(6H), sqrt|g| d^8x = e^{-a4} b4^2 e^{3Hy} dy d^3x dx4 d^3x_t).
u = b4'/b4, v = u', kk = e^{2a4}/b4, h4 = u/2 - a4'.

| file | role |
| --- | --- |
| `ks_source_a4.py` | the analysis (sympy for the exact identities, plain Python floats for the numerics); writes the four outputs below; exit code 0 iff every check passes |
| `test_ks_source_a4.py` | unit tests, the reproducibility of the committed outputs, and two negative controls (tampered Kohn-Sham inputs must fail) |
| `results/ks-source-moments.csv` | per Kohn-Sham state: hidden-direction averages rho_bar, p3_bar, p_t_bar, p0_bar, n_bar (per proper cell volume), the integral and conservation residuals, the mismatch measures mu1 and the p0 = p_t defects |
| `results/ks-source-a4-cases.csv` | per integration case (2 free series x (the author's weights + 3 theories x 6 values of sigma0)): Lambda, sigma0, outcome, the end point and (a4, b4, a4', u) at the output times, the constraint residual, the outcome at the second step size |
| `reports/ks-source-a4.json` | every check (name, verdict, detail), the assumptions, the conclusions |
| `reports/ks-source-a4-summary.md` | the results in words and tables, generated from the same run |

Run from the repository root (after `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`, whose dense history
is an input):

```text
python Revision/field_equations_a4/ks_source/ks_source_a4.py
python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
```

Two runs of the script give byte-identical outputs (LF). The script takes about 4.4 s and the tests about 20 s (2026-10-17, 22 cores).

## What is computed (all numbers in the report and the summary; 19 checks)

* **Exact (A, sympy, from a4-equations.json).** The hidden and the extra-time components of the left-hand side are
  one and the same expression, so a source needs p0 = p_t; the off-diagonal components vanish identically, so it needs
  T^x4_x0 = 0; the left-hand sides are free of x0, so every component of the source must be independent of x0 (A1).
  The x4 component is a first-order constraint and the x1 and x0 components are linear in (a4'', v) with the recorded
  Jacobian (A2); the constraint propagates (the x4 component of the Bianchi identity, d4 E^4_4 = 3 a4' (E^1_1 - E^4_4)
  + 4 h4 (E^0_0 - E^4_4), A3); the x0 conservation identity in the Kohn-Sham coordinate is p0_y + 3 H (p0 - p_t) = 0
  (A4); the x0-averaged free fold-band gas (rho ~ b4^{-2}, p3 = rho/3, p0 = p_t = 0) satisfies the energy exchange
  identically, for every a4 and b4 (A5); the history source of the record (exponentialHistory.authorWeights) is
  reproduced from the general components (A6).
* **The computed profiles (B).** The integrals of the recorded profiles reproduce `emt-integrals.csv` (B1); every
  profile satisfies the x0 conservation identity (B2): the recorded states CONSERVE energy-momentum along x0; the
  mismatch with an x0-independent source (the L1 measure mu1 with the volume weight e^{3Hy}) is O(1) for every state
  (B3); the numbers of `../reports/ks-source-conditions.json` are re-derived independently from the same files and
  agree (B0).
* **Hidden-direction moments along the record's history (C).** Averaged over x0, p0 = p_t holds to rounding for the
  free states (both vanish) and fails for every interacting state (C1); the energy relation dE/da4 = -3 P3 + P_t + P0/3
  (beta = 4/3) holds along the dense history of every series (C2); the record's history needs a source that no
  constant kappa makes of the free gas (C3); the signs of the averaged source (C4).
* **Integration (D, an APPROXIMATION, stated).** The x0-averaged equations (the x4 constraint and the x1 and x0
  components, a second-order system in x4) with the x0-averaged free fold-band gas as the source. That average is
  exact for every (a4, b4) while the gas stays on the fold band (D0): every occupied orbital is (e^{f M y}, 0) with
  eps = e^{-a4} |k|, so kappa rho_bar = sigma0 (b4/b4(0))^{-2}, kappa p3_bar = kappa rho_bar/3, p0_bar = p_t_bar = 0. The
  system is started on the record's history (a4'(0) = H, u(0) = (4/3) H, b4(0) = 1) and integrated in x4 with RK4 at
  the two base steps h = 1e-3/H and 2e-3/H, every step covered by substeps h 2^-l with step-doubling error control (local
  error 1e-12 relative to max(1, |y|)), so the solutions stay resolved where they steepen before an event (D1); the
  constraint is kept by the Bianchi identity (D3); for the author's weights (Lambda = -10, the constraint fixes sigma0;
  D2) and for Einstein, Gauss-Bonnet and cubic Lovelock with six values of sigma0 (Lambda from the constraint). The
  outcomes are classified (D4): regular (through x4 = 2/H), a4_turns (a4' reaches 0), leaves_fold_band (the Fermi level
  e^{-a4} k_F reaches the bulk edge, which depends on f), singular_second_order_system (det J changes sign, or falls to
  1e-6 of its start value: a4'' ~ 1/det J), runaway (|a4'| or |u| > 1e3 H), step_underflow (a substep below h 2^-40
  would be needed; not reached).

## Results (this run, 19/19 checks pass; every number from `reports/ks-source-a4.json`)

* **A (exact).** A1 to A6 hold identically: p0 = p_t, T^x4_x0 = 0 and x0-independence are necessary for a source; the
  x4 component is a constraint that propagates; the free fold-band gas conserves energy for every (a4, b4); the
  record's history source is reproduced.
* **B (the computed profiles).** The 75 recorded integrals are reproduced to 1.54655e-08
  (B1); the x0 conservation identity holds on all 70 nonzero profiles to 1.21233e-05
  of the largest term (B2); the mismatch with an x0-independent source is O(1): mu1_rho in
  [0.147738, 0.738255] (B3); the
  source-condition report is confirmed (B0).
* **C (moments along the history).** Averaged over x0, p0 = p_t holds for the 10 free states with a nonzero tensor and
  fails for all 60 interacting states (relative defect at least 0.00613418, C1); the energy relation
  dE/da4 = -3 P3 + P_t + P0/3 holds along the dense history to 4.27528e-09 (300 intervals, C2). With the
  author's weights the record's history needs kappa rho = 3.57407 at a4 = 0 and
  -7.63383 at a4 = 2 (a sign change between a4 = 0.75 and 0.8), while the free gas has rho_bar > 0
  at every slice: kappa would have to run from 16.5276 to
  -7311.81 (C3). The gas of N = 592 and 2352 has rho_bar > 0 and rho_bar + p3_bar > 0; the
  N = 8 states (only k = 0 levels, p3 = e_int) have rho_bar with the sign of -lambda and p3_bar/rho_bar in
  [0.949561, 0.998955], so the averaged null energy condition along 3-space is violated in the 10
  states with lambda > 0 (C4).
* **D (integration, an APPROXIMATION).** The averaged free gas is exact to 2.88658e-15 (D0;
  C = 0.034125, 0.216249 for N = 592, 2352). The two base steps agree to
  1.60994e-11 (D1) and the constraint is kept to 8.85098e-11 (D3). With the author's weights the constraint
  fixes sigma0 = kappa rho_bar(0) = 3.57407 (kappa > 0); the solution then departs from the record's history
  and reaches the singular surface det J = 0 of the second-order system at x4 = 0.428813/H (a4 = 0.3616,
  b4 = 0.8626, a4'/H = 0.9784, u/H = -2.602: b4 already decreasing), before x4 = 0.5/H (D2).
  The 38 cases (the two free series give identical cases: sigma0 fixes the source and the Fermi level never
  reaches the bulk edge) end as: a4_turns 24, regular 6, runaway 4, singular_second_order_system 4 (D4). Series N2352_lam0:

| gravity | case | Lambda/H^2 | outcome | x4 reached (1/H) | a4 there | b4 there | a4'/H there | u/H there |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| einstein | sigma0 = -10 | 3.66667 | regular | 2 | 0.659 | 39.59 | 0.3727 | 1.759 |
| einstein | sigma0 = -1 | -5.33333 | a4_turns | 0.384 | 0.1711 | 1.371 | -0.0004885 | 0.4447 |
| einstein | sigma0 = -1/10 | -6.23333 | a4_turns | 0.378 | 0.1707 | 1.318 | -7.226e-06 | 0.2736 |
| einstein | sigma0 = 1/10 | -6.43333 | a4_turns | 0.378 | 0.1706 | 1.307 | -0.002064 | 0.2322 |
| einstein | sigma0 = 1 | -7.33333 | a4_turns | 0.374 | 0.1707 | 1.259 | -6.554e-05 | 0.05132 |
| einstein | sigma0 = 10 | -16.3333 | runaway | 0.584205 | 1.614 | 0.05599 | 705.8 | -1000 |
| egb | sigma0 = -10 | 3.51852 | regular | 2 | 0.5604 | 33.34 | 0.3542 | 1.694 |
| egb | sigma0 = -1 | -5.48148 | a4_turns | 0.353 | 0.1573 | 1.293 | -0.001747 | 0.2757 |
| egb | sigma0 = -1/10 | -6.38148 | a4_turns | 0.358 | 0.162 | 1.25 | -0.0003783 | 0.07164 |
| egb | sigma0 = 1/10 | -6.58148 | a4_turns | 0.36 | 0.1632 | 1.24 | -0.001109 | 0.02187 |
| egb | sigma0 = 1 | -7.48148 | a4_turns | 0.37 | 0.1692 | 1.193 | -0.001397 | -0.218 |
| egb | sigma0 = 10 | -16.4815 | runaway | 0.613258 | 0.6866 | 0.000418 | 51.72 | -1002 |
| lovelock3 | sigma0 = -10 | 3.59852 | regular | 2 | 0.5651 | 34.13 | 0.3595 | 1.708 |
| lovelock3 | sigma0 = -1 | -5.40148 | a4_turns | 0.344 | 0.1532 | 1.293 | -5.525e-05 | 0.3102 |
| lovelock3 | sigma0 = -1/10 | -6.30148 | a4_turns | 0.349 | 0.1576 | 1.253 | -0.0001809 | 0.1118 |
| lovelock3 | sigma0 = 1/10 | -6.50148 | a4_turns | 0.351 | 0.1587 | 1.244 | -0.001351 | 0.06347 |
| lovelock3 | sigma0 = 1 | -7.40148 | a4_turns | 0.36 | 0.1642 | 1.2 | -0.001736 | -0.166 |
| lovelock3 | sigma0 = 10 | -16.4015 | singular_second_order_system | 0.349611 | 0.269 | 0.7629 | 1.177 | -3.507 |
| author | Lambda = -10 | -10 | singular_second_order_system | 0.428813 | 0.3616 | 0.8626 | 0.9784 | -2.602 |

So none of the stated gravity theories, with the averaged free gas as its source, follows the record's history:
3-space stops expanding (a4_turns) for |sigma0| <= 1 at x4 = 0.344 to 0.384/H, the system becomes singular or runs
away for sigma0 = 10 and for the author's weights, and only sigma0 = -10 (a negative kappa rho_bar, i.e. kappa < 0 for
the positive rho_bar of the gas) reaches x4 = 2/H, with a4'/H in [0.354, 0.373] and u/H in [1.69, 1.76] there
instead of (1, 4/3).

## History

Until 2026-10-16 this folder analysed the metric of 2026-10-14 (b4 only in the extra-time components) and before that
the metric b4 = 1 (23 and 22 checks; their texts are in the git history of this file). In that metric the off-diagonal
equation kappa q40 = cot z u Q(a4', u) forced Q = 0 for every history with b4 not constant, and the Kohn-Sham source had
the weight e^{6Hy}. In the corrected metric every off-diagonal component of the left-hand side vanishes identically,
the hidden and the extra-time components coincide (the source needs p0 = p_t), and the x0-averaged equations form a
second-order system in x4 with a first-order constraint; the free gas is an exact fold-band gas. The analysis was
rewritten accordingly (A1 to A6, B0 to B3, C1 to C4, D0 to D4). Two claims of the first rewrite were wrong and were
corrected before any commit (`claude_failures.md` H10): the N = 8 states have rho_bar with the sign of -lambda (not of
lambda) and p3_bar/rho_bar between 0 and 1 (not -1). The first run on the new dense history failed D3 with fixed RK4
steps (residual 1.2e-2 in the runaway cases, 4e-6 at det J -> 0): the solutions were not resolved where they steepen
before their events; the integration now uses step-doubling substeps and detects the singular surface at 1e-6 of
det J(0) (`claude_failures.md` H13; the criterion of D3 is unchanged).
