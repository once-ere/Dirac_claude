---
title: "UM-3 analysis"
subtitle: 'The x0 mass mechanism, dirac16complex as dark matter and as dark energy, and what the author may have left out'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Analysed and verified by Claude (Anthropic)"
  - "Analysis of UM-3, 2026-10-24"
  - "Repository once-ere/Dirac_claude, folder universe_model_3"
---

# How to read this document

## What this document contains

The author asks for three analyses of the universe model UM-3: the mass mechanism along the hidden coordinate $x_0$ (the period
$\pi/(6H)$ of the metric and the uncertainty relation), whether dirac16complex can be the dark matter, and whether it can be the
dark energy. He also asks to be told what he may have left out. This document gives the four answers. It is self-contained: every
equation it uses is written in it (with the tag it carries in every UM-3 document, FE-n for a field equation, or A-n for an
equation of this document), and every symbol of every display equation is defined right after it. The sections are:

* **The answers in brief.**
* **The $x_0$ mass mechanism**: the period of $x_0$, the proper length of the hidden direction, the spectra that replace the
  tower of a compact dimension, and the uncertainty relation.
* **dirac16complex as dark matter**: stability, gravitation on the fold, the equation of state of the Kohn-Sham states, the relic
  density, direct detection, and the window of parameters that survives.
* **dirac16complex and the dark energy**: why the gas of bound states cannot be dark energy, what the dark energy of UM-3 is,
  and how it compares with the baryon acoustic oscillations measured by DESI DR2 (the second data release of the Dark Energy
  Spectroscopic Instrument).
* **What the author may have left out**: the additions that UM-3 needed, and the open problems.

## The status labels

Every result carries one of the labels **AUTHOR** (from the author's notebooks `4+4.nb` and `Dirac_Einstein-Lovelock_4+4_Nash.nb`
and his order of 2026-10-24), **RECORD** (from the record of this repository: the Lagrangian of dirac16complex with its canonical
spin connection and contact self-interaction, the Kohn-Sham treatment), **STANDARD** (textbook physics or a published measurement,
named), **ASSUMED** (a choice of UM-3 without derivation), **INVENTED** (a new interaction of UM-3: the portals of dirac16complex),
**DERIVED** (computed and verified in UM-3, with the verification stated), **ESTIMATE** (an order-of-magnitude evaluation) and
**OPEN** (not settled).

## Every equation is followed by its symbols

Every display equation is followed by the list of EVERY symbol that appears in it, with its meaning, unit (natural units
$\hbar = c = 1$), value and status. The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space-like
coordinate (the metric depends on it through $z = 6Hx_0$), $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ three
extra time-like coordinates; the signature is $(+,+,+,+,-,-,-,-)$. $H$ is the author's constant (an inverse length), a free
parameter of UM-3. The Standard Model lives on the fold of the metric (the surface $z = \pi/2$, where the proper coordinate
$\sigma$ of the hidden direction is zero), dirac16complex and gravity in the bulk.

## The answers in brief

1. **The $x_0$ mass mechanism.** The coordinate $x_0$ has the period $\pi/(6H)$, but one period is a hidden direction of infinite
   proper length, warped towards the fold: there is no compact dimension, no Kaluza-Klein tower with spacing $12H$, and no
   uncertainty bound $p_{\mathrm{h}} \gtrsim 6H$ on the momentum along the hidden direction. The masses that $x_0$ produces are of a
   different kind: a gap above the massless zero modes of the massless bulk fields, set by the warp ($3H$ for scalars, $2H$ for
   gauge fields; a massless bulk fermion has none), and for dirac16complex a continuum above its bulk mass $m_\Psi$ with eight
   states bound to the fold at $\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}$ ($q_{\mathrm{b}}$ the inverse width of their profile along the
   hidden direction). The bound states obey the ordinary uncertainty relation; they are lighter the narrower they are because a
   narrower state is held by a stronger attraction of the fold, not because confinement costs energy (DERIVED).
2. **Dark matter.** The bound particles $\chi$ of dirac16complex cannot decay into the Standard Model alone (whether they are
   stable against the negative-energy states of their indefinite charge is open), gravitate on the fold like matter of the fold,
   form a pressureless gas in the dilute limit, and are a thermal relic with the measured density if they annihilate with
   $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 2.2\times10^{-26}$ cm$^3$/s (in the normalisation in which their number density counts all eight
   states of the bound level; one $\chi$ with one antiparticle annihilates four times faster). Direct detection by the LUX-ZEPLIN
   experiment excludes this through the quark portals, allows it through the lepton portals above about 1.5 TeV, and requires the
   binding to be weak ($q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}}$ at a few TeV); the right-handed neutrinos must not be thermalised.
   dirac16complex can be the dark matter in this window (DERIVED, ESTIMATE; OPEN: the stability against the negative-energy
   states).
3. **Dark energy.** No: the gas of bound states has a positive pressure that vanishes in the dilute limit, never a negative one.
   The dark energy of UM-3 is the vacuum energy of the fold, a free parameter whose pressure is minus its energy density ($w = -1$,
   $w$ the ratio of pressure to energy density); it fits the cosmic microwave background (CMB) but keeps the tension of the
   cosmological-constant model with the baryon acoustic oscillations (BAO) of DESI DR2, 2.3 standard deviations in DESI's own
   analysis (DERIVED: $w = -1$; STANDARD: the tension).
4. **What was left out.** UM-3 had to add right-handed quarks and Yukawa couplings, three right-handed neutrinos (accepted by the
   author), a thin fluid and an Einstein-Hilbert term on the fold, a medium in the bulk that violates the null energy condition
   and must respond to the fold, the gauge field that the author's ad hoc Higgs vacuum needs (the doublet $(\mathcal{A}, v + h)/\sqrt2$
   with the decaying upper component $\mathcal{A} = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$), and it found several open problems (the Krein
   norm, the extra times, Lorentz violation in the bulk). The last section lists them.

# The $x_0$ mass mechanism

