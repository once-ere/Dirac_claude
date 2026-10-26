#!/usr/bin/env python3
"""um4_thermal.py - the thermal history of UM-4: the radiation of the Standard Model, what a thermal relic density of the
particles chi of dirac16complex would require, when the particles chi of UM-4 can and cannot be one, the right-handed neutrinos
and the ad hoc vacuum before nucleosynthesis (SOLUTION.md; FE-47 and FE-59 to FE-62 of FIELD_EQUATIONS.md).

Units GeV (1 GeV^-2 = 3.894e-28 cm^2, times c: 1.1674e-17 cm^3/s).  The particles chi are the level of dirac16complex at the
fold (in UM-4 long-lived resonances, um4_spectra.py): four particle states (one (2,2) multiplet of the rotations of ordinary
space and of the extra times: two Dirac fermions chi_a, a = 1, 2, of mass omega_b) and their four antiparticles, g_chi = 8 in
n_chi of FE-61.  With two Dirac species, FE-61 written for n_chi = sum over a of (n_a + nbar_a) has <sigma_ann v> =
(sigma v)_{chi chibar}/4, where (sigma v)_{chi chibar} is the spin-averaged annihilation of one chi_a with one chibar_a summed
over the final states.  The particles chi must live longer than 160 Gyr (11.6 t_0, the observed bound for a decay into
invisible relativistic particles, um4_spectra.py U6), which with H > H_min = 2534 GeV (um4_propagators.py P5) requires omega_b
above a bound that falls from 2.5e6 GeV at q_b = m_Psi/2 to 2.2e3 GeV at q_b = 0.999 m_Psi (U6).
  T1  the radiation of the Standard Model (FE-60): g_rho(T) and g_s(T) from the exact Bose and Fermi integrals of every
      particle (quarks and gluons above the QCD transition at T_c = 0.155 GeV, the light hadrons below; neutrinos decoupled
      below 1 MeV, with T_nu/T from the conserved entropy of the photons and e+e-, (T_nu/T)^3 = (2 + g_s,e(T))/5.5, which
      reaches 4/11 after e+e- annihilation): 106.75 above the electroweak scale, 10.75 between
      the muon and the electron thresholds, 3.909 (g_s) and 3.363 (g_rho) today;
  T2  the relic density (FE-61): the Boltzmann equation for Y = n_chi/s solved numerically from x = 1 (with the
      relativistic equilibrium density g m^2 T K_2(m/T)/(2 pi^2)) to x = 1e5 for an s-wave <sigma_ann v> (the result changes by
      less than 1e-3 when the integration is continued to x = 1e6); the value that gives Omega_chi h^2 = 0.1200 (Planck 2018) for
      omega_b = 10 GeV ... 10 TeV, compared with the analytic estimate of FE-61 (agreement within 10 per cent);
  T3  the current portals (FE-19 to FE-24, FE-47): the portal of IN-16 couples the fermion-number current J_f of a kind f of
      Standard-Model fermions to the convective current j_X of dirac16complex at the fold.  Elastic scattering (the time
      component) has the coupling g_f of FE-47; the convective current creates a pair chi chibar only with an amplitude of the
      second order in the momentum (um4_krein.py KR9), so the annihilation into a massless chiral fermion state is
      (sigma v)_{chi chibar} = g_f^2 omega_b^2 v^4 rho/(96 pi) (v the relative velocity; rho = 1.000 for the chirality-blind
      current, which alone creates no ghost pair at rest and creates ghost pairs only at the next order in the momentum, with
      the relative rate 0.0089 k^2/m_Psi^2, KR7, KR9), with the thermal average <v^4> = 60/x^2; the relic density
      through the 30 or 36 chiral quark states (below and above the top threshold) fixes g_q and with it the coherent
      scattering on nuclei sigma_SI = mu_N^2 (3 g_q)^2/pi, excluded by LZ (2.2e-48 cm^2 at 40 GeV, limit ~ omega_b at high mass;
      no comparison is made below 40 GeV, where the measured limit rises steeply) by many orders of magnitude; through the
      lepton portals (6 + 3 chiral lepton states: the lepton doublets and the right-handed charged leptons; the right-handed
      neutrinos must not take part, T5) the scattering arises at one loop through the photon,
      g_p = (alpha/(3 pi)) g_l sum over e, mu, tau of ln(Lambda^2/max(m_l^2, q^2)) (Lambda = omega_b, q = 50 MeV), and LZ allows
      it only above about 2.3e4 GeV (ESTIMATE); the dimensionless strength g_l omega_b^2 of the contact coupling that the relic
      requires grows with the mass and exceeds 4 pi (no longer a perturbative coupling) above about 4e3 GeV: where LZ allows the
      lepton portals the coupling is about 80, so the current portals cannot set the relic density of a perturbatively coupled
      chi;
  T4  the Higgs portal (FE-47): g_hchi = -2 q_b^2/(omega_b v) is fixed by the binding q_b of the bound state; the Higgs
      exchange gives sigma_SI = mu_N^2 (g_hchi f_H m_N/(v m_h^2))^2/pi (f_H = 0.30), so LZ requires q_b/omega_b below a few
      per cent: particles chi bound by the Higgs portal must be weakly bound (ESTIMATE);
  T5  the right-handed neutrinos (FE-62): their Yukawa production is negligible (Gamma/H ~ y^2 M_Pl/T << 1 for y = m_nu/v);
      if the lepton portal includes them (c^nu != 0, 3 of 12 chiral lepton states, with the annihilation of T3) they stay in
      equilibrium with chi until n_chi,eq^2 (sigma v)_nu/n_nuR,eq = H, decouple at T_dec ~ omega_b/15 and add
      Delta N_eff = 3 (10.75/g_s(T_dec))^{4/3} = 0.141 ... 0.24; compared with Planck 2018 (N_eff = 2.99 +- 0.17) and ACT DR6
      (2.86 +- 0.13; 2.89 +- 0.11 with BBN): the portal of the right-handed neutrinos must be weak enough that they never
      thermalise (c^nu << c^l), and then N_eff = 3.044;
  T6  the ad hoc vacuum before nucleosynthesis: v_loc^2 = v^2 + A^2 (FE-49) changes the Fermi constant (G_F,loc = 1/(sqrt2
      v_loc^2)), the electron mass and the quark-mass part of the neutron-proton mass difference (both proportional to v_loc),
      and its potential energy lambda A^4/4 adds to the expansion.  ESTIMATE of the helium abundance: the neutron fraction from
      the Born rates of n nu <-> p e, n e+ <-> p nubar and n -> p e nubar (normalised to the neutron lifetime, with the entropy
      transfer of e+e- annihilation to the photons) from 10 MeV to the deuterium bottleneck at 0.078 MeV, Y_p = 2 X_n; the
      rates obey detailed balance and tend to 1/tau_n; |Delta Y_p| < 0.006 (twice the error of Y_p = 0.245 +- 0.003) bounds the
      decay rate a_40 of A = v_A e^{-2 a_40 x_4}: a_40 > 1.4 /s for v_A = v; and the potential energy of the ad hoc vacuum
      never exceeds that of the radiation of an era that begins at x_4 = 0 only if a_40 > v_A^2 sqrt(lambda pi/6)/(e M_Pl) =
      4.8e-16 GeV (v_A/v)^2 = 7.2e8 /s (v_A/v)^2, which is the stronger condition: then the ad hoc vacuum is gone long before
      nucleosynthesis;
  T7  the thermal relic and the lifetime: with the largest s-wave annihilation that partial-wave unitarity allows,
      (sigma v)_{chi chibar} = 4 pi/(m^2 v_rel) (thermal average <1/v_rel> = sqrt(x/pi)), freeze-out gives Omega h^2 = 0.12 at
      omega_b = 9.69e4 GeV (Griest and Kamionkowski 1990; converged in the end point of the integration; 6.9e4 GeV if only the
      singlet of the extra-time SU(2) annihilates, 1.37e5 GeV if every channel is open), and heavier particles would be
      overproduced; the lifetime bound of U6 lies below this mass only for a strong binding, q_b > 0.906 m_Psi (0.875 ... 0.929
      over the range of the bookkeeping): only such strongly bound particles chi can be a thermal relic;
  T8  the binding that direct detection allows for the Higgs-portal binding of the author's specification: the largest
      q_b/omega_b that LZ allows (T4, with the limit growing like omega_b) falls like omega_b^{-1/4}; with that binding the derived
      width of U4, Gamma = (2/e) (q_b/m_Psi)^2 m_Psi e^{-2 F(u_b) m_Psi/H} (u_b = omega_b/m_Psi, F(u) ~ (q_b/omega_b)^3/3 for weak
      binding), stays below hbar/(160 Gyr) only for H < H_max = 2 F(u_b) m_Psi/ln(P m_Psi/Gamma_max), which grows only like
      omega_b^{1/4}: from 4.9e-4 GeV at 10 TeV to about 2.5 GeV at the Planck mass, far below the bound H > 2534 GeV at every mass
      (above about 1e10 GeV g_hchi exceeds 4 pi there, and the estimate is only formal); the particles chi bound by the Higgs
      portal therefore cannot be the dark matter of UM-4 (ESTIMATE: the LZ limit extrapolated in proportion to the mass);
  T9  the binding by the gluon condensate: the gauge-kinetic portal of the gluons binds chi through <(alpha_s/pi) G^2> =
      0.012 GeV^4, and by the theorem of Feynman and Hellmann (FE-47) the same coupling makes chi scatter on nucleons through
      <N|(alpha_s/pi) G^2|N> = -(8/9) m_N f_TG (f_TG = 0.92; the trace anomaly): f_N = 8 m_N f_TG q_b^2/(9 <(alpha_s/pi) G^2>
      omega_b) = 64 q_b^2/omega_b GeV^-3 (alpha_s cancels), sigma_SI = mu_N^2 f_N^2/pi = 9e-14 ... 8e-12 cm^2 at the lifetime
      bound of every binding, above the LZ limit by 29 to 33 orders of magnitude (ESTIMATE); the other
      condensates of the portals of IN-16 vanish in the vacuum (<W^2>, <B^2>, <J_f> and <B_munu>), so every binding that the
      portals of IN-16 can give couples chi to nucleons: dark matter of UM-4 needs a binding of chi to the fold that does not
      couple it to nucleons (OPEN).
Reads outputs/spectra.json and outputs/krein.json (run um4_spectra.py and um4_krein.py first).  Writes outputs/thermal.json and
reports/thermal_checks.json.
Usage: python universe_model_4/code/um4_thermal.py

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
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad, simpson, solve_ivp
from scipy.optimize import brentq
from scipy.special import kn

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent

GEV2_CM2 = 3.894e-28           # (1 GeV^-1)^2 in cm^2
GEV2_CM3S = 1.1674e-17         # 1 GeV^-2 times c in cm^3/s
M_PL = 1.22089e19              # G_N^{-1/2} in GeV (FE-60)
V_EW = 246.22
M_H = 125.25
M_N = 0.9389
ALPHA = 1 / 137.036
S0_CM3 = 2891.2                # entropy density today (T0 = 2.7255 K)
RHOC_H2 = 1.05371e-5           # GeV/cm^3
OMEGA_DM_H2 = 0.1200           # Planck 2018
LZ_MIN = (2.2e-48, 40.0)       # cm^2 at GeV: LZ, 4.2 tonne-years, arXiv:2410.17036v3 = Phys. Rev. Lett. 135, 011802 (2025)
T_QCD = 0.155


def lz_limit(m):
    """The LZ limit at and above its minimum (40 GeV), approximated by the 1/number-density scaling sigma_lim ~ m (weaker
    than the measured curve between the minimum and a few hundred GeV, so the exclusions drawn from it are conservative).
    Below the minimum the measured limit rises steeply; it is not modelled here (None): no comparison is made there."""
    if m < LZ_MIN[1]:
        return None
    return LZ_MIN[0] * m / LZ_MIN[1]


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


# ---------------------------------------------------------------- T1: the degrees of freedom
# (name, mass in GeV, internal degrees of freedom, +1 fermion / -1 boson)
SM_HIGH = [('t', 172.69, 12, 1), ('b', 4.18, 12, 1), ('c', 1.27, 12, 1), ('s', 0.093, 12, 1), ('d', 0.0047, 12, 1),
           ('u', 0.0022, 12, 1), ('g', 0.0, 16, -1)]
SM_LOW_HADRONS = [('pi+-', 0.13957, 2, -1), ('pi0', 0.13498, 1, -1), ('K', 0.4937, 4, -1), ('eta', 0.5479, 1, -1),
                  ('rho', 0.7753, 9, -1), ('omega', 0.7827, 3, -1), ('N', 0.9389, 8, 1)]
SM_COMMON = [('W', 80.37, 6, -1), ('Z', 91.19, 3, -1), ('h', 125.25, 1, -1), ('gamma', 0.0, 2, -1), ('tau', 1.777, 4, 1),
             ('mu', 0.10566, 4, 1), ('e', 0.000511, 4, 1)]
NU_L = ('nu_L', 0.0, 6, 1)


def _rho_s(y, stat):
    """(rho, s) of one internal degree of freedom in units of (pi^2/30) T^4 and (2 pi^2/45) T^3."""
    if y > 60:
        return 0.0, 0.0
    f = (lambda u: 1.0 / (math.exp(math.sqrt(u * u + y * y)) + 1)) if stat > 0 else \
        (lambda u: 1.0 / math.expm1(math.sqrt(u * u + y * y)) if u * u + y * y > 0 else 0.0)
    rho = quad(lambda u: u * u * math.sqrt(u * u + y * y) * f(u), 0, 80, limit=200)[0] * 15 / math.pi ** 4
    p = quad(lambda u: u ** 4 / math.sqrt(u * u + y * y) * f(u) if u > 0 else 0.0, 0, 80, limit=200)[0] * 5 / math.pi ** 4
    return rho, 0.75 * (rho + p)


def g_star(T):
    """g_rho(T) and g_s(T) of the Standard Model plasma (with the neutrinos; after their decoupling at 1 MeV they carry
    T_nu = (4/11)^{1/3} T, the instantaneous approximation)."""
    parts = SM_COMMON + (SM_HIGH if T > T_QCD else SM_LOW_HADRONS)
    gr = gs = 0.0
    for _, m, g, st in parts:
        r, s = _rho_s(m / T, st)
        gr += g * r
        gs += g * s
    if T > 1e-3:
        gr += 6 * 7 / 8
        gs += 6 * 7 / 8
    else:
        # the neutrinos decoupled at 1 MeV: T_nu a = const, while the entropy of the photons and e+e- is conserved, so
        # (T_nu/T)^3 = (2 + g_s,e(T))/5.5 (g_s,e of e+e-, 3.5 at T >> m_e), which reaches 4/11 after e+e- annihilation
        gse = 4 * _rho_s(0.000511 / T, 1)[1]
        x = ((2 + gse) / 5.5) ** (1 / 3)
        gr += 6 * 7 / 8 * x ** 4
        gs += 6 * 7 / 8 * x ** 3
    return gr, gs


_LT = np.linspace(math.log(1e-5), math.log(2e4), 260)
_GT = np.array([g_star(math.exp(t)) for t in _LT])


def g_interp(T):
    lt = math.log(T)
    return float(np.interp(lt, _LT, _GT[:, 0])), float(np.interp(lt, _LT, _GT[:, 1]))


def dlngs_dlnT(T):
    lt = math.log(T)
    d = np.gradient(np.log(_GT[:, 1]), _LT)
    return float(np.interp(lt, _LT, d))


def hubble(T):
    gr, _ = g_interp(T)
    return math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / M_PL          # FE-60


def entropy(T):
    return 2 * math.pi ** 2 / 45 * g_interp(T)[1] * T ** 3


# ---------------------------------------------------------------- T2: the relic density
G_CHI = 8


def n_eq(m, T, g=G_CHI):
    x = m / T
    return g * m * m * T * kn(2, x) / (2 * math.pi ** 2) if x < 600 else 0.0


X_END = 1e5                    # the end point of the Boltzmann integration (T2: converged to 1e-3)


def relic(m, sv, g=G_CHI, x0=1.0, x1=X_END):
    """Omega h^2 from FE-61 for <sigma_ann v> = sv (GeV^-2; a number for an s-wave, or a function of x = m/T); returns
    (Omega h^2, x_f, Y_inf)."""
    svf = sv if callable(sv) else (lambda x: sv)

    def Yeq(x):
        T = m / x
        return n_eq(m, T, g) / entropy(T)

    def rhs(lx, W):
        # W = ln Y; dY/dx = -(s sv/(x H)) (1 + dln g_s/dln T/3) (Y^2 - Yeq^2)
        x = math.exp(lx)
        T = m / x
        Y = math.exp(W[0])
        fac = entropy(T) * svf(x) / (x * hubble(T)) * (1 + dlngs_dlnT(T) / 3)
        return [-x * fac * (Y * Y - Yeq(x) ** 2) / Y]
    sol = solve_ivp(rhs, (math.log(x0), math.log(x1)), [math.log(Yeq(x0))], method='Radau', rtol=1e-8, atol=1e-10,
                    dense_output=True)
    Yinf = math.exp(sol.y[0, -1])
    # freeze-out: where Y exceeds Y_eq by the factor 2.5 (the conventional delta = 1.5)
    xs = np.geomspace(x0, 200, 2000)
    Ys = np.exp(sol.sol(np.log(xs))[0])
    Ye = np.array([Yeq(x) for x in xs])
    k = int(np.argmax(Ys > 2.5 * Ye))
    xf = float(xs[k]) if k > 0 else float('nan')
    return m * Yinf * S0_CM3 / RHOC_H2, xf, Yinf


def sv_for_relic(m, target=OMEGA_DM_H2, x1=X_END):
    """The s-wave <sigma_ann v> (GeV^-2) that gives Omega h^2 = target."""
    f = lambda lsv: math.log(relic(m, math.exp(lsv), x1=x1)[0] / target)
    lsv = brentq(f, math.log(1e-11), math.log(1e-7), xtol=1e-10)
    return math.exp(lsv)


def b_for_relic(m, target=OMEGA_DM_H2, x1=X_END):
    """The coefficient B of <sigma_ann v> = B/x^2 (GeV^-2; the convective-current annihilation, <v^4> = 60/x^2) that gives
    Omega h^2 = target; the integration starts at x = 3, where the particles are in equilibrium."""
    f = lambda lb: math.log(relic(m, (lambda x, B=math.exp(lb): B / (x * x)), x0=3.0, x1=x1)[0] / target)
    lb = brentq(f, math.log(1e-9), math.log(1e-4), xtol=1e-10)
    return math.exp(lb)


# ---------------------------------------------------------------- T6: neutron-proton freeze-out (units MeV and s)
ME_MEV = 0.51099895            # electron mass
Q_NP = 1.29333                 # m_n - m_p
Q_QCD = 2.52                   # the part of m_n - m_p from m_d - m_u (Borsanyi et al., Science 347 (2015) 1452), proportional to v
TAU_N = 878.4                  # neutron lifetime in s (PDG 2024)
HBAR_MEVS = 6.582119569e-22    # MeV s
T_NUC = 0.078                  # MeV: the deuterium bottleneck, where the free neutrons are bound into helium
YP_OBS = (0.245, 0.003)        # PDG 2024 (Fields, Molaro, Sarkar): the primordial helium mass fraction
N_INT = 1601                   # points of the Simpson rule in every rate integral


def _fd(x):
    return 0.5 * (1.0 - np.tanh(0.5 * x))                      # 1/(e^x + 1) without overflow


def _simpson_mapped(a, b, f):
    """int_a^b f(E) dE with E = a + (b - a) s^2 (which removes the square-root behaviour at a), Simpson rule in s."""
    s = np.linspace(0.0, 1.0, N_INT)
    E = a + (b - a) * s * s
    return simpson(f(E) * 2 * (b - a) * s, x=s)


def np_rates(T, Tnu, me, Q, K):
    """The Born rates lambda(n -> p) and lambda(p -> n) in 1/s at the photon temperature T and the neutrino temperature Tnu
    (MeV), electron mass me, mass difference Q and K = G_F^2 (1 + 3 g_A^2)/(2 pi^3) (normalised to the neutron lifetime): the
    two-body processes n nu <-> p e, n e+ <-> p nubar and the three-body n <-> p e nubar, with the Pauli blocking of the
    leptons (so that the rates obey detailed balance at T = Tnu)."""
    top = 50.0 * max(T, Tnu) + Q + me
    pe = lambda E: np.sqrt(np.maximum(E * E - me * me, 0.0))
    lo = max(me, Q)
    i1 = _simpson_mapped(lo, lo + top, lambda E: (E - Q) ** 2 * E * pe(E) * _fd((E - Q) / Tnu) * (1 - _fd(E / T)))  # n nu -> p e
    i2 = _simpson_mapped(me, me + top, lambda E: E * pe(E) * (E + Q) ** 2 * _fd(E / T) * (1 - _fd((E + Q) / Tnu)))  # n e+ -> p nubar
    i3 = _simpson_mapped(me, Q, lambda E: E * pe(E) * (Q - E) ** 2 * (1 - _fd(E / T)) * (1 - _fd((Q - E) / Tnu))) if Q > me else 0.0
    j1 = _simpson_mapped(lo, lo + top, lambda E: E * pe(E) * (E - Q) ** 2 * _fd(E / T) * (1 - _fd((E - Q) / Tnu)))  # p e -> n nu
    j2 = _simpson_mapped(me, me + top, lambda E: E * pe(E) * (E + Q) ** 2 * _fd((E + Q) / Tnu) * (1 - _fd(E / T)))  # p nubar -> n e+
    j3 = _simpson_mapped(me, Q, lambda E: E * pe(E) * (Q - E) ** 2 * _fd(E / T) * _fd((Q - E) / Tnu)) if Q > me else 0.0  # p e nubar -> n
    return K * (i1 + i2 + i3), K * (j1 + j2 + j3)


def _decay_integral(me, Q):
    return _simpson_mapped(me, Q, lambda E: E * np.sqrt(np.maximum(E * E - me * me, 0.0)) * (Q - E) ** 2)


K_NP = 1.0 / (TAU_N * _decay_integral(ME_MEV, Q_NP))


def _electron_rho_s(T, me):
    """Energy density (MeV^4) and entropy density (MeV^3) of e+ e- (four states) at temperature T."""
    p_ = np.linspace(0.0, 60.0 * T, 3001)
    E = np.sqrt(p_ * p_ + me * me)
    f = _fd(E / T)
    rho = 4 / (2 * math.pi ** 2) * simpson(p_ * p_ * E * f, x=p_)
    P = 4 / (2 * math.pi ** 2) * simpson(p_ ** 4 / (3 * E) * f, x=p_)
    return rho, (rho + P) / T


T_START = 10.0                 # MeV
_TS = np.geomspace(0.5 * T_NUC, 1.5 * T_START, 400)
_S_GE = np.array([(2 * math.pi ** 2 / 45) * 2 * T ** 3 + _electron_rho_s(T, ME_MEV)[1] for T in _TS])
_LNT = np.log(_TS)
_LNTNU = np.log(_TS * (_S_GE / _TS ** 3 / (_S_GE[-1] / _TS[-1] ** 3)) ** (1 / 3))   # T_nu a = const, (s_gamma + s_e) a^3 = const


def helium(a40, vA_over_v, effects=('GF', 'masses')):
    """Y_p = 2 X_n(T_NUC) with the ad hoc vacuum eps(x_4) = A^2/v^2 = (v_A/v)^2 e^{-4 a40 x_4} (x_4 the time since the beginning
    of the radiation era, a40 in 1/s): G_F,loc = G_F/(1 + eps) (the rates scale as G_F^2), m_e and the quark-mass part of Q times
    sqrt(1 + eps) (FE-49); returns (Y_p, x_4 at T_NUC in s)."""
    def T_of_Tnu(Tnu):
        return math.exp(np.interp(math.log(Tnu), _LNTNU, _LNT))

    def rhs(s_, y):
        X, t_ = y
        Tnu = T_START * math.exp(-s_)
        T = T_of_Tnu(Tnu)
        eps = vA_over_v ** 2 * math.exp(-4 * a40 * t_)
        r = math.sqrt(1 + eps)
        me = ME_MEV * r if 'masses' in effects else ME_MEV
        Q = (Q_NP - Q_QCD) + Q_QCD * r if 'masses' in effects else Q_NP
        K = K_NP / (1 + eps) ** 2 if 'GF' in effects else K_NP
        lnp, lpn = np_rates(T, Tnu, me, Q, K)
        rho = (math.pi ** 2 / 15) * T ** 4 + _electron_rho_s(T, me)[0] + (7 / 8) * (math.pi ** 2 / 30) * 6 * Tnu ** 4
        Hs = math.sqrt(8 * math.pi * rho / 3) / (M_PL * 1e3) / HBAR_MEVS
        return [(-lnp * X + lpn * (1 - X)) / Hs, 1 / Hs]
    X0 = 1 / (1 + math.exp(Q_NP / T_START))
    t_start = 1 / (2 * math.sqrt(8 * math.pi * (math.pi ** 2 / 30) * 10.75 * T_START ** 4 / 3) / (M_PL * 1e3) / HBAR_MEVS)
    Tnu_end = math.exp(np.interp(math.log(T_NUC), _LNT, _LNTNU))
    sol = solve_ivp(rhs, (0.0, math.log(T_START / Tnu_end)), [X0, t_start], method='LSODA', rtol=1e-8, atol=1e-11)
    return 2 * sol.y[0, -1], sol.y[1, -1]



def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')

def main():
    t0 = time.time()
    rep = Report()
    out = {'conventions': {'g_chi': G_CHI, 'sigma_ann_v_FE61': '(sigma v)_{chi chibar}/4 for the two Dirac species',
                           'GeV^-2_in_cm^3/s': GEV2_CM3S}}

    # ---------------- T1
    pts = {}
    for T in (1e4, 300.0, 50.0, 5.0, 1.0, 0.2, 0.1, 0.01, 1e-3, 1e-5):
        gr, gs = g_interp(T)
        pts['%g GeV' % T] = {'g_rho': gr, 'g_s': gs}
    gr0, gs0 = g_star(1e-5)
    out['T1'] = pts
    ok1 = (abs(pts['10000 GeV']['g_rho'] - 106.75) < 0.05 and abs(pts['0.01 GeV']['g_s'] - 10.75) < 0.1
           and abs(gs0 - 3.909) < 0.01 and abs(gr0 - 3.363) < 0.01)
    rep.check('T1_degrees_of_freedom', ok1,
              'g_rho, g_s of the Standard Model: %s; above the electroweak scale 106.75 (three right-handed neutrinos in '
              'equilibrium would add 5.25), 10.75 between the muon and electron thresholds, today g_s = %.3f, g_rho = %.3f' % (
                  ', '.join('%s: %.2f/%.2f' % (k, v['g_rho'], v['g_s']) for k, v in pts.items()), gs0, gr0))

    # ---------------- T2
    rows = []
    for m in (10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 10000.0):
        sv = sv_for_relic(m)
        Oh2, xf, Y = relic(m, sv)
        gstar = g_interp(m / xf)[0]
        approx = 1.07e9 * xf / (math.sqrt(gstar) * M_PL * sv)          # FE-61
        rows.append({'omega_b_GeV': m, 'sv_FE61_GeV-2': sv, 'sv_FE61_cm3_s': sv * GEV2_CM3S,
                     'sv_chichibar_cm3_s': 4 * sv * GEV2_CM3S, 'x_f': xf, 'g_star_f': gstar, 'Omega_h2': Oh2,
                     'Omega_h2_FE61_estimate': approx})
        print('  relic m = %7.0f GeV: <sigma v>_FE61 = %.4e cm^3/s, x_f = %.1f, estimate %.4f' % (m, sv * GEV2_CM3S, xf, approx),
              flush=True)
    # convergence in the end point: the same <sigma v> integrated to x = 1e6
    conv2 = []
    for r in rows[::3]:
        m = r['omega_b_GeV']
        Oh2_long = relic(m, r['sv_FE61_GeV-2'], x1=10 * X_END)[0]
        conv2.append({'omega_b_GeV': m, 'Omega_h2_x_end_1e5': r['Omega_h2'], 'Omega_h2_x_end_1e6': Oh2_long,
                      'relative_change': Oh2_long / r['Omega_h2'] - 1})
    out['T2'] = {'rows': rows, 'x_end': X_END, 'end_point_convergence': conv2}
    est_dev = max(abs(r['Omega_h2_FE61_estimate'] / OMEGA_DM_H2 - 1) for r in rows)
    ok2 = (all(1.6e-26 < r['sv_FE61_cm3_s'] < 2.6e-26 for r in rows) and all(18 < r['x_f'] < 32 for r in rows)
           and est_dev < 0.10 and all(abs(c['relative_change']) < 1e-3 for c in conv2))
    rep.check('T2_relic_density', ok2,
              'Omega_chi h^2 = 0.1200 from the numerical solution of FE-61 (integrated to x = %.0e; continued to x = %.0e it changes '
              'by %s) for an s-wave annihilation requires <sigma_ann v> = %s cm^3/s (FE-61 normalisation, n_chi with g_chi = 8; '
              '(sigma v)_{chi chibar} is four times larger) with freeze-out at x_f = %s; the analytic estimate of FE-61 agrees within '
              '%.1f per cent' % (X_END, 10 * X_END, ', '.join('%.1e' % c['relative_change'] for c in conv2),
                                ', '.join('%.3e (%g GeV)' % (r['sv_FE61_cm3_s'], r['omega_b_GeV']) for r in rows),
                                ', '.join('%.1f' % r['x_f'] for r in rows), 100 * est_dev))

    # ---------------- T3: the current portals (convective current, KR9)
    kr = json.loads((UM4 / 'outputs' / 'krein.json').read_text())['KR9_convective_current_pairs']
    rho_x = kr['rho_X']
    rho1 = rho_x['1']                                                   # the chirality-blind current (ghost pairs only at O(k^3))
    ALPHA_V4 = 60.0                                                     # <v^4> = 60/x^2 (relative velocity, Maxwell-Boltzmann)
    M_TOP = 172.69
    dd = []
    for m in (10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 10000.0, 30000.0, 100000.0):
        B = b_for_relic(m)                                              # <sigma_ann v> = B/x^2 (FE-61 normalisation)
        # B = N g^2 m^2 rho <v^4> x^2/(4 96 pi): (sigma v)_{chi chibar} = 4 <sigma_ann v>, N chiral states of equal coupling g
        g2_per_state = lambda N: B * 4 * 96 * math.pi / (N * m * m * rho1 * ALPHA_V4)
        n_q = 36 if m > M_TOP else 30
        gq = math.sqrt(g2_per_state(n_q))
        mu = m * M_N / (m + M_N)
        sig_q = mu * mu * (3 * gq) ** 2 / math.pi * GEV2_CM2
        gl = math.sqrt(g2_per_state(9))
        L = sum(math.log(m * m / max(ml * ml, 0.05 ** 2)) for ml in (0.000511, 0.10566, 1.777))
        gp = ALPHA / (3 * math.pi) * gl * L
        sig_l = mu * mu * gp ** 2 / math.pi * GEV2_CM2 * (54 / 131) ** 2        # per nucleon in xenon (Z/A)^2
        lim = lz_limit(m)
        # x_f of this annihilation (where Y exceeds Y_eq by 2.5)
        Oh2_chk, xf_b, _ = relic(m, (lambda x, B=B: B / (x * x)), x0=3.0)
        dd.append({'omega_b_GeV': m, 'B_GeV-2': B, 'sv_at_x_f_cm3_s': B / xf_b ** 2 * GEV2_CM3S, 'x_f': xf_b,
                   'Omega_h2': Oh2_chk, 'n_quark_states': n_q, 'g_quark_GeV-2': gq, 'g_quark_times_m2': gq * m * m,
                   'sigma_SI_quark_cm2': sig_q, 'g_lepton_GeV-2': gl, 'g_lepton_times_m2': gl * m * m, 'loop_log_sum': L,
                   'sigma_SI_lepton_loop_cm2': sig_l, 'LZ_limit_cm2': lim,
                   'quark_excluded_by_factor': sig_q / lim if lim else None,
                   'lepton_ratio_to_limit': sig_l / lim if lim else None})
        print('  convective relic m = %8.0f GeV: B = %.3e GeV^-2, x_f = %.1f, g_l m^2 = %.3g' % (m, B, xf_b, gl * m * m), flush=True)
    out['T3'] = {'rho_X_KR9': rho_x, 'rho_used': rho1, 'thermal_v4': '60/x^2',
                 'sigma_v': '(sigma v)_{chi chibar} = g_f^2 omega_b^2 v^4 rho/(96 pi) per massless chiral state', 'rows': dd}
    cmp_ = [d for d in dd if d['LZ_limit_cm2']]
    m_min = None
    for a_, b_ in zip(cmp_[:-1], cmp_[1:]):
        if a_['lepton_ratio_to_limit'] >= 1 > b_['lepton_ratio_to_limit']:
            la, lb = math.log(a_['lepton_ratio_to_limit']), math.log(b_['lepton_ratio_to_limit'])
            m_min = math.exp(math.log(a_['omega_b_GeV']) + la / (la - lb) * (math.log(b_['omega_b_GeV']) - math.log(a_['omega_b_GeV'])))
    m_pert = None
    for a_, b_ in zip(dd[:-1], dd[1:]):
        if a_['g_lepton_times_m2'] < 4 * math.pi <= b_['g_lepton_times_m2']:
            la, lb = math.log(a_['g_lepton_times_m2']), math.log(b_['g_lepton_times_m2'])
            m_pert = math.exp(math.log(a_['omega_b_GeV']) + (math.log(4 * math.pi) - la) / (lb - la)
                              * (math.log(b_['omega_b_GeV']) - math.log(a_['omega_b_GeV'])))
    out['T3']['lepton_allowed_above_GeV'] = m_min
    out['T3']['lepton_coupling_reaches_4pi_at_GeV'] = m_pert
    window = m_min is not None and m_pert is not None and m_pert > m_min
    out['T3']['perturbative_leptophilic_window'] = window
    ok3 = (len(cmp_) == 7 and all(d['quark_excluded_by_factor'] > 1 for d in cmp_) and m_min is not None and m_pert is not None
           and all(abs(d['Omega_h2'] / OMEGA_DM_H2 - 1) < 1e-6 for d in dd) and abs(rho1 - 1) < 0.02
           and all(b_['B_GeV-2'] > a_['B_GeV-2'] for a_, b_ in zip(dd[:-1], dd[1:])))
    rep.check('T3_current_portals', ok3,
              'the convective current creates pairs only with an amplitude of the second order in the momentum (um4_krein.py KR9; '
              'rho = %.4f for the chirality-blind current), so the relic needs <sigma_ann v> = B/x^2 with B = %s GeV^-2 (%s GeV; at '
              'freeze-out x_f = %s); through the quark current portals this gives sigma_SI = %s cm^2, above the LZ limit by factors '
              '%s for %s GeV (below 40 GeV no comparison is made): the quark portals cannot set the relic density; through the '
              'lepton portals (9 chiral states) the scattering is loop-induced, sigma_SI = %s cm^2 per nucleon, above the limit '
              'below about %.0f GeV and allowed above (ESTIMATE: the loop cut-off Lambda = omega_b and the scaling of the LZ limit '
              'enter), and the strength g_l omega_b^2 = %s of the contact coupling exceeds 4 pi above %.2g GeV: %s' % (
                  rho1, ', '.join('%.2e' % d['B_GeV-2'] for d in dd), ', '.join('%g' % d['omega_b_GeV'] for d in dd),
                  ', '.join('%.1f' % d['x_f'] for d in dd), ', '.join('%.1e' % d['sigma_SI_quark_cm2'] for d in dd),
                  ', '.join('%.0e' % d['quark_excluded_by_factor'] for d in cmp_), ', '.join('%g' % d['omega_b_GeV'] for d in cmp_),
                  ', '.join('%.1e (%g GeV)' % (d['sigma_SI_lepton_loop_cm2'], d['omega_b_GeV']) for d in dd),
                  m_min if m_min else float('nan'), ', '.join('%.2g' % d['g_lepton_times_m2'] for d in dd),
                  m_pert if m_pert else float('nan'),
                  ('a leptophilic chi between about %.2g and %.2g GeV can be a perturbative thermal relic' % (m_min, m_pert)) if window
                  else ('where LZ allows the lepton portals the coupling that the relic needs is no longer perturbative (%.0f at the '
                        'crossing mass): the current portals cannot set the relic density of a perturbatively coupled chi' % (
                            math.exp(np.interp(math.log(m_min), [math.log(d['omega_b_GeV']) for d in dd],
                                               [math.log(d['g_lepton_times_m2']) for d in dd]))))))

    # ---------------- T4: the Higgs portal
    fH = 0.30
    hp = []
    for m in (100.0, 300.0, 1000.0, 3000.0, 10000.0):
        mu = m * M_N / (m + M_N)
        gmax = math.sqrt(lz_limit(m) / GEV2_CM2 * math.pi) / (mu * fH * M_N / (V_EW * M_H ** 2))
        qmax = math.sqrt(gmax * m * V_EW / 2)                            # g_hchi = 2 q_b^2/(omega_b v)
        hp.append({'omega_b_GeV': m, 'g_hchi_max': gmax, 'q_b_max_GeV': qmax, 'q_b_over_omega_b_max': qmax / m})
    out['T4'] = hp
    ok4 = all(h['q_b_over_omega_b_max'] < 0.1 for h in hp)
    rep.check('T4_higgs_portal_binding', ok4,
              'the Higgs-portal Yukawa coupling of FE-47, g_hchi = -2 q_b^2/(omega_b v), gives sigma_SI = mu_N^2 (g_hchi f_H '
              'm_N/(v m_h^2))^2/pi; LZ then requires |g_hchi| < %s and q_b/omega_b < %s for omega_b = %s GeV (ESTIMATE): '
              'particles chi bound by the Higgs portal must be weakly bound to the fold' % (
                  ', '.join('%.1e' % h['g_hchi_max'] for h in hp), ', '.join('%.3f' % h['q_b_over_omega_b_max'] for h in hp),
                  ', '.join('%g' % h['omega_b_GeV'] for h in hp)))

    # ---------------- T5: the right-handed neutrinos
    nr = []
    for d in dd[:7]:
        m = d['omega_b_GeV']
        B = d['B_GeV-2']                                                # the relic with 12 chiral lepton states (nu_R included)
        # (sigma v)_{chi chibar} = 4 B/x^2 summed over the 12 states; the 3 right-handed neutrino states take 3/12 of it

        def f(x, m=m, B=B):
            T = m / x
            n_nu = 3 * 2 * 3 * 1.2020569 / (4 * math.pi ** 2) * T ** 3        # 3 Weyl states (nu_R and its antiparticle)
            sv_nu = 4 * B / (x * x) * 3 / 12
            return math.log(n_eq(m, T) ** 2 / 4 * sv_nu / n_nu / hubble(T))
        xdec = brentq(f, 1.5, 60)
        Tdec = m / xdec
        dN = 3 * (10.75 / g_interp(Tdec)[1]) ** (4 / 3)                  # FE-62
        nr.append({'omega_b_GeV': m, 'x_dec': xdec, 'T_dec_GeV': Tdec, 'g_s_dec': g_interp(Tdec)[1], 'Delta_N_eff': dN,
                   'N_eff': 3.044 + dN, 'pull_Planck2018': (3.044 + dN - 2.99) / 0.17,
                   'pull_ACT_DR6_BBN': (3.044 + dN - 2.89) / 0.11})
    yuk = (0.05e-9 / V_EW) ** 2 * M_PL / 100.0                           # Gamma/H ~ y^2 M_Pl/T, y = 0.05 eV/v, T = 100 GeV
    out['T5'] = {'portal_thermalised': nr, 'yukawa_Gamma_over_H_at_100GeV': yuk}
    ok5 = all(0.13 < x['Delta_N_eff'] < 0.30 for x in nr) and yuk < 1e-6
    rep.check('T5_right_handed_neutrinos', ok5,
              'the Yukawa production of nu_R is negligible (Gamma/H ~ %.0e at 100 GeV); through the lepton portal with the '
              'annihilation of T3 they decouple at x_dec = %s and add Delta N_eff = %s (FE-62), i.e. N_eff = %s against Planck 2018 '
              '2.99 +- 0.17 (pulls %s) and ACT DR6 with BBN 2.89 +- 0.11 (pulls %s): the right-handed neutrinos must not thermalise '
              '(c^nu << c^l, then N_eff = 3.044)' % (
                  yuk, ', '.join('%.1f' % x['x_dec'] for x in nr), ', '.join('%.3f' % x['Delta_N_eff'] for x in nr),
                  ', '.join('%.2f' % x['N_eff'] for x in nr), ', '.join('%.1f' % x['pull_Planck2018'] for x in nr),
                  ', '.join('%.1f' % x['pull_ACT_DR6_BBN'] for x in nr)))

    # ---------------- T6: the ad hoc vacuum before nucleosynthesis
    l_np, l_pn = np_rates(1.0, 1.0, ME_MEV, Q_NP, K_NP)
    db_dev = abs(l_pn / l_np / math.exp(-Q_NP / 1.0) - 1)              # detailed balance at T = T_nu
    low_dev = abs(np_rates(0.002, 0.002, ME_MEV, Q_NP, K_NP)[0] * TAU_N - 1)  # free decay at low temperature
    Y0, tnuc = helium(1.0, 0.0)
    sens = {}
    for name, eff in (('Fermi constant', ('GF',)), ('masses', ('masses',)), ('both', ('GF', 'masses'))):
        sens[name] = (helium(0.0, math.sqrt(1e-3), effects=eff)[0] - Y0) / 1e-3      # dY_p/d(A^2/v^2), A constant
    lam_h = M_H ** 2 / (2 * V_EW ** 2)
    bounds = []
    for ratio in (0.1, 1.0, 10.0, 1e3, 1e6):
        f6 = lambda la, ratio=ratio: abs(helium(math.exp(la), ratio)[0] - Y0) - 2 * YP_OBS[1]
        if f6(math.log(1e-3)) < 0:
            a40_bbn = None                                              # no bound: allowed for every a40 > 1e-3 /s
        else:
            a40_bbn = math.exp(brentq(f6, math.log(1e-3), math.log(1e3), xtol=1e-4))
        # the potential energy lambda A^4/4 against the radiation 3 M_Pl^2/(32 pi x4^2) of an era that begins at x4 = 0:
        # largest at x4 = 1/(4 a40); it stays below only if a40 > v_A^2 sqrt(lambda pi/6)/(e M_Pl)
        vA = ratio * V_EW
        a40_E = vA ** 2 * math.sqrt(lam_h * math.pi / 6) / (math.e * M_PL)          # GeV
        ts = np.geomspace(1e-3, 1e3, 20001) / (4 * a40_E)
        rmax = float(np.max(lam_h * vA ** 4 / 4 * np.exp(-8 * a40_E * ts) * 32 * math.pi * ts ** 2 / (3 * M_PL ** 2)))
        bounds.append({'v_A_over_v': ratio, 'a40_min_helium_per_s': a40_bbn,
                       'a40_min_helium_GeV': a40_bbn * HBAR_MEVS * 1e-3 if a40_bbn else None,
                       'a40_min_energy_GeV': a40_E, 'a40_min_energy_per_s': a40_E / (HBAR_MEVS * 1e-3),
                       'largest_energy_ratio_at_the_energy_bound': rmax})
    out['T6'] = {'Y_p_standard_this_estimate': Y0, 'x4_at_T_nuc_s': tnuc, 'detailed_balance_deviation': db_dev,
                 'low_temperature_rate_times_tau_n_minus_1': low_dev, 'dYp_d_eps': sens, 'Y_p_observed': YP_OBS,
                 'bounds': bounds, 'Q_QCD_MeV': Q_QCD, 'T_nuc_MeV': T_NUC}
    ok6 = (db_dev < 1e-9 and low_dev < 1e-5 and abs(Y0 - YP_OBS[0]) < 0.01 and sens['Fermi constant'] > 0 > sens['masses']
           and abs(sens['both'] - sens['Fermi constant'] - sens['masses']) < 0.01
           and all(abs(b_['largest_energy_ratio_at_the_energy_bound'] - 1) < 1e-4 for b_ in bounds)
           and all(b_['a40_min_energy_per_s'] > 1e3 * (b_['a40_min_helium_per_s'] or 0) for b_ in bounds)
           and all((b_['a40_min_helium_per_s'] or 0) <= (c_['a40_min_helium_per_s'] or 0) for b_, c_ in zip(bounds[:-1], bounds[1:])))
    rep.check('T6_ad_hoc_vacuum_before_BBN', ok6,
              'ESTIMATE (Born rates, entropy transfer of e+e- annihilation, Y_p = 2 X_n at T = %.3f MeV): the rates obey detailed '
              'balance (%.0e) and tend to 1/tau_n (%.0e); without the ad hoc vacuum Y_p = %.4f (observed %.3f +- %.3f) at x_4 = '
              '%.0f s; per unit A^2/v^2 the Fermi constant raises Y_p by %.3f, the masses lower it by %.3f (together %.3f); '
              '|Delta Y_p| < %.3f requires a_40 > %s for v_A/v = %s; the potential energy lambda A^4/4 stays below that of the '
              'radiation of an era that begins at x_4 = 0 only if a_40 > v_A^2 sqrt(lambda pi/6)/(e M_Pl) = %s (the numerical '
              'maximum of the ratio at this bound: %s), the stronger condition by more than %.0e: the ad hoc vacuum must be gone '
              'long before nucleosynthesis, and then it does not change it' % (
                  T_NUC, db_dev, low_dev, Y0, YP_OBS[0], YP_OBS[1], tnuc, sens['Fermi constant'], -sens['masses'], sens['both'],
                  2 * YP_OBS[1], ', '.join(('%.3g /s' % b_['a40_min_helium_per_s']) if b_['a40_min_helium_per_s'] else 'none'
                                           for b_ in bounds),
                  ', '.join('%g' % b_['v_A_over_v'] for b_ in bounds),
                  ', '.join('%.2e GeV = %.2e /s' % (b_['a40_min_energy_GeV'], b_['a40_min_energy_per_s']) for b_ in bounds),
                  ', '.join('%.6f' % b_['largest_energy_ratio_at_the_energy_bound'] for b_ in bounds),
                  min(b_['a40_min_energy_per_s'] / b_['a40_min_helium_per_s'] for b_ in bounds if b_['a40_min_helium_per_s'])))

    # ---------------- T7: the thermal relic and the lifetime
    # partial-wave unitarity of the s-wave, spin-averaged: (sigma v)_{chi chibar} <= 4 pi/(m^2 v_rel); thermal average
    # <1/v_rel> = sqrt(x/pi) (Maxwell-Boltzmann, relative velocity); <sigma_ann v> of FE-61 = (sigma v)_{chi chibar}/4
    def m_unitarity(scale=1.0, g=G_CHI, per=4.0, x1=1e7):
        svu = lambda m: (lambda x: scale * (4 * math.pi / m ** 2) * math.sqrt(x / math.pi) / per)
        f7 = lambda lm: math.log(relic(math.exp(lm), svu(math.exp(lm)), g=g, x0=3.0, x1=x1)[0] / OMEGA_DM_H2)
        return math.exp(brentq(f7, math.log(1e4), math.log(1e7), xtol=1e-6))
    m_conv = {'%.0e' % x1: m_unitarity(x1=x1) for x1 in (1e5, 1e6, 1e7)}
    m_max = m_conv['1e+07']
    m_singlet = m_unitarity(scale=0.5)
    m_all = m_unitarity(scale=2.0)
    m_dirac = m_unitarity(g=4, per=2.0)
    spec = json.loads((UM4 / 'outputs' / 'spectra.json').read_text())['U6_lifetime']
    req = sorted([e_ for e_ in spec['rows'] if abs(e_['lifetime_over_t0'] - 160.0 / 13.8) < 1e-9], key=lambda e_: e_['q_b_over_m'])

    def q_cross(mass):
        for a_, b_ in zip(req[:-1], req[1:]):
            if a_['omega_b_min_GeV'] >= mass > b_['omega_b_min_GeV']:
                la, lb = math.log(a_['omega_b_min_GeV']), math.log(b_['omega_b_min_GeV'])
                return a_['q_b_over_m'] + (la - math.log(mass)) / (la - lb) * (b_['q_b_over_m'] - a_['q_b_over_m'])
        return None
    q_star = {'base': q_cross(m_max), 'singlet only': q_cross(m_singlet), 'every channel': q_cross(m_all)}
    out['T7'] = {'unitarity_mass_GeV': m_max, 'end_point_convergence_GeV': m_conv, 'singlet_only_GeV': m_singlet,
                 'every_channel_GeV': m_all, 'one_dirac_species_GeV': m_dirac, 'H_min_GeV': spec['H_min_GeV'],
                 'lifetime_bound_rows_160Gyr': [{k: e_[k] for k in ('q_b_over_m', 'omega_b_min_GeV')} for e_ in req],
                 'q_b_over_m_above_which_a_relic_lives_160Gyr': q_star}
    ok7 = (abs(m_conv['1e+06'] / m_max - 1) < 2e-3 and m_singlet < m_max < m_all and 5e4 < m_max < 2e5
           and all(q_star[k] is not None for k in q_star) and q_star['every channel'] < q_star['base'] < q_star['singlet only']
           and all(e_['omega_b_min_GeV'] > m_all for e_ in req if e_['q_b_over_m'] <= 0.8))
    rep.check('T7_thermal_relic_and_lifetime', ok7,
              'with the largest s-wave annihilation that partial-wave unitarity allows, (sigma v)_{chi chibar} = 4 pi/(m^2 v_rel), '
              'the relic density of FE-61 equals Omega h^2 = 0.12 at omega_b = %.4g GeV (integrated to x = 1e5, 1e6, 1e7: %s GeV); '
              '%.3g GeV if only the singlet of the extra-time SU(2) annihilates, %.3g GeV if every channel is open (%.3g GeV for one '
              'Dirac species): heavier particles chi would be overproduced by freeze-out; the lifetime bound of um4_spectra.py U6 '
              '(160 Gyr, H = %.0f GeV) on omega_b is %s GeV for q_b/m_Psi = %s: it lies below the unitarity mass only for '
              'q_b > %.3f m_Psi (%.3f ... %.3f over the bookkeeping range): only strongly bound particles chi can be a thermal relic' % (
                  m_max, ', '.join('%.4g' % v_ for v_ in m_conv.values()), m_singlet, m_all, m_dirac, spec['H_min_GeV'],
                  ', '.join('%.3g' % e_['omega_b_min_GeV'] for e_ in req), ', '.join('%g' % e_['q_b_over_m'] for e_ in req),
                  q_star['base'], q_star['every channel'], q_star['singlet only']))

    # ---------------- T8: the binding that direct detection allows and the lifetime that it gives
    def eps_max(m):
        mu = m * M_N / (m + M_N)
        gmax = math.sqrt(lz_limit(m) / GEV2_CM2 * math.pi) / (mu * fH * M_N / (V_EW * M_H ** 2))
        return math.sqrt(gmax * m * V_EW / 2) / m                       # q_b/omega_b at the LZ limit (T4)

    def F_weak(eps):
        # F(u_b) of um4_spectra.py U4 for u_b = 1/sqrt(1 + eps^2), written without cancellation:
        # ln((1 + s)/u) - s with s = sqrt(1 - u^2) = eps/sqrt(1 + eps^2)
        s_ = eps / math.sqrt(1 + eps * eps)
        return math.log1p(s_) + 0.5 * math.log1p(eps * eps) - s_ if eps > 1e-3 else eps ** 3 / 3 - 3 * eps ** 5 / 10
    gam_max = req[0]['Gamma_max_GeV']
    rows8 = []
    for m in (1e4, 1e6, 1e8, 1e10, 1e12, 1e14, 1e16, M_PL):
        eps = eps_max(m)
        mP = m * math.sqrt(1 + eps * eps)
        s_b = eps / math.sqrt(1 + eps * eps)                            # q_b/m_Psi
        P_ = 2 / math.e * s_b ** 2
        F_ = F_weak(eps)
        Hmax = 2 * F_ * mP / math.log(P_ * mP / gam_max)
        ghx = 2 * eps * eps * m / V_EW
        rows8.append({'omega_b_GeV': m, 'q_b_over_omega_b_max': eps, 'F': F_, 'prefactor_P': P_, 'H_max_GeV': Hmax,
                      'g_hchi': ghx, 'perturbative': ghx < 4 * math.pi, 'q_b_over_H_max': eps * m / Hmax})
    e_test = 2e-3
    s_t = e_test / math.sqrt(1 + e_test ** 2)
    F_closed = math.log1p(s_t) + 0.5 * math.log1p(e_test ** 2) - s_t
    ok8 = (abs(F_closed / (e_test ** 3 / 3 - 3 * e_test ** 5 / 10) - 1) < 1e-9
           and all(r_['H_max_GeV'] < spec['H_min_GeV'] for r_ in rows8)
           and all(rows8[i + 1]['H_max_GeV'] > rows8[i]['H_max_GeV'] for i in range(len(rows8) - 1))
           and all(r_['q_b_over_H_max'] > 10 for r_ in rows8)
           and abs(math.log(rows8[-1]['q_b_over_omega_b_max'] / rows8[0]['q_b_over_omega_b_max'])
                   / math.log(rows8[-1]['omega_b_GeV'] / rows8[0]['omega_b_GeV']) + 0.25) < 0.01)
    m_np = next((r_['omega_b_GeV'] for r_ in rows8 if not r_['perturbative']), None)
    out['T8'] = {'rows': rows8, 'Gamma_max_GeV': gam_max, 'H_min_GeV': spec['H_min_GeV'], 'requirement': spec['requirement'],
                 'first_mass_with_g_hchi_above_4pi_GeV': m_np}
    rep.check('T8_binding_and_lifetime', ok8,
              'ESTIMATE: with the Higgs-portal binding the largest q_b/omega_b that LZ allows falls like omega_b^(-1/4): %s for '
              'omega_b = %s GeV; with it the particles chi live longer than 160 Gyr only for H < H_max = 2F(u_b) m_Psi/ln(P m_Psi/'
              'Gamma_max) (P = (2/e) (q_b/m_Psi)^2, the width of um4_spectra.py U4, valid since q_b > 10 H_max): %s GeV, below the '
              'bound H > %.0f GeV at every mass up to the Planck mass (g_hchi = %s: above 4 pi from %.0e GeV on, where the estimate '
              'is only formal): the particles chi bound by the Higgs portal cannot be the dark matter of UM-4' % (
                  ', '.join('%.1e' % r_['q_b_over_omega_b_max'] for r_ in rows8), ', '.join('%.2g' % r_['omega_b_GeV'] for r_ in rows8),
                  ', '.join('%.1e' % r_['H_max_GeV'] for r_ in rows8), spec['H_min_GeV'],
                  ', '.join('%.1e' % r_['g_hchi'] for r_ in rows8), m_np if m_np else float('nan')))

    # ---------------- T9: the binding by the gluon condensate
    G2_COND = 0.012                                                     # <(alpha_s/pi) G^2> in GeV^4 (SVZ)
    F_TG = 0.92                                                         # 1 - f_Tu - f_Td - f_Ts
    cG = 8 * M_N * F_TG / (9 * G2_COND)                                 # f_N = cG q_b^2/omega_b (GeV^-3 times GeV)
    rows9 = []
    for e_ in req:
        wb = e_['omega_b_min_GeV']
        qb = e_['q_b_over_m'] * e_['m_Psi_min_GeV']
        fN = cG * qb * qb / wb
        mu = wb * M_N / (wb + M_N)
        sig = mu * mu * fN * fN / math.pi * GEV2_CM2
        ghx = 2 * qb * qb / (wb * V_EW)
        sig_h = mu * mu * (ghx * fH * M_N / (V_EW * M_H ** 2)) ** 2 / math.pi * GEV2_CM2
        rows9.append({'q_b_over_m': e_['q_b_over_m'], 'omega_b_GeV': wb, 'q_b_GeV': qb, 'f_N_GeV-2': fN, 'sigma_SI_gluon_cm2': sig,
                      'sigma_SI_higgs_cm2': sig_h, 'LZ_limit_cm2': lz_limit(wb), 'gluon_ratio_to_LZ': sig / lz_limit(wb),
                      'higgs_ratio_to_LZ': sig_h / lz_limit(wb)})
    out['T9'] = {'condensate_GeV4': G2_COND, 'f_TG': F_TG, 'f_N_over_qb2_per_omega_b_GeV-3': cG, 'rows': rows9,
                 'vanishing_condensates': ['<W^2>', '<B^2>', '<J_f>', '<B_munu>']}
    ok9 = (abs(cG - 64.0) < 0.5 and all(r_['gluon_ratio_to_LZ'] > 1e20 for r_ in rows9)
           and all(r_['higgs_ratio_to_LZ'] > 1e3 for r_ in rows9))
    rep.check('T9_gluon_condensate_binding', ok9,
              'ESTIMATE: a binding of chi by the gauge-kinetic portal of the gluons through <(alpha_s/pi) G^2> = %.3f GeV^4 couples chi '
              'to nucleons through <N|(alpha_s/pi) G^2|N> = -(8/9) m_N f_TG: f_N = %.1f q_b^2/omega_b GeV^-3 (alpha_s cancels); at the '
              'lifetime bound of U6 (160 Gyr) sigma_SI = %s cm^2 for q_b/m_Psi = %s, above the LZ limit by factors %s (the Higgs '
              'portal with the same binding: %s); the other condensates of the portals vanish in the vacuum, so every binding by the '
              'portals of IN-16 couples chi to nucleons: dark matter of UM-4 needs a binding of chi to the fold that does not '
              'couple it to nucleons (OPEN)' % (
                  G2_COND, cG, ', '.join('%.1e' % r_['sigma_SI_gluon_cm2'] for r_ in rows9),
                  ', '.join('%g' % r_['q_b_over_m'] for r_ in rows9), ', '.join('%.0e' % r_['gluon_ratio_to_LZ'] for r_ in rows9),
                  ', '.join('%.0e' % r_['higgs_ratio_to_LZ'] for r_ in rows9)))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM4 / 'outputs' / 'thermal.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=float) + '\n')
    report = {'script': 'universe_model_4/code/um4_thermal.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM4 / 'reports' / 'thermal_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
