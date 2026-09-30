# dirac16complex_kohn_sham — Stage-4 Kohn–Sham solver (Rust, CVODE shooting)

Kohn–Sham (Mermin finite-temperature LDA) solver for the dirac16complex fermion
gas in the *static* primordial gravitational field (a4 constant), on the
vendored pure-Rust SUNDIALS 7.8.0 CVODE engine (`vendor/rustSolveIt/sundials_rs`,
fetched by `scripts/setup_solver.*`).  Every eigenvalue problem is solved by
shooting in the proper hidden coordinate `y = ln(sin z)/(6H)` from the tip cutoff
`y = -L` to the Z2 brane `y = 0`; nothing is discretised into a matrix.

Binding documents: `STAGE4_SPEC.md`, `CONTRACT.md` (with errata),
`NUMERICS_CONTRACT.md` (expectation-value rule).  Units `H = 1`.

## Build and run

```
cd studies/dirac16complex_kohn_sham
cargo build --release
cargo test --release          # 46 unit tests (35 Stage 4, 11 Stage 5), 2 ignored timing probes
cargo clippy --release --all-targets && cargo fmt --check
cd ../..                      # run from the repository root (relative artifact paths)
./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham print-config
./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham all [--output DIR] [--rtol X] [--atol X] [--refined] [--quick]
python studies/dirac16complex_kohn_sham/tools/compare_runs.py --canonical artifacts/dirac16complex/kohn-sham/rust \
    --repeat DIR2 --refined DIR3 --report artifacts/dirac16complex/kohn-sham/rust/determinism-report.json
```

`tools/compare_runs.py` (standard library) compares a second run (`--repeat`,
byte identity of every file listed in the summaries) and a `--refined` run
(energies relative 1e-7, eigenvalues absolute 1e-7) with the canonical tree
and writes a checker-format report (`check_<name>=...`, exit 1 on failure).

Subcommands: `print-config`, `spectrum`, `scf`, `excited`, `thermo`, `emt`,
`all` (Stage 4), and `pairs` (Stage 5, section "Stage 5" below; not part of
`all`).  The default output root is `artifacts/dirac16complex/kohn-sham/rust/`
(canonical artifacts); subcommand X writes into `<root>/X/`.  Every check prints
`PASS - name: detail` / `FAIL - name: detail`; the last stdout line is
`SUCCESS` or `FAILURE` (exit code 0/1).  Outputs are deterministic (CSV with
`fmt_e(v, 17)`, LF; JSON with 2-space indent, insertion order, trailing newline;
no absolute paths, no timings), so a repeat run is byte-identical.  `--quick`
runs a reduced matrix (smoke test; not the canonical artifacts).

The constants module `src/generated.rs` is produced by
`scripts/generate_dirac16complex_ks_constants.py` from the exact algebra fixture
(`artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`), which also
verifies the exact 2x2 block basis in Gaussian-integer arithmetic and writes
`artifacts/dirac16complex/kohn-sham/rust/generator-report.json`.

## Physics implemented (summary; the module headers carry the derivations)

* **Field and geometry** (`geometry.rs`): warped form
  `ds^2 = dy^2 - dx4^2 + e^{2Hy}[e^{2a4_0} dx_3^2 - e^{-2a4_0} dx_t^2]`,
  `W = e^{Hy}`, proper 7-volume per coordinate volume `e^{6Hy}`,
  `R = -42H^2`, `G^mu_nu = diag(15,15,15,15,21,15,15,15)H^2`, so Einstein
  gravity needs `rho_req = -21H^2/kappa < 0`, `p_req = +15H^2/kappa`
  (re-derived numerically from the Christoffel symbols).  Extrinsic curvature
  `K^i_j = H` on the warped directions; Z2 extension `W = e^{-H|y|}` with the
  Israel brane stress `S = -(H/kappa) diag(10,10,10,12,10,10,10)` (brane energy
  density `+12H/kappa`), sign convention stated in the module.
