from build_lib import R

# ------------------------------------------------------------------ x0 eigenvalue problems of the bosons
R('Fprof', r'F(\xi),\ F_n', ['F'], r'The $x_0$ profile of a boson mode on one half of the period (a function of $y$ or of '
  r'$\xi = y/L$): of a gauge field (gauge $A_y = 0$) or of the transverse-traceless graviton; $F_n$ is the profile of the '
  r'$n$-th Kaluza-Klein level of the graviton tower ($F_0 = 1$ the flat zero mode).', 'dimensionless', status='DERIVED')
R('Ftilde', r'\tilde F', [r'\tilde F'], r'The rescaled boson profile, $F = \mathrm{e}^{-3HL\xi/2}\tilde F$.', 'dimensionless',
  status='DERIVED')
R('mmass', r'm,\ m_s,\ m_i', ['m'], r'A four-dimensional mass: $m$ the mass of a mode (the eigenvalue of an $x_0$ problem) or of '
  r'a fermion; $m_s$ the mass of the species $s$; $m_i$ the mass of the neutrino mass state $i$.', 'GeV', status='DERIVED')
R('mtilde', r'\tilde m,\ \tilde m_n', [r'\tilde m', r'\tilde m_1'], r'The dimensionless $x_0$ eigenvalue of a boson mode, '
  r'$\tilde m = m\,fL$; $\tilde m_n$ the $n$-th even Kaluza-Klein level of the tower with $\beta = 0$ ($\tilde m_1$ the first).',
  'dimensionless', r'$\tilde m_1^2 = 30.1196$, $\tilde m_2^2 = 59.7284$, $\tilde m_3^2 = 109.0764$ ($HL = 3$), i.e. $\tilde m_1 = 5.48813$, $\tilde m_2 = 7.72842$, $\tilde m_3 = 10.44397$', 'DERIVED')
R('mtildeW', r'\tilde m_{\mathrm{W}}', [r'\tilde m_{\mathrm{W}}'], r'The dimensionless $x_0$ eigenvalue of the lowest $W^\pm$ '
  r'mode ($\beta = \beta_{\mathrm{W}}$).', 'dimensionless', r'$\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$', 'DERIVED')
R('mtildeZ', r'\tilde m_{\mathrm{Z}}', [r'\tilde m_{\mathrm{Z}}'], r'The dimensionless $x_0$ eigenvalue of the lowest $Z$ mode '
  r'($\beta = \beta_{\mathrm{Z}}$).', 'dimensionless', r'$\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$', 'DERIVED')
R('betaRobin', r'\beta', [r'\beta'], r'The Robin parameter of the tip condition of a boson profile, '
  r'$\mathrm{d}F/\mathrm{d}\xi = \beta F$ at $\xi = -1$ (zero for the massless gauge fields and the graviton).',
  'dimensionless', status='DERIVED')
R('betaW', r'\beta_{\mathrm{W}}', [r'\beta_{\mathrm{W}}'], r'The Robin parameter of $W^+$ and $W^-$ (set by the tip mass term of '
  r'the sigma field).', 'dimensionless', '0.011912 (fitted)', 'DERIVED')
R('betaZ', r'\beta_{\mathrm{Z}}', [r'\beta_{\mathrm{Z}}'], r'The Robin parameter of the $Z$, '
  r'$\beta_{\mathrm{Z}} = \beta_{\mathrm{W}}/\cos^2\theta_{\mathrm{W}}$.', 'dimensionless', '0.015343', 'DERIVED')
R('varpi', r'\varpi,\ \varpi_n', [r'\varpi'], r'The wave number of an oscillating $x_0$ profile on $-1 \le \xi \le 0$ (of a '
  r'boson after the rescaling, or of a bulk level of dirac16complex); $\varpi_n$ that of the $n$-th even level '
  r'($\varpi_n = n\pi$ for $\beta = 0$).', 'dimensionless', r'1.89901 for the lowest odd level of dirac16complex', 'DERIVED')
R('mKK', r'm^{\mathrm{KK}}_n,\ m_{\mathrm{KK}}', [r'm^{\mathrm{KK}}', r'm_{\mathrm{KK}}'], r'The mass of the $n$-th '
  r'Kaluza-Klein graviton (and gauge) level, $m^{\mathrm{KK}}_n = \tilde m_n/(fL)$; $m_{\mathrm{KK}} = m^{\mathrm{KK}}_1$ is the '
  r'Kaluza-Klein scale.', 'GeV', r'$m_{\mathrm{KK}} = 121.32$ TeV', 'DERIVED')
R('Nnorm', r'N_n,\ N_0', ['N', r'N_0'], r'The normalisation integral of the profile $F_n$ of the $n$-th Kaluza-Klein level, '
  r'$N_n = \int_{-1}^{0}\mathrm{e}^{3HL\xi}F_n^2\,\mathrm{d}\xi$; $N_0$ that of the flat zero mode.', 'dimensionless',
  r'$N_0 = (1 - \mathrm{e}^{-3HL})/(3HL) = 0.1111$', 'DERIVED')
