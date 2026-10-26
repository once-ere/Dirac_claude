---
title: "UM-4 propagation"
subtitle: 'The answer to the author''s order of 2026-10-25, 13:15 PDT: the metric in which the time is warped like every other direction of the fold, photons and gravitons at the speed of light in the bulk, the photon a transverse wave of spin 1, the gravitational wave a wave of spin 2 with its plus and cross polarisations'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Formulated and verified by Claude (Anthropic)"
  - "Propagation in UM-4, 2026-10-25"
  - "Repository once-ere/Dirac_claude, folder universe_model_4"
---

# The fold: definition and examples

<!-- begin fold definition -->
**Definition.** The *fold* is the seven-dimensional surface of the author's eight-dimensional spacetime on which the
cosine of the angle $z = 6Hx_0$ of the hidden direction vanishes:

$$
\mathcal{F} = \big\{X = (x_0, x_1, \dots, x_7):\ \cos(6Hx_0) = 0\big\},\qquad
\text{in one period } 0 < z < \pi\text{ of the metric: } z = \frac{\pi}{2},\quad x_0 = \frac{\pi}{12H} \tag{FD-1}
$$
<!-- symbols: foldF, Xcoord, x0, x1, x7, Hconst, zvar, pi, Lambda, LambdaN, wL -->
<!-- begin generated symbol list -->
**Symbols in (FD-1).**

- $\mathcal{F}$: The fold: the seven-dimensional surface $\cos(6Hx_0) = 0$ of the eight-dimensional spacetime (FD-1), in one period $0 < z < \pi$ the surface $z = \pi/2$, $x_0 = \pi/(12H)$, where $\sigma = 0$; $\vert_{\mathcal{F}}$ means restricted to the fold. Status: DERIVED.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant of UM-4, $\Lambda = -21H^2$: the value for which the static block is a vacuum of Einstein gravity (its Einstein tensor is $21H^2$ in every direction). The author writes the pure number $\Lambda_{\mathrm{N}}$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$, so that $\Lambda = -\Lambda_{\mathrm{N}}H^2$. Unit: GeV$^2$. Value: $-21H^2$; the author's original $-10H^2$; UM-3: $-7H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $\Lambda_{\mathrm{N}}$: The author's pure number in the vacuum equations of his notebook, $\Lambda = -\Lambda_{\mathrm{N}}H^2$: his original value 10; 21 in UM-4 (Einstein gravity), 7 in UM-3. Unit: dimensionless. Value: 21 (the author's original 10). Status: AUTHOR.
- $w_{(p)}$: The Lovelock weights of the author's Einstein-Lovelock action, $w_{(1)} = 1$ and $w_{(2)}$, $w_{(3)}$ of the Gauss-Bonnet and the cubic densities. UM-4 sets $w_{(2)} = w_{(3)} = 0$ (Einstein gravity): the only weights for which gravitons propagate on the light cone on every background, not only around the static block. The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) keep the gravitons on the light cone only around the static block (with $\Lambda = -161H^2/16$); UM-3 used $(1, 1/20, 1/360)$. Unit: dimensionless. Value: $(1, 0, 0)$ in UM-4; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), DERIVED (the values that the order of 2026-10-25 selects).

<!-- end generated symbol list -->

$X = \{x_0, \dots, x_7\}$ are the author's coordinates: $x_0$ the hidden space-like direction, $x_1, x_2, x_3$ ordinary space,
$x_4$ the time, $x_5, x_6, x_7$ the three extra times; $H$ is the author's constant (an inverse length). The metric of UM-4
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
$\cot = \cos/\sin$ the trigonometric functions, $\sinh$, $\cosh$, $\tanh = \sinh/\cosh$ and $\coth = \cosh/\sinh$ the hyperbolic
functions, $\lvert y\rvert$ the absolute value, $\max$ and $\min$ the larger and the smaller of their arguments; $\det$,
$\mathrm{tr}$ and ${}^T$ are the determinant, the trace and the transpose of a square matrix, and $\mathbf{1}_4$, $\mathbf{1}_8$ and
$\mathbf{1}_{16}$ the identity matrices of 4, 8 and 16 rows; $f(0^+)$ and $f(0^-)$ are the limits of $f(\sigma)$ as $\sigma$
approaches 0 from above and from below.

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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.

<!-- end generated symbol list -->

(the fold is $\sigma = 0$; the half-period $0 < z < \pi/2$ is $\sigma < 0$, the half-period $\pi/2 < z < \pi$ is $\sigma > 0$; the
two ends of the period, the tips $z \to 0$ and $z \to \pi$, lie at $\sigma \to -\infty$ and $\sigma \to +\infty$), the metric of UM-4 is

$$
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{d}x_4^2 - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big] \tag{FD-4}
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
which multiplies the squared steps of all seven directions of the fold (ordinary space, the time and the extra times), is the
warp factor of the metric (its square root $\mathrm{e}^{-H\lvert\sigma\rvert}$ multiplies the lengths). The time $x_4$ is warped
like the other directions (the author's order of 2026-10-25, 13:15 PDT; in UM-3 it was not), so that every surface
$\sigma = \text{const}$ has the light cone of the fold. Four properties make the surface $\sigma = 0$ a fold, and together they
single it out within the period:

1. *It is a mirror.* The reflection $\sigma \to -\sigma$ (that is $z \to \pi - z$, or $x_0 \to \pi/(6H) - x_0$) maps the metric
   to itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
   period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are joined
   along the crease.
2. *The warp factor is largest on it.* The warp factor $(\sin^2z)^{1/6} = \mathrm{e}^{-2H\lvert\sigma\rvert}$ equals 1 on the
   fold and decreases on both sides.
3. *The metric has a kink on it.* The metric is continuous across the fold, but its first derivative along $\sigma$ jumps.
   The extrinsic curvature of the surfaces $\sigma = \text{const}$ changes sign across the fold,

$$
K^a{}_b = \frac12\,g^{ac}\,\partial_\sigma g_{cb} = -H\,\mathrm{sgn}(\sigma)\,\delta^a{}_b\quad(\text{all seven directions of the fold}) \tag{FD-5}
$$
<!-- symbols: Kextr, ia, ib, ic, metric, partial, isigma, sigma, Hconst, sgn, delta, eta, ghat7, diag, xfour -->
<!-- begin generated symbol list -->
**Symbols in (FD-5).**

- $K^a{}_b$: The extrinsic curvature of a surface of constant $\sigma$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along all seven directions of the fold for the author's form of the metric of UM-4; $K = K^c{}_c$ its trace. Unit: GeV (1/length). Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $c$: A frame index (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\hat g_{ab}$: The metric of the seven-dimensional fold (FD-2) in its coordinates $x_1, \dots, x_7$ (or in its frame), $\hat g^{ab}$ its inverse; $\hat h_{\mu\nu}$ is its part along the four observable directions. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.

<!-- end generated symbol list -->

   ($a, b$ frame indices along the fold); it jumps by $-2H$ in every direction of the fold. The field equations of gravity of
   UM-4, $\mathcal{E}_{(1)}{}^M{}_N + \Lambda\delta^M_N = \kappa\mathcal{T}^M{}_N$ (Einstein gravity: the author's Einstein-Lovelock
   equations with the weights of the Gauss-Bonnet and cubic terms set to zero; $\mathcal{E}_{(1)}$ the Einstein tensor,
   $\Lambda = -21H^2$ the cosmological constant, $\kappa = 8\pi G_8$ the gravitational coupling of eight dimensions,
   $\mathcal{T}^M{}_N$ the energy-momentum tensor, $\delta^M_N$ the Kronecker delta), are linear in the second $\sigma$-derivatives
   of the metric, so the jump puts a Dirac delta function $\delta_{\mathrm{D}}(\sigma)$ into them: the metric solves them only if
   the fold carries a thin source $\mathcal{S}^a{}_b$, an energy-momentum tensor concentrated on $\sigma = 0$, given by the
   integral of the equations across the fold (the junction condition of Israel),

$$
\kappa\,\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b
 = -\Big(\big(K^a{}_b\big\vert_{0^+} - K^a{}_b\big\vert_{0^-}\big) - \delta^a{}_b\big(K\big\vert_{0^+} - K\big\vert_{0^-}\big)\Big) \tag{FD-11}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, diff, sigma, LovE, ip, Kextr, delta, G8, Riemann, LovL -->
<!-- begin generated symbol list -->
**Symbols in (FD-11).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b$ (the junction condition of Israel); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -12H\delta^a{}_b$ for every $a_4$, $b_4$ of the author's form. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $K^a{}_b$: The extrinsic curvature of a surface of constant $\sigma$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along all seven directions of the fold for the author's form of the metric of UM-4; $K = K^c{}_c$ its trace. Unit: GeV (1/length). Status: DERIVED.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

   ($K = K^c{}_c$ the trace of the extrinsic curvature), with $\mathcal{S}^4{}_4 = -(\text{its energy density})$,
   $\mathcal{S}^1{}_1 = \mathcal{S}^2{}_2 = \mathcal{S}^3{}_3$ its pressure along ordinary space and
   $\mathcal{S}^5{}_5 = \mathcal{S}^6{}_6 = \mathcal{S}^7{}_7$ its pressure along the extra times; $\mathcal{S}$ is $\mathcal{T}$ integrated
   across the fold, an energy per unit volume of the six other directions of the fold (unit GeV$^7$). For the static block
   ($a_4$ and $b_4$ constant) and, to the first order in the curvature of the fold divided by $H^2$, for every fold

$$
\begin{aligned}
&\text{static block:}\quad \kappa\mathcal{S}^a{}_b = -12H\,\delta^a{}_b\quad\text{(a pure tension)},\qquad \kappa\lambda_{\mathrm{F}} = 12H,\\
&\text{any fold:}\quad \kappa\mathcal{S}^a{}_b = -12H\,\delta^a{}_b + \frac{2}{5H}\,\hat G^a{}_b + \dots
\end{aligned} \tag{FD-12}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, Hconst, delta, lambdaF, Ghat, Mred, Vstar, hhat, rhoL, GN, Vt, rhoc, rhoff, rhovac, H4, MPl, h100 -->
<!-- begin generated symbol list -->
**Symbols in (FD-12).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b$ (the junction condition of Israel); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -12H\delta^a{}_b$ for every $a_4$, $b_4$ of the author's form. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.
- $\hat G^\mu{}_\nu$: The Einstein tensor of the metric $\hat g_{ab}$ of the fold (FD-2), with frame indices along its seven directions; with four-dimensional indices, $\hat G^\mu{}_\nu$, its components along the four observable directions, which for frozen extra times are those of the Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$. Unit: 1/length$^2$. Status: STANDARD.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-4: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}V_*$ (four-dimensional normalisation). Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $\rho_{\mathrm{c}}$: The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today. Unit: GeV$^4$. Value: $\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$. Status: STANDARD.
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}}V_* + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}V_*$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{vac}}$: The vacuum energy of the fields of the fold: the minimum of their potential (for the Standard Model the minimum of the Higgs potential with its loop corrections), a tension of the seven-dimensional fold. Unit: GeV$^4$. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.221\times10^{19}$ GeV. Status: STANDARD.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.

<!-- end generated symbol list -->

   ($\hat G^a{}_b$ the Einstein tensor of the metric FD-2 of the fold): the tension plus matter that obeys the Einstein equations
   of seven dimensions, $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$ ($\mathsf{t}^a{}_b$ the matter of the fold),
   which for frozen extra times are the Friedmann equations of general relativity. The fold is therefore not only a place but a
   physical object: a thin layer that carries energy and momentum (a brane).
4. *The author's coordinate $x_0$ degenerates on it.* The metric component $g_{x_0x_0} = \cot^2(6Hx_0)$ vanishes on the fold
   and nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,

$$
\lvert\sigma\rvert = 3H\Big(x_0 - \frac{\pi}{12H}\Big)^2\Big[1 + 6H^2\Big(x_0 - \frac{\pi}{12H}\Big)^2 + \dots\Big] \tag{FD-6}
$$
<!-- symbols: sigma, Hconst, x0, pi -->
<!-- begin generated symbol list -->
**Symbols in (FD-6).**

- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

   so the two coordinate values on either side of $x_0 = \pi/(12H)$ at the same coordinate distance lie at the same proper
   distance from the fold: the coordinate line of $x_0$ is folded onto the line of proper distances (a fold map, example 5).

**What lives on the fold.** In UM-4 the Higgs doublet (with the author's ad hoc vacuum, a time-dependent choice of its vacuum
value), three generations of quarks and leptons, three right-handed neutrinos and the fold fluid (its tension and the pressure
along the extra times that keeps their volume fixed) live on the fold: they are fields at $\sigma = 0$, functions of
$x_1, \dots, x_4$ (no field depends on the extra times). The gauge fields of $SU(3)_C \times SU(2)_L \times U(1)_Y$ live in the
bulk; their massless modes are bound to the fold, so that the photon and the gluons of the four-dimensional world are waves of
the bulk that the fold holds, and photons that leave the fold travel through the bulk at the speed of light. dirac16complex (the
author's spinor field of eight dimensions) and gravity live in the bulk $\sigma \ne 0$ as well as on the fold; the states $\chi$
of dirac16complex that the fold holds (in UM-4 long-lived resonances) are the part of it near the fold, and the portals
(couplings between dirac16complex and the fields of the fold) act at $\sigma = 0$. Integrated over the extra times, the fold is
the four-dimensional universe that we observe, with the metric $\mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$
in $x_1, \dots, x_4$. In UM-4 files "the fold" means this surface; the examples below use the word for other surfaces with the
same properties. The word is not used in its other senses: a set of equal energy levels is called degenerate, and a growth by
the factor $\mathrm{e}$ is called an e-folding.

**Examples of folds that are meaningful for UM-4.**

1. *Our fold.* The fold $z = \pi/2$ of the period that contains our world (FD-1): the seven-dimensional world-volume of the
   quarks, leptons and the Higgs field, and after the integration over the extra times the four-dimensional universe that we
   observe.
2. *The copies of the fold.* Because the metric repeats with the period $\pi/(6H)$, every surface
   $x_0 = \pi/(12H) + (\text{an integer multiple of } \pi/(6H))$ is a copy of the fold, one per period. Neighbouring copies are
   separated by a tip ($z$ a multiple of $\pi$), where the warp factor $(\sin^2z)^{1/6}$ vanishes and $g_{x_0x_0} = \cot^2z$
   diverges, and which lies at an infinite proper distance from both: in proper distance every copy has its own complete
   line $-\infty < \sigma < \infty$. A compact direction of length $L$ would give every field a tower of particles with the
   masses $2\pi n/L$, $n = 1, 2, \dots$ (a Kaluza-Klein tower); because the copies are infinitely far apart, the period
   $\pi/(6H)$ of $x_0$ produces no such tower with the spacing $12H$: every field of the bulk has instead a continuum of modes
   that starts at zero mass, and the fold holds its massless mode.
3. *A folded sheet of paper.* The crease of a folded sheet is a fold in this sense: the two halves are mirror images
   (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
   In UM-4 the direction across the crease is the hidden direction $\sigma$, the seven directions along the crease are
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
 - \mathrm{d}x_4^2\big),\qquad \lambda_{\mathrm{RS}} = \frac{6k_{\mathrm{RS}}}{\kappa_5},\qquad \Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2 \tag{FD-8}
$$
<!-- symbols: diff, yRS, euler, kRS, x1, x2, x3, x4, lambdaRS, kappa5, LambdaRS -->
<!-- begin generated symbol list -->
**Symbols in (FD-8).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $y_{\mathrm{RS}}$: The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-4). Unit: length. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $k_{\mathrm{RS}}$: The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp factor of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-4). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\lambda_{\mathrm{RS}}$: The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-4). Unit: GeV$^4$. Status: STANDARD.
- $\kappa_5$: The gravitational coupling of five dimensions in the model of Randall and Sundrum, $8\pi$ times the Newton constant of five dimensions (FD-8, an example, not UM-4). Unit: GeV$^{-3}$. Status: STANDARD.
- $\Lambda_{\mathrm{RS}}$: The cosmological constant of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2$, the vacuum energy density $\Lambda_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-4). Unit: GeV$^2$. Status: STANDARD.

<!-- end generated symbol list -->

   has a fold at $y_{\mathrm{RS}} = 0$ with the properties 1 to 3 (its coordinate $y_{\mathrm{RS}}$ is already the proper
   distance, so property 4 does not arise); Einstein's equations require there a brane of the tension $\lambda_{\mathrm{RS}}$
   (Israel's junction condition) and in the bulk the cosmological constant $\Lambda_{\mathrm{RS}}$ (the vacuum energy
   $\Lambda_{\mathrm{RS}}/\kappa_5$), and the bulk is otherwise empty. The
   fold of UM-4 is of the same kind, with every direction of the fold warped by the same factor as in the model of Randall and
   Sundrum: its static block is a space of constant curvature $-H^2$ in all eight directions, a vacuum of Einstein gravity with
   $\Lambda = -21H^2$, with a fold of pure tension (FD-12), and the graviton is bound to the fold as there. It differs in that the
   fold has seven dimensions, three of them extra times, in that the space is not cut at the brane (Randall and Sundrum identify
   the two sides of their brane, one physical side; the fold of UM-4 has two distinct sides, example 7), and in that the gauge
   fields live in the bulk as well.
