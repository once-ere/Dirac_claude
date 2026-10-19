from build_lib import R

R('metric', r'g_{MN}', ['g'], r'The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order '
  r'$x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, '
  r'and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume '
  r'element.', 'dimensionless', status='AUTHOR')
R('gbar', r'\bar g_{MN}', [r'\bar g'], r'The order-0 (background) metric of the power series: the corrected primordial metric in the '
  r"author's coordinates, determined by the two functions $a_4(x_4)$ and $b_4(x_4)$; $\lvert\bar g\rvert$ is the absolute value "
  r'of its determinant.', 'dimensionless', status='AUTHOR')
R('gtip', r'g_{\mathrm{tip}}', [r'g_{\mathrm{tip}}'], r'The metric induced on the seven-dimensional tip $y = -L$ (the metric '
  r'$g_{MN}$ restricted to the tip directions $x_1, \dots, x_7$); $\lvert g_{\mathrm{tip}}\rvert$ is the absolute value of its '
  r'determinant.', 'dimensionless', status='DERIVED')
R('gperp', r'g_\perp', [r'g_\perp'], r'The metric of the four transverse directions $x_0, x_5, x_6, x_7$ (the block); '
  r'$\lvert g_\perp\rvert$ is the absolute value of its determinant.', 'dimensionless', status='DERIVED')
R('g4', r'g^{(4)}_{\mu\nu}', [r'g^{(4)}'], r'The four-dimensional metric of the observable coordinates $x_1, \dots, x_4$ (the '
  r'metric of the effective four-dimensional general relativity on the stabilised block).', 'dimensionless', status='DERIVED')
R('Riemann', r'R^{MN}{}_{PQ},\ R_{MN},\ R', ['R'], r'The curvature of the metric $g_{MN}$: with four indices the Riemann tensor, '
  r'with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the Ricci (scalar) curvature $R = g^{MN}R_{MN}$; '
  r'$R^{ab}{}_{ab}$ (no sum) is the sectional curvature of the coordinate plane $(a, b)$.', '1/length^2', status='STANDARD')
R('R4', r'R^{(4)}', [r'R^{(4)}'], r'The Ricci scalar of the four-dimensional metric $g^{(4)}_{\mu\nu}$.', '1/length^2',
  status='STANDARD')
R('Christoffel', r'\Gamma^N{}_{MP}', [r'\Gamma'], r'The Christoffel symbols (the Levi-Civita connection) of the metric, '
  r'$\Gamma^N{}_{MP} = \frac12 g^{NQ}(\partial_Mg_{QP} + \partial_Pg_{QM} - \partial_Qg_{MP})$.', '1/length', status='STANDARD')
R('kappa', r'\kappa', [r'\kappa'], r'The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$.', 'GeV^-6',
  r'$\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$', 'AUTHOR')
R('G8', r'G_8', [r'G_8'], r"The eight-dimensional Newton constant ($\kappa = 8\pi G_8$).", 'GeV^-6', status='AUTHOR')
R('Lambda', r'\Lambda', [r'\Lambda'], r'The eight-dimensional cosmological constant, $\Lambda = -10H^2$.', 'GeV^2',
  r'$-10H^2$', 'AUTHOR')
R('Lambda4', r'\Lambda_4', [r'\Lambda_4'], r'The four-dimensional cosmological constant of the effective theory on the block, '
  r'$\Lambda_4 = [6H^2K(1 - 2w_{(2)}K) + \Lambda + \kappa\rho_{\mathrm{stab}}]/\mathcal{G}(K)$; zero at the static point, the '
  r'observed dark energy a tuned residual.', 'GeV^2', r'0 at the static point; observed $\Lambda_4/H^2 \sim 10^{-92}$', 'DERIVED')
R('alphaL', r'\alpha_{(p)}', [r'\alpha'], r'The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$).',
  r'GeV^(2-2p)', status='AUTHOR')
