# Changed numbers after the precision fixes of 2026-10-18 (commit cc2d514); use these, not the version-3 text

- d ln Lambda_W / de (coupled.json WZ_kinetic_shift/dlnLambdaW_damp): -0.111252909326 (first-order perturbation theory,
  agrees with shooting to 3e-11). Version 3 said -0.1126 (finite elements, limited by rounding). The photon's value is
  exactly 0 (version 3: -2.5e-11, rounding).
- Y_nuR / Y_eq at x = 40 for the B - L variant of I13 (coupled.json I13_B_minus_L_alternative/Y_nuR_over_Yeq_at_x40):
  0.999697681992 (robust integration in s = x - 2).
- CNB (neutrino.json CNB/, copied in cosmology.json): Omega_nu h^2 = 0.000638217282098; mean velocities 0.435132624815,
  0.0604083086104, 0.0105351736626 (c); energy densities 9.95804523965e-16, 7.51619688306e-15, 4.31573842483e-14 eV^4
  (quadrature now accurate to 3e-16).
- Kohn-Sham: the "observed order" of the stress state is now 4.956 (rounds to 4.96); rounding-level fold-gap values
  7.9e-11 (electron density), 3.0e-9 (up-quark density), 9.3e-11 (neutrino density), -1.4e-10 (gluon condensate),
  1.2e-13 (I13 fold-band shift); every one is zero in exact arithmetic.
- The checks: 287 in all (235 of version 3 + 52 of the new um2_residuals.py).

# The residual analysis (outputs/residuals.json, reports/residuals-checks.json; 52 checks, all pass)

26 equations with the residual of the stored solution (afresh by direct substitution where cheap) and the neglected terms,
and 26 in-concert links (the same quantity in two equations). Not-small findings reported there and to be stated in the
documents: the weak angle has two values (0.223632 on shell in the x0 W/Z problem, 0.23122 MS-bar in the widths and
couplings: Gamma_Z moves by 0.83 %, within the electroweak loop corrections UM-2 does not compute); the thermal history's
Hubble rate leaves out the freeze-in fold bands (3.5e-4 of rho at freeze-out, H larger by 1.7e-4, the relic by about as
much); the thermal history uses N_eff = 3 after 2 MeV while the CMB uses 3.0442 (0.59 % in g_rho today); the plasma
energy density at freeze-out differs by 0.13 % between the thermal history and the coupled block sources (the trace
anomaly, by design); the ideal-gas thermal history leaves out the O(alpha) plasma pressure (-5.4 % at freeze-out: QCD
-4.7 %, SU(2) -0.7 %), so Omega h^2 would rise by about 2.7 % and G_A by about 1.4 % (ESTIMATE): the physics accuracy
of G_A is about 1 %, not the 1e-6 of the root finding; the block-shape source p0 - p_t is about 4 times the kept pbar for
non-relativistic dark matter (OPEN, now quantified).
