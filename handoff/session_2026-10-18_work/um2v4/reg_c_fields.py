from build_lib import R

# ------------------------------------------------------------------ dirac16complex and the Clifford algebra
R('Psi', r'\Psi,\ \bar\Psi', [r'\Psi', r'\bar\Psi'], r'dirac16complex: the 16-component complex spinor field of eight '
  r"dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless "
  r'fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint.', 'GeV^(7/2)', status='RECORD')
R('PsiAB', r'\Psi_A,\ \Psi_B', [r'\Psi_A', r'\Psi_B'], r'The two halves of dirac16complex, $\Psi = \Psi_A + \Psi_B$, the '
  r'eigenspaces of $\mathcal{B}$ with the eigenvalues $-1$ and $+1$; each half carries one dark-matter species.', 'GeV^(7/2)',
  status='AUTHOR')
R('PsiDM', r'\Psi_{\mathrm{DM}},\ \bar\Psi_{\mathrm{DM}}', [r'\Psi_{\mathrm{DM}}', r'\bar\Psi_{\mathrm{DM}}'], r'The '
  r'four-dimensional field of a dark-matter quantum (the lowest odd level of dirac16complex on the static block, in either '
  r'half) and its Dirac adjoint.', 'GeV^(3/2)', status='DERIVED')
R('Psifold', r'\Psi_{\mathrm{fold}},\ \bar\Psi_{\mathrm{fold}}', [r'\Psi_{\mathrm{fold}}', r'\bar\Psi_{\mathrm{fold}}'],
  r'The four-dimensional field of a fold-band quantum (an even zero mode of dirac16complex, massless) and its Dirac adjoint.',
  'GeV^(3/2)', status='DERIVED')
R('mPsi', r'm_\Psi', [r'm_\Psi'], r'The mass parameter of dirac16complex, $m_\Psi = 3H\mathcal{M} = H$.', 'GeV', '14.296 TeV',
  'RECORD')
R('calM', r'\mathcal{M}', [r'\mathcal{M}'], r"The record's dimensionless mass parameter of dirac16complex, "
  r'$\mathcal{M} = 1/3$ ($m_\Psi = 3H\mathcal{M}$).', 'dimensionless', '1/3', 'RECORD')
R('lambda', r'\lambda', [r'\lambda'], r'The contact self-coupling of dirac16complex (the term '
  r'$-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of the record).', 'GeV^-6',
  r'not fixed; Kohn-Sham states computed for $\lambda = 0$ and $\pm7\times10^{-5}H^{-6}$; the fold-band radiation requires '
  r'$\lvert\lambda\rvert \lesssim 1.4\times10^{-10}H^{-6}$ (for $\Delta N_{\mathrm{eff}} \le 0.001$)', 'RECORD')
R('gamma', r'\gamma^a,\ \gamma^M,\ \gamma^\mu', [r'\gamma'], r'The Dirac matrices: $\gamma^a$ with a frame index are the '
  r"author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ "
  r'along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; '
  r'$\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas.', 'dimensionless',
  status='AUTHOR')
R('eta', r'\eta_{ab}', [r'\eta'], r'The flat metric of the frame, $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ '
  r'($\eta^{ab}$ the same matrix).', 'dimensionless', status='AUTHOR')
R('vielbein', r'\mathbf{e}^a{}_M,\ \mathbf{e}_a{}^M', [r'\mathbf{e}'], r'The vielbein (frame field) of the metric: '
  r'$g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is the inverse matrix.', 'dimensionless',
  status='STANDARD')
R('Cmat', r'C', ['C'], r'The matrix of the Dirac adjoint, $C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ '
  r'($\bar\Psi = \Psi^\dagger C$); in each block of the reduction $C = \varsigma_2\sigma_2$.', 'dimensionless',
  status='AUTHOR')
