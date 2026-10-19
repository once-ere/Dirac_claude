from build_lib import E

E('FE', 'The Kohn-Sham equations of dirac16complex coupled to all fields', r'''
h\,\chi_o = \varepsilon_o\,\chi_o,\qquad
h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M_{\mathrm{eff}}(y)\,\sigma_2 + \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y)
 + \frac{1 - \sigma_3}{2}\,v_{\mathrm{b}}(y)''', 'DERIVED', ['dirac16complex Psi', 'metric g', 'all Standard-Model fields (mean fields)'],
  'Solved numerically to self-consistency (60 to 240 exact free eigenfunctions per sector, tolerance 1e-13, Anderson mixing, '
  'Richardson extrapolation in the basis size; the record states reproduced to 1e-13); the I13 term acts on the lower component '
  'only.', name='ks')

E('FE', 'The Kohn-Sham mean fields', r'''
\begin{aligned}
&M_{\mathrm{eff}}(y) = m_\Psi + \frac{15}{16}\,\lambda\,n^{\mathrm{sc}}(y) + \frac{\langle\mathcal{F}\rangle}{\Lambda_\star^3},\qquad
 v(y) = -\frac{\lambda}{16}\,n(y) + \frac{c_{\mathrm{V}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi q_\psi\,n_{\psi i}(y),\\
&v_{\mathrm{b}}(y) = \frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi q^{B}_\psi\,n_{\psi i}(y)
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'fermions (I11, I13)', 'gauge condensates (I12)'],
  'Local mean fields of the contact self-interaction (record) and of the portals; the portal fields are applied with the '
  'densities and condensates of each environment ([[levelshift]]).', name='ks_mean')

E('FE', 'The Kohn-Sham densities, shells, cell volume and occupations', r'''
\begin{aligned}
&n = \sum_o\tfrac12\,d_o\,\phi_o\,n_o,\qquad n^{\mathrm{sc}} = \sum_o\tfrac12\,d_o\,\phi_o\,n^{\mathrm{sc}}_o,\qquad
 n_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\chi_o,\\
&n^{\mathrm{sc}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_2\chi_o,\qquad
 n^{\mathrm{t}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_3\chi_o,\qquad
 d_o = 4\,r_3\big(\lvert\vec n_o\rvert^2\big),\qquad \vec k_o = k_{\mathrm{lat}}\,\vec n_o,\\
&\mathrm{Vol}_7 = \Big(\frac{2\pi}{k_{\mathrm{lat}}}\Big)^3v_{\mathrm{t}}\,f^4,\qquad
 \phi_o = \frac{1}{\mathrm{e}^{(\varepsilon_o - \mu_{\mathrm{chem}})/T} + 1}\ \ \text{(Mermin; or 0 and 1 for the aufbau)}
\end{aligned}''', 'RECORD', ['dirac16complex Psi'],
  'Exact definitions (the factor 1/2 is the weight of each fold parity); k_lat = 0.25 H in the computations.', name='ks_dens')

E('FE', 'The Kohn-Sham energy', r'''
E_{\mathrm{KS}} = \sum_o d_o\,\phi_o\,\varepsilon_o - 2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,e_{\mathrm{int}}\,\mathrm{d}y,
\qquad e_{\mathrm{int}} = \frac{15}{32}\,\lambda\,\big(n^{\mathrm{sc}}\big)^2 - \frac{1}{32}\,\lambda\,n^2''', 'RECORD',
  ['dirac16complex Psi'],
  'Computed for every state (Richardson errors below 2.2e-9 relative); the energy identity [[ks_id]] holds to 4e-15.',
  name='ks_energy')

E('FE', 'The energy-momentum tensor of a Kohn-Sham state', r'''
\begin{aligned}
&\rho = \sum_o\tfrac12\,d_o\phi_o\,\varepsilon_o\,n_o - e_{\mathrm{int}},\qquad
 p_3 = \sum_o\tfrac12\,d_o\phi_o\,\frac{\mathrm{e}^{-a_4}\lvert\vec k_o\rvert}{3}\,n^{\mathrm{t}}_o + e_{\mathrm{int}},
 \qquad p_5 = e_{\mathrm{int}},\\
&p_0 = \sum_o\tfrac12\,d_o\phi_o\Big[(\varepsilon_o - v)\,n_o - M_{\mathrm{eff}}\,n^{\mathrm{sc}}_o
 - \mathrm{e}^{-a_4}\lvert\vec k_o\rvert\,n^{\mathrm{t}}_o\Big] + e_{\mathrm{int}}
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'metric g (source)'],
  'Evaluated for every state; its block averages enter the block response [[adiabatic]] (dark matter at rest: p3 = 0 and '
  'p0/rho = 0.772034343 = -d ln eps_DM/d ln f).', name='ks_tmn')

E('FE', r'The energy identity and the $y$-conservation law of a Kohn-Sham state', r'''
E_{\mathrm{KS}} = 2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\rho\,\mathrm{d}y,\qquad
p_0\big\vert_{y=0} - \mathrm{e}^{-3HL}\,p_0\big\vert_{y=-L} = 3H\int_{-L}^{0}\mathrm{e}^{3Hy}p_5\,\mathrm{d}y''', 'DERIVED',
  ['dirac16complex Psi'],
  'Verified for every self-consistent state (4e-15 and 9e-8 with Richardson extrapolation).', name='ks_id')

E('FE', 'The boundary conditions of the Kohn-Sham orbitals', r'''
\chi = (\chi_1,\ \chi_2)^T:\qquad \chi_2(0) = 0\ \ \text{(even)}\quad\text{or}\quad \chi_1(0) = 0\ \ \text{(odd)},\qquad
\chi_2(-L) = 0''', 'DERIVED', ['dirac16complex Psi'],
  'The block form of [[bc_psi]] (gamma^{x0} = sigma_3 in every block); self-adjoint.', name='ks_bc')

E('FE', 'The portals I11 and I13 on the zero modes: the four-dimensional contact interactions', r'''
\begin{aligned}
&\mathcal{L}_4 = \big(G_{\mathrm{V}}\,q_f\,\tilde I_{of} + G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of}\big)
 \big(\mathrm{i}\bar\Psi_o\gamma^\mu\Psi_o\big)\big(\mathrm{i}\bar\psi_f\gamma_\mu\psi_f\big),\\
&\tilde I_{of} = \frac{1}{H}\int_{-L}^{0}\big(a_o^2 + b_o^2\big)\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 \tilde I^{(b)}_{of} = \frac{1}{H}\int_{-L}^{0}b_o^2\,\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 G_{\mathrm{V}} = \frac{c_{\mathrm{V}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\qquad
 G_{\mathrm{A}} = \frac{c_{\mathrm{A}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\\
&n_{\psi i}(y) = \frac{n_f\,\varrho_f(y)\,\mathrm{e}^{-3Hy}}{2f^4v_{\mathrm{t}}},\qquad
 \varrho(y; c) = \frac{2c}{L}\,\frac{\mathrm{e}^{2cy/L}}{1 - \mathrm{e}^{-2c}}
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'every Standard-Model fermion'],
  'The overlaps are computed with the Kohn-Sham orbitals (Q: 8.2722, L: 1.2524 for the dark matter) and equal the derivatives '
  'of self-consistent levels with respect to the mean-field amplitudes to 3e-10 (Hellmann-Feynman); I13 vanishes on the fold '
  'bands (to 7e-14).', name='contact4d')

E('FE', 'The portal I12 on the dark matter', r'''
\begin{aligned}
&\mathcal{L}_4^{\mathrm{I12}} = -\mathcal{O}_{\mathrm{DM}}\,\frac{\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{DM}}}{\Lambda_\star^3}
 \big(c_{\mathrm{G}}\,G^A_{\mu\nu}G^{A\mu\nu} + c_{\mathrm{W}}\,W^I_{\mu\nu}W^{I\mu\nu} + c_{\mathrm{B}}\,B_{\mu\nu}B^{\mu\nu}\big),\qquad
 \mathcal{O}_{\mathrm{DM}} = \frac{\partial\varepsilon_{\mathrm{DM}}}{\partial m_\Psi},\\
&G_{\mathrm{g}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{G}}\,g_3^2}{\Lambda_\star^3},\qquad
 G_{\mathrm{W}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{W}}\,g_2^2}{\Lambda_\star^3},\qquad
 G_{\mathrm{B}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{B}}\,g_1^2}{\Lambda_\star^3}
