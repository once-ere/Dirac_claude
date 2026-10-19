# Step 8: the coupled solution in environments

Steps 1 to 3 solve the field equations of gravity, of the masses and of dirac16complex one after the other. Step 8 couples them
in ten environments, from the cosmic mean density today to neutron-star cores and the hot Universe up to the dark-matter
freeze-out: the Kohn-Sham levels of dirac16complex in the mean fields of the Standard-Model fields of the environment (I11, I12,
I13), the action of dirac16complex back on the Standard-Model fields (its scalar density changes the gauge couplings and the
$x_0$ problem of the $W$), and the response of the block to the energy-momentum tensor of every species, iterated to
self-consistency.

## The field equations of step 8

The portals:

@@T:Portal I11@@

@@T:Portal I12@@

@@T:Portal I13@@

The Kohn-Sham equations with the mean fields of the portals (step 3):

@@ks@@

@@ks_mean@@

On the zero modes the portals I11 and I13 are four-dimensional contact interactions, and I12 couples the dark matter to the
gauge-field invariants:

@@contact4d@@

@@i12dm@@

The shift of a Kohn-Sham level by the mean fields of an environment, and in matter of protons, neutrons and electrons:

@@levelshift@@

@@levelshift_env@@

@@env@@

The condensates of the gauge fields (the mean fields of I12):

@@gluon_cond@@

@@qcd_measure@@

@@vector_cond@@

@@running@@

@@ew_cond@@

dirac16complex acting on the Standard Model:

@@geff@@

@@dm_on_sm@@

Gravity closes the loop: the total source of gravity, with the energy-momentum tensors of the Standard-Model fields and of the
portals, drives the adiabatic block response of step 1,

@@t_total@@

@@adiabatic@@

@@t_f@@

@@t_gauge@@

@@t_portal@@

@@t_i12@@

@@coupled_block@@

@@pbar_hidden@@

@@dlnalpha@@

@@nucleon@@

@@qcd_thresholds@@

@@fermion_sens@@

## The approximation of step 8

* *First order in the mean fields.* The level shifts are linear responses (Hellmann-Feynman); the second order is
  $(\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}})^2 = 2.3\times10^{-12}$ at most. The screening of the response by the interacting
  dirac16complex gas is $3.5\times10^{-4}$ at the test coupling $\lambda_{\mathrm{test}}$ and $7.2\times10^{-10}$ at the bound on
  $\lambda$ of step 9.
* *The thermodynamics of the environments.* The plasma species as ideal gases with their $x_0$ masses, the net nucleons and
  electrons as degenerate Fermi gases in the cold environments, the QCD interaction measure from a lattice-like shape below 1 GeV
  (ESTIMATE) and leading-order perturbation theory above, the order-$\alpha$ pressure of the electroweak plasma without a scalar
  term and with the thermal suppression of a massive vector below $m_{\mathrm{W}}$ (ESTIMATE), one-loop running for the couplings,
  the QCD scale and the nucleon (ESTIMATE).

*The block response at first order and adiabatic*, with the gain of the loop mass $\to$ source $\to$ block $\to$ mass

$$
\frac{\lvert\Delta\ln f\rvert_{\text{second iteration}}}{\lvert\Delta\ln f\rvert_{\text{first iteration}}} \le 1.1\times10^{-33}
$$

<!-- symbols: AUTO -->

and the neglected inertia of the block $(\mathcal{H}/\omega_{\mathrm{r}})^2 = 3.4\times10^{-33}$ at the freeze-out (step 1).

## The solution of step 8

### The portals on the zero modes

