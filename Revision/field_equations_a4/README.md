# field_equations_a4 — the Einstein-Lovelock equations for a4[x4] (SPEC section 5)

Revision code only (nothing imported from the old stages). Two independent derivations:

| file | engine | role |
| --- | --- | --- |
| `wolfram/FieldEquationsA4.wl` | Wolfram | metric, Christoffel, Riemann (MTW), Einstein, GKD (`Det` of the delta matrix), P_(1..3) computed directly, P_(k) rebuilt from `Revision/gkd_lovelock/results/lovelock-tensors.json`, the author's T16 read strictly from `Revision/algebra/gammas.json` (the primary representation, SPEC section 2), a Cl(1,1)^(x)4 representation kept only for comparison, canonical spin connection |
| `wolfram/verify_field_equations_a4.wls` | Wolfram | the field equations, reductions, Einstein case, linear member, field-specific sources (spinor statements in the author's T16; exact equivalence with the comparison representation and representation independence of the off-diagonal coefficients); writes `a4-equations.json` and `reports/wolfram-a4-report.json` |
| `python/check_field_equations_a4.py` | sympy | independent re-derivation (symbol calculus instead of trigonometry, GKD as a permutation sign; the spinor statements in the author's T16 from `Revision/algebra/gammas.json` (primary) and, for comparison only, in a third tensor-product representation, with an exact equivalence check); checks `a4-equations.json` and the GKD branch; writes `reports/python-a4-report.json` and `reports/a4-equations-summary.md` |
| `python/check_ks_source_conditions.py` | Python | evaluates the source conditions of the a4 and b4 equations (C1 x0-independence for every a4, b4; C2 the x1 + x5 - 2 x0 combination, p3 + p_t = 2 p0 on the history; C3 the constant source kappa (-2/27, -2/9, -22/27, -14/27) that the history a4 = H x4, b4 = b4(0) e^{(4/3) H x4} needs with the author's weights; C4 the off-diagonal equation, which holds there) on the recorded Kohn-Sham states of `Revision/kohn_sham/results/ground`; writes `reports/ks-source-conditions.json` (6 checks; result: no recorded Kohn-Sham state is an admissible source; the Kohn-Sham history is a prescribed background without back-reaction) |

Run from the repository root (Wolfram first, the Python checker reads its output):

```text
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
python Revision/field_equations_a4/python/check_b4_block.py
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python Revision/field_equations_a4/ks_source/ks_source_a4.py
```

Both exit with code 0 only if every check passes; two runs give byte-identical outputs (LF).
The Wolfram verifier and the Python checker read `Revision/algebra/gammas.json` strictly when they start (before any
check): a missing or malformed file stops the run with a line `ERROR  ...` and exit code 1 (no fallback to another
representation, no output written). The Wolfram verifier also stops with a line `ERROR  ...` and exit code 1 when
`FieldEquationsA4.wl` is missing or an output file cannot be opened for writing.
Run times on the development machine (wall clock, 2026-10-07, depending on the load): 43-70 s (Wolfram) and 7-28 s
(Python).
Since 2026-10-14 the set covers the user's metric with b4[x4] in the extra-time components (64 Wolfram checks: the
52 of the restriction b4 = 1 and 12 for the general b4, key `b4` of `a4-equations.json`; `check_b4_block.py`, 11
checks, is the sympy twin of the key `b4`) and uses the author's coordinates {x0, x1, ..., x7} (x0 = the hidden
direction, listed first; the hidden-direction pressure is p0, the off-diagonal components q40, q04). Runs of
2026-10-14: 45 s and 51 s (Wolfram, 64 of 64), `check_field_equations_a4.py` 63 of 63, `check_b4_block.py` 11 of
11, `check_ks_source_conditions.py` 6 of 6, `ks_source_a4.py` 23 of 23 (record: `wolfram/WOLFRAMSCRIPT_PROVENANCE.md`
section 6.8).
The exact condensate witnesses are built from null vectors of the author's T16. The value of S reported by
`condensate_diagonal_witness_exact` (51200, 28800, 51200) scales with the arbitrary normalisation of those null vectors
and therefore depends on the representation (the Cl(1,1)^(x)4 comparison basis gives 204800, 115200, 204800); the
frequencies, S != 0, its reality and the vanishing of the 15 three-gamma bilinears do not.

**Since 2026-10-15 every section is for GENERAL a4(x4) and b4(x4) > 0** (the user's orders "b4 is a function of x4;
b4 is NEVER 1" and "move everything to b4(x4)"): 59 Wolfram checks (`wolfram/WOLFRAMSCRIPT_PROVENANCE.md` section
6.9) and 65 sympy checks; the keys of `a4-equations.json` are general (exponentialHistory replaces the linear member;
the key b4 keeps the formulas of 2026-10-14 for its readers). Results: the off-diagonal pair E^x4_x0 = cot z u Q
(u = b4'/b4) forces a source with T^x4_x0 = cot z u Q/kappa unless u Q = 0 (Einstein: Q = 3 H/2); with the author's
weights the exponential history a4 = H x4 has Q = 0 exactly for beta = d ln b4/d a4 in {0, 4/3}, and beta = 4/3 needs
the constant source kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) (SPEC section 1); no exponential history
with b4 not constant is a vacuum solution for those weights, nor sourced by the homogeneous condensate.
Phase 5 of `HANDOFF.md` 0.9 (2026-10-16): `python/check_ks_source_conditions.py` (6 of 6) and `ks_source/ks_source_a4.py` (22 of 22; `ks_source/README.md`) are for general b4 as well: in Einstein gravity no source without T^x4_x0 (every Kohn-Sham state) is compatible with a history in which b4 changes; with the author's weights the record's history is not continued by the free gas (a fold of the truncated system at a4 = 0.024).

Conventions, the equations and the field-specific statements are in `a4-equations.json`; the sign of the
matter energy-momentum tensor relative to the gravitational side is the declared convention sigmaT = +1 of
SPEC section 4 (rho = m S + U, p = S U' - U for homogeneous on-shell states) and is carried as a parameter.
