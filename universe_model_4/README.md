# universe_model_4 — UM-4, the model of 2026-10-25

On 2026-10-25 at 13:15 PDT the author ordered:

> "Since in the UM-3 model anything that propagates in the bulk outruns light on the fold, and bulk scalars and photons faster
> than light, my model is physically incorrect. You must find a new metric model in which x4 is warped like the other
> directions, both photons and gravitons actually propagate at c in the bulk, photon waves are transverse spin-1 phenomena,
> Gravitational waves (ripples in spacetime) are spin-2 phenomena (because they originate from the rank-2 stress-energy tensor)
> and possess the following Polarization Modes: the spin-2 nature of gravitational waves manifests physically as
> characteristic "plus" (+) and "cross" (×) polarization modes that stretch and squeeze space perpendicularly. Find the best
> model and re-calculate and re-document; however keep UM-3 and create a new UM-4, placed in new folders."

This folder is UM-4. UM-3 is kept unchanged in its own folder `universe_model_3` (as committed in `c5a93c4`); nothing in this
folder changes it. Every document of UM-4 is self-contained: every equation it uses is written out in it, and every symbol of
every display equation is defined right after the equation.

## The fold: definition and examples

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

## The answer to the order in brief

* **Why UM-3 was physically incorrect.** Its time `x4` was not warped, so the light cone of the bulk at the proper depth
  `sigma` was `e^(H |sigma|)` times wider than that of the fold: bulk scalars moved 1.22 times and bulk photons 1.41 times as fast
  as light on the fold at long wavelengths, and faster than light at every wavelength (DERIVED, `um4_bulk.py`, B9).
* **The metric of UM-4.** The author's metric with the time warped by the same factor `(sin^2 z)^(1/6)` as the other six
  directions of the fold (`z = 6 H x0`): in the proper coordinate the warp factor `e^(-2 H |sigma|)` multiplies the whole metric
  of the fold. Every slice of the bulk then has the light cone of the fold, and among the static warps of the author's form only
  equal rates in all seven directions give a vacuum of gravity with a cosmological constant (DERIVED, `um4_geometry.py`, G8 and
  G10). Its static block is a space of constant curvature `-H^2` in all eight directions.
* **The gravity.** The author's Einstein-Lovelock action with the weights of its Gauss-Bonnet and cubic terms set to zero:
  Einstein gravity in eight dimensions with the cosmological constant `Lambda = -21 H^2`, the only choice for which gravitons
  travel on the light cone on every background (DERIVED, `um4_gravity.py`, L1 to L4). The fold is a pure tension
  `kappa lambda_F = 12 H`, like the brane of Randall and Sundrum; the bulk needs no stabiliser.
* **Gravitons at the speed of light, spin 2, plus and cross.** The graviton of the bulk has a massless mode bound to the fold that
  travels at the speed of light at every depth and every wavelength; the four-dimensional world sees a transverse traceless wave
  of helicity +-2 with the two polarisations + and x, which stretch and squeeze a ring of test masses along perpendicular
  directions (DERIVED, `um4_bulk.py`, B4 and B5; `um4_foldsources.py`, FS2).
* **Photons at the speed of light, transverse, spin 1.** The gauge fields of the Standard Model live in the bulk (the photon by
  the order); their massless modes are bound to the fold and travel at the speed of light; the photon is a transverse wave of
  helicity +-1 (DERIVED, `um4_bulk.py`, B2 and B3).
* **Nothing outruns light on the fold.** Every massless field of the bulk travels at the speed of light, every massive mode and
  every state of dirac16complex is slower; no signal through the static bulk is faster than light along the fold, and around the
  expanding fold the largest advance over the Hubble distance today is `4.5e-94` of the travel time for `H = 2.5 TeV` (DERIVED,
  `um4_bulk.py`, B7 and B10; `um4_causality.py`, C1 to C3).
