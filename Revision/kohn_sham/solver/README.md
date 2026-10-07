# Revision Kohn-Sham solver (Rust) — instantaneous states of dirac16complex in the deflating field

New Revision crate (own empty `[workspace]`, no external crates). It implements SPEC section 7 from the
formulas of `Revision/kohn_sham/ks-theory.json` (checked in `Revision/kohn_sham/reports/ks-theory-*.json`).
No code, number or fixture of the old stages is used; `studies/dirac16complex_kohn_sham` was read only to
recall that a shooting method with a Pruefer count suits this problem.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three EXTRA TIMES, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} sin^{1/6} z, a4
increasing); x8 = hidden direction, y = ln(sin z)/(6H) in [-L, 0] (brane y = 0, tip cutoff y = -L).

## Build and run (from the repository root)

```
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
cargo test  --release --manifest-path Revision/kohn_sham/solver/Cargo.toml      # 10 unit tests
B=Revision/kohn_sham/solver/target/release/revision_ks_solver
$B all --out Revision/kohn_sham/results --report Revision/kohn_sham/reports/ks-rust-solver.json   # canonical matrix
python Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work <scratch>/mermin-roots         # 40-digit mu roots
$B all --out <scratch>/repeat  --report <scratch>/repeat-report.json                              # repeat
$B all --refined --out <scratch>/refined --report <scratch>/refined-report.json                   # refined tolerances
python Revision/kohn_sham/solver/tools/compare_runs.py --canonical Revision/kohn_sham/results \
   --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json --repeat <scratch>/repeat \
   --repeat-report <scratch>/repeat-report.json --refined <scratch>/refined \
   --refined-report <scratch>/refined-report.json --report Revision/kohn_sham/reports/ks-rust-determinism.json
$B single --m M --lambda L --a4 A --N N --out FILE.json [--tip-theta TH] [--T T] [--exx] [--margin W]
   [--profiles FILE.csv] [--mermin-levels FILE.json] [--refined]
```

The 10 unit tests are `json::tests::roundtrip`, `model::tests::{r3_values, rounding}`,
`sha256::tests::known_answers`, `shoot::tests::{free_k0_even_spectrum_and_zero_mode,
phi_is_increasing_for_both_block_types}` and the four Mermin-root tests `mermin::tests::{two_level_closed_form,
log_balance_survives_underflow, forty_digit_roots, open_shell_and_repivot}` (see Method, The Mermin root).

