---
title: "UM-3 provenance"
subtitle: 'Where every input of UM-3 comes from, every decision taken, every computation and its checks, the external data and software, and how to reproduce all of it'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Recorded by Claude (Anthropic)"
  - "Provenance of UM-3, 2026-10-24"
  - "Repository once-ere/Dirac_claude, folder universe_model_3"
---

# The fold: definition and examples

<!-- begin fold definition -->
**Definition.** The *fold* is the seven-dimensional surface of the author's eight-dimensional spacetime on which the
cosine of the angle $z = 6Hx_0$ of the hidden direction vanishes:

$$
\mathcal{F} = \big\{X = (x_0, x_1, \dots, x_7):\ \cos(6Hx_0) = 0\big\},\qquad
\text{in one period } 0 < z < \pi\text{ of the metric: } z = \frac{\pi}{2},\quad x_0 = \frac{\pi}{12H} \tag{FD-1}
$$
<!-- symbols: foldF, Xcoord, x0, x1, x7, Hconst, zvar, pi -->
<!-- begin generated symbol list -->
**Symbols in (FD-1).**

- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

$X = \{x_0, \dots, x_7\}$ are the author's coordinates: $x_0$ the hidden space-like direction, $x_1, x_2, x_3$ ordinary space,
$x_4$ the time, $x_5, x_6, x_7$ the three extra times; $H$ is the author's constant (an inverse length). The author's metric
depends on $x_0$ only through $\cot^2z$ and $(\sin^2z)^{1/6}$, so it repeats with the period $\pi/(6H)$ of $x_0$, and every
period $0 < z < \pi$ contains exactly one fold, at $z = \pi/2$. A point of the fold is labelled by the seven coordinates
$x_1, \dots, x_7$, and the metric restricted to the fold ($\mathrm{d}x_0 = 0$, $z = \pi/2$) is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N\big\vert_{\mathcal{F}} = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big) \tag{FD-2}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, foldF, euler, a4, b4, x1, x2, x3, x4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (FD-2).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

with three space-like and four time-like directions; $a_4$ and $b_4$ are the author's two functions of the time $x_4$.

**Why this surface is called a fold.** Measured by the proper distance along the hidden direction,

$$
\sigma = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H},\qquad \mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0,\qquad
\sin z = \mathrm{e}^{-6H\lvert\sigma\rvert} \tag{FD-3}
$$
<!-- symbols: sigma, sgn, pi, zvar, Hconst, diff, x0, euler -->
<!-- begin generated symbol list -->
**Symbols in (FD-3).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.

<!-- end generated symbol list -->

(the fold is $\sigma = 0$; the half-period $0 < z < \pi/2$ is $\sigma < 0$, the half-period $\pi/2 < z < \pi$ is $\sigma > 0$; the
two ends of the period, the tips $z \to 0$ and $z \to \pi$, lie at $\sigma \to -\infty$ and $\sigma \to +\infty$), the author's metric is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
 - \mathrm{d}x_4^2 \tag{FD-4}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, sigma, euler, Hconst, a4, b4, x1, x2, x3, x4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (FD-4).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

It depends on $\sigma$ only through $\lvert\sigma\rvert$. Four properties make the surface $\sigma = 0$ a fold, and together
they single it out within the period:

1. *It is a mirror.* The reflection $\sigma \to -\sigma$ (that is $z \to \pi - z$, or $x_0 \to \pi/(6H) - x_0$) maps the metric
   to itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
   period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are joined
   along the crease.
2. *The warp is largest on it.* The warp factor $(\sin^2z)^{1/6} = \mathrm{e}^{-2H\lvert\sigma\rvert}$, which multiplies ordinary
   space and the extra times, equals 1 on the fold and decreases on both sides.
3. *The metric has a kink on it.* The metric is continuous across the fold, but its first derivative along $\sigma$ jumps.
   The extrinsic curvature of the surfaces $\sigma = \text{const}$ changes sign across the fold,

$$
K^a{}_b = \frac12\,g^{ac}\,\partial_\sigma g_{cb}:\qquad
K^{1}{}_{1} = K^{2}{}_{2} = K^{3}{}_{3} = K^{5}{}_{5} = K^{6}{}_{6} = K^{7}{}_{7} = -H\,\mathrm{sgn}(\sigma),\qquad K^{4}{}_{4} = 0 \tag{FD-5}
$$
<!-- symbols: Kextr, ia, ib, ic, metric, partial, isigma, sigma, Hconst, sgn -->
<!-- begin generated symbol list -->
**Symbols in (FD-5).**

