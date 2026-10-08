# Revision Kohn-Sham reference solver (Python, independent of the Rust solver)

An independent second solver for SPEC section 7 (instantaneous Kohn-Sham states of dirac16complex in the
author's primordial field). It shares no code with the Rust solver (`Revision/kohn_sham/solver`) and uses a
different discretisation. Its only theory input is `Revision/kohn_sham/ks-theory.json`; the functional
coefficients are read from it and checked to be exactly 15/16, -1/16, 15/32 and -1/32 (and 1/32, 1/16 for the
exact-Fock variant). Nothing from the old stages is used.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} sin^{1/6} z, a4
increasing); x8 = hidden direction, y = ln(sin z)/(6H) in [-L, 0] (brane y = 0, tip cutoff y = -L).

## Run (from the repository root)

```
python Revision/kohn_sham/reference/run_reference.py --jobs 22 --timing <scratch>/timing.json   # canonical
```

The run writes `reference/results/` (a fresh directory: a former output directory is replaced) and
`reports/ks-reference.json`, and prints every check as `PASS/FAIL - name: detail` on stderr and
`SUCCESS`/`FAILURE` last on stdout (exit 0/1). `--jobs N` (default min(20, cores - 2)) distributes the 333
independent jobs over processes, longest first, and does not change any output. The outputs are deterministic
(LF, no timings or paths). The repeat run that tests this is made by the cross-checker itself (`../checker/`,
check `reference_repeat_byte_identical`), which also compares the reference with the Rust solver.

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
* **Exact-Fock-exchange variant (lambda != 0).** ks-theory.json exchange.exactFockSlab gives the exact Fock
  exchange of the closed-shell slab determinant as -(lambda/32)(n^2 + S^2 - Q^2). The variant therefore adds
  lambda Q^2/32 to e_int and w_Q = lambda Q/16 sigma3 (both block types) to h. The coefficients are read from
  the theory file and checked (w_Q = d e_int/dQ; the n^2 and S^2 coefficients equal the uniform-gas ones). In
  the real form, w_Q enters as K -> K + j w_Q. The SCF mixes (dM, v_v, w_Q) and starts from the converged
  uniform-gas state, as the Rust matrix does. p8 gets -w_Q Q, and the report checks y-conservation,
  2 Vol_7 int e^{6Hy} rho = E_KS and the two energy forms for the variant.
* **Rescaling partners (a4,0 > 0).** The problem KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}, lambda) is solved
  independently: its own label set, three grids, Richardson. The report compares it with the state at a4,0 (the
  identity of ks-theory.json rescalingIdentity).
* **Particle-hole lists.** The lowest 48 excitations between degenerate groups. Hole groups hold particles.
  Particle groups lie above the hole group and below the lowest level outside the label set, and have
  vacancies. The groups come from the finest grid; the energies and the cut are Richardson values. Each row
  has delta_eps with U, the multiplicity (holes x vacancies) and a same-sector flag.
* **Sea-hole diagnostic (thermal).** For every shell n2 >= 1 of the thermal label set and five more shells,
  the highest sea level of the j = -1 even sector (Sturm index one below the lowest particle level, rank -1;
  the sea brane band) is computed in the converged potentials. The diagnostic reports 4 r3 f((mu - eps)/T) per
  shell and cumulatively: the thermal holes that the excluded sea would carry under the filling CONVENTION.
* **Crossing demonstration.** N_demo is re-derived as the smallest closed shell N > 8 of the free a4,0 = 0
  aufbau (levels up to 1.6 m) whose last group holds a level off the even j = +1 brane band. At each slice,
  for lambda = 0, the run computes the instantaneous aufbau state (open shells filled uniformly) and the
  adiabatically continued state with the a4,0 = 0 occupation by label. The label set is extended by those
  labels where needed.

## The full canonical matrix (all of it)

* **Ground states (75):** N in {8, N_mid, N_large} = {8, 136, 688} x 5 coupling tags (0, +-lambda_1,
  +-lambda_2) x 5 slices a4,0 = 0, 0.5, 1, 1.5, 2. Each comes with its Delta-SCF state, four a4 neighbours,
  the adiabaticity pairs and the particle-hole list.
* **Exact-Fock variant (60):** every ground state with lambda != 0.
* **Rescaling partners (60):** every ground state with a4,0 > 0.
* **Crossing demonstration:** lambda = 0, N_demo = 696, the five slices.
* **Thermal states (135):** N in {8, 136, 688} x lambda in {0, +-lambda_1} x 5 slices x T in {0.01, 0.02,
  0.05} m. Each comes with four temperature neighbours and the sea-hole diagnostic.
* **Fourth-grid validation:** N136_lamp2_a20, the strongest coupling with the largest tip densities, solved
  on G = 300, 600, 1200, 2400.

## Outputs (`results/`, deterministic: LF, Python float repr, no timings or paths)

