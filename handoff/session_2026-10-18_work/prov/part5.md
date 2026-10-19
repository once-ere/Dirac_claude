# The field equations and their origin

The 136 field equations of UM-2 are the variations of the action of section 6 (FE-1 to FE-30), their exact reductions on the order-0 metric and the static block (FE-31 to FE-86), and the equations of the four-dimensional effective theory: the metric series and the linear perturbations (FE-87 to FE-99), the neutrinos (FE-100 to FE-120) and the thermal history (FE-121 to FE-136). The table gives, for each, its title and status (as in the inventory of the field equations), how it was obtained and solved, and the checks that verify it. The checks are named by the report and their number in the catalogue of section 9: alg (`um2_algebra.py`), geo (`um2_geometry.py`), bg (`um2_background.py`), fld (`um2_fields.py`), mass (`um2_spectra.py`), flav (`um2_flavour.py`), nu (`um2_neutrino.py`), ksv, kss, ks8, ks592, ksdm, ksp, ksfb (`um2_ks_jobs.py` validate, spectrum, ground8, ground592, darkmatter, portals, feedback), ew (`um2_electroweak.py`), prim (`um2_primordial.py`), cos (`um2_cosmology.py`), ana (`um2_analysis.py`), th (`um2_thermal.py`), cpl (`um2_coupled.py`), ser (`um2_series.py`) and res (`um2_residuals.py`, version 4: res 1 to 26 are the residuals of the solution in its equations, res 27 to 52 the links in concert). The field equations that this document uses are written out where they are used (FE-1, FE-31, FE-32, FE-56, FE-64 to FE-66 in sections 4 and 5; FE-2, FE-47, FE-55, FE-67, FE-75, FE-76, FE-79, FE-102, FE-115, FE-120 to FE-123 and FE-131 in section 10).

