#!/usr/bin/env python3
"""um4_krein.py - is the indefinite Krein norm of the dirac16complex charge stable?  (UM-4: the states chi at the fold are
long-lived resonances; their charge form is that of UM-3.)

The charge of dirac16complex is Q_Psi = int d^7x d sigma sqrt|g| Psi^dagger B gamma-weight Psi, which for the fields of UM-4
(Psi = e^{(7/2)H|sigma|} chi, the frame component e^{H|sigma|} of gamma^(x4)) is Q = int d sigma e^{H|sigma|} chi^dagger B chi per
unit volume of the fold, with the Krein operator B = i sigma16 gamma^(4), a Hermitian involution with eight eigenvalues +1 and
eight -1 (the author's real matrices T_a of 4+4.nb, gamma^(a) = eta_aa T_a).  The canonical anticommutator of the field is
{Psi, Psi^dagger} = -B (the overall sign chosen so that the occupied states of Krein charge -1, the particles chi, have positive
norm); a mode u_n with Krein charge kappa_n = -1 or +1 then has {a_n, a_n^dagger} = -kappa_n, the Hamiltonian is
H = sum_n (-kappa_n omega_n) a_n^dagger a_n, and every quantum raises H by its frequency, [H, a_n^dagger] = omega_n a_n^dagger.
In the positive-energy quantisation (a_n|0> = 0 for omega_n > 0, a_n^dagger|0> = 0 for omega_n < 0) every particle and every
hole carries positive energy and the norm -kappa_n of its mode: the particles and the holes of the modes of Krein charge +1 are
ghosts (norm -1), those of the modes of Krein charge -1 are physical (norm +1).  The physical states are therefore the
particles chi (charge -1 at +omega_0) and the holes in the states of charge -1 at -omega_0 (the conjugates of the states of
charge +1 at +omega_0); the holes in the conjugates of the chi states (charge +1 at -omega_0) are ghost antiparticles.  A
fermion cannot trade its norm for its energy ({a, a^dagger} = -1 has no positive-definite representation), so the ghosts
cannot be removed by a choice of the vacuum.

Checks (the states at rest on the static block, units m_Psi = 1, mu_L = -0.6, mu_R = 0, H = 1e-4, the box |sigma| <= 40, as in
um4_kohnsham.py; omega_0 = 0.95378 the free level, which the warped time lowers from the omega_b = 0.95394 of UM-3):
  KR1  the charge form: B Hermitian, B^2 = 1, signature (8, 8); the anticommutator {a_n, a_m^dagger} = -kappa_n delta_nm
       of the modes derived from {Psi, Psi^dagger} = -B; the norm of a one-quantum state follows from it, <0|a a^K|0> =
       -kappa (for a particle and for a hole), and the two-dimensional Krein space with the metric diag(1, -kappa) represents
       it (a consistency check of the representation), with [H, a^dagger] = omega a^dagger; complex conjugation maps the level
       at +omega_0 onto the one at -omega_0 and reverses every Krein charge (the author's matrices are real; the measure
       e^{H|sigma|} d sigma is real);
  KR2  the symmetries of the problem at rest: the matrices that commute with gamma^(0), gamma^(4) and Gamma_8 and keep
       sigma16 (U^dagger sigma16 U = sigma16) form a Lie algebra of real dimension 32: 16 compact generators that keep the
       two Krein sectors and 16 Hermitian generators (boosts) that anticommute with B and mix them, among them the nine
       Lorentz boosts Sigma^{ir} between ordinary space and the extra times; with gamma^(1), gamma^(2), gamma^(3) added
       (moving particles) only u(1) + su(2) of the extra times remains, compact and sector-keeping (the warped energy changes
       none of this: it multiplies gamma^(4), which is already in the list);
  KR3  the mirror of the fold: under R_1 chi(sigma) -> T_0 T_1 T_2 T_3 chi(-sigma) the four states of Krein charge -1
       are even and the four of charge +1 odd; R_2 chi(sigma) -> T_0 T_5 T_6 T_7 chi(-sigma) maps each sector onto the other;
       the self-consistent occupied orbital and its mean field are R_1-even;
  KR4  flat directions: the boosts of KR2 map the self-consistent gas (G_KS = 0.1) onto self-consistent gases (the
       residuals of the sixteen-dimensional Kohn-Sham equation and of the fold matching unchanged, Krein charges -1,
       Krein-orthogonal) whose orbitals contain Krein-positive admixtures: exact flat directions; the linear response of
       the level (the time-dependent Kohn-Sham equations restricted to the occupied and the empty multiplet, frequencies in
       pairs nu, -nu*) has 32 frequencies far below the splitting of the two multiplets (below a tenth of it), two of them
       imaginary; the truncation keeps exactly the tangent space of the occupations of KR8, on which the first-order energy
       has a saddle, and whether the imaginary pair is an instability of the full response is OPEN;
  KR5  the Krein-positive partner of the occupied level in the self-consistent mean fields at G_KS = 0.01, 0.1, 0.2 and 0.3:
       a real level above the occupied one in the dilute gas, moving away from it as G_KS grows (they cannot mix: opposite
       R_1 parity); where it reaches the frequency at which the end of the box becomes classically allowed (omega e^{HL} = 1)
       it is no longer a state of the fold (it dissolves into the bulk, or turns into a complex pair at the end of the box,
       which depends on the size of the box);
  KR6  selection rules at the fold: of the 256 products Gamma_I of the author's matrices, the chirality-blind fold
       operators (products of gamma^(1)..gamma^(4)) never connect a physical state with a ghost at rest, the chiral ones
       (the same products times Gamma_8) always do; the amplitudes are the largest singular values of the 4 x 4 matrices
       between the degenerate multiplets (independent of the choice of the basis inside them); for moving particles (whose
       levels are omega(k) = sqrt(omega_0^2 + k^2) exactly, the boost invariance of UM-4) the scalar, density and
       vector-current operators still do not, the magnetic dipole does in proportion to the momentum;
  KR7  the consequence: in the positive-energy quantisation the vacuum cannot decay (every quantum of the free field raises
       the energy by its frequency; with the indefinite metric it is not a state of lowest energy among the states of
       positive norm), but the left-handed Higgs portal of the author's specification (c_R = 0) creates a physical particle
       with a ghost antiparticle at rest with exactly its elastic amplitude (all four singular values equal): the ghosts are
       produced wherever the chiral portals act, and UM-4 with chiral fold couplings is not unitary (as UM-3);
       chirality-blind couplings are necessary, not shown to be sufficient; the classical stability of the gas is not decided
       (KR4, KR5, KR8);
  KR8  the occupation of the level is a saddle: every four-dimensional subspace of negative Krein norm of the eight states of
       the free level, n_k + sum_j Z_kj p_j (Z a strict contraction, 32 real parameters), is an occupation of four particles
       chi; the first-order interaction integral I = sum over both sides of int e^{7H|sigma|} (rho_hat^2 - tr N_hat^2) (S-9)
       is stationary at the symmetric multiplet (Z = 0, I = 0.10216), and its Hessian has 15 negative, 16 zero (the 16
       sector-mixing symmetry generators of KR2) and one positive eigenvalue; towards the null cone (|Z| -> 1) I falls without
       bound along some directions and rises along others: the first-order energy of the repulsive gas has no lower bound on
       the occupations of negative norm, and the Kohn-Sham states are the symmetric stationary occupation, not a ground state;
  KR9  the pairs that the convective current of IN-16 creates: between the vacuum and a pair chi(k) chibar(-k) at the fold
       the time component of j_X vanishes and the spatial one is -2k <P_X>_pair(k); the four singular values of <P_X>_pair
       vanish at rest (KR6) and grow linearly in k (computed with the moving states at k = 0.01, 0.02, 0.05), so the
       amplitude is of the second order in k and (sigma v)_{chi chibar} = g_f^2 omega_b^2 v^4 rho_X/(96 pi) per massless
       chiral fermion state (v the relative velocity, g_f the elastic coupling of FE-47), with rho_X = 0.828 (P_L), 1.231 (P_R)
       and 1.000 for the chirality-blind current (P_L + P_R = 1): the value of a Dirac fermion whose current is the convective
       current of a scalar density.  The chiral currents also create a physical particle with a ghost antiparticle, at rest,
       with the elastic amplitude (KR7); the chirality-blind current does so only at the next order in the momentum: the
       singular values of <1> between chi(k) and the ghost antiparticle grow like k^2 (0.028 k^2, against 0.30 k for the
       physical pair), so its ghost pairs have the relative amplitude 0.094 k and the relative rate 0.0089 k^2 (k in units of
       m_Psi): small, but not zero.
The mean fields of KR3 to KR5 are the snapshots that um4_kohnsham.py keeps in outputs/kohnsham_parts (run its parts first).
Writes outputs/krein.json and reports/krein_checks.json.  Runs in a few minutes (under the 423 s limit).
Usage: python universe_model_4/code/um4_krein.py

BEGIN FOLD DEFINITION
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
END FOLD DEFINITION
"""
from __future__ import annotations

