---
title: "UM-4 analysis"
subtitle: 'The x0 mass mechanism, dirac16complex as dark matter and as dark energy, the open questions, what the author may have left out, and UM-4 compared with UM-3'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Analysed and verified by Claude (Anthropic)"
  - "Analysis of UM-4, 2026-10-25"
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

The author asked for three analyses of his universe model: the mass mechanism along the hidden coordinate $x_0$ (the period
$\pi/(6H)$ of the metric and the uncertainty relation), whether dirac16complex can be the dark matter, and whether it can be the dark
energy. He also asked to be told what he may have left out, and (on 2026-10-25) for answers to the questions that the model had left
open. On 2026-10-25 at 13:15 PDT he ordered a new metric, in which the time $x_4$ is warped like the other directions of the fold and
photons and gravitons propagate at the speed of light in the bulk; the model built on it is the universe model UM-4. This document
gives the analyses and the answers for UM-4, and compares UM-4 with its predecessor UM-3. All of them use the metric of UM-4 (FE-27)
and Einstein gravity in eight dimensions with the cosmological constant $\Lambda = -21H^2$ (the author's Einstein-Lovelock theory with
the weights of its Gauss-Bonnet and cubic terms set to zero, the only choice of the weights for which gravitons travel on the light cone
on every background). It is self-contained: every equation it uses is written in it, and every symbol of every display equation is
defined right after it; a symbol that one of these definitions uses is defined in this document as well. The equations keep the tag
they carry in every UM-4 document: FE-n for a field equation or a result of the field equations, IN-n for a term of the action, S-n for
an equation of the solution of UM-4; the equations that only this document needs carry the tags A-1, A-2, and so on. The sections are:

* **The answers in brief.**
* **The $x_0$ mass mechanism**: the period of $x_0$, the proper length of the hidden direction, the spectra that replace the tower of a
  compact dimension, and what the observer on the fold sees of them.
* **dirac16complex as dark matter**: the stability and the lifetime of its particles, their gravitation on the fold, the equation of
  state of their Kohn-Sham states, the relic density, direct detection, and what is left of the window of parameters.
* **dirac16complex and the dark energy**: why the gas of its particles cannot be dark energy, what the dark energy of UM-4 is, and how it
  compares with the baryon acoustic oscillations measured by DESI DR2 (the second data release of the Dark Energy Spectroscopic
  Instrument).
* **The open questions answered**: whether the indefinite Krein norm of dirac16complex is stable, what fields that depend on the extra
  times do, whether anything moves faster than light, the primordial era, and the lightest neutrino mass and the Dirac phase.
* **What the author may have left out**: the additions that UM-4 needed, and the open problems.
* **UM-4 compared with UM-3**: what the warped time changed.

## The status labels

Every result carries one of the labels **AUTHOR** (from the author's notebooks `4+4.nb` and `Dirac_Einstein-Lovelock_4+4_Nash.nb`
and his orders of 2026-10-24 and 2026-10-25), **RECORD** (from the record of this repository: the Lagrangian of dirac16complex with its
canonical spin connection and contact self-interaction, the Kohn-Sham treatment), **STANDARD** (textbook physics or a published
measurement, named), **ASSUMED** (a choice of UM-4 without derivation), **INVENTED** (a new interaction of UM-4: the portals of
dirac16complex), **DERIVED** (computed and verified in UM-4: the program and the check that verify it are named), **ESTIMATE** (an
order-of-magnitude evaluation) and **OPEN** (not settled).

## Every equation is followed by its symbols

Every display equation is followed by the list of EVERY symbol that appears in it, with its meaning, unit (natural units, in which the
reduced Planck constant $\hbar$ and the speed of light $c$ are 1), value and status. The author's coordinates are
$X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ the hidden space-like coordinate (the metric depends on it
through $z = 6Hx_0$), $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ three extra time-like coordinates; the signature
is $(+,+,+,+,-,-,-,-)$ in this order. $H$ is the author's constant (an inverse length), a free parameter of UM-4 bounded from below by
2534 GeV (about 2.5 TeV). A prime on a function of the time $x_4$ alone is its derivative with respect to $x_4$, on a profile (a function of the
proper coordinate $\sigma$ of the hidden direction alone) its derivative with respect to $\sigma$. The Higgs doublet, the quarks and the
leptons live on the fold of the metric (the surface $z = \pi/2$, where $\sigma = 0$; ASSUMED); gravity, dirac16complex and the gauge fields
of the Standard Model live in the bulk (the photon there by the author's order; ASSUMED for the other gauge fields).

## The answers in brief

1. **The $x_0$ mass mechanism.** The coordinate $x_0$ has the period $\pi/(6H)$, but one period is a hidden direction of infinite proper
   length, warped towards the fold: there is no compact dimension, no tower of Kaluza-Klein masses with the spacing $12H$, and no
   uncertainty bound $p_{\mathrm{h}} \gtrsim 6H$ on the momentum along the hidden direction. Because the time is warped like every other
   direction of the fold, the hidden direction gives no gap either (UM-3 had the gaps $3H$ for scalars and $2H$ for gauge fields): every
   massless field of the bulk has one massless mode bound to the fold and a continuum of massive modes that starts at zero mass. The
   continuum reaches the fold with a weight that vanishes like the fourth power of the mass over $H$ for the graviton and the scalars and
   like its square for the gauge fields; the observer on the fold sees it only as corrections to Newton's and Coulomb's laws at distances
   of the order of $1/H$ and as decays of the W and Z bosons into the bulk, which bound $H$ from below by 2534 GeV. For dirac16complex the
   continuum starts at zero frequency, and the fold holds long-lived resonances (the particles $\chi$) with the mass
   $\omega_{\mathrm{r}} \simeq \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}}))$, $\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2}$, and the width
   $(2/\mathrm{e})(q_{\mathrm{b}}^2/m_\Psi)\exp(-2F(\upsilon_{\mathrm{b}})m_\Psi/H)$, exponentially small in $m_\Psi/H$. Their masses come from the binding to the
   fold, not from the period of $x_0$ (DERIVED).
2. **Dark matter.** The particles $\chi$ cannot decay into the Standard Model alone, but they tunnel into the bulk: they live longer than
   160 Gyr (the bound for dark matter that decays into invisible particles) only if $m_\Psi/H$ is above 1135 for the binding
   $q_{\mathrm{b}} = m_\Psi/2$, so with $H > 2534$ GeV they are then heavier than $2.5\times10^6$ GeV; the bound falls with the binding, to
   $1.2\times10^4$ GeV for $q_{\mathrm{b}} = 0.99\,m_\Psi$. They gravitate on the fold like matter of the fold, and a dilute gas of them is
   pressureless: cold dark matter. A thermal relic is possible only up to $9.7\times10^4$ GeV (unitarity), so only particles bound more
   strongly than $q_{\mathrm{b}} \approx 0.9\,m_\Psi$ could be one. The portals of the author's action cannot bind them so: bound by the Higgs
   portal they would have to be bound so weakly (direct detection) that they would live long enough only for $H < 2.5$ GeV, and bound by
   the gluon condensate they would scatter on nucleons far above the limits; nor can the current portals, which annihilate them only with
   the fourth power of the velocity, set the relic density of a perturbatively coupled $\chi$. dirac16complex can be the dark matter of UM-4
   only with a binding to the fold that does not couple $\chi$ to nucleons, and, unless that binding is strong, with a non-thermal origin of
   its abundance; the action of UM-4 contains neither (DERIVED, ESTIMATE, OPEN).
3. **Dark energy.** No: the gas of the particles $\chi$ has a positive pressure that vanishes in the dilute limit, never a negative one.
   The dark energy of UM-4 is the excess of the tension of the fold over the value $\lambda_{\mathrm{F}}$ that the static bulk requires, a
   vacuum energy with the equation of state $w = -1$; the observed value needs the tension tuned to one part in $10^{92}$ for $H = 2534$ GeV.
   It fits the cosmic microwave background (CMB) but keeps the tension of the cosmological-constant model with the baryon acoustic
   oscillations (BAO) of DESI DR2, 2.3 standard deviations in DESI's own analysis (DERIVED: $w = -1$; STANDARD: the tension; OPEN: the
   tuning).
4. **The open questions.** The Krein norm: the vacuum cannot decay; whether a gas of $\chi$ is classically stable is not decided by the
   computations (its symmetric occupation is a saddle of the first-order energy, which has no lower bound); the chiral couplings of the fold
   (the author's left-handed Higgs portal among them) produce ghosts, so UM-4 with them is not unitary. The extra times: every field with a
   momentum along them larger than its mass and its momentum along ordinary space is tachyonic, and compact extra times do not help; UM-4
   needs a gauge principle that removes that momentum. Faster than light: no particle and no signal that stays at fixed extra times is
   observably faster than light: every massless field of the bulk travels at the speed of light, every state of dirac16complex obeys
   $\omega^2 = \omega_0^2 + k^2$ exactly, no signal through the static bulk at fixed extra times arrives earlier than light along the fold, and
   around the expanding fold the bulk is ahead by $4.4\times10^{-94}$ of the travel time over the Hubble distance; along the extra times the
   light cone of the four time-like directions gives no such bound and allows closed time-like curves. The primordial era: the author's vacuum is not a
   solution; the exact de Sitter fold inflates the extra times as well; an inflation with frozen extra times needs a Weyl tensor of the
   bulk and, in the regime of general relativity, a rate below $H/10$; the inflaton is not specified. The neutrinos: the Dirac phase drops
   out of every result; the lightest mass is below 23 meV and changes only the capture rate of the cosmic neutrinos (DERIVED, ESTIMATE;
   OPEN: the stability of the gas, a unitary coupling, the gauge principle, the inflaton).
5. **What was left out.** UM-4 had to add right-handed quarks and Yukawa couplings, three right-handed neutrinos (accepted by the author),
   a thin fluid on the fold (a tension and a pressure along the extra times that holds their volume fixed), the gauge field that the
   author's ad hoc Higgs vacuum needs, the choice of the gravity (Einstein gravity) and the gauge fields in the bulk; the dark matter of
   UM-4 needs a binding of $\chi$ to the fold and an origin of its abundance that the action does not contain. The last sections list the
   additions and the open problems and compare UM-4 with UM-3.

# The $x_0$ mass mechanism

## The period of $x_0$ and the proper length of the hidden direction

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

The metric of UM-4 and its proper chart. The metric depends on $x_0$ only through $z = 6Hx_0$, so its coefficients repeat with the
coordinate period $\pi/(6H)$: one period is $0 < z < \pi$, with the fold at $z = \pi/2$ and the tips at $z = 0$ and $z = \pi$, where
$g_{x_0x_0} = \cot^2z$ diverges and the warp factor $(\sin^2z)^{1/6}$ vanishes. In the proper coordinate $\sigma$ the warp factor
$\mathrm{e}^{-2H\lvert\sigma\rvert}$ multiplies the whole metric of the fold, the time included (UM-3: the time was not warped). Status: AUTHOR
(the metric and the order of 2026-10-25, 13:15 PDT), DERIVED (the chart, `um4_geometry.py`, G1).

$$
\int_0^{\pi/(6H)}\sqrt{\cot^2(6Hx_0)}\;\mathrm{d}x_0 = \frac{1}{6H}\int_0^{\pi}\lvert\cot z\rvert\,\mathrm{d}z = \infty,\qquad
\sigma(z) = \mathrm{sgn}\Big(\frac{\pi}{2} - z\Big)\frac{\ln\sin z}{6H} \to \mp\infty\ \ (z \to 0,\ \pi) \tag{A-1}
$$
<!-- symbols: x0, Hconst, diff, zvar, pi, infty, sigma, sgn -->
<!-- begin generated symbol list -->
**Symbols in (A-1).**

- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$, the fold is $z = \pi/2$. Unit: dimensionless. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{sgn}$: The sign function: $+1$ for a positive argument and $-1$ for a negative one. Status: STANDARD.

<!-- end generated symbol list -->

The proper length of one period of $x_0$ is infinite: $\lvert\cot z\rvert$ diverges at the tips like $1/z$, so its integral diverges
logarithmically, and the proper coordinate $\sigma$ runs over the whole line. The hidden direction is not a circle of circumference
$\pi/(6H)$ but an infinite line, warped by $\mathrm{e}^{-H\lvert\sigma\rvert}$ away from the fold; the tips are infinitely far away. The component
$g_{x_0x_0}$ is the author's and is the same in UM-3 and UM-4. Status: DERIVED (`um4_geometry.py`, G1: the proper chart on both halves of
the period).

$$
\begin{aligned}
&p_{\mathrm{h}} \gtrsim \frac{\pi}{\pi/(6H)} = 6H,\qquad m_{\mathrm{KK}}^2 = m_\Psi^2 + \big(12H\,\mathsf{k}\big)^2\ \ (\mathsf{k} = 0, \pm1, \pm2, \dots)\\
&\text{(for a compact direction of length } \pi/(6H)\text{, not UM-4)}
\end{aligned} \tag{A-2}
$$
<!-- symbols: ph, pi, Hconst, mKK, mPsi, kint -->
<!-- begin generated symbol list -->
**Symbols in (A-2).**

- $p_{\mathrm{h}}$: The momentum along the hidden direction of a particle confined to it, if that direction were compact (not UM-4). Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $m_{\mathrm{KK}}$: The masses of the tower of modes of a field on a compact hidden direction (Kaluza-Klein masses; not UM-4). Unit: GeV. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathsf{k}$: An integer that numbers the modes of a compact direction. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

The mass mechanism one would expect if $x_0$ were a compact direction of proper length $\pi/(6H)$: a particle confined to it has, by the
uncertainty relation, a momentum $p_{\mathrm{h}}$ along $x_0$ of at least about $\pi$ divided by the length, $6H$, and a field periodic in $x_0$
has a tower of masses $m_{\mathrm{KK}}$ with the spacing $12H$ (the Kaluza-Klein masses, numbered by the integer $\mathsf{k}$). Status:
STANDARD (for a compact direction). Neither applies to UM-4, because the proper length is infinite (A-1).

## What the hidden direction produces instead

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

The massless fields of the bulk: a scalar (FE-73; each polarisation of the graviton obeys the same equation) and a gauge field (FE-74,
written for the hypercharge field), each a profile $u(\sigma)$ along the hidden direction times a field of the fold of the mass $m$. Because
the warp factor multiplies the frequency as well as the momentum, they enter only through $m^2 = \omega^2 - k^2$: every mode is a field of
the fold with the Lorentz-invariant dispersion $\omega^2 = k^2 + m^2$. The massless mode has the profile 1 and a finite kinetic weight, so it
is bound to the fold and travels at the speed of light at every wavelength. Status: DERIVED (`um4_bulk.py`, B1 and B2).

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

The propagator of a massless field of the bulk from one point of the fold to another: the response at the fold to a unit source on the fold,
for the Euclidean momentum $\mathsf{p}$ along the fold. Status: DERIVED (`um4_propagators.py`, P1).

$$
\begin{aligned}
&u \propto \zeta_{\mathrm{w}}^{n/2}\Big(\mathrm{Y}_{n/2-1}\big(m/H\big)\,\mathrm{J}_{n/2}\big(m\zeta_{\mathrm{w}}\big) - \mathrm{J}_{n/2-1}\big(m/H\big)\,\mathrm{Y}_{n/2}\big(m\zeta_{\mathrm{w}}\big)\Big),\qquad
 \zeta_{\mathrm{w}} = \frac{\mathrm{e}^{H\lvert\sigma\rvert}}{H},\\
&\mathbb{G}_n(\mathsf{p}) = \frac{(n - 2)H}{2\mathsf{p}^2} + \int_0^\infty\mathrm{d}m\,\frac{\mathfrak{s}_n(m)}{\mathsf{p}^2 + m^2},\qquad
 \mathfrak{s}_n(m) = \frac{2H}{\pi^2m\,\big[\mathrm{J}_{n/2-1}(m/H)^2 + \mathrm{Y}_{n/2-1}(m/H)^2\big]},\\
&\mathfrak{s}_7(m) \simeq \frac{(m/H)^4}{9\pi},\quad \mathfrak{s}_5(m) \simeq \frac{(m/H)^2}{\pi}\quad(m \ll H),\qquad \mathfrak{s}_n(m) \to \frac{1}{\pi}\quad(m \gg H)
\end{aligned} \tag{A-3}
$$
<!-- symbols: uprof, zetaw, inn, BesselY, mmass, Hconst, BesselJ, euler, sigma, Gprop, psE, diff, infty, specdens, pi -->
<!-- begin generated symbol list -->
**Symbols in (A-3).**

- $u(\sigma),\ u_0$: The profile along the hidden direction of a mode of a field of the bulk (a scalar, a gauge field or a polarisation of the graviton): the field is $u(\sigma)$ times a field of the fold; $u_0 = 1$ is the profile of the massless mode (the zero mode); in a propagator the response of the field to a unit source on the fold. Unit: dimensionless (a relative amplitude); length in a propagator. Status: DERIVED.
- $\zeta_{\mathrm{w}}$: The warped distance from the fold, $\zeta_{\mathrm{w}} = \mathrm{e}^{H\lvert\sigma\rvert}/H$ ($1/H$ at the fold): $\omega\zeta_{\mathrm{w}}$ is the argument of the exact solutions of dirac16complex, and $m\zeta_{\mathrm{w}}$ that of the massive modes of the mass $m$ of the massless fields of the bulk. Unit: length. Status: DERIVED.
- $n$: The label of a field of the bulk in its profile equation: the exponent of the weight $\mathrm{e}^{-nH\lvert\sigma\rvert}$ of its $\sigma$-derivatives, $n = 7$ for a scalar and for each polarisation of the graviton, $n = 5$ for a gauge field. Status: STANDARD.
- $\mathrm{Y}$: The Bessel function of the second kind (of the order written as its subscript): the second solution of Bessel's equation, singular at zero argument; for a half-integer order an elementary function. Unit: dimensionless. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\mathrm{J}$: The Bessel function of the first kind (of the order written as its subscript): the solution of Bessel's equation that is finite at zero argument; for a half-integer order it is an elementary function (sines, cosines and powers of its argument). Unit: dimensionless. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathbb{G}_n,\ \mathbb{G}_7,\ \mathbb{G}_5$: The propagator of a massless field of the bulk from one point of the fold to another, in the momentum space of the fold: the value at the fold of its response to a unit source on the fold; $\mathbb{G}_7$ for each polarisation of the graviton and for a scalar, $\mathbb{G}_5$ for a gauge field. Unit: GeV$^{-1}$. Status: DERIVED.
- $\mathsf{p}$: The Euclidean momentum along the fold of a source on the fold: $\mathsf{p}^2$ the square of its seven-dimensional momentum (for a static source spread uniformly over the extra times the square of its momentum along ordinary space); $\mathsf{p} = -\mathrm{i}m$ for a time-like momentum of the mass $m$ with outgoing waves into the bulk. Unit: GeV. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no bound. Status: STANDARD.
- $\mathfrak{s}_n(m),\ \mathfrak{s}_7,\ \mathfrak{s}_5$: The spectral density at the fold of the massive modes of a massless field of the bulk ($n = 7$ for a scalar and each polarisation of the graviton, $n = 5$ for a gauge field): the square of the value at the fold of the normalised even profile of the mode of the mass $m$, per unit of $m$; the weight with which the mode of the mass $m$ propagates from one point of the fold to another. Unit: dimensionless. Value: $\mathfrak{s}_7 \simeq (m/H)^4/(9\pi)$, $\mathfrak{s}_5 \simeq (m/H)^2/\pi$ for $m \ll H$; $1/\pi$ for $m \gg H$. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

The massive modes, the masses that the hidden direction produces. With the warped distance $\zeta_{\mathrm{w}}$ from the fold the profile
equations FE-73 ($n = 7$) and FE-74 ($n = 5$) become Bessel's equation: their solutions are $\zeta_{\mathrm{w}}^{n/2}$ times the Bessel
functions of the order $n/2$ of $m\zeta_{\mathrm{w}}$. The combination of the first line is the even mode, which has no kink at the fold
($u' = 0$ on both sides of it, as for a field without a source at the fold); the odd modes vanish at the fold and do not reach it, so the even
modes are the ones that the fold sees. Far from the fold every one of them oscillates, for every $m > 0$, and
the kinetic weight $\mathrm{e}^{-(n-2)H\lvert\sigma\rvert}\mathrm{d}\sigma$ is the measure of the Hankel transform in $\zeta_{\mathrm{w}}$: the massive
modes form a continuum that starts at zero mass, with no gap and no tower, beside the one massless mode. The second line is the spectral
representation of the propagator FE-79: the massless mode with the weight $(n - 2)H/2$ plus the continuum, each mass with the weight
$\mathfrak{s}_n(m)$, the square of the value at the fold of its normalised profile. For masses far below $H$ the weight vanishes like
$(m/H)^4$ for the graviton and the scalars and like $(m/H)^2$ for the gauge fields: the light modes of the continuum live far from the fold,
and only modes heavier than $H$ reach the fold with full strength. (A record of UM-3, whose time was not warped: there the massless fields of
the bulk had a gap above their massless mode, $3H$ for a scalar and $2H$ for a gauge field; at zero momentum the profile equation of the
scalar, $u'' - 6H\,\mathrm{sgn}(\sigma)\,u' + \omega^2u = 0$, has no oscillating solutions below $\omega = 3H$.) Status: DERIVED (`um4_bulk.py`, B10:
the exact solutions with sympy on both halves, the measure, and the spectral representation, which reproduces FE-79 to $6\times10^{-16}$ at
$\mathsf{p}/H = 0.3$, 1 and 3).

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

What the observer on the fold sees of the continuum. Between two point sources on the fold at the distance $r$ the massless mode gives
Newton's law (the first potential, multiplied by the gravitational coupling) and Coulomb's law (the second, multiplied by the square of the
gauge coupling), and the continuum adds the relative corrections $16/(15\pi(Hr)^5) = 0.3395/(Hr)^5$ and $4/(3\pi(Hr)^3) = 0.4244/(Hr)^3$: they
are the integrals of the weights $\mathfrak{s}_7$ and $\mathfrak{s}_5$ of A-3 against the Yukawa factor $\mathrm{e}^{-mr}$ of each mass, divided by
the weight of the massless mode, and the computed integrals approach them (0.33945 and 0.42429 at $Hr = 200$). For $H = 2534$ GeV they are
$2.6\times10^{-75}$ at 52 micrometres, the shortest distance at which torsion balances test Newton's law ($2.7\times10^{-75}$ for $H = 2.5$ TeV), and
$1.4\times10^{-27}$ at the Bohr radius.
The mass that the Higgs vacuum gives the gauge fields at the fold turns the W and Z bosons into resonances of the bulk (FE-82): they can decay
into the continuum, with the width $\Gamma_{\mathrm{bulk}} = m_0^4/(3H^3)$, and the measured invisible width of the Z boson (the number of light
neutrinos $2.9963 \pm 0.0074$, which allows at most 1.42 MeV of extra invisible width) requires $H > 2534$ GeV (about 2.5 TeV), the bound used
in every UM-4 document. Status: DERIVED (`um4_propagators.py`, P3 and P4; `um4_bulk.py`, B10), ESTIMATE (the bounds, P5).

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

- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $c^{W}_X$: The $W$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle W^2\rangle$: The mean square of the $SU(2)$ field strength, $\langle W^I_{\mu\nu}W^{I\mu\nu}\rangle$. Unit: GeV$^4$. Status: STANDARD.
- $W^I_M,\ W^I_\mu,\ W^I_{MN}$: The gauge field of $SU(2)_L$ ($I = 1, 2, 3$): in the bulk $W^I_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $W^I_\mu(x)$ of its massless mode, $g_2W^I_\mu(x) = W^I_\mu(\sigma = 0, x)$; $W^I_{MN}$, $W^I_{\mu\nu}$ their field strengths; $W^\pm_\mu = (W^1_\mu \mp \mathrm{i}W^2_\mu)/\sqrt2$. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $c^{B}_X$: The $B$-kinetic portal coupling of the half $X$. Unit: GeV$^{-7}$. Status: INVENTED.
- $\langle B^2\rangle$: The mean square of the hypercharge field strength, $\langle B_{\mu\nu}B^{\mu\nu}\rangle$. Unit: GeV$^4$. Status: STANDARD.
- $B_M,\ B_\mu,\ B_{MN}$: The hypercharge gauge field of $U(1)_Y$: in the bulk $B_M$ (geometric normalisation), on the fold the canonically normalised four-dimensional field $B_\mu(x)$ of its massless mode, $g_1B_\mu(x) = B_\mu(\sigma = 0, x)$; $B_{MN}$, $B_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $n_f$: The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium. Unit: GeV$^3$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $\mathcal{A}$: The author's ad hoc upper component of the Higgs vacuum, almightyAdHoc, $\mathcal{A}(x_4) = v_{\mathcal{A}}\mathrm{e}^{-2a_{40}x_4}$. Unit: GeV. Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\begin{aligned}
&q_{\mathrm{b}} = -m_\Psi\,\big(\mu_{\mathrm{L}} + \mu_{\mathrm{R}}\big)\,\frac{\tanh\varsigma}{2\varsigma},\qquad \varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}},\qquad
\omega_{\mathrm{b}} = \sqrt{m_\Psi^2 - q_{\mathrm{b}}^2},\\
&\omega_{\mathrm{r}} = \omega_{\mathrm{b}}\Big(1 - \frac{H}{2q_{\mathrm{b}}}\Big) + \dots,\qquad
\lvert\chi_{\mathrm{b}}(\sigma)\rvert \propto \mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}\quad\big(\lvert\sigma\rvert \ll \sigma_{\mathrm{t}}\big)
\end{aligned} \tag{FE-40}
$$
<!-- symbols: qb, mPsi, muX, varsigma, omegab, omegar, Hconst, chib, euler, sigma, sigmat -->
<!-- begin generated symbol list -->
**Symbols in (FE-40).**

- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $\varsigma$: The auxiliary variable of the bound-state condition, $\varsigma = \sqrt{\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ ($\varsigma_- = \sqrt{-\mu_{\mathrm{L}}\mu_{\mathrm{R}}}$ when $\mu_{\mathrm{L}}\mu_{\mathrm{R}} < 0$). Unit: dimensionless. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{r}}$: The mass of the particle $\chi$: the real part of the energy at rest of the resonance of dirac16complex at the fold, $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\chi_{\mathrm{b}}$: The profile of a state of dirac16complex at the fold (a resonance): it decays as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$ out to the turning point and continues beyond it as an outgoing wave of exponentially small amplitude. Unit: GeV$^{2}$. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\sigma_{\mathrm{t}}$: The turning point of a state of dirac16complex of the frequency $\omega$: the depth at which the warped frequency equals the bulk mass, $\lvert\omega\rvert\mathrm{e}^{H\sigma_{\mathrm{t}}} = m_\Psi$; beyond it every solution oscillates. Unit: length. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

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

dirac16complex, the author's field, on the static block (the late-time state of the metric, in which $a_4$ and $b_4$ are constant). At zero
momentum (FE-37) the local gap $m_\Psi^2 - \omega^2\mathrm{e}^{2H\lvert\sigma\rvert}$ of its profile closes at the turning point $\sigma_{\mathrm{t}}$, because the
warped frequency grows away from the fold; beyond it every solution oscillates. Its continuum therefore starts at zero frequency, and the
fold, which acts on it as a chirality-dependent mass concentrated at $\sigma = 0$ with the strengths $\mu_{\mathrm{L}}$ and $\mu_{\mathrm{R}}$ set by the
mean fields of the Standard Model (FE-39), holds no bound states but resonances (FE-40, FE-86): eight states, four of each Krein sign, whose
profile decays at the local rate $q(\sigma)$ of FE-37 ($q_{\mathrm{b}}$ close to the fold, 0 at the turning point) and continues beyond the turning
point as an outgoing wave of exponentially small amplitude. Their mass $\omega_{\mathrm{r}}$ is the energy $\omega_{\mathrm{b}}$ of the bound states of UM-3
lowered by the warped time, and their width $\Gamma_\chi$ is the rate of the tunnelling through the region inside the turning point, with the
prefactor $p_{\mathrm{w}} = (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ derived from the asymptotic forms of the exact solutions. Computed with the author's exact
$16 \times 16$ matrices for a fold bound by the Higgs portal alone ($\mu_{\mathrm{L}} = -1$, $\mu_{\mathrm{R}} = 0$): $\omega_{\mathrm{r}}/m_\Psi = 0.7785$, 0.8175,
0.8333 and 0.8418 and $\Gamma_\chi/m_\Psi = 0.0587$, 0.0180, 0.00670 and 0.00263 for $m_\Psi/H = 10$, 20, 30 and 40, approaching the bound state
of UM-3, 0.8660, as $H/m_\Psi \to 0$; the prefactor of the computed widths approaches $p_{\mathrm{w}} = 0.18394$ like $H/m_\Psi$ (0.18356 at
$m_\Psi/H = 4000$). Status: DERIVED (`um4_spectra.py`, U1 to U4, U7).

$$
\ell_{\mathrm{b}} = \sqrt{\big\langle\sigma^2\big\rangle} = \frac{1}{\sqrt2\,q_{\mathrm{b}}},\qquad
m_\Psi - \omega_{\mathrm{r}} = \big(m_\Psi - \omega_{\mathrm{b}}\big) + \frac{\omega_{\mathrm{b}}H}{2q_{\mathrm{b}}} + \dots,\qquad
m_\Psi - \omega_{\mathrm{b}} \approx \frac{q_{\mathrm{b}}^2}{2m_\Psi} = \frac{1}{4m_\Psi\,\ell_{\mathrm{b}}^2}\quad\big(q_{\mathrm{b}} \ll m_\Psi\big) \tag{A-4}
$$
<!-- symbols: ellb, mean, sigma, qb, mPsi, omegar, omegab, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (A-4).**

- $\ell_{\mathrm{b}}$: The width of a state of dirac16complex at the fold along the hidden direction: the root mean square of $\sigma$ in its density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$ inside the turning point. Unit: length. Value: $1/(\sqrt2\,q_{\mathrm{b}})$. Status: DERIVED.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\omega_{\mathrm{r}}$: The mass of the particle $\chi$: the real part of the energy at rest of the resonance of dirac16complex at the fold, $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.

<!-- end generated symbol list -->

The width and the mass of the particles $\chi$: their width $\ell_{\mathrm{b}}$ along the hidden direction (the root mean square of $\sigma$ in the
density $\mathrm{e}^{-2q_{\mathrm{b}}\lvert\sigma\rvert}$ inside the turning point) and their mass deficit below the bulk mass. The states obey the ordinary
uncertainty relation: the mean square of the momentum along $\sigma$ in the profile $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$ is $q_{\mathrm{b}}^2$, so that
$\langle p_\sigma^2\rangle\langle\sigma^2\rangle = 1/2$. The narrower the state, the larger the deficit, because a narrower state is held by a stronger
attraction of the fold: the energy falls not because the particle is confined (in the compact case confinement raises it) but because the fold
binds it more strongly. The warped time lowers the mass further by $\omega_{\mathrm{b}}H$ times the mean distance $\langle\lvert\sigma\rvert\rangle = 1/(2q_{\mathrm{b}})$
of the state from the fold (the redshift of its energy, averaged over its profile). The $x_0$ mass of dirac16complex is therefore a binding
mass, set by the bulk mass and by the strengths of the fold terms, not by the period of $x_0$. Status: DERIVED (`um4_kohnsham.py`, K1: the
level equals $\omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}}))$ up to a term of the second order in $H$).

## The answer

The period $\pi/(6H)$ of the coordinate $x_0$ does not produce a mass by the uncertainty relation, because one period is an infinite proper
distance. In UM-4 the hidden direction produces neither a tower nor a gap: every massless field of the bulk has one massless mode bound to the
fold and a continuum of massive modes from zero mass upwards, which reaches the fold with the weight $\mathfrak{s}_n(m)$, vanishing like
$(m/H)^4$ (graviton, scalars) or $(m/H)^2$ (gauge fields) for light modes; the fold sees it as the corrections $0.34/(Hr)^5$ to Newton's law and
$0.42/(Hr)^3$ to Coulomb's law and as the widths of the W and Z bosons into the bulk. For dirac16complex the fold holds eight long-lived
resonances of mass $\omega_{\mathrm{r}} \simeq \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}}))$, which are lighter the narrower they are, because a narrower state is
bound more strongly, and which decay into the bulk at a rate exponentially small in $m_\Psi/H$. Status: DERIVED.

# dirac16complex as dark matter

## Stability and lifetime

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

$$
\begin{aligned}
&Q_\Psi = \int\mathrm{d}\sigma\,\mathrm{d}^3x\,\sqrt{\lvert g\rvert}\;\mathrm{e}^{H\lvert\sigma\rvert}\,\Psi^\dagger\mathfrak{B}\Psi
 = b_4^3\int\mathrm{d}\sigma\,\mathrm{d}^3x\;\mathrm{e}^{H\lvert\sigma\rvert}\,\chi^\dagger\mathfrak{B}\chi,\\
&\mathfrak{B} = \mathrm{i}\,\sigma_{16}\,\gamma^{(4)},\qquad \mathfrak{B}^\dagger = \mathfrak{B},\qquad \mathfrak{B}^2 = \mathbf{1},\qquad
E_o = -\omega_o\,\mathcal{Q}_o
\end{aligned} \tag{FE-43}
$$
<!-- symbols: QPsi, diff, sigma, xfour, metric, euler, Hconst, Psi, dagger, Bkrein, b4, chiprof, imag, sigma16, gammaM, identity, Eorb, io, omegafreq, Qorb -->
<!-- begin generated symbol list -->
**Symbols in (FE-43).**

- $Q_\Psi$: The conserved charge of dirac16complex (the Noether charge of a change of the phase of $\Psi$ by a constant), a Krein form (indefinite); as written it is the charge per unit coordinate volume of the extra times, on which no field depends. Unit: GeV$^3$. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $x$: The coordinates of the fold: $x_1, x_2, x_3$ of ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times; a field of the fold is a function of the four observable coordinates $x = (x_1, x_2, x_3, x_4)$, and $\mathrm{d}^4x = \mathrm{d}x_1\,\mathrm{d}x_2\,\mathrm{d}x_3\,\mathrm{d}x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\mathfrak{B}$: The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density. Unit: dimensionless. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $\chi(\sigma)$: The profile of a mode of dirac16complex along the hidden direction, $\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi(\sigma)\mathrm{e}^{\mathrm{i}(\vec k\cdot\vec x - \omega x_4)}$ (a 16-component spinor function of $\sigma$); as a four-dimensional field, $\chi$ denotes the particle of the level of dirac16complex at the fold (a long-lived resonance) and $\bar\chi$ its antiparticle. Unit: GeV$^{2}$ (with the $V_*$ normalisation). Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\sigma_{16}$: The matrix of the Dirac adjoint, $\sigma_{16} = T_0T_1T_2T_3$, real and symmetric; $\sigma_{16}T_a$ is real and antisymmetric. Unit: dimensionless. Status: AUTHOR.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1},\ \mathbf{1}_4,\ \mathbf{1}_8,\ \mathbf{1}_{16}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_4$, $\mathbf{1}_8$ and $\mathbf{1}_{16}$ are the identity matrices of 4, 8 and 16 rows. Unit: dimensionless. Status: STANDARD.
- $E$: An energy: $E_o$ the energy of the Kohn-Sham orbital $o$; in the neutrino sector the energy of a neutrino. Unit: GeV. Status: STANDARD.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $\mathcal{Q}_o$: The charge $Q_\Psi$ (the Krein charge) of the single-particle state $o$ of dirac16complex, a Kohn-Sham orbital or a mode: $+1$ or $-1$ for a normalised state. Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The portals of dirac16complex to the Standard Model (IN-16) and its conserved charge (FE-43). Every portal term, like the bulk Lagrangian and
the self-interaction, contains dirac16complex only in the bilinears $\bar\Psi\cdots\Psi$: the action is invariant under a constant change of the
phase of $\Psi$, and the charge $Q_\Psi$ is conserved. A particle $\chi$ can therefore annihilate only with an antiparticle, and it cannot decay
into the Standard Model alone. Conservation of $Q_\Psi$ does not by itself make it stable, for two reasons. The first is the indefinite Krein
form of the charge: with $E_o = -\omega_o\mathcal{Q}_o$, a particle of positive energy (charge $-1$ at $+\omega_{\mathrm{r}}$) could turn into a state of
negative energy with the same charge and Standard-Model quanta that carry away the difference; the quantisation of the charge settles this (the
section on the open questions, FE-67): in the positive-energy quantisation every quantum carries a positive energy, so no such decay exists and
the vacuum cannot decay. The second is new in UM-4: the particle $\chi$ is a resonance of the fold and decays into the waves of dirac16complex in the
bulk, which carry its charge away from the fold (FE-86). Status: DERIVED (no decay into the Standard Model alone, from the form of IN-16; the
Krein signature, `um4_fields.py`, F3, and `um4_spectra.py`, U7; the quantisation, `um4_krein.py`, KR1; the width, `um4_spectra.py`, U3 and U4).

$$
\Gamma_\chi < \frac{1}{11.6\,t_0}\quad\Leftrightarrow\quad
\frac{m_\Psi}{H} > \frac{\ln\big(11.6\,p_{\mathrm{w}}\,m_\Psi\,t_0\big)}{2F(\upsilon_{\mathrm{b}})},\qquad
p_{\mathrm{w}} \simeq \frac{2}{\mathrm{e}}\,\frac{q_{\mathrm{b}}^2}{m_\Psi^2},\qquad
F(\upsilon_{\mathrm{b}}) \simeq \frac13\Big(\frac{q_{\mathrm{b}}}{\omega_{\mathrm{b}}}\Big)^3 - \frac{3}{10}\Big(\frac{q_{\mathrm{b}}}{\omega_{\mathrm{b}}}\Big)^5\quad
\Big(\frac{q_{\mathrm{b}}}{\omega_{\mathrm{b}}} \ll 1\Big) \tag{S-6}
$$
<!-- symbols: Gammachi, tzero, mPsi, Hconst, pw, euler, Fwkb, upsilonr, qb, omegab -->
<!-- begin generated symbol list -->
**Symbols in (S-6).**

- $\Gamma_\chi$: The width of the particle $\chi$ at rest: the rate of its decay into the waves of dirac16complex in the bulk. Unit: GeV. Value: below $1/(11.6\,t_0) = 1.3\times10^{-43}$ GeV for dark matter (a lifetime above 160 Gyr). Status: DERIVED.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $p_{\mathrm{w}}$: The prefactor of the width of the particles $\chi$, $\Gamma_\chi = p_{\mathrm{w}}m_\Psi\mathrm{e}^{-2F(\upsilon_{\mathrm{b}})m_\Psi/H}$: $p_{\mathrm{w}} \simeq (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ to the leading order in $H/q_{\mathrm{b}}$ (FE-86; 0.184 for $q_{\mathrm{b}} = m_\Psi/2$). Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $F(\upsilon)$: The tunnelling exponent of the width of the particles $\chi$ per unit of $m_\Psi/H$: the integral of the local decay rate $q$ over the region inside the turning point, divided by $m_\Psi/H$, as a function of the ratio $\upsilon$ of the energy to the bulk mass. Unit: dimensionless. Value: 0.049 for $\upsilon = 0.866$; $(q_{\mathrm{b}}/\omega_{\mathrm{b}})^3/3$ for weak binding. Status: DERIVED.
- $\upsilon,\ \upsilon_{\mathrm{b}},\ \upsilon_{\mathrm{r}}$: The argument of the tunnelling exponent $F$, a ratio of an energy to the bulk mass $m_\Psi$; $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ that of the particle $\chi$ in the limit $H/q_{\mathrm{b}} \to 0$, $\upsilon_{\mathrm{r}} = \omega_{\mathrm{r}}/m_\Psi$ that of the real part of its resonance. Unit: dimensionless. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The lifetime that the dark matter requires. The particles $\chi$ that make up the dark matter today must live longer than 160 Gyr,
11.6 times the age $t_0 = 13.8$ Gyr of the universe: the bound on the lifetime of dark matter that decays into invisible relativistic
particles, from the cosmic microwave background and the large-scale structure (B. Audren, J. Lesgourgues, G. Mangano, P. D. Serpico and
T. Tram, JCAP 12 (2014) 028, arXiv:1407.2418), $\Gamma_\chi < 1.3\times10^{-43}$ GeV. With the width of FE-86, whose prefactor
$p_{\mathrm{w}} = (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ is derived from the asymptotic forms of the exact solutions, this bounds $m_\Psi/H$ from below; the
tunnelling exponent grows with the binding, and for weak binding it is small, $F \simeq (q_{\mathrm{b}}/\omega_{\mathrm{b}})^3/3$, so that the bound grows
like $(\omega_{\mathrm{b}}/q_{\mathrm{b}})^3$. With $H$ at its lower bound 2534 GeV (the exact widths at the bound, within 4 per cent of $p_{\mathrm{w}}$):

| $q_{\mathrm{b}}/m_\Psi$ | $q_{\mathrm{b}}/\omega_{\mathrm{b}}$ | $F(\upsilon_{\mathrm{b}})$ | $p_{\mathrm{w}}$ | $m_\Psi/H$ above | $\omega_{\mathrm{b}}$ above (GeV) |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 0.0995 | 0.100 | $3.30\times10^{-4}$ | 0.0073 | $1.72\times10^5$ | $4.34\times10^8$ |
| 0.3 | 0.314 | $9.52\times10^{-3}$ | 0.066 | 5911 | $1.43\times10^7$ |
| 0.5 | 0.577 | 0.0493 | 0.184 | 1135 | $2.49\times10^6$ |
| 0.7 | 0.980 | 0.167 | 0.361 | 333 | $6.02\times10^5$ |
| 0.8 | 1.333 | 0.299 | 0.471 | 186 | $2.83\times10^5$ |
| 0.9 | 2.065 | 0.572 | 0.596 | 96.7 | $1.07\times10^5$ |
| 0.95 | 3.04 | 0.882 | 0.664 | 62.5 | $4.95\times10^4$ |
| 0.99 | 7.02 | 1.66 | 0.721 | 33.1 | $1.18\times10^4$ |
| 0.999 | 22.3 | 2.80 | 0.734 | 19.5 | $2.21\times10^3$ |

The particles $\chi$ of UM-4 are therefore heavier than $2.5\times10^6$ GeV for $q_{\mathrm{b}} = m_\Psi/2$, more for weaker binding, and the bound
falls as the binding grows ($1.2\times10^4$ GeV for $q_{\mathrm{b}} = 0.99\,m_\Psi$); for the age $t_0$ instead of 160 Gyr the bounds are about 2 per cent
lower. A particle moving with the momentum $\vec k$ has the energy $\sqrt{\omega_0^2 + \vec k^2}$ and its width is dilated by the factor
$\omega_{\mathrm{r}}/\sqrt{\omega_{\mathrm{r}}^2 + \vec k^2}$, as for any unstable particle. Status: DERIVED (`um4_spectra.py`, U6: the exact widths at the
bounds), ESTIMATE (the measured bound on the lifetime is an input).

## Gravitation on the fold

$$
\kappa\int_{\text{layer}}\mathcal{T}_\Psi{}^a{}_b\,\mathrm{d}\sigma = \frac{\kappa}{\mathcal{Z}\,V_*}\,\mathcal{T}_\chi{}^a{}_b\qquad\big(H \ll q_{\mathrm{b}}\big) \tag{A-5}
$$
<!-- symbols: kappa, TPsi, ia, ib, diff, sigma, Zfold, Vstar, Tchi, Hconst, qb, SPsi -->
<!-- begin generated symbol list -->
**Symbols in (A-5).**

- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\mathcal{T}_\Psi$: The energy-momentum tensor of dirac16complex: $-2/\sqrt{\lvert g\rvert}$ times the variation of the action $S_\Psi$ of dirac16complex with respect to $g^{MN}$. Unit: GeV$^8$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathcal{Z}$: The fold factor, $\mathcal{Z}(x_4) = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3/V_*$: the factor by which the size of the extra times multiplies every term of the fold and the kinetic terms of the massless modes of the fields of the bulk; $\mathcal{Z} = 1$ when the extra times are frozen at their late value. Unit: dimensionless. Value: 1 in the late universe. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\mathcal{T}_\chi{}^a{}_b$: The four-dimensional energy-momentum tensor of the gas of the particles $\chi$ of dirac16complex (its long-lived states at the fold), per proper volume of ordinary space at the fold (energy density $\rho_\chi$). Unit: GeV$^4$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $S_\Psi$: The action of dirac16complex in the bulk (kinetic term with the canonical spin connection, mass term, contact self-interaction). Unit: dimensionless. Status: RECORD.

<!-- end generated symbol list -->

The particles $\chi$ live in the bulk, in a layer of the width $1/q_{\mathrm{b}}$ around the fold. The junction condition of the fold integrates the
bulk field equations across the fold: the jump of the extrinsic curvature across the fold equals $\kappa$ times the energy-momentum tensor of
everything that lives on the fold. If the layer is thin compared with the scale $1/H$ on which the metric varies, integrating across the whole
layer gives that jump the additional source A-5, where $\mathcal{T}_\chi$ is the four-dimensional energy-momentum tensor of the gas of $\chi$ (per
proper volume of ordinary space) and $\mathcal{Z}V_*$ the proper volume of the extra times at the fold ($\mathcal{Z} = 1$ with frozen extra times).
This is exactly the form in which the matter of the fold enters (the energy-momentum tensor of the Standard Model divided by the volume of the
extra times): the particles $\chi$ gravitate on the fold like matter of the fold, with the same Newton constant, and enter the Friedmann
equations FE-59 as $\rho_\chi$. In UM-4 the bulk is a vacuum of Einstein gravity with linear gravitons, so the response of the bulk to the part of
the source away from $\sigma = 0$ is linear in it, and the corrections to A-5 are of the relative order $H/q_{\mathrm{b}}$: at most $2\times10^{-3}$
for the long-lived particles with $q_{\mathrm{b}} \le m_\Psi/2$ ($m_\Psi/H > 1135$ at $q_{\mathrm{b}} = m_\Psi/2$, less for weaker binding), but up to 0.03 and
0.05 for the strongly bound ones at the bounds of S-6 ($q_{\mathrm{b}} = 0.99\,m_\Psi$ and $0.999\,m_\Psi$) (in UM-3, whose static bulk was a degenerate
vacuum without a linear part, their size was not known). Status: DERIVED (the
integration across a thin layer), ESTIMATE (the size of the corrections).

## The equation of state of the Kohn-Sham states

$$
\begin{aligned}
&\Psi = \mathrm{e}^{\frac72H\lvert\sigma\rvert}\,\chi_o(\sigma)\,\mathrm{e}^{-\mathrm{i}\omega x_4},\qquad
 \chi_o' = \gamma^{(0)}\Big(\mathrm{i}\omega\,\mathrm{e}^{H\lvert\sigma\rvert}\gamma^{(4)} + m_\Psi + \mathcal{M}(\sigma)\Big)\chi_o\qquad(\sigma \ne 0),\\
&\mathcal{M}(\sigma) = G_{\mathrm{KS}}\,\mathrm{e}^{7H\lvert\sigma\rvert}\Big(\hat\rho(\sigma)\,\mathbf{1} - \hat{\mathcal{N}}(\sigma)\Big),\qquad
 \hat\rho = \frac14\sum_{o=1}^{4}\bar\chi_o\chi_o,\qquad \hat{\mathcal{N}} = \frac14\sum_{o=1}^{4}\chi_o\bar\chi_o,\\
&\chi_o(0^+) = \exp\Big(\gamma^{(0)}\big(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}}\big)\Big)\chi_o(0^-),\qquad
 \int\mathrm{d}\sigma\,\mathrm{e}^{H\lvert\sigma\rvert}\,\chi_o^\dagger\mathfrak{B}\chi_p = -\delta_{op},\qquad G_{\mathrm{KS}} = \frac{\lambda_\Psi\,n_\chi}{V_*}
