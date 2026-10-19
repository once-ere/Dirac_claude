
# Gravity

## The Einstein-Lovelock equations

Varying the gravitational action IN-2 with respect to the inverse metric gives, up to a total derivative,

@@
\Delta S_{\mathrm{EL}} = \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)MN}
 + \Lambda\,g_{MN}\Big)\Delta g^{MN},
@@

because the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ is $\sqrt{\lvert g\rvert}\,\mathcal{E}_{(p)MN}\Delta g^{MN}$ (the defining property of the
Lovelock tensor $\mathcal{E}_{(p)}$, STANDARD) and the variation of $\sqrt{\lvert g\rvert}$ is $-\frac12\sqrt{\lvert g\rvert}\,g_{MN}\Delta g^{MN}$. The
variation of the rest of the action defines the energy-momentum tensor (FE-2), $\Delta S_{\mathrm{m}} = -\frac12\int\mathrm{d}^8X\sqrt{\lvert g\rvert}\,
\mathcal{T}_{MN}\Delta g^{MN}$; the sum of the two vanishes for every $\Delta g^{MN}$:

@FE-1

**The terms.** $\mathcal{E}_{(1)}$ is the Einstein tensor $R^M{}_N - \frac12\delta^M_NR$ of general relativity; $\mathcal{E}_{(2)}$ (Gauss-Bonnet) and
$\mathcal{E}_{(3)}$ (cubic Lovelock) are the higher-order Lovelock tensors, products of two and three curvature tensors contracted with the
generalised Kronecker delta, weighted by $\alpha_{(2)} = H^{-2}/32$ and $\alpha_{(3)} = H^{-4}/1152$. $\Lambda\delta^M_N$ is the
eight-dimensional cosmological constant. The right side is the energy-momentum tensor of every field (FE-3), multiplied by the
gravitational coupling $\kappa = 8\pi G_8$. These equations couple the metric to every field of UM-2. Each $\mathcal{E}_{(p)}$ contains at
most second derivatives of the metric, so the system is of second order. Status: AUTHOR (the weights and $\Lambda$), the equations
DERIVED from the action. They are solved exactly at order 0 (FE-38 to FE-43: the residual of the stored static block in the printed
equations is $3.9\times10^{-13}$ of the largest term) and at the first order through the four-dimensional reduction (FE-48, FE-49).

## The energy-momentum tensors

@FE-2

**The terms.** $\mathcal{T}_{MN}$ is the response of the matter action $S_{\mathrm{m}}$ (every term of IN-1 except $S_{\mathrm{EL}}$) to a
change $\Delta g^{MN}$ of the metric (for spinors the change is made in the vielbein, which carries the metric). Its time-time
component gives the energy density $\rho$ and its diagonal space-like components the pressures $p_M$ along each direction: $p_0$
along the hidden direction $x_0$, $p_3$ along ordinary space, $p_5$ along the extra times. Every source of UM-2 is diagonal on the
order-0 metric, with one pressure for $x_1, x_2, x_3$ and one for $x_5, x_6, x_7$; $\bar p$ is the pressure averaged over the four block
directions, the hidden pressure. Status: STANDARD.

@FE-3

**The terms.** The total source is the sum of the energy-momentum tensors of the stabiliser (FE-4), of dirac16complex (FE-5), of the
Standard-Model fermions (FE-6), of the gauge fields (FE-7), of the tip terms (FE-8) and of the three portals (FE-9, FE-10). At order 0
the stabiliser dominates; the matter terms enter the block through their block averages (FE-45 to FE-47): today their size relative
to the stabiliser is $2.4\times10^{-93}$, at the dark-matter freeze-out $3.0\times10^{-32}$ (DERIVED from the stored sources). Status: DERIVED.

The stabiliser density depends on the metric only through the block scale $f$, the fourth root of the proper volume of the block
directions. A change of the metric changes $f$ by

@@
\Delta\ln f = -\frac18\sum_{M\in\{x_0,\,x_5,\,x_6,\,x_7\}}g_{MM}\,\Delta g^{MM},\qquad
\Delta\big(\sqrt{\lvert g\rvert}\,\rho_{\mathrm{stab}}\big) = \sqrt{\lvert g\rvert}\,\Big(-\frac12\,\rho_{\mathrm{stab}}\,g_{MN}\Delta g^{MN}
 + f\,\frac{\mathrm{d}\rho_{\mathrm{stab}}}{\mathrm{d}f}\,\Delta\ln f\Big),
@@

