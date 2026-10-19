# Step 9: the thermal history and the relic with I13

Step 9 computes the thermal history of UM-2 with the $x_0$ masses of step 2, solves the Boltzmann equation of the dark matter with
the cross-sections of I12 and I13 and their partial-wave unitarity bounds, fixes the benchmark strengths of the three portals (I13 by
the relic, I11 by the freeze-in of the fold bands, I12 by unitarity), shows why I13 couples to the baryon current and not to $B - L$,
bounds the self-coupling of dirac16complex by the dark radiation it would make, and estimates the detection of the dark matter.

## The field equations of step 9

The portals whose strengths step 9 fixes:

@@T:Portal I11@@

@@T:Portal I12@@

@@T:Portal I13@@

The degrees of freedom of the hot Universe:

@@idealgas@@

@@dof@@

@@crossover@@

The electroweak couplings of the unitarity-safe I12 benchmark are run to $2M_{\mathrm{DM}}$ with the one-loop equations of step 8:

@@running@@

The dark matter: the Boltzmann equation, the thermal average, the cross-sections and their unitarity bounds, with the
four-dimensional couplings of the portals on the zero modes (step 8):

@@boltz@@

@@thermal_avg@@

@@relic@@

@@contact4d@@

@@xsec@@

@@unitarity@@

The fold bands of dirac16complex made by freeze-in through I11, and their dark radiation:

@@freezein@@

@@neff_fold@@

The right-handed neutrinos (the counterfactual that motivates the baryon current), the extra radiation of an early-decoupled species
and the production of right-handed neutrinos through I11:

@@nuR_BL@@

@@nuR_el@@

@@deltaneff@@

@@nuR_I11@@

The self-interaction channel of the dark matter into the fold bands:

@@selfint@@

@@selfint_energy@@

## The approximation of step 9

* *Ideal gases.* The degrees of freedom are those of ideal gases with the $x_0$ masses and a modelled QCD crossover. The
  order-$\alpha$ interaction pressure of the plasma, which step 8 uses for the condensates, is not small at the freeze-out: $-5.4$ %
  of the ideal-gas pressure at $T = 1.42$ TeV (QCD $-4.7$ %, $SU(2)$ $-0.7$ %, $U(1)_Y$ $-0.10$ %); since the relic scales as
  $g_\rho^{1/2}/g_s$ at the freeze-out, including it would raise $\Omega_{\mathrm{DM}}h_{100}^2$ by about $2.7$ % and the relic
  strength $G_{\mathrm{A}}$ by about $1.4$ % (ESTIMATE, computed in version 4): the physical accuracy of $G_{\mathrm{A}}$ is about
  1 %, not the $10^{-6}$ of its root finding.
* *Instantaneous neutrino decoupling* at 2 MeV in the degrees of freedom (it enters only the entropy today, taken as the standard
  $g_s = 43/11$, and the nucleosynthesis environment of step 8).
* *The dark matter* in kinetic equilibrium with Maxwell-Boltzmann statistics; its own contribution to $g_\rho$ is left out
  ($1.1\times10^{-2}$ of the energy density at the start of the integration, $x = 5$, where $Y_{\mathrm{DM}} = Y_{\mathrm{eq}}$ anyway,
  and $7\times10^{-12}$ at the freeze-out); the fold bands of the freeze-in are left out of the Hubble rate ($3.5\times10^{-4}$ of the
  energy density at the freeze-out, which moves the relic by $1.7\times10^{-4}$).
* *The unitarity completion.* Where an effective cross-section exceeds its partial-wave bound it is replaced by the bound (a
  completion that saturates it); for the I13 relic $21.7$ % of the freeze-out rate comes from collisions at the unitarity bound of the $^3S_1$ partial wave.
* *The freeze-in* with Maxwell-Boltzmann statistics and without inverse processes (the production rate per fold quantum is $0.012$
  of the Hubble rate at the highest temperature $T_{\mathrm{max}} = 10$ TeV, ASSUMED; the result grows like $T_{\mathrm{max}}^3$).