\end{aligned} \tag{S-7}
$$
<!-- symbols: Psi, euler, Hconst, sigma, chiKS, io, ip, imag, omegafreq, x4, prime, gammaM, mPsi, Mmean, GKS, rhohat, identity, Nhat, muX, PL, PR, diff, dagger, Bkrein, delta, lamPsi, nchi, Vstar -->
<!-- begin generated symbol list -->
**Symbols in (S-7).**

- $\Psi,\ \bar\Psi$: dirac16complex: the author's 16-component complex spinor field of eight dimensions; $\bar\Psi = \Psi^\dagger\sigma_{16}$ is its Dirac adjoint; in a term of the fold, $\Psi$ is its value at $\sigma = 0$. Unit: GeV$^{7/2}$. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\chi_o(\sigma),\ \bar\chi_o$: The profile of the occupied Kohn-Sham orbital $o$ ($o = 1, \dots, 4$, the four positive-energy states of the level at the fold) of a homogeneous gas of the particles $\chi$ at rest on the static block: a 16-component spinor function of $\sigma$; the orbital of each particle is $\mathrm{e}^{\frac72H\lvert\sigma\rvert}\chi_o(\sigma)\mathrm{e}^{-\mathrm{i}\omega x_4}$ divided by the square root of the volume of ordinary space and of $V_*$; normalised to the Krein charge $-1$ with the measure of UM-4, $\int\mathrm{d}\sigma\,\mathrm{e}^{H\lvert\sigma\rvert}\chi_o^\dagger\mathfrak{B}\chi_o = -1$; $\bar\chi_o = \chi_o^\dagger\sigma_{16}$ is its Dirac adjoint. Unit: GeV$^{1/2}$. Status: DERIVED.
- $o$: The label of a single-particle state of dirac16complex: a Kohn-Sham orbital, or a mode of the quantised field; a sum over $o$ runs over the orbitals or the modes. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic), as an index and as a number (UM-4 keeps only $p = 1$); in the Kohn-Sham equations also a second label of a Kohn-Sham orbital, with the Kronecker delta of the two labels. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\gamma^M,\ \gamma^{(a)}$: The Dirac matrices of dirac16complex along the coordinates, $\gamma^M = \mathbf{e}_a{}^MT^a$, $\gamma_M = g_{MN}\gamma^N$; $\gamma^{(a)} = T^a$ along the frame direction $(a)$ ($\gamma^{(0)}$ along $\sigma$, $\gamma^{(4)}$ along the time). Unit: dimensionless. Status: AUTHOR.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $\mathcal{M}(\sigma)$: The mean field of the self-interaction in the Kohn-Sham equation of the gas: the $16 \times 16$ matrix $\lambda_\Psi(n_{\mathrm{s}}\mathbf{1} - \mathcal{N})$ at each $\sigma$, which adds to the mass $m_\Psi$; positive (repulsive) for $\lambda_\Psi > 0$. Unit: GeV. Status: DERIVED.
- $G_{\mathrm{KS}}$: The dimensionless strength of the self-interaction of the gas of particles $\chi$ in the Kohn-Sham states: the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold divided by the volume $V_*$ of the extra times, $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ (in units of $m_\Psi$ when numbers are given). Unit: dimensionless. Value: $10^{-6}$ to 0.5 in the solutions. Status: DERIVED.
- $\hat\rho(\sigma)$: The scalar density of the occupied orbitals, $\hat\rho = \frac14\sum_o\bar\chi_o\chi_o$ (per particle); the scalar density of the gas is $n_{\mathrm{s}} = (n_\chi/V_*)\,\mathrm{e}^{7H\lvert\sigma\rvert}\hat\rho$. Unit: GeV. Status: DERIVED.
- $\mathbf{1},\ \mathbf{1}_4,\ \mathbf{1}_8,\ \mathbf{1}_{16}$: The identity matrix of the size fixed by the context ($16 \times 16$ on dirac16complex, $4 \times 4$ on a four-dimensional spinor, $3 \times 3$ in generation or flavour space); $\mathbf{1}_4$, $\mathbf{1}_8$ and $\mathbf{1}_{16}$ are the identity matrices of 4, 8 and 16 rows. Unit: dimensionless. Status: STANDARD.
- $\hat{\mathcal{N}}(\sigma)$: The one-body density matrix of the occupied orbitals, $\hat{\mathcal{N}} = \frac14\sum_o\chi_o\bar\chi_o$ (a $16 \times 16$ matrix at each $\sigma$, per particle); the density matrix of the gas is $\mathcal{N} = (n_\chi/V_*)\,\mathrm{e}^{7H\lvert\sigma\rvert}\hat{\mathcal{N}}$. Unit: GeV. Status: DERIVED.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $P_{\mathrm{L}}$: The author's left-handed chiral projector, $P_{\mathrm{L}} = (\mathbf{1} - \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $P_{\mathrm{R}}$: The author's right-handed chiral projector, $P_{\mathrm{R}} = (\mathbf{1} + \Gamma_8)/2$. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\mathfrak{B}$: The Krein operator, $\mathfrak{B} = \mathrm{i}\sigma_{16}\gamma^{(4)}$: a Hermitian involution with the signature (8, 8); $\Psi^\dagger\mathfrak{B}\Psi$ is the charge density. Unit: dimensionless. Status: DERIVED.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\lambda_\Psi$: The coupling of the contact self-interaction of dirac16complex. Unit: GeV$^{-6}$. Status: RECORD.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.

<!-- end generated symbol list -->

$$
\begin{aligned}
&\mathsf{E}_{\mathrm{int}} = \frac{G_{\mathrm{KS}}}{2}\int\mathrm{d}\sigma\,\mathrm{e}^{7H\lvert\sigma\rvert}\Big(\hat\rho^2 - \mathrm{tr}\,\hat{\mathcal{N}}^2\Big),\qquad
 \epsilon_{\mathrm{p}} = \omega - \mathsf{E}_{\mathrm{int}},\qquad P_{\mathrm{KS}} = q_\chi = n_\chi\,\mathsf{E}_{\mathrm{int}},\\
&\Delta\omega = G_{\mathrm{KS}}\int\mathrm{d}\sigma\,\mathrm{e}^{7H\lvert\sigma\rvert}\Big(\hat\rho^2 - \mathrm{tr}\,\hat{\mathcal{N}}^2\Big)\Big\vert_{G_{\mathrm{KS}} = 0}
\end{aligned} \tag{S-9}
$$
<!-- symbols: Eint, GKS, diff, sigma, euler, Hconst, rhohat, trace, Nhat, epsp, omegafreq, PKS, qchi, nchi, Delta -->
<!-- begin generated symbol list -->
**Symbols in (S-9).**

- $\mathsf{E}_{\mathrm{int}}$: The interaction energy per particle of the gas of $\chi$: the mean self-interaction energy $\frac{\lambda_\Psi}{2}(n_{\mathrm{s}}^2 - \mathrm{tr}\,\mathcal{N}^2)$ integrated across the hidden direction, per particle. Unit: GeV. Status: DERIVED.
- $G_{\mathrm{KS}}$: The dimensionless strength of the self-interaction of the gas of particles $\chi$ in the Kohn-Sham states: the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold divided by the volume $V_*$ of the extra times, $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ (in units of $m_\Psi$ when numbers are given). Unit: dimensionless. Value: $10^{-6}$ to 0.5 in the solutions. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\hat\rho(\sigma)$: The scalar density of the occupied orbitals, $\hat\rho = \frac14\sum_o\bar\chi_o\chi_o$ (per particle); the scalar density of the gas is $n_{\mathrm{s}} = (n_\chi/V_*)\,\mathrm{e}^{7H\lvert\sigma\rvert}\hat\rho$. Unit: GeV. Status: DERIVED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\hat{\mathcal{N}}(\sigma)$: The one-body density matrix of the occupied orbitals, $\hat{\mathcal{N}} = \frac14\sum_o\chi_o\bar\chi_o$ (a $16 \times 16$ matrix at each $\sigma$, per particle); the density matrix of the gas is $\mathcal{N} = (n_\chi/V_*)\,\mathrm{e}^{7H\lvert\sigma\rvert}\hat{\mathcal{N}}$. Unit: GeV. Status: DERIVED.
- $\epsilon_{\mathrm{p}}$: The energy per particle of the gas of $\chi$: the orbital energy minus the interaction energy per particle, which the orbital energy counts twice. Unit: GeV. Status: DERIVED.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $P_{\mathrm{KS}}$: The pressure of the gas of $\chi$ along ordinary space in the Kohn-Sham state: the particles are at rest, so it is the mean self-interaction, $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$. Unit: GeV$^4$. Status: DERIVED.
- $q_\chi$: The pressure of the particles $\chi$ of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $n_\chi$: The number density of the dark-matter particles $\chi$ (particles plus antiparticles). Unit: GeV$^3$. Status: DERIVED.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.

<!-- end generated symbol list -->

The Kohn-Sham equations of a homogeneous gas of the particles $\chi$ at rest on the fold (S-7) and its energy and pressure (S-9). Each particle
occupies one of the four positive-energy states of the level at the fold. The profiles $\chi_o$ obey the Dirac equation along the hidden direction
with the warped frequency $\omega\mathrm{e}^{H\lvert\sigma\rvert}$ and the mean field $\mathcal{M}$ of the self-interaction added to the mass, where
$\hat\rho$ and $\hat{\mathcal{N}}$ are the scalar density and the density matrix of the profiles and $\mathrm{e}^{7H\lvert\sigma\rvert}$ turns them into
proper densities; the Standard Model acts through the matching at the fold, and $G_{\mathrm{KS}} = \lambda_\Psi n_\chi/V_*$ is the dimensionless
strength of the self-interaction (the self-coupling $\lambda_\Psi$ times the number density $n_\chi$ of the particles on the fold, divided by the
volume $V_*$ of the extra times). $\mathsf{E}_{\mathrm{int}}$ is the interaction energy per particle, $\epsilon_{\mathrm{p}}$ the energy per particle (the
orbital energy counts the interaction twice) and $P_{\mathrm{KS}}$ the pressure: the particles are at rest and do not depend on the extra times,
so only the self-interaction contributes, along ordinary space and along the extra times alike. Status: DERIVED (from the field equation of
dirac16complex with its self-interaction), RECORD (the Kohn-Sham treatment).

The Kohn-Sham equations were solved (in units of $m_\Psi$) deep in the regime of long-lived particles, $H = 10^{-4}$ ($m_\Psi/H = 10^4$), with the
Higgs portal of the vacuum ($\mu_{\mathrm{L}} = -0.6$, $\mu_{\mathrm{R}} = 0$, so $q_{\mathrm{b}} = 0.3 = 3000H$), for $G_{\mathrm{KS}}$ from $10^{-6}$ to 0.5. The
self-interaction is repulsive for $\lambda_\Psi > 0$, the level rises, and the pressure is positive: the equation of state
$w_\chi = P_{\mathrm{KS}}/(n_\chi\epsilon_{\mathrm{p}})$ is $5.36\times10^{-8}$, $5.36\times10^{-6}$, $5.32\times10^{-4}$ and $5.00\times10^{-3}$ at
$G_{\mathrm{KS}} = 10^{-6}$, $10^{-4}$, $10^{-2}$ and $10^{-1}$; in the dilute limit the shift of the level is linear in $G_{\mathrm{KS}}$ (the exponent
1.0000) and equals first-order perturbation theory; within the box of the computation the proper density decays away from the fold, so the gas
stays at the fold. The four occupied orbitals are taken in one multiplet (the symmetric occupation, a stationary point of the first-order energy
that is a saddle, not a minimum; ASSUMED, see the Krein norm below). The repulsion also raises the level towards $m_\Psi$ and lowers the barrier
through which the particles tunnel into the bulk: at $m_\Psi/H = 10^4$ with $H$ at its bound the gas lives longer than 160 Gyr only for
$G_{\mathrm{KS}} < 0.139$. At a weakly bound point ($q_{\mathrm{b}} = 0.03\,m_\Psi$, $H = 10^{-7}m_\Psi$) the self-consistent
shift approaches first-order perturbation theory as $G_{\mathrm{KS}} \to 0$, and $w_\chi = 5.6\times10^{-7}$, $5.6\times10^{-6}$ and $5.1\times10^{-5}$ at
$G_{\mathrm{KS}} = 10^{-4}$, $10^{-3}$ and $10^{-2}$. Status: DERIVED (`um4_kohnsham.py`, K2 to K5, K7 to K9), ASSUMED (the symmetric occupation).

How dilute is the gas of the universe? With the self-coupling of the natural size $\lambda_\Psi = m_\Psi^{-6}$ and extra times of the size $1/m_\Psi$
($V_* = m_\Psi^{-3}$), $G_{\mathrm{KS}} = n_\chi/m_\Psi^3$. For the lightest particles that live longer than 160 Gyr (S-6 with $H = 2534$ GeV) and the
density of dark matter near the Sun (0.4 GeV/cm$^3$) this is $G_{\mathrm{KS}} = 5.2\times10^{-68}$ for $q_{\mathrm{b}} = m_\Psi/2$ ($\omega_{\mathrm{b}} = 2.49\times10^6$ GeV,
$m_\Psi = 2.88\times10^6$ GeV) and $4.4\times10^{-61}$ for the strong binding $q_{\mathrm{b}} = 0.99\,m_\Psi$ ($\omega_{\mathrm{b}} = 1.18\times10^4$ GeV,
$m_\Psi = 8.39\times10^4$ GeV), and $1.6\times10^{-73}$ and $1.4\times10^{-66}$ for the mean density of the universe today; extra times of the Planck size
($V_* = M_{\mathrm{Pl}}^{-3}$) give at most $1.4\times10^{-18}$. The cosmic gas of $\chi$ is therefore deep in the dilute limit, where
$w_\chi = 0.0536\,G_{\mathrm{KS}}$ (at most $2.4\times10^{-62}$ near the Sun for the natural sizes), and far below the coupling at which the
self-interaction would shorten its life: it is cold dark matter. Status: ESTIMATE (`um4_kohnsham.py`, K10).

## The relic density, direct detection and the window

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
- $\sigma_{\mathrm{ann}}$: The annihilation cross-section of the particles $\chi$ into Standard-Model particles (through the portals) in the normalisation of the relic abundance, where $n_\chi$ counts the four particle and the four antiparticle states of the level at the fold: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is a quarter of the annihilation rate $(\sigma\mathsf{v})_{\chi\bar\chi}$ of one particle $\chi_a$ with one antiparticle $\bar\chi_a$. Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathsf{v}$: The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product. Unit: dimensionless. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $n_{\chi,\mathrm{eq}}$: The number density of $\chi$ in thermal equilibrium with the plasma (non-relativistic). Unit: GeV$^3$. Status: STANDARD.
- $g_\chi$: The number of internal states of the level of $\chi$ at the fold that are in thermal equilibrium. Unit: dimensionless. Value: 8 (four particles and four antiparticles). Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\mathsf{T}$: The temperature of the Standard-Model plasma (of the photons after the annihilation of electrons and positrons). Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\Omega_\chi$: The density parameter of the dark matter today. Unit: dimensionless. Value: $\Omega_\chi h_{100}^2 = 0.120$ (Planck 2018). Status: DERIVED.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.
- $x_{\mathrm{f}}$: The ratio of the mass of $\chi$ to the temperature at which its annihilations stop (freeze-out). Unit: dimensionless. Value: 23 to 30 (for $\omega_{\mathrm{b}}$ = 10 GeV to 10 TeV). Status: STANDARD.
- $g_*$: The effective number of relativistic degrees of freedom at the freeze-out ($g_\rho$ there). Unit: dimensionless. Status: STANDARD.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.221\times10^{19}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\sigma_{\mathrm{pair}}\mathsf{v} \le \frac{4\pi}{\omega_{\mathrm{b}}^2\,\mathsf{v}},\qquad \Big\langle\frac{1}{\mathsf{v}}\Big\rangle = \sqrt{\frac{\mathsf{x}}{\pi}}:\qquad
\Omega_\chi h_{100}^2 = 0.120\ \ \text{at}\ \ \omega_{\mathrm{b}} = 9.69\times10^4\ \text{GeV} \tag{S-20}
$$
<!-- symbols: sigmapair, vrel, omegab, pi, mean, xmass, Omegachi, h100 -->
<!-- begin generated symbol list -->
**Symbols in (S-20).**

- $\sigma_{\mathrm{pair}}$: The cross-section of the annihilation of one particle $\chi_a$ with one antiparticle $\bar\chi_a$ of the same species, summed over the final states; $\sigma_{\mathrm{pair}}\mathsf{v}$ its product with the relative velocity (a constant for s-wave annihilation). Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathsf{v}$: The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product. Unit: dimensionless. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathsf{x}$: The ratio of the mass of $\chi$ to the temperature, $\mathsf{x} = \omega_{\mathrm{b}}/\mathsf{T}$ (the time variable of the freeze-out). Unit: dimensionless. Status: STANDARD.
- $\Omega_\chi$: The density parameter of the dark matter today. Unit: dimensionless. Value: $\Omega_\chi h_{100}^2 = 0.120$ (Planck 2018). Status: DERIVED.
- $h_{100}$: The present expansion rate of the fold in units of 100 km/s/Mpc. Unit: dimensionless. Value: 0.674 (Planck 2018). Status: STANDARD.

<!-- end generated symbol list -->

The relic density of a thermal relic (FE-61, solved numerically for $g_\chi = 8$: the four particle and the four antiparticle states of the
level at the fold, integrated far beyond freeze-out) needs an s-wave annihilation $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = 2.2\times10^{-26}$ cm$^3$/s for
every mass from 10 GeV to 10 TeV, that is $(\sigma\mathsf{v})_{\chi\bar\chi} \approx 9\times10^{-26}$ cm$^3$/s for the annihilation of one $\chi_a$ with one
$\bar\chi_a$. Partial-wave unitarity bounds the s-wave annihilation of one $\chi$ with one $\bar\chi$ (S-20, with the thermal average of $1/\mathsf{v}$
over the Maxwell-Boltzmann distribution): with the largest annihilation that unitarity allows, the relic density equals the measured one at
$\omega_{\mathrm{b}} = 9.69\times10^4$ GeV (converged in the end point of the integration; $6.9\times10^4$ to $1.37\times10^5$ GeV with the bookkeeping of the
channels of the multiplet), and heavier particles would be overproduced by freeze-out (the classic bound of K. Griest and M. Kamionkowski, Phys.
Rev. Lett. 64 (1990) 615). The lifetime of S-6 puts the particles $\chi$ above this mass unless they are strongly bound: only for
$q_{\mathrm{b}} > 0.906\,m_\Psi$ (0.875 to 0.929) does the bound on $\omega_{\mathrm{b}}$ fall below it. Only so strongly bound particles, of masses of
$10^4$ to $10^5$ GeV, could be a thermal relic; with a weaker binding their abundance needs a non-thermal origin. Status: DERIVED (`um4_thermal.py`,
T2 and T7), OPEN (the origin of the abundance).

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

- $\mathfrak{g}_{\Phi},\ \mathfrak{g}_{G},\ \mathfrak{g}_{f},\ \mathfrak{g}_{h\chi}$: The four-dimensional couplings of the particles $\chi$ of dirac16complex to the Standard Model: to $\Phi^\dagger\Phi$, to the gluon kinetic density, to the number densities of the fermions of kind $f$, and the Yukawa coupling of the Higgs boson to $\chi$. Unit: $\mathfrak{g}_{\Phi}$: GeV$^{-1}$; $\mathfrak{g}_{G}$: GeV$^{-3}$; $\mathfrak{g}_{f}$: GeV$^{-2}$; $\mathfrak{g}_{h\chi}$: dimensionless. Status: DERIVED.
- $\partial$: A partial derivative: the derivative with respect to one variable at fixed values of the others ($\partial_\sigma$ with respect to $\sigma$; $\partial_M$ and $\partial_\mu$ with respect to the coordinate that carries the same index, of the eight dimensions or of the fold). Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\mu_X,\ \mu_{\mathrm{L}},\ \mu_{\mathrm{R}}$: The dimensionless strengths of the fold for the left-handed and right-handed halves of dirac16complex, set by the mean fields of the Standard Model at the fold: the jump of the profile across the fold is the exponential of $\gamma^{(0)}(\mu_{\mathrm{L}}P_{\mathrm{L}} + \mu_{\mathrm{R}}P_{\mathrm{R}})$; negative values attract. Unit: dimensionless. Status: DERIVED.
- $c_\Phi$: The Higgs-portal coupling of the left-handed half of dirac16complex (the right-handed half has none). Unit: GeV$^{-5}$. Status: INVENTED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $c^{G}_X$: The gluon-kinetic portal coupling of the half $X$ of dirac16complex. Unit: GeV$^{-7}$. Status: INVENTED.
- $X$: The label of a half of dirac16complex: $X \in \{\mathrm{L}, \mathrm{R}\}$ (left-handed or right-handed half); a sum over $X$ runs over both. Status: STANDARD.
- $c^{f}_X$: The current-portal coupling of the half $X$ of dirac16complex with the fermion-number current of the multiplets of kind $f$ (flavour blind); $c^{\ell}_X$ and $c^{\nu}_X$ are those of the lepton doublets and of the right-handed neutrinos. Unit: GeV$^{-7}$. Status: INVENTED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\Phi$: The Higgs doublet (two complex components, hypercharge $1/2$), a field of the fold. Unit: GeV. Status: AUTHOR.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor; for an operator on the space of states, its adjoint with respect to the scalar product of that space (for the quantised dirac16complex the indefinite Krein scalar product). Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.
- $n_f$: The number density of the Standard-Model fermions of kind $f$ (particles minus antiparticles, summed over generations and gauge components), the time component of the mean current $\langle J_f^\mu\rangle$ in the rest frame of the medium. Unit: GeV$^3$. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\begin{aligned}
&\sigma_{\mathrm{pair}}\mathsf{v} = \sum_f\frac{\mathfrak{g}_f^2\,\omega_{\mathrm{b}}^2\,\mathsf{v}^4}{96\pi},\qquad \langle\mathsf{v}^4\rangle = \frac{60}{\mathsf{x}^2},\qquad
 \langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle = \frac{\langle\sigma_{\mathrm{pair}}\mathsf{v}\rangle}{4},\qquad
 \sigma_{\mathrm{SI}} = \frac{\mu_{\mathrm{red}}^2\,f_{\mathrm{N}}^2}{\pi},\qquad f_{\mathrm{N}} = 3\,\mathfrak{g}_{\mathrm{q}}\ \ (\text{quark portals}),\\
