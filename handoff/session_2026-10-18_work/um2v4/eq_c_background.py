from build_lib import E
from bg_latex import BG

NL = '\n'
BR = r' \\' + NL + ' &'      # a LaTeX line break followed by an alignment point


def regroup(lines, limit=200):
    """Join the generated lines of terms into fewer, longer lines (at most `limit` characters of LaTeX source)."""
    out = []
    for ln in lines:
        if out and len(out[-1]) + 1 + len(ln) <= limit:
            out[-1] += ' ' + ln
        else:
            out.append(ln)
    return out


def block(name):
    return BR.join(regroup(BG[name]))


def comp(p):
    rows = []
    for c, lab in (('x4', 'x_4'), ('x1', 'x_1'), ('x0', 'x_0')):
        lines = BG['E%s_%s' % (p, c)]
        rows.append(r'\mathcal{E}_{(%s)}{}^{%s}{}_{%s} ={}& ' % (p, lab, lab) + BR.join(regroup(lines)))
    return r'\begin{aligned}' + NL + (r' \\' + NL).join(rows) + NL + r'\end{aligned}'


E('FE', 'The order-0 metric in the author\'s coordinates', r'''
\begin{aligned}
\bar g = \mathrm{diag}\Big(&\mathrm{e}^{-2a_4}b_4\cot^2z,\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ -1,\\
&-\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6}\Big),
 \qquad z = 6Hx_0
\end{aligned}''', 'AUTHOR', ['metric g'],
  'The corrected primordial metric of the record (author\'s coordinates, x0 first); its curvature is computed exactly '
  '(sympy, identical in both charts) and does not depend on x0.', name='bg_metric')

E('FE', r'The hidden coordinate $y$, the block scale and the rates of the background', r'''
\begin{aligned}
&y = \frac{\ln\lvert\sin z\rvert}{6H},\qquad \mathrm{d}y = \cot z\,\mathrm{d}x_0,\qquad \xi = \frac{y}{L}\in[-1, 0],\\
&\bar g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 + f^2\Big[\mathrm{d}y^2 - \mathrm{e}^{2Hy}\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big],\\
&f = \mathrm{e}^{-a_4}b_4^{1/2},\qquad K = \frac{1}{f^2},\qquad \mathcal{H} = \dot a_4,\qquad
 \mathcal{H}_f = \frac{\dot f}{f} = \frac{\dot b_4}{2b_4} - \dot a_4,\qquad \dot K = -2K\mathcal{H}_f,\\
&\sqrt{\lvert\bar g\rvert} = \mathrm{e}^{3a_4}f^4\lvert\cot z\rvert(\sin^2z)^{1/4}
 = \mathrm{e}^{3a_4}f^4\,\mathrm{e}^{3Hy}\Big\lvert\frac{\mathrm{d}y}{\mathrm{d}x_0}\Big\rvert
\end{aligned}''', 'DERIVED', ['metric g'],
  'Exact change of chart; one period of x0 (length pi/(6H)) is two halves joined at the fold y = 0, each closed by the regular '
  'tip at y = -L (HL = 3, ASSUMED).', name='bg_ychart')

E('FE', 'The sectional curvatures of the order-0 metric', r'''
\begin{aligned}
&R^{x_1x_2}{}_{x_1x_2} = \mathcal{H}^2,\qquad R^{x_1x_4}{}_{x_1x_4} = \mathcal{H}^2 + \dot{\mathcal{H}},\qquad
 R^{x_1x_0}{}_{x_1x_0} = \mathcal{H}\mathcal{H}_f,\qquad R^{x_4x_0}{}_{x_4x_0} = \mathcal{H}_f^2 + \dot{\mathcal{H}}_f,\\
&R^{x_0x_5}{}_{x_0x_5} = \mathcal{H}_f^2 - H^2K;\\
&\text{the same for every pair of the same kind; all other $R^{ab}{}_{cd}$ with $\{a, b\} \ne \{c, d\}$ vanish}
\end{aligned}''', 'DERIVED', ['metric g'],
  'Exact (sympy, both charts, 25 checks); x1, x2, x3 are equivalent, and x0, x5, x6, x7 are equivalent.', name='sectional')

