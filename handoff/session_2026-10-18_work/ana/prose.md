---
title: "UM-2 analysis"
subtitle: "The $x_0$ mass mechanism, and the validity of associating dark matter and dark energy with the dirac16complex field"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Analysis, version 4, 2026-10-18 (versions 1 to 3: 2026-10-17 and 2026-10-18)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document {-}

**What it contains.** On 2026-10-18 the author ordered two analyses of the universe model UM-2: "analyze the $x_0$ mass
mechanism, and ... analyze the validity of associating dark matter (and dark energy) with dirac16complex". This document
carries out both. Part A analyses the mechanism by which every non-massless particle receives its mass from the dependence
of its wave function on the hidden space coordinate $x_0$, periodic with the period $\pi/(6H)$, with the uncertainty relation
as its physical reason; it states the author's argument as equations, shows what it gives quantitatively and where it
fails, writes out the exact $x_0$ eigenvalue equations of every field, and explains the hierarchy of the masses, the
mixing matrices and the massless zero modes. Part B analyses dirac16complex as dark matter (the candidate, the portals
that produce it, its relic density from the Boltzmann equation, its detection, the bound on its self-interaction and the
cosmological tests) and as dark energy (why this association is not supported). The last two sections collect the
conditions, the open problems, the conflicts with data and the closing assessment.

**Version 4.** Version 4 (2026-10-18) re-presents version 3. The physics and the numbers are those of version 3, taken
from the current outputs of the computations of the repository (after the precision fixes of the commit of 2026-10-18 that
added the residual analysis of the solution: 287 checks in all), with the results of that residual analysis where they
concern this document. What is new is the presentation, ordered by the author: every equation that is used is written out
here, every field equation and interaction term with the tag of the inventory of the field equations of UM-2, (FE-$n$) or
(IN-$n$), and every display equation is followed by the list of all of its symbols with their meanings, units, values and
status. A symbol has one meaning throughout (the notation of version 4: for example $\tilde m^2$ is the dimensionless boson
eigenvalue, $\tilde\varepsilon$ the dimensionless fermion eigenvalue, $K = 1/f^2$ the block variable, $\mathcal{H}$ the
Hubble rate and $H$ always the author's constant). The reader never needs another document: every equation, definition
and argument used is in this one. The repository files that hold the computations are named only for reproduction.
Besides the re-presentation, two elementary consequences of version-3 results are made explicit (the lower bound that the
uncertainty relation sets on a localised state, never below 11.05 TeV, and the asymptotic sensitivity of a zero-mode mass to its
localisation), the trace anomaly of the direct-detection estimate is written in the geometric normalisation of the gluon field
(the number is unchanged), and the accuracy statements of the residual analysis are added.

**Status labels.** AUTHOR (the author's notebooks and orders), RECORD (the Revision record of this repository), STANDARD
(textbook physics or a measured value), ASSUMED (a choice made in UM-2), INVENTED (a new interaction or structure of UM-2),
DERIVED (computed and verified in UM-2; the verification is stated), ESTIMATE (an order-of-magnitude evaluation), OPEN (not
solved). A measured bound that is quoted from memory, not re-read from its source, is marked FROM MEMORY, as in version 3.

**Units and conventions.** Natural units $\hbar = c = 1$ (the reduced Planck constant $\hbar$ is shown where the author's
relations contain it). The coordinates are the author's $X = \{x_0, x_1, \dots, x_7\}$, the hidden direction first: $x_0$
the hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times. $W^+$
carries the electric charge $+e$ and $W^-$ the charge $-e$. UM-2 contains no Higgs particle: the tip sigma field gives the
$W^\pm$ and $Z$ masses. A derivative with respect to $\xi$ is always written $\mathrm{d}/\mathrm{d}\xi$, a dot is
$\mathrm{d}/\mathrm{d}x_4$, and $\Delta$ is a change, a difference or (in an uncertainty relation) the root-mean-square
spread of the quantity that follows.

**Where the numbers come from.** The scripts in the folder `code` of `universe_model_2` write the outputs in the folder
`outputs`, with named checks in the folder `reports`: `analysis.json` (the uncertainty analysis, the sensitivities, the
condensate), `masses.json`, `flavour.json` and `series.json` (the $x_0$ spectra and the Kaluza-Klein tower), `thermal.json` and
`coupled.json` (the thermal history, the relic, the portals, the coupled solution), `neutrino.json` and `cosmology.json` (the
neutrinos, $N_{\mathrm{eff}}$, the CMB) and `residuals.json` (the residuals of the solution in every field equation and in
concert).

**Summary of the verdicts.**

| question | verdict |
| ------------ | ------------------------------------------------------------ |
| Can every mass come from the $x_0$ dependence of wave functions periodic with period $\pi/(6H)$? | YES (DERIVED): every four-dimensional mass of UM-2 ($W^\pm$, $Z$, the twelve fermions of three generations, the dark matter, the Kaluza-Klein modes) is an eigenvalue of an $x_0$ operator; the graviton, the photon, the gluons and the fold bands of dirac16complex are exactly massless |
| Is the uncertainty relation the reason for the masses? | ONLY FOR THE HEAVY STATES: the uncertainty estimate $m_{\mathrm{Heis}}$ lies below the masses of the computed Kaluza-Klein and odd excitations and of the dark matter (by factors 2.3 to 7.5), but the light masses ($W^\pm$, $Z$ and all twelve fermions) lie $3.2\times10^{-3}$ (top quark) to $1.1\times10^{-17}$ (lightest neutrino) below it and come from the tip of the $x_0$ cell |
| Why must the light fermions be zero modes? | The hidden kinetic energy of any profile that is negligible at the tip is at least that of a mass $m_{\mathrm{Heis}} \ge 1/(2fL) = 11$ TeV (DERIVED); a mass of 173 GeV or less needs an exact cancellation of it by the other terms of the $x_0$ operator, which happens only for the zero modes of that operator; their mass is then the small mixing of two chiral zero modes at the tip |
| Are the neutrino masses and their mixing $x_0$ effects? | YES for the masses, NO for the mixing angles: the three neutrino masses are $x_0$ eigenvalues (the most block-sensitive of all eigenvalues), the PMNS matrix is the tip matrix $\mathcal{K}_\nu$, an input; given both, the flavour conversion follows |
| Do the extra times deflate to irrelevance? | IN THE PRIMORDIAL ERA, then FROZEN: they deflate by up to a factor 2.9 into the stabilised block; a continuing deflation is excluded because every mass and coupling depends on the block size |
| Is dirac16complex dark matter? | YES, CONDITIONALLY: the lightest odd quanta of its two halves $\Psi_A$ and $\Psi_B$ (two degenerate Dirac fermions of 44.35 TeV) are cold, neutral and stable (DERIVED, conditional); the gauge-kinetic portal I12 alone cannot produce their relic abundance within perturbative unitarity, but with the s-wave portal I13 (INVENTED) they freeze out with $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ each (physics accuracy of the needed coupling about 1 %), and their scattering on xenon is 0.16 of the present LZ limit (testable); the massless fold bands are radiation ($\Delta N_{\mathrm{eff}} = 0.001$ by freeze-in), not dark matter |
| Is dirac16complex dark energy? | NOT SUPPORTED: no positive-energy state has a negative equation of state; a negative-coupling condensate runs away; the dark energy of UM-2 is a tuned four-dimensional cosmological term |
| Does the $x_0$ mechanism fix the nucleon mass? | INDIRECTLY: the nucleon mass is QCD binding energy, proportional to $\Lambda_{\mathrm{QCD}}$, which is set by the gauge coupling at the Kaluza-Klein scale, itself an $x_0$ quantity; $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$ makes it the most block-sensitive mass of UM-2 |

# A. The $x_0$ mass mechanism {-}

## A.1 The periodic hidden coordinate, the fold and the tip {-}

The hidden coordinate enters the metric through the angle variable $z = 6Hx_0$. The order-0 metric of UM-2, the first term
of the power series of the metric, is in the author's coordinates (AUTHOR)

$$
\begin{aligned}
\bar g = \mathrm{diag}\Big(&\mathrm{e}^{-2a_4}b_4\cot^2z,\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ 
 \mathrm{e}^{2a_4},\ -1,\\
&-\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(
 \sin^2z)^{1/6}\Big),
 \qquad z = 6Hx_0
\end{aligned} \tag{FE-31}
$$
<!-- symbols: gbar, diag, euler, a4, b4, zvar, Hconst, x0 -->

and in the chart $y$, which measures the hidden direction in proper units of the block, with the block scale $f$ and the
rates of the background (DERIVED)

$$
\begin{aligned}
&y = \frac{\ln\lvert\sin z\rvert}{6H},\qquad \mathrm{d}y = \cot z\,\mathrm{d}x_0,\qquad \xi =
 \frac{y}{L}\in[-1, 0],\\
&\bar g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 +
 \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 + f^2\Big[\mathrm{d}y^2 - \mathrm{e}^{2Hy}\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 +
 \mathrm{d}x_7^2\big)\Big],\\
&f = \mathrm{e}^{-a_4}b_4^{1/2},\qquad K = \frac{1}{f^2},\qquad \mathcal{H} = \dot a_4,\qquad
 \mathcal{H}_f = \frac{\dot f}{f} = \frac{\dot b_4}{2b_4} - \dot a_4,\qquad \dot K = -2K\mathcal{H}_f,\\
&\sqrt{\lvert\bar g\rvert} = \mathrm{e}^{3a_4}f^4\lvert\cot z\rvert(\sin^2z)^{1/4}
 = \mathrm{e}^{3a_4}f^4\,\mathrm{e}^{3Hy}\Big\lvert\frac{\mathrm{d}y}{\mathrm{d}x_0}\Big\rvert
\end{aligned} \tag{FE-32}
$$
<!-- symbols: ycoord, zvar, Hconst, diff, x0, xi, Lcut, gbar, iM, iN, Xcoord, euler, a4, x1, x2, x3, x4, fblock, x5, x6, x7, b4, Kblock, Hubble, a4dot, Hf, fdot, b4dot, Kdot -->

One period $0 < z < \pi$ of $x_0$, of coordinate length $\pi/(6H) = 3.663\times10^{-5}$ GeV$^{-1}$ $= 7.23\times10^{-21}$ m,
consists of two halves joined at the fold $y = 0$ ($z = \pi/2$); each half ends at a tip ($y \to -\infty$), which UM-2 replaces
by a regular cutoff at $y = -L$ with $HL = 3$ (ASSUMED). Every function of $y(z)$ is periodic in $x_0$ with the period
$\pi/(6H)$, and so is every wave function of UM-2: the author's periodicity requirement is built into the geometry. On the
stabilised block, $f = f_* = 0.215556$, the proper depth of one half is $fL = 8.926\times10^{-21}$ m, i.e.
$1/(fL) = 22.11$ TeV (DERIVED).

## A.2 The author's argument in equations {-}

The author's order of 2026-10-18 gives the reason for the masses in three steps (AUTHOR). First, a particle whose wave
function is localised with respect to $x_0$ obeys the uncertainty relation for the coordinate $x_0$ and the component
$k_{x_0}$ of its momentum along $x_0$ (with $\hbar = 1$ the momentum and the wave number coincide):

$$ \Delta x_0\,\Delta k_{x_0} \ge \frac{\hbar}{2} $$
<!-- symbols: Delta, x0, ana_kx0, ana_hbar -->

Second, the momentum may be thought of as proportional to the mass, and the kinetic energy as proportional to the momentum
squared divided by the mass:

$$ k_{x_0} \propto m_{\mathrm{eff}},\qquad E_{\mathrm{kin}} \propto \frac{k_{x_0}^2}{m_{\mathrm{eff}}} $$
<!-- symbols: ana_kx0, ana_meff, ana_Ekin -->

Third, hence every particle whose wave function depends on $x_0$, periodically with the period $\pi/(6H)$, has an
effective mass, of the order of the momentum spread that its localisation forces (up to factors of order one, in natural
units):

$$ m_{\mathrm{eff}} \sim \Delta k_{x_0} \ge \frac{\hbar}{2\Delta x_0} $$
<!-- symbols: ana_meff, Delta, ana_kx0, ana_hbar, x0 -->

This holds, the author states, for all particles except the graviton, the photon and perhaps the quanta of dirac16complex.
The coordinate $x_0$ is not a proper length (its proper element $f\cot z\,\mathrm{d}x_0$ vanishes at the fold and diverges at
the tips; section A.6), so version 3 applied the argument to the proper hidden length $fy$, the proper distance from the fold,
and defined the author's estimate of the mass of a state as (DERIVED from the AUTHOR argument)

$$ m_{\mathrm{Heis}} = \frac{\hbar}{2\Delta(fy)},\qquad \Delta(fy) = fL\,\Delta\xi,\qquad \Delta\xi^2 = \int_{-1}^{0}\xi^2\varrho_\xi\,\mathrm{d}\xi $$
<!-- symbols: ana_mHeis, ana_hbar, Delta, fblock, ycoord, Lcut, xi, ana_varrhoxi, diff -->

where $\Delta(fy)$ is the root-mean-square proper distance from the fold and $\varrho_\xi$ the probability density of the state
in $\xi$ on one half of the period, in the measure in which the hidden kinetic energy is a plain $\int(\mathrm{d}/\mathrm{d}\xi)^2$:

$$ \varrho_\xi = \frac{\tilde F^2}{\int_{-1}^{0}\tilde F^2\,\mathrm{d}\xi}\ \ (\text{boson},\ F = \mathrm{e}^{-3HL\xi/2}\tilde F),\qquad \varrho_\xi = \frac{\chi^\dagger\chi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi}\ \ (\text{fermion}) $$
<!-- symbols: ana_varrhoxi, Ftilde, diff, xi, Fprof, euler, Hconst, Lcut, chi, dagger -->

Over the full period the density is symmetric about the fold, so $\Delta\xi$ is also the spread of the full-period profile.
The argument is a heuristic. UM-2 tests it in two steps: every mass is computed exactly as an eigenvalue of the $x_0$
operator of its field (section A.3), and each eigenvalue is split exactly into the hidden kinetic energy, which the
uncertainty relation bounds, and the remaining terms of the operator, which it does not (section A.4).

## A.3 Every mass is an $x_0$ eigenvalue: the exact equations {-}

### Gauge bosons and the graviton (DERIVED) {-}

A four-dimensional component of a gauge field with the $x_0$ profile $F$ (in the gauge where the $y$ component of the field
vanishes), and equally the transverse-traceless graviton, obeys on the static block the $x_0$ eigenvalue equation

$$
\begin{aligned}
&\int_{-L}^{0}\mathrm{d}y\,f^4\mathrm{e}^{3Hy}\Big[\frac{(\partial_yF)^2}{f^2} -
 m^2F^2\Big]\ \text{stationary}:\qquad
 -\frac{1}{f^2}\,\mathrm{e}^{-3Hy}\,\partial_y\big(\mathrm{e}^{3Hy}\,\partial_yF\big) = m^2F,\\
&\Leftrightarrow\qquad
 -\mathrm{e}^{-3HL\xi}\,\frac{\mathrm{d}}{\mathrm{d}\xi}\Big(\mathrm{e}^{3HL\xi}\,\frac{\mathrm{d}F}{
 \mathrm{d}\xi}\Big)
 = \tilde m^2F,\qquad \tilde m = m\,fL
\end{aligned} \tag{FE-50}
$$
<!-- symbols: Lcut, diff, ycoord, fblock, euler, Hconst, partial, iy, Fprof, mmass, xi, mtilde -->

with the conditions at the fold and at the tip

$$
\begin{aligned}
&\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=0} = 0\ \ \text{(even)}\quad\text{or}\quad F(0) =
 0\ \ \text{(odd)},\qquad
 \frac{\mathrm{d}F}{\mathrm{d}\xi}\Big\vert_{\xi=-1} = \beta\,F(-1),\\
&\beta = 0\ \ (\text{photon, gluons, graviton}),\qquad \beta = \beta_{\mathrm{W}}\ \ (W^\pm),\qquad
 \beta = \beta_{\mathrm{Z}} = \frac{\beta_{\mathrm{W}}}{\cos^2\theta_{\mathrm{W}}}\ \ (Z)
\end{aligned} \tag{FE-51}
$$
<!-- symbols: diff, Fprof, xi, betaRobin, betaW, Wpm, betaZ, thetaW, Zboson -->

The tip condition is the natural boundary condition of the tip mass term of the sigma field: $\beta = 0$ for the photon, the
gluons and the graviton, $\beta_{\mathrm{W}}$ for $W^+$ and $W^-$ (one value for both: they are particle and antiparticle), and
$\beta_{\mathrm{Z}}$ for the $Z$. With the rescaled profile $\tilde F$ the solutions are elementary and the eigenvalue
conditions are

$$
\begin{aligned}
&F = \mathrm{e}^{-3HL\xi/2}\,\tilde F,\qquad \varpi^2 = \tilde m^2 - \frac{9H^2L^2}{4}:\\
&\text{even: }\Big[\varpi^2 + \frac{3HL}{2}\Big(\beta + \frac{3HL}{2}\Big)\Big]\sin\varpi -
 \beta\,\varpi\cos\varpi = 0,\qquad
 \text{odd: }\varpi\cos\varpi + \Big(\beta + \frac{3HL}{2}\Big)\sin\varpi = 0;\\
&\beta = 0:\quad \tilde m = 0\ \text{(flat profile)},\qquad \tilde m_n^2 = \frac{9H^2L^2}{4} +
 \varpi_n^2\ \text{(even)},\qquad
 \varpi\cot\varpi = -\frac{3HL}{2}\ \text{(odd)}
\end{aligned} \tag{FE-52}
$$
<!-- symbols: Fprof, euler, Hconst, Lcut, xi, Ftilde, varpi, mtilde, betaRobin, in -->

For $\beta = 0$ the flat profile is an exact eigenfunction with $\tilde m = 0$: the graviton, the photon and the gluons are
exactly massless, protected by four-dimensional general covariance and gauge invariance. The first even level has
$\tilde m_1^2 = 30.1196$, the first odd level $\tilde m^2 = 27.0890$, and the gap of the operator is $9H^2L^2/4 = 20.25$
(finite elements agree to $5\times10^{-10}$). The $W^\pm$ and $Z$ masses fix the tip parameter and the scale:

$$
\rho_{\mathrm{EW}} = \frac{\tilde m_{\mathrm{W}}^2}{\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}}} =
 \rho_{\mathrm{EW},0},\qquad