- $K^a{}_b$: The extrinsic curvature of a surface $\sigma = \mathrm{const}$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along ordinary space and the extra times, 0 along the time. Unit: GeV (1/length). Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $c$: A frame index (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.

<!-- end generated symbol list -->

   it jumps by $-2H$ along ordinary space and along the extra times. The Einstein-Lovelock equations are linear in the
   second $\sigma$-derivatives of the metric, so the jump puts a Dirac delta function $\delta_{\mathrm{D}}(\sigma)$ into them:
   the metric solves them only if the fold carries a thin source $\mathcal{S}^a{}_b$, an energy-momentum tensor concentrated
   on $\sigma = 0$ (the junction conditions). At the author's vacuum ($a_4' = H$, $b_4$ constant) its frame components along
   (ordinary space, the time, the extra times) are $\kappa\mathcal{S} = (-10H, -6H, -10H)$, at the static late-time state
   ($a_4$ and $b_4$ constant) $\kappa\mathcal{S} = (-61H/8, -31H/4, -61H/8)$, with $\kappa = 8\pi G_8$ the gravitational coupling of
   eight dimensions. The fold is therefore not only a place but a physical object: a thin layer that carries energy and
   momentum (a brane).
4. *The author's coordinate $x_0$ degenerates on it.* The metric component $g_{x_0x_0} = \cot^2(6Hx_0)$ vanishes on the fold
   and nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,

$$
\lvert\sigma\rvert = 3H\Big(x_0 - \frac{\pi}{12H}\Big)^2\Big[1 + 6H^2\Big(x_0 - \frac{\pi}{12H}\Big)^2 + \dots\Big] \tag{FD-6}
$$
<!-- symbols: sigma, Hconst, x0, pi -->
<!-- begin generated symbol list -->
**Symbols in (FD-6).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

   so the two coordinate values on either side of $x_0 = \pi/(12H)$ at the same coordinate distance lie at the same proper
   distance from the fold: the coordinate line of $x_0$ is folded onto the line of proper distances (a fold map, example 5).

**What lives on the fold.** In UM-3 the Standard Model (the Higgs doublet with the ad hoc vacuum, the gauge fields of
$SU(3)_C \times SU(2)_L \times U(1)_Y$, three generations of quarks and leptons and three right-handed neutrinos), the fold
fluid and the induced Einstein-Hilbert term of the fold live on the fold: they are fields at $\sigma = 0$, functions of
$x_1, \dots, x_4$ (no field depends on the extra times). Integrated over the extra times, the fold is the four-dimensional
universe that we observe, with the metric $\mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in
$x_1, \dots, x_4$. dirac16complex and gravity live in the bulk $\sigma \ne 0$ as well as on the fold; the bound states $\chi$
of dirac16complex are the part of it that the fold holds, and the portals couple dirac16complex to the Standard Model at
$\sigma = 0$. In UM-3 files the word *fold* means this surface and nothing else: a number of equal energy levels is
written as a number of degenerate states, and a growth by powers of Euler's number as a logarithm.

**Examples of folds that are meaningful for UM-3.**

1. *Our fold.* The fold $z = \pi/2$ of the period that contains our world (FD-1): the seven-dimensional world-volume of the
   Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
2. *The copies of the fold.* Because the metric repeats with the period $\pi/(6H)$, every surface
   $x_0 = \pi/(12H) + (\text{an integer multiple of } \pi/(6H))$ is a copy of the fold, one per period. Neighbouring copies are
   separated by a tip ($z$ a multiple of $\pi$), where the warp $(\sin^2z)^{1/6}$ vanishes and $g_{x_0x_0} = \cot^2z$
   diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
   line $-\infty < \sigma < \infty$. This is why the period $\pi/(6H)$ of $x_0$ produces no Kaluza-Klein tower with the spacing
   $12H$; the $x_0$ mass of the bound states is their binding to the fold.
3. *A folded sheet of paper.* The crease of a folded sheet is a fold in this sense: the two halves are mirror images
   (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
   In UM-3 the direction across the crease is the hidden direction $\sigma$, the seven directions along the crease are
   $x_1, \dots, x_7$, and the crease is the fold.
4. *A folded function.* The warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ is the simplest folded function: continuous,
   mirror symmetric, largest at $\sigma = 0$, with a jump of its derivative,

$$
\frac{\mathrm{d}}{\mathrm{d}\sigma}\mathrm{e}^{-2H\lvert\sigma\rvert} = -2H\,\mathrm{sgn}(\sigma)\,\mathrm{e}^{-2H\lvert\sigma\rvert},\qquad
\frac{\mathrm{d}^2}{\mathrm{d}\sigma^2}\mathrm{e}^{-2H\lvert\sigma\rvert} = 4H^2\,\mathrm{e}^{-2H\lvert\sigma\rvert} - 4H\,\delta_{\mathrm{D}}(\sigma) \tag{FD-7}
$$
<!-- symbols: diff, sigma, euler, Hconst, sgn, deltaD -->
<!-- begin generated symbol list -->
**Symbols in (FD-7).**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\delta_{\mathrm{D}}$: The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.

<!-- end generated symbol list -->

   whose delta function is the origin of the thin source of property 3. Every function of UM-3 that depends on $\sigma$
   through $\lvert\sigma\rvert$ is folded at $\sigma = 0$: the metric functions of FD-4 and the profiles of the bound states
   of dirac16complex (example 7).
5. *A fold map.* In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map $u \mapsto u^2$ of a line
   onto a half-line: it folds the line at $u = 0$, two points $\pm u$ land on the same point, and the derivative of the map
   vanishes on the fold. Near the fold the map from the author's coordinate $x_0$ to the distance $\lvert\sigma\rvert$ from the
   fold is of this kind (FD-6), and $g_{x_0x_0} = \cot^2z$, the square of the derivative $\mathrm{d}\sigma/\mathrm{d}x_0$,
   vanishes there.
6. *The brane of Randall and Sundrum.* The five-dimensional metric

$$
\mathrm{d}y_{\mathrm{RS}}^2 + \mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2
 - \mathrm{d}x_4^2\big),\qquad \lambda_{\mathrm{RS}} = \frac{6k_{\mathrm{RS}}}{\kappa_5},\qquad \Lambda_{\mathrm{RS}} = -\frac{6k_{\mathrm{RS}}^2}{\kappa_5} \tag{FD-8}
