from build_lib import R

# ------------------------------------------------------------------ notation, numbers, operators
R('euler', r'\mathrm{e}', [r'\mathrm{e}'], r"Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential "
  "of $X$.", 'dimensionless', '2.718281828', 'STANDARD')
R('imag', r'\mathrm{i}', [r'\mathrm{i}'], r'The imaginary unit, $\mathrm{i}^2 = -1$.', 'dimensionless', status='STANDARD')
R('diff', r'\mathrm{d}', [r'\mathrm{d}'], r'The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, '
  r'$\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables.',
  '', status='STANDARD')
R('pi', r'\pi', [r'\pi'], 'The number pi, the ratio of the circumference of a circle to its diameter.', 'dimensionless',
  '3.141592654', 'STANDARD')
R('infty', r'\infty', [r'\infty'], 'Infinity: as a limit of an integral or a sum it means that the range has no upper bound.',
  '', status='STANDARD')
R('zeta3', r'\zeta', [r'\zeta'], r'The Riemann zeta function; only its value $\zeta(3)$ occurs, the sum of $1/n^3$ over the '
  'positive integers $n$.', 'dimensionless', r'$\zeta(3) = 1.2020569$', 'STANDARD')
R('trace', r'\mathrm{tr}', [r'\mathrm{tr}'], 'The trace of a matrix: the sum of its diagonal entries.', '', status='STANDARD')
R('diag', r'\mathrm{diag}', [r'\mathrm{diag}'], 'A diagonal matrix with the listed entries on its diagonal (in the order of '
  r'the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions).', '', status='STANDARD')
R('imagpart', r'\mathrm{Im}', [r'\mathrm{Im}'], 'The imaginary part of a complex number.', '', status='STANDARD')
R('identity', r'\mathbf{1}', [r'\mathbf{1}'], 'The identity matrix (of the size fixed by the context: 16 x 16 on spinors, '
  '3 x 3 on the generations or flavours, 2 x 2 for the sigma field).', 'dimensionless', status='STANDARD')
R('partial', r'\partial', [r'\partial'], r'A partial derivative: $\partial_M$ is the derivative with respect to the coordinate '
  r'$X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the '
  'derivative of $X$ with respect to $Y$ at fixed other variables.', '', status='STANDARD')
R('nabla', r'\nabla', [r'\nabla'], 'The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ '
  r'(Christoffel symbols $\Gamma^N{}_{MP}$); $\nabla_M$ acts on the index $M$, $\nabla^M = g^{MN}\nabla_N$.', '',
  status='STANDARD')
R('grad3', r'\vec\nabla', [r'\vec\nabla'], r'The gradient in ordinary 3-space, $(\partial/\partial x_1, \partial/\partial x_2, '
  r'\partial/\partial x_3)$.', '1/length', status='STANDARD')
R('Delta', r'\Delta', [r'\Delta'], r'The change (difference or small perturbation) of the quantity that follows: $\Delta K$, '
  r'$\Delta\rho$, $\Delta p_3$ are first-order changes about the static block, $\Delta\varepsilon_o$ a level shift, '
  r'$\Delta m^2_{21} = m_2^2 - m_1^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$, '
  r'$\Delta S_{\mathrm{m}}$ the change of an action under a change $\Delta g^{MN}$ of the metric.', '', status='STANDARD')
R('delta', r'\delta', [r'\delta'], r'The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 '
  r'otherwise (likewise $\delta_{\alpha e}$, $\delta_{l0}$, $\delta^{I3}$); with upper and lower index strings the generalised '
  r'Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of Kronecker deltas '
  r'$\delta^{M_a}_{N_b}$ (+1 or -1 if the upper indices are an even or odd permutation of the lower ones, 0 '
  r'otherwise).', '',
  status='STANDARD')
R('deltaD', r'\delta_{\mathrm{D}}', [r'\delta_{\mathrm{D}}'], r'The Dirac delta function: '
  r'$\delta_{\mathrm{D}}(y + L)$ is zero except at $y = -L$ and has the unit integral over $y$.', '1/length',
  status='STANDARD')
R('prime', r"{}'", ['prime'], r"The prime on a function of the conformal time $\tau_{\mathrm{c}}$ is its derivative "
  r"$\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$ (it is used only in the cosmological perturbation equations; two primes are the "
  "second derivative).", '', status='STANDARD')
