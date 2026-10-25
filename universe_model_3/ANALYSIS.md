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

## What this document contains

The author asks for three analyses of the universe model UM-3: the mass mechanism along the hidden coordinate $x_0$ (the period
$\pi/(6H)$ of the metric and the uncertainty relation), whether dirac16complex can be the dark matter, and whether it can be the
dark energy. He also asks to be told what he may have left out, and (on 2026-10-25) for answers to the questions that UM-3 had left
open. This document gives the answers. All of them use the Lovelock weights $1, 1/20, 1/360$ and the cosmological constant
$\Lambda = -7H^2$ that UM-3 adopted at the author's order of 2026-10-25 (the only weights for which the graviton of the fold travels at
the speed of light while no graviton of the static bulk travels faster, a criterion chosen because the order cannot be met in full:
no weights give gravitons at the speed of light in the bulk as well);
results of the author's original values ($1, 1/32, 1/1152$ and $-10H^2$) are records and labelled so. It is self-contained: every
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
and his orders of 2026-10-24 and 2026-10-25; the corrected values of the Lovelock weights and of the cosmological constant that the
second order requires are DERIVED), **RECORD** (from the record of this repository: the Lagrangian of dirac16complex with its canonical
spin connection and contact self-interaction, the Kohn-Sham treatment), **STANDARD** (textbook physics or a published measurement,
named), **ASSUMED** (a choice of UM-3 without derivation), **INVENTED** (a new interaction of UM-3: the portals of dirac16complex),
**DERIVED** (computed and verified in UM-3, with the verification stated), **ESTIMATE** (an order-of-magnitude evaluation) and
**OPEN** (not settled).

## Every equation is followed by its symbols

Every display equation is followed by the list of EVERY symbol that appears in it, with its meaning, unit (natural units,
in which the reduced Planck constant $\hbar$ and the speed of light $c$ are 1), value and status. A symbol that one of these meanings uses is itself listed in this document. The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space-like
coordinate (the metric depends on it through $z = 6Hx_0$), $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ three
extra time-like coordinates; the signature is $(+,+,+,+,-,-,-,-)$. $H$ is the author's constant (an inverse length), a free
parameter of UM-3. The Standard Model lives on the fold of the metric (the surface $z = \pi/2$, where the proper coordinate
$\sigma$ of the hidden direction is zero; ASSUMED), dirac16complex and gravity in the bulk.

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
   norm of their charge does not make the vacuum decay, item 5), gravitate on the fold like matter of the fold if their layer acts as a
   thin source (ASSUMED: the response of the strongly coupled bulk to their profile is OPEN), form a pressureless gas in the dilute limit, and are a thermal relic with the measured density if they annihilate with
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
   author), a thin fluid on the fold (a tension and a pressure along the extra times that holds their volume fixed), and the gauge
   field that the author's ad hoc Higgs vacuum needs (the doublet $(\mathcal{A}, v + h)/\sqrt2$ with the decaying upper component
   $\mathcal{A} = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$). The author's original Lovelock weights made gravitons faster than light and needed a
   medium in the bulk (the stabiliser); at his order of 2026-10-25 they were replaced by the only weights for which the graviton of the
   fold travels at the speed of light while no graviton of the static bulk travels faster. With them the bulk is a vacuum, the fold
   has its own Einstein-Hilbert term, and the four-dimensional graviton travels at the speed of light at linear order; but the static
   bulk has no linear graviton at all and is strongly coupled, the bulk of an expanding fold keeps modes without a time-kinetic term
   (they respond instantaneously), the propagation of the polarisation along the extra times on an expanding fold is OPEN (generically
   not luminal), and no weights give gravitons at the speed of light in the bulk as well, because the time of the author's metric is
   not warped. The last
   section lists the additions and the open problems.
5. **The open questions.** The Krein norm: the vacuum is stable; whether the gas of $\chi$ is classically stable is not decided by the
   computations (flat directions, a truncated response of the size of its error, complex partner levels not converged); the chiral
   couplings of the fold (the author's left-handed Higgs portal among them) produce ghosts, so UM-3 with them is not unitary. The extra
   times: every field with a momentum along them is tachyonic, and compact extra times do not help; UM-3 needs a gauge principle that
   removes that momentum. The speed of $\chi$: its group velocity exceeds that of light by up to 0.46 per cent (in the computed regime)
   when it is ultrarelativistic, its front velocity is that of light, signals through the bulk outrun light on the fold, and the four
   time-like directions allow closed time-like curves; the Standard Model inherits a Lorentz violation through loops unless
   $q_{\mathrm{b}}/H$ is above about $10^{13}$ to $4\times10^{15}$. The primordial era: the author's vacuum is not a solution with the corrected
   weights; the primordial era can be an inflation of the fold with the volume of the extra times held fixed, as in general relativity,
   but the pressure that holds the volume would have to be enormous (about $\mathsf{A}^4/8$ times the tension of the fold, with
   $\mathsf{A} = H_{\mathrm{inf}}/H$: at least $10^{103}$ for an inflation at the largest rate that the tensor bound allows if
   $H \lesssim 4.6\times10^{-13}$ GeV), and the Higgs
   field could be its inflaton only with a coupling to the curvature of the fold that the action of UM-3 does not contain. The
   neutrinos: the Dirac phase drops out of every result of UM-3; the lightest mass is below 23 meV and changes only the capture rate
   of the cosmic neutrinos (DERIVED, ESTIMATE; OPEN: the stability of the gas, a unitary coupling, the gauge principle, the holding
   pressure of the early universe, the inflaton).

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
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

The author's metric and its proper chart. The metric depends on $x_0$ only through $z = 6Hx_0$, so its coefficients repeat with
the coordinate period $\pi/(6H)$: one period is $0 < z < \pi$, with the fold at $z = \pi/2$ and the tips at $z = 0$ and $z = \pi$, where
$g_{x_0x_0} = \cot^2z$ diverges and the warp factor $(\sin^2z)^{1/6}$ vanishes. Status: AUTHOR (the metric), DERIVED (the chart).

$$
\int_0^{\pi/(6H)}\sqrt{\cot^2(6Hx_0)}\;\mathrm{d}x_0 = \frac{1}{6H}\int_0^{\pi}\lvert\cot z\rvert\,\mathrm{d}z = \infty,\qquad
\sigma(z) = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H} \to \mp\infty\ \ (z \to 0,\ \pi) \tag{A-1}
$$
<!-- symbols: x0, Hconst, diff, zvar, pi, infty, sigma, sgn -->
<!-- begin generated symbol list -->
**Symbols in (A-1).**

- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.

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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
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

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of a bound state and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathbb{K}$: The transfer matrix of the profile equation at zero momentum, $\chi' = \mathbb{K}\chi$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
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
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
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
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold: $\hat\gamma^{(a)}$ along the frame directions of the fold and $\hat\gamma^\mu$ along its coordinates (the frame matrices contracted with the inverse frame field of the fold), $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

$$
Q_\Psi = \int\mathrm{d}\sigma\,\mathrm{d}^3x\,\sqrt{\lvert g\rvert}\;\Psi^\dagger\mathfrak{B}\Psi,\qquad
\mathfrak{B} = \mathrm{i}\,\sigma_{16}\,\gamma^{(4)},\qquad \mathfrak{B}^\dagger = \mathfrak{B},\qquad \mathfrak{B}^2 = \mathbf{1},\qquad
E_o = -\omega_o\,\mathcal{Q}_o \tag{FE-43}
$$
<!-- symbols: QPsi, diff, sigma, xfour, metric, Psi, dagger, Bkrein, imag, sigma16, gammaM, identity, Eorb, io, omegafreq, Qorb -->
<!-- begin generated symbol list -->
**Symbols in (FE-43).**

- $Q_\Psi$: The conserved charge of dirac16complex (the Noether charge of a change of the phase of $\Psi$ by a constant), a Krein form (indefinite); as written it is the charge per unit coordinate volume of the extra times, on which no field depends. Unit: GeV$^3$. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\mathfrak{B}$: The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density. Unit: dimensionless. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
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
quantisation every quantum carries a positive energy, so no such decay exists and the vacuum is stable; whether the gas is classically
stable is not decided, and the chiral portals produce ghosts. Status: DERIVED (no decay into the Standard Model alone, from the form of
IN-16; the Krein signature of the charge, `um3_fields.py`, F3, and `um3_spectra.py`, S4; the quantisation, `um3_krein.py`).

## Gravitation on the fold

$$
\kappa\int_{\text{layer}}\mathcal{T}_\Psi{}^a{}_b\,\mathrm{d}\sigma = \frac{\kappa}{\mathcal{Z}\,V_*}\,\mathcal{T}_\chi{}^a{}_b\qquad\big(H \ll q_{\mathrm{b}}\big) \tag{A-5}
$$
<!-- symbols: kappa, TPsi, ia, ib, diff, sigma, Zfold, Vstar, Tchi, Hconst, qb, SPsi -->
<!-- begin generated symbol list -->
**Symbols in (A-5).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex: $-2/\sqrt{\lvert g\rvert}$ times the variation of the action $S_\Psi$ of dirac16complex with respect to $g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{T}_\chi{}^a{}_b$: The four-dimensional energy-momentum tensor of the gas of the bound particles $\chi$ of dirac16complex, per proper volume of ordinary space at the fold (energy density $\rho_\chi$). Unit: GeV$^4$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.

<!-- end generated symbol list -->

The particles $\chi$ live in the bulk, in a layer of width $1/q_{\mathrm{b}}$ around the fold. The junction conditions of the fold
integrate the bulk field equations across the fold: the jump of the junction potential across the fold equals $\kappa$ times the
energy-momentum tensor $\mathcal{S}$ of everything that lives on the fold. If the layer is thin compared with the scale $1/H$ on which
the metric varies, integrating across the whole layer gives that jump the additional source A-5, where $\mathcal{T}_\chi$ is the
four-dimensional energy-momentum tensor of the gas of $\chi$ (per proper volume of ordinary space) and $\mathcal{Z}V_*$ the proper volume
of the extra times at the fold ($\mathcal{Z} = 1$ with frozen extra times, that is when the size $\mathrm{e}^{-a_4}b_4$ of the extra times
no longer changes). This is exactly the form in which the matter of the fold enters ($\mathcal{S} = \mathcal{T}_{\mathrm{SM}}/V_* + \dots$, the
energy-momentum tensor of the Standard Model divided by the volume of the extra times): the particles $\chi$ gravitate on the fold like
matter of the fold, with the same Newton constant, and enter the Friedmann equation of FE-59 as $\rho_\chi$. This holds exactly only in
the limit of a thin layer. With the corrected Lovelock weights the static block is a degenerate vacuum, whose bulk equations have no
linear part for any perturbation of the metric: the bulk answers the part of the source of the particles $\chi$ away from $\sigma = 0$
only at second order, so its response is not proportional to their density (it is not analytic in it), and the size of the
corrections to A-5 is not known. With a linear bulk they would be of relative order $H/q_{\mathrm{b}}$; for the degenerate bulk this is not
computed. Status: DERIVED (the integration of the junction conditions across a thin layer), ASSUMED (that the layer of the particles
$\chi$ acts as a thin source), OPEN (the response of the strongly coupled bulk to the profile).

