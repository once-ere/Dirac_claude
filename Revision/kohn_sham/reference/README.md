# Revision Kohn-Sham reference solver (Python, independent of the Rust solver)

An independent second solver for SPEC section 7 (instantaneous Kohn-Sham states of dirac16complex in the
author's primordial field). It shares no code with the Rust solver (`Revision/kohn_sham/solver`) and uses a
different discretisation. Its only theory input is `Revision/kohn_sham/ks-theory.json`; the functional
coefficients are read from it and checked to be exactly 15/16, -1/16, 15/32 and -1/32 (and 1/32, 1/16 for the
exact-Fock variant). Nothing from the old stages is used.

The metric is the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1,
ks-theory.json geometry): diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0
real, on the history a4 = H x4, b4 = b4(0) e^{beta a4}, b4(0) = 1, beta = 4/3 (read from ks-theory.json
`adiabaticity.historyBeta`). In the hidden coordinate y = ln|sin z|/(6H) <= 0 the metric reads
ds^2 = e^{2a4} dx_{1..3}^2 - dx4^2 + f^2 [dy^2 - e^{2Hy} dx_{5..7}^2] with the hidden scale f = e^{-a4} b4^{1/2}
(= e^{-a4/3} on the history). The densities are per Vol_7(a4,0) = ell^3 v_t e^{(2 beta - 1) a4,0} with the factor
e^{-3Hy}, and the coupling is lambda_hat = lambda b4(0)^{-2} (ks-theory.json densities). The record was moved to
this metric on 2026-10-16/17 (section "The corrected metric" below).

The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction (z = 6 H x0; the fold cos z = 0 is y = 0, the tip
cutoff y = -L); x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the three EXTRA TIMES, which
DEFLATE EXPONENTIALLY (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}). p0 = T^x0_x0 is the hidden-direction pressure.

## Run (from the repository root)

```
python Revision/kohn_sham/reference/run_reference.py --jobs 20 --timing <scratch>/timing.json   # one run (about 30 min: longer than the limit)
```

In parts, each within a time limit (the way the record was made; no single calculation may take longer than 423 s):

```
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache --stage 1 --part i/6 --jobs 20   # i = 1..6
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache --stage 2 --part i/6 --jobs 20   # i = 1..6
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/cache --jobs 20                       # writes the outputs
```

The jobs are split into two stages. Stage 1 holds every job except the temperature neighbours of the thermal states
(603 jobs: the free checks, the 75 ground states with their Delta-SCF states and a4 neighbours, the 60 exact-Fock
variants, the 60 rescaling partners, the crossing demonstration, the validation state, and the main state of every
thermal state on each grid, 405); stage 2 holds the temperature neighbours T(1 +- 0.01),
T(1 +- 0.02) of every thermal state on each grid (1620 jobs), which start from the stage-1 states. `--stage s
--part i/n` computes a fixed part of the jobs of stage s (sorted by `cost_estimate`, longest first, each given to the
part with the smallest total so far), saves every finished job in the cache (one pickle per job) and writes no
outputs. The run without `--part` computes any job still missing and writes the outputs. The cache is tied to the
SHA-256 of `ks-theory.json`, `run_reference.py` and `ks_fd.py` and to the Python and numpy versions
(`cache-identity.json`); a cache made with other inputs is refused. The outputs do not depend on how the jobs are
distributed: every job is a pure function of its inputs (single-threaded BLAS), and the results are written in a
fixed order.

The run writes `reference/results/` (a fresh directory: a former output directory is replaced) and
`reports/ks-reference.json`, and prints every check as `PASS/FAIL - name: detail` on stderr and
`SUCCESS`/`FAILURE` last on stdout (exit 0/1). `--jobs N` (default min(20, cores - 2)) distributes the jobs over
processes, longest first, and does not change any output. The outputs are deterministic (LF, no timings or paths).
The repeat run that tests this is made by the cross-checker itself (`../checker/`, check
`reference_repeat_byte_identical`), which also compares the reference with the Rust solver.

