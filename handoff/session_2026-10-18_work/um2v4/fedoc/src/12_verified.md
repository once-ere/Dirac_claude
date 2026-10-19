
# What was verified

## The checks

The computations of UM-2 are done by sixteen Python scripts (folder `universe_model_2/code`), each of which tests its own results
against independent computations, closed forms or limits, with a stated tolerance. There are 287 checks in all, and all pass: 235 of
the computations of version 3 and 52 of the residual analysis of the solution (`um2_residuals.py`). The scripts are deterministic
(the Kohn-Sham computations run with one numerical thread), so every number of this document can be reproduced by running them.

| script | checks | what is verified |
| ---------------------- | ------ | ------------------------------------------------------------------------ |
| `um2_algebra.py` | 31 | the author's $16 \times 16$ Dirac matrices rebuilt from his formulas: the Clifford relations of signature $(4, 4)$, $C$, the chirality, $\mathcal{B}$, the irreducibility of the representations of Pin(4,4) and Spin(4,4), the block basis and the block forms of FE-56 |
| `um2_geometry.py` | 25 | the curvature of the order-0 metric in both charts (FE-33), the Lovelock tensors by four routes (FE-34 to FE-37), the Bianchi identities ($p = 1, 2, 3$), the minisuperspace variation, the equations of the record, the static block, the vielbein and the spin connection (FE-13) |
| `um2_background.py` | 22 | the equal block components ($x_0$ and $x_5$), the static block (FE-42), the sourceless vacuum (repulsive), the stabiliser and its roots (FE-43), $\mathcal{G}(K_*) > 0$, the stability of the block for the stabiliser family (FE-44), the first-order response (FE-45 to FE-47), the dimensional reduction (FE-48) |
| `um2_primordial.py` | 5 | the nonlinear primordial evolution: the constraint preserved to $6\times10^{-10}$, the radion oscillation, the dust-like expansion, the basin of the stable block, the largest deflation |
| `um2_fields.py` | 16 | the exact Dirac reduction in all eight blocks (FE-56), the selection operator and the boundary conditions (FE-28, FE-29, self-adjoint), the zero modes of dirac16complex, of the doublets and of the singlets (FE-57), their helicity and dispersion, the tip mixing for one and for three generations (FE-30), the gauge $x_0$ operator and its boundary conditions (FE-50, FE-51), the gauge invariance of the tip terms |
| `um2_spectra.py` | 14 | the $x_0$ spectra of the bosons and the fermions (FE-52, FE-59): exact roots, finite elements and shooting, the massless zero modes, the gap, the Dirichlet bound, the custodial relation, the fit of $\beta_{\mathrm{W}}$, $m_{\mathrm{Z}}$, the twelve fermion masses, the first-order formula |
| `um2_electroweak.py` | 19 | the charges of three generations, the charges of $W^+$ and $W^-$, the photon and $Z$ couplings, the cancellation of the gauge anomalies, the chiral projector, the halves $\Psi_A$ and $\Psi_B$, the $Z$ charges, the invisible width, the $Z$ widths of three generations |
| `um2_flavour.py` | 7 | the PMNS and CKM matrices (unitarity, Jarlskog invariant, FE-61), the exact three-generation tip condition and a general tip matrix (FE-60), no tree-level flavour-changing couplings of the Kaluza-Klein modes, $\mu \to e\gamma$, lepton universality |
| `um2_ks_jobs.py` | 22 | seven Kohn-Sham jobs: the exact spectrum and the massless fold band (FE-62), basis convergence, the $y$-conservation law and the energy identity of the interacting states (FE-68), radiation of the fold-band gas, the record's reference states reproduced, the dark matter (energy bookkeeping, cold, hidden pressure), the block response (FE-47), the Hellmann-Feynman responses to the portal mean fields (FE-72) |
| `um2_coupled.py` | 16 | the overlaps and their screening (FE-70), the fold band massless, the freeze-in benchmark, direct detection, the I13 algebra, overlaps and relic, the $B - L$ alternative, the self-interaction channel, the proton sensitivity (FE-83), the mean fields in ten environments, the gravity loop (FE-80), $W$, $Z$ and photon with the dark matter (FE-79), the domain of validity |
| `um2_neutrino.py` | 16 | the masses and the cosmological bound, vacuum oscillations, the MSW resonances, long baselines with CP violation, the solar survival probability, the onset of oscillations in the early Universe, the QED integrals, the decoupling method against published values and $N_{\mathrm{eff}}$, the CNB, supernova resonances, the fast flavour instability (three checks), Dirac or Majorana neutrinos |
| `um2_cosmology.py` | 8 | the CMB with the angular scale matched, three massive neutrino states, the TT and EE spectra against Planck $\Lambda$CDM, BAO against DESI DR2, dark-radiation variants, $N_{\mathrm{eff}}$ and helium, the freeze-in radiation, $\sigma_8$ and the first-order potential |
| `um2_thermal.py` | 7 | the degrees of freedom, the thermal average, the Boltzmann solver, the relic, the unitarity of the effective operator and the unitarity-limited relic, the I12 benchmark |
| `um2_series.py` | 4 | the terms of the metric series: order 1 with $n = 0$, the Kaluza-Klein gravitons, the radion, the decreasing magnitudes |
| `um2_analysis.py` | 23 | the $x_0$ mass mechanism and the uncertainty relation, dirac16complex as dark matter (mass, stability, neutrality, cross-sections, direct detection) and as dark energy (it cannot be) |
| `um2_residuals.py` | 52 | the residuals of the solution in 26 field equations and 26 links between the equations (below) |

