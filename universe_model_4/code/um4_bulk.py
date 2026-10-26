#!/usr/bin/env python3
"""um4_bulk.py - fields that propagate in the bulk of UM-4: photons, gravitons, scalars and fermions travel at the speed of
light (the author's order of 2026-10-25, 13:15 PDT: "both photons and gravitons actually propagate at c in the bulk,
photon waves are transverse spin-1 phenomena, gravitational waves ... spin-2 ... plus and cross polarization modes").

The static block of UM-4, d sigma^2 + e^{-2H|sigma|} (dx_i^2 - dx4^2 - dx_r^2) (a4 = 0, b4 = 1 by the choice of units), has on
every slice sigma = const the light cone of the fold (um4_geometry.py G8), and the factor e^{-2H|sigma|} multiplies the whole
metric of the fold: every field of the bulk separates into a profile along sigma times a field of the fold whose equation is
the Lorentz-invariant equation of seven dimensions with a mass m (its value set by the profile).  Then omega^2 = k^2 + m^2 for
every mode: the massless modes (the zero modes) travel at the speed of light at every wavelength, the massive modes are
slower.  Computed:
  B1  a massless scalar of the bulk: with phi = u(sigma) e^{i (k x3 - omega x4)} the wave operator of the metric of the
      static block (computed from its components and sqrt|g| = e^{-7H|sigma|}) gives
      u'' - 7 H sgn(sigma) u' + e^{2H|sigma|} (omega^2 - k^2) u = 0: omega and k enter only through omega^2 - k^2 because the
      warp multiplies dx3^2 and dx4^2 alike; the zero mode u = 1 is normalisable (weight e^{-5H|sigma|}, norm 2/(5H)) and has
      omega = k exactly (the box of B9 inherits this property and reproduces it; UM-3: omega^2 = (3/2) k^2, 1.22 times the
      speed of light);
  B2  the Maxwell field of the bulk (the photon, IN-7 of UM-4: the gauge fields live in the bulk): Maxwell's equations
      computed from the metric of the static block for A_1 = u(sigma) e^{i (k x3 - omega x4)}, A_sigma = 0, give
      u'' - 5 H sgn(sigma) u' + e^{2H|sigma|} (omega^2 - k^2) u = 0 (the other components vanish identically); the zero mode
      u = 1 is normalisable (the kinetic weight e^{-3H|sigma|}, norm 2/(3H)): a massless photon of seven dimensions bound to
      the fold, with the coupling g_7^2 = (3/2) H g_8^2, omega = k exactly; a component A_sigma has no normalisable zero mode
      (its profile would be e^{5H|sigma|}) (UM-3: omega^2 = 2 k^2);
  B3  the photon as a wave: for the zero mode the field equation of the fold d_a F^{ab} = 0 with a plane wave A_mu =
      epsilon_mu e^{i k (x3 - x4)} (Lorenz gauge, fields of the four observable coordinates) leaves the two transverse
      polarisations epsilon = (1, 0, 0, 0) and (0, 1, 0, 0) along x1 and x2 as the only physical ones (the longitudinal and
      the time-like polarisation are pure gauge); under a rotation by the angle theta about the direction of motion the
      circular polarisations (1, +-i)/sqrt 2 pick up e^{-+i theta}: helicity +-1, a transverse spin-1 wave; its electric and
      magnetic fields are orthogonal to each other and to the direction of motion and equal in size;
  B4  the graviton of the bulk (Einstein gravity, um4_gravity.py L2 with P'(1) = 21): the + polarisation obeys
      (1/2)[e^{2H|sigma|} (h_tt - h_33) - h_ss + 7 H sgn(sigma) h_s] = 0, the equation of the massless scalar B1: the zero mode
      h = h(x3 - x4) (any profile along the fold, independent of sigma) solves the bulk equation and the junction condition
      (no jump of its sigma-derivative): the graviton of seven dimensions bound to the fold, with the coupling kappa_7 =
      (5/2) kappa H (um4_fold.py F2), at the speed of light;
  B5  the gravitational wave as seen in four dimensions: the transverse traceless zero mode h_ij (i, j = 1, 2, 3) of a wave
      along x3 has the two polarisations h_+ (h_11 = -h_22) and h_x (h_12 = h_21); a ring of free test masses in the plane
      x1, x2 is stretched along x1 and squeezed along x2 by h_+ (the relative change of the distance at the angle phi is
      (1/2) h_+ cos 2 phi) and along the diagonals by h_x ((1/2) h_x sin 2 phi); under a rotation by theta about x3,
      (h_+, h_x) rotate by 2 theta: helicity +-2, a spin-2 wave; the energy-momentum tensor of a field of the fold that does
      not depend on the extra times, computed from its Lagrangian (a scalar with any potential), has T_{mu r} = 0 and
      T_{rs} = ghat_rs L: the other components of the seven-dimensional zero mode (B11) are not sourced at the linear order,
      except the trace of h_{rs} (the volume of the extra times), which the fold fluid holds fixed: the gravitational waves
      that the matter of the fold emits have only the + and x polarisations;
  B6  a fermion of the bulk with a kink mass M sgn(sigma): with Psi = e^{(7/2)H|sigma|} chi the zero mode is chi =
      e^{-M|sigma|} chi_0 with T^(sigma) chi_0 = -chi_0 and Dhat chi_0 = 0, normalisable for M > H/2 (the density
      e^{(H - 2M)|sigma|}, the norm 2/(3H) at M = 2H over both sides): a massless fermion of seven dimensions at the speed of
      light (UM-3: 2M/(2M - H) times it);
  B7  dirac16complex (the author's field, mass m_Psi, the portal terms at the fold): its bulk equation
      T^(sigma) chi' + e^{H|sigma|} (-i omega T^(x4) + i k T^(x3)) chi - m_Psi chi = 0 is invariant under the boost of the
      fold generated by T^(x3) T^(x4)/2, which commutes with T^(sigma) and with the chirality T16^8, so with the portal terms
      of the fold (checked with the author's matrices), and turns
      (omega, k) into (omega cosh beta - k sinh beta, k cosh beta - omega sinh beta): every state of dirac16complex at the
      fold has omega^2 = k^2 + M^2 with its mass M, and its group velocity k/omega is below the speed of light (UM-3: up to
      1.0046);
  B9  the UM-3 speeds recomputed: on the static block of UM-3, d sigma^2 + e^{-2H|sigma|} (dx_i^2 - dx_r^2) - dx4^2 (the time
      not warped), a massless scalar phi = u(sigma) e^{i (k x3 - omega x4)} obeys u'' - 6 H sgn(sigma) u' + (omega^2 -
      e^{2H|sigma|} k^2) u = 0 (checked with sympy on both halves): omega and k no longer appear only through omega^2 - k^2;
      for k << H the lowest mode has u = 1 and omega^2/k^2 = int e^{-4H|sigma|}/int e^{-6H|sigma|} = 3/2, for the photon
      (the polarisation along x1) int e^{-2H|sigma|}/int e^{-4H|sigma|} = 2 (exact); the box gives omega^2/k^2 for k = 0.01 H
      to 3 H (scalar 1.4999 to 1.38, photon 1.9995 to 1.51: faster than light at every wavelength); the same box gives 1 for
      the metric of UM-4, the exact result of B1 and B2 (a test of the box, not of UM-4); the speeds in units of the speed
      of light of the fold are summarised in the output (every massless field of the bulk 1, every massive mode below 1;
      UM-3: scalar 1.2247, photon 1.4142);
  B10 the massive modes of the massless fields of the bulk (the "x0 masses" that the fold sees): with the warped distance
      zeta = e^{H|sigma|}/H the profile equation u'' - n H sgn(sigma) u' + e^{2H|sigma|} m^2 u = 0 (n = 7 for a scalar and each
      polarisation of the graviton, n = 5 for a gauge field) has the exact solutions zeta^{n/2} J_{n/2}(m zeta) and
      zeta^{n/2} Y_{n/2}(m zeta) on both halves (checked with sympy for the half-integer orders), d/d zeta (zeta^nu Z_nu(m zeta))
      = m zeta^nu Z_{nu-1}(m zeta), and the kinetic weight e^{-(n-2)H|sigma|} d sigma is H^{-(n-1)} zeta^{1-n} d zeta, so the
      modes are normalised by the Hankel transform: every m > 0 is in the spectrum (a continuum from zero mass, no gap); the
      even mode with u' = 0 at the fold is zeta^{n/2} (Y_{n/2-1}(m/H) J_{n/2}(m zeta) - J_{n/2-1}(m/H) Y_{n/2}(m zeta)), and its
      density at the fold is s_n(m) = 2H/(pi^2 m (J_{n/2-1}(m/H)^2 + Y_{n/2-1}(m/H)^2)) (from the Wronskian); the spectral
      representation G_n(p) = (n - 2)H/(2 p^2) + int_0^inf dm s_n(m)/(p^2 + m^2) reproduces the propagator of
      um4_propagators.py P1, K_{n/2}(p/H)/(2 p K_{n/2-1}(p/H)), to 1e-12 at p/H = 0.3, 1, 3; s_7 -> (m/H)^4/(9 pi) and
      s_5 -> (m/H)^2/pi for m << H, s_n -> 1/pi for m >> H; and the long-range parts of the static potentials,
      (2/((n - 2)H)) int_0^inf dm s_n(m) e^{-m r}, approach 16/(15 pi (Hr)^5) and 4/(3 pi (Hr)^3) (P3);
  B11 the polarisations of the graviton bound to the fold and the signs of their kinetic terms: the massless graviton of
      the seven-dimensional fold has 14 physical polarisations (the transverse traceless h for a null wave vector, 20, less
      the 6 residual gauge modes, by linear algebra), the graviton h_{mu nu} (2), three vectors h_{mu r} (6) and six scalars
      h_{rs} (6); the second-order Einstein-Hilbert density sqrt|g| R of eta + eps h on the flat fold of signature (3, 4),
      averaged over the phase of a wave A cos(omega x4 - k x1), is C (omega^2 - k^2) A^2 with C = 1/4 for the graviton
      (h_23, h_22 = -h_33) and the scalars (h_56, h_55 = -h_66) and C = -1/4 for the vectors (h_25, h_37): the vectors with
      one index along ordinary space and one along an extra time have kinetic terms of the wrong sign (ghosts), as the
      component A_5 of a gauge field (-(1/4) F_AB F^AB: healthy for A_2, ghost for A_5); the matter of the fold does not emit
      them at the linear order (B5).
Writes outputs/bulk.json and reports/bulk_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_bulk.py

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

import sys
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import sympy as sp
from scipy import integrate as sint
from scipy import special as spc

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM                          # noqa: E402
from um4_common import Report, write             # noqa: E402

H = sp.Symbol('H', positive=True)
SIG = sp.Symbol('sigma', real=True)
k, w, m, M = sp.symbols('k omega m M', positive=True)
x1, x2, x3, x4 = sp.symbols('x1:5', real=True)


Y567 = sp.symbols('x5:8', real=True)
XB = [SIG, x1, x2, x3, x4] + list(Y567)
EPSB = [1, 1, 1, 1, -1, -1, -1, -1]


def static_metric(side):
    """The diagonal components of the static block d sigma^2 + e^{-2H|sigma|}(dx_i^2 - dx4^2 - dx_r^2) on the side sigma > 0
    (side = +1) or sigma < 0 (side = -1), and sqrt|g| from them."""
    W = sp.exp(-2 * H * side * SIG)
    g = [sp.S(1)] + [W] * 3 + [-W] * 4
    sqg = sp.sqrt(sp.Mul(*[EPSB[i] * g[i] for i in range(8)]))
    return g, sp.simplify(sp.powsimp(sqg, force=True))


def eh_quadratic_average(pattern, Xf, etaf):
    """The second-order part of the Einstein-Hilbert density sqrt|g| R of the metric g = eta + eps h on the flat fold (signature
    (3, 4)), h = pattern f(x4, x1) with a symmetric numerical pattern, for f = A cos(omega x4 - k x1), averaged over the phase
    (total derivatives drop out): C (omega^2 - k^2) A^2, C > 0 for a healthy wave, C < 0 for a ghost."""
    eps_ = sp.Symbol('epsilon')
    om_, kk_, A_ = sp.symbols('omega_w k_w A_w', positive=True)
    th_ = sp.Symbol('theta_w', real=True)
    n = len(Xf)
    f = sp.Function('f')(Xf[3], Xf[0])
    h = sp.Matrix(pattern) * f
    g = etaf + eps_ * h
    ei = etaf.inv()
    gi = ei - eps_ * ei * h * ei + eps_ ** 2 * ei * h * ei * h * ei                     # the inverse to the second order
    Gam = [[[sp.expand(sum(gi[l, m_] * (sp.diff(g[m_, i], Xf[j]) + sp.diff(g[m_, j], Xf[i]) - sp.diff(g[i, j], Xf[m_])) / 2
                           for m_ in range(n) if gi[l, m_] != 0)) for j in range(n)] for i in range(n)] for l in range(n)]
    Ric = sp.zeros(n, n)
    for i in range(n):
        for k_ in range(n):
            v = 0
            for l in range(n):
                v += sp.diff(Gam[l][i][k_], Xf[l]) - sp.diff(Gam[l][i][l], Xf[k_])
                for m_ in range(n):
                    v += Gam[l][l][m_] * Gam[m_][i][k_] - Gam[l][k_][m_] * Gam[m_][i][l]
            Ric[i, k_] = v
    R = sum(gi[i, k_] * Ric[i, k_] for i in range(n) for k_ in range(n))
    lnd = sp.log(g.det())
    D1 = sp.diff(lnd, eps_).subs(eps_, 0)
    D2 = sp.diff(lnd, eps_, 2).subs(eps_, 0)
    sq = 1 + eps_ * D1 / 2 + eps_ ** 2 * (D2 / 4 + D1 ** 2 / 8)                         # sqrt(det g/det eta)
    L2 = sp.expand(sq * R).coeff(eps_, 2)
    fs = A_ * sp.cos(th_)
    L2s = L2.subs({sp.Derivative(f, Xf[3], 2): -om_ ** 2 * fs, sp.Derivative(f, Xf[0], 2): -kk_ ** 2 * fs,
                   sp.Derivative(f, Xf[3], Xf[0]): om_ * kk_ * fs, sp.Derivative(f, Xf[0], Xf[3]): om_ * kk_ * fs,
                   sp.Derivative(f, Xf[3]): -om_ * A_ * sp.sin(th_), sp.Derivative(f, Xf[0]): kk_ * A_ * sp.sin(th_)}).subs(f, fs)
    avg = sp.simplify(sp.integrate(L2s, (th_, 0, 2 * sp.pi)) / (2 * sp.pi))
    C = sp.simplify(avg / ((om_ ** 2 - kk_ ** 2) * A_ ** 2))
    return C, sp.factor(avg)


def box_lowest(nw, kvals, L=6.0, N=1600):
    """The lowest omega^2 of -(1/rho) d/ds(p du/ds) + k^2 u = omega^2 u on |s| < L (H = 1), p = e^{-nw |s|} the flux weight,
    rho = e^{-(nw - 2)|s|} the kinetic weight (u' = 0 at the ends), as a symmetric generalised eigenvalue problem."""
    s = np.linspace(-L, L, N + 1)
    hstep = s[1] - s[0]
    mid = 0.5 * (s[1:] + s[:-1])
    p = np.exp(-nw * np.abs(mid))
    rho = np.exp(-(nw - 2) * np.abs(s))
    A = np.zeros((N + 1, N + 1))
    for i in range(N):
        A[i, i] += p[i] / hstep ** 2
        A[i + 1, i + 1] += p[i] / hstep ** 2
        A[i, i + 1] -= p[i] / hstep ** 2
        A[i + 1, i] -= p[i] / hstep ** 2
    # trapezoidal mass matrix
    wts = np.full(N + 1, hstep)
    wts[0] = wts[-1] = hstep / 2
    A = A * hstep                      # the stiffness with the same quadrature
    Bm = np.diag(rho * wts)
    out = []
    for kk in kvals:
        ev = sla.eigh(A + kk ** 2 * Bm, Bm, eigvals_only=True, subset_by_index=[0, 0])
        out.append(float(ev[0]))
    return out


def box_general(n_flux, n_pot, n_kin, kvals, L=6.0, N=1600):
    """omega^2/k^2 of the lowest mode of -(p u')' + k^2 q u = omega^2 rho u on |s| < L (H = 1; u' = 0 at the ends), with the
    weights p = e^{-n_flux |s|}, q = e^{-n_pot |s|}, rho = e^{-n_kin |s|}: a symmetric generalised eigenvalue problem (the
    stiffness of the piecewise-linear elements, the trapezoidal mass matrices)."""
    s = np.linspace(-L, L, N + 1)
    hstep = s[1] - s[0]
    mid = 0.5 * (s[1:] + s[:-1])
    p = np.exp(-n_flux * np.abs(mid))
    A = np.zeros((N + 1, N + 1))
    for i in range(N):
        A[i, i] += p[i] / hstep
        A[i + 1, i + 1] += p[i] / hstep
        A[i, i + 1] -= p[i] / hstep
        A[i + 1, i] -= p[i] / hstep
    wts = np.full(N + 1, hstep)
    wts[0] = wts[-1] = hstep / 2
    Q = np.diag(np.exp(-n_pot * np.abs(s)) * wts)
    Bm = np.diag(np.exp(-n_kin * np.abs(s)) * wts)
    out = []
    for kk in kvals:
        ev = sla.eigh(A + kk ** 2 * Q, Bm, eigvals_only=True, subset_by_index=[0, 0])
        out.append(float(ev[0]) / kk ** 2)
    return out


def main():
    rep = Report()
    out = {}

    # ---------------- B1: the massless scalar
    u = sp.Function('u')(SIG)
    sgn = sp.Symbol('s', real=True)                    # sgn(sigma) on one side
    side_sub = {}
    ok1 = True
    for s_ in (1, -1):
        gB, sq = static_metric(s_)                      # the metric and sqrt|g| of the static block on this side
        ok1 &= sp.simplify(sq - sp.exp(-7 * H * s_ * SIG)) == 0
        phi = u * sp.exp(sp.I * (k * x3 - w * x4))
        # the wave operator of the metric, (1/sqrt|g|) d_M (sqrt|g| g^MM d_M phi), all eight coordinates
        box = sum(sp.diff(sq / gB[i] * sp.diff(phi, XB[i]), XB[i]) for i in range(8)) / sq
        mode = sp.simplify(box / sp.exp(sp.I * (k * x3 - w * x4)))
        target = sp.diff(u, SIG, 2) - 7 * H * s_ * sp.diff(u, SIG) + sp.exp(2 * H * s_ * SIG) * (w ** 2 - k ** 2) * u
        ok1 &= sp.simplify(mode - target) == 0
    norm_s = sp.integrate(2 * sp.exp(-5 * H * sp.Symbol('t', positive=True)), (sp.Symbol('t', positive=True), 0, sp.oo))
    kv = [0.1, 0.5, 1.0, 2.0]
    lo = box_lowest(7, kv)
    dev1 = max(abs(l_ - kk ** 2) for l_, kk in zip(lo, kv))
    ok1 &= dev1 < 1e-8 and sp.simplify(norm_s - sp.Rational(2, 5) / H) == 0
    out['B1_scalar'] = {'mode_equation': "u'' - 7H sgn(sigma) u' + e^{2H|sigma|}(omega^2 - k^2) u = 0", 'zero_mode_norm': str(norm_s),
                        'box_lowest_omega2': dict(zip([str(x) for x in kv], lo)), 'max_deviation_from_k2': dev1}
    rep.check('B1_bulk_scalar_at_c', ok1, 'the wave operator computed from the metric of the static block (sqrt|g| = e^{-7H|sigma|}) gives the '
              'mode equation u\'\' - 7H sgn u\' + e^{2H|sigma|}(omega^2 - k^2) u = 0 on both sides: omega and k enter only through '
              'omega^2 - k^2, because the warp multiplies dx3^2 and dx4^2 alike; the zero mode u = 1 has the norm %s and omega = k '
              'exactly (the box method of B9, which inherits this property, reproduces it: max |omega^2 - k^2| = %.1e for k = %s H; '
              'UM-3: omega^2 = 1.5 k^2)' % (norm_s, dev1, kv))

    # ---------------- B2: the Maxwell field
    ok2 = True
    for s_ in (1, -1):
        gB, sq = static_metric(s_)
        # Maxwell's equations d_M (sqrt|g| g^MM g^NN F_MN) = 0 computed from the metric for A_1 = u(sigma) e^{i(k x3 - omega x4)}
        # (the polarisation along x1, A_sigma = 0): the component N = 1 is the profile equation, the others vanish
        ph_ = sp.exp(sp.I * (k * x3 - w * x4))
        Avec = [0, u * ph_, 0, 0, 0, 0, 0, 0]
        Fm = [[sp.diff(Avec[N_], XB[M_]) - sp.diff(Avec[M_], XB[N_]) for N_ in range(8)] for M_ in range(8)]
        eqN = [sp.simplify(sum(sp.diff(sq / (gB[M_] * gB[N_]) * Fm[M_][N_], XB[M_]) for M_ in range(8))) for N_ in range(8)]
        ok2 &= all(eqN[N_] == 0 for N_ in range(8) if N_ != 1)
        mode = sp.simplify(eqN[1] / (sq / (gB[0] * gB[1])) / ph_)
        target = sp.diff(u, SIG, 2) - 5 * H * s_ * sp.diff(u, SIG) + sp.exp(2 * H * s_ * SIG) * (w ** 2 - k ** 2) * u
        ok2 &= sp.simplify(mode - target) == 0
        # A_sigma = f(sigma) phihat(x): the equations along the fold need (sqrt|g| g^ss g^aa f)' = 0, f = e^{5H|sigma|}
        f_sig = sp.exp(5 * H * s_ * SIG)
        ok2 &= sp.simplify(sp.diff(sq / (gB[0] * gB[1]) * f_sig, SIG)) == 0
    tq = sp.Symbol('t', positive=True)
    norm_v = sp.integrate(2 * sp.exp(-3 * H * tq), (tq, 0, sp.oo))
    lo2 = box_lowest(5, kv)
    dev2 = max(abs(l_ - kk ** 2) for l_, kk in zip(lo2, kv))
    ok2 &= dev2 < 1e-8 and sp.simplify(norm_v - sp.Rational(2, 3) / H) == 0
    out['B2_photon'] = {'mode_equation': "u'' - 5H sgn(sigma) u' + e^{2H|sigma|} m^2 u = 0", 'zero_mode_norm': str(norm_v),
                        'g7_squared': '(3/2) H g8^2', 'A_sigma_zero_mode_profile': 'e^{5H|sigma|} (not normalisable)',
                        'box_lowest_omega2': dict(zip([str(x) for x in kv], lo2)), 'max_deviation_from_k2': dev2}
    rep.check('B2_bulk_photon_at_c', ok2, 'Maxwell\'s equations computed from the metric of the static block for the polarisation along x1: '
              'u\'\' - 5H sgn u\' + e^{2H|sigma|} (omega^2 - k^2) u = 0 on both sides, the other components identically zero; the zero '
              'mode u = 1 is bound to the fold (norm %s: g_7^2 = 3 H g_8^2/2), massless in seven dimensions, omega = k exactly; '
              'A_sigma would need the profile e^{5H|sigma|} (no zero mode); the box of B9 reproduces omega = k to %.1e (UM-3: '
              'omega^2 = 2 k^2)' % (norm_v, dev2))

    # ---------------- B3: the photon as a transverse spin-1 wave
    kk = sp.Symbol('kappa_w', positive=True)
    eta4 = sp.diag(1, 1, 1, -1)
    kvec = sp.Matrix([0, 0, kk, -kk])                  # k_mu for e^{i k (x3 - x4)}: k_3 = k, k_4 = -k (k^mu = (0,0,k,k))
    kup = eta4 * kvec
    null = sp.simplify((kvec.T * eta4 * kvec)[0]) == 0
    # Lorenz gauge: k^mu eps_mu = 0; gauge: eps -> eps + c k
    e1 = sp.Matrix([1, 0, 0, 0])
    e2 = sp.Matrix([0, 1, 0, 0])
    lor = all(sp.simplify((kup.T * e)[0]) == 0 for e in (e1, e2))
    # the Lorenz solutions are spanned by e1, e2, k; the time-like polarisation (0,0,0,1) violates the Lorenz condition
    e4 = sp.Matrix([0, 0, 0, 1])
    lor_bad = sp.simplify((kup.T * e4)[0]) != 0
    # field strength and the physical fields for eps = e1: E and B orthogonal to the motion and to each other
    ph = sp.exp(sp.I * kk * (x3 - x4))
    A = [e1[i] * ph for i in range(4)]
    X4v = [x1, x2, x3, x4]
    F = [[sp.diff(A[nn], X4v[mm]) - sp.diff(A[mm], X4v[nn]) for nn in range(4)] for mm in range(4)]
    Evec = [sp.simplify(F[i][3]) for i in range(3)]          # E_i = F_{i4} (up to sign conventions)
    Bvec = [sp.simplify(F[1][2]), sp.simplify(F[2][0]), sp.simplify(F[0][1])]
    orth = (sp.simplify(Evec[2]) == 0 and sp.simplify(Bvec[2]) == 0
            and sp.simplify(sum(Evec[i] * Bvec[i] for i in range(3))) == 0
            and sp.simplify(sum(Evec[i] ** 2 for i in range(3)) - sum(Bvec[i] ** 2 for i in range(3))) == 0)
    # Maxwell: d_mu F^{mu nu} = 0 for k null
    maxwell = all(sp.simplify(sum(eta4[mm, mm] * sp.diff(F[mm][nn], X4v[mm]) for mm in range(4))) == 0 for nn in range(4))
    th = sp.Symbol('theta', real=True)
    Rz = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
    circ_p = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    circ_m = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
    hel = (sp.simplify((Rz * circ_p - sp.exp(-sp.I * th) * circ_p).applyfunc(lambda e_: e_.rewrite(sp.exp))) == sp.zeros(2, 1)
           and sp.simplify((Rz * circ_m - sp.exp(sp.I * th) * circ_m).applyfunc(lambda e_: e_.rewrite(sp.exp))) == sp.zeros(2, 1))
    ok3 = null and lor and lor_bad and orth and maxwell and hel
    out['B3_photon_wave'] = {'physical_polarisations': ['(1,0,0,0) along x1', '(0,1,0,0) along x2'],
                             'helicity': '+-1', 'E': [str(e_) for e_ in Evec], 'B': [str(b_) for b_ in Bvec]}
    rep.check('B3_photon_transverse_spin1', ok3, 'a plane wave e^{ik(x3 - x4)} on the fold: k null, Maxwell satisfied; the Lorenz condition '
              'leaves the polarisations along x1, x2 and the pure-gauge k; E and B orthogonal to x3 and to each other, |E| = |B|; '
              'the circular polarisations rotate with e^{-+i theta}: helicity +-1')

    # ---------------- B4: the graviton of the bulk
    hf = sp.Function('h')
    ok4 = True
    for s_ in (1, -1):
        hh = sp.Function('h')(SIG, x3, x4)
        lin = (sp.exp(2 * H * s_ * SIG) * (sp.diff(hh, x4, 2) - sp.diff(hh, x3, 2)) - sp.diff(hh, SIG, 2)
               + 7 * H * s_ * sp.diff(hh, SIG)) / 2
        zero_mode = hf(x3 - x4)
        ok4 &= sp.simplify(lin.subs(hh, zero_mode).doit()) == 0
    # same as the scalar: compare with B1 (u'' - 7 H sgn u' + e^{2H|sigma|}(w^2 - k^2) u) times -1/2
    out['B4_graviton'] = {'equation': '(1/2)[e^{2H|sigma|}(h_tt - h_33) - h_ss + 7H sgn(sigma) h_s] = 0',
                          'zero_mode': 'h = h(x3 - x4), any profile, independent of sigma', 'kappa_7': '(5/2) kappa H'}
    rep.check('B4_bulk_graviton_at_c', ok4, 'Einstein gravity: the + polarisation obeys the equation of the massless scalar; the zero mode '
              'h(x3 - x4) (independent of sigma, no jump of h_sigma) solves it on both sides: the graviton bound to the fold travels at '
              'the speed of light at every wavelength')

    # ---------------- B5: the gravitational wave in four dimensions
    hp, hx, ph_ = sp.symbols('h_plus h_cross phi', real=True)
    hmat = sp.Matrix([[hp, hx], [hx, -hp]])
    traceless = hmat.trace() == 0
    nvec = sp.Matrix([sp.cos(ph_), sp.sin(ph_)])
    rel = sp.simplify((nvec.T * hmat * nvec)[0] / 2)         # the relative change of the proper distance along n
    ring = sp.simplify(rel - (hp * sp.cos(2 * ph_) + hx * sp.sin(2 * ph_)) / 2) == 0
    rot = sp.simplify(Rz.T * hmat * Rz)
    hp_r, hx_r = sp.simplify(rot[0, 0]), sp.simplify(rot[0, 1])
    spin2 = (sp.simplify(hp_r - (hp * sp.cos(2 * th) + hx * sp.sin(2 * th))) == 0
             and sp.simplify(hx_r - (hx * sp.cos(2 * th) - hp * sp.sin(2 * th))) == 0)
    # circular: h_+ - +i h_x picks up e^{+-2 i theta}
    circ = sp.simplify(sp.expand(((hp_r + sp.I * hx_r) - sp.exp(-2 * sp.I * th) * (hp + sp.I * hx)).rewrite(sp.exp))) == 0
    # the sources of the fold: the energy-momentum tensor T_ab = -2 dL/dghat^ab + ghat_ab L of a field of the fold that does
    # not depend on the extra times (a scalar phi(x1..x4) with any potential), computed from its Lagrangian on the metric of
    # the fold with a general symmetric inverse metric: T_{mu r} = 0 and T_{rs} = ghat_rs L, so the coupling
    # (1/2) h^ab T_ab contains, of the components along the extra times, only ghat_rs h^rs (the change of their volume)
    Ginv = sp.Matrix(7, 7, lambda i, j: sp.Symbol('G%d%d' % (min(i, j), max(i, j))))
    phif = sp.Function('phi')(x1, x2, x3, x4)
    Vf = sp.Function('V')
    dphi = [sp.diff(phif, v_) for v_ in (x1, x2, x3, x4)] + [0, 0, 0]          # d_r phi = 0
    Lf = -sum(Ginv[i, j] * dphi[i] * dphi[j] for i in range(7) for j in range(7)) / 2 - Vf(phif)
    ghat0 = sp.diag(1, 1, 1, -1, -1, -1, -1)                                    # the static fold, a4 = 0, b4 = 1
    back = {Ginv[i, j]: ghat0.inv()[i, j] for i in range(7) for j in range(7)}
    Tab = sp.Matrix(7, 7, lambda i, j: (-2 * sp.diff(Lf, Ginv[i, j]) * (sp.Rational(1, 2) if i != j else 1)
                                        + ghat0[i, j] * Lf).subs(back))
    L0 = Lf.subs(back)
    t_mu_r = all(sp.simplify(Tab[i, j]) == 0 for i in range(4) for j in range(4, 7))
    t_rs = all(sp.simplify(Tab[i, j] - ghat0[i, j] * L0) == 0 for i in range(4, 7) for j in range(4, 7))
    ok5 = traceless and ring and spin2 and circ and t_mu_r and t_rs
    out['B5_gravitational_wave'] = {'polarisations': ['h_+ (h_11 = -h_22)', 'h_x (h_12 = h_21)'],
                                    'ring': '(1/2)(h_+ cos 2 phi + h_x sin 2 phi)', 'helicity': '+-2',
                                    'sources_of_the_fold': 'T_{mu r} = 0, T_{rs} = ghat_rs L (computed for a scalar of the fold): '
                                                           'h_{mu nu} and the trace of h_{rs} (held fixed by the fold fluid)'}
    rep.check('B5_gravitational_wave_plus_cross', ok5, 'h_ij traceless and transverse: a ring of test masses changes its radius at the '
              'angle phi by (1/2)(h_+ cos 2phi + h_x sin 2phi) (stretched along x1 and squeezed along x2 by h_+, along the '
              'diagonals by h_x); under a rotation by theta, (h_+, h_x) rotate by 2 theta and h_+ + i h_x by e^{-2i theta}: helicity '
              '+-2; the energy-momentum tensor of a field of the fold that does not depend on the extra times, computed from its '
              'Lagrangian, has T_{mu r} = 0 and T_{rs} = ghat_rs L: such matter couples only to h_{mu nu} and to the trace of h_{rs} '
              '(the polarisations of the seven-dimensional graviton and their signs: B11)')

    # ---------------- B6: the bulk fermion with a kink mass
    T = GM.T16A()
    eta = GM.eta4488()
    Ts = eta[0, 0] * T[0]                               # T^(sigma)
    ok6 = (Ts * Ts == sp.eye(16))
    # zero mode: T^(s) chi' - M sgn(s) chi = 0 with T^(s) chi_0 = -chi_0 -> chi = e^{-M|s|} chi_0
    tt = sp.Symbol('t', positive=True)
    conv = 2 * sp.integrate(sp.exp((H - 2 * M) * tt).subs(M, 2 * H), (tt, 0, sp.oo))          # both sides of the fold
    ok6 &= sp.simplify(conv - 2 / (3 * H)) == 0
    out['B6_fermion'] = {'zero_mode': 'chi = e^{-M|sigma|} chi_0, T^(sigma) chi_0 = -chi_0, Dhat chi_0 = 0',
                         'normalisable_for': 'M > H/2 (density e^{(H - 2M)|sigma|})', 'speed': '1'}
    rep.check('B6_bulk_fermion_at_c', ok6, 'T^(sigma) squares to 1 (two chiralities along sigma); the zero mode e^{-M|sigma|} chi_0 has the '
              'density e^{(H - 2M)|sigma|} (normalisable for M > H/2; norm 2/(3H) at M = 2H, both sides) and is a massless fermion of seven '
              'dimensions: the speed of light (UM-3: 2M/(2M - H))')

    # ---------------- B7: dirac16complex is boost invariant along the fold
    S34 = (eta[3, 3] * T[3]) * (eta[4, 4] * T[4]) / 2
    T3u, T4u = eta[3, 3] * T[3], eta[4, 4] * T[4]
    comm_s = (S34 * Ts - Ts * S34) == sp.zeros(16, 16)
    beta = sp.Symbol('beta', real=True)
    # infinitesimal action on T^(4), T^(3): [S34, T^(4)] and [S34, T^(3)]
    c4 = sp.simplify(S34 * T4u - T4u * S34)
    c3 = sp.simplify(S34 * T3u - T3u * S34)
    # for the boost: [S34, T^(4)] = +- T^(3), [S34, T^(3)] = +- T^(4) (a hyperbolic rotation since T^(3)^2 = 1, T^(4)^2 = -1)
    boost = (c4 == T3u or c4 == -T3u) and (c3 == T4u or c3 == -T4u)
    sq3 = T3u * T3u == sp.eye(16)
    sq4 = T4u * T4u == -sp.eye(16)
    chir = T[8]
    comm_chir = (S34 * chir - chir * S34) == sp.zeros(16, 16)          # the portal terms (P_L, P_R) are boost invariant
    ok7 = comm_s and boost and sq3 and sq4 and comm_chir
    out['B7_dirac16complex'] = {'boost_generator': 'T^(x3) T^(x4)/2', 'commutes_with_T_sigma': bool(comm_s),
                                'dispersion': 'omega^2 = k^2 + M^2 for every state', 'group_velocity': 'k/omega < 1'}
    rep.check('B7_dirac16complex_lorentz_invariant', ok7, 'with the author\'s matrices: S = T^(x3) T^(x4)/2 commutes with T^(sigma), with '
              'the chirality T16^8 (so with the portal terms mu_L P_L + mu_R P_R at the fold) and with the mass term, and [S, T^(x4)], [S, T^(x3)] = +-T^(x3), +-T^(x4) with T^(x3)^2 = 1, T^(x4)^2 = -1: the bulk equation is '
              'invariant under the boosts of the fold, so every state has omega^2 = k^2 + M^2 and moves slower than light')


    # ---------------- B9: the UM-3 speeds recomputed (the time not warped)
    ok9 = True
    tq9 = sp.Symbol('t', positive=True)
    for s_ in (1, -1):
        W2 = sp.exp(-2 * H * s_ * SIG)
        sq = sp.exp(-6 * H * s_ * SIG)                  # sqrt|g| of UM-3: six warped directions
        phi = u * sp.exp(sp.I * (k * x3 - w * x4))
        box3 = (sp.diff(sq * sp.diff(phi, SIG), SIG) + sq * (sp.diff(phi, x3, 2) / W2 - sp.diff(phi, x4, 2))) / sq
        mode3 = sp.simplify(box3 / sp.exp(sp.I * (k * x3 - w * x4)))
        target3 = sp.diff(u, SIG, 2) - 6 * H * s_ * sp.diff(u, SIG) + (w ** 2 - sp.exp(2 * H * s_ * SIG) * k ** 2) * u
        ok9 &= sp.simplify(mode3 - target3) == 0
    ratio_s = sp.simplify(sp.integrate(sp.exp(-4 * H * tq9), (tq9, 0, sp.oo)) / sp.integrate(sp.exp(-6 * H * tq9), (tq9, 0, sp.oo)))
    ratio_v = sp.simplify(sp.integrate(sp.exp(-2 * H * tq9), (tq9, 0, sp.oo)) / sp.integrate(sp.exp(-4 * H * tq9), (tq9, 0, sp.oo)))
    ok9 &= ratio_s == sp.Rational(3, 2) and ratio_v == 2
    kv9 = [0.01, 0.1, 0.5, 1.0, 3.0]
    um3_s = box_general(6, 4, 6, kv9)                   # flux sqrt g g^ss, potential sqrt g g^33, kinetic sqrt g |g^44|
    um3_v = box_general(4, 2, 4, kv9)                   # the same times g^11 for the polarisation along x1
    um4_s = box_general(7, 5, 5, kv9)
    um4_v = box_general(5, 3, 3, kv9)
    ok9 &= abs(um3_s[0] - 1.5) < 1e-3 and abs(um3_v[0] - 2.0) < 1e-3
    ok9 &= all(x > 1.0 for x in um3_s + um3_v) and all(a > b for a, b in zip(um3_s, um3_s[1:]))
    ok9 &= max(abs(x - 1.0) for x in um4_s + um4_v) < 1e-6
    out['B9_UM3_recomputed'] = {'UM3_scalar_mode_equation': "u'' - 6H sgn(sigma) u' + (omega^2 - e^{2H|sigma|} k^2) u = 0",
                                'UM3_long_wavelength': {'scalar_omega2_over_k2': str(ratio_s), 'photon_omega2_over_k2': str(ratio_v)},
                                'k_over_H': kv9, 'UM3_scalar_box_omega2_over_k2': um3_s, 'UM3_photon_box_omega2_over_k2': um3_v,
                                'UM4_scalar_box_omega2_over_k2': um4_s, 'UM4_photon_box_omega2_over_k2': um4_v}
    rep.check('B9_UM3_speeds_recomputed', ok9, 'UM-3 (time not warped): u\'\' - 6H sgn u\' + (omega^2 - e^{2H|sigma|} k^2) u = 0 on both '
              'halves; for k << H omega^2/k^2 = %s (scalar) and %s (photon) exactly; box omega^2/k^2 for k/H = %s: scalar %s, photon '
              '%s (faster than light at every wavelength); the same box for the metric of UM-4 gives 1 within %.1e, the exact result '
              'of B1 and B2 (a test of the box, not of UM-4)'
              % (ratio_s, ratio_v, kv9, ', '.join('%.4f' % x for x in um3_s), ', '.join('%.4f' % x for x in um3_v),
                 max(abs(x - 1.0) for x in um4_s + um4_v)))
    # the speeds in units of the speed of light of the fold (a summary of B1 to B7 and B9, not a separate check)
    out['speed_summary'] = {'photon_zero_mode': 1.0, 'graviton_zero_mode': 1.0, 'scalar_zero_mode': 1.0, 'fermion_zero_mode': 1.0,
                            'massive_modes': 'below 1 (group velocity k/omega)', 'UM3_scalar': float(sp.sqrt(ratio_s)),
                            'UM3_photon': float(sp.sqrt(ratio_v)), 'UM3_fermion': '2M/(2M - H) (UM-3, S-12)'}

    # ---------------- B11: the polarisations of the graviton bound to the fold and the signs of their kinetic terms
    # (a) the count: the massless graviton of the seven-dimensional fold (eta = diag(1, 1, 1, -1, -1, -1, -1)) for a null wave
    # vector along x1 and x4: symmetric h with k^A h_AB = 0 and eta^AB h_AB = 0, modulo h -> h + k xi + xi k with k.xi = 0
    etaN = np.diag([1.0, 1, 1, -1, -1, -1, -1])
    kup = np.array([1.0, 0, 0, 1, 0, 0, 0])                           # k^A: along x1 and x4, null
    klo = etaN @ kup
    basis = []
    for a_ in range(7):
        for b_ in range(a_, 7):
            E_ = np.zeros((7, 7))
            E_[a_, b_] = E_[b_, a_] = 1.0
            basis.append(E_)
    Bm_ = np.array([E_.ravel() for E_ in basis]).T                    # 49 x 28
    cons = np.vstack([np.array([(kup @ E_)[b_] for E_ in basis]) for b_ in range(7)]
                     + [np.array([np.trace(np.linalg.inv(etaN) @ E_) for E_ in basis])])
    ns_ = sla.null_space(cons)                                        # the transverse traceless h (coefficients)
    gauge = []
    for xi_lo in sla.null_space(kup.reshape(1, 7)).T:                 # gauge parameters xi_A with k^A xi_A = 0
        G_ = np.outer(klo, xi_lo) + np.outer(xi_lo, klo)
        gauge.append(np.linalg.lstsq(Bm_, G_.ravel(), rcond=None)[0])
    gauge = np.array(gauge).T
    rk_tt = ns_.shape[1]
    rk_gauge = np.linalg.matrix_rank(gauge, tol=1e-10)
    rk_in_tt = np.linalg.matrix_rank(np.hstack([ns_, gauge]), tol=1e-10) == rk_tt          # the gauge modes are inside TT
    n_phys = rk_tt - rk_gauge
    # (b) the sign of the kinetic term of each kind of polarisation from the second-order Einstein-Hilbert action
    Xf = [x1, x2, x3, x4] + list(Y567)
    etaf = sp.diag(1, 1, 1, -1, -1, -1, -1)

    def pat(pairs):
        P_ = sp.zeros(7, 7)
        for (a_, b_), c_ in pairs.items():
            P_[a_ - 1, b_ - 1] += c_
            if a_ != b_:
                P_[b_ - 1, a_ - 1] += c_
        return P_
    cases = [('graviton h_23 (cross, x)', {(2, 3): 1}, 'graviton'), ('graviton h_22 = -h_33 (plus, +)', {(2, 2): 1, (3, 3): -1}, 'graviton'),
             ('vector h_25 (ordinary space and an extra time)', {(2, 5): 1}, 'vector'),
             ('vector h_37', {(3, 7): 1}, 'vector'),
             ('scalar h_56 (two extra times)', {(5, 6): 1}, 'scalar'), ('scalar h_55 = -h_66', {(5, 5): 1, (6, 6): -1}, 'scalar')]
    signs = []
    for name_, pr_, kind_ in cases:
        C_, avg_ = eh_quadratic_average(pat(pr_), Xf, etaf)
        signs.append({'polarisation': name_, 'kind': kind_, 'C': str(C_), 'average_L2': str(avg_), 'healthy': bool(C_ > 0)})
    # (c) the Maxwell field of the fold for comparison: -(1/4) F_AB F^AB for A_2(x4, x1) and A_5(x4, x1)
    om2, kk2, A2s = sp.symbols('omega_m k_m A_m', positive=True)
    th2 = sp.Symbol('theta_m', real=True)
    maxw = {}
    for comp in (2, 5):
        Af = [0] * 7
        Af[comp - 1] = A2s * sp.cos(om2 * x4 - kk2 * x1)
        FF = sum(etaf[a_, a_] * etaf[b_, b_] * (sp.diff(Af[b_], Xf[a_]) - sp.diff(Af[a_], Xf[b_])) ** 2 for a_ in range(7) for b_ in range(7))
        Lm = -FF / 4
        avg_m = sp.simplify(sp.integrate(Lm.subs(om2 * x4 - kk2 * x1, th2).subs(x4, (th2 + kk2 * x1) / om2), (th2, 0, 2 * sp.pi)) / (2 * sp.pi))
        maxw['A_%d' % comp] = str(sp.factor(avg_m))
        maxw['A_%d_healthy' % comp] = bool(sp.simplify(avg_m / ((om2 ** 2 - kk2 ** 2) * A2s ** 2)) > 0)
    ok11 = (n_phys == 14 and rk_tt == 20 and rk_gauge == 6 and rk_in_tt
            and all(s_['healthy'] for s_ in signs if s_['kind'] in ('graviton', 'scalar'))
            and all(not s_['healthy'] for s_ in signs if s_['kind'] == 'vector')
            and maxw['A_2_healthy'] and not maxw['A_5_healthy'])
    out['B11_graviton_polarisations'] = {'transverse_traceless': rk_tt, 'residual_gauge': rk_gauge, 'physical': n_phys,
                                         'split': '2 (graviton h_{mu nu}) + 6 (three vectors h_{mu r}) + 6 (scalars h_{rs})',
                                         'kinetic_signs': signs, 'maxwell_for_comparison': maxw,
                                         'consequence': 'the vectors h_{mu r} are ghosts, as the components A_r of a gauge field'}
    rep.check('B11_graviton_polarisations_and_ghosts', ok11,
              'the massless graviton of the seven-dimensional fold has %d physical polarisations (%d transverse traceless less %d '
              'residual gauge modes): the graviton h_{mu nu} (2), three vectors h_{mu r} (6) and six scalars h_{rs} (6); the '
              'second-order Einstein-Hilbert action on the flat fold of signature (3, 4) gives the averaged Lagrangian '
              'C (omega^2 - k^2) A^2 with C = %s: positive (healthy) for the graviton and the scalars, negative for the vectors '
              'h_{mu r} with one index along ordinary space and one along an extra time: they are ghosts, like the component A_5 '
              'of a gauge field (Maxwell: %s for A_2, %s for A_5); the matter of the fold does not emit them at the linear order '
              '(T_{mu r} = 0, B5)' % (n_phys, rk_tt, rk_gauge, ', '.join('%s %s' % (s_['polarisation'].split(' (')[0], s_['C']) for s_ in signs),
                                     maxw['A_2'], maxw['A_5']))

    # ---------------- B10: the massive modes of the massless fields of the bulk, a continuum from zero mass
    ok10 = True
    zz = sp.Symbol('zeta', positive=True)
    for n_ in (5, 7):
        nu = sp.Rational(n_, 2)
        for s_ in (1, -1):
            zeta_s = sp.exp(H * s_ * SIG) / H
            for B_ in (sp.besselj, sp.bessely):
                u_ = zeta_s ** nu * sp.expand_func(B_(nu, m * zeta_s))
                res_ = sp.diff(u_, SIG, 2) - n_ * H * s_ * sp.diff(u_, SIG) + sp.exp(2 * H * s_ * SIG) * m ** 2 * u_
                ok10 &= sp.simplify(sp.expand(res_)) == 0
        for B_ in (sp.besselj, sp.bessely):
            lhs_ = sp.diff(zz ** nu * sp.expand_func(B_(nu, m * zz)), zz)
            ok10 &= sp.simplify(lhs_ - m * zz ** nu * sp.expand_func(B_(nu - 1, m * zz))) == 0
        zeta_p = sp.exp(H * SIG) / H
        ok10 &= sp.simplify(sp.exp(-(n_ - 2) * H * SIG) - H ** (-(n_ - 1)) * zeta_p ** (1 - n_) * sp.diff(zeta_p, SIG)) == 0
    sym10 = bool(ok10)

    def dens(n_, x):
        """the density at the fold of the even massive mode of mass m = x H, per unit m (H = 1)"""
        return 2.0 / (np.pi ** 2 * x * (spc.jv(n_ / 2 - 1, x) ** 2 + spc.yv(n_ / 2 - 1, x) ** 2))

    kl = []
    for n_ in (5, 7):
        for p_ in (0.3, 1.0, 3.0):
            f_ = (lambda x, n_=n_, p_=p_: dens(n_, x) / (p_ ** 2 + x ** 2))
            i1 = sint.quad(f_, 0, 50, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
            i2 = sint.quad(f_, 50, np.inf, limit=400, epsabs=1e-13, epsrel=1e-12)[0]
            spec = (n_ - 2) / (2 * p_ ** 2) + i1 + i2
            prop = spc.kv(n_ / 2, p_) / (2 * p_ * spc.kv(n_ / 2 - 1, p_))
            kl.append({'n': n_, 'p_over_H': p_, 'spectral': spec, 'propagator': float(prop), 'relative_difference': abs(spec / prop - 1)})
    dev_kl = max(r['relative_difference'] for r in kl)
    lim = {'s7_over_(x^4/(9 pi)) at x = 1e-3': float(dens(7, 1e-3) / (1e-3 ** 4 / (9 * np.pi))),
           's5_over_(x^2/pi) at x = 1e-3': float(dens(5, 1e-3) / (1e-3 ** 2 / np.pi)),
           'pi s7 at x = 200': float(np.pi * dens(7, 200.0)), 'pi s5 at x = 200': float(np.pi * dens(5, 200.0))}
    pos = all(dens(n_, x) > 0 for n_ in (5, 7) for x in np.geomspace(1e-4, 1e3, 200))
    lr = []
    for n_, cf in ((7, 16 / (15 * np.pi)), (5, 4 / (3 * np.pi))):
        for Hr in (50.0, 200.0):
            ii = sint.quad(lambda x, n_=n_, Hr=Hr: dens(n_, x) * np.exp(-x * Hr), 0, np.inf, limit=400, epsabs=0, epsrel=1e-11)[0]
            lr.append({'n': n_, 'H_r': Hr, 'coefficient': ii * 2 / (n_ - 2) * Hr ** (n_ - 2), 'predicted': cf})
    ok10 &= (dev_kl < 1e-10 and pos and abs(lim['s7_over_(x^4/(9 pi)) at x = 1e-3'] - 1) < 1e-5
             and abs(lim['s5_over_(x^2/pi) at x = 1e-3'] - 1) < 1e-5 and abs(lim['pi s7 at x = 200'] - 1) < 1e-3
             and abs(lim['pi s5 at x = 200'] - 1) < 1e-3
             and all(abs(r['coefficient'] / r['predicted'] - 1) < (1e-2 if r['H_r'] == 50.0 else 1e-3) for r in lr))
    out['B10_massive_modes'] = {'mode_equation': "u'' - n H sgn(sigma) u' + e^{2H|sigma|} m^2 u = 0 (n = 7 scalar and graviton, n = 5 "
                                                 'gauge field)',
                                'exact_solutions': 'zeta^{n/2} J_{n/2}(m zeta), zeta^{n/2} Y_{n/2}(m zeta), zeta = e^{H|sigma|}/H',
                                'even_mode': 'zeta^{n/2} (Y_{n/2-1}(m/H) J_{n/2}(m zeta) - J_{n/2-1}(m/H) Y_{n/2}(m zeta))',
                                'density_at_the_fold': 's_n(m) = 2H/(pi^2 m (J_{n/2-1}(m/H)^2 + Y_{n/2-1}(m/H)^2))',
                                'sympy_checks': sym10, 'spectral_representation': kl, 'limits': lim,
                                'long_range_coefficients': lr}
    rep.check('B10_continuum_from_zero_mass', ok10,
              'the massive modes zeta^{n/2} J_{n/2}(m zeta), zeta^{n/2} Y_{n/2}(m zeta) (zeta = e^{H|sigma|}/H) solve the profile '
              'equations of the scalar (n = 7) and of the gauge field (n = 5) on both halves, and the kinetic weight is the Hankel '
              'measure H^{-(n-1)} zeta^{1-n} d zeta: a continuum from m = 0 without a gap, beside the massless mode; the density at '
              'the fold s_n(m) = 2H/(pi^2 m (J_{n/2-1}^2 + Y_{n/2-1}^2)) gives the propagator (n - 2)H/(2p^2) + int dm s_n/(p^2 + m^2) '
              '= K_{n/2}(p/H)/(2p K_{n/2-1}(p/H)) to %.1e; s_7 = (m/H)^4/(9 pi), s_5 = (m/H)^2/pi for m << H (ratios %.7f, %.7f '
              'at m = 1e-3 H), s_n -> 1/pi for m >> H; the long-range coefficients of the static potentials at Hr = 200: %.5f '
              '(16/(15 pi) = %.5f) and %.5f (4/(3 pi) = %.5f)' % (
                  dev_kl, lim['s7_over_(x^4/(9 pi)) at x = 1e-3'], lim['s5_over_(x^2/pi) at x = 1e-3'],
                  lr[1]['coefficient'], lr[1]['predicted'], lr[3]['coefficient'], lr[3]['predicted']))
    return write('bulk', 'um4_bulk.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
