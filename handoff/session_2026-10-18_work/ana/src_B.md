
# B. dirac16complex as dark matter and as dark energy {-}

## B.1 The candidate (DERIVED, conditional) {-}

dirac16complex is the 16-component complex spinor field of the record, with the action (RECORD)

@@IN-5@@

in the Clifford algebra of the author, with the Dirac adjoint and the two halves of the field (AUTHOR)

@@IN-6@@

Its field equation, with the canonical spin connection and the three portals to the Standard Model, is (DERIVED)

@@FE-12@@

and on the order-0 metric the spin connection enters through (DERIVED, exact for every $a_4$, $b_4$ and on both halves)

@@FE-13@@

which contains $\gamma^{x_0}$ and $\gamma^{x_4}$ only. $\mathcal{B}$ commutes with $C$, with $\gamma^a$ and with $C\gamma^a$ for the
directions $x_0, \dots, x_4$, and anticommutes with them for $x_5, x_6, x_7$ (DERIVED with the author's matrices): in the good
sector (no extra-time momenta) every term of UM-2 commutes with $\mathcal{B}$, so the numbers of quanta of $\Psi_A$ and of $\Psi_B$
are separately conserved. The four-dimensional chirality projector is (DERIVED)

$$ P_L = \frac{1 + \Gamma_4}{2} = \frac{1 - \mathcal{B}\gamma^{x_0}}{2} $$
<!-- symbols: AUTO -->

since $\Gamma_4 = -\mathcal{B}\gamma^{x_0}$. Every orbital obeys the tip condition $(1 - \gamma^{x_0})\Psi = 0$, so $P_L$ annihilates every
$\Psi_B$ orbital at the tip, while a $\Psi_A$ orbital has a non-zero chiral tip charge density ($0.257$ for the lightest odd state).
UM-2 contains no tip operator (the chiral tip $Z$ portal of version 1 is removed), so neither half is reached at the tip. The
dark-matter candidate is the lightest odd state of each half, from the exact spectrum, written out again:

@@FE-62@@

* two Dirac fermions (the lowest odd level of $\Psi_A$ and of $\Psi_B$, the same orbital in all eight blocks, degenerate) of the
  mass

$$ M_{\mathrm{DM}} = \varepsilon_{\mathrm{DM}} = \sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2} = 3.102204\,m_\Psi = 44.35\ \text{TeV},\qquad \varpi = 1.89901,\qquad m_\Psi = H; $$
<!-- symbols: AUTO -->

* cold: $w_{\mathrm{KS}} = 0$ for quanta at rest (Kohn-Sham, DERIVED with the equations of section B.8; $2.8\times10^{-5}$ with the test
  coupling $\lambda_{\mathrm{test}}$);
* electrically neutral (gauge singlets), with no $Z$ coupling;
* stable: the numbers of quanta of the two halves are conserved, and the fold parity of each half is exact (the bulk is
  symmetric under the fold reflection, and UM-2 has no oriented tip operator that could connect an odd state to the even fold
  band);
* its mass is an $x_0$ mass: its hidden wave number carries $\varpi^2/\tilde\varepsilon^2 = 0.896$ of $\tilde\varepsilon^2$
  ($\tilde\varepsilon = \varepsilon_{\mathrm{DM}}fL$), $m/m_{\mathrm{Heis}} = 2.29$, and its hidden pressure is
  $p_0/\rho = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f = 0.772$ (two independent computations agree to $6\times10^{-12}$).

## B.2 The portals that produce it (INVENTED) {-}

$\Psi$ is a singlet of SU(3)$\times$SU(2)$\times$U(1)$_Y$, so it couples to the Standard Model only through gauge-invariant composite
operators. UM-2 contains three of them. I11, the vector contact portal to the $B - L$ currents:

@@IN-16@@

I12, the gauge-kinetic scalar portal:

@@IN-17@@

I13, the $x_0$-chiral vector portal to the baryon-number current:

@@IN-18@@

together with the contact self-interaction $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of (IN-5). Their properties (DERIVED): I11 couples both
halves of $\Psi$, the fold bands included, to the $B - L$ currents of the three generations (each term separately gauge invariant
and generation blind); I12 couples the scalar density, which vanishes identically for every chiral zero mode, so it does not
touch the fold bands; in I13 the bilinear $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ is Hermitian for the seven directions $M \ne x_0$
($\gamma^{x_0}$ anticommutes with every $\gamma^M$, $M \ne x_0$, and with $C$, so $P_a\gamma^M = \gamma^MP_b$ and $CP_bC^{-1} = P_a$), but not
for $M = x_0$ ($(\mathrm{i}C\gamma^{x_0}P_b)^\dagger = \mathrm{i}C\gamma^{x_0}P_a$), which is therefore left out; its four-dimensional
components form a Lorentz vector that does not mix the halves; in the block form $\gamma^{x_0} = \sigma_3$, so $P_b$ projects on the
lower component $b$ of an orbital, and I13 vanishes identically on the fold bands $(a_{\mathrm{fold}}, 0)$ (numerically to
$1.2\times10^{-13}$). $J^B$ is the baryon-number current, a singlet of the gauge group, conserved in perturbation theory. On the zero
modes the portals become four-dimensional contact interactions (DERIVED):