import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import scipy.linalg as sla
from scipy.optimize import minimize, minimize_scalar

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
sys.path.insert(0, str(HERE))
import um4_kohnsham as K  # noqa: E402

T = K.TUP
I16 = np.eye(16)
SIG = K.SIG
BKR = K.BKR
G8 = K.TN[8]
S1 = T[0] @ T[1] @ T[2] @ T[3]
S2 = T[0] @ T[5] @ T[6] @ T[7]
PARTS = UM4 / 'outputs' / 'kohnsham_parts'
HM, LM = K.H_MAIN, K.L_MAIN
_W0F = math.sqrt(1 - 0.09) * (1 - HM / 0.6)
WB = K.free_level(K.Shooter(HM, -0.6, 0.0, LM, 0.02, 4), _W0F, 2)       # the free level omega_0 (box h = 0.02)


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def commutant(ops):
    M = np.vstack([np.kron(O, I16) - np.kron(I16, O.T) for O in ops])
    u, s, vh = np.linalg.svd(M)
    null = vh[np.sum(s > 1e-9):].conj()
    return [null[k].reshape(16, 16) for k in range(null.shape[0])]


def real_null(rows_of, basis, tol=1e-9):
    """The real combinations of basis that satisfy the real-linear condition rows_of(X) = 0."""
    A = np.array([np.concatenate([rows_of(X).real.ravel(), rows_of(X).imag.ravel()]) for X in basis]).T
    u, s, vh = np.linalg.svd(A)
    null = vh[np.sum(s > tol):]
    return [sum(c * X for c, X in zip(v, basis)) for v in null]


def symmetry_algebra(extra=()):
    C = commutant([T[0], T[4], G8] + list(extra))
    basis = [ph * X for X in C for ph in (1.0, 1j)]
    return real_null(lambda X: X.conj().T @ SIG + SIG @ X, basis)


def fold_value(a, b, Op):
    """a^dagger sigma16 Op b at the fold: the mean of the two sides."""
    return 0.5 * (a[0][0].conj() @ SIG @ Op @ b[0][0] + a[1][0].conj() @ SIG @ Op @ b[1][0])


def krein_charge(o, sh):
    """The Krein charge with the measure e^{H|sigma|} d sigma of UM-4."""
    return float(sum(K.trap(np.einsum('ji,ik,jk->j', o[i].conj(), BKR, o[i]) * sh.ew, sh.h) for i in (0, 1)).real)


def conj(o):
    return (o[0].conj(), o[1].conj())


def reflect(o, S):
    """(R chi)(sigma) = S chi(-sigma): the sigma < 0 profile of R chi is S times the sigma > 0 profile of chi."""
    return ((S @ o[1].T).T, (S @ o[0].T).T)


def flat(o):
    return np.concatenate([o[0].ravel(), o[1].ravel()])


def load_snapshot(name, G):
    f = PARTS / ('snapshot_%s_G%g.npz' % (name, G))
    if not f.exists():
        return None
    z = np.load(f)
    sh = K.Shooter(float(z['H']), -0.6, 0.0, float(z['L']), float(z['h']), 4)
    sh.set_field(z['Ml'].copy(), z['Mr'].copy(), float(z['muL']))
    return sh, float(z['omega'])


def empty_level(sh, w, G):
    """The Krein-positive level of the reduced problem above the occupied one: the minimum of the smallest singular value
    in (w + 0.01 G, w + 0.15 G), where the splitting lies (it is about 0.05 G)."""
    f = lambda x: sh.sv(x)[0]
    lo, hi = w + 0.01 * G, w + 0.15 * G
    ws = np.linspace(lo, hi, 29)
    vals = []
    for x in ws:
        try:
            vals.append(f(x))
        except RuntimeError:
            vals.append(np.inf)
    i = int(np.argmin(vals))
    a, b = ws[max(i - 1, 0)], ws[min(i + 1, len(ws) - 1)]
    r = minimize_scalar(f, bounds=(a, b), method='bounded', options={'xatol': 1e-15, 'maxiter': 500})
    return float(r.x), float(r.fun)


def rpa_bound_level(sh, w, G):
    """The linearised time-dependent Kohn-Sham equations of the four occupied orbitals chi_o, restricted to admixtures of
    the four empty Krein-positive orbitals phi_p of the bound level: i dc/dt = A c + B c*, frequencies of
    [[A, B], [-B*, -A*]] (A Hermitian, B symmetric; chibar = chi^dagger sigma16; w = e^{7H|sigma|})."""
    negW, posW, ev, s = sh.krein_split(w, 1)
    xi = negW[0]
    wp, smin = empty_level(sh, w, G)
    orbs, s2 = sh.null_orbitals(wp, 1)
    kp = sh.gram(orbs, sh.kr)[0, 0].real
    phi = (orbs[0][0] / math.sqrt(abs(kp)), orbs[0][1] / math.sqrt(abs(kp)))
    occ, emp = K.lift(xi), K.lift(phi)
    wgt = np.exp(7 * sh.H * sh.s)
    bil = lambda a, b, side: np.einsum('ji,ik,jk->j', a[side].conj(), SIG, b[side])
    n = 4
    A = np.zeros((n * n, n * n), complex)
    Bm = np.zeros((n * n, n * n), complex)
    D = wp - w
    for q, o, p, o2 in itertools.product(range(n), repeat=4):
        tA = tB = 0.0
        for side in (0, 1):
            tA = tA + K.trap(wgt * (bil(occ[o2], emp[p], side) * bil(emp[q], occ[o], side)
                                    - bil(emp[q], emp[p], side) * bil(occ[o2], occ[o], side)), sh.h)
            tB = tB + K.trap(wgt * (bil(emp[p], occ[o2], side) * bil(emp[q], occ[o], side)
                                    - bil(emp[q], occ[o2], side) * bil(emp[p], occ[o], side)), sh.h)
        A[q * n + o, p * n + o2] = (D if (q == p and o == o2) else 0.0) - G / 4 * tA
        Bm[q * n + o, p * n + o2] = -G / 4 * tB
    nu = np.linalg.eigvals(np.block([[A, Bm], [-Bm.conj(), -A.conj()]]))
    # the structure of the response: with every frequency nu also -nu* (the matrix [[A, B], [-B*, -A*]] with A Hermitian and
    # B symmetric), so the imaginary ones come in pairs
    closed = max(min(abs(-x.conjugate() - y) for y in nu) for x in nu) / max(np.abs(nu).max(), 1e-300)
    charges = [krein_charge(o, sh) for o in emp]
    n_imag = int(np.sum(np.abs(nu.imag) > 1e-3 * np.abs(nu).max()))
    real_part = [float(x) for x in sorted(np.abs(nu[np.abs(nu.imag) <= 1e-3 * np.abs(nu).max()].real))]
    return {'omega_occupied': w, 'omega_empty': wp, 'splitting': D, 'smin_empty': smin, 'empty_krein_charges': charges,
            'A_hermitian': float(np.abs(A - A.conj().T).max()), 'B_symmetric': float(np.abs(Bm - Bm.T).max()),
            'max_abs_frequency': float(np.abs(nu).max()), 'max_abs_imaginary': float(np.abs(nu.imag).max()),
            'n_imaginary': n_imag, 'largest_real_frequency': max(real_part) if real_part else 0.0,
            'max_A_minus_splitting': float(np.abs(A - D * np.eye(n * n)).max()), 'max_B': float(np.abs(Bm).max()),
            'spectrum_closed_under_minus_conjugation': float(closed)}


