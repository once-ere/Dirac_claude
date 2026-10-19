from build_lib import E

E('FE', 'The ideal-gas densities of a species of the plasma', r'''
\rho_s = \frac{d_s}{2\pi^2}\int_0^\infty\frac{k^2E\,\mathrm{d}k}{\mathrm{e}^{E/T} \pm 1},\qquad
p_s = \frac{d_s}{6\pi^2}\int_0^\infty\frac{k^4\,\mathrm{d}k}{E\,(\mathrm{e}^{E/T} \pm 1)},\qquad
s_s = \frac{\rho_s + p_s}{T},\qquad E = \sqrt{k^2 + m_s^2}''', 'STANDARD', ['every species in equilibrium'],
  'Exact integrals with the x0 masses (upper sign fermions); no Higgs particle; right-handed neutrinos, fold bands, radion and '
  'Kaluza-Klein modes not in equilibrium.', name='idealgas')

E('FE', 'The effective degrees of freedom and the Hubble rate of the hot Universe', r'''
g_\rho = \frac{30}{\pi^2T^4}\sum_s\rho_s,\qquad g_s = \frac{45}{2\pi^2T^3}\sum_s s_s,\qquad
\mathcal{H} = \Big(\frac{8\pi^3g_\rho}{90}\Big)^{1/2}\frac{T^2}{M_{\mathrm{Pl}}}''', 'STANDARD', ['plasma'],
  'Checked against the exact limits 105.75, 86.25, 10.75 and 43/11.', name='dof')

E('FE', 'The QCD crossover, the neutrino temperature after decoupling and the cooling of the plasma', r'''
w_{\mathrm{QGP}}(T) = \frac12\Big[1 + \tanh\frac{T - T_{\mathrm{c}}}{T_{\mathrm{w}}}\Big],\qquad
\frac{T_\nu}{T} = \Big(\frac{g_{s,e\gamma}(T)}{11/2}\Big)^{1/3},\qquad
\frac{\mathrm{d}\ln T}{\mathrm{d}x_4} = -\frac{\mathcal{H}}{1 + \frac13\,\mathrm{d}\ln g_s/\mathrm{d}\ln T}''', 'ASSUMED', ['plasma'],
  'T_c = 155 MeV, T_w = 15 MeV with a gas of the twelve lightest hadron multiplets below (ASSUMED model of the crossover); '
  'neutrinos decoupled instantaneously at 2 MeV.', name='crossover')

E('FE', 'The Boltzmann equation of one dark-matter species', r'''
\begin{aligned}
&\frac{\mathrm{d}n_{\mathrm{DM}}}{\mathrm{d}x_4} + 3\mathcal{H}n_{\mathrm{DM}}
 = -\langle\sigma v_{\mathrm{rel}}\rangle\big(n_{\mathrm{DM}}\bar n_{\mathrm{DM}} - n_{\mathrm{DM,eq}}^2\big)\ \Rightarrow
 \frac{\mathrm{d}Y_{\mathrm{DM}}}{\mathrm{d}x} = -\Big(1 + \frac13\frac{\mathrm{d}\ln g_s}{\mathrm{d}\ln T}\Big)
 \frac{s\,\langle\sigma v_{\mathrm{rel}}\rangle}{2x\mathcal{H}}\big(Y_{\mathrm{DM}}^2 - Y_{\mathrm{eq}}^2\big),\\
&Y_{\mathrm{DM}} = \frac{n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}}{s},\qquad x = \frac{M_{\mathrm{DM}}}{T},\qquad
 s = \frac{2\pi^2}{45}\,g_sT^3,\qquad Y_{\mathrm{eq}} = \frac{4M_{\mathrm{DM}}^2TK_2(x)}{2\pi^2s}
\end{aligned}''', 'STANDARD', ['dark matter', 'plasma'],
  'Integrated implicitly (Radau, ln Y from x = 5 to 2000, relative tolerance 1e-10) with the degrees of freedom of UM-2; the '
  'late-time integral holds to 1.3e-8; each of the two species freezes out separately.', name='boltz')

