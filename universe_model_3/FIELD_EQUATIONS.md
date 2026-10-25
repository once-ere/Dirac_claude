---
title: "UM-3 field equations"
subtitle: 'The complete set of coupled field equations of Einstein-Lovelock gravity, dirac16complex, the Higgs doublet with the ad hoc vacuum, the gauge fields of SU(3), SU(2) and U(1), and three generations of quarks and leptons with three right-handed neutrinos'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Field equations of UM-3, 2026-10-24"
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

This document states the complete set of coupled field equations of the universe model UM-3, derives every one of them
from one action, and explains every term. It is self-contained: every equation it uses is written in it, and every symbol
of every equation is defined right after the equation. The sections are:

* **Where the fields live** (this section): the author's metric has a fold, the seven-dimensional surface $z = \pi/2$, that
  carries energy; the Standard Model lives on the fold, dirac16complex and gravity in the bulk.
* **The action** (IN-1 to IN-16): every term of the action, written out and explained; with the speed of the gravitational waves
  of the fold (FE-63), the gravity that the fields of the fold induce (FE-64) and the two parts of the fold fluid (FE-65).
* **Gravity** (FE-1 to FE-11): the Einstein-Lovelock equations in the bulk, the junction conditions at the fold, the
  energy-momentum tensor of every field and the conservation laws.
* **The matter fields** (FE-12 to FE-26): the field equations of dirac16complex, of the Higgs doublet, of the gauge fields
  and of the quarks and leptons, and the equations of the ad hoc Higgs vacuum.
* **The background** (FE-27 to FE-35, FE-66): the author's metric, its exact curvature, the exact background equations in the
  bulk and at the fold, the author's vacuum, the static late-time state, the frozen extra times, the two constraints of the bulk
  equations and the power series of the metric.
* **dirac16complex: modes and Kohn-Sham equations** (FE-36 to FE-43, FE-67): the equation of the hidden direction, the bulk
  continuum, the states bound to the fold, the Kohn-Sham equations with the mean fields of every other field, the Krein norm
  and its quantisation.
* **The Standard Model on the fold** (FE-44 to FE-47): the four-dimensional couplings, the masses with the ad hoc vacuum, the
  mixing matrices and the four-dimensional couplings of the bound states of dirac16complex.
* **The three neutrino flavours** (FE-48 to FE-53): the flavour evolution in vacuum, in matter, in dense neutrino gases
  (supernovae) and in the early Universe.
* **The cosmological perturbations** (FE-54 to FE-58): the metric as a power series and the Einstein-Boltzmann equations of the
  cosmic microwave background (CMB), the cosmic neutrino background (CNB) and the baryon acoustic oscillations (BAO).
* **The thermal history** (FE-59 to FE-62): the expansion of the fold, the degrees of freedom and the Boltzmann equations of
  the bound states of dirac16complex and of the right-handed neutrinos.
* **The coupled system**: which field appears in which equation, and how the system is solved.
* **What was verified**: the checks of the computations behind every derived statement.

## The status labels

Every equation and every result carries one of the labels

* **AUTHOR**: from the author (his notebooks `4+4.nb` and `Dirac_Einstein-Lovelock_4+4_Nash.nb`, and his order of 2026-10-24:
  the coordinates, the metric, the Lovelock weights, the Dirac matrices, the chiral projectors, the list of fields, the
  Higgs potential and the ad hoc vacuum);
* **RECORD**: from the record of this repository (the Lagrangian of dirac16complex with its canonical spin connection and its
  contact self-interaction, the Kohn-Sham treatment);
* **STANDARD**: textbook physics;
* **ASSUMED**: a choice made in UM-3 without derivation;
* **INVENTED**: a new interaction of UM-3 (the portals of dirac16complex);
* **DERIVED**: computed and verified in UM-3 (the verification is stated);
* **ESTIMATE**: an order-of-magnitude evaluation;
* **OPEN**: not settled.

## Every equation is followed by its symbols

Every display equation is followed by the list "Symbols in (FE-n)" (or "Symbols in this equation" for a display without a
tag) of EVERY symbol that appears in it: every quantity, field, coupling, constant and operator, every index letter with the
values it takes, every mark (prime, dagger, transpose, star), the imaginary unit, Euler's number and the differential. Each
item gives the meaning, the unit (natural units $\hbar = c = 1$), the value where one exists, and the status. A field
equation carries the tag FE-1 to FE-67 and a term of the action the tag IN-1 to IN-16; the numbering is that of the inventory
of UM-3 and is the same in every UM-3 document (FE-63 to FE-67 were added on 2026-10-25 and stand in the sections of their
subjects). Displays without a tag are steps of a derivation.

## Coordinates, signature and units

The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ is the hidden
space-like coordinate, on which the metric depends periodically with the period $\pi/(6H)$ through the angle $z = 6Hx_0$;
$x_1, x_2, x_3$ are ordinary space, $x_4$ is the time, and $x_5, x_6, x_7$ are three extra time-like coordinates. The
signature is $(+,+,+,+,-,-,-,-)$ in this order; the four observable coordinates $x_1, \dots, x_4$ have the signature
$(+,+,+,-)$. $H$ is the author's constant (an inverse length); this document keeps it as a free parameter. Units are natural,
$\hbar = c = 1$; in eight dimensions the field dirac16complex has the dimension GeV$^{7/2}$ and the gravitational coupling
$\kappa = 8\pi G_8$ the dimension GeV$^{-6}$. A prime on a function of the time $x_4$ alone is its derivative
$\mathrm{d}/\mathrm{d}x_4$ (in the cosmological perturbation equations, and only there, a dot is the derivative with respect
to the conformal time). The proper coordinate of the hidden direction is $\sigma$ (defined in FE-27): $\sigma = 0$ is the
fold $z = \pi/2$.

## The fields of UM-3 and where they live

The author orders a model universe with the following coupled fields (his order of 2026-10-24, items 1 to 10); UM-3 adds
the right-handed quark singlets, the Yukawa couplings and three right-handed neutrinos (accepted by the author on 2026-10-24
at 17:32), the stabiliser of the bulk, the fold fluid and the induced gravity of the fold (ASSUMED, explained below).

| field | symbol | what it is | lives in | it couples to | field equations |
| ---------------- | -------------- | ---------------------- | ----------- | ---------------------- | ---------------------- |
| Einstein-Lovelock gravity | $g_{MN}$ | the metric of eight dimensions | bulk and fold | every field | FE-1 to FE-11, FE-27 to FE-35, FE-54, FE-59 |
| dirac16complex | $\Psi$ | the author's 16-component complex spinor field; its left- and right-handed halves $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | the bulk | gravity (spin connection), itself, every Standard-Model field at the fold (IN-16) | FE-6, FE-12 to FE-14, FE-36 to FE-43, FE-47, FE-55, FE-61 |
| Higgs doublet | $\Phi$ | the scalar doublet with $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$, expanded about the ad hoc vacuum $\Phi = (\mathcal{A}, v + h)/\sqrt2$ | the fold | gravity, $W$, $B$, the fermions (Yukawa), $\Psi_{\mathrm{L}}$ only | FE-7, FE-15, FE-26, FE-45, FE-49 |
| three left-handed lepton doublets | $\ell_i$ | $(\nu_{\mathrm{L}i}, e_{\mathrm{L}i})$, $i = 1, 2, 3$ | the fold | gravity, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$ and $\Psi_{\mathrm{R}}$ | FE-9, FE-22, FE-48 to FE-53 |
| right-handed electron, muon, tau | $e_{\mathrm{R}i}$ | the charged-lepton singlets | the fold | gravity, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | FE-9, FE-23 |
| three right-handed neutrinos | $\nu_{\mathrm{R}i}$ | gauge singlets; Dirac neutrino masses | the fold | gravity, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | FE-9, FE-24, FE-62 |
| gauge fields of $SU(2)_L$ and $U(1)_Y$ | $W^1$, $W^2$, $W^3$, $B$ | the electroweak gauge fields | the fold | gravity, $\Phi$, the fermions, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | FE-8, FE-17, FE-18, FE-45 |
| three quark generations | $Q_i$, $u_{\mathrm{R}i}$, $d_{\mathrm{R}i}$ | the quark doublets and singlets | the fold | gravity, gluons, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | FE-9, FE-19 to FE-21, FE-46 |
| gluons | $G^A$ | the gauge field of $SU(3)_C$ | the fold | gravity, quarks, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | FE-8, FE-16 |
| stabiliser | $\mathcal{T}_{\mathrm{stab}}$ | a medium of the bulk that keeps the late-time bulk static | the bulk | gravity | FE-3, FE-32 |
| fold fluid | $\mathcal{T}_{\mathrm{ff}}$ | the part of the thin source that the kink of the metric requires at the fold not supplied by the other fields | the fold | gravity | FE-4, FE-5, FE-31 to FE-33, FE-59 |
| induced gravity of the fold | $\kappa_4$ | an Einstein-Hilbert term of the fold | the fold | gravity | FE-5, FE-59 |

**Why the Standard Model lives on the fold (DERIVED).** In the proper coordinate $\sigma$ of the hidden direction (FE-27), one
period of $x_0$ is the whole line $-\infty < \sigma < \infty$ and the author's metric is
$\mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\big(\mathrm{e}^{2a_4}\,\mathrm{d}\vec x^2 - \mathrm{e}^{-2a_4}b_4^2\,\mathrm{d}\vec x_5^2\big) - \mathrm{d}x_4^2$:
ordinary space is warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$, the time $x_4$ is not. A field confined to the fold
$\sigma = 0$ has the light cone of the fold; a field that spreads into the bulk moves along ordinary space with a speed set by
the $\sigma$-average of $\mathrm{e}^{2H\lvert\sigma\rvert}$ over its profile. With the author's metric a bulk photon moves
$\sqrt2$ times faster than light on the fold, a bulk scalar $\sqrt{3/2}$ times, a bulk fermion with a profile of width $1/M$
$2M/(2M - H)$ times (DERIVED, `um3_bulk.py`, checks B1 to B3). Species with different profiles would have different limiting
speeds (excluded at the level $10^{-15}$ to $10^{-20}$ for photons, electrons and nucleons), and three neutrino flavours with
three profiles would oscillate with energy-proportional phases that observation excludes. The author's request for correct
flavour conversion therefore fixes the place of the Standard Model: all of it lives on the fold, where it has one light cone,
and its flavour physics is that of the Standard Model with three Dirac neutrinos. dirac16complex is the author's field of
eight dimensions and lives in the bulk; it couples to the Standard Model at the fold.

**Why the fold carries a source (DERIVED).** The warp $\mathrm{e}^{-2H\lvert\sigma\rvert}$ has a kink at the fold. The
Einstein-Lovelock equations, which are linear in the second derivatives of the metric along $\sigma$, then contain a delta
function at $\sigma = 0$: the metric is a solution only if the fold carries a thin source $\mathcal{S}^a{}_b$ (FE-4). At the
author's vacuum $\kappa\mathcal{S} = \mathrm{diag}(-10H, -6H, -10H)$ for (ordinary space, time, extra times) (DERIVED,
`um3_fold.py`, check J5). This source is the fold fluid together with the Standard Model and the portals.

**Why the fold has its own Einstein-Hilbert term (DERIVED: the need; ASSUMED: the term).** The transverse traceless gravitons of
the bulk, with the author's Lovelock weights, have at the static late-time state the limiting speed $\sqrt{15/2} = 2.74$ times the
speed of light on the fold, and no time-kinetic term at all at the author's vacuum (DERIVED, `um3_bulk.py`, B5). The Gauss-Bonnet
and cubic terms of the author's action give the kink of the fold a graviton term of its own; with it the four-dimensional
gravitational wave (the zero mode, the same at every $\sigma$) moves with $c_{\mathrm{g}}^2 = 83/82$, 0.61 per cent faster than light
(FE-63; DERIVED, `um3_foldsources.py`, F1 to F3). Gravitational waves move with the speed of light to $7\times10^{-16}$ (GW170817).
UM-3 therefore gives the fold an Einstein-Hilbert term of its own, the induced gravity IN-9, which dominates four-dimensional
gravity: with it $c_{\mathrm{g}}^2 = (96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})$, and the bulk may contribute only the fraction
$\epsilon_{\mathrm{r}} < 1.344\times10^{-13}$ (FE-63, F4). A term of this form is induced by the quantum fluctuations of the fields of the fold
(FE-64).

## Conventions

* Indices. $M, N, P, Q$ (with numbered copies $M_1, M_2, \dots$): coordinate indices of eight dimensions; $a, b, c, d$: frame
  indices of eight dimensions (the frame direction $(0)$ is the $\sigma$ direction); $\mu, \nu, \rho$: coordinate indices of
  the four observable directions $x_1, \dots, x_4$; $A, B, C = 1, \dots, 8$: colour (adjoint) indices; $I, J, K = 1, 2, 3$:
  weak-isospin (adjoint) indices; $i, j = 1, 2, 3$: generations (and the neutrino mass states); $\alpha, \beta = e, \mu, \tau$:
  lepton flavours; $p = 1, 2, 3$: the Lovelock order; $l = 0, 1, 2, \dots$: the multipole index of the cosmological perturbations; $X = \mathrm{L}, \mathrm{R}$: the two halves of dirac16complex;
  $f \in \{Q, u, d, \ell, e, \nu\}$: the six kinds of Standard-Model multiplets. A repeated index is summed over its range.
* Two kinds of Dirac matrices. The author's real $16 \times 16$ matrices $T_a$ (IN-5) act on dirac16complex; the
  four-dimensional complex $4 \times 4$ matrices $\hat\gamma^\mu$ (IN-14) act on the Standard-Model fermions. They are never
  multiplied with each other; the couplings between dirac16complex and the Standard Model are products of Lorentz tensors.
* Normalisation of the fold. No field depends on the extra times $x_5, x_6, x_7$ (ASSUMED: a dependence on them gives
  tachyonic four-dimensional modes, FE-38). Integrated over them, the extra times give their physical volume on the fold,
  $V_*$; the Standard-Model fields are normalised as four-dimensional fields, the couplings are their measured
  four-dimensional values, and the fold action carries the factor $1/V_*$ (IN-8).
* A word or a particle name in a subscript is upright ($m_{\mathrm{W}}$, $\nu_{\mathrm{R}}$, $\Psi_{\mathrm{L}}$); an italic letter
  in a subscript is an index. $\mathrm{e}$ is Euler's number, $\mathrm{i}$ the imaginary unit, $\mathrm{d}$ the differential;
  $\delta$ is the Kronecker delta and $\delta_{\mathrm{D}}$ the Dirac delta function.


# The action

All field equations of UM-3 follow from one action by varying it with respect to every field. This section writes out every
term of the action (IN-1 to IN-16) and says in plain words what it couples. The Standard-Model part has exactly the gauge
group, the fermion content (three generations, each with a right-handed neutrino), the Higgs potential and the gauge couplings
of the Standard Model; it lives on the fold. dirac16complex is a singlet of the Standard-Model gauge group; its left-handed
and right-handed halves couple to every Standard-Model field at the fold through gauge-invariant portals with their own
coupling constants, and only its left-handed half couples to the Higgs doublet.

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

The action has four parts: Einstein-Lovelock gravity in eight dimensions ($S_{\mathrm{EL}}$, IN-2, IN-3), the stabiliser of
the bulk ($S_{\mathrm{stab}}$, IN-7), the field dirac16complex in the bulk ($S_\Psi$, IN-4 to IN-6) and the fold
($S_{\mathrm{fold}}$, IN-8 to IN-16). The Dirac delta $\delta_{\mathrm{D}}(\sigma)$ of the proper hidden coordinate $\sigma$
confines the terms of the fold to $\sigma = 0$; the factor $1/V_*$ turns the integral over the extra times into the
normalisation of four-dimensional fields (IN-8). On the fold live: the induced gravity of the fold ($\mathcal{L}_{\mathrm{IG}}$),
the fold fluid ($\mathcal{L}_{\mathrm{ff}}$), the Higgs doublet ($\mathcal{L}_{\mathrm{H}}$), the gauge fields
($\mathcal{L}_{\mathrm{gauge}}$), the quarks and leptons ($\mathcal{L}_{\mathrm{f}}$), their Yukawa couplings
($\mathcal{L}_{\mathrm{Y}}$) and the portals of dirac16complex ($\mathcal{L}_{\mathrm{P}}$). Varying $S_{\mathrm{tot}}$ with
respect to the metric gives the gravitational equations (FE-1, FE-4); with respect to $\bar\Psi$ the equation of
dirac16complex (FE-12, FE-13); with respect to $\Phi^\dagger$ the Higgs equation (FE-15); with respect to the gauge fields the
Yang-Mills equations (FE-16 to FE-18); with respect to every fermion its Dirac equation (FE-19 to FE-24). Status: ASSUMED
(the choice and the place of the terms; the content of each term is stated with its own label).

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

Gravity is the Einstein-Lovelock theory in eight dimensions with the author's weights. $\mathcal{L}_{(1)}$ is the
Einstein-Hilbert density (the Ricci scalar), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density and $\mathcal{L}_{(3)}$ the cubic
Lovelock density; in eight dimensions the series ends with $p = 3$ (the density of order 4 is a total derivative in eight
dimensions). The author writes the vacuum equations as
$0 = -\Lambda_{\mathrm{N}} + H^{-2}w_{(1)}\mathcal{E}_{(1)} + H^{-4}w_{(2)}\mathcal{E}_{(2)} + H^{-6}w_{(3)}\mathcal{E}_{(3)}$ with the pure number
$\Lambda_{\mathrm{N}} = 10$ (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[134]); multiplied by $H^2$ this is FE-1 without sources
and with $\Lambda = -\Lambda_{\mathrm{N}}H^2 = -10H^2$. Gravity couples to every field through the metric that appears in every
other term of the action (in $\sqrt{\lvert g\rvert}$, in the contractions of indices and in the spin connection). Status:
AUTHOR.

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

The Lovelock densities are built with the generalised Kronecker delta from $p$ Riemann tensors. Their key property
(Lovelock's theorem, STANDARD) is that their metric variation contains no derivative of the metric higher than the second,
so that the field equations FE-1 are second-order differential equations, and that it is linear in the second derivatives
along any one direction (quasi-linearity): a thin source at the fold produces a finite jump of first derivatives, the
junction conditions FE-4. Status: STANDARD.

## The field dirac16complex

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

dirac16complex $\Psi$ is the author's complex spinor field of eight dimensions with 16 components. Its Lagrangian is that of the
record: the kinetic term with the canonical spin connection (in the symmetric form, which is real without a factor
$\mathrm{i}$ for the author's real matrices, IN-5), the mass term and a contact self-interaction. It couples to gravity through
$\sqrt{\lvert g\rvert}$, $\gamma^M$ and the spin connection $\Omega_M$ inside $D_M$ (IN-6), and to itself through
$\lambda_\Psi$. $\bar\Psi\Psi = \bar\Psi_{\mathrm{L}}\Psi_{\mathrm{L}} + \bar\Psi_{\mathrm{R}}\Psi_{\mathrm{R}}$ (the mass term
does not mix the halves, IN-5), while the kinetic term mixes them (it contains one Dirac matrix). Status: RECORD.

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

$T_a$ ($a = 0, \dots, 7$) are the author's eight real $16 \times 16$ Dirac matrices `T16^A[a]` of `4+4.nb`, and $\Gamma_8$ is the
author's chirality matrix `T16^A[8]` $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $P_{\mathrm{L}}$ and $P_{\mathrm{R}}$ are the
author's chiral projectors (the provenance document `dirac matrices.md` of UM-3 proves the Clifford relations, the reality and
the projectors; the facts used here are restated in this paragraph). The Dirac adjoint uses $\sigma_{16} = T_0T_1T_2T_3$:
$\sigma_{16}$ is real and symmetric, $\sigma_{16}T_a$ is real and antisymmetric, and $\sigma_{16}$ commutes with $\Gamma_8$
(it is a product of four Dirac matrices), so $\overline{P_X\Psi} = \bar\Psi P_X$ and every bilinear with an even number of Dirac
matrices joins a half with itself, every bilinear with an odd number joins $\Psi_{\mathrm{L}}$ with $\Psi_{\mathrm{R}}$
(DERIVED, `um3_fields.py`, checks F1 and F2). Status: AUTHOR (matrices, projectors), RECORD (adjoint).

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

The canonical spin connection $\varpi_{Mab}$ of the vielbein (antisymmetric in $a, b$) acts on the spinor through the generators
$\Sigma^{ab}$ of Spin(4,4). With it the Dirac matrices are covariantly constant ($D_M\gamma^N = 0$), the kinetic term of IN-4 is
a scalar and the field equation FE-12 is covariant. For the author's metric $\gamma^M\Omega_M$ is never zero (FE-14). Status:
RECORD (the canonical construction), DERIVED (the vielbein postulate for the author's metric, `um3_geometry.py`, G5).

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

$S_{\mathrm{stab}}$ is the action of a medium of the bulk; only its energy-momentum tensor $\mathcal{T}_{\mathrm{stab}}$ enters
the field equations, and IN-7 states it in the frame of the author's metric. With the author's weights and $\Lambda$, the bulk
of a universe whose ordinary space expands slowly (the late universe, $a_4' \ll H$) is not a vacuum solution: its frame
curvature is that of the static block (FE-32), which requires exactly this source, a negative energy density
$\rho_{\mathrm{s}} = -H^2/(16\kappa)$ with the isotropic pressure $p_{\mathrm{s}} = 5\rho_{\mathrm{s}}$ (DERIVED, `um3_geometry.py`,
G4; `um3_stabiliser.py`, ST1). More generally, no slowly changing bulk is a vacuum: without a bulk source the energy constraint
FE-66 keeps $\mathsf{A}^2 + \mathsf{U}^2 \ge 0.2607$ at every instant, and with frozen extra times it reads
$3a_4'^2 = 16\kappa(\rho_{\mathrm{bulk}} - \rho_{\mathrm{s}})$: the stabiliser is the energy density of the bulk at which ordinary space stands
still (ST8). The stabiliser was found and named by Claude (Anthropic) on 2026-10-24 while deriving these equations; its
properties, verified by `um3_stabiliser.py` (ST1 to ST8): it violates the weak and the null energy condition, and the only simple
field that reproduces it has a negative kinetic energy (a ghost; ST5); on the static bulk it is conserved by itself, so there it
couples only to gravity (ST4); when ordinary space grows, the bulk source that the equations require gives off energy that flows
along $\sigma$ into the fold and is taken up there exactly (FE-66, FE-33, FE-11; ST6), so the stabiliser then exchanges energy with
the fold; it is absent in the primordial era, whose bulk is the author's vacuum (FE-31; ST2), but a separately conserved medium
with $p = 5\rho$ keeps $\rho\,b_4^{18}$ constant and cannot appear later (ST6): its creation needs the exchange with the fold or a
change of its equation of state. Status: DERIVED (its value, and that the late bulk needs a source), ASSUMED (that the source is a
separate medium), OPEN (its microscopic origin and its creation).

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

The fold is the seven-dimensional surface $\sigma = 0$ ($z = \pi/2$) with the coordinates $x_1, \dots, x_7$. No field depends on
the extra times (ASSUMED, FE-38), so the integral over them gives their coordinate volume $V_{\mathrm{t}}$ (the extra times are
compact) times their scale factors $(\mathrm{e}^{-a_4}b_4)^3$ at the fold. $V_*$ is the physical volume of the extra times on the
fold in the late universe, where $\mathrm{e}^{-a_4}b_4$ is constant (FE-33); with this normalisation $\mathcal{Z} = 1$ in the
whole late universe, the fields of the fold are four-dimensional fields in the four-dimensional metric $\hat h_{\mu\nu}$ of the
fold, and their couplings are the measured four-dimensional ones. $\mathcal{Z}(x_4)$ is the factor by which the extra times
rescale every coupling of the fold when $\mathrm{e}^{-a_4}b_4$ changes (FE-44). $\mathbb{F}$ stands for any function of the fields on the
fold. Status: ASSUMED (the place of the fields), DERIVED (the reduction).

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

The induced gravity of the fold: an Einstein-Hilbert term of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold
($\hat R$ its scalar curvature), with the coupling $\kappa_4 = 8\pi G_{\mathrm{ind}}$. UM-3 assumes that it dominates four-dimensional
gravity, because without it the four-dimensional gravitational wave moves faster than light (FE-63). With it, four-dimensional
gravity on the fold is general relativity with Newton's constant $G_{\mathrm{N}}$ (FE-59), up to a fraction $\epsilon_{\mathrm{r}}$ of bulk
gravity, and the speed of the gravitational waves of GW170817 requires $\epsilon_{\mathrm{r}} < 1.344\times10^{-13}$ (FE-63). Status:
ASSUMED.

$$
\begin{aligned}
&K_{44}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2} + K_{33}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2} = 0,\qquad
 c_{\mathrm{g}}^2 = -\frac{K_{33}}{K_{44}} = \frac{96 + 83\,\epsilon_{\mathrm{r}}}{96 + 82\,\epsilon_{\mathrm{r}}},\\
&\kappa K_{44} = \frac{1}{96H} + \frac{5}{12H} + \frac{1}{2H\epsilon_{\mathrm{r}}},\qquad
 -\kappa K_{33} = \frac{5}{64H} + \frac{17}{48H} + \frac{1}{2H\epsilon_{\mathrm{r}}}
\end{aligned} \tag{FE-63}
$$
<!-- symbols: K44, partial, hgw, x4, K33, x3, cgrav, epsr, kappa, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (FE-63).**

- $K_{44}$: The coefficient of the second time derivative in the equation of the zero mode of a gravitational wave, integrated across the hidden direction: the sum of the parts of the bulk, of the Lovelock terms at the fold and of the induced gravity of the fold. Unit: GeV$^5$ ($\kappa K_{44}$ is a length). Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$ (the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$), in its zero mode, the same at every $\sigma$: the gravitational wave of the four-dimensional world. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $K_{33}$: The coefficient of the second derivative along $x_3$ in the equation of the zero mode of a gravitational wave (negative), with the same three parts. Unit: GeV$^5$. Status: DERIVED.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $c_{\mathrm{g}}$: The limiting speed of the zero mode of the transverse traceless graviton (the four-dimensional gravitational wave) at the static block or with frozen extra times, in units of the speed of light on the fold. Unit: dimensionless. Value: $\sqrt{15/2} = 2.74$ for the bulk alone; $\sqrt{83/82} = 1.0061$ with the graviton term of the fold from the Gauss-Bonnet and cubic Lovelock terms; $\sqrt{(96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})}$ with the induced gravity of the fold. Status: DERIVED.
- $\epsilon_{\mathrm{r}}$: The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$. Unit: dimensionless. Value: below $1.344\times10^{-13}$: the four-dimensional gravitational wave has $c_{\mathrm{g}}^2 = (96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})$, and the gravitational waves and the light of the neutron-star merger GW170817 arrived together, $(c_{\mathrm{g}} - 1) < 7\times10^{-16}$. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

