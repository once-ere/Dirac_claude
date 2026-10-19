"""Replace the LaTeX body of named inventory equations (to fit the page width); the physics is unchanged."""
import re
import sys
from pathlib import Path

NEW = {}

NEW['bc_boson'] = r'''
\begin{aligned}
&z \to \pi - z:\qquad \partial_yF\big\vert_{y=0} = 0\ \ \text{(even)}\quad\text{or}\quad F\big\vert_{y=0} = 0\ \ \text{(odd)};\\
&\text{at } y = -L\text{: the natural (Robin) condition of the tip term}
\end{aligned}'''

NEW['bc_sm'] = r'''
\begin{aligned}
&P_{\mathrm{sel}} = \frac{1 + \Gamma_4\gamma^{x_0}}{2}\,\frac{1 - \mathrm{i}\gamma^{x_5}\gamma^{x_6}}{2};\\
&\text{doublets } (Q, \ell):\quad P_{\mathrm{sel}}\big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=0}
 = \big(1 - P_{\mathrm{sel}}\big)\big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=0} = 0,\qquad
 \big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=-L} = 0;\\
&\text{singlets } (u_R, d_R, e_R, \nu_R):\quad P_{\mathrm{sel}}\big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=0}
 = \big(1 - P_{\mathrm{sel}}\big)\big(1 - \gamma^{x_0}\big)\psi\big\vert_{y=0} = 0,\qquad
 \big(1 + \gamma^{x_0}\big)\psi\big\vert_{y=-L} = 0
\end{aligned}'''

NEW['bg_metric'] = r'''
\begin{aligned}
\bar g = \mathrm{diag}\Big(&\mathrm{e}^{-2a_4}b_4\cot^2z,\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ -1,\\
&-\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6}\Big),
 \qquad z = 6Hx_0
\end{aligned}'''

NEW['sectional'] = r'''
\begin{aligned}
&R^{x_1x_2}{}_{x_1x_2} = \mathcal{H}^2,\qquad R^{x_1x_4}{}_{x_1x_4} = \mathcal{H}^2 + \dot{\mathcal{H}},\qquad
 R^{x_1x_0}{}_{x_1x_0} = \mathcal{H}\mathcal{H}_f,\qquad R^{x_4x_0}{}_{x_4x_0} = \mathcal{H}_f^2 + \dot{\mathcal{H}}_f,\\
&R^{x_0x_5}{}_{x_0x_5} = \mathcal{H}_f^2 - H^2K;\\
&\text{the same for every pair of the same kind; all other $R^{ab}{}_{cd}$ with $\{a, b\} \ne \{c, d\}$ vanish}
\end{aligned}'''

NEW['stabiliser'] = r'''
\begin{aligned}
&\kappa\rho_{\mathrm{stab}} = 10H^2 - 6H^2K + \tfrac38H^2K^2 = \kappa\bar p = 3H^2K - 10H^2
 \ \Rightarrow\ K_{\pm} = 12 \pm \tfrac43\sqrt{51},\\
&K_* = 12 + \tfrac43\sqrt{51} = 21.5219,\qquad f_* = K_*^{-1/2} = 0.215556,\\
&\mathcal{G}(K_*) = \tfrac{20}{3} + \sqrt{51} = 13.8081,\qquad \kappa\rho_{\mathrm{stab}}(f_*) = \big(26 + 4\sqrt{51}\big)H^2
\end{aligned}'''

NEW['radion'] = r'''
\begin{aligned}
&\Delta\dot{\mathcal{H}} = \Xi_{\mathcal{H}K}\,\Delta K,\qquad \Delta\dot{\mathcal{H}}_f = \Xi_{fK}\,\Delta K,\qquad
 \Delta\dot K = -2K_*\,\Delta\mathcal{H}_f,\\
&\omega_{\mathrm{r}}^2 = 2K_*\,\Xi_{fK} = \Big(\frac{31552}{2249} - \frac{2416\sqrt{51}}{6747}\Big)H^2 = (3.38705\,H)^2
\end{aligned}'''

