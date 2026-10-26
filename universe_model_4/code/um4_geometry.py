#!/usr/bin/env python3
"""um4_geometry.py - the metric of UM-4 and its exact geometry: the author's metric with the time x4 warped like the other
six directions of the fold (the author's order of 2026-10-25, 13:15 PDT: "You must find a new metric model in which x4 is
warped like the other directions").

The UM-4 metric in the author's coordinates X = (x0, x1, ..., x7) (x0 the hidden direction, x1..x3 ordinary space, x4 the
time, x5..x7 the extra times; z = 6 H x0, s6 = (sin^2 z)^(1/6), a4 = a4(x4), b4 = b4(x4)):
    g = diag(cot^2 z, e^{2 a4} s6, e^{2 a4} s6, e^{2 a4} s6, -s6, -e^{-2 a4} b4^2 s6, -e^{-2 a4} b4^2 s6, -e^{-2 a4} b4^2 s6);
it differs from the author's UM-3 metric only in g_{x4 x4} = -s6 (UM-3: -1).  In the proper chart of the hidden direction,
sigma = sgn(pi/2 - z) ln(sin z)/(6 H) (sin z = e^{-6 H |sigma|}, d sigma = |cot z| dx0),
    ds^2 = d sigma^2 + e^{-2 H |sigma|} ghat_ab dx^a dx^b,
    ghat = diag(e^{2 a4}, e^{2 a4}, e^{2 a4}, -1, -e^{-2 a4} b4^2, -e^{-2 a4} b4^2, -e^{-2 a4} b4^2)   (a, b = x1..x7),
the metric of the fold (FD-2) multiplied by one warp factor e^{-2 H |sigma|} in all seven directions of the fold.
Computed exactly (sympy), on both halves of the period:
  G1  the chart: the components of g in the author's coordinates equal those of the proper chart (s6 = e^{-2 H |sigma|},
      cot^2 z dx0^2 = d sigma^2), and the determinants give sqrt|g| = e^{-7 H |sigma|} sqrt|ghat|;
  G2  the exact frame curvature for any a4(x4), b4(x4), computed in the author's coordinates on both halves: in every plane
      of two directions of the fold R^{ab}_{cd} = e^{2 H |sigma|} Rhat^{ab}_{cd} - H^2 delta^{ab}_{cd} (Rhat the frame
      curvature of the fold metric ghat), and in every plane that contains the hidden direction R^{(0)a}_{(0)b} =
      -H^2 delta^a_b; no other component;
  G3  the static block (a4 and b4 constant): curvature -H^2 in all 28 frame planes, a space of constant curvature in all
      eight directions (UM-3: -H^2 in the 21 planes without the time, 0 in the 7 planes with the time); its scalar
      curvature is -56 H^2 and its Weyl tensor, computed from the coordinate Riemann and Ricci tensors, vanishes;
  G4  the Einstein-Lovelock tensors of the static block for any weights (alpha_(p) = w_(p) H^{2-2p}, Lambda = lam H^2):
      sum_p alpha_(p) E_(p)^a_b + Lambda delta^a_b = (21 - 420 w2 + 2520 w3 + lam) H^2 delta^a_b in every direction, order by
      order (21, -420, 2520) from the curvature (UM-3's static block had (15, -180, 360) along the warped directions and
      (21, -420, 2520) along the time); Einstein gravity alone (w2 = w3 = 0) needs Lambda = -21 H^2;
  G5  Einstein gravity with Lambda = -21 H^2 for any a4(x4), b4(x4): along the fold G^a_b + Lambda delta^a_b =
      e^{2 H |sigma|} Ghat^a_b (Ghat the Einstein tensor of ghat), along the hidden direction G^0_0 + Lambda =
      -(1/2) e^{2 H |sigma|} Rhat (Rhat the scalar curvature of ghat), no mixed component: the author's form of the metric
      solves the vacuum equations of the bulk exactly when the metric of the fold is Ricci flat; the Einstein tensor is
      computed in two independent ways (the generalised Kronecker delta contracted with the frame curvature, and
      G^M_N = g^MM R_MN - delta^M_N R/2 with the Ricci tensor taken directly from the Christoffel symbols) and they agree;
  G6  the Ricci-flat metrics of the fold of the author's form: the static fold (a4, b4 constant), and the two Kasner metrics
      e^{a4} = x4^p, e^{-a4} b4 = x4^q with {p, q} = {(1 + sqrt 5)/6, (1 - sqrt 5)/6} (x4 > 0); with frozen extra times
      (e^{-a4} b4 constant) only the static fold: Ghat^(4)_(4) = -3 a4'^2, so an expanding fold with frozen extra times
      needs matter and a bulk metric that is not of the author's form (its corrections are computed in um4_fold.py, F1);
  G7  the extrinsic curvature of the slices sigma = const, K^a_b = (1/2) g^ac d_sigma g_cb = -H sgn(sigma) delta^a_b in all
      seven directions (UM-3: K^(4)_(4) = 0), its jump -2 H delta^a_b at the fold, and the junction condition of Einstein
      gravity (Israel): for the warp e^{-2F(sigma)} the Einstein tensor contains -6 F'' delta^a_b, so with F = H |sigma|
      (F'' = 2 H delta_D(sigma)) kappa S^a_b = integral_{0-}^{0+} d sigma G^a_b = -12 H delta^a_b (the coefficient of F''
      times the computed jump of F'), equal to -([K^a_b] - [K] delta^a_b) with the computed jump of K: for every a4, b4 the
      thin source of the author's form of the metric is a pure tension, kappa lambda_F = 12 H (UM-3: -(32/5) H with the
      Lovelock weights);
  G8  the light cone: on every slice sigma = const the metric is e^{-2 H |sigma|} ghat, so its light cone is the light cone
      of the fold: a field of the bulk that moves along x3 at fixed sigma has the coordinate speed dx3/dx4 = e^{-a4}, the
      speed of light of the fold, at every sigma (UM-3: e^{H |sigma| - a4}, so that bulk fields outran light on the fold);
  G9  the canonical spin connection of dirac16complex with the author's matrices T16^A: gamma^M Omega_M = (7/2) H T^(x0)
      + (3/2) (b4'/b4) s6^{-1/2} T^(x4) on 0 < z < pi/2 (on the second half the first term is -(7/2) H T^(x0), the frame
      of x0 along cot z), so that a bulk spinor Psi = e^{(7/2) H |sigma|} chi obeys
      gamma^M D_M Psi = e^{(7/2) H |sigma|} [T^(sigma) d_sigma chi + e^{H |sigma|} Dhat chi], Dhat the Dirac operator of the
      fold metric (verified with the matrices); the covariant constancy D_M gamma^N = 0 on both halves;
  G10 the static warps with different rates, d sigma^2 + e^{-2 p H sigma} dx_i^2 - e^{-2 q H sigma} dx4^2
      - e^{-2 r H sigma} dx_r^2 (sigma > 0): the Einstein tensor is diagonal, G^(1)_(1) - G^(4)_(4) = -(p - q)(3p + q + 3r) H^2,
      G^(1)_(1) - G^(5)_(5) = -(p - r)(3p + q + 3r) H^2, and the only real rates for which the metric is a vacuum of Einstein
      gravity with a cosmological constant are q = r = p (then Lambda = -21 p^2 H^2): among these warps only the one with the
      time warped like the other directions is a vacuum; the static block of UM-3, (p, q, r) = (1, 0, 1), is not;
  G11 the Dirac matrices written out in FD-13 of the definition of the fold below (the text that every UM-4 file carries):
      the six 4 x 4 matrices s_1, s_2, s_3, t_1, t_2, t_3 are read from this docstring, assembled into Xi_a,
      Xibar_a = sigma_8 Xi_a^T sigma_8 and T_a = [[0, Xibar_a], [Xi_a, 0]] as FD-13 says, and compared entry by entry with
      the author's T16^A[0..7] of 4+4.nb (um4_gammas.py).
Writes outputs/geometry.json and reports/geometry_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_4/code/um4_geometry.py

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

import re
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM                          # noqa: E402
from um4_common import Report, write             # noqa: E402
from um4_lovelock import christoffel, frame_riemann, lovelock_tensor, riemann_coord   # noqa: E402

H = sp.Symbol('H', positive=True)
X = sp.symbols('x0:8', real=True)
x4 = X[4]
a4 = sp.Function('a4')(x4)
b4 = sp.Function('b4')(x4)
w2, w3, lam = sp.symbols('w2 w3 lam')
SIG = sp.Symbol('sigma', real=True)
EPS = [1, 1, 1, 1, -1, -1, -1, -1]
NAMES = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']


def author_metric(half):
    """The UM-4 metric in the author's coordinates on the half 0 < z < pi/2 (half = 1) or pi/2 < z < pi (half = 2), and the
    positive scale factors h_a (g = diag(eps_a h_a^2))."""
    z = 6 * H * X[0]
    s6 = sp.sin(z) ** sp.Rational(1, 3)          # (sin^2 z)^(1/6) for 0 < z < pi
    h0 = sp.cot(z) if half == 1 else -sp.cot(z)
    h = [h0] + [sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.sin(z) ** sp.Rational(1, 6)] + \
        [sp.exp(-a4) * b4 * sp.sin(z) ** sp.Rational(1, 6)] * 3
    g = sp.diag(*[EPS[i] * h[i] ** 2 for i in range(8)])
    return g, h, s6


def proper_metric(side):
    """The UM-4 metric in the proper chart on the side sigma > 0 (side = +1) or sigma < 0 (side = -1), X[0] -> sigma."""
    W = sp.exp(-H * side * SIG)
    h = [sp.S(1)] + [W * sp.exp(a4)] * 3 + [W] + [W * sp.exp(-a4) * b4] * 3
    g = sp.diag(*[EPS[i] * h[i] ** 2 for i in range(8)])
    return g, h


def fold_metric():
    Y = list(X[1:])
    h = [sp.exp(a4)] * 3 + [sp.S(1)] + [sp.exp(-a4) * b4] * 3
    g = sp.diag(*[EPS[i + 1] * h[i] ** 2 for i in range(7)])
    return g, h, Y


def zero(e):
    return sp.simplify(e) == 0


def main():
    rep = Report()
    out = {'metric_author_coordinates': 'diag(cot^2 z, e^{2a4} s6 (x3), -s6, -e^{-2a4} b4^2 s6 (x3)), s6 = (sin^2 z)^(1/6)',
           'metric_proper_chart': 'd sigma^2 + e^{-2H|sigma|} [e^{2a4} dx_i^2 - dx4^2 - e^{-2a4} b4^2 dx_r^2]'}

    # ---------------- G1: the chart
    ok1 = True
    for half, side in ((1, -1), (2, +1)):
        g, h, s6 = author_metric(half)
        z = 6 * H * X[0]
        sig_of_x0 = (1 if half == 1 else -1) * sp.log(sp.sin(z)) / (6 * H)   # sigma = sgn(pi/2 - z) ln(sin z)/(6H)
        dsig = sp.diff(sig_of_x0, X[0])
        ok1 &= zero(dsig ** 2 - g[0, 0])                                  # d sigma^2 = cot^2 z dx0^2
        warp = sp.exp(-2 * H * side * sig_of_x0)                          # e^{-2H|sigma|} on this half
        ok1 &= zero(sp.expand(warp - s6 ** 1).rewrite(sp.exp)) or zero(sp.simplify(sp.log(warp) - sp.log(s6)))
        gp, hp = proper_metric(side)
        for i in range(1, 8):
            ok1 &= zero(gp[i, i].subs(SIG, sig_of_x0) - g[i, i])
        # sqrt|g| of the proper chart from its determinant, against e^{-7H|sigma|} sqrt|ghat|
        gf_, hf_, _ = fold_metric()
        detp = gp.det()
        detf = gf_.det()
        ok1 &= zero(detp / detf - sp.exp(-14 * H * side * SIG))          # a positive ratio: sqrt|g|/sqrt|ghat| = e^{-7H|sigma|}
    rep.check('G1_proper_chart', ok1, 'with sigma = sgn(pi/2 - z) ln(sin z)/(6H): cot^2 z dx0^2 = d sigma^2 and s6 = e^{-2H|sigma|} on '
              'both halves; every component along the fold, the time included, is e^{-2H|sigma|} ghat_ab; det g/det ghat = '
              'e^{-14H|sigma|} computed from the determinants, so sqrt|g| = e^{-7H|sigma|} sqrt|ghat|')

    # ---------------- G2: the exact curvature in the author's coordinates
    gf, hf, Y = fold_metric()
    Rhat = frame_riemann(gf, Y, hf)
    Rhat8 = {((a + 1, b + 1), (c + 1, d + 1)): v for ((a, b), (c, d)), v in Rhat.items()}
    ok2 = True
    curv = {}
    for half in (1, 2):
        g, h, s6 = author_metric(half)
        Rf = frame_riemann(g, X, h)
        curv[half] = Rf
        z = 6 * H * X[0]
        e2Hs = sp.sin(z) ** sp.Rational(-1, 3)                            # e^{2H|sigma|}
        keys = set(Rf) | set(Rhat8) | {((a, b), (a, b)) for a in range(8) for b in range(a + 1, 8)}
        for ((a, b), (c, d)) in keys:
            if a == 0 or c == 0:
                expect = -H ** 2 if (a, b) == (c, d) else 0
            else:
                expect = e2Hs * Rhat8.get(((a, b), (c, d)), 0) - (H ** 2 if (a, b) == (c, d) else 0)
            if not zero(Rf.get(((a, b), (c, d)), 0) - expect):
                ok2 = False
    out['curvature_fold_planes'] = 'R^{ab}_{cd} = e^{2H|sigma|} Rhat^{ab}_{cd} - H^2 delta^{ab}_{cd}'
    out['curvature_hidden_planes'] = 'R^{(0)a}_{(0)b} = -H^2 delta^a_b'
    out['fold_metric_frame_curvature'] = {'%s%s,%s%s' % (NAMES[k[0][0] + 1], NAMES[k[0][1] + 1], NAMES[k[1][0] + 1], NAMES[k[1][1] + 1]):
                                          str(sp.simplify(v)) for k, v in Rhat.items()}
    rep.check('G2_exact_curvature', ok2, 'on both halves of the period, for any a4(x4), b4(x4): R^{ab}_{cd} = e^{2H|sigma|} '
              'Rhat^{ab}_{cd} - H^2 delta^{ab}_{cd} in the planes of the fold, R^{(0)a}_{(0)b} = -H^2 delta^a_b in the planes '
              'with the hidden direction (%d non-zero frame components of the fold metric)' % len(Rhat))

    # ---------------- G3: the static block
    st = {a4: 0, b4: 1}
    g, h, s6 = author_metric(1)
    gs = g.subs(st).doit()
    hs = [sp.simplify(hh.subs(st).doit()) for hh in h]
    Rs = frame_riemann(gs, X, hs)
    planes = [((a, b), (a, b)) for a in range(8) for b in range(a + 1, 8)]
    ok3 = all(zero(Rs.get(p, 0) + H ** 2) for p in planes) and all(k in planes for k in Rs)
    # the Weyl tensor computed from the coordinate Riemann tensor, the Ricci tensor and the scalar curvature (eight
    # dimensions): C_{lijk} = R_{lijk} - (g_{lj} R_{ik} - g_{lk} R_{ij} - g_{ij} R_{lk} + g_{ik} R_{lj})/6
    #                         + R (g_{lj} g_{ik} - g_{lk} g_{ij})/42,
    # in the proper chart of the static block on both sides (exponentials, which simplify exactly)
    weyl_max = 0
    scalars = []
    for side in (+1, -1):
        gp_, hp_ = proper_metric(side)
        gs_ = gp_.subs(st).doit()
        Xp_ = [SIG] + list(X[1:])
        Rc = riemann_coord(gs_, Xp_)
        Ric_s = sp.zeros(8, 8)
        for (l_, i_, j_, k_), v_ in Rc.items():
            if l_ == j_:
                Ric_s[i_, k_] += v_
        Ric_s = Ric_s.applyfunc(sp.simplify)
        Rsc = sp.simplify(sum(Ric_s[i_, i_] / gs_[i_, i_] for i_ in range(8)))
        scalars.append(Rsc)
        gl = lambda p_, q_: gs_[p_, q_]
        for l_ in range(8):
            for i_ in range(8):
                for j_ in range(8):
                    for k_ in range(8):
                        Rl = gs_[l_, l_] * Rc.get((l_, i_, j_, k_), 0)                 # R_{lijk} (lower the first index)
                        C = (Rl - (gl(l_, j_) * Ric_s[i_, k_] - gl(l_, k_) * Ric_s[i_, j_] - gl(i_, j_) * Ric_s[l_, k_]
                                   + gl(i_, k_) * Ric_s[l_, j_]) / 6
                             + Rsc * (gl(l_, j_) * gl(i_, k_) - gl(l_, k_) * gl(i_, j_)) / 42)
                        if C != 0 and not zero(C):
                            weyl_max += 1
    Rsc = scalars[0]
    ok3 &= weyl_max == 0 and all(zero(r_ + 56 * H ** 2) for r_ in scalars)
    out['static_block_scalar_curvature'] = str(Rsc)
    rep.check('G3_static_block_constant_curvature', ok3, 'a4, b4 constant: R^{ab}_{ab} = -H^2 in all 28 frame planes and no '
              'other component: a space of constant curvature -H^2 in all eight directions; the scalar curvature %s and the Weyl '
              'tensor computed from the coordinate Riemann and Ricci tensors (proper chart, both sides): %d non-zero components '
              'of 2 x 4096; UM-3 had 0 in the 7 planes that contain the time' % (Rsc, weyl_max))

    # ---------------- G4: the Einstein-Lovelock tensors of the static block
    E = {p: lovelock_tensor(Rs, p) for p in (1, 2, 3)}
    per = {p: sorted(set(sp.simplify(E[p][i, i] / H ** (2 * p)) for i in range(8))) for p in (1, 2, 3)}
    offd = all(E[p][i, j] == 0 for p in (1, 2, 3) for i in range(8) for j in range(8) if i != j)
    tot = sorted(set(sp.expand(E[1][i, i] + w2 / H ** 2 * E[2][i, i] + w3 / H ** 4 * E[3][i, i] + lam * H ** 2) for i in range(8)),
                 key=str)
    ok4 = (offd and per == {1: [21], 2: [-420], 3: [2520]} and len(tot) == 1
           and sp.expand(tot[0] - (21 - 420 * w2 + 2520 * w3 + lam) * H ** 2) == 0)
    out['static_block_lovelock_per_order_over_H2p'] = {str(p): [str(v) for v in per[p]] for p in per}
    out['static_block_field_equation'] = str(sp.factor(tot[0]))
    rep.check('G4_static_block_lovelock', ok4, 'every direction: E_(1) = 21 H^2, E_(2) = -420 H^4, E_(3) = 2520 H^6, so '
              'sum alpha_p E_(p) + Lambda = (21 - 420 w2 + 2520 w3 + lam) H^2 delta^a_b (no off-diagonal component); Einstein '
              'gravity alone needs Lambda = -21 H^2')

    # ---------------- G5: Einstein gravity for any a4, b4
    Ghat = lovelock_tensor(Rhat, 1, n=7)
    Rhat_s = sp.simplify(-sum(Ghat[i, i] for i in range(7)) * 2 / 5)          # trace: Ghat^a_a = -(5/2) Rhat in 7D
    ok5 = True
    ricci_route = True
    for side in (+1, -1):
        gp, hp = proper_metric(side)
        Xp = [SIG] + list(X[1:])
        Rp = frame_riemann(gp, Xp, hp)
        G = lovelock_tensor(Rp, 1)
        # the independent route: the Ricci tensor directly from the Christoffel symbols,
        # R_ik = d_l Gamma^l_ik - d_k Gamma^l_il + Gamma^l_lm Gamma^m_ik - Gamma^l_km Gamma^m_il,
        # and G^M_N = g^MM R_MN - delta^M_N R/2 (no frame, no generalised Kronecker delta)
        Gc = christoffel(gp, Xp)
        Ric = sp.zeros(8, 8)
        for i_ in range(8):
            for k_ in range(8):
                v_ = 0
                for l_ in range(8):
                    v_ += sp.diff(Gc[l_][i_][k_], Xp[l_]) - sp.diff(Gc[l_][i_][l_], Xp[k_])
                    for m_ in range(8):
                        v_ += Gc[l_][l_][m_] * Gc[m_][i_][k_] - Gc[l_][k_][m_] * Gc[m_][i_][l_]
                Ric[i_, k_] = sp.simplify(v_)
        Rsc_ = sp.simplify(sum(Ric[i_, i_] / gp[i_, i_] for i_ in range(8)))
        Gmix = sp.Matrix(8, 8, lambda i_, k_: Ric[i_, k_] / gp[i_, i_] - (Rsc_ / 2 if i_ == k_ else 0))
        ricci_route &= all(zero(Gmix[i_, k_] - G[i_, k_]) for i_ in range(8) for k_ in range(8))
        e2 = sp.exp(2 * H * side * SIG)
        for i in range(8):
            for j in range(8):
                if i == 0 and j == 0:
                    target = -e2 * Rhat_s / 2
                elif i == 0 or j == 0:
                    target = 0
                else:
                    target = e2 * Ghat[i - 1, j - 1]
                if not zero(G[i, j] - (21 * H ** 2 if i == j else 0) - target):
                    ok5 = False
    ok5 &= ricci_route
    out['einstein_separable'] = {'fold_components': 'G^a_b - 21 H^2 delta^a_b = e^{2H|sigma|} Ghat^a_b',
                                 'hidden_component': 'G^0_0 - 21 H^2 = -(1/2) e^{2H|sigma|} Rhat', 'mixed': '0'}
    out['fold_metric_einstein_tensor'] = {NAMES[i + 1]: str(sp.factor(sp.simplify(Ghat[i, i]))) for i in range(7)}
    out['fold_metric_scalar_curvature'] = str(sp.factor(Rhat_s))
    out['einstein_two_routes_agree'] = bool(ricci_route)
    rep.check('G5_einstein_bulk_equations', ok5, 'Einstein gravity, Lambda = -21 H^2, any a4(x4), b4(x4), both sides: G^a_b + '
              'Lambda delta^a_b = e^{2H|sigma|} Ghat^a_b along the fold, G^0_0 + Lambda = -(1/2) e^{2H|sigma|} Rhat, no mixed '
              'component: the author\'s form of the metric is a vacuum of the bulk exactly when the fold metric is Ricci flat; the '
              'Einstein tensor computed in two ways, by the generalised Kronecker delta from the frame curvature and from the Ricci '
              'tensor taken directly from the Christoffel symbols (G^M_N = g^MM R_MN - delta^M_N R/2), agrees in all 64 components '
              'on both sides: %s' % ricci_route)

    # ---------------- G6: Ricci-flat fold metrics of the author's form
    t = sp.Symbol('t', positive=True)
    p, q = sp.symbols('p q', real=True)
    kas = {a4: p * sp.log(x4), b4: x4 ** (p + q)}
    Gk = [sp.simplify((Ghat[i, i].subs(kas).doit()) * x4 ** 2) for i in range(7)]
    eqs = sorted(set(sp.expand(e) for e in Gk), key=str)
    sols = sp.solve(eqs, [p, q], dict=True)
    sols_nonzero = [s_ for s_ in sols if not (s_.get(p, p) == 0 and s_.get(q, q) == 0)]
    expect = [{p: (1 + sp.sqrt(5)) / 6, q: (1 - sp.sqrt(5)) / 6}, {p: (1 - sp.sqrt(5)) / 6, q: (1 + sp.sqrt(5)) / 6}]
    ok6 = (len(sols_nonzero) == 2 and all(any(sp.simplify(s_.get(p, p) - e[p]) == 0 and sp.simplify(s_.get(q, q) - e[q]) == 0
                                              for e in expect) for s_ in sols_nonzero))
    c0 = sp.Symbol('c0', positive=True)
    frozen = {b4: c0 * sp.exp(a4)}
    G44_frozen = sp.simplify(Ghat[3, 3].subs(frozen).doit())
    ok6 &= sp.simplify(G44_frozen + 3 * sp.diff(a4, x4) ** 2) == 0
    out['kasner_exponents'] = [{str(k): str(v) for k, v in s_.items()} for s_ in sols_nonzero]
    out['frozen_extra_times_Ghat44'] = str(G44_frozen)
    rep.check('G6_ricci_flat_folds', ok6, 'e^{a4} = x4^p, e^{-a4} b4 = x4^q: Ricci flat only for p = q = 0 (static) and {p, q} = '
              '{(1 + sqrt 5)/6, (1 - sqrt 5)/6} (Kasner: 3p + 3q = 1, 3p^2 + 3q^2 = 1); with frozen extra times Ghat^(4)_(4) = %s, '
              'so the only Ricci-flat fold with frozen extra times is static' % G44_frozen)

    # ---------------- G7: extrinsic curvature and the junction condition
    ok7 = True
    for side in (+1, -1):
        gp, hp = proper_metric(side)
        K = [sp.simplify(sp.diff(gp[i, i], SIG) / (2 * gp[i, i])) for i in range(1, 8)]
        ok7 &= all(zero(k_ + side * H) for k_ in K)
    Fs = sp.Function('F')(SIG)
    hF = [sp.S(1)] + [sp.exp(-Fs)] * 7
    gF = sp.diag(*[EPS[i] * hF[i] ** 2 for i in range(8)])
    RF = frame_riemann(gF, [SIG] + list(X[1:]), hF)
    GF = lovelock_tensor(RF, 1)
    F1, F2 = sp.diff(Fs, SIG), sp.diff(Fs, SIG, 2)
    ok7 &= all(zero(GF[i, i] - (21 * F1 ** 2 - 6 * F2)) for i in range(1, 8)) and zero(GF[0, 0] - 21 * F1 ** 2)
    ok7 &= all(GF[i, j] == 0 for i in range(8) for j in range(8) if i != j)
    # F = H|sigma|: the thin part of G^a_b is its F'' term; its integral across the fold is the coefficient of F'' times the
    # jump of F' = H sgn(sigma) (F'(0+) - F'(0-) = 2H); Israel's form -([K^a_b] - [K] delta^a_b) from the computed K
    coefF2 = sp.simplify(sp.diff(GF[1, 1], F2))                       # the coefficient of F'' in G^a_b along the fold
    jumpF1 = (sp.diff(H * SIG, SIG) - sp.diff(-H * SIG, SIG))         # F'(0+) - F'(0-) for F = H|sigma|
    kappaS = sp.simplify(coefF2 * jumpF1)
    Kplus = [sp.simplify(sp.diff(proper_metric(+1)[0][i, i], SIG) / (2 * proper_metric(+1)[0][i, i])) for i in range(1, 8)]
    Kminus = [sp.simplify(sp.diff(proper_metric(-1)[0][i, i], SIG) / (2 * proper_metric(-1)[0][i, i])) for i in range(1, 8)]
    jumpK = [sp.simplify(kp - km) for kp, km in zip(Kplus, Kminus)]
    israel = [sp.simplify(-(jk - sum(jumpK))) for jk in jumpK]
    ok7 &= zero(kappaS + 12 * H) and all(zero(v_ + 12 * H) for v_ in israel)
    out['extrinsic_curvature'] = 'K^a_b = -H sgn(sigma) delta^a_b (all seven directions)'
    out['einstein_tensor_warp_F'] = {'fold': str(GF[1, 1]), 'hidden': str(GF[0, 0])}
    out['kappa_S_static'] = str(kappaS)
    out['israel_from_K_jump'] = [str(v_) for v_ in israel]
    rep.check('G7_junction_pure_tension', ok7, 'K^a_b = -H sgn(sigma) delta^a_b along all seven directions of the fold on both '
              'sides (jump -2H delta^a_b); for the warp e^{-2F}: G^a_b = 21 F\'^2 - 6 F\'\' along the fold, G^0_0 = 21 F\'^2; with '
              'F = H|sigma| the integral across the fold, the coefficient %s of F\'\' times the jump %s of F\', gives kappa S^a_b = %s '
              'delta^a_b, and Israel\'s condition kappa S^a_b = -([K^a_b] - [K] delta^a_b) with the computed jump of K gives %s in '
              'every direction: a pure tension kappa lambda_F = 12 H for every a4, b4 of the author\'s form' % (
                  coefF2, jumpF1, kappaS, sorted(set(str(v_) for v_ in israel))))

    # ---------------- G8: the light cone of every slice
    ok8 = True
    for side in (+1, -1):
        gp, hp = proper_metric(side)
        speed2 = sp.simplify(-gp[4, 4] / gp[3, 3])                    # (dx3/dx4)^2 of a null line along x3 at fixed sigma
        ok8 &= zero(speed2 - sp.exp(-2 * a4))
    out['coordinate_speed_along_x3_at_fixed_sigma'] = 'e^{-a4} (the speed of light of the fold), at every sigma'
    rep.check('G8_light_cone_of_every_slice', ok8, 'a null line along x3 at fixed sigma has dx3/dx4 = e^{-a4} at every sigma, the '
              'speed of light of the fold: the bulk has the light cone of the fold everywhere (UM-3: e^{H|sigma| - a4})')

    # ---------------- G9: the spin connection with the author's matrices
    T = GM.T16A()
    eta = GM.eta4488()
    S_ab = GM.SAB()
    ok9 = True
    for half in (1, 2):
        g, h, s6 = author_metric(half)
        Gm = christoffel(g, X)
        om = {}
        for M in range(8):
            for a in range(8):
                for b in range(8):
                    N = a
                    term = (sp.diff(eta[b, b] * h[b], X[M]) if N == b else 0) - Gm[b][M][N] * eta[b, b] * h[b]
                    val = sp.simplify(term / h[a])
                    if val != 0:
                        om[(M, a, b)] = val
        ok9 &= all(sp.simplify(om.get((M, a, b), 0) + om.get((M, b, a), 0)) == 0 for M in range(8) for a in range(8)
                   for b in range(8))
        Omega = {}
        for M in range(8):
            Om = sp.zeros(16, 16)
            for a in range(8):
                for b in range(8):
                    if (M, a, b) in om:
                        Om += sp.Rational(1, 2) * om[(M, a, b)] * eta[a, a] * eta[b, b] * S_ab[(a, b)]
            Omega[M] = Om.applyfunc(sp.simplify)
        gOm = sp.zeros(16, 16)
        for M in range(8):
            gOm += (eta[M, M] * T[M] / h[M]) * Omega[M]
        gOm = gOm.applyfunc(sp.simplify)
        sgn = 1 if half == 1 else -1
        target = sgn * sp.Rational(7, 2) * H * eta[0, 0] * T[0] + sp.Rational(3, 2) * (sp.diff(b4, x4) / b4) / h[4] * eta[4, 4] * T[4]
        ok9 &= (gOm - target).applyfunc(sp.simplify) == sp.zeros(16, 16)
        if True:                                         # D_M gamma^N = 0 on both halves of the period
            for M in range(8):
                for N in range(8):
                    gN = eta[N, N] * T[N] / h[N]
                    expr = sp.diff(gN, X[M]) + sum((Gm[N][M][P] * (eta[P, P] * T[P] / h[P]) for P in range(8)), sp.zeros(16, 16)) \
                        + Omega[M] * gN - gN * Omega[M]
                    if any(sp.simplify(e_) != 0 for e_ in expr if e_ != 0):
                        ok9 = False
    out['spin_connection_gamma_Omega'] = '(7/2) H T^(x0) + (3/2) (b4\'/b4) s6^{-1/2} T^(x4) on 0 < z < pi/2'
    out['bulk_dirac_operator'] = 'gamma^M D_M (e^{(7/2)H|sigma|} chi) = e^{(7/2)H|sigma|} [T^(sigma) d_sigma chi + e^{H|sigma|} Dhat chi]'
    rep.check('G9_spin_connection', ok9, 'with the author\'s matrices: omega_{M ab} antisymmetric, gamma^M Omega_M = (7/2) H T^(x0) + '
              '(3/2)(b4\'/b4) s6^{-1/2} T^(x4) on the first half (-(7/2) H T^(x0) on the second), D_M gamma^N = 0 on both halves: a bulk spinor '
              'Psi = e^{(7/2)H|sigma|} chi obeys gamma^M D_M Psi = e^{(7/2)H|sigma|}[T^(sigma) chi\' + e^{H|sigma|} Dhat chi] (the '
              'factor e^{H|sigma|} multiplies the whole Dirac operator of the fold, time derivative included)')

    # ---------------- G10: static warps with different rates: only equal rates give a vacuum of Einstein gravity
    s_ = sp.Symbol('s', positive=True)
    pr, qr, rr = sp.symbols('p q r', real=True)
    Xs = [s_] + list(sp.symbols('y1:8', real=True))
    rates = [0, pr, pr, pr, qr, rr, rr, rr]
    hs = [sp.S(1)] + [sp.exp(-rates[i] * H * s_) for i in range(1, 8)]
    gs = sp.diag(*[EPS[i] * hs[i] ** 2 for i in range(8)])
    E1s = lovelock_tensor(frame_riemann(gs, Xs, hs), 1)
    diag_only = all(sp.simplify(E1s[i, j]) == 0 for i in range(8) for j in range(8) if i != j)
    c0, c1, c4, c5 = [sp.expand(sp.simplify(E1s[i, i] / H ** 2)) for i in (0, 1, 4, 5)]
    d14 = sp.factor(c1 - c4)
    d15 = sp.factor(c1 - c5)
    ok10 = diag_only and zero(d14 + (pr - qr) * (3 * pr + qr + 3 * rr)) and zero(d15 + (pr - rr) * (3 * pr + qr + 3 * rr))
    sols = sp.solve([c0 - c1, c1 - c4, c1 - c5], [qr, rr], dict=True)
    real_sols = [s0 for s0 in sols if all(sp.simplify(sp.im(v)) == 0 for v in s0.values())]
    ok10 &= len(real_sols) == 1 and zero(real_sols[0][qr] - pr) and zero(real_sols[0][rr] - pr)
    ok10 &= zero(c1.subs({qr: pr, rr: pr}) - 21 * pr ** 2)
    um3_block = {pr: 1, qr: 0, rr: 1}
    um3_diffs = [sp.nsimplify(e_.subs(um3_block)) for e_ in (c0 - c1, c1 - c4, c1 - c5)]
    ok10 &= any(v != 0 for v in um3_diffs)
    out['static_warps_einstein'] = {'G11_minus_G44_over_H2': str(d14), 'G11_minus_G55_over_H2': str(d15),
                                    'G00_minus_G11_over_H2': str(sp.factor(c0 - c1)),
                                    'real_vacua': 'q = r = p, Lambda = -21 p^2 H^2',
                                    'UM3_block_differences': [str(v) for v in um3_diffs]}
    rep.check('G10_only_equal_warps_are_vacua', ok10, 'static warps (p, q, r): the Einstein tensor is diagonal, G^(1)_(1) - G^(4)_(4) = '
              '%s H^2, G^(1)_(1) - G^(5)_(5) = %s H^2; the only real solution of G^a_b + Lambda delta^a_b = 0 is q = r = p with '
              'Lambda = -21 p^2 H^2; the static block of UM-3 (1, 0, 1) has G^(0)_(0) - G^(1)_(1), G^(1)_(1) - G^(4)_(4), '
              'G^(1)_(1) - G^(5)_(5) = %s H^2 (not a vacuum of Einstein gravity)'
              % (d14, d15, [str(v) for v in um3_diffs]))
    # ---------------- G11: the matrices of FD-13 in the definition of the fold carried by this docstring
    fd = __doc__[__doc__.index('BEGIN FOLD DEFINITION'):__doc__.index('END FOLD DEFINITION')]
    four = {}
    for name, body in re.findall(r'\b([st]_[123]) = \[([-0-9 ;]+)\]', fd):
        four[name] = sp.Matrix([[int(x) for x in row.split()] for row in body.split(';')])
    ok11 = len(four) == 6
    if ok11:
        Z4m, I4m, I8m = sp.zeros(4, 4), sp.eye(4), sp.eye(8)
        blk = lambda A, B, C, D: sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]).as_explicit())
        Xi = {0: I8m, 1: blk(Z4m, four['s_1'], four['s_1'], Z4m), 2: blk(Z4m, four['s_2'], four['s_2'], Z4m),
              3: blk(Z4m, four['s_3'], four['s_3'], Z4m), 4: blk(Z4m, four['t_3'], -four['t_3'], Z4m),
              5: blk(Z4m, four['t_2'], -four['t_2'], Z4m), 6: blk(Z4m, four['t_1'], -four['t_1'], Z4m)}
        Xi[7] = Xi[1] * Xi[2] * Xi[3] * Xi[4] * Xi[5] * Xi[6]
        sig8 = blk(Z4m, I4m, I4m, Z4m)
        Xibar = {0: I8m}
        for a_ in range(1, 8):
            Xibar[a_] = sig8 * Xi[a_].T * sig8
        Z8m = sp.zeros(8, 8)
        T_fd = {a_: blk(Z8m, Xibar[a_], Xi[a_], Z8m) for a_ in range(8)}
        ok11 = (all(T_fd[a_] == T[a_] for a_ in range(8)) and Xi[7] == sp.diag(-1, -1, -1, -1, 1, 1, 1, 1)
                and 'Xi_7 = Xi_1 Xi_2 Xi_3 Xi_4 Xi_5 Xi_6 = [[-1_4, 0], [0, 1_4]]' in fd)
    out['G11_matrices_read_from_FD13'] = sorted(four)
    rep.check('G11_fold_definition_matrices', ok11,
              'the six 4 x 4 matrices %s written out in FD-13 of the definition of the fold carried by this file, assembled into '
              'Xi_a, Xibar_a = sigma_8 Xi_a^T sigma_8 and T_a = [[0, Xibar_a], [Xi_a, 0]] as FD-13 says, give T16^A[0..7] of 4+4.nb '
              'entry by entry (Xi_7 = diag(-1_4, 1_4))' % ', '.join(sorted(four)))

    return write('geometry', 'um4_geometry.py', out, rep, __doc__)


if __name__ == '__main__':
    sys.exit(main())
