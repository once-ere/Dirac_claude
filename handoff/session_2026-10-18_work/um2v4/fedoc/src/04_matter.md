
# The matter fields

## dirac16complex

The terms of the action that contain $\bar\Psi$ are $S_\Psi$ (IN-5) and the three portals (IN-16 to IN-18). Varying them with respect to
$\bar\Psi$ (the kinetic term after an integration by parts, which turns $-(D_M\bar\Psi)\gamma^M\Psi$ into $\bar\Psi\gamma^MD_M\Psi$) gives

@@
\frac{\Delta S}{\Delta\bar\Psi} = \sqrt{\lvert g\rvert}\,\Big[\gamma^MD_M\Psi - \Big(m_\Psi + \lambda\,\bar\Psi\Psi
 + \frac{\mathcal{F}}{\Lambda_\star^3}\Big)\Psi + \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,J^{B-L}_M\gamma^M\Psi
 + \mathrm{i}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}J^{B}_M\gamma^MP_b\Psi\Big] = 0,
@@

which is the field equation of dirac16complex:

@FE-12

**The terms.** $\gamma^MD_M\Psi$ is the eight-dimensional Dirac operator with the canonical spin connection (gravity). On the right,
$m_\Psi$ is the mass parameter, $\lambda\bar\Psi\Psi$ the mean field of the contact self-interaction, and $\mathcal{F}/\Lambda_\star^3$ the I12 term:
the gauge-field invariants act on $\Psi$ as an extra, field-dependent mass. The $c_{\mathrm{V}}$ term is I11: the $B - L$ current of the
Standard-Model fermions acts on $\Psi$ as a vector potential. The $c_{\mathrm{A}}$ term is I13: the baryon-number current acts on the
$x_0$-chirality selected by $P_b$ only. So dirac16complex couples to gravity, to itself, to every fermion (through $J^{B-L}$ and $J^B$) and
to every gauge field (through $\mathcal{F}$). Status: DERIVED. It is reduced exactly to a two-component problem in every block (FE-56), solved
exactly for the free spectrum (FE-62) and by Kohn-Sham theory with the mean fields of every other field (FE-63 to FE-73).

@FE-13

**The terms.** On the order-0 metric (FE-31) the spin connection contracted with the Dirac matrices has two parts: a term along $\gamma^{x_0}$
of strength $\frac32H/f$, from the warping of the extra times along the hidden direction ($\mathrm{e}^{2Hy}$ in FE-32), and a term along
$\gamma^{x_4}$ from the time dependence of the metric functions $a_4$ and $b_4$. It vanishes only in flat four-plus-four space ($H = 0$,
constant $a_4$, $b_4$), so the coupling of every spinor to gravity is non-trivial. The prefactors of the reduction ansatz of FE-56 remove
it exactly. Status: DERIVED (exact for every $a_4$, $b_4$ and on both halves of a period).

## The Standard-Model fermions

Varying $S_{\mathrm{f}}$ (IN-11), the tip action (IN-13) and the portals I11, I13 with respect to the adjoint of every multiplet gives
its Dirac equation. The quark doublets:

@FE-14

**The terms.** $\gamma^MD_MQ_i$ contains gravity (the spin connection) and the gauge fields: gluons, $W$ and $B$ (IN-12). $\mu_Q$ is the common bulk
mass of the three quark doublets, which localises their zero modes at the fold. The $c_{\mathrm{V}}$ term is I11 (the vector current of
dirac16complex acting with the $B - L$ charge $q_Q = \frac13$), the $c_{\mathrm{A}}$ term I13 (the $x_0$-chiral current of dirac16complex acting
with the baryon number $\frac13$). The last term is the tip Yukawa coupling: at $y = -L$ the doublet couples, through $\Sigma$ and the tip
matrices $\mathcal{Y}_u$, $\mathcal{Y}_d$, to the singlets $u_{Rj}$, $d_{Rj}$ of every generation $j$. Status: DERIVED. Solved on the static block by the zero
modes and the tip mixing (FE-56 to FE-60; exact roots). The portal terms act on the quarks as mean fields of the vector densities of
dirac16complex; they are neglected, because in every environment the density of the dark matter is far below that of the
Standard-Model fermions, so they are far smaller than the shifts of dirac16complex by the quarks (FE-72) (ESTIMATE; not computed).

@FE-15

**The terms.** The up-type singlets of the three generations (the right-handed up, charm and top quarks) couple to gravity, gluons and
$B$ (they carry no weak isospin), have the bulk mass $\mu_{\psi i}$ of their generation, feel I11 with $q_{u_R} = \frac13$ and I13 with the
baryon number $\frac13$, and couple at the tip to the upper component of $\Sigma^\dagger Q_j$ through the conjugate tip matrix. Status:
DERIVED; exact roots for the up, charm and top quarks.