NEW['response_coeffs'] = r'''
\begin{aligned}
&\Xi_{\mathcal{H}K} = \frac{6\big(238 - 19\sqrt{51}\big)}{2249}H^2,\qquad \Xi_{fK} = \frac{4063 - 485\sqrt{51}}{2249}H^2,\qquad
 \Xi_{\mathcal{H}3} = \frac{2283}{4498} - \frac{162\sqrt{51}}{2249},\\
&\Xi_{\mathcal{H}p} = \frac{28\sqrt{51} - 114}{2249},\qquad
 \Xi_{\mathcal{H}\rho} = \frac{135021}{265382} - \frac{10308\sqrt{51}}{132691},\qquad
 \Xi_{f3} = \frac{21\sqrt{51}}{2249} - \frac{171}{4498},\\
&\Xi_{fp} = \frac{239\sqrt{51}}{6747} - \frac{485}{2249},\qquad \Xi_{f\rho} = \frac{57}{4498} - \frac{7\sqrt{51}}{2249}
\end{aligned}'''

NEW['reduction'] = r'''
\begin{aligned}
&\mathcal{L}_{(1)} = \mathcal{L}^{(4)}_{(1)} + \mathcal{L}^{(\mathrm{int})}_{(1)},\qquad
 \mathcal{L}_{(2)} = \mathcal{L}^{(4)}_{(2)} + 2\mathcal{L}^{(4)}_{(1)}\mathcal{L}^{(\mathrm{int})}_{(1)}
 + \mathcal{L}^{(\mathrm{int})}_{(2)},\qquad
 \mathcal{L}_{(3)} = 3\mathcal{L}^{(4)}_{(2)}\mathcal{L}^{(\mathrm{int})}_{(1)} + 3\mathcal{L}^{(4)}_{(1)}\mathcal{L}^{(\mathrm{int})}_{(2)},\\
&\mathcal{L}^{(4)}_{(1)} = R^{(4)},\qquad \mathcal{L}^{(4)}_{(3)} = 0,\qquad \mathcal{L}^{(\mathrm{int})}_{(1)} = -12H^2K,\qquad
 \mathcal{L}^{(\mathrm{int})}_{(2)} = 24H^4K^2,\qquad \mathcal{L}^{(\mathrm{int})}_{(3)} = 0,\\
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)} - 2\Lambda - 2\kappa\rho_{\mathrm{stab}}
 = \mathcal{G}(K)\,R^{(4)} + \text{(topological)} - 2\mathcal{G}(K)\,\Lambda_4,\\
&\Lambda_4 = \frac{6H^2K\big(1 - 2w_{(2)}K\big) + \Lambda + \kappa\rho_{\mathrm{stab}}}{\mathcal{G}(K)}
\end{aligned}'''

NEW['x0_boson_bc'] = r'''
\begin{aligned}
&\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=0} = 0\ \ \text{(even)}\quad\text{or}\quad F(0) = 0\ \ \text{(odd)},\qquad
 \frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=-1} = \beta\,F(-1),\\
&\beta = 0\ \ (\text{photon, gluons, graviton}),\qquad \beta = \beta_{\mathrm{W}}\ \ (W^\pm),\qquad
 \beta = \beta_{\mathrm{Z}} = \frac{\beta_{\mathrm{W}}}{\cos^2\theta_{\mathrm{W}}}\ \ (Z)
\end{aligned}'''

NEW['x0_boson_eig'] = r'''
\begin{aligned}
&F = \mathrm{e}^{-3HL\xi/2}\,\tilde F,\qquad \varpi^2 = \tilde m^2 - \frac{9H^2L^2}{4}:\\
&\text{even: }\Big[\varpi^2 + \frac{3HL}{2}\Big(\beta + \frac{3HL}{2}\Big)\Big]\sin\varpi - \beta\,\varpi\cos\varpi = 0,\qquad
 \text{odd: }\varpi\cos\varpi + \Big(\beta + \frac{3HL}{2}\Big)\sin\varpi = 0;\\
&\beta = 0:\quad \tilde m = 0\ \text{(flat profile)},\qquad \tilde m_n^2 = \frac{9H^2L^2}{4} + \varpi_n^2\ \text{(even)},\qquad
 \varpi\cot\varpi = -\frac{3HL}{2}\ \text{(odd)}
\end{aligned}'''

