# The gauge fields: gluons, photons, $W^+$, $W^-$ and $Z$ (ASSUMED structure, STANDARD content)

The gauge group is $SU(3)_c\times SU(2)_L\times U(1)_Y$, with eight-dimensional gauge fields: the gluons $G^A_M$ ($A = 1, \dots, 8$), the
$SU(2)$ fields $W^I_M$ ($I = 1, 2, 3$) and the hypercharge field $B_M$:

@@IN-8@@

with the field strengths

@@IN-9@@

In this geometric normalisation the couplings stand in front of the kinetic terms and not in the covariant derivatives; the
fields have the dimension of a mass, the eight-dimensional couplings $\hat g_3$, $\hat g_2$, $\hat g_1$ the dimension
$\mathrm{GeV}^{-2}$, and the four-dimensional couplings are $g_3^2 = \hat g_3^2/V_\perp$, $g_2^2 = \hat g_2^2/V_\perp$, $g_1^2 = \hat g_1^2/V_\perp$,
where $V_\perp$ is the proper volume of the block per unit 4-volume (the section on dimensional reduction). The physical electroweak
fields are canonically normalised (divided by the coupling):

@@IN-10@@

**$W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$** ($W^-$ is the antiparticle of $W^+$; the charge follows from the
isospin raising and lowering components of $W^1 \mp \mathrm{i}W^2$ and $Y = 0$ of the $W$ fields); $Z$ and the photon $A$ are neutral
(DERIVED). The quadratic part of the gauge action in terms of the canonical fields is (DERIVED; $W^{\pm}{}_{MN}$, $Z_{MN}$, $A_{MN}$ the
abelian field strengths of FE-25 below)

$$
\frac{1}{\hat g_2^2}\,W^I_{MN}W^{IMN} + \frac{1}{\hat g_1^2}\,B_{MN}B^{MN} = 2\,W^{+}{}_{MN}W^{-}{}^{MN} + Z_{MN}Z^{MN} + A_{MN}A^{MN}
 + \big(\text{cubic and quartic terms}\big),
$$
<!-- symbols: AUTO -->

and the non-abelian (cubic and quartic) terms of $W^I_{MN}W^{IMN}$ contain the vertices $W^+W^-\gamma$ (strength $e$), $W^+W^-Z$ (strength
$g_2\cos\theta_{\mathrm{W}}$) and the quartic vertices $W^+W^-W^+W^-$, $W^+W^-\gamma\gamma$, $W^+W^-Z\gamma$, $W^+W^-ZZ$; every vertex conserves the
electric charge, so a single $W^+$ or $W^-$ always comes with a charged partner (STANDARD). With the fermion currents of the three
generations,

@@FE-20@@

and the effective inverse couplings produced by the portal I12 (a field-dependent coupling, the section on the interactions),

@@FE-21@@

the gauge-field equations are (in the unitary gauge $\Sigma = \mathbf{1}$ of the tip sigma field, geometric fields):

@@FE-22@@

@@FE-23@@

@@FE-24@@

To linear order in the fields (I12 neglected) they become the equations of the physical fields:

@@FE-25@@

The tip terms are mass terms for $W^\pm$ and $Z$ only: the photon receives none and stays massless; for an $x_0$ profile these tip
terms become the Robin conditions of the $x_0$ eigenvalue problem (the section on the $x_0$ mass mechanism). The boundary conditions
of gravity and of the gauge fields at the fold and the tip are

@@FE-27@@

($F$ the $x_0$ profile of the field). The energy-momentum tensor of the gauge fields is

@@FE-7@@

# The fermions: the three-flavour left-handed neutrinos, the electrons, two more lepton generations and three quark generations (ASSUMED structure, INVENTED boundary assignment)

Each multiplet is an eight-dimensional spinor of the same Clifford algebra (16 components times its gauge indices). There are three
generations, $i = 1, 2, 3$, with the same quantum numbers:

| field ($i = 1, 2, 3$) | members | $SU(3)_c$ | $SU(2)_L$ | $Y$ | electric charges $Q_{\mathrm{em}} = T_3 + Y$ | zero mode |
| --- | ----- | -- | -- | -- | ---- | -- |
| $Q_i$ | left-handed up and down, charm and strange, top and bottom quarks | 3 | 2 | $1/6$ | up-type $2/3$, down-type $-1/3$ | $\Gamma_4 = +1$ |
| $u_{Ri}$ | right-handed up, charm, top quarks | 3 | 1 | $2/3$ | $2/3$ | $\Gamma_4 = -1$ |
| $d_{Ri}$ | right-handed down, strange, bottom quarks | 3 | 1 | $-1/3$ | $-1/3$ | $\Gamma_4 = -1$ |
| $\ell_i$ | $\nu_e$ with the left-handed electron, $\nu_\mu$ with the left-handed muon, $\nu_\tau$ with the left-handed tau | 1 | 2 | $-1/2$ | neutrino 0, charged lepton $-1$ | $\Gamma_4 = +1$ |
| $e_{Ri}$ | right-handed electron, muon, tau | 1 | 1 | $-1$ | $-1$ | $\Gamma_4 = -1$ |
| $\nu_{Ri}$ | three right-handed neutrinos | 1 | 1 | 0 | 0 | $\Gamma_4 = -1$ |

The author's list is contained in this table: the **three-flavour left-handed neutrinos** are the upper (neutral) components of the
three lepton doublets $\ell_i$; the **left-handed electrons** are the lower component of $\ell_1$ and the **right-handed electron
singlet** is $e_{R1}$; the other two lepton generations and their right-handed partners ($\ell_2$, $\ell_3$, $e_{R2}$, $e_{R3}$) and the
three right-handed neutrinos are those of version 3; the **three quark generations** are $Q_i$, $u_{Ri}$, $d_{Ri}$. The action is

@@IN-11@@

with the covariant derivative (the same canonical spin connection as for $\Psi$, and the gauge fields) and the electric charge

@@IN-12@@

The bulk masses are diagonal in the generation index, and the doublet bulk mass is the same for the three generations of a sector
($\mu_\ell$ for the leptons, $\mu_Q$ for the quarks; ASSUMED), while the singlet bulk masses of $e_{Ri}$, $\nu_{Ri}$, $u_{Ri}$, $d_{Ri}$ differ
from generation to generation. Varying the action gives the Dirac equations of the six multiplets, each with its gravitational
coupling (in $D_M$), its gauge couplings (in $D_M$), its portal terms (I11 for every multiplet, I13 for the quarks) and its tip
Yukawa term (with $\delta_{\mathrm{tip}}$, the density that places a term on the tip):

@@FE-14@@

@@FE-15@@

@@FE-16@@

@@FE-17@@

@@FE-18@@

@@FE-19@@

Their energy-momentum tensor is

@@FE-6@@

**Boundary conditions.** With the selection projector $P_{\mathrm{sel}}$, which commutes with every four-dimensional Lorentz generator
(DERIVED), the conditions at the fold ($y = 0$) and at the tip ($y = -L$) are

@@FE-29@@

These are self-adjoint boundary conditions of the Dirac operator (DERIVED). At the tip they are modified by the tip Yukawa terms,
which turn into the self-adjoint mixing conditions (DERIVED: the boundary form vanishes identically for every complex tip matrix,
sympy, 42 real variables)

@@FE-30@@

(the choice of the tip matrices is ASSUMED; it is explained in the section on the $x_0$ mass mechanism). The result (DERIVED): every
doublet field has exactly one four-dimensional Weyl zero mode with $\Gamma_4 = +1$ and every singlet field exactly one with
$\Gamma_4 = -1$, all localised at the fold and all in the two blocks selected by $P_{\mathrm{sel}}$, which lie in the half $\mathcal{B} = -1$.
The zero-mode spectrum is three Standard-Model generations, each with its right-handed neutrino.

**Anomaly cancellation generation by generation (DERIVED, exact fractions).** Writing every zero mode as a left-handed Weyl field (a
right-handed field of hypercharge $Y$ as a left-handed one of hypercharge $-Y$), the gauge anomaly coefficients of one generation are

