# The interactions: every interaction in equation form, explained and analysed

The author's order: "You must invent/create and document new phenomenological interactions for these standard model particles
that should be consistent with qcd and electro-weak models", and "Put each and every interaction in equation form, and explain and
analyze it". This section does so for every interaction of UM-2. Each subsection gives (1) the interaction as an equation (the
interaction term of the action with its tag IN-n, or the form that follows from it), (2) what it couples and why it is consistent
with QCD and the electroweak model, and (3) its strength and its bounds. The catalogue at the end lists them all.

## Gravity with itself and with every field

**The equations.** The self-interaction of gravity is the Einstein-Lovelock action with the author's weights, written out again:

@@IN-2@@

with the Lovelock densities (written out again)

@@IN-3@@

and gravity couples to every field through $\sqrt{\lvert g\rvert}$, the inverse metric of every kinetic term and, for every spinor
(dirac16complex and the Standard-Model fermions), through the canonical spin connection:

@@IN-7@@

On the order-0 metric the gravitational coupling of every spinor is the non-zero term

@@FE-13@@

**Why it is consistent.** The Lovelock densities are the only scalar densities built from the curvature whose field equations are of
second order in the derivatives of the metric in eight dimensions (no ghost from higher derivatives), and every Lovelock tensor is
divergence-free, so the source is conserved; the minimal coupling through $\sqrt{\lvert g\rvert}$, $g^{MN}$ and $\Omega_M$ is the unique
coupling that respects general covariance and local frame rotations. Gravity does not distinguish the gauge charges, so it is
consistent with every gauge symmetry of the Standard Model.

**Strength and bounds.** On the stabilised block four-dimensional gravity is exactly general relativity with Newton's constant
$8\pi G_{\mathrm{N}} = \kappa/(\mathcal{G}(K_*)V_\perp)$ (the section on dimensional reduction); the Kaluza-Klein gravitons add Yukawa forces
of relative strength $\mathcal{A}_n < 0.2$ and range below $1.63\times10^{-21}$ m (FE-54 in the section on the metric), invisible at every
measurable distance. The sourceless block of the author's weights has repulsive four-dimensional gravity ($\mathcal{G} = -1$); the
stabiliser of the next subsection is what makes it attractive. Every source pushes on the block through its hidden pressure; the
largest push in the history of the model moves the block by $\Delta\ln f = 1.1\times10^{-34}$ (the coupled solution).

## The block stabiliser

**The equation.** A vacuum energy of the block, written out again:

@@IN-4@@

**Why it is consistent.** It is a function of the metric only (of the block volume), four-dimensionally Lorentz invariant and
isotropic in the block, so it respects every symmetry of the observable four dimensions and is blind to the gauge charges.
**Strength.** $\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2 = 54.566H^2$, fixed by the static block; it gives the radion its mass
$\omega_{\mathrm{r}} = 3.387H = 48.42$ TeV. Its microscopic origin is OPEN.

## The self-interaction of dirac16complex

**The equation.** The contact term $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of the action of dirac16complex, written out again:

@@IN-5@@

**What it couples, and why it is consistent.** $\Psi$ with itself; $\Psi$ is a singlet of $SU(3)_c\times SU(2)_L\times U(1)_Y$, so the term
is gauge invariant; $\bar\Psi\Psi = \bar\Psi_A\Psi_A + \bar\Psi_B\Psi_B$ commutes with $\mathcal{B}$, so it does not mix the halves. In the
Kohn-Sham description it produces the mean fields $\frac{15}{16}\lambda n^{\mathrm{sc}}$ and $-\frac{1}{16}\lambda n$ (FE-64 in the section on
dirac16complex in the cell).

**Strength and bounds.** Through the transition scalar density of the dark-matter orbital and a fold zero mode it lets the dark
matter annihilate into the massless fold bands; keeping their radiation below $\Delta N_{\mathrm{eff}} = 0.001$ requires
$G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ (ASSUMED bound, derived with FE-135 and FE-136 in the section on the dark sector), i.e.
$\lambda \le 1.4\times10^{-10}H^{-6}$ for $v_{\mathrm{t}} = H^{-3}$. The value $\lambda_{\mathrm{test}} = 7\times10^{-5}H^{-6}$ with which the
Kohn-Sham machinery was tested would thermalise the fold bands ($\Delta N_{\mathrm{eff}} = 0.19$) and is therefore only a test value.

## The strong interaction (QCD)

**The equations.** The gauge fields enter through their action and their field strengths, and the fermions through their action
and their covariant derivative (all written out again):

@@IN-8@@

@@IN-9@@

@@IN-11@@

@@IN-12@@

Inserting the covariant derivative IN-12 into the fermion action IN-11 gives the couplings of the fermions to the gauge fields through
the currents (written out again)

@@FE-20@@

