# Provenance of the metric change of 2026-10-14 (the metric function b4)

This file proves that the change of the primordial metric ordered by the user on 2026-10-14 was made correctly,
lists every recomputation it caused with its verification, and states plainly what was not recomputed and why.

## 1. The order

The user, 2026-10-14 (verbatim key sentences):

> CRITICAL: Read, understand and remember "Dirac_Einstein-Lovelock_4+4_Nash.nb".
> CRITICAL: We are changing the metric of the primordial gravitation field to
> {{Cot[6 H x0[]]^2, 0, 0, 0, 0, 0, 0, 0}, {0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0, 0, 0}, {0, 0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0, 0}, {0, 0, 0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0}, {0, 0, 0, 0, -1, 0, 0, 0}, {0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3), 0, 0}, {0, 0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3), 0}, {0, 0, 0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3)}}.
> Make this change throughout the entire project; create a provenance that proves that these critical changes were
> correctly made by you. Continue by re-computing each and every affected quantity.

together with the rule that no individual calculation may take longer than 7 minutes 3 seconds (423 s); every
calculation that did not finish within that time is recorded in `claude_failures.md` (repository root).

## 2. The source: the author's notebook

`Dirac_Einstein-Lovelock_4+4_Nash.nb` (repository root, read only, sha256
`4f2d83b53e4a35696e1ed4d0569f4cabbfc7463d0036c36ae5534bd6e549aafb`; 407 cells, 112 input cells).  It loads xAct, defines
the chart (x0, x1, ..., x7) with x0 the hidden direction (a small circle), x1..x3 3-space, x4 time, x5..x7 the deflating
extra times; builds the metric in input cell In[97] (beta1 = Sin[6 H x0]^(1/3), beta2 = Cot[6 H x0]^2,
beta3 = Exp[2 a4[x4]], DiagonalMatrix[{beta2, beta1 {beta3, beta3, beta3}, -1, -beta1 b4[x4] {1/beta3, 1/beta3, 1/beta3}}],
stored output Out[101]); computes the Christoffel symbols, Riemann, Ricci (Out[123], Out[124]), the Ricci scalar
(Out[119]), the Einstein tensor (Out[120]), the Lovelock tensors allLovelock1, allLovelock2, allLovelock3 (Out[126] to
Out[128]), the vacuum Einstein-Lovelock equations -Lambda delta + w1 L1/H^2 + w2 L2/H^4 + w3 L3/H^6 (Out[129]), their
distinct entries (Out[132]), and the solution b4 = 1, a4 = H x4, w1 = 1, w2 = 1/32: w3 = 1/1152, Lambda = 10
(Out[134], Out[135]).  `Revision/metric_b4/wolfram/extract_author_b4_outputs.wls` reads these stored cells without
evaluating anything (`results/author-b4-outputs.json`).

## 3. The change

The Revision record uses the author's coordinates {x0, x1, ..., x7} in the author's order (x0 the hidden direction,
listed first; ordered by the user on 2026-10-14; until then the record had named them x1..x8 with the hidden direction
x8 listed last, map x8 -> x0, xk -> xk).  The metric is the user's matrix:

```text
g = diag( Cot[6 H x0]^2 (x0), E^(2 a4[x4]) Sin[6 H x0]^(1/3) (x1, x2, x3), -1 (x4), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3) (x5, x6, x7) )
```