7. *A particle held by a thin layer.* A particle held by an attractive thin layer has a wave function that falls off
   exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order Dirac
   equation, the wave function itself). In UM-4 the states $\chi$ of dirac16complex near the fold are of this kind only near
   the fold: at rest and without their self-interaction (the field is
   $\Psi = \mathrm{e}^{(7/2)H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{-\mathrm{i}\omega x_4}$)

$$
\begin{aligned}
&\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^+)\ \ (0 < \sigma \ll \sigma_{\mathrm{t}}),\qquad
\chi(\sigma) = \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\chi(0^-)\ \ (0 < -\sigma \ll \sigma_{\mathrm{t}}),\\
&\chi(0^+) = \exp\Big(\gamma^{(0)}\big(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}\big)\Big)\chi(0^-),\qquad
\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\,\Gamma_\chi,\qquad \omega_{\mathrm{r}} \to \omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}
\end{aligned} \tag{FD-9}
$$
<!-- symbols: chiprof, sigma, euler, qb, sigmat, gammaM, muX, PL, PR, omega0, omegar, imag, Gammachi, omegab, mPsi, Gamma8, Psi, identity, vielbein, omegafreq, kvec, xvec, tzero, sigma16, dagger, io -->
<!-- begin generated symbol list -->
**Symbols in (FD-9).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\sigma_{\mathrm{t}}$: The turning point of a state of dirac16complex of the frequency $\omega$: the depth at which the warped frequency equals the bulk mass, $\lvert\omega\rvert\mathrm{e}^{H\sigma_{\mathrm{t}}} = m_\Psi$; beyond it every solution oscillates. Unit: length. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\omega_0$: The energy at rest (zero momentum along ordinary space and along the extra times) of a state of dirac16complex at the fold; complex for a resonance, $\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\Gamma_\chi$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{r}}$: The mass of the particle $\chi$: the real part of the energy at rest of the resonance of dirac16complex at the fold, $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$. Unit: GeV. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Gamma_\chi$: The width of the particle $\chi$ at rest: the rate of its decay into the waves of dirac16complex in the bulk. Unit: GeV. Value: below $1/(11.6\,t_0) = 1.3\times10^{-43}$ GeV for dark matter (a lifetime above 160 Gyr). Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_4,\ \mathbf{1}_8,\ \mathbf{1}_{16}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_4$, $\mathbf{1}_8$ and $\mathbf{1}_{16}$ are the identity matrices of 4, 8 and 16 rows. Unit: dimensionless. Status: STANDARD.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.

<!-- end generated symbol list -->

   where $\mu_{\mathrm{L}}$, $\mu_{\mathrm{R}}$ are the strengths of the fold for the left- and right-handed halves of
   dirac16complex (set by the fields of the fold), $q_{\mathrm{b}} = -m_\Psi(\mu_{\mathrm{L}} + \mu_{\mathrm{R}})\tanh\varsigma/(2\varsigma)$,
   $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$ for $\mu_{\mathrm{R}} = 0$), and $\omega_{\mathrm{r}}$
   tends to the energy $\omega_{\mathrm{b}}$ of the bound state of UM-3 when $H/q_{\mathrm{b}} \to 0$. Because the time is warped, the
   energy $\omega$ of the field enters its equation multiplied by $\mathrm{e}^{H\lvert\sigma\rvert}$: beyond the turning point
   $\sigma_{\mathrm{t}}$ ($\omega_{\mathrm{r}}\mathrm{e}^{H\sigma_{\mathrm{t}}} = m_\Psi$) the profile oscillates as a wave that leaves the fold, so the
   state is a resonance of the width $\Gamma_\chi = (2/\mathrm{e})(q_{\mathrm{b}}^2/m_\Psi)\,\mathrm{e}^{-2F(\upsilon_{\mathrm{b}})m_\Psi/H}$ (to the
   leading order in $H/q_{\mathrm{b}}$), with $F(\upsilon) = \ln((1 + \sqrt{1 - \upsilon^2})/\upsilon) - \sqrt{1 - \upsilon^2}$ and
   $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ (the tunnelling through the region between the fold and $\sigma_{\mathrm{t}}$, where the profile
   decays at the local rate $\sqrt{m_\Psi^2 - \omega_{\mathrm{r}}^2\mathrm{e}^{2H\lvert\sigma\rvert}}$, which falls to 0 at $\sigma_{\mathrm{t}}$). The
   profile is not a function of $\lvert\sigma\rvert$: it jumps at the fold, $\chi(0^+) \ne \chi(0^-)$.
8. *The fold as a mirror for dirac16complex.* The reflection across the fold acts on the profiles $\chi(\sigma)$ in two ways,

$$
(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma),\qquad (\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma) \tag{FD-10}
$$
<!-- symbols: R1refl, R2refl, chiprof, sigma, Tmat -->
<!-- begin generated symbol list -->
**Symbols in (FD-10).**

- $\mathsf{R}_1$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of ordinary space, $(\mathsf{R}_1\chi)(\sigma) = T_0T_1T_2T_3\,\chi(-\sigma)$ (FD-10): a symmetry of dirac16complex, of gravity and of the mean field of the gas of the particles $\chi$; the states at the fold of Krein charge $-1$ are even, those of Krein charge $+1$ odd. Unit: dimensionless. Status: DERIVED.
- $\mathsf{R}_2$: The reflection across the fold acting on a profile of dirac16complex together with the reflection of the extra times, $(\mathsf{R}_2\chi)(\sigma) = T_0T_5T_6T_7\,\chi(-\sigma)$ (FD-10): it maps the states at the fold of one Krein charge onto those of the other. Unit: dimensionless. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), written out in FD-13: $T_a$ has the block $\bar\Xi_a$ in its upper right and $\Xi_a$ in its lower left corner; $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}_{16}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

   (for states at rest $\mathsf{R}_1$ is the reflection across the fold combined with the reflection of ordinary space,
   $\mathsf{R}_2$ the reflection across the fold combined with the reflection of the extra times). $T_a$ ($a = 0, \dots, 7$) are the
   author's real $16 \times 16$ Dirac matrices `T16^A[a]` of `4+4.nb`, built there from six real $4 \times 4$ matrices:

$$
\begin{aligned}
&\mathbf{s}_1 = \begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},\quad
 \mathbf{s}_2 = \begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
 \mathbf{s}_3 = \begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\\
&\mathbf{t}_1 = \begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\quad
 \mathbf{t}_2 = \begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
 \mathbf{t}_3 = \begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\\
&\Xi_0 = \mathbf{1}_8,\quad
 \Xi_1 = \begin{pmatrix}0&\mathbf{s}_1\\ \mathbf{s}_1&0\end{pmatrix},\quad
 \Xi_2 = \begin{pmatrix}0&\mathbf{s}_2\\ \mathbf{s}_2&0\end{pmatrix},\quad
 \Xi_3 = \begin{pmatrix}0&\mathbf{s}_3\\ \mathbf{s}_3&0\end{pmatrix},\\
&\Xi_4 = \begin{pmatrix}0&\mathbf{t}_3\\ -\mathbf{t}_3&0\end{pmatrix},\quad
 \Xi_5 = \begin{pmatrix}0&\mathbf{t}_2\\ -\mathbf{t}_2&0\end{pmatrix},\quad
 \Xi_6 = \begin{pmatrix}0&\mathbf{t}_1\\ -\mathbf{t}_1&0\end{pmatrix},\quad
 \Xi_7 = \Xi_1\Xi_2\Xi_3\Xi_4\Xi_5\Xi_6 = \begin{pmatrix}-\mathbf{1}_4&0\\0&\mathbf{1}_4\end{pmatrix},\\
&\bar\Xi_0 = \mathbf{1}_8,\quad \bar\Xi_a = \sigma_8\,\Xi_a^T\,\sigma_8,\quad
 \sigma_8 = \begin{pmatrix}0&\mathbf{1}_4\\ \mathbf{1}_4&0\end{pmatrix},\qquad
 T_a = \begin{pmatrix}0&\bar\Xi_a\\ \Xi_a&0\end{pmatrix}
\end{aligned} \tag{FD-13}
$$
<!-- symbols: sHooft, tHooft, Xiblock, Xibar, identity, sigma8, transpose, Tmat, ia, eta, sigma16, diag -->
<!-- begin generated symbol list -->
**Symbols in (FD-13).**

- $\mathbf{s}_1,\ \mathbf{s}_2,\ \mathbf{s}_3$: The author's three real antisymmetric $4 \times 4$ matrices s4by4[1], s4by4[2], s4by4[3] of 4+4.nb (written out in FD-13), the blocks of $\Xi_1$, $\Xi_2$, $\Xi_3$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{t}_1,\ \mathbf{t}_2,\ \mathbf{t}_3$: The author's three real antisymmetric $4 \times 4$ matrices t4by4[1], t4by4[2], t4by4[3] of 4+4.nb (written out in FD-13), the blocks of $\Xi_6$, $\Xi_5$, $\Xi_4$. Unit: dimensionless. Status: AUTHOR.
- $\Xi_a$: The author's eight real $8 \times 8$ matrices tau[a] of 4+4.nb ($a = 0, \dots, 7$; $\Xi_0 = \mathbf{1}_8$, $\Xi_7 = \Xi_1\Xi_2\cdots\Xi_6$), the lower left blocks of the Dirac matrices $T_a$ (FD-13). Unit: dimensionless. Status: AUTHOR.
- $\bar\Xi_a$: The author's eight real $8 \times 8$ matrices taubar[a] of 4+4.nb, $\bar\Xi_0 = \mathbf{1}_8$ and $\bar\Xi_a = \sigma_8\Xi_a^T\sigma_8$ for $a = 1, \dots, 7$, the upper right blocks of the Dirac matrices $T_a$ (FD-13). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_4,\ \mathbf{1}_8,\ \mathbf{1}_{16}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_4$, $\mathbf{1}_8$ and $\mathbf{1}_{16}$ are the identity matrices of 4, 8 and 16 rows. Unit: dimensionless. Status: STANDARD.
- $\sigma_8$: The author's real symmetric $8 \times 8$ matrix sigma88 of 4+4.nb, with the blocks $\mathbf{1}_4$ off the diagonal and zeros on it (FD-13); $\sigma_8^2 = \mathbf{1}_8$ and $\sigma_{16} = \mathrm{diag}(-\sigma_8, \sigma_8)$. Unit: dimensionless. Status: AUTHOR.
- ${}^T$: The transpose of a matrix. Status: STANDARD.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), written out in FD-13: $T_a$ has the block $\bar\Xi_a$ in its upper right and $\Xi_a$ in its lower left corner; $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}_{16}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.

<!-- end generated symbol list -->

   ($\bar\Xi_a = \sigma_8\Xi_a^T\sigma_8$ for $a = 1, \dots, 7$, and $T_a$ for $a = 0, \dots, 7$; a matrix of four blocks, each block
   $4 \times 4$ or $8 \times 8$, 0 a block of zeros; $\mathbf{s}_1, \mathbf{s}_2, \mathbf{s}_3$ and $\mathbf{t}_1, \mathbf{t}_2, \mathbf{t}_3$ are
   `s4by4[1..3]` and `t4by4[1..3]`, $\Xi_a$ and $\bar\Xi_a$ are `tau[a]` and `taubar[a]`, $\sigma_8$ is `sigma88` of the notebook). They obey
   $\{T_a, T_b\} = T_aT_b + T_bT_a = 2\eta_{ab}\mathbf{1}_{16}$ with $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; $\gamma^{(a)} = \eta^{aa}T_a$
   (no sum) are the Dirac matrices of the frame, $\gamma^{(0)}$ along $\sigma$; the chirality matrix is $\Gamma_8 = T_0T_1\cdots T_7 =
   \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$, the chiral projectors are $P_{\mathrm{L}} = (\mathbf{1}_{16} - \Gamma_8)/2$ and
   $P_{\mathrm{R}} = (\mathbf{1}_{16} + \Gamma_8)/2$, and $\sigma_{16} = T_0T_1T_2T_3 = \mathrm{diag}(-\sigma_8, \sigma_8)$ defines the Dirac adjoint
   $\bar\Psi = \Psi^\dagger\sigma_{16}$ ($\Psi^\dagger$ the complex conjugate transpose). The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a
   state can carry the charge $-1$ or $+1$. $\mathsf{R}_1$ is a symmetry of dirac16complex, of gravity and of a mean field of a
   gas of the particles $\chi$ that is the same on both sides of the fold: the four resonances of Krein charge $-1$ (the
   particles $\chi$) are even under it and the four of Krein charge $+1$ are odd, so such a mean field cannot mix the two signs of
   the indefinite charge. $\mathsf{R}_2$ maps the states of one Krein charge onto those of the other and makes the two sets
   degenerate without the self-interaction.
9. *The planes of Horava and Witten.* In M-theory (the eleven-dimensional theory whose limits include the superstring
   theories) on an interval (a circle whose points are identified with their mirror images), the two ten-dimensional planes
   left in place by the reflection are mirror surfaces (property 1); each carries one $E_8$ gauge group while gravity fills
   the bulk. As in UM-4, gravity fills the bulk; unlike UM-4, the gauge fields live on the mirror planes (in UM-4 they live in
   the bulk), and the two sides of each plane are identified (one physical side).

**What is not a fold.**

* *The tips* $z = 0$ and $z = \pi$ (mod $\pi$): the mirror exchanges them within a period, but there the warp factor vanishes,
  $g_{x_0x_0}$ diverges, and they lie at an infinite proper distance; they carry no thin source.
* *A smooth maximum of a warp factor*, such as $1/\cosh^2(H\sigma)$: mirror symmetric and largest at $\sigma = 0$, but without a
  kink and without a thin source.
<!-- end fold definition -->

# How to read this document

## What this document contains

