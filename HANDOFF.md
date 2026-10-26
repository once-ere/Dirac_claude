# HANDOFF — exact restart procedure after a session limit

This file is the complete restart kit for a fresh Claude Code session (or a human)
that has none of the previous conversation.  Everything a restart needs is committed
in this repository; nothing depends on the old session's scratch directory.

## The fold of UM-4: definition and examples

<!-- begin fold definition of UM-4 -->
```text
THE FOLD (the definition used in every UM-4 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The metric of UM-4 depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one surface of F, at z = pi/2: F is the union of these copies, one per period (example 2), and "the
fold" without a qualifier is the copy in the period that contains our world. A point of the fold is labelled by the seven
coordinates x1, ..., x7, and the metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.
Notation: ln is the natural logarithm, e Euler's number, exp(y) = e^y, sin, cos and cot = cos/sin the trigonometric
functions, sinh, cosh, tanh = sinh/cosh and coth = cosh/sinh the hyperbolic functions, |y| the absolute value, max and
min the larger and the smaller of their arguments; det, tr and ^T are the determinant, the trace and the transpose of a
square matrix, and 1_4, 1_8 and 1_16 the identity matrices of 4, 8 and 16 rows; f(0+) and f(0-) are the limits of
f(sigma) as sigma approaches 0 from above and from below.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the metric of UM-4 is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ].
It depends on sigma only through |sigma|. The function W(sigma) = e^(-2 H |sigma|), which multiplies the squared steps of all
seven directions of the fold (ordinary space, the time and the extra times), is the warp factor of the metric (its square
root e^(-H |sigma|) multiplies the lengths). The time x4 is warped like the other directions (the author's order of
2026-10-25, 13:15 PDT; in UM-3 it was not), so that every surface sigma = const has the light cone of the fold. Four
properties make the surface sigma = 0 a fold, and together they single it out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp factor is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|) equals 1 on the fold and
     decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb = -H sgn(sigma) delta^a_b   (all seven directions a, b of the fold)
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function, delta^a_b the Kronecker delta, a, b frame indices along the fold); it jumps by -2 H in every direction
     of the fold. The field equations of gravity of UM-4, G^M_N + Lambda delta^M_N = kappa T^M_N (Einstein gravity: the
     author's Einstein-Lovelock equations with the weights of the Gauss-Bonnet and cubic terms set to zero; G^M_N the
     Einstein tensor, Lambda = -21 H^2 the cosmological constant, kappa = 8 pi G_8 the gravitational coupling of eight
     dimensions, T^M_N the energy-momentum tensor), are linear in the second sigma-derivatives of the metric, so the jump
     puts a Dirac delta function delta_D(sigma) into them: the metric solves them only if the fold carries a thin source
     S^a_b, an energy-momentum tensor concentrated on sigma = 0, given by the integral of the equations across the fold
     (the junction condition of Israel),
        (FD-11) kappa S^a_b = integral from sigma = 0- to 0+ of d sigma G^a_b = -([K^a_b] - [K] delta^a_b)
     ([K^a_b] the jump of the extrinsic curvature across the fold, K its trace), with S^4_4 = -(its energy density),
     S^1_1 = S^2_2 = S^3_3 its pressure along ordinary space and S^5_5 = S^6_6 = S^7_7 its pressure along the extra times; S is
     T integrated across the fold, an energy per unit volume of the six other directions of the fold (unit GeV^7). For the
     static block (a4 and b4 constant) and, to the first order in the curvature of the fold divided by H^2, for every fold
        (FD-12) static block:  kappa S^a_b = -12 H delta^a_b  (a pure tension, kappa lambda_F = 12 H),
                any fold:      kappa S^a_b = -12 H delta^a_b + (2/(5 H)) Ghat^a_b
     (Ghat^a_b the Einstein tensor of the metric FD-2 of the fold): the tension plus matter that obeys the Einstein equations
     of seven dimensions, Ghat^a_b = kappa_7 tau^a_b with kappa_7 = 5 kappa H/2 (tau the matter of the fold), which for frozen
     extra times are the Friedmann equations of general relativity. The fold is therefore not only a place but a physical
     object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-4 the Higgs doublet (with the author's ad hoc vacuum, a time-dependent choice of its vacuum
value), three generations of quarks and leptons, three right-handed neutrinos and the fold fluid (its tension and the
pressure along the extra times that keeps their volume fixed) live on the fold: they are fields at sigma = 0, functions of
x1, ..., x4 (no field depends on the extra times). The gauge fields of SU(3)_C x SU(2)_L x U(1)_Y live in the bulk; their
massless modes are bound to the fold, so that the photon and the gluons of the four-dimensional world are waves of the bulk
that the fold holds, and photons that leave the fold travel through the bulk at the speed of light. dirac16complex (the
author's spinor field of eight dimensions) and gravity live in the bulk sigma != 0 as well as on the fold; the states chi of
dirac16complex that the fold holds (in UM-4 long-lived resonances) are the part of it near the fold, and the portals
(couplings between dirac16complex and the fields of the fold) act at sigma = 0. Integrated over the extra times, the fold is
the four-dimensional universe that we observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. In UM-4
files "the fold" means this surface; the examples below use the word for other surfaces with the same properties. The word
is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by the factor e is called
an e-folding.

Examples of folds that are meaningful for UM-4.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     quarks, leptons and the Higgs field, and after the integration over the extra times the four-dimensional universe that
     we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp factor (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2
     diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
     line -infinity < sigma < infinity. A compact direction of length L would give every field a tower of particles with
     the masses 2 pi n/L, n = 1, 2, ... (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
     pi/(6 H) of x0 produces no such tower with the spacing 12 H: every field of the bulk has instead a continuum of modes
     that starts at zero mass, and the fold holds its massless mode.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-4 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
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
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the cosmological constant Lambda_RS (the vacuum energy Lambda_RS/kappa_5), and the bulk is otherwise empty.
     The fold of UM-4 is of the same kind, with every direction of the fold warped by the same factor as in the model of
     Randall and Sundrum: its static block is a space of constant curvature -H^2 in all eight directions, a vacuum of
     Einstein gravity with Lambda = -21 H^2, with a fold of pure tension (FD-12), and the graviton is bound to the fold as
     there. It differs in that the fold has seven dimensions, three of them extra times, in that the space is not cut at
     the brane (Randall and Sundrum identify the two sides of their brane, one physical side; the fold of UM-4 has two
     distinct sides, example 7), and in that the gauge fields live in the bulk as well.
  7. A particle held by a thin layer. A particle held by an attractive thin layer has a wave function that falls off
     exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
     equation, the wave function itself). In UM-4 the states chi of dirac16complex near the fold are of this kind only near
     the fold: at rest and without their self-interaction (the field is Psi = e^((7/2) H |sigma|) chi(sigma) e^(-i omega x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+)   (0 < sigma << sigma_t),
                chi(sigma) = e^(-q_b |sigma|) chi(0-)   (0 < -sigma << sigma_t),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),
                omega_0 = omega_r - i Gamma/2,   omega_r -> sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     fields of the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors, m_Psi the bulk
     mass, q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for mu_R = 0), and omega_r
     tends to the energy omega_b = sqrt(m_Psi^2 - q_b^2) of the bound state of UM-3 when H/q_b -> 0. Because the time is
     warped, the energy omega of the field enters its equation multiplied by e^(H |sigma|): beyond the turning point
     sigma_t (omega_r e^(H sigma_t) = m_Psi) the profile oscillates as a wave that leaves the fold, so the state is a
     resonance of the energy omega_0 at rest and the width Gamma = (2/e) (q_b^2/m_Psi) e^(-2 F_t(upsilon_b) m_Psi/H) (to the
     leading order in H/q_b), with the tunnelling exponent F_t(upsilon) = ln((1 + sqrt(1 - upsilon^2))/upsilon)
     - sqrt(1 - upsilon^2) and upsilon_b = omega_b/m_Psi (the tunnelling through the region between the fold and sigma_t,
     where the profile decays at the local rate sqrt(m_Psi^2 - omega_r^2 e^(2 H |sigma|)), which falls to 0 at sigma_t). The
     profile is not a function of |sigma|: it jumps at the fold, chi(0+) != chi(0-).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (for states at rest R_1 is the reflection across the fold combined with the reflection of ordinary space, R_2 the
     reflection across the fold combined with the reflection of the extra times). T_a (a = 0, ..., 7) are the author's real
     16 x 16 Dirac matrices T16^A[a] of 4+4.nb, built there from six real 4 x 4 matrices (rows separated by ";"):
        (FD-13) s_1 = [0 0 0 1; 0 0 1 0; 0 -1 0 0; -1 0 0 0],   s_2 = [0 0 -1 0; 0 0 0 1; 1 0 0 0; 0 -1 0 0],
                s_3 = [0 1 0 0; -1 0 0 0; 0 0 0 1; 0 0 -1 0],   t_1 = [0 0 0 -1; 0 0 1 0; 0 -1 0 0; 1 0 0 0],
                t_2 = [0 0 -1 0; 0 0 0 -1; 1 0 0 0; 0 1 0 0],   t_3 = [0 1 0 0; -1 0 0 0; 0 0 0 -1; 0 0 1 0],
                Xi_0 = 1_8,  Xi_1 = [[0, s_1], [s_1, 0]],  Xi_2 = [[0, s_2], [s_2, 0]],  Xi_3 = [[0, s_3], [s_3, 0]],
                Xi_4 = [[0, t_3], [-t_3, 0]],  Xi_5 = [[0, t_2], [-t_2, 0]],  Xi_6 = [[0, t_1], [-t_1, 0]],
                Xi_7 = Xi_1 Xi_2 Xi_3 Xi_4 Xi_5 Xi_6 = [[-1_4, 0], [0, 1_4]],
                Xibar_0 = 1_8,  Xibar_a = sigma_8 Xi_a^T sigma_8 (a = 1, ..., 7),  sigma_8 = [[0, 1_4], [1_4, 0]],
                T_a = [[0, Xibar_a], [Xi_a, 0]]  (a = 0, ..., 7)
     ([[A, B], [C, D]] the matrix made of the four blocks A, B, C, D, 0 a block of zeros; s_1, s_2, s_3 and t_1, t_2, t_3
     are s4by4[1..3] and t4by4[1..3], Xi_a and Xibar_a are tau[a] and taubar[a], sigma_8 is sigma88 of the notebook).
     They obey {T_a, T_b} = T_a T_b + T_b T_a = 2 eta_ab 1_16 with eta = diag(1, 1, 1, 1, -1, -1, -1, -1);
     gamma^(a) = eta^aa T_a (no sum) are the Dirac matrices of the frame, gamma^(0) along sigma; the chirality matrix is
     Gamma_8 = T_0 T_1 ... T_7 = [[-1_8, 0], [0, 1_8]], the chiral projectors are P_L = (1_16 - Gamma_8)/2 and
     P_R = (1_16 + Gamma_8)/2, and sigma_16 = T_0 T_1 T_2 T_3 = [[-sigma_8, 0], [0, sigma_8]] defines the Dirac adjoint
     Psibar = Psi^dagger sigma_16 (Psi^dagger the complex conjugate transpose).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of a mean field of a gas of the
     particles chi that is the same on both sides of the fold: the four resonances of Krein charge -1 (the particles chi)
     are even under it and the four of Krein charge +1 are odd, so such a mean field cannot mix the two signs of the
     indefinite charge. R_2 maps the states of one Krein charge onto those of the other and makes the two sets degenerate
     without the self-interaction.
  9. The planes of Horava and Witten. In M-theory (the eleven-dimensional theory whose limits include the superstring
     theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional
     planes left in place by the reflection are mirror surfaces (property 1); each carries one E8 gauge group while gravity
     fills the bulk. As in UM-4, gravity fills the bulk; unlike UM-4, the gauge fields live on the mirror planes (in UM-4
     they live in the bulk), and the two sides of each plane are identified (one physical side).

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp factor vanishes,
    g_x0x0 diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp factor, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a
    kink and without a thin source.
```
<!-- end fold definition of UM-4 -->

## The fold of UM-3: definition and examples

<!-- begin fold definition -->
**Definition.** The *fold* is the seven-dimensional surface of the author's eight-dimensional spacetime on which the
cosine of the angle $z = 6Hx_0$ of the hidden direction vanishes:

$$
\mathcal{F} = \big\{X = (x_0, x_1, \dots, x_7):\ \cos(6Hx_0) = 0\big\},\qquad
\text{in one period } 0 < z < \pi\text{ of the metric: } z = \frac{\pi}{2},\quad x_0 = \frac{\pi}{12H} \tag{FD-1}
$$
<!-- symbols: foldF, Xcoord, x0, x1, x7, Hconst, zvar, pi, Lambda, wL, LambdaN -->
<!-- begin generated symbol list -->
**Symbols in (FD-1).**

- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $\Lambda_{\mathrm{N}}$: The author's pure number in the vacuum equations of his notebook, $\Lambda = -\Lambda_{\mathrm{N}}H^2$: his original value 10, corrected to 7 on 2026-10-25. Unit: dimensionless. Value: 7 (the author's original 10). Status: AUTHOR.

<!-- end generated symbol list -->

$X = \{x_0, \dots, x_7\}$ are the author's coordinates: $x_0$ the hidden space-like direction, $x_1, x_2, x_3$ ordinary space,
$x_4$ the time, $x_5, x_6, x_7$ the three extra times; $H$ is the author's constant (an inverse length). The author's metric
depends on $x_0$ only through $\cot^2z$ and $(\sin^2z)^{1/6}$, so it repeats with the period $\pi/(6H)$ of $x_0$, and every
period $0 < z < \pi$ contains exactly one surface of $\mathcal{F}$, at $z = \pi/2$: $\mathcal{F}$ is the union of these copies,
one per period (example 2), and "the fold" without a qualifier is the copy in the period that contains our world. A point of
the fold is labelled by the seven coordinates $x_1, \dots, x_7$, and the metric restricted to the fold ($\mathrm{d}x_0 = 0$,
$z = \pi/2$) is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N\big\vert_{\mathcal{F}} = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big) \tag{FD-2}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, foldF, euler, a4, b4, x1, x2, x3, x4, x5, x6, x7, prime -->
<!-- begin generated symbol list -->
**Symbols in (FD-2).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.

<!-- end generated symbol list -->

with three space-like and four time-like directions; $a_4$ and $b_4$ are the author's two functions of the time $x_4$.
Notation: $\ln$ is the natural logarithm, $\mathrm{e}$ Euler's number, $\exp(y) = \mathrm{e}^y$, $\sin$, $\cos$ and
$\cot = \cos/\sin$ the trigonometric functions, $\tanh$ the hyperbolic tangent, $\lvert y\rvert$ the absolute value;
$f(0^+)$ and $f(0^-)$ are the limits of $f(\sigma)$ as $\sigma$ approaches 0 from above and from below.

**Why this surface is called a fold.** Measured by the proper distance along the hidden direction,

$$
\sigma = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H},\qquad \mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0,\qquad
\sin z = \mathrm{e}^{-6H\lvert\sigma\rvert} \tag{FD-3}
$$
<!-- symbols: sigma, sgn, pi, zvar, Hconst, diff, x0, euler, infty -->
<!-- begin generated symbol list -->
**Symbols in (FD-3).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.

<!-- end generated symbol list -->

(the fold is $\sigma = 0$; the half-period $0 < z < \pi/2$ is $\sigma < 0$, the half-period $\pi/2 < z < \pi$ is $\sigma > 0$; the
two ends of the period, the tips $z \to 0$ and $z \to \pi$, lie at $\sigma \to -\infty$ and $\sigma \to +\infty$), the author's metric is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
 - \mathrm{d}x_4^2 \tag{FD-4}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, sigma, euler, Hconst, a4, b4, x1, x2, x3, x4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (FD-4).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

It depends on $\sigma$ only through $\lvert\sigma\rvert$. The function $\mathcal{W}(\sigma) = \mathrm{e}^{-2H\lvert\sigma\rvert}$,
which multiplies the squared steps of ordinary space and of the extra times, is the warp factor of the metric (its square
root $\mathrm{e}^{-H\lvert\sigma\rvert}$ multiplies the lengths); the time $x_4$ is not warped. Four properties make the surface
$\sigma = 0$ a fold, and together they single it out within the period:

1. *It is a mirror.* The reflection $\sigma \to -\sigma$ (that is $z \to \pi - z$, or $x_0 \to \pi/(6H) - x_0$) maps the metric
   to itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
   period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are joined
   along the crease.
2. *The warp factor is largest on it.* The warp factor $(\sin^2z)^{1/6} = \mathrm{e}^{-2H\lvert\sigma\rvert}$ equals 1 on the
   fold and decreases on both sides.
3. *The metric has a kink on it.* The metric is continuous across the fold, but its first derivative along $\sigma$ jumps.
   The extrinsic curvature of the surfaces $\sigma = \text{const}$ changes sign across the fold,

$$
K^a{}_b = \frac12\,g^{ac}\,\partial_\sigma g_{cb}:\qquad
K^{1}{}_{1} = K^{2}{}_{2} = K^{3}{}_{3} = K^{5}{}_{5} = K^{6}{}_{6} = K^{7}{}_{7} = -H\,\mathrm{sgn}(\sigma),\qquad K^{4}{}_{4} = 0 \tag{FD-5}
$$
<!-- symbols: Kextr, ia, ib, ic, metric, partial, isigma, sigma, Hconst, sgn, eta, diag -->
<!-- begin generated symbol list -->
**Symbols in (FD-5).**

- $K^a{}_b$: The extrinsic curvature of a surface of constant $\sigma$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along ordinary space and the extra times, 0 along the time. Unit: GeV (1/length). Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $c$: A frame index (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.

<!-- end generated symbol list -->

   ($a, b$ frame indices along the fold); it jumps by $-2H$ along ordinary space and along the extra times. The
   Einstein-Lovelock equations of UM-3, $\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b + \Lambda\delta^a{}_b = \kappa\mathcal{T}^a{}_b$
   ($\mathcal{E}_{(p)}$ the Lovelock tensor of order $p = 1, 2, 3$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ its coupling with the weights
   $w = (1, 1/20, 1/360)$, $\Lambda = -7H^2$ the cosmological constant, $\kappa = 8\pi G_8$ the gravitational coupling of eight
   dimensions, $\mathcal{T}^a{}_b$ the energy-momentum tensor, $\delta^a{}_b$ the Kronecker delta), are linear in the second
   $\sigma$-derivatives of the metric, so the jump puts a Dirac delta function $\delta_{\mathrm{D}}(\sigma)$ into them: the
   metric solves them only if the fold carries a thin source $\mathcal{S}^a{}_b$, an energy-momentum tensor concentrated on
   $\sigma = 0$, given by the integral of the equations across the fold (the junction conditions),

$$
\kappa\,\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b \tag{FD-11}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, diff, sigma, ip, alphaL, LovE, G8, Riemann, LovL -->
<!-- begin generated symbol list -->
**Symbols in (FD-11).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

   with $\mathcal{S}^4{}_4 = -(\text{its energy density})$, $\mathcal{S}^1{}_1 = \mathcal{S}^2{}_2 = \mathcal{S}^3{}_3$ its pressure
   along ordinary space and $\mathcal{S}^5{}_5 = \mathcal{S}^6{}_6 = \mathcal{S}^7{}_7$ its pressure along the extra times;
   $\mathcal{S}$ is $\mathcal{T}$ integrated across the fold, an energy per unit volume of the six other directions of the fold
   (unit GeV$^7$). On the static block ($a_4$ and $b_4$ constant) and on an expanding fold whose extra times are frozen
   ($b_4$ proportional to $\mathrm{e}^{a_4}$; $\mathsf{A} = a_4'/H$, $\mathsf{A}_1 = a_4''/H^2$)

$$
\begin{aligned}
&\text{static block:}\quad \kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\,\delta^a{}_b\quad\text{(a pure tension)},\\
&\text{frozen extra times:}\quad \kappa\mathcal{S}^1{}_1 = -\frac{16}{15}\big(6 + 3\mathsf{A}^2 + 2\mathsf{A}_1\big)H,\quad
 \kappa\mathcal{S}^4{}_4 = -\frac{16}{5}\big(2 + \mathsf{A}^2\big)H,\\
&\qquad\qquad \kappa\mathcal{S}^5{}_5 = -\frac45\big(8 + 8\mathsf{A}^2 + \mathsf{A}^4 + 4\mathsf{A}_1 + \mathsf{A}^2\mathsf{A}_1\big)H
\end{aligned} \tag{FD-12}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, Hconst, delta, Asf, A1sf, H4, h100 -->
<!-- begin generated symbol list -->
**Symbols in (FD-12).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.

<!-- end generated symbol list -->

   the tension plus matter that obeys the Friedmann equations of general relativity. The fold is therefore not only a place
   but a physical object: a thin layer that carries energy and momentum (a brane). (FD-11 and FD-12 were added to this
   definition on 2026-10-25, after FD-1 to FD-10, with the corrected Lovelock weights; they stand here because they belong to
   property 3.)
4. *The author's coordinate $x_0$ degenerates on it.* The metric component $g_{x_0x_0} = \cot^2(6Hx_0)$ vanishes on the fold
   and nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,

$$
\lvert\sigma\rvert = 3H\Big(x_0 - \frac{\pi}{12H}\Big)^2\Big[1 + 6H^2\Big(x_0 - \frac{\pi}{12H}\Big)^2 + \dots\Big] \tag{FD-6}
$$
<!-- symbols: sigma, Hconst, x0, pi -->
<!-- begin generated symbol list -->
**Symbols in (FD-6).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

   so the two coordinate values on either side of $x_0 = \pi/(12H)$ at the same coordinate distance lie at the same proper
   distance from the fold: the coordinate line of $x_0$ is folded onto the line of proper distances (a fold map, example 5).

**What lives on the fold.** In UM-3 the Standard Model (the Higgs doublet with the author's ad hoc vacuum, a time-dependent
choice of its vacuum value; the gauge fields of $SU(3)_C \times SU(2)_L \times U(1)_Y$; three generations of quarks and
leptons and three right-handed neutrinos) and the fold fluid (its tension and the pressure along the extra times that keeps
their volume fixed) live on the fold: they are fields at $\sigma = 0$, functions of $x_1, \dots, x_4$ (no field depends on
the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we observe, with the
metric $\mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in $x_1, \dots, x_4$. dirac16complex (the
author's spinor field of eight dimensions) and gravity live in the bulk $\sigma \ne 0$ as well as on the fold; the bound
states $\chi$ of dirac16complex are the part of it that the fold holds, and the portals (couplings between dirac16complex and
Standard-Model fields) act at $\sigma = 0$. In UM-3 files "the fold" means this surface; the examples below use the word
for other surfaces with the same properties. The word is not used in its other senses: a set of equal energy levels is
called degenerate, and a growth by the factor $\mathrm{e}$ is called an e-folding.

**Examples of folds that are meaningful for UM-3.**

1. *Our fold.* The fold $z = \pi/2$ of the period that contains our world (FD-1): the seven-dimensional world-volume of the
   Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
2. *The copies of the fold.* Because the metric repeats with the period $\pi/(6H)$, every surface
   $x_0 = \pi/(12H) + (\text{an integer multiple of } \pi/(6H))$ is a copy of the fold, one per period. Neighbouring copies are
   separated by a tip ($z$ a multiple of $\pi$), where the warp factor $(\sin^2z)^{1/6}$ vanishes and $g_{x_0x_0} = \cot^2z$
   diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
   line $-\infty < \sigma < \infty$. A compact direction of length $L$ would give every field a tower of particles with the
   masses $2\pi n/L$, $n = 1, 2, \dots$ (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
   $\pi/(6H)$ of $x_0$ produces no such tower with the spacing $12H$, and the $x_0$ mass of the bound states is their binding
   to the fold.
3. *A folded sheet of paper.* The crease of a folded sheet is a fold in this sense: the two halves are mirror images
   (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
   In UM-3 the direction across the crease is the hidden direction $\sigma$, the seven directions along the crease are
   $x_1, \dots, x_7$, and the crease is the fold.
4. *A folded function.* The warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ is the simplest folded function: continuous,
   mirror symmetric, largest at $\sigma = 0$, with a jump of its derivative,

$$
\frac{\mathrm{d}}{\mathrm{d}\sigma}\mathrm{e}^{-2H\lvert\sigma\rvert} = -2H\,\mathrm{sgn}(\sigma)\,\mathrm{e}^{-2H\lvert\sigma\rvert},\qquad
\frac{\mathrm{d}^2}{\mathrm{d}\sigma^2}\mathrm{e}^{-2H\lvert\sigma\rvert} = 4H^2\,\mathrm{e}^{-2H\lvert\sigma\rvert} - 4H\,\delta_{\mathrm{D}}(\sigma) \tag{FD-7}
$$
<!-- symbols: diff, sigma, euler, Hconst, sgn, deltaD -->
<!-- begin generated symbol list -->
**Symbols in (FD-7).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.

<!-- end generated symbol list -->

   whose delta function is the origin of the thin source of property 3. Every metric function of FD-4 depends on $\sigma$
   through $\lvert\sigma\rvert$ and is folded at $\sigma = 0$ in this sense.
5. *A fold map.* In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map $u \mapsto u^2$ of a line
   onto a half-line: it folds the line at $u = 0$, two points $\pm u$ land on the same point, and the derivative of the map
   vanishes on the fold. Near the fold the map from the author's coordinate $x_0$ to the distance $\lvert\sigma\rvert$ from the
   fold is of this kind (FD-6), and $g_{x_0x_0} = \cot^2z$, the square of the derivative $\mathrm{d}\sigma/\mathrm{d}x_0$,
   vanishes there.
6. *The brane of Randall and Sundrum.* The five-dimensional metric

$$
\mathrm{d}y_{\mathrm{RS}}^2 + \mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2
 - \mathrm{d}x_4^2\big),\qquad \lambda_{\mathrm{RS}} = \frac{6k_{\mathrm{RS}}}{\kappa_5},\qquad \Lambda_{\mathrm{RS}} = -\frac{6k_{\mathrm{RS}}^2}{\kappa_5} \tag{FD-8}
$$
<!-- symbols: diff, yRS, euler, kRS, x1, x2, x3, x4, lambdaRS, kappa5, LambdaRS -->
<!-- begin generated symbol list -->
**Symbols in (FD-8).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $y_{\mathrm{RS}}$: The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-3). Unit: length. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $k_{\mathrm{RS}}$: The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp factor of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-3). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\lambda_{\mathrm{RS}}$: The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^4$. Status: STANDARD.
- $\kappa_5$: The gravitational coupling of five dimensions in the model of Randall and Sundrum, $8\pi$ times the Newton constant of five dimensions (FD-8, an example, not UM-3). Unit: GeV$^{-3}$. Status: STANDARD.
- $\Lambda_{\mathrm{RS}}$: The vacuum energy density of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^5$. Status: STANDARD.

<!-- end generated symbol list -->

   has a fold at $y_{\mathrm{RS}} = 0$ with the properties 1 to 3 (its coordinate $y_{\mathrm{RS}}$ is already the proper
   distance, so property 4 does not arise); Einstein's equations require there a brane of the tension $\lambda_{\mathrm{RS}}$
   (Israel's junction condition) and in the bulk the vacuum energy $\Lambda_{\mathrm{RS}}$, and the bulk is otherwise empty. The
   fold of UM-3 is of the same kind: its static block is a vacuum of the bulk with a fold of pure tension (FD-12). It differs
   in that the time $x_4$ is not warped, three extra times are warped together with ordinary space, the Lovelock terms add to
   the junction conditions, and the space is not cut at the brane: Randall and Sundrum identify the two sides of their brane
   (one physical side), while the fold of UM-3 has two distinct sides (example 7).
7. *A particle bound to a thin layer.* A particle held by an attractive thin layer has a wave function that falls off
   exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
   equation, the wave function itself). In UM-3 the particles $\chi$ of dark matter are the states of dirac16complex bound to
   the fold; at rest and without their self-interaction (the field is
   $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{-\mathrm{i}\omega_{\mathrm{b}}x_4}$)

$$
\begin{aligned}
&\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^+)\ \ (\sigma > 0),\qquad
\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^-)\ \ (\sigma < 0),\\
&\chi(0^+) = \exp\Big(\gamma^{(0)}\big(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}\big)\Big)\chi(0^-),\qquad
\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}
\end{aligned} \tag{FD-9}
$$
<!-- symbols: chiprof, sigma, euler, qb, gammaM, muX, PL, PR, Gamma8, identity, omegab, mPsi, Vstar, Psi, vielbein, imag, omegafreq, kvec, xvec, Vt, sigma16, dagger, io -->
<!-- begin generated symbol list -->
**Symbols in (FD-9).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.

<!-- end generated symbol list -->

   where $\mu_{\mathrm{L}}$, $\mu_{\mathrm{R}}$ are the strengths of the fold for the left- and right-handed halves of
   dirac16complex (set by the Standard-Model fields on the fold) and $q_{\mathrm{b}} = -m_\Psi(\mu_{\mathrm{L}} + \mu_{\mathrm{R}})\tanh\varsigma/(2\varsigma)$,
   $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$ for $\mu_{\mathrm{R}} = 0$). The profile
   is not a function of $\lvert\sigma\rvert$: it jumps at the fold, $\chi(0^+) \ne \chi(0^-)$.
8. *The fold as a mirror for dirac16complex.* The reflection across the fold acts on the profiles $\chi(\sigma)$ in two ways,

$$
(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma),\qquad (\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma) \tag{FD-10}
$$
<!-- symbols: R1refl, R2refl, chiprof, sigma, Tmat -->
<!-- begin generated symbol list -->
**Symbols in (FD-10).**

- $\mathsf{R}_1$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of ordinary space, $(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma)$ (FD-10): a symmetry of dirac16complex, of gravity and of the mean field of the gas of the particles $\chi$; the bound states of Krein charge $-1$ are even, those of Krein charge $+1$ odd. Unit: dimensionless. Status: DERIVED.
- $\mathsf{R}_2$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of the extra times, $(\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma)$ (FD-10): it maps the bound states of one Krein charge onto those of the other. Unit: dimensionless. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

   ($T_a$ the author's Dirac matrices; for states at rest $\mathsf{R}_1$ is the reflection across the fold combined with the
   reflection of ordinary space, $\mathsf{R}_2$ the reflection across the fold combined with the reflection of the extra
   times). The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a
   state can carry the charge $-1$ or $+1$. $\mathsf{R}_1$ is a symmetry of dirac16complex, of gravity and of the mean
   field of a gas of the particles $\chi$ (the average field that the particles of the gas create and feel): the four bound
   states of Krein charge $-1$ (the particles $\chi$) are even under it and the four of Krein charge $+1$ are odd, so the
   mean field of the gas cannot mix the two signs of the indefinite charge. $\mathsf{R}_2$ maps the bound states of one
   Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
