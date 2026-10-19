from build_lib import E

E('FE', 'The metric as a power series of terms of decreasing magnitude', r'''
g_{MN} = \bar g_{MN} + \epsilon\,h^{(1)}_{MN} + \epsilon^2\,h^{(2)}_{MN} + \dots,\qquad
h^{(1)}_{MN}(X^\mu, x_0) = \sum_{n\ge0}h^{(1,n)}_{MN}(X^\mu)\,F_n(x_0),\qquad \epsilon \sim 10^{-5}''', 'DERIVED',
  ['metric g'],
  'Order 0 exact; order 1, n = 0 by the linear Einstein-Boltzmann equations ([[pert_einstein]] to [[pert_nu]]; potentials '
  '2.4e-5 and smaller); n >= 1 by the graviton tower [[kk_tower]] (range below 1.6e-21 m); order 2 estimated (5.8e-10).',
  name='series')

E('FE', r'The order-1, $n = 0$ term of the metric in the Newtonian gauge (eight dimensions)', r'''
\begin{aligned}
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N ={}& \mathrm{e}^{2a_4}\Big[\big(1 - 2\Psi_{\mathrm{N}}\big)\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2
 + \mathrm{d}x_3^2\big) + \mathrm{d}\vec x\cdot h^{\mathrm{TT}}\cdot\mathrm{d}\vec x\Big] - \big(1 + 2\Phi\big)\,\mathrm{d}x_4^2\\
 &+ f^2\big(1 + 2\sigma_{\mathrm{r}}\big)\Big[\mathrm{d}y^2 - \mathrm{e}^{2Hy}\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
\end{aligned}''', 'DERIVED', ['metric g'],
  'The potentials, the tensor and the radion are of order epsilon; the radion is massive (48.42 TeV) and its static response '
  'is at most 1.1e-34; the tensor amplitude is an input (bounded, r < 0.036).', name='newton8')

E('FE', 'The four-dimensional perturbed metric in conformal time', r'''
g^{(4)}_{\mu\nu}\,\mathrm{d}X^\mu\mathrm{d}X^\nu = \mathrm{e}^{2a_4}\Big[-\big(1 + 2\Phi\big)\,\mathrm{d}\tau_{\mathrm{c}}^2
 + \big(1 - 2\Psi_{\mathrm{N}}\big)\,\mathrm{d}\vec x^{\,2}\Big],\qquad \mathrm{d}x_4 = \mathrm{e}^{a_4}\,\mathrm{d}\tau_{\mathrm{c}}''',
  'STANDARD', ['four-dimensional metric'],
  'Newtonian gauge (Ma and Bertschinger); the prime denotes d/d tau_c and a_4\' is the conformal expansion rate.', name='newton4')

E('FE', 'The linearised Einstein equations for a Fourier mode', r'''
\begin{aligned}
&k^2\Psi_{\mathrm{N}} + 3a_4'\big(\Psi_{\mathrm{N}}' + a_4'\Phi\big) = -4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\,\Delta\rho,\qquad
 k^2\big(\Psi_{\mathrm{N}}' + a_4'\Phi\big) = 4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\big(\rho_{\mathrm{tot}} + p_{\mathrm{tot}}\big)\theta_{\mathrm{tot}},\\
&\Psi_{\mathrm{N}}'' + a_4'\big(\Phi' + 2\Psi_{\mathrm{N}}'\big) + \big(2a_4'' + a_4'^2\big)\Phi + \frac{k^2}{3}\big(\Psi_{\mathrm{N}} - \Phi\big)
 = 4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\,\Delta p,\\
&k^2\big(\Psi_{\mathrm{N}} - \Phi\big) = 12\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\big(\rho_{\mathrm{tot}} + p_{\mathrm{tot}}\big)\sigma_{\mathrm{an}}
\end{aligned}''', 'STANDARD', ['four-dimensional metric', 'all species'],
  'Solved numerically with CAMB 2.0.5 (default accuracy, lensing) at the Planck 2018 parameters, summed over the species of '
  'UM-2; TT and EE agree with Planck LambdaCDM to 2.5e-4 and 2.7e-4.', name='pert_einstein')

E('FE', 'The perturbations of the dark matter (cold)', r'''
\delta_{\mathrm{DM}}' = -\theta_{\mathrm{DM}} + 3\Psi_{\mathrm{N}}',\qquad \theta_{\mathrm{DM}}' = -a_4'\,\theta_{\mathrm{DM}} + k^2\Phi''',
  'STANDARD', ['dark matter (the odd quanta of Psi_A and Psi_B)'],
  'Solved with CAMB; the dark matter is cold (w = 0 for quanta at rest, Kohn-Sham).', name='pert_dm')

