# Provenance of the Lovelock computation (written BEFORE any comparison with the author's answers)

This file records, at the moment the results were first committed, exactly what was read and what
was computed. The comparison with the author's own answers is done afterwards, in a separate,
later commit, so that the order can be checked in the git history.

## What was read from the author's notebook

* File: `Generalized _Kronecker_Delta_4+4.nb` (sha256
  `23bb4e0c70943e766d9b081a3a399ef29664889aad088041329ce2e065b80afb`).
* Only its INPUT cells were extracted, by `scripts/lovelock_extract_nb_inputs.wls`, which converts
  each input cell to text without evaluating it and never touches an output cell. What that
  extraction showed (label, size, first 160 characters of every input cell) is
  `artifacts/lovelock-gkd/notebook-input-cells.txt`.
* The definition used: the cell stored in the file as `In[87]` (the author's `In[54]`):
  `kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]`.
* The Lovelock definition: the cell stored in the file as `In[101]` (the author's `In[68]`) is an
  image of Lovelock's equation (4.38); it was rendered by `scripts/lovelock_export_nb_image.wls` to
  `artifacts/lovelock-gkd/notebook-in68-image.png` and read from that picture.
* Not opened: any output cell of this notebook, the file `Generalized_Kronecker_Delta.txt`, and the
  author's other Mathematica files.
* The metric was taken from the author's message (the 8 x 8 list in the task), not from a file.

## What was computed, and by what

* `studies/lovelock_gkd` (pure Rust, no dependencies): exact rational Laurent polynomials, exact
  derivatives, the Christoffel symbols and the Riemann tensor of the metric, GKD (the pure-Rust
  refactoring of kδ), and the three Lovelock tensors of (4.38) for n = 8 (k = 1, 2, 3).
* Commands (from the repository root):

```text
cargo build --release --manifest-path studies/lovelock_gkd/Cargo.toml
studies/lovelock_gkd/target/release/lovelock_gkd gkd-selftest --exhaustive-max 4 --output artifacts/lovelock-gkd
studies/lovelock_gkd/target/release/lovelock_gkd lovelock --output artifacts/lovelock-gkd --brute-force-k2
```

* Outputs: `curvature.json`, `lovelock-tensors.json` (every component, in Mathematica and LaTeX form
  and as exact monomial lists), `lovelock-components.md`, `lovelock-report.json` (19 checks, all
  passed), `gkd-selftest.json` (GKD equals the literal determinant for all 16,777,216 pairs of index
  lists of length 4 over 8 values and for 200,000 pseudo-random pairs of each length 5 to 9).
  Two runs give byte-identical files.
* The checks are mathematical identities, not comparisons with the author's numbers: P_(1) = -4 G
  (the Einstein tensor from the Ricci tensor), the trace identities, zero divergence, symmetry,
  P_(4) = 0, and the literal unpruned sums over all 8^4 and 8^8 index lists at a numerical point.