9. *The planes of Horava and Witten.* In M-theory (the eleven-dimensional theory whose limits include the superstring
   theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional planes
   left in place by the reflection are mirror surfaces (property 1); each carries one $E_8$ gauge group while gravity fills
   the bulk. As in UM-3, the gauge fields live on the mirror surface and gravity in the bulk; unlike UM-3, the two sides of
   each plane are identified (one physical side).

**What is not a fold.**

* *The tips* $z = 0$ and $z = \pi$ (mod $\pi$): the mirror exchanges them within a period, but there the warp factor vanishes,
  $g_{x_0x_0}$ diverges, and they lie at an infinite proper distance; they carry no thin source.
* *A smooth maximum of a warp factor*, such as $1/\cosh^2(H\sigma)$: mirror symmetric and largest at $\sigma = 0$, but without a
  kink and without a thin source.
<!-- end fold definition -->

## 0. Exact restart procedure

### 0.20 STATE 2026-10-25 evening: UM-4 corrected after three independent referees — START HERE

The first version of UM-4 (commit `6f076ab`, 0.19) was pushed on the order "push all to repo NOW; verify repo, then continue all
stages and do not stop" (2026-10-25, 17:31 PDT) and verified from a fresh clone (17:32 to 17:47 PDT: every module under
`timeout -k 5 423`, the Kohn-Sham module in its four parts from scratch, 185/185 checks, the outputs equal to the committed ones
apart from run times). Three independent referees (Claude agents of the session: gravity and propagation; dirac16complex and dark
matter; cosmology and the documents) then reviewed it; every finding was checked independently before it was accepted, and the
confirmed ones are corrected in the commit of this round (listed in `claude_failures.md`, J4 and J5). UM-3 is unchanged. What
changed in UM-4:
* Causality: "nothing crosses the bulk faster than light" holds for signals at fixed extra times (FE-83, `um4_causality.py` C1);
  a null line that also moves along an extra time arrives earlier, down to Delta x4 = 0, and the four time-like directions allow
  closed time-like curves (C4). Around an expanding fold the bulk light cone is wider wherever the expansion rate falls
  (a4'' = -(1 + q) H_4^2 < 0, today included); the largest advance over the Hubble distance today is 4.4e-94 at H = 2534 GeV.
* The bulk graviton: its three vector polarisations h_(mu r) (one index along an extra time) are ghosts (`um4_bulk.py` B11), not
  emitted by the matter of the fold at the linear order (OPEN beyond it); the gravitational waves keep only + and x.
* The bounds on H (`um4_propagators.py` P4, P5): H > 2534 GeV from the invisible width of the Z (1.42 MeV); contact interactions
  between quarks and leptons 1083 GeV; the parameter rho 969 GeV (the squared masses shift by -m0^4/(3 H^2)); the W width into the
  bulk 0.85 MeV; Newton's law at 52 micrometres corrected by 2.6e-75.
* dirac16complex at the fold: the width is derived, Gamma = (2/e)(q_b^2/m_Psi) e^{-2F(u_b) m_Psi/H} (`um4_spectra.py` U3, U4;
  `um4_kohnsham.py` K8); dark matter must live longer than 160 Gyr = 11.6 t_0 (Audren et al. 2014); the bound on omega_b for every
  binding (U6): 4.3e8 GeV at q_b/omega_b = 0.1, 2.5e6 GeV at q_b = m_Psi/2, 1.2e4 GeV at 0.99 m_Psi, 2.2e3 GeV at 0.999 m_Psi.
* The thermal history (`um4_thermal.py`): the unitarity mass of a thermal relic is 9.69e4 GeV (integrated to convergence), so a
  thermal relic needs q_b > 0.906 m_Psi (T7); the convective current annihilates with sigma v ~ v^4 (`um4_krein.py` KR9, T3); a
  binding by the Higgs portal (T8) or by the gluon condensate (T9) couples chi to nucleons far beyond the LZ limit: no portal of the
  action binds chi without a nucleon coupling (OPEN); the helium abundance with the ad hoc vacuum and the energy of the ad hoc vacuum
  require its decay rate a40 > 4.8e-16 (v_A/v)^2 GeV (T6).
* The gas of chi: its symmetric occupation is a saddle of the first-order energy (KR8); the pair amplitudes are basis independent
  singular values (KR6, KR7); the chirality-blind convective current creates ghost pairs only at the next order in the momentum
  (relative rate 0.0089 k^2/m_Psi^2, KR9).
* The definition of the fold writes out the author's Dirac matrices (FD-13, checked by `um4_geometry.py` G11) and gives
  Lambda_RS = -6 k_RS^2 for the brane of Randall and Sundrum (FD-8); no document refers the reader to another file.
* Inflation of the fold in the regime of general relativity at H = 2534 GeV: H_inf < 253 GeV (rho^{1/4} < 3.3e10 GeV).
* The tools: `symbols_close.py doc NAME` puts the entries that only the definitions of listed entries need into the list "Further
  symbols" of the document, so that the list after a display names only the symbols of that display.
* 189 checks in 20 programs, all passing (`um4_geometry.py` 11, `um4_krein.py` 9, `um4_thermal.py` 9; the rest unchanged); the
  documents rebuilt (md, tex, pdf) without overfull boxes.
* Verified from a fresh clone of commit `2bf1568` (2026-10-25, 20:48 to 21:06 PDT): every module under `timeout -k 5 423`, the
  Kohn-Sham module in its four parts from scratch, 189/189 checks (the longest calculation 260 s); the 40 output and report files
  equal to the committed ones value by value apart from run times; the symbol and fold checks passed; every document rebuilt
  identically (md, tex, pdf), apart from the run time of the matrices program quoted in `dirac matrices` (39 s against 37 s).

How to continue: as in 0.19 below (the Markdown files `universe_model_4/NAME.md` are the sources of the documents; the order of the
modules is in `universe_model_4/README.md`: `um4_propagators.py` before `um4_foldsources.py`, `um4_causality.py`, `um4_spectra.py`
and `um4_primordial.py`; `um4_spectra.py` before the assembly of `um4_kohnsham.py`; `um4_spectra.py` and `um4_krein.py` before
`um4_thermal.py`).

Open (stated in every document): the origin and tuning of the tension; the origin of the holding pressure along the extra times; the
projected Weyl tensor of the bulk for an expanding fold with dust; the ghost vectors of the bulk graviton beyond the linear order; a
gauge principle that removes the momentum along the extra times; a binding of chi to the fold without a nucleon coupling and a
non-thermal origin of its abundance (or a binding stronger than about q_b = 0.9 m_Psi for a thermal relic); the classical stability
of the gas of chi (the two imaginary frequencies of its truncated response) and a unitary coupling of dirac16complex at the fold;
the inflaton. Nothing is running; the next step is the author's next order.

### 0.19 STATE 2026-10-25: UM-4 complete (the order of 13:15 PDT, 0.18) (superseded as the start by 0.20)

UM-3 first. A fresh clone of commit `c5a93c4` (the last commit of UM-3) was verified on 2026-10-25 from 13:38 to 14:30 PDT: every
module run under `timeout -k 5 423` (the Kohn-Sham module in its six parts), 223/223 checks, and the 44 output and report files equal
to the committed ones apart from run times (compared value by value by a script of the session). After that UM-3 was not changed.

UM-4 is in `universe_model_4/` (its own `code/`, `docs_src/`, `tools/`, `outputs/`, `reports/`, the documents in md, tex and pdf, and
its `README.md`). What it is:
* The metric: the author's metric with the time warped like the other six directions of the fold, g_{x4x4} = -(sin^2 z)^(1/6)
  (z = 6 H x0); proper chart ds^2 = d sigma^2 + e^{-2H|sigma|} [e^{2 a4} dx^2 - dx4^2 - e^{-2 a4} b4^2 dx5^2]. Among the static warps
  of the author's form only equal rates are vacua of gravity (`um4_geometry.py`, G10).
