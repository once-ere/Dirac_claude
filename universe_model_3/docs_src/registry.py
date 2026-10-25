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
add('delta', r'\delta', [r'\delta', r'\delta_{X\mathrm{L}}'], r'The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}} = 1$ for $X = \mathrm{L}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise).')
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
add('Omega', r'\Omega_M', [r'\Omega'], r'The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$.', '1/length', '', 'RECORD')
add('omegaSC', r'\varpi_{Mab}', [r'\varpi'], r'The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$.', '1/length', '', 'STANDARD')
add('SigmaGen', r'\Sigma^{ab},\ \Sigma^{\mu\nu}', [r'\Sigma'], r"The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold.", 'dimensionless', '', 'AUTHOR')

# ---------------------------------------------------------------- stabiliser, fold
add('Tstab', r'\mathcal{T}_{\mathrm{stab}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{stab}}'], r'The energy-momentum tensor of the stabiliser of the bulk (frame components).', 'GeV$^8$', '', 'ASSUMED')
add('rhos', r'\rho_{\mathrm{s}}', [r'\rho_{\mathrm{s}}'], r'The energy density of the stabiliser.', 'GeV$^8$', r'$\kappa\rho_{\mathrm{s}} = -H^2/16$', 'ASSUMED')
add('ps', r'p_{\mathrm{s}}', [r'p_{\mathrm{s}}'], r'The pressure of the stabiliser (equal along $\sigma$, ordinary space and the extra times).', 'GeV$^8$', r'$\kappa p_{\mathrm{s}} = -5H^2/16$', 'ASSUMED')
add('Vstar', r'V_*', [r'V_{*}'], r'The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one.', 'length$^3$ (GeV$^{-3}$)', '', 'ASSUMED')
add('Vt', r'V_{\mathrm{t}}', [r'V_{\mathrm{t}}'], r'The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$.', 'length$^3$', '', 'ASSUMED')
add('Zfold', r'\mathcal{Z}', [r'\mathcal{Z}'], r'The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value.', 'dimensionless', '1 in the late universe', 'DERIVED')
add('Ffold', r'\mathbb{F}', [r'\mathbb{F}'], r'Any function of the fields at the fold (used to state a rule of integration).', '', '', 'STANDARD')
add('hhat', r'\hat h_{\mu\nu}', [r'\hat{h}'], r'The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation.', 'dimensionless', '', 'DERIVED')
add('Rhat', r'\hat R', [r'\hat{R}'], r'The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold.', '1/length$^2$', '', 'STANDARD')
add('kappa4', r'\kappa_4', [r'\kappa_{4}'], r'The coupling of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_4/(1 + 5\epsilon_{\mathrm{r}}/6)$ (FE-59).', 'GeV$^{-2}$', r'$\kappa_4 \simeq 8\pi G_{\mathrm{N}} = 8\pi/M_{\mathrm{Pl}}^2$', 'ASSUMED')
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
add('Yuk', r'\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}', [r'\mathcal{Y}', r'\mathcal{Y}^{u}', r'\mathcal{Y}^{d}', r'\mathcal{Y}^{e}', r'\mathcal{Y}^{\nu}'], r'The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos.', 'dimensionless', '', 'STANDARD')

# ---------------------------------------------------------------- portals
add('cPhi', r'c_\Phi', [r'c_{\Phi}'], r'The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none).', 'GeV$^{-5}$', '', 'INVENTED')
add('cG', r'c^{G}_X', [r'c^{G}'], r'The gluon-kinetic portal coupling of the half $X$ of dirac16complex.', 'GeV$^{-7}$', '', 'INVENTED')
add('cW', r'c^{W}_X', [r'c^{W}'], r'The $W$-kinetic portal coupling of the half $X$.', 'GeV$^{-7}$', '', 'INVENTED')
add('cB', r'c^{B}_X', [r'c^{B}'], r'The $B$-kinetic portal coupling of the half $X$.', 'GeV$^{-7}$', '', 'INVENTED')
add('ddip', r'd_X', ['d'], r'The dipole-portal coupling of the half $X$ of dirac16complex with the hypercharge field strength.', 'GeV$^{-5}$', '', 'INVENTED')
add('Ddip', r'\mathcal{D}_X^{\mu\nu}', [r'\mathcal{D}'], r'The dipole (antisymmetric tensor) density of the half $X$ of dirac16complex at the fold, $\mathcal{D}_X^{\mu\nu} = \mathrm{i}\bar\Psi\Sigma^{\mu\nu}P_X\Psi$ (real, DERIVED).', 'GeV$^7$', '', 'DERIVED')
add('cf', r'c^{f}_X', [r'c^{f}', r'c^{\ell}', r'c^{\nu}'], r'The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos.', 'GeV$^{-7}$', '', 'INVENTED')
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
add('epsr', r'\epsilon_{\mathrm{r}}', [r'\epsilon_{\mathrm{r}}'], r'The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$.', 'dimensionless', r'$\lesssim 10^{-15}$', 'DERIVED')
add('epsc', r'\epsilon_{\mathrm{c}}', [r'\epsilon_{\mathrm{c}}'], r'The bookkeeping parameter of the cosmological perturbations of the metric of the fold (the size of the CMB anisotropies).', 'dimensionless', r'$\sim 10^{-5}$', 'STANDARD')