The four-dimensional gravitational wave: a wave of the + polarisation travelling along $x_3$ on the static block or with frozen
extra times, in its zero mode (the same at every $\sigma$), with its field equation integrated across the hidden direction with
the volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$. Each coefficient has three parts: the bulk ($1/(96H)$ and $5/(64H)$), the thin
part of the Lovelock terms at the kink of the fold ($5/(12H)$ and $17/(48H)$, from the Gauss-Bonnet and the cubic terms of the
author's action; Einstein gravity alone has none), and the induced gravity IN-9 ($1/(2H\epsilon_{\mathrm{r}}) = \kappa/(2\kappa_4V_*)$). The bulk
alone gives $c_{\mathrm{g}}^2 = 15/2$, 2.74 times the speed of light; with the Lovelock terms of the fold $c_{\mathrm{g}}^2 = 83/82$
($c_{\mathrm{g}} = 1.0061$); with the induced gravity the wave approaches the light cone as $\epsilon_{\mathrm{r}} \to 0$, and the speed of the
gravitational waves of the neutron-star merger GW170817, which arrived together with its light, $c_{\mathrm{g}} - 1 < 7\times10^{-16}$,
requires $\epsilon_{\mathrm{r}} < 1.344\times10^{-13}$. At the author's vacuum the bulk has no time-kinetic term but the fold has
($\kappa K_{44} = 5/(12H)$ without the induced gravity, and $c_{\mathrm{g}}^2 = 19/10$). The Planck mass of the gravitational waves,
$(1 + 41\epsilon_{\mathrm{r}}/48)/\kappa_4$, and the Planck mass of the Friedmann equation of FE-59, $(1 + 5\epsilon_{\mathrm{r}}/6)/\kappa_4$, differ by the
factor $1 + \epsilon_{\mathrm{r}}/48$. Status: DERIVED (`um3_foldsources.py`, F1 to F4; the thin part also by smoothing the kink).

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

The Einstein-Hilbert term that the quantum fluctuations of the fields of the fold induce (Sakharov's induced gravity, evaluated at
one loop with the heat kernel and the proper-time cutoff $\Lambda_{\mathrm{c}}$): each real scalar with the curvature coupling $\xi$ counts
$1 - 6\xi$, each Weyl fermion 1, each gauge field $-4$ (with its ghost fields). In the Standard Model with three right-handed
neutrinos the 48 Weyl fermions and the 12 gauge fields cancel exactly, and only the four real scalars of the Higgs doublet remain,
$N_{\mathrm{ind}} = 4(1 - 6\xi_{\mathrm{H}})$ (without the right-handed neutrinos it would be $1 - 24\xi_{\mathrm{H}}$). The measured Newton constant
($G_{\mathrm{ind}} = G_{\mathrm{N}}$) then needs the cutoff $\Lambda_{\mathrm{c}} = \sqrt{24}\,\pi M_{\mathrm{red}} = 3.748\times10^{19}$ GeV, 3.07 times the Planck mass,
at $\xi_{\mathrm{H}} = 0$ ($M_{\mathrm{red}}$ the reduced Planck mass), and the sign requires $\xi_{\mathrm{H}} < 1/6$. Status: ESTIMATE (one loop and
cutoff-dependent; `um3_foldsources.py`, F5).

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

The fold fluid: a medium at rest on the fold (the frame indices $a, b$ run over the seven directions $1, \dots, 7$ of the fold), with the energy density $\rho_{\mathrm{ff}}$, the pressure $p_{\mathrm{ff}}$ along
ordinary space and the pressure $q_{\mathrm{ff}}$ along the extra times (four-dimensional normalisation, IN-8). The kink of the
author's metric at the fold requires a thin source (FE-4); the fold fluid is the part of it that the Standard Model and the
portals do not supply: at the static block $\rho_{\mathrm{ff}} = 31HV_*/(4\kappa)$, $p_{\mathrm{ff}} = q_{\mathrm{ff}} = -61HV_*/(8\kappa)$
(FE-32), at the author's vacuum $\rho_{\mathrm{ff}} = 6HV_*/\kappa$, $p_{\mathrm{ff}} = q_{\mathrm{ff}} = -10HV_*/\kappa$ less the
contribution of the induced gravity (FE-31). It plays the role of the brane tension of brane-world models; at the static block it
is a tension plus a small pressureless part (FE-65). $\mathcal{L}_{\mathrm{ff}}$ stands for its Lagrangian; only $\mathcal{T}_{\mathrm{ff}}$ enters
the field equations. Status: ASSUMED (its existence; its values DERIVED from the junction conditions); its microscopic origin is
OPEN.

$$
\rho_{\mathrm{ff}} = \lambda_{\mathrm{F}} + \rho_{\mathrm{d}},\qquad p_{\mathrm{ff}} = q_{\mathrm{ff}} = -\lambda_{\mathrm{F}},\qquad
\lambda_{\mathrm{F}} = \frac{61HV_*}{8\kappa},\qquad \rho_{\mathrm{d}} = \frac{HV_*}{8\kappa},\qquad
3a_4'\,\rho_{\mathrm{d}} = \frac{3}{8}\,\mathsf{A}\,\frac{H^2V_*}{\kappa} \tag{FE-65}
$$
<!-- symbols: rhoff, lambdaF, rhod, pff, qff, Hconst, Vstar, kappa, a4, prime, Asf -->
<!-- begin generated symbol list -->
**Symbols in (FE-65).**

- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $31HV_*/(4\kappa)$ at the static block. Status: ASSUMED.
- $\lambda_{\mathrm{F}}$: The tension of the fold fluid: the part of the fold fluid whose pressures along ordinary space and along the extra times are minus its energy density (a vacuum energy of the seven-dimensional fold), per unit volume of ordinary space of the fold. Unit: GeV$^4$. Value: $61HV_*/(8\kappa)$ at the static block. Status: DERIVED.
- $\rho_{\mathrm{d}}$: The pressureless part of the fold fluid: the energy density of the fold fluid minus its tension, per unit volume of ordinary space of the fold. Unit: GeV$^4$. Value: $HV_*/(8\kappa)$ at the static block. Status: DERIVED.
- $p_{\mathrm{ff}}$: The pressure of the fold fluid along ordinary space. Unit: GeV$^4$. Value: $-61HV_*/(8\kappa)$ at the static block. Status: ASSUMED.
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times. Unit: GeV$^4$. Value: $-61HV_*/(8\kappa)$ at the static block. Status: ASSUMED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.

<!-- end generated symbol list -->

The fold fluid of the static block (FE-32) is a tension $\lambda_{\mathrm{F}}$, a vacuum energy of the seven-dimensional fold whose pressures
along ordinary space and along the extra times are $-\lambda_{\mathrm{F}}$, plus a pressureless part $\rho_{\mathrm{d}}$, $1/62$ of its energy. The
vacuum energy of every field of the fold (its potential at the minimum) is a tension of this kind: the fields do not depend on the
extra times, so their pressure along the extra times is their on-shell Lagrangian (FE-5), minus the potential at the minimum, the
same as along ordinary space. A tension keeps its density when the fold grows; the pressureless part does not, and with frozen
extra times it needs the energy $3a_4'\rho_{\mathrm{d}}$ per unit volume and time to keep it: exactly $V_*$ times the part linear in
$\mathsf{A} = a_4'/H$ of the jump of the energy flow of the bulk at the fold (FE-66). The bulk feeds the fold fluid. Status: DERIVED
(`um3_foldsources.py`, F6; `um3_stabiliser.py`, ST6).

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

The Higgs doublet $\Phi$ (two complex components, hypercharge $1/2$) with the author's potential. In the signature
$(+,+,+,-)$ of the fold the kinetic term carries a minus sign, so that the energy density is positive. Status: AUTHOR (the
potential), STANDARD (the rest).

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

The author's ad hoc vacuum: the upper component of the Higgs doublet is the prescribed function almightyAdHoc
$\mathcal{A}(x_4) = \exp(-2a_{40}x_4)$ (the author writes it with the amplitude $v_{\mathcal{A}} = 1$ in the unit of the field;
UM-3 keeps $v_{\mathcal{A}}$ to show where it enters), the lower component is the vacuum expectation value $v$ plus the Higgs
field $h$. The Goldstone fields are absorbed by the gauge choice (unitary gauge). $\mathcal{A}$ decays with the rate
$2a_{40}$ from the beginning of the time $x_4 = 0$: it acts only in the primordial era. The ad hoc vacuum is not an exact solution
of the Higgs equation; the residuals are FE-26. Status: AUTHOR.

## The gauge fields

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

The gauge fields of $SU(3)_C \times SU(2)_L \times U(1)_Y$ on the fold, with the canonical normalisation (the couplings in the
covariant derivative): the gluons $G^A_\mu$, the weak-isospin fields $W^1_\mu, W^2_\mu, W^3_\mu$ and the hypercharge field
$B_\mu$. The covariant derivative of a field acts with the part that fits the field: $t^A$ on colour triplets, $\tau^I/2$ on
weak doublets, the hypercharge $Y_f$ of the field, and the four-dimensional spin connection $\hat\omega_\mu$ on spinors. The
hypercharges (STANDARD) are $Y = 1/6$ for $Q$, $2/3$ for $u_{\mathrm{R}}$, $-1/3$ for $d_{\mathrm{R}}$, $-1/2$ for $\ell$, $-1$ for
$e_{\mathrm{R}}$, $0$ for $\nu_{\mathrm{R}}$ and $1/2$ for $\Phi$. The gauge fields have no components along the extra times
(ASSUMED: such components would be scalars of wrong sign). Status: STANDARD.

## The quarks and leptons

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

Every Standard-Model fermion is a four-dimensional Weyl field on the fold, written as a four-component spinor with a fixed
chirality: the quark doublets $Q$ and the lepton doublets $\ell$ are left-handed, the singlets $u_{\mathrm{R}}$, $d_{\mathrm{R}}$,
$e_{\mathrm{R}}$, $\nu_{\mathrm{R}}$ right-handed. Each symbol stands for the three generations (a vector in generation space)
and, for quarks, the three colours. $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$ are complex $4 \times 4$ Dirac
matrices of the fold (with the frame matrices $\hat\gamma^{(a)}$, $a = 1, \dots, 4$, $(\hat\gamma^{(4)})^2 = \mathbf{1}$,
$(\hat\gamma^{(1)})^2 = (\hat\gamma^{(2)})^2 = (\hat\gamma^{(3)})^2 = -\mathbf{1}$); $\beta = \hat\gamma^{(4)}$ is Hermitian and
$(\hat\gamma^\mu)^\dagger = \beta\hat\gamma^\mu\beta$. With these conventions the free Dirac equation is
$(-\mathrm{i}\hat\gamma^\mu\partial_\mu + m)\psi = 0$ and $\bar\psi\beta\psi$-type energy densities are positive. Status:
STANDARD.

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

The Yukawa couplings, with the complex $3 \times 3$ matrices $\mathcal{Y}^{u}$, $\mathcal{Y}^{d}$, $\mathcal{Y}^{e}$,
$\mathcal{Y}^{\nu}$ in generation space; $\tilde\Phi$ is the conjugate doublet (hypercharge $-1/2$). In the vacuum they give the
quarks, the charged leptons and the neutrinos their Dirac masses (FE-46); with three right-handed neutrinos the neutrino masses
are Dirac masses and the lepton mixing is that of the PMNS matrix. No Majorana mass of $\nu_{\mathrm{R}}$ is included (lepton
number is conserved). Status: STANDARD (with $\nu_{\mathrm{R}}$: accepted by the author, 2026-10-24 17:32).

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

The new interactions of UM-3 (INVENTED), the order of the author that the left-handed and the right-handed halves of
dirac16complex each couple to every Standard-Model field with its own coupling, and that only the left-handed half couples to
the Higgs doublet. $\Psi$ is the value of dirac16complex at the fold. Every term is a product of a gauge-invariant
Standard-Model operator and a Lorentz-tensor bilinear of one half $X$ of dirac16complex, so every term is invariant under
$SU(3)_C \times SU(2)_L \times U(1)_Y$ and under the Lorentz transformations of the fold; none changes the flavour of a quark or a
lepton (consistent with QCD and with the electroweak theory, DERIVED by construction):

* the Higgs portal: the scalar density $\bar\Psi P_{\mathrm{L}}\Psi$ of the left-handed half times $\Phi^\dagger\Phi$, with the
  coupling $c_\Phi$; the right-handed half has no Higgs coupling;
* the gauge-kinetic portals: the scalar density of each half times the gauge-invariant kinetic densities of the gluons, of the
  $W$ fields and of the $B$ field, with the six couplings $c^{G}_X$, $c^{W}_X$, $c^{B}_X$: they make the gauge couplings of
  the fold depend on the density of dirac16complex at the fold (FE-16 to FE-18) and couple the bound states of dirac16complex
  to gluons, photons and weak bosons;
* the dipole portal: the antisymmetric tensor $\mathcal{D}_X^{\mu\nu}$ of each half times the hypercharge field strength (the
  only Standard-Model field strength that is gauge invariant by itself), with the couplings $d_X$: an electric and magnetic
  dipole moment of dirac16complex with respect to the photon and the $Z$;
* the current portals: the convective current $j_X^\mu$ of each half (the only real vector current that joins a half with
  itself: $\bar\Psi\gamma^\mu P_X\Psi$ joins $\Psi_{\mathrm{L}}$ with $\Psi_{\mathrm{R}}$ and is not real, DERIVED, `um3_fields.py`,
  F1) times the fermion-number current $J_f^\mu$ of each kind $f$ of Standard-Model multiplet, with the twelve couplings
  $c^{f}_X$; $J_f^\mu$ sums over the three generations and over the gauge components, so the portal is flavour blind.

The 21 couplings are $c_\Phi$, $c^{G}_{\mathrm{L}}$, $c^{G}_{\mathrm{R}}$, $c^{W}_{\mathrm{L}}$, $c^{W}_{\mathrm{R}}$,
$c^{B}_{\mathrm{L}}$, $c^{B}_{\mathrm{R}}$, $d_{\mathrm{L}}$, $d_{\mathrm{R}}$ and $c^{f}_{\mathrm{L}}$, $c^{f}_{\mathrm{R}}$ for
$f = Q, u, d, \ell, e, \nu$. Every term is bilinear in $\Psi$: the action is invariant under a change of the phase of $\Psi$ by a constant
(the charge of dirac16complex is conserved, and its lightest state is stable), and baryon and lepton numbers are conserved.
Status: INVENTED.


# Gravity

## The Einstein-Lovelock equations in the bulk

$$
\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_N + \Lambda\,\delta^M_N
 = \kappa\big(\mathcal{T}_\Psi{}^M{}_N + \mathcal{T}_{\mathrm{stab}}{}^M{}_N\big)\qquad (\sigma \ne 0) \tag{FE-1}
$$
<!-- symbols: ip, alphaL, LovE, iM, iN, Lambda, delta, kappa, TPsi, Tstab, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-1).**

- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$ (the author writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-10H^2$. Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{stab}}{}^a{}_b$: The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric requires, found and named by Claude (Anthropic) on 2026-10-24. Unit: GeV$^8$. Status: DERIVED (the value), ASSUMED (a separate medium).
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

The variation of $S_{\mathrm{tot}}$ with respect to the metric, away from the fold. The left-hand side is the Lovelock tensor of
the author's theory; the right-hand side is $\kappa$ times the energy-momentum tensor of the fields of the bulk:
dirac16complex (FE-6) and the stabiliser (IN-7). With the energy-momentum tensor defined by
$\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_{\mathrm{matter}}/\delta g^{MN}$, the time-time component
$\mathcal{T}_{x_4x_4} = -\mathcal{T}^{x_4}{}_{x_4}$ is the energy density seen by an observer at rest. Status: AUTHOR (the
theory), STANDARD (the variation).

$$
\begin{aligned}
\mathcal{E}_{(p)}{}^M{}_N &= -\frac{1}{2^{p+1}}\,\delta^{MM_1N_1\cdots M_pN_p}_{NP_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p},\\
\mathcal{E}_{(1)}{}^M{}_N &= R^M{}_N - \frac12\,\delta^M_N\,R,\\
\mathcal{E}_{(2)}{}^M{}_N &= 2\big(R\,R^M{}_N - 2R^M{}_PR^P{}_N - 2R^{MP}{}_{NQ}R^Q{}_P + R^{MPQS}R_{NPQS}\big)
 - \frac12\,\delta^M_N\,\mathcal{L}_{(2)}
\end{aligned} \tag{FE-2}
$$
<!-- symbols: LovE, ip, iM, iN, delta, iP, iQ, Riemann, iS, LovL -->
<!-- begin generated symbol list -->
**Symbols in (FE-2).**

- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor (convention $[\nabla_P, \nabla_Q]V^M = R^M{}_{NPQ}V^N$), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $S$: A coordinate index of eight dimensions, running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric. For
$p = 1$ it is the Einstein tensor, for $p = 2$ the Gauss-Bonnet tensor (written out in the third line); the cubic tensor
$\mathcal{E}_{(3)}$ is the first line with $p = 3$. UM-3 evaluates the first line exactly by enumerating the non-zero frame
components of the curvature (`um3_lovelock.py`); the second and third lines are independent checks of it (DERIVED,
`um3_geometry.py`, G3: the Einstein tensor from the coordinate Ricci tensor and the explicit Gauss-Bonnet tensor at random
points agree with the first line). Status: STANDARD.

$$
\mathcal{E}_{(p)}{}^M{}_M = -\frac{8 - 2p}{2}\,\mathcal{L}_{(p)},\qquad \nabla_M\,\mathcal{E}_{(p)}{}^M{}_N = 0 \tag{FE-3}
$$
<!-- symbols: LovE, ip, iM, iN, LovL, nabla -->
<!-- begin generated symbol list -->
**Symbols in (FE-3).**

- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.

<!-- end generated symbol list -->

Two identities of every Lovelock tensor in eight dimensions: its trace is a multiple of the Lovelock density, and its covariant
divergence vanishes (the contracted Bianchi identity). The second makes the energy-momentum tensor of the sources conserved
(FE-11). Status: STANDARD (DERIVED for the author's metric with general $a_4(x_4)$, $b_4(x_4)$: `um3_geometry.py`, G3).

## The junction conditions at the fold

$$
\begin{aligned}
&\kappa\,\mathcal{S}^a{}_b = \lim_{\varepsilon\to0}\int_{-\varepsilon}^{\varepsilon}\mathrm{d}\sigma\,
 \sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b
 = \mathfrak{F}^a{}_b\big\vert_{\sigma=0^+} - \mathfrak{F}^a{}_b\big\vert_{\sigma=0^-},\\
&\frac{\partial\mathfrak{F}^a{}_b}{\partial(\partial_\sigma\mathfrak{f})}
 = \frac{\partial}{\partial(\partial_\sigma^2\mathfrak{f})}\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b,
 \qquad \mathfrak{f} \in \{\mathfrak{a}, \mathfrak{b}, \mathfrak{n}\}
\end{aligned} \tag{FE-4}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, varepsilon, diff, sigma, ip, alphaL, LovE, Fpot, partial, isigma, fwarp, awarp, bwarp, nwarp -->
<!-- begin generated symbol list -->
**Symbols in (FE-4).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\varepsilon$: The half-thickness of a layer around the fold, taken to zero. Unit: length. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\mathfrak{F}^a{}_b$: The junction potential: a function of the first $\sigma$-derivatives of the metric functions whose derivatives are the coefficients of the second $\sigma$-derivatives in $\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FE-4). Unit: GeV. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $\mathfrak{f}$: Any one of the three metric functions $\mathfrak{a}, \mathfrak{b}, \mathfrak{n}$ of the general warped metric (FE-34). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{a},\ \mathfrak{a}_1$: The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{b},\ \mathfrak{b}_1$: The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{n},\ \mathfrak{n}_1$: The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The field equations at the fold. The author's metric (FE-27) has a kink at $\sigma = 0$; in general (FE-34) the metric functions
$\mathfrak{a}, \mathfrak{b}, \mathfrak{n}$ have first $\sigma$-derivatives that jump at the fold, so their second derivatives
contain $\delta_{\mathrm{D}}(\sigma)$. Because every Lovelock tensor is linear in the second $\sigma$-derivatives (quasi-linearity,
DERIVED for the general metric: `um3_fold.py`, J3), FE-1 extended across the fold reads
$\sum_p\alpha_{(p)}\mathcal{E}_{(p)} + \Lambda = \kappa(\mathcal{T}_{\mathrm{bulk}} + \mathcal{S}\,\delta_{\mathrm{D}}(\sigma))$: the
fold carries the thin source $\mathcal{S}^a{}_b$ (energy per unit area of the fold; $a, b$ along the fold), equal to the
integral of the Lovelock tensor across the fold. The coefficients of the second derivatives form an exact differential of the
first derivatives (DERIVED, J4), with the potential $\mathfrak{F}^a{}_b$; the integral is therefore the difference of
$\mathfrak{F}$ on the two sides. The $(\sigma, \sigma)$ and $(\sigma, x_4)$ components contain no second $\sigma$-derivative: they
carry no thin part and hold on each side separately. Status: DERIVED.

$$
\mathcal{S}^a{}_b = \frac{1}{V_*}\Big(\mathcal{T}_{\mathrm{H}}{}^a{}_b + \mathcal{T}_{\mathrm{gauge}}{}^a{}_b + \mathcal{T}_{\mathrm{f}}{}^a{}_b
 + \mathcal{T}_{\mathrm{P}}{}^a{}_b + \mathcal{T}_{\mathrm{ff}}{}^a{}_b + \mathcal{T}_{\mathrm{IG}}{}^a{}_b\Big),\qquad
\mathcal{T}_{\mathrm{IG}}{}^\mu{}_\nu = -\frac{1}{\kappa_4}\,\hat G^\mu{}_\nu,\qquad
\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}} \tag{FE-5}
$$
<!-- symbols: Sfoldsrc, ia, ib, Vstar, TH, Tgauge, Tf, TP, Tff, TIG, imu, inu, kappa4, Ghat, ir, Tany, Lfold -->
<!-- begin generated symbol list -->
**Symbols in (FE-5).**

- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{T}_{\mathrm{H}}$: The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{gauge}}$: The energy-momentum tensor of the gauge fields. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{f}}$: The energy-momentum tensor of the quarks and leptons. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{P}}$: The energy-momentum tensor of the portals of dirac16complex. Unit: GeV$^4$. Status: DERIVED.
- $\mathcal{T}_{\mathrm{ff}}{}^a{}_b$: The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation). Unit: GeV$^4$. Status: ASSUMED.
- $\mathcal{T}_{\mathrm{IG}}$: The energy-momentum tensor of the induced gravity of the fold, $\mathcal{T}_{\mathrm{IG}}{}^\mu{}_\nu = -\hat G^\mu{}_\nu/\kappa_4$. Unit: GeV$^4$. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\kappa_4$: The coupling of the induced gravity of the fold, $\kappa_4 = 8\pi G_{\mathrm{ind}}$; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_4/(1 + 5\epsilon_{\mathrm{r}}/6)$ (the Friedmann equation of the fold to first order in $\epsilon_{\mathrm{r}}$). Unit: GeV$^{-2}$. Value: $\kappa_4 \simeq 8\pi G_{\mathrm{N}} = 8\pi/M_{\mathrm{Pl}}^2$. Status: ASSUMED.
- $\hat G^\mu{}_\nu$: The Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold. Unit: 1/length$^2$. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->

The thin source of the fold is the energy-momentum tensor of everything that lives on the fold, divided by $V_*$ (IN-8): the
Higgs doublet (FE-7), the gauge fields (FE-8), the quarks and leptons (FE-9), the portals (FE-10), the fold fluid (IN-10) and
the induced gravity, whose energy-momentum tensor is $-1/\kappa_4$ times the Einstein tensor $\hat G^\mu{}_\nu$ of the metric of
the fold. Because the fields of the fold do not depend on the extra times and have no components along them, the extra times
enter only through $\sqrt{\lvert g\rvert}$: for every term of the fold the component along an extra time is the Lagrangian of
the term, $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$ (DERIVED: $\delta\sqrt{\lvert g\rvert} = -\frac12\sqrt{\lvert g\rvert}g_{rr}\delta g^{rr}$).
Combining FE-4 and FE-5 gives the Einstein equations of the fold (FE-59). Status: DERIVED.

## The energy-momentum tensors

$$
{\mathcal{T}_\Psi}_{MN} = -\frac14\Big(\bar\Psi\gamma_MD_N\Psi + \bar\Psi\gamma_ND_M\Psi - (D_M\bar\Psi)\gamma_N\Psi
 - (D_N\bar\Psi)\gamma_M\Psi\Big) + g_{MN}\,\mathcal{L}_\Psi \tag{FE-6}
$$
<!-- symbols: TPsi, iM, iN, Psi, gammaM, Dcov, metric, LPsi -->
<!-- begin generated symbol list -->
**Symbols in (FE-6).**

- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\mathcal{L}_\Psi$: The Lagrangian of dirac16complex, the square bracket of IN-4. Unit: GeV$^8$. Status: RECORD.

<!-- end generated symbol list -->

The symmetric energy-momentum tensor of dirac16complex, from the variation of the vielbein in IN-4 ($\mathcal{L}_\Psi$ is the
Lagrangian in the square bracket of IN-4; the variation of the spin connection adds only the divergence of the spin current,
which drops out of the symmetric part). On solutions of FE-12, $\mathcal{L}_\Psi = \frac{\lambda_\Psi}{2}(\bar\Psi\Psi)^2$. For a
stationary state $\Psi \propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ of the free field the energy density is
$\mathcal{T}_{\Psi\,x_4x_4} = -\omega\,\mathrm{i}\bar\Psi\gamma^{x_4}\Psi$: its sign is the product of the sign of the frequency
and of the Krein density (FE-43). Status: STANDARD (DERIVED for the energy density).

$$
{\mathcal{T}_{\mathrm{H}}}_{\mu\nu} = (D_\mu\Phi)^\dagger D_\nu\Phi + (D_\nu\Phi)^\dagger D_\mu\Phi + \hat h_{\mu\nu}\,\mathcal{L}_{\mathrm{H}} \tag{FE-7}
$$
<!-- symbols: TH, imu, inu, Dcov, Phi, dagger, hhat, LH -->
<!-- begin generated symbol list -->
**Symbols in (FE-7).**

- $\mathcal{T}_{\mathrm{H}}$: The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.

<!-- end generated symbol list -->

The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation): its time-time component is
$\lvert D_4\Phi\rvert^2 + \hat h^{ij}(D_i\Phi)^\dagger D_j\Phi + V \ge V$. Status: STANDARD.

$$
{\mathcal{T}_{\mathrm{gauge}}}_{\mu\nu} = G^A_{\mu\rho}G^A{}_\nu{}^\rho + W^I_{\mu\rho}W^I{}_\nu{}^\rho + B_{\mu\rho}B_\nu{}^\rho
 + \hat h_{\mu\nu}\,\mathcal{L}_{\mathrm{gauge}} \tag{FE-8}
$$
<!-- symbols: Tgauge, imu, inu, Ggluon, iA, irho, Wsu2, iI, Bhyp, hhat, Lgauge -->
<!-- begin generated symbol list -->
**Symbols in (FE-8).**

- $\mathcal{T}_{\mathrm{gauge}}$: The energy-momentum tensor of the gauge fields. Unit: GeV$^4$. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $\rho$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold. Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->

The energy-momentum tensor of the gauge fields; for each field its energy density is $(\vec E^2 + \vec B^2)/2$ in terms of the
electric and magnetic components. Status: STANDARD.

$$
{\mathcal{T}_{\mathrm{f}}}_{\mu\nu} = -\frac{\mathrm{i}}{4}\sum_\psi\Big(\bar\psi\hat\gamma_\mu D_\nu\psi + \bar\psi\hat\gamma_\nu D_\mu\psi
 - (D_\mu\bar\psi)\hat\gamma_\nu\psi - (D_\nu\bar\psi)\hat\gamma_\mu\psi\Big) + \hat h_{\mu\nu}\big(\mathcal{L}_{\mathrm{f}} + \mathcal{L}_{\mathrm{Y}}\big) \tag{FE-9}
$$
<!-- symbols: Tf, imu, inu, imag, ipsi, psiSM, gammahat, Dcov, hhat, Lf, LY -->
<!-- begin generated symbol list -->
**Symbols in (FE-9).**

- $\mathcal{T}_{\mathrm{f}}$: The energy-momentum tensor of the quarks and leptons. Unit: GeV$^4$. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\psi$: The label of a Standard-Model fermion field in a sum: $\psi$ runs over $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$. Status: STANDARD.
- $\psi,\ \bar\psi$: A Standard-Model fermion field (a four-dimensional Weyl field of the fold with three generations, written as a four-component spinor of fixed chirality); $\bar\psi = \psi^\dagger\beta$; $\psi_f$ the fields of the kind $f$. Unit: GeV$^{3/2}$. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->

The energy-momentum tensor of the quarks and leptons (with the kinetic term in its symmetric form). For a free particle of
energy $E$ at rest in the frame of the fold its time-time component is $E\,\psi^\dagger\psi > 0$. Status: STANDARD.

$$
\begin{aligned}
{\mathcal{T}_{\mathrm{P}}}_{\mu\nu} = {}&\sum_X\Big[\big(c^{G}_X\,G^A_{\mu\rho}G^A{}_\nu{}^\rho + c^{W}_X\,W^I_{\mu\rho}W^I{}_\nu{}^\rho
 + c^{B}_X\,B_{\mu\rho}B_\nu{}^\rho\big)\,\bar\Psi P_X\Psi\\
&+ \frac{d_X}{2}\big(B_{\mu\rho}\,\mathcal{D}_{X\nu}{}^\rho + B_{\nu\rho}\,\mathcal{D}_{X\mu}{}^\rho\big)
 + \sum_f\frac{c^{f}_X}{2}\big(J_{f\mu}\,j_{X\nu} + J_{f\nu}\,j_{X\mu}\big)\Big] + \hat h_{\mu\nu}\,\mathcal{L}_{\mathrm{P}}
\end{aligned} \tag{FE-10}
$$
<!-- symbols: TP, imu, inu, iX, cG, Ggluon, iA, irho, cW, Wsu2, iI, cB, Bhyp, Psi, PX, ddip, Ddip, if, cf, Jcur, jcur, hhat, LP -->
<!-- begin generated symbol list -->
**Symbols in (FE-10).**

- $\mathcal{T}_{\mathrm{P}}$: The energy-momentum tensor of the portals of dirac16complex. Unit: GeV$^4$. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $\rho$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_X$: The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$. Unit: dimensionless. Status: AUTHOR.
- $d_X$: The dipole-portal coupling of the half $X$ of dirac16complex with the hypercharge field strength. Unit: GeV$^{-5}$. Status: INVENTED.
- $\mathcal{D}_X^{\mu\nu}$: The dipole (antisymmetric tensor) density of the half $X$ of dirac16complex at the fold, $\mathcal{D}_X^{\mu\nu} = \mathrm{i}\bar\Psi\Sigma^{\mu\nu}P_X\Psi$ (real, DERIVED). Unit: GeV$^7$. Status: DERIVED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $J_f^\mu$: The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the currents that are the sources of the gauge fields. Unit: GeV$^3$. Status: STANDARD.
- $j_X^\mu$: The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED). Unit: GeV$^8$. Status: DERIVED.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->

The energy-momentum tensor of the portals (from the variation of IN-16 with respect to the metric of the fold, which enters
through the raised indices, through $\hat\gamma^\mu$ in $J_f^\mu$ and through $\sqrt{-\hat h}$); the Higgs portal enters only
through $\hat h_{\mu\nu}\mathcal{L}_{\mathrm{P}}$. It is a source of the fold. Status: DERIVED.

## The conservation laws

$$
\begin{aligned}
&\nabla_M\big(\mathcal{T}_\Psi{}^M{}_N + \mathcal{T}_{\mathrm{stab}}{}^M{}_N\big) = 0\qquad (\sigma \ne 0),\\
&\hat\nabla_a\,\mathcal{S}^a{}_b = -\Big(\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b\big\vert_{\sigma=0^+}
 - \mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b\big\vert_{\sigma=0^-}\Big)
\end{aligned} \tag{FE-11}
$$
<!-- symbols: nabla, TPsi, Tstab, iM, iN, sigma, nablahat, Sfoldsrc, ia, ib, Tbulk -->
<!-- begin generated symbol list -->
**Symbols in (FE-11).**

- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{stab}}{}^a{}_b$: The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric requires, found and named by Claude (Anthropic) on 2026-10-24. Unit: GeV$^8$. Status: DERIVED (the value), ASSUMED (a separate medium).
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\hat\nabla$: The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold (for four-dimensional tensors of its metric $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the observable coordinates $x_1, \dots, x_4$; for $\hat\nabla_a\mathcal{S}^a{}_b$ of the induced metric of the seven-dimensional fold). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.

<!-- end generated symbol list -->

The energy and momentum of the bulk are conserved away from the fold (FE-3 and FE-1). At the fold the thin source exchanges
energy and momentum with the bulk: its covariant divergence along the fold equals minus the jump of the flux
$\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ of the bulk sources along $\sigma$ (the frame component $(0), b$). For the author's
metric with general $a_4(x_4)$, $b_4(x_4)$ this is an identity of the junction formula FE-30 and the bulk equation FE-29
(DERIVED, `um3_fold.py`, J6). The fluxes of dirac16complex into the bulk carry its share of this exchange. Status: DERIVED.

# The matter fields

## dirac16complex

$$
\gamma^MD_M\Psi - m_\Psi\Psi - \lambda_\Psi\big(\bar\Psi\Psi\big)\Psi = 0\qquad (\sigma \ne 0) \tag{FE-12}
$$
<!-- symbols: gammaM, iM, Dcov, Psi, mPsi, lamPsi, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-12).**

- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

The field equation of dirac16complex in the bulk: the variation of IN-4 with respect to $\bar\Psi$ (the second half of the
symmetric kinetic term, integrated by parts with $D_M\gamma^M = 0$, doubles the first). With the author's real matrices the
operator $\gamma^MD_M - m_\Psi$ is real: the field equation does not contain $\mathrm{i}$, and a real solution exists for every
complex one. Status: RECORD.

$$
\begin{aligned}
&\Psi\big\vert_{\sigma=0^+} = \exp\Big(\frac{1}{V_*}\,\gamma^{(0)}\,\mathbb{M}\Big)\,\Psi\big\vert_{\sigma=0^-},\\
&\mathbb{M} = c_\Phi\big(\Phi^\dagger\Phi\big)P_{\mathrm{L}} + \sum_X\Big[\frac14\big(c^{G}_X\,G^A_{\mu\nu}G^{A\mu\nu}
 + c^{W}_X\,W^I_{\mu\nu}W^{I\mu\nu} + c^{B}_X\,B_{\mu\nu}B^{\mu\nu}\big)P_X + \frac{d_X}{2}\,B_{\mu\nu}\,\mathrm{i}\Sigma^{\mu\nu}P_X\\
&\qquad\qquad + \sum_f c^{f}_X\big(2\mathrm{i}\,J_f^\mu P_XD_\mu + \mathrm{i}(\hat\nabla_\mu J_f^\mu)P_X\big)\Big]
\end{aligned} \tag{FE-13}
$$
<!-- symbols: Psi, sigma, Vstar, gammaM, Mfold, cPhi, Phi, dagger, PL, iX, cG, Ggluon, iA, imu, inu, cW, Wsu2, iI, cB, Bhyp, PX, ddip, imag, SigmaGen, if, cf, Jcur, Dcov, nablahat -->
<!-- begin generated symbol list -->
**Symbols in (FE-13).**

- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mathbb{M}$: The fold operator of dirac16complex: the $16 \times 16$ matrix (with a derivative along the fold) built from the Standard-Model fields at the fold by varying the portals with respect to $\bar\Psi$ (FE-13). Unit: GeV$^{-3}$ (so that $\mathbb{M}/V_*$ is dimensionless). Status: DERIVED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
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
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Sigma^{ab},\ \Sigma^{\mu\nu}$: The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold. Unit: dimensionless. Status: AUTHOR.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $J_f^\mu$: The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the currents that are the sources of the gauge fields. Unit: GeV$^3$. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\hat\nabla$: The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold (for four-dimensional tensors of its metric $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the observable coordinates $x_1, \dots, x_4$; for $\hat\nabla_a\mathcal{S}^a{}_b$ of the induced metric of the seven-dimensional fold). Status: STANDARD.

<!-- end generated symbol list -->

The equation of dirac16complex at the fold: the variation of the portals IN-16 with respect to $\bar\Psi$ adds
$-\delta_{\mathrm{D}}(\sigma)\,\mathbb{M}\Psi/V_*$ to FE-12. $\mathbb{M}$ is the fold operator, a $16 \times 16$ matrix (with a
derivative along the fold from the current portals) built from the Standard-Model fields at the fold. Integrating FE-12 with
this term across a fold of vanishing thickness gives the matching condition in the first line: the values of dirac16complex on
the two sides of the fold differ by the exponential of $\gamma^{(0)}\mathbb{M}/V_*$ (the exact solution of
$\partial_\sigma\Psi = \gamma^{(0)}\mathbb{M}\,\delta_{\mathrm{D}}(\sigma)\Psi/V_*$ in a layer in which the fold term dominates;
$(\gamma^{(0)})^2 = \mathbf{1}$). The Higgs term acts on the left-handed half only. Status: DERIVED (from INVENTED terms).

$$
\gamma^M\Omega_M = -3H\,\mathrm{sgn}(\sigma)\,\gamma^{(0)} + \frac32\,\frac{b_4'}{b_4}\,\gamma^{(4)} \ne 0 \tag{FE-14}
$$
<!-- symbols: gammaM, iM, Omega, Hconst, sgn, sigma, b4, prime -->
<!-- begin generated symbol list -->
**Symbols in (FE-14).**

- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.

<!-- end generated symbol list -->

The coupling of dirac16complex to gravity through the canonical spin connection, for the author's metric: the contraction
$\gamma^M\Omega_M$ that enters the Dirac operator. The first term comes from the warp of the six directions $x_1, x_2, x_3, x_5,
x_6, x_7$ (each contributes $\frac12\partial_\sigma$ of the logarithm of its scale factor), the second from the time dependence of
their scale factors ($a_4$ cancels between ordinary space and the extra times). The first term never vanishes ($H > 0$, and it
only changes sign at the fold); the second is non-zero whenever $b_4$ depends on $x_4$, as the author requires. Hence the
coupling of dirac16complex to gravity through the spin connection is never identically zero (DERIVED, `um3_geometry.py`, G5,
with the author's matrices; the vielbein postulate $D_M\gamma^N = 0$ holds, G5). For the general warped metric FE-34,
$\gamma^M\Omega_M = \frac12\partial_\sigma(3\mathfrak{a} + 3\mathfrak{b} + \mathfrak{n})\gamma^{(0)} + \frac12\mathrm{e}^{-\mathfrak{n}}\partial_{x_4}(3\mathfrak{a} + 3\mathfrak{b})\gamma^{(4)}$.
Status: DERIVED.

## The Higgs doublet

$$
\begin{aligned}
&\frac{1}{\sqrt{-\hat h}\,\mathcal{Z}}\,D_\mu\big(\sqrt{-\hat h}\,\mathcal{Z}\,\hat h^{\mu\nu}D_\nu\Phi\big) - \mu^2\Phi
 - 2\lambda\big(\Phi^\dagger\Phi\big)\Phi - c_\Phi\,\bar\Psi P_{\mathrm{L}}\Psi\,\Phi = \Theta,\\
&\Theta = \begin{pmatrix}\bar d_{\mathrm{R}}(\mathcal{Y}^{d})^\dagger u_{\mathrm{L}} + \bar e_{\mathrm{R}}(\mathcal{Y}^{e})^\dagger\nu_{\mathrm{L}}
 - \bar d_{\mathrm{L}}\mathcal{Y}^{u}u_{\mathrm{R}} - \bar e_{\mathrm{L}}\mathcal{Y}^{\nu}\nu_{\mathrm{R}}\\
 \bar d_{\mathrm{R}}(\mathcal{Y}^{d})^\dagger d_{\mathrm{L}} + \bar e_{\mathrm{R}}(\mathcal{Y}^{e})^\dagger e_{\mathrm{L}}
 + \bar u_{\mathrm{L}}\mathcal{Y}^{u}u_{\mathrm{R}} + \bar\nu_{\mathrm{L}}\mathcal{Y}^{\nu}\nu_{\mathrm{R}}\end{pmatrix}
\end{aligned} \tag{FE-15}
$$
<!-- symbols: hhat, Zfold, Dcov, imu, inu, Phi, muH, lamH, dagger, cPhi, Psi, PL, Theta, dR, Yuk, uL, eR, nuL, dL, uR, nuR, eL -->
<!-- begin generated symbol list -->
**Symbols in (FE-15).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $\mu^2$: The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$). Unit: GeV$^2$. Value: $\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\Theta$: The Yukawa source of the Higgs equation, $\Theta = -\partial\mathcal{L}_{\mathrm{Y}}/\partial\Phi^\dagger$ (a doublet of fermion bilinears). Unit: GeV$^3$. Status: STANDARD.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $u_{\mathrm{L}}$: The upper (up-type, left-handed) components of the quark doublets. Unit: GeV$^{3/2}$. Status: STANDARD.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\nu_{\mathrm{L}}$: The upper (neutral, left-handed) components of the lepton doublets: the left-handed neutrinos. Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{L}}$: The lower (down-type, left-handed) components of the quark doublets. Unit: GeV$^{3/2}$. Status: STANDARD.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $e_{\mathrm{L}}$: The lower (charged, left-handed) components of the lepton doublets. Unit: GeV$^{3/2}$. Status: STANDARD.

<!-- end generated symbol list -->

The field equation of the Higgs doublet on the fold: the variation of IN-11, IN-15 and IN-16 with respect to $\Phi^\dagger$. The
factor $\mathcal{Z}$ (IN-8) is 1 in the late universe. The Higgs portal adds the term $-c_\Phi\bar\Psi P_{\mathrm{L}}\Psi\,\Phi$: the
scalar density of the left-handed half of dirac16complex at the fold shifts the mass parameter of the Higgs field. $\Theta$ is
the Yukawa source, $-\partial\mathcal{L}_{\mathrm{Y}}/\partial\Phi^\dagger$, written with the components
$Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ and $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ of the doublets (generation indices
contracted with the Yukawa matrices). Status: STANDARD (AUTHOR potential; INVENTED portal term).

## The gauge fields

$$
\begin{aligned}
&\frac{1}{\sqrt{-\hat h}\,\mathcal{Z}}\Big(\partial_\mu\big[\sqrt{-\hat h}\,\mathcal{Z}\,\mathcal{K}_{G}\,G^{A\mu\nu}\big]
 + g_3\,f^{ABC}G^B_\mu\,\sqrt{-\hat h}\,\mathcal{Z}\,\mathcal{K}_{G}\,G^{C\mu\nu}\Big) = -g_3\,J_{\mathrm{c}}^{A\nu},\qquad
 \mathcal{K}_{G} = 1 + \sum_X c^{G}_X\,\bar\Psi P_X\Psi,\\
&J_{\mathrm{c}}^{A\nu} = \bar Q\,\hat\gamma^\nu t^AQ + \bar u_{\mathrm{R}}\,\hat\gamma^\nu t^Au_{\mathrm{R}}
 + \bar d_{\mathrm{R}}\,\hat\gamma^\nu t^Ad_{\mathrm{R}}
\end{aligned} \tag{FE-16}
$$
<!-- symbols: hhat, Zfold, partial, imu, Kport, Ggluon, iA, inu, g3, fabc, iB, iC, Jcolour, iX, cG, Psi, PX, Qdoub, gammahat, tgen, uR, dR -->
<!-- begin generated symbol list -->
**Symbols in (FE-16).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\mathcal{K}_{G},\ \mathcal{K}_{W},\ \mathcal{K}_{B}$: The portal factors of the gauge kinetic terms, $\mathcal{K}_{G} = 1 + \sum_Xc^{G}_X\bar\Psi P_X\Psi$ (likewise for $W$ and $B$): the gauge couplings at the fold are divided by $\sqrt{\mathcal{K}}$. Unit: dimensionless. Value: 1 where dirac16complex vanishes. Status: DERIVED.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling (the strong coupling $g_s$). Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($\alpha_s = 0.1180$). Status: STANDARD.
- $f^{ABC}$: The structure constants of $SU(3)$, $[t^A, t^B] = \mathrm{i}f^{ABC}t^C$. Unit: dimensionless. Status: STANDARD.
- $B$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $C$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $J_{\mathrm{c}}^{A\nu}$: The colour current of the quarks. Unit: GeV$^3$. Status: STANDARD.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_X$: The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$. Unit: dimensionless. Status: AUTHOR.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $t^A$: The generators of $SU(3)$ on colour triplets, $t^A = \lambda_{\mathrm{GM}}^A/2$ (the Gell-Mann matrices halved), $\mathrm{tr}(t^At^B) = \delta^{AB}/2$. Unit: dimensionless. Status: STANDARD.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.

<!-- end generated symbol list -->

The Yang-Mills equation of the gluons (with the convention of the signature $(+,+,+,-)$: $\nabla_\mu F^{\mu\nu} = -J^\nu$ for a
Lagrangian $-\frac14F^2 + A_\mu J^\mu$). The gluon-kinetic portals multiply the gluon kinetic term by
$\mathcal{K}_{G}$: the strong coupling at the fold is $g_3/\sqrt{\mathcal{K}_{G}}$ where dirac16complex is dense. The colour
current $J_{\mathrm{c}}^{A\nu}$ of the quarks is the source. Status: STANDARD (INVENTED portal factor).

$$
\begin{aligned}
&\frac{1}{\sqrt{-\hat h}\,\mathcal{Z}}\Big(\partial_\mu\big[\sqrt{-\hat h}\,\mathcal{Z}\,\mathcal{K}_{W}\,W^{I\mu\nu}\big]
 + g_2\,\epsilon^{IJK}W^J_\mu\,\sqrt{-\hat h}\,\mathcal{Z}\,\mathcal{K}_{W}\,W^{K\mu\nu}\Big)
 = -g_2\big(J_{\mathrm{w}}^{I\nu} + J_\Phi^{I\nu}\big),\\
&\mathcal{K}_{W} = 1 + \sum_X c^{W}_X\,\bar\Psi P_X\Psi,\qquad J_{\mathrm{w}}^{I\nu} = \bar Q\,\hat\gamma^\nu\frac{\tau^I}{2}Q + \bar\ell\,\hat\gamma^\nu\frac{\tau^I}{2}\ell,\qquad
 J_\Phi^{I\nu} = \mathrm{i}\Big[(D^\nu\Phi)^\dagger\frac{\tau^I}{2}\Phi - \Phi^\dagger\frac{\tau^I}{2}D^\nu\Phi\Big]
\end{aligned} \tag{FE-17}
$$
<!-- symbols: hhat, Zfold, partial, imu, Kport, Wsu2, iI, inu, g2, epsLC, iJ, iK, Jweak, JPhi, iX, cW, Psi, PX, Qdoub, gammahat, taupauli, ell, imag, Dcov, Phi, dagger -->
<!-- begin generated symbol list -->
**Symbols in (FE-17).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\mathcal{K}_{G},\ \mathcal{K}_{W},\ \mathcal{K}_{B}$: The portal factors of the gauge kinetic terms, $\mathcal{K}_{G} = 1 + \sum_Xc^{G}_X\bar\Psi P_X\Psi$ (likewise for $W$ and $B$): the gauge couplings at the fold are divided by $\sqrt{\mathcal{K}}$. Unit: dimensionless. Value: 1 where dirac16complex vanishes. Status: DERIVED.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $\epsilon^{IJK}$: The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$. Unit: dimensionless. Status: STANDARD.
- $J$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.
- $K$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.
- $J_{\mathrm{w}}^{I\nu}$: The weak-isospin current of the left-handed fermion doublets. Unit: GeV$^3$. Status: STANDARD.
- $J_\Phi^{I\nu}$: The weak-isospin current of the Higgs doublet (it contains the mass terms of the $W$ fields); $J_\Phi^{2\,x_4}$ its isospin charge density with $I = 2$. Unit: GeV$^3$. Status: STANDARD.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_X$: The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$. Unit: dimensionless. Status: AUTHOR.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square). Unit: dimensionless. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.

<!-- end generated symbol list -->

The Yang-Mills equation of the $SU(2)_L$ fields. The sources are the weak-isospin current of the left-handed doublets and the
isospin current of the Higgs doublet (which contains the mass terms of the $W$ fields: in the vacuum
$J_\Phi^{I\nu} \ni -g_2(v^2 + \mathcal{A}^2)W^{I\nu}/4$, so that FE-17 becomes $\nabla_\mu W^{I\mu\nu} = m_{\mathrm{W}}^2W^{I\nu} + \dots$). Status: STANDARD (INVENTED portal factor).

$$
\begin{aligned}
&\frac{1}{\sqrt{-\hat h}\,\mathcal{Z}}\,\partial_\mu\Big[\sqrt{-\hat h}\,\mathcal{Z}\Big(\mathcal{K}_{B}\,B^{\mu\nu}
 + \sum_X d_X\,\mathcal{D}_X^{\mu\nu}\Big)\Big] = -g_1\,J_Y^\nu,\qquad \mathcal{K}_{B} = 1 + \sum_X c^{B}_X\,\bar\Psi P_X\Psi,\\
&J_Y^\nu = \sum_\psi Y_\psi\,\bar\psi\,\hat\gamma^\nu\psi + \frac{\mathrm{i}}{2}\big[(D^\nu\Phi)^\dagger\Phi - \Phi^\dagger D^\nu\Phi\big]
\end{aligned} \tag{FE-18}
$$
<!-- symbols: hhat, Zfold, partial, imu, Kport, Bhyp, inu, iX, ddip, Ddip, g1, JY, cB, Psi, PX, ipsi, Yhyp, psiSM, gammahat, imag, Dcov, Phi, dagger -->
<!-- begin generated symbol list -->
**Symbols in (FE-18).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\mathcal{K}_{G},\ \mathcal{K}_{W},\ \mathcal{K}_{B}$: The portal factors of the gauge kinetic terms, $\mathcal{K}_{G} = 1 + \sum_Xc^{G}_X\bar\Psi P_X\Psi$ (likewise for $W$ and $B$): the gauge couplings at the fold are divided by $\sqrt{\mathcal{K}}$. Unit: dimensionless. Value: 1 where dirac16complex vanishes. Status: DERIVED.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $d_X$: The dipole-portal coupling of the half $X$ of dirac16complex with the hypercharge field strength. Unit: GeV$^{-5}$. Status: INVENTED.
- $\mathcal{D}_X^{\mu\nu}$: The dipole (antisymmetric tensor) density of the half $X$ of dirac16complex at the fold, $\mathcal{D}_X^{\mu\nu} = \mathrm{i}\bar\Psi\Sigma^{\mu\nu}P_X\Psi$ (real, DERIVED). Unit: GeV$^7$. Status: DERIVED.
- $g_1$: The $U(1)_Y$ gauge coupling (usually $g'$; not normalised for grand unification). Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $J_Y^\nu$: The hypercharge current of the fermions and of the Higgs doublet. Unit: GeV$^3$. Status: STANDARD.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_X$: The chiral projector of the half $X$: $P_X = P_{\mathrm{L}}$ for $X = \mathrm{L}$, $P_{\mathrm{R}}$ for $X = \mathrm{R}$. Unit: dimensionless. Status: AUTHOR.
- $\psi$: The label of a Standard-Model fermion field in a sum: $\psi$ runs over $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$. Status: STANDARD.
- $Y_f$: The hypercharge of a field, the charge of its coupling $g_1Y_fB_\mu$ to the hypercharge field in the covariant derivative ($1/6$, $2/3$, $-1/3$, $-1/2$, $-1$, $0$ for $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$, $1/2$ for $\Phi$). Unit: dimensionless. Status: STANDARD.
- $\psi,\ \bar\psi$: A Standard-Model fermion field (a four-dimensional Weyl field of the fold with three generations, written as a four-component spinor of fixed chirality); $\bar\psi = \psi^\dagger\beta$; $\psi_f$ the fields of the kind $f$. Unit: GeV$^{3/2}$. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.

<!-- end generated symbol list -->

The Maxwell equation of the hypercharge field. The dipole portal adds the dipole density of dirac16complex to the field strength,
as a polarisation adds to the electric field in a medium: dirac16complex at the fold carries electric and magnetic dipole
moments. The source is the hypercharge current of the fermions and of the Higgs doublet. Status: STANDARD (INVENTED portal
terms).

## The quarks and leptons

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{Q}_\mu\big)Q = \mathcal{Y}^{u}\tilde\Phi\,u_{\mathrm{R}}
 + \mathcal{Y}^{d}\Phi\,d_{\mathrm{R}},\qquad \mathcal{V}^{f}_\mu = \sum_X c^{f}_X\,j_{X\mu} \tag{FE-19}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, Qdoub, Yuk, Phitilde, uR, Phi, dR, iX, cf, jcur, if -->
<!-- begin generated symbol list -->
**Symbols in (FE-19).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $j_X^\mu$: The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED). Unit: GeV$^8$. Status: DERIVED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.

<!-- end generated symbol list -->

The Dirac equation of the quark doublets: the variation of IN-14, IN-15 and IN-16 with respect to $\bar Q$. The current portals
act on every Standard-Model fermion of kind $f$ as a vector potential $\mathcal{V}^{f}_\mu$ built from the convective currents
of the two halves of dirac16complex at the fold; it is the same for the three generations (flavour blind). Status: STANDARD
(INVENTED potential).

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{u}_\mu\big)u_{\mathrm{R}} = (\mathcal{Y}^{u})^\dagger\tilde\Phi^\dagger Q \tag{FE-20}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, uR, Yuk, dagger, Phitilde, Qdoub -->
<!-- begin generated symbol list -->
**Symbols in (FE-20).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{d}_\mu\big)d_{\mathrm{R}} = (\mathcal{Y}^{d})^\dagger\Phi^\dagger Q \tag{FE-21}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, dR, Yuk, dagger, Phi, Qdoub -->
<!-- begin generated symbol list -->
**Symbols in (FE-21).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{\ell}_\mu\big)\ell = \mathcal{Y}^{e}\Phi\,e_{\mathrm{R}}
 + \mathcal{Y}^{\nu}\tilde\Phi\,\nu_{\mathrm{R}} \tag{FE-22}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, ell, Yuk, Phi, eR, Phitilde, nuR -->
<!-- begin generated symbol list -->
**Symbols in (FE-22).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.

<!-- end generated symbol list -->

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{e}_\mu\big)e_{\mathrm{R}} = (\mathcal{Y}^{e})^\dagger\Phi^\dagger\ell \tag{FE-23}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, eR, Yuk, dagger, Phi, ell -->
<!-- begin generated symbol list -->
**Symbols in (FE-23).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

$$
\mathrm{i}\hat\gamma^\mu\big(D_\mu + \mathrm{i}\,\mathcal{V}^{\nu}_\mu\big)\nu_{\mathrm{R}} = (\mathcal{Y}^{\nu})^\dagger\tilde\Phi^\dagger\ell \tag{FE-24}
$$
<!-- symbols: imag, gammahat, imu, Dcov, Vport, nuR, Yuk, dagger, Phitilde, ell -->
<!-- begin generated symbol list -->
**Symbols in (FE-24).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

The Dirac equations of the up-quark singlets, the down-quark singlets, the lepton doublets, the charged-lepton singlets and the
right-handed neutrinos (FE-20 to FE-24), each the variation of IN-14, IN-15 and IN-16 with respect to the conjugate field. Each
fermion sees the gauge fields (in $D_\mu$), the Higgs doublet (through the Yukawa matrices) and dirac16complex (through
$\mathcal{V}^{f}_\mu$). The right-handed neutrinos see no gauge field; they couple to the Standard Model only through the
neutrino Yukawa matrix, which gives the neutrinos their Dirac masses. Status: STANDARD (INVENTED potentials).

$$
\begin{aligned}
\hat\nabla_\mu J_{\ell}^\mu &= -\hat\nabla_\mu\big(J_{e}^\mu + J_{\nu}^\mu\big)
 = -\mathrm{i}\big(\bar\ell\,\mathcal{Y}^{e}\Phi\,e_{\mathrm{R}} + \bar\ell\,\mathcal{Y}^{\nu}\tilde\Phi\,\nu_{\mathrm{R}}\big) + \mathrm{h.c.},\\
\hat\nabla_\mu J_{Q}^\mu &= -\hat\nabla_\mu\big(J_{u}^\mu + J_{d}^\mu\big)
 = -\mathrm{i}\big(\bar Q\,\mathcal{Y}^{u}\tilde\Phi\,u_{\mathrm{R}} + \bar Q\,\mathcal{Y}^{d}\Phi\,d_{\mathrm{R}}\big) + \mathrm{h.c.}
\end{aligned} \tag{FE-25}
$$
<!-- symbols: nablahat, imu, Jcur, imag, ell, Yuk, Phi, eR, Phitilde, nuR, hc, Qdoub, uR, dR -->
<!-- begin generated symbol list -->
**Symbols in (FE-25).**

- $\hat\nabla$: The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold (for four-dimensional tensors of its metric $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the observable coordinates $x_1, \dots, x_4$; for $\hat\nabla_a\mathcal{S}^a{}_b$ of the induced metric of the seven-dimensional fold). Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $J_f^\mu$: The fermion-number current of the Standard-Model multiplets of kind $f$, $J_f^\mu = \bar\psi_f\hat\gamma^\mu\psi_f$ summed over the three generations and the gauge components; with other labels the currents that are the sources of the gauge fields. Unit: GeV$^3$. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\tilde\Phi$: The conjugate Higgs doublet, $\tilde\Phi = \mathrm{i}\tau^2\Phi^*$ (hypercharge $-1/2$). Unit: GeV. Status: STANDARD.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\mathrm{h.c.}$: The Hermitian conjugate of the preceding terms. Status: STANDARD.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $u_{\mathrm{R}}$: The right-handed up-type quarks $u, c, t$ (singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{R}}$: The right-handed down-type quarks $d, s, b$ (hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.

<!-- end generated symbol list -->

The divergences of the fermion-number currents of the six kinds of multiplets (DERIVED from FE-19 to FE-24): the Yukawa couplings
turn doublets into singlets, so the current of each kind is not conserved by itself, while the lepton number
$J_\ell + J_e + J_\nu$ and the baryon number $(J_Q + J_u + J_d)/3$ are conserved. The divergences enter the fold operator
$\mathbb{M}$ (FE-13). Status: DERIVED.

## The ad hoc Higgs vacuum

$$
\begin{aligned}
&\mathcal{R}_{\mathcal{A}} = \mathcal{A}'' + 3\frac{b_4'}{b_4}\mathcal{A}' + \lambda\mathcal{A}^3 + c_\Phi\,\bar\Psi P_{\mathrm{L}}\Psi\,\mathcal{A}
 = \Big(4a_{40}^2 - 6a_{40}\frac{b_4'}{b_4}\Big)\mathcal{A} + \lambda\mathcal{A}^3 + c_\Phi\,\bar\Psi P_{\mathrm{L}}\Psi\,\mathcal{A},\\
&\mathcal{R}_v = \lambda\mathcal{A}^2v + c_\Phi\,\bar\Psi P_{\mathrm{L}}\Psi\,v,\qquad
 J_\Phi^{2\,x_4} = a_{40}\,v\,\mathcal{A},\qquad J_\Phi^{1\,x_4} = J_\Phi^{3\,x_4} = 0
\end{aligned} \tag{FE-26}
$$
<!-- symbols: Rres, Aadhoc, prime, b4, lamH, cPhi, Psi, PL, a40, vev, JPhi, x4 -->
<!-- begin generated symbol list -->
**Symbols in (FE-26).**

- $\mathcal{R}_{\mathcal{A}},\ \mathcal{R}_v$: The residuals of the ad hoc Higgs vacuum in the upper ($\mathcal{R}_{\mathcal{A}}$) and lower ($\mathcal{R}_v$) components of the Higgs equation: what the ad hoc vacuum leaves unbalanced. Unit: GeV$^3$. Status: DERIVED.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $a_{40}$: The decay constant of almightyAdHoc, $a_{40} > 0$: $\mathcal{A}$ falls by $\mathrm{e}$ in the time $1/(2a_{40})$. Unit: GeV (1/length). Status: AUTHOR.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $J_\Phi^{I\nu}$: The weak-isospin current of the Higgs doublet (it contains the mass terms of the $W$ fields); $J_\Phi^{2\,x_4}$ its isospin charge density with $I = 2$. Unit: GeV$^3$. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.

<!-- end generated symbol list -->

The author's ad hoc vacuum IN-12 inserted into the Higgs equation FE-15 (homogeneous fields, no gauge fields, the fold factor
$\mathcal{Z} \propto b_4^3\mathrm{e}^{-3a_4}$ so that the time derivative of $\sqrt{-\hat h}\mathcal{Z}$ gives $3b_4'/b_4$). The
upper and lower components of FE-15 are not satisfied: $\mathcal{R}_{\mathcal{A}}$ and $\mathcal{R}_v$ are what remains (the
residuals; FE-15 holds exactly if the source $\Theta$ is replaced by $\Theta - (\mathcal{R}_{\mathcal{A}}, \mathcal{R}_v)/\sqrt2$). The ad
hoc vacuum is an exact solution only in the limit $\mathcal{A} \to 0$. It also carries a weak-isospin charge density
$J_\Phi^{2\,x_4} = a_{40}v\mathcal{A}$ (the component along $x_4$ of the isospin current of FE-17 with $I = 2$), which the
$W^2$ equation FE-17 must balance with a background field $W^2_{x_4}$ (DERIVED, `um3_fields.py`, F5: the masses of the $W$ and
$Z$, the direction of the photon, the charge density, the residual of the upper component). Status: DERIVED.

# The background

The background is the author's metric with the two functions $a_4(x_4)$ and $b_4(x_4)$ of the time, on which every other field
moves; the matter fields correct it by the next terms of a power series (FE-35). This section writes out its geometry and the
exact equations that its two functions obey, in the bulk and at the fold.

## The author's metric and the proper chart

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

The author's metric of the primordial gravitational field (his order of 2026-10-24: the metric of
`Dirac_Einstein-Lovelock_4+4_Nash.nb` with $b_4 \to b_4^2$; $(\sin^2z)^{1/6}$ is the positive branch of `Sin[6 H x0]^(1/3)`,
the author's rule of 2026-10-16), and the same metric in the proper chart $\sigma$ of the hidden direction. In the author's
chart the metric is smooth but degenerate at the fold $z = \pi/2$ ($\cot z = 0$); the proper distance from the fold is
$\lvert\sigma\rvert$, and $\sigma$ runs from $-\infty$ (the tip $z \to 0$) through $0$ (the fold) to $+\infty$ (the tip
$z \to \pi$): one period of $x_0$ is the whole line, and the two halves of a period are mirror images under $z \to \pi - z$
($\sigma \to -\sigma$). Ordinary space and the extra times are warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$ (with a kink at the fold),
the time $x_4$ is not warped. $a_4$ and $b_4$ are functions of $x_4$; $b_4$ is never identically 1. Status: AUTHOR (the metric),
DERIVED (the chart, `um3_fold.py`, J1).

$$
\begin{aligned}
&\mathbf{e}^{(0)} = \mathrm{d}\sigma,\quad \mathbf{e}^{(i)} = \mathrm{e}^{a_4 - H\lvert\sigma\rvert}\mathrm{d}x_i,\quad
 \mathbf{e}^{(4)} = \mathrm{d}x_4,\quad \mathbf{e}^{(r)} = b_4\,\mathrm{e}^{-a_4 - H\lvert\sigma\rvert}\mathrm{d}x_r,\\
&\sqrt{\lvert g\rvert} = b_4^3\,\mathrm{e}^{-6H\lvert\sigma\rvert},\qquad
 \mathsf{A} = \frac{a_4'}{H},\qquad \mathsf{U} = \frac{b_4'}{Hb_4},\qquad \mathsf{A}_1 = \frac{\mathsf{A}'}{H},\qquad
 \mathsf{U}_1 = \frac{\mathsf{U}'}{H},\\
&R^{(0)(i)}{}_{(0)(i)} = R^{(0)(r)}{}_{(0)(r)} = -H^2,\qquad R^{(0)(4)}{}_{(0)(4)} = 0,\qquad
 R^{(i)(j)}{}_{(i)(j)} = (\mathsf{A}^2 - 1)H^2,\\
&R^{(i)(4)}{}_{(i)(4)} = (\mathsf{A}^2 + \mathsf{A}_1)H^2,\qquad
 R^{(i)(r)}{}_{(i)(r)} = -(1 + \mathsf{A}^2 - \mathsf{A}\mathsf{U})H^2,\\
&R^{(4)(r)}{}_{(4)(r)} = \big((\mathsf{U} - \mathsf{A})^2 + \mathsf{U}_1 - \mathsf{A}_1\big)H^2,\qquad
 R^{(r)(s)}{}_{(r)(s)} = \big((\mathsf{U} - \mathsf{A})^2 - 1\big)H^2,\\
&R^{(0)(i)}{}_{(4)(i)} = \mathrm{sgn}(\sigma)\,\mathsf{A}H^2,\qquad
 R^{(0)(r)}{}_{(4)(r)} = \mathrm{sgn}(\sigma)\,(\mathsf{U} - \mathsf{A})H^2
\end{aligned} \tag{FE-28}
$$
<!-- symbols: vielbein, diff, sigma, euler, a4, Hconst, xfour, ii, x4, b4, ir, metric, Asf, Usf, A1sf, U1sf, prime, Riemann, ij, is, sgn -->
<!-- begin generated symbol list -->
**Symbols in (FE-28).**

- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x$: The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor (convention $[\nabla_P, \nabla_Q]V^M = R^M{}_{NPQ}V^N$), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $j$: A second generation or mass-state index (as $i$). Status: STANDARD.
- $s$: A second extra-time direction of the fold (as $r$, different from it). Status: STANDARD.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.

<!-- end generated symbol list -->

The vielbein and the volume element ($i, j$ any two different directions of ordinary space, $r, s$ any two different extra
times; $x_i$ and $x_r$ the coordinates of these directions), the four dimensionless rates of the background ($\mathsf{A}$ the
expansion rate of ordinary space in units of $H$, $\mathsf{U}$ the rate of change of $b_4$), and every non-zero frame component
of the Riemann tensor, up to the symmetries $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc} = R_{cd}{}^{ab}$ (the last with the
frame metric). No component depends on $\sigma$ except through the sign of the two mixed ones, which change sign at the fold:
the bulk on each side of the fold is homogeneous along $\sigma$ (DERIVED, `um3_geometry.py`, G2, exact; `um3_fold.py`, J2). The
frame curvature of the hidden direction is $-H^2$: each half of a period is a space of constant negative curvature along
$\sigma$, like a slice of anti-de Sitter space, with the time not warped. Status: DERIVED.

## The bulk equations of the background

$$
\begin{aligned}
\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(0)}}{H^2} = -\frac{1}{16}\Big(&\mathsf{A}^6 - 3\mathsf{A}^5\mathsf{U} + 12\mathsf{A}^4\mathsf{U}^2 + 3\mathsf{A}^4\mathsf{U}_1 + 3\mathsf{A}^4\\
&+ 12\mathsf{A}^3\mathsf{A}_1\mathsf{U} - 19\mathsf{A}^3\mathsf{U}^3 - 12\mathsf{A}^3\mathsf{U}\mathsf{U}_1 - 6\mathsf{A}^3\mathsf{U} - 18\mathsf{A}^2\mathsf{A}_1\mathsf{U}^2 + 9\mathsf{A}^2\mathsf{U}^4\\
&+ 9\mathsf{A}^2\mathsf{U}^2\mathsf{U}_1 - 18\mathsf{A}^2\mathsf{U}^2 - 6\mathsf{A}^2\mathsf{U}_1 - 9\mathsf{A}^2 + 6\mathsf{A}\mathsf{A}_1\mathsf{U}^3 - 12\mathsf{A}\mathsf{A}_1\mathsf{U}\\
&+ 21\mathsf{A}\mathsf{U}^3 + 12\mathsf{A}\mathsf{U}\mathsf{U}_1 + 9\mathsf{A}\mathsf{U} + 6\mathsf{A}_1\mathsf{U}^2 + 3\mathsf{U}^4 + 3\mathsf{U}^2\mathsf{U}_1\\
&+ 18\mathsf{U}^2 + 3\mathsf{U}_1 + 5\Big),\\
\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(i)}{}_{(i)}}{H^2} = -\frac{1}{16}\Big(&\mathsf{A}^6 - 6\mathsf{A}^5\mathsf{U} - 5\mathsf{A}^4\mathsf{A}_1 + 12\mathsf{A}^4\mathsf{U}^2 + 3\mathsf{A}^4\mathsf{U}_1\\
&+ 3\mathsf{A}^4 + 12\mathsf{A}^3\mathsf{A}_1\mathsf{U} - 10\mathsf{A}^3\mathsf{U}^3 - 6\mathsf{A}^3\mathsf{U}\mathsf{U}_1 + 12\mathsf{A}^3\mathsf{U} - 9\mathsf{A}^2\mathsf{A}_1\mathsf{U}^2\\
&+ 6\mathsf{A}^2\mathsf{A}_1 + 3\mathsf{A}^2\mathsf{U}^4 + 3\mathsf{A}^2\mathsf{U}^2\mathsf{U}_1 - 36\mathsf{A}^2\mathsf{U}^2 - 6\mathsf{A}^2\mathsf{U}_1 - 9\mathsf{A}^2\\
&+ 2\mathsf{A}\mathsf{A}_1\mathsf{U}^3 - 12\mathsf{A}\mathsf{A}_1\mathsf{U} + 18\mathsf{A}\mathsf{U}^3 + 6\mathsf{A}\mathsf{U}\mathsf{U}_1 - 6\mathsf{A}\mathsf{U} + 3\mathsf{A}_1\mathsf{U}^2\\
&- \mathsf{A}_1 + 3\mathsf{U}^4 + 3\mathsf{U}^2\mathsf{U}_1 + 24\mathsf{U}^2 + 3\mathsf{U}_1 + 5\Big),\\
\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}}{H^2} = \frac{1}{16}\Big(&5\mathsf{A}^6 - 15\mathsf{A}^5\mathsf{U} + 15\mathsf{A}^4\mathsf{U}^2 - 9\mathsf{A}^4 - 5\mathsf{A}^3\mathsf{U}^3\\
&+ 18\mathsf{A}^3\mathsf{U} + 3\mathsf{A}^2 - 9\mathsf{A}\mathsf{U}^3 - 3\mathsf{A}\mathsf{U} - 3\mathsf{U}^2 + 1\Big),\\
\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(r)}{}_{(r)}}{H^2} = -\frac{1}{16}\Big(&\mathsf{A}^6 + 5\mathsf{A}^4\mathsf{A}_1 - 3\mathsf{A}^4\mathsf{U}^2 - 2\mathsf{A}^4\mathsf{U}_1 + 3\mathsf{A}^4\\
&- 8\mathsf{A}^3\mathsf{A}_1\mathsf{U} + 2\mathsf{A}^3\mathsf{U}^3 + 2\mathsf{A}^3\mathsf{U}\mathsf{U}_1 - 24\mathsf{A}^3\mathsf{U} + 3\mathsf{A}^2\mathsf{A}_1\mathsf{U}^2 - 6\mathsf{A}^2\mathsf{A}_1\\
&+ 18\mathsf{A}^2\mathsf{U}^2 - 9\mathsf{A}^2 + 6\mathsf{A}\mathsf{U}^3 + 6\mathsf{A}\mathsf{U}\mathsf{U}_1 + 24\mathsf{A}\mathsf{U} + 3\mathsf{A}_1\mathsf{U}^2\\
&+ \mathsf{A}_1 + 9\mathsf{U}^2 + 2\mathsf{U}_1 + 5\Big),\\
\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}}{H^2} = \mathrm{sgn}(\sigma)\,\frac{3}{16}\,\mathsf{U}\,&\mathcal{G},\qquad
 \mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1