* Gravity: Einstein gravity in eight dimensions with Lambda = -21 H^2 (the author's Lovelock weights of the Gauss-Bonnet and cubic
  terms set to zero: the only choice with gravitons on the light cone on every background, `um4_gravity.py`, L1 to L4). The static
  block is AdS8 (curvature -H^2 in all 28 planes), the fold a pure tension kappa lambda_F = 12 H, lambda_F V_* = 30 H^2 M_red^2;
  the fold obeys the Einstein equations of seven dimensions with kappa_7 = 5 kappa H/2 (corrections (12/25)(a4'/H)^2).
* Propagation: the gauge fields of the Standard Model in the bulk (the photon by the order, ASSUMED for all); every massless field of
  the bulk has a massless mode bound to the fold at the speed of light and a continuum of massive modes from zero mass (`um4_bulk.py`,
  B1 to B10); the photon a transverse wave of helicity +-1, the gravitational wave transverse traceless with + and x (helicity +-2);
  nothing crosses the bulk faster than light (`um4_causality.py`, C1 to C4); Newton 1 + 0.3395/(Hr)^5, Coulomb 1 + 0.4244/(Hr)^3;
  the W and Z are resonances of the bulk, and the invisible width of the Z bounds H > 2534 GeV (`um4_propagators.py`, P5).
* dirac16complex: the states at the fold are resonances (omega_r = omega_b (1 - H/(2 q_b)), Gamma ~ 0.136 m_Psi e^{-2F m_Psi/H});
  dark matter needs m_Psi/H > 1.1e3 (q_b = m_Psi/2), so omega_b > 2.43e6 GeV; no thermal relic above 8.87e4 GeV (unitarity); the
  Higgs-portal binding allows long-lived, undetected chi only for H < 2.1 GeV: the binding and the origin of the dark matter are OPEN.
* The documents: `MODEL`, `FIELD_EQUATIONS` (IN-1 to IN-16, FE-1 to FE-88), `SOLUTION` (S-1 to S-28), `PROPAGATION` (P-1, P-2, the
  answer to the order), `ANALYSIS` (A-1 to A-8: the x0 mass mechanism, dark matter, dark energy, the open questions, what was left out,
  UM-4 compared with UM-3), `PROVENANCE`, `dirac matrices`; every document self-contained, every symbol of every display defined after
  it, the definition of the fold in every file that uses the word. 185 checks in 20 programs, all passing.

How to continue (the scratchpad of the session that built UM-4 is not part of the repository): the Markdown files
`universe_model_4/NAME.md` are the sources of the documents. After an edit run, from the repository root and each under
`timeout 423`: `python universe_model_4/docs_src/registry.py` (after a change of the registry), `python
universe_model_4/tools/make_inventory.py` (after a change of a tagged display of `FIELD_EQUATIONS.md`), `python
universe_model_4/tools/symbols_tool.py sync NAME`, `python universe_model_4/tools/symbols_tool.py expand NAME`, `python
universe_model_4/tools/symbols_close.py doc NAME`, `python universe_model_4/tools/inline_symbols.py NAME --add`, `python
universe_model_4/tools/symbols_tool.py check`, `python universe_model_4/tools/fold_block.py insert` and `check`, and `python
universe_model_4/tools/build_docs.py`. A module is rerun with `timeout -k 5 423 python universe_model_4/code/NAME.py` (the order of
the modules and the parts of the Kohn-Sham module are listed in `universe_model_4/README.md`).

Open (stated in every document): the origin and tuning of the tension; the origin of the holding pressure along the extra times; the
projected Weyl tensor of the bulk for an expanding fold with dust; a gauge principle that removes the momentum along the extra times;
a binding of chi to the fold without a nucleon coupling and a non-thermal origin of its abundance; the classical stability of the gas
of chi and a unitary coupling of dirac16complex at the fold; the inflaton. Nothing is running; the next step is the author's next order.

### 0.18 ORDER 2026-10-25 13:15 PDT: a new universe model UM-4 in which the time x4 is warped (superseded as the start by 0.19)

The author's order of 2026-10-25, 13:15 PDT (verbatim): "Since in the UM-3 model
anything that propagates in the bulk outruns light on the fold,
and bulk scalars and photons faster than light ,
my model is physically incorrect.
You must find a new metric model in which x4 is warped like the other directions,
both photons and gravitons  actually propagate at c in the bulk,
photon waves are transverse spin-1 phenomena,
Gravitational waves (ripples in spacetime) are spin-2 phenomena
(because they originate from the rank-2 stress-energy tensor)
and possess the following
Polarization Modes: the spin-2 nature of gravitational waves manifests physically as characteristic "plus" (+) and "cross" (×) polarization modes that stretch and squeeze space perpendicularly.
Find the best model and re-calculate and re-document;
however keep UM-3 and create a new UM-4,
placed in new folders."

Sequence chosen (reported to the author at 13:16): (1) the third referee round of UM-3 (0.17) was finished, rerun, verified and
pushed first, so that UM-3 is kept as a correct record; after that UM-3 (`universe_model_3/`) is NOT changed by the UM-4 work;
(2) UM-4 is built in the new folder `universe_model_4/` (its own `code/`, `docs_src/`, `tools/`, `outputs/`, `reports/` and the
documents in md, tex and pdf), with the same rules as UM-3: every document self-contained (every equation written in it, every
symbol defined in it, no reference to another file for an equation or a definition), every computation under `timeout -k 5 423`,
push as soon as verified, the private inputs never committed, the coordinates x0..x7 never relabelled.

The plan of UM-4 (to be refined as the work proceeds; a step is done only when its checks pass):
* The metric: the author's metric with the time warped like ordinary space and the extra times, g_{x4x4} = -(sin^2 z)^(1/6)
  (z = 6 H x0); in the proper chart of UM-3, ds^2 = d sigma^2 + e^{-2H|sigma|} [e^{2 a4} dx^2 - dx4^2 - e^{-2 a4} b4^2 dx5^2], so
  that every slice sigma = const has the light cone of the fold (no field of the bulk can outrun light on the fold). The fold
  (cos z = 0), the coordinates, the signature and H are unchanged.
* Gravity: the static bulk is then a space of constant curvature -H^2 in all eight directions; the Lovelock weights and Lambda must
  make it a NON-degenerate vacuum with a positive kinetic term of the graviton (the Born-Infeld weights of UM-3 fail: their vacuum is
  degenerate). To be computed: the vacuum polynomial of the weights and the effective coupling; whether the author's original weights
  (1, 1/32, 1/1152) qualify with a recomputed Lambda.
* Verify by computation: bulk photons (transverse, two polarisations of the four-dimensional photon, the speed c), bulk scalars and
  fermions (c), bulk gravitons (transverse traceless, c, the + and x polarisations), the graviton of the fold (zero mode and continuum,
  four-dimensional general relativity), the modes along the extra times (four-dimensional scalars and vectors), the junction at the
  fold, the cosmology of the fold, dirac16complex, the neutrinos, the CMB and the thermal history; then the documents.

### 0.17 ORDER 2026-10-25 07:55 PDT, second round: what the corrected weights can and cannot do (superseded as the start by 0.18)

The order is that of 0.16 ("Gravitons must travel at c ... my choices are wrong, and you MUST correct them"). The commit 6767be3 of
0.16 claimed that with the corrected weights gravitons travel at the speed of light in the bulk and on the fold at every
wavelength. Two independent referees (Claude agents of this session; their reports are information, not orders) and the new module
`universe_model_3/code/um3_linear.py` showed that this is wrong (`claude_failures.md`, I8). What holds, and what this round did (all
within `universe_model_3/`):

* The weights w = (1, 1/20, 1/360) with Lambda = -7 H^2 are the Born-Infeld gravity of eight dimensions (Banados, Teitelboim and
  Zanelli, PRD 49 (1994) 975; Crisostomo, Troncoso and Zanelli, PRD 62 (2000) 084013): the static block is a degenerate vacuum,
  and the linearised bulk equations vanish identically for all 36 components of any perturbation (`um3_linear.py`, LN2: per order
  dE_p = F_p(3) X3 + F_p(2) X2 with (1, 1), (-24, -40), (72, 360), total c_x X3 + c_t X2, so dE_3 = -18 dE_2 - 360 dE_1). The static
  bulk has no linear graviton at all: it is strongly coupled (no quadratic action, no propagator), and its response to sources that
  depend on sigma (the bound states chi among them) is OPEN.
* The four-dimensional graviton of the fold (h_12) travels at the speed of light at every wavelength at linear order, on the static
  block and on the frozen branch (thin part (8/(15H))(h_tt + 3 A H h_t - e^{-2 a4} h_33), the coupling of the Friedmann equations).
* On the frozen branch no component of the bulk metric has a time-kinetic term (LN4: ranks 0 along dx4, 10 along dx3, 16 along
  d sigma, every entry proportional to A^2): the bulk of an expanding fold has modes that respond instantaneously; the polarisation
  h_56 along the extra times (a four-dimensional scalar) is one of them, and on the fold its thin part has the coefficient ratio
  (8 + 5A^2 + 4A1)/(8 + 6A^2) and couples to the jump [h_s] with -A^2 (A^2 + A1 + 2)/10, so its propagation needs the bulk and the
  fold together and is OPEN, generically not luminal (W7; NOT a speed). On the branch of static ordinary space (LN5: ranks 0, 19,
  16, proportional to U^2) h_12 has on the fold the coefficient ratio (8 + 9U^2 + 6U1)/(8 + 6U^2) and the coupling
  -U^2 (U^2 + U1 + 2)/10 to [h_s] (propagation OPEN).
* No-go (W3): at the static block the warped minus the time entry is -6 c_t H^2 for every pair of weights; bulk gravitons at the
  local speed of light need w2 = 18 w3 (c_t = c_x = c_tx = 1 - 360 w3), and then c_g^2 - 1 = 5 c_tx/(32 - 22 c_tx) for the long
  wave of the fold, zero only for c_tx = 0 (positive for 0 < c_tx < 16/11; kappa K_44 = (16 - 11 c_tx)/(30 H), so c_tx < 0 is a bulk
  ghost and c_tx > 16/11 gives K_44 < 0); on the line c_t = 0 the bulk keeps c_x = 4/5 - 16 w2. No weights and Lambda give gravitons at c both in the bulk and on
  the fold: the cause is that the time x4 of the author's metric is not warped. A metric that warps x4 might remove it; changing the
  metric is the AUTHOR'S DECISION (offered to him, not done).
* The fold fluid: the pressure of the baryons along the extra times is ASSUMED (-rho_b gives Delta_r = 0.793 rho_c, 0 gives 0.842,
  +rho_b gives 0.891; with 0 a free volume would drift G 7973 times the bound of lunar laser ranging, SR5, SR6). In the early
  universe the holding pressure is enormous: q_hold/lambda_F is about A^4/8 (A = H_inf/H); with H at most 4.63e-13 GeV (the
  estimate SL5) an inflation at H_inf = 4.43e13 GeV has A >= 9.6e25 and needs q_hold of at least about 2e51 rho_v, 1e103 times the
  tension (a lower bound, growing without limit as H gets smaller); A > 1 above T = 574 GeV (PR4): OPEN. Higgs inflation
  (PR5) needs a curvature coupling xi_H that IN-11 does not contain: an extension. Newton's constant, the squares of the gauge and
  Yukawa couplings and the quartic Higgs coupling are divided by Z (not "every coupling").
* Code: `um3_linear.py` (new, 5/5; the jet code is the referee's, adopted after review, imports nothing from UM-3); `um3_weights.py`
  W3 (the no-go) and W7 (both vacuum branches, both polarisations); `um3_bulk.py` B5; `um3_fold.py` J7 (the extra-time pressure
  required); `um3_series.py` SR5 and SR6 (the three baryon pressures); `um3_primordial.py` PR4 (reads `outputs/superluminal.json`:
  run `um3_superluminal.py` first) and PR5; docstrings of geometry, foldsources and stabiliser qualified. Run order: dirac_matrices,
  geometry, fold, weights, linear, bulk, fields, spectra, neutrino, background, series, flavour, thermal, cosmology, kohnsham (six
  parts and `assemble`), foldsources, stabiliser, krein, extratimes, superluminal, primordial, numass; each under
  `timeout -k 5 423`: 223 checks in 22 modules.
* Documents (md, tex, pdf): all six revised (FIELD_EQUATIONS: the weights paragraph with what the correction can and cannot do,
  FE-35, FE-63 to FE-65, FE-69, FE-70, FE-72, the fold fluid; SOLUTION, ANALYSIS, MODEL, PROVENANCE and STABILISER accordingly).
  The symbol lists of every document are closed: every symbol that a meaning uses is listed in the same document (checked by
  `symbols_tool.py check`), and every symbol of the prose is listed (in the new list "Further symbols" at the end of each document)
  or defined in words where it is used (`tools/inline_symbols.py`; `tools/symbols_close.py` and `tools/closure_check.py` add the
  entries). The definition of the fold notes that FD-11 and FD-12 were added on 2026-10-25.
* A third independent referee (13:04; information, not orders) confirmed the physics (the Born-Infeld weights, the vanishing
  linearised operator at the static block, the no-go inputs, h_12 luminal on the frozen branch, the numbers of the reports) and found
  wording errors, all corrected before the commit of this round: "no graviton of the bulk travels faster" now says the STATIC bulk
  everywhere (the bulk of an expanding fold has instantaneous modes); "up to 1e103" is "at least 1e103" (about A^4/8 times the
  tension); the h_56 and static-space h_12 ratios are coefficient ratios, not speeds (propagation OPEN); FE-69 text "= Pi_gw" (no
  kappa); 5 c_tx/(32 - 22 c_tx) qualified (W3 now checks: zero only at 0, positive exactly on (0, 16/11), kappa K_44 H =
  (16 - 11 c_tx)/30); the common value is called c_tx (registry key `ctxw`; c is the speed of light); the criterion of the correction
  is labelled ASSUMED (the unique values DERIVED); the reason why the static block has no linear part is the identity
  sum alpha_p E_p + Lambda = -(1/(5760 H^4)) delta R-bar R-bar R-bar with the shifted curvature R-bar = R + H^2 delta, nonzero at the
  static block only in planes that contain x4 (new display after FE-70 in FIELD_EQUATIONS, registry key `Rbar`); the Born-Infeld
  statement holds up to the Euler density H^-6 L_(4)/2880 (topological in eight dimensions); FE-68 assumes a4 = 0 by the unit of x3;
  the dark matter has no pressure along the extra times in a dilute gas (on shell L = +(lambda_Psi/2)(Psibar Psi)^2 with the contact
  term); Delta_r and q_SM labelled ASSUMED for the baryons; "the two expanding branches" is "the two vacuum branches with a changing
  a4 or b4"; the BG4 and PR6 texts no longer say "every coupling"; PR4 says "A is at least".

OPEN after this round, in addition to 0.16: the strongly coupled bulk (its response to sources, the gravity of the bound states
beyond the thin-source approximation, its quantum theory), the modes without a time-kinetic term on the two vacuum branches with a
changing a4 or b4, the
holding pressure of the early universe, and the order "Gravitons must travel at c" in the bulk, which the author's metric does not
allow (the author's decision on the metric). The frozen pre-UM-3 records (`Revision/`, `universe_model_2/`, `handoff/`,
`provenance/` and the like) and the author's notebooks are unchanged.

### 0.16 ORDER 2026-10-25 07:55 PDT: the corrected Lovelock weights and the cosmological constant (superseded as the start by 0.17)

The author's order of 2026-10-25, 07:55 PDT (verbatim): "Regarding your statement: "Gravitational waves. The speed c_g² = (96 +
83ε_r)/(96 + 82ε_r) holds only for wavelengths much longer than 1/H; shorter waves are slower than light. Your 2.74 c premise came
from leaving out the fold's own Lovelock term. Gravitons in the bulk still travel at √5 c.", I do not understand : "Your 2.74 c
premise came from leaving out the fold's own Lovelock term. ", because I did not presume 2.74 c anywhere. I assume this is a
deduction from other assumptions. Please explain. This needs to be fixed because Gravitons must travel at c. If these incorrect
claims come from my choice of the Lovelock couplings and my choice of the cosmological constant Λ THEN my choices are wrong, and
you MUST correct them."

The explanation given to the author: the 2.74 c was Claude's own deduction (first written in 431d53d, quoted in the order of
03:21), the long-wavelength speed computed from the bulk alone; calling it "your premise" was wrong (`claude_failures.md`, I7).
The speeds came from the author's weights. What was done (all within UM-3, `universe_model_3/`):

* `code/um3_weights.py` (new, 8/8, about 53 s): for any weights, a transverse-traceless gravitational wave of the static block
  obeys FE-68 with the time-kinetic coefficient c_t = 1 - 40 w2 + 360 w3 and the gradient coefficient c_x = 1 - 24 w2 + 72 w3
  (the author's 1/32, 1/1152: c_t = 1/16, c_x = 5/16, so the local speed sqrt 5); the long wave collects a bulk and a thin part,
  kappa K44 - kappa K33 = -c_t/(12 H) for every pair of weights (FE-69). Gravitons travel at c everywhere only if c_t = c_x = 0 [WRONG
  as stated, corrected in 0.17 and `claude_failures.md` I8: the graviton of the fold travels at c at linear order, the bulk has no
  linear graviton at all, and no weights give gravitons at c both in the bulk and on the fold]:
  the unique weights w = (1, 1/20, 1/360), and then kappa K44 = kappa K33 = 8/(15 H), c_g = 1 at every wavelength. With them the
  static block has the entries 7 H^2 along the warped directions and the time (per order 15 - 9 + 1 and 21 - 21 + 7; FE-70), so
  Lambda = -7 H^2 makes it a vacuum: THE STABILISER VANISHES (it was a consequence of the original weights). The fold source of the
  static block is a pure tension, kappa S = -(32/5) H (FE-32); a bulk without a source has static ordinary space (A = 0) or frozen
  extra times (U = A) at every instant (FE-66: kappa T^4_4 = A^3 (A - U)^3 H^2, flow 3 A^2 U (A - U)^2 H^2 sgn(sigma)); on the
  branch of frozen extra times the bulk is an exact vacuum for every expansion history and the fold obeys exactly the Friedmann
  equations of general relativity with 8 pi G_N = kappa_7/V_*, kappa_7 = 15 kappa H/16 (FE-33, FE-71); the author's vacuum is no
  longer a solution (FE-31).
* The fold fluid must hold the volume of the extra times (FE-65, FE-72: the pressure q_hold = -Delta_r, Delta_r = 0.793 rho_c
  today); without it Newton's constant would have fallen by 15.8 since nucleosynthesis and would drift 6800 times faster than
  lunar laser ranging allows (`um3_series.py`, SR5, SR6). The static block is a degenerate vacuum (the static family gives
  (y - 1)^2 (y - 7) and 7 (y - 1)^3), so the bulk response to sources that depend on sigma starts at second order (the operator
  X of SR2, growth e^{3 H |sigma|}): OPEN.
* The primordial era is an inflation of the fold with the volume of the extra times held fixed (`um3_primordial.py`, 7/7:
  H_inf < 4.43e13 GeV for r < 0.032; with the fold's own Einstein-Hilbert term the Higgs field can be the inflaton, xi_H = 16195
  for lambda = 0.1294, n_s = 0.9636, r = 0.0040; a free volume would make the couplings fall like e^{-3N}).
* Every module was revised where the weights enter and rerun under `timeout -k 5 423` (2026-10-25, 10:13 PDT on): 218 checks in
  21 modules, in the order dirac_matrices 55, geometry 23, fold 13, weights 8, bulk 11, fields 16, spectra 5, neutrino 5,
  background 7, series 6, flavour 4, thermal 6, cosmology 6, kohnsham 9 (six parts and `assemble`), foldsources 6, stabiliser 9,
  krein 7, extratimes 5, superluminal 5, primordial 7, numass 5 (`um3_weights.py` must run after `um3_fold.py`). Checks of the
  original weights were replaced: geometry G4 (the vacua of the corrected bulk), bulk B5 (the graviton lives on the fold), fold J5,
  J7 (the frozen fold source, the Friedmann equations), foldsources F1 to F6 (the graviton at the speed of light, the fold fluid a
  tension), series SR1 to SR6 (the degenerate static block, the seven-dimensional Einstein brane, the volume held by the fold
  fluid), background BG0 to BG3, stabiliser ST3, ST8 and the new ST9 (the corrected weights remove the stabiliser), primordial PR0,
  PR4, PR6, extratimes EX3.
* Documents (md, tex, pdf): FIELD_EQUATIONS (new FE-68 to FE-72; IN-7, FE-31 to FE-33 and FE-63 to FE-66 rewritten), SOLUTION,
  ANALYSIS, MODEL, PROVENANCE, and STABILISER rebuilt as the record of the stabiliser and of its removal (SB-1 to SB-19; its
  verdicts are given for the original and for the corrected weights). The definition of the fold now carries the corrected weights
  and FD-11, FD-12 (the junction conditions, the pure tension).
* Two independent referees (STABILISER; the open questions) found 16 and 19 problems; all are corrected (`claude_failures.md`,
  I7): among them, the stability of the dilute gas of chi is not decided, the dense gas turns unstable where the partner level
  reaches the continuum of the box (not converged), the eight-dimensional metric has closed time-like curves, the electron bounds
  require q_b/H > 9.7e13 to 4.3e15 if the loops make the electrons faster (8.7e12 to 3.9e14 if slower; the sign is not
  derived), so H < 5e-13 to 7e-14 GeV, DESI with NuFIT 6.0 gives m_l < 23 meV (the inverted ordering
  disfavoured, not excluded), and P(nu_mu -> nu_e) = 0.0478 at delta = 212 degrees. `um3_weights.py`'s first run was killed at
  423 s (I6).

OPEN after this order: what produces the holding pressure q_hold; the response of the degenerate static block to sources that
depend on sigma (strongly coupled); the classical stability of the gas of chi (exact flat directions; the truncated response is
not decisive) and the convergence of the dense-gas instability; unitarity with chirality-blind couplings (necessary, not
sufficient); the closed time-like curves of the signature (4,4) and the gauge principle that removes the momentum along the
extra times; the fine tuning of the tension of the fold (as severe as the cosmological-constant problem).

Superseded statements of 0.15: the results of 03:21 (c_g^2 = 83/82, (96 + 83 eps_r)/(96 + 82 eps_r), the bound on eps_r, the
fold fluid fed by the bulk) and the verdicts of 05:09 on the stabiliser hold only for the original weights; of 03:23, "the dilute
gas is stable" (not decided), "group velocity at most 1.0045" (1.0046; 1.0093 for H = 0.1 m_Psi), "q_b/H > 4e10" (above),
"n_S - 1 = 2.5 in the author's vacuum" (a record: the author's vacuum is not a solution any more), "H_inf < 4.7e13 GeV"
(4.43e13), "Higgs inflation excluded by induced gravity" (possible: the fold has an Einstein-Hilbert term of its own) and
"m_1 < 4.12 meV" (m_l < 23 meV). The frozen pre-UM-3 records (`Revision/`, `universe_model_2/`, `handoff/`, `provenance/` and
the like) and the author's notebooks are unchanged.

### 0.15 ORDERS 2026-10-25 03:21 TO 05:09 PDT: the sources of the fold, the open questions, the definition of the fold, the stabiliser (superseded as the start by 0.16)

The author's orders of 2026-10-25 (all within UM-3, `universe_model_3/`):

* 03:21: "Fix or handle Sources on the fold. The fold needs a thin fluid and an Einstein–Hilbert term of its own. Without the
  latter, bulk gravitons would travel 2.74 times faster than light. push". Done: `code/um3_foldsources.py` (6/6) computes the
  graviton term that the Gauss-Bonnet and cubic Lovelock terms give the kink of the fold (the four-dimensional gravitational wave
  then moves with c_g^2 = 83/82, still too fast), the speed with the induced Einstein-Hilbert term, c_g^2 = (96 + 83 eps_r)/(96 +
  82 eps_r), and the bound eps_r < 1.344e-13 from GW170817; the gravity that the fields of the fold induce (Sakharov,
  N_ind = 4(1 - 6 xi_H), cutoff 3.75e19 GeV); the fold fluid as a tension plus 1/62 pressureless matter fed by the bulk.
  Documents: FE-63, FE-64, FE-65 (FIELD_EQUATIONS), the section "The sources of the fold" (SOLUTION, S-30).
* 03:23: analyse and answer the open questions: the Krein norm (`um3_krein.py`, 7/7: the vacuum and the dilute gas are stable,
  the dense gas grows, the chiral fold couplings produce ghosts, so UM-3 with them is not unitary; FE-67), the extra times
  (`um3_extratimes.py`, 5/5: tachyonic, the restriction consistent but unstable, a gauge principle needed), superluminal chi
  (`um3_superluminal.py`, 5/5: c_b^2 = 1.190, group velocity at most 1.0045, front velocity 1, the bulk a shortcut, q_b/H >
  4e10 from loops), the primordial era (`um3_primordial.py`, 5/5: n_S - 1 = 2.5 in the author's vacuum, an inflationary era
  needed, H_inf < 4.7e13 GeV, Higgs inflation excluded by induced gravity), the lightest neutrino mass and the Dirac phase
  (`um3_numass.py`, 5/5: the phase drops out of every result; m_1 < 4.12 meV by DESI DR2; NuFIT 6.0 changes the results by at
  most 1.5 per cent). Documents: ANALYSIS "The open questions answered" (A-9 to A-15), SOLUTION S-31 to S-34, FIELD_EQUATIONS
  FE-67 and the paragraphs of FE-38 and FE-43.
* 03:54: define the fold, with examples meaningful for UM-3, and put the same definition in every file that uses the word.
  Done: `universe_model_3/docs_src/fold_definition.md` (documents) and `fold_definition.txt` (docstrings, JSON);
  `universe_model_3/tools/fold_block.py insert` puts it into every file, `check` verifies it word for word (Mathematica's
  `Fold[]` in the author's notebook `author_inputs/4+4.nb` is excluded; the frozen pre-UM-3 records are left unchanged).
* 05:09: give proper attribution to Claude for the stabiliser and document it completely for a clever newcomer, with
  provenance, verifying five points. Done: `universe_model_3/STABILISER.md/.tex/.pdf` and `code/um3_stabiliser.py` (8/8);
  FE-66 (the two constraints of the bulk equations, the Friedmann equation of the bulk). The verdicts: [1] couples only to
  gravity: exact on the static bulk, not when the universe expands (the bulk source then feeds the fold); [2] absent in the
  primordial era: true, but then it cannot appear later on its own (OPEN: its creation); [3] its value DERIVED, the existence
  of a bulk source DERIVED (no instant without a source has both rates below 0.477 H), a separate medium ASSUMED; [4] the
  static bulk and [5] warp and warp factor are explained with examples.

The standing rule of 2026-10-14 (no single calculation over 423 s) is kept: `um3_kohnsham.py` runs in six parts plus
`assemble` (claude_failures.md, section I); every command runs under `timeout -k 5 423`, `git push` under `timeout 120`.
Corrections made while checking the work of this round: the ghost assignment in the text of KR1 (the particles and the holes of
the modes of Krein charge +1 are the ghosts), the stated size of the NuFIT change (1.5 per cent, not "below one per cent"), the
tachyon threshold of EX2 (with the computed c_b^2), a string in the text of the gravity check G4 (a4'' was printed as a4), and
the claim that a sourceless bulk with frozen extra times would expand at a4' = H/sqrt 3: with frozen extra times the flow along
sigma, (3/16) A (1 + A^2) H^2 sgn(sigma), vanishes only at A = 0, where P = 1, so a bulk without any source cannot have frozen
extra times (ST8 now checks this, and the bound: the larger of |A| and |U| is at least 0.4771 on P = 0).

### 0.14 ORDER 2026-10-24 17:02 PDT: a major new revision (UM-3); every earlier stage PERMANENTLY STOPPED (superseded as the start by 0.15)

The author's order of 2026-10-24 (attachment, verbatim in its defining parts): "NOTICE AND WARNING: This is a major new
revision of this project. Immediately: permanently STOP all ongoing stages. STOP all ongoing stages NOW! Push what is
ready for pushing. Create a new folder for all of this new revision's files and subfolders. Always include this new
folder and all of its files and subfolders in the repo. Always push this new folder ...". Then: read, understand and
remember the new notebook `4+4.nb` ("eight, real-valued, 16 by 16, Dirac Matrices"); prove in a new provenance file
'dirac matrices.md' that the eight real 16 x 16 Dirac matrices used are those of `4+4.nb`, that they are real, satisfy
the anticommutation relations, that their scaled commutators generate Pin(4,4); re-derive the chiral projectors of its
subsection 'Left - Handed vs . Right - Handed Fermion Fields (Chirality) ; projection operators'; the coordinates
{x0,...,x7} of `Dirac_Einstein-Lovelock_4+4_Nash.nb` (Section DEFCHART); the NEW metric (b4[x4] -> b4[x4]^2):
diag(Cot[6 H x0]^2, E^(2 a4) Sin[6 H x0]^(1/3) (x3), -1, -E^(-2 a4) b4^2 Sin[6 H x0]^(1/3) (x3)), b4 a function of x4,
NEVER identically 1; the complete coupled field equations with gravity (Einstein-Lovelock), the Higgs doublet (with the
ad hoc vacuum (almightyAdHoc, v + h)/sqrt 2, almightyAdHoc = Exp[-2 a40 x4], a40 > 0, x4 >= 0), three generations of
lepton doublets and right-handed charged-lepton singlets, W1, W2, W3, B, three generations of quark doublets, gluons,
dirac16complex coupled to gravity through the canonical spin connection (never identically zero; verify) and, with its
left-handed and its right-handed part separately, to every Standard-Model field with a unique coupling each (only the
left-handed part couples to the Higgs field); new phenomenological interactions consistent with QCD and the
electroweak model; an accurate approximate solution with Kohn-Sham theory for dirac16complex; CMB, CNB, BAO; the metric
as a power series; the x0 mass mechanism (period pi/(6H)) and the dark-matter/dark-energy association analysed; every
equation and symbol defined in every document; md + tex + pdf; push as soon as verified; check and verify the repo.

State at the stop (2026-10-24): nothing was running (the cloud sessions of 2026-10-18/19 and their detached old
Stage-4 jobs no longer exist). Everything verified is on `main` (last commit 95a578d, W8 chapter 15). The unverified
work-in-progress snapshots stay where they are and are NOT merged: branches `w8-wip-2026-10-18` (ba1ba25),
`w8-wip-ch11` (f779889) and `w8-wip-snapshot` (da03f2f, W8 chapter 15 WIP). Permanently stopped: W8 (the textbook,
chapters 16-23 and 00 and the open cross-references of 17, 22, 23, 00), old Stage 4 (the static-metric Kohn-Sham
record and its reference/repeat/refined runs), old Stage 5 (pairs numerics), and all follow-ups of UM-2 (which stays as
it is, version 4). The author may later resume or restart the paused/stopped agents' tasks ("Then we may possibly
resume or re-start the PAUSED/STOPPED agents' tasks").

The new revision lives entirely in [`universe_model_3/`](universe_model_3/README.md) (UM-3); its README is the
authoritative state of the work. The author's notebook is kept read-only as `universe_model_3/author_inputs/4+4.nb`
(sha256 recorded there).

State at the end of the order (2026-10-25): every task of the order of 2026-10-24 is done, verified and pushed. The
documents of UM-3 (`MODEL`, `FIELD_EQUATIONS`, `SOLUTION`, `ANALYSIS`, `PROVENANCE`, `dirac matrices`; each as .md, .tex and
.pdf) are self-contained: every equation they use is written out in each of them; in the first five every symbol of every
display is listed after it and every equation tag cited in a document is displayed in that document (the symbol check
reports 0 problems). 167 checks in 13 modules pass: the Dirac matrices of `4+4.nb` (55), the exact geometry of the new
metric (26), the fold and its junction conditions (13), the bulk speeds (10), the fields (16), the spectra (5), the
neutrino sector (5), the background (6), the power series of the metric (6), the Kohn-Sham states of dirac16complex
(9), the neutrino flavours (4), the thermal history (6) and the CMB, CNB and BAO (6). Everything is committed on `main` (the branch `um3-wip-2026-10-25`, an unverified snapshot pushed while the last Kohn-Sham run was going, is
superseded by it and not to be merged). A fresh clone of commit 431d53d reproduced all 167 checks, every stored output
apart from the run times and the five documents byte-identical (2026-10-25). A restart needs nothing that is not
committed; nothing is running. What is still OPEN (the stability of
the indefinite Krein norm, the extra times, the primordial era, the dark energy against DESI DR2) is stated in SOLUTION
("What the solution does not settle") and ANALYSIS ("What the author may have left out"), which also lists what UM-3 had to
add to the author's specification.

### 0.13 ORDER 2026-10-18 15:42: STOP/PAUSE everything; UM-2 version 4 (organisation and presentation) — superseded by 0.14

The author's order of 2026-10-18 15:42 (attachment; binding text in `universe_model_2/docs_src/STYLE_V4.md`): "STOP or
PAUSE everything. We need to organize and present your solution better." Then the UM-2 tasks again ([1] precisely, but
approximately, solve the coupled field equations and document an accurate approximate solution with Kohn-Sham theory for
dirac16complex coupled to gravity and all Standard-Model fields, no Higgs particle; "For each and every field equation
that you use, you must clearly state, write down, document the field equation itself, define each and every symbol that
appears in the field equation EVEN if you have done this before"; analyse the approximate solution in concert with the
other field equations; md + tex + pdf ALWAYS; CMB, CNB, BAO; the metric as a power series; the x0 mass mechanism with the
uncertainty argument; every interaction in equation form; never refer the reader to another file; [2]-[4] push the model,
the field equations and the solution with provenance; check and verify; notify; [5] then the open stages; "Then we may
possibly resume or re-start the PAUSED/STOPPED agents' tasks"). 15:44: "do not forget to push results as soon as they are
completed and verified".

State (2026-10-18 ~17:00):
- Paused: W8 (the textbook). Verified chapters on main (01-05, 07, 13, 14); the unverified partial work of the stopped
  chapter agents is on branch `w8-wip-2026-10-18` (state note `handoff/drafts_2026-10-18/w8_wip_state.md` on that branch).
- Old Stage 4: its detached jobs (reference rerun of m1_L3_N1016_lamm2_T0 at grid level 2, canonical repeat at scf) were
  paused at 15:44 and then KILLED by a container restart at ~16:52; to be restarted (`scripts/ks_reference_solver.py
  --resume` on a fresh copy of the committed reference tree, about 4.5 h; the repeat and refined Rust runs from scratch).
- UM-2 version 4 in progress: `universe_model_2/tools/symbols_tool.py` (symbol lists generated from the registry
  `universe_model_2/docs_src/symbols/*.json` and checked: every display equation followed by the complete list of its
  symbols, one symbol one meaning), `docs_src/STYLE_V4.md` (rules S1-S6); the inventory of field equations FE-n and
  interaction terms IN-n (`docs_src/equations.json`), the notation (`docs_src/NOTATION.md`), the residuals of the
  approximate solution in every field equation and in concert (`code/um2_residuals.py`), then MODEL, FIELD_EQUATIONS,
  SOLUTION, ANALYSIS, PROVENANCE rewritten as version 4, built, verified from a fresh clone, pushed.

### 0.12 ORDER 2026-10-17/18: UM-2, the universe model with Kohn-Sham dirac16complex; then all open stages

The author's orders (the defining parts, verbatim): 2026-10-17: a new model of the Universe with Einstein-Lovelock gravity, the
dirac16complex field coupled through the canonical spin connection and to all Standard-Model fields except the Higgs particle,
new phenomenological interactions consistent with QCD and the electroweak models, CMB, CNB, BAO, the metric as a power series
of terms of decreasing magnitude, every mass from the x0 dependence of the wave functions with period pi/(6H), "Put each and
every interaction in equation form ... both markdown and latex file types; compile all latex to pdf. NEVER refer the reader to
some other file! PUT EVERY EQUATION you create and/or use IN THESE FILES", the analysis of the x0 mass mechanism and of the
association of dark matter (and dark energy) with dirac16complex. 2026-10-18 08:02: "correct universe model 2 to include
three neutrino flavors with mixing and flavor conversion. this is your first and only priority!! just kill Stage 4"; 08:24:
"NOT (B). USE (A)!!!" (three full generations). 09:48: "[4] Compute an accurate approximate solution ... (use Kohn-Sham theory
...) and push ... [5] Continue and Complete and push all stages that are still open, and do not stop. ... Check and verify
this repo. DO NOT TAKE SHORTCUTS. DO NOT BECOME LAZY. Finish and notify me that you have finished."

Status (folder `universe_model_2/`, README there; every document as .md, .tex and .pdf, each self-contained):
- Version 1 (2026-10-17, one generation) and version 2 (2026-10-18, three generations, three neutrino flavours with mixing and
  flavour conversion; commit ecca926) are superseded by version 3.
- Version 3 (2026-10-18, commits 15c2aab to 726997f; the fixes of its independent review in 815db9e, PROVENANCE item
  24; reproduced from a fresh clone at 815db9e: 235 of 235 checks, every stored number, documents byte-identical): the portal I13 (an x0-chiral vector coupling of dirac16complex to the baryon-number current, summed
  over the seven directions M != x0, where its bilinear is Hermitian; with B - L it would thermalise the right-handed
  neutrinos, Delta N_eff = 0.144) gives the dark-matter relic within the unitarity limit (Omega h^2 = 0.060 per species,
  G_A = 1.278e-9 GeV^-2, direct detection 0.16 of the LZ limit); the thermal history (g_rho, g_s, freeze-in of the fold
  bands, Delta N_eff = 0.001; the self-interaction bounded, G_lambda <= 2.3e-15 GeV^-2, ASSUMED), the coupled Kohn-Sham
  solution in ten environments (mean-field shifts at most 1.5e-6; the full block response with the hot plasma, delta ln f
  <= 1.1e-34), the metric as a power series with the Kaluza-Klein graviton tower and the radion, sigma_8; 235 checks, all
  passing.  Computations:
  `universe_model_2/code/um2_*.py` (each writes `outputs/` and `reports/`), documents built by `tools/build_docs.py`;
  `MANUAL_TASKS` gives the verification and the review as hand steps.
- [5] next: the open stages below, in this order, each verified, committed and pushed.
- [5] W7: the seven Revision documents are rewritten for the corrected metric and pass their publication tests (all seven,
  2026-10-18 in the cloud session); `Revision/README.md` folder table and the paragraphs on the spin connection, the good
  sector and the pairing were brought to the corrected metric (2026-10-18). The verify-mode rebuild of a registered PDF
  (`REVISION_PDF_REBUILD=1`, the gate's pdf-* steps) reproduces the .tex byte for byte on Linux, but the PDF bytes only with
  the TeX installation that registered them (on the author's PC): on the cloud container (TeX Live 2023/Debian) only
  `registeredSha256` and `provenancePdfCopy` fail. Re-register on the PC or accept the Linux build.
- [5] old Stage 4 (the static-metric Kohn-Sham record, `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL`): the document's
  sections 1 to 13.3 are written (commits 2d1aaff, b7b3b85); the student guide draft is in the session scratch. Running in
  the cloud session since 2026-10-18 12:09 (detached, 2 cores): (a) the reference rerun of m1_L3_N1016_lamm2_T0 (STAGE4_SPEC
  E4.14 b) by `python3 -B scripts/ks_reference_solver.py --resume --skip-self-tests --output <copy of the reference tree>`;
  (b) a complete canonical repeat of the five Rust subcommands and (c) the refined runs of spectrum, scf, excited, emt, for
  the checker's `--repeat` and `--refined` (the trees of 2026-09-30 in `stage4_keep/` on the PC are empty). Then: install
  (a), the summary pass, the checker with (b) and (c) into `python-check-report.json` (expected 63 checks, 0 failed), the
  errata line of `provenance/ERRATA_FIRST_EDITION_TEXTBOOK.md` (CURRENT_COUNTS_FORMAT), the notebook refresh (builder,
  route B, route A, audit), sections 13.4, 13.5 and 14, the abstract and the status text, the student guide, review, gate.
- [5] W8 started in the cloud session on 2026-10-18 (plan and per-chapter brief: `handoff/drafts_2026-10-18/w8_plan.md`,
  `w8_chapter_brief.md`; chapters 03 and 14 first; the old Stage 4 jobs resumed at 13:55 at the lowest priority).
- [5] W8 (the textbook for the corrected metric) and old Stage 5 (pairs numerics: the reference pairs run needs about 4.5 h
  on 24 cores and up to 167 GB in two workers without the E5.3 guard; the Rust pairs canonical, repeat and refined runs) are
  open. The textbook's notebooks are byte-reproducible only in the environment of `Revision/textbook/requirements.txt`
  (Python 3.14.5 on Windows; the PNG bytes depend on the zlib of Pillow). On Linux the PNG bytes equal the Windows ones when
  the pinned environment runs with a zlib-ng build in compat mode on LD_LIBRARY_PATH (2.2.5 or 2.3.3; the cloud session of
  2026-10-18 built one in its scratch and the notebook kit's byte-for-byte check passed).

### 0.11 ORDER 2026-10-17: UM-1, a new model of the Universe; then finish W5-W8 (superseded as the start by 0.12)

The author's order of 2026-10-17 (the defining parts, verbatim): "Stop all stages, even though the Stop hook says to
continue. push all you have to the repo, check and verify. I task you to : [1] ... create a new model of the Universe
that includes [a] gravity (Einstein-Lovelock gravity); [b] the dirac16complex quantized spinor field (which is
hypothesied to represent dark matter) ... coupled to gravity using a non-trivial canonical spin connection; ... new
CRITICAL interactions ... [c] photons; [d] neutrinos; [e] electrons; [f] quarks (only up and down ...); [g] the 3 weak
interaction gauge bosons ... However do NOT include the Higgs particle. ... CMB ... CNB ... BAO ... power series ...
CRITICALLY IMPORTANT: Mass will be given ... by appropriate wave function dependence on the space coordinate x0 ...
periodic in x0 with period π/(6H) ... [2] push your new, improved, model ... along with provenance (both .md and .pdf
files). [3] Compute the coupled field equations and push ... [4] Compute an accurate approximate solution to the coupled
field equations (use Kohn-Sham theory for the dirac16complex field, which couples to all other fields) and push ...
[5] Continue and Complete and push all stages that are still open, and do not stop. ... Check and verify this repo. DO
NOT TAKE SHORTCUTS. DO NOT BECOME LAZY. Finish and notify me that you have finished."

Status (folder `Revision/universe_model/`, README there):
- [1] + [2] DONE (68abc82): `MODEL.md/.pdf` (now version 1.1), `PROVENANCE.md/.pdf`.
- [3] DONE (0ccb2f9): `FIELD_EQUATIONS.md/.pdf`, `field_equations/derive_field_equations.py` 13/13.
- [4] DONE (bf60ba1, revised after two adversarial reviews): `SOLUTION.md/.pdf`, `solution/` (vacua.py, masses.py,
  ks_coupled.py = the record's Kohn-Sham reference solver with the portal mean fields, cosmology.py, solve_model.py),
  21/21 checks. Findings that CHANGE the model (MODEL.md 1.1): the only static vacuum is k0 = 1/(4 w2),
  Lambda0 = -3H^2/(4 w2); the effective Newton constant is G_N/G(k0), G(k0) = -5 + 9 w3/(2 w2^2); the block mode has
  lambda^2 = k0 G(k0) H^2/4 (attractive gravity <=> unstable block); the author's weights give G(k0) = -1 (repulsive
  gravity), so version 1.1 uses w3 = 1/768, Lambda = -24H^2 + dLambda and an ASSUMED stabiliser (OPEN: the Casimir
  energy of the cell). m_KK = 121 TeV (fitted to rho0), H = 23.4 TeV, dark matter = the odd bulk level 2.17492 m =
  50.9 TeV, fold band g_F = 8 (whole cell) or 4 (one half: OPEN which); one generation: N_eff = 2.99 needs the fold band
  to decouple in the QCD crossover (g_F = 8) or comes out 3.015 untuned (g_F = 4). Gate steps um1-* (both twins).
  Rebuild: the `python solution/ks_coupled.py JOB` runs of SOLUTION.md section 8, `python solution/solve_model.py`,
  `python tools/build_pdfs.py` (deterministic PDFs).
- UM-1 analysis and version 1.3 (2026-10-17, at the author's requests "analyze the x0 mass mechanism ... the validity of
  associating dark matter (and dark energy) with dirac16complex" and "fix the gaps"): `Revision/universe_model/ANALYSIS.md`
  (21 + 13 checks; commit 5c7dcae) and `GAPS.md` (4 checks; 20446aa); the PDF builder made independent of earlier builds
  (cd6c020).
- [5] W5 DONE (0aa3c29; see 0.10).  W6 DONE 2026-10-17 (see 0.10, the entry "W6 DONE").  W7 IN PROGRESS: LOVELOCK_GKD,
  DIRAC16COMPLEX00_FIELD_THEORY and KOHN_SHAM_DEFLATING_FIELD done earlier; PAIR_CREATION_PROOFS,
  DIRAC16COMPLEX_FIELD_THEORY and DARK_SECTOR_HYPOTHESES are being rewritten by the workflow `w7-documents` (scratch
  `w7/w7_documents.js`: one drafting agent per document - its block files in `handoff/drafts_2026-10-17/w7/`, the .md and
  its publication test with every content test passing -, an adversarial reviewer, a fixer); the lead then builds the
  PDFs in verify mode, registers them, pins the sha256 in the tests, and updates `Revision/README.md` (documents rows,
  the pairing row with T3 9/9, 12/12) and `Revision/SPEC.md` section 9.  Then W8 (the textbook: every chapter and
  notebook; first TEXTBOOK_SPEC R2/R3 for the corrected metric; notes in the scratch `w8/notes.md`), each committed and
  pushed.
- Restart material for W7 (2026-10-17): the drafts and fill scripts in `handoff/drafts_2026-10-17/w7/` (`D16.draft.md` +
  `fill_d16.py` + `d16_*.md`; `PAIR.draft.md` + `fill_pair.py` + `pair_*.md`); the tests carry the requirements.

### 0.10 ORDER 2026-10-16: the corrected metric (version 2); recompute every primordial object

The user's order (verbatim, the defining parts): "a diagonal form for the metric of the primordial gravitational field
is only self-consistent if all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO.  This
is not the case here.  I task you to: [1] find the simplest modification for the current metric of the primordial
gravitational field that is probably self-consistent with the the Einstein field equations.  [2] push your new,
improved, metric ... to the repo, along with provenance and a pdf file explaination of the issues and remedies.
[3] Recompute all primordial objects and push to repo; revise all concomitant documention and push.  [4] Continue and
Complete and push all stages that are still open, and do not stop."  And: read the user's notebook
`WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (repository root) only to understand the issue; "DO NOT employ either
its definitions or conventions".

The author's corrections of the same day (verbatim): "x0 is a hypothetical space-like coordinate. x4 is time. ... At
any rate, g44 cannot oscillate."; "'For 0 < z < π/2', is wrong. Here, -\infty < z < \infty. ... For now try to fix
your warped metric. Do not take time repairing the repo right now. that will come later."; "use Sin[6 H x0]^(1/3) =
( Sin[6 H x0] ^2 )^(1/6), and take the positive branch. this is what i always use in my Mathematica notebooks".

Version 1 (commit 7897829, WITHDRAWN): g44 = -Sin[6 H x0]^(1/3) (the time-warped metric).  For real z its lapse
oscillates in x0 and vanishes at z = n Pi; the PDF called x4 "the time direction, which may depend on x0", used z and y
before defining them and assumed 0 < z < Pi/2.

The answer, version 2 ([1], [2] again, DONE 2026-10-16): the corrected metric
diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0 real.  With g44 = -1
the mixed curvature of the family g00 = b4^(2p) E^(2 q a4) Cot^2, g_ii = E^(2 a4) (Sin^2)^(3 alpha), g_tt =
-E^(-2 a4) b4 (Sin^2)^(3 beta) is 18 H Tan z E^(-2 q a4) b4^(-2p) times alpha ((q-1) a4' + p u), beta ((q+1) a4' +
(p-1/2) u); the corrected metric keeps the warp of the extra times (beta = 1/6, alpha = 0, q = -1, p = 1/2).  No mixed
Riemann component; every off-diagonal component of E_(1), E_(2), E_(3) vanishes identically for all a4, b4 and every
real z; every diagonal component is independent of x0; the block (x0, x5, x6, x7) is E^(-2 a4) b4 times a space of
constant curvature -H^2 (x0 shrinks with the extra times); gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) +
(b4'/b4 - a4'/2) gamma^(x4); the history a4 = H x4, b4 = e^(4/3 H x4) needs a diagonal conserved source with p0 = p_t
growing as H^2 e^(2/3 H x4).  Alternative K (x0 grows with 3-space) is also diagonal at every order; the choice is the
author's (asked, not yet answered).  Files: `Revision/metric_warped/` (sympy 14/14, Wolfram 13/13, both with an exact
normal form for every real z; provenance `WARPED_METRIC_PROVENANCE.md`; frozen reference of the record of 04fa2e7 in
`reference_2026_10_14/`), `Revision/docs/METRIC_SELF_CONSISTENCY.{md,tex,pdf}` (version 2, registered, 15 pages,
warning-free; test `Revision/tests/test_metric_self_consistency_publication.py`, 18 tests), `Revision/SPEC.md`
section 1 (the corrected metric is current; version 1 and the metric of 2026-10-14 withdrawn), gate steps
metric-warped-sympy, metric-warped-wolfram, pdf-metric-self-consistency.

[3] Phases, released by the author on 2026-10-16 ("go ahead with the recomputation using the corrected metric"; until
then on hold: "Do not take time repairing the repo right now. that will come later"); each verified, committed and
pushed; every calculation under `timeout -k 5 423`; no agent job longer than 423 s; the work is done sequentially, in
the order R0, W1, W4, W2, W3, W5, W6, W7, W8 (W2 rebuilds the Lovelock tensors from
`gkd_lovelock/results/lovelock-tensors.json`, the output of W4):
R0. Repository repair: the automatic Stop-hook snapshot d02ff19 committed and pushed the author's
    `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` and its four `.mx` files, which were never to be committed.
    DONE 2026-10-16 at the author's request ("remove the notebook and .mx files in a new commit"): removed from the
    repository by a new commit (no history rewrite; they remain in d02ff19) and listed in `.gitignore`, so the
    Stop hook's `git add -A` cannot add them again; the files stay on disk.  Still open in R0: the W1 files below,
    committed in d02ff19 for version 1.
W1. `Revision/theory/`: RevisionFieldTheory.wl / verify_field_theory.wls (six parts) / check_field_theory.py and the
    scope checks for the corrected metric (the files committed in d02ff19 use version 1, f4 = Sin^(1/6), and must be
    redone: f4 = 1, Omega_x4 = 0, f0 = E^(-a4) b4^(1/2) Cot z, f_i = E^a4, f_t = E^(-a4) b4^(1/2) (Sin^2)^(1/12); the
    gravity term; EMT; conservation; exact solutions; quantisation; every real z, the (Sin^2)^(1/6) branch).
W2. `Revision/field_equations_a4/`: no off-diagonal component, the diagonal equations, the history's source,
    `ks_source/`.
W3. `Revision/lead_checks/`.
W4. `Revision/gkd_lovelock/`: the Rust monomial lists and verifications for the corrected metric.
W5. `Revision/kohn_sham/`: theory (the hidden-direction mode problem with the factor E^(-a4) b4^(1/2)), Rust solver,
    reference, cross-check, tip convergence, exx; `ks_source`.
W6. `Revision/dark_sector/`, `Revision/pairing/` (T1, T2, Q, T3), `Revision/notebooks/`.
W7. The six documents of SPEC section 10 for the corrected metric; READMEs; gate; provenance; index.
W8. The textbook (every chapter and notebook; the b4 work of 0.9 phase 9 is superseded and moves directly to the
    corrected metric) and the book PDF; retire the b4 supplements.
Status (newest last):
- W0 version 1 DONE and WITHDRAWN 2026-10-16 (commit 7897829).
- W0 version 2 DONE 2026-10-16: [1] and [2] as above.  KNOWN OPEN until W4: `gkd_lovelock/comparison/compare_with_author.py`
  (check revision-metric-spec-vs-curvature-json, also run by test_lovelock_gkd_publication) compares the FIRST matrix
  of SPEC section 1, now the corrected metric, with `gkd_lovelock/results/curvature.json`, which still holds the
  metric of 2026-10-14.  A fresh run on 2026-10-16 reports mismatches at (x0, x0), (x1..x3) and (x5..x7); the last
  three because curvature.json writes Sin^(1/3), which differs from (Sin^2)^(1/6) for Sin < 0.  The committed
  `author-comparison-report.json` is older (PASS against the SPEC before 7897829) and is regenerated in W4.
- W1 DONE 2026-10-16: `Revision/theory/` for the corrected metric, general a4, b4 and every real z (exact zero test
  modulo Cos^2 + Sin^2 - 1, w^12 - Sin^2 with w = (Sin^2)^(1/12), sign(Cot z)^2 - 1; no PowerExpand).  Wolfram
  `verify_field_theory.wls` 86/86 (six parts, longest emt-G 179 s), `verify_scope.wls` 16/16; sympy
  `check_field_theory.py` 72/72 with comparison "agree", `check_scope.py` 15/15; every output reproduced byte for byte
  by a second run.  The b4 supplements of 2026-10-14 (`verify_field_theory_b4*.wls`, `check_field_theory_b4.py`,
  `field-theory-b4.json` and its four reports) are removed from the repository and the gate.  Provenance:
  `Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` section 6.10.  KNOWN OPEN until W7/W8: the publication tests
  of the documents that cite this record (`test_dirac16complex_field_theory_publication.py`,
  `test_dirac16complex00_field_theory_publication.py`, `test_pair_creation_proofs_publication.py`) fail, because the
  documents still describe the metric of 2026-10-14 (renamed checks, new counts 86/16/72/15, new formula blocks); the
  textbook still cites the retired b4 reports.
- W4 DONE 2026-10-16: `Revision/gkd_lovelock/` for the corrected metric, every real z.  Rust (`poly.rs`: the symbol
  W = (Sin^2)^(1/12) replaces S = Sin^(1/3), new symbol G = Sign[Cot], 14 exponents; `geometry.rs`: the metric,
  sqrt|det g| = G C E^-1 Q^4 W^3; `main.rs`: 27 checks, new `mixed_riemann_free_of_x0`, `mixed_riemann_only_sectional`,
  `sqrt_det_g_positive_every_quarter`, `k<k>_free_of_x0`, `k<k>_offdiagonal_vanishes`, `k<k>_hidden_equals_extra_times`;
  10 unit tests in all four quarters of z): 112 nonzero R^ab_cd (all R^ab_ab, x0-free), every P_(k) diagonal and
  x0-free with P^x0_x0 = P^xt_xt; 27/27, 13 s.  Wolfram `verify_lovelock_gkd.wls` 29/29 (exact zero test
  `LGKDZeroQ` for every real z; 48 s); sympy `check_lovelock_gkd.py` 56/56 (symbol form w = |sin|^(1/6), sign(sin),
  sign(cot); 13 s); all reproduced byte for byte by a second run; P_(1) = -4 G agrees with the independent sympy
  record `metric_warped/results/warped-metric.json` (einstein_diagonal).  `gkd-selftest.json` unchanged (gkd.rs
  unchanged; the 900 s self-test was not re-run).  The results of the metric of 2026-10-14 are frozen in
  `gkd_lovelock/reference_2026_10_14/` (files of c93fe22, sha256 pinned); `comparison/compare_with_author.py` compares
  the author's Pair_Creation notebook (written for that metric) with them: 80 checks, 75 PASS, 0 FAIL, 5 NOT-AVAILABLE
  (`comparison/README.md` 1.2).  Provenance: `verification/WOLFRAMSCRIPT_PROVENANCE.md` part 6.5,
  `results/PROVENANCE_OF_THE_COMPUTATION.md` note of 2026-10-16; `Revision/tests/test_gkd_lovelock.py` re-pinned
  (fast and slow tests pass).  KNOWN OPEN: `Revision/docs/LOVELOCK_GKD.md` and `test_lovelock_gkd_publication.py` (W7),
  `Revision/notebooks/src/lovelock_gkd.py` (W6, cites 19 Rust checks), the textbook chapters 3 and 11 (W8);
  `field_equations_a4` reads the new `lovelock-tensors.json` (W2, next).
- W2 DONE 2026-10-16 (the field equations; the Kohn-Sham parts move to W5): `Revision/field_equations_a4/` for the
  corrected metric, every real z.  Every E_(k) is diagonal and x0-free; three components x4, x1 (= x2 = x3), x0 (= x5 =
  x6 = x7) in a4', a4'', u = b4'/b4, v = u', k = e^{2a4}/b4; the source needs p0 = p_t and no off-diagonal component;
  constraint first order; (x1, x0) linear in (a4'', v), Einstein J = {{2, -2}, {0, -3/2}}; Bianchi d4 E^4_4 =
  3 a4' (E^1_1 - E^4_4) + 4 h4 (E^0_0 - E^4_4), h4 = u/2 - a4'; Einstein: G^4_4 = 6 H^2 k + 3 a4'^2 - (3/2) u^2, flat
  vacuum a4 = 0, b4 = H^2 (x4 - c)^2, no exponential-history vacuum; author's weights: the record's history needs the
  source of warped-metric.json (history_source, grows with k = e^{(2/3) H x4}), no exponential vacuum; EGB: vacuum only
  for constant k (beta = 2) with alpha2 = -1/(4 H^2 (A^2 - k0)); condensate: gamma Omega = (3/2) H e^{a4} b4^{-1/2}
  gamma^x0 + (u - a4'/2) gamma^x4, S = e^{a4} b4^{-2} S0, 24 off-diagonal three-gamma bilinears, exact witnesses for
  constant k; equal pressures on exponential histories: none in Einstein, for the author's weights only k0 = (16 +
  2 A^2)/(2 + A^2) (beta = 2) and k0 = 8 (A = 0).  Wolfram 57/57 (20 s), sympy 69/69 (8 s), both byte-identical on a
  second run; `check_b4_block.py` and `python-b4-block.json` retired (gate step removed).  Provenance:
  `field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` 6.10.  KNOWN OPEN until W5: `python/check_ks_source_conditions.py`
  and `ks_source/` (gate steps a4-ks-source-conditions, a4-ks-source, a4-ks-source-unittest) read keys of the metric of
  2026-10-14 (generalSource.identity_*, offDiagonal_*, exponentialHistory.*.Q) and evaluate the Kohn-Sham states of the
  old metric; they fail until the Kohn-Sham record is redone (W5).  Also open: the readers of a4-equations.json in
  lead_checks (W3), kohn_sham/theory (W5), dark_sector and pairing (W6), documents (W7), textbook (W8).
- W3 DONE 2026-10-16: `Revision/lead_checks/` for the corrected metric, each statement computed for both signs of
  sin z ((sin^2)^(1/6) = (s sin z)^(1/3)): `emt_divergence_and_spin_connection.py` 10/10 (divergence with h4, the
  y-coordinate form, gamma Omega = (3/2) H e^{a4} b4^{-1/2} gamma^x0 + (u - a4'/2) gamma^x4, negative control with a
  growing block: a4' coefficient +7/2), `einstein_gauss_bonnet_a4.py` 12/12 (own ring t = |sin|^(1/6); G diagonal and
  x0-free, record equations, flat vacuum, no exponential vacuum, classical Lanczos tensor = alpha_2 terms of the record),
  `charge_conjugation_and_u1.py` 12/12 (U(1) Noether matrix identity in the corrected metric); all reproduced byte
  for byte; `Revision/tests/test_lead_checks.py` passes (EGB count 14 -> 12).
- W5 STATE AT THE STOP OF 2026-10-17 ~07:52 (the author: "Stop all stages ... push all you have"; committed as WIP;
  the paragraph after this one is the older kit, still valid for its steps).  DONE and consistent: theory, the Rust
  solver's canonical record (`results/`, 243 files; a repeat with the binary of H15 reproduced it byte for byte, 244/244
  files and the report), `ks-rust-solver.json` 45/45, the reference record of the pre-H15 code (39/39), the tip study
  (7/7, README rewritten; the run of the pre-H15 sources), the dense history (8/8), `check_ks_source_conditions.py` 5/5,
  `ks_source_a4.py` 19/19 with its tests (H13: step-doubling substeps in part D), the READMEs of reference, tip study,
  ks_source and field_equations_a4, provenance 6.11, the gate rows in parts (both twins, `test_revision_gate.py` 16 OK).
  NOT DONE: the cross-check FAILED 3 of 31 checks (`reports/ks-crosscheck.json` is that failing run;
  `claude_failures.md` H14, H15, H16): int_p0 and E_exx - first order differ by ~2.4e-10 and 3.4e-10 because the SCF
  stopping error of both solvers was in neither uncertainty, and the reference's sea-hole list was shorter than three
  Rust thermal label sets.  The fix is IN THE CODE (uncommitted before this push, now committed) but its records are NOT
  regenerated: `solver/src/model.rs` (refined run: SCF tolerance 1e-14, cap 1000 iterations), `solver/src/runs.rs` (a4
  neighbours at scf_tol/10 but not below 1e-14), `reference/ks_fd.py` (SCF_TOL = 1e-14 for every state),
  `reference/run_reference.py` (sea-hole list + max(5, 10%) shells; texts), `checker/crosscheck_ks.py` (reads the
  reference's scfTolerance; H14 pattern), `checker/measure_rust_refinement.py` (texts).  So the committed
  `reference/results`, `reports/ks-reference.json` (scfTolerance 1e-12), `reports/ks-rust-determinism.json`,
  `checker/rust-refinement.json`, `reports/ks-crosscheck*.{json,csv}` and `tip_convergence/*` (source hashes) are of the
  pre-H15 code.  RESTART: run, in this order, the gate rows ks-rust-build, ks-rust-test, ks-rust-repeat-part1..3,
  ks-rust-repeat, ks-rust-repeat-identical, ks-rust-refined-part1..4, ks-rust-refined, ks-rust-determinism,
  ks-rust-refinement, ks-reference-s1-part1..6, ks-reference-s2-part1..6, ks-reference, ks-crosscheck-repeat-s1/s2-part1..6,
  ks-crosscheck, ks-tip-convergence-scan-part1..6, -recal-part1..3, ks-tip-convergence, dark16-ks-history-part1..3,
  dark16-ks-history, a4-ks-source-conditions, a4-ks-source, a4-ks-source-unittest (each under `timeout -k 5 423`; the
  measured times of the first attempt: repeat parts 75, 80, 90 s, refined parts 185, 190, 207, 176 s); then the
  READMEs of solver, reference, checker (still the b4-record text), tip study (scripts and drafts in
  `handoff/drafts_2026-10-17/`), the gate budgets from the measured times, HANDOFF W5 DONE, commit, push.  W6 drafts
  (pairing, T3 demos, dark sector, dirac16complex00, notebooks plan) are in the same folder with `w6_notes.md`.
- W5 DONE 2026-10-17: `Revision/kohn_sham/` and the Kohn-Sham source parts of `Revision/field_equations_a4/` for the
  corrected metric.  Theory (`kohn_sham/theory`): the hidden direction carries f = e^{-a4} b4^{1/2}, kappa = e^{-a4}
  constant in y, P = e^{-3Hy}/Vol_7, Vol_7 = ell^3 v_t e^{(5/3) a4}, the fold joins two halves (both fold conditions
  filled, ASSUMED), y-conservation p0' + 3H (p0 - p_t) = 0, dE/da4 = -3 P3 + P_t + P0/3, the rescaling identity changes
  H and L; Wolfram 51/51, sympy 61/61 (provenance 6.8).  Rust solver: N_mid = 592, N_large = 2352, lambda_1 = 157.7,
  2.131, 0.5363, lambda_2 = 473.1, 6.393, 1.609; the lambda = 0 states are exact fold-band gases (eps = e^{-a4}|k|);
  `ks-rust-solver.json` 45/45, mermin roots 5/5, determinism 14/14 (the refined run at the SCF tolerance 1e-14 since H15); the matrix, its repeat and the refined
  run in parts
  with a job cache (`--cache`, `--part`, `--inner-threads`; byte-identical to one run).  Reference: 39/39 (stages 1 and 2 in six parts each with the job cache, assembly 4.4 s; H12: the a4 neighbours at NB_TOL = 1e-14).
  Cross-check: 31/31 (the repeat of the reference computed beforehand in two stages of six parts into its own cache, then byte-identical to the record).  Tip study: 7/7 (scan 6 parts, recal 3 parts, final; 966 s): the free states are exact fold-band gases independent of L (except N = 2352 at a4,0 = 0, where k = 0 bulk levels become occupied from L = 3.5); the interacting zero modes depend on L the more the later the slice (N = 8 at a4,0 = 2: the recorded E_KS is 0.215 of the large-L value); the calibration rule has no non-trivial limit.  Dense history (`dark_sector/dirac16complex/compute/run_ks_history.py`, in
  parts): 8/8 (615 runs: 15 series x 41 slices; three parts of 23 s and an assembly of 0.7 s).  `field_equations_a4`: `check_ks_source_conditions.py` 5/5 (no recorded state is an admissible
  source: C1 fails for every nonzero state, C2 p0 = p_t only for lambda = 0, C3 holds); `ks_source/ks_source_a4.py`
  19/19 (H13: part D integrates with step-doubling substeps and detects det J -> 0 at 1e-6 of det J(0); the unit test pins the 19 check names).  Failures on the way: `claude_failures.md` H2-H15 (H11: a part's wall time included a 9-hour system sleep;
  H12: the reference's a4 neighbours needed the SCF tolerance 1e-14; H13: the fixed-step integration of ks_source
  part D did not resolve the solutions before their events; H14: the cross-check read a changed text of the
  determinism report; H15: the cross-check failed 3 checks: the SCF stopping error was in neither uncertainty (the
  Rust refined run now stops at 1e-14, the reference solves every state to 1e-14) and the reference's sea-hole list
  was shorter than the Rust thermal label sets).  Gate: the Kohn-Sham steps in parts (both twins; patch 1: the Rust matrix, repeat and refined run, the reference and the cross-check's repeat in parts; patch 2: the tip study (scan 6, recal 3, final) and the dense history (3 parts and the assembly), budgets from the measured times; `Revision/tests/test_revision_gate.py` 16 tests OK, 1 skipped (the full gate)).
  KNOWN OPEN until W6: the dark sector (`compute_eos.py`, `derive_effective.py`, `independent_free_gas.py`,
  `dirac16complex00`, the Wolfram twin), pairing T3 (`check_t3.py` tests the old Hamiltonian string; the demos read the
  old key `emtIntegrals_2Vol7_int_e6Hy`), the notebooks (pinned report counts); until W7: the documents and their
  publication tests; until W8: the textbook.
- W6 NEXT (restart kit): the dark sector, pairing (T1/T2/Q, T3 and its demos), the notebooks, in the corrected
  metric.  W6 preparation (not durable, session scratch, on disk at
  `C:\Users\nsh\AppData\Local\Temp\claude\D--Developer-github-Dirac-claude\837d3989-831c-4131-a54e-de216022bedc\scratchpad\`):
  `w6_notes.md` (the hand derivations for the corrected metric: dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt), w_eff(A) =
  P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E), w_eff(C) = w_eff(A) - 4/9, condensate S ~ e^{a4} b4^{-2}, w_eff(A) = (5/9) w_c, the
  free gas w_eff(A) = 1/3 exactly, T3 holds in the same form), drafts `w6/derive_effective.py` (37/37), `w6/compute_eos.py`,
  `w6/independent_free_gas.py`, `w6/patch_check_t3.py` (untested against the new dense history); dirac16complex00
  drafts `w6/d00/python/derive_eos.py` (48/48) and `independent_numerics.py` (32/32 against it); the Wolfram twin
  `w6/verify_dark_sector.wls` (7/7).  W6 findings that change CONTENT, not only numbers: (a) ks-theory.json
  boundaryConditions.fold: both halves of a cell carry the same chi(y), so the corrected metric has NO Z2 mirror copy
  carrying -m; T3's statement S5 and check `T3_z2_mirror_copy_carries_minus_m_plus_lambda` must be removed, and the pairing
  documents must not claim a mirror universe from the brane; T3 itself ((m, lambda, theta) -> (-m, +lambda, pi - theta))
  still holds (sigma2 h_j(M) sigma2 = h_{-j}(-M) for every f).  (b) The free Kohn-Sham gas is an exact fold-band gas:
  w_eff(A) = 1/3 exactly; normalisation C shifts by -(4 - 2 beta)/3 = -4/9 (before -1/3); the condensate has
  w_eff(A) = (5/9) w_c and drifts as e^{-(5/3) a4}; the record's history needs an ANISOTROPIC source (kappa (p3 - p0) =
  -9 kk^2/16 + 1069 kk/432 + 2015/972), so no condensate sources it.  (c) Bulk-band quanta are blue-shifted by the
  shrinking hidden direction (1/f = e^{a4/3}): compute their w_eff, do not presume the old dust-like law.
  (d) Pairing T1/T2/Q: z -> pi - z is still an isometry of the corrected metric; recompute with its vielbein.
  (e) Drafts of 2026-10-17 in the scratch folder (patch scripts `w6/patch_*.py`, patched copies; NOT yet run unless
  stated): pairing T1/T2/Q (`w6/pairing/python/check_pairing.py`, `w6/pairing/wolfram/verify_pairing.wls` and
  `RevisionPairing.wl`: the corrected vielbein, sqrt|g| = e^{-a4} b4^2 cot z sin^{1/2} z, the fold instead of the Z2
  brane, the not-established tokens 'across the fold' and 'degenerate' in both lists); `Revision/SPEC.md` section 9
  (`w6/spec9_draft.md`); the T3 demos (`w6/t3demo/`: key e3Hy, Vol_7 e^{(5/3) a4}, N_mid read from parameters.json);
  check_t3_completion with the zero mode (e^{f M y}, 0); the dirac16complex00 tests (`w6/d00/tests/`); compute_eos
  13/13 and independent_free_gas 10/10 on the new dense history (the latter after a fix: the collocation leaves a
  spurious partner of the fold-band mode in a degenerate eigenspace).  RUN-TIME RISK: the gate row t3-rust-demo
  (3 members x 210 states of the new matrix) will exceed 423 s and must be split into parts before it is run.
- W6 DONE 2026-10-17 (resumed after UM-1 1.3 at the author's order "resume the paused W6 work and push"): the dark
  sector, pairing (T1/T2/Q, T3 and its two demonstrations) and the notebooks in the corrected metric (version 2).
  Pairing: `verify_pairing.wls` 102/102 and `check_pairing.py` 67/67 (the reflection z -> pi - z across the fold z = pi/2
  between the two halves of a cell; no Z2 orbifold); T3 `verify_t3.wls` 9/9 and `check_t3.py` 12/12 (statements S1-S4;
  the statement S5 of the mirror copy is removed), completion `verify_t3_completion.wls` 3/3 and `check_t3_completion.py`
  7/7; demonstrations (not proofs): the Rust solver 7/7 (630 single runs in four parts, the family measure of H17) and
  the reference solver 7/7 (162 grid runs in six parts of 219, 170, 78, 122, 115 and 91 s and an assembly of 2 s, byte-identical to the
  earlier four-part run; H18).  Dark sector: `derive_effective.py` 37/37, the dense Kohn-Sham history 8/8 (615 states),
  `compute_eos.py` 13/13, `independent_free_gas.py` 10/10, dirac16complex00 A 48/48 and B 32/32 and its tests 4/4,
  Wolfram `verify_dark_sector.wls` 7/7 (and the twin of the withdrawn metric 8/8); results: the free Kohn-Sham gas is an
  exact fold-band gas (w_eff(A) = 1/3, w_eff(C) = -1/9), the interacting gas w_eff(A) in [0.330585, 0.336132], the
  massive bulk band is blue-shifted (w_eff(A) from 0.318721 to -0.081074), the condensate drifts (wa = -28077/12500),
  neither hypothesis is established; `Revision/dark_sector/CORRECTED_METRIC_PROVENANCE.md` records the change and a
  complete re-run that reproduced every output byte for byte.  Notebooks: `kohn_sham_states` and
  `dark_sector_hypotheses` rebuilt for the corrected metric (two builds and one check each: kohn_sham_states 19.7, 19.9 and 19.5 s, dark_sector_hypotheses 22.2, 21.7 and 21.9 s), each `check` byte-identical, provenance files
  updated.  A read-only audit of the W6 deliverables (workflow, 12 agents: 104 findings, 94 confirmed by
  adversarial verification) was applied by fixer agents and checked; the producers whose comment or detail texts changed
  were re-run (the reports differ only in those texts).  Gate: t3-reference-demo in six parts and an assembly (budgets
  from the measured times), comments, `test_revision_gate.py` (--fast about 170 min by the step table).  KNOWN OPEN until
  W7: the publication tests of PAIR_CREATION_PROOFS, DIRAC16COMPLEX_FIELD_THEORY and DARK_SECTOR_HYPOTHESES, the
  documents rows of `Revision/README.md`; until W8: the textbook (e.g. `00c_honesty_ledger.py` README_ORDER lacks
  `dark_sector/reports/wolfram-dark-sector.json`).

### 0.9 ORDER 2026-10-15 evening: move EVERYTHING to b4(x4) — START HERE

The user's order (verbatim): "yes, move everything to b4(x4); b4 is never 1".  Scope: the current record
`Revision/` and the textbook `Revision/textbook/`.  The first-edition stages (`artifacts/`, `provenance/`,
`studies/`, the first-edition textbook) stay unchanged, as the author ordered on 2026-10-01 ("You must NOT mix
old with new").  The rule (written into `Revision/SPEC.md`, section 1, "The background history"): exact results
are derived for general b4(x4); a numerical history is a4 = H x4, b4 = b4(0) e^{(4/3) H x4} (beta = 4/3, the only
non-constant branch the author's weights allow for a diagonal source; NOT a vacuum solution: it needs the constant
source kappa (-2/27, -2/9, -22/27, -14/27)); Kohn-Sham states are solved at lambda_hat e^{-2 a4}; b4 = 1 appears only
as the withdrawn earlier metric (a historical comparison, e.g. with the author's earlier notebook, which has no b4).

Phases (each verified, committed and pushed; every calculation under `timeout 423`; no agent job longer than
423 s):
1. `Revision/theory/`: every section of `verify_field_theory.wls` (84 checks at b4 = 1) and of
   `check_field_theory.py` (70), and the scope checks (15 and 14), for general b4; split into parts so that each
   run stays under 423 s.
2. `Revision/field_equations_a4/`: sections 1 to 6 (52 checks at b4 = 1) for general b4.
3. `Revision/lead_checks/`: the three checks for general b4.
4. `Revision/kohn_sham/`: ks-theory with the b4 reduction; the Rust solver and the Python reference with the
   history (lambda_eff); the whole record recomputed (canonical, repeat, refined, determinism, Mermin roots,
   reference in parts, cross-check, tip convergence, exx).
5. `Revision/field_equations_a4/ks_source/` and `ks-source-conditions` with b4.
6. `Revision/pairing/`: T1, T2, Q, T3 with b4 and the T3 demonstrations on the new Kohn-Sham record.
7. The Revision notebooks `kohn_sham_states` and `lovelock_gkd`.
8. The documents (field theories, Kohn-Sham, pair creation, Lovelock GKD), READMEs, gate, provenance, index.
9. The textbook: every chapter and notebook that uses b4 = 1; the book PDF.

Progress (newest last):
- Phase 1 DONE (2026-10-15, commit after 58d6d78). `RevisionFieldTheory.wl` defines the metric with b4;
  `verify_field_theory.wls` runs in six parts and a merge (base 35 s, emt-G 156 s, emt-C 108 s, solutions 34 s,
  solutions-G 51 s, quantisation 11 s, merge 5 s; part files in the git-ignored `build/theory-wolfram/`, the merge
  refuses part files of another version of its inputs): 84 of 84 for general a4 and b4, 33 formula records.
  `check_field_theory.py` runs twice (`--part nonlinear` 209 s, then the main run 128 s): 72 of 72, comparison with
  Wolfram agree (33 of 33 records, 65 of 65 pairs). Scope: Wolfram 15 of 15, sympy 14 of 14. Renamed checks: Wolfram
  `sqrt_det_g`, `gammaOmega_total`, `gammaOmega_per_direction`, `Omega_vanishes_iff_a4prime_b4prime_and_H_vanish`,
  scope `boosted_frame_removes_only_the_H_term` (no boost in the (x4, x0) plane removes the b4' part of gamma^mu
  Omega_mu); sympy `sqrt_det_g_equals_b4_cos_z`, `gamma_mu_Omega_mu_equals_3H_gamma_x0_plus_b4_term`,
  `a4_time_terms_cancel_b4_terms_add`, new `spinor_connection_real`, `gravity_term_square`; record
  `ricci_mixed_nonzero` replaces `ricci_mixed_diagonal`, new record `evolution_form`. Gate: 95 steps (8292 s
  expected), `--fast` skips 3. Provenance: `Revision/theory/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` 6.9; index row 2
  and 29; dated note in `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md` part 7; failures G1 to G4.
  KNOWN OPEN until phase 8: the publication tests of DIRAC16COMPLEX_FIELD_THEORY (29 failures, 3 errors),
  DIRAC16COMPLEX00_FIELD_THEORY (4 failures, 3 errors) and PAIR_CREATION_PROOFS (2 failures) fail, because those
  documents still describe b4 = 1 and quote the old check names and texts; the textbook (phase 9) still cites them
  too. The supplements `verify_field_theory_b4*.wls`, `check_field_theory_b4.py` and their outputs are superseded
  but kept unchanged (their sha256 are in METRIC_CHANGE_PROVENANCE.md) until the textbook no longer reads them.
  Second run (2026-10-15, the gate steps theory-* in five batches under 423 s, each revision_verification=OK): every
  committed output of the theory reproduced byte for byte.
- Phases 2 and 3 DONE (2026-10-16). `Revision/field_equations_a4`: every section for general a4 and b4 (Wolfram 59 of
  59, sympy twin rewritten with its own ring including b4^(1/2), u, v: 65 of 65; two runs byte-identical); keys of
  `a4-equations.json` general (exponentialHistory replaces linearMember; key b4 kept for the dark sector);
  results: the off-diagonal pair cot z u Q, Einstein Q = 3 H/2, the Bianchi identity with b4, the author's weights
  beta in {0, 4/3} at a4 = H x4 with the source (-2/27, -2/9, -22/27, -14/27), no vacuum and no condensate source with
  b4 not constant on exponential histories, the EGB branches beta = 4 and beta = 2 (1 + A^2)/A^2. Provenance
  `field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md` 6.9. `Revision/lead_checks`: all three for general b4
  (10/10, 14/14, 12/12); the EGB check rewritten with an exact ring (2.4 s) after its first general version ran past
  423 s (claude_failures G5; `timeout` did not stop the native python process: since then `timeout -k 5 423`).
  KNOWN OPEN until phase 5: `field_equations_a4/ks_source/ks_source_a4.py` stops (KeyError: it reads the removed
  b4 = 1 keys), so the gate steps a4-ks-source and a4-ks-source-unittest fail until then.
- Phase 4, part 1 DONE (2026-10-16): `Revision/kohn_sham` theory and Rust record for b4(x4). ks-theory with the b4
  reduction (Psi = e^{ik.x} W^{-3} b4^{-3/4} chi; b4 absent from h; densities per Vol_7(a4,0) = ell^3 v_t e^{(3/2) beta a4,0}
  in units of b4(0)^{3/2}, coupling lambda_hat = lambda b4(0)^{-3/2}; dE/da4 = -3 (P3 - P_t) - (3/2) beta P_t; rescaling
  partner v_t e^{(3 beta/2 - 3) a4,0}; historyBeta = 4/3): Wolfram 51/51, sympy 63/63. Rust solver: beta read from
  ks-theory.json, Vol_7(a4,0), the history identity, the thermal continuation fallback, a4 neighbours at scf_tol/10,
  `single --beta`. The calibration rule applied to the new history gives lambda_1 = 0.01946, 0.01206, 0.006645 (N = 8, 136,
  688; 13 and 36 times larger for N = 136, 688). Canonical 43/43 (78 s), Mermin roots 5/5, repeat byte-identical,
  refined 340.6 s, determinism 14/14. claude_failures G6 to G8. Solver README section "The metric with b4(x4)".
- Phase 4, part 2 DONE (2026-10-16): the Python reference with b4 (beta, Vol_7(a4,0), the history identity, its own
  continuation fallback `solve_state_robust`): 6 parts of 120 to 232 s, 38/38; `measure_rust_refinement.py` 32.9 s;
  the cross-check with its reference repeat (6 parts) 31/31 (beta compared as numbers; the exact N = 8 Q_max tie
  accepted); the tip-cutoff study 7/7 (187 s; reads `Vol7AtA4Zero`); KS theory provenance 6.7, index rows 6 and 30;
  gate: the reference and the cross-check repeat in six parts (99 steps, 8572 s expected; --fast 96 steps).
  claude_failures G9 to G11.
- Dark sector on the moved Kohn-Sham record DONE (2026-10-16): `run_ks_history.py` passes lambda_hat (8/8: all 15
  series equal the KS record at the five slices; the lambda_eff form agrees to 2.0e-13), `compute_eos.py` 15/15; all
  seven producers rerun (39, 8, 15, 10, 49, 32, 8). Only the interacting gas numbers changed (w_eff(C) [-0.040541,
  -0.006532], tangent wa [-0.019170, -0.008787], fitted wa [-0.028228, -0.019171], w_eff(A) [0.292793, 0.326802]); no
  verdict changed. README, B4_PROVENANCE section 10, the document DARK_SECTOR_HYPOTHESES (pdf rebuilt and registered,
  27 pages; publication test 30/30), the notebook dark_sector_hypotheses (46/46, check byte-identical; its provenance)
  updated. The textbook chapters 22/23 that quote the dark-sector numbers follow in phase 9.
- Phase 5 DONE (2026-10-16): `check_ks_source_conditions.py` for b4 (6/6: C1 x0-independence for every a4, b4; C2 on
  the history; C3 the constant source (-2/27, ...) the history needs; C4 the off-diagonal equation, which holds there);
  `ks_source/ks_source_a4.py` rewritten for b4 (22/22): Einstein gravity admits no history with a changing b4 for any
  source without T^x4_x0; the truncated system {x4 moment, off-diagonal equation} is algebraic in (a4', u) and is
  integrated for the free gas on the dense record history (author's weights: fold at a4 = 0.024; Gauss-Bonnet: regular,
  fold, adiabaticity_lost); unit tests 11/11; the gate runs a4-ks-source after dark16-eos (it reads the dense history).
  claude_failures G12. NEXT: phase 6 (`Revision/pairing/`: T1, T2, Q, T3 with b4 and the T3 demonstrations on the new
  Kohn-Sham record).
  KNOWN OPEN until phases 7 and 8 (they quote the record before b4): `Revision/tests/test_kohn_sham_deflating_field_publication.py`
  (test_cited_checks_exist_and_pass: the document cites the former check counts) and
  `Revision/tests/test_revision_notebooks.py` (test_kohn_sham_record_counts_printed); the pairing T3 demonstrations and
  their results (phase 6) still hold the runs of the former couplings.
- Phase 6 DONE (2026-10-16): `Revision/pairing/` in the author's metric with b4(x4). T1, T2, Q: the primordial and
  mirror vielbeins with e^-a4 b4^(1/2) sin^(1/6) z, sqrt|g| = b4^(3/2) cos z, b4 > 0 an arbitrary function of x4;
  `verify_pairing.wls` 102/102 (new check `primordial_connection_depends_on_b4`; 112 s and 100 s, byte-identical),
  `check_pairing.py` 67/67 (new `geometry.connection_depends_on_b4`; 202 s). T3: b4 does not enter h_j; the texts of
  `verify_t3.wls` (10/10), `verify_t3_completion.wls` (3/3), `check_t3.py` (13/13), `check_t3_completion.py` (7/7)
  moved to b4 (orbital factor b4^(-3/4), slice b4,0, the a4 and b4 equations). Demonstrations on the slices of the
  history with b4 (lambda_hat fixed, Vol_7 growing): Rust 7/7 (316 s, gate 320 s; image = plus to 1.7e-13 / 2.1e-11;
  T1-parameter control >= 3.3e-4), reference 7/7 (140 s; every member through `solve_state_robust`, none needed the
  continuation; its convergence check text corrected, claude_failures G13). Provenance: pairing part 6 last item,
  T3 6.8, index rows 4 and 5; READMEs. NEXT: phase 7 (the Revision notebooks kohn_sham_states and lovelock_gkd).
- Phase 7, part 1 DONE (2026-10-16): `Revision/notebooks/kohn_sham_states` for the record with b4 (texts: history with
  b4, deflation e^-a4 b4^(1/2), growing Vol_7, lambda_hat, b4 absent from h_j; expected report counts 51, 63, 43, 14,
  5, 38, 31): build 24/24 (14.6 s), check byte-identical; its provenance (hash tables refreshed, section 7 entry);
  `test_revision_notebooks.py` static 9 OK (the stale dark count 7 -> 8 fixed, claude_failures G14). Part 2 (the
  notebook lovelock_gkd for general b4: identities with all 13 symbols, comparison with a4-equations.json, the history
  source from the GKD tensors, figures on b4 = b4(0) e^(4 a4/3)) in progress.
- Phase 7 DONE (2026-10-16): `lovelock_gkd` no longer restricts to b4 = 1: the trace identities, E_(1) = G and the
  density form for general a4, b4; E_(k) in (H, a4', a4'', u, v) equal to a4-equations.json lovelockTensors (all six
  components, k = 1, 2, 3); on the history the blocks differ for k = 1, 2 and agree for k = 3; with the author's
  weights the Rust GKD tensors give kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) H^2, T^x4_x0 = 0. Build
  45/45, check byte-identical; provenance (a4-equations.json added to its inputs). claude_failures G15 (a wrong
  expectation of mine, caught by the check). NEXT: phase 8 (the documents KOHN_SHAM_DEFLATING_FIELD, LOVELOCK_GKD,
  PAIR_CREATION_PROOFS, DIRAC16COMPLEX_FIELD_THEORY, DIRAC16COMPLEX00_FIELD_THEORY and their pdfs and publication
  tests; READMEs, gate, provenance, index).
- Phase 8, parts 1-3 DONE (2026-10-16): KOHN_SHAM_DEFLATING_FIELD (53868b6; every table regenerated from the record
  with b4, re-run of the canonical matrix 43/43 in 95.6 s byte-identical, test 36 passed), LOVELOCK_GKD (179fdcb; every
  formula for general b4 in a4', a4'', u, v; author-comparison report regenerated for the SPEC hash), PAIR_CREATION_PROOFS
  (f52902a; section 2 for general b4, C1 for the a4 and b4 equations, T3 numbers). NEXT: DIRAC16COMPLEX_FIELD_THEORY
  and DIRAC16COMPLEX00_FIELD_THEORY (both still say "sections 2 to 13 are the record of the case b4 = 1"; the theory
  record field-theory.json is general b4 since phase 1: port every formula; their tests re-derive many blocks), then
  READMEs, gate, provenance, index; then phase 9 (textbook).
  KNOWN OPEN until phase 8: the publication tests of PAIR_CREATION_PROOFS, DIRAC16COMPLEX_FIELD_THEORY and
  DIRAC16COMPLEX00_FIELD_THEORY (the documents cite the former counts and texts).
- Phase 8 DONE (2026-10-16): DIRAC16COMPLEX_FIELD_THEORY (dd779a9) and DIRAC16COMPLEX00_FIELD_THEORY (8d32afe) for
  general b4: no section describes b4 = 1 any more (the 00 document's b4 section 17 is merged into the text); the 16
  component equations with hat-d4 = d4 + (3/4) b4'/b4 (in the 00 document the inverse scale factors are now eps_s,
  eps_t: u, v denote b4'/b4 and its derivative); the a4 and b4 equations with E_(k) in (a4', a4'', u, v), the
  off-diagonal factor Q (per order Q_(k)), the identity x1 + x5 - 2 x0 (per order I_(k)), Einstein gravity,
  exponential histories, the author's weights, the background history and its source; the Kohn-Sham source analysis
  (22/22); the dark-sector verdict for Hypothesis00 from the current records. Their publication tests render every
  new block from field-theory.json and a4-equations.json (17 and 16 tests pass); pdfs 39 and 42 pages, warning-free,
  registered. README (pages; the Kohn-Sham row), the gate (t3-rust-demo marked long: claude_failures G16; --fast
  now 95 steps), claude_failures G17 (two heredoc patches that changed nothing). All Revision unit tests except the
  textbook test pass (204 tests, 10 skipped, 123 s). The provenance index has no rows for the documents (nothing to
  change). NEXT: the gate steps of the six documents and the audits in batches under 423 s; then phase 9 (the
  textbook: every chapter and notebook that still uses b4 = 1 or cites the former check names, e.g. chapter 17's
  `ks_verdict_holds_for_every_b4`; the book PDF; retire the b4 supplements once the textbook no longer reads them).

### 0.8 STATE 2026-10-15 (dark sector with b4; done, superseded as the start by 0.9)

Never run `python -m unittest Revision.tests.test_universes_in_pairs_textbook` as a whole: it
takes longer than 423 s (claude_failures D2 and F2). Run its classes one by one.

The user's order of 2026-10-15: update and push every dark-sector file and object for the author's
metric with b4(x4) ("b4 is a function of x4; b4 is NEVER 1"), with a provenance that proves the
change; no calculation longer than 423 s; push each piece at once. The conventions of 0.7 hold.

**Done and pushed (origin/main equals HEAD).**
- The dark-sector record, recomputed on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4)
  (beta = 4/3, the branch of the author's weights): commits e9d1751 (derive_effective, 39
  checks), 0f73748 (run_ks_history at lambda_hat e^(-2 a4), 7), 3932af4 (compute_eos, 15),
  0f969b1 (independent free gas, 10), 98cf574 (dirac16complex00 A 49 and B 32), 4cb9b7d (both
  READMEs), 019337d and 3324b56 (Wolfram verification 8/8 and the non-evaluating reader of the
  author's notebook), 65d954c (DARK_SECTOR_HYPOTHESES md/tex/pdf, 27 pages, registered).
- e6113b0: the Revision notebook dark_sector_hypotheses for b4 (46 checks; two builds and a check
  byte-identical).
- c19fa18: `Revision/dark_sector/B4_PROVENANCE.md` (the provenance of the whole change: source,
  chain with independent confirmations, commits, withdrawn-against-new table, the re-run of
  2026-10-15 in which every producer reproduced the record byte for byte, sha256 of every file);
  index row 31 (rev-dark-sector-b4, fast) with a FULL test; row 27 updated; the notebook test.
- 35e80d9: the gate twins have the steps dark-b4-author-notebook, dark-b4-author-inputs and
  dark-b4-wolfram; both twins pass the dark-sector steps.

**Then done and pushed the same day (origin/main equals HEAD, 916cf7b and this commit):**
- 1d77417: a correction of the record's TEXT (no number, no check count changed). With b4(x4) a condensate
  reads w_eff(C) = -1/3 + (2/3) w_c, below -1 while its drifting ratio is in the phantom window; "phantom only
  at an instant", "not the observer's w_eff" and "no crossing in M1 to M5" were b4 = 1 leftovers
  (derive_eos.py text `ghost`, both READMEs, DARK_SECTOR_HYPOTHESES, the Revision notebook; B4_PROVENANCE
  section 9).
- 3d9d25c: compute_eos.py records the LARGEST w_a of the drifting-condensate mixtures near the Unite w0 too
  (max_wa_with_w0_within_0p1_of_unite; C: [-2.639515126434, -1.41320438962]); the document had read the minimum
  as a bound. The document (27 pages, registered), README, publication test and Revision notebook updated.
- e78d882: textbook chapter 22 (22.16 to 22.24, 22.27, exercises 11 to 14) and Notebook 22b (35 checks) for
  b4(x4); 69 quoted code blocks verbatim. 62b2513: Revision/README.md (dark_sector row, gate 88 steps), chapter
  00 and Notebook 00c (52 reports, 1383 checks; the dark sector is a twelfth two-verifier subject). 4f53714:
  chapter 09 section 9.19 and Notebook 09b. 7779c77: Notebook 23a (rebuilt last) and chapter 23 (regenerated,
  --check identical). 916cf7b: the book assembled (13/13), PDF 6548 pages, 0 warnings, two builds identical,
  registered.
- Fresh clone of 916cf7b (26 s): clean, no private file tracked; every dark-sector producer (the 615-state
  history and the free gas included), both Wolfram scripts, the dark-sector tests, test_revision_notebooks,
  test_revision_gate, test_execution_provenance, the Revision notebook check, nbkit check of 22b, 00c, 09b and
  23a, chapter23 --check and the textbook classes Book, Files and Validators: all pass, no tracked file
  changed; both registered PDFs equal the registry.
- ebf703e: the root README (unchanged since 2026-09-30 and silent about `Revision/`) points to the current
  record and its dark sector with b4(x4); the first-edition stages stay unchanged, as the author ordered
  ("must NOT mix old with new"). The chapter-22 plan of TEXTBOOK_SPEC and the publication test's docstring
  are up to date.

**Open (for the user to decide; not part of the dark-sector order):**
- The general Kohn-Sham record (`Revision/kohn_sham/`) and the textbook chapters on it (for example chapter 14,
  line 150, and chapter 9's general framing) still state that they work on the background b4 = 1; the
  dark-sector record now uses b4(x4) (the Kohn-Sham states there are Psi = b4^(-3/4) chi at the coupling
  lambda_hat e^(-2 a4)). Whether every other part of the project must also drop b4 = 1 is the user's decision.
- The items of 0.7b remain (old Stage-4 notebook report, matter-antimatter hash pins, gkd-rust-selftest,
  the serial textbook rebuild test longer than 423 s).

### 0.7 STATE 2026-10-15 07:00 PDT (superseded by 0.8)

The binding conventions of section 0.6 hold unchanged: X = {x0, ..., x7} with x0 the hidden
direction first, never x8; the metric with b4(x4); no single calculation longer than 423 s;
the user's modified `Dirac_Einstein-Lovelock_4+4_Nash.nb` is never staged by hand.

**Done and pushed since 0.6 (origin/main equals HEAD).**
- Every textbook chapter, 00 to 23, is in the author's coordinates x0..x7 and states where it
  uses the general b4 and where the background b4 = 1. The commits:
  - chapters: 12 efe22e7, 17 90e51f3, 18 882228c, 19 ef4eeb0, 20 8cb4588, 21 0b87507,
    11 3130b6c, 22 be3411d, 23 96b20cc;
  - TEXTBOOK_SPEC, 12a and 10d: faad793;
  - the book and its PDF: 04f9bbb.
  Every notebook was rebuilt under `timeout 423`. Chapter 23 was regenerated last
  (`Revision/textbook/tools/chapter23/run_all.py --check`: byte-identical). The walk-through
  audit finds no drift in any of the 91 notebooks.
- Notebook 11a no longer runs the Rust GKD self-test, which takes 7 to 13 minutes. It prints the
  command and reads the committed record `Revision/gkd_lovelock/results/gkd-selftest.json`.
- Notebook 23a writes the full step table of the gate to `Revision/textbook/data/23a_gate_steps.csv`.
  It prints only the long steps and the audits.
- The gate has 85 steps, 4 of them long; the expected time is 8057 s in full and 6487 s with
  `--fast`. Sections 0.4w and older say "65 steps": that was the gate of 2026-10-08, before the
  b4 steps. The gate run of 2026-10-14 (`Revision/README.md`) covered every step except
  gkd-rust-selftest; nothing of the Revision record outside the textbook has changed since.
- The book `Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md`:
  - assembly: 13 of 13 checks;
  - PDF: 6539 pages, 0 LaTeX warnings, both builds byte-identical;
  - registered in `Revision/pdf-specifications.json` (sha256 7d935e3e...).
  The first build had 18 warnings (`claude_failures.md`, E9). `tools/relabel/README.md` is
  updated.
- The seven WolframScript files of the metric with b4 were re-run on 2026-10-15. Their committed
  outputs were reproduced byte for byte. They now have rows 28 to 30 in
  `provenance/EXECUTION_PROVENANCE_INDEX.md` and their record is in section 9 of
  `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`.
- `claude_failures.md`, section E: every failure and overrun of this continuation.

**Tests and verification of 2026-10-15:** section 0.7b below.

### 0.7b Tests and fresh-clone verification, 2026-10-15

**Unit tests.** Every module of `tests/` and `Revision/tests/` was run separately, and every class of
`test_universes_in_pairs_textbook` separately; six ran at a time, each under 423 s. The longest was
`tests.test_d16c_stage5_dirac16complex00`, 167 s. Results: 43 units, 39 OK at first.
- Two new failures, both fixed in 0025743:
  - nine relabel tool files had been committed with CRLF (`test_revision_files_are_stored_with_lf`);
  - the Stage-5 gate twins held five unfilled `@@...@@` time placeholders from the run killed on
    2026-10-14. They are now filled with recorded or measured times, and
    `tests.test_d16c_stage5_gate` passes 13 of 13.
- Two failures are older and were left as they are (both first-edition material, recorded in
  `claude_failures.md` A6):
  - `tests.test_d16c_kohn_sham_notebook.TestCommittedReport`, 4 tests: the old Stage-4 notebook
    report has had verdict FAILURE since 2026-09-30. Whether to finish old Stage 4 or mark it
    superseded is the user's decision.
  - `tests.test_d16c_matter_antimatter_publication`, 4 hash pins: the pairing artifacts of
    `artifacts/dirac16complex/pair-creation` changed on 2026-10-08 (6b5936f) after the
    matter-antimatter record was made. Repairing the pins honestly needs the matter-antimatter
    Wolfram verifier re-run, which takes 7 to 8.5 min, longer than the 423 s limit. Changing the
    recorded hashes without that run would falsify the record.

**Notebooks.** `Revision/textbook/tools/relabel/check_all.py` with all chapters ran `nbkit check` on all
91 notebooks: 91 OK, every notebook, written file and provenance file byte-identical. The slowest
was 16a, 115 s; the wall time was 242 s.

**Fresh clone** of https://github.com/once-ere/Dirac_claude.git at 0025743 (48 s):
- `git status` clean; no private file tracked. `Generalized _Kronecker_Delta_4+4.nb` is tracked at the
  author's request, as `.gitignore` says.
- 51 tests OK, 9 skipped: the textbook classes Book, Files and Tools, `test_revision_gate`,
  `test_execution_provenance` and `test_d16c_stage5_gate`.
- `chapter23/run_all.py --check`: byte-identical. `walkthrough_all.py`: 91 notebooks, no drift.
- The registered book PDF: 6539 pages, sha256 equal to the registry.
- `nbkit check` of 00a, 06a, 07b, 11a, 18a and 23a: all OK.
- The tree was still clean after every check.

**Still open (not done, with the reason).**
- The general-b4 forms of three sections of `Revision/theory/wolfram/verify_field_theory.wls` were
  never derived (`METRIC_CHANGE_PROVENANCE.md`, section 7). These are the Noether identities, the
  exact solutions with conservation, and the canonical quantisation.
- gkd-rust-selftest (900 s expected) cannot run within 423 s and was not re-run. The generalized
  Kronecker delta it tests does not depend on the metric.
- The serial byte-for-byte rebuild test of the textbook notebooks takes longer than 423 s; it is
  replaced by `Revision/textbook/tools/relabel/check_all.py`.

### 0.6 STATE 2026-10-15 04:30 (superseded by 0.7)

**Binding conventions.**
- The author's coordinates are {x0, x1, ..., x7}:
  - x0 is the hidden direction (z = 6 H x0) and comes FIRST;
  - x1, x2, x3 are 3-space, x4 is the time, x5, x6, x7 are the extra times;
  - the Python index k is xk, and gamma^(xk) = T16[k] (T16[8] = Gamma);
  - the Revision record files number the directions from 1 in the order x0..x7, so subtract 1.
- Never write x8.
- The metric of 2026-10-14 has b4(x4): `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`.
- The backgrounds of the record (Kohn-Sham, pairing, scope reports, lead checks) have b4 = 1.
- No single calculation may wait longer than 423 s (7 min 3 s). Bound every command with `timeout 423`, and `git push` with `timeout 120`.
- The user's modified `Dirac_Einstein-Lovelock_4+4_Nash.nb` is NOT committed; stage specific paths only. The pinned version of the author's notebook is 4f2d83b5 (commit b13373c).

**Done and pushed (HEAD fccfdb3 and the handoff commit after it; origin/main equals HEAD).**
- The Revision record in the author's coordinates and with b4: earlier commits; gate run of 2026-10-14, 84 of 85 steps OK.
- General-b4 sympy checks: `check_field_theory_b4.py`, 8 of 8, including `gravity_term_square_b4`, MM = (9H^2 - (9/16)(b4'/b4)^2) 1.
- DIRAC16COMPLEX(00)_FIELD_THEORY PDFs rebuilt and registered. Revision unit tests: 200, OK.
- Textbook chapters 00-10 and 13-16 moved to x0..x7, with every builder fixed by position, every notebook rebuilt, and the chapter text and walk-throughs updated:
  - chapters 06 and 07 for the general b4;
  - chapter 08 at b4 = 1, with the general forms quoted from chapters 6 and 7;
  - chapter 09 with the record's x4 energy identity for b4;
  - chapters 10 and 13-16 on the b4 = 1 backgrounds, as stated in the text.
- The assembly `--only 00..10 13..16 --allow-missing` passes 13 of 13 checks.
- Tools for continuing: `Revision/textbook/tools/relabel/` (README.md gives the procedure per chapter, and `examples/` holds the fix scripts used).

**Remaining work (in this order).** The status of every notebook of chapters 09-23 against the relabelled records was measured with `tools/relabel/check_all.py` (nbkit check, 8 in parallel, each under 423 s) on 2026-10-14 at about 20:30. Chapters 09-10 and 13-16 have been fixed since then; the rest:

1. **Chapter 12** (12a, 12b, 12c, 12d fail).
   - The a4 records are relabelled: keys `x0x0` (it was `x8x8`), "independent of x0", and gammas.json in the order x0..x7.
   - Some a4 records also have b4 blocks (`Revision/field_equations_a4/a4-equations.json`, key `b4`).
   - Fix the positions as in chapters 08-10; keep b4 = 1 where the records are b4 = 1.
2. **Chapter 17** (17a, 17b).
   - The Kohn-Sham source-condition record changed (5 checks); `conservation_x8` is now `conservation_x0`.
3. **Chapters 18 and 19** (18a, 18b, 18c, 19a, 19b).
   - Gamma, C and B by position, with the chirality as the product g0 g1 ... g7.
   - The record texts "g^(x8) g^(x1) ..." are now "g^(x0) ...".
4. **Chapters 20 and 21** (20a, 20b, 21a, 21b, 21c, 21d).
   - Gammas by position; record keys `x0x0` and `x0`; Omega_components in the order x0..x7.
5. **Chapter 11.**
   - The Rust Lovelock program (`Revision/gkd_lovelock`) was rerun with the b4 metric. Its `curvature.json` and `lovelock-tensors.json` contain b4[x4], b4' and b4''.
   - 11b's exact polynomial engine (exponent tuples in H, A1, A2, C) needs three more variables (b4, b4', b4''), or every record value must be put at b4 = 1 before the comparison.
   - `examples/fix_11b_partial.py` holds the first part of the work: positions, METRIC order, and the mixing terms (4, c, 0, c).
   - 11a needs only the relabel; 11c reads the same tensors.
6. **Chapter 22**: the notebooks pass; only the chapter text needs the relabel.
7. **Chapter 23.**
   - 23a fails nbkit: In [9] prints 90 lines (at most 80).
   - Regenerate chapter 23 with `Revision/textbook/tools/chapter23/run_all.py` after all other chapters.
8. Then:
   - `Revision/textbook/TEXTBOOK_SPEC.md`: the relabel and the b4 rule;
   - the full book assembly and PDF (`Book.test_assembled_book_is_current` fails until then; it compares with the last assembled edition, which still has the old labels);
   - `provenance/EXECUTION_PROVENANCE_INDEX.md` rows for the b4 scripts;
   - section 0.4 and later of this file still say "gate 65 steps"; the gate has 85;
   - the full tests (each bounded: run the textbook test classes one by one; replace the serial byte-for-byte rebuild test with `check_all.py`);
   - a fresh-clone verification.

**Per-chapter procedure (it worked for chapters 03-16).**
1. `tb_relabel.py` on the builders.
2. Fix every position by hand. The patterns:
   - `G[3]` -> `G[4]` (x4), `G[7]` -> `G[0]` (x0), `x[3]` -> `x[4]`, `x[7]` -> `x[0]`;
   - frame lists start with the hidden factor;
   - `range(1, 9)` over directions -> `range(8)`; `fixture["gamma"][a - 1]` -> `[a]`;
   - unpacking `g1, ..., g8 = g` -> `g0, ..., g7 = g`;
   - record texts with k8/x8/p8/M8 -> k0/x0/p0/M0, and momentum samples in the order (k0, k1, k2, k3) = (4, 1, 2, 0).
3. Rebuild each notebook with `nbkit.py build ... --date YYYY-MM-DD` under `timeout 423`.
4. Check that the RESULT lines are unchanged except for labels (`nb_out_diff.py`).
5. Run `tb_relabel.py` and `wt_remap.py` on the chapter, then `walkthrough_diff.py`, `wt_contiguous.py` (compare with HEAD), `prose_indices.py`, `scan_old.py`, `prov_hashes.py` and the assembly.
6. Commit the specific paths and push.

Never edit with bash heredocs that contain backslashes: one turned `\frac` into a form feed. Check for control characters after every edit.

**Failures and overruns:** `claude_failures.md`, section D.


### 0.1 Resume the same conversation (preferred: keeps all context)

```powershell
cd D:\Developer\github\Dirac_claude
claude --continue
```

`claude --continue` (short: `claude -c`) reopens the most recent session started in
this directory.  If several exist, run `claude --resume` and choose the one whose
title mentions dirac16complex.  In the Claude desktop app: open the Code tab and
click the session in the sidebar.  After it opens, type:

```text
continue with all stages, do not stop
```

Background workflows do NOT survive a session limit.  The resumed session must
re-launch them (section 0.3); finished files are on disk and are reused.

### 0.2 Start a new session (if the old one cannot be resumed)

```powershell
cd D:\Developer\github\Dirac_claude
claude
```

Paste this prompt verbatim as the first message:

```text
Read HANDOFF.md completely. Then read handoff/specs/CONTRACT.md (all sections,
including section 11), handoff/specs/STAGE4_SPEC.md (including sections 7 and 8),
handoff/specs/NUMERICS_CONTRACT.md (including its erratum) and
handoff/specs/STAGE2_SPEC.md. Run "git pull" and "bash scripts/setup_solver.sh".
Then continue every unfinished stage listed in HANDOFF.md section 2, in order,
using the Workflow tool with the scripts in handoff/workflows/ as described in
HANDOFF.md section 3. Never modify dirac-main/, vendor/, or the .nb notebook.
Do not stop between stages. Commit and push to origin main after every completed
stage and after every ~30 minutes of work, verify from a fresh clone, and never
take shortcuts or weaken a check.
```

### 0.3 How the new session re-launches the work

1. Copy the needed `handoff/workflows/*.js` into its own scratchpad directory and set
   `const SP = '<its scratchpad path>'` in each (keep `ROOT`; LF line endings only).
2. Launch each script with the Workflow tool (`scriptPath`).  A fresh session has no
   cached agent results (resume by run id works only inside the session that ran it),
   so every agent runs again; the prompts tell the agents that partial files exist and
   must be inspected and finished, not restarted from zero.
3. NEVER use blocking waits or sleep loops (the user forbids any delay): launch the
   workflows in the background, do real work meanwhile, and act on the completion
   notifications.  Commit and push after every milestone; the Stop hook
   (`.claude/settings.local.json` -> `.claude/hooks/stop_push_verify.py`, git-ignored,
   so it must be re-created in a new clone; see the memory note) commits, pushes and
   checks the repository every time the session stops.
4. When the user writes "pause" or "STOP": halt at once (create `.claude/ALLOW_STOP` in
   the same first action so the Stop hook allows the stop), push, report in a few lines.

### 0.4g STATE 2026-10-07 (new session, no cache)

New session 9e0a6725 (the old session's cache is gone).  User order of 2026-10-07 done first: `provenance/dirac matrices.md`
(commit fdba6bb) - the author's eight REAL 16 x 16 Dirac matrices, obtained by evaluating the author's own input cells of the
`.nb` in a fresh kernel (`provenance/dirac_matrices/extract_from_author_notebook.wls`), proved by
`provenance/dirac_matrices/build_dirac_matrices_md.py` (35/35 exact checks: real, Cl(4,4) anticommutation, S^AB = [G_A,G_B]/4
span spin(4,4) ~ so(4,4), exponentials = products of two unit vectors generating Spin_0(4,4); with Gamma_0 and Gamma_4 all four
components of Pin(4,4)); displays the 8 matrices, sigma16, T16A[8], the 28 pair products, all 256 products, P_L, P_R.
CORRECTION (audit finding 16, 2026-10-08): it is NOT true that every gamma source equals them - the Revision a4 engine
(FieldEquationsA4.wl and its Python twin) uses an equivalent Cl(1,1)^(x)4 basis until the a4 patch (0.4k) is applied; the regenerated
file measures this and answers 'Instruction followed: not completely' until then, 'yes' after the patch.  Test `tests/test_dirac_matrices_provenance.py`; verified from a fresh clone.
Then both workflows were RELAUNCHED from scratch with SP of this session: textbook run wf_bf3a3e31-ec0, execution provenance
run wf_f856ecb5-265 (agents inspect and finish the existing partial files).  After them: Revision wave 1b, then wave 2.
Also RUNNING: `Revision/workflows/dirac_matrices_audit.js` (run wf_5ccefead-ea3): adversarial audit of `provenance/dirac matrices.md`
(notebook fidelity incl. later redefinitions and stored Out cells; the mathematics incl. the Pin(4,4) argument; COVERAGE of every
gamma-matrix source in the repository incl. Rust and .nb; fresh-clone reproducibility), two skeptics per finding, one fixer owning
provenance/dirac_matrices/*, the .md and its test, then a fresh-clone verifier.  If lost: relaunch with the new SP.
Also RUNNING (user 2026-10-07: "continue with all stages, do not stop"): Revision wave 1b followed automatically by wave 2,
chained in `Revision/workflows/revision_wave_1b_then_2.js` (run wf_987b1061-79b; set SP in the session copies of
revision_wave_1b.js, revision_wave_2.js and the chain script, and copy wave1_review_and_fix.json to <SP>/w1_args.json).
Both wave scripts now carry a CONCURRENCY NOTE: never edit Revision/textbook/, the textbook test, provenance/, notebooks/, tests/
while the other workflows run; pdf-specifications.json is shared (re-read before any change).
DONE 2026-10-07 (was: LEAD DECISION PENDING): the runner of old-primordial found that scripts/verify_dirac16complex_primordial.wls does not
check that wolfram/Dirac16ComplexPrimordial.wl loaded and that D16PRun returned an Association: with the package missing, checks
is not an Association, Count[Values[checks], False] = 0 and the script can exit 0 after writing a garbage report (false success).
FIX IT (after the execution-provenance chain for old-primordial has finished, to avoid a concurrent edit): fail with an ERROR line and
exit 1 unless AssociationQ[result] && AssociationQ[result["checks"]] && Length > 0, and count every non-True check as failed;
then re-run the set twice in a fresh clone (byte identity of both outputs) and update its provenance file.
  -> FIXED by the lead: package-existence check, AssociationQ guard on D16PRun's result, ERROR + exit 1 when an output cannot be
  written, every non-True check counted as failed.  Two runs: 126/126, both outputs identical between runs; primordial-components.json
  byte-identical to the committed file; the report changes only in the script's own sha256 (919928...->f49606...).  Missing package ->
  ERROR, exit 1; unwritable output -> ERROR, exit 1.  The Stage-2 publication pins that sha: provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md
  updated, .tex/.pdf rebuilt with --register (38 pages, 11/11; register and verify builds byte-identical), test pins updated;
  tests/test_d16c_primordial{,_publication}.py 53/53.  The set's provenance file is updated by the execution-provenance fixer of
  old-primordial (it re-verifies against the fixed script).
LEAD DECISION PENDING (2026-10-07, from the dirac-matrices audit, coverage lens): Revision/field_equations_a4/wolfram/FieldEquationsA4.wl
(FEsig1/FEeps/FEGen/FEGammaFrame, lines 119-128) builds its OWN real 16x16 Cl(4,4) basis Cl(1,1)^(x)4 and never reads
Revision/algebra/gammas.json; check_field_equations_a4.py runs its primary checks on a third basis own_rep().  Both are real 16x16
Cl(4,4) sets equivalent to the author's T16 (intertwiner dim 1, K^T K = 2 I16) and a4-equations.json holds only representation-
independent coefficients, but SPEC section 2 requires the author's T16.  FIX (after the execution-provenance chain for rev-a4 has
finished): make both use the author's matrices from gammas.json as the PRIMARY representation, keep the tensor bases only as labelled
comparison representations with an explicit equivalence check; re-run both verifiers twice in a fresh clone; a4-equations.json must stay
byte-identical (any change explained); update Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md; regenerate
provenance/dirac matrices.md (its coverage section).
  PREPARATION RUNNING: `Revision/workflows/a4_author_gammas_prep.js` (run wf_da94d8ca-701) makes and verifies this change in a
  SCRATCH clone only and writes <SP>/a4prep/a4_author_gammas.patch (implementer, two adversarial reviewers, fixer, fresh-clone
  verifier).  Apply the verified patch to the repository once the execution-provenance chain of rev-a4 has finished.
  ALSO in this change (rev-a4 runner, 2026-10-07): verify_field_equations_a4.wls exits 0 when an output cannot be written and never
  finishes when its package is missing - make both an ERROR line with exit code 1 (keep the committed output bytes identical); README
  says 'about 15 s' (measured 19-34 s on a loaded machine).
FRESH-CLONE TEST RESULT (2026-10-07, clone of a4c5eda, no setup_solver.sh): python -m unittest discover -s Revision/tests: 82 tests,
every failure (25 F + 1 E) is in test_universes_in_pairs_textbook (book in progress; the textbook workflow rebuilds it); everything
else passes.  python -m unittest discover -s tests: 615 tests, 5 failures, all OLD-STAGE and PRE-EXISTING: (1) four
test_d16c_kohn_sham_notebook.TestCommittedReport tests - the committed artifacts/dirac16complex/kohn-sham/notebook-report.json has
verdict FAILURE since 2026-09-30 (gauntlet rust_vs_reference_{deltaSCF,eigenvalues,particleHole} failed, python_check_report skipped)
and reference-summary.json was regenerated after it (33c07a3): old Stage 4 was paused unfinished when the Revision replaced it;
(2) test_d16c_student_guide_publication path studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe - exists
only after bash scripts/setup_solver.sh.  The execution-provenance agent nb-kohn-sham must document (1) truthfully; decide with the
user whether old Stage 4 is to be finished or formally marked superseded by Revision/kohn_sham.
CROSS-WORKFLOW SYNC OBLIGATIONS (2026-10-07; must be done before any stage is declared complete):
  (1) wave 1b's Mermin repair (ks-mermin-fix: solver 42/42, determinism 14/14, Mermin roots 5/5, KS theory python 58/58, wolfram 46/46,
      cross-check 29/29) added a 58th KS-theory check: Revision/docs/PAIR_CREATION_PROOFS.md line 492 and .tex line 702 still say 57 ->
      update to 58, rebuild + re-register the PDF (Revision/pdf-specifications.json), re-pin MARKDOWN_SHA256/TEX_SHA256 in
      Revision/tests/test_pair_creation_proofs_publication.py; also list check_ks_source_conditions.py before check_ks_theory.py in its
      section 10 (new run-order dependency).  Owner: wave 1b's fix phase; verify it is done.
  (2) The thermal Kohn-Sham outputs changed (mu moved by up to 8.3e-10 in three N8 T10 states; new last column of thermodynamics.csv;
      larger mu_rounding_bound): textbook notebooks 15a, 15d, 16a, 19a read them -> after wave 1b/2 have finished, rebuild every textbook
      notebook whose Revision inputs changed and re-run nbkit --check; rebuild the book.
  (3) Revision/kohn_sham/theory/check_ks_theory.py changed: re-check that Revision/kohn_sham/theory/WOLFRAMSCRIPT_PROVENANCE.md records no
      stale hash of it; likewise every provenance file must be re-checked against the final state of the files it hashes (the index step).
INCIDENT (2026-10-07): the execution-provenance runner of old-nb-build-ks ran `winget show --accept-source-agreements` to read
package versions; if the winget source agreements were not yet accepted on this machine, that accepted them without the user's
permission.  Reported to the user.  Every workflow script in Revision/workflows/ now carries a rule forbidding the acceptance of any
agreement/licence/EULA (effective for future launches; the prompts of already-running runs cannot be changed).

### 0.4j RESTARTED 2026-10-07 20:35 (user: "continue, resume, restart --accept-source-agreements. continue all stages and do not stop")

The user approved the winget source agreements that an agent had accepted (the rule that agents never accept agreements stays).
Restarted from the 0.4i kit in the same session (SP = <session scratchpad>/restart; the a4 prep's partial scratch clone was carried over
and fast-forwarded): textbook_restart wf_a71f212d-1cf, execution_provenance_restart wf_148a1d48-af6, dirac_matrices_audit_fix_restart
wf_7dd6d253-9cf, revision_wave_1b_restart_then_2 wf_2b4c1c8c-a30, a4_author_gammas_prep wf_e7ec46e7-1bf.  If these are lost: merge
their journals into Revision/workflows/state_restart/ with merge_state.py (add these run ids) and regenerate the restart scripts.

### 0.5a RESUMED 2026-10-14 (new session 837d3989; the weekly limit stopped session 9e0a6725 at 2026-10-08 16:57)

What the limit killed (all at 17:17 on 2026-10-08): the detached old-Stage-4 R1 run, the guarded Stage-5 reference pairs run
(BrokenProcessPool), the Stage-5 Rust canonical pairs run (no resume), and the agents of the book fix rounds (book v2
wf_f498b1dc-916: lenses book-references and book-notebooks never ran, all 12 chapter fixers of its 19 confirmed findings failed;
residual rounds wf_06568fcb-164, wf_2585e73c-8be, wf_732b0dc4-103 returned null with partial edits in the tree).
Old session scratchpad (kept on this machine): C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/
9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad (stage4_keep/, phase3c_book/ progress logs, sweep/ finding files).
New session scratchpad SP = C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/
837d3989-831c-4131-a54e-de216022bedc/scratchpad.

RELAUNCHED 2026-10-14 11:32 (detached; logs and done markers under SP):
* SP/stage4_R1/run_R1.cmd - old Stage 4 R1 (same config stage4_keep/refsmear120-config.json, same solver sha 8dbedada...);
  ~4.5 h; then R2-R5 of section 0.4u item 4 with <scratchpad>/stage4_R1/out = SP/stage4_R1/out.
* SP/s5ref/run_s5_reference_guarded.cmd - Stage-5 reference pairs, --workers 8 --resume (89 of 180 runs were recorded).
* SP/s5rust/run_canonical_then_refined.cmd (affinity FF: canonical into artifacts/.../rust, then --refined into
  build/s5-rust-refined) and SP/s5rust/run_repeat.cmd (affinity FF00, in parallel: build/s5-rust-repeat).
WORKFLOWS (this session): book continuation wf_dce5cca3-aa8 (skeptics for the 6 findings without skeptic results, one fixer +
one adversarial verifier per chapter 00, 05, 07, 09-18, 20, 21; items in SP/book_items.json); old Stage 5 documents prep
wf_4f461ffd-f21 (document A complete + review/skeptics/fix; document B sections 1-6, 8-10 with section 7 and the numerical rows
left to the lead; the gate twins).  DONE: the three minor rev7 verifier findings (8e75a17).
ORDER after these: (1) the two missing book lenses (references, notebooks) in small per-chapter-group agents -> skeptics ->
fixes; (2) 23a rebuilt last, chapter 23 regenerated (tools/chapter23/run_all.py), assembly, book PDF --register, textbook test;
(3) old Stage 4 R2-R5 when SP/stage4_R1/done.txt exists; (4) old Stage 5 when the reference and Rust runs are done: pairs
checker, compare_pairs_runs.py, document B section 7 + figures script, register, gate, matter-antimatter regeneration and the
PROVISIONAL strings (stage5_plan_final.md step 7, in the old scratchpad), pairing provenance, extract_repository_wolfram_gammas.wls;
(5) full Revision gate (detached), EXECUTION_PROVENANCE_FULL=1, all suites, two fresh clones, push, notify.

### 0.4z STATE 2026-10-08 ~16:10 (Revision record nearly final)

Done and verified since 0.4y (most edits are in the Stop hook's WIP snapshots; their content is described here): phases
3c-rev2/3/4/5 complete (fixers + adversarial verifiers); the theory Wolfram re-run checked (13/13 checks of
verify_after_run.py: report = expected, outputs = af0fc19, 70/70 agree, 103 printed lines as in 4.2) and recorded
(WOLFRAMSCRIPT_PROVENANCE 6.7, index row 2: one run); the tip-study README corrected (7 of 19 not established; 4.4 table =
JSON); README rows; the lead's batch after the last verifiers (DS/00/KS/PCP texts, KS number test with negative control,
dark-sector generator texts + byte-identical re-runs + notebook digests, provenance notes, index rows 25-27,
check_dirac16complex00.py cross-drive relative() fix + report regenerated, record 6.7) - one adversarial verifier
(<scratchpad>/verify6/) is checking that batch.  Textbook check pass 2 running (<scratchpad>/vc_sweep2).  Next: the book
workflow v2 with <scratchpad>/sweep/args.json (+ failing notebooks of pass 2); old Stage 4 after R1 (chain
<scratchpad>/vc_stage4chain/chain_R2_R4.py); old Stage 5 after the reference + Rust runs (pairs checker, then
handoff/workflows/wf_stage5_docs_review_v2.js); 23a last; book PDF; full gate; fresh clones.

### 0.4y VERIFICATION STATE 2026-10-08 ~15:40 (the Stop hook's WIP snapshots 6779cd3/0f569dd hold most agent edits)

- Phase 3c-rev2 (wf_35f24f29-e41): fix2:theory (generator 'conserved charge' texts, ExpandFileName roots; scope re-runs
  byte-identical; the 45-min verify_field_theory.wls + check_field_theory.py run detached since 15:14, check it with
  <scratchpad>/phase3c2/fix2-theory/verify_after_run.py - base af0fc19 because the WIP snapshots moved HEAD; it also checks
  the run log per WOLFRAMSCRIPT_PROVENANCE 3.6; then record 6.7 + index row 2: 'field theory one run equal to the expected
  report'); fix2:roots-a4 (6 roots, ks_source texts, a4 key; all outputs byte-identical; verifier running); fix2:docs-a and
  fix2:docs-b (verified; residual items went to rev4).
- Phase 3c-rev3 (wf_12f85853-978): dark_sector generator texts + the three Revision notebooks (cell 32, cargo-target, private
  POSIX build folder) - running; then EXECUTION_PROVENANCE_INDEX rows 25-27 by the lead.
- Phase 3c-rev4 docs (wf_96a1a6d8-65b): FT line 454, PCP 9.1 scope reports, KS tip study (patch <scratchpad>/gate2/
  patch_ks_doc.py), DS/00 phantom condition Lambda < -(21 + 3A^2)H^2 and the canonical-functional qualifier - running.
- Old Stage 5: E5.3 guard committed (095c17d); guarded reference run detached since ~15:40 (<scratchpad>/s5guard/,
  marker s5_reference_guarded.done.txt; it exits 1 if a non-control run is stopped by a guard - the m = 3 lamp2 runs are).
- Textbook check pass 1 (<scratchpad>/vc_sweep1): only 00c (new reports) and 23a (rebuilt last) fail so far.
- Root test suite running (<scratchpad>/vc_tests1/root.log).

### 0.4x PREPARED WORKFLOWS (2026-10-08 ~15:35)

- handoff/workflows/wf_stage5_docs_review_v2.js: old Stage 5 documents A and B, the Stage-5 gate, 4 review lenses, 2 skeptics
  per finding, fixer(s) and a fix-verifier; errata E5.1-E5.3 binding; registry lock; consistency with the Revision record.
  Launch after the guarded reference pairs, the Rust pairs (canonical, repeat, refined) and the pairs checker are done; set SP.
- Revision/workflows/completion/completion_phase_3c_book_v2.js: sweep of the chapters affected by the final Revision record
  (args.sweep / args.failing; prepared args: <scratchpad>/sweep/args.json for chapters 00, 09, 10, 14, 15, 16, 17, 21, 22;
  fill args.failing from the nbkit check pass <scratchpad>/vc_sweep*/summary.txt), then the 5 book lenses, skeptics, fixers in
  size-bounded parts (the 60000-character cut of v1 dropped findings in phase 3c-rev) and verifiers.  Launch after the Revision
  record is final (phase 3c-rev2/rev3 verifiers, the lead's KS/FT document items).  23a and chapter 23 stay with the lead.

### 0.4w STATE AND ORDER 2026-10-08 ~15:35

Done since 0.4v: tip_convergence committed (a8eb09d) and re-run by the lead byte-identically; gate 65 steps + 'Failed to open
file' rule + LF test + README corrections (ab84209); whole-book test build OK (<scratchpad>/bookcheck1: 6457 pages, no LaTeX
warning, register = verify).  INCIDENT 15:11: the old-Stage-5 reference pairs job (--workers 8) had two workers at 167 GB and
123 GB (runaway minusM_control and m3 lamp2 runs: 14k-104k states after widening the window); commit charge 325/326 GB; the
Stage-4 R1 run died with MemoryError.  The lead killed the pairs job; R1 RESTARTED 15:15 (<scratchpad>/stage4_R1, the failed
attempt in stage4_R1_oom); an agent (s5guard, <scratchpad>/s5guard/) designs a deterministic state/window guard in the DRIVER
ks_reference_pairs.py (not the solver, whose sha the Stage-4 records pin), writes erratum E5.3 and relaunches the pairs.
ORDER: (1) phase 3c-rev2 (wf_35f24f29-e41: theory incl. the detached 45-min verify_field_theory.wls, roots-a4, docs-a, docs-b)
-> commit; (2) dark_sector generator texts + Revision/notebooks/dark_sector_hypotheses cell 32 (after the notebooks
fix-verifier) and KOHN_SHAM_DEFLATING_FIELD 5/15.3/15.4 with the tip study (the agent's sentences in its report) -> commit;
(3) old Stage 5 numerics -> pairs checker -> documents -> gate -> matter-antimatter; (4) old Stage 4 R2-R5 after R1;
(5) TEXTBOOK SWEEP after the Revision record is final: nbkit check of every notebook (00c must list fock-quartic.json and
tip-convergence.json and the two new README counts; chapter 00 quotes '39 reports', '37 counts'), rebuild what fails with its
chapter, phase 3c-book review, chapter 23 template ('long step' definition; 65 steps, 9 long), 23a LAST, run_all.py, assemble,
PDF --date 'October 2026' --wide-page-numbers --register, test_universes_in_pairs_textbook; (6) full gate detached,
EXECUTION_PROVENANCE_FULL=1, all suites, two fresh clones, push, notify.

### 0.4v STATE 2026-10-08 ~15:10 (phase 3c-rev fixers done or finishing; follow-up round planned)

Committed: chapter-23 kit (36f7fce), 21d words list + check_chapter --book --wide-page-numbers (b0bae4b), Revision/workflows LF
(the fixer's extra Revision/workflows/.gitattributes was dropped: fix-verifier option a).  Uncommitted fixer edits in the tree:
Revision/docs (4 docs rebuilt + registered), gkd_lovelock/comparison (extractor root + no $Version; LOVELOCK_GKD.md 8.2 sha256
quote still old -> test_lovelock_gkd_publication fails until fixed), verify_revision twins + test_revision_gate + README (gate
failure path, precheck exit 3), Revision/notebooks (lovelock_gkd cargo target).  The docs fixer saw only 8 of 15 findings (task
text cut at 60000 chars): the 5 unhandled ones are in <scratchpad>/phase3c2/docs_missed_findings.json; every fixer/verifier open
item is in <scratchpad>/phase3c2/phase3c_rev_open_items.json.  Follow-up round (phase 3c-rev2): generator texts (dark_sector,
theory incl. the 45-min verify_field_theory.wls re-run detached, field_equations_a4 ks_source), ExpandFileName roots of 8 .wls,
docs (missed findings, LOVELOCK_GKD 8.2, FT abstract, PCP 100/407, fock_quartic in FT 12/15 + README theory row), README
versions/short-folder note.  Lead: gate steps fock_quartic + tip_convergence, wolframscript 'Failed to open file' = failure, an LF
test for Revision/, README step counts.  Detached: Stage-4 R1, Stage-5 reference + Rust, whole-book test build
(<scratchpad>/bookcheck1/, check_chapter --book).

### 0.4u PENDING LEAD INTEGRATIONS (2026-10-08 ~14:50) - do them in this order, each verified, committed, pushed

1. After phase 3c-rev's fixers: gate steps for Revision/theory/fock_quartic/check_fock_quartic.py (line proposed by its agent:
   `theory-fock-quartic|10|0|-|.../fock-quartic.json|.../fock-quartic.json|{python} Revision/theory/fock_quartic/check_fock_quartic.py`)
   and for Revision/kohn_sham/tip_convergence/ (agent running) in BOTH twins; Revision/tests/test_revision_gate.py must pass
   (it now fails on exactly these two scripts, as designed).
2. Documents: DIRAC16COMPLEX_FIELD_THEORY sections 12 and 15 + README theory row and canonical-quantisation answer (fock_quartic:
   the identity holds only with Wick ordering, in the single-mode-set model; texts in the agent report); KOHN_SHAM_DEFLATING_FIELD
   sections 5, 15.3, 15.4 + README kohn_sham row (tip convergence result); rebuild, register, test pins.
3. Old Stage 5 (detached since 14:36): reference pairs (--workers 8 --resume, ~4.5 h, 1.6-9.3 h) and Rust pairs canonical ->
   repeat -> refined (logs/done markers in <scratchpad>/phase3d/stage5-plan/plan/); then the pairs checker, the documents
   (handoff/workflows/wf_stage5_docs_review.js after telling STAGE5_DOC_OUTLINE about E5.1/E5.2), the gate
   verify_stage5_pair_creation, the matter-antimatter regeneration and its PROVISIONAL strings, the pairing provenance, HANDOFF C.
4. Old Stage 4 (detached since 13:22): after stage4_R1/done.txt: R2-R5 + the errata line, in one commit.
   R2: replace artifacts/dirac16complex/kohn-sham/reference/m1_L3_N1016_lamm2_T0 with <scratchpad>/stage4_R1/out/<that label>,
   then `python scripts/ks_reference_solver.py --resume --skip-self-tests` (summary; ~13 s).  R3: `python
   scripts/check_dirac16complex_kohn_sham.py --repeat <scratchpad>/stage4_keep/repeat --refined <scratchpad>/stage4_keep/refined`
   (~180 s; writes python-check-report.json).  R4: `python notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb`
   (route B; rewrites the 14 figures), `python -m nbconvert --to notebook --execute notebooks/dirac16complex_kohn_sham.ipynb
   --output-dir build/nbconvert` (route A), `python notebooks/check_dirac16complex_kohn_sham_notebook.py
   notebooks/dirac16complex_kohn_sham.ipynb --also build/nbconvert/dirac16complex_kohn_sham.ipynb --report
   artifacts/dirac16complex/kohn-sham/notebook-report.json`.  R5: `python -m unittest discover -s tests -p
   'test_d16c_kohn_sham*.py' -v` + tests/test_d16c_textbook_publication.py; then the PROVENANCE 6.6 passages and the errata line
   of provenance/ERRATA_FIRST_EDITION_TEXTBOOK.md (the first-edition textbook itself stays unmodified).  Expected reference
   deltaSCF about 0.04361951 (to be confirmed by the run).
5. Chapter 23 generator (0.4s), 23a rebuilt LAST, phase 3c-book, the two LaTeX warnings, assembly, PDF registration.
6. Full gate (detached, ~3 h), EXECUTION_PROVENANCE_FULL=1, all suites, two fresh clones, push, notify the user.
7. Added 15:00: (a) Revision/kohn_sham/tip_convergence/tip-convergence.json used the key 'result' (23a crashed with KeyError
   'verdict'): its agent was asked to switch to 'verdict' + summary; (b) 21d builder line ~175 words list: 'the conserved number
   of the phase symmetry' -> local law + ASSUMED no-flux total (wording in the refix:23 report); (c) the book edition must be
   re-registered with --date "October 2026" (Section 23.7 quotes the verify command); (d) the glossary regeneration kit is in
   <scratchpad>/phase3b/refix-23/ (extract.py, group.py, build.py, splice.py, manual.json): move it into
   Revision/textbook/tools/chapter23/ together with the chapter generator, with repository-relative paths.
   DONE 14:45 (36f7fce): Revision/textbook/tools/chapter23/run_all.py [--check]; --check reproduces chapter 23 byte for byte.
8. Added 14:50: the pairing Wolfram + sympy outputs of old Stage 5 were re-run after the E5.1 fix (wolfram 141 checks, 0 failed;
   python-pairing-report.json byte-identical; sha256 of every output unchanged) - <scratchpad>/vs5/summary.txt.

### 0.4t RUNNING AT ~14:40 (2026-10-08)

Phase 3c-rev (wf_632c3899-8ec: whole-Revision review, 5 lenses, 2 skeptics per finding, fixers per area, fix-verifiers);
phase 3b-2 (wf_b0dab77f-75b: chapter 23 glossary done, verifier found 12, re-fix running); agents: stage5-plan (old Stage 5:
Krein correction applied, pairs-checker per-member uncertainty, numerics measured, completion plan), ks-tip-convergence (new
Revision/kohn_sham/tip_convergence/: L = 3..6 series, extrapolation; SPEC 7 'regular tip'), fock-quartic (new
Revision/theory/fock_quartic/: the EMT operator identity for lambda != 0 in a finite Fock space; SPEC 4); the detached Stage-4
reference rerun.  Still to launch: phase 3c-book (after chapter 23 is final).  Final steps: section 0.4p step 5 plus the
chapter-23 generator (0.4s), the full gate (about 3 h, detached), EXECUTION_PROVENANCE_FULL=1, two fresh clones, notify.

### 0.4s CHAPTER 23 NOTES (2026-10-08 ~14:45)

Chapter 23 and Notebook 23a written (tb-23; glossary agent and verifier running).  (1) 23a reads every other notebook's
recorded check and the chapters, so it must be rebuilt LAST (after phase 3c), then chapter 23 regenerated.  (2) The chapter is
generated from a template by <scratchpad>/phase3b/tb-23/gen.py (+ ch23.template.md, fills.json): move them into
Revision/textbook/tools/chapter23/ with a repository-relative ROOT, and make the generator keep the glossary section (the glossary
agent edits the chapter file, not the template).  (3) A whole-book test build at 20:45 UTC failed on two LaTeX warnings from other
chapters (Overfull hbox 4.93 pt at .tex lines 788-795; 'Float too large for page by 3.5 pt' at input line 6381): find and fix
before the final PDF.  (4) 23a writes Revision/textbook/data/23a_*.csv (new folder): check the assembler and the textbook test.

### 0.4r OLD STAGES 4 AND 5 (2026-10-08 ~14:30; user: complete every open stage)

Old Stage 4: both root fixes and the checker follow-up committed (7baaf9e, 4ecfec5; tests 46/46; negative controls verified by
the lead).  REMAINING: the reference rerun m1_L3_N1016_lamm2_T0 (E4.14 b) runs DETACHED since 13:22 (scratchpad stage4_R1:
run_R1.cmd, run.log, done.txt when finished; ~4.5 h); then R2-R5 of notebooks/dirac16complex_kohn_sham.PROVENANCE.md section 6.6
(install the run in artifacts/dirac16complex/kohn-sham/reference/, ks_reference_solver.py --resume --skip-self-tests, the checker
with the preserved trees <scratchpad>/stage4_keep/{repeat,refined}, notebook builder -> route B -> route A -> audit, tests), with
the errata line of provenance/ERRATA_FIRST_EDITION_TEXTBOOK.md updated to the new counts in the same commit.
Old Stage 5 (HANDOFF item C): a planning agent (stage5-plan) applies the required Krein-reading correction (T1krein) at the root,
fixes the same per-member grid-uncertainty flaw in scripts/check_dirac16complex_pairs.py, measures the pending numerics and
returns the completion plan (numerics detached; checker; documents DIRAC16COMPLEX00_FIELD_THEORY and DIRAC16COMPLEX_PAIR_CREATION;
gate verify_stage5_pair_creation; matter-antimatter PROVISIONAL strings).

### 0.4q STATE 2026-10-08 ~14:40 (phase 3a nearly done; step 2 running)

Phase 3a results, each re-checked by the lead and committed: doc-updates (three wave-1 documents + README, six publication
tests OK with REVISION_PDF_REBUILD=1); prov-t3 (verify_t3.wls fixed at the root, provenance for both T3 scripts; lead negative
test FAILs as it must); lovelock-compare (Revision/gkd_lovelock/comparison: author's metric, Ricci scalar and Einstein tensor
agree exactly, 73 PASS / 0 FAIL / 5 NOT-AVAILABLE; no author output for k = 2, 3); revnb kohn_sham_states (check PASS);
chapters 16, 17, 19, 22 (fix, adversarial verify, re-fix; lead: nbkit check + check_chapter OK); tb-charge + refix-charge
(only the local U(1) law is proved; TEXTBOOK_SPEC R3 updated); the gate verify_revision.{sh,ps1} (--fast OK with bash and
pwsh; README section).  Index 26 rows, test 11/11.  Still running: stage4-fix (old Stage 4: reference delta_scf fix +
measured grid uncertainty in the level tolerance; gauntlet 60/60 in scratch so far).
Step 2 DONE (13:55): 89 of 89 notebooks (all but 00c) rebuilt with the patched tools and passed the independent `nbkit check --record`; walkthrough_all over 90 notebooks: 0 drift (audit tool fixed, 13e6113). The old Stage-4 reference re-run (E4.14 b) runs detached since 13:22 (scratchpad stage4_R1; expected ~4.5 h); a stage4-followup agent fixes the verifier's findings (per-member level uncertainty, relative paths). Phase 3b-1 (wf_aa3d04bc-99e) running; 3b-2 launched after this. Earlier note - step 2 was: tool patch + workaround removal + work_folders applied (uncommitted until the rebuild ends);
`rebuild_all_notebooks.py <scratchpad>/bulk` over all builders except 00c.  Next: walkthrough_all audit, commit, then phase 3b
(completion_phase_3b.js: revnb-dark, tb-21d, tb-23 + glossary, tb-00c, tb-05, rev-lovelock-sync), then 3c, then step 5.

### 0.4p RUN ORDER AFTER THE PAUSE (2026-10-08 ~10:20; user: "continue")

Running: phase 3a (wf_ad05323f-033, `Revision/workflows/completion/completion_phase_3a.js`, 11 chains).  Done meanwhile by the
lead (committed, pushed): the lead-check record correction (0eb99c0; normal ordering adds no sign; only the local U(1) law is
proved; 12/12, byte-identical re-runs); tools_patch.py fix 3 (be3eaa5: nbkit's PASS-line scanner read raw stdout chunks, so
the regenerated provenance depended on how the kernel split stdout - found in a fresh clone, 04b); the removal script for the
22 duplicated jupyter workarounds (fe2d80c); phase 3b and 3c scripts (8875805).
ORDER (each step: lead re-check -> commit -> push):
1. As each phase-3a chain ends: lead re-check (Revision: re-run with byte comparison; textbook: nbkit check of every changed
   notebook + check_chapter), commit, push; add index rows (Revision notebooks 25-26, the comparison .wls); TEXTBOOK_SPEC R3
   wording from tb-charge.
2. When NO textbook agent runs any more: `python Revision/workflows/completion/tools_patch.py`;
   `python Revision/workflows/completion/remove_local_jupyter_workarounds.py <the 22 builders that contain python -m jupyterlab>`;
   `python Revision/workflows/completion/add_work_folders.py` (11a, 11b, 15a, 15b, 15d, 19a); then rebuild EVERY notebook
   (nbkit build --date 2026-10-08, then nbkit check) in the background, 4-6 at a time; all 89 (+22b, 23a later) must pass.
3. Launch phase 3b (`completion_phase_3b.js`): chapter 23 + glossary + index (23a), 00c, chapter 05, LOVELOCK_GKD sync.
4. Launch phase 3c (`completion_phase_3c.js`): the two whole reviews with skeptics, fixers, fix-verifiers.
5. Re-assemble the book, build and register its PDF (TEXTBOOK_SPEC section 4, --wide-page-numbers), run every test suite,
   the gate (full), EXECUTION_PROVENANCE_FULL=1, the old Stage-4 gate; verify from two fresh clones; push; notify the user.

### 0.4o PAUSE 2026-10-08 ~10:10 (user: "pause NOW before session limit; push all ...; prepare to restart") - RESTART HERE

State: no workflow, agent or solver/Wolfram/Python process is running (checked).  Everything verified is committed and
pushed (last verified commit ae627be: KOHN_SHAM_DEFLATING_FIELD + DARK_SECTOR_HYPOTHESES, publication tests 34/34 and 27/27
with REVISION_PDF_REBUILD=1).  The commit after it ("WIP at pause") holds UNVERIFIED partial edits of agents that the session
limit stopped at ~08:50: chapters 16 and 17 (+ notebooks 16a-16c, 17a-17b, new figure 17b_6), Revision/docs/
PAIR_CREATION_PROOFS.md (doc-updates, partial), Revision/pairing/kohn_sham/wolfram/verify_t3.wls + reports/wolfram-t3.json
(prov-t3: coefficients now read from ks-theory.json, the tautological clause replaced; run 1 10/10; NOT yet re-verified,
provenance record not yet updated, so tests/test_execution_provenance.py fails for row 5 until prov-t3 finishes).

RESTART (new session, from D:\Developer\github\Dirac_claude):
1. `claude --continue` (or a new session), then: "continue all stages and do not stop".
2. Launch the phase-3a workflow with the Workflow tool: scriptPath
   `Revision/workflows/completion/completion_phase_3a.js` (generated by make_phase3a.py from the phase-2b scripts; every
   interrupted agent gets a RESUME note pointing at its progress log in <scratchpad>/phase2b/<log>.progress.md and is told to
   re-verify the partial edits).  Tasks: doc-updates, prov-t3, revnb-ks-dark, gate, lovelock-compare (comparison of
   curvature.json/Einstein tensor with the author's stored outputs Out[535] RS, Out[536] EinsteinG of the Pair_Creation
   notebook, read-only), fix:16 -> verify-fix -> refix, fix:17 -> verify-fix -> refix, review:19 -> fix -> verify -> refix,
   stage4-diagnose -> stage4-fix -> stage4-verify (old Stage 4; diagnosis so far: the reference delta_scf freezes the
   finest-level occupations - an O(h^2) bias Richardson does not remove; the notebook-time failures came from the N0=60
   pre-floor-rule reference), tb-charge -> verify (charge conservation needs no flux through the brane: chapters 00, 20, 21,
   abstract), tb-22-dark -> verify -> refix (chapter 22 teaches the dark-sector results + notebook 22b).
   NOTE: a new session has a new scratchpad directory; the script's SP constant points to the old one
   (C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad),
   which still exists on this machine and holds the progress logs - keep it.
3. As each chain finishes: the lead re-checks (nbkit check of every changed notebook + check_chapter; re-runs of Revision
   scripts with byte comparison), commits and pushes; adds the index rows the agents report (Revision notebooks 25, 26;
   the comparison .wls); updates the lead-owned texts (Revision/README.md rows if doc-updates did not, TEXTBOOK_SPEC R3 wording
   from tb-charge, LOVELOCK_GKD / PROVENANCE_OF_THE_COMPUTATION sentences from lovelock-compare).
4. Then phase 2c of section 0.4n: the tool patch `<scratchpad>/tools_patch.py` (copy kept in
   Revision/workflows/completion/tools_patch.py; tested in a scratch worktree: lint OK) + rebuild all 89 notebooks; the
   lead-check record corrections; 00c report list; chapter 23 with the glossary; the whole-Revision review; the book review;
   assembly, PDF registration; EXECUTION_PROVENANCE_FULL=1; fresh-clone verification; push; notify the user.

### 0.4n COMPLETION RUN, STATE 2026-10-08 07:00 (phase 1 running, phase 2a launched)

Done and pushed since 0.4m (each verified): gkd provenance run-time ranges (81ab063); ks-theory provenance 57/58
discrepancy resolved by dc6904e (fd94926); `dirac matrices.md` lists its files with sha256 (c30e170, 67/67, test 7/7);
primordial provenance 6.4 status (61d5133; the ORIGINAL textbook provenance/DIRAC16COMPLEX_TEXTBOOK.* stays unmodified by
the user's order of 2026-10-02, so its 2026-09-30 sample gate output keeps the old digest - this is intended).
Written, NOT yet committed (commit when green): `provenance/EXECUTION_PROVENANCE_INDEX.md` (23 sets + textbook notebooks)
and `tests/test_execution_provenance.py` (fails only for rev-a4 and verify_t3.wls until phase 1 updates their records).
Phase 2a workflow (wf_45e4b2cb-7b4; script `Revision/workflows/completion/completion_phase_2a.js`, reviews of 14-17 in the
same folder): LOVELOCK_GKD document + publication test; textbook fix 14, 15; review->fix 18, 20, 21, 22.
Phase 2b (after phase 1; lead): verify + commit every phase-1 result; provenance records for every changed or new .wls
(verify_t3.wls, new dark-sector/ks_source sets); the documents KOHN_SHAM_DEFLATING_FIELD and DARK_SECTOR_HYPOTHESES and the
wave-1 document updates; Revision/notebooks/ (SPEC section 10); the gate Revision/verify_revision.{ps1,sh} + test; textbook
16, 17, 19 (reviews exist for 16, 17 in workflows/completion/review_1[67].json; 19 needs a review); chapter 23; the
shared tool fix (run_instructions.py troubleshooting: `python -m jupyter` fails where jupyter is not on PATH - use
`python -m jupyterlab` / `python -m nbconvert`; then rebuild all 89 notebooks); the lead-check record
`Revision/lead_checks/charge_conjugation_and_u1.py` detail text of `bilinears_under_charge_conjugation` (its parenthetical
"normal ordering supplies one more sign" is contradicted by the proof of textbook section 5.34 and Notebook 05e; correct the
record, then chapter 05/05c/05e/21 and 00c); the whole-Revision review; the book review; re-assembly, PDF registration;
fresh-clone verification; push; notify the user.
UPDATE 07:50: committed and verified since: chapters 01-09, 03, 12 (lead re-check: nbkit check of every notebook + check_chapter),
dark_sector/dirac16complex (dd20166), ks_source + dark_sector/dirac16complex00 (26c0424), the index + its test + the rev-a4 record
(4122f2f), nb-kohn-sham record (d2dd531).  Phase 2b-1 launched (wf_6cda14c3-c49: doc-kohn-sham, doc-dark-sector, fix:16, fix:17,
stage4-diagnose); phase 2b-2 (Revision/workflows/completion/completion_phase_2b2.js: doc-updates + Revision/README, revnb-ks-dark,
gate, prov-t3, review/fix 19) waits for the T3 agent and the first Revision notebook.  MORE FOLLOW-UPS for phase 2c: (1) lead-check
record charge_conjugation_and_u1.py also: u1_noether_matrix_identity detail says Q is conserved without the boundary-flux caveat
(chapter 10 and DIRAC16COMPLEX_FIELD_THEORY section 11 say conservation needs a condition at z = pi/2); (2) a4 verifier failure
paths (rev-a4 record part 6.5: a missing lovelock-tensors.json gives FAIL checks instead of an ERROR line; a4-equations.json is
written before the report) - fix, then re-verify the record; (3) notebook 00c asserts the list of 27 Revision reports: update it
once all wave-2 reports are final, rebuild 00c; (4) run EXECUTION_PROVENANCE_FULL=1 tests/test_execution_provenance.py when no
agent writes in the tree.
UPDATE 08:40: phase 1 and phase 2a COMPLETE; everything verified by the lead and committed (chapters 00-15 except 00c's
report list, 18; KS cross-check 31/31; T3 completion; dark sector x2; ks_source; LOVELOCK_GKD; Revision/notebooks/
lovelock_gkd).  Running: phase 2b-1 (wf_6cda14c3-c49), phase 2b-2 (wf_4b4a4104-32c), agent lovelock-compare (new folder
Revision/gkd_lovelock/comparison/: the comparison with the author's own Lovelock outputs that PROVENANCE_OF_THE_COMPUTATION
announced but never recorded).  PHASE 2C LIST (lead, after the textbook agents finish): (a) tools: run_instructions.py
troubleshooting (python -m jupyterlab / python -m nbconvert), nbkit provenance text (notebooks 15a/15b/15d write solver output
into git-ignored target/textbook_* folders), walkthrough_diff false positives (blank line after an omitted docstring; '*'
inside a code span of a heading); then rebuild all 89 notebooks and remove the local workarounds (00a-00d, 10a-10g);
(b) lead-check record charge_conjugation_and_u1.py: the normal-ordering remark and the u1 conservation caveat; then 05c,
05e, chapter 05, and the qualification 'charge constant only with no flux through the brane' in chapters 00 (l.74), 20,
21, 22, abstract.md and TEXTBOOK_SPEC R3 (chapter 18 and 10 already corrected); (c) 00c report list; chapter 20 l.2868 vs
chapter 21 Proposition 2; record that R3's 'complete proofs' are met by chapters 18-20 together; (d) chapter 23 incl. the
glossary words reported by the fixers of 08, 11, 18, 20, 22; (e) a4 verifier failure paths; (f) old Stage 4 fix (after the
diagnosis); (g) whole-Revision review; book review; assembly; PDF registration; EXECUTION_PROVENANCE_FULL; fresh clones.

### 0.4m COMPLETION RUN 2026-10-08 (user: "continue and complete the stages that are still open")

Done directly (verified): the a4 author-T16 patch applied with its Revision-side sync (e377368; dirac matrices.md answers
'Instruction followed: yes', 67/67); wave-1b theory reconcile verified (check_field_theory.py 70/70, comparison agree,
byte-identical from a fresh clone).  PHASE 1 workflow `Revision/workflows/completion/completion_phase_1.js` (run
wf_0a79c6af-dca; generated by make_phase1.py from the original scripts and the journals; inputs review_*.json, verify_*.json):
KS full cross-check; wave-2 science (dark sector for both fields, a4 with the KS source, T3); provenance records rev-a4 and
nb-kohn-sham; textbook fixers for chapters 00-03, 05-10, 12, 13 (with the a4 sync of 00, 09, 12 and the quoted-code audit);
review and fix of chapter 11.  Every agent is bounded (~45 min, progress notes in <SP>/phase1/<label>.progress.md).
PHASE 2 (after phase 1): wave-2 documents (KS, dark sector, Lovelock/GKD; update the three wave-1 documents), Revision
notebooks, the reproduction gate verify_revision.{ps1,sh} + test, a review of the whole Revision record with skeptics and
fixes; textbook chapters 14-22 (fixes; reviews of 18-22), chapter 23, the book review, rebuild and registration; the
execution-provenance index and its test.

### 0.4l FINAL STATE 2026-10-08 (user stopped all work; Claude handed over)

User, 2026-10-08: "NEVER wait more than 60 seconds ... KILL ALL OF THESE RIDICULOUSLY LONG AGENT JOBS ... push everything and verify
repo, and QUIT. GPT-5.6 will take over."  All workflows were stopped (TaskStop) and every agent process was killed (0 left).  Work
committed and pushed.  `.claude/ALLOW_STOP` exists (delete it to re-enable the Stop hook).  Lesson for the successor: the agent
tasks were posed far too large (single agents ran for hours); split work into small, checkable steps and never block on long waits.

DONE AND VERIFIED
* `provenance/dirac matrices.md` (user order of 2026-10-07): generator `provenance/dirac_matrices/build_dirac_matrices_md.py`,
  extractors `extract_from_author_notebook.wls` (the author's own cells, in the author's In[n] order) and
  `extract_repository_wolfram_gammas.wls`; 66/66 exact checks; adversarial audit complete (23/23 confirmed findings fixed; independent
  fresh-clone verifier: 5 MINOR findings left, listed in `Revision/workflows/state_restart/dirac_audit_verify_findings.json`).  It
  answers measured: "Instruction followed: not completely" - every calculation uses eight real 16x16 Cl(4,4) matrices and all but
  the Revision a4 engine use the author's T16 entry by entry; the a4 engine uses an exactly equivalent Cl(1,1)^(x)4 basis.  With the
  a4 patch applied (below) a scratch rerun gave 67/67 and "yes".
* Primordial verifier false-success fix (b980c80), verified from a fresh clone; its provenance file updated by its fixer.
* Execution provenance, sets fully through runner -> independent verifier -> fixer: rev-algebra, rev-ks-theory, rev-pairing-ks,
  rev-pairing, rev-theory, rev-gkd-notebook-reading, old-nb-build-dark, old-nb-build-ks, old-nb-verify-dark, old-nb-verify-ks,
  old-algebra, old-geometry, old-primordial, old-kohn-sham, old-00, old-pairing, old-matter-antimatter, nb-dark-sector, handoff-probes.

FIXED 2026-10-08 after the handover note (verified):
* GKD verifier false-success defect fixed and its outputs regenerated (1f7d31b): verify_lovelock_gkd.wls prints
  'ERROR: cannot write ...' and exits 2; report 29/29 (only the script-sha line changed); test pin and
  WOLFRAMSCRIPT_PROVENANCE.md updated; test_gkd_lovelock OK incl. slow tests.
* PAIR_CREATION_PROOFS: KS-theory count 58 and the section-10 run order (dc6904e); PDF re-registered; 23/23 tests.
* Book PDF registered warning-free (c55c6cd) after the root cause of the 637 overfull boxes (four-digit page numbers
  in the contents) was fixed by the opt-in builder option --wide-page-numbers (e35bce6).

* Final book PDF (after the chapter 03 and 13 fixes) rebuilt warning-free and re-registered; GKD/pair-creation/field-theory
  and lead-check tests pass from a fresh clone.
* Textbook notebooks 13a/03b fixed and rebuilt, chapter 13's walk-through aligned with Notebook 13a (5041c5b); all 89
  notebooks pass nbkit check; book re-assembled.
FOLLOW-UP (textbook quality, not covered by any test): the walk-throughs quote notebook code by hand, and several
  builders were changed by interrupted chapter fixers after their chapters were written.  CONFIRMED drift: chapter 03 quotes
  an older version of Notebook 03b's In [3] (no PYTHON_REPORT/RUST_REPORT lines) and further cells - FIXED in 6df74c8 (every
  quoted block of the 03b walk-through now matches; record_check explained).  The scratch audit tool
  Revision/textbook/tools/audit/walkthrough_diff.py (+ walkthrough_all.py) compares quoted blocks with the notebook cells;
  it knows three deliberate conventions (captions shortened with '...)', docstrings omitted, the generated set-up cell) but
  its section detection is NOT reliable (it can pick up a mention of a walk-through as the section start), so its counts
  are an upper bound, not a list of defects.  A careful pass per chapter is needed.

NOT DONE / IN PROGRESS (partial edits are committed and UNVERIFIED)
* Execution provenance: rev-gkd-verification - its verifier found a MAJOR false-success defect (verify_lovelock_gkd.wls exits 0 /
  SUCCESS when it cannot write the report) and wrong temp-file text; NOT fixed.  nb-kohn-sham - verified (9 minor), not fixed; the
  old Stage-4 notebook's gauntlet fails 2/60 by design (old Stage 4 unfinished: user decision pending - finish or mark superseded by
  Revision/kohn_sham).  rev-a4 - fix HELD for the a4 patch.  The index provenance/EXECUTION_PROVENANCE_INDEX.md and
  tests/test_execution_provenance.py were NOT written.  All findings: state_restart/state_execution_provenance.json + journals.
* a4 author-T16 patch: `Revision/workflows/a4_patch/a4_author_gammas.patch` is ready, reviewed (2 reviewers) but NOT applied.  Apply it
  only together with the downstream list of section 0.4k (three Revision publications + PDFs + test pins, Revision/README.md table,
  the rev-a4 provenance file, dirac matrices.md regeneration, textbook chapters 00/09/12/17 and notebooks 00c/09c/12a/17b).  A
  prepared workflow for the Revision part: Revision/workflows/restart/a4_apply_sync.js (too large as one run - split it).
* Textbook "Universes in Pairs": ASSEMBLED 2026-10-08 (Revision/textbook/UNIVERSES_IN_PAIRS_TEXTBOOK.md, assemble_textbook.py 13/13
  checks, chapters 00-23, 89 notebooks, 556 figures; chapter 23 is a marked PLACEHOLDER).  PDF: Revision/textbook/UNIVERSES_IN_PAIRS_
  TEXTBOOK.pdf, 6082 pages, REGISTERED as edition universes-in-pairs-textbook (sha256 adb599cf511b...), warning-free, two
  independent builds byte-identical.  The 637 Overfull-hbox warnings of the first build were all table-of-contents entries on
  pages >= 1000 (four-digit page numbers in LaTeX's 1.55em box); fixed by the opt-in builder option --wide-page-numbers
  (e35bce6), which changes no other document.  Build command: TEXTBOOK_SPEC section 4.
  Every chapter's notebooks are built (00-22); chapter texts exist for 00-22 (chapter 21's text WAS written, 4891 lines, by the
  interrupted writer - not yet reviewed); adversarial reviews done for 00-10 and 12-16 with findings (several major: overclaims in 08, 10, 14; physics wording
  in 03, 05, 09, 13; numbers not asserted in 12; figure caption in 16); only chapter 04's fixer finished.  The six-lens book review and the book fix were NOT done.  Revision/tests/test_universes_in_pairs_textbook.py fails.
* Revision wave 1b: the Mermin-root repair is done and verified (solver 42/42, determinism 14/14, KS theory 58/58, cross-check 29/29).
  NOT done: theory-reconcile (partial edits may be in Revision/theory), the full KS cross-check, the reproduction gate, review, fix.
  Wave 2 NOT started.  Known failing test: test_pair_creation_proofs_publication (document quotes 57 KS-theory checks; the record has 58).
* Cross-workflow sync obligations: section 0.4h/0.4k lists (textbook notebooks reading changed KS outputs; provenance hashes).

### 0.4k A4 AUTHOR-T16 PATCH READY (2026-10-08 04:40; implementer of wf_e7ec46e7-1bf; its reviewers/verifier still running)

Patch <SP>/restart/a4prep/a4_author_gammas.patch (896 lines, sha256 7af48ee9..., 7 files under Revision/field_equations_a4/):
both engines take the author's T16 from gammas.json as the primary representation (strict reading; ERROR + exit 1 for every
malformed-fixture case, a missing package, an unwritable output); Cl(1,1)^(x)4 / own_rep kept only as labelled comparison
representations with exact intertwiner checks (dim 1; K^T K = 2 I16 resp. 8 I16; K C = C_T16 K) and the representation-independence
check.  a4-equations.json BYTE-IDENTICAL.  Wolfram 47 -> 52 checks, Python 61 -> 63, all pass, none removed.
APPLY it only together with ALL downstream updates, in one sync workflow, after the textbook chapter stages of 09, 12, 17 are done:
 (1) Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md (+tex/pdf): witness S = 51200, 28800, 51200 in the author's T16 (204800, 115200,
     204800 was the Cl(1,1)^4 normalisation; |v|^2 = 200 vs 400; w = {4,3,4} and S != 0 unchanged); index line 823: wolfram-a4 52,
     python-a4 63; Revision/tests/test_dirac16complex00_field_theory_publication.py line 476.
 (2) Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md line 17 (+tex line 47): 'Wolfram: 52 of 52; sympy: 63 of 63'.
 (3) Revision/docs/PAIR_CREATION_PROOFS.md lines 489-490 (52, 63) and line 492 (KS theory 58); section 10 run order.
     Rebuild + re-register each PDF (Revision/pdf-specifications.json), re-pin MARKDOWN_SHA256/TEX_SHA256 in the three tests.
 (4) Textbook: chapter 12 line ~757 (63 and 52); chapter 09 near line 2786 + notebook 09c (witness S; common factor 40000 instead of
     160000); 17b PROVENANCE counts; rebuild and nbkit --check every notebook that reads the a4 reports (00b, 00c, 02c, 03b, 09a, 09c,
     12a-12d, 17a, 17b, ...).
 (5) Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md (the HELD rev-a4 fix: new hashes, 52 checks, ERROR exits, run
     times 43-70 s, plus its verifier findings under verify:rev-a4 in state_execution_provenance.json).
 (6) Regenerate provenance/dirac matrices.md with its builder (the a4 engine then uses the author's T16).
 Open, out of scope of the patch: check_field_equations_a4.py ends with a traceback (not an ERROR line) when a report cannot be written.
 ADDED by the patch reviewers (2026-10-08): Revision/README.md line ~113 (a4 report counts; textbook notebook 00c asserts this table);
 DIRAC16COMPLEX00 doc rows ~786, 854, 860-861 must cite the author-T16 checks as primary evidence; a sentence that S depends on the
 null-vector normalisation; the rev-a4 provenance file's supplementary script must use FEGammaFrameComparison.  TEXTBOOK PART (run only
 after the textbook fixers of chapters 00, 09, 12, 17 are done): rebuild notebooks 00c (+figures), 09c, 12a, 17b and every notebook reading
 the a4 reports; chapter 00 lines ~1596 and ~3056 (947 / 382 / 458 totals); chapter 09 line ~2786 (record uses T16; factor 40000);
 chapter 12 line ~757 (63, 52); 09c prose 'own (equivalent) representation' -> the author's T16.
 SYNC WORKFLOW (Revision part): Revision/workflows/restart/a4_apply_sync.js (set SP); launch after the a4 prep and the dirac audit verifier finish.

### 0.4i RESTART KIT - PAUSED 2026-10-07 20:30 BEFORE A SESSION LIMIT

User, 2026-10-07: "pause NOW before session limit; push all and check repo; prepare to restart after a session limit; continue all
stages and do not stop".

State at the pause: ALL workflows were stopped (TaskStop) and every agent process was killed and checked (0 Wolfram, Python or Rust
processes left).  Everything is committed and pushed.  `.claude/ALLOW_STOP` exists: delete it on restart so that the Stop hook
works again.  The finished results of every run are in `Revision/workflows/state_restart/state_<family>.json` (families textbook,
execution_provenance, dirac_audit, wave_1b_2, a4_prep), plus `audit_confirmed.json` (the 23 skeptic-confirmed audit findings).
Agents stopped mid-task left partial, committed, UNVERIFIED edits; the restart scripts tell their agents to inspect and finish them.

RESTART (same conversation or a new session).  Do these steps in one go, then never end the turn while stages run.
1. `cd D:/Developer/github/Dirac_claude && git pull && rm -f .claude/ALLOW_STOP`
2. Copy `Revision/workflows/restart/*.js` and `Revision/workflows/restart/next_event.py` to the session scratchpad <SP>, and set SP
   in every .js file: `for f in <SP>/*.js; do sed -i "s|<SCRATCHPAD OF THE RUNNING SESSION>|<SP>|" "$f"; done` (keep ROOT; LF).
3. Launch with the Workflow tool (scriptPath = the <SP> copy), all five at once:
   a. `textbook_restart.js`: notebooks of chapters 11 and 21; writers of every chapter except 02 and 12; reviewers and fixers of all
      chapters; assembly; the six-lens book review with skeptics; book fix; fix verifier.
   b. `execution_provenance_restart.js`: fixers of the 13 verified-but-unfixed sets, the runner of nb-kohn-sham, the verifiers of
      handoff-probes, old-nb-verify-ks, rev-gkd-verification and rev-theory; rev-a4's fix stays HELD (step 4); then index and test.
   c. `dirac_matrices_audit_fix_restart.js`: one fixer for all 23 confirmed findings, then a fresh-clone verifier.
   d. `revision_wave_1b_restart_then_2.js` (it loads <SP>/revision_wave_1b_restart.js and <SP>/revision_wave_2.js): wave 1b from
      theory-reconcile on (the Mermin fix and the wave-1 fix verifier are done), then wave 2.
   e. `a4_author_gammas_prep.js`: the a4 author-T16 patch in a scratch clone, reviewed and verified, written to
      <SP>/a4prep/a4_author_gammas.patch.
4. LEAD ACTIONS while they run.  When (e) is verified: apply the patch to the repository, re-run both a4 engines
   (a4-equations.json must stay byte-identical), commit; then run one agent to update
   Revision/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md (the held rev-a4 fix, including its verifier findings under key
   verify:rev-a4 in state_execution_provenance.json); regenerate `provenance/dirac matrices.md` with its builder; re-check textbook
   chapters 12 and 17 against the new a4 report counts.  Then the CROSS-WORKFLOW SYNC OBLIGATIONS recorded below (pair-creation
   count 57 -> 58; textbook notebooks that read changed Kohn-Sham outputs; provenance hashes).
5. Stay in the turn: `python <SP>/next_event.py 540 <session dir>/subagents/workflows` blocks until any agent finishes and prints
   its result; act on each result; commit and push a snapshot about every 15 minutes (the Stop hook does not run while the turn
   continues).
6. After another session limit: do NOT rely on resumeFromRunId for pipelined workflows (on 2026-10-07 it re-ran finished agents).
   Merge the journals into new state files with `Revision/workflows/restart/merge_state.py` (pre-resume results of resumed runs,
   all results of continuation runs; edit its run-id table) and regenerate the restart scripts with `make_restart_scripts.py`.

### 0.4h STATE 2026-10-07 20:15 (after the second session limit)

The session hit its usage limit at about 19:50 (reset 20:00 PDT); every running workflow lost its unfinished agents.  Resuming with
resumeFromRunId re-ran FINISHED agents too (the cached prefix breaks as soon as concurrent calls come back in another order), so the
lead STOPPED the resumed textbook, execution-provenance and audit runs and launched CONTINUATIONS that take the finished results
from the journals (saved in `Revision/workflows/state_2026-10-07/state_<run>.json`, copied to <SP>) and run only unfinished stages:
* `Revision/workflows/textbook_universes_in_pairs_cont.js` - run wf_1964f603-07f (notebooks of ch. 11 and 21; writers of every chapter
  except 02 and 12; reviewers and fixers of all; assembly; book review; book fix).
* `Revision/workflows/execution_provenance_cont.js` - run wf_5cf02970-bb6 (fixers of 13 verified sets, run of nb-kohn-sham, verifiers
  of handoff-probes, old-nb-verify-ks, rev-gkd-verification, rev-theory; rev-a4's fix is HELD until the a4 patch is applied; index).
* `Revision/workflows/dirac_matrices_audit_fix.js` - run wf_ff12b9f0-bb0 (fixer for the 23 skeptic-confirmed findings in
  state_2026-10-07/audit_confirmed.json, then a fresh-clone verifier).
Still running from before (resumed, they re-ran only failed agents): the wave 1b -> wave 2 chain wf_987b1061-79b and the a4 prep
wf_da94d8ca-701.  Lesson: for pipelined workflows never rely on resumeFromRunId after a session limit; write a continuation from the
journal.  The primordial false-success fix is DONE (b980c80, verified from a fresh clone).

### 0.4f STATE 2026-10-03 (after the session limit)

The session hit its usage limit on 2026-10-02 (resets 09:50 America/Los_Angeles); both workflows lost the
agents that were running (textbook 32 of 42, execution provenance 4 of 66).  Both were RESUMED in the same
session with resumeFromRunId (finished agents replay from cache): textbook run wf_4139c503-a3e and execution
provenance run wf_6845510e-6a4.  Snapshot 06c2d25 holds the partial files.  Known and expected until the
pipelines rebuild them: notebooks built before 4fc381d (the run-instruction list fix) fail
test_universes_in_pairs_textbook's three-renderings test.  If a NEW session must take over (no cache):
relaunch both scripts from Revision/workflows/ with the new SP (agents inspect and finish existing files),
then rebuild every textbook notebook with `python Revision/textbook/tools/nbkit.py build <builder>` and
check with `nbkit.py check`.

### 0.4e CURRENT TASK (user, 2026-10-02): the NEW deep-dive textbook "Universes in Pairs"

The user stopped all stages and ordered, first: preserve the original textbook
(`provenance/DIRAC16COMPLEX_TEXTBOOK.*`, never modified) and create an updated, correct, complete,
RE-NAMED teaching textbook (.md/.tex/.pdf) with a complete executed Jupyter notebook for EVERY
example, complete self-contained run instructions just before each notebook's text (and as comments
in the notebook), the deep-dive technique, and many more plots.  Binding spec:
`Revision/textbook/TEXTBOOK_SPEC.md` (honesty rule R3: the pairing theorems are proved; creation and a
solution of the matter-antimatter problem are not - the user was told this on 2026-10-02).
Workflow `Revision/workflows/textbook_universes_in_pairs.js` RUNNING (relaunched 2026-10-02 as run wf_4139c503-a3e after the
user's STOP and error report; spec rules R5 charge conjugation as a MATRIX and R6 a provenance file per notebook added): infra
(nbkit, run instructions, renderer, assembler, pilot) -> 23 chapters pipelined (notebooks -> writer ->
adversarial reviewer -> fixer) -> assembly (chapter 23, ledger, PDF, registration, test) -> six
whole-book review lenses with two skeptics per finding -> fixers -> rebuild -> fix verifier.
Outputs: `Revision/textbook/` (chapters/, notebooks/, notebooks/src/, figures/, tools/,
UNIVERSES_IN_PAIRS_TEXTBOOK.{md,tex,pdf}), test `Revision/tests/test_universes_in_pairs_textbook.py`.
If a restart finds the run gone: copy the script to the new scratchpad, set SP, relaunch; agents
inspect and finish existing files.
ERROR REPORT (user, 2026-10-02): "complex conjugation Psi -> Psi*" is not charge conjugation for real fields - a
MATRIX operator is needed.  Fixed: Revision/lead_checks/charge_conjugation_and_u1.py (12/12): calC_+ = C (sigma16),
calC_- = Gamma C; for real fields the nontrivial real map is Gamma with m -> -m; the quantised field's conjugation
preserving {Psi, Psi^dagger} = B delta is Gamma (mass reversed).  Spec rule R5.
SECOND NEW TASK (same message): test and verify every wolframscript set and every Jupyter notebook and write a
provenance file for each (student instructions, expected output, side effects).  Workflow
`Revision/workflows/execution_provenance.js` RUNNING (run wf_6845510e-6a4): 22 items (8 Revision Wolfram sets,
11 old scripts/*.wls sets, the handoff probes, the 2 notebooks/*.ipynb), each run twice in a fresh clone, documented,
then verified by an independent agent following the provenance file literally, fixed; index
provenance/EXECUTION_PROVENANCE_INDEX.md and tests/test_execution_provenance.py.  The textbook notebooks get their
provenance files from nbkit (R6).
STOPPED for it (resume afterwards, "continue with all stages"): Revision wave 1b (run wf_39a30fcf-75b,
stopped in its Fix phase; commit 667f153 holds the unverified partial edits of fix:science:0; resume
with resumeFromRunId in the same session, otherwise relaunch `revision_wave_1b.js`), then wave 2.

### 0.4d STATE 2026-10-01 (resumed session)

The repository now lives at `D:\Developer\github\Dirac_claude` (drive C: was nearly full).  The workflow
scripts in `Revision/workflows/` carry `ROOT = 'D:/Developer/github/Dirac_claude'` and the `SP` of the
session of 2026-10-01 afternoon; a new session copies them to its scratchpad and sets its own `SP`.

* Wave 1 (`revision_wave_1.js`, run wf_6f22a73c-e62): COMPLETE, commit 70fab64.  19 agents; every stage
  passes its checks; review 27 findings (10 major, 17 minor), all fixed (record:
  `Revision/workflows/wave1_review_and_fix.json`).  Physics corrections of the review: gamma^mu Omega_mu is
  frame dependent (non-triviality stated with its exact scope); the extra-time evolution is Hadamard
  ill-posed; the dirac16complex00 energy is unbounded below; the Kohn-Sham states violate the a4 source
  conditions (x8 dependence, p3 + p_t = 2 p8), so the Kohn-Sham history is a PRESCRIBED BACKGROUND; T3 proved.
* Fresh-clone check of 1c297d6 by the lead: all 12 verifiers exit 0; python-field-theory.json was stale
  (energy_exchange "DISAGREE"); the lead's own sympy derivation: nabla_mu T^mu_x4 gives
  d rho/d x4 = -3 a4' (p3 - p_t), nabla_mu T^mu_x8 gives d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0, all other
  components identically zero (both sides were right; they stated different components).
* Wave 1b (`revision_wave_1b.js`, run wf_39a30fcf-75b, RUNNING): Rust Mermin mu repair (rounding-limited
  in N8_lamm1_a00_T10), prescribed-background label in ks-theory.json, theory comparison verification,
  wave-1 fix verification, FULL-matrix Kohn-Sham cross-check, fresh-clone reproduction gate, two skeptics per
  item, per-area fixers, fix verifier.  It reads `<SP>/w1_args.json` (= the committed record above).
  Checkpoint 2026-10-01 (second pause request): snapshot a9a1b70 adds the full-matrix reference results
  (Revision/kohn_sham/reference/results, 338 files, 24 MB) and the repaired Rust outputs, still under review.
  Lead check 2: `Revision/lead_checks/einstein_gauss_bonnet_a4.py` (15/15).
  Checkpoint 2026-10-01 (pause request): snapshot commit daeb5ba holds its partial work (new
  `solver/src/mermin.rs`, the prescribed-background label in ks-theory.json, the theory comparison edits),
  NOT yet reviewed.  If a restart finds the run gone: relaunch `revision_wave_1b.js` (copy
  `Revision/workflows/wave1_review_and_fix.json` to `<SP>/w1_args.json` first); its agents inspect and
  finish the existing files.
* Lead's independent checks: `Revision/lead_checks/` (10/10; conservation identities, gamma^mu Omega_mu =
  3 H gamma^(x8), negative control with inflating extra times), test `Revision/tests/test_lead_checks.py`.
* NEXT: commit and push wave 1b; then `revision_wave_2.js` (dark sector with stated observer assumptions
  for the time-like extra times, a4 with the Kohn-Sham source starting from the source-condition
  violation, T3 verification and numerics, documents, notebooks, gate, five-lens review with skeptics).

### 0.4c CURRENT TASK (user, 2026-10-01, later): `Revision/` - a new, separate record

The author asked for a completely new record, in the new folder `Revision/`, of new calculations for the
author's primordial metric (x8 hidden, x4 time, x5..x7 deflating extra times): both Lagrangians with the
canonical spin connection, non-triviality tests [1] and [2], field equations, EMT operator, KE, PE,
pressure, energy density, EoS, canonical quantisation in 4+4, the field equations for a4[x4]
(Einstein-Lovelock with the GKD Lovelock tensors), Kohn-Sham ground and first excited states, the two
dark-sector hypotheses against the Unite values of the private PDF, the pairing proofs, md/tex/pdf.
Binding: `Revision/SPEC.md`; task verbatim in `Revision/README.md`.  NOTHING from the old stages is
mixed in.  The GKD work was moved into `Revision/gkd_lovelock/` (git mv).

### 0.4b CURRENT TASK (user, 2026-10-01): GKD and the Lovelock tensors (the user's test)

The user found the Lovelock treatment deficient and set a test: refactor the author's kδ
(`kδ[lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]`, notebook
`Generalized _Kronecker_Delta_4+4.nb`, now tracked at the user's request; `Generalized_Kronecker_Delta.*`
is ignored) into a pure-Rust `GKD`, use it to compute, with provenance, the three non-zero Lovelock
tensors of Lovelock's (4.38) (the user's In[68], an image cell) for the user's 8x8 test metric (x8 hidden,
x4 time, x5..x7 deflating extra times), write every component, PROVE the work was done here without
reading the user's answers, with student instructions, Jupyter notebooks (rustSolveIt style), md/tex/pdf.
DONE by the lead: `studies/lovelock_gkd` (GKD with proof, exact Laurent-polynomial engine, curvature,
Lovelock sums), outputs `artifacts/lovelock-gkd/` (19/19 checks; GKD = literal determinant on all
16,777,216 length-4 pairs; two runs byte-identical), committed BEFORE any comparison (commit 3e81eeb,
2026-10-01 07:15) with `PROVENANCE_OF_THE_COMPUTATION.md`.  RUNNING: `handoff/workflows/wf_lovelock_gkd.js`
(independent sympy checker, Wolfram GKD = kδ check, Jupyter notebook, provenance/LOVELOCK_GKD.*, reviews,
fixer).  NEXT: commit; THEN, in a separate commit, compare with the author's answers (convention-aware)
and add that section; then integrate the Lovelock tensors into Stage 2 / the textbook (ledger L25) and
resume 0.4a.

### 0.4a NEW TOP PRIORITY (user, 2026-09-30 ~18:40): the deflating extra times

The user: "x5, x6, x7 are the three extra times that exponentially deflate. Fix this everywhere
they appear, and fix your docs and provenances"; asked, the user chose "Redo the physics".
Binding: `handoff/specs/DEFLATION_SPEC.md` (a4 = A t for all t, A = 1, 2; EXP-1 without the
window, EXP-2 from the notebook's deflation, EXP-3/EXP-4 with exponentially deflating extra
times, Stages 4/5 as instantaneous (adiabatic) Kohn-Sham states along a4 = A H x4 with an
adiabaticity analysis, TDDFT OPEN; every document and the textbook updated).  State: the spec is
written (commit 2e02e5e) and under adversarial review (physics, faithfulness, feasibility;
`handoff/workflows/wf_deflation_spec_review.js`, read-only reviewers; it was still running at the
pause of 2026-10-01 ~00:00 - after a restart rerun it, amend the spec with the confirmed findings,
commit); then write and run the implementation workflows of DEFLATION_SPEC D14.  Feasibility
checked by the lead: the Kohn-Sham crate (geometry.rs, shooting.rs, runs.rs) and the reference
solver already take a4_0 != 0 and check the E4.10 rescaling identity, so the slice series of D8
reuses them via a new `deflating` subcommand.  The textbook built before this
correction (671 pages, commit 4ede502) describes the static/frozen/window models and must be
updated by D12.  Sections 0.4 A-E below describe the state before the correction and remain
the to-do list for the parts the correction does not replace.

### 0.4 State at the pause of 2026-09-30 15:05 and the exact order of work

The user's priority (2026-09-30 12:10): the TEXTBOOK first, then the other stages.

A. Textbook (`handoff/specs/TEXTBOOK_SPEC.md`; chapters in `provenance/textbook/chapters/`).
   * Chapters 00-05, 08-13: written and adversarially reviewed (198 findings, skeptic-
     verified, fixed; `handoff/workflows/wf_textbook_wave_a_review.js`); cross-chapter
     items the per-chapter fixers could not apply: `handoff/reviews/textbook_wave_a_carryover.json`.
   * Chapters 06, 07, 14, 15, 16, 17, 18: written, reviewed and fixed
     (`handoff/workflows/wf_textbook_wave_b_chapters.js`).
   * 18:28 (pause): `wf_textbook_final.js` phases Carry-over, Ledger and Assembly DONE: the book
     `provenance/DIRAC16COMPLEX_TEXTBOOK.{md,tex,pdf}` is assembled (21 chapters, 350 sections, 3610
     references resolved), the PDF is 671 pages, warning-free, byte-identical in two builds, numbered
     from 0, registered (`provenance/pdf-specifications.json` entry dirac16complex-textbook), pinned by
     `tests/test_d16c_textbook_publication.py`.  RUNNING at the pause: the nine whole-book review
     lenses; then skeptics, per-chapter fixers and the rebuild.  After a restart: rerun
     `wf_textbook_final.js` from its Review phase (comment out the Carry-over, Ledger and Assembly
     agents, or let them re-check: they only fix what they find), then push.
   * 15:55: chapters 19 and 20 written, reviewed and fixed; the whole book (21 chapters) passes
     `python scripts/build_textbook.py --check` (12/12); `wf_textbook_final.js` launched (run
     wf_0b6d5db2-c76).  If a restart finds it unfinished: rerun `wf_textbook_final.js` (its agents
     inspect and finish partial work).  The notes below are kept for reference.
   * Chapters 19 and 20: the writer was still running at the pause.  After a restart:
     if `20-glossary-and-check-index.md` is missing or incomplete, run
     `wf_textbook_wave_b_chapters.js` with `TASKS` reduced to the `back` entry (writer,
     reviewer, fixer of chapters 19 and 20).  Chapter 19 had CRLF line endings: convert to LF.
   * Then run `handoff/workflows/wf_textbook_final.js` (carry-over items, final honesty
     ledger of Chapter 0 and Stage-4 status in Chapter 13, assembly with
     `scripts/build_textbook.py`, PDF with `--developer-layout --number-sections-from-zero`,
     registration, `tests/test_d16c_textbook_publication.py`, nine whole-book review
     lenses, skeptics, per-chapter fixers, rebuild and re-register).  Push.
B. Matter-antimatter (`provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.*`): COMPLETE 2026-09-30 15:40 -
   Wolfram 44/44 (twice, byte-identical), Python 77/77 (twice, byte-identical), all 49 tests of
   tests/test_d16c_matter_antimatter*.py pass, PDF 36 pages registered; 17 of the 18 review findings
   fixed, the 18th (Chapter 0 'no CP violation') belongs to the textbook final workflow.  When the
   Stage-5 documents and gate are complete, change the PROVISIONAL status strings in
   wolfram/Dirac16ComplexMatterAntimatter.wl (stage5Krein, M4/M5 statements) and
   scripts/check_dirac16complex_matter_antimatter.py, rerun both, rebuild the PDF.
C. Stage 5: exact theory COMPLETE (Wolfram 00 46/46, pairing 141/141; sympy 00 49/49,
   pairing 172/172, all under `artifacts/dirac16complex/pair-creation/`).  Numerics partial:
   `rust/pairs/` has run folders but no `summary.json`; `scripts/ks_reference_pairs.py
   --workers 10 --resume` was stopped at 12:12 (partial `reference/`).  After the textbook:
   rerun the `rust-pairs` and `reference-pairs` agents of `wf_stage5_theory_numerics.js`
   (the pairs checker scripts/check_dirac16complex_pairs.py on the partial outputs gave 71 checks,
   8 failed, at 15:10 - expected while the runs are incomplete)
   (and its checker), then `handoff/workflows/wf_stage5_docs_review.js` (documents
   DIRAC16COMPLEX00_FIELD_THEORY and DIRAC16COMPLEX_PAIR_CREATION, the gate
   `scripts/verify_stage5_pair_creation.*`, four review lenses, fixer), then the gate from a
   fresh clone.
   Stage-5 correction required (found by the matter-antimatter review, finding F1, confirmed by
   MA_M4_imageFieldFockModel): `pairing-theory.json` T1krein.imageField says the image universe carries
   'energy -|eps| and charge -1 per quantum' and T1krein.consequence 'T^pair = 0 at the operator level';
   under the image field's own anticommutator (-B) those operators are minus its x4-translation
   generator and minus its charge, so the physical reading must be corrected in
   wolfram/Dirac16ComplexPairing.wl and scripts/check_dirac16complex_pairing.py (see
   provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md section 7.3) before the Stage-5 documents are written.
D. Stage 4: cross-check final state 63 checks, 1 failed (canonical_eigenvalues, section 2
   Stage-4 row).  UPDATE 2026-10-08 (stage4-fix): analysed and fixed in the code, erratum
   E4.14 of handoff/specs/STAGE4_SPEC.md: (a) the eigenvalue tolerance gets the measured Rust
   grid change |eps(601) - eps(301)| level by level (as E4.12 for the scalars; Rust converges
   to the reference: 2.195e-6, 1.83e-7, 2.6e-8 at 301/601/1201 points); (b) for Fermi-Dirac
   (smeared) occupations the reference Delta-SCF builds the occupations of every grid level
   from that level's own ground state (+4.4e-7 bias of the smeared run removed; integer runs
   keep the old code path, bit-identical); 7 new tests in
   tests/test_d16c_kohn_sham_reference.py.  In a scratch copy (stage4-fix) the full checker
   gives 63 checks, 0 failed (eigenvalues 0.716, Delta-SCF 0.79) and the notebook gauntlet 60
   of 60.  NOT yet in the repository (two blockers for the lead/user): the reference rerun of
   m1_L3_N1016_lamm2_T0 under rule (b) (about 4.5 h; `--resume` now recomputes exactly that
   run), and tests/test_d16c_textbook_publication.py pins the preserved first-edition
   textbook's sentence "63 checks of which 1 failed" to the committed report, so refreshing
   python-check-report.json breaks it unless the user allows an erratum to the frozen book
   or a test change.  Committed python-check-report.json and notebook outputs are therefore
   still those of 2026-09-30.  Before that update the plan was: analyse it (Rust 301 vs 601 grid error of the deep state), then rerun the
   documents phase of `wf_stage4_notebooks_documents.js` (it was at doc-main/doc-student when
   the previous session ended), then `wf_stage4_review.js`, then the gate
   `scripts/verify_stage4_kohn_sham.{ps1,sh}` from a fresh clone (both twins; hours).
E. Final: README.md, HANDOFF.md and the memory notes; `python -m unittest discover -s tests
   -p "test_*.py"`; every stage's gate from fresh public clones; push.

## 1. What this repository is

`dirac16complex`: a 16-component complex Grassmann spinor field of Pin(4,4) in 4+4
dimensions.  Stages: (1) arbitrary gravitational field; (2) the notebook's primordial
pair-creation field; (3) dark-sector numerics (five CVODE experiments); (4) Kohn–Sham
DFT ground and first excited states in the primordial field.  README.md gives the
map; provenance/*.md are the documents; artifacts/dirac16complex/* the reports.

## 2. State at the last push and what remains

| Stage | Done (verified) | Remaining |
|---|---|---|
| 1 arbitrary field | COMPLETE: 153/153 exact checks in five reports, cross-implementation agreement, document `provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{md,tex,pdf}` (45 pp), 4-lens review + fixes, gate `scripts/verify_stage1_arbitrary_field.{ps1,sh}` = OK | nothing. (2026-09-30) public-clone mode added and VERIFIED: fresh public clone, sh and ps1 twins OK (153 checks true, 4 files identical, 3 with only the dirac-main differences), and sh with dirac-main OK (logs handoff/reviews/stage1_gate_2026-09-30_*.log) |
| 2 primordial field | COMPLETE: 126/126 + 16/16 checks, document `provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.{md,tex,pdf}` (38 pp), 3-lens review + 21 fixes, gate `scripts/verify_stage2_primordial_field.{ps1,sh}` = OK | nothing |
| 3 dark-sector numerics | COMPLETE: Rust crate `studies/dirac16complex_cosmology` (5 experiments), both notebooks, figures, documents `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS` and `provenance/DIRAC16COMPLEX_STUDENT_GUIDE`, two review rounds with all fixes (`handoff/reviews/stage3_review_round2_findings.json`); gate `scripts/verify_stage3_dark_sector.{ps1,sh}` = OK from a fresh clone of 1fb83c3 (`handoff/reviews/stage3_gate_2026-09-30_fresh_clone_OK.log`, 28 min) | nothing |
| 4 Kohn–Sham DFT | exact theory `wolfram/Dirac16ComplexKohnSham.wl` + verifier (125/125); `scripts/check_dirac16complex_kohn_sham_theory.py` (sympy, 157/157) with `artifacts/dirac16complex/kohn-sham/{kohn-sham-theory.json,exchange-table.json,python-theory-report.json}`; Rust crate `studies/dirac16complex_kohn_sham` COMPLETE (fmt/clippy clean, 35 tests; canonical tree `artifacts/dirac16complex/kohn-sham/rust/` with own checks spectrum 33, scf 137, excited 65 (with the g601 refinement), thermo 102, emt 60, all SUCCESS; a repeat run is byte-identical over 327 files; a refined run agrees to 6.0e-8 relative; `rust/determinism-report.json`); `scripts/ks_reference_solver.py` (55 reference runs in `artifacts/dirac16complex/kohn-sham/reference/`) and `scripts/check_dirac16complex_kohn_sham.py` written | (2026-09-30, later) The 4 cross-check failures were diagnosed and fixed in code (commit b22a558): (a) particle-hole pairs of T = 0 runs use an occupation floor of 1e-12 in both solvers (holes f > 1e-12, particles f < 1 - 1e-12; commit after b22a558, which had first tried an aufbau rule and misdescribed the case). The smeared N = 1016, -lambda_hat_2 run: the aufbau count closes at the 192-fold k = 0.935 band, the smeared ensemble moves about 4.2 particles into the 8-fold k = 0 level 3.7e-3 m above it; its KS gap and Delta-SCF refer to that ensemble; (b) the checker gives excited records the scf parameters (smeared f were compared as exact T = 0); (c) the reference's stale lamh_T0p3 run (own coupling) and its a4 rescaling partner (wrong lambda; now `lamp1rescaled`, lambda_hat_1 e^1.5 as in Rust) are recomputed, and the missing `m1_L3_N112_lamh_T1` is computed, by `python scripts/ks_reference_solver.py --resume --skip-self-tests --workers 8`; the Rust excited tree is regenerated with the fixed binary (canonical, repeat, refined). Open: the Delta-SCF of the smeared run differs by 3.3e-6 (tolerance 1e-6); the reference's own extrapolation spread there is about 2.5e-6, so a finer-grid reference run (N0 = 120) decides it. Delta-SCF investigation (N = 1016, -lambda_hat_2, 07:05): Rust 301 points 0.0436184212, 601 points 0.0436193591 (continuum ~0.0436197); reference (60/120/240 grids, (h^2,h^3) elimination) 0.0436216925, admissible three-grid extrapolations 0.0436207-0.0436232; experiment: reference on 120/240/480 grids with explicit smearing 1e-3 (scratch stage4_tmp/refsmear120); if it converges to the same ensemble and approaches Rust, adopt that grid for this run as a documented override (like N0 = 120 for m = 3). State at 06:50 on 2026-09-30: code fixes committed (414d11e, 936c75d, 80a8095: occupation-floor particle-hole rule, excited records with parameters, a 601-point refinement of the hardest Delta-SCF, the measured Rust grid uncertainty in the checker tolerances); reruns in progress: Rust `excited` (canonical, then repeat and refined in the scratch trees), reference `--resume` (lamh_T0p3, lamh_T1, lamp1rescaled) and the reference `--config` rerun of m1_L3_N1016_lamm2_T0; after them run `python scripts/ks_reference_solver.py --resume --skip-self-tests` once more (rewrites reference-summary.json) and the full checker `python scripts/check_dirac16complex_kohn_sham.py --repeat <repeat tree> --refined <refined tree>`. State at 08:40 on 2026-09-30: the Rust `excited` reruns are done with binary sha 3bbc395a (canonical in `rust/`, repeat and refined in the session scratch `stage4_tmp/rust/{repeat,refined}`); `rust/determinism-report.json` regenerated: 330 repeat files byte-identical, refined 65 runs / 364829 levels with max relative energy 5.96e-8 (4/4 checks); the reference `--resume` pass finished (56 runs, none failed; lamh_T1 E0 = 46815.4294); the quick checker gave 63 checks, 4 failed: canonical_deltaSCF, canonical_eigenvalues (g601) and canonical_particleHole, all on the smeared N = 1016 run (waiting for the N0 = 60 floor-rule rerun `stage4_tmp/ref1016`, which writes into `reference/`, and the N0 = 120 experiment `stage4_tmp/refsmear120`, whose ground energies 120/240/480 extrapolate to 1126.8581 against Rust 1126.85809); reproduce_m1_L2_N8_lamp1_T0 failed only on the coarse --quick grids. The full checker (canonical grids, with the repeat and refined trees, 08:42) gives 63 checks, 3 failed, all three on the smeared N = 1016 run (canonical_deltaSCF ratio 1.69, canonical_eigenvalues g601 ratio 1.46, canonical_particleHole pending the floor-rule reference). 08:52: the floor-rule rerun of m1_L3_N1016_lamm2_T0 finished (E0 1126.858099431928, gap 0.0412551026; ground 60/120/240 extrapolation agrees with Rust 1126.858089 to 1e-8 relative), the `--resume` summary pass kept all 56 runs, and the full checker gives 63 checks, 2 failed: canonical_deltaSCF (reference 60/120/240: 0.0436218 against Rust 601 0.0436194 and the Rust 301/601 estimate 0.0436197; the reference's own levels 0.0430172, 0.0434646, 0.0435817 have the ratio 3.8, not yet asymptotic) and canonical_eigenvalues at g601 (1.54e-6 against 1.05e-6; the 601-point Rust eigenvalue moves away from the reference). Both wait for `stage4_tmp/refsmear120` (the same run on 120/240/480 grids with the smearing 1e-3 given directly); if it moves to Rust, the run gets the documented override N0 = 120 and smearing 1e-3 in `ks_reference_solver.py`, its output is copied into `reference/`, and the summary pass and the checker are repeated. 09:03: refsmear120 ground state converged at 480: the 120/240/480 (h^2, h^3) extrapolation gives E0 = 1126.858089105 against Rust 601 1126.858089030 (8e-8 absolute), while the 60/120/240 one gave 1126.858099432 (1e-5 off): the N0 = 60 grids bias this run's extrapolation; the excited state on 120/240/480 follows. 11:33: RESOLVED (STAGE4_SPEC E4.13): refsmear120 finished, Delta-SCF 0.0436199531 (E1 levels 1126.97662, 1126.92066, 1126.90648, order 1.98) against Rust 601 0.0436193591 and the Rust 301/601 extrapolation 0.0436196717; the canonical run list now gives this run N0 = 120 and smearing 1e-3 m (`canonical_runs` in ks_reference_solver.py), its output replaced `reference/m1_L3_N1016_lamm2_T0/` (the N0 = 60 run is kept in the session scratch stage4_tmp/ref1016_N0_60_backup), and the `--resume` summary pass kept all 56 runs; the full checker then writes `artifacts/dirac16complex/kohn-sham/python-check-report.json`. The full checker (11:58) gives 63 checks, 1 failed: canonical_eigenvalues (the 301-point smeared run's deep state eps -1.0537 differs from the N0 = 120 reference by 2.2e-6 against 1.05e-6; with N0 = 60 it was the 601-point run that failed) - OPEN, to be analysed (the Rust grid error of that state, 301 versus 601 points) before the gate (analysed and fixed in the code on 2026-10-08, STAGE4_SPEC E4.14; outputs not yet refreshed, see item D of section 0). Also OPEN (found by the textbook review): the Rust `theory-agreement.json` note labelRelation reports 0 blocks for both j = -J and j = +J, i.e. its theory-label lookup matches nothing (studies/dirac16complex_kohn_sham/src/theory.rs); the relation s = -j itself is established by the Python theory checker. The notebooks, summary builder, gate scripts and both documents are written by `handoff/workflows/wf_stage4_notebooks_documents.js`; then `handoff/workflows/wf_stage4_review.js` (four review lenses + fixer); then the gate `scripts/verify_stage4_kohn_sham.{ps1,sh}` from a fresh clone |
| 5 dirac16complex00 and {+M,-M} pairing | spec `handoff/specs/STAGE5_SPEC.md` (2026-09-30) | exact theory (wolfram/Dirac16Complex00.wl, wolfram/Dirac16ComplexPairing.wl + verifiers), independent sympy checkers, Rust `pairs` subcommand + reference options + checker (`handoff/workflows/wf_stage5_theory_numerics.js`), then the documents `provenance/DIRAC16COMPLEX00_FIELD_THEORY.*` and `provenance/DIRAC16COMPLEX_PAIR_CREATION.*`, review, gate `scripts/verify_stage5_pair_creation.*`. Stage 4 was PAUSED at the user's request on 2026-09-30 (processes suspended; PIDs in the session scratch `suspended_pids.txt`; after a restart they are gone: rerun the Stage-4 reruns as listed in the Stage-4 row) |
| textbook | spec `handoff/specs/TEXTBOOK_SPEC.md` (2026-09-30) | wave A (chapters 00-05, 08-13 and the assembler `scripts/build_textbook.py` with `tests/test_d16c_textbook_assembler.py`, `handoff/workflows/wf_textbook_wave_a.js`) COMPLETE 2026-09-30 09:00 (7 agents, every chapter warning-free alone; the lead's review notes for the wave-B fixer are in the session scratch `textbook_lead_review.md`: ch00 Answer 0.5 photon pair creation needs a nucleus, ch00 L2 'the task's expression', ch05 'the task's scalar-field reference', ch13 numbers to refresh from the final Stage-4 reports); the PDF option `--number-sections-from-zero` (builder and build_provenance_pdf.py, opt-in, test in `tests/test_publication_tooling.py`) makes LaTeX print chapter N as N; wave B (chapters 06, 07, 14-18, final ledger, appendices 19-20) after Stage 5; then `provenance/DIRAC16COMPLEX_TEXTBOOK.{md,tex,pdf}`, review, register, test, push. Stage 4 was RESUMED on 2026-09-30 ("continue with all stages") 2026-09-30 12:15 (user: the textbook is the ONLY priority now; Stage 5 numerics and the Stage-4 documents were stopped, their orphan processes killed; resume them afterwards): running in parallel (disjoint files) `handoff/workflows/wf_textbook_wave_a_review.js` resumed from run wf_438d8253-305 (chapters 00-05, 08-13: 14 reviewers, skeptics, fixers) and `handoff/workflows/wf_textbook_wave_b_chapters.js` (chapters 06, 07, 14-20: writer, adversarial reviewer, fixer per chapter; run wf_feb9b915-2ef); then `handoff/workflows/wf_textbook_final.js` (chapter-0 ledger update, assembly, PDF with --developer-layout --number-sections-from-zero, four whole-book review lenses, fixer, registration, publication test). |
| matter-antimatter | spec `handoff/specs/MATTER_ANTIMATTER_SPEC.md` (2026-09-30; the requested "proof that the theory solves the matter-antimatter problem" is not provable: exact U(1) charge conservation) | exact theorems M1-M6 (Wolfram + sympy), document `provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.{md,tex,pdf}`, review, fix: `handoff/workflows/wf_matter_antimatter.js` running |
| final | — | README status table; `python -m unittest discover -s tests -v` all green; fresh-clone verification (clone into a scratch dir, `setup_solver`, run every gate); push |

How to tell what exists: `git log --stat -5`, `ls provenance scripts artifacts/dirac16complex/*`,
`python -m unittest discover -s tests -v`.  Every verifier prints
`check_count`/`failed_check_count`; every gate ends with `stageN_..._verification=OK`.

## 3. Workflow scripts (handoff/workflows/)

| Script | Covers | Launch when |
|---|---|---|
| `wf_stage3_docs.js` | Stage 3 integrate → notebooks → documents → review → fix → gate | the Stage-3 gate is not yet OK (finished phases are redone quickly because the files exist) |
| `wf_stage4.js` | all of Stage 4 (build → integrate → notebooks → documents → review → fix → gate) | always, until `stage4_kohn_sham_verification=OK` |
| `wf_stage1_doc.js`, `wf_stage2_doc.js` | Stage 1 / Stage 2 document, review, gate | only if their gates stop passing |
| `stage1-build-*.js`, `stage2-build-*.js`, `stage3-rust-engine-*.js`, `understand-*.js` | the original build phases (already complete) | never, unless rebuilding from scratch |

Each script defines `const SP = ...` (scratch path) and `ROOT`; update `SP`.
`handoff/tools/wait_for.py` is the blocking wait helper (section 0.3).

## 4. Binding conventions (never change silently)

- Counting from 0; `eta = diag(+,+,+,+,-,-,-,-)`; `x4` is time; gammas are the
  notebook's `T16^A` in the split-octonion block basis (exact fixture
  `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`); `C = sigma16`;
  `Psibar = Psi^dagger C`; `B = -i C gamma^4`; `Omega_mu = (1/8) omega_{mu ab}[gamma^a,gamma^b]`
  with `omega_{mu ab} = eta_ac omega_mu^c_b` (the notebook's `omega_mu^a_b S^{ab}` is wrong).
- Lagrangian, field equations, energy–momentum tensor, KE/PE splits, quantization:
  `handoff/specs/CONTRACT.md` sections 5–8 with the errata in section 11.
- Stage-2 corrections: `det g = +cos^2 z`; the condensate CAN source the field for
  `a4'' = 0` (`handoff/specs/STAGE4_SPEC.md` section 7); Stage-4 theory errata in
  its section 8 (p_req = +15H^2/kappa; 4-fold degeneracy per j-type; current matrix
  gamma^0 gamma^4; exchange is exactly local: e_x = -(lambda/32)(n^2 + S^2)).
- Engines: the committed numerical outputs come from the Win11 rustSolveIt engine
  (commit a8fdff45); macOS/Linux engines differ in their math library
  (`handoff/specs/NUMERICS_CONTRACT.md` erratum).
- Tooling: WolframScript 1.14 drops arguments after `--` (pass paths positionally);
  Windows PowerShell 5.1 cannot run the gates (they re-exec under PowerShell 7);
  PDFs only via `scripts/build_provenance_pdf.py <md> [--register]`; outputs
  deterministic (LF, `fmt_e(v,17)`); numbers in documents only from reports; large
  files written in chunks of ≤ 300 lines per tool call (64k output-token limit).

## 5. Private inputs (never commit)

`prompt_Dirac_claude*.txt`, the Gmail PDF, `dirac-main/`, `dirac-main_2.zip`,
`vendor/` are git-ignored on purpose.  The task statements are in the ignored
prompt files; their substance is in section 2 above and in the specs.