## Method

* **Block equation.** ks-theory.json gives, for chi = (a, i b), the real symmetric operator
  `[[jK + v, j((1/f) d_y + M)], [j(-(1/f) d_y + M), -jK + v]]` on (a, b), with K = kappa |k|, kappa = e^{-a4,0}
  (constant in y: nothing suppresses an orbital toward the tip), the hidden scale f = e^{-a4,0/3}, a regular tip
  b(-L) = 0 (theta = 0), and the fold conditions: the fold y = 0 joins the two halves of a cell, and both conditions
  even b(0) = 0 and odd a(0) = 0 are filled (an ASSUMED convention, ks-theory.json boundaryConditions.fold).
* **Rotated frame (exact).** chi = e^{i phi sigma1} psi, psi = (u, i w), turns both parities into the same
  Dirichlet problem w(-L) = w(0) = 0: phi = 0 (even) and phi = j (pi/2)(y + L)/L (odd). The transformed
  operator has the same form, with mass M cos 2phi - K sin 2phi, momentum term M sin 2phi + K cos 2phi and a
  scalar phi'/f. The choice phi_j = j phi keeps the exact k = 0 symmetry j -> -j as the sign flip w -> -w of the
  discrete problem, so the k = 0 levels of the two block types stay exactly degenerate on every grid.
* **Staggered finite differences.** G cells of width h = L/G; u lives on the half nodes and w on the interior
  nodes. The unknowns (u_1/2, w_1, ..., u_G-1/2) give a real symmetric tridiagonal matrix of size 2G - 1.
  Centred differences and centred averages give second order with an error expansion in even powers of h.
  The staggering avoids the doubling of naive centred Dirac discretisations.
* **Eigenvalues.** Sturm counts and bisection find each level by its index in its sector, so no level can be
  missed. The twisted factorisation then refines the level (Rayleigh-quotient steps) and gives the
  eigenvector. Every level is verified by two Sturm counts. The particle convention of ks-theory.json
  (positive lambda = 0 levels plus the k = 0 fold zero modes, which are exact zero eigenvalues of the
  discrete problem) fixes the lowest particle index of each sector. A level's rank (its index minus that
  offset) equals the Rust label minus label_min.
* **Densities, potentials, integrals.** u and w are averaged onto each other's positions. The proper
  densities (P = e^{-3Hy}/Vol_7) n, S, Q, the potentials M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n,
  e_int and the EMT (rho, p3, p_t, p0 as in ks-theory.json emt) are evaluated at all positions. Integrals are
  2 Vol_7 int e^{3Hy} X dy by the midpoint rule on the half nodes. Fold and tip values use a quintic extrapolation of
  u from the six nearest half nodes. Anderson mixing of the potentials runs to max |residual| <= 1e-14 m for every
  state (`ks_fd.SCF_TOL`; before 1e-12 m: the SCF stopping error enters E_band - E_int and p0 at first order, because
  they use the output densities with the levels of the input potential, and it is not part of the Richardson
  uncertainty, being nearly the same on the three grids; at 1e-12 m it reached 4e-11 in int_p0 of N = 2352,
  `claude_failures.md` H15).
* **Runs per state.** Each state gets the ground state (aufbau, closed shells), the Delta-SCF state (one
  particle from the HOMO group to the LUMO group, uniform over each group), and the four fixed-occupation
  neighbours at a4 +- delta and +- 2 delta (delta = 2e-3), solved to the SCF tolerance 1e-14 m (their energies enter
  the finite difference with weights of about 1.5/delta, so the former tolerance 1e-12 m put a noise of ~1e-9 into
  dE/da4, above the Richardson uncertainty of the strongest couplings; `claude_failures.md` H12, check
  `ground_a4_neighbours_tight`). The neighbours give dE/da4, compared with the history
  identity dE/da4 = -3 P3 + P_t + P0/3 (beta = 4/3; ks-theory.json emt.energyChange), and the self-consistent
  d_a M_eff and d_a v_v, which enter the exact discrete Hellmann-Feynman matrix elements z_n^T (dT/da4) z_m of
  the adiabaticity measure Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 (n occupied, m empty, same sector,
  rank <= 2); d_a h contains the kinetic term (1 - beta/2) (1/f) d_y of the hidden scale. Thermal states use the
  Mermin occupations at T and four neighbours at T(1 +- 0.01), T(1 +- 0.02) for C_V = T dS/dT, dE/dT and
  -dF/dT; each grid of a thermal state is a job of its own (stage 1: the main state; stage 2: the neighbours).
