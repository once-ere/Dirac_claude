# Step 4: the electroweak sector

UM-2 has the gauge group $SU(3)_c\times SU(2)_L\times U(1)_Y$ in eight dimensions, broken at the tip by the sigma field
$\Sigma$, which has no radial mode: there is no Higgs particle. Step 4 derives the charges and the couplings of the
electroweak bosons $W^+$, $W^-$, $Z$ and the photon, the anomaly cancellation of three generations, the reasons why
dirac16complex has no $Z$ coupling, and the $Z$ widths of three generations.

## The field equations of step 4

@@T:The gauge fields of SU(3)@@

@@T:The field strengths@@

@@T:The physical electroweak fields@@

@@T:The covariant derivative of a Standard-Model fermion@@

@@T:The tip sigma field and the tip Yukawa@@

@@T:The covariant derivative of the sigma field@@

@@T:The tip mass term@@

The halves of dirac16complex and the four-dimensional chirality come from the Clifford algebra of the author:

@@T:The Clifford algebra@@

The energy-momentum tensor of the tip, whose gravitational effect is part of the rest energies of $W^\pm$, $Z$ and the fermions:

@@t_tip@@

The Yang-Mills equations with the fermion currents and the tip currents, and the sigma-field equation (the Noether identity
of the gauge symmetry, not independent):

@@currents@@

@@ym_gluon@@

@@ym_su2@@

@@ym_b@@

@@ym_lin@@

@@sigma_eq@@

At momentum transfers far below $m_{\mathrm{W}}$ the exchange of $W^\pm$ and $Z$ between zero modes is a current-current
interaction with the Fermi constant and the neutral-current couplings:

@@gf@@

## The approximation of step 4

The charges, the couplings and the anomalies are exact. The $Z$ widths are computed at tree level with massless final-state
fermions, the measured $G_{\mathrm{F}}$ and $m_{\mathrm{Z}}$ and the $\overline{\mathrm{MS}}$ angle (STANDARD), with the factor
$1 + \alpha_3/\pi$ on the quarks for the comparison with the data. The neglected terms, relative to the total width, are the
electroweak loop corrections ($4.1\times10^{-3}$: the remaining difference to the measured total), the b-quark mass in the
b-quark channel ($-1.3\times10^{-3}$) and the order-$\alpha_3^2$ QCD term ($+1.3\times10^{-3}$) (DERIVED from the outputs).

## The solution of step 4

### Charges and couplings

In every generation $Q_{\mathrm{em}} = T_3 + Y$ gives the up-type quarks u, c, t the charge $2/3$, the down-type quarks d, s,
b the charge $-1/3$, the neutrinos 0 and the charged leptons e, $\mu$, $\tau$ the charge $-1$, for both chiralities (DERIVED).
The commutator $[T_3, T_\pm] = \pm T_\pm$ with $Y(W) = 0$ shows that **$W^+$, made of $W^1 - \mathrm{i}W^2$, carries the
electric charge $+e$, and $W^-$, made of $W^1 + \mathrm{i}W^2$, carries $-e$**; $W^-$ is the antiparticle of $W^+$. The photon
couples with the charge $e$ times $Q_{\mathrm{em}}$ and the $Z$ with its neutral current:

$$
e = \frac{g_2\,g_1}{\sqrt{g_2^2 + g_1^2}}\ \ \text{(photon: } e\,Q_{\mathrm{em}}\text{)},\qquad
g_{\mathrm{Z}}\big(T_3P_L - Q_{\mathrm{em}}\sin^2\theta_{\mathrm{W}}\big)\ \ \text{($Z$)},\qquad g_{\mathrm{Z}} = \sqrt{g_2^2 + g_1^2}
$$

<!-- symbols: AUTO -->

(DERIVED).

### Anomaly cancellation in three generations

With every zero mode written as a left-handed Weyl field (with $-Y$ for a right-handed one), $N_{\mathrm{col}}$ colour and
$N_{\mathrm{dbl}}$ weak components, one generation gives (DERIVED, exact fractions)

$$
\begin{aligned}
&\mathcal{A}_{\mathrm{SU(3)^2U(1)}} = \sum_{\text{triplets}}N_{\mathrm{dbl}}\,Y = 0,\qquad
\mathcal{A}_{\mathrm{SU(2)^2U(1)}} = \sum_{\text{doublets}}N_{\mathrm{col}}\,Y = \tfrac12 - \tfrac12 = 0,\\
&\mathcal{A}_{\mathrm{U(1)^3}} = \sum N_{\mathrm{col}}N_{\mathrm{dbl}}\,Y^3 = \tfrac1{36} - \tfrac89 + \tfrac19 - \tfrac14 + 1 = 0
\end{aligned}
$$

