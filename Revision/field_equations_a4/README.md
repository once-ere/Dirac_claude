# field_equations_a4 — the Einstein-Lovelock equations for a4[x4] (SPEC section 5)

Revision code only (nothing imported from the old stages). Two independent derivations:

| file | engine | role |
| --- | --- | --- |
| `wolfram/FieldEquationsA4.wl` | Wolfram | metric, Christoffel, Riemann (MTW), Einstein, GKD (`Det` of the delta matrix), P_(1..3) computed directly, P_(k) rebuilt from `Revision/gkd_lovelock/results/lovelock-tensors.json`, the author's T16 read strictly from `Revision/algebra/gammas.json` (the primary representation, SPEC section 2), a Cl(1,1)^(x)4 representation kept only for comparison, canonical spin connection |
| `wolfram/verify_field_equations_a4.wls` | Wolfram | the field equations, reductions, Einstein case, linear member, field-specific sources (spinor statements in the author's T16; exact equivalence with the comparison representation and representation independence of the off-diagonal coefficients); writes `a4-equations.json` and `reports/wolfram-a4-report.json` |
| `python/check_field_equations_a4.py` | sympy | independent re-derivation (symbol calculus instead of trigonometry, GKD as a permutation sign; the spinor statements in the author's T16 from `Revision/algebra/gammas.json` (primary) and, for comparison only, in a third tensor-product representation, with an exact equivalence check); checks `a4-equations.json` and the GKD branch; writes `reports/python-a4-report.json` and `reports/a4-equations-summary.md` |
| `python/check_ks_source_conditions.py` | Python | evaluates the source conditions of the a4 equations (x8-independence, p3 + p_t = 2 p8, the linear member's equal pressures) on the recorded Kohn-Sham states of `Revision/kohn_sham/results/ground`; writes `reports/ks-source-conditions.json` (result: no recorded Kohn-Sham state is an admissible source; the Kohn-Sham history is a prescribed background without back-reaction) |

Run from the repository root (Wolfram first, the Python checker reads its output):

```text
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
python Revision/field_equations_a4/python/check_ks_source_conditions.py
```

Both exit with code 0 only if every check passes; two runs give byte-identical outputs (LF).
The Wolfram verifier and the Python checker read `Revision/algebra/gammas.json` strictly when they start (before any
check): a missing or malformed file stops the run with a line `ERROR  ...` and exit code 1 (no fallback to another
representation, no output written). The Wolfram verifier also stops with a line `ERROR  ...` and exit code 1 when
`FieldEquationsA4.wl` is missing or an output file cannot be opened for writing.
Run times on the development machine (wall clock, 2026-10-07, depending on the load): 43-70 s (Wolfram) and 7-28 s
(Python).
The exact condensate witnesses are built from null vectors of the author's T16. The value of S reported by
`condensate_diagonal_witness_exact` (51200, 28800, 51200) scales with the arbitrary normalisation of those null vectors
and therefore depends on the representation (the Cl(1,1)^(x)4 comparison basis gives 204800, 115200, 204800); the
frequencies, S != 0, its reality and the vanishing of the 15 three-gamma bilinears do not.

Conventions, the equations and the field-specific statements are in `a4-equations.json`; the sign of the
matter energy-momentum tensor relative to the gravitational side is the declared convention sigmaT = +1 of
SPEC section 4 (rho = m S + U, p = S U' - U for homogeneous on-shell states) and is carried as a parameter.
