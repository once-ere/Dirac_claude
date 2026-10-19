from build_lib import E

# ---------------------------------------------------------------- gravity
E('FE', 'The Einstein-Lovelock equations', r'''
\begin{aligned}
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_N + \Lambda\,\delta^M_N = \kappa\,\mathcal{T}^M{}_N,\\
&\mathcal{E}_{(p)}{}^M{}_N = -\frac{1}{2^{p+1}}\,\delta^{MM_1N_1\cdots M_pN_p}_{NP_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p}
\end{aligned}''', 'AUTHOR', ['metric g', 'all fields (source)'],
  'Solved exactly at order 0 (the background equations [[bg_x4]] to [[bg_x0]], integrated numerically through the primordial era and '
  'solved in closed form for the static block); at order epsilon through the four-dimensional reduction [[einstein4]].', name='el')

E('FE', 'The energy-momentum tensor: definition and components', r'''
\begin{aligned}
&\Delta S_{\mathrm{m}} = -\frac12\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\mathcal{T}_{MN}\,\Delta g^{MN},\qquad
 \rho = -\mathcal{T}^{x_4}{}_{x_4},\qquad p_M = \mathcal{T}^M{}_M\quad \text{($M \ne x_4$, no sum)},\\
&\mathcal{T}^M{}_N = \mathrm{diag}\big(p_0,\ p_3,\ p_3,\ p_3,\ -\rho,\ p_5,\ p_5,\ p_5\big)\quad
 \text{(a diagonal source)},\qquad \bar p = \frac{p_0 + 3p_5}{4}
\end{aligned}''', 'STANDARD', ['metric g', 'all fields'],
  'Definition (for spinors the variation is taken with respect to the vielbein); every source of UM-2 is evaluated in this form.',
  name='tmn_def')

E('FE', 'The total source of gravity', r'''
\mathcal{T}^M{}_N = \mathcal{T}_{\mathrm{stab}}{}^M{}_N + \mathcal{T}_\Psi{}^M{}_N + \mathcal{T}_{\mathrm{gauge}}{}^M{}_N
 + \mathcal{T}_{\mathrm{f}}{}^M{}_N + \mathcal{T}_{\mathrm{tip}}{}^M{}_N + \mathcal{T}_{\mathrm{I11}}{}^M{}_N
 + \mathcal{T}_{\mathrm{I12}}{}^M{}_N + \mathcal{T}_{\mathrm{I13}}{}^M{}_N''', 'DERIVED', ['all fields'],
  'At order 0 the stabiliser dominates; the matter terms enter through their block averages in the first-order block '
  'response [[response]] (relative size 1e-92 today).', name='t_total')

E('FE', 'The energy-momentum tensor of the stabiliser', r'''
\mathcal{T}_{\mathrm{stab}}{}^M{}_N = \rho_{\mathrm{stab}}\;\mathrm{diag}(1,\ -1,\ -1,\ -1,\ -1,\ 1,\ 1,\ 1):\qquad
\rho = \rho_{\mathrm{stab}},\qquad p_3 = -\rho_{\mathrm{stab}},\qquad p_0 = p_5 = \rho_{\mathrm{stab}}''',
  'DERIVED', ['metric g (block scale f)'],
  'Exact; conserved because rho_stab is proportional to f^-8; it sets the static block [[stabiliser]].', name='t_stab')

