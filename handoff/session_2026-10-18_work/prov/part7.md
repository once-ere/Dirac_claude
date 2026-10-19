# The residuals of the approximate solution, and the precision fixes of version 4

## The residual analysis

The order of 2026-10-18, 15:42, asks for the approximate solution to be analysed "usually in concert with other field
equation". Version 4 adds the computation `um2_residuals.py` (outputs `residuals.json`, report `residuals-checks.json`, 52
checks). For every field equation (or system) that the solution uses, it records the solution (exact formula, numerical
method, order of the approximation); a precisely defined residual, either taken from the stored outputs or computed afresh
by substituting the stored solution into the equation; the size of the terms that the approximation drops; and the links in
concert, in which the same quantity is compared in the two or more places where different field equations use it (each
input is read where the script that uses it reads it). Every equation (res 1 to 26) and every link (res 27 to 52) has a
named check with a tolerance fixed in the script with a one-line justification; where a residual or a link is not small it
is reported as it is, and the tolerance is set by what the physics justifies. The script reads every output and writes only
its own; its linear algebra is single-threaded, so it gives the same numbers on every machine. For a root of a
transcendental condition the residual is the implied relative error (the value of the condition at the stored root divided by
the root times the derivative of the condition); for a differential equation it is the stored solution substituted into the
printed equation; for an integral it is an independent quadrature.

