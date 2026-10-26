#!/usr/bin/env python3
"""um4_kohnsham.py - the self-consistent Kohn-Sham states of dirac16complex at the fold of UM-4: a homogeneous gas of the
particles chi (the long-lived resonances of um4_spectra.py) with its self-interaction, on the static block.

The orbitals of the gas (at rest along ordinary space, independent of the extra times), Psi = e^{(7/2)H|sigma|} chi(sigma)
e^{-i omega x4}, obey the bulk equation of dirac16complex with its self-interaction lambda_Psi (Psibar Psi) Psi in the mean-field
(Kohn-Sham) form, reduced to the hidden direction (units m_Psi = 1):
    chi' = gamma^(0) [ i omega e^{H|sigma|} gamma^(4) + 1 + M(sigma) ] chi            (sigma != 0),
    M(sigma) = lambda_Psi (n_s - N) = G e^{7H|sigma|} ( rho_hat(sigma) 1 - N_hat(sigma) ),
    rho_hat = (1/4) sum_k chibar_k chi_k,   N_hat = (1/4) sum_k chi_k chibar_k,   chibar = chi^dagger sigma16,
    chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-)                 (the fold),
with the four orbitals of the occupied level (Krein charge -1 each, energy E = -omega Q = omega), normalised with the measure of
UM-4, Q = int d sigma e^{H|sigma|} chi^dagger B chi = -1 (B = i sigma16 gamma^(4), the Krein operator), and the dimensionless
self-coupling G = lambda_Psi n_chi/V_* (n_chi the number density of chi on the fold, V_* the volume of the extra times).
gamma^(a) are the author's matrices T^(a) of 4+4.nb.  Two factors differ from UM-3: the energy omega is multiplied by
e^{H|sigma|} because the time is warped (the factor e^{H|sigma|} multiplies the whole Dirac operator of the fold, um4_geometry.py
G9), and the spin connection is removed by e^{(7/2)H|sigma|}, so that the proper scalar density is n_s = e^{7H|sigma|} chibar chi
(UM-3: e^{3H|sigma|} and e^{6H|sigma|}).  The Higgs portal closes a second loop: mu_L is proportional to v_loc^2 = v^2 -
c_Phi <Psibar P_L Psi>(0)/lambda: mu_L = mu_L0 (1 - kappa_H rho_hat_L(0)/rho_hat_L0(0)), kappa_H = c_Phi n_chi rho_hat_L0(0)/
(lambda v^2 V_*) < 0 (the Higgs portal alone binds the fold, c_Phi < 0, and rho_hat_L0(0) > 0).

The states are resonances (um4_spectra.py U3, U4): beyond the turning point sigma_t (omega e^{H sigma_t} = m_Psi + M) every
solution oscillates.  They live longer than 160 Gyr (11.6 times the age t_0 of the universe, the observed bound for a decay into
invisible particles, U6) only if m_Psi/H is large (U6: above 1135 for q_b = m_Psi/2 and 5911 for q_b = 0.3 m_Psi), so the
parameters here are mu_L = -0.6, mu_R = 0 (q_b = 0.3, omega_b = 0.954 in the limit H -> 0, as in UM-3) with H = 1e-4
(m_Psi/H = 1e4, q_b = 3000 H: a narrow resonance; the states of UM-3 with q_b of the order of H do not exist in UM-4, because
they would be broad resonances, not particles), and the box |sigma| <= L = 40 lies far inside the turning point
(sigma_t = 473): the orbital is computed in the box with the decaying solutions at its end; the exponentially small outgoing
part beyond sigma_t is the width (U4), not resolved here.  Inside the box the warped measure e^{7H|sigma|} differs from 1 by at
most 7HL = 0.028, so the box tests the mean field near the fold, not its behaviour near the turning point (K4, K5).

Symmetry reduction (as in UM-3).  The author's T_0..T_3 are symmetric and T_4..T_7 antisymmetric, so the rotations of
ordinary space (Sigma^{ij}) and of the extra times (Sigma^{rs}) form a compact group SU(2) x SU(2) of orthogonal matrices;
gamma^(0), gamma^(4), P_L, P_R, sigma16 and the Krein operator commute with it, and 16 = (2,2) x 4.  The four occupied orbitals
form one (2,2) multiplet, the mean field is invariant, and the problem reduces exactly to the 4-dimensional weight space W
(Sigma^{12} = Sigma^{56} = i/2).  The reduced solution is lifted back to the full multiplet and checked in sixteen dimensions.

Method (as in UM-3): shooting (classical RK4 on |sigma| <= L, the step written as a matrix for all grid points at once, the
solutions re-orthonormalised every eight steps), the occupied level as the zero of the Krein-signed matching residual,
Anderson mixing of the mean field, continuation in G.  The computation is split into four parts (K1, the regime I, the Higgs
loop K6 and the weakly bound point K9); every invocation of a part stops after at most 400 s (the standing rule: no individual
calculation longer than 423 s) and keeps a checkpoint after every completed step; the assembly reads the parts and makes the
checks.
Checks:
  K1  without the self-interaction: the shooting with the full 16 x 16 matrices gives eight degenerate states, four of each
      Krein sign, and the reduced problem the same level with two (one of each sign); the level equals omega_b (1 - H/(2 q_b))
      up to a term of the second order in H (the first-order effect of the warped energy, delta omega = -omega_b H <|sigma|>,
      with <|sigma|> = 1/(2 q_b) the mean distance from the fold of the bound profile; the difference is 4 times as large at
      2H); and the box method gives the real part of the exact resonance of um4_spectra.py (outgoing Hankel waves on both
      sides) at m_Psi/H = 200, mu_L = -1;
  K2  the self-consistent shift at small G equals first-order perturbation theory,
      delta omega = G int e^{7H|sigma|} (rho_hat^2 - tr N_hat^2) d sigma (= 2 E_int, E_int the interaction energy per particle);
      the occupied and the empty multiplets split at every G, in proportion to G (the second singular value of the matching at
      the occupied level divided by G is constant to 3 per cent up to G = 0.1);
  K3  every converged solution, lifted to sixteen dimensions, satisfies the Kohn-Sham equation, the fold matching and
      self-consistency (residuals), with Krein charge -1 for each of the four orbitals;
  K4  the dilute limit: delta omega ~ G^p with p = 1 for G <= 1e-4 (a test of the continuation in the box: in the box the
      weight e^{7H|sigma|} is close to 1, so the exponent of first-order perturbation theory is what the box must give);
  K5  the gas stays at the fold within the box: there the proper scalar density decays (its decay rate 2 kappa - 7H, kappa
      the local decay rate of the orbital, stays far above 7H = 7e-4 for every G computed), for the repulsive and for the attractive
      self-interaction (G = -1e-4, -1e-2 from the free state, which converge); beyond the box the orbital continues to decay
      up to the turning point and then leaves the fold as the outgoing wave of the width (U3 to U5): this check describes the
      box, not the asymptotic region;
  K6  the Higgs-portal loop converges jointly with the orbitals (kappa_H = -0.3, G = 0.1): the gas raises v_loc^2, mu_L becomes
      more negative and the level falls; the fold density rho_hat_L0(0) of the free orbital equals d omega_0/d mu_L
      (Hellmann-Feynman, the derivative computed by solving the level at mu_L +- 1e-4) to the accuracy of the trapezoidal
      normalisation on the grid;
  K7  the equation of state of the gas: energy per particle e = omega - E_int, pressure P = n E_int (also the pressure along
      the extra times, q = P); P/e -> 0 in the dilute limit (cold dark matter);
  K8  the repulsive mean field raises the level towards m_Psi, and the tunnelling exponent of the width,
      S = 2 [ int_0^L kappa_min d sigma + F(omega e^{HL})/H ] (kappa_min the smallest decay rate of the local equation with the
      self-consistent mean field, F(u) = ln((1 + sqrt(1 - u^2))/u) - sqrt(1 - u^2) for the free barrier beyond the box), falls
      with it: the width grows as the barrier shrinks and the gas leaks into the bulk.  For G -> 0, S equals 2 F(omega_r)
      m_Psi/H at the resonance omega_r = omega_b (1 - H/(2 q_b)), which exceeds 2 F(upsilon_b) m_Psi/H by exactly 1 (the factor
      1/e of the derived width of um4_spectra.py U4, Gamma = (2/e) (q_b/m_Psi)^2 m_Psi e^{-2 F(upsilon_b) m_Psi/H}, so that
      Gamma = 2 (q_b/m_Psi)^2 m_Psi e^{-S}); with this prefactor and H at its lower bound H_min of um4_propagators.py P5
      (m_Psi = 1e4 H_min) the gas lives longer than 160 Gyr only below a coupling G_life (in UM-3 the warped proper density
      saturated far from the fold and kept the state bound beyond omega = m_Psi; in UM-4 the energy is warped as well and the
      level approaches m_Psi from below while the orbital spreads into the barrier);
  K9  a weakly bound point (q_b = 0.03 m_Psi, q_b/omega_b = 0.03) and H = 1e-7 m_Psi: with H at its lower bound H_min this
      is m_Psi = 1e7 H_min = 2.5e10 GeV, above the smallest mass (1.6e10 GeV) for which the binding q_b = 0.03 m_Psi lives
      longer than 160 Gyr (the width of U4): the shooting gives the level omega_b (1 - H/(2 q_b)) up to the second order in H,
      and the self-consistent shift approaches first-order perturbation theory as G -> 0;
  K10 how dilute the gas of the universe is: G = lambda_Psi n_chi/V_* for the lightest chi that lives longer than 160 Gyr
      (um4_spectra.py U6 with H = H_min: omega_b = 2.49e6 GeV for q_b = m_Psi/2, 1.18e4 GeV for the strong binding
      q_b = 0.99 m_Psi) with the natural sizes lambda_Psi = m_Psi^-6, V_* = m_Psi^-3 (G = n_chi/m_Psi^3) and with extra times of
      the Planck size (V_* = M_Pl^-3), for the dark-matter density near the Sun and for the mean density today: far below the
      smallest computed coupling and below G_life of K8, so the gas is in the dilute limit and cold (w_chi = (P/e)/G times G).
Reads outputs/spectra.json (run um4_spectra.py first; the assembly uses its lower bound on H and its lifetimes).
Writes outputs/kohnsham_parts/*.json (the parts, not kept in the repository), outputs/kohnsham.json and
reports/kohnsham_checks.json.
Usage (repository root; repeat a part until it reports that it is complete, exit code 0; 3 means run it again):
    python universe_model_4/code/um4_kohnsham.py part K1     (and part I, part K6, part K9)
    python universe_model_4/code/um4_kohnsham.py assemble
    python universe_model_4/code/um4_kohnsham.py             (the status of the parts)

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
import signal
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import scipy.linalg as sla
from scipy.optimize import brentq, minimize_scalar

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
sys.path.insert(0, str(HERE))
import um4_gammas as GM  # noqa: E402


def numeric_mats():
    T = GM.T16A()
    eta = GM.eta4488()
    Tn = {a: np.array(T[a].tolist(), dtype=float) for a in range(9)}
    Tup = {a: float(eta[a, a]) * Tn[a] for a in range(8)}
    PL, PR = GM.projectors()
    return (Tn, Tup, np.array(PL.tolist(), dtype=float), np.array(PR.tolist(), dtype=float),
            np.array(GM.sigma16().tolist(), dtype=float))


TN, TUP, PLN, PRN, SIG = numeric_mats()
G0, G4 = TUP[0], TUP[4]
I16 = np.eye(16)
BKR = 1j * SIG @ G4          # the Krein operator


def sig(a, b):
    return 0.25 * (TUP[a] @ TUP[b] - TUP[b] @ TUP[a])


GENS = [sig(i, j) for i, j in ((1, 2), (1, 3), (2, 3), (5, 6), (5, 7), (6, 7))]
_X = GENS[0] + 2 * GENS[3]
_ev, _V = np.linalg.eig(_X)
QW, _ = np.linalg.qr(_V[:, np.abs(_ev - 1.5j) < 1e-8])      # the weight space W: Sigma^{12} = Sigma^{56} = i/2
ROT1 = sla.expm(np.pi * GENS[1])     # rotation by pi in the (1,3) plane: Sigma^{12} -> -Sigma^{12}
ROT2 = sla.expm(np.pi * GENS[4])     # rotation by pi in the (5,7) plane: Sigma^{56} -> -Sigma^{56}


def restrict(A):
    return QW.conj().T @ A @ QW


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def trap(f, h):
    return h * (0.5 * f[0] + f[1:-1].sum(axis=0) + 0.5 * f[-1])


def F_wkb(u):
    """F(u) = int_u^1 sqrt(1 - t^2)/t dt, the free barrier between the energy u e^{H sigma} and the turning point (times H)."""
    if u >= 1.0:
        return 0.0
    r = math.sqrt(1 - u * u)
    return math.log((1 + r) / u) - r


class Shooter:
    """Shooting for chi' = g0 (i w e^{H|sigma|} g4 + 1 + M(sigma)) chi in dimension d (16, or 4 for W) with the fold matching."""
    WMAX = 0.05      # the widest bracket (in units of m_Psi) searched around the expected level

    def __init__(self, H, muL, muR, L, h, d, qr_every=8):
        self.H, self.muL0, self.muL, self.muR = H, muL, muL, muR
        self.d = d
        if d == 16:
            self.g0, self.g4, self.pl, self.pr, self.sg, self.kr = G0, G4, PLN, PRN, SIG, BKR
        else:
            self.g0, self.g4, self.pl, self.pr, self.sg, self.kr = (restrict(X) for X in (G0, G4, PLN, PRN, SIG, BKR))
        self.n = int(round(L / h))
        self.h = L / self.n
        self.s = np.linspace(0.0, L, self.n + 1)
        self.ew = np.exp(H * self.s)                                   # e^{H|sigma|} at the grid points
        self.ewm = np.exp(H * 0.5 * (self.s[1:] + self.s[:-1]))         # and at the midpoints
        self.qr_every = qr_every
        z = np.zeros((self.n + 1, d, d), complex)
        self.M = {-1: z.copy(), 1: z.copy()}
        self._prep()

    def _prep(self):
        self.Tf = sla.expm(self.g0 @ (self.muL * self.pl + self.muR * self.pr))
        self.GM = {sd: np.einsum('ab,jbc->jac', self.g0, self.M[sd]) for sd in (-1, 1)}
        self.GMm = {sd: 0.5 * (self.GM[sd][1:] + self.GM[sd][:-1]) for sd in (-1, 1)}
        self.C04 = self.g0 @ self.g4

    def set_field(self, Ml, Mr, muL=None):
        self.M = {-1: Ml, 1: Mr}
        if muL is not None:
            self.muL = muL
        self._prep()

    def _base(self, w):
        """The matrix of the equation without the mean field, at the grid points and at the midpoints."""
        bg = 1j * w * self.ew[:, None, None] * self.C04[None] + self.g0[None]
        bm = 1j * w * self.ewm[:, None, None] * self.C04[None] + self.g0[None]
        return bg, bm

    def _start(self, w, side):
        """The decaying solutions at the far end |sigma| = L (orthonormal columns) and the matrices of the equation."""
        bg, bm = self._base(w)
        try:
            ev, V = np.linalg.eig(bg[self.n] + self.GM[side][self.n])
        except np.linalg.LinAlgError as exc:
            raise RuntimeError('no eigenvectors at the far end (%s)' % exc)
        sel = ev.real > 0 if side < 0 else ev.real < 0
        if sel.sum() != self.d // 2 or np.min(np.abs(ev.real)) < 1e-12:
            raise RuntimeError('no decaying subspace of half dimension at the far end (the turning point is inside the box)')
        Y, _ = np.linalg.qr(V[:, sel])
        return Y, (bg, bm)

    def _steps(self, base, side):
        """The classical fourth-order Runge-Kutta step of the linear equation Y' = K(sigma) Y as a matrix: Y_{j-1} = P[j-1] Y_j
        for the step from the grid point j to j - 1 (all n steps at once); K1, K2, K3 at s_j, s_{j-1/2}, s_{j-1}."""
        bg, bm = base
        dd = self.h if side < 0 else -self.h
        GMs = self.GM[side]
        K1 = bg[1:] + GMs[1:]
        K2 = bm + self.GMm[side]
        K3 = bg[:-1] + GMs[:-1]
        one = np.eye(self.d)
        A2 = K2 @ (one + 0.5 * dd * K1)
        A3 = K2 @ (one + 0.5 * dd * A2)
        A4 = K3 @ (one + dd * A3)
        return one + dd / 6.0 * (K1 + 2.0 * A2 + 2.0 * A3 + A4)

    def integrate(self, w, side):
        n, d = self.n, self.d
        Y, base = self._start(w, side)
        Ys = np.empty((n + 1, d, d // 2), complex)
        Rk = {}
        try:
            with np.errstate(over='raise', invalid='raise'):
                P = self._steps(base, side)
                Ys[n] = Y
                for j in range(n, 0, -1):
                    Y = P[j - 1] @ Y
                    if (j - 1) % self.qr_every == 0:
                        Y, R = np.linalg.qr(Y)
                        Rk[j - 1] = R
                    Ys[j - 1] = Y
        except (FloatingPointError, np.linalg.LinAlgError) as exc:
            raise RuntimeError('the integration overflows (%s)' % exc)
        if not np.isfinite(Ys).all():
            raise RuntimeError('the integration overflows')
        return Ys, Rk

    def integrate_end(self, w, side):
        n, q = self.n, self.qr_every
        Y, base = self._start(w, side)
        try:
            with np.errstate(over='raise', invalid='raise'):
                P = self._steps(base, side)
                r = n % q
                for j in range(n, n - r, -1):
                    Y = P[j - 1] @ Y
                if r:
                    Y, _ = np.linalg.qr(Y)
                nb = (n - r) // q
                B = P[:n - r].reshape(nb, q, self.d, self.d)
                while B.shape[1] > 1:
                    if B.shape[1] % 2:
                        B = np.concatenate([B[:, :-2], (B[:, -2] @ B[:, -1])[:, None]], axis=1)
                        continue
                    B = B[:, 0::2] @ B[:, 1::2]
                B = B[:, 0]
                for m in range(nb - 1, -1, -1):
                    Y, _ = np.linalg.qr(B[m] @ Y)
        except (FloatingPointError, np.linalg.LinAlgError) as exc:
            raise RuntimeError('the integration overflows (%s)' % exc)
        if not np.isfinite(Y).all():
            raise RuntimeError('the integration overflows')
        return Y

    def match(self, w, full=True):
        if not full:
            return np.hstack([self.integrate_end(w, 1), -self.Tf @ self.integrate_end(w, -1)]), None
        Yl, Rl = self.integrate(w, -1)
        Yr, Rr = self.integrate(w, 1)
        return np.hstack([Yr[0], -self.Tf @ Yl[0]]), (Yl, Rl, Yr, Rr)

    def sv(self, w):
        return np.linalg.svd(self.match(w, full=False)[0], compute_uv=False)[::-1]

    def reconstruct(self, Ys, Rk, c0):
        out = np.empty((self.n + 1, self.d), complex)
        c = c0.copy()
        for j in range(self.n + 1):
            out[j] = Ys[j] @ c
            if j in Rk:
                c = np.linalg.solve(Rk[j], c)
        return out

    def null_orbitals(self, w, k):
        A, (Yl, Rl, Yr, Rr) = self.match(w)
        U, s, Vh = np.linalg.svd(A)
        order = np.argsort(s)
        null = Vh.conj().T[:, order[:k]]
        half = self.d // 2
        return ([(self.reconstruct(Yl, Rl, null[half:, kk]), self.reconstruct(Yr, Rr, null[:half, kk])) for kk in range(k)],
                np.sort(s))

    def gram(self, orbs, op):
        """The Gram matrix of op with the measure e^{H|sigma|} d sigma of the Krein charge of UM-4."""
        n = len(orbs)
        Gm = np.zeros((n, n), complex)
        for a in range(n):
            for b in range(n):
                fl = np.einsum('ji,ik,jk->j', orbs[a][0].conj(), op, orbs[b][0]) * self.ew
                fr = np.einsum('ji,ik,jk->j', orbs[a][1].conj(), op, orbs[b][1]) * self.ew
                Gm[a, b] = trap(fl, self.h) + trap(fr, self.h)
        return 0.5 * (Gm + Gm.conj().T)

    def krein_split(self, w, k):
        """The k orbitals of the null space at w combined into Krein-orthonormal ones: (negative, positive, eigenvalues, s)."""
        orbs, s = self.null_orbitals(w, k)
        Gk = self.gram(orbs, self.kr)
        ev, R = np.linalg.eigh(Gk)
        neg, pos = [], []
        for kk in range(len(ev)):
            c = R[:, kk] / math.sqrt(abs(ev[kk]))
            o = (sum(c[a] * orbs[a][0] for a in range(len(orbs))), sum(c[a] * orbs[a][1] for a in range(len(orbs))))
            (neg if ev[kk] < 0 else pos).append(o)
        return neg, pos, ev, s

    def fneg(self, w):
        """The squared residual of the best matching vector with negative Krein norm: zero exactly at the occupied
        (Krein-negative) level; the Krein norm of a bound state is estimated from its values at the fold (where e^{H|sigma|} = 1),
        within the two-dimensional near-null space."""
        Yr0, Yl0 = self.integrate_end(w, 1), self.integrate_end(w, -1)
        A = np.hstack([Yr0, -self.Tf @ Yl0])
        U, s, Vh = np.linalg.svd(A)
        V = Vh.conj().T
        order = np.argsort(s)
        V2 = V[:, order[:2]]
        h2 = self.d // 2
        P = np.zeros((self.d, self.d), complex)
        P[:h2, :h2] = Yr0.conj().T @ self.kr @ Yr0
        P[h2:, h2:] = Yl0.conj().T @ self.kr @ Yl0
        S2 = np.diag(np.sort(s)[:2] ** 2).astype(complex)
        P2 = V2.conj().T @ P @ V2
        P2 = 0.5 * (P2 + P2.conj().T)
        mu, X = np.linalg.eig(np.linalg.solve(P2, S2))
        best = np.inf
        for kk in range(2):
            x = X[:, kk]
            pn = float((x.conj() @ P2 @ x).real)
            if pn < 0:
                best = min(best, float((x.conj() @ S2 @ x).real) / abs(pn))
        return best

    def level(self, w_guess, width, thresh=1e-7):
        """The occupied (Krein-negative) level near w_guess, confirmed by the Krein charge of the orbital."""
        def g(dx):
            if w_guess + dx <= 0.0:
                return 1e3
            try:
                f = self.fneg(w_guess + dx)
            except (RuntimeError, np.linalg.LinAlgError):
                return 1e3
            return math.sqrt(max(f, 0.0)) if math.isfinite(f) else 1e3
        width = min(width, self.WMAX)
        for _ in range(8):
            w = w_guess + float(minimize_scalar(g, bounds=(-width, width), method='bounded',
                                                options={'xatol': 1e-16, 'maxiter': 2000}).x)
            try:
                s = self.sv(w)
                found = math.isfinite(self.fneg(w)) and s[0] < thresh
            except (RuntimeError, np.linalg.LinAlgError):
                found = False
            if found:
                break
            if width >= self.WMAX:
                raise RuntimeError('no Krein-negative level within %.2f of %.12f' % (self.WMAX, w_guess))
            width = min(10 * width, self.WMAX)
        else:
            raise RuntimeError('no Krein-negative level near %.12f' % w_guess)
        k = max(1, int(np.sum(s < thresh)))
        try:
            neg, pos, ev, s2 = self.krein_split(w, k)
        except np.linalg.LinAlgError as exc:
            raise RuntimeError('no Krein-negative level near %.12f (%s)' % (w_guess, exc))
        if len(neg) != 1:
            raise RuntimeError('no Krein-negative level near %.12f (Krein eigenvalues %s)' % (w_guess, ev))
        return w, neg[0], ev, s2


def densities_W(sh, xi):
    """rho_hat, N_hat restricted to W and the left-handed scalar density, from the W-orbital xi = (left, right)."""
    out = {}
    for side, idx in ((-1, 0), (1, 1)):
        x = xi[idx]
        rho = np.einsum('ji,ik,jk->j', x.conj(), sh.sg, x).real
        Nh = 0.25 * np.einsum('ji,jk,kl->jil', x, x.conj(), sh.sg)
        rhoL = np.einsum('ji,ik,jk->j', x.conj(), sh.sg @ sh.pl, x).real
        out[side] = (rho, Nh, rhoL)
    return out


def field_W(sh, dens, G, cap):
    F = {}
    capped = False
    for side in (-1, 1):
        rho, Nh, _ = dens[side]
        wgt = G * np.exp(7 * sh.H * sh.s)
        M = wgt[:, None, None] * (rho[:, None, None] * np.eye(sh.d)[None] - Nh)
        nrm = np.linalg.norm(M, axis=(1, 2))
        scale = np.minimum(1.0, cap / np.maximum(nrm, 1e-300))
        F[side] = M * scale[:, None, None]
        capped = capped or bool((scale < 1).any())
    return F, capped


def lift(xi):
    """The four orbitals of the (2,2) multiplet in sixteen dimensions: Q_W xi and its rotations by pi."""
    out = []
    for R in (I16, ROT1, ROT2, ROT1 @ ROT2):
        out.append((xi[0] @ QW.T @ R.T, xi[1] @ QW.T @ R.T))
    return out


def full_residuals(sh, w, occ16, G):
    """Residuals of the sixteen-dimensional problem for the lifted orbitals: the mean field rebuilt in sixteen
    dimensions, the Kohn-Sham equation (central differences), the fold matching, the Krein charges and orthogonality."""
    Tf16 = sla.expm(G0 @ (sh.muL * PLN + sh.muR * PRN))
    res_ode, res_match = 0.0, 0.0
    M16 = {}
    for side, idx in ((-1, 0), (1, 1)):
        chis = np.array([o[idx] for o in occ16])
        rho = np.einsum('kji,il,kjl->j', chis.conj(), SIG, chis).real / 4
        Nh = np.einsum('kji,kjl,lm->jim', chis, chis.conj(), SIG) / 4
        M16[side] = G * np.exp(7 * sh.H * sh.s)[:, None, None] * (rho[:, None, None] * I16[None] - Nh)
    for o in occ16:
        for side, idx in ((-1, 0), (1, 1)):
            chi = o[idx]
            dsig = -sh.h if side < 0 else sh.h
            dchi = (chi[2:] - chi[:-2]) / (2 * dsig)
            K = np.einsum('ab,jbc->jac', G0, 1j * w * sh.ew[1:-1, None, None] * G4[None] + I16[None] + M16[side][1:-1])
            rhs = np.einsum('jab,jb->ja', K, chi[1:-1])
            res_ode = max(res_ode, float(np.abs(dchi - rhs).max() / np.abs(rhs).max()))
        res_match = max(res_match, float(np.linalg.norm(o[1][0] - Tf16 @ o[0][0]) / np.linalg.norm(o[1][0])))
    charges = [float(sum(trap(np.einsum('ji,ik,jk->j', o[i].conj(), BKR, o[i]).real * sh.ew, sh.h) for i in (0, 1)))
               for o in occ16]
    off = 0.0
    for a in range(4):
        for b in range(a + 1, 4):
            v = sum(trap(np.einsum('ji,ik,jk->j', occ16[a][i].conj(), BKR, occ16[b][i]) * sh.ew, sh.h) for i in (0, 1))
            off = max(off, abs(v))
    return res_ode, res_match, charges, float(off)


def tunnelling_exponent(sh, w):
    """S = 2 [int_0^L kappa_min d sigma + F(w e^{HL})/H]: kappa_min the smallest decay rate of the local equation with the
    mean field held by sh (the larger of the two sides at each point is not needed: the field is the same on both sides up to
    the matching), F the free barrier from the end of the box to the turning point."""
    kap = np.empty(sh.n + 1)
    for j in range(sh.n + 1):
        K = 1j * w * sh.ew[j] * sh.C04 + sh.g0 + sh.GM[1][j]
        ev = np.linalg.eigvals(K)
        kap[j] = float(np.min(np.abs(ev.real)))
    inside = float(trap(kap, sh.h))
    u_end = w * float(sh.ew[-1])
    beyond = F_wkb(u_end) / sh.H
    return 2 * (inside + beyond), 2 * inside, 2 * beyond


ANDERSON_DEPTH = 6


def solve(sh, G, w_start, kappaH=0.0, rhoL0=None, beta=0.5, depth=None, tol=1e-8, maxit=150, cap=20.0, width=0.02, trace=None):
    """Iterate the reduced Kohn-Sham problem to self-consistency at coupling G with Anderson mixing of the mean field
    (and of mu_L for the Higgs loop).  sh keeps its field (continuation in G)."""
    def pack(Ml, Mr, mu):
        return np.concatenate([Ml.ravel(), Mr.ravel(), [mu]])

    def unpack(x):
        n = (x.size - 1) // 2
        return x[:n].reshape(sh.M[-1].shape), x[n:2 * n].reshape(sh.M[1].shape), float(x[-1].real)
    depth = ANDERSON_DEPTH if depth is None else depth
    x = pack(sh.M[-1], sh.M[1], sh.muL)
    Xh, Rh = [], []
    w = w_start
    retries = 0
    hist = []
    best = (np.inf, -1, None)
    for it in range(maxit):
        Ml, Mr, mu = unpack(x)
        sh.set_field(Ml, Mr, mu)
        try:
            w_new, xi, kev, s = sh.level(w, width)
        except (RuntimeError, np.linalg.LinAlgError) as exc:
            if Xh and retries < 4:
                retries += 1
                x = Xh[-1] + 0.25 * beta * Rh[-1]
                Xh, Rh = Xh[-1:], Rh[-1:]
                width = max(width, 1e-3)
                continue
            return {'converged': False, 'reason': str(exc), 'G': G, 'iterations': it}
        dens = densities_W(sh, xi)
        F, capped = field_W(sh, dens, G, cap)
        mu_t = sh.muL
        if kappaH != 0.0:
            rhoL_fold = 0.5 * (dens[-1][2][0] + dens[1][2][0])
            mu_t = sh.muL0 * (1.0 - kappaH * rhoL_fold / rhoL0)
        f = pack(F[-1], F[1], mu_t)
        r = f - x
        rn = float(np.abs(r).max() / max(1e-300, np.abs(f[:-1]).max()))
        hist.append((float(w_new), rn))
        if trace is not None:
            trace.append((it, float(w_new), rn))
        if rn < best[0]:
            best = (rn, it, x.copy())
        Xh.append(x.copy())
        Rh.append(r.copy())
        if len(Xh) > depth + 1:
            Xh.pop(0)
            Rh.pop(0)
        if len(Xh) >= 2:
            dX = np.array([Xh[i + 1] - Xh[i] for i in range(len(Xh) - 1)]).T
            dR = np.array([Rh[i + 1] - Rh[i] for i in range(len(Rh) - 1)]).T
            gam = np.linalg.lstsq(dR, r, rcond=None)[0]
            x = x + beta * r - (dX + beta * dR) @ gam
        else:
            x = x + beta * r
        Ml, Mr, mu = unpack(x)
        x = pack(*(M * np.minimum(1.0, cap / np.maximum(np.linalg.norm(M, axis=(1, 2)), 1e-300))[:, None, None]
                   for M in (Ml, Mr)), mu)
        dw = w_new - w
        w = w_new
        width = max(10 * abs(dw), 1e-9)
        if it > 2 and rn < tol and abs(dw) < 1e-10:
            break
        if best[0] < 1e-7 and it - best[1] >= 15:
            x = best[2]
            break
    else:
        if not best[0] < 1e-7:
            return {'converged': False, 'reason': 'no convergence in %d iterations (smallest residual %.1e)' % (maxit, best[0]),
                    'G': G, 'omega': w, 'history': hist[-5:]}
        x = best[2]
    Ml, Mr, mu = unpack(x)
    sh.set_field(Ml, Mr, mu)
    try:
        w, xi, kev, s = sh.level(w, max(width, 1e-9))
    except (RuntimeError, np.linalg.LinAlgError) as exc:
        return {'converged': False, 'reason': str(exc), 'G': G}
    dens = densities_W(sh, xi)
    F, capped = field_W(sh, dens, G, cap)
    selfcons = max(np.abs(F[-1] - sh.M[-1]).max(), np.abs(F[1] - sh.M[1]).max()) / max(1e-300, np.abs(F[1]).max())
    occ16 = lift(xi)
    res_ode, res_match, charges, off = full_residuals(sh, w, occ16, G)
    eint = 0.0
    for side in (-1, 1):
        rho, Nh, _ = dens[side]
        trN2 = 4.0 * np.einsum('jab,jba->j', Nh, Nh).real          # tr over sixteen dimensions = 4 x tr over W
        eint += 0.5 * G * trap(np.exp(7 * sh.H * sh.s) * (rho ** 2 - trN2), sh.h)
    rho_r = dens[1][0]
    jfar = int(0.85 * sh.n)
    k5 = max(5, int(1.0 / sh.h))
    rate = float(-(np.log(abs(rho_r[jfar + k5])) - np.log(abs(rho_r[jfar - k5]))) / (2 * k5 * sh.h))
    S, S_in, S_out = tunnelling_exponent(sh, w)
    return {'converged': True, 'G': G, 'omega': float(w), 'iterations': it + 1, 'krein_eig': [float(x) for x in kev],
            'singular_values': [float(x) for x in s], 'E_int_per_particle': float(eint),
            'energy_per_particle': float(w - eint), 'pressure_over_energy': float(eint / (w - eint)),
            'residual_KS_ode_16': res_ode, 'residual_fold_matching_16': res_match, 'residual_selfconsistency': float(selfcons),
            'krein_charges_16': charges, 'krein_offdiagonal_16': off, 'capped': capped, 'muL': float(sh.muL),
            'scalar_density_decay_rate_far': rate,
            'proper_density_decay_rate_far': rate - 7 * sh.H,
            'proper_density_far': float(G * math.exp(7 * sh.H * sh.s[jfar]) * rho_r[jfar]),
            'mean_field_norm_max': float(max(np.linalg.norm(sh.M[sd], axis=(1, 2)).max() for sd in (-1, 1))),
            'rhoL_fold': float(0.5 * (dens[-1][2][0] + dens[1][2][0])),
            'tunnelling_exponent_S': S, 'S_inside_box': S_in, 'S_beyond_box': S_out, 'S_times_H': S * sh.H,
            'free_barrier_2F': 2 * F_wkb(w)}


def first_order_shift(sh16, w):
    """delta omega / G from first-order perturbation theory with the four Krein-negative orbitals of the level of eight
    degenerate states (normalised with the measure e^{H|sigma|} d sigma)."""
    neg, pos, ev, s = sh16.krein_split(w, 8)
    tot = 0.0
    for side, idx in ((-1, 0), (1, 1)):
        chis = np.array([o[idx] for o in neg])
        rho = np.einsum('kji,il,kjl->j', chis.conj(), SIG, chis).real / 4
        Nh = np.einsum('kji,kjl,lm->jim', chis, chis.conj(), SIG) / 4
        trN2 = np.einsum('jab,jba->j', Nh, Nh).real
        tot += trap(np.exp(7 * sh16.H * sh16.s) * (rho ** 2 - trN2), sh16.h)
    return tot, len(neg)


TARGETS = [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
H_MAIN, L_MAIN, H_STEP = 1e-4, 40.0, 0.03
# (H, the box L, the step h).  The free orbital decays as e^{-q_b |sigma|} with q_b = 0.3: at the end of the box it is e^{-12}
# of its value at the fold, its density e^{-24}; the turning point of the free level (omega = 0.95378) lies at sigma_t = ln(1/omega)/H = 473.
MU_L, MU_R = -0.6, 0.0
OMEGA_STOP = 0.99      # the continuation in G stops once the level exceeds this (the orbital spreads towards the end of the box)


def regime_sequence():
    """The couplings of the continuation: the targets 1e-6 ... 0.1, then steps of 0.05 to 0.5 (the continuation stops before,
    once omega > OMEGA_STOP or the level search fails)."""
    return TARGETS + [round(0.1 + 0.05 * k, 2) for k in range(1, 9)]


MIXINGS = ((0.5, 6), (0.2, 10))


def step_to(sh, G, Gprev, w, attempts=12):
    """Continue the converged state held by sh at Gprev (level w) to G; where a step fails, the state is restored and an
    intermediate coupling (the geometric midpoint) is solved first.  Returns the result at G and the inserted results."""
    saved = (sh.M[-1].copy(), sh.M[1].copy(), sh.muL)
    lo, wlo, hi = Gprev, w, G
    inserted = []
    r = None
    for _ in range(attempts):
        order = getattr(sh, 'mix_order', list(MIXINGS))
        for mix in order:
            try:
                r = solve(sh, hi, wlo, beta=mix[0], depth=mix[1])
            except (RuntimeError, np.linalg.LinAlgError, FloatingPointError) as exc:
                r = {'converged': False, 'reason': repr(exc), 'G': hi}
            if r.get('converged'):
                r['mixing'] = list(mix)
                sh.mix_order = [mix] + [m for m in order if m != mix]
                break
            sh.set_field(*saved)
        if r.get('converged'):
            if hi == G:
                return r, inserted
            inserted.append(r)
            lo, wlo, hi = hi, r['omega'], G
            saved = (sh.M[-1].copy(), sh.M[1].copy(), sh.muL)
            continue
        sh.set_field(*saved)
        hi = math.sqrt(lo * hi) if lo > 0 else hi / 3
    return r, inserted


PARTS_DIR = UM4 / 'outputs' / 'kohnsham_parts'
PART_NAMES = ('K1', 'I', 'K6', 'K9')
HARD_LIMIT = 400      # seconds: no individual calculation may run longer than 423 s (the standing rule)
SOFT_BUDGET = 240     # no new step of a part is started after this many seconds
SNAPSHOT_G = (0.01, 0.1, 0.2, 0.3)   # couplings whose self-consistent mean field is kept for um4_krein.py


class TimeUp(Exception):
    """The hard time limit of one invocation was reached."""


def _alarm(signum, frame):
    raise TimeUp()


def _save_json(path, data):
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(data, indent=1, sort_keys=True, default=str) + '\n')
    tmp.replace(path)


def _state_paths(tag):
    return PARTS_DIR / ('%s.state.json' % tag), PARTS_DIR / ('%s.state.npz' % tag)


def _save_state(tag, sh, st):
    js, nz = _state_paths(tag)
    tmp = nz.with_name(nz.name + '.tmp')
    with open(tmp, 'wb') as f:
        np.savez(f, Ml=sh.M[-1], Mr=sh.M[1])
    tmp.replace(nz)
    st['muL'] = float(sh.muL)
    st['mix_order'] = [list(m) for m in sh.mix_order] if hasattr(sh, 'mix_order') else None
    _save_json(js, st)


def _load_state(tag, sh):
    js, nz = _state_paths(tag)
    if not js.exists():
        return None
    st = json.loads(js.read_text())
    with np.load(nz) as z:
        sh.set_field(z['Ml'].copy(), z['Mr'].copy(), st['muL'])
    if st.get('mix_order') is not None:
        sh.mix_order = [tuple(m) for m in st['mix_order']]
    return st


def _drop_state(tag):
    for q in _state_paths(tag):
        if q.exists():
            q.unlink()


def free_level(sh, wb, k):
    """The level of the free problem held by sh (no mean field) near wb: the minimum of the sum of the k smallest singular
    values of the matching."""
    def fk(dx):
        try:
            return float(np.sum(sh.sv(wb + dx)[:k]))
        except (RuntimeError, np.linalg.LinAlgError):
            return 1e3                    # beyond the frequency at which the end of the box is classically allowed
    wid = min(2e-3, 0.5 * (math.exp(-sh.H * sh.s[-1]) - wb))
    return wb + float(minimize_scalar(fk, bounds=(-wid, wid), method='bounded', options={'xatol': 1e-16, 'maxiter': 2000}).x)


def regime_part(t0):
    """The continuation in G, then the two attractive couplings from the free state; checkpointed after every step."""
    final = PARTS_DIR / 'regime_I.json'
    if final.exists():
        return True
    Hv, L, h = H_MAIN, L_MAIN, H_STEP
    qb = -MU_L / 2
    wb = math.sqrt(1 - qb * qb)
    w0 = wb * (1 - Hv / (2 * qb))
    keys = ('converged', 'omega', 'iterations', 'residual_KS_ode_16', 'residual_selfconsistency',
            'proper_density_decay_rate_far', 'S_times_H', 'capped', 'reason')
    tag = 'regime_I'
    sh = Shooter(Hv, MU_L, MU_R, L, h, 4)
    st = _load_state(tag, sh)
    if st is None:
        sh16 = Shooter(Hv, MU_L, MU_R, L, h, 16)
        w16 = free_level(sh16, w0, 8)
        pt, _ = first_order_shift(sh16, w16)
        st = {'pt': pt, 'w0': w16, 'w': w16, 'Gprev': 0.0, 'next': 0, 'stopped': False, 'stop_reason': None, 'rows': [],
              'path': [], 'log': [], 'neg_rows': [], 'seconds': time.time() - t0}
        _save_state(tag, sh, st)
    seq = regime_sequence()
    pt, w0 = st['pt'], st['w0']
    while st['next'] < len(seq) and not st['stopped']:
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = seq[st['next']]
        r, inserted = step_to(sh, G, st['Gprev'], st['w'])
        for x in inserted + [r]:
            x['first_order_prediction'] = w0 + pt * x['G']
            st['path'].append({k: x.get(k) for k in ('G', 'converged', 'omega', 'iterations', 'reason')})
            print('progress: regime I G = %.3g converged %s omega = %s, %s iterations (%.0f s)' % (
                x['G'], x.get('converged'), x.get('omega'), x.get('iterations'), time.time() - t0), flush=True)
            x['target'] = x['G'] in TARGETS
            if x is r and x.get('converged') and x['G'] in SNAPSHOT_G:
                with open(PARTS_DIR / ('snapshot_I_G%g.npz' % x['G']), 'wb') as f:
                    np.savez(f, Ml=sh.M[-1], Mr=sh.M[1], muL=sh.muL, omega=x['omega'], G=x['G'], H=Hv, L=L, h=h)
            st['rows'].append(x)
            st['log'].append('  regime I G=%.3g: %s' % (x['G'], {k: x.get(k) for k in keys}))
        if r.get('converged'):
            st['w'], st['Gprev'] = r['omega'], G
            if r['omega'] > OMEGA_STOP:
                st['stopped'], st['stop_reason'] = True, 'omega = %.6f > %.2f' % (r['omega'], OMEGA_STOP)
        else:
            st['stopped'], st['stop_reason'] = True, 'no convergence at G = %g: %s' % (G, r.get('reason'))
        st['next'] += 1
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    while len(st['neg_rows']) < 2:
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = (-1e-4, -1e-2)[len(st['neg_rows'])]
        sh2 = Shooter(Hv, MU_L, MU_R, L, h, 4)
        try:
            r = solve(sh2, G, w0)
        except TimeUp:
            raise
        except Exception as exc:
            r = {'converged': False, 'reason': str(exc), 'G': G}
        st['neg_rows'].append(r)
        st['log'].append('  regime I G=%g: %s' % (G, {k: r.get(k) for k in ('converged', 'omega', 'reason', 'capped')}))
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    _save_json(final, {'H': Hv, 'L': L, 'h': h, 'omega_free': w0, 'first_order_dw_over_G': pt, 'positive_G': st['rows'],
                       'negative_G': st['neg_rows'], 'continuation_path': st['path'], 'log': st['log'],
                       'stop_reason': st['stop_reason'], 'seconds': st['seconds'], 'definition_of_the_fold': fold_definition()})
    _drop_state(tag)
    return True


def k9_part(t0):
    """K9: the Kohn-Sham states at mu_L = -0.06 (q_b = 0.03), H = 1e-7, L = 500, h = 0.25; checkpointed."""
    final = PARTS_DIR / 'K9.json'
    if final.exists():
        return True
    muL, muR, Hv, L, h = -0.06, 0.0, 1e-7, 500.0, 0.25
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)
    w0 = wb * (1 - Hv / (2 * qb))
    tag = 'K9'
    sh = Shooter(Hv, muL, muR, L, h, 4)
    st = _load_state(tag, sh)
    if st is None:
        ts = time.time()
        sh16 = Shooter(Hv, muL, muR, L, h, 16)
        w16 = free_level(sh16, w0, 8)
        pt, nneg = first_order_shift(sh16, w16)
        w2 = free_level(Shooter(2 * Hv, muL, muR, L, h, 4), wb * (1 - 2 * Hv / (2 * qb)), 2)
        st = {'w16': w16, 'pt': pt, 'nneg': nneg, 'rows': [], 'w': w16, 'w_2H': w2, 'seconds': time.time() - ts}
        _save_state(tag, sh, st)
    couplings = (1e-4, 1e-3, 1e-2)
    while len(st['rows']) < len(couplings):
        if time.time() - t0 > SOFT_BUDGET:
            return False
        ts = time.time()
        G = couplings[len(st['rows'])]
        r = solve(sh, G, st['w'])
        r['ratio_to_first_order'] = (r['omega'] - st['w16']) / (st['pt'] * G) if r.get('converged') else None
        st['rows'].append(r)
        if r.get('converged'):
            st['w'] = r['omega']
        st['seconds'] += time.time() - ts
        _save_state(tag, sh, st)
    _save_json(final, {'muL': muL, 'H': Hv, 'q_b': qb, 'omega_b_flat': wb, 'omega_first_order_in_H': w0, 'omega_16': st['w16'],
                       'omega_W_at_2H': st['w_2H'], 'omega_first_order_at_2H': wb * (1 - 2 * Hv / (2 * qb)),
                       'first_order_dw_over_G': st['pt'], 'krein_negative_orbitals': st['nneg'],
                       'q_b_over_omega_b': qb / wb, 'free_barrier_2F_per_unit_m_over_H': 2 * F_wkb(st['w16']),
                       'rows': st['rows'], 'seconds': st['seconds'], 'definition_of_the_fold': fold_definition()})
    _drop_state(tag)
    return True


KAPPA_H = -0.3      # the test value of the Higgs loop; negative, the sign that the attractive Higgs portal implies (K6)


def higgs_loop(kappaH=KAPPA_H, G=0.1):
    """K6: the Kohn-Sham states with the Higgs-portal loop closed (kappa_H = -0.3, G = 0.1), from the free state; and the
    derivative d omega_0/d mu_L of the free level (Hellmann-Feynman)."""
    qb = -MU_L / 2
    wb = math.sqrt(1 - qb * qb)
    w0 = wb * (1 - H_MAIN / (2 * qb))
    sh = Shooter(H_MAIN, MU_L, MU_R, L_MAIN, H_STEP, 4)
    wfree = free_level(sh, w0, 2)
    negW0, _, _, _ = sh.krein_split(wfree, 2)
    d0 = densities_W(sh, negW0[0])
    rhoL0 = 0.5 * (d0[-1][2][0] + d0[1][2][0])
    dmu = 1e-4
    wl = []
    for s_ in (1, -1):
        sh2 = Shooter(H_MAIN, MU_L + s_ * dmu, MU_R, L_MAIN, H_STEP, 4)
        q2 = -(MU_L + s_ * dmu) / 2
        wl.append(free_level(sh2, math.sqrt(1 - q2 * q2) * (1 - H_MAIN / (2 * q2)), 2))
    dw_dmu = (wl[0] - wl[1]) / (2 * dmu)
    res = solve(sh, G, wfree, kappaH=kappaH, rhoL0=rhoL0)
    return res, float(rhoL0), float(dw_dmu), float(wfree)


def k6_part(t0):
    final = PARTS_DIR / 'K6.json'
    if final.exists():
        return True
    rH, rhoL0, dw_dmu, wfree = higgs_loop()
    _save_json(final, {'solution': rH, 'rhoL0': rhoL0, 'domega_dmuL': dw_dmu, 'omega_free': wfree,
                       'seconds': time.time() - t0, 'definition_of_the_fold': fold_definition()})
    return True


def k1_part(t0):
    """K1: the free level with the full 16 x 16 matrices and reduced to W; the box method against the exact resonance."""
    final = PARTS_DIR / 'K1.json'
    if final.exists():
        return True
    muL, muR = MU_L, MU_R
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)
    w_first = wb * (1 - H_MAIN / (2 * qb))
    sh16 = Shooter(H_MAIN, muL, muR, L_MAIN, H_STEP, 16)
    w16 = free_level(sh16, w_first, 8)
    s16 = sh16.sv(w16)
    neg, pos, ev16, _ = sh16.krein_split(w16, 8)
    shW = Shooter(H_MAIN, muL, muR, L_MAIN, H_STEP, 4)
    wW = free_level(shW, w_first, 2)
    sW = shW.sv(wW)
    negW, posW, evW, _ = shW.krein_split(wW, 2)
    # the second order in H: the level at 2H
    shW2 = Shooter(2 * H_MAIN, muL, muR, L_MAIN, H_STEP, 4)
    w_first2 = wb * (1 - 2 * H_MAIN / (2 * qb))
    wW2 = free_level(shW2, w_first2, 2)
    # the box method against the exact resonance: m_Psi/H = 200, mu_L = -1, mu_R = 0 (um4_spectra.py U3)
    import um4_spectra as SP
    nu, muLv = 200, -1.0
    root, wb2 = SP.resonance(nu, muLv, 0.0, 1, dps=40)
    w_res = complex(root) / nu                       # in units of m_Psi
    shV = Shooter(1.0 / nu, muLv, 0.0, 20.0, 0.02, 4)
    w_box = free_level(shV, w_res.real, 2)
    _save_json(final, {'omega_flat': wb, 'omega_first_order_in_H': w_first, 'omega_16': w16, 'omega_W': wW,
                       'sv16': [float(x) for x in s16[:9]], 'svW': [float(x) for x in sW], 'krein16': [len(neg), len(pos)],
                       'kreinW': [len(negW), len(posW)], 'omega_W_at_2H': wW2, 'omega_first_order_at_2H': w_first2,
                       'validation': {'m_over_H': nu, 'mu_L': muLv, 'resonance_omega_r': w_res.real, 'resonance_Gamma': -2 * w_res.imag,
                                      'box_level': w_box, 'box_L': 20.0, 'box_h': 0.02, 'omega_flat': wb2 / nu},
                       'seconds': time.time() - t0, 'definition_of_the_fold': fold_definition()})
    return True