R('Gamma4', r'\Gamma_4', [r'\Gamma_4'], r'The four-dimensional chirality matrix, '
  r'$\Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4}$; a doublet zero mode has $\Gamma_4 = +1$ '
  r'(left-handed), a singlet zero mode $\Gamma_4 = -1$ (right-handed).', 'dimensionless', status='DERIVED')
R('calB', r'\mathcal{B}', [r'\mathcal{B}'], r"The author's operator $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$; its eigenvalues "
  r'$\mp1$ define the halves $\Psi_A$ and $\Psi_B$, and it commutes with every interaction of the good sector.',
  'dimensionless', status='AUTHOR')
R('Dcov', r'D_M,\ D_\mu', ['D'], r'The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a '
  r'Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields.',
  '1/length', status='STANDARD')
R('Omega', r'\Omega_M', [r'\Omega'], r'The spin connection acting on spinors, the matrix '
  r'$\Omega_M = \frac12\omega_{Mab}\mathcal{S}^{ab}$.', '1/length', status='STANDARD')
R('omega', r'\omega_M{}^a{}_b', [r'\omega'], r'The coefficients of the spin connection of the vielbein (the Levi-Civita '
  r'connection in the frame basis); $\omega_{Mab} = \eta_{ac}\,\omega_M{}^c{}_b$.', '1/length', status='STANDARD')
R('calS', r'\mathcal{S}^{ab}', [r'\mathcal{S}'], r'The generators of frame rotations on spinors, '
  r'$\mathcal{S}^{ab} = \frac14[\gamma^a, \gamma^b]$ (the commutator).', 'dimensionless', status='STANDARD')
R('LPsi', r'\mathcal{L}_\Psi', [r'\mathcal{L}_\Psi'], r'The Lagrangian density of dirac16complex (the bracket of $S_\Psi$).',
  'GeV^8', status='RECORD')

# ------------------------------------------------------------------ gauge fields and couplings
R('Ggluon', r'G^A_M,\ G_M,\ G_{MN},\ G^A_{MN}', ['G'], r'The gluon field (SU(3)), in the geometric normalisation of the '
  r'action (couplings in front of the kinetic terms): the components $G^A_M$ ($A = 1, \dots, 8$), the matrix '
  r'$G_M = G^A_Mt^A$, the field strength $G_{MN}$ (matrix) and its components $G^A_{MN}$; $G^A_{\mu\nu}$ are its components '
  r'along the observable directions (the zero mode, flat in $x_0$).', 'GeV (field), GeV^2 (field strength)', status='ASSUMED')
R('Wsu2', r'W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}', ['W'], r'The SU(2) gauge field (geometric normalisation): the components '
  r'$W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and '
  r'its components $W^I_{MN}$; with Greek indices the components along the observable directions.',
  'GeV (field), GeV^2 (field strength)', status='ASSUMED')
R('Bhyp', r'B_M,\ B_{MN}', ['B'], r'The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength.',
  'GeV (field), GeV^2 (field strength)', status='ASSUMED')
R('tgen', r't^A', ['t'], r'The generators of SU(3) in the fundamental representation (the Gell-Mann matrices divided by 2), '
  r'$\mathrm{tr}(t^At^B) = \frac12\delta^{AB}$.', 'dimensionless', status='STANDARD')
R('tau', r'\tau^I', [r'\tau'], r'The Pauli matrices acting on weak-isospin doublets ($\tau^I/2$ the generators of SU(2); '
  r'$\tau^3 = \mathrm{diag}(1, -1)$).', 'dimensionless', status='STANDARD')
R('ghat3', r'\hat g_3', [r'\hat g_3'], r'The eight-dimensional SU(3) coupling (it multiplies the gluon kinetic term as '
  r'$1/\hat g_3^2$); $g_3^2 = \hat g_3^2/V_\perp$.', 'GeV^-2', status='ASSUMED')
R('ghat2', r'\hat g_2', [r'\hat g_2'], r'The eight-dimensional SU(2) coupling; $g_2^2 = \hat g_2^2/V_\perp$.', 'GeV^-2',
  status='ASSUMED')