so the quarks couple to the gluons through the term

$$
-\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;G^A_M\,J_3^{AM},
$$
<!-- symbols: AUTO -->

and the commutator in the gluon field strength of IN-9, inserted into the gluon term of IN-8, gives the three- and four-gluon vertices.

**Why it is consistent with QCD.** This is QCD in eight dimensions: the gauge group $SU(3)_c$ is never broken (the tip carries no
colour, so the gluon profiles have no tip term), the gluons are exactly massless $x_0$ zero modes with flat profiles, and the
four-dimensional theory of the zero modes is QCD with six quark flavours, asymptotically free ($b_3 = 11 - \frac23N_{\mathrm{f}} > 0$),
confining below its scale, with protons and neutrons as the baryons of the cosmology. No interaction of UM-2 carries colour
except the gauge couplings; the portals couple to colour-singlet currents (I11, I13) or to the colour-singlet invariant
$G^A_{MN}G^{AMN}$ (I12), so they leave the colour structure of QCD intact.

**Strength.** $g_3^2 = \hat g_3^2/V_\perp$ with the measured $\alpha_3(m_{\mathrm{Z}}) = 0.1180$ (STANDARD); at the Kaluza-Klein scale
$\alpha_3(m_{\mathrm{KK}}) = 0.0606$ (one loop, six flavours). Because the four-dimensional couplings scale as $f^{-4}$, the QCD scale is the most
block-sensitive quantity of UM-2 ($\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}/\mathrm{d}\ln f = -49.0$, the nucleon mass $-46.1$; the coupled
solution).

## Electromagnetism and the weak interactions of the three generations

**The equations.** The physical electroweak fields are the combinations (written out again)

@@IN-10@@

The gauge couplings of the fermions (from IN-11 and IN-12 of the previous subsection), in terms of the currents FE-20 and of these
physical fields, are (DERIVED)

$$
\begin{aligned}
&-\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(W^I_M\,J_2^{IM} + B_M\,J_1^M\Big)\\
&= -\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\hat g_2\big(W^{+}_MJ_2^{-M} + W^{-}_MJ_2^{+M}\big)
 + \hat g_Z\,Z_M\big(J_2^{3M} - \sin^2\theta_{\mathrm{W}}\,J_{\mathrm{em}}^M\big) + \hat e\,A_M\,J_{\mathrm{em}}^M\Big],
\end{aligned}
$$
<!-- symbols: AUTO + J2pm -->

with $J_2^{\pm} = (J_2^1 \mp \mathrm{i}J_2^2)/\sqrt2$ and $J_{\mathrm{em}} = J_2^3 + J_1$ (FE-20). These currents are the sources of the
linearised field equations of $W^+$, $W^-$, $Z$ and the photon (written out again), which also define $\hat e$:

@@FE-25@@

On the zero modes (four-dimensional fields; the couplings divided by $V_\perp^{1/2}$) these are the charged current of the
three generations, with the PMNS matrix in the neutrino fields $\nu_\alpha = \sum_iU_{\alpha i}\nu_i$ and the CKM matrix between the up-type
components $(Q_i)_1$ and the down-type components $(Q_j)_2$ of the quark doublets in the mass basis,

$$
-\frac{g_2}{\sqrt2}\Big[W^{+}_\mu\Big(\sum_{\alpha}\bar\nu_\alpha\gamma^\mu P_L\,\ell^-_\alpha
 + \sum_{i,j=1}^{3}\big(V_{\mathrm{CKM}}\big)_{ij}\,\big(\bar Q_i\big)_1\gamma^\mu P_L\big(Q_j\big)_2\Big) + \text{h.c.}\Big],
$$
<!-- symbols: AUTO -->

and the neutral currents of the $Z$ and of the photon, summed over the fermions $f$ (STANDARD form; the couplings of FE-102),

$$
-\frac{g_2}{\cos\theta_{\mathrm{W}}}\,Z_\mu\sum_f\bar\psi_f\gamma^\mu\big(\tilde g^f_LP_L + \tilde g^f_RP_R\big)\psi_f
 - e\,A_\mu\sum_fQ_{\mathrm{em}}^f\,\bar\psi_f\gamma^\mu\psi_f,\qquad e = \frac{g_2g_1}{\big(g_2^2 + g_1^2\big)^{1/2}} .
$$
<!-- symbols: AUTO -->

A fermion of weak isospin $T_3$ and hypercharge $Y$ couples to the photon with $eQ_{\mathrm{em}} = e(T_3 + Y)$ and to the $Z$ with
$(g_2/\cos\theta_{\mathrm{W}})(T_3P_L - Q_{\mathrm{em}}\sin^2\theta_{\mathrm{W}})$ (DERIVED).