<!-- symbols: AUTO -->

and the mixed gravitational anomaly $\sum N_{\mathrm{col}}N_{\mathrm{dbl}}\,Y = 1 - 2 + 1 - 1 + 1 = 0$ and the $SU(3)^3$
anomaly $2 - 1 - 1 = 0$ vanish too; three generations have twelve $SU(2)$ doublets (no Witten anomaly). Three lepton
generations with a single quark generation would leave $\mathcal{A}_{\mathrm{SU(2)^2U(1)}} = -1$ and $\mathcal{A}_{\mathrm{U(1)^3}} = 3/2$.

### The two halves of dirac16complex

$\mathcal{B}$ commutes with the four-dimensional Lorentz generators and with $C$, so $\Psi = \Psi_A + \Psi_B$ ($\mathcal{B} =
-1$, $+1$) splits into Lorentz-invariant halves and $\bar\Psi\Psi = \bar\Psi_A\Psi_A + \bar\Psi_B\Psi_B$. The identity
$\Gamma_4 = -\mathcal{B}\gamma^{x_0}$ (DERIVED, $16\times16$) gives the four-dimensional chiral projector $P_L = (1 + \Gamma_4)/2
= (1 - \mathcal{B}\gamma^{x_0})/2$, which equals $(1 + \gamma^{x_0})/2$ on $\Psi_A$ and $(1 - \gamma^{x_0})/2$ on $\Psi_B$; the
latter annihilates every orbital at the tip. The chiral charge densities at the tip, which a chiral tip current would couple
to, are (DERIVED): the $\Psi_A$ fold band $0.163$ per unit length in each of its four blocks, the $\Psi_B$ fold band 0; the
odd (heavy) states $0.257$ ($\Psi_A$) and 0 ($\Psi_B$); every transition current $\bar\Psi_A\gamma^\mu P_L\Psi_B$ vanishes at
the tip.

### The $Z$ invisible width and the tip $Z$ portal of version 1

Version 1 coupled the $\Psi_A$ fold band (two Weyl species) to the $Z$ through a chiral tip portal of the current
$\mathrm{i}\bar\Psi\gamma^\mu P_L\Psi$ to the tip current $\frac{\mathrm{i}}{2}v_\Sigma^2\,\mathrm{tr}(\Sigma^\dagger D_\mu\Sigma\,\tau^3)$,
with an even and an oriented (odd under the fold reflection) coefficient. With three neutrinos and a fold-band coupling
$r_{\mathrm{Z}}$ times that of a neutrino, the number of invisible species (the invisible width of the $Z$ in units of its
width into one neutrino flavour) would be

$$
N_\nu = 3 + 2r_{\mathrm{Z}}^2 ;
$$

<!-- symbols: AUTO -->

the measured $N_\nu = 2.9963 \pm 0.0074$ (PDG 2025) is reproduced by $r_{\mathrm{Z}} = 0$ (0.5 standard deviations) and bounds
$r_{\mathrm{Z}}^2 < 0.0056$ (two standard deviations). Even at that bound the neutral-current rate of the fold band, $r_{\mathrm{Z}}^2$
times the neutrino's ($\propto r_{\mathrm{Z}}^2G_{\mathrm{F}}^2T^5$ against the Hubble rate $\mathcal{H} \propto T^2/M_{\mathrm{Pl}}$),
would keep it in equilibrium down to $T \approx 2.6\ \text{MeV}\times r_{\mathrm{Z}}^{-2/3} = 14.7$ MeV, where $g_s = 10.75$, so it
would carry the neutrino temperature and add the extra radiation of an early-decoupled species,

@@deltaneff@@

with $N_{\mathrm{W}} = 2$ Weyl species ($F_{\mathrm{h}}$ corrects for the non-instantaneous neutrino decoupling of step 5: a species
decoupled earlier is not heated by $e^+e^-$ annihilation): $\Delta N_{\mathrm{eff}} = 2.02$, far above the measured
$N_{\mathrm{eff}} = 2.99 \pm 0.17$ (Planck 2018) and $2.86 \pm 0.13$ (ACT DR6) (STANDARD). The oriented part would let the heavy
odd $\Psi_A$ states decay into the fold band and a $Z$, and through the inverse decays and the exchange process keep the fold
band in equilibrium until the odd states disappear, at $T \sim M_{\mathrm{DM}}/30$ (above the electroweak scale, $g_s =
105.75$: the Standard Model without a Higgs particle), or, for an oriented coupling of the size of a neutrino's, until the $Z$
bosons annihilate near 15 GeV ($g_s = 86.25$: t, $W$, $Z$ gone) (ESTIMATE): then $\Delta N_{\mathrm{eff}} = 0.0958$ to $0.1257$
and $N_{\mathrm{eff}} = 3.139$ to $3.169$, 2.1 to 2.4 standard deviations above ACT DR6 (the three-flavour value $3.0432$:
1.4; disfavoured). UM-2 therefore drops the portal (ASSUMED; the bounds DERIVED): $N_\nu = 3$, neither fold band is ever
thermalised, and both halves keep an exact fold parity. (The plasma counts used are $g_s = 10.75$: photons, $e^\pm$, three
neutrinos; $61.75$ just above the QCD crossover: with gluons, u, d, s, $\mu$; $86.25$ below the top, $W$ and $Z$ masses;
$105.75$ above the electroweak scale. Right-handed neutrinos are never thermalised.)