| file | content |
| --- | --- |
| `parameters.json` | problem definition, numerics, re-derived N_mid, N_large, couplings (strength per slice, peak position and curvature), N_demo and its closed shells, the matrix (all ids) |
| `free-checks.json` | analytic k = 0 spectra on five grids, zero mode, brane-band slope, particle branch |
| `ground/<id>.json` (75) | per-grid raw scalars and iteration counts; Richardson values with U of the energies, HOMO/LUMO/gap, Delta-SCF, EMT integrals, brane/tip values, dE/da4 (EMT and finite differences), Delta E_x, the lowest excluded level; every level with key (n2, j, parity, rank), eps, U, f; the ten profiles at y = -3 + 0.02 i with U; the 10 largest adiabaticity pairs; the particle-hole list (48 rows) |
| `exx/<id>.json` (60) | exact-Fock variant per grid and Richardson: E_exact_fock_scf, E_uniform_gas, Delta E_x, E_exx - (E_uniform_gas + Delta E_x), HOMO/LUMO/gap, EMT and y-conservation integrals, residuals, occupations equal to the uniform-gas ones |
| `rescaling/<id>.json` (60) | rescaling partner: dk, v_t, E_KS with U, every level with U, occupations, five profiles |
| `crossing/crossing-demo.json` | N_demo, the a4,0 = 0 occupation, per slice: aufbau and continued energies with U, open shell, labels left and entered |
| `thermo/<id>.json` (135) | mu, E, S, F, Omega (two forms), C_V, dE/dT, -dF/dT with U; levels with occupations; sea holes per shell and cumulative with U |
| `validation/N136_lamp2_a20.json` | three-grid values of (300, 600, 1200) vs (600, 1200, 2400) per quantity class |
| `ground-summary.csv`, `thermo-summary.csv`, `exx-summary.csv`, `rescaling-summary.csv`, `crossing-demo.csv` | the main values with their U |
| `manifest.json` | SHA-256 of every file (339 files) |

## Results (`reports/ks-reference.json`: 37 checks, all PASS)

* **Discretisation.** The analytic k = 0 spectra are reproduced to 2.8e-14 by the three-grid values. Single
  grids give 9.3e-4 (G = 300) down to 1.5e-5 (G = 2400). The error ratio is 4.000 (between 3.99977 and
  4.00019): clean second order. The k = 0 j = +-1 spectra agree exactly. The zero mode is exact (|eps| <=
  1.3e-39, b = 0). The brane-band slope equals ks-theory.json c e^{-a4,0} to 2.6e-15.
* **Re-derived inputs.** The closed shells below the bulk edge 1.292292828069 m are 8, 32, 80, 112, 136, 232,
  328, 376, 496, 592, 688, so N_large = 688 and N_mid = 136. The strengths are 5.138803993 (N = 8, at the
  tip), 107.5483018 (N = 136) and 541.7158538 (N = 688), which give lambda_1 = 0.01946, 0.0009298, 0.0001846
  and lambda_2 = 0.05838, 0.002789, 0.0005538.
* **Every ground state (75).** Every check passes. SCF converged on every grid (residual <= 1.0e-12 m).
  Occupations and HOMO/LUMO groups are identical on all grids; shells are closed; label sets are complete; N
  is conserved; the two energy forms agree. 2 Vol_7 int e^{6Hy} rho = E_KS holds to 4.1e-5 of the allowance;
  y-conservation to 3.6e-4 of it. dE/da4 from finite differences equals the EMT form (worst 0.024 of the
  allowance). The discrete Hellmann-Feynman identity holds to 5.8e-11 m. Delta-SCF equals the gap at
  lambda = 0 to 8.9e-14 m. The asymptotic ratio is within 7.4e-5 of 4. The lowest particle-hole excitation
  is HOMO group -> LUMO group at the KS gap in every state.
* **Exact-Fock variant (60).** Converged on every grid (residual <= 6.1e-13 m), with the uniform-gas
  occupations. N is conserved, the two energy forms agree, and 2 Vol_7 int e^{6Hy} rho = E_KS holds. The
  y-conservation with the derived -w_Q Q term in p8 holds to 3.1e-4 of the allowance. Examples: for N = 8 the
  exact Fock exchange cancels the uniform-gas interaction energy (E_EXX = 2.5e-17 against
  E_uniform_gas = -0.002862652173735 for lambda_2, a4,0 = 0). For N688_lamp2_a20: E_EXX = 110.6531060797778
  (U 4.8e-10), E_uniform_gas = 110.5777627893853, Delta E_x = 0.07682582877714, and
  E_EXX - (E_uniform_gas + Delta E_x) = -0.001482538384567.
* **Rescaling partners (60).** The independently solved partner reproduces the state at a4,0, with the same
  label set and occupations, to 4.2e-14 (levels in m, E_KS and profiles relative). Example: N688_lamp2_a20,
  partner dk = 0.03383382080915318, v_t = 0.002478752176666359, E_KS = 110.5777627893853.