**Why it is consistent with the electroweak model.** These are exactly the couplings of the electroweak model of three generations:
the doublets $Q_i$, $\ell_i$ and the singlets carry the Standard-Model quantum numbers (the table of the fermion section), every term
is invariant under $SU(2)_L\times U(1)_Y$, the electric charge is $Q_{\mathrm{em}} = T_3 + Y$, and the gauge anomalies cancel generation by
generation (the fermion section). Because the three doublets of a sector share one bulk mass, the $W$ and $Z$ zero modes couple to
every generation with the same strength (lepton universality), and the neutral currents are flavour diagonal in every basis: the
first even Kaluza-Klein gauge mode couples to a zero mode of localisation $c$ through $\int\lvert\chi_c\rvert^2F_1\,\mathrm{d}\xi$, which relative
to the zero mode is $0.14434$ for every left-handed lepton and $-0.30066$ for every left-handed quark, and the right-handed rotations are
trivial, so in the mass basis the largest flavour-changing neutral coupling is $10^{-17}$ (round-off; DERIVED). With different doublet
bulk masses the PMNS rotation would create flavour-changing couplings up to $0.033$; the shared bulk mass is what makes UM-2 free of
tree-level flavour-changing neutral currents, as the Standard Model is. The PMNS and CKM matrices carry the whole flavour structure of
the charged currents.

**Strength and bounds.** $g_2$ and $g_1$ are fixed by the measured couplings ($\overline{\mathrm{MS}}$ value
$\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ for the couplings to the fermions, $\alpha_{\mathrm{em}} = 1/127.95$ at $m_{\mathrm{Z}}$); at low
energy the exchange of $W^\pm$ and $Z$ becomes the four-fermion interactions with the measured Fermi constant (next subsection). The
invisible width of the $Z$ counts three neutrinos exactly, against the measured $2.9963 \pm 0.0074$ (0.5 standard deviations), and the
tree-level total width with the QCD factor, $2485.2$ MeV, lies $0.41$ % below the measured $2495.5$ MeV, the size of the electroweak loop
corrections that UM-2 does not compute (the section on the neutrinos). Charged-lepton flavour violation through the neutrino masses
(the decay of a muon into an electron and a photon, of rate proportional to $\lvert\sum_iU^*_{\mu i}U_{ei}m_i^2/m_{\mathrm{W}}^2\rvert^2$) has the
branching ratio $2.8\times10^{-55}$: unobservable.

## The weak interactions at low energy and the forward scattering of neutrinos

**The equations.** At momentum transfers far below $m_{\mathrm{W}}$ and $m_{\mathrm{Z}}$ the exchange of $W^\pm$ and $Z$ between the zero-mode
fermions reduces to current-current interactions (STANDARD):

@@FE-101@@

@@FE-102@@

A neutrino crossing a medium scatters forward coherently on it; averaged over an unpolarised medium at rest the interactions add the
flavour-diagonal potentials

@@FE-103@@

**Why it is consistent.** This is the Fermi theory of the electroweak model with the PMNS matrix in the flavour fields; UM-2 uses the
measured $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$. **Use.** These potentials drive the MSW conversion in the Sun, the Earth and
supernovae, and the neutrino-neutrino term drives the collective flavour evolution of dense neutrino gases (the section on the
neutrinos).

## Electroweak symmetry breaking at the tip without a Higgs particle (INVENTED)

**The equations.** The tip sigma field and the tip Yukawa couplings, written out again:

@@IN-13@@

@@IN-14@@

and in the unitary gauge the mass term of the weak bosons:

@@IN-15@@

On the static block the tip term becomes the Robin condition of the $W^\pm$ and $Z$ profiles; the measured masses then fix its
strength (the section on the $x_0$ mass mechanism):

@@FE-55@@

**What it couples, and why it is consistent with the electroweak model.** $\Sigma$ couples to $W^I$ and $B$ through its covariant
derivative and to the fermions through the Yukawa terms. It is the gauged non-linear sigma model of $SU(2)_L\times U(1)_Y \to U(1)_{\mathrm{em}}$
(the electroweak chiral Lagrangian at lowest order), placed on the tip: every term is invariant under $\Sigma \to U_L\Sigma U_Y^\dagger$ with the
matching transformations of the gauge fields and fermions (DERIVED, deviation $1.1\times10^{-14}$ with random group elements and random
complex tip matrices); the three would-be Goldstone modes of $\Sigma$ become the longitudinal $W^+$, $W^-$ and $Z$; the unbroken combination
is the photon, which receives no tip term and stays exactly massless; the custodial symmetry of the kinetic term gives
$m_{\mathrm{Z}}/m_{\mathrm{W}} = 1/\cos\theta_{\mathrm{W}}$ at leading order. The difference from the electroweak model is that $\Sigma$ has no radial
mode: there is no Higgs particle, as the author orders.