&f_{\mathrm{N}} = \mathfrak{g}_{\mathrm{p}} = \frac{\alpha_{\mathrm{em}}}{3\pi}\,\mathfrak{g}_{\mathrm{l}}\sum_{l}\ln\frac{\omega_{\mathrm{b}}^2}{\max\big(m_l^2,\ q_{\mathrm{t}}^2\big)}\ \ (\text{lepton portals}),\qquad
 f_{\mathrm{N}} = \frac{\mathfrak{g}_{h\chi}\,f_{\mathrm{H}}\,m_{\mathrm{N}}}{v\,m_h^2}\ \ (\text{Higgs portal})
\end{aligned} \tag{S-21}
$$
<!-- symbols: sigmapair, vrel, gport, if, omegab, pi, mean, xmass, sigmaann, sigmaSI, mured, fN, gportql, alphaem, il, mmass, qtransfer, mN, vev, mh, fH -->
<!-- begin generated symbol list -->
**Symbols in (S-21).**

- $\sigma_{\mathrm{pair}}$: The cross-section of the annihilation of one particle $\chi_a$ with one antiparticle $\bar\chi_a$ of the same species, summed over the final states; $\sigma_{\mathrm{pair}}\mathsf{v}$ its product with the relative velocity (a constant for s-wave annihilation). Unit: GeV$^{-2}$. Status: DERIVED.
- $\mathsf{v}$: The relative velocity of two annihilating particles; $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is the thermal average of the product. Unit: dimensionless. Status: STANDARD.
- $\mathfrak{g}_{\Phi},\ \mathfrak{g}_{G},\ \mathfrak{g}_{f},\ \mathfrak{g}_{h\chi}$: The four-dimensional couplings of the particles $\chi$ of dirac16complex to the Standard Model: to $\Phi^\dagger\Phi$, to the gluon kinetic density, to the number densities of the fermions of kind $f$, and the Yukawa coupling of the Higgs boson to $\chi$. Unit: $\mathfrak{g}_{\Phi}$: GeV$^{-1}$; $\mathfrak{g}_{G}$: GeV$^{-3}$; $\mathfrak{g}_{f}$: GeV$^{-2}$; $\mathfrak{g}_{h\chi}$: dimensionless. Status: DERIVED.
- $f$: The label of a kind of Standard-Model multiplet: $f \in \{Q, u, d, \ell, e, \nu\}$ (quark doublets, up-quark singlets, down-quark singlets, lepton doublets, charged-lepton singlets, right-handed neutrinos); a sum over $f$ runs over the six. Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathsf{x}$: The ratio of the mass of $\chi$ to the temperature, $\mathsf{x} = \omega_{\mathrm{b}}/\mathsf{T}$ (the time variable of the freeze-out). Unit: dimensionless. Status: STANDARD.
- $\sigma_{\mathrm{ann}}$: The annihilation cross-section of the particles $\chi$ into Standard-Model particles (through the portals) in the normalisation of the relic abundance, where $n_\chi$ counts the four particle and the four antiparticle states of the level at the fold: $\langle\sigma_{\mathrm{ann}}\mathsf{v}\rangle$ is a quarter of the annihilation rate $(\sigma\mathsf{v})_{\chi\bar\chi}$ of one particle $\chi_a$ with one antiparticle $\bar\chi_a$. Unit: GeV$^{-2}$. Status: DERIVED.
- $\sigma_{\mathrm{SI}}$: The spin-independent cross-section of the scattering of $\chi$ on a nucleon (normalised per nucleon, as the direct-detection limits are quoted). Unit: GeV$^{-2}$ (cm$^2$). Status: ESTIMATE.
- $\mu_{\mathrm{red}}$: The reduced mass of $\chi$ and a nucleon, $\omega_{\mathrm{b}}m_{\mathrm{N}}/(\omega_{\mathrm{b}} + m_{\mathrm{N}})$. Unit: GeV. Status: STANDARD.
- $f_{\mathrm{N}}$: The effective coupling of $\chi$ to a nucleon in the coherent scattering (a vector or scalar contact interaction). Unit: GeV$^{-2}$. Status: ESTIMATE.
- $\mathfrak{g}_{\mathrm{q}},\ \mathfrak{g}_{\mathrm{l}},\ \mathfrak{g}_{\mathrm{p}}$: The current-portal couplings $\mathfrak{g}_f$ taken equal for all chiral quark states ($\mathfrak{g}_{\mathrm{q}}$) or for the nine chiral lepton states that take part, the six of the lepton doublets and the three right-handed charged leptons ($\mathfrak{g}_{\mathrm{l}}$), and the coupling to the proton that the lepton loop induces ($\mathfrak{g}_{\mathrm{p}}$). Unit: GeV$^{-2}$. Status: ESTIMATE.
- $\alpha_{\mathrm{em}}$: The fine-structure constant. Unit: dimensionless. Value: 1/137.036. Status: STANDARD.
- $l$: The multipole index and number ($l = 0, 1, 2, \dots$) of an expansion in Legendre polynomials of the direction of a photon or a neutrino relative to the wave vector, or of the CMB sky in spherical harmonics. Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $q_{\mathrm{t}}$: The momentum transfer of the scattering of $\chi$ on a xenon nucleus in a detector. Unit: GeV. Value: 0.05 GeV. Status: STANDARD.
- $m_{\mathrm{N}}$: The mass of a nucleon. Unit: GeV. Value: 0.939 GeV. Status: STANDARD.
- $v$: The vacuum expectation value of the lower component of the Higgs doublet, $v^2 = -\mu^2/\lambda$. Unit: GeV. Value: 246.22 GeV $= (\sqrt2\,G_{\mathrm{F}})^{-1/2}$ with the Fermi constant $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$ of the muon lifetime (Particle Data Group). Status: STANDARD.
- $m_h$: The mass of the Higgs boson. Unit: GeV. Value: 125.25 GeV (Particle Data Group 2022). Status: STANDARD.
- $f_{\mathrm{H}}$: The nucleon matrix element of the Higgs coupling: the fraction of the nucleon mass carried by the quark masses and, through the trace anomaly, by the gluons. Unit: dimensionless. Value: 0.30. Status: STANDARD.

<!-- end generated symbol list -->

The couplings of the particles $\chi$ to the Standard Model (FE-47) and their annihilation and scattering on nucleons (S-21). The Higgs-portal
Yukawa coupling is fixed by the binding: with the Higgs portal alone ($\mu_{\mathrm{R}} = 0$, so $q_{\mathrm{b}} = -m_\Psi\mu_{\mathrm{L}}/2$ by FE-40),
$\lvert\mathfrak{g}_{h\chi}\rvert = 2q_{\mathrm{b}}^2/(\omega_{\mathrm{b}}v)$. The current portals are free (through the INVENTED couplings $c^{f}_X$), but their
convective current creates a pair $\chi\bar\chi$ only with an amplitude of the second order in the momentum (`um4_krein.py`, KR9), so they annihilate
the particles only with the fourth power of the relative velocity (the first relation of S-21). Against the limit of the LUX-ZEPLIN experiment
(4.2 tonne-years of xenon, Phys. Rev. Lett. 135 (2025) 011802: $2.2\times10^{-48}$ cm$^2$ at its minimum, 40 GeV, at 90 per cent confidence, scaled in
proportion to the mass above it), quark portals strong enough to set a relic density are excluded from 100 GeV to $10^5$ GeV (by factors from
$4\times10^{10}$ to 60), lepton portals give a loop-suppressed scattering that is allowed only above about $2.3\times10^4$ GeV, where the contact
coupling that the relic needs is no longer perturbative ($\mathfrak{g}_{\mathrm{l}}\omega_{\mathrm{b}}^2 \approx 80$, above $4\pi$ from about $4\times10^3$ GeV on), and
the Higgs portal requires a weak binding, $q_{\mathrm{b}} \lesssim 0.06\,\omega_{\mathrm{b}}$ at 100 GeV to $0.02\,\omega_{\mathrm{b}}$ at 10 TeV. Status: STANDARD (the
formulas), DERIVED (the velocity dependence), ESTIMATE (`um4_thermal.py`, T3 and T4).

$$
\frac{q_{\mathrm{b}}}{\omega_{\mathrm{b}}}\Big\vert_{\max} \propto \omega_{\mathrm{b}}^{-1/4},\qquad
H < H_{\max} = \frac{2F(\upsilon_{\mathrm{b}})\,m_\Psi}{\ln\big(11.6\,p_{\mathrm{w}}\,m_\Psi\,t_0\big)} \tag{S-22}
$$
<!-- symbols: qb, omegab, Hconst, Hmaxb, Fwkb, upsilonr, mPsi, pw, tzero -->
<!-- begin generated symbol list -->
**Symbols in (S-22).**

- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $H_{\max}$: The largest value of the author's constant $H$ for which particles $\chi$ bound to the fold by the Higgs portal, with the strongest binding that direct detection allows, live longer than 160 Gyr ($11.6\,t_0$, the bound for dark matter that decays into invisible particles). Unit: GeV. Value: from $4.9\times10^{-4}$ GeV at $\omega_{\mathrm{b}} = 10^4$ GeV to 2.5 GeV at the Planck mass. Status: ESTIMATE.
- $F(\upsilon)$: The tunnelling exponent of the width of the particles $\chi$ per unit of $m_\Psi/H$: the integral of the local decay rate $q$ over the region inside the turning point, divided by $m_\Psi/H$, as a function of the ratio $\upsilon$ of the energy to the bulk mass. Unit: dimensionless. Value: 0.049 for $\upsilon = 0.866$; $(q_{\mathrm{b}}/\omega_{\mathrm{b}})^3/3$ for weak binding. Status: DERIVED.
- $\upsilon,\ \upsilon_{\mathrm{b}},\ \upsilon_{\mathrm{r}}$: The argument of the tunnelling exponent $F$, a ratio of an energy to the bulk mass $m_\Psi$; $\upsilon_{\mathrm{b}} = \omega_{\mathrm{b}}/m_\Psi$ that of the particle $\chi$ in the limit $H/q_{\mathrm{b}} \to 0$, $\upsilon_{\mathrm{r}} = \omega_{\mathrm{r}}/m_\Psi$ that of the real part of its resonance. Unit: dimensionless. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $p_{\mathrm{w}}$: The prefactor of the width of the particles $\chi$, $\Gamma_\chi = p_{\mathrm{w}}m_\Psi\mathrm{e}^{-2F(\upsilon_{\mathrm{b}})m_\Psi/H}$: $p_{\mathrm{w}} \simeq (2/\mathrm{e})(q_{\mathrm{b}}/m_\Psi)^2$ to the leading order in $H/q_{\mathrm{b}}$ (FE-86; 0.184 for $q_{\mathrm{b}} = m_\Psi/2$). Unit: dimensionless. Status: DERIVED.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.

<!-- end generated symbol list -->

The particles $\chi$ bound by the Higgs portal cannot be the dark matter of UM-4. With the binding of the author's specification (the Higgs portal of
the left-handed half) the largest $q_{\mathrm{b}}/\omega_{\mathrm{b}}$ that the LUX-ZEPLIN limit allows falls like $\omega_{\mathrm{b}}^{-1/4}$ (the coupling
$\mathfrak{g}_{h\chi}$ grows like $q_{\mathrm{b}}^2/\omega_{\mathrm{b}}$, the limit on the cross-section like $\omega_{\mathrm{b}}$), and with that binding the lifetime
condition S-6 holds only for $H$ below $H_{\max}$: $1.5\times10^{-3}$ GeV at $\omega_{\mathrm{b}} = 10^6$ GeV (where $q_{\mathrm{b}}/\omega_{\mathrm{b}}$ may be at most
0.0062), 0.14 GeV at $10^{14}$ GeV and 2.5 GeV at the Planck mass ($1.2\times10^{19}$ GeV). $H_{\max}$ grows only like $\omega_{\mathrm{b}}^{1/4}$ and stays
far below the bound $H > 2534$ GeV at every mass (above about $10^{10}$ GeV the Yukawa coupling exceeds $4\pi$ and the estimate is only formal).
Status: ESTIMATE (`um4_thermal.py`, T8: the limit extrapolated in proportion to the mass).

$$
\Delta\omega_{\mathrm{b}} = \mathfrak{g}_{G}\,\Delta\langle G^2\rangle,\qquad
\mathfrak{g}_{G} = -\frac{q_{\mathrm{b}}^2}{\omega_{\mathrm{b}}\,\langle G^2\rangle},\qquad
f_{\mathrm{N}} = \frac{8\,m_{\mathrm{N}}\,f_{\mathrm{TG}}}{9\,\langle(\alpha_3/\pi)G^2\rangle}\,\frac{q_{\mathrm{b}}^2}{\omega_{\mathrm{b}}} \tag{S-29}
$$
<!-- symbols: Delta, omegab, gport, Gsq, qb, fN, mN, fTG, alpha3, pi, Ggluon -->
<!-- begin generated symbol list -->
**Symbols in (S-29).**

- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $\mathfrak{g}_{\Phi},\ \mathfrak{g}_{G},\ \mathfrak{g}_{f},\ \mathfrak{g}_{h\chi}$: The four-dimensional couplings of the particles $\chi$ of dirac16complex to the Standard Model: to $\Phi^\dagger\Phi$, to the gluon kinetic density, to the number densities of the fermions of kind $f$, and the Yukawa coupling of the Higgs boson to $\chi$. Unit: $\mathfrak{g}_{\Phi}$: GeV$^{-1}$; $\mathfrak{g}_{G}$: GeV$^{-3}$; $\mathfrak{g}_{f}$: GeV$^{-2}$; $\mathfrak{g}_{h\chi}$: dimensionless. Status: DERIVED.
- $\langle G^2\rangle$: The mean square of the gluon field strength, $\langle G^A_{\mu\nu}G^{A\mu\nu}\rangle$ (the gluon condensate in the QCD vacuum, a thermal value in the plasma). Unit: GeV$^4$. Status: STANDARD.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $f_{\mathrm{N}}$: The effective coupling of $\chi$ to a nucleon in the coherent scattering (a vector or scalar contact interaction). Unit: GeV$^{-2}$. Status: ESTIMATE.
- $m_{\mathrm{N}}$: The mass of a nucleon. Unit: GeV. Value: 0.939 GeV. Status: STANDARD.
- $f_{\mathrm{TG}}$: The fraction of the nucleon mass carried by the gluons through the trace anomaly (one minus the fractions carried by the masses of the u, d and s quarks): the matrix element of $(\alpha_3/\pi)G^2$ in a nucleon at rest is $-\frac89m_{\mathrm{N}}f_{\mathrm{TG}}$. Unit: dimensionless. Value: 0.92. Status: STANDARD.
- $\alpha_3$: The strong coupling constant, $\alpha_3 = g_3^2/(4\pi)$; $\langle(\alpha_3/\pi)G^2\rangle$ is the gluon condensate of the vacuum, 0.012 GeV$^4$ (Shifman, Vainshtein and Zakharov). Unit: dimensionless. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G^A_M,\ G^A_\mu,\ G^A_{MN}$: The gluon field of $SU(3)_C$ ($A = 1, \dots, 8$): in the bulk $G^A_M$, a field of eight dimensions in its geometric normalisation (the covariant derivative $\partial - \mathrm{i}G$), and on the fold the canonically normalised four-dimensional field $G^A_\mu(x)$ of its massless mode, $g_3G^A_\mu(x) = G^A_\mu(\sigma = 0, x)$; $G^A_{MN}$ and $G^A_{\mu\nu}$ their field strengths. Unit: GeV (field), GeV$^2$ (field strength). Status: AUTHOR.

<!-- end generated symbol list -->

No portal of the author's action can bind the particles without coupling them to nucleons. A binding by the gauge-kinetic portal of the gluons
acts through the gluon condensate of the vacuum, $\langle(\alpha_3/\pi)G^2\rangle = 0.012$ GeV$^4$, and by the theorem of Feynman and Hellmann the
same coupling makes $\chi$ scatter on nucleons, because the matrix element of $(\alpha_3/\pi)G^2$ in a nucleon at rest is
$-\frac89m_{\mathrm{N}}f_{\mathrm{TG}}$ (the trace anomaly; $f_{\mathrm{TG}} = 0.92$): with the coupling of S-29 the cross-section at the lifetime bound of S-6 is
$9\times10^{-14}$ to $8\times10^{-12}$ cm$^2$ for every binding, 29 to 33 orders of magnitude above the limit of LZ (the Higgs portal with the same
binding is excluded by 7 to 11 orders of magnitude). The other mean values through which the portals act vanish in the vacuum
($\langle W^2\rangle$, $\langle B^2\rangle$, the number densities of the current portals, the field strength of the dipole portal). Status: ESTIMATE
(`um4_thermal.py`, T9), OPEN (the binding).

$$
\begin{aligned}
&\omega_{\mathrm{b}} > 9.69\times10^4\ \text{GeV}\ \ \big(q_{\mathrm{b}} < 0.906\,m_\Psi\big),\qquad
H_{\max} \le 2.5\ \text{GeV} < 2534\ \text{GeV} \le H,\\
&\sigma_{\mathrm{SI}} \ge 9\times10^{-14}\ \text{cm}^2\ \ \big(\text{a binding by the gluon condensate}\big)
\end{aligned} \tag{A-6}
$$
<!-- symbols: omegab, qb, mPsi, Hmaxb, Hconst, sigmaSI -->
<!-- begin generated symbol list -->
**Symbols in (A-6).**

- $\omega_{\mathrm{b}}$: The energy at zero momentum of the state of dirac16complex at the fold in the limit $H \to 0$ (the bound state of UM-3): the particle $\chi$ of UM-4 has the mass $\omega_{\mathrm{r}} = \omega_{\mathrm{b}}(1 - H/(2q_{\mathrm{b}})) + \dots$, equal to $\omega_{\mathrm{b}}$ up to the relative correction $H/(2q_{\mathrm{b}})$. Unit: GeV. Status: DERIVED.
- $q_{\mathrm{b}}$: The inverse width of a state of dirac16complex at the fold: inside the turning point its profile falls as $\mathrm{e}^{-q_{\mathrm{b}}\lvert\sigma\rvert}$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $H_{\max}$: The largest value of the author's constant $H$ for which particles $\chi$ bound to the fold by the Higgs portal, with the strongest binding that direct detection allows, live longer than 160 Gyr ($11.6\,t_0$, the bound for dark matter that decays into invisible particles). Unit: GeV. Value: from $4.9\times10^{-4}$ GeV at $\omega_{\mathrm{b}} = 10^4$ GeV to 2.5 GeV at the Planck mass. Status: ESTIMATE.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma_{\mathrm{SI}}$: The spin-independent cross-section of the scattering of $\chi$ on a nucleon (normalised per nucleon, as the direct-detection limits are quoted). Unit: GeV$^{-2}$ (cm$^2$). Status: ESTIMATE.

<!-- end generated symbol list -->

What is left of the window. The first chain: the particles $\chi$ that live longer than 160 Gyr (S-6 with the lower bound of $H$) are heavier than
the heaviest thermal relic that unitarity allows (S-20) unless they are bound more strongly than $q_{\mathrm{b}} = 0.906\,m_\Psi$. The second: the
largest $H$ for which particles bound by the Higgs portal both live long enough and escape direct detection (S-22, at any mass up to the Planck
mass) lies below the lower bound of $H$ from the width of the Z boson. The third: a binding by the gluon condensate makes them scatter on nucleons
far above the limits (S-29), and the other portals of the author's action supply no binding in the vacuum. dirac16complex can therefore be the dark
matter of UM-4 only if conditions hold that the action of UM-4 does not supply:

* a binding of $\chi$ to the fold that does not couple it to nucleons (a strength $\mu_X$ of the fold that no field of the Standard Model
  supplies), strong enough for a lifetime of 160 Gyr at the value of $m_\Psi/H$ (S-6);
* either a binding stronger than $q_{\mathrm{b}} \approx 0.9\,m_\Psi$ together with an annihilation that sets the relic density (the current portals
  cannot do it with a perturbative coupling, S-21), or a non-thermal origin of the abundance $\Omega_\chi h_{100}^2 = 0.120$ (for example production
  at the end of an inflation, which UM-4 does not compute);
* right-handed neutrinos that never thermalise: their portal couplings must be much smaller than those of the lepton doublets, or they would add
  0.14 to 0.24 to the effective number of neutrino species (0.141 at the masses of UM-4).

Within these conditions the particles $\chi$ are heavier than $2.2\times10^3$ GeV (the strongest binding computed, $q_{\mathrm{b}} = 0.999\,m_\Psi$) and
than $2.5\times10^6$ GeV for $q_{\mathrm{b}} = m_\Psi/2$, live longer than 160 Gyr, gravitate as matter of the fold and form a cold gas. Status:
ESTIMATE (the window), OPEN (the binding, the origin, the couplings of the right-handed neutrinos).

## The answer

dirac16complex can be the dark matter of UM-4 only in part of what that requires: its particles cannot decay into the Standard Model alone, live
longer than 160 Gyr if $m_\Psi/H$ is large enough (S-6: 1135 for $q_{\mathrm{b}} = m_\Psi/2$, so they are then heavier than $2.5\times10^6$ GeV; less
for a stronger binding), gravitate as matter of the fold, and form a cold, pressureless gas. But they could have the measured density as a thermal
relic only if they were bound more strongly than $q_{\mathrm{b}} \approx 0.9\,m_\Psi$, and no binding that the portals of the author's action supply
(the Higgs portal of his specification, the gluon condensate) can hold them at the fold while they escape direct detection. The dark matter of UM-4
needs a binding of $\chi$ to the fold without a nucleon coupling, and, unless that binding is strong, a non-thermal origin of its abundance, both
outside the action of UM-4. Status: DERIVED (no decay into the Standard Model alone, the resonances and their width, the equation of state),
ESTIMATE (the lifetime condition, the window), OPEN (the binding, the origin of the abundance, the classical stability of the gas, which the
indefinite charge leaves undecided).

# dirac16complex and the dark energy

$$
\begin{aligned}
&H_4^2 = \frac{8\pi G_{\mathrm{N}}}{3}\big(\rho_{\mathrm{SM}} + \rho_\chi + \rho_\Lambda\big),\qquad
 2H_4' + 3H_4^2 = -8\pi G_{\mathrm{N}}\,\mathcal{P},\qquad
 \frac{1}{8\pi G_{\mathrm{N}}} = \frac{V_*}{\kappa_7} + \frac{1}{\kappa_{\mathrm{ind}}},\qquad \kappa_7 = \frac52\,\kappa H,\\
&\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}V_*,\qquad
 q_{\mathrm{SM}} + q_\chi + q_{\mathrm{P}} + q_{\mathrm{ff}} + \lambda_{\mathrm{F}}V_* + \frac{\rho - 3\mathcal{P}}{2} = 0,\\
&q_{\mathrm{SM}} = \big\langle\mathcal{L}_{\mathrm{H}} + \mathcal{L}_{\mathrm{f}} + \mathcal{L}_{\mathrm{Y}}\big\rangle,\qquad
 q_{\mathrm{P}} = \langle\mathcal{L}_{\mathrm{P}}\rangle