* *Estimates.* The elastic rate of the right-handed neutrinos (a factor 1/2 or 2 moves their kinetic decoupling to
  $M_{\mathrm{DM}}/T = 23.77$ or $25.07$ and $\Delta N_{\mathrm{eff}}$ by at most $9.5\times10^{-6}$ of itself) and the cross-section
  of the self-interaction channel (its Fierz coefficients are not computed; at the bound the inverse annihilation of the fold quanta is
  $0.027$ of the Hubble rate).

## The solution of step 9

### The thermal history

The species in equilibrium (photon, gluons, $W^+$, $W^-$, $Z$, six quarks, three charged leptons, three neutrinos; no Higgs particle;
not the right-handed neutrinos, the fold bands, the radion or the Kaluza-Klein modes; the dark matter is not counted, since it would
add less than 0.1 at 5 TeV and nothing at its freeze-out) with their $x_0$ masses give the degrees of freedom of the field equations
written above, with the QCD crossover modelled by the weight $w_{\mathrm{QGP}}$ of the quark-gluon plasma against a gas of the twelve
lightest hadron multiplets (ASSUMED; masses in GeV and internal states: pion 0.1380, 3; kaon 0.4956, 4; eta 0.5479, 1; rho meson
0.7753, 9; omega meson 0.7827, 3; K-star 0.8917, 12; nucleon 0.9389, 8; eta-prime 0.9578, 1; phi meson 1.0195, 3; Lambda baryon
1.1157, 4; Sigma baryon 1.1932, 12; Delta baryon 1.232, 32; quoted without a checked reference) and the neutrinos decoupled at 2 MeV (DERIVED):

| $T$ | 5 TeV | 1.42 TeV | 200 GeV | 10 GeV | 1 GeV | 300 MeV | 155 MeV | 100 MeV | 3 MeV | 1 MeV | 0.1 MeV | today |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| $g_\rho$ | 105.75 | 105.73 | 104.95 | 86.22 | 76.34 | 64.57 | 42.35 | 17.54 | 10.74 | 10.56 | 4.30 | 3.363 |
| $g_s$ | 105.75 | 105.73 | 104.68 | 86.13 | 75.50 | 64.14 | 41.76 | 17.16 | 10.74 | 10.56 | 4.78 | 3.909 |

i.e. $105.75$ above the top threshold (three generations without a Higgs particle), $86.25$ without t, $W$, $Z$, $10.75$ before
$e^\pm$ annihilation, and today $g_s = 43/11 = 3.9091$, $g_\rho = 3.3626$ and the entropy density $s_0 = 2891.3$ cm$^{-3}$
($T_\gamma = 2.7255$ K).

### The Boltzmann equation

The Boltzmann equation of one Dirac species is integrated implicitly (Radau, $\ln Y_{\mathrm{DM}}$ from $x = 5$ to $2000$, relative
tolerance $10^{-10}$) with the thermal average by adaptive quadrature in the kinetic energy of the pair in units of its rest energy,
$E_{\mathrm{cm}}^2/(4M_{\mathrm{DM}}^2) - 1$, with exponentially scaled Bessel functions, tabulated on 260 points in $x$. Validation
(DERIVED): an s-wave cross-section of $4.4\times10^{-26}$ cm$^3$/s gives $\Omega_{\mathrm{DM}}h_{100}^2 = 0.1275$ (the freeze-out
formula $0.1306$), and the late-time integral $1/Y_\infty - 1/Y_{\mathrm{DM}}(x)$ equals the integral of the collision term from $x$ on
to $1.3\times10^{-8}$; for I12 the exact average exceeds the non-relativistic $6G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4/(\pi x)$ by $0.408$,
$0.111$, $0.031$, $0.0030$ at $x = 10$, $30$, $100$, $1000$, i.e. by about $3/x$ at large $x$.