E('FE', 'The energy-momentum tensor of dirac16complex', r'''
\begin{aligned}
(\mathcal{T}_\Psi)_{MN} &= -\frac14\Big[\bar\Psi\gamma_MD_N\Psi + \bar\Psi\gamma_ND_M\Psi - (D_M\bar\Psi)\gamma_N\Psi
 - (D_N\bar\Psi)\gamma_M\Psi\Big] + g_{MN}\,\mathcal{L}_\Psi,\\
\mathcal{L}_\Psi &= \tfrac12\big(\bar\Psi\gamma^PD_P\Psi - (D_P\bar\Psi)\gamma^P\Psi\big) - m_\Psi\,\bar\Psi\Psi
 - \frac{\lambda}{2}\big(\bar\Psi\Psi\big)^2
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'metric g'],
  'Evaluated for Kohn-Sham states in the form [[ks_tmn]] (verified: energy identity and y-conservation law [[ks_id]]).',
  name='t_psi')

E('FE', 'The energy-momentum tensor of the Standard-Model fermions', r'''
\begin{aligned}
(\mathcal{T}_{\mathrm{f}})_{MN} &= \sum_{i=1}^{3}\sum_\psi\Big\{-\frac14\Big[\bar\psi_i\gamma_MD_N\psi_i
 + \bar\psi_i\gamma_ND_M\psi_i - (D_M\bar\psi_i)\gamma_N\psi_i - (D_N\bar\psi_i)\gamma_M\psi_i\Big]
 + g_{MN}\,\mathcal{L}_{\psi i}\Big\},\\
\mathcal{L}_{\psi i} &= \tfrac12\big(\bar\psi_i\gamma^PD_P\psi_i - (D_P\bar\psi_i)\gamma^P\psi_i\big)
 - \mu_{\psi i}\,\bar\psi_i\psi_i
\end{aligned}''', 'DERIVED', ['every Standard-Model fermion', 'metric g', 'gauge fields'],
  'Used through the block averages of the plasma and of cold matter (ideal and degenerate gases with the x0 masses) in the '
  'block response [[response]] and the hidden pressure [[pbar_hidden]].', name='t_f')

E('FE', 'The energy-momentum tensor of the gauge fields', r'''
\begin{aligned}
(\mathcal{T}_{\mathrm{gauge}})_{MN} ={}& \frac{1}{\hat g_3^2}\Big(G^A_{MP}G^A{}_N{}^P - \frac14g_{MN}G^A_{PQ}G^{APQ}\Big)
 + \frac{1}{\hat g_2^2}\Big(W^I_{MP}W^I{}_N{}^P - \frac14g_{MN}W^I_{PQ}W^{IPQ}\Big)\\
&+ \frac{1}{\hat g_1^2}\Big(B_{MP}B_N{}^P - \frac14g_{MN}B_{PQ}B^{PQ}\Big)
\end{aligned}''', 'STANDARD', ['gluons', 'W', 'B', 'metric g'],
  'Used through the radiation and order-alpha plasma pressures in the block response; radiation drops out of it exactly.',
  name='t_gauge')

E('FE', 'The energy-momentum tensor of the tip', r'''
\begin{aligned}
(\mathcal{T}_{\mathrm{tip}})_{\mu\nu} &= \delta_{\mathrm{tip}}\Big[\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D_\nu\Sigma
 + (D_\nu\Sigma)^\dagger D_\mu\Sigma\big) + g_{\mu\nu}\,\mathcal{L}_{\mathrm{tip}}\Big],\qquad
 \delta_{\mathrm{tip}} = \frac{\delta_{\mathrm{D}}(y + L)}{f},\\
\mathcal{L}_{\mathrm{tip}} &= -\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big) - \mathcal{L}_{\mathrm{Y}}
\end{aligned}''', 'DERIVED', ['sigma field Sigma', 'W', 'B', 'every Standard-Model fermion', 'metric g'],
  'Zero for the hidden component; its gravitational effect is part of the W, Z and fermion rest energies counted in the plasma.',
  name='t_tip')

E('FE', 'The energy-momentum tensors of the portals I11 and I13', r'''
(\mathcal{T}_{\mathrm{I11}})_{MN} = g_{MN}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\big(\mathrm{i}\bar\Psi\gamma^P\Psi\big)J^{B-L}_P,
\qquad (\mathcal{T}_{\mathrm{I13}})_{MN} = g_{MN}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}
 \sum_{P\ne x_0}\big(\mathrm{i}\bar\Psi\gamma^PP_b\Psi\big)J^{B}_P''', 'DERIVED', ['dirac16complex Psi', 'fermions', 'metric g'],
  'Exact (the frame currents do not depend on the vielbein); negligible against the stabiliser in every environment '
  '(the level shifts of [[levelshift]] are below 1e-9 GeV).', name='t_portal')

E('FE', 'The energy-momentum tensor of the portal I12', r'''
\begin{aligned}
(\mathcal{T}_{\mathrm{I12}})_{MN} = \frac{4\bar\Psi\Psi}{\Lambda_\star^3}\Big[&c_{\mathrm{G}}\Big(G^A_{MP}G^A{}_N{}^P
 - \frac14g_{MN}G^A_{PQ}G^{APQ}\Big) + c_{\mathrm{W}}\Big(W^I_{MP}W^I{}_N{}^P - \frac14g_{MN}W^I_{PQ}W^{IPQ}\Big)\\
 &+ c_{\mathrm{B}}\Big(B_{MP}B_N{}^P - \frac14g_{MN}B_{PQ}B^{PQ}\Big)\Big]