\cos^2\theta_{\mathrm{W}} = \frac{m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2}{\rho_{\mathrm{EW},0}},\qquad
m_{\mathrm{KK}} = m_{\mathrm{W}}\,\frac{\tilde m_1}{\tilde m_{\mathrm{W}}},\qquad
m_{\mathrm{Z}} = m_{\mathrm{W}}\,\frac{\tilde m_{\mathrm{Z}}}{\tilde m_{\mathrm{W}}} \tag{FE-55}
$$
<!-- symbols: rhoEW, mtildeW, mtildeZ, thetaW, rhoEW0, mW, mZ, mKK, mtilde -->

With the measured $m_{\mathrm{W}} = 80.3625$ GeV, $m_{\mathrm{Z}} = 91.1879$ GeV and $\rho_{\mathrm{EW},0} - 1 = 0.00038$ (STANDARD) the
fit gives $\cos^2\theta_{\mathrm{W}} = 0.776368$, $\beta_{\mathrm{W}} = 0.011912$, $\beta_{\mathrm{Z}} = 0.015343$,
$\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, $\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$, $m_{\mathrm{KK}} = 121.32$ TeV and
$H = 14.296$ TeV, and both masses are reproduced (DERIVED). The residuals of the stored eigenvalues in their exact
conditions are $5.9\times10^{-12}$ ($W$) and $1.4\times10^{-12}$ ($Z$). The angle of the couplings of this $x_0$ problem,
$\sin^2\theta_{\mathrm{W}} = 0.223632$, is the on-shell value, while the widths and couplings of the electroweak sector use the
$\overline{\mathrm{MS}}$ value 0.23122; the $Z$ width moves by 0.83 % between the two, within the electroweak loop corrections that
UM-2 does not compute (residual analysis).

### The fermions of three generations (DERIVED) {-}

Every fermion of UM-2, dirac16complex included, reduces exactly to a $2\times2$ block Hamiltonian (all eight blocks, general
$a_4(x_4)$, $b_4(x_4)$, $M(y)$ and $v(y)$; checked with the author's matrices):

$$
\begin{aligned}
&\Psi = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\mathcal{V}
 \chi(y, x_4):\\
&\gamma^MD_M\Psi - \big(M(y) - \mathrm{i}v(y)\gamma^{x_4}\big)\Psi
 = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\gamma^{x_4}\mathcal{V}
 \big[\partial_{x_4}\chi + \mathrm{i}h\chi\big],\\
&h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M(y)\,\sigma_2 +
 \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y),\qquad
 \mathrm{i}\,\partial_{x_4}\chi = h\chi;\\
&\text{in each block: }\gamma^{x_0} = \sigma_3,\qquad \mathcal{B} = \varsigma\varsigma_2,\qquad
 C = \varsigma_2\sigma_2,\qquad \Gamma_4 = -\varsigma\varsigma_2\sigma_3
\end{aligned} \tag{FE-56}
$$
<!-- symbols: Psi, euler, imag, kwave, x1, Hconst, ycoord, a4, b4, calV, chi, x4, gamma, iM, Dcov, Mfun, vpot, partial, hblock, varsigma, fblock, sigmaPauli, iy, x0, calB, varsigma2, Cmat, Gamma4 -->

For a Standard-Model multiplet $M = \mu_{\psi i}$ and $v = 0$. Its chiral zero modes are

$$
\begin{aligned}
&\chi = \big(\mathrm{e}^{c\xi},\ 0\big)^T\ \ (\text{doublet},\ \Gamma_4 = +1),\qquad
 \chi = \big(0,\ \mathrm{e}^{-c\xi}\big)^T\ \ (\text{singlet},\ \Gamma_4 = -1),\qquad c = f\mu L,\\
&h\big(\mathrm{e}^{c\xi},\ 0\big)^T = \varsigma\,\mathrm{e}^{-a_4}k\big(\mathrm{e}^{c\xi},\ 0\big)^T
\end{aligned} \tag{FE-57}
$$
<!-- symbols: chi, euler, cloc, xi, transpose, Gamma4, fblock, mubulk, Lcut, hblock, varsigma, a4, kwave -->

massless four-dimensional particles with the energy $\mathrm{e}^{-a_4}\lvert k\rvert$ for every localisation $c$; a doublet zero
mode with $c_L > 0$ and a singlet zero mode with $c_R < 0$ are both localised at the fold. The tip Yukawa terms of the
sigma field are equivalent to the self-adjoint mixing conditions (the choice of the tip matrices is ASSUMED)

$$
\begin{aligned}
&\text{one generation:}\quad b_L(-L) = \mathcal{K}\,b_R(-L),\qquad a_R(-L) =
 -\mathcal{K}\,a_L(-L),\qquad \chi = (a,\ \mathrm{i}b);\\
&\text{three generations:}\quad b_L(-L) = \mathcal{K}\,b_R(-L),\qquad a_R(-L) = -\mathcal{K}^\dagger
 a_L(-L),\qquad
 \mathcal{K} \in \{\mathcal{K}_\nu, \mathcal{K}_e, \mathcal{K}_u, \mathcal{K}_d\};\\
&\text{UM-2:}\quad \mathcal{K}_e = \mathcal{K}_u = \mathbf{1},\qquad \mathcal{K}_\nu = U,\qquad
 \mathcal{K}_d = V_{\mathrm{CKM}}
\end{aligned} \tag{FE-30}
$$
<!-- symbols: ab, iL, Lcut, Ktip, iR, chi, imag, dagger, identity, Upmns, VCKM -->

At $k = 0$ the doublet and singlet solutions that satisfy the fold conditions $b(0) = 0$ (doublet) and $a(0) = 0$ (singlet)
reach the tip with

$$
\begin{aligned}
&\frac{\mathrm{d}a}{\mathrm{d}\xi} = c\,a - \tilde\varepsilon\,b,\qquad
 \frac{\mathrm{d}b}{\mathrm{d}\xi} = \tilde\varepsilon\,a - c\,b,
 \qquad \chi = (a,\ \mathrm{i}b),\qquad \tilde\varepsilon = \varepsilon fL,\qquad
 \upsilon_L = \sqrt{c_L^2 - \tilde\varepsilon^2},\qquad \upsilon_R = \sqrt{c_R^2 - \tilde\varepsilon^2},\\
&(a_L,\ b_L)\big\vert_{\xi=-1} = \Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L},
 -\tilde\varepsilon\,\frac{\sinh\upsilon_L}{\upsilon_L}\Big),\qquad
 (a_R,\ b_R)\big\vert_{\xi=-1} = \Big(\tilde\varepsilon\,\frac{\sinh\upsilon_R}{\upsilon_R},
 \cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big)
\end{aligned} \tag{FE-58}
$$
<!-- symbols: diff, ab, xi, cloc, epstilde, chi, imag, varepsilon, fblock, Lcut, upsilon, iL, iR -->

and the tip conditions give the exact mass condition of one generation and its first-order root

$$
\begin{aligned}
&\mathcal{D}(\tilde\varepsilon) =
 \tilde\varepsilon^2\,\frac{\sinh\upsilon_L}{\upsilon_L}\frac{\sinh\upsilon_R}{\upsilon_R}
 - \mathcal{K}^2\Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L}\Big)
 \Big(\cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big) = 0,\\
&\tilde\varepsilon \simeq \mathcal{K}\,\mathcal{Z}(c_L)\,\mathcal{Z}(-c_R),\qquad \mathcal{Z}(c)^2 =
 \frac{c\,\mathrm{e}^{-c}}{\sinh c}
\end{aligned} \tag{FE-59}
$$
<!-- symbols: calD, epstilde, upsilon, iL, iR, Ktip, cloc, calZ, euler -->

For three generations the conditions hold for the vectors of tip values over the generations:

$$
\begin{aligned}
&\Big[\mathrm{diag}\big(b_{L\alpha}\big) +
 \mathcal{K}\,\mathrm{diag}\Big(\frac{b_{Ri}}{a_{Ri}}\Big)\mathcal{K}^\dagger\,
 \mathrm{diag}\big(a_{L\alpha}\big)\Big]\boldsymbol{\alpha} = 0;\qquad
 \det\big[\cdots\big] = \prod_{i=1}^{3}\frac{b_La_{Ri} + a_Lb_{Ri}}{a_{Ri}},\\
&b_La_R + a_Lb_R = -\mathcal{D}(\tilde\varepsilon)\big\vert_{\mathcal{K} = 1},\qquad
 \boldsymbol{\alpha}^{(i)} = \mathcal{K}\,\mathbf{u}_i,\qquad \boldsymbol{\beta}^{(i)} \propto
 \mathbf{u}_i,\qquad
 U = \mathcal{K}_e^\dagger\mathcal{K}_\nu,\qquad V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d
\end{aligned} \tag{FE-60}
$$
<!-- symbols: diag, ab, iL, ialpha, Ktip, iR, ii, dagger, bsalpha, calD, epstilde, bfu, bsbeta, Upmns, VCKM -->

With one doublet bulk mass per sector and unitary tip matrices the determinant factorises into the one-generation conditions
with $\mathcal{K} = 1$, so every mass is a one-generation root and the left-handed rotation of a sector is its tip matrix. The
localisations that reproduce the measured masses (STANDARD targets, tree level) are the doublet localisations
$c_\ell = 5.9529$ (leptons) and $c_Q = 3.3823$ (quarks) and the singlet localisations $c_R$ (DERIVED):

| lepton | $\nu_1$ | $\nu_2$ | $\nu_3$ | electron | muon | tau |
| ---- | --- | --- | --- | --- | --- | --- |
| mass | $1.000$ meV | $8.712$ meV | $50.140$ meV | $0.511$ MeV | $105.66$ MeV | $1776.93$ MeV |
| $c_R$ | $-35.0452$ | $-32.8481$ | $-31.0702$ | $-14.5539$ | $-8.9809$ | $-5.9529$ |

| quark | up | charm | top | down | strange | bottom |
| ---- | --- | --- | --- | --- | --- | --- |
| mass | $2.16$ MeV | $1.273$ GeV | $172.56$ GeV | $4.70$ MeV | $93.5$ MeV | $4.183$ GeV |
| $c_R$ | $-15.4300$ | $-8.7683$ | $-3.3823$ | $-14.6258$ | $-11.5158$ | $-7.5005$ |

The heaviest member of each sector has $c_R = -c_L$; the lightest neutrino mass $m_1 = 1$ meV is ASSUMED, and $m_2$, $m_3$
follow from the measured splittings (section A.7). The roots of the $3\times3$ determinant agree with the one-generation roots,
both refined in the same 50-digit computation, to $3.0\times10^{-42}$; the residual of the stored masses in their exact
conditions is at most $5.4\times10^{-11}$ (for $\nu_1$; $1.2\times10^{-11}$ for the three-generation determinants) (DERIVED).

### The quanta of dirac16complex (DERIVED) {-}

dirac16complex has the same block Hamiltonian with $M = m_\Psi$ (for the free spectrum) and the boundary conditions

$$
\big(1 - \gamma^{x_0}\big)\Psi\big\vert_{y=0} = 0\ \ \text{(even)}\quad\text{or}\quad
\big(1 + \gamma^{x_0}\big)\Psi\big\vert_{y=0} = 0\ \ \text{(odd)},\qquad
\big(1 - \gamma^{x_0}\big)\Psi\big\vert_{y=-L} = 0 \tag{FE-28}
$$
<!-- symbols: gamma, x0, Psi, ycoord, Lcut -->

which in block form read

$$
\chi = (\chi_1,\ \chi_2)^T:\qquad \chi_2(0) = 0\ \ \text{(even)}\quad\text{or}\quad \chi_1(0) =
 0\ \ \text{(odd)},\qquad
\chi_2(-L) = 0 \tag{FE-69}
$$
<!-- symbols: chi, transpose, Lcut -->

Its exact spectrum at $k = 0$ is

$$
\begin{aligned}
&\text{even: }\chi = \big(\mathrm{e}^{c_\Psi\xi},\ 0\big)^T,\ \varepsilon = 0\ \text{(all eight
 blocks)},\qquad
 \varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi_n}{fL}\Big)^2},\ \varpi_n = \pi,\ 2\pi,\ \dots;\\
&\text{odd: }\varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2},\quad \tan\varpi =
 -\frac{\varpi}{c_\Psi};\qquad
 c_\Psi = f\,m_\Psi L;\qquad \text{fold band: }\varepsilon = \mathrm{e}^{-a_4}\lvert k\rvert
\end{aligned} \tag{FE-62}
$$
<!-- symbols: chi, euler, cPsi, xi, transpose, varepsilon, mPsi, varpi, in, fblock, Lcut, pi, a4, kwave -->

At the stabilised block $c_\Psi = 0.646667$: the fold band (the even zero mode, in all eight blocks) is massless, the lowest
odd level, $\varepsilon = 3.102204\,m_\Psi = 44.35$ TeV ($\varpi = 1.89901$), is the dark matter of part B, and the lowest even
bulk level is $4.959981\,m_\Psi$. The residual of the stored spectrum in its exact conditions is $8.5\times10^{-13}$.

### The masses (DERIVED) {-}

The photon, the gluons and the graviton are exactly massless (flat profile); the fold bands of dirac16complex are exactly
massless (chiral zero modes, energy $\mathrm{e}^{-a_4}\lvert k\rvert$); $W^\pm$ ($80.36$ GeV) and $Z$ ($91.19$ GeV) are reproduced; the
twelve fermions have the masses of the tables above; the dark matter has $44.35$ TeV; the Kaluza-Klein levels start at
$121.3$ TeV, and every odd mode and every excitation of the gauge fields and the graviton lies above the gap
$3H/(2f_*) = 99.48$ TeV; the excitations of dirac16complex start at its lowest odd level, $44.35$ TeV. Every one of these
masses is an eigenvalue of an $x_0$ operator acting on wave functions periodic in $x_0$ with the period $\pi/(6H)$.

The approximation: the spectra are computed on the static block $f = f_*$ (the block responds to matter by at most
$\Delta\ln f = 1.1\times10^{-34}$, section A.9), at tree level (the measured masses are tree-level targets; radiative running is
not included), and with the mixing of the zero modes with the Kaluza-Klein modes neglected (its relative size
$(m/m_{\mathrm{KK}})^2$ is at most $2.0\times10^{-6}$, for the top quark). In concert with the other field equations (residual analysis): the
twelve fermion masses enter the thermal history of part B unchanged (to $3.1\times10^{-12}$), the neutrino masses and the PMNS matrix
enter the flavour evolution, the cosmic neutrino background and the CMB computation unchanged (to $5.7\times10^{-12}$ and
$8.2\times10^{-13}$), and the dark-matter mass enters the Kohn-Sham states and the Boltzmann equation unchanged (to $8.1\times10^{-13}$).

## A.4 What the uncertainty relation gives quantitatively {-}

### The exact decomposition of every mass (DERIVED) {-}

For a boson write $F = \mathrm{e}^{-3HL\xi/2}\tilde F$. The exact identity

$$ \mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2 = \Big(\frac{\mathrm{d}\tilde F}{\mathrm{d}\xi}\Big)^2 + \frac{9H^2L^2}{4}\,\tilde F^2 - \frac{3HL}{2}\,\frac{\mathrm{d}\big(\tilde F^2\big)}{\mathrm{d}\xi} $$
<!-- symbols: euler, Hconst, Lcut, xi, diff, Fprof, Ftilde -->

turns the Rayleigh quotient of the eigenvalue equation (FE-50) with the tip condition (FE-51),

$$ \tilde m^2 = \frac{\int_{-1}^{0}\mathrm{e}^{3HL\xi}\big(\mathrm{d}F/\mathrm{d}\xi\big)^2\,\mathrm{d}\xi + \beta\,\mathrm{e}^{-3HL}F(-1)^2}{\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}, $$
<!-- symbols: mtilde, euler, Hconst, Lcut, xi, diff, Fprof, betaRobin -->

into the decomposition

$$ \tilde m^2 = \langle k_\xi^2\rangle + \frac{9H^2L^2}{4} - \frac{3HL}{2}\,\varrho_\xi(0) + \Big(\frac{3HL}{2} + \beta\Big)\varrho_\xi(-1),\qquad \langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\tilde F/\mathrm{d}\xi\big)^2\,\mathrm{d}\xi}{\int_{-1}^{0}\tilde F^2\,\mathrm{d}\xi} $$
<!-- symbols: mtilde, ana_kxi, Hconst, Lcut, ana_varrhoxi, betaRobin, diff, Ftilde, xi -->

of the eigenvalue into the hidden kinetic energy $\langle k_\xi^2\rangle$, the constant warp $9H^2L^2/4$ of the three extra times,
an attractive point term at the fold and a repulsive one at the tip. For a fermion mode of the block Hamiltonian with a
constant mass, i.e. a localisation $c$ (or $c_\Psi$), the corresponding exact decomposition is

$$ \tilde\varepsilon^2 = \langle k_\xi^2\rangle + c^2 - c\,\frac{\big[\chi^\dagger\sigma_3\chi\big]_{-1}^{0}}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi},\qquad \langle k_\xi^2\rangle = \frac{\int_{-1}^{0}\big(\mathrm{d}\chi/\mathrm{d}\xi\big)^\dagger\big(\mathrm{d}\chi/\mathrm{d}\xi\big)\,\mathrm{d}\xi}{\int_{-1}^{0}\chi^\dagger\chi\,\mathrm{d}\xi} $$
<!-- symbols: epstilde, ana_kxi, cloc, chi, dagger, sigmaPauli, diff, xi -->

(the hidden kinetic energy, the bulk mass and a boundary term). Only the hidden kinetic term is bounded by the uncertainty
relation.

### The uncertainty relation on the cell (DERIVED, a theorem) {-}

On the cell, which ends at the tip, the uncertainty relation acquires a tip term:

$$ \sqrt{\langle k_\xi^2\rangle}\;\Delta\xi \ge \frac{1 - \varrho_\xi(-1)}{2} $$
<!-- symbols: ana_kxi, Delta, xi, ana_varrhoxi -->

It follows from an integration by parts (the fold end $\xi = 0$ contributes nothing) and the Cauchy-Schwarz inequality:

$$ 1 = \int_{-1}^{0}\varrho_\xi\,\mathrm{d}\xi = \varrho_\xi(-1) - \int_{-1}^{0}\xi\,\frac{\mathrm{d}\varrho_\xi}{\mathrm{d}\xi}\,\mathrm{d}\xi,\qquad \Big\lvert\int_{-1}^{0}\xi\,\frac{\mathrm{d}\varrho_\xi}{\mathrm{d}\xi}\,\mathrm{d}\xi\Big\rvert \le 2\,\Delta\xi\,\sqrt{\langle k_\xi^2\rangle} $$
<!-- symbols: ana_varrhoxi, diff, xi, Delta, ana_kxi -->

