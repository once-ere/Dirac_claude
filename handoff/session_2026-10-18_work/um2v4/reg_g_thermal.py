from build_lib import R

# ------------------------------------------------------------------ the hot plasma
R('sentropy', r's,\ s_s', ['s'], r'The entropy density of the plasma, $s = 2\pi^2g_sT^3/45$; $s_s$ that of the species $s$.',
  'GeV^3', status='STANDARD')
R('s0', r's_0', [r's_0'], r'The entropy density today.', 'GeV^3 (quoted per cm^3)', r'2891.3 cm$^{-3}$', 'STANDARD')
R('grho', r'g_\rho,\ g_s', [r'g_\rho', r'g_s'], r'The effective numbers of relativistic degrees of freedom of the energy density '
  r'and of the entropy density of the plasma.', 'dimensionless',
  r'105.75 when every species of UM-2 in equilibrium is relativistic (no Higgs particle), 10.75 near 1 MeV, $g_s = 43/11$ today',
  'STANDARD')
R('gseg', r'g_{s,e\gamma}', [r'g_{s,e\gamma}'], r'The entropy degrees of freedom of the electrons, positrons and photons '
  r'only (after neutrino decoupling).', 'dimensionless', r'$11/2$ before and 2 after the annihilation of $e^\pm$',
  'STANDARD')
R('wQGP', r'w_{\mathrm{QGP}}(T)', [r'w_{\mathrm{QGP}}'], r'The weight of the quark-gluon plasma in the model of the QCD '
  r'crossover (1 above, 0 below).', 'dimensionless', status='ASSUMED')
R('Tcw', r'T_{\mathrm{c}},\ T_{\mathrm{w}}', [r'T_{\mathrm{c}}', r'T_{\mathrm{w}}'], r'The temperature and the width of the '
  r'QCD crossover.', 'GeV', '155 MeV and 15 MeV', 'ASSUMED')

# ------------------------------------------------------------------ dark matter: freeze-out and relic density
R('Yabund', r'Y_{\mathrm{DM}},\ Y_{\mathrm{eq}},\ Y_\infty', [r'Y_{\mathrm{DM}}', r'Y_{\mathrm{eq}}', r'Y_\infty'], r'The '
  r'abundance (number density per entropy density) of one dark-matter species (particles and antiparticles), its equilibrium '
  r'value and its final value.', 'dimensionless', status='STANDARD')
R('xMT', r'x', ['x'], r'The ratio $x = M_{\mathrm{DM}}/T$ of the dark-matter mass to the temperature.', 'dimensionless',
  r'$x_{\mathrm{f}} = 31.23$ at the freeze-out', 'STANDARD')
R('sigmaxs', r'\sigma', [r'\sigma'], r'A cross-section (of the dark-matter annihilation or production process named in the '
  r'equation; summed over the spins where marked).', 'GeV^-2', status='STANDARD')
R('vrel', r'v_{\mathrm{rel}}', [r'v_{\mathrm{rel}}'], r'The relative velocity of the two annihilating particles; '
  r'$\langle\sigma v_{\mathrm{rel}}\rangle$ the thermal average.', 'dimensionless (c = 1)', status='STANDARD')
R('nDMeq', r'n_{\mathrm{DM,eq}},\ \bar n_{\mathrm{DM,eq}}', [r'n_{\mathrm{DM,eq}}', r'\bar n_{\mathrm{DM,eq}}'], r'The '
  r'equilibrium number densities of dark-matter particles and antiparticles of one species.', 'GeV^3', status='STANDARD')
R('Kbessel', r'K_1,\ K_2', [r'K_1', r'K_2'], r'The modified Bessel functions of the second kind of orders 1 and 2 (not related '
  r'to the block variable $K$).', 'dimensionless', status='STANDARD')
R('Ecm', r'E_{\mathrm{cm}}', [r'E_{\mathrm{cm}}'], r'The total energy of the colliding pair in its centre-of-mass frame.', 'GeV',
  status='STANDARD')
R('OmegaDM', r'\Omega_{\mathrm{DM}}', [r'\Omega_{\mathrm{DM}}'], r'The dark-matter density today in units of the critical '
  r'density.', 'dimensionless', r'$\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$ (both species)', 'DERIVED')