\end{aligned}''', 'DERIVED', ['dirac16complex Psi', 'gauge fields', 'metric g'],
  'Exact; I12 acts as a field-dependent gauge coupling [[geff]]; its effect is computed in the coupled solution (at most 1.7e-16).',
  name='t_i12')

E('FE', 'Conservation of the source', r'''
\nabla_M\,\mathcal{T}^M{}_N = 0,\qquad \text{because}\qquad \nabla_M\,\mathcal{E}_{(p)}{}^M{}_N = 0\quad \text{($p = 1, 2, 3$)}''',
  'DERIVED', ['all fields'],
  'The Bianchi identities were verified for the order-0 metric (p = 1, 2, 3); the conservation holds on the matter field '
  'equations; at order 0 it is [[bg_cons]].', name='conservation')

# ---------------------------------------------------------------- matter
E('FE', 'The dirac16complex field equation with the canonical spin connection and the portals', r'''
\gamma^MD_M\Psi = \Big[m_\Psi + \lambda\,\bar\Psi\Psi + \frac{\mathcal{F}}{\Lambda_\star^3}\Big]\Psi
 - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,J^{B-L}_M\gamma^M\Psi
 - \mathrm{i}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}J^{B}_M\gamma^MP_b\Psi''', 'DERIVED',
  ['dirac16complex Psi', 'metric g', 'gauge fields (I12)', 'fermion currents (I11, I13)'],
  'Reduced exactly to the block Hamiltonian [[ferm_red]] (all eight blocks, general a4, b4); solved exactly for the free '
  'spectrum [[psi_spectrum]] and by Kohn-Sham theory with the portal mean fields [[ks]].', name='dirac16')

E('FE', 'The canonical spin connection on the order-0 metric', r'''
\gamma^M\Omega_M = \frac32\,\frac{H}{f}\,\gamma^{x_0} + \Big(\frac{\dot b_4}{b_4} - \frac{\dot a_4}{2}\Big)\gamma^{x_4}''',
  'DERIVED', ['dirac16complex Psi', 'every fermion', 'metric g'],
  'Exact for every a4, b4 and on both halves of a period; removed by the factors of the reduction ansatz [[ferm_red]]; it '
  'vanishes only in flat 4+4 space.', name='gomega')

E('FE', r'The Dirac equation of the quark doublets $Q_i$', r'''
\begin{aligned}
\gamma^MD_MQ_i ={}& \mu_Q\,Q_i - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_Q\,\big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^MQ_i
 - \frac{\mathrm{i}}{3}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma_MP_b\Psi\big)\gamma^MQ_i\\
 &+ \delta_{\mathrm{tip}}\sum_{j=1}^{3}\Sigma\begin{pmatrix}(\mathcal{Y}_u)_{ij}\,u_{Rj}\\ (\mathcal{Y}_d)_{ij}\,d_{Rj}\end{pmatrix}