The familiar form $\langle k_\xi^2\rangle\Delta\xi^2 \ge 1/4$ is guaranteed only for profiles negligible at the tip. It can hold
otherwise (the first even Kaluza-Klein mode, with $\varrho_\xi(-1) = 0.655$, has $\langle k_\xi^2\rangle\Delta\xi^2 = 4.59$), while the
broad fold zero mode of dirac16complex violates it ($\langle k_\xi^2\rangle\Delta\xi^2 = 0.097$, $\varrho_\xi(-1) = 0.489$) and
satisfies the relation with the tip term.

### The lower bound for a localised state (DERIVED) {-}

If the hidden kinetic energy were the whole mass, $\tilde m^2 = \langle k_\xi^2\rangle$, the relation on the cell would bound the
mass by the author's estimate:

$$ m = \frac{\sqrt{\langle k_\xi^2\rangle}}{fL} \ge \big(1 - \varrho_\xi(-1)\big)\,m_{\mathrm{Heis}},\qquad m_{\mathrm{Heis}} = \frac{\hbar}{2fL\,\Delta\xi} \ge \frac{\hbar}{2fL} = 11.05\ \text{TeV} $$
<!-- symbols: mmass, ana_kxi, fblock, Lcut, ana_varrhoxi, ana_mHeis, ana_hbar, Delta, xi -->

The last inequality holds because $\Delta\xi \le 1$ on the half cell. The author's estimate is therefore precisely the lower
bound that the uncertainty relation sets on the hidden kinetic energy of a state that is negligible at the tip, and no
profile on the cell can make it smaller than $11.05$ TeV. The actual masses differ from this bound by the other terms of the
decompositions: the warp, the fold and the tip terms of a boson, the bulk mass and the boundary term of a fermion. They were
computed for every class of particle (DERIVED; the sum rules reproduce the boson eigenvalues $\tilde m^2$ to $1.0\times10^{-8}$
in absolute value, the discretisation error of the finite-element profiles (relative $7.8\times10^{-4}$ for $W^\pm$ and
$6.0\times10^{-4}$ for $Z$, whose eigenvalues are only $1.3$ and $1.7\times10^{-5}$, and below $3\times10^{-11}$ for the
excitations), and the dark matter to $1.2\times10^{-11}$ relative; the relation with the tip term holds for every tabulated
state, with the smallest margin $0.057$ for the fold band of dirac16complex).

Bosons (the warp term is $9H^2L^2/4 = 20.25$ for every mode):

| state | $\langle k_\xi^2\rangle$ | fold term | tip term | $\tilde m^2$ | $m/m_{\mathrm{Heis}}$ |
| ---------- | ---- | ---- | ---- | ---- | ---- |
| photon, gluons, graviton | $20.250$ | $-40.505$ | $0.0050$ | $0$ | $0$ |
| $W^\pm$ | $20.250$ | $-40.505$ | $0.0050$ | $1.32\times10^{-5}$ | $1.14\times10^{-3}$ |
| $Z$ | $20.250$ | $-40.505$ | $0.0050$ | $1.70\times10^{-5}$ | $1.29\times10^{-3}$ |
| first even Kaluza-Klein mode | $9.870$ | $-2.949$ | $2.949$ | $30.120$ | $7.49$ |
| first odd mode | $4.891$ | $0$ | $1.948$ | $27.089$ | $6.47$ |

The chiral zero modes of the fermions: each alone is massless, its hidden kinetic energy $\langle k_\xi^2\rangle$ equals the
bulk term $c^2$ and the boundary term is $-2c^2$; one doublet zero mode serves the three generations of a sector, and every
fermion has its own singlet zero mode (a singlet zero mode is right-handed with $c_R < 0$; its profile is that of a doublet
zero mode with $c = -c_R$):

| zero mode | $c$ | $\langle k_\xi^2\rangle$ | boundary term | $\Delta(fy)$ (m) | $m_{\mathrm{Heis}}$ (GeV) | $\varrho_\xi(-1)$ | $\langle k_\xi^2\rangle\Delta\xi^2$ |
| ---------------- | -------- | -------- | --------- | ----------- | --------- | ----------- | --------- |
| lepton doublet | $5.9529$ | $35.437$ | $-70.874$ | $1.06\times10^{-21}$ | $93\,080$ | $8.0\times10^{-5}$ | $0.4997$ |
| quark doublet | $3.3823$ | $11.440$ | $-22.880$ | $1.83\times10^{-21}$ | $53\,800$ | $7.8\times10^{-3}$ | $0.4829$ |
| $\nu_1$ singlet | $35.0452$ | $1228.16$ | $-2456.33$ | $1.80\times10^{-22}$ | $547\,816$ | $2.5\times10^{-29}$ | $0.5000$ |
| $\nu_2$ singlet | $32.8481$ | $1079.00$ | $-2157.99$ | $1.92\times10^{-22}$ | $513\,472$ | $1.9\times10^{-27}$ | $0.5000$ |
| $\nu_3$ singlet | $31.0702$ | $965.36$ | $-1930.71$ | $2.03\times10^{-22}$ | $485\,680$ | $6.4\times10^{-26}$ | $0.5000$ |
| electron singlet | $14.5539$ | $211.82$ | $-423.63$ | $4.34\times10^{-22}$ | $227\,503$ | $6.6\times10^{-12}$ | $0.5000$ |
| muon singlet | $8.9809$ | $80.657$ | $-161.314$ | $7.03\times10^{-22}$ | $140\,388$ | $2.8\times10^{-7}$ | $0.5000$ |
| tau singlet | $5.9529$ | $35.437$ | $-70.874$ | $1.06\times10^{-21}$ | $93\,080$ | $8.0\times10^{-5}$ | $0.4997$ |
| up singlet | $15.4300$ | $238.09$ | $-476.17$ | $4.09\times10^{-22}$ | $241\,198$ | $1.2\times10^{-12}$ | $0.5000$ |
| charm singlet | $8.7683$ | $76.883$ | $-153.766$ | $7.20\times10^{-22}$ | $137\,064$ | $4.2\times10^{-7}$ | $0.5000$ |
| top singlet | $3.3823$ | $11.440$ | $-22.880$ | $1.83\times10^{-21}$ | $53\,800$ | $7.8\times10^{-3}$ | $0.4829$ |
| down singlet | $14.6258$ | $213.91$ | $-427.83$ | $4.32\times10^{-22}$ | $228\,626$ | $5.8\times10^{-12}$ | $0.5000$ |
| strange singlet | $11.5158$ | $132.61$ | $-265.23$ | $5.48\times10^{-22}$ | $180\,012$ | $2.3\times10^{-9}$ | $0.5000$ |
| bottom singlet | $7.5005$ | $56.258$ | $-112.516$ | $8.41\times10^{-22}$ | $117\,248$ | $4.6\times10^{-6}$ | $0.5000$ |

A zero mode localised exponentially at the fold, $\varrho_\xi \propto \mathrm{e}^{2c\xi}$, has

$$ \Delta\xi^2 \simeq \frac{1}{2c^2},\qquad \langle k_\xi^2\rangle\,\Delta\xi^2 \simeq \frac12\qquad (c \gg 1), $$
<!-- symbols: Delta, xi, cloc, ana_kxi -->

twice the minimum $1/4$ of the familiar relation. The fermions, their uncertainty estimates (that of the broader of their two
zero modes, i.e. the smaller $m_{\mathrm{Heis}}$) and their sensitivities to the localisation and to the block:

| fermion | mass | $m_{\mathrm{Heis}}$ (GeV) | $m/m_{\mathrm{Heis}}$ | $\frac{\mathrm{d}\ln m}{\mathrm{d}\ln(-c_R)}$ | $\frac{\mathrm{d}\ln m}{\mathrm{d}\ln f}$ |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| $\nu_1$ | $1.000$ meV | $93\,080$ | $1.1\times10^{-17}$ | $-34.55$ | $-41.0$ |
| $\nu_2$ | $8.712$ meV | $93\,080$ | $9.4\times10^{-17}$ | $-32.35$ | $-38.8$ |
| $\nu_3$ | $50.140$ meV | $93\,080$ | $5.4\times10^{-16}$ | $-30.57$ | $-37.0$ |
| electron | $0.511$ MeV | $93\,080$ | $5.5\times10^{-9}$ | $-14.05$ | $-20.5$ |
| muon | $105.66$ MeV | $93\,080$ | $1.1\times10^{-6}$ | $-8.48$ | $-14.9$ |
| tau | $1776.93$ MeV | $93\,080$ | $1.9\times10^{-5}$ | $-5.45$ | $-11.9$ |
| up | $2.16$ MeV | $53\,800$ | $4.0\times10^{-8}$ | $-14.93$ | $-18.8$ |
| charm | $1.273$ GeV | $53\,800$ | $2.4\times10^{-5}$ | $-8.27$ | $-12.2$ |
| top | $172.56$ GeV | $53\,800$ | $3.2\times10^{-3}$ | $-2.89$ | $-6.8$ |
| down | $4.70$ MeV | $53\,800$ | $8.7\times10^{-8}$ | $-14.13$ | $-18.0$ |
| strange | $93.5$ MeV | $53\,800$ | $1.7\times10^{-6}$ | $-11.02$ | $-14.9$ |
| bottom | $4.183$ GeV | $53\,800$ | $7.8\times10^{-5}$ | $-7.00$ | $-10.9$ |

(The sensitivity to the singlet localisation is that of the singlet tip density with the doublet fixed, written out in
section A.5; the doublet localisation enters every mass of its sector with $-5.45$ (leptons) and $-2.89$ (quarks); the block
sensitivity follows from (FE-85) in section A.8.) The bosons and the states of dirac16complex:

| state | $\Delta(fy)$ (m) | $m_{\mathrm{Heis}}$ (GeV) | $\varrho_\xi(-1)$ | $\langle k_\xi^2\rangle\Delta\xi^2$ |
| ---------- | ---- | ---- | ---- | ---- |
| photon, gluons, graviton; $W^\pm$; $Z$ | $1.40\times10^{-21}$ | $70\,560$ | $1.1\times10^{-3}$ | $0.497$ |
| first even Kaluza-Klein mode | $6.09\times10^{-21}$ | $16\,204$ | $0.655$ | $4.59$ |
| first odd mode | $5.55\times10^{-21}$ | $17\,771$ | $0.433$ | $1.89$ |
| fold band of dirac16complex | $4.31\times10^{-21}$ | $22\,903$ | $0.489$ | $0.097$ |
| dark matter (lowest odd level) | $5.09\times10^{-21}$ | $19\,395$ | $0.772$ | $0.847$ |

and the decomposition of the two states of dirac16complex (both halves; the bulk term is $c_\Psi^2 = (f_*m_\Psi L)^2 = 0.418$):

| state | $\langle k_\xi^2\rangle$ | bulk $c_\Psi^2$ | boundary term | $\tilde\varepsilon^2$ | $m/m_{\mathrm{Heis}}$ |
| ---------- | ---- | ---- | ---- | ---- | ---- |
| fold band | $0.418$ | $0.418$ | $-0.836$ | $0$ | $0$ |
| dark matter | $2.608$ | $0.418$ | $0.998$ | $4.024$ | $2.29$ |

## A.5 Where the argument fails, and what replaces it {-}

### Three classes of states (DERIVED) {-}

* **Massless although localised.** The photon, the gluons and the graviton are localised at the fold
  ($\Delta(fy) = 1.40\times10^{-21}$ m, $m_{\mathrm{Heis}} = 70.6$ TeV, $\langle k_\xi^2\rangle\Delta\xi^2 = 0.497$), yet exactly massless:
  the fold term cancels the hidden kinetic energy and the warp. The cancellation is exact because the flat profile is an
  eigenfunction with $\tilde m = 0$, protected by four-dimensional gauge invariance and general covariance. The fold bands of
  dirac16complex are massless for the analogous chiral reason (the zero mode $\chi = (\mathrm{e}^{c_\Psi\xi}, 0)^T$ of (FE-62) solves
  the block equation with both boundary conditions for every mass profile), and so is every fermion zero mode before the tip
  mixes it with its partner.
* **Heavy: the uncertainty estimate lies below the mass.** Every $x_0$ excitation of the gauge fields and the graviton lies
  above the gap of their operator: for every tip parameter $\beta$ from $0$ to $10^6$ exactly one even level lies below
  $9H^2L^2/4$ (the zero mode, lifted only by the tip) and no odd level does (the gap theorem, DERIVED), so every odd mode and
  every excitation of these fields has $m \ge 3H/(2f_*) = 99.5$ TeV. The Dirac operator of dirac16complex has no such warp gap;
  its excitations start at the lowest odd level, $3.10\,m_\Psi = 44.35$ TeV (the dark matter). For the computed states
  $m_{\mathrm{Heis}}$ is exceeded by factors 2.3 to 7.5 (dark matter 2.29, first odd mode 6.47, first even mode 7.49): the author's
  estimate lies below these masses (observed for these states, not derived for all), and the dark-matter mass is an $x_0$
  mass in the author's sense, since its hidden wave number carries $\varpi^2/\tilde\varepsilon^2 = 0.896$ of $\tilde\varepsilon^2$.
* **Light: the mass comes from the tip, not from the localisation.** For $W^\pm$, $Z$ and the twelve fermions the $x_0$
  dependence that costs energy sits at the tip, where the probability is small: $m/m_{\mathrm{Heis}} = 1.1\times10^{-3}$ ($W^\pm$),
  $1.3\times10^{-3}$ ($Z$), $3.2\times10^{-3}$ (the top quark, a factor 312 below the estimate) down to $1.1\times10^{-17}$ ($\nu_1$).
  For the fermions a sharper localisation gives a LIGHTER particle: $\mathrm{d}\ln m/\mathrm{d}\ln c < 0$ for every zero mode
  (from $-2.89$ for the quark doublet and the top singlet to $-34.55$ for the $\nu_1$ singlet), the reverse of the Heisenberg
  intuition. The lightest particles of all, the neutrinos, have the most sharply localised singlet partners
  ($\Delta(fy) \approx 2\times10^{-22}$ m, $m_{\mathrm{Heis}} \approx 0.5$ PeV).

![The $x_0$ mass mechanism: the actual masses against the uncertainty estimate $m_{\mathrm{Heis}} = \hbar/(2\Delta(fy))$ (circles: bosons and dirac16complex; squares: the twelve fermions, with the $m_{\mathrm{Heis}}$ of their broader zero mode); the excitations and the dark matter lie above the line $m = m_{\mathrm{Heis}}$, the light particles far below. The axis labels are in the plain-text notation of the plotting script: "hbar c/(2 Delta s)" is $m_{\mathrm{Heis}}$ and "m\_H" is $m_{\mathrm{Heis}}$.](figures/fig_analysis_heisenberg.png)

### Why the light fermions must be zero modes whose masses come from the tip (DERIVED) {-}

The lower bound of section A.4 makes the argument quantitative. The hidden kinetic energy of any profile on the cell that is
negligible at the tip is at least that of a mass $m_{\mathrm{Heis}} \ge 1/(2fL) = 11.05$ TeV; for the actual zero modes it is
that of $54$ to $548$ TeV. Every observed fermion mass is at least 64 times smaller than $11.05$ TeV (the top quark) and up to
$10^{16}$ times smaller (the lightest neutrino). A light fermion is therefore possible only if the other terms of its $x_0$
operator cancel its hidden kinetic energy, and the cancellation must be exact up to the tiny remainder: the profile must be
an exact zero mode of the $x_0$ operator. The chiral zero modes of (FE-57) are exactly such profiles: $h\chi = 0$ at $k = 0$, so
the kinetic term $c^2$ and the bulk term $c^2$ are cancelled by the boundary term $-2c^2$, for every localisation. They are
"flat relative to the geometry" in the same sense as the flat profile of the photon: in $\chi = \mathrm{e}^{c\xi}(1, 0)^T$ the
whole $x_0$ dependence is the exponential that the bulk mass itself generates, and it costs no four-dimensional energy. A
zero mode is massless and chiral; a mass requires a term that couples the doublet zero mode to a singlet zero mode of the
opposite chirality, and in UM-2 the only such term is the tip Yukawa coupling of the sigma field (the tip conditions
(FE-30)). Its effect is proportional to the probability amplitudes of the two zero modes at the tip, which is the first-order
root of the exact mass condition, written out again:

$$
\begin{aligned}
&\mathcal{D}(\tilde\varepsilon) =
 \tilde\varepsilon^2\,\frac{\sinh\upsilon_L}{\upsilon_L}\frac{\sinh\upsilon_R}{\upsilon_R}
 - \mathcal{K}^2\Big(\cosh\upsilon_L - c_L\frac{\sinh\upsilon_L}{\upsilon_L}\Big)
 \Big(\cosh\upsilon_R + c_R\frac{\sinh\upsilon_R}{\upsilon_R}\Big) = 0,\\
&\tilde\varepsilon \simeq \mathcal{K}\,\mathcal{Z}(c_L)\,\mathcal{Z}(-c_R),\qquad \mathcal{Z}(c)^2 =
 \frac{c\,\mathrm{e}^{-c}}{\sinh c}
\end{aligned} \tag{FE-59}
$$
<!-- symbols: calD, epstilde, upsilon, iL, iR, Ktip, cloc, calZ, euler -->

For $c \gg 1$ the tip density of a zero mode is exponentially small, and so are the masses and their sensitivities to the
localisation:

$$ \mathcal{Z}(c)^2 = \frac{c\,\mathrm{e}^{-c}}{\sinh c} \simeq 2c\,\mathrm{e}^{-2c},\qquad m = \frac{\tilde\varepsilon}{fL},\qquad \frac{\mathrm{d}\ln m}{\mathrm{d}\ln c} = \frac12\,\frac{\mathrm{d}\ln\mathcal{Z}(c)^2}{\mathrm{d}\ln c} \simeq \frac12 - c\qquad (c \gg 1) $$
<!-- symbols: calZ, cloc, euler, mmass, epstilde, fblock, Lcut, diff -->

($c = -c_R$ for a singlet with the doublet fixed; $-34.55$ for the $\nu_1$ singlet, $-2.89$ for the top singlet). The masses of
the light fermions are thus tip effects of zero modes, not localisation energies: the uncertainty relation does not produce
them, and a sharper localisation lowers them. The same holds for $W^\pm$ and $Z$, whose profiles are the photon's flat zero mode
bent by the tip parameter $\beta$: their masses are the small tip-induced bending ($m/m_{\mathrm{Heis}} \approx 10^{-3}$).