**Strength and bounds.** $\beta_{\mathrm{W}} = 0.011912$ reproduces both measured masses ($m_{\mathrm{W}} = 80.3625$ GeV, $m_{\mathrm{Z}} = 91.1879$ GeV)
and the measured tree-level custodial violation $\rho_{\mathrm{EW},0} - 1 = 0.00038$, which comes from the bending of the profiles at the tip,
and gives the Kaluza-Klein scale $m_{\mathrm{KK}} = 121.32$ TeV. A positive tip term cannot make the $W$ heavier than the Dirichlet limit,
$m_{\mathrm{W}} \le 0.01824\,m_{\mathrm{KK}}$. Without a Higgs particle the scattering of longitudinal $W^+W^-$ pairs violates perturbative unitarity
near $\sqrt{8\pi}\times246$ GeV $\approx 1.2$ TeV, far below the Kaluza-Klein modes that could restore it: a CONFLICT WITH DATA inherent in the
order, as is the absence of the observed Higgs boson of 125 GeV. The oblique parameter $S$ of the Higgsless tip is not computed (OPEN).

## Fermion masses and mixing from the tip (INVENTED)

**The equations.** The Yukawa part $\mathcal{L}_{\mathrm{Y}}$ of IN-13 (written out above) places, in each fermion field equation (FE-14 to
FE-19), a tip term that is equivalent to the self-adjoint tip mixing conditions, written out again:

@@FE-30@@

**What it couples, and why it is consistent.** Each lepton doublet with the singlets $\nu_{Rj}$ and $e_{Rj}$, each quark doublet with $u_{Rj}$
and $d_{Rj}$, through $\Sigma$, at the tip only. The terms are gauge invariant for arbitrary complex tip matrices; with one doublet bulk
mass per sector and unitary tip matrices the masses are the one-generation roots of the exact $x_0$ mass condition and the mixing matrices
are $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$ and $V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d$ (DERIVED; the section on the $x_0$ mass mechanism):
unitary, as in the Standard Model, with no tree-level flavour-changing neutral currents.

**Strength.** Tip matrices of order one ($\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, $\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$) and bulk masses
from $5.2H$ to $54.2H$ in magnitude give the whole fermion hierarchy, fourteen orders of magnitude from the lightest neutrino to the top
quark, because the tip values of exponentially localised zero modes depend exponentially on their localisations.

## Portal I11: the vector contact portal to the $B - L$ currents (INVENTED)

**The equation.**

@@IN-16@@

It enters the field equation of $\Psi$ (the term with $J^{B-L}_M$ in FE-12), the Dirac equation of every fermion (FE-14 to FE-19) and the
energy-momentum tensor

@@FE-9@@

On the zero modes it becomes the four-dimensional contact interaction (with I13)

@@FE-70@@

**What it couples, and why it is consistent.** The vector current of the whole field $\Psi$ (both halves, fold bands included) with the
$B - L$ currents of the fifteen multiplets of three generations and the three right-handed neutrinos. Each current is a gauge singlet,
so the term is invariant under $SU(3)_c\times SU(2)_L\times U(1)_Y$; it is generation blind (no flavour-changing coupling); and $B - L$ is free
of gauge and gravitational anomalies when the right-handed neutrinos are present ($\sum(B - L)^3 = 3\cdot2\cdot\frac{1}{27} - 3\cdot\frac{1}{27}
- 3\cdot\frac{1}{27} - 2 + 1 + 1 = 0$ and $\sum(B - L) = 0$ per generation, left-handed Weyl components), so the current is conserved and
could even be gauged. It is a vector coupling, so it conserves parity in four dimensions and the chirality of every fermion.

**Strength and bounds.** Its strength must be small, or it would keep the massless fold bands in equilibrium (too much dark radiation).
The benchmark (ASSUMED) is fixed by their freeze-in: the plasma produces fold-band pairs at the rate (FE-129 in the section on the dark
sector) that adds $\Delta N_{\mathrm{eff}} = 5.21\times10^{29}\,G_{\mathrm{V}}^2$ GeV$^4$ from $T_{\mathrm{max}} = 10$ TeV, so
$G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ ($3.8\times10^{-12}\,G_{\mathrm{F}}$) gives $\Delta N_{\mathrm{eff}} = 0.001$ without ever reaching
equilibrium (the production rate per fold quantum is 0.012 of the Hubble rate at $T_{\mathrm{max}}$). Its other effects are negligible:
its mean field moves the dark-matter level by at most $7.3\times10^{-17}$ GeV ($1.6\times10^{-21}$ of its mass, at the freeze-out;
$4.3\times10^{-19}$ GeV in a neutron-star core), contributes $3.9\times10^{-60}$ cm$^2$ to the direct-detection
cross-section, lets the dark matter annihilate into right-handed neutrinos at only $2.0\times10^{-17}$ of its I13 rate into quarks, and the
fold band stays massless under every I11 mean field (its first-order change of the gap is at most $3.0\times10^{-9}$ per unit amplitude,
rounding; zero in exact arithmetic).