@FE-16

**The terms.** As FE-15 for the down-type singlets (the right-handed down, strange and bottom quarks) with the lower component of
$\Sigma^\dagger Q_j$ and the tip matrix $\mathcal{Y}_d$; in UM-2 the tip mixing matrix of this sector is the CKM matrix (FE-30). Status: DERIVED.

@FE-17

**The terms.** The lepton doublets contain the three flavours of left-handed neutrinos and the left-handed charged leptons (electron,
muon, tau). They couple to gravity, $W$ and $B$ (no colour), have the common bulk mass $\mu_\ell$, feel I11 with $q_\ell = -1$ and no I13 term
(leptons carry no baryon number), and couple at the tip to the right-handed neutrinos (through $\mathcal{Y}_\nu$) and to the right-handed
charged leptons (through $\mathcal{Y}_e$). One doublet zero mode serves the three generations. Status: DERIVED; exact roots for the three
neutrinos and the three charged leptons.

@FE-18

**The terms.** The right-handed charged leptons of the three generations (electron, muon and tau singlets) couple to gravity and to $B$,
have their bulk masses, feel I11 with $q_{e_R} = -1$, and couple at the tip to the lower component of $\Sigma^\dagger\ell_j$. Status: DERIVED;
exact roots for the electron, muon and tau with the tip matrix $\mathbf{1}$.

@FE-19

**The terms.** The right-handed neutrinos are gauge singlets: no gauge field acts on them; they couple to gravity, to dirac16complex
through I11 ($q_{\nu_R} = -1$), and at the tip to the upper component of $\Sigma^\dagger\ell_j$. Their zero modes are sharply localised at the
fold ($c_R = -31$ to $-35$), so their values at the tip are tiny; mixed there with the doublet zero mode they give the small Dirac
masses of the three neutrinos (FE-100). They are never thermalised (FE-134). Status: DERIVED.

## The gauge fields

@FE-20

**The terms.** The currents are the sources of the gauge fields, summed over the three generations: $J_3^{AN}$ (colour) from the quarks,
$J_2^{IN}$ (weak isospin) from the doublets, $J_1^N$ (hypercharge) from every multiplet with its hypercharge $Y_\psi$; the electromagnetic
current $J_{\mathrm{em}}$ and the charged currents $J_2^\pm$, the sources of the photon and of $W^\pm$, are combinations of them. Status: STANDARD.

The gauge kinetic term IN-8 and the portal I12 (IN-17) contain the same invariants; for the gluons together

@@
-\frac14\Big(\frac{1}{\hat g_3^2} + \frac{4c_{\mathrm{G}}\,\bar\Psi\Psi}{\Lambda_\star^3}\Big)G^A_{MN}G^{AMN},
@@

and likewise for $W$ and $B$. The scalar density of dirac16complex therefore changes the effective couplings:

@FE-21

**The terms.** Where dirac16complex has a scalar density $\bar\Psi\Psi$, every gauge coupling is shifted by the I12 coefficient of its group.
In four dimensions this is the coupling shift of FE-79 (at most $1.7\times10^{-16}$ at the dark-matter freeze-out). Status: DERIVED.

Varying the gauge action with these couplings, the fermion action (through the covariant derivatives) and the tip action with respect
to the gauge fields gives the Yang-Mills equations:

@FE-22

**The terms.** The covariant divergence of the gluon field strength (with the field-dependent coupling of FE-21) plus the commutator term
(the self-interaction of the gluons) equals the colour current of the quarks. There is no tip term: the gluons do not couple to $\Sigma$.
Status: DERIVED. On the static block the gluon zero mode is exactly massless (flat $x_0$ profile, FE-50 to FE-52); below the confinement
scale QCD enters through the nucleon masses and the condensates (FE-74, FE-75).

@FE-23

**The terms.** The SU(2) equation (matrix form) has, besides the isospin current, the tip current of the sigma field in the unitary gauge
$\Sigma = \mathbf{1}$ ($N$ runs over the tip directions): a mass term for the charged components $W^1$, $W^2$ and for the combination
$W^3 - B$ only. Status: DERIVED. On the static block it is solved by the $x_0$ reduction (FE-50) with the Robin tip condition (FE-51).

@FE-24

**The terms.** The hypercharge equation is abelian (no commutator); its source is the hypercharge current, and the tip term (with the
opposite sign of FE-23) acts on $W^3 - B$ only. Status: DERIVED.