\end{aligned}''', 'DERIVED', ['dark matter', 'gluons', 'W', 'B'],
  'O_DM = 0.7072 (Hellmann-Feynman, checked to 1e-8); the field strengths are in the geometric normalisation of the action '
  '(flat zero modes), and G_g, G_W, G_B are the couplings to the canonically normalised fields (field divided by its '
  'four-dimensional coupling) used in the cross-section [[xsec]]; the benchmark strength is unitarity safe.', name='i12dm')

E('FE', 'The shift of a Kohn-Sham level by the mean fields of an environment', r'''
\Delta\varepsilon_o = \sum_f\big(G_{\mathrm{V}}\,q_f\,\tilde I_{of} + G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of}\big)\,n_f
 + \mathcal{O}_o\,\frac{c_{\mathrm{I12}}}{\Lambda_\star^3}\Big[\big\langle G^A_{\mu\nu}G^{A\mu\nu}\big\rangle
 + \big\langle W^I_{\mu\nu}W^{I\mu\nu}\big\rangle + \big\langle B_{\mu\nu}B^{\mu\nu}\big\rangle\Big],
 \qquad \mathcal{O}_o = \frac{\partial\varepsilon_o}{\partial m_\Psi}''', 'DERIVED',
  ['dirac16complex Psi', 'every Standard-Model field (densities, condensates)'],
  'First order in the mean fields (Hellmann-Feynman; the response is screened by only 3.5e-4 in the interacting state); '
  'universal I12 coefficients c_G = c_W = c_B = c_I12.', name='levelshift')

E('FE', 'The level shift of the dark matter in matter of protons, neutrons and electrons', r'''
\begin{aligned}
&\Delta\varepsilon_{\mathrm{I11}} = G_{\mathrm{V}}\Big[\frac13\,n_{\mathrm{u}}\,\frac{\tilde I_Q + \tilde I_{u_R}}{2}
 + \frac13\,n_{\mathrm{d}}\,\frac{\tilde I_Q + \tilde I_{d_R}}{2} - n_{\mathrm{e}}\,\frac{\tilde I_\ell + \tilde I_{e_R}}{2}\Big],\\