| | field equations | residual of the stored solution | largest neglected term |
|:----|:----------------|:---------------------------------------------|:---------------------------------------|
| res 1 | FE-38 to FE-40, FE-42, FE-43 | the static block in the printed equations: $3.9\times10^{-13}$ (the printed equations equal the code's symbolic ones) | the matter sources against the stabiliser: $3.0\times10^{-32}$ at the freeze-out, $2.4\times10^{-93}$ today |
| res 2 | FE-44 to FE-47 | the adiabatic response in the nonlinear equations: $1.4\times10^{-7}$ (second order, as expected) | second order and the inertia of the block at the freeze-out: $2.3\times10^{-32}$, $3.4\times10^{-33}$ |
| res 3 | FE-38 to FE-41 (primordial era) | constraint and one-step defect of the stored trajectories: $1.3\times10^{-11}$ | radiation of zero modes: $1.0\times10^{-6}$ of the final block |
| res 4 | FE-48, FE-49 | $\Lambda_4(K_*)$ and the $K$-derivative of the $x_4$ balance: $6.9\times10^{-13}$ | the dark energy, $\Lambda_4/H^2 \sim 10^{-92}$ (tuned, OPEN) |
| res 5 | FE-50 to FE-52, FE-55 | implied relative error of the stored eigenvalues: $5.9\times10^{-12}$ ($W$), $1.4\times10^{-12}$ ($Z$) | the I12 shift of $\tilde m_{\mathrm{W}}^2$ at the freeze-out: $1.9\times10^{-17}$; Lovelock corrections to the graviton operator OPEN |
| res 6 | FE-58 to FE-60 | implied relative root error: $5.4\times10^{-11}$ ($\nu_1$); three generations $1.2\times10^{-11}$ | mixing with the Kaluza-Klein modes, largest for the top quark: $2.0\times10^{-6}$ |
| res 7 | FE-62 | the stored levels against the closed form: $8.5\times10^{-13}$ | the shift by the Standard-Model mean fields: $1.5\times10^{-6}$ (added in the coupled solution) |
| res 8 | FE-63 to FE-68 | a state re-solved, one more Kohn-Sham map, the energy identity: $7.4\times10^{-14}\,H$ | the self-interaction at the assumed bound: $2.7\times10^{-9}\,m_\Psi$; correlation beyond the local exchange OPEN |
| res 9 | FE-67 with FE-47 | $\Delta K$ recomputed from the Kohn-Sham integrals: $1.4\times10^{-12}$ | the block-shape source $p_0 - p_5$: NOT small, up to 4.00 times $\bar p$ (OPEN) |
| res 10 | FE-70, FE-71, FE-135 | the overlaps from the closed-form orbitals: $3.8\times10^{-12}$ | screening by the interacting gas: $3.5\times10^{-4}$ at $\lambda_{\mathrm{test}}$, $7.2\times10^{-10}$ at the bound |
| res 11 | FE-72 to FE-86 | every mean field and block response recomputed: $2.0\times10^{-11}$ | the loop gain $1.1\times10^{-33}$; second order in the mean fields $2.3\times10^{-12}$ |
| res 12 | FE-79 | the first-order coefficient afresh: $3.3\times10^{-12}$ (shooting agrees) | the physical shift at the freeze-out: $1.9\times10^{-17}$ |
| res 13 | FE-55, FE-102 and the $Z$ widths | widths and $m_{\mathrm{Z}}$ recomputed: $2.7\times10^{-12}$ | electroweak loop corrections $0.41$ %; bottom-quark mass $-0.13$ %; order $\alpha_3^2$ $0.13$ % |
| res 14 | FE-89 to FE-99 | the Poisson form against the Weyl potential: $1.5\times10^{-6}$; matter-era limit $4.4\times10^{-5}$ | order $\epsilon^2$ against order $\epsilon$: $2.4\times10^{-5}$ |
| res 15 | FE-53, FE-54 | the profiles in the operator: $1.2\times10^{-12}$; Yukawa strengths $5.2\times10^{-9}$ | the Kaluza-Klein correction to Newton's law at 50 micrometres: zero in double precision |
| res 16 | FE-87, FE-88 | the first omitted order against the kept one: $2.4\times10^{-5}$ | order 2 at a neutron star: 0.030 (outside the cosmological solution) |
| res 17 | FE-103 to FE-108 | unitarity, vacuum formula, accelerator and solar probabilities: $7.1\times10^{-12}$ | non-adiabatic effects on the solar $\mathcal{P}_{ee}$: $1.3\times10^{-3}$ |
| res 18 | FE-109 | the onset condition at the stored temperatures: $8.7\times10^{-12}$ | the CP-asymmetric potential: $1.1\times10^{-2}$ of the thermal one (ESTIMATE) |
| res 19 | FE-110 to FE-115 | the instantaneous limit recomputed: $2.7\times10^{-12}$; published values within $4.6\times10^{-4}$ | electron mass and momentum dependence: $4.4\times10^{-3}$ in $N_{\mathrm{eff}}$ |
| res 20 | FE-116 to FE-119 | moments, analytic growth, homogeneous matrix: $3.3\times10^{-13}$ | the vacuum term: $9.0\times10^{-6}$ of the self-interaction |
| res 21 | FE-120 | densities, energy densities, velocities, $\Omega_\nu h_{100}^2$: $2.9\times10^{-12}$ | the non-instantaneous heating: $1.1\times10^{-2}$ in $\Omega_\nu h_{100}^2$ (included in the CMB) |
| res 22 | FE-121 to FE-123 | $g_\rho$, $g_s$ by an independent quadrature: $5.0\times10^{-9}$ | the order-$\alpha$ plasma pressure: NOT small, $-5.4$ % at the freeze-out |
| res 23 | FE-124 to FE-128 | the relic re-solved, $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060000000186$ per species; late-time identity $6.1\times10^{-9}$ | the order-$\alpha$ pressure: about $+2.7$ % in $\Omega_{\mathrm{DM}}h_{100}^2$ (ESTIMATE) |
| res 24 | FE-129, FE-130 | $\Delta N_{\mathrm{eff}}/G_{\mathrm{V}}^2$ re-integrated: $3.9\times10^{-5}$ | inverse processes: 0.012 of the Hubble rate at $T_{\mathrm{max}}$ |
| res 25 | FE-131 to FE-134 | the $\nu_R$ equation re-solved: $2.5\times10^{-12}$ | the elastic rate (ESTIMATE): $9.5\times10^{-6}$ in $\Delta N_{\mathrm{eff}}$ |
| res 26 | FE-135, FE-136 | $\Delta N_{\mathrm{eff}}/G_\lambda^2$ re-integrated: $1.1\times10^{-5}$ | inverse annihilation at the bound: 0.027 of the Hubble rate |

The 26 links in concert (the quantity, the field equations that share it, the difference):

| | quantity | shared by | difference |
|:----|:-----------------------------|:------------------------------|:---------------|
| res 27 | block averages of the Kohn-Sham states | FE-63 to FE-68, FE-45 to FE-47 | $3.4\times10^{-12}$ |
| res 28 | hidden pressure of the dark matter, $p_0/\rho = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ | FE-67, FE-62, FE-81 | $6.1\times10^{-12}$ |
| res 29 | $m_{\mathrm{Z}}$ | FE-55, the $Z$ widths | $2.0\times10^{-12}$ |
| res 30 | the weak angle and the total $Z$ width | FE-55, FE-102, the $Z$ widths | NOT zero: $8.3\times10^{-3}$ |
| res 31 | the twelve fermion masses | FE-59, FE-60, FE-121 | $3.1\times10^{-12}$ |
| res 32 | $m_1$, $m_2$, $m_3$ and the splittings | FE-60, FE-104, FE-120, FE-96, FE-109 | $5.7\times10^{-12}$ |
| res 33 | the PMNS matrix | FE-60, FE-104, FE-120 | $8.2\times10^{-13}$ |
| res 34 | $\Omega_\nu h_{100}^2$ | FE-120, FE-96 | $1.9\times10^{-5}$ |
| res 35 | $N_{\mathrm{eff}} = 3.0432 + \Delta N_{\mathrm{eff}}$ | FE-115, FE-130, FE-97 | $5.4\times10^{-16}$ |
| res 36 | $\Omega_{\mathrm{DM}}h_{100}^2$ | FE-126, FE-90 | $3.1\times10^{-9}$ |
| res 37 | the Hubble rate at the freeze-out | FE-122, FE-124, FE-49, FE-129 | NOT zero: $1.7\times10^{-4}$ |
| res 38 | $g_\rho$ today | FE-122, FE-115, FE-97 | NOT zero: $5.9\times10^{-3}$ |
| res 39 | the plasma energy density at the freeze-out | FE-121, FE-81 | NOT zero: $1.3\times10^{-3}$ |
| res 40 | the portal responses of the dark-matter level | FE-70, FE-63, FE-72 | $3.0\times10^{-12}$ |
| res 41 | $\mathcal{O}_{\mathrm{DM}}$ | FE-71, FE-124, FE-72, FE-79 | $5.7\times10^{-6}$ (4 digits coded) |
| res 42 | $c_{\mathrm{I12}}/\Lambda_\star^3$ | FE-127, FE-72 | $1.6\times10^{-12}$ |
| res 43 | $M_{\mathrm{DM}}$ | FE-62, FE-63, FE-124, FE-72 | $8.1\times10^{-13}$ |
| res 44 | $G_{\mathrm{A}}$, $G_{\mathrm{V}}$ | FE-126, FE-129, FE-72 | $6.7\times10^{-13}$ |
| res 45 | $\tilde m_{\mathrm{W}}^2$ without the kinetic function | FE-52, FE-79 | $2.3\times10^{-6}$ (finite elements) |
| res 46 | $c_\rho$, $c_3$, $c_p$ | FE-46, FE-47, FE-80 | $2.0\times10^{-13}$ |
| res 47 | the radion frequency | FE-44, FE-39, FE-53, FE-87 | NOT zero: $7.9\times10^{-5}$ (finite oscillation) |
| res 48 | $f_*$ | FE-43, FE-52, FE-59, FE-62, FE-63 | $2.2\times10^{-12}$ |
| res 49 | the heating factor $F_{\mathrm{h}}$ | FE-115, FE-133 | $5.8\times10^{-7}$ (4 digits coded) |
| res 50 | $\Phi_{\mathrm{rms}}$, $\Delta\ln f$, $m_{\mathrm{KK}}$, $\sigma_8$ | FE-87, FE-53, FE-98, FE-80 | $4.7\times10^{-12}$ |
| res 51 | the freeze-out temperature | FE-126, FE-86, FE-136 | $2.1\times10^{-12}$ |
| res 52 | the block sensitivities of the masses | FE-85, FE-83, FE-84 | $4.5\times10^{-11}$ |

Every residual lies within its tolerance and every check passes. The radion frequency (res 47) differs because the nonlinear
value is measured from the zero crossings of a finite oscillation (relative amplitude $3\times10^{-3}$); the other links that
are not zero are findings, stated next.

## The findings that are not small

**1. The weak angle has two values.** The $x_0$ problem of $W^\pm$ and $Z$ fixes the angle of the couplings with the measured
electroweak parameter,

@@FE-55@@

so that $\sin^2\theta_{\mathrm{W}} = 1 - 0.776368 = 0.223632$ (on shell); this angle also enters the tip condition of the $Z$
(FE-51), the $Z$ part of the electroweak condensates (FE-78) and the tree-level couplings

@@FE-102@@

while the $Z$ widths, the running couplings (FE-77) and the couplings of the I12 benchmark use the measured
$\overline{\mathrm{MS}}$ value $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ in the tree-level partial widths of the $Z$ into
massless fermions (with the factor $1 + \alpha_3/\pi$ for the hadronic widths),

$$
\Gamma_{\mathrm{Z}}^f = \frac{N_{\mathrm{col}}\,G_{\mathrm{F}}\,m_{\mathrm{Z}}^3}{6\sqrt2\,\pi}
 \Big[\big(T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\overline{\mathrm{MS}}}\big)^2 + \big(T_3^f\big)^2\Big]