* **Chemical potential.** mu is the root of sum g f = N. It is found by bisection on a well-conditioned
  form of the residual: (exact integer count of the states below mu - N) minus the holes below mu plus the
  particles above mu. The direct form sum g f - N loses about eps_mach N of absolute precision, which fixes mu
  only to eps_mach N / (dN/dmu) (History below).
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
  the real form, w_Q enters as K -> K + j w_Q. The SCF mixes (dM, v_v, w_Q), starts from the converged
  uniform-gas state and keeps its occupations (as the Rust solver does since 2026-10-16, `claude_failures.md` H3);
  the information field `aufbau_consistent` says whether those occupations are still aufbau-ordered. p0 gets
  -w_Q Q, and the report checks y-conservation, 2 Vol_7 int e^{3Hy} rho = E_KS and the two energy forms.
* **Rescaling partners (a4,0 > 0).** The problem KS(0; H/f0, f0 L, dk e^{-a4,0}, v_t e^{-3 a4,0} b4,0^{3/2}),
  f0 = f(a4,0), is solved independently: its own grid on [-f0 L, 0], label set, three grids, Richardson. The report
  compares it with the state at a4,0 (ks-theory.json rescalingIdentity; the profiles against the scale of their
  family, `claude_failures.md` H6).
* **Particle-hole lists.** The lowest 48 excitations between degenerate groups. Hole groups hold particles.
  Particle groups lie above the hole group and below the lowest level outside the label set, and have
  vacancies. The groups come from the finest grid; the energies and the cut are Richardson values. Each row
  has delta_eps with U, the multiplicity (holes x vacancies) and a same-sector flag.
* **Sea-hole diagnostic (thermal).** For every shell n2 >= 1 of the thermal label set and five more shells,
  the highest sea level of the j = -1 even sector (Sturm index one below the lowest particle level, rank -1;
  the sea fold band, eps = -kappa |k| at lambda = 0) is computed in the converged potentials. The diagnostic reports
  4 r3 f((mu - eps)/T) per shell and cumulatively: the thermal holes that the excluded sea would carry under the
  filling CONVENTION.
* **Crossing demonstration.** N_demo is re-derived as the smallest closed shell N > 8 of the free a4,0 = 0
  aufbau (levels up to 1.6 m) whose last group holds a level off the even j = +1 fold band. At each slice,
  for lambda = 0, the run computes the instantaneous aufbau state (open shells filled uniformly) and the
  adiabatically continued state with the a4,0 = 0 occupation by label. The label set is extended by those
  labels where needed.

## The full canonical matrix (all of it)

* **Ground states (75):** N in {8, N_mid, N_large} = {8, 592, 2352} x 5 coupling tags (0, +-lambda_1,
  +-lambda_2) x 5 slices a4,0 = 0, 0.5, 1, 1.5, 2. Each comes with its Delta-SCF state, four a4 neighbours,
  the adiabaticity pairs and the particle-hole list.