&\Delta\varepsilon_{\mathrm{I13}} = G_{\mathrm{A}}\Big[\frac13\,n_{\mathrm{u}}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{u_R}}{2}
 + \frac13\,n_{\mathrm{d}}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{d_R}}{2}\Big],\qquad
 n_{\mathrm{u}} = 2n_{\mathrm{p}} + n_{\mathrm{n}},\qquad n_{\mathrm{d}} = n_{\mathrm{p}} + 2n_{\mathrm{n}}
\end{aligned}''', 'DERIVED', ['dark matter', 'quarks', 'electrons'],
  'Evaluated in ten environments (unpolarised fermions, each chirality half of the density); at most 8.2e-10 GeV (I13, at the '
  'freeze-out).', name='levelshift_env')

E('FE', 'The thermal gluon condensate from the trace anomaly', r'''
\big\langle G^A_{\mu\nu}G^{A\mu\nu}\big\rangle(T) = \big\langle G^A_{\mu\nu}G^{A\mu\nu}\big\rangle(0)
 - \frac{32\pi^2}{b_3}\,\Theta_{\mathrm{QCD}},\qquad
\big\langle G^A_{\mu\nu}G^{A\mu\nu}\big\rangle(0) = 4\pi^2\times0.012\ \text{GeV}^4,\qquad
b_3 = 11 - \frac23\,N_{\mathrm{f}}''',
  'STANDARD', ['gluons'],
  'Geometric normalisation (the canonical field times g_3): the vacuum value is 4 pi^2 times the standard condensate '
  '<(alpha_s/pi) G^2> = 0.012 GeV^4 of canonically normalised fields (STANDARD); the relation does not depend on the '
  'signature convention.', name='gluon_cond')

E('FE', 'The QCD interaction measure', r'''
\begin{aligned}
&\frac{\Theta_{\mathrm{QCD}}}{T^4} = 4\exp\Big[-\frac{\ln^2(T/0.2\,\text{GeV})}{0.5}\Big]\ \ (T < 1\,\text{GeV}),\qquad
 \frac{\Theta_{\mathrm{QCD}}}{T^4} = \frac{b_3}{3}\Big(1 + \frac{5N_{\mathrm{f}}}{12}\Big)\alpha_3^2\ \ (T > 1\,\text{GeV}),\\
&p_{\mathrm{QCD}} = \frac{8\pi^2}{45}T^4\Big[1 + \frac{21N_{\mathrm{f}}}{32}
 - \frac{15}{4}\Big(1 + \frac{5N_{\mathrm{f}}}{12}\Big)\frac{\alpha_3}{\pi}\Big],\qquad
 \frac{\mathrm{d}\alpha_3}{\mathrm{d}\ln T} = -\frac{b_3}{2\pi}\,\alpha_3^2,\qquad
 \Theta_{\mathrm{QCD}} = T^5\,\frac{\mathrm{d}}{\mathrm{d}T}\Big(\frac{p_{\mathrm{QCD}}}{T^4}\Big)
