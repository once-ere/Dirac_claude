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
cargo test --release          # 27 unit tests (see below)
cargo clippy --release --all-targets && cargo fmt --check
./target/release/dirac16complex_kohn_sham print-config
./target/release/dirac16complex_kohn_sham all [--output DIR] [--rtol X] [--atol X] [--refined] [--quick]
```

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
  is not renormalisable in 8D).
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
  lattice multiplicities; states `(eps, s)` with multiplicity `4 g`; normal
  ordering with thermal antiparticles (`w = f` for `eps >= 0`, `-(1-f)` for
  `eps < 0`); `mu` by bisection; T = 0 ensemble filling of a straddling shell;
  proper densities `n_p = e^{-6Hy} n_c`, `S_p = e^{-6Hy} S_c`; Anderson mixing;
  convergence `max|Delta n_c|/max|n_c| < 1e-10` (same for `S_c`); energies
  `E = sum w eps - int[(lambda/2) S_p^2 + e_x] dV_p`, entropy, `F`, `Omega`;
  Delta-SCF with occupations fixed by level identity.
* **EMT** (`emt.rs`): `rho = e^{-6Hy}/l^3 sum w eps n - L_s`,
  `p_y = ... [(eps - v_x) n - P1 - M S] + L_s`, `p_3 = ... P1/3 + L_s`,
  `p_t = L_s`, `L_s = (lambda/2) S_p^2 + e_x`; `int rho dV_p = E`; the
  conservation `p_y' + 6H p_y - 3H p_3 - 3H p_t = 0` is checked; proper-volume
  averages, `w_y, w_3, w_t`, brane-localised fraction (within 1/H of the
  brane), and the mismatch with `rho_req < 0`.

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
(N = 8 = the brane zero modes, E = 0), thermal fill conserves N; `emt`:
`int rho = E` and conservation.

## Output layout (`artifacts/dirac16complex/kohn-sham/rust/`)

`spectrum/`: `reduction.json`, `geometry.json`, `exchange-check.json`,
`uniform-gas-table.csv`, `free-spectrum-m{1,3}-L{2,3,4}.csv`,
`closed-shells-m1-L3.csv`, `summary.json` (reference numbers: N_mid, N_large,
lambda_hat_1, lambda_hat_2).  `scf/`, `thermo/`, `emt/`: one directory per run
(`levels.csv`, `profiles.csv`, `history.csv`, `run.json`) and `summary.json`;
`excited/`: `particle-hole.csv`, `levels.csv`, `levels-excited.csv` per run and
`excitations.csv`; `thermo/thermodynamics.csv`; `emt/emt-summary.csv`.

## Origin of copied code

`src/driver.rs` and `src/output.rs` are copies of the Stage-3 crate
`studies/dirac16complex_cosmology` (this repository, GPL-3.0-or-later); the
driver gained `integrate_adjusted`.  `RunContext`, `Tolerances`,
`ExperimentSummary` and `math` in `lib.rs` are copied from the same crate.
