from build_lib import E

E('FE', 'The three neutrino masses', r'''
m_1 = 1.000\ \text{meV},\qquad m_2 = \sqrt{m_1^2 + \Delta m_{21}^2} = 8.712\ \text{meV},\qquad
m_3 = \sqrt{m_1^2 + \Delta m_{31}^2} = 50.140\ \text{meV}''', 'ASSUMED', ['neutrinos'],
  'm_1 and the normal ordering ASSUMED, the splittings STANDARD (NuFIT 6.0); they are x0 eigenvalues of [[ferm_1gen]] with '
  'c_R = -35.0452, -32.8481, -31.0702.', name='nu_masses')

E('FE', 'The four-fermion interactions at low energy', r'''
\begin{aligned}
&\mathcal{L}_{\mathrm{CC}} = -2\sqrt2\,G_{\mathrm{F}}\big(\bar\nu_\alpha\gamma^\mu P_L\,\ell^-_\alpha\big)
 \big(\bar\ell^-_\beta\gamma_\mu P_L\,\nu_\beta\big),\qquad
 \mathcal{L}_{\mathrm{NC}} = -2\sqrt2\,G_{\mathrm{F}}\big(\bar\nu_\alpha\gamma^\mu P_L\,\nu_\alpha\big)
 \sum_f\bar\psi_f\gamma_\mu\big(\tilde g^f_LP_L + \tilde g^f_RP_R\big)\psi_f,\\
&\nu_\alpha = \sum_{i=1}^{3}U_{\alpha i}\,\nu_i,\qquad P_L = \frac{1 + \Gamma_4}{2},\qquad P_R = \frac{1 - \Gamma_4}{2}
\end{aligned}''', 'STANDARD', ['neutrinos', 'charged leptons', 'medium fermions'],
  'The exchange of W+, W- and Z between zero modes far below m_W, m_Z; summed over the flavours alpha, beta and the fermions '
  'f of the medium.', name='fourfermion')

E('FE', 'The Fermi constant and the neutral-current couplings', r'''
\frac{G_{\mathrm{F}}}{\sqrt2} = \frac{g_2^2}{8m_{\mathrm{W}}^2},\qquad
\tilde g^f_L = T_3^f - Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}},\qquad \tilde g^f_R = -Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}},\qquad
\tilde g^f_V = \tilde g^f_L + \tilde g^f_R = T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}}''', 'STANDARD',
  ['W', 'Z', 'fermions'],
  'UM-2 uses the measured G_F = 1.1663788e-5 GeV^-2.', name='gf')

E('FE', 'The matter potentials of forward scattering', r'''
\begin{aligned}
&V_\alpha = \sqrt2\,G_{\mathrm{F}}\Big[\delta_{\alpha e}\big(n_{e^-} - n_{e^+}\big) + \sum_f\tilde g^f_V\big(n_f - n_{\bar f}\big)\Big],\\
&V = \mathrm{diag}\big(V_{\mathrm{CC}},\ 0,\ 0\big) + V_{\mathrm{NC}}\,\mathbf{1},\qquad V_{\mathrm{CC}} = \sqrt2\,G_{\mathrm{F}}\,n_{\mathrm{e}},
 \qquad V_{\mathrm{NC}} = -\frac{G_{\mathrm{F}}\,n_{\mathrm{n}}}{\sqrt2}
\end{aligned}''', 'STANDARD', ['neutrinos', 'electrons', 'neutrons'],
  'For an unpolarised medium at rest; in neutral matter of electrons, protons and neutrons; antineutrinos have -V.',
  name='potentials')