$$

<!-- symbols: sol_GammaZ, if, sol_Ncol, GF, mZ, pi, T3, Qem, thetaMS -->

With the on-shell angle (and the $m_{\mathrm{Z}}$ of the $x_0$ problem) the total width would be 2505.73 MeV instead of 2485.23
MeV: $0.83$ % (0.82 % at tree level without the QCD factor, check `Z_width_scheme`). The difference is a scheme ambiguity of a
tree-level angle, of the size of the electroweak loop corrections that UM-2 does not compute (the measured total width is
0.41 % above the computed one); the status of the widths (a tree-level comparison) is unchanged.

**2. The Hubble rate of the thermal history leaves out the fold bands.** The Boltzmann equation of the dark matter uses the
Hubble rate of the thermal history,

@@FE-122@@

whose $g_\rho$ counts the species of the Standard Model in equilibrium but not the fold bands produced by freeze-in. At the
freeze-out ($T = 1.42$ TeV) the fold bands carry $3.48\times10^{-4}$ of the energy density, so the four-dimensional Friedmann
equation with all species gives a Hubble rate larger by $1.7\times10^{-4}$; since the relic abundance is about proportional to
the Hubble rate at the freeze-out, it moves by about the same relative amount, about a factor 60 below the 1 % precision of the
measured $\Omega_{\mathrm{DM}}h_{100}^2$. The dark matter itself carries $1.1\times10^{-2}$ of the energy density at the start
of the Boltzmann integration ($x = 5$), where its abundance is the equilibrium one, and $7\times10^{-12}$ at the freeze-out.

