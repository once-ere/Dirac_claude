# pairing/kohn_sham — theorem T3 (the Kohn-Sham level of the pairing, SPEC section 9)

Revision code only (nothing from the old stages). T3 is proved here by exact symbolic computation, twice and
independently; a completion (2026-10-08) adds three exact checks found necessary by an adversarial verification, and
two numerical demonstrations solve the +M and -M universes with the Revision Rust solver and the independent
reference solver.

| file | engine | role |
| --- | --- | --- |
| `wolfram/verify_t3.wls` | Wolfram | the proof steps of T3; writes `t3-theory.json` (hypotheses, statement, proof, what is not established) and `reports/wolfram-t3.json` (10 checks) |
| `python/check_t3.py` | sympy | independent re-derivation of every step; compares with `t3-theory.json`; records the numerical self-test of the Rust Kohn-Sham solver as a confirmation (not a proof); writes `reports/python-t3.json` (13 checks) |
| `wolfram/verify_t3_completion.wls` | Wolfram | completion: the Kohn-Sham potentials read from ks-theory.json, the filling convention carried onto the -M member, the 16-component Krein expectation rule (statement S6); writes `t3-completion.json` and `reports/wolfram-t3-completion.json` (3 checks) |
| `python/check_t3_completion.py` | sympy | independent re-derivation of the completion; confirms the T3 reports; reads the two demonstrations as data; compares with `t3-completion.json`; writes `reports/python-t3-completion.json` (7 checks) |
| `numerics/t3_rust_demo.py` | Rust solver | numerical demonstration on the whole canonical matrix (210 states); writes `reports/t3-rust-demo.json` (7 checks) and `numerics/results/t3-rust-states.csv` |
| `numerics/t3_reference_demo.py` | reference solver | numerical demonstration with the independent finite-difference reference (18 states) and the -M universe of the two solvers compared; writes `reports/t3-reference-demo.json` (7 checks) and `numerics/results/t3-reference-states.csv` |

Inputs: `Revision/kohn_sham/ks-theory.json` (the Kohn-Sham problem: block equation, functional, densities,
energy-momentum tensor, boundary conditions, block basis V, expectation rule), `Revision/algebra/gammas.json`, and for
the demonstrations the solvers `Revision/kohn_sham/solver` (Rust, `single` subcommand) and
`Revision/kohn_sham/reference/ks_fd.py` (used read only), `Revision/kohn_sham/results/parameters.json` (the N and
lambda of the canonical matrix), `results/ground/summary.csv` and `results/thermo/thermodynamics.csv` (the +M runs must
reproduce them) and `Revision/field_equations_a4/reports/ks-source-conditions.json`.

## The prescribed background

T3 is a statement at a fixed slice a4,0 = a4(x4) and uses no history. The demonstrations solve the slices
a4,0 = 0, 0.5, 1, 1.5, 2 of the Kohn-Sham history a4 = A H x4 (A = 1), along which the extra times x5, x6, x7 deflate
exponentially (scale factor e^{-a4} sin^{1/6} z). That history is a PRESCRIBED BACKGROUND
(`Revision/kohn_sham/ks-theory.json` adiabaticity.historyStatus): the Kohn-Sham states violate the source conditions
of the a4 equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`, 5/5 checks), so the Kohn-Sham
gas is a test field without back-reaction, and nothing computed along the history is a consequence of the coupled
field equations.

## Run (from the repository root)

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml        # or with CARGO_TARGET_DIR=<scratch>
python Revision/pairing/kohn_sham/numerics/t3_rust_demo.py --solver <target>/release/revision_ks_solver --work <scratch> --jobs 8
python Revision/pairing/kohn_sham/numerics/t3_reference_demo.py --jobs 8
python Revision/pairing/kohn_sham/python/check_t3_completion.py
```

Each exits with code 0 only if every check passes; two runs give byte-identical outputs (LF). The reference
demonstration compares its -M universe with the Rust table, so it runs after the Rust demonstration; the sympy
completion checker reads both demonstration reports, so it runs last. Run times on the development machine (shared
with other jobs): about 3 s and 1 s (T3 verifiers), 15 s and 2 s (completion), 10 to 15 min for the Rust
demonstration (630 `single` runs, 8 at a time; `--reuse` re-reads the outputs of a former run in `--work`) and about
10 min for the reference demonstration (54 members on three grids, 8 processes).

## The theorem

The block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of the 16-component orbital), with
the brane parities exchanged and the tip angle theta -> pi - theta, maps every self-consistent instantaneous
Kohn-Sham state with (m, lambda, theta) onto one with (-m, +lambda, pi - theta), with equal levels, occupations,
Kohn-Sham energy, grand potential and energy-momentum profiles, and S -> -S (`t3-theory.json`, S1-S5). The completion
adds S6: with the expectation rule rho = sum f u u^dagger B of the canonical quantisation the image state has
rho' = -Gamma rho Gamma, so n is unchanged, S and Q change sign, and every component of the 16-component
energy-momentum tensor and of the current is unchanged (`t3-completion.json`). The Z2 brane is ASSUMED (as in
`Revision/kohn_sham/ks-theory.json`); the states are instantaneous (adiabatic) mean-field states; nothing here is a
creation process.