### I12 alone, and partial-wave unitarity

The effective operator would need $G_{\mathrm{I12}} = 2.509\times10^{-13}$ GeV$^{-3}$ $= (15.86\ \text{TeV})^{-3}$ for
$\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ per species ($x_{\mathrm{f}} = 31.70$, $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) =
1.89\times10^{-25}$ cm$^3$/s; step 7: $(15.5\ \text{TeV})^{-3}$ from the freeze-out formula). Its cross-section exceeds the $^3P_0$ bound
above $E_{\mathrm{cm}} = 89510$ GeV (815 GeV above threshold), i.e. above the relative velocity $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} =
0.269$ ($0.274$ from the non-relativistic formula); at the freeze-out 96 % of the annihilation rate comes from collisions above the
crossing, and 75 % of the pairs of the non-relativistic Maxwell distribution are faster than $0.274$. With $\sigma = \pi/(4k_{\mathrm{cm}}^2)$
at every energy, the largest annihilation from $^3P_0$, each species leaves $\Omega_{\mathrm{DM}}h_{100}^2 = 0.0582$ (at its freeze-out,
$x_{\mathrm{f}} = 30.77$, $\langle\sigma v_{\mathrm{rel}}\rangle = 5.33\times10^{-26}$ cm$^3$/s against the non-relativistic
$\sqrt{\pi x}/M_{\mathrm{DM}}^2 = 5.84\times10^{-26}$ cm$^3$/s at the same $x$); the effective operator capped at the bound leaves $0.1544$,
$0.1081$, $0.0836$, $0.0649$, $0.0585$ for $G_{\mathrm{I12}}^2/G_{\mathrm{relic}}^2 = 1$, $3$, $10$, $100$, $10^4$ ($G_{\mathrm{relic}}$ the
relic strength above). Within perturbative couplings I12 therefore overproduces the dark matter; only a strongly coupled $^3P_0$
channel at the unitarity limit could give the relic. UM-2 sets I12 to the unitarity-safe benchmark

$$
G_{\mathrm{I12}} = \frac{\pi}{2M_{\mathrm{DM}}^3} = 1.801\times10^{-14}\ \text{GeV}^{-3} = (38.2\ \text{TeV})^{-3},\qquad
\frac{c_{\mathrm{I12}}}{\Lambda_\star^3} = \frac{G_{\mathrm{I12}}}{\mathcal{O}_{\mathrm{DM}}\sqrt{8g_3^4 + 3g_2^4 + g_1^4}}
 = 1.106\times10^{-14}\ \text{GeV}^{-3},
$$

<!-- symbols: AUTO -->

below the bound up to $E_{\mathrm{cm}} = 106363$ GeV $= 2.40\,M_{\mathrm{DM}}$ (a fraction $5.2\times10^{-4}$ of the annihilation rate at
$x = 30$ comes from above), with universal coefficients $c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$ and the
one-loop couplings at $2M_{\mathrm{DM}} = 88.7$ TeV ($1/\alpha_3 = 1/\alpha_3(m_{\mathrm{Z}}) + \frac{7}{2\pi}\ln(2M_{\mathrm{DM}}/m_{\mathrm{Z}})$
and the running electroweak couplings of step 8 at $\mu_{\mathrm{ren}} = 2M_{\mathrm{DM}}$, from $\sin^2\theta_{\overline{\mathrm{MS}}} =
0.23122$ and $\alpha_{\mathrm{em}}(m_{\mathrm{Z}}) = 1/127.95$: $g_3^2 = 0.7786$, $g_2^2 = 0.3781$, $g_1^2 = 0.1380$), i.e.
$\Lambda_\star/c_{\mathrm{I12}}^{1/3} = 44.9$ TeV. Alone it would leave $\Omega_{\mathrm{DM}}h_{100}^2 = 8.0$ per species.