### The hierarchy of the masses (DERIVED) {-}

Because the tip densities depend exponentially on the localisations, bulk masses of order one produce the whole hierarchy:
the twelve fermion masses span fourteen orders of magnitude, from $\nu_1$ to the top quark, with bulk masses between $5.2H$
(the quark doublets, $\mu_Q = 5.2304\,H$) and $54.2H$ in magnitude (the $\nu_1$ singlet), and within a sector the lighter
fermion has the sharper singlet localisation. The doublet bulk masses are $\mu_\ell = 9.2055\,H$ and $\mu_Q = 5.2304\,H$. The
first-order root of (FE-59) agrees with the exact roots to $1.1\times10^{-3}$ for the top quark and to better than
$3\times10^{-4}$ for every other fermion. The hierarchy is the exponential response of the tip densities to order-one bulk masses;
it is not explained further by the mechanism (the bulk masses are fitted).

### The mixing matrices (DERIVED, ASSUMED inputs) {-}

With the doublet shared by the three generations of a sector, the charged current between the mass states $\nu_j$ and the
charged leptons of the generation $i$ carries $\sum_\alpha(\mathcal{K}_\nu)^*_{\alpha j}(\mathcal{K}_e)_{\alpha i}$, and the mixing
matrices are the tip matrices (from (FE-60)):

$$ U = \mathcal{K}_e^\dagger\mathcal{K}_\nu = \mathcal{K}_\nu,\qquad V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d = \mathcal{K}_d\qquad (\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}) $$
<!-- symbols: Upmns, Ktip, dagger, VCKM, identity -->

in the standard parametrisation (STANDARD; the same form for $V_{\mathrm{CKM}}$)

$$
\begin{aligned}
U = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}\mathrm{e}^{-\mathrm{i}\delta_{\mathrm{CP}}}\\
 -s_{12}c_{23} - c_{12}s_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} &
 c_{12}c_{23} - s_{12}s_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} & s_{23}c_{13}\\
 s_{12}s_{23} - c_{12}c_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} &
 -c_{12}s_{23} - s_{12}c_{23}s_{13}\mathrm{e}^{\mathrm{i}\delta_{\mathrm{CP}}} &
 c_{23}c_{13}\end{pmatrix},\qquad
J_{\mathrm{CP}} = c_{12}s_{12}c_{23}s_{23}c_{13}^2s_{13}\sin\delta_{\mathrm{CP}}
\end{aligned} \tag{FE-61}
$$
<!-- symbols: Upmns, cij, sij, euler, imag, deltaCP, JCP -->

with $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta_{\mathrm{CP}} = 212^\circ$ for the PMNS
matrix (NuFIT 6.0, normal ordering; $J_{\mathrm{CP}} = -0.01777$) and $s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$,
$\delta_{\mathrm{CP}} = 1.147$ for the CKM matrix (PDG global fit; $J_{\mathrm{CP}} = 3.117\times10^{-5}$), both unitary to $1.1\times10^{-16}$:

$$ \lvert U\rvert = \begin{pmatrix} 0.8226 & 0.5488 & 0.1488\\ 0.3351 & 0.6543 & 0.6779\\ 0.4594 & 0.5203 & 0.7199\end{pmatrix},\qquad \lvert V_{\mathrm{CKM}}\rvert = \begin{pmatrix} 0.97435 & 0.22501 & 0.00373\\ 0.22488 & 0.97349 & 0.04183\\ 0.00858 & 0.04111 & 0.99912\end{pmatrix} $$
<!-- symbols: Upmns, VCKM -->

The angles and phases are inputs of UM-2, not predictions: the mechanism explains the masses through the localisations, but
not the mixing, which is the choice of the tip matrices (OPEN: their origin). The right-handed rotations are trivial, and
because the doublets of a sector share one bulk mass the first even Kaluza-Klein gauge mode couples to every left-handed
lepton with the same relative strength $0.14434$ and to every left-handed quark with $-0.30066$, so there are no
flavour-changing neutral currents at tree level (the largest off-diagonal coupling in the mass basis is $10^{-17}$, round-off;
different doublet bulk masses would create off-diagonal couplings up to $0.033$) (DERIVED).

### The massless zero modes (DERIVED) {-}

The exactly massless states of UM-2 are the zero modes of $x_0$ operators that no term of the action lifts: the photon and
the gluons (flat profiles with $\beta = 0$, protected by the unbroken gauge invariance; the tip terms give mass to $W^\pm$ and $Z$
only), the graviton (flat profile, protected by four-dimensional general covariance), and the fold bands of both halves of
dirac16complex (chiral zero modes; no tip operator acts on them, the scalar density of a chiral zero mode vanishes, and I13
acts only on the lower component; part B). These are exactly the exceptions named by the author: the graviton, the photon
and the quanta of dirac16complex, more precisely its massless fold bands, while its odd quanta are massive (the dark matter).

## A.6 Proper versus coordinate localisation (DERIVED) {-}

The proper element of the hidden direction is

$$ f\,\mathrm{d}y = f\cot z\,\mathrm{d}x_0 $$
<!-- symbols: fblock, diff, ycoord, zvar, x0 -->

which vanishes at the fold and diverges at the tips. The photon zero mode, localised at the fold in proper length, has
61.9 % of its probability within $\pi/8$ of the tips in the coordinate $z = 6Hx_0$: localisation in the coordinate $x_0$ is chart
dependent. A profile confined to a small proper distance from the fold ($\Delta\xi = 0.157$, i.e. $\lvert y\rvert \lesssim 0.47/H$,
$\sin z \gtrsim \mathrm{e}^{-2.8}$) extends over almost the whole coordinate range of $z$, and its probability per unit $z$ is
largest near the tips. Only the proper hidden length enters the masses; the author's "$\Delta x_0$ small" must be read as
"$\Delta(fy)$ small".

## A.7 The neutrinos: masses, mixing and flavour conversion as $x_0$ effects {-}

The three neutrino masses are $x_0$ eigenvalues of the same kind as the charged-fermion masses: Dirac masses produced at the
tip by the overlap of the lepton-doublet zero mode ($c_\ell = 5.9529$) with three right-handed singlet zero modes localised
very sharply at the fold ($c_R = -35.05$, $-32.85$, $-31.07$). With the lightest mass ASSUMED and the measured splittings
(STANDARD, NuFIT 6.0, normal ordering):

$$
m_1 = 1.000\ \text{meV},\qquad m_2 = \sqrt{m_1^2 + \Delta m_{21}^2} = 8.712\ \text{meV},\qquad
m_3 = \sqrt{m_1^2 + \Delta m_{31}^2} = 50.140\ \text{meV} \tag{FE-100}
$$
<!-- symbols: mnu123, Delta, dm2 -->

The right-handed neutrinos are gauge singlets and are never in thermal equilibrium (their interactions are the tip mixing,
whose rate is suppressed by $(m_i/T)^2$, STANDARD, and the portal I11 with the $B - L$ charge $-1$, through which the dark matter
annihilates into right-handed neutrino pairs at only $2.0\times10^{-17}$ of its I13 rate into quarks, DERIVED; part B), so they
add no radiation. The PMNS matrix is the tip matrix $\mathcal{K}_\nu$ (section A.5); its angles and phase are inputs. Given the
masses and $U$, the flavour conversion follows from the four-dimensional effective theory (STANDARD):

$$
\mathrm{i}\,\frac{\mathrm{d}\boldsymbol{\psi}}{\mathrm{d}x_4} = H_{\mathrm{fl}}\,\boldsymbol{\psi},\qquad
H_{\mathrm{fl}} = \frac{1}{2E}\,U\,\mathrm{diag}\big(m_1^2,\ m_2^2,\ m_3^2\big)\,U^\dagger + V,\qquad
\mathcal{U}(L_{\mathrm{b}}) = \mathrm{e}^{-\mathrm{i}H_{\mathrm{fl}}L_{\mathrm{b}}},\qquad
\mathcal{P}(\nu_\alpha\to\nu_\beta) = \lvert\mathcal{U}_{\beta\alpha}\rvert^2 \tag{FE-104}
$$
<!-- symbols: imag, diff, bspsi, x4, Hfl, Eenergy, Upmns, diag, mnu123, dagger, Vmat, calU, Lb, euler, calP, nuflav, ialpha, ibeta -->

with the potentials of coherent forward scattering in matter

$$
\begin{aligned}
&V_\alpha = \sqrt2\,G_{\mathrm{F}}\Big[\delta_{\alpha e}\big(n_{e^-} - n_{e^+}\big) + \sum_f\tilde
 g^f_V\big(n_f - n_{\bar f}\big)\Big],\\
&V = \mathrm{diag}\big(V_{\mathrm{CC}},\ 0,\ 0\big) + V_{\mathrm{NC}}\,\mathbf{1},\qquad V_{\mathrm{CC}}
 = \sqrt2\,G_{\mathrm{F}}\,n_{\mathrm{e}},
 \qquad V_{\mathrm{NC}} = -\frac{G_{\mathrm{F}}\,n_{\mathrm{n}}}{\sqrt2}
\end{aligned} \tag{FE-103}
$$
<!-- symbols: Vmat, ialpha, GF, delta, ie, nepm, if, gtilde, iV, ndens, nfbar, diag, VCC, identity, ne, nn -->

(the neutral-current potential is common to the three flavours and drops out of the conversion; for antineutrinos
$U \to U^*$ and $V \to -V$). The oscillation phases $\Delta_{21}$, $\Delta_{31}$, $\Delta_{32}$ contain the differences of squared
$x_0$ eigenvalues, so oscillation experiments measure the $x_0$ spectrum directly. These differences are the quantities of
UM-2 most sensitive to the block scale (DERIVED):

$$ \begin{aligned} &\frac{\mathrm{d}\ln\big(m_j^2 - m_i^2\big)}{\mathrm{d}\ln f} = \frac{2}{m_j^2 - m_i^2}\Big(m_j^2\,\frac{\mathrm{d}\ln m_j}{\mathrm{d}\ln f} - m_i^2\,\frac{\mathrm{d}\ln m_i}{\mathrm{d}\ln f}\Big):\\
&\frac{\mathrm{d}\ln\Delta m_{21}^2}{\mathrm{d}\ln f} = -77.5,\qquad \frac{\mathrm{d}\ln\Delta m_{31}^2}{\mathrm{d}\ln f} = -74.0,\qquad \frac{\mathrm{d}\ln\Delta m_{32}^2}{\mathrm{d}\ln f} = -73.9 \end{aligned} $$
<!-- symbols: diff, mmass, ij, ii, fblock, Delta, dm2 -->

The light neutrino states also mix with the Kaluza-Klein excitations of the lepton fields, which makes the $3\times3$ PMNS
matrix non-unitary at the relative order $(m_i/m_{\mathrm{KK}})^2 \le 1.7\times10^{-31}$ (ESTIMATE; $2.0\times10^{-6}$ for the top
quark, the largest of all fermions): unobservable. The flavour conversion of UM-2 is therefore that of the three-flavour
Standard Model with Dirac neutrinos, which UM-2 computes for the vacuum, the Earth, the Sun, the early Universe and supernovae.

**Dirac or Majorana (DERIVED).** The $x_0$ mechanism explains the small Dirac masses by the localisation of the right-handed
singlets with tip couplings of order one. Without right-handed neutrinos the masses would be Majorana masses from the
gauge-invariant tip operator (the tip form of the Weinberg operator; not part of UM-2)

$$ S_{\mathrm{M}} = -\frac12\int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\sum_{i,j=1}^{3}m^{\mathrm{M}}_{ij}\,\tilde\nu_i\tilde\nu_j + \text{h.c.},\qquad \tilde\nu_i = \big(\Sigma^\dagger\ell_i\big)_1 $$
<!-- symbols: sol_SM, ycoord, Lcut, diff, Xtip, gtip, ii, ij, sol_mM, sol_nutilde, Sigma, dagger, ldoublet -->

(the upper component of $\Sigma^\dagger\ell_i$ is neutral, since $\Sigma \to U_L\Sigma U_Y^\dagger$ absorbs both the SU(2) and the
hypercharge transformations of $\ell_i$), which gives, to first order in the tip value of the doublet zero mode,

$$ m_i = \mathcal{K}_{\mathrm{M}}^{(i)}\,\frac{\mathcal{Z}(c_L)^2}{fL},\qquad \mathcal{Z}(c_L)^2 = 8.04\times10^{-5},\qquad \frac{1}{fL} = 22.11\ \text{TeV}, $$
<!-- symbols: mmass, ii, sol_KM, calZ, cloc, iL, fblock, Lcut -->

so the measured masses need $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.6\times10^{-13}$, $4.9\times10^{-12}$, $2.8\times10^{-11}$: a hierarchy of tip
couplings that the mechanism does not explain. The $x_0$ mechanism therefore favours Dirac neutrinos. The Majorana case would
show up in neutrinoless double-beta decay with

$$ m_{\beta\beta} = \Big\lvert\sum_{i=1}^{3}U_{ei}^2\,m_i\,\mathrm{e}^{\mathrm{i}\varphi^{\mathrm{M}}_i}\Big\rvert $$
<!-- symbols: sol_mbb, ii, Upmns, ie, mmass, euler, imag, sol_phiM -->

between $0.84$ and $4.41$ meV over all Majorana phases ($\lvert U_{ei}\rvert^2m_i = 0.677$, $2.624$, $1.111$ meV), below the reach of
present experiments, and in a twice larger capture rate of the non-relativistic cosmic neutrino background; the flavour
conversion is the same.

## A.8 The mass mechanism, the block and the deflating extra times {-}

Every mass and coupling depends on the block scale $f$ (DERIVED). A fermion mass $m = \tilde\varepsilon/(fL)$, with the
first-order root of (FE-59) and localisations $c = f\mu L$ proportional to $f$, has the block sensitivity

$$
\frac{\mathrm{d}\ln m}{\mathrm{d}\ln f} = -1 +
 \frac12\Big[\frac{\mathrm{d}\ln\mathcal{Z}(c_L)^2}{\mathrm{d}\ln c_L}
 + \frac{\mathrm{d}\ln\mathcal{Z}(-c_R)^2}{\mathrm{d}\ln(-c_R)}\Big] \tag{FE-85}
$$
<!-- symbols: diff, mmass, fblock, calZ, cloc, iL, iR -->

the Kaluza-Klein masses $m^{\mathrm{KK}}_n = \tilde m_n/(fL)$ scale as $f^{-1}$, and the four-dimensional couplings and Newton's
constant follow from the reduction on the block

$$
\begin{aligned}
&G^{(4)}_{\mu\nu} + \Lambda_4\,g^{(4)}_{\mu\nu} = 8\pi G_{\mathrm{N}}\,\mathcal{T}^{(4)}_{\mu\nu},\qquad
 8\pi G_{\mathrm{N}} = \frac{\kappa}{\mathcal{G}(K_*)\,V_\perp},\qquad V_\perp =
 \frac{2f^4v_{\mathrm{t}}\big(1 - \mathrm{e}^{-3HL}\big)}{3H},\\
&\mathcal{T}^{(4)}_{\mu\nu} =
 \int\mathrm{d}x_0\,\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7\,\sqrt{\lvert
 g_\perp\rvert}\;\mathcal{T}_{\mu\nu},
 \qquad g_3^2 = \frac{\hat g_3^2}{V_\perp},\qquad g_2^2 = \frac{\hat g_2^2}{V_\perp},\qquad g_1^2 =
 \frac{\hat g_1^2}{V_\perp}
\end{aligned} \tag{FE-49}
$$
<!-- symbols: G4tensor, imu, inu, Lambda4, g4, pi, GN, T4, kappa, GK, Kstar, Vperp, fblock, vt, euler, Hconst, Lcut, diff, x0, x5, x6, x7, gperp, EMT, g3, ghat3, g2, ghat2, g1, ghat1 -->

so that the gauge couplings scale as $g_3^2, g_2^2, g_1^2 \propto 1/V_\perp \propto f^{-4}$, and

$$ \frac{\mathrm{d}\ln G_{\mathrm{N}}}{\mathrm{d}\ln f} = -4 + \frac{2K_*}{\mathcal{G}(K_*)}\,\frac{\mathrm{d}\mathcal{G}}{\mathrm{d}K}\Big\vert_{K = K_*} = +2.05 $$
<!-- symbols: diff, GN, fblock, Kstar, GK, Kblock -->

(the Lovelock factor $\mathcal{G}$ of the four-dimensional Newton constant varies with the block too):

| quantity | $\mathrm{d}\ln(\cdot)/\mathrm{d}\ln f$ |
| ---------- | ---------- |
| Kaluza-Klein masses, the gap $3H/(2f)$ | $-1$ |
| $m_{\mathrm{W}}$ (and $m_{\mathrm{Z}}$) | $-0.501$ |
| $m_1$, $m_2$, $m_3$ | $-41.0$, $-38.8$, $-37.0$ |
| electron, muon, tau masses | $-20.5$, $-14.9$, $-11.9$ |
| up, charm, top masses | $-18.8$, $-12.2$, $-6.8$ |
| down, strange, bottom masses | $-18.0$, $-14.9$, $-10.9$ |
| $M_{\mathrm{DM}}$ | $-0.772$ |
| $\alpha_{\mathrm{em}}$ and the gauge couplings | $-4$ |
| $G_{\mathrm{N}}$ | $+2.05$ |

The author's metric lets the extra times $x_5, x_6, x_7$ (and, in the corrected metric, $x_0$ with them) deflate
exponentially. In UM-2 they do so in the primordial era: the full nonlinear equations take a large block into the stabilised
one at rates up to $\lvert\mathcal{H}_f\rvert = 2.63H$ (in the stored runs), deflating by up to the factor 2.917 in $f$ (the
largest block that still reaches the stabilised one), after which the block oscillates about $f_*$ (the
radion, $\omega_{\mathrm{r}} = 3.387H = 48.42$ TeV) and stays frozen. A continuing deflation today is excluded (ESTIMATE, bounds
FROM MEMORY): since

$$ \frac{\mathrm{d}\ln m}{\mathrm{d}x_4} = \frac{\mathrm{d}\ln m}{\mathrm{d}\ln f}\,\mathcal{H}_f,\qquad \frac{\mathrm{d}\ln\alpha_{\mathrm{em}}}{\mathrm{d}x_4} = -4\,\mathcal{H}_f,\qquad \frac{\mathrm{d}\ln G_{\mathrm{N}}}{\mathrm{d}x_4} = 2.05\,\mathcal{H}_f, $$
<!-- symbols: diff, mmass, x4, fblock, Hf, alphaem, GN -->

