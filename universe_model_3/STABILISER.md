---
title: "The stabiliser of the bulk"
subtitle: 'What the stabiliser of UM-3 was, why the field equations of the author''s metric with his original Lovelock weights required it, what it did and did not do, and why the corrected weights remove it: a complete account for a newcomer, with its provenance'
author:
  - "The stabiliser: found and named by Claude (Anthropic), 2026-10-24"
  - "This account and its checks: Claude (Anthropic), 2026-10-25"
  - "Underlying theory, metric and original Lovelock weights: Patrick L. Nash"
  - "Corrected Lovelock weights: derived by Claude at the author's order of 2026-10-25"
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
<!-- symbols: foldF, Xcoord, x0, x1, x7, Hconst, zvar, pi, Lambda, wL, LambdaN -->
<!-- begin generated symbol list -->
**Symbols in (FD-1).**

- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $\Lambda_{\mathrm{N}}$: The author's pure number in the vacuum equations of his notebook, $\Lambda = -\Lambda_{\mathrm{N}}H^2$: his original value 10, corrected to 7 on 2026-10-25. Unit: dimensionless. Value: 7 (the author's original 10). Status: AUTHOR.

<!-- end generated symbol list -->

$X = \{x_0, \dots, x_7\}$ are the author's coordinates: $x_0$ the hidden space-like direction, $x_1, x_2, x_3$ ordinary space,
$x_4$ the time, $x_5, x_6, x_7$ the three extra times; $H$ is the author's constant (an inverse length). The author's metric
depends on $x_0$ only through $\cot^2z$ and $(\sin^2z)^{1/6}$, so it repeats with the period $\pi/(6H)$ of $x_0$, and every
period $0 < z < \pi$ contains exactly one surface of $\mathcal{F}$, at $z = \pi/2$: $\mathcal{F}$ is the union of these copies,
one per period (example 2), and "the fold" without a qualifier is the copy in the period that contains our world. A point of
the fold is labelled by the seven coordinates $x_1, \dots, x_7$, and the metric restricted to the fold ($\mathrm{d}x_0 = 0$,
$z = \pi/2$) is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N\big\vert_{\mathcal{F}} = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big) \tag{FD-2}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, foldF, euler, a4, b4, x1, x2, x3, x4, x5, x6, x7, prime -->
<!-- begin generated symbol list -->
**Symbols in (FD-2).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.

<!-- end generated symbol list -->

with three space-like and four time-like directions; $a_4$ and $b_4$ are the author's two functions of the time $x_4$.
Notation: $\ln$ is the natural logarithm, $\mathrm{e}$ Euler's number, $\exp(y) = \mathrm{e}^y$, $\sin$, $\cos$ and
$\cot = \cos/\sin$ the trigonometric functions, $\tanh$ the hyperbolic tangent, $\lvert y\rvert$ the absolute value;
$f(0^+)$ and $f(0^-)$ are the limits of $f(\sigma)$ as $\sigma$ approaches 0 from above and from below.

**Why this surface is called a fold.** Measured by the proper distance along the hidden direction,

$$
\sigma = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H},\qquad \mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0,\qquad
\sin z = \mathrm{e}^{-6H\lvert\sigma\rvert} \tag{FD-3}
$$
<!-- symbols: sigma, sgn, pi, zvar, Hconst, diff, x0, euler, infty -->
<!-- begin generated symbol list -->
**Symbols in (FD-3).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.

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
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

It depends on $\sigma$ only through $\lvert\sigma\rvert$. The function $\mathcal{W}(\sigma) = \mathrm{e}^{-2H\lvert\sigma\rvert}$,
which multiplies the squared steps of ordinary space and of the extra times, is the warp factor of the metric (its square
root $\mathrm{e}^{-H\lvert\sigma\rvert}$ multiplies the lengths); the time $x_4$ is not warped. Four properties make the surface
$\sigma = 0$ a fold, and together they single it out within the period:

1. *It is a mirror.* The reflection $\sigma \to -\sigma$ (that is $z \to \pi - z$, or $x_0 \to \pi/(6H) - x_0$) maps the metric
   to itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
   period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are joined
   along the crease.
2. *The warp factor is largest on it.* The warp factor $(\sin^2z)^{1/6} = \mathrm{e}^{-2H\lvert\sigma\rvert}$ equals 1 on the
   fold and decreases on both sides.
3. *The metric has a kink on it.* The metric is continuous across the fold, but its first derivative along $\sigma$ jumps.
   The extrinsic curvature of the surfaces $\sigma = \text{const}$ changes sign across the fold,

$$
K^a{}_b = \frac12\,g^{ac}\,\partial_\sigma g_{cb}:\qquad
K^{1}{}_{1} = K^{2}{}_{2} = K^{3}{}_{3} = K^{5}{}_{5} = K^{6}{}_{6} = K^{7}{}_{7} = -H\,\mathrm{sgn}(\sigma),\qquad K^{4}{}_{4} = 0 \tag{FD-5}
$$
<!-- symbols: Kextr, ia, ib, ic, metric, partial, isigma, sigma, Hconst, sgn, eta, diag -->
<!-- begin generated symbol list -->
**Symbols in (FD-5).**