# ---------------------------------------------------------------- dirac16complex modes and Kohn-Sham
add('omegafreq', r'\omega', [r'\omega'], r'A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$).', 'GeV', '', 'STANDARD')
add('chiprof', r'\chi(\sigma)', [r'\chi'], r'The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state.', 'GeV$^{2}$ (with the $V_*$ normalisation)', '', 'DERIVED')
add('chib', r'\chi_{\mathrm{b}}', [r'\chi_{\mathrm{b}}'], r'The profile of a state of dirac16complex bound to the fold.', 'GeV$^{2}$', '', 'DERIVED')
add('kvec', r'\vec k', [r'\vec{k}'], r'The (comoving) momentum along ordinary space, $\vec k^2$ its square.', 'GeV', '', 'STANDARD')
add('xvec', r'\vec x', [r'\vec{x}'], r'The position in ordinary space, $\vec x = (x_1, x_2, x_3)$.', 'length', '', 'AUTHOR')
add('gammavec', r'\vec\gamma', [r'\vec{\gamma}'], r'The three frame Dirac matrices of dirac16complex along ordinary space, $\vec\gamma = (\gamma^{(1)}, \gamma^{(2)}, \gamma^{(3)})$.', 'dimensionless', '', 'AUTHOR')
add('Kbulk', r'\mathbb{K}', [r'\mathbb{K}'], r"The transfer matrix of the profile equation at zero momentum, $\chi' = \mathbb{K}\chi$.", 'GeV', '', 'DERIVED')
add('qdecay', r'q', ['q'], r'The decay rate of a profile along $\sigma$ at frequency $\omega$, $q = \sqrt{m_\Psi^2 - \omega^2}$ (imaginary in the continuum).', 'GeV', '', 'DERIVED')
add('psigma', r'p_\sigma', [r'p_{\sigma}'], r'The momentum along the hidden direction (local wave number of a profile along $\sigma$).', 'GeV', '', 'DERIVED')
add('kappavec', r'\vec\kappa', [r'\vec{\kappa}'], r'A momentum along the extra times (three components); the fields of UM-3 have $\vec\kappa = 0$.', 'GeV', '', 'DERIVED')
add('muX', r'\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}', [r'\mu_{X}', r'\mu_{\mathrm{L}}', r'\mu_{\mathrm{R}}'], r'The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex (FE-39): the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract.', 'dimensionless', '', 'DERIVED')
add('mean', r'\langle\cdots\rangle', [], r'The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state).', '', '', 'STANDARD')
add('Gsq', r'\langle G^2\rangle', [], r'The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma).', 'GeV$^4$', '', 'STANDARD')
add('Wsq', r'\langle W^2\rangle', [], r'The mean square of the $SU(2)$ field strength, $\langle W^I_{\mu\nu}W^{I\mu\nu}\rangle$.', 'GeV$^4$', '', 'STANDARD')
add('Bsq', r'\langle B^2\rangle', [], r'The mean square of the hypercharge field strength, $\langle B_{\mu\nu}B^{\mu\nu}\rangle$.', 'GeV$^4$', '', 'STANDARD')
add('nf', r'n_f', [r'n_{f}'], r'The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium.', 'GeV$^3$', '', 'STANDARD')
add('qb', r'q_{\mathrm{b}}', [r'q_{\mathrm{b}}'], r'The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$.', 'GeV', '', 'DERIVED')
add('varsigma', r'\varsigma', [r'\varsigma', r'\varsigma_{-}'], r'The auxiliary variable of the bound-state condition, $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($\varsigma_- = \sqrt{-\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ when $\mu_{\mathrm{L}}\mu_{\mathrm{R}} < 0$).', 'dimensionless', '', 'DERIVED')
add('omegab', r'\omega_{\mathrm{b}}', [r'\omega_{\mathrm{b}}'], r'The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$.', 'GeV', '', 'DERIVED')
add('ns', r'n_{\mathrm{s}}', [r'n_{\mathrm{s}}'], r'The scalar density of dirac16complex in the Kohn-Sham state, $n_{\mathrm{s}} = \langle\bar\Psi\Psi\rangle = \mathrm{tr}\,\mathcal{N}$.', 'GeV$^7$', '', 'DERIVED')
add('Nmat', r'\mathcal{N}', [r'\mathcal{N}'], r'The one-body density matrix of dirac16complex, $\mathcal{N} = \sum_o\mathsf{n}_o\varphi_o\bar\varphi_o$ (a $16 \times 16$ matrix at each point).', 'GeV$^7$', '', 'DERIVED')
add('KSorb', r'\varphi_o,\ \bar\varphi_o', [r'\varphi', r'\bar{\varphi}'], r'A Kohn-Sham orbital of dirac16complex (a single-particle solution of FE-41) and its Dirac adjoint.', 'GeV$^{7/2}$', '', 'RECORD')
add('nocc', r'\mathsf{n}_o', [r'\mathsf{n}'], r'The occupation of the Kohn-Sham orbital $o$ (between 0 and 1).', 'dimensionless', '', 'RECORD')
add('Eorb', r'E', ['E'], r'An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino.', 'GeV', '', 'STANDARD')
add('muPsi', r'\mu_\Psi', [r'\mu_{\Psi}'], r'The chemical potential of dirac16complex.', 'GeV', '', 'DERIVED')
add('TPsiT', r'\mathsf{T}_\Psi', [r'\mathsf{T}_{\Psi}'], r'The temperature of dirac16complex.', 'GeV', '', 'DERIVED')
add('QPsi', r'Q_\Psi', [r'Q_{\Psi}'], r'The conserved charge of dirac16complex (the Noether charge of a change of the phase of $\Psi$ by a constant), a Krein form (indefinite).', 'dimensionless', '', 'DERIVED')
add('Bkrein', r'\mathfrak{B}', [r'\mathfrak{B}'], r'The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density.', 'dimensionless', '', 'DERIVED')
add('Qorb', r'\mathcal{Q}_o', [r'\mathcal{Q}'], r'The charge $Q_\Psi$ of the Kohn-Sham orbital $o$ (positive or negative).', 'dimensionless', '', 'DERIVED')
add('Delta', r'\Delta', [r'\Delta'], r'A change, difference or small variation of the quantity that follows ($\Delta\rho$ a perturbation, $\Delta m^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$).', '', '', 'STANDARD')