## The residuals of the solution

For 26 of the field equations the stored solution is substituted afresh into the equation as printed in this document (or into
its closed form). The residual is the relative amount by which the equation fails; the neglected terms are those that the approximation
of the solution leaves out. Every residual is below its tolerance.

| field equations | residual | the largest neglected term |
| ---------------------------------- | ---------------------- | -------------------------------------------- |
| background, FE-38 to FE-43 | $3.9\times10^{-13}$ | matter against the stabiliser: $3.0\times10^{-32}$ at the freeze-out, $2.4\times10^{-93}$ today |
| block response, FE-44 to FE-47 | $1.4\times10^{-7}$ (second order, for sources of $10^{-5}H^2$) | second order at the freeze-out $2.3\times10^{-32}$; inertia $3.4\times10^{-33}$ |
| primordial era, FE-38 to FE-40 | $1.3\times10^{-11}$ | radiation $1.0\times10^{-6}$ of the final block; the block-shape mode (OPEN) |
| four-dimensional gravity, FE-48, FE-49 | $6.9\times10^{-13}$ | $\Lambda_4/H^2 \sim 10^{-92}$ (tuned, OPEN) |
| boson $x_0$ eigenvalues, FE-50 to FE-52 | $5.9\times10^{-12}$ | the dark-matter kinetic function $1.9\times10^{-17}$; the Lovelock corrections to the graviton operator (OPEN) |
| fermion tip conditions, FE-58 to FE-60 | $5.4\times10^{-11}$ | mixing with the Kaluza-Klein modes, $(m/m_{\mathrm{KK}})^2 \le 2.0\times10^{-6}$ |
| spectrum of dirac16complex, FE-62 | $8.5\times10^{-13}$ | the Standard-Model mean fields, $1.5\times10^{-6}$ of the dark-matter mass |
| Kohn-Sham equations, FE-63 to FE-69 | $7.4\times10^{-14}\,H$ | the self-interaction mean field at the bound on $\lambda$, $2.7\times10^{-9}\,m_\Psi$; correlation beyond the local exchange (OPEN) |
| Kohn-Sham source of gravity, FE-67 with FE-47 | $1.4\times10^{-12}$ | the block-shape source, $\lvert p_0 - p_5\rvert/\bar p$ up to 4 (OPEN) |
| portal overlaps, FE-70, FE-71 | $3.8\times10^{-12}$ | screening by the dirac16complex gas, $7.2\times10^{-10}$ at the bound on $\lambda$ |
| coupled environments, FE-72 to FE-86 | $2.0\times10^{-11}$ | the loop gain, $1.05\times10^{-33}$ |
| $W$, $Z$ with the dark matter, FE-79 | $3.3\times10^{-12}$ | the physical shift, $1.9\times10^{-17}$ |
| $W^\pm$, $Z$ masses and $Z$ widths, FE-25, FE-55 | $2.7\times10^{-12}$ | electroweak loop corrections, $4.1\times10^{-3}$ of the total width |
| CMB and BAO perturbations, FE-90 to FE-98 | $1.5\times10^{-6}$ | order $\epsilon^2$, $2.4\times10^{-5}$ |
| graviton tower, FE-53, FE-54 | $1.2\times10^{-12}$ | the Kaluza-Klein correction to Newton's law at 50 $\mu$m: zero in double precision |
| metric series, FE-87 | $2.4\times10^{-5}$ | order 2 at a neutron star, 0.03 |
| neutrino flavour evolution, FE-103 to FE-108 | $7.1\times10^{-12}$ | non-adiabatic solar effects, $1.3\times10^{-3}$ |
| thermal potential, FE-109 | $8.7\times10^{-12}$ | the CP-asymmetric potential, $1.1\times10^{-2}$ (ESTIMATE) |
| neutrino decoupling, FE-111 to FE-115 | $2.7\times10^{-12}$ | the electron mass and the momentum dependence, $4.4\times10^{-3}$ in $N_{\mathrm{eff}}$ |
| fast flavour instability, FE-116 to FE-119 | $3.3\times10^{-13}$ | the vacuum term, $9.0\times10^{-6}$ of the self-interaction |
| cosmic neutrino background, FE-120 | $2.9\times10^{-12}$ | non-instantaneous heating, $1.1\times10^{-2}$ in $\Omega_\nu h_{100}^2$ (included in the CMB computation) |
| degrees of freedom, FE-121 to FE-123 | $5.0\times10^{-9}$ | the order-$\alpha$ pressure, $-5.4$ % at the freeze-out |
| dark-matter relic, FE-124 to FE-128 | $6.1\times10^{-9}$ | the order-$\alpha$ pressure, about $+2.7$ % in $\Omega h^2$ (ESTIMATE) |
| freeze-in, FE-129, FE-130 | $3.9\times10^{-5}$ | inverse processes, $1.2\times10^{-2}$ at 10 TeV |
| right-handed neutrinos, FE-131 to FE-134 | $2.5\times10^{-12}$ | the elastic rate (ESTIMATE), $9.5\times10^{-6}$ in $\Delta N_{\mathrm{eff}}$ |
| self-interaction channel, FE-135, FE-136 | $1.1\times10^{-5}$ | inverse annihilation at the bound, $2.7\times10^{-2}$; the Fierz coefficients (not computed) |