## The period of $x_0$ and the proper length of the hidden direction

$$
\begin{aligned}
&g_{MN} = \mathrm{diag}\Big(\cot^2z,\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},
 \ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ -1,\\
&\qquad\qquad -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6},
 \ -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6}\Big),\qquad z = 6Hx_0,\\
&\sigma = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H},\qquad \mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0,\\
&g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
 - \mathrm{d}x_4^2
\end{aligned} \tag{FE-27}
$$
<!-- symbols: metric, iM, iN, diag, zvar, euler, a4, b4, Hconst, x0, sigma, sgn, pi, diff, Xcoord, x1, x2, x3, x4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (FE-27).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

The author's metric and its proper chart. The metric depends on $x_0$ only through $z = 6Hx_0$, so its coefficients repeat with
the coordinate period $\pi/(6H)$: one period is $0 < z < \pi$, with the fold at $z = \pi/2$ and the tips at $z = 0$ and $z = \pi$, where
$g_{x_0x_0} = \cot^2z$ diverges and the warp $(\sin^2z)^{1/6}$ vanishes. Status: AUTHOR (the metric), DERIVED (the chart).

$$
\int_0^{\pi/(6H)}\sqrt{\cot^2(6Hx_0)}\;\mathrm{d}x_0 = \frac{1}{6H}\int_0^{\pi}\lvert\cot z\rvert\,\mathrm{d}z = \infty,\qquad
\sigma(z) = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H} \to \mp\infty\ \ (z \to 0,\ \pi) \tag{A-1}
$$
<!-- symbols: x0, Hconst, diff, zvar, pi, infty, sigma, sgn -->
<!-- begin generated symbol list -->
**Symbols in (A-1).**

- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.

<!-- end generated symbol list -->

The proper length of one period of $x_0$ is infinite: $\lvert\cot z\rvert$ diverges at the tips like $1/z$, so its integral diverges
logarithmically, and the proper coordinate $\sigma$ runs over the whole line. The hidden direction is not a circle of
circumference $\pi/(6H)$ but an infinite line, warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$ away from the fold; the tips are infinitely
far away (DERIVED, `um3_fold.py`, J1).

$$
\begin{aligned}
&p_{\mathrm{h}} \gtrsim \frac{\pi}{\pi/(6H)} = 6H,\qquad m_{\mathrm{KK}}^2 = m_\Psi^2 + \big(12H\,\mathsf{k}\big)^2\ \ (\mathsf{k} = 0, \pm1, \pm2, \dots)\\
&\text{(for a compact direction of length } \pi/(6H)\text{, not UM-3)}
\end{aligned} \tag{A-2}
$$
<!-- symbols: ph, pi, Hconst, mKK, mPsi, kint -->
<!-- begin generated symbol list -->
**Symbols in (A-2).**

- $p_{\mathrm{h}}$: The momentum along the hidden direction of a particle confined to it, if that direction were compact (A-2, not UM-3). Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $m_{\mathrm{KK}}$: The masses of the tower of modes of a field on a compact hidden direction (Kaluza-Klein masses; A-2, not UM-3). Unit: GeV. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathsf{k}$: An integer that numbers the modes of a compact direction. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

The mass mechanism one would expect if $x_0$ were a compact direction of proper length $\pi/(6H)$: a particle confined to it has,
by the uncertainty relation, a momentum $p_{\mathrm{h}}$ along $x_0$ of at least about $\pi$ divided by the length, $6H$, and a field periodic
in $x_0$ has a tower of masses $m_{\mathrm{KK}}$ with the spacing $12H$ (the Kaluza-Klein masses, numbered by the integer $\mathsf{k}$). Status: STANDARD (for a compact direction). Neither
applies to UM-3, because the proper length is infinite (A-1).

## What the hidden direction produces instead

$$
u_{\mathrm{s}}'' + \big(\omega^2 - 9H^2\big)u_{\mathrm{s}} + 6H\,\delta_{\mathrm{D}}(\sigma)\,u_{\mathrm{s}} = 0:\qquad
\omega = 0\ \ \text{(zero mode)},\qquad \omega \ge 3H\ \ \text{(continuum)} \tag{A-3}
$$
<!-- symbols: us, prime, omegafreq, Hconst, deltaD, sigma -->
<!-- begin generated symbol list -->
**Symbols in (A-3).**

- $u_{\mathrm{s}}$: The rescaled profile of a massless scalar field of the bulk at zero momentum along ordinary space: the field is $\mathrm{e}^{3H\lvert\sigma\rvert}u_{\mathrm{s}}(\sigma)\,\mathrm{e}^{-\mathrm{i}\omega x_4}$. Unit: as the field. Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

A massless field of the bulk (here a scalar at zero momentum along ordinary space, its profile written as
$\mathrm{e}^{3H\lvert\sigma\rvert}u_{\mathrm{s}}(\sigma)$): the warp turns its mode equation into a Schrodinger problem with a constant
potential $9H^2$ and an attractive delta function at the fold, which binds exactly one state, the massless zero mode; above it the
continuum starts at the gap $3H$. A gauge field of the bulk has the same structure with the potential $4H^2$ and the gap $2H$ (its
profile written as $\mathrm{e}^{2H\lvert\sigma\rvert}u$), and a massless fermion of the bulk has no gap: once $\mathrm{e}^{3H\lvert\sigma\rvert}$ is
taken out, its equation at zero momentum is that of flat space. These gaps are the masses that the geometry of $x_0$ gives the
excitations of bulk fields: they are set by $H$, as the author's mechanism suggests, but they come from the warp, not from a
period, and there is no tower (the spectrum above the gap is continuous). Status: DERIVED (`um3_bulk.py`, B1, for the scalar; the
same transformation for the gauge field and the fermion).