## Adversarial verification (2026-10-08) and completion

Both T3 verifiers were re-run and reproduce `t3-theory.json`, `reports/wolfram-t3.json` and `reports/python-t3.json`
byte for byte; every proof step was re-derived. No error was found in the statement or the proof. Gaps found and
closed (details in `t3-completion.json` adversarial_verification):

1. `verify_t3.wls` writes the Kohn-Sham coefficients 15/16, -1/16, 15/32, -1/32 into the script instead of reading
   ks-theory.json, and its v_v clause compares an expression with itself: `T3C_mean_field_coefficients_from_ks_theory`.
2. The filling convention (hypothesis H5) was used for the -M member without showing that its particle set is the
   image of the +M member's: `T3C_filling_convention_mapped`.
3. The proof covers the four diagonal energy-momentum components of the 2 x 2 reduction; the 16-component Krein rule
   gives every component and the current: `T3C_krein_rule_16_component`.
4. The recorded numerical confirmation was the solver's two-state self-test: the two demonstrations below.

`t3-theory.json` and the two T3 reports are left byte-identical, because `Revision/docs/PAIR_CREATION_PROOFS`,
`Revision/docs/DIRAC16COMPLEX_FIELD_THEORY`, the publication tests in `Revision/tests/` and
`wolfram/WOLFRAMSCRIPT_PROVENANCE.md` quote their checks, counts and sha256; the completion is a separate record.

## The numerical demonstrations (not part of the proof)

Members of each state: plus = the +M universe (m, lambda, tip theta = 0); image = the -M universe (-m, +lambda,
tip theta = pi); control = (-m, +lambda) with the UNtransformed tip theta = 0. Numbers from the reports:

* Rust solver (`reports/t3-rust-demo.json`), all 75 ground and 135 Mermin states of the canonical matrix
  (N = 8, 136, 688; lambda = 0, +-lambda_1, +-lambda_2 at T = 0 and 0, +-lambda_1 at T = 0.01, 0.02, 0.05; the five
  slices): the plus members reproduce the committed canonical matrix to 2.538e-10. Image = plus to 2.179e-13 (ground)
  and 3.877e-12 (thermal), tolerance 1e-9: levels label by label with the sector map (n2, j, parity) ->
  (n2, -j, other parity), occupations, E_KS, mu, entropy, Omega, F, HOMO, LUMO, gap, the energy-momentum integrals,
  the even profiles pointwise and S, Q, M_eff with opposite sign. The shooting method is covariant under the map (the
  Pruefer equation of the image is that of the original with theta -> pi/2 - theta), so this equality is at the
  rounding level by construction: it tests the solver's handling of the transformed boundary conditions, labels,
  filling convention, self-consistency and Mermin root for both members. Negative control: with the untransformed tip
  the density profile n(y) differs from the plus state's by at least 4.750 of its maximum (N8_lamm1_a15; the k = 0
  zero modes (e^(-m y), 0) of -m are localised at the tip) in the 196 states where the solver finds a control state;
  in 14 states (all with lambda < 0) its SCF diverges, also in its coupling continuation (reported as such, not as a
  proof that no state exists). The T1 parameters (-m, -lambda, tip pi) differ from the plus state by at least
  1.21e-2 (combined measure of levels, energies, energy-momentum integrals and n(y)) in all 150 states with
  lambda != 0: the Kohn-Sham partner carries +lambda. Repeated runs (one of them from scratch) gave byte-identical
  tables.
* Reference solver (`reports/t3-reference-demo.json`), 13 ground and 5 Mermin states: the reference is used unchanged
  for plus and control; for the image its rotated frame gets the tip end rotated by pi/2 (checked: bit-identical to
  the reference's frame for theta = 0; exact k = 0 image spectra to 2.80e-14). Image = plus to 2.043e-14 (ground) and
  3.038e-14 (thermal) after Richardson extrapolation, while on a single grid the two discretisations differ by up to
  2.23e-4 (the image frame is not the discrete image of the plus frame: this equality is the discretisation-independent
  test, a continuum statement). With the untransformed tip the density profile differs by at least 5.296 of its
  maximum (N8_lamm2_a00; 3 states without a converged control, all with lambda < 0). The -M universe of the
  reference and of the Rust solver agree to 1.255e-11. Two runs gave byte-identical tables.

## What is not established

No creation process, rate or amplitude; instantaneous (adiabatic) mean-field states on a prescribed background
without back-reaction; the ASSUMED Z2 brane, the chosen tip and the filling CONVENTION; not a statement about two
independently quantised universes; the pairing is (m, lambda) -> (-m, +lambda), not (-m, -lambda). See the
`not_established` lists of `t3-theory.json` and `t3-completion.json`.