This document answers the author's order of 2026-10-25, 13:15 PDT. It shows why the universe model UM-3 was physically incorrect
(whatever propagated in its bulk outran light on the fold), which metric replaces it and why that metric is the best choice, which
theory of gravity goes with it, and it derives, for the universe model UM-4 built on them, that photons and gravitons propagate at
the speed of light in the bulk, that the photon is a transverse wave of spin 1 and that the gravitational wave is a wave of spin 2
with the plus and cross polarisations, which stretch and squeeze space perpendicularly. It then gives the propagation of every other
field of the bulk, the propagators of the bulk from one point of the fold to another (Newton's and Coulomb's laws, the W and Z bosons
and the bounds on the author's constant $H$ that follow), the causal structure of the bulk, and what the change of the metric changes
elsewhere in the model. The document is self-contained: every equation it uses is written out, and every symbol of every display
equation is defined right after it; a symbol that one of these definitions uses is defined in this document as well. The equations
of the field equations of UM-4 keep their tags (FE-n for a field equation or a result, IN-n for a term of the action), the same in
every UM-4 document; the equations that only this document needs carry the tags P-1 and P-2.

## The status labels

Every equation and every result carries one of the labels **AUTHOR** (from the author: his notebooks `4+4.nb` and
`Dirac_Einstein-Lovelock_4+4_Nash.nb` and his orders of 2026-10-24 and 2026-10-25), **RECORD** (from the record of this repository),
**STANDARD** (textbook physics or a published measurement), **ASSUMED** (a choice of UM-4 without derivation), **INVENTED** (a new
interaction), **DERIVED** (computed and verified in UM-4: the program and the check that verify it are named), **ESTIMATE** (an order
of magnitude) and **OPEN** (not settled).

## Coordinates, signature and units

The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ is the hidden
space-like coordinate, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, and $x_5, x_6, x_7$ three extra time-like coordinates. The
signature is $(+,+,+,+,-,-,-,-)$ in this order. Units are natural: the reduced Planck constant and the speed of light are 1. A prime
on a function of $\sigma$ alone (a profile along the hidden direction) is its derivative with respect to $\sigma$; on a function of
the time $x_4$ alone it is the derivative with respect to $x_4$. "The speed of light" without a qualifier is the speed of light on
the fold, one unit of $x_1$, $x_2$ or $x_3$ per unit of $x_4$ on the static fold.

# The order and the answer

On 2026-10-25 at 13:15 PDT the author ordered:

> "Since in the UM-3 model anything that propagates in the bulk outruns light on the fold, and bulk scalars and photons faster
> than light, my model is physically incorrect. You must find a new metric model in which x4 is warped like the other
> directions, both photons and gravitons actually propagate at c in the bulk, photon waves are transverse spin-1 phenomena,
> Gravitational waves (ripples in spacetime) are spin-2 phenomena (because they originate from the rank-2 stress-energy tensor)
> and possess the following Polarization Modes: the spin-2 nature of gravitational waves manifests physically as
> characteristic "plus" (+) and "cross" (×) polarization modes that stretch and squeeze space perpendicularly. Find the best
> model and re-calculate and re-document; however keep UM-3 and create a new UM-4, placed in new folders."

The answer, point by point (UM-3 is kept unchanged in its folder `universe_model_3`; UM-4 is in the new folder
`universe_model_4`):

1. **UM-3 was physically incorrect.** Its time was not warped, so the light cone of the bulk at the depth $\sigma$ was
   $\mathrm{e}^{H\lvert\sigma\rvert}$ times wider than that of the fold (P-1): bulk scalars moved 1.22 times and bulk photons 1.41 times as
   fast as light on the fold at long wavelengths, and faster than light at every wavelength (P-2). Status: DERIVED.
2. **The new metric.** The metric of UM-4 is the author's metric with the time warped by the same factor $(\sin^2z)^{1/6}$ as the
   other six directions of the fold (FE-27), the smallest change of the author's metric that meets the order. Every slice of
   constant depth then has the light cone of the fold (P-1, FE-83). Among the static warps of this kind it is the only one that is
   a vacuum of Einstein gravity with a cosmological constant (P-1), and its static block is a space of constant curvature $-H^2$
   (FE-32).
   Status: AUTHOR (the metric and the order), ASSUMED (the way the order is met), DERIVED (its properties).
3. **The gravity.** The author's Einstein-Lovelock theory with the weights of its Gauss-Bonnet and cubic terms set to zero:
   Einstein gravity with the cosmological constant $\Lambda = -21H^2$ (IN-2). It is the only choice of the weights for which gravitons
   travel on the light cone on every background, not only around the static block (FE-68 to FE-70). Status: DERIVED.
4. **Gravitons at the speed of light in the bulk; spin 2 with the plus and cross polarisations.** Each polarisation of the graviton
   obeys the equation of a massless scalar of the bulk; its massless mode is bound to the fold and travels at the speed of light at
   every depth and every wavelength. The four-dimensional world sees it as a transverse traceless wave of helicity $\pm2$ with the
   two polarisations $+$ and $\times$, which stretch and squeeze a ring of test masses along perpendicular directions (FE-76); on the
   expanding fold it obeys the wave equation of general relativity and travels at the speed of light at every wavelength (FE-63).
   Status: DERIVED.
5. **Photons at the speed of light in the bulk; transverse waves of spin 1.** The gauge fields of the Standard Model live in the bulk
   (IN-7); their massless modes are bound to the fold and travel at the speed of light (FE-74); the photon is a transverse wave of
   helicity $\pm1$ whose electric and magnetic fields are orthogonal to its direction of motion and to each other (FE-75). Status:
   ASSUMED (the gauge fields in the bulk), DERIVED (the rest).
6. **Every other field of the bulk.** A massless scalar (FE-73), a fermion of the bulk (FE-77) and the author's field
   dirac16complex (FE-78) move at most at the speed of light; the massive modes are slower. Status: DERIVED.
7. **Nothing that stays at fixed extra times crosses the bulk faster than light.** The static block is conformally flat, so a
   signal that leaves the fold and comes back to it at fixed extra times arrives later than light along the fold (FE-83); around an
   expanding fold the largest possible advance over the Hubble distance today is $4.4\times10^{-94}$ of the travel time for
   $H = 2534$ GeV (FE-84). Along the extra times the light cone gives no such bound: a null line that also moves along an extra time
   arrives earlier, and the four time-like directions allow closed time-like curves (FE-83). Status: DERIVED.
8. **The price.** Photons in the bulk make the W and Z bosons resonances of the bulk and modify Coulomb's law; the measured
   invisible width of the Z boson bounds $H$ from below by 2534 GeV, about 2.5 TeV (FE-82); the states of dirac16complex at the
   fold become resonances (FE-86), which live longer than 160 Gyr, as dark matter must, only if $m_\Psi/H$ is large (above 1135 for
   the binding $q_{\mathrm{b}} = m_\Psi/2$); of the three vector polarisations of the graviton of the bulk, which are ghosts, the matter
   of the fold emits none at the linear order (FE-76). Status: DERIVED, ESTIMATE (the bounds), OPEN (the ghost vectors beyond the
   linear order).

# Why UM-3 was physically incorrect

$$
\begin{aligned}
&\mathrm{d}\sigma^2 + \mathrm{e}^{-2\mathfrak{p}H\lvert\sigma\rvert}\,\mathrm{d}\vec x^2 - \mathrm{e}^{-2\mathfrak{q}H\lvert\sigma\rvert}\,\mathrm{d}x_4^2
 - \mathrm{e}^{-2\mathfrak{r}H\lvert\sigma\rvert}\,\mathrm{d}\vec x_5^2:\qquad
 c_{\mathrm{loc}}(\sigma) = \mathrm{e}^{(\mathfrak{p} - \mathfrak{q})H\lvert\sigma\rvert},\\
&\text{UM-3 } (\mathfrak{p} = \mathfrak{r} = 1,\ \mathfrak{q} = 0):\ \ c_{\mathrm{loc}} = \mathrm{e}^{H\lvert\sigma\rvert} > 1,\qquad
 \text{UM-4 } (\mathfrak{p} = \mathfrak{q} = \mathfrak{r} = 1):\ \ c_{\mathrm{loc}} = 1
\end{aligned} \tag{P-1}
$$
<!-- symbols: diff, sigma, euler, wexp, Hconst, xvec, x4, x5vec, cloc -->
<!-- begin generated symbol list -->
**Symbols in (P-1).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathfrak{p},\ \mathfrak{q},\ \mathfrak{r}$: The rates of the warps of ordinary space ($\mathfrak{p}$), of the time ($\mathfrak{q}$) and of the extra times ($\mathfrak{r}$) of a static warped background, in units of $H$. Unit: dimensionless. Value: $\mathfrak{p} = \mathfrak{q} = \mathfrak{r} = 1$ for the static block of UM-4; $\mathfrak{p} = \mathfrak{r} = 1$, $\mathfrak{q} = 0$ for that of UM-3. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\vec x_5$: The position along the extra times, $\vec x_5 = (x_5, x_6, x_7)$; $\mathrm{d}\vec x_5^2 = \mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2$. Unit: length. Status: AUTHOR.
- $c_{\mathrm{loc}}$: The coordinate speed of light along $x_3$ at the depth $\sigma$ (the rate of change of $x_3$ with $x_4$ along a null line at fixed $\sigma$), in units of that on the fold: $\mathrm{e}^{H\lvert\sigma\rvert}$ on the static block of UM-3, whose time was not warped, 1 on the static block of UM-4, and on an expanding fold of UM-4 different from 1 in proportion to the second derivative $a_4''$ of $a_4$ (the rate of change of the expansion rate $a_4'$). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The static warped metrics: the hidden direction $\sigma$ unwarped, ordinary space, the time and the extra times warped with the rates
$\mathfrak{p}$, $\mathfrak{q}$ and $\mathfrak{r}$ (in units of $H$), on both sides of the fold. A signal of light that moves along $x_3$ at
fixed depth follows a null line (the metric vanishes along it), so its coordinate speed is $\mathrm{d}x_3/\mathrm{d}x_4 = \mathrm{e}^{(\mathfrak{p} - \mathfrak{q})H\lvert\sigma\rvert}$, in
units of the speed of light on the fold ($\sigma = 0$): the light cone of the slice at the depth $\sigma$ is that of the fold only if
the time is warped like ordinary space, $\mathfrak{q} = \mathfrak{p}$. The author's metric with his original time component (UM-3) has
$\mathfrak{p} = \mathfrak{r} = 1$ and $\mathfrak{q} = 0$: at the depth $\sigma$ light moves $\mathrm{e}^{H\lvert\sigma\rvert}$ times as fast as on the
fold, and every field that propagates in the bulk inherits this wider light cone. The metric of UM-4 has
$\mathfrak{p} = \mathfrak{q} = \mathfrak{r} = 1$. Equal rates are also singled out by gravity: the Einstein tensor of these metrics is
diagonal, with $G^{(0)}{}_{(0)} - G^{(1)}{}_{(1)} = (\mathfrak{p}\mathfrak{q} + 3\mathfrak{p}\mathfrak{r} - \mathfrak{q}^2 - 3\mathfrak{r}^2)H^2$,
$G^{(1)}{}_{(1)} - G^{(4)}{}_{(4)} = -(\mathfrak{p} - \mathfrak{q})(3\mathfrak{p} + \mathfrak{q} + 3\mathfrak{r})H^2$ and
$G^{(1)}{}_{(1)} - G^{(5)}{}_{(5)} = -(\mathfrak{p} - \mathfrak{r})(3\mathfrak{p} + \mathfrak{q} + 3\mathfrak{r})H^2$ (frame components along
the hidden direction, $x_1$, $x_4$ and $x_5$), and the only real rates for which the metric is a vacuum of Einstein gravity with a
cosmological constant (the Einstein tensor the same in every direction) are $\mathfrak{q} = \mathfrak{r} = \mathfrak{p}$, with
$\Lambda = -21\mathfrak{p}^2H^2$; the static block of UM-3 is not one: its three differences $G^{(0)}{}_{(0)} - G^{(1)}{}_{(1)}$,
$G^{(1)}{}_{(1)} - G^{(4)}{}_{(4)}$ and $G^{(1)}{}_{(1)} - G^{(5)}{}_{(5)}$ are $0$, $-6H^2$ and $0$. Status: DERIVED (`um4_geometry.py`, G8: the coordinate speed
of light at every depth for the metric of UM-4; G10: the Einstein tensors of the static warps and their vacua, with sympy).

$$
\begin{aligned}
&\text{UM-3:}\quad \phi_{\mathrm{bulk}} = u(\sigma)\,\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}:\qquad
 u'' - 6H\,\mathrm{sgn}(\sigma)\,u' + \big(\omega^2 - \mathrm{e}^{2H\lvert\sigma\rvert}k^2\big)\,u = 0,\\
&\text{scalar: }\ \frac{\omega^2}{k^2} \to \frac{\int\mathrm{d}\sigma\,\mathrm{e}^{-4H\lvert\sigma\rvert}}{\int\mathrm{d}\sigma\,\mathrm{e}^{-6H\lvert\sigma\rvert}} = \frac32,\qquad
 \text{photon: }\ \frac{\omega^2}{k^2} \to \frac{\int\mathrm{d}\sigma\,\mathrm{e}^{-2H\lvert\sigma\rvert}}{\int\mathrm{d}\sigma\,\mathrm{e}^{-4H\lvert\sigma\rvert}} = 2\qquad
 (k \ll H)
\end{aligned} \tag{P-2}
$$
<!-- symbols: phibulk, uprof, sigma, euler, imag, kwave, x3, omegafreq, x4, prime, Hconst, sgn, diff -->
<!-- begin generated symbol list -->
**Symbols in (P-2).**

- $\phi_{\mathrm{bulk}}$: A massless scalar field of the bulk, $\nabla_M\nabla^M\phi_{\mathrm{bulk}} = 0$ (an illustration: each polarisation of the graviton obeys its equation). Unit: GeV$^3$. Status: STANDARD.
- $u(\sigma),\ u_0$: The profile along the hidden direction of a mode of a field of the bulk (a scalar, a gauge field or a polarisation of the graviton): the field is $u(\sigma)$ times a field of the fold; $u_0 = 1$ is the profile of the massless mode (the zero mode); in a propagator the response of the field to a unit source on the fold. Unit: dimensionless (a relative amplitude); length in a propagator. Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $k$: A wave number: the momentum of a plane wave along $x_3$, $\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}$; in the cosmological perturbations the comoving wave number of a Fourier mode, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.

<!-- end generated symbol list -->

The speeds of UM-3. A massless scalar of the bulk of UM-3 (on its static block, $a_4 = 0$, $b_4 = 1$) for a wave of the frequency
$\omega$ and the wave number $k$ along $x_3$ has a profile $u(\sigma)$ that obeys the first line: the volume element of UM-3 is
$\mathrm{e}^{-6H\lvert\sigma\rvert}$ (six warped directions) and only the momentum carries the factor $\mathrm{e}^{2H\lvert\sigma\rvert}$, the
frequency not, so $\omega$ and $k$ do not enter through $\omega^2 - k^2$ and the modes are not waves of the Lorentz-invariant fold.
At long wavelengths ($k \ll H$) the lowest mode has the profile $u = 1$, and its frequency is the mean of $\mathrm{e}^{2H\lvert\sigma\rvert}k^2$
over the kinetic weight $\mathrm{e}^{-6H\lvert\sigma\rvert}$, $\omega^2 = \frac32k^2$: the bulk scalar of UM-3 moved
$\sqrt{3/2} = 1.22$ times as fast as light on the fold. The photon (the polarisation along $x_1$, whose weights carry one more factor
$\mathrm{e}^{2H\lvert\sigma\rvert}$) had $\omega^2 = 2k^2$, 1.41 times the speed of light. At shorter wavelengths the lowest mode is
squeezed towards the fold and the excess falls, but it never vanishes: $\omega^2/k^2 = 1.4999$, 1.4993, 1.4880, 1.4657 and 1.3818 for the
scalar and 1.9995, 1.9825, 1.8658, 1.7499 and 1.5150 for the photon at $k/H = 0.01$, 0.1, 0.5, 1 and 3. The gravitons of UM-3 were no
better: with Einstein gravity they would move at the local speed of light of the bulk, $\mathrm{e}^{H\lvert\sigma\rvert}$ times that of the
fold (P-1), and with the author's original Lovelock weights $\sqrt5$ times faster still (FE-69, the case $\mathfrak{p} = \mathfrak{r} = 1$,
$\mathfrak{q} = 0$); UM-3's corrected weights made its static block a degenerate vacuum without linear gravitons (the same case of FE-69,
in which all three coefficients of the second derivatives vanish for these weights). Status: DERIVED (`um4_bulk.py`, B9: the profile equation of UM-3
on both halves with sympy, the two ratios exactly, and the lowest $\omega^2$ of the operator in a box $\lvert\sigma\rvert < 6/H$; the same
box gives exactly 1 for the metric of UM-4, B1 and B2).

# The metric of UM-4

$$
\begin{aligned}
&g_{MN} = \mathrm{diag}\Big(\cot^2z,\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},
 \ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ -(\sin^2z)^{1/6},\\
&\qquad\qquad -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6},
 \ -\mathrm{e}^{-2a_4}b_4^2(\sin^2z)^{1/6}\Big),\qquad z = 6Hx_0,\\
&\sigma = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H},\qquad \mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0,\\
&g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + \mathrm{e}^{-2H\lvert\sigma\rvert}\Big[\mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2
 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2\big) - \mathrm{d}x_4^2 - \mathrm{e}^{-2a_4}b_4^2\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2\big)\Big]
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
<!-- symbols: -->

The metric of UM-4 in the author's coordinates and in the proper coordinate $\sigma$ of the hidden direction: the author's metric with
his two functions of the time $a_4(x_4)$ and $b_4(x_4)$ and his constant $H$, with the one change that the order requires: the time
carries the warp factor $(\sin^2z)^{1/6}$ of the other six directions of the fold, $g_{x_4x_4} = -(\sin^2z)^{1/6}$ (UM-3: $-1$). In the
proper coordinate the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ multiplies the whole metric of the fold, the time included. The change
keeps everything else of the author's metric: the coordinates, the period $\pi/(6H)$ of $x_0$, the fold at $z = \pi/2$ with its four
properties (the mirror, the largest warp, the kink, the degenerate coordinate $x_0$), the functions $a_4$ and $b_4$, and the warp of
ordinary space and of the extra times. Status: AUTHOR (the metric and the order), ASSUMED (the way the order is met), DERIVED
(`um4_geometry.py`, G1: the proper chart on both halves of the period).

$$
a_4,\ b_4\ \text{constant}:\qquad R^{(a)(b)}{}_{(a)(b)} = -H^2\ \text{in all 28 frame planes},\qquad
\mathcal{E}_{(1)}{}^a{}_b = 21H^2\,\delta^a{}_b,\qquad \Lambda = -21H^2 \tag{FE-32}
$$
<!-- symbols: a4, b4, Riemann, ia, ib, Hconst, LovE, ip, delta, Lambda -->
<!-- begin generated symbol list -->
**Symbols in (FE-32).**

- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant of UM-4, $\Lambda = -21H^2$: the value for which the static block is a vacuum of Einstein gravity (its Einstein tensor is $21H^2$ in every direction). The author writes the pure number $\Lambda_{\mathrm{N}}$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$, so that $\Lambda = -\Lambda_{\mathrm{N}}H^2$. Unit: GeV$^2$. Value: $-21H^2$; the author's original $-10H^2$; UM-3: $-7H^2$. Status: AUTHOR (the term), DERIVED (the value).

<!-- end generated symbol list -->
<!-- symbols: -->

The static block ($a_4$ and $b_4$ constant): its curvature is $-H^2$ in all 28 planes of the frame, a space of constant curvature in all
eight directions (locally the anti-de Sitter space of eight dimensions of radius $1/H$; UM-3 had 0 in the seven planes that contain the
time), and its Einstein tensor is $21H^2$ in every direction, so it is a vacuum of Einstein gravity with $\Lambda = -21H^2$. Status: DERIVED
(`um4_geometry.py`, G3 and G4).

$$
K^a{}_b = \frac12\,g^{ac}\,\partial_\sigma g_{cb} = -H\,\mathrm{sgn}(\sigma)\,\delta^a{}_b,\qquad
\kappa\,\mathcal{S}^a{}_b = -12H\,\delta^a{}_b\quad\big(\kappa\lambda_{\mathrm{F}} = 12H\big) \tag{FE-30}
$$
<!-- symbols: Kextr, ia, ib, metric, ic, partial, isigma, Hconst, sgn, sigma, delta, kappa, Sfoldsrc, lambdaF -->
<!-- begin generated symbol list -->
**Symbols in (FE-30).**

- $K^a{}_b$: The extrinsic curvature of a surface of constant $\sigma$ of the hidden direction, $K^a{}_b = \frac12 g^{ac}\partial_\sigma g_{cb}$ for $a, b$ along the surface (FD-5): $-H\,\mathrm{sgn}(\sigma)$ along all seven directions of the fold for the author's form of the metric of UM-4; $K = K^c{}_c$ its trace. Unit: GeV (1/length). Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $c$: A frame index (as $a$). Status: STANDARD.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b$ (the junction condition of Israel); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -12H\delta^a{}_b$ for every $a_4$, $b_4$ of the author's form. Status: DERIVED.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The fold: the slices of constant $\sigma$ have the extrinsic curvature $-H\,\mathrm{sgn}(\sigma)$ in all seven directions of the fold (all
directions are scaled by the same factor; UM-3 had 0 along the time), it jumps by $-2H$ at the fold, and Israel's junction condition makes
the fold a pure tension $\kappa\lambda_{\mathrm{F}} = 12H$, for every $a_4$ and $b_4$ of the author's form: a brane of seven dimensions of the kind
of Randall and Sundrum. Status: DERIVED (`um4_geometry.py`, G7).

$$
\tilde\sigma = \mathrm{sgn}(\sigma)\,\frac{\mathrm{e}^{H\lvert\sigma\rvert} - 1}{H}:\qquad
g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \frac{\mathrm{d}\tilde\sigma^2 + \mathrm{d}x_1^2 + \mathrm{d}x_2^2 + \mathrm{d}x_3^2 - \mathrm{d}x_4^2
 - \mathrm{d}x_5^2 - \mathrm{d}x_6^2 - \mathrm{d}x_7^2}{\big(1 + H\lvert\tilde\sigma\rvert\big)^2},\qquad \Delta x_4 \ge L \tag{FE-83}