## The links between the equations

| quantity | field equations | difference |
| ------------------------------------------------------- | ---------------------------- | ----------------- |
| the Kohn-Sham energy density and pressures in the block response | FE-63 to FE-69, FE-45 to FE-47 | $3.4\times10^{-12}$ |
| the hidden pressure of the dark matter, $p_0/\rho = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ | FE-62, FE-67, FE-81 | $6.1\times10^{-12}$ |
| $m_{\mathrm{Z}}$ from the $x_0$ eigenvalues and in the $Z$ widths | FE-55, FE-25 | $2.0\times10^{-12}$ |
| the weak angle of the $x_0$ problem and of the $Z$ widths (change of the total width) | FE-51, FE-55, FE-102 | $8.3\times10^{-3}$ (by design) |
| the fermion masses in the thermal history | FE-59, FE-121 | $3.1\times10^{-12}$ |
| the neutrino masses in the flavour evolution, the CNB and the CMB | FE-100, FE-104, FE-120, FE-96 | $5.7\times10^{-12}$ |
| the PMNS matrix in the flavour evolution and the CNB | FE-61, FE-104, FE-120 | $8.2\times10^{-13}$ |
| the neutrino density today in the CNB and the CMB computation | FE-120, FE-96 | $1.9\times10^{-5}$ |
| $N_{\mathrm{eff}}$ of the decoupling and the freeze-in in the CMB computation | FE-115, FE-130, FE-97 | $5.4\times10^{-16}$ |
| the relic density as the cold dark matter of the CMB computation | FE-126, FE-91 | $3.1\times10^{-9}$ |
| the Hubble rate at the freeze-out: thermal history and four-dimensional gravity | FE-122, FE-49 | $1.7\times10^{-4}$ (by design) |
| the radiation after neutrino decoupling: thermal history and CMB computation | FE-123, FE-97 | $5.9\times10^{-3}$ (by design) |
| the plasma energy density at the freeze-out: thermal history and block sources | FE-121, FE-80, FE-81 | $1.3\times10^{-3}$ (by design) |
| the portal responses of the Kohn-Sham jobs and the overlaps of the coupled solution | FE-70, FE-72 | $3.0\times10^{-12}$ |
| the I12 response $\mathcal{O}_{\mathrm{DM}}$ across the computations | FE-71, FE-72, FE-79 | $5.7\times10^{-6}$ |
| the I12 benchmark in the relic and in the mean fields | FE-127, FE-72 | $1.6\times10^{-12}$ |
| the dark-matter mass of the spectrum in the Boltzmann equation | FE-62, FE-124 | $8.1\times10^{-13}$ |
| the relic and freeze-in couplings in the mean fields | FE-126, FE-129, FE-72 | $6.7\times10^{-13}$ |
| the $W$ eigenvalue in the problem with the dark-matter kinetic function | FE-52, FE-79 | $2.3\times10^{-6}$ |
| the block-response coefficients across the computations | FE-46, FE-47, FE-80 | $2.0\times10^{-13}$ |
| the radion frequency of the linear and of the nonlinear evolution | FE-44, FE-38 to FE-40 | $7.9\times10^{-5}$ (by design) |
| the block scale $f_*$ across the computations | FE-43, FE-52, FE-59, FE-62, FE-63 | $2.2\times10^{-12}$ |
| the heating factor $F_{\mathrm{h}}$ of the neutrino decoupling | FE-115, FE-133 | $5.8\times10^{-7}$ |
| the terms of the metric series in the cosmology, the coupled solution and the masses | FE-87, FE-53, FE-98, FE-80 | $4.7\times10^{-12}$ |
| the freeze-out temperature of the relic and of the freeze-out environment | FE-124, FE-86 | $2.1\times10^{-12}$ |
| the block sensitivities of the masses in the hidden pressure | FE-85, FE-81 | $4.5\times10^{-11}$ |

## What is not verified

The following are not settled and are labelled OPEN where they occur: the block-shape mode driven by $p_0 - p_5$ (the order-0 metric
has one block scale; its response to a block-anisotropic source is not computed, and the source is not small compared with the hidden
pressure that is kept); the Gauss-Bonnet and cubic corrections to the graviton operator of the Kaluza-Klein tower; the tuned value of
$\Lambda_4$ that the observed dark energy needs; the normalisation that relates the tip mixing matrices $\mathcal{K}$ to the Yukawa
matrices $\mathcal{Y}$ of the action; correlation beyond the local exchange in the Kohn-Sham treatment of dirac16complex; and the
nonlinear evolution of the fast flavour instability. The cross-section of the self-interaction channel (FE-135), the electroweak
condensates below $m_{\mathrm{W}}$ (FE-78), the QCD interaction measure below 1 GeV (FE-75) and the block dependence of the QCD scale and the
nucleon mass (FE-83, FE-84) are estimates.