## The equation of state of the Kohn-Sham states

$$
\mathsf{E}_{\mathrm{int}} = \frac{G_{\mathrm{KS}}}{2}\int_{-\infty}^{\infty}\mathrm{d}\sigma\,\mathrm{e}^{6H\lvert\sigma\rvert}\Big(\hat\rho^2 - \mathrm{tr}\,\hat{\mathcal{N}}^2\Big),\qquad
\epsilon_{\mathrm{p}} = \omega - \mathsf{E}_{\mathrm{int}},\qquad P_{\mathrm{KS}} = n_\chi\,\mathsf{E}_{\mathrm{int}},\qquad
w_\chi = \frac{P_{\mathrm{KS}}}{n_\chi\,\epsilon_{\mathrm{p}}} \tag{A-8}
$$
<!-- symbols: Eint, GKS, diff, sigma, infty, euler, Hconst, rhohat, trace, Nhat, epsp, omegafreq, PKS, nchi, wchi, chiKS, lamPsi, Nmat, ns, KSorb, nocc -->
<!-- begin generated symbol list -->
**Symbols in (A-8).**

- $\mathsf{E}_{\mathrm{int}}$: The interaction energy per particle of the gas of $\chi$: the mean self-interaction energy $\frac{\lambda_\Psi}{2}(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2)$ integrated across the hidden direction, per particle. Unit: GeV. Status: DERIVED.
- $G_{\mathrm{KS}}$: The dimensionless strength of the self-interaction of the gas of particles $\chi$ in the Kohn-Sham states: the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold divided by the volume $V_*$ of the extra times, $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ (in units of $m_\Psi$ when numbers are given). Unit: dimensionless. Value: $10^{-6}$ to 1 in the solutions. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\hat\rho(\sigma)$: The scalar density of the occupied orbitals, $\hat\rho = \frac14\sum_o\bar\chi_o\chi_o$ (per particle); the scalar density of the gas is $n_{\mathrm{s}} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat\rho$. Unit: GeV. Status: DERIVED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\hat{\mathcal{N}}(\sigma)$: The one-body density matrix of the occupied orbitals, $\hat{\mathcal{N}} = \frac14\sum_o\chi_o\bar\chi_o$ (a $16 \times 16$ matrix at each $\sigma$, per particle); the density matrix of the gas is $\mathcal{N} = (n_\chi/V_*)\,\mathrm{e}^{6H\lvert\sigma\rvert}\hat{\mathcal{N}}$. Unit: GeV. Status: DERIVED.
- $\epsilon_{\mathrm{p}}$: The energy per particle of the gas of $\chi$: the orbital energy minus the interaction energy per particle, which the orbital energy counts twice. Unit: GeV. Status: DERIVED.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $P_{\mathrm{KS}}$: The pressure of the gas of $\chi$ along ordinary space in the Kohn-Sham state: the particles are at rest, so it is the mean self-interaction, $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$. Unit: GeV$^4$. Status: DERIVED.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $w_\chi$: The equation of state of the gas of the particles $\chi$: its pressure divided by its energy density, $w_\chi = P_{\mathrm{KS}}/(n_\chi\epsilon_{\mathrm{p}})$ (0 for cold dark matter, $-1$ for a vacuum energy). Unit: dimensionless. Status: DERIVED.
- $\chi_o(\sigma),\ \bar\chi_o$: The profile of the occupied Kohn-Sham orbital $o$ ($o = 1, \dots, 4$, the four positive-energy states of the bound level) of a homogeneous gas of the particles $\chi$ at rest on the static block: a 16-component spinor function of $\sigma$; the orbital of each particle is $\mathrm{e}^{3H\lvert\sigma\rvert}\chi_o(\sigma)\mathrm{e}^{-\mathrm{i}\omega x_4}$ divided by the square root of the volume of ordinary space and of $V_*$; normalised to the Krein charge $-1$, $\int\mathrm{d}\sigma\,\chi_o^\dagger\mathfrak{B}\chi_o = -1$; $\bar\chi_o = \chi_o^\dagger\sigma_{16}$ is its Dirac adjoint. Unit: GeV$^{1/2}$. Status: DERIVED.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.
- $\mathcal{N}$: The one-body density matrix of dirac16complex, $\mathcal{N} = \sum_o\mathsf{n}_o\varphi_o\bar\varphi_o$ (a $16 \times 16$ matrix at each point). Unit: GeV$^7$. Status: DERIVED.
- $n_{\mathrm{s}}$: The scalar density of dirac16complex in the Kohn-Sham state, $n_{\mathrm{s}} = \langle\bar\Psi\Psi\rangle = \mathrm{tr}\,\mathcal{N}$. Unit: GeV$^7$. Status: DERIVED.
- $\varphi_o,\ \bar\varphi_o$: A Kohn-Sham orbital of dirac16complex (a single-particle solution of the Kohn-Sham equation: the Dirac equation of dirac16complex with the mean field of the gas added to its mass) and its Dirac adjoint. Unit: GeV$^{7/2}$. Status: RECORD.
- $\mathsf{n}_o$: The occupation of the Kohn-Sham orbital $o$ (between 0 and 1). Unit: dimensionless. Status: RECORD.

<!-- end generated symbol list -->

The equation of state of a homogeneous gas of the particles $\chi$ at rest on the fold, from its self-consistent Kohn-Sham states.
Each particle occupies one of the four positive-energy states of the bound level, with the field
$\Psi = \mathrm{e}^{3H\lvert\sigma\rvert}\chi_o(\sigma)\,\mathrm{e}^{-\mathrm{i}\omega x_4}$; the profiles $\chi_o$ obey the Dirac equation along the hidden
direction with the mean field $G_{\mathrm{KS}}\,\mathrm{e}^{6H\lvert\sigma\rvert}(\hat\rho\,\mathbf{1} - \hat{\mathcal{N}})$ of the self-interaction added to the
mass, where $\hat\rho$ and $\hat{\mathcal{N}}$ are the scalar density and the density matrix of the profiles, $\mathrm{e}^{6H\lvert\sigma\rvert}$, one over the
volume factor $\mathrm{e}^{-6H\lvert\sigma\rvert}$ of the six warped directions, turns the densities of the profiles into proper densities, and $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ is the dimensionless strength of the self-interaction (the self-coupling
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
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
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
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
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

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
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
| a thin layer and a near-luminal $\chi$ | $q_{\mathrm{b}} \gg H$ (A-5) and $c_{\mathrm{b}}^2 = q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$ close to 1 ($c_{\mathrm{b}}$ the speed coefficient of $\chi$ along ordinary space in units of the speed of light; $c_{\mathrm{b}}^2$ is the average of the inverse warp factor $\mathrm{e}^{2H\lvert\sigma\rvert}$ over its profile) | ASSUMED (A-5: the layer as a thin source; the response of the strongly coupled bulk to its profile is OPEN), ESTIMATE ($c_{\mathrm{b}}^2$, to first order in the momentum) |
| the effective number of neutrinos $N_{\mathrm{eff}}$ (Planck 2018; ACT DR6, the sixth data release of the Atacama Cosmology Telescope) | the right-handed neutrinos must not be thermalised by the portal: $c^{\nu}_X$ much smaller than the lepton-doublet couplings | DERIVED |

$$
H \ll q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}},\qquad \omega_{\mathrm{b}} \gtrsim 1.5\ \text{TeV},\qquad
\mathfrak{g}_{\mathrm{l}} \approx \frac{1}{\omega_{\mathrm{b}}}\sqrt{\frac{2\pi\cdot4\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle}{9}},\qquad c^{\nu}_X \ll c^{\ell}_X \tag{A-6}
$$
<!-- symbols: Hconst, qb, omegab, gportql, pi, mean, sigmaann, vrel, cf, iX -->
<!-- begin generated symbol list -->
**Symbols in (A-6).**

- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
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
the fold if their layer acts as a thin source, are cold, and have the measured density as a thermal relic, provided they are weakly
bound, heavier than about 1.5 TeV and leptophilic, and the right-handed neutrinos stay out of equilibrium. Status: DERIVED (no decay
into the Standard Model alone, equation of state, relic density), ASSUMED (the layer as a thin source), ESTIMATE (the window), OPEN (the
response of the strongly coupled bulk to their profile; the classical stability of the gas, which the indefinite charge leaves
undecided).

# dirac16complex and the dark energy

$$
\begin{aligned}
&H_4^2 = \frac{8\pi G_{\mathrm{N}}}{3}\big(\rho_{\mathrm{SM}} + \rho_\chi + \rho_\Lambda\big),\qquad
 2H_4' + 3H_4^2 = -8\pi G_{\mathrm{N}}\,\mathcal{P},\qquad
 \frac{1}{8\pi G_{\mathrm{N}}} = \frac{V_*}{\kappa_7} + \frac{1}{\kappa_{\mathrm{ind}}},\qquad \kappa_7 = \frac{15}{16}\,\kappa H,\\
&\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}},\qquad
 q_{\mathrm{SM}} + q_\chi + q_{\mathrm{P}} + q_{\mathrm{ff}} + \lambda_{\mathrm{F}} + \frac{\rho - 3\mathcal{P}}{2}
 = -\frac45\big(\mathsf{A}^4 + \mathsf{A}^2\mathsf{A}_1\big)\frac{HV_*}{\kappa},\\
&q_{\mathrm{SM}} = \big\langle\mathcal{L}_{\mathrm{H}} + \mathcal{L}_{\mathrm{gauge}} + \mathcal{L}_{\mathrm{f}} + \mathcal{L}_{\mathrm{Y}}\big\rangle,\qquad
 q_{\mathrm{P}} = \langle\mathcal{L}_{\mathrm{P}}\rangle