NEW['kk_tower'] = r'''
\begin{aligned}
&F_n(\xi) = \mathrm{e}^{-3HL\xi/2}\Big(\cos\varpi_n\xi + \frac{3HL}{2\varpi_n}\sin\varpi_n\xi\Big),\qquad
 \varpi_n = \pi,\ 2\pi,\ 3\pi,\ \dots,\\
&\tilde m_n^2 = \frac{9H^2L^2}{4} + \varpi_n^2,\qquad m^{\mathrm{KK}}_n = \frac{\tilde m_n}{fL},\qquad
 N_n = \int_{-1}^{0}\mathrm{e}^{3HL\xi}F_n^2\,\mathrm{d}\xi = \frac12\Big(1 + \frac{9H^2L^2}{4\varpi_n^2}\Big),\qquad
 N_0 = \frac{1 - \mathrm{e}^{-3HL}}{3HL}
\end{aligned}'''

NEW['ferm_red'] = r'''
\begin{aligned}
&\Psi = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\mathcal{V}\chi(y, x_4):\\
&\gamma^MD_M\Psi - \big(M(y) - \mathrm{i}v(y)\gamma^{x_4}\big)\Psi
 = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\gamma^{x_4}\mathcal{V}
 \big[\partial_{x_4}\chi + \mathrm{i}h\chi\big],\\
&h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M(y)\,\sigma_2 + \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y),\qquad
 \mathrm{i}\,\partial_{x_4}\chi = h\chi;\\
&\text{in each block: }\gamma^{x_0} = \sigma_3,\qquad \mathcal{B} = \varsigma\varsigma_2,\qquad
 C = \varsigma_2\sigma_2,\qquad \Gamma_4 = -\varsigma\varsigma_2\sigma_3
\end{aligned}'''

NEW['ferm_zero'] = r'''
\begin{aligned}
&\chi = \big(\mathrm{e}^{c\xi},\ 0\big)^T\ \ (\text{doublet},\ \Gamma_4 = +1),\qquad
 \chi = \big(0,\ \mathrm{e}^{-c\xi}\big)^T\ \ (\text{singlet},\ \Gamma_4 = -1),\qquad c = f\mu L,\\
&h\big(\mathrm{e}^{c\xi},\ 0\big)^T = \varsigma\,\mathrm{e}^{-a_4}k\big(\mathrm{e}^{c\xi},\ 0\big)^T
\end{aligned}'''

NEW['ferm_1gen'] = r'''
\begin{aligned}
&\mathcal{D}(\tilde\varepsilon) = \tilde\varepsilon^2\,\frac{\sinh\upsilon_L}{\upsilon_L}\frac{\sinh\upsilon_R}{\upsilon_R}
 - \mathcal{K}^2\Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L}\Big)
 \Big(\cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big) = 0,\\
&\tilde\varepsilon \simeq \mathcal{K}\,\mathcal{Z}(c_L)\,\mathcal{Z}(-c_R),\qquad \mathcal{Z}(c)^2 = \frac{c\,\mathrm{e}^{-c}}{\sinh c}
\end{aligned}'''

NEW['ferm_3gen'] = r'''
\begin{aligned}
&\Big[\mathrm{diag}\big(b_{L\alpha}\big) + \mathcal{K}\,\mathrm{diag}\Big(\frac{b_{Ri}}{a_{Ri}}\Big)\mathcal{K}^\dagger\,
 \mathrm{diag}\big(a_{L\alpha}\big)\Big]\boldsymbol{\alpha} = 0;\qquad
 \det\big[\cdots\big] = \prod_{i=1}^{3}\frac{b_La_{Ri} + a_Lb_{Ri}}{a_{Ri}},\\
&b_La_R + a_Lb_R = -\mathcal{D}(\tilde\varepsilon)\big\vert_{\mathcal{K} = 1},\qquad
 \boldsymbol{\alpha}^{(i)} = \mathcal{K}\,\mathbf{u}_i,\qquad \boldsymbol{\beta}^{(i)} \propto \mathbf{u}_i,\qquad
 U = \mathcal{K}_e^\dagger\mathcal{K}_\nu,\qquad V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d
\end{aligned}'''

NEW['psi_spectrum'] = r'''
\begin{aligned}
&\text{even: }\chi = \big(\mathrm{e}^{c_\Psi\xi},\ 0\big)^T,\ \varepsilon = 0\ \text{(all eight blocks)},\qquad
 \varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi_n}{fL}\Big)^2},\ \varpi_n = \pi,\ 2\pi,\ \dots;\\
&\text{odd: }\varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2},\quad \tan\varpi = -\frac{\varpi}{c_\Psi};\qquad
 c_\Psi = f\,m_\Psi L;\qquad \text{fold band: }\varepsilon = \mathrm{e}^{-a_4}\lvert k\rvert
\end{aligned}'''

