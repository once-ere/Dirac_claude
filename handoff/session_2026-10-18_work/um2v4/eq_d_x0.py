from build_lib import E

E('FE', r'The $x_0$ eigenvalue equation of the gauge fields and the graviton', r'''
\begin{aligned}
&\int_{-L}^{0}\mathrm{d}y\,f^4\mathrm{e}^{3Hy}\Big[\frac{(\partial_yF)^2}{f^2} - m^2F^2\Big]\ \text{stationary}:\qquad
 -\frac{1}{f^2}\,\mathrm{e}^{-3Hy}\,\partial_y\big(\mathrm{e}^{3Hy}\,\partial_yF\big) = m^2F,\\
&\Leftrightarrow\qquad -\mathrm{e}^{-3HL\xi}\,\frac{\mathrm{d}}{\mathrm{d}\xi}\Big(\mathrm{e}^{3HL\xi}\,\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)
 = \tilde m^2F,\qquad \tilde m = m\,fL
\end{aligned}''', 'DERIVED', ['gluons', 'photon', 'W+', 'W-', 'Z', 'graviton (transverse-traceless)'],
  'Exact reduction on the static block (gauge A_y = 0; the same operator for the transverse-traceless graviton in Einstein '
  'gravity); solved exactly by [[x0_boson_eig]] (mpmath) and checked with finite elements to 5e-10.', name='x0_boson')

E('FE', r'The fold and tip conditions of the boson $x_0$ profiles', r'''
\begin{aligned}
&\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=0} = 0\ \ \text{(even)}\quad\text{or}\quad F(0) = 0\ \ \text{(odd)},\qquad
 \frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=-1} = \beta\,F(-1),\\
&\beta = 0\ \ (\text{photon, gluons, graviton}),\qquad \beta = \beta_{\mathrm{W}}\ \ (W^\pm),\qquad
 \beta = \beta_{\mathrm{Z}} = \frac{\beta_{\mathrm{W}}}{\cos^2\theta_{\mathrm{W}}}\ \ (Z)
\end{aligned}''', 'DERIVED',
  ['gluons', 'photon', 'W+', 'W-', 'Z', 'graviton'],
  'The tip condition is the natural boundary condition of the tip mass term (IN tip action); one value for W+ and W- '
  '(particle and antiparticle); beta_W is fitted to the measured masses ([[wz_fit]]).', name='x0_boson_bc')

E('FE', 'The boson eigenvalue conditions', r'''
\begin{aligned}
&F = \mathrm{e}^{-3HL\xi/2}\,\tilde F,\qquad \varpi^2 = \tilde m^2 - \frac{9H^2L^2}{4}:\\
&\text{even: }\Big[\varpi^2 + \frac{3HL}{2}\Big(\beta + \frac{3HL}{2}\Big)\Big]\sin\varpi - \beta\,\varpi\cos\varpi = 0,\qquad
 \text{odd: }\varpi\cos\varpi + \Big(\beta + \frac{3HL}{2}\Big)\sin\varpi = 0;\\
&\beta = 0:\quad \tilde m = 0\ \text{(flat profile)},\qquad \tilde m_n^2 = \frac{9H^2L^2}{4} + \varpi_n^2\ \text{(even)},\qquad
 \varpi\cot\varpi = -\frac{3HL}{2}\ \text{(odd)}
\end{aligned}''', 'DERIVED', ['gauge fields', 'graviton'],
  'Exact; graviton, photon and gluons are exactly massless; the first even Kaluza-Klein level 30.1196, the first odd 27.0890, '
  'the gap 20.25 (HL = 3); W: 1.32149e-5, Z: 1.70150e-5 (mpmath; finite elements 3e-14).', name='x0_boson_eig')

E('FE', r'The tower of Kaluza-Klein gravitons (the terms $n \ge 1$ of the metric series)', r'''
\begin{aligned}
&F_n(\xi) = \mathrm{e}^{-3HL\xi/2}\Big(\cos\varpi_n\xi + \frac{3HL}{2\varpi_n}\sin\varpi_n\xi\Big),\qquad
 \varpi_n = \pi,\ 2\pi,\ 3\pi,\ \dots,\\
&\tilde m_n^2 = \frac{9H^2L^2}{4} + \varpi_n^2,\qquad m^{\mathrm{KK}}_n = \frac{\tilde m_n}{fL},\qquad
 N_n = \int_{-1}^{0}\mathrm{e}^{3HL\xi}F_n^2\,\mathrm{d}\xi = \frac12\Big(1 + \frac{9H^2L^2}{4\varpi_n^2}\Big),\qquad
 N_0 = \frac{1 - \mathrm{e}^{-3HL}}{3HL}
\end{aligned}''', 'DERIVED', ['graviton tower'],
  'Exact; 30.1196, 59.7284, 109.0764 for n = 1, 2, 3 (finite elements agree to 3.9e-9); m_1 = m_KK = 121.32 TeV.',
  name='kk_tower')

