# Revision Kohn-Sham cross-checker (Rust solver vs the independent Python reference)

This directory compares the committed canonical Rust results (`Revision/kohn_sham/results`) with the independent
reference (`Revision/kohn_sham/reference/results`) on the reference subset of the canonical matrix. The
reference uses staggered finite differences with Richardson extrapolation; Rust uses shooting with RK4 and a
Pruefer count. Revision code only.

Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially
DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction,
y = ln(sin z)/(6H).

## Run (from the repository root; the Rust binary must be built: `cargo build --release` in `../solver`)

```
python Revision/kohn_sham/checker/measure_rust_refinement.py --work <scratch>/rust-single      # writes rust-refinement.json
python Revision/kohn_sham/checker/crosscheck_ks.py --reference-repeat <scratch>/repeat           # writes the reports
```

Outputs: `Revision/kohn_sham/reports/ks-crosscheck.json` (every check with name, verdict and detail) and
`Revision/kohn_sham/reports/ks-crosscheck-table.csv` (every scalar comparison with both values, both
uncertainties, the tolerance and the ratio).

## Tolerance rule (fixed in `crosscheck_ks.py` before any comparison; never adjusted to a result)

```
|x_Rust - x_ref| <= 3 (U_ref + U_Rust) + 1e-12 scale
```

* `U_ref` is the reference's measured grid uncertainty: the size of the h^4 term of the three-grid
  Richardson value on the finest grid. A fourth grid (G = 2400) validates it for one state.
* `U_Rust` is (16/15) |canonical - refined| of the Rust solver. RK4 makes the refined error 1/16 of the
  canonical one, so this difference times 16/15 estimates the canonical error.
  * `measure_rust_refinement.py` measures it per state and per quantity: it runs the Rust `single` command
    with the canonical and the refined numerics and the label-set margin of the canonical matrix. This covers
    energies, EMT integrals, every level (largest difference of the state), every profile (largest
    difference of that profile), the brane and tip values, mu and the entropy. The canonical `single` run
    must reproduce the committed matrix (check `rust_refinement_applies_to_matrix`).
  * Quantities that `single` does not report (Delta-SCF, Q_max, the finite-difference dE/da4, C_V) take the
    maximum over the whole canonical matrix from `reports/ks-rust-determinism.json`, as stated in each check.
* `scale` is max(1, |x|) for scalars and the profile maximum for profiles. It provides a roundoff floor.
* dE/dT and -dF/dT are difference quotients of energies over dT = 0.01 T. Each solver's stated noise floor is
  therefore added: N x rootTolerance / dT for Rust (as in its `thermo_CV_identity` check) and N x 1e-12 / dT
  for the reference (its SCF tolerance, as in its own identity check). C_V = T dS/dT carries no such floor.

The re-derived couplings must be identical after rounding. The coupling strength is a maximum over y. The
reference reports the continuous maximum; Rust reports the largest of its fine-grid samples (spacing
L/1800). For an interior maximum the Rust value must therefore lie below the reference value, by at most the
sampling bound |f''| s^2/8 (f'' is the reference curvature at the peak), within the uncertainties.

## Results (`reports/ks-crosscheck.json`: 23 checks, 22 PASS, 1 FAIL)

Preconditions all pass. The reference report has 28/28 PASS, the Rust solver report 40/40 PASS and the Rust
determinism report 13/13 PASS. The canonical `single` runs reproduce the committed matrix exactly (every
difference 0). The problem definitions are identical. The reference re-derives the same N_mid = 136,
N_large = 688 and the same six couplings. For interior maxima the Rust strengths lie below the continuous
maxima and within the sampling bound (largest gap 3.3e-3 for N = 688 at a4,0 = 2, bound 4.5e-3).

Rust and the reference agree within the stated tolerances. Each line gives the largest ratio
|diff| / tolerance.

* occupied levels, occupations, HOMO and LUMO groups: identical in all 18 ground states.
* E_KS, E_band, E_int: 0.148.
* HOMO, LUMO, gap: 0.001.
* 2987 levels label by label: 0.324.
* Delta-SCF and E_excited: 0.106.
* EMT integrals: 0.225.
* brane and tip values: 0.495.
* 27180 profile points: 0.495.
* Delta E_x: 0.022.
* dE/da4 in both forms: 0.122.
* Q_max, its pair, matrix element and level spacing: 0.314. Both solvers give Q_max = 0 for N = 8.
* C_V, dE/dT and -dF/dT: 0.218.
* In the other seven thermal states, mu, E, S, F and Omega agree (the failing state is below).

The reference output is LF-only, matches its manifest, and a repeat run is byte-identical.

**FAIL: `thermo_state_functions`, state N8_lamm1_a00_T10 (mu and both Omega forms).** Rust's mu is
0.2100104489071649 and the reference's is 0.2100104497343054 (|diff| 8.27e-10). The tolerance is 7.97e-12,
because the measured U_Rust(mu) is 6.5e-16. Omega = F - mu N inherits 8 times that difference.

**Diagnosis.** The check `thermo_mu_high_precision` (PASS) and the DIAGNOSTIC `thermo_mu_rounding_diagnostic`
(PASS) establish the cause.

* The 40-digit roots of the Mermin condition on Rust's own final levels and on the reference levels agree to
  4.0e-13, so the two solvers' physics agree.
* Rust's floating-point mu lies -8.27e-10 from the root on its own levels. This is the floating-point
  conditioning of the direct count sum g f = N: the state is deep in the activated regime (dN/dmu = 1.24e-6;
  bound B eps_mach N / (dN/dmu) = 1.0e-8).
* Rust's canonical and refined runs carry nearly the same rounding error, so its measured U(mu) (6.5e-16)
  does not see it.
* E, S, F, C_V, dE/dT and -dF/dT of that state agree. Thermal levels are not compared one by one; they
  enter only through the 40-digit roots above.

The tolerance was not changed. The failure stands as a numerical defect of the reported Rust mu (and Omega)
in deeply activated states. Its size is at most the conditioning bound, about 1e-9 m here. The remedy is to
solve for mu with the well-conditioned residual that the reference now uses, in `solver/src/scf.rs`,
function `mermin`. The reference had the same defect (1.15e-9) in its first run, and that was fixed; see
`../reference/README.md`.

## Timings (this machine)

* `measure_rust_refinement.py`: 14.6 s for 52 Rust `single` runs on 20 threads. Two runs give
  byte-identical `rust-refinement.json`.
* `crosscheck_ks.py`: 24.8 s, mostly the 40-digit mu roots. Two runs give byte-identical reports.