# ---------------------------------------------------------------- Standard Model on the fold
add('geff', r'g_{k,\mathrm{eff}}', [r'g_{1,\mathrm{eff}}', r'g_{2,\mathrm{eff}}', r'g_{3,\mathrm{eff}}'], r'The effective (canonically normalised) gauge couplings of the fold when the fold factor is $\mathcal{Z}$, $g_{k,\mathrm{eff}} = g_k/\sqrt{\mathcal{Z}}$ ($k = 1, 2, 3$).', 'dimensionless', '', 'DERIVED')
add('lameff', r'\lambda_{\mathrm{eff}}', [r'\lambda_{\mathrm{eff}}'], r'The effective quartic Higgs coupling, $\lambda/\mathcal{Z}$.', 'dimensionless', '', 'DERIVED')
add('Yeff', r'\mathcal{Y}_{\mathrm{eff}}', [r'\mathcal{Y}_{\mathrm{eff}}'], r'The effective Yukawa matrices, $\mathcal{Y}/\sqrt{\mathcal{Z}}$ (for each of $\mathcal{Y}^{u}, \mathcal{Y}^{d}, \mathcal{Y}^{e}, \mathcal{Y}^{\nu}$).', 'dimensionless', '', 'DERIVED')
add('GNeff', r'G_{\mathrm{N,eff}}', [r'G_{\mathrm{N,eff}}'], r'The effective Newton constant of the fold, $G_{\mathrm{N}}/\mathcal{Z}$.', 'GeV$^{-2}$', '', 'DERIVED')
add('GN', r'G_{\mathrm{N}}', [r'G_{\mathrm{N}}'], r'Newton’s constant of four-dimensional gravity on the fold, $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$.', 'GeV$^{-2}$', r'$6.708\times10^{-39}$ GeV$^{-2}$', 'STANDARD')
add('mW', r'm_{\mathrm{W}}', [r'm_{\mathrm{W}}'], r'The mass of the $W$ bosons.', 'GeV', '80.37 GeV ($\\mathcal{A} = 0$)', 'STANDARD')
add('mZ', r'm_{\mathrm{Z}}', [r'm_{\mathrm{Z}}'], r'The mass of the $Z$ boson.', 'GeV', '91.19 GeV ($\\mathcal{A} = 0$)', 'STANDARD')
add('GF', r'G_{\mathrm{F}}', [r'G_{\mathrm{F}}'], r'The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in FE-45 the Fermi constant of the ad hoc vacuum, which is $G_{\mathrm{F,loc}}$ of FE-49.', 'GeV$^{-2}$', r'$1.1664\times10^{-5}$ GeV$^{-2}$', 'STANDARD')
add('mh', r'm_h', [r'm_{h}'], r'The mass of the Higgs boson.', 'GeV', '125.25 GeV', 'STANDARD')
add('Aphoton', r'A_\mu', ['A'], r'The photon field: the massless combination of $W^1, W^2, W^3$ and $B$ (canonically normalised).', 'GeV', '', 'STANDARD')
add('nI', r'n^I', [r'n^{I}'], r'The unit isovector of the ad hoc vacuum, $n = (2\mathcal{A}v, 0, \mathcal{A}^2 - v^2)/(\mathcal{A}^2 + v^2)$, which fixes which combination of $W^1, W^2, W^3$ joins $B$ in the photon.', 'dimensionless', r'$(0, 0, -1)$ for $\mathcal{A} = 0$', 'DERIVED')
add('Umix', r'U_{f\mathrm{L}},\ U_{f\mathrm{R}}', [r'U_{u\mathrm{L}}', r'U_{u\mathrm{R}}', r'U_{d\mathrm{L}}', r'U_{d\mathrm{R}}', r'U_{e\mathrm{L}}', r'U_{e\mathrm{R}}', r'U_{\nu \mathrm{L}}', r'U_{\nu \mathrm{R}}'], r'The unitary $3 \times 3$ matrices that diagonalise the mass matrices of the up quarks, the down quarks, the charged leptons and the neutrinos (left-handed and right-handed rotations).', 'dimensionless', '', 'STANDARD')
add('mferm', r'm_u, \dots, m_3', [r'm_{u}', r'm_{c}', r'm_{t}', r'm_{d}', r'm_{s}', r'm_{b}', r'm_{e}', r'm_{\mu}', r'm_{\tau}', r'm_{1}', r'm_{2}', r'm_{3}'], r'The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses).', 'GeV', r'measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.51\times10^{-3}$ eV$^2$', 'STANDARD')
add('Ckm', r'V_{\mathrm{CKM}}', [r'V_{\mathrm{CKM}}'], r'The quark mixing matrix (Cabibbo-Kobayashi-Maskawa).', 'dimensionless', '', 'STANDARD')
add('Pmns', r'U_{\mathrm{PMNS}}', [r'U_{\mathrm{PMNS}}'], r'The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; $U_{\alpha i}$ are its entries.', 'dimensionless', r'$\theta_{12} = 33.4^\circ$, $\theta_{23} = 49.0^\circ$, $\theta_{13} = 8.57^\circ$', 'STANDARD')
add('nugen', r'\nu_\alpha,\ \nu_i', [r'\nu', r'\bar{\nu}'], r'A neutrino field: $\nu_\alpha$ the flavour states ($\alpha = e, \mu, \tau$), $\nu_i$ the mass states ($i = 1, 2, 3$).', 'GeV$^{3/2}$', '', 'STANDARD')
add('LCC', r'\mathcal{L}_{\mathrm{CC}}', [r'\mathcal{L}_{\mathrm{CC}}'], r'The charged-current interaction of the quarks and leptons with the $W$ bosons.', 'GeV$^4$', '', 'STANDARD')
add('hatferm', r'\hat u_{\mathrm{L}},\ \hat d_{\mathrm{L}},\ \hat e_{\mathrm{L}\alpha}', [r'\bar{\hat u}_{\mathrm{L}}', r'\hat{u}_{\mathrm{L}}', r'\hat{d}_{\mathrm{L}}', r'\hat{e}_{\mathrm{L}\alpha}'], r'The left-handed quarks and charged leptons in the mass basis ($\hat e_{\mathrm{L}\alpha}$ the charged lepton of flavour $\alpha$).', 'GeV$^{3/2}$', '', 'STANDARD')
add('gport', r'\mathfrak{g}_{\Phi},\ \mathfrak{g}_{G},\ \mathfrak{g}_{f},\ \mathfrak{g}_{h\chi}', [r'\mathfrak{g}_{\Phi}', r'\mathfrak{g}_{G}', r'\mathfrak{g}_{f}', r'\mathfrak{g}_{h\chi}'], r'The four-dimensional couplings of the bound states $\chi$ of dirac16complex to the Standard Model (FE-47): to $\Phi^\dagger\Phi$, to the gluon kinetic density, to the number densities of the fermions of kind $f$, and the Yukawa coupling of the Higgs boson to $\chi$.', r'$\mathfrak{g}_{\Phi}$: GeV$^{-1}$; $\mathfrak{g}_{G}$: GeV$^{-3}$; $\mathfrak{g}_{f}$: GeV$^{-2}$; $\mathfrak{g}_{h\chi}$: dimensionless', '', 'DERIVED')