* **Exact-Fock variant (60):** every ground state with lambda != 0.
* **Rescaling partners (60):** every ground state with a4,0 > 0.
* **Crossing demonstration:** lambda = 0, N_demo = 2360, the five slices.
* **Thermal states (135):** N in {8, 592, 2352} x lambda in {0, +-lambda_1} x 5 slices x T in {0.01, 0.02,
  0.05} m. Each comes with four temperature neighbours and the sea-hole diagnostic, evaluated over the shells of the
  thermal label set and max(5, 10% of them) more shells (before 5: the Rust thermal label sets, whose window rule
  differs, reached about 50 shells further at a4,0 = 2, where the fold band is dense; H15).
* **Fourth-grid validation:** N592_lamp2_a20, the strongest coupling of N_mid at the last slice, solved on
  G = 300, 600, 1200, 2400.

## Outputs (`results/`, deterministic: LF, Python float repr, no timings or paths)

| file | content |
| --- | --- |
| `parameters.json` | problem definition, numerics, re-derived N_mid, N_large, couplings (strength per slice, peak position and curvature), N_demo and its closed shells, the matrix (all ids) |
| `free-checks.json` | analytic k = 0 spectra on five grids and at a4,0 = 1.5 (f = e^{-1/2}), zero mode, fold-band slope, particle branch |
| `ground/<id>.json` (75) | per-grid raw scalars and iteration counts; Richardson values with U of the energies, HOMO/LUMO/gap, Delta-SCF, EMT integrals, fold/tip values, dE/da4 (EMT and finite differences), Delta E_x, the lowest excluded level; every level with key (n2, j, parity, rank), eps, U, f; the ten profiles at y = -3 + 0.02 i with U; the 10 largest adiabaticity pairs; the particle-hole list (48 rows) |
| `exx/<id>.json` (60) | exact-Fock variant per grid and Richardson: E_exact_fock_scf, E_uniform_gas, Delta E_x, E_exx - (E_uniform_gas + Delta E_x), HOMO/LUMO/gap, EMT and y-conservation integrals, residuals, the occupations (those of the uniform-gas state) and `aufbau_consistent` |
| `rescaling/<id>.json` (60) | rescaling partner: H/f0, f0 L, dk, v_t, E_KS with U, every level with U, occupations, five profiles |
| `crossing/crossing-demo.json` | N_demo, the a4,0 = 0 occupation, per slice: aufbau and continued energies with U, open shell, labels left and entered |
| `thermo/<id>.json` (135) | mu, E, S, F, Omega (two forms), C_V, dE/dT, -dF/dT with U; levels with occupations; sea holes per shell and cumulative with U |
| `validation/N592_lamp2_a20.json` | three-grid values of (300, 600, 1200) vs (600, 1200, 2400) per quantity class |
| `ground-summary.csv`, `thermo-summary.csv`, `exx-summary.csv`, `rescaling-summary.csv`, `crossing-demo.csv` | the main values with their U |
| `manifest.json` | SHA-256 of every file (339 files) |

## Results (`reports/ks-reference.json`: 39 checks, all PASS; the record of 2026-10-17, corrected metric)

* **Discretisation.** The analytic k = 0 spectra (proper length f L; at a4,0 = 0 and, with f = e^{-1/2}, at 1.5) are
  reproduced to 2.8e-14 by the three-grid values. Single grids give 4.1e-3 (G = 150) down to 1.6e-5 (G = 2400). The
  error ratio is 4.000 (between 3.99977 and 4.00019): clean second order. The k = 0 j = +-1 spectra agree exactly. The
  zero mode is exact (|eps| <= 1.3e-39, b = 0; profile sqrt(2M/(1 - e^{-2ML})) e^{My} to 4.0e-15). The fold-band slope
  equals ks-theory.json c = e^{-a4,0} at the five slices to 1.4e-15 relative.
* **Re-derived inputs.** The closed shells below the bulk edge 1.292292828069 m are 8, 32, 80, 112, 136, 232, 328, 376,
  496, 592, 688, 720, 816, 1008, 1032, 1224, 1368, 1464, 1560, 1752, 1848, 1944, 2064, 2352, so N_large = 2352 and
  N_mid = 592 (the shell nearest to N_large/4). The strengths (per unit lambda_hat, densities per Vol_7(a4,0) with the
  factor e^{-3Hy}, maximum over the slices) are 0.000634178794 (N = 8), 0.04692923076 (N = 592) and 0.1864485654
  (N = 2352), which give lambda_1 = 157.7, 2.131, 0.5363 and lambda_2 = 473.1, 6.393, 1.609, the Rust values.
