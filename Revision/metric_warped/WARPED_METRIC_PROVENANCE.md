# Provenance of the warped metric of 2026-10-16

## 1. The order

On 2026-10-16 the user wrote (verbatim, the parts that define the task):

> As I have noted in my Mathematica notebooks [read and understand, the file
> "D:\Developer\github\Dirac_claude\WaveFunctionUniverse-4+4-Einstein-Lovelock.nb", but DO NOT employ either its
> definitions or conventions. Only read it and understand the issues raised. ...]
> So the issue is, a diagonal form for the metric of the primordial gravitational field is only self-consistent if
> all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO. This is not the case here.
> I task you to :
> [1] find the simplest modification for the current metric of the primordial gravitational field that is probably
> self-consistent with the the Einstein field equations.
> [2] push your new, improved, metric of the primordial gravitational field to the repo, along with provenance and a
> pdf file explaination of the issues and remedies.
> [3] Recompute all primordial objects and push to repo; revise all concomitant documention and push.

and, during the work: "Remember, DO NOT employ either the definitions or conventions of
WaveFunctionUniverse-4+4-Einstein-Lovelock.nb. Only read it and understand the issues raised."

## 2. The input that raised the issue (read only, not used, not committed)

| file | sha256 | bytes | use |
| --- | --- | --- | --- |
| `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (repository root, the author's scratch notebook, not committed) | `3e0ef380cc36198cbc05da72de26a4218c0a64ab0711fa179a1701c77ca0fb8b` | 6663858 | read as text to understand the issue: its text cells state that the universe sources are to be added to the Einstein or Einstein-Lovelock field equations and that all off-diagonal terms of all source terms must vanish for the diagonal metric (and the earlier solutions for Psi16) to be valid; it uses the metric before 2026-10-14 (no b4) |

No definition, convention, formula, number or output of that notebook enters the Revision record: every computation
below uses the Revision record's own conventions (`Revision/SPEC.md`, `Revision/field_equations_a4/a4-equations.json`).
The four `.mx` files next to the notebook were not opened.

## 3. The result

The metric of 2026-10-14 (`Revision/SPEC.md` section 1 until 2026-10-16),

```text
g = diag(Cot[6 H x0]^2, E^(2 a4[x4]) Sin[6 H x0]^(1/3) (x1, x2, x3), -1, -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3) (x5, x6, x7)),
```

has the off-diagonal component E_(k)^x4_x0 ~ Cot[z] b4'/b4 at every Lovelock order.  The only one-entry change in the
family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g44 = -Sin[z]^(2 gamma) that removes the off-diagonal components at the
Einstein and the Gauss-Bonnet order for all a4, b4 is gamma = 1/6, p = q = 0, and it removes them at every order:

```text
g = diag(Cot[6 H x0]^2, E^(2 a4[x4]) Sin[6 H x0]^(1/3) (x1, x2, x3), -Sin[6 H x0]^(1/3),
         -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3) (x5, x6, x7)),
```

the warped metric: ds^2 = dy^2 + E^(2 H y) ghat7 with y = Log[Sin[6 H x0]]/(6 H).  The derivation, the checks and the
consequences are in `Revision/docs/METRIC_SELF_CONSISTENCY.md` (and its PDF).

## 4. The programs, their checks and their outputs

| program | checks | time (this machine) |
| --- | --- | --- |
| `Revision/metric_warped/python/derive_warped_metric.py` (sympy; GKD by the sign of the permutation) | 16 of 16 PASS | 44.5 s |
| `Revision/metric_warped/wolfram/verify_warped_metric.wls` with `MetricWarped.wl` (the Wolfram record's Christoffel, Riemann and k-delta contraction of `Revision/gkd_lovelock/verification/LovelockGKDCheck.wl`) | 11 of 11 PASS | 44.2 s |

Two runs of each program on 2026-10-16 gave byte-identical outputs.  Tools: Python 3.14.5, sympy 1.14.0,
WolframScript (Wolfram Language 15.0).  Every run was made under `timeout -k 5 423`.

| file | role | sha256 |
| --- | --- | --- |
| `Revision/metric_warped/python/derive_warped_metric.py` | program | `74cc210a2da044de5d179a589065de6788ef07d738208dfb8636eff94c4b72ab` |
| `Revision/metric_warped/wolfram/MetricWarped.wl` | package | `2541e0aea36bb952dea7bcb797ccb3a7a9b0053e8792acc2a869211e39982815` |
| `Revision/metric_warped/wolfram/verify_warped_metric.wls` | program | `3b8e3527c7edc21f2f68e1b5d774efb2d6fd689dd3fbc57c887f5f19e771b268` |
| `Revision/gkd_lovelock/verification/LovelockGKDCheck.wl` | input (k-delta, pruned Lovelock sum) | `1112c5a3a54191a7fe1eae1e3659c92c9bb2a24002fbb24a64e7bbc7279795bd` |
| `Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json` | input: the entries `generalSource.offDiagonal_x4x0` and `offDiagonalFactor_Q` of `Revision/field_equations_a4/a4-equations.json` at commit 04fa2e7 (sha256 of that file `fa2acb5d9b55d49bbee79be2e5551a1efc3c9a78daad101eb3e12f441d47ad00`), frozen so that the comparison does not depend on the later recomputation for the warped metric | `64eb77e812e41e7f184aa1db692513a3ce6326b9b4d50f8867b1bb3683961705` |
| `Revision/metric_warped/results/warped-metric.json` | output (sympy) | `bfb7d6823b4ceeeadfd8d34173736a16938f9eb886b2766c87d3224af77deebb` |
| `Revision/metric_warped/reports/python-warped-metric-report.json` | output (sympy) | `ef7116aa36fbbc936cd4d64162d89b85a81fa08d7eab81d6f9c720f38442488f` |
| `Revision/metric_warped/reports/wolfram-warped-metric-report.json` | output (Wolfram) | `717098942bc8efa02cbb11861fc3cfb99e09d5cc67977f81e72df09aa4035dac` |

## 5. Reproduction

```text
python Revision/metric_warped/python/derive_warped_metric.py
wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls
```

The Wolfram program reads `warped-metric.json` (the sympy values of the history's source) and therefore runs second.

## 6. Status of the recomputation (newest last)

* 2026-10-16: the warped metric, its derivation and its verification (this folder); `Revision/SPEC.md` section 1
  states the warped metric; `Revision/docs/METRIC_SELF_CONSISTENCY.md` and its PDF.  The rest of the record (field
  theory, field equations, lead's checks, GKD record, dark sector, Kohn-Sham, pairing, notebooks, documents, textbook)
  still describes the metric of 2026-10-14 and is recomputed in the order of `HANDOFF.md` section 0.10.