- $K^a{}_b$: The extrinsic curvature of a surface of constant $\sigma$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along ordinary space and the extra times, 0 along the time. Unit: GeV (1/length). Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $c$: A frame index (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.

<!-- end generated symbol list -->

   ($a, b$ frame indices along the fold); it jumps by $-2H$ along ordinary space and along the extra times. The
   Einstein-Lovelock equations of UM-3, $\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b + \Lambda\delta^a{}_b = \kappa\mathcal{T}^a{}_b$
   ($\mathcal{E}_{(p)}$ the Lovelock tensor of order $p = 1, 2, 3$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ its coupling with the weights
   $w = (1, 1/20, 1/360)$, $\Lambda = -7H^2$ the cosmological constant, $\kappa = 8\pi G_8$ the gravitational coupling of eight
   dimensions, $\mathcal{T}^a{}_b$ the energy-momentum tensor, $\delta^a{}_b$ the Kronecker delta), are linear in the second
   $\sigma$-derivatives of the metric, so the jump puts a Dirac delta function $\delta_{\mathrm{D}}(\sigma)$ into them: the
   metric solves them only if the fold carries a thin source $\mathcal{S}^a{}_b$, an energy-momentum tensor concentrated on
   $\sigma = 0$, given by the integral of the equations across the fold (the junction conditions),

$$
\kappa\,\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b \tag{FD-11}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, diff, sigma, ip, alphaL, LovE, G8, Riemann, LovL -->
<!-- begin generated symbol list -->
**Symbols in (FD-11).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

   with $\mathcal{S}^4{}_4 = -(\text{its energy density})$, $\mathcal{S}^1{}_1 = \mathcal{S}^2{}_2 = \mathcal{S}^3{}_3$ its pressure
   along ordinary space and $\mathcal{S}^5{}_5 = \mathcal{S}^6{}_6 = \mathcal{S}^7{}_7$ its pressure along the extra times;
   $\mathcal{S}$ is $\mathcal{T}$ integrated across the fold, an energy per unit volume of the six other directions of the fold
   (unit GeV$^7$). On the static block ($a_4$ and $b_4$ constant) and on an expanding fold whose extra times are frozen
   ($b_4$ proportional to $\mathrm{e}^{a_4}$; $\mathsf{A} = a_4'/H$, $\mathsf{A}_1 = a_4''/H^2$)

$$
\begin{aligned}
&\text{static block:}\quad \kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\,\delta^a{}_b\quad\text{(a pure tension)},\\
&\text{frozen extra times:}\quad \kappa\mathcal{S}^1{}_1 = -\frac{16}{15}\big(6 + 3\mathsf{A}^2 + 2\mathsf{A}_1\big)H,\quad
 \kappa\mathcal{S}^4{}_4 = -\frac{16}{5}\big(2 + \mathsf{A}^2\big)H,\\
&\qquad\qquad \kappa\mathcal{S}^5{}_5 = -\frac45\big(8 + 8\mathsf{A}^2 + \mathsf{A}^4 + 4\mathsf{A}_1 + \mathsf{A}^2\mathsf{A}_1\big)H
\end{aligned} \tag{FD-12}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, Hconst, delta, Asf, A1sf, H4, h100 -->
<!-- begin generated symbol list -->
**Symbols in (FD-12).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.

<!-- end generated symbol list -->

   the tension plus matter that obeys the Friedmann equations of general relativity. The fold is therefore not only a place
   but a physical object: a thin layer that carries energy and momentum (a brane). (FD-11 and FD-12 were added to this
   definition on 2026-10-25, after FD-1 to FD-10, with the corrected Lovelock weights; they stand here because they belong to
   property 3.)
4. *The author's coordinate $x_0$ degenerates on it.* The metric component $g_{x_0x_0} = \cot^2(6Hx_0)$ vanishes on the fold
   and nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,

$$
\lvert\sigma\rvert = 3H\Big(x_0 - \frac{\pi}{12H}\Big)^2\Big[1 + 6H^2\Big(x_0 - \frac{\pi}{12H}\Big)^2 + \dots\Big] \tag{FD-6}
$$
<!-- symbols: sigma, Hconst, x0, pi -->
<!-- begin generated symbol list -->
**Symbols in (FD-6).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

   so the two coordinate values on either side of $x_0 = \pi/(12H)$ at the same coordinate distance lie at the same proper
   distance from the fold: the coordinate line of $x_0$ is folded onto the line of proper distances (a fold map, example 5).

**What lives on the fold.** In UM-3 the Standard Model (the Higgs doublet with the author's ad hoc vacuum, a time-dependent
choice of its vacuum value; the gauge fields of $SU(3)_C \times SU(2)_L \times U(1)_Y$; three generations of quarks and
leptons and three right-handed neutrinos) and the fold fluid (its tension and the pressure along the extra times that keeps
their volume fixed) live on the fold: they are fields at $\sigma = 0$, functions of $x_1, \dots, x_4$ (no field depends on
the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we observe, with the
metric $\mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in $x_1, \dots, x_4$. dirac16complex (the
author's spinor field of eight dimensions) and gravity live in the bulk $\sigma \ne 0$ as well as on the fold; the bound
states $\chi$ of dirac16complex are the part of it that the fold holds, and the portals (couplings between dirac16complex and
Standard-Model fields) act at $\sigma = 0$. In UM-3 files "the fold" means this surface; the examples below use the word
for other surfaces with the same properties. The word is not used in its other senses: a set of equal energy levels is
called degenerate, and a growth by the factor $\mathrm{e}$ is called an e-folding.

**Examples of folds that are meaningful for UM-3.**

1. *Our fold.* The fold $z = \pi/2$ of the period that contains our world (FD-1): the seven-dimensional world-volume of the
   Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
2. *The copies of the fold.* Because the metric repeats with the period $\pi/(6H)$, every surface
   $x_0 = \pi/(12H) + (\text{an integer multiple of } \pi/(6H))$ is a copy of the fold, one per period. Neighbouring copies are
   separated by a tip ($z$ a multiple of $\pi$), where the warp factor $(\sin^2z)^{1/6}$ vanishes and $g_{x_0x_0} = \cot^2z$
   diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
   line $-\infty < \sigma < \infty$. A compact direction of length $L$ would give every field a tower of particles with the
   masses $2\pi n/L$, $n = 1, 2, \dots$ (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
   $\pi/(6H)$ of $x_0$ produces no such tower with the spacing $12H$, and the $x_0$ mass of the bound states is their binding
   to the fold.
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

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.

<!-- end generated symbol list -->

   whose delta function is the origin of the thin source of property 3. Every metric function of FD-4 depends on $\sigma$
   through $\lvert\sigma\rvert$ and is folded at $\sigma = 0$ in this sense.
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

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $y_{\mathrm{RS}}$: The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-3). Unit: length. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $k_{\mathrm{RS}}$: The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp factor of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-3). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\lambda_{\mathrm{RS}}$: The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^4$. Status: STANDARD.
- $\kappa_5$: The gravitational coupling of five dimensions in the model of Randall and Sundrum, $8\pi$ times the Newton constant of five dimensions (FD-8, an example, not UM-3). Unit: GeV$^{-3}$. Status: STANDARD.
- $\Lambda_{\mathrm{RS}}$: The vacuum energy density of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2/\kappa_5$ (FD-8, an example, not UM-3). Unit: GeV$^5$. Status: STANDARD.

<!-- end generated symbol list -->

   has a fold at $y_{\mathrm{RS}} = 0$ with the properties 1 to 3 (its coordinate $y_{\mathrm{RS}}$ is already the proper
   distance, so property 4 does not arise); Einstein's equations require there a brane of the tension $\lambda_{\mathrm{RS}}$
   (Israel's junction condition) and in the bulk the vacuum energy $\Lambda_{\mathrm{RS}}$, and the bulk is otherwise empty. The
   fold of UM-3 is of the same kind: its static block is a vacuum of the bulk with a fold of pure tension (FD-12). It differs
   in that the time $x_4$ is not warped, three extra times are warped together with ordinary space, the Lovelock terms add to
   the junction conditions, and the space is not cut at the brane: Randall and Sundrum identify the two sides of their brane
   (one physical side), while the fold of UM-3 has two distinct sides (example 7).
7. *A particle bound to a thin layer.* A particle held by an attractive thin layer has a wave function that falls off
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
<!-- symbols: chiprof, sigma, euler, qb, gammaM, muX, PL, PR, Gamma8, identity, omegab, mPsi, Vstar, Psi, vielbein, imag, omegafreq, kvec, xvec, Vt, sigma16, dagger, io -->
<!-- begin generated symbol list -->
**Symbols in (FD-9).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.

<!-- end generated symbol list -->

   where $\mu_{\mathrm{L}}$, $\mu_{\mathrm{R}}$ are the strengths of the fold for the left- and right-handed halves of
   dirac16complex (set by the Standard-Model fields on the fold) and $q_{\mathrm{b}} = -m_\Psi(\mu_{\mathrm{L}} + \mu_{\mathrm{R}})\tanh\varsigma/(2\varsigma)$,
   $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$ for $\mu_{\mathrm{R}} = 0$). The profile
   is not a function of $\lvert\sigma\rvert$: it jumps at the fold, $\chi(0^+) \ne \chi(0^-)$.
8. *The fold as a mirror for dirac16complex.* The reflection across the fold acts on the profiles $\chi(\sigma)$ in two ways,

$$
(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma),\qquad (\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma) \tag{FD-10}
$$
<!-- symbols: R1refl, R2refl, chiprof, sigma, Tmat -->
<!-- begin generated symbol list -->
**Symbols in (FD-10).**

- $\mathsf{R}_1$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of ordinary space, $(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma)$ (FD-10): a symmetry of dirac16complex, of gravity and of the mean field of the gas of the particles $\chi$; the bound states of Krein charge $-1$ are even, those of Krein charge $+1$ odd. Unit: dimensionless. Status: DERIVED.
- $\mathsf{R}_2$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of the extra times, $(\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma)$ (FD-10): it maps the bound states of one Krein charge onto those of the other. Unit: dimensionless. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

   ($T_a$ the author's Dirac matrices; for states at rest $\mathsf{R}_1$ is the reflection across the fold combined with the
   reflection of ordinary space, $\mathsf{R}_2$ the reflection across the fold combined with the reflection of the extra
   times). The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a
   state can carry the charge $-1$ or $+1$. $\mathsf{R}_1$ is a symmetry of dirac16complex, of gravity and of the mean
   field of a gas of the particles $\chi$ (the average field that the particles of the gas create and feel): the four bound
   states of Krein charge $-1$ (the particles $\chi$) are even under it and the four of Krein charge $+1$ are odd, so the
   mean field of the gas cannot mix the two signs of the indefinite charge. $\mathsf{R}_2$ maps the bound states of one
   Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
9. *The planes of Horava and Witten.* In M-theory (the eleven-dimensional theory whose limits include the superstring
   theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional planes
   left in place by the reflection are mirror surfaces (property 1); each carries one $E_8$ gauge group while gravity fills
   the bulk. As in UM-3, the gauge fields live on the mirror surface and gravity in the bulk; unlike UM-3, the two sides of
   each plane are identified (one physical side).

**What is not a fold.**

* *The tips* $z = 0$ and $z = \pi$ (mod $\pi$): the mirror exchanges them within a period, but there the warp factor vanishes,
  $g_{x_0x_0}$ diverges, and they lie at an infinite proper distance; they carry no thin source.
* *A smooth maximum of a warp factor*, such as $1/\cosh^2(H\sigma)$: mirror symmetric and largest at $\sigma = 0$, but without a
  kink and without a thin source.
<!-- end fold definition -->

# How to read this document

## Who this document is for

It is written for a reader who is clever but new to the subject: someone who knows what a coordinate, a derivative, an energy
and a pressure are, but not general relativity, warped geometries or the universe model UM-3. Every term is explained where it is
first used, every equation that the document uses is written out in it, and every symbol of every display equation is listed and
defined right after the display. Nothing has to be looked up anywhere else.

## The status labels

Every statement carries one of the labels **AUTHOR** (from the author, Patrick L. Nash: his notebooks
`Dirac_Einstein-Lovelock_4+4_Nash.nb` and `4+4.nb` and his orders of 2026-10-24 and 2026-10-25), **RECORD** (from the earlier
record of this repository, such as the Lagrangian of dirac16complex), **STANDARD** (textbook physics or a published measurement,
named in the provenance), **ASSUMED** (a choice made in UM-3 without derivation), **DERIVED** (computed and verified in UM-3; the
check that verifies it is named, e.g. ST1), **ESTIMATE** (an order-of-magnitude evaluation) and **OPEN** (not settled). A result that
holds only for the author's original Lovelock weights, which UM-3 no longer uses, is called a record of the original weights.

## Every equation is followed by its symbols

A display equation carries a tag. SB-n is an equation of this document; FD-n belongs to the definition of the fold at the
beginning; FE-n (a field equation) and IN-n (a term of the action) are equations of UM-3 that are written identically, with the
same tag, in every UM-3 document that uses them. After every display comes the list "Symbols in ..." of every symbol in it, with
its meaning, its unit, its value where one exists, and its status. A symbol that one of these meanings uses is itself listed in this document. The units are natural units: the reduced Planck constant and
the speed of light are 1, so that a time is a length, and energies, masses and inverse lengths are all measured in GeV.

## The checks

Most statements labelled DERIVED in this document are verified by the nine checks ST1 to ST9 of a program that computes the field
equations exactly with computer algebra (ST1 to ST8 with the author's original weights, ST9 with the corrected ones). The others are
verified by checks of the other programs of UM-3, named where they are used: the gravitational waves and the corrected weights (W1
to W8), the linearised field equations for every perturbation of the metric (LN1 to LN5), the curvature and the bulk equations of the
author's metric (G2 to G4), the junction conditions and the fold sources (J4 to J7), and the proper distance of the definition of the
fold. The provenance at the end says what each check does and how to run it.

# The stabiliser in brief

UM-3 is a model universe built on a metric (a rule for measuring distances and durations, explained below) that the author wrote
down for an eight-dimensional spacetime. The metric has a fold, the surface defined at the beginning of this document, and around
it the bulk: everything that is not on the fold. Gravity in UM-3 obeys the Einstein-Lovelock field equations, which say how the
curvature of spacetime is fixed by the energy that it contains. These equations contain three weights and a cosmological constant.

**The finding (with the author's original weights).** When the universe is old and expands slowly, as ours does, the bulk of the
author's metric is very nearly static: nothing in it changes with time. With the weights and the cosmological constant of the
author's notebook, a static bulk of this metric is **not** a solution of the field equations with empty space. The equations
demanded a definite energy content: a negative energy density, and a negative pressure five times as large, the same in every
direction of the bulk except the time (SB-9). UM-3 called whatever supplies it **the stabiliser of the bulk**, because without it
the bulk could not stay static. It had no free parameter: its energy density and its pressure were fixed by the author's constant
$H$ and the gravitational coupling $\kappa$.

**Who found it.** The requirement and the stabiliser are not part of the author's specification. They were found, introduced and
named by Claude, an AI model made by Anthropic, working in Claude Code sessions configured for the model claude-opus-5-5, on
2026-10-24 while it derived the complete field equations of UM-3. The idea of something that holds a static block of the bulk is
older in this repository: the two earlier universe models assumed a "block stabiliser" of their own (the provenance gives the
lineage); the stabiliser of UM-3, for the author's new metric, was a different object with a definite, negative energy density.

**The correction.** On 2026-10-25 the author ordered: "Gravitons must travel at c. If these incorrect claims come from my choice of
the Lovelock couplings and my choice of the cosmological constant $\Lambda$ THEN my choices are wrong, and you MUST correct them." With
the original weights, gravitational waves in the bulk moved $\sqrt5 = 2.24$ times faster than light. There is exactly one choice of
the two higher weights for which the graviton of our four-dimensional world, on the fold, travels at the speed of light while no
graviton of the static bulk travels faster, and with it exactly one cosmological constant makes the static bulk empty (FE-68 to
FE-70). UM-3 now uses these values; the criterion is a choice, made because the order cannot be met in full. With them the static
bulk has no gravitational waves at all at the lowest order, and no choice of the weights gives
gravitational waves at the speed of light in the bulk as well, because the time of the author's metric is not warped (the part on the
correction explains both). **The stabiliser was a consequence of the author's original weights and cosmological constant; with the
corrected ones the static bulk is a vacuum, and the stabiliser vanishes** (IN-7, ST9).

**The five points of the author's order of 2026-10-25, in brief.**
1. *The stabiliser couples only to gravity.* That is how UM-3 defined it, and on the static bulk it was consistent: the stabiliser was
   conserved by itself (ST4). In an expanding universe the bulk source that the original equations required released energy that flowed
   along the hidden direction into the fold (ST6); reading this as an exchange of energy between the stabiliser and the matter of the
   fold is an interpretation (ASSUMED). With the corrected weights the question disappears: there is no stabiliser, and the bulk of an
   expanding fold with frozen extra times is a vacuum without any flow (FE-33).
2. *It is absent in the primordial era, whose bulk is the author's vacuum (FE-31).* With the original weights this was true: the author's
   vacuum solved the bulk equations with no source (ST2), and a medium that couples only to gravity with a pressure five times its
   energy density could not appear later out of nothing (ST6). With the corrected weights the author's vacuum is not a solution any more,
   the primordial era can be an inflation of the fold (a period of exponential expansion of ordinary space; it needs an enormous
   pressure that holds the volume of the extra times fixed, whose origin is OPEN), and no era of UM-3 has a stabiliser.
3. *Its existence and value are DERIVED from the requirement of a static bulk.* True: the static bulk fixed every entry (ST1), and a bulk
   without any source could only be the author's vacuum or its time reverse at every instant (ST3, ST8). That the source was a separate
   medium was ASSUMED. With the corrected weights the same derivation gives the value zero (ST9).
4. *The static bulk* is explained, with five examples, in the part "The static bulk".
5. *Warp and warp factor* are defined, with four examples, in the part "Warp and warp factor".

**Its importance.** With the original weights the stabiliser was what made a slowly expanding late universe with constant couplings
possible in the author's metric; it was also the most exotic ingredient of the model, because it violated the null energy condition.
Its removal by the corrected weights changes UM-3 in five ways: the gravitational waves of the four-dimensional world travel at the
speed of light at every wavelength, at the lowest order; the fold obeys the Friedmann equations of general relativity exactly; the bulk
needs no exotic medium; the bulk has no gravitational waves of its own at the lowest order, so that its response to matter is not
computed (it is strongly coupled, a term explained in the part on the correction); and a new requirement appears on the fold, a pressure
along the extra times that holds their volume fixed, a role that the "block stabiliser" of the first universe model of this repository
had played for its own metric.

# The language

## Coordinates, distances and the metric

A point of space and time is labelled by numbers, its coordinates. Ordinary space needs three ($x_1, x_2, x_3$) and time one
($x_4$). The spacetime of UM-3 has eight: $x_0$, a hidden direction that we do not see, $x_1, x_2, x_3$ ordinary space, $x_4$ the
time, and $x_5, x_6, x_7$ three extra directions that behave like time (the extra times). The metric is the rule that turns a
small step of the coordinates into the squared length (or the squared duration) of the step. A familiar example is the surface of
a globe of radius $R_{\mathrm{g}}$, on which a point is labelled by its angle $\theta_{\mathrm{g}}$ from the north pole and its
longitude $\phi_{\mathrm{g}}$:

$$
\mathrm{d}\ell_{\mathrm{g}}^2 = R_{\mathrm{g}}^2\,\mathrm{d}\theta_{\mathrm{g}}^2 + R_{\mathrm{g}}^2\sin^2\theta_{\mathrm{g}}\;\mathrm{d}\phi_{\mathrm{g}}^2 \tag{SB-1}
$$
<!-- symbols: diff, ellg, Rglobe, thglobe, phglobe -->
<!-- begin generated symbol list -->
**Symbols in (SB-1).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\ell_{\mathrm{g}}$: The length measured along the surface of a globe; $\mathrm{d}\ell_{\mathrm{g}}$ is the length of a small step on it (an example of a metric, not UM-3). Unit: length. Status: STANDARD.
- $R_{\mathrm{g}}$: The radius of a globe (an example, not UM-3). Unit: length. Status: STANDARD.
- $\theta_{\mathrm{g}}$: The angle of a point of a globe from its north pole: 0 at the north pole, $\pi/2$ on the equator, $\pi$ at the south pole (an example, not UM-3). Unit: radian. Status: STANDARD.
- $\phi_{\mathrm{g}}$: The longitude of a point of a globe (an example, not UM-3). Unit: radian. Status: STANDARD.

<!-- end generated symbol list -->

A step of the longitude by $\mathrm{d}\phi_{\mathrm{g}}$ is long on the equator ($\sin\theta_{\mathrm{g}} = 1$) and short near the
poles: the factor $R_{\mathrm{g}}^2\sin^2\theta_{\mathrm{g}}$ in front of $\mathrm{d}\phi_{\mathrm{g}}^2$ says how large one unit of longitude
is at each latitude ($\sin$ is the sine function; $\mathrm{d}$ marks a small step). Status: STANDARD.

The metric of the eight-dimensional spacetime is written $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$: the indices $M$ and $N$ run over
the eight coordinates $X = \{x_0, \dots, x_7\}$, a repeated index is summed, and the numbers $g_{MN}$ are the components of the
metric. In spacetime a step can be space-like (a positive squared interval: a distance) or time-like (a negative one: minus the
square of a duration). UM-3 counts $x_0, x_1, x_2, x_3$ as space-like and $x_4, x_5, x_6, x_7$ as time-like (the signature
$+,+,+,+,-,-,-,-$). The author's metric is written in FD-4 of the definition of the fold with the proper distance $\sigma$ from
the fold: $\mathrm{d}\sigma^2$ for the hidden direction, a factor that depends on $\sigma$ in front of ordinary space and of the
extra times, and $-\mathrm{d}x_4^2$ for the time. The two functions $a_4(x_4)$ and $b_4(x_4)$ of the time are the author's: at the
depth $\lvert\sigma\rvert$, a coordinate step of ordinary space has the length $\mathrm{e}^{a_4}\mathrm{e}^{-H\lvert\sigma\rvert}$ times the step,
and a coordinate step of an extra time the duration $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ times the step; on the fold,
$\mathrm{e}^{a_4}$ is the size of ordinary space and $\mathrm{e}^{-a_4}b_4$ that of the extra times ($\mathrm{e}$ is Euler's number,
$\lvert\sigma\rvert$ the absolute value). Status: AUTHOR (the metric), DERIVED (its form in $\sigma$, FD-3 and FD-4).

## Warp and warp factor

**Definition.** A metric is *warped* along a direction when the size of other directions depends on the position along it. In a
metric of the form $\mathrm{d}\sigma^2 + \mathcal{W}(\sigma)\,\mathrm{d}y^2 + \dots$ the function $\mathcal{W}(\sigma)$ that
multiplies the squared steps $\mathrm{d}y^2$ of the other directions is the **warp factor**. The length of a fixed coordinate step
$\mathrm{d}y$ is $\sqrt{\mathcal{W}}\,\mathrm{d}y$, so lengths along those directions scale with $\sqrt{\mathcal{W}}$. The **warp**
is the dependence itself, measured by the rate at which the natural logarithm $\ln\mathcal{W}$ changes along $\sigma$. In UM-3:

$$
\mathcal{W}(\sigma) = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6},\qquad
\frac{\mathrm{d}\ln\mathcal{W}}{\mathrm{d}\sigma} = -2H\,\mathrm{sgn}(\sigma) \tag{SB-2}
$$
<!-- symbols: Wwarp, euler, Hconst, sigma, zvar, diff, sgn -->
<!-- begin generated symbol list -->
**Symbols in (SB-2).**

- $\mathcal{W}$: The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-3 the function of $\sigma$ that multiplies ordinary space and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold. Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.

<!-- end generated symbol list -->

The warp factor multiplies ordinary space (together with $\mathrm{e}^{2a_4}$) and the extra times (together with
$\mathrm{e}^{-2a_4}b_4^2$), but not the time $x_4$ and not $\sigma$ itself. The warp factor is largest, 1, on the fold and falls on both
sides. A coordinate step of ordinary space at the depth $\lvert\sigma\rvert$ in the bulk is $\mathrm{e}^{-H\lvert\sigma\rvert}$ times as long as
the same coordinate step on the fold: the deeper in the bulk, the smaller ordinary space and the extra times become. The warp factor is
the same on both sides of the fold; the warp, its logarithmic rate of change, has the constant size $2H$ and changes its sign on the
fold ($\mathrm{sgn}$ is the sign function): this jump is the kink of the fold (property 3 of the definition). Status: AUTHOR (the metric),
DERIVED (the form in $\sigma$).

**Examples of warps.**

* *A globe* (SB-1): the longitude is warped along the angle from the pole, with the warp factor $R_{\mathrm{g}}^2\sin^2\theta_{\mathrm{g}}$
  in the proper coordinate $R_{\mathrm{g}}\theta_{\mathrm{g}}$ (the distance from the pole along a meridian).
* *The fold of UM-3* (SB-2): ordinary space and the extra times are warped along the hidden direction.
* *The brane of Randall and Sundrum* (FD-8, example 6 of the definition of the fold): the four directions of our world are warped
  by the warp factor $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ along a fifth direction. Unlike in UM-3, the time is warped as well.
* *Time near the Earth.* Near a mass the time is warped. In the weak gravity of the Earth the factor in front of $-\mathrm{d}x_4^2$
  is $1 + 2\Phi_{\mathrm{N}}$, where $\Phi_{\mathrm{N}}$ is the Newtonian gravitational potential (negative, and larger in size
  closer to the Earth). A clock lower down therefore runs slower. Pound and Rebka measured this in 1960 over the 22.5 m height of
  a tower, and the clocks of the GPS satellites are corrected for it. In UM-3 the time is not warped along the hidden direction:
  a clock deep in the bulk runs at the same rate as a clock on the fold.

## The bulk

**Definition.** The bulk is all of the eight-dimensional spacetime except the fold: the points with $\sigma \neq 0$. It extends
on both sides of the fold to the tips, which lie at an infinite proper distance. Gravity and dirac16complex live in the bulk as
well as on the fold; dirac16complex is the author's field of matter of spin one half in eight dimensions, a spinor with sixteen
complex components. The Standard Model of particle physics lives only on the fold. Status: ASSUMED (where the fields live), AUTHOR
(the metric and dirac16complex).

## Energy, pressure and the energy-momentum tensor

Matter and fields carry energy and momentum. Their densities and flows are collected in the energy-momentum tensor, an
eight-by-eight array whose entries are measured along the eight directions of an orthonormal frame: the frame direction $(0)$
along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time and $(5), (6), (7)$ along the extra times. For a medium
at rest the entry along the time is minus its energy density, the entries along the other directions are its pressures, and an
entry that mixes the time with another direction is a flow of energy along that direction. A medium at rest with the same
pressure $p_{\mathrm{med}}$ in every direction but the time has

$$
\mathcal{T}_{\mathrm{med}}{}^a{}_b = \mathrm{diag}\big(p_{\mathrm{med}}, p_{\mathrm{med}}, p_{\mathrm{med}}, p_{\mathrm{med}},
 -\rho_{\mathrm{med}}, p_{\mathrm{med}}, p_{\mathrm{med}}, p_{\mathrm{med}}\big) \tag{SB-3}
$$
<!-- symbols: Tmed, ia, ib, diag, pmed, rhomed -->
<!-- begin generated symbol list -->
**Symbols in (SB-3).**

- $\mathcal{T}_{\mathrm{med}}{}^a{}_b$: The energy-momentum tensor of one medium (frame components): for a medium at rest the entry along the time is minus its energy density, the entries along the other directions are its pressures, and the entries that mix the time with another direction are its flows of energy along that direction. Unit: GeV$^8$ (energy per volume in eight dimensions). Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $p_{\mathrm{med}}$: The pressure of a medium at rest, the same along every direction but the time (for a medium of the bulk: along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Status: STANDARD.
- $\rho_{\mathrm{med}}$: The energy density (energy per volume) of a medium at rest. Unit: GeV$^8$. Status: STANDARD.

<!-- end generated symbol list -->

Three examples in the four dimensions of our world: dust (pressureless matter, $p_{\mathrm{med}} = 0$), light
($p_{\mathrm{med}} = \rho_{\mathrm{med}}/3$) and the energy of the vacuum ($p_{\mathrm{med}} = -\rho_{\mathrm{med}}$). A positive vacuum energy is
a tension: it pulls instead of pushing, like a stretched skin. Yet its gravity is repulsive, because in general relativity pressure
gravitates too: the source of the attraction is $\rho + 3p$ in four dimensions, and a tension with $p = -\rho$ makes it negative. This is
why a positive cosmological constant makes a universe expand faster. Two energy conditions classify media: the weak energy condition
(the energy density is never negative) and the null energy condition (the energy density plus the pressure along any space-like
direction is never negative; for the frame of UM-3, which has four time-like directions, the condition is taken for light moving along
the time $x_4$ and one space-like direction). Ordinary matter, light and a positive vacuum energy satisfy both. A negative vacuum energy,
such as the negative cosmological constant of the bulk of UM-3, violates the weak condition but not the null one, since its energy
density plus its pressure is zero. A medium that violates the null condition is called exotic. Status: STANDARD.

## The field equations of gravity

Einstein's insight was that gravity is the curvature of spacetime, and that the curvature is fixed by the energy-momentum tensor.
One side of his field equations is a combination of derivatives of the metric (the Einstein tensor); the other is the
energy-momentum tensor times the gravitational coupling. UM-3 uses the generalisation found by Lovelock, which in eight dimensions
adds two more combinations of the curvature, each with a weight. The action (the quantity whose variation gives the equations) and its
curvature terms are

$$
\begin{aligned}
S_{\mathrm{EL}} &= \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)}
 - 2\Lambda\Big),\qquad \kappa = 8\pi G_8,\\
\alpha_{(p)} &= w_{(p)}\,H^{2-2p},\qquad w_{(1)} = 1,\quad w_{(2)} = \frac{1}{20},\quad w_{(3)} = \frac{1}{360},
 \qquad \Lambda = -7H^2
\end{aligned} \tag{IN-2}
$$
<!-- symbols: SEL, kappa, diff, Xcoord, metric, ip, alphaL, LovL, Lambda, pi, G8, wL, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-2).**

- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity in eight dimensions. Unit: dimensionless. Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

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

- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.

<!-- end generated symbol list -->

The curvature is measured by the Riemann tensor $R$, which says how much a direction turns when it is carried around a small loop; the
generalised Kronecker delta $\delta$ is the totally antisymmetric combination of ordinary Kronecker deltas, $+1$ or $-1$ when its lower
indices are an even or odd rearrangement of its upper ones and 0 otherwise. The weights in IN-2 are the corrected ones; the author's
notebook had $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ and $\Lambda = -10H^2$ (he writes the pure number 10 in his vacuum equations). Varying the
action with respect to the inverse metric $g^{MN}$ and dividing by $\sqrt{\lvert g\rvert}$ gives the Lovelock tensors

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

- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $S$: A coordinate index of eight dimensions, running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

($R^M{}_N$ the Ricci tensor and $R$ the scalar curvature, contractions of the Riemann tensor), and the field equations of the bulk are

$$
\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_N + \Lambda\,\delta^M_N
 = \kappa\,\mathcal{T}_\Psi{}^M{}_N\qquad (\sigma \ne 0) \tag{FE-1}
$$
<!-- symbols: ip, alphaL, LovE, iM, iN, Lambda, delta, kappa, TPsi, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-1).**

- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex: $-2/\sqrt{\lvert g\rvert}$ times the variation of the action $S_\Psi$ of dirac16complex with respect to $g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

The left-hand side is built from the metric alone. The right-hand side is the energy content of the bulk: dirac16complex, and, with
the original weights, the stabiliser. A metric solves the equations only if the right-hand side has exactly the value that the
left-hand side computes; a solution with nothing on the right is a *vacuum*. Status: AUTHOR (the theory), STANDARD (Lovelock gravity),
DERIVED (the corrected weights).

The divergence of every Lovelock tensor vanishes identically (the Bianchi identity). The right-hand side must therefore be
conserved: the energy and momentum of all sources together cannot be created or destroyed, only moved. A single medium that
interacts with nothing but gravity is conserved by itself:

$$
\nabla_M\,\mathcal{T}_{\mathrm{med}}{}^M{}_N = 0 \tag{SB-4}
$$
<!-- symbols: nabla, Tmed, iM, iN, Christoffel -->
<!-- begin generated symbol list -->
**Symbols in (SB-4).**

- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.
- $\mathcal{T}_{\mathrm{med}}{}^a{}_b$: The energy-momentum tensor of one medium (frame components): for a medium at rest the entry along the time is minus its energy density, the entries along the other directions are its pressures, and the entries that mix the time with another direction are its flows of energy along that direction. Unit: GeV$^8$ (energy per volume in eight dimensions). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Gamma^P{}_{MN}$: The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection). Unit: 1/length. Status: STANDARD.

<!-- end generated symbol list -->

($\nabla$ is the covariant derivative, the derivative that takes into account how the directions of the coordinates change from
point to point.) Status: STANDARD.

**The junction conditions.** The metric has a kink at the fold, so its second derivatives along $\sigma$ contain a Dirac delta function
there, and the field equations hold across the fold only if the fold carries a thin source $\mathcal{S}$, its energy-momentum tensor
integrated across it (unit GeV$^7$: an energy density times a length): the integral FD-11 of the definition of the fold. For the
Einstein term alone this is Israel's condition (1966): $\kappa\mathcal{S}^a{}_b = -([K^a{}_b] - \delta^a{}_b[K])$, with the jump $[K^a{}_b]$ of the
extrinsic curvature of the fold (FD-5) and its trace $[K]$; for the Gauss-Bonnet and cubic terms the integral adds terms of higher order
in the extrinsic curvature and the curvature of the fold (Davis 2003; Gravanis and Willison 2003). Status: STANDARD.

# The static bulk

## What static means

**Definition.** A spacetime is *static* when nothing in it changes with the time and nothing flows: its metric does not depend on
the time, and no motion that the reversal of time would change takes place in it. In the author's metric the time dependence sits
in the two functions $a_4(x_4)$ and $b_4(x_4)$. The bulk is static when both are constant, that is when the rates
$\mathsf{A} = a_4'/H$ (the rate at which ordinary space grows) and $\mathsf{U} = b_4'/(Hb_4)$ (the rate at which $b_4$ changes)
both vanish:

$$
\begin{aligned}
&\mathsf{A} = \frac{a_4'}{H} = 0,\qquad \mathsf{U} = \frac{b_4'}{Hb_4} = 0:\\
&g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
 - \mathrm{d}x_4^2
\end{aligned} \tag{SB-5}
$$
<!-- symbols: Asf, a4, prime, Hconst, Usf, b4, metric, iM, iN, diff, Xcoord, sigma, euler, x1, x2, x3, x4, x5, x6, x7 -->
<!-- begin generated symbol list -->
**Symbols in (SB-5).**

- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

with constant $a_4$ and $b_4$ (a prime is the derivative with respect to the time $x_4$). UM-3 calls this the *static block*.
Status: DERIVED (the form), ASSUMED (that the late bulk is the static block to first approximation).

## Static is not the same as empty

A static spacetime may be empty or it may need a source, and an empty spacetime may be static or not:

| spacetime | static? | empty (a vacuum)? |
| --- | --- | --- |
| the static block of UM-3 (SB-5), corrected weights | yes | yes (IN-7) |
| the static block of UM-3 (SB-5), the author's original weights | yes | no: it needed the stabiliser (SB-9) |
| the author's vacuum (FE-31) | no: ordinary space grows at the rate $H$ | with the original weights yes; with the corrected weights no |
| the space outside a star | yes | yes |
| Einstein's static universe (SB-6) | yes | no: it needs dust and a cosmological constant |

## Examples of static spacetimes and static media

**Example 1: the static block of UM-3** (SB-5). It is the late universe to first approximation. Today ordinary space expands at the
Hubble rate $H_4^{(0)} = 1.44\times10^{-42}$ GeV. If the author's constant $H$ is much larger, the rate $\mathsf{A} = H_4^{(0)}/H$ is tiny and
the bulk is static up to corrections of order $\mathsf{A}$. The extra times are frozen ($\mathrm{e}^{-a_4}b_4$ constant, $\mathsf{U} = \mathsf{A}$),
so that the couplings of the Standard Model do not change. With the corrected weights the static block is an exact vacuum, and so is the
bulk of an expanding fold with frozen extra times for every expansion history (FE-33). Status: ASSUMED (the late universe), DERIVED
(the vacuum).

**Example 2: the space outside a star or a planet** (Schwarzschild's solution of 1916). It is static and empty: a static vacuum.
Not every static spacetime needs a source. Status: STANDARD.

**Example 3: Einstein's static universe** (1917). Einstein wanted a universe that does not change. With dust of the mass density
$\rho_{\mathrm{E}}$ and nothing else his equations do not allow it, because gravity pulls the dust together. He added a positive
cosmological constant $\Lambda_{\mathrm{E}}$, whose gravity is repulsive (it acts like a positive vacuum energy, a tension), and found a
static universe, a three-dimensional sphere of radius $R_{\mathrm{E}}$, but only for one exact balance:

$$
\Lambda_{\mathrm{E}} = 4\pi G_{\mathrm{N}}\,\rho_{\mathrm{E}} = \frac{1}{R_{\mathrm{E}}^2} \tag{SB-6}
$$
<!-- symbols: LambdaE, pi, GN, rhoE, RE, MPl -->
<!-- begin generated symbol list -->
**Symbols in (SB-6).**

- $\Lambda_{\mathrm{E}}$: The cosmological constant of Einstein's static universe of 1917, in four dimensions (an example, not UM-3). Unit: 1/length$^2$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{E}}$: The mass density of the dust that fills Einstein's static universe (an example, not UM-3). Unit: mass per volume. Status: STANDARD.
- $R_{\mathrm{E}}$: The radius of the three-dimensional sphere that is the space of Einstein's static universe (an example, not UM-3). Unit: length. Status: STANDARD.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.221\times10^{19}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->

This is the classic example of a static spacetime that requires a definite source. It is also unstable (Eddington, 1930): a small
excess of matter makes it collapse, a small deficit makes it expand for ever. Einstein's $\Lambda_{\mathrm{E}}$ played for his universe
the part that the stabiliser played for the bulk of UM-3 with the original weights. Status: STANDARD.

**Example 4: the air at rest above the ground.** The atmosphere stays at rest only because its pressure falls with the altitude
exactly so fast that the difference of pressure carries the weight of the air in between:

$$
\frac{\mathrm{d}P_{\mathrm{air}}}{\mathrm{d}h_{\mathrm{alt}}} = -\rho_{\mathrm{air}}\,g_{\oplus} \tag{SB-7}
$$
<!-- symbols: diff, Pair, halt, rhoair, gearth -->
<!-- begin generated symbol list -->
**Symbols in (SB-7).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $P_{\mathrm{air}}$: The pressure of the air at the altitude $h_{\mathrm{alt}}$ (an example, not UM-3). Unit: Pa. Value: about $1.0\times10^5$ Pa at the ground. Status: STANDARD.
- $h_{\mathrm{alt}}$: The altitude above the ground (an example, not UM-3). Unit: m. Status: STANDARD.
- $\rho_{\mathrm{air}}$: The mass density of the air at the altitude $h_{\mathrm{alt}}$ (an example, not UM-3). Unit: kg/m$^3$. Value: about 1.2 kg/m$^3$ at the ground. Status: STANDARD.
- $g_{\oplus}$: The acceleration of free fall at the surface of the Earth (an example, not UM-3). Unit: m/s$^2$. Value: 9.81 m/s$^2$. Status: STANDARD.

<!-- end generated symbol list -->

Again, the static state needs a definite distribution of pressure; any other distribution sets the air in motion. Status:
STANDARD.

**Example 5: a drum skin at rest.** A stretched skin stays flat and at rest because its tension is the same everywhere, so that
the pulls on every small piece of it balance. Pressing it or loosening it locally sets it in motion. The fold of UM-3 is a skin of this
kind: at the static block its thin source is a pure tension (FE-32). Status: STANDARD.

In all these examples except the empty space outside a star, staying static requires a definite content: a definite balance of
energy and pressure. Whether the static block of UM-3 is of this kind or a vacuum depends on the Lovelock weights.

# The stabiliser of the author's original weights

This part is the record of the stabiliser as it was found, with the weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ and the cosmological
constant $\Lambda = -10H^2$ of the author's notebook. The next part shows what the corrected weights change.

## How the static block fixes the source

The static block SB-5 has a simple curvature. In each half of the bulk, the seven directions other than the time ($\sigma$, ordinary
space and the extra times) form a space of constant negative curvature $-H^2$, like a slice of anti-de Sitter space: every pair of these
directions has the frame curvature $R^{ab}{}_{ab} = -H^2$, and no pair with the time is curved (the time is not warped). For such a space
times a flat line, the Lovelock tensor of order $p$ (FE-2) has only diagonal entries, and the entry along a direction depends only on the
number $m_{\mathrm{c}}$ of the other curved directions:

$$
\begin{aligned}
&\mathcal{E}_{(p)}{}^{(a)}{}_{(a)}\Big\vert_{\text{static block}} = -\frac12\,\big(-H^2\big)^p\,\frac{m_{\mathrm{c}}!}{(m_{\mathrm{c}} - 2p)!}\\
&\big(m_{\mathrm{c}} = 6\ \text{along the hidden direction, ordinary space and the extra times},\ m_{\mathrm{c}} = 7\ \text{along the time}\big)
\end{aligned} \tag{SB-8}
$$
<!-- symbols: LovE, ia, ip, Hconst, mcurv -->
<!-- begin generated symbol list -->
**Symbols in (SB-8).**

- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $m_{\mathrm{c}}$: The number of the other curved directions of the static block seen from one direction: 6 for $\sigma$, ordinary space and the extra times (the seven curved directions without the given one), 7 for the time (which is not curved itself). Unit: dimensionless. Value: 6 or 7. Status: DERIVED.

<!-- end generated symbol list -->

(no sum over the frame index $a$; $m_{\mathrm{c}}!$ is the factorial $1\cdot2\cdots m_{\mathrm{c}}$.) Each Riemann tensor in FE-2 contributes the curvature $-H^2$ of a pair of
directions, and the generalised Kronecker delta counts the ordered ways of choosing the $2p$ other directions of the $p$ pairs among the
$m_{\mathrm{c}}$ curved ones, $m_{\mathrm{c}}!/(m_{\mathrm{c}} - 2p)!$. Multiplied by the couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$, the entries along a warped direction and along the time are, in
units of $H^2$:

| order $p$ | per unit weight (warped, time) | original weights (warped, time) | corrected weights (warped, time) |
| --- | --- | --- | --- |
| 1, Einstein | $(15, 21)$ | $(15, 21)$ | $(15, 21)$ |
| 2, Gauss-Bonnet | $(-180, -420)$ | $(-45/8, -105/8)$ | $(-9, -21)$ |
| 3, cubic | $(360, 2520)$ | $(5/16, 35/16)$ | $(1, 7)$ |
| the cosmological constant | | $(-10, -10)$ | $(-7, -7)$ |
| total | | $(-5/16, 1/16)$ | $(0, 0)$ |

For general weights this is FE-70:

$$
\begin{aligned}
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^1{}_1 + \Lambda = \big(15 - 180w_{(2)} + 360w_{(3)}\big)H^2 + \Lambda,\\
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^4{}_4 + \Lambda = \big(21 - 420w_{(2)} + 2520w_{(3)}\big)H^2 + \Lambda,\\
&w_{(2)} = \frac{1}{20},\ w_{(3)} = \frac{1}{360}:\quad \text{both } 7H^2 + \Lambda,\qquad \Lambda = -7H^2;\\
&\text{curvature } -\mathsf{y}H^2:\quad (\mathsf{y} - 1)^2(\mathsf{y} - 7)\,H^2,\quad 7(\mathsf{y} - 1)^3H^2
\end{aligned} \tag{FE-70}
$$
<!-- symbols: ip, alphaL, LovE, Lambda, wL, Hconst, ycurv -->
<!-- begin generated symbol list -->
**Symbols in (FE-70).**

- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{y}$: The curvature of a seven-dimensional space of constant curvature $-\mathsf{y}H^2$ (in units of $-H^2$), times the time line: $\mathsf{y} = 1$ is the static block. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

A cosmological constant adds the same number to every direction, so it can cancel the left-hand side only if the warped and the time
entries are equal. With the original weights they are not ($155/16$ along the warped directions and $161/16$ along the time before
$\Lambda$), and no value of $\Lambda$ makes the static block a vacuum. Status: DERIVED (ST1 by computer algebra on the static block, ST9;
`um3_weights.py`, W4, for general weights).

## The stabiliser

With the original weights and $\Lambda = -10H^2$ the left-hand side of FE-1 at the static block is therefore, on both sides of the fold and
with no entry that mixes two directions,

$$
\begin{aligned}
&w_{(2)} = \frac{1}{32},\ w_{(3)} = \frac{1}{1152},\ \Lambda = -10H^2:\\
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b + \Lambda\,\delta^a{}_b = H^2\,\mathrm{diag}\Big(-\frac{5}{16}, -\frac{5}{16}, -\frac{5}{16},
 -\frac{5}{16}, \frac{1}{16}, -\frac{5}{16}, -\frac{5}{16}, -\frac{5}{16}\Big) = \kappa\,\mathcal{T}_{\mathrm{stab}}{}^a{}_b,\\
&\mathcal{T}_{\mathrm{stab}}{}^a{}_b = \mathrm{diag}\big(p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}},
 -\rho_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}, p_{\mathrm{s}}\big),\qquad
 \kappa\rho_{\mathrm{s}} = -\frac{H^2}{16},\qquad \kappa p_{\mathrm{s}} = -\frac{5H^2}{16}
