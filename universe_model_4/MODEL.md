---
title: "UM-4 model"
subtitle: 'The universe model UM-4: the author''s spacetime of eight dimensions with the time warped like every other direction of the fold, the fields and where they live, the complete action, and every parameter'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Formulated and verified by Claude (Anthropic)"
  - "Model of UM-4, 2026-10-25"
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
$\cot = \cos/\sin$ the trigonometric functions, $\sinh$ and $\tanh$ the hyperbolic functions, $\lvert y\rvert$ the absolute value;
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2.5$ TeV. Status: DERIVED.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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
- $y_{\mathrm{RS}}$: The proper coordinate across the brane of the five-dimensional model of Randall and Sundrum (FD-8, an example, not UM-4). Unit: length. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $k_{\mathrm{RS}}$: The inverse curvature length of the bulk of the model of Randall and Sundrum: the warp factor of the brane is $\mathrm{e}^{-2k_{\mathrm{RS}}\lvert y_{\mathrm{RS}}\rvert}$ (FD-8, an example, not UM-4). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\lambda_{\mathrm{RS}}$: The tension (energy per unit volume of ordinary space) of the brane of the model of Randall and Sundrum, $\lambda_{\mathrm{RS}} = 6k_{\mathrm{RS}}/\kappa_5$ (FD-8, an example, not UM-4). Unit: GeV$^4$. Status: STANDARD.
- $\kappa_5$: The gravitational coupling of five dimensions in the model of Randall and Sundrum, $8\pi$ times the Newton constant of five dimensions (FD-8, an example, not UM-4). Unit: GeV$^{-3}$. Status: STANDARD.
- $\Lambda_{\mathrm{RS}}$: The vacuum energy density of the bulk of the model of Randall and Sundrum, $\Lambda_{\mathrm{RS}} = -6k_{\mathrm{RS}}^2/\kappa_5$ (FD-8, an example, not UM-4). Unit: GeV$^5$. Status: STANDARD.

