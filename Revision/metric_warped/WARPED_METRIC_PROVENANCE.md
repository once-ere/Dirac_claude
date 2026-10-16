# Provenance of the corrected primordial metric of 2026-10-16 (version 2)

## 1. The order and the author's rules

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

During the work: "Remember, DO NOT employ either the definitions or conventions of
WaveFunctionUniverse-4+4-Einstein-Lovelock.nb. Only read it and understand the issues raised."

After version 1 (commit 7897829, g44 = -Sin[6 H x0]^(1/3)) the user wrote, the same day (verbatim):

> do you think x0 is time, or time-like? x0 is a hypothetical space-like coordinate. x4 is time. Do you agree? If so,
> why/how can you suggest that g44 = -sin2γ z; what are y and z; I missed their definitions. At any rate, g44 cannot
> oscillate. I hope that you know this.

> "For 0 < z < π/2", is wrong. Here, -\infty < z < \infty. You seem to have an interesting idea, but as it stands it
> will not work. For now try to fix your warped metric. Do not take time repairing the repo right now. that will come
> later.

> use Sin[6 H x0]^(1/3) = ( Sin[6 H x0] ^2 )^(1/6), and take the positive branch. this is what i always use in my
> Mathematica notebooks

Version 2 (this record) follows these rules: x0 is space-like and x4 is the time; g44 = -1 (no oscillating lapse);
z = 6 H x0 takes every real value and no sign of Sin[z] or Cos[z] is assumed; Sin[z]^(1/3) = (Sin[z]^2)^(1/6) > 0.

## 2. The input that raised the issue (read only, not used)

| file | sha256 | bytes | use |
| --- | --- | --- | --- |
| `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (repository root, the author's scratch notebook) | `3e0ef380cc36198cbc05da72de26a4218c0a64ab0711fa179a1701c77ca0fb8b` | 6663858 | read as text to understand the issue: its text cells state that the universe sources are to be added to the Einstein or Einstein-Lovelock field equations and that all off-diagonal terms of all source terms must vanish for the diagonal metric (and the earlier solutions for Psi16) to be valid; it uses the metric before 2026-10-14 (no b4) |

No definition, convention, formula, number or output of that notebook enters the Revision record: every computation
below uses the Revision record's own conventions (`Revision/SPEC.md`, `Revision/field_equations_a4/a4-equations.json`).
The four `.mx` files next to the notebook were not opened.  The notebook and the four `.mx` files were not meant to be
committed; the automatic snapshot of the Stop hook (commit d02ff19) committed and pushed them by mistake.  At the
author's request ("remove the notebook and .mx files in a new commit") a later commit removes them from the
repository (they stay in the history of d02ff19) and lists them in `.gitignore`; the files themselves stay on the
author's disk.

## 3. The result

The metric of 2026-10-14 (`Revision/SPEC.md` section 1 until 2026-10-16),

```text
g = diag(Cot[z]^2, E^(2 a4) (Sin[z]^2)^(1/6) (x1, x2, x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x5, x6, x7)),  z = 6 H x0,
```

has the off-diagonal component E_(k)^x4_x0 ~ Cot[z] b4'/b4 at every Lovelock order (Einstein: (3/2) H Cot[z] b4'/b4).

Version 1 (withdrawn): g44 = -(Sin[z]^2)^(1/6) removed it, but its lapse oscillates in x0 and vanishes at z = n Pi.

With g44 = -1, in the family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g_ii = E^(2 a4) (Sin[z]^2)^(3 alpha),
g_tt = -E^(-2 a4) b4 (Sin[z]^2)^(3 beta), the mixed curvature is
R^{x0 xi}_{x4 xi} = 18 H Tan[z] E^(-2 q a4) b4^(-2 p) alpha ((q - 1) a4' + p b4'/b4) and
R^{x0 xt}_{x4 xt} = 18 H Tan[z] E^(-2 q a4) b4^(-2 p) beta ((q + 1) a4' + (p - 1/2) b4'/b4).  Keeping the warp of the
extra times (beta = 1/6, alpha = 0, q = -1, p = 1/2) gives the corrected metric (version 2):

```text
g = diag(E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]) (x1, x2, x3), -1,
         -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6) (x5, x6, x7)),   -Infinity < 6 H x0 < Infinity.