\end{aligned} \tag{FE-59}
$$
<!-- symbols: H4, prime, pi, GN, rhoSM, rhochi, rhoL, Ptot, Vstar, kappa7, kappaind, kappa, Hconst, rhoff, rhovac, lambdaF, qSM, qchi, qP, qff, rhotot, mean, LH, Lf, LY, LP -->
<!-- begin generated symbol list -->
**Symbols in (FE-59).**

- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.
- $\rho_{\mathrm{SM}}$: The energy density of the Standard-Model particles. Unit: GeV$^4$. Status: STANDARD.
- $\rho_\chi$: The energy density of the dark matter, the particles $\chi$ of dirac16complex; $\rho_\chi^{(0)}$ its value today. Unit: GeV$^4$. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-4: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}V_*$ (four-dimensional normalisation). Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $\mathcal{P}$: The total pressure of the matter of the fold; $\Delta\mathcal{P}$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\kappa_{\mathrm{ind}}$: The coupling of the Einstein-Hilbert term $\hat R/(2\kappa_{\mathrm{ind}})$ that the quantum fluctuations of the fields of the fold may induce, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$; it adds to the gravity of the fold, $1/(8\pi G_{\mathrm{N}}) = V_*/\kappa_7 + 1/\kappa_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Value: not fixed by UM-4; negligible for a cutoff of the order of $H$. Status: ESTIMATE.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\rho_{\mathrm{ff}}$: The energy density of the fold fluid. Unit: GeV$^4$. Value: $\lambda_{\mathrm{F}}V_* + \rho_\Lambda - \rho_{\mathrm{vac}}$: together with the vacuum energy $\rho_{\mathrm{vac}}$ of the fields of the fold it makes up the tension $\lambda_{\mathrm{F}}V_*$ that the static block requires plus the dark energy $\rho_\Lambda$. Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho_{\mathrm{vac}}$: The vacuum energy of the fields of the fold: the minimum of their potential (for the Standard Model the minimum of the Higgs potential with its loop corrections), a tension of the seven-dimensional fold. Unit: GeV$^4$. Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.
- $q_{\mathrm{SM}}$: The pressure of the Standard Model along the extra times at the fold: the mean on-shell Lagrangian density of the Standard-Model fields (the extra-time component of the energy-momentum tensor of every term of the fold is its Lagrangian, because the fields of the fold do not depend on the extra times). Unit: GeV$^4$. Status: DERIVED (for radiation and free fields), ASSUMED (for the baryons).
- $q_\chi$: The pressure of the particles $\chi$ of dirac16complex along the extra times, integrated across the fold (their on-shell Lagrangian, the self-interaction energy per volume; zero for a dilute gas). Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{P}}$: The pressure of the portals along the extra times: their mean on-shell Lagrangian density. Unit: GeV$^4$. Status: DERIVED.
- $q_{\mathrm{ff}}$: The pressure of the fold fluid along the extra times: minus its energy density (its tension) plus the pressure $q_{\mathrm{hold}}$ that holds the volume of the extra times fixed. Unit: GeV$^4$. Value: $-\rho_{\mathrm{ff}} + q_{\mathrm{hold}}$. Status: ASSUMED (the fluid), DERIVED (the value).
- $\rho$: The total energy density of the matter of the fold (all species); $\Delta\rho$ its perturbation. Unit: GeV$^4$. Status: STANDARD.
- $\langle\cdots\rangle$: The mean (expectation) value of an operator in the state of the medium (the vacuum, a plasma, the Kohn-Sham state). Status: STANDARD.
- $\mathcal{L}_{\mathrm{H}}$: The Lagrangian of the Higgs doublet on the fold. Unit: GeV$^4$. Status: AUTHOR.
- $\mathcal{L}_{\mathrm{f}}$: The kinetic Lagrangian of the quarks and leptons on the fold. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The Yukawa Lagrangian of the quarks and leptons with the Higgs doublet. Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{L}_{\mathrm{P}}$: The Lagrangian of the portals of dirac16complex at the fold. Unit: GeV$^4$. Status: INVENTED.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\mathcal{S}^a{}_b = -\big(\lambda_{\mathrm{F}} + \Delta\lambda_{\mathrm{F}}\big)\delta^a{}_b + \mathsf{t}^a{}_b:\qquad
\hat G^a{}_b = \kappa_7\big(\mathsf{t}^a{}_b - \Delta\lambda_{\mathrm{F}}\,\delta^a{}_b\big),\qquad
\rho_\Lambda = V_*\,\Delta\lambda_{\mathrm{F}},\qquad
\frac{\Delta\lambda_{\mathrm{F}}}{\lambda_{\mathrm{F}}} = \frac{\rho_\Lambda}{30H^2M_{\mathrm{red}}^2} = 2.2\times10^{-92} \tag{S-4}
$$
<!-- symbols: Sfoldsrc, ia, ib, lambdaF, Delta, delta, tfold, Ghat, kappa7, rhoL, Vstar, Hconst, Mred -->
<!-- begin generated symbol list -->
**Symbols in (S-4).**

- $\mathcal{S}^a{}_b$: The thin source of the fold: the energy-momentum tensor concentrated on the fold, integrated across it, $\kappa\mathcal{S}^a{}_b = \int_{0^-}^{0^+}\mathrm{d}\sigma\,\mathcal{E}_{(1)}{}^a{}_b$ (the junction condition of Israel); $\mathcal{S}^4{}_4$ is minus its energy density, $\mathcal{S}^1{}_1$ and $\mathcal{S}^5{}_5$ its pressures along ordinary space and along the extra times (frame components along the fold, eight-dimensional normalisation: an energy per unit volume of the six other directions of the fold). Unit: GeV$^7$. Value: $\kappa\mathcal{S}^a{}_b = -12H\delta^a{}_b$ for every $a_4$, $b_4$ of the author's form. Status: DERIVED.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{X\mathrm{L}}$ is 1 if the label $X$ of a half of dirac16complex is L and 0 otherwise); with two index strings of equal length the generalised Kronecker delta $\delta^{M_1M_2\cdots}_{N_1N_2\cdots}$, the determinant of the square matrix of the Kronecker deltas $\delta^{M_a}_{N_b}$ ($+1$ or $-1$ if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\mathsf{t}^a{}_b,\ \mathsf{t}$: The matter of the fold above its tension: the thin source minus the tension, $\mathcal{S}^a{}_b = -\lambda_{\mathrm{F}}\delta^a{}_b + \mathsf{t}^a{}_b$ (eight-dimensional normalisation); $\mathsf{t} = \mathsf{t}^c{}_c$ its trace; with frozen extra times $\mathsf{t}^a{}_b = \mathrm{diag}(P_7, P_7, P_7, -\rho_7, q_7, q_7, q_7)$. Unit: GeV$^7$. Status: DERIVED.
- $\hat G^\mu{}_\nu$: The Einstein tensor of the metric $\hat g_{ab}$ of the fold (FD-2), with frame indices along its seven directions; with four-dimensional indices, $\hat G^\mu{}_\nu$, its components along the four observable directions, which for frozen extra times are those of the Einstein tensor of the four-dimensional metric $\hat h_{\mu\nu}$. Unit: 1/length$^2$. Status: STANDARD.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-4: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}V_*$ (four-dimensional normalisation). Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $V_*$: The physical volume of the extra times $x_5, x_6, x_7$ on the fold in the late universe, $V_* = V_{\mathrm{t}}(\mathrm{e}^{-a_4}b_4)^3$ (with $V_{\mathrm{t}} = \int\mathrm{d}x_5\,\mathrm{d}x_6\,\mathrm{d}x_7$ the coordinate volume of the extra times) at a time when $\mathrm{e}^{-a_4}b_4$ is constant; it converts the eight-dimensional normalisation into the four-dimensional one. Unit: length$^3$ (GeV$^{-3}$). Status: ASSUMED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->

The Einstein equations of the fold with frozen extra times (FE-59) and the dark energy (S-4). The fold of the static block is a pure tension
$\lambda_{\mathrm{F}}$ ($\kappa\lambda_{\mathrm{F}} = 12H$, in the four-dimensional normalisation $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2$); a tension above it by
$\Delta\lambda_{\mathrm{F}}$ gives the fold a cosmological constant, the vacuum energy $\rho_\Lambda = V_*\Delta\lambda_{\mathrm{F}}$ with the equation of state
$w = -1$ (its pressure minus its energy density, exactly). The dark energy of UM-4 is this excess: the energy of the fold fluid and the vacuum
energy of the fields of the fold minus the critical tension. Status: DERIVED (`um4_foldsources.py`, FS4; with the ASSUMED fold fluid).

$$
\rho_\Lambda = \Omega_\Lambda\,\rho_{\mathrm{c}}^{(0)} = 0.685\cdot\frac{3\big(H_4^{(0)}\big)^2}{8\pi G_{\mathrm{N}}} = 2.5\times10^{-47}\ \text{GeV}^4 = \big(2.24\ \text{meV}\big)^4 \tag{A-7}
$$
<!-- symbols: rhoL, OmegaL, rhoc, H4, pi, GN -->
<!-- begin generated symbol list -->
**Symbols in (A-7).**

- $\rho_\Lambda$: The vacuum energy density of the fold above its static tension, the dark energy of UM-4: $\rho_\Lambda = \rho_{\mathrm{ff}} + \rho_{\mathrm{vac}} - \lambda_{\mathrm{F}}V_*$ (four-dimensional normalisation). Unit: GeV$^4$. Value: $0.685\,\rho_{\mathrm{c}}^{(0)} = 2.5\times10^{-47}$ GeV$^4$ (Planck 2018). Status: DERIVED.
- $\Omega_\Lambda$: The density parameter of the dark energy (the vacuum energy of the fold) today. Unit: dimensionless. Value: 0.685 (Planck 2018). Status: DERIVED.
- $\rho_{\mathrm{c}}$: The critical density, the energy density of a spatially flat fold at the expansion rate $H_4$; $\rho_{\mathrm{c}}^{(0)}$ its value today. Unit: GeV$^4$. Value: $\rho_{\mathrm{c}}^{(0)} = 1.0537\times10^{-5}\,h_{100}^2$ GeV/cm$^3$. Status: STANDARD.
- $H_4$: The expansion rate (Hubble rate) of the fold, $H_4 = a_4'$, as a function of the time or of the redshift; $H_4^{(0)}$ its value today, the Hubble constant. Unit: GeV (1/time). Value: $H_4^{(0)} = 100\,h_{100}$ km/s/Mpc with $h_{100} = 0.674$ (Planck 2018): 67.4 km/s/Mpc $= 1.44\times10^{-42}$ GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{N}}$: Newton’s constant of four-dimensional gravity (the gravity of our world, on the fold), $G_{\mathrm{N}} = 1/M_{\mathrm{Pl}}^2$ with the Planck mass $M_{\mathrm{Pl}} = 1.221\times10^{19}$ GeV. Unit: GeV$^{-2}$. Value: $6.708\times10^{-39}$ GeV$^{-2}$. Status: STANDARD.

<!-- end generated symbol list -->

The vacuum energy that the measurements require ($H_4^{(0)} = 67.36$ km/s/Mpc $= 1.44\times10^{-42}$ GeV). Status: STANDARD.

Can dirac16complex be the dark energy? A dark energy needs a pressure close to minus its energy density, an equation of state $w$ (pressure over
energy density) close to $-1$. The gas of the particles $\chi$ has the pressure $P_{\mathrm{KS}} = n_\chi\mathsf{E}_{\mathrm{int}}$ of its self-interaction
(S-9), which is positive for a repulsive self-interaction and vanishes in the dilute limit ($w_\chi = 5.4\times10^{-8}$ at $G_{\mathrm{KS}} = 10^{-6}$).
An attractive self-interaction ($G_{\mathrm{KS}} < 0$, whose states converge as well) would give by S-9 a negative pressure of the same small size,
since the integral of S-9 is positive at the symmetric occupation (0.102 per unit of $G_{\mathrm{KS}}$ in the dilute limit; on other occupations of
negative norm it takes either sign, `um4_krein.py`, KR8), and the gas of the universe has $G_{\mathrm{KS}}$ below $10^{-17}$ (K10): $w_\chi$ is far
from $-1$ in every case. The gas of $\chi$ is dark matter, not dark energy. The other contribution of dirac16complex to the vacuum energy,
the energy of its unoccupied and its negative-energy states (the sea, which the Kohn-Sham states leave out), is a renormalisation of the tension
of the fold and of the cosmological constant of the bulk that UM-4 does not compute; its sign and size are OPEN, and with the indefinite Krein
norm it is not even clear that it is bounded. The dark energy of UM-4 is therefore the excess of the tension, a free parameter: its value
$(2.24\ \text{meV})^4$ is accommodated by tuning the tension to $\Delta\lambda_{\mathrm{F}}/\lambda_{\mathrm{F}} = 2.2\times10^{-92}$ for $H = 2534$ GeV (smaller still
for a larger $H$), not explained: the cosmological-constant problem of the brane of Randall and Sundrum. With the Planck 2018 parameters UM-4
reproduces the CMB ($\chi^2 = 584$ for 613 high-multipole bins); against the BAO of DESI DR2 it has $\chi^2 = 32.0$ for 13 measurements, and DESI
alone prefers a lower matter density (0.297 instead of 0.315, $\chi^2 = 10.5$ for 11 degrees of freedom): with the errors of the CMB DESI quotes a
tension of 2.3 standard deviations between the BAO and the CMB in the cosmological-constant model, which UM-4 keeps, and UM-4 cannot produce the
evolving dark energy that DESI DR2 with the CMB prefers at 3.1 standard deviations, an equation of state $w(a) = w_0 + w_a(1 - a)$ that changes
with the scale factor $a = \mathrm{e}^{a_4}$ of the fold (with its present value $w_0 > -1$ and its slope $w_a < 0$). Status: DERIVED
(`um4_kohnsham.py`, K5, K7 and K10; `um4_krein.py`, KR8; `um4_cosmology.py`, C4 and C5: $w = -1$), STANDARD (DESI's significances), OPEN (the sea,
the tuning).

## The answer

No: dirac16complex is not the dark energy of UM-4. Its particles form cold dark matter; the dark energy is the excess of the tension of the fold, a
free parameter with $w = -1$, tuned to one part in $10^{92}$.

# The open questions answered

On 2026-10-25 the author asked for an analysis and an answer to the questions that the model had left open: whether the indefinite Krein norm
of the charge of dirac16complex is stable; what fields that depend on the extra times do (they would be tachyonic); whether the particles
$\chi$ move faster than light; the primordial era, for which the model had used the values of Planck 2018 as inputs; and the lightest neutrino
mass and the Dirac phase, which the model had set to zero. The answers follow for UM-4; where the warped time changed an answer, the change is
stated.

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
<!-- symbols: -->

The quantised dirac16complex (with FE-43). Each mode $o$ of the field, of the frequency $\omega_o$ and the Krein charge $\mathcal{Q}_o = \pm1$, has the
anticommutator $-\mathcal{Q}_o$ (the canonical anticommutator of the field is minus the Krein operator, the sign chosen so that the particles
$\chi$, the occupied states of charge $-1$, have a positive norm), and every quantum raises the energy by its frequency. In the positive-energy
quantisation, in which the vacuum is annihilated by $\mathsf{a}_o$ for $\omega_o > 0$ and by $\mathsf{a}_o^\dagger$ for $\omega_o < 0$, every particle and
every hole carries a positive energy and the norm $-\mathcal{Q}_o$ of its mode. The particles and the holes of the modes of charge $-1$ are
physical; those of the modes of charge $+1$ are ghosts, states of negative norm. A fermion cannot trade its norm for its energy, because an
anticommutator $-1$ has no representation with a positive norm: no choice of the vacuum removes the ghosts. Status: DERIVED (`um4_krein.py`,
KR1: the Krein operator has eight eigenvalues $+1$ and eight $-1$).

Five results decide the question; they were computed for the Kohn-Sham gas of UM-4 ($m_\Psi/H = 10^4$, $q_{\mathrm{b}} = 0.3\,m_\Psi$).

1. *The vacuum cannot decay.* Every quantum, physical or ghost, carries a positive energy and the energy is conserved, so the vacuum cannot
   decay into pairs of quanta of opposite energy, and a particle $\chi$ cannot fall into a state of negative energy. With the indefinite metric
   the vacuum is nevertheless not a state of lowest energy among the states of positive norm: a superposition of the vacuum with a ghost of
   higher frequency has a negative mean energy. Status: DERIVED (KR1, KR7).
2. *Whether the gas is classically stable is not decided.* At rest the transformations that keep the states at the fold form a Lie algebra of
   dimension 32: 16 compact generators keep the two charges apart, 16 boosts mix them (among them the nine boosts $\Sigma^{ir}$ between ordinary
   space and the extra times). The boosts map the self-consistent gas onto other self-consistent gases (at $G_{\mathrm{KS}} = 0.1$ the residual of
   the Kohn-Sham equation stays $3.5\times10^{-5}$, as without the boost, and the charges stay $-1$): they are exact flat directions, whose
   frequency in the linear response is zero. The linear response truncated to the level at the fold (the admixtures of the four empty orbitals
   of charge $+1$, split from the occupied level by $3.491\times10^{-3}$) has frequencies of the order $10^{-4}\,m_\Psi$, two of them imaginary (up
   to $2.05\times10^{-4}$). The truncation keeps exactly the tangent space of the occupations of the level (result 3), on which the first-order
   energy has a saddle; whether the imaginary pair is an instability of the full response, with the continuum of the bulk, is not decided
   (OPEN). Status: DERIVED (KR2, KR4).
3. *The occupation of the level is a saddle.* Every four-dimensional subspace of negative Krein norm of the eight states of the free level is an
   occupation of four particles $\chi$ (32 real parameters). The first-order interaction energy (the integral of S-9) is stationary at the
   symmetric multiplet that the Kohn-Sham states occupy (0.10216, gradient $3\times10^{-12}$), but its Hessian there has 15 negative eigenvalues,
   16 zero ones (the 16 symmetry generators that mix the charges) and one positive one, and towards the null cone the energy falls without bound
   along some directions ($-1514$ at $\lvert Z\rvert = 0.999$ of the mixing) and rises along others: the repulsive gas has no lowest-energy
   occupation at the first order, and its Kohn-Sham states are the symmetric stationary occupation, not a ground state (an assumption of the
   solution). Status: DERIVED (KR8).
4. *The partner level.* In the self-consistent mean field the level of charge $+1$ next to the occupied one is real and bound up to
   $G_{\mathrm{KS}} = 0.3$, the largest coupling computed, and it moves away from the occupied level as the self-interaction grows (the gap is
   0.0004, 0.0035, 0.0064 and 0.0087 at $G_{\mathrm{KS}} = 0.01$, 0.1, 0.2 and 0.3): the two cannot mix, because they have opposite parity under the
   mirror of the fold (FD-10) in a mirror-even mean field. (In UM-3, computed at $H = 0.05$, 0.15 and $0.3\,m_\Psi$, this level turned complex
   from $G_{\mathrm{KS}} = 0.3$, 0.7 and 1 on, with complex levels that were not converged in the size of the box; states with $q_{\mathrm{b}}$ of
   the order of $H$ are broad resonances in UM-4, not long-lived particles.) Status: DERIVED (KR3, KR5).
5. *The couplings of the fold decide unitarity.* At the fold, at rest, the 16 chirality-blind operators (products of
   $\gamma^{(1)}, \dots, \gamma^{(4)}$) never connect a physical state with a ghost; the 16 chiral ones (the same times $\Gamma_8$) always do. The
   author's Higgs portal acts on the left-handed half only ($P_{\mathrm{L}}$): its amplitude to create a physical $\chi$ together with a ghost
   antiparticle (an s-wave) equals its elastic amplitude, 0.157 (all four singular values of the amplitude matrix, which do not depend on the
   basis of the degenerate multiplets), while a physical pair needs a p-wave. For moving particles the scalar, the density and the vector
   currents still do not mix, the magnetic dipole does, in proportion to the momentum; the convective current of the current portals creates a
   physical pair only with an amplitude of the second order in the momentum, and its chirality-blind combination creates ghost pairs only at the
   next order (relative rate $0.0089\,\vec k^2/m_\Psi^2$: small, but not zero). Ghosts
   are therefore produced wherever the chiral portals act, and chirality-blind couplings are necessary for unitarity but not shown to be
   sufficient. Status: DERIVED (KR6, KR7, KR9).

The answer. The indefinite Krein norm does not make the vacuum decay. Whether it destabilises a gas of $\chi$ is not decided by these
computations: the directions that mix the two charges are exactly flat, the symmetric occupation of the level is a saddle of the first-order
energy, which has no lower bound on the occupations of negative norm, and the truncated response has an imaginary pair whose meaning is open.
The real problem is unitarity: with couplings at the fold that distinguish the two chiralities, the author's left-handed Higgs portal among them, UM-4 produces
ghosts and is not a unitary quantum theory. A unitary UM-4 would need couplings of dirac16complex to the fold that do not distinguish the
chiralities, and these are necessary but not shown to be sufficient (OPEN). The warped time does not change this answer.

## Fields that depend on the extra times

$$
\mathrm{e}^{2H\lvert\sigma\rvert}\Big(\omega^2 - \mathrm{e}^{-2a_4}\,\vec k^2 + \mathrm{e}^{2a_4}\,b_4^{-2}\,\vec\kappa^2\Big) = m_\Psi^2 + p_\sigma^2,\qquad
\omega^2 = \omega_0^2 + \vec k^2 - \vec\kappa^2\quad\big(a_4 = 0,\ b_4 = 1\big) \tag{FE-38}
$$
<!-- symbols: euler, Hconst, sigma, omegafreq, a4, kvec, b4, kappavec, mPsi, psigma, omega0 -->
<!-- begin generated symbol list -->
**Symbols in (FE-38).**

- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $\omega$: A frequency: the energy of a mode $\propto \mathrm{e}^{-\mathrm{i}\omega x_4}$ ($\omega_o$ of the orbital $o$). Unit: GeV. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $\vec k$: The (comoving) momentum along ordinary space, $\vec k^2$ its square. Unit: GeV. Status: STANDARD.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $\vec\kappa$: A momentum along the extra times (three components); the fields of UM-4 have $\vec\kappa = 0$. Unit: GeV. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex in the bulk. Unit: GeV. Status: RECORD.
- $p_\sigma$: The momentum along the hidden direction (local wave number of a profile along $\sigma$). Unit: GeV. Status: DERIVED.
- $\omega_0$: The energy at rest (zero momentum along ordinary space and along the extra times) of a state of dirac16complex at the fold; complex for a resonance, $\omega_0 = \omega_{\mathrm{r}} - \frac{\mathrm{i}}{2}\Gamma_\chi$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The local dispersion relation of dirac16complex with the momentum $p_\sigma$ along the hidden direction, $\vec k$ along ordinary space and $\vec\kappa$
along the extra times, and the exact dispersion of every state at the fold on the static block. In UM-4 the warp multiplies the frequency and
both momenta alike, so the boosts along ordinary space and the rotations of the time into an extra time (generated by
$\frac12\gamma^{(4)}\gamma^{(5)}$, which commutes with $\gamma^{(0)}$, with the chirality and with the mass term) are symmetries: a state at the fold
with the energy $\omega_0$ at rest has $\omega^2 = \omega_0^2 + \vec k^2 - \vec\kappa^2$ exactly. A momentum along a time-like direction enters with the
sign of the frequency: a state with $\lvert\vec\kappa\rvert > \omega_0$ has $\omega^2 < 0$ and grows exponentially in $x_4$, a tachyon. Computed with the
author's matrices ($H = 10^{-4}m_\Psi$, $q_{\mathrm{b}} = 0.3\,m_\Psi$, $\omega_0 = 0.95378\,m_\Psi$): $\omega = 0.94852$, 0.90537 and 0.74141 $m_\Psi$ for
$\lvert\vec\kappa\rvert = 0.1$, 0.3 and 0.6 $m_\Psi$, equal to the prediction to ten digits. (In UM-3 the momentum along the extra times was multiplied by
the warp but the frequency was not, so the states with such a momentum also leaked into the bulk; in UM-4 a state with $\lvert\vec\kappa\rvert \le \omega_0$
is the resonance at rest, rotated in the plane of the time and an extra time, and a state with $\lvert\vec\kappa\rvert > \omega_0$, which no rotation
reaches, is the continuation of the same dispersion to $\omega^2 < 0$.) The same holds for every field, in the bulk as on the fold: a field of
mass $m$ has $\omega^2 = m^2 + \vec k^2 - \vec\kappa^2$ on the static fold and growing modes for every $\vec\kappa^2 > m^2 + \vec k^2$ (a massless field
for every $\lvert\vec\kappa\rvert > \lvert\vec k\rvert$). The metric does not depend on $x_5, x_6, x_7$, so $\vec\kappa$ is conserved. Status: DERIVED (`um4_extratimes.py`, EX1 and
EX2).