E('FE', 'The relativistic thermal average of the annihilation cross-section', r'''
\langle\sigma v_{\mathrm{rel}}\rangle = \frac{1}{8M_{\mathrm{DM}}^4TK_2(x)^2}\int_{4M_{\mathrm{DM}}^2}^{\infty}\sigma\,
 \big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)\,E_{\mathrm{cm}}\,K_1\Big(\frac{E_{\mathrm{cm}}}{T}\Big)\,
 \mathrm{d}\big(E_{\mathrm{cm}}^2\big)''', 'STANDARD', ['dark matter'],
  'Adaptive quadrature in the kinetic energy of the pair, exponentially scaled Bessel functions (Gondolo and Gelmini).',
  name='thermal_avg')

E('FE', 'The relic density', r'''
\Omega_{\mathrm{DM}}h_{100}^2 = \frac{M_{\mathrm{DM}}\,Y_\infty\,s_0}{\rho_{\mathrm{crit}}/h_{100}^2},\qquad
\frac{\rho_{\mathrm{crit}}}{h_{100}^2} = 1.05368\times10^{-5}\ \text{GeV}/\text{cm}^3''', 'STANDARD', ['dark matter'],
  'Each species gives 0.060 (0.120 together) for G_A = 1.278e-9 GeV^-2 (x_f = 31.23).', name='relic')

E('FE', 'The annihilation cross-sections of the dark matter through I12 and I13', r'''
\begin{aligned}
&\sigma_{\mathrm{I12}} = \frac{G_{\mathrm{I12}}^2\,E_{\mathrm{cm}}^3\big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)^{1/2}}{8\pi},\qquad
 G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2,\\
&\sigma_{\mathrm{I13}} = \sum_f\frac{N_{\mathrm{c}}\,G_f^2\,E_{\mathrm{cm}}^2\big(1 + 2M_{\mathrm{DM}}^2/E_{\mathrm{cm}}^2\big)}{24\pi\beta_{\mathrm{cm}}},
 \qquad G_f = G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of},\\
&\beta_{\mathrm{cm}} = \sqrt{1 - \frac{4M_{\mathrm{DM}}^2}{E_{\mathrm{cm}}^2}},\qquad
 k_{\mathrm{cm}} = \sqrt{\frac{E_{\mathrm{cm}}^2}{4} - M_{\mathrm{DM}}^2}
\end{aligned}''', 'DERIVED', ['dark matter', 'gauge bosons', 'quarks'],
  'Spin averaged; I12 p-wave (from 3P0 only, polarisation sum and spin trace checked numerically), I13 s-wave (from 3S1), summed '
  'over the quark Weyl components (o the dark-matter orbital; the sum of N_c (q^B I^(b))^2 is 16.351); I12 at the unitarity-safe '
  'benchmark G_I12 = pi/(2 M_DM^3).', name='xsec')

E('FE', 'The partial-wave unitarity bounds', r'''
\sigma_{\mathrm{I12}} \le \frac{\pi}{4k_{\mathrm{cm}}^2}\ \ \text{(total angular momentum 0)},\qquad
\sigma_{\mathrm{I13}} \le \frac{3\pi}{4k_{\mathrm{cm}}^2}\ \ \text{(total angular momentum 1)}''', 'DERIVED', ['dark matter'],
  'Where an effective cross-section exceeds its bound it is replaced by the bound; I13 reaches it only above v_rel = 0.51 (22 % '
  'of the freeze-out rate); I12 alone would need a strongly coupled 3P0 channel.', name='unitarity')