* **Reduction** (`blocks.rs`, exact in the generator): the ansatz
  `Psi = e^{-i eps x4} e^{ikx} W^{-3} chi(y)` removes the spin connection;
  `gamma^0, gamma^0 gamma^1, gamma^0 gamma^4, C, B` are simultaneously
  block-diagonal in eight 2x2 blocks labelled by `A0 A1 A4 = -gamma^0 gamma^1 gamma^4 = s`
  (so `s = -j`, where `j` is the eigenvalue of `J = gamma^0 gamma^1 gamma^4` used by the
  exact theory; `rust/spectrum/theory-agreement.json`, note `labelRelation`),
  `i gamma^2 gamma^3 = c1`, `i gamma^5 gamma^6 = c2`.  Block forms:
  `A0 -> sigma_z, A1 -> -i sigma_y, A4 -> -s sigma_x, C -> -c1 sigma_y,
  B -> c1 s (scalar), BC -> -s sigma_y, gamma^4 gamma^1 -> s sigma_z`.
  With `chi = (a, ib)` the equation is real:
  `a' = M a + (s eps - kappa k) b`, `b' = -(s eps + kappa k) a - M b`,
  `kappa = e^{-Hy - a4_0}`.  Two inequivalent block types `s = +-1` (four
  blocks each); the `s = -1` problem is the `s = +1` one with `eps -> -eps`
  and the vector potential negated.
* **Interaction** (`exchange.rs`): `U = (lambda/2) S^2`; Hartree mass
  `lambda S_p`; Fock exchange of the isotropic uniform 8-fold gas is EXACTLY
  `e_x(n, S) = -lambda (n^2 + S^2)/32` at every temperature (the trace kernel
  `Tr[BC P_a(k) BC P_b(k')] = 4[1 + ab (M^2 - k.k')/(EE')]` makes the double
  momentum integral separable; verified by quadrature with the full 16x16
  projectors; the single-k filled shell gives `S^2/8`).  LDA potentials
  `v_s = -lambda S/16` (mass type) and `v_v = -lambda n/16` (potential type);
  the KS equation uses both: `M_eff = m + (15/16) lambda S_p`,
  `eps -> eps - v_v(y)`.  No correlation term (contact interaction beyond HF
  is not renormalisable in 8D).  The potentials use this exact closed form
  (STAGE4_SPEC E4.7); `artifacts/dirac16complex/kohn-sham/exchange-table.json`
  (written by the independent sympy checker) is used only as a cross-check
  (`spectrum/exchange-table-check.json`): the closed form reproduces the
  tabulated double quadrature of every row of the 3-space (`d3`) and
  4-space (`d4`) tables to 1.7e-14, and this crate's own 3-space gas
  quadrature reproduces the tabulated `S(n, T)` and `mu(n, T)` at T >= 0.3 m
  to 2e-9 (the lower-T rows are measured only: the fixed 400-node rule does
  not resolve the Fermi edge).
* **Boundary conditions** (`shooting.rs`): brane parity `Psi(-y) = +-gamma^0 Psi(y)`
  → `b(0) = 0` (+) or `a(0) = 0` (-); tip bag `gamma^0 chi(-L) = +chi(-L)` →
  `b(-L) = 0`.  In signature (4,4) `(gamma^0)^2 = +1`, so the MIT-type condition
  carries no `i` and is a `gamma^0` projection; all these kill the y-current
  (`-2 s Re(a conj(ib)) = 0`).  The + sign at the tip admits no tip-localised
  artefact zero mode for `M > 0`; for parity + and k = 0 the exact brane zero
  mode `a = e^{My}, b = 0, eps = 0` exists.
* **Eigenvalues**: Prüfer angle `a = r cos theta, b = -r sin theta`,
  `theta' = (eps - v_x) + kappa k cos 2theta - M sin 2theta`, `theta(-L) = 0`;
  `Theta(eps) = theta(0; eps)` is strictly increasing, the levels of parity +
  are `Theta = n pi` and of parity - `Theta = pi/2 + n pi` (Sturm-type
  oscillation theorem: every level in a window is found, none is missed; `n`
  is the Prüfer/node index, re-measured from the linear profile).  Bracketing
  by step doubling + Illinois regula falsi; CVODE (Adams for non-stiff shells,
  BDF otherwise).  Profiles: the linear system with accumulators
  `int (a^2+b^2), int(-2ab), int -kappa k (a^2-b^2)`, rescaled through
  `CVodeReInit` when the amplitude leaves `[1e-40, 1e40]`; a profile
  integration that fails in CVODE is retried deterministically (fresh BDF
  session with max_step/10, then Adams with max_step/10; counted in
  `run.json: profileRetries`) and validated by the same matching and winding
  residuals; the error of a failing level names its shell, block type,
  parity, Pruefer index and eps.