$$
\Gamma_{\mathrm{f}} = \frac{-3H_{\mathrm{i}} + \sqrt{9H_{\mathrm{i}}^2 + 4l_{\mathrm{t}}^2}}{2},\qquad
\Gamma_{\mathrm{t}} = \sqrt{l_{\mathrm{t}}^2 - k_{\mathrm{p}}^2},\qquad L_{\mathrm{t}} \ge 2\pi t_0 = 26.6\ \text{Gpc}\ \ (\text{static fold}) \tag{A-8}
$$
<!-- symbols: Gammaf, Hi, lt, Gammat, kp, Lt, pi, tzero -->
<!-- begin generated symbol list -->
**Symbols in (A-8).**

- $\Gamma_{\mathrm{f}}$: The growth rate of a mode of a massless field of the fold with the physical momentum $l_{\mathrm{t}}$ along the extra times and no momentum along ordinary space, on the branch of frozen extra times with the constant expansion rate $H_{\mathrm{i}}$ of ordinary space. Unit: GeV (1/time). Status: DERIVED.
- $H_{\mathrm{i}}$: A constant expansion rate of ordinary space: of the de Sitter fold (whose extra times expand at the same rate) or of an inflation of the fold with frozen extra times. Unit: GeV. Status: DERIVED (FE-87), ASSUMED (FE-88).
- $l_{\mathrm{t}}$: The physical momentum of a mode along the extra times. Unit: GeV. Status: STANDARD.
- $\Gamma_{\mathrm{t}}$: The growth rate of a mode of a massless field of the fold that has a momentum along the extra times, in the late universe. Unit: GeV (1/time). Status: DERIVED.
- $k_{\mathrm{p}}$: The physical momentum of a mode along ordinary space. Unit: GeV. Status: STANDARD.
- $L_{\mathrm{t}}$: The physical period of the extra times, if they are compact. Unit: length. Status: ASSUMED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $t_0$: The age of the universe. Unit: time. Value: 13.8 Gyr. Status: STANDARD.

<!-- end generated symbol list -->

How fast they grow. On a fold with frozen extra times (an expanding fold, as during an inflation of the fold or in the late universe, whose
extra times are held fixed) the physical momentum $l_{\mathrm{t}}$ along the extra times is constant, and a massless mode without a momentum along
ordinary space grows exponentially, with a constant expansion rate $H_{\mathrm{i}}$ of ordinary space at the rate $\Gamma_{\mathrm{f}}$ (computed: 0.646586
for $H_{\mathrm{i}} = 0.3$ and $l_{\mathrm{t}} = 1$, equal to the formula; for a mode of the mass $m$, $l_{\mathrm{t}}^2$ is replaced by $l_{\mathrm{t}}^2 - m^2$, and a
momentum along ordinary space redshifts, so that the growth is no longer a single exponential). On the static fold ($a_4$ and $b_4$ constant) a
massless mode with the physical momenta $l_{\mathrm{t}}$ along the extra times and $k_{\mathrm{p}}$ along ordinary space grows at the rate $\Gamma_{\mathrm{t}}$. If
the extra times were compact with the physical period $L_{\mathrm{t}}$, the slowest mode ($k_{\mathrm{p}} = 0$, $l_{\mathrm{t}} = 2\pi/L_{\mathrm{t}}$) would grow by
less than one e-folding over the age $t_0 = 13.8$ Gyr of the universe only if $L_{\mathrm{t}} \ge 2\pi t_0$, 26.6 Gpc, on the static fold, or about
13.5 Gpc with the Hubble friction of the expanding fold held at its value today (which slows this mode about threefold; an order of
magnitude); but the $n$-th harmonic, $l_{\mathrm{t}} = 2\pi n/L_{\mathrm{t}}$, grows $n$ times faster, so for every $L_{\mathrm{t}}$ infinitely many modes grow
without bound, and a compact time-like direction is itself a closed time-like curve. Status: DERIVED (EX3, EX4).

The answer. Fields that depend on the extra times are tachyonic: every field, in the bulk and on the fold, has growing modes once it carries a
momentum along the extra times larger than its energy at rest (for a field of the mass $m$ and the momentum $\vec k$ along ordinary space,
$\vec\kappa^2 > m^2 + \vec k^2$; a smaller momentum is a rotation of the state at rest). UM-4 keeps only fields without that momentum (ASSUMED). This is a consistent
truncation (the momentum is conserved, so the sector without it is invariant) but not a stable one: interactions of fields without that momentum
create pairs with the opposite momenta $\vec\kappa$ and $-\vec\kappa$, which are tachyonic (EX5; an ESTIMATE, no rate is computed). Making the extra
times compact does not help. UM-4 needs a gauge principle that removes the momentum along the extra times of every field, as the gauge invariance
of electromagnetism removes the unphysical polarisations of the photon; UM-4 does not contain one (OPEN).

## Does anything move faster than light?

In UM-3 the answer was yes: its time was not warped, so the light cone of the bulk was wider than that of the fold, bulk scalars and photons
moved 1.22 and 1.41 times as fast as light on the fold, the bound particles $\chi$ had the speed coefficient
$c_{\mathrm{b}}^2 = q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$ along ordinary space and a group velocity up to 1.0046 times the speed of light, and their loops passed a
Lorentz violation to the electron unless $q_{\mathrm{b}}/H$ was above about $10^{13}$. This was the reason for the author's order of 2026-10-25,
13:15 PDT, and UM-4 answers it.

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

Three facts. (1) dirac16complex is invariant under the boosts of the fold (FE-78): the generator $\mathsf{S}$ of the boosts along $x_3$, built from the
author's matrices, commutes with $\gamma^{(0)}$ and with the chirality, so with the portal terms of the fold, and the warp multiplies the frequency
and the momentum by the same factor. Every state at the fold therefore has $\omega^2 = \omega_0^2 + k^2$ exactly and moves slower than light, at
every momentum; the same holds for every massive mode of every field of the bulk (A-3), and the massless modes travel at the speed of light at
every wavelength. On the static block the metric is the metric of the fold times the warp factor, plus $\mathrm{d}\sigma^2$, so every Lorentz
transformation of the fold leaves it unchanged, and loops of $\chi$ cannot pass a Lorentz violation to the Standard Model: the bound of UM-3 on
$q_{\mathrm{b}}/H$ does not exist in UM-4. (2) Nothing that stays at fixed extra times crosses the static bulk faster than light (FE-83): in the
conformal coordinate $\tilde\sigma$ the static block is flat space of signature (4, 4) times a factor, which does not change which curves are null,
so a signal at fixed extra times that leaves a point of the fold and comes back at the distance $L$ along ordinary space needs the time
$\Delta x_4 \ge L$, equality only along the fold. A null line that also moves by $Y$ along an extra time needs only $\sqrt{L^2 - Y^2}$: in the full
spacetime there is no such bound, and the statement holds for the fields that do not depend on the extra times. Around an expanding fold
(FE-84) the light cone of the bulk is slightly wider than that of the fold wherever the expansion rate falls ($a_4'' < 0$, i.e. a deceleration
parameter above $-1$, which includes today); the path that gains the most arrives earlier than light along the fold by $a_4''^2L^3/(150H^2)$,
which extrapolated to the Hubble distance today is $4.4\times10^{-94}$ of the travel time for $H = 2534$ GeV.
(3) Causality is not protected by the time $x_4$ alone: the four time-like directions of the eight-dimensional metric allow closed time-like curves
through every point (every circle in the plane of the time and an extra time at fixed depth has a tangent of negative squared length everywhere,
for any $a_4$ and $b_4$), and $x_4$ is a time function only on the sections of fixed extra times, on which the fields of UM-4 live. Status: DERIVED
(`um4_bulk.py`, B1, B2, B7 and B10; `um4_spectra.py`, U5; `um4_causality.py`, C1 to C4).

The answer. No observable one: in UM-4 no particle and no signal that stays at fixed extra times moves faster than light on the fold. The
massless fields of the bulk, the photon and the graviton among them, travel at the speed of light at every depth and every wavelength; the
massive modes and the particles $\chi$ are slower; the static bulk offers no shortcut at fixed extra times, and the expanding bulk one of
$4.4\times10^{-94}$ of the travel time over the Hubble distance, far below any measurement. The Standard Model inherits no Lorentz violation, so
the scale $H$ is no longer bounded from above by the speed of the electron; it is bounded from below, by 2534 GeV, by the decays of the Z boson
into the bulk (FE-82). The eight-dimensional spacetime keeps the closed time-like curves of its four time-like directions, and along the extra
times its light cone gives no bound at all: causality on the fold rests on fields that do not depend on the extra times.

## The primordial era

$$
a_4 = Hx_4,\quad b_4 = \text{constant}\ (\mathsf{A} = 1,\ \mathsf{U} = 0):\qquad
\hat R_{ab} \ne 0,\qquad \kappa_7\rho_7 = -3H^2,\quad \kappa_7P_7 = \kappa_7q_7 = -3H^2 \tag{FE-31}
$$
<!-- symbols: a4, Hconst, x4, b4, Asf, Usf, Rhat, ia, ib, kappa7, rho7, P7, q7 -->
<!-- begin generated symbol list -->
**Symbols in (FE-31).**

- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the extra-time components, $b_4 > 0$, never identically 1 (the author's order of 2026-10-24); the scale factor (the factor of the lengths) of the extra times is $\mathrm{e}^{-a_4}b_4$ on the fold and $\mathrm{e}^{-a_4}b_4\,\mathrm{e}^{-H\lvert\sigma\rvert}$ at the distance $\sigma$ from it (the square root of the warp factor times $\mathrm{e}^{-a_4}b_4$). Unit: dimensionless. Status: AUTHOR.
- $\mathsf{A}$: The expansion rate of ordinary space in units of $H$, $\mathsf{A} = a_4'/H$. Unit: dimensionless. Value: 0 at the static block; $H_4^{(0)}/H$ today ($H_4^{(0)}$ the Hubble constant); the first-order equations of the fold hold for $\mathsf{A}^2 \ll 1$; 1 at the author's vacuum, which is not a solution of UM-4. Status: DERIVED.
- $\mathsf{U}$: The rate of change of $b_4$ in units of $H$, $\mathsf{U} = b_4'/(Hb_4)$. Unit: dimensionless. Value: $\mathsf{U} = \mathsf{A}$ with frozen extra times. Status: DERIVED.
- $\hat R$: The curvature of the metric $\hat g_{ab}$ of the fold (FD-2): with four frame indices its Riemann tensor, with two its Ricci tensor $\hat R_{ab}$, without indices its scalar curvature $\hat R$; for frozen extra times the scalar curvature equals that of the four-dimensional metric $\hat h_{\mu\nu}$. Unit: 1/length$^2$. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$ (frame direction $(0)$ along $\sigma$, $(1), (2), (3)$ along ordinary space, $(4)$ along the time, $(5), (6), (7)$ along the extra times); raised and lowered with the frame metric $\eta_{ab} = \mathrm{diag}(1, 1, 1, 1, -1, -1, -1, -1)$; on the fold ($a, b \in \{1, \dots, 7\}$) the frame of the fold; in the tensors of the fold written with its coordinates $x^a$ (its metric $\hat g_{ab}$ and the tensors built from it) a coordinate index of the fold, $a \in \{1, \dots, 7\}$; a repeated index is summed. Status: STANDARD.
- $b$: A frame index (as $a$). Status: STANDARD.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\rho_7$: The energy density of the matter of the fold above its tension in the seven-dimensional normalisation (minus the component $\mathsf{t}^{(4)}{}_{(4)}$: an energy per unit volume of the six other directions of the fold); $V_*\rho_7$ in the four-dimensional normalisation. Unit: GeV$^7$. Status: DERIVED.
- $P_7$: The pressure along ordinary space of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(i)}{}_{(i)}$). Unit: GeV$^7$. Status: DERIVED.
- $q_7$: The pressure along the extra times of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(r)}{}_{(r)}$). Unit: GeV$^7$. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

The author's vacuum, a de Sitter expansion of ordinary space at the rate $H$ with a constant $b_4$, which the earlier versions of the model took
as the primordial era, is not a solution of UM-4: the metric of its fold is not Ricci flat, so the bulk of the author's form is not a vacuum for it,
and as a fold with matter it would need a negative energy density. Status: DERIVED (`um4_primordial.py`, PR0).

$$
\begin{aligned}
&g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{d}\sigma^2 + f_{\mathrm{dS}}^2\Big[\mathrm{e}^{2H_{\mathrm{i}}x_4}\big(\mathrm{d}\vec x^2 - \mathrm{d}\vec x_5^2\big) - \mathrm{d}x_4^2\Big],\qquad
 f_{\mathrm{dS}} = \frac{\sinh\big(H(\sigma_0 - \lvert\sigma\rvert)\big)}{\sinh(H\sigma_0)},\qquad H_{\mathrm{i}} = \frac{H}{\sinh(H\sigma_0)},\\
&\kappa\big(\lambda_{\mathrm{F}} + \rho_{\mathrm{i}}\big) = 12H\coth(H\sigma_0),\qquad
 H_{\mathrm{i}}^2 = \Big(\frac{\kappa(\lambda_{\mathrm{F}} + \rho_{\mathrm{i}})}{12}\Big)^2 - H^2 = \frac{\kappa_7\rho_{\mathrm{i}}}{15}\Big(1 + \frac{\rho_{\mathrm{i}}}{2\lambda_{\mathrm{F}}}\Big)
\end{aligned} \tag{FE-87}
$$
<!-- symbols: metric, iM, iN, diff, Xcoord, sigma, fdS, euler, Hi, x4, xvec, x5vec, sigma0, Hconst, kappa, lambdaF, rhoi, kappa7 -->
<!-- begin generated symbol list -->
**Symbols in (FE-87).**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval, $g^{MN}$ its inverse, $\lvert g\rvert$ the absolute value of its determinant ($\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element). Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}$ in front of a quantity is an infinitesimal change of it (as $\mathrm{d}\sigma$, a small step of $\sigma$); the quotient of two such changes is a derivative; $\mathrm{d}$ with an exponent, in front of several variables, is their volume element, the product of their differentials. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first (Dirac_Einstein-Lovelock_4+4_Nash.nb, section DEFCHART); $X^M$ is the coordinate with the index $M$ and $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element. Unit: length (each coordinate). Status: AUTHOR.
- $\sigma$: The proper coordinate of the hidden direction: $\mathrm{d}\sigma = \lvert\cot z\rvert\,\mathrm{d}x_0$, $\sigma = \mathrm{sgn}(\pi/2 - z)\ln(\sin z)/(6H)$ on one period $0 < z < \pi$; $\sigma = 0$ is the fold $z = \pi/2$, $\sigma \to \mp\infty$ the tips $z \to 0, \pi$; one period of $x_0$ is the whole line $-\infty < \sigma < \infty$. Unit: length. Status: DERIVED.
- $f_{\mathrm{dS}}$: The warp of the de Sitter fold: the factor of the lengths of the fold at the depth $\sigma$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H_{\mathrm{i}}$: A constant expansion rate of ordinary space: of the de Sitter fold (whose extra times expand at the same rate) or of an inflation of the fold with frozen extra times. Unit: GeV. Status: DERIVED (FE-87), ASSUMED (FE-88).
- $x_4$: The time; a prime on a function of $x_4$ alone is $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, $c = 1$). Status: AUTHOR.
- $\vec x$: The position in ordinary space, $\vec x = (x_1, x_2, x_3)$. Unit: length. Status: AUTHOR.
- $\vec x_5$: The position along the extra times, $\vec x_5 = (x_5, x_6, x_7)$; $\mathrm{d}\vec x_5^2 = \mathrm{d}x_5^2 + \mathrm{d}x_6^2 + \mathrm{d}x_7^2$. Unit: length. Status: AUTHOR.
- $\sigma_0$: The depth at which the warp of the de Sitter fold vanishes (a horizon of the bulk), $\sinh(H\sigma_0) = H/H_{\mathrm{i}}$. Unit: length. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: GeV$^{-6}$. Status: AUTHOR.
- $\lambda_{\mathrm{F}}$: The tension that the static block requires of the fold, $\kappa\lambda_{\mathrm{F}} = 12H$: the total vacuum energy of the seven-dimensional fold, made of the tension of the fold fluid and the vacuum energy of the fields of the fold (both have the pressure minus their energy density along ordinary space and along the extra times), per unit volume of the six other directions of the fold (eight-dimensional normalisation); in the four-dimensional normalisation it is $\lambda_{\mathrm{F}}V_*$, and the excess of the total over $\lambda_{\mathrm{F}}V_*$ is the dark energy $\rho_\Lambda$. Unit: GeV$^7$. Value: $12H/\kappa$; $\lambda_{\mathrm{F}}V_* = 30H^2M_{\mathrm{red}}^2 = 1.1\times10^{45}$ GeV$^4$ for $H = 2534$ GeV. Status: DERIVED.
- $\rho_{\mathrm{i}}$: The vacuum energy of the fold above the critical tension $\lambda_{\mathrm{F}}$ that expands the de Sitter fold (eight-dimensional normalisation). Unit: GeV$^7$. Status: DERIVED.
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.

<!-- end generated symbol list -->
<!-- symbols: -->

$$
\mathsf{c}' = 0,\quad a_4' = H_{\mathrm{i}}:\qquad \kappa_7\rho_7 = 3H_{\mathrm{i}}^2,\qquad P_7 = -\rho_7,\qquad q_7 = -2\rho_7,\qquad
\frac{H_{\mathrm{i}}}{H} < \frac{1}{10} \tag{FE-88}
$$
<!-- symbols: cext, prime, a4, Hi, kappa7, rho7, P7, q7, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (FE-88).**

- $\mathsf{c}$: The logarithm of the scale factor of the extra times on the fold, $\mathsf{c} = \ln(\mathrm{e}^{-a_4}b_4)$; $\mathsf{c}' = \mathsf{V}H$; frozen extra times have $\mathsf{c}' = 0$. Unit: dimensionless. Status: DERIVED.
- ${}'$: The derivative of a function of the time $x_4$ alone with respect to $x_4$ ($a_4' = \mathrm{d}a_4/\mathrm{d}x_4$; two primes the second derivative); on a function of $\sigma$ alone (a profile) the derivative with respect to $\sigma$. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: on the fold $\mathrm{e}^{a_4}$ is the scale factor of cosmology and $a_4'$ the Hubble rate. Unit: dimensionless. Status: AUTHOR.
- $H_{\mathrm{i}}$: A constant expansion rate of ordinary space: of the de Sitter fold (whose extra times expand at the same rate) or of an inflation of the fold with frozen extra times. Unit: GeV. Status: DERIVED (FE-87), ASSUMED (FE-88).
- $\kappa_7$: The gravitational coupling of the fold: to the first order in its curvature over $H^2$ the fold obeys the Einstein equations of seven dimensions $\hat G^a{}_b = \kappa_7\mathsf{t}^a{}_b$ with $\kappa_7 = 5\kappa H/2$, the coupling of the massless graviton of the bulk bound to the fold; four-dimensional gravity on the fold has $8\pi G_{\mathrm{N}} = \kappa_7/V_*$ (plus the induced term, which is negligible). Unit: GeV$^{-5}$. Value: $5\kappa H/2$. Status: DERIVED.
- $\rho_7$: The energy density of the matter of the fold above its tension in the seven-dimensional normalisation (minus the component $\mathsf{t}^{(4)}{}_{(4)}$: an energy per unit volume of the six other directions of the fold); $V_*\rho_7$ in the four-dimensional normalisation. Unit: GeV$^7$. Status: DERIVED.
- $P_7$: The pressure along ordinary space of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(i)}{}_{(i)}$). Unit: GeV$^7$. Status: DERIVED.
- $q_7$: The pressure along the extra times of the matter of the fold above its tension in the seven-dimensional normalisation (the component $\mathsf{t}^{(r)}{}_{(r)}$). Unit: GeV$^7$. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.

<!-- end generated symbol list -->
<!-- symbols: -->

The two candidates for an inflation of the fold. The exact de Sitter fold (FE-87), a fold with a tension above the critical one in the bulk of
constant curvature, expands at the rate $H_{\mathrm{i}}$ in all its space-like and time-like directions: the extra times inflate together with ordinary
space, the factor $\mathcal{Z}$ of the couplings of the fold grows like $\mathrm{e}^{3N}$ after $N$ e-folds, and every coupling of the fold falls like
$\mathrm{e}^{-3N}$, by $6.7\times10^{-79}$ after 60 e-folds: it is not the primordial era of our universe. The inflation with frozen extra times
(FE-88), which the observed constancy of the couplings requires, needs the pressure $q_7 = -2\rho_7$ along the extra times, so the fold fluid adds
$q_{\mathrm{hold}} = -\rho_7$, a pressure of the size of the vacuum energy of the inflation (in UM-3, with its small $H$, it had to be about
$\mathsf{A}^4/8$ times the tension of the fold, with $\mathsf{A}$ the rate of the inflation in units of $H$: at least $10^{103}$ times for an inflation at
the largest allowed rate); the exact equations of such a fold in a bulk of
constant curvature have no solution for $H_{\mathrm{i}} \ne 0$, so it needs a Weyl tensor of the bulk, whose bulk solution is not computed. Status:
DERIVED (`um4_primordial.py`, PR1, PR2 and PR5), OPEN (the Weyl tensor of the bulk, the origin of the holding pressure).

$$
\begin{aligned}
&r_{\mathrm{T}} < 0.032:\qquad H_{\mathrm{i}} < \pi M_{\mathrm{red}}\sqrt{\frac{r_{\mathrm{T}}A_{\mathrm{s}}}{2}} = 4.43\times10^{13}\ \text{GeV},\\
&\frac{H_{\mathrm{i}}}{H} < \frac{1}{10}:\qquad H > 4.4\times10^{14}\ \text{GeV}\ \ \text{or}\ \ H_{\mathrm{i}} < 253\ \text{GeV}\ \ (H = 2534\ \text{GeV})
\end{aligned} \tag{S-24}
$$
<!-- symbols: rT, Hi, pi, Mred, As, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (S-24).**