<!-- end generated symbol list -->

   has a fold at $y_{\mathrm{RS}} = 0$ with the properties 1 to 3 (its coordinate $y_{\mathrm{RS}}$ is already the proper
   distance, so property 4 does not arise); Einstein's equations require there a brane of the tension $\lambda_{\mathrm{RS}}$
   (Israel's junction condition) and in the bulk the vacuum energy $\Lambda_{\mathrm{RS}}$, and the bulk is otherwise empty. The
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
- $\Gamma_\chi$: The width of the particle $\chi$ at rest: the rate of its decay into the waves of dirac16complex in the bulk. Unit: GeV. Value: below $1/t_0 = 1.5\times10^{-42}$ GeV for dark matter. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
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
   state is a resonance of the width $\Gamma_\chi$, which falls like $\mathrm{e}^{-2F(\upsilon_{\mathrm{b}})m_\Psi/H}$ with
   $F(\upsilon) = \ln((1 + \sqrt{1 - \upsilon^2})/\upsilon) - \sqrt{1 - \upsilon^2}$ and $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ (the
   tunnelling through the region between the fold and $\sigma_{\mathrm{t}}$). The profile is not a function of $\lvert\sigma\rvert$: it
   jumps at the fold, $\chi(0^+) \ne \chi(0^-)$.
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
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

   ($T_a$ the author's Dirac matrices; for states at rest $\mathsf{R}_1$ is the reflection across the fold combined with the
   reflection of ordinary space, $\mathsf{R}_2$ the reflection across the fold combined with the reflection of the extra
   times). The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a
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

This document defines the universe model UM-4, ordered by the author on 2026-10-25 at 13:15 PDT: in UM-3 anything that propagated in
the bulk outran light on the fold, because the time $x_4$ of the author's metric was not warped while ordinary space and the extra
times were (bulk scalars moved 1.22 times, bulk photons 1.41 times as fast as light on the fold). The author ordered "a new metric
model in which x4 is warped like the other directions", in which "both photons and gravitons actually propagate at c in the bulk",
photon waves are transverse spin-1 waves and gravitational waves are spin-2 waves with the "plus" and "cross" polarisations, and he
ordered that UM-3 be kept and UM-4 placed in new folders. This document gives the spacetime and its metric, the fields and where
they live, the complete action from which every field equation follows, and every parameter with its value and its origin. It is
self-contained: every equation is written out (the terms of the action carry the tags IN-1 to IN-16 and the metric the tag FE-27,
the same tags as in every UM-4 document), and every symbol of every display equation is defined right after it; a symbol that one
of these definitions uses is defined in this document as well.

## The status labels

Every equation and every parameter carries one of the labels **AUTHOR** (from the author: his notebooks `4+4.nb` and
`Dirac_Einstein-Lovelock_4+4_Nash.nb` and his orders of 2026-10-24 and 2026-10-25, the warped time among them), **RECORD** (from the
record of this repository: the Lagrangian of dirac16complex with its canonical spin connection and its contact self-interaction, the
Kohn-Sham treatment), **STANDARD** (textbook physics or a published measurement), **ASSUMED** (a choice of UM-4 without derivation),
**INVENTED** (a new interaction: the portals of dirac16complex), **DERIVED** (computed and verified in UM-4), **ESTIMATE** (an order of
magnitude) and **OPEN** (not settled).

## Coordinates, signature and units

The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ is the hidden
space-like coordinate, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, and $x_5, x_6, x_7$ three extra time-like coordinates. The
signature is $(+,+,+,+,-,-,-,-)$ in this order. Units are natural: the reduced Planck constant $\hbar$ and the speed of light $c$
are 1. A prime on a function of the time $x_4$ alone is its derivative with respect to $x_4$.

# The spacetime

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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
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

The metric of UM-4: the author's metric with his two functions of the time $a_4(x_4)$ and $b_4(x_4)$ ($b_4$ is never identically 1, by
the author's order of 2026-10-24) and his constant $H$, with the one change that his order of 2026-10-25 13:15 requires: the time $x_4$
carries the warp factor $(\sin^2z)^{1/6}$ of the other six directions of the fold ($g_{x_4x_4} = -(\sin^2z)^{1/6}$; in UM-3 it was $-1$).
The metric depends on $x_0$ only through $z = 6Hx_0$; one period $0 < z < \pi$ of $x_0$ is, in the proper coordinate $\sigma$ of the
hidden direction, the whole line $-\infty < \sigma < \infty$ (DERIVED). In that coordinate all seven directions of the fold, the time
included, are warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$, which has a kink at $\sigma = 0$ ($z = \pi/2$): this seven-dimensional surface is
the fold, and the rest of spacetime is the bulk. Every slice $\sigma = \text{const}$ is then a copy of the fold scaled by the same
factor in all seven directions, so that it has the light cone of the fold: whatever moves at the local speed of light in the bulk
moves along ordinary space at the speed of light of the fold (DERIVED, `um4_geometry.py`, G8). This is the smallest change of the
author's metric that meets the order: it keeps the coordinates, the period, the fold, the functions $a_4$, $b_4$ and the warp of
ordinary space and of the extra times. Without the fold and the functions $a_4$, $b_4$ the static block ($a_4$, $b_4$ constant) is,
on each side of the fold, a region of the anti-de Sitter space of eight dimensions of radius $1/H$ (constant curvature $-H^2$; DERIVED,
`um4_geometry.py`, G3). Status: AUTHOR (the metric and the order), ASSUMED (the way the order is met), DERIVED (the chart and the light
cone).

# The fields and where they live

| field | symbol | what it is | lives in | couples to |
| ---------------------- | ---------------- | ------------------------------------ | ---------- | ------------------------------ |
| Einstein gravity | $g_{MN}$ | the metric of eight dimensions; the author's Einstein-Lovelock action with the weights of the Gauss-Bonnet and cubic terms zero and $\Lambda = -21H^2$ | bulk and fold | every field |
| dirac16complex | $\Psi$ | the author's 16-component complex spinor field, with left- and right-handed halves $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ | the bulk | gravity (canonical spin connection), itself, every Standard-Model field at the fold; only $\Psi_{\mathrm{L}}$ to the Higgs doublet |
| gluons | $G^A$ | the gauge field of $SU(3)_{\mathrm{C}}$ | the bulk; its massless mode is bound to the fold | gravity, quarks, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ (at the fold) |
| electroweak gauge fields | $W^1$, $W^2$, $W^3$, $B$ | the gauge fields of $SU(2)_{\mathrm{L}}$ and $U(1)_Y$; the photon is the combination of $W^3$ and $B$ that the Higgs vacuum leaves massless | the bulk; their massless modes are bound to the fold | gravity, $\Phi$, the fermions, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ (at the fold) |
| Higgs doublet | $\Phi$ | the scalar doublet with $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$, $\lambda > 0$, $\mu^2 < 0$, expanded about the ad hoc vacuum $(\mathcal{A}, v + h)/\sqrt2$ | the fold | gravity, $W$, $B$, the fermions, $\Psi_{\mathrm{L}}$ |
| lepton doublets | $\ell_i$ | $(\nu_{\mathrm{L}i}, e_{\mathrm{L}i})$, three generations | the fold | gravity, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| right-handed charged leptons | $e_{\mathrm{R}i}$ | electron, muon, tau | the fold | gravity, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| right-handed neutrinos | $\nu_{\mathrm{R}i}$ | three gauge singlets: Dirac neutrino masses (accepted by the author, 2026-10-24 17:32) | the fold | gravity, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| quarks | $Q_i$, $u_{\mathrm{R}i}$, $d_{\mathrm{R}i}$ | three generations of doublets and singlets | the fold | gravity, gluons, $W$, $B$, $\Phi$, $\Psi_{\mathrm{L}}$, $\Psi_{\mathrm{R}}$ |
| fold fluid | $\mathcal{T}_{\mathrm{ff}}$ | the part of the thin source of the fold not supplied by the other fields: a tension, which the static block requires, and a pressure along the extra times that holds their volume fixed | the fold | gravity |
| induced gravity | $\kappa_{\mathrm{ind}}$ | an Einstein-Hilbert term that the fields of the fold induce; negligible for a cutoff of the order of $H$ | the fold | gravity |

The order places the photon in the bulk, and with it the electroweak gauge fields of which it is a combination; UM-4 places the
gluons there as well, so that all gauge fields of the Standard Model live in one place. In the metric of UM-4 every massless field of
the bulk has a mode bound to the fold that travels at the speed of light at every depth and every wavelength, and these modes are the
photon, the gluons and the electroweak gauge fields of the four-dimensional world, with the measured couplings. The Higgs doublet,
the quarks and the leptons stay on the fold, where their couplings and their flavour physics are those of the Standard Model with three
Dirac neutrinos (in the bulk they could also travel at the speed of light, but their Yukawa couplings would be set by the overlaps of
eighteen profiles). dirac16complex, the author's field of eight dimensions, lives in the bulk and couples to the fields of the fold at
the fold. No field depends on the extra times $x_5, x_6, x_7$: a field with a momentum along them is tachyonic (its frequency squared
falls with that momentum, because the extra times are time-like); the restriction is consistent but unstable, and UM-4 needs a gauge
principle that removes the momentum along the extra times of every field. Status: AUTHOR (the list of fields; the photon and the
graviton in the bulk, by the order), ASSUMED (the additions, the other places and the restriction), DERIVED (the speeds of the fields of
the bulk, the tachyons), OPEN (the gauge principle).

# The action

All field equations of UM-4 follow from one action by varying it with respect to every field.

## The sum of all terms

$$
\begin{aligned}
S_{\mathrm{tot}} &= S_{\mathrm{EL}} + S_\Psi + S_{\mathrm{gauge}} + S_{\mathrm{fold}},\\
S_{\mathrm{fold}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\delta_{\mathrm{D}}(\sigma)\,\frac{1}{V_*}\,
\big(\mathcal{L}_{\mathrm{IG}} + \mathcal{L}_{\mathrm{ff}} + \mathcal{L}_{\mathrm{H}} + \mathcal{L}_{\mathrm{f}}
+ \mathcal{L}_{\mathrm{Y}} + \mathcal{L}_{\mathrm{P}}\big)
\end{aligned} \tag{IN-1}
$$
<!-- symbols: Stot, SEL, SPsi, Sgauge, Sfold, diff, Xcoord, metric, deltaD, sigma, Vstar, LIG, Lff, LH, Lf, LY, LP -->
<!-- begin generated symbol list -->
**Symbols in (IN-1).**

- $S_{\mathrm{tot}}$: The action of UM-4 (the integral of the Lagrangian density over spacetime); its variation with respect to every field gives the field equations. Unit: dimensionless (in units in which the reduced Planck constant is 1). Status: ASSUMED.
- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity in eight dimensions; in UM-4 the Einstein-Hilbert action with the cosmological constant. Unit: dimensionless. Status: AUTHOR.
- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.
- $S_{\mathrm{gauge}}$: The action of the gauge fields in the bulk. Unit: dimensionless. Status: STANDARD.
- $S_{\mathrm{fold}}$: The action of the fold: the Standard Model, the portals of dirac16complex, the fold fluid and the Einstein-Hilbert term that the fields of the fold induce, all at $\sigma = 0$. Unit: dimensionless. Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{L}_{\mathrm{IG}}$: The Lagrangian of the Einstein-Hilbert term of the four-dimensional metric of the fold that the quantum fluctuations of the fields of the fold induce; it adds to the Einstein-Hilbert term that the graviton of the bulk gives the fold and does not change the speed of gravitational waves. Unit: GeV$^4$. Status: ESTIMATE.
- $\mathcal{L}_{\mathrm{ff}}$: The Lagrangian of the fold fluid (only its energy-momentum tensor $\mathcal{T}_{\mathrm{ff}}$ enters the equations). Unit: GeV$^4$. Status: ASSUMED.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->
<!-- symbols: -->

The action has four parts: Einstein gravity in eight dimensions, dirac16complex in the bulk, the gauge fields in the bulk, and the
fold, whose terms are confined to $\sigma = 0$ by the Dirac delta of the proper hidden coordinate; the bulk needs no other source
(the static block is a vacuum of Einstein gravity with $\Lambda = -21H^2$). Status: ASSUMED.

## Gravity

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
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

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
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor $R^M{}_{NPQ}$ (in the convention in which the commutator of two covariant derivatives, acting on a vector, is the Riemann tensor, with its last two indices those of the two derivatives, contracted with the vector), with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the scalar curvature $R = g^{MN}R_{MN}$; with frame indices $R^{(a)(b)}{}_{(c)(d)}$ its frame components, $R^{(a)(b)}{}_{(a)(b)}$ (no sum) the sectional curvature of the frame plane $(a, b)$. Unit: 1/length$^2$. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

Gravity is the author's Einstein-Lovelock theory (his notebook, In[134]) with the weights of the Gauss-Bonnet density
$\mathcal{L}_{(2)}$ and of the cubic Lovelock density $\mathcal{L}_{(3)}$ set to zero: Einstein gravity with the cosmological constant
$\Lambda = -21H^2$, for which the static block is a vacuum (its Einstein tensor is $21H^2$ in every direction; DERIVED, `um4_geometry.py`,
G4). The order requires gravitons at the speed of light in the bulk. Around the static block every non-degenerate choice of the weights
gives that (the graviton equation is, for any weights, the wave equation of the light cone of the fold times the factor
$1 - 40w_{(2)} + 360w_{(3)}$; DERIVED, `um4_gravity.py`, L2), but on every background that is not of constant curvature (an expanding
fold, a star, a gravitational wave of finite amplitude) the Gauss-Bonnet and cubic terms give the coefficients of the time and space
derivatives of a graviton different factors, and gravitons leave the light cone; only $w_{(2)} = w_{(3)} = 0$ keeps them on it on every
background (DERIVED, L3). The author's original weights $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$ would make the static block a vacuum only for
$\Lambda = -161H^2/16$ (not his $-10H^2$), with gravitons at the speed of light around it but not around an expanding fold; UM-3's weights
$1/20$, $1/360$ make the static block a degenerate vacuum without linear gravitons. Lovelock's densities contain no derivative of the
metric higher than the second in their variation, so a thin source at the fold produces a finite jump of first derivatives (the
junction condition). Status: AUTHOR (the action), DERIVED (the weights and $\Lambda$ that the order selects).

## dirac16complex

$$
S_\Psi = \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\frac12\big(\bar\Psi\gamma^MD_M\Psi - (D_M\bar\Psi)\gamma^M\Psi\big)
 - m_\Psi\,\bar\Psi\Psi - \frac{\lambda_\Psi}{2}\big(\bar\Psi\Psi\big)^2\Big] \tag{IN-4}
$$
<!-- symbols: SPsi, diff, Xcoord, metric, Psi, gammaM, iM, Dcov, mPsi, lamPsi -->
<!-- begin generated symbol list -->
**Symbols in (IN-4).**

- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.

<!-- end generated symbol list -->
<!-- symbols: -->

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
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$ (eta4488 of 4+4.nb); $\eta^{ab}$ is its inverse (the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality matrix of eight dimensions, $\Gamma_8 = T_0T_1\cdots T_7$ (the author's T16^A[8]) $= \mathrm{diag}(-\mathbf{1}_8, \mathbf{1}_8)$; $\Gamma_8^2 = \mathbf{1}$; it anticommutes with every $T_a$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\Psi_{\mathrm{L}}$: The left-handed half of dirac16complex, $\Psi_{\mathrm{L}} = P_{\mathrm{L}}\Psi$ (the upper eight components in the basis of 4+4.nb). Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\Psi_{\mathrm{R}}$: The right-handed half of dirac16complex, $\Psi_{\mathrm{R}} = P_{\mathrm{R}}\Psi$ (the lower eight components). Unit: GeV$^{7/2}$. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

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
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $\varpi_{Mab}$: The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$. Unit: 1/length. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\Sigma^{ab},\ \Sigma^{\mu\nu}$: The generators of Spin(4,4) on dirac16complex, $\Sigma^{ab} = \frac14[T^a, T^b]$ (the scaled commutators of the author's matrices); $\Sigma^{\mu\nu} = \mathbf{e}_a{}^\mu\mathbf{e}_b{}^\nu\Sigma^{ab}$ along the fold. Unit: dimensionless. Status: AUTHOR.
- $T_a,\ T^a$: The author's eight real $16 \times 16$ Dirac matrices T16^A[a] of 4+4.nb ($a = 0, \dots, 7$; $T_0, \dots, T_7$), with $\{T_a, T_b\} = 2\eta_{ab}\mathbf{1}$; $T^a = \eta^{ab}T_b$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{e}_a{}^M,\ \mathbf{e}^a{}_M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is its inverse; $\mathbf{e}_{bN} = \eta_{bc}\mathbf{e}^c{}_N$; $\mathbf{e}^{(a)}$ is the frame one-form $\mathbf{e}^a{}_M\,\mathrm{d}X^M$. Unit: dimensionless. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Gamma^P{}_{MN}$: The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection). Unit: 1/length. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

dirac16complex with the kinetic term in the symmetric form (real for the author's real matrices), the mass $m_\Psi$ and the contact
self-interaction $\lambda_\Psi$ (RECORD); the author's eight real $16 \times 16$ Dirac matrices, the Dirac adjoint and the chiral
projectors (AUTHOR); the canonical spin connection, which couples dirac16complex to gravity and is never identically zero for the
metric of UM-4: $\gamma^M\Omega_M = -\frac72H\,\mathrm{sgn}(\sigma)\gamma^{(0)} + \frac32(b_4'/b_4)\mathrm{e}^{H\lvert\sigma\rvert}\gamma^{(4)}$ (DERIVED,
`um4_geometry.py`, G9; $\gamma^{(0)} = T^0$ and $\gamma^{(4)} = T^4$ are the author's matrices along the hidden direction and along the
time, $\sigma$ the proper coordinate of the hidden direction with the fold at $\sigma = 0$, $\mathrm{sgn}$ the sign function; in UM-3 the
first term was $-3H\,\mathrm{sgn}(\sigma)\gamma^{(0)}$, because the time was not warped). The factor $\mathrm{e}^{(7/2)H\lvert\sigma\rvert}$ removes the
first term: a mode is $\Psi = \mathrm{e}^{(7/2)H\lvert\sigma\rvert}\chi(\sigma)$ times a plane wave of the fold, and the warp multiplies the
whole Dirac operator of the fold, the frequency as well as the momentum, by $\mathrm{e}^{H\lvert\sigma\rvert}$. The states of dirac16complex at
the fold are therefore Lorentz invariant along the fold, and, because the warped frequency exceeds the bulk mass far from the fold, they
are long-lived resonances rather than bound states (DERIVED, `um4_spectra.py`).

## The gauge fields in the bulk

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

The gauge fields of the Standard Model in the bulk of eight dimensions, with the couplings $\mathsf{g}_3$, $\mathsf{g}_2$, $\mathsf{g}_1$ of
eight dimensions. Their massless modes have the profile 1 along $\sigma$ and the kinetic weight $\mathrm{e}^{-3H\lvert\sigma\rvert}$, whose
integral over the hidden direction is $2/(3H)$: they are four-dimensional gauge fields with the couplings $g_k^2 = 3H\mathsf{g}_k^2/(2V_*)$
($k = 1, 2, 3$), the measured couplings of the Standard Model, and they travel at the speed of light at every depth (DERIVED,
`um4_bulk.py`, B2 and B3). Their massive modes form a continuum from zero mass upwards; they modify Coulomb's law at distances of the
order of $1/H$, add contact interactions between the currents of the fold, and give the W and Z bosons widths into the bulk, which
bound $H$ from below by about 2.5 TeV (DERIVED, ESTIMATE, `um4_bulk.py`, B10, and `um4_propagators.py`). The gauge fields have no components along the extra
times and no dependence on them (ASSUMED). Status: AUTHOR (the photon in the bulk, by the order), ASSUMED (all gauge fields in the bulk),
STANDARD (the Yang-Mills action).

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

- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\delta_{\mathrm{D}}$: The Dirac delta function of $\sigma$: zero for $\sigma \ne 0$, with the integral 1 over any range that contains $\sigma = 0$; the integral of $\delta_{\mathrm{D}}(\sigma)$ times a smooth function of $\sigma$ is the value of that function at $\sigma = 0$. Unit: 1/length (for $\delta_{\mathrm{D}}(\sigma)$). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathbb{F}$: Any function of the fields at the fold (used to state a rule of integration). Status: STANDARD.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold and the kinetic terms of the massless modes of the fields of the bulk; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_{\mathrm{t}}$: The coordinate volume of the (compact) extra times, $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$. Unit: length$^3$. Status: ASSUMED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\mathcal{L}_{\mathrm{IG}} = \frac{\hat R}{2\kappa_{\mathrm{ind}}} \tag{IN-9}
$$
<!-- symbols: LIG, Rhat, kappaind -->
<!-- begin generated symbol list -->
**Symbols in (IN-9).**

- $\mathcal{L}_{\mathrm{IG}}$: The Lagrangian of the Einstein-Hilbert term of the four-dimensional metric of the fold that the quantum fluctuations of the fields of the fold induce; it adds to the Einstein-Hilbert term that the graviton of the bulk gives the fold and does not change the speed of gravitational waves. Unit: GeV$^4$. Status: ESTIMATE.
- $\hat R$: The curvature of the metric $\hat g_{ab}$ of the fold (FD-2): with four frame indices its Riemann tensor, with two its Ricci tensor $\hat R_{ab}$, without indices its scalar curvature $\hat R$; for frozen extra times the scalar curvature equals that of the four-dimensional metric $\hat h_{\mu\nu}$. Unit: 1/length$^2$. Status: STANDARD.
- $\kappa_{\mathrm{ind}}$: The coupling of the Einstein-Hilbert term $\hat R/(2\kappa_{\mathrm{ind}})$ that the quantum fluctuations of the fields of the fold may induce, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$; it adds to the gravity of the fold, $1/(8\pi G_{\mathrm{N}}) = V_*/\kappa_7 + 1/\kappa_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Value: not fixed by UM-4; negligible for a cutoff of the order of $H$. Status: ESTIMATE.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\mathcal{T}_{\mathrm{ff}}{}^a{}_b = \mathrm{diag}\big(p_{\mathrm{ff}}, p_{\mathrm{ff}}, p_{\mathrm{ff}}, -\rho_{\mathrm{ff}},
 q_{\mathrm{ff}}, q_{\mathrm{ff}}, q_{\mathrm{ff}}\big) \tag{IN-10}
$$
<!-- symbols: Tff, ia, ib, diag, pff, rhoff, qff -->
<!-- begin generated symbol list -->
**Symbols in (IN-10).**

- $\mathcal{T}_{\mathrm{ff}}{}^a{}_b$: The energy-momentum tensor of the fold fluid (frame components of the fold, four-dimensional normalisation). Unit: GeV$^4$. Status: ASSUMED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ for a tensor of eight dimensions, $x_1, \dots, x_7$ for a tensor of the fold, $x_1, \dots, x_4$ for a four-dimensional tensor). Status: STANDARD.
- $p_{\mathrm{ff}}$: The pressure of the fold fluid along ordinary space. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}}$ (a tension). Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}}V_* + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}V_*$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times: minus its energy density (its tension) plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$. Status: ASSUMED (the fluid), DERIVED (the value).

