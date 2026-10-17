# Revision Kohn-Sham cross-checker (Rust solver vs the independent Python reference, full matrix)

This directory compares the committed canonical Rust results (`Revision/kohn_sham/results`) with the independent
reference (`Revision/kohn_sham/reference/results`) on the FULL canonical matrix. The comparison covers every
ground state (75), every thermal state (135, with every level label by label), the exact-Fock variant SCF energies
and gaps (60), the rescaling partners (60), the particle-hole lists (75), the sea-hole diagnostic (135) and the
crossing demonstration (5 slices). It also tests the stated rounding bound of the repaired Rust Mermin root
against 40-digit roots. The reference uses staggered finite differences with Richardson extrapolation; Rust uses
shooting with RK4 and a Pruefer count. Revision code only.

The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6H), z = 6 H x0 (the fold cos z = 0
at y = 0); x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times
(scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}, a4 increasing). p0 = T^x0_x0 is the hidden-direction pressure. Both
records are those of the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1): in the y
chart ds^2 = e^{2a4} dx_{1..3}^2 - dx4^2 + f^2 [dy^2 - e^{2Hy} dx_{5..7}^2], f = e^{-a4} b4^{1/2}, on the PRESCRIBED
history a4 = H x4, b4 = e^{(4/3) H x4} (f = e^{-a4/3}; solver README, "The corrected metric"). Names that contain
"brane" (CSV columns, check names) are kept from the earlier records; they denote the fold y = 0.

## Run (from the repository root; the Rust binary must be built: `cargo build --release` in `../solver`)

```
python Revision/kohn_sham/reference/run_reference.py --jobs 20                                   # the reference (once; or in stages and parts, ../reference/README.md)
python Revision/kohn_sham/checker/measure_rust_refinement.py --work <scratch>/rust-single --jobs 22   # writes rust-refinement.json
python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch>/cc --jobs 22                  # writes the reports
```

`crosscheck_ks.py` runs the reference a second time itself, into a fresh `<work>/reference-repeat`. It then
compares every result file and the report `ks-reference.json` byte for byte with the committed ones (check
`reference_repeat_byte_identical`). No repeat directory from elsewhere is accepted. The repeat may use a job cache of
its own (`--repeat-cache DIR`, passed to `run_reference.py --cache DIR`): the jobs of the repeat are then computed
beforehand in two stages of parts, each within a time limit, into that cache (it must not be the cache of the
canonical run), and the checker's run of `run_reference.py` only assembles them:

```
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/repeat-cache --stage 1 --part i/6 --jobs 20    # i = 1..6
python Revision/kohn_sham/reference/run_reference.py --cache <scratch>/repeat-cache --stage 2 --part i/6 --jobs 20    # i = 1..6
python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch>/cc --jobs 22 --repeat-cache <scratch>/repeat-cache
```

The checker also recomputes mu in 40-digit arithmetic in parallel processes for 405 level sets: the 16-digit levels of both solvers (270) and the
exact Rust levels (135).

Outputs: `Revision/kohn_sham/reports/ks-crosscheck.json` (every check with name, verdict and detail, plus a
`diagnosis` for a failing check) and `Revision/kohn_sham/reports/ks-crosscheck-table.csv` (every scalar
comparison with both values, both uncertainties, the tolerance and the ratio; the 20487 levels and 113250
profile points are aggregated in the report only).

## Tolerance rule (fixed in `crosscheck_ks.py` before any comparison; never adjusted to a result)

```
|x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 scale
```

* `U_ref` is the reference's measured grid uncertainty: the size of the h^4 term of the three-grid
  Richardson value on the finest grid. A fourth grid (G = 2400) validates it for one state.
