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
cargo test --release          # 34 unit tests, 2 ignored timing probes (see below)
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
`all`.  The default output root is `artifacts/dirac16complex/kohn-sham/rust/`
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
  block-diagonal in eight 2x2 blocks labelled by `J = gamma^0 gamma^1 gamma^4 = s`,
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
  `CVodeReInit` when the amplitude leaves `[1e-40, 1e40]`.
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
  lambda_hat_2) stop the exact T = 0 loop as stagnant and are re-solved with
  Fermi-Dirac occupation smearing (1e-4 m, then 1e-3 m), recorded in
  `run.json` (`parameters.occupationSmearing`,
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
  part sets the scale.  The convergence pairs (a4_0 = 0.5, grid 601,
  Delta k = 0.125 m) reuse the (m = 1, L = 3, N_mid) values.
* **EMT** (`emt.rs`): `rho = e^{-6Hy}/l^3 sum w eps n - L_s`,
  `p_y = ... [(eps - v_x) n - P1 - M S] + L_s`, `p_3 = ... P1/3 + L_s`,
  `p_t = L_s`, `L_s = (lambda/2) S_p^2 + e_x`; `int rho dV_p = E`; the
  conservation `p_y' + 6H p_y - 3H p_3 - 3H p_t = 0` is checked; proper-volume
  averages, `w_y, w_3, w_t`, brane-localised fraction (within 1/H of the
  brane), and the mismatch with `rho_req < 0`.  STAGE4_SPEC E4.1: the
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
deep-evanescence rescaling; `scf`: shells, Anderson, non-interacting fill
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
`excitations.csv`; `thermo/thermodynamics.csv` (column `series`: 0 lam0,
1 lamp1, 2 lamh; per-series couplings and first-order estimates in
`thermo/summary.json: series`); `emt/emt-summary.csv`;
`determinism-report.json` (repeat byte identity and refined-tolerance
convergence, written by `tools/compare_runs.py`; the repeat and refined
trees themselves are not committed).

## Origin of copied code

`src/driver.rs` and `src/output.rs` are copies of the Stage-3 crate
`studies/dirac16complex_cosmology` (this repository, GPL-3.0-or-later); the
driver gained `integrate_adjusted`.  `RunContext`, `Tolerances`,
`ExperimentSummary` and `math` in `lib.rs` are copied from the same crate.
