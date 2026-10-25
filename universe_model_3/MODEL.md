---
title: "UM-3 model"
subtitle: 'The universe model UM-3: the author''s spacetime of eight dimensions, the fields and where they live, the complete action, and every parameter'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Formulated and verified by Claude (Anthropic)"
  - "Model of UM-3, 2026-10-24"
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

This document defines the universe model UM-3, the revision of 2026-10-24 ordered by the author: the spacetime and its metric,
the fields and where they live, the complete action from which every field equation follows, and every parameter with its
value and its origin. It is self-contained: every equation is written out (the terms of the action carry the tags IN-1 to
IN-16 and the metric the tag FE-27, the same tags as in every UM-3 document), and every symbol of every display equation is
defined right after it.

## The status labels

Every equation and every parameter carries one of the labels **AUTHOR** (from the author: his notebooks `4+4.nb` and
`Dirac_Einstein-Lovelock_4+4_Nash.nb` and his order of 2026-10-24), **RECORD** (from the record of this repository: the
Lagrangian of dirac16complex with its canonical spin connection and its contact self-interaction, the Kohn-Sham treatment),
**STANDARD** (textbook physics or a published measurement), **ASSUMED** (a choice of UM-3 without derivation), **INVENTED** (a new
interaction of UM-3: the portals of dirac16complex), **DERIVED** (computed and verified in UM-3), **ESTIMATE** (an order of
magnitude) and **OPEN** (not settled).

## Coordinates, signature and units

The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ is the hidden
space-like coordinate, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, and $x_5, x_6, x_7$ three extra time-like coordinates. The
signature is $(+,+,+,+,-,-,-,-)$ in this order. Units are natural, $\hbar = c = 1$. A prime on a function of the time $x_4$ alone
is its derivative with respect to $x_4$.

# The spacetime

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

The author's metric, with his two functions of the time $a_4(x_4)$ and $b_4(x_4)$ ($b_4$ is never identically 1, by the author's
order) and his constant $H$. The metric depends on $x_0$ only through $z = 6Hx_0$; one period $0 < z < \pi$ of $x_0$ is, in the proper
coordinate $\sigma$ of the hidden direction, the whole line $-\infty < \sigma < \infty$ (DERIVED). In that coordinate ordinary
space and the extra times are warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$, which has a kink at $\sigma = 0$ ($z = \pi/2$): this
seven-dimensional surface is the fold. The rest of spacetime is the bulk. Status: AUTHOR (the metric), DERIVED (the chart).

# The fields and where they live

| field | symbol | what it is | lives in | couples to |
| ---------------------- | ---------------- | ------------------------------------ | ---------- | ------------------------------ |
| Einstein-Lovelock gravity | $g_{MN}$ | the metric of eight dimensions, with the author's Lovelock weights | bulk and fold | every field |
| dirac16complex | $\Psi$ | the author's 16-component complex spinor field, with left- and right-handed halves $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | the bulk | gravity (canonical spin connection), itself, every Standard-Model field at the fold; only $\Psi_{\mathrm{L}}$ to the Higgs doublet |
| Higgs doublet | $\Phi$ | the scalar doublet with $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$, $\lambda > 0$, $\mu^2 < 0$, expanded about the ad hoc vacuum $(\mathcal{A}, v + h)/\sqrt2$ | the fold | gravity, $W$, $B$, the fermions, $\Psi_{\mathrm{L}}$ |
| lepton doublets | $\ell_i$ | $(\nu_{\mathrm{L}i}, e_{\mathrm{L}i})$, three generations | the fold | gravity, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| right-handed charged leptons | $e_{\mathrm{R}i}$ | electron, muon, tau | the fold | gravity, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| right-handed neutrinos | $\nu_{\mathrm{R}i}$ | three gauge singlets: Dirac neutrino masses (accepted by the author, 2026-10-24 17:32) | the fold | gravity, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| electroweak gauge fields | $W^1$, $W^2$, $W^3$, $B$ | the gauge fields of $SU(2)_{\mathrm{L}}$ and $U(1)_Y$ | the fold | gravity, $\Phi$, the fermions, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| quarks | $Q_i$, $u_{\mathrm{R}i}$, $d_{\mathrm{R}i}$ | three generations of doublets and singlets | the fold | gravity, gluons, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| gluons | $G^A$ | the gauge field of $SU(3)_{\mathrm{C}}$ | the fold | gravity, quarks, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| stabiliser | $\mathcal{T}_{\mathrm{stab}}$ | the medium without which the late-time bulk cannot stay static (found and named by Claude, Anthropic, on 2026-10-24) | the bulk | gravity; when the universe expands it exchanges energy with the fold |
| fold fluid | $\mathcal{T}_{\mathrm{ff}}$ | the part of the thin source of the fold not supplied by the other fields; at the static block a tension with $1/62$ of pressureless matter | the fold | gravity; it takes up the energy that flows out of the bulk |
| induced gravity | $\kappa_4$ | an Einstein-Hilbert term of the fold, which must provide all but $1.3\times10^{-13}$ of four-dimensional gravity | the fold | gravity |