R('rhocrit', r'\rho_{\mathrm{crit}}', [r'\rho_{\mathrm{crit}}'], r'The critical density, '
  r'$3\mathcal{H}_0^2M_{\mathrm{Pl}}^2/(8\pi)$.', 'GeV^4 (quoted in GeV/cm^3)',
  r'$\rho_{\mathrm{crit}}/h_{100}^2 = 1.05368\times10^{-5}$ GeV/cm$^3$', 'STANDARD')
R('sigmaI1213', r'\sigma_{\mathrm{I12}},\ \sigma_{\mathrm{I13}}', [r'\sigma_{\mathrm{I12}}', r'\sigma_{\mathrm{I13}}'], r'The '
  r'spin-averaged annihilation cross-sections of a dark-matter pair through I12 (into gauge-boson pairs) and through I13 (into '
  r'quark pairs).', 'GeV^-2', status='DERIVED')
R('GI12', r'G_{\mathrm{I12}}', [r'G_{\mathrm{I12}}'], r'The combined coupling of I12 to all gauge-boson pairs, '
  r'$G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2$.', 'GeV^-3',
  r'benchmark $\pi/(2M_{\mathrm{DM}}^3) = 1.801\times10^{-14}$ GeV$^{-3}$', 'DERIVED')
R('Nc', r'N_{\mathrm{c}}', [r'N_{\mathrm{c}}'], r'The number of Weyl components of a fermion multiplet that share its zero-mode '
  r'profile and overlap (colour times isospin): 6 for a quark doublet, 3 for a quark singlet, 2 for a lepton doublet, 1 for a '
  r'charged-lepton singlet.', 'dimensionless', status='STANDARD')
R('Gf', r'G_f', [r'G_f'], r'The I13 coupling of the dark matter to the quark component $f$, '
  r'$G_f = G_{\mathrm{A}}q^B_f\tilde I^{(b)}_{of}$.', 'GeV^-2', status='DERIVED')
R('betacm', r'\beta_{\mathrm{cm}}', [r'\beta_{\mathrm{cm}}'], r'The velocity of each particle of the pair in the '
  r'centre-of-mass frame.', 'dimensionless', status='STANDARD')
R('kcm', r'k_{\mathrm{cm}}', [r'k_{\mathrm{cm}}'], r'The momentum of each particle of the pair in the centre-of-mass frame.',
  'GeV', status='STANDARD')

# ------------------------------------------------------------------ fold bands and right-handed neutrinos
R('Gammafi', r'\Gamma_{\mathrm{fi}}', [r'\Gamma_{\mathrm{fi}}'], r'The rate per volume of the production of fold-band pairs '
  r'from the plasma through I11 (freeze-in).', 'GeV^4', status='DERIVED')
R('Nfold', r'N_{\mathrm{fold}}', [r'N_{\mathrm{fold}}'], r'The number of fold bands: the massless fold zero modes of $\Psi_A$ and '
  r'of $\Psi_B$ (two Dirac fermions).', 'dimensionless', '2', 'DERIVED')
R('rhofold', r'\rho_{\mathrm{fold}}', [r'\rho_{\mathrm{fold}}'], r'The energy density of the fold bands.', 'GeV^4',
  status='DERIVED')
R('nfoldeq', r'n_{\mathrm{fold,eq}}', [r'n_{\mathrm{fold,eq}}'], r'The number density the fold bands would have in thermal '
  r'equilibrium.', 'GeV^3', status='DERIVED')
R('GABL', r'G_{\mathrm{A}}^{B-L}', [r'G_{\mathrm{A}}^{B-L}'], r'The strength I13 would need if it coupled to the $B - L$ current '
  r'(the same relic density).', 'GeV^-2', status='DERIVED')
R('SB', r'\mathcal{S}_B,\ \mathcal{S}_{B-L}', [r'\mathcal{S}_B', r'\mathcal{S}_{B-L}'], r'The colour-weighted sums of the '
  r'squared I13 overlaps of the dark matter with the baryon-number and with the $B - L$ charges.', 'dimensionless',
  r'$\mathcal{S}_B = 16.351$, $\mathcal{S}_{B-L} = 22.92$', 'DERIVED')