$$
\chi' = \mathbb{K}\,\chi,\qquad \mathbb{K} = \gamma^{(0)}\big(m_\Psi + \mathrm{i}\omega\gamma^{(4)}\big),\qquad
\mathbb{K}^2 = \big(m_\Psi^2 - \omega^2\big)\mathbf{1},\qquad \chi \propto \mathrm{e}^{\pm q\sigma},\qquad q = \sqrt{m_\Psi^2 - \omega^2} \tag{FE-37}
$$
<!-- symbols: chiprof, prime, Kbulk, gammaM, mPsi, imag, omegafreq, identity, euler, qdecay, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-37).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathbb{K}$: The transfer matrix of the profile equation at zero momentum, $\chi' = \mathbb{K}\chi$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $q$: The decay rate of a profile along $\sigma$ at frequency $\omega$, $q = \sqrt{m_\Psi^2 - \omega^2}$ (imaginary in the continuum). Unit: GeV. Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

$$
q_{\mathrm{b}} = -m_\Psi\,\big(\mu_{\mathrm{L}} + \mu_{\mathrm{R}}\big)\,\frac{\tanh\varsigma}{2\varsigma},\qquad \varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}},\qquad
\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2},\qquad \lvert\chi_{\mathrm{b}}(\sigma)\rvert \propto \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert} \tag{FE-40}
$$
<!-- symbols: qb, mPsi, muX, varsigma, omegab, chib, euler, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-40).**

- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $\varsigma$: The auxiliary variable of the bound-state condition, $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($\varsigma_- = \sqrt{-\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ when $\mu_{\mathrm{L}}\mu_{\mathrm{R}} < 0$). Unit: dimensionless. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\chi_{\mathrm{b}}$: The profile of a state of dirac16complex bound to the fold. Unit: GeV$^{2}$. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

dirac16complex on the static block (the late-time state of the author's metric in which $a_4$ and $b_4$ are constant in the bulk, so
that the bulk does not change with time): the continuum of its bulk modes starts at its bulk mass $m_\Psi$ (FE-37), and the fold, if it is
attractive, binds eight states below it (FE-40), with the rest energy $\omega_{\mathrm{b}}$ seen on the fold and the profile
$\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Status: DERIVED (`um3_spectra.py`, S1 to S4, with the author's exact $16 \times 16$ matrices).

$$
\ell_{\mathrm{b}} = \sqrt{\big\langle\sigma^2\big\rangle} = \frac{1}{\sqrt2\,q_{\mathrm{b}}},\qquad
m_\Psi - \omega_{\mathrm{b}} = m_\Psi - \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2} \approx \frac{q_{\mathrm{b}}^2}{2m_\Psi} = \frac{1}{4m_\Psi\,\ell_{\mathrm{b}}^2} \tag{A-4}
$$
<!-- symbols: ellb, mean, sigma, qb, mPsi, omegab -->
<!-- begin generated symbol list -->
**Symbols in (A-4).**

- $\ell_{\mathrm{b}}$: The width of a bound state of dirac16complex along the hidden direction: the root mean square of $\sigma$ in its density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: length. Value: $1/(\sqrt2\,q_{\mathrm{b}})$. Status: DERIVED.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The width and the mass of the bound states: their width $\ell_{\mathrm{b}}$ along the hidden direction (the root mean square of $\sigma$
in the density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$) and their mass deficit below the continuum (for weak binding). The states obey the
ordinary uncertainty relation: the mean square of the momentum along $\sigma$ in the profile $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$ is
$q_{\mathrm{b}}^2$, so that $\langle p_\sigma^2\rangle\langle\sigma^2\rangle = 1/2$. The narrower the state, the larger the deficit, because a
narrower state is held by a stronger attraction of the fold: the energy falls not because the particle is confined (in the
compact case confinement raises it) but because the fold binds it more strongly; outside the fold the profile is an evanescent
wave, $p_\sigma^2 = -q_{\mathrm{b}}^2$ in $\omega^2 = m_\Psi^2 + p_\sigma^2$. The $x_0$ mass of dirac16complex is therefore a binding mass:
$\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}$, set by the bulk mass and by the strengths of the fold terms (the mean fields of the
Standard Model at the fold), not by the period of $x_0$. Status: DERIVED.

## The answer

The period $\pi/(6H)$ of the coordinate $x_0$ does not produce a mass by the uncertainty relation, because one period is an infinite
proper distance. The hidden direction produces masses in two other ways: the warp gives the massless bulk scalars a gap $3H$ and
the bulk gauge fields a gap $2H$ above their zero modes (a mass scale set by $H$, without a tower; a massless bulk fermion has no
gap), and the fold binds dirac16complex in eight states of mass $\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}$, which are lighter the
narrower they are, because a narrower state is bound more strongly. Status: DERIVED.

# dirac16complex as dark matter

## Stability

$$
\begin{aligned}
\mathcal{L}_{\mathrm{P}} = {}&-c_\Phi\,\big(\Phi^\dagger\Phi\big)\,\bar\Psi P_{\mathrm{L}}\Psi
 - \sum_{X}\Big[\frac14\big(c^{G}_X\,G^A_{\mu\nu}G^{A\mu\nu} + c^{W}_X\,W^I_{\mu\nu}W^{I\mu\nu}
 + c^{B}_X\,B_{\mu\nu}B^{\mu\nu}\big)\,\bar\Psi P_X\Psi\\
&\qquad + \frac{d_X}{2}\,B_{\mu\nu}\,\mathcal{D}_X^{\mu\nu} + \sum_{f} c^{f}_X\,J_f^\mu\,j_{X\mu}\Big],\\
\mathcal{D}_X^{\mu\nu} = {}&\mathrm{i}\,\bar\Psi\,\Sigma^{\mu\nu}P_X\Psi,\qquad
j_X^\mu = \mathrm{i}\big(\bar\Psi P_X D^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi\big),\qquad
J_f^\mu = \bar\psi_f\,\hat\gamma^\mu\psi_f
\end{aligned} \tag{IN-16}
$$
<!-- symbols: LP, cPhi, Phi, dagger, Psi, PL, iX, cG, Ggluon, iA, imu, inu, cW, Wsu2, iI, cB, Bhyp, PX, ddip, Ddip, if, cf, Jcur, jcur, imag, SigmaGen, Dcov, psiSM, gammahat -->
<!-- begin generated symbol list -->
**Symbols in (IN-16).**

- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $P_X$: The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$. Unit: dimensionless. Status: AUTHOR.
- $d_X$: The dipole-portal coupling of the half $X$ of dirac16complex with the hypercharge field strength. Unit: GeV$^{-5}$. Status: INVENTED.
- $\mathcal{D}_X^{\mu\nu}$: The dipole (antisymmetric tensor) density of the half $X$ of dirac16complex at the fold, $\mathcal{D}_X^{\mu\nu} = \mathrm{i}\bar\Psi\Sigma^{\mu\nu}P_X\Psi$ (real, DERIVED). Unit: GeV$^7$. Status: DERIVED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $J_f^\mu$: The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the currents that are the sources of the gauge fields. Unit: GeV$^3$. Status: STANDARD.
- $j_X^\mu$: The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED). Unit: GeV$^8$. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Sigma^{ab},\ \Sigma^{\mu\nu}$: The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold. Unit: dimensionless. Status: AUTHOR.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\psi,\ \bar\psi$: A Standard-Model fermion field (a four-dimensional Weyl field of the fold with three generations, written as a four-component spinor of fixed chirality); $\bar\psi = \psi^\dagger\beta$; $\psi_f$ the fields of the kind $f$. Unit: GeV$^{3/2}$. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

$$
Q_\Psi = \int\mathrm{d}\sigma\,\mathrm{d}^3x\,\sqrt{\lvert g\rvert}\;\Psi^\dagger\mathfrak{B}\Psi,\qquad
\mathfrak{B} = \mathrm{i}\,\sigma_{16}\,\gamma^{(4)},\qquad \mathfrak{B}^\dagger = \mathfrak{B},\qquad \mathfrak{B}^2 = \mathbf{1},\qquad
E_o = -\omega_o\,\mathcal{Q}_o \tag{FE-43}
$$
<!-- symbols: QPsi, diff, sigma, xfour, metric, Psi, dagger, Bkrein, imag, sigma16, gammaM, identity, Eorb, io, omegafreq, Qorb -->
<!-- begin generated symbol list -->
**Symbols in (FE-43).**

- $Q_\Psi$: The conserved charge of dirac16complex (the Noether charge of a change of the phase of $\Psi$ by a constant), a Krein form (indefinite). Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $x$: The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathfrak{B}$: The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density. Unit: dimensionless. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $o$: The label of a Kohn-Sham orbital (a single-particle state of dirac16complex); a sum over $o$ runs over the orbitals. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathcal{Q}_o$: The charge $Q_\Psi$ of the Kohn-Sham orbital $o$ (positive or negative). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The portals of dirac16complex to the Standard Model (IN-16) and its conserved charge (FE-43). Every portal term, like the bulk
Lagrangian and the self-interaction, contains dirac16complex only in the bilinears $\bar\Psi\cdots\Psi$: the action is invariant under
a constant change of the phase of $\Psi$, and the charge $Q_\Psi$ is conserved. A particle $\chi$ (a bound state of dirac16complex)
can therefore annihilate only with an antiparticle, and the lightest states of dirac16complex, the bound states of the fold, cannot
decay into the Standard Model alone. Conservation of $Q_\Psi$ does not by itself make them stable, because the charge is a Krein
form (indefinite): with $E_o = -\omega_o\mathcal{Q}_o$, a particle $\chi$ of positive energy (charge $-1$ at $+\omega_{\mathrm{b}}$) could turn
into a state of negative energy with the same charge (at $-\omega_{\mathrm{b}}$) and Standard-Model quanta that carry away
$2\omega_{\mathrm{b}}$. Whether this happens, and how fast, is not settled. Status: DERIVED (no decay into the Standard Model alone, from
the form of IN-16; the Krein signature of the charge, `um3_fields.py`, F3, and `um3_spectra.py`, S4), OPEN (the stability against
the negative-energy states).

## Gravitation on the fold

$$
\kappa\int_{\text{layer}}\mathcal{T}_\Psi{}^a{}_b\,\mathrm{d}\sigma = \frac{\kappa}{\mathcal{Z}\,V_*}\,\mathcal{T}_\chi{}^a{}_b\qquad\big(H \ll q_{\mathrm{b}}\big) \tag{A-5}
$$
<!-- symbols: kappa, TPsi, ia, ib, diff, sigma, Zfold, Vstar, Tchi, Hconst, qb -->
<!-- begin generated symbol list -->
**Symbols in (A-5).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with $\eta_{ab}$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{T}_\chi{}^a{}_b$: The four-dimensional energy-momentum tensor of the gas of the bound particles $\chi$ of dirac16complex, per proper volume of ordinary space at the fold (energy density $\rho_\chi$). Unit: GeV$^4$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The particles $\chi$ live in the bulk, in a layer of width $1/q_{\mathrm{b}}$ around the fold. The junction conditions of the fold
integrate the bulk field equations across the fold: the jump of the junction potential across the fold equals $\kappa$ times the
energy-momentum tensor $\mathcal{S}$ of everything that lives on the fold. If the layer is thin compared with the scale $1/H$ on which
the metric varies, integrating across the whole layer gives that jump the additional source A-5, where $\mathcal{T}_\chi$ is the
four-dimensional energy-momentum tensor of the gas of $\chi$ (per proper volume of ordinary space) and $\mathcal{Z}V_*$ the proper volume
of the extra times at the fold ($\mathcal{Z} = 1$ with frozen extra times, that is when the size $\mathrm{e}^{-a_4}b_4$ of the extra times
no longer changes). This is exactly the form in which the matter of the fold enters ($\mathcal{S} = \mathcal{T}_{\mathrm{SM}}/V_* + \dots$, the
energy-momentum tensor of the Standard Model divided by the volume of the extra times): the particles $\chi$ gravitate on the fold like
matter of the fold, with the same Newton constant, and enter the Friedmann equation of FE-59 as $\rho_\chi$. The corrections are of
relative order $H/q_{\mathrm{b}}$. Status: DERIVED (from the junction conditions), ESTIMATE (the corrections).