\end{aligned}''', 'DERIVED', ['quark doublets', 'gauge fields', 'metric g', 'Psi (I11, I13)', 'Sigma'],
  'Solved on the static block by the zero mode and the tip mixing [[ferm_red]] to [[ferm_3gen]] (exact roots; the portal terms are '
  'mean fields of 1e-17 relative size at most).', name='dirac_Q')

E('FE', r'The Dirac equation of the up-type quark singlets $u_{Ri}$ (right-handed up, charm and top quarks)', r'''
\begin{aligned}
\gamma^MD_Mu_{Ri} ={}& \mu_{\psi i}\,u_{Ri} - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_{u_R}\,
 \big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^Mu_{Ri}
 - \frac{\mathrm{i}}{3}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma_MP_b\Psi\big)\gamma^Mu_{Ri}\\
 &+ \delta_{\mathrm{tip}}\sum_{j=1}^{3}(\mathcal{Y}_u)^*_{ji}\,\big(\Sigma^\dagger Q_j\big)_1\qquad (\psi = u_R)
\end{aligned}''', 'DERIVED', ['up-type quark singlets', 'gauge fields', 'metric g', 'Psi', 'Sigma'],
  'As [[dirac_Q]]: singlet zero modes mixed at the tip with the doublet (exact roots for u, c, t).', name='dirac_uR')

E('FE', r'The Dirac equation of the down-type quark singlets $d_{Ri}$ (right-handed down, strange and bottom quarks)', r'''
\begin{aligned}
\gamma^MD_Md_{Ri} ={}& \mu_{\psi i}\,d_{Ri} - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_{d_R}\,
 \big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^Md_{Ri}
 - \frac{\mathrm{i}}{3}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma_MP_b\Psi\big)\gamma^Md_{Ri}\\
 &+ \delta_{\mathrm{tip}}\sum_{j=1}^{3}(\mathcal{Y}_d)^*_{ji}\,\big(\Sigma^\dagger Q_j\big)_2\qquad (\psi = d_R)
\end{aligned}''', 'DERIVED', ['down-type quark singlets', 'gauge fields', 'metric g', 'Psi', 'Sigma'],
  'As [[dirac_Q]] (exact roots for d, s, b; the tip matrix of the sector is the CKM matrix).', name='dirac_dR')

E('FE', 'The Dirac equation of the lepton doublets (left-handed neutrinos and charged leptons of three flavours)', r'''
\begin{aligned}
\gamma^MD_M\ell_i ={}& \mu_\ell\,\ell_i - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_\ell\,
 \big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^M\ell_i
 + \delta_{\mathrm{tip}}\sum_{j=1}^{3}\Sigma\begin{pmatrix}(\mathcal{Y}_\nu)_{ij}\,\nu_{Rj}\\ (\mathcal{Y}_e)_{ij}\,e_{Rj}\end{pmatrix}
\end{aligned}''', 'DERIVED', ['lepton doublets', 'gauge fields', 'metric g', 'Psi (I11)', 'Sigma'],
  'As [[dirac_Q]]: one doublet zero mode serves the three generations; exact roots for the three neutrinos and the three '
  'charged leptons; no I13 term (leptons carry no baryon number).', name='dirac_l')

E('FE', r'The Dirac equation of the right-handed charged leptons $e_{Ri}$ (electron, muon and tau)', r'''
\gamma^MD_Me_{Ri} = \mu_{\psi i}\,e_{Ri} - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_{e_R}\,
 \big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^Me_{Ri}
 + \delta_{\mathrm{tip}}\sum_{j=1}^{3}(\mathcal{Y}_e)^*_{ji}\,\big(\Sigma^\dagger\ell_j\big)_2\qquad (\psi = e_R)''',
  'DERIVED', ['right-handed charged leptons', 'gauge fields', 'metric g', 'Psi', 'Sigma'],
  'As [[dirac_l]] (exact roots for e, mu, tau with the tip matrix 1).', name='dirac_eR')

E('FE', r'The Dirac equation of the right-handed neutrinos $\nu_{Ri}$', r'''
\gamma^MD_M\nu_{Ri} = \mu_{\psi i}\,\nu_{Ri} - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,q_{\nu_R}\,
 \big(\mathrm{i}\bar\Psi\gamma_M\Psi\big)\gamma^M\nu_{Ri}
 + \delta_{\mathrm{tip}}\sum_{j=1}^{3}(\mathcal{Y}_\nu)^*_{ji}\,\big(\Sigma^\dagger\ell_j\big)_1\qquad (\psi = \nu_R)''',
  'DERIVED', ['right-handed neutrinos', 'metric g', 'Psi (I11)', 'Sigma'],
  'Gauge singlets: sharply localised singlet zero modes (c_R = -31 to -35) mixed at the tip with the lepton doublet give the '
  'Dirac neutrino masses; never thermalised (their I11 production is computed in [[nuR_I11]]).', name='dirac_nuR')

# ---------------------------------------------------------------- gauge fields
E('FE', 'The fermion currents of the gauge fields', r'''
\begin{aligned}
J_3^{AN} &= \sum_{i=1}^{3}\big(\mathrm{i}\bar Q_i\gamma^Nt^AQ_i + \mathrm{i}\bar u_{Ri}\gamma^Nt^Au_{Ri}
 + \mathrm{i}\bar d_{Ri}\gamma^Nt^Ad_{Ri}\big),\qquad
 J_2^{IN} = \sum_{i=1}^{3}\Big(\mathrm{i}\bar Q_i\gamma^N\frac{\tau^I}{2}Q_i + \mathrm{i}\bar\ell_i\gamma^N\frac{\tau^I}{2}\ell_i\Big),\\