@@FE-70@@

@@FE-71@@

with the overlaps of the dark-matter orbital and of the fold band with the zero modes of the Standard-Model fermions (DERIVED;
each equals the derivative of a self-consistent Kohn-Sham level with respect to the amplitude of the corresponding mean field,
to $3.8\times10^{-12}$ for $\tilde I$ and $3.5\times10^{-12}$ for $\tilde I^{(b)}$; $\mathcal{O}_{\mathrm{DM}} = 0.7072$):

| zero mode $f$ | $\tilde I_{of}$, dark matter | $\tilde I^{(b)}_{of}$, dark matter | $\tilde I_{of}$, fold band |
| ---------- | ---- | ---- | ---- |
| quark doublets $Q$ | $8.272$ | $2.613$ | $6.685$ |
| lepton doublets $\ell$ | $1.252$ | $0.913$ | $1.659$ |
| up, charm, top singlets | $0.385$, $0.606$, $8.272$ | $0.379$, $0.557$, $2.613$ | $0.792$, $1.060$, $6.685$ |
| down, strange, bottom singlets | $0.396$, $0.462$, $0.762$ | $0.389$, $0.446$, $0.661$ | $0.807$, $0.893$, $1.221$ |
| electron, muon, tau singlets | $0.397$, $0.588$, $1.252$ | $0.390$, $0.544$, $0.913$ | $0.808$, $1.041$, $1.659$ |
| right-handed neutrinos | $0.302$ to $0.308$ | $0.301$ to $0.308$ | $0.668$ to $0.678$ |

(the top and tau singlets share the profiles of their doublets, $c_R = -c_Q$ and $-c_\ell$; $\tilde I^{(b)}_{of} = 0$ for the fold band.)
The broad quark-doublet zero mode overlaps the dark-matter orbital most.

## B.3 The relic density from the Boltzmann equation {-}

Since $\bar\Psi\Psi = \bar\Psi_A\Psi_A + \bar\Psi_B\Psi_B$ and every portal is diagonal in the halves, each of the two dark-matter species
freezes out separately and must supply half of $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$.

### The thermal history (STANDARD equations, DERIVED values) {-}

Every species in equilibrium contributes the ideal-gas densities

@@FE-121@@

which give the degrees of freedom and the Hubble rate of the hot Universe

@@FE-122@@

with the QCD crossover, the neutrino temperature after decoupling and the cooling of the plasma (the crossover model ASSUMED)

@@FE-123@@

for the particle content of UM-2 with its $x_0$ masses: the photon, the gluons, $W^+$, $W^-$, $Z$ (no Higgs particle), the six
quarks, the three charged leptons and the three neutrinos. The right-handed neutrinos and the fold bands are never thermalised,
the radion and the Kaluza-Klein modes not below 10 TeV, and the dark matter is not counted (it carries $1.1\times10^{-2}$ of the
energy density at $x = 5$, where the integration starts and its abundance is the equilibrium one, and $7\times10^{-12}$ at the
freeze-out). The result (DERIVED; residual $5.0\times10^{-9}$ against an independent quadrature and the exact limits):
$g_\rho = 105.75$ above the top threshold (three generations without a Higgs particle), $86.2$ at 10 GeV, $76.3$ at 1 GeV,
$10.75$ at a few MeV, and today $g_s = 43/11$, $g_\rho = 3.3626$, $s_0 = 2891.3$ cm$^{-3}$ ($T_\gamma = 2.7255$ K). The thermal history
uses three massless neutrino species after 2 MeV, while the CMB computation uses $N_{\mathrm{eff}} = 3.0442$: $g_\rho$ today differs by
0.59 % (residual analysis), irrelevant for the relic.

### The Boltzmann equation, the thermal average and the cross-sections (STANDARD, DERIVED) {-}

For one Dirac species

@@FE-124@@

with the relativistic thermal average (Gondolo and Gelmini)

@@FE-125@@

and the relic density

@@FE-126@@

The annihilation cross-sections through I12 and I13 and their partial-wave unitarity bounds are

@@FE-127@@

@@FE-128@@

where the effective cross-section exceeds its bound, it is replaced by the bound (a unitarity-respecting completion that saturates
it). The machinery is checked against the freeze-out formula (STANDARD, Kolb and Turner, for a Dirac fermion with
$\langle\sigma v_{\mathrm{rel}}\rangle = a_{\mathrm{sw}} + 6b_{\mathrm{pw}}/x$)

$$ x_{\mathrm{f}} = \ln\Big[0.095\,\frac{M_{\mathrm{Pl}}M_{\mathrm{DM}}\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}})}{\sqrt{g_\rho x_{\mathrm{f}}}}\Big],\qquad \Omega_{\mathrm{DM}}h_{100}^2 = \frac{2\times1.07\times10^9\,\text{GeV}^{-1}\,x_{\mathrm{f}}}{\sqrt{g_\rho}\,M_{\mathrm{Pl}}\,\big(a_{\mathrm{sw}} + 3b_{\mathrm{pw}}/x_{\mathrm{f}}\big)} $$
<!-- symbols: AUTO -->