R('wL', r'w_{(p)}', ['w'], r"The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$.", 'dimensionless',
  r'$(1, 1/32, 1/1152)$', 'AUTHOR')
R('Lov', r'\mathcal{L}_{(p)}', [r'\mathcal{L}'], r'The Lovelock density of order $p$ of the metric (a scalar built from $p$ '
  r'Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ '
  r'the cubic Lovelock density.', '1/length^(2p)', status='STANDARD')
R('Lov4', r'\mathcal{L}^{(4)}_{(r)}', [r'\mathcal{L}^{(4)}'], r'The Lovelock density of order $r$ of the four-dimensional metric '
  r'$g^{(4)}_{\mu\nu}$ ($\mathcal{L}^{(4)}_{(1)} = R^{(4)}$; the order 2 is topological and the order 3 vanishes in four '
  r'dimensions).', '1/length^(2r)', status='STANDARD')
R('Lovint', r'\mathcal{L}^{(\mathrm{int})}_{(r)}', [r'\mathcal{L}^{(\mathrm{int})}'], r'The Lovelock density of order $r$ of the '
  r'static block (a four-dimensional space of constant curvature $-H^2K$): 1, $-12H^2K$, $24H^4K^2$, 0 for $r = 0, 1, 2, 3$.',
  '1/length^(2r)', status='DERIVED')
R('LovE', r'\mathcal{E}_{(p)}{}^M{}_N', [r'\mathcal{E}'], r'The Lovelock tensor of order $p$, the metric variation of '
  r'$\sqrt{\lvert g\rvert}\mathcal{L}_{(p)}$: $\mathcal{E}_{(1)}$ is the Einstein tensor $R^M{}_N - \frac12\delta^M_NR$; every '
  r'$\mathcal{E}_{(p)}$ is divergence free.', '1/length^(2p)', status='STANDARD')
R('Saction', r'S', ['S'], r'The action of UM-2 (the integral of the Lagrangian density over spacetime); its variation with respect '
  r'to every field gives the field equations.', 'dimensionless (hbar = 1)', status='ASSUMED')
R('SEL', r'S_{\mathrm{EL}}', [r'S_{\mathrm{EL}}'], r'The Einstein-Lovelock action of gravity.', 'dimensionless', status='AUTHOR')
R('Sstab', r'S_{\mathrm{stab}}', [r'S_{\mathrm{stab}}'], r'The action of the block stabiliser (a vacuum energy of the block).',
  'dimensionless', status='ASSUMED')
R('SPsi', r'S_\Psi', [r'S_\Psi'], r'The action of the dirac16complex field (kinetic term with the canonical spin connection, mass '
  r'term and contact self-interaction).', 'dimensionless', status='RECORD')
R('Sgauge', r'S_{\mathrm{gauge}}', [r'S_{\mathrm{gauge}}'], r'The action of the gauge fields of SU(3), SU(2) and U(1)$_Y$ in eight '
  r'dimensions.', 'dimensionless', status='ASSUMED')
R('Sf', r'S_{\mathrm{f}}', [r'S_{\mathrm{f}}'], r'The action of the Standard-Model fermions of three generations (kinetic and '
  r'bulk-mass terms).', 'dimensionless', status='ASSUMED')
R('Stip', r'S_{\mathrm{tip}}', [r'S_{\mathrm{tip}}'], r'The action on the tip $y = -L$: the sigma field and the tip Yukawa '
  r'couplings.', 'dimensionless', status='INVENTED')
R('SI11', r'S_{\mathrm{I11}}', [r'S_{\mathrm{I11}}'], r'The action of the portal I11 (dirac16complex vector current times the '
  r'$B - L$ current of the fermions).', 'dimensionless', status='INVENTED')
R('SI12', r'S_{\mathrm{I12}}', [r'S_{\mathrm{I12}}'], r'The action of the portal I12 (scalar density of dirac16complex times the '
  r'gauge kinetic invariants).', 'dimensionless', status='INVENTED')
