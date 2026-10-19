# Step 7: the dark-matter relic and its detection

The lightest odd states of $\Psi_A$ and of $\Psi_B$ (step 2) are two degenerate Dirac fermions of the mass
$M_{\mathrm{DM}} = 3.102204\,m_\Psi = 44.35$ TeV ($m_\Psi = H$), cold (step 3) and neutral; UM-2 has no tip operator, so neither
couples to the $Z$, and both are stable by the fold parity (step 4). Step 7 computes their relic abundance through the portal I12
with the freeze-out formula, shows that I12 alone violates partial-wave unitarity, and estimates the detection; step 9 replaces
the freeze-out formula by the Boltzmann equation and resolves the unitarity problem with I13.

## The field equations of step 7

@@T:Portal I12@@

On the dark matter, I12 is a four-dimensional coupling of the scalar density to the gauge-field invariants, with the coefficient
$\mathcal{O}_{\mathrm{DM}}$ of step 3:

@@i12dm@@

The number density of each species obeys the Boltzmann equation with the thermal average of the annihilation cross-section,
bounded by partial-wave unitarity:

@@boltz@@

@@thermal_avg@@

@@xsec@@

@@unitarity@@

@@relic@@

## The approximation of step 7

* *The freeze-out formula* replaces the Boltzmann equation (the standard radiation-dominated freeze-out); against the numerical
  solution of step 9 it is accurate to $2.4$ % (an s-wave test case gives $0.1306$ against $0.1275$).
* *The non-relativistic expansion* of the thermal average, $\langle\sigma v_{\mathrm{rel}}\rangle = 6G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4/
  (\pi x)$; the exact relativistic average exceeds it by $0.111$ at $x = 30$ (by about $3/x$).
* *The effective operator* is used up to the energies of the annihilations ($\sqrt{4M_{\mathrm{DM}}^2}$ and above); where its
  cross-section exceeds the unitarity bound the operator is not a valid description (below).
* *The direct-detection estimate* uses the trace anomaly with a nucleon gluon fraction and a low-scale coupling quoted without a checked reference
  (ESTIMATE).

## The solution of step 7

Through I12 the dark matter annihilates in the p-wave into gauge-boson pairs. In the hypercharge channel, with the coupling
$G_{\mathrm{B}}$, the spin-averaged rate is $G_{\mathrm{B}}^2E_{\mathrm{cm}}^2(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2)/(4\pi)$ (the
polarisation sum $E_{\mathrm{cm}}^4/2$ and the spin trace $2(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2)$ checked numerically); each of the
eight gluon and three $SU(2)$ channels adds the same with its own coupling, so in total

$$
\sigma_{\mathrm{I12}}\,v_{\mathrm{rel}} = \frac{G_{\mathrm{I12}}^2E_{\mathrm{cm}}^2\big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)}{4\pi}
\ \to\ \frac{G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4\,v_{\mathrm{rel}}^2}{\pi}\qquad (v_{\mathrm{rel}} \ll 1)
$$

<!-- symbols: AUTO -->

(DERIVED). Since $\bar\Psi\Psi = \bar\Psi_A\Psi_A + \bar\Psi_B\Psi_B$ does not mix the halves, each species freezes out separately
and contributes half of $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$. The freeze-out of a Dirac fermion with $g_\rho = g_s = 105.75$ at
$T = M_{\mathrm{DM}}/x_{\mathrm{f}} \approx 1.5$ TeV (the Standard Model of three generations without a Higgs particle; the
right-handed neutrinos and the fold bands are never thermalised) gives

$$
x_{\mathrm{f}} = \ln\Big[0.095\,\frac{M_{\mathrm{Pl}}\,M_{\mathrm{DM}}\,\langle\sigma v_{\mathrm{rel}}\rangle}{\sqrt{g_\rho\,x_{\mathrm{f}}}}\Big] = 30.38,
\qquad
\Omega_{\mathrm{DM}}h_{100}^2 = \frac{2\times1.07\times10^9\ \text{GeV}^{-1}\,x_{\mathrm{f}}^2}{\sqrt{g_\rho}\,M_{\mathrm{Pl}}\,
3G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4/\pi} = 0.060\ \text{per species}
$$

<!-- symbols: AUTO -->

($M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2} = 1.22091\times10^{19}$ GeV; the number $0.095$ is the standard coefficient $0.038$ of the
freeze-out condition times the factor $5/4$ of its matching constant $1/2$ and times the two spin states of a Dirac fermion), which requires $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) =
2.01\times10^{-25}$ cm$^3$/s per species, i.e.

$$
G_{\mathrm{I12}} = \big(8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2\big)^{1/2} = (15.5\ \text{TeV})^{-3},\qquad
G_{\mathrm{g}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{G}}\,g_3^2}{\Lambda_\star^3},\quad \mathcal{O}_{\mathrm{DM}} = 0.7072
$$

<!-- symbols: AUTO -->

(a single species carrying all the dark matter would need $(17.6\ \text{TeV})^{-3}$ with the same $g_\rho$). These are the numbers
of the freeze-out formula (version 2); the numerical Boltzmann solution of step 9 needs $(15.86\ \text{TeV})^{-3}$ at
$x_{\mathrm{f}} = 31.70$.

**Unitarity** (DERIVED). The operator annihilates a fermion pair only from the state with total angular momentum zero and
positive parity ($^3P_0$); for unpolarised Dirac fermions the inelastic cross-section from it is bounded by
$\sigma \le \pi/(4k_{\mathrm{cm}}^2)$ ($k_{\mathrm{cm}} = M_{\mathrm{DM}}v_{\mathrm{rel}}/2$ for $v_{\mathrm{rel}} \ll 1$), i.e.
$\sigma v_{\mathrm{rel}} \le \pi/(M_{\mathrm{DM}}^2v_{\mathrm{rel}})$, whose thermal average over the relative velocities
($\propto v_{\mathrm{rel}}^2\,\mathrm{e}^{-xv_{\mathrm{rel}}^2/4}$) is