\end{aligned} \tag{FE-59}
$$
<!-- symbols: H4, prime, pi, GN, rhoSM, rhochi, rhoL, Ptot, Vstar, kappa7, kappaind, kappa, Hconst, rhoff, rhovac, lambdaF, qSM, qchi, qP, qff, rhotot, Asf, A1sf, mean, LH, Lgauge, Lf, LY, LP -->
<!-- begin generated symbol list -->
**Symbols in (FE-59).**

- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{SM}}$: The energy density of the Standard-Model particles. Unit: GeV$^4$. Status: STANDARD.
- $\rho_\chi$: The energy density of the dark matter, the bound states $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}$. Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa_7$: The gravitational coupling of the fold: with the corrected Lovelock weights the thin source of the fold equals, to second order in the rates of expansion, the Einstein tensor of the seven-dimensional metric of the fold divided by $\kappa_7 = 15\kappa H/16$, and exactly so in the Friedmann equations of a fold with frozen extra times; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, if the fields of the fold induce one). Unit: GeV$^{-5}$. Value: $15\kappa H/16$. Status: DERIVED.
- $\kappa_{\mathrm{ind}}$: The coupling of the Einstein-Hilbert term $\hat R/(2\kappa_{\mathrm{ind}})$ that the quantum fluctuations of the fields of the fold may induce, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$; it adds to the gravity of the fold, $1/(8\pi G_{\mathrm{N}}) = V_*/\kappa_7 + 1/\kappa_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Value: not fixed by UM-3. Status: ESTIMATE.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}} + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{vac}}$: The vacuum energy of the fields of the fold: the minimum of their potential (for the Standard Model the minimum of the Higgs potential with its loop corrections), a tension of the seven-dimensional fold. Unit: GeV$^4$. Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of ordinary space of the fold (four-dimensional normalisation); the excess of that total over $\lambda_{\mathrm{F}}$ is the dark energy $\rho_\Lambda$. Unit: GeV$^4$. Value: $32HV_*/(5\kappa) = 6H^2/(8\pi G_{\mathrm{N}})$. Status: DERIVED.
- $q_{\mathrm{SM}}$: The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times). Unit: GeV$^4$. Status: DERIVED (for radiation and free fields), ASSUMED (for the baryons).
- $q_\chi$: The pressure of the bound states of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{P}}$: The pressure of the portals along the extra times: their mean on-shell Lagrangian density. Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times: minus its energy density (its tension) plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$. Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $\mathsf{A}_1$: The time derivative of $\mathsf{A}$ in units of $H$, $\mathsf{A}_1 = \mathsf{A}'/H = a_4''/H^2$. Unit: dimensionless. Status: DERIVED.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->

The Einstein equations of the fold (FE-59), exact for frozen extra times: the dark energy of UM-3 is the vacuum energy of the fold
$\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}$, the energy of the fold fluid and the vacuum energy of the fields of the fold
minus the tension $\lambda_{\mathrm{F}} = 32HV_*/(5\kappa)$ that the kink of the static block needs. Status: DERIVED (with the ASSUMED fold
fluid).

$$
\rho_\Lambda = \Omega_\Lambda\,\rho_{\mathrm{c}}^{(0)} = 0.685\cdot\frac{3\big(H_4^{(0)}\big)^2}{8\pi G_{\mathrm{N}}} = 2.5\times10^{-47}\ \text{GeV}^4 = \big(2.2\ \text{meV}\big)^4 \tag{A-7}
$$
<!-- symbols: rhoL, OmegaL, rhoc, H4, pi, GN -->
<!-- begin generated symbol list -->
**Symbols in (A-7).**

- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-3: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}$. Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
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
$(2.2\ \text{meV})^4$ is accommodated by choosing $\rho_{\mathrm{ff}}$, not explained (it is the small excess of a tension of the order
$6H^2/(8\pi G_{\mathrm{N}})$ over $\lambda_{\mathrm{F}}$, a fine tuning as severe as the cosmological-constant problem), and it has $w = -1$ exactly. With the Planck 2018 parameters UM-3 reproduces the CMB, but it
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
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
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
2. *Whether the gas is classically stable is not decided.* At rest the transformations that keep the bound states of the fold form a
   Lie algebra of dimension 32: 16 compact generators keep the two charges apart, 16 boosts mix them (among them the nine boosts
   $\Sigma^{ir}$ between ordinary space and the extra times). The boosts map the self-consistent gas of the Kohn-Sham states onto other
   self-consistent gases with unchanged residuals: they are exact flat directions, whose frequency in the linear response is zero. The
   linear response truncated to the bound level (the admixtures of the four empty orbitals of charge $+1$) has frequencies of the order
   $10^{-4}\,m_\Psi$, two of them imaginary (up to $1.83\times10^{-4}$), but of the size of its truncation error: it does not decide whether
   the dilute gas is stable. Status: DERIVED (KR2, KR4).
3. *The partner level.* In the self-consistent mean field the level of charge $+1$ next to the occupied one is real and bound in the dilute
   gas, and it moves away from the occupied level as the self-interaction grows (the two have opposite parity under the mirror of the
   fold, so they cannot mix). With the strength $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ of the self-interaction ($\lambda_\Psi$ the self-coupling,
   $n_\chi$ the number density of the particles on the fold, $V_*$ the volume of the extra times) it turns complex, $\omega \pm \mathrm{i}\Gamma_{\mathrm{K}}$,
   from $G_{\mathrm{KS}} = 0.3\,m_\Psi$ for $H = 0.05\,m_\Psi$ ($\Gamma_{\mathrm{K}} = 5.1\times10^{-6}$ rising to $6.1\times10^{-4}$ at $G_{\mathrm{KS}} = m_\Psi$),
   from $0.7\,m_\Psi$ for $H = 0.15\,m_\Psi$ and at $m_\Psi$ for $H = 0.3\,m_\Psi$ (inverse width $q_{\mathrm{b}} = 0.3\,m_\Psi$ in all three), where it
   reaches the continuum at the end of the computational box (the first case) or meets another level (the other two). These complex
   levels are not converged in the size of the box, so whether dense gases of $\chi$ grow away from their state is not established; the dark
   matter of today is dilute by many orders of magnitude. Status: DERIVED (KR5), OPEN (the convergence).
4. *The couplings of the fold decide unitarity.* At the fold, at rest, the 16 chirality-blind operators (products of
   $\gamma^{(1)}, \dots, \gamma^{(4)}$) never connect a physical state with a ghost; the 16 chiral ones (the same times $\Gamma_8$) always do. The
   author's Higgs portal acts on the left-handed half only ($P_{\mathrm{L}}$): its amplitude to create a physical $\chi$ together with a ghost
   antiparticle (an s-wave, 0.140) is 0.89 times its elastic amplitude (0.157), while a physical pair needs a p-wave. For moving
   particles the scalar, the density and the vector currents still do not mix, the magnetic dipole does, in proportion to the momentum.
   Ghosts are therefore produced wherever the chiral portals act, and chirality-blind couplings are necessary for unitarity but not shown
   to be sufficient. Status: DERIVED (KR6, KR7).

The answer. The indefinite Krein norm does not make the vacuum decay. Whether it destabilises a gas of $\chi$ is not decided by these
computations: the directions that mix the two charges are exactly flat, the truncated response is inconclusive, and the complex partner
levels of the dense gases are not converged. The real problem is unitarity: with couplings at the fold that distinguish the two
chiralities, the author's left-handed Higgs portal among them, UM-3 produces ghosts and is not a unitary quantum theory. A unitary UM-3
would need couplings of dirac16complex to the fold that do not distinguish the chiralities, and these are necessary but not shown to be
sufficient (OPEN).

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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
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
- $c_{\mathrm{b}}$: The speed coefficient of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum their energy is $\omega^2 = \omega_{\mathrm{b}}^2 + c_{\mathrm{b}}^2\vec k^2$ (it is not a speed that the particles reach: at large momenta $\omega/\lvert\vec k\rvert$ tends to 1, the speed of light). Unit: dimensionless. Status: DERIVED.
- $\vec\kappa$: A momentum along the extra times (three components); the fields of UM-3 have $\vec\kappa = 0$. Unit: GeV. Status: DERIVED.
- $\sigma_{\mathrm{leak}}$: The distance from the fold beyond which a state of dirac16complex with the momentum $\vec\kappa$ along the extra times is no longer bound, $\sigma_{\mathrm{leak}} = \ln\big((m_\Psi^2 - \omega^2)/\vec\kappa^2\big)/(2H)$: the warping multiplies that momentum by $\mathrm{e}^{H\lvert\sigma\rvert}$, and beyond $\sigma_{\mathrm{leak}}$ the local decay rate $\sqrt{m_\Psi^2 - \omega^2 - \vec\kappa^2\mathrm{e}^{2H\lvert\sigma\rvert}}$ of its profile along $\sigma$ is imaginary. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->

The bound particles $\chi$ with a momentum along the extra times. The bound level falls with $\vec\kappa^2$ with the same coefficient with
which it rises with the momentum along ordinary space ($c_{\mathrm{b}}^2 = 1.190$ for $H = 0.05\,m_\Psi$ and $q_{\mathrm{b}} = 0.3\,m_\Psi$, where the
estimate $q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$ gives 1.2), and becomes a tachyon for $\lvert\vec\kappa\rvert > \omega_{\mathrm{b}}/c_{\mathrm{b}} = 0.874\,m_\Psi$ (the law extrapolated to large
momenta). Worse,
the momentum along the extra times is multiplied by $\mathrm{e}^{H\lvert\sigma\rvert}$, one over the square root of the warp factor, so beyond $\sigma_{\mathrm{leak}}$ it exceeds the local gap
and the state leaks into the bulk ($\sigma_{\mathrm{leak}} = 68$, 54 and 46 in units of $1/m_\Psi$ for $\lvert\vec\kappa\rvert = 0.01$, 0.02 and
$0.03\,m_\Psi$; the box of the computation ends before them), at a rate of the order of the tunnelling factor
$\mathrm{e}^{-2q_{\mathrm{b}}\sigma_{\mathrm{leak}}} = \mathrm{e}^{-41}$, $\mathrm{e}^{-33}$ and $\mathrm{e}^{-28}$ (an ESTIMATE): with a momentum along the extra times the
particles $\chi$ are neither strictly bound nor stable. Status: DERIVED (EX2), ESTIMATE (the rate).