* **Self-consistency** (`scf.rs`): torus `Delta k = 0.25 m`, shells with
  lattice multiplicities; states `(eps, s)` with multiplicity `4 g` (the
  `s = -1` states are the `s = +1` levels with `eps -> -eps` when `v_x = 0`,
  found on the union of the window and its mirror image; otherwise the
  negated-potential problem is solved); branches (particle / Dirac sea) by
  continuity from lambda = 0 (the sign of `eps_free` of the level with the
  same shell, parity, block type and Pruefer index); normal ordering with
  thermal antiparticles (`w = f` on the particle branch, `-(1-f)` on the
  sea branch); `mu` by bisection; T = 0 ensemble filling of a straddling shell;
  shells are distributed dynamically over the worker threads in blocks of
  4 x threads and merged in shell order (the output does not depend on the
  thread count); the free levels that define the branches are computed in
  parallel (union of the windows, widened by the exact eigenvalue-shift bound
  `max|M_eff - m| + max|v_x|` rounded up to a multiple of 0.25 m, at least
  one quantum, capped at 3 m, so that small changes of the bound do not
  trigger a new prefetch) and warm-start the interacting levels (no cache
  across solves: it would change the 1e-12-level path of the root search and
  break the byte identity of repeated solves); a lambda = 0 solve is its own
  free spectrum (`eps_free = eps`, no prefetch); the energy
  window is fixed in the first SCF iteration and enlarged only when its edge
  is not free (a window following the running mu moved its edge every
  iteration and, at T > 0, the edge states with occupation ~ f_cut changed
  the densities at the 1e-6 level, so the loop stagnated); energy
  windows always reach down to the T = 0 floor `-(2.5 m + 2 pi/L)` and, at
  T > 0, up to `mu + T ln(1/f_cut) + 0.5 m` with `f_cut = 1e-8` (the neglected
  Boltzmann tail of the level density ~ eps^3 is ~1e-5 of E at T = m, where
  the state is a thermal particle-antiparticle plasma of ~75000 levels);
  level crossings at the Fermi level (measured at N = 1016, attractive
  lambda_hat_2) stop the exact T = 0 loop as stagnant; `solve_ground` then
  follows the self-consistent branch connected to lambda = 0 by
  continuation in the coupling (lambda/4, lambda/2, 3 lambda/4, lambda,
  each step started from the previous converged solution, damped mixing
  beta/4, up to 200 iterations; exact occupations first, Fermi-Dirac
  occupation smearing 1e-3 m then 1e-2 m where they slosh; at the last step
  a smeared result is followed by one more exact-occupation attempt from
  it).  Measured motivation: restarting smeared attempts from a failed
  attempt converged or sloshed depending on 1e-11-level differences of
  lambda_hat (default vs refined tolerances), and a cold start at the full
  coupling drifted to a different, strongly condensed branch
  (max|lambda S_p|/m = 2 to 6).  The path is recorded in `run.json`
  (`parameters.zeroTemperatureFallbackStage`: 0 none, 1 continuation with a
  smeared result, 2 continuation with exact occupations, 3 failed;
  `parameters.occupationSmearing`, `parameters.mixBeta`,
  `exactZeroTemperatureOccupations`); heat capacity at constant N: the
  fixed-spectrum derivative `C_V^(0) = sum mult (df/dT)|_N <h_0>` (exact for
  lambda = 0, where it equals `T dS/dT`) for every T > 0, and the fully
  self-consistent central difference (delta = 0.05 T) for T <= 0.3 m
  (columns `C_V`, `C_V_fd`, `C_V_fixed_spectrum`, `C_V_fixed_spectrum_entropy`);
  thermodynamics (`thermo`): per N in {8, N_mid} three series at fixed
  lambda_hat over T/m in {0, 0.1, 0.3, 1}: `lam0` (free), `lamp1` (the
  T = 0-calibrated lambda_hat_1; a point runs only when its first-order
  pseudo-potential `lambda_hat_1 strength_free(T)` is at most 1 m, the upper
  edge of the STAGE4_SPEC window, because the thermal pair plasma multiplies
  max|S_p| by orders of magnitude: 44 m at T = m, where the Anderson loop
  oscillated between 3.5 m and 55 m; the skipped points and their estimates
  are listed in `thermo/summary.json: skippedRuns`) and `lamh`
  (hot-calibrated `lambda_hat = 0.1/strength_free(T_max)`, so one
  Hamiltonian covers the whole series inside the window at first order);
  interacting points at T > 0 start from the free state at the same T;
  proper densities `n_p = e^{-6Hy} n_c`, `S_p = e^{-6Hy} S_c`; Anderson mixing;
  convergence `max|Delta n_c|/D < 1e-10` and `max|Delta S_c|/D < 1e-10` with
  `D = max(max|n_c|, max|S_c|)` (in the hot pair plasma the net `n_c` is tiny
  while `S_c` is large, and the eigenvalue-noise floor of ~75000 levels in
  `S_c` divided by `max|n_c|` never reached 1e-10); energies
  `E = sum w eps - int[(lambda/2) S_p^2 + e_x] dV_p`, entropy, `F`, `Omega`;
  Delta-SCF with occupations fixed by level identity.