E('FE', 'The Lovelock densities and tensors of a pair-diagonal curvature', r'''
\begin{aligned}
&\mathcal{L}_{(1)} = 2\sum_{\text{pairs}}R^{ab}{}_{ab},\qquad
 \mathcal{L}_{(2)} = 8\sum_{\text{2 disjoint pairs}}\ \prod_{\text{pairs}}R^{ab}{}_{ab},\qquad
 \mathcal{L}_{(3)} = 48\sum_{\text{3 disjoint pairs}}\ \prod_{\text{pairs}}R^{ab}{}_{ab},\\
&\mathcal{E}_{(1)}{}^c{}_c = -\sum_{\text{pairs avoiding $c$}}R^{ab}{}_{ab},\qquad
 \mathcal{E}_{(2)}{}^c{}_c = -4\sum_{\text{2 disjoint pairs avoiding $c$}}\ \prod_{\text{pairs}}R^{ab}{}_{ab},\\
&\mathcal{E}_{(3)}{}^c{}_c = -24\sum_{\text{3 disjoint pairs avoiding $c$}}\ \prod_{\text{pairs}}R^{ab}{}_{ab}
\end{aligned}''', 'DERIVED', ['metric g'],
  'Exact (the coefficients are 2^p p! and -2^(p-1) p! for the order p); checked against the Ricci route (p = 1), the explicit '
  'Gauss-Bonnet tensor (p = 2), the Bianchi identities and the minisuperspace variation with a lapse (p = 1, 2, 3).',
  name='lov_pair')

E('FE', 'The first Lovelock tensor (the Einstein tensor) of the order-0 metric', comp('1'), 'DERIVED', ['metric g'],
  'Exact; every off-diagonal component vanishes and the x0 component equals the x5, x6, x7 components.', name='lov_E1')
E('FE', 'The second Lovelock tensor (Gauss-Bonnet) of the order-0 metric', comp('2'), 'DERIVED', ['metric g'],
  'Exact (sympy, four routes).', name='lov_E2')
E('FE', 'The third Lovelock tensor of the order-0 metric', comp('3'), 'DERIVED', ['metric g'],
  'Exact (sympy, four routes).', name='lov_E3')

E('FE', r'The background equation: the $x_4$ component (the constraint)', r'\begin{aligned}' + NL + r'x_4:\quad &' + block('F_x4_rest')
  + BR + r'= -\kappa\rho' + NL + r'\end{aligned}', 'DERIVED', ['metric g (a4, b4)', 'all sources (block averages)'],
  'Exact; preserved to 6e-10 in the numerical integration of the primordial era; at the static block it gives [[static]].',
  name='bg_x4')
E('FE', 'The background equation: the 3-space component', r'\begin{aligned}' + NL + r'x_1:\quad &\Big[' + block('F_x1_Adot')
  + r'\Big]\,\dot{\mathcal{H}}' + BR + r'+ \Big[' + block('F_x1_hdot') + r'\Big]\,\dot{\mathcal{H}}_f' + BR
  + block('F_x1_rest') + BR + r'= \kappa p_3' + NL + r'\end{aligned}', 'DERIVED', ['metric g', 'all sources'],
  'Exact; solved together with the x0 component for the two rates and integrated numerically (LSODA) from the primordial '
  'block to the static block.', name='bg_x1')
E('FE', 'The background equation: the hidden (block) component', r'\begin{aligned}' + NL + r'x_0:\quad &\Big[' + block('F_x0_Adot')
  + r'\Big]\,\dot{\mathcal{H}}' + BR + r'+ \Big[' + block('F_x0_hdot') + r'\Big]\,\dot{\mathcal{H}}_f' + BR
  + block('F_x0_rest') + BR + r'= \kappa p_0;\qquad x_5, x_6, x_7:\ \text{the same left side} = \kappa p_5;'
  + r' \\' + NL + r' &\text{block-isotropic order-0 metric: the same left side} = \kappa\bar p,\qquad'
  + r' \bar p = \tfrac14\big(p_0 + 3p_5\big)' + NL + r'\end{aligned}', 'DERIVED', ['metric g', 'all sources'],
  'Exact; the x0 and extra-time components have the same left side, so the order-0 metric solves both only if p0 = p5; for p0 '
  '!= p5 the common block scale f obeys the average (the variation of the action with respect to f), and p0 - p5 drives a '
  'block-shape mode outside the order-0 metric (OPEN).', name='bg_x0')

E('FE', 'The conservation of the order-0 source', r'''
\dot\rho = -3\mathcal{H}(\rho + p_3) - \mathcal{H}_f(\rho + p_0) - 3\mathcal{H}_f(\rho + p_5)
 = -3\mathcal{H}(\rho + p_3) - 4\mathcal{H}_f(\rho + \bar p)''', 'DERIVED', ['all sources'],
  'Exact consequence of [[conservation]]; for the stabiliser it gives rho_stab proportional to f^-8.', name='bg_cons')