* **Every ground state (75).** Every check passes. SCF converged on every grid (ground and Delta-SCF states residual <= 9.9e-13 m, the four a4 neighbours <= 1.0e-14 m; every ground state by the direct SCF). Occupations and HOMO/LUMO groups are identical on all
  grids; shells are closed; label sets are complete; N is conserved; the two energy forms agree (1.3e-12 relative).
  2 Vol_7 int e^{3Hy} rho = E_KS holds to 9.5e-5 of the allowance; y-conservation [e^{3Hy} p0] = 3H int e^{3Hy} p_t to
  5.1e-4 of it. dE/da4 from finite differences equals the history identity -3 P3 + P_t + P0/3
  (worst 0.135 of the allowance, N8_lamp2_a10). The discrete Hellmann-Feynman identity holds to 1.0e-11 m. Delta-SCF equals the gap at
  lambda = 0 to 1.9e-13 m. The asymptotic ratio is within 2.2e-4 of 4. The lowest particle-hole excitation is HOMO
  group -> LUMO group at the KS gap in every state. No state needed the coupling continuation (`scf_paths`: none).
* **Exact-Fock variant (60).** Converged on every grid (residual <= 9.9e-13 m) at the occupations of the uniform-gas
  state. N is conserved, the two energy forms agree, and 2 Vol_7 int e^{3Hy} rho = E_KS holds. The y-conservation with
  the derived -w_Q Q term in p0 holds to 9.1e-6 of the allowance. Examples: for N = 8 the exact Fock exchange cancels
  the uniform-gas interaction energy (E_EXX = -3.0e-15 against E_uniform_gas = -0.1109816005144721 for lambda_2,
  a4,0 = 0). For N2352_lamp2_a20: E_EXX = 309.6996697305796 (U 6.2e-10), E_uniform_gas = 303.5549032299388,
  Delta E_x = 6.129981383545180, and E_EXX - (E_uniform_gas + Delta E_x) = 0.01478511709564658.
* **Rescaling partners (60).** The independently solved partner KS(0; H/f0, f0 L, dk e^{-a4,0}, v_t e^{-a4,0}), f0 =
  e^{-a4,0/3}, reproduces the state at a4,0, with the same label set and occupations, to 3.5e-14 (levels in m, E_KS
  relative, profiles relative to the scale of their family). Example: N2352_lamp2_a20, partner dk = 0.03383382080915318,
  v_t = 0.1353352832366127, E_KS = 303.5549032299386.
* **Crossing demonstration.** N_demo = 2360 on every grid (the k = 0 odd bulk levels 0:+-1:odd:0 complete that shell
  at a4,0 = 0). From a4,0 = 0.5 on the bulk levels rise with 1/f, the aufbau empties them and fills the n2 = 27 fold-band
  shell (27:+1:even:0); that state is an open shell. The adiabatically continued state lies 4.676353789, 7.943280897,
  10.40582659 and 12.47798637 m above the aufbau state at a4,0 = 0.5, 1, 1.5, 2.
* **Every thermal state (135).** The thermal identities hold: Omega in two forms, and C_V = dE/dT and -dF/dT = S (worst
  7.8e-3 of the allowance). The window cut carries f <= 6.7e-16. Sea-hole diagnostic: the five shells beyond the label
  set add at most 1.7e-12 of the total. The excluded sea would carry more than 1% of N in 27 of the 135 states. The
  largest are N8_lamp1_a20_T50, N8_lamm1_a20_T50 and N8_lam0_a20_T50 (594.5 N each: 4755.97 holes, U 9.5e-9, at
  mu = -0.187): at a4,0 = 2 the sea fold band eps = -e^{-2} |k| lies within a few T of mu for many shells. There the
  particle-only Mermin ensemble is outside its range of validity (a DIAGNOSTIC of the CONVENTION, not a validation).