The Standard Model lives on the fold, because in the bulk every species would move with its own limiting speed (the warp averaged
over its profile) and three neutrino flavours with three profiles would oscillate with phases that measurements exclude; on the
fold every field has the one light cone of the fold (the limiting speeds are DERIVED; the place is ASSUMED on that basis).
dirac16complex, the author's field of eight dimensions, lives in the bulk and couples to the Standard Model at the fold. No field
depends on the extra times $x_5, x_6, x_7$: a field with a momentum along them is tachyonic (its frequency squared falls with that
momentum, because the extra times are time-like), and the bound particles of dirac16complex with such a momentum leak into the bulk; the
restriction is consistent but unstable, and UM-3 needs a gauge principle that removes the momentum along the extra times of every field.
Status: AUTHOR (the list of fields), ASSUMED (the additions, the places and the restriction), DERIVED (the tachyons), OPEN (the gauge
principle).

# The action

All field equations of UM-3 follow from one action by varying it with respect to every field.

## The sum of all terms

$$
\begin{aligned}
S_{\mathrm{tot}} &= S_{\mathrm{EL}} + S_{\mathrm{stab}} + S_\Psi + S_{\mathrm{fold}},\\
S_{\mathrm{fold}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\delta_{\mathrm{D}}(\sigma)\,\frac{1}{V_*}\,
\big(\mathcal{L}_{\mathrm{IG}} + \mathcal{L}_{\mathrm{ff}} + \mathcal{L}_{\mathrm{H}} + \mathcal{L}_{\mathrm{gauge}}
+ \mathcal{L}_{\mathrm{f}} + \mathcal{L}_{\mathrm{Y}} + \mathcal{L}_{\mathrm{P}}\big)
\end{aligned} \tag{IN-1}
$$
<!-- symbols: Stot, SEL, Sstab, SPsi, Sfold, diff, Xcoord, metric, deltaD, sigma, Vstar, LIG, Lff, LH, Lgauge, Lf, LY, LP -->
<!-- begin generated symbol list -->
**Symbols in (IN-1).**

- $S_{\mathrm{tot}}$: The action of UM-3 (the integral of the Lagrangian density over spacetime); its variation with respect to every field gives the field equations. Unit: dimensionless ($\hbar = 1$). Status: ASSUMED.
- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity in eight dimensions. Unit: dimensionless. Status: AUTHOR.
- $S_{\mathrm{stab}}$: The action of the stabiliser of the bulk (a medium specified by its energy-momentum tensor $\mathcal{T}_{\mathrm{stab}}$). Unit: dimensionless. Status: ASSUMED.
- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.
- $S_{\mathrm{fold}}$: The action of the fold: the Standard Model, the portals of dirac16complex, the fold fluid and the induced gravity of the fold, all at $\sigma = 0$. Unit: dimensionless. Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{L}_{\mathrm{IG}}$: The Lagrangian of the induced gravity of the fold. Unit: GeV$^4$. Status: ASSUMED.
- $\mathcal{L}_{\mathrm{ff}}$: The Lagrangian of the fold fluid (only its energy-momentum tensor $\mathcal{T}_{\mathrm{ff}}$ enters the equations). Unit: GeV$^4$. Status: ASSUMED.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->

The action has four parts: Einstein-Lovelock gravity in eight dimensions, the stabiliser of the bulk, dirac16complex in the bulk,
and the fold, whose terms are confined to $\sigma = 0$ by the Dirac delta of the proper hidden coordinate. Status: ASSUMED.

## Gravity

$$
\begin{aligned}
S_{\mathrm{EL}} &= \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)}
 - 2\Lambda\Big),\qquad \kappa = 8\pi G_8,\\
\alpha_{(p)} &= w_{(p)}\,H^{2-2p},\qquad w_{(1)} = 1,\quad w_{(2)} = \frac{1}{32},\quad w_{(3)} = \frac{1}{1152},
 \qquad \Lambda = -10H^2
\end{aligned} \tag{IN-2}
$$
<!-- symbols: SEL, kappa, diff, Xcoord, metric, ip, alphaL, LovL, Lambda, pi, G8, wL, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-2).**

- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity in eight dimensions. Unit: dimensionless. Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$ (the author writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-10H^2$. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $w_{(p)}$: The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]). Unit: dimensionless. Value: $(1, 1/32, 1/1152)$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