## The equation of state of the Kohn-Sham states

KS_ANALYSIS_EOS

## The relic density, direct detection and the window

$$
\begin{aligned}
&\mathfrak{g}_{\Phi} = \frac{\partial\omega_{\mathrm{b}}}{\partial\mu_{\mathrm{L}}}\,\frac{c_\Phi}{V_*},\qquad
 \mathfrak{g}_{G} = \sum_X\frac{\partial\omega_{\mathrm{b}}}{\partial\mu_X}\,\frac{c^{G}_X}{4V_*},\qquad
 \mathfrak{g}_{f} = \sum_X\frac{\partial\omega_{\mathrm{b}}}{\partial\mu_X}\,\frac{2\omega_{\mathrm{b}}\,c^{f}_X}{V_*},\qquad
 \frac{\partial\omega_{\mathrm{b}}}{\partial\mu_X} = -\frac{q_{\mathrm{b}}}{\omega_{\mathrm{b}}}\,\frac{\partial q_{\mathrm{b}}}{\partial\mu_X},\\
&\Delta\omega_{\mathrm{b}} = \mathfrak{g}_{\Phi}\,\Delta\langle\Phi^\dagger\Phi\rangle + \mathfrak{g}_{G}\,\Delta\langle G^2\rangle + \sum_f\mathfrak{g}_{f}\,\Delta n_f,\qquad
 \mathfrak{g}_{h\chi} = \mathfrak{g}_{\Phi}\,v = -\frac{m_\Psi^2\,\mu_{\mathrm{L}}^2}{2\,\omega_{\mathrm{b}}\,v}\quad(\mu_{\mathrm{R}} = 0)
\end{aligned} \tag{FE-47}
$$
<!-- symbols: gport, partial, omegab, muX, cPhi, Vstar, cG, iX, cf, if, qb, Delta, Phi, dagger, mean, Gsq, Ggluon, nf, vev, mPsi -->
<!-- begin generated symbol list -->
**Symbols in (FE-47).**

- $\mathfrak{g}_{\Phi},\ \mathfrak{g}_{G},\ \mathfrak{g}_{f},\ \mathfrak{g}_{h\chi}$: The four-dimensional couplings of the bound states $\chi$ of dirac16complex to the Standard Model (FE-47): to $\Phi^\dagger\Phi$, to the gluon kinetic density, to the number densities of the fermions of kind $f$, and the Yukawa coupling of the Higgs boson to $\chi$. Unit: $\mathfrak{g}_{\Phi}$: GeV$^{-1}$; $\mathfrak{g}_{G}$: GeV$^{-3}$; $\mathfrak{g}_{f}$: GeV$^{-2}$; $\mathfrak{g}_{h\chi}$: dimensionless. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\Delta$: A change, difference or small variation of the quantity that follows ($\Delta\rho$ a perturbation, $\Delta m^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $n_f$: The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium. Unit: GeV$^3$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->

$$
\frac{\mathrm{d}n_\chi}{\mathrm{d}x_4} + 3H_4\,n_\chi = -\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle\big(n_\chi^2 - n_{\chi,\mathrm{eq}}^2\big),\qquad
n_{\chi,\mathrm{eq}} = g_\chi\Big(\frac{\omega_{\mathrm{b}}\mathsf{T}}{2\pi}\Big)^{3/2}\mathrm{e}^{-\omega_{\mathrm{b}}/\mathsf{T}},\qquad
\Omega_\chi h_{100}^2 \simeq \frac{1.07\times10^9\ \text{GeV}^{-1}\,x_{\mathrm{f}}}{\sqrt{g_*}\,M_{\mathrm{Pl}}\,\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle} \tag{FE-61}
$$
<!-- symbols: diff, nchi, x4, H4, sigmaann, vrel, mean, nchieq, gchi, omegab, Ttemp, pi, euler, Omegachi, h100, xf, gstar, MPl -->
<!-- begin generated symbol list -->
**Symbols in (FE-61).**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc. Status: STANDARD.
- $\sigma_{\mathrm{ann}}$: The annihilation cross-section of the particles $\chi$ into Standard-Model particles (through the portals) in the normalisation of FE-61, where $n_\chi$ counts the four particle and the four antiparticle states of the bound level: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is a quarter of the annihilation rate $(\sigma\mathsf{v})_{\chi\bar\chi}$ of one particle $\chi_a$ with one antiparticle $\bar\chi_a$. Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathsf{v}$: The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product. Unit: dimensionless. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $n_{\chi,\mathrm{eq}}$: The number density of $\chi$ in thermal equilibrium with the plasma (non-relativistic). Unit: GeV$^3$. Status: STANDARD.
- $g_\chi$: The number of internal states of the bound level of $\chi$ that are in thermal equilibrium. Unit: dimensionless. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\mathsf{T}$: The temperature of the Standard-Model plasma (of the photons after the annihilation of electrons and positrons). Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\Omega_\chi$: The density parameter of the dark matter today. Unit: dimensionless. Value: $\Omega_\chi h_{100}^2 = 0.120$ (Planck 2018). Status: DERIVED.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.
- $x_{\mathrm{f}}$: The ratio of the mass of $\chi$ to the temperature at which its annihilations stop (freeze-out). Unit: dimensionless. Value: 23 to 30 (for $\omega_{\mathrm{b}}$ = 10 GeV to 10 TeV). Status: STANDARD.
- $g_*$: The effective number of relativistic degrees of freedom at the freeze-out ($g_\rho$ there). Unit: dimensionless. Status: STANDARD.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.221\times10^{19}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->

The couplings of $\chi$ to the Standard Model (FE-47) and its relic density (FE-61). Status: DERIVED, STANDARD.

| requirement | consequence for UM-3 | status |
| ------ | ------ | ------ |
| the measured density $\Omega_\chi h_{100}^2 = 0.120$ by thermal freeze-out | $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 2.2\times10^{-26}$ cm$^3$/s for $\omega_{\mathrm{b}} = 10$ GeV to 10 TeV (FE-61 with $g_\chi = 8$, numerical solution); FE-61 counts the four particle and the four antiparticle states of the bound level in $n_\chi$, so this is a quarter of the annihilation rate of one $\chi_a$ with one $\bar\chi_a$, $(\sigma\mathsf{v})_{\chi\bar\chi} = 9\times10^{-26}$ cm$^3$/s | DERIVED |
| direct detection, quark portals | a relic through quark portals scatters on nuclei 25 (10 TeV) to $2\times10^7$ (100 GeV) times above the limit of the LUX-ZEPLIN experiment (4.2 tonne-years of xenon; below its minimum at 40 GeV the limit is not compared): the quark portals are too weak to set the density | ESTIMATE |
| direct detection, lepton portals | the scattering through a lepton loop and the photon is below the LUX-ZEPLIN limit above about 1.5 TeV | ESTIMATE |
| direct detection, Higgs portal | the Yukawa coupling $\mathfrak{g}_{h\chi} = -2q_{\mathrm{b}}^2/(\omega_{\mathrm{b}}v)$ of FE-47 is fixed by the binding: $q_{\mathrm{b}}/\omega_{\mathrm{b}} \lesssim 0.06$ (100 GeV) to 0.02 (10 TeV) | ESTIMATE |
| a thin layer and a near-luminal $\chi$ | $q_{\mathrm{b}} \gg H$ (A-5) and $c_{\mathrm{b}}^2 = q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$ close to 1 ($c_{\mathrm{b}}$ the limiting speed of $\chi$ along ordinary space in units of the speed of light, the average of the warp $\mathrm{e}^{2H\lvert\sigma\rvert}$ over its profile) | DERIVED (A-5), ESTIMATE ($c_{\mathrm{b}}^2$, to first order in the momentum) |
| the effective number of neutrinos $N_{\mathrm{eff}}$ (Planck 2018; ACT DR6, the sixth data release of the Atacama Cosmology Telescope) | the right-handed neutrinos must not be thermalised by the portal: $c^{\nu}_X$ much smaller than the lepton-doublet couplings | DERIVED |

$$
H \ll q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}},\qquad \omega_{\mathrm{b}} \gtrsim 1.5\ \text{TeV},\qquad
\mathfrak{g}_{\mathrm{l}} \approx \frac{1}{\omega_{\mathrm{b}}}\sqrt{\frac{2\pi\cdot4\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle}{9}},\qquad c^{\nu}_X \ll c^{\ell}_X \tag{A-6}
$$
<!-- symbols: Hconst, qb, omegab, gportql, pi, mean, sigmaann, vrel, cf, iX -->
<!-- begin generated symbol list -->
**Symbols in (A-6).**

- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\mathfrak{g}_{\mathrm{q}},\ \mathfrak{g}_{\mathrm{l}},\ \mathfrak{g}_{\mathrm{p}}$: The current-portal couplings $\mathfrak{g}_f$ of FE-47 taken equal for all chiral quark states ($\mathfrak{g}_{\mathrm{q}}$) or for the nine chiral lepton states that take part, the six of the lepton doublets and the three right-handed charged leptons ($\mathfrak{g}_{\mathrm{l}}$), and the coupling to the proton that the lepton loop induces ($\mathfrak{g}_{\mathrm{p}}$). Unit: GeV$^{-2}$. Status: ESTIMATE.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\sigma_{\mathrm{ann}}$: The annihilation cross-section of the particles $\chi$ into Standard-Model particles (through the portals) in the normalisation of FE-61, where $n_\chi$ counts the four particle and the four antiparticle states of the bound level: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is a quarter of the annihilation rate $(\sigma\mathsf{v})_{\chi\bar\chi}$ of one particle $\chi_a$ with one antiparticle $\bar\chi_a$. Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathsf{v}$: The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product. Unit: dimensionless. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.

<!-- end generated symbol list -->

The window in which dirac16complex is the dark matter of UM-3: a weakly bound state ($q_{\mathrm{b}}$ a few per cent of its mass, with the
bulk scale $H$ smaller still), heavier than about 1.5 TeV, annihilating through current portals to the nine chiral lepton states
that take part (the six of the lepton doublets and the three right-handed charged leptons) with the coupling $\mathfrak{g}_{\mathrm{l}}$
($7.4\times10^{-8}$ GeV$^{-2}$ at 1 TeV, $7.4\times10^{-9}$ GeV$^{-2}$ at 10 TeV), with negligible quark portals and a negligible portal of the
right-handed neutrinos. Status: ESTIMATE. Within it the Kohn-Sham states are those of the weakly bound point of the equation of
state above: a cold, pressureless gas. Tests: direct detection through the lepton loop at the level $10^{-47}$ cm$^2$ for a few TeV
(within the reach of the next xenon experiments), and annihilation into charged leptons and neutrinos today, at the rate
$(\sigma\mathsf{v})_{\chi\bar\chi} \approx 9\times10^{-26}$ cm$^3$/s of one $\chi_a$ with one $\bar\chi_a$ (four times $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ of
FE-61), to be compared with the limits from gamma rays, positrons and neutrinos from the Galactic centre and dwarf galaxies for a
particle that is not its own antiparticle.

## The answer

dirac16complex can be the dark matter of UM-3: its bound states cannot decay into the Standard Model alone, gravitate as matter of
the fold, are cold, and have the measured density as a thermal relic, provided they are weakly bound, heavier than about 1.5 TeV
and leptophilic, and the right-handed neutrinos stay out of equilibrium. Status: DERIVED (no decay into the Standard Model alone,
gravitation, equation of state, relic density), ESTIMATE (the window), OPEN (the stability against the negative-energy states of
the indefinite charge).