### The relic with I13

With $G_f = G_{\mathrm{A}}\,q^B_f\,\tilde I^{(b)}_{of}$ for each quark Weyl component ($\mathcal{S}_B = \sum_fN_{\mathrm{c}}(q^B_f\tilde
I^{(b)}_{of})^2 = 16.351$ for the dark-matter orbital) the s-wave cross-section of I13 and its $^3S_1$ unitarity bound are those written above,
and the Boltzmann equation with $\sigma_{\mathrm{I12}} + \sigma_{\mathrm{I13}}$ gives each species $\Omega_{\mathrm{DM}}h_{100}^2 =
0.060$ for (DERIVED)

$$
G_{\mathrm{A}} = 1.278\times10^{-9}\ \text{GeV}^{-2} = 1.1\times10^{-4}\,G_{\mathrm{F}}\qquad (x_{\mathrm{f}} = 31.23),
$$

<!-- symbols: AUTO -->

with $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 9.50\times10^{-26}$ cm$^3$/s from I13 and $9.9\times10^{-28}$ cm$^3$/s from
I12, the I13 cross-section capped at its bound, which it reaches only above $v_{\mathrm{rel}} = 0.51$ (22 % of the freeze-out rate then
comes from collisions at the bound; without the cap $G_{\mathrm{A}} = 1.269\times10^{-9}$ GeV$^{-2}$, and the uncapped cross-section
exceeds the bound above $v_{\mathrm{rel}} = 0.52$, for 25 % of the rate). The relic of UM-2 is a thermal freeze-out with most
annihilations (78 % of the rate) below the unitarity bound; the contact form of I13 is an effective description (for the quark
doublet $(G_{\mathrm{A}}q^B_Q\tilde I^{(b)}_Q)^{-1/2} = 30$ TeV, below the energies $E_{\mathrm{cm}} \approx 89$ TeV of the
annihilations), whose completion by a mediator is OPEN.

**Why the baryon current.** With the $B - L$ current instead ($\mathcal{S}_{B-L} = 22.92$ over the quarks, the leptons and the
$\nu_R$, so the relic needs $G_{\mathrm{A}}^{B-L} = G_{\mathrm{A}}(16.351/22.92)^{1/2} = 1.072\times10^{-9}$ GeV$^{-2}$ with the uncapped
$G_{\mathrm{A}}$; the three $\nu_R$ carry 1.2 % of the annihilation) the right-handed neutrinos would be thermalised: per flavour, with
$G_\nu = G_{\mathrm{A}}^{B-L}\tilde I^{(b)}_{\nu_R}$ (one representative flavour, the rms of the three overlaps, which differ by 2 %),
from zero abundance at $M_{\mathrm{DM}}/T = 2$ they reach 0.9997 of the equilibrium number by $M_{\mathrm{DM}}/T = 40$; the
number-changing rate falls below the Hubble rate at $M_{\mathrm{DM}}/T = 16.1$, and the elastic scattering on the dark matter
(ESTIMATE) at $M_{\mathrm{DM}}/T = 24.4$ ($T = 1816$ GeV, $g_s = 105.7$); the three $\nu_R$ would add $\Delta N_{\mathrm{eff}} =
3(10.75/g_s)^{4/3}F_{\mathrm{h}} = 0.144$ ($F_{\mathrm{h}} = 1.0095$), $N_{\mathrm{eff}} = 3.187$, 2.5 standard deviations above ACT DR6
($2.86 \pm 0.13$). With $J^B$ the $\nu_R$ keep their tip coupling and the I11 coupling of charge $-1$, through which the dark matter
annihilates into $\nu_R$ pairs at only $r_{\nu_R} = 2.0\times10^{-17}$ of the I13 rate into quarks (DERIVED): they are never thermalised.

### The fold bands: freeze-in through I11