\end{aligned} \tag{FE-29}
$$
<!-- symbols: kappa, Tbulk, ii, ir, Hconst, Asf, Usf, A1sf, U1sf, sgn, sigma, Gfac -->
<!-- begin generated symbol list -->
**Symbols in (FE-29).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{G}$: The factor of the $(\sigma, x_4)$ bulk equation of the author’s metric, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The bulk equations FE-1 for the author's metric, divided by $H^2$: the left-hand side of FE-1 with the author's weights and
$\Lambda = -10H^2$, evaluated exactly (DERIVED, `um3_geometry.py`, G3 and G4, with the identities FE-3 checked; `um3_fold.py`,
J2, by an independent general computation). They state what the bulk sources must be for given $a_4(x_4)$, $b_4(x_4)$:
$\mathcal{T}^{(4)}{}_{(4)} = -\rho$ gives the energy density, $\mathcal{T}^{(0)}{}_{(0)}$, $\mathcal{T}^{(i)}{}_{(i)}$,
$\mathcal{T}^{(r)}{}_{(r)}$ the pressures along $\sigma$, ordinary space and the extra times, and $\mathcal{T}^{(0)}{}_{(4)}$ the energy
flux along $\sigma$, which has opposite signs on the two sides of the fold (it flows toward or away from the fold on both
sides). Because the frame components do not depend on $\sigma$, the author's metric can be exact only with sources whose frame
components do not depend on $\sigma$; sources that depend on $\sigma$ require the next terms of the power series of the metric
(FE-35). The time-time equation contains no $\mathsf{A}_1$ and no $\mathsf{U}_1$: it is the energy constraint of the background.
The flux equation factorises: with a source without flux along $\sigma$, either $\mathsf{U} = 0$ ($b_4$ constant) or
$\mathcal{G}(\mathsf{A}, \mathsf{U}) = 0$, which has real roots $\mathsf{U}$ only for $0.3249 \le \lvert\mathsf{A}\rvert \le 1.3764$
($5\mathsf{A}^4 - 10\mathsf{A}^2 + 1 \le 0$). Status: DERIVED.

## The fold equations of the background

$$
\begin{aligned}
\frac{\kappa\,\mathcal{S}^{(i)}{}_{(i)}}{H} = \frac{1}{24}\Big(&9\mathsf{A}^4 - 24\mathsf{A}^3\mathsf{U} - 12\mathsf{A}^2\mathsf{A}_1
 + 27\mathsf{A}^2\mathsf{U}^2 + 12\mathsf{A}^2\mathsf{U}_1 - 66\mathsf{A}^2 + 24\mathsf{A}\mathsf{A}_1\mathsf{U} - 6\mathsf{A}\mathsf{U}^3
 - 12\mathsf{A}\mathsf{U}\mathsf{U}_1 + 120\mathsf{A}\mathsf{U}\\
&- 6\mathsf{A}_1\mathsf{U}^2 + 20\mathsf{A}_1 - 6\mathsf{U}^4 - 6\mathsf{U}^2\mathsf{U}_1 - 111\mathsf{U}^2 - 60\mathsf{U}_1 - 183\Big),\\
\frac{\kappa\,\mathcal{S}^{(4)}{}_{(4)}}{H} = -\frac14\Big(&3\mathsf{A}^4 - 6\mathsf{A}^3\mathsf{U} - 10\mathsf{A}^2 + 3\mathsf{A}\mathsf{U}^3
 + 10\mathsf{A}\mathsf{U} + 10\mathsf{U}^2 + 31\Big),\\
\frac{\kappa\,\mathcal{S}^{(r)}{}_{(r)}}{H} = \frac{1}{24}\Big(&9\mathsf{A}^4 - 12\mathsf{A}^3\mathsf{U} + 12\mathsf{A}^2\mathsf{A}_1
 + 9\mathsf{A}^2\mathsf{U}^2 - 66\mathsf{A}^2 - 12\mathsf{A}\mathsf{U}^3 - 12\mathsf{A}\mathsf{U}\mathsf{U}_1 + 12\mathsf{A}\mathsf{U}
 - 6\mathsf{A}_1\mathsf{U}^2 - 20\mathsf{A}_1\\
&- 57\mathsf{U}^2 - 40\mathsf{U}_1 - 183\Big)
\end{aligned} \tag{FE-30}
$$
<!-- symbols: kappa, Sfoldsrc, ii, ir, Hconst, Asf, Usf, A1sf, U1sf -->
<!-- begin generated symbol list -->
**Symbols in (FE-30).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The junction conditions FE-4 for the author's metric: the thin source that the fold must carry for given $a_4(x_4)$,
$b_4(x_4)$ (the off-diagonal and $(\sigma, \sigma)$ components have no thin part). They follow from the potential $\mathfrak{F}$
evaluated with $\partial_\sigma\mathfrak{a} = \partial_\sigma\mathfrak{b} = -H\,\mathrm{sgn}(\sigma)$ on the two sides (DERIVED,
`um3_fold.py`, J4 and J5, and independently by smoothing the kink, $\partial_\sigma\mathfrak{a} = -H\tanh(\sigma/\varepsilon)$, and
integrating the full left-hand side of FE-1 across the layer: the result converges linearly in $\varepsilon$ to FE-30). With
the bulk flux of FE-29 they satisfy the conservation law FE-11 identically (DERIVED, J6). Status: DERIVED.

## The author's vacuum

$$
\begin{aligned}
&a_4 = Hx_4,\quad b_4 = \text{constant}\ (\mathsf{A} = 1,\ \mathsf{U} = \mathsf{A}_1 = \mathsf{U}_1 = 0):\qquad
 \sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_N + \Lambda\,\delta^M_N = 0\quad(\sigma \ne 0),\\
&\kappa\,\mathcal{S}^{(i)}{}_{(i)} = \kappa\,\mathcal{S}^{(r)}{}_{(r)} = -10H,\qquad \kappa\,\mathcal{S}^{(4)}{}_{(4)} = -6H,\\
&\kappa\rho_{\mathrm{bulk}} = -H^2\Big[\frac34\big((\mathsf{A} - 1 - \mathsf{U})^2 + (\mathsf{A} - 1)^2\big) + \dots\Big],\qquad
 \mathcal{G}(1, \mathsf{U}) = 2\mathsf{U}(3\mathsf{U} - 2)
\end{aligned} \tag{FE-31}
$$
<!-- symbols: a4, Hconst, x4, b4, Asf, Usf, A1sf, U1sf, ip, alphaL, LovE, iM, iN, Lambda, delta, sigma, kappa, Sfoldsrc, ii, ir, rhobulk, Gfac -->
<!-- begin generated symbol list -->
**Symbols in (FE-31).**

- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations a second label of a Kohn-Sham orbital (as $o$, with $\delta_{op}$ the Kronecker delta of the two labels). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$: the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to the metric ($\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$ (the author writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-10H^2$. Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $\mathcal{G}$: The factor of the $(\sigma, x_4)$ bulk equation of the author’s metric, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The author's solution (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[134]: $a_4' = H$, the weights $(1, 1/32, 1/1152)$ and
$\Lambda_{\mathrm{N}} = 10$): ordinary space inflates with the rate $H$ forever and the extra times deflate
($\mathrm{e}^{-a_4}b_4 \propto \mathrm{e}^{-Hx_4}$), "eternal inflation/deflation". With the new metric ($b_4^2$) it is still an exact
vacuum solution of the bulk equations for every constant $b_4$ (DERIVED, `um3_geometry.py`, G4). Three facts about it (DERIVED):

* The fold must carry a thin source: $\kappa\mathcal{S} = \mathrm{diag}(-10H, -6H, -10H)$ for (ordinary space, time, extra times),
  an energy density $6H/\kappa$ with the pressure $-10H/\kappa$ (`um3_fold.py`, J5).
* The vacuum is degenerate: near it the energy density of any bulk source is
  $\kappa\rho_{\mathrm{bulk}} = -H^2[\frac34((\mathsf{A} - 1 - \mathsf{U})^2 + (\mathsf{A} - 1)^2) + \dots]$ (the dots are of third
  order in $\mathsf{A} - 1$ and $\mathsf{U}$): the linear terms vanish, so a small positive energy density of the bulk cannot be
  carried by a small change of $a_4$ and $b_4$ (`um3_geometry.py`, G4). The transverse traceless gravitons of the bulk have no
  time-kinetic term at this point (`um3_bulk.py`, B5).
* $b_4$ is a function of $x_4$, never identically 1 (the author's order): a constant $b_4 \ne 1$ is equivalent to $b_4 = 1$ by a
  rescaling of $x_5, x_6, x_7$ unless their coordinate period is fixed, and $\mathsf{U} \ne 0$ is not a vacuum solution near
  $\mathsf{A} = 1$: it needs a bulk source with a flux along $\sigma$, $\kappa\mathcal{T}^{(0)}{}_{(4)} = \mathrm{sgn}(\sigma)\frac{3}{16}\mathsf{U}\,\mathcal{G}(1,
  \mathsf{U})H^2 = \mathrm{sgn}(\sigma)\frac38\mathsf{U}^2(3\mathsf{U} - 2)H^2$, and a non-positive energy density. At $\mathsf{A} = 1$ the
  flux vanishes for $\mathsf{U} = 2/3$ ($b_4 \propto \mathrm{e}^{2Hx_4/3}$), which needs the constant source
  $\kappa\mathcal{T} = (-14/27, -2/9, 2/27, -22/27)H^2$ for ($\sigma$, ordinary space, time, extra times), with
  $\kappa\rho_{\mathrm{bulk}} = -2H^2/27$ (`um3_geometry.py`, G4).

Status: AUTHOR (the solution), DERIVED (the three facts).

## The static block and the frozen extra times

$$
\begin{aligned}
&\mathsf{A} = \mathsf{U} = \mathsf{A}_1 = \mathsf{U}_1 = 0:\qquad
 \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^a{}_b = H^2\,\mathrm{diag}\Big(-\frac{5}{16}, -\frac{5}{16}, -\frac{5}{16}, -\frac{5}{16},
 \frac{1}{16}, -\frac{5}{16}, -\frac{5}{16}, -\frac{5}{16}\Big),\\
&\kappa\,\mathcal{S}^{(i)}{}_{(i)} = \kappa\,\mathcal{S}^{(r)}{}_{(r)} = -\frac{61}{8}H,\qquad \kappa\,\mathcal{S}^{(4)}{}_{(4)} = -\frac{31}{4}H
\end{aligned} \tag{FE-32}
$$
<!-- symbols: Asf, Usf, A1sf, U1sf, kappa, Tbulk, ia, ib, Hconst, diag, Sfoldsrc, ii, ir -->
<!-- begin generated symbol list -->
**Symbols in (FE-32).**

- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.

<!-- end generated symbol list -->

The static block: $a_4$ and $b_4$ constant. Its bulk is (each half of a period) a seven-dimensional space of constant negative
curvature $-H^2$ of the directions $\sigma, x_1, x_2, x_3, x_5, x_6, x_7$ times the unwarped time (FE-28 with
$\mathsf{A} = \mathsf{U} = 0$). It is not a vacuum solution: it requires the bulk source of the first line, which is the stabiliser
IN-7 ($\kappa\rho = -H^2/16$, $\kappa p = -5H^2/16$), and the thin source of the second line at the fold, which is the fold fluid
at rest ($\kappa\rho_{\mathrm{ff}}/V_* = 31H/4$, $\kappa p_{\mathrm{ff}}/V_* = \kappa q_{\mathrm{ff}}/V_* = -61H/8$, $\rho + p = H/(8\kappa)$
per $V_*$, positive). The late universe, whose expansion rate is tiny in units of $H$, is the static block plus small corrections
(FE-33, FE-59). Status: DERIVED.

$$
\begin{aligned}
&\mathsf{U} = \mathsf{A},\quad \mathsf{U}_1 = \mathsf{A}_1\ \ \big(\mathrm{e}^{-a_4}b_4 = \text{constant},\ \mathcal{Z} = 1\big):\\
&\frac{\kappa\rho_{\mathrm{bulk}}}{H^2} = \frac{3\mathsf{A}^2 - 1}{16},\qquad
 \frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(0)}}{H^2} = -\frac{3\mathsf{A}^4 + 3\mathsf{A}^2\mathsf{A}_1 + 18\mathsf{A}^2 + 3\mathsf{A}_1 + 5}{16},\\
&\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(i)}{}_{(i)}}{H^2} = -\frac{9\mathsf{A}^2 + 2\mathsf{A}_1 + 5}{16},\qquad
 \frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(r)}{}_{(r)}}{H^2} = -\frac{3\mathsf{A}^4 + 3\mathsf{A}^2\mathsf{A}_1 + 24\mathsf{A}^2 + 3\mathsf{A}_1 + 5}{16},\\
&\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}}{H^2} = \mathrm{sgn}(\sigma)\,\frac{3\mathsf{A}(1 + \mathsf{A}^2)}{16},\qquad
 \frac{\kappa\,\mathcal{S}^{(i)}{}_{(i)}}{H} = -\frac{57\mathsf{A}^2 + 40\mathsf{A}_1 + 183}{24},\\
&\frac{\kappa\,\mathcal{S}^{(4)}{}_{(4)}}{H} = -\frac{10\mathsf{A}^2 + 31}{4},\qquad
 \frac{\kappa\,\mathcal{S}^{(r)}{}_{(r)}}{H} = -\frac{2\mathsf{A}^4 + 2\mathsf{A}^2\mathsf{A}_1 + 37\mathsf{A}^2 + 20\mathsf{A}_1 + 61}{8}
\end{aligned} \tag{FE-33}
$$
<!-- symbols: Usf, Asf, U1sf, A1sf, euler, a4, b4, Zfold, kappa, rhobulk, Hconst, Tbulk, ii, ir, sgn, sigma, Sfoldsrc -->
<!-- begin generated symbol list -->
**Symbols in (FE-33).**

- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{S}^a{}_b$: The thin source of the fold: its energy-momentum tensor per unit proper length across the fold (eight-dimensional normalisation, frame components along the fold); it is fixed by the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions; $\kappa\mathcal{S}$ is the jump of the junction potential). Unit: GeV$^7$. Status: DERIVED.

<!-- end generated symbol list -->

The frozen extra times: the physical size $\mathrm{e}^{-a_4}b_4$ of the extra times is constant while ordinary space expands. Then the
fold factor $\mathcal{Z}$ is constant (IN-8) and every coupling of the Standard Model is constant in time, as observation requires
(the fine-structure constant has not changed by more than parts in $10^{6}$ since the CMB); this is the condition of the late
universe. It gives $b_4 = c_b\,\mathrm{e}^{a_4}$ with a constant $c_b$: $b_4$ grows with the scale factor of ordinary space, so it is a
non-trivial function of $x_4$, never identically 1, as the author requires. The equations of FE-29 and FE-30 on this branch are
written out (DERIVED, `um3_geometry.py`, G4, `um3_fold.py`, J7). For $\mathsf{A} \to 0$ they reduce to the static block FE-32.
The extra energy of the fold above the static value is $(5/2)a_4'^2/(\kappa H)$ per $V_*$: on the separable metric the fold
energy fixes the expansion rate. A fold fluid on top of the static values cannot be separately conserved on the separable metric,
for any equation of state: its continuity equation fails by $(3/8)a_4'^3/(\kappa H)$, the part of the jump of the bulk energy flux
at the fold that the static source does not balance (DERIVED, J7), so ordinary matter on the fold requires the next terms of the
power series (FE-35, FE-59). The whole source of the fold of FE-33, on the other hand, takes up the jump of the bulk energy flux
exactly, for any $a_4(x_4)$: $-(\kappa\mathcal{S}^{(4)}{}_{(4)})' + 3a_4'(\kappa\mathcal{S}^{(i)}{}_{(i)} - \kappa\mathcal{S}^{(4)}{}_{(4)})$ equals the jump
$\frac38\mathsf{A}(1 + \mathsf{A}^2)H^2$ (the second line of FE-11; DERIVED, `um3_stabiliser.py`, ST6). Status: DERIVED.

$$
\begin{aligned}
&\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = \frac{H^2}{16}\,\mathsf{P}(\mathsf{A}, \mathsf{U}),\qquad
 \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)} = \frac{3}{16}\,\mathsf{U}\,\mathcal{G}(\mathsf{A}, \mathsf{U})\,H^2\,\mathrm{sgn}(\sigma),\\
&\mathsf{P} = 5\mathsf{A}^6 - 15\mathsf{A}^5\mathsf{U} + 15\mathsf{A}^4\mathsf{U}^2 - 9\mathsf{A}^4 - 5\mathsf{A}^3\mathsf{U}^3
 + 18\mathsf{A}^3\mathsf{U} + 3\mathsf{A}^2 - 9\mathsf{A}\mathsf{U}^3 - 3\mathsf{A}\mathsf{U} - 3\mathsf{U}^2 + 1,\\
&\mathsf{P}(\mathsf{A}, \mathsf{U}) = 0\ \Rightarrow\ \mathsf{A}^2 + \mathsf{U}^2 \ge 0.2607,\qquad
 \mathsf{U} = \mathsf{A}:\ \ 3a_4'^2 = 16\kappa\big(\rho_{\mathrm{bulk}} - \rho_{\mathrm{s}}\big)
\end{aligned} \tag{FE-66}
$$
<!-- symbols: kappa, Tbulk, Hconst, Pcon, Asf, Usf, Gfac, sgn, sigma, a4, prime, rhobulk, rhos -->
<!-- begin generated symbol list -->
**Symbols in (FE-66).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk, $\mathcal{T}_\Psi + \mathcal{T}_{\mathrm{stab}}$; $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{P}(\mathsf{A}, \mathsf{U})$: The polynomial of the energy constraint of the bulk: the $(x_4, x_4)$ component of the bulk equations of the author’s metric is $\kappa\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = (H^2/16)\,\mathsf{P}(\mathsf{A}, \mathsf{U})$, whatever the time derivatives of the rates. Unit: dimensionless. Value: $\mathsf{P}(0, 0) = 1$, $\mathsf{P}(\pm1, 0) = 0$. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 1 at the author's vacuum, 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant). Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathcal{G}$: The factor of the $(\sigma, x_4)$ bulk equation of the author’s metric, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $\mathrm{sgn}(y) = +1$ for $y > 0$, $-1$ for $y < 0$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser; with frozen extra times it is the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$. Status: DERIVED (the value), ASSUMED (a separate medium).

<!-- end generated symbol list -->

The two constraints of the bulk equations of the author's metric, for any $a_4(x_4)$ and $b_4(x_4)$: the $(x_4, x_4)$ component (the
energy constraint) and the $(\sigma, x_4)$ component (the flow of energy along the hidden direction) contain no second time
derivative ($\mathsf{A}_1$ and $\mathsf{U}_1$ drop out). Without a bulk source $\mathsf{P} = 0$ at every instant, which keeps
$\mathsf{A}^2 + \mathsf{U}^2$ at least 0.2607 (reached at $(\mathsf{A}, \mathsf{U}) = \pm(0.1432, 0.4901)$) and the larger of $\lvert\mathsf{A}\rvert$
and $\lvert\mathsf{U}\rvert$ at least 0.4771 (reached at $\pm(0.2385, 0.4771)$): a sourceless bulk never has both rates below $0.477H$, and
with constant rates only $(\pm1, 0)$ are possible. With frozen extra times $\mathsf{P} = 1 - 3\mathsf{A}^2$,
and the energy constraint becomes a Friedmann equation of the bulk: the energy density $\rho_{\mathrm{s}} = -H^2/(16\kappa)$ of the
stabiliser IN-7 is the energy density of the bulk at which ordinary space stands still (a bulk source of zero energy density would
need $a_4' = H/\sqrt3$). The flow vanishes while $b_4$ is constant ($\mathsf{U} = 0$, as in the author's vacuum, where
$\mathcal{G}(1, \mathsf{U}) = 2\mathsf{U}(3\mathsf{U} - 2)$); with frozen extra times it is $\frac{3}{16}\mathsf{A}(1 + \mathsf{A}^2)H^2\,\mathrm{sgn}(\sigma)$
(FE-33), zero only at $\mathsf{A} = 0$, where $\mathsf{P} = 1$, so that a bulk without any source cannot have frozen extra times; it
jumps by $\frac38\mathsf{A}(1 + \mathsf{A}^2)H^2$ across the fold. It is the energy that the bulk source gives off while
ordinary space grows: at constant $\mathsf{A}$, $\kappa(\rho_{\mathrm{bulk}} + \mathcal{T}_{\mathrm{bulk}}{}^{(1)}{}_{(1)}) = -\frac38(1 + \mathsf{A}^2)H^2$
(FE-33), and $-3a_4'(\rho_{\mathrm{bulk}} + \mathcal{T}_{\mathrm{bulk}}{}^{(1)}{}_{(1)})$ per volume and time, integrated across the hidden direction with the
weight $\mathrm{e}^{-6H\lvert\sigma\rvert}$, is exactly the jump; the source of the fold takes it up (FE-33, FE-11). Status: DERIVED
(`um3_stabiliser.py`, ST6 and ST8; `um3_geometry.py`, G4).

## The general warped metric and the power series of the metric

$$
\begin{aligned}
&g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{2\mathfrak{a}}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)
 - \mathrm{e}^{2\mathfrak{n}}\,\mathrm{d}x_4^2 - \mathrm{e}^{2\mathfrak{b}}\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big),\\
&R^{(0)(i)}{}_{(0)(i)} = -\partial_\sigma^2\mathfrak{a} - (\partial_\sigma\mathfrak{a})^2,\qquad
 R^{(0)(4)}{}_{(0)(4)} = -\partial_\sigma^2\mathfrak{n} - (\partial_\sigma\mathfrak{n})^2,\qquad
 R^{(i)(j)}{}_{(i)(j)} = -(\partial_\sigma\mathfrak{a})^2 + \mathrm{e}^{-2\mathfrak{n}}(\partial_{x_4}\mathfrak{a})^2,\\
&R^{(i)(r)}{}_{(i)(r)} = -\partial_\sigma\mathfrak{a}\,\partial_\sigma\mathfrak{b} + \mathrm{e}^{-2\mathfrak{n}}\,\partial_{x_4}\mathfrak{a}\,\partial_{x_4}\mathfrak{b},\qquad
 R^{(i)(4)}{}_{(i)(4)} = -\partial_\sigma\mathfrak{a}\,\partial_\sigma\mathfrak{n} + \mathrm{e}^{-2\mathfrak{n}}\big(\partial_{x_4}^2\mathfrak{a}
 + (\partial_{x_4}\mathfrak{a})^2 - \partial_{x_4}\mathfrak{a}\,\partial_{x_4}\mathfrak{n}\big),\\
&R^{(0)(i)}{}_{(4)(i)} = -\mathrm{e}^{-\mathfrak{n}}\big(\partial_\sigma\partial_{x_4}\mathfrak{a} + \partial_\sigma\mathfrak{a}\,\partial_{x_4}\mathfrak{a}
 - \partial_{x_4}\mathfrak{a}\,\partial_\sigma\mathfrak{n}\big)
\end{aligned} \tag{FE-34}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, sigma, euler, awarp, x1, x2, x3, nwarp, x4, bwarp, x5, x6, x7, Riemann, ii, ij, ir, partial, isigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-34).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathfrak{a},\ \mathfrak{a}_1$: The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\mathfrak{n},\ \mathfrak{n}_1$: The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\mathfrak{b},\ \mathfrak{b}_1$: The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor (convention $[\nabla_P, \nabla_Q]V^M = R^M{}_{NPQ}V^N$), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $j$: A second generation or mass-state index (as $i$). Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.

<!-- end generated symbol list -->

The general metric with the symmetries of the author's metric (homogeneous and isotropic in ordinary space and in the extra
times, independent of the extra times) but with three arbitrary functions $\mathfrak{a}$, $\mathfrak{b}$, $\mathfrak{n}$ of $\sigma$ and
$x_4$, and its frame curvature: the components with the extra times follow from those with ordinary space by replacing
$\mathfrak{a}$ by $\mathfrak{b}$ and $(i)$ by $(r)$ ($R^{(0)(r)}{}_{(0)(r)}$, $R^{(r)(s)}{}_{(r)(s)}$, $R^{(r)(4)}{}_{(r)(4)}$,
$R^{(0)(r)}{}_{(4)(r)}$); all others vanish (DERIVED, `um3_fold.py`, J2). Its Lovelock tensor is FE-2 with these components; it has
only diagonal components and the $(\sigma, x_4)$ pair. The author's metric is $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$,
$\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$, $\mathfrak{n} = 0$, and the general equations reduce to FE-29 on both sides of the
fold (DERIVED, J2). Status: DERIVED.