$$
<!-- symbols: sigmaconf, sgn, sigma, euler, Hconst, metric, iM, iN, diff, Xcoord, x1, x2, x3, x4, x5, x6, x7, Delta, Ldist -->
<!-- begin generated symbol list -->
**Symbols in (FE-83).**

- $\tilde\sigma$: The conformal coordinate of the hidden direction on the static block, $\tilde\sigma = \mathrm{sgn}(\sigma)(\mathrm{e}^{H\lvert\sigma\rvert} - 1)/H$, in which the static block is conformally flat. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $L$: A distance between two points of the fold along ordinary space: for a gravitational wave the radius of a ring of free test masses ($\Delta L$ the change of the distance of one of them from the centre), for a signal the distance between its emitter and its receiver. Unit: length. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The light cone of the bulk: in the conformal coordinate $\tilde\sigma$ the static block is flat space of signature (4, 4) times the factor
$(1 + H\lvert\tilde\sigma\rvert)^{-2}$, which does not change which curves are null; the null geodesics are the null straight lines. Every slice
has the light cone of the fold, and a signal that leaves a point of the fold, travels through the bulk at the local speed of light at fixed
extra times ($\mathrm{d}x_5 = \mathrm{d}x_6 = \mathrm{d}x_7 = 0$) and arrives at another point of the fold at the distance $L$ along ordinary space
needs the time $\Delta x_4 \ge L$, with equality only for the path along the fold: nothing that stays at fixed extra times crosses the static
bulk faster than light on the fold. The bound is a statement about the section of fixed extra times, the spacetime of the fields that do not
depend on the extra times (all fields of the fold, and the modes of the bulk without momentum along them). In the full spacetime of signature
(4, 4) it does not hold: a null straight line that also moves by $Y$ along an extra time reaches the distance $L$ in the time
$\Delta x_4 = \sqrt{L^2 - Y^2}$, down to 0 for $Y = L$, and the four time-like directions allow closed time-like curves through every point.
Status: DERIVED (`um4_causality.py`, C1: the conformal form exactly; the geodesic equation; at fixed extra times 200 sampled paths through
the bulk, all later than the path along the fold, the smallest delay $1.7\times10^{-5}$ of the distance; the null line along an extra time;
C4: the closed time-like curves).

Why this is the best metric. The order fixes the time component up to the meaning of "warped like the other directions"; P-1 shows that
only the same rate for the time and for ordinary space gives photons and gravitons the speed of light at every depth, and that only the
same rate in all seven directions makes the static block a vacuum of Einstein gravity with a cosmological constant. A warp of the time with a
different function of $z$ would give $c_{\mathrm{loc}} \ne 1$ somewhere in the bulk. A metric without a warp (a flat bulk) would have
no fold and no bound graviton. Smooth warps without a kink (example "What is not a fold" of the definition of the fold) carry no thin
source and hold no field at a surface. The metric FE-27 is therefore the unique metric of the author's form, with his warp factor, that
meets the order. Status: DERIVED (P-1), ASSUMED (that the author's warp factor and fold are kept).

# Gravitons at the speed of light: spin 2 with the plus and cross polarisations

## Which gravity

$$
\begin{aligned}
S_{\mathrm{EL}} &= \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)}
 - 2\Lambda\Big) = \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\big(R - 2\Lambda\big),\qquad \kappa = 8\pi G_8,\\
\alpha_{(p)} &= w_{(p)}\,H^{2-2p},\qquad w_{(1)} = 1,\quad w_{(2)} = w_{(3)} = 0,\qquad \Lambda = -21H^2
\end{aligned} \tag{IN-2}
$$
<!-- symbols: SEL, kappa, diff, Xcoord, metric, ip, alphaL, LovL, Lambda, Riemann, pi, G8, wL, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-2).**

- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity in eight dimensions; in UM-4 the Einstein-Hilbert action with the cosmological constant. Unit: dimensionless. Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$: in UM-4 $\alpha_{(1)} = 1$ and $\alpha_{(2)} = \alpha_{(3)} = 0$ (Einstein gravity). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$, $\mathcal{L}_{(p)} = 2^{-p}\,\delta^{P_1\cdots P_{2p}}_{Q_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$, a scalar built from $p$ curvature tensors: $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/length$^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant of UM-4, $\Lambda = -21H^2$: the value for which the static block is a vacuum of Einstein gravity (its Einstein tensor is $21H^2$ in every direction). The author writes the pure number $\Lambda_{\mathrm{N}}$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$, so that $\Lambda = -\Lambda_{\mathrm{N}}H^2$. Unit: GeV$^2$. Value: $-21H^2$; the author's original $-10H^2$; UM-3: $-7H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: GeV$^{-6}$. Status: AUTHOR.
- $w_{(p)}$: The Lovelock weights of the author's Einstein-Lovelock action, $w_{(1)} = 1$ and $w_{(2)}$, $w_{(3)}$ of the Gauss-Bonnet and the cubic densities. UM-4 sets $w_{(2)} = w_{(3)} = 0$ (Einstein gravity): the only weights for which gravitons propagate on the light cone on every background, not only around the static block. The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) keep the gravitons on the light cone only around the static block (with $\Lambda = -161H^2/16$); UM-3 used $(1, 1/20, 1/360)$. Unit: dimensionless. Value: $(1, 0, 0)$ in UM-4; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), DERIVED (the values that the order of 2026-10-25 selects).
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

The gravity of UM-4: the author's Einstein-Lovelock action (his notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[134]) with the
weights of the Gauss-Bonnet density and of the cubic Lovelock density set to zero, which is Einstein gravity in eight dimensions with the
cosmological constant $\Lambda = -21H^2$. The three displays below show why. Status: AUTHOR (the action), DERIVED (the weights).

$$
\begin{aligned}
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^a{}_b + \Lambda\,\delta^a{}_b = \mathsf{P}(\mathsf{y})\,H^2\,\delta^a{}_b,\qquad
 \mathsf{P}(\mathsf{y}) = 21\mathsf{y} - 420w_{(2)}\mathsf{y}^2 + 2520w_{(3)}\mathsf{y}^3 + \frac{\Lambda}{H^2},\\
&\text{Einstein } (w_{(2)} = w_{(3)} = 0,\ \Lambda = -21H^2):\quad \mathsf{P} = 21(\mathsf{y} - 1);\\
&\text{the author's original weights } \Big(\frac{1}{32}, \frac{1}{1152}\Big),\ \Lambda = -\frac{161}{16}H^2:\quad
 \mathsf{P} = \frac{7}{16}(\mathsf{y} - 1)\big(5\mathsf{y}^2 - 25\mathsf{y} + 23\big);\\
&\text{UM-3's weights } \Big(\frac{1}{20}, \frac{1}{360}\Big),\ \Lambda = -7H^2:\quad \mathsf{P} = 7(\mathsf{y} - 1)^3
\end{aligned} \tag{FE-70}
$$
<!-- symbols: ip, alphaL, LovE, ia, ib, Lambda, delta, Pcon, ycurv, Hconst, wL -->
<!-- begin generated symbol list -->
**Symbols in (FE-70).**

- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$: in UM-4 $\alpha_{(1)} = 1$ and $\alpha_{(2)} = \alpha_{(3)} = 0$ (Einstein gravity). Unit: GeV$^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, $\mathcal{E}_{(p)}{}^M{}_N = -2^{-(p+1)}\,\delta^{MP_1\cdots P_{2p}}_{NQ_1\cdots Q_{2p}}\,R^{Q_1Q_2}{}_{P_1P_2}\cdots R^{Q_{2p-1}Q_{2p}}{}_{P_{2p-1}P_{2p}}$ (with both indices down it is $1/\sqrt{\lvert g\rvert}$ times the variation of $\sqrt{\lvert g\rvert}\,\mathcal{L}_{(p)}$ with respect to $g^{MN}$; $\mathcal{E}_{(1)}$ the Einstein tensor, $\mathcal{E}_{(2)}$ the Gauss-Bonnet tensor, $\mathcal{E}_{(3)}$ the cubic Lovelock tensor); with frame indices its frame components. Unit: 1/length$^{2p}$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant of UM-4, $\Lambda = -21H^2$: the value for which the static block is a vacuum of Einstein gravity (its Einstein tensor is $21H^2$ in every direction). The author writes the pure number $\Lambda_{\mathrm{N}}$ in $0 = -\Lambda_{\mathrm{N}} + \sum_p H^{-2p}w_{(p)}\mathcal{E}_{(p)}$, so that $\Lambda = -\Lambda_{\mathrm{N}}H^2$. Unit: GeV$^2$. Value: $-21H^2$; the author's original $-10H^2$; UM-3: $-7H^2$. Status: AUTHOR (the term), DERIVED (the value).
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\mathsf{P}(\mathsf{y})$: The vacuum polynomial of the static blocks of curvature $-\mathsf{y}H^2$: the left-hand side of the bulk equations divided by $H^2$, the same in every direction, $\mathsf{P}(\mathsf{y}) = 21\mathsf{y} - 420w_{(2)}\mathsf{y}^2 + 2520w_{(3)}\mathsf{y}^3 + \Lambda/H^2$; $\mathsf{P}'(1)$ its derivative at $\mathsf{y} = 1$, which sets the strength of the graviton around the static block relative to Einstein gravity ($\mathsf{P}'(1)/21$). Unit: dimensionless. Value: $21(\mathsf{y} - 1)$ for Einstein gravity with $\Lambda = -21H^2$. Status: DERIVED.
- $\mathsf{y}$: The curvature of a static block of constant curvature $-\mathsf{y}H^2$ in all eight directions, in units of $-H^2$ (its warp is $\mathrm{e}^{-2\sqrt{\mathsf{y}}H\lvert\sigma\rvert}$ in all seven directions of the fold): $\mathsf{y} = 1$ is the static block of UM-4. Unit: dimensionless. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $w_{(p)}$: The Lovelock weights of the author's Einstein-Lovelock action, $w_{(1)} = 1$ and $w_{(2)}$, $w_{(3)}$ of the Gauss-Bonnet and the cubic densities. UM-4 sets $w_{(2)} = w_{(3)} = 0$ (Einstein gravity): the only weights for which gravitons propagate on the light cone on every background, not only around the static block. The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) keep the gravitons on the light cone only around the static block (with $\Lambda = -161H^2/16$); UM-3 used $(1, 1/20, 1/360)$. Unit: dimensionless. Value: $(1, 0, 0)$ in UM-4; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), DERIVED (the values that the order of 2026-10-25 selects).

<!-- end generated symbol list -->
<!-- symbols: -->

The vacua of the static family (the static blocks of curvature $-\mathsf{y}H^2$ in all eight directions): the left-hand side of the bulk
equations is the same in every direction, $\mathsf{P}(\mathsf{y})H^2$. Einstein gravity has the single vacuum $\mathsf{y} = 1$ with
$\mathsf{P}'(1) = 21$. The author's original weights would need $\Lambda = -161H^2/16$ (not his $-10H^2$), with $\mathsf{P}'(1) = 21/16$;
UM-3's weights make $\mathsf{y} = 1$ a triple root, a degenerate vacuum without linear gravitons. Status: DERIVED (`um4_geometry.py`,
G4; `um4_gravity.py`, L1).

$$
\frac{\mathsf{P}'(1)}{42}\Big[\mathrm{e}^{2H\lvert\sigma\rvert}\Big(\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2}
 - \frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2}\Big) - \frac{\partial^2h_{\mathrm{gw}}}{\partial\sigma^2}
 + 7H\,\mathrm{sgn}(\sigma)\,\frac{\partial h_{\mathrm{gw}}}{\partial\sigma}\Big] = 0,\qquad
\mathsf{P}'(1) = 21 - 840w_{(2)} + 7560w_{(3)} \tag{FE-68}
$$
<!-- symbols: Pcon, prime, euler, Hconst, sigma, partial, hgw, x4, x3, sgn, wL -->
<!-- begin generated symbol list -->
**Symbols in (FE-68).**

- $\mathsf{P}(\mathsf{y})$: The vacuum polynomial of the static blocks of curvature $-\mathsf{y}H^2$: the left-hand side of the bulk equations divided by $H^2$, the same in every direction, $\mathsf{P}(\mathsf{y}) = 21\mathsf{y} - 420w_{(2)}\mathsf{y}^2 + 2520w_{(3)}\mathsf{y}^3 + \Lambda/H^2$; $\mathsf{P}'(1)$ its derivative at $\mathsf{y} = 1$, which sets the strength of the graviton around the static block relative to Einstein gravity ($\mathsf{P}'(1)/21$). Unit: dimensionless. Value: $21(\mathsf{y} - 1)$ for Einstein gravity with $\Lambda = -21H^2$. Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world, to the first order its plus polarisation $h_{+}$. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $w_{(p)}$: The Lovelock weights of the author's Einstein-Lovelock action, $w_{(1)} = 1$ and $w_{(2)}$, $w_{(3)}$ of the Gauss-Bonnet and the cubic densities. UM-4 sets $w_{(2)} = w_{(3)} = 0$ (Einstein gravity): the only weights for which gravitons propagate on the light cone on every background, not only around the static block. The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) keep the gravitons on the light cone only around the static block (with $\Lambda = -161H^2/16$); UM-3 used $(1, 1/20, 1/360)$. Unit: dimensionless. Value: $(1, 0, 0)$ in UM-4; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), DERIVED (the values that the order of 2026-10-25 selects).

<!-- end generated symbol list -->
<!-- symbols: -->

The graviton around the static block of UM-4 for any weights: the + polarisation of a wave along $x_3$ (the metric components along
$x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$). The time and ordinary space enter only through
$\mathrm{e}^{2H\lvert\sigma\rvert}(\partial^2/\partial x_4^2 - \partial^2/\partial x_3^2)$: at every depth the wave has the light cone of the fold, whatever
the weights, with the strength $\mathsf{P}'(1)/21$ relative to Einstein gravity. Around the static block the order therefore does not
single out Einstein gravity; FE-69 does. Status: DERIVED (`um4_gravity.py`, L2).

$$
\begin{aligned}
&\mathrm{d}\sigma^2 + \mathrm{e}^{-2\mathfrak{p}H\sigma}\,\mathrm{d}\vec x^2 - \mathrm{e}^{-2\mathfrak{q}H\sigma}\,\mathrm{d}x_4^2
 - \mathrm{e}^{-2\mathfrak{r}H\sigma}\,\mathrm{d}\vec x_5^2\quad(\sigma > 0):\\
&c_{\mathrm{x}} - c_{\mathrm{t}} = -4\,(\mathfrak{p} - \mathfrak{q})\big(18\mathfrak{r}^2w_{(3)} - w_{(2)}\big)\big(\mathfrak{p} + \mathfrak{q} + 3\mathfrak{r}\big),\\
&c_\sigma - c_{\mathrm{t}} = -4\big[w_{(2)}\big(\mathfrak{p}\mathfrak{q} - \mathfrak{p}^2 + 3\mathfrak{q}\mathfrak{r} - 3\mathfrak{r}^2\big)
 + 18w_{(3)}\mathfrak{r}^2\big(\mathfrak{p}^2 - 3\mathfrak{p}\mathfrak{q} + 2\mathfrak{p}\mathfrak{r} - \mathfrak{q}\mathfrak{r} + \mathfrak{r}^2\big)\big]