R('VN', r'V_{\mathrm{N}}(r)', [r'V_{\mathrm{N}}'], r'The potential energy of two static masses at the distance $r$ (Newton '
  r'potential with the Kaluza-Klein corrections).', 'GeV', status='DERIVED')
R('M12', r'M_1,\ M_2', [r'M_1', r'M_2'], r'The masses of the two static sources in the potential $V_{\mathrm{N}}$.', 'GeV',
  status='STANDARD')
R('rdist', r'r', ['r'], r'A distance: between the two masses in $V_{\mathrm{N}}(r)$, from the centre of the star in the '
  r'adiabaticity condition.', 'length', status='STANDARD')
R('calA', r'\mathcal{A}_n', [r'\mathcal{A}'], r'The relative strength of the Yukawa force of the $n$-th Kaluza-Klein graviton '
  r'between two sources with the profiles $\varrho_1$, $\varrho_2$.', 'dimensionless',
  r'0.0904, 0.0136, 0.0057 ($n = 1, 2, 3$, two quark-doublet profiles)', 'DERIVED')
R('varrho12', r'\varrho_1,\ \varrho_2', [r'\varrho_1', r'\varrho_2'], r'The $x_0$ profiles of the two sources of '
  r'$V_{\mathrm{N}}$ as probability densities in $\xi$ ($\int_{-1}^{0}\varrho_1\,\mathrm{d}\xi = 1$): $L$ times the profile '
  r'$\varrho_f$ of the zero mode of each source.', 'dimensionless', status='DERIVED')
R('rhoEW', r'\rho_{\mathrm{EW}}', [r'\rho_{\mathrm{EW}}'], r'The electroweak parameter, '
  r'$\rho_{\mathrm{EW}} = \tilde m_{\mathrm{W}}^2/(\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$.', 'dimensionless',
  status='DERIVED')
R('rhoEW0', r'\rho_{\mathrm{EW},0}', [r'\rho_{\mathrm{EW},0}'], r'The measured value of the electroweak parameter (PDG fit).',
  'dimensionless', r'$1.00038$', 'STANDARD')
R('mW', r'm_{\mathrm{W}}', [r'm_{\mathrm{W}}'], r'The mass of $W^+$ and $W^-$.', 'GeV', '80.3625 GeV (measured, input)',
  'STANDARD')
R('mZ', r'm_{\mathrm{Z}}', [r'm_{\mathrm{Z}}'], r'The mass of the $Z$.', 'GeV', '91.1879 GeV (reproduced)', 'STANDARD')

# ------------------------------------------------------------------ fermion reduction and zero modes
R('calV', r'\mathcal{V}', [r'\mathcal{V}'], r'The constant $16 \times 2$ matrix of the reduction ansatz that places the '
  r'two-component spinor $\chi$ of one block into the 16 components of the eight-dimensional spinor.', 'dimensionless',
  status='DERIVED')
R('chi', r'\chi,\ \chi_o,\ \chi_1,\ \chi_2', [r'\chi', r'\chi_1', r'\chi_2'], r'The two-component spinor of one block of the '
  r'reduction (a function of $y$ and $x_4$), $\chi = (\chi_1, \chi_2)^T = (a, \mathrm{i}b)^T$; $\chi_o$ the Kohn-Sham orbital $o$, '
  r'normalised as $\int_{-L}^{0}\chi_o^\dagger\chi_o\,\mathrm{d}y = 1$.', 'GeV^(1/2) (normalised orbital)', status='DERIVED')
R('Mfun', r'M(y)', ['M'], r'The mass function of the block Hamiltonian (the scalar potential): $M = \mu_{\psi i}$ for a '
  r'Standard-Model fermion, $M = M_{\mathrm{eff}}$ for dirac16complex.', 'GeV', status='DERIVED')
R('vpot', r'v(y)', ['v'], r'The vector potential of the block Hamiltonian (the mean field along $\gamma^{x_4}$): for '
  r'dirac16complex the contact term and the mean field of I11; zero for a Standard-Model fermion.', 'GeV', status='DERIVED')
R('vb', r'v_{\mathrm{b}}(y)', [r'v_{\mathrm{b}}'], r'The mean field of I13 (baryon densities), acting on the lower component '
  r'of $\chi$ only.', 'GeV', status='DERIVED')
R('hblock', r'h', ['h'], r'The block Hamiltonian: the $2 \times 2$ differential operator of one block that generates the time '
  r'evolution of $\chi$, $\mathrm{i}\,\partial_{x_4}\chi = h\chi$; its eigenvalues are the energies $\varepsilon$.', 'GeV',
  status='DERIVED')
R('varsigma', r'\varsigma', [r'\varsigma'], r'The first of the three signs $(\varsigma, \varsigma_2, \varsigma_3)$, each $\pm1$, '
  r'that label the eight blocks of the reduction.', 'dimensionless', status='DERIVED')
R('varsigma2', r'\varsigma_2', [r'\varsigma_2'], r'The second sign that labels the blocks ($\pm1$).', 'dimensionless',
  status='DERIVED')