\end{aligned}''', 'ESTIMATE', ['quark-gluon plasma'],
  'A lattice-like shape below 1 GeV (ESTIMATE) and leading-order perturbation theory above (alpha_3 at the scale 2 pi T).',
  name='qcd_measure')

E('FE', r'The thermal condensate of a massive vector boson and the order-$\alpha_{\mathrm{G}}$ condensate of a gauge plasma', r'''
\begin{aligned}
&\big\langle F^V_{\mu\nu}F^{V}{}^{\mu\nu}\big\rangle(T) = -2\,\Theta_V\ \ \text{(for $V = W^\pm, Z$)},\qquad
 \big\langle F_{\mathrm{geo}}^2\big\rangle = -4\,\frac{\partial p}{\partial\big(1/g_{\mathrm{G}}^2\big)} = 4g_{\mathrm{G}}^2\,p_{\alpha,\mathrm{G}},\\
&p_{\alpha,\mathrm{G}} = -\frac{g_{\mathrm{G}}^2T^4}{144}\,d_{\mathrm{adj}}\Big[C_{\mathrm{adj}} + \frac52\,T_{\mathrm{F}}N_{\mathrm{f}}\Big]
\end{aligned}''',
  'STANDARD', ['W', 'Z', 'gauge plasmas'],
  'The first is the free part (on shell the Proca Lagrangian is a total derivative); the second (Feynman-Hellmann) reproduces '
  'the trace-anomaly gluon condensate to 1e-16; SU(2): d_adj = 3, C_adj = 2, T_F N_f = 3; U(1)_Y: d_adj = 1, C_adj = 0, '
  '(5/2) T_F N_f -> 25/2; no scalar term (ESTIMATE).', name='vector_cond')

E('FE', 'The running electroweak couplings without a Higgs particle', r'''
\frac{1}{\alpha_2(\mu_{\mathrm{ren}})} = \frac{\sin^2\theta_{\overline{\mathrm{MS}}}}{\alpha_{\mathrm{em}}}
 + \frac{b_2}{2\pi}\ln\frac{\mu_{\mathrm{ren}}}{m_{\mathrm{Z}}},\qquad
\frac{1}{\alpha_1(\mu_{\mathrm{ren}})} = \frac{1 - \sin^2\theta_{\overline{\mathrm{MS}}}}{\alpha_{\mathrm{em}}}
 + \frac{b_1}{2\pi}\ln\frac{\mu_{\mathrm{ren}}}{m_{\mathrm{Z}}},\qquad b_2 = \frac{10}{3},\quad b_1 = -\frac{20}{3}''',
  'STANDARD', ['W', 'B'],
  'One loop from the MS-bar values at m_Z; the couplings of the condensates are taken at mu_R = 2 pi T.', name='running')

E('FE', 'The electroweak condensates of a hot plasma', r'''
\big\langle W^I_{\mu\nu}W^{I\mu\nu}\big\rangle = g_2^2\Big[2\big(-2\Theta_{\mathrm{W}}\big)
 + \cos^2\theta_{\mathrm{W}}\big(-2\Theta_{\mathrm{Z}}\big)\Big] + 4g_2^2\,p_{\alpha,2},\qquad
\big\langle B_{\mu\nu}B^{\mu\nu}\big\rangle = g_1^2\sin^2\theta_{\mathrm{W}}\big(-2\Theta_{\mathrm{Z}}\big) + 4g_1^2\,p_{\alpha,1}''',
  'ESTIMATE', ['W', 'Z', 'B'],
  'Below m_W the order-alpha part is multiplied by the thermal suppression of a massive vector (ESTIMATE); at the freeze-out '
  'the W condensate is -5.0e11 GeV^4, almost all from the interaction part.', name='ew_cond')

E('FE', r'dirac16complex acting on the Standard Model: the coupling shifts and the $x_0$ problem of $W^\pm$ and $Z$', r'''
\begin{aligned}
&\frac{\Delta\alpha_3}{\alpha_3} = -4G_{\mathrm{g}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_2}{\alpha_2} = -4G_{\mathrm{W}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_1}{\alpha_1} = -4G_{\mathrm{B}}\,n_{\mathrm{DM,tot}},\\
&-\frac{1}{\Upsilon\,\mathrm{e}^{3HL\xi}}\,\frac{\mathrm{d}}{\mathrm{d}\xi}\Big(\Upsilon\,\mathrm{e}^{3HL\xi}\,\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)
 = \tilde m^2F,\qquad \Upsilon(\xi) = 1 + A_{\mathrm{mf}}\,n^{\mathrm{sc}}_{\mathrm{DM}},\qquad
 n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}},\\
