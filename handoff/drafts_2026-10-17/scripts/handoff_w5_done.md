- W5 DONE 2026-10-17: `Revision/kohn_sham/` and the Kohn-Sham source parts of `Revision/field_equations_a4/` for the
  corrected metric.  Theory (`kohn_sham/theory`): the hidden direction carries f = e^{-a4} b4^{1/2}, kappa = e^{-a4}
  constant in y, P = e^{-3Hy}/Vol_7, Vol_7 = ell^3 v_t e^{(5/3) a4}, the fold joins two halves (both fold conditions
  filled, ASSUMED), y-conservation p0' + 3H (p0 - p_t) = 0, dE/da4 = -3 P3 + P_t + P0/3, the rescaling identity changes
  H and L; Wolfram 51/51, sympy 61/61 (provenance 6.8).  Rust solver: N_mid = 592, N_large = 2352, lambda_1 = 157.7,
  2.131, 0.5363, lambda_2 = 473.1, 6.393, 1.609; the lambda = 0 states are exact fold-band gases (eps = e^{-a4}|k|);
  `ks-rust-solver.json` 45/45, mermin roots 5/5, determinism 14/14; the matrix, its repeat and the refined run in parts
  with a job cache (`--cache`, `--part`, `--inner-threads`; byte-identical to one run).  Reference: @@REF@@.
  Cross-check: @@CC@@.  Tip study: @@TIP@@.  Dense history (`dark_sector/dirac16complex/compute/run_ks_history.py`, in
  parts): @@HIST@@.  `field_equations_a4`: `check_ks_source_conditions.py` 5/5 (no recorded state is an admissible
  source: C1 fails for every nonzero state, C2 p0 = p_t only for lambda = 0, C3 holds); `ks_source/ks_source_a4.py`
  @@KSS@@.  Failures on the way: `claude_failures.md` H2-H12 (H11: a part's wall time included a 9-hour system sleep;
  H12: the reference's a4 neighbours needed the SCF tolerance 1e-14).  Gate: the Kohn-Sham steps in parts (@@GATE@@).
  KNOWN OPEN until W6: the dark sector (`compute_eos.py`, `derive_effective.py`, `independent_free_gas.py`,
  `dirac16complex00`, the Wolfram twin), pairing T3 (`check_t3.py` tests the old Hamiltonian string; the demos read the
  old key `emtIntegrals_2Vol7_int_e6Hy`), the notebooks (pinned report counts); until W7: the documents and their
  publication tests; until W8: the textbook.