$$
\Big\langle\frac{\pi}{M_{\mathrm{DM}}^2\,v_{\mathrm{rel}}}\Big\rangle = \frac{\sqrt{\pi x}}{M_{\mathrm{DM}}^2}
 = 5.79\times10^{-26}\ \text{cm}^3/\text{s}\qquad (x = x_{\mathrm{f}} = 30.38)
$$

<!-- symbols: AUTO -->

(checked by numerical averaging). The freeze-out requirement exceeds it 3.47 times; the effective cross-section at the relic
strength exceeds the bound above the relative velocity

$$
v_{\mathrm{c}} = \Big(\frac{\pi}{G_{\mathrm{I12}}\,M_{\mathrm{DM}}^3}\Big)^{2/3} = 0.263,
$$

<!-- symbols: AUTO -->

i.e. for 79 % of the pairs at freeze-out (with the strength and $x_{\mathrm{f}}$ of the freeze-out formula; with the relic strength
of step 9 the formula gives $0.274$ and 75 % of the pairs, and the exact crossing lies at $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} =
0.269$). (Version 1 compared the requirement with $(4\pi/M_{\mathrm{DM}}^2)\sqrt{x_{\mathrm{f}}/\pi} = 2.32\times10^{-25}$ cm$^3$/s,
the bound of a single helicity channel without the spin average and the restriction to $^3P_0$, a factor 4 too large.) The
gauge-kinetic portal therefore cannot produce the relic abundance within perturbative unitarity. Step 9 recomputes this with the
Boltzmann equation (a cross-section at the $^3P_0$ limit at every energy would leave $\Omega_{\mathrm{DM}}h_{100}^2 = 0.058$ per
species: only a strongly coupled $^3P_0$ channel at the unitarity limit could give the relic) and resolves it with the s-wave
portal I13.

**Direct detection** (ESTIMATE). Even if the whole coupling were in gluons, the trace anomaly of QCD gives the coupling of the
dark matter to a nucleon of the mass $m_{\mathrm{N}}$, through the gluon fraction $f_{\mathrm{TG}}$ of the nucleon mass (the
nucleon matrix element of the gluon invariant is $-\frac{8\pi}{9\alpha_3}m_{\mathrm{N}}f_{\mathrm{TG}}$), and the spin-independent
cross-section per nucleon,

$$
f_{\mathrm{N}} = G_{\mathrm{g}}\,\frac{8\pi}{9\alpha_3}\,m_{\mathrm{N}}\,f_{\mathrm{TG}},\qquad
\sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi}
$$

<!-- symbols: AUTO -->

($f_{\mathrm{TG}} = 0.92$, $\alpha_3 = 0.3$ at a low scale, $m_{\mathrm{N}} = 0.939$ GeV, $\mu_{\mathrm{red}}$ the dark-matter-nucleon
reduced mass; approximate values quoted without a checked reference), i.e. $\sigma_{\mathrm{SI}} = 6.3\times10^{-53}$ cm$^2$ for each half (the two halves have the same
cross-section and together the full local density, so the limit applies as for one species), eight orders below the LZ limit
extrapolated linearly in the mass from $2.2\times10^{-48}$ cm$^2$ at 40 GeV to $44$ TeV ($2.4\times10^{-45}$ cm$^2$); the
electroweak channels have no tree-level nucleon coupling. Any relic value would also depend on the radion oscillation left over
from the deflation (which redshifts like dust): if it dominated the Universe until it decayed, it would dilute the dark matter
after freeze-out (the moduli problem, last section).

## The check of step 7

**In its own equations.** The polarisation sum and the spin trace of the cross-section were checked numerically, and the thermal
average of the unitarity bound by numerical averaging (DERIVED). The freeze-out formula is checked against the numerical solution
of the Boltzmann equation of step 9: on the s-wave test case they give $0.1306$ and $0.1275$ ($2.4$ %), and for I12 at the relic
strength the numerical solution needs $(15.86\ \text{TeV})^{-3}$ at $x_{\mathrm{f}} = 31.70$ against $(15.5\ \text{TeV})^{-3}$ at
$30.38$ (DERIVED).

**In concert with the other field equations.**

* *The I12 coefficient of the Kohn-Sham equations.* $\mathcal{O}_{\mathrm{DM}} = \partial\varepsilon_{\mathrm{DM}}/\partial m_\Psi$
  of step 3 ($0.707196002672$) is the rounded $0.7072$ of this computation to $5.7\times10^{-6}$ (DERIVED).
* *The dark-matter mass of the $x_0$ spectrum* (step 2) is the mass of the Boltzmann equation to $8.1\times10^{-13}$ (DERIVED).
* *The degrees of freedom of the thermal history* (step 9): $g_\rho = g_s = 105.75$ at the freeze-out is the value of the ideal
  gases with the $x_0$ masses (105.73 at 1.42 TeV) (DERIVED).
* *The I12 strength in the mean fields* of step 8 is the benchmark of step 9 to $1.6\times10^{-12}$ (DERIVED).

## The status of step 7

DERIVED: the I12 cross-section, the freeze-out numbers and the violation of partial-wave unitarity by I12 at the relic strength.
ESTIMATE: the direct detection through the trace anomaly (inputs quoted without a checked reference). INVENTED: the portal I12. OPEN: the microscopic
origin of the portals (I12 alone could give the relic only as a strongly coupled $^3P_0$ channel).