R('sigmaPauli', r'\sigma_1,\ \sigma_2,\ \sigma_3', [r'\sigma_1', r'\sigma_2', r'\sigma_3'], r'The Pauli matrices acting on '
  r'the two components of a block spinor $\chi$ ($\sigma_3 = \mathrm{diag}(1, -1)$).', 'dimensionless', status='STANDARD')
R('kwave', r'k', ['k'], r'The magnitude of the wave vector (the momentum, $\hbar = 1$) of a mode: in the reduction, the Kohn-Sham '
  r'and the perturbation equations the comoving wavenumber (physical momentum $\mathrm{e}^{-a_4}k$); in the thermal integrals '
  r'the momentum of a particle at the time considered (the variable of integration).', 'GeV (1/length)', status='STANDARD')
R('kvec', r'\vec k,\ \vec k_o', [r'\vec k'], r'The wave vector (momentum) in ordinary 3-space; $\vec k_o$ that of the orbital $o$, '
  r'a point of the lattice $k_{\mathrm{lat}}\vec n_o$.', 'GeV', status='STANDARD')
R('cloc', r'c,\ c_L,\ c_R', ['c'], r'The localisation of a zero mode, $c = f\mu L$ (bulk mass times the proper depth); $c_L$ of '
  r'a doublet (localised at the fold for $c_L > 0$), $c_R$ of a singlet (localised at the fold for $c_R < 0$).',
  'dimensionless', r'doublets $c_L = 3.38230$ (quarks) and 5.95288 (leptons); singlets $c_R$: up $-15.4300$, down '
  r'$-14.6258$, strange $-11.5158$, charm $-8.7683$, bottom $-7.5005$, top $-3.3823$, electron $-14.5539$, muon $-8.9809$, tau '
  r'$-5.9529$, neutrinos $-35.0452$, $-32.8481$, $-31.0702$ (fixed by the measured masses)', 'DERIVED')
R('cPsi', r'c_\Psi', [r'c_\Psi'], r'The localisation parameter of dirac16complex, $c_\Psi = f\,m_\Psi L$.', 'dimensionless',
  '0.646667 at the stabilised block', 'DERIVED')
R('ab', r'a,\ b', ['a', 'b'], r'The upper and lower components of a block spinor, $\chi = (a, \mathrm{i}b)$, real at $k = 0$: '
  r'$a_L, b_L$ of a doublet and $a_R, b_R$ of a singlet solution ($a_{Ri}$, $b_{Ri}$ of the generation $i$, $b_{L\alpha}$, '
  r'$a_{L\alpha}$ of the doublet in the flavour basis), $a_o, b_o$ of the orbital $o$.', 'GeV^(1/2) (normalised orbital)',
  status='DERIVED')
R('varepsilon', r'\varepsilon,\ \varepsilon_o', [r'\varepsilon'], r'The energy of a fermion mode (an eigenvalue of the block '
  r'Hamiltonian; at $k = 0$ the four-dimensional mass); $\varepsilon_o$ the Kohn-Sham level of the orbital $o$.', 'GeV',
  status='DERIVED')
R('epstilde', r'\tilde\varepsilon', [r'\tilde\varepsilon'], r'The dimensionless energy (mass) of a fermion mode, '
  r'$\tilde\varepsilon = \varepsilon fL$.', 'dimensionless', status='DERIVED')
R('upsilon', r'\upsilon_L,\ \upsilon_R', [r'\upsilon'], r'The auxiliary roots $\upsilon = (c^2 - \tilde\varepsilon^2)^{1/2}$ of '
  r'the doublet ($\upsilon_L$) and singlet ($\upsilon_R$) solutions at $k = 0$.', 'dimensionless', status='DERIVED')
R('calD', r'\mathcal{D}(\tilde\varepsilon)', [r'\mathcal{D}'], r'The mass function of one generation: its zeros are the '
  r'dimensionless masses $\tilde\varepsilon$.', 'dimensionless', status='DERIVED')
R('calZ', r'\mathcal{Z}(c)', [r'\mathcal{Z}'], r'The tip amplitude of a normalised zero mode with the localisation $c$, '
  r'$\mathcal{Z}(c)^2 = c\,\mathrm{e}^{-c}/\sinh c$.', 'dimensionless', status='DERIVED')
R('bsalpha', r'\boldsymbol{\alpha},\ \boldsymbol{\alpha}^{(i)}', [r'\boldsymbol{\alpha}'], r'The vector of the three doublet '
  r'amplitudes at the tip in the mass condition of three generations; $\boldsymbol{\alpha}^{(i)}$ its null vector for the mass '
  r'state $i$ (the left-handed flavour content).', 'dimensionless', status='DERIVED')
R('bsbeta', r'\boldsymbol{\beta}^{(i)}', [r'\boldsymbol{\beta}'], r'The vector of the three singlet amplitudes of the mass '
  r'state $i$.', 'dimensionless', status='DERIVED')
R('bfu', r'\mathbf{u}_i', [r'\mathbf{u}'], r'The unit vector of the generation $i$ (the $i$-th column of the $3 \times 3$ '
  r'identity).', 'dimensionless', status='STANDARD')
