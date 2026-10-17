# pairing/kohn_sham — theorem T3 (the Kohn-Sham level of the pairing, SPEC section 9)

Revision code only (nothing from the old stages). T3 is proved here by exact symbolic computation, twice and
independently; a completion (2026-10-08) adds three exact checks found necessary by an adversarial verification, and
two numerical demonstrations solve the +M and -M universes with the Revision Rust solver and the independent
reference solver. Everything is that of the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md`
section 1); the records of the withdrawn metrics are in the git history.

| file | engine | role |
| --- | --- | --- |
| `wolfram/verify_t3.wls` | Wolfram | the proof steps of T3; writes `t3-theory.json` (hypotheses, statement S1-S4, proof, what is not established) and `reports/wolfram-t3.json` (9 checks) |
| `python/check_t3.py` | sympy | independent re-derivation of every step; compares with `t3-theory.json`; records the numerical self-test of the Rust Kohn-Sham solver as a confirmation (not a proof); writes `reports/python-t3.json` (12 checks) |
| `wolfram/verify_t3_completion.wls` | Wolfram | completion: the Kohn-Sham potentials read from ks-theory.json, the filling convention carried onto the -M member, the 16-component Krein expectation rule (statement S6); writes `t3-completion.json` and `reports/wolfram-t3-completion.json` (3 checks) |
| `python/check_t3_completion.py` | sympy | independent re-derivation of the completion; confirms the T3 reports (9 and 12 checks); reads the two demonstrations as data; compares with `t3-completion.json`; writes `reports/python-t3-completion.json` (7 checks) |
| `numerics/t3_rust_demo.py` | Rust solver | numerical demonstration on the whole canonical matrix (210 states); writes `reports/t3-rust-demo.json` (7 checks) and `numerics/results/t3-rust-states.csv` |
| `numerics/t3_reference_demo.py` | reference solver | numerical demonstration with the independent finite-difference reference (18 states) and the -M universe of the two solvers compared; writes `reports/t3-reference-demo.json` (7 checks) and `numerics/results/t3-reference-states.csv` |

Inputs: `Revision/kohn_sham/ks-theory.json` (the Kohn-Sham problem: block equation, functional, densities,
energy-momentum tensor, boundary conditions, block basis V, expectation rule), `Revision/algebra/gammas.json`, and for
the demonstrations the solvers `Revision/kohn_sham/solver` (Rust, `single` subcommand) and
`Revision/kohn_sham/reference/ks_fd.py` and `run_reference.py` (used read only),
`Revision/kohn_sham/results/parameters.json` (the N and lambda of the canonical matrix),
`Revision/kohn_sham/results/ground/summary.csv` and `Revision/kohn_sham/results/thermo/thermodynamics.csv` (the +M runs
must reproduce them), `Revision/field_equations_a4/reports/ks-source-conditions.json`,
`Revision/kohn_sham/reports/ks-rust-solver.json` (the solver self-test read by `check_t3.py`) and
`numerics/results/t3-rust-states.csv` (read by the reference demonstration).

## The prescribed background

The metric is the corrected metric diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),
z = 6 H x0 real. T3 is a statement at a fixed slice a4,0 = a4(x4), b4,0 = b4(x4) and uses no history: a4 and b4 enter
the block Hamiltonians h_j = j[-(i/f) sigma1 d_y + M_eff sigma2 + kappa k sigma3] + v_v only through the positive
constants f = e^{-a4} b4^{1/2} (the hidden scale) and kappa = e^{-a4} of the slice, and the proper densities through
the cell volume Vol_7, so T3 holds for every a4 and b4. The Rust demonstration solves the slices
a4,0 = 0, 0.5, 1, 1.5, 2 (the reference demonstration the slices 0, 1, 2: N = 8 at a4,0 = 0, 1, 2 and N = 592 at 0, 2)
of the Kohn-Sham history a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4} (A = 1), along which the extra times x5, x6, x7
deflate exponentially (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12} = b4(0)^{1/2} e^{-a4/3} (sin^2 z)^{1/12}); the
coupling of each tag is the solvers' lambda_hat, held fixed while the cell volume
Vol_7(a4,0) = ell^3 v_t e^{(5/3) a4,0} grows, as in the canonical matrix. That history is a PRESCRIBED BACKGROUND
(`Revision/kohn_sham/ks-theory.json` adiabaticity.historyStatus): the Kohn-Sham states violate the source conditions
of the a4 and b4 equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`, 5/5 checks), so the
Kohn-Sham gas is a test field without back-reaction, and nothing computed along the history is a consequence of the
coupled field equations.