E('FE', 'The flavour evolution in vacuum and in matter', r'''
\mathrm{i}\,\frac{\mathrm{d}\boldsymbol{\psi}}{\mathrm{d}x_4} = H_{\mathrm{fl}}\,\boldsymbol{\psi},\qquad
H_{\mathrm{fl}} = \frac{1}{2E}\,U\,\mathrm{diag}\big(m_1^2,\ m_2^2,\ m_3^2\big)\,U^\dagger + V,\qquad
\mathcal{U}(L_{\mathrm{b}}) = \mathrm{e}^{-\mathrm{i}H_{\mathrm{fl}}L_{\mathrm{b}}},\qquad
\mathcal{P}(\nu_\alpha\to\nu_\beta) = \lvert\mathcal{U}_{\beta\alpha}\rvert^2''', 'STANDARD', ['neutrinos'],
  'Solved exactly (matrix exponential for constant density, ordered products of layers otherwise); vacuum formula reproduced to '
  '3.9e-15, unitarity 1.8e-15; antineutrinos: U -> U*, V -> -V.', name='flavour_ham')

E('FE', 'The vacuum oscillation probability, CPT and the T-odd difference', r'''
\begin{aligned}
&\mathcal{P}(\nu_\alpha\to\nu_\beta) = \Big\lvert\sum_{i=1}^{3}U_{\beta i}U^*_{\alpha i}\,
 \mathrm{e}^{-\mathrm{i}m_i^2L_{\mathrm{b}}/(2E)}\Big\rvert^2,\qquad
 \mathcal{P}(\nu_\alpha\to\nu_\beta) = \mathcal{P}(\bar\nu_\beta\to\bar\nu_\alpha),\\
&\mathcal{P}(\nu_\mu\to\nu_e) - \mathcal{P}(\nu_e\to\nu_\mu) = -16J_{\mathrm{CP}}\sin\Delta_{21}\sin\Delta_{31}\sin\Delta_{32},\qquad
 \Delta_{ij} = \frac{\Delta m_{ij}^2L_{\mathrm{b}}}{4E},\qquad
 J_{\mathrm{CP}} = \mathrm{Im}\big(U_{e2}U_{\mu3}U_{e3}^*U_{\mu2}^*\big)
\end{aligned}''', 'STANDARD', ['neutrinos'],
  'Checked against the exact evolution (CPT to 2.8e-16, T-odd difference to 5.9e-14).', name='vacuum_prob')

E('FE', 'The MSW resonances of the 1-3 and 1-2 sectors', r'''
2E\,V_{\mathrm{CC}} = \Delta m_{ee}^2\cos2\theta_{13},\qquad \Delta m_{ee}^2 = c_{12}^2\,\Delta m_{31}^2 + s_{12}^2\,\Delta m_{32}^2,
\qquad 2E\,V_{\mathrm{CC}}\,c_{13}^2 = \Delta m_{21}^2\cos2\theta_{12}''', 'STANDARD', ['neutrinos', 'electrons'],
  'The 1-3 resonance at 11.135 GeV in rock of 2.8 g/cm^3 (exact three-flavour 11.133 GeV); the 1-2 resonance at the centre of '
  'the Sun at 1.93 MeV.', name='msw')

E('FE', 'The adiabatic survival probability of solar electron neutrinos', r'''
\begin{aligned}
&\mathcal{P}_{ee} = c_{13}^4\Big(\frac12 + \frac12\cos2\theta_{12}\cos2\theta^{\mathrm{m}}_{12}\Big) + s_{13}^4,\qquad
 A_{\mathrm{MSW}} = \frac{2E\,V_{\mathrm{CC}}\,c_{13}^2}{\Delta m_{21}^2},\\
&\cos2\theta^{\mathrm{m}}_{12} = \frac{\cos2\theta_{12} - A_{\mathrm{MSW}}}{\sqrt{\big(\cos2\theta_{12} - A_{\mathrm{MSW}}\big)^2
 + \sin^22\theta_{12}}}
\end{aligned}''', 'STANDARD',
  ['neutrinos', 'electrons'],
  'Evaluated at the production point; the numerical three-flavour evolution through the solar density agrees to 1.3e-3.',
  name='pee')