J_1^N &= \sum_{i=1}^{3}\sum_\psi Y_\psi\,\mathrm{i}\bar\psi_i\gamma^N\psi_i,\qquad
 J_{\mathrm{em}}^N = J_2^{3N} + J_1^N,\qquad J_2^{\pm}{}^N = \frac{J_2^{1N} \mp \mathrm{i}J_2^{2N}}{\sqrt2}
\end{aligned}''', 'STANDARD', ['every Standard-Model fermion', 'gauge fields'],
  'Definitions; summed over the three generations.', name='currents')

E('FE', 'The field-dependent gauge couplings produced by I12', r'''
\frac{1}{\hat g_{3,\mathrm{eff}}^2} = \frac{1}{\hat g_3^2} + \frac{4c_{\mathrm{G}}\bar\Psi\Psi}{\Lambda_\star^3},\qquad
\frac{1}{\hat g_{2,\mathrm{eff}}^2} = \frac{1}{\hat g_2^2} + \frac{4c_{\mathrm{W}}\bar\Psi\Psi}{\Lambda_\star^3},\qquad
\frac{1}{\hat g_{1,\mathrm{eff}}^2} = \frac{1}{\hat g_1^2} + \frac{4c_{\mathrm{B}}\bar\Psi\Psi}{\Lambda_\star^3}''',
  'DERIVED', ['gauge fields', 'dirac16complex Psi'],
  'Exact; in four dimensions it is the coupling shift [[dm_on_sm]] (at most 1.7e-16 at the dark-matter freeze-out).',
  name='geff')

E('FE', 'The Yang-Mills equation of the gluons', r'''
\nabla_M\Big(\frac{G^{MN}}{\hat g_{3,\mathrm{eff}}^2}\Big) - \mathrm{i}\Big[G_M,\ \frac{G^{MN}}{\hat g_{3,\mathrm{eff}}^2}\Big]
 = J_3^{AN}\,t^A''', 'DERIVED', ['gluons', 'quarks', 'Psi (I12)', 'metric g'],
  'Solved on the static block by the x0 reduction [[x0_boson]] with no tip term: the gluon zero mode is exactly massless '
  '(flat profile); QCD below the confinement scale enters through the nucleon masses and the condensates [[gluon_cond]].',
  name='ym_gluon')

E('FE', r'The Yang-Mills equation of the SU(2) field $W^I$ (matrix form) with the tip current', r'''
\nabla_M\Big(\frac{W^{MN}}{\hat g_{2,\mathrm{eff}}^2}\Big) - \mathrm{i}\Big[W_M,\ \frac{W^{MN}}{\hat g_{2,\mathrm{eff}}^2}\Big]
 = J_2^{IN}\,\frac{\tau^I}{2} + \delta_{\mathrm{tip}}\,\frac{v_\Sigma^2}{4}\Big(W^N - B^N\,\frac{\tau^3}{2}\Big)\qquad
 (\Sigma = \mathbf{1})''', 'DERIVED', ['W', 'B', 'lepton and quark doublets', 'Sigma', 'Psi (I12)', 'metric g'],
  'The tip term (in the unitary gauge; N runs over the tip directions) is a mass term for the charged components and for '
  'W^3 - B only; solved on the static block by [[x0_boson]] with the Robin condition [[x0_boson_bc]].', name='ym_su2')

E('FE', r'The Yang-Mills equation of the hypercharge field $B$', r'''
\nabla_M\Big(\frac{B^{MN}}{\hat g_{1,\mathrm{eff}}^2}\Big) = J_1^N - \delta_{\mathrm{tip}}\,\frac{v_\Sigma^2}{4}\,
 \big(W^{3N} - B^N\big)\qquad (\Sigma = \mathbf{1})''', 'DERIVED', ['B', 'W^3', 'every fermion', 'Sigma', 'Psi (I12)', 'metric g'],
  'As [[ym_su2]]; the combination that receives no tip term is the photon (see [[ym_lin]]).', name='ym_b')

E('FE', r'The $W^+$, $W^-$, $Z$ and photon field equations to linear order in the fields (I12 neglected)', r'''
\begin{aligned}
&\nabla_MW^{\pm}{}^{MN} = \hat g_2\,J_2^{\pm}{}^N + \delta_{\mathrm{tip}}\,\frac{v_\Sigma^2}{4}\,\hat g_2^2\,W^{\pm}{}^N,\qquad
 \nabla_MA^{MN} = \hat e\,J_{\mathrm{em}}^N,\qquad \hat e = \frac{\hat g_2\hat g_1}{\hat g_Z},\\