* **Couplings** (`runs.rs`): per configuration (m, L, N), from the free
  ground state of that configuration: `strength = max_y max((15/16)|S_p|,
  n_p/16)/m^7` (the LDA pair `(M_eff - m, v_x)` per unit lambda_hat in units
  of m), `lambda_hat_1 = 0.1/strength`, `lambda_hat_2 = 1.0/strength`, so the
  pseudo-potential reaches 0.1 m and 1.0 m at first order (STAGE4_SPEC
  section 4); the self-consistent `max|lambda S_p|/m` and `max|v_x|/m` are
  in every `run.json`.  No global lambda_hat can serve all configurations:
  the proper densities at the tip scale like `e^{6HL}` and grow with N
  (measured: the N = 112 value gives |lambda S_p|/m = 11 in the free N = 1016
  state and the attractive SCF at that coupling runs away).  For N = 8 the
  free scalar density vanishes exactly (brane zero modes) and the vector
  part sets the scale.  The convergence runs (grid 601, Delta k = 0.125 m
  with 8 N) reuse the (m = 1, L = 3, N_mid) value; the a4_0 = 0.5 run is
  paired with the EXACTLY equivalent a4_0 = 0 problem at Delta k e^{-0.5}
  and lambda_hat_1 e^{1.5} (same M_eff, v_x, levels and E: the torus of the
  partner is larger by e^{1.5} in coordinate volume), compared level by
  level (`a4_rescaling_pair_exact`).
* **EMT** (`emt.rs`): `rho = e^{-6Hy}/l^3 sum w eps n - L_s`,
  `p_y = ... [(eps - v_x) n - P1 - M S] + L_s`, `p_3 = ... P1/3 + L_s`,
  `p_t = L_s`, `L_s = (lambda/2) S_p^2 + e_x`; `int rho dV_p = E`; the
  conservation `p_y' + 6H p_y - 3H p_3 - 3H p_t = 0` is checked; proper-volume
  averages, `w_y, w_3, w_t`, brane-localised fraction (within 1/H of the
  brane), and the comparison with `rho_req < 0` (the sign of `<rho>`, the
  kappa it would need and its sign compatibility per run; the spec's
  expectation of a positive KS energy density fails for N = 8, recorded in
  `emt/summary.json: positiveRhoExpectation`).  STAGE4_SPEC E4.1: the
  static-field sourcing conditions `m S = -36 H^2/kappa`, `lambda S^2 =
  30 H^2/kappa` (together `lambda S/m = -5/6`, `m S < 0`) are evaluated on
  `<S_p>` of every run (`run.json: emt.E41_sourcingConditions`, columns of
  `emt/emt-summary.csv`): the two kappa's, the ratio `lambda <S_p>/m`, the
  first-order `lambda_hat` at which they would coincide, the sign of `S_p`
  (min/max on the grid) and the verdict.  Measured sign of S: massive bulk
  levels carry positive scalar charge (`M/eps` at k = 0), the k = 0 brane
  zero modes exactly 0, and the brane band `eps = +ck` (k != 0) NEGATIVE
  scalar charge (`d eps/dM = k dc/dM < 0`, the exact `c(M)` decreases toward
  1 with M); the ground states of this study are dominated by the brane
  band, so `<S_p> < 0` and the mass condition alone gives a positive kappa.
  Mirror sector: the block swap `(a, b) -> (b, a)` with `s -> -s` maps the
  problem (m, lambda, tip bag `b(-L) = 0`) exactly onto (-m, lambda, bag
  `a(-L) = 0`) with identical energies and `S -> -S`, so `m S`, `lambda S^2`
  and the E4.1 verdict are unchanged there (the KS form of the gamma^8 map;
  derivation in the `emt.rs` header).

