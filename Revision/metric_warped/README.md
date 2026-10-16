# Revision/metric_warped — the corrected primordial metric of 2026-10-16 (version 2)

The user's order of 2026-10-16 asked for the simplest modification of the primordial metric that is probably
self-consistent with the Einstein field equations, after the author's observation that a diagonal metric is
self-consistent only if every off-diagonal component of the sources vanishes.  Version 1 of this folder (the
time-warped metric, g44 = -Sin[6 H x0]^(1/3)) is withdrawn: with z = 6 H x0 real its lapse oscillates.  Version 2 keeps
g44 = -1 and works for every real z, with Sin[z]^(1/3) = (Sin[z]^2)^(1/6) > 0:

```text
g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x1, x2, x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x5, x6, x7))
```

- `python/derive_warped_metric.py` — sympy: the off-diagonal component of the metric of 2026-10-14 at every Lovelock
  order, the oscillating lapse of version 1, the conditions of the family with g44 = -1, and the properties of the
  corrected metric (no mixed curvature, no off-diagonal component at any order, diagonal free of x0, the block of
  constant curvature, Ricci tensor, divergence of a diagonal tensor, the history's source and its conservation, the
  gravity term of the Dirac operator, a flat check) and of the alternatives.  Writes `results/warped-metric.json` and
  `reports/python-warped-metric-report.json`.
- `wolfram/verify_warped_metric.wls` (package `wolfram/MetricWarped.wl`) — the independent Wolfram check; writes
  `reports/wolfram-warped-metric-report.json`.
- `reference_2026_10_14/a4-offdiagonal-x4x0.json` — the frozen off-diagonal entry of the record of 2026-10-14.
- `WARPED_METRIC_PROVENANCE.md` — the order, the author's rules, the inputs, the programs, the checks and the sha256
  of every file.
- The explanation of the issue and of the remedy: `Revision/docs/METRIC_SELF_CONSISTENCY.md` (PDF next to it).

Run from the repository root:

```text
python Revision/metric_warped/python/derive_warped_metric.py
wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls
```