the atomic-clock bound $\lvert\mathrm{d}\ln\alpha_{\mathrm{em}}/\mathrm{d}x_4\rvert < 10^{-17}$/yr requires
$\lvert\mathcal{H}_f\rvert < 2.5\times10^{-18}$/yr $= 3.6\times10^{-8}\,\mathcal{H}_0$ ($\mathcal{H}_0 = 6.90\times10^{-11}$/yr), lunar ranging
($\lvert\mathrm{d}\ln G_{\mathrm{N}}/\mathrm{d}x_4\rvert < 10^{-13}$/yr) requires $\lvert\mathcal{H}_f\rvert < 4.9\times10^{-14}$/yr
$= 7.1\times10^{-4}\,\mathcal{H}_0$, and a block deflating at the Hubble rate ($\lvert\mathcal{H}_f\rvert = \mathcal{H}_0$) would change the
electron mass by $20.5\,\mathcal{H}_0 = 1.4\times10^{-9}$ per year. The extra times are irrelevant at low energies not because they
keep deflating but because they are small (the proper half cell $f_*L = 3f_*/H = 8.9\times10^{-21}$ m, Kaluza-Klein masses above
100 TeV) and frozen. The price is the stabiliser (ASSUMED, origin OPEN) and the radion left over from the deflation, whose
Planck-suppressed decay is estimated (ESTIMATE) as

$$ \Gamma_{\mathrm{r}} = \frac{C_{\mathrm{r}}\,\omega_{\mathrm{r}}^3}{4\pi\bar M_{\mathrm{Pl}}^2},\qquad T_{\mathrm{RH}} = \Big(\frac{90}{\pi^2g_\rho}\Big)^{1/4}\sqrt{\Gamma_{\mathrm{r}}\bar M_{\mathrm{Pl}}} $$
<!-- symbols: ana_Gammar, ana_Cr, omegar, pi, ana_MPlbar, ana_TRH, grho -->

with the reduced Planck mass $\bar M_{\mathrm{Pl}} = 2.435\times10^{18}$ GeV, an order-one coupling factor $C_{\mathrm{r}}$ and
$g_\rho = 10.75$: the lifetime is $0.43\,\text{s}/C_{\mathrm{r}}$ and the reheating temperature $T_{\mathrm{RH}} = 1.85\sqrt{C_{\mathrm{r}}}$ MeV,
below the 4.7 MeV that nucleosynthesis needs unless $C_{\mathrm{r}} > 6.5$: a moduli problem (OPEN).

## A.9 The nucleon mass, the block response and the Kaluza-Klein gravitons {-}

Most of the visible mass is nucleon mass, i.e. QCD binding energy, which is not an $x_0$ eigenvalue of a field but follows from
the strong coupling by dimensional transmutation. In UM-2 the coupling is fixed at the Kaluza-Klein scale,
$g_3^2 = \hat g_3^2/V_\perp \propto f^{-4}$ (FE-49), so the QCD scale is an $x_0$ quantity too (ESTIMATE at one loop):

$$
\begin{aligned}
&\frac{1}{\alpha_3(m_{\mathrm{KK}})} = \frac{1}{\alpha_3(m_{\mathrm{Z}})} +
 \frac{7}{2\pi}\ln\frac{m_{\mathrm{KK}}}{m_{\mathrm{Z}}},\qquad
 \Lambda_{\mathrm{QCD}}^{(6)} = m_{\mathrm{KK}}\,\mathrm{e}^{-2\pi/(7\alpha_3(m_{\mathrm{KK}}))},\qquad
 \Lambda_{\mathrm{QCD}}^{(3)} =
 \big(\Lambda_{\mathrm{QCD}}^{(6)}\big)^{21/27}\big(m_{\mathrm{c}}m_{\mathrm{b}}m_{\mathrm{t}}\big)^{2/27},\\
&\frac{\mathrm{d}\ln m_{\mathrm{p}}}{\mathrm{d}\ln f} = \Big(1 - \frac{\sigma_{\pi N} +
 \sigma_{\mathrm{s}}}{m_{\mathrm{p}}}\Big)
 \frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}}{\mathrm{d}\ln f}
 + \frac{\sigma_{\pi N}}{2m_{\mathrm{p}}}\Big(\frac{\mathrm{d}\ln m_{\mathrm{u}}}{\mathrm{d}\ln f} +
 \frac{\mathrm{d}\ln m_{\mathrm{d}}}{\mathrm{d}\ln f}\Big)
 + \frac{\sigma_{\mathrm{s}}}{m_{\mathrm{p}}}\,\frac{\mathrm{d}\ln m_{\mathrm{s}}}{\mathrm{d}\ln f}
\end{aligned} \tag{FE-83}
$$
<!-- symbols: alpha3, mKK, mZ, pi, rhoQCDscale, euler, mquarks, diff, mnucleon, fblock, sigmapiN, sigmas -->

and through the quark thresholds

$$
\begin{aligned}
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f} = -1 -
 \frac{8\pi}{7\alpha_3(m_{\mathrm{KK}})},\qquad
 \frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(5)}}{\mathrm{d}\ln f} =
 \frac{21}{23}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{23}\frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f},\\
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(4)}}{\mathrm{d}\ln f} =
 \frac{21}{25}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{25}\Big(\frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f} + \frac{\mathrm{d}\ln
 m_{\mathrm{b}}}{\mathrm{d}\ln f}\Big),\\
&\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(3)}}{\mathrm{d}\ln f} =
 \frac{21}{27}\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(6)}}{\mathrm{d}\ln f}
 + \frac{2}{27}\Big(\frac{\mathrm{d}\ln m_{\mathrm{c}}}{\mathrm{d}\ln f} + \frac{\mathrm{d}\ln
 m_{\mathrm{b}}}{\mathrm{d}\ln f}
 + \frac{\mathrm{d}\ln m_{\mathrm{t}}}{\mathrm{d}\ln f}\Big)
\end{aligned} \tag{FE-84}
$$
<!-- symbols: diff, rhoQCDscale, fblock, pi, alpha3, mKK, mquarks -->

With $\alpha_3(m_{\mathrm{Z}}) = 0.1180$, i.e. $\alpha_3(m_{\mathrm{KK}}) = 0.0606$, the sigma terms $\sigma_{\pi N} = 45$ MeV and
$\sigma_{\mathrm{s}} = 40$ MeV (FROM MEMORY) and the quark sensitivities of (FE-85) ($-18.82$, $-18.01$, $-14.90$, $-12.15$, $-10.89$,
$-6.77$ for the up, down, strange, charm, bottom and top quarks), the QCD scale has the sensitivities $-60.2$ (six flavours),
$-55.6$, $-52.0$ and $-49.0$ (three flavours), and $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$: the nucleon mass is the most
block-sensitive mass of UM-2, more than the lightest neutrino ($-41.0$), and a block that drifted today would change the
proton-to-electron mass ratio by $(46.1 - 20.5)\lvert\mathcal{H}_f\rvert$ per unit time.

In the coupled solution the block responds to the block-averaged sources of all species with the adiabatic response of the
linearised background equations (DERIVED)

$$
\begin{aligned}
&\Delta K = \frac{c_\rho\,\kappa\Delta\rho + c_3\,\kappa\Delta p_3 + c_p\,\kappa\Delta\bar p}{H^2},\qquad
 \Delta\ln f = -\frac{\Delta K}{2K_*},\\
&\Delta\ln m_s = \frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}\,\Delta\ln f,\qquad
 \kappa\Delta\rho = 8\pi G_{\mathrm{N}}\,\mathcal{G}(K_*)\,\rho_4
\end{aligned} \tag{FE-80}
$$
<!-- symbols: Delta, Kblock, crho, kappa, rho, c3, p3, cp, pbar, Hconst, fblock, Kstar, mmass, is, diff, pi, GN, GK, rho4 -->

in which radiation drops out exactly ($c_3 = -3c_\rho$), so that only the trace $\rho - 3p_3$ and the hidden pressure act; the
hidden pressure is the response of the pressure to the block scale at fixed temperature (DERIVED)

$$
\bar p = -\frac14\sum_s\big(\rho_s - 3p_s\big)\frac{\mathrm{d}\ln m_s}{\mathrm{d}\ln f}
 - \frac14\,\Theta_{\mathrm{QCD}}\,\frac{\mathrm{d}\ln\Lambda_{\mathrm{QCD}}^{(N_{\mathrm{f}})}}{
 \mathrm{d}\ln f}
 + \frac14\,p_{\alpha,2}\,\frac{\mathrm{d}\ln\alpha_2}{\mathrm{d}\ln f} +
 \frac14\,p_{\alpha,1}\,\frac{\mathrm{d}\ln\alpha_1}{\mathrm{d}\ln f} \tag{FE-81}
$$
<!-- symbols: pbar, is, rho, pressure, diff, mmass, fblock, Theta, rhoQCDscale, palpha, alpha2, alpha1 -->

It shifts the block by at most $\Delta\ln f = 1.1\times10^{-34}$ (at the dark-matter freeze-out, pushed by the hot plasma, whose
hidden pressure $\bar p = 3.1\times10^{12}$ GeV$^4$ is mostly the QCD interaction measure; $10^{-62}$ in the Earth), and the loop
mass $\to$ source $\to$ block $\to$ mass has the gain $1.1\times10^{-33}$ at most, so the masses are fixed to that accuracy. The
plasma energy density at the freeze-out differs by 0.13 % between the ideal-gas thermal history and these block sources, which
include the trace anomaly by design (residual analysis). The block-shape source $p_0 - p_5$, which the order-0 metric cannot
absorb, is about 4 times the kept $\bar p$ for non-relativistic dark matter (residual analysis; OPEN), but it is suppressed like
$\bar p$ itself ($\kappa p/(\kappa\rho_{\mathrm{stab}}) \le 3\times10^{-32}$ at the freeze-out) if the shape mode is stable (OPEN).

The Kaluza-Klein gravitons, the terms $n \ge 1$ of the metric series, couple to a source through the overlap of its $x_0$
profile with theirs (DERIVED):

$$
\begin{aligned}
&F_n(\xi) = \mathrm{e}^{-3HL\xi/2}\Big(\cos\varpi_n\xi + \frac{3HL}{2\varpi_n}\sin\varpi_n\xi\Big),\qquad
 \varpi_n = \pi,\ 2\pi,\ 3\pi,\ \dots,\\
&\tilde m_n^2 = \frac{9H^2L^2}{4} + \varpi_n^2,\qquad m^{\mathrm{KK}}_n = \frac{\tilde m_n}{fL},\qquad
 N_n = \int_{-1}^{0}\mathrm{e}^{3HL\xi}F_n^2\,\mathrm{d}\xi = \frac12\Big(1 +
 \frac{9H^2L^2}{4\varpi_n^2}\Big),\qquad
 N_0 = \frac{1 - \mathrm{e}^{-3HL}}{3HL}
\end{aligned} \tag{FE-53}
$$
<!-- symbols: Fprof, in, xi, euler, Hconst, Lcut, varpi, pi, mtilde, mKK, fblock, Nnorm, diff -->

$$
V_{\mathrm{N}}(r) = -\frac{G_{\mathrm{N}}M_1M_2}{r}\Big[1 +
 \sum_{n\ge1}\mathcal{A}_n\,\mathrm{e}^{-m^{\mathrm{KK}}_nr}\Big],\qquad
\mathcal{A}_n = \frac{N_0}{N_n}\Big(\int_{-1}^{0}\varrho_1F_n\,\mathrm{d}\xi\Big)\Big(\int_{-1}^{0}
 \varrho_2F_n\,\mathrm{d}\xi\Big) \tag{FE-54}
$$
<!-- symbols: VN, rdist, GN, M12, in, calA, euler, mKK, Nnorm, varrho12, Fprof, diff, xi -->

Their profiles are orthogonal to the flat profile of the gauge zero modes in the measure $\mathrm{e}^{3HL\xi}$, so the gluon field
energy that makes up most of the nucleon mass excites none of them (DERIVED to $2\times10^{-10}$): gravity at short distances
feels only the localised quark and lepton zero modes. The first mode has $\mathcal{A}_1 = 0.0904$ between two masses with the
quark-doublet profile and $0.0208$ with the lepton-doublet profile, and the range $1/m_{\mathrm{KK}} = 1.63\times10^{-21}$ m:
$\mathrm{e}^{-m_{\mathrm{KK}}r} = \mathrm{e}^{-3.1\times10^{16}}$ at 50 micrometres, and Newton's law is exact at every measurable distance.

## A.10 Assessment of the mechanism {-}

The author's mechanism works in UM-2 in a precise sense: every mass is an $x_0$ eigenvalue, the period $\pi/(6H)$ is built into
every wave function, and the massless particles are exactly those protected by symmetry (the photon, the gluons, the
graviton and the fold bands of dirac16complex). The uncertainty relation, however, is the reason for the masses of the heavy
states only: for the Kaluza-Klein and odd excitations and for the dark matter the author's estimate $m_{\mathrm{Heis}}$ lies below
the mass (by factors 2.3 to 7.5). The light masses need two ingredients that are not consequences of the uncertainty
relation: exact chiral zero modes, whose hidden kinetic energy is cancelled exactly, and the tip of the cell, where the
electroweak symmetry is broken by the sigma field and the zero modes are mixed. Their overlap at the tip,
$\mathcal{Z}(c)^2 \simeq 2c\,\mathrm{e}^{-2c}$, produces the hierarchy of the twelve fermion masses, fourteen orders of magnitude from
$\nu_1$ to the top quark, from bulk masses between $5.2H$ and $54.2H$ in magnitude; a sharper localisation gives a lighter
fermion, the reverse of the Heisenberg intuition. The mixing matrices are tip matrices and are not explained by the mechanism.
The scales are not free: once the Kaluza-Klein scale is fitted ($m_{\mathrm{KK}} = 121.3$ TeV from $\rho_{\mathrm{EW},0}$), the
dark-matter mass ($44.35$ TeV) and the radion mass ($48.4$ TeV) follow. Three further results: the nucleon mass, the bulk of the
visible mass, depends on the block through the QCD scale more strongly than any $x_0$ eigenvalue ($-46.1$); the mechanism favours
Dirac over Majorana neutrinos; and in the coupled solution every back-reaction on the masses (the Standard-Model mean fields
on dirac16complex, dirac16complex on the gauge couplings, all species on the block) stays below $1.5\times10^{-6}$, so the $x_0$
spectra of the static block are the masses of the solution.

# B. dirac16complex as dark matter and as dark energy {-}

## B.1 The candidate (DERIVED, conditional) {-}

dirac16complex is the 16-component complex spinor field of the record, with the action (RECORD)

$$
\begin{aligned}
S_\Psi &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\tfrac12\big(\bar\Psi\gamma^MD_M\Psi
 - (D_M\bar\Psi)\gamma^M\Psi\big) - m_\Psi\,\bar\Psi\Psi - \frac{\lambda}{2}\big(\bar\Psi\Psi\big)^2\Big],\\
m_\Psi &= 3H\mathcal{M} = H\qquad (\mathcal{M} = 1/3)
\end{aligned} \tag{IN-5}
$$
<!-- symbols: SPsi, diff, Xcoord, metric, Psi, gamma, iM, Dcov, mPsi, lambda, Hconst, calM -->

in the Clifford algebra of the author, with the Dirac adjoint and the two halves of the field (AUTHOR)

$$
\begin{aligned}
&\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
 \eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1),\qquad \gamma^M = \mathbf{e}_a{}^M\gamma^a,\\
&\bar\Psi = \Psi^\dagger C,\qquad C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3},\qquad
 \Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4},\qquad \mathcal{B} =
 -\mathrm{i}C\gamma^{x_4},\\
&\Psi = \Psi_A + \Psi_B,\qquad \mathcal{B}\Psi_A = -\Psi_A,\qquad \mathcal{B}\Psi_B = +\Psi_B
\end{aligned} \tag{IN-6}
$$
<!-- symbols: gamma, ia, ib, eta, identity, diag, iM, vielbein, Psi, dagger, Cmat, x0, x1, x2, x3, Gamma4, imag, x4, calB, PsiAB -->

Its field equation, with the canonical spin connection and the three portals to the Standard Model, is (DERIVED)

$$
\gamma^MD_M\Psi = \Big[m_\Psi + \lambda\,\bar\Psi\Psi + \frac{\mathcal{F}}{\Lambda_\star^3}\Big]\Psi
 - \mathrm{i}\,\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,J^{B-L}_M\gamma^M\Psi
 - \mathrm{i}\,\frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{M\ne x_0}J^{B}_M\gamma^MP_b\Psi \tag{FE-12}
$$
<!-- symbols: gamma, iM, Dcov, Psi, mPsi, lambda, calF, LambdaStar, imag, cV, JBL, cA, x0, JB, Pab -->

and on the order-0 metric the spin connection enters through (DERIVED, exact for every $a_4$, $b_4$ and on both halves)

$$
\gamma^M\Omega_M = \frac32\,\frac{H}{f}\,\gamma^{x_0} + \Big(\frac{\dot b_4}{b_4} - \frac{\dot
 a_4}{2}\Big)\gamma^{x_4} \tag{FE-13}
$$
<!-- symbols: gamma, iM, Omega, Hconst, fblock, x0, b4dot, b4, a4dot, x4 -->

which contains $\gamma^{x_0}$ and $\gamma^{x_4}$ only. $\mathcal{B}$ commutes with $C$, with $\gamma^a$ and with $C\gamma^a$ for the
directions $x_0, \dots, x_4$, and anticommutes with them for $x_5, x_6, x_7$ (DERIVED with the author's matrices): in the good
sector (no extra-time momenta) every term of UM-2 commutes with $\mathcal{B}$, so the numbers of quanta of $\Psi_A$ and of $\Psi_B$
are separately conserved. The four-dimensional chirality projector is (DERIVED)

$$ P_L = \frac{1 + \Gamma_4}{2} = \frac{1 - \mathcal{B}\gamma^{x_0}}{2} $$
<!-- symbols: PLR, iL, Gamma4, calB, gamma, x0 -->

since $\Gamma_4 = -\mathcal{B}\gamma^{x_0}$. Every orbital obeys the tip condition $(1 - \gamma^{x_0})\Psi = 0$, so $P_L$ annihilates every
$\Psi_B$ orbital at the tip, while a $\Psi_A$ orbital has a non-zero chiral tip charge density ($0.257$ for the lightest odd state).
UM-2 contains no tip operator (the chiral tip $Z$ portal of version 1 is removed), so neither half is reached at the tip. The
dark-matter candidate is the lightest odd state of each half, from the exact spectrum, written out again:

$$
\begin{aligned}
&\text{even: }\chi = \big(\mathrm{e}^{c_\Psi\xi},\ 0\big)^T,\ \varepsilon = 0\ \text{(all eight
 blocks)},\qquad
 \varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi_n}{fL}\Big)^2},\ \varpi_n = \pi,\ 2\pi,\ \dots;\\