&\frac{\mathrm{d}F}{\mathrm{d}\xi}(0) = 0,\qquad \Upsilon(-1)\,\frac{\mathrm{d}F}{\mathrm{d}\xi}(-1) = \beta_{\mathrm{W}}F(-1)
\end{aligned}''', 'DERIVED', ['W', 'Z', 'photon', 'gluons', 'dark matter'],
  'Finite elements (300 quadratic elements, Richardson in the amplitude): d ln m_W^2/dA_mf = -0.1126 while the photon and gluon '
  'zero mode stays massless; the physical shifts are at most 1.7e-16.', name='dm_on_sm')

E('FE', 'Gravity in the coupled solution: the block response to every species', r'''
\begin{aligned}
&\Delta K = \frac{c_\rho\,\kappa\Delta\rho + c_3\,\kappa\Delta p_3 + c_p\,\kappa\Delta\bar p}{H^2},\qquad
 \Delta\ln f = -\frac{\Delta K}{2K_*},\\
&\Delta\ln m_s = \frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}\,\Delta\ln f,\qquad
 \kappa\Delta\rho = 8\pi G_{\mathrm{N}}\,\mathcal{G}(K_*)\,\rho_4
\end{aligned}''', 'DERIVED', ['metric g (block)', 'all species'],
  'Iterated with the masses until self-consistency (the loop gain is at most 1.1e-33, so one step suffices); the block moves '
  'by at most Delta ln f = 1.1e-34 (at the freeze-out).', name='coupled_block')

E('FE', 'The hidden pressure of matter and of the hot plasma', r'''
\bar p = -\frac14\sum_s\big(\rho_s - 3p_s\big)\frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}
 - \frac14\,\Theta_{\mathrm{QCD}}\,\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(N_{\mathrm{f}})}}{\mathrm{d}\ln f}
 + \frac14\,p_{\alpha,2}\,\frac{\mathrm{d}\ln\alpha_2}{\mathrm{d}\ln f} + \frac14\,p_{\alpha,1}\,\frac{\mathrm{d}\ln\alpha_1}{\mathrm{d}\ln f}''',
  'DERIVED', ['all species'],
  'The response of the pressure to the block scale at fixed temperature (p_bar = (1/4) dp/d ln f); the plasma species as ideal '
  'gases with their x0 masses, nucleons and electrons as degenerate Fermi gases in the cold environments.', name='pbar_hidden')

E('FE', 'The block dependence of a gauge coupling and the trace of an electroweak plasma', r'''
\frac{\mathrm{d}\ln\alpha_{\mathrm{G}}(\mu_{\mathrm{ren}})}{\mathrm{d}\ln f}
 = -\alpha_{\mathrm{G}}(\mu_{\mathrm{ren}})\Big[\frac{4}{\alpha_{\mathrm{G}}(m_{\mathrm{KK}})} + \frac{b_{\mathrm{G}}}{2\pi}\Big],\qquad
\Theta_{\mathrm{G}} = -\frac{b_{\mathrm{G}}\,\alpha_{\mathrm{G}}}{2\pi}\,p_{\alpha,\mathrm{G}}''', 'DERIVED', ['gauge fields'],
  'The bulk couplings scale as f^-4 (g^2 = g_hat^2/V_perp) and m_KK as 1/f; leading-order trace anomaly.', name='dlnalpha')

E('FE', 'The block dependence of the QCD scale and of the nucleon mass', r'''
\begin{aligned}
&\frac{1}{\alpha_3(m_{\mathrm{KK}})} = \frac{1}{\alpha_3(m_{\mathrm{Z}})} + \frac{7}{2\pi}\ln\frac{m_{\mathrm{KK}}}{m_{\mathrm{Z}}},\qquad
 \Lambda_{\mathrm{QCD}}^{(6)} = m_{\mathrm{KK}}\,\mathrm{e}^{-2\pi/(7\alpha_3(m_{\mathrm{KK}}))},\qquad
 \Lambda_{\mathrm{QCD}}^{(3)} = \big(\Lambda_{\mathrm{QCD}}^{(6)}\big)^{21/27}\big(m_{\mathrm{c}}m_{\mathrm{b}}m_{\mathrm{t}}\big)^{2/27},\\