# dirac16complex and the dark energy

$$
\begin{aligned}
&\frac{1}{\kappa_4}\,\hat G^\mu{}_\nu = \mathcal{T}_{\mathrm{SM}}{}^\mu{}_\nu + \mathcal{T}_{\mathrm{P}}{}^\mu{}_\nu + \mathcal{T}_{\mathrm{ff}}{}^\mu{}_\nu
 - \frac{V_*}{\kappa}\,\mathcal{J}^\mu{}_\nu,\qquad \mathcal{J}^a{}_b = \kappa\,\mathcal{S}^a{}_b\ \text{(the junction condition)},\\
&H_4^2 = \frac{8\pi G_{\mathrm{N}}}{3}\big(\rho_{\mathrm{SM}} + \rho_\chi + \rho_\Lambda\big),\qquad
 8\pi G_{\mathrm{N}} = \frac{\kappa_4}{1 + 5\epsilon_{\mathrm{r}}/6},\qquad \epsilon_{\mathrm{r}} = \frac{\kappa_4V_*}{\kappa H},\qquad
 \rho_\Lambda = \rho_{\mathrm{ff}} - \frac{31HV_*}{4\kappa},\\
&\frac{\hat R}{2\kappa_4} + q_{\mathrm{SM}} + q_\chi + q_{\mathrm{P}} + q_{\mathrm{ff}} = \frac{V_*}{\kappa}\,\mathcal{J}^{(r)}{}_{(r)},\qquad
 q_{\mathrm{SM}} = \big\langle\mathcal{L}_{\mathrm{H}} + \mathcal{L}_{\mathrm{gauge}} + \mathcal{L}_{\mathrm{f}} + \mathcal{L}_{\mathrm{Y}}\big\rangle,\qquad
 q_{\mathrm{P}} = \langle\mathcal{L}_{\mathrm{P}}\rangle
\end{aligned} \tag{FE-59}
$$
<!-- symbols: kappa4, Ghat, imu, inu, TSM, TP, Tff, Vstar, kappa, Jgeo, ia, ib, Sfoldsrc, H4, pi, GN, rhoSM, rhochi, rhoL, epsr, Hconst, rhoff, Rhat, qSM, qchi, qP, qff, ir, mean, LH, Lgauge, Lf, LY, LP -->
<!-- begin generated symbol list -->
**Symbols in (FE-59).**

- $\kappa_4$: The coupling of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_4/(1 + 5\epsilon_{\mathrm{r}}/6)$ (the Friedmann equation of the fold to first order in $\epsilon_{\mathrm{r}}$). Unit: GeV$^{-2}$. Value: $\kappa_4 \simeq 8\pi G_{\mathrm{N}} = 8\pi/M_{\mathrm{Pl}}^2$. Status: ASSUMED.
- $\hat G^\mu{}_\nu$: The Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold. Unit: 1/length$^2$. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\mathcal{T}_{\mathrm{SM}}$: The energy-momentum tensor of the Standard Model on the fold, $\mathcal{T}_{\mathrm{H}} + \mathcal{T}_{\mathrm{gauge}} + \mathcal{T}_{\mathrm{f}}$. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{P}}$: The energy-momentum tensor of the portals of dirac16complex. Unit: GeV$^4$. Status: DERIVED.
- $\mathcal{T}_{\mathrm{ff}}{}^a{}_b$: The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation). Unit: GeV$^4$. Status: ASSUMED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{J}^a{}_b$: The jump of the junction potential across the fold computed from the metric: the geometric side of the junction condition $\mathcal{J} = \kappa\mathcal{S}$, which equates it to $\kappa$ times the energy-momentum tensor $\mathcal{S}$ of everything on the fold. Unit: GeV. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with $\eta_{ab}$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); $\kappa\mathcal{S}$ is the jump of the potential $\mathfrak{F}$. Unit: GeV$^7$. Status: DERIVED.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity on the fold, $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{SM}}$: The energy density of the Standard-Model particles. Unit: GeV$^4$. Status: STANDARD.
- $\rho_\chi$: The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$ (FE-59). Unit: GeV$^4$. Status: DERIVED.
- $\epsilon_{\mathrm{r}}$: The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$. Unit: dimensionless. Value: $\lesssim 10^{-15}$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $31HV_*/(4\kappa)$ at the static block. Status: ASSUMED.
- $\hat R$: The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold. Unit: 1/length$^2$. Status: STANDARD.
- $q_{\mathrm{SM}}$: The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times). Unit: GeV$^4$. Status: DERIVED.
- $q_\chi$: The pressure of the bound states of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{P}}$: The pressure of the portals along the extra times: their mean on-shell Lagrangian density. Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times. Unit: GeV$^4$. Value: $-61HV_*/(8\kappa)$ at the static block. Status: ASSUMED.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->

The Einstein equations of the fold (FE-59): the dark energy of UM-3 is the vacuum energy of the fold
$\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$, the energy of the fold fluid minus the part that the kink of the static block
needs. Status: DERIVED (with the ASSUMED fold fluid).

$$
\rho_\Lambda = \Omega_\Lambda\,\rho_{\mathrm{c}}^{(0)} = 0.685\cdot\frac{3\big(H_4^{(0)}\big)^2}{8\pi G_{\mathrm{N}}} = 2.5\times10^{-47}\ \text{GeV}^4 = \big(2.2\ \text{meV}\big)^4 \tag{A-7}
$$
<!-- symbols: rhoL, OmegaL, rhoc, H4, pi, GN -->
<!-- begin generated symbol list -->
**Symbols in (A-7).**

- $\rho_\Lambda$: The vacuum energy density of the fold, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$ (FE-59). Unit: GeV$^4$. Status: DERIVED.
- $\Omega_\Lambda$: The density parameter of the dark energy (the vacuum energy of the fold) today. Unit: dimensionless. Value: 0.685 (Planck 2018). Status: DERIVED.
- $\rho_{\mathrm{c}}$: The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today. Unit: GeV$^4$. Value: $\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity on the fold, $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.