R('Upmns', r'U', ['U', r'U_{\mu3}', r'U_{\mu2}'], r'The PMNS matrix, the unitary $3 \times 3$ mixing matrix of the leptons, '
  r'$\nu_\alpha = \sum_iU_{\alpha i}\nu_i$ (rows $\alpha = e, \mu, \tau$, columns the mass states $i$); in UM-2 '
  r'$U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$.', 'dimensionless',
  r'$\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$, '
  r'$\delta_{\mathrm{CP}} = 212^\circ$ (NuFIT 6.0)', 'STANDARD')
R('VCKM', r'V_{\mathrm{CKM}}', [r'V_{\mathrm{CKM}}'], r'The CKM matrix, the unitary $3 \times 3$ mixing matrix of the quarks '
  r'(the same parametrisation as $U$); in UM-2 $V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d$.', 'dimensionless',
  r'$s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$, $\delta = 1.147$ (PDG)', 'STANDARD')
R('cij', r'c_{12},\ c_{13},\ c_{23}', [r'c_{12}', r'c_{13}', r'c_{23}'], r'The cosines of the mixing angles, '
  r'$c_{ij} = \cos\theta_{ij}$.', 'dimensionless', status='STANDARD')
R('sij', r's_{12},\ s_{13},\ s_{23}', [r's_{12}', r's_{13}', r's_{23}'], r'The sines of the mixing angles, '
  r'$s_{ij} = \sin\theta_{ij}$.', 'dimensionless', status='STANDARD')
R('deltaCP', r'\delta_{\mathrm{CP}}', [r'\delta_{\mathrm{CP}}'], r'The CP-violating phase of a mixing matrix.', 'dimensionless',
  r'$212^\circ$ (PMNS), 1.147 rad (CKM)', 'STANDARD')
R('JCP', r'J_{\mathrm{CP}}', [r'J_{\mathrm{CP}}'], r'The Jarlskog invariant of a mixing matrix (the measure of CP violation).',
  'dimensionless', r'$-0.01777$ (PMNS), $3.117\times10^{-5}$ (CKM)', 'STANDARD')

# ------------------------------------------------------------------ Kohn-Sham theory
R('Meff', r'M_{\mathrm{eff}}(y)', [r'M_{\mathrm{eff}}'], r'The effective (scalar) mass field of the Kohn-Sham Hamiltonian: '
  r'$m_\Psi$ plus the mean fields of the contact term and of I12.', 'GeV', status='DERIVED')
R('nsc', r'n^{\mathrm{sc}},\ n^{\mathrm{sc}}_o', [r'n^{\mathrm{sc}}'], r'The scalar density of dirac16complex (the '
  r'Kohn-Sham expectation of $\bar\Psi\Psi$, per proper 7-volume) and $n^{\mathrm{sc}}_o$ the contribution of the orbital $o$.',
  'GeV^7', status='RECORD')
R('nt', r'n^{\mathrm{t}}_o', [r'n^{\mathrm{t}}'], r'The density of the orbital $o$ along the momentum term '
  r'($\chi_o^\dagger\varsigma\sigma_3\chi_o$ times the weight $\mathrm{e}^{-3Hy}/\mathrm{Vol}_7$); it carries the 3-space pressure.',
  'GeV^7', status='RECORD')
R('ndens', r'n,\ n_o,\ n_{\psi i},\ n_f,\ n_i', ['n'], r'A number density: $n(y)$ the particle density of dirac16complex in '
  r'the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model '
  r'fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that '
  r'of the neutrino mass state $i$ (per 3-volume of four dimensions).', 'GeV^7 (eight dimensions), GeV^3 (four dimensions)',
  status='STANDARD')
R('ddeg', r'd_o,\ d_s', ['d'], r'A degeneracy: $d_o = 4r_3(\lvert\vec n_o\rvert^2)$ the number of states of the momentum shell of '
  r'the orbital $o$; $d_s$ the number of internal states (spin, colour, particle and antiparticle) of the species $s$.',
  'dimensionless', status='STANDARD')
R('phiocc', r'\phi_o', [r'\phi'], r'The occupation of the Kohn-Sham orbital $o$ (Fermi-Dirac for the Mermin functional, 0 or 1 '
  r'for the aufbau).', 'dimensionless', status='RECORD')
R('Vol7', r'\mathrm{Vol}_7', [r'\mathrm{Vol}_7'], r'The normalisation volume of a Kohn-Sham cell, '
  r'$\mathrm{Vol}_7 = (2\pi/k_{\mathrm{lat}})^3v_{\mathrm{t}}f^4$ (the proper seven-volume of a cell is '
  r'$2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$).', 'GeV^-6', r'34.27 in units $H = 1$, $v_{\mathrm{t}} = 1$, $f = f_*$',
  'RECORD')
R('r3', r'r_3', [r'r_3'], r'The number of representations of an integer as an ordered sum of three squares of integers '
  r'(signs counted).', 'dimensionless', status='STANDARD')
R('nvec', r'\vec n_o', [r'\vec n'], r'The integer lattice vector of the momentum shell of the orbital $o$ '
  r'($\vec n \in \mathbb{Z}^3$).', 'dimensionless', status='RECORD')
