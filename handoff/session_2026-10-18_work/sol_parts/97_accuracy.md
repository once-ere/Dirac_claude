# Accuracy of the solution

The table collects, for every field equation or system of field equations of the solution, the method of solution, the residual of
the solution in its own equation (a precisely defined, measured quantity: the residual of the stored solution substituted into the
equation, the implied relative error of a root, or the agreement of independent evaluations), the size of the terms that the
approximation neglects, and the checks in concert with the other field equations that contain the same fields (the same quantity
compared where two or more equations use it). All residuals and links were computed anew in version 4 (`um2_residuals.py`, 52 named
checks, all passed; with the 235 checks of the computations of version 3, UM-2 has 287 named checks); "NOT small" marks a neglected term or a difference that is not small and is reported as it is.

| equations | solution method | residual in its own equation | neglected terms | in concert |
|:-----------------|:-----------------|:------------------|:------------------|:------------------|
| background: [[bg_x4]], [[bg_x1]], [[bg_x0]], [[static]], [[stabiliser]] (step 1) | exact closed form (symbolic) | $3.9\times10^{-13}$ of the largest term with the stored 12-digit $K_*$ ($1.2\times10^{-16}$ closed form); printed = coded equations exactly | matter against the stabiliser: $3.0\times10^{-32}$ (freeze-out), $2.4\times10^{-93}$ (today) | $f_*$ in steps 2, 3, 10: $2.2\times10^{-12}$ |
| block response: [[radion]], [[response]], [[response_coeffs]], [[adiabatic]] (steps 1, 3, 8) | exact algebraic numbers | second order as it must be: $1.4\times10^{-7}$ at sources $10^{-5}H^2$ (ratio $0.10$ per decade); radiation cancels to $2\times10^{-13}$ | second order $2.3\times10^{-32}$ and inertia $3.4\times10^{-33}$ at the freeze-out | Kohn-Sham sources $3.4\times10^{-12}$; coefficients $2\times10^{-13}$; radion linear vs nonlinear $7.9\times10^{-5}$ |
| primordial era: [[bg_x4]], [[bg_x1]], [[bg_x0]] integrated (step 1) | DOP853, relative tolerance $10^{-11}$ | one-step defect $1.3\times10^{-11}$; constraint $3.6\times10^{-12}$ of its terms | radiation of zero modes: $1.0\times10^{-6}$ of the final block; block-shape mode (OPEN) | radion frequency $7.9\times10^{-5}$ |
| four-dimensional gravity: [[reduction]], [[einstein4]] (steps 1, 6) | exact (symbolic) | $\Lambda_4(K_*)$ and the stationarity of the $x_4$ balance: $3.9\times10^{-13}$ (stored), $10^{-16}$ (closed form); coefficient of $R^{(4)}$ = $\mathcal{G}(K)$ exactly | dark energy needs $\Lambda_4/H^2 \sim 10^{-92}$ (tuned, OPEN) | Hubble rate of the thermal history at the freeze-out: $1.7\times10^{-4}$ (fold bands left out there) |
| boson $x_0$ problem: [[x0_boson]], [[x0_boson_bc]], [[x0_boson_eig]], [[wz_fit]] (step 2) | exact roots (mpmath); finite elements as check | implied relative eigenvalue error $\le 5.9\times10^{-12}$; finite elements $5\times10^{-10}$ | dark-matter kinetic function $1.9\times10^{-17}$; radiative corrections; Lovelock corrections to the graviton (OPEN) | $m_{\mathrm{Z}}$ in the widths $2.0\times10^{-12}$; two values of the weak angle: $0.82$ % of the total width (NOT zero; per-cent scheme ambiguity) |
| fermion $x_0$ problem: [[dirac_Q]] to [[dirac_nuR]], [[bc_tip]], [[ferm_red]] to [[pmns]] (step 2) | exact roots (mpmath, 50 to 60 digits) | implied relative root error $\le 5.4\times10^{-11}$; three-generation determinant $1.2\times10^{-11}$; its roots = one-generation roots to $3.0\times10^{-42}$ | mixing with Kaluza-Klein modes $(m_{\mathrm{t}}/m_{\mathrm{KK}})^2 = 2.0\times10^{-6}$ | masses in the thermal history $3.1\times10^{-12}$; neutrino masses in flavour, CNB, CMB $5.7\times10^{-12}$; PMNS $8.2\times10^{-13}$ |
| spectrum of dirac16complex: [[dirac16]], [[bc_psi]], [[psi_spectrum]] (step 2) | exact formulas | $8.5\times10^{-13}$ | mean-field shifts of the level $1.5\times10^{-6}$ (step 8) | hidden pressure in three equations $6.1\times10^{-12}$; $M_{\mathrm{DM}}$ $8.1\times10^{-13}$ |
| Kohn-Sham: [[ks]] to [[ks_bc]] (step 3) | Galerkin in the free eigenbasis, self-consistent to $10^{-13}$, Richardson | re-solved state $7.4\times10^{-14}$ (absolute); one more map $1.8\times10^{-14}$; $y$-conservation $8.8\times10^{-8}$; basis $1.5\times10^{-9}$ | self-interaction mean field at the bound on $\lambda$: $2.7\times10^{-9}$; correlation beyond local exchange (OPEN) | Kohn-Sham sources in gravity $3.4\times10^{-12}$; portal responses $3.0\times10^{-12}$ |
| Kohn-Sham source in gravity: [[ks_tmn]] in [[adiabatic]] (step 3) | cell averages of the energy-momentum tensor | $1.4\times10^{-12}$; free gas cancels to $9\times10^{-13}$ | block-shape source $p_0 - p_5$: 0.9 to 4 of $\bar p$ (NOT small; suppressed with $\bar p$; OPEN) | response coefficients $2\times10^{-13}$ |
| portal overlaps: [[contact4d]], [[i12dm]], [[levelshift]] (steps 3, 8) | quadrature of exact orbitals; Hellmann-Feynman | $3.8\times10^{-12}$; Kohn-Sham finite differences $3.0\times10^{-10}$ | screening by the interacting gas $7.2\times10^{-10}$ at the bound on $\lambda$ | $\mathcal{O}_{\mathrm{DM}}$ across computations $5.7\times10^{-6}$ (rounded $0.7072$) |
| coupled environments: [[levelshift_env]] to [[env]] (step 8) | closed formulas, iterated | $2.0\times10^{-11}$; iteration converged (loop gain) | loop gain $1.1\times10^{-33}$; second order $2.3\times10^{-12}$ | plasma energy density vs thermal history $1.3\times10^{-3}$ (by design); $G_{\mathrm{A}}$, $G_{\mathrm{V}}$ $6.7\times10^{-13}$; freeze-out temperature $2.1\times10^{-12}$ |
| $W$ with the dark-matter kinetic function: [[dm_on_sm]] (step 8) | first-order perturbation theory with the exact eigenfunction and orbital (finite elements in version 3) | independent quadrature $3.3\times10^{-12}$; shooting $3.0\times10^{-11}$; photon exactly unshifted | the physical shift $1.9\times10^{-17}$ | $W$ eigenvalue of the finite elements at zero amplitude $2.3\times10^{-6}$; $\mathcal{O}_{\mathrm{DM}}$ $5.7\times10^{-6}$ |
| Yang-Mills masses and $Z$ widths: [[ym_lin]], [[gf]] (steps 2, 4) | closed formulas, tree level | $2.7\times10^{-12}$ | electroweak loops $4.1\times10^{-3}$; b-quark mass $-1.3\times10^{-3}$; $\alpha_3^2$ term $+1.3\times10^{-3}$ | $m_{\mathrm{Z}}$ $2.0\times10^{-12}$; $F_{\mathrm{h}}$ $5.8\times10^{-7}$ |
| linear perturbations: [[pert_einstein]] to [[sigma8]] (step 6) | CAMB 2.0.5, default accuracy | Poisson form of the first-order potential $1.5\times10^{-6}$; matter-era form $4.4\times10^{-5}$; masses iterated to $7.8\times10^{-12}$ | order $\epsilon^2$: $2.4\times10^{-5}$ of order $\epsilon$; Kaluza-Klein modes and radion absent | neutrino masses $5.7\times10^{-12}$; $\Omega_\nu h_{100}^2$ $1.9\times10^{-5}$; $N_{\mathrm{eff}}$ $5\times10^{-16}$; relic as cold dark matter $3.1\times10^{-9}$; radiation today $0.59$ % (instantaneous decoupling in step 9) |
| graviton tower: [[kk_tower]], [[kk_potential]] (steps 2, 10) | exact eigenfunctions | $1.2\times10^{-12}$; boundary $9\times10^{-16}$; stored strengths $5.2\times10^{-9}$ | Kaluza-Klein correction at 50 micrometres: $\mathrm{e}^{-3.1\times10^{16}}$; Lovelock corrections (OPEN) | radion $7.9\times10^{-5}$; series $4.7\times10^{-12}$ |
| metric series: [[series]], [[newton8]] (step 10) | magnitudes of the computed solution | first omitted order $2.4\times10^{-5}$ of the kept one | order 2 at a neutron star $0.03$ (nonlinear gravity there) | $4.7\times10^{-12}$ |
| flavour evolution: [[potentials]] to [[adiabaticity]] (step 5) | exact matrix exponentials | $7.1\times10^{-12}$; unitarity $1.3\times10^{-15}$; CPT $2.2\times10^{-16}$ | adiabatic solar formula $1.3\times10^{-3}$; Landau-Zener $2.6\times10^{-77}$; collective effects (OPEN) | masses $5.7\times10^{-12}$; PMNS $8.2\times10^{-13}$ |
| thermal potential: [[thermal_pot]] (step 5) | root of the onset condition | $8.7\times10^{-12}$ | CP-asymmetric potential $1.1\times10^{-2}$ (ESTIMATE); $(T/m_{\mathrm{W}})^2 \sim 4\times10^{-9}$ | masses $5.7\times10^{-12}$ |
| neutrino decoupling: [[qke]] to [[neff]] (step 5) | LSODA, relative tolerance $10^{-11}$ | instantaneous limit recomputed $2.7\times10^{-12}$; published values $4.6\times10^{-4}$ | electron mass in the rates and momentum dependence: $0.0044$ in $N_{\mathrm{eff}}$ | $N_{\mathrm{eff}}$ in the CMB $5\times10^{-16}$; $F_{\mathrm{h}}$ $5.8\times10^{-7}$ |
| fast flavour instability: [[ffi_eln]] to [[ffi_homog]] (step 5) | Newton iterations; discretised eigenvalues | $3.3\times10^{-13}$ (in units of $\sqrt2G_{\mathrm{F}}n_{\nu_e}$) | vacuum term $9.0\times10^{-6}$; nonlinear evolution (OPEN) | |
| CNB: [[cnb]] (step 5) | adaptive quadrature | $2.9\times10^{-12}$ | non-instantaneous heating $1.08$ % (included in the CMB) | $\Omega_\nu h_{100}^2$ in the CMB $1.9\times10^{-5}$ |
| degrees of freedom: [[idealgas]], [[dof]], [[crossover]] (step 9) | Gauss-Legendre quadrature | $5.0\times10^{-9}$ (exact limits); table $4.6\times10^{-11}$ | order-$\alpha$ plasma pressure: $-5.4$ % at the freeze-out (NOT small) | masses $3.1\times10^{-12}$; Hubble rate $1.7\times10^{-4}$; radiation today $0.59$ % |
| relic: [[boltz]] to [[unitarity]] (steps 7, 9) | Radau (relative tolerance $10^{-10}$); root finding | relic condition $3.1\times10^{-9}$; late-time identity $6.1\times10^{-9}$ | order-$\alpha$ pressure: $+2.7$ % in $\Omega_{\mathrm{DM}}h_{100}^2$, $+1.4$ % in $G_{\mathrm{A}}$ (ESTIMATE; NOT small); $21.7$ % of the rate at the $^3S_1$ bound | relic as the cold dark matter of the CMB $3.1\times10^{-9}$; $\mathcal{O}_{\mathrm{DM}}$ $5.7\times10^{-6}$; $M_{\mathrm{DM}}$ $8.1\times10^{-13}$ |
| freeze-in: [[freezein]], [[neff_fold]] (step 9) | trapezoid on 600 logarithmic temperatures | $3.9\times10^{-5}$ | inverse processes $0.012$ of the Hubble rate; $T_{\mathrm{max}}$ (ASSUMED) | $N_{\mathrm{eff}}$ of the CMB $5\times10^{-16}$; $G_{\mathrm{V}}$ $6.7\times10^{-13}$ |
| right-handed neutrinos: [[nuR_BL]] to [[nuR_I11]] (step 9) | Radau in $M_{\mathrm{DM}}/T - 2$ | $2.5\times10^{-12}$ | elastic rate (ESTIMATE): $9.5\times10^{-6}$ of $\Delta N_{\mathrm{eff}}$ | $F_{\mathrm{h}}$ $5.8\times10^{-7}$ |
| self-interaction channel: [[selfint]], [[selfint_energy]] (step 9) | trapezoid on 800 logarithmic temperatures | $1.1\times10^{-5}$ | inverse annihilation $0.027$; Fierz coefficients (ESTIMATE) | freeze-out temperature $2.1\times10^{-12}$ |

