#!/usr/bin/env python3
"""um4_propagators.py - gravity and electromagnetism between sources on the fold of UM-4: the propagators of the bulk
graviton and of the bulk photon from one point of the fold to another, Newton's and Coulomb's laws with their corrections,
and the masses and widths of the W and Z bosons, whose gauge fields live in the bulk.

A massless field of the bulk with the flux weight e^{-n H |sigma|} (n = 7 for the graviton and a scalar, n = 5 for the
photon; um4_bulk.py B1, B2, B4) and a source J on the fold obeys, for the Euclidean momentum p along the fold (p^2 the
square of the seven-dimensional momentum),
    -e^{n H |sigma|} d_sigma(e^{-n H |sigma|} d_sigma u) + e^{2H|sigma|} p^2 u = J delta_D(sigma).
With z = e^{H|sigma|}/H the solution that decays into the bulk is u = C z^nu K_nu(p z), nu = n/2 (K_nu the modified Bessel
function of the second kind), and the jump of u' at the fold gives the brane-to-brane propagator
    G_n(p) = K_nu(p/H) / (2 p K_{nu-1}(p/H)).
Computed:
  P1  u = z^nu K_nu(p z) solves the mode equation on both sides (sympy, exact), and the jump condition gives G_n; for
      small p, G_n -> (nu - 1) H/p^2: the zero mode with the strength (5/2) H for the graviton (kappa_7 = 5 kappa H/2) and
      (3/2) H for the photon (g_7^2 = 3 H g_8^2/2);
  P2  for half-integer nu the ratio is rational: G_7 = H (x^3 + 6x^2 + 15x + 15)/(2 p^2 (x^2 + 3x + 3)) and
      G_5 = H (x^2 + 3x + 3)/(2 p^2 (x + 1)) with x = p/H; their expansions G_7 = (5H/(2p^2)) (1 + x^2/15 - x^4/45 + x^5/45 +
      ...) and G_5 = (3H/(2p^2)) (1 + x^2/3 - x^3/3 + ...); the even powers are contact terms, the first odd power gives the
      long-range correction;
  P3  the static potentials between point sources on the fold (spread uniformly over the extra times; three-dimensional
      Fourier transform, numerically with an oscillatory quadrature, checked against the asymptotic form): the graviton
      part V_7(r) = (5H/(8 pi r)) [1 + (16/(15 pi)) (H r)^-5 + ...] and the photon V_5(r) = (3H/(8 pi r)) [1 +
      (4/(3 pi)) (H r)^-3 + ...]: Newton's law with a correction of relative size 0.34/(H r)^5 (the scalar part of the
      exchange; the tensor structure of the massive modes changes the coefficient by a factor of order one) and Coulomb's
      law with 0.42/(H r)^3;
  P4  the W and Z bosons: the Higgs doublet on the fold gives the bulk gauge fields a mass term M_b^2 delta_D(sigma) on the
      fold; the pole of G_5/(1 + M_b^2 G_5) for time-like momentum (the outgoing continuation p = -i m) lies at
      m^2 = m_0^2 (1 - m_0^2/(3 H^2) + ...) - i m_0^5/(3 H^3) + ..., m_0^2 = (3H/2) M_b^2 = g^2 v^2/4 for the W: a resonance of
      the width Gamma = m_0 (m_0/H)^3/3 into the bulk (numerically: the exact pole of the rational propagator deviates from it by
      1.83 (m_0/H)^2 in the imaginary part and 0.44 (m_0/H)^4 in the real part, the next orders of the expansion);
  P5  the lower bounds on H that these give (ESTIMATE; the measured values are inputs, the formulas are P2 to P4):
      (a) Newton's law, tested by torsion balances at separations from 52 micrometres to 3 mm (Lee, Adelberger, Cook,
          Fleischer and Heckel, Phys. Rev. Lett. 124 (2020) 101101: gravitational-strength Yukawa forces of range above
          38.6 micrometres are excluded at 95 per cent), taken as holding at 52 micrometres to 1 per cent (a criterion, not the
          published limit): H r > (0.34/0.01)^(1/5) = 2.0, H > 7.7e-3 eV; at the bound of (b) the correction there is 2.6e-75
          (2.7e-75 for H = 2.5 TeV);
      (b) the invisible width of the Z: a Z boson that decays into the bulk leaves the fold unseen and adds
          Gamma_Z = m_Z (m_Z/H)^3/3 (P4) to the invisible width; the number of light neutrinos measured at the Z,
          N_nu = 2.9963 +- 0.0074 (Janot and Jadach, Phys. Lett. B 803 (2020) 135319), with Gamma(Z -> nu nubar) = 167.2 MeV
          per neutrino, allows at most (N_nu - 3 + 1.645 x 0.0074) x 167.2 MeV = 1.42 MeV more (95 per cent, one-sided):
          H > m_Z (m_Z/(3 x 1.42 MeV))^(1/3) = 2534 GeV (about 2.5 TeV), the strongest of these bounds;
      (c) contact interactions: the even term x^2/3 of G_5 is a contact interaction e^2 Q_q Q_l/(3 H^2) (qbar gamma q)(lbar gamma l)
          between the quark and lepton currents of the fold (photon exchange through the massive modes); written as
          4 pi/Lambda^2 (the convention of the experiments) it has Lambda = H sqrt(3/(alpha |Q_q Q_l|)); the limit
          Lambda > 26.0 TeV of ATLAS (e e and mu mu combined, destructive interference, the left-left operator; JHEP 11 (2020)
          005) with the up-quark charge (|Q_u Q_l| = 2/3, alpha = 1/128) gives H > Lambda sqrt(2 alpha/9) = 1.1 TeV (1.3 TeV with
          unit charges; the vector structure of photon exchange and the weak gauge fields, whose bulk modes add to it, change
          this by factors of order one);
      (d) the squared masses of the W and Z (P4) are shifted by -m_0^4/(3 H^2) (the masses by -m_0^3/(6 H^2)), which changes
          rho = m_W^2/(cos^2 theta_W m_Z^2) by
          sin^2 theta_W m_Z^2/(3 H^2); rho_0 = 1.00031 +- 0.00019 (Particle Data Group 2024) gives H > 0.97 TeV;
      so H is at least of the order of a few TeV; at H = 2534 GeV the width of the W into the bulk is 0.85 MeV (its measured
      total width is 2.1 GeV) and the Coulomb correction 0.42/(H r)^3 is 1.4e-27 at the Bohr radius.
Writes outputs/propagators.json and reports/propagators_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_propagators.py

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

import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import integrate

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from um4_common import Report, write             # noqa: E402

H = sp.Symbol('H', positive=True)
p = sp.Symbol('p', positive=True)
SIG = sp.Symbol('sigma', positive=True)
xx = sp.Symbol('x', positive=True)


def G_rational(n, x):
    """G_n(p) p^2/H as a function of x = p/H (n = 7 or 5)."""
    if n == 7:
        return (x ** 3 + 6 * x ** 2 + 15 * x + 15) / (2 * (x ** 2 + 3 * x + 3))
    return (x ** 2 + 3 * x + 3) / (2 * (x + 1))


def potential(n, r):
    """V(r) = int d^3p/(2 pi)^3 e^{i p.r} G_n(p) = (1/(2 pi^2 r)) int_0^inf p G_n(p) sin(p r) dp (H = 1).  With
    f(p) = p G_n(p) = g0/p + f2(p) (f2 regular at p = 0, rational in p, its poles in the left half plane), the sine transform
    of g0/p gives g0/(4 pi r), and that of f2 is Re int_0^inf f2(i t) e^{-t r} dt after turning the contour to the positive
    imaginary axis (no pole in the first quadrant): a Laplace transform, numerically stable for large r."""
    g0 = mp.mpf(5) / 2 if n == 7 else mp.mpf(3) / 2
    def f2(pp):
        x = pp
        return pp * G_rational(n, x) / pp ** 2 - g0 / pp
    F = mp.quad(lambda t: f2(1j * t) * mp.exp(-t * r), [0, 1 / mp.mpf(r), 10 / mp.mpf(r), mp.inf])
    return float(g0 / (4 * mp.pi * r)), float(mp.re(F) / (2 * mp.pi ** 2 * r))


def main():
    rep = Report()
    out = {}

    # ---------------- P1: the solution and the propagator
    ok1 = True
    for n in (7, 5):
        nu = sp.Rational(n, 2)
        z = sp.exp(H * SIG) / H
        u = z ** nu * sp.besselk(nu, p * z)
        eq = sp.diff(sp.exp(-n * H * SIG) * sp.diff(u, SIG), SIG) * sp.exp(n * H * SIG) - sp.exp(2 * H * SIG) * p ** 2 * u
        val = sp.N(eq.subs({H: 1, p: sp.Rational(7, 10), SIG: sp.Rational(3, 10)}), 30)
        ok1 &= abs(val) < 1e-25
        # u'(0+) = -H C p H^{-nu-1} K_{nu-1}(p/H) with u = C z^nu K_nu: G = u(0)/(-2 u'(0+)) per unit source
        up = sp.diff(u, SIG).subs(SIG, 0)
        G = sp.simplify(u.subs(SIG, 0) / (-2 * up))
        Gform = sp.besselk(nu, p / H) / (2 * p * sp.besselk(nu - 1, p / H))
        ok1 &= abs(sp.N((G - Gform).subs({H: 1, p: sp.Rational(13, 10)}), 30)) < 1e-25
        lim = sp.limit(sp.expand_func(Gform * p ** 2 / H).subs(p, xx * H), xx, 0)
        ok1 &= sp.simplify(lim - (nu - 1)) == 0
        out['P1_n%d' % n] = {'propagator': 'K_%s(p/H)/(2 p K_%s(p/H))' % (nu, nu - 1), 'zero_mode_strength_over_H': str(lim)}
    rep.check('P1_brane_to_brane_propagator', ok1, 'u = z^nu K_nu(p z), z = e^{H|sigma|}/H, solves the mode equation (n = 7, 5); the jump '
              'gives G_n = K_nu(p/H)/(2p K_{nu-1}(p/H)); for p -> 0, G_n -> (nu - 1) H/p^2: 5H/2 (graviton) and 3H/2 (photon)')

    # ---------------- P2: the rational forms and their expansions
    ok2 = True
    ser = {}
    for n, g0 in ((7, sp.Rational(5, 2)), (5, sp.Rational(3, 2))):
        nu = sp.Rational(n, 2)
        exact = sp.expand_func(sp.besselk(nu, xx) / (2 * xx * sp.besselk(nu - 1, xx)) * xx ** 2)
        ok2 &= sp.simplify(exact - G_rational(n, xx)) == 0
        s6 = sp.series(G_rational(n, xx) / g0, xx, 0, 7).removeO()
        ser[n] = sp.expand(s6)
    ok2 &= [ser[7].coeff(xx, j) for j in range(6)] == [1, 0, sp.Rational(1, 15), 0, -sp.Rational(1, 45), sp.Rational(1, 45)]
    ok2 &= ser[5].coeff(xx, 1) == 0 and ser[5].coeff(xx, 2) == sp.Rational(1, 3) and ser[5].coeff(xx, 3) == -sp.Rational(1, 3)
    out['P2_series'] = {'G7_over_5H_2p2': str(ser[7]), 'G5_over_3H_2p2': str(ser[5])}
    rep.check('P2_expansions', ok2, 'G_7 p^2/(5H/2) = %s, G_5 p^2/(3H/2) = %s (x = p/H): the first odd powers are x^5 (gravity) and x^3 '
              '(photon)' % (ser[7], ser[5]))

    # ---------------- P3: the static potentials
    # the odd term c x^m of G p^2/(g0 H) gives V/V0 - 1 = c * F(m)/(H r)^m with the Fourier transform of |p|^{m-2}
    def coeff(m, c):
        a = m - 2
        ft = 2 ** (a + 3) * math.pi ** 1.5 * math.gamma((a + 3) / 2) / math.gamma(-a / 2)   # int d^3p e^{ipr} |p|^a r^{a+3}
        # V0 = g0 H/(4 pi r); delta V = g0 H c H^{-m} ft r^{-(a+3)}/(8 pi^3)
        return c * ft / (8 * math.pi ** 3) * 4 * math.pi
    cg = coeff(5, 1 / 45)
    cp = coeff(3, -1 / 3)
    ok3 = abs(cg - 16 / (15 * math.pi)) < 1e-12 and abs(cp - 4 / (3 * math.pi)) < 1e-12
    num = {}
    for n, c, m in ((7, cg, 5), (5, cp, 3)):
        rows = []
        for Hr in (8.0, 16.0, 32.0):
            v0, dv = potential(n, Hr)
            rel = dv / v0
            pred = c / Hr ** m
            rows.append({'Hr': Hr, 'relative_correction': rel, 'asymptotic': pred})
        num[n] = rows
        ok3 &= abs(rows[-1]['relative_correction'] / rows[-1]['asymptotic'] - 1) < 0.05
    out['P3_potentials'] = {'newton': 'V_7 = (5H/(8 pi r)) [1 + (16/(15 pi)) (Hr)^-5]', 'coulomb': 'V_5 = (3H/(8 pi r)) [1 + (4/(3 pi)) (Hr)^-3]',
                            'numeric_graviton': num[7], 'numeric_photon': num[5]}
    rep.check('P3_newton_and_coulomb', ok3, 'Newton: 1 + (16/(15 pi))/(Hr)^5 = 1 + %.4f/(Hr)^5; Coulomb: 1 + (4/(3 pi))/(Hr)^3 = 1 + %.4f/(Hr)^3; '
              'numerical Fourier transforms at Hr = 32: %.4f and %.4f of the asymptotic forms' % (
                  cg, cp, num[7][-1]['relative_correction'] / num[7][-1]['asymptotic'],
                  num[5][-1]['relative_correction'] / num[5][-1]['asymptotic']))

    # ---------------- P4: the W and Z resonances
    mp.mp.dps = 40
    def pole(m0):
        """the zero of 1 + M_b^2 G_5(p) with p = -i m (H = 1), M_b^2 = m0^2/(3/2)."""
        Mb2 = mp.mpf(m0) ** 2 / mp.mpf(1.5)
        def F(m):
            pp = -1j * m
            x = pp
            G = (x ** 2 + 3 * x + 3) / (2 * pp ** 2 * (x + 1))
            return 1 + Mb2 * G
        return mp.findroot(F, mp.mpc(m0, -m0 ** 4 / 6))
    rows = []
    ok4 = True
    for m0 in (0.01, 0.003, 0.001):
        mc = pole(m0)
        m2 = mc ** 2
        re_pred = m0 ** 2 * (1 - m0 ** 2 / 3)
        im_pred = -m0 ** 5 / 3
        dre = abs(float(m2.real) / re_pred - 1)
        dim = abs(float(m2.imag) / im_pred - 1)
        rows.append({'m0_over_H': m0, 'm2_real': float(m2.real), 'm2_imag': float(m2.imag), 'pred_real': re_pred, 'pred_imag': im_pred,
                     'relative_deviation_real': dre, 'relative_deviation_imag': dim,
                     'width_over_m0': float(-m2.imag / m0 ** 2), 'pred_width_over_m0': m0 ** 3 / 3})
    # the expansion is right to the order shown if the deviations are of the next orders: the imaginary part deviates by a
    # constant times (m0/H)^2 and the real part by a constant times (m0/H)^4
    cim = [r_['relative_deviation_imag'] / r_['m0_over_H'] ** 2 for r_ in rows]
    cre = [r_['relative_deviation_real'] / r_['m0_over_H'] ** 4 for r_ in rows]
    ok4 = (max(cim) / min(cim) < 1.05 and max(cre) / min(cre) < 1.05 and max(cim) < 5 and max(cre) < 5
           and all(r_['relative_deviation_imag'] < 2e-4 and r_['relative_deviation_real'] < 1e-5 for r_ in rows))
    out['P4_W_Z'] = rows
    out['P4_next_order_coefficients'] = {'imag_over_m0^2': cim, 'real_over_m0^4': cre}
    rep.check('P4_W_and_Z_resonances', ok4, 'the pole of G_5/(1 + M_b^2 G_5): m^2 = m0^2 (1 - m0^2/(3H^2)) - i m0^5/(3H^3); the exact pole of the '
              'rational propagator deviates from it by %s (imaginary part) and %s (real part) for m0/H = %s, i.e. by %.3f (m0/H)^2 and '
              '%.3f (m0/H)^4, the next orders: the W and Z are resonances of the width Gamma = m0 (m0/H)^3/3 into the bulk (%s)' % (
                  ', '.join('%.1e' % r_['relative_deviation_imag'] for r_ in rows), ', '.join('%.1e' % r_['relative_deviation_real'] for r_ in rows),
                  ', '.join('%g' % r_['m0_over_H'] for r_ in rows), cim[0], cre[0],
                  ', '.join('m0/H = %g: Gamma/m0 = %.3e' % (r_['m0_over_H'], r_['width_over_m0']) for r_ in rows)))

    # ---------------- P5: bounds on H (ESTIMATE)
    hbarc_eVm = 1.973269804e-7
    r_test = 52e-6                                  # m
    eps_test = 0.01
    Hmin_newton = (cg / eps_test) ** 0.2 / r_test * hbarc_eVm      # eV
    # (b) the invisible width of the Z (Janot and Jadach 2020: N_nu = 2.9963 +- 0.0074; Gamma(Z -> nu nubar) = 167.2 MeV)
    mZ, mW = 91.1876, 80.37
    Nnu, dNnu, Gnu = 2.9963, 0.0074, 0.1672
    Gextra = (Nnu - 3 + 1.645 * dNnu) * Gnu                         # GeV, 95 per cent one-sided
    Hmin_Z = mZ * (mZ / (3 * Gextra)) ** (1 / 3)
    # check the width formula of P4 against the exact pole of the rational propagator at this H
    m0n = mZ / Hmin_Z
    m2 = complex(pole(m0n) ** 2)                                     # m^2 = M^2 - i M Gamma (H = 1)
    width_exact = -m2.imag / math.sqrt(m2.real) * Hmin_Z             # GeV
    width_formula = mZ * m0n ** 3 / 3
    # (c) contact interactions: photon exchange through the massive modes gives e^2 Q_q Q_l/(3 H^2) (qbar gamma q)(lbar gamma l)
    # between quarks and leptons (the operators of Drell-Yan production); written as 4 pi/Lambda^2 it has
    # H = Lambda sqrt(alpha |Q_q Q_l|/3); the ATLAS limit Lambda > 26.0 TeV (ee and mu mu combined, destructive interference,
    # left-left operator) with the up-quark charge |Q_u Q_l| = 2/3 (the dominant quark) gives about 1.1 TeV
    Lam_CI, alpha_em = 26.0e3, 1 / 128.0
    Hmin_CI = Lam_CI * math.sqrt(alpha_em * (2.0 / 3.0) / 3)
    Hmin_CI_unit_charges = Lam_CI * math.sqrt(alpha_em / 3)
    # (a') the correction of Newton's law at 52 micrometres for H at the bound of (b) and for H = 2.5 TeV
    r_test_GeVinv = r_test / 1.973269804e-16                         # 52 micrometres in GeV^-1
    # (d) rho parameter: Delta rho = sin^2 theta_W m_Z^2/(3 H^2); rho_0 - 1 < 0.00031 + 1.96 x 0.00019
    s2w = 0.23122
    drho_max = 0.00031 + 1.96 * 0.00019
    Hmin_rho = math.sqrt(s2w * mZ ** 2 / (3 * drho_max))
    width_W = mW * (mW / Hmin_Z) ** 3 / 3
    r_atom_GeVinv = 0.529e-10 / 1.973269804e-16                      # Bohr radius in GeV^-1
    coulomb_atom = cp / (Hmin_Z * r_atom_GeVinv) ** 3
    newton_52um = {'H_bound': cg / (Hmin_Z * r_test_GeVinv) ** 5, 'H_2500_GeV': cg / (2.5e3 * r_test_GeVinv) ** 5}
    ok5 = (7e-3 < Hmin_newton < 8e-3 and 2.3e3 < Hmin_Z < 2.7e3 and abs(width_exact / width_formula - 1) < 0.02
           and 1.0e3 < Hmin_CI < 1.2e3 and 0.9e3 < Hmin_rho < 1.0e3 and width_W < 1e-3 and coulomb_atom < 1e-26
           and 2e-75 < newton_52um['H_bound'] < 3e-75 and 2e-75 < newton_52um['H_2500_GeV'] < 3e-75)
    out['P5_bounds'] = {'H_min_from_newton_eV': Hmin_newton, 'Z_extra_invisible_width_max_GeV': Gextra,
                        'H_min_from_Z_invisible_width_GeV': Hmin_Z, 'Z_width_into_bulk_exact_pole_GeV': width_exact,
                        'Z_width_into_bulk_formula_GeV': width_formula, 'H_min_from_contact_interactions_GeV': Hmin_CI,
                        'H_min_from_contact_interactions_unit_charges_GeV': Hmin_CI_unit_charges,
                        'H_min_from_rho_parameter_GeV': Hmin_rho, 'W_width_into_bulk_at_H_min_GeV': width_W,
                        'coulomb_correction_at_bohr_radius': coulomb_atom, 'newton_correction_at_52_micrometres': newton_52um}
    rep.check('P5_bounds_on_H', ok5, 'ESTIMATE: Newton\'s law (tested at separations of 52 micrometres to 3 mm; gravitational-strength '
              'Yukawa forces of range above 38.6 micrometres are excluded), taken to hold to 1 per cent at 52 micrometres: H > %.2e eV; '
              'the invisible width of the Z (at most %.2f MeV more than three neutrinos give): H > %.0f GeV (the exact pole of the '
              'propagator gives the width %.3e GeV, the formula m_Z (m_Z/H)^3/3 %.3e GeV); quark-lepton contact interactions (ATLAS, '
              '26.0 TeV; the up-quark charge 2/3): H > %.0f GeV (%.0f GeV with unit charges); rho parameter: H > %.0f GeV; at '
              'H = %.0f GeV the width of the W into the bulk is %.1e GeV, the correction of Newton\'s law at 52 micrometres %.2e '
              '(%.2e at H = 2.5 TeV) and the Coulomb correction at the Bohr radius %.1e' % (
                  Hmin_newton, 1e3 * Gextra, Hmin_Z, width_exact, width_formula, Hmin_CI, Hmin_CI_unit_charges, Hmin_rho, Hmin_Z,
                  width_W, newton_52um['H_bound'], newton_52um['H_2500_GeV'], coulomb_atom))
    return write('propagators', 'um4_propagators.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