R('ghat1', r'\hat g_1', [r'\hat g_1'], r'The eight-dimensional U(1)$_Y$ coupling; $g_1^2 = \hat g_1^2/V_\perp$.', 'GeV^-2',
  status='ASSUMED')
R('ghatZ', r'\hat g_Z', [r'\hat g_Z'], r'The eight-dimensional coupling of the $Z$, $\hat g_Z = (\hat g_2^2 + \hat g_1^2)^{1/2}$.',
  'GeV^-2', status='STANDARD')
R('ehat', r'\hat e', [r'\hat e'], r'The eight-dimensional electric coupling, $\hat e = \hat g_2\hat g_1/\hat g_Z$ '
  r'($e^2 = \hat e^2/V_\perp$).', 'GeV^-2', status='STANDARD')
R('geff', r'\hat g_{3,\mathrm{eff}},\ \hat g_{2,\mathrm{eff}},\ \hat g_{1,\mathrm{eff}}',
  [r'\hat g_{3,\mathrm{eff}}', r'\hat g_{2,\mathrm{eff}}', r'\hat g_{1,\mathrm{eff}}'], r'The field-dependent '
  r'eight-dimensional couplings produced by I12: $1/\hat g_{i,\mathrm{eff}}^2 = 1/\hat g_i^2 + 4c\,\bar\Psi\Psi/\Lambda_\star^3$ '
  r'with $c = c_{\mathrm{G}}, c_{\mathrm{W}}, c_{\mathrm{B}}$.', 'GeV^-2', status='DERIVED')
R('g3', r'g_3', [r'g_3'], r'The four-dimensional strong coupling ($g_3^2 = 4\pi\alpha_3$).', 'dimensionless',
  r'$g_3^2 = 0.7786$ at $2M_{\mathrm{DM}}$', 'DERIVED')
R('g2', r'g_2', [r'g_2'], r'The four-dimensional SU(2) coupling ($g_2^2 = 4\pi\alpha_2$).', 'dimensionless',
  r'$g_2^2 = 0.3781$ at $2M_{\mathrm{DM}}$', 'DERIVED')
R('g1', r'g_1', [r'g_1'], r'The four-dimensional hypercharge coupling ($g_1^2 = 4\pi\alpha_1$, Standard-Model normalisation '
  r'without the GUT factor).', 'dimensionless', r'$g_1^2 = 0.1380$ at $2M_{\mathrm{DM}}$', 'DERIVED')
R('Wpm', r'W^\pm_M,\ W^+,\ W^-', [r'W^\pm', r'W^+', r'W^-'], r'The charged weak bosons, canonically normalised: '
  r'$W^\pm_M = (W^1_M \mp \mathrm{i}W^2_M)/(\sqrt2\,\hat g_2)$; $W^+$ carries the electric charge $+e$ and $W^-$ the charge '
  r"$-e$ (they are each other's antiparticles and have one mass).", 'GeV^3', status='STANDARD')
R('Zboson', r'Z_M', ['Z'], r'The $Z$ boson field, canonically normalised, $Z_M = (W^3_M - B_M)/\hat g_Z$.', 'GeV^3',
  status='STANDARD')
R('Aphoton', r'A_M', ['A'], r'The photon field, canonically normalised, '
  r'$A_M = (\hat g_1^2W^3_M + \hat g_2^2B_M)/(\hat g_1\hat g_2\hat g_Z)$.', 'GeV^3', status='STANDARD')
R('thetaW', r'\theta_{\mathrm{W}}', [r'\theta_{\mathrm{W}}'], r'The weak mixing angle of the couplings, '
  r'$\cos\theta_{\mathrm{W}} = \hat g_2/\hat g_Z$, $\sin\theta_{\mathrm{W}} = \hat g_1/\hat g_Z$; fixed by the measured $W$ and '
  r'$Z$ masses with $\rho_{\mathrm{EW},0}$.', 'dimensionless', r'$\cos^2\theta_{\mathrm{W}} = 0.776368$', 'DERIVED')