def moving_states(k, H=HM, L=LM, h=0.02):
    """The free states moving along x_1 with the momentum k (the term -i k e^{H|sigma|} gamma^(1) of the Dirac operator at
    a_4 = 0): the level, its Krein-negative and Krein-positive states; boost invariance predicts omega(k)^2 = omega_0^2 + k^2."""
    sh = K.Shooter(H, -0.6, 0.0, L, h, 16)
    Mk = (-1j * k * np.exp(H * sh.s))[:, None, None] * T[1][None]
    sh.set_field(Mk.copy(), Mk.copy())
    w0 = math.sqrt(WB ** 2 + k * k)
    f8 = lambda dx: float(np.sum(sh.sv(w0 + dx)[:8]))
    w = w0 + float(minimize_scalar(f8, bounds=(-5e-3, 5e-3), method='bounded', options={'xatol': 1e-15, 'maxiter': 500}).x)
    nk = int(np.sum(sh.sv(w) < 1e-6))
    neg, pos, ev, s = sh.krein_split(w, nk)
    return w, neg, pos, nk, w0


SNAPSHOT_G = K.SNAPSHOT_G


def partner_level(sh, w):
    """The Krein-positive partner of the occupied level w of the reduced problem.  First the local continuum of the far
    bulk: the smallest frequency above w at which the equation at the end of the box has a non-decaying solution.  Below
    it, a real root of the matching (local minima of the smallest singular value on a grid that is fine near w, refined;
    a singular value below 1e-7 and a positive Krein charge) is a bound partner.  Without one, the complex root above w
    (Nelder-Mead from the best points of a grid in the complex plane; a singular value below 1e-10 and an imaginary part
    above 1e-6) is a normalisable mode that grows as e^{Gamma x4}, Gamma its imaginary part; with neither, the partner
    has dissolved into the continuum of the far bulk."""
    def f(x):
        try:
            return float(sh.sv(x)[0])
        except (RuntimeError, np.linalg.LinAlgError):
            return 1e3
    far = None
    for x in np.linspace(w, w + 0.8, 321):
        ev = np.linalg.eigvals(1j * x * sh.ew[-1] * sh.C04 + sh.g0 + sh.GM[1][sh.n])
        if np.abs(ev.real).min() < 1e-9:
            far = float(x)
            break
    top = far if far is not None else w + 0.8
    ws = w + np.geomspace(1e-5, max(top - w - 1e-6, 2e-5), 120)
    vals = [f(x) for x in ws]
    roots = []
    for i in range(len(ws)):
        left = vals[i - 1] if i > 0 else np.inf
        right = vals[i + 1] if i + 1 < len(ws) else np.inf
        if vals[i] <= left and vals[i] <= right and vals[i] < 1e2:
            a = ws[i - 1] if i > 0 else w + 1e-6
            b = ws[i + 1] if i + 1 < len(ws) else top - 1e-7
            r = minimize_scalar(f, bounds=(a, b), method='bounded', options={'xatol': 1e-15, 'maxiter': 600})
            if r.fun < 1e-7 and r.x < top:
                try:
                    orbs, s2 = sh.null_orbitals(float(r.x), 1)
                except (RuntimeError, np.linalg.LinAlgError):
                    continue
                kq = float(sh.gram(orbs, sh.kr)[0, 0].real)
                if kq > 0:
                    roots.append({'omega': float(r.x), 'sv': float(r.fun), 'krein': kq})
    if roots:
        r0 = min(roots, key=lambda r: r['omega'])
        return {'kind': 'real', 'omega_occupied': w, 'omega_partner': r0['omega'], 'sv': r0['sv'], 'krein': r0['krein'],
                'far_continuum_from': far, 'growth_rate': 0.0}

    def g(z):
        try:
            return float(sh.sv(z[0] + 1j * z[1])[0])
        except (RuntimeError, np.linalg.LinAlgError):
            return 1e3
    pts = [(re, im) for re in np.linspace(w + 1e-3, w + 0.6, 61) for im in (2e-4, 1e-3, 4e-3, 1.6e-2, 5e-2)]
    if far is not None:
        # just above the continuum of the far bulk, where an embedded partner turns into a slowly growing mode
        pts += [(re, im) for re in np.arange(far - 0.01, far + 0.12, 0.002) for im in (1e-5, 3e-5, 1e-4, 3e-4, 1e-3)]
    grid = sorted((g([re, im]), re, im) for re, im in pts)
    best = None
    for v0, re, im in grid[:4]:
        z0 = [re, im]
        r = minimize(g, z0, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-18, 'maxiter': 800,
                                                            'initial_simplex': [z0, [re + 1e-3, im], [re, im * 2.0]]})
        if r.fun < 1e-10 and r.x[1] > 1e-6 and r.x[0] > w + 1e-4 and (best is None or r.x[0] < best[0]):
            best = (float(r.x[0]), float(r.x[1]), float(r.fun))
    if best is None:
        return {'kind': 'dissolved', 'omega_occupied': w, 'far_continuum_from': far, 'growth_rate': 0.0}
    return {'kind': 'complex', 'omega_occupied': w, 'omega_partner': best[0], 'growth_rate': best[1], 'sv': best[2],
            'far_continuum_from': far}


def _partner_job(args):
    name, G = args
    snp = load_snapshot(name, G)
    return ('%s G=%g' % (name, G)), (partner_level(*snp) if snp is not None else None)