&\text{odd: }\varepsilon = \pm\sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2},\quad \tan\varpi =
 -\frac{\varpi}{c_\Psi};\qquad
 c_\Psi = f\,m_\Psi L;\qquad \text{fold band: }\varepsilon = \mathrm{e}^{-a_4}\lvert k\rvert
\end{aligned} \tag{FE-62}
$$
<!-- symbols: chi, euler, cPsi, xi, transpose, varepsilon, mPsi, varpi, in, fblock, Lcut, pi, a4, kwave -->

* two Dirac fermions (the lowest odd level of $\Psi_A$ and of $\Psi_B$, the same orbital in all eight blocks, degenerate) of the
  mass

$$ M_{\mathrm{DM}} = \varepsilon_{\mathrm{DM}} = \sqrt{m_\Psi^2 + \Big(\frac{\varpi}{fL}\Big)^2} = 3.102204\,m_\Psi = 44.35\ \text{TeV},\qquad \varpi = 1.89901,\qquad m_\Psi = H; $$
<!-- symbols: MDM, epsDM, mPsi, varpi, fblock, Lcut, Hconst -->

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

$$
\begin{aligned}
S_{\mathrm{I11}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,
 \big(\mathrm{i}\bar\Psi\gamma^M\Psi\big)\,J^{B-L}_M,\qquad
 J^{B-L}_M = \sum_{i=1}^{3}\sum_{\psi} q_\psi\,\big(\mathrm{i}\bar\psi_i\gamma_M\psi_i\big),\\
q_Q &= q_{u_R} = q_{d_R} = \frac13,\qquad q_\ell = q_{e_R} = q_{\nu_R} = -1
\end{aligned} \tag{IN-16}
$$
<!-- symbols: SI11, diff, Xcoord, metric, cV, LambdaStar, imag, Psi, gamma, iM, JBL, ii, ipsi, qBL, psi -->

I12, the gauge-kinetic scalar portal:

$$
S_{\mathrm{I12}} = -\int\mathrm{d}^8X\,\sqrt{\lvert
 g\rvert}\;\frac{\bar\Psi\Psi}{\Lambda_\star^3}\,\mathcal{F},\qquad
\mathcal{F} = c_{\mathrm{G}}\,G^A_{MN}G^{AMN} + c_{\mathrm{W}}\,W^I_{MN}W^{IMN} +
 c_{\mathrm{B}}\,B_{MN}B^{MN} \tag{IN-17}
$$
<!-- symbols: SI12, diff, Xcoord, metric, Psi, LambdaStar, calF, cG, Ggluon, iA, iM, iN, cW, Wsu2, iI, cB, Bhyp -->

I13, the $x_0$-chiral vector portal to the baryon-number current:

$$
\begin{aligned}
S_{\mathrm{I13}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{A}}}{\Lambda_\star^6}
 \sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma^MP_b\Psi\big)\,J^{B}_M,\qquad P_b = \frac{1 - \gamma^{x_0}}{2},
 \qquad P_a = \frac{1 + \gamma^{x_0}}{2},\\
J^{B}_M &= \frac13\sum_{i=1}^{3}\big(\mathrm{i}\bar Q_i\gamma_MQ_i + \mathrm{i}\bar u_{Ri}\gamma_Mu_{Ri}
 + \mathrm{i}\bar d_{Ri}\gamma_Md_{Ri}\big)
\end{aligned} \tag{IN-18}
$$
<!-- symbols: SI13, diff, Xcoord, metric, cA, LambdaStar, iM, x0, imag, Psi, gamma, Pab, JB, ii, Qdoublet, uR, dR -->

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

$$
\begin{aligned}
&\mathcal{L}_4 = \big(G_{\mathrm{V}}\,q_f\,\tilde I_{of} + G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of}\big)
 \big(\mathrm{i}\bar\Psi_o\gamma^\mu\Psi_o\big)\big(\mathrm{i}\bar\psi_f\gamma_\mu\psi_f\big),\\
&\tilde I_{of} = \frac{1}{H}\int_{-L}^{0}\big(a_o^2 +
 b_o^2\big)\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 \tilde I^{(b)}_{of} = \frac{1}{H}\int_{-L}^{0}b_o^2\,\varrho_f\,\mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 G_{\mathrm{V}} = \frac{c_{\mathrm{V}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\qquad
 G_{\mathrm{A}} = \frac{c_{\mathrm{A}}H}{2f^4v_{\mathrm{t}}\Lambda_\star^6},\\
&n_{\psi i}(y) = \frac{n_f\,\varrho_f(y)\,\mathrm{e}^{-3Hy}}{2f^4v_{\mathrm{t}}},\qquad
 \varrho(y; c) = \frac{2c}{L}\,\frac{\mathrm{e}^{2cy/L}}{1 - \mathrm{e}^{-2c}}
\end{aligned} \tag{FE-70}
$$
<!-- symbols: L4, GV, qBL, if, tildeI, io, GA, qB, tildeIb, imag, Psi, gamma, imu, psi, Hconst, Lcut, ab, varrho, euler, ycoord, diff, cV, fblock, vt, LambdaStar, cA, ndens, ipsi, ii, cloc -->

$$
\begin{aligned}
&\mathcal{L}_4^{\mathrm{I12}} =
 -\mathcal{O}_{\mathrm{DM}}\,\frac{\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{DM}}}{\Lambda_\star^3}
 \big(c_{\mathrm{G}}\,G^A_{\mu\nu}G^{A\mu\nu} + c_{\mathrm{W}}\,W^I_{\mu\nu}W^{I\mu\nu} +
 c_{\mathrm{B}}\,B_{\mu\nu}B^{\mu\nu}\big),\qquad
 \mathcal{O}_{\mathrm{DM}} = \frac{\partial\varepsilon_{\mathrm{DM}}}{\partial m_\Psi},\\
&G_{\mathrm{g}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{G}}\,g_3^2}{\Lambda_\star^3},\qquad
 G_{\mathrm{W}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{W}}\,g_2^2}{\Lambda_\star^3},\qquad
 G_{\mathrm{B}} = \mathcal{O}_{\mathrm{DM}}\,\frac{c_{\mathrm{B}}\,g_1^2}{\Lambda_\star^3}
\end{aligned} \tag{FE-71}
$$
<!-- symbols: L4I12, calO, PsiDM, LambdaStar, cG, Ggluon, iA, imu, inu, cW, Wsu2, iI, cB, Bhyp, partial, epsDM, mPsi, Gg, g3, GW, g2, GB, g1 -->

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

$$
\rho_s = \frac{d_s}{2\pi^2}\int_0^\infty\frac{k^2E\,\mathrm{d}k}{\mathrm{e}^{E/T} \pm 1},\qquad
p_s = \frac{d_s}{6\pi^2}\int_0^\infty\frac{k^4\,\mathrm{d}k}{E\,(\mathrm{e}^{E/T} \pm 1)},\qquad
s_s = \frac{\rho_s + p_s}{T},\qquad E = \sqrt{k^2 + m_s^2} \tag{FE-121}
$$
<!-- symbols: rho, is, ddeg, pi, infty, kwave, Eenergy, diff, euler, Temp, pressure, sentropy, mmass -->

which give the degrees of freedom and the Hubble rate of the hot Universe

$$
g_\rho = \frac{30}{\pi^2T^4}\sum_s\rho_s,\qquad g_s = \frac{45}{2\pi^2T^3}\sum_s s_s,\qquad
\mathcal{H} = \Big(\frac{8\pi^3g_\rho}{90}\Big)^{1/2}\frac{T^2}{M_{\mathrm{Pl}}} \tag{FE-122}
$$
<!-- symbols: grho, pi, Temp, is, rho, sentropy, Hubble, MPl -->

with the QCD crossover, the neutrino temperature after decoupling and the cooling of the plasma (the crossover model ASSUMED)

$$
w_{\mathrm{QGP}}(T) = \frac12\Big[1 + \tanh\frac{T - T_{\mathrm{c}}}{T_{\mathrm{w}}}\Big],\qquad
\frac{T_\nu}{T} = \Big(\frac{g_{s,e\gamma}(T)}{11/2}\Big)^{1/3},\qquad
\frac{\mathrm{d}\ln T}{\mathrm{d}x_4} = -\frac{\mathcal{H}}{1 + \frac13\,\mathrm{d}\ln g_s/\mathrm{d}\ln
 T} \tag{FE-123}
$$
<!-- symbols: wQGP, Temp, Tcw, Tnu, gseg, diff, x4, Hubble, grho -->

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

$$
\begin{aligned}
&\frac{\mathrm{d}n_{\mathrm{DM}}}{\mathrm{d}x_4} + 3\mathcal{H}n_{\mathrm{DM}}
 = -\langle\sigma v_{\mathrm{rel}}\rangle\big(n_{\mathrm{DM}}\bar n_{\mathrm{DM}} -
 n_{\mathrm{DM,eq}}^2\big)\ \Rightarrow
 \frac{\mathrm{d}Y_{\mathrm{DM}}}{\mathrm{d}x} = -\Big(1 + \frac13\frac{\mathrm{d}\ln g_s}{\mathrm{d}\ln
 T}\Big)
 \frac{s\,\langle\sigma v_{\mathrm{rel}}\rangle}{2x\mathcal{H}}\big(Y_{\mathrm{DM}}^2 -
 Y_{\mathrm{eq}}^2\big),\\
&Y_{\mathrm{DM}} = \frac{n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}}{s},\qquad x =
 \frac{M_{\mathrm{DM}}}{T},\qquad
 s = \frac{2\pi^2}{45}\,g_sT^3,\qquad Y_{\mathrm{eq}} = \frac{4M_{\mathrm{DM}}^2TK_2(x)}{2\pi^2s}
\end{aligned} \tag{FE-124}
$$
<!-- symbols: diff, nDM, x4, Hubble, sigmaxs, vrel, nDMeq, Yabund, xMT, grho, Temp, sentropy, MDM, pi, Kbessel -->

with the relativistic thermal average (Gondolo and Gelmini)

$$
\langle\sigma v_{\mathrm{rel}}\rangle =
 \frac{1}{8M_{\mathrm{DM}}^4TK_2(x)^2}\int_{4M_{\mathrm{DM}}^2}^{\infty}\sigma\,
 \big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)\,E_{\mathrm{cm}}\,K_1\Big(\frac{E_{\mathrm{cm}}}{T}\Big)\,
 \mathrm{d}\big(E_{\mathrm{cm}}^2\big) \tag{FE-125}
$$
<!-- symbols: sigmaxs, vrel, MDM, Temp, Kbessel, xMT, infty, Ecm, diff -->

and the relic density

$$
\Omega_{\mathrm{DM}}h_{100}^2 = \frac{M_{\mathrm{DM}}\,Y_\infty\,s_0}{\rho_{\mathrm{crit}}/h_{100}^2},\qquad
\frac{\rho_{\mathrm{crit}}}{h_{100}^2} = 1.05368\times10^{-5}\ \text{GeV}/\text{cm}^3 \tag{FE-126}
$$
<!-- symbols: OmegaDM, h100, MDM, Yabund, s0, rhocrit -->

The annihilation cross-sections through I12 and I13 and their partial-wave unitarity bounds are

$$
\begin{aligned}
&\sigma_{\mathrm{I12}} = \frac{G_{\mathrm{I12}}^2\,E_{\mathrm{cm}}^3\big(E_{\mathrm{cm}}^2 -
 4M_{\mathrm{DM}}^2\big)^{1/2}}{8\pi},\qquad
 G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2,\\
&\sigma_{\mathrm{I13}} = \sum_f\frac{N_{\mathrm{c}}\,G_f^2\,E_{\mathrm{cm}}^2\big(1 +
 2M_{\mathrm{DM}}^2/E_{\mathrm{cm}}^2\big)}{24\pi\beta_{\mathrm{cm}}},
 \qquad G_f = G_{\mathrm{A}}\,q^{B}_f\,\tilde I^{(b)}_{of},\\
&\beta_{\mathrm{cm}} = \sqrt{1 - \frac{4M_{\mathrm{DM}}^2}{E_{\mathrm{cm}}^2}},\qquad
 k_{\mathrm{cm}} = \sqrt{\frac{E_{\mathrm{cm}}^2}{4} - M_{\mathrm{DM}}^2}
\end{aligned} \tag{FE-127}
$$
<!-- symbols: sigmaI1213, GI12, Ecm, MDM, pi, Gg, GW, GB, if, Nc, Gf, betacm, GA, qB, tildeIb, io, kcm -->

$$
\sigma_{\mathrm{I12}} \le \frac{\pi}{4k_{\mathrm{cm}}^2}\ \ \text{(total angular momentum 0)},\qquad
\sigma_{\mathrm{I13}} \le \frac{3\pi}{4k_{\mathrm{cm}}^2}\ \ \text{(total angular momentum 1)} \tag{FE-128}
$$
<!-- symbols: sigmaI1213, pi, kcm -->

where the effective cross-section exceeds its bound, it is replaced by the bound (a unitarity-respecting completion that saturates
it). The machinery is checked against the freeze-out formula (STANDARD, Kolb and Turner, for a Dirac fermion with
$\langle\sigma v_{\mathrm{rel}}\rangle = a_{\mathrm{sw}} + 6b_{\mathrm{pw}}/x$)

$$ x_{\mathrm{f}} = \ln\Big[0.095\,\frac{M_{\mathrm{Pl}}M_{\mathrm{DM}}\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}})}{\sqrt{g_\rho x_{\mathrm{f}}}}\Big],\qquad \Omega_{\mathrm{DM}}h_{100}^2 = \frac{2\times1.07\times10^9\,\text{GeV}^{-1}\,x_{\mathrm{f}}}{\sqrt{g_\rho}\,M_{\mathrm{Pl}}\,\big(a_{\mathrm{sw}} + 3b_{\mathrm{pw}}/x_{\mathrm{f}}\big)} $$
<!-- symbols: sol_xf, MPl, MDM, sigmaxs, vrel, grho, OmegaDM, h100, ana_swpw -->

($0.095 = 0.038\times\frac12(\frac12 + 2)\times2$: the matching constant $\frac12$ and the two internal states of a Dirac fermion;
$M_{\mathrm{Pl}} = 1.22091\times10^{19}$ GeV): an s-wave cross-section of $4.4\times10^{-26}$ cm$^3$/s gives $\Omega_{\mathrm{DM}}h_{100}^2 = 0.1275$
from the Boltzmann equation and $0.1306$ from the formula, and the late-time integral of the Boltzmann equation is reproduced to
$1.3\times10^{-8}$.

### I12 alone violates unitarity (DERIVED) {-}

The I12 cross-section of (FE-127) is p-wave:

$$ \sigma_{\mathrm{I12}}v_{\mathrm{rel}} = \frac{G_{\mathrm{I12}}^2E_{\mathrm{cm}}^2\big(E_{\mathrm{cm}}^2 - 4M_{\mathrm{DM}}^2\big)}{4\pi} \to \frac{G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4v_{\mathrm{rel}}^2}{\pi},\qquad a_{\mathrm{sw}} = 0,\qquad b_{\mathrm{pw}} = \frac{G_{\mathrm{I12}}^2M_{\mathrm{DM}}^4}{\pi} $$
<!-- symbols: sigmaI1213, vrel, GI12, Ecm, MDM, pi, ana_swpw -->

(each of the $8 + 3 + 1$ abelian channels of the gluon, $W$ and $B$ fields contributes with its own coupling, which add up to
$G_{\mathrm{I12}}^2 = 8G_{\mathrm{g}}^2 + 3G_{\mathrm{W}}^2 + G_{\mathrm{B}}^2$). With the freeze-out formula ($g_\rho = 105.75$ at
$T \approx 1.5$ TeV) the relic $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ per species requires $x_{\mathrm{f}} = 30.38$,
$\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 2.01\times10^{-25}$ cm$^3$/s and $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$ (a single species
carrying all the dark matter would need $(17.6\ \text{TeV})^{-3}$). But the operator annihilates a fermion pair only from the state
with total angular momentum 0 and positive parity, $^3P_0$, whose partial-wave bound (FE-128), averaged over the four spin states
of an unpolarised Dirac pair and with $k_{\mathrm{cm}} = M_{\mathrm{DM}}v_{\mathrm{rel}}/2$ ($v_{\mathrm{rel}} \ll 1$), gives

$$ \sigma_{\mathrm{I12}}v_{\mathrm{rel}} \le \frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}},\qquad \Big\langle\frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}}\Big\rangle = \frac{\int_0^\infty\frac{\pi}{M_{\mathrm{DM}}^2v_{\mathrm{rel}}}\,v_{\mathrm{rel}}^2\,\mathrm{e}^{-xv_{\mathrm{rel}}^2/4}\,\mathrm{d}v_{\mathrm{rel}}}{\int_0^\infty v_{\mathrm{rel}}^2\,\mathrm{e}^{-xv_{\mathrm{rel}}^2/4}\,\mathrm{d}v_{\mathrm{rel}}} = \frac{\sqrt{\pi x}}{M_{\mathrm{DM}}^2} $$
<!-- symbols: sigmaI1213, vrel, pi, MDM, infty, euler, xMT, diff -->

i.e. $5.79\times10^{-26}$ cm$^3$/s at $x_{\mathrm{f}} = 30.38$ (the thermal average over the non-relativistic distribution of the relative
velocity, checked by numerical averaging). The freeze-out requirement exceeds the bound 3.47 times, and the effective cross-section
at the relic strength exceeds the bound above

$$ v_{\mathrm{c}} = \Big(\frac{\pi}{G_{\mathrm{I12}}M_{\mathrm{DM}}^3}\Big)^{2/3} = 0.263, $$
<!-- symbols: sol_vc, pi, GI12, MDM -->

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
<!-- symbols: GI12, pi, MDM -->

