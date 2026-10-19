from build_lib import R

# ------------------------------------------------------------------ neutrino masses and mixing
R('mnu123', r'm_1,\ m_2,\ m_3', [r'm_1', r'm_2', r'm_3'], r'The masses of the neutrino mass states $\nu_1$, $\nu_2$, $\nu_3$ '
  r'(normal ordering).', 'GeV (quoted in meV)', r'1.000, 8.712, 50.140 meV ($m_1$ ASSUMED)', 'DERIVED')
R('dm2', r'\Delta m_{21}^2,\ \Delta m_{31}^2,\ \Delta m_{32}^2', [r'm_{21}', r'm_{31}', r'm_{32}'], r'The differences of the '
  r'squared neutrino masses, $\Delta m_{ij}^2 = m_i^2 - m_j^2$.', 'GeV^2 (quoted in eV^2)',
  r'$\Delta m_{21}^2 = 7.49\times10^{-5}$ eV$^2$, $\Delta m_{31}^2 = 2.513\times10^{-3}$ eV$^2$ (NuFIT 6.0)', 'STANDARD')
R('dmee', r'\Delta m_{ee}^2', [r'm_{ee}'], r'The effective squared-mass difference of electron-neutrino disappearance, '
  r'$\Delta m_{ee}^2 = c_{12}^2\Delta m_{31}^2 + s_{12}^2\Delta m_{32}^2$.', 'GeV^2', status='STANDARD')
R('thetamix', r'\theta_{ij}', [r'\theta', r'\theta_{12}', r'\theta_{13}'], r'The mixing angles of the standard '
  r'parametrisation of $U$ (or of $V_{\mathrm{CKM}}$): $\theta_{12}$, $\theta_{13}$, $\theta_{23}$; in two-flavour formulas '
  r'$\theta_{ij}$ is the angle of the sector $(i, j)$.', 'dimensionless',
  r'$\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$ (PMNS)', 'STANDARD')
R('thetam', r'\theta^{\mathrm{m}}_{12}', [r'\theta^{\mathrm{m}}', r'\theta^{\mathrm{m}}_{12}'], r'The effective 1-2 mixing '
  r'angle in matter at the production point of a solar neutrino.', 'dimensionless', status='STANDARD')
R('nuflav', r'\nu_\alpha,\ \nu_i', [r'\nu', r'\nu_\mu'], r'A left-handed neutrino: $\nu_\alpha$ of the flavour '
  r'$\alpha = e, \mu, \tau$ ($\nu_e$, $\nu_\mu$, $\nu_\tau$), $\nu_i$ of the mass state $i$ (mass $m_i$).', 'GeV^(3/2)',
  status='STANDARD')
R('nubar', r'\bar\nu_\alpha', [r'\bar\nu'], r'The antineutrino of the flavour $\alpha$; in a Lagrangian the Dirac adjoint of the '
  r'neutrino field (it annihilates antineutrinos).', 'GeV^(3/2)', status='STANDARD')
R('ellminus', r'\ell^-_\alpha,\ \bar\ell^-_\alpha', [r'\ell^-', r'\bar\ell^-'], r'The charged lepton of the flavour $\alpha$ '
  r'($e^-$, $\mu^-$, $\tau^-$; the lower member of the lepton doublet) at low energy, and its Dirac adjoint.', 'GeV^(3/2)',
  status='STANDARD')
R('LCC', r'\mathcal{L}_{\mathrm{CC}},\ \mathcal{L}_{\mathrm{NC}}', [r'\mathcal{L}_{\mathrm{CC}}', r'\mathcal{L}_{\mathrm{NC}}'],
  r'The charged-current and neutral-current four-fermion Lagrangians (exchange of $W^\pm$ and of $Z$ far below their masses).',
  'GeV^4', status='STANDARD')