$$
<!-- symbols: diff, yRS, euler, kRS, x1, x2, x3, x4, lambdaRS, kappa5, LambdaRS -->
<!-- begin generated symbol list -->
**Symbols in (FD-8).**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $y_{\mathrm{RS}}$: The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-3). Unit: length. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $k_{\mathrm{RS}}$: The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-3). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\lambda_{\mathrm{RS}}$: The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^4$. Status: STANDARD.
- $\kappa_5$: The gravitational coupling of five dimensions in the model of Randall and Sundrum, $\kappa_5 = 8\pi G_5$ (FD-8, an example, not UM-3). Unit: GeV$^{-3}$. Status: STANDARD.
- $\Lambda_{\mathrm{RS}}$: The vacuum energy density of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^5$. Status: STANDARD.

<!-- end generated symbol list -->

   has a fold at $y_{\mathrm{RS}} = 0$ with the properties 1 to 3 (its coordinate $y_{\mathrm{RS}}$ is already the proper
   distance, so property 4 does not arise); Einstein's equations require there a brane of the tension
   $\lambda_{\mathrm{RS}}$ (Israel's junction condition) and in the bulk the vacuum energy $\Lambda_{\mathrm{RS}}$. The fold of UM-3 is
   of the same kind; it differs in that the time $x_4$ is not warped, three extra times are warped together with ordinary
   space, and the Lovelock terms add to the junction conditions.
7. *A particle bound to a thin layer.* A particle held by an attractive thin layer has a folded wave function: it falls off
   exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
   equation, the wave function itself). In UM-3 the particles $\chi$ of dark matter are the states of dirac16complex bound to
   the fold; at rest and without their self-interaction (the field is
   $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{-\mathrm{i}\omega_{\mathrm{b}}x_4}$)

$$
\begin{aligned}
&\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^+)\ \ (\sigma > 0),\qquad
\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^-)\ \ (\sigma < 0),\\
&\chi(0^+) = \exp\Big(\gamma^{(0)}\big(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}\big)\Big)\chi(0^-),\qquad
\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}
\end{aligned} \tag{FD-9}
$$
<!-- symbols: chiprof, sigma, euler, qb, gammaM, muX, PL, PR, omegab, mPsi -->
<!-- begin generated symbol list -->
**Symbols in (FD-9).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->

   where $\mu_{\mathrm{L}}$, $\mu_{\mathrm{R}}$ are the strengths of the fold for the left- and right-handed halves of
   dirac16complex (set by the Standard-Model fields on the fold) and $q_{\mathrm{b}} = -m_\Psi(\mu_{\mathrm{L}} + \mu_{\mathrm{R}})\tanh\varsigma/(2\varsigma)$,
   $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$ for $\mu_{\mathrm{R}} = 0$).
8. *The fold as a mirror for dirac16complex.* The reflection across the fold acts on the profiles $\chi(\sigma)$ in two ways,

$$
(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma),\qquad (\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma) \tag{FD-10}
$$
<!-- symbols: R1refl, R2refl, chiprof, sigma, Tmat -->
<!-- begin generated symbol list -->
**Symbols in (FD-10).**

- $\mathsf{R}_1$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of ordinary space, $(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma)$ (FD-10): a symmetry of dirac16complex, of gravity and of the mean field of the gas of the particles $\chi$; the bound states of Krein charge $-1$ are even, those of Krein charge $+1$ odd. Unit: dimensionless. Status: DERIVED.
- $\mathsf{R}_2$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of the extra times, $(\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma)$ (FD-10): it maps the bound states of one Krein charge onto those of the other. Unit: dimensionless. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

   ($T_a$ the author's Dirac matrices; for states at rest $\mathsf{R}_1$ is the reflection across the fold combined with the
   reflection of ordinary space, $\mathsf{R}_2$ the reflection across the fold combined with the reflection of the extra
   times). The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a
   state can carry the charge $-1$ or $+1$. $\mathsf{R}_1$ is a symmetry of dirac16complex, of gravity and of the mean
   field of a gas of the particles $\chi$: the four bound states of Krein charge $-1$ (the particles $\chi$) are even under
   it and the four of Krein charge $+1$ are odd, so the mean field of the gas cannot mix the two signs of the indefinite charge. $\mathsf{R}_2$ maps the
   bound states of one Krein charge onto those of the other and makes the two sets degenerate without the
   self-interaction.