## Unit tests (`cargo test --release`)

`blocks`: reduction exact to 1e-14, complex block equation = real system;
`geometry`: curvature closed forms, coordinate maps; `exchange`: Gauss–Legendre,
filled-shell 1/8, kernel identity and closed form at finite T, potentials are
derivatives, gas `mu(n)`; `spline`; `driver` (incl. the `CVodeReInit`
rescaling hook); `shooting`: free-box parity ± spectra vs the analytic 1D Dirac
box (`eps = 0, +-sqrt(M^2 + (n pi/L)^2)`; `tan(pL) = -p/M`), momentum lifts the
brane mode and the lowest excitation, Hellmann–Feynman in `M` (non-uniform
potential) and in `k` (5-point stencils), `(k, eps) -> (-k, -eps)` symmetry,
deep-evanescence rescaling, the profile fallback ladder reproduces the
primary integration; `scf`: shells, Anderson, non-interacting fill
(N = 8 = the brane zero modes, E = 0), thermal fill conserves N, repeat run
byte-identical, an asymmetric window keeps every mirror state (regression
test for the closed-shell table), free-window widening quantised and capped;
`emt`: `int rho = E`, conservation and the E4.1 evaluation (negative scalar
charge of the brane band); `theory`: SHA-256 known answers, the
exchange-table cross-check (skipped when the table is absent).

## Output layout (`artifacts/dirac16complex/kohn-sham/rust/`)

`generator-report.json` (exact block basis, from the generator);
`spectrum/`: `reduction.json`, `geometry.json`, `exchange-check.json`,
`exchange-table-check.json`, `theory-agreement.json`, `uniform-gas-table.csv`,
`free-spectrum-m{1,3}-L{2,3,4}.csv`, `closed-shells-m1-L3.csv`,
`summary.json` (reference numbers: N_mid, N_large, lambda_hat_1,
lambda_hat_2).  `scf/`, `thermo/`, `emt/`: one directory per run
(`levels.csv`, `profiles.csv`, `history.csv`, `run.json`) and `summary.json`;
`excited/`: `particle-hole.csv`, `levels.csv`, `levels-excited.csv` per run and
`excitations.csv`; the summary record of every excited run carries the
parameters of its converged ground state (including the T = 0 occupation
smearing of a level-crossing fallback); the particle-hole lists count a
state as a hole when f > 1e-12 and as a particle when f < 1 - 1e-12
(`PH_OCCUPATION_FLOOR`, the reference solver's T = 0 rule: the Fermi-Dirac
tails of a smeared run are neither); the run `m1_L3_N1016_lamm2_T0_g601` is
the 601-point grid refinement of the hardest Delta-SCF (check
`excited_grid_refinement_delta_scf`; not a row of `excitations.csv`); `thermo/thermodynamics.csv` (column `series`: 0 lam0,
1 lamp1, 2 lamh; per-series couplings and first-order estimates in
`thermo/summary.json: series`); `emt/emt-summary.csv`;
`determinism-report.json` (repeat byte identity and refined-tolerance
convergence, written by `tools/compare_runs.py`; the repeat and refined
trees themselves are not committed).

## Canonical results (`artifacts/dirac16complex/kohn-sham/rust/`, H = 1, m = 1, L = 3 unless stated)

All five subcommands SUCCESS (spectrum 33 checks, scf 137, excited 65,
thermo 102, emt 60); `determinism-report.json`: a second run is
byte-identical (327 files) and a `--refined` run (rtol, atol / 10,
max_step / 2) agrees to 6.0e-8 relative in E and F (65 runs) and 2.8e-8
absolute in 364829 eigenvalues.