R('nnuR', r'n_{\nu_R},\ n_{\nu_R}^{\mathrm{eq}}', [r'n_{\nu_R}', r'n_{\nu_R}^{\mathrm{eq}}'], r'The number density of the '
  r'right-handed neutrinos (three generations) and its equilibrium value.', 'GeV^3', status='DERIVED')
R('Gammanu', r'\Gamma_\nu', [r'\Gamma_\nu'], r'The production rate per volume of right-handed neutrinos in the counterfactual '
  r'$B - L$ variant of I13.', 'GeV^4', status='DERIVED')
R('Gnu', r'G_\nu', [r'G_\nu'], r'The four-dimensional coupling of the dark matter to a right-handed neutrino in the $B - L$ '
  r'variant of I13.', 'GeV^-2', status='DERIVED')
R('Gammael', r'\Gamma_{\mathrm{el}},\ \sigma_{\mathrm{el}}', [r'\Gamma_{\mathrm{el}}', r'\sigma_{\mathrm{el}}'], r'The rate of '
  r'elastic scattering of a right-handed neutrino on the dark matter, and its cross-section.', 'GeV; GeV^-2',
  status='ESTIMATE')
R('NW', r'N_{\mathrm{W}}', [r'N_{\mathrm{W}}'], r'The number of Weyl species that decouple early.', 'dimensionless',
  status='DERIVED')
R('Fh', r'F_{\mathrm{h}}', [r'F_{\mathrm{h}}'], r'The correction factor of the early-decoupled radiation for the heating of the '
  r'neutrinos.', 'dimensionless', '1.0095', 'DERIVED')
R('hnu', r'h_\nu', [r'h_\nu'], r'The relative heating of the neutrinos by the electron-positron annihilation (beyond '
  r'instantaneous decoupling).', 'dimensionless', '0.00165', 'DERIVED')
R('rnuR', r'r_{\nu_R}', [r'r_{\nu_R}'], r'The ratio of the I11 production of right-handed neutrinos to the I13 annihilation rate '
  r'of the dark matter.', 'dimensionless', r'$2.0\times10^{-17}$', 'DERIVED')
R('abfold', r'a_{\mathrm{fold}},\ b_{\mathrm{fold}}', [r'a_{\mathrm{fold}}', r'b_{\mathrm{fold}}'], r'The upper and lower '
  r'components of a fold-band orbital ($b_{\mathrm{fold}} = 0$ for the even zero mode).', 'GeV^(1/2)', status='DERIVED')
R('nscDF', r'n^{\mathrm{sc}}_{\mathrm{DF}}', [r'n^{\mathrm{sc}}_{\mathrm{DF}}'], r'The transition scalar density between the '
  r'dark-matter orbital and a fold-band orbital.', 'GeV (normalised orbitals)', status='DERIVED')
R('Glam', r'G_\lambda', [r'G_\lambda'], r'The four-dimensional strength of the self-interaction channel of the dark matter into '
  r'fold-band pairs.', 'GeV^-2', r'$\le 2.3\times10^{-15}$ GeV$^{-2}$ (for $\Delta N_{\mathrm{eff}} \le 0.001$)', 'ESTIMATE')
R('Ilam', r'\tilde I_\lambda', [r'\tilde I_\lambda'], r'The overlap of the squared transition scalar density, '
  r'$\tilde I_\lambda = H^{-1}\int_{-L}^{0}(n^{\mathrm{sc}}_{\mathrm{DF}})^2\mathrm{e}^{-3Hy}\mathrm{d}y$.', 'dimensionless',
  '14.38', 'DERIVED')
R('sigmalam', r'\sigma_\lambda', [r'\sigma_\lambda'], r'The cross-section of the self-interaction channel (per final fold '
  r'species).', 'GeV^-2', status='ESTIMATE')
R('Gammalam', r'\Gamma_\lambda', [r'\Gamma_\lambda'], r'The rate per volume of the self-interaction channel.', 'GeV^4',
  status='ESTIMATE')