9. *The planes of Horava and Witten.* In M-theory on an interval (a circle whose points are identified with their mirror
   images), the two ten-dimensional planes left in place by the reflection are mirror surfaces (property 1); the gauge
   fields $E_8 \times E_8$ live on them while gravity fills the bulk. This is the arrangement of UM-3, where the Standard
   Model lives on the fold and gravity and dirac16complex fill the bulk.

**What is not a fold.**

* *The tips* $z = 0$ and $z = \pi$ (mod $\pi$): the mirror exchanges them within a period, but there the warp vanishes,
  $g_{x_0x_0}$ diverges, and they lie at an infinite proper distance; they carry no thin source.
* *A smooth maximum of a warp*, such as $1/\cosh^2(H\sigma)$: mirror symmetric and largest at $\sigma = 0$, but without a kink
  and without a thin source.
<!-- end fold definition -->

# How to read this document

This document records the origin of everything in the universe model UM-3: the author's inputs and orders, the decisions taken
while building the model, the computations that verify every derived statement (each a Python script that checks itself), the
external measurements and software that were used, and the commands that reproduce every result and every document. It is a
record of origins, decisions and computations, not of the model itself, and so it contains no equations other than those of the
definition of the fold at its beginning.

The status labels used throughout UM-3: **AUTHOR** (from the author), **RECORD** (from the record of this repository),
**STANDARD** (textbook physics or a published measurement), **ASSUMED** (a choice without derivation), **INVENTED** (a new
interaction: the portals of dirac16complex), **DERIVED** (computed and verified), **ESTIMATE** (an order of magnitude),
**OPEN** (not settled).

# The author's inputs

| input | content and place |
| ---------------------- | ------------------------------------------------------------ |
| the order of 2026-10-24, 17:02 PDT | stop every earlier stage permanently; a new revision folder; read `4+4.nb` and verify its eight real $16 \times 16$ Dirac matrices; the new metric with $b_4^2$ ($b_4$ a function of the time $x_4$ in the extra-time components of the metric, never identically 1); the complete coupled field equations of the listed fields (Einstein-Lovelock gravity, the Higgs doublet with the ad hoc vacuum, three generations of lepton doublets, the right-handed electron, muon and tau, $W^1, W^2, W^3, B$, three generations of quark doublets, the gluons, dirac16complex coupled to gravity with a non-trivial spin connection and with its left- and right-handed halves coupled to every Standard-Model field, only the left-handed half to the Higgs field); new phenomenological interactions; an accurate approximate Kohn-Sham solution; the CMB, the CNB and the BAO with the metric as a power series; the $x_0$ mass mechanism; dark matter and dark energy; every equation and every symbol in every document, never a reference to another file; Markdown, LaTeX and PDF; push as soon as verified. In the author's private prompt file (not committed). |
| the notebook 4+4.nb | the author's notebook "eight, real-valued, 16 by 16, Dirac Matrices" (Wolfram 15.0) with the matrices `T16^A[0..8]`; copied unchanged into the folder `author_inputs` of UM-3 (its sha256 is given below) |
| the notebook of the record | `Dirac_Einstein-Lovelock_4+4_Nash.nb` in the root of the repository: the coordinates $X = \{x_0, \dots, x_7\}$ (Section DEFCHART: $x_0$ the hidden direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times) and the Lovelock weights $w = (1, 1/32, 1/1152)$ of the Einstein, Gauss-Bonnet and cubic terms with the cosmological-constant parameter $\Lambda_{\mathrm{N}} = 10$ of the notebook ($\Lambda = -10H^2$; In[134]) |
| the decision of 17:32 | "rather have three $\nu_{\mathrm{R}}$": three right-handed neutrinos, Dirac masses (in the conversation) |
| the reason of 17:34 | Gogilashvili and Tamborra, "Neutrino Flavor Conversion Shapes the Rate of Failed Core-collapse Supernovae", arXiv:2605.16504: why the flavour conversion of UM-3 must be correct (a third-party paper on the author's computer, read, not committed) |
| the standing rule of 2026-10-14 | no single calculation may take longer than 423 s (7 min 3 s); every command runs under a time limit (recorded in `claude_failures.md` and `HANDOFF.md` of the repository) |
| the order of 2026-10-25, 03:21 PDT | handle the sources on the fold: the fold needs a thin fluid and an Einstein-Hilbert term of its own (without the latter, bulk gravitons would travel 2.74 times faster than light); push |
| the order of 2026-10-25, 03:23 PDT | analyse and answer the open questions: the stability of the indefinite Krein norm of the charge of dirac16complex; fields that depend on the extra times (tachyonic); superluminal particles $\chi$ unless the binding is tight ($q_{\mathrm{b}} \gg H$); the primordial era, for which the Planck values were inputs; the lightest neutrino mass and the Dirac phase, which had been set to zero |
| the order of 2026-10-25, 03:54 PDT | define the fold clearly, correctly and precisely, with as many examples meaningful for UM-3 as possible, and present the same definition and examples in every file that uses the word, never referring to another file |
| the order of 2026-10-25, 05:09 PDT | give proper attribution to Claude for the stabiliser; discuss it in its own complete documentation with provenance (Markdown, LaTeX, PDF) for an ignorant but clever student of science; verify that it couples only to gravity, that it is absent in the primordial era, and that its existence and value are derived from the requirement of a static bulk; explain the static bulk with examples; define warp and warp factor; analyse its importance for UM-3 |

The sha256 of the author's notebook `4+4.nb` as received and committed:

```text
7ec1709a0028bce0b443f116cf27b5d3e670de7aa195659a9c3274527270429d
```

The author's private files (his prompt files, his notes, the third-party paper, his scratch notebook of 2026-10-16 with its
`.mx` files and the files `Generalized_Kronecker_Delta.*`) are never committed; the repository's `.gitignore` excludes them.

