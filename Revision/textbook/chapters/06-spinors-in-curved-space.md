## 6. Spinors in curved 4+4 space: vielbein, spin connection and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$

The two fields of the author, dirac16complex and dirac16complex00, have sixteen components at every point of spacetime. Chapters 4 and 5 built the eight gamma matrices that act on these components and the groups Pin(4,4) and Spin(4,4) that turn them. All of that was done in flat 4+4 space, where the eight directions are the same at every point. The author's universe is not flat: 3-space inflates, the three extra times deflate exponentially, and the hidden direction is warped. This chapter teaches, from zero, how a field with sixteen components is differentiated in such a curved space, and it computes exactly what gravity puts into the field equations of the author's two fields through the canonical spin connection. The answer is one $16 \times 16$ matrix, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$, and the chapter also proves precisely what this matrix does and does not mean.

### 6.1 What this chapter does

**The problem in plain words.** A spinor field $\Psi$ is a list of sixteen numbers at every point. The numbers are not measured in the coordinates $x_1, \dots, x_8$ directly: they are measured with respect to eight perpendicular unit directions chosen at each point, a **frame**. In flat space one frame serves everywhere. In a curved space the frame of one point and the frame of a neighbouring point are turned with respect to each other, so the plain derivative $\partial_\mu\Psi$ mixes two things: how the field really changes, and how the frame turns. The **spin connection** measures how the frame turns, and the **covariant derivative** $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ removes the turning. The field equation of both fields (Chapter 7 derives it) is

$$
\sum_\mu \gamma^\mu D_\mu\Psi = \big(m + U'(S)\big)\Psi ,
$$

and the spin connection enters it only through the one matrix $\sum_\mu\gamma^\mu\Omega_\mu$. The author asked that the field equations "always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime)" (quoted from `Revision/README.md`). This chapter computes the matrix exactly and examines the request line by line.

**What the chapter proves.**

- The author's metric has a diagonal vielbein (Section 6.2), 25 independent nonzero Christoffel symbols (Section 6.3) and a canonical spin connection with 12 independent nonzero components (Sections 6.4 to 6.6).
- The spinor connection $\Omega_\mu$ makes the curved gammas covariantly constant (Section 6.7), and in the diagonal vielbein $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$ for every $H > 0$ and every function $a_4(x_4)$: the terms along the time $x4$ of the three inflating directions and of the three deflating extra times cancel exactly, and the six terms along the hidden direction add up (Sections 6.8 and 6.9).
- A **negative control**: if the extra times inflated instead of deflating, a term $3a_4'\gamma^{(x4)}$ would survive; the cancellation is caused by the deflation (Section 6.10).
- The value $3H\gamma^{(x8)}$ belongs to the chosen frame: in another frame of the same metric the contraction is $\frac{6H - \beta}{2}(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)})$ and vanishes for $\beta = 6H$ (Sections 6.15 and 6.16), and a rescaling of the field removes it (Section 6.18). What no frame and no rescaling can remove is the curvature: $R^{x8}{}_{x8} = -6H^2$ for every $H > 0$ (Section 6.17).
- Why the record contracts the spin connection with both frame indices down: the author's notebook contracts the mixed components, which lacks a metric factor; that contraction deletes all 16 boost parts of the connection and would give $\frac{3H}{2}\gamma^{(x8)} + \frac{3a_4'}{2}\gamma^{(x4)}$ (Sections 6.23 and 6.24).

**The three worked examples.** Each is a complete Jupyter notebook; the chapter places each one where its theory has been explained, gives the complete instructions to run it, prints its complete text and then explains every line of its code.

| notebook | what it computes | figures | checks |
| --- | --- | --- | --- |
| 06a | vielbein, Christoffel symbols, spin connection, $\Omega_\mu$, the contraction $3H\gamma^{(x8)}$ direction by direction, the divergence form, the Dirac operator, the negative control, a warm-up in the plane | 10 | 34 |
| 06b | a boosted frame, local spin covariance, the Riemann and Ricci tensors, the spinor curvature, the rescaling | 6 | 26 |
| 06c | the mixed contraction of the author's notebook and what the missing metric factor changes | 6 | 27 |

All three reproduce the Revision record where they overlap with it; every such check prints a second line that names the record file and its check. Their last lines are ALL 34 CHECKS PASSED (notebook 06a), ALL 26 CHECKS PASSED (notebook 06b) and ALL 27 CHECKS PASSED (notebook 06c).

**Statuses.** Every statement carries one of the five labels of Chapter 0. **PROVED**: derived exactly here, line by line, and confirmed by an exact check of a notebook; where the Revision record proves the same, the record file and its check are named. **COMPUTED**: a number obtained by a notebook, with its accuracy. **ASSUMED**: the author's metric itself (the input of the theory), two standard theorems that are quoted and named where they are used, and the illustrative history $a_4 = x_4$ (with $H = 1$) used only in some plots, which is the prescribed background of Chapter 3 with slope $A = 1$. No HYPOTHESIS enters this chapter, and nothing in it is OPEN except the choice of boundary condition at the patch end, which Section 6.24 names and Chapter 14 treats. Nothing in this chapter concerns pairs of universes, their creation, or matter and antimatter; Chapters 18 to 21 treat those questions and state exactly what is and what is not proved about them.

**Notation.** The eight directions are named $x1, \dots, x8$ as in Chapter 5: $x1, x2, x3$ are 3-space (inflating), $x4$ is the time, $x5, x6, x7$ are the three extra times (time-like, deflating exponentially), $x8$ is the hidden direction. Inside formulas the coordinate values are written $x_1, \dots, x_8$, for example $z = 6Hx_8$ with $0 < z < \pi/2$. The letter $i$ stands for one of the 3-space directions $x1, x2, x3$ and the letter $t$ for one of the extra times $x5, x6, x7$ (except in the polar plane, where $i$ is the imaginary unit, and in Section 6.16, where $t$ is a component). The function $a_4$ depends on $x_4$ only; $a_4' = da_4/dx_4$ and $a_4'' = d^2a_4/dx_4^2$. The frame metric is

$$
\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)
$$

in the order $x1, \dots, x8$; $\eta_{aa}$ is its entry for the direction $a$, and $\eta^{aa} = \eta_{aa}$ because every entry is $\pm 1$. The constant gamma matrix of a direction carries the direction in parentheses, $\gamma^{(x4)}$; a gamma without parentheses, $\gamma^{x4}$ or $\gamma^\mu$, is a **curved gamma** (Section 6.2). Sums are written with $\sum$ as in Chapter 3. The one exception is the contraction $\gamma^\mu\Omega_\mu$: it always means $\sum_\mu\gamma^\mu\Omega_\mu$, and a single term is marked "(no sum)". Finally $s = \sin^{1/6}z$.

**The record files.** The Revision record files are named by their short names. The formula file `field-theory.json` lies in the folder `Revision/theory`. The reports `python-field-theory.json` and `wolfram-field-theory.json` (written by a sympy program and by a WolframScript program that share no code) and the two scope reports `python-scope.json` and `wolfram-scope.json` lie in the folder `Revision/theory/reports`. The **lead report** is the file `emt-divergence-and-spin-connection.json` in the folder `Revision/lead_checks/reports`, written by an independent program of the lead of the Revision work.

### 6.2 A frame at every point: the vielbein

**Why a spinor needs a frame.** The gamma matrices obey the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}1$ with the constant matrix $\eta$ (Chapter 4). In a curved space the metric $g_{\mu\nu}(x)$ changes from point to point and is not $\eta$. The way out is to describe every point by its own eight reference directions, perpendicular to each other and of unit length (unit duration for a time-like direction). Measured in such a frame the metric looks exactly like $\eta$, so the constant gammas of Chapter 4 can be used unchanged. The spinor components are always measured with respect to such a frame.

**Definition (vielbein).** A **vielbein** (German for "many legs") is an $8 \times 8$ matrix $e^a{}_\mu(x)$ at every point with

$$
g_{\mu\nu} = \sum_{a} \eta_{aa}\, e^a{}_\mu\, e^a{}_\nu \qquad \text{for all } \mu, \nu .
$$

The upper index $a$ is a **frame index**: it numbers the eight frame directions. The lower index $\mu$ is a **coordinate index**: it numbers the coordinates. Row $a$ of the matrix holds the components of the frame direction $a$ in the sense that a small coordinate step $dx^\mu$ has the frame components $dX^a = \sum_\mu e^a{}_\mu dx^\mu$, and then $ds^2 = \sum_{\mu,\nu} g_{\mu\nu}dx^\mu dx^\nu = \sum_a \eta_{aa}(dX^a)^2$: lengths in frame components are computed with $\eta$. The **inverse vielbein** $e_a{}^\mu$ is the inverse matrix, $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ (1 when $a = b$, 0 otherwise).

**The diagonal vielbein of the author's metric.** The author's metric is diagonal, $g_{\mu\mu} = \eta_{\mu\mu} f_\mu^2$ with the positive **vielbein factors** (Chapter 3 calls them scale factors $h_a$; they are the same numbers)

$$
f = \big(e^{a_4}s,\ e^{a_4}s,\ e^{a_4}s,\ 1,\ e^{-a_4}s,\ e^{-a_4}s,\ e^{-a_4}s,\ \cot z\big), \qquad s = \sin^{1/6}z .
$$

The diagonal matrix $e^a{}_\mu = f_a\,\delta^a_\mu$ is a vielbein: in the sum $\sum_a \eta_{aa}e^a{}_\mu e^a{}_\nu$ only $a = \mu = \nu$ survives, which gives $\eta_{\mu\mu}f_\mu^2 = g_{\mu\mu}$. For example, for $\mu = \nu = x1$,

$$
\eta_{11}f_1^2 = (+1)\big(e^{a_4}\sin^{1/6}z\big)^2 = e^{2a_4}\sin^{1/3}z
$$

(a power of a product is the product of the powers, and $(\sin^{1/6}z)^2 = \sin^{1/3}z$), which is the author's $g_{11}$; for $\mu = \nu = x5$, $\eta_{55}f_5^2 = (-1)e^{-2a_4}\sin^{1/3}z$, the author's $g_{55}$; for $x8$, $(+1)\cot^2 z = g_{88}$. The inverse vielbein is diagonal too, $e_a{}^\mu = \delta_a^\mu/f_a$. PROVED; `field-theory.json`, formulas `metric` and `vielbein_diagonal`; the lead report, check `vielbein_reproduces_metric`; Notebook 06a, In [7].

**The volume factor.** The determinant of a diagonal matrix is the product of its diagonal entries, so $\det g = \prod_\mu \eta_{\mu\mu}f_\mu^2 = (+1)^4(-1)^4\prod_\mu f_\mu^2$, and $\sqrt{\lvert\det g\rvert} = f_1 f_2\cdots f_8$. Line by line:

$$
f_1f_2f_3 = e^{3a_4}s^3, \qquad f_5f_6f_7 = e^{-3a_4}s^3
$$

(three equal factors; $e^{a_4}e^{a_4}e^{a_4} = e^{3a_4}$),

$$
f_1f_2f_3\,f_4\,f_5f_6f_7 = e^{3a_4}e^{-3a_4}s^6 \cdot 1 = s^6 = \sin z
$$

(the exponentials cancel, $e^{u}e^{-u} = 1$, and $(\sin^{1/6}z)^6 = \sin z$),

$$
\sqrt{\lvert\det g\rvert} = \sin z \cdot \cot z = \sin z\cdot\frac{\cos z}{\sin z} = \cos z
$$

(multiply by $f_8 = \cot z$ and cancel $\sin z$). The volume factor $\cos z$ does not depend on the time $x_4$: what 3-space gains, the extra times lose. PROVED; `python-field-theory.json`, check `sqrt_det_g_equals_cos_z`; `wolfram-field-theory.json`, check `sqrt_det_g_is_cos_z`; Notebook 06a, In [7]. This one fact will explain, in Section 6.9, why the function $a_4$ drops out of $\gamma^\mu\Omega_\mu$.

**Curved gammas.** With the constant frame gammas $\gamma^a$ define, for every coordinate $\mu$,

$$
\gamma^\mu = \sum_a e_a{}^\mu\,\gamma^a .
$$

They obey the **curved Clifford relation**. Line by line:

$$
\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = \sum_{a,b} e_a{}^\mu e_b{}^\nu\big(\gamma^a\gamma^b + \gamma^b\gamma^a\big)
$$

(insert the definition twice; numbers commute with matrices),

$$
= \sum_{a,b} e_a{}^\mu e_b{}^\nu\, 2\eta^{ab}\,1 = 2\sum_a \eta^{aa}\, e_a{}^\mu e_a{}^\nu\,1 = 2g^{\mu\nu}\,1
$$

(the Clifford relation; $\eta^{ab}$ is zero unless $a = b$; and $g^{\mu\nu} = \sum_a\eta^{aa}e_a{}^\mu e_a{}^\nu$ is the inverse metric, as one checks for the diagonal vielbein directly: $\eta^{\mu\mu}/f_\mu^2 = 1/g_{\mu\mu}$). For the diagonal vielbein the curved gammas are the frame gammas divided by the factors, $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ (no sum):

$$
\gamma^{x_i} = e^{-a_4}s^{-1}\gamma^{(x_i)},\qquad \gamma^{x4} = \gamma^{(x4)},\qquad \gamma^{x_t} = e^{a_4}s^{-1}\gamma^{(x_t)},\qquad \gamma^{x8} = \tan z\,\gamma^{(x8)} ,
$$

with $i = 1, 2, 3$, $t = 5, 6, 7$ and $1/\cot z = \tan z$.

**A vielbein is a choice.** Let $\Lambda(x)$ be an $8 \times 8$ matrix at every point with $\Lambda^T\eta\Lambda = \eta$ (an element of O(4,4), Chapter 5). Then $e'^a{}_\mu = \sum_c \Lambda^a{}_c\,e^c{}_\mu$ is another vielbein of the same metric. Line by line, in matrix form ($g = e^T\eta e$ is the definition written with matrices, $e$ having rows $a$ and columns $\mu$):

$$
e'^T\eta\,e' = (\Lambda e)^T\eta(\Lambda e) = e^T\big(\Lambda^T\eta\Lambda\big)e = e^T\eta\,e = g
$$

(the transpose of a product is the product of the transposes in reverse order; then the defining property of $\Lambda$). Such a point-dependent turning of the frame is a **local frame rotation** (a rotation, or a boost when it mixes a space-like with a time-like direction; Chapter 5). The diagonal vielbein is the simplest choice for the author's metric, but it is one choice among infinitely many. Sections 6.15 and 6.16 show that this freedom matters.

| statement | status | where it is verified |
| --- | --- | --- |
| $e^a{}_\mu = f_a\delta^a_\mu$ reproduces the author's metric | PROVED | `field-theory.json`, formulas `metric` and `vielbein_diagonal`; `python-field-theory.json`, check `metric_from_vielbein_equals_SPEC`; lead report, check `vielbein_reproduces_metric` |
| $\sqrt{\lvert\det g\rvert} = \cos z$, independent of $x_4$ | PROVED | `python-field-theory.json`, check `sqrt_det_g_equals_cos_z`; `wolfram-field-theory.json`, check `sqrt_det_g_is_cos_z` |
| curved Clifford relation; another frame $\Lambda e$ gives the same metric | PROVED (above) | Notebook 06b checks the second for a boost, In [7] |

### 6.3 The Christoffel symbols of the author's metric

**What they are.** Chapter 3 introduced the **Christoffel symbols**, the numbers that say how the coordinate directions change from point to point:

$$
\Gamma^\lambda{}_{\mu\nu} = \tfrac12\sum_\rho g^{\lambda\rho}\big(\partial_\mu g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}\big) .
$$

They are symmetric in the two lower indices, $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$ (exchange $\mu$ and $\nu$: the first two terms exchange places and the third is unchanged because $g$ is symmetric). They enter the **coordinate covariant derivative** of a vector field, $\nabla_\mu V^\nu = \partial_\mu V^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}V^\lambda$, the derivative that compares the vector at two points correctly although the coordinate directions change between them.

**A diagonal metric.** When $g$ is diagonal, so is its inverse, $g^{\lambda\rho} = \delta^{\lambda\rho}/g_{\lambda\lambda}$, and only $\rho = \lambda$ survives in the sum. With $g_{\lambda\lambda} = \eta_{\lambda\lambda}f_\lambda^2$ there are four cases, each derived from the formula with $\rho = \lambda$ (no sums below).

(a) All three indices equal, $\lambda = \mu = \nu$:

$$
\Gamma^\lambda{}_{\lambda\lambda} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\lambda g_{\lambda\lambda} + \partial_\lambda g_{\lambda\lambda} - \partial_\lambda g_{\lambda\lambda}\big) = \frac{\partial_\lambda g_{\lambda\lambda}}{2g_{\lambda\lambda}} = \frac{2\eta_{\lambda\lambda}f_\lambda\partial_\lambda f_\lambda}{2\eta_{\lambda\lambda}f_\lambda^2} = \partial_\lambda\ln f_\lambda
$$

(two of the three terms cancel; the derivative of $f^2$ is $2f\,\partial f$; and $\partial f/f = \partial\ln f$).

(b) The upper index equals one lower index, $\lambda = \mu \neq \nu$:

$$
\Gamma^\lambda{}_{\lambda\nu} = \frac{1}{2g_{\lambda\lambda}}\big(\partial_\lambda g_{\lambda\nu} + \partial_\nu g_{\lambda\lambda} - \partial_\lambda g_{\lambda\nu}\big) = \frac{\partial_\nu g_{\lambda\lambda}}{2g_{\lambda\lambda}} = \partial_\nu\ln f_\lambda
$$

($g_{\lambda\nu} = 0$ for $\lambda \neq \nu$; then the same steps as in (a)).

(c) The two lower indices equal, the upper one different, $\mu = \nu \neq \lambda$:

$$
\Gamma^\lambda{}_{\mu\mu} = \frac{1}{2g_{\lambda\lambda}}\big(0 + 0 - \partial_\lambda g_{\mu\mu}\big) = -\frac{\eta_{\mu\mu}\,2f_\mu\partial_\lambda f_\mu}{2\eta_{\lambda\lambda}f_\lambda^2} = -\eta_{\lambda\lambda}\eta_{\mu\mu}\,\frac{f_\mu\,\partial_\lambda f_\mu}{f_\lambda^2}
$$

(the off-diagonal entries $g_{\lambda\mu}$ vanish; $1/\eta_{\lambda\lambda} = \eta_{\lambda\lambda}$ because $\eta_{\lambda\lambda} = \pm1$).

(d) All three different: every term contains an off-diagonal entry of $g$, so $\Gamma^\lambda{}_{\mu\nu} = 0$.

**The derivatives of the factors.** The author's metric depends on $x_4$ (through $a_4$) and on $x_8$ (through $z = 6Hx_8$) only, so only $\partial_4$ and $\partial_8$ of the factors can be nonzero. With $\ln f_i = a_4 + \frac16\ln\sin z$ for $i = 1, 2, 3$, $\ln f_t = -a_4 + \frac16\ln\sin z$ for $t = 5, 6, 7$, $\ln f_4 = 0$ and $\ln f_8 = \ln\cos z - \ln\sin z$:

$$
\partial_4\ln f_i = a_4', \qquad \partial_4\ln f_t = -a_4', \qquad \partial_4\ln f_8 = 0
$$

(only $\pm a_4$ depends on $x_4$; its derivative is $\pm a_4'$),

$$
\partial_8\ln f_i = \partial_8\ln f_t = \frac16\cdot\frac{\cos z}{\sin z}\cdot 6H = H\cot z
$$

(the chain rule: the derivative of $\ln\sin z$ with respect to $z$ is $\cos z/\sin z$, and $dz/dx_8 = 6H$),

$$
\partial_8\ln f_8 = 6H\Big(\frac{-\sin z}{\cos z} - \frac{\cos z}{\sin z}\Big) = -6H\,\frac{\sin^2 z + \cos^2 z}{\sin z\cos z} = -\frac{6H}{\sin z\cos z}
$$

(the chain rule again; common denominator; $\sin^2 z + \cos^2 z = 1$).

**The 25 symbols.** Insert these into the four cases. From (a) and (b) with $\lambda = x_i$ and $\lambda = x_t$:

$$
\Gamma^{x_i}{}_{x_i\,x4} = a_4',\qquad \Gamma^{x_t}{}_{x_t\,x4} = -a_4',\qquad \Gamma^{x_i}{}_{x_i\,x8} = \Gamma^{x_t}{}_{x_t\,x8} = H\cot z ,
$$

and with $\lambda = x8$, case (a): $\Gamma^{x8}{}_{x8\,x8} = -6H/(\sin z\cos z) = -12H/\sin 2z$ (the double-angle formula $\sin 2z = 2\sin z\cos z$). From (c) with $\lambda = x4$ ($\eta_{44} = -1$, $f_4 = 1$):

$$
\Gamma^{x4}{}_{x_i\,x_i} = -(-1)(+1)f_i\,\partial_4 f_i = f_i^2\,a_4' = e^{2a_4}\sin^{1/3}z\;a_4',
$$

$$
\Gamma^{x4}{}_{x_t\,x_t} = -(-1)(-1)f_t\,\partial_4 f_t = f_t^2\,a_4' = e^{-2a_4}\sin^{1/3}z\;a_4'
$$

(for the extra times $\partial_4 f_t = -a_4'f_t$, and the three minus signs make a plus). From (c) with $\lambda = x8$ ($\eta_{88} = +1$, $f_8 = \cot z$):

$$
\Gamma^{x8}{}_{x_i\,x_i} = -\frac{f_i\,\partial_8 f_i}{\cot^2 z} = -\frac{f_i^2 H\cot z}{\cot^2 z} = -f_i^2 H\tan z, \qquad \Gamma^{x8}{}_{x_t\,x_t} = +f_t^2H\tan z
$$

($\partial_8 f_i = f_i H\cot z$; $\eta_{tt} = -1$ reverses the sign for the extra times). Every other symbol vanishes: $f_4 = 1$ and $f_8$ do not depend on $x_4$, and the factors depend on no other coordinate. Counting with $\mu \le \nu$: three each of the eight families $\Gamma^{x_i}{}_{x_i x4}$, $\Gamma^{x_i}{}_{x_i x8}$, $\Gamma^{x_t}{}_{x4 x_t}$, $\Gamma^{x_t}{}_{x_t x8}$, $\Gamma^{x4}{}_{x_ix_i}$, $\Gamma^{x4}{}_{x_tx_t}$, $\Gamma^{x8}{}_{x_ix_i}$, $\Gamma^{x8}{}_{x_tx_t}$, and one $\Gamma^{x8}{}_{x8x8}$: $8 \cdot 3 + 1 = 25$. Every nonzero symbol carries an index $x4$ or $x8$. In words: moving forward in time a 3-space direction grows at the rate $a_4'$ ($\Gamma^{x1}{}_{x1x4} = a_4'$) and an extra-time direction shrinks at the same rate ($\Gamma^{x5}{}_{x4x5} = -a_4'$).

| statement | status | where it is verified |
| --- | --- | --- |
| the 25 independent nonzero Christoffel symbols above | PROVED | `field-theory.json`, formula `christoffel_nonzero`; `wolfram-field-theory.json`, check `christoffel_count`; `python-field-theory.json`, check `christoffel_symmetric_metric_compatible`; Notebook 06a, In [9] |

### 6.4 The canonical spin connection: the vielbein postulate and its solution

**The problem.** A vector field $V$ has the coordinate components $V^\nu$ and the frame components $V^a = \sum_\nu e^a{}_\nu V^\nu$. The frame turns from point to point, so $\partial_\mu V^a$ mixes the change of $V$ with the turning of the frame, just as $\partial_\mu V^\nu$ mixed the change of $V$ with the bending of the coordinate lines. The cure is the same: a correction that is linear in $V$,

$$
\nabla_\mu V^a = \partial_\mu V^a + \sum_b \omega_\mu{}^a{}_b\,V^b ,
$$

with coefficients $\omega_\mu{}^a{}_b(x)$, the **spin connection**. It has one coordinate index $\mu$ (the direction of the step) and two frame indices $a$, $b$ (which frame direction turns towards which).

**The requirement.** The frame components of the covariant derivative must be the covariant derivative of the frame components: $\sum_\nu e^a{}_\nu\,\nabla_\mu V^\nu = \nabla_\mu V^a$ for every vector field $V$. Write both sides out. The left side is

$$
\sum_\nu e^a{}_\nu\Big(\partial_\mu V^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}V^\lambda\Big) .
$$

The right side is

$$
\partial_\mu\Big(\sum_\lambda e^a{}_\lambda V^\lambda\Big) + \sum_b\omega_\mu{}^a{}_b\sum_\lambda e^b{}_\lambda V^\lambda = \sum_\lambda\big(\partial_\mu e^a{}_\lambda\big)V^\lambda + \sum_\lambda e^a{}_\lambda\,\partial_\mu V^\lambda + \sum_{b,\lambda}\omega_\mu{}^a{}_b\,e^b{}_\lambda V^\lambda
$$

(the definition of $V^a$ and $V^b$; then the product rule). The terms with $\partial_\mu V$ are the same on both sides (rename $\nu$ as $\lambda$). Subtracting the left side from the right side leaves

$$
\sum_\lambda\Big(\partial_\mu e^a{}_\lambda - \sum_\nu\Gamma^\nu{}_{\mu\lambda}e^a{}_\nu + \sum_b\omega_\mu{}^a{}_b\,e^b{}_\lambda\Big)V^\lambda = 0
$$

(collect the coefficient of each $V^\lambda$). This must hold for every $V$, so every bracket vanishes. Renaming $\lambda$ as $\nu$ and the summed $\nu$ as $\lambda$, this is the **vielbein postulate**:

$$
\partial_\mu e^a{}_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}\,e^a{}_\lambda + \sum_b\omega_\mu{}^a{}_b\,e^b{}_\nu = 0 \qquad\text{for all } \mu, a, \nu .
$$

In eight dimensions these are $8 \cdot 8 \cdot 8 = 512$ equations.

**The solution.** Multiply the postulate by $e_c{}^\nu$ and sum over $\nu$. The last term becomes $\sum_b\omega_\mu{}^a{}_b\sum_\nu e^b{}_\nu e_c{}^\nu = \sum_b\omega_\mu{}^a{}_b\delta^b_c = \omega_\mu{}^a{}_c$ (the inverse vielbein), so

$$
\omega_\mu{}^a{}_c = \sum_{\nu,\lambda}e_c{}^\nu\,\Gamma^\lambda{}_{\mu\nu}\,e^a{}_\lambda - \sum_\nu e_c{}^\nu\,\partial_\mu e^a{}_\nu .
$$

Differentiate $\sum_\nu e^a{}_\nu e_c{}^\nu = \delta^a_c$ (a constant) with the product rule: $\sum_\nu e_c{}^\nu\partial_\mu e^a{}_\nu = -\sum_\nu e^a{}_\nu\partial_\mu e_c{}^\nu$. Inserting this and renaming the summation letters gives the formula that the Revision record and all three notebooks use:

$$
\omega_\mu{}^a{}_b = \sum_\nu e^a{}_\nu\Big(\partial_\mu e_b{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\,e_b{}^\lambda\Big) .
$$

The derivation shows that the postulate has this one solution and no other: it is the **canonical spin connection**. Its components $\omega_\mu{}^a{}_b$, with the first frame index up, are called the **mixed components**.

**Lowering the first index.** Define $\omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b$ (no sum). **Theorem: $\omega_{\mu ab} = -\omega_{\mu ba}$.** Proof, line by line. First, $\eta_{aa}e^a{}_\nu = \sum_\sigma g_{\nu\sigma}e_a{}^\sigma$: multiply $g_{\nu\sigma} = \sum_c\eta_{cc}e^c{}_\nu e^c{}_\sigma$ by $e_a{}^\sigma$ and sum over $\sigma$; only $c = a$ survives. So

$$
\omega_{\mu ab} = \sum_{\nu,\sigma}g_{\nu\sigma}\,e_a{}^\sigma\,\partial_\mu e_b{}^\nu + \sum_{\sigma,\lambda}e_a{}^\sigma\,\Gamma_{\sigma\mu\lambda}\,e_b{}^\lambda, \qquad \Gamma_{\sigma\mu\lambda} = \sum_\nu g_{\sigma\nu}\Gamma^\nu{}_{\mu\lambda}
$$

(insert into the formula; $\Gamma_{\sigma\mu\lambda}$ is the Christoffel symbol with its first index lowered, $\frac12(\partial_\mu g_{\sigma\lambda} + \partial_\lambda g_{\sigma\mu} - \partial_\sigma g_{\mu\lambda})$). Second, adding the two lowered symbols with the outer indices exchanged,

$$
\Gamma_{\sigma\mu\lambda} + \Gamma_{\lambda\mu\sigma} = \tfrac12\big(\partial_\mu g_{\sigma\lambda} + \partial_\lambda g_{\sigma\mu} - \partial_\sigma g_{\mu\lambda} + \partial_\mu g_{\lambda\sigma} + \partial_\sigma g_{\lambda\mu} - \partial_\lambda g_{\mu\sigma}\big) = \partial_\mu g_{\sigma\lambda}
$$

($g$ is symmetric, so the second and sixth terms cancel, the third and fifth cancel, and the first and fourth are equal). Third, add $\omega_{\mu ab}$ and $\omega_{\mu ba}$:

$$
\omega_{\mu ab} + \omega_{\mu ba} = \sum_{\nu,\sigma}g_{\nu\sigma}\big(e_a{}^\sigma\partial_\mu e_b{}^\nu + e_b{}^\sigma\partial_\mu e_a{}^\nu\big) + \sum_{\sigma,\lambda}e_a{}^\sigma e_b{}^\lambda\,\partial_\mu g_{\sigma\lambda} = \partial_\mu\Big(\sum_{\sigma,\lambda}g_{\sigma\lambda}e_a{}^\sigma e_b{}^\lambda\Big)
$$

(the second step: in the second $\Gamma$ term rename $\sigma \leftrightarrow \lambda$ and use the identity just shown; then the three terms are the three pieces of the product rule for $g\,e_a\,e_b$). Finally $\sum_{\sigma,\lambda}g_{\sigma\lambda}e_a{}^\sigma e_b{}^\lambda = \eta_{ab}$ (the frame directions are perpendicular and of unit length), a constant, whose derivative is zero. $\square$

So for each $\mu$ the lowered connection is an antisymmetric $8 \times 8$ array: its diagonal vanishes and it has $8 \cdot 7/2 = 28$ independent entries, one for each of the 28 generators $S^{ab}$ of Chapter 5. In words: $\omega_{\mu ab}$ is the rate at which the frame turns in the plane $(a, b)$ when one moves along $x^\mu$. The mixed components are not antisymmetric in general: $\omega_\mu{}^b{}_a = \eta_{bb}\omega_{\mu ba} = -\eta_{bb}\omega_{\mu ab} = -\eta_{aa}\eta_{bb}\,\omega_\mu{}^a{}_b$, which is antisymmetric for a pair of two space-like or two time-like directions and **symmetric** for a boost pair (Section 6.23 returns to this).

| statement | status | where it is verified |
| --- | --- | --- |
| the vielbein postulate has exactly the solution above | PROVED (above) | the postulate in all 512 components: `python-field-theory.json` and `wolfram-field-theory.json`, check `vielbein_postulate`; Notebook 06a, In [11] |
| $\omega_{\mu ab} = -\omega_{\mu ba}$ | PROVED (above) | `python-field-theory.json`, check `spin_connection_antisymmetric`; `wolfram-field-theory.json`, check `omega_antisymmetric`; Notebook 06a, In [11] |

### 6.5 A warm-up by hand: the flat plane in polar coordinates

Before eight dimensions, two. A point of the flat plane has the polar coordinates $r$ (distance from the centre) and $\varphi$ (angle). The metric is $ds^2 = dr^2 + r^2d\varphi^2$ (Chapter 3), so $g = \mathrm{diag}(1, r^2)$, $\eta = \mathrm{diag}(1, 1)$, and the factors are $f_r = 1$, $f_\varphi = r$: the unit radial direction (frame index 0) and the unit angular direction (frame index 1).

**Christoffel symbols.** Case (c) of Section 6.3 with $\lambda = r$, $\mu = \varphi$: $\Gamma^r{}_{\varphi\varphi} = -(1)(1)\,f_\varphi\partial_rf_\varphi/f_r^2 = -r\cdot 1 = -r$. Case (b): $\Gamma^\varphi{}_{\varphi r} = \partial_r\ln r = 1/r$. All others vanish.

**Spin connection.** The formula of Section 6.4 with $\mu = \varphi$, $a = 1$ (angular), $b = 0$ (radial), where $e^1{}_\varphi = r$ and $e_0{}^r = 1$ are the only entries needed:

$$
\omega_\varphi{}^1{}_0 = e^1{}_\varphi\big(\partial_\varphi e_0{}^\varphi + \Gamma^\varphi{}_{\varphi r}e_0{}^r\big) = r\Big(0 + \frac1r\cdot1\Big) = 1
$$

(only $\nu = \varphi$ has $e^1{}_\nu \neq 0$; $e_0{}^\varphi = 0$; only $\lambda = r$ has $e_0{}^\lambda \neq 0$). With $\eta = \mathrm{diag}(1, 1)$ lowering changes nothing: $\omega_{\varphi 10} = 1$ and, by the antisymmetry, $\omega_{\varphi 01} = -1$. For $\mu = r$ everything vanishes. **Meaning:** the radial and angular unit directions at the angle $\varphi$ are the Cartesian ones turned by the angle $\varphi$; moving in $\varphi$ turns the frame at one radian per radian, and the spin connection records this rate.

**Spinor connection.** Two $2 \times 2$ matrices with the Clifford relation of the plane are the Pauli matrices $\gamma^0 = \sigma_1 = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ and $\gamma^1 = \sigma_2 = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}$, with $\sigma_3 = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$; one checks by multiplying out that $\sigma_1\sigma_2 = i\sigma_3$ and $\sigma_2\sigma_3 = i\sigma_1$. The generator of the plane is $S^{01} = \frac14[\sigma_1, \sigma_2] = \frac12\sigma_1\sigma_2 = \frac i2\sigma_3$. Section 6.7 will show that the spinor connection is $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$, so

$$
\Omega_\varphi = \omega_{\varphi01}S^{01} = -\tfrac i2\,\sigma_3, \qquad \Omega_r = 0 .
$$

**The contraction.** The curved gammas are $\gamma^r = \sigma_1$ and $\gamma^\varphi = \sigma_2/r$, so

$$
\sum_\mu\gamma^\mu\Omega_\mu = \frac{\sigma_2}{r}\Big(-\frac i2\sigma_3\Big) = -\frac{i}{2r}\,\sigma_2\sigma_3 = -\frac{i}{2r}\,i\sigma_1 = \frac{\sigma_1}{2r}
$$

($i \cdot i = -1$). The Dirac operator of the flat plane in polar coordinates is therefore $\sigma_1(\partial_r + \frac{1}{2r}) + \frac{\sigma_2}{r}\partial_\varphi$: a term without derivative appears although the plane is flat.

**But the plane is flat, and the connection can be undone.** The **curvature of the spinor connection** is $F_{r\varphi} = \partial_r\Omega_\varphi - \partial_\varphi\Omega_r + \Omega_r\Omega_\varphi - \Omega_\varphi\Omega_r$; here $\Omega_\varphi$ is constant and $\Omega_r = 0$, so every term vanishes: $F_{r\varphi} = 0$. And with the spinor rotation $U(\varphi) = \cos\frac\varphi2 + i\sin\frac\varphi2\,\sigma_3$ (Chapter 5: a rotation by the angle $\varphi$ acts on spinors through the half angle),

$$
\partial_\varphi U = -\tfrac12\sin\tfrac\varphi2 + \tfrac i2\cos\tfrac\varphi2\,\sigma_3 = \tfrac i2\sigma_3\Big(\cos\tfrac\varphi2 + i\sin\tfrac\varphi2\,\sigma_3\Big) = \tfrac i2\sigma_3\,U
$$

(differentiate each entry; then factor out $\frac i2\sigma_3$, using $\sigma_3\sigma_3 = 1$ and $i \cdot i = -1$), so $-(\partial_\varphi U)U^{-1} = -\frac i2\sigma_3 = \Omega_\varphi$. In a flat space the spin connection is only the turning of the chosen frame, and a spinor rotation removes it. At $\varphi = 2\pi$ the frame is back where it started, but $U(2\pi) = \cos\pi = -1$: a spinor turns by half the angle, the double cover of Chapter 5. Notebook 06a checks all of this in In [5] and draws it in figure 1. PROVED (exact; the notebook's checks are its own, the plane is not a Revision record).

**Two lessons.** First, a nonzero spin connection, and even a nonzero $\sum_\mu\gamma^\mu\Omega_\mu$, does not mean that space is curved; it may only record how the chosen frame turns. Second, the test of curvature is $F_{\mu\nu}$, not $\Omega_\mu$. Both lessons return in Sections 6.16 and 6.17.

### 6.6 The spin connection of the author's metric: twelve components

**A diagonal vielbein, in general.** Let $e^a{}_\mu = f_a\delta^a_\mu$ and $e_b{}^\nu = \delta_b^\nu/f_b$. In the formula of Section 6.4 only $\nu = a$ survives in the outer sum and only $\lambda = b$ in the inner sum:

$$
\omega_\mu{}^a{}_b = f_a\Big(\partial_\mu\frac{\delta_b^a}{f_b} + \Gamma^a{}_{\mu b}\frac{1}{f_b}\Big) .
$$

For $a = b$ this is $f_a\big(-\partial_\mu f_a/f_a^2 + \Gamma^a{}_{\mu a}/f_a\big) = \Gamma^a{}_{\mu a} - \partial_\mu\ln f_a = 0$, by cases (a) and (b) of Section 6.3. For $a \neq b$ only the second term remains, $(f_a/f_b)\Gamma^a{}_{\mu b}$, and by case (d) it can be nonzero only when $\mu = a$ or $\mu = b$:

$$
\omega_a{}^a{}_b = \frac{f_a}{f_b}\,\partial_b\ln f_a = \frac{\partial_bf_a}{f_b}, \qquad \omega_b{}^a{}_b = \frac{f_a}{f_b}\Big(-\eta_{aa}\eta_{bb}\frac{f_b\,\partial_af_b}{f_a^2}\Big) = -\eta_{aa}\eta_{bb}\,\frac{\partial_af_b}{f_a}
$$

(no sums; case (b) with $\lambda = a$, $\nu = b$, and case (c) with $\lambda = a$, $\mu = b$). Lowering with $\eta_{aa}$ gives the two forms

$$
\omega_{a\,ab} = \eta_{aa}\,\frac{\partial_bf_a}{f_b}, \qquad \omega_{b\,ab} = -\eta_{bb}\,\frac{\partial_af_b}{f_a} \qquad (a \neq b,\ \text{no sum}) ,
$$

and the antisymmetry of Section 6.4 can be seen directly: the second form with the letters $a$ and $b$ exchanged reads $\omega_{a\,ba} = -\eta_{aa}\partial_bf_a/f_b = -\omega_{a\,ab}$. So: **in a diagonal vielbein, $\omega_{\mu ab}$ is nonzero only when $\mu$ is one of the two frame indices, and then $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\,\partial_bf_\mu/f_b$.**

**The author's metric.** The factors depend on $x_4$ and $x_8$ only, so $b$ must be $x4$ or $x8$. With $\partial_4f_i = a_4'f_i$, $\partial_4f_t = -a_4'f_t$, $\partial_8f_i = H\cot z\,f_i$, $\partial_8f_t = H\cot z\,f_t$ (Section 6.3), $f_4 = 1$ and $f_8 = \cot z$:

$$
\omega_{x_i\,x_i\,x4} = (+1)\frac{a_4'f_i}{1} = a_4'\,e^{a_4}s, \qquad \omega_{x_i\,x_i\,x8} = (+1)\frac{H\cot z\,f_i}{\cot z} = H\,e^{a_4}s ,
$$

$$
\omega_{x_t\,x_t\,x4} = (-1)\frac{-a_4'f_t}{1} = a_4'\,e^{-a_4}s, \qquad \omega_{x_t\,x_t\,x8} = (-1)\frac{H\cot z\,f_t}{\cot z} = -H\,e^{-a_4}s .
$$

The record lists the components with the smaller index first, $a < b$; for the extra times this is $\omega_{x_t\,x4\,x_t} = -\omega_{x_t\,x_t\,x4} = -a_4'\,e^{-a_4}s$. For $\mu = x4$ every candidate contains $\partial_bf_4 = 0$ (because $f_4 = 1$), and for $\mu = x8$ the only candidate, $b = x4$, contains $\partial_4f_8 = 0$ (because $\cot z$ does not depend on the time); so $\omega_{x4\,ab} = \omega_{x8\,ab} = 0$. Altogether there are $3 \cdot 2 + 3 \cdot 2 = 12$ independent nonzero components:

| $\mu$ | pair $(a, b)$ | $\omega_{\mu ab}$ | kind of pair |
| --- | --- | --- | --- |
| $x_i$ ($i = 1, 2, 3$) | $(x_i, x4)$ | $a_4'\,e^{a_4}s$ | boost (space-like with time-like) |
| $x_i$ | $(x_i, x8)$ | $H\,e^{a_4}s$ | rotation (two space-like) |
| $x_t$ ($t = 5, 6, 7$) | $(x4, x_t)$ | $-a_4'\,e^{-a_4}s$ | rotation (two time-like) |
| $x_t$ | $(x_t, x8)$ | $-H\,e^{-a_4}s$ | boost (time-like with space-like) |

Each component is $a_4'$ or $H$ times a factor $\pm e^{\pm a_4}\sin^{1/6}z$ that never vanishes for $0 < z < \pi/2$. So the part made by the time dependence (3-space inflating, the extra times deflating) vanishes only if $a_4$ is constant, and the part made by the hidden direction vanishes only if $H = 0$, which is not a metric of the family (the entries $\sin^{1/3}(6Hx_8)$ would vanish; record check `degenerate_at_H_0`). **For every admissible $H > 0$ the spin connection of the diagonal vielbein is nonzero.** Note also the signs: the extra time $x5$ has the opposite signs of the 3-space direction $x1$, because it shrinks while 3-space grows. Figure 06a.4 shows the arrays $\omega_{x1\,ab}$ and $\omega_{x5\,ab}$ at a sample point.

| statement | status | where it is verified |
| --- | --- | --- |
| exactly 12 independent nonzero $\omega_{\mu ab}$, with the values of the table | PROVED | `field-theory.json`, formula `omega_nonzero`; `wolfram-field-theory.json`, check `omega_components`; Notebook 06a, In [11] |
| each is $a_4'$ or $H$ times a nonvanishing factor; $\Omega_\mu = 0$ for all $\mu$ only if $a_4' = 0$ and $H = 0$ | PROVED | `wolfram-field-theory.json`, check `Omega_vanishes_iff_a4prime_and_H_vanish`; `python-field-theory.json`, check `nontriviality_Omega_zero_iff_flat` |

### 6.7 The spinor connection and the covariant derivative of a spinor

**What we want.** A spinor $\Psi$ has no coordinate index; its sixteen components are measured in the frame. Its covariant derivative must be of the form

$$
D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi
$$

with eight $16 \times 16$ matrices $\Omega_\mu(x)$, the **spinor connection**. Which matrices? The gamma matrices link spinors and vectors: $\gamma^\nu\Psi$ is again a spinor, but $\gamma^\nu$ carries the vector index $\nu$. The natural requirement is that the derivative treats the curved gammas as constants, as the flat derivative treats the constant gammas:

$$
D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0 ,
$$

where $[A, B] = AB - BA$ is the **commutator**. The first two terms are the coordinate covariant derivative of the vector index of $\gamma^\nu$, the commutator is the spinor connection acting on the matrix from the left and from the right. With this requirement the product rule holds in the form $D_\mu(\gamma^\nu\Psi) = \gamma^\nu D_\mu\Psi$, so the field equation $\sum_\mu\gamma^\mu D_\mu\Psi = (m + U')\Psi$ does not depend on where the derivative is written.

**The requirement in frame form.** Insert $\gamma^\nu = \sum_a e_a{}^\nu\gamma^a$ (the frame gammas are constant):

$$
D_\mu\gamma^\nu = \sum_a\Big(\partial_\mu e_a{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}e_a{}^\lambda\Big)\gamma^a + \sum_a e_a{}^\nu[\Omega_\mu, \gamma^a]
$$

(the product rule; numbers commute with matrices). Multiply the formula of Section 6.4 by $e_c{}^\sigma$ and sum over $c$: since $\sum_c e_c{}^\sigma e^c{}_\nu = \delta^\sigma_\nu$, this gives $\partial_\mu e_b{}^\sigma + \sum_\lambda\Gamma^\sigma{}_{\mu\lambda}e_b{}^\lambda = \sum_c e_c{}^\sigma\,\omega_\mu{}^c{}_b$. With it the first sum becomes $\sum_{a,c}e_c{}^\nu\omega_\mu{}^c{}_a\gamma^a$, and

$$
D_\mu\gamma^\nu = \sum_c e_c{}^\nu\Big([\Omega_\mu, \gamma^c] + \sum_a\omega_\mu{}^c{}_a\gamma^a\Big)
$$

(rename $a$ as $c$ in the second sum). The inverse vielbein is invertible, so $D_\mu\gamma^\nu = 0$ for all $\nu$ holds exactly when

$$
[\Omega_\mu, \gamma^c] = -\sum_b\omega_\mu{}^c{}_b\,\gamma^b \qquad\text{for all } \mu, c .
$$

This is the **defining property** of the spinor connection: commuting with $\Omega_\mu$ turns the gammas exactly as $\omega_\mu$ turns the frame.

**The solution.** **Theorem.** $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$, with the generators $S^{ab} = \frac14[\gamma^a, \gamma^b]$ of Chapter 5, has the defining property. Proof, line by line. Chapter 5 proved the **vector rule** $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$. So

$$
[\Omega_\mu, \gamma^c] = \tfrac12\sum_{a,b}\omega_{\mu ab}\big(\eta^{bc}\gamma^a - \eta^{ac}\gamma^b\big) = \tfrac12\,\eta^{cc}\sum_a\omega_{\mu ac}\gamma^a - \tfrac12\,\eta^{cc}\sum_b\omega_{\mu cb}\gamma^b
$$

(a commutator is linear in each argument; $\eta^{bc}$ is nonzero only for $b = c$, $\eta^{ac}$ only for $a = c$). By the antisymmetry $\omega_{\mu ac} = -\omega_{\mu ca}$ the first sum is $-\frac12\eta^{cc}\sum_a\omega_{\mu ca}\gamma^a$, the same as the second (rename $a$ as $b$). Hence

$$
[\Omega_\mu, \gamma^c] = -\eta^{cc}\sum_b\omega_{\mu cb}\gamma^b = -\sum_b\omega_\mu{}^c{}_b\gamma^b
$$

(two equal halves; and $\eta^{cc}\omega_{\mu cb} = \eta_{cc}\eta_{cc}\omega_\mu{}^c{}_b = \omega_\mu{}^c{}_b$ because $\eta_{cc}^2 = 1$). $\square$

**Uniqueness.** If $\Omega'_\mu$ also had the defining property, the difference $\Omega'_\mu - \Omega_\mu$ would commute with all eight gammas, and Chapter 5 proved that only multiples of the identity do (the commutant of Pin(4,4) is one-dimensional). Every $S^{ab}$ has trace 0 (it is a multiple of a commutator, and $\mathrm{tr}(AB) = \mathrm{tr}(BA)$), so $\Omega_\mu$ is the only solution with trace 0. A multiple of the identity would be an extra field of the electromagnetic kind, not part of gravity; the canonical connection has none.

**Summing over $a < b$.** Both $\omega_{\mu ab}$ and $S^{ab}$ change sign when $a$ and $b$ are exchanged, so the terms $(a, b)$ and $(b, a)$ are equal, the terms $a = b$ vanish, and

$$
\Omega_\mu = \tfrac12\sum_{a,b}\omega_{\mu ab}S^{ab} = \sum_{a<b}\omega_{\mu ab}S^{ab}, \qquad S^{ab} = \tfrac12\gamma^a\gamma^b \ (a \neq b)
$$

(for $a \neq b$ the two gammas anticommute, so $\gamma^a\gamma^b - \gamma^b\gamma^a = 2\gamma^a\gamma^b$).

**The derivative of the Dirac adjoint.** The Dirac adjoint is $\bar\Psi = \Psi^\dagger C$ (Chapter 5), and its covariant derivative is $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\,\Omega_\mu$; with this sign the number $\bar\Psi\Phi$ obeys the ordinary product rule, $(D_\mu\bar\Psi)\Phi + \bar\Psi D_\mu\Phi = \partial_\mu(\bar\Psi\Phi)$, because the two $\Omega_\mu$ terms cancel. It agrees with the conjugate of $D_\mu\Psi$: $\Omega_\mu$ is real and Chapter 5 proved $(S^{ab})^TC = -CS^{ab}$, so $(D_\mu\Psi)^\dagger C = \partial_\mu\Psi^\dagger C + \Psi^\dagger\Omega_\mu^TC = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$.

**The author's metric.** With the table of Section 6.6 and $S^{ab} = \frac12\gamma^a\gamma^b$:

$$
\Omega_{x_i} = e^{a_4}s\big(a_4'\,S^{x_i\,x4} + H\,S^{x_i\,x8}\big), \qquad \Omega_{x_t} = -e^{-a_4}s\big(a_4'\,S^{x4\,x_t} + H\,S^{x_t\,x8}\big), \qquad \Omega_{x4} = \Omega_{x8} = 0 .
$$

No frame direction turns when one moves along the time or along the hidden direction. Each nonzero $\Omega_\mu$ is a combination of two generators. A boost generator is a **symmetric** matrix and a rotation generator an **antisymmetric** one: the transpose of a product reverses the order, and the author's gammas satisfy $(\gamma^a)^T = \eta_{aa}\gamma^a$ (Chapter 5), so

$$
(\gamma^a\gamma^b)^T = (\gamma^b)^T(\gamma^a)^T = \eta_{aa}\eta_{bb}\,\gamma^b\gamma^a = -\eta_{aa}\eta_{bb}\,\gamma^a\gamma^b \qquad (a \neq b) ,
$$

which is $+\gamma^a\gamma^b$ for a boost pair ($\eta_{aa}\eta_{bb} = -1$, 16 pairs) and $-\gamma^a\gamma^b$ for a rotation pair (12 pairs). In $\Omega_{x1}$ the $a_4'$ part is a boost ($x1$ with $x4$) and the $H$ part a rotation ($x1$ with $x8$); in $\Omega_{x5}$ it is the other way round. Figure 06a.5 shows both matrices.

**The covariant constancy, checked.** With these $\Omega_\mu$ the defining property holds for all 64 pairs $(\mu, c)$ and $D_\mu\gamma^\nu = 0$ for all 64 pairs $(\mu, \nu)$ (Notebook 06a, In [13]).

| statement | status | where it is verified |
| --- | --- | --- |
| $\Omega_{x_i}$, $\Omega_{x_t}$ as above; $\Omega_{x4} = \Omega_{x8} = 0$ | PROVED | `field-theory.json`, formula `Omega_components`; `python-field-theory.json`, check `Omega_x4_and_Omega_x8_vanish`; `wolfram-field-theory.json`, check `Omega_components` |
| the defining property for all 64 pairs | PROVED | `wolfram-field-theory.json`, check `S_rotates_gamma_with_omega` |
| $D_\mu\gamma^\nu = 0$ for all 64 pairs | PROVED | `python-field-theory.json`, check `covariant_constancy_D_mu_gamma_nu`; `wolfram-field-theory.json`, check `gamma_covariantly_constant` |
| uniqueness up to a multiple of $1$ | PROVED (above, with the commutant of Chapter 5) | `python-algebra.json`, check `pin_commutant_dimension_1` (in `Revision/algebra/reports`) |

### 6.8 The contraction $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$, direction by direction

The field equation contains $\sum_\mu\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu\partial_\mu\Psi + \big(\sum_\mu\gamma^\mu\Omega_\mu\big)\Psi$, so the spin connection enters it only through the one $16 \times 16$ matrix $\sum_\mu\gamma^\mu\Omega_\mu$. We compute it one direction at a time.

**A 3-space direction**, $\mu = x1$ (the same for $x2$ and $x3$). With $\gamma^{x1} = \gamma^{(x1)}/f_1$ and $f_1 = e^{a_4}s$:

$$
\gamma^{x1}\Omega_{x1} = \frac{\gamma^{(x1)}}{f_1}\,f_1\Big(a_4'\,\tfrac12\gamma^{(x1)}\gamma^{(x4)} + H\,\tfrac12\gamma^{(x1)}\gamma^{(x8)}\Big)
$$

(the formulas of Sections 6.2 and 6.7),

$$
= \tfrac12 a_4'\,\gamma^{(x1)}\gamma^{(x1)}\gamma^{(x4)} + \tfrac12 H\,\gamma^{(x1)}\gamma^{(x1)}\gamma^{(x8)} = \tfrac12 a_4'\,\gamma^{(x4)} + \tfrac12 H\,\gamma^{(x8)}
$$

(the factor $f_1$ cancels; $\gamma^{(x1)}\gamma^{(x1)} = \eta_{11}1 = +1$ by the Clifford relation).

**An extra time**, $\mu = x5$ (the same for $x6$ and $x7$). With $\gamma^{x5} = \gamma^{(x5)}/f_5$:

$$
\gamma^{x5}\Omega_{x5} = \frac{\gamma^{(x5)}}{f_5}\,(-f_5)\Big(a_4'\,\tfrac12\gamma^{(x4)}\gamma^{(x5)} + H\,\tfrac12\gamma^{(x5)}\gamma^{(x8)}\Big) = -\tfrac12 a_4'\,\gamma^{(x5)}\gamma^{(x4)}\gamma^{(x5)} - \tfrac12 H\,\gamma^{(x5)}\gamma^{(x5)}\gamma^{(x8)}
$$

(the factor $f_5$ cancels and leaves the sign). Now $\gamma^{(x5)}\gamma^{(x4)}\gamma^{(x5)} = -\gamma^{(x4)}\gamma^{(x5)}\gamma^{(x5)} = -\gamma^{(x4)}(-1) = \gamma^{(x4)}$ (two different gammas anticommute; $\gamma^{(x5)}\gamma^{(x5)} = \eta_{55}1 = -1$), and $\gamma^{(x5)}\gamma^{(x5)}\gamma^{(x8)} = -\gamma^{(x8)}$. Hence

$$
\gamma^{x5}\Omega_{x5} = -\tfrac12 a_4'\,\gamma^{(x4)} + \tfrac12 H\,\gamma^{(x8)} .
$$

**The time and the hidden direction.** $\Omega_{x4} = \Omega_{x8} = 0$, so $\gamma^{x4}\Omega_{x4} = \gamma^{x8}\Omega_{x8} = 0$.

**The sum.** Writing each term as $\alpha_\mu\gamma^{(x4)} + \beta_\mu\gamma^{(x8)}$:

| direction $\mu$ | $\alpha_\mu$ (coefficient of $\gamma^{(x4)}$) | $\beta_\mu$ (coefficient of $\gamma^{(x8)}$) |
| --- | --- | --- |
| $x1$, $x2$, $x3$ (inflating) | $+\frac12 a_4'$ each | $\frac12 H$ each |
| $x4$ (time) | $0$ | $0$ |
| $x5$, $x6$, $x7$ (deflating) | $-\frac12 a_4'$ each | $\frac12 H$ each |
| $x8$ (hidden) | $0$ | $0$ |
| total | $\frac32 a_4' - \frac32 a_4' = 0$ | $6 \cdot \frac12 H = 3H$ |

$$
\sum_\mu\gamma^\mu\Omega_\mu = 3H\,\gamma^{(x8)} .
$$

**In words.** Along the time direction the inflating 3-space and the deflating extra times push with equal and opposite strength, and their contributions cancel exactly, for every function $a_4(x_4)$. Along the hidden direction all six warped directions push the same way, and their contributions add. The result is a constant matrix: it contains neither $a_4$ nor $x_4$ nor $x_8$.

**Reading off the coefficients with traces.** Notebook 06a finds $\alpha_\mu$ and $\beta_\mu$ with traces (the **trace** of a square matrix is the sum of its diagonal entries). For two different gammas $\mathrm{tr}(\gamma^a\gamma^b) = 0$, while $\mathrm{tr}(\gamma^{(x4)}\gamma^{(x4)}) = \mathrm{tr}(-1) = -16$ and $\mathrm{tr}(\gamma^{(x8)}\gamma^{(x8)}) = +16$ (Chapter 4). So for $M = \alpha\gamma^{(x4)} + \beta\gamma^{(x8)}$:

$$
\mathrm{tr}(M\gamma^{(x4)}) = \alpha(-16) + \beta\cdot 0, \qquad \mathrm{tr}(M\gamma^{(x8)}) = \alpha\cdot0 + \beta\cdot16 ,
$$

hence $\alpha = -\mathrm{tr}(M\gamma^{(x4)})/16$ and $\beta = \mathrm{tr}(M\gamma^{(x8)})/16$. The notebook then checks that $M - \alpha\gamma^{(x4)} - \beta\gamma^{(x8)}$ is the zero matrix, so that nothing else is hidden in $M$.

| statement | status | where it is verified |
| --- | --- | --- |
| the eight terms $\gamma^\mu\Omega_\mu$ (no sum) of the table | PROVED | `field-theory.json`, formula `gammaOmega_per_direction`; `wolfram-field-theory.json`, check `gammaOmega_x4_terms_cancel`; `python-field-theory.json`, check `time_terms_cancel_hidden_term_survives` |
| $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$ for every $H > 0$ and every $a_4$ | PROVED | `field-theory.json`, formula `gammaOmega_total`; `wolfram-field-theory.json`, check `gammaOmega_equals_3H_gamma_x8`; `python-field-theory.json`, check `gamma_mu_Omega_mu_equals_3H_gamma_x8`; lead report, check `gamma_Omega_equals_3H_gamma8`; Notebook 06a, In [15] |

### 6.9 Why $a_4$ drops out: the divergence form

The cancellation of Section 6.8 is not an accident. Two facts explain it without computing $\Omega_\mu$ at all.

**Fact 1: for each $\mu$ separately, $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum).** In the diagonal vielbein $\Omega_\mu$ contains only generators $S^{(\mu)b}$ with $b \neq \mu$ (Section 6.6), and $\gamma^\mu$ is a multiple of $\gamma^{(\mu)}$. For one such generator:

$$
\gamma^{(\mu)}\,\tfrac12\gamma^{(\mu)}\gamma^{(b)} = \tfrac12\eta_{\mu\mu}\gamma^{(b)}, \qquad \tfrac12\gamma^{(\mu)}\gamma^{(b)}\,\gamma^{(\mu)} = -\tfrac12\gamma^{(\mu)}\gamma^{(\mu)}\gamma^{(b)} = -\tfrac12\eta_{\mu\mu}\gamma^{(b)}
$$

(the Clifford relation; in the second product the two different gammas $\gamma^{(b)}$ and $\gamma^{(\mu)}$ are exchanged at the cost of a sign). The two products are opposite, so they anticommute, and so do the combinations.

**The divergence form.** Take the covariant constancy $D_\mu\gamma^\nu = 0$ of Section 6.7, put $\nu = \mu$ and sum over $\mu$:

$$
\sum_\mu\partial_\mu\gamma^\mu + \sum_{\mu,\lambda}\Gamma^\mu{}_{\mu\lambda}\gamma^\lambda + \sum_\mu\big(\Omega_\mu\gamma^\mu - \gamma^\mu\Omega_\mu\big) = 0 .
$$

The contracted Christoffel symbol of a diagonal metric is $\sum_\mu\Gamma^\mu{}_{\mu\lambda} = \sum_\mu\partial_\lambda\ln f_\mu = \partial_\lambda\ln\big(\prod_\mu f_\mu\big) = \partial_\lambda\ln\sqrt{\lvert g\rvert}$ (cases (a) and (b) of Section 6.3; the logarithm of a product is the sum of the logarithms; Section 6.2). So the first two sums are

$$
\sum_\lambda\Big(\partial_\lambda\gamma^\lambda + \frac{\partial_\lambda\sqrt{\lvert g\rvert}}{\sqrt{\lvert g\rvert}}\gamma^\lambda\Big) = \frac{1}{\sqrt{\lvert g\rvert}}\sum_\lambda\partial_\lambda\big(\sqrt{\lvert g\rvert}\,\gamma^\lambda\big)
$$

(the product rule read backwards). By Fact 1, $\Omega_\mu\gamma^\mu = -\gamma^\mu\Omega_\mu$, so the third sum is $-2\sum_\mu\gamma^\mu\Omega_\mu$. Solving for the contraction:

$$
\sum_\mu\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu\big(\sqrt{\lvert g\rvert}\,\gamma^\mu\big) .
$$

The right side is built from the volume factor and the vielbein alone.

**Fact 2: the product structure.** For the diagonal vielbein $\sqrt{\lvert g\rvert}\,\gamma^\mu = \big(\prod_c f_c\big)\gamma^{(\mu)}/f_\mu = \big(\prod_{c\neq\mu}f_c\big)\gamma^{(\mu)}$ (no sum over $\mu$). The term $\partial_\mu$ of this product can be nonzero only if the product depends on its own coordinate $x_\mu$, that is only for $\mu = x4$ or $\mu = x8$. For the time:

$$
\prod_{c\neq x4}f_c = e^{3a_4}s^3\cdot e^{-3a_4}s^3\cdot\cot z = \sin z\cot z = \cos z
$$

(Section 6.2): it does not depend on $x_4$, so **the time direction contributes nothing**. This is the deeper reason for the cancellation of Section 6.8: the 7-volume of a slice does not change with time. For the hidden direction:

$$
\prod_{c\neq x8}f_c = e^{3a_4}s^3\cdot1\cdot e^{-3a_4}s^3 = s^6 = \sin z, \qquad \frac{1}{2\cos z}\,\partial_8\sin z\;\gamma^{(x8)} = \frac{6H\cos z}{2\cos z}\gamma^{(x8)} = 3H\,\gamma^{(x8)}
$$

(the chain rule with $dz/dx_8 = 6H$; then cancel $\cos z$). So the divergence form gives $3H\gamma^{(x8)}$ again, by a second and much shorter route. Notebook 06a checks Fact 1 for every $\mu$, the divergence form and the eight products (In [18]), and once more with a calculator's method, a central difference (In [19]).

| statement | status | where it is verified |
| --- | --- | --- |
| $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ | PROVED | `python-field-theory.json`, check `anticommutator_gamma_Omega_vanishes` |
| the divergence form equals $3H\gamma^{(x8)}$ | PROVED | `python-field-theory.json`, check `divergence_of_sqrtg_gamma`; `wolfram-field-theory.json`, check `gammaOmega_divergence_form`; lead report, check `gamma_Omega_divergence_formula` |
| the central difference reproduces $3H$ to $1.9 \times 10^{-9}$ | COMPUTED (Notebook 06a, In [19]; the expected size of the error is $18h^2 = 1.8 \times 10^{-9}$ for the step $h = 10^{-5}$) | Notebook 06a only |

### 6.10 The Dirac operator written out, non-triviality and the negative control

**The Dirac operator.** Combine $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ with the contraction:

$$
\sum_\mu\gamma^\mu D_\mu\Psi = \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x8)}\Psi ,
$$

that is, with the factors written out,

$$
\begin{aligned}
&e^{-a_4}s^{-1}\big(\gamma^{(x1)}\partial_1 + \gamma^{(x2)}\partial_2 + \gamma^{(x3)}\partial_3\big)\Psi + \gamma^{(x4)}\partial_4\Psi \\
&\quad + e^{a_4}s^{-1}\big(\gamma^{(x5)}\partial_5 + \gamma^{(x6)}\partial_6 + \gamma^{(x7)}\partial_7\big)\Psi + \tan z\,\gamma^{(x8)}\partial_8\Psi + 3H\gamma^{(x8)}\Psi .
\end{aligned}
$$

This is the left side of the field equation of both fields; the right side is $(m + U'(S))\Psi$ with $S = \bar\Psi\Psi$ (Chapter 7). The Revision record writes out all sixteen component equations (formula `field_equation_components`), and Notebook 06a compares each of them with its own computation (In [20]). **Where the deflation enters.** It does not enter $\gamma^\mu\Omega_\mu$, but it enters every derivative term through the factors $1/f_a$: as 3-space inflates the 3-space derivatives are weighted less and less ($e^{-a_4}/s$), and as the extra times deflate the extra-time derivatives are weighted more and more ($e^{a_4}/s$). Figure 06a.9 draws these factors.

**The block form.** In the chiral split $\Psi = (\psi_-, \psi_+)$ (components 1 to 8 and 9 to 16, Chapter 5) every gamma of the author has zero blocks on the diagonal, $\gamma^{(xa)} = \begin{pmatrix}0 & \bar\tau_a\\ \tau_a & 0\end{pmatrix}$, and $\gamma^{(x8)}$ has the $8 \times 8$ identity in both off-diagonal blocks. So $3H\gamma^{(x8)}$ maps the first eight components onto the last eight and back with the factor $3H$, which is why its picture (figure 06a.7) shows the value 3 on two diagonal lines. Record: formula `field_equation_blocks`; `wolfram-field-theory.json`, check `block_form`.

**Non-triviality.** $(\gamma^{(x8)})^2 = 1$, so if $3H\gamma^{(x8)}\Psi = 0$ then $\Psi = \gamma^{(x8)}\gamma^{(x8)}\Psi = 0$ (multiply from the left by $\gamma^{(x8)}$ and divide by $3H > 0$). For every $H > 0$ and every field that is not identically zero, the term is present. PROVED; `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`, for the two fields. Section 6.29 states precisely how far this statement reaches.

**The negative control: extra times that INFLATE.** Is the cancellation caused by the deflation, or is it an accident of the algebra? Change the metric so that the extra times inflate like 3-space: $g_{tt} = -e^{+2a_4}\sin^{1/3}z$, factors $f_t = e^{+a_4}s$. Repeat Section 6.6: now $\partial_4f_t = +a_4'f_t$, so

$$
\omega_{x_t\,x_t\,x4} = (-1)\frac{a_4'f_t}{1} = -a_4'f_t, \qquad \omega_{x_t\,x4\,x_t} = +a_4'f_t, \qquad \omega_{x_t\,x_t\,x8} = -Hf_t
$$

(the formula $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\partial_bf_\mu/f_b$; the antisymmetry; $\partial_8f_t$ is unchanged), and $\Omega_{x_t} = f_t\big(a_4'S^{x4\,x_t} - HS^{x_t\,x8}\big)$. Repeat Section 6.8:

$$
\gamma^{x5}\Omega_{x5} = \tfrac12a_4'\,\gamma^{(x5)}\gamma^{(x4)}\gamma^{(x5)} - \tfrac12H\,\gamma^{(x5)}\gamma^{(x5)}\gamma^{(x8)} = \tfrac12a_4'\,\gamma^{(x4)} + \tfrac12H\,\gamma^{(x8)}
$$

(the same two products as before). Now all six warped directions contribute $+\frac12a_4'$ along the time, and

$$
\sum_\mu\gamma^\mu\Omega_\mu\Big|_{\text{control}} = 3a_4'\,\gamma^{(x4)} + 3H\,\gamma^{(x8)} .
$$

The divergence form of Section 6.9 agrees. With inflating extra times the volume factor is $\sqrt{\lvert g\rvert} = e^{3a_4}s^3\cdot1\cdot e^{3a_4}s^3\cot z = e^{6a_4}\cos z$, which now changes with time, and

$$
\frac{1}{2\sqrt{\lvert g\rvert}}\,\partial_4\Big(\prod_{c\neq x4}f_c\Big) = \frac{\partial_4\big(e^{6a_4}\cos z\big)}{2e^{6a_4}\cos z} = \frac{6a_4'e^{6a_4}\cos z}{2e^{6a_4}\cos z} = 3a_4'
$$

(the product without $x4$ is the whole volume factor because $f_4 = 1$; the chain rule gives $\partial_4e^{6a_4} = 6a_4'e^{6a_4}$; then cancel). **The cancellation in the author's metric is caused by the deflation.** The hidden term $3H\gamma^{(x8)}$ is the same in both cases: it comes from $x8$, not from the time dependence. PROVED; lead report, check `negative_control_inflating_extra_times`; Notebook 06a, In [22], and figure 10.

| statement | status | where it is verified |
| --- | --- | --- |
| the Dirac operator written out; all 16 components | PROVED | `field-theory.json`, formulas `field_equation` and `field_equation_components`; `wolfram-field-theory.json`, checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C` |
| the term $3H\gamma^{(x8)}\Psi$ vanishes only for $\Psi = 0$ (both fields) | PROVED, in the diagonal vielbein (scope: Section 6.29) | `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00` |
| negative control: $3a_4'\gamma^{(x4)} + 3H\gamma^{(x8)}$ with inflating extra times | PROVED | lead report, check `negative_control_inflating_extra_times` |

### 6.11 Example: Notebook 06a

Notebook 06a puts Sections 6.2 to 6.10 to work with exact algebra. It reads the author's eight gammas from the record `Revision/algebra/gammas.json`, checks the Clifford relations, and defines four general functions (Christoffel symbols, canonical spin connection, spinor connection, curved gammas) that work in any number of dimensions. It first applies them to the polar plane of Section 6.5 and draws the turning frame and the half-angle spinor rotation. Then it builds the author's metric with an arbitrary function $a_4(x_4)$ and computes, exactly: the vielbein, the volume factor, the 25 Christoffel symbols, the 12 components of the spin connection, the 512 equations of the vielbein postulate, $\Omega_\mu$, the covariant constancy of the gammas, the eight terms $\gamma^\mu\Omega_\mu$ and their sum $3H\gamma^{(x8)}$, the divergence form, the Dirac operator for sixteen arbitrary component functions, and the negative control. It compares every result that the Revision record also contains with the record, draws ten figures, needs no Rust, runs in about 30 seconds and ends with the line ALL 34 CHECKS PASSED (notebook 06a).

<!-- NOTEBOOK 06a -->

### 6.14 Line-by-line walk-through of Notebook 06a

The notebook has 24 code cells, In [1] to In [24]. This section explains every line of every one of them, in order: a line or a small group of lines is quoted and then explained. A line that starts with `#` is a **comment**, which Python skips; it is there for the reader. In a quoted figure cell a line `...` stands for the remaining lines of a long caption; every caption is printed in full under its figure in Section 6.13, and a paragraph "What Figure 06a.k shows" after the code says what to look for and why. The words of the notebook are those of its section 3 (Section 6.13), which Sections 6.2 to 6.7 defined.

**In [1], the set-up cell.** Its first part is the complete run instructions of Section 6.12 once more, as comment lines, so that the notebook file carries its own instructions. The code starts below the line that announces THE SET-UP. The set-up code is the same in every notebook of the book except for one line, the notebook's name; it is explained here once, and the walk-throughs of Notebooks 06b and 06c refer back to this explanation.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux

import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

`import` loads a **module** (a part of Python or of an installed package) so that the code can use it. `json` reads and writes JSON files (text files that store names, lists and numbers), `os` reads settings of the computer, `textwrap` breaks long lines, and `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on Windows, macOS and Linux. The plotting package matplotlib is loaded together with its drawing functions under the short name `plt`, and `Image` and `display` come from IPython, the part of Jupyter that runs Python; together they show a saved picture below a cell.

```python
NOTEBOOK_ID = "06a"  # this notebook: chapter 06, example a
```

A **variable** is a name for a value. This line gives the name `NOTEBOOK_ID` to the **string** (a text in quotes) `"06a"`. It is the only line of the set-up code that differs from notebook to notebook; the figure files and the last printed line are named after it.

```python
def find_repository_root():
    """Return the repository folder (Dirac_claude).

    Jupyter runs a notebook in the folder that holds it.  Starting there, go up one
    folder at a time until a folder contains Revision/textbook/requirements.txt (the
    list of the book's packages); that folder is the repository."""
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**, a named piece of code that runs when it is called. The text in triple quotes below the `def` line is its **docstring**, a description that Python stores and does not execute. `Path.cwd()` is the folder in which the notebook runs and `.resolve()` writes it as a complete address. `here.parents` is the list of the folders above it; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes these folders one after the other; `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that holds `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder holds it, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
# The repository folder.  It is never printed: it differs from computer to computer,
# and the printed output of a notebook must not.
REPO = find_repository_root()
# Every file is WRITTEN below OUTPUT_ROOT.  OUTPUT_ROOT is the repository folder unless
# the environment variable TEXTBOOK_OUTPUT_ROOT names another folder; the book's
# checking tool sets it, so that a check run writes into a scratch folder instead.
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The function is called and its result named `REPO`. It is never printed: it differs from computer to computer, while the printed output of a notebook must not. `os.environ` holds the **environment variables** of the computer (named texts that a program receives when it starts); `.get(name, default)` returns the value of `TEXTBOOK_OUTPUT_ROOT` when it is set and the repository folder otherwise. When you run the notebook the variable is not set, so files are written into the repository; the book's checking tool sets it to a scratch folder, so that a check never changes the repository.

```python
def repository_file(relative):
    """The path of the repository file relative, for READING (a Revision record)."""
    return REPO / relative


def output_file(relative):
    """The path at which to WRITE the repository file relative (its folder is made)."""
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

`repository_file("Revision/...")` is the full path of a repository file, used to READ a Revision record. `output_file("Revision/...")` is the full path at which a file is WRITTEN; `path.parent.mkdir(parents=True, exist_ok=True)` first creates its folder (and any missing folder above it) and does nothing if the folder exists.

```python
def say(text):
    """Print text in lines of at most 89 characters (the width of a page of the book)."""
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, the width of a page of the book: `str(text)` turns any value into text, and `textwrap.fill` breaks it at blanks; every line after the first starts with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

`matplotlib.rcdefaults()` returns to the built-in settings of matplotlib, so that the figures are the same on every computer whatever personal settings it has. `plt.rcParams.update({...})` then sets the size of a figure (7.0 by 4.2 inches), the size of its letters (10 points) and a faint grid behind the curves. The braces make a **dictionary**, a collection of pairs `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
# Start with an empty captions file ({} is an empty JSON dictionary); save_figure fills
# it.  newline="\n" writes the same line ends on Windows, macOS and Linux.
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: each name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/06a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes an empty dictionary `{}` and a line end into the captions file; `encoding="utf-8"` fixes how the letters are stored, and `newline="\n"` stores the same line end on every system.

```python
def save_figure(fig, name, caption):
    """Save the figure fig as Revision/textbook/figures/<id>_<k>_<name>.png, record its
    caption in CAPTION_FILE, show the saved picture below the cell and close the figure.
    k counts the figures of the notebook 1, 2, 3, ...; a cell run again keeps its k."""
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    # dpi=150: 150 dots per inch.  bbox_inches="tight": cut away the empty margin.
    # metadata={"Software": None}: no program name is stored in the PNG file, so that
    # every run writes exactly the same bytes.
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

`save_figure` is called once for every figure. `FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)` returns the number already stored for this figure name, or stores and returns one more than the number of figures so far; so the figures are numbered 1, 2, 3, and a cell that is run twice keeps its number. The file name joins the notebook id, the number and the name, for example `06a_1_polar_frame_and_spin_rotation.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch, cuts away the empty margin and stores no program name, so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory (Jupyter would otherwise draw it a second time). The caption is stored, and the whole dictionary of captions is written to the captions file (`json.dumps` turns it into JSON text with sorted keys). `display(Image(...))` shows the saved picture below the cell, and the last line prints where it was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    """A check.  If condition is False, stop with an AssertionError that names the
    check (an if statement is used instead of assert, because python -O would skip an
    assert).  Otherwise print "PASS <name>" and, when the check reproduces a Revision
    record, a second line naming the record file and its check."""
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list**, an ordered collection written with square brackets. `check` is the function behind every check of the book. `condition` is `True` or `False`; if it is false, `raise AssertionError(...)` stops the notebook with an error that names the check (Python's own statement `assert` is not used, because Python started with the option `-O` would skip it). If it is true, the name is appended to `PASSED` and the line PASS name is printed; when the optional argument `record` names a Revision record, a second line says which record file and which check the result reproduces.

```python
def report(label, value, unit=""):
    """Print a key number as a line "RESULT <label> = <value> <unit>"."""
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    """Print the last line of the notebook: how many checks passed."""
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT. `all_checks_passed` prints the last line of the notebook with the number of checks that passed (`len` is the length of a list). The final statement prints the single output line of In [1].

**In [2], the gammas from the record.**

```python
import sys  # the Python system module (here: the stream of printed text)

# Jupyter sends printed text to the screen in pieces, about every 0.2 seconds.  The
# book's checking tool reads each PASS line together with its "reproduces" line, so
# the pieces must be the same in every run: send the printed text of a cell in one
# piece when the cell ends (or just before a figure), at the latest after 600 s.
if hasattr(sys.stdout, "flush_interval"):  # true inside Jupyter only
    sys.stdout.flush_interval = 600.0
```

`sys` is the Python module that holds, among other things, `sys.stdout`, the channel through which everything printed travels. Inside Jupyter this channel collects printed text and sends it to the screen in pieces, about every 0.2 seconds. The book's checking tool reads each PASS line together with its "reproduces" line, so the pieces must be the same in every run. `hasattr(sys.stdout, "flush_interval")` is true only inside Jupyter (outside it the channel has no such setting), and then the interval is set to 600 seconds: the text of a cell is sent in one piece when the cell ends, or just before a figure is shown. This changes no result.

```python
import numpy as np  # arrays of decimal numbers (only for the plots)
import sympy as sp  # exact algebra and calculus with symbols
```

numpy (short name `np`) computes with decimal numbers and is used only for the plots; sympy (short name `sp`) computes exactly with symbols, fractions and functions, and does all the mathematics of the notebook.

```python
GAMMA_FILE = "Revision/algebra/gammas.json"  # a Revision record (read only)
fixture = json.loads(repository_file(GAMMA_FILE).read_text(encoding="utf-8"))
NAMES = fixture["coordinates"]  # ["x1", ..., "x8"], the names of the directions
ETA = fixture["eta"]  # the frame metric: +1 space-like, -1 time-like
```

`GAMMA_FILE` names the Revision record of the gammas. `read_text` reads the file as text and `json.loads` turns the text into Python objects: `fixture` is a dictionary whose keys are the names stored in the record. `fixture["coordinates"]` is the list `["x1", ..., "x8"]`, and `fixture["eta"]` the list of the diagonal entries of $\eta$.

```python
# Each gamma is stored as 16 rows of 16 whole numbers; sp.Matrix makes it an exact
# sympy matrix.  gamma[a] is the gamma of the direction NAMES[a].
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]
I16 = sp.eye(16)  # the 16 x 16 identity matrix
Z16 = sp.zeros(16, 16)  # the 16 x 16 zero matrix
say(f"directions: {NAMES}")
say(f"eta (frame metric): {ETA}")
```

Each gamma is stored as 16 rows of 16 whole numbers; `sp.Matrix(rows)` turns it into an exact sympy matrix. The **list comprehension** `[... for rows in ...]` builds the list of the eight matrices in one line, so `gamma[0]` is $\gamma^{(x1)}$, `gamma[3]` is $\gamma^{(x4)}$ and `gamma[7]` is $\gamma^{(x8)}$ (Python counts from 0). `sp.eye(16)` is the identity matrix and `sp.zeros(16, 16)` the zero matrix. The two `say` lines print the directions and the signs of $\eta$, the first two output lines.

```python
# The Clifford relation for all 8 x 8 = 64 pairs (a, b): the anticommutator is
# 2 eta_aa times the identity when a = b and the zero matrix when a and b differ.
clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
               == (2 * ETA[a] if a == b else 0) * I16
               for a in range(8) for b in range(8))
check(clifford, "the 64 Clifford relations of the author's gammas",
      record="Revision/theory/reports/python-field-theory.json, "
             "check clifford_relations")
```

`all(... for a in range(8) for b in range(8))` is true when the expression is true for every one of the $8 \times 8 = 64$ pairs; `range(8)` is the list $0, 1, \dots, 7$. For each pair the left side is the anticommutator $\gamma^a\gamma^b + \gamma^b\gamma^a$ (with sympy matrices `*` is the matrix product) and the right side is $2\eta_{aa}$ times the identity when $a = b$ and the zero matrix otherwise (`x if condition else y` is `x` when the condition holds and `y` otherwise; `0 * I16` is the zero matrix). `==` compares two sympy matrices entry by entry, exactly. The check prints PASS and the record it reproduces.

```python
# eight matrices, each with 16 rows and 16 columns, and every entry a real number
check(len(gamma) == 8 and all(matrix.shape == (16, 16) for matrix in gamma)
      and all(entry.is_real for matrix in gamma for entry in matrix),
      "the eight gammas are 16 x 16 matrices with real entries",
      record="Revision/theory/reports/python-field-theory.json, check gammas_real")
```

The second check requires eight matrices, each of shape 16 by 16, and every entry real (`entry.is_real` is true for a whole number). `and` is true only when all its parts are true.

```python
# S[a][b] = (1/4)(gamma^a gamma^b - gamma^b gamma^a), for all 64 pairs (a, b).
S = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
     for a in range(8)]
```

`S[a][b]` is the generator $S^{ab} = \frac14(\gamma^a\gamma^b - \gamma^b\gamma^a)$ for all 64 ordered pairs, built with a nested list comprehension: for each `a` a list over `b`. The cell prints the two lines of the directions and of $\eta$, and two PASS lines with their records.

**In [3], four helpers.**

```python
from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation
```

`parse_mathematica` is sympy's reader of formulas written in the notation of the Wolfram Language, the notation in which the record `Revision/theory/field-theory.json` stores its formulas.

```python
def is_zero(expr):
    """True when expr is exactly zero for all values of its symbols."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    # Fast route: sin, cos, tan, ... written through exp, multiplied out, cancelled.
    if sp.cancel(sp.expand(expr.rewrite(sp.exp))) == 0:
        return True
    return sp.simplify(expr) == 0  # the slower general route
```

`is_zero(expr)` decides exactly whether an expression is zero for all values of its symbols. `sp.sympify` turns a plain number into a sympy number. If the expression is already the number 0 the answer is yes. Otherwise the fast route writes every sine, cosine and tangent through exponential functions (`rewrite(sp.exp)`; for example $\cos z = (e^{iz} + e^{-iz})/2$), multiplies everything out (`expand`) and cancels common factors of numerator and denominator (`cancel`); if that gives 0, the expression is zero. If not, the slower general `sp.simplify` decides. Both routes are exact transformations, so the function never calls a nonzero expression zero; at worst it fails to recognise a zero, and then a check fails visibly.

```python
def matrix_is_zero(matrix):
    """True when every entry of the matrix is exactly zero."""
    return all(is_zero(entry) for entry in matrix)
```

`matrix_is_zero` applies `is_zero` to every entry of a matrix (a `for` over a sympy matrix runs through its entries).

```python
def record_passed(path, name):
    """True when the Revision report at path records the check name as passed."""
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in data["checks"]:
        if entry["name"] == name:
            return entry["verdict"].upper() == "PASS"  # "PASS" or "pass"
    raise KeyError(f"{path} has no check {name}")
```

`record_passed(path, name)` reads a Revision report, a JSON file with a list `checks` whose entries have the keys `name`, `verdict` and `detail`, and returns `True` when the check `name` is recorded with the verdict PASS (`.upper()` writes the verdict in capitals, because one report writes PASS and another pass). If the report has no such check, `raise KeyError` stops the notebook: a misspelled check name can never pass silently.

```python
THEORY_FILE = "Revision/theory/field-theory.json"  # the record of the formulas
FORMULAS = {item["key"]: item["wl"] for item in json.loads(
    repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
```

The record `field-theory.json` holds a list `formulas`, each with a key and the formula as Wolfram text (`wl`). The **dictionary comprehension** `{item["key"]: item["wl"] for item in ...}` builds the dictionary from key to text in one line.

```python
def record_formula(key, names):
    """The formula key of the record as a sympy expression.  names maps the
    record's symbol names (texts) to the symbols and functions of this notebook."""
    text = FORMULAS[key]
    # The record writes a4', a4'' and a4(x4) as Derivative[1][a4][x4],
    # Derivative[2][a4][x4] and a4[x4]; give them short names before reading.
    for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                  ("Derivative[2][a4][x4]", "a4pp"),
                                  ("a4[x4]", "a4")):
        text = text.replace(long_form, short_form)
    expr = parse_mathematica(text)
    return expr.subs({sp.Symbol(name): value for name, value in names.items()},
                     simultaneous=True)
```

`record_formula(key, names)` turns one formula of the record into a sympy expression. The record writes $a_4'$, $a_4''$ and $a_4(x_4)$ as `Derivative[1][a4][x4]`, `Derivative[2][a4][x4]` and `a4[x4]`; the loop replaces them by the short names `a4p`, `a4pp` and `a4` (`text.replace(old, new)` replaces every occurrence). `parse_mathematica` reads the text, and `.subs({...}, simultaneous=True)` replaces each plain symbol of the record by the symbol or function of the notebook that the dictionary `names` gives for it, all at the same time.

```python
REPORT_PY = "Revision/theory/reports/python-field-theory.json"
REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
REPORT_LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
say(f"{len(FORMULAS)} formulas read from {THEORY_FILE}")
```

Three names for the three Revision reports that the notebook reproduces, and one output line: 32 formulas read from Revision/theory/field-theory.json.

**In [4], four general formulas as Python functions.** The four functions work for any number of dimensions and any vielbein, so the same code serves the plane and the author's eight-dimensional metric.

```python
def christoffel(g, coords):
    """Gam[l][m][n] = (1/2) sum_r g^lr (d_m g_rn + d_n g_rm - d_r g_mn)."""
    n = len(coords)
    g_inv = g.inv()  # the inverse metric g^lr
    Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for k in range(m, n):  # Gamma^l_mk = Gamma^l_km: compute it once
                value = sum(g_inv[l, r] * (sp.diff(g[r, k], coords[m])
                                           + sp.diff(g[r, m], coords[k])
                                           - sp.diff(g[m, k], coords[r]))
                            for r in range(n) if g_inv[l, r] != 0) / 2
                value = sp.simplify(value)
                Gam[l][m][k] = value
                Gam[l][k][m] = value
    return Gam
```

`christoffel(g, coords)` computes $\Gamma^l{}_{mn}$ by the formula of Section 6.3. `g.inv()` is the inverse matrix $g^{lr}$. `Gam` starts as a three-level list of zeros (`[sp.Integer(0)] * n` is a list of `n` exact zeros). The loops run over all `l` and `m` and over `k` from `m` upwards only: since $\Gamma^l{}_{mk} = \Gamma^l{}_{km}$, each symmetric pair is computed once and stored in both places. `sp.diff(g[r, k], coords[m])` is the partial derivative $\partial_m g_{rk}$; the generator expression sums over `r`, skipping the entries where the inverse metric is zero (for a diagonal metric only `r = l` remains), and `/ 2` is the factor $\frac12$. `sp.simplify` brings each symbol into a short form.

```python
def spin_connection(e, Gam, coords, eta):
    """omega[mu][a][b] = omega_{mu ab} = eta_aa omega_mu^a_b, where
    omega_mu^a_b = sum_nu e^a_nu (d_mu e_b^nu + sum_lam Gam^nu_{mu lam} e_b^lam)."""
    n = len(coords)
    E = e.inv()  # E[nu, b] = e_b^nu, the inverse vielbein
    omega = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for a in range(n):
            for b in range(n):
                mixed = 0  # will become omega_mu^a_b
                for nu in range(n):
                    if e[a, nu] == 0:
                        continue  # this term is zero
                    inner = sp.diff(E[nu, b], coords[mu]) + sum(
                        Gam[nu][mu][lam] * E[lam, b] for lam in range(n))
                    mixed += e[a, nu] * inner
                omega[mu][a][b] = sp.simplify(eta[a] * mixed)  # lower the index a
    return omega
```

`spin_connection(e, Gam, coords, eta)` computes the canonical spin connection by the formula of Section 6.4 and lowers its first index. The vielbein is the matrix `e` with `e[a, mu]` $= e^a{}_\mu$ (row = frame index, column = coordinate index). Its inverse matrix `E = e.inv()` has `E[mu, a]` $= e_a{}^\mu$, because $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ says exactly `e * E` $= 1$. For each $\mu$, $a$, $b$ the variable `mixed` collects $\sum_\nu e^a{}_\nu\big(\partial_\mu e_b{}^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda\big)$, the mixed component $\omega_\mu{}^a{}_b$; `continue` skips the values of $\nu$ where $e^a{}_\nu = 0$, which contribute nothing. The last line multiplies by $\eta_{aa}$ (lowering the index $a$) and simplifies, so the function returns `omega[mu][a][b]` $= \omega_{\mu ab}$.

```python
def spinor_connection(omega, S):
    """Omega[mu] = (1/2) sum_{a,b} omega_{mu ab} S^ab = sum_{a<b} omega_{mu ab} S^ab."""
    n = len(omega)
    size = S[0][0].shape[0]  # 16 for the author's gammas, 2 in two dimensions
    Omega = []
    for mu in range(n):
        total = sp.zeros(size, size)
        for a in range(n):
            for b in range(a + 1, n):
                if omega[mu][a][b] != 0:
                    total += omega[mu][a][b] * S[a][b]
        Omega.append(total)
    return Omega
```

`spinor_connection(omega, S)` builds $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$ (Section 6.7 showed that the sum over $a < b$ uses up the factor $\frac12$). `S[0][0].shape[0]` is the size of the matrices, 16 for the author's gammas and 2 in the plane. For each $\mu$ a zero matrix is filled with the terms whose coefficient is not zero, and the eight matrices are collected in the list `Omega`.

```python
def curved_gammas(e, gammas):
    """gamma^mu = sum_a e_a^mu gamma^a for every coordinate mu."""
    E = e.inv()
    n = len(gammas)
    return [sum((E[mu, a] * gammas[a] for a in range(n)),
                sp.zeros(*gammas[0].shape)) for mu in range(n)]
```

`curved_gammas(e, gammas)` returns the list of the curved gammas $\gamma^\mu = \sum_a e_a{}^\mu\gamma^a$; `sum(..., sp.zeros(...))` adds the matrices starting from a zero matrix of the right shape (`*gammas[0].shape` passes the two numbers of the shape as two arguments).

```python
say("defined: christoffel, spin_connection, spinor_connection, curved_gammas")
```

One output line names the four functions.

**In [5], the warm-up in the polar plane** (Section 6.5).

```python
r, phi = sp.symbols("r phi", positive=True)  # polar coordinates, r > 0
sigma1 = sp.Matrix([[0, 1], [1, 0]])  # the three Pauli matrices
sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
plane_gammas = [sigma1, sigma2]  # gamma^0 (radial), gamma^1 (angular)
plane_eta = [1, 1]
plane_S = [[(plane_gammas[a] * plane_gammas[b] - plane_gammas[b] * plane_gammas[a])
            / 4 for b in range(2)] for a in range(2)]
plane_g = sp.diag(1, r**2)  # ds^2 = dr^2 + r^2 dphi^2
plane_e = sp.diag(1, r)  # e^a_mu: unit radial and unit angular direction
```

`sp.symbols("r phi", positive=True)` makes two symbols that sympy treats as positive numbers, the polar coordinates $r$ and $\varphi$. The three Pauli matrices are typed entry by entry (`sp.I` is the imaginary unit $i$). The plane has the two gammas $\sigma_1$ (radial) and $\sigma_2$ (angular), the frame metric $\eta = (1, 1)$, the generators `plane_S` built exactly as `S` in In [2], the metric $\mathrm{diag}(1, r^2)$ and the vielbein $\mathrm{diag}(1, r)$.

```python
plane_Gam = christoffel(plane_g, [r, phi])
plane_omega = spin_connection(plane_e, plane_Gam, [r, phi], plane_eta)
plane_Omega = spinor_connection(plane_omega, plane_S)
plane_gup = curved_gammas(plane_e, plane_gammas)
plane_slash = sp.simplify(plane_gup[0] * plane_Omega[0] + plane_gup[1] * plane_Omega[1])
```

The four general functions are applied to the plane. `plane_slash` is $\gamma^r\Omega_r + \gamma^\varphi\Omega_\varphi$, the contraction, simplified.

```python
say(f"Gamma^r_phiphi = {plane_Gam[0][1][1]},  Gamma^phi_rphi = {plane_Gam[1][0][1]}")
say(f"omega_phi01 = {plane_omega[1][0][1]},  omega_phi10 = {plane_omega[1][1][0]}")
say(f"Omega_phi = {plane_Omega[1].tolist()}")
say(f"gamma^mu Omega_mu = {plane_slash.tolist()}")
```

Four output lines print the results: $\Gamma^r{}_{\varphi\varphi} = -r$, $\Gamma^\varphi{}_{r\varphi} = 1/r$, $\omega_{\varphi01} = -1$, $\omega_{\varphi10} = 1$, $\Omega_\varphi$ as the nested list `[[-I/2, 0], [0, I/2]]` (`.tolist()` turns a matrix into a list of rows) and the contraction `[[0, 1/(2*r)], [1/(2*r), 0]]`, which is $\sigma_1/(2r)$. Index `[1]` is $\varphi$ and `[0]` is $r$.

```python
check(plane_Gam[0][1][1] == -r and plane_Gam[1][0][1] == 1 / r,
      "polar plane: Gamma^r_phiphi = -r and Gamma^phi_rphi = 1/r")
check(plane_omega[1][0][1] == -1 and plane_omega[1][1][0] == 1
      and plane_omega[0][0][1] == 0, "polar plane: omega_phi01 = -1, omega_r = 0")
check(plane_Omega[1] == -sp.I / 2 * sigma3 and plane_Omega[0] == sp.zeros(2, 2),
      "polar plane: Omega_phi = -(i/2) sigma3 and Omega_r = 0")
check(plane_slash == sigma1 / (2 * r), "polar plane: gamma^mu Omega_mu = sigma1/(2 r)")
```

Four checks compare the results with the hand computation of Section 6.5: the two Christoffel symbols; the two components of $\omega_\varphi$ and the vanishing of $\omega_r$; $\Omega_\varphi = -\frac i2\sigma_3$ and $\Omega_r = 0$; and $\sum_\mu\gamma^\mu\Omega_\mu = \sigma_1/(2r)$.

```python
F_rphi = (plane_Omega[1].diff(r) - plane_Omega[0].diff(phi)
          + plane_Omega[0] * plane_Omega[1] - plane_Omega[1] * plane_Omega[0])
U = sp.cos(phi / 2) * sp.eye(2) + sp.I * sp.sin(phi / 2) * sigma3  # spinor rotation
pure_gauge = -U.diff(phi) * U.inv() - plane_Omega[1]  # must be the zero matrix
check(F_rphi == sp.zeros(2, 2) and matrix_is_zero(pure_gauge),
      "polar plane: flat (F_rphi = 0) and Omega_phi = -(dU/dphi) U^-1")
```

`F_rphi` is the curvature $\partial_r\Omega_\varphi - \partial_\varphi\Omega_r + [\Omega_r, \Omega_\varphi]$ (`.diff(r)` differentiates every entry). `U` is the spinor rotation $\cos\frac\varphi2 + i\sin\frac\varphi2\,\sigma_3$, and `pure_gauge` is $-(\partial_\varphi U)U^{-1} - \Omega_\varphi$ (`U.inv()` is the inverse matrix). The fifth check requires both to be zero: the plane is flat, and its spin connection is only the turning of the frame. The cell prints five PASS lines.

**In [6], figure 1.**

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.6))
angles = np.arange(12) * np.pi / 6  # 12 angles, 30 degrees apart
for radius in (1.0, 2.0):
    px, py = radius * np.cos(angles), radius * np.sin(angles)  # the points
    ax_left.quiver(px, py, np.cos(angles), np.sin(angles), color="black",
                   angles="xy", scale_units="xy", scale=3.0, width=0.006)
    ax_left.quiver(px, py, -np.sin(angles), np.cos(angles), color="tab:orange",
                   angles="xy", scale_units="xy", scale=3.0, width=0.006)
    circle = np.linspace(0.0, 2.0 * np.pi, 200)
    ax_left.plot(radius * np.cos(circle), radius * np.sin(circle), ":",
                 color="gray", linewidth=1.0)
```

`plt.subplots(1, 2, figsize=(10.0, 4.6))` makes one figure with two panels side by side, called `ax_left` and `ax_right`. `np.arange(12) * np.pi / 6` is the list of the twelve angles $0, \pi/6, \dots, 11\pi/6$ (30 degrees apart). For the radii 1 and 2 the points $(r\cos\varphi, r\sin\varphi)$ are computed, and `quiver` draws an arrow at each point: the unit radial direction $(\cos\varphi, \sin\varphi)$ in black and the unit angular direction $(-\sin\varphi, \cos\varphi)$ in orange. The options `angles="xy", scale_units="xy", scale=3.0` draw an arrow of length one third in the units of the axes. The dotted circle is drawn through 200 points.

```python
ax_left.plot([], [], color="black", label="unit radial direction $e_{(0)}$")
ax_left.plot([], [], color="tab:orange", label="unit angular direction $e_{(1)}$")
ax_left.set_aspect("equal")
ax_left.set_xlim(-2.8, 2.8)
ax_left.set_ylim(-2.8, 3.6)  # room for the legend above the circles
ax_left.set_xlabel("Cartesian $x = r\\cos\\varphi$")
ax_left.set_ylabel("Cartesian $y = r\\sin\\varphi$")
ax_left.set_title("The polar frame turns with the angle")
ax_left.legend(loc="upper left", fontsize=8)
```

Two empty plots (`[]`, `[]`) only create the legend entries. `set_aspect("equal")` makes one unit equally long on both axes, so the circles look round. The axis limits leave room for the legend above the circles; the axes are labelled and the legend is placed in the upper left corner.

```python
turn = np.linspace(0.0, 4.0 * np.pi, 400)  # phi from 0 to 4 pi
ax_right.plot(turn / np.pi, np.cos(turn / 2), label="$\\cos(\\varphi/2)$, real part")
ax_right.plot(turn / np.pi, np.sin(turn / 2), "--",
              label="$\\sin(\\varphi/2)$, imaginary part")
ax_right.set_xlabel("$\\varphi / \\pi$")
ax_right.set_ylabel("entry $U_{11}$ of the spinor rotation")
ax_right.set_ylim(-1.45, 1.2)  # room for the legend below the curves
ax_right.set_title("A spinor turns by half the angle")
ax_right.legend(loc="lower center", ncol=2, fontsize=8)
```

The right panel draws the entry $U_{11} = \cos\frac\varphi2 + i\sin\frac\varphi2$ of the spinor rotation for 400 values of $\varphi$ from $0$ to $4\pi$: its real part $\cos(\varphi/2)$ as a solid line and its imaginary part $\sin(\varphi/2)$ dashed (the style string of two minus signs). The horizontal axis shows $\varphi/\pi$, so the full turn is at 2 and the double turn at 4. In the labels `\\` is a single backslash for matplotlib's formula typesetting.

```python
save_figure(fig, "polar_frame_and_spin_rotation",
            "Warm-up in the flat plane. Left: the unit radial direction (black) and "
            ...
            "$4\\pi$ is it $+1$ again.")
```

`save_figure` saves the figure with its caption, shows it and prints one line with the name of the saved file, `06a_1_polar_frame_and_spin_rotation.png` in the folder `Revision/textbook/figures`.

**What Figure 06a.1 shows.** On the left, the black and orange arrows turn together as one goes around the circle: the polar frame at the angle $\varphi$ is the Cartesian frame turned by $\varphi$. That turning is exactly what $\omega_{\varphi01} = -1$ records, although the plane is flat. On the right, the solid curve $\cos(\varphi/2)$ reaches $-1$ at $\varphi = 2\pi$ (the value 2 on the axis), where the dashed curve is 0: after one full turn the spinor rotation is $-1$, and only at $4\pi$ is it $+1$ again. A spinor turns by half the angle of its frame.

**In [7], the author's metric and its vielbein** (Section 6.2).

```python
x = sp.symbols("x1:9", real=True)  # x[0] = x1, ..., x[3] = x4, ..., x[7] = x8
x4, x8 = x[3], x[7]
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
a4 = sp.Function("a4")(x4)  # the metric function a4(x4): any function of the time
z = 6 * H * x8  # the hidden angle z = 6 H x8, between 0 and pi/2
s = sp.sin(z) ** sp.Rational(1, 6)  # sin^(1/6) z
f = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3 + [sp.cot(z)]
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # g_aa = eta_aa f_a^2
e = sp.diag(*f)  # the diagonal vielbein e^a_mu = f_a delta^a_mu
```

`sp.symbols("x1:9", real=True)` makes the eight real symbols $x_1, \dots, x_8$ (the range `1:9` stops before 9); `x[3]` is $x_4$ and `x[7]` is $x_8$. `H` is positive. `sp.Function("a4")(x4)` is an unknown function of $x_4$: every result below holds for every function $a_4$. `z` is $6Hx_8$, `s` is $\sin^{1/6}z$ (`sp.Rational(1, 6)` is the exact fraction $\frac16$). The list `f` holds the eight factors: `[...] * 3` repeats a one-element list three times and `+` joins lists. `g` is the diagonal matrix with the entries $\eta_{aa}f_a^2$ (`sp.diag(*list)` puts the list on the diagonal), and `e` the diagonal vielbein.

```python
# The names under which the record writes symbols, and our symbols for them:
RECORD_NAMES = {"H": H, "x4": x4, "x8": x8, "a4": a4,
                "a4p": sp.Derivative(a4, x4), "a4pp": sp.Derivative(a4, (x4, 2))}
metric_record = sp.Matrix([list(row) for row in record_formula("metric", RECORD_NAMES)])
f_record = record_formula("vielbein_diagonal", RECORD_NAMES)
```

The record writes its symbols as plain names; `RECORD_NAMES` says which symbol or function of the notebook each name means (`sp.Derivative(a4, x4)` is $a_4'$ and `sp.Derivative(a4, (x4, 2))` is $a_4''$). The record's metric is read as a nested list and turned into a matrix (`list(row)` makes each row a list), and the record's eight vielbein factors are read as a list.

```python
check(matrix_is_zero(g - metric_record),
      "eta_aa f_a^2 is the author's metric (all 64 entries)",
      record=f"{THEORY_FILE}, formula metric")
check(all(is_zero(f[a] - f_record[a]) for a in range(8))
      and record_passed(REPORT_LEAD, "vielbein_reproduces_metric"),
      "the eight vielbein factors f_a",
      record=f"{THEORY_FILE}, formula vielbein_diagonal")
```

The first check requires all 64 entries of $g$ minus the record's metric to vanish. The second requires the eight factors to equal the record's and the lead's independent report to record `vielbein_reproduces_metric` as passed.

```python
volume = sp.simplify(sp.prod(f))  # f1 f2 ... f8
say(f"f1 f2 ... f8 = {volume}")
check(is_zero(volume - sp.cos(z)) and is_zero(volume**2 - g.det()),
      "sqrt|det g| = f1 f2 ... f8 = cos z, independent of x4",
      record=f"{REPORT_PY}, check sqrt_det_g_equals_cos_z")
```

`sp.prod(f)` multiplies the eight factors, and the simplified product is printed: `f1 f2 ... f8 = cos(6*H*x8)`. The check requires it to be $\cos z$ and its square to be the determinant of $g$ (`g.det()`), so that it is $\sqrt{\lvert\det g\rvert}$. The cell prints three PASS lines with their records and the product.

**In [8], figure 2.**

```python
X4_SYMBOL = sp.Symbol("t", real=True)  # the time x4 as a plain symbol for numbers
history = {a4: X4_SYMBOL}  # the illustrative history a4(x4) = x4 (with H = 1)
f_of_time = sp.lambdify(X4_SYMBOL, [fa.subs(history).subs({H: 1, x8: sp.pi / 24})
                                    for fa in f])  # z = 6 x8 = pi/4
times = np.linspace(-2.0, 2.0, 201)
values = [np.broadcast_to(v, times.shape) for v in f_of_time(times)]
```

For numbers the unknown function $a_4$ must be given a form. `history` replaces $a_4(x_4)$ by the plain symbol `t`, the illustrative history $a_4 = x_4$ (with $H = 1$, the prescribed background of Chapter 3 with slope 1). `sp.lambdify(t, [...])` turns the eight factors, with $H = 1$ and $x_8 = \pi/24$ (so $z = 6x_8 = \pi/4$), into one numerical function of `t` that returns the eight values. `times` is a list of 201 times from $-2$ to $2$. The factor $f_4 = 1$ does not depend on `t`, so `lambdify` returns the single number 1 for it; `np.broadcast_to(v, times.shape)` turns such a number into a list of 201 equal values, so that every curve can be plotted.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.4))
ax_left.semilogy(times, values[0], label="$f_1 = f_2 = f_3 = e^{a_4}s$ (3-space)")
ax_left.semilogy(times, values[4], "--",
                 label="$f_5 = f_6 = f_7 = e^{-a_4}s$ (extra times)")
ax_left.semilogy(times, values[3], ":", color="black", label="$f_4 = 1$ (time)")
ax_left.semilogy(times, values[0] * values[4], "-.", color="gray",
                 label="product $f_1 f_5 = s^2$")
ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$")
ax_left.set_ylabel("vielbein factor (logarithmic axis)")
ax_left.set_title("Inflating 3-space, deflating extra times")
ax_left.legend(fontsize=8)
```

`semilogy` plots with a logarithmic vertical axis, on which an exponential function is a straight line. Four curves: $f_1 = e^{a_4}s$ (solid), $f_5 = e^{-a_4}s$ (dashed), $f_4 = 1$ (dotted, black) and the product $f_1f_5 = s^2$ (dash-dotted, gray).

```python
zz = np.linspace(0.02, np.pi / 2 - 0.02, 300)  # z inside (0, pi/2)
ax_right.plot(zz, np.sin(zz) ** (1 / 6), label="$s = \\sin^{1/6} z$")
ax_right.plot(zz, 1 / np.tan(zz), "--", label="$f_8 = \\cot z$ (hidden)")
ax_right.plot(zz, np.cos(zz), ":", color="black",
              label="$\\sqrt{|\\det g|} = \\cos z$")
ax_right.set_ylim(0.0, 3.0)
ax_right.set_xlabel("hidden angle $z = 6 H x_8$ (radians)")
ax_right.set_ylabel("factor (pure number)")
ax_right.set_title("Dependence on the hidden direction")
ax_right.legend(fontsize=8)
```

The right panel uses 300 values of $z$ inside $(0, \pi/2)$ (0.02 away from both ends, where $\cot z$ would be infinite) and draws $s = \sin^{1/6}z$, $f_8 = \cot z$ ($1/\tan z$) and the volume factor $\cos z$. `set_ylim(0.0, 3.0)` cuts the axis at 3, because $\cot z$ grows without bound near $z = 0$.

```python
save_figure(fig, "vielbein_factors",
            "The eight factors $f_a$ of the diagonal vielbein. Left: versus the time "
            ...
            "z$, which does not depend on the time.")
```

The figure is saved with its caption; the cell prints the name of the saved file, `06a_2_vielbein_factors.png`.

**What Figure 06a.2 shows.** On the left, the 3-space factor rises and the extra-time factor falls along straight lines of opposite slope (on a logarithmic axis an exponential is a straight line): 3-space inflates while the extra times deflate exponentially, at the same rate. Their product is the flat gray line $s^2$, and the time factor is 1. On the right, as functions of the hidden angle: $s$ rises slowly to 1, the hidden factor $\cot z$ falls from very large values near the tip $z = 0$ to 0 at the patch end $z = \pi/2$, and the volume factor $\cos z$ falls from 1 to 0. The volume factor does not depend on the time at all; Section 6.9 showed why this matters.

**In [9], the Christoffel symbols** (Section 6.3).

```python
Gam = christoffel(g, x)
independent = {(l, m, n): Gam[l][m][n] for l in range(8) for m in range(8)
               for n in range(m, 8) if Gam[l][m][n] != 0}
report("number of independent nonzero Christoffel symbols", len(independent))
```

`christoffel(g, x)` computes all $8 \cdot 8 \cdot 8 = 512$ symbols. The dictionary `independent` keeps those with $m \le n$ (`range(m, 8)`) that are not zero, under the key `(l, m, n)`. `report` prints their number, 25.

```python
christoffel_record = record_formula("christoffel_nonzero", RECORD_NAMES)
# The record numbers the directions 1..8; Python counts 0..7: subtract 1.
record_dict = {(int(l) - 1, int(m) - 1, int(n) - 1): value
               for l, m, n, value in christoffel_record}
same = set(record_dict) == set(independent) and all(
    is_zero(independent[key] - record_dict[key]) for key in independent)
```

The record's list `christoffel_nonzero` has entries $\{l, m, n, \text{value}\}$ with the directions numbered 1 to 8; subtracting 1 gives Python's positions. `set(record_dict) == set(independent)` requires the same 25 keys on both sides (a **set** is a collection without order), and `all(...)` requires every value to agree exactly.

```python
for key in [(0, 0, 3), (4, 3, 4), (0, 0, 7), (3, 0, 0), (7, 7, 7)]:
    l, m, n = key
    say(f"Gamma^{NAMES[l]}_{NAMES[m]}{NAMES[n]} = {independent[key]}")
```

Five symbols are printed as examples: $\Gamma^{x1}{}_{x1x4} = a_4'$, $\Gamma^{x5}{}_{x4x5} = -a_4'$, $\Gamma^{x1}{}_{x1x8} = H/\tan z$, $\Gamma^{x4}{}_{x1x1} = e^{2a_4}\sin^{1/3}z\,a_4'$ and $\Gamma^{x8}{}_{x8x8} = -12H/\sin 2z$, as derived in Section 6.3 (sympy prints the power $\frac13$ as `**(1/3)` and $a_4'$ as `Derivative(a4(x4), x4)`).

```python
check(len(independent) == 25 and same,
      "the 25 independent nonzero Christoffel symbols equal the record",
      record=f"{THEORY_FILE}, formula christoffel_nonzero")
```

The check requires 25 symbols equal to the record's; it prints PASS and the record.

**In [10], figure 3.**

```python
SAMPLE = {H: 1, x8: sp.pi / 24}  # H = 1 and z = 6 H x8 = pi/4


def at_sample(expr):
    """The decimal value of expr at the sample point H = 1, z = pi/4, a4 = 1/2,
    a4' = 1/2, a4'' = 0 (derivatives are replaced first, then a4 itself)."""
    expr = sp.sympify(expr).subs(sp.Derivative(a4, (x4, 2)), 0)
    expr = expr.subs(sp.Derivative(a4, x4), sp.Rational(1, 2))
    expr = expr.subs(a4, sp.Rational(1, 2))
    return complex(sp.N(expr.subs(SAMPLE)))
```

`SAMPLE` fixes $H = 1$ and $x_8 = \pi/24$, so $z = \pi/4$. `at_sample(expr)` gives the decimal value of an expression at the **sample point** $H = 1$, $z = \pi/4$, $a_4 = \frac12$, $a_4' = \frac12$, $a_4'' = 0$. The order of the replacements matters: the derivatives are replaced first, because replacing $a_4(x_4)$ by the number $\frac12$ first would turn $a_4'$ into the derivative of a constant, which is 0. `sp.N` evaluates the expression as a decimal number, and `complex(...)` makes it an ordinary Python number.

```python
fig, axes = plt.subplots(2, 4, figsize=(10.0, 5.6))
for l, ax in enumerate(axes.flat):
    signs = np.array([[np.sign(at_sample(Gam[l][m][n]).real) for n in range(8)]
                      for m in range(8)])
    ax.imshow(signs, cmap="RdBu_r", vmin=-1.5, vmax=1.5)
    ax.set_title(f"$\\Gamma^{{x{l + 1}}}{{}}_{{mn}}$", fontsize=9)
    ax.set_xticks(range(8), [f"{k + 1}" for k in range(8)], fontsize=7)
    ax.set_yticks(range(8), [f"{k + 1}" for k in range(8)], fontsize=7)
    ax.set_xlabel("$n$ (x-number)", fontsize=7)
    ax.set_ylabel("$m$ (x-number)", fontsize=7)
    ax.grid(False)
fig.suptitle("Signs of the Christoffel symbols at a sample point "
             "(red +, blue -, white 0)", fontsize=10)
fig.tight_layout()
```

`plt.subplots(2, 4)` makes eight small panels in two rows, one for each upper index `l`; `enumerate(axes.flat)` numbers them 0 to 7. For each panel an $8 \times 8$ table of the signs $+1$, $-1$ or $0$ of $\Gamma^l{}_{mn}$ at the sample point is computed (`np.sign`; `.real` takes the real part of the complex number) and drawn by `imshow` as a picture whose squares are coloured with the colour map `"RdBu_r"` (red for positive, blue for negative, white for zero). The tick labels number the rows and columns 1 to 8; `ax.grid(False)` removes the grid lines; `fig.suptitle` puts a title above all panels and `fig.tight_layout()` arranges them without overlap. In the title string the doubled braces `{{` and `}}` print single braces inside an f-string.

```python
save_figure(fig, "christoffel_pattern",
            "Where the Christoffel symbols $\\Gamma^l{}_{mn}$ of the author's metric "
            ...
            "grids are symmetric because $\\Gamma^l{}_{mn} = \\Gamma^l{}_{nm}$.")
```

The figure is saved; the cell prints the name of the saved file, `06a_3_christoffel_pattern.png`.

**What Figure 06a.3 shows.** Every coloured square lies in row 4 or 8, in column 4 or 8, or in a panel $l = 4$ or $l = 8$: every nonzero symbol carries an index $x4$ or $x8$, because the metric depends only on the time and on the hidden coordinate. Each grid is mirror-symmetric about its diagonal, because $\Gamma^l{}_{mn} = \Gamma^l{}_{nm}$. In the panels $l = x1, x2, x3$ the two squares with the index 4 are red ($a_4' > 0$: 3-space grows), and in the panels $l = x5, x6, x7$ they are blue ($-a_4'$: the extra times shrink). The panel $l = x4$ has red squares on the diagonal for all six warped directions, and the panel $l = x8$ has blue squares for 3-space, red squares for the extra times and one blue square at $(8, 8)$, as the signs derived in Section 6.3 say.

**In [11], the canonical spin connection** (Sections 6.4 and 6.6).

```python
omega = spin_connection(e, Gam, x, ETA)
postulate = [sp.diff(e[a, nu], x[mu])
             - sum(Gam[lam][mu][nu] * e[a, lam] for lam in range(8))
             + sum(ETA[a] * omega[mu][a][b] * e[b, nu] for b in range(8))
             for mu in range(8) for a in range(8) for nu in range(8)]
check(len(postulate) == 512 and all(is_zero(v) for v in postulate),
      "the vielbein postulate holds in all 512 components",
      record=f"{REPORT_PY}, check vielbein_postulate")
```

`omega` holds all $8^3 = 512$ components $\omega_{\mu ab}$. The list `postulate` holds the left side of the vielbein postulate for every $\mu$, $a$, $\nu$; the mixed components are recovered as $\omega_\mu{}^a{}_b = \eta_{aa}\omega_{\mu ab}$ (multiplying by $\eta_{aa}$ again undoes the lowering, because $\eta_{aa}^2 = 1$). The check requires 512 entries, all exactly zero.

```python
check(all(is_zero(omega[mu][a][b] + omega[mu][b][a])
          for mu in range(8) for a in range(8) for b in range(8)),
      "omega_mu ab = -omega_mu ba for all mu, a, b",
      record=f"{REPORT_PY}, check spin_connection_antisymmetric")
```

The antisymmetry $\omega_{\mu ab} + \omega_{\mu ba} = 0$, checked for all 512 triples.

```python
omega_nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a in range(8)
                 for b in range(a + 1, 8) if omega[mu][a][b] != 0}
for (mu, a, b), value in omega_nonzero.items():
    say(f"omega_{NAMES[mu]},{NAMES[a]}{NAMES[b]} = {value}")
```

The nonzero components with $a < b$ are collected and printed, one line each: twelve lines such as `omega_x1,x1x4 = exp(a4(x4))*sin(6*H*x8)**(1/6)*Derivative(a4(x4), x4)`, which is $a_4'e^{a_4}s$, exactly the table of Section 6.6.

```python
omega_record = {(int(m) - 1, int(a) - 1, int(b) - 1): v for m, a, b, v
                in record_formula("omega_nonzero", RECORD_NAMES)}
check(len(omega_nonzero) == 12 and set(omega_record) == set(omega_nonzero)
      and all(is_zero(omega_nonzero[k] - omega_record[k]) for k in omega_nonzero),
      "the 12 independent nonzero omega_mu ab equal the record",
      record=f"{THEORY_FILE}, formula omega_nonzero")
```

The record's list `omega_nonzero` (entries $\{\mu, a, b, \text{value}\}$) is read and renumbered; the check requires exactly 12 components, the same keys and the same values.

```python
a4p = sp.Derivative(a4, x4)
factors = {sp.exp(a4) * s, -sp.exp(a4) * s, sp.exp(-a4) * s, -sp.exp(-a4) * s}
# value / (c * phys) must simplify to exactly 1 for one choice of c and phys.
shape_ok = all(any(sp.simplify(value / (c * phys)) == 1 for c in (a4p, H)
                   for phys in factors) for value in omega_nonzero.values())
check(shape_ok, "every nonzero omega is a4' or H times +-exp(+-a4) sin^(1/6) z",
      record=f"{REPORT_WL}, check Omega_vanishes_iff_a4prime_and_H_vanish")
```

The last check makes the statement of Section 6.6 precise: for every nonzero component there is a choice of `c` (either $a_4'$ or $H$) and of `phys` (one of the four factors $\pm e^{\pm a_4}s$) such that the component divided by `c * phys` simplifies to exactly 1. `any(...)` is true when at least one choice works. The cell prints the twelve components and four PASS lines.

**In [12], figure 4.**

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6))
for ax, mu in zip(axes, (0, 4)):
    table = np.array([[at_sample(omega[mu][a][b]).real for b in range(8)]
                      for a in range(8)])
    limit = np.abs(table).max()
    image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
```

Two panels, for $\mu = x1$ (position 0) and $\mu = x5$ (position 4); `zip(axes, (0, 4))` pairs each panel with its $\mu$. `table` is the $8 \times 8$ array of the values $\omega_{\mu ab}$ at the sample point. The colour scale is symmetric, from minus to plus the largest absolute value `limit`, so that white means zero.

```python
    for a in range(8):
        for b in range(8):
            if table[a, b] != 0:
                ax.text(b, a, f"{table[a, b]:.2f}", ha="center", va="center",
                        fontsize=7)
```

Each nonzero value is written into its square with two decimals (`f"{...:.2f}"`), centred.

```python
    ax.set_xticks(range(8), NAMES, fontsize=8)
    ax.set_yticks(range(8), NAMES, fontsize=8)
    ax.set_xlabel("frame index $b$")
    ax.set_ylabel("frame index $a$")
    ax.set_title(f"$\\omega_{{x{mu + 1}\\,ab}}$ at the sample point")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.8)
fig.tight_layout()
```

The tick labels are the names $x1$ to $x8$, the axes are the frame indices $a$ (rows) and $b$ (columns), and each panel gets its own **colour bar** (`fig.colorbar`), the scale that translates colours into numbers.

```python
save_figure(fig, "omega_heat_maps",
            "The canonical spin connection $\\omega_{\\mu ab}$ of the diagonal "
            ...
            "3-space direction $x1$.")
```

The figure is saved; the cell prints the name of the saved file, `06a_4_omega_heat_maps.png`.

**What Figure 06a.4 shows.** For $\mu = x1$ the only nonzero squares are $(x1, x4) = 0.78$ and $(x1, x8) = 1.56$ with their mirror images $-0.78$ and $-1.56$: the antisymmetry. These numbers are $a_4'e^{a_4}s$ and $He^{a_4}s$ at the sample point, where $e^{a_4}s = e^{1/2}\sin^{1/6}(\pi/4) = 1.556$. For $\mu = x5$ the nonzero squares are $(x4, x5) = -0.29$ and $(x5, x8) = -0.57$ with their mirror images: $-a_4'e^{-a_4}s$ and $-He^{-a_4}s$, with $e^{-a_4}s = 0.572$. The extra time has the opposite signs of the 3-space direction and smaller values, because its factor $e^{-a_4}$ is smaller than $e^{a_4}$ when $a_4 > 0$.

**In [13], the spinor connection and the covariant constancy** (Section 6.7).

```python
Omega = spinor_connection(omega, S)  # eight 16 x 16 matrices
gup = curved_gammas(e, gamma)  # gamma^mu = gamma^a / f_a for mu = a
check(Omega[3] == Z16 and Omega[7] == Z16, "Omega_x4 = Omega_x8 = 0",
      record=f"{REPORT_PY}, check Omega_x4_and_Omega_x8_vanish")
```

`Omega` is the list of the eight matrices $\Omega_\mu$ and `gup` the list of the curved gammas, $\gamma^{(\mu)}/f_\mu$. The first check requires $\Omega_{x4}$ and $\Omega_{x8}$ to be the zero matrix.

```python
rotation_ok = all(matrix_is_zero(
    Omega[mu] * gamma[a] - gamma[a] * Omega[mu]
    + sum((ETA[a] * omega[mu][a][b] * gamma[b] for b in range(8)), Z16))
    for mu in range(8) for a in range(8))
check(rotation_ok, "[Omega_mu, gamma^a] = -omega_mu^a_b gamma^b for all 64 pairs",
      record=f"{REPORT_WL}, check S_rotates_gamma_with_omega")
```

The defining property $[\Omega_\mu, \gamma^a] + \sum_b\omega_\mu{}^a{}_b\gamma^b = 0$, with $\omega_\mu{}^a{}_b = \eta_{aa}\omega_{\mu ab}$, checked for all 64 pairs $(\mu, a)$.

```python
constancy_ok = all(matrix_is_zero(
    gup[nu].diff(x[mu]) + sum((Gam[nu][mu][lam] * gup[lam] for lam in range(8)), Z16)
    + Omega[mu] * gup[nu] - gup[nu] * Omega[mu])
    for mu in range(8) for nu in range(8))
check(constancy_ok, "D_mu gamma^nu = 0 for all 64 pairs (mu, nu)",
      record=f"{REPORT_PY}, check covariant_constancy_D_mu_gamma_nu")
```

The covariant constancy $D_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu, \gamma^\nu] = 0$, checked for all 64 pairs $(\mu, \nu)$ (`.diff(x[mu])` differentiates every entry of the matrix).

```python
say(f"Omega_x1 has {sum(1 for v in Omega[0] if v != 0)} nonzero entries of 256")
```

The last line counts the nonzero entries of $\Omega_{x1}$ and prints Omega_x1 has 32 nonzero entries of 256. Each generator $S^{ab} = \frac12\gamma^a\gamma^b$ is one half of a signed permutation matrix, with 16 nonzero entries, and the two generators of $\Omega_{x1}$ have them in different places: $16 + 16 = 32$.

**In [14], figure 5.**

```python
pattern_ok = True
for a in range(8):
    for b in range(a + 1, 8):
        boost = ETA[a] * ETA[b] == -1  # one space-like, one time-like direction
        want = S[a][b] if boost else -S[a][b]  # S^T = S (boost) or -S (rotation)
        pattern_ok = pattern_ok and S[a][b].T == want
check(pattern_ok, "S^ab is symmetric for the 16 boosts, antisymmetric for the 12 "
      "rotations")
```

For all 28 pairs $a < b$ the loop decides whether the pair is a boost ($\eta_{aa}\eta_{bb} = -1$) and requires `S[a][b].T` (the transpose) to equal $S^{ab}$ for a boost and $-S^{ab}$ for a rotation, as Section 6.7 proved.

```python
fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6))
for ax, mu in zip(axes, (0, 4)):
    table = np.array([[at_sample(v).real for v in row] for row in Omega[mu].tolist()])
    limit = np.abs(table).max()
    image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
    ax.set_xticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_yticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
    ax.set_xlabel("column (spinor component 1 to 16)")
    ax.set_ylabel("row (spinor component)")
    ax.set_title(f"$\\Omega_{{x{mu + 1}}}$ at the sample point")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.8)
fig.tight_layout()
```

Two heat maps, of $\Omega_{x1}$ and $\Omega_{x5}$ at the sample point (`.tolist()` gives the rows of the matrix, and `at_sample` evaluates each entry). The ticks label every third component, 1, 4, 7, 10, 13, 16.

```python
save_figure(fig, "spinor_connection_heat_maps",
            "The spinor connection $\\Omega_{x1}$ (left) and $\\Omega_{x5}$ (right) as "
            ...
            "components to the first eight and the last eight to the last eight.")
```

The figure is saved; the cell prints its PASS line and the saved file name.

**What Figure 06a.5 shows.** Each matrix has its colours only in the upper-left and the lower-right $8 \times 8$ blocks: a generator is a product of two gammas, an even product, and maps the first eight components to the first eight and the last eight to the last eight (the two chiral halves of Chapter 5). In each matrix one set of squares appears in mirror pairs of the same colour (a symmetric matrix, the boost part) and another in mirror pairs of opposite colours (an antisymmetric matrix, the rotation part). For $\Omega_{x1}$ the boost part carries $a_4'$ (entries $\pm0.39$) and the rotation part $H$ (entries $\pm0.78$); for $\Omega_{x5}$ the rotation part carries $a_4'$ and the boost part $H$ (entries $\pm0.14$ and $\pm0.29$).

**In [15], the contraction direction by direction** (Section 6.8).

```python
per_direction = []  # (alpha_mu, beta_mu) for mu = x1 ... x8
decomposed = True
for mu in range(8):
    M = (gup[mu] * Omega[mu]).applyfunc(sp.simplify)
    alpha = sp.simplify(-(M * gamma[3]).trace() / 16)  # coefficient of gamma^(x4)
    beta = sp.simplify((M * gamma[7]).trace() / 16)  # coefficient of gamma^(x8)
    decomposed = decomposed and matrix_is_zero(M - alpha * gamma[3] - beta * gamma[7])
    per_direction.append((alpha, beta))
    say(f"gamma^{NAMES[mu]} Omega_{NAMES[mu]} = ({alpha}) gamma^(x4) "
        f"+ ({beta}) gamma^(x8)")
```

For each $\mu$, `M` is the matrix $\gamma^\mu\Omega_\mu$ (no sum), simplified entry by entry (`applyfunc`). Its coefficients are read off with traces as in Section 6.8 (`.trace()` is the trace; `gamma[3]` is $\gamma^{(x4)}$ and `gamma[7]` is $\gamma^{(x8)}$), and `decomposed` stays true only if $M - \alpha\gamma^{(x4)} - \beta\gamma^{(x8)}$ is the zero matrix for every $\mu$. Each pair $(\alpha_\mu, \beta_\mu)$ is stored and printed: eight lines, the table of Section 6.8.

```python
table_record = record_formula("gammaOmega_per_direction", RECORD_NAMES)
check(decomposed and all(is_zero(per_direction[k][0] - table_record[k][1])
                         and is_zero(per_direction[k][1] - table_record[k][2])
                         for k in range(8)),
      "the eight terms gamma^mu Omega_mu (no sum) equal the record",
      record=f"{THEORY_FILE}, formula gammaOmega_per_direction")
```

The record's table `gammaOmega_per_direction` lists $\{\mu, \alpha_\mu, \beta_\mu\}$; the check compares all eight rows (`table_record[k][1]` is the record's $\alpha$, `[k][2]` its $\beta$).

```python
inflating = sp.simplify(sum(per_direction[k][0] for k in (0, 1, 2)))
deflating = sp.simplify(sum(per_direction[k][0] for k in (4, 5, 6)))
hidden = sp.simplify(sum(beta for _, beta in per_direction))
report("x4 part from the inflating x1, x2, x3", inflating)
report("x4 part from the deflating x5, x6, x7", deflating)
report("x8 part from all directions", hidden)
check(is_zero(inflating + deflating) and is_zero(hidden - 3 * H),
      "the x4 terms cancel (3a4'/2 - 3a4'/2 = 0); the x8 terms add to 3H",
      record=f"{REPORT_WL}, check gammaOmega_x4_terms_cancel")
```

The time parts of the three inflating directions (positions 0, 1, 2) and of the three deflating directions (positions 4, 5, 6) are added separately, and all eight hidden parts together. Three RESULT lines print $\frac32a_4'$, $-\frac32a_4'$ and $3H$, and the check requires the first two to cancel and the third to be $3H$.

```python
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
check(matrix_is_zero(slash - 3 * H * gamma[7])
      and record_passed(REPORT_LEAD, "gamma_Omega_equals_3H_gamma8"),
      "gamma^mu Omega_mu = 3 H gamma^(x8) exactly, for every a4 and H",
      record=f"{REPORT_LEAD}, check gamma_Omega_equals_3H_gamma8")
```

`slash` is the full sum $\sum_\mu\gamma^\mu\Omega_\mu$, and the last check requires it to be exactly $3H\gamma^{(x8)}$, for symbolic $H$ and symbolic $a_4$, and the lead's independent report to record the same. The cell prints eight lines, three PASS lines and three RESULT lines.

**In [16], figure 6.**

```python
alpha_units = [float(sp.simplify(alpha / sp.Derivative(a4, x4))) for alpha, _
               in per_direction]  # alpha_mu / a4'
beta_units = [float(sp.simplify(beta / H)) for _, beta in per_direction]  # beta / H
positions = np.arange(8)
```

The coefficients in units of $a_4'$ and of $H$, as ordinary decimal numbers (`float`): $\pm\frac12$ or 0. `positions` is the list 0 to 7, the places of the bars.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
colors = ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3 + ["gray"]
ax_left.bar(positions, alpha_units, color=colors, width=0.6)
ax_left.set_title(f"coefficient of $\\gamma^{{(x4)}}$ / $a_4'$: total "
                  f"{sum(alpha_units):g}")
ax_right.bar(positions, beta_units, color=colors, width=0.6)
ax_right.set_title(f"coefficient of $\\gamma^{{(x8)}}$ / $H$: total "
                   f"{sum(beta_units):g}")
```

Two bar charts with a common vertical axis (`sharey=True`); the bars of 3-space are red, of the extra times blue, of the time and the hidden direction gray. Each title shows the total (`:g` writes a number in its shortest form).

```python
for ax in (ax_left, ax_right):
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, NAMES)
    ax.set_xlabel("direction $\\mu$ of the term $\\gamma^\\mu\\Omega_\\mu$")
ax_left.set_ylabel("coefficient (in the unit named in the title)")
```

A black zero line, the direction names under the bars, and the axis labels.

```python
save_figure(fig, "gamma_omega_per_direction",
            "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the diagonal "
            ...
            "= 3H\\gamma^{(x8)}$.")
```

The figure is saved; the cell prints its file name.

**What Figure 06a.6 shows.** On the left, three red bars of height $+\frac12$ and three blue bars of height $-\frac12$: the time-direction terms of the inflating and the deflating directions cancel, total 0. On the right, six bars of height $\frac12$ all pointing up: the hidden-direction terms add, total 3. The gray directions $x4$ and $x8$ contribute nothing, because $\Omega_{x4} = \Omega_{x8} = 0$.

**In [17], the block form and figure 7.**

```python
I8, Z8 = sp.eye(8), sp.zeros(8, 8)  # 8 x 8 identity and zero matrices
blocks_ok = True
for entry in FORMULAS["field_equation_blocks"]:  # eight texts {"xa", tb, t}
    name, tb, t = json.loads(entry.replace("{", "[").replace("}", "]"))
    a = NAMES.index(name)  # the position of the direction xa (0 ... 7)
    # gamma^(xa) must be the block matrix with the zero blocks on the diagonal
    blocks_ok = blocks_ok and gamma[a] == sp.BlockMatrix(
        [[Z8, sp.Matrix(tb)], [sp.Matrix(t), Z8]]).as_explicit()
check(blocks_ok and len(FORMULAS["field_equation_blocks"]) == 8,
      "the eight gammas have the block form of the record",
      record=f"{THEORY_FILE}, formula field_equation_blocks")
check(gamma[7] == sp.BlockMatrix([[Z8, I8], [I8, Z8]]).as_explicit(),
      "gamma^(x8) has the 8 x 8 identity in its two off-diagonal blocks")
```

The record's formula `field_equation_blocks` is a list of eight texts $\{\text{"xa"}, \bar\tau, \tau\}$ written with curly brackets. Replacing the curly brackets by square brackets turns each text into JSON, which `json.loads` reads into a name and two $8 \times 8$ lists. `NAMES.index(name)` finds the position of the direction. `sp.BlockMatrix([[Z8, tb], [t, Z8]]).as_explicit()` builds the $16 \times 16$ matrix with zero blocks on the diagonal and the two blocks off it; the first check requires all eight gammas to have this form. The second requires $\gamma^{(x8)}$ to have the $8 \times 8$ identity in both off-diagonal blocks.

```python
panels = [
    ("sum over $x1, x2, x3$", sum((gup[k] * Omega[k] for k in (0, 1, 2)), Z16)),
    ("sum over $x5, x6, x7$", sum((gup[k] * Omega[k] for k in (4, 5, 6)), Z16)),
    ("total $\\gamma^\\mu\\Omega_\\mu$", slash),
    ("$3H\\gamma^{(x8)}$", 3 * H * gamma[7]),
]
```

The four matrices of the figure: the sum of the three inflating terms, the sum of the three deflating terms, the total and $3H\gamma^{(x8)}$, each with its title.

```python
fig, axes = plt.subplots(2, 2, figsize=(8.0, 7.6))
for ax, (title, matrix) in zip(axes.flat, panels):
    table = np.array([[at_sample(v).real for v in row] for row in matrix.tolist()])
    image = ax.imshow(table, cmap="RdBu_r", vmin=-3.5, vmax=3.5)
    ax.set_title(title, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.7, label="entry value")
```

A $2 \times 2$ grid of heat maps, all on the same colour scale from $-3.5$ to $3.5$, without tick marks, and one common colour bar.

```python
save_figure(fig, "gamma_omega_cancellation",
            "The cancellation as pictures of 16 x 16 matrices at the sample point "
            ...
            "two bottom pictures are identical.")
```

The figure is saved; the cell prints two PASS lines and the file name.

**What Figure 06a.7 shows.** The two upper pictures contain the same pattern of $\gamma^{(x8)}$ with the value $\frac32H = 1.5$ (two diagonal lines in the off-diagonal blocks), and on top of it the pattern of $\gamma^{(x4)}$ with entries $\pm\frac32a_4' = \pm0.75$, with opposite colours in the two pictures. In the total (lower left) the $\gamma^{(x4)}$ pattern is gone and the value on the two diagonal lines is 3; the lower right picture, $3H\gamma^{(x8)}$, is identical to it.

**In [18], the divergence form** (Section 6.9).

```python
anticommutes = all(matrix_is_zero(gup[mu] * Omega[mu] + Omega[mu] * gup[mu])
                   for mu in range(8))
check(anticommutes, "{gamma^mu, Omega_mu} = 0 for each mu separately",
      record=f"{REPORT_PY}, check anticommutator_gamma_Omega_vanishes")
```

Fact 1: $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each $\mu$ separately.

```python
sqrt_g = sp.cos(z)
divergence = sum(((sqrt_g * gup[mu]).diff(x[mu]) for mu in range(8)), Z16) / (2 * sqrt_g)
check(matrix_is_zero(divergence - 3 * H * gamma[7])
      and record_passed(REPORT_LEAD, "gamma_Omega_divergence_formula"),
      "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = 3 H gamma^(x8)",
      record=f"{REPORT_LEAD}, check gamma_Omega_divergence_formula")
```

`divergence` is $\frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)$ with $\sqrt{\lvert g\rvert} = \cos z$; the check requires it to equal $3H\gamma^{(x8)}$ and the lead's report to record the same.

```python
products = [sp.simplify(sp.prod([f[c] for c in range(8) if c != b])) for b in range(8)]
for b in (3, 7):
    say(f"product of the f_c with c != {NAMES[b]}: {products[b]}")
own_coordinate = [sp.simplify(sp.diff(products[b], x[b]) / (2 * sqrt_g))
                  for b in range(8)]
say(f"(1/(2 cos z)) d_b (product without b), b = x1 ... x8: {own_coordinate}")
check(own_coordinate == [0] * 7 + [3 * H],
      "only the hidden direction contributes, with 3 H")
```

Fact 2: `products[b]` is the product of the seven factors other than $f_b$. The two interesting ones are printed, `cos(6*H*x8)` for $b = x4$ and `sin(6*H*x8)` for $b = x8$. `own_coordinate` divides the derivative of each product with respect to its own coordinate by $2\cos z$; the printed list is `[0, 0, 0, 0, 0, 0, 0, 3*H]`, and the check requires exactly this: only the hidden direction contributes, with $3H$.

**In [19], central differences and figure 8.**

```python
H_value = 1.0
x8_values = np.linspace(0.002, np.pi / 12 - 0.002, 300)  # z = 6 x8 inside (0, pi/2)
step = 1e-5  # the step h of the central difference
```

Numbers instead of symbols: $H = 1$, 300 values of $x_8$ inside $(0, \pi/12)$ (so that $z = 6x_8$ lies inside $(0, \pi/2)$), and the step $h = 10^{-5}$.

```python
def hidden_product(x8_value):
    return np.sin(6 * H_value * x8_value)  # sqrt|g| e_(x8)^x8 = sin z
```

The density $\sqrt{\lvert g\rvert}\,e_{(x8)}{}^{x8} = \cos z\tan z = \sin z$ as a numerical function.

```python
derivative = (hidden_product(x8_values + step)
              - hidden_product(x8_values - step)) / (2 * step)
ratio = derivative / (2 * np.cos(6 * H_value * x8_values))  # should be 3 H = 3
time_term = np.zeros_like(x8_values)  # d/dx4 cos z = 0: the time contributes 0
report("largest |central difference - 3 H| over the grid",
       f"{np.max(np.abs(ratio - 3.0)):.1e}")
check(np.max(np.abs(ratio - 3.0)) < 1e-6, "the numerical derivative gives 3 H")
```

The **central difference** $\big(F(x_8 + h) - F(x_8 - h)\big)/(2h)$ approximates the derivative $F'(x_8)$ with an error of about $\frac{h^2}{6}F'''$; divided by $2\cos z$ it should be $3H = 3$. The time term is identically zero (the density $\cos z$ does not depend on $x_4$). The RESULT line prints the largest deviation from 3 over the grid, 1.9e-09, and the check requires it to be below $10^{-6}$. For $F = \sin 6x_8$ the error estimate is $\frac{h^2}{6}\cdot216\cos z/(2\cos z) = 18h^2 = 1.8 \times 10^{-9}$, the printed size.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
zz = 6 * H_value * x8_values
ax_left.plot(zz, np.sin(zz), label="$\\sqrt{|g|}\\,e_{(x8)}{}^{x8} = \\sin z$")
ax_left.plot(zz, np.cos(zz), "--",
             label="$\\sqrt{|g|}\\,e_{(x4)}{}^{x4} = \\cos z$ (no $x_4$)")
ax_left.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax_left.set_ylabel("density (pure number)")
ax_left.set_title("The two densities that could contribute")
ax_left.legend(fontsize=8)
```

The left panel draws the two densities $\sin z$ and $\cos z$ versus $z$.

```python
ax_right.plot(zz, ratio, label="hidden direction: $\\partial_{x8}\\sin z/(2\\cos z)$")
ax_right.plot(zz, time_term, "--", label="time direction: $\\partial_{x4}\\cos z = 0$")
ax_right.set_ylim(-0.5, 3.8)
ax_right.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax_right.set_ylabel("coefficient in units of $H$")
ax_right.set_title("Central differences: the constant $3H$")
ax_right.legend(fontsize=8, loc="center right")
```

The right panel draws the numerical coefficient (solid) and the zero time term (dashed).

```python
save_figure(fig, "divergence_form",
            "The divergence form of $\\gamma^\\mu\\Omega_\\mu$ with $H = 1$. Left: the "
            ...
            "$z$, and the time-direction coefficient is $0$ (dashed).")
```

The figure is saved; the cell prints the RESULT line, the PASS line and the file name.

**What Figure 06a.8 shows.** On the left, the hidden density $\sin z$ rises from 0 to 1 and the time density $\cos z$ falls from 1 to 0; only the first can contribute, because only it is differentiated with respect to its own coordinate in a nonzero way. On the right, the solid line is flat at 3 over the whole range of $z$: the coefficient of $\gamma^{(x8)}$ is the constant $3H$, and the dashed time coefficient is 0.

**In [20], the Dirac operator written out** (Section 6.10).

```python
import re  # text patterns, to rename the record's symbols

psi = sp.Matrix([sp.Function(f"psi{A}")(*x) for A in range(1, 17)])  # 16 functions
D = [psi.diff(x[mu]) + Omega[mu] * psi for mu in range(8)]  # D_mu Psi
dirac = sum((gup[mu] * D[mu] for mu in range(8)), sp.zeros(16, 1))
written_out = sum((gamma[a] * psi.diff(x[a]) / f[a] for a in range(8)),
                  sp.zeros(16, 1)) + 3 * H * gamma[7] * psi
check(all(is_zero(v) for v in dirac - written_out),
      "gamma^mu D_mu Psi = sum_a (1/f_a) gamma^a d_a Psi + 3 H gamma^(x8) Psi",
      record=f"{REPORT_WL}, check Dirac_operator_explicit_C")
```

`re` is Python's module for text patterns. `psi` is a column of sixteen unknown functions $\psi_1, \dots, \psi_{16}$ of all eight coordinates (`sp.Function(f"psi{A}")(*x)` makes the function named psi1, psi2, ... with the eight arguments). `D` is the list of the eight covariant derivatives $\partial_\mu\Psi + \Omega_\mu\Psi$, `dirac` is $\sum_\mu\gamma^\mu D_\mu\Psi$, and `written_out` is $\sum_a f_a^{-1}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x8)}\Psi$. The check requires the sixteen differences to vanish.

```python
# Rename the derivatives d psi_B / d x_k and then the functions psi_B as plain
# symbols dPsi<B>x<k> and Psi<B> (derivatives first: renaming psi_B first would
# turn its derivatives into derivatives of a constant symbol, which are zero).
rename_derivatives = {sp.Derivative(psi[B], x[k]):
                      sp.Symbol(f"dPsi{B + 1}x{k + 1}")
                      for B in range(16) for k in range(8)}
rename_functions = {psi[B]: sp.Symbol(f"Psi{B + 1}") for B in range(16)}
```

To compare with the record's sixteen equations, the derivatives $\partial\psi_B/\partial x_k$ are renamed as plain symbols `dPsi<B>x<k>` and the functions as `Psi<B>`. The order matters, as the comment says: renaming the functions first would turn their derivatives into derivatives of constants, which are zero.

```python
same = True
for A, equation in enumerate(FORMULAS["field_equation_components"]):
    left = equation.split("==")[0]  # the record: left side == V*Psi[A]
    left = left.replace(chr(34), "")  # chr(34) is the double-quote character
    # dd[x4, Psi[14]] (the derivative of Psi_14 by x4) becomes dPsi14x4:
    left = re.sub(r"dd\[x(\d), Psi\[(\d+)\]\]", r"dPsi\2x\1", left)
    left = re.sub(r"Psi\[(\d+)\]", r"Psi\1", left).replace("a4[x4]", "a4")
    record_left = parse_mathematica(left).subs(
        {sp.Symbol("H"): H, sp.Symbol("x8"): x8, sp.Symbol("a4"): a4},
        simultaneous=True)
    mine = dirac[A].subs(rename_derivatives).subs(rename_functions)
    same = same and is_zero(mine - record_left)
```

For each record equation (`enumerate` numbers them from 0) the text left of `==` is taken (the right side is $V\Psi_A$ and not needed). `chr(34)` is the double-quote character, which is removed. The pattern `dd\[x(\d), Psi\[(\d+)\]\]` matches texts such as `dd[x4, Psi[14]]`, the derivative of $\psi_{14}$ by $x_4$; `\d` is a digit, `\d+` one or more digits, the parentheses capture them, and `re.sub` replaces the match by `dPsi14x4` (`\2` and `\1` insert the captured numbers). The second pattern turns `Psi[9]` into `Psi9`. The text is read with `parse_mathematica`, its symbols are replaced by the notebook's, and the notebook's component `A` with the same renaming must agree with it exactly.

```python
check(same, "all 16 components of the Dirac operator equal the record",
      record=f"{THEORY_FILE}, formula field_equation_components")
check(gamma[7] * gamma[7] == I16 and record_passed(REPORT_PY,
                                                    "nontriviality_Omega_zero_iff_flat"),
      "(gamma^(x8))^2 = 1: the term 3 H gamma^(x8) Psi vanishes only for Psi = 0",
      record=f"{REPORT_WL}, checks nontriviality_1_dirac16complex and "
             "nontriviality_2_dirac16complex00")
```

The check of all sixteen components, and the non-triviality check: $(\gamma^{(x8)})^2 = 1$, so the term $3H\gamma^{(x8)}\Psi$ vanishes only for $\Psi = 0$, together with the record's checks for both fields. The cell prints three PASS lines with their records.

**In [21], figure 9.**

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
coefficient = [sp.lambdify(X4_SYMBOL, (1 / fa).subs(history).subs(
    {H: 1, x8: sp.pi / 24})) for fa in f]
```

The eight factors $1/f_a$ in front of the derivatives, as numerical functions of the time for the illustrative history, at $z = \pi/4$.

```python
ax_left.semilogy(times, coefficient[0](times),
                 label="$1/f_1 = e^{-a_4}/s$ (3-space derivatives)")
ax_left.semilogy(times, coefficient[4](times), "--",
                 label="$1/f_5 = e^{a_4}/s$ (extra-time derivatives)")
ax_left.semilogy(times, np.ones_like(times), ":", color="black",
                 label="$1/f_4 = 1$ (time derivative)")
ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$")
ax_left.set_ylabel("factor in front of the derivative (log axis)")
ax_left.set_title("Where the deflation enters the field equation")
ax_left.legend(fontsize=8)
```

The left panel, on a logarithmic axis: $1/f_1 = e^{-a_4}/s$ (solid), $1/f_5 = e^{a_4}/s$ (dashed) and $1/f_4 = 1$ (dotted).

```python
zz = np.linspace(0.05, np.pi / 2 - 0.15, 300)
ax_right.plot(zz, np.tan(zz), label="$1/f_8 = \\tan z$ (hidden derivative)")
ax_right.plot(zz, np.sin(zz) ** (-1 / 6), "--",
              label="$1/s = \\sin^{-1/6} z$ (warped directions, $a_4 = 0$)")
ax_right.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax_right.set_ylabel("factor (pure number)")
ax_right.set_title("Dependence on the hidden direction")
ax_right.legend(fontsize=8)
```

The right panel, versus $z$: $1/f_8 = \tan z$ and $1/s = \sin^{-1/6}z$; the range stops at $\pi/2 - 0.15$ because $\tan z$ grows without bound at $\pi/2$.

```python
save_figure(fig, "derivative_coefficients",
            "The factors $1/f_a$ in front of the derivatives in the Dirac operator "
            ...
            "the six warped directions.")
```

The figure is saved; the cell prints the file name.

**What Figure 06a.9 shows.** On the left the two warped factors are straight lines of opposite slope: the factor in front of the 3-space derivatives falls and the factor in front of the extra-time derivatives rises as $a_4$ grows. This is how the deflation of the extra times enters the field equation, although it does not enter $\gamma^\mu\Omega_\mu$. On the right, the hidden factor $\tan z$ rises steeply towards the patch end, while $\sin^{-1/6}z$ is large only very near the tip.

**In [22], the negative control** (Section 6.10).

```python
f_control = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(a4) * s] * 3 + [sp.cot(z)]
g_control = sp.diag(*[ETA[a] * f_control[a] ** 2 for a in range(8)])
e_control = sp.diag(*f_control)
Gam_control = christoffel(g_control, x)
omega_control = spin_connection(e_control, Gam_control, x, ETA)
Omega_control = spinor_connection(omega_control, S)
gup_control = curved_gammas(e_control, gamma)
slash_control = sum((gup_control[mu] * Omega_control[mu] for mu in range(8)), Z16)
```

The same computation for the control metric: the factors of the extra times are $e^{+a_4}s$ instead of $e^{-a_4}s$, and everything else (metric, vielbein, Christoffel symbols, spin connection, spinor connection, curved gammas, contraction) is computed by the same four functions.

```python
alpha_control = sp.simplify(-(slash_control * gamma[3]).trace() / 16)
beta_control = sp.simplify((slash_control * gamma[7]).trace() / 16)
report("control: coefficient of gamma^(x4)", alpha_control)
report("control: coefficient of gamma^(x8)", beta_control)
```

The two coefficients of the control contraction, found with traces, are printed: `3*Derivative(a4(x4), x4)` and `3*H`.

```python
lead = json.loads(repository_file(REPORT_LEAD).read_text(encoding="utf-8"))
detail = [c["detail"] for c in lead["checks"]
          if c["name"] == "negative_control_inflating_extra_times"][0]
```

The lead's report is read, and `detail` is the detail text of its check `negative_control_inflating_extra_times` (the list comprehension keeps the one matching check, and `[0]` takes it).

```python
check(matrix_is_zero(slash_control - alpha_control * gamma[3] - beta_control * gamma[7])
      and is_zero(alpha_control - 3 * sp.Derivative(a4, x4))
      and is_zero(beta_control - 3 * H)
      and "(3*Derivative(a4(x4), x4)) gamma^(x4)" in detail
      and record_passed(REPORT_LEAD, "negative_control_inflating_extra_times"),
      "control with inflating extra times: 3 a4' gamma^(x4) + 3 H gamma^(x8)",
      record=f"{REPORT_LEAD}, check negative_control_inflating_extra_times")
```

The check requires the control contraction to be exactly $3a_4'\gamma^{(x4)} + 3H\gamma^{(x8)}$ with nothing left over, the lead's detail text to contain the same coefficient, and the lead's check to be recorded as passed. The cell prints two RESULT lines and one PASS line.

**In [23], figure 10.**

```python
rates = np.linspace(-2.0, 2.0, 81)  # values of a4'
rate_symbol = sp.Symbol("rate")
author_alpha = sp.lambdify(rate_symbol, sp.simplify(sum(
    a for a, _ in per_direction)).subs(sp.Derivative(a4, x4), rate_symbol))
control_alpha = sp.lambdify(rate_symbol, alpha_control.subs(
    sp.Derivative(a4, x4), rate_symbol))
```

81 rates $a_4'$ from $-2$ to $2$. The total time coefficient of the author's metric ($0$) and of the control ($3a_4'$) become numerical functions of the rate (the derivative $a_4'$ is replaced by the plain symbol `rate`).

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
ax_left.plot(rates, np.broadcast_to(author_alpha(rates), rates.shape),
             label="author: deflating extra times")
ax_left.plot(rates, np.broadcast_to(control_alpha(rates), rates.shape), "--",
             label="control: inflating extra times")
ax_left.set_xlabel("rate $a_4'$ (units of $H$)")
ax_left.set_ylabel("coefficient of $\\gamma^{(x4)}$ (units of $H$)")
ax_left.set_title("The time-direction term")
ax_left.legend(fontsize=8)
```

The left panel: the author's coefficient (solid) and the control's (dashed) versus the rate. `np.broadcast_to` turns the author's constant 0 into a list of 81 zeros.

```python
ax_right.plot(rates, np.full_like(rates, float(hidden.subs(H, 1))),
              label="author: deflating extra times")
ax_right.plot(rates, np.full_like(rates, float(beta_control.subs(H, 1))), "--",
              label="control: inflating extra times")
ax_right.set_ylim(0.0, 4.0)
ax_right.set_xlabel("rate $a_4'$ (units of $H$)")
ax_right.set_ylabel("coefficient of $\\gamma^{(x8)}$ (units of $H$)")
ax_right.set_title("The hidden-direction term (identical lines)")
ax_right.legend(fontsize=8)
```

The right panel: the hidden coefficient $3H$ with $H = 1$ for both metrics (`np.full_like` makes a list of 81 equal values).

```python
save_figure(fig, "negative_control",
            "The negative control. Left: the coefficient of $\\gamma^{(x4)}$ in "
            ...
            "of the time-direction terms is caused by the deflation.")
```

The figure is saved; the cell prints the file name.

**What Figure 06a.10 shows.** On the left, the author's line lies flat on 0 for every rate, while the control's line rises through the origin with slope 3. On the right, the two lines lie on top of each other at 3. The deflation of the extra times is exactly what cancels the time-direction terms; the hidden-direction term does not care whether the extra times deflate or inflate.

**In [24], the last checks.**

```python
cited = {
    REPORT_PY: ["clifford_relations", "gammas_real", "metric_from_vielbein_equals_SPEC",
                "sqrt_det_g_equals_cos_z", "vielbein_postulate",
                "spin_connection_antisymmetric", "nontriviality_Omega_zero_iff_flat",
                "Omega_x4_and_Omega_x8_vanish", "covariant_constancy_D_mu_gamma_nu",
                "time_terms_cancel_hidden_term_survives",
                "gamma_mu_Omega_mu_equals_3H_gamma_x8",
                "anticommutator_gamma_Omega_vanishes", "divergence_of_sqrtg_gamma"],
    REPORT_WL: ["metric_is_the_authors", "sqrt_det_g_is_cos_z", "christoffel_count",
                "vielbein_postulate", "omega_antisymmetric", "omega_components",
                "Omega_components", "S_rotates_gamma_with_omega",
                "gamma_covariantly_constant", "gammaOmega_equals_3H_gamma_x8",
                "gammaOmega_x4_terms_cancel", "gammaOmega_divergence_form",
                "Dirac_operator_explicit_C", "Dirac_operator_explicit_G",
                "nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00",
                "Omega_vanishes_iff_a4prime_and_H_vanish", "block_form"],
    REPORT_LEAD: ["vielbein_reproduces_metric", "gamma_Omega_equals_3H_gamma8",
                  "gamma_Omega_divergence_formula",
                  "negative_control_inflating_extra_times"],
}
count = sum(len(names) for names in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names),
      f"the {count} cited record checks are recorded as passed")
```

`cited` lists, for each of the three reports, the checks that state a result reproduced in this notebook: 13 of the sympy report, 18 of the WolframScript report and 4 of the lead's report, 35 in all. The check requires every one of them to be recorded as passed, so that the record this notebook reproduces is itself a passing record.

```python
expected = [f"06a_{k}_{name}.png" for k, name in enumerate([
    "polar_frame_and_spin_rotation", "vielbein_factors", "christoffel_pattern",
    "omega_heat_maps", "spinor_connection_heat_maps", "gamma_omega_per_direction",
    "gamma_omega_cancellation", "divergence_form", "derivative_coefficients",
    "negative_control"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all ten figure files exist")
all_checks_passed()
```

The names of the ten figure files (`enumerate(..., 1)` numbers them from 1); the check requires all ten to exist, and `all_checks_passed()` prints the last line, ALL 34 CHECKS PASSED (notebook 06a).

### 6.15 Changing the frame: local spin covariance

Section 6.2 showed that the vielbein is a choice: for every point-dependent matrix $\Lambda(x)$ with $\Lambda^T\eta\Lambda = \eta$ the frame $e' = \Lambda e$ describes the same metric. Physics must not depend on this choice. This section derives how the spin connection, the spinor connection, the curved gammas and the contraction $\gamma^\mu\Omega_\mu$ change when the frame is changed. Matrices are written without indices: for each $\mu$, $\omega_\mu$ is the $8 \times 8$ matrix with the entries $\omega_\mu{}^a{}_b$ (row $a$, column $b$), and $e_\nu$ is the column of the eight numbers $e^a{}_\nu$.

**The spin connection of the new frame.** In this notation the vielbein postulate of Section 6.4 reads $\partial_\mu e_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}e_\lambda + \omega_\mu e_\nu = 0$. The new frame describes the same metric, so it has the same Christoffel symbols. Its postulate, with $e'_\nu = \Lambda e_\nu$:

$$
\partial_\mu(\Lambda e_\nu) - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}\Lambda e_\lambda + \omega'_\mu\Lambda e_\nu = (\partial_\mu\Lambda)e_\nu + \Lambda\Big(\partial_\mu e_\nu - \sum_\lambda\Gamma^\lambda{}_{\mu\nu}e_\lambda\Big) + \omega'_\mu\Lambda e_\nu
$$

(the product rule; $\Lambda$ taken out of the sum)

$$
= (\partial_\mu\Lambda)e_\nu - \Lambda\omega_\mu e_\nu + \omega'_\mu\Lambda e_\nu = 0
$$

(the old postulate replaces the bracket by $-\omega_\mu e_\nu$). The eight columns $e_\nu$ form an invertible matrix, so the matrix in front of them vanishes: $\partial_\mu\Lambda - \Lambda\omega_\mu + \omega'_\mu\Lambda = 0$, and multiplying from the right by $\Lambda^{-1}$:

$$
\omega'_\mu = \Lambda\,\omega_\mu\,\Lambda^{-1} - (\partial_\mu\Lambda)\Lambda^{-1} .
$$

The first term turns the old connection with the frame. The second term is new: it is the rate at which the frame is turned from point to point. The spin connection is not a tensor in its frame indices.

**The spinor connection of the new frame.** When the frame is turned by $\Lambda$, the spinor components change by a spin transformation $R(x)$ that **covers** $\Lambda$ (Chapter 5): $R^{-1}\gamma^aR = \sum_c\Lambda^a{}_c\gamma^c$ for every $a$, or, inverted, $R\gamma^cR^{-1} = \sum_d(\Lambda^{-1})^c{}_d\gamma^d$. The new components are $\Psi' = R\Psi$. Covariance demands that the covariant derivative of the new components be the new components of the covariant derivative, $D'_\mu(R\Psi) = R\,D_\mu\Psi$ for every $\Psi$. Write it out:

$$
\partial_\mu(R\Psi) + \Omega'_\mu R\Psi = (\partial_\mu R)\Psi + R\,\partial_\mu\Psi + \Omega'_\mu R\Psi \qquad\text{must equal}\qquad R\,\partial_\mu\Psi + R\,\Omega_\mu\Psi
$$

(the product rule on the left). The terms $R\,\partial_\mu\Psi$ agree, so $(\partial_\mu R)\Psi + \Omega'_\mu R\Psi = R\Omega_\mu\Psi$ for every $\Psi$, that is $\partial_\mu R + \Omega'_\mu R = R\Omega_\mu$, and multiplying from the right by $R^{-1}$:

$$
\Omega'_\mu = R\,\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1} .
$$

**Theorem (local spin covariance).** The canonical spinor connection of the frame $e' = \Lambda e$ is exactly this matrix. Proof, line by line. By the uniqueness of Section 6.7 it suffices to show that $X_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$ has the defining property with the new connection $\omega'_\mu$, and trace 0. First part of $X_\mu$:

$$
\begin{aligned}
[R\Omega_\mu R^{-1}, \gamma^a] &= R\,[\Omega_\mu, R^{-1}\gamma^aR]\,R^{-1} = \sum_c\Lambda^a{}_c\,R[\Omega_\mu, \gamma^c]R^{-1} \\
&= -\sum_{c,b}\Lambda^a{}_c\,\omega_\mu{}^c{}_b\,R\gamma^bR^{-1} = -\sum_d\big(\Lambda\omega_\mu\Lambda^{-1}\big)^a{}_d\gamma^d
\end{aligned}
$$

(multiply out both sides of the first equality; the covering relation; the defining property of $\Omega_\mu$; the inverted covering relation and the rule of matrix multiplication). Second part: differentiate the covering relation $R^{-1}\gamma^aR = \sum_c\Lambda^a{}_c\gamma^c$ with the product rule, using $\partial_\mu(R^{-1}) = -R^{-1}(\partial_\mu R)R^{-1}$ (differentiate $R^{-1}R = 1$):

$$
-R^{-1}(\partial_\mu R)R^{-1}\gamma^aR + R^{-1}\gamma^a\,\partial_\mu R = \sum_c(\partial_\mu\Lambda^a{}_c)\gamma^c .
$$

Multiply from the left by $R$ and from the right by $R^{-1}$:

$$
-(\partial_\mu R)R^{-1}\gamma^a + \gamma^a(\partial_\mu R)R^{-1} = \sum_c(\partial_\mu\Lambda^a{}_c)R\gamma^cR^{-1} = \sum_d\big((\partial_\mu\Lambda)\Lambda^{-1}\big)^a{}_d\gamma^d .
$$

The left side is $[-(\partial_\mu R)R^{-1}, \gamma^a]$. Adding the two parts:

$$
[X_\mu, \gamma^a] = -\sum_d\big(\Lambda\omega_\mu\Lambda^{-1} - (\partial_\mu\Lambda)\Lambda^{-1}\big)^a{}_d\gamma^d = -\sum_d\omega'_\mu{}^a{}_d\,\gamma^d .
$$

The trace of $R\Omega_\mu R^{-1}$ is that of $\Omega_\mu$, which is 0 ($\mathrm{tr}(ABA^{-1}) = \mathrm{tr}(BA^{-1}A)$). The trace of $(\partial_\mu R)R^{-1}$ is the derivative of $\ln\det R$, a standard fact of linear algebra (Jacobi's formula, quoted without proof here, ASSUMED), and $\det R = 1$ for every element of Pin(4,4) (Chapter 5), so it is 0. For the one frame change used below this trace is also computed directly. $\square$

**The curved gammas and the contraction.** The new inverse vielbein is $e'_a{}^\mu = \sum_c e_c{}^\mu(\Lambda^{-1})^c{}_a$ (the inverse of $\Lambda e$ is $e^{-1}\Lambda^{-1}$). Hence

$$
\gamma'^\mu = \sum_a e'_a{}^\mu\gamma^a = \sum_c e_c{}^\mu\sum_a(\Lambda^{-1})^c{}_a\gamma^a = \sum_c e_c{}^\mu\,R\gamma^cR^{-1} = R\,\gamma^\mu R^{-1}
$$

(the inverted covering relation). Multiply with $\Omega'_\mu$ and sum over $\mu$:

$$
\sum_\mu\gamma'^\mu\Omega'_\mu = \sum_\mu R\gamma^\mu R^{-1}\big(R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}\big) = R\Big(\sum_\mu\gamma^\mu\Omega_\mu\Big)R^{-1} - \sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}
$$

($R^{-1}R = 1$ in the first product; $R\gamma^\mu R^{-1} = \gamma'^\mu$ in the second). The first term only turns the old contraction; **the second term can change it completely**. The contraction $\gamma^\mu\Omega_\mu$ is **frame-dependent**.

| statement | status | where it is verified |
| --- | --- | --- |
| $\omega'_\mu = \Lambda\omega_\mu\Lambda^{-1} - (\partial_\mu\Lambda)\Lambda^{-1}$ | PROVED (above) | the boosted frame of Section 6.16: `python-scope.json` and `wolfram-scope.json`, check `boosted_frame_canonical_connection` |
| local spin covariance $\Omega'_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$, $\gamma'^\mu = R\gamma^\mu R^{-1}$ | PROVED (above, with Jacobi's formula quoted) | Notebook 06b checks both for all eight $\mu$ in the boosted frame, In [12] |

The two scope reports lie in `Revision/theory/reports`; they were written by two programs that share no code (a sympy program and a WolframScript program).

### 6.16 A boost in the plane of $x4$ and $x8$

**The boost.** Mix the time $x4$ (time-like) and the hidden direction $x8$ (space-like) with the **rapidity** $b$:

$$
e'^{(x4)} = \cosh b\;e^{(x4)} + \sinh b\;e^{(x8)}, \qquad e'^{(x8)} = \sinh b\;e^{(x4)} + \cosh b\;e^{(x8)},
$$

and keep the other six frame directions. Here $\cosh b = (e^b + e^{-b})/2$ and $\sinh b = (e^b - e^{-b})/2$ (Chapter 5), with $\cosh^2b - \sinh^2b = 1$. The matrix $\Lambda(b)$ is the identity except in the rows and columns of $x4$ and $x8$, where it is $\begin{pmatrix}\cosh b & \sinh b\\ \sinh b & \cosh b\end{pmatrix}$. In these two rows and columns $\eta$ is $\mathrm{diag}(-1, +1)$, and

$$
\Lambda^T\eta\Lambda = \begin{pmatrix}\cosh b & \sinh b\\ \sinh b & \cosh b\end{pmatrix}\begin{pmatrix}-\cosh b & -\sinh b\\ \sinh b & \cosh b\end{pmatrix}
$$

($\Lambda$ is symmetric, so $\Lambda^T = \Lambda$; and $\eta\Lambda$ is $\Lambda$ with the sign of its first row changed)

$$
= \begin{pmatrix}-\cosh^2b + \sinh^2b & -\cosh b\sinh b + \sinh b\cosh b\\ -\sinh b\cosh b + \cosh b\sinh b & -\sinh^2b + \cosh^2b\end{pmatrix} = \begin{pmatrix}-1 & 0\\ 0 & 1\end{pmatrix}
$$

(multiply row by column; then $\cosh^2 - \sinh^2 = 1$). So $\Lambda(b)$ keeps $\eta$ for every $b$, and $e' = \Lambda(b)e$ is a vielbein of the author's metric. A rotation moves a direction along a circle; a boost moves it along a **hyperbola**, keeping $t^2 - y^2$ (figure 06b.1). Now let the rapidity grow with the time,

$$
b = \beta x_4 + b_0 ,
$$

with two constants $\beta$ (the rate) and $b_0$ (the starting value).

**The spinor boost.** Put $X = \gamma^{(x4)}\gamma^{(x8)}$. Then

$$
X^2 = \gamma^{(x4)}\gamma^{(x8)}\gamma^{(x4)}\gamma^{(x8)} = -\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)}\gamma^{(x8)} = -(-1)(+1) = 1
$$

(exchange the two middle factors at the cost of a sign; then the Clifford relation twice). With $c = \cosh\frac b2$ and $s = \sinh\frac b2$ define $R = c - sX$; its inverse is $R^{-1} = c + sX$, because $(c - sX)(c + sX) = c^2 - s^2X^2 = c^2 - s^2 = 1$. Chapter 5 showed that $R$ is the spinor boost $\exp(-\frac b2X)$ in the plane $(x4, x8)$. $X$ anticommutes with $\gamma^{(x4)}$ and with $\gamma^{(x8)}$ (moving either through the product of two gammas meets one equal and one different factor: one sign) and commutes with the other six gammas (two signs). Hence $R^{-1}\gamma^cR = \gamma^c$ for the six other directions, and for $x4$:

$$
R^{-1}\gamma^{(x4)} = (c + sX)\gamma^{(x4)} = \gamma^{(x4)}(c - sX) = \gamma^{(x4)}R
$$

(move $\gamma^{(x4)}$ to the left through $X$ at the cost of a sign), so

$$
\begin{aligned}
R^{-1}\gamma^{(x4)}R &= \gamma^{(x4)}R^2 = \gamma^{(x4)}\big(c^2 + s^2 - 2cs\,X\big) \\
&= \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x4)}X = \cosh b\,\gamma^{(x4)} + \sinh b\,\gamma^{(x8)}
\end{aligned}
$$

(multiply out $(c - sX)^2$ with $X^2 = 1$; the half-angle formulas $c^2 + s^2 = \cosh b$ and $2cs = \sinh b$ of Chapter 5; and $\gamma^{(x4)}X = \gamma^{(x4)}\gamma^{(x4)}\gamma^{(x8)} = -\gamma^{(x8)}$). In the same way $R^{-1}\gamma^{(x8)}R = \gamma^{(x8)}(\cosh b - \sinh b\,X) = \sinh b\,\gamma^{(x4)} + \cosh b\,\gamma^{(x8)}$, using $\gamma^{(x8)}X = \gamma^{(x8)}\gamma^{(x4)}\gamma^{(x8)} = -\gamma^{(x4)}$. These are the two rows of $\Lambda(b)$: **$R$ covers the boost.**

**The contraction in the boosted frame.** By Section 6.15, $\sum_\mu\gamma'^\mu\Omega'_\mu = R(3H\gamma^{(x8)})R^{-1} - \sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}$. The first term, line by line:

$$
R\gamma^{(x8)} = (c - sX)\gamma^{(x8)} = \gamma^{(x8)}(c + sX) = \gamma^{(x8)}R^{-1},
$$

$$
R\gamma^{(x8)}R^{-1} = \gamma^{(x8)}(c + sX)^2 = \gamma^{(x8)}(\cosh b + \sinh b\,X) = \cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)}
$$

(the same steps as before). Call $v = \cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)}$; the first term is $3H\,v$. The second term: $R$ depends on $x_4$ only, through $b$, with $db/dx_4 = \beta$, so only $\mu = x4$ contributes:

$$
\partial_4R = \tfrac\beta2\big(s - cX\big), \qquad (\partial_4R)R^{-1} = \tfrac\beta2(s - cX)(c + sX) = \tfrac\beta2\big(sc + s^2X - c^2X - csX^2\big) = -\tfrac\beta2X
$$

(the chain rule, $\frac{d}{db}\cosh\frac b2 = \frac12\sinh\frac b2$ and $\frac{d}{db}\sinh\frac b2 = \frac12\cosh\frac b2$; multiply out; $X^2 = 1$, so $sc - cs = 0$ and $(s^2 - c^2)X = -X$). Its trace is 0, because $X$ is a product of two different gammas. With $\gamma'^{x4} = R\gamma^{(x4)}R^{-1} = \gamma^{(x4)}(\cosh b + \sinh b\,X) = \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x8)}$ (the same steps; $f_4 = 1$):

$$
\gamma'^{x4}(\partial_4R)R^{-1} = -\tfrac\beta2\big(\cosh b\,\gamma^{(x4)}X - \sinh b\,\gamma^{(x8)}X\big) = -\tfrac\beta2\big(-\cosh b\,\gamma^{(x8)} + \sinh b\,\gamma^{(x4)}\big) = \tfrac\beta2\,v
$$

($\gamma^{(x4)}X = -\gamma^{(x8)}$ and $\gamma^{(x8)}X = -\gamma^{(x4)}$). Subtracting:

$$
\sum_\mu\gamma'^\mu\Omega'_\mu = 3H\,v - \tfrac\beta2\,v = \frac{6H - \beta}{2}\big(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)}\big) .
$$

At $\beta = b_0 = 0$ (no boost) this is $3H\gamma^{(x8)}$ again. **For the rate $\beta = 6H$ the contraction vanishes identically**, at every time and for every function $a_4$.

**But the spinor connection does not vanish.** For $\beta = 6H$: $\Omega'_{x4} = R\Omega_{x4}R^{-1} - (\partial_4R)R^{-1} = 0 + 3H\,X = 3H\gamma^{(x4)}\gamma^{(x8)}$, which is not zero; $\Omega'_{x_i} = R\Omega_{x_i}R^{-1}$ and $\Omega'_{x_t} = R\Omega_{x_t}R^{-1}$ are not zero because $R$ is invertible; only $\Omega'_{x8} = R\,0\,R^{-1} - 0 = 0$. In this frame the field equation $\sum_\mu\gamma'^\mu D'_\mu\Psi' = (m + U')\Psi'$ contains no term $\gamma'^\mu\Omega'_\mu\Psi'$ at all, although the spinor connection is present in seven of the eight directions. The canonical spin connection of the boosted frame has 13 independent nonzero components (Notebook 06b, In [7], COMPUTED exactly).

| statement | status | where it is verified |
| --- | --- | --- |
| the boosted frame gives the author's metric; its canonical connection obeys the vielbein postulate | PROVED | `python-scope.json` and `wolfram-scope.json`, checks `boosted_frame_reproduces_metric`, `boosted_frame_canonical_connection` |
| $\gamma'^\mu\Omega'_\mu = \frac{6H-\beta}{2}(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)})$ | PROVED | both scope reports, check `boosted_frame_gammaOmega_formula`; Notebook 06b, In [8] |
| for $\beta = 6H$ the contraction is zero, $\Omega'_\mu \neq 0$ for $\mu = x1, \dots, x7$ | PROVED | both scope reports, check `boosted_frame_gammaOmega_vanishes`; Notebook 06b, In [10] |
| $R$ covers the boost; the two pieces $3Hv$ and $\frac\beta2v$ | PROVED (above) | Notebook 06b, In [12] (its own checks) |

### 6.17 What no frame can remove: the curvature

Sections 6.5 and 6.16 taught the same lesson twice: the spin connection, and even its contraction, can look different, or vanish, in another frame. What does not depend on the frame is **curvature**.

**The Riemann and Ricci tensors.** Chapter 3 defined the Riemann tensor

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \sum_\lambda\big(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}\big),
$$

the Ricci tensor $R_{\sigma\nu} = \sum_\rho R^\rho{}_{\sigma\rho\nu}$, its mixed form $R^\mu{}_\nu = \sum_\sigma g^{\mu\sigma}R_{\sigma\nu}$ and the Ricci scalar $R = \sum_\mu R^\mu{}_\mu$. A space is flat exactly when the Riemann tensor vanishes everywhere.

**One component by hand: $R^{x8}{}_{x8} = -6H^2$.** Put $\sigma = \nu = x8$ in the Ricci tensor and use the Christoffel symbols of Section 6.3. Write $u = \partial_8\ln\cos z$ and $v = \Gamma^{x8}{}_{x8x8}$, and note that $\sum_\rho\Gamma^\rho{}_{\rho8} = \partial_8\ln\sqrt{\lvert g\rvert} = u$ (Section 6.9). The four terms of $R_{88} = \sum_\rho R^\rho{}_{8\rho8}$ are:

$$
\sum_\rho\partial_\rho\Gamma^\rho{}_{88} = \partial_8v
$$

(the only nonzero $\Gamma^\rho{}_{88}$ is $\rho = x8$; $\Gamma^{x4}{}_{88} = 0$ because $f_8$ does not depend on $x_4$);

$$
-\partial_8\sum_\rho\Gamma^\rho{}_{\rho8} = -\partial_8u
$$

(the contracted symbol);

$$
\sum_{\rho,\lambda}\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{88} = u\,v
$$

(only $\lambda = x8$ has $\Gamma^\lambda{}_{88} \neq 0$);

$$
-\sum_{\rho,\lambda}\Gamma^\rho{}_{8\lambda}\Gamma^\lambda{}_{\rho8} = -\big(6H^2\cot^2z + v^2\big)
$$

($\Gamma^\rho{}_{8\lambda}$ is nonzero only for $\rho = \lambda$: $H\cot z$ for the six warped directions and $v$ for $x8$; each gives its square). With $\partial_8 = 6H\frac{d}{dz}$ (the chain rule), $u = -6H\tan z$, $\partial_8u = -36H^2/\cos^2z$, $v = -6H(\tan z + \cot z)$ (Section 6.3, written with $\frac{1}{\sin z\cos z} = \tan z + \cot z$) and $\partial_8v = -36H^2\big(\frac{1}{\cos^2z} - \frac{1}{\sin^2z}\big)$ (the derivatives of $\tan z$ and $\cot z$ are $1/\cos^2z$ and $-1/\sin^2z$):

$$
R_{88} = -36H^2\Big(\frac{1}{\cos^2z} - \frac{1}{\sin^2z}\Big) + \frac{36H^2}{\cos^2z} + 36H^2\tan z(\tan z + \cot z) - 6H^2\cot^2z - 36H^2(\tan z + \cot z)^2
$$

(insert the four terms; $uv = (-6H\tan z)(-6H)(\tan z + \cot z)$)

$$
= \frac{36H^2}{\sin^2z} + 36H^2\tan^2z + 36H^2 - 6H^2\cot^2z - 36H^2\big(\tan^2z + 2 + \cot^2z\big)
$$

(the terms with $1/\cos^2z$ cancel; $\tan z\cot z = 1$; multiply out the square)

$$
= \frac{36H^2}{\sin^2z} - 36H^2 - 42H^2\cot^2z = 36H^2(1 + \cot^2z) - 36H^2 - 42H^2\cot^2z = -6H^2\cot^2z
$$

(the $\tan^2z$ terms cancel; $1/\sin^2z = 1 + \cot^2z$, which is $\sin^2 + \cos^2 = 1$ divided by $\sin^2z$). Finally $R^{x8}{}_{x8} = g^{88}R_{88} = \tan^2z\cdot(-6H^2\cot^2z) = -6H^2$. It is negative for every $H > 0$ and every function $a_4$: **the author's metric is never flat.**

**All Ricci components.** The same computation for every component gives the record's values

$$
R^{x_i}{}_{x_i} = a_4'' - 6H^2,\qquad R^{x4}{}_{x4} = 6a_4'^2,\qquad R^{x_t}{}_{x_t} = -a_4'' - 6H^2,\qquad R^{x8}{}_{x8} = -6H^2,
$$

and the Ricci scalar $R = 3(a_4'' - 6H^2) + 6a_4'^2 + 3(-a_4'' - 6H^2) - 6H^2 = 6(a_4'^2 - 7H^2)$ (add the eight components; the $a_4''$ terms cancel). The component $R^{x4}{}_{x4} = 6a_4'^2$ is curvature made entirely by the inflation of 3-space and the deflation of the extra times, **although $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$ does not contain $a_4$ at all**: the contraction is blind to the deflation, the metric is not.

**The curvature of the spinor connection.** The commutator of two covariant derivatives of a spinor, line by line:

$$
D_\mu D_\nu\Psi = \partial_\mu\big(\partial_\nu\Psi + \Omega_\nu\Psi\big) + \Omega_\mu\big(\partial_\nu\Psi + \Omega_\nu\Psi\big) = \partial_\mu\partial_\nu\Psi + (\partial_\mu\Omega_\nu)\Psi + \Omega_\nu\partial_\mu\Psi + \Omega_\mu\partial_\nu\Psi + \Omega_\mu\Omega_\nu\Psi
$$

(the definition twice; the product rule). Subtract the same with $\mu$ and $\nu$ exchanged: $\partial_\mu\partial_\nu\Psi$ and the two middle terms are symmetric and cancel, and

$$
\big(D_\mu D_\nu - D_\nu D_\mu\big)\Psi = F_{\mu\nu}\Psi, \qquad F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu] .
$$

**Theorem (quoted, and checked exactly for this metric).** $F_{\mu\nu} = \frac12\sum_{a,b}R_{ab\mu\nu}S^{ab}$, where $R_{ab\mu\nu}$ is the Riemann tensor with its first two indices turned into frame indices (for the diagonal vielbein $R_{ab\mu\nu} = \eta_{aa}f_a R^a{}_{b\mu\nu}/f_b$). The general proof is a standard but long computation that this book does not reproduce; for the author's metric the identity is PROVED by exact computation in all 28 coordinate planes (`python-field-theory.json`, check `spinor_curvature_equals_riemann`; `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann`; Notebook 06b, In [15]). The spinor curvature is the Riemann curvature acting on spinors.

**It cannot be removed by a change of frame.** By Section 6.15, $D'_\mu(R\Psi) = R\,D_\mu\Psi$ for every spinor. Apply it twice, the second time to the spinor $D_\nu\Psi$: $D'_\mu D'_\nu(R\Psi) = D'_\mu(R\,D_\nu\Psi) = R\,D_\mu D_\nu\Psi$. Subtracting the same with $\mu$ and $\nu$ exchanged gives $F'_{\mu\nu}R\Psi = R\,F_{\mu\nu}\Psi$ for every $\Psi$, so

$$
F'_{\mu\nu} = R\,F_{\mu\nu}\,R^{-1} .
$$

An invertible $R$ can change the entries of $F_{\mu\nu}$ but cannot make a nonzero matrix zero. If some frame had $\Omega'_\mu = 0$ for all $\mu$, its $F'_{\mu\nu}$ would vanish, hence $F_{\mu\nu}$ in every frame, hence the Riemann tensor, which contradicts $R^{x8}{}_{x8} = -6H^2$. **No frame makes the spin connection vanish.** In the diagonal vielbein 27 of the 28 planes have $F_{\mu\nu} \neq 0$ at the sample point; the plane $(x4, x8)$ has $F_{x4\,x8} = 0$ exactly, because $\Omega_{x4} = \Omega_{x8} = 0$ make every term of its formula vanish (Notebook 06b, In [16], and figure 5). In the boosted frame with $\beta = 6H$, where the contraction vanished, $F'_{x1\,x8} = RF_{x1\,x8}R^{-1}$ is not zero (In [15]).

| statement | status | where it is verified |
| --- | --- | --- |
| the eight Ricci components and $R = 6(a_4'^2 - 7H^2)$ | PROVED ($R^{x8}{}_{x8}$ by hand above) | `field-theory.json`, formulas `ricci_mixed_diagonal`, `ricci_scalar`; `wolfram-field-theory.json`, checks `ricci_mixed_components`, `ricci_scalar` |
| never flat for $H > 0$: $R^{x8}{}_{x8} = -6H^2$ | PROVED | `wolfram-field-theory.json`, check `never_flat_for_H_positive`; `python-field-theory.json`, check `curvature_nonzero_flat_only_formally` |
| $\gamma^\mu\Omega_\mu$ contains no $a_4$, while $R^{x4}{}_{x4} = 6a_4'^2$ | PROVED | both scope reports, check `gammaOmega_blind_to_the_deflation` |
| $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$ in all 28 planes | PROVED for this metric (general theorem quoted) | `python-field-theory.json`, check `spinor_curvature_equals_riemann`; `wolfram-field-theory.json`, check `spin_curvature_equals_Riemann` |
| $F' = RFR^{-1}$; in the boosted frame $F'_{x1\,x8} \neq 0$ | PROVED | both scope reports, check `boosted_frame_curvature_nonzero` |

### 6.18 Changing the field variable: the rescaling $\Psi = \sin^{-1/2}(z)\,\chi$

A frame change is one way to remove the term $3H\gamma^{(x8)}$; a change of the field variable is another. Keep the diagonal vielbein, and write the field as a known function times a new field,

$$
\Psi = w\,\chi, \qquad w = \sin^{-1/2}z .
$$

**The derivation.** By the product rule, $\partial_\mu(w\chi) = (\partial_\mu w)\chi + w\,\partial_\mu\chi$, so

$$
\sum_\mu\gamma^\mu D_\mu\Psi = w\sum_\mu\gamma^\mu\partial_\mu\chi + \Big(\sum_\mu\gamma^\mu\partial_\mu w + w\sum_\mu\gamma^\mu\Omega_\mu\Big)\chi
$$

($w$ is a number at each point and commutes with every matrix). Only $x_8$ appears in $w$, and $\gamma^{x8} = \tan z\,\gamma^{(x8)}$, so the bracket is $\big(\tan z\,\partial_8w + 3H\,w\big)\gamma^{(x8)}$. Now

$$
\partial_8\sin^{-1/2}z = -\tfrac12\sin^{-3/2}z\cdot\cos z\cdot 6H = -3H\cos z\,\sin^{-3/2}z
$$

(the power rule and the chain rule), and

$$
\tan z\,\partial_8w = \frac{\sin z}{\cos z}\big(-3H\cos z\,\sin^{-3/2}z\big) = -3H\sin^{-1/2}z = -3H\,w
$$

(cancel $\cos z$; $\sin z\cdot\sin^{-3/2}z = \sin^{-1/2}z$). The bracket is $(-3Hw + 3Hw)\gamma^{(x8)} = 0$:

$$
\sum_\mu\gamma^\mu D_\mu(w\chi) = w\sum_\mu\gamma^\mu\partial_\mu\chi .
$$

**The rescaled field equation.** The bilinear is $S[\Psi] = \Psi^\dagger C\Psi$; $w$ is real and positive, so $S[w\chi] = w^2\chi^\dagger C\chi = S[\chi]/\sin z$. For the potential $U = \frac\lambda2S^2$, $U'(S) = \lambda S$, and the field equation $\sum_\mu\gamma^\mu D_\mu\Psi = (m + \lambda S[\Psi])\Psi$ becomes, after division by $w$,

$$
\sum_\mu\gamma^\mu\partial_\mu\chi = \Big(m + \frac{\lambda\,S[\chi]}{\sin z}\Big)\chi .
$$

For $U = 0$ ($\lambda = 0$) the term $3H\gamma^{(x8)}$ is removed completely. For $U \neq 0$ it reappears in another form: as the coupling $\lambda S[\chi]/\sin z$, which depends on the hidden coordinate. What remains of gravity in the equation of $\chi$ are the vielbein factors $1/f_a$ in front of every derivative.

| statement | status | where it is verified |
| --- | --- | --- |
| $\sum_\mu\gamma^\mu D_\mu(w\chi) = w\sum_\mu\gamma^\mu\partial_\mu\chi$ for $w = \sin^{-1/2}z$ and any 16 functions $\chi$ | PROVED | `python-scope.json` and `wolfram-scope.json`, check `rescaling_removes_the_connection_term`; Notebook 06b, In [17] |
| $S[w\chi] = S[\chi]/\sin z$; the rescaled equation with $U = \frac\lambda2S^2$ | PROVED | both scope reports, check `rescaled_equation_quadratic_potential` |

### 6.19 Example: Notebook 06b

Notebook 06b checks Sections 6.15 to 6.18 with exact algebra. It rebuilds the tools of Notebook 06a (so that it runs on its own), recomputes the diagonal vielbein and its contraction $3H\gamma^{(x8)}$ as a control, builds the boost matrix and checks that it keeps $\eta$, and draws the boosted frame on its hyperbolas. It then computes the canonical spin connection of the boosted frame with a symbolic rate $\beta$ and starting value $b_0$, checks the vielbein postulate, the formula $\frac{6H-\beta}{2}(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)})$ and its vanishing at $\beta = 6H$, and explains it with the explicit spinor boost $R$. It computes the Riemann tensor, the Ricci components and the spinor curvature in all 28 planes, and finally the rescaling. It compares every result that the Revision record also contains with the record (mainly the two scope reports), draws six figures, needs no Rust, runs in about a minute and ends with the line ALL 26 CHECKS PASSED (notebook 06b).

<!-- NOTEBOOK 06b -->

### 6.22 Line-by-line walk-through of Notebook 06b

The notebook has 19 code cells, In [1] to In [19]; this section explains every line of every one of them. As in Section 6.14, a line `...` in a quoted figure cell stands for the remaining lines of a long caption, printed in full in Section 6.21.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 6.20. Its code is, line for line, the set-up code of Notebook 06a explained at the beginning of Section 6.14, with the single difference

```python
NOTEBOOK_ID = "06b"  # this notebook: chapter 06, example b
```

so that the figures are named `06b_<k>_<name>.png` and the captions file is `Revision/textbook/figures/06b.captions.json`. It prints one line, Set-up of notebook 06b complete: repository folder found, helpers defined.

**In [2], the tools.**

```python
import sys  # the Python system module (here: the stream of printed text)

# Jupyter sends printed text to the screen in pieces, about every 0.2 seconds.  The
# book's checking tool reads each PASS line together with its "reproduces" line, so
# the pieces must be the same in every run: send the printed text of a cell in one
# piece when the cell ends (or just before a figure), at the latest after 600 s.
if hasattr(sys.stdout, "flush_interval"):  # true inside Jupyter only
    sys.stdout.flush_interval = 600.0
```

The same setting of the output channel as in In [2] of Notebook 06a: inside Jupyter the printed text of a cell is sent in one piece, so that every PASS line arrives together with its "reproduces" line.

```python
import numpy as np  # decimal numbers for the plots
import sympy as sp  # exact algebra and calculus with symbols
from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation
```

numpy for the plots, sympy for the exact algebra, and sympy's reader of Wolfram notation.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
NAMES = fixture["coordinates"]  # ["x1", ..., "x8"]
ETA = fixture["eta"]  # +1 space-like, -1 time-like
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(x(a+1))
C = sp.Matrix(fixture["C"])  # the author's C (Dirac adjoint Psibar = Psi^dagger C)
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
```

The record `Revision/algebra/gammas.json` is read as in Notebook 06a: the direction names, the signs of $\eta$, and the eight gammas as exact matrices. New is `C`, the author's matrix $C = \gamma^{(x8)}\gamma^{(x1)}\gamma^{(x2)}\gamma^{(x3)}$ stored in the same record (Chapter 5); In [17] needs it for the bilinear $S = \Psi^\dagger C\Psi$. `I16, Z16 = ...` gives two names at once (the identity and the zero matrix).

```python
check(all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
          == (2 * ETA[a] if a == b else 0) * I16
          for a in range(8) for b in range(8)),
      "the 64 Clifford relations of the author's gammas")
S = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
     for a in range(8)]
```

The 64 Clifford relations (the same test as in Notebook 06a, In [2]) and the 64 generators $S^{ab}$.

```python
def is_zero(expr):
    """True when expr is exactly zero for all values of its symbols."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    if sp.cancel(sp.expand(expr.rewrite(sp.exp))) == 0:  # the fast route
        return True
    return sp.simplify(expr) == 0  # the slower general route
```

The exact zero test `is_zero`, explained in Section 6.14 (Notebook 06a, In [3]): first the fast route through exponential functions, then `simplify`; it never calls a nonzero expression zero.

```python
def matrix_is_zero(matrix):
    return all(is_zero(entry) for entry in matrix)


def record_passed(path, name):
    """True when the Revision report at path records the check name as passed."""
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in data["checks"]:
        if entry["name"] == name:
            return entry["verdict"].upper() == "PASS"
    raise KeyError(f"{path} has no check {name}")
```

`matrix_is_zero` applies the test to every entry, and `record_passed` reads a Revision report and says whether a check is recorded as passed; both as in Notebook 06a.

```python
SCOPE_PY = "Revision/theory/reports/python-scope.json"
SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
REPORT_PY = "Revision/theory/reports/python-field-theory.json"
REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
THEORY_FILE = "Revision/theory/field-theory.json"
```

The paths of the five records that this notebook reproduces: the two scope reports, the two field-theory reports and the formula file. The cell prints one PASS line.

**In [3], the four general formulas.** They are those of Notebook 06a, In [4], written a little more compactly; Section 6.14 explains them line by line.

```python
def christoffel(g, coords):
    """Gam[l][m][n] = (1/2) sum_r g^lr (d_m g_rn + d_n g_rm - d_r g_mn)."""
    n = len(coords)
    g_inv = g.inv()
    Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for k in range(m, n):
                value = sum(g_inv[l, r] * (sp.diff(g[r, k], coords[m])
                                           + sp.diff(g[r, m], coords[k])
                                           - sp.diff(g[m, k], coords[r]))
                            for r in range(n) if g_inv[l, r] != 0) / 2
                Gam[l][m][k] = Gam[l][k][m] = sp.simplify(value)
    return Gam
```

The Christoffel symbols; the one difference from Notebook 06a is that the line `Gam[l][m][k] = Gam[l][k][m] = sp.simplify(value)` stores the simplified symbol in both places at once.

```python
def spin_connection(e, Gam, coords, eta):
    """omega[mu][a][b] = eta_aa sum_nu e^a_nu (d_mu e_b^nu + Gam^nu_mu,lam e_b^lam)."""
    n = len(coords)
    E = e.inv()  # E[nu, b] = e_b^nu
    omega = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for a in range(n):
            for b in range(n):
                mixed = 0
                for nu in range(n):
                    if e[a, nu] == 0:
                        continue
                    mixed += e[a, nu] * (sp.diff(E[nu, b], coords[mu]) + sum(
                        Gam[nu][mu][lam] * E[lam, b] for lam in range(n)))
                omega[mu][a][b] = sp.simplify(eta[a] * mixed)
    return omega
```

The canonical spin connection with the first index lowered. Here it matters that the function accepts ANY vielbein matrix `e`, not only a diagonal one: In [7] gives it the boosted vielbein, which has off-diagonal entries in the rows and columns of $x4$ and $x8$, and then the inverse `E = e.inv()` and the sums over `nu` and `lam` really have several terms.

```python
def spinor_connection(omega, S):
    """Omega[mu] = sum_{a<b} omega_{mu ab} S^ab."""
    n = len(omega)
    size = S[0][0].shape[0]
    return [sum((omega[mu][a][b] * S[a][b] for a in range(n)
                 for b in range(a + 1, n) if omega[mu][a][b] != 0),
                sp.zeros(size, size)) for mu in range(n)]
```

The spinor connection $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$, as one list comprehension: for each $\mu$ a sum of matrices starting from the zero matrix.

```python
def curved_gammas(e, gammas):
    """gamma^mu = sum_a e_a^mu gamma^a."""
    E = e.inv()
    return [sum((E[mu, a] * gammas[a] for a in range(len(gammas))),
                sp.zeros(*gammas[0].shape)) for mu in range(len(gammas))]
```

The curved gammas, and one output line.

```python
say("defined: christoffel, spin_connection, spinor_connection, curved_gammas")
```

**In [4], the diagonal vielbein again (the control).**

```python
x = sp.symbols("x1:9", real=True)
x4, x8 = x[3], x[7]
H = sp.Symbol("H", positive=True)
a4 = sp.Function("a4")(x4)  # any function of the time
z = 6 * H * x8
s = sp.sin(z) ** sp.Rational(1, 6)
f = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3 + [sp.cot(z)]
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the author's metric
e = sp.diag(*f)  # the diagonal vielbein
```

The symbols, the factors, the author's metric and the diagonal vielbein, exactly as in Notebook 06a, In [7].

```python
Gam = christoffel(g, x)
omega = spin_connection(e, Gam, x, ETA)
Omega = spinor_connection(omega, S)
gup = curved_gammas(e, gamma)
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
```

The Christoffel symbols, the spin connection, the spinor connection, the curved gammas and the contraction of the diagonal vielbein.

```python
check(matrix_is_zero(slash - 3 * H * gamma[7]),
      "control: the diagonal vielbein gives gamma^mu Omega_mu = 3 H gamma^(x8)",
      record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
```

The control: the same code, with no boost, must give $3H\gamma^{(x8)}$. The check names the scope report's check `rescaling_removes_the_connection_term`, whose detail records this control value. The cell prints one PASS line with its record.

**In [5], the boost matrix** (Section 6.16).

```python
def boost(b):
    """The 8 x 8 boost matrix Lambda(b) in the plane of x4 (index 3) and x8 (7)."""
    L = sp.eye(8)
    L[3, 3], L[3, 7], L[7, 3], L[7, 7] = sp.cosh(b), sp.sinh(b), sp.sinh(b), sp.cosh(b)
    return L
```

`boost(b)` returns the $8 \times 8$ identity with the four entries of the rows and columns 3 ($x4$) and 7 ($x8$) replaced by $\cosh b$, $\sinh b$, $\sinh b$, $\cosh b$. The four assignments are made in one line (a tuple of four places receives a tuple of four values).

```python
b_symbol = sp.Symbol("b", real=True)  # a rapidity
eta_matrix = sp.diag(*ETA)
L_test = boost(b_symbol)
```

A symbolic rapidity `b_symbol`, the matrix $\eta$ as a diagonal matrix, and the boost with this rapidity.

```python
check(matrix_is_zero(L_test.T * eta_matrix * L_test - eta_matrix),
      "Lambda(b)^T eta Lambda(b) = eta for every rapidity b")
check(matrix_is_zero(L_test * boost(-b_symbol) - sp.eye(8)),
      "the inverse of the boost with rapidity b is the boost with -b")
```

Two checks for every rapidity: $\Lambda(b)^T\eta\Lambda(b) - \eta = 0$ (`.T` is the transpose), and $\Lambda(b)\Lambda(-b) = 1$, so the inverse boost is the boost with $-b$. The cell prints two PASS lines.

**In [6], figure 1.**

```python
fig, ax = plt.subplots(figsize=(6.4, 6.0))
rapidity = np.linspace(-1.4, 1.4, 200)
ax.plot(np.cosh(rapidity), np.sinh(rapidity), color="tab:blue", linewidth=1.0,
        label="unit hyperbola of the time direction: $t^2 - y^2 = 1$")
ax.plot(np.sinh(rapidity), np.cosh(rapidity), color="tab:orange", linewidth=1.0,
        label="unit hyperbola of the hidden direction: $y^2 - t^2 = 1$")
ax.plot([0, 2.2], [0, 2.2], ":", color="gray", label="light line $t = y$")
```

One square panel. 200 rapidities from $-1.4$ to $1.4$ trace the two unit hyperbolas: $(\cosh b, \sinh b)$, where $t^2 - y^2 = 1$ (blue), and $(\sinh b, \cosh b)$, where $y^2 - t^2 = 1$ (orange); the dotted diagonal is the **light line** $t = y$.

```python
for b_value, alpha in ((0.0, 1.0), (0.5, 0.7), (1.0, 0.45)):
    c_b, s_b = np.cosh(b_value), np.sinh(b_value)
    ax.annotate("", xy=(c_b, s_b), xytext=(0, 0), arrowprops=dict(
        arrowstyle="-|>", color="tab:blue", alpha=alpha, linewidth=1.6))
    ax.annotate("", xy=(s_b, c_b), xytext=(0, 0), arrowprops=dict(
        arrowstyle="-|>", color="tab:orange", alpha=alpha, linewidth=1.6))
    ax.text(c_b + 0.04, s_b - 0.12, f"$b = {b_value:g}$", fontsize=8,
            color="tab:blue")
    ax.text(s_b - 0.30, c_b + 0.06, f"$b = {b_value:g}$", fontsize=8,
            color="tab:orange")
```

For the rapidities $b = 0$, $0.5$ and $1$ two arrows are drawn from the origin with `annotate` (an annotation with an empty text and an arrow): the boosted time direction to $(\cosh b, \sinh b)$ and the boosted hidden direction to $(\sinh b, \cosh b)$, fainter for larger $b$ (`alpha` is the opacity). `ax.text` writes the value of $b$ next to each arrow tip (`{b_value:g}` writes the number in its shortest form).

```python
ax.set_xlim(-0.4, 2.3)
ax.set_ylim(-0.25, 2.3)
ax.set_aspect("equal")
ax.set_xlabel("component along $e^{(x4)}$ (time), $t$")
ax.set_ylabel("component along $e^{(x8)}$ (hidden direction), $y$")
ax.set_title("A boost moves the frame along hyperbolas")
ax.legend(fontsize=8, loc="upper left")
```

The axis ranges, equal units on both axes, the labels and the legend.

```python
save_figure(fig, "boost_hyperbolas",
            "A boost of the frame in the plane of the time $x4$ and the hidden "
            ...
            "and tilt symmetrically towards the light line $t = y$ (dotted).")
```

The figure is saved; the cell prints its file name.

**What Figure 06b.1 shows.** At $b = 0$ the two arrows point along the axes. As $b$ grows, the blue arrow (the time direction) moves along its hyperbola away from the horizontal axis and the orange arrow (the hidden direction) along its hyperbola away from the vertical axis: both tilt symmetrically towards the light line, and both get longer on the paper, while their $\eta$-lengths stay $-1$ and $+1$. They remain perpendicular in the sense of $\eta$ ($-\cosh b\sinh b + \sinh b\cosh b = 0$). A boost never brings the arrows back, unlike a rotation.

**In [7], the boosted vielbein and its spin connection.**

```python
beta, b0 = sp.symbols("beta b0", real=True)  # the rate and the start of the rapidity
b = beta * x4 + b0  # the rapidity grows with the time
L = boost(b)
e_boosted = L * e  # e'^a_mu = sum_c Lambda^a_c e^c_mu
```

Two symbols, the rate $\beta$ and the starting value $b_0$, and the rapidity $b = \beta x_4 + b_0$, which grows with the time. `e_boosted` is the matrix product $\Lambda(b)\,e$, the boosted vielbein $e'^a{}_\mu = \sum_c\Lambda^a{}_c e^c{}_\mu$.

```python
check(matrix_is_zero(e_boosted.T * eta_matrix * e_boosted - g),
      "the boosted vielbein gives the author's metric (64 entries)",
      record=f"{SCOPE_PY}, check boosted_frame_reproduces_metric")
```

The check computes all 64 entries of $e'^T\eta e'$ and compares them with the author's metric.

```python
omega_b = spin_connection(e_boosted, Gam, x, ETA)  # omega'_{mu ab}
postulate = [sp.diff(e_boosted[a, nu], x[mu])
             - sum(Gam[lam][mu][nu] * e_boosted[a, lam] for lam in range(8))
             + sum(ETA[a] * omega_b[mu][a][c] * e_boosted[c, nu] for c in range(8))
             for mu in range(8) for a in range(8) for nu in range(8)]
antisymmetric = all(is_zero(omega_b[mu][a][c] + omega_b[mu][c][a])
                    for mu in range(8) for a in range(8) for c in range(8))
check(all(is_zero(v) for v in postulate) and antisymmetric,
      "boosted vielbein: vielbein postulate (512) and antisymmetry of omega'",
      record=f"{SCOPE_PY}, check boosted_frame_canonical_connection")
```

The canonical spin connection of the boosted frame, computed by the general function (with the same Christoffel symbols `Gam`, because the metric is the same). Then the vielbein postulate in all 512 components and the antisymmetry, as in Notebook 06a, In [11], but with the boosted vielbein; one check for both. This is the slowest step of the notebook: every entry contains $\cosh$ and $\sinh$ of $\beta x_4 + b_0$, and sympy must simplify them.

```python
Omega_b = spinor_connection(omega_b, S)  # Omega'_mu
gup_b = curved_gammas(e_boosted, gamma)  # gamma'^mu
count_b = sum(1 for mu in range(8) for a in range(8) for c in range(a + 1, 8)
              if omega_b[mu][a][c] != 0)
say(f"nonzero components omega'_mu ab with a < b: {count_b}")
```

The boosted spinor connection $\Omega'_\mu$, the boosted curved gammas $\gamma'^\mu$, and the number of nonzero components $\omega'_{\mu ab}$ with $a < b$, printed: 13. The cell prints two PASS lines and this number.

**In [8], the contraction in the boosted frame.**

```python
slash_b = sum((gup_b[mu] * Omega_b[mu] for mu in range(8)), Z16)
formula = (6 * H - beta) / 2 * (sp.cosh(b) * gamma[7] - sp.sinh(b) * gamma[3])
check(matrix_is_zero(slash_b - formula),
      "gamma'^mu Omega'_mu = ((6H - beta)/2)(cosh b gamma^(x8) - sinh b gamma^(x4))",
      record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_formula")
```

`slash_b` is $\sum_\mu\gamma'^\mu\Omega'_\mu$, and `formula` the record's $\frac{6H-\beta}{2}(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)})$. The check requires them to be equal for symbolic $a_4$, $H$, $\beta$ and $b_0$.

```python
check(formula.subs({beta: 0, b0: 0}) == 3 * H * gamma[7],
      "with no boost (beta = b0 = 0) the formula is 3 H gamma^(x8)")
```

With $\beta = b_0 = 0$ the formula must give back $3H\gamma^{(x8)}$ (`.subs` with a dictionary replaces both symbols). Two PASS lines.

**In [9], figure 2.**

```python
times = np.linspace(-0.25, 0.25, 101)
t_symbol = sp.Symbol("t", real=True)
coefficient_x8 = (6 * H - beta) / 2 * sp.cosh(b)  # the coefficient of gamma^(x8)
coefficient_x4 = -(6 * H - beta) / 2 * sp.sinh(b)  # the coefficient of gamma^(x4)
```

101 times from $-0.25$ to $0.25$, a plain symbol `t` for the time, and the two coefficients of the formula: of $\gamma^{(x8)}$, $\frac{6H-\beta}{2}\cosh b$, and of $\gamma^{(x4)}$, $-\frac{6H-\beta}{2}\sinh b$.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
for rate, style in ((0, "-"), (3, "--"), (6, "-."), (9, ":")):
    values = {H: 1, beta: rate, b0: 0, x4: t_symbol}
    c8 = sp.lambdify(t_symbol, coefficient_x8.subs(values))
    c4 = sp.lambdify(t_symbol, coefficient_x4.subs(values))
    ax_left.plot(times, np.broadcast_to(c8(times), times.shape), style,
                 label=f"$\\beta = {rate}H$" if rate else "no boost")
    ax_right.plot(times, np.broadcast_to(c4(times), times.shape), style,
                  label=f"$\\beta = {rate}H$" if rate else "no boost")
```

For the four rates $\beta = 0, 3, 6, 9$ (with $H = 1$ and $b_0 = 0$, so $b = \beta x_4$), each with its own line style, the two coefficients become numerical functions of the time and are plotted, the first on the left and the second on the right. `np.broadcast_to` makes a constant into a list of 101 values (for $\beta = 6$ both coefficients are the constant 0, for $\beta = 0$ the $\gamma^{(x8)}$ coefficient is the constant 3). The label is "no boost" for the rate 0 (the number 0 counts as false in `if rate`).

```python
ax_left.set_title("coefficient of $\\gamma^{(x8)}$")
ax_right.set_title("coefficient of $\\gamma^{(x4)}$")
for ax in (ax_left, ax_right):
    ax.set_xlabel("time $x_4$ (units $1/H$), with $b = \\beta x_4$")
    ax.legend(fontsize=8)
ax_left.set_ylabel("coefficient in $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
```

Titles, axis labels and legends.

```python
save_figure(fig, "boosted_contraction",
            "The contraction $\\gamma'^\\mu\\Omega'_\\mu$ in the boosted vielbein with "
            ...
            "the same metric, a different frame, a different value.")
```

The figure is saved; the cell prints its file name.

**What Figure 06b.2 shows.** Without boost (solid) the coefficients are the constants 3 and 0: the value $3H\gamma^{(x8)}$ of the diagonal vielbein. For $\beta = 3H$ (dashed) the $\gamma^{(x8)}$ coefficient is about $1.5\cosh(3x_4)$, smaller and slightly curved, and a $\gamma^{(x4)}$ coefficient appears. For $\beta = 6H$ (dash-dotted) both coefficients are zero at every time. For $\beta = 9H$ (dotted) they change sign. The same metric, a different frame, a different value of $\gamma^\mu\Omega_\mu$.

**In [10], the rate $\beta = 6H$.**

```python
six_H = {beta: 6 * H}
slash_6H = slash_b.subs(six_H)
Omega_6H = [M.subs(six_H) for M in Omega_b]
nonzero = [NAMES[mu] for mu in range(8) if not matrix_is_zero(Omega_6H[mu])]
say(f"Omega'_mu is nonzero for mu = {nonzero}")
```

`six_H` replaces $\beta$ by $6H$; substituting after the computation is allowed, because the computation was done for every $\beta$. `nonzero` lists the directions $\mu$ whose $\Omega'_\mu$ is not the zero matrix and is printed: `['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']`.

```python
check(matrix_is_zero(slash_6H) and nonzero == NAMES[:7],
      "beta = 6H: gamma'^mu Omega'_mu = 0, Omega'_mu nonzero for x1 ... x7",
      record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_vanishes")
```

The check requires the contraction to vanish identically and $\Omega'_\mu$ to be nonzero exactly for $x1, \dots, x7$ (`NAMES[:7]` is the list of the first seven names). One line and one PASS line.

**In [11], figure 3.**

```python
def at_sample(expr):
    """The decimal value of expr at H = 1, b0 = 0, x4 = 1/6, z = pi/4, a4 = 1/2,
    a4' = 1/2, a4'' = 0 (derivatives replaced first, then a4, then x4)."""
    expr = sp.sympify(expr).subs(sp.Derivative(a4, (x4, 2)), 0)
    expr = expr.subs(sp.Derivative(a4, x4), sp.Rational(1, 2))
    expr = expr.subs(a4, sp.Rational(1, 2))
    expr = expr.subs({H: 1, b0: 0, x4: sp.Rational(1, 6), x8: sp.pi / 24})
    return float(sp.N(expr))
```

The sample point of this notebook: $H = 1$, $b_0 = 0$, $x_4 = \frac16$ (so that $b = 6Hx_4 = 1$), $z = \pi/4$, $a_4 = \frac12$, $a_4' = \frac12$, $a_4'' = 0$, with the derivatives replaced first (Section 6.14, In [10] of Notebook 06a, explains why). `float` gives an ordinary decimal number.

```python
def sample_table(matrix):
    return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])
```

`sample_table` turns a matrix into an array of its decimal values at the sample point.

```python
panels = [("$\\Omega'_{x4}$", Omega_6H[3]), ("$\\Omega'_{x1}$", Omega_6H[0]),
          ("$\\gamma'^\\mu\\Omega'_\\mu$ (all zero)", slash_6H)]
tables = [sample_table(M) for _, M in panels]
```

The three matrices of the figure: $\Omega'_{x4}$, $\Omega'_{x1}$ and the contraction, and their tables.

```python
fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6))
for ax, (title, _), table in zip(axes, panels, tables):
    limit = max(np.abs(table).max(), 1.0)  # each panel its own colour scale
    image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.8)
```

Three heat maps side by side, each with its own symmetric colour scale; `max(..., 1.0)` keeps the scale at least $\pm1$, so that the zero matrix is drawn white and not with an undefined scale.

```python
save_figure(fig, "boosted_connection_heat_maps",
            "The boosted vielbein with the rate $\\beta = 6H$ at the sample point "
            ...
            "zero matrix. The spinor connection is present, its contraction is not.")
```

The figure is saved.

```python
check(np.abs(tables[2]).max() < 1e-12 and np.abs(tables[0]).max() > 0.1,
      "at the sample point Omega'_x4 is nonzero and the contraction is zero")
```

A numerical check of what the picture shows: the largest entry of the contraction is below $10^{-12}$, and the largest entry of $\Omega'_{x4}$ is above 0.1. The cell prints the file name and one PASS line.

**What Figure 06b.3 shows.** The left panel, $\Omega'_{x4}$, is coloured, although $\Omega_{x4} = 0$ in the diagonal vielbein: in the boosted frame the frame turns with the time, at the rate $\beta = 6H$, and $\Omega'_{x4} = 3H\gamma^{(x4)}\gamma^{(x8)}$ (Section 6.16), a signed permutation matrix times 3 whose squares lie in the two diagonal blocks. The middle panel, $\Omega'_{x1}$, is coloured too. The right panel is white: the contraction of the two is the zero matrix. The spinor connection is present; its contraction is not.

**In [12], why: the explicit spinor boost** (Sections 6.15 and 6.16).

```python
X = gamma[3] * gamma[7]  # gamma^(x4) gamma^(x8)
check(X * X == I16, "X = gamma^(x4) gamma^(x8) squares to the identity")
R = sp.cosh(b / 2) * I16 - sp.sinh(b / 2) * X  # the spinor boost
R_inv = sp.cosh(b / 2) * I16 + sp.sinh(b / 2) * X
check(matrix_is_zero(R * R_inv - I16), "R R^-1 = 1")
```

$X = \gamma^{(x4)}\gamma^{(x8)}$ and the check $X^2 = 1$; the spinor boost $R = \cosh\frac b2 - \sinh\frac b2X$ and its inverse $\cosh\frac b2 + \sinh\frac b2X$, and the check $RR^{-1} = 1$.

```python
covers = all(matrix_is_zero(R_inv * gamma[a] * R
                            - sum((L[a, c] * gamma[c] for c in range(8)), Z16))
             for a in range(8))
check(covers, "R^-1 gamma^a R = Lambda^a_c gamma^c: R covers the boost")
```

The covering relation $R^{-1}\gamma^aR = \sum_c\Lambda^a{}_c\gamma^c$ for all eight $a$ (`L[a, c]` is $\Lambda^a{}_c$ for the rapidity $b = \beta x_4 + b_0$).

```python
gammas_turn = all(matrix_is_zero(gup_b[mu] - R * gup[mu] * R_inv) for mu in range(8))
connection_rule = all(matrix_is_zero(Omega_b[mu] - (R * Omega[mu] * R_inv
                                                   - R.diff(x[mu]) * R_inv))
                      for mu in range(8))
check(gammas_turn and connection_rule,
      "gamma'^mu = R gamma^mu R^-1 and Omega'_mu = R Omega_mu R^-1 - (d_mu R) R^-1")
```

The theorem of Section 6.15 for this boost: $\gamma'^\mu = R\gamma^\mu R^{-1}$ and $\Omega'_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$ for all eight $\mu$ (`R.diff(x[mu])` differentiates every entry of $R$).

```python
turned = R * (3 * H * gamma[7]) * R_inv
extra = sum((gup_b[mu] * R.diff(x[mu]) * R_inv for mu in range(8)), Z16)
direction = sp.cosh(b) * gamma[7] - sp.sinh(b) * gamma[3]
check(matrix_is_zero(turned - 3 * H * direction)
      and matrix_is_zero(extra - beta / 2 * direction),
      "R (3H g8) R^-1 = 3H v and extra term = (beta/2) v, v = cosh b g8 - sinh b g4")
```

The two pieces of the formula: `turned` is $R(3H\gamma^{(x8)})R^{-1}$ and `extra` is $\sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}$; with $v = \cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)}$ (`direction`), the check requires `turned` $= 3Hv$ and `extra` $= \frac\beta2v$, as derived by hand in Section 6.16. The cell prints five PASS lines.

**In [13], the Riemann and Ricci tensors** (Section 6.17).

```python
def riemann_component(r, sg, mu, nu):
    value = sp.diff(Gam[r][nu][sg], x[mu]) - sp.diff(Gam[r][mu][sg], x[nu])
    for lam in range(8):
        value += Gam[r][mu][lam] * Gam[lam][nu][sg] - Gam[r][nu][lam] * Gam[lam][mu][sg]
    return value
```

`riemann_component(r, sg, mu, nu)` is $R^r{}_{\sigma\mu\nu}$ by the formula of Section 6.17 (`sg` stands for $\sigma$).

```python
def is_nonzero(expr):
    """True when expr is not identically zero.  A value clearly different from zero
    at the sample point proves it (fast); otherwise the exact test decides."""
    if abs(at_sample(expr)) > 1e-9:
        return True
    return not is_zero(expr)
```

`is_nonzero(expr)` decides whether an expression is not identically zero. If its value at the sample point is clearly different from zero, that proves it at once (a function that is not zero at one point is not the zero function); otherwise the exact test decides.

```python
riemann = {}  # (r, sigma, mu, nu) -> R^r_sigma mu nu, only the nonzero ones
for r in range(8):
    for sg in range(8):
        for mu in range(8):
            for nu in range(mu + 1, 8):
                value = riemann_component(r, sg, mu, nu)
                if value != 0 and is_nonzero(value):
                    riemann[(r, sg, mu, nu)] = value
                    riemann[(r, sg, nu, mu)] = -value
report("nonzero components R^r_sigma mu nu with mu < nu", len(riemann) // 2)
```

All components with $\mu < \nu$ are computed (the others follow from the antisymmetry $R^\rho{}_{\sigma\nu\mu} = -R^\rho{}_{\sigma\mu\nu}$, which the two assignments use). `value != 0` first skips the components that are zero without any work. The RESULT line prints the number of nonzero components with $\mu < \nu$: 78 (`//` is division without remainder; the dictionary holds every component twice).

```python
ricci_mixed = [sum(riemann.get((r, a, r, a), 0) for r in range(8)) / g[a, a]
               for a in range(8)]  # R^a_a = g^aa R_aa
names = {"H": H, "a4p": sp.Derivative(a4, x4), "a4pp": sp.Derivative(a4, (x4, 2))}
FORMULAS = {item["key"]: item["wl"] for item in json.loads(
    repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
```

The mixed Ricci components $R^a{}_a = g^{aa}\sum_r R^r{}_{ara}$ (dividing by $g_{aa}$ is multiplying by $g^{aa}$; `riemann.get(key, 0)` gives 0 for a missing key). Then the names under which the record writes $H$, $a_4'$ and $a_4''$, and the formulas of the record, as in Notebook 06a.

```python
def record_formula(key):
    text = FORMULAS[key]
    for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                  ("Derivative[2][a4][x4]", "a4pp")):
        text = text.replace(long_form, short_form)
    return parse_mathematica(text).subs(
        {sp.Symbol(k): v for k, v in names.items()}, simultaneous=True)
```

`record_formula(key)` reads one formula of the record, as in Notebook 06a, In [3], here with the fixed dictionary `names`.

```python
ricci_record = record_formula("ricci_mixed_diagonal")
check(all(is_zero(ricci_mixed[a] - ricci_record[a]) for a in range(8)),
      "the eight Ricci components R^mu_mu equal the record",
      record=f"{THEORY_FILE}, formula ricci_mixed_diagonal")
for a in range(8):
    say(f"R^{NAMES[a]}_{NAMES[a]} = {ricci_record[a]}")
```

The check compares the eight Ricci components with the record's `ricci_mixed_diagonal`, and the loop prints them: $-6H^2 + a_4''$ three times, $6a_4'^2$, $-6H^2 - a_4''$ three times and $-6H^2$.

```python
ricci_scalar = sum(ricci_mixed)
check(is_zero(ricci_scalar - record_formula("ricci_scalar")),
      "the Ricci scalar R = 6 (a4'^2 - 7 H^2) equals the record",
      record=f"{THEORY_FILE}, formula ricci_scalar")
```

The Ricci scalar is the sum of the eight mixed components, compared with the record's $6(a_4'^2 - 7H^2)$.

```python
a4_free = all(sp.diff(entry, sp.Derivative(a4, x4)) == 0 and not entry.has(a4)
              for entry in slash)
check(a4_free and is_zero(ricci_mixed[7] + 6 * H**2)
      and is_zero(ricci_mixed[3] - 6 * sp.Derivative(a4, x4) ** 2),
      "gamma^mu Omega_mu contains no a4, but R^x4_x4 = 6 a4'^2; R^x8_x8 = -6 H^2",
      record=f"{SCOPE_PY}, check gammaOmega_blind_to_the_deflation")
```

The last check: no entry of the contraction `slash` of In [4] contains $a_4$ or $a_4'$ (`sp.diff(entry, ...) == 0` and `not entry.has(a4)`), while $R^{x8}{}_{x8} = -6H^2$ and $R^{x4}{}_{x4} = 6a_4'^2$. The cell prints one RESULT line, eight component lines and three PASS lines.

**In [14], figure 4.**

```python
rate_symbol, accel_symbol = sp.symbols("rate accel", real=True)
numeric = [sp.lambdify((rate_symbol, accel_symbol), ricci_record[a].subs(
    {H: 1, sp.Derivative(a4, (x4, 2)): accel_symbol,
     sp.Derivative(a4, x4): rate_symbol})) for a in range(8)]
```

The eight Ricci components as numerical functions of two plain symbols, the rate $a_4'$ and the acceleration $a_4''$, with $H = 1$.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
values = [float(numeric[a](0.5, 0.0)) for a in range(8)]
colors = ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3 + ["black"]
ax_left.bar(range(8), values, color=colors, width=0.6)
ax_left.axhline(0.0, color="black", linewidth=0.8)
ax_left.set_xticks(range(8), [f"$R^{{{n}}}{{}}_{{{n}}}$" for n in NAMES], fontsize=8)
ax_left.set_ylabel("value (units of $H^2$)")
ax_left.set_title("Ricci components at $a_4' = 1/2$, $a_4'' = 0$")
```

The left panel: a bar chart of the eight components at $a_4' = \frac12$, $a_4'' = 0$, coloured by kind (red 3-space, gray time, blue extra times, black hidden direction), with labels such as $R^{x1}{}_{x1}$ under the bars.

```python
rates = np.linspace(-3.0, 3.0, 121)
for a, label, style in ((7, "$R^{x8}{}_{x8} = -6H^2$", "-"),
                        (3, "$R^{x4}{}_{x4} = 6a_4'^2$", "--"),
                        (0, "$R^{x1}{}_{x1} = a_4'' - 6H^2$", ":")):
    ax_right.plot(rates, np.broadcast_to(numeric[a](rates, 0.0), rates.shape),
                  style, label=label)
ax_right.axhline(0.0, color="black", linewidth=0.8)
ax_right.set_xlabel("rate $a_4'$ (units of $H$), with $a_4'' = 0$")
ax_right.set_ylabel("value (units of $H^2$)")
ax_right.set_title("Never flat: $R^{x8}{}_{x8} = -6H^2$")
ax_right.legend(fontsize=8)
```

The right panel: three components versus the rate $a_4'$ from $-3$ to $3$ with $a_4'' = 0$: $R^{x8}{}_{x8}$ (solid), $R^{x4}{}_{x4}$ (dashed) and $R^{x1}{}_{x1}$ (dotted).

```python
save_figure(fig, "ricci_components",
            "The mixed Ricci components $R^\\mu{}_\\mu$ of the author's metric in "
            ...
            "dotted line lies on the solid one because $a_4^{\\prime\\prime} = 0$).")
```

The figure is saved; the cell prints its file name.

**What Figure 06b.4 shows.** On the left, the six warped bars and the hidden bar lie at $-6$ (with $a_4'' = 0$ the 3-space and extra-time components are both $-6H^2$), while the time bar is $6 \cdot \frac14 = 1.5$. On the right, the solid line is flat at $-6$ for every rate: the hidden component is negative for every history, so the metric is never flat. The dashed parabola $6a_4'^2$ is curvature made by the inflation and deflation alone; it vanishes only for a constant $a_4$. The dotted line lies on the solid one because $a_4'' = 0$.

**In [15], the spinor curvature** (Section 6.17).

```python
def spinor_curvature(Om, mu, nu):
    return (Om[nu].diff(x[mu]) - Om[mu].diff(x[nu])
            + Om[mu] * Om[nu] - Om[nu] * Om[mu])
```

`spinor_curvature(Om, mu, nu)` is $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$ for any list of spinor connections `Om`.

```python
F = {}
theorem_ok = True
for mu in range(8):
    for nu in range(mu + 1, 8):
        F[(mu, nu)] = spinor_curvature(Omega, mu, nu)
        from_riemann = sum((ETA[a] * f[a] * riemann[(a, c, mu, nu)] / f[c] * S[a][c] / 2
                            for a in range(8) for c in range(8)
                            if (a, c, mu, nu) in riemann), Z16)
        theorem_ok = theorem_ok and matrix_is_zero(F[(mu, nu)] - from_riemann)
check(theorem_ok, "F_mu nu = (1/2) R_ab mu nu S^ab in all 28 coordinate planes",
      record=f"{REPORT_PY}, check spinor_curvature_equals_riemann")
```

For the 28 planes $\mu < \nu$ of the diagonal vielbein, $F_{\mu\nu}$ is computed and compared with $\frac12\sum_{a,c}R_{ac\mu\nu}S^{ac}$, where $R_{ac\mu\nu} = \eta_{aa}f_aR^a{}_{c\mu\nu}/f_c$ (the term is added only when the Riemann component is nonzero, `if (a, c, mu, nu) in riemann`). The check requires the theorem in all 28 planes.

```python
F18_boosted = spinor_curvature(Omega_6H, 0, 7)
R_6H, R_inv_6H = R.subs(six_H), R_inv.subs(six_H)
check(matrix_is_zero(F18_boosted - R_6H * F[(0, 7)] * R_inv_6H)
      and np.abs(sample_table(F18_boosted)).max() > 0.1,
      "boosted (beta = 6H): F'_x1x8 = R F_x1x8 R^-1, nonzero",
      record=f"{SCOPE_PY}, check boosted_frame_curvature_nonzero")
```

In the boosted frame with $\beta = 6H$: $F'_{x1\,x8}$ is computed from the boosted spinor connection, $R$ and $R^{-1}$ are taken at $\beta = 6H$, and the check requires $F'_{x1x8} = RF_{x1x8}R^{-1}$ and an entry above 0.1 at the sample point, so that it is not zero. Two PASS lines with their records.

**In [16], figure 5.**

```python
norms = np.zeros((8, 8))
for (mu, nu), matrix in F.items():
    norms[mu, nu] = norms[nu, mu] = np.sqrt((sample_table(matrix) ** 2).sum())
```

For each plane the size $\lVert F_{\mu\nu}\rVert$, the square root of the sum of the squares of its 256 entries at the sample point (`** 2` squares every entry, `.sum()` adds them), stored symmetrically in an $8 \times 8$ array.

```python
fig, ax = plt.subplots(figsize=(6.4, 5.4))
image = ax.imshow(norms, cmap="Purples")
for mu in range(8):
    for nu in range(8):
        if norms[mu, nu] > 0:
            # white digits on the dark squares (the largest sizes), black elsewhere
            dark = norms[mu, nu] > 0.6 * norms.max()
            ax.text(nu, mu, f"{norms[mu, nu]:.1f}", ha="center", va="center",
                    fontsize=7, color="white" if dark else "black")
ax.set_xticks(range(8), NAMES)
ax.set_yticks(range(8), NAMES)
ax.set_xlabel("coordinate $\\nu$")
ax.set_ylabel("coordinate $\\mu$")
ax.set_title("Size of the spinor curvature $\\|F_{\\mu\\nu}\\|$")
ax.grid(False)
fig.colorbar(image, ax=ax, shrink=0.8, label="$\\|F_{\\mu\\nu}\\|$ (units of $H^2$)")
```

A heat map in shades of purple (white is zero), with the size written into each nonzero square with one decimal, in white on the dark squares (above 60 percent of the largest size) and in black elsewhere, and a colour bar.

```python
save_figure(fig, "spinor_curvature_norms",
            "The size $\\|F_{\\mu\\nu}\\|$, the square root of the sum of the squares "
            ...
            "change of frame removes.")
```

The figure is saved.

```python
report("largest |F_mu nu| at the sample point (units of H^2)", f"{norms.max():.3f}")
curved = [pair for pair in F if norms[pair] > 1e-9]  # the curved planes
check(matrix_is_zero(F[(3, 7)]) and len(curved) == 27,
      "F_x4x8 = 0 exactly; the other 27 planes are curved at the sample point")
```

The RESULT line prints the largest size, 3.633 (in units of $H^2$). `curved` lists the planes with a size above $10^{-9}$, and the check requires $F_{x4x8} = 0$ exactly and the other 27 planes to be curved at the sample point.

**What Figure 06b.5 shows.** Every square off the diagonal is coloured except the two of the pair $(x4, x8)$. The largest sizes, about 3.6 and 3.5, lie in the planes within 3-space and between 3-space and the hidden direction; the planes of 3-space with the extra times have about 2.2, with the time about 1.7; the planes of the extra times among themselves about 0.5, with the time 0.6 and with the hidden direction 1.3. The pattern reflects the factors $e^{a_4}$ and $e^{-a_4}$ at $a_4 = \frac12$. Whatever the numbers in another frame, $F' = RFR^{-1}$ can never turn a coloured square white: this curvature is a property of the metric.

**In [17], the rescaling** (Section 6.18).

```python
w = sp.sin(z) ** sp.Rational(-1, 2)  # the weight sin^(-1/2) z
bracket = sum((gup[mu] * sp.diff(w, x[mu]) for mu in range(8)), Z16) + w * slash
```

The weight $w = \sin^{-1/2}z$ and the bracket $\sum_\mu\gamma^\mu\partial_\mu w + w\sum_\mu\gamma^\mu\Omega_\mu$ of Section 6.18.

```python
chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])
psi = w * chi
dirac_psi = sum((gup[mu] * (psi.diff(x[mu]) + Omega[mu] * psi) for mu in range(8)),
                sp.zeros(16, 1))
dirac_chi = sum((gup[mu] * chi.diff(x[mu]) for mu in range(8)), sp.zeros(16, 1))
check(matrix_is_zero(bracket) and all(is_zero(v) for v in dirac_psi - w * dirac_chi),
      "gamma^mu D_mu (w chi) = w gamma^mu d_mu chi for w = sin^(-1/2) z",
      record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
```

For safety the statement is also checked on sixteen completely general functions $\chi_1, \dots, \chi_{16}$ of all eight coordinates: `dirac_psi` is $\sum_\mu\gamma^\mu D_\mu(w\chi)$ and `dirac_chi` is $\sum_\mu\gamma^\mu\partial_\mu\chi$; the check requires the bracket to vanish and $\sum_\mu\gamma^\mu D_\mu(w\chi) - w\sum_\mu\gamma^\mu\partial_\mu\chi$ to vanish in all sixteen components.

```python
chi_conj = sp.Matrix([sp.conjugate(v) for v in chi])  # complex conjugates
S_psi = (w * chi_conj).T * C * (w * chi)  # Psi^dagger C Psi (w is real)
S_chi = chi_conj.T * C * chi
check(is_zero(S_psi[0, 0] - S_chi[0, 0] / sp.sin(z)),
      "S[sin^(-1/2) z chi] = S[chi] / sin z",
      record=f"{SCOPE_PY}, check rescaled_equation_quadratic_potential")
```

The bilinear: `chi_conj` is the column of the complex conjugates $\chi_A^*$, so `(w * chi_conj).T * C * (w * chi)` is $\Psi^\dagger C\Psi$ for $\Psi = w\chi$ (the conjugate of the real $w$ is $w$), a $1 \times 1$ matrix whose only entry `[0, 0]` is the number. The check requires $S[w\chi] = S[\chi]/\sin z$. Two PASS lines with their records.

**In [18], figure 6.**

```python
z_values = np.linspace(0.05, np.pi / 2 - 0.02, 300)
x8_symbol = sp.Symbol("u", positive=True)
term_derivative = sp.lambdify(x8_symbol, (sp.tan(z) * sp.diff(w, x8)).subs(
    {H: 1}).subs(x8, x8_symbol))
term_connection = sp.lambdify(x8_symbol, (3 * H * w).subs({H: 1}).subs(x8, x8_symbol))
weight = sp.lambdify(x8_symbol, w.subs({H: 1}).subs(x8, x8_symbol))
u_values = z_values / 6.0  # x8 = z / (6 H) with H = 1
first, second = term_derivative(u_values), term_connection(u_values)
```

300 values of $z$ inside $(0, \pi/2)$, and three numerical functions of $x_8$ (a positive symbol `u` replaces $x_8$): the derivative term $\tan z\,\partial_8w$, the connection term $3Hw$ and the weight $w$, all with $H = 1$. With $H = 1$, $x_8 = z/6$.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
ax_left.plot(z_values, weight(u_values), label="$w = \\sin^{-1/2} z$")
ax_left.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax_left.set_ylabel("weight (pure number)")
ax_left.set_title("The rescaling weight")
ax_left.legend(fontsize=8)
ax_right.plot(z_values, first, label="$\\tan z\\,\\partial_{x8} w$")
ax_right.plot(z_values, second, "--", label="$3H w$ (from $\\gamma^\\mu\\Omega_\\mu$)")
ax_right.plot(z_values, first + second, ":", color="black", label="sum")
ax_right.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax_right.set_ylabel("coefficient of $\\gamma^{(x8)}\\chi$ (units of $H$)")
ax_right.set_title("The two terms cancel")
ax_right.legend(fontsize=8)
```

The left panel draws $w$; the right panel the two terms and their sum.

```python
save_figure(fig, "rescaling",
            "The rescaling $\\Psi = w\\chi$ with $w = \\sin^{-1/2}z$ and $H = 1$. "
            ...
            "variable $\\chi$ the equation has no term $3H\\gamma^{(x8)}$.")
```

The figure is saved.

```python
check(np.max(np.abs(first + second)) < 1e-12, "the two terms cancel at all 300 points")
```

The two terms cancel at all 300 points to better than $10^{-12}$. The cell prints the file name and one PASS line.

**What Figure 06b.6 shows.** On the left, the weight $w = \sin^{-1/2}z$ is large near the tip $z \to 0$ and falls to 1 at the patch end. On the right, the derivative term $\tan z\,\partial_8w = -3Hw$ (solid) is the mirror image of the connection term $3Hw$ (dashed) about the zero line, and their sum (dotted) lies on zero everywhere: in the variable $\chi$ the field equation has no term $3H\gamma^{(x8)}$.

**In [19], the last checks.**

```python
scope_names = ["boosted_frame_reproduces_metric", "boosted_frame_canonical_connection",
               "boosted_frame_gammaOmega_formula", "boosted_frame_gammaOmega_vanishes",
               "boosted_frame_curvature_nonzero",
               "rescaling_removes_the_connection_term",
               "rescaled_equation_quadratic_potential",
               "gammaOmega_blind_to_the_deflation"]
cited = {SCOPE_PY: scope_names, SCOPE_WL: scope_names,
         REPORT_PY: ["spinor_curvature_equals_riemann",
                     "curvature_nonzero_flat_only_formally"],
         REPORT_WL: ["ricci_scalar", "ricci_mixed_components",
                     "never_flat_for_H_positive", "spin_curvature_equals_Riemann"]}
count = sum(len(v) for v in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names), f"the {count} cited record checks are recorded as passed")
```

`scope_names` lists the eight scope checks that this notebook reproduces; each appears in both scope reports, the sympy one and the WolframScript one. Together with two curvature checks of the sympy field-theory report and four of the WolframScript one, that makes $8 + 8 + 2 + 4 = 22$ cited checks, and the check requires all of them to be recorded as passed.

```python
expected = [f"06b_{k}_{name}.png" for k, name in enumerate([
    "boost_hyperbolas", "boosted_contraction", "boosted_connection_heat_maps",
    "ricci_components", "spinor_curvature_norms", "rescaling"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist, and the last line is printed: ALL 26 CHECKS PASSED (notebook 06b).

### 6.23 Upper and lower frame indices: the mixed contraction

**The issue.** The spin connection comes out of its formula with the first frame index up, $\omega_\mu{}^a{}_b$ (the mixed components, Section 6.4), and the spinor connection is built from the components with both frame indices down, $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ with $\omega_{\mu ab} = \eta_{aa}\omega_\mu{}^a{}_b$. The Revision record states (in `Revision/SPEC.md`, section 3, and in `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md`, section 4) that the author's Mathematica notebook contracts the mixed components with $S^{ab}$ instead, that this contraction lacks one factor of the frame metric, and that the record does not use it. This book has not opened the author's notebook file; it relies on the record's statement, which Notebook 06c checks in `Revision/SPEC.md`. We call that contraction

$$
\Omega^{nb}_\mu = \tfrac12\sum_{a,b}\omega_\mu{}^a{}_b\,S^{ab}
$$

("nb" for notebook) and derive exactly what the missing factor changes.

**The derivation, line by line.** Lowering is multiplication by $\eta_{aa}$, and $\eta_{aa}\eta_{aa} = 1$, so $\omega_\mu{}^a{}_b = \eta_{aa}\omega_{\mu ab}$ (multiply $\omega_{\mu ab} = \eta_{aa}\omega_\mu{}^a{}_b$ by $\eta_{aa}$). Hence

$$
\Omega^{nb}_\mu = \tfrac12\sum_{a,b}\eta_{aa}\,\omega_{\mu ab}\,S^{ab} .
$$

The terms with $a = b$ vanish ($S^{aa} = 0$). Every other term belongs to exactly one unordered pair $\{a, b\}$ with $a < b$, which contributes two terms:

$$
\eta_{aa}\,\omega_{\mu ab}S^{ab} + \eta_{bb}\,\omega_{\mu ba}S^{ba} = (\eta_{aa} + \eta_{bb})\,\omega_{\mu ab}S^{ab}
$$

(both factors of the second term change sign when $a$ and $b$ are exchanged, $\omega_{\mu ba}S^{ba} = (-\omega_{\mu ab})(-S^{ab})$). So

$$
\Omega^{nb}_\mu = \sum_{a<b}\tfrac12(\eta_{aa} + \eta_{bb})\,\omega_{\mu ab}S^{ab}, \qquad\text{while}\qquad \Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}
$$

(the same steps without $\eta$, Section 6.7). The factor $\frac12(\eta_{aa} + \eta_{bb})$ is $+1$ for a pair of two space-like directions (**space-space**), $-1$ for a pair of two time-like directions (**time-time**) and $0$ for a boost pair. In the author's frame metric there are $\binom42 = 6$ space-space pairs among $x1, x2, x3, x8$, 6 time-time pairs among $x4, x5, x6, x7$, and $4 \cdot 4 = 16$ boost pairs. Writing $\Omega^{ss}_\mu$, $\Omega^{tt}_\mu$ and $\Omega^{st}_\mu$ for the parts of $\Omega_\mu$ that come from the three kinds of pairs:

$$
\Omega^{nb}_\mu = \Omega^{ss}_\mu - \Omega^{tt}_\mu, \qquad \Omega_\mu = \Omega^{ss}_\mu + \Omega^{tt}_\mu + \Omega^{st}_\mu .
$$

**The mixed contraction keeps the 6 space-space parts, reverses the sign of the 6 time-time parts and deletes all 16 boost parts.** In a space whose metric is positive (every $\eta_{aa} = +1$) the factor is always $+1$ and the two contractions agree: in the polar plane of Section 6.5 both give $\Omega_\varphi = -\frac i2\sigma_3$. The mistake cannot be seen in the usual textbook examples; in signature (4,4) it deletes 16 of the 28 parts.

**Where it is total: the Milne wedge.** Take the flat plane with one time $t$ and one space direction $y$, $ds^2 = -dt^2 + dy^2$, and in the part $t > \lvert y\rvert$ the coordinates $\tau = \sqrt{t^2 - y^2}$ and $\theta$ with $t = \tau\cosh\theta$, $y = \tau\sinh\theta$. Line by line, $dt = \cosh\theta\,d\tau + \tau\sinh\theta\,d\theta$ and $dy = \sinh\theta\,d\tau + \tau\cosh\theta\,d\theta$ (the product rule and $\frac{d}{d\theta}\cosh\theta = \sinh\theta$, $\frac{d}{d\theta}\sinh\theta = \cosh\theta$), so

$$
-dt^2 + dy^2 = -(\cosh^2\theta - \sinh^2\theta)\,d\tau^2 + \tau^2(\cosh^2\theta - \sinh^2\theta)\,d\theta^2 = -d\tau^2 + \tau^2d\theta^2
$$

(square, add; the cross terms $\mp2\tau\cosh\theta\sinh\theta\,d\tau\,d\theta$ cancel; $\cosh^2 - \sinh^2 = 1$). This part of the flat plane is called the **Milne wedge**. Its frame metric is $\eta = \mathrm{diag}(-1, +1)$ (frame index 0 the unit time direction, 1 the unit space direction) and its vielbein factors are $f_\tau = 1$, $f_\theta = \tau$. By the formula of Section 6.6, $\omega_{\theta\,10} = \eta_{11}\,\partial_\tau f_\theta/f_\tau = 1$, so $\omega_{\theta\,01} = -1$, and the mixed components are

$$
\omega_\theta{}^0{}_1 = \eta_{00}\,\omega_{\theta01} = (-1)(-1) = 1, \qquad \omega_\theta{}^1{}_0 = \eta_{11}\,\omega_{\theta10} = 1 :
$$

**symmetric**, as for every boost pair (Section 6.4). Two real $2 \times 2$ matrices with $(\gamma^0)^2 = -1$, $(\gamma^1)^2 = +1$ and $\gamma^0\gamma^1 + \gamma^1\gamma^0 = 0$ are $\gamma^0 = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$ and $\gamma^1 = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$ (multiply out to check), with $\gamma^0\gamma^1 = \mathrm{diag}(1, -1)$. Then

$$
\Omega_\theta = \omega_{\theta01}S^{01} = -\tfrac12\gamma^0\gamma^1, \qquad \Omega^{nb}_\theta = \tfrac12\big(\omega_\theta{}^0{}_1S^{01} + \omega_\theta{}^1{}_0S^{10}\big) = \tfrac12\big(S^{01} - S^{01}\big) = 0 .
$$

The plane is flat, but the frame is boosted by the rapidity $\theta$ as one moves along $\theta$, and the correct spinor connection records this: $\Omega_\theta = -(\partial_\theta U)U^{-1}$ for the spinor boost $U(\theta) = \cosh\frac\theta2 + \sinh\frac\theta2\,\gamma^0\gamma^1 = \mathrm{diag}(e^{\theta/2}, e^{-\theta/2})$ (since $\partial_\theta U = \frac12\gamma^0\gamma^1U$). The mixed contraction deletes the whole connection. It also violates the divergence form of Section 6.9: with $\sqrt{\lvert g\rvert} = \tau$, $\gamma^\tau = \gamma^0$ and $\gamma^\theta = \gamma^1/\tau$,

$$
\frac{1}{2\tau}\Big(\partial_\tau(\tau\gamma^0) + \partial_\theta\big(\tau\cdot\tfrac{\gamma^1}{\tau}\big)\Big) = \frac{\gamma^0}{2\tau}, \qquad \gamma^\theta\Omega_\theta = \frac{\gamma^1}{\tau}\Big(-\tfrac12\gamma^0\gamma^1\Big) = \frac{1}{2\tau}\gamma^0\gamma^1\gamma^1 = \frac{\gamma^0}{2\tau}
$$

(in the second: exchange $\gamma^1$ and $\gamma^0$ at the cost of a sign; $(\gamma^1)^2 = 1$). The correct value equals the divergence form; the mixed contraction gives 0.

**The author's metric.** Of the 12 components of Section 6.6 the six with an $x8$ for $\mu = x_i$ are space-space pairs (kept), the three $(x4, x_t)$ are time-time pairs (sign reversed), and the three $(x_i, x4)$ and the three $(x_t, x8)$ are boost pairs (deleted). So

$$
\Omega^{nb}_{x_i} = e^{a_4}s\,H\,S^{x_i\,x8}, \qquad \Omega^{nb}_{x_t} = +e^{-a_4}s\,a_4'\,S^{x4\,x_t},
$$

compared with $\Omega_{x_i} = e^{a_4}s(a_4'S^{x_ix4} + HS^{x_ix8})$ and $\Omega_{x_t} = -e^{-a_4}s(a_4'S^{x4x_t} + HS^{x_tx8})$. The contraction, by the steps of Section 6.8:

$$
\gamma^{x_i}\Omega^{nb}_{x_i} = \frac{\gamma^{(x_i)}}{f_i}\,f_iH\,\tfrac12\gamma^{(x_i)}\gamma^{(x8)} = \tfrac H2\gamma^{(x8)}, \qquad \gamma^{x_t}\Omega^{nb}_{x_t} = \frac{\gamma^{(x_t)}}{f_t}\,f_ta_4'\,\tfrac12\gamma^{(x4)}\gamma^{(x_t)} = \tfrac{a_4'}2\gamma^{(x4)}
$$

($(\gamma^{(x_i)})^2 = 1$; and $\gamma^{(x_t)}\gamma^{(x4)}\gamma^{(x_t)} = \gamma^{(x4)}$ as in Section 6.8). Summed over the six warped directions:

$$
\sum_\mu\gamma^\mu\Omega^{nb}_\mu = \tfrac{3H}{2}\gamma^{(x8)} + \tfrac{3a_4'}{2}\gamma^{(x4)} \qquad\text{instead of}\qquad \sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)} .
$$

Half of the hidden term is lost, and the time-direction terms no longer cancel: with the mixed contraction the deflation would appear in this term.

**The gammas are no longer covariantly constant.** Replace $\Omega_\mu$ by $\Omega^{nb}_\mu$ in $D_\mu\gamma^\nu$:

$$
D^{nb}_\mu\gamma^\nu = \partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega^{nb}_\mu, \gamma^\nu] = D_\mu\gamma^\nu + [\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu] = [\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu]
$$

(add and subtract $[\Omega_\mu, \gamma^\nu]$; then $D_\mu\gamma^\nu = 0$, Section 6.7). By the vector rule, $[S^{ab}, \gamma^c]$ is nonzero only when $c$ is $a$ or $b$. For $\mu = x1$ the difference is $\Omega^{nb}_{x1} - \Omega_{x1} = -f_1a_4'S^{x1x4}$, the deleted boost part, and

$$
[\Omega^{nb}_{x1} - \Omega_{x1}, \gamma^{x1}] = -a_4'[S^{x1x4}, \gamma^{(x1)}] = -a_4'\big(\eta^{x4\,x1}\gamma^{(x1)} - \eta^{x1x1}\gamma^{(x4)}\big) = a_4'\gamma^{(x4)}
$$

(the factor $f_1$ of the difference cancels against the $1/f_1$ of $\gamma^{x1}$; then the vector rule $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$ with $\eta^{x4x1} = 0$ and $\eta^{x1x1} = 1$), and in the same way, with $\eta^{x4x4} = -1$,

$$
[\Omega^{nb}_{x1} - \Omega_{x1}, \gamma^{x4}] = -f_1a_4'\big(\eta^{x4x4}\gamma^{(x1)} - \eta^{x1x4}\gamma^{(x4)}\big) = f_1a_4'\gamma^{(x1)} .
$$

So for each 3-space direction two pairs $(\mu, \nu)$ are violated. For $\mu = x5$ the difference is $2f_5a_4'S^{x4x5} + f_5HS^{x5x8}$ (the time-time part counted twice, because its sign was reversed, and the deleted boost part), and the same rule gives $[\ldots, \gamma^{x5}] = -2a_4'\gamma^{(x4)} + H\gamma^{(x8)}$, $[\ldots, \gamma^{x4}] = 2f_5a_4'\gamma^{(x5)}$ and $[\ldots, \gamma^{x8}] = \tan z\,f_5H\gamma^{(x5)}$: three violated pairs for each extra time. Altogether $3 \cdot 2 + 3 \cdot 3 = 15$ of the 64 pairs. Each violated matrix is a multiple of one gamma (16 nonzero entries), except $-2a_4'\gamma^{(x4)} + H\gamma^{(x8)}$, which has 32 because $\gamma^{(x4)}$ and $\gamma^{(x8)}$ have their nonzero entries in different places (the tables of Chapter 5); so there are $6 \cdot 16 + 3(16 + 32 + 16) = 288$ nonzero entries. Notebook 06c finds exactly these numbers (In [13]; COMPUTED exactly by the notebook, not a Revision record).

| statement | status | where it is verified |
| --- | --- | --- |
| $\Omega^{nb}_\mu = \sum_{a<b}\frac12(\eta_{aa} + \eta_{bb})\omega_{\mu ab}S^{ab} = \Omega^{ss}_\mu - \Omega^{tt}_\mu$ | PROVED (above) | Notebook 06c, In [4] and In [8] (its own exact checks) |
| polar plane: the contractions agree; Milne wedge: $\Omega_\theta = -\frac12\gamma^0\gamma^1$, $\Omega^{nb} = 0$ | PROVED (above) | Notebook 06c, In [6] |
| the record does not use the mixed contraction | the record's statement | `Revision/SPEC.md`, section 3 (checked as text by Notebook 06c, In [2]) |
| $\gamma^\mu\Omega^{nb}_\mu = \frac{3H}{2}\gamma^{(x8)} + \frac{3a_4'}{2}\gamma^{(x4)}$; 15 violated pairs, 288 entries | PROVED above and COMPUTED exactly by Notebook 06c; not a Revision result (it describes the contraction the record does not use) | Notebook 06c, In [10] and In [13] |

### 6.24 Why only the value $3H$ is right

Two facts single out the correct value $3H\gamma^{(x8)}$ among all candidates.

**The divergence form.** Section 6.9 showed that the correct contraction equals $\frac{1}{2\sqrt{\lvert g\rvert}}\sum_\mu\partial_\mu(\sqrt{\lvert g\rvert}\gamma^\mu)$, a quantity built from the volume factor and the vielbein alone. The mixed contraction, $\frac{3H}{2}\gamma^{(x8)} + \frac{3a_4'}{2}\gamma^{(x4)}$, does not equal it.

**The hidden-direction operator.** For fields that depend on $x_8$ only, the part of the Dirac operator along the hidden direction is $\tan z\,\gamma^{(x8)}\partial_8 + c\,\gamma^{(x8)}$, where $c$ is the coefficient of $\gamma^{(x8)}$ in the contraction ($c = 3H$ for the correct one, $c = \frac32H$ for the mixed one). Write $A_cq = \tan z\,\partial_8q + c\,q$ for a function $q(x_8)$. An operator $A$ is called **antisymmetric for the weight $w(x_8)$** when $\int w\,p\,(Aq)\,dx_8 = -\int w\,(Ap)\,q\,dx_8$ for all functions $p$, $q$, up to **boundary terms** (values at the ends of the interval). This is the property that makes $iA$ a Hermitian operator in quantum theory (Chapter 10), and the natural weight is the volume factor $\cos z$. Compute, line by line, for two functions $p(x_8)$, $q(x_8)$ (primes are derivatives by $x_8$ here):

$$
\partial_8(\sin z\,p\,q) = 6H\cos z\;p\,q + \sin z\,(p'q + p\,q')
$$

(the product rule; $\partial_8\sin z = 6H\cos z$),

$$
\cos z\,\big(p\,A_cq + (A_cp)\,q\big) = \cos z\tan z\,(p\,q' + p'q) + 2c\cos z\;p\,q = \sin z\,(p\,q' + p'q) + 2c\cos z\;p\,q
$$

(insert $A_c$; $\cos z\tan z = \sin z$). Subtracting the first line from the second:

$$
\cos z\,\big(p\,A_cq + (A_cp)\,q\big) - \partial_8(\sin z\,p\,q) = (2c - 6H)\cos z\;p\,q .
$$

For $c = 3H$ the right side vanishes: integrated over $x_8$, $\int\cos z\,p\,A_{3H}q\,dx_8 = -\int\cos z\,(A_{3H}p)\,q\,dx_8 + \big[\sin z\,p\,q\big]$, so $A_{3H}$ is antisymmetric for the weight $\cos z$ up to the boundary term. This is the record's formula `hidden_direction_hermiticity`. For the mixed value $c = \frac32H$ the term $-3H\cos z\,p\,q$ remains, which is not a boundary term (it has no derivative in front), so no boundary condition can remove it. For $c = 0$ (no spin-connection term at all) the leftover would be $-6H\cos z\,p\,q$.

**Scope of this argument.** The boundary term $[\sin z\,p\,q]$ vanishes at the tip $z \to 0$ but not at the patch end $z = \pi/2$, where $\sin z = 1$; there a boundary condition is needed, which Chapter 14 supplies by the ASSUMED $Z_2$ mirror (the choice of boundary condition is the one point of this chapter that is left OPEN here). And the role of $3H$ depends on the variables: in the rescaled field $\chi$ of Section 6.18, with the proper distance $y$ of Chapter 3 as coordinate and the weight $dy$, the operator $\partial_y$ has the same antisymmetry without any $H$ term (the record says so in the same formula). PROVED; `field-theory.json`, formula `hidden_direction_hermiticity`; `wolfram-field-theory.json`, check `good_sector_hermiticity_curved`; both scope reports, check `good_sector_hermiticity_up_to_the_brane_flux`; Notebook 06c, In [15].

### 6.25 Example: Notebook 06c

Notebook 06c checks Sections 6.23 and 6.24 with exact algebra. It reads the author's gammas and the formulas of the record, and checks that `Revision/SPEC.md` contains the record's statement about the mixed contraction. It defines the general formulas again, now with the MIXED spin connection, a separate lowering function and a contraction over all ordered pairs. It sorts the 28 frame pairs into their three kinds and checks the key step of the derivation for all of them; works the polar plane and the Milne wedge; computes, for the author's metric, the correct and the mixed spinor connections and their contractions direction by direction; counts where the covariant constancy of the gammas breaks; and checks the divergence form and the antisymmetry of the hidden-direction operator for two arbitrary functions. Every correct result is compared with the Revision record; the results about the mixed contraction are the notebook's own and are labelled so. It draws six figures, needs no Rust, runs in less than a minute and ends with the line ALL 27 CHECKS PASSED (notebook 06c).

<!-- NOTEBOOK 06c -->

### 6.28 Line-by-line walk-through of Notebook 06c

The notebook has 17 code cells, In [1] to In [17]; this section explains every line of every one of them. A line `...` in a quoted figure cell stands for the remaining lines of a long caption, printed in full in Section 6.27.

**In [1], the set-up cell.** Its comment lines are the run instructions of Section 6.26. Its code is the set-up code of Notebook 06a explained at the beginning of Section 6.14, with the single difference

```python
NOTEBOOK_ID = "06c"  # this notebook: chapter 06, example c
```

It prints one line, Set-up of notebook 06c complete: repository folder found, helpers defined.

**In [2], the tools and the record.**

```python
import sys  # the Python system module (here: the stream of printed text)

# Jupyter sends printed text to the screen in pieces, about every 0.2 seconds.  The
# book's checking tool reads each PASS line together with its "reproduces" line, so
# the pieces must be the same in every run: send the printed text of a cell in one
# piece when the cell ends (or just before a figure), at the latest after 600 s.
if hasattr(sys.stdout, "flush_interval"):  # true inside Jupyter only
    sys.stdout.flush_interval = 600.0
```

The setting of the output channel explained in Section 6.14 (Notebook 06a, In [2]).

```python
import numpy as np  # decimal numbers (only for the plots)
import sympy as sp  # exact algebra and calculus with symbols
```

numpy for the plots and sympy for the exact algebra.

```python
fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
    encoding="utf-8"))
NAMES = fixture["coordinates"]  # ["x1", ..., "x8"]
ETA = fixture["eta"]  # +1 space-like, -1 time-like
gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(x(a+1))
I16, Z16 = sp.eye(16), sp.zeros(16, 16)  # identity and zero matrix
```

The record of the gammas is read as in Notebook 06a: the names, the signs of $\eta$, the eight exact matrices, the identity and the zero matrix.

```python
check(all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
          == (2 * ETA[a] if a == b else 0) * I16
          for a in range(8) for b in range(8)),
      "the 64 Clifford relations of the author's gammas",
      record="Revision/theory/reports/python-field-theory.json, "
             "check clifford_relations")
check(len(gamma) == 8 and all(M.shape == (16, 16) for M in gamma)
      and all(entry.is_real for M in gamma for entry in M),
      "the eight gammas are 16 x 16 matrices with real entries",
      record="Revision/theory/reports/python-field-theory.json, check gammas_real")
```

The two checks of Notebook 06a, In [2]: the 64 Clifford relations, and eight real $16 \times 16$ matrices, each with its record.

```python
S = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
     for a in range(8)]  # S[a][b] = S^ab
```

The 64 generators $S^{ab}$.

```python
def is_zero(expr):
    """True when expr is exactly zero for all values of its symbols."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    if sp.cancel(sp.expand(expr.rewrite(sp.exp))) == 0:  # the fast route
        return True
    return sp.simplify(expr) == 0  # the slower general route
```

The exact zero test (Section 6.14, In [3] of Notebook 06a).

```python
def matrix_is_zero(matrix):
    """True when every entry of the matrix is exactly zero."""
    return all(is_zero(entry) for entry in matrix)


def record_passed(path, name):
    """True when the Revision report at path records the check name as passed."""
    data = json.loads(repository_file(path).read_text(encoding="utf-8"))
    for entry in data["checks"]:
        if entry["name"] == name:
            return entry["verdict"].upper() == "PASS"  # "PASS" or "pass"
    raise KeyError(f"{path} has no check {name}")
```

`matrix_is_zero` and `record_passed`, as in Notebook 06a.

```python
THEORY_FILE = "Revision/theory/field-theory.json"
FORMULAS = {item["key"]: item["wl"] for item in json.loads(
    repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
REPORT_PY = "Revision/theory/reports/python-field-theory.json"
REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
```

The formulas of `Revision/theory/field-theory.json`, read into a dictionary from key to Wolfram text, and the paths of the two field-theory reports.

```python
# " ".join(text.split()) replaces every run of blanks and line breaks by one blank,
# so a sentence that the file breaks across two lines is found as one line.
spec_text = " ".join(repository_file("Revision/SPEC.md").read_text(
    encoding="utf-8").split())
statement = "contraction of the mixed omega_mu^a_b, which lacks a metric factor"
check(statement in spec_text,
      "Revision/SPEC.md section 3 records the missing metric factor")
```

The notebook checks that the statement on which it is built is in the record. `" ".join(text.split())` replaces every run of blanks and line breaks by one blank (`split()` cuts the text at all blanks and line breaks, `" ".join` glues the pieces with single blanks), so that a sentence that the file breaks across two lines is found as one line. The check requires `Revision/SPEC.md` to contain the words "contraction of the mixed omega_mu^a_b, which lacks a metric factor" (`in` tests whether one text occurs inside another). The cell prints three PASS lines.

**In [3], the general formulas, now with the mixed connection** (Sections 6.4 and 6.23).

```python
def christoffel(g, coords):
    """Gam[l][m][n] = (1/2) sum_r g^lr (d_m g_rn + d_n g_rm - d_r g_mn)."""
    n = len(coords)
    g_inv = g.inv()  # the inverse metric
    Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for k in range(m, n):  # Gamma^l_mk = Gamma^l_km: compute it once
                value = sum(g_inv[l, r] * (sp.diff(g[r, k], coords[m])
                                           + sp.diff(g[r, m], coords[k])
                                           - sp.diff(g[m, k], coords[r]))
                            for r in range(n) if g_inv[l, r] != 0) / 2
                Gam[l][m][k] = Gam[l][k][m] = sp.simplify(value)
    return Gam
```

The Christoffel symbols, as in Notebook 06b, In [3].

```python
def mixed_spin_connection(e, Gam, coords):
    """mixed[mu][a][b] = omega_mu^a_b (first frame index up)."""
    n = len(coords)
    E = e.inv()  # E[nu, b] = e_b^nu, the inverse vielbein
    mixed = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for mu in range(n):
        for a in range(n):
            for b in range(n):
                value = 0
                for nu in range(n):
                    if e[a, nu] == 0:
                        continue  # this term is zero
                    value += e[a, nu] * (sp.diff(E[nu, b], coords[mu]) + sum(
                        Gam[nu][mu][lam] * E[lam, b] for lam in range(n)))
                mixed[mu][a][b] = sp.simplify(value)
    return mixed
```

`mixed_spin_connection` is the spin connection of Notebook 06a, In [4], without the last step: it returns the MIXED components $\omega_\mu{}^a{}_b$ exactly as the formula of Section 6.4 gives them, without multiplying by $\eta_{aa}$.

```python
def lower_first_index(mixed, eta):
    """omega[mu][a][b] = eta_aa omega_mu^a_b (eta is diagonal)."""
    n = len(mixed)
    return [[[eta[a] * mixed[mu][a][b] for b in range(n)] for a in range(n)]
            for mu in range(n)]
```

`lower_first_index` does the lowering separately: $\omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b$ for all $\mu$, $a$, $b$.

```python
def contract(coefficients, gens):
    """(1/2) sum over ALL ordered pairs (a, b) of coefficients[mu][a][b] S^ab."""
    n = len(coefficients)
    size = gens[0][0].shape[0]  # 16 for the author's gammas, 2 in a plane
    return [sum((coefficients[mu][a][b] * gens[a][b] / 2 for a in range(n)
                 for b in range(n) if coefficients[mu][a][b] != 0),
                sp.zeros(size, size)) for mu in range(n)]
```

`contract(coefficients, gens)` is $\frac12\sum_{a,b}c_{\mu ab}S^{ab}$ for every $\mu$, summed over ALL ordered pairs $(a, b)$ (the term is skipped when the coefficient is zero). Notebook 06a summed over $a < b$ only, which is allowed for the antisymmetric lowered components; the mixed components are not antisymmetric, so here the full sum is needed, and the same function serves both contractions.

```python
def curved_gammas(e, gammas):
    """gamma^mu = sum_a e_a^mu gamma^a for every coordinate mu."""
    E = e.inv()
    n = len(gammas)
    return [sum((E[mu, a] * gammas[a] for a in range(n)),
                sp.zeros(*gammas[0].shape)) for mu in range(n)]
```

The curved gammas, as before.

```python
def generators(gammas):
    """S[a][b] = (1/4)(gamma^a gamma^b - gamma^b gamma^a)."""
    n = len(gammas)
    return [[(gammas[a] * gammas[b] - gammas[b] * gammas[a]) / 4 for b in range(n)]
            for a in range(n)]
```

`generators(gammas)` builds the matrices $S^{ab} = \frac14[\gamma^a, \gamma^b]$ for any list of gammas; it is used for the $2 \times 2$ gammas of the two planes.

```python
say("defined: christoffel, mixed_spin_connection, lower_first_index, contract, "
    "curved_gammas, generators")
```

One output line names the six functions.

**In [4], the three kinds of frame pairs.**

```python
KIND = {1: "space-space", -1: "time-time", 0: "boost"}  # the factor and its name
factor = [[sp.Rational(ETA[a] + ETA[b], 2) for b in range(8)] for a in range(8)]
pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]  # the 28 pairs a < b
counts = {k: sum(1 for a, b in pairs if factor[a][b] == k) for k in KIND}
for k, name in KIND.items():
    report(f"number of {name} pairs (factor {k})", counts[k])
```

`KIND` names the three values of the factor. `factor[a][b]` is $\frac12(\eta_{aa} + \eta_{bb})$ as an exact fraction (`sp.Rational(n, 2)`); `pairs` lists the 28 pairs $a < b$, and `counts` counts the pairs of each kind (`sum(1 for ... if ...)` counts the cases in which the condition holds). Three RESULT lines print 6, 6 and 16.

```python
check(len(pairs) == 28 and counts == {1: 6, -1: 6, 0: 16},
      "28 pairs: 6 space-space (+1), 6 time-time (-1), 16 boost pairs (0)")
```

The check of the counts: 28 pairs, 6 with the factor $+1$, 6 with $-1$, 16 with 0.

```python
w = sp.Symbol("w")  # stands for omega_mu ab; then omega_mu ba = -w
check(all(matrix_is_zero(ETA[a] * w * S[a][b] + ETA[b] * (-w) * S[b][a]
                         - (ETA[a] + ETA[b]) * w * S[a][b]) for a, b in pairs),
      "eta_aa w S^ab + eta_bb (-w) S^ba = (eta_aa + eta_bb) w S^ab, all 28 pairs")
```

The key step of the derivation of Section 6.23 as a matrix identity, for all 28 pairs: with a symbol $w$ standing for $\omega_{\mu ab}$ (so that $\omega_{\mu ba} = -w$), $\eta_{aa}\,w\,S^{ab} + \eta_{bb}(-w)S^{ba} = (\eta_{aa} + \eta_{bb})\,w\,S^{ab}$. The cell prints three RESULT lines and two PASS lines.

**In [5], figure 1.**

```python
from matplotlib.colors import ListedColormap  # a colour map with a few colours
```

`ListedColormap` makes a colour map out of a short list of colours: the number 0 gets the first colour, 1 the second, and so on.

```python
grid = np.full((8, 8), 3)  # 3 = the diagonal (white)
for a in range(8):
    for b in range(8):
        if a != b:
            grid[a, b] = {1: 0, -1: 1, 0: 2}[int(factor[a][b])]  # colour number
```

`grid` is an $8 \times 8$ array filled with 3 (white, for the diagonal); off the diagonal the factor $+1$, $-1$, $0$ is translated into the colour numbers 0, 1, 2 by the small dictionary `{1: 0, -1: 1, 0: 2}`.

```python
colours = ListedColormap(["tab:green", "tab:orange", "lightgray", "white"])
fig, ax = plt.subplots(figsize=(6.4, 5.6))
ax.imshow(grid, cmap=colours, vmin=-0.5, vmax=3.5)
```

The four colours green, orange, light gray and white; `imshow` draws the grid with them (the limits $-0.5$ and $3.5$ put each whole number in the middle of its colour).

```python
for a in range(8):
    for b in range(8):
        if a != b:
            ax.text(b, a, f"{int(factor[a][b]):+d}" if factor[a][b] else "0",
                    ha="center", va="center", fontsize=9)
```

Each off-diagonal square gets its factor written in it, `+1`, `-1` or `0` (`:+d` writes a whole number with its sign).

```python
ax.set_xticks(range(8), NAMES)
ax.set_yticks(range(8), NAMES)
ax.set_xlabel("frame direction $b$")
ax.set_ylabel("frame direction $a$")
ax.set_title("Factor $(\\eta_{aa} + \\eta_{bb})/2$ of the notebook's contraction")
ax.grid(False)
```

Labels and title; no grid lines.

```python
for colour, label in (("tab:green", "kept: space-space (+1)"),
                      ("tab:orange", "sign reversed: time-time (-1)"),
                      ("lightgray", "deleted: boost pair (0)")):
    ax.plot([], [], "s", color=colour, markersize=9, label=label)  # legend only
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=8)
```

Three empty plots with square markers (`"s"`) only make the legend entries, and the legend is placed below the picture in two columns (`bbox_to_anchor` gives its position relative to the panel).

```python
save_figure(fig, "pair_kinds",
            "What the missing metric factor does to each pair of frame directions "
            ...
            "reversed and 16 deleted.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.1 shows.** Green squares ($+1$, kept) fill the pairs among $x1, x2, x3, x8$, orange squares ($-1$, sign reversed) the pairs among $x4, x5, x6, x7$, and gray squares (0, deleted) form two $4 \times 4$ rectangles: every space-like direction paired with every time-like direction. Counting the upper half: 6 green, 6 orange, 16 gray. The mixed contraction deletes more than half of the spin connection.

**In [6], the two flat planes** (Section 6.23).

```python
r, phi = sp.symbols("r phi", positive=True)  # the polar plane
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
polar_S = generators([sigma1, sigma2])
polar_e = sp.diag(1, r)  # unit radial and unit angular direction
polar_mixed = mixed_spin_connection(polar_e, christoffel(sp.diag(1, r**2), [r, phi]),
                                    [r, phi])
polar_Omega = contract(lower_first_index(polar_mixed, [1, 1]), polar_S)
polar_Omega_nb = contract(polar_mixed, polar_S)
check(polar_Omega == polar_Omega_nb and polar_Omega[1] == -sp.I / 2 * sigma3,
      "polar plane (eta = +1, +1): both contractions give Omega_phi = -(i/2) sigma3")
```

The polar plane: the Pauli matrices, their generators, the vielbein $\mathrm{diag}(1, r)$, the mixed connection of the metric $\mathrm{diag}(1, r^2)$, and both contractions, the correct one from the lowered components (with $\eta = (1, 1)$) and the mixed one. The check requires them to be equal and $\Omega_\varphi = -\frac i2\sigma_3$, as in Notebook 06a.

```python
tau = sp.Symbol("tau", positive=True)  # the Milne wedge: tau > 0
theta = sp.Symbol("theta", real=True)  # the rapidity coordinate
g0 = sp.Matrix([[0, 1], [-1, 0]])  # real, squares to -1 (the time direction)
g1 = sp.Matrix([[0, 1], [1, 0]])  # real, squares to +1 (the space direction)
I2, Z2 = sp.eye(2), sp.zeros(2, 2)
check(g0 * g0 == -I2 and g1 * g1 == I2 and g0 * g1 + g1 * g0 == Z2,
      "Milne: real gammas with (g0)^2 = -1, (g1)^2 = +1, g0 g1 + g1 g0 = 0")
```

The Milne wedge: the positive symbol $\tau$, the real symbol $\theta$ (the rapidity can be negative), the two real gammas of Section 6.23 and the check of their three relations.

```python
milne_S = generators([g0, g1])
milne_e = sp.diag(1, tau)  # unit time direction and unit space direction
milne_Gam = christoffel(sp.diag(-1, tau**2), [tau, theta])
milne_mixed = mixed_spin_connection(milne_e, milne_Gam, [tau, theta])
milne_lowered = lower_first_index(milne_mixed, [-1, 1])
```

The generators, the vielbein $\mathrm{diag}(1, \tau)$, the Christoffel symbols of the metric $\mathrm{diag}(-1, \tau^2)$, the mixed connection, and its lowered form with $\eta = (-1, +1)$.

```python
say(f"Gamma^tau_thetatheta = {milne_Gam[0][1][1]}, "
    f"Gamma^theta_tautheta = {milne_Gam[1][0][1]}")
say(f"mixed: omega_theta^0_1 = {milne_mixed[1][0][1]}, "
    f"omega_theta^1_0 = {milne_mixed[1][1][0]}")
say(f"lowered: omega_theta01 = {milne_lowered[1][0][1]}, "
    f"omega_theta10 = {milne_lowered[1][1][0]}")
check(milne_mixed[1][0][1] == 1 and milne_mixed[1][1][0] == 1
      and milne_lowered[1][0][1] == -1 and milne_lowered[1][1][0] == 1,
      "Milne: mixed components symmetric (1, 1), lowered antisymmetric (-1, +1)")
```

Three output lines print $\Gamma^\tau{}_{\theta\theta} = \tau$, $\Gamma^\theta{}_{\tau\theta} = 1/\tau$, the mixed components $1, 1$ and the lowered ones $-1, 1$; the check requires exactly these: mixed symmetric, lowered antisymmetric.

```python
milne_Omega = contract(milne_lowered, milne_S)
milne_Omega_nb = contract(milne_mixed, milne_S)
X2 = g0 * g1  # gamma^0 gamma^1, the boost generator of the plane (X2^2 = 1)
check(milne_Omega[0] == Z2 and milne_Omega[1] == -X2 / 2
      and milne_Omega_nb == [Z2, Z2],
      "Milne: Omega_theta = -(1/2) g0 g1, but the notebook's contraction gives 0")
```

The two contractions. `X2` is $\gamma^0\gamma^1$, the boost generator of the plane times 2. The check requires $\Omega_\tau = 0$, $\Omega_\theta = -\frac12\gamma^0\gamma^1$, and the mixed contraction to be zero in both directions (a list of two zero matrices).

```python
U = sp.cosh(theta / 2) * I2 + sp.sinh(theta / 2) * X2  # the spinor boost
check(matrix_is_zero(-U.diff(theta) * U.inv() - milne_Omega[1]),
      "Milne: Omega_theta = -(dU/dtheta) U^-1, U = cosh(theta/2) + sinh(theta/2) g0 g1")
```

The spinor boost $U(\theta) = \cosh\frac\theta2 + \sinh\frac\theta2\,\gamma^0\gamma^1$ and the check $\Omega_\theta = -(\partial_\theta U)U^{-1}$.

```python
milne_gup = curved_gammas(milne_e, [g0, g1])  # gamma^tau = g0, gamma^theta = g1/tau
slash_milne = (milne_gup[0] * milne_Omega[0] + milne_gup[1] * milne_Omega[1])
divergence_milne = ((tau * milne_gup[0]).diff(tau)
                    + (tau * milne_gup[1]).diff(theta)) / (2 * tau)
check(matrix_is_zero(slash_milne - g0 / (2 * tau))
      and matrix_is_zero(divergence_milne - slash_milne),
      "Milne: gamma^mu Omega_mu = g0/(2 tau) = the divergence form (notebook: 0)")
```

The curved gammas $\gamma^\tau = \gamma^0$, $\gamma^\theta = \gamma^1/\tau$, the correct contraction, and the divergence form with $\sqrt{\lvert g\rvert} = \tau$; the check requires both to be $\gamma^0/(2\tau)$, which the mixed value 0 violates. The cell prints three lines and six PASS lines.

**In [7], figure 2.**

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.8))
curve = np.linspace(-1.3, 1.3, 200)  # values of theta for the hyperbolas
for radius in (1.0, 2.0):
    ax_left.plot(radius * np.sinh(curve), radius * np.cosh(curve), ":",
                 color="gray", linewidth=1.0)
    for rapidity in (-1.0, -0.5, 0.0, 0.5, 1.0):
        py, pt = radius * np.sinh(rapidity), radius * np.cosh(rapidity)  # the point
        ax_left.quiver(py, pt, np.sinh(rapidity), np.cosh(rapidity),
                       color="tab:blue", angles="xy", scale_units="xy", scale=2.5,
                       width=0.006)  # e_(0), the unit time direction
        ax_left.quiver(py, pt, np.cosh(rapidity), np.sinh(rapidity),
                       color="tab:orange", angles="xy", scale_units="xy",
                       scale=2.5, width=0.006)  # e_(1), the unit space direction
```

Two panels. On the left, for $\tau = 1$ and $\tau = 2$, the dotted curve $(y, t) = (\tau\sinh\theta, \tau\cosh\theta)$ for 200 values of $\theta$, and at five rapidities $\theta = -1, -0.5, 0, 0.5, 1$ the frame: the unit time direction $(\sinh\theta, \cosh\theta)$ in blue and the unit space direction $(\cosh\theta, \sinh\theta)$ in orange, both in $(y, t)$ components, drawn with `quiver` as in Notebook 06a.

```python
light = np.linspace(0.0, 3.6, 2)
ax_left.plot(light, light, "--", color="black", linewidth=0.8)  # t = y
ax_left.plot(-light, light, "--", color="black", linewidth=0.8,
             label="light lines $t = \\pm y$")  # t = -y
ax_left.plot([], [], color="tab:blue", label="unit time direction $e_{(0)}$")
ax_left.plot([], [], color="tab:orange", label="unit space direction $e_{(1)}$")
```

The two dashed light lines $t = y$ and $t = -y$ from the origin, and two empty plots for the legend.

```python
ax_left.set_xlim(-3.6, 3.6)
ax_left.set_ylim(0.0, 4.6)
ax_left.set_aspect("equal")
ax_left.set_xlabel("space coordinate $y = \\tau\\sinh\\theta$")
ax_left.set_ylabel("time $t = \\tau\\cosh\\theta$")
ax_left.set_title("The Milne frame is boosted along $\\theta$")
ax_left.legend(loc="upper center", fontsize=7)
```

Axis ranges, equal units, labels, title and legend.

```python
rapidities = np.linspace(-4.0, 4.0, 401)
ax_right.plot(rapidities, np.exp(rapidities / 2),
              label="$U_{11} = e^{\\theta/2}$")
ax_right.plot(rapidities, np.exp(-rapidities / 2), "--",
              label="$U_{22} = e^{-\\theta/2}$")
ax_right.plot(rapidities, np.cosh(rapidities / 2), ":", color="black",
              label="$\\cosh(\\theta/2)$")
ax_right.plot(rapidities, np.sinh(rapidities / 2), "-.", color="gray",
              label="$\\sinh(\\theta/2)$")
ax_right.set_xlabel("rapidity $\\theta$")
ax_right.set_ylabel("entry of the spinor boost (pure number)")
ax_right.set_title("A spinor boost is real and grows")
ax_right.legend(fontsize=8)
```

The right panel: for $\theta$ from $-4$ to $4$ the two diagonal entries of the spinor boost, $e^{\theta/2}$ and $e^{-\theta/2}$ (because $\gamma^0\gamma^1 = \mathrm{diag}(1, -1)$, $U = \mathrm{diag}(\cosh\frac\theta2 + \sinh\frac\theta2, \cosh\frac\theta2 - \sinh\frac\theta2)$), and for comparison $\cosh\frac\theta2$ and $\sinh\frac\theta2$.

```python
save_figure(fig, "milne_frame_and_spin_boost",
            "The Milne wedge, a flat plane with one time in which the notebook's "
            ...
            "and unbounded, unlike a spinor rotation.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.2 shows.** On the left, the frame at $\theta = 0$ is upright (time up, space to the right); moving along $\theta$ the blue and orange arrows tilt symmetrically towards the dashed light lines, as in figure 1 of Notebook 06b: the frame is boosted along $\theta$, and the correct spin connection $\omega_{\theta01} = -1$ records this rate, although the plane is flat. On the right, the entries $e^{\pm\theta/2}$ of the spinor boost grow or fall without bound and never return, unlike the spinor rotation of figure 1 of Notebook 06a, which came back after $4\pi$. The mixed contraction would delete this whole connection.

**In [8], the author's metric: the correct and the mixed spinor connection** (Section 6.23).

```python
from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation
```

The reader of Wolfram notation.

```python
x = sp.symbols("x1:9", real=True)  # x[0] = x1, ..., x[3] = x4, ..., x[7] = x8
x4, x8 = x[3], x[7]
H = sp.Symbol("H", positive=True)  # the author's constant H > 0
a4 = sp.Function("a4")(x4)  # any function of the time
a4p = sp.Derivative(a4, x4)  # a4'
z = 6 * H * x8  # the hidden angle
s = sp.sin(z) ** sp.Rational(1, 6)
f = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3 + [sp.cot(z)]
g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the author's metric
e = sp.diag(*f)  # the diagonal vielbein
```

The symbols, the factors, the metric and the diagonal vielbein, as in Notebook 06a, In [7]; `a4p` is a short name for $a_4'$.

```python
Gam = christoffel(g, x)
mixed = mixed_spin_connection(e, Gam, x)  # omega_mu^a_b
omega = lower_first_index(mixed, ETA)  # omega_mu ab
```

The Christoffel symbols, the mixed connection $\omega_\mu{}^a{}_b$ and the lowered connection $\omega_{\mu ab}$.

```python
# The record lists {mu, a, b, value} with a < b, numbered 1..8, in Wolfram notation.
text = FORMULAS["omega_nonzero"].replace("Derivative[1][a4][x4]", "a4p")
text = text.replace("a4[x4]", "a4")
names = {sp.Symbol("H"): H, sp.Symbol("x8"): x8, sp.Symbol("a4"): a4,
         sp.Symbol("a4p"): a4p}
omega_record = {(int(m) - 1, int(a) - 1, int(b) - 1): v.subs(names, simultaneous=True)
                for m, a, b, v in parse_mathematica(text)}
```

The record's list `omega_nonzero` is read: its Wolfram names for $a_4'$ and $a_4$ are shortened, the text is parsed, the plain symbols are replaced by the notebook's, and the directions are renumbered from 1..8 to 0..7.

```python
nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a, b in pairs
           if omega[mu][a][b] != 0}
check(set(nonzero) == set(omega_record)
      and all(is_zero(nonzero[k] - omega_record[k]) for k in nonzero),
      "the 12 nonzero lowered components omega_mu ab equal the record",
      record=f"{THEORY_FILE}, formula omega_nonzero")
```

The nonzero lowered components with $a < b$, compared with the record: the same twelve keys and the same values.

```python
ACTION = {1: "kept", -1: "sign reversed", 0: "deleted"}
for (mu, a, b) in sorted(nonzero):
    k = int(factor[a][b])
    say(f"omega_{NAMES[mu]},{NAMES[a]}{NAMES[b]}: {KIND[k]} pair, {ACTION[k]}")
```

For each of the twelve components (sorted by their keys) one line is printed with the kind of its pair and what the mixed contraction does to it, for example `omega_x1,x1x4: boost pair, deleted` and `omega_x5,x4x5: time-time pair, sign reversed`.

```python
Omega = contract(omega, S)  # the correct spinor connection
Omega_nb = contract(mixed, S)  # the notebook's contraction
```

The correct spinor connection is the contraction of the lowered components, the mixed one the contraction of the mixed components; the same function `contract` makes both.

```python
def part(kind):
    """The part of Omega that comes from the pairs of one kind."""
    return contract([[[omega[mu][a][b] if factor[a][b] == kind else 0
                       for b in range(8)] for a in range(8)] for mu in range(8)], S)
```

`part(kind)` keeps only the lowered components whose pair is of the given kind (all others are set to 0) and contracts them: the parts $\Omega^{ss}$, $\Omega^{tt}$ and $\Omega^{st}$.

```python
Omega_ss, Omega_tt, Omega_st = part(1), part(-1), part(0)
check(all(matrix_is_zero(Omega[mu] - Omega_ss[mu] - Omega_tt[mu] - Omega_st[mu])
          and matrix_is_zero(Omega_nb[mu] - Omega_ss[mu] + Omega_tt[mu])
          for mu in range(8)),
      "Omega^nb_mu = Omega^ss_mu - Omega^tt_mu for all eight mu (boosts deleted)")
```

The check of the identity of Section 6.23 for all eight $\mu$: $\Omega_\mu$ is the sum of its three parts, and $\Omega^{nb}_\mu = \Omega^{ss}_\mu - \Omega^{tt}_\mu$. The cell prints twelve lines and two PASS lines.

**In [9], the closed forms.**

```python
closed_ok = True
for i in (0, 1, 2):  # the 3-space directions x1, x2, x3
    closed_ok = closed_ok and matrix_is_zero(
        Omega_nb[i] - sp.exp(a4) * s * H * S[i][7])  # pair (xi, x8) kept
    closed_ok = closed_ok and matrix_is_zero(
        Omega[i] - sp.exp(a4) * s * (a4p * S[i][3] + H * S[i][7]))
for t in (4, 5, 6):  # the extra times x5, x6, x7
    closed_ok = closed_ok and matrix_is_zero(
        Omega_nb[t] - sp.exp(-a4) * s * a4p * S[3][t])  # pair (x4, xt) reversed
    closed_ok = closed_ok and matrix_is_zero(
        Omega[t] + sp.exp(-a4) * s * (a4p * S[3][t] + H * S[t][7]))
check(closed_ok, "the closed forms of Omega_mu and Omega^nb_mu for x1 ... x3, "
      "x5 ... x7")
```

For the three 3-space directions (positions 0, 1, 2) the check requires $\Omega^{nb}_{x_i} = e^{a_4}s\,H\,S^{x_ix8}$ and $\Omega_{x_i} = e^{a_4}s\,(a_4'S^{x_ix4} + HS^{x_ix8})$ (`S[i][7]` is $S^{x_ix8}$, `S[i][3]` is $S^{x_ix4}$); for the three extra times (positions 4, 5, 6), $\Omega^{nb}_{x_t} = e^{-a_4}s\,a_4'S^{x4x_t}$ and $\Omega_{x_t} = -e^{-a_4}s\,(a_4'S^{x4x_t} + HS^{x_tx8})$. One PASS line.

**In [10], the two contractions direction by direction.**

```python
gup = curved_gammas(e, gamma)  # gamma^mu = gamma^a / f_a for mu = a
```

The curved gammas.

```python
def split(M):
    """(alpha, beta, rest is zero) for M = alpha gamma^(x4) + beta gamma^(x8)."""
    alpha = sp.simplify(-(M * gamma[3]).trace() / 16)  # coefficient of gamma^(x4)
    beta = sp.simplify((M * gamma[7]).trace() / 16)  # coefficient of gamma^(x8)
    return alpha, beta, matrix_is_zero(M - alpha * gamma[3] - beta * gamma[7])
```

`split(M)` returns the coefficients $\alpha$ of $\gamma^{(x4)}$ and $\beta$ of $\gamma^{(x8)}$, found with traces as in Section 6.8, and whether nothing else is left.

```python
correct_terms = [split(gup[mu] * Omega[mu]) for mu in range(8)]
notebook_terms = [split(gup[mu] * Omega_nb[mu]) for mu in range(8)]
for mu in range(8):
    say(f"{NAMES[mu]}: correct ({correct_terms[mu][0]}, {correct_terms[mu][1]}), "
        f"notebook ({notebook_terms[mu][0]}, {notebook_terms[mu][1]})")
```

Both contractions are split for each direction and printed side by side, eight lines such as `x5: correct (-Derivative(a4(x4), x4)/2, H/2), notebook (Derivative(a4(x4), x4)/2, 0)`.

```python
want_nb = [(0, H / 2)] * 3 + [(0, 0)] + [(a4p / 2, 0)] * 3 + [(0, 0)]
check(all(term[2] for term in correct_terms + notebook_terms)
      and all(is_zero(notebook_terms[mu][0] - want_nb[mu][0])
              and is_zero(notebook_terms[mu][1] - want_nb[mu][1]) for mu in range(8)),
      "notebook's terms: (H/2) gamma^(x8) for x1, x2, x3; (a4'/2) gamma^(x4) for "
      "x5, x6, x7")
```

The check requires every split to leave nothing over and the mixed terms to be $(0, \frac H2)$ for $x1, x2, x3$, $(\frac{a_4'}{2}, 0)$ for $x5, x6, x7$ and $(0, 0)$ for $x4$ and $x8$, as derived in Section 6.23.

```python
slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
slash_nb = sum((gup[mu] * Omega_nb[mu] for mu in range(8)), Z16)
total_record = parse_mathematica(FORMULAS["gammaOmega_total"].replace(
    'gamma["x8"]', "G8")).subs({sp.Symbol("H"): H, sp.Symbol("G8"): 1})
check(matrix_is_zero(slash - total_record * gamma[7])
      and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_3H_gamma_x8"),
      "correct: gamma^mu Omega_mu = 3 H gamma^(x8)",
      record=f"{THEORY_FILE}, formula gammaOmega_total")
```

The two totals. The record's formula `gammaOmega_total` is the text `3*H*gamma["x8"]`; replacing `gamma["x8"]` by a symbol `G8`, reading it, and setting $G8 = 1$ gives the number $3H$, the coefficient of $\gamma^{(x8)}$. The check requires the correct total to be $3H\gamma^{(x8)}$ and the sympy report to record the same.

```python
report("notebook: coefficient of gamma^(x8)", sum(t[1] for t in notebook_terms))
report("notebook: coefficient of gamma^(x4)", sum(t[0] for t in notebook_terms))
check(matrix_is_zero(slash_nb - 3 * H / 2 * gamma[7] - 3 * a4p / 2 * gamma[3]),
      "notebook: gamma^mu Omega^nb_mu = (3H/2) gamma^(x8) + (3 a4'/2) gamma^(x4)")
```

Two RESULT lines print the mixed coefficients $\frac{3H}{2}$ and $\frac{3a_4'}{2}$, and the last check requires the mixed total to be exactly $\frac{3H}{2}\gamma^{(x8)} + \frac{3a_4'}{2}\gamma^{(x4)}$. The cell prints eight lines, three PASS lines and two RESULT lines.

**In [11], figure 3.**

```python
positions = np.arange(8)
width = 0.38  # the width of one bar; two bars side by side per direction
alpha_c = [float(sp.simplify(t[0] / a4p)) for t in correct_terms]  # units of a4'
alpha_n = [float(sp.simplify(t[0] / a4p)) for t in notebook_terms]
beta_c = [float(sp.simplify(t[1] / H)) for t in correct_terms]  # units of H
beta_n = [float(sp.simplify(t[1] / H)) for t in notebook_terms]
```

The places of the bars, the width of one bar (two bars side by side for each direction), and the coefficients in units of $a_4'$ and of $H$ for both contractions.

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
ax_left.bar(positions - width / 2, alpha_c, width, color="tab:blue",
            label=f"correct (total {sum(alpha_c):g})")
ax_left.bar(positions + width / 2, alpha_n, width, color="lightskyblue",
            label=f"notebook (total {sum(alpha_n):g})")
ax_right.bar(positions - width / 2, beta_c, width, color="tab:red",
             label=f"correct (total {sum(beta_c):g})")
ax_right.bar(positions + width / 2, beta_n, width, color="lightsalmon",
             label=f"notebook (total {sum(beta_n):g})")
```

Two bar charts with a common vertical axis: the correct bars dark (blue on the left, red on the right) and shifted half a bar to the left, the mixed bars light and shifted to the right; each label shows the total.

```python
ax_left.set_title("coefficient of $\\gamma^{(x4)}$, units of $a_4'$")
ax_right.set_title("coefficient of $\\gamma^{(x8)}$, units of $H$")
for ax in (ax_left, ax_right):
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, NAMES)
    ax.set_xlabel("direction $\\mu$ of the term $\\gamma^\\mu\\Omega_\\mu$")
    ax.set_ylim(-0.8, 0.8)
    ax.legend(fontsize=8, loc="lower left")
ax_left.set_ylabel("coefficient")
```

Titles, a zero line, the direction names, the axis range from $-0.8$ to $0.8$ and the legends.

```python
save_figure(fig, "per_direction_comparison",
            "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the author's "
            ...
            "to $3$, the notebook keeps only three of them, total $3/2$.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.3 shows.** On the left, the dark bars are $+\frac12$ for $x1, x2, x3$ and $-\frac12$ for $x5, x6, x7$ and cancel (total 0), while the light bars are zero for 3-space and $+\frac12$ for the extra times (total $\frac32$): the deleted boost parts of 3-space and the reversed time-time parts of the extra times destroy the cancellation. On the right, the six dark bars of height $\frac12$ add to 3, while the mixed contraction keeps only the three of 3-space (total $\frac32$): the boost parts $(x_t, x8)$ of the extra times are deleted.

**In [12], figure 4.**

```python
SAMPLE = {H: 1, x8: sp.pi / 24}  # H = 1 and z = 6 H x8 = pi/4


def at_sample(expr):
    """The decimal value of expr at H = 1, z = pi/4, a4 = 1/2, a4' = 1/2."""
    expr = sp.sympify(expr).subs(a4p, sp.Rational(1, 2))  # a4' first, then a4
    expr = expr.subs(a4, sp.Rational(1, 2))
    return float(sp.N(expr.subs(SAMPLE)))


def sample_table(matrix):
    """The matrix as an array of decimal numbers at the sample point."""
    return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])
```

The sample point of Notebook 06a ($H = 1$, $z = \pi/4$, $a_4 = a_4' = \frac12$; here no $a_4''$ occurs), with $a_4'$ replaced first; and `sample_table`, as in Notebook 06b.

```python
fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
for ax, (title, matrix) in zip(axes, (
        ("correct: $\\gamma^\\mu\\Omega_\\mu$", slash),
        ("notebook: $\\gamma^\\mu\\Omega^{nb}_\\mu$", slash_nb))):
    image = ax.imshow(sample_table(matrix), cmap="RdBu_r", vmin=-3.2, vmax=3.2)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
fig.colorbar(image, ax=axes, shrink=0.85, label="entry value")
```

Two heat maps on one common colour scale from $-3.2$ to $3.2$: the correct total and the mixed total.

```python
save_figure(fig, "contraction_heat_maps",
            "The total $\\gamma^\\mu\\Omega_\\mu$ as a 16 x 16 heat map at the sample "
            ...
            "deflation.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.4 shows.** On the left, the correct $3H\gamma^{(x8)}$: the value 3 (dark red) on two diagonal lines in the off-diagonal blocks, nothing else. On the right, the same two lines with half the value, 1.5, and in addition the pattern of $\gamma^{(x4)}$ with entries $\pm0.75$: with the mixed contraction the field equation would contain a term proportional to the rate $a_4'$ of the deflation.

**In [13], the covariant constancy** (Section 6.23).

```python
violation = {}  # (mu, nu) -> D^nb_mu gamma^nu, for the pairs where it is not zero
correct_ok, identity_ok, entries = True, True, 0
for mu in range(8):
    for nu in range(8):
        common = gup[nu].diff(x[mu]) + sum((Gam[nu][mu][lam] * gup[lam]
                                            for lam in range(8)), Z16)
        D_correct = common + Omega[mu] * gup[nu] - gup[nu] * Omega[mu]
        D_nb = common + Omega_nb[mu] * gup[nu] - gup[nu] * Omega_nb[mu]
        difference = Omega_nb[mu] - Omega[mu]
        correct_ok = correct_ok and matrix_is_zero(D_correct)
        identity_ok = identity_ok and matrix_is_zero(
            D_nb - (difference * gup[nu] - gup[nu] * difference))
        nonzero_entries = sum(1 for v in D_nb if not is_zero(v))
        if nonzero_entries:
            violation[(mu, nu)] = D_nb
            entries += nonzero_entries
```

For all 64 pairs $(\mu, \nu)$: `common` is the part $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda$ that both versions share; `D_correct` adds $[\Omega_\mu, \gamma^\nu]$ and `D_nb` adds $[\Omega^{nb}_\mu, \gamma^\nu]$. Three things are recorded: whether `D_correct` is zero, whether `D_nb` equals $[\Omega^{nb}_\mu - \Omega_\mu, \gamma^\nu]$, and how many entries of `D_nb` are not zero; the nonzero matrices are kept in the dictionary `violation`, and their nonzero entries are counted in `entries`.

```python
check(correct_ok and record_passed(REPORT_PY, "covariant_constancy_D_mu_gamma_nu"),
      "correct: D_mu gamma^nu = 0 for all 64 pairs",
      record=f"{REPORT_PY}, check covariant_constancy_D_mu_gamma_nu")
check(identity_ok, "D^nb_mu gamma^nu = [Omega^nb_mu - Omega_mu, gamma^nu], all 64")
```

Two checks: the correct version vanishes for all 64 pairs (with the record's check), and the identity of Section 6.23 holds for all 64.

```python
report("pairs (mu, nu) with D^nb_mu gamma^nu not zero", len(violation))
report("nonzero entries of these 16 x 16 matrices", entries)
say("violated pairs: " + ", ".join(f"({NAMES[m]},{NAMES[n]})"
                                   for m, n in sorted(violation)))
check(len(violation) == 15 and entries == 288,
      "notebook: D^nb_mu gamma^nu is not zero in 15 of 64 pairs (288 entries)")
```

Two RESULT lines print 15 pairs and 288 entries, one line lists the violated pairs, `(x1,x1), (x1,x4), ..., (x7,x8)`, and the check requires exactly 15 and 288, the numbers derived in Section 6.23.

```python
failures = [(mu, a) for mu in range(8) for a in range(8) if not matrix_is_zero(
    Omega_nb[mu] * gamma[a] - gamma[a] * Omega_nb[mu]
    + sum((mixed[mu][a][b] * gamma[b] for b in range(8)), Z16))]
report("pairs (mu, a) where the defining property fails for Omega^nb", len(failures))
check(len(failures) > 0 and all(matrix_is_zero(
    Omega[mu] * gamma[a] - gamma[a] * Omega[mu]
    + sum((mixed[mu][a][b] * gamma[b] for b in range(8)), Z16))
    for mu in range(8) for a in range(8)),
      "the defining property holds for Omega and fails for Omega^nb",
      record=f"{REPORT_WL}, check S_rotates_gamma_with_omega")
```

`failures` lists the pairs $(\mu, a)$ in which the defining property $[\Omega, \gamma^a] = -\sum_b\omega_\mu{}^a{}_b\gamma^b$ fails for $\Omega^{nb}$; a RESULT line prints their number, 15. The check requires at least one failure for $\Omega^{nb}$ and none for the correct $\Omega$ (all 64 pairs), with the WolframScript report's check. The cell prints three PASS lines, three RESULT lines and the list.

**In [14], figure 5.**

```python
size = np.zeros((8, 8))
for (mu, nu), matrix in violation.items():
    size[mu, nu] = np.abs(sample_table(matrix)).max()  # the largest entry
```

For each violated pair, the largest absolute entry of $D^{nb}_\mu\gamma^\nu$ at the sample point.

```python
fig, ax = plt.subplots(figsize=(6.4, 5.4))
image = ax.imshow(size, cmap="Oranges", vmin=0.0)
for (mu, nu) in violation:
    dark = size[mu, nu] > 0.6 * size.max()  # white digits on dark squares
    ax.text(nu, mu, f"{size[mu, nu]:.2f}", ha="center", va="center", fontsize=7,
            color="white" if dark else "black")
ax.set_xticks(range(8), NAMES)
ax.set_yticks(range(8), NAMES)
ax.set_xlabel("upper index $\\nu$ of $\\gamma^\\nu$")
ax.set_ylabel("derivative index $\\mu$")
ax.set_title("Largest entry of $D^{nb}_\\mu\\gamma^\\nu$ at the sample point")
ax.grid(False)
fig.colorbar(image, ax=ax, shrink=0.8, label="largest absolute entry")
```

A heat map in shades of orange with the values written into the squares (white digits on the dark squares), the derivative index $\mu$ as rows and the upper index $\nu$ as columns, and a colour bar.

```python
save_figure(fig, "constancy_violation",
            "Where the notebook's contraction breaks the covariant constancy of the "
            ...
            "connection all 64 matrices vanish exactly.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.5 shows.** Only the rows of the six warped directions have coloured squares; the rows $x4$ and $x8$ are white because $\Omega_{x4} = \Omega_{x8} = 0$ in both versions. Each 3-space row has two squares: $(x_i, x_i) = 0.50$, which is $a_4' = \frac12$, and $(x_i, x4) = 0.78$, which is $f_1a_4' = 1.556 \cdot \frac12$. Each extra-time row has three: $(x_t, x_t) = 1.00$, the larger of $2a_4' = 1$ and $H = 1$, and $(x_t, x4) = (x_t, x8) = 0.57$, which is $2f_5a_4' = f_5H = 0.572$ at $z = \pi/4$ ($\tan z = 1$). All values are those derived in Section 6.23. With the correct connection the whole grid would be white.

**In [15], why only $3H$ is right** (Section 6.24).

```python
sqrt_g = sp.cos(z)  # sqrt|det g| of the author's metric
divergence = sum(((sqrt_g * gup[mu]).diff(x[mu]) for mu in range(8)), Z16) / (2 * sqrt_g)
check(matrix_is_zero(divergence - slash) and not matrix_is_zero(divergence - slash_nb),
      "the divergence form equals the correct contraction, not the notebook's",
      record=f"{REPORT_WL}, check gammaOmega_divergence_form")
```

The divergence form with $\sqrt{\lvert g\rvert} = \cos z$; the check requires it to equal the correct contraction and NOT the mixed one (`not matrix_is_zero(...)`).

```python
p = sp.Function("p")(x8)  # two arbitrary functions of x8
q = sp.Function("q")(x8)
c = sp.Symbol("c", real=True)  # the coefficient of gamma^(x8)
```

Two arbitrary functions $p(x_8)$, $q(x_8)$ and a real symbol $c$ for the coefficient of $\gamma^{(x8)}$.

```python
def A(u):
    """The hidden-direction operator A_c u = tan z du/dx8 + c u."""
    return sp.tan(z) * u.diff(x8) + c * u
```

The hidden-direction operator $A_cu = \tan z\,\partial_8u + c\,u$.

```python
leftover = sp.cos(z) * (p * A(q) + A(p) * q) - sp.diff(sp.sin(z) * p * q, x8)
check(is_zero(leftover - (2 * c - 6 * H) * sp.cos(z) * p * q),
      "cos z (p A_c q + (A_c p) q) - d8(sin z p q) = (2c - 6H) cos z p q")
```

`leftover` is $\cos z\,(p\,A_cq + (A_cp)\,q) - \partial_8(\sin z\,p\,q)$, and the check requires it to be $(2c - 6H)\cos z\,p\,q$ exactly, for every $c$ and all functions $p$, $q$.

```python
record_text = FORMULAS["hidden_direction_hermiticity"]
check(is_zero(leftover.subs(c, 3 * H)) and "Tan[z] d8 + 3 H" in record_text
      and "= d8 (Sin[z] p q)" in record_text,
      "c = 3H: A_c is antisymmetric for the weight cos z up to d8(sin z p q)",
      record=f"{THEORY_FILE}, formula hidden_direction_hermiticity")
```

For $c = 3H$ the leftover vanishes; and the record's text of `hidden_direction_hermiticity` must contain the operator `Tan[z] d8 + 3 H` and the boundary term `= d8 (Sin[z] p q)`.

```python
check(is_zero(leftover.subs(c, 3 * H / 2) + 3 * H * sp.cos(z) * p * q),
      "c = 3H/2 (notebook): the leftover -3 H cos z p q remains")
```

For the mixed value $c = \frac32H$ the leftover is $-3H\cos z\,p\,q$. The cell prints four PASS lines, two with records.

**In [16], figure 6.**

```python
zz = np.linspace(0.0, np.pi / 2, 300)  # the hidden angle z from 0 to pi/2
fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.axhline(0.0, color="gray", linewidth=0.6, zorder=1)  # the zero line, underneath
for value, style, width, label in ((3.0, "-", 2.5, "correct $c = 3H$"),
                                   (1.5, "--", 1.5, "notebook $c = 3H/2$"),
                                   (0.0, ":", 1.5, "no connection term, $c = 0$")):
    ax.plot(zz, (2 * value - 6) * np.cos(zz), style, linewidth=width, label=label,
            zorder=3)  # drawn above the zero line
ax.set_xlabel("hidden angle $z = 6Hx_8$ (radians)")
ax.set_ylabel("leftover coefficient $(2c/H - 6)\\cos z$")
ax.set_title("Only $c = 3H$ makes the hidden operator antisymmetric")
ax.legend(fontsize=8)
```

300 values of $z$ from $0$ to $\pi/2$. A thin gray zero line is drawn first (`zorder=1` puts it underneath), then the leftover coefficient $(2c/H - 6)\cos z$ for $c = 3H$ (thick solid), $c = \frac32H$ (dashed) and $c = 0$ (dotted), above it (`zorder=3`).

```python
save_figure(fig, "hermiticity_defect",
            "The term that spoils the antisymmetry of the hidden-direction operator "
            ...
            "term; the solid line lies on the zero line.")
```

The figure is saved; the cell prints its file name.

**What Figure 06c.6 shows.** The thick solid line of the correct value $c = 3H$ lies on the zero line for every $z$: nothing is left but the boundary term. The dashed line of the mixed value starts at $-3$ at the tip and rises to 0 at the patch end, and the dotted line of $c = 0$ starts at $-6$. Only the correct coefficient makes the hidden-direction operator antisymmetric for the volume weight $\cos z$.

**In [17], the last checks.**

```python
cited = {
    REPORT_PY: ["clifford_relations", "gammas_real", "vielbein_postulate",
                "spin_connection_antisymmetric", "covariant_constancy_D_mu_gamma_nu",
                "gamma_mu_Omega_mu_equals_3H_gamma_x8", "divergence_of_sqrtg_gamma"],
    REPORT_WL: ["omega_components", "S_rotates_gamma_with_omega",
                "gamma_covariantly_constant", "gammaOmega_equals_3H_gamma_x8",
                "gammaOmega_divergence_form", "good_sector_hermiticity_curved"],
}
count = sum(len(names) for names in cited.values())
check(all(record_passed(path, name) for path, names in cited.items()
          for name in names),
      f"the {count} cited record checks are recorded as passed")
```

The 13 cited checks, 7 of the sympy field-theory report and 6 of the WolframScript one, each stating a correct result reproduced here; the check requires all of them to be recorded as passed.

```python
expected = [f"06c_{k}_{name}.png" for k, name in enumerate([
    "pair_kinds", "milne_frame_and_spin_boost", "per_direction_comparison",
    "contraction_heat_maps", "constancy_violation", "hermiticity_defect"], 1)]
check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
      "all six figure files exist")
all_checks_passed()
```

The six figure files must exist, and the last line is printed: ALL 27 CHECKS PASSED (notebook 06c).

### 6.29 The exact scope of the statement that gravity enters the field equations

The author asked that the field equations of both fields "always possess non-zero contributions from gravity (through the canonical spin-connection, unless we are in flat 4+4 spacetime)". This chapter has proved several exact statements, and they must be read together. The Revision record states the conclusion in its own correction (in `Revision/README.md`): the non-triviality tests [1] and [2] hold in a qualified sense. Here is that sense, statement by statement.

**What is true in the diagonal vielbein.** $\sum_\mu\gamma^\mu D_\mu\Psi - \sum_\mu\gamma^\mu\partial_\mu\Psi = 3H\gamma^{(x8)}\Psi$, which is nonzero for every $H > 0$, every function $a_4$ and every field that is not zero (Sections 6.8 and 6.10).

**Where the term comes from.** The Lagrangian of Chapter 7 contains the symmetric kinetic term $\frac12\sum_\mu\big(\bar\Psi\gamma^\mu D_\mu\Psi - (D_\mu\bar\Psi)\gamma^\mu\Psi\big)$. Insert $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and $D_\mu\bar\Psi = \partial_\mu\bar\Psi - \bar\Psi\Omega_\mu$ (Section 6.7):

$$
\tfrac12\sum_\mu\big(\bar\Psi\gamma^\mu\partial_\mu\Psi - (\partial_\mu\bar\Psi)\gamma^\mu\Psi\big) + \tfrac12\sum_\mu\bar\Psi\big(\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu\big)\Psi
$$

(multiply out; the two $\Omega$ terms collect into one). By Fact 1 of Section 6.9 the last bracket vanishes for each $\mu$ separately. **In the author's metric and the diagonal vielbein the canonical spin connection drops out of the Lagrangian completely.** The term $3H\gamma^{(x8)}$ comes back in the field equation from the volume factor and the vielbein: vary the connection-free term $\sqrt{\lvert g\rvert}\,\frac12\sum_\mu(\bar\Psi\gamma^\mu\partial_\mu\Psi - (\partial_\mu\bar\Psi)\gamma^\mu\Psi)$ with respect to $\bar\Psi$ by the Euler-Lagrange rule of Chapter 7 (the derivative by $\bar\Psi$ minus $\sum_\mu\partial_\mu$ of the derivative by $\partial_\mu\bar\Psi$, the two treated as independent):

$$
\tfrac12\sqrt{\lvert g\rvert}\sum_\mu\gamma^\mu\partial_\mu\Psi - \sum_\mu\partial_\mu\Big(-\tfrac12\sqrt{\lvert g\rvert}\,\gamma^\mu\Psi\Big) = \sqrt{\lvert g\rvert}\sum_\mu\gamma^\mu\partial_\mu\Psi + \tfrac12\sum_\mu\partial_\mu\big(\sqrt{\lvert g\rvert}\,\gamma^\mu\big)\Psi
$$

(the product rule on the second term). Divided by $\sqrt{\lvert g\rvert}$ the last term is the divergence form of Section 6.9, $\sum_\mu\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(x8)}\Psi$. The record calls it the **half-density term** (volume and vielbein divergence). Chapter 7 carries out the variation for both statistics with every sign. Records: both scope reports, check `connection_free_lagrangian_same_equations`; `wolfram-field-theory.json`, checks `L_spin_connection_drops_out_G` and `L_spin_connection_drops_out_C`.

**What depends on choices.** The value $3H\gamma^{(x8)}$ belongs to the diagonal vielbein: in the frame boosted with the rate $\beta = 6H$ the contraction vanishes identically (Section 6.16). It also belongs to the field variable $\Psi$: for $\chi = \sin^{1/2}(z)\,\Psi$ the term is absent for $U = 0$ and becomes the coupling $\lambda S[\chi]/\sin z$ for $U = \frac\lambda2S^2$ (Section 6.18). It contains no trace of the deflation (Section 6.8).

**What does not depend on any choice.**

- The spin connection vanishes in no frame: its curvature is the Riemann curvature, $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$, and $R^{x8}{}_{x8} = -6H^2 \neq 0$ for every $H > 0$ (Section 6.17). The metric is curved for every member of the family.
- The vielbein enters every derivative term of the field equation through the factors $e^{\mp a_4}s^{-1}$ and $\tan z$; this is where the inflation of 3-space and the exponential deflation of the extra times act on the fields (Section 6.10).
- The spin connection reaches the energy-momentum tensor of the fields: for a configuration that depends on the time only, the off-diagonal kinetic term $K^{x4}{}_{x1}$ has the connection part $\frac12e^{a_4}s\,H\,\bar\Phi\gamma^{(x4)}\gamma^{(x1)}\gamma^{(x8)}\Phi$, which is not identically zero (both scope reports, check `spin_connection_in_the_energy_momentum_tensor`; Chapter 9 treats the energy-momentum tensor).

**In one sentence.** Gravity enters the field equations of both fields in every frame and every choice of field variables, through the vielbein factors and through a spin connection whose curvature cannot be removed; the particular matrix $3H\gamma^{(x8)}$ is the form this takes in the diagonal vielbein with the variable $\Psi$, and it is a property of these choices, not of the physics alone. Chapter 8 returns to this scope and adds the question of well-posedness.

| statement | status | where it is verified |
| --- | --- | --- |
| the connection drops out of the symmetric Lagrangian; the field equations are those of the connection-free symmetric Lagrangian, with the half-density term | PROVED | both scope reports, check `connection_free_lagrangian_same_equations`; `wolfram-field-theory.json`, checks `L_spin_connection_drops_out_G`, `L_spin_connection_drops_out_C` |
| the value $3H\gamma^{(x8)}$ is frame-dependent and removable by a rescaling | PROVED | Sections 6.16 and 6.18 (scope reports) |
| the spin connection vanishes in no frame; the metric is never flat | PROVED | Section 6.17 |
| the connection enters the energy-momentum tensor | PROVED | both scope reports, check `spin_connection_in_the_energy_momentum_tensor` |

### 6.30 What we proved, what we computed, what we assumed

**PROVED** (exact; derived in this chapter line by line, confirmed by exact checks of the notebooks named, and, where stated, by the Revision record):

- The diagonal vielbein $f = (e^{a_4}s\ (\times3),\ 1,\ e^{-a_4}s\ (\times3),\ \cot z)$ reproduces the author's metric; $\sqrt{\lvert\det g\rvert} = \cos z$ does not depend on the time; the curved gammas obey $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}$; every $\Lambda e$ with $\Lambda^T\eta\Lambda = \eta$ is another vielbein (Section 6.2; Notebook 06a, In [7]; `field-theory.json`, formulas `metric`, `vielbein_diagonal`; `python-field-theory.json`, check `sqrt_det_g_equals_cos_z`).
- The 25 independent nonzero Christoffel symbols (Section 6.3; Notebook 06a, In [9]; formula `christoffel_nonzero`, check `christoffel_count`).
- The vielbein postulate has exactly one solution, the canonical spin connection, and its lowered form is antisymmetric; for the author's metric it has exactly 12 independent nonzero components, each $a_4'$ or $H$ times a nonvanishing factor (Sections 6.4 and 6.6; Notebook 06a, In [11]; formula `omega_nonzero`; checks `vielbein_postulate`, `spin_connection_antisymmetric`, `omega_components`, `Omega_vanishes_iff_a4prime_and_H_vanish`).
- $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ is the unique traceless solution of the defining property; it makes the curved gammas covariantly constant; $\Omega_{x4} = \Omega_{x8} = 0$ (Section 6.7; Notebook 06a, In [13]; checks `S_rotates_gamma_with_omega`, `covariant_constancy_D_mu_gamma_nu`, `Omega_x4_and_Omega_x8_vanish`).
- $\gamma^\mu\Omega_\mu = 3H\gamma^{(x8)}$ in the diagonal vielbein, for every $H > 0$ and every $a_4$: the time-direction terms $\pm\frac12a_4'$ of the three inflating and the three deflating directions cancel, the six hidden terms $\frac12H$ add; equivalently, the divergence form (Sections 6.8 and 6.9; Notebook 06a, In [15] and In [18]; formulas `gammaOmega_per_direction`, `gammaOmega_total`; checks `gammaOmega_x4_terms_cancel`, `gamma_mu_Omega_mu_equals_3H_gamma_x8`, `gamma_Omega_equals_3H_gamma8`, `gammaOmega_divergence_form`).
- The Dirac operator written out, all sixteen components; the term $3H\gamma^{(x8)}\Psi$ vanishes only for $\Psi = 0$, for both fields (Section 6.10; Notebook 06a, In [20]; checks `Dirac_operator_explicit_G`, `Dirac_operator_explicit_C`, `nontriviality_1_dirac16complex`, `nontriviality_2_dirac16complex00`).
- The negative control: with inflating extra times the contraction is $3a_4'\gamma^{(x4)} + 3H\gamma^{(x8)}$; the cancellation is caused by the deflation (Section 6.10; Notebook 06a, In [22]; lead report, check `negative_control_inflating_extra_times`).
- Local spin covariance $\Omega'_\mu = R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$, $\gamma'^\mu = R\gamma^\mu R^{-1}$, $F' = RFR^{-1}$ (Sections 6.15 and 6.17; Notebook 06b, In [12] and In [15]).
- In the frame boosted with $b = \beta x_4 + b_0$, $\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}(\cosh b\,\gamma^{(x8)} - \sinh b\,\gamma^{(x4)})$, zero for $\beta = 6H$ while $\Omega'_\mu \neq 0$ for $x1, \dots, x7$ (Section 6.16; Notebook 06b, In [8] and In [10]; both scope reports, checks `boosted_frame_gammaOmega_formula`, `boosted_frame_gammaOmega_vanishes`).
- The Ricci components, $R = 6(a_4'^2 - 7H^2)$, and $R^{x8}{}_{x8} = -6H^2$ (by hand): the metric is never flat; the contraction is blind to the deflation while $R^{x4}{}_{x4} = 6a_4'^2$; $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$ in all 28 planes; $F'_{x1x8} \neq 0$ in the boosted frame (Section 6.17, whose table names the field-theory and scope checks of the record that prove the same; Notebook 06b, In [13] and In [15]).
- The rescaling $\Psi = \sin^{-1/2}(z)\chi$ removes the term; with $U = \frac\lambda2S^2$ it becomes $\lambda S[\chi]/\sin z$ (Section 6.18; Notebook 06b, In [17]; checks `rescaling_removes_the_connection_term`, `rescaled_equation_quadratic_potential`).
- The mixed contraction equals $\Omega^{ss} - \Omega^{tt}$: it keeps 6, reverses 6 and deletes 16 of the 28 parts; it agrees with the correct one in the polar plane and deletes the whole connection in the Milne wedge (Section 6.23; Notebook 06c, In [4], In [6], In [8]).
- Only $c = 3H$ makes the hidden-direction operator antisymmetric for the weight $\cos z$, up to the boundary term $[\sin z\,p\,q]$ (Section 6.24; Notebook 06c, In [15]; formula `hidden_direction_hermiticity`; check `good_sector_hermiticity_curved`).
- In the diagonal vielbein the canonical connection drops out of the symmetric Lagrangian, and $3H\gamma^{(x8)}$ is the half-density term of its field equation (Section 6.29; check `connection_free_lagrangian_same_equations`).

**COMPUTED** (by the notebooks):

- The central difference of Notebook 06a, In [19], reproduces the constant $3H$ to $1.9 \times 10^{-9}$, the size $18h^2$ expected for the step $h = 10^{-5}$.
- The figures at the sample point $H = 1$, $z = \pi/4$, $a_4 = a_4' = \frac12$: for example $\omega_{x1\,x1x4} = 0.78$, $\omega_{x5\,x5x8} = -0.57$, the largest spinor curvature $\lVert F_{\mu\nu}\rVert = 3.633$ (in units of $H^2$; Notebook 06b, In [16]) with 27 of 28 planes curved there.
- Exact counts made by the notebooks themselves, not stated in the Revision record: 13 nonzero components of the boosted spin connection (Notebook 06b, In [7]); 78 nonzero Riemann components with $\mu < \nu$ (Notebook 06b, In [13]); for the mixed contraction, $\frac{3H}{2}\gamma^{(x8)} + \frac{3a_4'}{2}\gamma^{(x4)}$, 15 violated pairs with 288 nonzero entries, and 15 pairs in which its defining property fails (Notebook 06c, In [10] and In [13]). These describe a contraction that the record does not use.

**ASSUMED**: the author's metric and the roles of his coordinates (the input of the theory); the illustrative history $a_4 = x_4$ with $H = 1$ in figures 2 and 9 of Notebook 06a (the prescribed background of Chapter 3; no result depends on it); two standard theorems quoted without proof: Jacobi's formula for the derivative of a determinant (Section 6.15) and the general identity $F_{\mu\nu} = \frac12R_{ab\mu\nu}S^{ab}$, which is however checked exactly for the author's metric (Section 6.17); and the record's statement about the author's notebook contraction (Section 6.23), which this book takes from `Revision/SPEC.md`.

**HYPOTHESIS and OPEN**: this chapter states no hypothesis. The boundary condition at the patch end $z = \pi/2$, needed for the antisymmetry of the hidden-direction operator, is not fixed here (Section 6.24); Chapter 14 assumes the $Z_2$ mirror. Nothing in this chapter concerns the creation of universes or matter and antimatter.

### 6.31 Exercises

**Exercise 1 (the sphere).** The unit sphere has the metric $ds^2 = d\theta^2 + \sin^2\theta\,d\varphi^2$ ($0 < \theta < \pi$), the frame metric $\eta = \mathrm{diag}(1, 1)$, the vielbein factors $f_\theta = 1$, $f_\varphi = \sin\theta$, and the gammas $\gamma^0 = \sigma_1$, $\gamma^1 = \sigma_2$. Compute the Christoffel symbols, the spin connection, $\Omega_\mu$, $\sum_\mu\gamma^\mu\Omega_\mu$ (check it with the divergence form) and $F_{\theta\varphi}$. Is the sphere flat?

*Answer.* Case (c) of Section 6.3: $\Gamma^\theta{}_{\varphi\varphi} = -f_\varphi\partial_\theta f_\varphi/f_\theta^2 = -\sin\theta\cos\theta$; case (b): $\Gamma^\varphi{}_{\varphi\theta} = \partial_\theta\ln\sin\theta = \cot\theta$; all others vanish. By Section 6.6 the only nonzero component is $\omega_{\varphi\,10} = \eta_{11}\,\partial_\theta f_\varphi/f_\theta = \cos\theta$, so $\omega_{\varphi\,01} = -\cos\theta$. With $S^{01} = \frac12\sigma_1\sigma_2 = \frac i2\sigma_3$: $\Omega_\varphi = -\cos\theta\,S^{01} = -\frac i2\cos\theta\,\sigma_3$ and $\Omega_\theta = 0$. With $\gamma^\varphi = \sigma_2/\sin\theta$: $\sum_\mu\gamma^\mu\Omega_\mu = \frac{\sigma_2}{\sin\theta}\big(-\frac i2\cos\theta\,\sigma_3\big) = -\frac{i\cot\theta}{2}\sigma_2\sigma_3 = -\frac{i\cot\theta}{2}\,i\sigma_1 = \frac{\cot\theta}{2}\sigma_1$. Divergence form with $\sqrt{\lvert g\rvert} = \sin\theta$: $\frac{1}{2\sin\theta}\big(\partial_\theta(\sin\theta\,\sigma_1) + \partial_\varphi(\sin\theta\cdot\sigma_2/\sin\theta)\big) = \frac{\cos\theta}{2\sin\theta}\sigma_1$, the same. Finally $F_{\theta\varphi} = \partial_\theta\Omega_\varphi - \partial_\varphi\Omega_\theta + [\Omega_\theta, \Omega_\varphi] = \partial_\theta\big(-\frac i2\cos\theta\,\sigma_3\big) = \frac i2\sin\theta\,\sigma_3 \neq 0$. The sphere is curved: unlike the polar plane of Section 6.5, here no change of frame can remove the spin connection (Section 6.17). (Check with the theorem of Section 6.17: $R^\theta{}_{\varphi\theta\varphi} = \sin^2\theta$ for the unit sphere, so $R_{01\theta\varphi} = \eta_{00}f_\theta R^\theta{}_{\varphi\theta\varphi}/f_\varphi = \sin\theta$ and $\frac12(R_{01\theta\varphi}S^{01} + R_{10\theta\varphi}S^{10}) = \sin\theta\,S^{01} = \frac i2\sin\theta\,\sigma_3$.)

**Exercise 2 (an extra time by hand).** Compute $\omega_{x6\,ab}$ for the author's metric with the formula of Section 6.6 and then $\gamma^{x6}\Omega_{x6}$, without looking at Section 6.8. Why is the coefficient of $\gamma^{(x4)}$ negative?

*Answer.* $f_6 = e^{-a_4}s$, so $\partial_4f_6 = -a_4'f_6$ and $\partial_8f_6 = H\cot z\,f_6$. With $\omega_{\mu\,\mu b} = \eta_{\mu\mu}\partial_bf_\mu/f_b$ and $\eta_{66} = -1$: $\omega_{x6\,x6\,x4} = (-1)(-a_4'f_6)/1 = a_4'f_6$, hence $\omega_{x6\,x4\,x6} = -a_4'f_6$; and $\omega_{x6\,x6\,x8} = (-1)H\cot z\,f_6/\cot z = -Hf_6$. So $\Omega_{x6} = -f_6\big(a_4'S^{x4x6} + HS^{x6x8}\big)$ and $\gamma^{x6}\Omega_{x6} = \frac{\gamma^{(x6)}}{f_6}(-f_6)\big(\frac{a_4'}2\gamma^{(x4)}\gamma^{(x6)} + \frac H2\gamma^{(x6)}\gamma^{(x8)}\big) = -\frac{a_4'}2\gamma^{(x6)}\gamma^{(x4)}\gamma^{(x6)} - \frac H2\gamma^{(x6)}\gamma^{(x6)}\gamma^{(x8)}$. Since $\gamma^{(x6)}\gamma^{(x4)}\gamma^{(x6)} = -\gamma^{(x4)}(\gamma^{(x6)})^2 = \gamma^{(x4)}$ and $(\gamma^{(x6)})^2 = -1$, $\gamma^{x6}\Omega_{x6} = -\frac{a_4'}2\gamma^{(x4)} + \frac H2\gamma^{(x8)}$. The coefficient of $\gamma^{(x4)}$ is negative because the extra time shrinks ($\partial_4f_6 = -a_4'f_6$) while a 3-space direction grows; this is the sign that cancels the 3-space terms.

**Exercise 3 (a general deflation rate).** Replace the extra-time factors by $e^{-ka_4}s$ with a constant $k$ (the author's metric has $k = 1$, the negative control $k = -1$). Use the divergence form to find the coefficient of $\gamma^{(x4)}$ in $\sum_\mu\gamma^\mu\Omega_\mu$. For which $k$ does it vanish?

*Answer.* With $f_4 = 1$ the product of the other seven factors is the whole volume factor: $\sqrt{\lvert g\rvert} = e^{3a_4}s^3\cdot e^{-3ka_4}s^3\cdot\cot z = e^{3(1-k)a_4}\cos z$ ($s^6\cot z = \sin z\cot z = \cos z$). The time contribution of the divergence form is $\frac{1}{2\sqrt{\lvert g\rvert}}\partial_4\sqrt{\lvert g\rvert}\,\gamma^{(x4)} = \frac{3(1-k)a_4'e^{3(1-k)a_4}\cos z}{2e^{3(1-k)a_4}\cos z}\gamma^{(x4)} = \frac32(1-k)a_4'\gamma^{(x4)}$ (the chain rule). For $k = 1$ (the author's deflation) it is 0; for $k = -1$ it is $3a_4'$, the negative control of Section 6.10. It vanishes only for $k = 1$, exactly when the 7-volume does not change with time. (The hidden term is $3H$ for every $k$, because $\prod_{c\neq x8}f_c = e^{3(1-k)a_4}\sin z$ and the factor $e^{3(1-k)a_4}$ cancels in the division.)

**Exercise 4 (the boosted contraction in numbers).** Take $H = 1$, $b_0 = 0$ and the rate $\beta = 3$. Give the coefficients of $\gamma^{(x8)}$ and $\gamma^{(x4)}$ in $\gamma'^\mu\Omega'_\mu$ at $x_4 = 0$ and at $x_4 = \frac13$. Which rate $\beta$ gives $-3\gamma^{(x8)}$ at $x_4 = 0$?

*Answer.* By Section 6.16 the coefficients are $\frac{6 - \beta}{2}\cosh b$ and $-\frac{6 - \beta}{2}\sinh b$ with $b = \beta x_4$. Here $\frac{6-3}{2} = 1.5$. At $x_4 = 0$: $b = 0$, coefficients $1.5$ and $0$. At $x_4 = \frac13$: $b = 1$, $\cosh 1 = 1.5431$, $\sinh 1 = 1.1752$, so the coefficients are $1.5 \cdot 1.5431 = 2.3146$ and $-1.5 \cdot 1.1752 = -1.7628$. At $x_4 = 0$ the coefficient of $\gamma^{(x8)}$ is $\frac{6-\beta}{2}$, which equals $-3$ for $\beta = 12$. A frame can thus give the contraction any multiple of $\gamma^{(x8)}$ at one instant; the value is not a property of the metric.

**Exercise 5 (rescaling with a general power).** Let $\Psi = \sin^\alpha(z)\,\chi$ with a constant $\alpha$ in the diagonal vielbein. Show that $\sum_\mu\gamma^\mu D_\mu\Psi = \sin^\alpha z\,\big(\sum_\mu\gamma^\mu\partial_\mu\chi + 3H(2\alpha + 1)\gamma^{(x8)}\chi\big)$. Which $\alpha$ removes the term, and which leaves it unchanged?

*Answer.* By the product rule, and because only $x_8$ appears in $\sin^\alpha z$,

$$
\sum_\mu\gamma^\mu D_\mu(\sin^\alpha z\,\chi) = \sin^\alpha z\sum_\mu\gamma^\mu\partial_\mu\chi + \big(\gamma^{x8}\partial_8\sin^\alpha z + 3H\sin^\alpha z\,\gamma^{(x8)}\big)\chi .
$$

With $\gamma^{x8} = \tan z\,\gamma^{(x8)}$ and $\partial_8\sin^\alpha z = 6H\alpha\sin^{\alpha-1}z\cos z$ (the power rule and the chain rule),

$$
\tan z\,\partial_8\sin^\alpha z = \frac{\sin z}{\cos z}\,6H\alpha\sin^{\alpha-1}z\cos z = 6H\alpha\sin^\alpha z .
$$

The bracket is $(6H\alpha + 3H)\sin^\alpha z\,\gamma^{(x8)} = 3H(2\alpha + 1)\sin^\alpha z\,\gamma^{(x8)}$, which gives the formula. $\alpha = -\frac12$ removes the term (Section 6.18), and $\alpha = 0$ leaves it unchanged. This is the factor $3H(2\alpha + 1)$ that the record's exact solution family contains (`field-theory.json`, formula `exact_solutions`).

**Exercise 6 (mixed components).** Using $\omega_\mu{}^b{}_a = -\eta_{aa}\eta_{bb}\,\omega_\mu{}^a{}_b$ (Section 6.4), show that the mixed components of a time-time pair are antisymmetric and those of a boost pair symmetric. Then compute $\Omega^{nb}_{x2}$ and $\Omega^{nb}_{x7}$ for the author's metric.

*Answer.* For a time-time pair $\eta_{aa}\eta_{bb} = (-1)(-1) = +1$, so $\omega_\mu{}^b{}_a = -\omega_\mu{}^a{}_b$: antisymmetric. For a boost pair $\eta_{aa}\eta_{bb} = -1$, so $\omega_\mu{}^b{}_a = +\omega_\mu{}^a{}_b$: symmetric, and in $\frac12\sum_{a,b}\omega_\mu{}^a{}_bS^{ab}$ its two terms cancel because $S^{ba} = -S^{ab}$. For $x2$ the pair $(x2, x4)$ is a boost pair (deleted) and $(x2, x8)$ a space-space pair (kept): $\Omega^{nb}_{x2} = e^{a_4}s\,H\,S^{x2x8}$. For $x7$ the pair $(x4, x7)$ is time-time (sign reversed) and $(x7, x8)$ a boost pair (deleted): $\Omega^{nb}_{x7} = -\omega_{x7\,x4x7}S^{x4x7} = +e^{-a_4}s\,a_4'\,S^{x4x7}$.

**Exercise 7 (the hidden operator in numbers).** Take $p = q = 1$ (constant functions) and integrate the identity of Section 6.24 over the whole patch $0 \le x_8 \le \pi/(12H)$. Compare the left side with the boundary term for $c = 3H$ and for $c = \frac32H$.

*Answer.* With $p = q = 1$, $A_c1 = c$, so the left side is $\int\cos z\cdot2c\,dx_8 = 2c\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 = 2c\cdot\frac{1}{6H} = \frac{c}{3H}$ (the 7-volume integral of Chapter 3). The boundary term is $[\sin z\,p\,q]_{z=0}^{z=\pi/2} = 1 - 0 = 1$. For $c = 3H$ the left side is 1, equal to the boundary term: nothing else is left. For $c = \frac32H$ it is $\frac12$, and the difference $\frac12 - 1 = -\frac12$ is the integral of the leftover $-3H\cos z$, $-3H\cdot\frac{1}{6H} = -\frac12$, which no boundary term can absorb.

**Exercise 8 (which pairs break).** Without a computer, explain why $D^{nb}_{x1}\gamma^{x2} = 0$ although $\Omega^{nb}_{x1} \neq \Omega_{x1}$, and why the row $x8$ of figure 5 of Notebook 06c is white.

*Answer.* By Section 6.23, $D^{nb}_{x1}\gamma^{x2} = [\Omega^{nb}_{x1} - \Omega_{x1}, \gamma^{x2}] = -f_1a_4'[S^{x1x4}, \gamma^{(x2)}]/f_2$. By the vector rule $[S^{ab}, \gamma^c] = \eta^{bc}\gamma^a - \eta^{ac}\gamma^b$, which vanishes when $c$ is neither $a$ nor $b$; here $c = x2$ is neither $x1$ nor $x4$, so the commutator is zero. The row $x8$ is white because $\Omega_{x8} = 0$ (Section 6.6) and also $\Omega^{nb}_{x8} = 0$ (it is built from the same components, all zero for $\mu = x8$), so their difference vanishes and $D^{nb}_{x8}\gamma^\nu = D_{x8}\gamma^\nu = 0$ for every $\nu$.