`tools/mermin_roots_mp.py` runs `single --mermin-levels` for all 135 thermal states (the option writes the
final levels and mu as shortest round-trip decimals, so the tool reads exactly the solver's doubles), computes
the root of sum g f = N on these levels with mpmath at 40 digits (checked at 50 digits), and writes
`reports/ks-rust-mermin-roots.json` (5 checks) and the fixture `tools/mermin-roots-40digit.json` (the 8 states
with the largest conditioning bound of the former direct count). Its check `single_reproduces_committed_matrix`
compares with the committed `results/thermo/thermodynamics.csv`, so it runs after the canonical matrix. The
fixture is in turn an input of the canonical run (check `thermo_mu_vs_40digit_roots`) and of the unit test
`mermin::tests::forty_digit_roots`: after a change of the solver, run `all`, the tool, and `all` again; on a
reproduction of the committed state every file is byte-identical in one pass.

`all` prints every check as `PASS/FAIL - name: detail` on stderr and `SUCCESS`/`FAILURE` last on stdout
(exit 0/1). `--threads N` (default min(cores, 22)) does not change any output: independent runs are
distributed over threads and merged in a fixed order. `--timing FILE` writes the wall-clock times
(kept outside the results so that two runs are byte-identical). `single` solves one state with chosen
parameters (for example the T3 image problem: `--m -1 --tip-theta 3.141592653589793`) and writes levels,
energies, energy-momentum integrals and identities.

## Method

* **Reduction (from ks-theory.json, re-verified here numerically):** Psi = e^{-i eps x4} e^{i k.x} W^{-3}
  V_beta chi(y), W = e^{Hy}, gives in each of the eight 2 x 2 blocks
  h_j = j[-i sigma1 d_y + M_eff sigma2 + kappa k sigma3] + v_v, kappa = e^{-Hy - a4,0}. The crate reads the
  exported basis V and the gamma matrices (`Revision/algebra/gammas.json`) and checks that V^dag X V is block
  diagonal with exactly these forms for the operators of h and of the densities (check
  `block_reduction_numeric`). With chi = (a, i b) the equation is real.
* **Eigenvalues by shooting with a Pruefer count (justification):** the Pruefer angle theta = atan2(b, a)
  has d theta(0)/d eps = j int r^2 dy / r(0)^2, so Phi(eps) = j theta(0) is strictly increasing. The tip
  condition (regular tip, theta_tip = 0: b(-L) = 0) fixes theta(-L); the ASSUMED Z2 brane gives b(0) = 0
  (even) or a(0) = 0 (odd), i.e. Phi = l pi or pi/2 + l pi. Every level is the unique root for an integer
  label l (oscillation theorem): no level is missed, and l is a topological label that follows a level
  continuously between SCF iterations, couplings and slices. Roots: safeguarded Newton (derivative from
  int r^2) inside a bracket, tolerance 1e-13 m.
* **Integration:** classical RK4 with G = 900 steps on [-L, 0] (refined run: 1800). The potentials live on
  the fine grid (nodes and step midpoints), so every RK4 stage uses stored values. Orbitals at the midpoints
  come from cubic Hermite interpolation (O(h^4)). Integrals use Simpson's rule on the fine grid.
* **Lattice of 3-space momenta:** k = dk n, n in Z^3, dk = 0.25 m (3-torus of size ell = 2 pi/dk), shells
  n2 = |n|^2 with r3(n2) vectors. Each level of h_j(|k|) is 4 r3(n2)-fold for each j (4 blocks times the
  directions; ks-theory.json blockEquation.degeneracy). Sectors are (n2, j, parity).
* **Particles (CONVENTION of ks-theory.json, justification OPEN):** particles are the labels whose lambda = 0
  level at the same slice is positive, plus the k = 0 zero modes. In a sector these are the labels
  l >= l_min (check `free_particle_branch_labels`). The negative branch is the normal-ordered sea: it is not
  populated, not even thermally (see the diagnostic below).
* **Densities and functional:** n, S, Q proper (per proper 7-volume, P = e^{-6Hy}/Vol_7), w_Z2 = 1/2.
  M_eff = m + (15/16) lambda S and v_v = -(1/16) lambda n are the Hartree terms plus the exact local
  exchange of the uniform 8-fold gas, e_int = lambda[(15/32) S^2 - (1/32) n^2]. This is the canonical
  functional. The **exact Fock exchange** of the closed-shell slab determinant differs by +lambda Q^2/32
  (ks-theory.json exchange.exactFockSlab). It is reported for every state as Delta E_x and solved as the
  variant w_Q = lambda Q/16 sigma3 (`exx/`).
* **Self-consistency:** Anderson (Pulay) mixing of the potential vector (depth 6, beta = 0.4), stopped when
  max |residual| <= 1e-11 m. Safeguards: backtracking when a level solve fails, a divergence abort, and a
  coupling continuation (lambda/4 ... lambda) as fallback. The exact-Fock variant falls back to a
  continuation in the weight of its exact-Fock term instead. No fallback was needed for the 75 canonical
  ground states (all paths "direct", at most 17 iterations; `ground/summary.csv`).
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
  the module documentation of `src/mermin.rs`): (n + 2) eps_mach (P + Hl + |d|)/(dN/dmu) + eps_mach <|eps - mu|>
  + 2 eps_mach |mu|, with n the number of levels and <.> the mean weighted with g f (1 - f). The three terms are
  the summation and evaluation of the terms, the rounding of the arguments x_i = (eps_i - mu)/T, and the two
  adjacent doubles at the root; the first is about n eps_mach T. For the former direct count the first term has N
  in place of P + Hl + |d|: that count missed the root by 8.267e-10 m in the activated state N8_lamm1_a00_T10
  (dN/dmu = 1.24e-6; found by the cross-check, see History below). `thermodynamics.csv` records dN/dmu, this
  bound (`mu_rounding_bound`) and, as a DIAGNOSTIC for the negative control of the refined comparison, the root of
  the former direct count on the same final levels minus mu (`mu_direct_count_minus_mu`) for every state.
* **Particle number:** N = sum g f over both brane parities is the particle number of the doubled
  (universe + Z2 image) system; the patch holds N/2. Note: ks-theory.json thermodynamics.occupation writes
  "sum w_Z2 g f = N". That line is inconsistent with its own densities.total, energy and grand potential;
  the solver follows the latter, and records the discrepancy in `parameters.json`.