R('klat', r'k_{\mathrm{lat}}', [r'k_{\mathrm{lat}}'], r'The spacing of the momentum lattice of the Kohn-Sham cell.', 'GeV',
  r'$0.25\,H$', 'RECORD')
R('muchem', r'\mu_{\mathrm{chem}}', [r'\mu_{\mathrm{chem}}'], r'The chemical potential of the Mermin occupations.', 'GeV',
  status='RECORD')
R('Temp', r'T', ['T'], r'The temperature of the plasma (of the photons and of every species in equilibrium with them); in the '
  r'Mermin occupations the temperature of the Kohn-Sham state.', 'GeV', status='STANDARD')
R('EKS', r'E_{\mathrm{KS}}', [r'E_{\mathrm{KS}}'], r'The Kohn-Sham energy of a cell.', 'GeV', status='RECORD')
R('eint', r'e_{\mathrm{int}}', [r'e_{\mathrm{int}}'], r'The interaction energy density of the contact term in the Kohn-Sham '
  r'energy and energy-momentum tensor.', 'GeV^8', status='RECORD')

# ------------------------------------------------------------------ the portals on the zero modes
R('L4', r'\mathcal{L}_4', [r'\mathcal{L}_4'], r'The four-dimensional contact Lagrangian of I11 and I13 between a state $o$ of '
  r'dirac16complex and a Standard-Model fermion component $f$.', 'GeV^4', status='DERIVED')
R('L4I12', r'\mathcal{L}_4^{\mathrm{I12}}', [r'\mathcal{L}_4^{\mathrm{I12}}'], r'The four-dimensional Lagrangian of I12 on the '
  r'dark matter.', 'GeV^4', status='DERIVED')
R('L4lam', r'\mathcal{L}_4^{\lambda}', [r'\mathcal{L}_4^{\lambda}'], r'The four-dimensional term of the contact self-interaction '
  r'that couples a dark-matter pair to a fold-band pair.', 'GeV^4', status='ESTIMATE')
R('GV', r'G_{\mathrm{V}}', [r'G_{\mathrm{V}}'], r'The four-dimensional strength of the vector portal I11 on the zero modes, '
  r'$G_{\mathrm{V}} = c_{\mathrm{V}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$.', 'GeV^-2',
  r'benchmark $4.38\times10^{-17}$ GeV$^{-2}$ ($\Delta N_{\mathrm{eff}} = 0.001$)', 'DERIVED')
R('GA', r'G_{\mathrm{A}}', [r'G_{\mathrm{A}}'], r'The four-dimensional strength of the portal I13 on the zero modes, '
  r'$G_{\mathrm{A}} = c_{\mathrm{A}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$.', 'GeV^-2',
  r'$1.278\times10^{-9}$ GeV$^{-2}$ (dark-matter relic density)', 'DERIVED')
R('tildeI', r'\tilde I_{of}', [r'\tilde I', r'\tilde I_Q', r'\tilde I_{u_R}', r'\tilde I_{d_R}', r'\tilde I_\ell',
                                  r'\tilde I_{e_R}', r'\tilde I_{\nu_R,i}'],
  r'The overlap of the state $o$ of dirac16complex with the zero mode of the fermion component $f$, '
  r'$\tilde I_{of} = H^{-1}\int_{-L}^{0}(a_o^2 + b_o^2)\varrho_f\mathrm{e}^{-3Hy}\mathrm{d}y$ (the integral in units of $H$); $\tilde I_Q$, '
  r'$\tilde I_{u_R}$, $\tilde I_{d_R}$, $\tilde I_\ell$, $\tilde I_{e_R}$ those of the dark matter with $Q$, $u_R$, $d_R$, '
  r'$\ell$, $e_R$, $\tilde I_{\nu_R,i}$ with the right-handed neutrino of the generation $i$.', 'dimensionless',
  r'dark matter: $\tilde I_Q = 8.2722$, $\tilde I_\ell = 1.2524$, $\tilde I_{u_R} = 0.3854$, $\tilde I_{d_R} = 0.3961$, '
  r'$\tilde I_{e_R} = 0.3972$', 'DERIVED')
R('tildeIb', r'\tilde I^{(b)}_{of}', [r'\tilde I^{(b)}', r'\tilde I^{(b)}_Q', r'\tilde I^{(b)}_{u_R}', r'\tilde I^{(b)}_{d_R}',
                                        r'\tilde I^{(b)}_{\nu_R}'],
  r'The overlap of the lower component of the state $o$ with the zero mode of $f$, '
  r'$\tilde I^{(b)}_{of} = H^{-1}\int_{-L}^{0}b_o^2\varrho_f\mathrm{e}^{-3Hy}\mathrm{d}y$ (the overlap of I13); $\tilde I^{(b)}_Q$, '
  r'$\tilde I^{(b)}_{u_R}$, $\tilde I^{(b)}_{d_R}$, $\tilde I^{(b)}_{\nu_R}$ those of the dark matter.',
  'dimensionless', r'dark matter: $\tilde I^{(b)}_Q = 2.6135$', 'DERIVED')