R('GF', r'G_{\mathrm{F}}', [r'G_{\mathrm{F}}'], r'The Fermi constant.', 'GeV^-2', r'$1.1663788\times10^{-5}$ GeV$^{-2}$ (measured)',
  'STANDARD')
R('gtilde', r'\tilde g^f_L,\ \tilde g^f_R,\ \tilde g^f_V', [r'\tilde g'], r'The neutral-current couplings of the fermion $f$ to '
  r'the $Z$ (left-handed, right-handed and vector), $\tilde g^f_L = T_3^f - Q^f_{\mathrm{em}}\sin^2\theta_{\mathrm{W}}$.',
  'dimensionless', status='STANDARD')
R('gnue', r'\tilde g^{\nu_e e}_L,\ \tilde g^{\nu_e e}_R', [r'\tilde g^{\nu_e e}'], r'The effective left- and right-handed '
  r'couplings of electron neutrinos to electrons (charged and neutral current), '
  r'$\tilde g^{\nu_e e}_L = \frac12 + \sin^2\theta_{\mathrm{W}}$, $\tilde g^{\nu_e e}_R = \sin^2\theta_{\mathrm{W}}$.',
  'dimensionless', r'0.727 and 0.233 (radiatively corrected)', 'STANDARD')
R('gnumu', r'\tilde g^{\nu_\mu e}_L,\ \tilde g^{\nu_\mu e}_R', [r'\tilde g^{\nu_\mu e}'], r'The effective couplings of muon '
  r'(and tau) neutrinos to electrons (neutral current only), $\tilde g^{\nu_\mu e}_L = -\frac12 + \sin^2\theta_{\mathrm{W}}$, '
  r'$\tilde g^{\nu_\mu e}_R = \sin^2\theta_{\mathrm{W}}$.', 'dimensionless', r'$-0.273$ and 0.233 (radiatively corrected)',
  'STANDARD')
R('Vmat', r'V_\alpha,\ V', ['V', r'V_\mu'], r'The matter potential of forward scattering: $V_\alpha$ of the flavour $\alpha$ '
  r'($V_e$, $V_\mu$), $V$ the $3 \times 3$ matrix of the potentials in the flavour basis; antineutrinos have $-V$.', 'GeV',
  status='STANDARD')
R('VCC', r'V_{\mathrm{CC}},\ V_{\mathrm{NC}}', [r'V_{\mathrm{CC}}', r'V_{\mathrm{NC}}'], r'The charged-current potential of '
  r'electron neutrinos and the neutral-current potential common to all flavours.', 'GeV', status='STANDARD')
R('Vnunu', r'V_{\nu\nu}', [r'V_{\nu\nu}'], r'The potential of neutrino-neutrino forward scattering (a matrix in flavour space).',
  'GeV', status='STANDARD')
R('nepm', r'n_{e^-},\ n_{e^+}', [r'n_{e^-}', r'n_{e^+}'], r'The number densities of electrons and of positrons.', 'GeV^3',
  status='STANDARD')
R('nfbar', r'n_{\bar f}', [r'n_{\bar f}'], r'The number density of the antiparticles of the fermion $f$.', 'GeV^3',
  status='STANDARD')
R('bspsi', r'\boldsymbol{\psi}', [r'\boldsymbol{\psi}'], r'The vector of the three flavour amplitudes of a neutrino.',
  'dimensionless', status='STANDARD')
R('Hfl', r'H_{\mathrm{fl}}', [r'H_{\mathrm{fl}}'], r'The flavour Hamiltonian of a neutrino of energy $E$ (vacuum mass term plus '
  r'matter potential).', 'GeV', status='STANDARD')
R('Hvac', r'H^{\mathrm{vac}}_{\vec k}', [r'H^{\mathrm{vac}}'], r'The vacuum flavour Hamiltonian of a neutrino of momentum '
  r'$\vec k$.', 'GeV', status='STANDARD')