# ---------------------------------------------------------------- neutrino flavours
add('vhat', r'\hat v,\ \hat v^\mu', [r'\hat{v}'], r'The direction of motion of a neutrino: the unit vector $\hat v = \vec p/\lvert\vec p\rvert$ ($\hat v_{\vec p}$, $\hat v_{\vec q}$ for the momenta $\vec p$, $\vec q$), and the four-vector $\hat v^\mu = (1, \hat v)$ in the order $(x_4; x_1, x_2, x_3)$; $\mathrm{d}^2\hat v$ is the element of solid angle of the directions.', 'dimensionless', '', 'STANDARD')
add('nablavec', r'\vec\nabla', [r'\vec{\nabla}'], r'The gradient along ordinary space, $\vec\nabla = (\partial_{x_1}, \partial_{x_2}, \partial_{x_3})$ (in the local frame of the medium).', '1/length', '', 'STANDARD')
add('pvec', r'\vec p', [r'\vec{p}'], r'The momentum of a neutrino (three components along ordinary space, in the rest frame of the medium); $\lvert\vec p\rvert = E$ for a neutrino of negligible mass.', 'GeV', '', 'STANDARD')
add('qvec', r'\vec q', [r'\vec{q}'], r'The momentum of another neutrino of the medium (the integration variable of the neutrino-neutrino potential); $\mathrm{d}^3\vec q$ its volume element.', 'GeV', '', 'STANDARD')
add('rhoflav', r'\varrho_{\vec p},\ \bar\varrho_{\vec p}', [r'\varrho', r'\bar{\varrho}'], r'The $3 \times 3$ flavour density matrices of the neutrinos and of the antineutrinos of momentum $\vec p$ in the basis $e, \mu, \tau$: the diagonal entries are the occupation numbers of the three flavours, the off-diagonal entries the coherence between the flavours; $\bar\varrho$ is defined with the flavour indices in the reversed order, so that it obeys an equation of the same form.', 'dimensionless', '', 'STANDARD')
add('Hflav', r'\mathsf{H}_{\vec p},\ \bar{\mathsf{H}}_{\vec p}', [r'\mathsf{H}', r'\bar{\mathsf{H}}'], r'The flavour Hamiltonians ($3 \times 3$ Hermitian matrices) of the neutrinos and of the antineutrinos of momentum $\vec p$.', 'GeV', '', 'STANDARD')
add('Ccoll', r'\mathcal{C}_{\vec p},\ \bar{\mathcal{C}}_{\vec p}', [r'\mathcal{C}', r'\bar{\mathcal{C}}'], r'The collision terms ($3 \times 3$ matrices) of the neutrinos and the antineutrinos of momentum $\vec p$: the rates of change of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$ by emission, absorption, scattering and pair processes with the matter.', 'GeV', '', 'STANDARD')
add('Mmass', r'\mathsf{M}^2', [r'\mathsf{M}'], r'The diagonal matrix of the squared masses of the three neutrino mass states, $\mathsf{M}^2 = \mathrm{diag}(m_1^2, m_2^2, m_3^2)$ ($\mathsf{M}$ appears only squared).', r'GeV$^2$ (of $\mathsf{M}^2$)', '', 'STANDARD')
add('Vm', r'\mathsf{V}_{\mathrm{m}}', [r'\mathsf{V}_{\mathrm{m}}'], r'The matter potential of the neutrinos (a $3 \times 3$ matrix in flavour space) from their forward scattering on the electrons, positrons and neutrons of the medium.', 'GeV', '', 'STANDARD')
add('Vnunu', r'\mathsf{V}_{\nu\nu}', [r'\mathsf{V}_{\nu \nu}'], r'The neutrino-neutrino potential (a $3 \times 3$ matrix in flavour space) from the forward scattering of a neutrino on the other neutrinos and antineutrinos of the medium; it depends on their flavour content and their directions.', 'GeV', '', 'STANDARD')
add('VPsi', r'V_\Psi', [r'V_{\Psi}'], r'The potential energy that dirac16complex gives every neutrino through the current portal of the lepton doublets, $V_\Psi = \mathcal{V}^{\ell}_{x_4}$ (the same for the three flavours).', 'GeV', '', 'DERIVED')
add('vloc', r'v_{\mathrm{loc}}', [r'v_{\mathrm{loc}}'], r'The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum.', 'GeV', r'$v$ in the late universe outside dense dirac16complex', 'DERIVED')
add('GFloc', r'G_{\mathrm{F,loc}}', [r'G_{\mathrm{F,loc}}'], r'The local Fermi constant, $G_{\mathrm{F,loc}} = 1/(\sqrt2\,v_{\mathrm{loc}}^2)$ ($= G_{\mathrm{F}}$ where $v_{\mathrm{loc}} = v$).', 'GeV$^{-2}$', '', 'DERIVED')
add('ne', r'n_e', [r'n_{e}'], r'The number density of electrons (bound and free; in a supernova all are free, in the recombining universe $x_{\mathrm{e}}n_e$ is the density of the free electrons).', 'GeV$^3$ (cm$^{-3}$)', '', 'STANDARD')
add('nebar', r'n_{\bar e}', [r'n_{\bar e}'], r'The number density of positrons.', 'GeV$^3$', '', 'STANDARD')
add('nn', r'n_n', [r'n_{n}'], r'The number density of neutrons.', 'GeV$^3$', '', 'STANDARD')
add('thetamix', r'\theta', [r'\theta'], r'The vacuum mixing angle of two neutrino flavours (in the two-flavour description of a resonance, one of the three angles $\theta_{12}, \theta_{13}, \theta_{23}$ of $U_{\mathrm{PMNS}}$).', 'dimensionless', '', 'STANDARD')
add('thetam', r'\theta_{\mathrm{m}}', [r'\theta_{\mathrm{m}}'], r'The mixing angle of two neutrino flavours in matter.', 'dimensionless', '', 'STANDARD')
add('mmass', r'm', ['m'], r'A mass: $m_i$ the mass of the neutrino mass state $i$; in $\Delta m^2$ the squared-mass difference of two neutrino mass states ($m_2^2 - m_1^2$ for the two states of a resonance, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1).', 'GeV', '', 'STANDARD')
add('VCC', r'V_{\mathrm{CC}}', [r'V_{\mathrm{CC}}'], r'The charged-current matter potential of the electron neutrinos (forward scattering on electrons through $W$ exchange).', 'GeV', '', 'STANDARD')
add('neres', r'n_{e,\mathrm{res}}', [r'n_{e,\mathrm{res}}'], r'The electron density at which the flavour conversion in matter is resonant (the Mikheyev-Smirnov-Wolfenstein resonance).', 'GeV$^3$', '', 'STANDARD')
add('PLZ', r'P_{\mathrm{LZ}}', [r'P_{\mathrm{LZ}}'], r'The probability that a neutrino jumps between the eigenstates of matter at the resonance (Landau-Zener); $P_{\mathrm{LZ}} = 0$ is an adiabatic resonance.', 'dimensionless', '', 'STANDARD')
add('rrad', r'r', ['r'], r'The distance from the centre of the star along the path of a neutrino.', 'length', '', 'STANDARD')
add('res', r'\mathrm{res}', [r'\mathrm{res}'], r'The label of a quantity evaluated at the resonance, where $n_e = n_{e,\mathrm{res}}$.', '', '', 'STANDARD')
add('GELN', r'\mathcal{G}_{\mathrm{ELN}}(\hat v)', [r'\mathcal{G}_{\mathrm{ELN}}'], r'The angular distribution of the electron lepton number carried by the neutrinos minus that carried by the heavy-lepton neutrinos, per unit solid angle of the direction $\hat v$, multiplied by $\sqrt2G_{\mathrm{F,loc}}$.', 'GeV', '', 'STANDARD')
add('Focc', r'\mathcal{F}_{e},\ \bar{\mathcal{F}}_{e},\ \mathcal{F}_{x},\ \bar{\mathcal{F}}_{x}', [r'\mathcal{F}_{e}', r'\bar{\mathcal{F}}_{e}', r'\mathcal{F}_{x}', r'\bar{\mathcal{F}}_{x}'], r'The occupation numbers of the electron neutrinos, of the electron antineutrinos, and of one heavy-lepton neutrino and antineutrino ($x = \mu$ or $\tau$), as functions of the energy $E$ and the direction $\hat v$ (the diagonal entries of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$); in a transport code, the same for the number of particles in an energy bin.', 'dimensionless', '', 'STANDARD')
add('etaM', r'\eta_{\mathrm{M}}^{\mu\nu}', [r'\eta_{\mathrm{M}}'], r'The Minkowski metric of the four-vectors $\hat v^\mu$, $\eta_{\mathrm{M}} = \mathrm{diag}(1, -1, -1, -1)$ in the order $(x_4; x_1, x_2, x_3)$.', 'dimensionless', '', 'STANDARD')
add('Omegafw', r'\Omega_{\mathrm{fw}}', [r'\Omega_{\mathrm{fw}}'], r'The (complex) frequency of a flavour wave of the neutrino gas, measured from the shift caused by the potentials; an imaginary part greater than zero is an instability.', 'GeV', '', 'STANDARD')
add('Kvec', r'\vec K', [r'\vec{K}'], r'The (real) wave vector of a flavour wave of the neutrino gas, measured from the shift caused by the potentials.', 'GeV', '', 'STANDARD')
add('deltaFC', r'\delta_{\mathrm{FC}}', [r'\delta_{\mathrm{FC}}'], r'The occupation (or number per energy bin) of electron neutrino-antineutrino pairs converted into heavy-lepton pairs by the flavour equipartition FE-52; a negative value converts heavy-lepton pairs into electron pairs.', 'dimensionless', '', 'ASSUMED')
add('rhob', r'\rho_{\mathrm{b}}', [r'\rho_{\mathrm{b}}'], r'The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today).', 'GeV$^4$', '', 'STANDARD')
add('rhoFC', r'\rho_{\mathrm{FC}}', [r'\rho_{\mathrm{FC}}'], r'The baryon density below which the flavour equipartition FE-52 is applied (the critical density $\rho_{\mathrm{c}}$ of Gogilashvili and Tamborra).', 'GeV$^4$ (g/cm$^3$)', r'$10^9$, $10^{10}$, $10^{11}$ or $10^{13}$ g/cm$^3$', 'STANDARD')
add('x4b', r'x_{4,\mathrm{b}}', [r'x_{4,\mathrm{b}}'], r'The time of the bounce of the collapsing stellar core.', 'length (= time)', '', 'STANDARD')
add('tFC', r't_{\mathrm{FC}}', [r't_{\mathrm{FC}}'], r'The time after the bounce from which the flavour equipartition FE-52 is applied.', 'time', '0.02 s', 'STANDARD')
add('Neff', r'N_{\mathrm{eff}}', [r'N_{\mathrm{eff}}'], r'The effective number of neutrino species: the energy density of the relativistic particles other than photons in units of that of one neutrino species whose temperature is $(4/11)^{1/3}$ times that of the photons.', 'dimensionless', r'3.044 (Standard Model); measured $2.99 \pm 0.17$ (Planck 2018)', 'STANDARD')
add('rhonu', r'\rho_\nu', [r'\rho_{\nu}'], r'The energy density of the neutrinos and antineutrinos of all flavours.', 'GeV$^4$', '', 'STANDARD')
add('rhogamma', r'\rho_\gamma', [r'\rho_{\gamma}'], r'The energy density of the photons.', 'GeV$^4$', '', 'STANDARD')
add('Tnu', r'\mathsf{T}_\nu', [r'\mathsf{T}_{\nu}'], r'The temperature of the cosmic neutrino background; $\mathsf{T}_\nu^{(0)}$ its value today.', 'GeV (or K)', '1.945 K today', 'STANDARD')
add('Tgamma', r'\mathsf{T}_\gamma', [r'\mathsf{T}_{\gamma}'], r'The temperature of the photons (of the CMB); $\mathsf{T}_\gamma^{(0)}$ its value today.', 'GeV (or K)', '2.7255 K today', 'STANDARD')
add('nnu', r'n_\nu', [r'n_{\nu}'], r'The number density of the cosmic neutrino background per flavour (neutrinos plus antineutrinos, one helicity each); $n_\nu^{(0)}$ its value today.', 'GeV$^3$', r'112 cm$^{-3}$ today', 'STANDARD')
add('zeta', r'\zeta', [r'\zeta'], r'The Riemann zeta function; $\zeta(3) = 1.2020569$.', 'dimensionless', '', 'STANDARD')