With $G_f = G_{\mathrm{V}}q_f\tilde I_{of}$ for the fold band $o$, the pair production $f\bar f \to \Psi_{\mathrm{fold}}
\bar\Psi_{\mathrm{fold}}$ has the cross-section $G_f^2E_{\mathrm{cm}}^2/(12\pi)$ per Dirac $f$ (spin averaged; half for one chirality),
and the rate density and the energy injection are those written above (Maxwell-Boltzmann; $\int_0^\infty x^6K_1\,\mathrm{d}x = 384$,
$\int_0^\infty x^7K_2\,\mathrm{d}x = 3072$, both checked), with $N_{\mathrm{fold}} = 2$ and $\sum_fN_{\mathrm{c}}(q_f\tilde I_{of})^2 =
126.85$ over the Weyl components of three generations (no $\nu_R$ in the plasma). Integrated from $T_{\mathrm{max}}$ (DERIVED):
$\Delta N_{\mathrm{eff}} = 5.21\times10^{29}\,G_{\mathrm{V}}^2$ GeV$^4$ for $T_{\mathrm{max}} = 10$ TeV, so the benchmark $\Delta
N_{\mathrm{eff}} = 0.001$ means

$$
G_{\mathrm{V}} = 4.38\times10^{-17}\ \text{GeV}^{-2};
$$

<!-- symbols: AUTO -->

for that $G_{\mathrm{V}}$, $\Delta N_{\mathrm{eff}} = 8.0\times10^{-6}$, $1.25\times10^{-4}$, $1.0\times10^{-3}$, $8.0\times10^{-3}$ at
$T_{\mathrm{max}} = 2$, $5$, $10$, $20$ TeV, and at $T_{\mathrm{max}}$ the production rate per fold quantum is $0.012$ of the Hubble
rate: never in equilibrium.

### The self-interaction channel

The contact self-interaction $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ contains the term written above, with the transition scalar density
$n^{\mathrm{sc}}_{\mathrm{DF}}$ of the dark-matter orbital and the fold zero mode, which is odd under the fold reflection while its square
is even, so the dark matter can annihilate into the fold bands; $\tilde I_\lambda = 14.38$ (units of $H$; DERIVED), and the s-wave
cross-section is estimated as the value of one vector channel per final fold species (ESTIMATE). While the dark matter is in
equilibrium ($T_{\mathrm{max}} = 10$ TeV to $x_{\mathrm{f}} = 31.23$) each annihilation puts $2M_{\mathrm{DM}}$ into the fold bands,
which gives (DERIVED) $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$ as long as the fold bands stay out of
equilibrium. $\Delta N_{\mathrm{eff}} \le 0.001$ therefore requires

$$
G_\lambda \le 2.3\times10^{-15}\ \text{GeV}^{-2}\quad (1.8\times10^{-6}\,G_{\mathrm{A}}),
$$

<!-- symbols: AUTO -->

at which the production rate per fold quantum is at most 0.027 of the Hubble rate. The self-coupling
$\lambda_{\mathrm{test}} = 7\times10^{-5}\,H^{-6}$ of the Kohn-Sham tests of step 3 would, with $v_{\mathrm{t}} = H^{-3}$, give
$G_\lambda = 1.14\times10^{-9}$ GeV$^{-2}$, keep the fold bands in equilibrium down to $T = 2.6$ TeV (production rate up to
$6.3\times10^9$ times the Hubble rate) and add $\Delta N_{\mathrm{eff}} = 4(10.75/g_s)^{4/3}F_{\mathrm{h}} = 0.19$ (four Weyl species,
$N_{\mathrm{eff}} = 3.23$). UM-2 therefore ASSUMES $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$, i.e. $\lambda \le 1.4\times10^{-10}\,H^{-6}$
for $v_{\mathrm{t}} = H^{-3}$, or $v_{\mathrm{t}} \ge 4.9\times10^5\,H^{-3}$ for $\lambda = \lambda_{\mathrm{test}}$; with such a $\lambda$
the self-interaction mean fields of every Kohn-Sham state of the cosmology are negligible, and $\lambda_{\mathrm{test}}$ is only the value
with which the Kohn-Sham machinery was tested.