($0.095 = 0.038\times\frac12(\frac12 + 2)\times2$: the matching constant $\frac12$ and the two internal states of a Dirac fermion;
$M_{\mathrm{Pl}} = 1.22091\times10^{19}$ GeV): an s-wave cross-section of $4.4\times10^{-26}$ cm$^3$/s gives $\Omega_{\mathrm{DM}}h_{100}^2 = 0.1275$
from the Boltzmann equation and $0.1306$ from the formula, and the late-time integral of the Boltzmann equation is reproduced to
$1.3\times10^{-8}$.

### I12 alone violates unitarity (DERIVED) {-}

The I12 cross-section of (FE-127) is p-wave:

$$ \sigma_{\mathrm{I12}}v_{\mathrm{rel}} = \frac{G_{\mathrm{I12}}^2E_{\mathrm{cm}}^2\big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)}{4\pi} \to \frac{G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4v_{\mathrm{rel}}^2}{\pi},\qquad a_{\mathrm{sw}} = 0,\qquad b_{\mathrm{pw}} = \frac{G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4}{\pi} $$
<!-- symbols: AUTO -->

(each of the $8 + 3 + 1$ abelian channels of the gluon, $W$ and $B$ fields contributes with its own coupling, which add up to
$G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2$). With the freeze-out formula ($g_\rho = 105.75$ at
$T \approx 1.5$ TeV) the relic $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ per species requires $x_{\mathrm{f}} = 30.38$,
$\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 2.01\times10^{-25}$ cm$^3$/s and $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$ (a single species
carrying all the dark matter would need $(17.6\ \text{TeV})^{-3}$). But the operator annihilates a fermion pair only from the state
with total angular momentum 0 and positive parity, $^3P_0$, whose partial-wave bound (FE-128), averaged over the four spin states
of an unpolarised Dirac pair and with $k_{\mathrm{cm}} = M_{\mathrm{DM}}v_{\mathrm{rel}}/2$ ($v_{\mathrm{rel}} \ll 1$), gives

$$ \sigma_{\mathrm{I12}}v_{\mathrm{rel}} \le \frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}},\qquad \Big\langle\frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}}\Big\rangle = \frac{\int_0^\infty\frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}}\,v_{\mathrm{rel}}^2\,\mathrm{e}^{-xv_{\mathrm{rel}}^2/4}\,\mathrm{d}v_{\mathrm{rel}}}{\int_0^\infty v_{\mathrm{rel}}^2\,\mathrm{e}^{-xv_{\mathrm{rel}}^2/4}\,\mathrm{d}v_{\mathrm{rel}}} = \frac{\sqrt{\pi x}}{M_{\mathrm{DM}}^2} $$
<!-- symbols: AUTO -->

i.e. $5.79\times10^{-26}$ cm$^3$/s at $x_{\mathrm{f}} = 30.38$ (the thermal average over the non-relativistic distribution of the relative
velocity, checked by numerical averaging). The freeze-out requirement exceeds the bound 3.47 times, and the effective cross-section
at the relic strength exceeds the bound above

$$ v_{\mathrm{c}} = \Big(\frac{\pi}{G_{\mathrm{I12}}M_{\mathrm{DM}}^3}\Big)^{2/3} = 0.263, $$
<!-- symbols: AUTO -->

i.e. for 79 % of the pairs at the freeze-out. (Version 1 compared the requirement with $(4\pi/M_{\mathrm{DM}}^2)\sqrt{x_{\mathrm{f}}/\pi}
= 2.32\times10^{-25}$ cm$^3$/s, the bound of a single helicity channel without the spin average and without the restriction to $^3P_0$,
four times too large.) The Boltzmann equation confirms and quantifies the conclusion: the effective I12 would need
$G_{\mathrm{I12}} = (15.86\ \text{TeV})^{-3}$ ($x_{\mathrm{f}} = 31.70$, $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 1.89\times10^{-25}$ cm$^3$/s), crossing
the $^3P_0$ bound at $E_{\mathrm{cm}} = 89\,510$ GeV, i.e. at $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} = 0.269$ ($0.274$ from the
non-relativistic formula), with 96 % of the freeze-out rate from collisions above the crossing; a cross-section at the bound at
every energy, the largest annihilation from $^3P_0$, leaves $\Omega_{\mathrm{DM}}h_{100}^2 = 0.058$ per species ($x_{\mathrm{f}} = 30.77$), and
the effective operator capped at the bound leaves $0.154$, $0.108$, $0.084$, $0.065$, $0.059$ for $G_{\mathrm{I12}}^2$ equal to 1, 3, 10,
100 and $10^4$ times the relic value. Within perturbative couplings I12 overproduces the dark matter; it could produce the relic only
as a strongly coupled $^3P_0$ channel at the unitarity limit, outside the validity of the effective description. UM-2 therefore
keeps I12 at the unitarity-safe benchmark (ASSUMED)