R('SI13', r'S_{\mathrm{I13}}', [r'S_{\mathrm{I13}}'], r'The action of the portal I13 (the $x_0$-chiral vector current of '
  r'dirac16complex times the baryon-number current).', 'dimensionless', status='INVENTED')
R('Sm', r'S_{\mathrm{m}}', [r'S_{\mathrm{m}}'], r'The matter action: all terms of the action except $S_{\mathrm{EL}}$ (the '
  r'stabiliser included).', 'dimensionless', status='DERIVED')
R('rhostab', r'\rho_{\mathrm{stab}}', [r'\rho_{\mathrm{stab}}'], r'The energy density of the block stabiliser, a function of the '
  r'block scale, $\rho_{\mathrm{stab}} \propto f^{-8}$; its value at the static block is $\rho_{\mathrm{stab}}(f_*)$.', 'GeV^8',
  r'$\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2 = 54.566\,H^2$', 'ASSUMED')
R('fblock', r'f', ['f'], r'The block scale: the common scale factor of the hidden direction and the extra times, '
  r'$f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$).',
  'dimensionless', status='DERIVED')
R('fstar', r'f_*', [r'f_*'], r'The block scale of the stabilised (static) block, $f_* = K_*^{-1/2}$.', 'dimensionless', '0.215556',
  'DERIVED')
R('a4', r'a_4', [r'a_4'], r"The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of "
  r'cosmology is $\mathrm{e}^{a_4}$.', 'dimensionless', status='AUTHOR')
R('a4tilde', r'\tilde a_4', [r'\tilde a_4'], r'An earlier value of $a_4$ (the integration variable of the growth integral).',
  'dimensionless', status='STANDARD')
R('b4', r'b_4', [r'b_4'], r"The author's metric function of the time $x_4$ in the hidden and extra-time components, "
  r'$b_4 > 0$.', 'dimensionless', status='AUTHOR')
R('a4dot', r'\dot a_4', [r'\dot a_4'], r'The time derivative $\mathrm{d}a_4/\mathrm{d}x_4$.', 'GeV', status='DERIVED')
R('b4dot', r'\dot b_4', [r'\dot b_4'], r'The time derivative $\mathrm{d}b_4/\mathrm{d}x_4$.', 'GeV', status='DERIVED')
R('fdot', r'\dot f', [r'\dot f'], r'The time derivative $\mathrm{d}f/\mathrm{d}x_4$ of the block scale.', 'GeV', status='DERIVED')
R('Kblock', r'K', ['K'], r'The block variable, $K = 1/f^2$.', 'dimensionless', status='DERIVED')
R('Kstar', r'K_*', [r'K_*'], r'The block variable of the stabilised block, $K_* = 12 + \frac43\sqrt{51}$ (the upper root '
  r'$K_+$).', 'dimensionless', '21.5219', 'DERIVED')
R('Kpm', r'K_\pm', [r'K_\pm'], r'The two static blocks with the stabiliser, $K_\pm = 12 \pm \frac43\sqrt{51}$.', 'dimensionless',
  r'21.5219 and 2.4781', 'DERIVED')
R('Kdot', r'\dot K', [r'\dot K'], r'The time derivative $\mathrm{d}K/\mathrm{d}x_4$.', 'GeV', status='DERIVED')
R('Kddot', r'\ddot K', [r'\ddot K'], r'The second time derivative $\mathrm{d}^2K/\mathrm{d}x_4^2$.', 'GeV^2', status='DERIVED')
R('Hubble', r'\mathcal{H}', [r'\mathcal{H}'], r'The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate '
  r'of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$).', 'GeV', status='DERIVED')
R('Hf', r'\mathcal{H}_f', [r'\mathcal{H}_f'], r'The expansion rate of the block, $\mathcal{H}_f = \dot f/f = \dot b_4/(2b_4) - '
  r'\dot a_4$ (negative when the extra times and $x_0$ deflate).', 'GeV', status='DERIVED')