### Detection

Per nucleon, with the couplings of the dark matter to the up and down quarks (I13 and I11, unpolarised quarks with each chirality
half),

$$
G_{\mathrm{u}} = \frac{G_{\mathrm{A}}}{3}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{u_R}}{2} + \frac{G_{\mathrm{V}}}{3}\,\frac{\tilde I_Q + \tilde I_{u_R}}{2},
\qquad
G_{\mathrm{d}} = \frac{G_{\mathrm{A}}}{3}\,\frac{\tilde I^{(b)}_Q + \tilde I^{(b)}_{d_R}}{2} + \frac{G_{\mathrm{V}}}{3}\,\frac{\tilde I_Q + \tilde I_{d_R}}{2},
$$

<!-- symbols: AUTO -->

$$
f_{\mathrm{p}} = 2G_{\mathrm{u}} + G_{\mathrm{d}},\qquad f_{\mathrm{n}} = G_{\mathrm{u}} + 2G_{\mathrm{d}},\qquad
f_{\mathrm{N}} = \frac{Z_{\mathrm{Xe}}f_{\mathrm{p}} + (A_{\mathrm{Xe}} - Z_{\mathrm{Xe}})f_{\mathrm{n}}}{A_{\mathrm{Xe}}},\qquad
\sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi}
$$

<!-- symbols: AUTO -->

(xenon, $Z_{\mathrm{Xe}} = 54$, $A_{\mathrm{Xe}} = 131$): $f_{\mathrm{p}} = 1.915\times10^{-9}$, $f_{\mathrm{n}} = 1.917\times10^{-9}$ GeV$^{-2}$,
$\sigma_{\mathrm{SI}} = 4.01\times10^{-46}$ cm$^2$, 0.16 of the LZ limit linearly extrapolated to $44.35$ TeV ($2.44\times10^{-45}$ cm$^2$;
ESTIMATE): allowed and within reach of the next generation of xenon detectors (I11 alone: $3.9\times10^{-60}$ cm$^2$). The s-wave
annihilation into quark pairs continues today with

$$
\sigma_{\mathrm{I13}}\,v_{\mathrm{rel}}\big\vert_{v_{\mathrm{rel}}\to0} = \sum_f\frac{N_{\mathrm{c}}\,G_f^2\,M_{\mathrm{DM}}^2}{2\pi}
 = 9.76\times10^{-26}\ \text{cm}^3/\text{s}
$$

<!-- symbols: AUTO -->

(DERIVED, 7 + 16 checks).

![The thermal history of UM-2 (degrees of freedom with the $x_0$ masses, left) and the freeze-out of one dark-matter species through the effective I12 at the relic strength and at the $^3P_0$ unitarity limit (right).](figures/fig_thermal_relic.png)

## The check of step 9

**In its own equations.**

* *The degrees of freedom.* $g_\rho$ and $g_s$ at the 13 tabulated temperatures, recomputed with adaptive quadrature, agree with the
  stored values to $4.6\times10^{-11}$; today $g_s = 43/11$ and $g_\rho = 2 + \frac78\cdot6\,(4/11)^{4/3}$ hold to $4.3\times10^{-9}$
  and $5.0\times10^{-9}$ (DERIVED).
* *The relic.* The Boltzmann equation re-solved at the stored $G_{\mathrm{A}}$ gives $\Omega_{\mathrm{DM}}h_{100}^2 = 0.0600000002$
  per species ($3.1\times10^{-9}$ from the condition); the late-time identity holds to $6.1\times10^{-9}$ on the recomputed I13 history
  and to $3.3\times10^{-9}$ on the stored I12 history; the freeze-out point is reproduced to $1.3\times10^{-12}$, the s-wave validation
  to $1.3\times10^{-8}$ (DERIVED).