<!-- end generated symbol list -->
<!-- symbols: -->

The fold: the reduction of the terms of the fold to four-dimensional fields with the volume $V_*$ of the extra times and the factor
$\mathcal{Z}$ (IN-8); the Einstein-Hilbert term that the fields of the fold induce (IN-9), negligible for a cutoff of the order of $H$
because the graviton of the bulk gives the fold its gravity: to the first order in its curvature over $H^2$ the fold obeys the Einstein
equations of seven dimensions with $\kappa_7 = 5\kappa H/2$, which with the volume of the extra times held fixed are the Friedmann
equations of general relativity with Newton's constant $8\pi G_{\mathrm{N}} = \kappa_7/V_*$, and its four-dimensional gravitational waves travel
at the speed of light at every wavelength; and the fold fluid (IN-10, with the values FE-65), the thin source that the kink of the warp
factor requires: a pure tension $\lambda_{\mathrm{F}}$ at the static block, $\kappa\lambda_{\mathrm{F}} = 12H$, as for the brane of Randall and Sundrum,
whose excess over $\lambda_{\mathrm{F}}$ (together with the vacuum energy of the fields) is the dark energy, and the pressure $q_{\mathrm{hold}}$ along
the extra times that holds their volume fixed (without it Newton's constant, the squares of the gauge and Yukawa couplings and the
quartic Higgs coupling would change far beyond the observed bounds). Status: ASSUMED (the fold fluid and its holding pressure), DERIVED
(the reduction, the gravity of the fold, the values of the fold fluid), ESTIMATE (the induced term).