# The decisions taken in UM-3

| decision | reason | status |
| ------ | ------ | ------ |
| the proper coordinate $\sigma$ of the hidden direction; the fold at $z = \pi/2$ ($z = 6Hx_0$, the angle on which the metric depends) | the author's metric has a kink in $\sigma$ there, which the junction conditions turn into a thin source | DERIVED |
| the Standard Model on the fold, dirac16complex in the bulk | species in the bulk have different limiting speeds and neutrino profiles would spoil flavour conversion | ASSUMED (motivated by the DERIVED limiting speeds) |
| right-handed quark singlets and Yukawa couplings | masses of the quarks and cancellation of the anomalies (defaults of the notification of 17:20; the author answered only on the neutrinos) | ASSUMED |
| three right-handed neutrinos | the author's decision of 17:32 | AUTHOR |
| the induced gravity of the fold | bulk gravitons move faster than light and have no time-kinetic term at the author's vacuum; with the graviton term that the Lovelock terms give the fold, the gravitational waves still move with $c_{\mathrm{g}}^2 = 83/82$; GW170817 requires the induced term to provide all but $1.3\times10^{-13}$ of the gravity of the fold | ASSUMED (the term), DERIVED (the need and the bound) |
| the fold fluid and the stabiliser | the kink at the fold and the late-time bulk need sources: without a bulk source no instant has both rates of the metric below $0.477H$, and the static bulk needs exactly the stabiliser, which Claude found and named on 2026-10-24 | DERIVED (that sources are needed, and their values), ASSUMED (that they are separate media) |
| the responding bulk medium (the radion mode) | a rigid medium would change the expansion law of the fold | ASSUMED |
| the portals of dirac16complex | the author's request for couplings of both halves to every Standard-Model field, only the left-handed half to the Higgs field | INVENTED |
| the pure-gauge $W^2$ of the ad hoc vacuum | the Gauss law of $SU(2)$ | DERIVED |
| no dependence of any field on the extra times | such fields are tachyonic; the restriction is consistent but unstable, and a gauge principle that removes the momentum along the extra times is needed | ASSUMED (OPEN: the gauge principle) |
| the lightest neutrino mass zero, the Dirac phase zero | not fixed by the specification; the phase drops out of every result of UM-3, and DESI DR2 bounds the lightest mass below 4.12 meV | ASSUMED (the mass within the bound), DERIVED (the phase is irrelevant) |
| the primordial spectrum, the optical depth and the densities from Planck 2018 | the author's vacuum gives a spectrum with $n_{\mathrm{S}} - 1 = 2.5$; the observed one needs an inflationary era with frozen extra times, which UM-3 does not contain | ASSUMED (inputs; the era OPEN) |
| the quantisation of dirac16complex with positive energies | it makes the vacuum stable; the modes of positive Krein charge are then ghosts, which the chiral couplings of the fold produce | DERIVED (the consequences), OPEN (a unitary coupling) |
| one definition of the fold in every file | the order of 2026-10-25, 03:54: the definition with its examples, `docs_src/fold_definition.md` for the documents and `docs_src/fold_definition.txt` for the code and the JSON files, inserted and checked by `tools/fold_block.py` | AUTHOR (the order) |
| a document of its own for the stabiliser of the bulk, `STABILISER.md` | the order of 2026-10-25, 05:09: the stabiliser was found, introduced and named by Claude (Anthropic) on 2026-10-24 (the gravity module, check G4, and the term IN-7 of the field equations); the document explains it for a newcomer, verifies the five points of the order with the eight checks of `um3_stabiliser.py`, and records its provenance | AUTHOR (the order) |
| the Kohn-Sham module in parts | the standing rule of 423 s: the module runs in six parts with snapshots, each under the time limit, and an assembly that reproduces the single run exactly | AUTHOR (the rule) |

