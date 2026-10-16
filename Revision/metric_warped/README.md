# Revision/metric_warped — the warped primordial metric of 2026-10-16

The user's order of 2026-10-16 asked for the simplest modification of the primordial metric that is probably
self-consistent with the Einstein field equations, after the author's observation that a diagonal metric is
self-consistent only if every off-diagonal component of the sources vanishes.

* `python/derive_warped_metric.py` — sympy: the off-diagonal component of the metric of 2026-10-14 at every Lovelock
  order, the scan of the family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g44 = -Sin[z]^(2 gamma), and the properties of the
  warped metric (g44 = -Sin[6 H x0]^(1/3)): no off-diagonal component at any order, the layers of the field equations,
  the Kasner vacuum of Einstein gravity, the history's source and its conservation, the gravity term of the Dirac
  operator.  Writes `results/warped-metric.json` and `reports/python-warped-metric-report.json`.
* `wolfram/verify_warped_metric.wls` (package `wolfram/MetricWarped.wl`) — the independent Wolfram check; writes
  `reports/wolfram-warped-metric-report.json`.
* `WARPED_METRIC_PROVENANCE.md` — the order, the inputs, the programs, the checks and the sha256 of every file.
* The explanation of the issue and of the remedy: `Revision/docs/METRIC_SELF_CONSISTENCY.md` (PDF next to it).

Run from the repository root:

```text
python Revision/metric_warped/python/derive_warped_metric.py
wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls
```