$$
\begin{aligned}
&\mathfrak{a} = a_4 - H\lvert\sigma\rvert + \sum_{n\ge1}\epsilon_{\mathrm{r}}^{\,n}\,\mathfrak{a}_n(\sigma, x_4),\qquad
 \mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert + \sum_{n\ge1}\epsilon_{\mathrm{r}}^{\,n}\,\mathfrak{b}_n(\sigma, x_4),\\
&\mathfrak{n} = \sum_{n\ge1}\epsilon_{\mathrm{r}}^{\,n}\,\mathfrak{n}_n(\sigma, x_4),\qquad
 \hat h_{\mu\nu} \to \hat h_{\mu\nu} + \epsilon_{\mathrm{c}}\,\hat h^{(1)}_{\mu\nu} + \dots
\end{aligned} \tag{FE-35}
$$
<!-- symbols: awarp, a4, Hconst, sigma, inn, epsr, x4, bwarp, b4, nwarp, hhat, imu, inu, epsc -->
<!-- begin generated symbol list -->
**Symbols in (FE-35).**

- $\mathfrak{a},\ \mathfrak{a}_1$: The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $n$: The order $n = 1, 2, \dots$ of a term of the power series of the metric (also its exponent of $\epsilon_{\mathrm{r}}$); $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{n}_n$ are the terms of order $n$. Status: STANDARD.
- $\epsilon_{\mathrm{r}}$: The bookkeeping parameter of the response of the bulk to the matter of the fold: the ratio of the bulk to the fold gravity, $\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$. Unit: dimensionless. Value: below $1.344\times10^{-13}$: the four-dimensional gravitational wave has $c_{\mathrm{g}}^2 = (96 + 83\epsilon_{\mathrm{r}})/(96 + 82\epsilon_{\mathrm{r}})$, and the gravitational waves and the light of the neutron-star merger GW170817 arrived together, $(c_{\mathrm{g}} - 1) < 7\times10^{-16}$. Status: DERIVED.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\mathfrak{b},\ \mathfrak{b}_1$: The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $\mathfrak{n},\ \mathfrak{n}_1$: The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\epsilon_{\mathrm{c}}$: The bookkeeping parameter of the cosmological perturbations of the metric of the fold (the size of the CMB anisotropies). Unit: dimensionless. Value: $\sim 10^{-5}$. Status: STANDARD.

<!-- end generated symbol list -->

The metric as a power series of terms of decreasing magnitude (the author's request): the order-0 term is the author's metric;
the terms of order $n$ in $\epsilon_{\mathrm{r}}$ are the response of the bulk to the matter of the fold and of dirac16complex,
which depends on $\sigma$; $\epsilon_{\mathrm{c}} \sim 10^{-5}$ (the size of the CMB anisotropies) counts the cosmological perturbations
of the metric of the fold. The bookkeeping parameter $\epsilon_{\mathrm{r}}$ is the ratio of the bulk to the fold gravity,
$\epsilon_{\mathrm{r}} = \kappa_4V_*/(\kappa H)$ (FE-59). Each order obeys the linearisation of FE-1 and FE-4 around the previous orders, with the
sources of that order. Around the static block the static first-order terms obey linear equations with constant coefficients; if the bulk
medium does not respond, their only solution is the difference mode $\mathfrak{a}_1' = -\mathfrak{b}_1' \propto \mathrm{e}^{6H\lvert\sigma\rvert}$, which
grows away from the fold, while a responding medium admits the radion mode, whose jumps at the fold are in the ratio
$[\mathfrak{a}_1'] : [\mathfrak{b}_1'] : [\mathfrak{n}_1'] = 1 : -1 : 5$ and change only the extra-time component of FE-4 (DERIVED, `um3_series.py`, SR1
to SR3; FE-59). Status: DERIVED (the scheme and the first-order modes).

# dirac16complex: modes and Kohn-Sham equations

dirac16complex lives in the bulk; its four-dimensional particles are its modes along the hidden direction. This section writes
the equation of those modes on the static block (the late universe; the primordial era replaces $a_4$, $b_4$ by their values
there), the conditions at the fold, the states bound to the fold, and the Kohn-Sham equations that make the description
self-consistent with the self-interaction, with gravity and with the mean fields of the Standard Model.

## The equation of the hidden direction

$$
\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\,\chi(\sigma)\,\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)},\qquad
\gamma^{(0)}\chi' - \mathrm{i}\omega\,\gamma^{(4)}\chi + \mathrm{i}\,\mathrm{e}^{H\lvert\sigma\rvert}\,\vec k\cdot\vec\gamma\,\chi
 - m_\Psi\chi = 0\qquad(\sigma \ne 0) \tag{FE-36}
$$
<!-- symbols: Psi, euler, Hconst, sigma, chiprof, imag, kvec, xvec, omegafreq, x4, gammaM, prime, gammavec, mPsi -->
<!-- begin generated symbol list -->
**Symbols in (FE-36).**

- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings and the cosmological constant $\Lambda = -10H^2$; in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\vec\gamma$: The three frame Dirac matrices of dirac16complex along ordinary space, $\vec\gamma = (\gamma^{(1)}, \gamma^{(2)}, \gamma^{(3)})$. Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->

The free field equation FE-12 on the static block ($a_4$ and $b_4$ constant, ordinary space normalised so that $\mathrm{e}^{a_4} = 1$
at the fold) for a mode of definite momentum $\vec k$ along ordinary space and frequency $\omega$, independent of the extra
times. The factor $\mathrm{e}^{3H\lvert\sigma\rvert}$ removes the spin connection exactly ($\gamma^{(0)}\partial_\sigma\mathrm{e}^{3H\lvert\sigma\rvert} =
3H\,\mathrm{sgn}(\sigma)\gamma^{(0)}\mathrm{e}^{3H\lvert\sigma\rvert}$ cancels the first term of FE-14), so that the profile $\chi(\sigma)$ obeys a
Dirac equation of one variable whose only dependence on $\sigma$ is the warp $\mathrm{e}^{H\lvert\sigma\rvert}$ of the momentum. The
four-dimensional norm density is $\sqrt{\lvert g\rvert}\,\Psi^\dagger\Psi = \chi^\dagger\chi$ (times $b_4^3$). Status: DERIVED.

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

At zero momentum along ordinary space ($\vec k = 0$) the profile equation has constant coefficients on each side of the fold:
$\chi$ is a combination of $\mathrm{e}^{+q\sigma}$ and $\mathrm{e}^{-q\sigma}$ (eight solutions each). For $\lvert\omega\rvert \ge m_\Psi$,
$q$ is imaginary and the modes are waves along $\sigma$: the bulk continuum, which starts at the bulk mass $m_\Psi$. For
$\lvert\omega\rvert < m_\Psi$ the solutions grow or decay exponentially, and only the fold terms (FE-39) can join decaying
solutions on the two sides into a normalisable state. With chirality-dependent masses $m_{\mathrm{L}}P_{\mathrm{L}} + m_{\mathrm{R}}P_{\mathrm{R}}$
in place of $m_\Psi$ the threshold would be $\sqrt{m_{\mathrm{L}}m_{\mathrm{R}}}$ (tachyonic for $m_{\mathrm{L}}m_{\mathrm{R}} < 0$); UM-3
keeps the record's single bulk mass and puts the difference of the halves into the fold terms (DERIVED, `um3_spectra.py`, S1,
and `um3_bulk.py`, B4, with the author's matrices). Status: DERIVED.

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

The local dispersion relation of dirac16complex (WKB: for profiles that vary slowly compared with the warp), with the momentum
$p_\sigma$ along the hidden direction and a momentum $\vec\kappa$ along the extra times. A momentum along a time-like direction
enters with the negative sign: modes that depend on the extra times have $\omega^2 < 0$ for large $\lvert\vec\kappa\rvert$, they grow
exponentially in $x_4$ (tachyons). The same holds for every field (the sign comes from $g^{rr} < 0$). UM-3 therefore keeps only
the fields that do not depend on the extra times (ASSUMED); making the extra times small does not help, because it only
raises the lowest non-zero $\lvert\vec\kappa\rvert$. The restriction is consistent but not stable (DERIVED, `um3_extratimes.py`, EX1 to
EX5): the metric does not depend on $x_5, x_6, x_7$, so the momentum along the extra times is conserved and a field without it
stays without it classically, but interactions create pairs of opposite momenta, and every mode with $\vec\kappa \ne 0$ of every
field is a tachyon. A state of dirac16complex bound to the fold (FE-40, at the energy $\omega_{\mathrm{b}}$) with the momentum $\vec\kappa$ has
$\omega^2 = \omega_{\mathrm{b}}^2 - c_{\mathrm{b}}^2\vec\kappa^2$, where $c_{\mathrm{b}}$ is the limiting speed of the bound particles along ordinary space
($c_{\mathrm{b}}^2 = 1.19$ for $H = 0.05\,m_\Psi$ and the inverse width $q_{\mathrm{b}} = 0.3\,m_\Psi$), and is no longer bound, because the warp raises its momentum along the
extra times above the local gap far from the fold; in the author's vacuum the tachyonic modes grow double-exponentially; and compact
extra times would have to be longer than $2\pi$ times the age of the universe, 26.6 Gpc, to keep the slowest of them from growing
within that age. UM-3 needs a gauge principle that removes the momentum along the extra times of every field. Status: DERIVED (the
dispersion, from the identity $(\mathcal{D} + m_\Psi)(\mathcal{D} - m_\Psi) = \mathcal{D}^2 - m_\Psi^2$ of the Dirac operator $\mathcal{D}$, and the
instability), ASSUMED (the restriction), OPEN (the gauge principle).

## The fold and the states bound to it

$$
\begin{aligned}
&\chi(0^+) = \exp\Big(\gamma^{(0)}\big(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}\big)\Big)\,\chi(0^-),\\
&\mu_X = \frac{1}{V_*}\Big[c_\Phi\,\langle\Phi^\dagger\Phi\rangle\,\delta_{X\mathrm{L}} + \frac14\big(c^{G}_X\langle G^2\rangle
 + c^{W}_X\langle W^2\rangle + c^{B}_X\langle B^2\rangle\big) + 2\omega\sum_f c^{f}_X\,n_f\Big],\qquad
 \langle\Phi^\dagger\Phi\rangle = \frac{v^2 + \mathcal{A}^2}{2}
\end{aligned} \tag{FE-39}
$$
<!-- symbols: chiprof, gammaM, muX, PL, PR, iX, Vstar, cPhi, Phi, dagger, mean, delta, cG, Gsq, Ggluon, cW, Wsq, Wsu2, cB, Bsq, Bhyp, omegafreq, if, cf, nf, vev, Aadhoc -->
<!-- begin generated symbol list -->
**Symbols in (FE-39).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $G^A_\mu,\ G^A_{\mu\nu}$: The gluon field of $SU(3)_C$ on the fold ($A = 1, \dots, 8$) and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle W^2\rangle$: The mean square of the $SU(2)$ field strength, $\langle W^I_{\mu\nu}W^{I\mu\nu}\rangle$. Unit: GeV$^4$. Status: STANDARD.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle B^2\rangle$: The mean square of the hypercharge field strength, $\langle B_{\mu\nu}B^{\mu\nu}\rangle$. Unit: GeV$^4$. Status: STANDARD.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $n_f$: The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium. Unit: GeV$^3$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.

<!-- end generated symbol list -->

The matching condition FE-13 for a mode, with the Standard-Model fields replaced by their mean values in a homogeneous,
isotropic medium at rest on the fold (no mean field strength, no mean spatial current): the fold acts on dirac16complex as a
chirality-dependent mass concentrated at $\sigma = 0$, with the dimensionless strengths $\mu_{\mathrm{L}}$ and $\mu_{\mathrm{R}}$. The
Higgs portal acts on the left-handed half only ($\delta_{X\mathrm{L}} = 1$ for $X = \mathrm{L}$, 0 for $X = \mathrm{R}$); the gauge-kinetic
portals act through the mean squares $\langle G^2\rangle = \langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate of the QCD vacuum,
or of the plasma), $\langle W^2\rangle$, $\langle B^2\rangle$; the current portals act through the number densities $n_f$ of the
Standard-Model fermions of kind $f$ (they give an energy-dependent strength). In the vacuum of the late universe only the Higgs
term and the gluon condensate contribute. $(\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}))^2 = \mu_{\mathrm{L}}\mu_{\mathrm{R}}\mathbf{1}$,
so the exponential is $\cosh\varsigma + (\sinh\varsigma/\varsigma)\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$ with $\varsigma^2 = \mu_{\mathrm{L}}\mu_{\mathrm{R}}$; for
$\mu_{\mathrm{R}} = 0$ it is exactly $1 + \mu_{\mathrm{L}}\gamma^{(0)}P_{\mathrm{L}}$ (DERIVED, `um3_spectra.py`, S2). Status: DERIVED.

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

