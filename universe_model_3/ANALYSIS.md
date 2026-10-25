---
title: "UM-3 analysis"
subtitle: 'The x0 mass mechanism, dirac16complex as dark matter and as dark energy, and what the author may have left out'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Analysed and verified by Claude (Anthropic)"
  - "Analysis of UM-3, 2026-10-24"
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

## What this document contains

The author asks for three analyses of the universe model UM-3: the mass mechanism along the hidden coordinate $x_0$ (the period
$\pi/(6H)$ of the metric and the uncertainty relation), whether dirac16complex can be the dark matter, and whether it can be the
dark energy. He also asks to be told what he may have left out, and (on 2026-10-25) for answers to the questions that UM-3 had left
open. This document gives the answers. It is self-contained: every
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
* **The open questions answered**: whether the indefinite Krein norm of dirac16complex is stable, what fields that depend on the
  extra times do, whether the particles $\chi$ move faster than light, the primordial era, and the lightest neutrino mass and the
  Dirac phase.
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
2. **Dark matter.** The bound particles $\chi$ of dirac16complex cannot decay into the Standard Model alone (and the indefinite Krein
   norm of their charge does not destabilise the dilute gas or the vacuum, item 5), gravitate on the fold like matter of the fold,
   form a pressureless gas in the dilute limit, and are a thermal relic with the measured density if they annihilate with
   $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 2.2\times10^{-26}$ cm$^3$/s (in the normalisation in which their number density counts all eight
   states of the bound level; one $\chi$ with one antiparticle annihilates four times faster). Direct detection by the LUX-ZEPLIN
   experiment excludes this through the quark portals, allows it through the lepton portals above about 1.5 TeV, and requires the
   binding to be weak ($q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}}$ at a few TeV); the right-handed neutrinos must not be thermalised.
   dirac16complex can be the dark matter in this window (DERIVED, ESTIMATE).
3. **Dark energy.** No: the gas of bound states has a positive pressure that vanishes in the dilute limit, never a negative one.
   The dark energy of UM-3 is the vacuum energy of the fold, a free parameter whose pressure is minus its energy density ($w = -1$,
   $w$ the ratio of pressure to energy density); it fits the cosmic microwave background (CMB) but keeps the tension of the
   cosmological-constant model with the baryon acoustic oscillations (BAO) of DESI DR2, 2.3 standard deviations in DESI's own
   analysis (DERIVED: $w = -1$; STANDARD: the tension).
4. **What was left out.** UM-3 had to add right-handed quarks and Yukawa couplings, three right-handed neutrinos (accepted by the
   author), a thin fluid and an Einstein-Hilbert term on the fold, a medium in the bulk that violates the null energy condition
   and must respond to the fold, the gauge field that the author's ad hoc Higgs vacuum needs (the doublet $(\mathcal{A}, v + h)/\sqrt2$
   with the decaying upper component $\mathcal{A} = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$), and it found several open problems. The last
   section lists them.
