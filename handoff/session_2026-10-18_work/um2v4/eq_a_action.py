from build_lib import E

E('IN', 'The action of UM-2', r'''
\begin{aligned}
S ={}& S_{\mathrm{EL}} + S_{\mathrm{stab}} + S_\Psi + S_{\mathrm{gauge}} + S_{\mathrm{f}} + S_{\mathrm{tip}}
 + S_{\mathrm{I11}} + S_{\mathrm{I12}} + S_{\mathrm{I13}}
\end{aligned}''', 'ASSUMED', ['all fields'],
  'The sum of all terms; varying it gives every field equation ([[el]] to [[bc_tip]]); no Higgs field is present.')

E('IN', 'Einstein-Lovelock gravity with the author\'s weights', r'''
\begin{aligned}
S_{\mathrm{EL}} &= \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,
 \Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)} - 2\Lambda\Big),\qquad \kappa = 8\pi G_8,\\
\alpha_{(p)} &= w_{(p)}\,H^{2-2p},\qquad w_{(1)} = 1,\quad w_{(2)} = \frac{1}{32},\quad w_{(3)} = \frac{1}{1152},
 \qquad \Lambda = -10H^2
\end{aligned}''', 'AUTHOR', ['metric g'],
  'Kept unchanged; its metric variation is the left side of [[el]], evaluated exactly (symbolically) for the order-0 metric.')

E('IN', 'The Lovelock densities', r'''
\begin{aligned}
\mathcal{L}_{(p)} &= \frac{1}{2^{p}}\,\delta^{M_1N_1\cdots M_pN_p}_{P_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p},\\
\mathcal{L}_{(1)} &= R,\qquad \mathcal{L}_{(2)} = R^2 - 4R_{MN}R^{MN} + R_{MNPQ}R^{MNPQ}
\end{aligned}''', 'STANDARD', ['metric g'],
  'Evaluated exactly for the pair-diagonal curvature of the order-0 metric ([[lov_pair]]) and for a product with the static block ([[reduction]]).')

E('IN', 'The block stabiliser', r'''
S_{\mathrm{stab}} = -\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\rho_{\mathrm{stab}}(f),\qquad
\kappa\rho_{\mathrm{stab}}(f) = \kappa\rho_{\mathrm{stab}}(f_*)\Big(\frac{f_*}{f}\Big)^{8},\qquad
f = \mathrm{e}^{-a_4}\,b_4^{1/2}''', 'ASSUMED', ['metric g (block scale f)'],
  'Its energy-momentum tensor ([[t_stab]]) enters the background exactly; its normalisation is fixed by the static block ([[stabiliser]]); '
  'its microscopic origin is OPEN.')

E('IN', 'The dirac16complex field', r'''
\begin{aligned}
S_\Psi &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\tfrac12\big(\bar\Psi\gamma^MD_M\Psi
 - (D_M\bar\Psi)\gamma^M\Psi\big) - m_\Psi\,\bar\Psi\Psi - \frac{\lambda}{2}\big(\bar\Psi\Psi\big)^2\Big],\\
m_\Psi &= 3H\mathcal{M} = H\qquad (\mathcal{M} = 1/3)
\end{aligned}''', 'RECORD', ['dirac16complex Psi', 'metric g'],
  'Gives [[t_psi]] and [[dirac16]]; solved by the exact x0 spectrum ([[psi_spectrum]]) and by Kohn-Sham theory ([[ks]] to '
  '[[ks_bc]]); the self-coupling lambda is bounded by the fold-band radiation ([[selfint]]).')

E('IN', 'The Clifford algebra, the Dirac adjoint and the two halves of dirac16complex', r'''
\begin{aligned}
&\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
 \eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1),\qquad \gamma^M = \mathbf{e}_a{}^M\gamma^a,\\
&\bar\Psi = \Psi^\dagger C,\qquad C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3},\qquad
 \Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4},\qquad \mathcal{B} = -\mathrm{i}C\gamma^{x_4},\\
&\Psi = \Psi_A + \Psi_B,\qquad \mathcal{B}\Psi_A = -\Psi_A,\qquad \mathcal{B}\Psi_B = +\Psi_B
\end{aligned}''', 'AUTHOR', ['dirac16complex Psi', 'every Standard-Model fermion'],
  'The author\'s real 16 x 16 matrices satisfy the algebra exactly (31 checks); B commutes with every interaction of the good '
  'sector, so the two halves are conserved separately.')