&\nabla_MZ^{MN} = \hat g_Z\big(J_2^{3N} - \sin^2\theta_{\mathrm{W}}\,J_{\mathrm{em}}^N\big)
 + \delta_{\mathrm{tip}}\,\frac{v_\Sigma^2}{4}\,\hat g_Z^2\,Z^N,\\
&W^{\pm}{}^{MN} = \nabla^MW^{\pm}{}^N - \nabla^NW^{\pm}{}^M,\qquad Z^{MN} = \nabla^MZ^N - \nabla^NZ^M,\qquad
 A^{MN} = \nabla^MA^N - \nabla^NA^M
\end{aligned}''', 'DERIVED', ['W+', 'W-', 'Z', 'photon A', 'every fermion', 'Sigma'],
  'Obtained exactly from [[ym_su2]] and [[ym_b]] at linear order; the photon has no tip term and stays massless; the W and Z '
  'tip terms become the Robin conditions [[x0_boson_bc]].', name='ym_lin')

# ---------------------------------------------------------------- tip sigma field
E('FE', 'The tip sigma field equation (the Noether identity of the gauge symmetry)', r'''
\begin{aligned}
&\nabla^\mu j_\mu - \mathrm{i}\big[W^\mu,\ j_\mu\big] = -\mathrm{i}\,\frac{\tau^I}{2}\sum_{i,j=1}^{3}\Big[
 \bar\ell_i\,\frac{\tau^I}{2}\,\Sigma\begin{pmatrix}(\mathcal{Y}_\nu)_{ij}\,\nu_{Rj}\\ (\mathcal{Y}_e)_{ij}\,e_{Rj}\end{pmatrix}
 + \bar Q_i\,\frac{\tau^I}{2}\,\Sigma\begin{pmatrix}(\mathcal{Y}_u)_{ij}\,u_{Rj}\\ (\mathcal{Y}_d)_{ij}\,d_{Rj}\end{pmatrix}
 - \text{h.c.}\Big],\\
&j_\mu = j^I_\mu\,\frac{\tau^I}{2},\qquad j^I_\mu = \frac{\mathrm{i}v_\Sigma^2}{4}\,\mathrm{tr}\big(\tau^I(D_\mu\Sigma)\Sigma^\dagger\big),
 \qquad j^I_\mu\big\vert_{\Sigma = \mathbf{1}} = \frac{v_\Sigma^2}{4}\big(W^I_\mu - \delta^{I3}B_\mu\big)