* **The price.** The W and Z bosons become resonances of the bulk, and the invisible width of the Z boson bounds `H > 2.5 TeV`;
  the states of dirac16complex at the fold become long-lived resonances (the particles chi, heavier than `2.4e6 GeV` if they are to
  live longer than the universe), which cannot be a thermal relic and cannot be bound by the author's Higgs portal alone; the
  dark energy is the excess of the tension of the fold, tuned to one part in `1e92` (DERIVED, ESTIMATE, OPEN).

## The documents

Each document is written in Markdown and built as LaTeX and PDF (`NAME.md`, `NAME.tex`, `NAME.pdf`).

| document | contents |
| --- | --- |
| `MODEL` | the summary of UM-4: the spacetime, the fields and where they live, the action term by term, the parameters |
| `FIELD_EQUATIONS` | the complete coupled field equations of UM-4 (the action IN-1 to IN-16, the field equations FE-1 to FE-88), each display followed by the definition of every symbol in it |
| `SOLUTION` | the approximate solution step by step (S-1 to S-28): gravity, the background, the volume of the extra times, the sources of the fold, the ad hoc Higgs vacuum, the propagation in the bulk, the resonances of dirac16complex, its Kohn-Sham states, the residuals, the neutrino flavours, the thermal history, the primordial era, the CMB, the CNB and the BAO |
| `PROPAGATION` | the answer to the order of 13:15 (P-1, P-2): why UM-3 was incorrect, the metric of UM-4 and why it is the best, the gravity, gravitons and photons at the speed of light with their spins and polarisations, every other field of the bulk, the propagators, the causal structure |
| `ANALYSIS` | the `x0` mass mechanism, dirac16complex as dark matter and as dark energy, the open questions answered, what the author may have left out, UM-4 compared with UM-3 (A-1 to A-8) |
| `PROVENANCE` | every input, every decision, every computation with its checks, the external data and software, how to reproduce |
| `dirac matrices` | the provenance of the author's eight real 16 x 16 Dirac matrices of `4+4.nb` |

## The programs and their checks

Each program in `code/` computes, checks itself, writes its results to `outputs/` and its checks to `reports/`, and exits with 0
only if every check passes; no single calculation runs longer than 423 seconds.

| program | checks | program | checks |
| --- | --- | --- | --- |
| `um4_dirac_matrices.py` | 55 | `um4_fields.py` | 16 |
| `um4_geometry.py` | 10 | `um4_spectra.py` | 8 |
| `um4_gravity.py` | 4 | `um4_kohnsham.py` (in parts) | 10 |
| `um4_bulk.py` | 10 | `um4_krein.py` | 7 |
| `um4_fold.py` | 6 | `um4_extratimes.py` | 5 |
| `um4_foldsources.py` | 5 | `um4_neutrino.py` | 5 |
| `um4_background.py` | 6 | `um4_flavour.py` | 4 |
| `um4_propagators.py` | 5 | `um4_numass.py` | 5 |
| `um4_causality.py` | 4 | `um4_thermal.py` | 8 |
| `um4_primordial.py` | 6 | `um4_cosmology.py` | 6 |

185 checks in 20 programs, all passing. The libraries `um4_common.py`, `um4_gammas.py` and `um4_lovelock.py` have no checks of
their own; `um4_dirac_matrices_doc.py` writes the document `dirac matrices`. The tools in `tools/` build the documents
(`build_docs.py`), keep the symbol lists (`symbols_tool.py`, `symbols_close.py`, `closure_check.py`, `inline_symbols.py`,
`make_inventory.py`), insert and check the one definition of the fold in every file that uses the word (`fold_block.py`) and read
the author's notebooks without Mathematica (`nb_reader.py`); `docs_src/` holds the registry of the symbols, the inventory of the
tagged equations and the two versions of the definition of the fold.

## How to reproduce

From the root of a clone of the repository (Python 3 with numpy, scipy, sympy, mpmath, matplotlib and CAMB 2.0.5; pandoc and
pdfTeX for the documents), each command under `timeout 423`:

```text
python universe_model_4/code/um4_dirac_matrices.py
python universe_model_4/code/um4_dirac_matrices_doc.py
python universe_model_4/code/um4_geometry.py
python universe_model_4/code/um4_gravity.py
python universe_model_4/code/um4_bulk.py
python universe_model_4/code/um4_fold.py
python universe_model_4/code/um4_foldsources.py
python universe_model_4/code/um4_background.py
python universe_model_4/code/um4_propagators.py
python universe_model_4/code/um4_causality.py
python universe_model_4/code/um4_fields.py
python universe_model_4/code/um4_spectra.py
python universe_model_4/code/um4_kohnsham.py part K1
python universe_model_4/code/um4_kohnsham.py part I
python universe_model_4/code/um4_kohnsham.py part K6
python universe_model_4/code/um4_kohnsham.py part K9
python universe_model_4/code/um4_kohnsham.py assemble
python universe_model_4/code/um4_krein.py
python universe_model_4/code/um4_extratimes.py
python universe_model_4/code/um4_neutrino.py
python universe_model_4/code/um4_flavour.py
python universe_model_4/code/um4_numass.py
python universe_model_4/code/um4_thermal.py
python universe_model_4/code/um4_primordial.py
python universe_model_4/code/um4_cosmology.py
python universe_model_4/docs_src/registry.py
python universe_model_4/tools/fold_block.py insert
python universe_model_4/tools/make_inventory.py
python universe_model_4/tools/symbols_tool.py sync
python universe_model_4/tools/symbols_tool.py check
python universe_model_4/tools/fold_block.py check
python universe_model_4/tools/build_docs.py
```

A part of `um4_kohnsham.py` that reaches its own limit of 400 seconds saves its state and exits with the code 3; it is then run
again until it exits with 0. `um4_cosmology.py` downloads the Planck 2018 plik-lite files once into `external/` (git-ignored, not
redistributed); the parts of the Kohn-Sham module are kept in `outputs/kohnsham_parts/` (git-ignored).

## Rules kept

* No single calculation longer than 423 seconds (the standing rule of 2026-10-14); every command runs under a time limit.
* The author's coordinates `x0, ..., x7` are never relabelled; the author's notebooks are never modified (UM-4 reads `4+4.nb`
  from `universe_model_3/author_inputs/`).
* The author's private inputs (prompt files, notes, the third-party paper, his scratch notebook and its `.mx` files, the files
  `Generalized_Kronecker_Delta.*`) are never committed; the Planck data are not redistributed.
* UM-3 and the frozen records before it (`Revision/`, `universe_model_2/`, `handoff/`, `provenance/`) are unchanged.

## Status

| part | state |
| --- | --- |
| metric, gravity, fold, propagation, causality, resonances of dirac16complex (`um4_geometry.py`, `um4_gravity.py`, `um4_fold.py`, `um4_bulk.py`, `um4_propagators.py`, `um4_causality.py`, `um4_spectra.py`) | DONE 2026-10-25 |
| the modules carried over from UM-3 and corrected for the warped time (`um4_fields.py`, `um4_neutrino.py`, `um4_flavour.py`, `um4_numass.py`, `um4_thermal.py`, `um4_cosmology.py`, `um4_dirac_matrices.py`) | DONE 2026-10-25 |
| background, sources of the fold, primordial era, extra times (`um4_background.py`, `um4_foldsources.py`, `um4_primordial.py`, `um4_extratimes.py`) | DONE 2026-10-25 |
| Kohn-Sham states and Krein norm (`um4_kohnsham.py` in four parts, `um4_krein.py`) | DONE 2026-10-25 |
| the documents `MODEL`, `FIELD_EQUATIONS`, `SOLUTION`, `PROPAGATION`, `ANALYSIS`, `PROVENANCE`, `dirac matrices` (.md, .tex, .pdf), the definition of the fold in every file | DONE 2026-10-25 |