$$
\mathcal{A}_{\mathrm{SU(3)^2U(1)}} = \sum_{\text{triplets}}N_{\mathrm{dbl}}\,Y = 2\cdot\frac16 - \frac23 + \frac13 = 0,\qquad
\mathcal{A}_{\mathrm{SU(2)^2U(1)}} = \sum_{\text{doublets}}N_{\mathrm{col}}\,Y = 3\cdot\frac16 - \frac12 = 0,
$$
<!-- symbols: AUTO -->

$$
\mathcal{A}_{\mathrm{U(1)^3}} = \sum N_{\mathrm{col}}N_{\mathrm{dbl}}\,Y^3 = \frac{1}{36} - \frac89 + \frac19 - \frac14 + 1 = 0,\qquad
\mathcal{A}_{\mathrm{grav^2U(1)}} = \sum N_{\mathrm{col}}N_{\mathrm{dbl}}\,Y = 1 - 2 + 1 - 1 + 1 = 0,
$$
<!-- symbols: AUTO -->

and $\mathcal{A}_{\mathrm{SU(3)^3}}$ (left-handed minus right-handed colour triplets) $= 2 - 1 - 1 = 0$; the twelve $SU(2)$ doublets of
three generations are an even number (no Witten anomaly). The anomalies cancel generation by generation; three lepton generations
with a single quark generation would leave $\mathcal{A}_{\mathrm{SU(2)^2U(1)}} = -1$ and $\mathcal{A}_{\mathrm{U(1)^3}} = 3/2$, so the second
and third quark generations are required together with the second and third lepton generations (DERIVED).

**QCD (STANDARD).** The gluons are the massless $x_0$ zero modes of $G^A_M$. Below the QCD scale the quarks are confined into
hadrons; the top quark decays (into $W^+$ and a bottom quark) before it can form one. The baryons of the cosmology are the protons
(two up quarks and a down quark, charge $+1$) and the neutrons (an up quark and two down quarks, charge 0), whose masses
$m_{\mathrm{p}} = 938.3$ MeV and $m_{\mathrm{n}} = 939.6$ MeV come from QCD; they are inputs of the cosmology. The QCD scale depends on the
block through $g_3^2 = \hat g_3^2/V_\perp$ (the section on the coupled solution).

# No Higgs particle: the tip sigma field (INVENTED for this geometry)

At the regular tip a non-linear sigma field $\Sigma(x) \in SU(2)$ carries the electroweak symmetry breaking, and the tip Yukawa terms
couple the doublets to the singlets:

@@IN-13@@

with the covariant derivative and the gauge transformation

@@IN-14@@

with four complex $3\times3$ tip Yukawa matrices $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$, $\mathcal{Y}_d$ (the upper component of
$\Sigma^\dagger\ell_i$ couples to $\nu_R$, the lower one to $e_R$). $\Sigma$ has no radial mode, so there is no Higgs particle; its three
would-be Goldstone modes become the longitudinal $W^+$, $W^-$ and $Z$. Every term is $SU(2)_L\times U(1)_Y$ invariant, the Yukawa terms for
arbitrary complex generation matrices (DERIVED with random group elements and random matrices, deviation $1.1\times10^{-14}$). In the
unitary gauge $\Sigma = \mathbf{1}$ the first term is

@@IN-15@@

which gives $W^+$ and $W^-$ one common mass (they are particle and antiparticle), gives the $Z$ a mass larger by $1/\cos\theta_{\mathrm{W}}$ at
leading order (custodial symmetry: $\hat g_Z^2 = \hat g_2^2/\cos^2\theta_{\mathrm{W}}$), and leaves the photon massless. The Yukawa terms mix
the doublet and singlet zero modes at the tip and give the fermions their masses and their mixing (the tip mixing conditions FE-30).
The equations of motion of $\Sigma$ are the Noether identities of the gauge symmetry (STANDARD for a gauged non-linear sigma model):

@@FE-26@@

in the unitary gauge they are not independent of the gauge-field equations. The energy-momentum tensor of the tip terms is

@@FE-8@@

(zero for the hidden components; its gravitational effect is part of the $W^\pm$, $Z$ and fermion rest energies counted in the plasma).

