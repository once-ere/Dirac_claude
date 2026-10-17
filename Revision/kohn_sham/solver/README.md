# Revision Kohn-Sham solver (Rust) — instantaneous states of dirac16complex in the primordial field

New Revision crate (own empty `[workspace]`, no external crates). It implements SPEC section 7 from the
formulas of `Revision/kohn_sham/ks-theory.json` (checked in `Revision/kohn_sham/reports/ks-theory-*.json`).
No code, number or fixture of the old stages is used; `studies/dirac16complex_kohn_sham` was read only to
recall that a shooting method with a Pruefer count suits this problem.

The metric is the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md`, section 1):
g = diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real. In the hidden
coordinate y = ln|sin z|/(6H) <= 0 (on every quarter of the period of z; the fold cos z = 0 is y = 0) the line element
is ds^2 = e^{2a4} dx_{1..3}^2 - dx4^2 + f^2 [dy^2 - e^{2Hy} dx_{5..7}^2] with the hidden scale f = e^{-a4} b4^{1/2}.
The history of the record is a4 = H x4, b4 = e^{(4/3) H x4} (beta = d ln b4/d a4 = 4/3, b4(0) = 1), a PRESCRIBED
BACKGROUND: f = e^{-a4/3}, the momentum weight kappa = e^{-a4} (constant in y), the proper 7-volume of the cell grows
like e^{(5/3) a4}. The record was moved to this metric on 2026-10-16 (section "The corrected metric" below); the
metric of 2026-10-14 with b4(x4) in the extra-time components only, and the one before it (b4 = 1), are withdrawn
(their sections at the end are history).

The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction (cut off at the tip y = -L); x1, x2, x3 = 3-space
(scale factor e^{a4}); x4 = time; x5, x6, x7 = the three extra times (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}
= f e^{Hy}). p0 = T^x0_x0 is the hidden-direction pressure, p_t = T^x5_x5 the extra-time pressure. Names of files,
CSV columns and checks that contain "brane" are kept from the earlier record for continuity; they denote the fold
y = 0.

## Build and run (from the repository root)

```
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
cargo test  --release --manifest-path Revision/kohn_sham/solver/Cargo.toml      # 13 unit tests
B=Revision/kohn_sham/solver/target/release/revision_ks_solver
# canonical matrix in two parts with a job cache, then the assembly (each invocation far below 423 s)
$B all --cache build/revision/ks-canonical-cache --part 1/2
$B all --cache build/revision/ks-canonical-cache --part 2/2
$B all --cache build/revision/ks-canonical-cache --out Revision/kohn_sham/results --report Revision/kohn_sham/reports/ks-rust-solver.json
python Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work <scratch>/mermin-roots         # 40-digit mu roots
# repeat (three parts, other thread counts) and refined tolerances (four parts), each with its own cache
$B all --cache <scratch>/repeat-cache --part i/3 --inner-threads 2                                # i = 1, 2, 3
$B all --cache <scratch>/repeat-cache --out <scratch>/repeat --report <scratch>/repeat-report.json --inner-threads 3
$B all --refined --cache <scratch>/refined-cache --part i/4                                        # i = 1..4
$B all --refined --cache <scratch>/refined-cache --out <scratch>/refined --report <scratch>/refined-report.json
python Revision/kohn_sham/solver/tools/compare_runs.py --canonical Revision/kohn_sham/results \
   --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json --repeat <scratch>/repeat \
   --repeat-report <scratch>/repeat-report.json --refined <scratch>/refined \
   --refined-report <scratch>/refined-report.json --report Revision/kohn_sham/reports/ks-rust-determinism.json
$B single --m M --lambda L --a4 A --N N --out FILE.json [--beta B] [--coordinate-cell] [--tip-theta TH] [--T T]
   [--exx] [--margin W] [--profiles FILE.csv] [--mermin-levels FILE.json] [--refined]
