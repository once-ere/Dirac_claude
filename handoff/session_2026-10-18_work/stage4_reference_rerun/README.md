# Old Stage 4: the reference rerun of `m1_L3_N1016_lamm2_T0` (STAGE4_SPEC erratum E4.14 b), cloud session 2026-10-18/19

A safe copy of the finished rerun, kept here until it is installed into
`artifacts/dirac16complex/kohn-sham/reference/` together with the checker report, the notebook refresh and the errata line
(steps R2 to R5 of `HANDOFF.md`, section 0.4u item 4, in one commit). Nothing in `artifacts/` was changed.

* Command (repository root, on a copy of the committed reference tree):
  `taskset -c 0 python3 -B scripts/ks_reference_solver.py --resume --skip-self-tests --output <copy>`
  (the reference solver with SHA-256 `8dbedada523de6df7346921edf6c926058e97fe296ba9c2f24331524b0a60494`, the version with
  the per-grid Delta-SCF occupations of erratum E4.14 (2)).
* Started `2026-10-19T02:26:42Z`, finished `2026-10-19T05:30:26Z` (exit code 0; 11018 s for the run, 11023.4 s in all,
  56 runs in the summary, failed: none). Linux cloud container, 2 cores, the run pinned to core 0 at nice 19.
* Result: converged, `E0 = 1126.858089184764`, `mu = 1.3895671875`, KS gap `0.04125509949243433`,
  Delta-SCF `0.04361950549196081` (the committed run, made before the per-grid rule: `0.04361995310432576`; expected by
  E4.14: about `0.04361951`, confirmed). Every other quantity agrees with the committed run to about 1e-9 relative or
  better. The label of the highest occupied state changed between the two exactly degenerate states `0:+1:-1:1` and
  `0:+1:+1:1` (their energies differ by 2.5e-15).
* Only this one run folder and `reference-summary.json` differ from the committed reference tree (`diff -rq`).

Files: `m1_L3_N1016_lamm2_T0/` (the run folder), `reference-summary.json` (the summary the solver wrote), `ref.log`
(the solver's log), `ref_start.txt`, `ref_done.txt`.