**3. The thermal history decouples the neutrinos instantaneously.** Below 2 MeV the thermal history uses

@@FE-123@@

which gives $N_{\mathrm{eff}} = 3$ and $g_\rho = 3.362644$ today, while the CMB computation uses
$N_{\mathrm{eff}} = 3.0432 + 0.0010 = 3.0442$ from the decoupling equations with the precision value,

@@FE-115@@

and so $g_\rho = 3.382720$ today: 0.59 %. Below 2 MeV the thermal history enters only the entropy density today ($g_s = 43/11$,
the standard value) and the environment of nucleosynthesis (effects below $10^{-58}$), so the difference has no effect on a
result.

**4. The plasma energy density differs by 0.13 % between the thermal history and the block sources, by design.** The thermal
history sums the ideal gases with the $x_0$ masses,

@@FE-121@@

($1.414292\times10^{14}$ GeV$^4$ with the equilibrium dark matter at the freeze-out), while the sources of the block response in
the coupled solution add the trace anomaly of the interacting plasma, the QCD interaction measure

@@FE-75@@

and the electroweak trace ($1.416139\times10^{14}$ GeV$^4$). The trace anomaly enters only $\rho - 3p_3$, which is what the block
responds to.

**5. The order-$\alpha$ pressure of the plasma is not in the thermal history.** The interaction part of the pressure of a gauge
plasma,