R('Eenergy', r'E', ['E'], r'The energy of a particle: of the neutrino in the flavour equations, $E = (k^2 + m^2)^{1/2}$ of a '
  r'particle of momentum $k$ in the thermal integrals.', 'GeV', status='STANDARD')
R('calU', r'\mathcal{U}', [r'\mathcal{U}'], r'The flavour evolution operator over the baseline $L_{\mathrm{b}}$; '
  r'$\mathcal{U}_{\beta\alpha}$ the amplitude of $\nu_\alpha \to \nu_\beta$.', 'dimensionless', status='STANDARD')
R('Lb', r'L_{\mathrm{b}}', [r'L_{\mathrm{b}}'], r'The baseline: the distance travelled by the neutrino.', 'length',
  status='STANDARD')
R('calP', r'\mathcal{P}', [r'\mathcal{P}'], r'The probability of a flavour transition, $\mathcal{P}(\nu_\alpha \to \nu_\beta)$; '
  r'$\mathcal{P}_{ee}$ the survival probability of electron neutrinos.', 'dimensionless', status='STANDARD')
R('Deltaij', r'\Delta_{ij}', [r'\Delta_{ij}', r'\Delta_{21}', r'\Delta_{31}', r'\Delta_{32}'], r'The oscillation phase of the '
  r'pair of mass states $(i, j)$, $\Delta_{ij} = \Delta m_{ij}^2L_{\mathrm{b}}/(4E)$.', 'dimensionless', status='STANDARD')
R('AMSW', r'A_{\mathrm{MSW}}', [r'A_{\mathrm{MSW}}'], r'The ratio of the matter term to the vacuum term in the 1-2 sector.',
  'dimensionless', status='STANDARD')
R('neres', r'n_{\mathrm{e}}^{\mathrm{res}}', [r'n_{\mathrm{e}}^{\mathrm{res}}'], r'The electron density of an MSW resonance.',
  'GeV^3', status='STANDARD')
R('gammaad', r'\gamma_{\mathrm{ad}}', [r'\gamma_{\mathrm{ad}}'], r'The adiabaticity parameter of a resonance (adiabatic for '
  r'$\gamma_{\mathrm{ad}} \gg 1$).', 'dimensionless', status='STANDARD')
R('PLZ', r'\mathcal{P}_{\mathrm{LZ}}', [r'\mathcal{P}_{\mathrm{LZ}}'], r'The Landau-Zener probability of a jump between the '
  r'matter eigenstates at a resonance.', 'dimensionless', status='STANDARD')
R('rhoe', r'\rho_{\mathrm{e}},\ p_{\mathrm{e}}', [r'\rho_{\mathrm{e}}', r'p_{\mathrm{e}}'], r'The energy density and the '
  r'pressure of the electrons and positrons together (ideal gas).', 'GeV^4', status='STANDARD')
R('boldrho', r'\boldsymbol{\rho}_{\vec k},\ \bar{\boldsymbol{\rho}}_{\vec k}', [r'\boldsymbol{\rho}', r'\bar{\boldsymbol{\rho}}'],
  r'The $3 \times 3$ flavour density matrices of the neutrinos and of the antineutrinos of momentum $\vec k$.',
  'dimensionless', status='STANDARD')
R('Ccoll', r'C_{\mathrm{coll}}', [r'C_{\mathrm{coll}}'], r'The collision term of the quantum kinetic equations.', 'GeV',
  status='STANDARD')
R('Tnua', r'T_{\nu_\alpha},\ T_{\nu_e},\ T_{\nu_\mu}', [r'T_{\nu_\alpha}', r'T_{\nu_e}', r'T_{\nu_\mu}'], r'The temperature of '
  r'the neutrinos of the flavour $\alpha$ (of $\nu_e$, of $\nu_\mu$ and $\nu_\tau$) during decoupling.', 'GeV',
  status='STANDARD')