NEW['ks_dens'] = r'''
\begin{aligned}
&n = \sum_o\tfrac12\,d_o\,\phi_o\,n_o,\qquad n^{\mathrm{sc}} = \sum_o\tfrac12\,d_o\,\phi_o\,n^{\mathrm{sc}}_o,\qquad
 n_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\chi_o,\\
&n^{\mathrm{sc}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_2\chi_o,\qquad
 n^{\mathrm{t}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_3\chi_o,\qquad
 d_o = 4\,r_3\big(\lvert\vec n_o\rvert^2\big),\qquad \vec k_o = k_{\mathrm{lat}}\,\vec n_o,\\
&\mathrm{Vol}_7 = \Big(\frac{2\pi}{k_{\mathrm{lat}}}\Big)^3v_{\mathrm{t}}\,f^4,\qquad
 \phi_o = \frac{1}{\mathrm{e}^{(\varepsilon_o - \mu_{\mathrm{chem}})/T} + 1}\ \ \text{(Mermin; or 0 and 1 for the aufbau)}
\end{aligned}'''

NEW['contact4d'] = r'''
\begin{aligned}
&\mathcal{L}_4 = \big(G_{\mathrm{V}}\,q_f\,\tilde I_{of} + G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of}\big)
 \big(\mathrm{i}\bar\Psi_o\gamma^\mu\Psi_o\big)\big(\mathrm{i}\bar\psi_f\gamma_\mu\psi_f\big),\\
&\tilde I_{of} = \frac{1}{H}\int_{-L}^{0}\big(a_o^2 + b_o^2\big)\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 \tilde I^{(b)}_{of} = \frac{1}{H}\int_{-L}^{0}b_o^2\,\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 G_{\mathrm{V}} = \frac{c_{\mathrm{V}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\qquad
 G_{\mathrm{A}} = \frac{c_{\mathrm{A}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\\
&n_{\psi i}(y) = \frac{n_f\,\varrho_f(y)\,\mathrm{e}^{-3Hy}}{2f^4v_{\mathrm{t}}},\qquad
 \varrho(y; c) = \frac{2c}{L}\,\frac{\mathrm{e}^{2cy/L}}{1 - \mathrm{e}^{-2c}}
\end{aligned}'''

NEW['vector_cond'] = r'''
\begin{aligned}
&\big\langle F^V_{\mu\nu}F^{V}{}^{\mu\nu}\big\rangle(T) = -2\,\Theta_V\ \ \text{(for $V = W^\pm, Z$)},\qquad
 \big\langle F_{\mathrm{geo}}^2\big\rangle = -4\,\frac{\partial p}{\partial\big(1/g_{\mathrm{G}}^2\big)} = 4g_{\mathrm{G}}^2\,p_{\alpha,\mathrm{G}},\\
&p_{\alpha,\mathrm{G}} = -\frac{g_{\mathrm{G}}^2T^4}{144}\,d_{\mathrm{adj}}\Big[C_{\mathrm{adj}} + \frac52\,T_{\mathrm{F}}N_{\mathrm{f}}\Big]
\end{aligned}'''

NEW['dm_on_sm'] = r'''
\begin{aligned}
&\frac{\Delta\alpha_3}{\alpha_3} = -4G_{\mathrm{g}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_2}{\alpha_2} = -4G_{\mathrm{W}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_1}{\alpha_1} = -4G_{\mathrm{B}}\,n_{\mathrm{DM,tot}},\\
&-\frac{1}{\Upsilon\,\mathrm{e}^{3HL\xi}}\,\frac{\mathrm{d}}{\mathrm{d}\xi}\Big(\Upsilon\,\mathrm{e}^{3HL\xi}\,\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)
 = \tilde m^2F,\qquad \Upsilon(\xi) = 1 + A_{\mathrm{mf}}\,n^{\mathrm{sc}}_{\mathrm{DM}},\qquad
 n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}},\\
&\frac{\mathrm{d}F}{\mathrm{d}\xi}(0) = 0,\qquad \Upsilon(-1)\,\frac{\mathrm{d}F}{\mathrm{d}\xi}(-1) = \beta_{\mathrm{W}}F(-1)
\end{aligned}'''