The states of dirac16complex bound to the fold at zero momentum: the decaying solutions of FE-37 on the two sides, joined by
FE-39. A bound state exists if and only if $0 < q_{\mathrm{b}} < m_\Psi$, that is if the fold is attractive, $\mu_{\mathrm{L}} + \mu_{\mathrm{R}} < 0$
(for $\mu_{\mathrm{L}}\mu_{\mathrm{R}} < 0$, $\tanh(\varsigma)/\varsigma$ means $\tan(\varsigma_-)/\varsigma_-$ with $\varsigma_- = \sqrt{-\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$). Its energy
$\omega_{\mathrm{b}}$ is the four-dimensional rest mass of a particle that lives near the fold, with the profile
$\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$ of width $1/q_{\mathrm{b}}$ along $\sigma$: the "$x_0$ mass" of dirac16complex. The bound states are
degenerate eight times at $+\omega_{\mathrm{b}}$ and eight times at $-\omega_{\mathrm{b}}$ (DERIVED, `um3_spectra.py`, S3: the roots of the $8 \times 8$
matching determinant with the author's $16 \times 16$ matrices agree with this formula to $10^{-7}$ in seven cases, with and
without bound states). For the Higgs portal alone ($\mu_{\mathrm{R}} = 0$): $q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$,
$\omega_{\mathrm{b}} = m_\Psi\sqrt{1 - \mu_{\mathrm{L}}^2/4}$. Status: DERIVED.

## The Kohn-Sham equations

$$
\begin{aligned}
&\big[\gamma^MD_M - m_\Psi - \lambda_\Psi\,n_{\mathrm{s}} + \lambda_\Psi\,\mathcal{N}\big]\varphi_o
 = \delta_{\mathrm{D}}(\sigma)\,\frac{1}{V_*}\,\langle\mathbb{M}\rangle\,\varphi_o,\\
&\mathcal{N} = \sum_o\mathsf{n}_o\,\varphi_o\bar\varphi_o,\qquad n_{\mathrm{s}} = \mathrm{tr}\,\mathcal{N} = \sum_o\mathsf{n}_o\,\bar\varphi_o\varphi_o,\qquad
 \mathsf{n}_o = \frac{1}{\mathrm{e}^{(E_o - \mu_\Psi)/\mathsf{T}_\Psi} + 1}
\end{aligned} \tag{FE-41}
$$
<!-- symbols: gammaM, iM, Dcov, mPsi, lamPsi, ns, Nmat, KSorb, io, deltaD, sigma, Vstar, mean, Mfold, nocc, trace, euler, Eorb, muPsi, TPsiT -->
<!-- begin generated symbol list -->
**Symbols in (FE-41).**

- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.
- $n_{\mathrm{s}}$: The scalar density of dirac16complex in the Kohn-Sham state, $n_{\mathrm{s}} = \langle\bar\Psi\Psi\rangle = \mathrm{tr}\,\mathcal{N}$. Unit: GeV$^7$. Status: DERIVED.
- $\mathcal{N}$: The one-body density matrix of dirac16complex, $\mathcal{N} = \sum_o\mathsf{n}_o\varphi_o\bar\varphi_o$ (a $16 \times 16$ matrix at each point). Unit: GeV$^7$. Status: DERIVED.
- $\varphi_o,\ \bar\varphi_o$: A Kohn-Sham orbital of dirac16complex (a single-particle solution of FE-41) and its Dirac adjoint. Unit: GeV$^{7/2}$. Status: RECORD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- $\delta_{\mathrm{D}}$: The Dirac delta function: $\int\mathrm{d}\sigma\,\delta_{\mathrm{D}}(\sigma)F(\sigma) = F(0)$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathbb{M}$: The fold operator of dirac16complex: the $16 \times 16$ matrix (with a derivative along the fold) built from the Standard-Model fields at the fold by varying the portals with respect to $\bar\Psi$ (FE-13). Unit: GeV$^{-3}$ (so that $\mathbb{M}/V_*$ is dimensionless). Status: DERIVED.
- $\mathsf{n}_o$: The occupation of the Kohn-Sham orbital $o$ (between 0 and 1). Unit: dimensionless. Status: RECORD.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $\mu_\Psi$: The chemical potential of dirac16complex. Unit: GeV. Status: DERIVED.
- $\mathsf{T}_\Psi$: The temperature of dirac16complex. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The Kohn-Sham equations of dirac16complex coupled to itself, to gravity and to every Standard-Model field: the quantised field
is described by single-particle orbitals $\varphi_o$ with the occupations $\mathsf{n}_o$ (Fermi-Dirac with the temperature $\mathsf{T}_\Psi$ and the
chemical potential $\mu_\Psi$ of dirac16complex; $\mathsf{n}_o = 0$ or 1 in a degenerate state). Each orbital obeys the field equation
with the mean fields: gravity through $D_M$ and $\gamma^M$ (the background metric and its spin connection), the self-interaction
through the Hartree term $\lambda_\Psi n_{\mathrm{s}}$ (the scalar density) and the exact exchange term $-\lambda_\Psi\mathcal{N}$ (the
one-body density matrix, a $16 \times 16$ matrix at each point), and every Standard-Model field through the fold operator with
the mean fields of the Standard Model, $\langle\mathbb{M}\rangle$ (FE-13, FE-39). The mean-field decomposition of
$-\frac{\lambda_\Psi}{2}(\bar\Psi\Psi)^2$ is $-\lambda_\Psi n_{\mathrm{s}}\bar\Psi\Psi + \lambda_\Psi\bar\Psi\mathcal{N}\Psi$ (the second term with the sign
of fermion exchange); correlation beyond exchange is neglected and the negative-energy sea is not included (no-sea
approximation). Status: RECORD (the Kohn-Sham treatment), DERIVED (the exchange term), ASSUMED (no correlation, no sea).

$$
\langle{\mathcal{T}_\Psi}_{MN}\rangle = -\frac14\sum_o\mathsf{n}_o\Big(\bar\varphi_o\gamma_MD_N\varphi_o + \bar\varphi_o\gamma_ND_M\varphi_o
 - (D_M\bar\varphi_o)\gamma_N\varphi_o - (D_N\bar\varphi_o)\gamma_M\varphi_o\Big) + \frac{\lambda_\Psi}{2}\,g_{MN}\big(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2\big) \tag{FE-42}
$$
<!-- symbols: mean, TPsi, iM, iN, io, nocc, KSorb, gammaM, Dcov, lamPsi, metric, ns, trace, Nmat -->
<!-- begin generated symbol list -->
**Symbols in (FE-42).**

- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex, $\mathcal{T}_{MN} = -(2/\sqrt{\lvert g\rvert})\,\delta S_\Psi/\delta g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- $\mathsf{n}_o$: The occupation of the Kohn-Sham orbital $o$ (between 0 and 1). Unit: dimensionless. Status: RECORD.
- $\varphi_o,\ \bar\varphi_o$: A Kohn-Sham orbital of dirac16complex (a single-particle solution of FE-41) and its Dirac adjoint. Unit: GeV$^{7/2}$. Status: RECORD.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $n_{\mathrm{s}}$: The scalar density of dirac16complex in the Kohn-Sham state, $n_{\mathrm{s}} = \langle\bar\Psi\Psi\rangle = \mathrm{tr}\,\mathcal{N}$. Unit: GeV$^7$. Status: DERIVED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\mathcal{N}$: The one-body density matrix of dirac16complex, $\mathcal{N} = \sum_o\mathsf{n}_o\varphi_o\bar\varphi_o$ (a $16 \times 16$ matrix at each point). Unit: GeV$^7$. Status: DERIVED.

<!-- end generated symbol list -->

The energy-momentum tensor of the Kohn-Sham state, the source of dirac16complex in FE-1 and, through the portals, in FE-5: the
sum over the occupied orbitals of FE-6, and the mean value of the self-interaction (on solutions of FE-41,
$\langle\mathcal{L}_\Psi\rangle = \frac{\lambda_\Psi}{2}(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2)$). It closes the loop: the orbitals determine the
densities, the densities the mean fields and the metric, the metric and the mean fields the orbitals. Status: DERIVED.

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

The conserved charge of dirac16complex (the Noether charge of a constant change of the phase of $\Psi$, whose density is
$\mathrm{i}\bar\Psi\gamma^{x_4}\Psi$) is a Krein form: $\mathfrak{B}$ is a Hermitian involution with eight eigenvalues $+1$ and eight
eigenvalues $-1$, so the charge, and with it the norm of the quantised field, is indefinite (the consequence of the signature
(4,4); DERIVED, `um3_fields.py`, F3). $\mathfrak{B}$ commutes with $\gamma^{(0)}, \dots, \gamma^{(4)}$ and anticommutes with
$\gamma^{(5)}, \gamma^{(6)}, \gamma^{(7)}$ and with $\Gamma_8$: every term that treats the two halves differently (here: the fold terms with
$\mu_{\mathrm{L}} \ne \mu_{\mathrm{R}}$) mixes the two Krein sectors. The energy of a stationary orbital of frequency $\omega_o$ and charge
$\mathcal{Q}_o$ is $E_o = -\omega_o\mathcal{Q}_o$ (from FE-6), positive when the frequency and the charge have opposite signs. Of the eight bound
states at $+\omega_{\mathrm{b}}$, four have positive and four negative charge (DERIVED, `um3_spectra.py`, S4; no null states): four carry
positive and four negative energy. The quantisation of this charge is FE-67. Status: DERIVED.

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

The quantised dirac16complex. The canonical anticommutator of the field is $\{\Psi, \Psi^\dagger\} = -\mathfrak{B}$ (times the delta function
of the positions), the overall sign chosen so that the occupied bound states of charge $-1$, the particles $\chi$, have a positive norm.
A mode $o$ of the frequency $\omega_o$ and the Krein charge $\mathcal{Q}_o = \pm1$ then has the anticommutator $-\mathcal{Q}_o$, the field has the
Hamiltonian $\mathsf{H}_\Psi$ (with FE-43, the energy of the mode is $-\mathcal{Q}_o\omega_o$), and every quantum raises the energy by its
frequency. In the positive-energy quantisation (the vacuum is annihilated by $\mathsf{a}_o$ for $\omega_o > 0$ and by $\mathsf{a}_o^\dagger$ for
$\omega_o < 0$) every particle and every hole carries a positive energy and the norm $-\mathcal{Q}_o$ of its mode: the particles and the
holes of the modes of charge $-1$ are physical, those of the modes of charge $+1$ are ghosts (negative norm). A fermion cannot trade its
norm for its energy ($\{\mathsf{a}, \mathsf{a}^\dagger\} = -1$ has no representation with a positive norm), so no choice of the vacuum removes the
ghosts. The consequences (DERIVED, `um3_krein.py`, KR1 to KR7): the vacuum cannot decay, because every quantum has a positive energy;
classically the dilute gas of the particles $\chi$ is stable, since the directions that mix the two charges are flat (zero modes of
boosts between ordinary space and the extra times), but the dense gas is not: where the repulsion has pushed the partner level of
charge $+1$ onto the occupied level, a growing mode appears (for $H = 0.05\,m_\Psi$ and $q_{\mathrm{b}} = 0.3\,m_\Psi$ from the strength
$\lambda_\Psi n_\chi/V_* = 0.3\,m_\Psi$ of the self-interaction on, $n_\chi$ the number density of the particles on the fold); and the
couplings at the fold decide unitarity: the chirality-blind fold operators (products of $\gamma^{(1)}, \dots, \gamma^{(4)}$) never connect
a physical state with a ghost at rest, the chiral ones (the same times $\Gamma_8$) always do, and the left-handed Higgs portal of the
author creates a physical particle $\chi$ with a ghost antiparticle with 0.89 times its elastic amplitude. With chiral couplings at
the fold UM-3 is therefore not a unitary quantum theory. Status: DERIVED.

# The Standard Model on the fold

## The four-dimensional couplings

$$
\begin{aligned}
&g_{1,\mathrm{eff}} = \frac{g_1}{\sqrt{\mathcal{Z}}},\quad g_{2,\mathrm{eff}} = \frac{g_2}{\sqrt{\mathcal{Z}}},\quad g_{3,\mathrm{eff}} = \frac{g_3}{\sqrt{\mathcal{Z}}},\qquad \lambda_{\mathrm{eff}} = \frac{\lambda}{\mathcal{Z}},\\
&\mathcal{Y}_{\mathrm{eff}} = \frac{\mathcal{Y}}{\sqrt{\mathcal{Z}}},\qquad G_{\mathrm{N,eff}} = \frac{G_{\mathrm{N}}}{\mathcal{Z}},\qquad
\mathcal{Z} = \frac{V_{\mathrm{t}}\big(\mathrm{e}^{-a_4}b_4\big)^3}{V_*}
\end{aligned} \tag{FE-44}
$$
<!-- symbols: geff, g1, g2, g3, Zfold, lameff, lamH, Yeff, Yuk, GNeff, GN, Vt, euler, a4, b4, Vstar -->
<!-- begin generated symbol list -->
**Symbols in (FE-44).**

- $g_{k,\mathrm{eff}}$: The effective (canonically normalised) gauge couplings of the fold when the fold factor is $\mathcal{Z}$, $g_{k,\mathrm{eff}} = g_k/\sqrt{\mathcal{Z}}$ ($k = 1, 2, 3$). Unit: dimensionless. Status: DERIVED.
- $g_1$: The $U(1)_Y$ gauge coupling (usually $g'$; not normalised for grand unification). Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling (the strong coupling $g_s$). Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($\alpha_s = 0.1180$). Status: STANDARD.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\lambda_{\mathrm{eff}}$: The effective quartic Higgs coupling, $\lambda/\mathcal{Z}$. Unit: dimensionless. Status: DERIVED.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $\mathcal{Y}_{\mathrm{eff}}$: The effective Yukawa matrices, $\mathcal{Y}/\sqrt{\mathcal{Z}}$ (for each of $\mathcal{Y}^{u}, \mathcal{Y}^{d}, \mathcal{Y}^{e}, \mathcal{Y}^{\nu}$). Unit: dimensionless. Status: DERIVED.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{N,eff}}$: The effective Newton constant of the fold, $G_{\mathrm{N}}/\mathcal{Z}$. Unit: GeV$^{-2}$. Status: DERIVED.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor of the extra times is $\mathrm{e}^{-a_4}b_4$ times the warp. Unit: dimensionless. Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.

<!-- end generated symbol list -->

When the extra times have the size $\mathrm{e}^{-a_4}b_4$, every term of the fold carries the factor $\mathcal{Z}$ (IN-8); rescaling every
field of the fold by $\sqrt{\mathcal{Z}}$ restores the canonical normalisation and leaves the effective couplings of FE-44, while
the masses (products of a coupling and a vacuum value) are unchanged. In the late universe $\mathcal{Z} = 1$ (frozen extra times,
FE-33); in the primordial era at the author's vacuum $\mathrm{e}^{-a_4}b_4 \propto \mathrm{e}^{-Hx_4}$, so $\mathcal{Z} \propto \mathrm{e}^{-3Hx_4}$ and
all couplings grow as $\mathrm{e}^{3Hx_4/2}$ until the extra times freeze. Status: DERIVED.

## The electroweak vacuum with the ad hoc component

$$
\begin{aligned}
&m_{\mathrm{W}}^2 = \frac{g_2^2\,(v^2 + \mathcal{A}^2)}{4},\qquad m_{\mathrm{Z}}^2 = \frac{(g_1^2 + g_2^2)(v^2 + \mathcal{A}^2)}{4},\qquad
 \frac{G_{\mathrm{F}}}{\sqrt2} = \frac{g_2^2}{8m_{\mathrm{W}}^2} = \frac{1}{2(v^2 + \mathcal{A}^2)},\qquad m_{h}^2 = 2\lambda v^2,\\
&A_\mu = \frac{g_2\,B_\mu - g_1\,n^I W^I_\mu}{\sqrt{g_1^2 + g_2^2}},\qquad
 n^I = \frac{\big(2\mathcal{A}v,\ 0,\ \mathcal{A}^2 - v^2\big)}{\mathcal{A}^2 + v^2}
\end{aligned} \tag{FE-45}
$$
<!-- symbols: mW, g2, vev, Aadhoc, mZ, g1, GF, mh, lamH, Aphoton, imu, Bhyp, nI, iI, Wsu2 -->
<!-- begin generated symbol list -->
**Symbols in (FE-45).**

- $m_{\mathrm{W}}$: The mass of the $W$ bosons. Unit: GeV. Value: 80.37 GeV ($\mathcal{A} = 0$). Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $m_{\mathrm{Z}}$: The mass of the $Z$ boson. Unit: GeV. Value: 91.19 GeV ($\mathcal{A} = 0$). Status: STANDARD.
- $g_1$: The $U(1)_Y$ gauge coupling (usually $g'$; not normalised for grand unification). Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $G_{\mathrm{F}}$: The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in FE-45 the Fermi constant of the ad hoc vacuum, which is $G_{\mathrm{F,loc}}$ of FE-49. Unit: GeV$^{-2}$. Value: $1.1664\times10^{-5}$ GeV$^{-2}$. Status: STANDARD.
- $m_h$: The mass of the Higgs boson. Unit: GeV. Value: 125.25 GeV (Particle Data Group 2022). Status: STANDARD.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $A_\mu$: The photon field: the massless combination of $W^1, W^2, W^3$ and $B$ (canonically normalised). Unit: GeV. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $B_\mu,\ B_{\mu\nu}$: The hypercharge gauge field of $U(1)_Y$ on the fold and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $n^I$: The unit isovector of the ad hoc vacuum, $n = (2\mathcal{A}v, 0, \mathcal{A}^2 - v^2)/(\mathcal{A}^2 + v^2)$, which fixes which combination of $W^1, W^2, W^3$ joins $B$ in the photon. Unit: dimensionless. Value: $(0, 0, -1)$ for $\mathcal{A} = 0$. Status: DERIVED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.

<!-- end generated symbol list -->

The masses of the gauge bosons and the photon in the author's ad hoc vacuum (the eigenvalues and eigenvectors of the mass matrix
of $W^1, W^2, W^3, B$ from $\lvert D_\mu\Phi\rvert^2$ with $\Phi = (\mathcal{A}, v)/\sqrt2$; DERIVED, `um3_fields.py`, F5): the vacuum value that
breaks the electroweak symmetry is $\sqrt{v^2 + \mathcal{A}^2}$, and the unbroken direction, the photon $A_\mu$, is rotated from the usual
combination by the unit isovector $n^I$ (for $\mathcal{A} = 0$: $n = (0, 0, -1)$ and $A_\mu = (g_2B_\mu + g_1W^3_\mu)/\sqrt{g_1^2 + g_2^2}$).
The Fermi constant measured in muon decay is that of the total vacuum value. As $\mathcal{A}$ decays (rate $2a_{40}$), the electroweak
vacuum becomes the Standard-Model vacuum. The Higgs mass is that of the Standard-Model vacuum ($\mathcal{A} \to 0$). Status: DERIVED.

## The masses and the mixing of quarks and leptons

$$
\begin{aligned}
&\frac{v}{\sqrt2}\,\mathcal{Y}^{u} = U_{u\mathrm{L}}\,\mathrm{diag}(m_u, m_c, m_t)\,U_{u\mathrm{R}}^\dagger,\qquad
 \frac{v}{\sqrt2}\,\mathcal{Y}^{d} = U_{d\mathrm{L}}\,\mathrm{diag}(m_d, m_s, m_b)\,U_{d\mathrm{R}}^\dagger,\\
&\frac{v}{\sqrt2}\,\mathcal{Y}^{e} = U_{e\mathrm{L}}\,\mathrm{diag}(m_e, m_\mu, m_\tau)\,U_{e\mathrm{R}}^\dagger,\qquad
 \frac{v}{\sqrt2}\,\mathcal{Y}^{\nu} = U_{\nu\mathrm{L}}\,\mathrm{diag}(m_1, m_2, m_3)\,U_{\nu\mathrm{R}}^\dagger,\\
&V_{\mathrm{CKM}} = U_{u\mathrm{L}}^\dagger U_{d\mathrm{L}},\qquad U_{\mathrm{PMNS}} = U_{e\mathrm{L}}^\dagger U_{\nu\mathrm{L}},\qquad
 \nu_\alpha = \sum_{i=1}^{3}\big(U_{\mathrm{PMNS}}\big)_{\alpha i}\,\nu_i,\\
&\mathcal{L}_{\mathrm{CC}} = \frac{g_2}{\sqrt2}\,W^+_\mu\Big(\bar{\hat u}_{\mathrm{L}}\,\hat\gamma^\mu V_{\mathrm{CKM}}\,\hat d_{\mathrm{L}}
 + \sum_\alpha\bar\nu_\alpha\,\hat\gamma^\mu\hat e_{\mathrm{L}\alpha}\Big) + \mathrm{h.c.},\qquad W^\pm_\mu = \frac{W^1_\mu \mp \mathrm{i}W^2_\mu}{\sqrt2}
\end{aligned} \tag{FE-46}
$$
<!-- symbols: vev, Yuk, Umix, diag, mferm, dagger, Ckm, Pmns, nugen, ialpha, ii, LCC, g2, Wsu2, imu, hatferm, gammahat, hc, imag -->
<!-- begin generated symbol list -->
**Symbols in (FE-46).**

- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $U_{f\mathrm{L}},\ U_{f\mathrm{R}}$: The unitary $3 \times 3$ matrices that diagonalise the mass matrices of the up quarks, the down quarks, the charged leptons and the neutrinos (left-handed and right-handed rotations). Unit: dimensionless. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-3 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 4.12 meV by DESI DR2 with the CMB. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $V_{\mathrm{CKM}}$: The quark mixing matrix (Cabibbo-Kobayashi-Maskawa). Unit: dimensionless. Status: STANDARD.
- $U_{\mathrm{PMNS}}$: The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; $U_{\alpha i}$ are its entries. Unit: dimensionless. Value: $\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, with the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$). Status: STANDARD, ASSUMED (the phase).
- $\nu_\alpha,\ \nu_i$: A neutrino field: $\nu_\alpha$ the flavour states ($\alpha = e, \mu, \tau$), $\nu_i$ the mass states ($i = 1, 2, 3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\alpha$: A lepton-flavour index, $\alpha \in \{e, \mu, \tau\}$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\mathcal{L}_{\mathrm{CC}}$: The charged-current interaction of the quarks and leptons with the $W$ bosons. Unit: GeV$^4$. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $W^I_\mu,\ W^I_{\mu\nu}$: The gauge field of $SU(2)_L$ on the fold, $W^1_\mu, W^2_\mu, W^3_\mu$, and its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\hat u_{\mathrm{L}},\ \hat d_{\mathrm{L}},\ \hat e_{\mathrm{L}\alpha}$: The left-handed quarks and charged leptons in the mass basis ($\hat e_{\mathrm{L}\alpha}$ the charged lepton of flavour $\alpha$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold, $\hat\gamma^\mu = \hat{\mathbf{e}}_a{}^\mu\hat\gamma^{(a)}$, $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{h.c.}$: The Hermitian conjugate of the preceding terms. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

The Dirac masses of the quarks, the charged leptons and the three neutrinos (in the vacuum with $\mathcal{A} = 0$; with $\mathcal{A} \ne 0$ the same
with the rotated vacuum), the unitary matrices that diagonalise the Yukawa matrices, the quark mixing matrix $V_{\mathrm{CKM}}$ and the
lepton mixing matrix $U_{\mathrm{PMNS}}$, and the charged-current interaction in the mass basis (fields with a hat; the neutrino flavour
states $\nu_\alpha$ are the partners of the charged leptons of definite mass). This is the flavour structure of the Standard Model with
three Dirac neutrinos; the portals of dirac16complex add nothing to it (they are flavour blind, IN-16). The values of the masses and
mixing angles are the measured ones (STANDARD inputs). Status: STANDARD.

## The four-dimensional couplings of the bound states of dirac16complex

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

The couplings of the bound states (the particles $\chi$ of mass $\omega_{\mathrm{b}}$) to the Standard Model, by the theorem of
Feynman and Hellmann: a slowly varying Standard-Model field shifts the strengths $\mu_X$ of FE-39 and with them the energy of the
bound state, so the coupling of the bound state to a Standard-Model operator is the derivative of $\omega_{\mathrm{b}}$ with respect to its
mean value (valid for momentum transfers small compared with $q_{\mathrm{b}}$). $\mathfrak{g}_{h\chi}$ is the Yukawa coupling of the Higgs boson
$h$ to the bound state ($\Delta\langle\Phi^\dagger\Phi\rangle = vh$), here for the Higgs portal alone; it is fixed by the mass of the bound
state and the bulk mass. The couplings to $W$ and $B$ follow like $\mathfrak{g}_{G}$; the dipole portal gives the bound states magnetic and
electric dipole moments. These couplings govern the annihilation (FE-61), the scattering on nuclei and the production of the
bound states. Status: DERIVED.

# The three neutrino flavours

The neutrinos are the upper components $\nu_{\mathrm{L}}$ of the three lepton doublets on the fold; with the three right-handed
neutrinos they have Dirac masses and the lepton mixing of FE-46. Their flavour conversion follows from FE-22 and FE-24 for
neutrinos that propagate through a medium of electrons, nucleons, other neutrinos and dirac16complex, by the standard reduction of
the Dirac equations of ultrarelativistic neutrinos to equations for their flavour content (the mean-field quantum kinetic equations
of Sigl and Raffelt, 1993). The author asks for correct flavour conversion because it shapes the fate of core-collapse supernovae:
Gogilashvili and Tamborra ("Neutrino Flavor Conversion Shapes the Rate of Failed Core-collapse Supernovae", arXiv:2605.16504v3)
simulate the collapse of 195 stars of 9 to 120 solar masses and find that flavour equipartition below a critical baryon density
raises the fraction of failed explosions from 25.6% (without flavour conversion) to 50.8%, 77.4%, 93.3% and 96.4% for critical
densities of $10^9$, $10^{10}$, $10^{11}$ and $10^{13}$ g/cm$^3$ (from 27.0% to between 47.6% and 88.3% when the stars are weighted
with the Salpeter initial mass function). This section writes the equations of motion of the flavour content and shows exactly
which terms UM-3 adds to those of the Standard Model.

## The equations of motion of the flavour content

$$
\begin{aligned}
&\mathrm{i}\big(\partial_{x_4} + \hat v\cdot\vec\nabla\big)\varrho_{\vec p} = \big[\mathsf{H}_{\vec p},\ \varrho_{\vec p}\big] + \mathrm{i}\,\mathcal{C}_{\vec p},\qquad
 \mathrm{i}\big(\partial_{x_4} + \hat v\cdot\vec\nabla\big)\bar\varrho_{\vec p} = \big[\bar{\mathsf{H}}_{\vec p},\ \bar\varrho_{\vec p}\big] + \mathrm{i}\,\bar{\mathcal{C}}_{\vec p},\\
&\mathsf{H}_{\vec p} = \frac{v_{\mathrm{loc}}^2}{v^2}\,\frac{U_{\mathrm{PMNS}}\,\mathsf{M}^2\,U_{\mathrm{PMNS}}^\dagger}{2E} + \mathsf{V}_{\mathrm{m}} + \mathsf{V}_{\nu\nu} + V_\Psi\mathbf{1},\qquad
 \mathsf{M}^2 = \mathrm{diag}\big(m_1^2,\ m_2^2,\ m_3^2\big),\\
&\bar{\mathsf{H}}_{\vec p} = -\frac{v_{\mathrm{loc}}^2}{v^2}\,\frac{U_{\mathrm{PMNS}}\,\mathsf{M}^2\,U_{\mathrm{PMNS}}^\dagger}{2E} + \mathsf{V}_{\mathrm{m}} + \mathsf{V}_{\nu\nu} + V_\Psi\mathbf{1}
\end{aligned} \tag{FE-48}
$$
<!-- symbols: imag, partial, x4, vhat, nablavec, rhoflav, pvec, Hflav, Ccoll, vloc, vev, Pmns, dagger, Mmass, Eorb, Vm, Vnunu, VPsi, identity, diag, mferm -->
<!-- begin generated symbol list -->
**Symbols in (FE-48).**

- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\hat v,\ \hat v^\mu$: The direction of motion of a neutrino: the unit vector $\hat v = \vec p/\lvert\vec p\rvert$ ($\hat v_{\vec p}$, $\hat v_{\vec q}$ for the momenta $\vec p$, $\vec q$), and the four-vector $\hat v^\mu = (1, \hat v)$ in the order $(x_4; x_1, x_2, x_3)$; $\mathrm{d}^2\hat v$ is the element of solid angle of the directions. Unit: dimensionless. Status: STANDARD.
- $\vec\nabla$: The gradient along ordinary space, $\vec\nabla = (\partial_{x_1}, \partial_{x_2}, \partial_{x_3})$ (in the local frame of the medium). Unit: 1/length. Status: STANDARD.
- $\varrho_{\vec p},\ \bar\varrho_{\vec p}$: The $3 \times 3$ flavour density matrices of the neutrinos and of the antineutrinos of momentum $\vec p$ in the basis $e, \mu, \tau$: the diagonal entries are the occupation numbers of the three flavours, the off-diagonal entries the coherence between the flavours; $\bar\varrho$ is defined with the flavour indices in the reversed order, so that it obeys an equation of the same form. Unit: dimensionless. Status: STANDARD.
- $\vec p$: The momentum of a neutrino (three components along ordinary space, in the rest frame of the medium); $\lvert\vec p\rvert = E$ for a neutrino of negligible mass. Unit: GeV. Status: STANDARD.
- $\mathsf{H}_{\vec p},\ \bar{\mathsf{H}}_{\vec p}$: The flavour Hamiltonians ($3 \times 3$ Hermitian matrices) of the neutrinos and of the antineutrinos of momentum $\vec p$. Unit: GeV. Status: STANDARD.
- $\mathcal{C}_{\vec p},\ \bar{\mathcal{C}}_{\vec p}$: The collision terms ($3 \times 3$ matrices) of the neutrinos and the antineutrinos of momentum $\vec p$: the rates of change of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$ by emission, absorption, scattering and pair processes with the matter. Unit: GeV. Status: STANDARD.
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $U_{\mathrm{PMNS}}$: The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; $U_{\alpha i}$ are its entries. Unit: dimensionless. Value: $\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, with the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$). Status: STANDARD, ASSUMED (the phase).
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathsf{M}^2$: The diagonal matrix of the squared masses of the three neutrino mass states, $\mathsf{M}^2 = \mathrm{diag}(m_1^2, m_2^2, m_3^2)$ ($\mathsf{M}$ appears only squared). Unit: GeV$^2$ (of $\mathsf{M}^2$). Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $\mathsf{V}_{\mathrm{m}}$: The matter potential of the neutrinos (a $3 \times 3$ matrix in flavour space) from their forward scattering on the electrons, positrons and neutrons of the medium. Unit: GeV. Status: STANDARD.
- $\mathsf{V}_{\nu\nu}$: The neutrino-neutrino potential (a $3 \times 3$ matrix in flavour space) from the forward scattering of a neutrino on the other neutrinos and antineutrinos of the medium; it depends on their flavour content and their directions. Unit: GeV. Status: STANDARD.
- $V_\Psi$: The potential energy that dirac16complex gives every neutrino through the current portal of the lepton doublets, $V_\Psi = \mathcal{V}^{\ell}_{x_4}$ (the same for the three flavours). Unit: GeV. Status: DERIVED.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-3 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 4.12 meV by DESI DR2 with the CMB. Status: STANDARD.

<!-- end generated symbol list -->

The equations of motion of the $3 \times 3$ flavour density matrices of the neutrinos ($\varrho_{\vec p}$) and of the antineutrinos
($\bar\varrho_{\vec p}$, defined with the flavour indices in the reversed order) of momentum $\vec p$, energy $E = \lvert\vec p\rvert$ and
direction $\hat v$; the diagonal entries are the occupation numbers of the three flavours, the off-diagonal entries the coherence
between them. Free streaming stands on the left, the commutator with the flavour Hamiltonian and the collisions $\mathcal{C}$
(emission, absorption, scattering and pair processes) on the right. The Hamiltonian contains the vacuum term of the three Dirac
masses (with the opposite sign for antineutrinos in this convention), multiplied by $v_{\mathrm{loc}}^2/v^2$ because the masses are the
Yukawa couplings times the local value of the Higgs field (FE-49); the matter potential; the neutrino-neutrino potential; and the
potential $V_\Psi$ of dirac16complex. Status: STANDARD (UM-3 adds $V_\Psi$ and the factor $v_{\mathrm{loc}}^2/v^2$).

$$
\begin{aligned}
&\mathsf{V}_{\mathrm{m}} = \sqrt2\,G_{\mathrm{F,loc}}\,\mathrm{diag}\big(n_e - n_{\bar e},\ 0,\ 0\big) - \frac{G_{\mathrm{F,loc}}}{\sqrt2}\,n_n\mathbf{1},\qquad
 \mathsf{V}_{\nu\nu} = \sqrt2\,G_{\mathrm{F,loc}}\int\frac{\mathrm{d}^3\vec q}{(2\pi)^3}\big(1 - \hat v_{\vec p}\cdot\hat v_{\vec q}\big)\big(\varrho_{\vec q} - \bar\varrho_{\vec q}\big),\\
&V_\Psi = \mathcal{V}^{\ell}_{x_4} = \sum_X c^{\ell}_X\,j_{X\,x_4},\qquad G_{\mathrm{F,loc}} = \frac{1}{\sqrt2\,v_{\mathrm{loc}}^2},\\
&v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle,\qquad v_{\mathrm{loc}}^2 = v^2 + \mathcal{A}^2\ \ \text{(the ad hoc vacuum)},\\
&v_{\mathrm{loc}}^2 = v^2 - \frac{c_\Phi}{\lambda}\,\langle\bar\Psi P_{\mathrm{L}}\Psi\rangle\ \ \text{(the relaxed vacuum with dirac16complex)}
\end{aligned} \tag{FE-49}
$$
<!-- symbols: Vm, GFloc, diag, ne, nebar, nn, identity, Vnunu, diff, qvec, pi, vhat, pvec, rhoflav, VPsi, Vport, x4, iX, cf, jcur, vloc, Phi, dagger, mean, vev, Aadhoc, cPhi, lamH, Psi, PL -->
<!-- begin generated symbol list -->
**Symbols in (FE-49).**

- $\mathsf{V}_{\mathrm{m}}$: The matter potential of the neutrinos (a $3 \times 3$ matrix in flavour space) from their forward scattering on the electrons, positrons and neutrons of the medium. Unit: GeV. Status: STANDARD.
- $G_{\mathrm{F,loc}}$: The local Fermi constant, $G_{\mathrm{F,loc}} = 1/(\sqrt2\,v_{\mathrm{loc}}^2)$ ($= G_{\mathrm{F}}$ where $v_{\mathrm{loc}} = v$). Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $n_e$: The number density of electrons (bound and free; in a supernova all are free, in the recombining universe $x_{\mathrm{e}}n_e$ is the density of the free electrons). Unit: GeV$^3$ (cm$^{-3}$). Status: STANDARD.
- $n_{\bar e}$: The number density of positrons. Unit: GeV$^3$. Status: STANDARD.
- $n_n$: The number density of neutrons. Unit: GeV$^3$. Status: STANDARD.
- $\mathbf{1}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space). Unit: dimensionless. Status: STANDARD.
- $\mathsf{V}_{\nu\nu}$: The neutrino-neutrino potential (a $3 \times 3$ matrix in flavour space) from the forward scattering of a neutrino on the other neutrinos and antineutrinos of the medium; it depends on their flavour content and their directions. Unit: GeV. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\vec q$: The momentum of another neutrino of the medium (the integration variable of the neutrino-neutrino potential); $\mathrm{d}^3\vec q$ its volume element. Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\hat v,\ \hat v^\mu$: The direction of motion of a neutrino: the unit vector $\hat v = \vec p/\lvert\vec p\rvert$ ($\hat v_{\vec p}$, $\hat v_{\vec q}$ for the momenta $\vec p$, $\vec q$), and the four-vector $\hat v^\mu = (1, \hat v)$ in the order $(x_4; x_1, x_2, x_3)$; $\mathrm{d}^2\hat v$ is the element of solid angle of the directions. Unit: dimensionless. Status: STANDARD.
- $\vec p$: The momentum of a neutrino (three components along ordinary space, in the rest frame of the medium); $\lvert\vec p\rvert = E$ for a neutrino of negligible mass. Unit: GeV. Status: STANDARD.
- $\varrho_{\vec p},\ \bar\varrho_{\vec p}$: The $3 \times 3$ flavour density matrices of the neutrinos and of the antineutrinos of momentum $\vec p$ in the basis $e, \mu, \tau$: the diagonal entries are the occupation numbers of the three flavours, the off-diagonal entries the coherence between the flavours; $\bar\varrho$ is defined with the flavour indices in the reversed order, so that it obeys an equation of the same form. Unit: dimensionless. Status: STANDARD.
- $V_\Psi$: The potential energy that dirac16complex gives every neutrino through the current portal of the lepton doublets, $V_\Psi = \mathcal{V}^{\ell}_{x_4}$ (the same for the three flavours). Unit: GeV. Status: DERIVED.
- $\mathcal{V}^{f}_\mu$: The vector potential that dirac16complex exerts on the Standard-Model fermions of kind $f$ through the current portals, $\mathcal{V}^{f}_\mu = \sum_Xc^{f}_Xj_{X\mu}$ ($\mathcal{V}^{Q}, \mathcal{V}^{u}, \dots, \mathcal{V}^{\nu}$ for the six kinds); flavour blind. Unit: GeV. Status: DERIVED.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $j_X^\mu$: The convective current of the half $X$ of dirac16complex, $j_X^\mu = \mathrm{i}(\bar\Psi P_XD^\mu\Psi - (D^\mu\bar\Psi)P_X\Psi)$ (real and joining the half with itself, DERIVED). Unit: GeV$^8$. Status: DERIVED.
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

The potentials and the local electroweak vacuum. Forward scattering on electrons and positrons through $W$ exchange gives the
electron flavour the potential $\sqrt2G_{\mathrm{F,loc}}(n_e - n_{\bar e})$; neutral currents give all flavours the same potential, here
from the neutrons (the neutral-current potentials of electrons and protons cancel in neutral matter for any weak mixing angle);
forward scattering on the other neutrinos gives the neutrino-neutrino potential, which depends on the flavour content and the
directions of all other neutrinos and makes the equations non-linear. dirac16complex acts on the neutrinos in exactly two ways,
both fixed by the action (IN-16):

* through the current portal of the lepton doublets: $V_\Psi$ is the time component of the vector potential $\mathcal{V}^{\ell}_\mu$
  of FE-22, the same for the three flavours because the portals are flavour blind. A multiple of the unit matrix drops out of every
  commutator: $V_\Psi$ shifts the energies of the neutrinos but does not change their flavour;
* through the Higgs portal: the scalar density of the left-handed half shifts the mass parameter of the Higgs field (FE-15). Where the
  Higgs field relaxes to the minimum of its potential (a homogeneous, static vacuum with $\mathcal{A} = 0$ in FE-15), its local value
  is $v_{\mathrm{loc}}^2 = v^2 - c_\Phi\langle\bar\Psi P_{\mathrm{L}}\Psi\rangle/\lambda$; in the author's ad hoc vacuum $v_{\mathrm{loc}}^2 = v^2 + \mathcal{A}^2$ (FE-45).
  All masses scale with $v_{\mathrm{loc}}/v$ and the Fermi constant with $v^2/v_{\mathrm{loc}}^2$ (at tree level $G_{\mathrm{F}} = 1/(\sqrt2 v^2)$
  does not depend on the gauge couplings, so the gauge-kinetic portals do not change it), while the Yukawa matrices, and with them
  $U_{\mathrm{PMNS}}$, are unchanged.

So dirac16complex changes neither the mixing angles nor the flavour pattern of the conversion: it rescales the vacuum oscillation
frequencies by $v_{\mathrm{loc}}^2/v^2$ and the potentials by $v^2/v_{\mathrm{loc}}^2$ (the resonance density of FE-50 by $v_{\mathrm{loc}}^4/v^4$).
In the late universe $\mathcal{A} = 0$, and the dark matter is far too dilute to move $v_{\mathrm{loc}}$: with FE-47 the shift is
$\Delta v^2/v^2 = -\mathfrak{g}_{h\chi}\rho_\chi/(\lambda v^3\omega_{\mathrm{b}})$, about $10^{-50}\,\mathfrak{g}_{h\chi}$ for the local dark-matter
density $0.3$ GeV/cm$^3$ and $\omega_{\mathrm{b}} = 100$ GeV. The flavour conversion of UM-3 is therefore that of the Standard Model with three
Dirac neutrinos wherever $v_{\mathrm{loc}} = v$, which includes every supernova and the Sun (DERIVED). The Dirac neutrinos of UM-3 have the
magnetic moments of the Standard Model, about $3.2\times10^{-19}$ Bohr magnetons times the mass in eV, too small to turn left-handed into
right-handed neutrinos in the magnetic fields of supernovae; the dipole portal does not act on neutrinos directly. Status: STANDARD
(the potentials), DERIVED ($V_\Psi$, $v_{\mathrm{loc}}$ and their consequences; `um3_neutrino.py`, N1).

## Matter-enhanced conversion

$$
\begin{aligned}
&\tan2\theta_{\mathrm{m}} = \frac{\sin2\theta}{\cos2\theta - 2EV_{\mathrm{CC}}/\Delta m^2},\qquad
 V_{\mathrm{CC}} = \sqrt2\,G_{\mathrm{F,loc}}\,n_e,\qquad
 n_{e,\mathrm{res}} = \frac{\Delta m^2\cos2\theta}{2\sqrt2\,G_{\mathrm{F,loc}}\,E},\\
&P_{\mathrm{LZ}} = \exp\Big(-\frac{\pi}{2}\,\frac{\Delta m^2\sin^22\theta}{2E\cos2\theta}\,\Big\lvert\frac{\mathrm{d}\ln n_e}{\mathrm{d}r}\Big\rvert^{-1}_{\mathrm{res}}\Big)
\end{aligned} \tag{FE-50}
$$
<!-- symbols: thetam, thetamix, Eorb, VCC, Delta, mmass, GFloc, ne, neres, PLZ, pi, diff, rrad, res -->
<!-- begin generated symbol list -->
**Symbols in (FE-50).**

- $\theta_{\mathrm{m}}$: The mixing angle of two neutrino flavours in matter. Unit: dimensionless. Status: STANDARD.
- $\theta$: The vacuum mixing angle of two neutrino flavours (in the two-flavour description of a resonance, one of the three angles $\theta_{12}, \theta_{13}, \theta_{23}$ of $U_{\mathrm{PMNS}}$). Unit: dimensionless. Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $V_{\mathrm{CC}}$: The charged-current matter potential of the electron neutrinos (forward scattering on electrons through $W$ exchange). Unit: GeV. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; in $\Delta m^2$ the squared-mass difference of two neutrino mass states ($m_2^2 - m_1^2$ for the two states of a resonance, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1). Unit: GeV. Status: STANDARD.
- $G_{\mathrm{F,loc}}$: The local Fermi constant, $G_{\mathrm{F,loc}} = 1/(\sqrt2\,v_{\mathrm{loc}}^2)$ ($= G_{\mathrm{F}}$ where $v_{\mathrm{loc}} = v$). Unit: GeV$^{-2}$. Status: DERIVED.
- $n_e$: The number density of electrons (bound and free; in a supernova all are free, in the recombining universe $x_{\mathrm{e}}n_e$ is the density of the free electrons). Unit: GeV$^3$ (cm$^{-3}$). Status: STANDARD.
- $n_{e,\mathrm{res}}$: The electron density at which the flavour conversion in matter is resonant (the Mikheyev-Smirnov-Wolfenstein resonance). Unit: GeV$^3$. Status: STANDARD.
- $P_{\mathrm{LZ}}$: The probability that a neutrino jumps between the eigenstates of matter at the resonance (Landau-Zener); $P_{\mathrm{LZ}} = 0$ is an adiabatic resonance. Unit: dimensionless. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $r$: The distance from the centre of the star along the path of a neutrino. Unit: length. Status: STANDARD.
- $\mathrm{res}$: The label of a quantity evaluated at the resonance, where $n_e = n_{e,\mathrm{res}}$. Status: STANDARD.

<!-- end generated symbol list -->

The resonant flavour conversion in matter (Mikheyev-Smirnov-Wolfenstein) for two flavours with the vacuum mixing angle $\theta$ and
the squared-mass difference $\Delta m^2$ (which includes the factor $v_{\mathrm{loc}}^2/v^2$ of FE-48): the mixing angle in matter
$\theta_{\mathrm{m}}$ (FE-48 with the diagonal potential $V_{\mathrm{CC}}$ in the electron flavour), the electron density of the resonance, where
$\theta_{\mathrm{m}} = 45^\circ$, and the probability $P_{\mathrm{LZ}}$ that the neutrino jumps between the eigenstates of matter at the resonance
for the density profile $n_e(r)$ along its path (the Landau-Zener formula, exact for a linear profile). With the measured masses and
mixing angles this gives the survival probability of solar neutrinos and the conversion in the outer layers of supernovae (the
resonances of $\Delta m^2_{31}$ and $\Delta m^2_{21}$). Status: STANDARD (`um3_neutrino.py`, N2).

## The fast flavour instability of dense neutrino gases

$$
\begin{aligned}
&\mathcal{G}_{\mathrm{ELN}}(\hat v) = \sqrt2\,G_{\mathrm{F,loc}}\int_0^\infty\frac{E^2\,\mathrm{d}E}{(2\pi)^3}\Big[\mathcal{F}_{e} - \bar{\mathcal{F}}_{e}
 - \big(\mathcal{F}_{x} - \bar{\mathcal{F}}_{x}\big)\Big],\\
&\det\Big[\eta_{\mathrm{M}}^{\mu\nu} + \int\mathrm{d}^2\hat v\;\mathcal{G}_{\mathrm{ELN}}(\hat v)\,
 \frac{\hat v^\mu\hat v^\nu}{\Omega_{\mathrm{fw}} - \vec K\cdot\hat v}\Big] = 0,\qquad \hat v^\mu = (1,\ \hat v)
\end{aligned} \tag{FE-51}
$$
<!-- symbols: GELN, vhat, GFloc, infty, Eorb, diff, pi, Focc, etaM, imu, inu, Omegafw, Kvec -->
<!-- begin generated symbol list -->
**Symbols in (FE-51).**

- $\mathcal{G}_{\mathrm{ELN}}(\hat v)$: The angular distribution of the electron lepton number carried by the neutrinos minus that carried by the heavy-lepton neutrinos, per unit solid angle of the direction $\hat v$, multiplied by $\sqrt2G_{\mathrm{F,loc}}$. Unit: GeV. Status: STANDARD.
- $\hat v,\ \hat v^\mu$: The direction of motion of a neutrino: the unit vector $\hat v = \vec p/\lvert\vec p\rvert$ ($\hat v_{\vec p}$, $\hat v_{\vec q}$ for the momenta $\vec p$, $\vec q$), and the four-vector $\hat v^\mu = (1, \hat v)$ in the order $(x_4; x_1, x_2, x_3)$; $\mathrm{d}^2\hat v$ is the element of solid angle of the directions. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{F,loc}}$: The local Fermi constant, $G_{\mathrm{F,loc}} = 1/(\sqrt2\,v_{\mathrm{loc}}^2)$ ($= G_{\mathrm{F}}$ where $v_{\mathrm{loc}} = v$). Unit: GeV$^{-2}$. Status: DERIVED.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathcal{F}_{e},\ \bar{\mathcal{F}}_{e},\ \mathcal{F}_{x},\ \bar{\mathcal{F}}_{x}$: The occupation numbers of the electron neutrinos, of the electron antineutrinos, and of one heavy-lepton neutrino and antineutrino ($x = \mu$ or $\tau$), as functions of the energy $E$ and the direction $\hat v$ (the diagonal entries of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$); in a transport code, the same for the number of particles in an energy bin. Unit: dimensionless. Status: STANDARD.
- $\eta_{\mathrm{M}}^{\mu\nu}$: The Minkowski metric of the four-vectors $\hat v^\mu$, $\eta_{\mathrm{M}} = \mathrm{diag}(1, -1, -1, -1)$ in the order $(x_4; x_1, x_2, x_3)$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\Omega_{\mathrm{fw}}$: The (complex) frequency of a flavour wave of the neutrino gas, measured from the shift caused by the potentials; an imaginary part greater than zero is an instability. Unit: GeV. Status: STANDARD.
- $\vec K$: The (real) wave vector of a flavour wave of the neutrino gas, measured from the shift caused by the potentials. Unit: GeV. Status: STANDARD.

<!-- end generated symbol list -->