5. **The open questions.** The Krein norm: the vacuum is stable and the dilute gas of $\chi$ is stable, the dense gas is not, and the
   chiral couplings of the fold (the author's left-handed Higgs portal among them) produce ghosts, so UM-3 with them is not unitary.
   The extra times: every field with a momentum along them is tachyonic; UM-3 needs a gauge principle that removes that momentum. The
   speed of $\chi$: superluminal by at most 0.45 per cent in group velocity, with the front velocity of light and no causal paradox,
   but the Standard Model inherits it through loops unless $q_{\mathrm{b}}/H > 4\times10^{10}$. The primordial era: the author's vacuum gives a
   spectrum with $n_{\mathrm{S}} - 1 = 2.5$; an inflationary era with frozen extra times is needed, which UM-3 does not contain. The neutrinos:
   the Dirac phase drops out of every result of UM-3; the lightest mass is below 4.12 meV and changes only the capture rate of the
   cosmic neutrinos (DERIVED, ESTIMATE; OPEN: a unitary coupling, the gauge principle, the inflaton).

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
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathcal{Q}_o$: The charge $Q_\Psi$ (the Krein charge) of the single-particle state $o$ of dirac16complex, a Kohn-Sham orbital or a mode: $+1$ or $-1$ for a normalised state. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The portals of dirac16complex to the Standard Model (IN-16) and its conserved charge (FE-43). Every portal term, like the bulk
Lagrangian and the self-interaction, contains dirac16complex only in the bilinears $\bar\Psi\cdots\Psi$: the action is invariant under
a constant change of the phase of $\Psi$, and the charge $Q_\Psi$ is conserved. A particle $\chi$ (a bound state of dirac16complex)
can therefore annihilate only with an antiparticle, and the lightest states of dirac16complex, the bound states of the fold, cannot
decay into the Standard Model alone. Conservation of $Q_\Psi$ does not by itself make them stable, because the charge is a Krein
form (indefinite): with $E_o = -\omega_o\mathcal{Q}_o$, a particle $\chi$ of positive energy (charge $-1$ at $+\omega_{\mathrm{b}}$) could turn
into a state of negative energy with the same charge (at $-\omega_{\mathrm{b}}$) and Standard-Model quanta that carry away
$2\omega_{\mathrm{b}}$. The quantisation of the charge settles this (the section on the open questions, FE-67): in the positive-energy
quantisation every quantum carries a positive energy, so no such decay exists and the vacuum is stable; the dilute gas is stable,
the dense gas is not, and the chiral portals produce ghosts. Status: DERIVED (no decay into the Standard Model alone, from the form of
IN-16; the Krein signature of the charge, `um3_fields.py`, F3, and `um3_spectra.py`, S4; the quantisation, `um3_krein.py`).

## Gravitation on the fold

$$
\kappa\int_{\text{layer}}\mathcal{T}_\Psi{}^a{}_b\,\mathrm{d}\sigma = \frac{\kappa}{\mathcal{Z}\,V_*}\,\mathcal{T}_\chi{}^a{}_b\qquad\big(H \ll q_{\mathrm{b}}\big) \tag{A-5}
$$
<!-- symbols: kappa, TPsi, ia, ib, diff, sigma, Zfold, Vstar, Tchi, Hconst, qb -->
<!-- begin generated symbol list -->
**Symbols in (A-5).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
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

$$
\mathsf{E}_{\mathrm{int}} = \frac{G_{\mathrm{KS}}}{2}\int_{-\infty}^{\infty}\mathrm{d}\sigma\,\mathrm{e}^{6H\lvert\sigma\rvert}\Big(\hat\rho^2 - \mathrm{tr}\,\hat{\mathcal{N}}^2\Big),\qquad
\epsilon_{\mathrm{p}} = \omega - \mathsf{E}_{\mathrm{int}},\qquad P_{\mathrm{KS}} = n_\chi\,\mathsf{E}_{\mathrm{int}},\qquad
w_\chi = \frac{P_{\mathrm{KS}}}{n_\chi\,\epsilon_{\mathrm{p}}} \tag{A-8}
$$
<!-- symbols: Eint, GKS, diff, sigma, infty, euler, Hconst, rhohat, trace, Nhat, epsp, omegafreq, PKS, nchi, wchi -->
<!-- begin generated symbol list -->
**Symbols in (A-8).**

- $\mathsf{E}_{\mathrm{int}}$: The interaction energy per particle of the gas of $\chi$: the mean self-interaction energy $\frac{\lambda_\Psi}{2}(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2)$ integrated across the hidden direction, per particle. Unit: GeV. Status: DERIVED.
- $G_{\mathrm{KS}}$: The dimensionless strength of the self-interaction of the gas of particles $\chi$ in the Kohn-Sham states: the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold divided by the volume $V_*$ of the extra times, $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ (in units of $m_\Psi$ when numbers are given). Unit: dimensionless. Value: $10^{-6}$ to 1 in the solutions. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\hat\rho(\sigma)$: The scalar density of the occupied orbitals, $\hat\rho = \frac14\sum_o\bar\chi_o\chi_o$ (per particle); the scalar density of the gas is $n_{\mathrm{s}} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat\rho$. Unit: GeV. Status: DERIVED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\hat{\mathcal{N}}(\sigma)$: The one-body density matrix of the occupied orbitals, $\hat{\mathcal{N}} = \frac14\sum_o\chi_o\bar\chi_o$ (a $16 \times 16$ matrix at each $\sigma$, per particle); the density matrix of the gas is $\mathcal{N} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat{\mathcal{N}}$. Unit: GeV. Status: DERIVED.
- $\epsilon_{\mathrm{p}}$: The energy per particle of the gas of $\chi$: the orbital energy minus the interaction energy per particle, which the orbital energy counts twice. Unit: GeV. Status: DERIVED.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $P_{\mathrm{KS}}$: The pressure of the gas of $\chi$ along ordinary space in the Kohn-Sham state: the particles are at rest, so it is the mean self-interaction, $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$. Unit: GeV$^4$. Status: DERIVED.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $w_\chi$: The equation of state of the gas of the particles $\chi$: its pressure divided by its energy density, $w_\chi = P_{\mathrm{KS}}/(n_\chi\epsilon_{\mathrm{p}})$ (0 for cold dark matter, $-1$ for a vacuum energy). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The equation of state of a homogeneous gas of the particles $\chi$ at rest on the fold, from its self-consistent Kohn-Sham states.
Each particle occupies one of the four positive-energy states of the bound level, with the field
$\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi_o(\sigma)\,\mathrm{e}^{-\mathrm{i}\omega x_4}$; the profiles $\chi_o$ obey the Dirac equation along the hidden
direction with the mean field $G_{\mathrm{KS}}\,\mathrm{e}^{6H\lvert\sigma\rvert}(\hat\rho\,\mathbf{1} - \hat{\mathcal{N}})$ of the self-interaction added to the
mass, where $\hat\rho$ and $\hat{\mathcal{N}}$ are the scalar density and the density matrix of the profiles, $\mathrm{e}^{6H\lvert\sigma\rvert}$ is the warp
of the proper density, and $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ is the dimensionless strength of the self-interaction (the self-coupling
$\lambda_\Psi$ of dirac16complex times the number density $n_\chi$ of the particles on the fold, divided by the volume $V_*$ of the
extra times). $\omega$ is the orbital energy, $\mathsf{E}_{\mathrm{int}}$ the interaction energy per particle, $\epsilon_{\mathrm{p}}$ the energy per
particle (the orbital energy counts the interaction twice), and $P_{\mathrm{KS}}$ the pressure: the particles are at rest and do not
depend on the extra times, so only the self-interaction contributes, along ordinary space and along the extra times alike;
$w_\chi$ is the equation of state, the pressure over the energy density. Status: DERIVED.

The Kohn-Sham equations were solved (in units of $m_\Psi$, with the Higgs portal of the vacuum, $q_{\mathrm{b}} = 0.3$) in three regimes of
the bulk scale: $H = 0.05$, where the proper density of the bound state without the self-interaction decays away from the fold;
$H = 0.15$, where it grows but the first-order shift of the level is finite; and $H = 0.3$, where both grow. In every regime and at
every coupling from $G_{\mathrm{KS}} = 10^{-6}$ to 1 the self-interaction is repulsive for $\lambda_\Psi > 0$, the level rises, and the
pressure is positive: $w_\chi$ takes the values $7.2\times10^{-8}$, $2.1\times10^{-7}$, $4.7\times10^{-5}$ at $G_{\mathrm{KS}} = 10^{-6}$ and 0.056, 0.137, 0.224 at $G_{\mathrm{KS}} = 1$ in the three regimes. Where the proper
density would grow, the repulsion makes it saturate at a constant value far from the fold, and the level can rise above the
threshold $m_\Psi$ of the free continuum without unbinding (at $G_{\mathrm{KS}} = 0.371$ and $0.142$ in the first two regimes). At a
weakly bound point of the window below ($q_{\mathrm{b}} = 0.03$, $H = 0.002$) the self-consistent shift approaches first-order
perturbation theory as $G_{\mathrm{KS}} \to 0$ and $w_\chi$ takes the values $6.2\times10^{-7}$, $6.2\times10^{-6}$, $5.8\times10^{-5}$ at $G_{\mathrm{KS}} = 10^{-4}$, $10^{-3}$ and $10^{-2}$. Status: DERIVED
(`um3_kohnsham.py`, K3, K7, K8, K9; 9 checks).

How dilute is the gas of the universe? With the self-coupling of the natural size $\lambda_\Psi = m_\Psi^{-6}$ and extra times of the size
$1/m_\Psi$ ($V_* = m_\Psi^{-3}$), $G_{\mathrm{KS}} = n_\chi/m_\Psi^3$; for $m_\Psi = 1.5$ TeV and the density of dark matter near the Sun
($0.4$ GeV/cm$^3$, $n_\chi = 2.7\times10^{-4}$ cm$^{-3}$) this is $G_{\mathrm{KS}} \approx 6\times10^{-55}$, and the mean density of the universe is
smaller still. $G_{\mathrm{KS}}$ reaches $10^{-6}$ only if $\lambda_\Psi/V_*$ is larger by a factor of about $10^{48}$; extra times of the
Planck length ($V_* = M_{\mathrm{Pl}}^{-3}$) give $5\times10^{47}$, so $G_{\mathrm{KS}} \approx 3\times10^{-7}$. The cosmic gas of $\chi$ is therefore deep in the dilute limit, where $w_\chi$ is far below the values above: it is
cold dark matter. Status: ESTIMATE.

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
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $n_f$: The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium. Unit: GeV$^3$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
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
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
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
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{J}^a{}_b$: The jump of the junction potential across the fold computed from the metric: the geometric side of the junction condition $\mathcal{J} = \kappa\mathcal{S}$, which equates it to $\kappa$ times the energy-momentum tensor $\mathcal{S}$ of everything on the fold. Unit: GeV. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{SM}}$: The energy density of the Standard-Model particles. Unit: GeV$^4$. Status: STANDARD.
- $\rho_\chi$: The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$ (FE-59). Unit: GeV$^4$. Status: DERIVED.
- $\epsilon_{\mathrm{r}}$: The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$. Unit: dimensionless. Value: below $1.344\times10^{-13}$: the four-dimensional gravitational wave has $c_{\mathrm{g}}^2 = (96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})$, and the gravitational waves and the light of the neutron-star merger GW170817 arrived together, $(c_{\mathrm{g}} - 1) < 7\times10^{-16}$. Status: DERIVED.
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
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.