E('FE', 'The resonance density, the adiabaticity and the Landau-Zener jump probability', r'''
n_{\mathrm{e}}^{\mathrm{res}} = \frac{\Delta m_{ij}^2\cos2\theta_{ij}}{2\sqrt2\,G_{\mathrm{F}}E},\qquad
\gamma_{\mathrm{ad}} = \frac{\Delta m_{ij}^2\sin^22\theta_{ij}}{2E\cos2\theta_{ij}\,\lvert\mathrm{d}\ln n_{\mathrm{e}}/\mathrm{d}r\rvert} \gg 1,
\qquad \mathcal{P}_{\mathrm{LZ}} = \mathrm{e}^{-\pi\gamma_{\mathrm{ad}}/2}''', 'STANDARD', ['neutrinos', 'electrons'],
  'Two-flavour conditions; in the supernova envelope both resonances are adiabatic (P_LZ <= 2.6e-77).', name='adiabaticity')

E('FE', 'The thermal potential of the early Universe', r'''
V_e - V_\mu = -\frac{8\sqrt2\,G_{\mathrm{F}}\lvert\vec k\rvert}{3m_{\mathrm{W}}^2}\,\rho_{\mathrm{e}},\qquad
\rho_{\mathrm{e}} \simeq \frac{7\pi^2}{60}\,T^4\ \ (T \gg m_{\mathrm{e}})''', 'STANDARD', ['neutrinos', 'electrons and positrons'],
  'Leading order in T/m_W; it falls below the vacuum term at T = 4.99 MeV (atmospheric) and 2.39 MeV (solar) for k = 3.15 T.',
  name='thermal_pot')

E('FE', 'The quantum kinetic equations of a neutrino gas', r'''
\begin{aligned}
&\mathrm{i}\Big(\partial_{x_4} + \frac{\vec k}{\lvert\vec k\rvert}\cdot\vec\nabla\Big)\boldsymbol{\rho}_{\vec k}
 = \big[H^{\mathrm{vac}}_{\vec k} + V + V_{\nu\nu},\ \boldsymbol{\rho}_{\vec k}\big] + \mathrm{i}\,C_{\mathrm{coll}}[\boldsymbol{\rho}],
 \qquad H^{\mathrm{vac}}_{\vec k} = \frac{U\,\mathrm{diag}\big(m_1^2,\ m_2^2,\ m_3^2\big)\,U^\dagger}{2\lvert\vec k\rvert},\\
&V_{\nu\nu} = \sqrt2\,G_{\mathrm{F}}\int\frac{\mathrm{d}^3\vec k_2}{(2\pi)^3}\Big(1 - \frac{\vec k\cdot\vec k_2}{\lvert\vec k\rvert\lvert\vec k_2\rvert}\Big)
 \big(\boldsymbol{\rho}_{\vec k_2} - \bar{\boldsymbol{\rho}}_{\vec k_2}\big),\qquad
 \partial_{x_4} \to \partial_{x_4} - \mathcal{H}\lvert\vec k\rvert\,\partial_{\lvert\vec k\rvert}\ \ \text{(expanding Universe)}
\end{aligned}''', 'STANDARD', ['neutrinos'],
  'Used in its linearised form for the fast flavour instability ([[ffi_disp]]) and, momentum averaged, for neutrino decoupling '
  '([[decoupling]]).', name='qke')

E('FE', 'Neutrino decoupling: the temperature equations', r'''
\begin{aligned}
\frac{\mathrm{d}T_\gamma}{\mathrm{d}x_4} &= -\frac{4\mathcal{H}\rho_\gamma + 3\mathcal{H}\big(\rho_{\mathrm{e}} + p_{\mathrm{e}}\big)
 + 3\mathcal{H}T_\gamma\,\frac{\mathrm{d}p_{\mathrm{QED}}}{\mathrm{d}T_\gamma} + C_{\nu_e} + 2C_{\nu_\mu}}
 {\frac{\mathrm{d}\rho_\gamma}{\mathrm{d}T_\gamma} + \frac{\mathrm{d}\rho_{\mathrm{e}}}{\mathrm{d}T_\gamma}
 + T_\gamma\,\frac{\mathrm{d}^2p_{\mathrm{QED}}}{\mathrm{d}T_\gamma^2}},\qquad
 \frac{\mathrm{d}T_{\nu_\alpha}}{\mathrm{d}x_4} = -\mathcal{H}T_{\nu_\alpha} + \frac{C_{\nu_\alpha}}{\mathrm{d}\rho_{\nu_\alpha}/\mathrm{d}T_{\nu_\alpha}},\\
\mathcal{H} &= \frac{\sqrt{8\pi\rho_{\mathrm{tot}}/3}}{M_{\mathrm{Pl}}},\qquad \rho_\gamma = \frac{\pi^2}{15}\,T_\gamma^4,\qquad
 \rho_{\nu_\alpha} = \frac{7\pi^2}{120}\,T_{\nu_\alpha}^4
\end{aligned}''', 'STANDARD', ['photons', 'electrons and positrons', 'neutrinos'],
  'Integrated from 20 MeV to 5 keV (LSODA, relative tolerance 1e-11); the method reproduces the published values (Escudero '
  '2020) to 1e-3; nu_tau follows nu_mu.', name='decoupling')