$$ G_{\mathrm{I12}} = \frac{\pi}{2M_{\mathrm{DM}}^3} = (38.2\ \text{TeV})^{-3} $$
<!-- symbols: AUTO -->

(below the bound up to $E_{\mathrm{cm}} = 2.40\,M_{\mathrm{DM}}$; alone it would leave $\Omega_{\mathrm{DM}}h_{100}^2 = 8.0$ per species; with
universal coefficients and the one-loop couplings at $2M_{\mathrm{DM}}$ it means $c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$
GeV$^{-3}$, i.e. $\Lambda_\star/c_{\mathrm{I12}}^{1/3} = 44.9$ TeV, and $G_{\mathrm{g}}$, $G_{\mathrm{W}}$, $G_{\mathrm{B}} = 6.09$, $2.96$,
$1.08\times10^{-15}$ GeV$^{-3}$).

### The relic with I13 (DERIVED) {-}

Through I13 the dark matter annihilates in the s-wave ($^3S_1$) into quark pairs, with $G_f = G_{\mathrm{A}}q^B_f\tilde I^{(b)}_{of}$ for each
quark Weyl component of (FE-127) ($\sum_fN_{\mathrm{c}}(q^B_f\tilde I^{(b)}_{of})^2 = 16.351$). The Boltzmann equation with the cross-sections of
I12 (benchmark) and I13 gives each species $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ for

$$ G_{\mathrm{A}} = 1.278\times10^{-9}\ \text{GeV}^{-2} = 1.1\times10^{-4}\,G_{\mathrm{F}},\qquad x_{\mathrm{f}} = 31.23 $$
<!-- symbols: AUTO -->

($T = M_{\mathrm{DM}}/x_{\mathrm{f}} = 1.42$ TeV), with $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 9.50\times10^{-26}$ cm$^3$/s from I13 and
$9.9\times10^{-28}$ cm$^3$/s from I12, the I13 cross-section capped at its bound $3\pi/(4k_{\mathrm{cm}}^2)$ for total angular momentum 1, which it reaches only
above $v_{\mathrm{rel}} = 0.51$: 21.7 % of the freeze-out rate comes from collisions at the bound and 78 % from collisions below it
(without the cap $G_{\mathrm{A}} = 1.269\times10^{-9}$ GeV$^{-2}$, and the uncapped cross-section would exceed the bound above
$v_{\mathrm{rel}} = 0.52$, for 25 % of the rate). The relic of UM-2 is therefore a thermal freeze-out with most annihilations
perturbative. The contact form of I13 is an effective description (for the quark doublet
$G_f^{-1/2} = (G_{\mathrm{A}}q^B_f\tilde I^{(b)}_{of})^{-1/2} = 30$ TeV, below the energies $E_{\mathrm{cm}} \approx 89$ TeV of the
annihilations), whose completion by a mediator is OPEN.

**Accuracy of the relic (residual analysis).** Re-solving the Boltzmann equation at the stored $G_{\mathrm{A}}$ gives
$\Omega_{\mathrm{DM}}h_{100}^2 = 0.0600000002$ (late-time identity $6.1\times10^{-9}$), and the relic agrees with the dark-matter density
$\Omega_{\mathrm{DM}}h_{100}^2$ of the CMB computation to $3.1\times10^{-9}$ (DERIVED). The neglected physics is larger. The ideal-gas thermal history leaves out the
order-$\alpha$ interaction pressure of the plasma, $-5.4$ % of the pressure at the freeze-out (QCD $-4.7$ %, SU(2) $-0.7$ %, U(1)$_Y$
$-0.10$ %), which would raise $\Omega_{\mathrm{DM}}h_{100}^2$ by about 2.7 % and the needed $G_{\mathrm{A}}$ by about 1.4 % (ESTIMATE): the physics
accuracy of $G_{\mathrm{A}}$ is about 1 %, not the $10^{-6}$ of the root finding. The fold bands produced by freeze-in are missing from
the Hubble rate of the Boltzmann equation ($3.5\times10^{-4}$ of the energy density at the freeze-out: $\mathcal{H}$ larger by
$1.7\times10^{-4}$, the relic by about as much), and the thermal shift of the dark-matter mass is $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}} =
1.5\times10^{-6}$. The relic also assumes that the radion oscillation left over from the deflation, which redshifts like dust,
does not dominate and dilute the Universe after the freeze-out (the moduli problem of section A.8).

### Why the baryon-number current (DERIVED; the elastic rate an ESTIMATE) {-}

If I13 coupled to the $B - L$ current instead of $J^B$, the relic would need a different strength, and the dark matter would
annihilate into right-handed neutrino pairs and bring them into equilibrium:

@@FE-131@@

while elastic scattering on the dark matter keeps them at the plasma temperature as long as

@@FE-132@@

and a species of $N_{\mathrm{W}}$ Weyl fermions that stays in equilibrium until the plasma has $g_s$ entropy degrees of freedom adds

@@FE-133@@