E('FE', 'The static block', r'''
\begin{aligned}
&x_4:\ -3\mathcal{G}(K)\,\mathcal{H}^2 + 6H^2K\big(1 - 2w_{(2)}K\big) + \Lambda + \kappa\rho = 0,\qquad
 x_1:\ \text{the same with } -\kappa p_3 \text{ in place of } \kappa\rho,\\
&x_0:\ 6\big(12w_{(2)}K - 1\big)\mathcal{H}^2 - \frac{12\big(w_{(2)} - 18w_{(3)}K\big)}{H^2}\,\mathcal{H}^4 + 3H^2K + \Lambda
 - \kappa p_0 = 0,\\
&x_5, x_6, x_7:\ \text{the same with } \kappa p_5 \text{ in place of } \kappa p_0;\qquad
 \text{block-isotropic order-0 metric: the same with } \kappa\bar p,\\
&\mathcal{G}(K) = 1 - 24w_{(2)}K + 72w_{(3)}K^2 = \frac{K^2 - 12K + 16}{16}
\end{aligned}''', 'DERIVED', ['metric g', 'sources'],
  'Exact for H_f = 0 and dH/dx4 = 0; without sources and with H = 0 the only static block is K = 1/(4 w_(2)) = 8, which needs '
  'Lambda = -24 H^2 and has G = -1 (repulsive gravity).', name='static')

E('FE', 'The stabilised block', r'''
\begin{aligned}
&\kappa\rho_{\mathrm{stab}} = 10H^2 - 6H^2K + \tfrac38H^2K^2\ \ (x_4),\qquad
 \kappa p_0 = \kappa p_5 = \kappa\rho_{\mathrm{stab}} = 3H^2K - 10H^2\ \ (x_0;\ x_5, x_6, x_7),\\
&\Rightarrow\ K_{\pm} = 12 \pm \tfrac43\sqrt{51},\qquad
K_* = 12 + \tfrac43\sqrt{51} = 21.5219,\qquad f_* = K_*^{-1/2} = 0.215556,\\
&\mathcal{G}(K_*) = \tfrac{20}{3} + \sqrt{51} = 13.8081,\qquad \kappa\rho_{\mathrm{stab}}(f_*) = \big(26 + 4\sqrt{51}\big)H^2
\end{aligned}''', 'DERIVED', ['metric g (block scale)', 'stabiliser'],
  'Exact (closed form); the upper root is the vacuum of UM-2 with attractive four-dimensional gravity; the lower root '
  'K_- = 2.4781 has G = -0.4748.', name='stabiliser')

E('FE', 'The linearised block and the radion', r'''
\begin{aligned}
&\Delta\dot{\mathcal{H}} = \Xi_{\mathcal{H}K}\,\Delta K,\qquad \Delta\dot{\mathcal{H}}_f = \Xi_{fK}\,\Delta K,\qquad
 \Delta\dot K = -2K_*\,\Delta\mathcal{H}_f,\\
&\omega_{\mathrm{r}}^2 = 2K_*\,\Xi_{fK} = \Big(\frac{31552}{2249} - \frac{2416\sqrt{51}}{6747}\Big)H^2 = (3.38705\,H)^2
\end{aligned}''',
  'DERIVED', ['metric g (block scale)'],
  'Exact; eigenvalues 0 and +-i omega_r: the block is stable and oscillates (the radion, mass 48.42 TeV); stable for every '
  'stabiliser law of the family tried.', name='radion')

E('FE', 'The response of the block to matter to first order', r'''
\begin{aligned}
\Delta\dot{\mathcal{H}} &= \Xi_{\mathcal{H}K}\,\Delta K + \Xi_{\mathcal{H}3}\,\kappa\Delta p_3
 + \Xi_{\mathcal{H}p}\,\kappa\Delta\bar p + \Xi_{\mathcal{H}\rho}\,\kappa\Delta\rho,\qquad
 3\mathcal{G}(K_*)\,\mathcal{H}^2 = \kappa\Delta\rho,\\
\Delta\dot{\mathcal{H}}_f &= \Xi_{fK}\,\Delta K + \Xi_{f3}\,\kappa\Delta p_3 + \Xi_{fp}\,\kappa\Delta\bar p
 + \Xi_{f\rho}\,\kappa\Delta\rho,\\
\Delta\ddot K + \omega_{\mathrm{r}}^2\,\Delta K &= -2K_*\big(\Xi_{f3}\,\kappa\Delta p_3 + \Xi_{fp}\,\kappa\Delta\bar p
 + \Xi_{f\rho}\,\kappa\Delta\rho\big)
\end{aligned}''', 'DERIVED', ['metric g (block)', 'all sources'],
  'Exact to first order (H^2 counted as first order); the coefficients are [[response_coeffs]].', name='response')

