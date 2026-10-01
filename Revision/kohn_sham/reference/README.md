# Revision Kohn-Sham reference solver (Python, independent of the Rust solver)

An independent second solver for SPEC section 7 (instantaneous Kohn-Sham states of dirac16complex in the
author's primordial field). It shares no code with the Rust solver (`Revision/kohn_sham/solver`) and uses a
different discretisation. Its only theory input is `Revision/kohn_sham/ks-theory.json`; the functional
coefficients are read from it and checked to be exactly 15/16, -1/16, 15/32 and -1/32. Nothing from the old
stages is used.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} sin^{1/6} z, a4
increasing); x8 = hidden direction, y = ln(sin z)/(6H) in [-L, 0] (brane y = 0, tip cutoff y = -L).

## Run (from the repository root)

```
python Revision/kohn_sham/reference/run_reference.py --timing <scratch>/timing.json            # canonical
python Revision/kohn_sham/reference/run_reference.py --out <scratch>/repeat --report <scratch>/repeat.json   # repeat
```

The run writes `reference/results/` and `reports/ks-reference.json`, and prints every check as
`PASS/FAIL - name: detail` on stderr and `SUCCESS`/`FAILURE` last on stdout (exit 0/1). `--jobs N` (default
min(20, cores - 2)) distributes independent states over processes and does not change any output. The
outputs are deterministic (LF, no timings or paths). The cross-check against Rust is in `../checker/`.

## Method

* **Block equation.** ks-theory.json gives, for chi = (a, i b), the real symmetric operator
  `[[jK + v, j(d_y + M)], [j(-d_y + M), -jK + v]]` on (a, b), with K = e^{-Hy - a4,0} |k|, a regular tip
  b(-L) = 0 (theta = 0), and the ASSUMED Z2 brane: even b(0) = 0, odd a(0) = 0.
* **Rotated frame (exact).** chi = e^{i phi sigma1} psi, psi = (u, i w), turns both parities into the same
  Dirichlet problem w(-L) = w(0) = 0: phi = 0 (even) and phi = j (pi/2)(y + L)/L (odd). The transformed
  operator has the same form, with mass M cos 2phi - K sin 2phi, momentum term M sin 2phi + K cos 2phi and a
  scalar phi'. The choice phi_j = j phi keeps the exact k = 0 symmetry j -> -j as the sign flip w -> -w of the
  discrete problem, so the k = 0 levels of the two block types stay exactly degenerate on every grid.
* **Staggered finite differences.** G cells of width h = L/G; u lives on the half nodes and w on the interior
  nodes. The unknowns (u_1/2, w_1, ..., u_G-1/2) give a real symmetric tridiagonal matrix of size 2G - 1.
  Centred differences and centred averages give second order with an error expansion in even powers of h.
  The staggering avoids the doubling of naive centred Dirac discretisations.
* **Eigenvalues.** Sturm counts and bisection find each level by its index in its sector, so no level can be
  missed. The twisted factorisation then refines the level (Rayleigh-quotient steps) and gives the
  eigenvector. Every level is verified by two Sturm counts. The particle convention of ks-theory.json
  (positive lambda = 0 levels plus the k = 0 brane zero modes, which are exact zero eigenvalues of the
  discrete problem) fixes the lowest particle index of each sector. A level's rank (its index minus that
  offset) equals the Rust label minus label_min.
* **Densities, potentials, integrals.** u and w are averaged onto each other's positions. The proper
  densities n, S, Q, the potentials M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n, e_int and the EMT
  (rho, p3, p_t, p8 as in ks-theory.json emt) are evaluated at all positions. Integrals use the midpoint rule
  on the half nodes. Brane and tip values use a quintic extrapolation of u from the six nearest half nodes.
  Anderson mixing of the potentials runs to max |residual| <= 1e-12 m.
* **Runs per state.** Each state gets the ground state (aufbau, closed shells), the Delta-SCF state (one
  particle from the HOMO group to the LUMO group, uniform over each group), and the four fixed-occupation
  neighbours at a4 +- delta and +- 2 delta (delta = 2e-3). The neighbours give dE/da4 and the self-consistent
  d_a M_eff and d_a v_v, which enter the exact discrete Hellmann-Feynman matrix elements z_n^T (dT/da4) z_m of
  the adiabaticity measure Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 (n occupied, m empty, same sector,
  rank <= 2). Thermal states use the Mermin occupations at T and four neighbours at T(1 +- 0.01),
  T(1 +- 0.02) for C_V = T dS/dT, dE/dT and -dF/dT.