Besides these, the approximations of the whole solution are: the static block with an assumed stabiliser; the good sector (no
momenta along the extra times); the Kohn-Sham mean-field treatment; the portal couplings as external mean fields; tree level for the
electroweak widths; the coherent flavour evolution in the Sun, the Earth and the supernova envelope with schematic density profiles;
neutrino decoupling with one temperature per flavour; the linear analysis of the fast flavour instability and a schematic estimate of
its effect on the heating; the freeze-out formula of step 7 (replaced by the Boltzmann equation in step 9); order $\epsilon$ for the
cosmology; ideal gases with a modelled QCD crossover and instantaneous neutrino decoupling for the degrees of freedom; Maxwell-Boltzmann
statistics for the freeze-in; the effective cross-sections capped at the partial-wave bounds; the QCD interaction measure below 1 GeV
from a lattice-like shape and leading-order perturbation theory above; the order-$\alpha$ electroweak pressure without scalars; one-loop
running for the couplings and the proton sensitivity; the elastic $\nu_R$ rate and the self-interaction cross-section as estimates.

**What the residual computation of version 4 found.** The claims of version 3 are confirmed; these points are not small or were
corrected, and are stated here as they are:

* the weak angle has two values in the solution: $\sin^2\theta_{\mathrm{W}} = 0.223632$ on shell in the $x_0$ problem of $W$ and
  $Z$, and the $\overline{\mathrm{MS}}$ value $0.23122$ in the $Z$ widths and the couplings; the total width moves by $0.83$ %, within
  the electroweak loop corrections that UM-2 does not compute (step 4);