* Free spectrum: brane zero modes `eps = 0` at k = 0 (exact), split as
  `+-c k` with `c = 1.9051482` (theory file: 1.9051482536); KS gap of
  N = 8: 0.4243017 (L = 2), 0.4307337 (L = 3), 0.4307456 (L = 4) m;
  closed shells N_mid = 112, N_large = 1016 (also N_mid = 112 at m = 3).
* Couplings (first-order pseudo-potential 0.1 m / 1 m): lambda_hat_1 =
  9.73e-3 (N = 8), 9.57e-3 (112), 1.577e-4 (1016); lambda_hat_2 = 10 x;
  self-consistent max|lambda S_p|/m up to 1.37 and max|v_x|/m up to 1.5
  (N = 1016, attractive lambda_hat_2).
* Ground states E_0 / KS gap / Delta-SCF (m): N = 8: 0 / 0.430734 /
  0.430734 (lambda = 0), -9.87e-4 / 0.430944 / 0.430938 (+lh1),
  -7.83e-3 / 0.431899 / 0.431946 (+lh2); N = 112: 61.090723 / 0.0955462 /
  0.0955462, 61.113212 / 0.0954841 / 0.0954842 (+lh1), 61.328311 /
  0.0948132 / 0.0948140 (+lh2), 60.891305 / 0.0960102 / 0.0960098 (-lh2);
  N = 1016: 1127.136625 / 0.0530077 / 0.0530077, 1127.342203 / 0.0544240 /
  0.0545261 (+lh2), 1126.858093 / 0.0412551 / 0.0436184 (-lh2: level
  crossing, coupling continuation, smearing 1e-3 m; on 601 grid points
  1126.858089 / 0.0412551 / 0.0436194).  The lowest particle-hole
  excitation of the -lh2 ensemble is zero (6.6e-12: the two numerically split
  halves of the fractionally occupied k = 0 level), then 3.69e-3 m (band ->
  k = 0 level) and the KS gap 0.0412551 m.
* Thermodynamics (N = 8, lambda = 0): F = -0.39398, -30.5115, -11447.70 and
  C_V = 33.62, 1754.1, 2.383e5 at T/m = 0.1, 0.3, 1 (E = 46811.7 at T = m:
  a thermal pair plasma of ~75000 levels per block type); the
  T = 0-calibrated lh1 would reach a first-order pseudo-potential of 41 m
  at T = m (not run, recorded), the hot-calibrated lambda_hat = 2.368e-5
  gives max|lambda S_p|/m = 0.104 at T = m.
* EMT: w_y = 0.449, 0.336 and w_3 = 0.297, 0.290 (N = 112, 1016; w_t = p_t/rho
  = 0 without interaction); brane-localised fraction of N within 1/H of the
  brane 0.867 (N = 8), 0.924 (112), 0.962 (1016), 0.998 at m = 3; <rho> > 0
  for every state with bulk levels, so rho_req = -21 H^2/kappa would need
  kappa = -909 (N = 112), -49.3 (N = 1016); for N = 8 the spec's
  positive-energy expectation FAILS (measured): <rho> = 0 (free) and
  -3.7e-7 (lambda > 0, sign-compatible kappa = 5.6e7, but then the E4.1
  mass condition gives kappa = -1.2e7); the E4.1 conditions are met in no
  run (they would need lambda <S_p>/m = -5/6, i.e. lambda_hat ~ 106
  (N = 112) and 9.6 (N = 1016) at first order, 10^3 to 10^4 x lambda_hat_2).

## Provenance of the canonical tree

`spectrum`, `scf` and `thermo` were produced by one release build (SHA-256
of the executable 6e7d2a93...).  `emt` was produced by a later build
(SHA-256 17b010b8...), which differs from 6e7d2a93 only in `runs::run_emt`
(the positive-energy assertion replaced by the evaluated comparison and the
per-run sign lists) and reproduces the `spectrum` tree of 6e7d2a93 byte for
byte (15 files).  `excited` was produced by the final build (SHA-256
3bbc395a...), which adds the occupation-floor particle-hole rule, the
parameter blocks of the excited records and the 601-point refinement run;
its other excited outputs are byte-identical to those of 6e7d2a93.  The
Stage-4 gate reproduces every subcommand with the final build.  The repeat
and refined trees were produced the same way (the same build per
subcommand), so the byte comparison of `determinism-report.json` compares
like with like.  Temporary diagnostic examples used during development are
not part of the crate.