```

It has no mixed Riemann component; every off-diagonal component of E_(1), E_(2), E_(3) vanishes identically for all
a4, b4 and every real z; every diagonal component is independent of x0; the block (x0, x5, x6, x7) is E^(-2 a4) b4
times a space of constant curvature -H^2 (signature (1,3)), so x0 shrinks with the deflating extra times.  The
alternative K (keep the warp of 3-space: g00 = E^(2 a4) Cot[z]^2, g_tt = -E^(-2 a4) b4) is also diagonal at every
order, with x0 growing with 3-space; the choice between the two is the author's.  The derivation, the checks and the
consequences are in `Revision/docs/METRIC_SELF_CONSISTENCY.md` (and its PDF, version 2).

## 4. The programs, their checks and their outputs

| program | checks | time (this machine) |
| --- | --- | --- |
| `Revision/metric_warped/python/derive_warped_metric.py` (sympy; GKD by the sign of the permutation; exact normal form for every real z) | 14 of 14 PASS | 16.4 s |
| `Revision/metric_warped/wolfram/verify_warped_metric.wls` with `MetricWarped.wl` (the Wolfram record's Christoffel, Riemann and k-delta contraction of `Revision/gkd_lovelock/verification/LovelockGKDCheck.wl`; its own exact normal form for every real z) | 13 of 13 PASS | 38.0 s |

The normal form of both programs: Sin[z] and Cos[z] keep their signs, w = (Sin[z]^2)^(1/12) > 0, numerators and
denominators are reduced modulo Cos^2 + Sin^2 - 1 and w^12 - Sin^2.  Negative controls (run by hand, scratch only):
the family check fails with the cores interchanged, the metric of 2026-10-14 has 48 mixed entries and
E_(1)^x4_x0 != 0, g00 without the factor b4 leaves E_(1)^x4_x0 = (3/2) H Cot[z] b4'/b4, and the normal form keeps the
sign of Cot[z] ((Sin[z]^2)^(1/2) - Sin[z] is not zero).

Two runs of each program on 2026-10-16 gave byte-identical outputs.  Tools: Python 3.14.5, sympy 1.14.0,
WolframScript (Wolfram Language 15.0.1).  Every run was made under `timeout -k 5 423`.

| file | role | sha256 |
| --- | --- | --- |
| `Revision/metric_warped/python/derive_warped_metric.py` | program | `19cc42852f86852d1b7877087115deee71dfa9134fae7ea51b988ebc4e107d05` |
| `Revision/metric_warped/wolfram/MetricWarped.wl` | package | `e44ceed1f87cb4703b6586aead28a5d146868cc29aba249ca51841e0bc4503cf` |
| `Revision/metric_warped/wolfram/verify_warped_metric.wls` | program | `02559027708defdbc75cce37751d2ee1901068a429752fee28296100dbb6e3d8` |
| `Revision/gkd_lovelock/verification/LovelockGKDCheck.wl` | input (k-delta, pruned Lovelock sum) | `1112c5a3a54191a7fe1eae1e3659c92c9bb2a24002fbb24a64e7bbc7279795bd` |
| `Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json` | input: the entries `generalSource.offDiagonal_x4x0` and `offDiagonalFactor_Q` of `Revision/field_equations_a4/a4-equations.json` at commit 04fa2e7 (sha256 of that file `fa2acb5d9b55d49bbee79be2e5551a1efc3c9a78daad101eb3e12f441d47ad00`), frozen so that the comparison does not depend on the later recomputation | `64eb77e812e41e7f184aa1db692513a3ce6326b9b4d50f8867b1bb3683961705` |
| `Revision/metric_warped/results/warped-metric.json` | output (sympy) | `c6167b356838f9ce4708f8826c561c001060b512acc73a101df4581f62c01aa6` |
| `Revision/metric_warped/reports/python-warped-metric-report.json` | output (sympy) | `573b698efdc7fd2d6da61d0adb477ae9af86218b1c1f9f693c8157a204cee75c` |
| `Revision/metric_warped/reports/wolfram-warped-metric-report.json` | output (Wolfram) | `5b3a4883dc134a99aa63f5f9f949bf79e51f19b44a168bc832300285fbcbbe8a` |
| `Revision/docs/METRIC_SELF_CONSISTENCY.pdf` | the explanation (version 2, 15 pages, warning-free, registered as edition `metric-self-consistency`) | `32d0532371001d38dbc06d388fcba8e0d3bce58adb3dc0db90f0c5cf9b5b2806` |

## 5. Reproduction

```text
python Revision/metric_warped/python/derive_warped_metric.py
wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls
python -m unittest Revision/tests/test_metric_self_consistency_publication.py -v
```

The Wolfram program reads `warped-metric.json` (the sympy Ricci tensor, history source and gravity term) and
therefore runs second.

## 6. Status of the recomputation (newest last)

* 2026-10-16, version 1 (commit 7897829): the time-warped metric g44 = -Sin[z]^(1/3).  Withdrawn the same day.
* 2026-10-16, version 2 (this record): the corrected metric, its derivation and its verification for every real z;
  `Revision/SPEC.md` section 1 states it; `Revision/docs/METRIC_SELF_CONSISTENCY.md` and its PDF (version 2).  The
  field-theory files committed in d02ff19 (`Revision/theory/wolfram/RevisionFieldTheory.wl`,
  `verify_field_theory.wls`) still use version 1; the rest of the record (field equations, lead's checks, GKD record,
  dark sector, Kohn-Sham, pairing, notebooks, documents, textbook) still describes the metric of 2026-10-14.  Both are
  recomputed for the corrected metric when the author says so (`HANDOFF.md` section 0.10).