* the ideal-gas thermal history leaves out the order-$\alpha$ interaction pressure of the plasma ($-5.4$ % of the pressure at the
  freeze-out: QCD $-4.7$ %, $SU(2)$ $-0.7$ %), which step 8 uses for the condensates; with it $\Omega_{\mathrm{DM}}h_{100}^2$ would rise
  by about $2.7$ % and $G_{\mathrm{A}}$ by about $1.4$ % (ESTIMATE): the physical accuracy of the relic strength $G_{\mathrm{A}}$ is
  about 1 %, not the $10^{-6}$ of its root finding (step 9);
* the Hubble rate of the thermal history leaves out the fold bands of the freeze-in ($3.5\times10^{-4}$ of the energy density at the
  freeze-out), so it is $1.7\times10^{-4}$ too small, and the relic moves by about as much (steps 1 and 9);
* the thermal history uses three neutrino species decoupled instantaneously at 2 MeV, while the CMB computation uses
  $N_{\mathrm{eff}} = 3.0442$: $0.59$ % in the radiation today (steps 5, 6, 9); the plasma energy density at the freeze-out differs by
  $0.13$ % between the thermal history and the block sources of the coupled solution, by design (the trace anomaly, step 8);
* the block-shape source $p_0 - p_5$ is about 4 times the kept hidden pressure for dark matter at rest (0.9 for the test states of
  step 3); its absolute size is suppressed with the hidden pressure, and the mode is OPEN, as in version 3, now quantified (steps 1, 3);
* corrected in the outputs: the coefficient $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}}$ of step 8 is $-0.111253$
  (version 3: $-0.1126$, finite elements limited by rounding; without physical consequence, since the physical amplitudes are below
  $1.7\times10^{-16}$); the photon's shift is exactly zero; the derivative of the $x_4$ balance at $K_*$, quoted as $-6\times10^{-12}$ in
  version 3, is exactly zero (the quoted number is rounding); the CNB integrals are now accurate to $3\times10^{-16}$ (the quoted digits
  are unchanged); the $\nu_R$ integration of step 9 no longer depends on the twelfth digit of its input; the fold-band gap changes of
  step 3 are at the rounding level ($10^{-13}$ to $3\times10^{-9}$), zero in exact arithmetic.