def main():
    t0 = time.time()
    rep = Report()
    out = {'units': 'm_Psi = 1', 'muL': -0.6, 'muR': 0.0}

    # ---------------- KR1: the charge form and the Fock representation of one mode
    evB = np.linalg.eigvalsh(BKR)
    herm, invol = np.allclose(BKR, BKR.conj().T), np.allclose(BKR @ BKR, I16)
    fock = {}
    for kappa in (-1, 1):
        # basis |0>, |1>; a |1> = |0>; the Krein metric eta = diag(1, -kappa); the Krein adjoint a^K = eta^{-1} a^dagger eta
        a = np.array([[0.0, 1.0], [0.0, 0.0]])
        eta = np.diag([1.0, -kappa])
        aK = np.linalg.inv(eta) @ a.T @ eta
        anti = a @ aK + aK @ a
        omega = 0.7
        Hm = -kappa * omega * aK @ a
        comm = Hm @ aK - aK @ Hm
        # the other vacuum: |1> annihilated by a^K, the hole a|1> = |0> ... its norm relative to the vacuum norm
        norm_particle = (eta[1, 1] / eta[0, 0])
        norm_hole = (eta[0, 0] / eta[1, 1])
        fock[kappa] = {'anticommutator': float(anti[0, 0]), 'anticommutator_is_multiple_of_1': bool(np.allclose(anti, anti[0, 0] * np.eye(2))),
                       'norm_one_quantum': float(norm_particle), 'norm_hole_relative': float(norm_hole),
                       'H_raises_by_omega': bool(np.allclose(comm, omega * aK))}
    # the derivation from the field: in a basis of modes u_n of the 16 components with u_n^dagger B u_m = kappa_n delta_nm
    # (the eigenvectors of B), Psi = sum_n a_n u_n gives a_n = kappa_n u_n^dagger B Psi, and the canonical anticommutator
    # {Psi, Psi^dagger} = -B gives {a_n, a_m^dagger} = kappa_n kappa_m u_n^dagger B (-B) B u_m = -kappa_n delta_nm
    evB2, Ub = np.linalg.eigh(BKR)
    kap_n = np.sign(evB2)
    gram_B = Ub.conj().T @ BKR @ Ub
    acomm = np.diag(kap_n) @ Ub.conj().T @ BKR @ (-BKR) @ BKR @ Ub @ np.diag(kap_n)
    derived_ok = bool(np.allclose(gram_B, np.diag(kap_n)) and np.allclose(acomm, -np.diag(kap_n)))
    sh16 = K.Shooter(HM, -0.6, 0.0, LM, 0.02, 16)
    neg, pos, ev, s = sh16.krein_split(WB, 8)
    conj_charges = sorted(round(krein_charge(conj(o), sh16), 9) for o in neg + pos)
    out['KR1'] = {'B_eigenvalues': [float(x) for x in evB], 'fock': {str(k): v for k, v in fock.items()},
                  'anticommutator_derived_from_the_field': derived_ok, 'krein_charges_of_conjugates': conj_charges}
    rep.check('KR1_charge_form', herm and invol and int(np.sum(evB > 0)) == 8 and int(np.sum(evB < 0)) == 8 and derived_ok
              and all(fock[k]['anticommutator'] == -k and fock[k]['anticommutator_is_multiple_of_1'] and fock[k]['norm_one_quantum'] == -k
                      and fock[k]['norm_hole_relative'] == -k and fock[k]['H_raises_by_omega'] for k in (-1, 1))
              and len(neg) == 4 and len(pos) == 4
              and all(round(krein_charge(conj(o), sh16), 6) == 1.0 for o in neg)
              and all(round(krein_charge(conj(o), sh16), 6) == -1.0 for o in pos),
              'B = i sigma16 gamma^(4) is a Hermitian involution with eight eigenvalues +1 and eight -1; expanding the field in '
              'modes with u_n^dagger B u_m = kappa_n delta_nm, the canonical anticommutator {Psi, Psi^dagger} = -B gives '
              '{a_n, a_m^dagger} = -kappa_n delta_nm (derived for the 16 modes of B); from it the norm of a one-quantum state '
              'follows, <0|a a^K|0> = -kappa - <0|a^K a|0> = -kappa (and the same for a hole, with a and a^K exchanged), and the '
              'two-dimensional Krein space with the metric diag(1, -kappa), whose Krein adjoint reproduces {a, a^K} = -kappa, '
              'represents it (a consistency check of the representation, not an independent result), with [H, a^K] = omega a^K: '
              'the particles and the holes of the Krein-positive modes are ghosts (norm -1), those of the Krein-negative modes '
              'physical (norm +1), all at positive energy; the conjugates '
              'of the four Krein-negative (positive) states at '
              '+omega_0 are Krein-positive (negative) states at -omega_0 (omega_0 = %.10f)' % WB)

    # ---------------- KR2: the symmetries at rest and their breaking by motion
    alg = symmetry_algebra()
    keep = real_null(lambda X: X @ BKR - BKR @ X, alg)
    mix = real_null(lambda X: X @ BKR + BKR @ X, alg)
    compact_keep = sum(np.allclose(X, -X.conj().T) for X in keep)
    herm_mix = sum(np.allclose(X, X.conj().T) for X in mix)
    boosts_ir = [K.sig(i, r) for i in (1, 2, 3) for r in (5, 6, 7)]

    def in_span(X, L):
        Bm = np.array([np.concatenate([Y.real.ravel(), Y.imag.ravel()]) for Y in L]).T
        x = np.concatenate([X.real.ravel(), X.imag.ravel()])
        c = np.linalg.lstsq(Bm, x, rcond=None)[0]
        return float(np.linalg.norm(Bm @ c - x))
    ir_in = max(in_span(X, mix) for X in boosts_ir)
    alg_moving = symmetry_algebra([T[1], T[2], T[3]])
    moving_keep = all(np.allclose(X @ BKR, BKR @ X) for X in alg_moving)
    moving_compact = all(np.allclose(X, -X.conj().T) for X in alg_moving)
    out['KR2'] = {'dimension_at_rest': len(alg), 'sector_keeping': len(keep), 'compact_among_them': int(compact_keep),
                  'sector_mixing': len(mix), 'hermitian_boosts_among_them': int(herm_mix),
                  'space_extra_time_boosts_in_the_mixing_part_residual': ir_in, 'dimension_moving': len(alg_moving)}
    rep.check('KR2_symmetry_at_rest', len(alg) == 32 and len(keep) == 16 and compact_keep == 16 and len(mix) == 16
              and herm_mix == 16 and ir_in < 1e-9 and len(alg_moving) == 4 and moving_keep and moving_compact,
              'at rest the sigma16-preserving matrices that commute with gamma^(0), gamma^(4), Gamma_8 form a Lie algebra of '
              'real dimension %d: %d compact generators keep the Krein sectors, %d Hermitian generators anticommute with B and '
              'mix them (the nine space-extra-time boosts Sigma^{ir} among them, residual %.1e); with gamma^(1), gamma^(2), '
              'gamma^(3) added (moving particles) %d generators remain, compact and sector-keeping (u(1) + su(2) of the extra '
              'times)' % (len(alg), len(keep), len(mix), ir_in, len(alg_moving)))

    # ---------------- KR3: the reflections across the fold
    Sneg = np.array([flat(o) for o in neg]).T
    Spos = np.array([flat(o) for o in pos]).T
    r1_neg = max(np.linalg.norm(flat(reflect(o, S1)) - flat(o)) / np.linalg.norm(flat(o)) for o in neg)
    r1_pos = max(np.linalg.norm(flat(reflect(o, S1)) + flat(o)) / np.linalg.norm(flat(o)) for o in pos)

    def resid_in(v, Sb):
        c = np.linalg.lstsq(Sb, v, rcond=None)[0]
        return float(np.linalg.norm(Sb @ c - v) / np.linalg.norm(v))
    r2_np = max(resid_in(flat(reflect(o, S2)), Spos) for o in neg)
    r2_pn = max(resid_in(flat(reflect(o, S2)), Sneg) for o in pos)
    sigma_props = {'S1 keeps sigma16': bool(np.allclose(S1.T @ SIG @ S1, SIG)), 'S2 reverses sigma16': bool(np.allclose(S2.T @ SIG @ S2, -SIG)),
                   'S1 commutes with B': bool(np.allclose(S1 @ BKR, BKR @ S1)), 'S2 anticommutes with B': bool(np.allclose(S2 @ BKR, -BKR @ S2))}
    snap = load_snapshot('I', 0.1)
    sc = {}
    if snap is not None:
        shI, wI = snap
        negW, posW, evW, sW = shI.krein_split(wI, 1)
        QW = K.QW
        S1W = QW.conj().T @ S1 @ QW
        o = negW[0]
        v, u = flat(reflect(o, S1W)), flat(o)
        c = np.vdot(u, v) / np.vdot(u, u)
        sc = {'omega': wI, 'parity': [float(c.real), float(c.imag)], 'residual': float(np.linalg.norm(v - c * u) / np.linalg.norm(v)),
              'mean_field_even': float(max(np.abs(shI.M[-1][j] - S1W @ shI.M[1][j] @ S1W.conj().T).max() for j in range(0, shI.n + 1, 25))
                                       / np.abs(shI.M[1]).max())}
    out['KR3'] = {'R1_even_residual_negative': r1_neg, 'R1_odd_residual_positive': r1_pos, 'R2_maps_negative_to_positive': r2_np,
                  'R2_maps_positive_to_negative': r2_pn, 'matrices': sigma_props, 'self_consistent': sc}
    rep.check('KR3_mirror_of_the_fold', r1_neg < 1e-12 and r1_pos < 1e-12 and r2_np < 1e-12 and r2_pn < 1e-12 and all(sigma_props.values())
              and sc and abs(sc['parity'][0] - 1) < 1e-8 and sc['residual'] < 1e-8 and sc['mean_field_even'] < 1e-8,
              'R_1 (T_0T_1T_2T_3, keeps sigma16 and B): the four Krein-negative bound states even (residual %.1e), the four '
              'Krein-positive odd (%.1e); R_2 (T_0T_5T_6T_7, reverses sigma16 and B): each sector mapped onto the other '
              '(%.1e, %.1e); the self-consistent occupied orbital at G_KS = 0.1 is R_1-even (parity %.8f, residual '
              '%.1e) and so is its mean field (relative deviation %.1e)' % (
                  r1_neg, r1_pos, r2_np, r2_pn, sc.get('parity', [float('nan')])[0], sc.get('residual', float('nan')),
                  sc.get('mean_field_even', float('nan'))))

    # ---------------- KR4: flat directions and the linear response of the bound level
    kr4 = {}
    ok4 = False
    if snap is not None:
        shI, wI = snap
        negW, posW, evW, sW = shI.krein_split(wI, 1)
        occ = K.lift(negW[0])
        base = K.full_residuals(shI, wI, occ, 0.1)
        fam = []
        for kx in (0, 7, 13):
            X = mix[kx] / np.linalg.norm(mix[kx], 2)
            for th in (0.3, 1.0):
                U = sla.expm(th * X)
                occU = [(o_[0] @ U.T, o_[1] @ U.T) for o_ in occ]
                rr = K.full_residuals(shI, wI, occU, 0.1)
                # the positive-definite norm int |chi|^2 of the boosted orbitals relative to the original ones: it grows while
                # the Krein charges stay -1 (the Krein-positive admixture)
                grow = float(sum(np.linalg.norm(o_[i]) ** 2 for o_ in occU for i in (0, 1))
                             / sum(np.linalg.norm(o_[i]) ** 2 for o_ in occ for i in (0, 1)))
                fam.append({'generator': kx, 'theta': th, 'res_ode': rr[0], 'res_match': rr[1], 'charges': rr[2], 'offdiag': rr[3],
                            'norm_U': float(np.linalg.norm(U, 2)), 'positive_norm_growth': grow})
        rpa = rpa_bound_level(shI, wI, 0.1)
        kr4 = {'base_residuals': [base[0], base[1]], 'family': fam, 'linear_response': rpa}
        ok4 = (all(abs(f['res_ode'] - base[0]) < 0.05 * base[0] and (f['theta'] < 0.5 or f['positive_norm_growth'] > 1.5) and f['res_match'] < 1e-12 and all(abs(q + 1) < 1e-9 for q in f['charges'])
                   and f['offdiag'] < 1e-9 for f in fam)
               and all(abs(q - 1) < 1e-6 for q in rpa['empty_krein_charges']) and rpa['smin_empty'] < 1e-7
               and rpa['max_abs_frequency'] < 0.1 * rpa['splitting'] and rpa['A_hermitian'] < 1e-15 and rpa['B_symmetric'] < 1e-15
               and rpa['spectrum_closed_under_minus_conjugation'] < 1e-10)
    out['KR4'] = kr4
    rep.check('KR4_flat_directions', ok4,
              'G_KS = 0.1: three boosts e^{theta X} (theta = 0.3, 1; |U| = e^theta) map the self-consistent gas onto '
              'self-consistent gases (residual of the 16-dimensional Kohn-Sham equation %.2e as without the boost, fold matching '
              '%.0e, Krein charges -1, Krein-orthogonal) whose orbitals carry Krein-positive admixtures (their positive-definite norm grows '
              'up to %.2f times while the charges stay -1): the boosts are exact flat directions of the self-consistent gas; the '
              'linear response truncated to the bound level (16 admixtures of the four empty Krein-positive orbitals, splitting '
              '%.3e; its frequencies come in pairs nu, -nu*) has frequencies far below it (largest |nu| %.2e, %.3f of the splitting), %d of '
              'them imaginary (|Im nu| up to %.2e, the largest real one %.2e); the truncation keeps exactly the 32-dimensional tangent '
              'space of the occupations of the level, on which the first-order energy has a saddle (KR8): whether the imaginary pair '
              'is an instability of the full response (with the continuum of the bulk) is not decided here (OPEN)' % (
                  kr4.get('base_residuals', [float('nan')])[0], max([f['res_match'] for f in kr4.get('family', [])] or [float('nan')]),
                  max([f['positive_norm_growth'] for f in kr4.get('family', [])] or [float('nan')]),
                  kr4.get('linear_response', {}).get('splitting', float('nan')),
                  kr4.get('linear_response', {}).get('max_abs_frequency', float('nan')),
                  kr4.get('linear_response', {}).get('max_abs_frequency', float('nan')) / kr4.get('linear_response', {}).get('splitting', float('nan')),
                  kr4.get('linear_response', {}).get('n_imaginary', -1),
                  kr4.get('linear_response', {}).get('max_abs_imaginary', float('nan')),
                  kr4.get('linear_response', {}).get('largest_real_frequency', float('nan'))))

    # ---------------- KR5: the Krein-positive partner level in the self-consistent mean fields (two processes)
    from multiprocessing import Pool
    jobs = [('I', g) for g in SNAPSHOT_G]
    with Pool(2) as pool:
        kr5 = dict(pool.map(_partner_job, jobs))
    out['KR5'] = kr5
    keys5 = ['I G=%g' % g for g in SNAPSHOT_G]
    dilute_real = all(kr5[k] and kr5[k]['kind'] == 'real' for k in ('I G=0.01', 'I G=0.1'))
    classified = all(kr5[k] is not None and kr5[k]['kind'] in ('real', 'complex', 'dissolved') for k in keys5)
    kinds = [(g, kr5['I G=%g' % g]['kind']) for g in SNAPSHOT_G]
    first_c = next((g for g, k_ in kinds if k_ == 'complex'), None)
    last_real = max((g for g, k_ in kinds if k_ == 'real' and (first_c is None or g < first_c)), default=None)
    diss = [g for g, k_ in kinds if k_ == 'dissolved']
    onset = {'last_bound_partner': last_real, 'first_growing_mode': first_c, 'dissolved_at': diss,
             'growth_rates': {('%g' % g): kr5['I G=%g' % g]['growth_rate'] for g, k_ in kinds if k_ == 'complex'},
             'far_continuum_from': {('%g' % g): kr5['I G=%g' % g].get('far_continuum_from') for g in SNAPSHOT_G}}
    out['KR5_onset'] = onset
    gaps = [(g, kr5['I G=%g' % g]['omega_partner'] - kr5['I G=%g' % g]['omega_occupied']) for g in SNAPSHOT_G
            if 'omega_partner' in kr5['I G=%g' % g]]
    gaps_grow = len(gaps) >= 2 and all(b_[1] > a_[1] for a_, b_ in zip(gaps[:-1], gaps[1:]))
    out['KR5_gap_partner_minus_occupied'] = gaps
    parts5 = ['bound partner up to G_KS = %s' % last_real]
    if diss:
        parts5.append('no partner below the frequency at which the end of the box becomes classically allowed at G_KS = %s'
                      % ', '.join('%g' % g for g in diss))
    if first_c is not None:
        parts5.append('a complex partner from G_KS = %g (Gamma = %s m_Psi)' % (
            first_c, ', '.join('%.1e at %s' % (v, g) for g, v in onset['growth_rates'].items())))
    parts5.append('the gap partner - occupied %s' % ', '.join('%.4f (G_KS = %g)' % (d_, g) for g, d_ in gaps))
    rep.check('KR5_partner_level', classified and dilute_real and gaps_grow,
              'the Krein-positive partner of the occupied level in the self-consistent mean field (G_KS = %s): %s; the partner '
              'moves away from the occupied level as G_KS grows (it cannot mix with it: they have opposite R_1 parity in an '
              'R_1-even mean field); the end of the box becomes classically allowed at %s; dilute gas (G_KS = 0.01, 0.1) with a '
              'bound, real partner: %s' % (', '.join('%g' % g for g in SNAPSHOT_G), ', '.join(parts5),
                                         ', '.join('%s (G_KS = %s)' % (('%.4f' % v) if v is not None else 'none', g)
                                                   for g, v in onset['far_continuum_from'].items()), dilute_real))

    # ---------------- KR6: selection rules at the fold
    negm = [conj(o) for o in pos]    # negative-frequency modes of Krein charge -1: their holes are physical antiparticles
    posm = [conj(o) for o in neg]    # negative-frequency modes of Krein charge +1: their holes are ghost antiparticles

    def amps(Op):
        # the largest singular value of the 4 x 4 matrix of the amplitudes: independent of the choice of the basis inside the
        # degenerate multiplets (the largest single entry is not)
        m = lambda A, B: float(np.linalg.svd(np.array([[fold_value(b, a, Op) for a in A] for b in B]), compute_uv=False)[0])
        return {'physical_to_physical': m(neg, neg), 'physical_to_ghost': m(neg, pos), 'pair_physical': m(neg, negm),
                'pair_physical_with_ghost_antiparticle': m(neg, posm), 'pair_ghost_with_physical_antiparticle': m(pos, negm)}
    classes = {'fold_chirality_blind': [], 'fold_chiral': [], 'other': []}
    for r in range(9):
        for I in itertools.combinations(range(8), r):
            Op = I16.copy()
            for a in I:
                Op = Op @ T[a]
            v = amps(Op)
            mixes = v['physical_to_ghost'] > 1e-9 or v['pair_physical_with_ghost_antiparticle'] > 1e-9 or v['pair_ghost_with_physical_antiparticle'] > 1e-9
            if set(I) <= {1, 2, 3, 4}:
                classes['fold_chirality_blind'].append(mixes)
            elif set(I) >= {0, 5, 6, 7}:          # the products Gamma_J Gamma_8, J within {1, 2, 3, 4}
                classes['fold_chiral'].append(mixes)
            else:
                classes['other'].append(mixes)
    portal_ops = {'P_L (Higgs portal)': K.PLN, 'P_R': K.PRN, '1': I16, 'gamma^(4)': T[4], 'gamma^(4) P_L': T[4] @ K.PLN,
                  'gamma^(1)': T[1], 'gamma^(1) P_L': T[1] @ K.PLN, 'Sigma^{12}': K.sig(1, 2), 'Sigma^{12} P_L': K.sig(1, 2) @ K.PLN,
                  'Sigma^{14}': K.sig(1, 4), 'Sigma^{14} P_L': K.sig(1, 4) @ K.PLN, 'Gamma_8': G8}
    table = {nm: amps(Op) for nm, Op in portal_ops.items()}
    mov = {}
    for k in (0.05, 0.15):
        w, nk_, pk_, nk, wpred = moving_states(k)
        mm = lambda Op: (float(np.linalg.svd(np.array([[fold_value(b, a, Op) for a in nk_] for b in pk_]), compute_uv=False)[0]),
                         float(np.linalg.svd(np.array([[fold_value(b, a, Op) for a in nk_] for b in nk_]), compute_uv=False)[0]))
        mov[str(k)] = {'omega': w, 'omega_boost_prediction': wpred, 'states': nk, 'krein': [len(nk_), len(pk_)],
                       'physical_to_ghost': {nm: mm(Op)[0] for nm, Op in (('1', I16), ('gamma^(4)', T[4]), ('gamma^(1)', T[1]),
                                                                        ('gamma^(2)', T[2]), ('Sigma^{12}', K.sig(1, 2)),
                                                                        ('Sigma^{24}', K.sig(2, 4)), ('gamma^(4) Gamma_8', T[4] @ G8))}}
    out['KR6'] = {'counts': {k: [len(v), int(sum(v))] for k, v in classes.items()}, 'portal_table': table, 'moving': mov}
    hl = table['P_L (Higgs portal)']
    ok6 = (len(classes['fold_chirality_blind']) == 16 and not any(classes['fold_chirality_blind'])
           and len(classes['fold_chiral']) == 16 and all(classes['fold_chiral'])
           and all(max(mov[str(k)]['physical_to_ghost'][n] for n in ('1', 'gamma^(4)', 'gamma^(1)', 'gamma^(2)')) < 1e-9 for k in (0.05, 0.15))
           and mov['0.15']['physical_to_ghost']['Sigma^{12}'] > 2 * mov['0.05']['physical_to_ghost']['Sigma^{12}'] > 0
           and hl['physical_to_ghost'] < 1e-12 and hl['pair_physical'] < 1e-12 and hl['pair_physical_with_ghost_antiparticle'] > 0.1
           and all(abs(mov[str(k)]['omega'] - mov[str(k)]['omega_boost_prediction']) < 1e-9 and mov[str(k)]['states'] == 8
                   for k in (0.05, 0.15)))
    rep.check('KR6_selection_rules', ok6,
              'at the fold, at rest: none of the 16 chirality-blind fold operators (products of gamma^(1)..gamma^(4)) connects a '
              'physical state with a ghost, each of the 16 chiral ones (times Gamma_8) does; the Higgs portal P_L (largest singular '
              'values of the 4 x 4 amplitude matrices, independent of the basis): elastic %.5f, conversion %.0e, physical pair %.0e '
              '(no pair at rest), physical particle with ghost antiparticle %.5f (s-wave); moving '
              'along x_1 (k = 0.05, 0.15; eight states at omega = %.10f and %.10f, sqrt(omega_0^2 + k^2) = %.10f and %.10f: the '
              'boost invariance of UM-4): the scalar, density and vector currents still do not mix (below 1e-9), the magnetic '
              'dipole Sigma^{12} does, %.1e and %.1e, in proportion to k' % (
                  hl['physical_to_physical'], hl['physical_to_ghost'], hl['pair_physical'], hl['pair_physical_with_ghost_antiparticle'],
                  mov['0.05']['omega'], mov['0.15']['omega'], mov['0.05']['omega_boost_prediction'],
                  mov['0.15']['omega_boost_prediction'],
                  mov['0.05']['physical_to_ghost']['Sigma^{12}'], mov['0.15']['physical_to_ghost']['Sigma^{12}']))

    # ---------------- KR7: the consequence
    ratio = hl['pair_physical_with_ghost_antiparticle'] / hl['physical_to_physical']
    # all singular values of the two matrices (the elastic and the ghost-pair amplitudes of the Higgs portal)
    sv_el = np.linalg.svd(np.array([[fold_value(b, a, K.PLN) for a in neg] for b in neg]), compute_uv=False)
    sv_gp = np.linalg.svd(np.array([[fold_value(b, a, K.PLN) for a in neg] for b in posm]), compute_uv=False)
    out['KR7'] = {'higgs_portal_ghost_pair_over_elastic': ratio, 'singular_values_elastic': [float(x) for x in sv_el],
                  'singular_values_ghost_pair': [float(x) for x in sv_gp],
                  'vacuum': 'it cannot decay in the positive-energy quantisation: every quantum raises H by its frequency (KR1); '
                            'it is not a state of lowest energy among the states of positive norm (indefinite metric)',
                  'unitarity': 'violated by the chiral parts of the portals (KR6); the Higgs portal is purely left-handed'}
    rep.check('KR7_consequence', abs(ratio - 1) < 1e-3 and np.allclose(sv_el, sv_el[0], rtol=1e-6) and np.allclose(sv_gp, sv_el[0], rtol=1e-3)
              and fock[1]['H_raises_by_omega'] and fock[-1]['H_raises_by_omega'] and dilute_real,
              'in the positive-energy quantisation every quantum of the free field raises the energy by its frequency, so the '
              'vacuum cannot decay (the energy is conserved and no transition lowers it), although with the indefinite metric it '
              'is not a state of lowest energy among the states of positive norm (a superposition of the vacuum and a ghost has a '
              'negative mean energy); the left-handed Higgs portal creates a physical particle chi with a ghost antiparticle at rest '
              'with the amplitude of its elastic one (all four singular values %.5f against %.5f, ratio %.4f): ghosts are produced wherever the chiral portals '
              'act (without the self-interaction their level is degenerate with that of the particles), so with chiral '
              'fold couplings UM-4 is not unitary; chirality-blind couplings are necessary for a unitary UM-4 (at rest they '
              'never connect the two sectors), but not shown to be sufficient (the magnetic dipole connects them for moving '
              'particles, KR6); the classical stability of the gas is not decided: the exact boosts are flat directions, the '
              'occupation of the level is a saddle of the first-order energy (KR8), the truncated response has an imaginary pair '
              'whose meaning is open (KR4), and the partners of the dense gases depend on the size of the box (KR5)' % (
                  sv_gp[0], sv_el[0], ratio))

    # ---------------- KR8: the occupation of the level is a saddle of the first-order energy
    # the free level at the fold holds eight states, four of Krein charge -1 (n_k) and four of +1 (p_j); every
    # four-dimensional subspace of negative Krein norm (the occupation of four particles chi) is spanned by n_k + sum_j Z_kj p_j
    # with a strict contraction Z (a manifold of 32 real dimensions); the first-order energy of the repulsive gas is
    # (G_KS/2) I with I = sum over the two sides of int d sigma e^{7H|sigma|} (rho_hat^2 - tr N_hat^2) (S-9) for the
    # Krein-orthonormal occupied orbitals
    basis8 = neg + pos
    w7 = np.exp(7 * sh16.H * sh16.s)

    def kprod(a, b):
        return sum(K.trap(np.einsum('ji,ik,jk->j', a[i].conj(), BKR, b[i]) * sh16.ew, sh16.h) for i in (0, 1))
    Gram8 = np.array([[kprod(a, b) for b in basis8] for a in basis8])
    Dbil = [np.einsum('aji,il,bjl->jab', np.array([o[side] for o in basis8]).conj(), SIG, np.array([o[side] for o in basis8]))
            for side in (0, 1)]

    def I_first(x):
        Z = (x[:16] + 1j * x[16:]).reshape(4, 4)
        C = np.hstack([np.eye(4), Z])                                     # coefficients of the occupied orbitals in basis8
        Gv = C.conj() @ Gram8 @ C.T
        wv, Uv = np.linalg.eigh(-0.5 * (Gv + Gv.conj().T))
        Cn = (Uv @ np.diag(wv ** -0.5) @ Uv.conj().T).T @ C                  # Krein-orthonormal (charges -1)
        tot = 0.0
        for side in (0, 1):
            beta = np.einsum('la,jab,mb->jlm', Cn.conj(), Dbil[side], Cn)   # chibar_l chi_m on the grid
            rho = np.einsum('jll->j', beta).real / 4
            trN2 = np.einsum('jlm,jml->j', beta, beta).real / 16
            tot += K.trap(w7 * (rho ** 2 - trN2), sh16.h)
        return tot
    x0 = np.zeros(32)
    I0 = I_first(x0)
    hfd = 1e-4
    E32 = np.eye(32)
    grad = np.array([(I_first(x0 + hfd * e_) - I_first(x0 - hfd * e_)) / (2 * hfd) for e_ in E32])
    Hess = np.zeros((32, 32))
    for i_ in range(32):
        for j_ in range(i_, 32):
            Hess[i_, j_] = Hess[j_, i_] = (I_first(x0 + hfd * (E32[i_] + E32[j_])) - I_first(x0 + hfd * (E32[i_] - E32[j_]))
                                           - I_first(x0 - hfd * (E32[i_] - E32[j_])) + I_first(x0 - hfd * (E32[i_] + E32[j_]))) / (4 * hfd ** 2)
    evH, vecH = np.linalg.eigh(Hess)
    scaleH = np.abs(evH).max()
    n_neg, n_zero, n_pos = int(np.sum(evH < -1e-4 * scaleH)), int(np.sum(np.abs(evH) <= 1e-4 * scaleH)), int(np.sum(evH > 1e-4 * scaleH))
    # the zero modes are the exact symmetries: the 16 generators of KR2 that mix the Krein sectors move the occupation along
    # dZ_kj = <p_j, X n_k> (Krein product) without changing I
    tangents = []
    for X in mix:
        dZ = np.array([[kprod(pos[j_], (neg[k_][0] @ X.T, neg[k_][1] @ X.T)) for j_ in range(4)] for k_ in range(4)])
        tangents.append(np.concatenate([dZ.real.ravel(), dZ.imag.ravel()]))
    Tmat = np.array(tangents).T
    rank_sym = int(np.linalg.matrix_rank(Tmat, tol=1e-8))
    sym_null = max(float(np.linalg.norm(Hess @ tv) / (scaleH * np.linalg.norm(tv))) for tv in tangents)
    # towards the null cone (the largest singular value of Z -> 1) along the most negative and the most positive direction
    def along(vec, tt):
        Zv = (vec[:16] + 1j * vec[16:]).reshape(4, 4)
        return I_first(vec / np.linalg.norm(Zv, 2) * tt)
    path_neg = {('%g' % tt): along(vecH[:, 0], tt) for tt in (0.3, 0.9, 0.99, 0.999)}
    path_pos = {('%g' % tt): along(vecH[:, -1], tt) for tt in (0.3, 0.9, 0.99, 0.999)}
    out['KR8_first_order_energy_of_the_occupations'] = {
        'I_multiplet': I0, 'gradient_norm': float(np.linalg.norm(grad)), 'hessian_eigenvalues': [float(x) for x in evH],
        'negative_zero_positive': [n_neg, n_zero, n_pos], 'symmetry_tangents_rank': rank_sym,
        'symmetry_tangents_in_null_space': sym_null, 'toward_null_cone_most_negative': path_neg,
        'toward_null_cone_most_positive': path_pos}
    ok8 = (abs(I0 - 0.10216) < 1e-4 and np.linalg.norm(grad) < 1e-8 and n_neg == 15 and n_zero == 16 and n_pos == 1
           and rank_sym == 16 and sym_null < 1e-4 and path_neg['0.999'] < -100 and path_pos['0.999'] > 100)
    rep.check('KR8_occupation_saddle', ok8,
              'the first-order interaction integral I of S-9 on the 32-dimensional manifold of the occupations of the level at the '
              'fold (four-dimensional subspaces of negative Krein norm, n_k + sum_j Z_kj p_j): at the symmetric multiplet (Z = 0) '
              'I = %.6f, |grad I| = %.1e (a stationary point), and the Hessian has %d negative (%.5f), %d zero and %d positive (%.5f) '
              'eigenvalues; the 16 zero modes are the 16 symmetry generators that mix the Krein sectors (rank %d, |Hess t|/(|Hess| |t|) '
              '<= %.1e): the multiplet is a saddle; towards the null cone (|Z| -> 1) I falls to %.4g along the most negative direction '
              'and rises to %.4g along the most positive one (|Z| = 0.999): the first-order energy of the repulsive gas has no lower '
              'bound on the occupations of negative norm, and the Kohn-Sham states of um4_kohnsham.py are the symmetric stationary '
              'occupation, not a ground state' % (I0, np.linalg.norm(grad), n_neg, evH[0], n_zero, n_pos, evH[-1], rank_sym, sym_null,
                                                   path_neg['0.999'], path_pos['0.999']))

    # ---------------- KR9: the pairs that the convective current creates
    # j_X^mu = i (Psibar P_X d^mu Psi - (d^mu Psibar) P_X Psi) (IN-16; d along the fold) between the vacuum and a pair chi(k)
    # chibar(-k) at the fold: the time component vanishes (the frequencies of the two modes cancel), the spatial one is
    # -2 k <P_X>_pair(k); <P_X>_pair vanishes at rest (KR6) and grows linearly in k, so the amplitude is of the second order in k
    sv_k = {}
    for kk in (0.01, 0.02, 0.05):
        _, negp, posp, nkp, _ = moving_states(kk)
        _, negq, posq, nkq, _ = moving_states(-kk)
        anti = [conj(o) for o in posq]                      # physical antiparticle modes (frequency -omega, mode momentum +k)
        anti_g = [conj(o) for o in negq]                    # ghost antiparticle modes
        row = {}
        for nm, Op in (('P_L', K.PLN), ('P_R', K.PRN), ('1', I16)):
            Mp = np.array([[fold_value(b, a, Op) for a in negp] for b in anti])
            Mg = np.array([[fold_value(b, a, Op) for a in negp] for b in anti_g])
            row[nm] = {'pair_physical': [float(x) for x in np.linalg.svd(Mp, compute_uv=False)],
                       'pair_with_ghost_antiparticle': [float(x) for x in np.linalg.svd(Mg, compute_uv=False)]}
        row['states'] = [nkp, nkq]
        sv_k['%g' % kk] = row
    elastic = {nm: float(np.linalg.svd(np.array([[fold_value(b, a, Op) for a in neg] for b in neg]), compute_uv=False)[0])
               for nm, Op in (('P_L', K.PLN), ('P_R', K.PRN), ('1', I16))}
    slope = {nm: [x / 0.01 for x in sv_k['0.01'][nm]['pair_physical']] for nm in ('P_L', 'P_R', '1')}
    lin = {nm: max(abs(sv_k['%g' % kk][nm]['pair_physical'][0] / (kk * slope[nm][0]) - 1) for kk in (0.02, 0.05)) for nm in slope}
    # (sigma v) for one chi_a chibar_a into a massless chiral fermion pair through c_X J_f.j_X, written with the elastic
    # coupling g_f = 2 omega_b e_X c_X/V_* of FE-47 (e_X the elastic amplitude): g_f^2 omega_b^2 v^4 rho_X/(96 pi), with
    # rho_X = sum_i (dsv_i/dk)^2 omega_b^2/(4 e_X^2) (1 for a Dirac fermion with a scalar density)
    rho = {nm: sum(c_ ** 2 for c_ in slope[nm]) * WB ** 2 / (4 * elastic[nm] ** 2) for nm in slope}
    blind_ghost = max(sv_k['%g' % kk]['1']['pair_with_ghost_antiparticle'][0] for kk in (0.01, 0.02, 0.05))
    # the chirality-blind current creates ghost pairs only at the next order: <1> with the ghost antiparticle grows like k^2
    ghost_k2 = {'%g' % kk: sv_k['%g' % kk]['1']['pair_with_ghost_antiparticle'][0] / kk ** 2 for kk in (0.01, 0.02, 0.05)}
    ghost_c = ghost_k2['0.01']
    ghost_dev = max(abs(v_ / ghost_c - 1) for v_ in ghost_k2.values())
    ghost_rel = ghost_c / slope['1'][0]                     # relative amplitude of the ghost pair: ghost_rel * k
    out['KR9_convective_current_pairs'] = {'singular_values': sv_k, 'elastic': elastic, 'slope_dsv_dk': slope,
                                           'linearity_deviation': lin, 'rho_X': rho,
                                           'chirality_blind_ghost_pairs_max': blind_ghost,
                                           'chirality_blind_ghost_pair_over_k2': ghost_k2,
                                           'chirality_blind_ghost_relative_amplitude_per_k': ghost_rel,
                                           'chirality_blind_ghost_relative_rate_per_k2': ghost_rel ** 2,
                                           'sigma_v': '(sigma v)_{chi chibar} = g_f^2 omega_b^2 v^4 rho_X/(96 pi) per chiral state'}
    ok9 = (all(v_ < 0.01 for v_ in lin.values()) and all(len(set(round(x, 8) for x in slope[nm])) == 1 for nm in slope)
           and abs(rho['1'] - 1) < 0.02 and ghost_dev < 0.01 and ghost_rel < 0.2
           and all(sv_k['%g' % kk]['states'] == [8, 8] for kk in (0.01, 0.02, 0.05)))
    rep.check('KR9_convective_current_pairs', ok9,
              'the physical pair chi(k) chibar(-k) at the fold: the four singular values of <P_X>_pair grow linearly in k (dsv/dk = '
              '%.5f for P_L and P_R, %.5f for 1; deviation from linearity up to k = 0.05: %s), so the convective current, -2k <P_X>_pair, '
              'creates a pair with an amplitude of the second order in k: (sigma v)_{chi chibar} = g_f^2 omega_b^2 v^4 rho_X/(96 pi) '
              'per chiral fermion state, written with the elastic coupling g_f of FE-47 (elastic amplitudes %s), rho_X = %s; for the '
              'chirality-blind current (P_L + P_R = 1) rho = %.4f, the value of a Dirac fermion with a scalar density; it creates a '
              'physical particle with a ghost antiparticle only at the next order in k (the singular values grow like %.4f k^2, '
              'deviation %.1e; %.1e at k = 0.05): ghost pairs with the relative amplitude %.4f k and the relative rate %.4f k^2 '
              '(k in units of m_Psi), small but not zero' % (slope['P_L'][0], slope['1'][0], ', '.join('%s %.1e' % (k_, v_) for k_, v_ in lin.items()),
                               ', '.join('%s %.5f' % (k_, v_) for k_, v_ in elastic.items()),
                               ', '.join('%s %.4f' % (k_, v_) for k_, v_ in rho.items()), rho['1'], ghost_c, ghost_dev,
                               blind_ghost, ghost_rel, ghost_rel ** 2))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM4 / 'outputs' / 'krein.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_4/code/um4_krein.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM4 / 'reports' / 'krein_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
