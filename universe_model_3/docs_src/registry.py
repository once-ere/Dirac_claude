#!/usr/bin/env python3
r"""The symbol registry of the UM-3 documents (source).  Running this file writes docs_src/symbols/core.json, which the
symbol tool (tools/symbols_tool.py) reads.  Each entry: key -> (tex, atoms, meaning, units, value, status); see the
docstring of the symbol tool for the meaning of the fields.  One symbol, one meaning: an atom belongs to one entry.

Usage: python universe_model_3/docs_src/registry.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
E = {}


def add(key, tex, atoms, meaning, units='', value='', status='STANDARD'):
    if key in E:
        raise SystemExit('duplicate key ' + key)
    E[key] = {'tex': tex, 'atoms': atoms, 'meaning': meaning, 'units': units, 'value': value, 'status': status}


# ---------------------------------------------------------------- mathematics and typography
add('euler', r'\mathrm{e}', [r'\mathrm{e}'], r"Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$.", 'dimensionless', '2.718281828')
add('imag', r'\mathrm{i}', [r'\mathrm{i}'], r'The imaginary unit, $\mathrm{i}^2 = -1$.', 'dimensionless')
add('diff', r'\mathrm{d}', [r'\mathrm{d}'], r'The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables.')
add('pi', r'\pi', [r'\pi'], r'The number pi, the ratio of the circumference of a circle to its diameter.', 'dimensionless', '3.141592654')
add('infty', r'\infty', [r'\infty'], r'Infinity: as a limit of an integral or a sum it means that the range has no bound.')
add('diag', r'\mathrm{diag}', [r'\mathrm{diag}'], r'A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor).')
add('identity', r'\mathbf{1}', [r'\mathbf{1}'], r'The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space).', 'dimensionless')
add('partial', r'\partial', [r'\partial'], r'A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables.')
add('nabla', r'\nabla', [r'\nabla'], r'The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$).')
add('nablahat', r'\hat\nabla', [r'\hat{\nabla}'], r'The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold ($\hat h_{\mu\nu}$ for four-dimensional tensors, the induced metric of the seven-dimensional fold for $\hat\nabla_a\mathcal{S}^a{}_b$).')
add('delta', r'\delta', [r'\delta'], r'The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}} = 1$ for $X = \mathrm{L}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise).')
add('deltaD', r'\delta_{\mathrm{D}}', [r'\delta_{\mathrm{D}}'], r'The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$.', r'1/length (for $\delta_{\mathrm{D}}(\sigma)$)')
add('dagger', r'{}^\dagger', ['dagger'], r'Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator).')
add('transpose', r'{}^T', ['transpose'], r'The transpose of a matrix.')
add('star', r'{}^*', ['star'], r'Complex conjugation of a number, or of each entry of a matrix or column.')
add('prime', r"{}'", ['prime'], r"The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$.")
add('hc', r'\mathrm{h.c.}', [r'\mathrm{h.c.}'], r'The Hermitian conjugate of the preceding terms.')
add('sgn', r'\mathrm{sgn}', [r'\mathrm{sgn}'], r'The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$.')
add('trace', r'\mathrm{tr}', [r'\mathrm{tr}'], r'The trace of a matrix: the sum of its diagonal entries.')

# ---------------------------------------------------------------- index letters and labels
for k, letter, text in [
        ('iM', 'M', r'A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed.'),
        ('iN', 'N', r'A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed.'),
        ('iP', 'P', r'A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed.'),
        ('iQ', 'Q', r'A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed.'),
        ('iS', 'S', r'A coordinate index of eight dimensions, running over $x_0, \dots, x_7$; a repeated index is summed.'),
        ('ia', 'a', r'A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with $\eta_{ab}$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed.'),
        ('ib', 'b', r'A frame index (as $a$).'),
        ('ic', 'c', r'A frame index (as $a$).'),
        ('idx', 'd', r'A frame index (as $a$).'),
        ('imu', r'\mu', r'A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed.'),
        ('inu', r'\nu', r'A four-dimensional coordinate index (as $\mu$).'),
        ('irho', r'\rho', r'A four-dimensional coordinate index (as $\mu$).'),
        ('iA', 'A', r'A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed.'),
        ('iB', 'B', r'A colour (adjoint SU(3)) index (as $A$).'),
        ('iC', 'C', r'A colour (adjoint SU(3)) index (as $A$).'),
        ('iI', 'I', r'A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed.'),
        ('iJ', 'J', r'A weak-isospin (adjoint SU(2)) index (as $I$).'),
        ('iK', 'K', r'A weak-isospin (adjoint SU(2)) index (as $I$).'),
        ('ii', 'i', r'A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written.'),
        ('ij', 'j', r'A second generation or mass-state index (as $i$).'),
        ('ialpha', r'\alpha', r'A lepton-flavour index, $\alpha \in \{e, \mu, \tau\}$.'),
        ('ibeta', r'\beta', r'A second lepton-flavour index (as $\alpha$).'),
        ('iX', 'X', r'The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both.'),
        ('if', 'f', r'The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six.'),
        ('ipsi', r'\psi', r'The label of a Standard-Model fermion field in a sum: $\psi$ runs over $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$.'),
        ('ir', 'r', r'An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal).'),
        ('io', 'o', r'The label of a Kohn-Sham orbital (a single-particle state of dirac16complex); a sum over $o$ runs over the orbitals.'),
]:
    add(k, letter, ['index:' + letter], text)

# ---------------------------------------------------------------- coordinates and geometry
add('Xcoord', r'X = \{x_0, \dots, x_7\}', ['X'], r"The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element.", 'length (each coordinate)', '', 'AUTHOR')
add('xfour', r'x', ['x'], r'The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$.', 'length (each coordinate)', '', 'AUTHOR')
add('x0', r'x_0', ['x_{0}'], r'The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$.', 'length', '', 'AUTHOR')
add('x1', r'x_1', ['x_{1}'], r'The first coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x2', r'x_2', ['x_{2}'], r'The second coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x3', r'x_3', ['x_{3}'], r'The third coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x4', r'x_4', ['x_{4}'], r'The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$.', 'length (= time, $c = 1$)', '', 'AUTHOR')
add('x5', r'x_5', ['x_{5}'], r'The first of the three extra time-like coordinates.', 'length', '', 'AUTHOR')
add('x6', r'x_6', ['x_{6}'], r'The second of the three extra time-like coordinates.', 'length', '', 'AUTHOR')
add('x7', r'x_7', ['x_{7}'], r'The third of the three extra time-like coordinates.', 'length', '', 'AUTHOR')
add('sigma', r'\sigma', [r'\sigma'], r'The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$.', 'length', '', 'DERIVED')
add('zvar', r'z', ['z'], r'The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$.', 'dimensionless', '', 'AUTHOR')
add('metric', r'g_{MN}', ['g'], r'The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element).', 'dimensionless', '', 'AUTHOR')
add('eta', r'\eta_{ab}', [r'\eta'], r'The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix).', 'dimensionless', '', 'AUTHOR')
add('vielbein', r'\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M', [r'\mathbf{e}'], r'The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$.', 'dimensionless', '', 'STANDARD')
add('Christoffel', r'\Gamma^P{}_{MN}', [r'\Gamma'], r'The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection).', '1/length', '', 'STANDARD')
add('Riemann', r'R^{MN}{}_{PQ},\ R_{MN},\ R', ['R'], r'The curvature of the metric $g_{MN}$: with four indices the Riemann tensor (convention $[\nabla_P, \nabla_Q]V^M = R^M{}_{NPQ}V^N$), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$.', '1/length$^2$', '', 'STANDARD')
add('Hconst', r'H', ['H'], r"The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter.", 'GeV (1/length)', '', 'AUTHOR')
add('a4', r'a_4', ['a_{4}'], r"The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate.", 'dimensionless', '', 'AUTHOR')
add('b4', r'b_4', ['b_{4}'], r"The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp.", 'dimensionless', '', 'AUTHOR')

# ---------------------------------------------------------------- gravity
add('Stot', r'S_{\mathrm{tot}}', [r'S_{\mathrm{tot}}'], r'The action of UM-3 (the integral of the Lagrangian density over spacetime); its variation with respect to every field gives the field equations.', 'dimensionless ($\\hbar = 1$)', '', 'ASSUMED')
add('SEL', r'S_{\mathrm{EL}}', [r'S_{\mathrm{EL}}'], r'The Einstein-Lovelock action of gravity in eight dimensions.', 'dimensionless', '', 'AUTHOR')
add('Sstab', r'S_{\mathrm{stab}}', [r'S_{\mathrm{stab}}'], r'The action of the stabiliser of the bulk (a medium specified by its energy-momentum tensor $\mathcal{T}_{\mathrm{stab}}$).', 'dimensionless', '', 'ASSUMED')
add('SPsi', r'S_\Psi', [r'S_{\Psi}'], r'The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction).', 'dimensionless', '', 'RECORD')
add('Sfold', r'S_{\mathrm{fold}}', [r'S_{\mathrm{fold}}'], r'The action of the fold: the Standard Model, the portals of dirac16complex, the fold fluid and the induced gravity of the fold, all at $\sigma = 0$.', 'dimensionless', '', 'ASSUMED')
add('kappa', r'\kappa', [r'\kappa'], r'The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$.', 'GeV$^{-6}$', '', 'AUTHOR')
add('G8', r'G_8', [r'G_{8}'], r'The eight-dimensional Newton constant ($\kappa = 8\pi G_8$).', 'GeV$^{-6}$', '', 'AUTHOR')
add('alphaL', r'\alpha_{(p)}', [r'\alpha'], r'The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$).', 'GeV$^{2-2p}$', '', 'AUTHOR')
add('wL', r'w_{(p)}', ['w'], r"The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]).", 'dimensionless', '$(1, 1/32, 1/1152)$', 'AUTHOR')
add('LovL', r'\mathcal{L}_{(p)}', [r'\mathcal{L}'], r'The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density.', '1/length$^{2p}$', '', 'STANDARD')
add('Lambda', r'\Lambda', [r'\Lambda'], r'The eight-dimensional cosmological constant, $\Lambda = -10H^2$ (the author writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$).', 'GeV$^2$', '$-10H^2$', 'AUTHOR')
add('LambdaN', r'\Lambda_{\mathrm{N}}', [r'\Lambda_{\mathrm{N}}'], r"The author's pure number in the vacuum equations of his notebook, $\Lambda_{\mathrm{N}} = 10$; $\Lambda = -\Lambda_{\mathrm{N}}H^2$.", 'dimensionless', '10', 'AUTHOR')

# ---------------------------------------------------------------- dirac16complex
add('Psi', r'\Psi,\ \bar\Psi', [r'\Psi', r'\bar{\Psi}'], r"dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$.", 'GeV$^{7/2}$', '', 'AUTHOR')
add('PsiL', r'\Psi_{\mathrm{L}}', [r'\Psi_{\mathrm{L}}'], r'The left-handed half of dirac16complex, $\Psi_{\mathrm{L}} = P_{\mathrm{L}}\Psi$ (the upper eight components in the basis of 4+4.nb).', 'GeV$^{7/2}$', '', 'AUTHOR')
add('PsiR', r'\Psi_{\mathrm{R}}', [r'\Psi_{\mathrm{R}}'], r'The right-handed half of dirac16complex, $\Psi_{\mathrm{R}} = P_{\mathrm{R}}\Psi$ (the lower eight components).', 'GeV$^{7/2}$', '', 'AUTHOR')
add('Tmat', r'T_a,\ T^a', ['T', 'T_{0}', 'T_{1}', 'T_{2}', 'T_{3}', 'T_{4}', 'T_{5}', 'T_{6}', 'T_{7}'], r"The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$.", 'dimensionless', '', 'AUTHOR')
add('gammaM', r'\gamma^M,\ \gamma^{(a)}', [r'\gamma'], r'The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time).', 'dimensionless', '', 'AUTHOR')
add('sigma16', r'\sigma_{16}', [r'\sigma_{16}'], r'The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric.', 'dimensionless', '', 'AUTHOR')
add('Gamma8', r'\Gamma_8', [r'\Gamma_{8}'], r"The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$.", 'dimensionless', '', 'AUTHOR')
add('PL', r'P_{\mathrm{L}}', [r'P_{\mathrm{L}}'], r"The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$.", 'dimensionless', '', 'AUTHOR')
add('PR', r'P_{\mathrm{R}}', [r'P_{\mathrm{R}}'], r"The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$.", 'dimensionless', '', 'AUTHOR')
add('PX', r'P_X', ['P'], r'The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$.', 'dimensionless', '', 'AUTHOR')
add('Dcov', r'D_M,\ D_\mu', ['D'], r'The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ of IN-13; $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$).', '1/length', '', 'STANDARD')
add('mPsi', r'm_\Psi', [r'm_{\Psi}'], r'The mass parameter of dirac16complex in the bulk.', 'GeV', '', 'RECORD')
add('lamPsi', r'\lambda_\Psi', [r'\lambda_{\Psi}'], r'The coupling of the contact self-interaction of dirac16complex.', 'GeV$^{-6}$', '', 'RECORD')
add('Omega', r'\Omega_M', [r'\Omega'], r'The spin connection acting on dirac16complex, $\Omega_M = \frac12\omega_{Mab}\Sigma^{ab}$.', '1/length', '', 'RECORD')
add('omegaSC', r'\omega_{Mab}', [r'\omega'], r'The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$.', '1/length', '', 'STANDARD')
add('SigmaGen', r'\Sigma^{ab},\ \Sigma^{\mu\nu}', [r'\Sigma'], r"The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold.", 'dimensionless', '', 'AUTHOR')

# ---------------------------------------------------------------- stabiliser, fold
add('Tstab', r'\mathcal{T}_{\mathrm{stab}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{stab}}'], r'The energy-momentum tensor of the stabiliser of the bulk (frame components).', 'GeV$^8$', '', 'ASSUMED')
add('rhos', r'\rho_{\mathrm{s}}', [r'\rho_{\mathrm{s}}'], r'The energy density of the stabiliser.', 'GeV$^8$', r'$\kappa\rho_{\mathrm{s}} = -H^2/16$', 'ASSUMED')
add('ps', r'p_{\mathrm{s}}', [r'p_{\mathrm{s}}'], r'The pressure of the stabiliser (equal along $\sigma$, ordinary space and the extra times).', 'GeV$^8$', r'$\kappa p_{\mathrm{s}} = -5H^2/16$', 'ASSUMED')
add('Vstar', r'V_*', [r'V_{*}'], r'The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one.', 'length$^3$ (GeV$^{-3}$)', '', 'ASSUMED')
add('Vt', r'V_{\mathrm{t}}', [r'V_{\mathrm{t}}'], r'The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$.', 'length$^3$', '', 'ASSUMED')
add('Zfold', r'\mathcal{Z}', [r'\mathcal{Z}'], r'The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value.', 'dimensionless', '1 in the late universe', 'DERIVED')
add('Ffold', r'F', ['F'], r'Any function of the fields at the fold (used to state a rule of integration).', '', '', 'STANDARD')
add('hhat', r'\hat h_{\mu\nu}', [r'\hat{h}'], r'The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation.', 'dimensionless', '', 'DERIVED')
add('Rhat', r'\hat R', [r'\hat{R}'], r'The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold.', '1/length$^2$', '', 'STANDARD')
add('kappa4', r'\kappa_4', [r'\kappa_{4}'], r'The coupling of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_4/(1 + 5r/6)$ (FE-59).', 'GeV$^{-2}$', r'$\kappa_4 \simeq 8\pi G_{\mathrm{N}} = 8\pi/M_{\mathrm{Pl}}^2$', 'ASSUMED')
add('LIG', r'\mathcal{L}_{\mathrm{IG}}', [r'\mathcal{L}_{\mathrm{IG}}'], r'The Lagrangian of the induced gravity of the fold.', 'GeV$^4$', '', 'ASSUMED')
add('Lff', r'\mathcal{L}_{\mathrm{ff}}', [r'\mathcal{L}_{\mathrm{ff}}'], r'The Lagrangian of the fold fluid (only its energy-momentum tensor $\mathcal{T}_{\mathrm{ff}}$ enters the equations).', 'GeV$^4$', '', 'ASSUMED')
add('Tff', r'\mathcal{T}_{\mathrm{ff}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{ff}}'], r'The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation).', 'GeV$^4$', '', 'ASSUMED')
add('rhoff', r'\rho_{\mathrm{ff}}', [r'\rho_{\mathrm{ff}}'], r'The energy density of the fold fluid.', 'GeV$^4$', r'$31HV_*/(4\kappa)$ at the static block', 'ASSUMED')
add('pff', r'p_{\mathrm{ff}}', [r'p_{\mathrm{ff}}'], r'The pressure of the fold fluid along ordinary space.', 'GeV$^4$', r'$-61HV_*/(8\kappa)$ at the static block', 'ASSUMED')
add('qff', r'q_{\mathrm{ff}}', [r'q_{\mathrm{ff}}'], r'The pressure of the fold fluid along the extra times.', 'GeV$^4$', r'$-61HV_*/(8\kappa)$ at the static block', 'ASSUMED')

# ---------------------------------------------------------------- Standard Model on the fold
add('LH', r'\mathcal{L}_{\mathrm{H}}', [r'\mathcal{L}_{\mathrm{H}}'], r'The Lagrangian of the Higgs doublet on the fold.', 'GeV$^4$', '', 'AUTHOR')
add('Lgauge', r'\mathcal{L}_{\mathrm{gauge}}', [r'\mathcal{L}_{\mathrm{gauge}}'], r'The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold.', 'GeV$^4$', '', 'STANDARD')
add('Lf', r'\mathcal{L}_{\mathrm{f}}', [r'\mathcal{L}_{\mathrm{f}}'], r'The kinetic Lagrangian of the quarks and leptons on the fold.', 'GeV$^4$', '', 'STANDARD')
add('LY', r'\mathcal{L}_{\mathrm{Y}}', [r'\mathcal{L}_{\mathrm{Y}}'], r'The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet.', 'GeV$^4$', '', 'STANDARD')
add('LP', r'\mathcal{L}_{\mathrm{P}}', [r'\mathcal{L}_{\mathrm{P}}'], r'The Lagrangian of the portals of dirac16complex at the fold.', 'GeV$^4$', '', 'INVENTED')
add('Phi', r'\Phi', [r'\Phi'], r'The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold.', 'GeV', '', 'AUTHOR')
add('Phitilde', r'\tilde\Phi', [r'\tilde{\Phi}'], r'The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$).', 'GeV', '', 'STANDARD')
add('Vpot', r'V(\Phi)', ['V'], r'The Higgs potential, $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$.', 'GeV$^4$', '', 'AUTHOR')
add('muH', r'\mu^2', [r'\mu'], r'The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$).', 'GeV$^2$', r'$\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$', 'AUTHOR')
add('lamH', r'\lambda', [r'\lambda'], r'The quartic coupling of the Higgs potential, $\lambda > 0$.', 'dimensionless', r'$\lambda = m_h^2/(2v^2) = 0.129$', 'AUTHOR')
add('vev', r'v', ['v'], r'The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$.', 'GeV', '246.22 GeV', 'STANDARD')
add('hHiggs', r'h', ['h'], r'The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$.', 'GeV', r'$m_h = 125.25$ GeV', 'STANDARD')
add('Aadhoc', r'\mathcal{A}', [r'\mathcal{A}'], r"The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$.", 'GeV', '', 'AUTHOR')
add('vA', r'v_{\mathcal{A}}', [r'v_{\mathcal{A}}'], r"The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc $= \mathrm{Exp}[-2\,a_{40}\,x_4]$ has $v_{\mathcal{A}} = 1$ in the unit of the field.", 'GeV', '1 (author)', 'AUTHOR')
add('a40', r'a_{40}', [r'a_{40}'], r'The decay constant of almightyAdHoc, $a_{40} > 0$: $\mathcal{A}$ falls by $\mathrm{e}$ in the time $1/(2a_{40})$.', 'GeV (1/length)', '', 'AUTHOR')
add('omegahat', r'\hat\omega_\mu', [r'\hat{\omega}'], r'The spin connection of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold acting on four-dimensional spinors.', '1/length', '', 'STANDARD')
add('g3', r'g_3', [r'g_{3}'], r'The $SU(3)_C$ gauge coupling (the strong coupling $g_s$).', 'dimensionless', r'$g_3(m_Z) = 1.2177$ ($\alpha_s = 0.1180$)', 'STANDARD')
add('g2', r'g_2', [r'g_{2}'], r'The $SU(2)_L$ gauge coupling (usually $g$).', 'dimensionless', r'$g_2(m_Z) = 0.6517$', 'STANDARD')
add('g1', r'g_1', [r'g_{1}'], r"The $U(1)_Y$ gauge coupling (usually $g'$; not normalised for grand unification).", 'dimensionless', r'$g_1(m_Z) = 0.3574$', 'STANDARD')
add('Ggluon', r'G^A_\mu,\ G^A_{\mu\nu}', ['G'], r'The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength.', 'GeV (field), GeV$^2$ (field strength)', '', 'AUTHOR')
add('Wsu2', r'W^I_\mu,\ W^I_{\mu\nu}', ['W'], r'The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength.', 'GeV (field), GeV$^2$ (field strength)', '', 'AUTHOR')
add('Bhyp', r'B_\mu,\ B_{\mu\nu}', ['B'], r'The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength.', 'GeV (field), GeV$^2$ (field strength)', '', 'AUTHOR')
add('tgen', r't^A', ['t'], r'The generators of $SU(3)$ on colour triplets, $t^A = \lambda_{\mathrm{GM}}^A/2$ (the Gell-Mann matrices halved), $\mathrm{tr}(t^At^B) = \delta^{AB}/2$.', 'dimensionless', '', 'STANDARD')
add('taupauli', r'\tau^I', [r'\tau'], r'The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square).', 'dimensionless', '', 'STANDARD')
add('Yhyp', r'Y_f', ['Y'], r'The hypercharge of a field (IN-13: $1/6$, $2/3$, $-1/3$, $-1/2$, $-1$, $0$ for $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$, $1/2$ for $\Phi$).', 'dimensionless', '', 'STANDARD')
add('fabc', r'f^{ABC}', ['f'], r'The structure constants of $SU(3)$, $[t^A, t^B] = \mathrm{i}f^{ABC}t^C$.', 'dimensionless', '', 'STANDARD')
add('epsLC', r'\epsilon^{IJK}', [r'\epsilon'], r'The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$.', 'dimensionless', '', 'STANDARD')
add('psiSM', r'\psi,\ \bar\psi', [r'\psi', r'\bar{\psi}'], r'A Standard-Model fermion field (a four-dimensional Weyl field of the fold with three generations, written as a four-component spinor of fixed chirality); $\bar\psi = \psi^\dagger\beta$; $\psi_f$ the fields of the kind $f$.', 'GeV$^{3/2}$', '', 'STANDARD')
add('gammahat', r'\hat\gamma^\mu', [r'\hat{\gamma}'], r'The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$.', 'dimensionless', '', 'STANDARD')
add('betaD', r'\beta', [r'\beta'], r'The matrix of the four-dimensional Dirac adjoint, $\beta = \hat\gamma^{(4)}$ (Hermitian, $\beta^2 = \mathbf{1}$).', 'dimensionless', '', 'STANDARD')
add('gamma5hat', r'\hat\gamma_5', [r'\hat{\gamma}_{5}'], r'The four-dimensional chirality matrix, $\hat\gamma_5 = \mathrm{i}\hat\gamma^{(4)}\hat\gamma^{(1)}\hat\gamma^{(2)}\hat\gamma^{(3)}$, $\hat\gamma_5^2 = \mathbf{1}$.', 'dimensionless', '', 'STANDARD')
add('PLhat', r'\hat P_{\mathrm{L}}', [r'\hat{P}_{\mathrm{L}}'], r'The four-dimensional left-handed projector, $\hat P_{\mathrm{L}} = (\mathbf{1} - \hat\gamma_5)/2$.', 'dimensionless', '', 'STANDARD')
add('PRhat', r'\hat P_{\mathrm{R}}', [r'\hat{P}_{\mathrm{R}}'], r'The four-dimensional right-handed projector, $\hat P_{\mathrm{R}} = (\mathbf{1} + \hat\gamma_5)/2$.', 'dimensionless', '', 'STANDARD')
add('Qdoub', r'Q,\ \bar Q', ['Q', r'\bar{Q}'], r'The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$).', 'GeV$^{3/2}$', '', 'AUTHOR')
add('uR', r'u_{\mathrm{R}}', [r'u_{\mathrm{R}}', r'\bar{u}_{\mathrm{R}}'], r'The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$).', 'GeV$^{3/2}$', '', 'STANDARD')
add('dR', r'd_{\mathrm{R}}', [r'd_{\mathrm{R}}', r'\bar{d}_{\mathrm{R}}'], r'The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$).', 'GeV$^{3/2}$', '', 'STANDARD')
add('ell', r'\ell,\ \bar\ell', [r'\ell', r'\bar{\ell}'], r'The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$).', 'GeV$^{3/2}$', '', 'AUTHOR')
add('eR', r'e_{\mathrm{R}}', [r'e_{\mathrm{R}}', r'\bar{e}_{\mathrm{R}}'], r'The right-handed electron, muon and tau (singlets, hypercharge $-1$).', 'GeV$^{3/2}$', '', 'AUTHOR')
add('nuR', r'\nu_{\mathrm{R}}', [r'\nu_{\mathrm{R}}', r'\bar{\nu}_{\mathrm{R}}'], r'The three right-handed neutrinos (gauge singlets).', 'GeV$^{3/2}$', '', 'ASSUMED')
add('Yuk', r'\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}', [r'\mathcal{Y}^{u}', r'\mathcal{Y}^{d}', r'\mathcal{Y}^{e}', r'\mathcal{Y}^{\nu}'], r'The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos.', 'dimensionless', '', 'STANDARD')

# ---------------------------------------------------------------- portals
add('cPhi', r'c_\Phi', [r'c_{\Phi}'], r'The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none).', 'GeV$^{-5}$', '', 'INVENTED')
add('cG', r'c^{G}_X', [r'c^{G}'], r'The gluon-kinetic portal coupling of the half $X$ of dirac16complex.', 'GeV$^{-7}$', '', 'INVENTED')
add('cW', r'c^{W}_X', [r'c^{W}'], r'The $W$-kinetic portal coupling of the half $X$.', 'GeV$^{-7}$', '', 'INVENTED')
add('cB', r'c^{B}_X', [r'c^{B}'], r'The $B$-kinetic portal coupling of the half $X$.', 'GeV$^{-7}$', '', 'INVENTED')
add('ddip', r'd_X', ['d'], r'The dipole-portal coupling of the half $X$ of dirac16complex with the hypercharge field strength.', 'GeV$^{-5}$', '', 'INVENTED')
add('Ddip', r'\mathcal{D}_X^{\mu\nu}', [r'\mathcal{D}'], r'The dipole (antisymmetric tensor) density of the half $X$ of dirac16complex at the fold, $\mathcal{D}_X^{\mu\nu} = \mathrm{i}\bar\Psi\Sigma^{\mu\nu}P_X\Psi$ (real, DERIVED).', 'GeV$^7$', '', 'DERIVED')
add('cf', r'c^{f}_X', [r'c^{f}'], r'The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind).', 'GeV$^{-7}$', '', 'INVENTED')
add('Jcur', r'J_f^\mu', ['J', r'J_{\ell}', r'J_{e}', r'J_{\nu}', r'J_{Q}', r'J_{u}', r'J_{d}'], r'The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the gauge currents (FE-16 to FE-18).', 'GeV$^3$', '', 'STANDARD')
add('jcur', r'j_X^\mu', ['j'], r'The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED).', 'GeV$^8$', '', 'DERIVED')


# ---------------------------------------------------------------- gravity: equations, sources
add('ip', r'p', ['index:p', 'p'], r'The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number.')
add('LovE', r'\mathcal{E}_{(p)}{}^M{}_N', [r'\mathcal{E}'], r'The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components.', '1/length$^{2p}$', '', 'STANDARD')
add('isigma', r'\sigma', ['index:\\sigma'], r'The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$.')
add('TPsi', r'\mathcal{T}_\Psi', [r'\mathcal{T}_{\Psi}'], r'The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$.', 'GeV$^8$', '', 'STANDARD')
add('Tbulk', r'\mathcal{T}_{\mathrm{bulk}}', [r'\mathcal{T}_{\mathrm{bulk}}'], r'The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components).', 'GeV$^8$', '', 'STANDARD')
add('Sfoldsrc', r'\mathcal{S}^a{}_b', [r'\mathcal{S}'], r'The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); $\kappa\mathcal{S}$ is the jump of the potential $\mathfrak{F}$.', 'GeV$^7$', '', 'DERIVED')
add('varepsilon', r'\varepsilon', [r'\varepsilon'], r'The half-thickness of a layer around the fold, taken to zero.', 'length', '', 'STANDARD')
add('Fpot', r'\mathfrak{F}^a{}_b', [r'\mathfrak{F}'], r'The junction potential: a function of the first $\sigma$-derivatives of the metric functions whose derivatives are the coefficients of the second $\sigma$-derivatives in $\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FE-4).', 'GeV', '', 'DERIVED')
add('fwarp', r'\mathfrak{f}', [r'\mathfrak{f}'], r'Any one of the three metric functions $\mathfrak{a}, \mathfrak{b}, \mathfrak{n}$ of the general warped metric (FE-34).', 'dimensionless', '', 'DERIVED')
add('awarp', r'\mathfrak{a}', [r'\mathfrak{a}'], r'The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35.', 'dimensionless', '', 'DERIVED')
add('bwarp', r'\mathfrak{b}', [r'\mathfrak{b}'], r'The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$.', 'dimensionless', '', 'DERIVED')
add('nwarp', r'\mathfrak{n}', [r'\mathfrak{n}'], r'The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$.', 'dimensionless', '', 'DERIVED')
add('TH', r'\mathcal{T}_{\mathrm{H}}', [r'\mathcal{T}_{\mathrm{H}}'], r'The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation).', 'GeV$^4$', '', 'STANDARD')
add('Tgauge', r'\mathcal{T}_{\mathrm{gauge}}', [r'\mathcal{T}_{\mathrm{gauge}}'], r'The energy-momentum tensor of the gauge fields.', 'GeV$^4$', '', 'STANDARD')
add('Tf', r'\mathcal{T}_{\mathrm{f}}', [r'\mathcal{T}_{\mathrm{f}}'], r'The energy-momentum tensor of the quarks and leptons.', 'GeV$^4$', '', 'STANDARD')
add('TP', r'\mathcal{T}_{\mathrm{P}}', [r'\mathcal{T}_{\mathrm{P}}'], r'The energy-momentum tensor of the portals of dirac16complex.', 'GeV$^4$', '', 'DERIVED')
add('TIG', r'\mathcal{T}_{\mathrm{IG}}', [r'\mathcal{T}_{\mathrm{IG}}'], r'The energy-momentum tensor of the induced gravity of the fold, $\mathcal{T}_{\mathrm{IG}}{}^\mu{}_\nu = -\hat G^\mu{}_\nu/\kappa_4$.', 'GeV$^4$', '', 'DERIVED')
add('Tany', r'\mathcal{T}', [r'\mathcal{T}'], r'The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$).', 'GeV$^4$', '', 'STANDARD')
add('Lfold', r'\mathcal{L}_{\mathrm{fold}}', [r'\mathcal{L}_{\mathrm{fold}}'], r'The Lagrangian of any one term of the fold (four-dimensional normalisation).', 'GeV$^4$', '', 'STANDARD')
add('LPsi', r'\mathcal{L}_\Psi', [r'\mathcal{L}_{\Psi}'], r'The Lagrangian of dirac16complex, the square bracket of IN-4.', 'GeV$^8$', '', 'RECORD')
add('Ghat', r'\hat G^\mu{}_\nu', [r'\hat{G}'], r'The Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold.', '1/length$^2$', '', 'STANDARD')

# ---------------------------------------------------------------- matter equations
add('Mfold', r'\mathbb{M}', [r'\mathbb{M}'], r'The fold operator of dirac16complex: the $16 \times 16$ matrix (with a derivative along the fold) built from the Standard-Model fields at the fold by varying the portals with respect to $\bar\Psi$ (FE-13).', r'GeV$^{-3}$ (so that $\mathbb{M}/V_*$ is dimensionless)', '', 'DERIVED')
add('Theta', r'\Theta', [r'\Theta'], r'The Yukawa source of the Higgs equation, $\Theta = -\partial\mathcal{L}_{\mathrm{Y}}/\partial\Phi^\dagger$ (a doublet of fermion bilinears).', 'GeV$^3$', '', 'STANDARD')
add('uL', r'u_{\mathrm{L}}', [r'u_{\mathrm{L}}', r'\bar{u}_{\mathrm{L}}'], r'The upper (up-type, left-handed) components of the quark doublets.', 'GeV$^{3/2}$', '', 'STANDARD')
add('dL', r'd_{\mathrm{L}}', [r'd_{\mathrm{L}}', r'\bar{d}_{\mathrm{L}}'], r'The lower (down-type, left-handed) components of the quark doublets.', 'GeV$^{3/2}$', '', 'STANDARD')
add('nuL', r'\nu_{\mathrm{L}}', [r'\nu_{\mathrm{L}}', r'\bar{\nu}_{\mathrm{L}}'], r'The upper (neutral, left-handed) components of the lepton doublets: the left-handed neutrinos.', 'GeV$^{3/2}$', '', 'STANDARD')
add('eL', r'e_{\mathrm{L}}', [r'e_{\mathrm{L}}', r'\bar{e}_{\mathrm{L}}'], r'The lower (charged, left-handed) components of the lepton doublets.', 'GeV$^{3/2}$', '', 'STANDARD')
add('Kport', r'\mathcal{K}_{G},\ \mathcal{K}_{W},\ \mathcal{K}_{B}', [r'\mathcal{K}_{G}', r'\mathcal{K}_{W}', r'\mathcal{K}_{B}'], r'The portal factors of the gauge kinetic terms, $\mathcal{K}_{G} = 1 + \sum_Xc^{G}_X\bar\Psi P_X\Psi$ (likewise for $W$ and $B$): the gauge couplings at the fold are divided by $\sqrt{\mathcal{K}}$.', 'dimensionless', '1 where dirac16complex vanishes', 'DERIVED')
add('Jcolour', r'J_{\mathrm{c}}^{A\nu}', [r'J_{\mathrm{c}}'], r'The colour current of the quarks.', 'GeV$^3$', '', 'STANDARD')
add('Jweak', r'J_{\mathrm{w}}^{I\nu}', [r'J_{\mathrm{w}}'], r'The weak-isospin current of the left-handed fermion doublets.', 'GeV$^3$', '', 'STANDARD')
add('JPhi', r'J_\Phi^{I\nu}', [r'J_{\Phi}'], r'The weak-isospin current of the Higgs doublet (it contains the mass terms of the $W$ fields); $J_\Phi^{2\,x_4}$ its isospin charge density with $I = 2$.', 'GeV$^3$', '', 'STANDARD')
add('JY', r'J_Y^\nu', [r'J_{Y}'], r'The hypercharge current of the fermions and of the Higgs doublet.', 'GeV$^3$', '', 'STANDARD')
add('Vport', r'\mathcal{V}^{f}_\mu', [r'\mathcal{V}^{f}', r'\mathcal{V}^{Q}', r'\mathcal{V}^{u}', r'\mathcal{V}^{d}', r'\mathcal{V}^{\ell}', r'\mathcal{V}^{e}', r'\mathcal{V}^{\nu}'], r'The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind.', 'GeV', '', 'DERIVED')
add('Rres', r'\mathcal{R}_{\mathcal{A}},\ \mathcal{R}_v', [r'\mathcal{R}', r'\mathcal{R}_{v}'], r'The residuals of the ad hoc Higgs vacuum in the upper ($\mathcal{R}_{\mathcal{A}}$) and lower ($\mathcal{R}_v$) components of the Higgs equation: what the ad hoc vacuum leaves unbalanced.', 'GeV$^3$', '', 'DERIVED')


# ---------------------------------------------------------------- background
add('Asf', r'\mathsf{A}', [r'\mathsf{A}'], r"The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$.", 'dimensionless', r"1 at the author's vacuum; $H_0/H$ today ($H_0$ the Hubble constant)", 'DERIVED')
add('Usf', r'\mathsf{U}', [r'\mathsf{U}'], r"The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$.", 'dimensionless', r'$\mathsf{U} = \mathsf{A}$ with frozen extra times', 'DERIVED')
add('A1sf', r'\mathsf{A}_1', [r'\mathsf{A}_{1}'], r"The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$.", 'dimensionless', '', 'DERIVED')
add('U1sf', r'\mathsf{U}_1', [r'\mathsf{U}_{1}'], r"The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$.", 'dimensionless', '', 'DERIVED')
add('Gfac', r'\mathcal{G}', [r'\mathcal{G}'], r'The factor of the $(\sigma, x_4)$ bulk equation of the author’s metric, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$.', 'dimensionless', '', 'DERIVED')
add('rhobulk', r'\rho_{\mathrm{bulk}}', [r'\rho_{\mathrm{bulk}}'], r'The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$.', 'GeV$^8$', '', 'DERIVED')
add('is', 's', ['index:s'], r'A second extra-time direction of the fold (as $r$, different from it).')
add('inn', 'n', ['index:n'], r'The order $n = 1, 2, \dots$ of a term of the power series of the metric (also its exponent of $\epsilon_{\mathrm{r}}$); $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{n}_n$ are the terms of order $n$.')
add('epsr', r'\epsilon_{\mathrm{r}}', [r'\epsilon_{\mathrm{r}}'], r'The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} \sim r = \kappa_4V_*/(\kappa H)$.', 'dimensionless', r'$\lesssim 10^{-15}$', 'DERIVED')
add('epsc', r'\epsilon_{\mathrm{c}}', [r'\epsilon_{\mathrm{c}}'], r'The bookkeeping parameter of the cosmological perturbations of the metric of the fold (the size of the CMB anisotropies).', 'dimensionless', r'$\sim 10^{-5}$', 'STANDARD')


def main():
    out = HERE / 'symbols'
    out.mkdir(exist_ok=True)
    (out / 'core.json').write_text(json.dumps(E, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('%d entries written to %s' % (len(E), out / 'core.json'))


if __name__ == '__main__':
    main()