* **Energy-momentum tensor:** rho = sum w g f eps n_o - e_int, p3 = sum w g f (kappa|k|/3) t_o + e_int,
  p_t = e_int, p8 = sum w g f [(eps - v) n_o - M s_o - kappa |k| t_o] + e_int (ks-theory.json emt). For the
  exact-Fock variant, p8 gets -w_Q q_o inside the sum. This is derived here: the orbital identity holds with
  kappa k replaced by kappa k + j w_Q, and e_int stays homogeneous of degree 2.
* **History and adiabaticity:** a4 = A H x4 with A = 1, slices a4,0 in {0, 0.5, 1, 1.5, 2}. This history is a
  PRESCRIBED test-field background without back-reaction: the a4 equations of SPEC section 5 allow the linear
  member only with p3 = p_t = p8 and constant rho, and the Kohn-Sham gas along it has p3 != p_t and a changing
  rho (and depends on x8); it is not a solution of the a4 equations with the Kohn-Sham source
  (`Revision/field_equations_a4/reports/ks-source-conditions.json`). ks-theory.json carries this label
  (`adiabaticity.history` ends "PRESCRIBED BACKGROUND (see historyStatus)", `adiabaticity.historyStatus`); the
  solver refuses a ks-theory.json without it and copies it into `parameters.json` and `adiabatic/history.json`.
  The measure is
  Q_nm = A H |<n| d_a h |m>| / (eps_n - eps_m)^2 for n occupied and m empty in the same (shell, j, parity),
  with d_a h = -j kappa k sigma3 + j (d_a M_eff) sigma2 + d_a v_v. The self-consistent derivatives come from
  the states at a4 +- delta and +- 2 delta (delta = 2e-3, fixed occupations, Richardson). Changes of the
  aufbau occupation between slices are flagged as Fermi-level crossings, and the adiabatically continued
  state (the a4,0 = 0 labels) is then solved.

## Parameters and calibration (`results/parameters.json`)

H = 1, m = 1, L = 3, dk = 0.25, v_t = 1, Vol_7 = ell^3 v_t, tip theta = 0.

* **Particle numbers:** N = 8 (the k = 0 brane zero modes); N_large = 688, the largest closed shell of the
  free a4,0 = 0 aufbau below the bulk edge 1.2923 m (it fills the brane band up to n2 = 11); N_mid = 136,
  the closed shell nearest N_large/4.
* **Couplings, per N:** lambda_1, lambda_2 = 0.1 m and 0.3 m divided by the largest first-order mean-field
  potential per unit lambda of the free ground states over ALL slices, rounded to 4 digits. This gives
  lambda_1 = 0.01946, 0.0009298, 0.0001846 and lambda_2 = 0.05838, 0.002789, 0.0005538 for
  N = 8, 136, 688.
* **Why the whole history:** for N > 8 the potential per unit lambda grows along the history (N = 688: 5.2
  at a4,0 = 0, 541.7 at a4,0 = 2). The redshifted brane-band orbitals spread toward the tip, where the
  proper 7-volume e^{6Hy} is small. A calibration at a4,0 = 0 alone made the a4,0 = 2 states strongly
  coupled (measured in development: self-consistent potentials of 1.3 m for lambda_1, N = 136), and the
  exact-Fock variant diverged there.
* **Temperatures:** T in {0.01, 0.02, 0.05} m, for N in {8, 136, 688}, lambda in {0, +-lambda_1}, all five
  slices.

## Outputs (`Revision/kohn_sham/results/`, deterministic: LF, 16 significant digits, no paths or timings)

| file | content |
| --- | --- |
| `parameters.json`, `manifest.json` | parameters, calibration, conventions; SHA-256 of every file |
| `spectrum/` | analytic k = 0 spectra, brane-band slope per slice, band and bulk levels vs k, tip-angle test, closed shells per slice |
| `ground/summary.csv`, `ground/runs.json` | 75 ground states: E_KS, HOMO, LUMO, KS gap, potentials, SCF history |
| `ground/levels/<id>.csv`, `ground/profiles/<id>.csv` | levels with labels and occupations; proper profiles n, S, Q, M_eff, v_v, e_int, rho, p3, p_t, p8 at y = -3 + 0.02 i |
| `ground/emt-integrals.csv` | 2 Vol_7 int e^{6Hy}(rho, p3, p_t, p8, n) dy, brane and tip values, identities |
| `excited/summary.csv`, `excited/particle-hole/<id>.csv` | KS gap, Delta-SCF, the 24 lowest particle-hole excitations |
| `adiabatic/` | Q_max per state, Fermi-level crossings, continued states, crossing demonstration (N = 696) |
| `rescaling/rescaling.csv` | the exact rescaling identity, solved independently |
| `exx/exact-fock-variant.csv` | uniform-gas vs exact-Fock exchange |
| `thermo/thermodynamics.csv` | 135 Mermin states: mu, E, S, F, Omega (two forms), C_V = T dS/dT, dE/dT, -dF/dT, sea-hole diagnostic, dN/dmu, the rounding bound of mu and the former direct-count root minus mu (`dN_dmu`, `mu_rounding_bound`, `mu_direct_count_minus_mu`) |

