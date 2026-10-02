# field_equations_a4 — the Einstein-Lovelock equations for a4[x4] (SPEC section 5)

Revision code only (nothing imported from the old stages). Two independent derivations:

| file | engine | role |
| --- | --- | --- |
| `wolfram/FieldEquationsA4.wl` | Wolfram | metric, Christoffel, Riemann (MTW), Einstein, GKD (`Det` of the delta matrix), P_(1..3) computed directly, P_(k) rebuilt from `Revision/gkd_lovelock/results/lovelock-tensors.json`, a real Cl(4,4) representation, canonical spin connection |
| `wolfram/verify_field_equations_a4.wls` | Wolfram | the field equations, reductions, Einstein case, linear member, field-specific sources; writes `a4-equations.json` and `reports/wolfram-a4-report.json` |
| `python/check_field_equations_a4.py` | sympy | independent re-derivation (symbol calculus instead of trigonometry, GKD as a permutation sign, a different Clifford representation plus the author's T16 from `Revision/algebra/gammas.json`); checks `a4-equations.json` and the GKD branch; writes `reports/python-a4-report.json` and `reports/a4-equations-summary.md` |
| `python/check_ks_source_conditions.py` | Python | evaluates the source conditions of the a4 equations (x8-independence, p3 + p_t = 2 p8, the linear member's equal pressures) on the recorded Kohn-Sham states of `Revision/kohn_sham/results/ground`; writes `reports/ks-source-conditions.json` (result: no recorded Kohn-Sham state is an admissible source; the Kohn-Sham history is a prescribed background without back-reaction) |

Run from the repository root (Wolfram first, the Python checker reads its output):

```text
wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
python Revision/field_equations_a4/python/check_field_equations_a4.py
python Revision/field_equations_a4/python/check_ks_source_conditions.py
```

Both exit with code 0 only if every check passes; two runs give byte-identical outputs (LF).
Run times on the development machine: about 15 s (Wolfram) and 5 s (Python).

Conventions, the equations and the field-specific statements are in `a4-equations.json`; the sign of the
matter energy-momentum tensor relative to the gravitational side is the declared convention sigmaT = +1 of
SPEC section 4 (rho = m S + U, p = S U' - U for homogeneous on-shell states) and is carried as a parameter.