R('dagger', r'{}^\dagger', ['dagger'], 'Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor '
  '(for field operators the adjoint operator).', '', status='STANDARD')
R('transpose', r'{}^T', ['transpose'], 'The transpose: a row written with $^T$ is a column.', '', status='STANDARD')
R('star', r'{}^*', ['star'], 'Complex conjugation of a number or of each entry of a matrix.', '', status='STANDARD')

# ------------------------------------------------------------------ coordinates
R('Xcoord', r'X = \{x_0, \dots, x_7\}', ['X'], "The author's coordinates of the eight-dimensional spacetime, "
  r"$X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, "
  r"$\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ "
  r"(four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$.", 'length (each coordinate)', status='AUTHOR')
R('Xtip', r'X_{\mathrm{tip}}', [r'X_{\mathrm{tip}}'], r'The seven coordinates $x_1, \dots, x_7$ of the tip $y = -L$ of the hidden '
  r'direction; $\mathrm{d}^7X_{\mathrm{tip}}$ is their coordinate volume element.', 'length (each coordinate)', status='DERIVED')
R('x0', r'x_0', [r'x_0'], 'The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, '
  r'periodically with the period $\pi/(6H)$.', 'length', status='AUTHOR')
R('x1', r'x_1', [r'x_1'], 'The first coordinate of ordinary 3-space.', 'length', status='AUTHOR')
R('x2', r'x_2', [r'x_2'], 'The second coordinate of ordinary 3-space.', 'length', status='AUTHOR')
R('x3', r'x_3', [r'x_3'], 'The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis).',
  'length', status='AUTHOR')
R('x4', r'x_4', [r'x_4'], r'The time; dots denote $\mathrm{d}/\mathrm{d}x_4$.', 'length (= time, c = 1)', status='AUTHOR')
R('x5', r'x_5', [r'x_5'], 'The first of the three extra time-like coordinates.', 'length', status='AUTHOR')
R('x6', r'x_6', [r'x_6'], 'The second of the three extra time-like coordinates.', 'length', status='AUTHOR')
R('x7', r'x_7', [r'x_7'], 'The third of the three extra time-like coordinates.', 'length', status='AUTHOR')
R('vecx', r'\vec x', [r'\vec x'], r'The position in ordinary 3-space, $\vec x = (x_1, x_2, x_3)$; '
  r'$\mathrm{d}\vec x^{\,2} = \mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2$.', 'length', status='STANDARD')
R('zvar', r'z', ['z'], r'The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$.',
  'dimensionless', status='AUTHOR')
R('ycoord', r'y', ['y'], r'The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold '
  r'($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$.',
  'length', status='DERIVED')
R('xi', r'\xi', [r'\xi'], r'The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a '
  'period.', 'dimensionless', status='DERIVED')
R('Lcut', r'L', ['L'], 'The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$.', 'length',
  r'$L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block)', 'ASSUMED')
R('Hconst', r'H', ['H'], r"The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock "
  r"couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$.", 'GeV (1/length)',
  r'14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$)', 'AUTHOR')

# ------------------------------------------------------------------ index sets
R('iM', 'M', ['index:M'], r'A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over '
  r'$x_0, x_1, \dots, x_7$; a repeated index is summed.', '', status='STANDARD')
R('iN', 'N', ['index:N'], r'A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a '
  'repeated index is summed.', '', status='STANDARD')
R('iP', 'P', ['index:P'], r'A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a '
  'repeated index is summed.', '', status='STANDARD')
R('iQ', 'Q', ['index:Q'], r'A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a '
  'repeated index is summed.', '', status='STANDARD')
R('ia', 'a', ['index:a'], r'A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and '
  r'lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$).', '',
  status='STANDARD')
R('ib', 'b', ['index:b'], r'A frame index running over $0, \dots, 7$ (as $a$).', '', status='STANDARD')
R('ic', 'c', ['index:c'], r'A frame index running over $0, \dots, 7$ (as $a$).', '', status='STANDARD')
R('id', 'd', ['index:d'], r'A frame index running over $0, \dots, 7$ (as $a$).', '', status='STANDARD')
R('imu', r'\mu', [r'index:\mu'], 'A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, '
  'x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed.', '',
  status='STANDARD')