* **Uncertainty validated.** On G = 2400 the three-grid value of N592_lamp2_a20 moves by at most 0.029 of the stated U,
  in every element of 19 quantity classes.
* **Examples (Richardson value, U).** E_KS(N592_lamp2_a20) = 47.32639515681918 (9.5e-11); E_KS(N2352_lam0_a00) =
  2288.388233459555 (4.6e-9); E_KS(N2352_lamp2_a00) = 2255.043581213520 (4.7e-9); Delta-SCF(N8_lamp2_a00) =
  0.2499328874693825; Q_max(N2352_lam0_a00) = 0.1943290163255606, Q_max(N2352_lamp2_a00) = 0.1801719041261737.

## Timings (this machine, 24 cores, `--jobs 20`, 2026-10-17, the record of H15)

* Stage 1 (603 jobs, 14759 CPU-seconds: 405 thermal main states 7884 s, 75 ground states 4303 s, 60 exact-Fock variants
  1559 s, 60 rescaling partners 884 s, the validation state 80 s, the crossing demonstration 32 s, the free checks 16 s)
  in six parts, the machine otherwise idle: 193.0, 175.4, 214.0, 179.8, 100.7 and 191.2 s. The longest single jobs:
  N2352_lamm1_a00_T50_G1200 (212.5 s), N2352_lamp2_a20 (178.2 s), N592_lamp1_a20_T50_G1200 (175.7 s).
* Stage 2 (1620 jobs, the temperature neighbours, 15972 CPU-seconds) in six parts: 136.8, 143.7, 133.7, 133.7, 134.2 and
  139.8 s. The longest single jobs: N2352_lamm1_a20_T50_G1200_s+2 (110.2 s), N2352_lamp1_a20_T50_G1200_s-2 (109.6 s).
* The assembly from the cache: 4.4 s. One invocation without a cache would take about 30 minutes on 20 processes,
  longer than the limit of 423 s for one calculation; it was not run.
* Before H15 (every state at the SCF tolerance 1e-12 m except the a4 neighbours): stage 1 188.9, 170.9, 199.7, 202.6,
  107.2 and 207.3 s (15258 CPU-seconds), stage 2 119.8 to 123.3 s per part, the assembly 4.5 s.

## The corrected metric (2026-10-16/17)

On 2026-10-16 the author released the recomputation with the corrected primordial metric (`HANDOFF.md` 0.10, phase
W5). What changed in the code, and why:

* `ks_fd.py`: the hidden scale f (`Phys.fh`, `fh_at`; f = e^{(beta/2 - 1) a4}) divides d_y in the block operator, in the
  rotated-frame scalar phi'/f and in the derivative arrays; kappa = e^{-a4,0} is constant in y (no e^{-Hy}); the
  proper densities carry P = e^{-3Hy}/Vol_7 with Vol_7 = ell^3 v_t e^{(2 beta - 1) a4,0} (`Phys.vol7`), and the
  integrals the weight e^{3Hy} (`Grid.e3`); the y-conservation is [e^{3Hy} p0] = 3H int e^{3Hy} p_t (p0' + 3H (p0 - p_t) =
  0); the history identity is dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0; d_a h contains the kinetic term
  (1 - beta/2) (1/f) d_y; the fold conditions replace the Z2 brane (the names `*_brane` are kept for the fold y = 0).