NEW['coupled_block'] = r'''
\begin{aligned}
&\Delta K = \frac{c_\rho\,\kappa\Delta\rho + c_3\,\kappa\Delta p_3 + c_p\,\kappa\Delta\bar p}{H^2},\qquad
 \Delta\ln f = -\frac{\Delta K}{2K_*},\\
&\Delta\ln m_s = \frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}\,\Delta\ln f,\qquad
 \kappa\Delta\rho = 8\pi G_{\mathrm{N}}\,\mathcal{G}(K_*)\,\rho_4
\end{aligned}'''

NEW['env'] = r'''
\begin{aligned}
&n_{\mathrm{p}} + n_{\mathrm{n}} = \eta_{\mathrm{b}}\,n_\gamma,\qquad n_\gamma = \frac{2\zeta(3)}{\pi^2}\,T^3,\qquad
 \frac{n_{\mathrm{n}}}{n_{\mathrm{p}}} = \mathrm{e}^{-(m_{\mathrm{n}} - m_{\mathrm{p}})/T},\qquad n_{\mathrm{e}} = n_{\mathrm{p}},\\
&n_{\mathrm{DM,tot}} = 2\big(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}\big) = 2\cdot4\,\Big(\frac{M_{\mathrm{DM}}T}{2\pi}\Big)^{3/2}\mathrm{e}^{-M_{\mathrm{DM}}/T}
 \ \ \Big(\frac{M_{\mathrm{DM}}}{T} < 40\Big)
\end{aligned}'''

NEW['pert_einstein'] = r'''
\begin{aligned}
&k^2\Psi_{\mathrm{N}} + 3a_4'\big(\Psi_{\mathrm{N}}' + a_4'\Phi\big) = -4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\,\Delta\rho,\qquad
 k^2\big(\Psi_{\mathrm{N}}' + a_4'\Phi\big) = 4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\big(\rho_{\mathrm{tot}} + p_{\mathrm{tot}}\big)\theta_{\mathrm{tot}},\\
&\Psi_{\mathrm{N}}'' + a_4'\big(\Phi' + 2\Psi_{\mathrm{N}}'\big) + \big(2a_4'' + a_4'^2\big)\Phi + \frac{k^2}{3}\big(\Psi_{\mathrm{N}} - \Phi\big)
 = 4\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\,\Delta p,\\
&k^2\big(\Psi_{\mathrm{N}} - \Phi\big) = 12\pi G_{\mathrm{N}}\,\mathrm{e}^{2a_4}\big(\rho_{\mathrm{tot}} + p_{\mathrm{tot}}\big)\sigma_{\mathrm{an}}
\end{aligned}'''

NEW['phi_rms'] = r'''
\begin{aligned}
&\Phi_{\mathrm{rms}}(k) = \Big[\frac{k^3P_{\Phi_{\mathrm{W}}}(k)}{2\pi^2}\Big]^{1/2},\qquad
 \Phi_{\mathrm{W}} = \frac{\Phi + \Psi_{\mathrm{N}}}{2},\qquad
 \Phi_{\mathrm{W}} = \frac32\,\Omega_{\mathrm{m}}\mathcal{H}_0^2\,\frac{\delta_{\mathrm{m}}}{\mathrm{e}^{a_4}k^2}\ \ \text{(inside the horizon)},\\
&\Phi_{\mathrm{W}} = \frac35\,\mathcal{R}\,\mathrm{e}^{-a_4}D_+\ \ \text{(largest scales)},\qquad
 D_+ = \frac52\,\Omega_{\mathrm{m}}\,\frac{\mathcal{H}}{\mathcal{H}_0}\int_{-\infty}^{a_4}\Big(\frac{\mathcal{H}_0}{\mathcal{H}}\Big)^3
 \mathrm{e}^{-2\tilde a_4}\,\mathrm{d}\tilde a_4,\\
&\frac{\mathcal{H}}{\mathcal{H}_0} = \big(\Omega_{\mathrm{m}}\mathrm{e}^{-3a_4} + 1 - \Omega_{\mathrm{m}}\big)^{1/2}
\end{aligned}'''