* *The freeze-in.* $\Delta N_{\mathrm{eff}}$ per $G_{\mathrm{V}}^2$, re-integrated with Gauss-Legendre panels, agrees with the stored
  trapezoid value to $3.9\times10^{-5}$ (the trapezoid error on 600 logarithmic points); the Bessel moments are exact and the
  benchmark gives $0.001$ to $5\times10^{-13}$ (DERIVED).
* *The right-handed neutrinos.* Re-solved (Radau in the variable $M_{\mathrm{DM}}/T - 2$, relative tolerance $10^{-13}$), the $\nu_R$
  equation gives the number density $0.999697681992$ of its equilibrium value at $M_{\mathrm{DM}}/T = 40$, the stored value to
  $2.6\times10^{-13}$, unchanged when the coupling is varied by $\pm2\times10^{-12}$; the kinetic decoupling, $\Delta N_{\mathrm{eff}}
  = 0.144$, $G_{\mathrm{A}}^{B-L}$ and $r_{\nu_R}$ are reproduced to $2.5\times10^{-12}$ (DERIVED; the integration of version 3
  depended on the twelfth digit of its input coupling, the result did not).
* *The self-interaction channel.* $\Delta N_{\mathrm{eff}}$ per $G_\lambda^2$ re-integrated agrees to $1.1\times10^{-5}$, and
  $\Delta N_{\mathrm{eff}}$ at the bound is $0.001$ to $4\times10^{-12}$ (DERIVED).

**In concert with the other field equations.**

* *The masses of step 2* are the masses of the ideal gases to $3.1\times10^{-12}$, and the dark-matter mass of the $x_0$ spectrum is
  that of the Boltzmann equation to $8.1\times10^{-13}$ (DERIVED).
* *The four-dimensional Friedmann equation of step 1.* The Hubble rate of the Boltzmann equation at the freeze-out is that of the
  four-dimensional Friedmann equation with all species to $1.7\times10^{-4}$ (the fold bands of the freeze-in, left out here) (DERIVED).
* *The CMB of step 6.* The relic $2\times0.060$ is the cold dark matter of the CMB computation to $3.1\times10^{-9}$, and the freeze-in
  radiation is its $\Delta N_{\mathrm{eff}} = 0.0010$ exactly; the radiation today of the instantaneous decoupling differs from that of
  the CMB computation by $0.59$ % (DERIVED).
* *The coupled solution of step 8.* $G_{\mathrm{A}}$ and $G_{\mathrm{V}}$ are the strengths of the mean fields to $6.7\times10^{-13}$, the
  I12 benchmark to $1.6\times10^{-12}$, and the freeze-out temperature to $2.1\times10^{-12}$; the plasma energy density at the
  freeze-out differs from the block sources by $1.3\times10^{-3}$, by design (the trace anomaly of the interacting plasma) (DERIVED).
* *The neutrino decoupling of step 5.* The heating factor $F_{\mathrm{h}}$ is that of the decoupling to $5.8\times10^{-7}$ (DERIVED).

## The status of step 9

DERIVED: the degrees of freedom with the $x_0$ masses, the Boltzmann solutions, the violation of unitarity by I12 alone and the
unitarity-safe benchmark, the I13 relic strength, the freeze-in benchmark of I11, the thermalisation of the $\nu_R$ in the $B - L$
alternative, the bound on the self-interaction channel, the detection rates. ASSUMED: the model of the QCD crossover, $T_{\mathrm{max}}
= 10$ TeV, the bound on $\lambda$. ESTIMATE: the LZ extrapolation, the elastic $\nu_R$ rate, the self-interaction cross-section, the
effect of the order-$\alpha$ plasma pressure on the relic. INVENTED: the portals. OPEN: the completion of the I13 contact interaction by
a mediator above about 30 TeV.