E('FE', 'The perturbations of the baryons', r'''
\delta_{\mathrm{b}}' = -\theta_{\mathrm{b}} + 3\Psi_{\mathrm{N}}',\qquad
\theta_{\mathrm{b}}' = -a_4'\,\theta_{\mathrm{b}} + c_{\mathrm{s}}^2k^2\delta_{\mathrm{b}}
 + R_{\mathrm{b}}\,\mathrm{e}^{a_4}n_{\mathrm{e}}\sigma_{\mathrm{T}}\big(\theta_\gamma - \theta_{\mathrm{b}}\big) + k^2\Phi,\qquad
R_{\mathrm{b}} = \frac{4\rho_\gamma}{3\rho_{\mathrm{b}}}''', 'STANDARD', ['baryons (protons, neutrons, electrons)', 'photons'],
  'Solved with CAMB (recombination and Thomson drag of the standard code).', name='pert_baryon')

E('FE', 'The perturbations of the photons: density and velocity', r'''
\delta_\gamma' = -\frac43\,\theta_\gamma + 4\Psi_{\mathrm{N}}',\qquad
\theta_\gamma' = k^2\Big(\frac14\,\delta_\gamma - \sigma_{\mathrm{an},\gamma}\Big) + k^2\Phi
 + \mathrm{e}^{a_4}n_{\mathrm{e}}\sigma_{\mathrm{T}}\big(\theta_{\mathrm{b}} - \theta_\gamma\big)''', 'STANDARD', ['photons', 'baryons'],
  'Solved with CAMB.', name='pert_photon')

E('FE', 'The photon temperature hierarchy', r'''
\begin{aligned}
&F^\gamma_l{}' = \frac{k}{2l + 1}\big[l\,F^\gamma_{l-1} - (l + 1)F^\gamma_{l+1}\big]
 - \mathrm{e}^{a_4}n_{\mathrm{e}}\sigma_{\mathrm{T}}\Big[F^\gamma_l - \frac{\delta_{l2}}{10}\big(F^\gamma_2 + G^\gamma_0 + G^\gamma_2\big)\Big]
 \quad (l \ge 2),\\
&F^\gamma_0 = \delta_\gamma,\qquad F^\gamma_1 = \frac{4\theta_\gamma}{3k},\qquad F^\gamma_2 = 2\sigma_{\mathrm{an},\gamma}
\end{aligned}''', 'STANDARD', ['photons'],
  'Solved with CAMB (the l = 2 equation equals the separate quadrupole equation of Ma and Bertschinger).', name='pert_photon_hier')

E('FE', 'The photon polarisation hierarchy', r'''
G^\gamma_l{}' = \frac{k}{2l + 1}\big[l\,G^\gamma_{l-1} - (l + 1)G^\gamma_{l+1}\big]
 + \mathrm{e}^{a_4}n_{\mathrm{e}}\sigma_{\mathrm{T}}\Big[-G^\gamma_l + \frac12\big(F^\gamma_2 + G^\gamma_0 + G^\gamma_2\big)
 \Big(\delta_{l0} + \frac{\delta_{l2}}{5}\Big)\Big]''', 'STANDARD', ['photons'], 'Solved with CAMB.', name='pert_pol')

E('FE', 'The hierarchy of each neutrino mass state (the cosmic neutrino background)', r'''
\begin{aligned}
&\mathcal{N}^{(i)\prime}_0 = -\frac{k_\nu k}{E^{\mathrm{c}}_i}\,\mathcal{N}^{(i)}_1
 - \Psi_{\mathrm{N}}'\,\frac{\mathrm{d}\ln f_{\mathrm{FD}}}{\mathrm{d}\ln k_\nu},\qquad
 \mathcal{N}^{(i)\prime}_1 = \frac{k_\nu k}{3E^{\mathrm{c}}_i}\big(\mathcal{N}^{(i)}_0 - 2\mathcal{N}^{(i)}_2\big)
 - \frac{E^{\mathrm{c}}_ik}{3k_\nu}\,\Phi\,\frac{\mathrm{d}\ln f_{\mathrm{FD}}}{\mathrm{d}\ln k_\nu},\\
&\mathcal{N}^{(i)\prime}_l = \frac{k_\nu k}{(2l + 1)E^{\mathrm{c}}_i}\big[l\,\mathcal{N}^{(i)}_{l-1} - (l + 1)\mathcal{N}^{(i)}_{l+1}\big]
 \quad (l \ge 2),\qquad E^{\mathrm{c}}_i = \sqrt{k_\nu^2 + \mathrm{e}^{2a_4}m_i^2}
\end{aligned}''', 'STANDARD', ['neutrino mass states nu_1, nu_2, nu_3', 'fold bands (massless limit)'],
  'Solved with CAMB, each mass state separately with the degeneracy N_eff/3 = 1.0144 (masses iterated to 7.8e-12); the fold '
  'bands produced by freeze-in obey the massless limit E^c_i = k_nu.', name='pert_nu')

