# The GKD/Lovelock record of the metric of 2026-10-14 (frozen)

These three files are the outputs of `lovelock_gkd lovelock --output Revision/gkd_lovelock/results --brute-force-k2`
for the metric of 2026-10-14, copied unchanged from commit c93fe22 (they were not changed after it until 2026-10-16):

| file | sha256 | lines | bytes |
| --- | --- | --- | --- |
| `curvature.json` | `b6951e389572cb4c7b91aaa33c2e543d7387765f101d5faee6c306118aff46c1` | 325 | 40,878 |
| `lovelock-tensors.json` | `f7b59ebbb3ac54ecbacf74bf528883c6880cc398270cec7855a68c68b04db10c` | 405 | 163,905 |
| `lovelock-report.json` | `c0202db95902003ad9dfe3b58137c5db798057d75265d7bcd16fe0483fa3b4d0` | 34 | 3,231 |

The metric of 2026-10-14, diag(Cot[6 H x0]^2, E^(2 a4) Sin[6 H x0]^(1/3) (x3), -1, -E^(-2 a4) b4 Sin[6 H x0]^(1/3) (x3)) on
0 < 6 H x0 < Pi/2, is WITHDRAWN since 2026-10-16: its Lovelock tensors have the off-diagonal component E_(k)^x4_x0 ~
Cot z b4'/b4 that no diagonal source can match (`Revision/docs/METRIC_SELF_CONSISTENCY.md`).  The record of the
corrected metric is in `Revision/gkd_lovelock/results/`.

These files are kept for one purpose: the author's notebook
`Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` was written for this metric (at
b4 = 1), and `Revision/gkd_lovelock/comparison/compare_with_author.py` compares its stored outputs with these files
(`comparison/README.md` section 1.2; the check `reference-files-are-the-record-of-2026-10-14` requires the sha256
above, and `Revision/tests/test_gkd_lovelock.py` pins them as well).  They are verified records of their time: 19 of
19 Rust checks, 29 of 29 Wolfram checks and 49 of 49 sympy checks on 2026-10-14
(`verification/WOLFRAMSCRIPT_PROVENANCE.md` part 6.4).  Do not regenerate or edit them.