\end{aligned} \tag{SB-9}
$$
<!-- symbols: wL, Lambda, Hconst, ip, alphaL, LovE, ia, ib, delta, diag, kappa, Tstab, ps, rhos -->
<!-- begin generated symbol list -->
**Symbols in (SB-9).**

- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{stab}}{}^a{}_b$: The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric required with the author's original Lovelock weights, found and named by Claude (Anthropic) on 2026-10-24; with the corrected weights and $\Lambda = -7H^2$ it is zero (IN-7). Unit: GeV$^8$. Value: 0 with the corrected weights. Status: DERIVED.
- $p_{\mathrm{s}}$: The pressure of the stabiliser of the bulk with the author's original weights (equal along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Value: $\kappa p_{\mathrm{s}} = -5H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser of the bulk with the author's original weights; with frozen extra times it was the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.

<!-- end generated symbol list -->

in the order ($\sigma$, $x_1$, $x_2$, $x_3$, $x_4$, $x_5$, $x_6$, $x_7$). The static bulk was therefore not a vacuum: the field equations held
only if the bulk contained a source whose energy-momentum tensor is this left-hand side divided by $\kappa$, a medium at rest in the
language of SB-3, without any flow, with the energy density $\rho_{\mathrm{s}}$ and the same pressure $p_{\mathrm{s}} = 5\rho_{\mathrm{s}}$ in every
direction but the time. Calling this source a medium of its own, the stabiliser, assumes that dirac16complex contributes nothing to the
static bulk (its energy-momentum tensor $\mathcal{T}_\Psi$ zero or negligible there; ASSUMED). Status: DERIVED (ST1).

The kink of the static block needed, with the original weights, the source of the fold

$$
\kappa\,\mathcal{S}^{(i)}{}_{(i)} = \kappa\,\mathcal{S}^{(r)}{}_{(r)} = -\frac{61}{8}H,\qquad
\kappa\,\mathcal{S}^{(4)}{}_{(4)} = -\frac{31}{4}H\qquad(\text{original weights, static block}) \tag{SB-10}
$$
<!-- symbols: kappa, Sfoldsrc, ii, ir, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (SB-10).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

along ordinary space, the time and the extra times. Order by order (in units of $H$): Einstein $(-10, -12, -10)$, which is Israel's
$-([K^a{}_b] - \delta^a{}_b[K])$ with the jump $-2H$ of the extrinsic curvature along the six warped directions; Gauss-Bonnet $(5/2, 5, 5/2)$;
cubic $(-1/8, -3/4, -1/8)$. It splits into a tension $61H/8$ (pressures equal to minus the energy density) and a pressureless part
$H/8$. With the corrected weights the Gauss-Bonnet and cubic parts are $(4, 8, 4)$ and $(-2/5, -12/5, -2/5)$, and the total is the pure
tension $-32H/5$ in all seven directions (FE-32 below). Status: DERIVED (ST1 and ST9, from the junction conditions FD-11; `um3_fold.py`,
J5).

## Why it is called the stabiliser, and who found it

It was the energy content without which the bulk of the author's metric could not stay static: it *stabilised* the bulk in the sense
of keeping it static. (Whether the static bulk with the stabiliser was also stable, that is whether small disturbances die away, is a
separate question that was not analysed.) The stabiliser was not part of the author's specification. Claude (Anthropic's AI model,
working in Claude Code) found the requirement SB-9 on 2026-10-24 while deriving the complete coupled field equations of UM-3, introduced
the medium to meet it, and named it the stabiliser of the bulk. The name and the idea of a medium that holds a static block had appeared
before in this repository, in the two earlier universe models, for their own metrics and with other properties (the provenance gives
the lineage). Status: DERIVED (the requirement), ASSUMED (the medium).

## What kind of medium it was

**Its energy density and its pressure were negative.** $\rho_{\mathrm{s}} = -H^2/(16\kappa)$, and the pressure five times as large,
$p_{\mathrm{s}} = 5\rho_{\mathrm{s}}$, the same along the hidden direction, ordinary space and the extra times. It did not flow.

**It violated both energy conditions.**

$$
\kappa\rho_{\mathrm{s}} = -\frac{H^2}{16} < 0,\qquad \kappa\big(\rho_{\mathrm{s}} + p_{\mathrm{s}}\big) = -\frac{3H^2}{8} < 0 \tag{SB-11}
$$
<!-- symbols: kappa, rhos, Hconst, ps -->
<!-- begin generated symbol list -->
**Symbols in (SB-11).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser of the bulk with the author's original weights; with frozen extra times it was the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $p_{\mathrm{s}}$: The pressure of the stabiliser of the bulk with the author's original weights (equal along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Value: $\kappa p_{\mathrm{s}} = -5H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.

<!-- end generated symbol list -->

The second inequality, for light moving along the time and one space-like direction, is the violation of the null energy condition; it
is what made the stabiliser exotic. The negative cosmological constant of the bulk violates only the weak condition, since its energy
density plus its pressure is zero. Status: DERIVED (ST5).

**Among homogeneous scalar fields, only a ghost reproduced it.** A scalar field that fills the bulk uniformly and changes only with the
time has a kinetic energy $K_{\mathrm{f}}$ and a potential energy $V_{\mathrm{f}}$ per volume, and its energy density and pressure (the same in
every direction but the time) are

$$
\rho_{\mathrm{med}} = K_{\mathrm{f}} + V_{\mathrm{f}},\qquad p_{\mathrm{med}} = K_{\mathrm{f}} - V_{\mathrm{f}};\qquad
p_{\mathrm{med}} = 5\rho_{\mathrm{med}}:\quad V_{\mathrm{f}} = -\frac{2}{3}K_{\mathrm{f}},\quad \rho_{\mathrm{med}} = \frac{K_{\mathrm{f}}}{3} \tag{SB-12}
$$
<!-- symbols: rhomed, Kf, Vf, pmed -->
<!-- begin generated symbol list -->
**Symbols in (SB-12).**

- $\rho_{\mathrm{med}}$: The energy density (energy per volume) of a medium at rest. Unit: GeV$^8$. Status: STANDARD.
- $K_{\mathrm{f}}$: The kinetic energy per volume of a field that fills the bulk uniformly and changes only with the time $x_4$: half the square of its rate of change for an ordinary field (never negative), minus that for a field whose kinetic term has the opposite sign (a ghost). Unit: GeV$^8$. Status: STANDARD.
- $V_{\mathrm{f}}$: The potential energy per volume of a field that fills the bulk uniformly and changes only with the time $x_4$. Unit: GeV$^8$. Status: STANDARD.
- $p_{\mathrm{med}}$: The pressure of a medium at rest, the same along every direction but the time (for a medium of the bulk: along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Status: STANDARD.

<!-- end generated symbol list -->

(derived by varying the action of the field with respect to the metric, ST5). An ordinary field has $K_{\mathrm{f}} \ge 0$ and so, with a
pressure five times its energy density, a positive energy density. Only a field whose kinetic energy is negative, a so-called ghost, with
$K_{\mathrm{f}} = 3\rho_{\mathrm{s}}$ and $V_{\mathrm{f}} = -2\rho_{\mathrm{s}}$, reproduced the stabiliser; on the static bulk it would roll at a constant
speed on a flat stretch of its potential. A scalar field that depends on $\sigma$ instead of the time could not do it, because its
pressure along $\sigma$ differs from its pressure along the other directions unless it is constant, and a constant field is a vacuum
energy with $p = -\rho$. Vector fields and other kinds of fields were not examined. Status: DERIVED (ST5, for homogeneous scalar fields).

**If it had been a simple fluid, its sound would have been faster than light.** For a fluid whose pressure is a fixed multiple of its
energy density, small compressions travel at the speed of sound $c_{\mathrm{s}}$ with $c_{\mathrm{s}}^2 = \mathrm{d}p/\mathrm{d}\rho$; for the stabiliser
this is 5, so its sound would have travelled $\sqrt5 \approx 2.24$ times faster than light. The ghost field instead propagates at the speed
of light, but its quanta carry negative energy. A general theorem (Dubovsky, Grégoire, Nicolis and Rattazzi, 2006) states that, under broad
conditions, a medium that violates the null energy condition has either signals faster than light or unstable excitations. Status:
STANDARD (the theorem and the fluid formula), DERIVED (their application).

**It was conserved by itself on the static bulk.** The covariant divergence SB-4 of the constant tensor of SB-9 vanishes on the static
block, in every component (ST4). The reason: its pressure along the hidden direction equals its pressure along every warped direction,
and the time, along which its entry differs, is not warped. Unlike the air of SB-7, the stabiliser needed no change of pressure along the
hidden direction: because the time is not warped there is no gravitational pull along $\sigma$. Status: DERIVED (ST4).

## How it would have evolved on its own

A medium that interacts only through gravity obeys SB-4. For a medium that fills the bulk uniformly, with the energy density
$\rho_{\mathrm{med}}(x_4)$ and the pressure $p_{\mathrm{med}}(x_4)$ in every warped direction, in the author's metric with arbitrary $a_4(x_4)$ and
$b_4(x_4)$, the time component of SB-4 reads (ST6)

$$
\rho_{\mathrm{med}}' = -3\,\frac{b_4'}{b_4}\,\big(\rho_{\mathrm{med}} + p_{\mathrm{med}}\big);\qquad
p_{\mathrm{med}} = 5\rho_{\mathrm{med}}:\quad \rho_{\mathrm{med}}\,b_4^{18} = \text{constant} \tag{SB-13}
$$
<!-- symbols: rhomed, prime, b4, pmed -->
<!-- begin generated symbol list -->
**Symbols in (SB-13).**

- $\rho_{\mathrm{med}}$: The energy density (energy per volume) of a medium at rest. Unit: GeV$^8$. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $p_{\mathrm{med}}$: The pressure of a medium at rest, the same along every direction but the time (for a medium of the bulk: along $\sigma$, ordinary space and the extra times). Unit: GeV$^8$. Status: STANDARD.

<!-- end generated symbol list -->

The growth of ordinary space drops out, because ordinary space grows with $\mathrm{e}^{a_4}$ and the extra times with $\mathrm{e}^{-a_4}b_4$, so
that the volume of all six warped directions together grows with $b_4^3$. Two consequences follow. A stabiliser that is absent
($\rho = 0$) stays absent. And with frozen extra times ($b_4$ proportional to $\mathrm{e}^{a_4}$) a stabiliser on its own would have been
diluted as $\mathrm{e}^{-18a_4}$ while the universe expands. Status: DERIVED (ST6).

## What the original equations required when the universe expanded

With frozen extra times, the condition of the late universe ($\mathsf{U} = \mathsf{A}$: the size $\mathrm{e}^{-a_4}b_4$ of the extra times constant,
so that the couplings of the Standard Model stay constant), the original equations required in the bulk and on the fold (with
$\mathsf{A}_1 = a_4''/H^2$ the rate of change of $\mathsf{A}$):

$$
\begin{aligned}
&\mathsf{U} = \mathsf{A}:\qquad \frac{\kappa\rho_{\mathrm{bulk}}}{H^2} = \frac{3\mathsf{A}^2 - 1}{16},\qquad
 \frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(0)}}{H^2} = -\frac{3\mathsf{A}^4 + 3\mathsf{A}^2\mathsf{A}_1 + 18\mathsf{A}^2 + 3\mathsf{A}_1 + 5}{16},\\
&\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(i)}{}_{(i)}}{H^2} = -\frac{9\mathsf{A}^2 + 2\mathsf{A}_1 + 5}{16},\qquad
 \frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(r)}{}_{(r)}}{H^2} = -\frac{3\mathsf{A}^4 + 3\mathsf{A}^2\mathsf{A}_1 + 24\mathsf{A}^2 + 3\mathsf{A}_1 + 5}{16},\\
&\frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}}{H^2} = \mathrm{sgn}(\sigma)\,\frac{3\mathsf{A}\big(1 + \mathsf{A}^2\big)}{16},\qquad
 \frac{\kappa\,\mathcal{S}^{(4)}{}_{(4)}}{H} = -\frac{10\mathsf{A}^2 + 31}{4},\\
&\frac{\kappa\,\mathcal{S}^{(i)}{}_{(i)}}{H} = -\frac{57\mathsf{A}^2 + 40\mathsf{A}_1 + 183}{24},\qquad
 \frac{\kappa\,\mathcal{S}^{(r)}{}_{(r)}}{H} = -\frac{2\mathsf{A}^4 + 2\mathsf{A}^2\mathsf{A}_1 + 37\mathsf{A}^2 + 20\mathsf{A}_1 + 61}{8}