## Run (from the repository root)

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml        # or with CARGO_TARGET_DIR=<scratch>
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py --solver <target>/release/revision_ks_solver --work <scratch1> --jobs 10 --part 1/4
                                                                    # ... --part 2/4, 3/4, 4/4, then --reuse
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py --jobs 22 --work <scratch2> --part 1/6
                                                                    # ... --part 2/6 to 6/6, then --reuse
python Revision/pairing/kohn_sham/python/check_t3_completion.py
```

Each exits with code 0 only if every check passes; two runs give byte-identical outputs (LF). The reference
demonstration compares its -M universe with the Rust table, so it runs after the Rust demonstration; the sympy
completion checker reads both demonstration reports, so it runs last. The demonstrations run in parts (each part
solves a fixed subset of the single runs and stores them in its work folder; `--reuse` assembles them and writes the
outputs as one run would), because on the matrix of the corrected metric one invocation of the reference demonstration
does not fit into the limit of 423 s of one calculation (`claude_failures.md` H18), and the Rust demonstration is split
so that every step stays well below that limit. Run times on the development machine, 2026-10-17: the T3
verifiers 5.8 s and 1.3 s, the completion 2.9 s and 0.9 s; the Rust demonstration 630 `single` runs with `--jobs 10`
in four parts of 88, 91, 76 and 67 s and an assembly of 2 s; the reference demonstration (54 members on three grids,
`--jobs 22`, one BLAS thread per process) in six parts of 219, 170, 78, 122, 115 and 91 s (the 162 grid runs, 18 states x plus, image, control x G = 300, 600, 1200, assigned longest-first by an estimated cost) and an assembly of 2 s.

## The theorem

The block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of the 16-component orbital), with
the two fold conditions exchanged and the tip angle theta -> pi - theta, maps every self-consistent instantaneous
Kohn-Sham state with (m, lambda, theta) onto one with (-m, +lambda, pi - theta), with equal levels, occupations,
Kohn-Sham energy, grand potential and energy-momentum profiles, and S -> -S (`t3-theory.json`, S1-S4, hypotheses H1-H6).
The completion adds S6: with the expectation rule rho = sum f u u^dagger B of the canonical quantisation the image
state has rho' = -Gamma rho Gamma, so n is unchanged, S and Q change sign, and every component of the 16-component
energy-momentum tensor and of the current is unchanged (`t3-completion.json`). Filling both fold conditions is ASSUMED
(as in `Revision/kohn_sham/ks-theory.json`); the corrected metric has no Z2 orbifold and no mirror copy (both halves of
a cell carry the same chi(y)), so T3 relates two Kohn-Sham problems, (m, lambda, theta) and (-m, +lambda, pi - theta),
not a universe and its mirror image; the states are instantaneous (adiabatic) mean-field states; nothing here is a
creation process. In the metric of 2026-10-14 the record had a fifth statement, S5 (the Z2 mirror copy carried
(-m, +lambda)), and 10 and 13 checks; it was removed with the orbifold on 2026-10-17.

## Adversarial verification (2026-10-08) and completion

Both T3 verifiers were re-run and reproduced `t3-theory.json`, `reports/wolfram-t3.json` and `reports/python-t3.json`
byte for byte; every proof step was re-derived. No error was found in the statement or the proof. Gaps found and
closed (details in `t3-completion.json` adversarial_verification):

1. `verify_t3.wls` wrote the Kohn-Sham coefficients 15/16, -1/16, 15/32, -1/32 into the script instead of reading
   ks-theory.json, and its v_v clause compared an expression with itself: `T3C_mean_field_coefficients_from_ks_theory`.
   Fixed at the root on 2026-10-08: `verify_t3.wls` reads the coefficients from ks-theory.json and its check
   `T3_mean_field_map` writes v_v as a function of (m, lambda, n, S) and compares its values at the original and the
   image arguments (a broken coefficient makes the check fail; wolfram/WOLFRAMSCRIPT_PROVENANCE.md section 6.5).
2. The filling convention (hypothesis H5) was used for the -M member without showing that its particle set is the
   image of the +M member's: `T3C_filling_convention_mapped`.
3. The proof covers the four diagonal energy-momentum components of the 2 x 2 reduction; the 16-component Krein rule
   gives every component and the current: `T3C_krein_rule_16_component`.
4. The recorded numerical confirmation was the solver's two-state self-test: the two demonstrations below.

On 2026-10-17 (the corrected metric) the four verifiers were run again and reproduced `t3-theory.json`,
`reports/wolfram-t3.json` (9/9), `reports/python-t3.json` (12/12) and `reports/wolfram-t3-completion.json` (3/3) byte
for byte; `reports/python-t3-completion.json` (7/7) reads the two demonstration reports and changes with them. After
that run the detail texts were corrected, text only (no computation, check or count changed): in `verify_t3.wls` and
`check_t3.py` the exact k = 0 spectra carry the hidden scale f (chi' = f N chi, computed at f = 1), and in
`verify_t3_completion.wls` the fix of 2026-10-08 is stated in the past tense, the gamma index runs over x0, ..., x7 and
Gap 5 records the regeneration of `t3-theory.json` for the corrected metric. `t3-theory.json` does not contain these
texts; `reports/wolfram-t3.json`, `reports/python-t3.json`, `t3-completion.json` and
`reports/wolfram-t3-completion.json` differ from those of that run only in them.

## The numerical demonstrations (not part of the proof)

Members of each state: plus = the +M universe (m, lambda, tip theta = 0); image = the -M universe (-m, +lambda,
tip theta = pi); control = (-m, +lambda) with the UNtransformed tip theta = 0. Numbers from the reports:

* Rust solver (`reports/t3-rust-demo.json`), all 75 ground and 135 Mermin states of the canonical matrix
  (N = 8, 592, 2352; lambda = 0, +-lambda_1, +-lambda_2 at T = 0 and 0, +-lambda_1 at T = 0.01, 0.02, 0.05; the five
  slices): the plus members reproduce the committed canonical matrix to 1.916e-10. Image = plus to 1.853e-12 (ground)
  and 3.502e-12 (thermal), tolerance 1e-9: levels label by label with the sector map (n2, j, fold condition) ->
  (n2, -j, other fold condition), occupations, E_KS, mu, entropy, Omega, F, HOMO, LUMO, gap, the energy-momentum
  integrals, the even profiles pointwise and S, Q, M_eff with opposite sign, each profile difference measured against
  the maximum of its family (n, S, Q against max |n|; M_eff, v_v; e_int, rho, p3, p_t, p0), because S, p_t and p0 of
  the free fold-band gas vanish identically (`claude_failures.md` H17). The shooting method is covariant under the map
  (the Pruefer equation of the image is that of the original with theta -> pi/2 - theta), so this equality is at the
  rounding level by construction: it tests the solver's handling of the transformed boundary conditions, labels,
  filling convention, self-consistency and Mermin root for both members. Negative control: with the untransformed tip
  the density profile n(y) differs from the plus state's by at least 0.4657 of its maximum (N2352_lamm1_a00_T50; the
  k = 0 zero modes (e^(-f m y), 0) of -m are localised at the tip instead of the fold) in all 210 states. The T1
  parameters (-m, -lambda, tip pi) differ from the plus state by at least 5.120e-2 (N8_lamp1_a20_T10; combined measure
  of levels, energies, energy-momentum integrals and n(y)) in all 150 states with lambda != 0: the Kohn-Sham partner
  carries +lambda.
* Reference solver (`reports/t3-reference-demo.json`), 13 ground and 5 Mermin states: the reference is used unchanged
  for plus and control; for the image its rotated frame gets the tip end rotated by pi/2 (checked: bit-identical to
  the reference's frame for theta = 0; exact k = 0 image spectra to 2.80e-14). Every member is solved with the
  reference's `solve_state_robust` (one member, the control of N8_lamm2_a00 on G = 1200, needed its coupling
  continuation). Image = plus to 1.332e-14 (ground) and 3.159e-14 (thermal) after Richardson extrapolation, while on a
  single grid the levels of the two members differ by up to 1.81e-4 (the image frame is not the discrete image of the plus
  frame: this equality is the discretisation-independent test, a continuum statement). With the untransformed tip the
  density profile differs by at least 3.776 of its maximum (N592_lamp2_a00) in all 18 states. The -M universe of the
  reference and of the Rust solver agree to 7.311e-11 (N592_lamp1_a20_T50). The six-part run of 2026-10-17 (the grid split) and the earlier four-part run (one member per task) wrote byte-identical `reports/t3-reference-demo.json` and `numerics/results/t3-reference-states.csv`: the outputs do not depend on how the work is divided.

## What is not established

No creation process, rate or amplitude; instantaneous (adiabatic) mean-field states on a prescribed background
without back-reaction; both fold conditions filled (ASSUMED), the chosen tip and the filling CONVENTION; not a
statement about two independently quantised universes or about a mirror universe (the corrected metric has no mirror
copy); the pairing is (m, lambda) -> (-m, +lambda), not (-m, -lambda). See the `not_established` lists of
`t3-theory.json` and `t3-completion.json`.
