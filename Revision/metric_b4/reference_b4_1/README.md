# The record before the metric change of 2026-10-14 (b4 = 1), frozen

`curvature.json` and `lovelock-tensors.json` are the files of `Revision/gkd_lovelock/results/` at commit `e3e35fe`
(2026-10-14), the last commit before the GKD record was recomputed for the metric with b4 (commit `52053a9`). They are
byte-identical to that commit (`git show e3e35fe:Revision/gkd_lovelock/results/curvature.json`); their sha256 are the
values that `Revision/tests/test_gkd_lovelock.py` pinned before the change:

| file | sha256 |
|---|---|
| `curvature.json` | `d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e` |
| `lovelock-tensors.json` | `9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567` |

`Revision/metric_b4/wolfram/verify_metric_b4.wls` and `Revision/metric_b4/python/check_metric_b4.py` check these
hashes and then prove that the metric with b4 reproduces this record exactly at b4 = 1.

These two files are kept byte for byte as they were, so they still use the labels of that time: x1 ... x8 with the
hidden direction x8 listed last. Those labels are withdrawn (2026-10-14: the author's coordinates are x0, x1, ..., x7,
x0 the hidden direction, listed first). Both checkers read the files through the map x8 -> x0, xk -> xk (component
keys and every expression), and compare them with the curvature of the metric with b4, at b4 = 1, in the author's
coordinates.