| FE | field equation (status) | how it was obtained and solved | verified by |
|:------|:-------------------------|:----------------------------------------|:------------------------|
| FE-1 | The Einstein-Lovelock equations (AUTHOR) | metric variation of IN-2 and of the matter action: the author's notebook equations with a source (section 4); solved at order 0 through FE-38 to FE-40 and at order $\epsilon$ through FE-49 | geo 4-12, 16-18; res 1 |
| FE-2 | The energy-momentum tensor: definition and components (STANDARD) | definition (for spinors the variation with respect to the vielbein) | ks8 2; ks592 2 |
| FE-3 | The total source of gravity (DERIVED) | sum of the energy-momentum tensors of the terms of IN-1 | cpl 14; res 9, 11 |
| FE-4 | The energy-momentum tensor of the stabiliser (DERIVED) | metric variation of IN-4 with $\rho_{\mathrm{stab}} \propto f^{-8}$ | bg 10, 13, 15; res 1 |
| FE-5 | The energy-momentum tensor of dirac16complex (DERIVED) | symmetrised vielbein variation of IN-5; for Kohn-Sham states it is FE-67 | ks8 2, 3; ks592 2-4; ksdm 3; ana 20 |
| FE-6 | The energy-momentum tensor of the Standard-Model fermions (DERIVED) | vielbein variation of IN-11; used through ideal and degenerate gases with the $x_0$ masses | th 1; cpl 14 |
| FE-7 | The energy-momentum tensor of the gauge fields (STANDARD) | metric variation of IN-8 | bg 19; ks592 4 |
| FE-8 | The energy-momentum tensor of the tip (DERIVED) | metric variation of IN-13 at $y = -L$; its effect is part of the rest energies of $W^\pm$, $Z$ and the fermions | (no separate check) |
| FE-9 | The energy-momentum tensors of the portals I11 and I13 (DERIVED) | metric variation of IN-16 and IN-18 (the frame currents do not depend on the vielbein) | cpl 13 |
| FE-10 | The energy-momentum tensor of the portal I12 (DERIVED) | metric variation of IN-17 | cpl 15; res 12 |
| FE-11 | Conservation of the source (DERIVED) | diffeomorphism invariance: the Bianchi identities of the Lovelock tensors | geo 6-8; ks8 2; ks592 2 |
| FE-12 | The dirac16complex field equation with the canonical spin connection and the portals (DERIVED) | variation of IN-5 and IN-16 to IN-18 with respect to $\bar\Psi$; reduced exactly to FE-56 | fld 1; cpl 6; ksp 5 |
| FE-13 | The canonical spin connection on the order-0 metric (DERIVED) | IN-7 evaluated on FE-31 (sympy, both halves of a period) | geo 22-25 |
| FE-14 | The Dirac equation of the quark doublets $Q_i$ (DERIVED) | variation of IN-11, IN-13, IN-16, IN-18 with respect to $\bar Q_i$; solved by FE-56 to FE-60 | fld 1, 8, 12, 13; mass 11-13; flav 3 |
| FE-15 | The Dirac equation of the up-type quark singlets $u_{Ri}$ (right-handed up, charm and top quarks) (DERIVED) | as FE-14, with respect to $\bar u_{Ri}$ | fld 9, 12, 13; mass 11-13; flav 3 |
| FE-16 | The Dirac equation of the down-type quark singlets $d_{Ri}$ (right-handed down, strange and bottom quarks) (DERIVED) | as FE-14, with respect to $\bar d_{Ri}$; the tip matrix of the sector is the CKM matrix | fld 9, 12, 13; mass 11-13; flav 3 |
| FE-17 | The Dirac equation of the lepton doublets (left-handed neutrinos and charged leptons of three flavours) (DERIVED) | variation of IN-11, IN-13, IN-16 with respect to $\bar\ell_i$ (no I13 term) | fld 8, 12, 13; mass 11-13; flav 3, 7 |
| FE-18 | The Dirac equation of the right-handed charged leptons $e_{Ri}$ (electron, muon and tau) (DERIVED) | as FE-17, with respect to $\bar e_{Ri}$ | fld 9, 12, 13; mass 11-13 |
| FE-19 | The Dirac equation of the right-handed neutrinos $\nu_{Ri}$ (DERIVED) | as FE-17, with respect to $\bar\nu_{Ri}$ (gauge singlets) | mass 11, 13; flav 3; cpl 10 |
| FE-20 | The fermion currents of the gauge fields (STANDARD) | variation of IN-11 with respect to the gauge fields | ew 1-4 |
| FE-21 | The field-dependent gauge couplings produced by I12 (DERIVED) | IN-8 and IN-17 combined | cpl 15, 16; res 12 |
| FE-22 | The Yang-Mills equation of the gluons (DERIVED) | variation of IN-8, IN-11, IN-17 with respect to the gluon field | fld 14; mass 1, 3 |
| FE-23 | The Yang-Mills equation of the SU(2) field $W^I$ (matrix form) with the tip current (DERIVED) | variation of IN-8, IN-11, IN-13, IN-17 with respect to the SU(2) field, in the unitary gauge | fld 14, 15; mass 6-8 |
| FE-24 | The Yang-Mills equation of the hypercharge field $B$ (DERIVED) | as FE-23, with respect to the hypercharge field | fld 14, 15 |
| FE-25 | The $W^+$, $W^-$, $Z$ and photon field equations to linear order in the fields (I12 neglected) (DERIVED) | FE-23 and FE-24 at linear order with IN-10 | ew 2-4; mass 3, 7, 8 |
| FE-26 | The tip sigma field equation (the Noether identity of the gauge symmetry) (STANDARD) | variation of IN-13 with respect to $\Sigma$ (the Noether identity of the gauge symmetry) | fld 16 |
| FE-27 | The boundary conditions of gravity and the gauge fields at the fold and the tip (DERIVED) | boundary terms of the variation at the fold and at the tip | fld 15 |
| FE-28 | The boundary conditions of dirac16complex (DERIVED) | the record's fold and tip conditions; self-adjoint | fld 5, 7; kss 1 |
| FE-29 | The boundary conditions of the Standard-Model fermions (INVENTED) | selection projector chosen so that each doublet has one left-handed and each singlet one right-handed Weyl zero mode | fld 3-5, 8-10; ew 12 |
| FE-30 | The tip mixing conditions of one and of three generations (DERIVED) | IN-13 on the zero modes; self-adjoint for every complex matrix (sympy, 42 real variables); the tip matrices ASSUMED | fld 12, 13; flav 3, 4 |
| FE-31 | The order-0 metric in the author's coordinates (AUTHOR) | the record's corrected metric (section 5) in the author's coordinates | geo 1-3 |
| FE-32 | The hidden coordinate $y$, the block scale and the rates of the background (DERIVED) | change of chart to $y$ (section 5) | geo 1-3, 22 |
| FE-33 | The sectional curvatures of the order-0 metric (DERIVED) | Riemann tensor of FE-31 in both charts (sympy) | geo 1-3 |
| FE-34 | The Lovelock densities and tensors of a pair-diagonal curvature (DERIVED) | pairing formula, coefficients $2^pp!$ and $-2^{p-1}p!$ (sympy) | geo 4-12; bg 4 |
| FE-35 | The first Lovelock tensor (the Einstein tensor) of the order-0 metric (DERIVED) | FE-34 with FE-33 (sympy, four routes) | geo 4, 6, 10, 13; bg 1, 4 |
| FE-36 | The second Lovelock tensor (Gauss-Bonnet) of the order-0 metric (DERIVED) | as FE-35 | geo 5, 7, 11, 14; bg 2, 4 |
| FE-37 | The third Lovelock tensor of the order-0 metric (DERIVED) | as FE-35 | geo 8, 12, 15; bg 3, 4 |
| FE-38 | The background equation: the $x_4$ component (the constraint) (DERIVED) | FE-1 with FE-35 to FE-37, the author's weights and $\Lambda$ | geo 16, 19; prim 1; res 1, 3 |
| FE-39 | The background equation: the 3-space component (DERIVED) | as FE-38; integrated through the primordial era (DOP853) | geo 17, 20; bg 14; prim 1-5; res 1, 3 |
| FE-40 | The background equation: the hidden (block) component (DERIVED) | as FE-38; the $x_0$ and the extra-time components have the same left side, and the order-0 metric (one block scale) obeys their average with $\bar p$ | geo 18, 21; bg 1-3, 14; res 1, 3 |
| FE-41 | The conservation of the order-0 source (DERIVED) | FE-11 on FE-31 | bg 15; prim 1 |
| FE-42 | The static block (DERIVED) | FE-38 to FE-40 with $\mathcal{H}_f = 0$, $\dot{\mathcal{H}} = 0$ | geo 19-21; bg 5-9; res 1 |
| FE-43 | The stabilised block (DERIVED) | closed form (sympy) | bg 10-13, 15; res 1, 48 |
| FE-44 | The linearised block and the radion (DERIVED) | Jacobian of FE-39 and FE-40 at the static block | bg 16, 17; prim 2; ana 22; res 2, 47 |
| FE-45 | The response of the block to matter to first order (DERIVED) | linearisation with block-averaged sources | bg 18; res 2 |
| FE-46 | The coefficients of the first-order block response (DERIVED) | exact algebraic numbers (sympy) | bg 18, 19; res 46 |
| FE-47 | The adiabatic block response and the four-dimensional Friedmann acceleration equation (DERIVED) | FE-45 with the second time derivative of $\Delta K$ neglected | bg 19; ksfb 1; res 2, 9 |
| FE-48 | The four-dimensional reduction of the Lovelock action on the static block (DERIVED) | dimensional reduction on the static block (sympy) | bg 20-22; ksfb 2; ana 21; res 4 |
| FE-49 | The four-dimensional effective gravity and the four-dimensional couplings (DERIVED) | the reduced action and the zero modes of the gauge fields | bg 21, 22; ana 23; res 4, 37 |
| FE-50 | The $x_0$ eigenvalue equation of the gauge fields and the graviton (DERIVED) | reduction of FE-22 to FE-25 (and of FE-1 for the transverse-traceless graviton) on the static block | fld 14; mass 1-4; ana 1-7; ser 2; res 5 |
| FE-51 | The fold and tip conditions of the boson $x_0$ profiles (DERIVED) | natural boundary conditions of IN-15 | fld 15; mass 6, 7; res 5 |
| FE-52 | The boson eigenvalue conditions (DERIVED) | exact solution of FE-50: mpmath roots (30 to 60 digits), finite elements as a check | mass 1-5, 9; flav 5; ana 2; res 5 |
| FE-53 | The tower of Kaluza-Klein gravitons (the terms $n \ge 1$ of the metric series) (DERIVED) | exact eigenfunctions of FE-50 with $\beta = 0$ | mass 1, 2; ser 2; res 15 |
| FE-54 | The potential between two static masses with the Kaluza-Klein gravitons (DERIVED) | exchange of the tower between two static sources | ser 2; res 15 |
| FE-55 | The $W^\pm$ and $Z$ masses, the electroweak parameter and the Kaluza-Klein scale (DERIVED) | fit of $\beta_{\mathrm{W}}$ by bisection in $\ln\beta_{\mathrm{W}}$ (80 steps) | mass 7, 8, 10; res 5, 13, 29, 30 |
| FE-56 | The exact reduction of the eight-dimensional Dirac equation to the block Hamiltonian (DERIVED) | the record's reduction, re-derived exactly for all eight blocks with the author's matrices (sympy) | fld 1, 2; alg 19-29 |
| FE-57 | The chiral zero modes (massless four-dimensional fermions) (DERIVED) | exact solutions of FE-56 at $k = 0$ | fld 6-11; kss 2 |
| FE-58 | The tip values of the doublet and singlet solutions at $k = 0$ (DERIVED) | exact solutions of the doublet and singlet systems | mass 11-13 |
| FE-59 | The exact mass condition of one generation and its first-order root (DERIVED) | FE-58 in FE-30; mpmath roots, shooting (DOP853) as a check | mass 11-14; ana 8, 9; res 6 |
| FE-60 | The mass condition of three generations with the $3 \times 3$ tip matrices (DERIVED) | FE-58 in the three-generation FE-30; mpmath at 50 digits | flav 3, 4, 7; res 6 |
| FE-61 | The standard parametrisation of the mixing matrices (the tip matrices of UM-2) (STANDARD) | NuFIT 6.0 and PDG values (section 7) | flav 1, 2, 6; res 33 |
| FE-62 | The spectrum of dirac16complex on the static block (DERIVED) | exact solution of FE-56 with $M = m_\Psi$ | kss 1-3; ew 13; ana 12; res 7 |
| FE-63 | The Kohn-Sham equations of dirac16complex coupled to all fields (DERIVED) | the record's block Hamiltonian with the mean fields FE-64; Galerkin in the free basis, Anderson mixing, Richardson in the basis size | ksv 1, 2; ks8 1; ks592 1; cpl 1, 7; res 8 |
| FE-64 | The Kohn-Sham mean fields (DERIVED) | the record's Hartree-plus-exchange fields of the contact term and the portal mean fields of IN-16 to IN-18 | ksp 1-4; cpl 1, 7, 13; res 8, 10, 11 |
| FE-65 | The Kohn-Sham densities, shells, cell volume and occupations (RECORD) | the record's definitions | ksv 1, 2 |
| FE-66 | The Kohn-Sham energy (RECORD) | the record's functional | ks8 3; ks592 3; ksdm 1 |
| FE-67 | The energy-momentum tensor of a Kohn-Sham state (DERIVED) | FE-5 for Kohn-Sham states | ksdm 2, 3; ks592 4; ana 19; res 9, 28 |
| FE-68 | The energy identity and the $y$-conservation law of a Kohn-Sham state (DERIVED) | from FE-66, FE-67 and FE-11 | ks8 2, 3; ks592 2, 3; res 8 |
| FE-69 | The boundary conditions of the Kohn-Sham orbitals (DERIVED) | block form of FE-28 ($\gamma^{x_0} = \sigma_3$ in every block) | alg 20; fld 5; ew 13 |
| FE-70 | The portals I11 and I13 on the zero modes: the four-dimensional contact interactions (DERIVED) | reduction of IN-16 and IN-18 with the zero-mode profiles | cpl 1, 3, 5-7, 9; ksp 1-3; res 10, 40 |
| FE-71 | The portal I12 on the dark matter (DERIVED) | reduction of IN-17 with the dark-matter orbital | ksp 4; ana 17; res 10, 41 |
| FE-72 | The shift of a Kohn-Sham level by the mean fields of an environment (DERIVED) | first order in the mean fields (Hellmann-Feynman) | cpl 1, 2, 13; res 11 |
| FE-73 | The level shift of the dark matter in matter of protons, neutrons and electrons (DERIVED) | FE-72 for protons, neutrons and electrons | cpl 13; res 11 |
| FE-74 | The thermal gluon condensate from the trace anomaly (STANDARD) | trace anomaly (Shifman, Vainshtein, Zakharov) | cpl 13; res 11 |
| FE-75 | The QCD interaction measure (ESTIMATE) | lattice-like shape below 1 GeV, leading order above | cpl 13 |
| FE-76 | The thermal condensate of a massive vector boson and the order-$\alpha_{\mathrm{G}}$ condensate of a gauge plasma (STANDARD) | free part; Feynman-Hellmann at order $\alpha_{\mathrm{G}}$ | cpl 13; res 11, 22 |
| FE-77 | The running electroweak couplings without a Higgs particle (STANDARD) | one loop from the $\overline{\mathrm{MS}}$ values at $m_{\mathrm{Z}}$ | cpl 13 |
| FE-78 | The electroweak condensates of a hot plasma (ESTIMATE) | FE-76 with FE-77; thermal suppression below $m_{\mathrm{W}}$ | cpl 13 |
| FE-79 | dirac16complex acting on the Standard Model: the coupling shifts and the $x_0$ problem of $W^\pm$ and $Z$ (DERIVED) | FE-21 and FE-50 with the dark-matter scalar density; first-order perturbation theory (version 4) | cpl 15; res 12, 45 |
| FE-80 | Gravity in the coupled solution: the block response to every species (DERIVED) | FE-47 with all species, iterated with the masses | cpl 14; res 11 |
| FE-81 | The hidden pressure of matter and of the hot plasma (DERIVED) | $\bar p = \frac14\,\mathrm{d}p/\mathrm{d}\ln f$ at fixed temperature | cpl 14; res 11, 39 |
| FE-82 | The block dependence of a gauge coupling and the trace of an electroweak plasma (DERIVED) | $g_{\mathrm{G}}^2 \propto f^{-4}$, $m_{\mathrm{KK}} \propto 1/f$, one loop | cpl 14 |
| FE-83 | The block dependence of the QCD scale and of the nucleon mass (ESTIMATE) | one loop; nucleon sigma terms | cpl 12; res 52 |
| FE-84 | The block dependence of the QCD scale through the quark thresholds (ESTIMATE) | one-loop matching at the quark thresholds | cpl 12; res 52 |
| FE-85 | The block dependence of a fermion mass (DERIVED) | FE-59 with localisations proportional to $f$ | ana 11; cpl 12; res 52 |
| FE-86 | The densities of the environments of the coupled solution (ASSUMED) | net baryons in weak equilibrium; dark matter in equilibrium below $x = 40$ | cpl 13; res 11 |
| FE-87 | The metric as a power series of terms of decreasing magnitude (DERIVED) | magnitudes of the computed terms | ser 1-4; res 16 |
| FE-88 | The order-1, $n = 0$ term of the metric in the Newtonian gauge (eight dimensions) (DERIVED) | Newtonian gauge in eight dimensions | ser 1, 3; res 16 |
| FE-89 | The four-dimensional perturbed metric in conformal time (STANDARD) | Newtonian gauge (Ma and Bertschinger) | cos 3 |
| FE-90 | The linearised Einstein equations for a Fourier mode (STANDARD) | CAMB 2.0.5 (default accuracy, lensing) | cos 1, 3, 4, 8; res 14 |
| FE-91 | The perturbations of the dark matter (cold) (STANDARD) | CAMB; cold (a Kohn-Sham quantum at rest has zero pressure) | cos 3; ksdm 2 |
| FE-92 | The perturbations of the baryons (STANDARD) | CAMB | cos 3, 4 |
| FE-93 | The perturbations of the photons: density and velocity (STANDARD) | CAMB | cos 3 |
| FE-94 | The photon temperature hierarchy (STANDARD) | CAMB | cos 3 |
| FE-95 | The photon polarisation hierarchy (STANDARD) | CAMB | cos 3 |
| FE-96 | The hierarchy of each neutrino mass state (the cosmic neutrino background) (STANDARD) | CAMB, the three mass states separately (masses iterated) | cos 2, 6, 7; res 32, 34 |
| FE-97 | The background expansion, the neutrino temperature and the primordial spectrum (STANDARD) | Planck 2018 parameters; $N_{\mathrm{eff}} = 3.0432 + 0.0010$ | cos 1, 4, 6; res 35, 38 |
| FE-98 | The size of the first-order potentials: rms value, Poisson equation and large scales (STANDARD) | from the CAMB solution | cos 8; ser 1; res 14 |
| FE-99 | The amplitude of the matter fluctuations (STANDARD) | from the CAMB matter power spectrum | cos 8; res 50 |
| FE-100 | The three neutrino masses (ASSUMED) | $m_1$ and the ordering chosen, the splittings of NuFIT 6.0; $x_0$ eigenvalues of FE-59 | nu 1, 16; mass 11; res 32 |
| FE-101 | The four-fermion interactions at low energy (STANDARD) | exchange of $W^\pm$ and $Z$ far below their masses | nu 2-5; ew 6-11 |
| FE-102 | The Fermi constant and the neutral-current couplings (STANDARD) | tree level; the measured $G_{\mathrm{F}}$ | ew 4, 16, 18, 19; res 13, 30 |
| FE-103 | The matter potentials of forward scattering (STANDARD) | forward scattering in an unpolarised medium | nu 3-5, 11 |
| FE-104 | The flavour evolution in vacuum and in matter (STANDARD) | exact matrix exponentials; ordered products of layers | nu 2-5; res 17 |
| FE-105 | The vacuum oscillation probability, CPT and the T-odd difference (STANDARD) | analytic | nu 2; res 17 |
| FE-106 | The MSW resonances of the 1-3 and 1-2 sectors (STANDARD) | two-flavour conditions; the exact three-flavour root as a check | nu 3, 5; res 17 |
| FE-107 | The adiabatic survival probability of solar electron neutrinos (STANDARD) | adiabatic formula; numerical evolution as a check | nu 5; res 17 |
| FE-108 | The resonance density, the adiabaticity and the Landau-Zener jump probability (STANDARD) | two-flavour conditions | nu 11; res 17 |
| FE-109 | The thermal potential of the early Universe (STANDARD) | leading order in $T/m_{\mathrm{W}}$; Brent roots | nu 6; res 18 |
| FE-110 | The quantum kinetic equations of a neutrino gas (STANDARD) | linearised (FE-117) and momentum averaged (FE-111) | nu 8, 9, 12-14 |
| FE-111 | Neutrino decoupling: the temperature equations (STANDARD) | Escudero's method; LSODA from 20 MeV to 5 keV | nu 8, 9; res 19 |
| FE-112 | The energy transfer by collisions (STANDARD) | Escudero's kernels with the radiatively corrected couplings | nu 8, 9 |
| FE-113 | The finite-temperature QED pressure of the electron-photon plasma (STANDARD) | Bennett et al. | nu 7 |
| FE-114 | The integrals of the QED pressure (STANDARD) | Gauss-Legendre panels | nu 7 |
| FE-115 | The effective number of neutrino species and the common temperature (STANDARD) | from FE-111; the precision value 3.0432 is adopted | nu 8, 9; res 19, 35, 49 |
| FE-116 | The fast flavour instability: the electron-lepton-number distribution (STANDARD) | definitions; axially symmetric gas | nu 12, 13; res 20 |
| FE-117 | The fast flavour instability: the dispersion relation (STANDARD) | vectorised Newton iterations | nu 12, 13; res 20 |
| FE-118 | The axisymmetric and azimuthal branches of the dispersion relation (STANDARD) | analytic | nu 13 |
| FE-119 | The homogeneous mode and the mode $k_{\mathrm{f}} = \mathcal{I}_1$ (STANDARD) | 300-node discretisation; analytic growth | nu 12, 14, 15; res 20 |
| FE-120 | The cosmic neutrino background (STANDARD) | adaptive quadrature (to $3\times10^{-16}$ since version 4) | nu 10; res 21, 34 |
| FE-121 | The ideal-gas densities of a species of the plasma (STANDARD) | Gauss-Legendre quadrature with the $x_0$ masses | th 1; res 22, 31, 39 |
| FE-122 | The effective degrees of freedom and the Hubble rate of the hot Universe (STANDARD) | sums of FE-121 | th 1; res 22, 37 |
| FE-123 | The QCD crossover, the neutrino temperature after decoupling and the cooling of the plasma (ASSUMED) | smooth switch; instantaneous neutrino decoupling at 2 MeV | th 1; res 22, 38 |
| FE-124 | The Boltzmann equation of one dark-matter species (STANDARD) | implicit Radau on $\ln Y_{\mathrm{DM}}$ | th 3, 4; cpl 8; res 23 |
| FE-125 | The relativistic thermal average of the annihilation cross-section (STANDARD) | Gondolo and Gelmini; adaptive quadrature | th 2; res 23 |
| FE-126 | The relic density (STANDARD) | from FE-124 | th 3, 4; cpl 8; res 23, 36 |
| FE-127 | The annihilation cross-sections of the dark matter through I12 and I13 (DERIVED) | spin traces and polarisation sums of FE-70 and FE-71 | ana 13-16; cpl 8; res 23 |
| FE-128 | The partial-wave unitarity bounds (DERIVED) | partial waves $^3P_0$ and $^3S_1$ | th 5-7; ana 16; cpl 8 |
| FE-129 | The freeze-in of the fold bands through I11 (DERIVED) | FE-70 with Maxwell-Boltzmann statistics; trapezoid rule | cpl 4; res 24 |
| FE-130 | The dark radiation of the fold bands and their departure from equilibrium (DERIVED) | from FE-129 | cpl 4; cos 6, 7; res 24, 35 |
| FE-131 | The right-handed neutrinos if I13 coupled to $B - L$ (DERIVED) | Radau in the shifted variable $x - 2$ (version 4) | cpl 10; res 25 |
| FE-132 | The elastic scattering of right-handed neutrinos on the dark matter (ESTIMATE) | a Weyl $\nu_R$ on a heavy Dirac fermion | cpl 10; res 25 |
| FE-133 | The extra radiation of species that decouple early (DERIVED) | entropy conservation with the heating factor | cpl 10, 11; cos 5; res 49 |
| FE-134 | The production of right-handed neutrinos through I11 (with the baryon current in I13) (DERIVED) | ratio of the I11 and I13 rates | cpl 10; res 25 |
| FE-135 | The self-interaction channel of the dark matter into the fold bands (ESTIMATE) | IN-5 on the dark matter and the fold bands; Fierz coefficients not computed | cpl 11; res 10, 26 |
| FE-136 | The energy put into the fold bands by the self-interaction channel (DERIVED) | trapezoid rule from $T_{\mathrm{max}}$ to the freeze-out | cpl 11; res 26 |