$$
\Gamma_{\mathrm{f}} = \frac{-3H_{\mathrm{i}} + \sqrt{9H_{\mathrm{i}}^2 + 4l_{\mathrm{t}}^2}}{2},\qquad
\Gamma_{\mathrm{t}} = \sqrt{l_{\mathrm{t}}^2 - k_{\mathrm{p}}^2},\qquad L_{\mathrm{t}} \ge 2\pi t_0 = 26.6\ \text{Gpc} \tag{A-10}
$$
<!-- symbols: Gammaf, Hi, lt, Gammat, kp, Lt, pi, tzero -->
<!-- begin generated symbol list -->
**Symbols in (A-10).**

- $\Gamma_{\mathrm{f}}$: The growth rate of a mode of a massless field of the fold with the physical momentum $l_{\mathrm{t}}$ along the extra times and no momentum along ordinary space, on the branch of frozen extra times with the constant expansion rate $H_{\mathrm{i}}$ of ordinary space. Unit: GeV (1/time). Status: DERIVED.
- $H_{\mathrm{i}}$: A constant expansion rate $a_4'$ of ordinary space on the branch of frozen extra times (an inflation of the fold, or a constant rate in an example). Unit: GeV. Status: ASSUMED.
- $l_{\mathrm{t}}$: The physical momentum of a mode along the extra times. Unit: GeV. Status: STANDARD.
- $\Gamma_{\mathrm{t}}$: The growth rate of a mode of a massless field of the fold that has a momentum along the extra times, in the late universe. Unit: GeV (1/time). Status: DERIVED.
- $k_{\mathrm{p}}$: The physical momentum of a mode along ordinary space. Unit: GeV. Status: STANDARD.
- $L_{\mathrm{t}}$: The physical period of the extra times, if they are compact. Unit: length. Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.

<!-- end generated symbol list -->

How fast they grow. On the branch of frozen extra times, the background of the late universe and of an inflation of the fold, the
physical momentum $l_{\mathrm{t}}$ along the extra times is constant, and a mode with $\vec k = 0$ grows exponentially, with the expansion rate
$H_{\mathrm{i}}$ of ordinary space at the rate $\Gamma_{\mathrm{f}}$ of A-10 (computed: 0.646586 for $H_{\mathrm{i}} = 0.3$ and $l_{\mathrm{t}} = 1$, equal to the
formula). In the late universe, with $a_4$ and $b_4$ constant, a mode with the physical momenta $l_{\mathrm{t}}$ along
the extra times and $k_{\mathrm{p}}$ along ordinary space grows at the rate $\Gamma_{\mathrm{t}}$ of A-10. If the extra times were compact with the
physical period $L_{\mathrm{t}}$, the slowest mode ($k_{\mathrm{p}} = 0$, $l_{\mathrm{t}} = 2\pi/L_{\mathrm{t}}$) would grow by less than one e-folding over the age
$t_0 = 13.8$ Gyr of the universe only if $L_{\mathrm{t}} \ge 2\pi t_0$ (with the speed of light 1), 26.6 Gpc; for $L_{\mathrm{t}} = 1$ mm it would
grow by $8.2\times10^{29}$ e-foldings. But the $n$-th harmonic, $l_{\mathrm{t}} = 2\pi n/L_{\mathrm{t}}$, grows $n$ times faster, so for every $L_{\mathrm{t}}$
infinitely many modes grow without bound, and a compact time-like direction is itself a closed time-like curve. As a record, in the
author's vacuum ($a_4 = Hx_4$, constant $b_4$; with the original weights) the physical momentum along the extra times grew as $\mathrm{e}^{Hx_4}$,
and a massless mode of the fold with $\vec k = 0$ grew double-exponentially, its logarithm as
$(\lvert\vec\kappa\rvert/(Hb_4))(\mathrm{e}^{Hx_4} - 1) - Hx_4/2$ in the WKB approximation (the computed growth of the logarithm between $Hx_4 = 2$,
2.5 and 3, 4.5359 and 7.6487 for $\lvert\vec\kappa\rvert = Hb_4$, agrees with the predicted 4.5434 and 7.6530). Status: DERIVED (EX3, EX4).

The answer. Fields that depend on the extra times are tachyonic: every field, in the bulk and on the fold, has growing modes once it
carries a momentum along the extra times, and the bound particles $\chi$ with such a momentum also leak into the bulk. UM-3 keeps only
fields without that momentum. This is a consistent truncation (the momentum is conserved, so the sector without it is invariant) but not
a stable one: interactions of fields without momentum create pairs with opposite momenta $\vec\kappa$ and $-\vec\kappa$, which are tachyonic
(EX5; an ESTIMATE, no rate is computed). Making the extra times compact does not help: small extra times only raise the smallest
momentum, and the higher harmonics grow faster still. UM-3 needs a gauge principle that
removes the momentum along the extra times of every field, as the gauge invariance of electromagnetism removes the unphysical
polarisations of the photon; UM-3 does not contain one (OPEN).

## Do the particles $\chi$ move faster than light?

$$
c_{\mathrm{b}}^2 \simeq \frac{q_{\mathrm{b}}}{q_{\mathrm{b}} - H},\qquad
v_{\mathrm{g}} = \frac{\mathrm{d}\omega}{\mathrm{d}\lvert\vec k\rvert} \le 1.0046\ \ \Big(\frac{H}{q_{\mathrm{b}}} = \frac16\Big),\qquad
\sinh\Big(\frac{H\,\Delta x_4}{2}\Big) = \frac{H\,\Delta x_1}{2} \tag{A-11}
$$
<!-- symbols: cb, qb, Hconst, vg, diff, omegafreq, kvec, Delta, x4, x1 -->
<!-- begin generated symbol list -->
**Symbols in (A-11).**

- $c_{\mathrm{b}}$: The speed coefficient of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum their energy is $\omega^2 = \omega_{\mathrm{b}}^2 + c_{\mathrm{b}}^2\vec k^2$ (it is not a speed that the particles reach: at large momenta $\omega/\lvert\vec k\rvert$ tends to 1, the speed of light). Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $v_{\mathrm{g}}$: The group velocity of a particle $\chi$ along ordinary space, $\mathrm{d}\omega/\mathrm{d}\lvert\vec k\rvert$, in units of the speed of light on the fold. Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

Three facts. (1) The speed coefficient of the particles $\chi$ along ordinary space is $c_{\mathrm{b}}$: at small momenta their energy is
$\omega^2 = \omega_{\mathrm{b}}^2 + c_{\mathrm{b}}^2\vec k^2$, and the average of the inverse warp factor $\mathrm{e}^{2H\lvert\sigma\rvert}$ over the density
$\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$ of the profile gives the first expression; the exact dispersion gives $c_{\mathrm{b}}^2 = 1.190$, 1.440 and
1.069 where the estimate gives 1.2, 1.5 and 1.071 (SL1). It is not a speed that the particles reach: a slow $\chi$ moves with the group
velocity $c_{\mathrm{b}}^2\lvert\vec k\rvert/\omega_{\mathrm{b}}$. (2) At large momenta the energy approaches the momentum from above; the group velocity
$v_{\mathrm{g}}$ exceeds 1 only from about $\lvert\vec k\rvert = 6\,m_\Psi$ on, by at most 0.46 per cent near $13\,m_\Psi$ for $H/q_{\mathrm{b}} = 1/6$ (about
0.9 per cent for $H/q_{\mathrm{b}} = 1/3$: the excess grows with $H/q_{\mathrm{b}}$), and the front velocity (the limit of $\omega/\lvert\vec k\rvert$ at infinite
momentum) is the speed of light (SL2). The particles $\chi$ of the halo of the Galaxy move at $10^{-3}$ of the speed of light, and at the
freeze-out of the relic density at 0.37; only ultrarelativistic $\chi$, long before the freeze-out, can outrun light, and only slightly
(SL3). (3) Signals through the bulk are faster than along the fold: at fixed extra times the optical metric of the bulk is the hyperbolic
plane of radius $1/H$, and the earliest signal between two points of the fold at the distance $\Delta x_1$ arrives after the time
$\Delta x_4$ of the third expression, less than $\Delta x_1$ and growing only with the logarithm of the distance (one light year in
$1.5\times10^{-10}$ s for $H = 4\times10^{-13}$ GeV). Causality itself is not protected by the time $x_4$: with four time-like directions
the eight-dimensional metric has closed time-like curves through every point (circles in the plane of $x_4$ and an extra time), and $x_4$ is
a time function only on the section of fixed extra times (SL4). Status: DERIVED.

$$
\begin{aligned}
&\lvert c_{\mathrm{e}} - 1\rvert \simeq \Big(\frac{g_{\mathrm{P}}\,\omega_{\mathrm{b}}^2}{16\pi^2}\Big)^2\big(c_{\mathrm{b}}^2 - 1\big),\\
&c_{\mathrm{e}} - 1 < 5\times10^{-21}\ \Rightarrow\ \frac{q_{\mathrm{b}}}{H} > 9.7\times10^{13},\qquad
1 - c_{\mathrm{e}} < 5.6\times10^{-20}\ \Rightarrow\ \frac{q_{\mathrm{b}}}{H} > 8.7\times10^{12}\qquad\big(\omega_{\mathrm{b}} = 1.5\ \text{TeV}\big)
\end{aligned} \tag{A-12}
$$
<!-- symbols: ce, gP, omegab, pi, cb, qb, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (A-12).**

- $c_{\mathrm{e}}$: The maximal speed of the electron, in units of the speed of light. Unit: dimensionless. Value: $c_{\mathrm{e}} - 1 < 5\times10^{-21}$ (no vacuum Cherenkov radiation of the 5 PeV electrons of the 2010 flare of the Crab nebula) and $1 - c_{\mathrm{e}} < 5.6\times10^{-20}$ (synchrotron electrons with the Lorentz factor $3\times10^9$). Status: STANDARD.
- $g_{\mathrm{P}}$: The strength of one lepton portal of the particles $\chi$ (a coupling of the currents of $\chi$ and of a chiral lepton), fixed by the relic density: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 9g_{\mathrm{P}}^2\omega_{\mathrm{b}}^2/(2\pi)$ for one $\chi$ with one antiparticle and nine chiral lepton states. Unit: GeV$^{-2}$. Value: $g_{\mathrm{P}}\omega_{\mathrm{b}}^2 = 0.110$, 0.220 and 0.734 for $\omega_{\mathrm{b}} = 1.5$, 3 and 10 TeV. Status: ESTIMATE.
- $\omega_{\mathrm{b}}$: The energy of a state of dirac16complex bound to the fold at zero momentum: the four-dimensional mass of the particle $\chi$. Unit: GeV. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $c_{\mathrm{b}}$: The speed coefficient of the bound particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum their energy is $\omega^2 = \omega_{\mathrm{b}}^2 + c_{\mathrm{b}}^2\vec k^2$ (it is not a speed that the particles reach: at large momenta $\omega/\lvert\vec k\rvert$ tends to 1, the speed of light). Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex bound to the fold: its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.