The fast flavour instability (STANDARD: FE-48 linearised in the flavour coherence, without the vacuum term, which is negligible
in the dense gas; Izaguirre, Raffelt and Tamborra 2017). $\mathcal{G}_{\mathrm{ELN}}$ is the angular distribution of the electron lepton
number carried by the neutrinos minus that of the heavy-lepton flavours ($\mathcal{F}$ the occupation numbers of $\nu_e$, $\bar\nu_e$
and of one heavy flavour $\nu_x$, $\bar\nu_x$, as functions of the energy and the direction; $\mathrm{d}^2\hat v$ the element of solid
angle). A small flavour coherence $\propto \mathrm{e}^{-\mathrm{i}(\Omega_{\mathrm{fw}}x_4 - \vec K\cdot\vec x)}$ grows exponentially if the
dispersion relation (the second line, written with the Minkowski metric $\eta_{\mathrm{M}}$ of the four-vectors $\hat v^\mu$) has a solution
with an imaginary part of $\Omega_{\mathrm{fw}}$ greater than zero for a real wave vector $\vec K$ (the frequency and the wave vector are
measured from the shifts that the matter and the neutrino-neutrino potentials cause, which drop out). This happens if and only if
$\mathcal{G}_{\mathrm{ELN}}$ changes sign as a function of the direction, an angular crossing (Morinaga 2022). The instability then grows on
lengths of the order of $1/(\sqrt2G_{\mathrm{F}}n_\nu)$, centimetres in a supernova core, much shorter than the scales of the explosion, and
drives the flavours toward equipartition; transport codes therefore model its outcome by a prescription such as FE-52. Status:
STANDARD (`um3_neutrino.py`, N3).

$$
\begin{aligned}
&\mathcal{F}_{e} \to \mathcal{F}_{e} - \delta_{\mathrm{FC}},\qquad \bar{\mathcal{F}}_{e} \to \bar{\mathcal{F}}_{e} - \delta_{\mathrm{FC}},\qquad
 \mathcal{F}_{x} = \bar{\mathcal{F}}_{x} \to \mathcal{F}_{x} + \frac{\delta_{\mathrm{FC}}}{2},\\
&\delta_{\mathrm{FC}} = \max\Big(\frac23\Big(\min\big(\mathcal{F}_{e},\ \bar{\mathcal{F}}_{e}\big) - \mathcal{F}_{x}\Big),\ \max\big(\mathcal{F}_{e},\ \bar{\mathcal{F}}_{e}\big) - 1\Big),\\
&\text{applied where}\ \ \rho_{\mathrm{b}} < \rho_{\mathrm{FC}}\ \ \text{and}\ \ x_4 - x_{4,\mathrm{b}} > t_{\mathrm{FC}}
\end{aligned} \tag{FE-52}
$$
<!-- symbols: Focc, deltaFC, rhob, rhoFC, x4, x4b, tFC -->
<!-- begin generated symbol list -->
**Symbols in (FE-52).**

- $\mathcal{F}_{e},\ \bar{\mathcal{F}}_{e},\ \mathcal{F}_{x},\ \bar{\mathcal{F}}_{x}$: The occupation numbers of the electron neutrinos, of the electron antineutrinos, and of one heavy-lepton neutrino and antineutrino ($x = \mu$ or $\tau$), as functions of the energy $E$ and the direction $\hat v$ (the diagonal entries of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$); in a transport code, the same for the number of particles in an energy bin. Unit: dimensionless. Status: STANDARD.
- $\delta_{\mathrm{FC}}$: The occupation (or number per energy bin) of electron neutrino-antineutrino pairs converted into heavy-lepton pairs by the flavour equipartition FE-52; a negative value converts heavy-lepton pairs into electron pairs. Unit: dimensionless. Status: ASSUMED.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $\rho_{\mathrm{FC}}$: The baryon density below which the flavour equipartition FE-52 is applied (the critical density $\rho_{\mathrm{c}}$ of Gogilashvili and Tamborra). Unit: GeV$^4$ (g/cm$^3$). Value: $10^9$, $10^{10}$, $10^{11}$ or $10^{13}$ g/cm$^3$. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_{4,\mathrm{b}}$: The time of the bounce of the collapsing stellar core. Unit: length (= time). Status: STANDARD.
- $t_{\mathrm{FC}}$: The time after the bounce from which the flavour equipartition FE-52 is applied. Unit: time. Value: 0.02 s. Status: STANDARD.

<!-- end generated symbol list -->

The flavour equipartition that models the outcome of the fast instability in the transport of a core-collapse supernova, written in
the form that satisfies the constraints stated by Gogilashvili and Tamborra for their scheme: in every energy bin (and in the same way
for the flux of every energy bin) electron neutrino-antineutrino pairs are converted into heavy-lepton pairs, which conserves the
electron lepton number $\mathcal{F}_{e} - \bar{\mathcal{F}}_{e}$, the number of neutrinos $\mathcal{F}_{e} + 2\mathcal{F}_{x}$, the number of
antineutrinos $\bar{\mathcal{F}}_{e} + 2\mathcal{F}_{x}$ and the momentum, with the four heavy-lepton species equal as in the transport
($\mathcal{F}_{x} = \bar{\mathcal{F}}_{x}$). The amount $\delta_{\mathrm{FC}}$ brings the less abundant of $\nu_e$ and $\bar\nu_e$ into equipartition with
the heavy-lepton flavours (complete equipartition of all six species is impossible when the electron lepton number is not zero,
because flavour conversion conserves it); the second argument of the maximum keeps every occupation number at most 1 (the Pauli
principle) when heavy-lepton pairs are converted into electron pairs, and every occupation number stays between 0 and 1. The map is applied where the baryon density is below $\rho_{\mathrm{FC}}$ (their $\rho_{\mathrm{c}}$, varied
from $10^9$ to $10^{13}$ g/cm$^3$) and from $t_{\mathrm{FC}} = 0.02$ s after the bounce of the core at $x_{4,\mathrm{b}}$. In UM-3, FE-48 and
FE-49 are those of the Standard Model wherever $v_{\mathrm{loc}} = v$, so the prescription and its consequences carry over unchanged: the
supernova physics of UM-3 is that of the Standard Model with three Dirac neutrinos, and the failed-explosion fractions of the paper
apply (DERIVED from FE-49). Status: STANDARD (the constraints), ASSUMED (this explicit form), DERIVED (its validity in UM-3;
`um3_neutrino.py`, N4).

## Neutrinos in the expanding universe

$$
\begin{aligned}
&\Big(\partial_{x_4} - a_4'\,\lvert\vec p\rvert\,\frac{\partial}{\partial\lvert\vec p\rvert}\Big)\varrho_{\vec p}
 = -\mathrm{i}\big[\mathsf{H}_{\vec p},\ \varrho_{\vec p}\big] + \mathcal{C}_{\vec p},\\
&N_{\mathrm{eff}} = \frac87\Big(\frac{11}{4}\Big)^{4/3}\frac{\rho_\nu}{\rho_\gamma},\qquad
 \mathsf{T}_\nu^{(0)} = \Big(\frac{4}{11}\Big)^{1/3}\mathsf{T}_\gamma^{(0)},\qquad
 n_\nu^{(0)} = \frac{3\zeta(3)}{2\pi^2}\big(\mathsf{T}_\nu^{(0)}\big)^3
\end{aligned} \tag{FE-53}
$$
<!-- symbols: partial, x4, a4, prime, pvec, rhoflav, imag, Hflav, Ccoll, Neff, rhonu, rhogamma, Tnu, Tgamma, nnu, zeta, pi -->
<!-- begin generated symbol list -->
**Symbols in (FE-53).**

- $\partial$: A partial derivative: $\partial_M$ with respect to the coordinate $X^M$, $\partial_\mu$ with respect to $x^\mu$, $\partial_\sigma$ with respect to $\sigma$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\vec p$: The momentum of a neutrino (three components along ordinary space, in the rest frame of the medium); $\lvert\vec p\rvert = E$ for a neutrino of negligible mass. Unit: GeV. Status: STANDARD.
- $\varrho_{\vec p},\ \bar\varrho_{\vec p}$: The $3 \times 3$ flavour density matrices of the neutrinos and of the antineutrinos of momentum $\vec p$ in the basis $e, \mu, \tau$: the diagonal entries are the occupation numbers of the three flavours, the off-diagonal entries the coherence between the flavours; $\bar\varrho$ is defined with the flavour indices in the reversed order, so that it obeys an equation of the same form. Unit: dimensionless. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\mathsf{H}_{\vec p},\ \bar{\mathsf{H}}_{\vec p}$: The flavour Hamiltonians ($3 \times 3$ Hermitian matrices) of the neutrinos and of the antineutrinos of momentum $\vec p$. Unit: GeV. Status: STANDARD.
- $\mathcal{C}_{\vec p},\ \bar{\mathcal{C}}_{\vec p}$: The collision terms ($3 \times 3$ matrices) of the neutrinos and the antineutrinos of momentum $\vec p$: the rates of change of $\varrho_{\vec p}$ and $\bar\varrho_{\vec p}$ by emission, absorption, scattering and pair processes with the matter. Unit: GeV. Status: STANDARD.
- $N_{\mathrm{eff}}$: The effective number of neutrino species: the energy density of the relativistic particles other than photons in units of that of one neutrino species whose temperature is $(4/11)^{1/3}$ times that of the photons. Unit: dimensionless. Value: 3.044 (Standard Model); measured $2.99 \pm 0.17$ (Planck 2018). Status: STANDARD.
- $\rho_\nu$: The energy density of the neutrinos and antineutrinos of all flavours. Unit: GeV$^4$. Status: STANDARD.
- $\rho_\gamma$: The energy density of the photons. Unit: GeV$^4$. Status: STANDARD.
- $\mathsf{T}_\nu$: The temperature of the cosmic neutrino background; $\mathsf{T}_\nu^{(0)}$ its value today. Unit: GeV (or K). Value: 1.945 K today. Status: STANDARD.
- $\mathsf{T}_\gamma$: The temperature of the photons (of the CMB); $\mathsf{T}_\gamma^{(0)}$ its value today. Unit: GeV (or K). Value: 2.7255 K today. Status: STANDARD.
- $n_\nu$: The number density of the cosmic neutrino background per flavour (neutrinos plus antineutrinos, one helicity each); $n_\nu^{(0)}$ its value today. Unit: GeV$^3$. Value: 112 cm$^{-3}$ today. Status: STANDARD.
- $\zeta$: The Riemann zeta function; $\zeta(3) = 1.2020569$. Unit: dimensionless. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

The neutrinos in the homogeneous, isotropic, expanding fold (the momentum redshifts with the expansion rate $a_4'$) and the cosmic
neutrino background (CNB); the superscript $(0)$ marks a value today. Until the temperature falls to about 1 MeV the collisions keep
the neutrinos in equilibrium with the plasma; they then decouple, the annihilation of electrons and positrons heats the photons, and
the effective number of neutrino species is $N_{\mathrm{eff}} = 3.044$ in the Standard Model (with the small heating of the neutrinos and the
flavour conversion during decoupling included). Today the CNB has the temperature $\mathsf{T}_\nu^{(0)} = 1.945$ K and $n_\nu^{(0)} = 112$
neutrinos and antineutrinos per cm$^3$ and flavour (one helicity each: the right-handed states of the Dirac neutrinos are not populated
by the Standard-Model collisions). The right-handed neutrinos add to $N_{\mathrm{eff}}$ only if something else brings them into equilibrium
(FE-62). Status: STANDARD (`um3_neutrino.py`, N5).

# The cosmological perturbations

The CMB, the CNB and the BAO are computed on the fold, where four-dimensional gravity is general relativity with $G_{\mathrm{N}}$ (FE-59)
up to corrections of order $\epsilon_{\mathrm{r}}$, the matter is that of the Standard Model, the dark matter is the bound states $\chi$ of
dirac16complex, and the dark energy is the vacuum energy $\rho_\Lambda$ of the fold (FE-59). The metric of the fold is the background plus
the first-order cosmological term of the power series FE-35 (order $\epsilon_{\mathrm{c}}$); the equations are those of Ma and Bertschinger
(1995) in the conformal Newtonian gauge, written out here.

$$
\begin{aligned}
&\hat h_{\mu\nu}\,\mathrm{d}x^\mu\mathrm{d}x^\nu = a^2\Big[-(1 + 2\psi_{\mathrm{B}})\,\mathrm{d}\tau_{\mathrm{c}}^2
 + (1 - 2\phi_{\mathrm{B}})\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)\Big],\\
&a = \mathrm{e}^{a_4},\qquad \mathrm{d}\tau_{\mathrm{c}} = \frac{\mathrm{d}x_4}{a},\qquad \mathcal{H} = \frac{\dot a}{a},\\
&k^2\phi_{\mathrm{B}} + 3\mathcal{H}\big(\dot\phi_{\mathrm{B}} + \mathcal{H}\psi_{\mathrm{B}}\big) = -4\pi G_{\mathrm{N}}a^2\,\Delta\rho,\qquad
 k^2\big(\dot\phi_{\mathrm{B}} + \mathcal{H}\psi_{\mathrm{B}}\big) = 4\pi G_{\mathrm{N}}a^2(\rho + \mathcal{P})\,\vartheta,\\
&\ddot\phi_{\mathrm{B}} + \mathcal{H}\big(\dot\psi_{\mathrm{B}} + 2\dot\phi_{\mathrm{B}}\big) + \Big(2\frac{\ddot a}{a} - \mathcal{H}^2\Big)\psi_{\mathrm{B}}
 + \frac{k^2}{3}\big(\phi_{\mathrm{B}} - \psi_{\mathrm{B}}\big) = 4\pi G_{\mathrm{N}}a^2\,\Delta\mathcal{P},\\
&k^2\big(\phi_{\mathrm{B}} - \psi_{\mathrm{B}}\big) = 12\pi G_{\mathrm{N}}a^2(\rho + \mathcal{P})\,\Sigma_{\mathrm{s}}
\end{aligned} \tag{FE-54}
$$
<!-- symbols: hhat, imu, inu, diff, xfour, ascale, psiB, tauc, phiB, x1, x2, x3, euler, a4, x4, Hconf, kwave, pi, GN, Delta, rhotot, Ptot, varthetatot, Sigmas -->
<!-- begin generated symbol list -->
**Symbols in (FE-54).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $x$: The coordinates of the fold: $x_i$ ($i = 1, 2, 3$) of ordinary space, $x_4$ the time, $x_r$ ($r = 5, 6, 7$) the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $a,\ \dot a,\ \ddot a$: The scale factor of the fold, $a = \mathrm{e}^{a_4}$ (normalised to 1 today by the choice of the comoving coordinates $x_1, x_2, x_3$), and its first and second derivatives with respect to the conformal time $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $\psi_{\mathrm{B}},\ \dot\psi_{\mathrm{B}}$: The Bardeen potential of the time-time part of the perturbed metric of the fold (the Newtonian potential) in the conformal Newtonian gauge, a function of $\tau_{\mathrm{c}}$ and of the wave number $k$, and its derivative with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $\tau_{\mathrm{c}}$: The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{d}x_4/a$; a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$. Unit: length (= time). Status: STANDARD.
- $\phi_{\mathrm{B}},\ \dot\phi_{\mathrm{B}},\ \ddot\phi_{\mathrm{B}}$: The Bardeen potential of the space-space part of the perturbed metric of the fold (the curvature potential) in the conformal Newtonian gauge, and its first and second derivatives with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\mathcal{H}$: The conformal expansion rate, $\mathcal{H} = \dot a/a = a\,a_4'$. Unit: 1/length. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\vartheta$: The divergence of the velocity of the total matter: $(\rho + \mathcal{P})\vartheta$ is the sum over the species of their energy density plus pressure times the divergence of their velocity. Unit: 1/length. Status: STANDARD.
- $\Sigma_{\mathrm{s}}$: The anisotropic stress (shear) of the total matter: $(\rho + \mathcal{P})\Sigma_{\mathrm{s}}$ is the sum over the species (photons and neutrinos) of their energy density plus pressure times their shear. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

The metric of the fold with the scalar perturbations in the conformal Newtonian gauge ($\psi_{\mathrm{B}}$ and $\phi_{\mathrm{B}}$ the two Bardeen
potentials, functions of the conformal time $\tau_{\mathrm{c}}$ and of the comoving wave number $k$ of a Fourier mode; a dot is
$\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$; the comoving coordinates are chosen so that $a = 1$ today), and the Einstein equations of the fold
(FE-59) to first order: the energy constraint, the momentum constraint, the trace of the space-space equations and their traceless
part. $\Delta\rho$ and $\Delta\mathcal{P}$ are the perturbations of the total energy density and pressure; $(\rho + \mathcal{P})\vartheta$ and
$(\rho + \mathcal{P})\Sigma_{\mathrm{s}}$ are the sums over the species of (energy density plus pressure) times the divergence of their
velocity and times their anisotropic stress. The bulk adds terms of relative order $\epsilon_{\mathrm{r}} < 1.344\times10^{-13}$ (FE-35, FE-59),
which are dropped. Status: STANDARD (DERIVED: the fold equations are those of general relativity up to order $\epsilon_{\mathrm{r}}$).

$$
\begin{aligned}
&\dot\delta_\chi = -\vartheta_\chi + 3\dot\phi_{\mathrm{B}},\qquad
 \dot\vartheta_\chi = -\mathcal{H}\vartheta_\chi + k^2\psi_{\mathrm{B}} + \Gamma_{\chi\mathrm{b}}\big(\vartheta_{\mathrm{b}} - \vartheta_\chi\big),\\
&\dot\delta_{\mathrm{b}} = -\vartheta_{\mathrm{b}} + 3\dot\phi_{\mathrm{B}},\qquad
 \dot\vartheta_{\mathrm{b}} = -\mathcal{H}\vartheta_{\mathrm{b}} + c_{\mathrm{s}}^2k^2\delta_{\mathrm{b}} + k^2\psi_{\mathrm{B}}
 + \frac{a\,x_{\mathrm{e}}n_e\sigma_{\mathrm{T}}}{\mathsf{R}}\big(\vartheta_\gamma - \vartheta_{\mathrm{b}}\big)
 + \frac{\rho_\chi}{\rho_{\mathrm{b}}}\,\Gamma_{\chi\mathrm{b}}\big(\vartheta_\chi - \vartheta_{\mathrm{b}}\big),\qquad
 \mathsf{R} = \frac{3\rho_{\mathrm{b}}}{4\rho_\gamma},\\
&\dot\delta_\gamma = -\frac43\vartheta_\gamma + 4\dot\phi_{\mathrm{B}},\qquad
 \dot\vartheta_\gamma = k^2\Big(\frac{\delta_\gamma}{4} - \Sigma_\gamma\Big) + k^2\psi_{\mathrm{B}} + a\,x_{\mathrm{e}}n_e\sigma_{\mathrm{T}}\big(\vartheta_{\mathrm{b}} - \vartheta_\gamma\big),\\
&\dot{\mathsf{F}}_l = \frac{k}{2l + 1}\big(l\,\mathsf{F}_{l-1} - (l + 1)\,\mathsf{F}_{l+1}\big)
 - a\,x_{\mathrm{e}}n_e\sigma_{\mathrm{T}}\Big(\mathsf{F}_l - \frac{\mathsf{G}_0 + \mathsf{F}_2 + \mathsf{G}_2}{10}\,\delta_{l2}\Big)\quad(l \ge 2),\\
&\dot{\mathsf{G}}_l = \frac{k}{2l + 1}\big(l\,\mathsf{G}_{l-1} - (l + 1)\,\mathsf{G}_{l+1}\big)
 - a\,x_{\mathrm{e}}n_e\sigma_{\mathrm{T}}\Big(\mathsf{G}_l - \frac{\mathsf{G}_0 + \mathsf{F}_2 + \mathsf{G}_2}{2}\Big(\delta_{l0} + \frac{\delta_{l2}}{5}\Big)\Big)\quad(l \ge 0),\\
&\mathsf{F}_0 = \delta_\gamma,\qquad \mathsf{F}_1 = \frac{4\vartheta_\gamma}{3k},\qquad \mathsf{F}_2 = 2\Sigma_\gamma,\\
&\dot\delta_\nu = -\frac43\vartheta_\nu + 4\dot\phi_{\mathrm{B}},\qquad \dot\vartheta_\nu = k^2\Big(\frac{\delta_\nu}{4} - \Sigma_\nu\Big) + k^2\psi_{\mathrm{B}},\qquad
 \dot{\mathsf{N}}_l = \frac{k}{2l + 1}\big(l\,\mathsf{N}_{l-1} - (l + 1)\,\mathsf{N}_{l+1}\big)\quad(l \ge 2),\\
&\mathsf{N}_1 = \frac{4\vartheta_\nu}{3k},\qquad \mathsf{N}_2 = 2\Sigma_\nu,\\
&\dot\Upsilon_0 = -\frac{\mathsf{q}k}{\mathsf{E}}\Upsilon_1 - \dot\phi_{\mathrm{B}}\frac{\mathrm{d}\ln\mathcal{F}_0}{\mathrm{d}\ln\mathsf{q}},\qquad
 \dot\Upsilon_1 = \frac{\mathsf{q}k}{3\mathsf{E}}\big(\Upsilon_0 - 2\Upsilon_2\big) - \frac{\mathsf{E}k}{3\mathsf{q}}\,\psi_{\mathrm{B}}\frac{\mathrm{d}\ln\mathcal{F}_0}{\mathrm{d}\ln\mathsf{q}},\\
&\dot\Upsilon_l = \frac{\mathsf{q}k}{(2l + 1)\mathsf{E}}\big(l\,\Upsilon_{l-1} - (l + 1)\,\Upsilon_{l+1}\big)\quad(l \ge 2),\qquad
 \mathsf{E} = \sqrt{\mathsf{q}^2 + a^2m_i^2},\qquad \mathcal{F}_0 = \frac{1}{\mathrm{e}^{\mathsf{q}/\mathsf{T}_\nu^{(0)}} + 1}
\end{aligned} \tag{FE-55}
$$
<!-- symbols: deltachi, varthetachi, phiB, Hconf, kwave, psiB, Gammachib, varthetab, deltab, cs, ascale, xe, ne, sigmaT, Rbg, varthetagamma, rhochi, rhob, rhogamma, deltagamma, Sigmagamma, Fgamma, il, Ggamma, delta, deltanu, varthetanu, Sigmanu, Nnu, Upsilonnu, qcom, Ecom, diff, Fzero, mmass, ii, euler, Tnu -->
<!-- begin generated symbol list -->
**Symbols in (FE-55).**

- $\delta_\chi,\ \dot\delta_\chi$: The density contrast of the dark matter (the bound states $\chi$ of dirac16complex), the perturbation of its energy density divided by its mean, and its derivative with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $\vartheta_\chi,\ \dot\vartheta_\chi$: The divergence of the velocity of the dark matter (for a Fourier mode, $\mathrm{i}k$ times its velocity along the wave vector), and its derivative. Unit: 1/length. Status: STANDARD.
- $\phi_{\mathrm{B}},\ \dot\phi_{\mathrm{B}},\ \ddot\phi_{\mathrm{B}}$: The Bardeen potential of the space-space part of the perturbed metric of the fold (the curvature potential) in the conformal Newtonian gauge, and its first and second derivatives with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $\mathcal{H}$: The conformal expansion rate, $\mathcal{H} = \dot a/a = a\,a_4'$. Unit: 1/length. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\psi_{\mathrm{B}},\ \dot\psi_{\mathrm{B}}$: The Bardeen potential of the time-time part of the perturbed metric of the fold (the Newtonian potential) in the conformal Newtonian gauge, a function of $\tau_{\mathrm{c}}$ and of the wave number $k$, and its derivative with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $\Gamma_{\chi\mathrm{b}}$: The rate (per conformal time) at which the dark matter exchanges momentum with the baryons through the portal couplings of FE-47 (elastic scattering of $\chi$ on nuclei and electrons). Unit: 1/length. Value: negligible for the couplings that direct detection allows. Status: DERIVED.
- $\vartheta_{\mathrm{b}},\ \dot\vartheta_{\mathrm{b}}$: The divergence of the velocity of the baryons and its derivative. Unit: 1/length. Status: STANDARD.
- $\delta_{\mathrm{b}},\ \dot\delta_{\mathrm{b}}$: The density contrast of the baryons and its derivative. Unit: dimensionless. Status: STANDARD.
- $c_{\mathrm{s}}$: The sound speed of the baryon gas: its square is the temperature of the gas divided by the mean mass per particle, times one minus a third of the logarithmic derivative of that temperature with respect to $a$. Unit: dimensionless. Status: STANDARD.
- $a,\ \dot a,\ \ddot a$: The scale factor of the fold, $a = \mathrm{e}^{a_4}$ (normalised to 1 today by the choice of the comoving coordinates $x_1, x_2, x_3$), and its first and second derivatives with respect to the conformal time $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $x_{\mathrm{e}}$: The ionisation fraction: the fraction of the electrons that are free. Unit: dimensionless. Status: STANDARD.
- $n_e$: The number density of electrons (bound and free; in a supernova all are free, in the recombining universe $x_{\mathrm{e}}n_e$ is the density of the free electrons). Unit: GeV$^3$ (cm$^{-3}$). Status: STANDARD.
- $\sigma_{\mathrm{T}}$: The Thomson cross-section of the scattering of photons on free electrons. Unit: GeV$^{-2}$. Value: $6.6524587\times10^{-25}$ cm$^2$. Status: STANDARD.
- $\mathsf{R}$: The ratio of the inertia of the baryons to that of the photons, $\mathsf{R} = 3\rho_{\mathrm{b}}/(4\rho_\gamma)$. Unit: dimensionless. Status: STANDARD.
- $\vartheta_\gamma,\ \dot\vartheta_\gamma$: The divergence of the velocity of the photons and its derivative. Unit: 1/length. Status: STANDARD.
- $\rho_\chi$: The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $\rho_\gamma$: The energy density of the photons. Unit: GeV$^4$. Status: STANDARD.
- $\delta_\gamma,\ \dot\delta_\gamma$: The density contrast of the photons and its derivative. Unit: dimensionless. Status: STANDARD.
- $\Sigma_\gamma$: The anisotropic stress (shear) of the photons. Unit: dimensionless. Status: STANDARD.
- $\mathsf{F}_l,\ \dot{\mathsf{F}}_l$: The multipoles of the temperature perturbation of the photons ($\mathsf{F}_0 = \delta_\gamma$, $\mathsf{F}_1 = 4\vartheta_\gamma/(3k)$, $\mathsf{F}_2 = 2\Sigma_\gamma$; the $F_{\gamma l}$ of Ma and Bertschinger) and their derivatives with respect to $\tau_{\mathrm{c}}$. Unit: dimensionless. Status: STANDARD.
- $l$: The multipole index and number ($l = 0, 1, 2, \dots$) of an expansion in Legendre polynomials of the direction of a photon or a neutrino relative to the wave vector, or of the CMB sky in spherical harmonics. Status: STANDARD.
- $\mathsf{G}_l,\ \dot{\mathsf{G}}_l$: The multipoles of the polarisation perturbation of the photons (the $G_{\gamma l}$ of Ma and Bertschinger) and their derivatives. Unit: dimensionless. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\delta_\nu,\ \dot\delta_\nu$: The density contrast of the relativistic neutrinos and its derivative. Unit: dimensionless. Status: STANDARD.
- $\vartheta_\nu,\ \dot\vartheta_\nu$: The divergence of the velocity of the relativistic neutrinos and its derivative. Unit: 1/length. Status: STANDARD.
- $\Sigma_\nu$: The anisotropic stress (shear) of the relativistic neutrinos. Unit: dimensionless. Status: STANDARD.
- $\mathsf{N}_l,\ \dot{\mathsf{N}}_l$: The multipoles of the perturbation of the relativistic neutrinos ($\mathsf{N}_0 = \delta_\nu$, $\mathsf{N}_1 = 4\vartheta_\nu/(3k)$, $\mathsf{N}_2 = 2\Sigma_\nu$) and their derivatives. Unit: dimensionless. Status: STANDARD.
- $\Upsilon_l(\mathsf{q}),\ \dot\Upsilon_l$: The multipoles of the relative perturbation of the distribution of a massive neutrino state at the comoving momentum $\mathsf{q}$ (the $\Psi_l$ of Ma and Bertschinger) and their derivatives. Unit: dimensionless. Status: STANDARD.
- $\mathsf{q}$: The comoving momentum of a neutrino, $a\lvert\vec p\rvert$. Unit: GeV. Status: STANDARD.
- $\mathsf{E}$: The comoving energy of a massive neutrino ($a$ times its energy). Unit: GeV. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\mathcal{F}_0(\mathsf{q})$: The unperturbed (Fermi-Dirac) occupation number of the cosmic neutrino background at the comoving momentum $\mathsf{q}$. Unit: dimensionless. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; in $\Delta m^2$ the squared-mass difference of two neutrino mass states ($m_2^2 - m_1^2$ for the two states of a resonance, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1). Unit: GeV. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathsf{T}_\nu$: The temperature of the cosmic neutrino background; $\mathsf{T}_\nu^{(0)}$ its value today. Unit: GeV (or K). Value: 1.945 K today. Status: STANDARD.

<!-- end generated symbol list -->

The Boltzmann equations of the species in the same gauge (Ma and Bertschinger 1995, their equations 42, 66, 63, 49 and 57): the
dark matter $\chi$ (the bound states of dirac16complex: pressureless, with the drag $\Gamma_{\chi\mathrm{b}}$ on the baryons from its portal
couplings, FE-47, which is negligible for the couplings that direct detection allows); the baryons (with the sound speed $c_{\mathrm{s}}$ of
the gas and the Thomson coupling to the photons through the free electrons, $x_{\mathrm{e}}$ the ionisation fraction); the photons (the
multipoles $\mathsf{F}_l$ of the temperature and $\mathsf{G}_l$ of the polarisation, $l$ the multipole index; $\delta_{l0}$, $\delta_{l2}$ are
Kronecker deltas, and the term $l\,\mathsf{G}_{l-1}$ vanishes for $l = 0$); the neutrinos while they are relativistic (the multipoles
$\mathsf{N}_l$); and each massive neutrino state $i$ of mass $m_i$ (the multipoles $\Upsilon_l$ of the relative perturbation of its
distribution at the comoving momentum $\mathsf{q}$ and energy $\mathsf{E}$, with the Fermi-Dirac occupation $\mathcal{F}_0$ of the CNB). The
hierarchies are truncated at a large $l$ in a numerical solution. Status: STANDARD (UM-3: the dark matter is $\chi$, with the drag term).

$$
\begin{aligned}
&r_{\mathrm{s}} = \int_0^{\tau_{\mathrm{d}}}c_{\gamma\mathrm{b}}\,\mathrm{d}\tau_{\mathrm{c}},\qquad c_{\gamma\mathrm{b}} = \frac{1}{\sqrt{3(1 + \mathsf{R})}},\\
&D_{\mathrm{M}}(\mathsf{z}) = \int_0^{\mathsf{z}}\frac{\mathrm{d}\mathsf{z}'}{H_4(\mathsf{z}')},\qquad
 D_{\mathrm{H}}(\mathsf{z}) = \frac{1}{H_4(\mathsf{z})},\qquad
 D_{\mathrm{V}}(\mathsf{z}) = \big(\mathsf{z}\,D_{\mathrm{M}}^2(\mathsf{z})\,D_{\mathrm{H}}(\mathsf{z})\big)^{1/3}