The metric the record used before 2026-10-14 (`Revision/SPEC.md` section 1 of 2026-10-01) is the same with b4 = 1:
g00 = Cot^2 was already there.  So the change is exactly one new metric function b4(x4) > 0 multiplying the three
extra-time components.  `Revision/SPEC.md` section 1 (both coordinate orders, the user's text verbatim) and section 5,
and `Revision/README.md`, state the new metric.

## 4. Proof that the change is correct (every check exact; outputs byte-identical over two runs)

| Set | What is checked | Result | Time |
|---|---|---|---|
| `metric_b4/wolfram/verify_metric_b4.wls` | metric, Ricci (both index positions), R, Einstein, Lovelock E_(1..3), vacuum equations, distinct entries and the solution EQUAL the author's stored Out[101], Out[119], Out[120], Out[123], Out[124], Out[126]-Out[129], Out[132], Out[134], Out[135] (the author's coordinates on both sides: identity); at b4 = 1 they equal the earlier record (the frozen copy `metric_b4/reference_b4_1/` of `gkd_lovelock/results/curvature.json`, `lovelock-tensors.json` before b4, read through x8 -> x0); every E_(k) divergence-free; sqrt|det g| = b4^(3/2) cos z; a constant b4 drops out; the only off-diagonal entries are (x0, x4), (x4, x0), proportional to b4' | 27/27 | 77-83 s |
| `metric_b4/python/check_metric_b4.py` | independent sympy (permutation-sign contraction, exact normal form): the same against Wolfram, the author and the b4 = 1 record | 21/21 | 30-40 s |
| `metric_b4/wolfram/vacuum_b4.wls` | with the author's weights every C^2 vacuum solution has b4 = const and a4 = +-H x4 + const | 6/6 | 3 s |
| `metric_b4/wolfram/consequences_b4.wls` | T1 and T2 of the pairing record hold with b4; T3 via the Kohn-Sham result; dark-sector volume factor e^(-3a4) b4^(3/2) | 4/4 | 3 s |
| `gkd_lovelock` (Rust, 13 Laurent symbols incl. Q = b4^(1/2)) | `lovelock --brute-force-k2`: Riemann symmetries, P_(k) trace, divergence, symmetry, brute force over 1073741824 index lists at b4 = 1.37 | 19/19 | 15 s |
| `gkd_lovelock/verification/verify_lovelock_gkd.wls` | the Rust output against Wolfram's own curvature with b4 and the verbatim kdelta | 29/29 | 73 s |
| `gkd_lovelock/verification/check_lovelock_gkd.py` | the Rust output against sympy (ring generators b4'/b4, b4''/b4) | 49/49 | 17 s |
| `gkd_lovelock/comparison/compare_with_author.py` | the OLD author notebook (Pair_Creation..., no b4) at b4 = 1 | 73 PASS, 0 FAIL, 5 N/A | 1 s |
| `field_equations_a4/wolfram/verify_field_equations_a4.wls` | the earlier analysis restricted to b4 = 1 (unchanged keys) and the new key b4 (12 checks) | 64/64 | 40 s |
| `field_equations_a4/python/check_field_equations_a4.py`, `check_b4_block.py` | sympy twins (b4 = 1 keys; the key b4 with the author's T16) | 63/63, 11/11 | 5 s, 31 s |
| `field_equations_a4/python/check_ks_source_conditions.py`, `ks_source/ks_source_a4.py` | the Kohn-Sham source verdict holds for every b4 | 6/6, 23/23 | 1 s, 2 s |
| `theory/wolfram/verify_field_theory_b4.wls` | geometry, spin connection, gamma^mu Omega_mu, Dirac operator, evolution form, conservation, both statistics | 19/19 | 7 s |
| `theory/wolfram/verify_field_theory_b4_emt.wls C`, `G` | EMT by vielbein variation, Belinfante part, diagonal components, T^x4_x0 | 4/4, 4/4 | 185 s, 107 s |
| `theory/python/check_field_theory_b4.py` | sympy twin (Christoffel, spin connection, gamma^mu Omega_mu); the spin connection is real and the U(1) Noether matrix identity holds with sqrt(det g) = b4^(3/2) cos z for general b4 (added 2026-10-14; `lead_checks/charge_conjugation_and_u1.py` checks the case b4 = 1); negative control: with sqrt(det g) = cos z the identity fails | 7/7 | 2 s |
| `kohn_sham/theory/verify_ks_b4.wls` | b4 enters the Dirac operator only through b4^(-3/4) and the extra-time derivatives; the good-sector Kohn-Sham problem is independent of b4 | 4/4 | 4 s |

## 5. What the change does (the recomputed physics)

* **Curvature.**  Ricci, Einstein and the Lovelock tensors acquire the terms in b4'/b4 and b4''/b4 (a constant b4
  drops out: it is the rescaling x5,6,7 -> b4^(1/2) x5,6,7).  New nonzero components E_(k)^x4_x0 = cot z (b4'/b4) (...)
  and E_(k)^x0_x4 = -tan z (b4'/b4) (...).  sqrt|det g| = b4^(3/2) cos z: the 7-volume is constant only when b4 is.
* **Vacuum.**  With the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10) every vacuum history has
  b4 = constant and a4 = +-H x4 + const: the author's solution b4 = 1, a4 = H x4 and its time reverse
  (`vacuum-b4.json`; the time-time equation is a constraint C(a4'/H, b4'/(H b4)) and the off-diagonal one is
  (b4'/b4) Q(a4'/H, b4'/(H b4)); {C = 0, Q = 0} has only a4' = +-H, b4' = 0).
* **Field equations with a source** (`a4-equations.json`, key b4): the constraint stays first order; kappa q40 = cot z
  (b4'/b4) Q and kappa q04 = -tan z (b4'/b4) Q (Einstein: Q = 3H/2, so a source without T^x4_x0 forces b4 constant);
  the earlier algebraic condition p3 + p_t = 2 p0 becomes kappa (p3 + p_t - 2 p0) = (b4'/b4)^2/4 + b4''/(2 b4)
  (Einstein); conservation gains -(3/2)(b4'/b4)(rho + p_t) and +(3/2)(b4'/b4) q40.
* **Spinors.**  gamma^mu Omega_mu = 3H gamma^x0 + (3/4)(b4'/b4) gamma^x4; the field equation gains (3/4)(b4'/b4) gamma^x4 Psi
  and the extra-time derivatives are scaled by b4^(-1/2); exactly, D_b4[b4^(-3/4) X] = b4^(-3/4)(D_1[X] + (b4^(-1/2) - 1)
  e^a4 sin^(-1/6) sum_t gamma^t d_t X).  The homogeneous condensate is Phi = b4^(-3/4) Phi_1 and b4^(3/2) S is constant.
* **Kohn-Sham, pairing, dark sector.**  The good-sector Kohn-Sham problem (no extra-time momenta) does not contain b4:
  levels, orbitals and slices are unchanged; the rescaling identity reads KS(a4,0, b4,0; Delta k, v_t) = KS(0, 1;
  Delta k e^(-a4,0), v_t e^(-3 a4,0) b4,0^(3/2)).  T1, T2, T3 hold unchanged.  The dark-sector volume factor is
  e^(-3 a4) b4^(3/2).  On the background of the record (b4 = 1, forced in vacuum) every recorded number is unchanged.

## 6. Where the change was made

Updated for b4 and re-verified: `Revision/SPEC.md` (sections 1, 5, 11), `Revision/README.md`, `Revision/metric_b4/`
(new), `Revision/gkd_lovelock/` (Rust code, both verifiers, the author comparison, its test), `Revision/field_equations_a4/`
(package, driver, both sympy checks, the Kohn-Sham source conditions), `Revision/theory/` (supplement scripts and outputs),
`Revision/kohn_sham/theory/verify_ks_b4.wls`.  Kept as the record of the case b4 = 1 (valid there, and b4 = 1 is the
vacuum background): `Revision/theory/field-theory.json` with its 84-check verifier, the Kohn-Sham numerics, the
pairing numerics, the dark-sector numerics, and the three lead checks of `Revision/lead_checks` (their general-b4
counterparts: the Einstein and Lovelock tensors in `metric_b4` and the key `b4` of `field_equations_a4`; the
divergence of a diagonal source and gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) in
`theory/reports/wolfram-field-theory-b4.json`; the reality of the spin connection and the U(1) Noether matrix
identity with sqrt|g| = b4^(3/2) cos z in `theory/reports/python-field-theory-b4.json`, added 2026-10-14).  The documents, the Revision notebooks, the textbook and the gate are updated
in later commits (this file is extended as they are done; see HANDOFF.md section 0.5b).

Relabelled to the author's coordinates x0..x7 the same day and re-run (each run within 423 s; record in the
provenance files of the sets): `Revision/algebra` (the fixture `gammas.json` now in the author's order), `gkd_lovelock`,
`metric_b4`, `theory` (the 84-check verifier for b4 = 1 now evaluates its slow zero tests on 16 parallel subkernels:
309 s and 310 s instead of 1783-2508 s), `field_equations_a4`, `kohn_sham` (Wolfram and sympy theory, the Rust solver:
canonical, repeat, refined, refinement measurement; the Python reference in four parts of at most 268 s with a job
cache; the tip-convergence study with 22 workers, 196 s), `pairing` (T1, T2, T3 and both T3 demonstrations),
`dark_sector`, `lead_checks`.  In every set the outputs equal the previous ones after the renaming (x8 -> x0, p8 -> p0,
q48 -> q40, q84 -> q04, check names); the physics is unchanged.

## 7. Not recomputed within the time limit

See `claude_failures.md`, section C.  Not computed for GENERAL b4: the sections Noether identities, exact solutions
and conservation, and canonical quantisation of `Revision/theory/wolfram/verify_field_theory.wls` (at b4 = 1 they took
910.8 s, 1005.4 s and part of 1783-2508 s serially on 2026-10-08; with the parallel zero tests of 2026-10-14 the whole
b4 = 1 verifier takes 309 s, but the general-b4 versions of these three sections were not derived or run).  The
Kohn-Sham, pairing and dark-sector numerics are recomputed for b4 = 1 only (b4 = 1 is fixed by the vacuum theorem, and
the good-sector Kohn-Sham problem is independent of b4: `verify_ks_b4.wls`).

## 8. Reproduction (repository root)

```text
wolframscript -file Revision/metric_b4/wolfram/extract_author_b4_outputs.wls
wolframscript -file Revision/metric_b4/wolfram/verify_metric_b4.wls
python Revision/metric_b4/python/check_metric_b4.py
wolframscript -file Revision/metric_b4/wolfram/vacuum_b4.wls
wolframscript -file Revision/metric_b4/wolfram/consequences_b4.wls
```

Each prints its checks and ends with a line `...=OK` or `N/N checks passed`; exit code 0.