* **Chemical potential.** mu is the root of sum g f = N. It is found by bisection on a well-conditioned
  form of the residual: (exact integer count of the states below mu - N) minus the holes below mu plus the
  particles above mu. The direct form sum g f - N loses about eps_mach N of absolute precision, which fixes mu
  only to eps_mach N / (dN/dmu). Deep in the activated regime (gap >> T) that error reaches ~1e-9 m; see
  History below.
* **Label sets.** The label set comes from the free (lambda = 0) problem at the same slice on the coarsest
  grid. At T = 0 it holds every particle level below max(E_F, LUMO) + 0.25 + 2 sigma, plus ranks 0..2 of every
  sector of an occupied shell. At T > 0 it holds every particle level below mu + T ln(1e13) + 0.2 + 2 sigma.
  Completeness is checked after self-consistency: the lowest excluded level, including the next five shells,
  must lie above the LUMO, or carry an occupation below 2e-13.
* **Richardson extrapolation and uncertainty.** Every quantity is computed on G = 300, 600 and 1200 and
  reported as R = (64 x(1200) - 20 x(600) + x(300))/45, which removes the h^2 and h^4 terms. Its measured
  grid uncertainty is U = |R - (4 x(1200) - x(600))/3| + 2e-12 max(1, |R|): the size of the h^4 term on the
  finest grid, plus a roundoff floor. The report checks the asymptotic ratio
  (x(300) - x(600))/(x(600) - x(1200)) = 4. One state is also solved on G = 2400 to confirm that the
  three-grid value moves by less than U.
* **Re-derived inputs.** N_large and N_mid are re-derived from the free a4,0 = 0 closed shells below the
  bulk edge. lambda_1 and lambda_2 are re-derived as 0.1 m and 0.3 m divided by the coupling strength, rounded
  to 4 significant digits. The strength is max over slices and y of max((15/16)|S|, |n|/16) of the free
  ground states. The reference takes the continuous maximum (quartic interpolation over the nodes), whereas
  the Rust value is a maximum over grid samples; the checker accounts for the difference.

## The representative subset (from the canonical matrix of 75 ground and 135 thermal states)

The subset covers all three particle numbers N = 8, 136, 688, all five coupling tags (0, +-lambda_1,
+-lambda_2), all five slices a4,0 = 0 ... 2 and all three temperatures.

* **Ground states (18):** N8_lam0_a00, N8_lamp1_a10, N8_lamp2_a00, N8_lamm2_a20, N136_lam0_a00, N136_lam0_a20,
  N136_lamp1_a05, N136_lamm1_a15, N136_lamp2_a10, N136_lamp2_a20, N136_lamm2_a20, N688_lam0_a00,
  N688_lam0_a20, N688_lamp1_a15, N688_lamm1_a05, N688_lamp2_a00, N688_lamp2_a20, N688_lamm2_a10. Each comes
  with its Delta-SCF state, four a4 neighbours and the adiabaticity pairs.
* **Thermal states (8):** N8_lam0_a20_T50, N8_lamp1_a10_T20, N8_lamm1_a00_T10, N136_lam0_a15_T50,
  N136_lamp1_a20_T20, N136_lamm1_a05_T10, N688_lam0_a10_T20, N688_lamp1_a20_T50. Each comes with four
  temperature neighbours.
* **Fourth-grid validation:** N136_lamp2_a20, the strongest coupling with the largest tip densities, solved
  on G = 300, 600, 1200, 2400.

## Outputs (`results/`, deterministic: LF, Python float repr, no timings or paths)

