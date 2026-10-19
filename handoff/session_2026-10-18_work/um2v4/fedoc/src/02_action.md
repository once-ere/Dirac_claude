
# The action

All field equations of UM-2 follow from one action by varying it with respect to every field. This section writes out every
term of the action (IN-1 to IN-18) and says in plain words what it couples. The Standard-Model part has exactly the gauge
group, the fermion content (three generations, each with a right-handed neutrino) and the gauge couplings of the Standard Model,
but no Higgs field: the electroweak symmetry is broken at the tip of the hidden direction by a non-linear sigma field, and every
mass comes from the dependence of the wave functions on $x_0$. dirac16complex is a singlet of the Standard-Model gauge group and
couples to the Standard Model only through three gauge-invariant portals.

## The sum of all terms

@IN-1

The action is the sum of nine terms: Einstein-Lovelock gravity ($S_{\mathrm{EL}}$), the block stabiliser ($S_{\mathrm{stab}}$), the
field dirac16complex ($S_\Psi$), the gauge fields of SU(3), SU(2) and U(1)$_Y$ ($S_{\mathrm{gauge}}$), the Standard-Model fermions of
three generations ($S_{\mathrm{f}}$), the tip terms (the sigma field and the tip Yukawa couplings, $S_{\mathrm{tip}}$) and the three
portals of dirac16complex ($S_{\mathrm{I11}}$, $S_{\mathrm{I12}}$, $S_{\mathrm{I13}}$). Varying $S$ with respect to the metric gives the
gravitational equations FE-1; with respect to $\bar\Psi$ the dirac16complex equation FE-12; with respect to every fermion its Dirac
equation FE-14 to FE-19; with respect to the gauge fields the Yang-Mills equations FE-22 to FE-25; the boundary terms of the
variation give the boundary conditions FE-27 to FE-30. There is no Higgs field. Status: ASSUMED (the choice of the terms).

## Gravity

@IN-2

Gravity is the Einstein-Lovelock theory in eight dimensions with the author's weights. $\mathcal{L}_{(1)}$ is the Einstein-Hilbert
density (the Ricci scalar), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density and $\mathcal{L}_{(3)}$ the cubic Lovelock density; in eight
dimensions the series ends with $p = 3$ (the density of order 4 is a total derivative in eight dimensions). The couplings
$\alpha_{(p)} = w_{(p)}H^{2-2p}$ carry the author's dimensionless weights $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$, and the
cosmological constant is $\Lambda = -10H^2$. Gravity couples to every field through the metric that appears in every other term of
the action (in $\sqrt{\lvert g\rvert}$, in the contractions of indices and in the spin connection). Status: AUTHOR.

@IN-3