<!-- end generated symbol list -->

The vacuum energy that the measurements require ($H_4^{(0)} = 67.36$ km/s/Mpc $= 1.44\times10^{-42}$ GeV). Status: STANDARD.

Can dirac16complex be the dark energy? A dark energy needs a pressure close to minus its energy density, an equation of state
$w = P/\rho$ (pressure over energy density) close to $-1$. The gas of bound states has the pressure $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$
of its self-interaction (A-8), which is positive for a repulsive self-interaction and vanishes in the dilute limit
($w_\chi = 7.2\times10^{-8}$ to $4.7\times10^{-5}$ at $G_{\mathrm{KS}} = 10^{-6}$, A-8). The gas of $\chi$ is dark matter, not dark energy. The other contribution of dirac16complex to
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

# The open questions answered

On 2026-10-25 the author asked for an analysis and an answer to the questions that UM-3 had left open: whether the indefinite
Krein norm of the charge of dirac16complex is stable; what fields that depend on the extra times do (they would be tachyonic);
whether the particles $\chi$ move faster than light unless their binding is tight ($q_{\mathrm{b}} \gg H$); the primordial era, for which
UM-3 had used the values of Planck 2018 as inputs; and the lightest neutrino mass and the Dirac phase, which UM-3 had set to zero.
Each was computed by a new program of UM-3; the answers follow.

## Is the indefinite Krein norm stable?

$$
\big\{\mathsf{a}_o, \mathsf{a}_o^\dagger\big\} = -\mathcal{Q}_o,\qquad
\mathsf{H}_\Psi = \sum_o\big(-\mathcal{Q}_o\,\omega_o\big)\,\mathsf{a}_o^\dagger\mathsf{a}_o,\qquad
\big[\mathsf{H}_\Psi, \mathsf{a}_o^\dagger\big] = \omega_o\,\mathsf{a}_o^\dagger \tag{FE-67}
$$
<!-- symbols: amode, io, dagger, Qorb, HPsi, omegafreq -->
<!-- begin generated symbol list -->
**Symbols in (FE-67).**

- $\mathsf{a}_o,\ \mathsf{a}_o^\dagger$: The annihilation and the creation operator of the mode $o$ of the quantised dirac16complex (frequency $\omega_o$, Krein charge $\mathcal{Q}_o$); the dagger is the adjoint with respect to the indefinite (Krein) scalar product. Unit: dimensionless. Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathcal{Q}_o$: The charge $Q_\Psi$ (the Krein charge) of the single-particle state $o$ of dirac16complex, a Kohn-Sham orbital or a mode: $+1$ or $-1$ for a normalised state. Unit: dimensionless. Status: DERIVED.
- $\mathsf{H}_\Psi$: The Hamiltonian (the energy operator) of the quantised dirac16complex. Unit: GeV. Status: DERIVED.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.

<!-- end generated symbol list -->

The quantised dirac16complex (with FE-43). Each mode $o$ of the field, of the frequency $\omega_o$ and the Krein charge $\mathcal{Q}_o = \pm1$,
has the anticommutator $-\mathcal{Q}_o$ (the canonical anticommutator of the field is $-\mathfrak{B}$, the sign chosen so that the particles
$\chi$, the occupied bound states of charge $-1$, have a positive norm), and every quantum raises the energy by its frequency. In the
positive-energy quantisation, in which the vacuum is annihilated by $\mathsf{a}_o$ for $\omega_o > 0$ and by $\mathsf{a}_o^\dagger$ for $\omega_o < 0$, every
particle and every hole carries a positive energy and the norm $-\mathcal{Q}_o$ of its mode. The particles and the holes of the modes of
charge $-1$ are physical; those of the modes of charge $+1$ are ghosts, states of negative norm. A fermion cannot trade its norm for its
energy, because $\{\mathsf{a}, \mathsf{a}^\dagger\} = -1$ has no representation with a positive norm: no choice of the vacuum removes the ghosts.
Status: DERIVED (`um3_krein.py`, KR1).

Four results decide the question.

1. *The vacuum is stable.* Every quantum, physical or ghost, carries a positive energy, so the vacuum cannot decay into pairs of
   quanta of opposite energy. The worry of the analysis of dark matter, that a particle $\chi$ could fall into a state of negative
   energy, does not arise in this quantisation. Status: DERIVED (KR1, KR7).
2. *The dilute gas is classically stable.* At rest the transformations that keep the bound states of the fold form a Lie algebra of
   dimension 32: 16 compact generators keep the two charges apart, 16 boosts mix them (among them the nine boosts $\Sigma^{ir}$ between
   ordinary space and the extra times). The boosts map the self-consistent gas of the Kohn-Sham states onto other self-consistent
   gases with unchanged residuals: they are flat directions, not instabilities, and the linear response of the bound level has all 32
   frequencies far below the splitting of the occupied and the empty multiplet ($1.8\times10^{-4}$ against $4.815\times10^{-3}$ in units of
   $m_\Psi$). In the dilute gas the partner of the occupied level, the level of charge $+1$, stays a real level above it. Status: DERIVED
   (KR2, KR4, KR5).
3. *The dense gas is not.* The repulsion of the self-interaction pushes the partner level onto the occupied level; where they meet
   (a collision of levels of opposite Krein charge) the two form a pair of complex frequencies $\omega \pm \mathrm{i}\Gamma_{\mathrm{K}}$, and the gas
   grows away from its state as $\mathrm{e}^{\Gamma_{\mathrm{K}}x_4}$. With the strength $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ of the
   self-interaction ($\lambda_\Psi$ the self-coupling, $n_\chi$ the number density of the particles on the fold, $V_*$ the volume of the extra
   times) this happens from $G_{\mathrm{KS}} = 0.3\,m_\Psi$ for $H = 0.05\,m_\Psi$ ($\Gamma_{\mathrm{K}} = 5.1\times10^{-6}$ rising to $6.1\times10^{-4}$ at
   $G_{\mathrm{KS}} = m_\Psi$), from $0.7\,m_\Psi$ for $H = 0.15\,m_\Psi$ and at $m_\Psi$ for $H = 0.3\,m_\Psi$ (inverse width $q_{\mathrm{b}} = 0.3\,m_\Psi$ in
   all three). The dark matter of today is dilute by many orders of magnitude, but dense gases of $\chi$ (in the early universe, or
   in compact objects) would be unstable. Status: DERIVED (KR5).
