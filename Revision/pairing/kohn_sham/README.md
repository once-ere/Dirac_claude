# pairing/kohn_sham — theorem T3 (the Kohn-Sham level of the pairing, SPEC section 9)

Revision code only (nothing from the old stages). T3 is proved here by exact symbolic computation, twice and
independently:

| file | engine | role |
| --- | --- | --- |
| `wolfram/verify_t3.wls` | Wolfram | the proof steps of T3; writes `t3-theory.json` (hypotheses, statement, proof, what is not established) and `reports/wolfram-t3.json` |
| `python/check_t3.py` | sympy | independent re-derivation of every step; compares with `t3-theory.json`; records the numerical self-test of the Rust Kohn-Sham solver as a confirmation (not a proof); writes `reports/python-t3.json` |

Inputs: `Revision/kohn_sham/ks-theory.json` (the Kohn-Sham problem: block equation, functional, densities,
energy-momentum tensor, boundary conditions, block basis V) and `Revision/algebra/gammas.json`.

Run from the repository root (Wolfram first, the sympy checker reads its theorem record):

```text
wolframscript -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
python Revision/pairing/kohn_sham/python/check_t3.py
```

Both exit with code 0 only if every check passes; two runs give byte-identical outputs (LF). Run times on the
development machine: about 3 s (Wolfram, including the kernel start) and 1 s (sympy).

The theorem in one line: the block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of
the 16-component orbital), with the brane parities exchanged and the tip angle theta -> pi - theta, maps every
self-consistent instantaneous Kohn-Sham state with (m, lambda, theta) onto one with (-m, +lambda, pi - theta), with
equal levels, occupations, Kohn-Sham energy, grand potential and energy-momentum profiles, and S -> -S. The Z2
brane is ASSUMED (as in `Revision/kohn_sham/ks-theory.json`); the states are instantaneous (adiabatic) mean-field
states; nothing here is a creation process.
