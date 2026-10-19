from build_lib import R

# ------------------------------------------------------------------ the metric series and the linear perturbations
R('epsser', r'\epsilon', [r'\epsilon'], r'The bookkeeping parameter of the power series of the metric: the term of order $q$ is '
  r'multiplied by $\epsilon^q$ (the size of the first-order potentials).', 'dimensionless', r'$\epsilon \sim 10^{-5}$',
  'DERIVED')
R('h1', r'h^{(1)}_{MN},\ h^{(2)}_{MN}', [r'h^{(1)}', r'h^{(2)}'], r'The first- and second-order terms of the power series of '
  r'the metric.', 'dimensionless', status='DERIVED')
R('h1n', r'h^{(1,n)}_{MN}', [r'h^{(1,n)}'], r'The four-dimensional coefficient of the $n$-th $x_0$ profile $F_n$ in the '
  r'first-order term ($n = 0$: the flat zero mode, the perturbations of four-dimensional gravity; $n \ge 1$: the Kaluza-Klein '
  r'gravitons).', 'dimensionless', status='DERIVED')
R('hTT', r'h^{\mathrm{TT}}', [r'h^{\mathrm{TT}}'], r'The transverse-traceless (tensor) part of the first-order metric of '
  r'3-space (gravitational waves).', 'dimensionless', r'an input (tensor-to-scalar ratio below 0.036)', 'STANDARD')
R('PsiN', r'\Psi_{\mathrm{N}}', [r'\Psi_{\mathrm{N}}'], r'The curvature potential of the Newtonian gauge (the perturbation of '
  r'the 3-space metric, $1 - 2\Psi_{\mathrm{N}}$); not related to the field $\Psi$.', 'dimensionless',
  r'at most $2.4\times10^{-5}$', 'STANDARD')
R('Phi', r'\Phi', [r'\Phi'], r'The lapse potential of the Newtonian gauge (the perturbation of the time component, '
  r'$1 + 2\Phi$).', 'dimensionless', r'at most $2.4\times10^{-5}$', 'STANDARD')
R('sigmar', r'\sigma_{\mathrm{r}}', [r'\sigma_{\mathrm{r}}'], r'The radion perturbation: the first-order change of the block '
  r'scale, $f^2 \to f^2(1 + 2\sigma_{\mathrm{r}})$.', 'dimensionless', r'at most $1.1\times10^{-34}$ (static response)',
  'DERIVED')
R('tauc', r'\tau_{\mathrm{c}}', [r'\tau_{\mathrm{c}}'], r'The conformal time, $\mathrm{d}x_4 = \mathrm{e}^{a_4}\mathrm{d}\tau_{\mathrm{c}}$; '
  r'primes denote $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$.', 'length', status='STANDARD')
R('rhotot', r'\rho_{\mathrm{tot}},\ p_{\mathrm{tot}}', [r'\rho_{\mathrm{tot}}', r'p_{\mathrm{tot}}'], r'The total background '
  r'energy density and pressure of four-dimensional cosmology (all species).', 'GeV^4', status='STANDARD')
R('thetatot', r'\theta_{\mathrm{tot}}', [r'\theta_{\mathrm{tot}}'], r'The velocity divergence of the total matter, weighted '
  r'with $\rho + p$ of each species.', '1/length', status='STANDARD')
R('sigmaan', r'\sigma_{\mathrm{an}}', [r'\sigma_{\mathrm{an}}'], r'The anisotropic stress (shear) of the total matter (the '
  r'quantity $\sigma$ of Ma and Bertschinger), weighted with $\rho + p$.', 'dimensionless', status='STANDARD')
R('sigmaangamma', r'\sigma_{\mathrm{an},\gamma}', [r'\sigma_{\mathrm{an},\gamma}'], r'The anisotropic stress (shear) of the '
  r'photons, $F^\gamma_2/2$.', 'dimensionless', status='STANDARD')
R('deltaDM', r'\delta_{\mathrm{DM}},\ \theta_{\mathrm{DM}}', [r'\delta_{\mathrm{DM}}', r'\theta_{\mathrm{DM}}'], r'The density '
  r'contrast and the velocity divergence of the dark matter.', 'dimensionless; 1/length', status='STANDARD')