E('IN', 'The canonical spin connection (the coupling of every spinor to gravity)', r'''
\begin{aligned}
&D_M\Psi = \partial_M\Psi + \Omega_M\Psi,\qquad D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M,\qquad
 \Omega_M = \tfrac12\,\omega_{Mab}\,\mathcal{S}^{ab},\qquad \mathcal{S}^{ab} = \tfrac14\big[\gamma^a, \gamma^b\big],\\
&\omega_M{}^a{}_b = \mathbf{e}^a{}_N\big(\partial_M\mathbf{e}_b{}^N + \Gamma^N{}_{MP}\,\mathbf{e}_b{}^P\big),\qquad
 \omega_{Mab} = \eta_{ac}\,\omega_M{}^c{}_b,\qquad g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\,\mathbf{e}^b{}_N,\\
&\Gamma^N{}_{MP} = \tfrac12\,g^{NQ}\big(\partial_Mg_{QP} + \partial_Pg_{QM} - \partial_Qg_{MP}\big)
\end{aligned}''', 'STANDARD', ['metric g', 'dirac16complex Psi', 'every Standard-Model fermion'],
  'Evaluated exactly for the order-0 metric ([[gomega]]); it makes gamma^N covariantly constant (verified symbolically).')

E('IN', r'The gauge fields of SU(3) $\times$ SU(2) $\times$ U(1)$_Y$ in eight dimensions', r'''
S_{\mathrm{gauge}} = -\frac14\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\frac{1}{\hat g_3^2}\,G^A_{MN}G^{AMN}
 + \frac{1}{\hat g_2^2}\,W^I_{MN}W^{IMN} + \frac{1}{\hat g_1^2}\,B_{MN}B^{MN}\Big)''', 'ASSUMED',
  ['gluons G', 'SU(2) fields W', 'hypercharge field B', 'metric g'],
  'Gives [[t_gauge]] and the Yang-Mills equations [[ym_gluon]] to [[ym_lin]]; their x0 reduction gives the massless photon and '
  'gluons and the W, Z masses ([[x0_boson]] to [[wz_fit]]).')

E('IN', 'The field strengths', r'''
\begin{aligned}
&G_M = G^A_M\,t^A,\qquad G_{MN} = \partial_MG_N - \partial_NG_M - \mathrm{i}\big[G_M, G_N\big],\qquad
 G^A_{MN} = 2\,\mathrm{tr}\big(t^AG_{MN}\big),\\
&W_M = W^I_M\,\frac{\tau^I}{2},\qquad W_{MN} = \partial_MW_N - \partial_NW_M - \mathrm{i}\big[W_M, W_N\big],\qquad
 W^I_{MN} = \mathrm{tr}\big(\tau^IW_{MN}\big),\\
&B_{MN} = \partial_MB_N - \partial_NB_M
\end{aligned}''', 'STANDARD', ['gluons G', 'SU(2) fields W', 'hypercharge field B'],
  'Exact definitions; the non-abelian terms are kept in [[ym_gluon]] to [[ym_b]] and neglected in the linearised W, Z '
  'and photon equations [[ym_lin]].')