R('J3', r'J_3^{AN}', [r'J_3'], r'The colour current of the quarks (the source of the gluons), summed over the generations.',
  'GeV^7', status='STANDARD')
R('J2', r'J_2^{IN}', [r'J_2'], r'The weak-isospin current of the doublets $Q_i$, $\ell_i$ (the source of $W^I$).', 'GeV^7',
  status='STANDARD')
R('J2pm', r'J_2^{\pm}{}^N', [r'J_2^\pm'], r'The charged combinations of the isospin current, '
  r'$J_2^\pm = (J_2^1 \mp \mathrm{i}J_2^2)/\sqrt2$ (the sources of $W^\pm$).', 'GeV^7', status='STANDARD')
R('J1', r'J_1^N', [r'J_1'], r'The hypercharge current of all fermions (the source of $B$).', 'GeV^7', status='STANDARD')
R('Jem', r'J_{\mathrm{em}}^N', [r'J_{\mathrm{em}}'], r'The electromagnetic current, $J_{\mathrm{em}} = J_2^3 + J_1$ (in units '
  r'of the elementary charge).', 'GeV^7', status='STANDARD')

# ------------------------------------------------------------------ Standard-Model fermions
R('psi', r'\psi_i,\ \bar\psi_i', [r'\psi', r'\bar\psi'], r'A Standard-Model fermion field of eight dimensions: $\psi_i$ is '
  r'the multiplet $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ of the generation $i$, $\psi_f$ one fermion component $f$ (in '
  r'four-dimensional formulas its zero mode); $\bar\psi = \psi^\dagger C$ the Dirac adjoint.',
  'GeV^(7/2) (eight dimensions), GeV^(3/2) (four dimensions)', status='ASSUMED')
R('Qdoublet', r'Q_i,\ \bar Q_i', ['Q', r'\bar Q'], r'The quark doublet of the generation $i$ (left-handed up and down quark '
  r'of one generation, three colours) and its Dirac adjoint.', 'GeV^(7/2)', status='ASSUMED')
R('uR', r'u_R,\ u_{Ri},\ \bar u_{Ri}', [r'u_R', r'u_{Ri}', r'u_{Rj}', r'\bar u_{Ri}'], r'The up-type quark singlet: $u_R$ '
  r'the multiplet, $u_{Ri}$ that of the generation $i$ ($u_R$, $c_R$, $t_R$), $\bar u_{Ri}$ its Dirac adjoint.',
  'GeV^(7/2)', status='ASSUMED')
R('dR', r'd_R,\ d_{Ri},\ \bar d_{Ri}', [r'd_R', r'd_{Ri}', r'd_{Rj}', r'\bar d_{Ri}'], r'The down-type quark singlet: $d_R$ '
  r'the multiplet, $d_{Ri}$ that of the generation $i$ ($d_R$, $s_R$, $b_R$), $\bar d_{Ri}$ its Dirac adjoint.',
  'GeV^(7/2)', status='ASSUMED')
R('ldoublet', r'\ell_i,\ \bar\ell_i', [r'\ell', r'\bar\ell'], r'The lepton doublet of the generation $i$ (left-handed '
  r'neutrino and charged lepton) and its Dirac adjoint.', 'GeV^(7/2)', status='ASSUMED')
R('eR', r'e_R,\ e_{Ri}', [r'e_R', r'e_{Ri}', r'e_{Rj}'], r'The right-handed charged-lepton singlet: $e_R$ the multiplet, '
  r'$e_{Ri}$ that of the generation $i$ ($e_R$, $\mu_R$, $\tau_R$).', 'GeV^(7/2)', status='ASSUMED')