- $r_{\mathrm{T}}$: The ratio of the amplitudes of the primordial spectra of gravitational waves (tensor) and of curvature (scalar) at the pivot scale. Unit: dimensionless. Value: below 0.032 (Planck PR4 with BICEP/Keck 2018 and BAO, M. Tristram et al. 2022, 95 per cent). Status: STANDARD.
- $H_{\mathrm{i}}$: A constant expansion rate of ordinary space: of the de Sitter fold (whose extra times expand at the same rate) or of an inflation of the fold with frozen extra times. Unit: GeV. Status: DERIVED (FE-87), ASSUMED (FE-88).
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ of the metric, the cosmological constant $\Lambda = -21H^2$ and the tension $\kappa\lambda_{\mathrm{F}} = 12H$ of the fold; in UM-4 a free parameter, bounded from below by the propagation of the gauge fields in the bulk. Unit: GeV (1/length). Value: $H > 2534$ GeV, about 2.5 TeV (from the invisible width of the Z boson). Status: AUTHOR.

<!-- end generated symbol list -->

$$
\xi_{\mathrm{H}} = N_{\mathrm{e}}\sqrt{\frac{\lambda}{72\pi^2A_{\mathrm{s}}}},\qquad n_{\mathrm{S}} = 1 - \frac{2}{N_{\mathrm{e}}},\qquad r_{\mathrm{T}} = \frac{12}{N_{\mathrm{e}}^2},\qquad
H_{\mathrm{i}} = \sqrt{\frac{\lambda}{12}}\,\frac{M_{\mathrm{red}}}{\xi_{\mathrm{H}}} \tag{S-25}
$$
<!-- symbols: xiH, Ne, lamH, pi, As, nS, rT, Hi, Mred -->
<!-- begin generated symbol list -->
**Symbols in (S-25).**

- $\xi_{\mathrm{H}}$: The coupling of the Higgs doublet to the scalar curvature of the fold, the term $-\xi_{\mathrm{H}}\hat R\,\Phi^\dagger\Phi$ in the Lagrangian of the fold: an extension of UM-4, whose Higgs Lagrangian has no such term ($\xi_{\mathrm{H}} = 0$). Unit: dimensionless. Value: 0 in UM-4; about $1.6\times10^4$ if the Higgs field drove inflation (ESTIMATE, an extension of the action). Status: ESTIMATE (an extension of the action).
- $N_{\mathrm{e}}$: The number of e-foldings of inflation after the pivot scale left the horizon. Unit: dimensionless. Value: 55. Status: STANDARD.
- $\lambda$: The quartic coupling of the Higgs potential, $\lambda > 0$. Unit: dimensionless. Value: $\lambda = m_h^2/(2v^2) = 0.129$. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $A_{\mathrm{s}}$: The amplitude of the primordial curvature spectrum at the pivot $k_*$. Unit: dimensionless. Value: $2.10\times10^{-9}$ (Planck 2018). Status: ASSUMED.
- $n_{\mathrm{S}}$: The spectral index of the primordial curvature spectrum. Unit: dimensionless. Value: 0.965 (Planck 2018). Status: ASSUMED.
- $r_{\mathrm{T}}$: The ratio of the amplitudes of the primordial spectra of gravitational waves (tensor) and of curvature (scalar) at the pivot scale. Unit: dimensionless. Value: below 0.032 (Planck PR4 with BICEP/Keck 2018 and BAO, M. Tristram et al. 2022, 95 per cent). Status: STANDARD.
- $H_{\mathrm{i}}$: A constant expansion rate of ordinary space: of the de Sitter fold (whose extra times expand at the same rate) or of an inflation of the fold with frozen extra times. Unit: GeV. Status: DERIVED (FE-87), ASSUMED (FE-88).
- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->

The scales of the inflation (S-24) and Higgs inflation (S-25). The tensor bound $r_{\mathrm{T}} < 0.032$ (Planck PR4 with BICEP/Keck 2018 and BAO,
M. Tristram et al. 2022, 95 per cent) with the measured amplitude $A_{\mathrm{s}} = 2.1\times10^{-9}$ of the scalar perturbations limits any inflation to
$H_{\mathrm{i}} < 4.4\times10^{13}$ GeV. The equations of the fold are those of general relativity only for $(12/25)(H_{\mathrm{i}}/H)^2 \ll 1$, that is
$H_{\mathrm{i}} < H/10$: an inflation at the tensor bound needs $H > 4.4\times10^{14}$ GeV, and with $H$ at its lower bound of 2534 GeV only an inflation
with $H_{\mathrm{i}} < 253$ GeV (an energy scale below $3.3\times10^{10}$ GeV) is in that regime. If the Higgs doublet had a coupling $\xi_{\mathrm{H}}$ to the
curvature of the fold, which the Higgs Lagrangian of UM-4 does not contain, the Higgs field could drive the inflation of the fold: with
$N_{\mathrm{e}} = 55$ e-folds, $\xi_{\mathrm{H}} = 16195$ ($\lambda = 0.1294$) or 4502 ($\lambda = 0.01$, the running value near the scale of inflation),
$n_{\mathrm{S}} = 0.9636$ and $r_{\mathrm{T}} = 0.0040$ (0.3 standard deviations below Planck 2018, $0.9649 \pm 0.0042$, and 3.5 below ACT DR6 combined with
Planck, CMB lensing and DESI, $0.974 \pm 0.003$), and $H_{\mathrm{i}} = 1.6\times10^{13}$ GeV, so that UM-4 would need $H > 1.6\times10^{14}$ GeV for it.
Status: DERIVED (`um4_primordial.py`, PR3), ESTIMATE (PR4, an extension of the action), STANDARD (the measurements).

$$
\frac{1}{16\pi G_{\mathrm{ind}}} = \frac{N_{\mathrm{ind}}\,\Lambda_{\mathrm{c}}^2}{192\pi^2},\qquad
N_{\mathrm{ind}} = \sum_{\text{real scalars}}\big(1 - 6\xi\big) + N_{\mathrm{Weyl}} - 4N_{\mathrm{gauge}} = 52 - 24\xi_{\mathrm{H}} \tag{FE-64}
$$
<!-- symbols: pi, Gind, Nind, Lambdac, xinm, NWeyl, Ngauge, xiH -->
<!-- begin generated symbol list -->
**Symbols in (FE-64).**

- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_{\mathrm{ind}}$: The Newton constant of the induced Einstein-Hilbert term of the fold, $\kappa_{\mathrm{ind}} = 8\pi G_{\mathrm{ind}}$. Unit: GeV$^{-2}$. Status: ESTIMATE.
- $N_{\mathrm{ind}}$: The weighted number of the fields of the fold that induce the Einstein-Hilbert term: each real scalar counts $1 - 6\xi$, each Weyl fermion 1, each gauge field $-4$ (with its ghost fields). Unit: dimensionless. Value: 52 for the fields of the fold of UM-4 (the four real scalars of the Higgs doublet and 48 Weyl fermions; the gauge fields live in the bulk) with $\xi_{\mathrm{H}} = 0$; $52 - 24\xi_{\mathrm{H}}$ with the curvature coupling $\xi_{\mathrm{H}}$ of an extension. Status: DERIVED.
- $\Lambda_{\mathrm{c}}$: The cutoff of the proper-time integral of the one-loop effective action of the fields of the fold: the highest energy of the quantum fluctuations that induce gravity. Unit: GeV. Value: taken of the order of $H$ (2534 GeV); the induced term alone would give the measured Newton constant for $\Lambda_{\mathrm{c}} = \pi M_{\mathrm{red}}\sqrt{96/52} = 1.0\times10^{19}$ GeV. Status: ESTIMATE.
- $\xi$: The coupling of a real scalar field to the scalar curvature $\hat R$ of the fold: the term $-\frac12\xi\hat R$ times the square of the field in its Lagrangian ($\xi = 1/6$ is the conformal coupling). Unit: dimensionless. Status: STANDARD.
- $N_{\mathrm{Weyl}}$: The number of Weyl (two-component) fermion fields of the fold. Unit: dimensionless. Value: 48 (three generations of quarks and leptons with three right-handed neutrinos). Status: STANDARD.
- $N_{\mathrm{gauge}}$: The number of gauge fields of the fold. Unit: dimensionless. Value: 0 in UM-4 (the gauge fields live in the bulk); 12 (eight gluons, three $W$, one $B$) if they lived on the fold. Status: STANDARD.
- $\xi_{\mathrm{H}}$: The coupling of the Higgs doublet to the scalar curvature of the fold, the term $-\xi_{\mathrm{H}}\hat R\,\Phi^\dagger\Phi$ in the Lagrangian of the fold: an extension of UM-4, whose Higgs Lagrangian has no such term ($\xi_{\mathrm{H}} = 0$). Unit: dimensionless. Value: 0 in UM-4; about $1.6\times10^4$ if the Higgs field drove inflation (ESTIMATE, an extension of the action). Status: ESTIMATE (an extension of the action).

<!-- end generated symbol list -->
<!-- symbols: -->

The induced gravity of the fold. The Einstein-Hilbert term that the fields of the fold induce at one loop (the Higgs doublet and the 48 Weyl
fermions of the quarks and leptons with three right-handed neutrinos; the gauge fields are in the bulk) is negligible for a cutoff of the order of
$H$: $1/(8\pi G_{\mathrm{ind}}) = 5.9\times10^{-32}M_{\mathrm{red}}^2$ at $\Lambda_{\mathrm{c}} = H = 2534$ GeV. The gravity of the fold is that of the bulk graviton, and
a coupling $\xi_{\mathrm{H}} \ne 0$ would not be needed for it. Status: ESTIMATE (`um4_foldsources.py`, FS3).

The answer. The author's vacuum is not a solution of UM-4. The exact de Sitter fold inflates the extra times as well and is excluded by the
constancy of the couplings. The primordial era of UM-4 can be an inflation of the fold with frozen extra times, which is the inflation of
four-dimensional general relativity, if the fold fluid supplies a holding pressure of the size of its vacuum energy, if a Weyl tensor of the bulk
completes the solution, and if its rate is below $H/10$, which for $H$ near its lower bound means an inflation far below the scales of the usual
models. UM-4 does not specify its inflaton: Higgs inflation is an extension that would need $H > 1.6\times10^{14}$ GeV. What precedes inflation and the
reheating after it are not computed, and the Planck values remain inputs of the cosmological calculation (OPEN).

## The lightest neutrino mass and the Dirac phase

$$
\big(\lvert U_{\mathrm{e}i}\rvert^2\big)_{i = 1, 2, 3} = \big(\cos^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{12}\cos^2\theta_{13},\ \sin^2\theta_{13}\big) \tag{S-17}
$$
<!-- symbols: Uei, ii, thetaij -->
<!-- begin generated symbol list -->
**Symbols in (S-17).**

- $U_{\mathrm{e}i}$: The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$. Unit: dimensionless. Value: $\lvert U_{\mathrm{e}i}\rvert^2 = 0.682$, 0.296 and 0.022 for $i = 1, 2, 3$ (NuFIT 5.2, the fit without the Super-Kamiokande atmospheric data: the values of the record; NuFIT 6.0 with them gives 0.677, 0.301 and 0.022). Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal), and in a tensor of ordinary space such as $\mathsf{h}_{ij}$ one of the directions $x_1, x_2, x_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\theta_{12},\ \theta_{13},\ \theta_{23}$: The three mixing angles of $U_{\mathrm{PMNS}}$ (its fourth parameter is the Dirac phase, which does not enter the electron-flavour results of UM-4). Unit: dimensionless. Value: $33.40^\circ$, $8.54^\circ$, $49.14^\circ$ in the computations of UM-4 ($\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$: NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); $33.71^\circ$, $8.56^\circ$, $43.28^\circ$ in NuFIT 6.0 (2024, with the Super-Kamiokande atmospheric data; $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$). Status: STANDARD.

<!-- end generated symbol list -->

The Dirac phase $\delta_{\mathrm{CP}}$. The mixing matrix is three rotations by the angles $\theta_{23}$, $\theta_{13}$ and $\theta_{12}$, the phase attached to
the middle one, and its electron row (S-17) contains no phase. Every flavour result of UM-4 is a result for electron neutrinos: the solar survival
probabilities, the conversion in the envelope of a supernova (the matter potential acts on $\nu_e$ only, so the phase can be moved into $\nu_\mu$
and $\nu_\tau$), and the capture of the cosmic neutrinos. Computed with the global fit NuFIT 6.0 (I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni,
I. Martinez-Soler, J. P. Pinheiro and T. Schwetz, JHEP 12 (2024) 216; with the atmospheric data of Super-Kamiokande, $\delta_{\mathrm{CP}} = 212^\circ$
in the normal ordering), the electron row is the same for $\delta_{\mathrm{CP}} = 0$, $177^\circ$, $212^\circ$ and $274^\circ$ to $7\times10^{-18}$, and the
envelope gives the same survival probability as with $\delta_{\mathrm{CP}} = 0$ to $6\times10^{-14}$. The phase appears only in the appearance
channels, which UM-4 does not compute (in vacuum at 295 km and 0.6 GeV, the baseline and the peak energy of T2K, $\nu_\mu \to \nu_e$ has the
probability 0.0421, 0.0478 and 0.0541 for $\delta_{\mathrm{CP}} = 0$, $212^\circ$ and $270^\circ$, $\bar\nu_\mu \to \bar\nu_e$ 0.0421, 0.0346 and 0.0291),
and in the Jarlskog invariant of CP violation, $-0.0178$ at $212^\circ$. Status: DERIVED (`um4_numass.py`, NM3).

$$
m_2 = \sqrt{m_1^2 + \Delta m^2_{21}},\qquad m_3 = \sqrt{m_1^2 + \Delta m^2_{31}},\qquad
m_1 < 23\ \text{meV}\ \ (\text{95 per cent}),\qquad
m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2 \tag{S-18}
$$
<!-- symbols: mferm, Delta, mmass, ii, meff, Uei -->
<!-- begin generated symbol list -->
**Symbols in (S-18).**

- $m_u, \dots, m_3$: The masses of the quarks ($m_u, m_c, m_t$; $m_d, m_s, m_b$), of the charged leptons ($m_e, m_\mu, m_\tau$) and of the three neutrino mass states ($m_1, m_2, m_3$, Dirac masses). Unit: GeV. Value: measured values; $\Delta m_{21}^2 = 7.41\times10^{-5}$ eV$^2$, $\lvert\Delta m_{31}^2\rvert = 2.511\times10^{-3}$ eV$^2$ in the computations of UM-4 (the global fit NuFIT 5.2 of the oscillation data, November 2022), $7.49\times10^{-5}$ and $2.513\times10^{-3}$ eV$^2$ in NuFIT 6.0 (2024); the lightest mass $m_1 = 0$ in the computations, below 23 meV by DESI DR2 with the CMB and NuFIT 6.0. Status: STANDARD.
- $\Delta$: A change, difference or small variation of the quantity that follows (for example an interval of the time, a perturbation of a density, a difference of two squared masses, or an addition to an effective number of species). Status: STANDARD.
- $m$: A mass: $m_i$ the mass of the neutrino mass state $i$; $\Delta m_{ij}^2 = m_i^2 - m_j^2$ the squared-mass difference of the states $i$ and $j$ ($\Delta m_{21}^2$, $\Delta m_{31}^2$, $\Delta m_{32}^2$); $\Delta m^2$ without labels the difference of the two states of a resonance, $m_2^2 - m_1^2$, multiplied by $v_{\mathrm{loc}}^2/v^2$ where this differs from 1; $m$ without a label the mass of a mode of a field of the bulk as the fold sees it, $m^2 = \omega^2 - k^2$; for the W and Z bosons their complex pole mass, $m^2 = m_0^2 - \mathrm{i}m_0\Gamma_{\mathrm{bulk}}$ to the leading order; in the relic abundance of the particles $\chi$ their mass. Unit: GeV. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal), and in a tensor of ordinary space such as $\mathsf{h}_{ij}$ one of the directions $x_1, x_2, x_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $m_{\mathrm{eff}}$: The effective mass of the electron neutrino measured in the beta decay of tritium, $m_{\mathrm{eff}}^2 = \sum_i\lvert U_{\mathrm{e}i}\rvert^2m_i^2$. Unit: eV. Value: below 0.45 eV (KATRIN 2025, 90 per cent). Status: STANDARD.
- $U_{\mathrm{e}i}$: The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$. Unit: dimensionless. Value: $\lvert U_{\mathrm{e}i}\rvert^2 = 0.682$, 0.296 and 0.022 for $i = 1, 2, 3$ (NuFIT 5.2, the fit without the Super-Kamiokande atmospheric data: the values of the record; NuFIT 6.0 with them gives 0.677, 0.301 and 0.022). Status: STANDARD.

<!-- end generated symbol list -->

$$
\Gamma_{\mathrm{C\nu B}} = N_{\mathrm{T}}\,\bar\sigma_{\mathrm{T}}\,\frac{n_\nu^{(0)}}{2}\sum_{i=1}^{3}\lvert U_{\mathrm{e}i}\rvert^2\big(1 + \mathsf{s}_i\big)\qquad(\text{Dirac neutrinos}) \tag{S-28}
$$
<!-- symbols: GammaCnuB, NT, sigmabarT, nnu, ii, Uei, sstate -->
<!-- begin generated symbol list -->
**Symbols in (S-28).**

- $\Gamma_{\mathrm{C\nu B}}$: The rate at which a tritium target captures neutrinos of the cosmic neutrino background. Unit: 1/time. Status: STANDARD.
- $N_{\mathrm{T}}$: The number of tritium nuclei of the target. Unit: dimensionless. Value: $2.0\times10^{25}$ for 100 g. Status: STANDARD.
- $\bar\sigma_{\mathrm{T}}$: The averaged cross-section of the capture of an electron neutrino on tritium: a tritium nucleus captures left-handed electron neutrinos of mean speed $\mathsf{s}$ and number density $n$ at the rate $\bar\sigma_{\mathrm{T}}(1 + \mathsf{s})\,c\,n$ ($c$ the speed of light, 1 in the formulas; Long, Lunardini and Sabancilar). Unit: cm$^2$. Value: $3.834\times10^{-45}$ cm$^2$. Status: STANDARD.
- $n_\nu$: The number density of the cosmic neutrino background per flavour (neutrinos plus antineutrinos, one helicity each); $n_\nu^{(0)}$ its value today. Unit: GeV$^3$. Value: 112 cm$^{-3}$ today. Status: STANDARD.
- $i$: A generation index ($i = 1, 2, 3$), which also labels the three neutrino mass states; in a frame component such as $\mathcal{S}^{(i)}{}_{(i)}$ one of the three directions of ordinary space (the three components are equal), and in a tensor of ordinary space such as $\mathsf{h}_{ij}$ one of the directions $x_1, x_2, x_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $U_{\mathrm{e}i}$: The electron row of the mixing matrix, $U_{\mathrm{e}i} = (U_{\mathrm{PMNS}})_{ei}$: $\lvert U_{\mathrm{e}i}\rvert^2$ is the electron-flavour fraction of the mass state $i$. Unit: dimensionless. Value: $\lvert U_{\mathrm{e}i}\rvert^2 = 0.682$, 0.296 and 0.022 for $i = 1, 2, 3$ (NuFIT 5.2, the fit without the Super-Kamiokande atmospheric data: the values of the record; NuFIT 6.0 with them gives 0.677, 0.301 and 0.022). Status: STANDARD.
- $\mathsf{s}_i$: The mean speed of the neutrino mass state $i$ today, averaged over its momentum distribution (0 for a state at rest, 1 for a massless one). Unit: dimensionless. Value: 1, 0.061 and 0.011 for the mass states 1, 2 and 3 with $m_1 = 0$; 0.023 for the state 1 with $m_1 = 23$ meV. Status: STANDARD.

<!-- end generated symbol list -->

The lightest mass $m_1$. DESI DR2 (the BAO) with the CMB, combined with NuFIT 6.0 (W. Elbers et al., arXiv:2503.14744; the
cosmological-constant model, 95 per cent), bounds the lightest mass to $m_1 < 23$ meV in the normal ordering (24 meV in the inverted one) and the
sum of the masses to 0.101 eV (normal) and 0.133 eV (inverted); the inverted ordering, whose smallest sum is 0.0989 eV, is disfavoured (the
probability of the normal ordering is 0.91) but not excluded. With $\Delta m^2_{21} = 7.49\times10^{-5}$ eV$^2$ and
$\Delta m^2_{31} = 2.513\times10^{-3}$ eV$^2$ (S-18) the masses at $m_1 = 23$ meV are 23.00, 24.57 and 55.15 meV, and the effective mass of tritium beta
decay is 8.84 to 24.64 meV in this range, far below the limit 0.45 eV of KATRIN. Within the range $m_1$ changes one result of UM-4, the capture
rate of the cosmic neutrinos (S-28): on 100 g of tritium it falls from 6.88 per year at $m_1 = 0$ to 4.15 per year at $m_1 = 23$ meV, as the lightest mass state
$\nu_1$ becomes slow (mean speed 0.023) and loses the doubling of the capture of relativistic neutrinos (4.06 per year if all states were at rest).
Status: DERIVED (`um4_numass.py`, NM1, NM2 and NM4), STANDARD (the bounds).

The answer. Setting the Dirac phase to zero was without consequence: it drops out of every result of UM-4. The lightest mass is not fixed by any
measurement; DESI DR2 with NuFIT 6.0 bounds it below 23 meV, and within this range it lowers the capture rate of the cosmic neutrinos by up to
40 per cent. The results computed with NuFIT 5.2 differ from NuFIT 6.0 by at most 1.5 per cent (NM5). The neutrino sector does not depend on the
warp of the time: the neutrinos live on the fold.

# What the author may have left out

The author asked to be told if something important was missing from his specification. UM-4 had to add the following, and the analysis found the
following problems.