R('Cnua', r'C_{\nu_\alpha},\ C_{\nu_e},\ C_{\nu_\mu}', [r'C_{\nu_\alpha}', r'C_{\nu_e}', r'C_{\nu_\mu}'], r'The energy '
  r'transfer rate per volume into the neutrinos of the flavour $\alpha$ by collisions.', 'GeV^5', status='STANDARD')
R('rhonu', r'\rho_\nu,\ \rho_{\nu_\alpha}', [r'\rho_\nu', r'\rho_{\nu_\alpha}'], r'The energy density of one neutrino flavour '
  r'(neutrinos and antineutrinos) at the common temperature $T_\nu$, $\frac78\frac{\pi^2}{15}T_\nu^4$ when massless; '
  r'$\rho_{\nu_\alpha}$ that of the flavour $\alpha$ at its temperature $T_{\nu_\alpha}$.', 'GeV^4', status='STANDARD')
R('MPl', r'M_{\mathrm{Pl}}', [r'M_{\mathrm{Pl}}'], r'The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$.', 'GeV',
  r'$1.22091\times10^{19}$ GeV', 'STANDARD')
R('Ftr', r'\mathcal{F}_{\mathrm{tr}}', [r'\mathcal{F}_{\mathrm{tr}}'], r'The energy-transfer function of two species with the '
  r'temperatures $T_{\mathrm{A}}$ and $T_{\mathrm{B}}$ (Maxwell-Boltzmann with the corrections $f_{\mathrm{a}}$, $f_{\mathrm{s}}$).',
  'GeV^9', status='STANDARD')
R('TAB', r'T_{\mathrm{A}},\ T_{\mathrm{B}}', [r'T_{\mathrm{A}}', r'T_{\mathrm{B}}'], r'The temperatures of the two species '
  r'that exchange energy in $\mathcal{F}_{\mathrm{tr}}$.', 'GeV', status='STANDARD')
R('fas', r'f_{\mathrm{a}},\ f_{\mathrm{s}}', [r'f_{\mathrm{a}}', r'f_{\mathrm{s}}'], r'The Fermi-Dirac corrections of the '
  r'annihilation and scattering parts of the energy transfer.', 'dimensionless', '0.884 and 0.829', 'STANDARD')
R('Neff', r'N_{\mathrm{eff}}', [r'N_{\mathrm{eff}}'], r'The effective number of neutrino species (the radiation beyond the '
  r'photons in units of one neutrino species with $T_\nu/T_\gamma = (4/11)^{1/3}$); $\Delta N_{\mathrm{eff}}$ an addition to it.',
  'dimensionless', r'3.0432 (neutrinos) + 0.0010 (fold bands)', 'STANDARD')
R('pQED', r'p_{\mathrm{QED}},\ p_{\mathrm{QED}}^{(2)},\ p_{\mathrm{QED}}^{(3)}',
  [r'p_{\mathrm{QED}}', r'p_{\mathrm{QED}}^{(2)}', r'p_{\mathrm{QED}}^{(3)}'], r'The finite-temperature QED correction to the '
  r'pressure of the electron-photon plasma, and its parts of order $e^2$ and $e^3$.', 'GeV^4', status='STANDARD')
R('rhoQED', r'\rho_{\mathrm{QED}}', [r'\rho_{\mathrm{QED}}'], r'The QED correction to the energy density of the plasma.',
  'GeV^4', status='STANDARD')
R('eel', r'e', ['e'], r'The elementary charge (the charge of the positron), $e^2 = 4\pi\alpha_{\mathrm{em}}$; $W^+$ has the charge '
  r'$+e$ and $W^-$ the charge $-e$.', 'dimensionless', r'$e^2 = 4\pi/137.036$ at low energy', 'STANDARD')
R('calQ', r'\mathcal{Q}_1,\ \mathcal{Q}_2,\ \mathcal{Q}_3', [r'\mathcal{Q}_1', r'\mathcal{Q}_2', r'\mathcal{Q}_3'], r'The '
  r'momentum integrals of the QED pressure.', 'GeV^2', status='STANDARD')