A four-dimensional particle of the density $n_f$ (per 3-volume) in a zero mode with the normalised profile $\varrho_f(y)$ has the
proper eight-dimensional density $n_f\varrho_f\mathrm{e}^{-3Hy}/(2f^4v_{\mathrm{t}})$ on each half of the period, so the portals I11
and I13 couple a state $o$ of $\Psi$ to a chirality component $f$ of a Standard-Model fermion through the overlaps of the contact
interaction written above, with $G_{\mathrm{V}} = c_{\mathrm{V}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$, $G_{\mathrm{A}} =
c_{\mathrm{A}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$, $q_f$ the $B - L$ charge and $q^B_f = \frac13$ for quarks and 0 for leptons;
I13 acts on the lower component only, because $\gamma^{x_0} = \sigma_3$ in the block form. The overlaps (DERIVED; $H = 1$, 80
basis functions per sector):

| zero mode $f$ | $Q$ | $\ell$ | $u_R$ | $c_R$ | $t_R$ | $d_R$ | $s_R$ | $b_R$ | $e_R$ | $\mu_R$ | $\tau_R$ | $\nu_{Ri}$ |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| $\tilde I$, dark matter | 8.2722 | 1.2524 | 0.3854 | 0.6056 | 8.2722 | 0.3961 | 0.4620 | 0.7622 | 0.3972 | 0.5879 | 1.2524 | 0.302-0.308 |
| $\tilde I^{(b)}$, dark matter | 2.6135 | 0.9134 | 0.3795 | 0.5569 | 2.6135 | 0.3891 | 0.4459 | 0.6607 | 0.3900 | 0.5442 | 0.9134 | 0.301-0.308 |
| $\tilde I$, fold band | 6.685 | 1.659 | 0.792 | 1.060 | 6.685 | 0.807 | 0.893 | 1.221 | 0.808 | 1.041 | 1.659 | 0.668-0.678 |
| $\tilde I$, first even bulk level | 8.92 | 1.185 | 0.428 | 0.602 | 8.92 | 0.437 | 0.488 | 0.733 | 0.438 | 0.588 | 1.185 | 0.359-0.365 |

($\tilde I^{(b)} = 0$ for the fold band; $\nu_{Ri}$ the three right-handed neutrinos; the right-handed top and tau share the
localisation of their doublets, $c_R = -c_L$, hence the equal overlaps.) Self-consistent Kohn-Sham states (eight fold zero modes and
eight dark-matter quanta, $\lambda = 0$) with the mean field $A_{\mathrm{mf}}\varrho_f\mathrm{e}^{-3Hy}$ on both components (I11) or on
the lower one (I13), at $A_{\mathrm{mf}} = \pm10^{-4}$, $\pm2\times10^{-4}$ with Richardson extrapolation, reproduce $\tilde I$ for $Q$,
$e_R$, $\ell$ to $3.0\times10^{-10}$ and $\tilde I^{(b)}$ for $Q$, $\ell$, $u_R$ to $2.3\times10^{-10}$; with the benchmark self-coupling
$\lambda_{\mathrm{test}}$ the response to the quark-doublet field is $8.2693$ against $8.2722$ (screening $-3.5\times10^{-4}$); under the
lepton-doublet I11 field the gap between the $k = 0$ fold zero mode and the first shell changes by $-9.3\times10^{-11}$ per unit
amplitude (the rounding level; zero in exact arithmetic) (the second order, $-0.041A_{\mathrm{mf}}^2$, is a change of the group velocity: the ratio of the shell energies at
$\lvert\vec k\rvert = 2k_{\mathrm{lat}}$ and $k_{\mathrm{lat}}$ stays $2.000000000$), and under I13 the fold levels move by at most
$1.2\times10^{-13}$ (the rounding level): the fold band stays massless and untouched by I13 (DERIVED).

### The mean fields of the Standard-Model fields

In an environment with the net densities $n_{\mathrm{p}}$, $n_{\mathrm{n}}$, $n_{\mathrm{e}}$ (unpolarised fermions, each chirality
half) and the temperature $T$, the dark-matter level moves by the shifts written above, with the benchmark strengths
$G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$, $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$, $c_{\mathrm{I12}}/\Lambda_\star^3 =
1.106\times10^{-14}$ GeV$^{-3}$ (step 9) and $\mathcal{O}_{\mathrm{DM}} = 0.7072$; the vacuum gluon condensate of the gluon field in
its geometric normalisation is $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle(0) = 4\pi^2\times0.012$ GeV$^4$ (STANDARD: $0.012$ GeV$^4$ is
the condensate of the canonically normalised field strength weighted with $\alpha_3/\pi$), and the couplings of the condensates are taken
at $\mu_{\mathrm{ren}} = 2\pi T$ from the $\overline{\mathrm{MS}}$ values at $m_{\mathrm{Z}}$ ($\sin^2\theta_{\overline{\mathrm{MS}}} =
0.23122$, $\alpha_{\mathrm{em}} = 1/127.95$). The trace anomaly is written in the signature $(+,-,-,-)$, in which the trace of the
energy-momentum tensor of a fluid is $\rho - 3p$; in the signature $(+,+,+,-)$ of UM-2 both sides change sign and the relation is
the same; likewise on shell the Proca Lagrangian of a massive vector is a total derivative in either signature. The cold
environments: the cosmic mean today (the Planck baryon density with the helium fraction $0.2457$, $\Omega_{\mathrm{DM}}h_{100}^2 =
0.120$), the Galaxy at the Sun ($n_{\mathrm{p}} = n_{\mathrm{e}} = 1$ cm$^{-3}$), the Earth (mean density $5.51$ g/cm$^3$, 48 %
protons), the centre of the Sun (150 g/cm$^3$, 66 % protons, 32 % neutrons), a white dwarf ($10^6$ g/cm$^3$ of carbon and oxygen,
equal numbers of protons and neutrons) and a neutron-star core ($0.3$ fm$^{-3}$, 10 % protons, $n_{\mathrm{e}} = n_{\mathrm{p}}$), with
the local dark-matter density $0.4$ GeV/cm$^3$ in the bound objects. In the early-Universe environments the densities are those of
the field equation written above ($\eta_{\mathrm{b}} = 6.1\times10^{-10}$, $m_{\mathrm{n}} - m_{\mathrm{p}} = 1.293$ MeV), with the
dark matter in equilibrium for $M_{\mathrm{DM}}/T < 40$ and its relic density scaled with the entropy afterwards; the freeze-out
environment is at $T = M_{\mathrm{DM}}/x_{\mathrm{f}}$ with the $x_{\mathrm{f}} = 31.23$ of step 9. Results (DERIVED):

| environment | $n_{\mathrm{p}}$ (cm$^{-3}$) | $\Delta\varepsilon_{\mathrm{I11}}$ (GeV) | $\Delta\varepsilon_{\mathrm{I13}}$ (GeV) | $\Delta\varepsilon_{\mathrm{I12}}$ (GeV) | $\Delta\varepsilon/M_{\mathrm{DM}}$ | $\Delta\ln f$ |
| ----- | --- | --- | --- | --- | --- | --- |
| cosmic mean today | $2.2\times10^{-7}$ | $3\times10^{-64}$ | $4\times10^{-57}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $7\times10^{-94}$ |
| the Galaxy at the Sun | $1$ | $1\times10^{-57}$ | $1.5\times10^{-50}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $3\times10^{-87}$ |
| the Earth ($5.51$ g/cm$^3$) | $1.6\times10^{24}$ | $4.4\times10^{-33}$ | $4.9\times10^{-26}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $1\times10^{-62}$ |
| centre of the Sun ($150$ g/cm$^3$) | $6.0\times10^{25}$ | $1.1\times10^{-31}$ | $1.3\times10^{-24}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $3\times10^{-61}$ |
| white dwarf ($10^6$ g/cm$^3$) | $3.0\times10^{29}$ | $7.9\times10^{-28}$ | $8.9\times10^{-21}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $2\times10^{-57}$ |
| neutron-star core ($0.3$ fm$^{-3}$) | $3.0\times10^{37}$ | $4.3\times10^{-19}$ | $4.4\times10^{-12}$ | $3.7\times10^{-15}$ | $1.0\times10^{-16}$ | $9\times10^{-49}$ |
| nucleosynthesis ($T = 1$ MeV) | $1.5\times10^{22}$ | $2.4\times10^{-35}$ | $2.8\times10^{-28}$ | $3.7\times10^{-15}$ | $8.4\times10^{-20}$ | $7\times10^{-60}$ |
| QCD crossover ($T = 200$ MeV) | $7.8\times10^{28}$ | $2.0\times10^{-28}$ | $2.3\times10^{-21}$ | $1.9\times10^{-15}$ | $4.4\times10^{-20}$ | $3\times10^{-48}$ |
| electroweak era ($T = 100$ GeV) | $9.7\times10^{36}$ | $2.6\times10^{-20}$ | $2.8\times10^{-13}$ | $-2.4\times10^{-6}$ | $-5.5\times10^{-11}$ | $7\times10^{-39}$ |
| dark-matter freeze-out ($T = 1.42$ TeV) | $2.8\times10^{40}$ | $7.3\times10^{-17}$ | $8.2\times10^{-10}$ | $-6.8\times10^{-2}$ | $-1.5\times10^{-6}$ | $1.1\times10^{-34}$ |

The QCD vacuum condensate dominates at low temperature ($\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle = 0.474$ GeV$^4$, half of it left
at 200 MeV); the thermal condensates dominate in the electroweak era and at the freeze-out, where the shift reaches $1.5\times10^{-6}$
of the mass ($\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle = -8.1\times10^{12}$, $\langle W^I_{\mu\nu}W^{I\mu\nu}\rangle =
-5.0\times10^{11}$, almost all from the order-$\alpha$ interaction, $\langle B_{\mu\nu}B^{\mu\nu}\rangle = -2.6\times10^{10}$ GeV$^4$; all
condensates in the geometric normalisation of the gauge fields).

### dirac16complex acting on the Standard Model

Through I12 the scalar density of the dark matter changes the gauge couplings: $\Delta\alpha_3/\alpha_3 = -1.7\times10^{-16}$ at the
freeze-out, $-1.1\times10^{-20}$ in the electroweak era, at most $-1.1\times10^{-36}$ from nucleosynthesis on, $-1.7\times10^{-60}$ in
the Galaxy today. In the $x_0$ problem of the $W$ with the kinetic function $\Upsilon = 1 + A_{\mathrm{mf}}n^{\mathrm{sc}}_{\mathrm{DM}}$
written above, first-order perturbation theory of the Sturm-Liouville problem with the exact $W$ eigenfunction and the exact
dark-matter orbital gives $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111253$, and direct shooting of the
perturbed problem agrees to $3\times10^{-11}$ (DERIVED; version 3 quoted $-0.1126$ from quadratic finite elements, whose finite
differences in the amplitude are limited by rounding). The photon and gluon zero mode keeps $\tilde m = 0$ exactly: its profile is
flat, so the kinetic function does not act on it (version 3 quoted the finite-element rounding $-2.5\times10^{-11}$). The physical amplitude is
of the size of the relative shift of the $SU(2)$ coupling, $A_{\mathrm{mf}} \sim \lvert\Delta\alpha_2/\alpha_2\rvert =
4G_{\mathrm{W}}n_{\mathrm{DM,tot}}$, which is at most the shift of the strong coupling quoted above (with universal coefficients
smaller by $g_2^2/g_3^2$): at most $1.7\times10^{-16}$ at the freeze-out, $1.1\times10^{-20}$ in the electroweak era,
$1.1\times10^{-36}$ from nucleosynthesis on and $5\times10^{-66}$ for the cosmic mean today, so the squared $W$ mass (the eigenvalue
$\tilde m_{\mathrm{W}}^2$) moves by at most $1.9\times10^{-17}$ of itself.

### Gravity: the block response to every species

The block responds to the block-averaged sources of every species with the adiabatic response written above, in which radiation
drops out; the hidden pressure is the response of the pressure to the block scale at fixed temperature, through the species of mass
$m_s(f)$ as ideal gases with their $x_0$ masses (for an ideal gas $m\,\partial p/\partial m = -(\rho - 3p)$; non-relativistic matter
gives $-\frac14\rho\,\mathrm{d}\ln m/\mathrm{d}\ln f$), the QCD plasma through $\partial p/\partial\ln\Lambda_{\mathrm{QCD}} =
-\Theta_{\mathrm{QCD}}$ and the electroweak plasma through its order-$\alpha$ pressure, with the bulk couplings scaling as
$\alpha_{\mathrm{G}}(m_{\mathrm{KK}}) \propto f^{-4}$ and $m_{\mathrm{KK}} \propto 1/f$; in the trace the QCD and electroweak plasmas
add $\Theta_{\mathrm{QCD}}$ and $\Theta_{\mathrm{G}}$. The sensitivities (DERIVED, and one loop where stated): $\mathrm{d}\ln
m_{\mathrm{e}}/\mathrm{d}\ln f = -20.5$, $\mathrm{d}\ln M_{\mathrm{DM}}/\mathrm{d}\ln f = -0.772$, and for the quarks u, d, s, c, b, t
$-18.82$, $-18.01$, $-14.90$, $-12.15$, $-10.89$, $-6.77$; through the QCD scale ($\alpha_3(m_{\mathrm{KK}}) = 0.0606$,
$\sigma_{\pi N} = 45$ MeV, $\sigma_{\mathrm{s}} = 40$ MeV; ESTIMATE, one loop) $-60.2$ ($\Lambda_{\mathrm{QCD}}^{(6)}$), $-55.6$, $-52.0$,
$-49.0$ ($\Lambda_{\mathrm{QCD}}^{(3)}$), and for the nucleon $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$, the most
block-sensitive mass of UM-2. The block moves by at most $\Delta\ln f = 1.1\times10^{-34}$, at the freeze-out, where the hot plasma has
$\bar p = 3.1\times10^{12}$ GeV$^4$ (mostly the QCD interaction measure with $\mathrm{d}\ln\Lambda_{\mathrm{QCD}}/\mathrm{d}\ln f =
-60$) and $\rho - 3p_3 = 2.2\times10^{11}$ GeV$^4$ (the nucleon mass moves by $5.3\times10^{-33}$); by $7\times10^{-39}$ in the
electroweak era; by at most $9\times10^{-49}$ from nucleosynthesis to today. The gain of the loop is at most $1.1\times10^{-33}$, so
the iteration converges after one step in every environment. (Version 3 as first written kept only the hidden pressure of
non-relativistic matter and only the $\Delta\bar p$ term of the response and found $5.6\times10^{-45}$; the conclusion is unchanged.)

**The coupled solution is therefore the stabilised background with the $x_0$ spectra and the Kohn-Sham states of steps 1 to 3,
corrected by the mean fields of this step; the corrections are computed and below $1.5\times10^{-6}$.** The I12 benchmark changes the
strong coupling by 10 % through the thermal dark-matter density only at $T = 27.4$ TeV ($M_{\mathrm{DM}}/T = 1.62$), so the coupled
effective description holds through the freeze-out and everything later (DERIVED, 16 checks with step 9).

![The coupled solution: the $x_0$ profiles that enter the overlaps (left) and the shift of the dark-matter level by the Standard-Model mean fields in the ten environments (right).](figures/fig_coupled.png)

## The check of step 8

**In its own equations.**

* *The overlaps.* Recomputed from the closed-form orbitals (the odd level, the fold zero mode, the first even level) and the
  zero-mode profiles with 2400 Gauss nodes refined at the fold, $\tilde I$, $\tilde I^{(b)}$ and $\tilde I_\lambda$ agree with the
  stored values to $3.8\times10^{-12}$, $3.5\times10^{-12}$ and $1.3\times10^{-12}$; they equal the responses of self-consistent
  Kohn-Sham levels to finite mean fields to $3.0\times10^{-10}$ (I11) and $2.3\times10^{-10}$ (I13) (DERIVED).
* *The mean fields and the block response.* Every stored shift, condensate and block response of the ten environments, recomputed
  from the stored overlaps, strengths, densities, condensates and sources, agrees to $2.0\times10^{-11}$ (relative); the vacuum
  condensate $4\pi^2\times0.012$ GeV$^4$ to $6\times10^{-13}$; the iterated and the one-step block shifts are equal (the loop gain is
  $1.1\times10^{-33}$) (DERIVED).
* *The condensate of a gauge plasma.* The Feynman-Hellmann condensate of the order-$\alpha$ pressure reproduces the trace-anomaly
  gluon condensate to $1.1\times10^{-16}$ (DERIVED).
* *The $W$ problem with the kinetic function.* The stored coefficient is reproduced by the same first-order integral on an
  independent quadrature to $3.3\times10^{-12}$, and the shooting of the perturbed problem agrees to $3.0\times10^{-11}$ (DERIVED).

**In concert with the other field equations.**

* *The Kohn-Sham equations of step 3.* The portal responses of the Kohn-Sham jobs are the overlaps of the coupled solution to
  $3.0\times10^{-12}$; the hidden pressure of the dark matter in the block response is the Kohn-Sham stress and the $x_0$ sensitivity
  to $6.1\times10^{-12}$; the dark-matter mass agrees to $8.1\times10^{-13}$ (DERIVED).
* *The relic and freeze-in couplings of step 9.* The strengths $G_{\mathrm{A}}$ and $G_{\mathrm{V}}$ implied by the stored shifts
  at the freeze-out are those of the relic and of the freeze-in to $6.7\times10^{-13}$; the I12 benchmark is that of the relic
  computation to $1.6\times10^{-12}$; the freeze-out temperature of the environment is $M_{\mathrm{DM}}/x_{\mathrm{f}}$ of the relic to
  $2.1\times10^{-12}$ (DERIVED).
* *The thermal history of step 9.* The plasma energy density at the freeze-out in the block sources ($1.416139\times10^{14}$
  GeV$^4$) differs from the ideal gases of the thermal history ($1.414292\times10^{14}$ GeV$^4$) by $1.3\times10^{-3}$, by design: the
  block sources add the trace anomaly of the interacting plasma (of order $\alpha_3^2T^4$), which enters only $\rho - 3p_3$; the
  order-$\alpha$ interaction energy (5 %) is absent from both (DERIVED).
* *The $x_0$ problems of step 2.* The $W$ eigenvalue of the finite elements at zero amplitude, stored with the kinetic-function
  computation, is the exact eigenvalue to $2.3\times10^{-6}$ (the rounding of the matrix Rayleigh quotient), and the shooting of the
  perturbed problem at zero amplitude to $1.4\times10^{-11}$; the block sensitivities of the masses used in the hidden
  pressure equal the first-order $x_0$ mass formula to $4.5\times10^{-11}$; the response coefficients are those of step 1 to
  $2\times10^{-13}$ (DERIVED).

## The status of step 8

DERIVED: the overlaps and their Hellmann-Feynman checks, the mean-field shifts in the ten environments, the coupling shifts and the
$W$ problem, the block response to every species and the convergence of the coupled iteration. ESTIMATE: the QCD interaction measure
below 1 GeV, the electroweak condensate below $m_{\mathrm{W}}$, the one-loop QCD scale and nucleon sensitivity. STANDARD: the vacuum
gluon condensate, the trace anomaly and the leading-order plasma pressures. ASSUMED: the compositions of the environments and the
benchmark strengths (fixed in step 9). INVENTED: the portals.
