# universe_model_3 — UM-3, the revision of 2026-10-24

The author's order of 2026-10-24 ("This is a major new revision of this project") stopped every earlier stage
permanently (repository `HANDOFF.md`, section 0.14) and asked for a new folder holding all files of the revision. This
folder is that revision. Nothing in it refers to, or depends on, the earlier records (`Revision/`, `universe_model_2/`,
`provenance/`); its documents are self-contained.

## The fold: definition and examples

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

## The author's specification (2026-10-24)

* **Coordinates** (author, `Dirac_Einstein-Lovelock_4+4_Nash.nb`, Section DEFCHART):
  `X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}` — `x0` the hidden space-like direction, `x1, x2, x3` ordinary
  space, `x4` the time, `x5, x6, x7` the three extra (deflating) time-like directions. Never relabelled.
* **Dirac matrices** (author, `author_inputs/4+4.nb`): eight real 16 x 16 matrices `T16^A[0..7]` with
  `{T16^A[a], T16^A[b]} = 2 eta_ab I16`, `eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)`; chirality `T16^A[8]`, projectors
  `P_L = (I16 - T16^A[8])/2`, `P_R = (I16 + T16^A[8])/2`. Provenance: `dirac matrices.md` (also `.tex`, `.pdf`).
* **Metric of the primordial gravitational field** (author, new: `b4[x4] -> b4[x4]^2`; `b4` is a function of `x4`,
  never identically 1):

  ```text
  {{Cot[6 H x0]^2, 0, 0, 0, 0, 0, 0, 0},
   {0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0, 0, 0},
   {0, 0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0, 0},
   {0, 0, 0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0},
   {0, 0, 0, 0, -1, 0, 0, 0},
   {0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3), 0, 0},
   {0, 0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3), 0},
   {0, 0, 0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3)}}
  ```

  with `Sin[6 H x0]^(1/3) = (Sin[6 H x0]^2)^(1/6)`, the positive branch (the author's rule of 2026-10-16).
* **Fields**: Einstein-Lovelock gravity (couples to all fields); the Higgs doublet `Phi` with
  `V = mu^2 Phi^dagger Phi + lambda (Phi^dagger Phi)^2`, `lambda > 0`, `mu^2 < 0`, expanded about the ad hoc vacuum
  `Phi = (almightyAdHoc, v + h)/sqrt 2`, `almightyAdHoc = Exp[-2 a40 x4]`, `a40 > 0`, `x4 >= 0`; the three
  left-handed lepton doublets and the right-handed electron, muon and tau; the gauge fields `W1, W2, W3` of `SU(2)_L` and
  `B` of `U(1)_Y`; the three generations of quark doublets; the gluons of `SU(3)_C`; the dirac16complex quantised spinor
  field, coupled to gravity through the canonical spin connection (never identically zero) and, with its left-handed
  and its right-handed part separately, to every Standard-Model field with a unique coupling parameter each (only the
  left-handed part couples to the Higgs field); new phenomenological interactions consistent with QCD and the
  electroweak model.
* **Additions accepted by the author (2026-10-24 17:32)**: three right-handed neutrinos `nu_R` (one per generation), so
  that the neutrinos have Dirac masses and PMNS mixing; the right-handed quark singlets and the Yukawa couplings are
  included as listed in the notification of 17:20 (the author answered only on the neutrinos; the other defaults stand).
* **Why flavour conversion matters** (the author, 17:34): Gogilashvili & Tamborra, "Neutrino Flavor Conversion Shapes
  the Rate of Failed Core-collapse Supernovae", arXiv:2605.16504v3 (a third-party paper, not in the repository): flavour
  equipartition below a critical density turns 25.6% failed explosions into 50.8-96.4%. UM-3 therefore derives the
  complete neutrino flavour evolution (vacuum, matter, neutrino-neutrino forward scattering, the dirac16complex
  potential) from its action and solves it, the supernova environment included.
* **Tasks**: the complete coupled field equations; an accurate approximate solution with Kohn-Sham theory for
  dirac16complex; CMB, CNB, BAO (the metric as a power series of terms of decreasing magnitude); the `x0` mass mechanism
  (period `pi/(6H)`, the uncertainty relation) and the association of dark matter and dark energy with dirac16complex
  analysed; every equation written out and every symbol defined in every document; Markdown + LaTeX + PDF always.

## Status (newest last)

| part | files | state |
| --- | --- | --- |
| author inputs | `author_inputs/` | DONE: `4+4.nb` (read only, sha256 in `author_inputs/README.md`) and its cell listing |
| notebook reader | `tools/nb_reader.py` | DONE: reads every cell of a `.nb` file without Mathematica (also the author's other notebooks) |
| Dirac matrices provenance | `dirac matrices.md/.tex/.pdf`; `code/um3_gammas.py`, `code/um3_dirac_matrices.py` (55/55 checks), `code/um3_dirac_matrices_doc.py`, `tools/build_docs.py` | DONE 2026-10-24: the eight matrices of `4+4.nb` rebuilt cell by cell, equal to every stored output of the notebook and to every other source in the repository; real; Clifford relations; spin(4,4) basis, Spin_0(4,4) generated by the exponentials, Pin(4,4) with T_0 and T_4; chiral projectors re-derived |
| gravity sector of the new metric | `code/um3_geometry.py` (26/26), `code/um3_lovelock.py`, `code/um3_fold.py` (13/13), `code/um3_bulk.py` (10/10) | DONE 2026-10-24: exact curvature and Einstein-Lovelock tensors of the author's metric; the fold z = pi/2 and its junction conditions; bulk propagation speeds (why the Standard Model lives on the fold); graviton principal symbol |
| matter sector | `code/um3_fields.py` (16/16), `code/um3_spectra.py` (5/5), `code/um3_neutrino.py` (5/5) | DONE 2026-10-24: bilinears and Krein operator of dirac16complex, ad hoc Higgs vacuum, anomalies with nu_R; bound states of dirac16complex at the fold; neutrino flavour evolution (flavour blindness of the portals, local electroweak vacuum, MSW and Landau-Zener, fast-instability crossing criterion, the supernova equipartition map, CNB) |
| coupled field equations | `FIELD_EQUATIONS.md/.tex/.pdf` (74 pages, 78 tagged displays IN-1..IN-16, FE-1..FE-62, every symbol listed after every display; `tools/symbols_tool.py` check OK), `docs_src/` (registry, inventory) | DONE 2026-10-24 |
| the solution | `SOLUTION.md/.tex/.pdf` (77 pages, 80 displays); `code/um3_background.py` (6/6), `code/um3_series.py` (6/6), `code/um3_kohnsham.py` (9/9), `code/um3_flavour.py` (4/4), `code/um3_thermal.py` (6/6), `code/um3_cosmology.py` (6/6) | DONE 2026-10-25: the background and the static late-time block; the metric as a power series (the radion mode); the Higgs field in the ad hoc vacuum; the spectra along the hidden direction (the `x0` mass of the bound states); the self-consistent Kohn-Sham states of dirac16complex coupled to itself, to gravity and to every Standard-Model field, in three regimes up to `G_KS = 1`, and a weakly bound point; the residuals of every field equation; the neutrino flavours (Sun, supernova envelope, fast instability, equipartition); the thermal history and the portals (direct detection); CMB (Planck 2018), BAO (DESI DR2), CNB |
| model summary | `MODEL.md/.tex/.pdf` (16 pages) | DONE 2026-10-25: fields, couplings, parameters and their status |
| analysis | `ANALYSIS.md/.tex/.pdf` (18 pages, A-1..A-8) | DONE 2026-10-25: the `x0` mass mechanism (period `pi/(6H)`, the uncertainty relation), dark matter (the particles chi, cold) and dark energy (the vacuum energy, `w = -1`), what the author's order left out |
| provenance | `PROVENANCE.md/.tex/.pdf` | DONE 2026-10-25: every source, every author input, every check module |
| verification from a fresh clone | | DONE 2026-10-25: a fresh clone of commit 431d53d reproduces all 167 checks of the 13 modules (the Kohn-Sham module in 28 minutes on two cores, a single calculation over the 423 s limit, recorded in `claude_failures.md`, I2; the module has run in parts since), every stored output apart from the run times, the symbol check (191 displays, 0 problems) and the documents MODEL, FIELD_EQUATIONS, SOLUTION, ANALYSIS and PROVENANCE byte-identical (.md, .tex and .pdf); the Dirac-matrix provenance differs only in the run time it quotes |
| sources of the fold | `code/um3_foldsources.py` (6/6); FE-63 to FE-65 in `FIELD_EQUATIONS`, the chapter "The sources of the fold" (S-30) in `SOLUTION` | DONE 2026-10-25 (the order of 03:21): the Gauss-Bonnet and cubic Lovelock terms give the kink of the fold a graviton term of its own; with the bulk alone the four-dimensional gravitational wave would move with c_g^2 = 15/2 (2.74 times the speed of light), with the Lovelock term of the fold still with 83/82; with the induced Einstein-Hilbert term of the fold c_g^2 = (96 + 83 eps_r)/(96 + 82 eps_r), and GW170817 bounds eps_r below 1.344e-13; the gravity that the fields of the fold induce (Sakharov: N_ind = 4(1 - 6 xi_H) for the Standard Model with three nu_R, cutoff 3.75e19 GeV); the fold fluid, a tension plus a pressureless part fed by the bulk |
| open questions | `code/um3_krein.py` (7/7), `code/um3_extratimes.py` (5/5), `code/um3_superluminal.py` (5/5), `code/um3_primordial.py` (5/5), `code/um3_numass.py` (5/5); `ANALYSIS` "The open questions answered" (A-9 to A-15), `SOLUTION` S-31 to S-34, `FIELD_EQUATIONS` FE-67 | DONE 2026-10-25 (the order of 03:23): the Krein norm (the vacuum and the dilute gas are stable, the dense gas grows, the chiral couplings of the fold produce ghosts, so UM-3 with them is not unitary); fields that depend on the extra times (tachyonic; leaving them out is consistent but unstable; a gauge principle is needed); the speed of chi (group velocity at most 1.0045, front velocity 1, cosmological chi slow; loops require q_b/H > 4e10); the primordial era (n_S - 1 = 2.5 in the author's vacuum, so an inflationary era is needed, H_inf < 4.7e13 GeV; Higgs inflation is excluded by the induced gravity); the lightest neutrino mass and the Dirac phase (the phase drops out of every result; m_1 < 4.12 meV) |
| definition of the fold | `docs_src/fold_definition.md` (FD-1 to FD-10), `docs_src/fold_definition.txt`, `tools/fold_block.py` | DONE 2026-10-25 (the order of 03:54): one definition of the fold with its examples, inserted word for word into every file of UM-3 that uses the word (the documents, the READMEs, the program docstrings, the JSON outputs and reports) and verified by `tools/fold_block.py check`; the author's notebook `author_inputs/4+4.nb` (where `Fold[]` is a Mathematica function) is not modified |
| the stabiliser | `STABILISER.md/.tex/.pdf` (29 pages, SB-1 to SB-17), `code/um3_stabiliser.py` (8/8); FE-66 in `FIELD_EQUATIONS` and `SOLUTION` | DONE 2026-10-25 (the order of 05:09): the medium of the bulk that a static late-time bulk requires, found and named by Claude (Anthropic) on 2026-10-24, explained for a newcomer together with the static bulk, warp and warp factor and their examples; the five points of the order verified ([1] couples only to gravity: exact on the static bulk, not when the universe expands; [2] absent in the primordial era: true, its later creation OPEN; [3] the value DERIVED, the existence of a bulk source DERIVED, a separate medium ASSUMED); the two constraints of the bulk equations (the Friedmann equation of the bulk: the stabiliser is the zero point of the expansion); its importance for UM-3; its provenance |
| the Kohn-Sham module in parts | `code/um3_kohnsham.py` | DONE 2026-10-25: six checkpointed parts and `assemble`, every invocation under 423 s (the earlier unsplit runs are recorded in `claude_failures.md`, I1 to I3); the assembled outputs equal the record of 431d53d |
| documents of 2026-10-25 | `FIELD_EQUATIONS` (86 pages, 83 tagged displays IN-1 to IN-16 and FE-1 to FE-67), `SOLUTION` (93 pages, S-1 to S-34), `ANALYSIS` (32 pages, A-1 to A-15), `MODEL` (24 pages), `PROVENANCE` (15 pages), `STABILISER` | DONE 2026-10-25: the symbol check 307 displays, 0 problems; the definition of the fold verified in every file |