* `run_reference.py`: the fold-band slope c = e^{-a4,0} (ks-theory.json checksNumeric.braneBandSlope_a0); the analytic
  spectra also at a4,0 = 1.5 (f = e^{-1/2}); the rescaling partner on its own grid [-f0 L, 0] with H/f0 (ks-theory.json
  rescalingIdentity); the profile comparisons of the rescaling partner against the scale of the profile's family
  (`claude_failures.md` H6: S and p0 vanish identically for the lambda = 0 fold-band states); the exact-Fock variant at
  the occupations of the uniform-gas state (H3); every thermal grid a job of its own and the two stages of parts (H7);
  the a4 neighbours at the SCF tolerance 1e-14 m (H12) and, since H15, every state; the sea-hole list longer by
  max(5, 10%) shells (H15).
* What changed in the numbers: everything (solver README, "The corrected metric"): N_mid = 592 and N_large = 2352
  (before 136 and 688), lambda_1 = 157.7, 2.131, 0.5363 and lambda_2 = 473.1, 6.393, 1.609, N_demo = 2360 (before 696),
  the lambda = 0 states are exact fold-band gases, and the excluded sea of the thermal states is much larger at the late
  slices (27 of 135 states above 1% of N, before 15).
* Runs on the way (`claude_failures.md` section H): the first thermal job of three grids in one process was killed at
  423 s (H7), so the thermal grids became jobs of their own; the first stage-1 part 4 ran through a 9-hour system sleep
  (H11; its timing is not used); the first complete run failed `emt_energy_change_dE_da4` in 9 of 75 states (H12) and
  was redone with the tighter neighbour tolerance; a stale docstring of `sea_brane_levels` (eps ~ -c kappa |k|) was
  corrected before the record run, which rebuilt the cache once more; the cross-check of that record failed 3 of 31
  checks (H15: the SCF stopping errors of both solvers at the 1e-10 level in int_p0 and in the exact-Fock first-order
  difference, and the sea-hole coverage), so every state is now solved to 1e-14 m and the sea-hole list is longer; the
  record and both job caches were rebuilt.

## History

The first version solved a representative subset of the canonical matrix (18 of 75 ground states, 8 of 135
thermal states; 28 checks, 226.8 s). It was extended to the full matrix with the exact-Fock variant, the
rescaling partners, the particle-hole lists, the sea-hole diagnostic and the crossing demonstration. Before
that, the subset run had found the Mermin rounding error described next.

The first complete run computed mu by bisection on the direct sum g f - N. The cross-check
(`../checker`) then found that in N8_lamm1_a00_T10 this mu differed by 1.15e-9 from the 40-digit root on
its own levels. That error was far above its stated U (3.2e-11): the direct sum fixes mu only to
eps_mach N / (dN/dmu), and there dN/dmu = 1.2e-6 (gap/T = 43). The reference has used the well-conditioned
residual above since then (cross-checker check `thermo_mu_rounding_diagnostic`).

Records before the corrected metric (superseded; their numbers are in the git history of this file): the record of
2026-10-08 and of 2026-10-14 (the author's metric with b4 = 1, relabelled to x0..x7 on 2026-10-14: N_mid = 136,
N_large = 688, lambda_1 = 0.01946, 0.01206, 0.006645, 38 checks) and the record with b4(x4) of 2026-10-16 (densities per
ell^3 v_t e^{(3/2) beta a4,0} with the factor e^{-6Hy}, withdrawn the same day with that metric).

## What this does not establish

The reference tests the Rust solver's numerics, not the physics model. Both solvers implement the same
ks-theory.json functional, the same ASSUMED fold convention (both fold conditions filled), the same tip cutoff
L = 3 and the same filling CONVENTION. An error in those inputs would be common to both and could not be detected
here. In the corrected metric the extended levels depend on L like those of a box of proper length f L (the tip
condition is a CHOICE; `../tip_convergence/`). The states are instantaneous (adiabatic) Kohn-Sham states; the
non-adiabatic problem is OPEN. The exact-Fock variant is a variant of the functional, not the canonical model. The
sea-hole numbers are a DIAGNOSTIC of the filling convention. They do not justify the convention, whose
justification stays OPEN. The crossing demonstration is a lambda = 0 illustration with N_demo outside the canonical N.