$$
\begin{aligned}
\mathcal{L}_{(p)} &= \frac{1}{2^{p}}\,\delta^{M_1N_1\cdots M_pN_p}_{P_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p},\\
\mathcal{L}_{(1)} &= R,\qquad \mathcal{L}_{(2)} = R^2 - 4R_{MN}R^{MN} + R_{MNPQ}R^{MNPQ}
\end{aligned} \tag{IN-3}
$$
<!-- symbols: LovL, ip, delta, iM, iN, iP, iQ, Riemann -->
<!-- begin generated symbol list -->
**Symbols in (IN-3).**

- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor (convention $[\nabla_P, \nabla_Q]V^M = R^M{}_{NPQ}V^N$), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.

<!-- end generated symbol list -->

Einstein-Lovelock gravity with the author's weights and cosmological constant (his notebook, In[134]): the Einstein-Hilbert, the
Gauss-Bonnet and the cubic Lovelock densities, built from the Riemann tensor with the generalised Kronecker delta. Their variation
contains no derivative of the metric higher than the second, so the field equations are of second order and a thin source at the
fold produces a finite jump of first derivatives. Status: AUTHOR, STANDARD.

## dirac16complex

$$
S_\Psi = \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\frac12\big(\bar\Psi\gamma^MD_M\Psi - (D_M\bar\Psi)\gamma^M\Psi\big)
 - m_\Psi\,\bar\Psi\Psi - \frac{\lambda_\Psi}{2}\big(\bar\Psi\Psi\big)^2\Big] \tag{IN-4}
$$
<!-- symbols: SPsi, diff, Xcoord, metric, Psi, gammaM, iM, Dcov, mPsi, lamPsi -->
<!-- begin generated symbol list -->
**Symbols in (IN-4).**

- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.

<!-- end generated symbol list -->

$$
\begin{aligned}
&\{T_a, T_b\} = 2\eta_{ab}\mathbf{1},\qquad \eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1),\qquad T^a = \eta^{ab}T_b,
 \qquad \gamma^M = \mathbf{e}_a{}^M\,T^a,\\
&\bar\Psi = \Psi^\dagger\sigma_{16},\qquad \sigma_{16} = T_0T_1T_2T_3,\qquad \Gamma_8 = T_0T_1T_2T_3T_4T_5T_6T_7,\\
&P_{\mathrm{L}} = \frac{\mathbf{1} - \Gamma_8}{2},\qquad P_{\mathrm{R}} = \frac{\mathbf{1} + \Gamma_8}{2},\qquad
 \Psi_{\mathrm{L}} = P_{\mathrm{L}}\Psi,\qquad \Psi_{\mathrm{R}} = P_{\mathrm{R}}\Psi
\end{aligned} \tag{IN-5}
$$
<!-- symbols: Tmat, ia, ib, eta, identity, diag, gammaM, iM, vielbein, Psi, dagger, sigma16, Gamma8, PL, PR, PsiL, PsiR -->
<!-- begin generated symbol list -->
**Symbols in (IN-5).**

- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\Psi_{\mathrm{L}}$: The left-handed half of dirac16complex, $\Psi_{\mathrm{L}} = P_{\mathrm{L}}\Psi$ (the upper eight components in the basis of 4+4.nb). Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\Psi_{\mathrm{R}}$: The right-handed half of dirac16complex, $\Psi_{\mathrm{R}} = P_{\mathrm{R}}\Psi$ (the lower eight components). Unit: GeV$^{7/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\begin{aligned}
&D_M\Psi = \partial_M\Psi + \Omega_M\Psi,\qquad D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\,\Omega_M,\qquad
 \Omega_M = \frac12\,\varpi_{Mab}\,\Sigma^{ab},\qquad \Sigma^{ab} = \frac14\big[T^a, T^b\big],\\
&\varpi_{Mab} = \mathbf{e}_a{}^N\big(\partial_M\mathbf{e}_{bN} - \Gamma^P{}_{MN}\,\mathbf{e}_{bP}\big)
\end{aligned} \tag{IN-6}
$$
<!-- symbols: Dcov, iM, partial, Psi, Omega, omegaSC, ia, ib, SigmaGen, Tmat, vielbein, iN, Christoffel, iP -->
<!-- begin generated symbol list -->
**Symbols in (IN-6).**

- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $\varpi_{Mab}$: The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$. Unit: 1/length. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\Sigma^{ab},\ \Sigma^{\mu\nu}$: The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold. Unit: dimensionless. Status: AUTHOR.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Gamma^P{}_{MN}$: The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection). Unit: 1/length. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.

<!-- end generated symbol list -->