NEW['pee'] = r'''
\begin{aligned}
&\mathcal{P}_{ee} = c_{13}^4\Big(\frac12 + \frac12\cos2\theta_{12}\cos2\theta^{\mathrm{m}}_{12}\Big) + s_{13}^4,\qquad
 A_{\mathrm{MSW}} = \frac{2E\,V_{\mathrm{CC}}\,c_{13}^2}{\Delta m_{21}^2},\\
&\cos2\theta^{\mathrm{m}}_{12} = \frac{\cos2\theta_{12} - A_{\mathrm{MSW}}}{\sqrt{\big(\cos2\theta_{12} - A_{\mathrm{MSW}}\big)^2
 + \sin^22\theta_{12}}}
\end{aligned}'''

NEW['qed_pressure'] = r'''
\begin{aligned}
&p_{\mathrm{QED}} = p_{\mathrm{QED}}^{(2)} + p_{\mathrm{QED}}^{(3)},\qquad
 p_{\mathrm{QED}}^{(2)} = -\frac{e^2T^2}{12\pi^2}\,\mathcal{Q}_1 - \frac{e^2}{8\pi^4}\,\mathcal{Q}_1^2
 + \frac{e^2m_{\mathrm{e}}^2}{16\pi^4}\,\mathcal{Q}_2,\\
&p_{\mathrm{QED}}^{(3)} = \frac{e^3T}{12\pi^4}\,\mathcal{Q}_3^{3/2},\qquad
 \rho_{\mathrm{QED}} = -p_{\mathrm{QED}} + T\,\frac{\mathrm{d}p_{\mathrm{QED}}}{\mathrm{d}T}
\end{aligned}'''

NEW['ffi_homog'] = r'''
\begin{aligned}
&\mathrm{i}\,\frac{\mathrm{d}\mathcal{C}(u)}{\mathrm{d}x_4} = \big(\mathcal{I}_0 - u\,\mathcal{I}_1\big)\mathcal{C}(u)
 - \int_{-1}^{1}\frac{\mathrm{d}\tilde u}{2}\,G_{\mathrm{ELN}}(\tilde u)\,(1 - u\tilde u)\,\mathcal{C}(\tilde u);\\
&\bar\omega^2 - \big(\mathcal{I}_2 - \mathcal{I}_0\big)\bar\omega - \big(\mathcal{I}_0\mathcal{I}_2 - \mathcal{I}_1^2\big) = 0,\qquad
 \mathrm{Im}\,\bar\omega = \frac12\sqrt{4\mathcal{I}_1^2 - \big(\mathcal{I}_0 + \mathcal{I}_2\big)^2}
\end{aligned}'''

NEW['xsec'] = r'''
\begin{aligned}
&\sigma_{\mathrm{I12}} = \frac{G_{\mathrm{I12}}^2\,E_{\mathrm{cm}}^3\big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)^{1/2}}{8\pi},\qquad
 G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2,\\
&\sigma_{\mathrm{I13}} = \sum_f\frac{N_{\mathrm{c}}\,G_f^2\,E_{\mathrm{cm}}^2\big(1 + 2M_{\mathrm{DM}}^2/E_{\mathrm{cm}}^2\big)}{24\pi\beta_{\mathrm{cm}}},
 \qquad G_f = G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of},\\
&\beta_{\mathrm{cm}} = \sqrt{1 - \frac{4M_{\mathrm{DM}}^2}{E_{\mathrm{cm}}^2}},\qquad
 k_{\mathrm{cm}} = \sqrt{\frac{E_{\mathrm{cm}}^2}{4} - M_{\mathrm{DM}}^2}
\end{aligned}'''


def replace(name, latex):
    for f in sorted(Path('.').glob('eq_*.py')):
        s = f.read_text()
        key = "name='%s')" % name
        k = s.find(key)
        if k < 0:
            continue
        start = s.rfind("\nE('", 0, k)
        a = s.index("r'''", start) + 4
        b = s.index("'''", a)
        assert b < k, name
        s = s[:a] + latex + s[b:]
        f.write_text(s)
        return f.name
    raise SystemExit('not found: ' + name)


if __name__ == '__main__':
    names = sys.argv[1:] or list(NEW)
    for n in names:
        print(n, replace(n, NEW[n]))