def run_part(name):
    PARTS_DIR.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(HARD_LIMIT)
    try:
        if name == 'K1':
            return k1_part(t0)
        if name == 'I':
            return regime_part(t0)
        if name == 'K6':
            return k6_part(t0)
        if name == 'K9':
            return k9_part(t0)
        raise SystemExit('unknown part %s (parts: %s)' % (name, ', '.join(PART_NAMES)))
    except TimeUp:
        print('part %s reached the time limit of %d s; its last checkpoint is kept, run it again' % (name, HARD_LIMIT),
              flush=True)
        return False
    finally:
        signal.alarm(0)


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def part_file(n):
    return PARTS_DIR / (('regime_%s.json' % n) if n == 'I' else (n + '.json'))


def assemble():
    t0 = time.time()
    missing = [n for n in PART_NAMES if not part_file(n).exists()]
    if missing:
        print('parts not yet complete: %s (run: python universe_model_4/code/um4_kohnsham.py part NAME)' % ', '.join(missing))
        return 2
    part = {n: json.loads(part_file(n).read_text()) for n in PART_NAMES}
    rep = Report()
    out = {'units': 'm_Psi = 1', 'muL': MU_L, 'muR': MU_R, 'H': H_MAIN, 'L': L_MAIN, 'h': H_STEP}
    muL = MU_L
    qb = -muL / 2
    wb = math.sqrt(1 - qb * qb)

    sym = {'T0..T3 symmetric': all(np.allclose(TN[a], TN[a].T) for a in range(4)),
           'T4..T7 antisymmetric': all(np.allclose(TN[a], -TN[a].T) for a in range(4, 8)),
           'commutant contains g0, g4, P_L, sigma16, Krein': all(np.allclose(X @ g, g @ X) for X in (G0, G4, PLN, SIG, BKR) for g in GENS),
           'dim W': int(QW.shape[1])}
    out['symmetry'] = sym

    # ---------------- K1
    k1 = part['K1']
    w16, wW, s16, sW = k1['omega_16'], k1['omega_W'], k1['sv16'], k1['svW']
    nneg, npos = k1['krein16']
    nnegW, nposW = k1['kreinW']
    val = k1['validation']
    dev_first = w16 - k1['omega_first_order_in_H']
    dev_first2 = k1['omega_W_at_2H'] - k1['omega_first_order_at_2H']
    ratio2 = dev_first2 / dev_first
    c2 = dev_first / H_MAIN ** 2
    dev_val = abs(val['box_level'] - val['resonance_omega_r'])
    out['K1'] = {k: v for k, v in k1.items() if k not in ('seconds', 'definition_of_the_fold')}
    rep.check('K1_free_level', abs(w16 - wW) < 1e-10 and s16[7] < 1e-6 < s16[8] and sW[1] < 1e-6 < sW[2]
              and nneg == 4 and npos == 4 and nnegW == 1 and nposW == 1 and abs(ratio2 - 4) < 0.2 and abs(c2) < 50
              and dev_val < 1e-7
              and all(v for k, v in sym.items() if k != 'dim W') and sym['dim W'] == 4,
              'omega = %.10f (16 dimensions), %.10f (reduced to W); omega_b (1 - H/(2 q_b)) = %.10f (the flat value omega_b = '
              '%.10f); the difference %.2e is of the second order in H: %.1f H^2 (at 2H %.2f times as large); eight degenerate '
              'states (two in W) with Krein signature (%d, %d) [(%d, %d) in W]; the box method at m_Psi/H = %d, mu_L = %g: %.10f, '
              'the real part of the exact resonance %.10f (difference %.1e; its width Gamma/m_Psi = %.1e)' % (
                  w16, wW, k1['omega_first_order_in_H'], wb, dev_first, c2, ratio2, nneg, npos, nnegW, nposW, val['m_over_H'],
                  val['mu_L'], val['box_level'], val['resonance_omega_r'], dev_val, val['resonance_Gamma']))

    results = {k: v for k, v in part['I'].items() if k not in ('seconds', 'definition_of_the_fold')}
    k9 = {k: v for k, v in part['K9'].items() if k not in ('seconds', 'definition_of_the_fold')}
    rH, rhoL0, dw_dmu = part['K6']['solution'], part['K6']['rhoL0'], part['K6']['domega_dmuL']
    compute_seconds = sum(part[n]['seconds'] for n in PART_NAMES)
    for line in results.pop('log'):
        print(line, flush=True)
    out['regime_I'] = results
    w0 = results['omega_free']
    pt = results['first_order_dw_over_G']
    conv = sorted([r for r in results['positive_G'] if r.get('converged')], key=lambda r: r['G'])

    # ---------------- K2
    small = [r for r in conv if r['G'] in TARGETS[:4]]
    ratios = [(r['omega'] - w0) / (pt * r['G']) for r in small]
    split = [(r['G'], r['singular_values'][1] / r['G']) for r in conv]
    split_small = [x for g, x in split if g <= 0.1]
    split_spread = max(split_small) / min(split_small) - 1
    out['K2'] = {'shift_over_first_order': ratios, 'split_over_G': split}
    rep.check('K2_first_order_limit', len(small) == 4 and all(abs(x - 1) < 2e-3 for x in ratios) and split_spread < 0.03
              and all(x > 0 for _, x in split),
              '(omega - omega_0)/(first-order shift) = %s for G <= 1e-3 (first-order coefficient %.6f with the weight e^{7H|sigma|}); '
              'at the occupied level the other Krein state of W is split off at every G, in proportion to G: the second singular '
              'value of the matching divided by G is %s for G = %s (constant to %.1f per cent up to G = 0.1)' % (
                  ['%.5f' % x for x in ratios], pt, ', '.join('%.4f' % x for _, x in split), ', '.join('%g' % g for g, _ in split),
                  100 * split_spread))

    # ---------------- K3
    worst = max(max(r['residual_KS_ode_16'], r['residual_fold_matching_16']) for r in conv) if conv else 1.0
    worst_sc = max(r['residual_selfconsistency'] for r in conv) if conv else 1.0
    charges_ok = all(all(abs(q + 1) < 1e-6 for q in r['krein_charges_16']) and r['krein_offdiagonal_16'] < 1e-6 for r in conv)
    tg = all(any(r['G'] == g for r in conv) for g in TARGETS)
    Gmax = max(r['G'] for r in conv) if conv else 0.0
    rep.check('K3_residuals_16', tg and Gmax >= 0.25 and worst < 1e-3 and worst_sc < 1e-6 and charges_ok
              and not any(r['capped'] for r in conv),
              '%d converged solutions for G = 1e-6 ... %.2f (the continuation stopped: %s); lifted to sixteen dimensions the four '
              'orbitals have Krein charge -1 each (measure e^{H|sigma|} d sigma) and are Krein-orthogonal; largest relative residual '
              'of the 16-dimensional Kohn-Sham equation and fold matching %.1e (central differences on the grid), of '
              'self-consistency %.1e; no cap active' % (len(conv), Gmax, results['stop_reason'], worst, worst_sc))

    # ---------------- K4
    rr = [r for r in conv if r['G'] in TARGETS[:3]]
    slope = float(np.polyfit(np.log([r['G'] for r in rr]), np.log([r['omega'] - w0 for r in rr]), 1)[0])
    out['K4'] = {'fitted_exponent': slope, 'predicted': 1.0}
    rep.check('K4_dilute_exponent', abs(slope - 1) < 0.01,
              'delta omega ~ G^p for G <= 1e-4: p = %.4f (first-order perturbation theory: 1; in the box |sigma| <= %g the weight '
              'e^{7H|sigma|} differs from 1 by at most %.3f, so this tests the continuation in the box, not the region near the '
              'turning point sigma_t = %.0f)' % (slope, L_MAIN, 7 * H_MAIN * L_MAIN, math.log(1 / w0) / H_MAIN))

    # ---------------- K5
    rates = [r['proper_density_decay_rate_far'] for r in conv]
    negI = [r.get('converged', False) for r in results['negative_G']]
    out['K5'] = {'proper_density_decay_rates_far': rates, 'negative_G_converged': negI,
                 'negative_G_omega': [r.get('omega') for r in results['negative_G']]}
    rep.check('K5_confined_to_the_fold', all(x > 100 * 7 * H_MAIN for x in rates) and all(negI),
              'near the end of the box (|sigma| <= %g) the proper scalar density e^{7H|sigma|} n_s decays at the rates %.3f ... %.3f '
              '(2 kappa - 7H with 7H = %.1e) for every G computed; the attractive self-interaction G = -1e-4, -1e-2 from the free '
              'state converges (omega = %s); this describes the box: beyond it the orbital decays up to the turning point and '
              'leaves the fold there as the outgoing wave of the width (um4_spectra.py U3 to U5)' % (
                  L_MAIN, min(rates), max(rates), 7 * H_MAIN, ['%.8f' % r.get('omega', float('nan')) for r in results['negative_G']]))

    # ---------------- K6
    rI01 = [r for r in conv if r['G'] == 0.1][0]
    hf_rel = abs(rhoL0 - dw_dmu) / dw_dmu
    hf_trap = (2 * qb * H_STEP) ** 2 / 12
    out['K6'] = {'kappa_H': KAPPA_H, 'solution': rH, 'without_feedback_omega': rI01.get('omega'), 'rhoL0_fold': float(rhoL0),
                 'domega_dmuL_finite_difference': dw_dmu, 'flat_formula_domega_dmuL': -muL / (4 * wb),
                 'relative_difference': hf_rel, 'trapezoid_normalisation_error': hf_trap,
                 'sign_of_kappa_H': 'negative: c_Phi < 0 (mu_L0 < 0) and rho_hat_L0(0) > 0'}
    rep.check('K6_higgs_portal_loop', bool(rH.get('converged')) and rH.get('residual_selfconsistency', 1) < 1e-6
              and rH.get('residual_KS_ode_16', 1) < 1e-3 and rhoL0 > 0 and abs(hf_rel - hf_trap) < 0.1 * hf_trap and KAPPA_H < 0
              and rH.get('muL', muL) < muL - 1e-3 and rH.get('omega', 2.0) < rI01.get('omega', 0.0),
              'the free orbital has rho_hat_L0(0) = %.8f > 0, equal to d omega_0/d mu_L = %.8f (finite difference of the level; the '
              'flat formula -mu_L/(4 omega_b) gives %.8f) up to %.2e, the error %.2e of the trapezoidal normalisation; with kappa_H = '
              '%.2f and G = 0.1 the joint loop converges in %s iterations: mu_L = %.6f (from %.2f), the level falls to omega = %.8f '
              '(%.8f without the feedback)' % (
                  rhoL0, dw_dmu, -muL / (4 * wb), hf_rel, hf_trap, KAPPA_H, rH.get('iterations'), rH.get('muL', float('nan')), muL,
                  rH.get('omega', float('nan')), rI01.get('omega', float('nan'))))

    # ---------------- K7
    eos = [(r['G'], r['pressure_over_energy']) for r in conv if r['target']]
    out['K7'] = eos
    rep.check('K7_equation_of_state', eos[0][0] == 1e-6 and abs(eos[0][1]) < 1e-3 and all(p > 0 for _, p in eos),
              'P/e (= q/e) = %s for G = %s: positive (repulsive) and vanishing in the dilute limit: the chi gas is cold dark matter' % (
                  ['%.2e' % p for _, p in eos], [g for g, _ in eos]))

    # ---------------- K8: the width grows as the level rises
    SH = [(r['G'], r['omega'], r['S_times_H'], r['free_barrier_2F']) for r in conv]
    mono = all(b_[2] < a_[2] for a_, b_ in zip(SH[:-1], SH[1:]) if b_[0] > a_[0])
    agree = all(abs(r['S_times_H'] / r['free_barrier_2F'] - 1) < 0.1 for r in conv if r['G'] <= 1e-2)
    # the lifetime condition Gamma < hbar/tau (tau = 160 Gyr, um4_spectra.py U6) with the width of U4 written with S at the
    # resonance: Gamma = 2 (q_b/m_Psi)^2 m_Psi e^{-S}; m_Psi = (m_Psi/H) H_min with H_min of um4_propagators.py P5
    spec6 = json.loads((UM4 / 'outputs' / 'spectra.json').read_text())['U6_lifetime']
    H_min = spec6['H_min_GeV']
    tau_s = 160e9 * 3.15576e7
    hbar_GeVs = 6.582119569e-25
    m_K8 = H_min / H_MAIN
    pref_K8 = 2 * qb ** 2
    S_min = math.log(pref_K8 * m_K8 * tau_s / hbar_GeVs)
    S_flat = 2 * F_wkb(wb) / H_MAIN                       # 2 F(upsilon_b) m_Psi/H at the flat level omega_b
    S_excess = conv[0]['tunnelling_exponent_S'] - S_flat   # = 1 (the factor 1/e of U4) at G -> 0
    Svals = [(r['G'], r['tunnelling_exponent_S']) for r in conv]
    G_life = None
    for (ga, sa), (gb, sb) in zip(Svals[:-1], Svals[1:]):
        if sa >= S_min > sb:
            G_life = math.exp(math.log(ga) + (math.log(gb) - math.log(ga)) * (sa - S_min) / (sa - sb))
            break
    first, last = conv[0], conv[-1]
    out['K8'] = {'G_omega_S_times_H_2F': SH, 'S_min_lifetime_160Gyr': S_min, 'm_over_H': 1 / H_MAIN, 'm_Psi_GeV': m_K8,
                 'H_min_GeV': H_min, 'prefactor_2_qb2': pref_K8, 'S_flat_2F_upsilon_b_over_H': S_flat,
                 'S_minus_S_flat_at_smallest_G': S_excess, 'G_largest_with_lifetime_above_160Gyr': G_life}
    rep.check('K8_width_grows', mono and agree and G_life is not None and last['S_times_H'] < 0.1 * first['S_times_H']
              and abs(S_excess - 1) < 0.01,
              'the tunnelling exponent of the width per unit m_Psi/H, S H, falls from %.5f (G = %g, omega = %.6f; the free barrier '
              '2F(omega) = %.5f) to %.5f at G = %.2f (omega = %.6f): the width grows with the self-interaction as the level '
              'approaches m_Psi, the barrier shrinks and the gas leaks into the bulk; at G -> 0, S exceeds 2F(upsilon_b) m_Psi/H = '
              '%.3f by %.4f (the factor 1/e of the width of um4_spectra.py U4), so Gamma = 2 (q_b/m_Psi)^2 m_Psi e^{-S}; at '
              'm_Psi/H = %.0e with H = H_min = %.0f GeV (m_Psi = %.3g GeV) the gas lives longer than 160 Gyr (S > %.2f) only for '
              'G < %.3f' % (first['S_times_H'], first['G'], first['omega'], first['free_barrier_2F'], last['S_times_H'], last['G'],
                            last['omega'], S_flat, S_excess, 1 / H_MAIN, H_min, m_K8, S_min, G_life or float('nan')))

    # ---------------- K9
    out['K9'] = k9
    rr = k9['rows']
    d9 = k9['omega_16'] - k9['omega_first_order_in_H']
    r9 = (k9['omega_W_at_2H'] - k9['omega_first_order_at_2H']) / d9
    # the smallest m_Psi at which q_b = 0.03 m_Psi lives longer than 160 Gyr with H = H_min (the asymptotic width of U4)
    s9 = k9['q_b']
    u9 = math.sqrt(1 - s9 * s9)
    gam9 = hbar_GeVs / tau_s
    f9 = lambda lm: 2 * F_wkb(u9) * math.exp(lm) / H_min - math.log((2 / math.e) * s9 * s9 * math.exp(lm) / gam9)
    m9_min = math.exp(brentq(f9, math.log(1e3), math.log(1e16), xtol=1e-12))
    m9 = H_min / k9['H']
    k9['m_Psi_at_H_min_GeV'] = m9
    k9['m_Psi_min_lifetime_160Gyr_GeV'] = m9_min
    ok9 = (abs(r9 - 4) < 0.2 and abs(d9) < 1e-8 and k9['krein_negative_orbitals'] == 4 and m9 > m9_min
           and all(r.get('converged') for r in rr) and abs(rr[0]['ratio_to_first_order'] - 1) < 2e-3
           and abs(1 - rr[0]['ratio_to_first_order']) < abs(1 - rr[1]['ratio_to_first_order']) < abs(1 - rr[2]['ratio_to_first_order'])
           and max(r['residual_KS_ode_16'] for r in rr) < 1e-3 and max(r['residual_selfconsistency'] for r in rr) < 1e-6
           and all(0 < r['pressure_over_energy'] < 1e-3 for r in rr))
    rep.check('K9_weak_binding', ok9,
              'q_b = 0.03 m_Psi (q_b/omega_b = %.3f), H = 1e-7 m_Psi (free barrier 2F = %.2e per unit m_Psi/H, so 2F m_Psi/H = %.0f); '
              'with H = H_min = %.0f GeV this is m_Psi = %.3g GeV, above the smallest mass %.3g GeV at which this binding lives '
              'longer than 160 Gyr: omega = %.10f from the 16-dimensional shooting (omega_b (1 - H/(2 q_b)) = %.10f; the difference '
              '%.2e is of the second order in H, %.2f times as large at 2H), first-order coefficient %.6f; '
              'self-consistent shift / first order = %s for G = 1e-4, 1e-3, 1e-2, P/e = %s' % (
                  k9['q_b_over_omega_b'], k9['free_barrier_2F_per_unit_m_over_H'], k9['free_barrier_2F_per_unit_m_over_H'] / k9['H'],
                  H_min, m9, m9_min, k9['omega_16'], k9['omega_first_order_in_H'], d9, r9, k9['first_order_dw_over_G'],
                  ['%.5f' % r['ratio_to_first_order'] for r in rr], ['%.1e' % r['pressure_over_energy'] for r in rr]))

    # ---------------- K10: how dilute is the gas of the universe?
    # G_KS = lambda_Psi n_chi/V_*; with the natural sizes lambda_Psi = m_Psi^-6 and V_* = m_Psi^-3, G_KS = n_chi/m_Psi^3; with extra
    # times of the Planck size, V_* = M_Pl^-3, G_KS = n_chi M_Pl^3/m_Psi^6.  The lightest chi that lives longer than 160 Gyr
    # (um4_spectra.py U6 with H = H_min) for q_b = m_Psi/2 and for the strong binding q_b = 0.99 m_Psi; the dark-matter density
    # near the Sun 0.4 GeV/cm^3 and the mean density today 0.120 rho_c/h^2 = 0.120 x 1.0537e-5 GeV/cm^3.
    hbarc_cm = 1.973269804e-14                       # GeV cm
    mpl = 1.22089e19
    coef_w = eos[0][1] / eos[0][0]                   # w_chi/G_KS in the dilute limit (K7)
    req6 = [r_ for r_ in spec6['rows'] if abs(r_['lifetime_over_t0'] - 160.0 / 13.8) < 1e-9]
    rows10 = []
    for qm in (0.5, 0.99):
        r6 = [r_ for r_ in req6 if abs(r_['q_b_over_m'] - qm) < 1e-9][0]
        wb10, mpsi10 = r6['omega_b_min_GeV'], r6['m_Psi_min_GeV']
        for label, rho10 in (('near the Sun', 0.4), ('mean of the universe today', 0.120 * 1.0537e-5)):
            n10 = rho10 / wb10 * hbarc_cm ** 3           # GeV^3
            g_nat = n10 / mpsi10 ** 3
            g_pl = n10 * mpl ** 3 / mpsi10 ** 6
            rows10.append({'q_b_over_m': qm, 'omega_b_GeV': wb10, 'm_Psi_GeV': mpsi10, 'density': label, 'rho_GeV_per_cm3': rho10,
                           'n_chi_per_cm3': rho10 / wb10, 'n_chi_GeV3': n10, 'G_KS_natural_sizes': g_nat,
                           'G_KS_Planck_extra_times': g_pl, 'w_chi_natural_sizes': coef_w * g_nat})
    out['K10'] = {'w_over_G_dilute': coef_w, 'rows': rows10, 'requirement': spec6['requirement']}
    gmax10 = max(max(r['G_KS_natural_sizes'], r['G_KS_Planck_extra_times']) for r in rows10)
    rep.check('K10_dilute_today', gmax10 < 1e-6 and G_life is not None and gmax10 < G_life and 0.04 < coef_w < 0.07,
              'G_KS = lambda_Psi n_chi/V_* for the lightest chi that lives longer than 160 Gyr (H = H_min): %s; with lambda_Psi = '
              'm_Psi^-6 and V_* = m_Psi^-3 at most %.1e (near the Sun, 0.4 GeV/cm^3), with extra times of the Planck size '
              '(V_* = M_Pl^-3) at most %.1e: far below the smallest computed coupling 1e-6 and below G_life = %.3f, so the gas of the '
              'universe is in the dilute limit, w_chi = %.4f G_KS (K7): at most %.1e near the Sun' % (
                  '; '.join('q_b = %g m_Psi: omega_b = %.3g GeV, m_Psi = %.3g GeV, G_KS = %.1e (natural) and %.1e (Planck) %s' % (
                      r['q_b_over_m'], r['omega_b_GeV'], r['m_Psi_GeV'], r['G_KS_natural_sizes'], r['G_KS_Planck_extra_times'],
                      r['density']) for r in rows10),
                  max(r['G_KS_natural_sizes'] for r in rows10), max(r['G_KS_Planck_extra_times'] for r in rows10),
                  G_life or float('nan'), coef_w, max(r['w_chi_natural_sizes'] for r in rows10)))

    out['runtime_s'] = round(compute_seconds + time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM4 / 'outputs' / 'kohnsham.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_4/code/um4_kohnsham.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM4 / 'reports' / 'kohnsham_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed (the parts computed in %.1f s, the assembly in %.1f s)' % (
        report['passed'], report['total'], compute_seconds, time.time() - t0))
    return 0 if report['all_passed'] else 1


def main(argv):
    if len(argv) == 2 and argv[0] == 'part':
        return 0 if run_part(argv[1]) else 3
    if argv == ['assemble']:
        return assemble()
    print(__doc__.split('BEGIN FOLD DEFINITION')[0])
    for n in PART_NAMES:
        tag = ('regime_' + n) if n == 'I' else n
        print('part %-4s %s' % (n, 'complete' if part_file(n).exists() else ('checkpointed' if _state_paths(tag)[0].exists()
                                                                             else 'not started')))
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