R('Hdot', r'\dot{\mathcal{H}}', [r'\dot{\mathcal{H}}'], r'The time derivative $\mathrm{d}\mathcal{H}/\mathrm{d}x_4$.', 'GeV^2',
  status='DERIVED')
R('Hfdot', r'\dot{\mathcal{H}}_f', [r'\dot{\mathcal{H}}_f'], r'The time derivative $\mathrm{d}\mathcal{H}_f/\mathrm{d}x_4$.',
  'GeV^2', status='DERIVED')
R('H0', r'\mathcal{H}_0', [r'\mathcal{H}_0'], r'The Hubble rate today (the Hubble constant).', 'GeV (km/s/Mpc)',
  r'67.38 km/s/Mpc', 'DERIVED')
R('EMT', r'\mathcal{T}^M{}_N', [r'\mathcal{T}'], r'The energy-momentum tensor of all matter (every field except gravity, the '
  r'stabiliser included), the source of gravity; defined by the change of the matter action under a change of the metric.',
  'GeV^8', status='STANDARD')
R('Tstab', r'\mathcal{T}_{\mathrm{stab}}', [r'\mathcal{T}_{\mathrm{stab}}'], r'The energy-momentum tensor of the stabiliser.',
  'GeV^8', status='DERIVED')
R('TPsi', r'\mathcal{T}_\Psi', [r'\mathcal{T}_\Psi'], r'The energy-momentum tensor of the dirac16complex field.', 'GeV^8',
  status='DERIVED')
R('Tgauge', r'\mathcal{T}_{\mathrm{gauge}}', [r'\mathcal{T}_{\mathrm{gauge}}'], r'The energy-momentum tensor of the gauge fields.',
  'GeV^8', status='STANDARD')
R('Tf', r'\mathcal{T}_{\mathrm{f}}', [r'\mathcal{T}_{\mathrm{f}}'], r'The energy-momentum tensor of the Standard-Model fermions.',
  'GeV^8', status='DERIVED')
R('Ttip', r'\mathcal{T}_{\mathrm{tip}}', [r'\mathcal{T}_{\mathrm{tip}}'], r'The energy-momentum tensor of the tip terms (non-zero '
  r'only for the tip directions).', 'GeV^8', status='DERIVED')
R('TI11', r'\mathcal{T}_{\mathrm{I11}}', [r'\mathcal{T}_{\mathrm{I11}}'], r'The energy-momentum tensor of the portal I11.', 'GeV^8',
  status='DERIVED')
R('TI12', r'\mathcal{T}_{\mathrm{I12}}', [r'\mathcal{T}_{\mathrm{I12}}'], r'The energy-momentum tensor of the portal I12.', 'GeV^8',
  status='DERIVED')
R('TI13', r'\mathcal{T}_{\mathrm{I13}}', [r'\mathcal{T}_{\mathrm{I13}}'], r'The energy-momentum tensor of the portal I13.', 'GeV^8',
  status='DERIVED')
R('T4', r'\mathcal{T}^{(4)}_{\mu\nu}', [r'\mathcal{T}^{(4)}'], r'The four-dimensional energy-momentum tensor: '
  r'$\mathcal{T}_{\mu\nu}$ integrated over the block (both halves of a period of $x_0$ and the extra times).', 'GeV^4',
  status='DERIVED')
R('rho', r'\rho', [r'\rho'], r'An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or '
  r'of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological '
  r'perturbation equations $\Delta\rho$ is the density perturbation summed over the species.', 'GeV^8 (eight dimensions), GeV^4 '
  r'(four dimensions)', status='STANDARD')