R('deltab', r'\delta_{\mathrm{b}},\ \theta_{\mathrm{b}}', [r'\delta_{\mathrm{b}}', r'\theta_{\mathrm{b}}'], r'The density '
  r'contrast and the velocity divergence of the baryons (nucleons and electrons).', 'dimensionless; 1/length',
  status='STANDARD')
R('deltagamma', r'\delta_\gamma,\ \theta_\gamma', [r'\delta_\gamma', r'\theta_\gamma'], r'The density contrast and the '
  r'velocity divergence of the photons.', 'dimensionless; 1/length', status='STANDARD')
R('cs', r'c_{\mathrm{s}}', [r'c_{\mathrm{s}}'], r'The sound speed of the baryon fluid.', 'dimensionless (c = 1)',
  status='STANDARD')
R('Rb', r'R_{\mathrm{b}}', [r'R_{\mathrm{b}}'], r'The photon-to-baryon momentum ratio of the Thomson drag, '
  r'$R_{\mathrm{b}} = 4\rho_\gamma/(3\rho_{\mathrm{b}})$.', 'dimensionless', status='STANDARD')
R('sigmaT', r'\sigma_{\mathrm{T}}', [r'\sigma_{\mathrm{T}}'], r'The Thomson cross-section.', 'GeV^-2',
  r'$6.6524587\times10^{-29}$ m$^2$', 'STANDARD')
R('rhogamma', r'\rho_\gamma', [r'\rho_\gamma'], r'The energy density of the photons, $\rho_\gamma = \pi^2T_\gamma^4/15$.',
  'GeV^4', status='STANDARD')
R('rhob', r'\rho_{\mathrm{b}}', [r'\rho_{\mathrm{b}}'], r'The energy density of the baryons.', 'GeV^4', status='STANDARD')
R('Fgamma', r'F^\gamma_l', [r'F^\gamma', r'F^\gamma_0', r'F^\gamma_1', r'F^\gamma_2'], r'The multipole $l$ of the photon '
  r'temperature perturbation (the brightness function of Ma and Bertschinger).', 'dimensionless', status='STANDARD')
R('Ggamma', r'G^\gamma_l', [r'G^\gamma', r'G^\gamma_0', r'G^\gamma_2'], r'The multipole $l$ of the photon polarisation '
  r'perturbation.', 'dimensionless', status='STANDARD')
R('calN', r'\mathcal{N}^{(i)}_l', [r'\mathcal{N}'], r'The multipole $l$ of the perturbation of the distribution of the neutrino '
  r'mass state $i$ (a function of $k$, $k_\nu$ and $\tau_{\mathrm{c}}$; the quantity $\Psi_l$ of Ma and Bertschinger).',
  'dimensionless', status='STANDARD')
R('knu', r'k_\nu', [r'k_\nu'], r'The comoving momentum of a neutrino (the physical momentum times $\mathrm{e}^{a_4}$).', 'GeV',
  status='STANDARD')
R('Ec', r'E^{\mathrm{c}}_i', [r'E^{\mathrm{c}}'], r'The comoving energy of a neutrino of the mass state $i$, '
  r'$E^{\mathrm{c}}_i = (k_\nu^2 + \mathrm{e}^{2a_4}m_i^2)^{1/2}$.', 'GeV', status='STANDARD')
R('fFD', r'f_{\mathrm{FD}}', [r'f_{\mathrm{FD}}'], r'The Fermi-Dirac distribution of the relic neutrinos, '
  r'$f_{\mathrm{FD}} = 1/(\mathrm{e}^{k/T_\nu} + 1)$.', 'dimensionless', status='STANDARD')
R('Tnu', r'T_\nu', [r'T_\nu'], r'The temperature of the relic neutrinos (one common temperature).', 'GeV',
  r'1.9454 K today', 'STANDARD')
