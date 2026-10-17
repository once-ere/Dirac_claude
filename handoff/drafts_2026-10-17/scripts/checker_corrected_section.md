## The record of the corrected metric (2026-10-16/17)

Both solvers were moved to the corrected primordial metric (solver README, "The corrected metric"; reference README,
"The corrected metric"): the hidden scale f = e^{-a4/3}, kappa = e^{-a4} constant in y, P = e^{-3Hy}/Vol_7, the fold
joining two halves of a cell, N_mid = 592, N_large = 2352, lambda_1 = 157.7, 2.131, 0.5363, lambda_2 = 473.1, 6.393, 1.609.
The checker's tolerance rule is unchanged. What changed in `crosscheck_ks.py` and `measure_rust_refinement.py`:
* the integrals carry the weight e^{3Hy} (the key `emtIntegrals_2Vol7_int_e3Hy` of `single`), the fold value is the
  profile end point at y = 0 (the names `*_brane` are kept), and the texts state the corrected metric;
* `adiabatic_dE_da4`: the EMT form of the history is dE/da4 = -3 P3 - 3 (beta/2 - 1) P_t - (beta/2 - 1) P0
  (= -3 P3 + P_t + P0/3), so U_Rust = 3 U_Rust(int p3) + 3 |beta/2 - 1| U_Rust(int p_t) + |beta/2 - 1| U_Rust(int p0);
* `ground_profiles`: the roundoff floor of a profile is set by the maximum of its family (n, S, Q: max |n|; rho, p3,
  p_t, p0, e_int: the largest of their maxima; M_eff, v_v: their own), because S and p0 vanish identically for the
  lambda = 0 fold-band states and a profile's own maximum is then roundoff (`claude_failures.md` H6, H9);
* the exact-Fock variant: the matrix and `single --exx` both solve it at the occupations of the converged uniform-gas
  ground state, started from it (`claude_failures.md` H3);
* the reference repeat is computed beforehand in two stages of parts (`--stage 1|2 --part i/6`);
* the matrix-wide profile uncertainty of the determinism report is read in units of the profile family's maximum
  (`claude_failures.md` H14), and the reference's SCF tolerance (the noise floor of its temperature quotients) from its
  `parameters.json` instead of a constant;
* the first run of the cross-check on this record failed 3 of 31 checks (`claude_failures.md` H15): int_p0 and the
  exact-Fock first-order difference differed by about 2.4e-10 and 3.4e-10, from the SCF stopping errors of both
  solvers, which entered neither uncertainty (the Rust refined run stopped at the same iteration as the canonical
  one, and the Richardson term of the reference does not see an error that is nearly the same on its three grids);
  and the reference's sea-hole list was shorter than three Rust thermal label sets. The Rust refined run now stops at
  the SCF tolerance 1e-14 (its canonical record is unchanged), the reference solves every state to 1e-14 m and evaluates
  the sea holes over max(5, 10%) more shells than its label set; the tolerance rule is unchanged.

@@RUN@@