E('FE', 'The energy transfer by collisions', r'''
\begin{aligned}
&C_{\nu_e} = \frac{G_{\mathrm{F}}^2}{\pi^5}\Big[4\Big(\big(\tilde g^{\nu_e e}_L\big)^2 + \big(\tilde g^{\nu_e e}_R\big)^2\Big)
 \mathcal{F}_{\mathrm{tr}}(T_\gamma, T_{\nu_e}) + 2\mathcal{F}_{\mathrm{tr}}(T_{\nu_\mu}, T_{\nu_e})\Big],\\
&C_{\nu_\mu} = \frac{G_{\mathrm{F}}^2}{\pi^5}\Big[4\Big(\big(\tilde g^{\nu_\mu e}_L\big)^2 + \big(\tilde g^{\nu_\mu e}_R\big)^2\Big)
 \mathcal{F}_{\mathrm{tr}}(T_\gamma, T_{\nu_\mu}) - \mathcal{F}_{\mathrm{tr}}(T_{\nu_\mu}, T_{\nu_e})\Big],\\
&\mathcal{F}_{\mathrm{tr}}(T_{\mathrm{A}}, T_{\mathrm{B}}) = 32f_{\mathrm{a}}\big(T_{\mathrm{A}}^9 - T_{\mathrm{B}}^9\big)
 + 56f_{\mathrm{s}}T_{\mathrm{A}}^4T_{\mathrm{B}}^4\big(T_{\mathrm{A}} - T_{\mathrm{B}}\big),\\
&\tilde g^{\nu_e e}_L = \frac12 + \sin^2\theta_{\mathrm{W}},\qquad \tilde g^{\nu_e e}_R = \tilde g^{\nu_\mu e}_R = \sin^2\theta_{\mathrm{W}},
 \qquad \tilde g^{\nu_\mu e}_L = -\frac12 + \sin^2\theta_{\mathrm{W}}
\end{aligned}''', 'STANDARD', ['neutrinos', 'electrons and positrons'],
  'f_a = 0.884, f_s = 0.829; the radiatively corrected couplings 0.727, 0.233, -0.273, 0.233 are used (the tree-level ones '
  'change N_eff by 4e-4).', name='transfer')

E('FE', 'The finite-temperature QED pressure of the electron-photon plasma', r'''
\begin{aligned}
&p_{\mathrm{QED}} = p_{\mathrm{QED}}^{(2)} + p_{\mathrm{QED}}^{(3)},\qquad
 p_{\mathrm{QED}}^{(2)} = -\frac{e^2T^2}{12\pi^2}\,\mathcal{Q}_1 - \frac{e^2}{8\pi^4}\,\mathcal{Q}_1^2
 + \frac{e^2m_{\mathrm{e}}^2}{16\pi^4}\,\mathcal{Q}_2,\\
&p_{\mathrm{QED}}^{(3)} = \frac{e^3T}{12\pi^4}\,\mathcal{Q}_3^{3/2},\qquad
 \rho_{\mathrm{QED}} = -p_{\mathrm{QED}} + T\,\frac{\mathrm{d}p_{\mathrm{QED}}}{\mathrm{d}T}
\end{aligned}''', 'STANDARD',
  ['photons', 'electrons and positrons'],
  'Massless limits -5e^2T^4/288 and e^3T^4/(36 sqrt3 pi) reproduced to 1e-16 (Bennett et al. 2020).', name='qed_pressure')