R('nuR', r'\nu_R,\ \nu_{Ri}', [r'\nu_R', r'\nu_{Ri}', r'\nu_{Rj}'], r'The right-handed neutrino (a gauge singlet): $\nu_R$ the '
  r'multiplet, $\nu_{Ri}$ that of the generation $i$; its zero modes give Dirac neutrino masses.', 'GeV^(7/2)',
  status='ASSUMED')
R('mubulk', r'\mu_{\psi i}', [r'\mu'], r'The bulk mass of a Standard-Model fermion: $\mu_{\psi i}$ of the multiplet $\psi$ of the '
  r'generation $i$; with the hidden direction it fixes the localisation $c = f\mu L$ of the zero mode.', 'GeV',
  r'$\mu_{\psi i} = c/(fL)$ with the localisation $c$ of the zero mode (doublets: $\mu_Q = 5.2304\,H$, $\mu_\ell = 9.2055\,H$)', 'ASSUMED')
R('muQ', r'\mu_Q', [r'\mu_Q'], r'The common bulk mass of the three quark doublets.', 'GeV', r'$5.2304\,H$ ($c_Q = 3.38230$)',
  'DERIVED')
R('muell', r'\mu_\ell', [r'\mu_\ell'], r'The common bulk mass of the three lepton doublets.', 'GeV',
  r'$9.2055\,H$ ($c_\ell = 5.95288$)', 'DERIVED')
R('Lpsi', r'\mathcal{L}_{\psi i}', [r'\mathcal{L}_{\psi i}'], r'The Lagrangian density of the fermion multiplet $\psi$ of the '
  r'generation $i$ (the bracket of $S_{\mathrm{f}}$).', 'GeV^8', status='ASSUMED')
R('Qem', r'Q_{\mathrm{em}}', [r'Q_{\mathrm{em}}'], r'The electric charge in units of the elementary charge, '
  r'$Q_{\mathrm{em}} = T_3 + Y$; $Q^f_{\mathrm{em}}$ that of the fermion $f$.', 'dimensionless', status='STANDARD')
R('T3', r'T_3', [r'T_3'], r'The third component of the weak isospin ($+\frac12$ for the upper and $-\frac12$ for the lower '
  r'member of a doublet, 0 for a singlet); $T_3^f$ that of the fermion $f$.', 'dimensionless', status='STANDARD')
R('Yhyp', r'Y', ['Y'], r'The hypercharge (the generator of U(1)$_Y$); $Y_\psi$ the hypercharge of the multiplet $\psi$ '
  r'($Q$: $\frac16$, $u_R$: $\frac23$, $d_R$: $-\frac13$, $\ell$: $-\frac12$, $e_R$: $-1$, $\nu_R$: 0).', 'dimensionless',
  status='STANDARD')

# ------------------------------------------------------------------ the tip: sigma field and Yukawa terms
R('Sigma', r'\Sigma', [r'\Sigma'], r'The tip sigma field: a unitary $2 \times 2$ matrix field on the tip '
  r'($\Sigma^\dagger\Sigma = \mathbf{1}$) that replaces the Higgs doublet; its three modes are the longitudinal $W^+$, $W^-$ and '
  r'$Z$, and $\Sigma = \mathbf{1}$ is the unitary gauge.', 'dimensionless', status='INVENTED')
R('vSigma', r'v_\Sigma', [r'v_\Sigma'], r'The scale of the tip sigma field (its kinetic term is '
  r'$-\frac{v_\Sigma^2}{4}\mathrm{tr}((D_\mu\Sigma)^\dagger D^\mu\Sigma)$); on the static block it fixes the Robin parameter '
  r'$\beta_{\mathrm{W}}$.', 'GeV^(5/2)', r'fixed through $\beta_{\mathrm{W}} = 0.011912$', 'INVENTED')
R('LYuk', r'\mathcal{L}_{\mathrm{Y}}', [r'\mathcal{L}_{\mathrm{Y}}'], r'The tip Yukawa Lagrangian: the couplings of the '
  r'doublets to the singlets through the sigma field and the tip matrices $\mathcal{Y}$ (plus the Hermitian conjugate, h.c.).',
  'GeV^7', status='INVENTED')