R('nD', r'n_{\mathrm{D}}(k)', [r'n_{\mathrm{D}}'], r'The Fermi-Dirac occupation of the electrons and positrons summed over the '
  r'two spin states.', 'dimensionless', status='STANDARD')
R('k2', r'k_2,\ \vec k_2', [r'k_2', r'\vec k_2'], r'A second momentum (variable of integration).', 'GeV', status='STANDARD')
R('me', r'm_{\mathrm{e}}', [r'm_{\mathrm{e}}'], r'The electron mass.', 'GeV', '0.51099895 MeV', 'STANDARD')

# ------------------------------------------------------------------ fast flavour instability
R('GELN', r'G_{\mathrm{ELN}}(u)', [r'G_{\mathrm{ELN}}'], r'The angular distribution of the electron lepton number of a dense '
  r'neutrino gas (in units of a potential).', 'GeV', status='STANDARD')
R('nnue', r'n_{\nu_e},\ n_{\bar\nu_e}', [r'n_{\nu_e}', r'n_{\bar\nu_e}'], r'The number densities of electron neutrinos and '
  r'electron antineutrinos.', 'GeV^3', status='STANDARD')
R('gnu_ang', r'g_{\nu_e}(u),\ g_{\bar\nu_e}(u)', [r'g_{\nu_e}', r'g_{\bar\nu_e}'], r'The normalised angular distributions of '
  r'electron neutrinos and antineutrinos.', 'dimensionless', status='STANDARD')
R('ucos', r'u', ['u'], r'The cosine of the angle between a momentum and the symmetry axis $x_3$ of the neutrino gas.',
  'dimensionless', status='STANDARD')
R('utilde', r'\tilde u', [r'\tilde u'], r'A second direction cosine (variable of integration).', 'dimensionless',
  status='STANDARD')
R('calI', r'\mathcal{I}_l', [r'\mathcal{I}', r'\mathcal{I}_0', r'\mathcal{I}_1', r'\mathcal{I}_2'], r'The $l$-th angular '
  r'moment of the electron-lepton-number distribution.', 'GeV', status='STANDARD')
R('calJ', r'\mathcal{J}_l', [r'\mathcal{J}', r'\mathcal{J}_0', r'\mathcal{J}_1', r'\mathcal{J}_2'], r'The $l$-th moment of the '
  r'dispersion integral of the fast flavour instability.', 'dimensionless', status='STANDARD')
R('calC', r'\mathcal{C}(u)', [r'\mathcal{C}'], r'The flavour coherence (off-diagonal element of the density matrix) of the '
  r'neutrinos moving in the direction $u$.', 'dimensionless', status='STANDARD')
R('omegaf', r'\omega_{\mathrm{f}},\ k_{\mathrm{f}}', [r'\omega_{\mathrm{f}}', r'k_{\mathrm{f}}'], r'The frequency and the '
  r'wavenumber (along $x_3$) of a flavour wave.', 'GeV', status='STANDARD')
R('omegabar', r'\bar\omega,\ \bar k', [r'\bar\omega', r'\bar k'], r'The frequency and wavenumber of a flavour wave shifted by the '
  r'moments, $\bar\omega = \omega_{\mathrm{f}} - \mathcal{I}_0$, $\bar k = k_{\mathrm{f}} - \mathcal{I}_1$; a mode with '
  r'$\mathrm{Im}\,\bar\omega > 0$ grows.', 'GeV', status='STANDARD')
R('Pidisp', r'\Pi', [r'\Pi'], r'The $2 \times 2$ dispersion matrix of the fast flavour instability.', 'dimensionless',
  status='STANDARD')
R('vbar', r'\bar v_i', [r'\bar v'], r'The mean velocity of the relic neutrinos of the mass state $i$.', 'dimensionless (c = 1)',
  r'0.435, 0.0604, 0.0105 today', 'STANDARD')