| item | why it is needed or what it means | where it stands |
| ------ | ------ | ------ |
| right-handed quark singlets and the Yukawa couplings | the quark doublets alone have no masses, and the hypercharges cancel the gauge anomalies only with the singlets | added (a default proposed in the notification of 2026-10-24, 17:20, which the author did not answer: ASSUMED) |
| three right-handed neutrinos | Dirac neutrino masses and the mixing that flavour conversion needs; the anomalies still cancel | added (accepted by the author, 2026-10-24, 17:32); they must never thermalise, or they would add 0.141 to the effective number of neutrino species at the masses of the particles $\chi$ of UM-4 (0.14 to 0.24 for masses of 10 TeV to 10 GeV) |
| the warped time | in UM-3 the time was not warped, so the light cone of the bulk was wider than that of the fold and every field of the bulk outran light on the fold | the author's order of 2026-10-25, 13:15 PDT: the time carries the warp factor of the other six directions of the fold (FE-27); among the static warps of the author's form only equal rates in all seven directions give a vacuum of Einstein gravity with a cosmological constant (DERIVED, `um4_geometry.py`, G10) |
| the gravity | the author's Einstein-Lovelock action has free weights | Einstein gravity with $\Lambda = -21H^2$ (the weights of the Gauss-Bonnet and cubic terms set to zero), the only choice for which gravitons travel on the light cone on every background, not only around the static block (DERIVED, `um4_gravity.py`, L1 to L4) |
| the gauge fields in the bulk | the order puts the photon in the bulk; with it the electroweak fields, of which it is a combination | ASSUMED for all gauge fields; their massless modes are bound to the fold and travel at the speed of light, the W and Z bosons become resonances of the bulk, and the invisible width of the Z boson bounds $H > 2534$ GeV (FE-82) |
| a thin source at the fold | the kink of the warp factor $\mathrm{e}^{-2H\lvert\sigma\rvert}$ requires one (the fold fluid); at the static block it is a pure tension, $\kappa\lambda_{\mathrm{F}} = 12H$, like the brane of Randall and Sundrum; its excess over $\lambda_{\mathrm{F}}$ is the dark energy, tuned to one part in $10^{92}$ (S-4) | ASSUMED (its values DERIVED); OPEN (the tuning) |
| the gravity of the fold | the fold obeys the Einstein equations of seven dimensions with the coupling of the massless graviton of the bulk, with frozen extra times the Friedmann equations of general relativity, with corrections of the relative order $(a_4'/H)^2$ (in the equation of the energy $(a_4'/H)^2/25$ for radiation and $11(a_4'/H)^2/400$ for dust); its gravitational waves travel at the speed of light at every wavelength, with the plus and cross polarisations; of the other polarisations of the graviton of the bulk the three vectors $h_{\mu r}$ are ghosts, which the matter of the fold does not emit at the linear order; dust requires a projected Weyl tensor of the bulk at the order of the square of its density over the tension | DERIVED; OPEN (the Weyl tensor of the bulk; the ghost vectors beyond the linear order) |
| the volume of the extra times | it is not frozen by itself: dust and vacuum energy drive it, and a free volume would change Newton's constant 8545 times faster than lunar laser ranging allows; the fold fluid must add the pressure $-0.842\rho_{\mathrm{c}}^{(0)}$ along the extra times today (with no pressure of the baryons along them; $-0.793$ or $-0.891\rho_{\mathrm{c}}^{(0)}$ with $-\rho_{\mathrm{b}}$ or $+\rho_{\mathrm{b}}$), and minus the vacuum energy of an inflation of the fold | ASSUMED (the holding pressure and the pressure of the baryons); OPEN (its origin, a potential for the volume) |
| frozen extra times in the late universe | otherwise the couplings of the Standard Model change: Newton's constant, the squares of the gauge and Yukawa couplings and the quartic Higgs coupling of the fold are divided by the factor $\mathcal{Z}$ of the volume of the extra times | required, and held by the fold fluid |
| a gauge field for the ad hoc Higgs vacuum | the literal ad hoc vacuum carries an isospin charge that the Gauss law forbids; with the pure-gauge field $W^2$ along the time (the value at the fold of the field of the bulk) it is a rotated vacuum with one radial residual; its potential energy must never exceed that of the radiation, which requires the decay rate $a_{40} > 4.8\times10^{-16}(v_{\mathcal{A}}/v)^2$ GeV, and then it is gone long before nucleosynthesis | DERIVED; ESTIMATE (the radiation era from $x_4 = 0$) |
| the Krein norm of dirac16complex | the signature $(4,4)$ of the author's matrices makes the charge indefinite; quantised, it has ghosts that no vacuum removes; the vacuum cannot decay, the classical stability of the gas is not decided (its symmetric occupation is a saddle of the first-order energy); chiral couplings at the fold produce ghosts | DERIVED; ASSUMED (the symmetric occupation); OPEN: the stability of the gas, a unitary coupling (chirality-blind at the fold is necessary, not shown sufficient) |
| the extra times | fields with a momentum along them larger than their mass and their momentum along ordinary space are tachyonic; the restriction to fields without a momentum along them is consistent but unstable; compact extra times do not help (the $n$-th harmonic grows $n$ times faster than the first, and a compact time-like direction is a closed time-like curve) | ASSUMED (no dependence); OPEN: a gauge principle that removes that momentum |
| causality | nothing that stays at fixed extra times moves observably faster than light in UM-4 (the expanding bulk is ahead by $4.4\times10^{-94}$ over the Hubble distance), but along the extra times the light cone gives no bound, and the four time-like directions allow closed time-like curves through every point | DERIVED; causality on the fold rests on fields that do not depend on the extra times |
| the binding of $\chi$ to the fold | the states of dirac16complex at the fold are resonances, which live longer than 160 Gyr only if $m_\Psi/H$ is large enough (1135 for $q_{\mathrm{b}} = m_\Psi/2$, less for a stronger binding); bound by the author's Higgs portal they would have to be bound so weakly (direct detection) that they live long enough only for $H < 2.5$ GeV, below the bound $H > 2534$ GeV, and a binding by the gluon condensate makes them scatter on nucleons 29 to 33 orders of magnitude above the limit | OPEN: a binding that does not couple $\chi$ to nucleons (A-6) |
| the origin of the dark matter | the long-lived particles $\chi$ are heavier than any thermal relic that unitarity allows ($9.69\times10^4$ GeV) unless they are bound more strongly than $q_{\mathrm{b}} \approx 0.9\,m_\Psi$, and the current portals cannot set the relic density of a perturbatively coupled $\chi$ | OPEN: a strong binding with an annihilation channel, or a non-thermal origin of the abundance |
| the dark energy | a vacuum energy with $w = -1$; DESI DR2 prefers an evolving one | OPEN (tension at 2.3 to 3.1 standard deviations) |
| the primordial era | the author's vacuum is not a solution; the de Sitter fold inflates the extra times; an inflation with frozen extra times needs a Weyl tensor of the bulk and, in the regime of general relativity, a rate below $H/10$ (below 253 GeV for $H = 2534$ GeV); the Higgs field could drive it only with a curvature coupling that the action does not contain | DERIVED; ESTIMATE (Higgs inflation, an extension); OPEN (the inflaton, the Weyl tensor; Planck inputs) |
| the lightest neutrino mass and the Dirac phase | not fixed by the specification; the phase drops out of every result of UM-4; DESI DR2 with NuFIT 6.0 bounds $m_1 < 23$ meV, which changes only the capture rate of the cosmic neutrinos | DERIVED (the phase is irrelevant); ASSUMED: $m_1 = 0$ within the bound |

# UM-4 compared with UM-3

UM-3 is kept unchanged as the record of the model before the order of 2026-10-25, 13:15 PDT. The table lists what the warped time changed; the
values of UM-3 are records.

| | UM-3 | UM-4 |
| ------ | ------ | ------ |
| the time component of the metric | $-1$: the time not warped | $-(\sin^2z)^{1/6}$: the time warped like the other six directions of the fold |
| the light cone of the bulk at the depth $\sigma$ | $\mathrm{e}^{H\lvert\sigma\rvert}$ times wider than that of the fold | that of the fold at every depth |
| the static block | a space whose curvature is $-H^2$ in the planes without the time and zero in the seven planes with the time | a space of constant curvature $-H^2$ in all 28 planes (locally the space of constant negative curvature of eight dimensions and signature (4, 4), the analogue of anti-de Sitter space) |
| the gravity | the Lovelock weights $1, 1/20, 1/360$ with $\Lambda = -7H^2$: a degenerate vacuum without linear gravitons in the static bulk | Einstein gravity with $\Lambda = -21H^2$: a vacuum with a massless graviton bound to the fold |
| bulk scalars and photons | 1.22 and 1.41 times the speed of light at long wavelengths, faster than light at every wavelength | the massless modes at the speed of light, the massive modes slower |
| the gravitational wave | the four-dimensional graviton at the speed of light at linear order only | the massless graviton of the bulk at the speed of light at every depth and wavelength, with the plus and cross polarisations (helicity $\pm2$); its three vector polarisations $h_{\mu r}$ are ghosts, not emitted by the matter of the fold at the linear order |
| the gauge fields of the Standard Model | on the fold | in the bulk; the photon a transverse wave of spin 1 bound to the fold |
| the spectrum of the hidden direction | gaps $3H$ (scalars) and $2H$ (gauge fields) above the massless modes | no gap: a continuum from zero mass (A-3) |
| the states of dirac16complex at the fold | eight bound states | eight long-lived resonances that tunnel into the bulk |
| their speed | the speed coefficient $c_{\mathrm{b}}^2 = q_{\mathrm{b}}/(q_{\mathrm{b}} - H)$, a group velocity up to 1.0046 times the speed of light | exactly relativistic, $\omega^2 = \omega_0^2 + k^2$ |
| the author's constant $H$ | below about $5\times10^{-13}$ GeV (the Lorentz violation passed to the electron, for $\omega_{\mathrm{b}} = 1.5$ TeV) | above 2534 GeV (the invisible width of the Z boson) |
| the dark matter | a thermal relic, weakly bound and leptophilic, heavier than about 1.5 TeV | a thermal relic only if bound more strongly than $q_{\mathrm{b}} \approx 0.9\,m_\Psi$ (then of the order of $10^4$ to $10^5$ GeV), otherwise of non-thermal origin (heavier than $2.5\times10^6$ GeV for $q_{\mathrm{b}} = m_\Psi/2$); a binding without a nucleon coupling needed (OPEN) |
| the inflation of the fold with frozen extra times | a holding pressure of about $\mathsf{A}^4/8$ times the tension of the fold | a holding pressure of the size of the vacuum energy of the inflation, a Weyl tensor of the bulk, and a rate below $H/10$ |
| unchanged | the free volume excluded; the Krein norm with its ghosts; the tachyons of the extra times; the closed time-like curves; the neutrino sector | the same |

# What was verified

Every result labelled DERIVED rests on a computation in the folder `universe_model_4/code/` of the repository, which checks itself and writes a
report to `universe_model_4/reports/` (all equations and results are written out above). Each script is run with
`python universe_model_4/code/NAME.py` (Python 3 with numpy, scipy, sympy, mpmath and matplotlib, and CAMB for the cosmology), and no single
calculation runs longer than 423 seconds. The programs that this document cites, with their checks, all passed:

| program | checks | what they verify |
| ------ | ------ | ------ |
| `um4_geometry.py` | G1, G10, G11 | the proper chart (A-1); the static warps and their vacua; the matrices of FD-13 |
| `um4_gravity.py` | L1 to L4 | the choice of Einstein gravity |
| `um4_bulk.py` | B1, B2, B7, B10, B11 | the massless modes of the scalar and the gauge field, the boost invariance of dirac16complex, the continuum from zero mass and its spectral density (A-3), the ghost vectors of the graviton |
| `um4_propagators.py` | P1 to P5 | the propagators, Newton's and Coulomb's laws, the W and Z resonances, the bounds on $H$ |
| `um4_spectra.py` | U1 to U7 | the resonances of dirac16complex, their widths with the derived prefactor, their dispersion, the lifetime condition over the bindings (S-6), their Krein signature |
| `um4_fields.py` | F3 | the Krein operator and the signature of the charge |
| `um4_kohnsham.py` | K1 to K10 | the Kohn-Sham states of the gas (S-7, S-9), their equation of state, their width, the weakly bound point, how dilute the gas of the universe is |
| `um4_krein.py` | KR1 to KR9 | FE-67, the symmetries and the mirror of the states at the fold, the flat directions and the partner level of the gas, the selection rules at the fold, the occupation as a saddle, the pairs of the convective current |
| `um4_thermal.py` | T2 to T9 | the relic density, the portals and direct detection (S-21), the right-handed neutrinos, the ad hoc vacuum before nucleosynthesis, the unitarity bound and the strong binding (S-20), the binding by the Higgs portal (S-22) and by the gluon condensate (S-29) |
| `um4_foldsources.py` | FS3, FS4 | the induced gravity, the tuning of the tension (S-4) |
| `um4_cosmology.py` | C4, C5 | the CMB and the BAO with $w = -1$ |
| `um4_extratimes.py` | EX1 to EX5 | the fields with a momentum along the extra times (A-8) |
| `um4_causality.py` | C1 to C4 | no shortcut through the static bulk, the light cone of an expanding fold, the largest advance, the closed time-like curves |
| `um4_primordial.py` | PR0 to PR5 | the author's vacuum, the de Sitter fold, the inflation with frozen extra times, its scales (S-24), Higgs inflation (S-25), the fold factor |
| `um4_numass.py` | NM1 to NM5 | S-17, S-18, the capture rate S-28, and the comparison with NuFIT 6.0 |

All 189 checks of the 20 programs of UM-4 pass. The Kohn-Sham module runs in parts (`um4_kohnsham.py part NAME` for NAME = K1, I, K6, K9, then
`um4_kohnsham.py assemble`), so that no single calculation takes longer than 423 seconds.

# Further symbols

<!-- further symbols: Mred, hHiggs, GF, Pmns, Omega, betaD, epsLC, Nmat, Vsf, gbulk, hTT, nabla, g1, g2, g3, grho, kstar, ns, qhold, vA, vloc, Christoffel, KSorb, nocc, omegaSC, Tany, Wwarp, cb, deltaCP, nugen, rhob, wchi, Lfold -->
<!-- begin generated symbol list -->
**Further symbols.** These symbols appear in the definitions of the symbols listed after the equations of this document.

- $M_{\mathrm{red}}$: The reduced Planck mass, $M_{\mathrm{red}} = (8\pi G_{\mathrm{N}})^{-1/2}$. Unit: GeV. Value: $2.435\times10^{18}$ GeV. Status: STANDARD.
- $h$: The Higgs field: the fluctuation of the lower component of the Higgs doublet about $v$. Unit: GeV. Value: $m_h = 125.25$ GeV. Status: STANDARD.
- $G_{\mathrm{F}}$: The Fermi constant, $G_{\mathrm{F}} = 1/(\sqrt2\,v^2)$ in the Standard-Model vacuum (its measured value); in the equations of the neutrino flavours it stands for the local Fermi constant of the ad hoc vacuum. Unit: GeV$^{-2}$. Value: $1.1664\times10^{-5}$ GeV$^{-2}$. Status: STANDARD.
- $U_{\mathrm{PMNS}}$: The lepton mixing matrix (Pontecorvo-Maki-Nakagawa-Sakata) of the three Dirac neutrinos; its entries $(U_{\mathrm{PMNS}})_{\alpha i}$ connect the flavour state $\nu_\alpha$ with the mass state $\nu_i$. Unit: dimensionless. Value: $\theta_{12} = 33.40^\circ$, $\theta_{23} = 49.14^\circ$, $\theta_{13} = 8.54^\circ$ (NuFIT 5.2, November 2022, normal ordering, the fit without the Super-Kamiokande atmospheric data); the Dirac phase is set to zero (ASSUMED; the fit prefers $197^\circ$). Status: STANDARD, ASSUMED (the phase).
- $\Omega_M$: The spin connection acting on dirac16complex, $\Omega_M = \frac12\varpi_{Mab}\Sigma^{ab}$. Unit: 1/length. Status: RECORD.
- $\beta$: The matrix of the four-dimensional Dirac adjoint, $\beta = \hat\gamma^{(4)}$ (Hermitian, $\beta^2 = \mathbf{1}$). Unit: dimensionless. Status: STANDARD.
- $\epsilon^{IJK}$: The Levi-Civita symbol of three indices (the structure constants of $SU(2)$), $\epsilon^{123} = 1$. Unit: dimensionless. Status: STANDARD.
- $\mathcal{N}$: The one-body density matrix of dirac16complex, $\mathcal{N} = \sum_o\mathsf{n}_o\varphi_o\bar\varphi_o$ (a $16 \times 16$ matrix at each point). Unit: GeV$^7$. Status: DERIVED.
- $\mathsf{V}$: The rate of change of the scale factor $\mathrm{e}^{-a_4}b_4$ of the extra times on the fold in units of $H$, $\mathsf{V} = \mathsf{U} - \mathsf{A}$; zero with frozen extra times. Unit: dimensionless. Status: DERIVED.
- $\mathsf{g}_1,\ \mathsf{g}_2,\ \mathsf{g}_3$: The gauge couplings of eight dimensions of $U(1)_Y$, $SU(2)_L$ and $SU(3)_C$: the coefficients of the kinetic terms of the gauge fields of the bulk in their geometric normalisation; the four-dimensional couplings are $g_k^2 = 3H\mathsf{g}_k^2/(2V_*)$. Unit: GeV$^{-2}$ ($\mathsf{g}^2$: length$^4$). Status: ASSUMED.
- $\mathsf{h}_{ij}$: The transverse traceless perturbation of the metric of ordinary space by a gravitational wave as the four-dimensional world sees it: $\hat h_{ij} = \mathrm{e}^{2a_4}(\delta_{ij} + \mathsf{h}_{ij})$ ($i, j = 1, 2, 3$). Unit: dimensionless. Status: STANDARD.
- $\nabla$: The covariant derivative of a tensor with the Levi-Civita connection of the metric $g_{MN}$ (Christoffel symbols $\Gamma^P{}_{MN}$). Status: STANDARD.
- $g_1$: The $U(1)_Y$ gauge coupling of the four-dimensional world (usually $g'$; not normalised for grand unification): the coupling of the massless mode of the hypercharge field of the bulk, $g_1^2 = 3H\mathsf{g}_1^2/(2V_*)$. Unit: dimensionless. Value: $g_1(m_Z) = 0.3574$. Status: STANDARD.
- $g_2$: The $SU(2)_L$ gauge coupling of the four-dimensional world (usually $g$): the coupling of the massless mode of the $SU(2)_L$ field of the bulk, $g_2^2 = 3H\mathsf{g}_2^2/(2V_*)$. Unit: dimensionless. Value: $g_2(m_Z) = 0.6517$. Status: STANDARD.
- $g_3$: The $SU(3)_C$ gauge coupling of the four-dimensional world (the strong coupling $g_s$): the coupling of the massless mode of the gluon field of the bulk, $g_3^2 = 3H\mathsf{g}_3^2/(2V_*)$. Unit: dimensionless. Value: $g_3(m_Z) = 1.2177$ ($g_3^2/(4\pi) = 0.1180$). Status: STANDARD.
- $g_\rho$: The effective number of relativistic degrees of freedom of the energy density. Unit: dimensionless. Value: 106.75 in the Standard Model above the electroweak scale. Status: STANDARD.
- $k_*$: The pivot wave number of the primordial spectrum. Unit: GeV (1/length). Value: 0.05 Mpc$^{-1}$. Status: STANDARD.
- $n_{\mathrm{s}}$: The scalar density of dirac16complex in the Kohn-Sham state, $n_{\mathrm{s}} = \langle\bar\Psi\Psi\rangle = \mathrm{tr}\,\mathcal{N}$. Unit: GeV$^7$. Status: DERIVED.
- $q_{\mathrm{hold}}$: The pressure along the extra times that the fold fluid adds to its tension to hold the volume of the extra times fixed (four-dimensional normalisation). Unit: GeV$^4$. Value: $-(\rho - 3\mathcal{P})/2 - q_{\mathrm{SM}} - q_\chi - q_{\mathrm{P}}$: 0 for radiation, $-\rho/2$ for dust, $-\rho$ for a vacuum energy; today $-0.842\,\rho_{\mathrm{c}}^{(0)}$ if the baryons have no pressure along the extra times (ASSUMED). Status: DERIVED (the value), ASSUMED (that the fold fluid supplies it).
- $v_{\mathcal{A}}$: The amplitude of almightyAdHoc at $x_4 = 0$; the author's almightyAdHoc, $\mathrm{e}^{-2a_{40}x_4}$ (written Exp[-2 a40 x4] in his notebook), has $v_{\mathcal{A}} = 1$ in the units of his notebook. Unit: GeV. Value: 1 in the units of the author's notebook; UM-4 keeps it free (the examples take $v_{\mathcal{A}} = v$ and $10v$). Status: AUTHOR (the form), ASSUMED (a free amplitude).
- $v_{\mathrm{loc}}$: The local value of the electroweak vacuum, $v_{\mathrm{loc}}^2 = 2\langle\Phi^\dagger\Phi\rangle$: it sets the local masses of the quarks and leptons (each mass times $v_{\mathrm{loc}}/v$) and the local Fermi constant; $v_{\mathrm{loc}} = v$ in the Standard-Model vacuum. Unit: GeV. Value: $v$ in the late universe outside dense dirac16complex. Status: DERIVED.
- $\Gamma^P{}_{MN}$: The Christoffel symbols of the metric $g_{MN}$ (the Levi-Civita connection). Unit: 1/length. Status: STANDARD.
- $\varphi_o,\ \bar\varphi_o$: A Kohn-Sham orbital of dirac16complex (a single-particle solution of the Kohn-Sham equation: the Dirac equation of dirac16complex with the mean field of the gas added to its mass) and its Dirac adjoint. Unit: GeV$^{7/2}$. Status: RECORD.
- $\mathsf{n}_o$: The occupation of the Kohn-Sham orbital $o$ (between 0 and 1). Unit: dimensionless. Status: RECORD.
- $\varpi_{Mab}$: The canonical (Levi-Civita) spin connection of the vielbein, antisymmetric in $a, b$. Unit: 1/length. Status: STANDARD.
- $\mathcal{T}$: The energy-momentum tensor of any one term of the fold (in $\mathcal{T}^r{}_r = \mathcal{L}_{\mathrm{fold}}$). Unit: GeV$^4$. Status: STANDARD.
- $\mathcal{W}$: The warp factor: in a warped metric, the function of the position along one direction that multiplies the squared steps of other directions (its square root multiplies their lengths); in UM-4 the function of $\sigma$ that multiplies all seven directions of the fold, ordinary space, the time and the extra times, $\mathcal{W} = \mathrm{e}^{-2H\lvert\sigma\rvert} = (\sin^2z)^{1/6}$, equal to 1 on the fold. Unit: dimensionless. Status: DERIVED.
- $c_{\mathrm{b}}$: The speed coefficient of the particles $\chi$ of dirac16complex along ordinary space, in units of the speed of light on the fold: at small momentum $\omega^2 = \omega_0^2 + c_{\mathrm{b}}^2\vec k^2$. In UM-3, whose time was not warped, $c_{\mathrm{b}}^2 = 1.19$ for $H = 0.05\,m_\Psi$ and $q_{\mathrm{b}} = 0.3\,m_\Psi$ (faster than light); in UM-4 the boosts of the fold are a symmetry and $c_{\mathrm{b}} = 1$ exactly. Unit: dimensionless. Value: 1 in UM-4; 1.09 in UM-3. Status: DERIVED.
- $\delta_{\mathrm{CP}}$: The Dirac phase of the mixing matrix $U_{\mathrm{PMNS}}$. Unit: degree. Value: $212^\circ$ (NuFIT 6.0, normal ordering); 0 in the computations of UM-4. Status: STANDARD.
- $\nu_\alpha,\ \nu_i$: A neutrino field: $\nu_\alpha$ the flavour states (the flavour index runs over the electron, muon and tau flavours), $\nu_i$ the mass states ($i = 1, 2, 3$). Unit: GeV$^{3/2}$. Status: STANDARD.
- $\rho_{\mathrm{b}}$: The (rest-mass) energy density of the baryons: in a supernova the local density of the matter (quoted in g/cm$^3$), in cosmology the mean density of the baryons ($\rho_{\mathrm{b}}^{(0)}$ today). Unit: GeV$^4$. Status: STANDARD.
- $w_\chi$: The equation of state of the gas of the particles $\chi$: its pressure divided by its energy density, $w_\chi = P_{\mathrm{KS}}/(n_\chi\epsilon_{\mathrm{p}})$ (0 for cold dark matter, $-1$ for a vacuum energy). Unit: dimensionless. Status: DERIVED.
- $\mathcal{L}_{\mathrm{fold}}$: The Lagrangian of any one term of the fold (four-dimensional normalisation). Unit: GeV$^4$. Status: STANDARD.

<!-- end generated symbol list -->