* `U_Rust` is (16/15) |canonical - refined| of the Rust solver. RK4 makes the refined error 1/16 of the
  canonical one, so this difference times 16/15 estimates the canonical error.
  * `measure_rust_refinement.py` measures it for EVERY state of the matrix: 75 ground, 135 thermal, 60
    exact-Fock (`single --exx`) and the 5 crossing-demonstration slices, 550 `single` runs in all. It runs
    the Rust `single` command with the canonical and the refined numerics and the label-set margin of the
    canonical matrix. This covers energies, EMT integrals, every level (largest difference of the state),
    every profile (largest difference of that profile), the brane and tip values, mu and the entropy. For
    the exact-Fock variant it covers E_KS and the gap (from the levels). For the crossing demonstration it
    covers E_aufbau and the continued energy (the a4,0 = 0 occupation summed over the levels).
  * For every thermal state it also records the canonical levels with their keys and occupations (the Rust
    matrix writes no thermal levels file). From `single --mermin-levels` of the same canonical run it records
    the exact doubles of the final levels and of mu (shortest round-trip decimals). The main outputs carry 16
    significant digits, so the exact values are needed to test the rounding bound of mu (|mu_Rust - root| at most 2.868e-16 m in this run).
  * The canonical `single` runs must reproduce the committed matrix (check `rust_refinement_applies_to_matrix`).
    The exact-Fock variant is the exception, because the matrix starts its SCF from the uniform-gas state and
    `single --exx` from zero potentials. Both stop at the SCF tolerance 1e-11, so |single - matrix| <= N x
    scfTolerance (E) and 6 scfTolerance (gap) are required (check `rust_refinement_applies_to_matrix_exx`).
    The measured |single - matrix| is added to U_Rust of every exact-Fock comparison.
  * Quantities that `single` does not report (Delta-SCF, Q_max, the finite-difference dE/da4, C_V) take the
    maximum over the whole canonical matrix from `reports/ks-rust-determinism.json`, as stated in each check.
  * Propagated (stated in each check): HOMO, LUMO and particle-hole delta_eps use the largest level
    difference of the state. Rescaling partner: U_Rust(E_KS at the slice) + |partner_E_KS - E_KS| of Rust (the
    partner problem has the same coefficient functions up to rounding). Sea holes: holes x (U_Rust(mu) +
    U_Rust(levels))/T, because |d f| <= f (|d mu| + |d eps|)/T.
* `scale` is max(1, |x|) for scalars and the profile maximum for profiles. It provides a roundoff floor.
* dE/dT and -dF/dT are difference quotients of energies over dT = 0.01 T. Each solver's stated noise floor is
  therefore added: N x rootTolerance / dT for Rust (as in its `thermo_CV_identity` check) and N x 1e-12 / dT
  for the reference (its SCF tolerance, as in its own identity check). C_V = T dS/dT carries no such floor.

The re-derived couplings must be identical after rounding. The coupling strength is a maximum over y. The
reference reports the continuous maximum; Rust reports the largest of its fine-grid samples (spacing
L/1800). For an interior maximum the Rust value must therefore lie below the reference value, by at most the
sampling bound |f''| s^2/8 (f'' is the reference curvature at the peak), within the uncertainties.

Particle-hole lists are compared where both solvers can hold the excitation. The particle must lie below both
solvers' lowest excluded level (reference: Richardson value), lowered by the comparison tolerance. Rust labels
are converted to reference ranks with the label_min of the Rust levels file. Each Rust row must appear in the
reference list (48 rows kept) with the same hole and particle groups, multiplicity and same-sector flag, and
with delta_eps within the rule. Conversely, no reference excitation clearly below the last Rust row may be
missing from the Rust list.

The sea-hole diagnostic of Rust sums over the shells n2 >= 1 of its thermal label set, which are the first
`shells` shells of the lattice. The reference reports the cumulative sum per shell, so the same shells are
compared. Rust label 0 of the j = -1 even sector is reference rank -1 (label_min = 1 there).

Thermal levels (`thermo_levels`) are compared label by label like the ground levels. The Rust levels are those
of the canonical `single` run, which reproduces the committed mu, E and S exactly. In each sector the Rust label
set starts at label_min (`solver/src/scf.rs`, `solve_levels`), so rank = label - (lowest label of the sector in
the set). This is checked against label_min of the Rust ground levels files at the same slice wherever the sector
occurs there. The reference ranks of every sector must start at 0. Every level with f >= 1e-12 in one set must be
in the other set. U_Rust is (16/15) x the largest |canonical - refined| over the levels of the state, as for
ground states.

The stated rounding bound of the Rust mu (`thermo_mu_rust_stated_bound`) is not a Rust-vs-reference comparison.
On the exact doubles of each canonical thermal run, the checker computes the root of sum g f = N in 40 digits and
takes mu_Rust - root in 40 digits. It requires |mu_Rust - root| <= `mu_rounding_bound` of `thermodynamics.csv`, and
that the exact values round to the committed 16-digit mu and levels.

## Results (`reports/ks-crosscheck.json`: 31 checks, all PASS; run of 2026-10-17, the corrected metric)