\end{aligned} \tag{SB-14}
$$
<!-- symbols: Usf, Asf, A1sf, kappa, rhobulk, Hconst, Tbulk, ii, ir, sgn, sigma, Sfoldsrc -->
<!-- begin generated symbol list -->
**Symbols in (SB-14).**

- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.

<!-- end generated symbol list -->

($\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$ is the energy density of all bulk sources together.) For $\mathsf{A} \to 0$ they reduce
to SB-9 and SB-10. The entry $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}$ is a flow of energy along the hidden direction, equal in size on the two
sides of the fold and opposite in sign, so it jumps across the fold by $\frac38\mathsf{A}(1 + \mathsf{A}^2)H^2/\kappa$; the energy current, minus
this entry, points towards the fold on both sides. Status: DERIVED (ST6, with its $\mathsf{A}_1$ terms; `um3_fold.py`, J5 and J7).

**Where the energy came from.** With frozen extra times only ordinary space grows, and the volume of the bulk grows at the rate $3a_4'$.
The required bulk source had, for constant $\mathsf{A}$, an energy density plus pressure along ordinary space that is negative:

$$
\begin{aligned}
&\kappa\big(\rho_{\mathrm{bulk}} + \mathcal{T}_{\mathrm{bulk}}{}^{(1)}{}_{(1)}\big) = -\frac{3}{8}\big(1 + \mathsf{A}^2\big)H^2\qquad
 (\mathsf{U} = \mathsf{A},\ \mathsf{A}_1 = 0),\\
&\int_{-\infty}^{\infty}\mathrm{d}\sigma\;\mathrm{e}^{-6H\lvert\sigma\rvert}\;\big(-3a_4'\big)\,\kappa\big(\rho_{\mathrm{bulk}}
 + \mathcal{T}_{\mathrm{bulk}}{}^{(1)}{}_{(1)}\big) = \frac{3}{8}\,\mathsf{A}\big(1 + \mathsf{A}^2\big)H^2
\end{aligned} \tag{SB-15}
$$
<!-- symbols: kappa, rhobulk, Tbulk, Asf, Hconst, Usf, A1sf, diff, sigma, infty, euler, a4, prime -->
<!-- begin generated symbol list -->
**Symbols in (SB-15).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.

<!-- end generated symbol list -->

Left to itself, a medium of the bulk changes its energy density at the rate $-3a_4'(\rho + p)$ while only ordinary space grows. The required
source, with $\rho + p < 0$, would have seen its negative energy density rise towards zero; since the field equations kept its energy density
fixed, it had to give off the energy $-3a_4'(\rho_{\mathrm{bulk}} + \mathcal{T}_{\mathrm{bulk}}{}^{(1)}{}_{(1)})$ per volume and time. Integrated over the
hidden direction with the volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$ of the six warped directions, this is exactly the jump of the flow:
all the energy that the bulk gave off arrived at the fold. This is a consistency identity (it follows from the Bianchi identity), not an
independent result. Status: DERIVED (ST6).

**Where the energy went.** The source of the fold took up exactly the energy that arrived from the bulk, for any $a_4(x_4)$:

$$
-\big(\kappa\,\mathcal{S}^{(4)}{}_{(4)}\big)' + 3a_4'\big(\kappa\,\mathcal{S}^{(i)}{}_{(i)} - \kappa\,\mathcal{S}^{(4)}{}_{(4)}\big)
 = \kappa\Big(\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}\big\vert_{\sigma=0^+} - \mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)}\big\vert_{\sigma=0^-}\Big)
 \qquad (\mathsf{U} = \mathsf{A}) \tag{SB-16}
$$
<!-- symbols: kappa, Sfoldsrc, ii, a4, prime, Tbulk, sigma, Usf, Asf -->
<!-- begin generated symbol list -->
**Symbols in (SB-16).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.

<!-- end generated symbol list -->

($-\mathcal{S}^{(4)}{}_{(4)}$ is the energy density of the source of the fold and $\mathcal{S}^{(i)}{}_{(i)}$ its pressure along ordinary space;
$0^+$ and $0^-$ mark the limits from above and from below.) This is the conservation law at the fold, FE-11, again an identity of the
junction conditions. At the static block the earlier version of UM-3 split the source of the fold into a tension $61HV_*/(8\kappa)$ (with
the original weights; with the corrected weights the whole source of the static block is the tension $\lambda_{\mathrm{F}} = 32HV_*/(5\kappa)$)
and a pressureless part $\rho_{\mathrm{d}} = HV_*/(8\kappa)$ (per unit volume of ordinary space, $V_*$ the volume of the extra times), and the
pressureless part needed exactly the energy $3a_4'\rho_{\mathrm{d}} = \frac38\mathsf{A}H^2V_*/\kappa$, the part of the jump linear in
$\mathsf{A}$. Reading this as an exchange of energy between the stabiliser and a fold fluid is an interpretation: what the equations fix is
only the total bulk source and its flow; a medium of the bulk that couples only to gravity could also carry its flow into a thin layer of its
own (ASSUMED). Moreover, with the original weights a fluid on top of the static source could not be conserved by itself on the separable
metric of the author, so ordinary matter on the fold needed metric functions that depend on $\sigma$ (a check of `um3_fold.py` of the commit
`cd5709d`); these energy balances describe the fold sources that the separable metric required, not ordinary matter. With the corrected
weights the matter of the fold above the tension is conserved by itself on the separable metric (FE-33).
Status: DERIVED (ST6), ASSUMED (the interpretation). The conservation law at the fold, for every metric of UM-3:

$$
\begin{aligned}
&\nabla_M\,\mathcal{T}_\Psi{}^M{}_N = 0\qquad (\sigma \ne 0),\\
&\hat\nabla_a\,\mathcal{S}^a{}_b = -\Big(\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b\big\vert_{\sigma=0^+}
 - \mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b\big\vert_{\sigma=0^-}\Big)
\end{aligned} \tag{FE-11}
$$
<!-- symbols: nabla, TPsi, iM, iN, sigma, nablahat, Sfoldsrc, ia, ib, Tbulk -->
<!-- begin generated symbol list -->
**Symbols in (FE-11).**

- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex: $-2/\sqrt{\lvert g\rvert}$ times the variation of the action $S_\Psi$ of dirac16complex with respect to $g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\hat\nabla$: The covariant derivative of the fold: with the Levi-Civita connection of the metric of the fold (for four-dimensional tensors of its metric $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the observable coordinates $x_1, \dots, x_4$; for $\hat\nabla_a\mathcal{S}^a{}_b$ of the induced metric of the seven-dimensional fold). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.

<!-- end generated symbol list -->

## The constraints of the original equations

Two components of the bulk equations contain no second time derivative of the metric, for any $a_4(x_4)$ and $b_4(x_4)$: the energy
constraint (the time component, like the Friedmann equation of cosmology) and the flow of energy along the hidden direction. With the
original weights they were

$$
\begin{aligned}
&\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = \frac{H^2}{16}\,\mathsf{P},\qquad
 \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)} = \frac{3}{16}\,\mathsf{U}\,\mathcal{G}\,H^2\,\mathrm{sgn}(\sigma),\qquad \mathsf{V} = \mathsf{U} - \mathsf{A},\\
&\mathsf{P} = 1 - 3\mathsf{A}^2 - 3\mathsf{V}^2 - 9\mathsf{A}\mathsf{V} - 27\mathsf{A}^2\mathsf{V}^2 - 9\mathsf{A}^3\mathsf{V} - 9\mathsf{A}\mathsf{V}^3 - 5\mathsf{A}^3\mathsf{V}^3,\qquad
 \mathcal{G} = 1 + \mathsf{A}^2 + 8\mathsf{A}\mathsf{V} + \mathsf{V}^2 + 5\mathsf{A}^2\mathsf{V}^2
\end{aligned} \tag{SB-17}
$$
<!-- symbols: kappa, Tbulk, Hconst, Pcon, Usf, Gfac, sgn, sigma, Vsf, Asf -->
<!-- begin generated symbol list -->
**Symbols in (SB-17).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{P}(\mathsf{A}, \mathsf{U})$: The polynomial of the energy constraint of the bulk with the author’s original Lovelock weights: the $(x_4, x_4)$ component of the bulk equations of the author’s metric was $\kappa\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = (H^2/16)\,\mathsf{P}(\mathsf{A}, \mathsf{U})$, whatever the time derivatives of the rates (with the corrected weights it is $\mathsf{A}^3(\mathsf{A} - \mathsf{U})^3H^2$). Unit: dimensionless. Value: $\mathsf{P}(0, 0) = 1$, $\mathsf{P}(\pm1, 0) = 0$. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathcal{G}$: The factor of the $(\sigma, x_4)$ bulk equation of the author's metric with the author's original weights, $\mathcal{G} = 5\mathsf{A}^2(\mathsf{A} - \mathsf{U})^2 - 6\mathsf{A}^2 + 6\mathsf{A}\mathsf{U} + \mathsf{U}^2 + 1$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathsf{V}$: The rate of change of the scale factor $\mathrm{e}^{-a_4}b_4$ of the extra times on the fold in units of $H$, $\mathsf{V} = \mathsf{U} - \mathsf{A}$; zero with frozen extra times. Unit: dimensionless. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.

<!-- end generated symbol list -->

written with the rate $\mathsf{A}$ of ordinary space and the rate $\mathsf{V}$ of the scale factor $\mathrm{e}^{-a_4}b_4$ of the extra times; both
polynomials are symmetric under the exchange of $\mathsf{A}$ and $\mathsf{V}$. A bulk without any source needs $\mathsf{P} = 0$ and
$\mathsf{U}\mathcal{G} = 0$ at every instant. For $\mathsf{U} = 0$, $\mathsf{P} = (\mathsf{A}^2 - 1)^2(5\mathsf{A}^2 + 1)$ vanishes only at $\mathsf{A} = \pm1$; for
$\mathsf{U} \ne 0$ both polynomials would need a common root, but their resultant has no real root except $\mathsf{U} = 0$. **With the original
weights, a bulk without any source was therefore at every instant the author's vacuum $(\mathsf{A}, \mathsf{U}) = (1, 0)$ or its time reverse
$(-1, 0)$**, whatever the time dependence of the rates. A late universe that expands slowly with constant couplings needed a bulk source.
With frozen extra times ($\mathsf{V} = 0$) $\mathsf{P} = 1 - 3\mathsf{A}^2$ for any $a_4(x_4)$, and the energy constraint became a Friedmann equation of
the bulk, $3a_4'^2 = H^2 + 16\kappa\rho_{\mathrm{bulk}} = 16\kappa(\rho_{\mathrm{bulk}} - \rho_{\mathrm{s}})$: the energy density of the stabiliser was the
energy density of the bulk at which ordinary space stands still. Status: DERIVED (ST3, ST8).

# The correction of the weights removes the stabiliser

## Gravitons must travel at the speed of light

A gravitational wave is a small ripple of the metric that travels. The simplest one, of the "+" polarisation, multiplies the metric
components along $x_1$ and $x_2$ by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$ and travels along $x_3$. Put into the field
equations of the static bulk (where $a_4$ is a constant, chosen as 0 by the unit of $x_3$) and kept to first order in $h_{\mathrm{gw}}$,
the Lovelock terms give it the wave equation

$$
\begin{aligned}
&\frac{c_{\mathrm{t}}}{2}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2}
 - \frac{c_{\mathrm{x}}}{2}\Big(\mathrm{e}^{2H\lvert\sigma\rvert}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2}
 + \frac{\partial^2h_{\mathrm{gw}}}{\partial\sigma^2} - 6H\,\mathrm{sgn}(\sigma)\,\frac{\partial h_{\mathrm{gw}}}{\partial\sigma}\Big) = 0,\\
&c_{\mathrm{t}} = 1 - 40w_{(2)} + 360w_{(3)},\qquad c_{\mathrm{x}} = 1 - 24w_{(2)} + 72w_{(3)}
\end{aligned} \tag{FE-68}
$$
<!-- symbols: ctw, partial, hgw, x4, cxw, euler, Hconst, sigma, x3, sgn, wL -->
<!-- begin generated symbol list -->
**Symbols in (FE-68).**

- $c_{\mathrm{t}}$: The coefficient of the second time derivative of a transverse traceless gravitational wave in the bulk at the static block, in units of its value with Einstein gravity alone: $c_{\mathrm{t}} = 1 - 40w_{(2)} + 360w_{(3)}$ (FE-68). Unit: dimensionless. Value: 0 with the corrected weights; $1/16$ with the author's original weights. Status: DERIVED.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $c_{\mathrm{x}}$: The coefficient of the second derivatives along ordinary space and along $\sigma$ of the same wave, in the same units: $c_{\mathrm{x}} = 1 - 24w_{(2)} + 72w_{(3)}$ (FE-68); bulk gravitons move with the local speed $\sqrt{c_{\mathrm{x}}/c_{\mathrm{t}}}$. Unit: dimensionless. Value: 0 with the corrected weights; $5/16$ with the author's original weights. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).

<!-- end generated symbol list -->

with a time-kinetic coefficient $c_{\mathrm{t}}$ and a gradient coefficient $c_{\mathrm{x}}$ ($\partial$ marks a partial derivative). In the bulk the
wave moves with the local speed $\sqrt{c_{\mathrm{x}}/c_{\mathrm{t}}}$ times the speed of light. Einstein gravity alone gives
$c_{\mathrm{t}} = c_{\mathrm{x}} = 1$, the speed of light; the Gauss-Bonnet and cubic terms change the two coefficients differently, because the static
block is curved along $\sigma$, ordinary space and the extra times but not along the time. With the author's original weights
$c_{\mathrm{t}} = 1/16$ and $c_{\mathrm{x}} = 5/16$: gravitational waves in the bulk moved $\sqrt5 = 2.24$ times faster than light. At the fold the wave
has a thin part of its own, and a wave of long wavelength collects both:

$$
\begin{aligned}
&\int_{0^-}^{0^+}\mathrm{d}\sigma\,(\dots) = \frac{16\big(w_{(2)} - 6w_{(3)}\big)}{H}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2}
 - \frac{12\big(w_{(2)} - 2w_{(3)}\big)}{H}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2}
 - \frac{c_{\mathrm{x}}}{2}\Big(\frac{\partial h_{\mathrm{gw}}}{\partial\sigma}\Big\vert_{0^+} - \frac{\partial h_{\mathrm{gw}}}{\partial\sigma}\Big\vert_{0^-}\Big)
 = \kappa\,\Pi_{\mathrm{gw}},\\
&\kappa K_{44} = \frac{c_{\mathrm{t}}}{6H} + \frac{16\big(w_{(2)} - 6w_{(3)}\big)}{H},\qquad
 \kappa K_{33} = \frac{c_{\mathrm{x}}}{4H} + \frac{12\big(w_{(2)} - 2w_{(3)}\big)}{H},\qquad
 \kappa\big(K_{44} - K_{33}\big) = -\frac{c_{\mathrm{t}}}{12H},\qquad c_{\mathrm{g}}^2 = \frac{K_{33}}{K_{44}}