\end{aligned} \tag{FE-69}
$$
<!-- symbols: diff, sigma, euler, wexp, Hconst, xvec, x4, x5vec, cxw, ctw, csig, wL -->
<!-- begin generated symbol list -->
**Symbols in (FE-69).**

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathfrak{p},\ \mathfrak{q},\ \mathfrak{r}$: The rates of the warps of ordinary space ($\mathfrak{p}$), of the time ($\mathfrak{q}$) and of the extra times ($\mathfrak{r}$) of a static warped background, in units of $H$. Unit: dimensionless. Value: $\mathfrak{p} = \mathfrak{q} = \mathfrak{r} = 1$ for the static block of UM-4; $\mathfrak{p} = \mathfrak{r} = 1$, $\mathfrak{q} = 0$ for that of UM-3. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\vec x_5$: The position along the extra times, $\vec x_5 = (x_5, x_6, x_7)$; $\mathrm{d}\vec x_5^2 = \mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2$. Unit: length. Status: AUTHOR.
- $c_{\mathrm{x}}$: The coefficient of the second derivative along the proper length of $x_3$ in the same equation; the wave moves along $x_3$ with the local speed $\sqrt{c_{\mathrm{x}}/c_{\mathrm{t}}}$ in units of the local speed of light. Unit: dimensionless. Value: 1 for Einstein gravity on every background; $1 - 24w_{(2)} + 72w_{(3)}$ at the static block of UM-3 ($c_{\mathrm{x}}/c_{\mathrm{t}} = 5$ with the author's original weights). Status: DERIVED.
- $c_{\mathrm{t}}$: The coefficient of the second derivative along the proper time in the linearised equation of a gravitational wave of the + polarisation on a static warped background, normalised so that Einstein gravity gives 1. Unit: dimensionless. Value: 1 for Einstein gravity on every background; $1 - 40w_{(2)} + 360w_{(3)}$ at the static block of UM-3. Status: DERIVED.
- $c_\sigma$: The coefficient of the second derivative along $\sigma$ in the linearised equation of a gravitational wave on a static warped background, normalised so that Einstein gravity gives 1; the wave moves along $\sigma$ with the local speed $\sqrt{c_\sigma/c_{\mathrm{t}}}$ in units of the local speed of light. Unit: dimensionless. Value: 1 for Einstein gravity on every background. Status: DERIVED.
- $w_{(p)}$: The Lovelock weights of the author's Einstein-Lovelock action, $w_{(1)} = 1$ and $w_{(2)}$, $w_{(3)}$ of the Gauss-Bonnet and the cubic densities. UM-4 sets $w_{(2)} = w_{(3)} = 0$ (Einstein gravity): the only weights for which gravitons propagate on the light cone on every background, not only around the static block. The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[134]) keep the gravitons on the light cone only around the static block (with $\Lambda = -161H^2/16$); UM-3 used $(1, 1/20, 1/360)$. Unit: dimensionless. Value: $(1, 0, 0)$ in UM-4; the author's original $(1, 1/32, 1/1152)$. Status: AUTHOR (the form), DERIVED (the values that the order of 2026-10-25 selects).

<!-- end generated symbol list -->
<!-- symbols: -->

The gravitons on backgrounds that are not of constant curvature: the static warps of P-1 with any rates. The coefficients
$c_{\mathrm{t}}$, $c_{\mathrm{x}}$ and $c_\sigma$ of the second derivatives along the proper time, the proper length of $x_3$ and $\sigma$ in
the linearised equation of the + polarisation are 1 for Einstein gravity on every such background; the Gauss-Bonnet and cubic terms give
the deviations shown, which vanish for all rates only for $w_{(2)} = w_{(3)} = 0$. An expanding universe, a star or a gravitational wave of
finite amplitude make the warps of the different directions differ, so with the Gauss-Bonnet or the cubic term gravitons would leave the
light cone there. At the static block of UM-3 ($\mathfrak{p} = \mathfrak{r} = 1$, $\mathfrak{q} = 0$) the author's original weights give
$c_{\mathrm{x}}/c_{\mathrm{t}} = 5$: gravitons $\sqrt5$ times faster than the local light, which itself was faster than light on the fold.
Status: DERIVED (`um4_gravity.py`, L3 and L4).

## The gravitational wave

$$
\begin{aligned}
&\frac12\Big[\mathrm{e}^{2H\lvert\sigma\rvert}\Big(\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2} - \frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2}\Big)
 - \frac{\partial^2h_{\mathrm{gw}}}{\partial\sigma^2} + 7H\,\mathrm{sgn}(\sigma)\,\frac{\partial h_{\mathrm{gw}}}{\partial\sigma}\Big] = 0:\qquad
 h_{\mathrm{gw}} = h_{+}(x_3 - x_4),\\
&\mathsf{h}_{ij} = \begin{pmatrix} h_{+} & h_{\times} & 0\\ h_{\times} & -h_{+} & 0\\ 0 & 0 & 0\end{pmatrix},\qquad
 \frac{\Delta L}{L} = \frac12\big(h_{+}\cos2\phi_{\mathrm{r}} + h_{\times}\sin2\phi_{\mathrm{r}}\big),\qquad
 h_{+} \pm \mathrm{i}h_{\times} \to \mathrm{e}^{\mp2\mathrm{i}\theta_{\mathrm{r}}}\big(h_{+} \pm \mathrm{i}h_{\times}\big)
\end{aligned} \tag{FE-76}
$$
<!-- symbols: euler, Hconst, sigma, partial, hgw, x4, x3, sgn, hplus, hTT, ii, ij, hcross, Delta, Ldist, phir, imag, thetar -->
<!-- begin generated symbol list -->
**Symbols in (FE-76).**

- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world, to the first order its plus polarisation $h_{+}$. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $h_{+}$: The plus polarisation of a gravitational wave travelling along $x_3$: $\mathsf{h}_{11} = -\mathsf{h}_{22} = h_{+}$, a function of $x_3 - x_4$; to the first order the zero mode of $h_{\mathrm{gw}}$. Unit: dimensionless. Status: STANDARD.
- $\mathsf{h}_{ij}$: The transverse traceless perturbation of the metric of ordinary space by a gravitational wave as the four-dimensional world sees it: $\hat h_{ij} = \mathrm{e}^{2a_4}(\delta_{ij} + \mathsf{h}_{ij})$ ($i, j = 1, 2, 3$). Unit: dimensionless. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal), and in a tensor of ordinary space such as $\mathsf{h}_{ij}$ one of the directions $x_1, x_2, x_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $j$: A second generation or mass-state index, or a second direction of ordinary space (as $i$). Status: STANDARD.
- $h_{\times}$: The cross polarisation of a gravitational wave travelling along $x_3$: $\mathsf{h}_{12} = \mathsf{h}_{21} = h_{\times}$, a function of $x_3 - x_4$. Unit: dimensionless. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $L$: A distance between two points of the fold along ordinary space: for a gravitational wave the radius of a ring of free test masses ($\Delta L$ the change of the distance of one of them from the centre), for a signal the distance between its emitter and its receiver. Unit: length. Status: STANDARD.
- $\phi_{\mathrm{r}}$: The angle at which a test mass sits on a ring of test masses in the plane of $x_1$ and $x_2$, measured from the $x_1$ axis. Unit: dimensionless (radian). Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\theta_{\mathrm{r}}$: The angle of a rotation about the direction of motion of a wave. Unit: dimensionless (radian). Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The gravitational wave in the bulk and on the fold. First line: Einstein's equation of the bulk to the first order in the + polarisation
$h_{\mathrm{gw}}$ of a wave along $x_3$; it is the equation of a massless scalar of the bulk (FE-73), and its zero mode, independent of $\sigma$,
is any function of $x_3 - x_4$: it solves the bulk equation on both sides and the junction condition at the fold, so the graviton of the
bulk has a massless mode bound to the fold that travels at the speed of light at every wavelength and at every depth. Second line: the wave
as the four-dimensional world sees it, the transverse traceless perturbation $\mathsf{h}_{ij}$ of the metric of ordinary space, with the two
polarisations $h_{+}$ (the "plus" mode, $\mathsf{h}_{11} = -\mathsf{h}_{22}$) and $h_{\times}$ (the "cross" mode,
$\mathsf{h}_{12} = \mathsf{h}_{21}$). A ring of free test masses of the radius $L$ in the plane of $x_1$ and $x_2$ changes the distance of the mass
at the angle $\phi_{\mathrm{r}}$ from its centre by $\Delta L$: the plus mode stretches the ring along $x_1$ while it squeezes it along $x_2$ and
then the reverse, the cross mode does the same along the two diagonals, rotated by $45^\circ$: they stretch and squeeze space
perpendicularly to each other and to the direction of motion. Under a rotation by the angle $\theta_{\mathrm{r}}$ about the direction of motion
the circular combinations $h_{+} \pm \mathrm{i}h_{\times}$ are multiplied by $\mathrm{e}^{\mp2\mathrm{i}\theta_{\mathrm{r}}}$: helicity $\pm2$, a wave of
spin 2, as it must be for a wave sourced by the rank-2 energy-momentum tensor. The massless graviton of seven dimensions has
$7\cdot(7 - 3)/2 = 14$ polarisations (20 transverse traceless components less 6 residual gauge modes), which the four-dimensional world sees
as the graviton (2), three vectors $h_{\mu r}$ (6) and six scalars $h_{rs}$ (6). In the Einstein-Hilbert action to the second order on the
fold of signature (3, 4) the graviton and the six scalars have kinetic terms of the right sign, but the three vectors $h_{\mu r}$, with one
index along ordinary space or the time and one along an extra time, have the wrong sign: they are ghosts, like the components $A_r$ of a
gauge field along the extra times that UM-4 excludes. Matter of the fold that does not depend on the extra times and is the same along the
three of them has no stress $\mathcal{T}_{\mu r}$ and only the trace of $\mathcal{T}_{rs}$, so at the linear order it emits only $h_{+}$,
$h_{\times}$ and the trace of $h_{rs}$, the volume of the extra times, which the fold fluid holds fixed, and no ghost vectors: the
gravitational waves that the matter of the fold emits have only the plus and the cross polarisations, as the order requires and as observed
(no other polarisation has been detected). The ghost vectors remain a defect of the bulk gravity of signature (3, 4) at higher orders.
Status: DERIVED (`um4_bulk.py`, B4, B5 and B11: the signs of the kinetic terms of all 14 polarisations from the action;
`um4_foldsources.py`, FS2), ASSUMED (that the fold fluid holds the volume of the extra times fixed for waves as well), OPEN (the ghost
vectors beyond the linear order).

$$
\frac{1}{2}\Big(\frac{\partial^2h_{\mathrm{gw}}}{\partial x_4^2} + 3a_4'\,\frac{\partial h_{\mathrm{gw}}}{\partial x_4}
 - \mathrm{e}^{-2a_4}\,\frac{\partial^2h_{\mathrm{gw}}}{\partial x_3^2}\Big) = \kappa_7\,\Pi_{\mathrm{gw}},\qquad
\kappa_7 = \frac52\,\kappa H,\qquad c_{\mathrm{g}} = 1 \tag{FE-63}
$$
<!-- symbols: partial, hgw, x4, a4, prime, euler, x3, kappa7, Pigw, kappa, Hconst, cgrav -->
<!-- begin generated symbol list -->
**Symbols in (FE-63).**

- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $h_{\mathrm{gw}}$: The amplitude of a gravitational wave of the + polarisation travelling along $x_3$: the metric components along $x_1$ and $x_2$ multiplied by $\mathrm{e}^{h_{\mathrm{gw}}}$ and $\mathrm{e}^{-h_{\mathrm{gw}}}$; a function of $\sigma$, $x_3$ and $x_4$ in the bulk, and on the fold the gravitational wave of the four-dimensional world, to the first order its plus polarisation $h_{+}$. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\Pi_{\mathrm{gw}}$: The transverse traceless stress of the matter of the fold that drives the gravitational wave $h_{\mathrm{gw}}$ (half the difference of its components along $x_1$ and $x_2$), integrated across the fold (eight-dimensional normalisation). Unit: GeV$^7$. Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $c_{\mathrm{g}}$: The speed of gravitational waves on the fold, in units of the speed of light. Unit: dimensionless. Value: 1 at every wavelength for the four-dimensional graviton on the static block and on every fold with frozen extra times, and for the massless graviton of the bulk at every depth; measured $-3\times10^{-15} \le c_{\mathrm{g}} - 1 \le 7\times10^{-16}$ (GW170817). Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The gravitational wave on the expanding fold (frozen extra times): the wave equation of general relativity on the metric of the
four-dimensional universe, sourced by the transverse traceless stress of the matter of the fold with the coupling $\kappa_7$ of the
Friedmann equations. It travels at the speed of light at every wavelength ($c_{\mathrm{g}} = 1$ identically), which the simultaneous arrival of
the gravitational wave GW170817 and of the light of its source confirms to $10^{-15}$. Status: DERIVED (`um4_foldsources.py`, FS2), STANDARD
(the measurement).

$$
\kappa\,\mathcal{S}^a{}_b = -12H\,\delta^a{}_b + \frac{2}{5H}\,\hat G^a{}_b + \dots,\qquad
\mathcal{S}^a{}_b = -\lambda_{\mathrm{F}}\,\delta^a{}_b + \mathsf{t}^a{}_b:\qquad
\hat G^a{}_b = \kappa_7\,\mathsf{t}^a{}_b,\qquad \kappa_7 = \frac52\,\kappa H \tag{FE-71}
$$
<!-- symbols: kappa, Sfoldsrc, ia, ib, Hconst, delta, Ghat, lambdaF, tfold, kappa7 -->
<!-- begin generated symbol list -->
**Symbols in (FE-71).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b$ (the junction condition of Israel); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -12H\delta^a{}_b$ for every $a_4$, $b_4$ of the author's form. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\hat G^\mu{}_\nu$: The Einstein tensor of the metric $\hat g_{ab}$ of the fold (FD-2), with frame indices along its seven directions; with four-dimensional indices, $\hat G^\mu{}_\nu$, its components along the four observable directions, which for frozen extra times are those of the Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$. Unit: 1/length$^2$. Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.
- $\mathsf{t}^a{}_b,\ \mathsf{t}$: The matter of the fold above its tension: the thin source minus the tension, $\mathcal{S}^a{}_b = -\lambda_{\mathrm{F}}\delta^a{}_b + \mathsf{t}^a{}_b$ (eight-dimensional normalisation); $\mathsf{t} = \mathsf{t}^c{}_c$ its trace; with frozen extra times $\mathsf{t}^a{}_b = \mathrm{diag}(P_7, P_7, P_7, -\rho_7, q_7, q_7, q_7)$. Unit: GeV$^7$. Status: DERIVED.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The gravity of the fold: the junction condition, to the first order in the curvature of the fold divided by $H^2$, is the pure tension plus
the Einstein tensor of seven dimensions; the thin source is the tension plus the matter of the fold, which therefore obeys the Einstein
equations of seven dimensions with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold. With
frozen extra times they are the Friedmann equations of general relativity with Newton's constant $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (FE-44),
up to corrections of the relative size $(a_4'/H)^2$, about $3\times10^{-91}$ today for $H = 2534$ GeV. Status: DERIVED (`um4_fold.py`, F1,
F2, F4 and F5).

# Photons at the speed of light: transverse waves of spin 1

$$
\begin{aligned}
S_{\mathrm{gauge}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\mathcal{L}_{\mathrm{gauge}},\qquad
\mathcal{L}_{\mathrm{gauge}} = -\frac{1}{4\mathsf{g}_3^2}\,G^A_{MN}G^{AMN} - \frac{1}{4\mathsf{g}_2^2}\,W^I_{MN}W^{IMN}
 - \frac{1}{4\mathsf{g}_1^2}\,B_{MN}B^{MN},\\
G^A_{MN} &= \partial_MG^A_N - \partial_NG^A_M + f^{ABC}G^B_MG^C_N,\qquad
W^I_{MN} = \partial_MW^I_N - \partial_NW^I_M + \epsilon^{IJK}W^J_MW^K_N,\\
B_{MN} &= \partial_MB_N - \partial_NB_M
\end{aligned} \tag{IN-7}
$$
<!-- symbols: Sgauge, diff, Xcoord, metric, Lgauge, gbulk, Ggluon, iA, iM, iN, Wsu2, iI, Bhyp, partial, fabc, iB, iC, epsLC, iJ, iK -->
<!-- begin generated symbol list -->
**Symbols in (IN-7).**

- $S_{\mathrm{gauge}}$: The action of the gauge fields in the bulk. Unit: dimensionless. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{gauge}}$: The Lagrangian of the gauge fields of $SU(3)_C\times SU(2)_L\times U(1)_Y$ in the bulk. Unit: GeV$^8$. Status: STANDARD.
- $\mathsf{g}_1,\ \mathsf{g}_2,\ \mathsf{g}_3$: The gauge couplings of eight dimensions of $U(1)_Y$, $SU(2)_L$ and $SU(3)_C$: the coefficients of the kinetic terms of the gauge fields of the bulk in their geometric normalisation; the four-dimensional couplings are $g_k^2 = 3H\mathsf{g}_k^2/(2V_*)$. Unit: GeV$^{-2}$ ($\mathsf{g}^2$: length$^4$). Status: ASSUMED.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $W^I_M,\ W^I_\mu,\ W^I_{MN}$: The gauge field of $SU(2)_L$ ($I = 1, 2, 3$): in the bulk $W^I_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $W^I_\mu(x)$ of its massless mode, $g_2W^I_\mu(x) = W^I_\mu(\sigma = 0, x)$; $W^I_{MN}$, $W^I_{\mu\nu}$ their field strengths; $W^\pm_\mu = (W^1_\mu \mp \mathrm{i}W^2_\mu)/\sqrt2$. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $B_M,\ B_\mu,\ B_{MN}$: The hypercharge gauge field of $U(1)_Y$: in the bulk $B_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $B_\mu(x)$ of its massless mode, $g_1B_\mu(x) = B_\mu(\sigma = 0, x)$; $B_{MN}$, $B_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $f^{ABC}$: The structure constants of $SU(3)$, $[t^A, t^B] = \mathrm{i}f^{ABC}t^C$. Unit: dimensionless. Status: STANDARD.
- $B$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $C$: A colour (adjoint SU(3)) index (as $A$). Status: STANDARD.
- $\epsilon^{IJK}$: The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$. Unit: dimensionless. Status: STANDARD.
- $J$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.
- $K$: A weak-isospin (adjoint SU(2)) index (as $I$). Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The gauge fields of the Standard Model in the bulk of eight dimensions (the order puts the photon in the bulk, and with it the
electroweak gauge fields of which it is a combination; UM-4 puts the gluons there as well). Status: AUTHOR (the photon in the bulk, by the
order), ASSUMED (all gauge fields in the bulk), STANDARD (the Yang-Mills action).

$$
\begin{aligned}
&B_\sigma = 0,\quad B_a = u(\sigma)\,\hat B_a(x):\qquad
u'' - 5H\,\mathrm{sgn}(\sigma)\,u' + \mathrm{e}^{2H\lvert\sigma\rvert}\,m^2\,u = 0,\qquad
\eta^{ac}\,\partial_a\hat B_{cb} = m^2\,\hat B_b,\\
&u_0 = 1,\quad \int_{-\infty}^{\infty}\mathrm{d}\sigma\,\mathrm{e}^{-3H\lvert\sigma\rvert}\,u_0^2 = \frac{2}{3H}
\end{aligned} \tag{FE-74}
$$
<!-- symbols: Bhyp, isigma, ia, uprof, sigma, Bhat, xfour, prime, Hconst, sgn, euler, mmass, eta, ic, partial, ib, infty, diff -->
<!-- begin generated symbol list -->
**Symbols in (FE-74).**