E('FE', 'The potential between two static masses with the Kaluza-Klein gravitons', r'''
V_{\mathrm{N}}(r) = -\frac{G_{\mathrm{N}}M_1M_2}{r}\Big[1 + \sum_{n\ge1}\mathcal{A}_n\,\mathrm{e}^{-m^{\mathrm{KK}}_nr}\Big],\qquad
\mathcal{A}_n = \frac{N_0}{N_n}\Big(\int_{-1}^{0}\varrho_1F_n\,\mathrm{d}\xi\Big)\Big(\int_{-1}^{0}\varrho_2F_n\,\mathrm{d}\xi\Big)''',
  'DERIVED', ['graviton tower', 'sources with x0 profiles'],
  'Evaluated with the zero-mode profiles (0.0904, 0.0136, 0.0057 for two quark-doublet profiles); zero for the flat profile of '
  'the gauge zero modes; Newton\'s law is exact at every measurable distance.', name='kk_potential')

E('FE', r'The $W^\pm$ and $Z$ masses, the electroweak parameter and the Kaluza-Klein scale', r'''
\rho_{\mathrm{EW}} = \frac{\tilde m_{\mathrm{W}}^2}{\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}}} = \rho_{\mathrm{EW},0},\qquad
\cos^2\theta_{\mathrm{W}} = \frac{m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2}{\rho_{\mathrm{EW},0}},\qquad
m_{\mathrm{KK}} = m_{\mathrm{W}}\,\frac{\tilde m_1}{\tilde m_{\mathrm{W}}},\qquad
m_{\mathrm{Z}} = m_{\mathrm{W}}\,\frac{\tilde m_{\mathrm{Z}}}{\tilde m_{\mathrm{W}}}''', 'DERIVED', ['W+', 'W-', 'Z'],
  'Fit (DERIVED): beta_W = 0.011912 reproduces rho_EW,0 - 1 = 0.00038 and both measured masses; m_KK = 121.32 TeV, '
  'H = 14.296 TeV.', name='wz_fit')

E('FE', 'The exact reduction of the eight-dimensional Dirac equation to the block Hamiltonian', r'''
\begin{aligned}
&\Psi = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\mathcal{V}\chi(y, x_4):\\
&\gamma^MD_M\Psi - \big(M(y) - \mathrm{i}v(y)\gamma^{x_4}\big)\Psi
 = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\gamma^{x_4}\mathcal{V}
 \big[\partial_{x_4}\chi + \mathrm{i}h\chi\big],\\
&h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M(y)\,\sigma_2 + \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y),\qquad
 \mathrm{i}\,\partial_{x_4}\chi = h\chi;\\
&\text{in each block: }\gamma^{x_0} = \sigma_3,\qquad \mathcal{B} = \varsigma\varsigma_2,\qquad
 C = \varsigma_2\sigma_2,\qquad \Gamma_4 = -\varsigma\varsigma_2\sigma_3
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'every Standard-Model fermion', 'metric g'],
  'Exact (all eight blocks, general a4(x4), b4(x4), M(y), v(y); checked with the author\'s matrices); the basis of the reduction '
  'for every fermion of UM-2.', name='ferm_red')

E('FE', 'The chiral zero modes (massless four-dimensional fermions)', r'''
\begin{aligned}
&\chi = \big(\mathrm{e}^{c\xi},\ 0\big)^T\ \ (\text{doublet},\ \Gamma_4 = +1),\qquad
 \chi = \big(0,\ \mathrm{e}^{-c\xi}\big)^T\ \ (\text{singlet},\ \Gamma_4 = -1),\qquad c = f\mu L,\\
&h\big(\mathrm{e}^{c\xi},\ 0\big)^T = \varsigma\,\mathrm{e}^{-a_4}k\big(\mathrm{e}^{c\xi},\ 0\big)^T
\end{aligned}''', 'DERIVED',
  ['every Standard-Model fermion', 'dirac16complex Psi (fold band)'],
  'Exact: the zero modes are massless four-dimensional particles with energy e^{-a4}|k|; localised at the fold for c_L > 0 and '
  'c_R < 0.', name='ferm_zero')

E('FE', r'The tip values of the doublet and singlet solutions at $k = 0$', r'''
\begin{aligned}
&\frac{\mathrm{d}a}{\mathrm{d}\xi} = c\,a - \tilde\varepsilon\,b,\qquad \frac{\mathrm{d}b}{\mathrm{d}\xi} = \tilde\varepsilon\,a - c\,b,
 \qquad \chi = (a,\ \mathrm{i}b),\qquad \tilde\varepsilon = \varepsilon fL,\qquad
 \upsilon_L = \sqrt{c_L^2 - \tilde\varepsilon^2},\qquad \upsilon_R = \sqrt{c_R^2 - \tilde\varepsilon^2},\\
&(a_L,\ b_L)\big\vert_{\xi=-1} = \Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L},
 -\tilde\varepsilon\,\frac{\sinh\upsilon_L}{\upsilon_L}\Big),\qquad
 (a_R,\ b_R)\big\vert_{\xi=-1} = \Big(\tilde\varepsilon\,\frac{\sinh\upsilon_R}{\upsilon_R},
 \cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big)