R('inu', r'\nu', [r'index:\nu'], r'A four-dimensional coordinate index running over $x_1, \dots, x_4$ (as $\mu$).', '',
  status='STANDARD')
R('iA', 'A', ['index:A'], r'A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed.', '',
  status='STANDARD')
R('iB', 'B', ['index:B'], r'A colour (adjoint SU(3)) index running over $1, \dots, 8$ (as $A$).', '', status='STANDARD')
R('iI', 'I', ['index:I'], 'A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed.', '',
  status='STANDARD')
R('ii', 'i', ['index:i'], r'The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, '
  r'\nu_3$; a repeated index is not summed unless a sum sign is written.', '', status='STANDARD')
R('ij', 'j', ['index:j'], 'A second generation index ($j = 1, 2, 3$).', '', status='STANDARD')
R('ialpha', r'\alpha', [r'index:\alpha'], r'A flavour index running over $e, \mu, \tau$ (the flavour states of the leptons and '
  'neutrinos).', '', status='STANDARD')
R('ibeta', r'\beta', [r'index:\beta'], r'A second flavour index running over $e, \mu, \tau$.', '', status='STANDARD')
R('ie', 'e', ['index:e'], r'The electron flavour as a value of a flavour index ($\delta_{\alpha e}$, $U_{e2}$, $V_e$, '
  r'$\mathcal{P}_{ee}$).', '', status='STANDARD')
R('ipsi', r'\psi', [r'index:\psi'], r'The label of a Standard-Model multiplet: $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ '
  '(quark doublet, up and down quark singlets, lepton doublet, charged-lepton singlet, right-handed neutrino); a sum over '
  r'$\psi$ runs over the six.', '', status='STANDARD')
R('if', 'f', ['index:f'], r'The label of a fermion species: a Standard-Model multiplet of one generation (its '
  r'$N_{\mathrm{c}}$ Weyl components share one zero-mode profile; the zero mode of each chirality) or a fermion of a medium '
  r'(electron, proton, neutron); a sum over $f$ runs over these species.', '', status='STANDARD')
R('io', 'o', ['index:o'], 'The label of a Kohn-Sham orbital (a state of dirac16complex in the cell: block, momentum shell, '
  'fold parity and level); a sum over $o$ runs over the orbitals.', '', status='RECORD')
R('in', 'n', ['index:n'], r'The level number of the Kaluza-Klein tower ($n = 1, 2, 3, \dots$; $n = 0$ the flat zero mode).',
  '', status='DERIVED')
R('ip', 'p', ['index:p'], 'The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic).', '', status='STANDARD')
R('ir', 'r', ['index:r'], 'The Lovelock order of the four-dimensional factor in the reduction on the static block.', '',
  status='DERIVED')
R('il', 'l', ['index:l', 'l'], r'The multipole (angular moment) number $l = 0, 1, 2, \dots$ of a Boltzmann hierarchy or of an '
  r'angular moment $\int u^l\cdots$; as a coefficient it is the same number.', '', status='STANDARD')
R('is', 's', ['index:s'], r'The label of a particle species of the plasma or of matter (photon, gluons, $W^\pm$, $Z$, quarks, '
  'leptons, nucleons, dark matter); a sum over $s$ runs over the species present.', '', status='STANDARD')
R('iL', 'L', ['index:L'], 'The chirality label L: the left-handed (doublet) zero mode, or the left-handed projection '
  r'$P_L = (1 + \Gamma_4)/2$.', '', status='STANDARD')
R('iR', 'R', ['index:R'], 'The chirality label R: the right-handed (singlet) zero mode or field, or the projection '
  r'$P_R = (1 - \Gamma_4)/2$.', '', status='STANDARD')
R('iV', 'V', ['index:V'], r'The label V of the vector coupling of a fermion to the $Z$, '
  r'$\tilde g^f_V = \tilde g^f_L + \tilde g^f_R$.', '', status='STANDARD')
R('iy', 'y', ['index:y'], r'The label $y$ in $\partial_y$: the derivative with respect to the hidden coordinate $y$.', '',
  status='STANDARD')
