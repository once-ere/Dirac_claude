# Revision Kohn-Sham cross-checker (Rust solver vs the independent Python reference, full matrix)

This directory compares the committed canonical Rust results (`Revision/kohn_sham/results`) with the independent
reference (`Revision/kohn_sham/reference/results`) on the FULL canonical matrix. The comparison covers every
ground state (75), every thermal state (135, with every level label by label), the exact-Fock variant SCF energies
and gaps (60), the rescaling partners (60), the particle-hole lists (75), the sea-hole diagnostic (135) and the
crossing demonstration (5 slices). It also tests the stated rounding bound of the repaired Rust Mermin root
against 40-digit roots. The reference uses staggered finite differences with Richardson extrapolation; Rust uses
shooting with RK4 and a Pruefer count. Revision code only.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction,
y = ln(sin z)/(6H).

## Run (from the repository root; the Rust binary must be built: `cargo build --release` in `../solver`)

```
python Revision/kohn_sham/reference/run_reference.py --jobs 22                                   # the reference (once)
python Revision/kohn_sham/checker/measure_rust_refinement.py --work <scratch>/rust-single --jobs 22   # writes rust-refinement.json
python Revision/kohn_sham/checker/crosscheck_ks.py --work <scratch>/cc --jobs 22                  # writes the reports
```

`crosscheck_ks.py` runs the reference a second time itself, into a fresh `<work>/reference-repeat`. It then
compares every result file and the report `ks-reference.json` byte for byte with the committed ones (check
`reference_repeat_byte_identical`). No repeat directory from elsewhere is accepted. It also recomputes mu in
40-digit arithmetic in parallel processes for 405 level sets: the 16-digit levels of both solvers (270) and the
exact Rust levels (135).