With the $B - L$ current $\mathcal{S}_{B-L} = 22.92$ (the three right-handed neutrinos carry 1.2 % of the annihilation) and
$G_{\mathrm{A}}^{B-L} = 1.072\times10^{-9}$ GeV$^{-2}$ (from the uncapped $G_{\mathrm{A}}$); the right-handed neutrinos would reach 0.9997 of
the equilibrium number by $x = 40$, the number-changing rate would fall below $\mathcal{H}$ at $x = 16.1$, elastic scattering would keep
them coupled until $x = 24.4$ ($T = 1.82$ TeV, $g_s = 105.7$), and they would decouple as $N_{\mathrm{W}} = 3$ Weyl species adding
$\Delta N_{\mathrm{eff}} = 0.144$, i.e. $N_{\mathrm{eff}} = 3.19$, 2.5 standard deviations above the ACT DR6 value $2.86 \pm 0.13$. With the
baryon-number current the right-handed neutrinos keep only their tip coupling and their I11 coupling (charge $-1$), through which
they are produced at the fraction

@@FE-134@@

$r_{\nu_R} = 2.0\times10^{-17}$ of the I13 annihilation rate into quarks: they are never thermalised.

## B.4 Direct and indirect detection {-}

**Through I12 (ESTIMATE, version 2).** In the geometric normalisation of the gluon field the trace anomaly of QCD gives the
matrix element of $G^A_{\mu\nu}G^{A\mu\nu}$ in a nucleon, and with (FE-71) the scalar coupling of the dark matter to a nucleon and its
spin-independent cross-section:

$$ \langle\mathrm{N}\rvert G^A_{\mu\nu}G^{A\mu\nu}\lvert\mathrm{N}\rangle = -g_3^2\,\frac{8\pi}{9\alpha_3}\,m_{\mathrm{N}}f_{\mathrm{TG}} = -\frac{32\pi^2}{9}\,m_{\mathrm{N}}f_{\mathrm{TG}},\qquad f_{\mathrm{N}} = G_{\mathrm{g}}\,\frac{8\pi}{9\alpha_3}\,m_{\mathrm{N}}f_{\mathrm{TG}},\qquad \sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi} $$
<!-- symbols: AUTO -->

($f_{\mathrm{TG}} = 0.92$, $\alpha_3 = 0.3$ at a low scale, $m_{\mathrm{N}} = 0.939$ GeV, FROM MEMORY). Even if the whole coupling of version 2 (the
relic strength $(15.5\ \text{TeV})^{-3}$) were in gluons, $G_{\mathrm{g}} = G_{\mathrm{I12}}/\sqrt8$, the cross-section per dark-matter species
would be $\sigma_{\mathrm{SI}} = 6.3\times10^{-53}$ cm$^2$ (the two halves have the same cross-section and together the full local density,
so the limit applies as for one species), eight orders below the LZ limit extrapolated linearly in the mass from
$2.2\times10^{-48}$ cm$^2$ at 40 GeV to 44.35 TeV ($2.44\times10^{-45}$ cm$^2$; STANDARD FROM MEMORY, the extrapolation an ESTIMATE): the
limit would allow a gluon coupling whose square is $3.9\times10^7$ times the relic requirement. The electroweak channels have no
tree-level nucleon coupling.

**Through I13 and I11 (DERIVED; ESTIMATE for the limit).** These portals couple the dark matter coherently to the vector currents of
the quarks. With unpolarised quarks (each chirality carries half of the density) the couplings to the up and down quarks are

$$ G_{\mathrm{u}} = \frac{G_{\mathrm{A}}}{3}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{u_R}}{2} + \frac{G_{\mathrm{V}}}{3}\,\frac{\tilde I_Q + \tilde I_{u_R}}{2},\qquad G_{\mathrm{d}} = \frac{G_{\mathrm{A}}}{3}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{d_R}}{2} + \frac{G_{\mathrm{V}}}{3}\,\frac{\tilde I_Q + \tilde I_{d_R}}{2} $$
<!-- symbols: AUTO -->

and the couplings to a proton, a neutron and a xenon nucleus, and the cross-section per nucleon, are

$$ f_{\mathrm{p}} = 2G_{\mathrm{u}} + G_{\mathrm{d}},\qquad f_{\mathrm{n}} = G_{\mathrm{u}} + 2G_{\mathrm{d}},\qquad f_{\mathrm{N}} = \frac{Z_{\mathrm{Xe}}f_{\mathrm{p}} + (A_{\mathrm{Xe}} - Z_{\mathrm{Xe}})f_{\mathrm{n}}}{A_{\mathrm{Xe}}},\qquad \sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi} $$
<!-- symbols: AUTO -->

with $Z_{\mathrm{Xe}} = 54$, $A_{\mathrm{Xe}} = 131$: $f_{\mathrm{p}} = 1.915\times10^{-9}$ GeV$^{-2}$, $f_{\mathrm{n}} = 1.917\times10^{-9}$ GeV$^{-2}$ and
$\sigma_{\mathrm{SI}} = 4.01\times10^{-46}$ cm$^2$, 0.16 of the extrapolated LZ limit (I11 alone would give $3.9\times10^{-60}$ cm$^2$): the dark matter
of UM-2 is allowed and testable by the next generation of xenon detectors (an exposure about six times that of LZ).