```

`all` without `--cache` computes the whole matrix in one invocation (285 s on 22 threads, 2026-10-16: too close to
the limit of 423 s for one calculation, hence the parts). The job cache (`src/cache.rs`): `--cache DIR --part i/n`
computes a fixed part of the 75 ground and 135 thermal tasks (a longest-processing-time assignment by a cost model;
only the balance depends on it) and stores every finished task in DIR, writing no outputs; `--cache DIR` alone loads
the cached tasks, computes any missing one, runs the rest (free spectra, calibration, history, crossing
demonstration, T3 self-test) and writes the outputs. Every task is a pure function of its inputs and every float is
stored as its IEEE-754 bit pattern, so the assembled outputs are byte for byte those of one run without a cache
(verified on 2026-10-16: two parts and the assembly with inner threads 2, 2, 3 against one run with 4, all files and
the report identical). The cache is tied to a key (`cache-key.txt`: the sha256 of ks-theory.json, gammas.json and of
the solver source compiled into the binary, the numerics, `--quick`) and refuses a cache made with other inputs.
`--inner-threads N` (default 4) solves the sectors of one Kohn-Sham state in parallel; the sectors are independent
problems collected in a fixed order, so no output depends on N (nor on `--threads`, which distributes the states).

The 13 unit tests are `json::tests::roundtrip`, `model::tests::{r3_values, rounding}`,
`sha256::tests::known_answers`, `cache::tests::exact_float_roundtrip`, `shoot::tests::{free_k0_even_spectrum_and_zero_mode,
free_k0_even_spectrum_with_hidden_scale, phi_is_increasing_for_both_block_types}` and the five Mermin-root tests
`mermin::tests::{two_level_closed_form, log_balance_survives_underflow, open_shell_and_repivot,
direct_count_negative_control, forty_digit_roots}` (see Method, The Mermin root).

`tools/mermin_roots_mp.py` runs `single --mermin-levels` for all 135 thermal states (the option writes the
final levels and mu as shortest round-trip decimals, so the tool reads exactly the solver's doubles), computes
the root of sum g f = N on these levels with mpmath at 40 digits (checked at 50 digits), and writes
`reports/ks-rust-mermin-roots.json` (5 checks) and the fixture `tools/mermin-roots-40digit.json` (the 8 states
with the largest conditioning bound of the former direct count). Its check `single_reproduces_committed_matrix`
compares with the committed `results/thermo/thermodynamics.csv`, so it runs after the canonical matrix. The
fixture is in turn an input of the canonical report (check `thermo_mu_vs_40digit_roots`) and of the unit test
`mermin::tests::forty_digit_roots`: after a change of the solver, run the matrix, the tool, and the assembly
again; on a reproduction of the committed state every file is byte-identical in one pass.

`all` prints every check as `PASS/FAIL - name: detail` on stderr and `SUCCESS`/`FAILURE` last on stdout
(exit 0/1). `--timing FILE` writes the wall-clock times (kept outside the results so that two runs are
byte-identical). `single` solves one state with chosen parameters (for example the T3 image problem:
`--m -1 --tip-theta 3.141592653589793`) and writes levels, energies, energy-momentum integrals and identities;
`--beta B` sets the history b4 = e^{B a4} (f = e^{(B/2 - 1) a4}, Vol_7 = ell^3 v_t e^{(2B - 1) a4}),
`--coordinate-cell` keeps f and kappa of the slice and uses Vol_7 = ell^3 v_t (then `--lambda` is lambda_eff =
lambda_hat e^{-(2 beta - 1) a4,0}, ks-theory.json densities.couplingVolumeScaling), `--exx` at T = 0 takes the path of
the canonical matrix (the uniform-gas ground state, then the exact-Fock variant at its occupations).

## Method

* **Reduction (from ks-theory.json, re-verified here numerically):** Psi = e^{-i eps x4} e^{i k.x} e^{-(3/2)Hy}
  e^{a4/2} b4^{-1} V_beta chi(y) gives in each of the eight 2 x 2 blocks
  h_j = j[-(i/f) sigma1 d_y + M_eff sigma2 + kappa k sigma3] + v_v, kappa = e^{-a4,0}, f = e^{-a4,0} b4,0^{1/2}
  (= e^{-a4,0/3} on the history); the factor e^{-(3/2)Hy} removes the (3/2)(H/f) gamma^(x0) and e^{a4/2} b4^{-1} the
  (b4'/b4 - a4'/2) gamma^(x4) of gamma^mu Omega_mu (ks-theory.json sectorAndAnsatz, checks ansatz_* of the theory
  reports). The crate reads the exported basis V and the gamma matrices (`Revision/algebra/gammas.json`) and checks
  that V^dag X V is block diagonal with exactly these forms for the operators of h and of the densities (check
  `block_reduction_numeric`); check `theory_input_metric_forms` verifies that ks-theory.json states exactly the forms
  implemented here (the real form with f, kappa constant in y, P = e^{-3Hy}/Vol_7 with Vol_7 = ell^3 v_t
  e^{(2 beta - 1) a4,0}, the y-conservation, the history identity, c = e^{-a4,0}). With chi = (a, i b) the equation is
  real: a' = f [M a - (K + j(eps - v)) b], b' = f [(j(eps - v) - K) a - M b], K = kappa k (+ j w_Q).
* **Eigenvalues by shooting with a Pruefer count (justification):** the Pruefer angle theta = atan2(b, a)
  has d theta(0)/d eps = j f int r^2 dy / r(0)^2, so Phi(eps) = j theta(0) is strictly increasing. The tip
  condition (regular tip, theta_tip = 0: b(-L) = 0) fixes theta(-L); the fold conditions (the two halves of a cell
  joined at the fold; self-adjointness requires (1 - Q(theta)) chi(0) = 0, and the record solves and fills both
  theta = 0, b(0) = 0 "even", and theta = pi, a(0) = 0 "odd", an ASSUMED convention) give Phi = l pi or pi/2 + l pi.
  Every level is the unique root for an integer label l (oscillation theorem): no level is missed, and l is a
  topological label that follows a level continuously between SCF iterations, couplings and slices. Roots:
  safeguarded Newton (derivative from f int r^2) inside a bracket, tolerance 1e-13 m.
* **Integration:** classical RK4 with G = 900 steps on [-L, 0] (refined run: 1800). The potentials live on
  the fine grid (nodes and step midpoints), so every RK4 stage uses stored values. Orbitals at the midpoints
  come from cubic Hermite interpolation (O(h^4)). Integrals use Simpson's rule on the fine grid.
* **Lattice of 3-space momenta:** k = dk n, n in Z^3, dk = 0.25 m (3-torus of size ell = 2 pi/dk), shells
  n2 = |n|^2 with r3(n2) vectors. Each level of h_j(|k|) is 4 r3(n2)-fold for each j (4 blocks times the
  directions; ks-theory.json blockEquation.degeneracy). Sectors are (n2, j, fold condition).
* **The fold band:** with constant M and theta_tip = 0 the even j = +1 level of every k is exactly
  chi = (e^{f M y}, 0) with eps = kappa k (b = 0 solves both boundary conditions), the k = 0 member is the zero mode;
  for j = -1 the same orbital has eps = -kappa k (the sea fold band). The bulk levels at k = 0 are
  +-sqrt(M^2 + (n pi/(f L))^2) (even) and +-sqrt(M^2 + p^2), tan(p f L) = -p/M (odd): they rise along the history,
  while the fold band redshifts.
* **Particles (CONVENTION of ks-theory.json, justification OPEN):** particles are the labels whose lambda = 0
  level at the same slice is positive, plus the k = 0 zero modes. In a sector these are the labels
  l >= l_min (check `free_particle_branch_labels`). The negative branch is the normal-ordered sea: it is not
  populated, not even thermally (see the diagnostic below).
* **Densities and functional:** n, S, Q per proper 7-volume, P = e^{-3Hy}/Vol_7(a4,0) with
  Vol_7(a4,0) = ell^3 v_t e^{-a4,0} b4,0^2 = ell^3 v_t e^{(2 beta - 1) a4,0} = ell^3 v_t e^{(5/3) a4,0}, w = 1/2 (each
  orbital is normalised on one half of the cell, int_{-L}^0 chi^dag chi dy = 1). The record uses b4(0) = 1; the
  coupling is lambda_hat = lambda b4(0)^{-2} (ks-theory.json densities.proper; b4(0) also enters f0 = b4(0)^{1/2}
  e^{-a4,0/3}). Because a state depends on the coupling and the cell volume only through lambda/Vol
  (ks-theory.json densities.couplingVolumeScaling), a slice state equals the state of the coordinate cell
  ell^3 v_t at lambda_eff = lambda_hat e^{-(5/3) a4,0} with the same f and kappa (`single --coordinate-cell`).
  M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n are the Hartree terms plus the exact local
  exchange of the uniform 8-fold gas, e_int = lambda[(15/32) S^2 - (1/32) n^2]. This is the canonical
  functional. The **exact Fock exchange** of the closed-shell slab determinant differs by +lambda Q^2/32
  (ks-theory.json exchange.exactFockSlab). It is reported for every state as Delta E_x and solved as the
  variant w_Q = lambda Q/16 sigma3 (`exx/`) at the occupations of the uniform-gas ground state, started from it
  (since 2026-10-16: with aufbau occupations the variant of N2352_lamp1_a00 has no self-consistent closed-shell
  solution, a level crosses the Fermi level; the column `occupations_are_aufbau` and the information check
  `exx_variant_occupation_order` name the states whose kept occupations are not the variant's own aufbau order).
* **Self-consistency:** Anderson (Pulay) mixing of the potential vector (depth 6, beta = 0.4), stopped when
  max |residual| <= 1e-11 m. Safeguards: backtracking when a level solve fails, a divergence abort, and a
  coupling continuation (lambda/4 ... lambda) as fallback. The exact-Fock variant falls back to a
  continuation in the weight of its exact-Fock term instead. The Mermin states use the same coupling
  continuation as fallback. No fallback was needed in the canonical matrix (all 75 ground and 135 thermal paths
  "direct", at most 29 ground iterations; `ground/summary.csv`, check `thermo_scf_path`). The four a4 neighbours of
  the finite differences d/da4 are converged to scf_tol/10 (1e-12 m canonical): the difference quotient amplifies
  their SCF error by ~1/delta.
* **Occupations:** at T = 0 the aufbau with exact degeneracy groups (open shells are flagged). The first
  excited state is the ensemble Delta-SCF: one particle moved from the highest occupied group to the lowest
  empty group, uniformly over each group, so the block and direction symmetry of the reduction is kept. At
  T > 0 the Mermin occupations are used, with mu fixed by sum g f = N.
* **The Mermin root (`src/mermin.rs`):** mu is the root of a well-conditioned residual, not of the direct
  count sum g f - N. About a split S of the levels (a prefix in energy order), sum g f - N = P - Hl - d exactly,
  with P = sum_{i not in S} g f(x_i) the thermal particles above the split, Hl = sum_{i in S} g f(-x_i) the
  thermal holes below it (each hole factor computed directly as f(-x), never as 1 - f), and d = N - sum_S g
  exact; x_i = (eps_i - mu)/T. The split starts at the T = 0 filling and is moved to {eps < mu} when the root
  lies outside its gap (at most 2 passes were needed in the matrix). Canonical form `LogBalance`:
  ln(P + d-) - ln(Hl + d+), d+- = max(+-d, 0), each sum a log-sum-exp so that nothing underflows; safeguarded
  Newton in a sign bracket, then bisection down to adjacent doubles. The refined run uses `LinearDeviation`, the
  exactly equivalent (P - Hl) - d summed in descending level order and solved by bisection, so the two runs
  reach the root by different rounding paths. Rounding bound of mu (first order in eps_mach = 2^-52, derived in
  the module documentation of `src/mermin.rs`, one formula with generous constants for both forms):
  eps_mach [(n + 2 + L) (P + Hl + |d|)/(dN/dmu) + 3 <|eps - mu|> + T (ln g_max + 3) + 2 |mu|], with n the number
  of levels, <.> the mean weighted with g f (1 - f), g_max the largest degeneracy and L = max(|ln(P + d-)|,
  |ln(Hl + d+)|). Its pieces: the rounding of the arguments x_i = (eps_i - mu)/T (eps_mach <|eps - mu|>), the log
  domain of `LogBalance` (2 eps_mach <|eps - mu|> + eps_mach T (ln g_max + 3)), the summation, the logarithms
  and the shift ((n + 2 + L) eps_mach (P + Hl + |d|)/(dN/dmu), about (n + L) eps_mach T), and the two adjacent
  doubles at the root (2 eps_mach |mu|). The former direct count has eps_mach [(n + 2) N/(dN/dmu) + ...] with the
  same remaining terms: it missed the root by 8.267e-10 m in the activated state N8_lamm1_a00_T10
  (dN/dmu = 1.24e-6; found by the cross-check, see History below). `thermodynamics.csv` records dN/dmu, this
  bound (`mu_rounding_bound`) and, as a DIAGNOSTIC for the negative control of the refined comparison, the root of
  the former direct count on the same final levels minus mu (`mu_direct_count_minus_mu`) for every state.
* **Particle number:** N = sum g f over both fold conditions is the particle number of the cell (the two halves
  z < pi/2 and z > pi/2 joined at the fold); each half holds N/2. Note: ks-theory.json thermodynamics.occupation
  writes "sum w g f = N". That line is inconsistent with its own densities.total, energy and grand potential; the
  solver follows the latter, and records the discrepancy in `parameters.json`.
* **Energy-momentum tensor:** rho = sum w g f eps n_o - e_int, p3 = sum w g f (kappa|k|/3) t_o + e_int,
  p_t = e_int, p0 = sum w g f [(eps - v) n_o - M s_o - kappa |k| t_o] + e_int (ks-theory.json emt). For the
  exact-Fock variant, p0 gets -w_Q q_o inside the sum (the orbital identity holds with kappa k replaced by
  kappa k + j w_Q, and e_int stays homogeneous of degree 2). Identities: 2 Vol_7 int e^{3Hy} rho dy = E_KS and the
  y-conservation p0' + 3H (p0 - p_t) = 0, i.e. (e^{3Hy} p0)' = 3H e^{3Hy} p_t (p3 does not enter: 3-space has no warp
  along y). At lambda = 0 the fold-band states have p0 = p_t = 0 and p3 = rho/3 exactly.
* **History and adiabaticity:** a4 = A H x4 with A = 1 and b4 = b4(0) e^{beta a4} with beta = 4/3 and b4(0) = 1
  (ks-theory.json `adiabaticity.historyBeta`, read by the solver; SPEC section 1), slices a4,0 in {0, 0.5, 1, 1.5, 2}.
  This history is a PRESCRIBED test-field background without back-reaction: with the author's weights the a4 and b4
  equations of SPEC section 5 allow it only with the x0-independent source of
  `Revision/field_equations_a4/a4-equations.json` (exponentialHistory.authorWeights.historySource_kappaT_minus_Lam, a
  function of kk = e^{(2/3) H x4} with p0 = p_t), which the Kohn-Sham gas (it depends on x0) does not supply
  (`Revision/field_equations_a4/reports/ks-source-conditions.json`). ks-theory.json carries this label
  (`adiabaticity.history` ends "PRESCRIBED BACKGROUND (see historyStatus)", `adiabaticity.historyStatus`); the
  solver refuses a ks-theory.json without it or without `historyBeta` and copies them into `parameters.json` and
  `adiabatic/history.json`.
  The measure is Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 for n occupied and m empty in the same
  (shell, j, fold condition), with d_a h = -j kappa k sigma3 + (1 - beta/2) T_j + j (d_a M_eff) sigma2 + d_a v_v
  (+ d_a w_Q sigma3), T_j = j(-(i/f) sigma1 d_y) the kinetic term (f = e^{(beta/2 - 1) a4}): its matrix elements follow
  from the eigen-equation, T_j chi_m = (eps_m - v - j M sigma2 - (j kappa k + w_Q) sigma3) chi_m, without derivatives
  of the orbitals. The self-consistent derivatives come from the states at a4 +- delta and +- 2 delta
  (delta = 2e-3, fixed occupations, Richardson); along the history kappa, f and Vol_7 change. The energy changes as
  dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0 = -3 P3 + P_t + P0/3, P = 2 Vol_7 int e^{3Hy} p dy
  (ks-theory.json emt.energyChange). Changes of the aufbau occupation between slices are flagged as Fermi-level
  crossings, and the adiabatically continued state (the a4,0 = 0 labels) is then solved.
* **Rescaling identity (exact, solved independently):** KS(a4,0; H, L, dk, v_t, lambda) = KS(0; H/f0, f0 L,
  dk e^{-a4,0}, v_t e^{(3 beta/2 - 3) a4,0}, lambda), f0 = e^{-a4,0/3}: the partner is solved on its own grid with the
  same number of RK4 steps (node i at Y = f0 y_i), and its levels, occupations, energy and proper profiles at
  corresponding points equal those of the slice (ks-theory.json rescalingIdentity).

## Parameters and calibration (`results/parameters.json`)

H = 1, m = 1, L = 3, dk = 0.25, v_t = 1, Vol_7(a4,0) = ell^3 v_t e^{(2 beta - 1) a4,0} (beta = 4/3), f(a4,0) =
e^{-a4,0/3}, kappa(a4,0) = e^{-a4,0}, tip theta = 0.

* **Particle numbers:** N = 8 (the k = 0 zero modes); N_large = 2352, the largest closed shell of the free a4,0 = 0
  aufbau below the bulk edge 1.2923 m (the fold band eps = k reaches k = 1.29, it fills the shells up to n2 = 26);
  N_mid = 592, the closed shell nearest N_large/4. (Record of 2026-10-15: 688 and 136; there kappa = e^{-Hy - a4} made
  the brane band rise faster.)
* **Couplings, per N:** lambda_1, lambda_2 = 0.1 m and 0.3 m divided by the largest first-order mean-field
  potential per unit lambda (lambda_hat) of the free ground states over ALL slices, rounded to 4 digits:
  lambda_1 = 157.7, 2.131, 0.5363 and lambda_2 = 473.1, 6.393, 1.609 for N = 8, 592, 2352.
* **Why the whole history:** the potential per unit lambda (proper densities, e^{-3Hy}/Vol_7(a4,0)) falls along the
  history: N = 8: 6.342e-4, 5.883e-4, 4.755e-4, 3.428e-4, 2.251e-4; N = 592: 0.04693, 0.04353, 0.03519, 0.02537,
  0.01665; N = 2352: 0.1864, 0.1730, 0.1398, 0.1008, 0.06617 at a4,0 = 0, 0.5, 1, 1.5, 2: the cell volume grows like
  e^{(5/3) a4,0} while the fold-band orbitals e^{f M y} spread toward the tip as f shrinks; the maximum lies at
  a4,0 = 0. The proper density of a fold-band orbital is ~ e^{(2 f M - 3H) y}, largest at the tip for 2 f M < 3H.
* **Temperatures:** T in {0.01, 0.02, 0.05} m, for N in {8, 592, 2352}, lambda in {0, +-lambda_1}, all five
  slices.

## Outputs (`Revision/kohn_sham/results/`, deterministic: LF, 16 significant digits, no paths or timings)

| file | content |
| --- | --- |
| `parameters.json`, `manifest.json` | parameters, calibration, conventions; SHA-256 of every file (243 files) |
| `spectrum/` | analytic k = 0 spectra (columns m, L, a4, f), fold-band slope per slice, band and bulk levels vs k, the tip-angle boundary identity (`tip-angle.csv`), closed shells per slice |
| `ground/summary.csv`, `ground/runs.json` | 75 ground states: E_KS, HOMO, LUMO, KS gap, potentials, SCF history |
| `ground/levels/<id>.csv`, `ground/profiles/<id>.csv` | levels with labels and occupations; proper profiles n, S, Q, M_eff, v_v, e_int, rho, p3, p_t, p0 at y = -3 + 0.02 i |
| `ground/emt-integrals.csv` | 2 Vol_7 int e^{3Hy}(rho, p3, p_t, p0, n) dy, fold (`_brane`) and tip values, identities |
| `excited/summary.csv`, `excited/particle-hole/<id>.csv` | KS gap, Delta-SCF, the 24 lowest particle-hole excitations |
| `adiabatic/` | Q_max per state, Fermi-level crossings, continued states, crossing demonstration (N = 2360) |
| `rescaling/rescaling.csv` | the exact rescaling identity, solved independently (columns partner_H and partner_L added) |
| `exx/exact-fock-variant.csv` | uniform-gas vs exact-Fock exchange (column occupations_are_aufbau added) |
| `thermo/thermodynamics.csv` | 135 Mermin states: mu, E, S, F, Omega (two forms), C_V = T dS/dT, dE/dT, -dF/dT, sea-hole diagnostic, dN/dmu, the rounding bound of mu and the former direct-count root minus mu (`dN_dmu`, `mu_rounding_bound`, `mu_direct_count_minus_mu`) |

Run ids: `N<N>_<lam0|lamp1|lamm1|lamp2|lamm2>_a<10 a4,0>` (`_T<1000 T>` for thermal states).

Outside `results/`: `tools/mermin-roots-40digit.json` (the 40-digit fixture of the Mermin root, written by
`tools/mermin_roots_mp.py`) and the reports `ks-rust-solver.json`, `ks-rust-mermin-roots.json` and
`ks-rust-determinism.json` in `Revision/kohn_sham/reports/`.

## Checks

`Revision/kohn_sham/reports/ks-rust-solver.json` holds 45 checks, all PASS (42 validations and the information
items `thermo_scf_path`, `exx_variant_occupation_order` and the sea-hole diagnostic). Per-run checks are aggregated,
with the worst case and its run id.

* **Theory and algebra:** `theory_input_metric_forms` (the corrected forms of ks-theory.json), coefficients, gamma
  fixture, block reduction.
* **Free field:** analytic k = 0 spectra of both fold conditions with the factor f (at f = 1 and f = e^{-1/2}; error
  7.2e-10 m below 4 m, O((f h eps)^4)), the exact zero mode e^{f M y} at a4,0 = 0 and 2, the fold-band slope
  c = e^{-a4,0} at every slice (to 2.1e-16), block-type symmetries, branch labels, the tip-angle boundary identity
  (`free_tip_angle_boundary_identity`: (eps_theta - eps_0) int chi_0^dag chi_theta dy = -j a_0(-L) b_theta(-L)/f to
  1.1e-12; the fold band shifts by at most 3.3e-2 m between theta = 0 and 1, the extended level by at least 6.2e-2 m:
  kappa does not grow toward the tip), the free rescaling relation eps(k, a4,0; L) = eps(k e^{-a4,0}, 0; f0 L) (to
  1.3e-15) and the exact fold band eps = kappa k.
* **Every state:** SCF convergence, N conservation (sum g f and the density integral), fold boundary residuals, the
  two energy forms, the EMT energy integral, nabla_mu T^mu_y = 0 (integrated and pointwise, 5.2e-10), the derivative
  form of the y-kinetic term with the factor f (an orbital-equation residual, 2.6e-10), window completeness, closed
  shells.
* **Along the history:** dE/da4 = -3 P3 + P_t + P0/3 against Richardson differences (worst 9.2e-10 of the energy
  scale); Hellmann-Feynman d eps/da4 = <d_a h> with the kinetic term (6.4e-11 m); the exact rescaling identity with
  H/f0 and f0 L, solved independently (levels to 1.6e-13 m, energies and profiles to 8.2e-13).
* **Excited states:** Delta-SCF = KS gap at lambda = 0.
* **Exact-Fock variant:** convergence at the kept occupations, y-conservation, and the information
  `exx_variant_occupation_order` (2 of 60 states keep occupations that are not their own aufbau order:
  N2352_lamp1_a00 and N2352_lamp2_a00).
* **Thermodynamics:** Omega in two forms; C_V = T dS/dT = dE/dT and -dF/dT = S. Both are Richardson
  differences, compared within 1e-4 relative plus the noise floor N x root tolerance / dT of a difference
  quotient of energies. Also the window cut and the shells beyond the window.
* **The Mermin root:** `thermo_mu_well_conditioned_root`: in all 135 thermal states mu equals the `LogBalance` root
  on the final levels bit for bit; `LogBalance` and `LinearDeviation` agree within the larger of their rounding
  bounds (max difference 2.914e-16 m, max ratio to the bound 0.196, largest bound 9.43e-14 m; at most 2 split
  passes). `thermo_mu_vs_40digit_roots`: on the 8 states of the fixture both forms lie within their bounds of the
  40-digit roots (largest ratio 0.006), `LogBalance` reproduces the recorded mu bit for bit; the former direct count
  misses these roots by at most 1.682e-13 m (1.8 times the largest new bound): no state of the corrected record
  exhibits the defect of the former method, whose negative control is therefore the synthetic unit test
  `direct_count_negative_control` (2^30 levels deep below mu and one near it: the direct count misses the closed-form
  root by 5.7e-9 m, the new forms are within 9.5e-17 m).
* **Crossing-flag demonstration, and the T3 solver self-test.** The self-test solves (m, lambda, tip 0) and
  (-m, lambda, tip pi) independently and gets equal levels, E and EMT integrals and opposite S, to 3.6e-13;
  the untransformed tip is the negative control. It is NOT a proof of T3, which is owned by
  `Revision/pairing/kohn_sham`.

`Revision/kohn_sham/reports/ks-rust-mermin-roots.json` (5 checks, all PASS; `tools/mermin_roots_mp.py`): all
135 `single --mermin-levels` runs completed; the 40-digit and 50-digit roots agree to 1.5e-38 (relative); the
solver's mu lies within its rounding bound of the 40-digit root on its own levels in 135 of 135 states (largest
|mu - root| 2.868e-16 m, N592_lamp1_a20_T50; largest ratio to the bound 0.089, N2352_lamp1_a00_T10); the mu of every
`single` run equals the committed matrix; the fixture holds the 8 states with the largest direct-count bound.

`Revision/kohn_sham/reports/ks-rust-determinism.json` covers the repeat (byte identity of all files) and the
refined-tolerance run (RK4 steps x 2, root tolerance / 10, SCF tolerance / 10, thermal cut / 100, and the
Mermin root in the form `LinearDeviation` instead of `LogBalance`). Its tolerances were fixed before the
comparison: eigenvalues 1e-8 m, energies 1e-8 relative, profiles 1e-6, thermodynamics 1e-8, derived
derivatives 1e-6. Because the two runs solve the Mermin root along different rounding paths, |canonical -
refined| of mu and Omega contains the rounding error of the root instead of sharing it (check
`refined_mermin_root_path`; `refined_thermodynamics` compares both forms of Omega). Results of 2026-10-16:
`ks-rust-determinism.json` 14/14. The repeat (three parts with `--inner-threads 2`, assembly with 3, against the
canonical two parts with 4) is byte-identical in all 244 files (8695824 bytes) and in its report. Refined against
canonical: E_KS to 1.8e-11 relative (N8_lamp2_a00); HOMO, LUMO and gaps to 2.2e-12 m; 50420 levels label by label to
5.7e-10 m, label sets and occupations identical; Delta-SCF to 4.4e-9 m; profiles to 2.0e-10 of their family's maximum
(the measure was changed from the profile's own maximum, see `claude_failures.md` H9); Q_max and dE/da4 to 4.5e-8;
thermodynamics (mu, E, F, both forms of Omega, S) to 1.9e-10; C_V to 3.9e-9; the analytic spectra converge with the
error ratio 16.00 (RK4). The Mermin root along the two rounding paths: U_mu <= 1.020e-11 m and U_Omega <= 9.877e-9
(N2352_lamm1_a00_T50); largest B_c + B_r 2.380e-13 m; the negative control passes in the one state where the former
direct-count root would be off by more than 2 U_mu (N8_lam0_a00_T10, -1.682e-13 m).

## Canonical results (from `results/`; units m = H = 1)

* **lambda = 0 is a fold-band gas.** Every occupied level of N = 8, 592 and 2352 lies on the fold band chi =
  (e^{f M y}, 0), eps = e^{-a4,0} |k|: E_KS = 0 (N = 8; the zero modes), 361.1161, 132.8472, 48.87176 (N = 592) and
  2288.388, 841.8510, 309.6997 (N = 2352) at a4,0 = 0, 1, 2, i.e. exactly e^{-a4,0} times the slice-0 value; the KS
  gap of N = 8 is the n2 = 1 band level e^{-a4,0} dk = 0.25, 0.09197, 0.03383. The pressures are exact: int p3 /
  int rho = 1/3 (N = 592 and 2352; the zero modes of N = 8 carry no energy-momentum at all) and p0 = p_t = 0 pointwise (the hidden kinetic pressure (eps - v) n_o - M s_o - kappa k t_o vanishes
  on these orbitals, e_int = 0). (Along the prescribed history, without back-reaction: equations of state derived
  from it are not consequences of the coupled field equations.)
* **With the interaction:** E_KS of N = 8 with lambda_2 is -0.1109816, -0.04272548, -0.02085244 at a4,0 = 0, 1, 2
  (a pure interaction energy; Delta-SCF 0.2499329 against the gap 0.2499331 at a4,0 = 0); N = 592 with lambda_2:
  352.7980 and 47.32640, N = 2352: 2255.044 and 303.5549 at a4,0 = 0 and 2. The interaction makes p0 and p_t nonzero:
  int p0 / int rho = -0.0189, -0.0392 and int p_t / int rho = -0.0078, -0.0107 (N = 592, lambda_1, a4,0 = 0 and 2);
  int p3 / int rho = 0.328, 0.326.
* **Adiabaticity:** Q_max <= 0.198 over the whole matrix (N2352_lamm1_a00, the fold-band level of the Fermi shell
  n2 = 26 -> the first bulk level of the same sector), so the adiabatic approximation is only marginal at the Fermi
  edge of N_large. For N = 8, Q_max = 0.068 already at lambda = 0 (before: 0): the shrinking hidden length (the
  kinetic term (1/3) T_j of d_a h) couples the zero mode to the bulk levels of k = 0.
* **Fermi-level crossings:** none occur in the canonical matrix. Demonstration at lambda = 0, N = 2360 (the first
  closed shell that occupies a level off the fold band): the k = 0 bulk level is emptied along the history (it
  rises as sqrt(M^2 + (n pi/(f L))^2)) while the fold band redshifts; the adiabatically continued state lies 4.68 m
  (a4,0 = 0.5) to 12.48 m (a4,0 = 2) above the instantaneous aufbau state.
* **Exact Fock vs uniform-gas exchange:** for N = 8 (b = 0 zero modes, Q = n) the exact Fock exchange cancels the
  interaction: E_EXX = 2.7e-14 against E_LDA = -0.1110 (lambda_2, a4,0 = 0). For N = 592 and 2352 the functionals
  differ by Delta E_x (33.25 of E = 2255.04, N = 2352, lambda_2, a4,0 = 0; 6.130 of E = 303.55 at a4,0 = 2);
  E_EXX - (E_LDA + Delta E_x) is at most 4.0% of Delta E_x (second order).
* **Thermal sea holes (diagnostic of the convention):** the excluded sea would carry more than 1% of N in 27 of
  the 135 thermal states, from a4,0 = 0.5 on; the largest is 594.5 N (N8_lamp1_a20_T50: at a4,0 = 2 the sea fold band
  -e^{-2} |k| lies within a few T of mu). There the particle-only Mermin ensemble is outside its range of
  validity, and a thermal treatment of the Dirac sea (pairs) would be required.

## What this does not establish (OPEN or ASSUMED)

* **Non-adiabatic evolution:** the states are instantaneous (adiabatic) Kohn-Sham states; Q_max reaches 0.198 at
  the Fermi edge of N_large, so the adiabatic approximation is not uniformly good there; the time-dependent problem
  is OPEN.
* **Assumed fold convention and the cutoff:** filling both fold conditions is ASSUMED (the boundary form fixes the
  condition only up to theta). The regular tip at L = 3 is a cutoff choice: kappa is constant in y, so the extended
  levels depend on L like those of a box of proper length f L, and the proper densities of the fold-band orbitals
  grow toward the tip like e^{(3H - 2 f M)|y|}; the interacting results depend on L
  (`Revision/kohn_sham/tip_convergence`).
* **Filling convention:** the particle/sea split and the zero-mode convention are CONVENTIONS whose
  justification is OPEN. The thermal sea is excluded (diagnostic above).
* **Exchange and correlation:** the exact-Fock functional is exact only for the closed-shell determinants
  of ks-theory.json, and no correlation is included; the exact-Fock variant is solved at the uniform-gas
  occupations (2 states are not aufbau-ordered with them).
* **Delta-SCF:** the excited state is an ensemble over degenerate groups, not a symmetry-broken single
  determinant.
* **The history** is a prescribed background (above).

## Timings (this machine, 22 threads, 2026-10-16)

* Canonical matrix in one invocation (`all`, no cache, inner threads 4; build/revision scratch): 284.5 s (free spectra
  and closed shells 2.2 s, calibration 1.2 s, ground matrix 165.7 s, history 0.7 s, thermodynamics 113.6 s, T3
  self-test 1.1 s). The first such run (before the exact-Fock change and the inner parallelism) took 394.6 s.
* Canonical matrix in parts (the record): part 1/2 134.6 s, part 2/2 130.5 s, assembly 5.4 s;
  `tools/mermin_roots_mp.py` 18.3 s (135 `single` runs 16.1 s, 40-digit roots 2.2 s); the assembly again 5 s (results
  byte-identical, the report differs only by the fixture's sha256 when the fixture changed; here the fixture was
  unchanged).
* Repeat in three parts: 76.9 s, 73.0 s, 84.7 s; assembly 6 s.
* Refined-tolerance run (G = 1800, root tolerance 1e-14, SCF tolerance 1e-12, thermal cut 1e-14, Mermin form
  `LinearDeviation`) in four parts: 152.5 s, 147.8 s, 156.0 s, 125.9 s; assembly 11.3 s.
* `cargo test --release`: 13 of 13, below 1 s.

## The corrected metric (2026-10-16)

On 2026-10-16 the author released the recomputation with the corrected primordial metric (`HANDOFF.md` 0.10, phase
W5). What changed, and why:

* **Theory** (`Revision/kohn_sham/theory`, ks-theory.json; `theory/WOLFRAMSCRIPT_PROVENANCE.md` section 6.8): the
  hidden direction carries the scale f = e^{-a4} b4^{1/2} (in the y chart dy is multiplied by f), the extra times f
  e^{Hy}, 3-space e^{a4} without warp; sqrt|g| = e^{-a4} b4^2 e^{3Hy}; kappa = e^{-a4} is constant in y; the half-density
  ansatz is e^{-(3/2)Hy} e^{a4/2} b4^{-1}; the block equation chi' = f N chi; the fold joins two halves of a cell (the
  Z2 orbifold of the metric of 2026-10-14 is gone); y-conservation p0' + 3H (p0 - p_t) = 0; dE/da4 = -3 P3 + P_t +
  P0/3; the rescaling identity changes H and L; c = e^{-a4,0}. Wolfram 51/51, sympy 61 checks.
* **Solver:** `src/model.rs` (`Physics::fh`, Vol_7 = ell^3 v_t e^{(2 beta - 1) a4,0}, `coord_cell`), `src/shoot.rs` (the
  factor f in the ODE, the Pruefer derivative and the profiles; the grid carries e^{3Hy}, no e^{-Hy}), `src/scf.rs`
  (P = e^{-3Hy}/Vol_7, kappa constant; the sectors in parallel), `src/analysis.rs` (the y-conservation, the history
  identity, the trace identity with f, d_a h with the kinetic term), `src/spectrum.rs` (the exact checks with f, the
  tip-angle boundary identity, the rescaling relation with f0 L), `src/runs.rs` (the rescaling partner on its own
  grid, the exact-Fock variant at the kept occupations, the parameters, the job cache), `src/theory.rs` (the slope key
  `braneBandSlope_a0`, `theory_input_metric_forms`), `src/cache.rs` (new), `src/main.rs` (`--cache`, `--part`,
  `--inner-threads`, `--coordinate-cell`); `src/mermin.rs` only in its tests. `cargo test` 13/13.
* **What changed in the numbers:** everything, because the momentum weight no longer grows toward the tip and the
  density factor is e^{-3Hy} instead of e^{-6Hy}: N_mid = 592 and N_large = 2352 (before 136 and 688), lambda_1 =
  157.7, 2.131, 0.5363 (before 0.01946, 0.01206, 0.006645), the lambda = 0 states are exact fold-band gases, the fold
  band slope is e^{-a4,0} (before 1.905 e^{-a4,0} at M = H = 1, L = 3), and the tip-angle insensitivity of the former
  record is replaced by an exact boundary identity (the levels do depend on the tip condition).
* **Failures on the way** (`claude_failures.md`, section H): the first one-invocation run took 394.6 s and the
  exact-Fock variant of N2352_lamp1_a00 did not converge with aufbau occupations (H3), the first tip-angle bound was
  an approximation (H5), the rescaling profile measure divided round-off by round-off (H6), and the data-dependent
  negative control of the 40-digit fixture had no defective state left (H8).

## History of the Mermin root (the record of 2026-10-02 to 2026-10-15)

How the uncertainty measure of mu and Omega was made sensitive to the rounding of the root (the error class that
the cross-check found and that the former measure could not show):
1. Different rounding paths: the canonical run (and `single`) solves the root in the form `LogBalance`, the
   refined run (and `single --refined`, which `Revision/kohn_sham/checker/measure_rust_refinement.py` uses) in
   the exactly equivalent form `LinearDeviation`. A rounding error of one root therefore enters |mu_c - mu_r|
   instead of cancelling in it; the former direct count gave both runs the same rounding (their levels differ too
   little to change it).
2. The rounding bound of each root is added: U_mu = |mu_c - mu_r| + B_c + B_r and
   U_Omega = |Omega_c - Omega_r| + N (B_c + B_r) (B = `mu_rounding_bound` of each run; dOmega/dmu = -N at fixed
   levels). The bound is validated against 40-digit roots in all 135 states (`ks-rust-mermin-roots.json`), in the
   solver check `thermo_mu_vs_40digit_roots` and in the unit test `mermin::tests::forty_digit_roots`.
3. A live negative control in `refined_mermin_root_path`: from the column `mu_direct_count_minus_mu` of both runs
   it evaluates the former measure (direct count in both runs) and requires that it stayed below half of the
   former error wherever that error exceeds 2 U_mu (the shared rounding that hid the defect), and that the present
   refined run differs from a former canonical root by at least half of it there.

History of that comparison: the first refined comparison, made with G = 600, failed two checks.
1. The highest (empty) bulk levels of the label sets, near 5.6 m, differed by up to 1.08e-8 m (RK4 error).
2. C_V, then taken as dE/dT, differed by 1.8e-4 relative in the activated N = 8, T = 0.01 states, where
   dE/dT is a noise-limited difference quotient.

The tolerances were kept. Instead, the canonical resolution was raised to G = 900, and C_V is reported as
the well-conditioned T dS/dT (dE/dT is kept for the identity check).

3. The Mermin root (wave 1b). The full cross-check against the independent reference
   (`Revision/kohn_sham/reports/ks-crosscheck.json`, check `thermo_state_functions`) failed in N8_lamm1_a00_T10:
   the solver then found mu by bisection on the direct count sum g f - N, which fixes mu only to
   eps_mach N/(dN/dmu), and there mu was 8.27e-10 m from the root of its own levels. The refined comparison
   could not show it, because both runs used the same direct count and so shared its rounding error. The root
   was rewritten (`src/mermin.rs`, Method above), the refined run was given
   the second form, and the check `refined_mermin_root_path` was added: max |mu_c - mu_r| 1.254e-12 m
   (N136_lamm1_a00_T20), max |Omega_c - Omega_r| 2.738e-10 (N688_lamm1_a00_T20); with the rounding bounds added,
   U_mu <= 1.255e-12 m and U_Omega <= 2.753e-10 (largest B_c + B_r 1.149e-13 m). The old canonical mu against
   the new refined run differs by 8.271e-10 m (Omega by 6.617e-9) in N8_lamm1_a00_T10, so the new measure would
   have exposed the defect; the live negative control of `refined_mermin_root_path` shows the same from the
   current runs: for N8_lamm1_a00_T10 the former measure (direct count in both runs, -8.267e-10 and -8.271e-10 m
   from the well-conditioned roots) is 5.8e-16 m, the present refined run against a former canonical root
   8.271e-10 m (likewise N8_lam0_a00_T10: former measure 7.5e-13 m against an error of 2.722e-10 m;
   N8_lamp1_a00_T10: 7.5e-13 m against 6.959e-11 m). Changes of the committed numbers (old, commit 70fab64 ->
   new): mu of N8_lamm1_a00_T10 0.2100104489071649 -> 0.2100104497339036, of N8_lam0_a00_T10
   0.2098737766593366 -> 0.2098737763871040, of N8_lamp1_a00_T10 0.2097333312113810 -> 0.2097333311417908; Omega
   (both forms) of these three states by -6.614e-9, +2.178e-9 and +5.567e-10 (N8_lamm1_a00_T10:
   -1.679096748762439 -> -1.679096755376349); every other mu change is at most 4.0e-13 m and every other Omega
   change at most 1.6e-11 absolute (within the SCF tolerance). The quantities derived from mu changed with it:
   the thermal window cut by up to 9.48e-10 m (N8_lam0_a00_T10, 0.7361839880842111 -> 0.7361839890319382; it is
   placed from the free mu) and f at the cut by up to 1.2e-7 relative; E by at most 9.1e-12 absolute (relative
   2.7e-8 only in N8_lam0_a00_T10, where E = 2.646e-9: 2.646041051066313e-9 -> 2.646040979032455e-9); S by at
   most 1.3e-10 absolute (2.0e-9 relative); F by at most 8.5e-12 absolute (relative 5.7e-7 only in
   N8_lam0_a00_T10, where F = -1.229e-10); C_V = T dS/dT by at most 8.7e-9 relative; the noise-limited
   difference quotients dE/dT and -dF/dT by up to 5.3e-8 absolute (6.8e-6 relative in N8_lamp1_a00_T10,
   -dF/dT 2.750519551341623e-7 -> 2.750500821749093e-7); the sea-hole diagnostic by at most 8.3e-8 relative;
   the final SCF residuals, |M_eff - m|, |v_v| and N_check in the last digits. Ground, excited, adiabatic,
   spectrum, rescaling and exact-Fock outputs are unchanged (byte-identical except the history label of
   `adiabatic/history.json`). In the verification pass of 2026-10-07 the rounding bound was re-derived to first
   order for both forms: the former (n + 2) eps_mach (P + Hl + |d|)/(dN/dmu) + 2 eps_mach |mu| omitted the
   rounding of the arguments x_i and the log domain of `LogBalance`; the bound is now the formula of Method
   above, so every `mu_rounding_bound` grew, by a factor 1.007 (N688_lamm1_a20_T50) to 2.85 (N8_lam0_a00_T10:
   1.087e-16 -> 3.095e-16 m), and the column `mu_direct_count_minus_mu` was added; mu and every other number of the matrix are unchanged by that
   pass.

## The author's coordinates x0..x7 (2026-10-14)

On 2026-10-14 the Revision record was relabelled to the author's coordinates {x0, x1, ..., x7} (x0 = the hidden
direction, listed first; before: x1..x8 with the hidden direction x8 listed last). `Revision/algebra/gammas.json` now
lists gamma^(xk) = T16[k] at index k with eta = (1, 1, 1, 1, -1, -1, -1, -1). The solver was changed accordingly:
`src/theory.rs` takes g0 = gamma^(x0) = `g[0]`, g1 = `g[1]`, g4 = `g[4]` and C = g0 g1 g2 g3 (before: `g[7]`, `g[0]`,
`g[3]` and `g[7] g[0] g[1] g[2]`, which are the same matrices in the old order) and checks the new eta; the
hidden-direction pressure p8 is now named p0 (`analysis.rs`, `runs.rs`, `scf.rs`: profile column `p0`, CSV columns
`int_p0`, `p0_brane`, `p0_tip`, JSON key `p0`; `tools/compare_runs.py`). The physics is unchanged.

Runs of 2026-10-14 (22 threads; other jobs of this work shared the machine): canonical matrix 75 s (ground matrix
33.0 s, thermodynamics 35.0 s) and, after a one-word change of the description, 78 s; repeat 77 s; refined-tolerance
run alone 328 s (ground matrix 146.0 s, thermodynamics 169.8 s; 618.6 s before, when it ran in parallel with the
repeat); `tools/mermin_roots_mp.py` 9 s; `cargo test --release` 10 of 10. Every result file equals the one of
2026-10-08 after the renaming p8 -> p0, except `parameters.json` (the description names the author's coordinates; the
sha256 of `ks-theory.json` and of `gammas.json`); the manifest lists the new hashes of the 78 renamed files. The
report `ks-rust-solver.json` differs only in the first 16 hex digits of these two sha256 values. The repeat is
byte-identical in all 244 files and its report; `ks-rust-determinism.json` (14 of 14) differs from the one of
2026-10-08 only in the byte total of the compared files (5857843 instead of 5857791: the longer description).

## The metric with b4(x4) (2026-10-16, withdrawn the same day by the corrected metric)

On 2026-10-15 the author ordered "move everything to b4(x4); b4 is never 1" (`HANDOFF.md`, section 0.9, phase 4).
The record above is the one of the author's metric with b4(x4) on the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4}.
What changed, and why:

* **Theory** (`Revision/kohn_sham/theory`, ks-theory.json): every statement is derived for general a4(x4) and b4(x4).
  gamma^mu Omega_mu = 3H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4); the ansatz carries the half-density factor b4^{-3/4}
  and removes both terms, so the slice Hamiltonian does not contain b4; sqrt|g| = b4^{3/2} e^{6Hy}; the densities are
  per proper 7-volume ell^3 v_t b4^{3/2} (in units of b4(0)^{3/2}: Vol_7(a4,0) = ell^3 v_t e^{(3/2) beta a4,0}, coupling
  lambda_hat = lambda b4(0)^{-3/2}); nabla_mu T^mu_x4 = -d_x4 rho - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t), so
  dE/da4 = -3 (P3 - P_t) - (3/2) beta P_t on the history; the rescaling partner of slice a4,0 is slice 0 with
  dk e^{-a4,0} and v_t e^{(3 beta/2 - 3) a4,0}. Wolfram `verify_ks_theory.wls` 51/51 (34.8 s; 46 checks before),
  sympy `check_ks_theory.py` 63/63 (49 s; 58 before).
* **Solver:** `Physics.beta` (read from ks-theory.json `adiabaticity.historyBeta`) and Vol_7(a4,0) in `src/model.rs`;
  the history identity in `src/analysis.rs`; the rescaling partner, the parameters, the thermal continuation
  fallback (`solve_with_continuation`, check `thermo_scf_path`), the a4 neighbours converged to scf_tol/10 and the
  key `beta` of `adiabatic/history.json` in `src/runs.rs`; `single --beta` in `src/main.rs`. `cargo test` 10/10.
* **What changed in the numbers.** The calibration rule is unchanged; applied to the new history it gives
  lambda_1 = 0.01946, 0.01206, 0.006645 and lambda_2 = 0.05838, 0.03617, 0.01993 (N = 8, 136, 688; before 0.01946,
  0.0009298, 0.0001846 and 0.05838, 0.002789, 0.0005538). So every interacting state with N = 136 or 688 changed, and
  every interacting state with N = 8 at a4,0 > 0 (its effective coupling now falls like e^{-2 a4,0}). The lambda = 0
  states keep their levels, energies and integrals; their profiles are per Vol_7(a4,0) and therefore e^{-2 a4,0}
  times the former ones. The N = 8 interacting energies fall like e^{-2 a4,0} (E_KS = -2.863e-3, -4.022e-4, -5.448e-5
  at a4,0 = 0, 1, 2 with lambda_2; before -2.863e-3 at every slice), and Q_max of N = 8 is no longer 0 for lambda != 0
  (at most 0.0039).
* **Two numerical consequences, found by the record's own checks.** (1) With the stronger couplings the direct
  Mermin SCF of N688_lamm1_a00_T10 diverged (residual 0.197 after 400 iterations; first canonical run). The Mermin
  states now use the coupling continuation of the ground states as fallback; it is used for this one state only.
  `single` uses the same path for T > 0 (the Mermin-roots tool failed on this state before). (2) The first refined
  comparison failed `refined_adiabatic_derivatives`: dE/da4 of N8_lamp1_a20 is only 3.632e-5, and the canonical
  difference quotient of energies was 7.0e-11 off (1.9e-6 relative; the refined run agreed with the EMT identity
  to 2e-15). The tolerance (1e-6, fixed before the comparison) was kept; instead the four a4 neighbours are now
  converged to scf_tol/10, and the quotient agrees with the identity to 2.4e-15 (refined comparison: 1.4e-7).
* **Runs of 2026-10-16** (22 threads, otherwise idle machine): canonical matrix 78.0 s (ground matrix 39.1 s,
  thermodynamics 32.4 s); `tools/mermin_roots_mp.py` 8.6 s (135 `single` runs, 135 of 135 within the bound, largest
  |mu - root| 1.639e-16 m, largest ratio 0.149; the fixture holds the same 8 states, with new levels at a4,0 = 0.5);
  the canonical matrix again (results byte-identical, the report differs only by the fixture's sha256 and the
  per-state values of the fixture states); repeat 75.7 s, byte-identical in all 244 files and the report;
  refined-tolerance run 340.6 s (ground matrix 160.6 s, thermodynamics 168.8 s), below the limit of 423 s.
  `ks-rust-determinism.json` 14/14: E_KS to 2.0e-12 relative, HOMO/LUMO/gap to 7.6e-12 m, 23724 levels to
  2.1e-9 m, Delta-SCF 6.5e-11 m, profiles 7.1e-9 of their maxima, Q_max and dE/da4 1.4e-7, thermodynamics 2.5e-10,
  C_V 5.7e-9; U_mu <= 1.310e-12 m (N688_lamm1_a00_T10), U_Omega <= 2.537e-10; the negative control passes in the
  3 N = 8, a4,0 = 0 states (unchanged: their slice is a4,0 = 0).
* **Not yet redone in this phase when this section was written:** the Python reference and the cross-check, the
  tip-cutoff convergence and `checker/measure_rust_refinement.py` (their committed reports describe the record
  before this change until they are rerun); `Revision/dark_sector/dirac16complex/compute/run_ks_history.py` passes
  lambda_eff to `single` and reads the calibrated couplings, so the dark sector is rerun after this phase.