### The $Z$ widths of three generations

At tree level, with massless final-state fermions, the partial width of the $Z$ into the pair of a fermion $f$ is

$$
\Gamma_{\mathrm{Z}}^{f} = \frac{N_{\mathrm{col}}\,G_{\mathrm{F}}\,m_{\mathrm{Z}}^3}{6\sqrt2\,\pi}
\Big[\big(T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\overline{\mathrm{MS}}}\big)^2 + \big(T_3^f\big)^2\Big]
$$

<!-- symbols: AUTO -->

with $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ ($G_{\mathrm{F}}$, $m_{\mathrm{Z}}$ and the angle STANDARD; DERIVED), in MeV:

| channel | each $\nu$ | invisible ($3\nu$) | each of e, $\mu$, $\tau$ | each of u, c | each of d, s, b | hadronic | total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tree level | $165.9$ | $497.7$ | $83.4$ | $285.4$ | $367.9$ | $1674.4$ | $2422.3$ |
| with $1 + \alpha_3/\pi$ on the quarks | | | | | | $1737.3$ | $2485.2$ |
| measured (PDG 2025) | | $499.1$ | | | | | $2495.5$ |

The top quark is too heavy for the $Z$ to decay into it; $\alpha_3(m_{\mathrm{Z}}) = 0.1180$ (STANDARD). The ratio of the
hadronic to one charged-lepton width is $20.83$ against the measured $20.77$ (STANDARD, PDG 2025). The remaining difference
($0.4$ % in the total) is the size of the electroweak loop corrections, which UM-2 does not compute; with the tree-level angle
of the couplings of the mass fit, $\sin^2\theta_{\mathrm{W}} = 0.22363$, the total changes by $+0.82$ % (a per-cent scheme
ambiguity). The one-generation conflict of version 1 (a total of $1232$ MeV) is gone.

## The check of step 4

**In its own equations.** The charges, the couplings of the photon and the $Z$, the anomaly sums and the projector algebra are
exact (DERIVED, fractions and $16\times16$ matrices). The stored widths (each channel, the invisible, hadronic and total widths
and the ratio $20.83$) agree with the formula recomputed from the stored inputs to $2.7\times10^{-12}$ (DERIVED).

**In concert with the other field equations.**

* *The $W$ and $Z$ masses of the $x_0$ problem.* The $Z$ mass of the widths is the $Z$ mass of the $x_0$ eigenvalues of step 2
  to $2.0\times10^{-12}$; the angle of the couplings of the $x_0$ problem and the $\overline{\mathrm{MS}}$ angle of the widths
  differ by $0.0076$, which moves the total width by $0.82$ % at tree level ($0.83$ % with the QCD factor), within the per-cent
  size of the uncomputed loop corrections (DERIVED).
* *The heating factor of the neutrino decoupling.* The factor $F_{\mathrm{h}} = 1.009500589$ of the neutrino decoupling of step 5
  is the one used here and in step 9, to $5.8\times10^{-7}$ (the rounded $1.0095$) (DERIVED).
* *Three neutrinos everywhere.* $N_\nu = 3$ of the $Z$ width is the content of the neutrino decoupling and of $N_{\mathrm{eff}}$
  (step 5) and of the CMB computation (step 6), in which the fold bands enter only through the freeze-in radiation of step 9.

## The status of step 4

DERIVED: the charges and couplings, the anomaly cancellation, the projector identities and tip densities, the bounds on the
removed tip $Z$ portal, the tree-level $Z$ widths. ASSUMED: the removal of the tip $Z$ portal. INVENTED: the tip sigma field.
STANDARD: $G_{\mathrm{F}}$, $m_{\mathrm{Z}}$, $\alpha_3(m_{\mathrm{Z}})$, the $\overline{\mathrm{MS}}$ angle and the measured
widths. OPEN: the electroweak loop corrections and the $S$ parameter of the Higgsless tip. Conflicts with data, inherent in the
author's order: no Higgs boson, and the longitudinal $W^+W^-$ scattering violates perturbative unitarity near 1.2 TeV (see the
last section).