\end{aligned}''', 'DERIVED', ['every Standard-Model fermion'],
  'Exact solutions (block varsigma = +1) that satisfy the fold conditions b(0) = 0 (doublet, c_L > 0) and a(0) = 0 (singlet, '
  'c_R < 0).', name='ferm_k0')

E('FE', 'The exact mass condition of one generation and its first-order root', r'''
\begin{aligned}
&\mathcal{D}(\tilde\varepsilon) = \tilde\varepsilon^2\,\frac{\sinh\upsilon_L}{\upsilon_L}\frac{\sinh\upsilon_R}{\upsilon_R}
 - \mathcal{K}^2\Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L}\Big)
 \Big(\cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big) = 0,\\
&\tilde\varepsilon \simeq \mathcal{K}\,\mathcal{Z}(c_L)\,\mathcal{Z}(-c_R),\qquad \mathcal{Z}(c)^2 = \frac{c\,\mathrm{e}^{-c}}{\sinh c}
\end{aligned}''',
  'DERIVED', ['every Standard-Model fermion'],
  'Exact roots (shooting agrees to 6e-10); the first-order formula agrees to 1.1e-3 (top quark) and better than 3e-4 otherwise.',
  name='ferm_1gen')

E('FE', r'The mass condition of three generations with the $3 \times 3$ tip matrices', r'''
\begin{aligned}
&\Big[\mathrm{diag}\big(b_{L\alpha}\big) + \mathcal{K}\,\mathrm{diag}\Big(\frac{b_{Ri}}{a_{Ri}}\Big)\mathcal{K}^\dagger\,
 \mathrm{diag}\big(a_{L\alpha}\big)\Big]\boldsymbol{\alpha} = 0;\qquad
 \det\big[\cdots\big] = \prod_{i=1}^{3}\frac{b_La_{Ri} + a_Lb_{Ri}}{a_{Ri}},\\
&b_La_R + a_Lb_R = -\mathcal{D}(\tilde\varepsilon)\big\vert_{\mathcal{K} = 1},\qquad
 \boldsymbol{\alpha}^{(i)} = \mathcal{K}\,\mathbf{u}_i,\qquad \boldsymbol{\beta}^{(i)} \propto \mathbf{u}_i,\qquad
 U = \mathcal{K}_e^\dagger\mathcal{K}_\nu,\qquad V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d
\end{aligned}''', 'DERIVED', ['quarks and leptons of three generations'],
  'The factorisation holds for one doublet bulk mass per sector and a unitary tip matrix; verified with mpmath at 50 digits '
  '(roots equal the one-generation roots to 3.0e-42, null vectors the columns of the tip matrix to 1.1e-16).',
  name='ferm_3gen')

E('FE', 'The standard parametrisation of the mixing matrices (the tip matrices of UM-2)', r'''
\begin{aligned}
U = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}\mathrm{e}^{-\mathrm{i}\delta_{\mathrm{CP}}}\\
 -s_{12}c_{23} - c_{12}s_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} &
 c_{12}c_{23} - s_{12}s_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} & s_{23}c_{13}\\
 s_{12}s_{23} - c_{12}c_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} &
 -c_{12}s_{23} - s_{12}c_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} & c_{23}c_{13}\end{pmatrix},\qquad
J_{\mathrm{CP}} = c_{12}s_{12}c_{23}s_{23}c_{13}^2s_{13}\sin\delta_{\mathrm{CP}}
\end{aligned}''', 'STANDARD', ['neutrinos', 'quarks'],
  'Inputs: the NuFIT 6.0 values for the PMNS matrix and the PDG values for the CKM matrix (the same form); unitary to 1.1e-16.',
  name='pmns')

E('FE', 'The spectrum of dirac16complex on the static block', r'''
\begin{aligned}
&\text{even: }\chi = \big(\mathrm{e}^{c_\Psi\xi},\ 0\big)^T,\ \varepsilon = 0\ \text{(all eight blocks)},\qquad
 \varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi_n}{fL}\Big)^2},\ \varpi_n = \pi,\ 2\pi,\ \dots;\\
&\text{odd: }\varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2},\quad \tan\varpi = -\frac{\varpi}{c_\Psi};\qquad
 c_\Psi = f\,m_\Psi L;\qquad \text{fold band: }\varepsilon = \mathrm{e}^{-a_4}\lvert k\rvert
\end{aligned}''', 'DERIVED', ['dirac16complex Psi'],
  'Exact; at the stabilised block c_Psi = 0.646667, the lowest odd level (the dark matter) is 3.102204 m_Psi = 44.35 TeV '
  '(varpi = 1.89901) and the lowest even bulk level 4.959981 m_Psi.', name='psi_spectrum')