and for $\rho_{\mathrm{stab}} \propto f^{-8}$ (IN-4), $f\,\mathrm{d}\rho_{\mathrm{stab}}/\mathrm{d}f = -8\rho_{\mathrm{stab}}$: the second term turns the coefficient of the
block components from $-\frac12$ into $+\frac12$, so that $\mathcal{T}_{MN} = -g_{MN}\rho_{\mathrm{stab}}$ for the observable directions
$x_1, \dots, x_4$ and $\mathcal{T}_{MN} = +g_{MN}\rho_{\mathrm{stab}}$ for the block directions:

@FE-4

**The terms.** The stabiliser is a vacuum energy of the block: in ordinary space it acts like a cosmological constant (energy density
$\rho_{\mathrm{stab}}$, pressure $p_3 = -\rho_{\mathrm{stab}}$), along the block directions it pushes outwards with the pressures
$p_0 = p_5 = \rho_{\mathrm{stab}}$. It is block-isotropic ($p_0 = p_5$). It is conserved (FE-41 with $\mathcal{H}_f$: $\dot\rho = -4\mathcal{H}_f(\rho + \bar p)
= -8\mathcal{H}_f\rho$ gives $\rho \propto f^{-8}$, consistent with IN-4). Its value at the static block is fixed in FE-43. Status: DERIVED (from
the ASSUMED IN-4).

@FE-5

**The terms.** The first bracket is the symmetrised kinetic stress of the spinor (each of $\gamma_M D_N$ and $\gamma_N D_M$, acting on $\Psi$ and
on $\bar\Psi$, with the spin connection inside $D$); $g_{MN}\mathcal{L}_\Psi$ comes from the variation of $\sqrt{\lvert g\rvert}$. $\mathcal{L}_\Psi$ contains the
mass $m_\Psi$ and the contact self-interaction $\lambda$. It couples dirac16complex to gravity. For the Kohn-Sham states of dirac16complex
it takes the form FE-67 (verified by the energy identity and the $y$-conservation law FE-68). Status: DERIVED.

@FE-6

**The terms.** The same form for every Standard-Model fermion multiplet $\psi$ of every generation $i$, with the bulk mass $\mu_{\psi i}$ in place
of $m_\Psi$, no self-interaction, and the gauge fields in $D$. It enters the block through the block averages of the plasma and of cold
matter (ideal and degenerate gases of particles with their $x_0$ masses) in the block response FE-45 and in the hidden pressure FE-81.
Status: DERIVED.

@FE-7

**The terms.** The standard energy-momentum tensor of the gauge fields (geometric normalisation, so each group carries its inverse
squared coupling): the stress $F_{MP}F_N{}^P$ minus the trace part. It is traceless in four dimensions, so radiation drops out of the
block response (FE-47: $c_3 = -3c_\rho$); what remains is the trace anomaly of the interacting plasma (FE-75, FE-82). Status: STANDARD.

@FE-8

**The terms.** The tip terms act only on the tip $y = -L$: $\delta_{\mathrm{tip}} = \delta_{\mathrm{D}}(y + L)/f$ is the Dirac delta function in
proper length. The first part is the stress of the sigma field, the second the tip Lagrangian (sigma field and Yukawa terms) times
the metric; the indices $\mu, \nu$ run over the tip directions, and the components along $y$ vanish. Its gravitational effect is
part of the rest energies of $W^\pm$, $Z$ and the fermions, which are counted in the plasma. Status: DERIVED.

@FE-9

**The terms.** The portal currents are frame currents, $\mathrm{i}\bar\Psi\gamma^a\Psi$ and $\mathrm{i}\bar\psi\gamma^a\psi$, which do not depend on the
vielbein; only $\sqrt{\lvert g\rvert}$ and the explicit metric in the contraction vary, so the energy-momentum tensor is the metric times the
interaction density. They couple dirac16complex and the fermions to gravity; their effect on the block is negligible in every
environment (the level shifts FE-72 are below $10^{-9}$ GeV). Status: DERIVED.

@FE-10

**The terms.** I12 multiplies the gauge kinetic invariants by $\bar\Psi\Psi$, so its energy-momentum tensor is that of the gauge fields
(FE-7) with $1/\hat g_i^2$ replaced by $4c\,\bar\Psi\Psi/\Lambda_\star^3$: I12 acts as a field-dependent gauge coupling (FE-21). Its effect in
the coupled solution is at most $1.7\times10^{-16}$. Status: DERIVED.

@FE-11

**The terms.** Every Lovelock tensor is divergence-free identically (the Bianchi identities of the Lovelock tensors, STANDARD), so the
field equations FE-1 imply that the total source is conserved; the conservation holds when the matter fields obey their own field
equations. Status: DERIVED (the Bianchi identities verified for the order-0 metric for $p = 1, 2, 3$, sympy, exact). At order 0
the conservation is FE-41.