E('FE', 'The integrals of the QED pressure', r'''
\begin{aligned}
&\mathcal{Q}_1 = \int_0^\infty\mathrm{d}k\,\frac{k^2}{E}\,n_{\mathrm{D}}(k),\qquad
 \mathcal{Q}_2 = \int_0^\infty\!\!\int_0^\infty\mathrm{d}k\,\mathrm{d}k_2\,\frac{kk_2}{E(k)E(k_2)}
 \ln\Big\lvert\frac{k + k_2}{k - k_2}\Big\rvert\,n_{\mathrm{D}}(k)\,n_{\mathrm{D}}(k_2),\\
&\mathcal{Q}_3 = \int_0^\infty\mathrm{d}k\,\frac{k^2 + E^2}{E}\,n_{\mathrm{D}}(k),\qquad
 n_{\mathrm{D}}(k) = \frac{2}{\mathrm{e}^{E/T} + 1},\qquad E = \sqrt{k^2 + m_{\mathrm{e}}^2}
\end{aligned}''', 'STANDARD', ['electrons and positrons'],
  'Gauss-Legendre panels; the logarithmic singularity at k_2 = k removed by a substitution.', name='qed_integrals')

E('FE', 'The effective number of neutrino species and the common temperature', r'''
N_{\mathrm{eff}} = \Big(\frac{11}{4}\Big)^{4/3}\Big[\Big(\frac{T_{\nu_e}}{T_\gamma}\Big)^4 + 2\Big(\frac{T_{\nu_\mu}}{T_\gamma}\Big)^4\Big],
\qquad \frac{\mathrm{d}T_\nu}{\mathrm{d}x_4} = -\mathcal{H}T_\nu + \frac{C_{\nu_e} + 2C_{\nu_\mu}}{3\,\mathrm{d}\rho_\nu/\mathrm{d}T_\nu}''',
  'STANDARD', ['neutrinos', 'photons'],
  'UM-2 computes 3.0476 (separate temperatures) and 3.0485 (one common temperature, efficient oscillations) and adopts the '
  'precision value 3.0432 (Cielo et al. 2023); for instantaneous decoupling the plasma entropy per comoving volume is conserved '
  'and T_nu falls as e^{-a4}.', name='neff')

E('FE', 'The fast flavour instability: the electron-lepton-number distribution', r'''
G_{\mathrm{ELN}}(u) = \sqrt2\,G_{\mathrm{F}}\big[n_{\nu_e}\,g_{\nu_e}(u) - n_{\bar\nu_e}\,g_{\bar\nu_e}(u)\big],\qquad
\int_{-1}^{1}g_{\nu_e}\,\frac{\mathrm{d}u}{2} = \int_{-1}^{1}g_{\bar\nu_e}\,\frac{\mathrm{d}u}{2} = 1,\qquad
\mathcal{I}_l = \int_{-1}^{1}\frac{\mathrm{d}u}{2}\,G_{\mathrm{ELN}}(u)\,u^l''', 'STANDARD', ['neutrinos (dense gas)'],
  'Homogeneous, axially symmetric gas of electron neutrinos and antineutrinos (symmetry axis x3).', name='ffi_eln')

E('FE', 'The fast flavour instability: the dispersion relation', r'''
\begin{aligned}
&\mathcal{C}(u) \propto \mathrm{e}^{-\mathrm{i}(\omega_{\mathrm{f}}x_4 - k_{\mathrm{f}}x_3)},\qquad \bar\omega = \omega_{\mathrm{f}} - \mathcal{I}_0,
 \qquad \bar k = k_{\mathrm{f}} - \mathcal{I}_1:\qquad \det\Pi(\bar\omega, \bar k) = 0,\\
&\Pi = \mathrm{diag}(1,\ -1) + \int_{-1}^{1}\frac{\mathrm{d}u}{2}\,\frac{G_{\mathrm{ELN}}(u)}{\bar\omega - \bar ku}
 \begin{pmatrix}1 & u\\ u & u^2\end{pmatrix}
\end{aligned}''', 'STANDARD', ['neutrinos (dense gas)'],
  'Roots found for real k on a grid by vectorised Newton iterations; three independent evaluations agree to 1.2e-14.',
  name='ffi_disp')