Run ids: `N<N>_<lam0|lamp1|lamm1|lamp2|lamm2>_a<10 a4,0>` (`_T<1000 T>` for thermal states).

Outside `results/`: `tools/mermin-roots-40digit.json` (the 40-digit fixture of the Mermin root, written by
`tools/mermin_roots_mp.py`) and the reports `ks-rust-solver.json`, `ks-rust-mermin-roots.json` and
`ks-rust-determinism.json` in `Revision/kohn_sham/reports/`.

## Checks

`Revision/kohn_sham/reports/ks-rust-solver.json` holds 42 checks, all PASS. Per-run checks are aggregated,
with the worst case and its run id.

* **Theory and algebra:** coefficients, gamma fixture, block reduction.
* **Free field:** analytic k = 0 spectra of both parities (error O((h eps)^4)), the exact zero mode, the
  brane-band slope c e^{-a4,0} with c = 1.9051482536 at every slice (to 1.9e-12), block-type symmetries,
  branch labels, tip-angle insensitivity, the free rescaling relation, monotone band.
* **Every state:** SCF convergence, N conservation (sum g f and the density integral), brane boundary
  residuals, the two energy forms, the EMT energy integral, nabla_mu T^mu_y = 0 (integrated and
  pointwise), the derivative form of the y-kinetic term (an orbital-equation residual), window
  completeness, closed shells.
* **Along the history:** dE/da4 = -6 Vol_7 int e^{6Hy}(p3 - p_t) dy against Richardson differences;
  Hellmann-Feynman d eps/da4 = <d_a h>; the exact rescaling identity
  KS(a4,0; dk, v_t) = KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}), solved independently (levels to 1.5e-13 m).
* **Excited states:** Delta-SCF = KS gap at lambda = 0.
* **Exact-Fock variant:** convergence and y-conservation.
* **Thermodynamics:** Omega in two forms; C_V = T dS/dT = dE/dT and -dF/dT = S. Both are Richardson
  differences, compared within 1e-4 relative plus the noise floor N x root tolerance / dT of a difference
  quotient of energies. Also the window cut and the shells beyond the window.
* **The Mermin root:** `thermo_mu_well_conditioned_root`: in all 135 thermal states mu equals the
  `LogBalance` root on the final levels bit for bit; `LogBalance` and `LinearDeviation` agree within the larger
  of their rounding bounds (max difference 2.429e-16 m, max ratio to the bound 0.353, largest bound 4.74e-14 m; at
  most 2 split passes). As a diagnostic it records how far the former direct count would deviate: by more than
  1e-12 m in 3 states, -8.267e-10 m (N8_lamm1_a00_T10), 2.722e-10 m (N8_lam0_a00_T10) and 6.959e-11 m
  (N8_lamp1_a00_T10), each within its own conditioning bound. `thermo_mu_vs_40digit_roots`: on the 8 states of
  the fixture both forms lie within their bounds of the 40-digit roots (largest ratio 0.228, largest bound
  2.0e-16 m), `LogBalance` reproduces the recorded mu bit for bit, and the negative control (the direct count)
  misses the root by up to 8.267e-10 m, 4.2e6 times the largest new bound.
* **Crossing-flag demonstration, and the T3 solver self-test.** The self-test solves (m, lambda, tip 0) and
  (-m, lambda, tip pi) independently and gets equal levels, E and EMT integrals and opposite S, to 1e-13;
  the untransformed tip is the negative control. It is NOT a proof of T3, which is owned by
  `Revision/pairing/kohn_sham`.