## Stage 5: the `pairs` subcommand ({+M, -M} pairing, both statistics)

Binding: `handoff/specs/STAGE5_SPEC.md` (sections 4, 5: T3, T4) and the exact
theory `artifacts/dirac16complex/pair-creation/pairing-theory.json` (section
T3, `wolfram/Dirac16ComplexPairing.wl`).  Module `src/pairs.rs`; output root
`artifacts/dirac16complex/pair-creation/rust/` (the subcommand writes into
`<root>/pairs/`; `--output DIR` writes into `DIR/pairs/`).

```
./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham pairs [--output DIR] [--refined] [--quick]
python studies/dirac16complex_kohn_sham/tools/compare_pairs_runs.py --canonical artifacts/dirac16complex/pair-creation/rust \
    --repeat DIR2 --refined DIR3 --report artifacts/dirac16complex/pair-creation/rust/determinism-report.json
python studies/dirac16complex_kohn_sham/tools/compare_pairs_runs.py --stage4-committed artifacts/dirac16complex/kohn-sham/rust \
    --stage4-run DIR4 --full spectrum --quick excited scf --report artifacts/dirac16complex/pair-creation/rust/stage4-identity-report.json
```

`pairs` is not part of `all` and does not change `print-config`.

### New parameters (all default to the Stage-4 values)

* `Params::statistics` (`exchange::Statistics`): `Anticommuting`
  (dirac16complex, the Stage-4 functional: `e_x = -(lambda/32)(n^2 + S^2)`,
  `M_eff = m + (15/16) lambda S_p`, `v_x = -(lambda/16) n_p`) or `Commuting`
  (dirac16complex00: `e_x = +(lambda/32)(n^2 + S^2)`, `M_eff = m + (17/16)
  lambda S_p`, `v_x = +(lambda/16) n_p`), the formulas of
  pairing-theory.json `statistics.hartreeFock` / `T3.numericsPrescription`.
  The anticommuting methods call the Stage-4 functions, bit for bit.
* `Params::tip_bag` / `Potential::tip` (`shooting::TipBag`): `B` (`b(-L) =
  0`, bag angle theta = 0, Pruefer `theta(-L) = 0`, Stage 4) or `A` (`a(-L)
  = 0`, theta = pi, Pruefer `theta(-L) = pi/2`, profile start `(a, b) = (0,
  -1)`): the image of `B` under the block form of gamma^8
  (`sigma2 Q(theta) sigma2 = Q(pi - theta)`).
* Negative mass: every scale of the units "m = 1" uses `|m|`
  (`Params::mass_scale`: Delta k, the window floor, the T = 0 and T > 0
  margins, the window enlargement, the fallback smearing, the free-level
  window quantum and cap, max|lambda S_p|/m and max|v_x|/m, the coupling
  strength per m^7); `lambda_hat = lambda m^6` is even in m.  The free
  partner levels that classify the particle/sea branches are computed with
  the signed m and the run's tip bag, so the branch labels of the -M universe
  are the images of the +M ones (the zero mode `(0, e^{My})` of minusM is a
  particle state like `(e^{My}, 0)` of plusM).
* `run.json` / `summary.json` of the Stage-4 subcommands are unchanged:
  `statistics`, `exchangeSign`, `tipBag`, `bagAngleTheta` are written into a
  parameter block only when they differ from the defaults.

### Universes, maps and checks