R('rhodot', r'\dot\rho', [r'\dot\rho'], r'The time derivative $\mathrm{d}\rho/\mathrm{d}x_4$.', 'GeV^9', status='STANDARD')
R('pressure', r'p', ['p'], r'A pressure: $p_M = \mathcal{T}^M{}_M$ (no sum) for the direction $M \ne x_4$, $p_s$ the pressure of '
  r'the species $s$; $\Delta p$ the pressure perturbation in the cosmological perturbation equations; in the Feynman-Hellmann '
  r'relation the pressure of a gauge plasma.', 'GeV^8 (eight dimensions), GeV^4 (four dimensions)', status='STANDARD')
R('p0', r'p_0', [r'p_0'], r'The pressure along the hidden direction $x_0$, $p_0 = \mathcal{T}^{x_0}{}_{x_0}$.', 'GeV^8',
  status='STANDARD')
R('p3', r'p_3', [r'p_3'], r'The pressure of ordinary 3-space, $p_3 = \mathcal{T}^{x_1}{}_{x_1} = \mathcal{T}^{x_2}{}_{x_2} = '
  r'\mathcal{T}^{x_3}{}_{x_3}$ for an isotropic source.', 'GeV^8', status='STANDARD')
R('p5', r'p_5', [r'p_5'], r'The pressure along the extra times, $p_5 = \mathcal{T}^{x_5}{}_{x_5} = \mathcal{T}^{x_6}{}_{x_6} = '
  r'\mathcal{T}^{x_7}{}_{x_7}$.', 'GeV^8', status='STANDARD')
R('pbar', r'\bar p', [r'\bar p'], r'The hidden pressure, the pressure averaged over the block, $\bar p = (p_0 + 3p_5)/4$; for a '
  r'species at fixed temperature $\bar p = \frac14\,\partial p/\partial\ln f$.', 'GeV^8 (or GeV^4 for a four-dimensional density)',
  status='DERIVED')
R('GK', r'\mathcal{G}(K)', [r'\mathcal{G}'], r'The coefficient of the four-dimensional Einstein-Hilbert term on a static block, '
  r'$\mathcal{G}(K) = 1 - 24w_{(2)}K + 72w_{(3)}K^2 = (K^2 - 12K + 16)/16$; four-dimensional gravity is attractive for '
  r'$\mathcal{G} > 0$.', 'dimensionless', r'$\mathcal{G}(K_*) = 20/3 + \sqrt{51} = 13.8081$', 'DERIVED')
R('XiHK', r'\Xi_{\mathcal{H}K}', [r'\Xi_{\mathcal{H}K}'], r'The coefficient of $\Delta K$ in the first-order equation for '
  r'$\Delta\dot{\mathcal{H}}$ (linearised block about $K_*$).', 'GeV^2', r'$6(238 - 19\sqrt{51})H^2/2249 = 0.272956\,H^2$',
  'DERIVED')
R('XifK', r'\Xi_{fK}', [r'\Xi_{fK}'], r'The coefficient of $\Delta K$ in the first-order equation for $\Delta\dot{\mathcal{H}}_f$.',
  'GeV^2', r'$(4063 - 485\sqrt{51})H^2/2249 = 0.266522\,H^2$', 'DERIVED')
R('XiH3', r'\Xi_{\mathcal{H}3}', [r'\Xi_{\mathcal{H}3}'], r'The coefficient of $\kappa\Delta p_3$ in the equation for '
  r'$\Delta\dot{\mathcal{H}}$.', 'dimensionless', r'$2283/4498 - 162\sqrt{51}/2249 = -0.006853$', 'DERIVED')
R('XiHp', r'\Xi_{\mathcal{H}p}', [r'\Xi_{\mathcal{H}p}'], r'The coefficient of $\kappa\Delta\bar p$ in the equation for '
  r'$\Delta\dot{\mathcal{H}}$.', 'dimensionless', r'$(28\sqrt{51} - 114)/2249 = 0.038221$', 'DERIVED')