`Revision/kohn_sham/reports/ks-rust-mermin-roots.json` (5 checks, all PASS; `tools/mermin_roots_mp.py`): all
135 `single --mermin-levels` runs completed; the 40-digit and 50-digit roots agree to 7.5e-35 (relative); the
solver's mu lies within its rounding bound of the 40-digit root on its own levels in 135 of 135 states (largest
|mu - root| 2.433e-16 m, N136_lamp1_a20_T50; largest ratio to the bound 0.156; N8_lamm1_a00_T10 -2.519e-17 m
with bound 1.610e-16 m, where the former direct count was 8.27e-10 m off; the tool evaluates the bounds at the
40-digit root, independently of the solver); the mu of every `single` run equals the committed matrix;
the fixture holds the 8 states with the largest direct-count bound.

`Revision/kohn_sham/reports/ks-rust-determinism.json` covers the repeat (byte identity of all files) and the
refined-tolerance run (RK4 steps x 2, root tolerance / 10, SCF tolerance / 10, thermal cut / 100, and the
Mermin root in the form `LinearDeviation` instead of `LogBalance`). Its tolerances were fixed before the
comparison: eigenvalues 1e-8 m, energies 1e-8 relative, profiles 1e-6, thermodynamics 1e-8, derived
derivatives 1e-6. Because the two runs solve the Mermin root along different rounding paths, |canonical -
refined| of mu and Omega contains the rounding error of the root instead of sharing it (check
`refined_mermin_root_path`; `refined_thermodynamics` compares both forms of Omega).

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
   U_mu <= 1.255e-12 m and U_Omega <= 2.752e-10 (largest B_c + B_r 1.143e-13 m). The old canonical mu against
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
   `adiabatic/history.json`). In the verification pass of 2026-10-07 the rounding bound gained the argument term
   eps_mach <|eps - mu|> (it was omitted before; it is at most 0.44 of the former bound in the matrix, so every
   `mu_rounding_bound` grew by a factor 1.0005 to 1.44) and the column `mu_direct_count_minus_mu` was added; mu
   and every other number of the matrix are unchanged by that pass.

## Canonical results (from `results/`; units m = H = 1)

* **N = 8, KS gap:** 0.4307337 m at a4,0 = 0, 0.1703493 at 1, 0.06415941 at 2 (lambda = 0). The LUMO is
  the n2 = 1 brane band, which redshifts as e^{-a4,0} c dk; the k = 0 zero modes do not depend on a4,0, so
  E_KS is the same at every slice. Delta-SCF equals the gap at lambda = 0; with lambda_2 it is 0.4312929
  vs gap 0.4312996 at a4,0 = 0.
* **E_KS along the history (lambda = 0):** 80.28222, 32.38412, 12.44507 for N = 136 and 680.4412, 279.4249,
  110.3867 for N = 688, at a4,0 = 0, 1, 2. The brane-band gas redshifts. (Along the prescribed history, without
  back-reaction: equations of state derived from it are not consequences of the coupled field equations.)
* **Integrated pressure ratios (lambda = 0):** int p3 / int rho is 0.2966, 0.3100, 0.3264 (N = 136) and
  0.2929, 0.3018, 0.3183 (N = 688); int p8 / int rho is 0.4365, 0.5969, 0.6808 (N = 136). These are the
  integrated EMT components only. Equations of state seen by a 3-space observer are the work of
  `Revision/dark_sector`.
* **Adiabaticity:** Q_max <= 0.0935 over the whole matrix, the largest for the Fermi-shell brane-band level
  -> the first bulk level of the same sector (e.g. N = 688, a4,0 = 0). Q_max = 0 exactly for N = 8: d_a h
  vanishes on the k = 0 sector.
* **Fermi-level crossings:** none occur in the canonical matrix. Demonstration at lambda = 0, N = 696: the
  k = 0 odd bulk level is emptied and the n2 = 12 band shell fills from a4,0 = 0.5 on. The adiabatically
  continued state lies 3.66 m (a4,0 = 0.5) to 8.62 m (a4,0 = 2) above the instantaneous aufbau state, so
  the instantaneous ground state is not the adiabatically reached state there.
* **Exact Fock vs uniform-gas exchange:** for N = 8 (b = 0 zero modes, Q = n) the exact Fock exchange
  cancels the vector part, and E_EXX = -2.0e-13 against E_LDA = -2.863e-3 (lambda_2). So the canonical
  interaction energy of the zero-mode state is entirely the uniform-gas exchange term that the exact
  exchange removes. For N = 136 and 688 the two functionals differ by Delta E_x (e.g. 0.0768 of E = 110.58,
  N = 688, lambda_2, a4,0 = 2). E_EXX - (E_LDA + Delta E_x) is at most 3.7% of Delta E_x (second order).