- $B_M,\ B_\mu,\ B_{MN}$: The hypercharge gauge field of $U(1)_Y$: in the bulk $B_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $B_\mu(x)$ of its massless mode, $g_1B_\mu(x) = B_\mu(\sigma = 0, x)$; $B_{MN}$, $B_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $u(\sigma),\ u_0$: The profile along the hidden direction of a mode of a field of the bulk (a scalar, a gauge field or a polarisation of the graviton): the field is $u(\sigma)$ times a field of the fold; $u_0 = 1$ is the profile of the massless mode (the zero mode); in a propagator the response of the field to a unit source on the fold. Unit: dimensionless (a relative amplitude); length in a propagator. Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\hat B_a,\ \hat B_{ab}$: The field of the fold of a mode of the hypercharge field of the bulk (of any gauge field of the bulk to the first order in the field), $B_a = u(\sigma)\hat B_a(x)$; $\hat B_{ab} = \partial_a\hat B_b - \partial_b\hat B_a$ its field strength. Unit: GeV (field), GeV$^2$ (field strength). Status: STANDARD.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $c$: A frame index (as $a$). Status: STANDARD.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The modes of a gauge field of the bulk, written for the hypercharge field, in the gauge $B_\sigma = 0$: the field of the fold $\hat B_a(x)$ obeys
the Proca equation of the fold with the mass $m$, and the profile the equation in the middle. The massless mode has the profile 1 and the
kinetic weight $\mathrm{e}^{-3H\lvert\sigma\rvert}$ with the finite integral $2/(3H)$: a massless gauge field of the fold, bound to it, at the speed
of light at every wavelength. The massive modes form a continuum from zero mass upwards and move slower than light. A component along the
hidden direction has no normalisable zero mode. (In UM-3 the bulk photon had $\omega^2 = 2k^2$, P-2.) Status: DERIVED (`um4_bulk.py`, B2:
the profile equation exactly on both halves; the lowest $\omega^2$ in a box equals $k^2$ to $4\times10^{-12}$; B10: the continuum of massive
modes from zero mass, Bessel functions of the warped distance from the fold).

$$
\begin{aligned}
&A_\mu = \mathfrak{e}_\mu\,\mathrm{e}^{\mathrm{i}k(x_3 - x_4)}:\qquad \mathfrak{e}_3 + \mathfrak{e}_4 = 0,\qquad
\mathfrak{e}_\mu \sim \mathfrak{e}_\mu + \beta_{\mathrm{g}}\,k\,(0, 0, 1, -1),\\
&\mathfrak{e}_\pm = \frac{1}{\sqrt2}\big(1, \pm\mathrm{i}, 0, 0\big) \to \mathrm{e}^{\mp\mathrm{i}\theta_{\mathrm{r}}}\,\mathfrak{e}_\pm,\qquad
\vec E\cdot\vec B = 0,\quad \vec E^2 = \vec B^2
\end{aligned} \tag{FE-75}
$$
<!-- symbols: Aphoton, imu, polvec, euler, imag, kwave, x3, x4, betag, thetar, Efield, Bfield -->
<!-- begin generated symbol list -->
**Symbols in (FE-75).**

- $A_\mu$: The photon field of the fold (canonically normalised): the massless combination of the massless modes of $W^1, W^2, W^3$ and $B$ that the Higgs vacuum leaves massless; a field of the bulk whose zero mode travels at the speed of light. Unit: GeV. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\mathfrak{e}_\mu,\ \mathfrak{e}_\pm$: The polarisation vector of a plane wave of the photon, with components along $x_1, x_2, x_3, x_4$; $\mathfrak{e}_\pm = (1, \pm\mathrm{i}, 0, 0)/\sqrt2$ the circular polarisations of a wave travelling along $x_3$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $k$: A wave number: the momentum of a plane wave along $x_3$, $\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}$; in the cosmological perturbations the comoving wave number of a Fourier mode, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\beta_{\mathrm{g}}$: Any constant: the size of a gauge transformation, which adds a multiple of the wave vector to the polarisation vector of the photon. Unit: dimensionless. Status: STANDARD.
- $\theta_{\mathrm{r}}$: The angle of a rotation about the direction of motion of a wave. Unit: dimensionless (radian). Status: STANDARD.
- $\vec E$: The electric field of the photon on the fold: its component along the direction $x_i$ of ordinary space is $\partial A_4/\partial x_i - \partial A_i/\partial x_4$ ($i = 1, 2, 3$; $A_4$ and $A_i$ the components of $A_\mu$); $\vec E^2$ its square. Unit: GeV$^2$. Status: STANDARD.
- $\vec B$: The magnetic field of the photon on the fold, the curl of the components $A_1, A_2, A_3$ of $A_\mu$ along ordinary space (its component along $x_1$ is $\partial A_3/\partial x_2 - \partial A_2/\partial x_3$, and cyclically); $\vec B^2$ its square. Unit: GeV$^2$. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The photon as a wave: the zero mode for the combination of $W^3$ and $B$ that the Higgs vacuum leaves massless, a plane wave along $x_3$ with
the polarisation vector $\mathfrak{e}_\mu$. Its wave vector is null, so it satisfies Maxwell's equations of the fold. The Lorenz condition
requires $\mathfrak{e}_3 + \mathfrak{e}_4 = 0$, and a gauge transformation removes the remaining component along the direction of motion: the only
physical polarisations are the two transverse ones, along $x_1$ and along $x_2$. Its electric and magnetic fields are orthogonal to the
direction of motion and to each other and equal in size. Under a rotation by $\theta_{\mathrm{r}}$ about the direction of motion the circular
polarisations are multiplied by $\mathrm{e}^{\mp\mathrm{i}\theta_{\mathrm{r}}}$: helicity $\pm1$, a transverse wave of spin 1, as the order requires,
at the speed of light. A photon that leaves the fold travels through the bulk at the local speed of light, which at every depth is that
of the fold (FE-83). The massless vector of seven dimensions has five polarisations; the three that point along the extra times are the
components $A_r$, which UM-4 excludes (IN-7: they have kinetic terms of the wrong sign, `um4_bulk.py`, B11). Status: DERIVED
(`um4_bulk.py`, B3 and B11), ASSUMED (no components along the extra times).

$$
\begin{aligned}
&g_1^2 = \frac{3H\mathsf{g}_1^2}{2V_*},\qquad g_2^2 = \frac{3H\mathsf{g}_2^2}{2V_*},\qquad g_3^2 = \frac{3H\mathsf{g}_3^2}{2V_*},\qquad
 8\pi G_{\mathrm{N}} = \frac{\kappa_7}{V_*},\\
&g_{1,\mathrm{eff}} = \frac{g_1}{\sqrt{\mathcal{Z}}},\quad g_{2,\mathrm{eff}} = \frac{g_2}{\sqrt{\mathcal{Z}}},\quad g_{3,\mathrm{eff}} = \frac{g_3}{\sqrt{\mathcal{Z}}},\qquad \lambda_{\mathrm{eff}} = \frac{\lambda}{\mathcal{Z}},\qquad
 \mathcal{Y}_{\mathrm{eff}} = \frac{\mathcal{Y}}{\sqrt{\mathcal{Z}}},\qquad G_{\mathrm{N,eff}} = \frac{G_{\mathrm{N}}}{\mathcal{Z}},\\
&\mathcal{Z} = \frac{V_{\mathrm{t}}\big(\mathrm{e}^{-a_4}b_4\big)^3}{V_*}
\end{aligned} \tag{FE-44}
$$
<!-- symbols: g1, g2, g3, Hconst, gbulk, Vstar, pi, GN, kappa7, geff, Zfold, lameff, lamH, Yeff, Yuk, GNeff, Vt, euler, a4, b4 -->
<!-- begin generated symbol list -->
**Symbols in (FE-44).**

- $g_1$: The $U(1)_Y$ gauge coupling of the four-dimensional world (usually $g'$; not normalised for grand unification): the coupling of the massless mode of the hypercharge field of the bulk, $g_1^2 = 3H\mathsf{g}_1^2/(2V_*)$. Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling of the four-dimensional world (usually $g$): the coupling of the massless mode of the $SU(2)_L$ field of the bulk, $g_2^2 = 3H\mathsf{g}_2^2/(2V_*)$. Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling of the four-dimensional world (the strong coupling $g_s$): the coupling of the massless mode of the gluon field of the bulk, $g_3^2 = 3H\mathsf{g}_3^2/(2V_*)$. Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($g_3^2/(4\pi) = 0.1180$). Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathsf{g}_1,\ \mathsf{g}_2,\ \mathsf{g}_3$: The gauge couplings of eight dimensions of $U(1)_Y$, $SU(2)_L$ and $SU(3)_C$: the coefficients of the kinetic terms of the gauge fields of the bulk in their geometric normalisation; the four-dimensional couplings are $g_k^2 = 3H\mathsf{g}_k^2/(2V_*)$. Unit: GeV$^{-2}$ ($\mathsf{g}^2$: length$^4$). Status: ASSUMED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $g_{k,\mathrm{eff}}$: The effective (canonically normalised) gauge couplings of the fold when the fold factor is $\mathcal{Z}$, $g_{k,\mathrm{eff}} = g_k/\sqrt{\mathcal{Z}}$ ($k = 1, 2, 3$): the kinetic terms of the massless modes of the gauge fields of the bulk carry the volume of the extra times as the terms of the fold do. Unit: dimensionless. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold and the kinetic terms of the massless modes of the fields of the bulk; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $\lambda_{\mathrm{eff}}$: The effective quartic Higgs coupling, $\lambda/\mathcal{Z}$. Unit: dimensionless. Status: DERIVED.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $\mathcal{Y}_{\mathrm{eff}}$: The effective Yukawa matrices, $\mathcal{Y}/\sqrt{\mathcal{Z}}$ (for each of $\mathcal{Y}^{u}, \mathcal{Y}^{d}, \mathcal{Y}^{e}, \mathcal{Y}^{\nu}$). Unit: dimensionless. Status: DERIVED.
- $\mathcal{Y}^{u},\ \mathcal{Y}^{d},\ \mathcal{Y}^{e},\ \mathcal{Y}^{\nu}$: The Yukawa matrices ($3 \times 3$ complex matrices in generation space) of the up quarks, the down quarks, the charged leptons and the neutrinos. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{N,eff}}$: The effective Newton constant of the fold, $G_{\mathrm{N}}/\mathcal{Z}$. Unit: GeV$^{-2}$. Status: DERIVED.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

The four-dimensional couplings: the gauge couplings of the Standard Model are those of the massless modes, $g_k^2 = 3H\mathsf{g}_k^2/(2V_*)$
($k = 1, 2, 3$), and Newton's constant is that of the massless graviton; the couplings measured today follow when the volume of the extra
times is frozen ($\mathcal{Z} = 1$). Status: DERIVED (`um4_bulk.py`, B2; `um4_fold.py`, F2).

# The other fields of the bulk

$$
\begin{aligned}
&\phi_{\mathrm{bulk}} = u(\sigma)\,\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}:\qquad
u'' - 7H\,\mathrm{sgn}(\sigma)\,u' + \mathrm{e}^{2H\lvert\sigma\rvert}\,m^2\,u = 0,\qquad m^2 = \omega^2 - k^2,\\
&u_0 = 1,\quad \int_{-\infty}^{\infty}\mathrm{d}\sigma\,\mathrm{e}^{-5H\lvert\sigma\rvert}\,u_0^2 = \frac{2}{5H}
\end{aligned} \tag{FE-73}
$$
<!-- symbols: phibulk, uprof, sigma, euler, imag, kwave, x3, omegafreq, x4, prime, Hconst, sgn, mmass, infty, diff -->
<!-- begin generated symbol list -->
**Symbols in (FE-73).**

- $\phi_{\mathrm{bulk}}$: A massless scalar field of the bulk, $\nabla_M\nabla^M\phi_{\mathrm{bulk}} = 0$ (an illustration: each polarisation of the graviton obeys its equation). Unit: GeV$^3$. Status: STANDARD.
- $u(\sigma),\ u_0$: The profile along the hidden direction of a mode of a field of the bulk (a scalar, a gauge field or a polarisation of the graviton): the field is $u(\sigma)$ times a field of the fold; $u_0 = 1$ is the profile of the massless mode (the zero mode); in a propagator the response of the field to a unit source on the fold. Unit: dimensionless (a relative amplitude); length in a propagator. Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $k$: A wave number: the momentum of a plane wave along $x_3$, $\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}$; in the cosmological perturbations the comoving wave number of a Fourier mode, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

A massless scalar of the bulk (an illustration: each polarisation of the graviton obeys this equation): $\omega$ and $k$ enter only through
$m^2 = \omega^2 - k^2$, so every mode is a field of the fold with the Lorentz-invariant dispersion $\omega^2 = k^2 + m^2$; the zero mode has the
profile 1 and the kinetic weight $\mathrm{e}^{-5H\lvert\sigma\rvert}$ with the integral $2/(5H)$ and travels at the speed of light; the massive modes
are slower. Status: DERIVED (`um4_bulk.py`, B1).

$$
\begin{aligned}
&\Psi_{\mathrm{k}} = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\,\mathrm{e}^{-M_{\mathrm{k}}\lvert\sigma\rvert}\,\chi_0(x),\qquad
\gamma^{(0)}\chi_0 = -\chi_0,\qquad \gamma^{(a)}\,\partial_a\chi_0 = 0\quad(\text{along the fold}),\\
&\sqrt{\lvert g\rvert}\,\bar\Psi_{\mathrm{k}}\gamma^{x_4}\Psi_{\mathrm{k}} \propto \mathrm{e}^{(H - 2M_{\mathrm{k}})\lvert\sigma\rvert}
\end{aligned} \tag{FE-77}
$$
<!-- symbols: Psik, euler, Hconst, sigma, Mkink, chizero, xfour, gammaM, ia, partial, metric, x4 -->
<!-- begin generated symbol list -->
**Symbols in (FE-77).**

- $\Psi_{\mathrm{k}},\ \bar\Psi_{\mathrm{k}}$: A fermion field of the bulk with the kink mass $M_{\mathrm{k}}\,\mathrm{sgn}(\sigma)$ (an illustration, not a field of UM-4). Unit: GeV$^{7/2}$. Status: ASSUMED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $M_{\mathrm{k}}$: The mass of a fermion of the bulk that changes sign at the fold (a kink mass $M_{\mathrm{k}}\,\mathrm{sgn}(\sigma)$), used to illustrate the speeds of bulk fermions. Unit: GeV. Status: ASSUMED.
- $\chi_0$: The spinor of the fold of the massless mode of a fermion of the bulk: a solution of the massless Dirac equation of the fold of one chirality along $\sigma$. Unit: GeV$^{7/2}$. Status: DERIVED.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

A fermion of the bulk with a mass that changes sign at the fold (an illustration: UM-4 has no such field; it shows that quarks and leptons
could live in the bulk without outrunning light): its zero mode is a massless fermion of seven dimensions bound to the fold for
$M_{\mathrm{k}} > H/2$, at the speed of light (in UM-3 it moved at $2M_{\mathrm{k}}/(2M_{\mathrm{k}} - H)$ times the speed of light). Status: DERIVED
(`um4_bulk.py`, B6).

$$
\gamma^M\Omega_M = -\frac72\,H\,\mathrm{sgn}(\sigma)\,\gamma^{(0)} + \frac32\,\frac{b_4'}{b_4}\,\mathrm{e}^{H\lvert\sigma\rvert}\,\gamma^{(4)} \ne 0 \tag{FE-14}
$$
<!-- symbols: gammaM, iM, Omega, Hconst, sgn, sigma, b4, prime, euler -->
<!-- begin generated symbol list -->
**Symbols in (FE-14).**

- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The canonical spin connection of dirac16complex (the author's field of eight dimensions) for the metric of UM-4, with the author's
matrices: its first term is $-\frac72H\,\mathrm{sgn}(\sigma)\gamma^{(0)}$ (UM-3: $-3H\,\mathrm{sgn}(\sigma)\gamma^{(0)}$), and it is never identically zero.
Status: DERIVED (`um4_geometry.py`, G9).

$$
\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\,\chi(\sigma)\,\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)},\qquad
\gamma^{(0)}\chi' + \mathrm{e}^{H\lvert\sigma\rvert}\big(-\mathrm{i}\omega\,\gamma^{(4)} + \mathrm{i}\,\vec k\cdot\vec\gamma\big)\chi
 - m_\Psi\chi = 0\qquad(\sigma \ne 0) \tag{FE-36}
$$
<!-- symbols: Psi, euler, Hconst, sigma, chiprof, imag, kvec, xvec, omegafreq, x4, gammaM, prime, gammavec, mPsi -->
<!-- begin generated symbol list -->
**Symbols in (FE-36).**

- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\vec\gamma$: The three frame Dirac matrices of dirac16complex along ordinary space, $\vec\gamma = (\gamma^{(1)}, \gamma^{(2)}, \gamma^{(3)})$. Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->
<!-- symbols: -->

A mode of dirac16complex on the static block: the factor $\mathrm{e}^{(7/2)H\lvert\sigma\rvert}$ removes the first term of the spin connection, and
the factor $\mathrm{e}^{H\lvert\sigma\rvert}$ multiplies the whole Dirac operator of the fold, the frequency as well as the momentum (in UM-3 only the
momentum). Status: DERIVED (`um4_geometry.py`, G9).

$$
\mathsf{S} = \frac12\,\gamma^{(3)}\gamma^{(4)}:\qquad
\big[\mathsf{S}, \gamma^{(0)}\big] = \big[\mathsf{S}, \Gamma_8\big] = 0,\qquad
\big[\mathsf{S}, \gamma^{(3)}\big] = -\gamma^{(4)},\qquad \big[\mathsf{S}, \gamma^{(4)}\big] = -\gamma^{(3)}\qquad\Rightarrow\qquad
\omega^2 = \omega_0^2 + k^2 \tag{FE-78}
$$
<!-- symbols: Sboost, gammaM, Gamma8, omegafreq, omega0, kwave -->
<!-- begin generated symbol list -->
**Symbols in (FE-78).**