\end{aligned}''', 'STANDARD', ['sigma field Sigma', 'W', 'B', 'fermions at the tip'],
  'Not independent: it is the divergence of the tip part of [[ym_su2]] (the fermion currents are conserved up to the same '
  'tip terms); in the unitary gauge the three modes of Sigma are the longitudinal W+, W- and Z.', name='sigma_eq')

# ---------------------------------------------------------------- boundary conditions
E('FE', 'The boundary conditions of gravity and the gauge fields at the fold and the tip', r'''
\begin{aligned}
&z \to \pi - z:\qquad \partial_yF\big\vert_{y=0} = 0\ \ \text{(even)}\quad\text{or}\quad F\big\vert_{y=0} = 0\ \ \text{(odd)};\\
&\text{at } y = -L\text{: the natural (Robin) condition of the tip term}
\end{aligned}''', 'DERIVED',
  ['metric g', 'gauge fields'],
  'Lagrangian boundary conditions of the variational principle; for an x0 profile they are [[x0_boson_bc]].', name='bc_boson')

E('FE', 'The boundary conditions of dirac16complex', r'''
\big(1 - \gamma^{x_0}\big)\Psi\big\vert_{y=0} = 0\ \ \text{(even)}\quad\text{or}\quad
\big(1 + \gamma^{x_0}\big)\Psi\big\vert_{y=0} = 0\ \ \text{(odd)},\qquad
\big(1 - \gamma^{x_0}\big)\Psi\big\vert_{y=-L} = 0''', 'DERIVED', ['dirac16complex Psi'],
  'Both parities are modes of the full period; self-adjoint (DERIVED); in block form they are [[ks_bc]].', name='bc_psi')

E('FE', 'The boundary conditions of the Standard-Model fermions', r'''
\begin{aligned}
&P_{\mathrm{sel}} = \frac{1 + \Gamma_4\gamma^{x_0}}{2}\,\frac{1 - \mathrm{i}\gamma^{x_5}\gamma^{x_6}}{2};\\
&\text{doublets } (Q, \ell):\quad P_{\mathrm{sel}}\big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=0}
 = \big(1 - P_{\mathrm{sel}}\big)\big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=0} = 0,\qquad
 \big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=-L} = 0;\\
&\text{singlets } (u_R, d_R, e_R, \nu_R):\quad P_{\mathrm{sel}}\big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=0}
 = \big(1 - P_{\mathrm{sel}}\big)\big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=0} = 0,\qquad
 \big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=-L} = 0
\end{aligned}''', 'INVENTED', ['every Standard-Model fermion'],
  'Self-adjoint (DERIVED); each doublet has one Weyl zero mode with Gamma4 = +1 and each singlet one with Gamma4 = -1, in the '
  'two selected blocks of the half B = -1; at the tip modified by the mixing conditions [[bc_tip]].', name='bc_sm')

E('FE', 'The tip mixing conditions of one and of three generations', r'''
\begin{aligned}
&\text{one generation:}\quad b_L(-L) = \mathcal{K}\,b_R(-L),\qquad a_R(-L) = -\mathcal{K}\,a_L(-L),\qquad \chi = (a,\ \mathrm{i}b);\\
&\text{three generations:}\quad b_L(-L) = \mathcal{K}\,b_R(-L),\qquad a_R(-L) = -\mathcal{K}^\dagger a_L(-L),\qquad
 \mathcal{K} \in \{\mathcal{K}_\nu, \mathcal{K}_e, \mathcal{K}_u, \mathcal{K}_d\};\\
&\text{UM-2:}\quad \mathcal{K}_e = \mathcal{K}_u = \mathbf{1},\qquad \mathcal{K}_\nu = U,\qquad \mathcal{K}_d = V_{\mathrm{CKM}}
\end{aligned}''', 'DERIVED', ['every Standard-Model fermion', 'Sigma'],
  'Equivalent to the tip Yukawa terms; self-adjoint for every complex matrix (sympy, 42 real variables); the choice of the '
  'tip matrices is ASSUMED; solved exactly by the mass conditions [[ferm_1gen]] to [[ferm_3gen]].', name='bc_tip')