\end{aligned} \tag{FE-69}
$$
<!-- symbols: diff, sigma, wL, Hconst, partial, hgw, x4, x3, cxw, kappa, Pigw, K44, ctw, K33, cgrav -->
<!-- begin generated symbol list -->
**Symbols in (FE-69).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $w_{(p)}$: The Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/20$, $w_{(3)} = 1/360$: the only weights for which both coefficients of a transverse traceless gravitational wave in the static bulk vanish, $1 - 40w_{(2)} + 360w_{(3)}$ (of its second time derivative) and $1 - 24w_{(2)} + 72w_{(3)}$ (of its second derivatives along ordinary space and along $\sigma$). Then the four-dimensional graviton of the fold travels at the speed of light at linear order, and no graviton of the static bulk travels faster, because the static bulk has no linear graviton at all (the Born-Infeld point of Lovelock gravity in eight dimensions). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) made bulk gravitons $\sqrt5$ times faster than light; they were corrected at the author's order of 2026-10-25. Unit: dimensionless. Value: $(1, 1/20, 1/360)$; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), ASSUMED (the criterion of the correction), DERIVED (the unique values that meet it).
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $c_{\mathrm{x}}$: The coefficient of the second derivatives along ordinary space and along $\sigma$ of the same wave, in the same units: $c_{\mathrm{x}} = 1 - 24w_{(2)} + 72w_{(3)}$ (FE-68); bulk gravitons move with the local speed $\sqrt{c_{\mathrm{x}}/c_{\mathrm{t}}}$. Unit: dimensionless. Value: 0 with the corrected weights; $5/16$ with the author's original weights. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\Pi_{\mathrm{gw}}$: The transverse traceless stress of the matter of the fold that drives the gravitational wave $h_{\mathrm{gw}}$ (half the difference of its components along $x_1$ and $x_2$), integrated across the fold (eight-dimensional normalisation). Unit: GeV$^7$. Status: STANDARD.
- $K_{44}$: The coefficient of $\partial^2h_{\mathrm{gw}}/\partial x_4^2$ in the equation of the long-wavelength gravitational wave (the same at every $\sigma$) at the static block, integrated across the hidden direction with the volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$: the part of the bulk plus the thin part at the fold. Unit: GeV$^5$ ($\kappa K_{44}$ is a length). Status: DERIVED.
- $c_{\mathrm{t}}$: The coefficient of the second time derivative of a transverse traceless gravitational wave in the bulk at the static block, in units of its value with Einstein gravity alone: $c_{\mathrm{t}} = 1 - 40w_{(2)} + 360w_{(3)}$ (FE-68). Unit: dimensionless. Value: 0 with the corrected weights; $1/16$ with the author's original weights. Status: DERIVED.
- $K_{33}$: The coefficient of $-\partial^2h_{\mathrm{gw}}/\partial x_3^2$ in the same equation, with the same two parts; the wave travels at $c_{\mathrm{g}}^2 = K_{33}/K_{44}$. Unit: GeV$^5$. Status: DERIVED.
- $c_{\mathrm{g}}$: The speed of gravitational waves on the fold, in units of the speed of light. Unit: dimensionless. Value: with the corrected weights 1 at every wavelength, at linear order, for the four-dimensional graviton (the polarisations along ordinary space) on the static block and on every fold with frozen extra times; the polarisation along the extra times, a scalar of the four-dimensional world, is not luminal on an expanding fold; with the author's original weights the long-wavelength mode had $c_{\mathrm{g}}^2 = 83/82$ and shorter waves were slower than light. Status: DERIVED.

<!-- end generated symbol list -->

For every pair of weights the difference of the two coefficients of the long wave is $-c_{\mathrm{t}}/(12\kappa H)$: it travels at the speed of
light only if $c_{\mathrm{t}} = 0$. If $c_{\mathrm{t}}$ were zero but not $c_{\mathrm{x}}$, waves in the bulk would have no time-kinetic term at all, an infinite
local speed. The graviton of the fold travels at the speed of light, with no faster graviton in the static bulk, only if both coefficients
vanish: $1 - 40w_{(2)} + 360w_{(3)} = 0$ and $1 - 24w_{(2)} + 72w_{(3)} = 0$, two linear equations with the single solution
$w_{(2)} = 1/20$, $w_{(3)} = 1/360$. With the original weights the long wave had $c_{\mathrm{g}}^2 = 83/82$, faster than light (the bulk part
alone $15/2$: $c_{\mathrm{g}} = 2.74$, a figure that an earlier version of UM-3 quoted), and the wave bound to the fold was slower than light
at short wavelengths. With the corrected weights the bulk part vanishes, $\kappa K_{44} = \kappa K_{33} = 8/(15H)$, and $c_{\mathrm{g}} = 1$ at
every wavelength for the gravitational wave of our four-dimensional world, at the lowest order in its amplitude (the linear order, in
which the wave is so weak that the square of its amplitude can be neglected). Status: DERIVED (`um3_weights.py`, W1 to W3, W7;
`um3_bulk.py`, B5).

What the correction cannot do. A first version of the correction claimed that gravitons now travel at the speed of light everywhere;
independent checks showed that this is not so, and the following is what holds.

* *The static bulk has no gravitational waves at the linear order.* With the corrected weights the terms of first order cancel in the field
  equations of the static bulk for every small ripple of the metric, of any shape and in any of its 36 components (LN2). A theory in
  which small ripples obey no equation at the first order, so that the first terms that fix them are of the second order, is called
  strongly coupled around that solution: small ripples do not obey a wave equation, and how the bulk responds to matter cannot be
  computed by the usual expansion in small amplitudes (OPEN). The corrected gravity is known in the literature: these weights and this
  cosmological constant are the Born-Infeld gravity of eight dimensions, up to its term of order four, which in eight dimensions does not
  change the field equations (M. Bañados, C. Teitelboim and J. Zanelli, Phys. Rev. D 49 (1994) 975; J. Crisóstomo, R. Troncoso and
  J. Zanelli, Phys. Rev. D 62 (2000) 084013). Its maximally symmetric vacuum is degenerate, and there its field equations cannot be
  linearised (G. Arenas-Henriquez, R. B. Mann, O. Miskovic and R. Olea, Phys. Rev. D 100 (2019) 064038). The static block is not that
  vacuum, because its time is not warped, but the same happens there for a simple reason: with these weights the field equations are a
  product of three factors, each the curvature minus the curvature of the maximally symmetric vacuum; at the static block such a factor
  is nonzero only in the planes that contain the time, and a term of the first order, which contains two of the background factors,
  would need the time twice in one antisymmetric combination and therefore vanishes.
* *One polarisation is not settled.* On an expanding fold the ripple of the extra times (the + polarisation that multiplies the metric
  components along $x_5$ and $x_6$ by inverse factors), which the four-dimensional world sees as a field without spin, keeps in the bulk a
  gradient term but no time-kinetic term, so that it responds instantaneously there (an infinite local speed: the bulk of an expanding
  fold does carry such modes). On the fold the part of its equation that is concentrated there has the ratio
  $(8 + 5\mathsf{A}^2 + 4\mathsf{A}_1)/(8 + 6\mathsf{A}^2)$ of its two coefficients (of the second derivative along the proper length of $x_3$
  to the second time derivative; $\mathsf{A} = a_4'/H$ is the expansion rate of the fold in units of $H$ and $\mathsf{A}_1 = a_4''/H^2$ its
  rate of change), but it also couples there to the jump of its slope across the fold, at the same order $\mathsf{A}^2$, so that how fast
  it moves follows only from the bulk and the fold solved together, which has not been done (OPEN; generically not the speed of light).
  Today $\mathsf{A}$ is below $10^{-30}$ for every $H$ above $10^{-26}$ GeV, so the effect is far below every measurement; in the early
  universe it is not small (W7, LN4).
* *Gravitons at the speed of light in the bulk and on the fold together are impossible.* Waves in the bulk move at the local speed of
  light only if $c_{\mathrm{t}} = c_{\mathrm{x}} = c_{\mathrm{tx}} \ne 0$; then the long wave of the fold has
  $c_{\mathrm{g}}^2 - 1 = 5c_{\mathrm{tx}}/(32 - 22c_{\mathrm{tx}})$, which is zero only for $c_{\mathrm{tx}} = 0$ (faster than light for
  $0 < c_{\mathrm{tx}} < 16/11$; for $c_{\mathrm{tx}} < 0$ the bulk graviton is a ghost, and above $16/11$ the long wave has a negative
  kinetic coefficient), and the static bulk is not empty either. The reason is the author's metric, which warps ordinary space and the extra times but
  not the time. A metric that warps the time as well might allow both; the metric is the author's, and changing it is his decision (W3).

Status: DERIVED (`um3_weights.py`, W3 and W7; `um3_linear.py`, LN2 and LN4), OPEN (the strongly coupled bulk).

## The static block with the corrected weights

With $w_{(2)} = 1/20$ and $w_{(3)} = 1/360$ the warped and the time entries of the static block are both $7H^2$ before the cosmological constant
(the last column of the table of SB-8; FE-70), so the cosmological constant $\Lambda = -7H^2$ makes the static block a vacuum:

$$
\begin{aligned}
&\kappa\,\mathcal{T}_{\mathrm{stab}}{}^a{}_b = \Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b + \Lambda\,\delta^a{}_b\Big)\Big\vert_{\text{static block}} = 0:\\
&\qquad (15 - 9 + 1 - 7)H^2 = 0\ \text{(warped directions)},\qquad (21 - 21 + 7 - 7)H^2 = 0\ \text{(the time)}
\end{aligned} \tag{IN-7}
$$
<!-- symbols: kappa, Tstab, ia, ib, ip, alphaL, LovE, Lambda, delta, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-7).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{stab}}{}^a{}_b$: The energy-momentum tensor of the stabiliser of the bulk (frame components): the source that a static bulk of the author's metric required with the author's original Lovelock weights, found and named by Claude (Anthropic) on 2026-10-24; with the corrected weights and $\Lambda = -7H^2$ it is zero (IN-7). Unit: GeV$^8$. Value: 0 with the corrected weights. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number; in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -7H^2$: with the corrected weights the value for which the static block is a vacuum (its Lovelock tensors add to $7H^2$ in every direction). The author's original value was $\Lambda = -10H^2$ (he writes the pure number $\Lambda_{\mathrm{N}} = 10$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$). Unit: GeV$^2$. Value: $-7H^2$; the author's original $-10H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

The stabiliser of SB-9 is zero: order by order, Einstein $(15, 21)$, Gauss-Bonnet $(-9, -21)$, cubic $(1, 7)$ and the cosmological constant
$(-7, -7)$ add to zero along the warped directions and along the time. The source of the fold of the static block becomes a pure tension, the
same in all seven directions of the fold:

$$
\mathsf{A} = \mathsf{U} = \mathsf{A}_1 = \mathsf{U}_1 = 0:\qquad \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^a{}_b = 0,\qquad
\kappa\,\mathcal{S}^{(i)}{}_{(i)} = \kappa\,\mathcal{S}^{(4)}{}_{(4)} = \kappa\,\mathcal{S}^{(r)}{}_{(r)} = -\frac{32}{5}H \tag{FE-32}
$$
<!-- symbols: Asf, Usf, A1sf, U1sf, kappa, Tbulk, ia, ib, Sfoldsrc, ii, ir, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (FE-32).**

- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

This is the arrangement of Randall and Sundrum (FD-8): an empty bulk with a negative cosmological constant and a fold of pure tension, like
the drum skin of example 5. Status: DERIVED (ST9; `um3_weights.py`, W4; `um3_fold.py`, J5).

## The expanding fold with the corrected weights

The corrected equations have no need of a stabiliser in any era. Their two constraints are

$$
\begin{aligned}
&\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)} = \mathsf{A}^3(\mathsf{A} - \mathsf{U})^3H^2,\qquad
 \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_{(4)} = 3\mathsf{A}^2\mathsf{U}(\mathsf{A} - \mathsf{U})^2H^2\,\mathrm{sgn}(\sigma),\\
&\text{no bulk source:}\quad \mathsf{A} = 0\ \ \text{or}\ \ \mathsf{U} = \mathsf{A}\quad\text{at every instant}
\end{aligned} \tag{FE-66}
$$
<!-- symbols: kappa, Tbulk, Asf, Usf, Hconst, sgn, sigma -->
<!-- begin generated symbol list -->
**Symbols in (FE-66).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->