## Portal I12: the gauge-kinetic scalar portal (INVENTED)

**The equation.**

@@IN-17@@

It enters the field equation of $\Psi$ (the term $\mathcal{F}/\Lambda_\star^3$ in FE-12), the energy-momentum tensor

@@FE-10@@

and acts on the gauge fields as a field-dependent coupling (written out again):

@@FE-21@@

On the dark matter it becomes the four-dimensional operator

@@FE-71@@

with $\mathcal{O}_{\mathrm{DM}} = \partial\varepsilon_{\mathrm{DM}}/\partial m_\Psi = 0.7072$ (DERIVED, Hellmann-Feynman, checked to $10^{-8}$).

**What it couples, and why it is consistent.** The scalar density $\bar\Psi\Psi$ with the three gauge invariants $G^A_{MN}G^{AMN}$,
$W^I_{MN}W^{IMN}$, $B_{MN}B^{MN}$; with $W^I_{MN}W^{IMN}$ expanded in the physical fields (the gauge section) it couples $\bar\Psi\Psi$ to the pairs
$W^+W^-$, $ZZ$, $Z\gamma$, $\gamma\gamma$ and to gluon pairs. Each invariant is gauge invariant and Lorentz invariant, so I12 breaks no symmetry
of QCD or of the electroweak model; it changes only the strength of the gauge couplings where $\Psi$ has a scalar density, and in the
QCD vacuum the gluon condensate makes it a uniform mass shift of $\Psi$. The scalar density of every chiral zero mode vanishes
identically (its lower component is zero), so **I12 does not touch the massless fold bands**; it couples the massive states, in particular
the dark matter, which it lets annihilate into gauge-boson pairs in the p-wave.

**Strength and bounds.** Its benchmark strength (ASSUMED) is set by unitarity, $G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3) = (38.2\ \text{TeV})^{-3}$,
which keeps its annihilation cross-section below the partial-wave bound of total angular momentum 0 ($^3P_0$) up to $E_{\mathrm{cm}} = 2.40\,M_{\mathrm{DM}}$:

@@FE-127@@

@@FE-128@@

With universal coefficients $c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$ and the gauge couplings at the annihilation scale
$2M_{\mathrm{DM}}$ (one loop: $g_3^2 = 0.779$, $g_2^2 = 0.378$, $g_1^2 = 0.138$) this is $c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$ GeV$^{-3}$,
i.e. $\Lambda_\star/c_{\mathrm{I12}}^{1/3} = 44.9$ TeV, and $G_{\mathrm{g}}$, $G_{\mathrm{W}}$, $G_{\mathrm{B}} = 6.09$, $2.96$, $1.08\times10^{-15}$
GeV$^{-3}$. I12 alone cannot produce the relic abundance within perturbative unitarity (it would leave $\Omega_{\mathrm{DM}}h_{100}^2 = 8.0$
per species at the benchmark; the dark sector). Its other effects: the dark-matter density shifts the gauge couplings by at most
$1.7\times10^{-16}$ (at the freeze-out), its direct-detection cross-section through the trace anomaly is at most $6\times10^{-53}$ cm$^2$, and the
benchmark changes the strong coupling by 10 % through the thermal dark-matter density only at $T = 27$ TeV ($M_{\mathrm{DM}}/T = 1.6$): the
effective description holds through the freeze-out and everything later.

## Portal I13: the $x_0$-chiral vector portal to the baryon-number current (INVENTED)

**The equation.**

@@IN-18@@

($\gamma^{x_0}$ the frame matrix; the sum runs over the seven directions $M = x_1, \dots, x_7$). It enters the field equation of $\Psi$ (the
$J^B_M$ term of FE-12), the Dirac equations of the quarks (FE-14 to FE-16) and the energy-momentum tensor FE-9 (above); on the zero modes
it is the $G_{\mathrm{A}}$ term of the contact interaction FE-70 (above), and its annihilation cross-section is $\sigma_{\mathrm{I13}}$ of FE-127
(above), bounded by FE-128.