Per configuration (statistics, |m|, L = 3, N, lambda_hat, T): `plusM` (+|m|,
`b(-L) = 0`, the Stage-4 problem, solved by `scf::solve_ground`), `minusM`
(-|m|, the same lambda and statistics, `a(-L) = 0`: the transformed boundary
conditions of T3.theoremStandardRule, solved by `scf::solve_ground`) and
`minusM_control` (-|m|, `b(-L) = 0`, untransformed).  The control is solved by
the direct Stage-4 SCF attempt (the first stage of `solve_ground`, without
the coupling continuation) and only when its first SCF update satisfies the
window premise of the solver, `max|M_eff - m| + max|v_x| <= |window floor|`
(`pairs::first_update_shift`; the analogue of the Stage-4 thermo rule that
runs a point only when its first-order pseudo-potential lies in the window).
At lambda = 0 the control always runs (the exact control of the theory:
tip-localised zero mode, mixed-sector levels `q cos qL - M sin qL = 0`, bound
state `tanh(kappa L) = kappa/M`).  At lambda != 0 its free state has the
zero modes at the tip, where the proper-density factor is `e^{6HL}` = 6.6e7
(L = 3); the measured first-update shift bounds are recorded in
`pairing.json` and `summary.json: controlOutcomes` (not run when above the
floor).
Level map plusM -> minusM: `(shell, p, s, n) -> (shell, -p, -s, -n)`, same eps,
orbital `(a, b) -> +-(b, a)`.  Checked per configuration: levels (eps, f,
weights, multiplicities, the sorted spectra with multiplicity), orbitals, mu,
E, F, S_ent, N, the KS gap, the particle-hole list, Delta-SCF and E1 (T = 0),
the total scalar charge (opposite), the profiles n_c, n_p, v_x, rho, p_y,
p_3, p_t (equal) and S_c, S_p, M_eff (opposite) in the SCF's own convergence
norm (coordinate densities relative to `D = max(max|n_c|, max|S_c|)`, the
proper quantities divided by `e^{-6Hy}` first: relative to their own maximum
the tip amplification `e^{6HL}` of the SCF resolution would dominate), the
EMT averages (relative, or in energy units after multiplication with the
proper volume), the first SCF updates (equal shift bounds), the pair
totals (mirror pair plusM + minusM: 2E, 2N, S = 0; Krein-image pair plusM -
minusM: E = 0, charge 0, <rho> = <p> = 0, S = 2 S_+), the KS potentials
against the formulas of the statistics (node by node, within the residual
bound of the last SCF iteration, whose input densities built them), the window premise of the solver
(max|M_eff - m| + max|v_x| <= |window floor|), and for plusM of dirac16complex
the bitwise reproduction of the committed Stage-4 numbers.  Across
configurations: plusM(lambda) vs minusM(-lambda) must not map; the two
statistics are bitwise identical at lambda = 0 and differ at lambda != 0.
The lambda-independent free section checks the key map on the free spectra
(|m| = 1, 3; L = 2, 3, 4), the analytic k = 0 box spectra of the three
universes (the control's mixed sector `q cos qL - M sin qL = 0` and its
bound state `tanh(kappa L) = kappa/M`), the zero modes and their
localisation, the splitting constants `c(M)` and `c_ctrl(M)` against the
closed forms and the values exported by the exact theory, and the 16 x 16
block map of gamma^8 in this crate's basis.

First excited state: T = 0 KS gap, particle-hole list (floor 1e-12),
Delta-SCF; T > 0 the Mermin state, the KS gap and the particle-hole list with
the finite-T rule (holes f >= 1/2, particles f < 1/2); Delta-SCF is the T = 0
construction of Stage 4 and is not computed at T > 0.

### Unit tests added (Stage 5)

`exchange::statistics_sign_of_the_exchange`; `pairs`: the swap identity of
the real block system, the key map, gamma^8 = sigma2 between partner blocks,
the block map on the free spectrum (shooting levels and profiles, KS
spectrum keys and multiplicities), the negative-mass free box spectra
(minusM and the control, incl. the bound state) against the analytic ones,
the zero-mode localisation `(0, e^{My})` and `(e^{-My}, 0)` and the
splitting constants, the statistics sign in the KS potentials (v_x opposite,
(M_eff - m) in the ratio 17/15), the Stage-4 defaults (no new keys in
`run.json`; |m| scales), and an interacting SCF pairing (both statistics).

## Origin of copied code

`src/driver.rs` and `src/output.rs` are copies of the Stage-3 crate
`studies/dirac16complex_cosmology` (this repository, GPL-3.0-or-later); the
driver gained `integrate_adjusted`.  `RunContext`, `Tolerances`,
`ExperimentSummary` and `math` in `lib.rs` are copied from the same crate.