**Indirect detection (DERIVED).** The I12 annihilation is p-wave, suppressed by $v_{\mathrm{rel}}^2 \sim 10^{-6}$ in galaxies today; the I13
annihilation is s-wave and continues today, per pair of particle and antiparticle, into quark pairs with

$$ \sigma_{\mathrm{I13}}v_{\mathrm{rel}} = \sum_f\frac{N_{\mathrm{c}}G_f^2M_{\mathrm{DM}}^2}{2\pi} = 9.76\times10^{-26}\ \text{cm}^3/\text{s}\qquad (v_{\mathrm{rel}} \to 0), $$
<!-- symbols: AUTO -->

the thermal value for a heavy relic. **Colliders:** 44 TeV is beyond the reach of present and planned colliders.

## B.5 The self-interaction bound {-}

The contact self-interaction of (IN-5) contains a four-dimensional term that couples a dark-matter pair to a fold-band pair
through the transition scalar density of the two orbitals; $n^{\mathrm{sc}}_{\mathrm{DF}}$ is odd under the fold reflection and its square
even, so the dark matter can annihilate into the fold bands (ESTIMATE for the cross-section, whose Fierz coefficients are not
computed):

@@FE-135@@

While the dark matter is in equilibrium, from $T_{\mathrm{max}} = 10$ TeV (ASSUMED) to the freeze-out, each annihilation puts
$2M_{\mathrm{DM}}$ into the fold bands:

@@FE-136@@

which gives $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$ as long as the fold bands stay out of equilibrium (DERIVED; the
re-integration of the residual analysis agrees to $1.1\times10^{-5}$), with $\tilde I_\lambda = 14.38$. $\Delta N_{\mathrm{eff}} \le 0.001$ therefore
requires

$$ G_\lambda \le 2.3\times10^{-15}\ \text{GeV}^{-2} = 1.8\times10^{-6}\,G_{\mathrm{A}},\qquad \frac{2\Gamma_\lambda}{n_{\mathrm{fold,eq}}\mathcal{H}} \le 0.027 $$
<!-- symbols: AUTO -->

(ASSUMED bound of UM-2). If the fold bands were kept in equilibrium, they would decouple as four Weyl species, with the extra
radiation, written out again,

@@FE-133@@

($N_{\mathrm{W}} = 4$): the test coupling $\lambda_{\mathrm{test}} = 7\times10^{-5}H^{-6}$ of the Kohn-Sham computations would, with
$v_{\mathrm{t}} = H^{-3}$, give $G_\lambda = 1.14\times10^{-9}$ GeV$^{-2}$, keep the fold bands in equilibrium down to $T = 2.6$ TeV (production rate up
to $6.3\times10^9$ times the Hubble rate) and add $\Delta N_{\mathrm{eff}} = 0.19$ ($N_{\mathrm{eff}} = 3.23$, 2.9 standard deviations above ACT DR6).
UM-2 therefore ASSUMES $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$, i.e. $\lambda \le 1.4\times10^{-10}H^{-6}$ for $v_{\mathrm{t}} = H^{-3}$, or
$v_{\mathrm{t}} \ge 4.9\times10^5H^{-3}$ for $\lambda = \lambda_{\mathrm{test}}$; with such a coupling the self-interaction mean fields of every
Kohn-Sham state of the cosmology are negligible, and $\lambda_{\mathrm{test}}$ is only the value with which the Kohn-Sham machinery was tested.

## B.6 The cosmological tests {-}

**The massless quanta are radiation, not dark matter (DERIVED).** The fold bands of both halves are massless four-dimensional fermions
(energy $\mathrm{e}^{-a_4}\lvert k\rvert$); a gas of them has $w_{\mathrm{KS}} = 1/3$ exactly (section B.8). In UM-2 they are never thermalised: there is
no tip operator, I12 and I13 do not act on them, the self-interaction is bounded (section B.5), and the vector portal I11 is weak. I11
produces them by freeze-in from the Standard-Model plasma:

@@FE-129@@

@@FE-130@@

(the sum $\sum_fN_{\mathrm{c}}(q_f\tilde I_{of})^2 = 126.85$ runs over the fifteen multiplets of three generations in the plasma, without the
right-handed neutrinos). Integrated from $T_{\mathrm{max}} = 10$ TeV this gives $\Delta N_{\mathrm{eff}} = 5.21\times10^{29}\,G_{\mathrm{V}}^2$ GeV$^4$, so the
benchmark strength (ASSUMED) $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ ($3.8\times10^{-12}\,G_{\mathrm{F}}$) adds $\Delta N_{\mathrm{eff}} = 0.001$
(and $8.0\times10^{-6}$, $1.25\times10^{-4}$, $8.0\times10^{-3}$ for $T_{\mathrm{max}} = 2$, 5 and 20 TeV), while the production rate per fold quantum
stays at most 0.012 of the Hubble rate: the fold bands never reach equilibrium, and $N_{\mathrm{eff}} = 3.0442$ instead of $3.0432$. A trace of
dark radiation, not dark matter.