<!-- end generated symbol list -->

What the Standard Model inherits. Through loops of the particles $\chi$ the lepton portals pass the Lorentz violation of $\chi$ to the
electron, with a sign that is not computed. With the portal strength that the relic density requires ($g_{\mathrm{P}}\omega_{\mathrm{b}}^2 = 0.110$, 0.220
and 0.734 for $\omega_{\mathrm{b}} = 1.5$, 3 and 10 TeV) the loop factor is $4.9\times10^{-7}$, $1.9\times10^{-6}$ and $2.2\times10^{-5}$. The bound on
electrons faster than light, $c_{\mathrm{e}} - 1 < 5\times10^{-21}$ (no vacuum Cherenkov radiation of the 5 PeV electrons of the flare of the Crab
nebula of 2010), requires $q_{\mathrm{b}}/H$ above $9.7\times10^{13}$, $3.9\times10^{14}$ and $4.3\times10^{15}$; the bound on slower electrons,
$1 - c_{\mathrm{e}} < 5.6\times10^{-20}$ (synchrotron electrons with the Lorentz factor $3\times10^9$), requires $8.7\times10^{12}$, $3.5\times10^{13}$ and
$3.9\times10^{14}$. Status: ESTIMATE (SL5).

The answer. Yes, ultrarelativistic particles $\chi$ are slightly superluminal unless their binding is tight, but the effect is bounded:
their speed coefficient is $c_{\mathrm{b}} = \sqrt{q_{\mathrm{b}}/(q_{\mathrm{b}} - H)}$ at small momenta, their group velocity exceeds that of light by less than
one per cent in the computed regimes, and their front velocity is that of light. The eight-dimensional spacetime has closed time-like curves
anyway, because it has four time-like directions; causality on the fold rests on the confinement of the Standard Model to the fold and on
fields without a momentum along the extra times. The binding must be very tight, $q_{\mathrm{b}}/H$ above about $10^{13}$ to $4\times10^{15}$, so that the
Standard Model does not inherit a measurable Lorentz violation; with the bound $q_{\mathrm{b}} \lesssim 0.03\,\omega_{\mathrm{b}}$ of direct detection this
places the scale of the bulk at $H \lesssim 5\times10^{-13}$ GeV for $\omega_{\mathrm{b}}$ of 1.5 TeV and lower for heavier $\chi$. With the corrected
weights the Friedmann equations of the fold are exact for every $H$, so the expansion sets no lower bound on $H$ (ESTIMATE). A small $H$
has a price in the early universe: for $H = 4.6\times10^{-13}$ GeV the expansion rate of the fold exceeds $H$ above the temperature 574 GeV,
and the pressure that holds the volume of the extra times grows like the fourth power of the expansion rate in units of $H$ (the
primordial era, below).

## The primordial era

With the author's original weights UM-3 took the author's vacuum, $a_4 = Hx_4$ with a constant $b_4$, as its primordial era, and used the
values of Planck 2018 as inputs. With the corrected weights the author's vacuum is no longer a solution:

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

It would need a bulk source with a negative energy density. On the branch of frozen extra times, instead, the bulk is a vacuum for every
expansion history and the fold obeys the Friedmann equations of general relativity exactly, so the primordial era of UM-3 is whatever the
fields of the fold make of it: an inflation of the fold, if the volume of the extra times can be held fixed. Status: DERIVED
(`um3_primordial.py`, PR0).

$$
\begin{aligned}
&\mathsf{U} = \mathsf{A}:\qquad 3a_4'^2 = 8\pi G_{\mathrm{N}}\,\rho_{\mathrm{inf}},\qquad q_{\mathrm{hold}} = -\rho_{\mathrm{inf}}\Big(1 + \frac{\mathsf{A}^2}{4}\Big),\qquad
 H_{\mathrm{inf}} < \pi M_{\mathrm{red}}\sqrt{\frac{r_{\mathrm{T}}A_{\mathrm{s}}}{2}} = 4.43\times10^{13}\ \text{GeV},\\
&\xi_{\mathrm{H}} = N_{\mathrm{e}}\sqrt{\frac{\lambda}{72\pi^2A_{\mathrm{s}}}} = 16195\ \text{or}\ 4502,\qquad
 n_{\mathrm{S}} = 1 - \frac{2}{N_{\mathrm{e}}} = 0.9636,\qquad r_{\mathrm{T}} = \frac{12}{N_{\mathrm{e}}^2} = 0.0040
\end{aligned} \tag{A-13}
$$
<!-- symbols: Usf, Asf, a4, prime, pi, GN, rhoinf, qhold, Hinf, Mred, rT, As, xiH, Ne, lamH, nS, Deltar, Rhat, rhob, kstar, mh -->
<!-- begin generated symbol list -->
**Symbols in (A-13).**

- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); larger than 1 whenever the expansion rate of the fold exceeds $H$; 1 at the author's vacuum, which is not a solution with the corrected weights. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{inf}}$: The vacuum energy density that drives an inflation of the fold: the potential energy of a field of the fold (four-dimensional normalisation), with the pressure $-\rho_{\mathrm{inf}}$ along ordinary space and along the extra times. Unit: GeV$^4$. Status: ASSUMED.
- $q_{\mathrm{hold}}$: The pressure along the extra times that the fold fluid adds to its tension to hold the volume of the extra times fixed (four-dimensional normalisation). Unit: GeV$^4$. Value: $-\Delta_{\mathrm{r}}$ today: $-0.793\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have the pressure $-\rho_{\mathrm{b}}$ along the extra times (ASSUMED), $-0.842\,\rho_{\mathrm{c}}^{(0)}$ if they have none, $-0.891\,\rho_{\mathrm{c}}^{(0)}$ for $+\rho_{\mathrm{b}}$. Status: DERIVED (the value), ASSUMED (that the fold fluid supplies it).
- $H_{\mathrm{inf}}$: The expansion rate of ordinary space during an inflationary era. Unit: GeV. Status: STANDARD.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $r_{\mathrm{T}}$: The ratio of the amplitudes of the primordial spectra of gravitational waves (tensor) and of curvature (scalar) at the pivot scale. Unit: dimensionless. Value: below 0.036 (BICEP/Keck 2021, 95 per cent). Status: STANDARD.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $\xi_{\mathrm{H}}$: The coupling of the Higgs doublet to the scalar curvature of the fold, the term $-\xi_{\mathrm{H}}\hat R\,\Phi^\dagger\Phi$ in the Lagrangian of the fold: an extension of UM-3, whose Higgs Lagrangian has no such term ($\xi_{\mathrm{H}} = 0$). Unit: dimensionless. Value: 0 in UM-3; about $1.6\times10^4$ if the Higgs field drove inflation (ESTIMATE, an extension of the action). Status: ESTIMATE (an extension of the action).
- $N_{\mathrm{e}}$: The number of e-foldings of inflation after the pivot scale left the horizon. Unit: dimensionless. Value: 55. Status: STANDARD.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.
- $\Delta_{\mathrm{r}}$: The mismatch of the radion condition: the sum over the matter of the fold of its pressure along the extra times and $(\rho - 3\mathcal{P})/2$ (zero for radiation). Unit: GeV$^4$. Value: today $0.793\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have the pressure $-\rho_{\mathrm{b}}$ along the extra times (ASSUMED), $0.842\,\rho_{\mathrm{c}}^{(0)}$ if they have none, $0.891\,\rho_{\mathrm{c}}^{(0)}$ for $+\rho_{\mathrm{b}}$. Status: DERIVED (the condition and the values for each choice), ASSUMED (the pressure of the baryons along the extra times).
- $\hat R$: The scalar curvature of the metric $\hat h_{\mu\nu}$ of the fold. Unit: 1/length$^2$. Status: STANDARD.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $k_*$: The pivot wave number of the primordial spectrum. Unit: GeV (1/length). Value: 0.05 Mpc$^{-1}$. Status: STANDARD.
- $m_h$: The mass of the Higgs boson. Unit: GeV. Value: 125.25 GeV (Particle Data Group 2022). Status: STANDARD.

<!-- end generated symbol list -->

The inflation of the fold. A vacuum energy $\rho_{\mathrm{inf}}$ of a field of the fold, on the branch of frozen extra times ($\mathsf{U} = \mathsf{A}$,
with $\mathsf{A} = a_4'/H$ and $\mathsf{U} = b_4'/(Hb_4)$), expands ordinary space exactly as in general relativity (the first expression), provided
the fold fluid adds the pressure $q_{\mathrm{hold}}$ along the extra times that holds their volume fixed. Such an era makes the spectrum of
four-dimensional inflation: a slowly rolling field gives the observed nearly scale-invariant spectrum ($n_{\mathrm{S}} - 1 = -0.0351$, Planck 2018),
and the bound on primordial gravitational waves, $r_{\mathrm{T}} < 0.032$ (95 per cent; Planck PR4 with BICEP/Keck 2018 and BAO, M. Tristram et al.,
Phys. Rev. D 105 (2022) 083524), with the measured amplitude $A_{\mathrm{s}} = 2.1\times10^{-9}$, limits its expansion rate $H_{\mathrm{inf}}$ by the third
expression (PR4). The holding pressure of the first line is about $\mathsf{A}^4/8$ times the tension of the fold, with $\mathsf{A} = H_{\mathrm{inf}}/H$:
for an inflation at the largest allowed rate and $H$ at most $4.6\times10^{-13}$ GeV (the estimate of the maximal speed of the electron,
above) $\mathsf{A} \ge 9.6\times10^{25}$, and the fold fluid must add at least $2\times10^{51}$ times the vacuum energy of inflation, $10^{103}$ times
its own tension. What could supply such a pressure is OPEN, and with it whether the fold can inflate. With a free volume the extra times
would inflate together with ordinary space, and Newton's constant, the squares of the gauge and Yukawa couplings and the quartic Higgs
coupling of the fold would fall like $\mathrm{e}^{-3N}$ over $N$ e-foldings ($6.7\times10^{-79}$ after 60): the volume must be held fixed during
inflation as well (PR6). Since the fold has its own Einstein-Hilbert term, the Higgs field could be the inflaton if the action had a
large coupling $\xi_{\mathrm{H}}$ of the Higgs doublet to the curvature of the fold, which UM-3 does not contain (its Higgs Lagrangian has
none; an extension): with it (the second line, for $N_{\mathrm{e}} = 55$ e-foldings and the quartic coupling $\lambda = 0.1294$ or 0.01 at the scale
of inflation) it gives $n_{\mathrm{S}} = 0.9636$ and $r_{\mathrm{T}} = 0.0040$, 0.3 standard deviations below Planck 2018 ($0.9649 \pm 0.0042$) and 3.5 below
the combination of ACT DR6 with Planck, CMB lensing and DESI ($0.974 \pm 0.003$); whether Higgs inflation stays unitary above
$M_{\mathrm{red}}/\xi_{\mathrm{H}}$ is debated (PR5). Status: DERIVED (PR4, PR6), OPEN (the holding pressure), ESTIMATE (Higgs inflation, an
extension, PR5), STANDARD (the measurements).