dirac16complex with the kinetic term in the symmetric form (real for the author's real matrices), the mass $m_\Psi$ and the contact
self-interaction $\lambda_\Psi$ (RECORD); the author's eight real $16 \times 16$ Dirac matrices, the Dirac adjoint and the chiral
projectors (AUTHOR); the canonical spin connection, which couples dirac16complex to gravity and is never identically zero for the
author's metric ($\gamma^M\Omega_M = -3H\,\mathrm{sgn}(\sigma)\gamma^{(0)} + \frac32(b_4'/b_4)\gamma^{(4)}$, DERIVED; here $\gamma^{(0)} = T^0$
and $\gamma^{(4)} = T^4$ are the author's matrices along the hidden direction and along the time, $\sigma$ the proper coordinate of
the hidden direction with the fold at $\sigma = 0$, and $\mathrm{sgn}$ the sign function).

## The stabiliser of the bulk

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

The medium of the bulk that the late universe needs, found and named by Claude (Anthropic) on 2026-10-24 while deriving the field
equations of UM-3: with the author's weights the bulk of a slowly expanding universe is not a vacuum solution (without a bulk source no
instant has both the expansion rate of ordinary space and the rate of change of $b_4$ below $0.477H$), and its static state requires
this energy-momentum tensor, with a negative energy density $\rho_{\mathrm{s}} = -H^2/(16\kappa)$ and the pressure $p_{\mathrm{s}} = 5\rho_{\mathrm{s}}$ in every
direction but the time. It violates the weak and the null energy condition, and only a field with negative kinetic energy (a ghost)
reproduces it. On the static bulk it is conserved by itself; when ordinary space grows (with frozen extra times) the bulk source gives
off energy that flows into the fold and is taken up there, so it then exchanges energy with the fold. It is absent in the primordial
era, whose bulk is the author's vacuum, and as a medium of its own it could not appear later (its density times $b_4^{18}$ would stay
constant); its value is the energy density of the bulk at which ordinary space stands still. Status: DERIVED (its value, and that the
late bulk needs a source), ASSUMED (a separate medium), OPEN (its origin).

## The fold

$$
\begin{aligned}
&\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\delta_{\mathrm{D}}(\sigma)\,\frac{1}{V_*}\,\mathbb{F}
 = \int\mathrm{d}^4x\,\sqrt{-\hat h}\;\mathcal{Z}\,\mathbb{F}\big\vert_{\sigma=0},\qquad \mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4,\\
&\hat h_{\mu\nu} = \mathrm{diag}\big(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1\big),\qquad
 \sqrt{-\hat h} = \mathrm{e}^{3a_4},\qquad
 \mathcal{Z} = \frac{V_{\mathrm{t}}\big(\mathrm{e}^{-a_4}b_4\big)^3}{V_*},\qquad V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7
\end{aligned} \tag{IN-8}
$$
<!-- symbols: diff, Xcoord, metric, deltaD, sigma, Vstar, Ffold, xfour, x1, x2, x3, x4, hhat, imu, inu, diag, euler, a4, Zfold, Vt, b4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (IN-8).**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathbb{F}$: Any function of the fields at the fold (used to state a rule of integration). Status: STANDARD.
- $x$: The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\mathcal{L}_{\mathrm{IG}} = \frac{\hat R}{2\kappa_4} \tag{IN-9}
$$
<!-- symbols: LIG, Rhat, kappa4 -->
<!-- begin generated symbol list -->
**Symbols in (IN-9).**

- $\mathcal{L}_{\mathrm{IG}}$: The Lagrangian of the induced gravity of the fold. Unit: GeV$^4$. Status: ASSUMED.
- $\hat R$: The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold. Unit: 1/length$^2$. Status: STANDARD.
- $\kappa_4$: The coupling of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_4/(1 + 5\epsilon_{\mathrm{r}}/6)$ (the Friedmann equation of the fold to first order in $\epsilon_{\mathrm{r}}$). Unit: GeV$^{-2}$. Value: $\kappa_4 \simeq 8\pi G_{\mathrm{N}} = 8\pi/M_{\mathrm{Pl}}^2$. Status: ASSUMED.

<!-- end generated symbol list -->

$$
\mathcal{T}_{\mathrm{ff}}{}^a{}_b = \mathrm{diag}\big(p_{\mathrm{ff}}, p_{\mathrm{ff}}, p_{\mathrm{ff}}, -\rho_{\mathrm{ff}},
 q_{\mathrm{ff}}, q_{\mathrm{ff}}, q_{\mathrm{ff}}\big) \tag{IN-10}
$$
<!-- symbols: Tff, ia, ib, diag, pff, rhoff, qff -->
<!-- begin generated symbol list -->
**Symbols in (IN-10).**

- $\mathcal{T}_{\mathrm{ff}}{}^a{}_b$: The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation). Unit: GeV$^4$. Status: ASSUMED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $p_{\mathrm{ff}}$: The pressure of the fold fluid along ordinary space. Unit: GeV$^4$. Value: $-61HV_*/(8\kappa)$ at the static block. Status: ASSUMED.
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $31HV_*/(4\kappa)$ at the static block. Status: ASSUMED.
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times. Unit: GeV$^4$. Value: $-61HV_*/(8\kappa)$ at the static block. Status: ASSUMED.