E('FE', 'The axisymmetric and azimuthal branches of the dispersion relation', r'''
\big(1 + \mathcal{J}_0\big)\big(-1 + \mathcal{J}_2\big) - \mathcal{J}_1^2 = 0,\qquad
\mathcal{J}_l = \int_{-1}^{1}\frac{\mathrm{d}u}{2}\,\frac{G_{\mathrm{ELN}}(u)\,u^l}{\bar\omega - \bar ku};\qquad
-1 + \int_{-1}^{1}\frac{\mathrm{d}u}{2}\,\frac{G_{\mathrm{ELN}}(u)\,(1 - u^2)}{2(\bar\omega - \bar ku)} = 0''', 'STANDARD',
  ['neutrinos (dense gas)'],
  'A root with Im omega_bar > 0 for real k_bar is an instability; with an ELN crossing the largest growth rate is 0.088 mu_nunu, '
  'without one no mode grows (Morinaga 2022).', name='ffi_branches')

E('FE', r'The homogeneous mode and the mode $k_{\mathrm{f}} = \mathcal{I}_1$', r'''
\begin{aligned}
&\mathrm{i}\,\frac{\mathrm{d}\mathcal{C}(u)}{\mathrm{d}x_4} = \big(\mathcal{I}_0 - u\,\mathcal{I}_1\big)\mathcal{C}(u)
 - \int_{-1}^{1}\frac{\mathrm{d}\tilde u}{2}\,G_{\mathrm{ELN}}(\tilde u)\,(1 - u\tilde u)\,\mathcal{C}(\tilde u);\\
&\bar\omega^2 - \big(\mathcal{I}_2 - \mathcal{I}_0\big)\bar\omega - \big(\mathcal{I}_0\mathcal{I}_2 - \mathcal{I}_1^2\big) = 0,\qquad
 \mathrm{Im}\,\bar\omega = \frac12\sqrt{4\mathcal{I}_1^2 - \big(\mathcal{I}_0 + \mathcal{I}_2\big)^2}
\end{aligned}''', 'STANDARD',
  ['neutrinos (dense gas)'],
  'Eigenvalues of the discretised homogeneous equation (300 nodes) agree with the dispersion relation; growth by e in '
  '6e-10 to 6e-11 s near the neutrinosphere (mu_nunu = sqrt2 G_F n_nue).', name='ffi_homog')

E('FE', 'The cosmic neutrino background', r'''
\begin{aligned}
&f_{\mathrm{FD}}(k) = \frac{1}{\mathrm{e}^{k/T_\nu} + 1},\qquad
 n_i = 2\int\frac{\mathrm{d}^3\vec k}{(2\pi)^3}\,f_{\mathrm{FD}} = \frac{3\zeta(3)}{2\pi^2}\,T_\nu^3,\qquad
 \rho_i = 2\int\frac{\mathrm{d}^3\vec k}{(2\pi)^3}\,\sqrt{k^2 + m_i^2}\,f_{\mathrm{FD}},\\
&\bar v_i = \frac{\int_0^\infty k^2\,\frac{k}{\sqrt{k^2 + m_i^2}}\,f_{\mathrm{FD}}\,\mathrm{d}k}{\int_0^\infty k^2\,f_{\mathrm{FD}}\,\mathrm{d}k},
 \qquad \text{flavour content of }\nu_i:\ \lvert U_{\alpha i}\rvert^2
\end{aligned}''', 'STANDARD', ['neutrino mass states'],
  'Exact integrals: T_nu = 1.9454 K, 112.0 per cm^3 per mass state, mean velocities 0.435, 0.0604, 0.0105 c today, '
  'Omega_nu h^2 = 6.382e-4.', name='cnb')