**What it couples, and why it is consistent** (DERIVED with the author's matrices, exact):

* for $M \ne x_0$ the bilinear $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ is Hermitian: $\gamma^{x_0}$ anticommutes with every $\gamma^M$, $M \ne x_0$, so
  $P_a\gamma^M = \gamma^MP_b$, and $C$ anticommutes with $\gamma^{x_0}$, so $CP_bC^{-1} = P_a$; for $M = x_0$ it is not ($\gamma^{x_0}$ commutes with
  $P_b$), so that component is left out (it would make the action complex; $J^B_{x_0}$ vanishes on the quark zero modes anyway);
* its components along $x_1, \dots, x_4$ form a four-dimensional vector ($\gamma^{x_0}$ commutes with the four-dimensional Lorentz
  generators), and $C\gamma^MP_b$ commutes with $\mathcal{B}$ for $M = x_1, \dots, x_4$, so I13 does not mix the halves $\Psi_A$, $\Psi_B$ in four
  dimensions; for the extra times it anticommutes with $\mathcal{B}$, which is harmless because $J^B_{x_5}$, $J^B_{x_6}$, $J^B_{x_7}$ vanish on the
  zero modes (which lie in the half $\mathcal{B} = -1$);
* in the block form of the Kohn-Sham reduction $\gamma^{x_0} = \sigma_3$, so $P_b$ projects on the lower component of an orbital; the fold
  bands have no lower component, so **I13 vanishes identically on the fold bands** and cannot produce dark radiation; it couples the
  massive states, in particular the dark matter (the lowest odd level, whose lower component is non-zero);
* $J^B$ is the baryon-number current, a singlet of $SU(3)_c\times SU(2)_L\times U(1)_Y$ term by term and conserved in perturbation theory, so
  I13 is gauge invariant and respects the symmetries of QCD and of the electroweak model; it is a vector coupling to quarks only.

**Why the baryon-number current** (DERIVED; the elastic rate is an ESTIMATE). With the $B - L$ current instead, the annihilation into
right-handed neutrino pairs would bring the three right-handed neutrinos into equilibrium above the freeze-out (they reach 0.9997 of the
equilibrium number by $M_{\mathrm{DM}}/T = 40$) and they would decouple as three Weyl species adding $\Delta N_{\mathrm{eff}} = 0.144$
($N_{\mathrm{eff}} = 3.19$, 2.5 standard deviations above the ACT DR6 value $2.86 \pm 0.13$). With $J^B$ the right-handed neutrinos keep only
their tip coupling and their I11 coupling and are never thermalised (the dark sector).

**Strength and bounds.** The strength is fixed by the dark-matter relic: each species freezes out with $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ for
$G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ ($1.1\times10^{-4}\,G_{\mathrm{F}}$), the s-wave cross-section capped at its unitarity bound of total angular momentum 1,
which it reaches only above the relative velocity $0.51$ (22 % of the freeze-out rate comes from collisions at the bound; without the
cap $G_{\mathrm{A}} = 1.269\times10^{-9}$ GeV$^{-2}$). It predicts the direct-detection cross-section $4.0\times10^{-46}$ cm$^2$ per nucleon on
xenon, 0.16 of the LZ limit extrapolated to 44.35 TeV (testable), and an s-wave annihilation into quark pairs today with
$\sigma v_{\mathrm{rel}} = 9.8\times10^{-26}$ cm$^3$/s (the thermal value of a heavy relic). The contact form is an effective description: for the
quark doublet $(G_{\mathrm{A}}q^B_Q\tilde I^{(b)}_Q)^{-1/2} = 30$ TeV lies below the energies $E_{\mathrm{cm}} \approx 89$ TeV of the annihilations,
so a mediator at or below about 90 TeV must complete it (OPEN). The physics accuracy of $G_{\mathrm{A}}$ is about 1 %: the ideal-gas thermal
history leaves out the order-$\alpha$ interaction pressure of the plasma ($-5.4$ % at the freeze-out), which would raise
$\Omega_{\mathrm{DM}}h_{100}^2$ by about 2.7 % and $G_{\mathrm{A}}$ by about 1.4 % (ESTIMATE; residual analysis).

## The radion couplings

**The equation.** A change of the block scale, $f \to f(1 + \sigma_{\mathrm{r}})$, changes every mass of a species $s$ by

$$
\Delta m_s = \frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}\,m_s\,\sigma_{\mathrm{r}},
$$
<!-- symbols: AUTO -->

so the radion couples to every massive field with the strength of its block sensitivity ($-1$ for the Kaluza-Klein masses, $-0.501$ for
$m_{\mathrm{W}}$, $-0.772$ for $M_{\mathrm{DM}}$, $-6.8$ to $-41$ for the fermions, $-46.1$ for the nucleon; the section on dimensional reduction).
**Why it is consistent.** It is a gravitational (metric) mode: its couplings follow from general covariance and are blind to the gauge
charges. **Strength and bounds.** Its mass is $\omega_{\mathrm{r}} = 48.42$ TeV (range $4.08\times10^{-21}$ m), its static response to matter is at
most $\Delta\ln f = 1.1\times10^{-34}$, and the oscillation left over from the deflation decays with the Planck-suppressed rate of the last
section (lifetime $0.43\,\text{s}/C_{\mathrm{r}}$; the moduli problem, OPEN).

## Removed in version 2: the chiral tip $Z$ portal