<!-- end generated symbol list -->

The fold: the reduction of the terms of the fold to four-dimensional fields with the volume $V_*$ of the extra times and the factor
$\mathcal{Z}$ (IN-8); the induced gravity of the fold, which makes four-dimensional gravity general relativity (IN-9), because the
gravitons of the bulk move 2.74 times faster than light at the static block (the late-time state of the bulk, in which $a_4$ and
$b_4$ are constant) and have no time-kinetic term at the author's vacuum (the history $a_4 = Hx_4$ with constant $b_4$, which needs
no sources in the bulk), and because with the graviton term that the Gauss-Bonnet and cubic Lovelock terms give the kink of the fold
the four-dimensional gravitational waves still move with the squared speed $83/82$; the speed of light of the gravitational waves of
GW170817 requires the induced term to provide all but $1.3\times10^{-13}$ of the gravity of the fold, and the fields of the fold induce
such a term with a cutoff at the Planck scale if the Higgs doublet couples to the curvature with $\xi_{\mathrm{H}} < 1/6$; the fold fluid, the
thin source that the kink of the warp requires (IN-10), at the static block a tension with $1/62$ of pressureless matter, which the energy
flowing out of the bulk keeps from diluting. Status: ASSUMED, DERIVED (the reduction, the speeds, the bound and the fold fluid),
ESTIMATE (the induced term).

## The Higgs doublet with the ad hoc vacuum

$$
\mathcal{L}_{\mathrm{H}} = -\hat h^{\mu\nu}\big(D_\mu\Phi\big)^\dagger D_\nu\Phi - V(\Phi),\qquad
V(\Phi) = \mu^2\,\Phi^\dagger\Phi + \lambda\big(\Phi^\dagger\Phi\big)^2,\qquad \lambda > 0,\quad \mu^2 < 0 \tag{IN-11}
$$
<!-- symbols: LH, hhat, imu, inu, Dcov, Phi, dagger, Vpot, muH, lamH -->
<!-- begin generated symbol list -->
**Symbols in (IN-11).**

- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $V(\Phi)$: The Higgs potential, $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$. Unit: GeV$^4$. Status: AUTHOR.
- $\mu^2$: The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$). Unit: GeV$^2$. Value: $\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\Phi = \frac{1}{\sqrt2}\begin{pmatrix}\mathcal{A}(x_4)\\ v + h\end{pmatrix},\qquad
\mathcal{A}(x_4) = v_{\mathcal{A}}\,\mathrm{e}^{-2a_{40}x_4},\qquad a_{40} > 0,\quad x_4 \ge 0,\qquad v^2 = -\frac{\mu^2}{\lambda} \tag{IN-12}
$$
<!-- symbols: Phi, Aadhoc, x4, vev, hHiggs, vA, euler, a40, muH, lamH -->
<!-- begin generated symbol list -->
**Symbols in (IN-12).**

- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $h$: The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$. Unit: GeV. Value: $m_h = 125.25$ GeV. Status: STANDARD.
- $v_{\mathcal{A}}$: The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc $= \mathrm{Exp}[-2\,a_{40}\,x_4]$ has $v_{\mathcal{A}} = 1$ in the units of his notebook. Unit: GeV. Value: 1 in the units of the author's notebook; UM-3 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$). Status: AUTHOR (the form), ASSUMED (a free amplitude).
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_{40}$: The decay constant of almightyAdHoc, $a_{40} > 0$: $\mathcal{A}$ falls by $\mathrm{e}$ in the time $1/(2a_{40})$. Unit: GeV (1/length). Status: AUTHOR.
- $\mu^2$: The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$). Unit: GeV$^2$. Value: $\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.

<!-- end generated symbol list -->

The Higgs doublet with the author's potential, expanded about the author's ad hoc vacuum, whose upper component almightyAdHoc
decays as $\mathrm{e}^{-2a_{40}x_4}$ (the author writes $\mathrm{Exp}[-2a_{40}x_4]$; UM-3 gives it the amplitude $v_{\mathcal{A}}$ so that it has the
dimension of the Higgs field). Status: AUTHOR.

## The gauge fields, the quarks and the leptons

$$
\begin{aligned}
D_\mu &= \partial_\mu + \hat\omega_\mu - \mathrm{i}g_3\,G^A_\mu\,t^A - \mathrm{i}g_2\,W^I_\mu\,\frac{\tau^I}{2}
 - \mathrm{i}g_1\,Y_f\,B_\mu,\\