R('varrho', r'\varrho_f(y),\ \varrho(y; c)', [r'\varrho'], r'The $x_0$ profile of a zero mode as a probability density on one '
  r'half, $\int_{-L}^{0}\varrho\,\mathrm{d}y = 1$: $\varrho_f$ that of the fermion component $f$, $\varrho(y; c)$ its form for '
  r'the localisation $c$.', '1/length (GeV)', status='DERIVED')
R('Gg', r'G_{\mathrm{g}}', [r'G_{\mathrm{g}}'], r'The coupling of a dark-matter pair to canonically normalised gluon pairs through '
  r'I12.', 'GeV^-3', r'$6.09\times10^{-15}$ GeV$^{-3}$ (benchmark)', 'DERIVED')
R('GW', r'G_{\mathrm{W}}', [r'G_{\mathrm{W}}'], r'The coupling of a dark-matter pair to canonically normalised SU(2) gauge pairs '
  r'through I12.', 'GeV^-3', r'$2.96\times10^{-15}$ GeV$^{-3}$', 'DERIVED')
R('GB', r'G_{\mathrm{B}}', [r'G_{\mathrm{B}}'], r'The coupling of a dark-matter pair to canonically normalised hypercharge pairs '
  r'through I12.', 'GeV^-3', r'$1.08\times10^{-15}$ GeV$^{-3}$', 'DERIVED')
R('calO', r'\mathcal{O}_o,\ \mathcal{O}_{\mathrm{DM}}', [r'\mathcal{O}', r'\mathcal{O}_{\mathrm{DM}}'], r'The scalar overlap of '
  r'a state of dirac16complex, $\mathcal{O}_o = \partial\varepsilon_o/\partial m_\Psi$ (Hellmann-Feynman: the integrated scalar '
  r'density of the orbital); $\mathcal{O}_{\mathrm{DM}}$ that of the dark matter.', 'dimensionless',
  r'$\mathcal{O}_{\mathrm{DM}} = 0.7072$', 'DERIVED')
R('epsDM', r'\varepsilon_{\mathrm{DM}}', [r'\varepsilon_{\mathrm{DM}}'], r'The energy of the dark-matter level at rest (its mass '
  r'$M_{\mathrm{DM}}$ on the static block).', 'GeV', r'$3.102204\,m_\Psi = 44.35$ TeV', 'DERIVED')
R('epsI1113', r'\Delta\varepsilon_{\mathrm{I11}},\ \Delta\varepsilon_{\mathrm{I13}}',
  [r'\varepsilon_{\mathrm{I11}}', r'\varepsilon_{\mathrm{I13}}'], r'The shifts of the dark-matter level by the mean fields of '
  r'I11 and of I13 in matter.', 'GeV', r'at most $8.2\times10^{-10}$ GeV (I13, at the freeze-out)', 'DERIVED')
R('nquark', r'n_{\mathrm{u}},\ n_{\mathrm{d}}', [r'n_{\mathrm{u}}', r'n_{\mathrm{d}}'], r'The number densities of up and down '
  r'quarks bound in nucleons, $n_{\mathrm{u}} = 2n_{\mathrm{p}} + n_{\mathrm{n}}$, $n_{\mathrm{d}} = n_{\mathrm{p}} + 2n_{\mathrm{n}}$.',
  'GeV^3', status='STANDARD')
R('np', r'n_{\mathrm{p}}', [r'n_{\mathrm{p}}'], r'The number density of protons (free and bound).', 'GeV^3',
  status='STANDARD')
R('nn', r'n_{\mathrm{n}}', [r'n_{\mathrm{n}}'], r'The number density of neutrons (free and bound).', 'GeV^3',
  status='STANDARD')
R('ne', r'n_{\mathrm{e}}', [r'n_{\mathrm{e}}'], r'The number density of electrons (net of positrons); in the Thomson terms of '
  r'the photon and baryon equations only free (ionised) electrons count.', 'GeV^3', status='STANDARD')

# ------------------------------------------------------------------ condensates, QCD and the electroweak plasma
R('alpha3', r'\alpha_3', [r'\alpha_3'], r'The strong fine-structure constant, $\alpha_3 = g_3^2/(4\pi)$, at the scale given in '
  r'brackets.', 'dimensionless', r'$\alpha_3(m_{\mathrm{Z}}) = 0.1180$; $\alpha_3(m_{\mathrm{KK}}) = 0.0606$', 'STANDARD')
R('alpha2', r'\alpha_2', [r'\alpha_2'], r'The SU(2) fine-structure constant, $\alpha_2 = g_2^2/(4\pi)$.', 'dimensionless',
  status='STANDARD')
R('alpha1', r'\alpha_1', [r'\alpha_1'], r'The hypercharge fine-structure constant, $\alpha_1 = g_1^2/(4\pi)$.', 'dimensionless',
  status='STANDARD')
R('alphaG', r'\alpha_{\mathrm{G}}', [r'\alpha_{\mathrm{G}}'], r'The fine-structure constant of the gauge group G (one of '
  r'$\alpha_3$, $\alpha_2$, $\alpha_1$).', 'dimensionless', status='STANDARD')