so a bulk without any source has, at every instant, either static ordinary space ($\mathsf{A} = 0$) or frozen extra times ($\mathsf{U} = \mathsf{A}$), and
on both branches every component of the bulk equations vanishes. The expanding fold of our universe is on the second branch, where the bulk is
an exact vacuum for every expansion history and the fold obeys exactly the Friedmann equations of four-dimensional general relativity (the
equations of the expansion of a homogeneous universe, $3a_4'^2 = \kappa_7\rho$ for the energy density $\rho$ and
$-(2a_4'' + 3a_4'^2) = \kappa_7p$ for the pressure $p$ of its matter above the tension, both in the normalisation of the thin source):

$$
\begin{aligned}
&\mathsf{U} = \mathsf{A},\quad \mathsf{U}_1 = \mathsf{A}_1\ \ \big(\mathrm{e}^{-a_4}b_4 = \text{constant},\ \mathcal{Z} = 1\big):\qquad
 \kappa\,\mathcal{T}_{\mathrm{bulk}}{}^a{}_b = 0\ \ \text{for any } a_4(x_4),\\
&\frac{\kappa\,\mathcal{S}^{(i)}{}_{(i)}}{H} = -\frac{16}{15}\big(6 + 3\mathsf{A}^2 + 2\mathsf{A}_1\big),\qquad
 \frac{\kappa\,\mathcal{S}^{(4)}{}_{(4)}}{H} = -\frac{16}{5}\big(2 + \mathsf{A}^2\big),\qquad
 \frac{\kappa\,\mathcal{S}^{(r)}{}_{(r)}}{H} = -\frac45\big(8 + 8\mathsf{A}^2 + \mathsf{A}^4 + 4\mathsf{A}_1 + \mathsf{A}^2\mathsf{A}_1\big),\\
&3a_4'^2 = -\kappa_7\Big(\mathcal{S}^{(4)}{}_{(4)} + \frac{32H}{5\kappa}\Big),\qquad
 -\big(2a_4'' + 3a_4'^2\big) = \kappa_7\Big(\mathcal{S}^{(i)}{}_{(i)} + \frac{32H}{5\kappa}\Big),\qquad \kappa_7 = \frac{15}{16}\,\kappa H
\end{aligned} \tag{FE-33}
$$
<!-- symbols: Usf, Asf, U1sf, A1sf, euler, a4, b4, Zfold, kappa, Tbulk, ia, ib, x4, Sfoldsrc, ii, ir, Hconst, prime, kappa7 -->
<!-- begin generated symbol list -->
**Symbols in (FE-33).**

- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\kappa_7$: The gravitational coupling of the fold: with the corrected Lovelock weights the thin source of the fold equals, to second order in the rates of expansion, the Einstein tensor of the seven-dimensional metric of the fold divided by $\kappa_7 = 15\kappa H/16$, and exactly so in the Friedmann equations of a fold with frozen extra times; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, if the fields of the fold induce one). Unit: GeV$^{-5}$. Value: $15\kappa H/16$. Status: DERIVED.

<!-- end generated symbol list -->

There is no flow of energy along the hidden direction, so the matter of the fold is conserved by itself (FE-11 with a vanishing right-hand
side). The author's vacuum, in which the original weights needed no source, now needs one:

$$
\begin{aligned}
&a_4 = Hx_4,\quad b_4 = \text{constant}\ (\mathsf{A} = 1,\ \mathsf{U} = \mathsf{A}_1 = \mathsf{U}_1 = 0):\qquad
 \frac{\kappa\,\mathcal{T}_{\mathrm{bulk}}{}^a{}_b}{H^2} = \mathrm{diag}\Big(-\frac75, -\frac75, -\frac75, -\frac75, 1, -\frac75, -\frac75, -\frac75\Big),\\
&\kappa\rho_{\mathrm{bulk}} = -H^2,\qquad \kappa\,\mathcal{S}^{(i)}{}_{(i)} = \kappa\,\mathcal{S}^{(r)}{}_{(r)} = -\frac{42}{5}H,\qquad
 \kappa\,\mathcal{S}^{(4)}{}_{(4)} = -\frac{28}{5}H
\end{aligned} \tag{FE-31}
$$
<!-- symbols: a4, Hconst, x4, b4, Asf, Usf, A1sf, U1sf, kappa, Tbulk, ia, ib, diag, rhobulk, Sfoldsrc, ii, ir -->
<!-- begin generated symbol list -->
**Symbols in (FE-31).**

- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{U}_1$: The time derivative of $\mathsf{U}$ in units of $H$, $\mathsf{U}_1 = \mathsf{U}'/H$. Unit: dimensionless. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_{\mathrm{bulk}}$: The energy-momentum tensor of all sources of the bulk (with the corrected weights dirac16complex alone, $\mathcal{T}_\Psi$; with the author’s original weights also the stabiliser); $\mathcal{T}_{\mathrm{bulk}}{}^{(0)}{}_b$ is its flux along $\sigma$ (frame components). Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\rho_{\mathrm{bulk}}$: The energy density of the bulk sources, $\rho_{\mathrm{bulk}} = -\mathcal{T}_{\mathrm{bulk}}{}^{(4)}{}_{(4)}$. Unit: GeV$^8$. Status: DERIVED.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\sum_p\alpha_{(p)}\mathcal{E}_{(p)}{}^a{}_b$ (FD-11, the junction conditions); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -\frac{32}{5}H\delta^a{}_b$ at the static block. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $r$: An extra-time direction of the fold: $r \in \{5, 6, 7\}$ ($x_5, x_6, x_7$); not summed (the three components are equal). Status: STANDARD.

<!-- end generated symbol list -->

so the primordial era of UM-3 is no longer the author's vacuum. It can be an inflation of the fold on the branch of frozen extra times (a
period in which ordinary space expands exponentially), driven by the vacuum energy of a field of the fold, as in general relativity, but only
if the fold fluid holds the volume of the extra times fixed with a pressure that grows like the fourth power of the expansion rate in units
of $H$ (the next section; what could supply it is OPEN). Status: DERIVED (ST9; `um3_weights.py`, W5 and W6; `um3_geometry.py`, G4).

## What takes the place of the stabiliser

Nothing in the bulk: the corrected bulk is a vacuum on both branches. But one requirement remains, on the fold. The component of the junction
along the extra times (the third line of FE-33) asks the matter of the fold for a definite pressure along the extra times, which radiation has
and dust and vacuum energy do not. Without it the volume of the extra times would change, and with it Newton's constant, the squares of the gauge
and Yukawa couplings and the quartic Higgs coupling of the fold, which the volume divides: since the time of nucleosynthesis Newton's constant
would have fallen by the factor 15.8, and today it would change 6800 times faster than lunar laser ranging allows (with the pressure
$-\rho_{\mathrm{b}}$ of the baryons along the extra times, ASSUMED; 7973 times without it). UM-3 therefore assumes that the fold fluid, the thin
medium of the fold, supplies the missing pressure $q_{\mathrm{hold}}$:

$$
\begin{aligned}
&p_{\mathrm{ff}} = -\rho_{\mathrm{ff}},\qquad q_{\mathrm{ff}} = -\rho_{\mathrm{ff}} + q_{\mathrm{hold}},\qquad
 \lambda_{\mathrm{F}} = \frac{32HV_*}{5\kappa},\\
&q_{\mathrm{hold}} = -\Delta_{\mathrm{r}} - \frac45\big(\mathsf{A}^4 + \mathsf{A}^2\mathsf{A}_1\big)\frac{HV_*}{\kappa},\qquad
 \Delta_{\mathrm{r}} = q_{\mathrm{SM}} + q_\chi + q_{\mathrm{P}} - \big(\rho_{\mathrm{ff}} - \lambda_{\mathrm{F}}\big) + \frac{\rho - 3\mathcal{P}}{2}
\end{aligned} \tag{FE-65}
$$
<!-- symbols: pff, rhoff, qff, qhold, lambdaF, Hconst, Vstar, kappa, Deltar, Asf, A1sf, qSM, qchi, qP, rhotot, Ptot -->
<!-- begin generated symbol list -->
**Symbols in (FE-65).**

- $p_{\mathrm{ff}}$: The pressure of the fold fluid along ordinary space. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}}$ (a tension). Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}} + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times: minus its energy density (its tension) plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$. Status: ASSUMED (the fluid), DERIVED (the value).
- $q_{\mathrm{hold}}$: The pressure along the extra times that the fold fluid adds to its tension to hold the volume of the extra times fixed (four-dimensional normalisation). Unit: GeV$^4$. Value: $-\Delta_{\mathrm{r}}$ today: $-0.793\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have the pressure $-\rho_{\mathrm{b}}$ along the extra times (ASSUMED), $-0.842\,\rho_{\mathrm{c}}^{(0)}$ if they have none, $-0.891\,\rho_{\mathrm{c}}^{(0)}$ for $+\rho_{\mathrm{b}}$. Status: DERIVED (the value), ASSUMED (that the fold fluid supplies it).
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of ordinary space of the fold (four-dimensional normalisation); the excess of that total over $\lambda_{\mathrm{F}}$ is the dark energy $\rho_\Lambda$. Unit: GeV$^4$. Value: $32HV_*/(5\kappa) = 6H^2/(8\pi G_{\mathrm{N}})$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\Delta_{\mathrm{r}}$: The mismatch of the radion condition: the sum over the matter of the fold of its pressure along the extra times and $(\rho - 3\mathcal{P})/2$ (zero for radiation). Unit: GeV$^4$. Value: today $0.793\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have the pressure $-\rho_{\mathrm{b}}$ along the extra times (ASSUMED), $0.842\,\rho_{\mathrm{c}}^{(0)}$ if they have none, $0.891\,\rho_{\mathrm{c}}^{(0)}$ for $+\rho_{\mathrm{b}}$. Status: DERIVED (the condition and the values for each choice), ASSUMED (the pressure of the baryons along the extra times).
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{SM}}$: The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times). Unit: GeV$^4$. Status: DERIVED (for radiation and free fields), ASSUMED (for the baryons).
- $q_\chi$: The pressure of the bound states of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{P}}$: The pressure of the portals along the extra times: their mean on-shell Lagrangian density. Unit: GeV$^4$. Status: DERIVED.
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->

The equation of the volume of the extra times (the radion) shows what $q_{\mathrm{hold}}$ does:

$$
H^2\big(\mathsf{V}_1 + 3\mathsf{V}(\mathsf{A} + \mathsf{V})\big) = \frac{8\pi G_{\mathrm{N}}}{5}\big(\rho - 3\mathcal{P} + 2q_{\mathrm{tot}}\big) \tag{FE-72}
$$
<!-- symbols: Hconst, V1sf, Vsf, Asf, pi, GN, rhotot, Ptot, qtot -->
<!-- begin generated symbol list -->
**Symbols in (FE-72).**

- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathsf{V}_1$: The time derivative of $\mathsf{V}$ in units of $H$, $\mathsf{V}_1 = \mathsf{V}'/H$. Unit: dimensionless. Status: DERIVED.
- $\mathsf{V}$: The rate of change of the scale factor $\mathrm{e}^{-a_4}b_4$ of the extra times on the fold in units of $H$, $\mathsf{V} = \mathsf{U} - \mathsf{A}$; zero with frozen extra times. Unit: dimensionless. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $q_{\mathrm{tot}}$: The total pressure along the extra times of the matter of the fold (the Standard Model, the bound states of dirac16complex, the portals and the fold fluid without its tension). Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->

The rate $\mathsf{V}$ of the scale factor of the extra times stays zero only if $\rho - 3\mathcal{P} + 2q_{\mathrm{tot}} = 0$, and $q_{\mathrm{hold}}$
makes this so. It acts as a potential that holds the size of the extra times, a role that the "block stabiliser" of the first universe model
of this repository played for its own metric; what produces it is OPEN. Today $q_{\mathrm{hold}} = -0.793$ times the critical density of the
universe, if the baryons have the pressure $-\rho_{\mathrm{b}}$ along the extra times ($-0.842$ or $-0.891$ times it for 0 or $+\rho_{\mathrm{b}}$). In an
early universe that expands faster than $H$ the term of order $\mathsf{A}^4$ dominates, and during an inflation of the fold at the rate
$\mathsf{A}H$ the holding pressure would have to be about $\mathsf{A}^4/8$ times the tension of the fold: at least $10^{103}$ times for an
inflation at the largest rate that the bound on primordial gravitational waves allows if $H \lesssim 4.6\times10^{-13}$ GeV, and more for a
smaller $H$; what could supply it is OPEN. The tension that the static block requires, $\lambda_{\mathrm{F}}$, is the total of the tension of the fold fluid and of the vacuum
energy of the fields of the fold; the excess of that total over $\lambda_{\mathrm{F}}$ is the dark energy. Status: DERIVED (the requirement and its
value, `um3_series.py`, SR4 to SR6; `um3_primordial.py`, PR4), ASSUMED (that the fold fluid supplies it; the pressure of the baryons), OPEN (its
origin and its size in the early universe).

# The five points, verified

**[1] The stabiliser couples only to gravity.** By its definition it had no term in the action of UM-3 other than its own: it entered the
field equations only through its energy-momentum tensor in FE-1, and it exerted no force on dirac16complex or on the Standard Model except
through the curvature that it caused. On the static bulk this was consistent: the stabiliser was conserved by itself (ST4). In an expanding
universe the bulk source that the original equations required released energy (SB-15) that flowed into the fold (SB-14) and was taken up
there (SB-16). What the equations fixed was the total bulk source and its flow; whether this meant an exchange of energy between the
stabiliser and the matter of the fold, or a second medium of the bulk, or a thin layer of the stabiliser itself, they did not say (ASSUMED,
an interpretation). **Verdict, original weights:** exact on the static bulk; in an expanding universe a medium that couples only to gravity
and keeps $p = 5\rho$ was not enough to supply the required source (SB-13 against SB-14). **Verdict, corrected weights:** there is no
stabiliser, and the bulk of an expanding fold with frozen extra times is a vacuum without any flow (FE-33). Status: DERIVED (ST4, ST6, ST9).

**[2] It is absent in the primordial era, whose bulk is the author's vacuum (FE-31).** With the original weights the author's vacuum,
$a_4 = Hx_4$ with constant $b_4$ ($\mathsf{A} = 1$, $\mathsf{U} = 0$), solved the field equations of the bulk with nothing on the right (ST2), and with
the stabiliser present it would not have been a solution: the stabiliser was absent there. But a stabiliser that couples only to gravity and
keeps $p = 5\rho$ cannot appear later out of nothing (SB-13). Points [1] and [2] together required a mechanism that created it between the
primordial era and the late universe: an exchange of energy with the fold (which breaks [1]), a conversion from or into dirac16complex in
the bulk (the bulk source is the sum of both), or a change of its equation of state (which a single medium with $p = 5\rho$ does not have);
UM-3 contained none. **Verdict, original weights:** [2] true, with the creation of the stabiliser OPEN. **Verdict, corrected weights:** the
author's vacuum is not a solution (FE-31); the primordial era can be an inflation of the fold with frozen extra times, whose bulk is a
vacuum (if an enormous pressure holds the volume of the extra times, OPEN); no era of UM-3 has a stabiliser, so the question of its creation
no longer arises. Status: DERIVED (ST2, ST6, ST9; `um3_primordial.py`, PR0).

**[3] Its existence and value are DERIVED from the requirement of a static bulk.** With the original weights the value was DERIVED: SB-9
fixed every entry (ST1). The existence of a bulk source was DERIVED more generally than for an exactly static bulk: without any bulk source
the bulk was at every instant the author's vacuum or its time reverse (SB-17, ST3, ST8), so a slowly expanding bulk needed one. What was
ASSUMED is that the source is a separate medium, with dirac16complex contributing nothing; its microscopic nature was OPEN, and among
homogeneous scalar fields only a ghost reproduced it (SB-12, ST5). **Verdict:** value DERIVED; the existence of a bulk source DERIVED; its
identification with a separate medium ASSUMED. With the corrected weights the same derivation gives the value zero (IN-7, ST9): the
existence of the stabiliser was a consequence of the original weights.

**[4] The static bulk** is defined in SB-5 and illustrated by five examples and a comparison of static and empty spacetimes in the part
"The static bulk".

**[5] Warp and warp factor** are defined in SB-2 and illustrated by four examples in the part "Warp and warp factor".

# The importance of the stabiliser for UM-3

**With the original weights, no late universe like ours without it.** A bulk without any source was at every instant the author's vacuum or
its time reverse (SB-17): ordinary space had to grow or shrink at the full rate $H$. The only alternative to the stabiliser would have been
to make the author's vacuum itself the late universe, with $H$ equal to today's expansion rate $H_4^{(0)}$. But in the author's vacuum the
extra times shrink, as $\mathrm{e}^{-a_4}b_4 = \mathrm{e}^{-Hx_4}b_4$, and the squares of the gauge and Yukawa couplings and the quartic Higgs
coupling of the fold are divided by the volume of the extra times, so they grow as $\mathrm{e}^{3Hx_4}$. The natural nuclear reactor of Oklo (Gabon), which ran about 1.8
billion years ago, bounds the change of the fine-structure constant $\alpha_{\mathrm{em}}$ since then to about one part in ten million
($-0.9\times10^{-7} < \Delta\alpha_{\mathrm{em}}/\alpha_{\mathrm{em}} < 1.2\times10^{-7}$). The author's vacuum would change it by

$$
\Delta\ln\alpha_{\mathrm{em}} = 3H_4^{(0)}\,\Delta x_4 = 0.372 \tag{SB-18}
$$
<!-- symbols: Delta, alphaem, H4, x4 -->
<!-- begin generated symbol list -->
**Symbols in (SB-18).**

- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\alpha_{\mathrm{em}}$: The fine-structure constant. Unit: dimensionless. Value: 1/137.036. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.

<!-- end generated symbol list -->

($H_4^{(0)} = 67.4$ km/s/Mpc, $\Delta x_4 = 1.8$ Gyr; $\Delta$ marks a change): 3.1 million times the bound. With the stabiliser and frozen extra
times the couplings stayed constant. Status: DERIVED (ST7), STANDARD (the bound of Oklo).

**With the original weights, the zero point of the expansion.** With frozen extra times the energy constraint was a Friedmann equation of the
bulk, $3a_4'^2 = 16\kappa(\rho_{\mathrm{bulk}} - \rho_{\mathrm{s}})$ (SB-17): the energy density of the stabiliser was the energy density of the bulk at
which ordinary space stands still, and the expansion measured the excess of the bulk energy density over it. Integrated over the hidden
direction and the extra times, per unit volume of ordinary space on the fold, the stabiliser carried the energy

$$
\rho_{4,\mathrm{s}} = \frac{\rho_{\mathrm{s}}V_*}{3H} = -\frac{HV_*}{48\kappa} \tag{SB-19}
$$
<!-- symbols: rho4s, rhos, Vstar, Hconst, kappa -->
<!-- begin generated symbol list -->
**Symbols in (SB-19).**

- $\rho_{4,\mathrm{s}}$: The energy of the stabiliser per unit volume of ordinary space of the fold with the author's original weights: its energy density integrated over the hidden direction and the extra times. Unit: GeV$^4$. Value: $-HV_*/(48\kappa)$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser of the bulk with the author's original weights; with frozen extra times it was the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.

<!-- end generated symbol list -->

(the volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$ of the warped directions, integrated over both sides of the fold, gives $1/(3H)$, and $V_*$ is
the physical volume of the extra times on the fold in the late universe). It was not a vacuum energy that makes the fold expand: the static
block as a whole did not expand at all. Status: DERIVED (ST7, ST8).

**With the original weights, the most exotic ingredient.** Its violation of the null energy condition (SB-11) put it among the sources that
come with instabilities or with signals faster than light; Einstein's static universe, the example most like it, is unstable. If the
stabiliser had been a ghost field, its quanta would carry negative energy, and even through gravity alone a ghost lets the vacuum decay into
pairs of ghosts and pairs of ordinary particles, at a rate that is finite only if the momenta of the ghosts are cut off (Cline, Jeon and
Moore, 2004). Whether the static block with the stabiliser was stable was never analysed. Status: STANDARD (the general results).

**With the corrected weights, its absence changes UM-3.** The weights for which the graviton of the fold travels at the speed of light while
no graviton of the static bulk travels faster make the static bulk a vacuum, and the stabiliser disappears with them. Four consequences:

1. The gravitational waves of the four-dimensional world travel at the speed of light at every wavelength, at the lowest order in their
   amplitude (FE-69 with the corrected weights, $\kappa K_{44} = \kappa K_{33}$), so the bound that the neutron-star merger GW170817 sets on
   their speed (its gravitational waves arrived together with its light) is satisfied for every value of $H$. The propagation of the
   polarisation along the extra times on an expanding fold is not settled (generically not luminal), and no weights give gravitons at the speed of light in the bulk as well (the part on
   the correction).
2. The fold obeys the Friedmann equations of four-dimensional general relativity exactly, with Newton's constant $8\pi G_{\mathrm{N}} = \kappa_7/V_*$,
   $\kappa_7 = 15\kappa H/16$ (FE-33): the Gauss-Bonnet and cubic terms give the fold an Einstein-Hilbert term of its own (the action of
   general relativity, the scalar curvature of the metric of the fold times a constant, here $V_*/(2\kappa_7)$; it is what makes gravity on
   the fold that of general relativity).
3. The bulk needs no exotic medium in any era: no violation of the null energy condition, no ghost, and no question of how the stabiliser
   would be created after the primordial era.
4. Two new tasks appear. The fold fluid must hold the volume of the extra times fixed with the pressure $q_{\mathrm{hold}}$ (FE-65, FE-72), whose
   origin is OPEN and which would be enormous in an early universe that expands faster than $H$; and the static block is a degenerate vacuum
   (the double and triple roots of FE-70), around which the bulk equations have no linear part for any perturbation of the metric, so the
   bulk is strongly coupled and its response to sources that depend on $\sigma$ is not computed (OPEN).

**Summary.** The stabiliser was the price of a slowly expanding late universe with constant couplings in the author's metric with the
author's original weights and cosmological constant. Its value was fixed exactly and introduced no new parameter. It was not a property of
the author's metric but of those weights: the weights that make the graviton of the fold travel at the speed of light without a faster
graviton in the static bulk make the static bulk empty, and the stabiliser vanishes with them.

# Provenance

**What comes from the author (AUTHOR).** The coordinates $X = \{x_0, \dots, x_7\}$ and their roles
(`Dirac_Einstein-Lovelock_4+4_Nash.nb`, section DEFCHART); the metric with $b_4[x_4]^2$ and its two functions $a_4(x_4)$ and $b_4(x_4)$ (the
author's order of 2026-10-24); the Einstein-Lovelock action with its original weights $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ and the
cosmological constant $\Lambda = -10H^2$ (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[134], where the author writes the pure number 10); the
author's vacuum $a_4 = Hx_4$ with constant $b_4$; the field dirac16complex; the order of 2026-10-25, 05:09 PDT, to document the stabiliser
with proper attribution and to verify the five points; and the order of 2026-10-25, 07:55 PDT: "Gravitons must travel at c. If these
incorrect claims come from my choice of the Lovelock couplings and my choice of the cosmological constant $\Lambda$ THEN my choices are wrong,
and you MUST correct them."

**What UM-3 adds.** The proper distance $\sigma$ (DERIVED from the metric); the static block as the first approximation of the late universe
(ASSUMED); the stabiliser of the original weights (found and named by Claude on 2026-10-24; its value DERIVED, the medium ASSUMED); the
corrected weights $w_{(2)} = 1/20$, $w_{(3)} = 1/360$ and $\Lambda = -7H^2$ (DERIVED by Claude at the author's order of 07:55; the original weights
are the author's); the fold fluid with its tension and its holding pressure (ASSUMED, with DERIVED values).

**The lineage.** The first universe model of this repository (the folder `Revision/universe_model`, version 1.1, present at the first
commit of the repository, `0fdf375` of 2026-10-19) assumed a "block stabiliser": a potential for the size $\mathrm{e}^{-a_4}b_4^{1/2}$ of the block
of the hidden direction and the extra times of its metric (whose extra-time components carried $b_4$ instead of $b_4^2$), with an origin left
open; that version had itself changed the third weight to $1/768$. The second universe model (`universe_model_2`, version 3 of 2026-10-18)
assumed a block stabiliser whose energy density falls as the inverse eighth power of the block scale, $\kappa\rho_{\mathrm{stab}} =
(26 + 4\sqrt{51})H^2 = 54.566H^2$ at its static point. The stabiliser of UM-3 was a new object, for the author's new metric with $b_4^2$, with a
negative energy density and $p = 5\rho$.

**Who found what, and when.** On 2026-10-24 Claude computed, in the gravity module of UM-3 (`um3_geometry.py`, check G4, commit `4448938` of
2026-10-24 17:54 UTC-7), that a static bulk of the author's metric needs the energy density $-H^2/(16\kappa)$ and that the bulk with frozen extra
times needs the energy density $(3\mathsf{A}^2 - 1)H^2/(16\kappa)$ and a flow of energy along the hidden direction; the pressures $-5H^2/(16\kappa)$ were
added when the medium was introduced and named "the stabiliser of the bulk", as the term IN-7 of the action of UM-3, in the commit `170d8d3`
of 2026-10-24 19:05 UTC-7 (the field equations of UM-3, where its existence was labelled ASSUMED and its value DERIVED). On 2026-10-25, at the
author's order of 05:09, Claude wrote the first version of this document with its LaTeX source and its PDF and the checks ST1 to ST8 (commit
`cd5709d` of 2026-10-25 06:55 UTC-7), and an independent referee read it; its corrections (the energy conditions of a negative vacuum energy,
the use of "warp", the constraints of a sourceless bulk, the rates of the extra times, the derivation of SB-9, the junction conditions, the
lineage and the references) are in this version. After the author's order of 07:55 Claude derived the weights for which the graviton of the
fold travels at the speed of light while no graviton of the static bulk travels faster (`um3_weights.py`), found that with them the static bulk is a
vacuum and the stabiliser vanishes (check ST9), and rewrote this document as the record of the stabiliser and of its removal (commit
`6767be3`). That version claimed that gravitons then travel at the speed of light everywhere; independent referees (Claude agents of the
same session) showed that the static bulk has no linear graviton at all, that the bulk of an expanding fold keeps modes without a
time-kinetic term, that the propagation of the polarisation along the extra times on an expanding fold is not settled (generically not
luminal), and that no weights give gravitons at the speed of light both in the bulk and on the fold with the author's metric; the
linearised equations for every perturbation of the metric (`um3_linear.py`, whose jet code one of the referees wrote) confirm it, and this
version says so. All of this work was done in Claude Code sessions configured for the model claude-opus-5-5 (session
https://claude.ai/code/session_01AyG7BZ5rkLxBARRjLHHquB).

**How it was computed.** The left-hand side of the field equations was computed exactly with the computer algebra system sympy for the
general diagonal warped metric $\mathrm{d}\sigma^2 + \mathrm{e}^{2\mathfrak{a}}(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2) - \mathrm{e}^{2\mathfrak{n}}\mathrm{d}x_4^2
- \mathrm{e}^{2\mathfrak{b}}(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2)$, with functions $\mathfrak{a}$, $\mathfrak{n}$, $\mathfrak{b}$ of $\sigma$ and $x_4$: the curvature
in an orthonormal frame, and the Lovelock tensors of orders 1, 2 and 3 contracted with the generalised Kronecker delta. It was then specialised to
the author's metric, $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$, $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$, $\mathfrak{n} = 0$. The source of the fold was
computed from the jump of the first $\sigma$-derivatives of the metric across the fold (the junction conditions FD-11), as the difference of a
junction potential on the two sides, and independently by smoothing the kink. The program `universe_model_3/code/um3_stabiliser.py` of the
repository computes and checks the following:

| check | what it verifies | result |
| --- | --- | --- |
| ST1 | original weights: the static bulk requires the source SB-9 on both sides, without flow; the order-by-order values of SB-8 and its table; the source of the fold SB-10 order by order | PASS |
| ST2 | original weights: the author's vacuum needs no source; its fold source $(-10, -6, -10)H$; the expansion around it | PASS |
| ST3 | original weights: without a source the bulk is at every instant the author's vacuum or its time reverse (the two constraints and their resultant, SB-17) | PASS |
| ST4 | the stabiliser is conserved by itself on the static bulk | PASS |
| ST5 | from the values of ST1: the weak and the null energy condition fail (SB-11); among homogeneous scalar fields only a ghost reproduces it (SB-12) | PASS |
| ST6 | SB-13; the frozen branch SB-14 with its $\mathsf{A}_1$ terms and its fold source; the energy budget SB-15; the tension and pressureless part of the fold source; the balance of the fold SB-16 | PASS |
| ST7 | the drift SB-18 in the author's vacuum, and the share SB-19 | PASS |
| ST8 | the two constraints contain no second time derivative; their form in $(\mathsf{A}, \mathsf{V})$; the Friedmann equation of the bulk | PASS |
| ST9 | corrected weights: the static bulk is a vacuum (IN-7), the fold source is a pure tension (FE-32), the frozen branch and static ordinary space are vacua without flow, the constraints FE-66, the author's vacuum is no longer a solution | PASS |

The other checks used here are in the programs `um3_weights.py` (W1 to W8: the gravitational waves FE-68 and FE-69 for any weights, the
unique weights and the impossibility of gravitons at the speed of light both in the bulk and on the fold, FE-70, the vacua and the fold of the
corrected weights, the gravitons on the two vacuum branches), `um3_linear.py` (LN1 to LN5: the linearised field equations for every
perturbation of the metric), `um3_geometry.py` (G2 to G4: the curvature and the bulk equations of
the author's metric), `um3_fold.py` (J4 to J7: the junction conditions and the sources of the fold), `um3_series.py` (SR4 to SR6: the volume of
the extra times) and `um3_primordial.py` (PR0). `um3_stabiliser.py` writes `outputs/stabiliser.json` and `reports/stabiliser_checks.json`, reads
the general source of the fold from the output of `um3_fold.py`, and runs in about 45 seconds (`python universe_model_3/code/um3_stabiliser.py`
from the root of the repository).

**Sources outside UM-3 (STANDARD).** A. Einstein, "Kosmologische Betrachtungen zur allgemeinen Relativitätstheorie", Sitzungsberichte der
Königlich Preußischen Akademie der Wissenschaften (1917) 142 (the static universe, SB-6); A. S. Eddington, "On the instability of Einstein's
spherical world", Monthly Notices of the Royal Astronomical Society 90 (1930) 668; K. Schwarzschild, "Über das Gravitationsfeld eines
Massenpunktes nach der Einsteinschen Theorie", Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (1916) 189 (the static
field outside a mass); D. Lovelock, "The Einstein tensor and its generalizations", Journal of Mathematical Physics 12 (1971) 498;
W. Israel, "Singular hypersurfaces and thin shells in general relativity", Il Nuovo Cimento B 44 (1966) 1 (the junction conditions);
S. C. Davis, "Generalised Israel junction conditions for a Gauss-Bonnet brane world", Physical Review D 67 (2003) 024030; E. Gravanis and
S. Willison, "Israel conditions for the Gauss-Bonnet theory and the Friedmann equation on the brane universe", Physics Letters B 562 (2003) 118;
R. V. Pound and G. A. Rebka, "Apparent weight of photons", Physical Review Letters 4 (1960) 337; L. Randall and R. Sundrum, "A large mass
hierarchy from a small extra dimension", Physical Review Letters 83 (1999) 3370, and "An alternative to compactification", Physical Review
Letters 83 (1999) 4690 (FD-8); P. Hořava and E. Witten, "Heterotic and type I string dynamics from eleven dimensions", Nuclear Physics B 460
(1996) 506, and "Eleven-dimensional supergravity on a manifold with boundary", Nuclear Physics B 475 (1996) 94 (example 9 of the definition of
the fold); H. Whitney, "On singularities of mappings of Euclidean spaces. I. Mappings of the plane into the plane", Annals of Mathematics 62
(1955) 374 (the fold map of example 5); S. W. Hawking and G. F. R. Ellis, "The Large Scale Structure of Space-Time" (Cambridge University Press, 1973) (the
energy conditions); S. Dubovsky, T. Grégoire, A. Nicolis and R. Rattazzi, "Null energy condition and superluminal propagation", Journal of High
Energy Physics 03 (2006) 025; J. M. Cline, S. Jeon and G. D. Moore, "The phantom menaced: constraints on low-energy effective ghosts", Physical
Review D 70 (2004) 043543; the bound of Oklo on the drift of the fine-structure constant over 1.8 Gyr (A. I. Shlyakhter, "Direct test of the
constancy of fundamental nuclear constants", Nature 264 (1976) 340; T. Damour and F. Dyson, "The Oklo bound on the time variation of the
fine-structure constant revisited", Nuclear Physics B 480 (1996) 37); the Hubble constant $H_4^{(0)} = 67.4$ km/s/Mpc (Planck Collaboration,
"Planck 2018 results. VI. Cosmological parameters", Astronomy and Astrophysics 641 (2020) A6); the speed of gravitational waves (B. P. Abbott et
al., "Gravitational waves and gamma-rays from a binary neutron star merger: GW170817 and GRB 170817A", Astrophysical Journal Letters 848 (2017)
L13); the Born-Infeld gravity of eight dimensions and its degenerate vacuum (M. Bañados, C. Teitelboim and J. Zanelli, "Dimensionally
continued black holes", Physical Review D 49 (1994) 975; J. Crisóstomo, R. Troncoso and J. Zanelli, "Black hole scan", Physical Review D 62
(2000) 084013; G. Arenas-Henriquez, R. B. Mann, O. Miskovic and R. Olea, "Mass in Lovelock unique vacuum gravity theories", Physical
Review D 100 (2019) 064038).

# Further symbols

<!-- further symbols: SPsi, hhat, rhoL, rhob, rhoc, rhovac, Tany, awarp, bwarp, cs, nwarp, rhod, Lfold, inn, epsb, varsigma, ctxw -->
<!-- begin generated symbol list -->
**Further symbols.** These symbols appear in the definitions of the symbols listed after the equations of this document.

- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}$. Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $\rho_{\mathrm{c}}$: The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today. Unit: GeV$^4$. Value: $\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$. Status: STANDARD.
- $\rho_{\mathrm{vac}}$: The vacuum energy of the fields of the fold: the minimum of their potential (for the Standard Model the minimum of the Higgs potential with its loop corrections), a tension of the seven-dimensional fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathfrak{a},\ \mathfrak{a}_1$: The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{b},\ \mathfrak{b}_1$: The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $c_{\mathrm{s}}$: The sound speed of the baryon gas: its square is the temperature of the gas divided by the mean mass per particle, times one minus a third of the logarithmic derivative of that temperature with respect to $a$. Unit: dimensionless. Status: STANDARD.
- $\mathfrak{n},\ \mathfrak{n}_1$: The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\rho_{\mathrm{d}}$: The pressureless part of the static source of the fold with the author's original weights: the energy density of the fold fluid minus its tension, per unit volume of ordinary space of the fold. Unit: GeV$^4$. Value: $HV_*/(8\kappa)$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $n$: The order $n = 1, 2, \dots$ of a term of the power series of the metric (also the exponent of the bookkeeping parameter $\epsilon_{\mathrm{b}}$); $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{n}_n$ are the terms of order $n$. Status: STANDARD.
- $\epsilon_{\mathrm{b}}$: The bookkeeping parameter of the deformations of the metric along $\sigma$ that sources depending on $\sigma$ require (their amplitude relative to the order-0 metric of the author). Unit: dimensionless. Status: STANDARD.
- $\varsigma$: The auxiliary variable of the bound-state condition, $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($\varsigma_- = \sqrt{-\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ when $\mu_{\mathrm{L}}\mu_{\mathrm{R}} < 0$). Unit: dimensionless. Status: DERIVED.
- $c_{\mathrm{tx}}$: The common value of the two coefficients $c_{\mathrm{t}} = c_{\mathrm{x}}$ of the bulk equation of a transverse traceless gravitational wave at the static block on the line $w_{(2)} = 18w_{(3)}$ of the Lovelock weights, where bulk gravitons move with the local speed of light: $c_{\mathrm{tx}} = 1 - 360w_{(3)}$ (weights that UM-3 does not use). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->