R('Tgamma', r'T_\gamma', [r'T_\gamma'], r'The temperature of the photons (equal to the plasma temperature $T$; the subscript '
  r'is written where the neutrinos have their own temperature).', 'GeV', r'2.7255 K today', 'STANDARD')
R('PR', r'P_{\mathcal{R}}(k)', [r'P_{\mathcal{R}}'], r'The dimensionless power spectrum of the primordial curvature '
  r'perturbation $\mathcal{R}$.', 'dimensionless', status='STANDARD')
R('As', r'A_{\mathrm{s}}', [r'A_{\mathrm{s}}'], r'The amplitude of the primordial spectrum at $k_0$.', 'dimensionless',
  r'$2.099\times10^{-9}$ ($\ln(10^{10}A_{\mathrm{s}}) = 3.044$, Planck 2018)', 'STANDARD')
R('k0', r'k_0', [r'k_0'], r'The pivot wavenumber of the primordial spectrum.', '1/length', r'0.05 Mpc$^{-1}$', 'STANDARD')
R('ns', r'n_{\mathrm{s}}', [r'n_{\mathrm{s}}'], r'The spectral index of the primordial spectrum.', 'dimensionless',
  r'0.9649 (Planck 2018)', 'STANDARD')
R('Phirms', r'\Phi_{\mathrm{rms}}(k)', [r'\Phi_{\mathrm{rms}}'], r'The root-mean-square amplitude of the Weyl potential per '
  r'logarithmic interval of $k$.', 'dimensionless', r'$2.42\times10^{-5}$ at $k = 10^{-4}$ Mpc$^{-1}$', 'STANDARD')
R('PPhiW', r'P_{\Phi_{\mathrm{W}}}(k)', [r'P_{\Phi_{\mathrm{W}}}'], r'The power spectrum of the Weyl potential.', 'length^3',
  status='STANDARD')
R('PhiW', r'\Phi_{\mathrm{W}}', [r'\Phi_{\mathrm{W}}'], r'The Weyl potential, $\Phi_{\mathrm{W}} = (\Phi + \Psi_{\mathrm{N}})/2$ '
  r'(it deflects light).', 'dimensionless', status='STANDARD')
R('Omegam', r'\Omega_{\mathrm{m}}', [r'\Omega_{\mathrm{m}}'], r'The matter density today in units of the critical density.',
  'dimensionless', '0.3150', 'STANDARD')
R('deltam', r'\delta_{\mathrm{m}}', [r'\delta_{\mathrm{m}}'], r'The density contrast of the total matter (dark matter and '
  r'baryons).', 'dimensionless', status='STANDARD')
R('calR', r'\mathcal{R}', [r'\mathcal{R}'], r'The primordial comoving curvature perturbation.', 'dimensionless',
  status='STANDARD')
R('Dplus', r'D_+', [r'D_+'], r'The linear growth factor of the matter perturbations, normalised as $D_+ = \mathrm{e}^{a_4}$ '
  r'in the matter era.', 'dimensionless', r'$D_+\mathrm{e}^{-a_4} = 0.7878$ today', 'STANDARD')
R('sigma8', r'\sigma_8', [r'\sigma_8'], r'The root-mean-square linear matter fluctuation in spheres of radius $R_8$ today.',
  'dimensionless', '0.8118', 'DERIVED')
R('Pm', r'P_{\mathrm{m}}(k)', [r'P_{\mathrm{m}}'], r'The linear matter power spectrum today.', 'length^3', status='STANDARD')
R('Wth', r'W_{\mathrm{th}}', [r'W_{\mathrm{th}}'], r'The Fourier transform of a spherical top-hat window.', 'dimensionless',
  status='STANDARD')
R('R8', r'R_8', [r'R_8'], r'The radius of the spheres of $\sigma_8$, $R_8 = 8\,h_{100}^{-1}$ Mpc.', 'length', status='STANDARD')
R('h100', r'h_{100}', [r'h_{100}'], r'The reduced Hubble constant, $\mathcal{H}_0/(100$ km s$^{-1}$ Mpc$^{-1})$.',
  'dimensionless', '0.6738', 'STANDARD')