$$
\begin{aligned}
&p_{\mathrm{ff}} = -\rho_{\mathrm{ff}},\qquad q_{\mathrm{ff}} = -\rho_{\mathrm{ff}} + q_{\mathrm{hold}},\qquad
 \kappa\lambda_{\mathrm{F}} = 12H\ \ \big(\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2\big),\\
&q_{\mathrm{hold}} = -\frac{\rho - 3\mathcal{P}}{2} - q_{\mathrm{SM}} - q_\chi - q_{\mathrm{P}}:\qquad
 \text{radiation } 0,\quad \text{dust } -\frac{\rho}{2},\quad \text{a vacuum energy } -\rho
\end{aligned} \tag{FE-65}
$$
<!-- symbols: pff, rhoff, qff, qhold, kappa, lambdaF, Hconst, Vstar, Mred, rhotot, Ptot, qSM, qchi, qP -->
<!-- begin generated symbol list -->
**Symbols in (FE-65).**

- $p_{\mathrm{ff}}$: The pressure of the fold fluid along ordinary space. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}}$ (a tension). Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}}V_* + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}V_*$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times: minus its energy density (its tension) plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$. Status: ASSUMED (the fluid), DERIVED (the value).
- $q_{\mathrm{hold}}$: The pressure along the extra times that the fold fluid adds to its tension to hold the volume of the extra times fixed (four-dimensional normalisation). Unit: GeV$^4$. Value: $-(\rho - 3\mathcal{P})/2 - q_{\mathrm{SM}} - q_\chi - q_{\mathrm{P}}$: 0 for radiation, $-\rho/2$ for dust, $-\rho$ for a vacuum energy; today $-0.842\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have no pressure along the extra times (ASSUMED). Status: DERIVED (the value), ASSUMED (that the fold fluid supplies it).
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2.5$ TeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H \gtrsim 2.5$ TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $q_{\mathrm{SM}}$: The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times). Unit: GeV$^4$. Status: DERIVED (for radiation and free fields), ASSUMED (for the baryons).
- $q_\chi$: The pressure of the particles $\chi$ of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{P}}$: The pressure of the portals along the extra times: their mean on-shell Lagrangian density. Unit: GeV$^4$. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The values of the fold fluid with frozen extra times: its energy density and its pressure along ordinary space are those of a tension;
the tension that the static block requires is $\kappa\lambda_{\mathrm{F}} = 12H$, in the four-dimensional normalisation
$\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2$; the pressure along the extra times adds $q_{\mathrm{hold}}$, which makes up what the matter of the fold
lacks of the pressure $-(\rho - 3\mathcal{P})/2$ that the radion condition requires (today $-0.842$ times the critical density if the
baryons have no pressure along the extra times, ASSUMED). The observed dark energy needs the tension tuned to one part in $10^{92}$ for
$H = 2.5$ TeV, the cosmological-constant problem of the brane of Randall and Sundrum. Status: DERIVED (the values), ASSUMED (that the
fold fluid supplies them; the pressure of the baryons), OPEN (its origin, the tuning).

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
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $V(\Phi)$: The Higgs potential, $V = \mu^2\Phi^\dagger\Phi + \lambda(\Phi^\dagger\Phi)^2$. Unit: GeV$^4$. Status: AUTHOR.
- $\mu^2$: The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$). Unit: GeV$^2$. Value: $\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\Phi = \frac{1}{\sqrt2}\begin{pmatrix}\mathcal{A}(x_4)\\ v + h\end{pmatrix},\qquad
\mathcal{A}(x_4) = v_{\mathcal{A}}\,\mathrm{e}^{-2a_{40}x_4},\qquad a_{40} > 0,\quad x_4 \ge 0,\qquad v^2 = -\frac{\mu^2}{\lambda} \tag{IN-12}
$$
<!-- symbols: Phi, Aadhoc, x4, vev, hHiggs, vA, euler, a40, muH, lamH -->
<!-- begin generated symbol list -->
**Symbols in (IN-12).**

- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $h$: The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$. Unit: GeV. Value: $m_h = 125.25$ GeV. Status: STANDARD.
- $v_{\mathcal{A}}$: The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc, $\mathrm{e}^{-2a_{40}x_4}$ (written Exp[-2 a40 x4] in his notebook), has $v_{\mathcal{A}} = 1$ in the units of his notebook. Unit: GeV. Value: 1 in the units of the author's notebook; UM-4 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$). Status: AUTHOR (the form), ASSUMED (a free amplitude).
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_{40}$: The decay constant of almightyAdHoc, $a_{40} > 0$: $\mathcal{A}$ falls by $\mathrm{e}$ in the time $1/(2a_{40})$. Unit: GeV (1/length). Status: AUTHOR.
- $\mu^2$: The mass parameter of the Higgs potential, $\mu^2 < 0$ (it enters only as $\mu^2$). Unit: GeV$^2$. Value: $\mu^2 = -\lambda v^2 = -m_h^2/2 = -(88.6\ \mathrm{GeV})^2$. Status: AUTHOR.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

The Higgs doublet with the author's potential, expanded about the author's ad hoc vacuum, whose upper component almightyAdHoc decays as
$\mathrm{e}^{-2a_{40}x_4}$ (the author writes $\mathrm{Exp}[-2a_{40}x_4]$; UM-4 gives it the amplitude $v_{\mathcal{A}}$ so that it has the dimension
of the Higgs field). Status: AUTHOR.

## The gauge fields at the fold, the quarks and the leptons

$$
\begin{aligned}
D_\mu &= \partial_\mu + \hat\omega_\mu - \mathrm{i}g_3\,G^A_\mu\,t^A - \mathrm{i}g_2\,W^I_\mu\,\frac{\tau^I}{2}
 - \mathrm{i}g_1\,Y_f\,B_\mu,\\
g_3\,G^A_\mu(x) &= G^A_\mu(\sigma = 0, x),\qquad g_2\,W^I_\mu(x) = W^I_\mu(\sigma = 0, x),\qquad g_1\,B_\mu(x) = B_\mu(\sigma = 0, x)
\end{aligned} \tag{IN-13}
$$
<!-- symbols: Dcov, imu, partial, omegahat, imag, g3, Ggluon, iA, tgen, g2, Wsu2, iI, taupauli, g1, Yhyp, if, Bhyp, sigma, xfour -->
<!-- begin generated symbol list -->
**Symbols in (IN-13).**

- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\hat\omega_\mu$: The spin connection of the four-dimensional metric $\hat h_{\mu\nu}$ of the fold acting on four-dimensional spinors. Unit: 1/length. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling of the four-dimensional world (the strong coupling $g_s$): the coupling of the massless mode of the gluon field of the bulk, $g_3^2 = 3H\mathsf{g}_3^2/(2V_*)$. Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($g_3^2/(4\pi) = 0.1180$). Status: STANDARD.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $t^A$: The generators of $SU(3)$ on colour triplets, $t^A$: half the Gell-Mann matrices, with $\mathrm{tr}(t^At^B) = \delta^{AB}/2$. Unit: dimensionless. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling of the four-dimensional world (usually $g$): the coupling of the massless mode of the $SU(2)_L$ field of the bulk, $g_2^2 = 3H\mathsf{g}_2^2/(2V_*)$. Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $W^I_M,\ W^I_\mu,\ W^I_{MN}$: The gauge field of $SU(2)_L$ ($I = 1, 2, 3$): in the bulk $W^I_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $W^I_\mu(x)$ of its massless mode, $g_2W^I_\mu(x) = W^I_\mu(\sigma = 0, x)$; $W^I_{MN}$, $W^I_{\mu\nu}$ their field strengths; $W^\pm_\mu = (W^1_\mu \mp \mathrm{i}W^2_\mu)/\sqrt2$. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square). Unit: dimensionless. Status: STANDARD.
- $g_1$: The $U(1)_Y$ gauge coupling of the four-dimensional world (usually $g'$; not normalised for grand unification): the coupling of the massless mode of the hypercharge field of the bulk, $g_1^2 = 3H\mathsf{g}_1^2/(2V_*)$. Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $Y_f$: The hypercharge of a field, the charge of its coupling $g_1Y_fB_\mu$ to the hypercharge field in the covariant derivative ($1/6$, $2/3$, $-1/3$, $-1/2$, $-1$, $0$ for $Q, u_{\mathrm{R}}, d_{\mathrm{R}}, \ell, e_{\mathrm{R}}, \nu_{\mathrm{R}}$, $1/2$ for $\Phi$). Unit: dimensionless. Status: STANDARD.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $B_M,\ B_\mu,\ B_{MN}$: The hypercharge gauge field of $U(1)_Y$: in the bulk $B_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $B_\mu(x)$ of its massless mode, $g_1B_\mu(x) = B_\mu(\sigma = 0, x)$; $B_{MN}$, $B_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

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
- $\hat\gamma^\mu$: The four-dimensional complex $4 \times 4$ Dirac matrices of the fold: $\hat\gamma^{(a)}$ along the frame directions of the fold and $\hat\gamma^\mu$ along its coordinates (the frame matrices contracted with the inverse frame field of the fold), $\{\hat\gamma^\mu, \hat\gamma^\nu\} = -2\hat h^{\mu\nu}\mathbf{1}$; $\hat\gamma_\mu = \hat h_{\mu\nu}\hat\gamma^\nu$. Unit: dimensionless. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on dirac16complex $D_M = \partial_M + \Omega_M$ (with $D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M$); on the fields of the fold the gauge and spin covariant derivative $D_\mu$ (the partial derivative plus the spin connection of the fold and the gauge fields times their couplings and generators); $D^\mu = \hat h^{\mu\nu}D_\nu$; on an adjoint field $(D_\mu X)^A = \partial_\mu X^A + g_3f^{ABC}G^B_\mu X^C$ (likewise for $SU(2)$ with $g_2\epsilon^{IJK}$). Unit: 1/length. Status: STANDARD.
- $Q,\ \bar Q$: The left-handed quark doublets of the three generations, $Q = (u_{\mathrm{L}}, d_{\mathrm{L}})$ (colour triplets, hypercharge $1/6$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $u_{\mathrm{R}}$: The right-handed up-type quarks (up, charm and top; singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{R}}$: The right-handed down-type quarks (down, strange and bottom; hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $\hat h_{\mu\nu}$: The four-dimensional metric of the fold, $\hat h_{\mu\nu} = \mathrm{diag}(\mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, \mathrm{e}^{2a_4}, -1)$ in the coordinates $x_1, \dots, x_4$ (the induced metric at $\sigma = 0$ without the extra times); $\hat h^{\mu\nu}$ its inverse, $\hat h$ its determinant, $\sqrt{-\hat h} = \mathrm{e}^{3a_4}$; $\hat h^{(1)}_{\mu\nu}$ its first-order cosmological perturbation. Unit: dimensionless. Status: DERIVED.
- $\mathbf{1},\ \mathbf{1}_8$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_8$ is the $8 \times 8$ identity matrix. Unit: dimensionless. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\beta$: The matrix of the four-dimensional Dirac adjoint, $\beta = \hat\gamma^{(4)}$ (Hermitian, $\beta^2 = \mathbf{1}$). Unit: dimensionless. Status: STANDARD.
- $\hat\gamma_5$: The four-dimensional chirality matrix, $\hat\gamma_5 = \mathrm{i}\hat\gamma^{(4)}\hat\gamma^{(1)}\hat\gamma^{(2)}\hat\gamma^{(3)}$, $\hat\gamma_5^2 = \mathbf{1}$. Unit: dimensionless. Status: STANDARD.
- $\hat P_{\mathrm{L}}$: The four-dimensional left-handed projector, $\hat P_{\mathrm{L}} = (\mathbf{1} - \hat\gamma_5)/2$. Unit: dimensionless. Status: STANDARD.
- $\hat P_{\mathrm{R}}$: The four-dimensional right-handed projector, $\hat P_{\mathrm{R}} = (\mathbf{1} + \hat\gamma_5)/2$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

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
- $u_{\mathrm{R}}$: The right-handed up-type quarks (up, charm and top; singlets of $SU(2)_L$, hypercharge $2/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- $d_{\mathrm{R}}$: The right-handed down-type quarks (down, strange and bottom; hypercharge $-1/3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\ell,\ \bar\ell$: The left-handed lepton doublets of the three generations, $\ell = (\nu_{\mathrm{L}}, e_{\mathrm{L}})$ (hypercharge $-1/2$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $e_{\mathrm{R}}$: The right-handed electron, muon and tau (singlets, hypercharge $-1$). Unit: GeV$^{3/2}$. Status: AUTHOR.
- $\nu_{\mathrm{R}}$: The three right-handed neutrinos (gauge singlets). Unit: GeV$^{3/2}$. Status: ASSUMED.
- $\mathrm{h.c.}$: The Hermitian conjugate of the preceding terms. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak doublets ($\tau^1, \tau^2, \tau^3$; $\tau^2$ is the second one, not a square). Unit: dimensionless. Status: STANDARD.
- ${}^*$: Complex conjugation of a number, or of each entry of a matrix or column. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

The gauge fields of the bulk act on the fields of the fold through their values at the fold (IN-13: for the massless modes, the
canonically normalised four-dimensional gauge fields with the measured couplings), the three generations of quarks and leptons with
three right-handed neutrinos (IN-14), and their Yukawa couplings to the Higgs doublet (IN-15). With the right-handed neutrinos the
gauge anomalies still cancel (DERIVED, `um4_fields.py`), and the neutrino Yukawa couplings give the neutrinos Dirac masses, whose values
are chosen to reproduce the measured mass differences with the lightest mass zero (ASSUMED). Status: STANDARD (UM-4 adds the
right-handed neutrinos and puts the gauge fields in the bulk).

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
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ of the fold (signature $+,+,+,-$); a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index (as $\mu$). Status: STANDARD.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $W^I_M,\ W^I_\mu,\ W^I_{MN}$: The gauge field of $SU(2)_L$ ($I = 1, 2, 3$): in the bulk $W^I_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $W^I_\mu(x)$ of its massless mode, $g_2W^I_\mu(x) = W^I_\mu(\sigma = 0, x)$; $W^I_{MN}$, $W^I_{\mu\nu}$ their field strengths; $W^\pm_\mu = (W^1_\mu \mp \mathrm{i}W^2_\mu)/\sqrt2$. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $B_M,\ B_\mu,\ B_{MN}$: The hypercharge gauge field of $U(1)_Y$: in the bulk $B_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $B_\mu(x)$ of its massless mode, $g_1B_\mu(x) = B_\mu(\sigma = 0, x)$; $B_{MN}$, $B_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
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
<!-- symbols: -->

The new interactions (the same as in UM-3): every Standard-Model field couples at the fold to the left-handed and to the right-handed
half of dirac16complex, each with its own coupling, through gauge-invariant operators: the Higgs portal (left-handed half only), the
gauge-kinetic portals of the gluons, $W$ and $B$, a dipole portal to $B$, and current portals between the fermion-number current of
every multiplet of the Standard Model and the convective currents of the two halves. Each is invariant under the gauge group of the
Standard Model and contains dirac16complex only in bilinears, so the charge of dirac16complex is conserved and its lightest states
cannot decay into the Standard Model alone; in UM-4 they decay slowly into the waves of dirac16complex in the bulk (the resonances).
The charge is indefinite (a Krein form); quantised with positive energies, every quantum carries a positive energy, so the vacuum is
stable (whether a gas of the particles is classically stable is not decided); but the modes of positive Krein charge are ghosts
(negative norm), and every coupling of the fold that distinguishes the two chiralities, the Higgs portal of the left-handed half among
them, creates them together with physical particles: with these portals UM-4 is not a unitary quantum theory, and a unitary UM-4 would
need couplings of the fold that do not distinguish the chiralities (necessary, not shown to be sufficient). Status: INVENTED (the
portals), DERIVED (the stability of the vacuum and the ghosts, `um4_krein.py`), OPEN (the stability of the gas, a unitary coupling).

# The parameters

| parameter | meaning | value | status |
| ------ | ------ | ------ | ------ |
| $H$ | the author's constant: the period $\pi/(6H)$ of $x_0$, the warp factor, the curvature $-H^2$ of the static block | free, bounded from below: $H \gtrsim 2.5$ TeV by the invisible width of the Z boson (its decay into the bulk), 1.3 TeV by contact interactions, 0.97 TeV by the parameter rho of the electroweak fits, $7.7\times10^{-3}$ eV by Newton's law at 52 micrometres | AUTHOR (the constant), DERIVED and ESTIMATE (the bounds) |
| $a_4(x_4)$, $b_4(x_4)$ | the author's functions of the time | frozen extra times, $\mathrm{e}^{-a_4}b_4$ constant, with the expansion $a_4(x_4)$ of general relativity (the metric FE-27 solves the field equations exactly only for the static block; around an expanding fold the bulk metric is corrected by terms of the order of the curvature of the fold divided by $H^2$, which vanish at the fold); the author's vacuum $a_4 = Hx_4$ with constant $b_4$ is not a solution | AUTHOR, DERIVED |
| $w_{(p)}$, $\Lambda$ | the Lovelock weights and the cosmological constant of the bulk | $w = (1, 0, 0)$ (Einstein gravity), $\Lambda = -21H^2$: gravitons on the light cone on every background (the author's original values $(1, 1/32, 1/1152)$ and $-10H^2$; UM-3: $(1, 1/20, 1/360)$ and $-7H^2$) | AUTHOR (the form), DERIVED (the values that the order selects) |
| $\kappa = 8\pi G_8$ | the gravitational coupling of the bulk | free; Newton's constant fixes $5\kappa H/(2V_*)$ | ASSUMED |
| $\kappa_7$ | the gravitational coupling of the fold | $5\kappa H/2$; $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus $1/\kappa_{\mathrm{ind}}$ in $1/(8\pi G_{\mathrm{N}})$) | DERIVED |
| $\kappa_{\mathrm{ind}}$ | the coupling of the induced Einstein-Hilbert term of the fold | negligible for a cutoff of the order of $H$; not fixed by UM-4 | ESTIMATE |
| $V_*$ | the physical volume of the extra times at the fold | free; Newton's constant fixes $\kappa H/V_*$ | ASSUMED |
| $\mathsf{g}_1$, $\mathsf{g}_2$, $\mathsf{g}_3$ | the gauge couplings of eight dimensions | $\mathsf{g}_k^2 = 2V_*g_k^2/(3H)$ from the measured couplings | ASSUMED (the place), DERIVED (the relation) |
| $\xi_{\mathrm{H}}$ | the coupling of the Higgs doublet to the curvature of the fold | 0: the Higgs Lagrangian of UM-4 (IN-11) has no such term; about $1.6\times10^4$ if the Higgs field drove an inflation of the fold in an extension of the action (ESTIMATE), which would need $H > 1.6\times10^{14}$ GeV | not in the action; ESTIMATE (the extension) |
| $\rho_{\mathrm{ff}}$, $p_{\mathrm{ff}}$, $q_{\mathrm{ff}}$ | the fold fluid (energy density, pressure along ordinary space, pressure along the extra times) | a tension: $p_{\mathrm{ff}} = -\rho_{\mathrm{ff}}$; with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields, $\rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} = \lambda_{\mathrm{F}}V_* + \rho_\Lambda$, $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2$, $\rho_\Lambda = (2.2\ \mathrm{meV})^4$ the dark energy; $q_{\mathrm{ff}} = -\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$, $q_{\mathrm{hold}} = -0.842$ times the critical density today (with no pressure of the baryons along the extra times) | ASSUMED (its values DERIVED) |
| $m_\Psi$ | the bulk mass of dirac16complex | free; the particles $\chi$ of dark matter live longer than the universe only if $m_\Psi/H$ is large (above about $1.1\times10^3$ for $q_{\mathrm{b}} = m_\Psi/2$) | RECORD |
| $\lambda_\Psi$ | the self-coupling of dirac16complex | free; at $m_\Psi/H = 10^4$ a gas of the particles $\chi$ lives longer than the universe only if its dimensionless strength is below 0.147 | RECORD |
| $c_\Phi$, $c^{G}_X$, $c^{W}_X$, $c^{B}_X$, $d_X$, $c^{f}_X$ | the portal couplings ($X$ = L, R) | free; direct detection and the effective number of neutrino species $N_{\mathrm{eff}}$ (the energy density of the relativistic species besides the photons, in units of one neutrino species) constrain them; a binding of the particles $\chi$ to the fold by the Higgs portal alone is excluded by direct detection together with their lifetime | INVENTED |
| $v$, $\lambda$, $\mu^2$ | the Higgs vacuum and potential | $v = 246.22$ GeV, $\lambda = 0.129$, $\mu^2 = -\lambda v^2$ | AUTHOR, STANDARD |
| $v_{\mathcal{A}}$, $a_{40}$ | amplitude and rate of the ad hoc vacuum $\mathcal{A} = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$ | the author's amplitude is 1 in the units of his notebook; UM-4 keeps $v_{\mathcal{A}}$ free (the examples take $v$ and $10v$); $a_{40} > 0$; nucleosynthesis needs $a_{40} > \ln(v_{\mathcal{A}}/(0.1v))/(2\ \text{s})$ | AUTHOR, ASSUMED (a free amplitude) |
| $g_1$, $g_2$, $g_3$ | the four-dimensional gauge couplings | the measured values | STANDARD |
| $\mathcal{Y}^{u}$, $\mathcal{Y}^{d}$, $\mathcal{Y}^{e}$, $\mathcal{Y}^{\nu}$ | the Yukawa matrices | the measured masses and mixings (Particle Data Group); neutrinos (the global fit NuFIT 5.2 of the oscillation data, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data): the differences of the squared masses of the three mass states $\Delta m^2_{21} = 7.41\times10^{-5}$ eV$^2$ and $\Delta m^2_{31} = 2.511\times10^{-3}$ eV$^2$, the mixing angles $\theta_{12} = 33.40^\circ$, $\theta_{13} = 8.54^\circ$, $\theta_{23} = 49.14^\circ$; the lightest mass 0 and the Dirac phase 0. The newer fit NuFIT 6.0 (2024) changes the results by at most 1.5 per cent; the Dirac phase (212 degrees in NuFIT 6.0) drops out of every result of UM-4; DESI DR2 with the CMB and NuFIT 6.0 bounds the lightest mass below 23 meV | STANDARD, ASSUMED (the lightest mass; the phase is irrelevant, DERIVED) |
| $A_{\mathrm{s}}$, $n_{\mathrm{S}}$, $\tau_{\mathrm{reion}}$ | the primordial spectrum and the optical depth | Planck 2018: $\ln(10^{10}A_{\mathrm{s}}) = 3.044$, $n_{\mathrm{S}} = 0.9649$, $\tau_{\mathrm{reion}} = 0.0544$; they need an inflation of the fold with frozen extra times, in the regime of general relativity only if its rate is below $H/10$ (its inflaton is not specified; the Higgs field only with a curvature coupling that the action does not contain) | ASSUMED (inputs; the inflaton and the holding pressure OPEN) |

# Further symbols

<!-- further symbols: Mred, kwave, GF, Gind, Delta, kappa7, trace, nuL, dL, eL, mmass, mh, uL, Gammabulk, tfold, ii, mzero, mferm, vloc, Mloc, hTT, rho7, q7, As, Neff, Tany, Wwarp, nS, thetaij, upsilonr, xiH, Fwkb, Pmns, Lfold, kstar, qdecay -->
<!-- begin generated symbol list -->
**Further symbols.** These symbols appear in the definitions of the symbols listed after the equations of this document.

- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $k$: A wave number: the momentum of a plane wave along $x_3$, $\mathrm{e}^{\mathrm{i}(kx_3 - \omega x_4)}$; in the cosmological perturbations the comoving wave number of a Fourier mode, $k = \lvert\vec k\rvert$. Unit: GeV (1/length). Status: STANDARD.
- $G_{\mathrm{F}}$: The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in the equations of the neutrino flavours it stands for the local Fermi constant of the ad hoc vacuum. Unit: GeV$^{-2}$. Value: $1.1664\times10^{-5}$ GeV$^{-2}$. Status: STANDARD.
- $G_{\mathrm{ind}}$: The Newton constant of the induced Einstein-Hilbert term of the fold, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Status: ESTIMATE.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\nu_{\mathrm{L}}$: The upper (neutral, left-handed) components of the lepton doublets: the left-handed neutrinos. Unit: GeV$^{3/2}$. Status: STANDARD.
- $d_{\mathrm{L}}$: The lower (down-type, left-handed) components of the quark doublets. Unit: GeV$^{3/2}$. Status: STANDARD.
- $e_{\mathrm{L}}$: The lower (charged, left-handed) components of the lepton doublets. Unit: GeV$^{3/2}$. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $m_h$: The mass of the Higgs boson. Unit: GeV. Value: 125.25 GeV (Particle Data Group 2022). Status: STANDARD.
- $u_{\mathrm{L}}$: The upper (up-type, left-handed) components of the quark doublets. Unit: GeV$^{3/2}$. Status: STANDARD.
- $\Gamma_{\mathrm{bulk}}$: The width of the W or the Z boson into the bulk (its decay into the massive modes of the gauge fields of the bulk), $\Gamma_{\mathrm{bulk}} = m_0(m_0/H)^3/3$. Unit: GeV. Value: 1.4 MeV for the Z and 0.9 MeV for the W at $H = 2.5$ TeV. Status: DERIVED.
- $\mathsf{t}^a{}_b,\ \mathsf{t}$: The matter of the fold above its tension: the thin source minus the tension, $\mathcal{S}^a{}_b = -\lambda_{\mathrm{F}}\delta^a{}_b + \mathsf{t}^a{}_b$ (eight-dimensional normalisation); $\mathsf{t} = \mathsf{t}^c{}_c$ its trace; with frozen extra times $\mathsf{t}^a{}_b = \mathrm{diag}(P_7, P_7, P_7, -\rho_7, q_7, q_7, q_7)$. Unit: GeV$^7$. Status: DERIVED.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal), and in a tensor of ordinary space such as $\mathsf{h}_{ij}$ one of the directions $x_1, x_2, x_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $m_0$: The mass of the W or the Z boson without the massive modes of the bulk (the mass of the massless mode with the Higgs vacuum), $m_0^2 = \frac32HM_{\mathrm{loc}}^2$; $m_0^2 = g_2^2(v^2 + \mathcal{A}^2)/4$ for the W. Unit: GeV. Status: DERIVED.
- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-4 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 23 meV by DESI DR2 with the CMB and NuFIT 6.0. Status: STANDARD.
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.
- $M_{\mathrm{loc}}$: The mass term that the Higgs vacuum on the fold gives a gauge field of the bulk: $M_{\mathrm{loc}}^2\delta_{\mathrm{D}}(\sigma)$ in its profile equation; for the W, $M_{\mathrm{loc}}^2 = \mathsf{g}_2^2(v^2 + \mathcal{A}^2)/(4V_*)$. Unit: GeV$^{1/2}$ ($M_{\mathrm{loc}}^2$ in GeV). Status: DERIVED.
- $\mathsf{h}_{ij}$: The transverse traceless perturbation of the metric of ordinary space by a gravitational wave as the four-dimensional world sees it: $\hat h_{ij} = \mathrm{e}^{2a_4}(\delta_{ij} + \mathsf{h}_{ij})$ ($i, j = 1, 2, 3$). Unit: dimensionless. Status: STANDARD.
- $\rho_7$: The energy density of the matter of the fold above its tension in the seven-dimensional normalisation (minus the component $\mathsf{t}^{(4)}{}_{(4)}$: an energy per unit volume of the six other directions of the fold); $V_*\rho_7$ in the four-dimensional normalisation. Unit: GeV$^7$. Status: DERIVED.
- $q_7$: The pressure along the extra times of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(r)}{}_{(r)}$). Unit: GeV$^7$. Status: DERIVED.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $N_{\mathrm{eff}}$: The effective number of neutrino species: the energy density of the relativistic particles other than photons in units of that of one neutrino species whose temperature is $(4/11)^{1/3}$ times that of the photons. Unit: dimensionless. Value: 3.044 (Standard Model); measured $2.99 \pm 0.17$ (Planck 2018). Status: STANDARD.
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{W}$: The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-4 the function of $\sigma$ that multiplies all seven directions of the fold, ordinary space, the time and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold. Unit: dimensionless. Status: DERIVED.
- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.
- $\theta_{12},\ \theta_{13},\ \theta_{23}$: The three mixing angles of $U_{\mathrm{PMNS}}$ (its fourth parameter is the Dirac phase, which does not enter the electron-flavour results of UM-4). Unit: dimensionless. Value: $33.40^\circ$, $8.54^\circ$, $49.14^\circ$ in the computations of UM-4 ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$: NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); $33.71^\circ$, $8.56^\circ$, $43.28^\circ$ in NuFIT 6.0 (2024, with the Super-Kamiokande atmospheric data; $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$). Status: STANDARD.
- $\upsilon,\ \upsilon_{\mathrm{b}}$: The argument of the tunnelling exponent $F$, a ratio of an energy to the bulk mass $m_\Psi$; $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ that of the particle $\chi$. Unit: dimensionless. Status: DERIVED.
- $\xi_{\mathrm{H}}$: The coupling of the Higgs doublet to the scalar curvature of the fold, the term $-\xi_{\mathrm{H}}\hat R\,\Phi^\dagger\Phi$ in the Lagrangian of the fold: an extension of UM-4, whose Higgs Lagrangian has no such term ($\xi_{\mathrm{H}} = 0$). Unit: dimensionless. Value: 0 in UM-4; about $1.6\times10^4$ if the Higgs field drove inflation (ESTIMATE, an extension of the action). Status: ESTIMATE (an extension of the action).
- $F(\upsilon)$: The tunnelling exponent of the width of the particles $\chi$ per unit of $m_\Psi/H$: the integral of the local decay rate $q$ over the region inside the turning point, divided by $m_\Psi/H$, as a function of the ratio $\upsilon$ of the energy to the bulk mass. Unit: dimensionless. Value: 0.049 for $\upsilon = 0.866$; $(q_{\mathrm{b}}/\omega_{\mathrm{b}})^3/3$ for weak binding. Status: DERIVED.
- $U_{\mathrm{PMNS}}$: The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; its entries $(U_{\mathrm{PMNS}})_{\alpha i}$ connect the flavour state $\nu_\alpha$ with the mass state $\nu_i$. Unit: dimensionless. Value: $\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$). Status: STANDARD, ASSUMED (the phase).
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.
- $k_*$: The pivot wave number of the primordial spectrum. Unit: GeV (1/length). Value: 0.05 Mpc$^{-1}$. Status: STANDARD.
- $q$: The local decay rate of a profile of dirac16complex along $\sigma$ at the frequency $\omega$, $q = \sqrt{m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}}$ (imaginary beyond the turning point, where the profile oscillates). Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->