Version 1 contained a fourth portal on the tip,

$$
S_{\mathrm{I9}} = \int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\big(c_{\mathrm{Z}} + \tilde c_{\mathrm{Z}}\varsigma_{\mathrm{t}}\big)
 \big(\mathrm{i}\bar\Psi\gamma^\mu P_L\Psi\big)\,\frac{\mathrm{i}v_\Sigma^2}{2}\,\mathrm{tr}\big(\Sigma^\dagger D_\mu\Sigma\,\tau^3\big),
$$
<!-- symbols: AUTO -->

whose even part $c_{\mathrm{Z}}$ made the $\Psi_A$ fold band (two Weyl species) couple to the $Z$ like two neutrinos and so stand in for the
missing $\nu_\mu$, $\nu_\tau$ of one generation. Its algebra is DERIVED and remains true: $P_L$ is a Hermitian projector commuting with the
four-dimensional Lorentz generators and with $C\gamma^\mu$; $\Gamma_4 = -\mathcal{B}\gamma^{x_0}$, so $P_L = (1 - \mathcal{B}\gamma^{x_0})/2$, which is
$(1 + \gamma^{x_0})/2$ on $\Psi_A$ and $(1 - \gamma^{x_0})/2$ on $\Psi_B$ and annihilates $\Psi_B$ at the tip (every orbital satisfies
$(1 - \gamma^{x_0})\Psi = 0$ there): **no $P_L$ tip current and no tip operator built on $\bar\Psi\Psi$ reaches $\Psi_B$**. With three neutrinos the
portal has no role left, and both of its parts are bounded or disfavoured by the data (DERIVED): its even part gives the $Z$ an invisible
width $N_\nu = 3 + 2r_{\mathrm{Z}}^2$, bounded by the measured $N_\nu = 2.9963 \pm 0.0074$ to $r_{\mathrm{Z}}^2 < 0.0056$; even at that bound the fold
band would stay in equilibrium down to $14.7$ MeV and add, as a species of $N_{\mathrm{W}}$ Weyl fermions that decouples early,

@@FE-133@@

($N_{\mathrm{W}} = 2$, $g_s = 10.75$), i.e. $\Delta N_{\mathrm{eff}} = 2.02$, far above the measured $N_{\mathrm{eff}} = 2.99 \pm 0.17$ (Planck 2018) and
$2.86 \pm 0.13$ (ACT DR6) (STANDARD); its oriented part $\tilde c_{\mathrm{Z}}$ (odd under the fold reflection) would let the heavy odd $\Psi_A$
states decay into the $\Psi_A$ fold band and a $Z$, and by the inverse decays and the exchange process keep the fold band in equilibrium
until the odd states or the $Z$ bosons disappear (at $g_s = 105.75$ or $86.25$), adding $\Delta N_{\mathrm{eff}} = 0.096$ to $0.126$ (ESTIMATE), i.e.
$N_{\mathrm{eff}} = 3.14$ to $3.17$, $2.1$ to $2.4$ standard deviations above the ACT DR6 value (disfavoured). UM-2 therefore sets
$c_{\mathrm{Z}} = \tilde c_{\mathrm{Z}} = 0$ (ASSUMED). Consequences: $N_\nu = 3$ exactly; neither fold band is ever thermalised (no tip operator,
zero scalar density for I12, the weak benchmark of I11, the bound on the self-interaction); both halves keep an exact fold parity, so
the lightest odd states of $\Psi_A$ and of $\Psi_B$ are both stable.

**Not included, and why.** A dipole portal $\bar\Psi\mathcal{S}^{MN}\Psi B_{MN}$ would couple the fold bands to the photon and thermalise them
(too much dark radiation). No gauge-invariant operator couples the neutral $\Psi$ to a single $W^+$ or $W^-$; $W^\pm$ enter only in pairs (I12)
or with a charged fermion pair (the covariant derivatives of the fermions in I11).

## Consistency of the new interactions with QCD and the electroweak model: summary

* **Gauge invariance.** Every term of the action is invariant under $SU(3)_c\times SU(2)_L\times U(1)_Y$: $\Psi$ is a gauge singlet and the portals
  couple it to gauge-invariant composites (the $B - L$ and baryon-number currents, the field-strength invariants); the tip terms are
  invariant under $\Sigma \to U_L\Sigma U_Y^\dagger$ for arbitrary complex tip matrices (DERIVED, $1.1\times10^{-14}$).
* **Anomalies.** The gauge anomalies of the fermions cancel generation by generation (exact fractions, the fermion section); the
  currents of I11 ($B - L$, with the right-handed neutrinos) and I13 ($B$, perturbatively) are conserved.