Preconditions: reference report 39/39 PASS, Rust solver report 45/45 PASS, Rust determinism report 14/14 PASS; failing checks: {'ks-reference.json': [], 'ks-rust-solver.json': [], 'ks-rust-determinism.json': []}; Rust refinement runs (single canonical and refined) failed: none; the refinement covers every state of the Rust matrix: True (states per kind: Rust {'ground': 75, 'thermo': 135, 'exx': 60, 'crossing': 5}, measured {'ground': 75, 'thermo': 135, 'exx': 60, 'crossing': 5}).

* the canonical `single` runs of checker/rust-refinement.json reproduce the committed canonical matrix (tolerance 1e-12 for every class; crossing demonstration relative to max(1, |E|)): E_KS_rel 0.000e+00, E_aufbau_abs_rel 0.000e+00, E_continued_abs_rel 3.957e-16, E_rel 0.000e+00, emt_integrals_rel 0.000e+00, entropy_rel 0.000e+00, levels_max_abs 0.000e+00, mu_abs 0.000e+00, profiles_max_rel 0.000e+00; hence |canonical - refined| of these runs measures the error of the committed Rust results
* exact-Fock variant: the matrix and `single --exx` solve it at the occupations of the converged uniform-gas ground state, started from it (the same path); both stop at max |residual| <= scfTolerance = 1e-11: |E_single - E_matrix| <= N x scfTolerance and |gap_single - gap_matrix| <= 6 scfTolerance (two levels, three potentials) are required; worst ratios: E 0.000 (N8_lamp2_a20 |dE| 0.000e+00), gap 0.000 (N2352_lamm1_a00 |dgap| 2.255e-16); the measured |single - matrix| is added to U_Rust of the exact-Fock comparisons
* H, m, L, dk, v_t, tip angle, history A and beta (b4 = b4(0) e^(beta a4)), slices and temperatures identical: True (no differences); both read the same ks-theory.json (sha256 34f7fa2a4543fd91): True
* particle numbers re-derived by the reference from the stated rules (free a4,0 = 0 aufbau, bulk edge, closed shells); 5 comparisons; worst |diff|/tolerance 0.000 (bulk edge: Rust 1.29229282806878, reference 1.29229282806858, |diff| 2.003e-13, tolerance 1.832e-09); N_large = 2352, N_mid = 592, N of the crossing demonstration = 2360 (U_Rust of the bulk edge: matrix-wide eigenvalue maximum 6.067e-10); failures: none
* couplings lambda_1, lambda_2 re-derived by the reference (4 significant digits) must be identical; strengths: the Rust value is the maximum over its fine-grid samples (spacing s = L/(2 x rk4Steps)), the reference value is the continuous maximum (quartic interpolation), so for an interior maximum 0 <= ref - Rust <= |f''| s^2/8 within 3 (U_ref + U_Rust), with f'' the reference curvature at the peak; for a maximum at the tip y = -L (a sample point of both) the values must agree; U_Rust = the matrix-wide maximum (16/15) x 1.950e-10 of |canonical - refined| relative to the maximum of the profile's family (n for the strength) x strength; 21 comparisons; worst |diff|/tolerance 0.007 (strength N = 2352 a4 = 0.0: Rust 0.18644856544471, reference 0.186448565443816, |diff| 8.935e-13, tolerance 1.244e-10); failures: none

Rust and the reference agree within the stated tolerances everywhere. Each line gives the number of comparisons and the largest ratio |diff| / tolerance (where it occurs).