\mathcal{L}_{\mathrm{gauge}} &= -\frac14\,G^A_{\mu\nu}G^{A\mu\nu} - \frac14\,W^I_{\mu\nu}W^{I\mu\nu} - \frac14\,B_{\mu\nu}B^{\mu\nu},\\
G^A_{\mu\nu} &= \partial_\mu G^A_\nu - \partial_\nu G^A_\mu + g_3\,f^{ABC}G^B_\mu G^C_\nu,\qquad
W^I_{\mu\nu} = \partial_\mu W^I_\nu - \partial_\nu W^I_\mu + g_2\,\epsilon^{IJK}W^J_\mu W^K_\nu,\qquad
B_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu
\end{aligned} \tag{IN-13}
$$
<!-- symbols: Dcov, imu, inu, partial, omegahat, imag, g3, Ggluon, iA, iB, iC, tgen, g2, Wsu2, iI, iJ, iK, taupauli, g1, Yhyp, if, Bhyp, Lgauge, fabc, epsLC -->
<!-- begin generated symbol list -->
**Symbols in (IN-13).**

- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\hat\omega_\mu$: The spin connection of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold acting on four-dimensional spinors. Unit: 1/length. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling (the strong coupling $g_s$). Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($\alpha_s = 0.1180$). Status: STANDARD.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $B$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $C$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $t^A$: The generators of $SU(3)$ on colour triplets, $t^A = \lambda_{\mathrm{GM}}^A/2$ (the Gell-Mann matrices halved), $\mathrm{tr}(t^At^B) = \delta^{AB}/2$. Unit: dimensionless. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $J$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.
- $K$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square). Unit: dimensionless. Status: STANDARD.
- $g_1$: The $U(1)_Y$ gauge coupling (usually $g'$; not normalised for grand unification). Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $Y_f$: The hypercharge of a field, the charge of its coupling $g_1Y_fB_\mu$ to the hypercharge field in the covariant derivative ($1/6$, $2/3$, $-1/3$, $-1/2$, $-1$, $0$ for $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$, $1/2$ for $\Phi$). Unit: dimensionless. Status: STANDARD.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold. Unit: GeV$^4$. Status: STANDARD.
- $f^{ABC}$: The structure constants of $SU(3)$, $[t^A, t^B] = \mathrm{i}f^{ABC}t^C$. Unit: dimensionless. Status: STANDARD.
- $\epsilon^{IJK}$: The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

$$
\begin{aligned}
&\mathcal{L}_{\mathrm{f}} = \sum_{\psi}\mathrm{i}\,\bar\psi\,\hat\gamma^\mu D_\mu\psi,\qquad
 \psi \in \{Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}\},\\
&\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1},\qquad \bar\psi = \psi^\dagger\beta,\qquad
 \beta = \hat\gamma^{(4)},\qquad \hat\gamma_5 = \mathrm{i}\,\hat\gamma^{(4)}\hat\gamma^{(1)}\hat\gamma^{(2)}\hat\gamma^{(3)},\\
&\hat P_{\mathrm{L}} = \frac{\mathbf{1} - \hat\gamma_5}{2},\quad \hat P_{\mathrm{R}} = \frac{\mathbf{1} + \hat\gamma_5}{2},\qquad
 \hat P_{\mathrm{L}}Q = Q,\quad \hat P_{\mathrm{L}}\ell = \ell,\quad \hat P_{\mathrm{R}}u_{\mathrm{R}} = u_{\mathrm{R}},\quad
 \hat P_{\mathrm{R}}d_{\mathrm{R}} = d_{\mathrm{R}},\quad \hat P_{\mathrm{R}}e_{\mathrm{R}} = e_{\mathrm{R}},\quad
 \hat P_{\mathrm{R}}\nu_{\mathrm{R}} = \nu_{\mathrm{R}}
\end{aligned} \tag{IN-14}
$$
<!-- symbols: Lf, ipsi, imag, psiSM, gammahat, imu, Dcov, Qdoub, uR, dR, ell, eR, nuR, inu, hhat, identity, dagger, betaD, gamma5hat, PLhat, PRhat -->
<!-- begin generated symbol list -->
**Symbols in (IN-14).**

- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\psi$: The label of a Standard-Model fermion field in a sum: $\psi$ runs over $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\psi,\ \bar\psi$: A Standard-Model fermion field (a four-dimensional Weyl field of the fold with three generations, written as a four-component spinor of fixed chirality); $\bar\psi = \psi^\dagger\beta$; $\psi_f$ the fields of the kind $f$. Unit: GeV$^{3/2}$. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\beta$: The matrix of the four-dimensional Dirac adjoint, $\beta = \hat\gamma^{(4)}$ (Hermitian, $\beta^2 = \mathbf{1}$). Unit: dimensionless. Status: STANDARD.
- $\hat\gamma_5$: The four-dimensional chirality matrix, $\hat\gamma_5 = \mathrm{i}\hat\gamma^{(4)}\hat\gamma^{(1)}\hat\gamma^{(2)}\hat\gamma^{(3)}$, $\hat\gamma_5^2 = \mathbf{1}$. Unit: dimensionless. Status: STANDARD.
- $\hat P_{\mathrm{L}}$: The four-dimensional left-handed projector, $\hat P_{\mathrm{L}} = (\mathbf{1} - \hat\gamma_5)/2$. Unit: dimensionless. Status: STANDARD.
- $\hat P_{\mathrm{R}}$: The four-dimensional right-handed projector, $\hat P_{\mathrm{R}} = (\mathbf{1} + \hat\gamma_5)/2$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