\end{aligned} \tag{FE-56}
$$
<!-- symbols: rs, taud, csgb, diff, tauc, Rbg, DM, zred, prime, H4, DH, DV -->
<!-- begin generated symbol list -->
**Symbols in (FE-56).**

- $r_{\mathrm{s}}$: The comoving sound horizon at the drag epoch: the comoving distance that a sound wave of the photon-baryon fluid travels until the baryons are released from the photons. Unit: length. Value: about 147 Mpc (Planck 2018). Status: STANDARD.
- $\tau_{\mathrm{d}}$: The conformal time of the drag epoch, when the baryons are released from the photons (redshift about 1060). Unit: length (= time). Status: STANDARD.
- $c_{\gamma\mathrm{b}}$: The sound speed of the tightly coupled photon-baryon fluid. Unit: dimensionless. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\tau_{\mathrm{c}}$: The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{d}x_4/a$; a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$. Unit: length (= time). Status: STANDARD.
- $\mathsf{R}$: The ratio of the inertia of the baryons to that of the photons, $\mathsf{R} = 3\rho_{\mathrm{b}}/(4\rho_\gamma)$. Unit: dimensionless. Status: STANDARD.
- $D_{\mathrm{M}}(\mathsf{z})$: The transverse comoving distance (comoving angular-diameter distance) to the redshift $\mathsf{z}$, for a spatially flat fold. Unit: length. Status: STANDARD.
- $\mathsf{z}$: The redshift, $1 + \mathsf{z} = 1/a$; $\mathsf{z}'$ an integration variable. Unit: dimensionless. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $D_{\mathrm{H}}(\mathsf{z})$: The Hubble distance at the redshift $\mathsf{z}$. Unit: length. Status: STANDARD.
- $D_{\mathrm{V}}(\mathsf{z})$: The volume-averaged distance to the redshift $\mathsf{z}$. Unit: length. Status: STANDARD.

<!-- end generated symbol list -->

The baryon acoustic oscillations: the sound horizon $r_{\mathrm{s}}$ at the drag epoch $\tau_{\mathrm{d}}$ (the comoving distance that a sound wave
of the photon-baryon fluid, of speed $c_{\gamma\mathrm{b}}$, travels before the baryons are released from the photons), and the distances to
the redshift $\mathsf{z}$ at which galaxy surveys measure it: the transverse comoving distance $D_{\mathrm{M}}$ (for a spatially flat fold), the
Hubble distance $D_{\mathrm{H}}$ and their volume average $D_{\mathrm{V}}$ ($H_4 = a_4'$ the expansion rate of the fold as a function of redshift).
The surveys measure $D_{\mathrm{M}}/r_{\mathrm{s}}$, $D_{\mathrm{H}}/r_{\mathrm{s}}$ and $D_{\mathrm{V}}/r_{\mathrm{s}}$. Status: STANDARD.

$$
\begin{aligned}
&C_l^{\mathrm{TT}} = 4\pi\int\frac{\mathrm{d}k}{k}\,\mathcal{P}_{\mathcal{R}}(k)\,\big(\mathcal{I}_l^{\mathrm{T}}(k)\big)^2,\qquad
 C_l^{\mathrm{TE}} = 4\pi\int\frac{\mathrm{d}k}{k}\,\mathcal{P}_{\mathcal{R}}(k)\,\mathcal{I}_l^{\mathrm{T}}(k)\,\mathcal{I}_l^{\mathrm{E}}(k),\\
&C_l^{\mathrm{EE}} = 4\pi\int\frac{\mathrm{d}k}{k}\,\mathcal{P}_{\mathcal{R}}(k)\,\big(\mathcal{I}_l^{\mathrm{E}}(k)\big)^2,\qquad
 \mathcal{P}_{\mathcal{R}}(k) = A_{\mathrm{s}}\Big(\frac{k}{k_*}\Big)^{n_{\mathrm{S}} - 1}
\end{aligned} \tag{FE-57}
$$
<!-- symbols: Cl, il, CMBlab, pi, diff, kwave, PRspec, Itrans, As, kstar, nS -->
<!-- begin generated symbol list -->
**Symbols in (FE-57).**

- $C_l^{\mathrm{TT}},\ C_l^{\mathrm{TE}},\ C_l^{\mathrm{EE}}$: The angular power spectra of the CMB at the multipole $l$: temperature with temperature, temperature with E-mode polarisation, E-mode polarisation with itself. Unit: dimensionless. Status: STANDARD.
- $l$: The multipole index and number ($l = 0, 1, 2, \dots$) of an expansion in Legendre polynomials of the direction of a photon or a neutrino relative to the wave vector, or of the CMB sky in spherical harmonics. Status: STANDARD.
- $\mathrm{T},\ \mathrm{E}$: The labels of the CMB observables: $\mathrm{T}$ the temperature anisotropy, $\mathrm{E}$ the E-mode (gradient) polarisation; $\mathrm{TT}$, $\mathrm{TE}$, $\mathrm{EE}$ label the spectra of their products. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\mathcal{P}_{\mathcal{R}}(k)$: The primordial power spectrum of the comoving curvature perturbation, per logarithmic interval of $k$. Unit: dimensionless. Status: ASSUMED.
- $\mathcal{I}_l^{\mathrm{T}}(k),\ \mathcal{I}_l^{\mathrm{E}}(k)$: The transfer functions of the CMB: the multipole $l$ of the temperature or E-mode anisotropy today produced by a Fourier mode $k$ of unit primordial curvature perturbation, computed from FE-54 and FE-55 (the line-of-sight integral). Unit: dimensionless. Status: STANDARD.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $k_*$: The pivot wave number of the primordial spectrum. Unit: GeV (1/length). Value: 0.05 Mpc$^{-1}$. Status: STANDARD.
- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.

<!-- end generated symbol list -->

The angular power spectra of the CMB temperature (T) and E-mode polarisation (E) at the multipole $l$: the transfer functions
$\mathcal{I}_l^{\mathrm{T}}$, $\mathcal{I}_l^{\mathrm{E}}$ follow from FE-54 and FE-55, integrated from the early universe to today (the line-of-sight
integral), and are weighted with the primordial spectrum $\mathcal{P}_{\mathcal{R}}$ of the comoving curvature perturbation (amplitude
$A_{\mathrm{s}}$, spectral index $n_{\mathrm{S}}$, pivot $k_*$). The primordial spectrum is an input of UM-3 (ASSUMED: the author's primordial era
is not computed to the precision this needs). Status: STANDARD.

$$
\begin{aligned}
&\Omega_\chi = \frac{\rho_\chi^{(0)}}{\rho_{\mathrm{c}}^{(0)}},\qquad \Omega_{\mathrm{b}} = \frac{\rho_{\mathrm{b}}^{(0)}}{\rho_{\mathrm{c}}^{(0)}},\qquad
 \Omega_\Lambda = \frac{\rho_\Lambda}{\rho_{\mathrm{c}}^{(0)}},\qquad \Omega_\nu h_{100}^2 = \frac{\sum_im_i}{93.14\ \text{eV}},\\
&\rho_{\mathrm{c}}^{(0)} = \frac{3\big(H_4^{(0)}\big)^2}{8\pi G_{\mathrm{N}}},\qquad H_4^{(0)} = 100\,h_{100}\ \text{km/s/Mpc}
\end{aligned} \tag{FE-58}
$$
<!-- symbols: Omegachi, rhochi, rhoc, Omegab, rhob, OmegaL, rhoL, Omeganu, h100, ii, mmass, H4, pi, GN -->
<!-- begin generated symbol list -->
**Symbols in (FE-58).**

- $\Omega_\chi$: The density parameter of the dark matter today. Unit: dimensionless. Value: $\Omega_\chi h_{100}^2 = 0.120$ (Planck 2018). Status: DERIVED.
- $\rho_\chi$: The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_{\mathrm{c}}$: The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today. Unit: GeV$^4$. Value: $\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$. Status: STANDARD.
- $\Omega_{\mathrm{b}}$: The density parameter of the baryons today. Unit: dimensionless. Value: $\Omega_{\mathrm{b}}h_{100}^2 = 0.0224$ (Planck 2018). Status: STANDARD.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $\Omega_\Lambda$: The density parameter of the dark energy (the vacuum energy of the fold) today. Unit: dimensionless. Value: 0.685 (Planck 2018). Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} - 31HV_*/(4\kappa)$ (FE-59). Unit: GeV$^4$. Status: DERIVED.
- $\Omega_\nu,\ \Omega_\nu^{(i)}$: The density parameter of the neutrinos of the CNB: $\Omega_\nu$ that of the massive states today; $\Omega_\nu^{(i)}(\mathsf{z})$ the energy density of the mass state $i$ at the redshift $\mathsf{z}$ in units of the critical density today. Unit: dimensionless. Status: STANDARD.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ a direction $x_i$ of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; in $\Delta m^2$ the squared-mass difference of two neutrino mass states ($m_2^2 - m_1^2$ for the two states of a resonance, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1). Unit: GeV. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.

<!-- end generated symbol list -->

The density parameters today: the dark matter (the relic density of $\chi$, FE-61), the baryons, the dark energy (the vacuum energy of
the fold, FE-59) and the massive neutrinos of the CNB (for the three left-handed states with the temperature and the small
non-thermal distortion of the Standard Model; the right-handed states are not populated). Together with $A_{\mathrm{s}}$, $n_{\mathrm{S}}$ and the
optical depth of reionisation they fix the CMB, the CNB and the BAO. Status: STANDARD.

# The thermal history

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

The Einstein equations of the fold: FE-4 and FE-5 combined. The left-hand side is the induced gravity; the sources are the Standard
Model ($\mathcal{T}_{\mathrm{SM}} = \mathcal{T}_{\mathrm{H}} + \mathcal{T}_{\mathrm{gauge}} + \mathcal{T}_{\mathrm{f}}$), the portals, the fold fluid and the bulk, which
acts through the jump $\mathcal{J}$ of the junction potential computed from the metric (FE-30, or FE-33 with frozen extra times). For a
homogeneous fold with frozen extra times $\mathcal{J}^{(4)}{}_{(4)} = -(31 + 10\mathsf{A}^2)H/4$ (FE-33): its constant part cancels against the
fold fluid except for the remainder $\rho_\Lambda$, the dark energy of UM-3 (a vacuum energy of the fold), and its part
$-\frac52\,a_4'^2/H$ adds to the left-hand side, so that the Friedmann equation of the fold has Newton's constant reduced by the factor
$1 + 5\epsilon_{\mathrm{r}}/6$ ($\epsilon_{\mathrm{r}}$ the ratio of bulk to fold gravity; DERIVED from FE-33 with $\mathsf{A} = a_4'/H$ and
$\hat G^{(4)}{}_{(4)} = -3a_4'^2$). The space-space components give, in the same way, the acceleration equation of general relativity
up to terms of order $\epsilon_{\mathrm{r}}$. The component along the extra times (the third line; $q$ is a pressure along the extra times,
for every term of the fold its on-shell Lagrangian density by FE-5, and the induced gravity contributes $\hat R/(2\kappa_4)$, $\hat R$ the scalar
curvature of the fold) is an additional equation: the equation of the size of the extra times at the fold (the radion). To leading
order in $\epsilon_{\mathrm{r}}$ it requires that the sum over the matter of the fold of $q + (\rho - 3p)/2$ vanishes. Radiation satisfies it;
non-relativistic matter ($q = 0$ for the bound states of dirac16complex, $q = -\rho$ for classical particles on the fold) and vacuum energy
($q = -\rho$) do not. The first-order terms of the power series FE-35 must therefore carry the difference: if the bulk medium does not
respond, the only available bulk mode is the difference mode of FE-35, which changes the acceleration equation to
$5H_4' + 9H_4^2 = -\kappa_4(p + q)$ (dust would expand as $x_4^{5/6}$, which observation excludes); UM-3 therefore requires (ASSUMED) that the
bulk medium responds with the radion mode of FE-35, which changes only the extra-time component and keeps the four-dimensional equations
those of general relativity (DERIVED, `um3_series.py`, SR1 to SR6). The radion mode with the jumps $c\,(1, -1, 5)$ of
$(\mathfrak{a}_1', \mathfrak{b}_1', \mathfrak{n}_1')$ at the fold changes the extra-time component of the junction by
$\kappa\,\delta\mathcal{S}^{(r)}{}_{(r)} = 5c/8$; today it must carry the mismatch $0.793\,\rho_{\mathrm{c}}^{(0)}$ of the dark matter
($q = 0$), the baryons and the vacuum energy ($q = -\rho$), which needs the amplitude $c/H = 3.806\,\mathsf{A}^2/\epsilon_{\mathrm{r}}$
($\mathsf{A} = a_4'/H$, $\rho_{\mathrm{c}}^{(0)}$ the critical density of FE-58), a small term of the power series when
$\mathsf{A}^2 \ll \epsilon_{\mathrm{r}}$, that is when the bulk curvature scale $H$ exceeds the Hubble rate by far more than
$\epsilon_{\mathrm{r}}^{-1/2}$ (DERIVED, SR6). With
$\epsilon_{\mathrm{r}} < 1.344\times10^{-13}$ (FE-63) the fold then expands as in general relativity. Status: DERIVED (with the ASSUMED induced gravity and
the ASSUMED response of the bulk medium).

$$
\rho_{\mathrm{SM}} = \frac{\pi^2}{30}\,g_\rho(\mathsf{T})\,\mathsf{T}^4,\qquad s = \frac{2\pi^2}{45}\,g_{\mathrm{s}}(\mathsf{T})\,\mathsf{T}^3,\qquad
H_4 = \sqrt{\frac{8\pi^3g_\rho}{90}}\,\frac{\mathsf{T}^2}{M_{\mathrm{Pl}}},\qquad M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2} \tag{FE-60}
$$
<!-- symbols: rhoSM, pi, grho, Ttemp, sent, gs, H4, MPl, GN -->
<!-- begin generated symbol list -->
**Symbols in (FE-60).**

- $\rho_{\mathrm{SM}}$: The energy density of the Standard-Model particles. Unit: GeV$^4$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $g_\rho$: The effective number of relativistic degrees of freedom of the energy density. Unit: dimensionless. Value: 106.75 in the Standard Model above the electroweak scale. Status: STANDARD.
- $\mathsf{T}$: The temperature of the Standard-Model plasma (of the photons after the annihilation of electrons and positrons). Unit: GeV. Status: STANDARD.
- $s$: The entropy density of the Standard-Model plasma. Unit: GeV$^3$. Status: STANDARD.
- $g_{\mathrm{s}}$: The effective number of relativistic degrees of freedom of the entropy density. Unit: dimensionless. Value: 3.909 today. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.221\times10^{19}$ GeV. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.

<!-- end generated symbol list -->

The radiation of the Standard Model in thermal equilibrium at the temperature $\mathsf{T}$: the energy density and the entropy density with
the effective numbers of relativistic degrees of freedom $g_\rho$ and $g_{\mathrm{s}}$ (106.75 above the electroweak scale in the Standard
Model; three right-handed neutrinos in equilibrium would add $\frac78\times6 = 5.25$; the bound states of dirac16complex add theirs while
they are relativistic), and the expansion rate of the radiation era. Status: STANDARD.

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

The relic density of the bound states of dirac16complex: their number density $n_\chi$ (particles plus antiparticles) follows the
Boltzmann equation with the thermally averaged annihilation cross-section $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ into Standard-Model
particles through the portal couplings of FE-47 (Higgs exchange, pairs of gluons and photons, pairs of fermions); $g_\chi$ is the number of
states of the bound level that are in equilibrium. The freeze-out at $x_{\mathrm{f}} = \omega_{\mathrm{b}}/\mathsf{T}_{\mathrm{f}} \approx 20$ to 25
($\mathsf{T}_{\mathrm{f}}$ the temperature at which the annihilations stop) gives the standard estimate of the relic density for an annihilation
that does not depend on the velocity ($g_*$ the degrees of freedom at freeze-out). Status: STANDARD (UM-3: the cross-section from the portals).

$$
\frac{\mathrm{d}\rho_{\nu_{\mathrm{R}}}}{\mathrm{d}x_4} + 4H_4\,\rho_{\nu_{\mathrm{R}}} = \mathcal{C}_{\nu_{\mathrm{R}}},\qquad
\Delta N_{\mathrm{eff}} = 3\Big(\frac{10.75}{g_{\mathrm{s}}(\mathsf{T}_{\mathrm{dec}})}\Big)^{4/3}\ \ \text{(three right-handed neutrinos decoupling at } \mathsf{T}_{\mathrm{dec}}) \tag{FE-62}
$$
<!-- symbols: diff, rhonuR, x4, H4, CnuR, Delta, Neff, gs, Tdec -->
<!-- begin generated symbol list -->
**Symbols in (FE-62).**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\rho_{\nu_{\mathrm{R}}}$: The energy density of the three right-handed neutrinos. Unit: GeV$^4$. Status: STANDARD.
- $x_4$: The time ($x_4 \ge 0$ in the ad hoc vacuum); a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $\mathcal{C}_{\nu_{\mathrm{R}}}$: The collision term of the right-handed neutrinos: the rate at which collisions produce (or remove) their energy density. Unit: GeV$^5$. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $N_{\mathrm{eff}}$: The effective number of neutrino species: the energy density of the relativistic particles other than photons in units of that of one neutrino species whose temperature is $(4/11)^{1/3}$ times that of the photons. Unit: dimensionless. Value: 3.044 (Standard Model); measured $2.99 \pm 0.17$ (Planck 2018). Status: STANDARD.
- $g_{\mathrm{s}}$: The effective number of relativistic degrees of freedom of the entropy density. Unit: dimensionless. Value: 3.909 today. Status: STANDARD.
- $\mathsf{T}_{\mathrm{dec}}$: The temperature at which the right-handed neutrinos decouple from the plasma. Unit: GeV. Status: STANDARD.

<!-- end generated symbol list -->

The right-handed neutrinos in the early universe: their energy density grows by the collision term $\mathcal{C}_{\nu_{\mathrm{R}}}$ (production by
the neutrino Yukawa couplings, negligible for Dirac masses below 0.1 eV because it is suppressed by the square of the mass over the
temperature, and by the current portal $c^{\nu}_X$ with dirac16complex), and if they were in equilibrium until the temperature
$\mathsf{T}_{\mathrm{dec}}$ they add $\Delta N_{\mathrm{eff}}$ to the effective number of neutrinos (from the conservation of entropy after their
decoupling). The measured $N_{\mathrm{eff}} = 2.99 \pm 0.17$ (Planck 2018) and $2.89 \pm 0.11$ (ACT DR6, the sixth data release of the
Atacama Cosmology Telescope, with Planck, lensing, BAO and nucleosynthesis, 2025) bound $\Delta N_{\mathrm{eff}}$ and with it the portal couplings $c^{\nu}_X$: if the portal keeps the
right-handed neutrinos in equilibrium with $\chi$ they decouple at $\mathsf{T}_{\mathrm{dec}} \approx \omega_{\mathrm{b}}/13$ to $\omega_{\mathrm{b}}/17$ and add
$\Delta N_{\mathrm{eff}} = 0.14$ to $0.24$ for $\omega_{\mathrm{b}} = 10$ TeV to 10 GeV, 2.7 to 3.5 standard deviations above the ACT value; the
right-handed neutrinos of UM-3 must therefore never thermalise ($c^{\nu}_X$ much smaller than the lepton-doublet couplings), and
then $N_{\mathrm{eff}} = 3.044$ (DERIVED, `um3_thermal.py`, T5). Status: STANDARD (the equations), DERIVED (the bound).

# The coupled system

## Which field appears in which equation

| equation | the fields in it | how they enter |
| ---------------------------- | ------------------------------------ | -------------------------------------------------------- |
| bulk gravity FE-1 | metric, dirac16complex, stabiliser | the Lovelock tensors of the metric; $\mathcal{T}_\Psi$; $\mathcal{T}_{\mathrm{stab}}$ |
| fold junction FE-4, FE-5, FE-59 | metric, every field of the fold, dirac16complex at the fold | the jump of the junction potential; $\mathcal{T}_{\mathrm{H}}$, $\mathcal{T}_{\mathrm{gauge}}$, $\mathcal{T}_{\mathrm{f}}$, $\mathcal{T}_{\mathrm{P}}$, $\mathcal{T}_{\mathrm{ff}}$; the induced gravity $\hat G/\kappa_4$ |
| dirac16complex FE-12, FE-13, FE-41 | metric, itself, every Standard-Model field | the spin connection; the self-interaction; the fold operator $\mathbb{M}$ of the portals (the Higgs portal for $\Psi_{\mathrm{L}}$ only) |
| Higgs FE-15 | metric, dirac16complex, $W$, $B$, quarks and leptons | $\hat h$ and $\mathcal{Z}$; $c_\Phi\bar\Psi P_{\mathrm{L}}\Psi$; $D_\mu$; the Yukawa source $\Theta$ |
| gauge fields FE-16 to FE-18 | metric, dirac16complex, Higgs, quarks and leptons | $\hat h$ and $\mathcal{Z}$; the portal factors $\mathcal{K}$ and the dipole density $\mathcal{D}_X$; the currents |
| quarks and leptons FE-19 to FE-24 | metric, gauge fields, Higgs, dirac16complex | $\hat h$; $D_\mu$; the Yukawa matrices; the potentials $\mathcal{V}^{f}$ |
| neutrino flavours FE-48 to FE-53 | expansion, Higgs, dirac16complex, matter, other neutrinos | $a_4'$; $v_{\mathrm{loc}}$ and $G_{\mathrm{F,loc}}$; $V_\Psi$; $\mathsf{V}_{\mathrm{m}}$ and $\mathsf{V}_{\nu\nu}$ |
| cosmology FE-54 to FE-58 | metric perturbations, dark matter $\chi$, baryons, photons, neutrinos | $\phi_{\mathrm{B}}$ and $\psi_{\mathrm{B}}$; $\Gamma_{\chi\mathrm{b}}$; Thomson scattering; $\rho_\Lambda$ |
| thermal history FE-59 to FE-62 | metric, plasma, dark matter $\chi$, right-handed neutrinos | $H_4$, $G_{\mathrm{N}}$ and $\rho_\Lambda$; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$; $\mathcal{C}_{\nu_{\mathrm{R}}}$ |

## How the system is solved

The equations are coupled in a chain that UM-3 solves in steps, each with the results of the earlier ones:

1. The background: the author's vacuum in the primordial era (FE-31: exact in the bulk, with its fold source) and the static block
   with frozen extra times in the late universe (FE-32, FE-33: exact with the stabiliser and the fold fluid).
2. The modes of dirac16complex on the background: the bulk continuum and the bound states (FE-36 to FE-40) with the mean fields of the
   Standard-Model vacuum (FE-39).
3. The Kohn-Sham states (FE-41, FE-42): the bound states filled to a given density, with the self-interaction and the mean fields, to
   self-consistency; their energy-momentum tensor enters the bulk equations and the fold junction (the next order of FE-35).
4. The Standard Model on the fold (FE-44 to FE-47): the masses with the ad hoc vacuum, the residuals FE-26, the couplings of the bound
   states.
5. The neutrino flavours (FE-48 to FE-53), the thermal history (FE-59 to FE-62) and the relic density of $\chi$.
6. The cosmological perturbations (FE-54 to FE-58): the CMB, the CNB and the BAO.

# What was verified

Every statement labelled DERIVED in this document rests on a computation in the folder `universe_model_3/code/` of the repository,
which checks itself and writes a report to `universe_model_3/reports/` (the equations and results themselves are all written out
above). The checks used here:

* `um3_dirac_matrices.py` (55 checks): the author's matrices, their reality, the Clifford relations, the chiral projectors, Pin(4,4).
* `um3_geometry.py` (26 checks): the exact curvature of the author's metric, the Lovelock tensors by two routes, the trace and Bianchi
  identities, the background equations FE-29, the author's vacuum, the degeneracy, the frozen extra times, the spin connection FE-14
  and the vielbein postulate.
* `um3_fold.py` (13 checks): the proper chart, the general warped metric FE-34, quasi-linearity, the junction potential, the fold
  sources FE-30 to FE-33 (also by smoothing the kink), the conservation law FE-11 at the fold.
* `um3_bulk.py` (10 checks): the zero modes and the speeds of bulk scalars, photons, fermions and gravitons (with the Lovelock terms),
  the dispersion of dirac16complex with chiral masses.
* `um3_fields.py` (16 checks): the reality and chirality of the bilinears of dirac16complex, the Krein operator, the four-dimensional
  chirality, the electroweak masses and the photon of the ad hoc vacuum, its isospin charge and residual, the Yukawa invariance, the
  anomalies with three right-handed neutrinos, the electric charges.
* `um3_spectra.py` (5 checks): the transfer matrices, the fold transfer, the bound states FE-40 with the exact $16 \times 16$ matrices, their
  Krein signature.
* `um3_neutrino.py` (5 checks): the flavour blindness of $V_\Psi$ and the invariance of the mixing under $v_{\mathrm{loc}}$ (N1), the
  resonance formulas FE-50 against an exact integration (N2), the crossing criterion of FE-51 (N3), the conservation laws of FE-52
  (N4), the CNB numbers of FE-53 (N5).
* `um3_background.py` (6 checks): the histories of FE-29 with constant rates (only $(\mathsf{A}, \mathsf{U}) = (\pm1, 0)$, a
  degenerate double root), the violation of the null energy condition by the stabiliser and by the bulk medium of the frozen
  branch, the bulk sources that a varying $b_4$ needs in the primordial era (of second order in $\mathsf{U}$, without flux at
  $\mathsf{U} = 2/3$), the factor $\mathcal{Z}$ of the couplings of the fold, the gauge equivalence of the ad hoc vacuum (FE-45) and
  its radial residual, with numbers for three values of $a_{40}$.
* `um3_series.py` (6 checks): the linear operator of the first-order terms of FE-35 around the static block, its only static
  solution (the difference mode $\propto \mathrm{e}^{6H\lvert\sigma\rvert}$), the linear junction conditions and the radion mode, the
  radion condition of FE-59, the acceleration law with a rigid bulk medium, the amplitude of the response today.
* `um3_kohnsham.py` (9 checks): the Kohn-Sham equations FE-41 for a homogeneous gas of the bound particles $\chi$, solved
  self-consistently with the author's matrices (reduced exactly by the rotations of ordinary space and of the extra times, and
  lifted back to sixteen components for the checks): the free level FE-40 (K1), first-order perturbation theory in the dilute limit
  (K2), the residuals of FE-41 and of the matching at the fold in three regimes of $H$, with the dimensionless strength
  $\lambda_\Psi n_\chi/V_*$ of the self-interaction ($n_\chi$ the number density of the particles on the fold) up to 1 in units of
  $m_\Psi$ (K3), the exponents of the dilute limit (K4), the saturation of the proper density far from the fold and the attractive
  case (K5), the Higgs-portal loop through FE-49 (K6), the equation of state from FE-42 (K7), the level raised through the free
  threshold $m_\Psi$ without unbinding (K8), and a weakly bound point that direct detection allows (K9).
* `um3_flavour.py` (4 checks): the survival probability of solar neutrinos by exact integration of FE-48 and FE-49, against the
  adiabatic formula of FE-50 and the measurements of Borexino; the three-flavour conversion in the envelope of a supernova for both
  mass orderings; the fast instability near a neutrinosphere and the dispersion relation FE-51 at its solutions; the equipartition
  FE-52 (its conservation laws, its fixed point, the bound $0 \le \mathcal{F} \le 1$) and its effect on the heating behind the shock.
* `um3_cosmology.py` (6 checks): the expansion rate of FE-59 and the ruler FE-56 computed independently and by the Boltzmann code
  CAMB; the derived quantities of the CMB against Planck 2018; the CMB spectra (FE-57) against the Planck 2018 high-$l$ data, with a
  refit for thermal right-handed neutrinos; the BAO distances against DESI DR2 (the second data release of the Dark Energy
  Spectroscopic Instrument); the CNB numbers of FE-53 and FE-58.
* `um3_thermal.py` (6 checks): $g_\rho$ and $g_{\mathrm{s}}$ of FE-60, the relic density FE-61 by numerical solution, the current
  portals against the limits of direct detection, the Higgs-portal coupling of FE-47 and the binding of $\chi$, the right-handed
  neutrinos and $N_{\mathrm{eff}}$ (FE-62), the ad hoc vacuum before nucleosynthesis.
* `um3_foldsources.py` (6 checks): the linearised equation of the gravitational wave and its junction potential (F1), the thin
  part of the Lovelock terms at the fold, also by smoothing the kink (F2), the speed of the four-dimensional gravitational wave
  FE-63 without (F3) and with (F4) the induced gravity, the gravity induced by the fields of the fold FE-64 (F5), the two parts of
  the fold fluid FE-65 and the energy that feeds them (F6).
* `um3_stabiliser.py` (8 checks): the source that the static bulk requires, IN-7 (ST1); none at the author's vacuum (ST2); no
  sourceless bulk with constant slow rates (ST3); the conservation of the stabiliser on the static bulk (ST4); its energy
  conditions and the ghost field that reproduces it (ST5); its history, the energy flow into the fold and the energy balance of
  the fold (ST6); the drift of the couplings without it and its integrated energy (ST7); the constraints FE-66 (ST8).
* `um3_krein.py` (7 checks): the Krein form and its quantisation FE-67 (KR1), the symmetries at rest and in motion (KR2), the
  mirrors of the fold (KR3), the flat directions of the dilute gas (KR4), the partner level and the growing modes of the dense gas
  (KR5), the selection rules at the fold (KR6), the consequences for stability and unitarity (KR7).
* `um3_extratimes.py` (5 checks): the dispersion with a momentum along the extra times on the fold (EX1), the bound states of
  dirac16complex with such a momentum and their leaking into the bulk (EX2), the double-exponential growth in the author's vacuum
  (EX3), the bound on compact extra times in the late universe (EX4), the truncation to fields without that momentum (EX5).
* `um3_superluminal.py` (5 checks): the limiting speed $c_{\mathrm{b}}$ of the particles $\chi$ (SL1), their dispersion up to large
  momenta, group and front velocity (SL2), the speeds of cosmological $\chi$ (SL3), causality and the shortcut through the bulk
  (SL4), the loop estimate of the Lorentz violation of the electron (SL5).
* `um3_primordial.py` (5 checks): the fields of the fold in the author's vacuum (PR1), their spectrum (PR2), the growth of the
  couplings (PR3), the bound on an inflationary era (PR4), Higgs inflation against induced gravity (PR5).
* `um3_numass.py` (5 checks): the neutrino masses of both orderings (NM1), the bounds of DESI DR2 and KATRIN (NM2), the Dirac
  phase in the results of UM-3 (NM3), what the lightest mass changes (NM4), the record against NuFIT 6.0 (NM5).

The Kohn-Sham module runs in parts (`um3_kohnsham.py part NAME` for NAME = K1, I, II, III, K6, K9, then
`um3_kohnsham.py assemble`), so that no single calculation takes longer than 423 seconds; the assembled results are identical to a
single run.