- $\mathsf{S}$: The generator of the boosts along $x_3$ on dirac16complex, $\mathsf{S} = \frac12\gamma^{(3)}\gamma^{(4)}$. Unit: dimensionless. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\omega_0$: The energy at rest (zero momentum along ordinary space and along the extra times) of a state of dirac16complex at the fold; complex for a resonance, $\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\Gamma_\chi$. Unit: GeV. Status: DERIVED.
- $k$: A wave number: the momentum of a plane wave along $x_3$, $\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}$; in the cosmological perturbations the comoving wave number of a Fourier mode, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

dirac16complex is invariant under the boosts of the fold: the generator $\mathsf{S}$ of the boosts along $x_3$, built from the author's
matrices, commutes with $\gamma^{(0)}$, with the chirality and with the mass term and rotates $\gamma^{(3)}$ and $\gamma^{(4)}$ into each other
hyperbolically, and the warp multiplies the frequency and the momentum by the same factor. Every state of dirac16complex at the fold with the
energy $\omega_0$ at rest therefore has $\omega^2 = \omega_0^2 + k^2$ exactly and moves slower than light (in UM-3 the bound states had the
speed coefficient $c_{\mathrm{b}}^2 = 1.19$ along ordinary space). Status: DERIVED (`um4_bulk.py`, B7, with the author's matrices).

$$
\begin{aligned}
&\chi' = \mathbb{K}\,\chi,\qquad \mathbb{K} = \gamma^{(0)}\big(m_\Psi + \mathrm{i}\omega\,\mathrm{e}^{H\lvert\sigma\rvert}\gamma^{(4)}\big),\qquad
\mathbb{K}^2 = \big(m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}\big)\mathbf{1},\\
&q = \sqrt{m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}},\qquad \lvert\omega\rvert\,\mathrm{e}^{H\sigma_{\mathrm{t}}} = m_\Psi
\end{aligned} \tag{FE-37}
$$
<!-- symbols: chiprof, prime, Kbulk, gammaM, mPsi, imag, omegafreq, euler, Hconst, sigma, identity, qdecay, sigmat -->
<!-- begin generated symbol list -->
**Symbols in (FE-37).**

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\mathbb{K}$: The transfer matrix of the profile equation at zero momentum, $\chi' = \mathbb{K}\chi$. Unit: GeV. Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathbf{1},\ \mathbf{1}_4,\ \mathbf{1}_8,\ \mathbf{1}_{16}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_4$, $\mathbf{1}_8$ and $\mathbf{1}_{16}$ are the identity matrices of 4, 8 and 16 rows. Unit: dimensionless. Status: STANDARD.
- $q$: The local decay rate of a profile of dirac16complex along $\sigma$ at the frequency $\omega$, $q = \sqrt{m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}}$ (imaginary beyond the turning point, where the profile oscillates). Unit: GeV. Status: DERIVED.
- $\sigma_{\mathrm{t}}$: The turning point of a state of dirac16complex of the frequency $\omega$: the depth at which the warped frequency equals the bulk mass, $\lvert\omega\rvert\mathrm{e}^{H\sigma_{\mathrm{t}}} = m_\Psi$; beyond it every solution oscillates. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The profile of dirac16complex at zero momentum: the local gap $m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}$ closes at the turning point
$\sigma_{\mathrm{t}}$, beyond which every solution oscillates. Because the time is warped, the warped frequency exceeds the bulk mass far from the
fold for every $\omega \ne 0$: there is no gap in the bulk and no normalisable state of non-zero frequency, and the states that UM-3 bound to
the fold are resonances in UM-4. Status: DERIVED (`um4_spectra.py`, U1).

$$
\begin{aligned}
&\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\,\Gamma_\chi,\qquad
\Gamma_\chi = p_{\mathrm{w}}\,m_\Psi\exp\Big(-2F(\upsilon_{\mathrm{b}})\,\frac{m_\Psi}{H}\Big),\qquad
p_{\mathrm{w}} \simeq \frac{2}{\mathrm{e}}\,\frac{q_{\mathrm{b}}^2}{m_\Psi^2},\\
&F(\upsilon) = \ln\frac{1 + \sqrt{1 - \upsilon^2}}{\upsilon} - \sqrt{1 - \upsilon^2},\qquad \upsilon_{\mathrm{b}} = \frac{\omega_{\mathrm{b}}}{m_\Psi}
\end{aligned} \tag{FE-86}
$$
<!-- symbols: omega0, omegar, imag, Gammachi, pw, mPsi, euler, Fwkb, upsilonr, omegab, Hconst, qb -->
<!-- begin generated symbol list -->
**Symbols in (FE-86).**