* **Electroweak symmetry breaking without a Higgs particle.** The breaking is carried by the tip sigma field, a non-linear realisation
  without a radial mode: the $W^\pm$ and $Z$ masses and the custodial ratio are those of the electroweak model at tree level, the photon
  stays massless, and the price is the loss of perturbative unitarity of $W^+W^-$ scattering near 1.2 TeV and the absence of the observed
  Higgs boson (CONFLICTS WITH DATA, inherent in the order).
* **QCD.** Colour is never broken; the gluons are exactly massless; the portals couple only to colour singlets.
* **Flavour.** The shared doublet bulk mass makes the neutral currents flavour diagonal (no tree-level flavour-changing neutral currents);
  the PMNS and CKM matrices are unitary tip matrices.
* **Validity.** The portals are contact operators of an effective description valid below their scale; I13 needs a mediator at or below
  about 90 TeV (OPEN).

## The catalogue of interactions

| # | interaction | fields | equation | role in UM-2 |
| - | ---- | ---- | ------- | ---- |
| 1 | Einstein-Lovelock self-interaction | $g_{MN}$ | IN-2, IN-3, FE-1 | background, block dynamics, four-dimensional Newton constant $\propto 1/\mathcal{G}(K_*)$ |
| 2 | gravity of every field | $g_{MN}$ with all | IN-7 ($\sqrt{\lvert g\rvert}$, $g^{MN}$, $\Omega_M$ in each action), FE-13 | universal coupling; $\Psi$ through the canonical spin connection |
| 3 | block stabiliser | $g_{MN}$ | IN-4 | static, stable block with attractive four-dimensional gravity |
| 4 | $\Psi$ self-interaction | $\Psi$ | IN-5 ($-\frac{\lambda}{2}(\bar\Psi\Psi)^2$) | Kohn-Sham mean fields; bounded by the fold-band radiation |
| 5 | strong interaction | gluons, the six quarks | IN-8, IN-9, IN-11, IN-12, FE-20; $-G^A_MJ_3^{AM}$ | confinement, protons and neutrons |
| 6 | electromagnetic interaction | photon, charged fermions, $W^\pm$ | IN-10, IN-11, IN-12, FE-25; $-eQ_{\mathrm{em}}A_\mu\bar\psi\gamma^\mu\psi$; $W^+W^-\gamma$ | CMB photons, recombination, Thomson drag |
| 7 | weak charged current | $W^\pm$, three lepton and quark generations | $-\frac{g_2}{\sqrt2}W^+_\mu(\dots) + \text{h.c.}$ with $U$, $V_{\mathrm{CKM}}$ | beta decay, neutron-proton conversion, neutrinos produced and detected in flavour states |
| 8 | weak neutral current | $Z$, all fermions | $-\frac{g_2}{\cos\theta_{\mathrm{W}}}Z_\mu\bar\psi\gamma^\mu(\tilde g_LP_L + \tilde g_RP_R)\psi$ | neutrino decoupling, $Z$ widths |
| 9 | gauge self-interactions | $W^\pm$, $Z$, $\gamma$, gluons | IN-9 (commutators) | electroweak and QCD consistency |
| 10 | $W^\pm$, $Z$ masses | $\Sigma$, $W^I$, $B$ | IN-13, IN-14, IN-15, FE-55 | $x_0$ profiles bent at the tip |
| 11 | fermion masses and mixing | $\Sigma$, $\ell_i$, $\nu_{Rj}$, $e_{Rj}$, $Q_i$, $u_{Rj}$, $d_{Rj}$ | IN-13 ($\mathcal{L}_{\mathrm{Y}}$), FE-30 | tip mixing of the chiral zero modes: masses, PMNS, CKM |
| 12 | low-energy weak interactions, forward scattering | $\nu$ with electrons, nucleons, $\nu$ | FE-101, FE-102, FE-103 | MSW conversion, early-Universe potentials, fast flavour instability |
| 13 | $\Psi$ with the fermion currents | $\Psi$, all fermions | IN-16 (I11), FE-70 | freeze-in of the fold bands ($\Delta N_{\mathrm{eff}} = 0.001$); Kohn-Sham mean fields |
| 14 | $\Psi$ with gauge pairs | $\Psi$, $W^+W^-$, $ZZ$, $Z\gamma$, $\gamma\gamma$, gluon pairs | IN-17 (I12), FE-21, FE-71 | p-wave annihilation (subdominant); condensate mass shifts; field-dependent couplings |
| 15 | radion couplings | $\sigma_{\mathrm{r}}$ with all massive fields | $\Delta m_s = (\mathrm{d}\ln m_s/\mathrm{d}\ln f)\,m_s\,\sigma_{\mathrm{r}}$ | the masses track the block size |
| 16 | $\Psi$ ($x_0$-chiral) with the baryon current | massive states of $\Psi$, the six quarks | IN-18 (I13), FE-70 | s-wave annihilation: the dark-matter relic; direct detection |