The stabiliser of the bulk enters the action of UM-3 only through its energy-momentum tensor, which the static late-time
bulk fixes completely (the value DERIVED, the medium ASSUMED; found, introduced and named by Claude on 2026-10-24); its frame
components, in the order of the directions $\sigma$, $x_1$, $x_2$, $x_3$, $x_4$, $x_5$, $x_6$, $x_7$, are

$$
\mathcal{T}_{\mathrm{stab}}{}^a{}_b = \mathrm{diag}\big(p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}},
 -\rho_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}\big),\qquad
\kappa\rho_{\mathrm{s}} = -\frac{H^2}{16},\qquad \kappa p_{\mathrm{s}} = -\frac{5H^2}{16} \tag{IN-7}
$$
<!-- symbols: Tstab, ia, ib, diag, ps, rhos, kappa, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-7).**

- $\mathcal{T}_{\mathrm{stab}}{}^a{}_b$: The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric requires, found and named by Claude (Anthropic) on 2026-10-24. Unit: GeV$^8$. Status: DERIVED (the value), ASSUMED (a separate medium).
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $p_{\mathrm{s}}$: The pressure of the stabiliser (equal along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Value: $\kappa p_{\mathrm{s}} = -5H^2/16$. Status: DERIVED (the value), ASSUMED (a separate medium).
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser; with frozen extra times it is the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$. Status: DERIVED (the value), ASSUMED (a separate medium).
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

# The computations

Every derived statement rests on one of these scripts in `universe_model_3/code/`. Each computes, checks itself and writes its
results to `universe_model_3/outputs/` and its checks to `universe_model_3/reports/`.

| script | what it computes | checks |
| ------ | ------ | ------ |
| `um3_gammas.py` | the author's Dirac matrices, rebuilt from `4+4.nb` (a library) | |
| `um3_dirac_matrices.py` | reality, Clifford relations, Spin(4,4) and Pin(4,4), chiral projectors, agreement with every stored output of the notebook | 55 |
| `um3_dirac_matrices_doc.py` | the document `dirac matrices` from the checked results | |
| `um3_lovelock.py` | the Lovelock tensors by the generalised Kronecker delta (a library) | |
| `um3_geometry.py` | the exact curvature and Einstein-Lovelock equations of the author's metric, the author's vacuum, the spin connection | 26 |
| `um3_fold.py` | the proper chart, the general warped metric, the junction potential and the fold sources, the conservation law at the fold | 13 |
| `um3_bulk.py` | the zero modes and the speeds of the bulk fields | 10 |
| `um3_fields.py` | the bilinears of dirac16complex, the Krein operator, the electroweak vacuum with the ad hoc component, the anomalies | 16 |
| `um3_spectra.py` | the bound states of dirac16complex with the exact matrices | 5 |
| `um3_neutrino.py` | the flavour blindness of the portals, the matter conversion, the crossing criterion, the equipartition, the cosmic neutrino background (CNB) | 5 |
| `um3_background.py` | the histories of the background, the energy conditions, the ad hoc vacuum as a gauge rotation | 6 |
| `um3_series.py` | the first-order terms of the power series of the metric, the radion condition | 6 |
| `um3_kohnsham.py` | the self-consistent Kohn-Sham states of dirac16complex in three regimes and at a weakly bound point | 9 |
| `um3_flavour.py` | the neutrino flavours in the Sun and in supernovae | 4 |
| `um3_thermal.py` | the degrees of freedom, the relic density, the portals and direct detection, the right-handed neutrinos | 6 |
| `um3_cosmology.py` | the cosmic microwave background (CMB), the CNB and the baryon acoustic oscillations (BAO) with the Boltzmann code CAMB and an independent background, against Planck 2018 and DESI DR2 (the second data release of the Dark Energy Spectroscopic Instrument) | 6 |
| `um3_foldsources.py` | the gravitational wave of the fold: its thin part from the Lovelock terms, its speed without and with the induced gravity, the bound from GW170817; the gravity induced by the fields of the fold; the two parts of the fold fluid | 6 |
| `um3_stabiliser.py` | the stabiliser of the bulk: the source that the static bulk requires, its absence at the author's vacuum, its conservation, its energy conditions and the ghost field, its history, the flow of energy into the fold and the energy balance of the fold, its importance, the constraints of the bulk equations | 8 |
| `um3_krein.py` | the Krein form and its quantisation, the symmetries and mirrors of the bound states, the flat directions and the growing modes of the gas, the selection rules at the fold, stability and unitarity (reads the snapshots of `um3_kohnsham.py`) | 7 |
| `um3_extratimes.py` | fields with a momentum along the extra times: the dispersion, the bound states and their leaking, the growth in the author's vacuum and in the late universe, the truncation | 5 |
| `um3_superluminal.py` | the limiting speed of the particles $\chi$, their dispersion up to large momenta, the speeds of cosmological $\chi$, the shortcut through the bulk, the loop estimate for the electron | 5 |
| `um3_primordial.py` | the fields of the fold in the author's vacuum, their spectrum, the growth of the couplings, the bound on an inflationary era, Higgs inflation against induced gravity | 5 |
| `um3_numass.py` | the lightest neutrino mass and the Dirac phase: the masses of both orderings, the bounds of DESI DR2 and KATRIN, the phase in the results of UM-3, the effect of the lightest mass, the record against NuFIT 6.0 | 5 |

The documents are written in Markdown and built with `universe_model_3/tools/build_docs.py` (pandoc to LaTeX, pdflatex to PDF,
deterministic). `universe_model_3/docs_src/registry.py` holds the meaning, unit, value and status of every symbol;
`universe_model_3/tools/make_inventory.py` writes the inventory of the tagged equations from `FIELD_EQUATIONS.md`, and
`universe_model_3/tools/symbols_tool.py` copies every tagged equation into the other documents (`sync`), writes the symbol list
after every display (`expand`) and checks that every symbol of every display is defined and every tagged equation is written
identically in every document (`check`). `universe_model_3/tools/fold_block.py` inserts the one definition of the fold into every
file that uses the word (`insert`) and checks that every such file carries it word for word (`check`).

# External measurements and software

| source | used for |
| ------ | ------ |
| Planck Collaboration, Planck 2018 results VI, A&A 641, A6 (2020), Table 2 (TT,TE,EE+lowE+lensing) | the cosmological parameters and the derived quantities of the CMB |
| Planck 2018 plik-lite likelihood files (Planck Legacy Archive), via github.com/heatherprince/planck-lite-py | the CMB spectra (downloaded at run time into `universe_model_3/external/`, not redistributed) |
| DESI Collaboration, DESI DR2 Results II, arXiv:2503.14738, Table IV | the BAO distances; the 2.3 and 3.1 standard-deviation statements of its abstract |
| ACT Collaboration (Atacama Cosmology Telescope), DR6 constraints on extended cosmological models, arXiv:2503.14454 | $N_{\mathrm{eff}} = 2.86 \pm 0.13$ and $2.89 \pm 0.11$, $\sum m_\nu < 0.082$ eV |
| Borexino Collaboration, Nature 562, 505 (2018) | the survival probabilities of solar neutrinos |
| the global fit NuFIT 5.2 of the neutrino oscillation data (Esteban, Gonzalez-Garcia, Maltoni, Schwetz and Zhou, JHEP 09 (2020) 178; version 5.2 of November 2022 at www.nu-fit.org), normal ordering with the Super-Kamiokande atmospheric data | $\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$, $\Delta m^2_{21} = 7.41\times10^{-5}$ eV$^2$, $\Delta m^2_{31} = 2.511\times10^{-3}$ eV$^2$ |
| Particle Data Group, Review of Particle Physics (2022) | the masses of the Higgs boson (125.25 GeV), of the quarks and charged leptons and of the nucleon, the Fermi constant $1.1663788\times10^{-5}$ GeV$^{-2}$ and $v = 246.22$ GeV, the fine-structure constant |
| DESI Collaboration, DESI DR2 Results II, arXiv:2503.14738 | the bound $\sum m_\nu < 0.064$ eV (95%, DESI DR2 with the CMB, cosmological-constant model) |
| LUX-ZEPLIN (LZ) Collaboration, Phys. Rev. Lett. 135, 011802 (2025), arXiv:2410.17036 version 3 (4.2 tonne-years) | the limit $2.2\times10^{-48}$ cm$^2$ at 40 GeV (90% confidence) on spin-independent scattering |
| Long, Lunardini and Sabancilar, arXiv:1405.7654 | the capture rate of the CNB on tritium (4 and 8 per year per 100 g for Dirac and Majorana neutrinos) |
| Gogilashvili and Tamborra, arXiv:2605.16504 (version 3) | the flavour equipartition (the equal sharing of the three flavours that fast flavour conversion produces) and its effect on the explosions of massive stars |
| Bahcall's exponential solar density profile; Petcov's crossing probability; Keil, Raffelt and Janka's spectral shape; Izaguirre, Raffelt and Tamborra's dispersion relation; Morinaga's crossing theorem; Ma and Bertschinger's Boltzmann equations | the standard physics named in the documents |
| CAMB 2.0.5 (Lewis, Challinor and Lasenby) | the Boltzmann hierarchy and the CMB spectra |
| the global fit NuFIT 6.0 (Esteban, Gonzalez-Garcia, Maltoni, Schwetz and Zhou, JHEP 12 (2024) 216, arXiv:2410.05380), data set IC24 with the Super-Kamiokande atmospheric data | $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta_{\mathrm{CP}} = 212^\circ$, $\Delta m^2_{21} = 7.49\times10^{-5}$ eV$^2$, $\Delta m^2_{31} = 2.513\times10^{-3}$ eV$^2$ (normal ordering), and the inverted ordering, for the comparison with the record |
| KATRIN Collaboration, Science 388 (2025) 180 | the limit 0.45 eV (90%) on the effective electron-neutrino mass of tritium beta decay |
| BICEP/Keck Collaboration, Phys. Rev. Lett. 127, 151301 (2021) | the bound $r < 0.036$ (95%) on the tensor-to-scalar ratio |
| LIGO Scientific, Virgo, Fermi GBM and INTEGRAL Collaborations, Astrophys. J. Lett. 848, L13 (2017) | the speed of gravitational waves, $-3\times10^{-15} < c_{\mathrm{g}} - 1 < 7\times10^{-16}$ (GW170817 and GRB 170817A) |
| A. D. Sakharov, Dokl. Akad. Nauk SSSR 177, 70 (1967); D. V. Vassilevich, Phys. Rep. 388, 279 (2003) | induced gravity; the heat-kernel coefficients of scalars, fermions and gauge fields |
| B. Altschul, Phys. Rev. Lett. 96, 201101 (2006); the inverse-Compton electrons of the Crab nebula (energy up to $2\times10^8$ electron masses) | the bounds on the maximal speed of electrons: slower than light by less than $6\times10^{-20}$ (synchrotron), faster by less than $1/(2\cdot(2\times10^8)^2) = 1.2\times10^{-17}$ (no vacuum Cherenkov radiation) |
| A. I. Shlyakhter, Nature 264, 340 (1976); T. Damour and F. Dyson, Nucl. Phys. B 480, 37 (1996) | the bound of the natural reactor of Oklo on the change of the fine-structure constant over 1.8 Gyr |
| S. Dubovsky, T. Grégoire, A. Nicolis and R. Rattazzi, JHEP 03 (2006) 025; J. M. Cline, S. Jeon and G. D. Moore, Phys. Rev. D 70, 043543 (2004) | the instabilities of media that violate the null energy condition, and of ghosts |
| A. Einstein (1917); A. S. Eddington (1930); K. Schwarzschild (1916); R. V. Pound and G. A. Rebka (1960); D. Lovelock (1971); L. Randall and R. Sundrum (1999) | the examples and the standard physics of the document on the stabiliser |
| Python 3.13.17 with numpy 2.5.3, scipy 1.18.1, sympy 1.14.0, mpmath, matplotlib 3.11.2; pandoc 3.1.3; pdfTeX (TeX Live 2023) | every computation and document |

# How to reproduce

From the root of a clone of the repository, with the software above installed:

```text
python universe_model_3/code/um3_dirac_matrices.py
python universe_model_3/code/um3_geometry.py
python universe_model_3/code/um3_fold.py
python universe_model_3/code/um3_bulk.py
python universe_model_3/code/um3_fields.py
python universe_model_3/code/um3_spectra.py
python universe_model_3/code/um3_neutrino.py
python universe_model_3/code/um3_background.py
python universe_model_3/code/um3_series.py
python universe_model_3/code/um3_flavour.py
python universe_model_3/code/um3_thermal.py
python universe_model_3/code/um3_cosmology.py
python universe_model_3/code/um3_kohnsham.py part K1
python universe_model_3/code/um3_kohnsham.py part I
python universe_model_3/code/um3_kohnsham.py part II
python universe_model_3/code/um3_kohnsham.py part III
python universe_model_3/code/um3_kohnsham.py part K6
python universe_model_3/code/um3_kohnsham.py part K9
python universe_model_3/code/um3_kohnsham.py assemble
python universe_model_3/code/um3_foldsources.py
python universe_model_3/code/um3_stabiliser.py
python universe_model_3/code/um3_krein.py
python universe_model_3/code/um3_extratimes.py
python universe_model_3/code/um3_superluminal.py
python universe_model_3/code/um3_primordial.py
python universe_model_3/code/um3_numass.py
python universe_model_3/docs_src/registry.py
python universe_model_3/tools/make_inventory.py
python universe_model_3/tools/symbols_tool.py sync
python universe_model_3/tools/fold_block.py insert
python universe_model_3/tools/symbols_tool.py check
python universe_model_3/tools/fold_block.py check
python universe_model_3/tools/build_docs.py
```

Every script prints one line per check and ends with "n/n checks passed"; `um3_series.py` reads the output of `um3_fold.py`,
`um3_stabiliser.py` reads it too, `um3_krein.py` reads the snapshots of the parts of `um3_kohnsham.py`, and `um3_cosmology.py`
downloads the Planck files once (about 7 MB). By the standing rule no single calculation may take longer than 423 seconds: each command
is run under `timeout 423`; a part of `um3_kohnsham.py` that reaches its own limit of 400 seconds saves its state and exits with the code
3, and is then simply run again until it exits with 0 (the six parts together take about 37 minutes of computing; the longest single
module otherwise is `um3_krein.py`, about 4.5 minutes). The documents are rebuilt identically (no dates in the LaTeX, fixed PDF
metadata).
