#!/usr/bin/env python3
"""um4_spectra.py - the states of dirac16complex at the fold of UM-4: no gap in the bulk, the states bound in UM-3 become
resonances, their energies, widths and multiplicity, their Krein form, and the condition that they live longer than the
universe.

Bulk equation of dirac16complex on the static block (um4_geometry.py G9), Psi = e^{(7/2) H |sigma|} chi(sigma) e^{-i omega x4},
fields independent of x1..x3 and of the extra times (k = 0):
    chi' = (m_Psi M0 + omega e^{H|sigma|} M1) chi,   M0 = T^(x0),   M1 = i T^(x0) T^(x4)       (sigma != 0)
(T^(a) = eta^aa T16^A[a]), with the matching condition of the portal terms at the fold (as in UM-3)
    chi(0+) = exp( T^(x0) (mu_L P_L + mu_R P_R) ) chi(0-).
The factor e^{H|sigma|} on omega is new in UM-4 (the time is warped): far from the fold omega e^{H|sigma|} exceeds m_Psi and
every solution oscillates, so there is no gap and no normalisable bound state with omega != 0: the bound states of UM-3
become resonances, solutions with outgoing waves on both sides at a complex omega = omega_r - i Gamma/2.  Computed:
  U1  the algebra: M0^2 = 1, M1^2 = -1, M0 M1 = -M1 M0, and the central element C = T^(x0) T^(x4) T16^8 (C^2 = 1, eigenvalues
      +1 and -1 eight times each) commutes with M0, M1 and the chirality T16^8 (P_L = (1 - T16^8)/2): the 16 components split
      into eight copies of two inequivalent two-dimensional problems, M0 = s3, M1 = i s1, T16^8 = c s1 with c = +-1 (s1, s3
      the Pauli matrices);
  U2  the exact solutions in a copy: with xi = (omega/H) e^{H|sigma|} and nu = m_Psi/H, chi = xi^{1/2} (Z_{nu-1/2}(xi),
      i Z_{nu+1/2}(xi)) on sigma > 0 and chi = xi^{1/2} (-i Z_{nu+1/2}(xi), Z_{nu-1/2}(xi)) on sigma < 0 (Z a Bessel function),
      checked against the differential equation at three depths on each side for Z = J and Z = Y; the outgoing waves are the
      Hankel functions H^(1) = J + i Y;
  U3  the resonances: the zeros of the 2 x 2 determinant of the matching with outgoing waves on both sides, for the cases of
      UM-3 (mu_L, mu_R) = (-1, 0) (UM-3: q_b = m_Psi/2, omega_b = 0.866 m_Psi) and (-0.6, -0.3), for m_Psi/H = 10 to 40:
      omega_r tends to the bound-state energy omega_b of UM-3 as H/m_Psi -> 0, both copies c = +-1 give the same omega, and
      the full 16 x 16 matching matrix has an eight-dimensional kernel there (eight degenerate resonances, as the eight bound
      states of UM-3); the first-order shift omega_r = omega_b (1 - H/(2 q_b)) is tested at m_Psi/H = 400 to 3200 (computed
      with the forward recurrence of the spherical Hankel functions, exact for integer m_Psi/H): the remainder times
      (m_Psi/H)^2 converges like H/m_Psi, to -2.60 for (-1, 0) and -5.69 for (-0.6, -0.3);
  U4  the width: ln(Gamma/omega_b) falls linearly in m_Psi/H with the slope -2F(u_b), F(u) = int_u^1 sqrt(1 - t^2)/t dt =
      ln((1 + sqrt(1 - u^2))/u) - sqrt(1 - u^2), u_b = omega_b/m_Psi (the tunnelling exponent through the region where
      omega e^{H|sigma|} < m_Psi), checked by the differences of the computed widths; and the prefactor: for m_Psi/H -> infinity
          Gamma = (2/e) (q_b^2/m_Psi) e^{-2F(u_b) m_Psi/H},
      derived from the Debye asymptotics of the Bessel functions (Y_mu(mu sech a) ~ -e^{mu(a - tanh a)}/sqrt(pi mu tanh a/2),
      J_mu(mu sech a) ~ e^{-mu(a - tanh a)}/sqrt(2 pi mu tanh a)): the ratio r = H^(1)_{nu+1/2}/H^(1)_{nu-1/2} at the fold is
      rho (1 - i eps) with rho ~ e^a and eps ~ e^{-2 nu F} sinh a (sech a = omega/m_Psi), the matching condition r^2 = r_b^2
      (real) gives Gamma = -2 eps/(d ln rho/d omega) = 2 m_Psi (q_b/m_Psi)^2 e^{-2 nu F(u_r)}, and the first-order shift of
      omega_r adds 1 to the exponent, nu F(u_r) = nu F(u_b) + 1/2; the computed prefactor approaches (2/e)(q_b/m_Psi)^2 like
      H/m_Psi (at m_Psi/H = 100, 1000, 4000 for both bindings, and at q_b = 0.99 m_Psi);
  U5  the dispersion, computed: the resonance at rest, boosted along x3 by the generator T^(x3) T^(x4)/2 (um4_bulk.py B7) with
      the complex rapidity asinh(k/omega_0), solves the 16-component equation of a state with the momentum k,
      chi' = (m_Psi M0 + e^{H|sigma|}(omega M1 + k M_k)) chi (M_k = -i T^(x0) T^(x3)), with omega = sqrt(omega_0^2 + k^2) on both
      sides of the fold and satisfies the matching at the fold: a resonance moving with the momentum k has
      omega^2 = omega_0^2 + k^2 and moves slower than light;
  U6  the condition that the particles chi live long enough for every binding (mu_L = -2 q_b/m_Psi, mu_R = 0, q_b/m_Psi from
      0.0995 (q_b/omega_b = 0.1) to 0.999): Gamma < hbar/tau at H = H_min (the bound 2534 GeV of um4_propagators.py P5), with
      the exact width at the bound (integer m_Psi/H by the recurrence of U3, interpolated in ln Gamma) where m_Psi/H <= 6000,
      and with the derived asymptotic width of U4 for weaker binding; the lifetimes tau = t_0 = 13.8 Gyr, 160 Gyr = 11.6 t_0
      (the observed bound for dark matter that decays into invisible relativistic particles, Audren et al., JCAP 12 (2014)
      028: the requirement used here) and 100 t_0; for 160 Gyr the lightest long-lived chi has omega_b > 4.3e8 GeV
      (q_b/omega_b = 0.1), 1.4e7 GeV (q_b = 0.3 m_Psi), 2.5e6 GeV (q_b = m_Psi/2), 1.1e5 GeV (q_b = 0.9 m_Psi), 1.2e4 GeV
      (q_b = 0.99 m_Psi) and 2.2e3 GeV (q_b = 0.999 m_Psi): the bound falls with the binding and vanishes as q_b -> m_Psi
      (omega_b -> 0);
  U7  the Krein form of the eight resonances, integrated over the region of the fold |sigma| < sigma_t/2 (sigma_t the turning
      point omega_r e^{H sigma_t} = m_Psi) with the density e^{H|sigma|} chi^dagger B chi (B = i sigma16 T^(x4)): four positive
      and four negative eigenvalues, as for the bound states of UM-3;
  U8  the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma) (the reflection across the fold with that of ordinary space) maps the
      eight resonances onto themselves; four are even and four odd, the even ones of one Krein sign and the odd ones of the
      other (so that a mean field that is even under R_1 cannot mix the two signs).
Reads outputs/propagators.json (run um4_propagators.py first).
Writes outputs/spectra.json and reports/spectra_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_spectra.py

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

import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sla

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM                          # noqa: E402
from um4_common import Report, write             # noqa: E402

T = GM.T16A()
ETA = GM.eta4488()
TN = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
TUP = {a: float(ETA[a, a]) * TN[a] for a in range(8)}
PLN, PRN = (np.array(P_.tolist(), dtype=float) for P_ in GM.projectors())
SIG16 = np.array(GM.sigma16().tolist(), dtype=float)
I16 = np.eye(16)
M0 = TUP[0]
M1 = 1j * TUP[0] @ TUP[4]
T9 = TN[8]
S1 = mp.matrix([[0, 1], [1, 0]])
S3 = mp.matrix([[1, 0], [0, -1]])


def expm2(A):
    """exp of a 2 x 2 mpmath matrix."""
    return mp.expm(A)


def F_wkb(u):
    u = mp.mpf(u)
    return mp.log((1 + mp.sqrt(1 - u * u)) / u) - mp.sqrt(1 - u * u)


def lam_um3(muL, muR):
    s2 = muL * muR
    if abs(s2) < 1e-15:
        f = 1.0
    elif s2 > 0:
        s_ = math.sqrt(s2)
        f = math.tanh(s_) / s_
    else:
        s_ = math.sqrt(-s2)
        f = math.tan(s_) / s_
    return -(muL + muR) * f / 2


def det2(omega, nu, muL, muR, c):
    """The determinant of the matching of the outgoing solutions in the copy c (m_Psi = nu, H = 1)."""
    xi = omega
    hm = mp.hankel1(nu - mp.mpf(1) / 2, xi)
    hp = mp.hankel1(nu + mp.mpf(1) / 2, xi)
    r = hp / hm                                   # normalised: the common factor xi^{1/2} H^(1)_{nu-1/2} dropped
    vp = mp.matrix([1, 1j * r])                   # sigma = 0+
    vm = mp.matrix([-1j * r, 1])                  # sigma = 0-
    pL = (mp.eye(2) - c * S1) / 2
    pR = (mp.eye(2) + c * S1) / 2
    N = expm2(S3 * (muL * pL + muR * pR))
    w = N * vm
    return vp[0] * w[1] - vp[1] * w[0]


def resonance(nu, muL, muR, c, dps=40):
    mp.mp.dps = dps
    lam = lam_um3(muL, muR) * nu
    wb = math.sqrt(nu * nu - lam * lam)
    f = lambda w: det2(w, mp.mpf(nu), mp.mpf(muL), mp.mpf(muR), c)
    # start from the UM-3 energy with the WKB width
    g0 = wb * float(mp.exp(-2 * F_wkb(wb / nu) * nu))
    root = mp.findroot(f, mp.mpc(wb, -g0 / 2))
    return root, wb


def det2_ratio(r, muL, muR, c):
    """The matching determinant of the copy c as a function of the ratio r = H^(1)_{nu+1/2}/H^(1)_{nu-1/2} at the fold."""
    vp = mp.matrix([1, 1j * r])
    vm = mp.matrix([-1j * r, 1])
    pL = (mp.eye(2) - c * S1) / 2
    pR = (mp.eye(2) + c * S1) / 2
    N = expm2(S3 * (muL * pL + muR * pR))
    w = N * vm
    return vp[0] * w[1] - vp[1] * w[0]


def ratio_hankel(nu, w):
    return mp.hankel1(nu + mp.mpf(1) / 2, w) / mp.hankel1(nu - mp.mpf(1) / 2, w)


def ratio_sph(N, z):
    """H^(1)_{N+1/2}(z)/H^(1)_{N-1/2}(z) = h_N(z)/h_{N-1}(z) for an integer N >= 1, by the forward recurrence of the spherical
    Hankel functions of the first kind, h_{n+1} = (2n + 1) h_n/z - h_{n-1} (h_0 = -i e^{iz}/z, h_1 = -e^{iz}(z + i)/z^2)."""
    a = -1j * mp.exp(1j * z) / z
    b = -mp.exp(1j * z) * (z + 1j) / z ** 2
    for n in range(1, N):
        a, b = b, (2 * n + 1) / z * b - a
    return b / a


def resonance_robust(nu, muL, muR, c=1, integer=False):
    """The resonance of the copy c for any binding: the real root of Re D bracketed around the first-order estimate
    omega_b (1 - H/(2 q_b)) (Anderson's method), then Newton steps in the complex plane; the working precision 40 +
    2 F(u_b) nu/ln 10 digits resolves the width ~ m e^{-2 F nu}.  Returns (omega, q_b/m, u_b, F(u_b)), H = 1, m = nu."""
    qb_m = lam_um3(muL, muR)
    ub = math.sqrt(1 - qb_m ** 2)
    Fb = float(F_wkb(ub))
    mp.mp.dps = 40 + int(2 * Fb * nu / 2.3)
    nu_ = mp.mpf(nu)
    rat = (lambda w: ratio_sph(int(nu), w)) if integer else (lambda w: ratio_hankel(nu_, w))
    f = lambda w: det2_ratio(rat(w), mp.mpf(muL), mp.mpf(muR), c)
    w1 = ub * nu * (1 - 1 / (2 * qb_m * nu))
    a, b = mp.mpf(w1 * 0.97), mp.mpf(min(w1 * 1.03, nu * 0.99999))
    wr = mp.findroot(lambda w: mp.re(f(w)), (a, b), solver='anderson', tol=mp.mpf(10) ** (-(mp.mp.dps - 8)))
    w = mp.mpc(wr)
    for _ in range(3):
        hstep = mp.mpf(10) ** (-(mp.mp.dps // 3)) * nu
        d = (f(w + hstep) - f(w - hstep)) / (2 * hstep)
        w = w - f(w) / d
    return w, qb_m, ub, Fb


def p_asymptotic(qb_m):
    """The derived prefactor of the width for m_Psi/H -> infinity: Gamma/m_Psi = (2/e) (q_b/m_Psi)^2 e^{-2 F(u_b) m_Psi/H}."""
    return 2.0 / math.e * qb_m ** 2


def lifetime_bound(qb_m, H_GeV, Gamma_max, exact_max_nu=6000):
    """The smallest m_Psi/H for which the width at the given H is below Gamma_max (mu_L = -2 q_b/m_Psi, mu_R = 0): the exact
    width at integer m_Psi/H (spherical Hankel recurrence), ln Gamma interpolated linearly between the neighbouring integers
    that bracket the bound, for m_Psi/H <= exact_max_nu; above, the derived asymptotic width (its error is of the order
    H/q_b, below 1e-5 there)."""
    ub = math.sqrt(1 - qb_m ** 2)
    Fb = float(F_wkb(ub))
    Pinf = p_asymptotic(qb_m)
    nu_a = 10.0
    for _ in range(200):
        nu_a = math.log(Pinf * nu_a * H_GeV / Gamma_max) / (2 * Fb)
    row = {'q_b_over_m': qb_m, 'q_b_over_omega_b': qb_m / ub, 'u_b': ub, 'F': Fb, 'P_asymptotic': Pinf,
           'm_over_H_asymptotic': nu_a}
    if nu_a > exact_max_nu:
        row.update({'method': 'asymptotic width', 'm_over_H_min': nu_a, 'P_exact_at_bound': None})
    else:
        def lnG(N):
            w, _, _, _ = resonance_robust(N, -2 * qb_m, 0.0, 1, integer=True)
            gm = float(-2 * w.imag) / N
            return math.log(gm) + math.log(N * H_GeV / Gamma_max), gm
        N = max(2, int(math.floor(nu_a)))
        fN, gN = lnG(N)
        while fN <= 0:
            N -= 1
            fN, gN = lnG(N)
        fN1, gN1 = lnG(N + 1)
        while fN1 > 0:
            N += 1
            fN, gN = fN1, gN1
            fN1, gN1 = lnG(N + 1)
        nu_min = N + fN / (fN - fN1)
        P_ex = gN * math.exp(2 * Fb * N)
        row.update({'method': 'exact width', 'm_over_H_min': nu_min, 'P_exact_at_bound': P_ex,
                    'P_exact_over_asymptotic': P_ex / Pinf})
    row['m_Psi_min_GeV'] = row['m_over_H_min'] * H_GeV
    row['omega_b_min_GeV'] = ub * row['m_Psi_min_GeV']
    return row


def outgoing16(omega, nu):
    """The eight outgoing solutions at 0+ and at 0- in the 16-component space (columns), H = 1."""
    ev, vec = np.linalg.eig(M0)
    E = vec[:, np.isclose(ev, 1)]
    Fv = -1j * M1 @ E
    hm = complex(mp.hankel1(nu - 0.5, omega))
    hp = complex(mp.hankel1(nu + 0.5, omega)) / hm
    hm = 1.0
    Vp = hm * E + 1j * hp * Fv
    Vm = hm * Fv - 1j * hp * E                     # (-psi2, psi1) in the basis (e', f') = (f, -e)
    return Vp, Vm


def main():
    rep = Report()
    out = {}

    # ---------------- U1: the algebra
    C = TUP[0] @ TUP[4] @ T9
    ok1 = (np.allclose(M0 @ M0, I16) and np.allclose(M1 @ M1, -I16) and np.allclose(M0 @ M1 + M1 @ M0, 0)
           and np.allclose(C @ C, I16) and np.allclose(C @ M0, M0 @ C) and np.allclose(C @ M1, M1 @ C)
           and np.allclose(C @ T9, T9 @ C) and np.allclose(PLN, (I16 - T9) / 2))
    evC = np.linalg.eigvals(C).real
    ok1 &= int(np.sum(evC > 0.5)) == 8 and int(np.sum(evC < -0.5)) == 8
    rep.check('U1_algebra', ok1, 'M0^2 = 1, M1^2 = -1, {M0, M1} = 0; C = T^(x0) T^(x4) T16^8 squares to 1 (eigenvalues +1, -1 eight '
              'times each) and commutes with M0, M1 and T16^8; P_L = (1 - T16^8)/2: eight copies of two inequivalent 2 x 2 problems')

    # ---------------- U2: the exact solutions, both kinds of Bessel functions, on both sides of the fold
    mp.mp.dps = 30
    nu = mp.mpf(7.3)
    om = mp.mpf(5.1)
    ok2 = True
    worst2 = 0
    for side in (1, -1):
        for Z in (mp.besselj, mp.bessely):
            for s_ in (0.2, 0.9, 1.7):
                sig = mp.mpf(s_) * side
                if side == 1:
                    psi = lambda sg, Z=Z: mp.sqrt(om * mp.e ** abs(sg)) * mp.matrix([Z(nu - 0.5, om * mp.e ** abs(sg)), 1j * Z(nu + 0.5, om * mp.e ** abs(sg))])
                else:
                    psi = lambda sg, Z=Z: mp.sqrt(om * mp.e ** abs(sg)) * mp.matrix([-1j * Z(nu + 0.5, om * mp.e ** abs(sg)), Z(nu - 0.5, om * mp.e ** abs(sg))])
                d = (psi(sig + mp.mpf('1e-12')) - psi(sig - mp.mpf('1e-12'))) / mp.mpf('2e-12')
                rhs = (nu * mp.matrix([[1, 0], [0, -1]]) + om * mp.e ** abs(sig) * mp.matrix([[0, 1j], [1j, 0]])) * psi(sig)
                rel = mp.norm(d - rhs) / mp.norm(rhs)
                worst2 = max(worst2, float(rel))
                ok2 &= rel < mp.mpf('1e-8')
    rep.check('U2_exact_solutions', ok2, 'chi = xi^{1/2} (Z_{nu-1/2}(xi), i Z_{nu+1/2}(xi)) on sigma > 0 and xi^{1/2} (-i Z_{nu+1/2}(xi), '
              'Z_{nu-1/2}(xi)) on sigma < 0, xi = (omega/H) e^{H|sigma|}, solve chi\' = (nu s3 + omega e^{H|sigma|} i s1) chi (nu = '
              'm_Psi/H) for Z = J and Z = Y at three depths on each side (largest relative residual %.1e)' % worst2)

    # ---------------- U3, U4: the resonances
    rows = []
    ok3 = True
    ok4 = True
    for (muL, muR) in ((-1.0, 0.0), (-0.6, -0.3)):
        series = []
        for nuv in (10, 20, 30, 40):
            rts = []
            for c in (1, -1):
                r_, wb = resonance(nuv, muL, muR, c)
                rts.append(r_)
            same = abs(rts[0] - rts[1]) < mp.mpf(10) ** (-20) * abs(rts[0])
            w = rts[0]
            # 16 x 16 check: the matching matrix [Vp | -N Vm] has an eight-dimensional kernel
            Vp, Vm = outgoing16(complex(w), nuv)
            N16 = sla.expm(TUP[0] @ (muL * PLN + muR * PRN))
            Mbig = np.hstack([Vp, -N16 @ Vm])
            sv = np.linalg.svd(Mbig, compute_uv=False)
            kern = int(np.sum(sv / sv[0] < 1e-9))
            series.append({'m_over_H': nuv, 'omega_r_over_m': float(w.real / nuv), 'Gamma_over_m': float(-2 * w.imag / nuv),
                           'omega_b_UM3_over_m': wb / nuv, 'copies_equal': bool(same), 'kernel_16': kern})
            ok3 &= same and kern == 8
        # the first-order shift omega_r = omega_b (1 - H/(2 q_b)): the remainder times (m/H)^2 tends to a constant
        qbm = lam_um3(muL, muR)
        rem = []
        for nuv in (400, 800, 1600, 3200):
            w_, _, ub_, _ = resonance_robust(nuv, muL, muR, 1, integer=True)
            first = ub_ * (1 - 1 / (2 * qbm * nuv))
            rem.append({'m_over_H': nuv, 'omega_r_over_m': float(w_.real) / nuv, 'first_order': first,
                        'remainder_times_nu2': (float(w_.real) / nuv - first) * nuv ** 2})
        rr_ = [x['remainder_times_nu2'] for x in rem]
        dif = [abs(rr_[i + 1] - rr_[i]) for i in range(3)]
        c2_ = 2 * rr_[-1] - rr_[-2]                         # Richardson extrapolation of c2 + c3 H/m_Psi
        ok3 &= all(0.35 < dif[i + 1] / dif[i] < 0.65 for i in range(2)) and abs(c2_) < 10
        ub = series[0]['omega_b_UM3_over_m']
        Fb = float(F_wkb(ub))
        slopes = [(math.log(series[i + 1]['Gamma_over_m']) - math.log(series[i]['Gamma_over_m'])) / 10 for i in range(3)]
        ok4 &= abs(slopes[-1] / (-2 * Fb) - 1) < 0.1
        # the derived asymptotic width (2/e)(q_b/m)^2 m e^{-2 F nu}: the computed prefactor approaches it like 1/nu
        pref = []
        for nuv in (100, 1000, 4000):
            w_, _, _, _ = resonance_robust(nuv, muL, muR, 1, integer=True)
            Pn = float(-2 * w_.imag) / nuv * math.exp(2 * Fb * nuv)
            pref.append({'m_over_H': nuv, 'prefactor': Pn, 'ratio_to_asymptotic': Pn / p_asymptotic(qbm),
                         'deviation_times_nu': (Pn / p_asymptotic(qbm) - 1) * nuv})
        dv = [abs(x['ratio_to_asymptotic'] - 1) for x in pref]
        ok4 &= dv[0] > dv[1] > dv[2] and dv[2] < 5e-3 and abs(pref[2]['deviation_times_nu'] / pref[1]['deviation_times_nu'] - 1) < 0.1
        rows.append({'mu_L': muL, 'mu_R': muR, 'q_b_over_m': qbm, 'series': series, 'first_order_remainder': rem,
                     'second_order_coefficient': c2_, 'F_wkb': Fb,
                     'slopes_dlnGamma_dnu': slopes, 'predicted_slope': -2 * Fb, 'prefactor_vs_asymptotic': pref,
                     'P_asymptotic': p_asymptotic(qbm)})
    # strong binding: the prefactor at q_b = 0.99 m_Psi
    strong = []
    for nuv in (20, 60, 200):
        w_, qbm_, ub_, Fb_ = resonance_robust(nuv, -1.98, 0.0, 1, integer=True)
        Pn = float(-2 * w_.imag) / nuv * math.exp(2 * Fb_ * nuv)
        strong.append({'m_over_H': nuv, 'omega_r_over_m': float(w_.real) / nuv, 'prefactor': Pn, 'ratio_to_asymptotic': Pn / p_asymptotic(qbm_)})
    ok4 &= all(abs(s_['ratio_to_asymptotic'] - 1) < 0.05 for s_ in strong) and abs(strong[-1]['ratio_to_asymptotic'] - 1) < 0.01
    out['U3_resonances'] = rows
    out['U4_strong_binding_prefactor'] = {'q_b_over_m': 0.99, 'rows': strong, 'P_asymptotic': p_asymptotic(0.99)}
    rep.check('U3_resonances', ok3, 'outgoing waves on both sides: the resonances of the two copies coincide, the 16 x 16 matching has an '
              'eight-dimensional kernel, and omega_r/m_Psi -> omega_b/m_Psi of UM-3: %s; the remainder of the first-order formula '
              'omega_b (1 - H/(2 q_b)) times (m_Psi/H)^2 at m_Psi/H = 400, 800, 1600, 3200: %s, converging like H/m_Psi to %s: the '
              'first-order shift is exact and the rest is of the second order in H/m_Psi' % (
                  '; '.join('(%g, %g): %s -> %.4f' % (r_['mu_L'], r_['mu_R'], ', '.join('%.4f' % s['omega_r_over_m'] for s in r_['series']),
                                                       r_['series'][0]['omega_b_UM3_over_m']) for r_ in rows),
                  '; '.join('(%g, %g): %s' % (r_['mu_L'], r_['mu_R'], ', '.join('%.4f' % x['remainder_times_nu2'] for x in r_['first_order_remainder']))
                            for r_ in rows), ', '.join('%.3f' % r_['second_order_coefficient'] for r_ in rows)))
    rep.check('U4_widths', ok4, 'd ln Gamma/d(m_Psi/H) between m_Psi/H = 30 and 40: %s against -2F(u_b) = %s (F(u) = ln((1 + '
              'sqrt(1 - u^2))/u) - sqrt(1 - u^2)); the prefactor Gamma e^{2F m_Psi/H}/m_Psi at m_Psi/H = 100, 1000, 4000: %s, approaching '
              'the derived asymptotic value (2/e)(q_b/m_Psi)^2 = %s like H/m_Psi; at q_b = 0.99 m_Psi (m_Psi/H = 20, 60, 200) %s of '
              'the asymptotic value %.4f' % (
                  ', '.join('%.4f' % r_['slopes_dlnGamma_dnu'][-1] for r_ in rows), ', '.join('%.4f' % r_['predicted_slope'] for r_ in rows),
                  '; '.join(', '.join('%.5f' % x['prefactor'] for x in r_['prefactor_vs_asymptotic']) for r_ in rows),
                  ', '.join('%.5f' % r_['P_asymptotic'] for r_ in rows), ', '.join('%.4f' % s_['ratio_to_asymptotic'] for s_ in strong),
                  p_asymptotic(0.99)))

    # ---------------- U5: the dispersion of a resonance, computed: the boosted resonance solves the equation of a moving state
    nu5, k5 = 30, 0.3                                      # m_Psi/H and the momentum along x3 in units of m_Psi
    w0, _ = resonance(nu5, -1.0, 0.0, 1)
    w0c = complex(w0)
    Vp5, Vm5 = outgoing16(w0c, nu5)
    N16 = sla.expm(TUP[0] @ (-1.0 * PLN))
    U5_, s5_, Vh5 = np.linalg.svd(np.hstack([Vp5, -N16 @ Vm5]))
    ker5 = Vh5.conj().T[:, -8:]
    ev0, vec0 = np.linalg.eig(M0)
    E0 = vec0[:, np.isclose(ev0, 1)]
    F0 = -1j * M1 @ E0
    kz = k5 * nu5                                           # k in units of H
    S34 = 0.5 * TUP[3] @ TUP[4]                             # the boost along x3 (um4_bulk.py B7)
    beta = np.arcsinh(kz / w0c)                             # complex rapidity: omega_0 cosh(beta) = omega, omega_0 sinh(beta) = k
    Sb = sla.expm(beta * S34)
    wk = np.sqrt(w0c ** 2 + kz ** 2)
    Mk = -1j * TUP[0] @ TUP[3]
    worst5 = 0.0
    mp.mp.dps = 30
    for side in (1, -1):
        coef = ker5[:8, :] if side == 1 else ker5[8:, :]
        for s_v in (0.05, 0.4, 1.2, 2.5):
            def prof(sv):
                xi = w0c * math.exp(sv)
                pre = complex(mp.sqrt(xi))
                h1 = complex(mp.hankel1(nu5 - 0.5, xi)) * pre
                h2 = complex(mp.hankel1(nu5 + 0.5, xi)) * pre
                basis = (h1 * E0 + 1j * h2 * F0) if side == 1 else (h1 * F0 - 1j * h2 * E0)
                return Sb @ (basis @ coef)
            hs = 1e-6
            dchi = (prof(s_v + hs) - prof(s_v - hs)) / (2 * hs)
            # on sigma < 0 the coordinate is -s_v: d/d sigma = -d/ds, and e^{H|sigma|} = e^{s_v}
            lhs = dchi if side == 1 else -dchi
            rhs = (nu5 * M0 + math.exp(s_v) * (wk * M1 + kz * Mk)) @ prof(s_v)
            worst5 = max(worst5, float(np.linalg.norm(lhs - rhs) / np.linalg.norm(rhs)))
    # the matching at the fold of the boosted states
    chi_p = Sb @ (Vp5 @ ker5[:8, :])
    chi_m = Sb @ (Vm5 @ ker5[8:, :])
    match5 = float(np.linalg.norm(chi_p - N16 @ chi_m) / np.linalg.norm(chi_p))
    comm5 = float(np.abs(S34 @ N16 - N16 @ S34).max())
    ok5 = worst5 < 1e-6 and match5 < 1e-9 and comm5 < 1e-12
    out['U5_dispersion'] = {'m_over_H': nu5, 'k_over_m': k5, 'omega_0_over_m': [w0c.real / nu5, w0c.imag / nu5],
                            'omega_over_m': [wk.real / nu5, wk.imag / nu5], 'ode_residual': worst5, 'fold_matching_residual': match5,
                            'boost_commutes_with_fold_matching': comm5,
                            'group_velocity_real_part': float((kz / wk).real)}
    rep.check('U5_dispersion', ok5, 'the resonance at rest (m_Psi/H = %d, (mu_L, mu_R) = (-1, 0), omega_0 = (%.6f - %.2e i) m_Psi), boosted '
              'along x3 with the complex rapidity asinh(k/omega_0) (k = %.1f m_Psi), solves the 16-component equation of a moving state, '
              'chi\' = (m_Psi M0 + e^{H|sigma|}(omega M1 + k M_k)) chi with omega = sqrt(omega_0^2 + k^2), on both sides (largest relative '
              'residual %.1e) and the matching at the fold (%.1e; the boost commutes with it, %.1e): a resonance moving with the momentum '
              'k has omega^2 = omega_0^2 + k^2, the group velocity Re(k/omega) = %.4f below 1' % (
                  nu5, w0c.real / nu5, -w0c.imag / nu5 * 2, k5, worst5, match5, comm5, float((kz / wk).real)))

    # ---------------- U6: the lifetime condition for every binding
    hbar = 6.582119569e-25                               # GeV s
    t0 = 13.8e9 * 3.15576e7                              # s
    prop = json.loads((HERE.parent / 'outputs' / 'propagators.json').read_text())
    Hmin = prop['P5_bounds']['H_min_from_Z_invisible_width_GeV']
    bindings = [0.1 / math.sqrt(1.01), 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99, 0.999]
    lifetimes = (1.0, 160.0 / 13.8, 100.0)
    est = []
    for life in lifetimes:
        Gmax = hbar / (life * t0)
        for qb_m in bindings:
            r6 = lifetime_bound(qb_m, Hmin, Gmax)
            r6.update({'lifetime_over_t0': life, 'Gamma_max_GeV': Gmax})
            est.append(r6)
    req = [e_ for e_ in est if abs(e_['lifetime_over_t0'] - 160.0 / 13.8) < 1e-9]
    one = [e_ for e_ in est if e_['lifetime_over_t0'] == 1.0]
    mono = all(a_['omega_b_min_GeV'] > b_['omega_b_min_GeV'] for grp in (one, req) for a_, b_ in zip(grp[:-1], grp[1:]))
    exact_ok = (all(abs(e_['P_exact_over_asymptotic'] - 1) < 0.04 for e_ in est if e_['method'] == 'exact width')
                and all(abs(e_['P_exact_over_asymptotic'] - 1) < 0.01 for e_ in est if e_['method'] == 'exact width'
                        and e_['m_over_H_min'] > 1000))
    half = [e_ for e_ in one if abs(e_['q_b_over_m'] - 0.5) < 1e-12][0]
    ok6 = (mono and exact_ok and 1.0e3 < half['m_over_H_min'] < 1.2e3 and 2.2e6 < half['omega_b_min_GeV'] < 2.6e6
           and min(e_['omega_b_min_GeV'] for e_ in req) < 1e4)
    out['U6_lifetime'] = {'H_min_GeV': Hmin, 'requirement': 'tau > 160 Gyr = 11.6 t_0 (decay into invisible relativistic particles: '
                                                         'Audren et al., JCAP 12 (2014) 028)',
                          'prefactor_asymptotic': '(2/e) (q_b/m_Psi)^2', 'rows': est}
    rep.check('U6_lifetime_condition', ok6, 'Gamma < hbar/tau at H = %.0f GeV (um4_propagators.py P5), with the exact widths at the bound '
              '(their prefactor within %s of the asymptotic (2/e)(q_b/m_Psi)^2) or the derived asymptotic width for weak binding; '
              'for the lifetime 160 Gyr (11.6 t_0, the observed bound for an invisible decay): %s; for t_0: q_b = m_Psi/2 needs '
              'm_Psi/H > %.4g (omega_b > %.3g GeV): the bound on omega_b falls with the binding and vanishes as q_b -> m_Psi' % (
                  Hmin, '4 per cent (1 per cent where m_Psi/H > 1000)', '; '.join('q_b/m_Psi = %.4g: m_Psi/H > %.4g, omega_b > %.3g GeV' % (
                      e_['q_b_over_m'], e_['m_over_H_min'], e_['omega_b_min_GeV']) for e_ in req),
                  half['m_over_H_min'], half['omega_b_min_GeV']))

    # ---------------- U7: the Krein form near the fold
    B = 1j * SIG16 @ TUP[4]
    okB = np.allclose(B, B.conj().T) and np.allclose(B @ B, I16)
    krein = []
    for (muL, muR) in ((-1.0, 0.0), (-0.6, -0.3)):
        nuv = 30
        w, wb = resonance(nuv, muL, muR, 1)
        w = complex(w)
        Vp, Vm = outgoing16(w, nuv)
        N16 = sla.expm(TUP[0] @ (muL * PLN + muR * PRN))
        Mbig = np.hstack([Vp, -N16 @ Vm])
        U_, s_, Vh = np.linalg.svd(Mbig)
        ker = Vh.conj().T[:, -8:]
        ab = ker[:8, :]
        bb = ker[8:, :]
        # profiles: chi(sigma > 0) = sum_k a_k (psi1 e_k + psi2 f_k) etc.; integrate the Krein density numerically
        ev, vec = np.linalg.eig(M0)
        E = vec[:, np.isclose(ev, 1)]
        Fv = -1j * M1 @ E
        st = math.log(nuv / w.real)                    # turning point (H = 1)
        sg = np.linspace(0, st / 2, 400)
        G = np.zeros((8, 8), dtype=complex)
        for side in (1, -1):
            coef = ab if side == 1 else bb
            for j, s_v in enumerate(sg):
                xi = w * math.exp(s_v)
                pref = complex(mp.sqrt(xi))
                h1 = complex(mp.hankel1(nuv - 0.5, xi)) * pref
                h2 = complex(mp.hankel1(nuv + 0.5, xi)) * pref
                if side == 1:
                    basis = h1 * E + 1j * h2 * Fv
                else:
                    basis = h1 * Fv - 1j * h2 * E
                chi = basis @ coef                     # 16 x 8
                wt = (sg[1] - sg[0]) * (0.5 if j in (0, len(sg) - 1) else 1.0) * math.exp(s_v)
                G += wt * chi.conj().T @ B @ chi
        G = 0.5 * (G + G.conj().T)
        evs = np.linalg.eigvalsh(G)
        scale = max(abs(evs))
        npos, nneg = int(np.sum(evs > 1e-6 * scale)), int(np.sum(evs < -1e-6 * scale))
        # the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma): a state is fixed by (chi(0+), chi(0-)) = (Vp a, Vm b)
        R = TN[0] @ TN[1] @ TN[2] @ TN[3]
        top = Vp @ ab                                   # chi(0+) of the eight states
        bot = Vm @ bb                                   # chi(0-)
        Rtop, Rbot = R @ bot, R @ top                   # the reflected states
        basis = np.vstack([top, bot])
        image = np.vstack([Rtop, Rbot])
        Rm, res_, rk, sv_ = np.linalg.lstsq(basis, image, rcond=None)
        closed = np.linalg.norm(basis @ Rm - image) < 1e-8 * np.linalg.norm(image)
        evR = np.linalg.eigvals(Rm)
        n_even = int(np.sum(np.abs(evR - 1) < 1e-6))
        n_odd = int(np.sum(np.abs(evR + 1) < 1e-6))
        # Krein signs on the even and odd subspaces
        wR, VR = np.linalg.eig(Rm)
        Ve = VR[:, np.abs(wR - 1) < 1e-6]
        Vo = VR[:, np.abs(wR + 1) < 1e-6]
        ke = np.linalg.eigvalsh(0.5 * ((Ve.conj().T @ G @ Ve) + (Ve.conj().T @ G @ Ve).conj().T)) if Ve.shape[1] else np.array([])
        ko = np.linalg.eigvalsh(0.5 * ((Vo.conj().T @ G @ Vo) + (Vo.conj().T @ G @ Vo).conj().T)) if Vo.shape[1] else np.array([])
        sign_even = 'negative' if ke.size and np.all(ke < 0) else ('positive' if ke.size and np.all(ke > 0) else 'mixed')
        sign_odd = 'negative' if ko.size and np.all(ko < 0) else ('positive' if ko.size and np.all(ko > 0) else 'mixed')
        krein.append({'mu_L': muL, 'mu_R': muR, 'm_over_H': nuv, 'positive': npos, 'negative': nneg, 'R1_closed': bool(closed),
                      'R1_even': n_even, 'R1_odd': n_odd, 'krein_sign_even': sign_even, 'krein_sign_odd': sign_odd})
    out['U7_krein'] = krein
    ok7 = okB and all(k_['positive'] == 4 and k_['negative'] == 4 for k_ in krein)
    rep.check('U7_krein_signature', ok7, 'the Krein Gram matrix of the eight resonances near the fold has (positive, negative) = %s, as '
              'the bound states of UM-3 (4, 4)' % [(k_['positive'], k_['negative']) for k_ in krein])
    ok8 = all(k_['R1_closed'] and k_['R1_even'] == 4 and k_['R1_odd'] == 4 and k_['krein_sign_even'] != 'mixed'
              and k_['krein_sign_odd'] != 'mixed' and k_['krein_sign_even'] != k_['krein_sign_odd'] for k_ in krein)
    rep.check('U8_mirror_R1', ok8, 'the mirror R_1 chi(sigma) = T0 T1 T2 T3 chi(-sigma) maps the eight resonances onto themselves: four '
              'even and four odd, the even ones of one Krein sign and the odd ones of the other: %s' % [
                  (k_['R1_even'], k_['R1_odd'], k_['krein_sign_even'], k_['krein_sign_odd']) for k_ in krein])
    return write('spectra', 'um4_spectra.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