E('IN', r'The physical electroweak fields $W^+$, $W^-$, $Z$ and the photon (canonically normalised)', r'''
\begin{aligned}
&W^\pm_M = \frac{W^1_M \mp \mathrm{i}W^2_M}{\sqrt2\,\hat g_2},\qquad
 Z_M = \frac{W^3_M - B_M}{\hat g_Z},\qquad A_M = \frac{\hat g_1^2\,W^3_M + \hat g_2^2\,B_M}{\hat g_1\hat g_2\hat g_Z},\\
&\hat g_Z = \sqrt{\hat g_2^2 + \hat g_1^2},\qquad \cos\theta_{\mathrm{W}} = \frac{\hat g_2}{\hat g_Z},\qquad
 \sin\theta_{\mathrm{W}} = \frac{\hat g_1}{\hat g_Z}
\end{aligned}''', 'STANDARD', ['W+', 'W-', 'Z', 'photon A', 'SU(2) fields W', 'hypercharge field B'],
  'W+ carries the electric charge +e and W- the charge -e (DERIVED); Z and A are the neutral combinations; the angle of the '
  'couplings is fixed by the measured masses ([[wz_fit]]).')

E('IN', 'The Standard-Model fermions: three generations with bulk masses', r'''
\begin{aligned}
S_{\mathrm{f}} &= \sum_{i=1}^{3}\sum_{\psi}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\tfrac12\big(\bar\psi_i\gamma^MD_M\psi_i
 - (D_M\bar\psi_i)\gamma^M\psi_i\big) - \mu_{\psi i}\,\bar\psi_i\psi_i\Big],\\
\psi &\in \{Q,\ u_R,\ d_R,\ \ell,\ e_R,\ \nu_R\},\qquad \mu_{\psi i} = \mu_Q\ (\psi = Q),\qquad
 \mu_{\psi i} = \mu_\ell\ (\psi = \ell)
\end{aligned}''', 'ASSUMED', ['quarks Q, u_R, d_R', 'leptons l, e_R, nu_R', 'metric g', 'gauge fields'],
  'Gives [[t_f]] and the Dirac equations [[dirac_Q]] to [[dirac_nuR]]; the zero modes and the tip mixing give all twelve masses '
  '([[ferm_red]] to [[ferm_3gen]]).')

E('IN', 'The covariant derivative of a Standard-Model fermion and the electric charge', r'''
D_M = \partial_M + \Omega_M - \mathrm{i}G^A_M\,t^A - \mathrm{i}W^I_M\,\frac{\tau^I}{2} - \mathrm{i}\,Y B_M,\qquad
Q_{\mathrm{em}} = T_3 + Y''', 'STANDARD', ['every Standard-Model fermion', 'gauge fields', 'metric g'],
  'Exact (geometric normalisation: the couplings stand in front of the kinetic terms of IN-8).')

E('IN', 'The tip sigma field and the tip Yukawa couplings (no Higgs particle)', r'''
\begin{aligned}
S_{\mathrm{tip}} &= \int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\Big[
 -\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big) - \mathcal{L}_{\mathrm{Y}}\Big],\\
\mathcal{L}_{\mathrm{Y}} &= \sum_{i,j=1}^{3}\Big[\bar\ell_i\,\Sigma\begin{pmatrix}(\mathcal{Y}_\nu)_{ij}\,\nu_{Rj}\\
 (\mathcal{Y}_e)_{ij}\,e_{Rj}\end{pmatrix}
 + \bar Q_i\,\Sigma\begin{pmatrix}(\mathcal{Y}_u)_{ij}\,u_{Rj}\\ (\mathcal{Y}_d)_{ij}\,d_{Rj}\end{pmatrix}\Big]
 + \text{h.c.}
\end{aligned}''', 'INVENTED', ['sigma field Sigma', 'W', 'B', 'every Standard-Model fermion'],
  'Gives [[t_tip]], the tip terms of [[dirac_Q]] to [[dirac_nuR]] and of [[ym_su2]], [[ym_b]], and the sigma-field equation '
  '[[sigma_eq]]; on the static block it becomes the Robin condition of the W, Z profiles ([[x0_boson_bc]]) and the tip mixing '
  'of the fermions ([[bc_tip]]).')