E('FE', 'The background expansion, the neutrino temperature and the primordial spectrum', r'''
a_4'^2 = \frac{8\pi G_{\mathrm{N}}}{3}\,\mathrm{e}^{2a_4}\rho_{\mathrm{tot}} + \frac{\Lambda_4}{3}\,\mathrm{e}^{2a_4},\qquad
T_\nu = \Big(\frac{4}{11}\Big)^{1/3}T_\gamma,\qquad
P_{\mathcal{R}}(k) = A_{\mathrm{s}}\Big(\frac{k}{k_0}\Big)^{n_{\mathrm{s}} - 1}''', 'STANDARD', ['four-dimensional metric', 'all species'],
  'Inputs: the Planck 2018 primordial parameters; N_eff = 3.0432 (neutrinos) + 0.0010 (freeze-in fold bands) = 3.0442; '
  'H_0 = 67.38 km/s/Mpc, r_drag = 147.10 Mpc, BAO chi^2 = 31.5 for 13 DESI DR2 points.', name='pert_bg')

E('FE', 'The size of the first-order potentials: rms value, Poisson equation and large scales', r'''
\begin{aligned}
&\Phi_{\mathrm{rms}}(k) = \Big[\frac{k^3P_{\Phi_{\mathrm{W}}}(k)}{2\pi^2}\Big]^{1/2},\qquad
 \Phi_{\mathrm{W}} = \frac{\Phi + \Psi_{\mathrm{N}}}{2},\qquad
 \Phi_{\mathrm{W}} = \frac32\,\Omega_{\mathrm{m}}\mathcal{H}_0^2\,\frac{\delta_{\mathrm{m}}}{\mathrm{e}^{a_4}k^2}\ \ \text{(inside the horizon)},\\
&\Phi_{\mathrm{W}} = \frac35\,\mathcal{R}\,\mathrm{e}^{-a_4}D_+\ \ \text{(largest scales)},\qquad
 D_+ = \frac52\,\Omega_{\mathrm{m}}\,\frac{\mathcal{H}}{\mathcal{H}_0}\int_{-\infty}^{a_4}\Big(\frac{\mathcal{H}_0}{\mathcal{H}}\Big)^3
 \mathrm{e}^{-2\tilde a_4}\,\mathrm{d}\tilde a_4,\\
&\frac{\mathcal{H}}{\mathcal{H}_0} = \big(\Omega_{\mathrm{m}}\mathrm{e}^{-3a_4} + 1 - \Omega_{\mathrm{m}}\big)^{1/2}
\end{aligned}''', 'STANDARD', ['four-dimensional metric', 'matter'],
  'From the CAMB solution: 2.42e-5 at k = 1e-4/Mpc down to 5.03e-8 at 1/Mpc; the Poisson form agrees to 1.5e-6 for '
  'k >= 0.01/Mpc and the large-scale form to 4.4e-5 (D_+ e^{-a4} = 0.7878 today); inside the integral H is evaluated at '
  'a4 = a4 tilde.', name='phi_rms')

E('FE', 'The amplitude of the matter fluctuations', r'''
\sigma_8^2 = \int_0^\infty\frac{\mathrm{d}k}{k}\,\frac{k^3P_{\mathrm{m}}(k)}{2\pi^2}\,W_{\mathrm{th}}(kR_8)^2,\qquad
W_{\mathrm{th}}(kR_8) = \frac{3\big[\sin(kR_8) - kR_8\cos(kR_8)\big]}{(kR_8)^3},\qquad R_8 = 8\,h_{100}^{-1}\,\text{Mpc}''',
  'STANDARD', ['matter'],
  'Computed from the CAMB linear matter power spectrum: 0.8118 for UM-2 against 0.8109 for LambdaCDM.', name='sigma8')