Outputs: `Revision/kohn_sham/reports/ks-crosscheck.json` (every check with name, verdict and detail, plus a
`diagnosis` for a failing check) and `Revision/kohn_sham/reports/ks-crosscheck-table.csv` (every scalar
comparison with both values, both uncertainties, the tolerance and the ratio; the 9616 levels and 113250
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
    significant digits, so the exact values are needed to test the rounding bound of mu (about 1e-16 m).
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

## Results (`reports/ks-crosscheck.json`: 31 checks, all PASS; run of 2026-10-08)

Preconditions all pass. The reference report has 37/37 PASS, the Rust solver report 42/42 PASS and the Rust
determinism report 14/14 PASS. The 550 refinement runs cover every state. The canonical `single` runs
reproduce the committed ground and thermal matrix exactly (every difference 0). The crossing-demonstration
energies agree to 1.1e-13 relative (summation order of the continued occupation). The exact-Fock single runs
agree with the matrix to at most 0.017 of N x scfTolerance in E (1.2e-10, N688_lamp1_a00) and 0.020 of
6 scfTolerance in the gap (1.2e-12). The problem definitions are
identical. The reference re-derives the same N_mid = 136, N_large = 688, N_demo = 696 and the same six
couplings.

Rust and the reference agree within the stated tolerances everywhere. Each line gives the number of
comparisons and the largest ratio |diff| / tolerance.

* occupied levels, occupations, HOMO and LUMO groups: identical in all 75 ground states (300 comparisons).
* E_KS, E_band, E_int (225): 0.148.
* HOMO, LUMO, gap (225): 0.001.
* levels label by label (9616): 0.324.
* Delta-SCF and E_excited (150): 0.296.
* particle-hole lists (4842 comparisons): the Rust lists hold 1610 rows. 60 lists have 24 rows; 15 have
  fewer (3 to 21), because they hold every excitation below Rust's lowest excluded level. 1589 rows are
  compared, and each is in the reference list with the same groups, multiplicity and sector flag. The
  delta_eps worst ratio is 0.001, and no reference excitation is missing from Rust. The other 21 rows (16
  states, at most 5 in N136_lam0_a00) have the particle at or above one solver's lowest excluded level and
  are not compared.
* EMT integrals (375): 0.225.
* brane and tip values (600): 0.495.
* profile points (113250): 0.495.
* Delta E_x (75): 0.044.
* dE/da4 in both forms (150): 0.122.
* Q_max, its pair, matrix element and level spacing (225): 0.314. Both solvers give Q_max = 0 for N = 8.
* exact-Fock variant: E_EXX, gap and E_EXX - (E_uniform_gas + Delta E_x) in all 60 states (240): 0.128. Both
  solvers have the same aufbau occupation as the uniform-gas state.
* rescaling partners (180): partner_E_KS 0.137; partner dk and v_t identical; the Rust identity flags true.
* crossing demonstration (31): the same flags (occupied set equal to a4,0 = 0 only at a4,0 = 0; open shell from
  0.5 on), the same labels left (0:+-1:odd:0) and entered (12:+1:even:0), and E_aufbau, E_continued and their
  difference agree (worst 0.111).
* thermal mu, E, S, F, Omega in all 135 states (810): 0.284.
* C_V, dE/dT and -dF/dT (405): 0.226.
* sea-hole diagnostic (270): 0.048, and the same verdict on the 1% criterion in every state where the
  reference decides it. Rust has 15 of 135 states above 1% of N (largest N8_lamm1_a20_T50, 30.98 N).
* thermal levels label by label in all 135 states (33973 levels; 34378 comparisons with the label and coverage
  flags): 0.312 (N688_lamm1_a00_T50, level 0:+1:odd:2, |diff| 1.4e-10 against a tolerance of 4.5e-10). Every
  level with f >= 1e-12 is in both sets. The lowest Rust label agrees with label_min of the ground levels files
  in all 20824 sectors where both occur.
* mu in 40 digits from each solver's own levels (270): 0.050. The DIAGNOSTIC: the Rust floating-point mu
  differs from the 40-digit root on its own levels by at most 6.7e-16 m. This is measured on the 16-digit
  outputs, so it includes their rounding. That is the repaired Mermin root of `solver/src/mermin.rs`. Before the
  repair the error was 8.3e-10 m in N8_lamm1_a00_T10; see History.
* the stated rounding bound of the Rust mu, on the exact doubles (135 states, 270 flags): |mu_Rust - root| <=
  `mu_rounding_bound` in every state. The largest ratio is 0.149 (N688_lam0_a00_T10: 1.03e-16 m, bound
  6.9e-16 m). The largest |mu_Rust - root| is 2.43e-16 m (N136_lamp1_a20_T50) and the largest bound 4.77e-14 m
  (N688_lamm1_a20_T50). N8_lamm1_a00_T10, where the former direct count was 8.3e-10 m off, gives 2.5e-17 m
  (bound 3.2e-16 m). All 135 canonical runs use the root form LogBalance. These numbers equal those of the
  solver's own tool (`reports/ks-rust-mermin-roots.json`); the checker computes them independently.

The reference output is LF-only and matches its manifest (339 files). The checker's own repeat run of the
reference is byte-identical in all 340 files and in the report.

## Timings (this machine, 24 cores)

Run of 2026-10-08. Other workflows ran on the machine at the same time (after the second run, for example, 21
Rust solver processes and 7 Python processes of other workflows). These times are therefore longer than those of
2026-10-01 (in brackets).

* `run_reference.py` (canonical, 22 processes): 578.3 s on 2026-10-01; details in `../reference/README.md`.
* `measure_rust_refinement.py`: 85.2 s and 61.3 s [31.6 s, 31.3 s] for 550 Rust `single` runs on 22 threads
  (each run is one process). The slowest single run took 50.8 s and 33.0 s [19 s] (refined N688_lamm1_a20_T50
  and N688_lamp1_a20_T50). Two runs give byte-identical `rust-refinement.json`.
* `crosscheck_ks.py` (22 processes): 721.2 s and 777.1 s in total [588.9 s, 554.1 s]. Of that, the reference
  repeat it runs itself takes 692.9 s and 748.0 s [570.8 s, 536.1 s]. The 40-digit mu roots take 27.3 s and
  27.7 s [17.5 s]; they are 405 level sets in a process pool (270 before the exact Rust levels were added). The
  comparisons themselves take about 1 s. Two runs give byte-identical `ks-crosscheck.json` and
  `ks-crosscheck-table.csv`. Each repeat of the reference is byte-identical to the committed reference (340
  files and the report).

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
