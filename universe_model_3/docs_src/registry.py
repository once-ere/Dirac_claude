#!/usr/bin/env python3
r"""The symbol registry of the UM-3 documents (source).  Running this file writes docs_src/symbols/core.json, which the
symbol tool (tools/symbols_tool.py) reads.  Each entry: key -> (tex, atoms, meaning, units, value, status); see the
docstring of the symbol tool for the meaning of the fields.  One symbol, one meaning: an atom belongs to one entry.

Usage: python universe_model_3/docs_src/registry.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one surface of F, at z = pi/2: F is the union of these copies, one per period (example 2), and "the
fold" without a qualifier is the copy in the period that contains our world. A point of the fold is labelled by the seven
coordinates x1, ..., x7, and the metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.
Notation: ln is the natural logarithm, e Euler's number, exp(y) = e^y, sin, cos and cot = cos/sin the trigonometric
functions, tanh the hyperbolic tangent, |y| the absolute value; f(0+) and f(0-) are the limits of f(sigma) as sigma
approaches 0 from above and from below.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. The function W(sigma) = e^(-2 H |sigma|), which multiplies the squared steps of
ordinary space and of the extra times, is the warp factor of the metric (its square root e^(-H |sigma|) multiplies the
lengths); the time x4 is not warped. Four properties make the surface sigma = 0 a fold, and together they single it out
within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp factor is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|) equals 1 on the fold and
     decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function, a, b frame indices along the fold); it jumps by -2 H along ordinary space and along the extra times.
     The Einstein-Lovelock equations of UM-3, sum_p alpha_(p) E_(p)^a_b + Lambda delta^a_b = kappa T^a_b (E_(p) the
     Lovelock tensor of order p = 1, 2, 3, alpha_(p) = w_(p) H^(2-2p) its coupling with the weights w = (1, 1/20, 1/360),
     Lambda = -7 H^2 the cosmological constant, kappa = 8 pi G_8 the gravitational coupling of eight dimensions, T^a_b the
     energy-momentum tensor, delta^a_b the Kronecker delta), are linear in the second sigma-derivatives of the metric, so
     the jump puts a Dirac delta function delta_D(sigma) into them: the metric solves them only if the fold carries a thin
     source S^a_b, an energy-momentum tensor concentrated on sigma = 0, given by the integral of the equations across the
     fold (the junction conditions),
        (FD-11) kappa S^a_b = integral from sigma = 0- to 0+ of d sigma sum_p alpha_(p) E_(p)^a_b,
     with S^4_4 = -(its energy density), S^1_1 = S^2_2 = S^3_3 its pressure along ordinary space and S^5_5 = S^6_6 = S^7_7
     its pressure along the extra times; S is T integrated across the fold, an energy per unit volume of the six other
     directions of the fold (unit GeV^7). On the static block (a4 and b4 constant) and on an expanding fold whose extra
     times are frozen (b4 proportional to e^(a4), A = a4'/H, A1 = a4''/H^2)
        (FD-12) static block:      kappa S^a_b = -(32/5) H delta^a_b  (a pure tension),
                frozen extra times: kappa S^1_1 = -(16/15)(6 + 3 A^2 + 2 A1) H,  kappa S^4_4 = -(16/5)(2 + A^2) H,
                                    kappa S^5_5 = -(4/5)(8 + 8 A^2 + A^4 + 4 A1 + A^2 A1) H:
     the tension plus matter that obeys the Friedmann equations of general relativity. The fold is therefore not only a
     place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the author's ad hoc vacuum, a time-dependent
choice of its vacuum value; the gauge fields of SU(3)_C x SU(2)_L x U(1)_Y; three generations of quarks and leptons and
three right-handed neutrinos) and the fold fluid (its tension and the pressure along the extra times that keeps their
volume fixed) live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no field depends on the extra
times). Integrated over the extra times, the fold is the four-dimensional universe that we observe, with the metric
diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex (the author's spinor field of eight dimensions) and
gravity live in the bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that
the fold holds, and the portals (couplings between dirac16complex and Standard-Model fields) act at sigma = 0. In UM-3
files "the fold" means this surface; the examples below use the word for other surfaces with the same properties. The
word is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by the factor e is
called an e-folding.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp factor (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2
     diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
     line -infinity < sigma < infinity. A compact direction of length L would give every field a tower of particles with
     the masses 2 pi n/L, n = 1, 2, ... (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
     pi/(6 H) of x0 produces no such tower with the spacing 12 H, and the x0 mass of the bound states is their binding to
     the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every metric function of FD-4 depends on sigma
     through |sigma| and is folded at sigma = 0 in this sense.
  5. A fold map. In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map u -> u^2 of a line onto
     a half-line: it folds the line at u = 0, two points +u and -u land on the same point, and the derivative of the map
     vanishes on the fold. Near the fold the map from the author's coordinate x0 to the distance |sigma| from the fold is
     of this kind (FD-6), and g_x0x0 = cot(z)^2, the square of the derivative d sigma/d x0, vanishes there.
  6. The brane of Randall and Sundrum. The five-dimensional metric
        (FD-8)  dy_RS^2 + e^(-2 k_RS |y_RS|) (dx1^2 + dx2^2 + dx3^2 - dx4^2),
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2/kappa_5
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the vacuum energy Lambda_RS, and the bulk is otherwise empty. The fold of UM-3 is of the same kind: its static
     block is a vacuum of the bulk with a fold of pure tension (FD-12). It differs in that the time x4 is not warped,
     three extra times are warped together with ordinary space, the Lovelock terms add to the junction conditions, and
     the space is not cut at the brane: Randall and Sundrum identify the two sides of their brane (one physical side),
     while the fold of UM-3 has two distinct sides (example 7).
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a wave function that falls off
     exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
     equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex bound
     to the fold; at rest and without their self-interaction (the field is Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0). The profile is not a function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi (the average field that the particles of the gas create and feel): the four bound states of Krein
     charge -1 (the particles chi) are even under it and the four of Krein charge +1 are odd, so the mean field of the gas
     cannot mix the two signs of the indefinite charge. R_2 maps the bound states of one Krein charge onto those of the
     other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory (the eleven-dimensional theory whose limits include the superstring
     theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional
     planes left in place by the reflection are mirror surfaces (property 1); each carries one E8 gauge group while gravity
     fills the bulk. As in UM-3, the gauge fields live on the mirror surface and gravity in the bulk; unlike UM-3, the two
     sides of each plane are identified (one physical side).

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp factor vanishes,
    g_x0x0 diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp factor, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a
    kink and without a thin source.
END FOLD DEFINITION
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
add('identity', r'\mathbf{1},\ \mathbf{1}_8', [r'\mathbf{1}', r'\mathbf{1}_{8}'], r'The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix.', 'dimensionless')
add('partial', r'\partial', [r'\partial'], r'A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables.')
add('nabla', r'\nabla', [r'\nabla'], r'The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$).')
add('nablahat', r'\hat\nabla', [r'\hat{\nabla}'], r'The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold (for four-dimensional tensors of its metric $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the observable coordinates $x_1, \dots, x_4$; for $\hat\nabla_a\mathcal{S}^a{}_b$ of the induced metric of the seven-dimensional fold).')
add('delta', r'\delta', [r'\delta', r'\delta_{X\mathrm{L}}'], r'The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise).')
add('deltaD', r'\delta_{\mathrm{D}}', [r'\delta_{\mathrm{D}}'], r'The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$.', r'1/length (for $\delta_{\mathrm{D}}(\sigma)$)')
add('dagger', r'{}^\dagger', ['dagger'], r'Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product).')
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
        ('ia', 'a', r'A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed.'),
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
        ('ii', 'i', r'A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written.'),
        ('ij', 'j', r'A second generation or mass-state index (as $i$).'),
        ('ialpha', r'\alpha', r'A lepton-flavour index, $\alpha \in \{e, \mu, \tau\}$.'),
        ('ibeta', r'\beta', r'A second lepton-flavour index (as $\alpha$).'),
        ('iX', 'X', r'The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both.'),
        ('if', 'f', r'The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six.'),
        ('ipsi', r'\psi', r'The label of a Standard-Model fermion field in a sum: $\psi$ runs over $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$.'),
        ('ir', 'r', r'An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal).'),
        ('io', 'o', r'The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes.'),
]:
    add(k, letter, ['index:' + letter], text)

# ---------------------------------------------------------------- coordinates and geometry
add('Xcoord', r'X = \{x_0, \dots, x_7\}', ['X'], r"The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element.", 'length (each coordinate)', '', 'AUTHOR')
add('xfour', r'x', ['x'], r'The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$.', 'length (each coordinate)', '', 'AUTHOR')
add('x0', r'x_0', ['x_{0}'], r'The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$.', 'length', '', 'AUTHOR')
add('x1', r'x_1', ['x_{1}'], r'The first coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x2', r'x_2', ['x_{2}'], r'The second coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x3', r'x_3', ['x_{3}'], r'The third coordinate of ordinary 3-space.', 'length', '', 'AUTHOR')
add('x4', r'x_4', ['x_{4}'], r'The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$.', 'length (= time, $c = 1$)', '', 'AUTHOR')
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
add('Hconst', r'H', ['H'], r"The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter.", 'GeV (1/length)', '', 'AUTHOR')
add('a4', r'a_4', ['a_{4}'], r"The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate.", 'dimensionless', '', 'AUTHOR')
add('b4', r'b_4', ['b_{4}'], r"The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$).", 'dimensionless', '', 'AUTHOR')

# ---------------------------------------------------------------- gravity
add('Stot', r'S_{\mathrm{tot}}', [r'S_{\mathrm{tot}}'], r'The action of UM-3 (the integral of the Lagrangian density over spacetime); its variation with respect to every field gives the field equations.', 'dimensionless ($\\hbar = 1$)', '', 'ASSUMED')
add('SEL', r'S_{\mathrm{EL}}', [r'S_{\mathrm{EL}}'], r'The Einstein-Lovelock action of gravity in eight dimensions.', 'dimensionless', '', 'AUTHOR')
add('Sstab', r'S_{\mathrm{stab}}', [r'S_{\mathrm{stab}}'], r"The action of the stabiliser of the bulk, a medium that a static bulk required with the author's original Lovelock weights; with the corrected weights the stabiliser is zero and $S_{\mathrm{stab}}$ is not part of UM-3 (IN-7).", 'dimensionless', '', 'DERIVED')
add('SPsi', r'S_\Psi', [r'S_{\Psi}'], r'The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction).', 'dimensionless', '', 'RECORD')
add('Sfold', r'S_{\mathrm{fold}}', [r'S_{\mathrm{fold}}'], r'The action of the fold: the Standard Model, the portals of dirac16complex, the fold fluid and the Einstein-Hilbert term that the fields of the fold induce, all at $\sigma = 0$.', 'dimensionless', '', 'ASSUMED')
add('kappa', r'\kappa', [r'\kappa'], r'The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$.', 'GeV$^{-6}$', '', 'AUTHOR')
add('G8', r'G_8', [r'G_{8}'], r'The eight-dimensional Newton constant ($\kappa = 8\pi G_8$).', 'GeV$^{-6}$', '', 'AUTHOR')
add('alphaL', r'\alpha_{(p)}', [r'\alpha'], r'The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$).', 'GeV$^{2-2p}$', '', 'AUTHOR')
add('wL', r'w_{(p)}', ['w'], r"The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which gravitational waves travel at the speed of light in the bulk and on the fold (both coefficients of the bulk wave, $1 - 40w_{(2)} + 360w_{(3)}$ and $1 - 24w_{(2)} + 72w_{(3)}$, vanish). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons faster than light; they were corrected at the author's order of 2026-10-25.", 'dimensionless', '$(1, 1/20, 1/360)$; the author\'s original $(1, 1/32, 1/1152)$', 'AUTHOR (the form), DERIVED (the values)')
add('ctw', r'c_{\mathrm{t}}', [r'c_{\mathrm{t}}'], r'The coefficient of the second time derivative of a transverse traceless gravitational wave in the bulk at the static block, in units of its value with Einstein gravity alone: $c_{\mathrm{t}} = 1 - 40w_{(2)} + 360w_{(3)}$ (FE-68).', 'dimensionless', r"0 with the corrected weights; $1/16$ with the author's original weights", 'DERIVED')
add('cxw', r'c_{\mathrm{x}}', [r'c_{\mathrm{x}}'], r'The coefficient of the second derivatives along ordinary space and along $\sigma$ of the same wave, in the same units: $c_{\mathrm{x}} = 1 - 24w_{(2)} + 72w_{(3)}$ (FE-68); bulk gravitons move with the local speed $\sqrt{c_{\mathrm{x}}/c_{\mathrm{t}}}$.', 'dimensionless', r"0 with the corrected weights; $5/16$ with the author's original weights", 'DERIVED')
add('ycurv', r'\mathsf{y}', [r'\mathsf{y}'], r'The curvature of a seven-dimensional space of constant curvature $-\mathsf{y}H^2$ (in units of $-H^2$), times the time line: $\mathsf{y} = 1$ is the static block.', 'dimensionless', '', '')
add('LovL', r'\mathcal{L}_{(p)}', [r'\mathcal{L}'], r'The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density.', '1/length$^{2p}$', '', 'STANDARD')
add('Lambda', r'\Lambda', [r'\Lambda'], r"The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$).", 'GeV$^2$', '$-7H^2$; the author\'s original $-10H^2$', 'AUTHOR (the term), DERIVED (the value)')
add('LambdaN', r'\Lambda_{\mathrm{N}}', [r'\Lambda_{\mathrm{N}}'], r"The author's pure number in the vacuum equations of his notebook, $\Lambda = -\Lambda_{\mathrm{N}}H^2$: his original value 10, corrected to 7 on 2026-10-25.", 'dimensionless', '7 (the author\'s original 10)', 'AUTHOR')

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
add('Dcov', r'D_M,\ D_\mu', ['D'], r'The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$).', '1/length', '', 'STANDARD')
add('mPsi', r'm_\Psi', [r'm_{\Psi}'], r'The mass parameter of dirac16complex in the bulk.', 'GeV', '', 'RECORD')
add('lamPsi', r'\lambda_\Psi', [r'\lambda_{\Psi}'], r'The coupling of the contact self-interaction of dirac16complex.', 'GeV$^{-6}$', '', 'RECORD')
add('Omega', r'\Omega_M', [r'\Omega'], r'The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$.', '1/length', '', 'RECORD')
add('omegaSC', r'\varpi_{Mab}', [r'\varpi'], r'The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$.', '1/length', '', 'STANDARD')
add('SigmaGen', r'\Sigma^{ab},\ \Sigma^{\mu\nu}', [r'\Sigma'], r"The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold.", 'dimensionless', '', 'AUTHOR')

# ---------------------------------------------------------------- stabiliser, fold
add('Tstab', r'\mathcal{T}_{\mathrm{stab}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{stab}}'], r"The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric required with the author's original Lovelock weights, found and named by Claude (Anthropic) on 2026-10-24; with the corrected weights and $\Lambda = -7H^2$ it is zero (IN-7).", 'GeV$^8$', '0 with the corrected weights', 'DERIVED')
add('rhos', r'\rho_{\mathrm{s}}', [r'\rho_{\mathrm{s}}'], r"The energy density of the stabiliser of the bulk with the author's original weights; with frozen extra times it was the energy density of the bulk at which ordinary space stands still.", 'GeV$^8$', r"$\kappa\rho_{\mathrm{s}} = -H^2/16$ with the author's original weights; 0 with the corrected weights", 'DERIVED')
add('ps', r'p_{\mathrm{s}}', [r'p_{\mathrm{s}}'], r"The pressure of the stabiliser of the bulk with the author's original weights (equal along $\sigma$, ordinary space and the extra times).", 'GeV$^8$', r"$\kappa p_{\mathrm{s}} = -5H^2/16$ with the author's original weights; 0 with the corrected weights", 'DERIVED')
add('Vstar', r'V_*', [r'V_{*}'], r'The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one.', 'length$^3$ (GeV$^{-3}$)', '', 'ASSUMED')
add('Vt', r'V_{\mathrm{t}}', [r'V_{\mathrm{t}}'], r'The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$.', 'length$^3$', '', 'ASSUMED')
add('Zfold', r'\mathcal{Z}', [r'\mathcal{Z}'], r'The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value.', 'dimensionless', '1 in the late universe', 'DERIVED')
add('Ffold', r'\mathbb{F}', [r'\mathbb{F}'], r'Any function of the fields at the fold (used to state a rule of integration).', '', '', 'STANDARD')
add('hhat', r'\hat h_{\mu\nu}', [r'\hat{h}'], r'The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation.', 'dimensionless', '', 'DERIVED')
add('Rhat', r'\hat R', [r'\hat{R}'], r'The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold.', '1/length$^2$', '', 'STANDARD')
add('kappa7', r'\kappa_7', [r'\kappa_{7}'], r"The gravitational coupling of the fold: with the corrected Lovelock weights the thin source of the fold equals, to second order in the rates of expansion, the Einstein tensor of the seven-dimensional metric of the fold divided by $\kappa_7 = 15\kappa H/16$, and exactly so in the Friedmann equations of a fold with frozen extra times; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, if the fields of the fold induce one).", 'GeV$^{-5}$', r'$15\kappa H/16$', 'DERIVED')
add('kappaind', r'\kappa_{\mathrm{ind}}', [r'\kappa_{\mathrm{ind}}'], r'The coupling of the Einstein-Hilbert term $\hat R/(2\kappa_{\mathrm{ind}})$ that the quantum fluctuations of the fields of the fold may induce, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$; it adds to the gravity of the fold, $1/(8\pi G_{\mathrm{N}}) = V_*/\kappa_7 + 1/\kappa_{\mathrm{ind}}$.', 'GeV$^{-2}$', 'not fixed by UM-3', 'ESTIMATE')
add('LIG', r'\mathcal{L}_{\mathrm{IG}}', [r'\mathcal{L}_{\mathrm{IG}}'], r'The Lagrangian of the Einstein-Hilbert term of the four-dimensional metric of the fold that the quantum fluctuations of the fields of the fold induce; it adds to the Einstein-Hilbert term that the Lovelock terms give the fold and does not change the speed of gravitational waves.', 'GeV$^4$', '', 'ESTIMATE')
add('Lff', r'\mathcal{L}_{\mathrm{ff}}', [r'\mathcal{L}_{\mathrm{ff}}'], r'The Lagrangian of the fold fluid (only its energy-momentum tensor $\mathcal{T}_{\mathrm{ff}}$ enters the equations).', 'GeV$^4$', '', 'ASSUMED')
add('Tff', r'\mathcal{T}_{\mathrm{ff}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{ff}}'], r'The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation).', 'GeV$^4$', '', 'ASSUMED')
add('rhoff', r'\rho_{\mathrm{ff}}', [r'\rho_{\mathrm{ff}}'], r'The energy density of the fold fluid.', 'GeV$^4$', r'$\lambda_{\mathrm{F}} = 32HV_*/(5\kappa)$ (its tension)', 'ASSUMED (the fluid), DERIVED (the value)')
add('pff', r'p_{\mathrm{ff}}', [r'p_{\mathrm{ff}}'], r'The pressure of the fold fluid along ordinary space.', 'GeV$^4$', r'$-\lambda_{\mathrm{F}} = -32HV_*/(5\kappa)$', 'ASSUMED (the fluid), DERIVED (the value)')
add('qff', r'q_{\mathrm{ff}}', [r'q_{\mathrm{ff}}'], r'The pressure of the fold fluid along the extra times: minus its tension plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed.', 'GeV$^4$', r'$-\lambda_{\mathrm{F}} + q_{\mathrm{hold}}$; $-32HV_*/(5\kappa)$ at the static block', 'ASSUMED (the fluid), DERIVED (the value)')

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
add('vev', r'v', ['v'], r'The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$.', 'GeV', r'246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group)', 'STANDARD')
add('hHiggs', r'h', ['h'], r'The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$.', 'GeV', r'$m_h = 125.25$ GeV', 'STANDARD')
add('Aadhoc', r'\mathcal{A}', [r'\mathcal{A}'], r"The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$.", 'GeV', '', 'AUTHOR')
add('vA', r'v_{\mathcal{A}}', [r'v_{\mathcal{A}}'], r"The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc $= \mathrm{Exp}[-2\,a_{40}\,x_4]$ has $v_{\mathcal{A}} = 1$ in the units of his notebook.", 'GeV', r"1 in the units of the author's notebook; UM-3 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$)", 'AUTHOR (the form), ASSUMED (a free amplitude)')
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
add('Yhyp', r'Y_f', ['Y'], r'The hypercharge of a field, the charge of its coupling $g_1Y_fB_\mu$ to the hypercharge field in the covariant derivative ($1/6$, $2/3$, $-1/3$, $-1/2$, $-1$, $0$ for $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$, $1/2$ for $\Phi$).', 'dimensionless', '', 'STANDARD')
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
add('Jcur', r'J_f^\mu', ['J', r'J_{\ell}', r'J_{e}', r'J_{\nu}', r'J_{Q}', r'J_{u}', r'J_{d}'], r'The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the currents that are the sources of the gauge fields.', 'GeV$^3$', '', 'STANDARD')
add('jcur', r'j_X^\mu', ['j'], r'The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED).', 'GeV$^8$', '', 'DERIVED')


# ---------------------------------------------------------------- gravity: equations, sources
add('ip', r'p', ['index:p', 'p'], r'The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels).')
add('LovE', r'\mathcal{E}_{(p)}{}^M{}_N', [r'\mathcal{E}'], r'The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components.', '1/length$^{2p}$', '', 'STANDARD')
add('isigma', r'\sigma', ['index:\\sigma'], r'The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$.')
add('TPsi', r'\mathcal{T}_\Psi', [r'\mathcal{T}_{\Psi}'], r'The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$.', 'GeV$^8$', '', 'STANDARD')
add('Tbulk', r'\mathcal{T}_{\mathrm{bulk}}', [r'\mathcal{T}_{\mathrm{bulk}}'], r'The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components).', 'GeV$^8$', '', 'STANDARD')
add('Sfoldsrc', r'\mathcal{S}^a{}_b', [r'\mathcal{S}'], r'The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold).', 'GeV$^7$', r'$\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block', 'DERIVED')
add('Gfold7', r'\mathcal{G}_{\mathrm{F}}{}^a{}_b', [r'\mathcal{G}_{\mathrm{F}}'], r'The Einstein tensor of the seven-dimensional metric of the fold (FD-2), frame components along the fold.', '1/length$^2$', '', 'STANDARD')
add('Pigw', r'\Pi_{\mathrm{gw}}', [r'\Pi_{\mathrm{gw}}'], r'The transverse traceless stress of the matter of the fold that drives the gravitational wave $h_{\mathrm{gw}}$ (half the difference of its components along $x_1$ and $x_2$), integrated across the fold (eight-dimensional normalisation).', 'GeV$^7$', '', 'STANDARD')
add('qhold', r'q_{\mathrm{hold}}', [r'q_{\mathrm{hold}}'], r'The pressure along the extra times that the fold fluid adds to its tension to hold the volume of the extra times fixed (four-dimensional normalisation).', 'GeV$^4$', r'$-\Delta_{\mathrm{r}} = -0.793\,\rho_{\mathrm{c}}^{(0)}$ today', 'DERIVED (the value), ASSUMED (that the fold fluid supplies it)')
add('qtot', r'q_{\mathrm{tot}}', [r'q_{\mathrm{tot}}'], r'The total pressure along the extra times of the matter of the fold (the Standard Model, the bound states of dirac16complex, the portals and the fold fluid without its tension).', 'GeV$^4$', '', 'STANDARD')
add('rhoinf', r'\rho_{\mathrm{inf}}', [r'\rho_{\mathrm{inf}}'], r'The vacuum energy density that drives an inflation of the fold: the potential energy of a field of the fold (four-dimensional normalisation), with the pressure $-\rho_{\mathrm{inf}}$ along ordinary space and along the extra times.', 'GeV$^4$', '', 'ASSUMED')
add('pinf', r'p_{\mathrm{inf}}', [r'p_{\mathrm{inf}}'], r'The pressure along ordinary space of the vacuum energy that drives an inflation of the fold.', 'GeV$^4$', r'$-\rho_{\mathrm{inf}}$', 'STANDARD')
add('Xsec', r'\mathcal{X}^a{}_b', [r'\mathcal{X}'], r'The second-order static bulk operator around the static block: the term of second order in $\epsilon_{\mathrm{b}}$ of the bulk equations for static deformations of the metric (frame components; the first-order term vanishes identically).', 'GeV$^2$', '', 'DERIVED')
add('jumpab', r'j_{\mathfrak{a}},\ j_{\mathfrak{b}}', [r'j_{\mathfrak{a}}', r'j_{\mathfrak{b}}'], r"The jumps at the fold of the first $\sigma$-derivatives of the first-order deformations of the metric: $j_{\mathfrak{a}} = \mathfrak{a}_1'(0^+) - \mathfrak{a}_1'(0^-)$, $j_{\mathfrak{b}} = \mathfrak{b}_1'(0^+) - \mathfrak{b}_1'(0^-)$.", 'GeV', '', 'DERIVED')
add('varepsilon', r'\varepsilon', [r'\varepsilon'], r'The half-thickness of a layer around the fold, taken to zero.', 'length', '', 'STANDARD')
add('Fpot', r'\mathfrak{F}^a{}_b', [r'\mathfrak{F}'], r'The junction potential: a function of the first $\sigma$-derivatives of the metric functions whose derivatives are the coefficients of the second $\sigma$-derivatives in $\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FE-4).', 'GeV', '', 'DERIVED')
add('fwarp', r'\mathfrak{f}', [r'\mathfrak{f}'], r'Any one of the three metric functions $\mathfrak{a}, \mathfrak{b}, \mathfrak{n}$ of the general warped metric (FE-34).', 'dimensionless', '', 'DERIVED')
add('awarp', r'\mathfrak{a},\ \mathfrak{a}_1', [r'\mathfrak{a}', r'\mathfrak{a}_{1}'], r'The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term).', 'dimensionless', '', 'DERIVED')
add('bwarp', r'\mathfrak{b},\ \mathfrak{b}_1', [r'\mathfrak{b}', r'\mathfrak{b}_{1}'], r'The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term).', 'dimensionless', '', 'DERIVED')
add('nwarp', r'\mathfrak{n},\ \mathfrak{n}_1', [r'\mathfrak{n}', r'\mathfrak{n}_{1}'], r'The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term).', 'dimensionless', '', 'DERIVED')
add('TH', r'\mathcal{T}_{\mathrm{H}}', [r'\mathcal{T}_{\mathrm{H}}'], r'The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation).', 'GeV$^4$', '', 'STANDARD')
add('Tgauge', r'\mathcal{T}_{\mathrm{gauge}}', [r'\mathcal{T}_{\mathrm{gauge}}'], r'The energy-momentum tensor of the gauge fields.', 'GeV$^4$', '', 'STANDARD')
add('Tf', r'\mathcal{T}_{\mathrm{f}}', [r'\mathcal{T}_{\mathrm{f}}'], r'The energy-momentum tensor of the quarks and leptons.', 'GeV$^4$', '', 'STANDARD')
add('TP', r'\mathcal{T}_{\mathrm{P}}', [r'\mathcal{T}_{\mathrm{P}}'], r'The energy-momentum tensor of the portals of dirac16complex.', 'GeV$^4$', '', 'DERIVED')
add('TIG', r'\mathcal{T}_{\mathrm{IG}}', [r'\mathcal{T}_{\mathrm{IG}}'], r'The energy-momentum tensor of the induced Einstein-Hilbert term of the fold, $\mathcal{T}_{\mathrm{IG}}{}^\mu{}_\nu = -\hat G^\mu{}_\nu/\kappa_{\mathrm{ind}}$.', 'GeV$^4$', '', 'ESTIMATE')
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
add('Asf', r'\mathsf{A}', [r'\mathsf{A}'], r"The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$.", 'dimensionless', r"0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); 1 at the author's vacuum, which is not a solution with the corrected weights", '')
add('Usf', r'\mathsf{U}', [r'\mathsf{U}'], r"The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$.", 'dimensionless', r'$\mathsf{U} = \mathsf{A}$ with frozen extra times', '')
add('Vsf', r'\mathsf{V}', [r'\mathsf{V}'], r"The rate of change of the scale factor $\mathrm{e}^{-a_4}b_4$ of the extra times on the fold in units of $H$, $\mathsf{V} = \mathsf{U} - \mathsf{A}$; zero with frozen extra times.", 'dimensionless', '', '')
add('V1sf', r'\mathsf{V}_1', [r'\mathsf{V}_{1}'], r"The time derivative of $\mathsf{V}$ in units of $H$, $\mathsf{V}_1 = \mathsf{V}'/H$.", 'dimensionless', '', '')
add('A1sf', r'\mathsf{A}_1', [r'\mathsf{A}_{1}'], r"The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$.", 'dimensionless', '', '')
add('U1sf', r'\mathsf{U}_1', [r'\mathsf{U}_{1}'], r"The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$.", 'dimensionless', '', 'DERIVED')
add('Gfac', r'\mathcal{G}', [r'\mathcal{G}'], r"The factor of the $(\sigma, x_4)$ bulk equation of the author's metric with the author's original weights, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$.", 'dimensionless', '', 'DERIVED')
add('rhobulk', r'\rho_{\mathrm{bulk}}', [r'\rho_{\mathrm{bulk}}'], r'The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$.', 'GeV$^8$', '', 'DERIVED')
add('is', 's', ['index:s'], r'A second extra-time direction of the fold (as $r$, different from it).')
add('inn', 'n', ['index:n'], r'The order $n = 1, 2, \dots$ of a term of the power series of the metric (also its exponent of $\epsilon_{\mathrm{r}}$); $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{n}_n$ are the terms of order $n$.')
add('epsb', r'\epsilon_{\mathrm{b}}', [r'\epsilon_{\mathrm{b}}'], r'The bookkeeping parameter of the deformations of the metric along $\sigma$ that sources depending on $\sigma$ require (their amplitude relative to the order-0 metric of the author).', 'dimensionless', '', '')
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
add('muX', r'\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}', [r'\mu_{X}', r'\mu_{\mathrm{L}}', r'\mu_{\mathrm{R}}'], r'The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract.', 'dimensionless', '', 'DERIVED')
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
add('QPsi', r'Q_\Psi', [r'Q_{\Psi}'], r'The conserved charge of dirac16complex (the Noether charge of a change of the phase of $\Psi$ by a constant), a Krein form (indefinite); as written it is the charge per unit coordinate volume of the extra times, on which no field depends.', r'GeV$^3$', '', 'DERIVED')
add('Bkrein', r'\mathfrak{B}', [r'\mathfrak{B}'], r'The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density.', 'dimensionless', '', 'DERIVED')
add('Qorb', r'\mathcal{Q}_o', [r'\mathcal{Q}'], r'The charge $Q_\Psi$ (the Krein charge) of the single-particle state $o$ of dirac16complex, a Kohn-Sham orbital or a mode: $+1$ or $-1$ for a normalised state.', 'dimensionless', '', 'DERIVED')
# the Kohn-Sham states of the gas of bound particles (SOLUTION, ANALYSIS); no meaning cites an equation tag
add('chiKS', r'\chi_o(\sigma),\ \bar\chi_o', [r'\chi_{o}', r'\bar{\chi}_{o}', r'\chi_{p}', r'\chi_{1}'], r'The profile of the occupied Kohn-Sham orbital $o$ ($o = 1, \dots, 4$, the four positive-energy states of the bound level) of a homogeneous gas of the particles $\chi$ at rest on the static block: a 16-component spinor function of $\sigma$; the orbital of each particle is $\mathrm{e}^{3H\lvert\sigma\rvert}\chi_o(\sigma)\mathrm{e}^{-\mathrm{i}\omega x_4}$ divided by the square root of the volume of ordinary space and of $V_*$; normalised to the Krein charge $-1$, $\int\mathrm{d}\sigma\,\chi_o^\dagger\mathfrak{B}\chi_o = -1$; $\bar\chi_o = \chi_o^\dagger\sigma_{16}$ is its Dirac adjoint.', r'GeV$^{1/2}$', '', 'DERIVED')
add('GKS', r'G_{\mathrm{KS}}', [r'G_{\mathrm{KS}}'], r'The dimensionless strength of the self-interaction of the gas of particles $\chi$ in the Kohn-Sham states: the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold divided by the volume $V_*$ of the extra times, $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ (in units of $m_\Psi$ when numbers are given).', 'dimensionless', r'$10^{-6}$ to 1 in the solutions', 'DERIVED')
add('Mmean', r'\mathcal{M}(\sigma)', [r'\mathcal{M}'], r'The mean field of the self-interaction in the Kohn-Sham equation of the gas: the $16 \times 16$ matrix $\lambda_\Psi(n_{\mathrm{s}}\mathbf{1} - \mathcal{N})$ at each $\sigma$, which adds to the mass $m_\Psi$; positive (repulsive) for $\lambda_\Psi > 0$.', 'GeV', '', 'DERIVED')
add('Minf', r'\mathcal{M}_\infty', [r'\mathcal{M}_{\infty}'], r'The limit of the mean field far from the fold where the proper density of the gas has saturated: the matrix for which the local equation has a solution decaying exactly at the rate $3H$.', 'GeV', '', 'DERIVED')
add('rhohat', r'\hat\rho(\sigma)', [r'\hat{\rho}'], r'The scalar density of the occupied orbitals, $\hat\rho = \frac14\sum_o\bar\chi_o\chi_o$ (per particle); the scalar density of the gas is $n_{\mathrm{s}} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat\rho$.', 'GeV', '', 'DERIVED')
add('rhohatinf', r'\hat\rho_\infty', [r'\hat{\rho}_{\infty}'], r'The constant that the proper scalar density $\mathrm{e}^{6H\lvert\sigma\rvert}\hat\rho$ approaches far from the fold where it saturates.', 'GeV', '', 'DERIVED')
add('rhohatL', r'\hat\rho_{\mathrm{L}}', [r'\hat{\rho}_{\mathrm{L}}'], r'The scalar density of the left-handed half of the occupied orbitals, $\hat\rho_{\mathrm{L}} = \frac14\sum_o\bar\chi_oP_{\mathrm{L}}\chi_o$; at the fold the mean of its values on the two sides.', 'GeV', '', 'DERIVED')
add('rhohatL0', r'\hat\rho_{\mathrm{L}0}', [r'\hat{\rho}_{\mathrm{L}0}'], r'The left-handed scalar density $\hat\rho_{\mathrm{L}}$ of the bound state without the self-interaction and without the Higgs feedback.', 'GeV', '', 'DERIVED')
add('Nhat', r'\hat{\mathcal{N}}(\sigma)', [r'\hat{\mathcal{N}}'], r'The one-body density matrix of the occupied orbitals, $\hat{\mathcal{N}} = \frac14\sum_o\chi_o\bar\chi_o$ (a $16 \times 16$ matrix at each $\sigma$, per particle); the density matrix of the gas is $\mathcal{N} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat{\mathcal{N}}$.', 'GeV', '', 'DERIVED')
add('Eint', r'\mathsf{E}_{\mathrm{int}}', [r'\mathsf{E}_{\mathrm{int}}'], r'The interaction energy per particle of the gas of $\chi$: the mean self-interaction energy $\frac{\lambda_\Psi}{2}(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2)$ integrated across the hidden direction, per particle.', 'GeV', '', 'DERIVED')
add('epsp', r'\epsilon_{\mathrm{p}}', [r'\epsilon_{\mathrm{p}}'], r'The energy per particle of the gas of $\chi$: the orbital energy minus the interaction energy per particle, which the orbital energy counts twice.', 'GeV', '', 'DERIVED')
add('wchi', r'w_\chi', [r'w_{\chi}'], r'The equation of state of the gas of the particles $\chi$: its pressure divided by its energy density, $w_\chi = P_{\mathrm{KS}}/(n_\chi\epsilon_{\mathrm{p}})$ (0 for cold dark matter, $-1$ for a vacuum energy).', 'dimensionless', '', 'DERIVED')
add('PKS', r'P_{\mathrm{KS}}', [r'P_{\mathrm{KS}}'], r'The pressure of the gas of $\chi$ along ordinary space in the Kohn-Sham state: the particles are at rest, so it is the mean self-interaction, $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$.', 'GeV$^4$', '', 'DERIVED')
add('muL0', r'\mu_{\mathrm{L}0}', [r'\mu_{\mathrm{L}0}'], r'The strength $\mu_{\mathrm{L}}$ of the fold for the left-handed half without the feedback of the gas on the Higgs field.', 'dimensionless', '$-0.6$ in the solutions', 'DERIVED')
add('kappaH', r'\kappa_{\mathrm{H}}', [r'\kappa_{\mathrm{H}}'], r'The strength of the Higgs-portal loop of the gas: the gas without the feedback changes the local $v_{\mathrm{loc}}^2$ at the fold by the factor $1 - \kappa_{\mathrm{H}}$, $\kappa_{\mathrm{H}} = c_\Phi n_\chi\hat\rho_{\mathrm{L}0}(0)/(\lambda v^2V_*)$; negative where the Higgs portal binds the fold ($c_\Phi < 0$, $\hat\rho_{\mathrm{L}0}(0) > 0$): the gas raises $v_{\mathrm{loc}}^2$.', 'dimensionless', '$-0.3$ in the test of the loop', 'ASSUMED (the value), DERIVED (the sign)')
add('Delta', r'\Delta', [r'\Delta'], r'A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species).', '', '', 'STANDARD')

# ---------------------------------------------------------------- Standard Model on the fold
add('geff', r'g_{k,\mathrm{eff}}', [r'g_{1,\mathrm{eff}}', r'g_{2,\mathrm{eff}}', r'g_{3,\mathrm{eff}}'], r'The effective (canonically normalised) gauge couplings of the fold when the fold factor is $\mathcal{Z}$, $g_{k,\mathrm{eff}} = g_k/\sqrt{\mathcal{Z}}$ ($k = 1, 2, 3$).', 'dimensionless', '', 'DERIVED')
add('lameff', r'\lambda_{\mathrm{eff}}', [r'\lambda_{\mathrm{eff}}'], r'The effective quartic Higgs coupling, $\lambda/\mathcal{Z}$.', 'dimensionless', '', 'DERIVED')
add('Yeff', r'\mathcal{Y}_{\mathrm{eff}}', [r'\mathcal{Y}_{\mathrm{eff}}'], r'The effective Yukawa matrices, $\mathcal{Y}/\sqrt{\mathcal{Z}}$ (for each of $\mathcal{Y}^{u}, \mathcal{Y}^{d}, \mathcal{Y}^{e}, \mathcal{Y}^{\nu}$).', 'dimensionless', '', 'DERIVED')
add('GNeff', r'G_{\mathrm{N,eff}}', [r'G_{\mathrm{N,eff}}'], r'The effective Newton constant of the fold, $G_{\mathrm{N}}/\mathcal{Z}$.', 'GeV$^{-2}$', '', 'DERIVED')
add('GN', r'G_{\mathrm{N}}', [r'G_{\mathrm{N}}'], r'Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV.', 'GeV$^{-2}$', r'$6.708\times10^{-39}$ GeV$^{-2}$', 'STANDARD')
add('mW', r'm_{\mathrm{W}}', [r'm_{\mathrm{W}}'], r'The mass of the $W$ bosons.', 'GeV', '80.37 GeV ($\\mathcal{A} = 0$)', 'STANDARD')
add('mZ', r'm_{\mathrm{Z}}', [r'm_{\mathrm{Z}}'], r'The mass of the $Z$ boson.', 'GeV', '91.19 GeV ($\\mathcal{A} = 0$)', 'STANDARD')
add('GF', r'G_{\mathrm{F}}', [r'G_{\mathrm{F}}'], r'The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in FE-45 the Fermi constant of the ad hoc vacuum, which is $G_{\mathrm{F,loc}}$ of FE-49.', 'GeV$^{-2}$', r'$1.1664\times10^{-5}$ GeV$^{-2}$', 'STANDARD')
add('mh', r'm_h', [r'm_{h}'], r'The mass of the Higgs boson.', 'GeV', '125.25 GeV (Particle Data Group 2022)', 'STANDARD')
add('Aphoton', r'A_\mu', ['A'], r'The photon field: the massless combination of $W^1, W^2, W^3$ and $B$ (canonically normalised).', 'GeV', '', 'STANDARD')
add('nI', r'n^I', [r'n^{I}'], r'The unit isovector of the ad hoc vacuum, $n = (2\mathcal{A}v, 0, \mathcal{A}^2 - v^2)/(\mathcal{A}^2 + v^2)$, which fixes which combination of $W^1, W^2, W^3$ joins $B$ in the photon.', 'dimensionless', r'$(0, 0, -1)$ for $\mathcal{A} = 0$', 'DERIVED')
add('Umix', r'U_{f\mathrm{L}},\ U_{f\mathrm{R}}', [r'U_{u\mathrm{L}}', r'U_{u\mathrm{R}}', r'U_{d\mathrm{L}}', r'U_{d\mathrm{R}}', r'U_{e\mathrm{L}}', r'U_{e\mathrm{R}}', r'U_{\nu \mathrm{L}}', r'U_{\nu \mathrm{R}}'], r'The unitary $3 \times 3$ matrices that diagonalise the mass matrices of the up quarks, the down quarks, the charged leptons and the neutrinos (left-handed and right-handed rotations).', 'dimensionless', '', 'STANDARD')
add('mferm', r'm_u, \dots, m_3', [r'm_{u}', r'm_{c}', r'm_{t}', r'm_{d}', r'm_{s}', r'm_{b}', r'm_{e}', r'm_{\mu}', r'm_{\tau}', r'm_{1}', r'm_{2}', r'm_{3}'], r'The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses).', 'GeV', r'measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-3 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 23 meV by DESI DR2 with the CMB and NuFIT 6.0', 'STANDARD')
add('Ckm', r'V_{\mathrm{CKM}}', [r'V_{\mathrm{CKM}}'], r'The quark mixing matrix (Cabibbo-Kobayashi-Maskawa).', 'dimensionless', '', 'STANDARD')
add('Pmns', r'U_{\mathrm{PMNS}}', [r'U_{\mathrm{PMNS}}'], r'The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; $U_{\alpha i}$ are its entries.', 'dimensionless', r'$\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$)', 'STANDARD, ASSUMED (the phase)')
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
add('tauc', r'\tau_{\mathrm{c}}', [r'\tau_{\mathrm{c}}'], r'The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{e}^{-a_4}\mathrm{d}x_4$ (the time divided by the scale factor $\mathrm{e}^{a_4}$ of the fold); a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$.', 'length (= time)', '', 'STANDARD')
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
add('H4', r'H_4', [r'H_{4}'], r"The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant.", 'GeV (1/time)', r'$H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV', 'STANDARD')
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
add('Omeganu', r'\Omega_\nu,\ \Omega_\nu^{(i)}', [r'\Omega_{\nu}'], r'The density parameter of the neutrinos of the CNB: $\Omega_\nu$ that of the massive states today; $\Omega_\nu^{(i)}(\mathsf{z})$ the energy density of the mass state $i$ at the redshift $\mathsf{z}$ in units of the critical density today.', 'dimensionless', '', 'STANDARD')
add('h100', r'h_{100}', [r'h_{100}'], r'The present expansion rate of the fold in units of 100 km/s/Mpc.', 'dimensionless', '0.674 (Planck 2018)', 'STANDARD')
add('rhoc', r'\rho_{\mathrm{c}}', [r'\rho_{\mathrm{c}}'], r'The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today.', 'GeV$^4$', r'$\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$', 'STANDARD')
add('rhoL', r'\rho_\Lambda', [r'\rho_{\Lambda}'], r'The vacuum energy density of the fold above its static tension, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}$.', 'GeV$^4$', r'$0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018)', 'DERIVED')
add('rhovac', r'\rho_{\mathrm{vac}}', [r'\rho_{\mathrm{vac}}'], r'The vacuum energy of the fields of the fold: the minimum of their potential (for the Standard Model the minimum of the Higgs potential with its loop corrections), a tension of the seven-dimensional fold.', 'GeV$^4$', '', 'STANDARD')

# ---------------------------------------------------------------- thermal history
add('TSM', r'\mathcal{T}_{\mathrm{SM}}', [r'\mathcal{T}_{\mathrm{SM}}'], r'The energy-momentum tensor of the Standard Model on the fold, $\mathcal{T}_{\mathrm{H}} + \mathcal{T}_{\mathrm{gauge}} + \mathcal{T}_{\mathrm{f}}$.', 'GeV$^4$', '', 'STANDARD')
add('Jgeo', r'\mathcal{J}^a{}_b', [r'\mathcal{J}'], r'The jump of the junction potential across the fold computed from the metric: the geometric side of the junction condition $\mathcal{J} = \kappa\mathcal{S}$, which equates it to $\kappa$ times the energy-momentum tensor $\mathcal{S}$ of everything on the fold.', 'GeV', '', 'DERIVED')
add('rhoSM', r'\rho_{\mathrm{SM}}', [r'\rho_{\mathrm{SM}}'], r'The energy density of the Standard-Model particles.', 'GeV$^4$', '', 'STANDARD')
add('grho', r'g_\rho', [r'g_{\rho}'], r'The effective number of relativistic degrees of freedom of the energy density.', 'dimensionless', '106.75 in the Standard Model above the electroweak scale', 'STANDARD')
add('gs', r'g_{\mathrm{s}}', [r'g_{\mathrm{s}}'], r'The effective number of relativistic degrees of freedom of the entropy density.', 'dimensionless', '3.909 today', 'STANDARD')
add('Ttemp', r'\mathsf{T}', [r'\mathsf{T}'], r'The temperature of the Standard-Model plasma (of the photons after the annihilation of electrons and positrons).', 'GeV', '', 'STANDARD')
add('sent', r's', ['s'], r'The entropy density of the Standard-Model plasma.', 'GeV$^3$', '', 'STANDARD')
add('MPl', r'M_{\mathrm{Pl}}', [r'M_{\mathrm{Pl}}'], r'The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$.', 'GeV', r'$1.221\times10^{19}$ GeV', 'STANDARD')
add('nchi', r'n_\chi', [r'n_{\chi}'], r'The number density of the dark-matter particles $\chi$ (particles plus antiparticles).', 'GeV$^3$', '', 'DERIVED')
add('nchieq', r'n_{\chi,\mathrm{eq}}', [r'n_{\chi ,\mathrm{eq}}'], r'The number density of $\chi$ in thermal equilibrium with the plasma (non-relativistic).', 'GeV$^3$', '', 'STANDARD')
add('gchi', r'g_\chi', [r'g_{\chi}'], r'The number of internal states of the bound level of $\chi$ that are in thermal equilibrium.', 'dimensionless', '', 'DERIVED')
add('sigmaann', r'\sigma_{\mathrm{ann}}', [r'\sigma_{\mathrm{ann}}'], r'The annihilation cross-section of the particles $\chi$ into Standard-Model particles (through the portals) in the normalisation of FE-61, where $n_\chi$ counts the four particle and the four antiparticle states of the bound level: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is a quarter of the annihilation rate $(\sigma\mathsf{v})_{\chi\bar\chi}$ of one particle $\chi_a$ with one antiparticle $\bar\chi_a$.', 'GeV$^{-2}$', '', 'DERIVED')
add('vrel', r'\mathsf{v}', [r'\mathsf{v}'], r'The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product.', 'dimensionless', '', 'STANDARD')
add('xf', r'x_{\mathrm{f}}', [r'x_{\mathrm{f}}'], r'The ratio of the mass of $\chi$ to the temperature at which its annihilations stop (freeze-out).', 'dimensionless', r'23 to 30 (for $\omega_{\mathrm{b}}$ = 10 GeV to 10 TeV)', 'STANDARD')
add('gstar', r'g_*', [r'g_{*}'], r'The effective number of relativistic degrees of freedom at the freeze-out ($g_\rho$ there).', 'dimensionless', '', 'STANDARD')
add('rhonuR', r'\rho_{\nu_{\mathrm{R}}}', [r'\rho_{\nu _{\mathrm{R}}}'], r'The energy density of the three right-handed neutrinos.', 'GeV$^4$', '', 'STANDARD')
add('CnuR', r'\mathcal{C}_{\nu_{\mathrm{R}}}', [r'\mathcal{C}_{\nu _{\mathrm{R}}}'], r'The collision term of the right-handed neutrinos: the rate at which collisions produce (or remove) their energy density.', 'GeV$^5$', '', 'STANDARD')
add('Tdec', r'\mathsf{T}_{\mathrm{dec}}', [r'\mathsf{T}_{\mathrm{dec}}'], r'The temperature at which the right-handed neutrinos decouple from the plasma.', 'GeV', '', 'STANDARD')

add('qSM', r'q_{\mathrm{SM}}', [r'q_{\mathrm{SM}}'], r'The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times).', 'GeV$^4$', '', 'DERIVED')
add('qchi', r'q_\chi', [r'q_{\chi}'], r'The pressure of the bound states of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas).', 'GeV$^4$', '', 'DERIVED')
add('qP', r'q_{\mathrm{P}}', [r'q_{\mathrm{P}}'], r'The pressure of the portals along the extra times: their mean on-shell Lagrangian density.', 'GeV$^4$', '', 'DERIVED')

# ---------------------------------------------------------------- SOLUTION: background, power series, Higgs vacuum, spectra
add('Deltar', r'\Delta_{\mathrm{r}}', [r'\Delta_{\mathrm{r}}'], r'The mismatch of the radion condition: the sum over the matter of the fold of its pressure along the extra times and $(\rho - 3\mathcal{P})/2$ (zero for radiation).', 'GeV$^4$', r'$0.793\,\rho_{\mathrm{c}}^{(0)}$ today', 'DERIVED')
add('Orot', r'\mathcal{O}(\phi_{\mathrm{rot}})', [r'\mathcal{O}'], r'The $2 \times 2$ isospin rotation by the angle $\phi_{\mathrm{rot}}$ about the second isospin axis (a real element of $SU(2)$).', 'dimensionless', '', 'DERIVED')
add('phirot', r'\phi_{\mathrm{rot}}', [r'\phi_{\mathrm{rot}}'], r'The angle of the isospin rotation that turns $(0, V_{\mathrm{rad}})/\sqrt2$ into the ad hoc vacuum: $\tan(\phi_{\mathrm{rot}}/2) = \mathcal{A}/v$.', 'dimensionless', '', 'DERIVED')
add('Vrad', r'V_{\mathrm{rad}}', [r'V_{\mathrm{rad}}'], r'The modulus of the Higgs doublet in the ad hoc vacuum, $V_{\mathrm{rad}} = \sqrt{v^2 + \mathcal{A}^2}$ ($V_{\mathrm{rad}}^2 = 2\Phi^\dagger\Phi$).', 'GeV', '', 'DERIVED')
add('Rrad', r'\mathcal{R}_{\mathrm{rad}}', [r'\mathcal{R}_{\mathrm{rad}}'], r'The radial residual of the Higgs equation FE-15 in the ad hoc vacuum written as a gauge rotation (S-10): the amount by which $V_{\mathrm{rad}}$ fails to solve the radial equation; zero for a solution.', 'GeV$^3$', '', 'DERIVED')
add('us', r'u_{\mathrm{s}}', [r'u_{\mathrm{s}}'], r'The rescaled profile of a massless scalar field of the bulk at zero momentum along ordinary space: the field is $\mathrm{e}^{3H\lvert\sigma\rvert}u_{\mathrm{s}}(\sigma)\,\mathrm{e}^{-\mathrm{i}\omega x_4}$.', 'as the field', '', 'DERIVED')
add('csc', r'c_{\mathrm{sc}}', [r'c_{\mathrm{sc}}'], r'The limiting speed of the zero mode of a scalar field of the bulk along ordinary space, in units of the speed of light on the fold.', 'dimensionless', r'$\sqrt{3/2}$', 'DERIVED')
add('cgauge', r'c_{\mathrm{gauge}}', [r'c_{\mathrm{gauge}}'], r'The limiting speed of the zero mode of a gauge field (a photon) of the bulk, in units of the speed of light on the fold.', 'dimensionless', r'$\sqrt2$', 'DERIVED')
add('cfer', r'c_{\mathrm{fer}}', [r'c_{\mathrm{fer}}'], r'The limiting speed of the zero mode of a fermion of the bulk with the kink mass $M_{\mathrm{k}}\,\mathrm{sgn}(\sigma)$, in units of the speed of light on the fold.', 'dimensionless', '', 'DERIVED')
add('cgrav', r'c_{\mathrm{g}}', [r'c_{\mathrm{g}}'], r'The speed of gravitational waves on the fold, in units of the speed of light.', 'dimensionless', r"1 at every wavelength with the corrected weights; with the author's original weights the long-wavelength mode had $c_{\mathrm{g}}^2 = 83/82$ and shorter waves were slower than light", 'DERIVED')
add('Mkink', r'M_{\mathrm{k}}', [r'M_{\mathrm{k}}'], r'The mass of a fermion of the bulk that changes sign at the fold (a kink mass $M_{\mathrm{k}}\,\mathrm{sgn}(\sigma)$), used to illustrate the speeds of bulk fermions.', 'GeV', '', 'ASSUMED')
add('cb', r'c_{\mathrm{b}}', [r'c_{\mathrm{b}}'], r'The speed coefficient of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum their energy is $\omega^2 = \omega_{\mathrm{b}}^2 + c_{\mathrm{b}}^2\vec k^2$ (it is not a speed that the particles reach: at large momenta $\omega/\lvert\vec k\rvert$ tends to 1, the speed of light).', 'dimensionless', '', 'DERIVED')
# ---------------------------------------------------------------- SOLUTION: neutrino flavours
add('H2flav', r'\mathsf{H}_{2}', [r'\mathsf{H}_{2}'], r'The two-flavour Hamiltonian of the electron neutrinos in the Sun (the mass states 1 and 2 with the potential $\cos^2\theta_{13}V_{\mathrm{CC}}$; the third state decouples).', 'GeV (or 1/km)', '', 'STANDARD')
add('thetaij', r'\theta_{12},\ \theta_{13},\ \theta_{23}', [r'\theta_{12}', r'\theta_{13}', r'\theta_{23}'], r'The three mixing angles of $U_{\mathrm{PMNS}}$ (its fourth parameter is the Dirac phase, which does not enter the electron-flavour results of UM-3).', 'dimensionless', r'$33.40^\circ$, $8.54^\circ$, $49.14^\circ$ in the computations of UM-3 ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$: NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); $33.71^\circ$, $8.56^\circ$, $43.28^\circ$ in NuFIT 6.0 (2024, with the Super-Kamiokande atmospheric data; $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$)', 'STANDARD')
add('NA', r'N_{\mathrm{A}}', [r'N_{\mathrm{A}}'], r"Avogadro's number: $245N_{\mathrm{A}}$ cm$^{-3}$ is 245 moles of electrons per cubic centimetre.", 'per mole', r'$6.02214076\times10^{23}$', 'STANDARD')
add('Rsun', r'R_\odot', [r'R_{\odot}'], r'The radius of the Sun.', 'length', r'$6.957\times10^5$ km', 'STANDARD')
add('Pee', r'\mathsf{P}_{\mathrm{ee}}', [r'\mathsf{P}_{\mathrm{ee}}'], r'The survival probability of electron neutrinos: the probability that an electron neutrino is detected as an electron neutrino.', 'dimensionless', '', 'DERIVED')
add('P2', r'\mathsf{P}_{2}', [r'\mathsf{P}_{2}'], r'The survival probability of the two-flavour problem of the mass states 1 and 2 (S-20).', 'dimensionless', '', 'DERIVED')
add('Pc', r'\mathsf{P}_{\mathrm{c}}', [r'\mathsf{P}_{\mathrm{c}}'], r'The crossing probability: the probability that a neutrino jumps from one eigenstate of matter to the other on its way through the Sun (exact for an exponential profile, Petcov).', 'dimensionless', '', 'STANDARD')
add('rprod', r'r_{\mathrm{p}}', [r'r_{\mathrm{p}}'], r'The radius at which the solar neutrinos of a given reaction are produced.', 'length', r'$0.05R_\odot$ to $0.10R_\odot$', 'STANDARD')
add('rsunscale', r'r_\odot', [r'r_{\odot}'], r'The scale height of the electron density of the Sun, $r_\odot = R_\odot/10.54$.', 'length', r'$6.6\times10^4$ km', 'STANDARD')
add('Ye', r'Y_{\mathrm{e}}', [r'Y_{\mathrm{e}}'], r'The electron fraction of stellar matter: the number of electrons per nucleon.', 'dimensionless', '0.5 in the envelope', 'STANDARD')
add('mamu', r'm_{\mathrm{u}}', [r'm_{\mathrm{u}}'], r'The atomic mass unit, the mass per nucleon of stellar matter to within one per cent: $n_e = Y_e\rho/m_{\mathrm{u}}$.', 'g', r'$1.66054\times10^{-24}$ g', 'STANDARD')
add('gammaLZ', r'\gamma_{\mathrm{LZ}}', [r'\gamma_{\mathrm{LZ}}'], r'The adiabaticity parameter of a resonance: the jump probability of FE-50 is $\exp(-\pi\gamma_{\mathrm{LZ}}/2)$; $\gamma_{\mathrm{LZ}} \gg 1$ is adiabatic.', 'dimensionless', '', 'STANDARD')
add('rres', r'r_{\mathrm{res}}', [r'r_{\mathrm{res}}'], r'The radius of a resonance: where the electron density equals $n_{e,\mathrm{res}}$ of FE-50 ($r_{\mathrm{H}}$ for $\Delta m^2_{31}$, $r_{\mathrm{L}}$ for $\Delta m^2_{21}$).', 'length', '', 'STANDARD')
add('Kr', r'K_{\mathrm{r}}', [r'K_{\mathrm{r}}'], r'The wave number of a flavour wave along the radial direction (the radial component of $\vec K$).', 'GeV (1/length)', '', 'STANDARD')
add('ucos', r'\mathsf{u}', [r'\mathsf{u}'], r'The cosine of the angle between the direction of motion of a neutrino and the radial direction ($\mathsf{u}_e$, $\mathsf{u}_{\bar e}$ the edges of the emission cones of the electron neutrinos and antineutrinos).', 'dimensionless', '', 'STANDARD')
add('Qflav', r'\mathsf{Q}(\mathsf{u})', [r'\mathsf{Q}'], r'The amplitude of a small flavour coherence (the off-diagonal entry of $\varrho$) of the neutrinos moving with the direction cosine $\mathsf{u}$, in a flavour wave.', 'dimensionless', '', 'STANDARD')
add('Qheat', r'\dot Q_{\mathrm{heat}}', [r'\dot{Q}_{\mathrm{heat}}'], r'The rate at which the absorption of electron neutrinos and antineutrinos heats the matter of the gain region (energy per time and mass).', 'energy per time and mass', '', 'STANDARD')
add('Lspec', r'L_{\mathrm{s}}', [r'L_{\mathrm{s}}'], r'The luminosity (energy per time) of one neutrino species leaving the neutrinosphere.', 'erg/s', r'$(2$ to $5)\times10^{52}$ erg/s', 'STANDARD')
add('Espec', r'E_{\mathrm{s}}', [r'E_{\mathrm{s}}'], r'The mean energy of one neutrino species.', 'GeV (MeV)', '10 to 16 MeV', 'STANDARD')
add('alphas', r'\alpha_{\mathrm{s}}', [r'\alpha_{\mathrm{s}}'], r'The shape (pinching) parameter of a neutrino spectrum (Keil, Raffelt and Janka).', 'dimensionless', '3', 'STANDARD')
# ---------------------------------------------------------------- SOLUTION: thermal history
add('Yield', r'\mathsf{Y}', [r'\mathsf{Y}'], r'The yield of the particles $\chi$: their number density divided by the entropy density, $\mathsf{Y} = n_\chi/s$ (constant when they neither annihilate nor are produced).', 'dimensionless', '', 'STANDARD')
add('Yieldeq', r'\mathsf{Y}_{\mathrm{eq}}', [r'\mathsf{Y}_{\mathrm{eq}}'], r'The yield of $\chi$ in thermal equilibrium, $n_{\chi,\mathrm{eq}}/s$.', 'dimensionless', '', 'STANDARD')
add('xmass', r'\mathsf{x}', [r'\mathsf{x}'], r'The ratio of the mass of $\chi$ to the temperature, $\mathsf{x} = \omega_{\mathrm{b}}/\mathsf{T}$ (the time variable of the freeze-out).', 'dimensionless', '', 'STANDARD')
add('Kbessel', r'K_2', [r'K_{2}'], r'The modified Bessel function of the second kind of order 2 ($K_2(y) \approx \sqrt{\pi/(2y)}\,\mathrm{e}^{-y}$ for large $y$).', 'dimensionless', '', 'STANDARD')
add('sigmapair', r'\sigma_{\mathrm{pair}}', [r'\sigma_{\mathrm{pair}}'], r'The cross-section of the annihilation of one particle $\chi_a$ with one antiparticle $\bar\chi_a$ of the same species, summed over the final states; $\sigma_{\mathrm{pair}}\mathsf{v}$ its product with the relative velocity (a constant for s-wave annihilation).', 'GeV$^{-2}$', '', 'DERIVED')
add('sigmaSI', r'\sigma_{\mathrm{SI}}', [r'\sigma_{\mathrm{SI}}'], r'The spin-independent cross-section of the scattering of $\chi$ on a nucleon (normalised per nucleon, as the direct-detection limits are quoted).', 'GeV$^{-2}$ (cm$^2$)', '', 'ESTIMATE')
add('mured', r'\mu_{\mathrm{red}}', [r'\mu_{\mathrm{red}}'], r'The reduced mass of $\chi$ and a nucleon, $\omega_{\mathrm{b}}m_{\mathrm{N}}/(\omega_{\mathrm{b}} + m_{\mathrm{N}})$.', 'GeV', '', 'STANDARD')
add('fN', r'f_{\mathrm{N}}', [r'f_{\mathrm{N}}'], r'The effective coupling of $\chi$ to a nucleon in the coherent scattering (a vector or scalar contact interaction).', 'GeV$^{-2}$', '', 'ESTIMATE')
add('gportql', r'\mathfrak{g}_{\mathrm{q}},\ \mathfrak{g}_{\mathrm{l}},\ \mathfrak{g}_{\mathrm{p}}', [r'\mathfrak{g}_{\mathrm{q}}', r'\mathfrak{g}_{\mathrm{l}}', r'\mathfrak{g}_{\mathrm{p}}'], r'The current-portal couplings $\mathfrak{g}_f$ of FE-47 taken equal for all chiral quark states ($\mathfrak{g}_{\mathrm{q}}$) or for the nine chiral lepton states that take part, the six of the lepton doublets and the three right-handed charged leptons ($\mathfrak{g}_{\mathrm{l}}$), and the coupling to the proton that the lepton loop induces ($\mathfrak{g}_{\mathrm{p}}$).', 'GeV$^{-2}$', '', 'ESTIMATE')
add('alphaem', r'\alpha_{\mathrm{em}}', [r'\alpha_{\mathrm{em}}'], r'The fine-structure constant.', 'dimensionless', '1/137.036', 'STANDARD')
add('qtransfer', r'q_{\mathrm{t}}', [r'q_{\mathrm{t}}'], r'The momentum transfer of the scattering of $\chi$ on a xenon nucleus in a detector.', 'GeV', '0.05 GeV', 'STANDARD')
add('mN', r'm_{\mathrm{N}}', [r'm_{\mathrm{N}}'], r'The mass of a nucleon.', 'GeV', '0.939 GeV', 'STANDARD')
add('fH', r'f_{\mathrm{H}}', [r'f_{\mathrm{H}}'], r'The nucleon matrix element of the Higgs coupling: the fraction of the nucleon mass carried by the quark masses and, through the trace anomaly, by the gluons.', 'dimensionless', '0.30', 'STANDARD')
add('nnuReq', r'n_{\nu_{\mathrm{R}},\mathrm{eq}}', [r'n_{\nu _{\mathrm{R}},\mathrm{eq}}'], r'The number density of the three right-handed neutrinos and their antiparticles in thermal equilibrium at the temperature $\mathsf{T}$.', 'GeV$^3$', '', 'STANDARD')
# ---------------------------------------------------------------- SOLUTION: CMB, CNB, BAO
add('Omegagamma', r'\Omega_\gamma', [r'\Omega_{\gamma}'], r'The density parameter of the photons today.', 'dimensionless', r'$5.450\times10^{-5}$ (for $h_{100} = 0.6736$)', 'STANDARD')
add('Tnueff', r'\mathsf{T}_{\nu,\mathrm{eff}}', [r'\mathsf{T}_{\nu ,\mathrm{eff}}'], r'The effective temperature of the neutrinos that carries $N_{\mathrm{eff}}$ (the convention of CAMB).', 'GeV (or K)', '', 'STANDARD')
add('Ifd', r'\mathsf{I}(y)', [r'\mathsf{I}'], r'The Fermi-Dirac energy integral of a neutrino state with the mass-to-temperature ratio $y$; $\mathsf{I}(0) = 7\pi^4/120$.', 'dimensionless', '', 'STANDARD')
add('yarg', r'y', ['y'], r'The ratio of the mass of a neutrino state to its temperature, the argument of $\mathsf{I}$.', 'dimensionless', '', 'STANDARD')
add('chisq', r'\chi_{\mathrm{fit}}^2', [r'\chi_{\mathrm{fit}}'], r'The chi-square of a comparison of a model with data (written $\chi^2$ in the text): the squared deviations weighted with the inverse covariance.', 'dimensionless', '', 'STANDARD')
add('Xvec', r'\mathsf{X}_{\mathrm{model}},\ \mathsf{X}_{\mathrm{data}}', [r'\mathsf{X}_{\mathrm{model}}', r'\mathsf{X}_{\mathrm{data}}'], r'The vectors of the model values and of the measured values of a data set (binned CMB spectra, BAO distances).', 'as the data', '', 'STANDARD')
add('Cmat', r'\mathsf{C}', [r'\mathsf{C}'], r'The covariance matrix of the measured values; $\mathsf{C}^{-1}$ its inverse.', 'as the data squared', '', 'STANDARD')
add('Xbin', r'\mathsf{X}_b', [r'\mathsf{X}'], r'A model value of the binned CMB spectrum, for the bin $b$ of the plik-lite binning.', r'$\mu$K$^2$', '', 'STANDARD')
add('wbin', r'\mathsf{w}_l', [r'\mathsf{w}'], r'The Planck weight of the multipole $l$ in its bin.', 'dimensionless', '', 'STANDARD')
add('GammaCnuB', r'\Gamma_{\mathrm{C\nu B}}', [r'\Gamma_{\mathrm{C\nu B}}'], r'The rate at which a tritium target captures neutrinos of the cosmic neutrino background.', '1/time', '', 'STANDARD')
add('NT', r'N_{\mathrm{T}}', [r'N_{\mathrm{T}}'], r'The number of tritium nuclei of the target.', 'dimensionless', r'$2.0\times10^{25}$ for 100 g', 'STANDARD')
add('sigmabarT', r'\bar\sigma_{\mathrm{T}}', [r'\bar{\sigma}_{\mathrm{T}}'], r'The averaged cross-section of the capture of an electron neutrino on tritium: a tritium nucleus captures left-handed electron neutrinos of mean speed $\mathsf{s}$ and number density $n$ at the rate $\bar\sigma_{\mathrm{T}}(1 + \mathsf{s})\,c\,n$ ($c$ the speed of light, 1 in the formulas; Long, Lunardini and Sabancilar).', 'cm$^2$', r'$3.834\times10^{-45}$ cm$^2$', 'STANDARD')
add('Uei', r'U_{\mathrm{e}i}', [r'U_{\mathrm{e}i}'], r'The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$.', 'dimensionless', r'$\lvert U_{\mathrm{e}i}\rvert^2 = 0.682$, 0.296 and 0.022 for $i = 1, 2, 3$ (NuFIT 5.2, the fit without the Super-Kamiokande atmospheric data: the values of the record; NuFIT 6.0 with them gives 0.677, 0.301 and 0.022)', 'STANDARD')
add('sstate', r'\mathsf{s}_i', [r'\mathsf{s}'], r'The mean speed of the neutrino mass state $i$ today, averaged over its momentum distribution (0 for a state at rest, 1 for a massless one).', 'dimensionless', r'1, 0.061 and 0.011 for $\nu_1$, $\nu_2$ and $\nu_3$ with $m_1 = 0$; 0.023 for $\nu_1$ with $m_1 = 23$ meV', 'STANDARD')

# ---------------------------------------------------------------- ANALYSIS
add('ph', r'p_{\mathrm{h}}', [r'p_{\mathrm{h}}'], r'The momentum along the hidden direction of a particle confined to it, if that direction were compact (A-2, not UM-3).', 'GeV', '', 'STANDARD')
add('mKK', r'm_{\mathrm{KK}}', [r'm_{\mathrm{KK}}'], r'The masses of the tower of modes of a field on a compact hidden direction (Kaluza-Klein masses; A-2, not UM-3).', 'GeV', '', 'STANDARD')
add('kint', r'\mathsf{k}', [r'\mathsf{k}'], r'An integer that numbers the modes of a compact direction.', 'dimensionless', '', 'STANDARD')
add('ellb', r'\ell_{\mathrm{b}}', [r'\ell_{\mathrm{b}}'], r'The width of a bound state of dirac16complex along the hidden direction: the root mean square of $\sigma$ in its density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$.', 'length', r'$1/(\sqrt2\,q_{\mathrm{b}})$', 'DERIVED')
add('Tchi', r'\mathcal{T}_\chi{}^a{}_b', [r'\mathcal{T}_{\chi}'], r'The four-dimensional energy-momentum tensor of the gas of the bound particles $\chi$ of dirac16complex, per proper volume of ordinary space at the fold (energy density $\rho_\chi$).', 'GeV$^4$', '', 'DERIVED')

# ---------------------------------------------------------------- STABILISER (the stabiliser of the bulk)
add('ellg', r'\ell_{\mathrm{g}}', [r'\ell_{\mathrm{g}}'], r'The length measured along the surface of a globe; $\mathrm{d}\ell_{\mathrm{g}}$ is the length of a small step on it (an example of a metric, not UM-3).', 'length', '', 'STANDARD')
add('Rglobe', r'R_{\mathrm{g}}', [r'R_{\mathrm{g}}'], r'The radius of a globe (an example, not UM-3).', 'length', '', 'STANDARD')
add('thglobe', r'\theta_{\mathrm{g}}', [r'\theta_{\mathrm{g}}'], r'The angle of a point of a globe from its north pole: 0 at the north pole, $\pi/2$ on the equator, $\pi$ at the south pole (an example, not UM-3).', 'radian', '', 'STANDARD')
add('phglobe', r'\phi_{\mathrm{g}}', [r'\phi_{\mathrm{g}}'], r'The longitude of a point of a globe (an example, not UM-3).', 'radian', '', 'STANDARD')
add('Wwarp', r'\mathcal{W}', [r'\mathcal{W}'], r'The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-3 the function of $\sigma$ that multiplies ordinary space and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold.', 'dimensionless', '', 'DERIVED')
add('Tmed', r'\mathcal{T}_{\mathrm{med}}{}^a{}_b', [r'\mathcal{T}_{\mathrm{med}}'], r'The energy-momentum tensor of one medium (frame components): for a medium at rest the entry along the time is minus its energy density, the entries along the other directions are its pressures, and the entries that mix the time with another direction are its flows of energy along that direction.', 'GeV$^8$ (energy per volume in eight dimensions)', '', 'STANDARD')
add('pmed', r'p_{\mathrm{med}}', [r'p_{\mathrm{med}}'], r'The pressure of a medium at rest, the same along every direction but the time (for a medium of the bulk: along $\sigma$, ordinary space and the extra times).', 'GeV$^8$', '', 'STANDARD')
add('rhomed', r'\rho_{\mathrm{med}}', [r'\rho_{\mathrm{med}}'], r'The energy density (energy per volume) of a medium at rest.', 'GeV$^8$', '', 'STANDARD')
add('LambdaE', r'\Lambda_{\mathrm{E}}', [r'\Lambda_{\mathrm{E}}'], r"The cosmological constant of Einstein's static universe of 1917, in four dimensions (an example, not UM-3).", '1/length$^2$', '', 'STANDARD')
add('rhoE', r'\rho_{\mathrm{E}}', [r'\rho_{\mathrm{E}}'], r"The mass density of the dust that fills Einstein's static universe (an example, not UM-3).", 'mass per volume', '', 'STANDARD')
add('RE', r'R_{\mathrm{E}}', [r'R_{\mathrm{E}}'], r"The radius of the three-dimensional sphere that is the space of Einstein's static universe (an example, not UM-3).", 'length', '', 'STANDARD')
add('Pair', r'P_{\mathrm{air}}', [r'P_{\mathrm{air}}'], r'The pressure of the air at the altitude $h_{\mathrm{alt}}$ (an example, not UM-3).', 'Pa', r'about $1.0\times10^5$ Pa at the ground', 'STANDARD')
add('halt', r'h_{\mathrm{alt}}', [r'h_{\mathrm{alt}}'], r'The altitude above the ground (an example, not UM-3).', 'm', '', 'STANDARD')
add('rhoair', r'\rho_{\mathrm{air}}', [r'\rho_{\mathrm{air}}'], r'The mass density of the air at the altitude $h_{\mathrm{alt}}$ (an example, not UM-3).', 'kg/m$^3$', r'about 1.2 kg/m$^3$ at the ground', 'STANDARD')
add('gearth', r'g_{\oplus}', [r'g_{\oplus}'], r'The acceleration of free fall at the surface of the Earth (an example, not UM-3).', 'm/s$^2$', r'9.81 m/s$^2$', 'STANDARD')
add('Kf', r'K_{\mathrm{f}}', [r'K_{\mathrm{f}}'], r'The kinetic energy per volume of a field that fills the bulk uniformly and changes only with the time $x_4$: half the square of its rate of change for an ordinary field (never negative), minus that for a field whose kinetic term has the opposite sign (a ghost).', 'GeV$^8$', '', 'STANDARD')
add('Vf', r'V_{\mathrm{f}}', [r'V_{\mathrm{f}}'], r'The potential energy per volume of a field that fills the bulk uniformly and changes only with the time $x_4$.', 'GeV$^8$', '', 'STANDARD')
add('lambdaF', r'\lambda_{\mathrm{F}}', [r'\lambda_{\mathrm{F}}'], r'The tension of the fold: the part of the fold fluid whose pressures along ordinary space and along the extra times are minus its energy density (a vacuum energy of the seven-dimensional fold), per unit volume of ordinary space of the fold (four-dimensional normalisation).', 'GeV$^4$', r'$32HV_*/(5\kappa)$', 'DERIVED')
add('rhod', r'\rho_{\mathrm{d}}', [r'\rho_{\mathrm{d}}'], r"The pressureless part of the static source of the fold with the author's original weights: the energy density of the fold fluid minus its tension, per unit volume of ordinary space of the fold.", 'GeV$^4$', r"$HV_*/(8\kappa)$ with the author's original weights; 0 with the corrected weights", 'DERIVED')
add('mcurv', r'm_{\mathrm{c}}', [r'm_{\mathrm{c}}'], r'The number of the other curved directions of the static block seen from one direction: 6 for $\sigma$, ordinary space and the extra times (the seven curved directions without the given one), 7 for the time (which is not curved itself).', 'dimensionless', '6 or 7', 'DERIVED')
add('rho4s', r'\rho_{4,\mathrm{s}}', [r'\rho_{4,\mathrm{s}}'], r"The energy of the stabiliser per unit volume of ordinary space of the fold with the author's original weights: its energy density integrated over the hidden direction and the extra times.", 'GeV$^4$', r"$-HV_*/(48\kappa)$ with the author's original weights; 0 with the corrected weights", 'DERIVED')
add('Pcon', r'\mathsf{P}(\mathsf{A}, \mathsf{U})', [r'\mathsf{P}'], r'The polynomial of the energy constraint of the bulk with the author’s original Lovelock weights: the $(x_4, x_4)$ component of the bulk equations of the author’s metric was $\kappa\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = (H^2/16)\,\mathsf{P}(\mathsf{A}, \mathsf{U})$, whatever the time derivatives of the rates (with the corrected weights it is $\mathsf{A}^3(\mathsf{A} - \mathsf{U})^3H^2$).', 'dimensionless', r'$\mathsf{P}(0, 0) = 1$, $\mathsf{P}(\pm1, 0) = 0$', 'DERIVED')

# ---------------------------------------------------------------- 2026-10-25: the sources of the fold, the constraints, the open questions
add('hgw', r'h_{\mathrm{gw}}', [r'h_{\mathrm{gw}}'], r'The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world.', 'dimensionless', '', 'STANDARD')
add('K44', r'K_{44}', [r'K_{44}'], r'The coefficient of $\partial^2h_{\mathrm{gw}}/\partial x_4^2$ in the equation of the long-wavelength gravitational wave (the same at every $\sigma$) at the static block, integrated across the hidden direction with the volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$: the part of the bulk plus the thin part at the fold.', r'GeV$^5$ ($\kappa K_{44}$ is a length)', '', 'DERIVED')
add('K33', r'K_{33}', [r'K_{33}'], r'The coefficient of $-\partial^2h_{\mathrm{gw}}/\partial x_3^2$ in the same equation, with the same two parts; the wave travels at $c_{\mathrm{g}}^2 = K_{33}/K_{44}$.', r'GeV$^5$', '', 'DERIVED')
add('Gind', r'G_{\mathrm{ind}}', [r'G_{\mathrm{ind}}'], r'The Newton constant of the induced Einstein-Hilbert term of the fold, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$.', 'GeV$^{-2}$', '', 'ESTIMATE')
add('Nind', r'N_{\mathrm{ind}}', [r'N_{\mathrm{ind}}'], r'The weighted number of the fields of the fold that induce the Einstein-Hilbert term: each real scalar counts $1 - 6\xi$, each Weyl fermion 1, each gauge field $-4$ (with its ghost fields).', 'dimensionless', r'$4(1 - 6\xi_{\mathrm{H}})$ for the Standard Model with three right-handed neutrinos', 'DERIVED')
add('Lambdac', r'\Lambda_{\mathrm{c}}', [r'\Lambda_{\mathrm{c}}'], r'The cutoff of the proper-time integral of the one-loop effective action of the fields of the fold: the highest energy of the quantum fluctuations that induce gravity.', 'GeV', r'$\sqrt{24}\,\pi M_{\mathrm{red}} = 3.748\times10^{19}$ GeV $= 3.07M_{\mathrm{Pl}}$ if the induced term alone gave the measured Newton constant at $\xi_{\mathrm{H}} = 0$', 'ESTIMATE')
add('xinm', r'\xi', [r'\xi'], r'The coupling of a real scalar field to the scalar curvature $\hat R$ of the fold: the term $-\frac12\xi\hat R$ times the square of the field in its Lagrangian ($\xi = 1/6$ is the conformal coupling).', 'dimensionless', '', 'STANDARD')
add('xiH', r'\xi_{\mathrm{H}}', [r'\xi_{\mathrm{H}}'], r'The coupling $\xi$ of the Higgs doublet to the scalar curvature of the fold.', 'dimensionless', r'not fixed by UM-3; about $1.6\times10^4$ if the Higgs field drives inflation (ESTIMATE); it would have to be below $1/6$ only if the whole gravity of the fold were induced by its fields', 'ASSUMED')
add('NWeyl', r'N_{\mathrm{Weyl}}', [r'N_{\mathrm{Weyl}}'], r'The number of Weyl (two-component) fermion fields of the fold.', 'dimensionless', r'48 (three generations of quarks and leptons with three right-handed neutrinos)', 'STANDARD')
add('Ngauge', r'N_{\mathrm{gauge}}', [r'N_{\mathrm{gauge}}'], r'The number of gauge fields of the fold.', 'dimensionless', r'12 (eight gluons, three $W$, one $B$)', 'STANDARD')
add('Mred', r'M_{\mathrm{red}}', [r'M_{\mathrm{red}}'], r'The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$.', 'GeV', r'$2.435\times10^{18}$ GeV', 'STANDARD')
add('amode', r'\mathsf{a}_o,\ \mathsf{a}_o^\dagger', [r'\mathsf{a}'], r'The annihilation and the creation operator of the mode $o$ of the quantised dirac16complex (frequency $\omega_o$, Krein charge $\mathcal{Q}_o$); the dagger is the adjoint with respect to the indefinite (Krein) scalar product.', 'dimensionless', '', 'STANDARD')
add('HPsi', r'\mathsf{H}_\Psi', [r'\mathsf{H}_{\Psi}'], r'The Hamiltonian (the energy operator) of the quantised dirac16complex.', 'GeV', '', 'DERIVED')
add('sigmaleak', r'\sigma_{\mathrm{leak}}', [r'\sigma_{\mathrm{leak}}'], r'The distance from the fold beyond which a state of dirac16complex with a momentum along the extra times is no longer bound: the warping multiplies that momentum by $\mathrm{e}^{H\lvert\sigma\rvert}$, and beyond $\sigma_{\mathrm{leak}}$ it exceeds the local gap.', 'length', '', 'DERIVED')
add('Gammaf', r'\Gamma_{\mathrm{f}}', [r'\Gamma_{\mathrm{f}}'], r'The growth rate of a mode of a massless field of the fold with the physical momentum $l_{\mathrm{t}}$ along the extra times and no momentum along ordinary space, on the branch of frozen extra times with the constant expansion rate $H_{\mathrm{i}}$ of ordinary space.', 'GeV (1/time)', '', 'DERIVED')
add('Hi', r'H_{\mathrm{i}}', [r'H_{\mathrm{i}}'], r'A constant expansion rate $a_4'"'"'$ of ordinary space on the branch of frozen extra times (an inflation of the fold, or a constant rate in an example).', 'GeV', '', 'ASSUMED')
add('Gammat', r'\Gamma_{\mathrm{t}}', [r'\Gamma_{\mathrm{t}}'], r'The growth rate of a mode of a massless field of the fold that has a momentum along the extra times, in the late universe.', 'GeV (1/time)', '', 'DERIVED')
add('lt', r'l_{\mathrm{t}}', [r'l_{\mathrm{t}}'], r'The physical momentum of a mode along the extra times.', 'GeV', '', 'STANDARD')
add('kp', r'k_{\mathrm{p}}', [r'k_{\mathrm{p}}'], r'The physical momentum of a mode along ordinary space.', 'GeV', '', 'STANDARD')
add('Lt', r'L_{\mathrm{t}}', [r'L_{\mathrm{t}}'], r'The physical period of the extra times, if they are compact.', 'length', '', 'ASSUMED')
add('tzero', r't_0', [r't_{0}'], r'The age of the universe.', 'time', r'13.8 Gyr', 'STANDARD')
add('vg', r'v_{\mathrm{g}}', [r'v_{\mathrm{g}}'], r'The group velocity of a particle $\chi$ along ordinary space, $\mathrm{d}\omega/\mathrm{d}\lvert\vec k\rvert$, in units of the speed of light on the fold.', 'dimensionless', '', 'DERIVED')
add('phik', r'\phi_k', [r'\phi', 'index:k'], r'The amplitude of a Fourier mode of a massless scalar field of the fold: of comoving wave number $k$ (the label $k$) along ordinary space, and, where it is said, with a momentum $\vec\kappa$ along the extra times.', 'GeV', '', 'STANDARD')
add('ce', r'c_{\mathrm{e}}', [r'c_{\mathrm{e}}'], r'The maximal speed of the electron, in units of the speed of light.', 'dimensionless', r'$c_{\mathrm{e}} - 1 < 5\times10^{-21}$ (no vacuum Cherenkov radiation of the 5 PeV electrons of the 2010 flare of the Crab nebula) and $1 - c_{\mathrm{e}} < 5.6\times10^{-20}$ (synchrotron electrons with the Lorentz factor $3\times10^9$)', 'STANDARD')
add('gP', r'g_{\mathrm{P}}', [r'g_{\mathrm{P}}'], r'The strength of one lepton portal of the particles $\chi$ (a coupling of the currents of $\chi$ and of a chiral lepton), fixed by the relic density: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 9g_{\mathrm{P}}^2\omega_{\mathrm{b}}^2/(2\pi)$ for one $\chi$ with one antiparticle and nine chiral lepton states.', 'GeV$^{-2}$', r'$g_{\mathrm{P}}\omega_{\mathrm{b}}^2 = 0.110$, 0.220 and 0.734 for $\omega_{\mathrm{b}} = 1.5$, 3 and 10 TeV', 'ESTIMATE')
add('Hankel', r'\mathrm{H}^{(1)}_0', [r'\mathrm{H}'], r'The Hankel function of the first kind of order zero, $\mathrm{H}^{(1)}_0 = J_0 + \mathrm{i}Y_0$ with the Bessel functions $J_0$ and $Y_0$ of order zero.', 'dimensionless', '', 'STANDARD')
add('gammaE', r'\gamma_{\mathrm{E}}', [r'\gamma_{\mathrm{E}}'], r'The Euler-Mascheroni constant.', 'dimensionless', '0.5772157', 'STANDARD')
add('rT', r'r_{\mathrm{T}}', [r'r_{\mathrm{T}}'], r'The ratio of the amplitudes of the primordial spectra of gravitational waves (tensor) and of curvature (scalar) at the pivot scale.', 'dimensionless', r'below 0.036 (BICEP/Keck 2021, 95 per cent)', 'STANDARD')
add('Hinf', r'H_{\mathrm{inf}}', [r'H_{\mathrm{inf}}'], r'The expansion rate of ordinary space during an inflationary era.', 'GeV', '', 'STANDARD')
add('Ne', r'N_{\mathrm{e}}', [r'N_{\mathrm{e}}'], r'The number of e-foldings of inflation after the pivot scale left the horizon.', 'dimensionless', '55', 'STANDARD')
add('deltaCP', r'\delta_{\mathrm{CP}}', [r'\delta_{\mathrm{CP}}'], r'The Dirac phase of the mixing matrix $U_{\mathrm{PMNS}}$.', 'degree', r'$212^\circ$ (NuFIT 6.0, normal ordering); 0 in the computations of UM-3', 'STANDARD')
add('meff', r'm_{\mathrm{eff}}', [r'm_{\mathrm{eff}}'], r'The effective mass of the electron neutrino measured in the beta decay of tritium, $m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2$.', 'eV', r'below 0.45 eV (KATRIN 2025, 90 per cent)', 'STANDARD')
add('GammaK', r'\Gamma_{\mathrm{K}}', [r'\Gamma_{\mathrm{K}}'], r'The growth rate of a perturbation of the gas of particles $\chi$ when the Krein-positive partner of its occupied level collides with it (a pair of complex frequencies $\omega \pm \mathrm{i}\Gamma_{\mathrm{K}}$).', r'$m_\Psi$', '', 'DERIVED')

# ---------------------------------------------------------------- the definition of the fold (FD-1 to FD-10)
add('foldF', r'\mathcal{F}', [r'\mathcal{F}'], r'The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold.', '', '', 'DERIVED')
add('Kextr', r'K^a{}_b', [r'K'], r'The extrinsic curvature of a surface $\sigma = \mathrm{const}$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along ordinary space and the extra times, 0 along the time.', 'GeV (1/length)', '', 'DERIVED')
add('yRS', r'y_{\mathrm{RS}}', [r'y_{\mathrm{RS}}'], r'The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-3).', 'length', '', 'STANDARD')
add('kRS', r'k_{\mathrm{RS}}', [r'k_{\mathrm{RS}}'], r'The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp factor of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-3).', 'GeV (1/length)', '', 'STANDARD')
add('lambdaRS', r'\lambda_{\mathrm{RS}}', [r'\lambda_{\mathrm{RS}}'], r'The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-3).', 'GeV$^4$', '', 'STANDARD')
add('LambdaRS', r'\Lambda_{\mathrm{RS}}', [r'\Lambda_{\mathrm{RS}}'], r'The vacuum energy density of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2/\kappa_5$ (FD-8, an example, not UM-3).', 'GeV$^5$', '', 'STANDARD')
add('kappa5', r'\kappa_5', [r'\kappa_{5}'], r'The gravitational coupling of five dimensions in the model of Randall and Sundrum, $\kappa_5 = 8\pi G_5$ (FD-8, an example, not UM-3).', 'GeV$^{-3}$', '', 'STANDARD')
add('R1refl', r'\mathsf{R}_1', [r'\mathsf{R}_{1}'], r'The reflection across the fold acting on a profile of dirac16complex together with the reflection of ordinary space, $(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma)$ (FD-10): a symmetry of dirac16complex, of gravity and of the mean field of the gas of the particles $\chi$; the bound states of Krein charge $-1$ are even, those of Krein charge $+1$ odd.', 'dimensionless', '', 'DERIVED')
add('R2refl', r'\mathsf{R}_2', [r'\mathsf{R}_{2}'], r'The reflection across the fold acting on a profile of dirac16complex together with the reflection of the extra times, $(\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma)$ (FD-10): it maps the bound states of one Krein charge onto those of the other.', 'dimensionless', '', 'DERIVED')



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this file (written into its JSON file)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    out = HERE / 'symbols'
    out.mkdir(exist_ok=True)
    data = {'_definition_of_the_fold': {'text': fold_definition()}}
    data.update(E)
    (out / 'core.json').write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('%d entries written to %s' % (len(E), out / 'core.json'))


if __name__ == '__main__':
    main()