<!-- end generated symbol list -->

The vacuum energy that the measurements require ($H_4^{(0)} = 67.36$ km/s/Mpc $= 1.44\times10^{-42}$ GeV). Status: STANDARD.

Can dirac16complex be the dark energy? A dark energy needs a pressure close to minus its energy density, an equation of state
$w = P/\rho$ (pressure over energy density) close to $-1$. The gas of bound states has the pressure $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$
of its self-interaction (A-8), which is positive for a repulsive self-interaction and vanishes in the dilute limit
(KS_DE_EOS). The gas of $\chi$ is dark matter, not dark energy. The other contribution of dirac16complex to
the vacuum energy, the energy of its unoccupied and its negative-energy states (the sea, which the Kohn-Sham states leave out), is a
renormalisation of $\rho_\Lambda$ that UM-3 does not compute; its sign and size are OPEN, and with the indefinite Krein norm it is not
even clear that it is bounded. The dark energy of UM-3 is therefore the vacuum energy of the fold, a free parameter: its value
$(2.2\ \text{meV})^4$ is accommodated by choosing $\rho_{\mathrm{ff}}$, not explained, and it has $w = -1$ to the order of the power series
computed here (first order in $\epsilon_{\mathrm{r}} \lesssim 10^{-15}$). With the Planck 2018 parameters UM-3 reproduces the CMB, but it
keeps the tension of the cosmological-constant model with the BAO of DESI DR2 (2.3 standard deviations in DESI's analysis) and
cannot produce the evolving dark energy that DESI DR2 with the CMB prefers at 3.1 standard deviations: an equation of state
$w(a) = w_0 + w_a(1 - a)$ that changes with the scale factor $a = \mathrm{e}^{a_4}$ of the fold, with $w_0 > -1$ and $w_a < 0$. Status:
DERIVED (`um3_kohnsham.py`, K5, K7; `um3_cosmology.py`, C5: $w = -1$), STANDARD (DESI's significances), OPEN (the sea).

## The answer

No: dirac16complex is not the dark energy of UM-3. Its bound states are cold dark matter; the dark energy is the vacuum energy of the
fold, a free parameter with $w = -1$.

# What the author may have left out

The author asked to be told if something important was missing from his specification. UM-3 had to add the following, and the
analysis found the following problems.

| item | why it is needed or what it means | where it stands |
| ------ | ------ | ------ |
| right-handed quark singlets and the Yukawa couplings | the quark doublets alone have no masses and the hypercharges cancel the gauge anomalies only with the singlets | added (a default of UM-3, proposed in the notification of 17:20, which the author did not answer: ASSUMED) |
| three right-handed neutrinos | Dirac neutrino masses and the mixing that flavour conversion needs; the anomalies still cancel | added (accepted by the author, 17:32); they must never thermalise |
| the place of the Standard Model | in the bulk, every species would move with its own limiting speed and three neutrino profiles would oscillate wrongly; on the fold all share one light cone | the Standard Model lives on the fold (ASSUMED, motivated by the DERIVED limiting speeds) |
| a thin source at the fold | the kink of the warp $\mathrm{e}^{-H\lvert\sigma\rvert}$ requires one (the fold fluid); its energy above the static value is the dark energy | ASSUMED |
| an Einstein-Hilbert term of the fold | bulk gravitons move 2.74 times faster than light at the static block and have no time-kinetic term at the author's vacuum (the history $a_4 = Hx_4$ with constant $b_4$, which needs no sources in the bulk); gravitational waves move with the speed of light to $10^{-15}$ | ASSUMED (induced gravity) |
| a medium of the bulk | the static late-time bulk and the frozen extra times need bulk matter that violates the null energy condition | ASSUMED, no field theory given |
| the response of that medium | to first order in the bulk response, the component of the junction condition along the extra times (the radion condition) cannot be met by a rigid medium without changing the expansion law of the fold (dust would expand as $x_4^{5/6}$); a responding medium meets it with the radion mode, a combination of first-order jumps of the metric at the fold in the ratio $1 : -1 : 5$ that changes only that component | ASSUMED (the radion mode) |
| frozen extra times in the late universe (the size $\mathrm{e}^{-a_4}b_4$ of the extra times constant) | otherwise the couplings of the Standard Model change: in the author's vacuum ($a_4 = Hx_4$, $b_4$ constant) the gauge and Yukawa couplings grow as $\mathrm{e}^{3Hx_4/2}$, the quartic Higgs coupling and Newton's constant as $\mathrm{e}^{3Hx_4}$ | required |
| a gauge field for the ad hoc Higgs vacuum | the literal ad hoc vacuum carries an isospin charge that the Gauss law forbids; with the pure-gauge $W^2_{x_4}$ it is a rotated vacuum with one radial residual, and it must decay before nucleosynthesis | DERIVED |
| the Krein norm of dirac16complex | the signature $(4,4)$ of the author's matrices makes the charge indefinite: half of the bound states carry negative energy | OPEN (stability) |
| the extra times | fields that depend on them are tachyonic | ASSUMED (no dependence), OPEN |
| Lorentz violation in the bulk | the particles $\chi$ move faster than light on the fold unless $q_{\mathrm{b}} \gg H$ | a condition on the parameters |
| direct detection | the Higgs portal fixed by the binding and the quark portals are strongly constrained | a weakly bound, leptophilic $\chi$ above about 1.5 TeV |
| the dark energy | a vacuum energy with $w = -1$; DESI DR2 prefers an evolving one | OPEN (tension at 2.3 to 3.1 standard deviations) |
| the primordial era | the transition from the author's vacuum to the late universe and the primordial spectrum are not computed | OPEN (Planck inputs) |
| the lightest neutrino mass and the Dirac phase | not fixed by the specification | ASSUMED: $m_1 = 0$, phase 0 |