(below the bound up to $E_{\mathrm{cm}} = 2.40\,M_{\mathrm{DM}}$; alone it would leave $\Omega_{\mathrm{DM}}h_{100}^2 = 8.0$ per species; with
universal coefficients and the one-loop couplings at $2M_{\mathrm{DM}}$ it means $c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$
GeV$^{-3}$, i.e. $\Lambda_\star/c_{\mathrm{I12}}^{1/3} = 44.9$ TeV, and $G_{\mathrm{g}}$, $G_{\mathrm{W}}$, $G_{\mathrm{B}} = 6.09$, $2.96$,
$1.08\times10^{-15}$ GeV$^{-3}$).

### The relic with I13 (DERIVED) {-}

Through I13 the dark matter annihilates in the s-wave ($^3S_1$) into quark pairs, with $G_f = G_{\mathrm{A}}q^B_f\tilde I^{(b)}_{of}$ for each
quark Weyl component of (FE-127) ($\sum_fN_{\mathrm{c}}(q^B_f\tilde I^{(b)}_{of})^2 = 16.351$). The Boltzmann equation with the cross-sections of
I12 (benchmark) and I13 gives each species $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ for

$$ G_{\mathrm{A}} = 1.278\times10^{-9}\ \text{GeV}^{-2} = 1.1\times10^{-4}\,G_{\mathrm{F}},\qquad x_{\mathrm{f}} = 31.23 $$
<!-- symbols: GA, GF, sol_xf -->

($T = M_{\mathrm{DM}}/x_{\mathrm{f}} = 1.42$ TeV), with $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 9.50\times10^{-26}$ cm$^3$/s from I13 and
$9.9\times10^{-28}$ cm$^3$/s from I12, the I13 cross-section capped at its $J = 1$ bound $3\pi/(4k_{\mathrm{cm}}^2)$, which it reaches only
above $v_{\mathrm{rel}} = 0.51$: 21.7 % of the freeze-out rate comes from collisions at the bound and 78 % from collisions below it
(without the cap $G_{\mathrm{A}} = 1.269\times10^{-9}$ GeV$^{-2}$, and the uncapped cross-section would exceed the bound above
$v_{\mathrm{rel}} = 0.52$, for 25 % of the rate). The relic of UM-2 is therefore a thermal freeze-out with most annihilations
perturbative. The contact form of I13 is an effective description (for the quark doublet
$G_f^{-1/2} = (G_{\mathrm{A}}q^B_f\tilde I^{(b)}_{of})^{-1/2} = 30$ TeV, below the energies $E_{\mathrm{cm}} \approx 89$ TeV of the
annihilations), whose completion by a mediator is OPEN.

**Accuracy of the relic (residual analysis).** Re-solving the Boltzmann equation at the stored $G_{\mathrm{A}}$ gives
$\Omega_{\mathrm{DM}}h_{100}^2 = 0.0600000002$ (late-time identity $6.1\times10^{-9}$), and the relic agrees with the $\Omega_{\mathrm{c}}h_{100}^2$ of the
CMB computation to $3.1\times10^{-9}$ (DERIVED). The neglected physics is larger. The ideal-gas thermal history leaves out the
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

$$
\begin{aligned}
&G_{\mathrm{A}}^{B-L} = G_{\mathrm{A}}\Big[\frac{\mathcal{S}_B}{\mathcal{S}_{B-L}}\Big]^{1/2},\qquad
 \mathcal{S}_B = \sum_fN_{\mathrm{c}}\big(q^{B}_f\tilde I^{(b)}_{of}\big)^2,\qquad
 \mathcal{S}_{B-L} = \sum_fN_{\mathrm{c}}\big(q_f\tilde I^{(b)}_{of}\big)^2,\\
&\frac{\mathrm{d}n_{\nu_R}}{\mathrm{d}x_4} + 3\mathcal{H}n_{\nu_R} = \Gamma_\nu\Big(1 -
 \frac{n_{\nu_R}^2}{(n_{\nu_R}^{\mathrm{eq}})^2}\Big),\qquad
 \Gamma_\nu = 2\,n_{\mathrm{DM,eq}}\,\bar n_{\mathrm{DM,eq}}\,\frac{G_\nu^2M_{\mathrm{DM}}^2}{2\pi},\qquad
 G_\nu = G_{\mathrm{A}}^{B-L}\,\tilde I^{(b)}_{\nu_R},\\
&n_{\nu_R}^{\mathrm{eq}} = \frac34\,\frac{\zeta(3)}{\pi^2}\,T^3,\qquad
 n_{\mathrm{DM,eq}} = \bar n_{\mathrm{DM,eq}} = 2\Big(\frac{M_{\mathrm{DM}}T}{2\pi}\Big)^{3/2}\mathrm{e}^{-x}
\end{aligned} \tag{FE-131}
$$
<!-- symbols: GABL, GA, SB, if, Nc, qB, tildeIb, io, qBL, diff, nnuR, x4, Hubble, Gammanu, nDMeq, Gnu, MDM, pi, zeta3, Temp, euler, xMT -->

while elastic scattering on the dark matter keeps them at the plasma temperature as long as

$$
\Gamma_{\mathrm{el}} = 2\big(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}}\big)\,\sigma_{\mathrm{el}} >
 \mathcal{H},\qquad
\sigma_{\mathrm{el}} = \frac{G_\nu^2E^2}{2\pi},\qquad E \simeq 3T \tag{FE-132}
$$
<!-- symbols: Gammael, nDM, Hubble, Gnu, Eenergy, pi, Temp -->

and a species of $N_{\mathrm{W}}$ Weyl fermions that stays in equilibrium until the plasma has $g_s$ entropy degrees of freedom adds

$$
\Delta N_{\mathrm{eff}} = N_{\mathrm{W}}\Big(\frac{10.75}{g_s}\Big)^{4/3}F_{\mathrm{h}},\qquad
F_{\mathrm{h}} = \Big[\frac{T_\nu}{T_\gamma}\Big(\frac{11}{4}\Big)^{1/3}\Big/\big(1 + h_\nu\big)\Big]^4
 = 1.0095 \tag{FE-133}
$$
<!-- symbols: Delta, Neff, NW, grho, Fh, Tnu, Tgamma, hnu -->

With the $B - L$ current $\mathcal{S}_{B-L} = 22.92$ (the three right-handed neutrinos carry 1.2 % of the annihilation) and
$G_{\mathrm{A}}^{B-L} = 1.072\times10^{-9}$ GeV$^{-2}$ (from the uncapped $G_{\mathrm{A}}$); the right-handed neutrinos would reach 0.9997 of
the equilibrium number by $x = 40$, the number-changing rate would fall below $\mathcal{H}$ at $x = 16.1$, elastic scattering would keep
them coupled until $x = 24.4$ ($T = 1.82$ TeV, $g_s = 105.7$), and they would decouple as $N_{\mathrm{W}} = 3$ Weyl species adding
$\Delta N_{\mathrm{eff}} = 0.144$, i.e. $N_{\mathrm{eff}} = 3.19$, 2.5 standard deviations above the ACT DR6 value $2.86 \pm 0.13$. With the
baryon-number current the right-handed neutrinos keep only their tip coupling and their I11 coupling (charge $-1$), through which
they are produced at the fraction

$$
r_{\nu_R} = \frac{G_{\mathrm{V}}^2\sum_{i=1}^{3}\tilde I_{\nu_R,i}^2}{G_{\mathrm{A}}^2\,\mathcal{S}_B}
 \tag{FE-134}
$$
<!-- symbols: rnuR, GV, ii, tildeI, GA, SB -->

$r_{\nu_R} = 2.0\times10^{-17}$ of the I13 annihilation rate into quarks: they are never thermalised.

## B.4 Direct and indirect detection {-}

**Through I12 (ESTIMATE, version 2).** In the geometric normalisation of the gluon field the trace anomaly of QCD gives the
matrix element of $G^A_{\mu\nu}G^{A\mu\nu}$ in a nucleon, and with (FE-71) the scalar coupling of the dark matter to a nucleon and its
spin-independent cross-section:

$$ \langle\mathrm{N}\rvert G^A_{\mu\nu}G^{A\mu\nu}\lvert\mathrm{N}\rangle = -g_3^2\,\frac{8\pi}{9\alpha_3}\,m_{\mathrm{N}}f_{\mathrm{TG}} = -\frac{32\pi^2}{9}\,m_{\mathrm{N}}f_{\mathrm{TG}},\qquad f_{\mathrm{N}} = G_{\mathrm{g}}\,\frac{8\pi}{9\alpha_3}\,m_{\mathrm{N}}f_{\mathrm{TG}},\qquad \sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi} $$
<!-- symbols: ana_Nstate, Ggluon, iA, imu, inu, g3, pi, alpha3, sol_mN, sol_fTG, sol_fN, Gg, sol_sigmaSI, sol_mured -->

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
<!-- symbols: sol_Gud, GA, tildeIb, GV, tildeI -->

and the couplings to a proton, a neutron and a xenon nucleus, and the cross-section per nucleon, are

$$ f_{\mathrm{p}} = 2G_{\mathrm{u}} + G_{\mathrm{d}},\qquad f_{\mathrm{n}} = G_{\mathrm{u}} + 2G_{\mathrm{d}},\qquad f_{\mathrm{N}} = \frac{Z_{\mathrm{Xe}}f_{\mathrm{p}} + (A_{\mathrm{Xe}} - Z_{\mathrm{Xe}})f_{\mathrm{n}}}{A_{\mathrm{Xe}}},\qquad \sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2f_{\mathrm{N}}^2}{\pi} $$
<!-- symbols: sol_fN, sol_Gud, sol_ZAXe, sol_sigmaSI, sol_mured, pi -->

with $Z_{\mathrm{Xe}} = 54$, $A_{\mathrm{Xe}} = 131$: $f_{\mathrm{p}} = 1.915\times10^{-9}$ GeV$^{-2}$, $f_{\mathrm{n}} = 1.917\times10^{-9}$ GeV$^{-2}$ and
$\sigma_{\mathrm{SI}} = 4.01\times10^{-46}$ cm$^2$, 0.16 of the extrapolated LZ limit (I11 alone would give $3.9\times10^{-60}$ cm$^2$): the dark matter
of UM-2 is allowed and testable by the next generation of xenon detectors (an exposure about six times that of LZ).

**Indirect detection (DERIVED).** The I12 annihilation is p-wave, suppressed by $v_{\mathrm{rel}}^2 \sim 10^{-6}$ in galaxies today; the I13
annihilation is s-wave and continues today, per pair of particle and antiparticle, into quark pairs with

$$ \sigma_{\mathrm{I13}}v_{\mathrm{rel}} = \sum_f\frac{N_{\mathrm{c}}G_f^2M_{\mathrm{DM}}^2}{2\pi} = 9.76\times10^{-26}\ \text{cm}^3/\text{s}\qquad (v_{\mathrm{rel}} \to 0), $$
<!-- symbols: sigmaI1213, vrel, if, Nc, Gf, MDM, pi -->

the thermal value for a heavy relic. **Colliders:** 44 TeV is beyond the reach of present and planned colliders.

## B.5 The self-interaction bound {-}

The contact self-interaction of (IN-5) contains a four-dimensional term that couples a dark-matter pair to a fold-band pair
through the transition scalar density of the two orbitals; $n^{\mathrm{sc}}_{\mathrm{DF}}$ is odd under the fold reflection and its square
even, so the dark matter can annihilate into the fold bands (ESTIMATE for the cross-section, whose Fierz coefficients are not
computed):

$$
\begin{aligned}
&\mathcal{L}_4^{\lambda} =
 -\lambda\,\big(\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{fold}}\big)\big(\bar\Psi_{\mathrm{fold}}\Psi_{
 \mathrm{DM}}\big)
 \big(n^{\mathrm{sc}}_{\mathrm{DF}}\big)^2,\qquad n^{\mathrm{sc}}_{\mathrm{DF}} =
 a_{\mathrm{DM}}b_{\mathrm{fold}} + b_{\mathrm{DM}}a_{\mathrm{fold}},
 \qquad b_{\mathrm{fold}} = 0,\\
&G_\lambda = \frac{\lambda H\tilde I_\lambda}{2f^4v_{\mathrm{t}}},\qquad
 \tilde I_\lambda = \frac{1}{H}\int_{-L}^{0}\big(n^{\mathrm{sc}}_{\mathrm{DF}}\big)^2\,
 \mathrm{e}^{-3Hy}\,\mathrm{d}y,\qquad
 \sigma_\lambda v_{\mathrm{rel}} = \frac{G_\lambda^2M_{\mathrm{DM}}^2}{2\pi}\ \ \text{(per final fold
 species)}
\end{aligned} \tag{FE-135}
$$
<!-- symbols: L4lam, lambda, PsiDM, Psifold, nscDF, abDM, abfold, Glam, Hconst, Ilam, fblock, vt, Lcut, euler, ycoord, diff, sigmalam, vrel, MDM, pi -->

While the dark matter is in equilibrium, from $T_{\mathrm{max}} = 10$ TeV (ASSUMED) to the freeze-out, each annihilation puts
$2M_{\mathrm{DM}}$ into the fold bands:

$$
\frac{\mathrm{d}\big(\rho_{\mathrm{fold}}\,\mathrm{e}^{4a_4}\big)}{\mathrm{d}x_4} =
 2M_{\mathrm{DM}}\,\Gamma_\lambda\,\mathrm{e}^{4a_4},\qquad
\Gamma_\lambda = 2\,n_{\mathrm{DM,eq}}\,\bar n_{\mathrm{DM,eq}}\,\sigma_\lambda
 v_{\mathrm{rel}}\,N_{\mathrm{fold}},\qquad
\frac{2\Gamma_\lambda}{n_{\mathrm{fold,eq}}\,\mathcal{H}} \ll 1 \tag{FE-136}
$$
<!-- symbols: diff, rhofold, euler, a4, x4, MDM, Gammalam, nDMeq, sigmalam, vrel, Nfold, nfoldeq, Hubble -->

which gives $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$ as long as the fold bands stay out of equilibrium (DERIVED; the
re-integration of the residual analysis agrees to $1.1\times10^{-5}$), with $\tilde I_\lambda = 14.38$. $\Delta N_{\mathrm{eff}} \le 0.001$ therefore
requires

$$ G_\lambda \le 2.3\times10^{-15}\ \text{GeV}^{-2} = 1.8\times10^{-6}\,G_{\mathrm{A}},\qquad \frac{2\Gamma_\lambda}{n_{\mathrm{fold,eq}}\mathcal{H}} \le 0.027 $$
<!-- symbols: Glam, GA, Gammalam, nfoldeq, Hubble -->

(ASSUMED bound of UM-2). If the fold bands were kept in equilibrium, they would decouple as four Weyl species, with the extra
radiation, written out again,

$$
\Delta N_{\mathrm{eff}} = N_{\mathrm{W}}\Big(\frac{10.75}{g_s}\Big)^{4/3}F_{\mathrm{h}},\qquad
F_{\mathrm{h}} = \Big[\frac{T_\nu}{T_\gamma}\Big(\frac{11}{4}\Big)^{1/3}\Big/\big(1 + h_\nu\big)\Big]^4
 = 1.0095 \tag{FE-133}
$$
<!-- symbols: Delta, Neff, NW, grho, Fh, Tnu, Tgamma, hnu -->

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

$$
\Gamma_{\mathrm{fi}} =
 \frac{T}{32\pi^4}\int_0^\infty\mathrm{d}\big(E_{\mathrm{cm}}^2\big)\Big(\sum_{\text{spins}}\sigma
 \Big)E_{\mathrm{cm}}^3
 K_1\Big(\frac{E_{\mathrm{cm}}}{T}\Big) =
 \frac{4}{\pi^5}\,N_{\mathrm{fold}}\,G_{\mathrm{V}}^2\,T^8\sum_fN_{\mathrm{c}}\big(q_f\tilde I_{of}\big)^2,
\qquad \frac{\mathrm{d}\big(\rho_{\mathrm{fold}}\,\mathrm{e}^{4a_4}\big)}{\mathrm{d}x_4} =
 8T\,\Gamma_{\mathrm{fi}}\,\mathrm{e}^{4a_4} \tag{FE-129}
$$
<!-- symbols: Gammafi, Temp, pi, infty, diff, Ecm, sigmaxs, Kbessel, Nfold, GV, if, Nc, qBL, tildeI, io, rhofold, euler, a4, x4 -->

$$
\Delta N_{\mathrm{eff}} = \frac{\rho_{\mathrm{fold}}}{\rho_\nu},\qquad \rho_\nu =
 \frac78\,\frac{\pi^2}{15}\,T_\nu^4,\qquad
\frac{2\Gamma_{\mathrm{fi}}}{n_{\mathrm{fold,eq}}\,\mathcal{H}} \ll 1,\qquad
n_{\mathrm{fold,eq}} = N_{\mathrm{fold}}\cdot4\cdot\frac34\,\frac{\zeta(3)}{\pi^2}\,T^3 \tag{FE-130}
$$
<!-- symbols: Delta, Neff, rhofold, rhonu, pi, Tnu, Gammafi, nfoldeq, Hubble, Nfold, zeta3, Temp -->

(the sum $\sum_fN_{\mathrm{c}}(q_f\tilde I_{of})^2 = 126.85$ runs over the fifteen multiplets of three generations in the plasma, without the
right-handed neutrinos). Integrated from $T_{\mathrm{max}} = 10$ TeV this gives $\Delta N_{\mathrm{eff}} = 5.21\times10^{29}\,G_{\mathrm{V}}^2$ GeV$^4$, so the
benchmark strength (ASSUMED) $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ ($3.8\times10^{-12}\,G_{\mathrm{F}}$) adds $\Delta N_{\mathrm{eff}} = 0.001$
(and $8.0\times10^{-6}$, $1.25\times10^{-4}$, $8.0\times10^{-3}$ for $T_{\mathrm{max}} = 2$, 5 and 20 TeV), while the production rate per fold quantum
stays at most 0.012 of the Hubble rate: the fold bands never reach equilibrium, and $N_{\mathrm{eff}} = 3.0442$ instead of $3.0432$. A trace of
dark radiation, not dark matter.

**Had one half's fold band been thermalised (DERIVED).** It would decouple as two Weyl species with the extra radiation (written
out again)

$$
\Delta N_{\mathrm{eff}} = N_{\mathrm{W}}\Big(\frac{10.75}{g_s}\Big)^{4/3}F_{\mathrm{h}},\qquad
F_{\mathrm{h}} = \Big[\frac{T_\nu}{T_\gamma}\Big(\frac{11}{4}\Big)^{1/3}\Big/\big(1 + h_\nu\big)\Big]^4
 = 1.0095 \tag{FE-133}