4. *The couplings of the fold decide unitarity.* At the fold, at rest, the 16 chirality-blind operators (products of
   $\gamma^{(1)}, \dots, \gamma^{(4)}$) never connect a physical state with a ghost; the 16 chiral ones (the same times $\Gamma_8$) always do. The
   author's Higgs portal acts on the left-handed half only ($P_{\mathrm{L}}$): its amplitude to create a physical $\chi$ together with a ghost
   antiparticle (an s-wave, 0.140) is 0.89 times its elastic amplitude (0.157), while a physical pair needs a p-wave. For moving
   particles the scalar, the density and the vector currents still do not mix, the magnetic dipole does, in proportion to the momentum.
   Ghosts are therefore produced wherever the chiral portals act. Status: DERIVED (KR6, KR7).

The answer. The indefinite Krein norm does not make the vacuum decay, and it does not destabilise the dilute dark matter of today; it
destabilises dense gases of $\chi$. The real problem is unitarity: with couplings at the fold that distinguish the two chiralities,
the author's left-handed Higgs portal among them, UM-3 produces ghosts and is not a unitary quantum theory. A unitary UM-3 would need
couplings of dirac16complex to the fold that do not distinguish the chiralities (OPEN).

## Fields that depend on the extra times

$$
\omega^2 = m_\Psi^2 + p_\sigma^2 + \mathrm{e}^{2H\lvert\sigma\rvert - 2a_4}\,\vec k^2 - \mathrm{e}^{2H\lvert\sigma\rvert + 2a_4}\,b_4^{-2}\,\vec\kappa^2 \tag{FE-38}
$$
<!-- symbols: omegafreq, mPsi, psigma, euler, Hconst, sigma, a4, kvec, b4, kappavec -->
<!-- begin generated symbol list -->
**Symbols in (FE-38).**

- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $p_\sigma$: The momentum along the hidden direction (local wave number of a profile along $\sigma$). Unit: GeV. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\vec\kappa$: A momentum along the extra times (three components); the fields of UM-3 have $\vec\kappa = 0$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The local dispersion relation of dirac16complex with the momentum $p_\sigma$ along the hidden direction, $\vec k$ along ordinary space and
$\vec\kappa$ along the extra times. A momentum along a time-like direction enters with the negative sign, and the same holds for every
field: on the fold a field of mass $m$ has $\omega^2 = m^2 + \vec k^2\mathrm{e}^{-2a_4} - \vec\kappa^2\mathrm{e}^{2a_4}/b_4^2$, so every mode with a
large enough momentum along the extra times has $\omega^2 < 0$, a tachyon. The metric does not depend on $x_5, x_6, x_7$, so $\vec\kappa$ is
conserved. Status: DERIVED (`um3_extratimes.py`, EX1).

$$
\omega^2 = \omega_{\mathrm{b}}^2 - c_{\mathrm{b}}^2\,\vec\kappa^2,\qquad
\sigma_{\mathrm{leak}} = \frac{1}{2H}\,\ln\frac{m_\Psi^2 - \omega^2}{\vec\kappa^2} \tag{A-9}
$$
<!-- symbols: omegafreq, omegab, cb, kappavec, sigmaleak, Hconst, mPsi -->
<!-- begin generated symbol list -->
**Symbols in (A-9).**

- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $c_{\mathrm{b}}$: The limiting speed of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold (first order in the momentum). Unit: dimensionless. Status: DERIVED.
- $\vec\kappa$: A momentum along the extra times (three components); the fields of UM-3 have $\vec\kappa = 0$. Unit: GeV. Status: DERIVED.
- $\sigma_{\mathrm{leak}}$: The distance from the fold beyond which a state of dirac16complex with a momentum along the extra times is no longer bound: there the warp has raised that momentum above the local gap. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->

The bound particles $\chi$ with a momentum along the extra times. The bound level falls with $\vec\kappa^2$ with the same coefficient with
which it rises with the momentum along ordinary space ($c_{\mathrm{b}}^2 = 1.190$ for $H = 0.05\,m_\Psi$ and $q_{\mathrm{b}} = 0.3\,m_\Psi$, where the
estimate $q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$ gives 1.2), and becomes a tachyon for $\lvert\vec\kappa\rvert > \omega_{\mathrm{b}}/c_{\mathrm{b}} = 0.874\,m_\Psi$ (the law extrapolated to large
momenta). Worse,
the warp multiplies the momentum along the extra times by $\mathrm{e}^{H\lvert\sigma\rvert}$, so beyond $\sigma_{\mathrm{leak}}$ it exceeds the local gap
and the state leaks into the bulk ($\sigma_{\mathrm{leak}} = 68$, 54 and 46 in units of $1/m_\Psi$ for $\lvert\vec\kappa\rvert = 0.01$, 0.02 and
$0.03\,m_\Psi$): with a momentum along the extra times the particles $\chi$ are neither bound nor stable. Status: DERIVED (EX2).

$$
\ln\lvert\phi_k\rvert \simeq \frac{\lvert\vec\kappa\rvert}{Hb_4}\big(\mathrm{e}^{Hx_4} - 1\big) - \frac{Hx_4}{2},\qquad
\Gamma_{\mathrm{t}} = \sqrt{l_{\mathrm{t}}^2 - k_{\mathrm{p}}^2},\qquad L_{\mathrm{t}} \ge 2\pi t_0 = 26.6\ \text{Gpc} \tag{A-10}
$$
<!-- symbols: phik, kappavec, Hconst, b4, euler, x4, Gammat, lt, kp, Lt, pi, tzero -->
<!-- begin generated symbol list -->
**Symbols in (A-10).**

- $\phi_k$: The amplitude of a Fourier mode of a massless scalar field of the fold: of comoving wave number $k$ (the label $k$) along ordinary space, and, where it is said, with a momentum $\vec\kappa$ along the extra times. Unit: GeV. Status: STANDARD.
- $\vec\kappa$: A momentum along the extra times (three components); the fields of UM-3 have $\vec\kappa = 0$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\Gamma_{\mathrm{t}}$: The growth rate of a mode of a massless field of the fold that has a momentum along the extra times, in the late universe. Unit: GeV (1/time). Status: DERIVED.
- $l_{\mathrm{t}}$: The physical momentum of a mode along the extra times. Unit: GeV. Status: STANDARD.
- $k_{\mathrm{p}}$: The physical momentum of a mode along ordinary space. Unit: GeV. Status: STANDARD.
- $L_{\mathrm{t}}$: The physical period of the extra times, if they are compact. Unit: length. Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.

<!-- end generated symbol list -->