&\frac{\mathrm{d}\ln m_{\mathrm{p}}}{\mathrm{d}\ln f} = \Big(1 - \frac{\sigma_{\pi N} + \sigma_{\mathrm{s}}}{m_{\mathrm{p}}}\Big)
 \frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}}{\mathrm{d}\ln f}
 + \frac{\sigma_{\pi N}}{2m_{\mathrm{p}}}\Big(\frac{\mathrm{d}\ln m_{\mathrm{u}}}{\mathrm{d}\ln f} + \frac{\mathrm{d}\ln m_{\mathrm{d}}}{\mathrm{d}\ln f}\Big)
 + \frac{\sigma_{\mathrm{s}}}{m_{\mathrm{p}}}\,\frac{\mathrm{d}\ln m_{\mathrm{s}}}{\mathrm{d}\ln f}
\end{aligned}''', 'ESTIMATE', ['quarks', 'gluons', 'nucleons'],
  'One loop; alpha_3(m_KK) = 0.0606 and d ln m_p/d ln f = -46.1: the most block-sensitive mass of UM-2.', name='nucleon')

E('FE', 'The block dependence of the QCD scale through the quark thresholds', r'''
\begin{aligned}
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f} = -1 - \frac{8\pi}{7\alpha_3(m_{\mathrm{KK}})},\qquad
 \frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(5)}}{\mathrm{d}\ln f} = \frac{21}{23}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{23}\frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f},\\
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(4)}}{\mathrm{d}\ln f} = \frac{21}{25}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{25}\Big(\frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f} + \frac{\mathrm{d}\ln m_{\mathrm{b}}}{\mathrm{d}\ln f}\Big),\\
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}}{\mathrm{d}\ln f} = \frac{21}{27}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{27}\Big(\frac{\mathrm{d}\ln m_{\mathrm{c}}}{\mathrm{d}\ln f} + \frac{\mathrm{d}\ln m_{\mathrm{b}}}{\mathrm{d}\ln f}
 + \frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f}\Big)
\end{aligned}''', 'ESTIMATE', ['gluons', 'quarks'],
  'One loop: -60.2 (six flavours), -55.6, -52.0 and -49.0 (three flavours).', name='qcd_thresholds')

E('FE', 'The block dependence of a fermion mass', r'''
\frac{\mathrm{d}\ln m}{\mathrm{d}\ln f} = -1 + \frac12\Big[\frac{\mathrm{d}\ln\mathcal{Z}(c_L)^2}{\mathrm{d}\ln c_L}
 + \frac{\mathrm{d}\ln\mathcal{Z}(-c_R)^2}{\mathrm{d}\ln(-c_R)}\Big]''', 'DERIVED', ['every Standard-Model fermion'],
  'From m = eps_tilde/(fL) with the first-order root of [[ferm_1gen]] and localisations c proportional to f: -18.82, -18.01, '
  '-14.90, -12.15, -10.89, -6.77 for u, d, s, c, b, t.', name='fermion_sens')

E('FE', 'The densities of the environments of the coupled solution', r'''
\begin{aligned}
&n_{\mathrm{p}} + n_{\mathrm{n}} = \eta_{\mathrm{b}}\,n_\gamma,\qquad n_\gamma = \frac{2\zeta(3)}{\pi^2}\,T^3,\qquad
 \frac{n_{\mathrm{n}}}{n_{\mathrm{p}}} = \mathrm{e}^{-(m_{\mathrm{n}} - m_{\mathrm{p}})/T},\qquad n_{\mathrm{e}} = n_{\mathrm{p}},\\
&n_{\mathrm{DM,tot}} = 2\big(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}\big) = 2\cdot4\,\Big(\frac{M_{\mathrm{DM}}T}{2\pi}\Big)^{3/2}\mathrm{e}^{-M_{\mathrm{DM}}/T}
 \ \ \Big(\frac{M_{\mathrm{DM}}}{T} < 40\Big)
\end{aligned}''',
  'ASSUMED', ['baryons', 'electrons', 'dark matter'],
  'The hot environments (the cold ones use measured densities); the dark matter in equilibrium for both species while '
  'M_DM/T < 40, its relic density afterwards.', name='env')