R('alphaem', r'\alpha_{\mathrm{em}}', [r'\alpha_{\mathrm{em}}'], r'The electromagnetic fine-structure constant '
  r'($\overline{\mathrm{MS}}$, at $m_{\mathrm{Z}}$).', 'dimensionless', r'$1/127.95$', 'STANDARD')
R('bcoef', r'b_3,\ b_2,\ b_1,\ b_{\mathrm{G}}', [r'b_3', r'b_2', r'b_1', r'b_{\mathrm{G}}'], r'The one-loop coefficients of the '
  r'running couplings, $\mathrm{d}\alpha/\mathrm{d}\ln\mu_{\mathrm{ren}} = -b\,\alpha^2/(2\pi)$: $b_3 = 11 - \frac23N_{\mathrm{f}}$ '
  r'(SU(3)), $b_2 = \frac{10}{3}$ (SU(2) without a Higgs particle), $b_1 = -\frac{20}{3}$ (U(1)$_Y$), $b_{\mathrm{G}}$ that of '
  r'the group G (not related to the metric function $b_4$).', 'dimensionless', status='STANDARD')
R('Nf', r'N_{\mathrm{f}}', [r'N_{\mathrm{f}}'], r'The number of active quark flavours (quarks lighter than the scale).',
  'dimensionless', status='STANDARD')
R('Theta', r'\Theta_{\mathrm{QCD}},\ \Theta_{\mathrm{G}},\ \Theta_V',
  [r'\Theta_{\mathrm{QCD}}', r'\Theta_{\mathrm{G}}', r'\Theta_V', r'\Theta_{\mathrm{W}}', r'\Theta_{\mathrm{Z}}'],
  r'The trace $\rho - 3p$ of the energy-momentum tensor (interaction measure) of a plasma component: $\Theta_{\mathrm{QCD}}$ of '
  r'the quark-gluon plasma or hadron gas, $\Theta_{\mathrm{G}}$ of the gauge plasma of the group G, $\Theta_V$ of the thermal gas '
  r'of the massive vector $V$ ($\Theta_{\mathrm{W}}$ of $W^\pm$, $\Theta_{\mathrm{Z}}$ of $Z$).', 'GeV^4', status='STANDARD')
R('pQCD', r'p_{\mathrm{QCD}}', [r'p_{\mathrm{QCD}}'], r'The pressure of the quark-gluon plasma (leading orders).', 'GeV^4',
  status='ESTIMATE')
R('FV', r'F^V_{\mu\nu}', [r'F^V'], r'The field strength of the canonically normalised massive vector $V = W^\pm$ or $Z$, '
  r'$F^V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$.', 'GeV^2', status='STANDARD')
R('Fgeo', r'F_{\mathrm{geo}}', [r'F_{\mathrm{geo}}'], r'The field strength of the gauge group G in geometric normalisation; '
  r'$\langle F_{\mathrm{geo}}^2\rangle$ is its condensate ($G^A_{\mu\nu}G^{A\mu\nu}$, $W^I_{\mu\nu}W^{I\mu\nu}$ or '
  r'$B_{\mu\nu}B^{\mu\nu}$).', 'GeV^2', status='STANDARD')
R('gG', r'g_{\mathrm{G}}', [r'g_{\mathrm{G}}'], r'The four-dimensional coupling of the gauge group G (one of $g_3$, $g_2$, $g_1$).',
  'dimensionless', status='STANDARD')
R('palpha', r'p_{\alpha,\mathrm{G}},\ p_{\alpha,2},\ p_{\alpha,1}', [r'p_{\alpha,\mathrm{G}}', r'p_{\alpha,2}', r'p_{\alpha,1}'],
  r'The order-$\alpha$ (interaction) part of the pressure of the gauge plasma of the group G; $p_{\alpha,2}$ of SU(2), '
  r'$p_{\alpha,1}$ of U(1)$_Y$.', 'GeV^4', status='STANDARD')
R('dadj', r'd_{\mathrm{adj}}', [r'd_{\mathrm{adj}}'], r'The dimension of the adjoint representation of the gauge group (8, 3, 1).',
  'dimensionless', status='STANDARD')
R('Cadj', r'C_{\mathrm{adj}}', [r'C_{\mathrm{adj}}'], r'The quadratic Casimir of the adjoint representation (3, 2, 0).',
  'dimensionless', status='STANDARD')
R('TF', r'T_{\mathrm{F}}', [r'T_{\mathrm{F}}'], r'The Dynkin index of the fermion representation ($\frac12$ per Dirac '
  r'fundamental; for U(1)$_Y$ the sum of the squared hypercharges).', 'dimensionless', status='STANDARD')
R('mu_ren', r'\mu_{\mathrm{ren}}', [r'\mu_{\mathrm{ren}}'], r'The renormalisation scale of a running coupling (taken as '
  r'$2\pi T$ for the condensates of a plasma).', 'GeV', status='STANDARD')