**Had one half's fold band been thermalised (DERIVED).** It would decouple as two Weyl species with the extra radiation (written
out again)

@@FE-133@@

($N_{\mathrm{W}} = 2$; $g_s$ the entropy degrees of freedom at its decoupling; $F_{\mathrm{h}}$ corrects for the heating of the neutrinos by
$e^+e^-$ annihilation, which an earlier-decoupled species does not receive, with the computed $T_\nu/T_\gamma = 0.71664$ and $h_\nu = 0.00165$):
$\Delta N_{\mathrm{eff}} = 0.0958$ for a decoupling above the electroweak scale ($g_s = 105.75$) and $0.1963$ just above the QCD crossover
($g_s = 61.75$). At fixed Planck parameters these would change the CMB temperature spectrum by up to 1.5 % and 3.1 % for
$30 \le l \le 2500$, and put $N_{\mathrm{eff}}$ 2.1 and 2.9 standard deviations above the ACT DR6 value $2.86 \pm 0.13$.

**The dark matter is cold (DERIVED, STANDARD equations).** The heavy odd quanta are pressureless ($w_{\mathrm{KS}} = 0$ at rest), so in the
linear cosmology of UM-2 they obey the equations of cold dark matter

@@FE-91@@

with $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$, the relic of the two species, which agrees with the dark-matter density of the CMB computation to
$3.1\times10^{-9}$ (residual analysis).

**Open.** Whether the fold bands are produced gravitationally during the primordial deflation, and whether the radion oscillation
dilutes the relic (the moduli problem), are OPEN.

## B.7 Assessment of the association with dark matter {-}

The association of dirac16complex with dark matter is valid in UM-2 under stated conditions: (i) the good sector (no extra-time
momenta; outside it the halves mix and modes are tachyonic, OPEN); (ii) the exact fold parity of both halves, which UM-2 secures by
containing no oriented tip operator ($P_L\Psi_B = 0$ at the tip even protects $\Psi_B$ against any chiral tip current); (iii) fold bands
that never thermalise (I11 weak, I12 and I13 blind to them, a weak self-interaction $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$, no dipole
portal, no significant gravitational production); (iv) an annihilation channel that produces the relic within unitarity: the
gauge-kinetic portal I12 alone cannot (its freeze-out requirement exceeds the $^3P_0$ bound 3.5 times), the INVENTED s-wave portal I13
to the baryon-number current does, with $G_{\mathrm{A}} = 1.28\times10^{-9}$ GeV$^{-2}$ (physics accuracy about 1 %, set by the neglected
order-$\alpha$ pressure of the plasma), and predicts a direct-detection signal at 0.16 of the present LZ limit; (v) no late dilution by
the radion (the moduli problem). The candidate is falsifiable: a xenon exposure about six times that of LZ would test it. It is the
heavy odd part of the field, not the field as a whole, that is dark matter; the field's massless fold bands are radiation
($\Delta N_{\mathrm{eff}} = 0.001$).

## B.8 dirac16complex as dark energy: why it is not supported {-}

### No positive-energy state accelerates (DERIVED) {-}

The many-body states of $\Psi$ on the static block (computed with $H = 1$, $a_4 = 0$, $f = f_*$) are described by the Kohn-Sham
equations coupled to all fields

@@FE-63@@

with the mean fields

@@FE-64@@

the densities, momentum shells, cell volume and occupations

@@FE-65@@

and the boundary conditions of the orbitals, written out again,

@@FE-69@@

Their energy-momentum tensor is

@@FE-67@@

and the equation of state of a state is the ratio of its integrated 3-space pressure to its integrated energy density:

$$ w_{\mathrm{KS}} = \frac{2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,p_3\,\mathrm{d}y}{2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,\rho\,\mathrm{d}y} $$
<!-- symbols: AUTO -->

Every computed state has $w_{\mathrm{KS}} \ge 0$: eight dark-matter quanta at rest $w_{\mathrm{KS}} = 0$ ($2.8\times10^{-5}$ with $\lambda_{\mathrm{test}}$);
the fold-band gas of 592 quanta $w_{\mathrm{KS}} = 1/3$ ($0.3312$ with $+\lambda_{\mathrm{test}}$, $0.3354$ with $-\lambda_{\mathrm{test}}$). The quanta of
dirac16complex are matter or radiation.

### The condensate runs away (DERIVED) {-}

A homogeneous scalar condensate of $\Psi$, diluted by the expansion, with the self-interaction energy $U_{\mathrm{cond}}$ has

$$ U_{\mathrm{cond}} = \frac{\lambda}{2}\big(n^{\mathrm{sc}}\big)^2,\qquad n^{\mathrm{sc}} \propto \mathrm{e}^{-3a_4},\qquad \rho = m_\Psi n^{\mathrm{sc}} + U_{\mathrm{cond}},\qquad p = n^{\mathrm{sc}}\,\frac{\mathrm{d}U_{\mathrm{cond}}}{\mathrm{d}n^{\mathrm{sc}}} - U_{\mathrm{cond}} = \frac{\lambda}{2}\big(n^{\mathrm{sc}}\big)^2 $$
<!-- symbols: AUTO -->