* **Thermal sea holes (diagnostic of the convention):** the excluded sea would carry more than 1% of N in
  15 of the 135 thermal states, all at a4,0 >= 1. The largest is 30.98 N (N8_lamm1_a20_T50: N = 8,
  lambda = -lambda_1, a4,0 = 2, T = 0.05, mu = -0.0977; 30.80 N at lambda = 0 and 30.62 N at +lambda_1): there
  the particle-only Mermin ensemble is outside its range of validity, and a thermal treatment of the Dirac sea
  (pairs) would be required.

## What this does not establish (OPEN or ASSUMED)

* **Non-adiabatic evolution:** the states are instantaneous (adiabatic) Kohn-Sham states. Q_max << 1 makes
  the adiabatic approximation self-consistent within the same-sector transitions, but the time-dependent
  problem is OPEN.
* **Assumed boundary conditions and the cutoff:** the Z2 brane is ASSUMED. The regular tip at L = 3 is a
  cutoff choice; the proper densities near the tip are large (e^{6H|y|} amplification), so the
  interacting results depend on L.
* **Filling convention:** the particle/sea split and the zero-mode convention are CONVENTIONS whose
  justification is OPEN. The thermal sea is excluded (diagnostic above).
* **Exchange and correlation:** the exact-Fock functional is exact only for the closed-shell determinants
  of ks-theory.json, and no correlation is included.
* **Delta-SCF:** the excited state is an ensemble over degenerate groups, not a symmetry-broken single
  determinant.

## Timings (this machine, 22 threads)

Canonical matrix with the repaired Mermin root, measured on an otherwise idle machine (re-run on 2026-10-02 into a
scratch directory): 78.1 s in total.
* free spectra and closed shells 1.2 s
* calibration 0.8 s
* ground matrix 35.7 s: 75 states, each with 4 a4 neighbours, Delta-SCF, rescaling partner and exact-Fock
  variant
* history 3.3 s
* thermodynamics 35.4 s: 135 states, each with 4 temperature neighbours
* T3 self-test 1.5 s

Verification pass of 2026-10-07 (rounding bound with the argument term, column `mu_direct_count_minus_mu`,
the live negative control), run while other workflows used the same machine, so the times are longer:
* canonical matrix 166.6 s (ground matrix 89.1 s, thermodynamics 56.3 s); `tools/mermin_roots_mp.py` 24.1 s
  (135 `single` runs 19.0 s, 40-digit roots 5.1 s), which rewrote the bound strings of the fixture; the canonical
  matrix again 171.7 s (results byte-identical to the first pass, the report differs only by the fixture's
  sha256 and ratios);
* repeat of the canonical matrix 194.1 s: all 244 result files and the report byte-identical;
* refined-tolerance run (G = 1800, root tolerance 1e-14, SCF tolerance 1e-12, thermal cut 1e-14, Mermin form
  `LinearDeviation`) 635.3 s (ground matrix 265.1 s, thermodynamics 299.0 s).

The comparison (`Revision/kohn_sham/reports/ks-rust-determinism.json`, 14 checks, all PASS):
* the repeat is byte-identical in all 244 files, and its check report is byte-identical too;
* refined vs canonical: E_KS to 1.9e-12 relative; HOMO, LUMO and gaps to 1.3e-12 m; 23724 eigenvalues
  label by label to 2.1e-9 m; Delta-SCF to 5.8e-11 m; profiles to 2.8e-9 of their maxima; Q_max and
  dE/da4 to 9.0e-10; thermodynamics (mu, E, F, both forms of Omega, S) to 2.5e-10; C_V to 5.7e-9;
* the Mermin root along the two rounding paths (`refined_mermin_root_path`): U_mu = |mu_c - mu_r| + B_c + B_r
  at most 1.255e-12 m (N136_lamm1_a00_T20), U_Omega = |Omega_c - Omega_r| + N (B_c + B_r) at most 2.752e-10
  (N688_lamm1_a00_T20); the largest B_c + B_r is 1.143e-13 m (N688_lamm1_a20_T50; canonical bound 4.738e-14 m,
  refined 6.693e-14 m); the negative control passes in the 3 states where the former error exceeds 2 U_mu;
* the analytic spectra converge with a measured error ratio of 16.00, the order of RK4.