$$
<!-- symbols: Delta, Neff, NW, grho, Fh, Tnu, Tgamma, hnu -->

($N_{\mathrm{W}} = 2$; $g_s$ the entropy degrees of freedom at its decoupling; $F_{\mathrm{h}}$ corrects for the heating of the neutrinos by
$e^+e^-$ annihilation, which an earlier-decoupled species does not receive, with the computed $T_\nu/T_\gamma = 0.71664$ and $h_\nu = 0.00165$):
$\Delta N_{\mathrm{eff}} = 0.0958$ for a decoupling above the electroweak scale ($g_s = 105.75$) and $0.1963$ just above the QCD crossover
($g_s = 61.75$). At fixed Planck parameters these would change the CMB temperature spectrum by up to 1.5 % and 3.1 % for
$30 \le l \le 2500$, and put $N_{\mathrm{eff}}$ 2.1 and 2.9 standard deviations above the ACT DR6 value $2.86 \pm 0.13$.

**The dark matter is cold (DERIVED, STANDARD equations).** The heavy odd quanta are pressureless ($w_{\mathrm{KS}} = 0$ at rest), so in the
linear cosmology of UM-2 they obey the equations of cold dark matter

$$
\delta_{\mathrm{DM}}' = -\theta_{\mathrm{DM}} + 3\Psi_{\mathrm{N}}',\qquad \theta_{\mathrm{DM}}' =
 -a_4'\,\theta_{\mathrm{DM}} + k^2\Phi \tag{FE-91}
$$
<!-- symbols: deltaDM, prime, PsiN, a4, kwave, Phi -->

with $\Omega_{\mathrm{c}}h_{100}^2 = 0.120$, the relic of the two species, which agrees with the dark-matter density of the CMB computation to
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

$$
h\,\chi_o = \varepsilon_o\,\chi_o,\qquad
h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M_{\mathrm{eff}}(y)\,\sigma_2 +
 \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y)
 + \frac{1 - \sigma_3}{2}\,v_{\mathrm{b}}(y) \tag{FE-63}
$$
<!-- symbols: hblock, chi, io, varepsilon, varsigma, imag, fblock, sigmaPauli, partial, iy, Meff, ycoord, euler, a4, kwave, vpot, vb -->

with the mean fields

$$
\begin{aligned}
&M_{\mathrm{eff}}(y) = m_\Psi + \frac{15}{16}\,\lambda\,n^{\mathrm{sc}}(y) +
 \frac{\langle\mathcal{F}\rangle}{\Lambda_\star^3},\qquad
 v(y) = -\frac{\lambda}{16}\,n(y) + \frac{c_{\mathrm{V}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi
 q_\psi\,n_{\psi i}(y),\\
&v_{\mathrm{b}}(y) = \frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi q^{B}_\psi\,n_{\psi i}(y)
\end{aligned} \tag{FE-64}
$$
<!-- symbols: Meff, ycoord, mPsi, lambda, nsc, calF, LambdaStar, vpot, ndens, cV, ii, ipsi, qBL, vb, cA, qB -->

the densities, momentum shells, cell volume and occupations

$$
\begin{aligned}
&n = \sum_o\tfrac12\,d_o\,\phi_o\,n_o,\qquad n^{\mathrm{sc}} =
 \sum_o\tfrac12\,d_o\,\phi_o\,n^{\mathrm{sc}}_o,\qquad
 n_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\chi_o,\\
&n^{\mathrm{sc}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_2\chi_o,\qquad
 n^{\mathrm{t}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_3\chi_o,\qquad
 d_o = 4\,r_3\big(\lvert\vec n_o\rvert^2\big),\qquad \vec k_o = k_{\mathrm{lat}}\,\vec n_o,\\
&\mathrm{Vol}_7 = \Big(\frac{2\pi}{k_{\mathrm{lat}}}\Big)^3v_{\mathrm{t}}\,f^4,\qquad
 \phi_o = \frac{1}{\mathrm{e}^{(\varepsilon_o - \mu_{\mathrm{chem}})/T} + 1}\ \ \text{(Mermin; or 0 and
 1 for the aufbau)}
\end{aligned} \tag{FE-65}
$$
<!-- symbols: ndens, io, ddeg, phiocc, nsc, euler, Hconst, ycoord, Vol7, chi, dagger, varsigma, sigmaPauli, nt, r3, nvec, kvec, klat, pi, vt, fblock, varepsilon, muchem, Temp -->

and the boundary conditions of the orbitals, written out again,

$$
\chi = (\chi_1,\ \chi_2)^T:\qquad \chi_2(0) = 0\ \ \text{(even)}\quad\text{or}\quad \chi_1(0) =
 0\ \ \text{(odd)},\qquad
\chi_2(-L) = 0 \tag{FE-69}
$$
<!-- symbols: chi, transpose, Lcut -->

Their energy-momentum tensor is

$$
\begin{aligned}
&\rho = \sum_o\tfrac12\,d_o\phi_o\,\varepsilon_o\,n_o - e_{\mathrm{int}},\qquad
 p_3 = \sum_o\tfrac12\,d_o\phi_o\,\frac{\mathrm{e}^{-a_4}\lvert\vec k_o\rvert}{3}\,n^{\mathrm{t}}_o +
 e_{\mathrm{int}},
 \qquad p_5 = e_{\mathrm{int}},\\
&p_0 = \sum_o\tfrac12\,d_o\phi_o\Big[(\varepsilon_o - v)\,n_o - M_{\mathrm{eff}}\,n^{\mathrm{sc}}_o
 - \mathrm{e}^{-a_4}\lvert\vec k_o\rvert\,n^{\mathrm{t}}_o\Big] + e_{\mathrm{int}}
\end{aligned} \tag{FE-67}
$$
<!-- symbols: rho, io, ddeg, phiocc, varepsilon, ndens, eint, p3, euler, a4, kvec, nt, p5, p0, vpot, Meff, nsc -->

and the equation of state of a state is the ratio of its integrated 3-space pressure to its integrated energy density:

$$ w_{\mathrm{KS}} = \frac{2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,p_3\,\mathrm{d}y}{2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,\rho\,\mathrm{d}y} $$
<!-- symbols: ana_wKS, Vol7, Lcut, euler, Hconst, ycoord, p3, diff, rho -->

Every computed state has $w_{\mathrm{KS}} \ge 0$: eight dark-matter quanta at rest $w_{\mathrm{KS}} = 0$ ($2.8\times10^{-5}$ with $\lambda_{\mathrm{test}}$);
the fold-band gas of 592 quanta $w_{\mathrm{KS}} = 1/3$ ($0.3312$ with $+\lambda_{\mathrm{test}}$, $0.3354$ with $-\lambda_{\mathrm{test}}$). The quanta of
dirac16complex are matter or radiation.

### The condensate runs away (DERIVED) {-}

A homogeneous scalar condensate of $\Psi$, diluted by the expansion, with the self-interaction energy $U_{\mathrm{cond}}$ has

$$ U_{\mathrm{cond}} = \frac{\lambda}{2}\big(n^{\mathrm{sc}}\big)^2,\qquad n^{\mathrm{sc}} \propto \mathrm{e}^{-3a_4},\qquad \rho = m_\Psi n^{\mathrm{sc}} + U_{\mathrm{cond}},\qquad p = n^{\mathrm{sc}}\,\frac{\mathrm{d}U_{\mathrm{cond}}}{\mathrm{d}n^{\mathrm{sc}}} - U_{\mathrm{cond}} = \frac{\lambda}{2}\big(n^{\mathrm{sc}}\big)^2 $$
<!-- symbols: ana_Ucond, lambda, nsc, euler, a4, rho, mPsi, pressure, diff -->

so that its equation of state, in the parametrisation of the supernova fits, is

$$ w_{\mathrm{de}} = \frac{p}{\rho} = \frac{\mathcal{X}}{1 + \mathcal{X}},\qquad \mathcal{X} = \frac{\lambda n^{\mathrm{sc}}}{2m_\Psi} = \mathcal{X}_0\,\mathrm{e}^{-3a_4},\qquad \mathcal{X}_0 = \frac{w_{\mathrm{de},0}}{1 - w_{\mathrm{de},0}},\qquad w_{\mathrm{de},a} = -\frac{\mathrm{d}w_{\mathrm{de}}}{\mathrm{d}\,\mathrm{e}^{a_4}}\Big\vert_{a_4 = 0} = \frac{3\mathcal{X}_0}{(1 + \mathcal{X}_0)^2} $$
<!-- symbols: ana_wde, pressure, rho, ana_calX, lambda, nsc, mPsi, euler, a4, diff -->

A negative $w_{\mathrm{de}}$ needs $\lambda < 0$, and then the energy density $\rho = m_\Psi n^{\mathrm{sc}}(1 + \mathcal{X})$ crosses zero where
$\mathcal{X} = -1$, in the past:

$$ \mathrm{e}^{a_4} = \big(-\mathcal{X}_0\big)^{1/3},\qquad z_{\mathrm{red}} = \big(-\mathcal{X}_0\big)^{-1/3} - 1 $$
<!-- symbols: euler, a4, ana_calX, sol_zred -->

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
<!-- symbols: ana_rhovac, mKK, pi, ana_rhode -->

In UM-2 the four-dimensional cosmological term is the residual of the stabiliser balance in the reduction of the Lovelock action
on the static block:

$$
\begin{aligned}
&\mathcal{L}_{(1)} = \mathcal{L}^{(4)}_{(1)} + \mathcal{L}^{(\mathrm{int})}_{(1)},\qquad
 \mathcal{L}_{(2)} = \mathcal{L}^{(4)}_{(2)} + 2\mathcal{L}^{(4)}_{(1)}\mathcal{L}^{(\mathrm{int})}_{(1)}
 + \mathcal{L}^{(\mathrm{int})}_{(2)},\qquad
 \mathcal{L}_{(3)} = 3\mathcal{L}^{(4)}_{(2)}\mathcal{L}^{(\mathrm{int})}_{(1)} +
 3\mathcal{L}^{(4)}_{(1)}\mathcal{L}^{(\mathrm{int})}_{(2)},\\
&\mathcal{L}^{(4)}_{(1)} = R^{(4)},\qquad \mathcal{L}^{(4)}_{(3)} = 0,\qquad
 \mathcal{L}^{(\mathrm{int})}_{(1)} = -12H^2K,\qquad
 \mathcal{L}^{(\mathrm{int})}_{(2)} = 24H^4K^2,\qquad \mathcal{L}^{(\mathrm{int})}_{(3)} = 0,\\
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)} - 2\Lambda - 2\kappa\rho_{\mathrm{stab}}
 = \mathcal{G}(K)\,R^{(4)} + \text{(topological)} - 2\mathcal{G}(K)\,\Lambda_4,\\
&\Lambda_4 = \frac{6H^2K\big(1 - 2w_{(2)}K\big) + \Lambda + \kappa\rho_{\mathrm{stab}}}{\mathcal{G}(K)}
\end{aligned} \tag{FE-48}
$$
<!-- symbols: Lov, Lov4, Lovint, R4, Hconst, Kblock, ip, alphaL, Lambda, kappa, rhostab, GK, Lambda4, wL -->

zero at the static point by construction. The observed dark energy needs

$$ \frac{\Lambda_4}{H^2} \sim \Big(\frac{\mathcal{H}_0}{H}\Big)^2 = 1.0\times10^{-92}: $$
<!-- symbols: Lambda4, Hconst, H0 -->

the cosmological-constant problem, unsolved (OPEN). A slowly deflating block cannot provide a dynamical dark energy instead,
because it would make $\alpha_{\mathrm{em}}$, $G_{\mathrm{N}}$ and the masses drift ($\lvert\mathcal{H}_f\rvert < 3.6\times10^{-8}\,\mathcal{H}_0$, section
A.8), the neutrino oscillation lengths most of all.

### Assessment of the association with dark energy {-}

The association of dirac16complex with dark energy is not supported in UM-2: its positive-energy states are matter or radiation,
its only accelerating configuration is unstable and reaches a negative energy density at $z_{\mathrm{red}} \approx 0.2$ to $0.6$, and the
measured $(w_{\mathrm{de},0}, w_{\mathrm{de},a})$ are not reproduced. The dark energy of UM-2 is the tuned four-dimensional cosmological term
$\Lambda_4$.

# Status labels, conditions, open problems and conflicts {-}

* **AUTHOR** (the author's input): the coordinates and the periodic hidden direction with the period $\pi/(6H)$; the order-0
  metric; the Lovelock weights and $\Lambda = -10H^2$; the Clifford algebra and the two halves of dirac16complex; the order that
  every non-massless particle receive its mass from its $x_0$ dependence, with the uncertainty relation as the reason, except
  the graviton, the photon and perhaps the quanta of dirac16complex.
* **RECORD**: the dirac16complex Lagrangian and the Kohn-Sham functional of its self-interaction.
* **DERIVED** (computed and verified): every mass as an $x_0$ eigenvalue; the exact decompositions of the eigenvalues; the
  uncertainty relation on the cell and the lower bound $(1 - \varrho_\xi(-1))\,m_{\mathrm{Heis}}$, never below $11.05$ TeV; the three
  classes of states; the zero-mode origin of the light masses and their hierarchy; the absence of tree-level flavour-changing
  neutral currents; the block sensitivities and the bounds on a deflation today; the candidate and its stability; the failure of
  I12 alone and the relic with I13; the detection rates; the bound on the self-interaction; the freeze-in of the fold bands; the
  non-negative equation of state of every Kohn-Sham state; the runaway of the condensate.
* **ASSUMED** (conditions on which the conclusions rest): the stabiliser and its $f^{-8}$ law; the good sector; the regular tip at
  $HL = 3$; $m_\Psi = H$; the tip sigma field, the tip matrices and the boundary assignments of the Standard-Model fields of three
  generations; the lightest neutrino mass $m_1 = 1$ meV and the normal ordering; the benchmark strengths of I11 and I12, the bound
  $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ on the self-interaction and the highest temperature $T_{\mathrm{max}} = 10$ TeV (the strength of I13
  follows from the relic abundance).
* **INVENTED**: the portals I11, I12 and I13; the tip sigma field without a radial mode (no Higgs particle) and the fermion
  boundary conditions.
* **ESTIMATE**: the radion decay and the reheating temperature; the direct-detection limit extrapolated to 44 TeV; the
  cross-section of the self-interaction channel (Fierz coefficients not computed); the elastic rate of the right-handed
  neutrinos; the effect of the order-$\alpha$ plasma pressure on the relic (about 2.7 % in $\Omega_{\mathrm{DM}}h_{100}^2$, 1.4 % in
  $G_{\mathrm{A}}$); the one-loop sensitivity of the nucleon mass.
* **OPEN**: the origin of the stabiliser; the extra-time modes; the closed time-like curves implied by compact extra times; the
  radion moduli problem; the block-shape mode driven by $p_0 - p_5$ (about 4 times the kept hidden pressure for non-relativistic
  dark matter, but absolutely suppressed); the microscopic origin of the portals (I12 alone could give the relic only as a
  strongly coupled $^3P_0$ channel; I13 gives it, and its contact form needs a mediator above about 30 TeV); the gravitational
  production of the fold bands; the origin of the tip matrices (the mixing angles); Dirac or Majorana neutrinos (the mechanism
  favours Dirac); the cosmological-constant problem.
* **Conflicts with data inherent in the order**: no Higgs boson (one is observed), and perturbative unitarity of $W^+W^-$ scattering
  lost near 1.2 TeV. (The one-generation conflict of version 1, a $Z$ width of $1.23$ GeV, is removed: three generations give
  $2.485$ GeV against the measured $2.4955$ GeV; the two values of the weak angle, on shell in the $x_0$ problem and
  $\overline{\mathrm{MS}}$ in the widths, move the width by 0.83 %, within the loop corrections that UM-2 does not compute.)

# Closing assessment {-}

**The $x_0$ mass mechanism.** The author's requirement is realised exactly in UM-2: every wave function depends on $x_0$
periodically with the period $\pi/(6H)$, every four-dimensional mass is an eigenvalue of the $x_0$ operator of its field, and the
massless particles (the photon, the gluons, the graviton and the fold bands of dirac16complex) are exactly the zero modes that
symmetry protects, which are also the exceptions the author names. The author's physical reason, the uncertainty relation,
holds as a theorem on the cell (with a tip term) and is quantitative for the heavy states: the Kaluza-Klein and odd excitations
and the dark matter lie above the estimate $m_{\mathrm{Heis}}$, by factors 2.3 to 7.5, and the dark-matter mass is 90 % hidden
momentum. It fails for every light particle: the bound it sets on the hidden kinetic energy of a localised state is at least
$11.05$ TeV, while the observed masses of $W^\pm$, $Z$ and all twelve fermions lie $3\times10^{-3}$ to $10^{-17}$ below their estimates. Those
masses come from exact zero modes, whose hidden kinetic energy is cancelled exactly, mixed at the tip of the cell, where the
electroweak symmetry is broken; the exponential tip densities turn order-one bulk masses into the fourteen orders of magnitude of
the fermion masses, a sharper localisation giving a lighter particle. The mixing matrices are inputs (tip matrices), and the
extra times are irrelevant today because the block is small and frozen, not because it keeps deflating.

**dirac16complex as dark matter.** Supported, conditionally. The heavy odd quanta of the two halves, two degenerate Dirac fermions
of 44.35 TeV, are cold, neutral and stable in the good sector with an exact fold parity. They obtain the observed relic density
only through the INVENTED s-wave portal I13 to the baryon-number current ($G_{\mathrm{A}} = 1.28\times10^{-9}$ GeV$^{-2}$, about 1 % physics
accuracy), since the gauge-kinetic portal alone would violate partial-wave unitarity; the candidate predicts a spin-independent
cross-section on xenon at 0.16 of the present LZ limit and is therefore falsifiable by the next generation of xenon detectors.
The field as a whole is not dark matter: its massless fold bands are a trace of dark radiation ($\Delta N_{\mathrm{eff}} = 0.001$), kept out
of equilibrium by the weak portal I11 and a bounded self-interaction.

**dirac16complex as dark energy.** Not supported. No positive-energy state of the field has a negative equation of state, the
only accelerating configuration (a negative-coupling condensate) runs away to a negative energy density at a redshift of 0.2 to
0.6 and does not reproduce the measured $(w_{\mathrm{de},0}, w_{\mathrm{de},a})$, and the dark energy of UM-2 is the four-dimensional
cosmological term $\Lambda_4$ of the stabilised block, tuned to $10^{-92}H^2$: the cosmological-constant problem remains open.