To linear order in the fields the commutators drop out, and the combinations of IN-10 decouple. For the photon, for example,

@@
\nabla_MA^{MN} = \frac{\hat g_1^2\,\nabla_MW^{3MN} + \hat g_2^2\,\nabla_MB^{MN}}{\hat g_1\hat g_2\hat g_Z}
 = \frac{\hat g_1\hat g_2}{\hat g_Z}\,\big(J_2^{3N} + J_1^N\big),
@@

because the tip terms of the third component of FE-23 and of FE-24, multiplied by $\hat g_2^2$ and $\hat g_1^2$, cancel. The same steps for
$W^\pm$ and $Z$ give

@FE-25

**The terms.** $W^+$ and $W^-$ are sourced by the charged currents and have the tip mass term with $\hat g_2^2$; the $Z$ is sourced by the neutral
current $J_2^3 - \sin^2\theta_{\mathrm{W}}J_{\mathrm{em}}$ and has the tip mass term with $\hat g_Z^2$; the photon is sourced by the electromagnetic
current with the coupling $\hat e$ and has no tip term, so it stays massless. Status: DERIVED (exact at linear order). The tip terms become
the Robin conditions FE-51; the $W^\pm$ and $Z$ masses and the tree-level $Z$ widths of three generations reproduce the measured values
(residual $2.7\times10^{-12}$ in the recomputed widths; the neglected electroweak loop corrections are $4\times10^{-3}$ of the total width).

## The tip sigma field

@FE-26

**The terms.** The sigma field carries the current $j_\mu$ (in the unitary gauge the mass current of $W^I$ and $B$). Its field equation states
that this current is covariantly conserved up to the tip Yukawa terms, which transfer isospin between the doublets and the singlets.
It is not an independent equation: the covariant divergence of the left side of FE-23 vanishes identically, so the covariant
divergence of its right side, evaluated with the fermion equations FE-14 to FE-19, gives exactly this equation (the Noether identity
of the gauge symmetry). In the unitary gauge it therefore holds automatically, and the three modes of $\Sigma$ are the longitudinal
$W^+$, $W^-$ and $Z$. Status: STANDARD (for a gauged non-linear sigma model).

## The boundary conditions

The hidden direction is periodic with the period $\pi/(6H)$; each half of a period is the interval $-L \le y \le 0$, joined to the other
half at the fold $y = 0$ by the reflection $z \to \pi - z$ and closed at the regular tip $y = -L$. The variational principle with these
boundaries gives:

@FE-27

**The terms.** At the fold an $x_0$ profile $F$ is even (zero derivative) or odd (zero value) under the reflection; at the tip the boundary
term of the variation gives the natural (Robin) condition of the tip term (zero derivative where there is no tip term). Status:
DERIVED. For an $x_0$ profile they are FE-51.

@FE-28

**The terms.** At the fold the even modes of dirac16complex satisfy $(1 - \gamma^{x_0})\Psi = 0$ and the odd ones $(1 + \gamma^{x_0})\Psi = 0$
(both parities are modes of the full period); at the tip $(1 - \gamma^{x_0})\Psi = 0$. The conditions are Lagrangian for the boundary form of
the Dirac operator, so the operator is self-adjoint. Status: DERIVED. In the block form they are FE-69.

@FE-29

**The terms.** $P_{\mathrm{sel}}$ selects the two blocks (of the half $\mathcal{B} = -1$) in which the Standard-Model zero modes live. The conditions
give every doublet exactly one Weyl zero mode with $\Gamma_4 = +1$ (left-handed) and every singlet exactly one with $\Gamma_4 = -1$
(right-handed), all localised at the fold: the four-dimensional fermion content is exactly that of three Standard-Model generations,
each with its right-handed neutrino. Status: INVENTED (the conditions), self-adjoint DERIVED.

@FE-30

**The terms.** The tip Yukawa terms are equivalent to these mixing conditions between the lower components $b$ and upper components $a$ of
the doublet ($L$) and singlet ($R$) solutions at the tip, with the tip mixing number $\mathcal{K}$ for one generation and the $3 \times 3$ tip
matrices of each sector for three generations. UM-2 takes $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, $\mathcal{K}_\nu = U$ (PMNS) and $\mathcal{K}_d = V_{\mathrm{CKM}}$, so
the mixing matrices of the leptons and quarks are those measured. Status: DERIVED (self-adjoint for every complex matrix, sympy, 42
real variables), the choice of the tip matrices ASSUMED; the normalisation that relates $\mathcal{K}$ to the Yukawa matrices $\mathcal{Y}$ of the
action is not fixed (OPEN). Solved exactly by the mass conditions FE-59 and FE-60.