@@FE-76@@

is $-5.4$ % of the ideal-gas pressure at the freeze-out (QCD $-4.7$ %, SU(2) $-0.7$ %, U(1)$_Y$ $-0.10$ %). The coupled solution
uses it for the condensates, but the ideal-gas thermal history, and so the Hubble rate and the entropy density of the
Boltzmann equation, leave it out: with it $\Omega_{\mathrm{DM}}h_{100}^2$ would rise by about 2.7 % at fixed strength, and the
strength $G_{\mathrm{A}}$ that gives the measured relic by about 1.4 % (ESTIMATE). The physics accuracy of
$G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ is therefore about 1 %, not the $10^{-6}$ of its root finding (a precision
statement made in version 4; the value is unchanged).

**6. The block-shape source, quantified.** The order-0 metric has one block scale, so the block responds only to the hidden
pressure averaged over the block,

@@FE-2@@

through the adiabatic response

@@FE-47@@

while the difference $p_0 - p_5$ would drive a change of the shape of the block that the order-0 metric cannot describe (OPEN
since version 3, corrections item 14). For a Kohn-Sham state

@@FE-67@@

and for dark matter at rest without self-interaction ($e_{\mathrm{int}} = 0$, so $p_5 = 0$ and $\bar p = p_0/4$) the neglected
source is 4.00 times the kept one; for the self-interacting test states it is 0.90 times. Its absolute size is suppressed like
that of $\bar p$ ($\kappa p/\kappa\rho_{\mathrm{stab}} \le 3\times10^{-32}$ at the freeze-out), provided the shape mode is
stable, which remains OPEN.

**A rounding note.** The response of the four-dimensional cosmological term to a shift of the block vanishes at the stabilised
block,

$$
\frac{\mathrm{d}}{\mathrm{d}K}\Big[6H^2K\big(1 - 2w_{(2)}K\big) + \kappa\rho_{\mathrm{stab}}\Big]\Big\vert_{K = K_*} = 0
$$

<!-- symbols: diff, Kblock, Hconst, wL, kappa, rhostab, Kstar -->

exactly (with $\kappa\rho_{\mathrm{stab}}$ proportional to $K^4$); the stored value $-6.3\times10^{-12}$ (`ks/feedback.json`, check
`friedmann_decoupled_from_block_shift`) is the rounding of the 12-digit $K_*$ and $\kappa\rho_{\mathrm{stab}}(f_*)$.

## The precision fixes of version 4 (commit `cc2d514`)

The residual analysis found five places where a stored number was limited by the numerics, not by the physics. Each was
fixed and the affected scripts rerun; every script exits with code 0 with all its checks.

**1. The response of the $W$ eigenvalue to the dark matter, by first-order perturbation theory.** Through I12 the scalar
density of the dark matter changes the gauge kinetic term along $x_0$:

@@FE-79@@

With the weight $\Upsilon\,\mathrm{e}^{3HL\xi}$ on both sides, the eigenvalue is a Rayleigh quotient whose tip term does not
depend on $A_{\mathrm{mf}}$, so its derivative at $A_{\mathrm{mf}} = 0$ is, exactly,

$$
\frac{\mathrm{d}\tilde m^2}{\mathrm{d}A_{\mathrm{mf}}}\bigg\vert_{A_{\mathrm{mf}} = 0}
 = \frac{\displaystyle\int_{-1}^{0}n^{\mathrm{sc}}_{\mathrm{DM}}\,\mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2\mathrm{d}\xi
 - \tilde m^2\int_{-1}^{0}n^{\mathrm{sc}}_{\mathrm{DM}}\,\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}
 {\displaystyle\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}
$$

<!-- symbols: diff, mtilde, Amf, nscDM, euler, Hconst, Lcut, xi, Fprof -->

evaluated with the exact $W$ eigenfunction of the fold condition (its tip condition holds with the stored $\tilde m_{\mathrm{W}}^2$
to $6\times10^{-12}$)

$$
\begin{aligned}
&F(\xi) = \mathrm{e}^{-3HL\xi/2}\Big(\cosh\varkappa_{\mathrm{W}}\xi + \frac{3HL}{2\varkappa_{\mathrm{W}}}\sinh\varkappa_{\mathrm{W}}\xi\Big),
\qquad \frac{\mathrm{d}F}{\mathrm{d}\xi} = -\frac{\tilde m_{\mathrm{W}}^2}{\varkappa_{\mathrm{W}}}\,\mathrm{e}^{-3HL\xi/2}\sinh\varkappa_{\mathrm{W}}\xi,\\
&\varkappa_{\mathrm{W}} = \Big(\frac{9H^2L^2}{4} - \tilde m_{\mathrm{W}}^2\Big)^{1/2}
\end{aligned}
$$

<!-- symbols: Fprof, euler, Hconst, Lcut, xi, prov_varkappaW, diff, mtildeW -->

and the dark-matter orbital on the 800 Gauss nodes of the Kohn-Sham cell. Result:
$\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111252909326$ (`coupled.json`, key
`WZ_kinetic_shift/dlnLambdaW_damp`), confirmed by shooting the perturbed problem (DOP853, Richardson in the amplitude) to
$3\times10^{-11}$. Version 3 quoted $-0.1126$ from finite differences of finite-element eigenvalues, which are dominated by
rounding. For the photon and the gluons the flat profile $F = 1$ solves the problem for every $\Upsilon$, so their eigenvalue
stays exactly zero (version 3: $-2.5\times10^{-11}$, rounding). The physical shift stays negligible: at the freeze-out, where
the amplitude is largest ($A_{\mathrm{mf}} = 1.7\times10^{-16}$), $\tilde m_{\mathrm{W}}^2$ moves by $1.9\times10^{-17}$ of itself.

**2. A robust integration of the right-handed neutrinos of the $B - L$ alternative.** The counterfactual of FE-131,

@@FE-131@@

is integrated for the abundance $n_{\nu_R}/s$ from zero at $x = 2$. The equilibration from zero takes only about
$7\times10^{-11}$ in $x$ (the equilibrium abundance divided by its initial rate of growth); to resolve its start the error
control of the Radau method needs steps of about $7\times10^{-11}$ times the square root of the relative tolerance
($7\times10^{-15}$ at the version-3 tolerance $10^{-8}$), at or below the smallest step it allows at $x = 2$ (ten times the
spacing of the floating-point numbers, $4.4\times10^{-15}$), so the integration in $x$ could stop at its first step depending on
the last digits of the inputs. It now runs in the shifted variable $x - 2$ (from 0 to
38), where the steps are free, with a relative tolerance of $10^{-13}$: $n_{\nu_R}/n_{\nu_R}^{\mathrm{eq}} = 0.999697681992$ at
$x = 40$ (`coupled.json`, `I13_B_minus_L_alternative/Y_nuR_over_Yeq_at_x40`), stable to $3\times10^{-13}$ when the coupling is
changed by $\pm10^{-12}$ (check `R_right_handed_neutrino_boltzmann`). The version-3 statement (0.9997 of equilibrium,
$\Delta N_{\mathrm{eff}} = 0.144$) is unchanged.