E('FE', 'The freeze-in of the fold bands through I11', r'''
\Gamma_{\mathrm{fi}} = \frac{T}{32\pi^4}\int_0^\infty\mathrm{d}\big(E_{\mathrm{cm}}^2\big)\Big(\sum_{\text{spins}}\sigma\Big)E_{\mathrm{cm}}^3
 K_1\Big(\frac{E_{\mathrm{cm}}}{T}\Big) = \frac{4}{\pi^5}\,N_{\mathrm{fold}}\,G_{\mathrm{V}}^2\,T^8\sum_fN_{\mathrm{c}}\big(q_f\tilde I_{of}\big)^2,
\qquad \frac{\mathrm{d}\big(\rho_{\mathrm{fold}}\,\mathrm{e}^{4a_4}\big)}{\mathrm{d}x_4} = 8T\,\Gamma_{\mathrm{fi}}\,\mathrm{e}^{4a_4}''',
  'DERIVED', ['fold bands of Psi', 'Standard-Model plasma'],
  'Maxwell-Boltzmann, massless (o the fold band; the sum is 126.85 over the fifteen multiplets of three generations); integrated '
  'from T_max = 10 TeV (ASSUMED): Delta N_eff = 5.21e29 G_V^2 GeV^4, so the benchmark G_V = 4.38e-17 GeV^-2 gives 0.001.',
  name='freezein')

E('FE', 'The dark radiation of the fold bands and their departure from equilibrium', r'''
\Delta N_{\mathrm{eff}} = \frac{\rho_{\mathrm{fold}}}{\rho_\nu},\qquad \rho_\nu = \frac78\,\frac{\pi^2}{15}\,T_\nu^4,\qquad
\frac{2\Gamma_{\mathrm{fi}}}{n_{\mathrm{fold,eq}}\,\mathcal{H}} \ll 1,\qquad
n_{\mathrm{fold,eq}} = N_{\mathrm{fold}}\cdot4\cdot\frac34\,\frac{\zeta(3)}{\pi^2}\,T^3''', 'DERIVED', ['fold bands'],
  'The production rate per fold quantum is 0.012 of the Hubble rate at T_max: never in equilibrium.', name='neff_fold')

E('FE', r'The right-handed neutrinos if I13 coupled to $B - L$', r'''
\begin{aligned}
&G_{\mathrm{A}}^{B-L} = G_{\mathrm{A}}\Big[\frac{\mathcal{S}_B}{\mathcal{S}_{B-L}}\Big]^{1/2},\qquad
 \mathcal{S}_B = \sum_fN_{\mathrm{c}}\big(q^{B}_f\tilde I^{(b)}_{of}\big)^2,\qquad
 \mathcal{S}_{B-L} = \sum_fN_{\mathrm{c}}\big(q_f\tilde I^{(b)}_{of}\big)^2,\\
&\frac{\mathrm{d}n_{\nu_R}}{\mathrm{d}x_4} + 3\mathcal{H}n_{\nu_R} = \Gamma_\nu\Big(1 - \frac{n_{\nu_R}^2}{(n_{\nu_R}^{\mathrm{eq}})^2}\Big),\qquad
 \Gamma_\nu = 2\,n_{\mathrm{DM,eq}}\,\bar n_{\mathrm{DM,eq}}\,\frac{G_\nu^2M_{\mathrm{DM}}^2}{2\pi},\qquad
 G_\nu = G_{\mathrm{A}}^{B-L}\,\tilde I^{(b)}_{\nu_R},\\
&n_{\nu_R}^{\mathrm{eq}} = \frac34\,\frac{\zeta(3)}{\pi^2}\,T^3,\qquad
 n_{\mathrm{DM,eq}} = \bar n_{\mathrm{DM,eq}} = 2\Big(\frac{M_{\mathrm{DM}}T}{2\pi}\Big)^{3/2}\mathrm{e}^{-x}
\end{aligned}''', 'DERIVED', ['right-handed neutrinos', 'dark matter'],
  'The counterfactual that motivates the baryon current: the three nu_R would reach 0.9997 of equilibrium by M/T = 40 and add '
  'Delta N_eff = 0.144 (the factor 2 counts the two dark-matter species).', name='nuR_BL')

E('FE', 'The elastic scattering of right-handed neutrinos on the dark matter', r'''
\Gamma_{\mathrm{el}} = 2\big(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}\big)\,\sigma_{\mathrm{el}} > \mathcal{H},\qquad
\sigma_{\mathrm{el}} = \frac{G_\nu^2E^2}{2\pi},\qquad E \simeq 3T''', 'ESTIMATE', ['right-handed neutrinos', 'dark matter'],
  'For a Weyl nu_R on a heavy Dirac fermion (two species); kinetic decoupling at M/T = 24.4.', name='nuR_el')