$$
\mathcal{L}_{\mathrm{Y}} = -\big(\bar Q\,\mathcal{Y}^{u}\,\tilde\Phi\,u_{\mathrm{R}} + \bar Q\,\mathcal{Y}^{d}\,\Phi\,d_{\mathrm{R}}
 + \bar\ell\,\mathcal{Y}^{e}\,\Phi\,e_{\mathrm{R}} + \bar\ell\,\mathcal{Y}^{\nu}\,\tilde\Phi\,\nu_{\mathrm{R}}\big)
 + \mathrm{h.c.},\qquad \tilde\Phi = \mathrm{i}\tau^2\Phi^* \tag{IN-15}
$$
<!-- symbols: LY, Qdoub, Yuk, Phitilde, uR, Phi, dR, ell, eR, nuR, hc, imag, taupauli, star -->
<!-- begin generated symbol list -->
**Symbols in (IN-15).**

- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\mathrm{h.c.}$: The Hermitian conjugate of the preceding terms. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square). Unit: dimensionless. Status: STANDARD.
- ${}^*$: Complex conjugation of a number, or of each entry of a matrix or column. Status: STANDARD.

<!-- end generated symbol list -->

The gauge fields of $SU(3)_{\mathrm{C}} \times SU(2)_{\mathrm{L}} \times U(1)_Y$ on the fold (IN-13), the three generations of quarks and leptons
with three right-handed neutrinos (IN-14), and their Yukawa couplings to the Higgs doublet (IN-15). With the right-handed neutrinos
the gauge anomalies still cancel (DERIVED, `um3_fields.py`), and the neutrino Yukawa couplings give the neutrinos Dirac masses, whose
values are chosen to reproduce the measured mass differences with the lightest mass zero (ASSUMED). Status: STANDARD (UM-3 adds the
right-handed neutrinos).

## The portals of dirac16complex

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

The new interactions of UM-3: every Standard-Model field couples at the fold to the left-handed and to the right-handed half of
dirac16complex, each with its own coupling, through gauge-invariant operators: the Higgs portal (left-handed half only), the
gauge-kinetic portals of the gluons, $W$ and $B$, a dipole portal to $B$, and current portals between the fermion-number current
of every multiplet of the Standard Model and the convective currents of the two halves. Each is invariant under the gauge group of
the Standard Model and contains dirac16complex only in bilinears, so the charge of dirac16complex is conserved and its lightest
states cannot decay into the Standard Model alone. The charge is indefinite (a Krein form); quantised with positive energies, every
quantum carries a positive energy, so the vacuum is stable, and the dilute gas of the bound particles is stable as well, while a dense
gas is not; but the modes of positive Krein charge are ghosts (negative norm), and every coupling of the fold that distinguishes the two
chiralities, the Higgs portal of the left-handed half among them, creates them together with physical particles: with these portals
UM-3 is not a unitary quantum theory, and a unitary UM-3 would need couplings of the fold that do not distinguish the chiralities.
Status: INVENTED (the portals), DERIVED (the stability and the ghosts, `um3_krein.py`), OPEN (a unitary coupling).

# The parameters