**3. The integrals of the cosmic neutrino background to $3\times10^{-16}$.** The integrals of

@@FE-120@@

are of order $T_\nu^4 \approx 10^{-15}$ eV$^4$, far below the default absolute tolerance of the adaptive quadrature, which
therefore stopped at a relative error of $5.8\times10^{-7}$; with a relative tolerance only they are accurate to
$3\times10^{-16}$: $\Omega_\nu h_{100}^2 = 6.38217282098\times10^{-4}$; mean velocities 0.435132624815, 0.0604083086104,
0.0105351736626; energy densities $9.95804523965\times10^{-16}$, $7.51619688306\times10^{-15}$,
$4.31573842483\times10^{-14}$ eV$^4$ (`neutrino.json`, `CNB`, copied in `cosmology.json`). Every number quoted in version 3 is
unchanged at its quoted precision.

**4. Deterministic thread counts in the Kohn-Sham scripts.** The number of threads of the linear algebra (BLAS, LAPACK,
OpenMP) is now fixed to one in `um2_kohnsham.py`, `um2_ks_jobs.py`, `um2_coupled.py` and `um2_residuals.py`, before numpy is
imported: with two threads the energy of the 8-particle state with $\lambda_{\mathrm{test}}$ had differed by $5\times10^{-13}\,H$,
and the fresh-clone runs of versions 1 to 3 had found one Kohn-Sham integral differing by $1.1\times10^{-12}$ relative because
threaded sums are not taken in a fixed order. The rerun changed only quantities at the rounding level, among them quantities
that are zero in exact arithmetic: the changes of the fold-band gap per unit amplitude, $7.9\times10^{-11}$ (electron density),
$3.0\times10^{-9}$ (up-quark density), $-9.3\times10^{-11}$ (neutrino density), $-1.4\times10^{-10}$ (gluon condensate) and
$1.2\times10^{-13}$ (the I13 shift of the fold band); and the observed order of the Kohn-Sham energy of the stress state, now
4.956 (version 3: 4.95).

**5. A stale check text.** The text of the check `tip_Z_portal_dropped` of `um2_electroweak.py` still said "$c_{\mathrm{V}} = 0$
for I11" (version 2); it now states that I11 is kept with the freeze-in strength $G_{\mathrm{V}} = 4.38\times10^{-17}$
GeV$^{-2}$, at which the fold bands are produced only by freeze-in ($\Delta N_{\mathrm{eff}} = 0.001$). No number changed.

## What changed in the claims

No claim of version 3 changes; the status labels are those of version 3, and the conflicts with data stand (no Higgs boson;
the unitarity of $W^+W^-$ scattering near 1.2 TeV). Numbers changed by the precision fixes:
$\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.11125$ (was $-0.1126$), the photon's value exactly zero (was
$-2.5\times10^{-11}$), the observed order 4.96 (was 4.95), the rounding-level values listed in fix 4, and further digits of the
CNB. Statements made precise by the residual analysis: the two values of the weak angle and their 0.83 % effect on the
$Z$ width; the physics accuracy of about 1 % of $G_{\mathrm{A}}$; the block-shape source, now quantified (OPEN); the fold
bands missing from the Hubble rate of the thermal history ($1.7\times10^{-4}$); the instantaneous neutrino decoupling of the
thermal history (0.59 % in $g_\rho$ today, without effect on a result).