R('Ltip', r'\mathcal{L}_{\mathrm{tip}}', [r'\mathcal{L}_{\mathrm{tip}}'], r'The Lagrangian density of the tip action '
  r'(the bracket of $S_{\mathrm{tip}}$).', 'GeV^7', status='INVENTED')
R('Yuk', r'\mathcal{Y}_\nu,\ \mathcal{Y}_e,\ \mathcal{Y}_u,\ \mathcal{Y}_d',
  [r'\mathcal{Y}_\nu', r'\mathcal{Y}_e', r'\mathcal{Y}_u', r'\mathcal{Y}_d'], r'The complex $3 \times 3$ tip Yukawa matrices of '
  r'the neutrino, charged-lepton, up-quark and down-quark sectors (generation indices $i, j$); on the static block they '
  r'become the tip mixing matrices $\mathcal{K}$ (the normalisation of that relation is not fixed: OPEN).', 'dimensionless',
  status='INVENTED')
R('UL', r'U_L', [r'U_L'], r'An SU(2) gauge transformation (a unitary $2 \times 2$ matrix acting on doublets from the left).',
  'dimensionless', status='STANDARD')
R('UY', r'U_Y', [r'U_Y'], r'A U(1)$_Y$ gauge transformation of the sigma field, $U_Y = \mathrm{e}^{\mathrm{i}\vartheta\tau^3/2}$.',
  'dimensionless', status='STANDARD')
R('vartheta', r'\vartheta', [r'\vartheta'], r'The angle (gauge parameter) of a U(1)$_Y$ transformation.', 'dimensionless',
  status='STANDARD')
R('deltatip', r'\delta_{\mathrm{tip}}', [r'\delta_{\mathrm{tip}}'], r'The density that places a tip term in the field '
  r'equations of eight dimensions, $\delta_{\mathrm{tip}} = \delta_{\mathrm{D}}(y + L)/f$ (the Dirac delta function at the tip with the proper '
  r'length of the hidden direction).', '1/length', status='DERIVED')
R('jsigma', r'j_\mu,\ j^I_\mu', ['j'], r'The current of the sigma field on the tip, $j^I_\mu = \frac{\mathrm{i}v_\Sigma^2}{4}'
  r'\mathrm{tr}(\tau^I(D_\mu\Sigma)\Sigma^\dagger)$, and the matrix $j_\mu = j^I_\mu\tau^I/2$.', 'GeV^6', status='STANDARD')
R('Ktip', r'\mathcal{K}', [r'\mathcal{K}', r'\mathcal{K}_\nu', r'\mathcal{K}_e', r'\mathcal{K}_u', r'\mathcal{K}_d'],
  r'The tip mixing matrix of a sector in the boundary conditions of the fermion zero modes (a number $\mathcal{K}$ for one '
  r'generation, a $3 \times 3$ matrix for three): $\mathcal{K}_\nu$, $\mathcal{K}_e$, $\mathcal{K}_u$, $\mathcal{K}_d$ of the '
  r'neutrino, charged-lepton, up-quark and down-quark sectors; UM-2 takes $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, '
  r'$\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$.', 'dimensionless', status='ASSUMED')

# ------------------------------------------------------------------ portals
R('LambdaStar', r'\Lambda_\star', [r'\Lambda_\star'], r'The scale of the portal operators I11, I12, I13.', 'GeV',
  r'only the combinations $c/\Lambda_\star^n$ enter', 'INVENTED')
R('cV', r'c_{\mathrm{V}}', [r'c_{\mathrm{V}}'], r'The coefficient of the vector portal I11.', 'dimensionless',
  r'benchmark through $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$', 'INVENTED')
R('cA', r'c_{\mathrm{A}}', [r'c_{\mathrm{A}}'], r'The coefficient of the $x_0$-chiral vector portal I13.', 'dimensionless',
  r'fixed through $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (dark-matter relic)', 'INVENTED')