The Lovelock densities are built with the generalised Kronecker delta from $p$ Riemann tensors. Their key property
(Lovelock's theorem, STANDARD) is that their metric variation contains no derivatives of the metric higher than the second,
so that the field equations FE-1 remain second-order differential equations, as in general relativity. For $p = 1$ the formula
gives the Ricci scalar, for $p = 2$ the Gauss-Bonnet combination written in the second line. Status: STANDARD.

## The block stabiliser

@IN-4

The four directions $x_0, x_5, x_6, x_7$ form the "block". The order-0 metric (FE-31) scales all four of them with one block
scale $f = \mathrm{e}^{-a_4}b_4^{1/2}$. With the author's weights and $\Lambda$ alone there is no static block with attractive
four-dimensional gravity (FE-42); UM-2 therefore assumes a vacuum energy of the block, $\rho_{\mathrm{stab}}$, that falls with the
block scale as $f^{-8}$ (the law of a Casimir-type energy of a block of size $f$). Its normalisation $\kappa\rho_{\mathrm{stab}}(f_*)$ is
fixed by the requirement that the block be static (FE-43). It couples only to gravity: its energy-momentum tensor is FE-4.
Status: ASSUMED; its microscopic origin is OPEN.

## The field dirac16complex

@IN-5

dirac16complex $\Psi$ is the author's 16-component complex spinor field of eight dimensions. Its Lagrangian is the record's:
the symmetrised Dirac kinetic term (both $\Psi$ and $\bar\Psi$ are differentiated, so the action is real), the mass term with the
mass parameter $m_\Psi = 3H\mathcal{M} = H$, and the contact self-interaction $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$. The covariant
derivative $D_M$ contains the canonical spin connection (IN-7), through which $\Psi$ couples to gravity. $\Psi$ carries no colour,
weak isospin or hypercharge. Status: RECORD.

@IN-6

The Dirac matrices satisfy the Clifford algebra of the signature $(4, 4)$; the author's matrices are real $16 \times 16$
matrices, and the algebra holds exactly (31 checks of `code/um2_algebra.py`). The Dirac adjoint uses the matrix
$C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ (in four-four signature the usual $\gamma^0$ is replaced by the product of the four
space-like matrices). $\Gamma_4$ is the four-dimensional chirality. The author's operator $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$ has the
eigenvalues $\pm1$ and splits $\Psi$ into two halves, $\Psi_A$ and $\Psi_B$; it commutes with every interaction of the good sector, so
the two halves never mix (each carries one dark-matter species). The same algebra and adjoint serve every Standard-Model fermion.
Status: AUTHOR.

@IN-7

The spin connection couples every spinor to gravity: $\Omega_M$ is built from the vielbein $\mathbf{e}^a{}_M$ of the metric and the
Christoffel symbols, and it makes the Dirac matrices covariantly constant (verified symbolically). On the order-0 metric it is
the non-zero term FE-13. Status: STANDARD.

## The gauge fields

@IN-8

The gauge group is that of the Standard Model, SU(3) $\times$ SU(2) $\times$ U(1)$_Y$, in eight dimensions. The fields are in the
geometric normalisation: the eight-dimensional couplings $\hat g_3$, $\hat g_2$, $\hat g_1$ stand in front of the kinetic terms, and
the four-dimensional couplings are $g_i^2 = \hat g_i^2/V_\perp$ (FE-49). The gauge zero modes are flat in $x_0$ (FE-52), so the
four-dimensional theory has exactly the gauge interactions of QCD and of the electroweak theory. Status: ASSUMED (the
eight-dimensional form).

@IN-9

The field strengths are the standard non-abelian ones (STANDARD): $t^A$ are the generators of SU(3) and $\tau^I/2$ those of SU(2); the
commutator terms make the gluons and the $W$ bosons self-interacting, as in QCD and in the electroweak theory.

@IN-10

The physical electroweak fields are the canonically normalised combinations of the SU(2) and hypercharge fields: $W^+$ and $W^-$
from $W^1$ and $W^2$, the $Z$ and the photon $A$ from $W^3$ and $B$, rotated by the weak mixing angle $\theta_{\mathrm{W}}$ of the couplings.
$W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$ (DERIVED from the charge operator of IN-12); they are each other's
antiparticles. Status: STANDARD.

## The Standard-Model fermions

@IN-11

Each generation $i = 1, 2, 3$ contains the quark doublet $Q_i$ (left-handed up and down quarks, three colours, hypercharge
$\frac16$), the up-type singlet $u_{Ri}$ ($\frac23$), the down-type singlet $d_{Ri}$ ($-\frac13$), the lepton doublet $\ell_i$
(left-handed neutrino and charged lepton, $-\frac12$), the charged-lepton singlet $e_{Ri}$ ($-1$) and the right-handed neutrino
$\nu_{Ri}$ (a gauge singlet). These are eight-dimensional spinor fields with bulk masses $\mu_{\psi i}$; the doublets of a sector share
one bulk mass ($\mu_Q$, $\mu_\ell$). The bulk mass fixes the localisation of the four-dimensional zero mode along $x_0$, and with the
tip mixing it fixes the four-dimensional mass (FE-56 to FE-60). With this content the gauge anomalies cancel generation by
generation, exactly as in the Standard Model (DERIVED, exact fractions; a lepton generation without its quark generation would
leave the anomalies $\mathcal{A}_{SU(2)^2U(1)} = -1$ and $\mathcal{A}_{U(1)^3} = 3/2$): the three quark generations are required together
with the three lepton generations. Status: ASSUMED (the eight-dimensional form; the boundary conditions FE-29 are INVENTED).

@IN-12

Every fermion couples to gravity through the spin connection and to the gauge fields through its covariant derivative, with
the generators of its representation ($t^A$ for quarks, $\tau^I/2$ for doublets, the hypercharge $Y$). The electric charge is
$Q_{\mathrm{em}} = T_3 + Y$: $+\frac23$ and $-\frac13$ for the quarks, 0 and $-1$ for the leptons. Status: STANDARD.

## The tip: the sigma field and the Yukawa couplings (no Higgs particle)

@IN-13

At the regular tip $y = -L$ of the hidden direction, a non-linear sigma field $\Sigma$ (a unitary $2 \times 2$ matrix) breaks the
electroweak symmetry. Its kinetic term is the gauged non-linear sigma model of the electroweak chiral Lagrangian, located on the
seven-dimensional tip: it gives masses to $W^+$, $W^-$ and $Z$ and none to the photon (IN-15). $\Sigma$ has no radial mode, so there is
no Higgs particle; its three modes become the longitudinal $W^+$, $W^-$ and $Z$. The Yukawa terms $\mathcal{L}_{\mathrm{Y}}$ couple the
doublets to the singlets through $\Sigma$ with complex $3 \times 3$ matrices $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$, $\mathcal{Y}_d$ (generation indices $i$,
$j$); they mix the doublet and singlet zero modes at the tip and give the fermions their masses and their mixing (FE-30, FE-59,
FE-60). Every term is invariant under SU(2) $\times$ U(1)$_Y$ (IN-14), so the construction is consistent with the electroweak theory at
tree level; it is the Higgsless limit of the Standard Model, which conflicts with the observed Higgs boson at 125 GeV and lets the
longitudinal $W^+W^-$ scattering violate perturbative unitarity near 1.2 TeV (a conflict with data inherent in the order to omit
the Higgs particle). Status: INVENTED.

@IN-14

The covariant derivative of $\Sigma$ contains the SU(2) field from the left and the hypercharge field from the right, so that
$\Sigma$ transforms as $\Sigma \to U_L\,\Sigma\,U_Y^\dagger$. The tip terms are invariant under this transformation for arbitrary complex
tip matrices (DERIVED with random group elements, deviation $1.1\times10^{-14}$). Status: INVENTED.

@IN-15

In the unitary gauge $\Sigma = \mathbf{1}$ the sigma-field kinetic term becomes a mass term of $W^+$, $W^-$ and $Z$ on the tip. $W^+$ and $W^-$
share one mass (particle and antiparticle); the $Z$ term has the coefficient $\hat g_Z^2 = \hat g_2^2 + \hat g_1^2$ instead of $\hat g_2^2$
(at leading order the $Z$ is heavier by $1/\cos\theta_{\mathrm{W}}$, the custodial relation); the photon receives no term and stays massless.
On the static block this term becomes the Robin condition of the $W^\pm$ and $Z$ profiles (FE-51). Status: DERIVED.

## The portals of dirac16complex

$\Psi$ is a singlet of the Standard-Model gauge group, so it can couple to the Standard Model only through gauge-invariant
composite operators of the Standard-Model fields. UM-2 contains three of them; they respect every symmetry of QCD and of the
electroweak theory, and none of them breaks a gauge symmetry or gives a gauge boson a mass. Their strengths are fixed by the
cosmology (the relic density of the dark matter, the freeze-in of the fold bands, partial-wave unitarity).

@IN-16

I11 couples the vector current of $\Psi$ (both halves, including the massless fold bands) to the $B - L$ current of the
Standard-Model fermions of three generations: baryon number minus lepton number, with the charges $q_\psi$. $B - L$ is conserved in
the Standard Model and, with the right-handed neutrinos, free of gauge anomalies, so I11 is consistent with QCD and the electroweak
theory; every term is separately gauge invariant and generation blind. $c_{\mathrm{V}}$ is dimensionless and $\Lambda_\star$ is the common
scale of the portals. On the zero modes it becomes the contact interaction FE-70; its benchmark strength keeps the fold bands out of
equilibrium (FE-129). Status: INVENTED.

@IN-17

I12 couples the scalar density $\bar\Psi\Psi$ of dirac16complex to the gauge-kinetic invariants of the three gauge groups. Each
invariant is gauge invariant and a Lorentz scalar; the coupling acts as a field-dependent gauge coupling (FE-21) and does not
break any symmetry of QCD or of the electroweak theory. On the dark matter it is FE-71; it is set to the unitarity-safe
benchmark. Status: INVENTED.

@IN-18

I13 couples the $x_0$-chiral vector current of $\Psi$ (the projector $P_b$ selects one $x_0$-chirality) to the baryon-number current
of the quarks (one third per quark, three generations). The sum leaves out the direction $x_0$, for which the bilinear is not
Hermitian (DERIVED with the author's matrices: $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ is Hermitian for $M \ne x_0$ only). Baryon number is
conserved in QCD and in the perturbative electroweak theory, and $J^B_M$ is gauge invariant, so I13 is consistent with both. On the
zero modes it is the contact interaction FE-70, whose strength is fixed by the relic density of the dark matter (FE-126); it
vanishes on the fold bands (to $7\times10^{-14}$), which have no lower component. Status: INVENTED.