* the same occupied levels (Rust label - label_min = reference rank), occupations, HOMO group and LUMO group; 300 comparisons; failures: none
* E_KS, E_band, E_int (225): 0.269 (N8_lamm2_a00 E_KS: Rust 0.110981600530415, reference 0.110981600513165, |diff| 1.725e-11, tolerance 6.418e-11).
* HOMO, LUMO, gap (225): 0.002 (N8_lamp2_a00 HOMO: Rust -0.0272625480151966, reference -0.0272625480130267, |diff| 2.170e-12, tolerance 8.989e-10).
* levels label by label (20487): 0.296 (N592_lamm1_a20 level 1:-1:even:2: Rust 6.20666695367002, reference 6.20666695306336, |diff| 6.067e-10, tolerance 2.050e-09).
* Delta-SCF and E_excited (150): 0.312 (N2352_lamm2_a00 delta_SCF: Rust 0.0242785182208536, reference 0.0242785225637615, |diff| 4.343e-09, tolerance 1.391e-08).
* EMT integrals (375): 0.309 (N2352_lamm1_a15 int_p0: Rust 11.3145792569937, reference 11.3145792590192, |diff| 2.025e-09, tolerance 6.564e-09).
* fold and tip values (600): 0.454 (N2352_lamm2_a05 rho_tip: Rust 1.00210451952915, reference 1.00210451952564, |diff| 3.513e-12, tolerance 7.743e-12).
* profile points (113250): 0.438 (N2352_lamm2_a05 n(y = -3.00).
* Delta E_x (75): 0.160 (N592_lamp2_a20 deltaE_x: Rust 1.54026693871053, reference 1.54026693871447, |diff| 3.946e-12, tolerance 2.459e-11).
* dE/da4 in both forms (150): 0.310 (N8_lamm1_a20 dE_da4_finite_difference: Rust -0.00541154602713278, reference -0.00541154627125748, |diff| 2.441e-10, tolerance 7.885e-10).
* Q_max, its pair, matrix element and level spacing (300): 0.003 (N2352_lamp1_a00 Q_max matrix element: Rust 0.0740703429315664, reference 0.0740703428970555, |diff| 3.451e-11, tolerance 1.070e-08).
* exact-Fock variant: E_EXX, gap and E_EXX - (E_uniform_gas + Delta E_x) (240): 0.311 (N2352_lamp1_a10 E_exx_minus_first_order: Rust -0.00928858063110205, reference -0.00928858188606444, |diff| 1.255e-09, tolerance 4.040e-09).
* rescaling partners (180): 0.235 (N592_lamm1_a15 partner_E_KS: Rust 81.3232255302446, reference 81.3232255308006, |diff| 5.560e-10, tolerance 2.370e-09).
* crossing demonstration (31): 0.036 (crossing a4 = 0.5 difference: Rust 4.67635378929845, reference 4.67635378929654, |diff| 1.905e-12, tolerance 5.309e-11).
* thermal mu, E, S, F, Omega (810): 0.277 (N8_lam0_a10_T50 E: Rust 0.95834020967101, reference 0.958340209839179, |diff| 1.682e-10, tolerance 6.066e-10).
* C_V, dE/dT and -dF/dT (405): 0.996 (N8_lamp1_a00_T20 minus_dFdT: Rust 0.390957900885241, reference 0.390957918842, |diff| 1.796e-08, tolerance 1.803e-08).
* sea-hole diagnostic (270): 0.167 (N8_lam0_a10_T50 sea_holes_excluded: Rust 29.1059293216175, reference 29.1059293220216, |diff| 4.041e-10, tolerance 2.420e-09).
* thermal levels label by label (78240): 0.316 (N2352_lamp1_a00_T50 level 1:-1:odd:2: Rust 2.93256179057636, reference 2.93256179043646, |diff| 1.399e-10, tolerance 4.421e-10).
* mu in 40 digits from each solver's own levels (270): 0.124 (N8_lamp1_a10_T20 mu_high_precision: Rust 0.0265271111109533, reference 0.0265271111093771, |diff| 1.576e-12, tolerance 1.267e-11).
* the 24 lowest particle-hole excitations (excited/particle-hole/<id>.csv) against the reference list (48 rows): the same hole and particle groups (Rust labels converted to ranks), the same multiplicity and same-sector flag, delta_eps within the rule (U_Rust = 2 x (16/15) x the largest |canonical - refined| over the levels of the state); compared where the particle lies below both solvers' lowest excluded level; and no reference excitation below the Rust 24th (minus its tolerance) is missing from the Rust list; 5109 comparisons; worst |diff|/tolerance 0.002 (N2352_lamm2_a00 particle-hole rank 12 delta_eps: Rust 0.125960541899873, reference 0.125960541896041, |diff| 3.831e-12, tolerance 1.848e-09); N592_lam0_a00: 1 Rust rows with the particle at or above the common cut 1.089724735, 0 beyond the last kept reference row (not compared); N8_lam0_a00: 2 Rust rows with the particle at or above the common cut 0.4999999991, 0 beyond the last kept reference row (not compared); N8_lamm1_a00: 1 Rust rows with the particle at or above the common cut 0.7164828913, 0 beyond the last kept reference row (not compared); N8_lamm1_a05: 1 Rust rows with the particle at or above the common cut 0.6120193779, 0 beyond the last kept reference row (not compared); N8_lamm2_a00: 1 Rust rows with the particle at or above the common cut 1.145020302, 0 beyond the last kept reference row (not compared); N8_lamp1_a00: 1 Rust rows with the particle at or above the common cut 0.6976610217, 0 beyond the last kept reference row (not compared); N8_lamp1_a05: 1 Rust rows with the particle at or above the common cut 0.6009894159, 0 beyond the last kept reference row (not compared); N8_lamp2_a00: 1 Rust rows with the particle at or above the common cut 1.090455269, 0 beyond the last kept reference row (not compared); 1678 Rust rows matched to reference rows; failures: none
* DIAGNOSTIC (not a replacement of thermo_state_functions): each solver's floating-point mu minus the 40-digit root on its own levels, against the floating-point conditioning bound B eps_mach N / (dN/dmu), dN/dmu = sum g f (1 - f)/T, B = number of levels (plus 3 U(mu) for the reference, whose mu is a Richardson combination); 270 comparisons; largest |Rust mu - 40-digit root on its levels|: N2352_lam0_a00_T50 6.661e-16 (bound 5.140e-14), N2352_lamm1_a00_T50 6.661e-16 (bound 4.048e-14), N2352_lamp1_a00_T10 -4.441e-16 (bound 1.246e-14); largest |reference mu - 40-digit root on its levels|: N2352_lamm1_a00_T20 -1.998e-15 (bound 3.021e-11), N2352_lamm1_a00_T50 1.110e-15 (bound 3.457e-10), N2352_lamm1_a00_T10 -4.441e-16 (bound 8.385e-12); failures: none
* the Rust solver's stated first-order rounding bound of mu (thermodynamics.csv mu_rounding_bound, solver/src/mermin.rs), tested on the exact doubles of the canonical `single` run (`--mermin-levels`, shortest round-trip; they round to the committed 16-digit mu and levels): |mu_Rust - root| <= mu_rounding_bound, the root of sum g f = N on those levels and the difference in 40-digit arithmetic, in every thermal state; 270 comparisons; root form of the canonical runs: LogBalance; largest |mu_Rust - root| / bound 0.089 (N2352_lamp1_a00_T10: |mu_Rust - root| 1.012e-16, bound 1.134e-15); largest |mu_Rust - root| 2.868e-16 (N592_lamp1_a20_T50); largest stated bound 9.433e-14 (N2352_lamm1_a20_T50); N8_lamm1_a00_T10 (the state of the former 8.3e-10 m error): |mu_Rust - root| 5.655e-18, bound 2.108e-16; failures: none

340 reference result files; files with CRLF: none; manifest.json lists 339 files with SHA-256 (339 result files besides it); mismatches: none. this checker ran run_reference.py again into a fresh directory (<work>/reference-repeat; exit SUCCESS: True; its jobs computed beforehand in parts into a separate job cache, run_reference.py --cache DIR --stage 1|2 --part i/n): 340 result files, same file set: True, differing files: none; report ks-reference.json byte-identical: True.

## Timings (this machine, 24 cores)

Runs of 2026-10-17 (the corrected metric, the record of `claude_failures.md` H15; every call under `timeout -k 5 423`, the machine otherwise idle):

* `run_reference.py` (canonical) in two stages of six parts each with the job cache `--cache DIR --stage 1|2 --part i/6 --jobs 20`, then the assembly (4.4 s); the parts' times are in `../reference/README.md`.
* `measure_rust_refinement.py --jobs 20`: 550 `single` runs (275 states, canonical and refined) in 108.8 s.
* The checker's reference repeat into its own job cache: stage 1 193.4, 176.5, 213.9, 184.1, 105.3, 182.7 s, stage 2 130.0, 133.9, 125.5, 128.2, 130.3, 135.0 s.
* `crosscheck_ks.py --jobs 22 --repeat-cache DIR`: 87.6 s in total (the 40-digit mu roots, the assembly of the reference repeat from the cache and the comparisons); 31 checks, all PASS.

The runs of 2026-10-08 and 2026-10-14 (the earlier records) are in the git history of this file.

## The record of the corrected metric (2026-10-16/17)

Both solvers were moved to the corrected primordial metric (solver README, "The corrected metric"; reference README,
"The corrected metric"): the hidden scale f = e^{-a4/3}, kappa = e^{-a4} constant in y, P = e^{-3Hy}/Vol_7, the fold
joining two halves of a cell, N_mid = 592, N_large = 2352, lambda_1 = 157.7, 2.131, 0.5363, lambda_2 = 473.1, 6.393, 1.609.
The checker's tolerance rule is unchanged. What changed in `crosscheck_ks.py` and `measure_rust_refinement.py`:
* the integrals carry the weight e^{3Hy} (the key `emtIntegrals_2Vol7_int_e3Hy` of `single`), the fold value is the
  profile end point at y = 0 (the names `*_brane` are kept), and the texts state the corrected metric;
* `adiabatic_dE_da4`: the EMT form of the history is dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0
  (= -3 P3 + P_t + P0/3), so U_Rust = 3 U_Rust(int p3) + 3 |beta/2 - 1| U_Rust(int p_t) + |beta/2 - 1| U_Rust(int p0);
* `ground_profiles`: the roundoff floor of a profile is set by the maximum of its family (n, S, Q: max |n|; rho, p3,
  p_t, p0, e_int: the largest of their maxima; M_eff, v_v: their own), because S and p0 vanish identically for the
  lambda = 0 fold-band states and a profile's own maximum is then roundoff (`claude_failures.md` H6, H9);
* the exact-Fock variant: the matrix and `single --exx` both solve it at the occupations of the converged uniform-gas
  ground state, started from it (`claude_failures.md` H3);
* the reference repeat is computed beforehand in two stages of parts (`--stage 1|2 --part i/6`);
* the matrix-wide profile uncertainty of the determinism report is read in units of the profile family's maximum
  (`claude_failures.md` H14), and the reference's SCF tolerance (the noise floor of its temperature quotients) from its
  `parameters.json` instead of a constant;
* the first run of the cross-check on this record failed 3 of 31 checks (`claude_failures.md` H15): int_p0 and the
  exact-Fock first-order difference differed by about 2.4e-10 and 3.4e-10, from the SCF stopping errors of both
  solvers, which entered neither uncertainty (the Rust refined run stopped at the same iteration as the canonical
  one, and the Richardson term of the reference does not see an error that is nearly the same on its three grids);
  and the reference's sea-hole list was shorter than three Rust thermal label sets. The Rust refined run now stops at
  the SCF tolerance 1e-14 (its canonical record is unchanged), the reference solves every state to 1e-14 m and evaluates
  the sea holes over max(5, 10%) more shells than its label set; the tolerance rule is unchanged.

The run of 2026-10-17: 31 of 31 checks PASS (section Results); the reference repeat, computed into its own cache, is byte-identical to the committed reference.

## History

1. The first cross-check covered a representative subset (18 of 75 ground states, 8 of 135 thermal states).
   It failed `thermo_state_functions` in N8_lamm1_a00_T10. Rust's mu was 0.2100104489071649 and the reference's
   0.2100104497343054 (|diff| 8.27e-10 against a tolerance of 7.97e-12). The diagnosis: the 40-digit roots on
   both solvers' levels agreed to 4.0e-13; Rust's floating-point mu, from the direct count sum g f - N, missed
   its own root by the conditioning error eps_mach N/(dN/dmu). Rust was repaired (`solver/src/mermin.rs`).
   The rerun on the subset then passed 23/23.
2. The cross-check now covers the full matrix and the derived results listed above. The tolerance rule is
   the same. That run (2026-10-01) gave 29 checks, all PASS.
3. Re-run against the current solver (2026-10-08). The 2026-10-01 run predated the Rust changes of 2026-10-07.
   Those changes re-derived the rounding bound of mu in `solver/src/mermin.rs` and added the column
   `mu_direct_count_minus_mu` (`solver/src/runs.rs`). In `thermodynamics.csv` the column `mu_rounding_bound`
   changed in all 135 rows; mu and every other number stayed the same. With the current binary the 550
   refinement runs reproduce every number of the 2026-10-01 measurement bit for bit; only the new fields were
   added. The 29 former checks give the same details as before, and `ks-crosscheck-table.csv` is byte-identical
   to the 2026-10-01 table. Two checks were added: `thermo_levels` (every thermal level) and
   `thermo_mu_rust_stated_bound`. The tolerance rule is unchanged. A first version of the stated-bound check
   was run on scratch outputs only. It took mu and the levels from the 16-digit outputs and passed with a worst
   ratio of 0.620. That measure includes the rounding of the outputs (up to about 6e-16 m), which is as large as
   the bound itself. The check therefore uses the exact doubles of `single --mermin-levels` (worst ratio 0.149).
