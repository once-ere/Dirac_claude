# Provenance of the Lovelock computation (written BEFORE any comparison with the author's answers)

This file records, at the moment the results were first committed, exactly what was read and what
was computed. The comparison with the author's own answers is done afterwards, in a separate,
later commit, so that the order can be checked in the git history.

## What was read from the author's notebook

* File: `Generalized _Kronecker_Delta_4+4.nb` (sha256
  `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb`).
* Only its INPUT cells were extracted, by `Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls`, which converts
  each input cell to text without evaluating it and never touches an output cell. What that
  extraction showed (label, size, first 160 characters of every input cell) is
  `Revision/gkd_lovelock/results/notebook-input-cells.txt`.
* The definition used: the cell stored in the file as `In[87]` (the author's `In[54]`):
  `kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]`.
* The Lovelock definition: the cell stored in the file as `In[101]` (the author's `In[68]`) is an
  image of Lovelock's equation (4.38); it was rendered by `Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls` to
  `Revision/gkd_lovelock/results/notebook-in68-image.png` and read from that picture.
* Not opened: any output cell of this notebook, the file `Generalized_Kronecker_Delta.txt`, and the
  author's other Mathematica files.
* The metric was taken from the author's message (the 8 x 8 list in the task), not from a file.

## What was computed, and by what

* `Revision/gkd_lovelock/code` (pure Rust, no dependencies): exact rational Laurent polynomials, exact
  derivatives, the Christoffel symbols and the Riemann tensor of the metric, GKD (the pure-Rust
  refactoring of kδ), and the three Lovelock tensors of (4.38) for n = 8 (k = 1, 2, 3).
* Commands (from the repository root):

```text
cargo build --release --manifest-path Revision/gkd_lovelock/code/Cargo.toml
Revision/gkd_lovelock/code/target/release/lovelock_gkd gkd-selftest --exhaustive-max 4 --output Revision/gkd_lovelock/results
Revision/gkd_lovelock/code/target/release/lovelock_gkd lovelock --output Revision/gkd_lovelock/results --brute-force-k2
```

* Outputs: `curvature.json`, `lovelock-tensors.json` (every component, in Mathematica and LaTeX form
  and as exact monomial lists), `lovelock-components.md`, `lovelock-report.json` (19 checks, all
  passed), `gkd-selftest.json` (GKD equals the literal determinant for all 16,777,216 pairs of index
  lists of length 4 over 8 values and for 200,000 pseudo-random pairs of each length 5 to 9).
  Two runs give byte-identical files.
* The checks are mathematical identities, not comparisons with the author's numbers: P_(1) = -4 G
  (the Einstein tensor from the Ricci tensor), the trace identities, zero divergence, symmetry,
  P_(4) = 0, and the literal unpruned sums over all 8^4 and 8^8 index lists at a numerical point.

## Location

This work was first committed under `studies/lovelock_gkd` and `artifacts/lovelock-gkd` (commit
3e81eeb, 2026-10-01 07:15) and moved on 2026-10-01 into `Revision/gkd_lovelock/` (code/, results/,
notebook_reading/) with `git mv`, unchanged, when the author asked for all new calculations for this
metric to be kept in the new folder `Revision`.  The files in `verification_unfinished/` were written by a
verification workflow that was stopped at the author's request before it finished; they are NOT verified
and are not used for any result until they have been run and checked.

## Later note (2026-10-01, appended; nothing above is changed)

* The verification was finished in `Revision/gkd_lovelock/verification/` (`verify_lovelock_gkd.wls` with
  `LovelockGKDCheck.wl`, report `wolfram-gkd-report.json`, 29 checks; `check_lovelock_gkd.py`, report
  `python-lovelock-report.json`, 49 checks; all pass). The unfinished files of `verification_unfinished/` were
  removed and are not used.
* The two notebook-reading outputs are reproduced by these commands (from the repository root):

```text
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
python Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
```

  The first writes the full InputForm text of the 58 input cells to `build/lovelock_nb_inputs.txt` (or to
  `$LOVELOCK_NB_INPUTS`; not committed), the second writes the digest `notebook-input-cells.txt` from it
  (byte-identical to the file recorded above), the third renders the image `notebook-in68-image.png` without the
  PNG text and time chunks that `Export` adds, so that two runs are byte-identical (the pixel data are those of
  the first rendering).

## Later note (2026-10-16, appended; nothing above is changed): the corrected metric (version 2)

* On the user's orders of 2026-10-16 (the remedy of `Revision/metric_warped/`, `Revision/SPEC.md` section 1, version 2;
  "go ahead with the recomputation using the corrected metric"; `HANDOFF.md` 0.10, phase W4) the program computes the
  corrected metric diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0,
  for general a4(x4), b4(x4) > 0 and EVERY real z with Sin z Cos z != 0 ((Sin^2)^(1/6) the positive branch).  Changed:
  `poly.rs` (the symbol S = Sin^(1/3) is replaced by W = (Sin^2)^(1/12) > 0 with d/dx0 W = H C W, and the new symbol
  G = Sign[Cot z], G^2 = 1, zero derivatives; 14 exponents per monomial), `geometry.rs` (the metric; sqrt|det g| =
  G C E^-1 Q^4 W^3 = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4), its square asserted equal to det g; the unit tests now run in
  all four quarters of the period of z), `main.rs` (the metric text; the checks `mixed_riemann_free_of_x0`,
  `mixed_riemann_only_sectional`, `sqrt_det_g_positive_every_quarter`, and for k = 1, 2, 3 `k<k>_free_of_x0`,
  `k<k>_offdiagonal_vanishes`, `k<k>_hidden_equals_extra_times`; 27 checks).  `gkd.rs`, `lovelock.rs`, `rational.rs`
  and `output.rs` are unchanged, so `gkd-selftest.json` (which does not depend on the metric) is unchanged.
* Result: 112 non-zero R^ab_cd (all of the form R^ab_ab, 28 planes; the metric of 2026-10-14 had 156), all free of x0;
  every P_(k) (k = 1, 2, 3) is diagonal and free of x0, with P_(k)^x0_x0 = P_(k)^x5_x5 = P_(k)^x6_x6 = P_(k)^x7_x7;
  `lovelock-report.json` 27 of 27 checks passed (13.3 s).  Two runs give byte-identical files.
* The results of the metric of 2026-10-14 (the files of commit c93fe22) are kept, frozen, in
  `Revision/gkd_lovelock/reference_2026_10_14/` for the comparison with the author's notebook (written for that
  metric; `Revision/gkd_lovelock/comparison/README.md` section 1.2).
* The two verifications were adapted to the corrected metric and re-run: `verify_lovelock_gkd.wls` (29 checks, exact
  zero test for every real z) and `check_lovelock_gkd.py` (56 checks; symbol form with w = |sin|^(1/6), sign(sin),
  sign(cot)); all pass (`Revision/gkd_lovelock/verification/WOLFRAMSCRIPT_PROVENANCE.md` section 7).
