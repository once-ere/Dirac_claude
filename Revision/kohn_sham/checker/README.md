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