R('cG', r'c_{\mathrm{G}}', [r'c_{\mathrm{G}}'], r'The coefficient of the gluon term of the portal I12.', 'dimensionless',
  r'$c_{\mathrm{G}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$', 'INVENTED')
R('cW', r'c_{\mathrm{W}}', [r'c_{\mathrm{W}}'], r'The coefficient of the SU(2) term of the portal I12.', 'dimensionless',
  r'$c_{\mathrm{W}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$', 'INVENTED')
R('cB', r'c_{\mathrm{B}}', [r'c_{\mathrm{B}}'], r'The coefficient of the hypercharge term of the portal I12.', 'dimensionless',
  r'$c_{\mathrm{B}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$', 'INVENTED')
R('cI12', r'c_{\mathrm{I12}}', [r'c_{\mathrm{I12}}'], r'The common coefficient of the three terms of I12 when they are '
  r'universal ($c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$).', 'dimensionless',
  r'$c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$ GeV$^{-3}$ (unitarity-safe benchmark)', 'INVENTED')
R('JBL', r'J^{B-L}_M', [r'J^{B-L}'], r'The $B - L$ current of the Standard-Model fermions (baryon minus lepton number), '
  r'summed over the generations.', 'GeV^7', status='STANDARD')
R('JB', r'J^{B}_M', [r'J^B'], r'The baryon-number current of the quarks (one third per quark), summed over the generations.',
  'GeV^7', status='STANDARD')
R('qBL', r'q_\psi,\ q_f', ['q', r'q_Q', r'q_{u_R}', r'q_{d_R}', r'q_\ell', r'q_{e_R}', r'q_{\nu_R}'], r'The $B - L$ charge: '
  r'$q_\psi$ of the multiplet $\psi$ ($q_Q = q_{u_R} = q_{d_R} = \frac13$, $q_\ell = q_{e_R} = q_{\nu_R} = -1$), $q_f$ of the '
  r'fermion component $f$.', 'dimensionless', status='STANDARD')
R('qB', r'q^B_\psi,\ q^B_f', [r'q^B'], r'The baryon number of the multiplet $\psi$ or of the fermion component $f$ '
  r'($\frac13$ for quarks, 0 for leptons).', 'dimensionless', status='STANDARD')
R('calF', r'\mathcal{F}', [r'\mathcal{F}'], r'The gauge-kinetic operator of the portal I12, '
  r'$\mathcal{F} = c_{\mathrm{G}}G^A_{MN}G^{AMN} + c_{\mathrm{W}}W^I_{MN}W^{IMN} + c_{\mathrm{B}}B_{MN}B^{MN}$; '
  r'$\langle\mathcal{F}\rangle$ its mean value in an environment.', 'GeV^4', status='INVENTED')
R('Pab', r'P_a,\ P_b', [r'P_a', r'P_b'], r'The projectors on the two $x_0$-chiralities, $P_a = (1 + \gamma^{x_0})/2$ and '
  r'$P_b = (1 - \gamma^{x_0})/2$ (in a block: the upper and the lower component).', 'dimensionless', status='INVENTED')
R('PLR', r'P_L,\ P_R', ['P'], r'The projectors on the four-dimensional chiralities, $P_L = (1 + \Gamma_4)/2$ (left-handed) and '
  r'$P_R = (1 - \Gamma_4)/2$ (right-handed).', 'dimensionless', status='STANDARD')
R('Psel', r'P_{\mathrm{sel}}', [r'P_{\mathrm{sel}}'], r'The projector that selects the two blocks of the half $\mathcal{B} = -1$ '
  r'in which the Standard-Model zero modes live, $P_{\mathrm{sel}} = \frac{1 + \Gamma_4\gamma^{x_0}}{2}\,'
  r'\frac{1 - \mathrm{i}\gamma^{x_5}\gamma^{x_6}}{2}$.', 'dimensionless', status='INVENTED')