E('FE', 'The extra radiation of species that decouple early', r'''
\Delta N_{\mathrm{eff}} = N_{\mathrm{W}}\Big(\frac{10.75}{g_s}\Big)^{4/3}F_{\mathrm{h}},\qquad
F_{\mathrm{h}} = \Big[\frac{T_\nu}{T_\gamma}\Big(\frac{11}{4}\Big)^{1/3}\Big/\big(1 + h_\nu\big)\Big]^4 = 1.0095''', 'DERIVED',
  ['decoupled Weyl species'],
  'T_nu/T_gamma = 0.71664 and h_nu = 0.00165 from the common-temperature decoupling of [[neff]]; used for the B - L variant '
  '(0.144) and the self-interaction channel.', name='deltaneff')

E('FE', 'The production of right-handed neutrinos through I11 (with the baryon current in I13)', r'''
r_{\nu_R} = \frac{G_{\mathrm{V}}^2\sum_{i=1}^{3}\tilde I_{\nu_R,i}^2}{G_{\mathrm{A}}^2\,\mathcal{S}_B}''', 'DERIVED',
  ['right-handed neutrinos', 'dark matter'],
  'Evaluated: 2.0e-17, so the right-handed neutrinos are never thermalised.', name='nuR_I11')

E('FE', 'The self-interaction channel of the dark matter into the fold bands', r'''
\begin{aligned}
&\mathcal{L}_4^{\lambda} = -\lambda\,\big(\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{fold}}\big)\big(\bar\Psi_{\mathrm{fold}}\Psi_{\mathrm{DM}}\big)
 \big(n^{\mathrm{sc}}_{\mathrm{DF}}\big)^2,\qquad n^{\mathrm{sc}}_{\mathrm{DF}} = a_{\mathrm{DM}}b_{\mathrm{fold}} + b_{\mathrm{DM}}a_{\mathrm{fold}},
 \qquad b_{\mathrm{fold}} = 0,\\
&G_\lambda = \frac{\lambda H\tilde I_\lambda}{2f^4v_{\mathrm{t}}},\qquad
 \tilde I_\lambda = \frac{1}{H}\int_{-L}^{0}\big(n^{\mathrm{sc}}_{\mathrm{DF}}\big)^2\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 \sigma_\lambda v_{\mathrm{rel}} = \frac{G_\lambda^2M_{\mathrm{DM}}^2}{2\pi}\ \ \text{(per final fold species)}
\end{aligned}''', 'ESTIMATE', ['dark matter', 'fold bands'],
  'I_lambda = 14.38 (units of H, DERIVED); the cross-section is an ESTIMATE (Fierz coefficients not computed).', name='selfint')

E('FE', 'The energy put into the fold bands by the self-interaction channel', r'''
\frac{\mathrm{d}\big(\rho_{\mathrm{fold}}\,\mathrm{e}^{4a_4}\big)}{\mathrm{d}x_4} = 2M_{\mathrm{DM}}\,\Gamma_\lambda\,\mathrm{e}^{4a_4},\qquad
\Gamma_\lambda = 2\,n_{\mathrm{DM,eq}}\,\bar n_{\mathrm{DM,eq}}\,\sigma_\lambda v_{\mathrm{rel}}\,N_{\mathrm{fold}},\qquad
\frac{2\Gamma_\lambda}{n_{\mathrm{fold,eq}}\,\mathcal{H}} \ll 1''', 'DERIVED', ['dark matter', 'fold bands'],
  'Integrated from T_max to the freeze-out: Delta N_eff = 1.83e26 G_lambda^2 GeV^4, so Delta N_eff <= 0.001 requires '
  'G_lambda <= 2.3e-15 GeV^-2 (ASSUMED bound on lambda); otherwise the fold bands decouple as four Weyl species ([[deltaneff]]).',
  name='selfint_energy')