- $\omega_0$: The energy at rest (zero momentum along ordinary space and along the extra times) of a state of dirac16complex at the fold; complex for a resonance, $\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\Gamma_\chi$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{r}}$: The mass of the particle $\chi$: the real part of the energy at rest of the resonance of dirac16complex at the fold, $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$. Unit: GeV. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Gamma_\chi$: The width of the particle $\chi$ at rest: the rate of its decay into the waves of dirac16complex in the bulk. Unit: GeV. Value: below $1/(11.6\,t_0) = 1.3\times10^{-43}$ GeV for dark matter (a lifetime above 160 Gyr). Status: DERIVED.
- $p_{\mathrm{w}}$: The prefactor of the width of the particles $\chi$, $\Gamma_\chi = p_{\mathrm{w}}m_\Psi\mathrm{e}^{-2F(\upsilon_{\mathrm{b}})m_\Psi/H}$: $p_{\mathrm{w}} \simeq (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ to the leading order in $H/q_{\mathrm{b}}$ (FE-86; 0.184 for $q_{\mathrm{b}} = m_\Psi/2$). Unit: dimensionless. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $F(\upsilon)$: The tunnelling exponent of the width of the particles $\chi$ per unit of $m_\Psi/H$: the integral of the local decay rate $q$ over the region inside the turning point, divided by $m_\Psi/H$, as a function of the ratio $\upsilon$ of the energy to the bulk mass. Unit: dimensionless. Value: 0.049 for $\upsilon = 0.866$; $(q_{\mathrm{b}}/\omega_{\mathrm{b}})^3/3$ for weak binding. Status: DERIVED.
- $\upsilon,\ \upsilon_{\mathrm{b}},\ \upsilon_{\mathrm{r}}$: The argument of the tunnelling exponent $F$, a ratio of an energy to the bulk mass $m_\Psi$; $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ that of the particle $\chi$ in the limit $H/q_{\mathrm{b}} \to 0$, $\upsilon_{\mathrm{r}} = \omega_{\mathrm{r}}/m_\Psi$ that of the real part of its resonance. Unit: dimensionless. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The resonances of dirac16complex at the fold: complex energies with the real part $\omega_{\mathrm{r}}$ (the mass of the particle $\chi$) and the
width $\Gamma_\chi$, the rate of the tunnelling through the region inside the turning point, whose exponent is $2F(\upsilon_{\mathrm{b}})m_\Psi/H$;
the prefactor $p_{\mathrm{w}} \simeq (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ follows from the exact solutions for large $m_\Psi/H$ (0.184 for
$q_{\mathrm{b}} = m_\Psi/2$, 0.721 for $q_{\mathrm{b}} = 0.99\,m_\Psi$). A particle $\chi$ of the dark matter must live longer than 160 Gyr, 11.6 times the age
$t_0 = 13.8$ Gyr of the universe (the bound on the lifetime of dark matter that decays into invisible relativistic particles: B. Audren,
J. Lesgourgues, G. Mangano, P. D. Serpico and T. Tram, JCAP 12 (2014) 028, arXiv:1407.2418), $\Gamma_\chi < 1.3\times10^{-43}$ GeV. With $H$ at its
lower bound of 2534 GeV (FE-82) this requires $m_\Psi/H > 1135$ and $\omega_{\mathrm{b}} > 2.5\times10^6$ GeV for $q_{\mathrm{b}} = m_\Psi/2$, and
$m_\Psi/H > 1.72\times10^5$ and $\omega_{\mathrm{b}} > 4.3\times10^8$ GeV for the weak binding $q_{\mathrm{b}}/\omega_{\mathrm{b}} = 0.1$; the bounds fall with
the binding, to $m_\Psi/H > 33.1$ and $\omega_{\mathrm{b}} > 1.2\times10^4$ GeV for $q_{\mathrm{b}} = 0.99\,m_\Psi$. Status: DERIVED (`um4_spectra.py`, U3 and
U4: the exponent and the prefactor of the exact widths; `um4_kohnsham.py`, K8: the tunnelling exponent at the resonance exceeds
$2F(\upsilon_{\mathrm{b}})m_\Psi/H$ by 1.002), ESTIMATE (the bounds, U6, with the measured lifetime as input).

# From one point of the fold to another

$$
-\mathrm{e}^{nH\lvert\sigma\rvert}\,\partial_\sigma\big(\mathrm{e}^{-nH\lvert\sigma\rvert}\,\partial_\sigma u\big)
 + \mathrm{e}^{2H\lvert\sigma\rvert}\,\mathsf{p}^2\,u = \delta_{\mathrm{D}}(\sigma),\qquad
\mathbb{G}_n(\mathsf{p}) = u(0) = \frac{\mathrm{K}_{n/2}(\mathsf{p}/H)}{2\mathsf{p}\,\mathrm{K}_{n/2-1}(\mathsf{p}/H)} \tag{FE-79}
$$
<!-- symbols: euler, inn, Hconst, sigma, partial, isigma, uprof, psE, deltaD, Gprop, BesselK -->
<!-- begin generated symbol list -->
**Symbols in (FE-79).**

- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $n$: The label of a field of the bulk in its profile equation: the exponent of the weight $\mathrm{e}^{-nH\lvert\sigma\rvert}$ of its $\sigma$-derivatives, $n = 7$ for a scalar and for each polarisation of the graviton, $n = 5$ for a gauge field. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\sigma$: The label $\sigma$ in $\partial_\sigma$: the derivative with respect to the proper hidden coordinate $\sigma$. Status: STANDARD.
- $u(\sigma),\ u_0$: The profile along the hidden direction of a mode of a field of the bulk (a scalar, a gauge field or a polarisation of the graviton): the field is $u(\sigma)$ times a field of the fold; $u_0 = 1$ is the profile of the massless mode (the zero mode); in a propagator the response of the field to a unit source on the fold. Unit: dimensionless (a relative amplitude); length in a propagator. Status: DERIVED.
- $\mathsf{p}$: The Euclidean momentum along the fold of a source on the fold: $\mathsf{p}^2$ the square of its seven-dimensional momentum (for a static source spread uniformly over the extra times the square of its momentum along ordinary space); $\mathsf{p} = -\mathrm{i}m$ for a time-like momentum of the mass $m$ with outgoing waves into the bulk. Unit: GeV. Status: STANDARD.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\mathbb{G}_n,\ \mathbb{G}_7,\ \mathbb{G}_5$: The propagator of a massless field of the bulk from one point of the fold to another, in the momentum space of the fold: the value at the fold of its response to a unit source on the fold; $\mathbb{G}_7$ for each polarisation of the graviton and for a scalar, $\mathbb{G}_5$ for a gauge field. Unit: GeV$^{-1}$. Status: DERIVED.
- $\mathrm{K}$: The modified Bessel function of the second kind (of the order written as its subscript): the solution of the modified Bessel equation that decays exponentially for a large argument; for a half-integer order it is an exponential times a polynomial in the inverse of the argument, which makes the propagators of the bulk rational functions. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The response of a massless field of the bulk to a unit source on the fold, for the Euclidean momentum $\mathsf{p}$ along the fold: the
propagator of the bulk from one point of the fold to another ($n = 7$ for the graviton and a scalar, $n = 5$ for a gauge field). For small
momenta it is the massless propagator of the fold with the strength $\frac52H$ for the graviton and $\frac32H$ for a gauge field. Status:
DERIVED (`um4_propagators.py`, P1).

$$
\begin{aligned}
&\mathbb{G}_7 = \frac{H}{2\mathsf{p}^2}\,\frac{x_{\mathrm{p}}^3 + 6x_{\mathrm{p}}^2 + 15x_{\mathrm{p}} + 15}{x_{\mathrm{p}}^2 + 3x_{\mathrm{p}} + 3}
 = \frac{5H}{2\mathsf{p}^2}\Big(1 + \frac{x_{\mathrm{p}}^2}{15} - \frac{x_{\mathrm{p}}^4}{45} + \frac{x_{\mathrm{p}}^5}{45} + \dots\Big),\\
&\mathbb{G}_5 = \frac{H}{2\mathsf{p}^2}\,\frac{x_{\mathrm{p}}^2 + 3x_{\mathrm{p}} + 3}{x_{\mathrm{p}} + 1}
 = \frac{3H}{2\mathsf{p}^2}\Big(1 + \frac{x_{\mathrm{p}}^2}{3} - \frac{x_{\mathrm{p}}^3}{3} + \dots\Big),\qquad x_{\mathrm{p}} = \frac{\mathsf{p}}{H}
\end{aligned} \tag{FE-80}
$$
<!-- symbols: Gprop, Hconst, psE, xp -->
<!-- begin generated symbol list -->
**Symbols in (FE-80).**

- $\mathbb{G}_n,\ \mathbb{G}_7,\ \mathbb{G}_5$: The propagator of a massless field of the bulk from one point of the fold to another, in the momentum space of the fold: the value at the fold of its response to a unit source on the fold; $\mathbb{G}_7$ for each polarisation of the graviton and for a scalar, $\mathbb{G}_5$ for a gauge field. Unit: GeV$^{-1}$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathsf{p}$: The Euclidean momentum along the fold of a source on the fold: $\mathsf{p}^2$ the square of its seven-dimensional momentum (for a static source spread uniformly over the extra times the square of its momentum along ordinary space); $\mathsf{p} = -\mathrm{i}m$ for a time-like momentum of the mass $m$ with outgoing waves into the bulk. Unit: GeV. Status: STANDARD.
- $x_{\mathrm{p}}$: The Euclidean momentum along the fold in units of $H$, $x_{\mathrm{p}} = \mathsf{p}/H$. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

For the half-integer orders of the Bessel functions the propagators are rational functions of $x_{\mathrm{p}} = \mathsf{p}/H$. In the expansions
for small momenta the even powers are contact interactions between the sources on the fold; the first odd power ($x_{\mathrm{p}}^5$ for gravity,
$x_{\mathrm{p}}^3$ for a gauge field) gives a correction of long range. Status: DERIVED (`um4_propagators.py`, P2).

$$
\mathcal{V}_7(r) = \frac{5H}{8\pi r}\Big[1 + \frac{16}{15\pi}\,\frac{1}{(Hr)^5} + \dots\Big],\qquad
\mathcal{V}_5(r) = \frac{3H}{8\pi r}\Big[1 + \frac{4}{3\pi}\,\frac{1}{(Hr)^3} + \dots\Big] \tag{FE-81}
$$
<!-- symbols: Vstat, rrad, Hconst, pi -->
<!-- begin generated symbol list -->
**Symbols in (FE-81).**

- $\mathcal{V}_7(r),\ \mathcal{V}_5(r)$: The static potentials between two unit point sources on the fold at the distance $r$ (spread uniformly over the extra times) from the exchange of the graviton ($\mathcal{V}_7$) and of a gauge field ($\mathcal{V}_5$) of the bulk: the three-dimensional Fourier transforms of $\mathbb{G}_7$ and $\mathbb{G}_5$. Unit: GeV$^2$. Status: DERIVED.
- $r$: A distance from a centre: the distance from the centre of the star along the path of a neutrino; in Newton's and Coulomb's laws the distance between two point sources on the fold. Unit: length. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

Newton's law (the first potential, multiplied by the gravitational coupling) and Coulomb's law (the second, multiplied by the square of the
gauge coupling) between two point sources on the fold: the massive modes of the bulk add the relative corrections $0.3395/(Hr)^5$ and
$0.4244/(Hr)^3$. Newton's law was tested by torsion balances at separations from 52 micrometres to 3 mm (J. G. Lee, E. G. Adelberger,
T. S. Cook, S. M. Fleischer and B. R. Heckel, Phys. Rev. Lett. 124 (2020) 101101, which excludes Yukawa forces of gravitational strength
with a range above 38.6 micrometres); taken to hold to one per cent at 52 micrometres, it requires $H > 7.7\times10^{-3}$ eV. For the
bound $H > 2534$ GeV of FE-82 the corrections are $2.6\times10^{-75}$ at 52 micrometres and $1.4\times10^{-27}$ for Coulomb's law at the Bohr
radius: unobservable. Status: DERIVED (`um4_propagators.py`, P3), ESTIMATE (the factor of order one of the tensor structure of the massive
gravitons; the bounds).

$$
\Big(1 + M_{\mathrm{loc}}^2\,\mathbb{G}_5(\mathsf{p})\Big)\Big\vert_{\mathsf{p} = -\mathrm{i}m} = 0:\qquad
m^2 = m_0^2\Big(1 - \frac{m_0^2}{3H^2}\Big) - \mathrm{i}\,\frac{m_0^5}{3H^3} + \dots,\qquad
m_0^2 = \frac32\,H M_{\mathrm{loc}}^2,\qquad \Gamma_{\mathrm{bulk}} = \frac{m_0^4}{3H^3} \tag{FE-82}
$$
<!-- symbols: Mloc, Gprop, psE, imag, mmass, mzero, Hconst, Gammabulk -->
<!-- begin generated symbol list -->
**Symbols in (FE-82).**

- $M_{\mathrm{loc}}$: The mass term that the Higgs vacuum on the fold gives a gauge field of the bulk: $M_{\mathrm{loc}}^2\delta_{\mathrm{D}}(\sigma)$ in its profile equation; for the W, $M_{\mathrm{loc}}^2 = \mathsf{g}_2^2(v^2 + \mathcal{A}^2)/(4V_*)$. Unit: GeV$^{1/2}$ ($M_{\mathrm{loc}}^2$ in GeV). Status: DERIVED.
- $\mathbb{G}_n,\ \mathbb{G}_7,\ \mathbb{G}_5$: The propagator of a massless field of the bulk from one point of the fold to another, in the momentum space of the fold: the value at the fold of its response to a unit source on the fold; $\mathbb{G}_7$ for each polarisation of the graviton and for a scalar, $\mathbb{G}_5$ for a gauge field. Unit: GeV$^{-1}$. Status: DERIVED.
- $\mathsf{p}$: The Euclidean momentum along the fold of a source on the fold: $\mathsf{p}^2$ the square of its seven-dimensional momentum (for a static source spread uniformly over the extra times the square of its momentum along ordinary space); $\mathsf{p} = -\mathrm{i}m$ for a time-like momentum of the mass $m$ with outgoing waves into the bulk. Unit: GeV. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $m_0$: The mass of the W or the Z boson without the massive modes of the bulk (the mass of the massless mode with the Higgs vacuum), $m_0^2 = \frac32HM_{\mathrm{loc}}^2$; $m_0^2 = g_2^2(v^2 + \mathcal{A}^2)/4$ for the W. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\Gamma_{\mathrm{bulk}}$: The width of the W or the Z boson into the bulk (its decay into the massive modes of the gauge fields of the bulk), $\Gamma_{\mathrm{bulk}} = m_0(m_0/H)^3/3$. Unit: GeV. Value: 1.42 MeV for the Z and 0.85 MeV for the W at $H = 2534$ GeV. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The W and Z bosons: the Higgs vacuum on the fold gives the gauge fields of the bulk a mass term concentrated on the fold, and the pole of the
propagator lies at a complex mass: the W and the Z are resonances of the bulk, with the width $\Gamma_{\mathrm{bulk}} = m_0(m_0/H)^3/3$ into the bulk
($m_0$ the mass that the zero mode alone would have, $m_0^2 = g_2^2(v^2 + \mathcal{A}^2)/4$ for the W and
$(g_1^2 + g_2^2)(v^2 + \mathcal{A}^2)/4$ for the Z, with the Higgs vacuum value $v$ and the ad hoc component $\mathcal{A}$ of the author's vacuum);
the massive modes shift the squared mass by $-m_0^4/(3H^2)$. A Z boson that decays into the bulk leaves the fold unseen and adds to its
invisible width. The number of light neutrinos measured at the Z, $2.9963 \pm 0.0074$, with the width 167.2 MeV of the Z into one neutrino
and its antineutrino, allows at most 1.42 MeV of extra invisible width (95 per cent, one-sided), so
$H > m_{\mathrm{Z}}\big(m_{\mathrm{Z}}/(3\cdot1.42\ \mathrm{MeV})\big)^{1/3} = 2534$ GeV ($m_{\mathrm{Z}}$ the mass of the Z; about 2.5 TeV). At this bound the
width of the W into the bulk is 0.85 MeV. Status: DERIVED (`um4_propagators.py`, P4: the complex pole, whose deviations from the formulas
are $1.83(m_0/H)^2$ of the imaginary part and $0.44(m_0/H)^4$ of the real part), ESTIMATE (the bounds, P5).

| bound on $H$ | from | value |
| ------ | ------ | ------ |
| invisible width of the Z boson | its decay into the bulk, $\Gamma_{\mathrm{bulk}} < 1.42$ MeV (the measured number of light neutrinos $2.9963 \pm 0.0074$, P. Janot and S. Jadach, Phys. Lett. B 803 (2020) 135319, with 167.2 MeV per neutrino species; the exact pole gives 1.414 MeV, the formula 1.417 MeV) | $H > 2534$ GeV (about 2.5 TeV) |
| contact interactions between quarks and leptons | the contact term $x_{\mathrm{p}}^2/3$ of the propagator of the photon (with the charge $2/3$ of the up quark) against the limit $\Lambda_{\mathrm{CI}} > 26.0$ TeV of ATLAS for the destructive left-left structure in the spectra of electron and muon pairs (JHEP 11 (2020) 005; the photon exchange is a vector-vector interaction, so this is an estimate) | $H > 1083$ GeV (1327 GeV with unit charges) |
| the parameter rho of the electroweak fits | the shift $-m_0^4/(3H^2)$ of the squared masses of the W and Z, against $1.00031 \pm 0.00019$ (Particle Data Group 2024) | $H > 969$ GeV |
| Newton's law at 52 micrometres | the correction $0.3395/(Hr)^5$, taken to be below one per cent at 52 micrometres, the shortest separation of the torsion balances of J. G. Lee et al. (Phys. Rev. Lett. 124 (2020) 101101) | $H > 7.7\times10^{-3}$ eV |

All four are ESTIMATE ($\Lambda_{\mathrm{CI}}$ is the scale of a contact interaction, $r$ the distance between the sources). The strongest, the
invisible width of the Z boson, is the bound used in every UM-4 document.

# Causality around an expanding fold

$$
c_{\mathrm{loc}}(\sigma) = 1 - \frac{a_4''}{5H^2}\big(\mathrm{e}^{2H\lvert\sigma\rvert} - 1\big),\qquad
\sigma(x_3) = \frac{\lvert a_4''\rvert}{5H}\,x_3\,(L - x_3),\qquad
\Delta x_4 = L - \frac{a_4''^2L^3}{150H^2} \tag{FE-84}
$$
<!-- symbols: cloc, sigma, a4, prime, Hconst, euler, x3, Ldist, Delta, x4 -->
<!-- begin generated symbol list -->
**Symbols in (FE-84).**

- $c_{\mathrm{loc}}$: The coordinate speed of light along $x_3$ at the depth $\sigma$ (the rate of change of $x_3$ with $x_4$ along a null line at fixed $\sigma$), in units of that on the fold: $\mathrm{e}^{H\lvert\sigma\rvert}$ on the static block of UM-3, whose time was not warped, 1 on the static block of UM-4, and on an expanding fold of UM-4 different from 1 in proportion to the second derivative $a_4''$ of $a_4$ (the rate of change of the expansion rate $a_4'$). Unit: dimensionless. Status: DERIVED.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $L$: A distance between two points of the fold along ordinary space: for a gravitational wave the radius of a ring of free test masses ($\Delta L$ the change of the distance of one of them from the centre), for a signal the distance between its emitter and its receiver. Unit: length. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

An expanding fold with frozen extra times: the coordinate speed of light $c_{\mathrm{loc}}$ along $x_3$ at the depth $\sigma$ differs from 1 in
proportion to the second derivative $a_4'' = H_4' = -(1 + q_{\mathrm{dec}})H_4^2$ of the logarithm of the scale factor ($H_4 = a_4'$ the expansion
rate, $q_{\mathrm{dec}} = -1 - a_4''/a_4'^2$ the deceleration parameter). Wherever the expansion rate falls ($a_4'' < 0$, i.e. $q_{\mathrm{dec}} > -1$:
the eras of radiation and of matter, and also today, $q_{\mathrm{dec}} = -0.55$) the light cone of the bulk is slightly wider than that of the
fold, and the path that gains the most between two points of the fold at the distance $L$ (small compared with $1/H_4$) is the parabola of
the second relation, which arrives earlier than light along the fold by $a_4''^2L^3/(150H^2)$. Extrapolated to the Hubble distance today (an
order of magnitude) this is $4.4\times10^{-94}$ of the travel time for $H = 2534$ GeV ($3\times10^{-63}$ even for $H = 10^{-3}$ eV): the bulk is
ahead of light on the fold, but by an unobservable amount. Where the expansion rate grows ($a_4'' > 0$) the path along the fold is the fastest,
and on the static fold no signal at fixed extra times is ahead at all (FE-83). Status: DERIVED (`um4_causality.py`, C2: the speed from the
metric of the fold; C3: the numerical minimisation of the travel time gives 0.997 of the formula, and no advance where $a_4'' > 0$).

# What the change of the metric changes elsewhere

The warped time changes more than the speeds of the fields of the bulk. Each item is derived in the field equations of UM-4 and in
their programs; the values are those of UM-4.

* **Gravity on the fold** is general relativity: the Einstein equations of seven dimensions with $\kappa_7 = 5\kappa H/2$ (FE-71), with
  frozen extra times the Friedmann equations, gravitational waves at the speed of light at every wavelength (FE-63). The order of the
  corrections is $(a_4'/H)^2$. Status: DERIVED.
* **The tension of the fold** is $\kappa\lambda_{\mathrm{F}} = 12H$ (FE-30), in the four-dimensional normalisation
  $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV ($M_{\mathrm{red}}$ the reduced Planck mass): the
  observed dark energy, $2.5\times10^{-47}$ GeV$^4$, needs it tuned to $2.2\times10^{-92}$, one part in $10^{92}$, the cosmological-constant
  problem of the brane of Randall and Sundrum. Status: DERIVED (`um4_foldsources.py`, FS4: the value), OPEN (the tuning).
* **The bulk needs no stabiliser.** With Einstein gravity and $\Lambda = -21H^2$ the static block is a vacuum (FE-32); UM-3 needed either a
  stabiliser of the bulk (with the author's original weights) or the degenerate weights $(1, 1/20, 1/360)$. Status: DERIVED.
* **The author's vacuum** $a_4 = Hx_4$ with constant $b_4$ is not a solution of UM-4 (as a fold with matter it would need a negative energy
  density). Status: DERIVED (`um4_primordial.py`, PR0).
* **The states of dirac16complex at the fold** are resonances, not bound states (FE-86): the particles $\chi$ of the dark matter live longer
  than 160 Gyr only if $m_\Psi/H$ is large, so with $H \ge 2534$ GeV they are heavier than $2.5\times10^6$ GeV for the binding
  $q_{\mathrm{b}} = m_\Psi/2$; only a strong binding lowers the bound ($1.2\times10^4$ GeV for $q_{\mathrm{b}} = 0.99\,m_\Psi$). A thermal relic
  needs a mass below the unitarity bound of $9.7\times10^4$ GeV, which the lifetime allows only for a binding stronger than about
  $q_{\mathrm{b}} = 0.9\,m_\Psi$; for weaker bindings the abundance needs a non-thermal origin. Bound to the fold by the Higgs portal or by the
  gluon condensate the particles cannot both live long enough and escape direct detection: the dark matter of UM-4 needs a binding of $\chi$
  to the fold that does not couple it to nucleons. Status: DERIVED, ESTIMATE (`um4_spectra.py`, U6; `um4_thermal.py`, T7 to T9), OPEN (the
  binding and the origin).
* **Inflation** of the fold in the regime of general relativity needs a rate below $H/10$; with $H = 2534$ GeV only a rate below 253 GeV
  (an energy scale below $3.3\times10^{10}$ GeV), far below the rates of the usual models of inflation (Higgs inflation, with a curvature
  coupling that the action of UM-4 does not contain, would need $H > 1.6\times10^{14}$ GeV). Status: DERIVED, ESTIMATE (`um4_primordial.py`,
  PR2 to PR4), OPEN (the inflaton).
* **The extra times** remain time-like: every field with a momentum along them larger than its mass and its momentum along ordinary space is
  tachyonic, in the bulk as on the fold (a smaller one is a rotation of the state at rest), and UM-4 keeps only fields without such a
  momentum; a gauge principle that removes it is needed. Status: DERIVED (`um4_extratimes.py`, EX1 to EX5), OPEN (the principle).

# What is open

* The origin of the tension of the fold, its tuning to one part in $10^{92}$ against the observed dark energy, and the origin of the pressure
  along the extra times that holds their volume fixed.
* The three vector polarisations $h_{\mu r}$ of the graviton of the bulk, which are ghosts; the matter of the fold does not emit them at the
  linear order, but nothing yet forbids them at higher orders.
* The projected Weyl tensor of the bulk that an expanding fold with matter other than radiation requires at the order of the square of its
  energy density divided by the tension (`um4_fold.py`, F6), and the bulk solution that would fix it.
* A gauge principle that removes the momentum of every field along the extra times.
* A binding of the particles $\chi$ of dirac16complex to the fold that does not couple them to nucleons, and a non-thermal origin of their
  abundance.
* The inflaton of the fold.

# What was verified

Every statement labelled DERIVED in this document is verified by a program of UM-4 (Python with sympy for the exact algebra and with
numpy and scipy for the numerics; every program runs in less than 423 seconds). The checks that this document cites, all passed:

| program | checks | what they verify |
| ------ | ------ | ------ |
| `um4_geometry.py` | G1 to G11 | the proper chart, the exact curvature, the static block of constant curvature, the Lovelock tensors, the bulk equations, the Ricci-flat folds, the pure tension, the light cone of every slice, the spin connection with the author's matrices, the static warps and their vacua, the matrices of FD-13 in the definition of the fold |
| `um4_gravity.py` | L1 to L4 | the vacua of the static family, the graviton around the static block for any weights, the light cone on every background only for Einstein gravity, the choice of UM-4 |
| `um4_bulk.py` | B1 to B7, B9 to B11 | the scalar, the photon, the transverse photon of spin 1, the graviton, the plus and cross polarisations of spin 2, the bulk fermion, the boost invariance of dirac16complex, the speeds of UM-3 recomputed, the continuum of massive modes from zero mass, the signs of the kinetic terms of the 14 polarisations of the graviton and of the components of a gauge field (the ghost vectors $h_{\mu r}$) |
| `um4_fold.py` | F1 to F6 | the bulk metric of an expanding fold, the Einstein equations of seven dimensions on the fold, the exact equations of the fold, the Friedmann equations, the size of the corrections, the Weyl term |
| `um4_foldsources.py` | FS1 to FS5 | the tension, the gravitational waves of the fold, the induced gravity, the tuning of the tension, the fold fluid |
| `um4_propagators.py` | P1 to P5 | the propagators of the bulk, their expansions, Newton's and Coulomb's laws, the W and Z resonances, the bounds on $H$ |
| `um4_causality.py` | C1 to C4 | no shortcut through the static bulk at fixed extra times and the null lines along an extra time, the light cone of an expanding fold, the largest advance, the closed time-like curves |
| `um4_spectra.py` | U1 to U8 | the resonances of dirac16complex, their widths, their dispersion, their lifetime, their Krein signature and mirror symmetry |

# Further symbols

<!-- further symbols: Mred, is, P7, SigmaGen, Aadhoc, nabla, rho7, omegaSC, mferm, mh, q7, tgen, vev, vloc, GF, Christoffel, Phi, trace, vA, Tany, Wwarp, cb, mZ, Lfold -->
<!-- begin generated symbol list -->
**Further symbols.** These symbols appear in the definitions of the symbols listed after the equations of this document.

- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $s$: A second extra-time direction of the fold (as $r$, different from it). Status: STANDARD.
- $P_7$: The pressure along ordinary space of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(i)}{}_{(i)}$). Unit: GeV$^7$. Status: DERIVED.
- $\Sigma^{ab},\ \Sigma^{\mu\nu}$: The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.
- $\rho_7$: The energy density of the matter of the fold above its tension in the seven-dimensional normalisation (minus the component $\mathsf{t}^{(4)}{}_{(4)}$: an energy per unit volume of the six other directions of the fold); $V_*\rho_7$ in the four-dimensional normalisation. Unit: GeV$^7$. Status: DERIVED.
- $\varpi_{Mab}$: The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$. Unit: 1/length. Status: STANDARD.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-4 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 23 meV by DESI DR2 with the CMB and NuFIT 6.0. Status: STANDARD.
- $m_h$: The mass of the Higgs boson. Unit: GeV. Value: 125.25 GeV (Particle Data Group 2022). Status: STANDARD.
- $q_7$: The pressure along the extra times of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(r)}{}_{(r)}$). Unit: GeV$^7$. Status: DERIVED.
- $t^A$: The generators of $SU(3)$ on colour triplets, $t^A$: half the Gell-Mann matrices, with $\mathrm{tr}(t^At^B) = \delta^{AB}/2$. Unit: dimensionless. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.
- $G_{\mathrm{F}}$: The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in the equations of the neutrino flavours it stands for the local Fermi constant of the ad hoc vacuum. Unit: GeV$^{-2}$. Value: $1.1664\times10^{-5}$ GeV$^{-2}$. Status: STANDARD.
- $\Gamma^P{}_{MN}$: The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection). Unit: 1/length. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $v_{\mathcal{A}}$: The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc, $\mathrm{e}^{-2a_{40}x_4}$ (written Exp[-2 a40 x4] in his notebook), has $v_{\mathcal{A}} = 1$ in the units of his notebook. Unit: GeV. Value: 1 in the units of the author's notebook; UM-4 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$). Status: AUTHOR (the form), ASSUMED (a free amplitude).
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{W}$: The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-4 the function of $\sigma$ that multiplies all seven directions of the fold, ordinary space, the time and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold. Unit: dimensionless. Status: DERIVED.
- $c_{\mathrm{b}}$: The speed coefficient of the particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum $\omega^2 = \omega_0^2 + c_{\mathrm{b}}^2\vec k^2$. In UM-3, whose time was not warped, $c_{\mathrm{b}}^2 = 1.19$ for $H = 0.05\,m_\Psi$ and $q_{\mathrm{b}} = 0.3\,m_\Psi$ (faster than light); in UM-4 the boosts of the fold are a symmetry and $c_{\mathrm{b}} = 1$ exactly. Unit: dimensionless. Value: 1 in UM-4; 1.09 in UM-3. Status: DERIVED.
- $m_{\mathrm{Z}}$: The mass of the Z boson. Unit: GeV. Value: 91.19 GeV ($\mathcal{A} = 0$). Status: STANDARD.
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->