# ---------------------------------------------------------------- cosmological perturbations
add('ascale', r'a,\ \dot a,\ \ddot a', ['a', r'\dot{a}', r'\ddot{a}'], r'The scale factor of the fold, $a = \mathrm{e}^{a_4}$ (normalised to 1 today by the choice of the comoving coordinates $x_1, x_2, x_3$), and its first and second derivatives with respect to the conformal time $\tau_{\mathrm{c}}$.', 'dimensionless', '', 'STANDARD')
add('tauc', r'\tau_{\mathrm{c}}', [r'\tau_{\mathrm{c}}'], r'The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{d}x_4/a$; a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$.', 'length (= time)', '', 'STANDARD')
add('Hconf', r'\mathcal{H}', [r'\mathcal{H}'], r"The conformal expansion rate, $\mathcal{H} = \dot a/a = a\,a_4'$.", '1/length', '', 'STANDARD')
add('psiB', r'\psi_{\mathrm{B}},\ \dot\psi_{\mathrm{B}}', [r'\psi_{\mathrm{B}}', r'\dot{\psi}_{\mathrm{B}}'], r'The Bardeen potential of the time-time part of the perturbed metric of the fold (the Newtonian potential) in the conformal Newtonian gauge, a function of $\tau_{\mathrm{c}}$ and of the wave number $k$, and its derivative with respect to $\tau_{\mathrm{c}}$.', 'dimensionless', '', 'STANDARD')
add('phiB', r'\phi_{\mathrm{B}},\ \dot\phi_{\mathrm{B}},\ \ddot\phi_{\mathrm{B}}', [r'\phi_{\mathrm{B}}', r'\dot{\phi}_{\mathrm{B}}', r'\ddot{\phi}_{\mathrm{B}}'], r'The Bardeen potential of the space-space part of the perturbed metric of the fold (the curvature potential) in the conformal Newtonian gauge, and its first and second derivatives with respect to $\tau_{\mathrm{c}}$.', 'dimensionless', '', 'STANDARD')
add('kwave', r'k', ['k'], r'The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$.', 'GeV (1/length)', '', 'STANDARD')
add('rhotot', r'\rho', [r'\rho'], r'The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation.', 'GeV$^4$', '', 'STANDARD')
add('Ptot', r'\mathcal{P}', [r'\mathcal{P}'], r'The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation.', 'GeV$^4$', '', 'STANDARD')
add('varthetatot', r'\vartheta', [r'\vartheta'], r'The divergence of the velocity of the total matter: $(\rho + \mathcal{P})\vartheta$ is the sum over the species of their energy density plus pressure times the divergence of their velocity.', '1/length', '', 'STANDARD')
add('Sigmas', r'\Sigma_{\mathrm{s}}', [r'\Sigma_{\mathrm{s}}'], r'The anisotropic stress (shear) of the total matter: $(\rho + \mathcal{P})\Sigma_{\mathrm{s}}$ is the sum over the species (photons and neutrinos) of their energy density plus pressure times their shear.', 'dimensionless', '', 'STANDARD')
add('deltachi', r'\delta_\chi,\ \dot\delta_\chi', [r'\delta_{\chi}', r'\dot{\delta}_{\chi}'], r'The density contrast of the dark matter (the bound states $\chi$ of dirac16complex), the perturbation of its energy density divided by its mean, and its derivative with respect to $\tau_{\mathrm{c}}$.', 'dimensionless', '', 'STANDARD')
add('varthetachi', r'\vartheta_\chi,\ \dot\vartheta_\chi', [r'\vartheta_{\chi}', r'\dot{\vartheta}_{\chi}'], r'The divergence of the velocity of the dark matter (for a Fourier mode, $\mathrm{i}k$ times its velocity along the wave vector), and its derivative.', '1/length', '', 'STANDARD')
add('deltab', r'\delta_{\mathrm{b}},\ \dot\delta_{\mathrm{b}}', [r'\delta_{\mathrm{b}}', r'\dot{\delta}_{\mathrm{b}}'], r'The density contrast of the baryons and its derivative.', 'dimensionless', '', 'STANDARD')
add('varthetab', r'\vartheta_{\mathrm{b}},\ \dot\vartheta_{\mathrm{b}}', [r'\vartheta_{\mathrm{b}}', r'\dot{\vartheta}_{\mathrm{b}}'], r'The divergence of the velocity of the baryons and its derivative.', '1/length', '', 'STANDARD')
add('deltagamma', r'\delta_\gamma,\ \dot\delta_\gamma', [r'\delta_{\gamma}', r'\dot{\delta}_{\gamma}'], r'The density contrast of the photons and its derivative.', 'dimensionless', '', 'STANDARD')
add('varthetagamma', r'\vartheta_\gamma,\ \dot\vartheta_\gamma', [r'\vartheta_{\gamma}', r'\dot{\vartheta}_{\gamma}'], r'The divergence of the velocity of the photons and its derivative.', '1/length', '', 'STANDARD')
add('deltanu', r'\delta_\nu,\ \dot\delta_\nu', [r'\delta_{\nu}', r'\dot{\delta}_{\nu}'], r'The density contrast of the relativistic neutrinos and its derivative.', 'dimensionless', '', 'STANDARD')
add('varthetanu', r'\vartheta_\nu,\ \dot\vartheta_\nu', [r'\vartheta_{\nu}', r'\dot{\vartheta}_{\nu}'], r'The divergence of the velocity of the relativistic neutrinos and its derivative.', '1/length', '', 'STANDARD')
add('Sigmagamma', r'\Sigma_\gamma', [r'\Sigma_{\gamma}'], r'The anisotropic stress (shear) of the photons.', 'dimensionless', '', 'STANDARD')
add('Sigmanu', r'\Sigma_\nu', [r'\Sigma_{\nu}'], r'The anisotropic stress (shear) of the relativistic neutrinos.', 'dimensionless', '', 'STANDARD')
add('Gammachib', r'\Gamma_{\chi\mathrm{b}}', [r'\Gamma_{\chi \mathrm{b}}'], r'The rate (per conformal time) at which the dark matter exchanges momentum with the baryons through the portal couplings of FE-47 (elastic scattering of $\chi$ on nuclei and electrons).', '1/length', 'negligible for the couplings that direct detection allows', 'DERIVED')
add('cs', r'c_{\mathrm{s}}', [r'c_{\mathrm{s}}'], r'The sound speed of the baryon gas: its square is the temperature of the gas divided by the mean mass per particle, times one minus a third of the logarithmic derivative of that temperature with respect to $a$.', 'dimensionless', '', 'STANDARD')
add('xe', r'x_{\mathrm{e}}', [r'x_{\mathrm{e}}'], r'The ionisation fraction: the fraction of the electrons that are free.', 'dimensionless', '', 'STANDARD')
add('sigmaT', r'\sigma_{\mathrm{T}}', [r'\sigma_{\mathrm{T}}'], r'The Thomson cross-section of the scattering of photons on free electrons.', 'GeV$^{-2}$', r'$6.6524587\times10^{-25}$ cm$^2$', 'STANDARD')
add('Rbg', r'\mathsf{R}', [r'\mathsf{R}'], r'The ratio of the inertia of the baryons to that of the photons, $\mathsf{R} = 3\rho_{\mathrm{b}}/(4\rho_\gamma)$.', 'dimensionless', '', 'STANDARD')
add('rhochi', r'\rho_\chi', [r'\rho_{\chi}'], r'The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today.', 'GeV$^4$', '', 'DERIVED')
add('il', r'l', ['index:l', 'l'], r'The multipole index and number ($l = 0, 1, 2, \dots$) of an expansion in Legendre polynomials of the direction of a photon or a neutrino relative to the wave vector, or of the CMB sky in spherical harmonics.')
add('Fgamma', r'\mathsf{F}_l,\ \dot{\mathsf{F}}_l', [r'\mathsf{F}', r'\mathsf{F}_{0}', r'\mathsf{F}_{1}', r'\mathsf{F}_{2}', r'\dot{\mathsf{F}}'], r'The multipoles of the temperature perturbation of the photons ($\mathsf{F}_0 = \delta_\gamma$, $\mathsf{F}_1 = 4\vartheta_\gamma/(3k)$, $\mathsf{F}_2 = 2\Sigma_\gamma$; the $F_{\gamma l}$ of Ma and Bertschinger) and their derivatives with respect to $\tau_{\mathrm{c}}$.', 'dimensionless', '', 'STANDARD')
add('Ggamma', r'\mathsf{G}_l,\ \dot{\mathsf{G}}_l', [r'\mathsf{G}', r'\mathsf{G}_{0}', r'\mathsf{G}_{2}', r'\dot{\mathsf{G}}'], r'The multipoles of the polarisation perturbation of the photons (the $G_{\gamma l}$ of Ma and Bertschinger) and their derivatives.', 'dimensionless', '', 'STANDARD')
add('Nnu', r'\mathsf{N}_l,\ \dot{\mathsf{N}}_l', [r'\mathsf{N}', r'\mathsf{N}_{1}', r'\mathsf{N}_{2}', r'\dot{\mathsf{N}}'], r'The multipoles of the perturbation of the relativistic neutrinos ($\mathsf{N}_0 = \delta_\nu$, $\mathsf{N}_1 = 4\vartheta_\nu/(3k)$, $\mathsf{N}_2 = 2\Sigma_\nu$) and their derivatives.', 'dimensionless', '', 'STANDARD')
add('Upsilonnu', r'\Upsilon_l(\mathsf{q}),\ \dot\Upsilon_l', [r'\Upsilon', r'\Upsilon_{0}', r'\Upsilon_{1}', r'\Upsilon_{2}', r'\dot{\Upsilon}', r'\dot{\Upsilon}_{0}', r'\dot{\Upsilon}_{1}'], r'The multipoles of the relative perturbation of the distribution of a massive neutrino state at the comoving momentum $\mathsf{q}$ (the $\Psi_l$ of Ma and Bertschinger) and their derivatives.', 'dimensionless', '', 'STANDARD')
add('qcom', r'\mathsf{q}', [r'\mathsf{q}'], r'The comoving momentum of a neutrino, $a\lvert\vec p\rvert$.', 'GeV', '', 'STANDARD')
add('Ecom', r'\mathsf{E}', [r'\mathsf{E}'], r'The comoving energy of a massive neutrino ($a$ times its energy).', 'GeV', '', 'STANDARD')
add('Fzero', r'\mathcal{F}_0(\mathsf{q})', [r'\mathcal{F}_{0}'], r'The unperturbed (Fermi-Dirac) occupation number of the cosmic neutrino background at the comoving momentum $\mathsf{q}$.', 'dimensionless', '', 'STANDARD')
add('rs', r'r_{\mathrm{s}}', [r'r_{\mathrm{s}}'], r'The comoving sound horizon at the drag epoch: the comoving distance that a sound wave of the photon-baryon fluid travels until the baryons are released from the photons.', 'length', r'about 147 Mpc (Planck 2018)', 'STANDARD')
add('taud', r'\tau_{\mathrm{d}}', [r'\tau_{\mathrm{d}}'], r'The conformal time of the drag epoch, when the baryons are released from the photons (redshift about 1060).', 'length (= time)', '', 'STANDARD')
add('csgb', r'c_{\gamma\mathrm{b}}', [r'c_{\gamma \mathrm{b}}'], r'The sound speed of the tightly coupled photon-baryon fluid.', 'dimensionless', '', 'STANDARD')
add('DM', r'D_{\mathrm{M}}(\mathsf{z})', [r'D_{\mathrm{M}}'], r'The transverse comoving distance (comoving angular-diameter distance) to the redshift $\mathsf{z}$, for a spatially flat fold.', 'length', '', 'STANDARD')
add('DH', r'D_{\mathrm{H}}(\mathsf{z})', [r'D_{\mathrm{H}}'], r'The Hubble distance at the redshift $\mathsf{z}$.', 'length', '', 'STANDARD')
add('DV', r'D_{\mathrm{V}}(\mathsf{z})', [r'D_{\mathrm{V}}'], r'The volume-averaged distance to the redshift $\mathsf{z}$.', 'length', '', 'STANDARD')
add('zred', r'\mathsf{z}', [r'\mathsf{z}'], r"The redshift, $1 + \mathsf{z} = 1/a$; $\mathsf{z}'$ an integration variable.", 'dimensionless', '', 'STANDARD')
add('H4', r'H_4', [r'H_{4}'], r"The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant.", 'GeV (1/time)', r'$H_4^{(0)} = 100\,h_{100}$ km/s/Mpc', 'STANDARD')
add('Cl', r'C_l^{\mathrm{TT}},\ C_l^{\mathrm{TE}},\ C_l^{\mathrm{EE}}', ['C'], r'The angular power spectra of the CMB at the multipole $l$: temperature with temperature, temperature with E-mode polarisation, E-mode polarisation with itself.', 'dimensionless', '', 'STANDARD')
add('CMBlab', r'\mathrm{T},\ \mathrm{E}', [r'\mathrm{T}', r'\mathrm{E}', r'\mathrm{TT}', r'\mathrm{TE}', r'\mathrm{EE}'], r'The labels of the CMB observables: $\mathrm{T}$ the temperature anisotropy, $\mathrm{E}$ the E-mode (gradient) polarisation; $\mathrm{TT}$, $\mathrm{TE}$, $\mathrm{EE}$ label the spectra of their products.')
add('Itrans', r'\mathcal{I}_l^{\mathrm{T}}(k),\ \mathcal{I}_l^{\mathrm{E}}(k)', [r'\mathcal{I}'], r'The transfer functions of the CMB: the multipole $l$ of the temperature or E-mode anisotropy today produced by a Fourier mode $k$ of unit primordial curvature perturbation, computed from FE-54 and FE-55 (the line-of-sight integral).', 'dimensionless', '', 'STANDARD')
add('PRspec', r'\mathcal{P}_{\mathcal{R}}(k)', [r'\mathcal{P}_{\mathcal{R}}'], r'The primordial power spectrum of the comoving curvature perturbation, per logarithmic interval of $k$.', 'dimensionless', '', 'ASSUMED')
add('As', r'A_{\mathrm{s}}', [r'A_{\mathrm{s}}'], r'The amplitude of the primordial curvature spectrum at the pivot $k_*$.', 'dimensionless', r'$2.10\times10^{-9}$ (Planck 2018)', 'ASSUMED')
add('nS', r'n_{\mathrm{S}}', [r'n_{\mathrm{S}}'], r'The spectral index of the primordial curvature spectrum.', 'dimensionless', '0.965 (Planck 2018)', 'ASSUMED')
add('kstar', r'k_*', [r'k_{*}'], r'The pivot wave number of the primordial spectrum.', 'GeV (1/length)', r'0.05 Mpc$^{-1}$', 'STANDARD')
add('Omegachi', r'\Omega_\chi', [r'\Omega_{\chi}'], r'The density parameter of the dark matter today.', 'dimensionless', r'$\Omega_\chi h_{100}^2 = 0.120$ (Planck 2018)', 'DERIVED')
add('Omegab', r'\Omega_{\mathrm{b}}', [r'\Omega_{\mathrm{b}}'], r'The density parameter of the baryons today.', 'dimensionless', r'$\Omega_{\mathrm{b}}h_{100}^2 = 0.0224$ (Planck 2018)', 'STANDARD')
add('OmegaL', r'\Omega_\Lambda', [r'\Omega_{\Lambda}'], r'The density parameter of the dark energy (the vacuum energy of the fold) today.', 'dimensionless', '0.685 (Planck 2018)', 'DERIVED')
add('Omeganu', r'\Omega_\nu', [r'\Omega_{\nu}'], r'The density parameter of the massive neutrinos of the CNB today.', 'dimensionless', '', 'STANDARD')
add('h100', r'h_{100}', [r'h_{100}'], r'The present expansion rate of the fold in units of 100 km/s/Mpc.', 'dimensionless', '0.674 (Planck 2018)', 'STANDARD')
add('rhoc', r'\rho_{\mathrm{c}}', [r'\rho_{\mathrm{c}}'], r'The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today.', 'GeV$^4$', r'$\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$', 'STANDARD')
add('rhoL', r'\rho_\Lambda', [r'\rho_{\Lambda}'], r'The vacuum energy density of the fold, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$ (FE-59).', 'GeV$^4$', '', 'DERIVED')