so that its equation of state, in the parametrisation of the supernova fits, is

$$ w_{\mathrm{de}} = \frac{p}{\rho} = \frac{\mathcal{X}}{1 + \mathcal{X}},\qquad \mathcal{X} = \frac{\lambda n^{\mathrm{sc}}}{2m_\Psi} = \mathcal{X}_0\,\mathrm{e}^{-3a_4},\qquad \mathcal{X}_0 = \frac{w_{\mathrm{de},0}}{1 - w_{\mathrm{de},0}},\qquad w_{\mathrm{de},a} = -\frac{\mathrm{d}w_{\mathrm{de}}}{\mathrm{d}\,\mathrm{e}^{a_4}}\Big\vert_{a_4 = 0} = \frac{3\mathcal{X}_0}{(1 + \mathcal{X}_0)^2} $$
<!-- symbols: AUTO -->

A negative $w_{\mathrm{de}}$ needs $\lambda < 0$, and then the energy density $\rho = m_\Psi n^{\mathrm{sc}}(1 + \mathcal{X})$ crosses zero where
$\mathcal{X} = -1$, in the past:

$$ \mathrm{e}^{a_4} = \big(-\mathcal{X}_0\big)^{1/3},\qquad z_{\mathrm{red}} = \big(-\mathcal{X}_0\big)^{-1/3} - 1 $$
<!-- symbols: AUTO -->

| $w_{\mathrm{de},0}$ | $-1.2$ | $-1$ | $-0.9$ | $-0.861$ | $-0.764$ | $-0.5$ | $-0.3$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $w_{\mathrm{de},a}$ (tangent) | $-7.92$ | $-6.00$ | $-5.13$ | $-4.81$ | $-4.04$ | $-2.25$ | $-1.17$ |
| energy zero at $z_{\mathrm{red}}$ | $0.224$ | $0.260$ | $0.283$ | $0.293$ | $0.322$ | $0.442$ | $0.630$ |

The supernova fits of the author's private file, a constant $w_{\mathrm{de}} = -0.764$ and $(w_{\mathrm{de},0}, w_{\mathrm{de},a}) = (-0.861, -0.60)$,
are not reproduced: a condensate tuned to $w_{\mathrm{de},0} = -0.861$ has $w_{\mathrm{de},a} = -4.81$ and a negative energy density beyond
$z_{\mathrm{red}} = 0.29$.

![The equation of state of the $\lambda < 0$ condensate for several present values $w_{\mathrm{de},0}$: $w_{\mathrm{de}}$ runs away to $-\infty$ where the energy density crosses zero. The labels are in the plain-text notation of the plotting script: "z" is the redshift $z_{\mathrm{red}}$, "w" is $w_{\mathrm{de}}$ and "w0" is $w_{\mathrm{de},0}$.](figures/fig_analysis_condensate.png)

### The vacuum energy and the tuning (OPEN) {-}

A natural vacuum energy of the cell exceeds the observed dark-energy density by 64 orders of magnitude:

$$ \rho_{\mathrm{vac}} = \frac{m_{\mathrm{KK}}^4}{16\pi^2} = 1.4\times10^{18}\ \text{GeV}^4,\qquad \frac{\rho_{\mathrm{vac}}}{\rho_{\mathrm{de}}} = 5.5\times10^{64}\qquad \big(\rho_{\mathrm{de}} = 2.5\times10^{-47}\ \text{GeV}^4\big) $$
<!-- symbols: AUTO -->

In UM-2 the four-dimensional cosmological term is the residual of the stabiliser balance in the reduction of the Lovelock action
on the static block:

@@FE-48@@

zero at the static point by construction. The observed dark energy needs

$$ \frac{\Lambda_4}{H^2} \sim \Big(\frac{\mathcal{H}_0}{H}\Big)^2 = 1.0\times10^{-92}: $$
<!-- symbols: AUTO -->

the cosmological-constant problem, unsolved (OPEN). A slowly deflating block cannot provide a dynamical dark energy instead,
because it would make $\alpha_{\mathrm{em}}$, $G_{\mathrm{N}}$ and the masses drift ($\lvert\mathcal{H}_f\rvert < 3.6\times10^{-8}\,\mathcal{H}_0$, section
A.8), the neutrino oscillation lengths most of all.

### Assessment of the association with dark energy {-}

The association of dirac16complex with dark energy is not supported in UM-2: its positive-energy states are matter or radiation,
its only accelerating configuration is unstable and reaches a negative energy density at $z_{\mathrm{red}} \approx 0.2$ to $0.6$, and the
measured $(w_{\mathrm{de},0}, w_{\mathrm{de},a})$ are not reproduced. The dark energy of UM-2 is the tuned four-dimensional cosmological term
$\Lambda_4$.