How fast they grow. In the author's vacuum ($a_4 = Hx_4$, constant $b_4$) the physical momentum along the extra times grows as
$\mathrm{e}^{Hx_4}$, and a massless mode of the fold with $\vec k = 0$ grows double-exponentially (the first expression, from the WKB
approximation; the computed growth of $\ln\lvert\phi_k\rvert$ between $Hx_4 = 2$, 2.5 and 3, 4.5359 and 7.6487 for $\lvert\vec\kappa\rvert = Hb_4$,
agrees with the predicted 4.5434 and 7.6530). In the late universe, with $a_4$ and $b_4$ constant, a mode with the physical momenta
$l_{\mathrm{t}}$ along the extra times and $k_{\mathrm{p}}$ along ordinary space grows at the rate $\Gamma_{\mathrm{t}}$. If the extra times were compact with the
physical period $L_{\mathrm{t}}$, the slowest mode ($k_{\mathrm{p}} = 0$, $l_{\mathrm{t}} = 2\pi/L_{\mathrm{t}}$) would grow by less than one e-folding over the age
$t_0 = 13.8$ Gyr of the universe only if $L_{\mathrm{t}} \ge 2\pi t_0$ (with the speed of light 1), 26.6 Gpc; for $L_{\mathrm{t}} = 1$ mm it would
grow by $8.2\times10^{29}$ e-foldings. Status: DERIVED (EX3, EX4).

The answer. Fields that depend on the extra times are tachyonic: every field, in the bulk and on the fold, has growing modes once it
carries a momentum along the extra times, and the bound particles $\chi$ with such a momentum also leak into the bulk. UM-3 keeps only
fields without that momentum. This is a consistent truncation (the momentum is conserved, so the sector without it is invariant) but not
a stable one: interactions of fields without momentum create pairs with opposite momenta $\vec\kappa$ and $-\vec\kappa$, which are tachyonic
(EX5). Making the extra times compact and small does not help, it only raises the smallest momentum. UM-3 needs a gauge principle that
removes the momentum along the extra times of every field, as the gauge invariance of electromagnetism removes the unphysical
polarisations of the photon; UM-3 does not contain one (OPEN).

## Do the particles $\chi$ move faster than light?

$$
c_{\mathrm{b}}^2 \simeq \frac{q_{\mathrm{b}}}{q_{\mathrm{b}} - H},\qquad
v_{\mathrm{g}} = \frac{\mathrm{d}\omega}{\mathrm{d}\lvert\vec k\rvert} \le 1.0045,\qquad
\sinh\Big(\frac{H\,\Delta x_4}{2}\Big) = \frac{H\,\Delta x_1}{2} \tag{A-11}
$$
<!-- symbols: cb, qb, Hconst, vg, diff, omegafreq, kvec, Delta, x4, x1 -->
<!-- begin generated symbol list -->
**Symbols in (A-11).**

- $c_{\mathrm{b}}$: The limiting speed of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold (first order in the momentum). Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $v_{\mathrm{g}}$: The group velocity of a particle $\chi$ along ordinary space, $\mathrm{d}\omega/\mathrm{d}\lvert\vec k\rvert$, in units of the speed of light on the fold. Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

Three facts. (1) The limiting speed of the particles $\chi$ along ordinary space, at small momenta, is $c_{\mathrm{b}}$: the average of the
warp $\mathrm{e}^{2H\lvert\sigma\rvert}$ over the density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$ of the profile gives the first expression, and
the exact dispersion gives $c_{\mathrm{b}}^2 = 1.190$, 1.440 and 1.069 where the estimate gives 1.2, 1.5 and 1.071 (SL1). (2) At large momenta
the energy approaches the momentum from above; the group velocity $v_{\mathrm{g}}$ exceeds 1 only from $\lvert\vec k\rvert = 6.5\,m_\Psi$ on, by at most
0.45 per cent at $12\,m_\Psi$, and the front velocity (the limit at infinite momentum) is the speed of light (SL2). The particles $\chi$ of the
halo of the Galaxy move at $10^{-3}$ of the speed of light, and at the freeze-out of the relic density at 0.37; only relativistic
$\chi$, before the freeze-out, can outrun light, and only slightly (SL3). (3) Signals through the bulk are faster than along the fold: the
optical metric of the bulk is the hyperbolic plane of radius $1/H$, and the earliest signal between two points of the fold at the distance
$\Delta x_1$ arrives after the time $\Delta x_4$ of the third expression, less than $\Delta x_1$. The time $x_4$ is a time function of the metric,
so no closed causal curves, and no causal paradoxes, arise; but the fold alone is not causally complete (SL4). Status: DERIVED.

$$
c_{\mathrm{e}} - 1 \simeq \Big(\frac{g_{\mathrm{P}}\,\omega_{\mathrm{b}}^2}{16\pi^2}\Big)^2\big(c_{\mathrm{b}}^2 - 1\big) < 1.2\times10^{-17}\quad\Rightarrow\quad
\frac{q_{\mathrm{b}}}{H} > 4\times10^{10}\ \ \big(\omega_{\mathrm{b}} = 1.5\ \text{TeV}\big) \tag{A-12}
$$
<!-- symbols: ce, gP, omegab, pi, cb, qb, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (A-12).**

- $c_{\mathrm{e}}$: The maximal speed of the electron, in units of the speed of light. Unit: dimensionless. Value: $-6\times10^{-20} < c_{\mathrm{e}} - 1 < 1.2\times10^{-17}$ (synchrotron and inverse-Compton emission of astrophysical electrons). Status: STANDARD.
- $g_{\mathrm{P}}$: The strength of one lepton portal of the particles $\chi$ (a coupling of the currents of $\chi$ and of a chiral lepton), fixed by the relic density: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 9g_{\mathrm{P}}^2\omega_{\mathrm{b}}^2/(2\pi)$ for one $\chi$ with one antiparticle and nine chiral lepton states. Unit: GeV$^{-2}$. Value: $g_{\mathrm{P}}\omega_{\mathrm{b}}^2 = 0.110$, 0.220 and 0.734 for $\omega_{\mathrm{b}} = 1.5$, 3 and 10 TeV. Status: ESTIMATE.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $c_{\mathrm{b}}$: The limiting speed of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold (first order in the momentum). Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

What the Standard Model inherits. Through loops of the particles $\chi$ the lepton portals pass the larger limiting speed of $\chi$ to the
electron. With the portal strength that the relic density requires ($g_{\mathrm{P}}\omega_{\mathrm{b}}^2 = 0.110$, 0.220 and 0.734 for
$\omega_{\mathrm{b}} = 1.5$, 3 and 10 TeV) the loop factor is $4.9\times10^{-7}$, $1.9\times10^{-6}$ and $2.2\times10^{-5}$, and the bound on electrons
faster than light from the absence of anomalous inverse-Compton and synchrotron emission of astrophysical electrons requires
$c_{\mathrm{b}}^2 - 1 = H/(q_{\mathrm{b}} - H)$ below $2\times10^{-11}$, $6\times10^{-12}$ and $6\times10^{-13}$: $q_{\mathrm{b}}/H$ above $4\times10^{10}$,
$2\times10^{11}$ and $2\times10^{12}$. Status: ESTIMATE (SL5).