R('XiHrho', r'\Xi_{\mathcal{H}\rho}', [r'\Xi_{\mathcal{H}\rho}'], r'The coefficient of $\kappa\Delta\rho$ in the equation for '
  r'$\Delta\dot{\mathcal{H}}$.', 'dimensionless', r'$135021/265382 - 10308\sqrt{51}/132691 = -0.045997$', 'DERIVED')
R('Xif3', r'\Xi_{f3}', [r'\Xi_{f3}'], r'The coefficient of $\kappa\Delta p_3$ in the equation for $\Delta\dot{\mathcal{H}}_f$.',
  'dimensionless', r'$21\sqrt{51}/2249 - 171/4498 = 0.028666$', 'DERIVED')
R('Xifp', r'\Xi_{fp}', [r'\Xi_{fp}'], r'The coefficient of $\kappa\Delta\bar p$ in the equation for $\Delta\dot{\mathcal{H}}_f$.',
  'dimensionless', r'$239\sqrt{51}/6747 - 485/2249 = 0.037320$', 'DERIVED')
R('Xifrho', r'\Xi_{f\rho}', [r'\Xi_{f\rho}'], r'The coefficient of $\kappa\Delta\rho$ in the equation for '
  r'$\Delta\dot{\mathcal{H}}_f$.', 'dimensionless', r'$57/4498 - 7\sqrt{51}/2249 = -0.009555$', 'DERIVED')
R('crho', r'c_\rho', [r'c_\rho'], r'The coefficient of $\kappa\Delta\rho$ in the adiabatic block response $\Delta K$.',
  'dimensionless', '0.0358521', 'DERIVED')
R('c3', r'c_3', [r'c_3'], r'The coefficient of $\kappa\Delta p_3$ in the adiabatic block response, $c_3 = -3c_\rho$ (so radiation '
  r'drops out).', 'dimensionless', '-0.107556', 'DERIVED')
R('cp', r'c_p', [r'c_p'], r'The coefficient of $\kappa\Delta\bar p$ in the adiabatic block response.', 'dimensionless',
  '-0.140028', 'DERIVED')
R('omegar', r'\omega_{\mathrm{r}}', [r'\omega_{\mathrm{r}}'], r'The angular frequency of the oscillation of the block about the '
  r'static point (the radion), equal to the radion mass.', 'GeV', r'$3.38705\,H = 48.42$ TeV', 'DERIVED')
R('G4tensor', r'G^{(4)}_{\mu\nu}', [r'G^{(4)}'], r'The Einstein tensor of the four-dimensional metric, '
  r'$R^{(4)}_{\mu\nu} - \frac12 g^{(4)}_{\mu\nu}R^{(4)}$.', '1/length^2', status='STANDARD')
R('GN', r'G_{\mathrm{N}}', [r'G_{\mathrm{N}}'], r"Newton's constant of four-dimensional gravity, "
  r'$8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$.', 'GeV^-2', r'$6.709\times10^{-39}$ GeV$^{-2}$ '
  r'($M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2} = 1.22091\times10^{19}$ GeV)', 'STANDARD')
R('Vperp', r'V_\perp', [r'V_\perp'], r'The proper volume of the block per unit four-volume (both halves of a period of $x_0$ and '
  r'the extra times), $V_\perp = 2f^4v_{\mathrm{t}}(1 - \mathrm{e}^{-3HL})/(3H)$.', 'GeV^-4', status='DERIVED')
R('vt', r'v_{\mathrm{t}}', [r'v_{\mathrm{t}}'], r'The coordinate volume of the compact extra times $x_5, x_6, x_7$.', 'GeV^-3',
  r'not fixed; $v_{\mathrm{t}} = H^{-3}$ in the quoted conversions', 'ASSUMED')
R('rho4', r'\rho_4', [r'\rho_4'], r'A four-dimensional energy density (per 3-volume); its block average is '
  r'$\kappa\Delta\rho = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*)\rho_4$.', 'GeV^4', status='DERIVED')