$$
\frac{1}{16\pi G_{\mathrm{ind}}} = \frac{N_{\mathrm{ind}}\,\Lambda_{\mathrm{c}}^2}{192\pi^2},\qquad
N_{\mathrm{ind}} = \sum_{\text{real scalars}}\big(1 - 6\xi\big) + N_{\mathrm{Weyl}} - 4N_{\mathrm{gauge}} = 4\big(1 - 6\xi_{\mathrm{H}}\big) \tag{FE-64}
$$
<!-- symbols: pi, Gind, Nind, Lambdac, xinm, NWeyl, Ngauge, xiH -->
<!-- begin generated symbol list -->
**Symbols in (FE-64).**

- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{ind}}$: The Newton constant of the induced Einstein-Hilbert term of the fold, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Status: ESTIMATE.
- $N_{\mathrm{ind}}$: The weighted number of the fields of the fold that induce the Einstein-Hilbert term: each real scalar counts $1 - 6\xi$, each Weyl fermion 1, each gauge field $-4$ (with its ghost fields). Unit: dimensionless. Value: 4 for the Standard Model with three right-handed neutrinos, whose Higgs doublet has no curvature coupling in UM-3; $4(1 - 6\xi_{\mathrm{H}})$ with the curvature coupling $\xi_{\mathrm{H}}$ of an extension. Status: DERIVED.
- $\Lambda_{\mathrm{c}}$: The cutoff of the proper-time integral of the one-loop effective action of the fields of the fold: the highest energy of the quantum fluctuations that induce gravity. Unit: GeV. Value: $\sqrt{24}\,\pi M_{\mathrm{red}} = 3.748\times10^{19}$ GeV $= 3.07M_{\mathrm{Pl}}$ if the induced term alone gave the measured Newton constant at $\xi_{\mathrm{H}} = 0$. Status: ESTIMATE.
- $\xi$: The coupling of a real scalar field to the scalar curvature $\hat R$ of the fold: the term $-\frac12\xi\hat R$ times the square of the field in its Lagrangian ($\xi = 1/6$ is the conformal coupling). Unit: dimensionless. Status: STANDARD.
- $N_{\mathrm{Weyl}}$: The number of Weyl (two-component) fermion fields of the fold. Unit: dimensionless. Value: 48 (three generations of quarks and leptons with three right-handed neutrinos). Status: STANDARD.
- $N_{\mathrm{gauge}}$: The number of gauge fields of the fold. Unit: dimensionless. Value: 12 (eight gluons, three $W$, one $B$). Status: STANDARD.
- $\xi_{\mathrm{H}}$: The coupling of the Higgs doublet to the scalar curvature of the fold, the term $-\xi_{\mathrm{H}}\hat R\,\Phi^\dagger\Phi$ in the Lagrangian of the fold: an extension of UM-3, whose Higgs Lagrangian has no such term ($\xi_{\mathrm{H}} = 0$). Unit: dimensionless. Value: 0 in UM-3; about $1.6\times10^4$ if the Higgs field drove inflation (ESTIMATE, an extension of the action). Status: ESTIMATE (an extension of the action).

<!-- end generated symbol list -->

The induced gravity of the fold. The Einstein-Hilbert term that the fields of the fold induce at one loop has the right sign only for
$\xi_{\mathrm{H}} < 1/6$; with the author's original weights UM-3 needed it to carry nearly all of four-dimensional gravity, which excluded Higgs
inflation. With the corrected weights the fold has its own Einstein-Hilbert term, the induced term is optional, and the bound
$\xi_{\mathrm{H}} < 1/6$ no longer applies. The action of UM-3 itself has no such coupling ($\xi_{\mathrm{H}} = 0$); a coupling $\xi_{\mathrm{H}} \ne 0$
would be an extension. Status: ESTIMATE (`um3_foldsources.py`, F5).

$$
\begin{aligned}
&\frac{\big(\sqrt{-\hat h}\,\mathcal{Z}\,\phi_k'\big)'}{\sqrt{-\hat h}\,\mathcal{Z}} + k^2\mathrm{e}^{-2a_4}\phi_k = 0,\qquad
 a_4 = Hx_4:\ \ \sqrt{-\hat h}\,\mathcal{Z} = \frac{V_{\mathrm{t}}b_4^3}{V_*},\qquad
 \phi_k = \sqrt{\frac{\pi}{4H}}\,\mathrm{H}^{(1)}_0\big(-k\tau_{\mathrm{c}}\big),\qquad -\tau_{\mathrm{c}} = \frac{\mathrm{e}^{-Hx_4}}{H},\\
&\lvert\phi_k\rvert^2 \to \frac{\pi}{4H}\Big[1 + \frac{4}{\pi^2}\Big(\ln\frac{-k\tau_{\mathrm{c}}}{2} + \gamma_{\mathrm{E}}\Big)^2\Big],\qquad
 n_{\mathrm{S}} - 1 = \frac{\mathrm{d}\ln\big(k^3\lvert\phi_k\rvert^2\big)}{\mathrm{d}\ln k} \ge 3 - \frac{2}{\pi}
\end{aligned} \tag{A-14}
$$
<!-- symbols: hhat, Zfold, phik, prime, kwave, euler, a4, Hconst, x4, Vt, b4, Vstar, pi, Hankel, tauc, gammaE, nS, diff -->
<!-- begin generated symbol list -->
**Symbols in (A-14).**

- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\phi_k$: The amplitude of a Fourier mode of a massless scalar field of the fold: of comoving wave number $k$ (the label $k$) along ordinary space, and, where it is said, with a momentum $\vec\kappa$ along the extra times. Unit: GeV. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $k$: The comoving wave number of a Fourier mode of the perturbations, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings $\alpha_{(p)} = w_{(p)}H^{2-2p}$ and the cosmological constant $\Lambda = -7H^2$ (the author's original value $-10H^2$ was corrected on 2026-10-25); in UM-3 a free parameter. Unit: GeV (1/length). Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{H}^{(1)}_0$: The Hankel function of the first kind of order zero, $\mathrm{H}^{(1)}_0$: the Bessel function of the first kind of order zero plus $\mathrm{i}$ times the Bessel function of the second kind of order zero. Unit: dimensionless. Status: STANDARD.
- $\tau_{\mathrm{c}}$: The conformal time of the fold, $\mathrm{d}\tau_{\mathrm{c}} = \mathrm{e}^{-a_4}\mathrm{d}x_4$ (the time divided by the scale factor $\mathrm{e}^{a_4}$ of the fold); a dot on a quantity of the cosmological perturbations is $\mathrm{d}/\mathrm{d}\tau_{\mathrm{c}}$. Unit: length (= time). Status: STANDARD.
- $\gamma_{\mathrm{E}}$: The Euler-Mascheroni constant. Unit: dimensionless. Value: 0.5772157. Status: STANDARD.
- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.

<!-- end generated symbol list -->

The record of the author's vacuum. A massless scalar field of the fold (four-dimensional normalisation) has the mode equation of the first
expression, with the volume factor $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$ of ordinary space and the factor $\mathcal{Z}$ of the size of the extra times.
In the author's vacuum ordinary space grew as $\mathrm{e}^{3Hx_4}$ while the extra times shrank as $\mathrm{e}^{-3Hx_4}$: their product was constant,
and the fields of the fold felt no Hubble friction (PR1). The mode equation was then Bessel's equation of order zero in $-k\tau_{\mathrm{c}}$, with
the conformal time $\tau_{\mathrm{c}}$, solved with the canonical normalisation by the Hankel function of the second expression; at late times its
square grows only logarithmically, so the spectrum $k^3\lvert\phi_k\rvert^2/(2\pi^2)$ grows like $k^3$ times a logarithm: its index is never below
$3 - 2/\pi = 2.363$ (2.545 fitted over the computed scales), against the observed $-0.0351$ (PR2), and the squares of the gauge and Yukawa
couplings and the quartic Higgs coupling of the fold grew as $\mathrm{e}^{3Hx_4}$ (PR3). Status: DERIVED (records).

The answer. The author's vacuum is not a solution with the corrected weights, and as a record it could not have made the observed
fluctuations. The primordial era of UM-3 can be an inflation of the fold with the volume of the extra times held fixed, which is the
inflation of four-dimensional general relativity, but only if the fold fluid supplies a holding pressure of about $\mathsf{A}^4/8$ times
its tension ($\mathsf{A} = H_{\mathrm{inf}}/H$), at least $10^{103}$ times for an inflation at the largest allowed rate if
$H \lesssim 4.6\times10^{-13}$ GeV; what could supply it is OPEN. UM-3 does not specify the inflaton, and the Higgs field could be it only with a curvature
coupling that the action does not contain (ESTIMATE, an extension). What precedes inflation and the reheating after it are not
computed, and the Planck values remain inputs of the cosmological calculation (OPEN).

## The lightest neutrino mass and the Dirac phase

$$
\begin{aligned}
&\big(\lvert U_{\mathrm{e}i}\rvert^2\big)_{i = 1, 2, 3} = \big(\cos^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{13}\big),\\
&m_2 = \sqrt{m_1^2 + \Delta m^2_{21}},\qquad m_3 = \sqrt{m_1^2 + \Delta m^2_{31}},\qquad
 m_1 < 23\ \text{meV}\ \ (\text{95 per cent}),\qquad
 m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2
\end{aligned} \tag{A-15}
$$
<!-- symbols: Uei, ii, thetaij, mferm, Delta, mmass, meff, Pmns, vloc -->
<!-- begin generated symbol list -->
**Symbols in (A-15).**

- $U_{\mathrm{e}i}$: The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$. Unit: dimensionless. Value: $\lvert U_{\mathrm{e}i}\rvert^2 = 0.682$, 0.296 and 0.022 for $i = 1, 2, 3$ (NuFIT 5.2, the fit without the Super-Kamiokande atmospheric data: the values of the record; NuFIT 6.0 with them gives 0.677, 0.301 and 0.022). Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal); a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\theta_{12},\ \theta_{13},\ \theta_{23}$: The three mixing angles of $U_{\mathrm{PMNS}}$ (its fourth parameter is the Dirac phase, which does not enter the electron-flavour results of UM-3). Unit: dimensionless. Value: $33.40^\circ$, $8.54^\circ$, $49.14^\circ$ in the computations of UM-3 ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$: NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); $33.71^\circ$, $8.56^\circ$, $43.28^\circ$ in NuFIT 6.0 (2024, with the Super-Kamiokande atmospheric data; $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$). Status: STANDARD.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-3 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 23 meV by DESI DR2 with the CMB and NuFIT 6.0. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1. Unit: GeV. Status: STANDARD.
- $m_{\mathrm{eff}}$: The effective mass of the electron neutrino measured in the beta decay of tritium, $m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2$. Unit: eV. Value: below 0.45 eV (KATRIN 2025, 90 per cent). Status: STANDARD.
- $U_{\mathrm{PMNS}}$: The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; its entries $(U_{\mathrm{PMNS}})_{\alpha i}$ connect the flavour $\alpha$ with the mass state $i$. Unit: dimensionless. Value: $\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$). Status: STANDARD, ASSUMED (the phase).
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.