| parameter | meaning | value | status |
| ------ | ------ | ------ | ------ |
| $H$ | the author's constant: the period $\pi/(6H)$ of $x_0$, the warp, the Lovelock weights | free; the bound states of dirac16complex need $H \ll q_{\mathrm{b}}$, where $q_{\mathrm{b}}$ is the inverse width of their profile $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$ along the hidden direction | AUTHOR |
| $a_4(x_4)$, $b_4(x_4)$ | the author's functions of the time | the author's vacuum $a_4 = Hx_4$ with constant $b_4$ (primordial); frozen extra times $\mathrm{e}^{-a_4}b_4$ = constant (late) | AUTHOR, DERIVED |
| $\alpha_{(p)}$, $\Lambda$ | Lovelock weights and cosmological constant of the bulk | $\alpha_{(p)} = H^{2-2p}w_{(p)}$ with $w = (1, 1/32, 1/1152)$, $\Lambda = -10H^2$ | AUTHOR |
| $\kappa = 8\pi G_8$ | the gravitational coupling of the bulk | free | ASSUMED |
| $\kappa_4$ | the coupling of the induced gravity of the fold | $8\pi G_{\mathrm{N}}(1 + 5\epsilon_{\mathrm{r}}/6)$, with Newton's constant $G_{\mathrm{N}}$ | ASSUMED, DERIVED |
| $V_*$ | the physical volume of the extra times at the fold | free | ASSUMED |
| $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$ | the ratio of bulk to fold gravity | below $1.344\times10^{-13}$: the four-dimensional gravitational waves move with $c_{\mathrm{g}}^2 = (96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})$, and those of the neutron-star merger GW170817 arrived with its light, $c_{\mathrm{g}} - 1 < 7\times10^{-16}$ | DERIVED |
| $\xi_{\mathrm{H}}$ | the coupling of the Higgs doublet to the curvature of the fold | free; below $1/6$ if the gravity of the fold is induced by its fields | ASSUMED |
| $\rho_{\mathrm{s}}$, $p_{\mathrm{s}}$ | the stabiliser | $-H^2/(16\kappa)$, $5\rho_{\mathrm{s}}$; no free parameter | DERIVED |
| $\rho_{\mathrm{ff}}$, $p_{\mathrm{ff}}$, $q_{\mathrm{ff}}$ | the fold fluid (energy density, pressure along ordinary space, pressure along the extra times) | at the static block a tension $61HV_*/(8\kappa)$ with the pressureless part $HV_*/(8\kappa)$; $\rho_{\mathrm{ff}} - 31HV_*/(4\kappa) = \rho_\Lambda = (2.2\ \text{meV})^4$, the vacuum energy of the fold (the dark energy) | ASSUMED (its values DERIVED) |
| $m_\Psi$ | the bulk mass of dirac16complex | free | RECORD |
| $\lambda_\Psi$ | the self-coupling of dirac16complex | free | RECORD |
| $c_\Phi$, $c^{G}_X$, $c^{W}_X$, $c^{B}_X$, $d_X$, $c^{f}_X$ | the portal couplings ($X$ = L, R) | free; direct detection and the effective number of neutrino species $N_{\mathrm{eff}}$ (the energy density of the relativistic species besides the photons, in units of one neutrino species) constrain them | INVENTED |
| $v$, $\lambda$, $\mu^2$ | the Higgs vacuum and potential | $v = 246.22$ GeV, $\lambda = 0.129$, $\mu^2 = -\lambda v^2$ | AUTHOR, STANDARD |
| $v_{\mathcal{A}}$, $a_{40}$ | amplitude and rate of the ad hoc vacuum $\mathcal{A} = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$ | the author's amplitude is 1 in the units of his notebook; UM-3 keeps $v_{\mathcal{A}}$ free (the examples take $v$ and $10v$); $a_{40} > 0$; nucleosynthesis needs $a_{40} > \ln(v_{\mathcal{A}}/(0.1v))/(2\ \text{s})$ | AUTHOR, ASSUMED (a free amplitude) |
| $g_1$, $g_2$, $g_3$ | the gauge couplings | the measured values | STANDARD |
| $\mathcal{Y}^{u}$, $\mathcal{Y}^{d}$, $\mathcal{Y}^{e}$, $\mathcal{Y}^{\nu}$ | the Yukawa matrices | the measured masses and mixings (Particle Data Group); neutrinos (the global fit NuFIT 5.2 of the oscillation data, November 2022, normal ordering, with the Super-Kamiokande atmospheric data): the differences of the squared masses of the three mass states $\Delta m^2_{21} = 7.41\times10^{-5}$ eV$^2$ and $\Delta m^2_{31} = 2.511\times10^{-3}$ eV$^2$, the mixing angles $\theta_{12} = 33.40^\circ$, $\theta_{13} = 8.54^\circ$, $\theta_{23} = 49.14^\circ$; the lightest mass 0 and the Dirac phase 0. The newer fit NuFIT 6.0 (2024) changes the results of UM-3 by at most 1.5 per cent; the Dirac phase (212 degrees in NuFIT 6.0) drops out of every result of UM-3; DESI DR2 with the CMB bounds the lightest mass below 4.12 meV | STANDARD, ASSUMED (the lightest mass; the phase is irrelevant, DERIVED) |
| $A_{\mathrm{s}}$, $n_{\mathrm{S}}$, $\tau_{\mathrm{reion}}$ | the primordial spectrum and the optical depth | Planck 2018: $\ln(10^{10}A_{\mathrm{s}}) = 3.044$, $n_{\mathrm{S}} = 0.9649$, $\tau_{\mathrm{reion}} = 0.0544$; the author's vacuum would give $n_{\mathrm{S}} - 1 = 2.5$, so these values need an inflationary era with frozen extra times that UM-3 does not contain | ASSUMED (inputs; the era OPEN) |