* **Crossing demonstration.** N_demo = 696 on every grid (the k = 0 odd bulk levels 0:+-1:odd:0 complete
  that shell). From a4,0 = 0.5 on, the aufbau empties them and fills the n2 = 12 brane-band shell; that state
  is an open shell. The adiabatically continued state lies 3.656690187, 6.052645255, 7.611826821 and
  8.623383504 m above the aufbau state at a4,0 = 0.5, 1, 1.5, 2.
* **Every thermal state (135).** The thermal identities hold: Omega in two forms, and C_V = dE/dT and
  -dF/dT = S (worst 8.1e-3 of the allowance). The window cut carries f <= 6.7e-16. Sea-hole diagnostic: the
  five shells beyond the label set add at most 6.4e-13 of the total. The excluded sea would carry more than
  1% of N in 15 of the 135 states. The largest are N8_lamm1_a20_T50 (30.98 N), N8_lam0_a20_T50 (30.80 N:
  246.4351774641 holes, U 2.6e-9, at mu = -0.09766539473) and N8_lamp1_a20_T50 (30.62 N). There the
  particle-only Mermin ensemble is outside its range of validity (a DIAGNOSTIC of the CONVENTION, not a
  validation).
* **Uncertainty validated.** On G = 2400 the three-grid value moves by at most 0.79 of the stated U, in
  every element of 19 quantity classes. The largest U are at the tip (p8 there: U = 1.0e-7, against
  |p8| ~ 1e3). Energies and levels carry U of 1e-12 to 3e-9 absolute.
* **Examples (Richardson value, U).** E_KS(N136_lamp2_a20) = 12.44899948125322 (4.6e-11);
  E_KS(N688_lam0_a00) = 680.4412465815219 (3.3e-9); Delta-SCF(N8_lamp2_a00) = 0.4312928642917516 (2.6e-12);
  Q_max(N688_lam0_a00) = 0.09345059173142507.

## Timings (this machine, 24 cores, `--jobs 22`)

The canonical run takes 578.3 s of wall time for 333 jobs (12076 CPU-seconds in the jobs). The cross-checker's
repeat run is byte-identical in all 340 files and in the report (see `../checker/README.md`). On 2026-10-08 the
cross-checker repeated the run twice more, while other workflows shared the machine: 692.9 s and 748.0 s, again
byte-identical. Per kind (CPU time of the jobs, under full load, 2026-10-01):

* The parameter derivation (serial, before the pool) takes 17.0 s.
* 135 thermal states: 8863 s in all, from 3.3 s (N8_lam0_a00_T10) to 559.3 s (N688_lamp1_a20_T50: 2000 levels
  on three grids, each with four temperature neighbours). This single job sets the wall time.
* 75 ground states: 1971 s, from 2.9 s to 132.7 s (N688_lamp2_a20).
* 60 exact-Fock variants: 728 s, at most 44.8 s. 60 rescaling partners: 426 s, at most 27.5 s.
* The four-grid validation takes 40.9 s, the crossing demonstration 21.2 s and the free checks 8.8 s.

## History

The first version solved a representative subset of the canonical matrix (18 of 75 ground states, 8 of 135
thermal states; 28 checks, 226.8 s). It was extended to the full matrix with the exact-Fock variant, the
rescaling partners, the particle-hole lists, the sea-hole diagnostic and the crossing demonstration. Before
that, the subset run had found the Mermin rounding error described next.

The first complete run computed mu by bisection on the direct sum g f - N. The cross-check
(`../checker`) then found that in N8_lamm1_a00_T10 this mu differed by 1.15e-9 from the 40-digit root on
its own levels. That error was far above its stated U (3.2e-11): the direct sum fixes mu only to
eps_mach N / (dN/dmu), and here dN/dmu = 1.2e-6 (gap/T = 43). The reference now uses the well-conditioned
residual above. On the full matrix its mu agrees with the 40-digit root on its own levels to at most
1.3e-15 m (checker check `thermo_mu_rounding_diagnostic`).

## What this does not establish

The reference tests the Rust solver's numerics, not the physics model. Both solvers implement the same
ks-theory.json functional, the same ASSUMED Z2 brane, the same tip cutoff L = 3 and the same filling
CONVENTION. An error in those inputs would be common to both and could not be detected here. The states are
instantaneous (adiabatic) Kohn-Sham states; the non-adiabatic problem is OPEN. The exact-Fock variant is a
variant of the functional, not the canonical model. The sea-hole numbers are a DIAGNOSTIC of the filling
convention. They show where the particle-only ensemble is outside its range of validity (15 thermal states).
They do not justify the convention, whose justification stays OPEN. The crossing
demonstration is a lambda = 0 illustration with N_demo = 696, outside the canonical N.