<!-- end generated symbol list -->

The Dirac phase $\delta_{\mathrm{CP}}$. The mixing matrix is three rotations by the angles $\theta_{23}$, $\theta_{13}$ and $\theta_{12}$, the phase attached
to the middle one, and its electron row (the first line of A-15) contains no phase. Every flavour result of UM-3 is a result for electron
neutrinos: the solar survival probabilities, the conversion in the envelope of a supernova (the matter potential acts on $\nu_e$ only, so the
phase can be moved into $\nu_\mu$ and $\nu_\tau$), and the capture of the cosmic neutrinos. Computed with the newer global fit NuFIT 6.0
(I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, I. Martinez-Soler, J. P. Pinheiro and T. Schwetz, JHEP 12 (2024) 216; with the
atmospheric data of Super-Kamiokande, $\delta_{\mathrm{CP}} = 212^\circ$ in the normal ordering), the envelope gives the same survival probability as
with $\delta_{\mathrm{CP}} = 0$ to $6\times10^{-14}$. The phase appears only in the appearance channels, which UM-3 does not compute (in vacuum at
295 km and 0.6 GeV, the baseline and the peak energy of T2K, $\nu_\mu \to \nu_e$ has the probability 0.0421, 0.0478 and 0.0541 for
$\delta_{\mathrm{CP}} = 0$, $212^\circ$ and $270^\circ$, $\bar\nu_\mu \to \bar\nu_e$ 0.0421, 0.0346 and 0.0291), and in the Jarlskog invariant of CP violation,
$-0.0178$ at $212^\circ$. Status: DERIVED (`um3_numass.py`, NM3).

The lightest mass $m_1$. DESI DR2 (the BAO) with the CMB, combined with NuFIT 6.0 (W. Elbers et al., arXiv:2503.14744; the
cosmological-constant model, 95 per cent), bounds the lightest mass to $m_1 < 23$ meV in the normal ordering (24 meV in the inverted one)
and the sum of the masses to 0.101 eV (normal) and 0.133 eV (inverted); the inverted ordering, whose smallest sum is 0.0989 eV, is
disfavoured (the probability of the normal ordering is 0.91) but not excluded. The bound 0.0642 eV on the sum that the same data give for
three equal masses is not a bound on $m_1$ (an earlier version of this document applied it to $m_1$). With $\Delta m^2_{21} = 7.49\times10^{-5}$
eV$^2$ and $\Delta m^2_{31} = 2.513\times10^{-3}$ eV$^2$ (the second line of A-15) the masses at $m_1 = 23$ meV are 23.00, 24.57 and 55.15 meV, and the
effective mass of tritium beta decay is 8.84 to 24.64 meV in this range, far below the limit 0.45 eV of KATRIN. Within the range $m_1$ changes
one result of UM-3, the capture rate of the cosmic neutrinos on 100 g of tritium,
$N_{\mathrm{T}}\bar\sigma_{\mathrm{T}}(n_\nu^{(0)}/2)\sum_i\lvert U_{\mathrm{e}i}\rvert^2(1 + \mathsf{s}_i)$ ($N_{\mathrm{T}}$ the number of tritium nuclei,
$\bar\sigma_{\mathrm{T}} = 3.834\times10^{-45}$ cm$^2$ the averaged capture cross-section, $n_\nu^{(0)}/2 = 56$ cm$^{-3}$ the density per mass state of
one helicity, $\mathsf{s}_i$ the mean speed of the state today): from 6.88 per year at $m_1 = 0$ to 4.15 per year at $m_1 = 23$ meV, as $\nu_1$
becomes slow (mean speed 0.023). Status: DERIVED (NM1, NM2, NM4), STANDARD (the bounds).

The answer. Setting the Dirac phase to zero was without consequence: it drops out of every result of UM-3. The lightest mass is not fixed
by any measurement; DESI DR2 with NuFIT 6.0 bounds it below 23 meV, and within this range it lowers the capture rate of the cosmic neutrinos
by up to 40 per cent. The records computed with NuFIT 5.2 differ from NuFIT 6.0 by at most 1.5 per cent (NM5).

# What the author may have left out

The author asked to be told if something important was missing from his specification. UM-3 had to add the following, and the
analysis found the following problems.

| item | why it is needed or what it means | where it stands |
| ------ | ------ | ------ |
| right-handed quark singlets and the Yukawa couplings | the quark doublets alone have no masses and the hypercharges cancel the gauge anomalies only with the singlets | added (a default of UM-3, proposed in the notification of 17:20, which the author did not answer: ASSUMED) |
| three right-handed neutrinos | Dirac neutrino masses and the mixing that flavour conversion needs; the anomalies still cancel | added (accepted by the author, 17:32); they must never thermalise |
| the place of the Standard Model | in the bulk, every species would move with its own limiting speed and three neutrino profiles would oscillate wrongly; on the fold all share one light cone | the Standard Model lives on the fold (ASSUMED, motivated by the DERIVED limiting speeds) |
| the Lovelock weights and the cosmological constant | with the author's original weights $1, 1/32, 1/1152$ and $\Lambda = -10H^2$ gravitons in the bulk were faster than light (local cone $\sqrt5$, long-wavelength zero mode of the bulk alone 2.74 times the speed of light, a deduction of Claude) and the static bulk needed a medium; only the weights $1, 1/20, 1/360$ give a graviton of the fold at the speed of light without a faster graviton in the static bulk, and with them the static block is a vacuum for $\Lambda = -7H^2$ (the Born-Infeld gravity of eight dimensions); no weights give gravitons at the speed of light both in the bulk and on the fold, because the time of the author's metric is not warped | corrected at the author's order of 2026-10-25 (ASSUMED the criterion, because the order cannot be met in full; DERIVED the unique values that meet it); the order "Gravitons must travel at c" is met for the graviton of the fold at linear order and cannot be met in full with the author's metric: changing the metric is the author's decision |
| a thin source at the fold | the kink of the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ requires one (the fold fluid); at the static block it is a pure tension $\lambda_{\mathrm{F}} = 6H^2/(8\pi G_{\mathrm{N}})$, like the brane of Randall and Sundrum; its excess over $\lambda_{\mathrm{F}}$ is the dark energy, a fine tuning as severe as the cosmological-constant problem | ASSUMED (its values DERIVED); OPEN (the fine tuning) |
| the gravity of the fold | with the corrected weights the Gauss-Bonnet and cubic terms give the fold its own Einstein-Hilbert term: the fold obeys the Friedmann equations of general relativity exactly and its four-dimensional gravitational waves travel at the speed of light at every wavelength at linear order (GW170817 satisfied for every $H$); the propagation of the polarisation along the extra times, a scalar of the four-dimensional world, on an expanding fold is OPEN (it couples to the bulk, generically not luminal); an induced term of its fields is optional (with the original weights it had to provide all but $1.3\times10^{-13}$ of four-dimensional gravity) | DERIVED; OPEN (the coupling to the degenerate bulk beyond linear order) |
| the stabiliser of the bulk | with the original weights the static bulk needed a medium with $\kappa\rho_{\mathrm{s}} = -H^2/16$ and the pressure $5\rho_{\mathrm{s}}$, found and named by Claude (Anthropic) on 2026-10-24, which violated the null energy condition; with the corrected weights it vanishes | a record; not part of UM-3 |
| the volume of the extra times | it is not frozen by itself: dust and vacuum energy drive it, and a free volume would change Newton's constant 6800 times faster than lunar laser ranging allows (and $G_{\mathrm{N}}$ at nucleosynthesis by the factor 15.8); the fold fluid must add the pressure $q_{\mathrm{hold}} = -0.793\rho_{\mathrm{c}}^{(0)}$ along the extra times today (with the assumed pressure $-\rho_{\mathrm{b}}$ of the baryons along them; $-0.842$ or $-0.891\rho_{\mathrm{c}}^{(0)}$ with 0 or $+\rho_{\mathrm{b}}$), and about $\mathsf{A}^4/8$ times the tension of the fold during an inflation at the rate $H_{\mathrm{inf}} = \mathsf{A}H$ (at least $10^{103}$ at the largest rate that the tensor bound allows if $H \lesssim 4.6\times10^{-13}$ GeV) | ASSUMED (the holding pressure and the pressure of the baryons); OPEN (its origin, a potential for the volume, and its size in the early universe) |
| the strongly coupled bulk | the static block is a degenerate vacuum: the bulk equations have no linear part for any perturbation of the metric, static deformations grow like $\mathrm{e}^{3H\lvert\sigma\rvert}$, on the expanding branch no component of the metric has a time-kinetic term, and the response of the bulk to sources that depend on $\sigma$ (the bound states $\chi$ among them) is not computed; the bulk metric has no perturbative quantum theory there | DERIVED (the degeneracy); OPEN (the response) |
| frozen extra times in the late universe (the size $\mathrm{e}^{-a_4}b_4$ of the extra times constant) | otherwise the couplings of the Standard Model change: Newton's constant, the squares of the gauge and Yukawa couplings and the quartic Higgs coupling of the fold are divided by the volume factor of the extra times | required, and held by the fold fluid |
| a gauge field for the ad hoc Higgs vacuum | the literal ad hoc vacuum carries an isospin charge that the Gauss law forbids; with the pure-gauge $W^2_{x_4}$ it is a rotated vacuum with one radial residual, and it must decay before nucleosynthesis | DERIVED |
| the Krein norm of dirac16complex | the signature $(4,4)$ of the author's matrices makes the charge indefinite; quantised, it has ghosts that no vacuum removes; the vacuum is stable, the classical stability of the gas is not decided; chiral couplings at the fold produce ghosts | DERIVED; OPEN: the stability of the gas, a unitary coupling (chirality-blind at the fold is necessary, not shown sufficient) |
| the extra times | fields that depend on them are tachyonic; the restriction to fields without a momentum along them is consistent but unstable; compact extra times do not help (the $n$-th harmonic grows $n$ times faster than the first, and a compact time-like direction is a closed time-like curve) | ASSUMED (no dependence); OPEN: a gauge principle that removes that momentum |
| Lorentz violation and causality | ultrarelativistic particles $\chi$ move faster than light on the fold unless $q_{\mathrm{b}} \gg H$ (group velocity up to 1.0046, front velocity that of light), signals through the bulk outrun light on the fold, and the four time-like directions allow closed time-like curves; loops pass the violation to the electron | a condition on the parameters: $q_{\mathrm{b}}/H$ above about $10^{13}$ to $4\times10^{15}$ (ESTIMATE) |
| direct detection | the Higgs portal fixed by the binding and the quark portals are strongly constrained | a weakly bound, leptophilic $\chi$ above about 1.5 TeV |
| the dark energy | a vacuum energy with $w = -1$; DESI DR2 prefers an evolving one | OPEN (tension at 2.3 to 3.1 standard deviations) |
| the primordial era | the author's vacuum is not a solution with the corrected weights (as a record it gave a spectrum with $n_{\mathrm{S}} - 1 \ge 2.36$); the primordial era can be an inflation of the fold with the volume of the extra times held fixed, below $4.43\times10^{13}$ GeV, if the fold fluid supplies a holding pressure of about $\mathsf{A}^4/8$ times its tension (at least $10^{103}$ at that rate if $H \lesssim 4.6\times10^{-13}$ GeV); the Higgs field could drive it only with a curvature coupling that the action does not contain | DERIVED; ESTIMATE (Higgs inflation, an extension); OPEN (the holding pressure; the inflaton is not specified; Planck inputs) |
| the lightest neutrino mass and the Dirac phase | not fixed by the specification; the phase drops out of every result of UM-3; DESI DR2 with NuFIT 6.0 bounds $m_1 < 23$ meV, which changes only the capture rate of the cosmic neutrinos | DERIVED (the phase is irrelevant); ASSUMED: $m_1 = 0$ within the bound |