The answer. Yes, the particles $\chi$ are superluminal unless their binding is tight, but the effect is bounded: their limiting speed is
$c_{\mathrm{b}} = \sqrt{q_{\mathrm{b}}/(q_{\mathrm{b}} - H)}$ at small momenta, their group velocity never exceeds that of light by more than 0.45 per cent,
their front velocity is that of light, and no causal paradox arises. The binding must nevertheless be very tight, $q_{\mathrm{b}}/H$ above about
$4\times10^{10}$, so that the Standard Model does not inherit a measurable Lorentz violation; with the bound $q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}}$
of direct detection this places the scale of the bulk at $H \lesssim 10^{-9}$ GeV for $\omega_{\mathrm{b}}$ of a few TeV, and with the condition
of the power series, $H$ above $4\times10^{-36}$ GeV, it leaves a wide window (ESTIMATE).

## The primordial era

$$
\begin{aligned}
&\frac{\big(\sqrt{-\hat h}\,\mathcal{Z}\,\phi_k'\big)'}{\sqrt{-\hat h}\,\mathcal{Z}} + k^2\mathrm{e}^{-2a_4}\phi_k = 0,\qquad
 a_4 = Hx_4:\ \ \sqrt{-\hat h}\,\mathcal{Z} = \frac{V_{\mathrm{t}}b_4^3}{V_*},\\
&\phi_k = \sqrt{\frac{\pi}{4H}}\,\mathrm{H}^{(1)}_0\big(-k\tau_{\mathrm{c}}\big),\qquad -\tau_{\mathrm{c}} = \frac{\mathrm{e}^{-Hx_4}}{H},\qquad
 \lvert\phi_k\rvert^2 \to \frac{\pi}{4H}\Big[1 + \frac{4}{\pi^2}\Big(\ln\frac{-k\tau_{\mathrm{c}}}{2} + \gamma_{\mathrm{E}}\Big)^2\Big]
\end{aligned} \tag{A-13}
$$
<!-- symbols: hhat, Zfold, phik, prime, kwave, euler, a4, Hconst, x4, Vt, b4, Vstar, pi, Hankel, tauc, gammaE -->
<!-- begin generated symbol list -->
**Symbols in (A-13).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\phi_k$: The amplitude of a Fourier mode of a massless scalar field of the fold: of comoving wave number $k$ (the label $k$) along ordinary space, and, where it is said, with a momentum $\vec\kappa$ along the extra times. Unit: GeV. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{H}^{(1)}_0$: The Hankel function of the first kind of order zero, $\mathrm{H}^{(1)}_0 = J_0 + \mathrm{i}Y_0$ with the Bessel functions $J_0$ and $Y_0$ of order zero. Unit: dimensionless. Status: STANDARD.
- $\tau_{\mathrm{c}}$: The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{d}x_4/a$; a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$. Unit: length (= time). Status: STANDARD.
- $\gamma_{\mathrm{E}}$: The Euler-Mascheroni constant. Unit: dimensionless. Value: 0.5772157. Status: STANDARD.

<!-- end generated symbol list -->

The fields of the fold in the author's vacuum. A massless scalar field of the fold (four-dimensional normalisation) has the mode
equation of the first expression, with the volume factor $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$ of ordinary space and the factor $\mathcal{Z}$ of the size
of the extra times. In the author's vacuum ordinary space grows as $\mathrm{e}^{3Hx_4}$ while the extra times shrink as $\mathrm{e}^{-3Hx_4}$: their
product is constant, and the fields of the fold feel no Hubble friction (PR1). The mode equation is then Bessel's equation of order zero in
$-k\tau_{\mathrm{c}}$, with the conformal time $\tau_{\mathrm{c}}$, and its solution with the canonical normalisation is the Hankel function of the second
expression; at late times ($-k\tau_{\mathrm{c}} \to 0$) its square grows only logarithmically (PR2). Status: DERIVED.

$$
\begin{aligned}
&n_{\mathrm{S}} - 1 = \frac{\mathrm{d}\ln\big(k^3\lvert\phi_k\rvert^2\big)}{\mathrm{d}\ln k}:\quad 2.545\ \text{(author's vacuum)},\qquad
 -0.0351\ \text{(observed)},\\
&H_{\mathrm{inf}} < \pi M_{\mathrm{red}}\sqrt{\frac{r_{\mathrm{T}}A_{\mathrm{s}}}{2}} = 4.70\times10^{13}\ \text{GeV},\qquad
 \xi_{\mathrm{H}} = N_{\mathrm{e}}\sqrt{\frac{\lambda}{72\pi^2A_{\mathrm{s}}}} = 16233\ \text{or}\ 4502
\end{aligned} \tag{A-14}
$$
<!-- symbols: nS, diff, kwave, phik, Hinf, pi, Mred, rT, As, xiH, Ne, lamH -->
<!-- begin generated symbol list -->
**Symbols in (A-14).**

- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\phi_k$: The amplitude of a Fourier mode of a massless scalar field of the fold: of comoving wave number $k$ (the label $k$) along ordinary space, and, where it is said, with a momentum $\vec\kappa$ along the extra times. Unit: GeV. Status: STANDARD.
- $H_{\mathrm{inf}}$: The expansion rate of ordinary space during an inflationary era. Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $r_{\mathrm{T}}$: The ratio of the amplitudes of the primordial spectra of gravitational waves (tensor) and of curvature (scalar) at the pivot scale. Unit: dimensionless. Value: below 0.036 (BICEP/Keck 2021, 95 per cent). Status: STANDARD.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $\xi_{\mathrm{H}}$: The coupling $\xi$ of the Higgs doublet to the scalar curvature of the fold. Unit: dimensionless. Value: not fixed by UM-3; below $1/6$ if the gravity of the fold is induced by its fields. Status: ASSUMED.
- $N_{\mathrm{e}}$: The number of e-foldings of inflation after the pivot scale left the horizon. Unit: dimensionless. Value: 55. Status: STANDARD.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\frac{1}{16\pi G_{\mathrm{ind}}} = \frac{N_{\mathrm{ind}}\,\Lambda_{\mathrm{c}}^2}{192\pi^2},\qquad
N_{\mathrm{ind}} = \sum_{\text{real scalars}}\big(1 - 6\xi\big) + N_{\mathrm{Weyl}} - 4N_{\mathrm{gauge}} = 4\big(1 - 6\xi_{\mathrm{H}}\big) \tag{FE-64}
$$
<!-- symbols: pi, Gind, Nind, Lambdac, xinm, NWeyl, Ngauge, xiH -->
<!-- begin generated symbol list -->
**Symbols in (FE-64).**

- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{ind}}$: The Newton constant of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$ (Newton’s constant $G_{\mathrm{N}}$ up to the factor $1 + 5\epsilon_{\mathrm{r}}/6$). Unit: GeV$^{-2}$. Status: ASSUMED.
- $N_{\mathrm{ind}}$: The weighted number of the fields of the fold that induce the Einstein-Hilbert term: each real scalar counts $1 - 6\xi$, each Weyl fermion 1, each gauge field $-4$ (with its ghost fields). Unit: dimensionless. Value: $4(1 - 6\xi_{\mathrm{H}})$ for the Standard Model with three right-handed neutrinos. Status: DERIVED.
- $\Lambda_{\mathrm{c}}$: The cutoff of the proper-time integral of the one-loop effective action of the fields of the fold: the highest energy of the quantum fluctuations that induce gravity. Unit: GeV. Value: $\sqrt{24}\,\pi M_{\mathrm{red}} = 3.748\times10^{19}$ GeV for the measured Newton constant at $\xi_{\mathrm{H}} = 0$. Status: ESTIMATE.
- $\xi$: The coupling of a real scalar field to the scalar curvature $\hat R$ of the fold: the term $-\frac12\xi\hat R$ times the square of the field in its Lagrangian ($\xi = 1/6$ is the conformal coupling). Unit: dimensionless. Status: STANDARD.
- $N_{\mathrm{Weyl}}$: The number of Weyl (two-component) fermion fields of the fold. Unit: dimensionless. Value: 48 (three generations of quarks and leptons with three right-handed neutrinos). Status: STANDARD.
- $N_{\mathrm{gauge}}$: The number of gauge fields of the fold. Unit: dimensionless. Value: 12 (eight gluons, three $W$, one $B$). Status: STANDARD.
- $\xi_{\mathrm{H}}$: The coupling $\xi$ of the Higgs doublet to the scalar curvature of the fold. Unit: dimensionless. Value: not fixed by UM-3; below $1/6$ if the gravity of the fold is induced by its fields. Status: ASSUMED.

<!-- end generated symbol list -->

What the author's vacuum produces, and what the observations need. The spectrum of the fluctuations, $k^3\lvert\phi_k\rvert^2/(2\pi^2)$,
grows like $k^3$ times a logarithm: its index, the first line of A-14, is $n_{\mathrm{S}} - 1 = 2.545$ at the computed scales, against the
observed $-0.0351$ (Planck 2018). The
author's vacuum cannot be the era in which the observed fluctuations were made (PR2). It also changes the couplings of the fold: the
action of a gauge field carries $\mathcal{Z}/g^2$, so every squared coupling $g^2$ grows as $\mathrm{e}^{3Hx_4}$ (PR3). The observed nearly flat
spectrum needs an era with frozen extra times and nearly exponential expansion of ordinary space; the bound on primordial gravitational
waves, $r_{\mathrm{T}} < 0.036$ (BICEP/Keck 2021), with the measured amplitude $A_{\mathrm{s}} = 2.1\times10^{-9}$, limits its expansion rate $H_{\mathrm{inf}}$
by the second line of A-14 (PR4). UM-3 contains no field that could drive such an era. The Higgs field could, with a large coupling
$\xi_{\mathrm{H}}$ to the curvature (the second line of A-14, for $N_{\mathrm{e}} = 55$ e-foldings and the quartic coupling $\lambda = 0.13$ or 0.01 at
the scale of inflation), but if the gravity of the fold is induced by its own fields (FE-64), its sign needs $\xi_{\mathrm{H}} < 1/6$: the two
exclude each other (PR5). Status: DERIVED (PR2 to PR5), STANDARD (the measurements).

The answer. The Planck values that UM-3 used as inputs cannot be derived from the author's vacuum, which gives a spectrum rising as
$k^{2.5}$ and couplings that grow. An inflationary era with frozen extra times, below $4.7\times10^{13}$ GeV, is needed; UM-3 has no inflaton
for it, and its Higgs field cannot serve if the gravity of the fold is induced. How the universe passes from the author's vacuum to such an
era and then to the static block, and what creates the stabiliser of the bulk on the way, is OPEN. The Planck values remain inputs.

## The lightest neutrino mass and the Dirac phase

$$
\begin{aligned}
&\big(\lvert U_{\mathrm{e}i}\rvert^2\big)_{i = 1, 2, 3} = \big(\cos^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{13}\big),\\
&m_2 = \sqrt{m_1^2 + \Delta m^2_{21}},\qquad m_3 = \sqrt{m_1^2 + \Delta m^2_{31}},\qquad
 \sum_i m_i < 0.064\ \text{eV}\ \Rightarrow\ m_1 < 4.12\ \text{meV},\qquad
 m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2
\end{aligned} \tag{A-15}
$$
<!-- symbols: Uei, ii, thetaij, mferm, Delta, mmass, meff -->
<!-- begin generated symbol list -->
**Symbols in (A-15).**

- $U_{\mathrm{e}i}$: The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$. Unit: dimensionless. Value: $\lvert U_{\mathrm{e}i}\rvert^2 = 0.681, 0.296, 0.022$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\theta_{12},\ \theta_{13},\ \theta_{23}$: The three mixing angles of $U_{\mathrm{PMNS}}$ (its fourth parameter is the Dirac phase, which does not enter the electron-flavour results of UM-3). Unit: dimensionless. Value: $33.40^\circ$, $8.54^\circ$, $49.14^\circ$ in the computations of UM-3 ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$: NuFIT 5.2, November 2022, normal ordering, with the Super-Kamiokande atmospheric data); $33.71^\circ$, $8.56^\circ$, $43.28^\circ$ in NuFIT 6.0 (2024; $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$). Status: STANDARD.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-3 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 4.12 meV by DESI DR2 with the CMB. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; in $\Delta m^2$ the squared-mass difference of two neutrino mass states ($m_2^2 - m_1^2$ for the two states of a resonance, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1). Unit: GeV. Status: STANDARD.
- $m_{\mathrm{eff}}$: The effective mass of the electron neutrino measured in the beta decay of tritium, $m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2$. Unit: eV. Value: below 0.45 eV (KATRIN 2025, 90 per cent). Status: STANDARD.

<!-- end generated symbol list -->

The Dirac phase $\delta_{\mathrm{CP}}$. The mixing matrix is three rotations by the angles $\theta_{23}$, $\theta_{13}$ and $\theta_{12}$, the phase attached
to the middle one, and its electron row (the first line of A-15) contains no phase. Every flavour result of UM-3 is a result for electron
neutrinos: the solar survival probabilities, the conversion in the envelope of a supernova (the matter potential acts on $\nu_e$ only, so the
phase can be moved into $\nu_\mu$ and $\nu_\tau$), and the capture of the cosmic neutrinos. Computed with the newer global fit NuFIT 6.0
($\delta_{\mathrm{CP}} = 212^\circ$ in the normal ordering), the envelope gives the same survival probability as with $\delta_{\mathrm{CP}} = 0$ to
$6\times10^{-14}$. The phase appears only in the appearance channels ($\nu_\mu \to \nu_e$: 0.0421 for $\delta_{\mathrm{CP}} = 0$ and 0.0346 for
$212^\circ$ at 295 km and 0.6 GeV) and in the Jarlskog invariant of CP violation, $-0.0178$. Status: DERIVED (`um3_numass.py`, NM3).

The lightest mass $m_1$. The bound of DESI DR2 with the CMB on the sum of the masses, 0.064 eV, excludes the inverted ordering (whose
smallest sum is 0.0989 eV) and bounds $m_1$ below 4.12 meV in the normal ordering (the second line of A-15, with NuFIT 6.0:
$\Delta m^2_{21} = 7.49\times10^{-5}$ eV$^2$, $\Delta m^2_{31} = 2.513\times10^{-3}$ eV$^2$); the effective mass of tritium beta decay is then
8.84 to 9.76 meV, far below the limit 0.45 eV of KATRIN. Within this range $m_1$ changes one result of UM-3, the capture rate of the cosmic
neutrinos on 100 g of tritium, $N_{\mathrm{T}}\bar\sigma_{\mathrm{T}}(n_\nu^{(0)}/2)\sum_i\lvert U_{\mathrm{e}i}\rvert^2(1 + \mathsf{s}_i)$ ($N_{\mathrm{T}}$ the number of tritium
nuclei, $\bar\sigma_{\mathrm{T}} = 3.834\times10^{-45}$ cm$^2$ the averaged capture cross-section, $n_\nu^{(0)}/2 = 56$ cm$^{-3}$ the density per mass
state of one helicity, $\mathsf{s}_i$ the mean speed of the state today): from 6.88 per year at $m_1 = 0$ to 4.47 per year at $m_1 = 4.12$ meV, as
$\nu_1$ becomes slow (mean speed 0.126). Status: DERIVED (NM1, NM2, NM4), STANDARD (the bounds).

The answer. Setting the Dirac phase to zero was without consequence: it drops out of every result of UM-3. The lightest mass is not fixed
by any measurement; DESI DR2 bounds it below 4.12 meV, and within this range it lowers the capture rate of the cosmic neutrinos by up to 35
per cent. The records computed with NuFIT 5.2 differ from NuFIT 6.0 by at most 1.5 per cent (NM5).

# What the author may have left out

The author asked to be told if something important was missing from his specification. UM-3 had to add the following, and the
analysis found the following problems.

| item | why it is needed or what it means | where it stands |
| ------ | ------ | ------ |
| right-handed quark singlets and the Yukawa couplings | the quark doublets alone have no masses and the hypercharges cancel the gauge anomalies only with the singlets | added (a default of UM-3, proposed in the notification of 17:20, which the author did not answer: ASSUMED) |
| three right-handed neutrinos | Dirac neutrino masses and the mixing that flavour conversion needs; the anomalies still cancel | added (accepted by the author, 17:32); they must never thermalise |
| the place of the Standard Model | in the bulk, every species would move with its own limiting speed and three neutrino profiles would oscillate wrongly; on the fold all share one light cone | the Standard Model lives on the fold (ASSUMED, motivated by the DERIVED limiting speeds) |
| a thin source at the fold | the kink of the warp $\mathrm{e}^{-H\lvert\sigma\rvert}$ requires one (the fold fluid); at the static block it is a tension with $1/62$ of pressureless matter, which the energy flowing out of the bulk keeps from diluting; its energy above the static value is the dark energy | ASSUMED (its values DERIVED) |
| an Einstein-Hilbert term of the fold | bulk gravitons move 2.74 times faster than light at the static block and have no time-kinetic term at the author's vacuum (the history $a_4 = Hx_4$ with constant $b_4$, which needs no sources in the bulk); the Gauss-Bonnet and cubic terms give the fold a graviton term of its own, but its gravitational waves still move with $c_{\mathrm{g}}^2 = 83/82$; gravitational waves move with the speed of light to $7\times10^{-16}$ (GW170817) | ASSUMED (induced gravity); DERIVED: it must provide all but $1.3\times10^{-13}$ of the gravity of the fold; ESTIMATE: its own fields induce it with a cutoff at the Planck scale if $\xi_{\mathrm{H}} < 1/6$ |
| a medium of the bulk (the stabiliser) | without a bulk source no instant has both rates of the metric below $0.477H$; the static late-time bulk needs exactly the stabiliser, $\kappa\rho_{\mathrm{s}} = -H^2/16$ with the pressure $5\rho_{\mathrm{s}}$, found by Claude (Anthropic) on 2026-10-24; it violates the null energy condition and only a ghost field reproduces it; when the universe expands, the bulk source gives energy to the fold | DERIVED (that a source is needed, and its value); ASSUMED (a separate medium, no field theory given); OPEN (its origin after the primordial era) |
| the response of that medium | to first order in the bulk response, the component of the junction condition along the extra times (the radion condition) cannot be met by a rigid medium without changing the expansion law of the fold (dust would expand as $x_4^{5/6}$); a responding medium meets it with the radion mode, a combination of first-order jumps of the metric at the fold in the ratio $1 : -1 : 5$ that changes only that component | ASSUMED (the radion mode) |
| frozen extra times in the late universe (the size $\mathrm{e}^{-a_4}b_4$ of the extra times constant) | otherwise the couplings of the Standard Model change: in the author's vacuum ($a_4 = Hx_4$, $b_4$ constant) the gauge and Yukawa couplings grow as $\mathrm{e}^{3Hx_4/2}$, the quartic Higgs coupling and Newton's constant as $\mathrm{e}^{3Hx_4}$ | required |
| a gauge field for the ad hoc Higgs vacuum | the literal ad hoc vacuum carries an isospin charge that the Gauss law forbids; with the pure-gauge $W^2_{x_4}$ it is a rotated vacuum with one radial residual, and it must decay before nucleosynthesis | DERIVED |
| the Krein norm of dirac16complex | the signature $(4,4)$ of the author's matrices makes the charge indefinite; quantised, it has ghosts that no vacuum removes; the vacuum and the dilute gas are stable, the dense gas is not; chiral couplings at the fold produce ghosts | DERIVED; OPEN: a unitary coupling (chirality-blind at the fold) |
| the extra times | fields that depend on them are tachyonic; the restriction to fields without a momentum along them is consistent but unstable; compact extra times would have to exceed 26.6 Gpc | ASSUMED (no dependence); OPEN: a gauge principle that removes that momentum |
| Lorentz violation in the bulk | the particles $\chi$ move faster than light on the fold unless $q_{\mathrm{b}} \gg H$ (group velocity at most 1.0045, front velocity that of light), and signals through the bulk outrun light on the fold; loops pass the violation to the electron | a condition on the parameters: $q_{\mathrm{b}}/H > 4\times10^{10}$ (ESTIMATE) |
| direct detection | the Higgs portal fixed by the binding and the quark portals are strongly constrained | a weakly bound, leptophilic $\chi$ above about 1.5 TeV |
| the dark energy | a vacuum energy with $w = -1$; DESI DR2 prefers an evolving one | OPEN (tension at 2.3 to 3.1 standard deviations) |
| the primordial era | the author's vacuum gives the fields of the fold a spectrum with $n_{\mathrm{S}} - 1 = 2.5$ and growing couplings; the observed spectrum needs an inflationary era with frozen extra times below $4.7\times10^{13}$ GeV, and the Higgs field cannot drive it if the gravity of the fold is induced | DERIVED; OPEN (no inflaton; Planck inputs) |
| the lightest neutrino mass and the Dirac phase | not fixed by the specification; the phase drops out of every result of UM-3; DESI DR2 bounds $m_1 < 4.12$ meV, which changes only the capture rate of the cosmic neutrinos | DERIVED (the phase is irrelevant); ASSUMED: $m_1 = 0$ within the bound |
