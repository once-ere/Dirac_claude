DRAFT of the new prose of MODEL v4 (v3 notation; to be translated with NOTATION.md)

# How to read this document

This document DEFINES the model universe UM-2: its space and coordinates, its metric, its fields, every interaction among
them, the mechanism that gives the particles their masses, and what follows for gravity, for the dirac16complex field, for
the three neutrino flavours, for the dark sector and for the cosmology. It is self-contained: every equation it uses is
written here, and every symbol of every display equation is defined right below that equation.

Status labels (every statement carries one):
* AUTHOR: taken from the author's notebooks (the coordinates, the metric, the Lovelock weights, the gamma matrices, the
  mass parameter);
* RECORD: taken from the Revision record of this repository (a choice made there and kept);
* STANDARD: textbook physics or a measured value used as an input;
* ASSUMED: a choice made for this model;
* INVENTED: a new phenomenological ingredient of this model (an interaction or a field that the Standard Model does not have);
* DERIVED: computed and verified in this work (the verification is stated with the result);
* ESTIMATE: an order-of-magnitude evaluation, not a precision computation;
* OPEN: not resolved in this version.

The rule of the symbol lists: every display equation is followed by the list of all its symbols ("Symbols in (FE-n)." or
"Symbols in this equation."), each with its meaning, unit, value and status. A FIELD EQUATION carries the tag (FE-n), an
INTERACTION TERM of the action the tag (IN-n); the numbers are those of the inventory of UM-2 (one numbering for all the
documents of UM-2). Whenever a field equation or an interaction term is used, it is written out again with its tag and its
complete symbol list, so that the reader never has to look for a definition elsewhere. One symbol has one meaning throughout.
Units: hbar = c = 1 unless stated (a few equations of the uncertainty argument keep hbar and c visible).

Versions. Version 1 (2026-10-17): one Standard-Model generation. Version 2 (2026-10-18): three generations with three
neutrino flavours, their masses, mixing and flavour conversion; the chiral tip Z portal of version 1 removed. Version 3
(2026-10-18): the portal I13 and the relic; benchmark strengths of I11 and I12; the coupled Kohn-Sham solution in ten
environments; the thermal history; the magnitudes of the metric series and sigma_8; the Majorana alternative; the
corrections of the independent review. Version 4 (2026-10-18), by the author's order of 2026-10-18 (15:42) to organise and
present the solution better: the same physics and the same numbers as version 3, re-presented: every field equation and
every interaction term written out with its tag and its complete symbol list wherever it is used; every interaction
explained (what it couples, why it is consistent with QCD and the electroweak model) and analysed (strength, bounds); the
x0 mass mechanism presented first as the author's uncertainty argument, then by the exact x0 eigenvalue equations; one
symbol, one meaning (the symbols that version 3 used for several things have been given separate names).

# The fields of UM-2

The author's list (order of 2026-10-18), and the fields of UM-2 that realise it:

| author's field | UM-2 field | content | couples to | mass |
| Einstein-Lovelock gravity | metric g_MN (vielbein e^a_M) | graviton, KK gravitons, radion | every field (sqrt|g|, g^MN, spin connection) and itself | graviton massless |
| dirac16complex | Psi (16 complex Grassmann components) | halves Psi_A, Psi_B; fold bands (massless), bulk band (DM 44.35 TeV) | gravity (spin connection), itself (lambda), all SM fermions (I11), quarks (I13), gauge fields (I12) | fold bands massless |
| three-flavour left-handed neutrinos | upper components of L_i | nu_e, nu_mu, nu_tau (flavour) = U nu_i (mass) | W+-, Z, gravity, Psi (I11), Sigma at tip | 1.000, 8.712, 50.140 meV |
| left-handed electrons | lower component of L_1 | e_L | photon, W+-, Z, gravity, Psi (I11), Sigma | 0.511 MeV (with e_R) |
| right-handed electron singlet | e_R1 | e_R | photon, Z, gravity, Psi (I11), Sigma | |
| other two lepton generations (as v3) | L_2, L_3, e_R2, e_R3, nu_Ri | mu, tau, right-handed partners, three right-handed neutrinos | | |
| three quark generations | Q_i, u_Ri, d_Ri | u,d,c,s,t,b | gluons, photon, W+-, Z, gravity, Psi (I11, I13), Sigma | |
| gluons | G^alpha_M | 8 | quarks, themselves, Psi (I12), gravity | 0 |
| photons | A_M (from W3, B) | | charged fermions, W+-, Psi (I12) | 0 |
| W+, W-, Z | W^1, W^2, W^3, B combinations | W+ charge +e, W- charge -e, Z neutral | fermions, photon, each other, Sigma at tip, Psi (I12) | 80.36, 80.36, 91.19 GeV |
| no Higgs particle | tip sigma field Sigma in SU(2) (no radial mode) | 3 Goldstones = longitudinal W+, W-, Z | W, B, fermions at tip | no particle |
| (version 3) | block stabiliser rho_b(f) | vacuum energy of the block | gravity | |

# The x0 mass mechanism: the author's argument

Step 1 (periodicity). Every wave function of UM-2 depends on x0 through z = 6 H x0 and y(z), so
  Phi(x0 + l0, x1, ..., x7) = Phi(x0, x1, ..., x7),   l0 = pi/(6H).
Step 2 (localisation). A wave function localised in x0 (within one period) with spread Delta x0 has a spread of the
hidden momentum p_{x0} = -i hbar d/dx0 that obeys
  Delta x0 Delta p_{x0} >= hbar/2.
Step 3 (momentum is mass). The hidden momentum is invisible to a four-dimensional observer; its energy is rest energy.
For a field of bulk mass mu the dispersion relation of eight dimensions,
  E^2 = c^2 |p|^2 + c^2 p_{x0}^2 + mu^2 c^4,
seen at rest in four dimensions (p = 0) gives the effective mass
  m_eff^2 c^4 = c^2 <p_{x0}^2> + mu^2 c^4.
Step 4 (kinetic energy p^2/m). For <p_{x0}^2> << mu^2 c^2 the hidden kinetic energy
  E_kin = <p_{x0}^2>/(2 mu)
adds to the rest energy: m_eff c^2 = mu c^2 + <p_{x0}^2>/(2mu).
Step 5 (the bound). With <p_{x0}^2> >= (Delta p_{x0})^2 >= hbar^2/(4 Delta x0^2) and mu = 0:
  m_eff >= hbar/(2 c Delta x0).
In the proper hidden length s (the chart-independent measure of localisation; ds = f dy) the author's estimate is
  m_H = hbar c/(2 Delta s).
Step 6 (exceptions). A wave function whose x0 dependence costs no energy is massless even if localised: graviton, photon
(and the gluons: SU(3) unbroken) by general covariance and gauge invariance (flat profile an exact eigenfunction with zero
eigenvalue); the fold bands of dirac16complex by chirality (chiral zero modes). Their uncertainty estimate (70.6 TeV for
the photon) is NOT their mass: the argument is a heuristic that the exact equations make precise below.