# Further symbols

<!-- further symbols: GF, Omega, betaD, epsLC, g2, g3, grho, omegaSC, Aadhoc, GammaK, NT, Neff, TSM, Tany, Wwarp, deltaCP, nnu, nugen, rhos, sigmabarT, sstate, vA, Lfold, TH, Tf, Tgauge, inn, epsb, awarp, bwarp, nwarp, hHiggs -->
<!-- begin generated symbol list -->
**Further symbols.** These symbols appear in the definitions of the symbols listed after the equations of this document.

- $G_{\mathrm{F}}$: The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in the equations of the neutrino flavours it stands for the local Fermi constant of the ad hoc vacuum. Unit: GeV$^{-2}$. Value: $1.1664\times10^{-5}$ GeV$^{-2}$. Status: STANDARD.
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $\beta$: The matrix of the four-dimensional Dirac adjoint, $\beta = \hat\gamma^{(4)}$ (Hermitian, $\beta^2 = \mathbf{1}$). Unit: dimensionless. Status: STANDARD.
- $\epsilon^{IJK}$: The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$. Unit: dimensionless. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling (usually $g$). Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling (the strong coupling $g_s$). Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($\alpha_s = 0.1180$). Status: STANDARD.
- $g_\rho$: The effective number of relativistic degrees of freedom of the energy density. Unit: dimensionless. Value: 106.75 in the Standard Model above the electroweak scale. Status: STANDARD.
- $\varpi_{Mab}$: The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$. Unit: 1/length. Status: STANDARD.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $\Gamma_{\mathrm{K}}$: The growth rate of a perturbation of the gas of particles $\chi$ when the Krein-positive partner of its occupied level collides with it (a pair of complex frequencies $\omega \pm \mathrm{i}\Gamma_{\mathrm{K}}$). Unit: $m_\Psi$. Status: DERIVED.
- $N_{\mathrm{T}}$: The number of tritium nuclei of the target. Unit: dimensionless. Value: $2.0\times10^{25}$ for 100 g. Status: STANDARD.
- $N_{\mathrm{eff}}$: The effective number of neutrino species: the energy density of the relativistic particles other than photons in units of that of one neutrino species whose temperature is $(4/11)^{1/3}$ times that of the photons. Unit: dimensionless. Value: 3.044 (Standard Model); measured $2.99 \pm 0.17$ (Planck 2018). Status: STANDARD.
- $\mathcal{T}_{\mathrm{SM}}$: The energy-momentum tensor of the Standard Model on the fold, $\mathcal{T}_{\mathrm{H}} + \mathcal{T}_{\mathrm{gauge}} + \mathcal{T}_{\mathrm{f}}$. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{W}$: The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-3 the function of $\sigma$ that multiplies ordinary space and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold. Unit: dimensionless. Status: DERIVED.
- $\delta_{\mathrm{CP}}$: The Dirac phase of the mixing matrix $U_{\mathrm{PMNS}}$. Unit: degree. Value: $212^\circ$ (NuFIT 6.0, normal ordering); 0 in the computations of UM-3. Status: STANDARD.
- $n_\nu$: The number density of the cosmic neutrino background per flavour (neutrinos plus antineutrinos, one helicity each); $n_\nu^{(0)}$ its value today. Unit: GeV$^3$. Value: 112 cm$^{-3}$ today. Status: STANDARD.
- $\nu_\alpha,\ \nu_i$: A neutrino field: $\nu_\alpha$ the flavour states (the index $\alpha$ runs over the electron, muon and tau flavours), $\nu_i$ the mass states ($i = 1, 2, 3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\rho_{\mathrm{s}}$: The energy density of the stabiliser of the bulk with the author's original weights; with frozen extra times it was the energy density of the bulk at which ordinary space stands still. Unit: GeV$^8$. Value: $\kappa\rho_{\mathrm{s}} = -H^2/16$ with the author's original weights; 0 with the corrected weights. Status: DERIVED.
- $\bar\sigma_{\mathrm{T}}$: The averaged cross-section of the capture of an electron neutrino on tritium: a tritium nucleus captures left-handed electron neutrinos of mean speed $\mathsf{s}$ and number density $n$ at the rate $\bar\sigma_{\mathrm{T}}(1 + \mathsf{s})\,c\,n$ ($c$ the speed of light, 1 in the formulas; Long, Lunardini and Sabancilar). Unit: cm$^2$. Value: $3.834\times10^{-45}$ cm$^2$. Status: STANDARD.
- $\mathsf{s}_i$: The mean speed of the neutrino mass state $i$ today, averaged over its momentum distribution (0 for a state at rest, 1 for a massless one). Unit: dimensionless. Value: 1, 0.061 and 0.011 for the mass states 1, 2 and 3 with $m_1 = 0$; 0.023 for the state 1 with $m_1 = 23$ meV. Status: STANDARD.
- $v_{\mathcal{A}}$: The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc, $\mathrm{e}^{-2a_{40}x_4}$ (written Exp[-2 a40 x4] in his notebook), has $v_{\mathcal{A}} = 1$ in the units of his notebook. Unit: GeV. Value: 1 in the units of the author's notebook; UM-3 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$). Status: AUTHOR (the form), ASSUMED (a free amplitude).
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{H}}$: The energy-momentum tensor of the Higgs doublet (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{f}}$: The energy-momentum tensor of the quarks and leptons. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{T}_{\mathrm{gauge}}$: The energy-momentum tensor of the gauge fields. Unit: GeV$^4$. Status: STANDARD.
- $n$: The order $n = 1, 2, \dots$ of a term of the power series of the metric (also the exponent of the bookkeeping parameter $\epsilon_{\mathrm{b}}$); $\mathfrak{a}_n$, $\mathfrak{b}_n$, $\mathfrak{n}_n$ are the terms of order $n$. Status: STANDARD.
- $\epsilon_{\mathrm{b}}$: The bookkeeping parameter of the deformations of the metric along $\sigma$ that sources depending on $\sigma$ require (their amplitude relative to the order-0 metric of the author). Unit: dimensionless. Status: STANDARD.
- $\mathfrak{a},\ \mathfrak{a}_1$: The logarithm of the scale factor of ordinary space in the general warped metric FE-34, a function of $\sigma$ and $x_4$; for the author’s metric $\mathfrak{a} = a_4 - H\lvert\sigma\rvert$; $\mathfrak{a}_n$ its term of order $n$ in the power series FE-35 ($\mathfrak{a}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{b},\ \mathfrak{b}_1$: The logarithm of the scale factor of the extra times in the general warped metric FE-34; for the author’s metric $\mathfrak{b} = \ln b_4 - a_4 - H\lvert\sigma\rvert$; $\mathfrak{b}_n$ its term of order $n$ ($\mathfrak{b}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $\mathfrak{n},\ \mathfrak{n}_1$: The logarithm of the lapse in the general warped metric FE-34 ($g_{x_4x_4} = -\mathrm{e}^{2\mathfrak{n}}$); for the author’s metric $\mathfrak{n} = 0$; $\mathfrak{n}_n$ its term of order $n$ ($\mathfrak{n}_1$ the first-order term). Unit: dimensionless. Status: DERIVED.
- $h$: The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$. Unit: GeV. Value: $m_h = 125.25$ GeV. Status: STANDARD.

<!-- end generated symbol list -->