E('FE', 'The coefficients of the first-order block response', r'''
\begin{aligned}
&\Xi_{\mathcal{H}K} = \frac{6\big(238 - 19\sqrt{51}\big)}{2249}H^2,\qquad \Xi_{fK} = \frac{4063 - 485\sqrt{51}}{2249}H^2,\qquad
 \Xi_{\mathcal{H}3} = \frac{2283}{4498} - \frac{162\sqrt{51}}{2249},\\
&\Xi_{\mathcal{H}p} = \frac{28\sqrt{51} - 114}{2249},\qquad
 \Xi_{\mathcal{H}\rho} = \frac{135021}{265382} - \frac{10308\sqrt{51}}{132691},\qquad
 \Xi_{f3} = \frac{21\sqrt{51}}{2249} - \frac{171}{4498},\\
&\Xi_{fp} = \frac{239\sqrt{51}}{6747} - \frac{485}{2249},\qquad \Xi_{f\rho} = \frac{57}{4498} - \frac{7\sqrt{51}}{2249}
\end{aligned}''', 'DERIVED', ['metric g (block)'],
  'Exact (sympy); numerically 0.272956 H^2, 0.266522 H^2, -0.006853, 0.038221, -0.045997, 0.028666, 0.037320, -0.009555.',
  name='response_coeffs')

E('FE', 'The adiabatic block response and the four-dimensional Friedmann acceleration equation', r'''
\Delta K = \frac{c_\rho\,\kappa\Delta\rho + c_3\,\kappa\Delta p_3 + c_p\,\kappa\Delta\bar p}{H^2},\qquad
\Delta\ln f = -\frac{\Delta K}{2K_*},\qquad c_3 = -3c_\rho,\qquad
\Delta\dot{\mathcal{H}} = -\frac{\kappa(\Delta\rho + \Delta p_3)}{2\mathcal{G}(K_*)}''', 'DERIVED',
  ['metric g (block)', 'all sources'],
  'Exact for a slowly varying source (second time derivative of Delta K neglected); radiation drops out exactly; used in every '
  'environment of the coupled solution [[coupled_block]].', name='adiabatic')

E('FE', 'The four-dimensional reduction of the Lovelock action on the static block', r'''
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
\end{aligned}''', 'DERIVED', ['metric g'],
  'Exact (the four-dimensional quadratic density is topological, the cubic one vanishes); Lambda_4 = 0 at the static point; '
  'the observed dark energy is a tuned residual, Lambda_4/H^2 ~ 1e-92 (OPEN).', name='reduction')

E('FE', 'The four-dimensional effective gravity and the four-dimensional couplings', r'''
\begin{aligned}
&G^{(4)}_{\mu\nu} + \Lambda_4\,g^{(4)}_{\mu\nu} = 8\pi G_{\mathrm{N}}\,\mathcal{T}^{(4)}_{\mu\nu},\qquad
 8\pi G_{\mathrm{N}} = \frac{\kappa}{\mathcal{G}(K_*)\,V_\perp},\qquad V_\perp = \frac{2f^4v_{\mathrm{t}}\big(1 - \mathrm{e}^{-3HL}\big)}{3H},\\
&\mathcal{T}^{(4)}_{\mu\nu} = \int\mathrm{d}x_0\,\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7\,\sqrt{\lvert g_\perp\rvert}\;\mathcal{T}_{\mu\nu},
 \qquad g_3^2 = \frac{\hat g_3^2}{V_\perp},\qquad g_2^2 = \frac{\hat g_2^2}{V_\perp},\qquad g_1^2 = \frac{\hat g_1^2}{V_\perp}
\end{aligned}''', 'DERIVED', ['four-dimensional metric', 'all fields'],
  'Exact: four-dimensional gravity on the stabilised block is general relativity; its linear perturbations are '
  '[[pert_einstein]].', name='einstein4')