E('IN', 'The covariant derivative of the sigma field and its gauge transformation', r'''
D_\mu\Sigma = \partial_\mu\Sigma - \mathrm{i}W^I_\mu\,\frac{\tau^I}{2}\,\Sigma + \mathrm{i}B_\mu\,\Sigma\,\frac{\tau^3}{2},\qquad
\Sigma^\dagger\Sigma = \mathbf{1},\qquad \Sigma \to U_L\,\Sigma\,U_Y^\dagger,\qquad
U_Y = \mathrm{e}^{\mathrm{i}\vartheta\tau^3/2}''', 'INVENTED', ['sigma field Sigma', 'W', 'B'],
  'Every tip term is invariant for arbitrary complex tip matrices (DERIVED with random group elements, deviation 1.1e-14).')

E('IN', r'The tip mass term of $W^+$, $W^-$ and $Z$ in the unitary gauge', r'''
-\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big)\Big\vert_{\Sigma = \mathbf{1}}
= -\frac{v_\Sigma^2}{8}\Big[2\hat g_2^2\,W^+_\mu W^-{}^\mu + \hat g_Z^2\,Z_\mu Z^\mu\Big]''', 'DERIVED',
  ['W+', 'W-', 'Z', 'photon A'],
  'Exact; the photon receives no tip term, so it stays massless; W+ and W- share one mass (particle and antiparticle).')

E('IN', r'Portal I11: the vector contact portal to the $B - L$ currents', r'''
\begin{aligned}
S_{\mathrm{I11}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,
 \big(\mathrm{i}\bar\Psi\gamma^M\Psi\big)\,J^{B-L}_M,\qquad
 J^{B-L}_M = \sum_{i=1}^{3}\sum_{\psi} q_\psi\,\big(\mathrm{i}\bar\psi_i\gamma_M\psi_i\big),\\
q_Q &= q_{u_R} = q_{d_R} = \frac13,\qquad q_\ell = q_{e_R} = q_{\nu_R} = -1
\end{aligned}''', 'INVENTED', ['dirac16complex Psi', 'every Standard-Model fermion'],
  'Enters [[t_portal]], [[dirac16]] and [[dirac_Q]] to [[dirac_nuR]]; on the zero modes it is the contact interaction '
  '[[contact4d]], with the benchmark strength fixed by the freeze-in of the fold bands ([[freezein]]).')

E('IN', 'Portal I12: the gauge-kinetic scalar portal', r'''
S_{\mathrm{I12}} = -\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{\bar\Psi\Psi}{\Lambda_\star^3}\,\mathcal{F},\qquad
\mathcal{F} = c_{\mathrm{G}}\,G^A_{MN}G^{AMN} + c_{\mathrm{W}}\,W^I_{MN}W^{IMN} + c_{\mathrm{B}}\,B_{MN}B^{MN}''',
  'INVENTED', ['dirac16complex Psi', 'gluons', 'W', 'B'],
  'Enters [[t_i12]], [[dirac16]] and the field-dependent couplings [[geff]]; on the dark matter it is [[i12dm]], set to the '
  'unitarity-safe benchmark.')

E('IN', r'Portal I13: the $x_0$-chiral vector portal to the baryon-number current', r'''
\begin{aligned}
S_{\mathrm{I13}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{A}}}{\Lambda_\star^6}
 \sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma^MP_b\Psi\big)\,J^{B}_M,\qquad P_b = \frac{1 - \gamma^{x_0}}{2},
 \qquad P_a = \frac{1 + \gamma^{x_0}}{2},\\
J^{B}_M &= \frac13\sum_{i=1}^{3}\big(\mathrm{i}\bar Q_i\gamma_MQ_i + \mathrm{i}\bar u_{Ri}\gamma_Mu_{Ri}
 + \mathrm{i}\bar d_{Ri}\gamma_Md_{Ri}\big)
\end{aligned}''', 'INVENTED', ['dirac16complex Psi', 'quarks'],
  'Enters [[t_portal]], [[dirac16]] and [[dirac_Q]] to [[dirac_dR]]; the bilinear is Hermitian for M != x0 only (DERIVED); on '
  'the zero modes it is [[contact4d]], its strength fixed by the dark-matter relic ([[relic]]).')