| file | content |
| --- | --- |
| `parameters.json` | problem definition, numerics, re-derived N_mid, N_large, couplings (strength per slice, peak position and curvature), subset |
| `free-checks.json` | analytic k = 0 spectra on five grids, zero mode, brane-band slope, particle branch |
| `ground/<id>.json` | per-grid raw scalars and iteration counts; Richardson values with U of the energies, HOMO/LUMO/gap, Delta-SCF, EMT integrals, brane/tip values, dE/da4 (EMT and finite differences), Delta E_x; every level with key (n2, j, parity, rank), eps, U, f; the ten profiles at y = -3 + 0.02 i with U; the 10 largest adiabaticity pairs |
| `thermo/<id>.json` | mu, E, S, F, Omega (two forms), C_V, dE/dT, -dF/dT with U; levels with occupations |
| `validation/N136_lamp2_a20.json` | three-grid values of (300, 600, 1200) vs (600, 1200, 2400) per quantity class |
| `ground-summary.csv`, `thermo-summary.csv` | the main values with their U |
| `manifest.json` | SHA-256 of every file |

## Results (`reports/ks-reference.json`: 28 checks, all PASS)

* **Discretisation.** The analytic k = 0 spectra are reproduced to 2.8e-14 by the three-grid values. Single
  grids give 9.3e-4 (G = 300) down to 1.5e-5 (G = 2400). The error ratio is 4.000 (between 3.99977 and
  4.00019): clean second order. The k = 0 j = +-1 spectra agree exactly. The zero mode is exact (|eps| <=
  1.3e-39, b = 0). The brane-band slope equals ks-theory.json c e^{-a4,0} to 2.6e-15.
* **Re-derived inputs.** The closed shells below the bulk edge 1.292292828069 m are 8, 32, 80, 112, 136, 232,
  328, 376, 496, 592, 688, so N_large = 688 and N_mid = 136. The strengths are 5.138803993 (N = 8, at the
  tip), 107.5483018 (N = 136) and 541.7158538 (N = 688), which give lambda_1 = 0.01946, 0.0009298, 0.0001846
  and lambda_2 = 0.05838, 0.002789, 0.0005538.
* **Per state.** Every check passes: SCF converged on every grid; occupations and HOMO/LUMO groups identical
  on all grids; closed shells; complete label sets; N conserved; the two energy forms agree;
  2 Vol_7 int e^{6Hy} rho = E_KS; y-conservation; dE/da4 (finite differences) equals the EMT form; the
  discrete Hellmann-Feynman identity holds to 5.5e-11 m; Delta-SCF equals the gap at lambda = 0; the
  asymptotic ratio is within 7.4e-5 of 4. The thermal identities also hold (Omega in two forms,
  C_V = dE/dT, -dF/dT = S).
* **Uncertainty validated.** On G = 2400 the three-grid value moves by at most 0.79 of the stated U, in
  every element of 19 quantity classes. The largest U are at the tip (p8 there: U = 1.0e-7, against
  |p8| ~ 1e3). Energies and levels carry U of 1e-12 to 3e-9 absolute.
* **Examples (Richardson value, U).** E_KS(N136_lamp2_a20) = 12.44899948125322 (4.6e-11);
  E_KS(N688_lam0_a00) = 680.4412465815219 (3.3e-9); Delta-SCF(N8_lamp2_a00) = 0.4312928642917516 (2.6e-12);
  Q_max(N688_lam0_a00) = 0.09345059173142507.

## Timings (this machine, 20 processes)

The run takes 226.8 s in total; the repeat takes 223.6 s and is byte-identical in all 32 files and in the
report.

* The parameter derivation takes 18.8 s.
* Ground states take 2.6 s (N8_lam0_a00) to 62.9 s (N688_lamp2_a20).
* Thermal states take 7.0 s to 198.2 s (N688_lamp1_a20_T50, 2000 levels).
* The four-grid validation takes 29.3 s.

## History

The first complete run computed mu by bisection on the direct sum g f - N. The cross-check
(`../checker`) then found that in N8_lamm1_a00_T10 this mu differed by 1.15e-9 from the 40-digit root on
its own levels. That error was far above its stated U (3.2e-11): the direct sum fixes mu only to
eps_mach N / (dN/dmu), and here dN/dmu = 1.2e-6 (gap/T = 43). The reference now uses the well-conditioned
residual above. Its mu agrees with the 40-digit root to 0 (that state) or at most 1.1e-16 (the others).

## What this does not establish

The reference tests the Rust solver's numerics, not the physics model. Both solvers implement the same
ks-theory.json functional, the same ASSUMED Z2 brane, the same tip cutoff L = 3 and the same filling
CONVENTION. An error in those inputs would be common to both and could not be detected here. The states are
instantaneous (adiabatic) Kohn-Sham states; the non-adiabatic problem is OPEN.