R('thetaMS', r'\theta_{\overline{\mathrm{MS}}}', [r'\theta_{\overline{\mathrm{MS}}}'], r'The weak mixing angle in the '
  r'$\overline{\mathrm{MS}}$ scheme at $m_{\mathrm{Z}}$.', 'dimensionless',
  r'$\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$', 'STANDARD')
R('Upsilon', r'\Upsilon(\xi)', [r'\Upsilon'], r'The factor by which the scalar density of the dark matter changes the gauge '
  r'kinetic term along $x_0$ (I12), $\Upsilon = 1 + A_{\mathrm{mf}}n^{\mathrm{sc}}_{\mathrm{DM}}$.', 'dimensionless',
  status='DERIVED')
R('Amf', r'A_{\mathrm{mf}}', [r'A_{\mathrm{mf}}'], r'The amplitude of the I12 mean field in the $x_0$ problem of the gauge '
  r'fields (a bookkeeping parameter: the result is linear in it).', 'GeV^-1 (with the orbital normalisation)',
  status='DERIVED')
R('nscDM', r'n^{\mathrm{sc}}_{\mathrm{DM}}', [r'n^{\mathrm{sc}}_{\mathrm{DM}}'], r'The scalar density of the dark-matter orbital, '
  r'$n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}}$.', 'GeV (normalised orbital)', status='DERIVED')
R('abDM', r'a_{\mathrm{DM}},\ b_{\mathrm{DM}}', [r'a_{\mathrm{DM}}', r'b_{\mathrm{DM}}'], r'The upper and lower components of '
  r'the dark-matter orbital (block spinor $(a, \mathrm{i}b)$, normalised on one half).', 'GeV^(1/2)', status='DERIVED')
R('nDM', r'n_{\mathrm{DM}},\ \bar n_{\mathrm{DM}}', [r'n_{\mathrm{DM}}', r'\bar n_{\mathrm{DM}}'], r'The number densities of '
  r'dark-matter particles and antiparticles of one species.', 'GeV^3', status='STANDARD')
R('nDMtot', r'n_{\mathrm{DM,tot}}', [r'n_{\mathrm{DM,tot}}'], r'The total number density of dark-matter quanta: both species '
  r'(the lowest odd levels of $\Psi_A$ and $\Psi_B$), particles and antiparticles, '
  r'$n_{\mathrm{DM,tot}} = 2(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}})$.', 'GeV^3', status='STANDARD')
R('rhoQCDscale', r'\Lambda_{\mathrm{QCD}}^{(N_{\mathrm{f}})}', [r'\Lambda_{\mathrm{QCD}}',
                                                               r'\Lambda_{\mathrm{QCD}}^{(N_{\mathrm{f}})}'],
  r'The QCD scale with $N_{\mathrm{f}}$ active flavours ($\Lambda_{\mathrm{QCD}}^{(6)}$, $^{(5)}$, $^{(4)}$, $^{(3)}$), defined '
  r'by the one-loop running.', 'GeV', status='STANDARD')
R('mquarks', r'm_{\mathrm{u}},\ m_{\mathrm{d}},\ m_{\mathrm{s}},\ m_{\mathrm{c}},\ m_{\mathrm{b}},\ m_{\mathrm{t}}',
  [r'm_{\mathrm{u}}', r'm_{\mathrm{d}}', r'm_{\mathrm{s}}', r'm_{\mathrm{c}}', r'm_{\mathrm{b}}', r'm_{\mathrm{t}}'],
  r'The masses of the up, down, strange, charm, bottom and top quarks (the upright subscript names the quark).', 'GeV',
  r'2.16 MeV, 4.70 MeV, 93.5 MeV, 1.273 GeV, 4.183 GeV, 172.56 GeV (the $x_0$ masses, fitted to the PDG values)', 'DERIVED')
R('mnucleon', r'm_{\mathrm{p}},\ m_{\mathrm{n}}', [r'm_{\mathrm{p}}', r'm_{\mathrm{n}}'], r'The masses of the proton and the '
  r'neutron.', 'GeV', r'0.938272 GeV, 0.939565 GeV', 'STANDARD')
R('sigmapiN', r'\sigma_{\pi N}', [r'\sigma_{\pi N}'], r'The pion-nucleon sigma term (the contribution of the up and down quark '
  r'masses to the nucleon mass).', 'GeV', '45 MeV', 'STANDARD')
R('sigmas', r'\sigma_{\mathrm{s}}', [r'\sigma_{\mathrm{s}}'], r'The strange sigma term of the nucleon.', 'GeV', '40 MeV',
  'STANDARD')
R('etab', r'\eta_{\mathrm{b}}', [r'\eta_{\mathrm{b}}'], r'The ratio of the baryon density to the photon density.',
  'dimensionless', r'$6.1\times10^{-10}$', 'STANDARD')
R('ngamma', r'n_\gamma', [r'n_\gamma'], r'The number density of photons.', 'GeV^3', status='STANDARD')
R('MDM', r'M_{\mathrm{DM}}', [r'M_{\mathrm{DM}}'], r'The mass of a dark-matter particle (the lowest odd level of dirac16complex).',
  'GeV', '44.35 TeV', 'DERIVED')