# ---------------------------------------------------------------- thermal history
add('TSM', r'\mathcal{T}_{\mathrm{SM}}', [r'\mathcal{T}_{\mathrm{SM}}'], r'The energy-momentum tensor of the Standard Model on the fold, $\mathcal{T}_{\mathrm{H}} + \mathcal{T}_{\mathrm{gauge}} + \mathcal{T}_{\mathrm{f}}$.', 'GeV$^4$', '', 'STANDARD')
add('Jgeo', r'\mathcal{J}^a{}_b', [r'\mathcal{J}'], r'The jump of the junction potential across the fold computed from the metric (the right-hand side of FE-30, or of FE-33 with frozen extra times): the geometric side of the junction condition, $\mathcal{J} = \kappa\mathcal{S}$.', 'GeV', '', 'DERIVED')
add('rhoSM', r'\rho_{\mathrm{SM}}', [r'\rho_{\mathrm{SM}}'], r'The energy density of the Standard-Model particles.', 'GeV$^4$', '', 'STANDARD')
add('grho', r'g_\rho', [r'g_{\rho}'], r'The effective number of relativistic degrees of freedom of the energy density.', 'dimensionless', '106.75 in the Standard Model above the electroweak scale', 'STANDARD')
add('gs', r'g_{\mathrm{s}}', [r'g_{\mathrm{s}}'], r'The effective number of relativistic degrees of freedom of the entropy density.', 'dimensionless', '3.909 today', 'STANDARD')
add('Ttemp', r'\mathsf{T}', [r'\mathsf{T}'], r'The temperature of the Standard-Model plasma (of the photons after the annihilation of electrons and positrons).', 'GeV', '', 'STANDARD')
add('sent', r's', ['s'], r'The entropy density of the Standard-Model plasma.', 'GeV$^3$', '', 'STANDARD')
add('MPl', r'M_{\mathrm{Pl}}', [r'M_{\mathrm{Pl}}'], r'The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$.', 'GeV', r'$1.221\times10^{19}$ GeV', 'STANDARD')
add('nchi', r'n_\chi', [r'n_{\chi}'], r'The number density of the dark-matter particles $\chi$ (particles plus antiparticles).', 'GeV$^3$', '', 'DERIVED')
add('nchieq', r'n_{\chi,\mathrm{eq}}', [r'n_{\chi ,\mathrm{eq}}'], r'The number density of $\chi$ in thermal equilibrium with the plasma (non-relativistic).', 'GeV$^3$', '', 'STANDARD')
add('gchi', r'g_\chi', [r'g_{\chi}'], r'The number of internal states of the bound level of $\chi$ that are in thermal equilibrium.', 'dimensionless', '', 'DERIVED')
add('sigmaann', r'\sigma_{\mathrm{ann}}', [r'\sigma_{\mathrm{ann}}'], r'The cross-section of the annihilation of $\chi$ with its antiparticle into Standard-Model particles (through the portals).', 'GeV$^{-2}$', '', 'DERIVED')
add('vrel', r'\mathsf{v}', [r'\mathsf{v}'], r'The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product.', 'dimensionless', '', 'STANDARD')
add('xf', r'x_{\mathrm{f}}', [r'x_{\mathrm{f}}'], r'The ratio of the mass of $\chi$ to the temperature at which its annihilations stop (freeze-out).', 'dimensionless', '20 to 25', 'STANDARD')
add('gstar', r'g_*', [r'g_{*}'], r'The effective number of relativistic degrees of freedom at the freeze-out ($g_\rho$ there).', 'dimensionless', '', 'STANDARD')
add('rhonuR', r'\rho_{\nu_{\mathrm{R}}}', [r'\rho_{\nu _{\mathrm{R}}}'], r'The energy density of the three right-handed neutrinos.', 'GeV$^4$', '', 'STANDARD')
add('CnuR', r'\mathcal{C}_{\nu_{\mathrm{R}}}', [r'\mathcal{C}_{\nu _{\mathrm{R}}}'], r'The collision term of the right-handed neutrinos: the rate at which collisions produce (or remove) their energy density.', 'GeV$^5$', '', 'STANDARD')
add('Tdec', r'\mathsf{T}_{\mathrm{dec}}', [r'\mathsf{T}_{\mathrm{dec}}'], r'The temperature at which the right-handed neutrinos decouple from the plasma.', 'GeV', '', 'STANDARD')


def main():
    out = HERE / 'symbols'
    out.mkdir(exist_ok=True)
    (out / 'core.json').write_text(json.dumps(E, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('%d entries written to %s' % (len(E), out / 'core.json'))


if __name__ == '__main__':
    main()
